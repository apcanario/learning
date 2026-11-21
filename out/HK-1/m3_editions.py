"""HK-1 M3 · marketing-ai and the template edition (fieldnotes), built at the start commit and on the working tree.

  python3 -I out/HK-1/m3_editions.py /tmp/hk1m3
/tmp/hk1m3/start is `git archive 9447f39`, /tmp/hk1m3/now the working tree's tracked files (kit/academy left out); in each,
out/DEC-C/p_dec11_template.py recreated the template edition `fieldnotes`, then `build.py --edition marketing-ai` and
`--edition fieldnotes` ran. For every file of each edition: identical, or identical once the new shell CSS is swapped
for the start's and each Audit cadence cell replaced by a marker. The CSS is matched verbatim, or, where a brand inlines it without comments, as the one added rule. Reads only. Exit 1 on any unexplained difference."""
import difflib, pathlib, re, sys

R = pathlib.Path(sys.argv[1])
old_css = (R / 'start/kit/shell.css').read_text(encoding='utf-8')
new_css = (R / 'now/kit/shell.css').read_text(encoding='utf-8')
CELL = re.compile(r'(<tr><td>Audit cadence</td><td>[^<]*</td><td>)(.*?)(</td></tr>)', re.S)
TOPO = re.compile(r'<div class="topo"[^>]*>.*?</svg></div>', re.S)
bad = 0


def vbytes(h):   # verify.py's measure: the outerHTML, every self-closed element with its end tag
    return len(re.sub(r'<(\w+)([^<>]*?)/>', r'<\1\2></\1>', h).encode())


for ed in ('marketing-ai', 'fieldnotes'):
    a, b = R / 'start/kit/editions' / ed, R / 'now/kit/editions' / ed
    fa = {p.relative_to(a).as_posix() for p in a.rglob('*') if p.is_file()}
    fb = {p.relative_to(b).as_posix() for p in b.rglob('*') if p.is_file()}
    print(f'{ed}: {len(fa)} files at the start, {len(fb)} now; added {sorted(fb - fa)}, removed {sorted(fa - fb)}')
    bad += len(fa ^ fb)
    for rel in sorted(fa & fb):
        x, y = (a / rel).read_bytes(), (b / rel).read_bytes()
        if x == y:
            continue
        xs, ys = x.decode(), y.decode()
        why = []
        if ys.count(new_css) == 1 and xs.count(old_css) == 1:
            ys = ys.replace(new_css, old_css); why.append('P-DEC20 CSS')
        else:   # an edition whose brand inlines the CSS without its comments: the one rule, added, nothing removed
            xl, yl = xs.splitlines(True), ys.splitlines(True)
            ops = [o for o in difflib.SequenceMatcher(None, xl, yl, autojunk=False).get_opcodes() if o[0] != 'equal']
            ins = [l.strip() for t, i1, i2, j1, j2 in ops for l in yl[j1:j2] if l.strip()]
            if ops and all(t == 'insert' for t, *_ in ops) and ins == ['.panel.home>.hero.has-topo{min-height:380px}']:
                ys = ''.join(l for k, l in enumerate(yl) if not any(j1 <= k < j2 for _, _, _, j1, j2 in ops))
                why.append('P-DEC20 CSS (the rule alone, comments stripped by the brand)')
        cx, cy = CELL.findall(xs), CELL.findall(ys)
        if cx != cy:
            xs, ys = CELL.sub(r'\1CELL\3', xs), CELL.sub(r'\1CELL\3', ys)
            why.append(f'P-DEC21 Audit cadence cell x{len(cy)}')
        same = xs == ys
        bad += not same
        print(f'  {rel}: {"identical once " + " and ".join(why) + " are set aside" if same else "UNEXPLAINED difference (" + ", ".join(why) + ")"}')
        for c in sorted({c[1] for c in cy} | {c[1] for c in cx}):
            print('     cell:', c[:110])
    t = TOPO.search((b / 'index.html').read_text(encoding='utf-8')).group(0)
    t0 = TOPO.search((a / 'index.html').read_text(encoding='utf-8')).group(0)
    rings = re.findall(r'<svg class="topo-l topo-(\w+)".*?(?=<svg|$)', t, re.S)
    print(f'  hero layer: start {len(t0.encode()):,} B / {vbytes(t0):,} B as verify counts; now {len(t.encode()):,} / {vbytes(t):,}; '
          f'{"byte-identical" if t == t0 else "CHANGED"}; rises '
          + ', '.join(f'{l} {w} words {r} rings' for l, w, r in dict.fromkeys(re.findall(r'data-label="([^"]*)" data-words="(\d+)" data-rings="(\d+)"', t))))
    bad += t != t0
print('VERDICT:', 'PASS' if not bad else f'FAULT ({bad})')
sys.exit(1 if bad else 0)
