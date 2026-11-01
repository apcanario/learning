"""P71-3 (1 Nov 2026): where a history report lives. Since Greece and Rome moved to Markdown, a report is one file in
the vault, courses/<course>/<id>-<slug>.md (docs/method.md §7), and nothing in the kit holds its text: build.py,
epub.py, check.py, register.py, crosscheck.py, biblio.py and verify.py all read it through here.

  report_path(c, i)       the vault file of report i of history course c (None if it is not filed)
  report_ids(c)           every report id filed in the course's vault, in syllabus order where the syllabus has it
  report_html(c, i, draw) its fragment HTML (mdcourse.history_html): figures drawn, or as declarations with draw=False
"""
import pathlib, re

KIT = pathlib.Path(__file__).resolve().parent
REPO = KIT.parent


def folder(c):
    return REPO / c['vault']


def _key(i):
    return [int(x) for x in i.split('.')]


def report_path(c, i):
    hits = sorted(folder(c).glob(f'{i}-*.md'))
    return hits[0] if hits else None


def report_ids(c):
    ids = [m.group(1) for f in folder(c).glob('*.md') for m in [re.match(r'(\d+\.\d+)-', f.name)] if m]
    return sorted(ids, key=_key)


def report_html(c, i, draw=True):
    import mdcourse
    return mdcourse.history_html(report_path(c, i).read_text(encoding='utf-8'), draw=draw)
