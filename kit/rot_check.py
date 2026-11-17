"""Rot between sessions (P30-F11 and P30-F16, 17 Nov 2026; B4's findings F9, F11 and F16).

python3 kit/rot_check.py     prints every failure and warning; exit 1 on a failure, "rot check: OK" otherwise

verify.py runs check() and fails the build on any failure; warnings are printed and never fail. Needs no browser.
  1. the theme copy: kit/shell.css is design/theme.css, byte for byte (the build inlines shell.css)
  2. no live instruction names a retired thing (RETIRED below), in the files a chat is told to follow (LIVE below);
     records (changelogs, the backlog, audits, the vault, kit/archive, docs/archive) are not read
  3. staleness: every date in the index's "Staleness checks due" table that is past or within 30 days is a warning
The size of the Project's knowledge cannot be read from the repo; method.md §8 step 4 names the set that is kept.
"""
import pathlib, re, sys, datetime

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
RETIRED = ('python3 build_hub.py', 'personal-assistant Project', 'personal assistant', 'named `learning-project`',
           'due after B1', 'kit/BACKLOG.md`', 'kit/NEXT-SESSION.md', 'docs/handoffs/', 'check_page.py` run')
ALLOW = ('until 17 Nov 2026', 'once `kit/BACKLOG.md`', 'RETIRED')   # a line that says the thing is gone may name it
LIVE = ['SETUP.md', 'README.md', 'design/README.md', 'generator/README.md', 'kit/README.md', 'kit/next_prompt.py',
        'docs/method.md', 'docs/project-instructions.md', 'docs/public-courses.md', 'docs/sport-psychology-prompts.md']
MON = {m: i + 1 for i, m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split())}


def live_files():
    fs = [ROOT / f for f in LIVE]
    fs += sorted((ROOT / 'skills').glob('*/SKILL.md')) + sorted((ROOT / 'generator' / 'data').glob('*/hub.py'))
    return [f for f in fs if f.exists()]


def check(today=None):
    """(failures, warnings)."""
    fails, warns = [], []
    if (ROOT / 'design' / 'theme.css').read_bytes() != (R / 'shell.css').read_bytes():
        fails.append('kit/shell.css differs from design/theme.css: cp design/theme.css kit/shell.css, then rebuild')
    for f in live_files():
        for n, ln in enumerate(f.read_text(encoding='utf-8').splitlines(), 1):
            if any(a in ln for a in ALLOW):
                continue
            for t in RETIRED:
                if t in ln:
                    fails.append(f'{f.relative_to(ROOT)}:{n}: names a retired thing ({t!r})')
    today = today or datetime.date.today()
    ix = (ROOT / 'docs' / 'courses-index.md').read_text(encoding='utf-8')
    m = re.search(r'(?ms)^## Staleness checks due.*?(?=^## )', ix)
    for ln in (m.group(0).splitlines() if m else []):
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        d = re.fullmatch(r'(\d{1,2}) (\w{3}) (\d{4})', cells[-1]) if len(cells) >= 3 else None
        if d and d.group(2) in MON:
            due = datetime.date(int(d.group(3)), MON[d.group(2)], int(d.group(1)))
            if due <= today:
                warns.append(f'staleness check of {cells[0]} was due {cells[-1]}')
            elif (due - today).days <= 30:
                warns.append(f'staleness check of {cells[0]} is due {cells[-1]}, in {(due - today).days} days')
    return fails, warns


if __name__ == '__main__':
    f, w = check()
    print('\n'.join(['warn ' + x for x in w] + ['FAIL ' + x for x in f]) or 'rot check: OK')
    if w and not f:
        print('rot check: OK')
    sys.exit(1 if f else 0)
