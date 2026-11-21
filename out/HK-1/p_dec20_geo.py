# P-DEC20: as out/DEC-C/p_dec11_geo.py, but with the band a frame Wf x Hf shows exactly: the layer's overscan (--ox, --oy
# in theme.css: 100cqh|cqw * sin(turn) / 2 + 1px), slice scaling, the fade over the last 10%; the wide layout (desktop,
# Wf 980 at 1280 px) or the tall one (tablet, Wf 768 at 768 px). n equal rises of 1,200 words, placed by build.py's ct_fit.
#   python3 out/HK-1/p_dec20_geo.py kit <Hf> [Wf=980] [N=25] [wide|tall]
import ast, sys, math, pathlib
kit = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(kit))
import viz
src = (kit/'build.py').read_text(); tree = ast.parse(src)
want = {'ct_lattice','ct_fit','turned_inside','_TT','TOPO_TURN','TOPO_GROW','COURSE_TOPO'}
body = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in want) or (isinstance(n, ast.Assign) and any(getattr(t,'id',None) in want or (isinstance(t, ast.Tuple) and any(getattr(e,'id',None) in want for e in t.elts)) for t in n.targets))]
g = {'math': math, 're': __import__('re'), 'pathlib': pathlib, 'viz': viz, '__file__': str(kit/'build.py')}
exec(compile(ast.Module(body=body, type_ignores=[]), 'b', 'exec'), g)
Hf = float(sys.argv[2]); Wf = float(sys.argv[3]) if len(sys.argv) > 3 else 980; N = int(sys.argv[4]) if len(sys.argv) > 4 else 25
t = math.sin(math.radians(g['TOPO_TURN']))
ox, oy = Hf * t / 2 + 1, Wf * t / 2 + 1
Ws, Hs = Wf + 2 * ox, Hf + 2 * oy
LN0 = sys.argv[5] if len(sys.argv) > 5 else 'wide'; LH0 = 1000 if LN0 == 'tall' else 500
s = max(Ws / 1000, Hs / LH0)
u = lambda yf: (yf + oy - (Hs - LH0 * s) / 2) / s / LH0
v = lambda xf: (xf + ox - (Ws - 1000 * s) / 2) / s / 1000
band = (v(0), u(0), v(Wf), u(.9 * Hf))
print(f'Hf {Hf} Wf {Wf}: band x {band[0]:.4f}..{band[2]:.4f} y {band[1]:.4f}..{band[3]:.4f}; layout {LN0}')
fails = []
for n in range(1, N):
    rises = [dict(label=f'U{k}', tone=3, words=1200) for k in range(n)]
    lays = g['ct_fit'](rises, 1200/5.5, g['COURSE_TOPO'])
    LN = sys.argv[5] if len(sys.argv) > 5 else 'wide'; wide = [l for l in lays if l['name']==LN][0]; LW, LH = wide['width'], wide['height']
    rr = viz.contours_rings(dict(kind='contours', interval=1200/5.5, rises=rises, layouts=[wide]))[LN]
    if not all(g['turned_inside'](b, LW, LH, view=band) for *_, b in rr): fails.append(n)
print('fail n:', fails or 'none')
