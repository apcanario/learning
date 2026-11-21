import ast, sys, math, pathlib
kit = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(kit))
import viz
src = (kit/'build.py').read_text(); tree = ast.parse(src)
want = {'ct_lattice','ct_fit','turned_inside','_TT','TOPO_TURN','COURSE_TOPO'}
body = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in want) or (isinstance(n, ast.Assign) and any(getattr(t,'id',None) in want or (isinstance(t, ast.Tuple) and any(getattr(e,'id',None) in want for e in t.elts)) for t in n.targets))]
g = {'math': math, 're': __import__('re'), 'pathlib': pathlib, 'viz': viz, '__file__': str(kit/'build.py')}
exec(compile(ast.Module(body=body, type_ignores=[]), 'b', 'exec'), g)
H_f = float(sys.argv[2]) if len(sys.argv) > 2 else 347
# visible band of the wide layout (1000x500 slice in a ~1000-wide svg): y .5 +- H_f/1000, fade over the last 10%
y0 = .5 - H_f / 1000; y1 = y0 + .9 * (H_f / 500)
for n in range(1, 8):
    rises = [dict(label=f'U{k}', tone=3, words=1200) for k in range(n)]
    lays = g['ct_fit'](rises, 1200/5.5, g['COURSE_TOPO'])
    wide = [l for l in lays if l['name']=='wide'][0]
    rr = viz.contours_rings(dict(kind='contours', interval=1200/5.5, rises=rises, layouts=[wide]))['wide']
    ok = all(g['turned_inside'](b, 1000, 500, view=(.04, y0, .96, y1)) for *_, b in rr)
    print(n, 'spread', wide['spread'], 'inside a', H_f, 'px hero band:', ok)
