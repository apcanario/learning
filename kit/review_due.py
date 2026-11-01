"""Fable review alert: is the four-module review due?

Pedro's cadence (decided 28 October 2026, S3; method.md §6): the Fable 5.1 review runs after every
four Personal Mythology content reports written since the last review, Greece and Rome pooled. A
module counts when its provenance.json entry does not mention Fable 5.1 (it is unreviewed) and it is
not one of the reports the last review carried over (`review_mark` in provenance.json: the date of
the last review and the flagged reports it left to a row of their own, e.g. the six Greek reports of
S4). The audit unit's modules never count. Batches cut across syllabus units (kit/BACKLOG.md).

When a review has run, its session sets `review_mark`: the date, and as `carried` any report still
flagged that the review hands to another row (empty when it clears the batch). The reviewed reports
mention Fable 5.1 and drop out of the count by themselves.

    python3 review_due.py            prints the status line; exit code 2 when a review is due
    from review_due import status    status() -> (due: bool, line: str)

register.py prints the line after every registration, build.py after every build and at the head
of FABLE-REVIEW.md, so the alert surfaces in any writing session without anyone remembering to look.
"""
import sys, json, re, pathlib
from courses import HISTORY as COURSES

R = pathlib.Path(__file__).resolve().parent
EVERY = 4


def _order(c):
    """The course's module ids in syllabus order, the audit unit left out."""
    syl = (R / c['syllabus']).read_text()
    return [i for i in re.findall(r'data-id="([\d.]+)"', syl) if i.split('.')[0] != str(c['audit_unit'])]


def status():
    prov = json.load(open(R / 'provenance.json'))
    mark = prov.get('review_mark', {})
    carried = set(mark.get('carried', []))
    new = []
    for c in COURSES:
        p = prov.get(c['id'], {})
        for i in _order(c):
            if i in p and 'Fable 5.1' not in p[i] and f'{c["id"]} {i}' not in carried:
                new.append(f'{c["short"]} {i}')
    n = len(new)
    since = f' (last review {mark["date"]})' if mark.get('date') else ''
    if n >= EVERY:
        return True, (f'FABLE REVIEW DUE: {n} modules written since the last review{since}: {", ".join(new)}. '
                      f'Stop writing; the review runs on Fable 5.1 (method.md §6 claim-sample prompt; '
                      f'a module failing more than one claim in ten gets the scorecard audit, audits/AUDIT-BRIEF.md).')
    return False, (f'Fable review: {n} of {EVERY} modules written since the last review'
                   + (f' ({", ".join(new)})' if new else '') + '.')


if __name__ == '__main__':
    due, line = status()
    print(line)
    sys.exit(2 if due else 0)
