import sys, re, html, pathlib, tomllib
root = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(root / 'kit'))
import viz
src = (root / 'kit/build.py').read_text()
a = src.index('COURSE_TOPO = ['); b = src.index('\ndef hero_layer(')
seg = src[a:b]
_TT = (root / 'design/theme.css').read_text()
g = dict(re=re, html=html, viz=viz, _TT=_TT, ct_lattice=None, ct_ridge=None)
exec(seg, g)
brand = tomllib.loads((root / 'brands/workbench.toml').read_text())
viz.set_metrics(brand)
lede = 'word ' * 120
t = g['course_topo'](lede)
print('extra lines:', g['lede_lines'](lede, viz._ADV['sans']) - g['lede_lines'](lede, viz._DEFAULT[0]['sans']))
print('same object:', t is g['COURSE_TOPO'])
for sp in t: print(sp['name'], sp['box'], sp['view'], sp.get('small'))
