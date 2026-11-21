"""P-DEC6 proof: every file baseline.py --check lists as changed differs from its old bytes only by the bibliography path.

usage: python3 p-dec6-proof.py CHECK_OUTPUT OLD_SNAPSHOT_DIR
CHECK_OUTPUT: the stdout of `python3 kit/baseline.py --check` after the change.
OLD_SNAPSHOT_DIR: copies of every non-site output taken before the change (paths as in kit/baseline.json, '../' as 'UP/').
For each changed file: map the new text back (new path -> old path, and the README's one sentence) and require byte equality
with the old copy (BIBLIO-BRIEF.md, edited by hand, has its three edits mapped back); also require that no changed file is under academy/ and that no greece file changed.
"""
import pathlib, re, sys

K = pathlib.Path(__file__).resolve().parents[2] / 'kit'
check, old = pathlib.Path(sys.argv[1]).read_text().splitlines(), pathlib.Path(sys.argv[2])
changed = [l.split(' changed ', 1)[1] for l in check if l.startswith('academy: changed ')]
other = [l for l in check if re.match(r'\w+: (added|removed|changed) ', l) and not l.startswith('academy: changed ')]
bad = []
if other: bad.append(f'differences outside academy-edition changes: {other}')
site = [p for p in changed if p.startswith('academy/')]
if site: bad.append(f'site files changed: {site}')
COURSE = re.compile(r'`courses/([a-z-]+)/bibliography/')
for p in changed:
    new = (K / p).read_text()
    back = COURSE.sub(r'`bibliography/\1/', new)
    if p == 'bibliography/BIBLIO-BRIEF.md':   # the hand-edited brief: its three edits mapped back
        back = new.replace(", except `courses/<course>/bibliography/`, which is from the repo root (the folder's place since S-DEC5, 20 Nov 2026).", '.')
        back = back.replace('`courses/<course>/bibliography/', '`KIT/bibliography/<course>/')
    if p == 'bibliography/README.md':
        back = back.replace('(`courses/<course>/bibliography/unit-<n>.md`)', '(`<course>/unit-<n>.md`)')
    was = (old / p.replace('../', 'UP/')).read_bytes()
    n = len(COURSE.findall(new)) + new.count('courses/<course>/bibliography/')
    ok = back.encode() == was and n > 0
    print(f"{'ok  ' if ok else 'FAIL'} {p}  ({n} path mention{'s' if n != 1 else ''} rewritten)")
    if not ok: bad.append(p)
print(f'{len(changed)} changed files; academy/ site files among them: {len(site)}; other editions differing: {len(other)}')
print('PROOF PASSED' if not bad else f'PROOF FAILED: {bad}')
sys.exit(1 if bad else 0)
