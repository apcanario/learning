"""P-DEC15: after `kit/baseline.py --check`, prove (1) P-DEC8's 4 academy files and academy's and greece's What's new
(new.html) carry the sha256 recorded before the change (out/DEC-C/p_dec15_sha-before.txt), (2) academy's new.html
equals HEAD's committed bytes, and (3) marketing-ai built before and after differs in new.html only.

  python3 out/DEC-C/p_dec15_check.py <marketing-ai before dir> <marketing-ai after dir>
"""
import hashlib, pathlib, subprocess, sys
R = pathlib.Path('/home/claude/learning')
ok = True
for line in (R / 'out/DEC-C/p_dec15_sha-before.txt').read_text().splitlines():
    h, p = line.split(maxsplit=1)
    now = hashlib.sha256((R / p).read_bytes()).hexdigest()
    print(f'{"same" if now == h else "DIFFERS"}  {p}'); ok &= now == h
head = subprocess.run(['git', 'show', 'HEAD:kit/academy/new.html'], cwd=R, capture_output=True).stdout
same = head == (R / 'kit/academy/new.html').read_bytes()
print(f'{"same" if same else "DIFFERS"}  kit/academy/new.html against HEAD'); ok &= same
a, b = map(pathlib.Path, sys.argv[1:3])
fa = {p.relative_to(a) for p in a.rglob('*') if p.is_file()}
fb = {p.relative_to(b) for p in b.rglob('*') if p.is_file()}
diff = sorted(str(p) for p in fa & fb if (a / p).read_bytes() != (b / p).read_bytes())
print(f'marketing-ai: {len(fa)} files before, {len(fb)} after, added {sorted(map(str, fb - fa))}, removed {sorted(map(str, fa - fb))}, differ {diff}')
ok &= diff == ['new.html'] and fa == fb
print('P-DEC15 CHECK', 'PASSED' if ok else 'FAILED')

# kit/README.md (a manifest output, hand-edited prose): differs from HEAD only by the P-DEC15 phrase
OLD = "a contour every 14,000 words, `NEW_INTERVAL`, each day"
NEW = "a contour every 11,000 words, `NEW_INTERVAL`, or in an edition whose largest day is under 110,000 words a tenth of that day, `new_interval`, so its largest day also stands 10 levels (P-DEC15), each day"
cur = (R / 'kit/README.md').read_text(encoding='utf-8')
headr = subprocess.run(['git', 'show', 'HEAD:kit/README.md'], cwd=R, capture_output=True, text=True).stdout
rd = cur.count(NEW) == 1 and cur.replace(NEW, OLD) == headr
print(f'kit/README.md: {"differs from HEAD only by the P-DEC15 phrase" if rd else "DIFFERS BEYOND THE PHRASE"}')
print('P-DEC15 README CHECK', 'PASSED' if rd else 'FAILED')
