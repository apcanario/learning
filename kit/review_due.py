"""Fable review alert: is a sample-first review due?

Pedro's cadence (27 October 2026): the sample-first Fable review runs at the end of every four
written units of any course, on the reports written since the last review. A unit counts as
written when every content module in it has a report; it counts as unreviewed while any report
in it is flagged (its provenance.json entry does not mention Fable 5.1). Both courses pool.

    python3 review_due.py            prints the status line; exit code 2 when a review is due
    from review_due import status    status() -> (due: bool, line: str)

register.py prints the line after every registration and build.py after every build, so the
alert surfaces in any writing session without anyone remembering to look.
"""
import sys, json, re, pathlib
from courses import HISTORY as COURSES

R = pathlib.Path(__file__).resolve().parent
EVERY = 4


def status():
    prov = json.load(open(R / 'provenance.json'))
    done, partial = [], []
    for c in COURSES:
        syl = (R / c['syllabus']).read_text()
        units = {}
        for i in re.findall(r'data-id="([\d.]+)"', syl):
            u = i.split('.')[0]
            if u != str(c['audit_unit']):
                units.setdefault(u, []).append(i)
        p = prov.get(c['id'], {})
        for u, mods in units.items():
            written = [i for i in mods if i in p]
            flagged = [i for i in written if 'Fable 5.1' not in p[i]]
            if not flagged:
                continue
            (done if len(written) == len(mods) else partial).append(f'{c["short"]} {u}')
    n = len(done)
    tail = f'; in progress: {", ".join(partial)}' if partial else ''
    if n >= EVERY:
        line = f'FABLE REVIEW DUE: {n} units written since the last review ({", ".join(done)}){tail}. Stop writing and run NEXT-SESSION.md (sample-first review) on Fable 5.1.'
        return True, line
    line = f'Fable review: {n} of {EVERY} units written since the last review' + (f' ({", ".join(done)})' if done else '') + tail + '.'
    return False, line


if __name__ == '__main__':
    due, line = status()
    print(line)
    sys.exit(2 if due else 0)
