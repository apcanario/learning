"""P-DEC11: which course homes of an edition have two or fewer rises (the hero layouts P-DEC11 changes).

  python3 out/DEC-C/p_dec11_rises.py [<repo-root>] [<edition>]

From the course data (markdown courses: kit/pack.py, one home per [[pack.courses]], one rise per unit, a layer only when
a unit is written) and, as a cross-check, from the built site (each <course>/home.html: the rises of its wide layout).
History courses are counted from the built site only (their rises come from the syllabus the build parses).
"""
import pathlib, re, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/learning').resolve()
edition = sys.argv[2] if len(sys.argv) > 2 else 'academy'
sys.path.insert(0, str(root / 'kit'))
import courses, pack  # noqa: E402

ed = courses.EDITIONS[edition]
site = root / 'kit' / ed['site']
held = [c for c in courses.COURSES if ed['courses'] is None or c['id'] in ed['courses']]
rows, small = [], []
for c in held:
    if c['family'] == 'markdown':
        P = pack.load(c)
        for sc in P.COURSES:
            units = [u[0] if isinstance(u, (list, tuple)) else u['code'] for u in sc['units']]
            written = {re.search(r'^code: (\S+)', f.read_text(), re.M).group(1) for f in (root / c['vault']).glob('*.md')
                       if re.search(r'^code: (\S+)', f.read_text(), re.M)}
            rows.append(('data', c['id'], sc['key'], len(units), any(u in written for u in units)))
for f in sorted(site.glob('*/home.html')):
    t = f.read_text()
    m = re.search(r'<svg class="topo-l topo-wide".*?</svg>', t, re.S)
    if not m:
        rows.append(('built', f.parent.name, '-', 0, False))
        continue
    n = len(re.findall(r'<g class="ct-(?:rise|plan)[" ]', m.group(0)))
    rows.append(('built', f.parent.name, '-', n, True))
for r in rows:
    print(f'{r[0]:5}  {r[1]:28} {r[2]:4} rises {r[3]:3}  layer {"yes" if r[4] else "no"}' + ('   <= 2' if r[4] and r[3] <= 2 else ''))
    if r[4] and r[3] <= 2:
        small.append(r)
nd, nb = sum(r[0] == 'data' for r in small), sum(r[0] == 'built' for r in small)
print(f'course homes with a hero layer of two or fewer rises in {edition}: {nb} in the built site, {nd} in the markdown course data'
      + ('' if small else ' (none)'))
