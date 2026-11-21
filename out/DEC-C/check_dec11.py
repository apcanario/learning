"""P-DEC11 check: after the change, the built academy (kit/academy, kit/README.md, kit/bibliography, the history
bibliographies) and greece (kit/editions/greece) are byte-identical to the sha256 list taken before it, and
`kit/baseline.py --check` (its saved output) lists only P-DEC8's 4 files (out/DEC-C/expected-P-DEC11.md). Exit 1 on any
other difference.

  python3 out/DEC-C/check_dec11.py <sha-before.txt> <baseline-check.log>
    sha-before.txt: `sha256sum` lines over those roots, paths relative to kit/, taken before the change
"""
import hashlib, os, pathlib, re, sys

K = pathlib.Path('/home/claude/learning/kit')
P_DEC8 = {'academy/building-with-ai-bw/built.html', 'academy/sport-psychology-sp/built.html',
          'academy/supply-chain-execution-sce/built.html', 'academy/ux-ia/built.html'}
EXPECTED_MORE = set()   # expected-P-DEC11.md: no course home of academy or greece has two or fewer rises

before = {}
for line in pathlib.Path(sys.argv[1]).read_text().splitlines():
    h, p = line.split(None, 1)
    before[p.strip()] = h
roots = ['academy', 'editions/greece', 'README.md', 'bibliography', '../courses/greece/bibliography', '../courses/rome/bibliography']
after = {}
for r in roots:
    rp = K / r
    for f in ([rp] if rp.is_file() else sorted(x for x in rp.rglob('*') if x.is_file())):
        after[os.path.relpath(f, K)] = hashlib.sha256(f.read_bytes()).hexdigest()
fails = []
for k in sorted(set(before) | set(after)):
    if k not in before or k not in after:
        fails.append(f'{k}: {"added" if k not in before else "removed"}')
    elif before[k] != after[k] and k not in EXPECTED_MORE:
        fails.append(f'{k}: differs from the post-P-DEC8 bytes')
print(f'bytes: {len(after)} files compared with the post-P-DEC8 state, {len(fails)} differ')
log = pathlib.Path(sys.argv[2]).read_text()
listed = set(re.findall(r'^academy: changed (\S+)$', log, re.M)) | set(re.findall(r'^greece: changed (\S+)$', log, re.M))
other = re.findall(r'^\w[\w-]*: (?:added|removed) (\S+)$', log, re.M)
if listed != P_DEC8 | EXPECTED_MORE:
    fails.append(f'baseline --check lists {sorted(listed)}, expected {sorted(P_DEC8 | EXPECTED_MORE)}')
if other:
    fails.append(f'baseline --check lists added or removed files {other}')
if not re.search(r'^greece: \d+ files, 0 differ$', log, re.M):
    fails.append('baseline --check: greece does not report 0 differ')
print(f'baseline --check: {len(listed)} changed, all P-DEC8\'s 4: {listed == P_DEC8}')
for f in fails:
    print('FAIL', f)
print('P-DEC11 check: ' + ('PASSED (only P-DEC8\'s 4 files differ from the manifest; each unchanged by this row)' if not fails else f'{len(fails)} FAIL'))
sys.exit(1 if fails else 0)
