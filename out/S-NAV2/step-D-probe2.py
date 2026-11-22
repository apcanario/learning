"""The home, What's new, topography, tiles, area and motion passes of verify.py main() at given viewports.
python3 probe2.py [--edition NAME] [--vp name,w,h,mobile ...] [--motion]"""
import sys, time
args = sys.argv[1:]
vps = [tuple(int(x) if x.isdigit() else (x == 'True' if x in ('True', 'False') else x) for x in a.split(',')) for i, a in enumerate(args) if i and args[i - 1] == '--vp']
motion = '--motion' in args
sys.argv = sys.argv[:1] + (['--edition', args[args.index('--edition') + 1]] if '--edition' in args else [])
import pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'kit'))
import verify as V
from playwright.sync_api import sync_playwright
vps = vps or V.NEW_VIEWPORTS
fails, errors = [], []
EXPECT = V.home_expect()
TOPO_ALL = [x for x in V.SAMPLE if x in V.HIST_HOMES or x in EXPECT['courses']] + V.AREA_IDS + ['new']
NONE_ALL = [x for x in ('changelog', 'backlog', 'viz-examples') if (x != 'viz-examples' or 'figures' not in V.OMIT) and (x not in ('changelog', 'backlog') or x not in V.OMIT)]
TOPO_PAGES, NONE_PAGES = V.SCOPE.only(TOPO_ALL), V.SCOPE.only(NONE_ALL)
T = time.time()
with sync_playwright() as p:
    br = p.chromium.launch()
    for name, w, h, mobile in vps:
        t = time.time()
        ctx, pg, _ = V.new_page(p, br, errors, name, w, h, mobile)
        V.check_home(pg, name, fails, EXPECT); V.check_new(pg, name, fails, EXPECT)
        pg.evaluate(f"localStorage.setItem('{V.THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
        V.check_home(pg, name + ' light', fails, EXPECT)
        ctx.close()
        t1 = time.time()
        ctx, pg, _ = V.new_page(p, br, errors, name + ' pages', w, h, mobile)
        reads = pg.evaluate("""() => { const seen = {}, out = []; document.querySelectorAll('.panel[data-kind="report"]').forEach(p => { const c = p.getAttribute('data-ctx'); if (!seen[c]) { seen[c] = 1; out.push(p.id); } }); return out; }""")
        for theme in ('dark', 'light'):
            if theme == 'light': pg.evaluate(f"localStorage.setItem('{V.THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
            pg.evaluate("location.hash = 'home'"); V.ready(pg); pg.wait_for_timeout(120)
            pg.evaluate(f"document.querySelectorAll({V.PLANNED_SEL!r}).forEach(d => d.open = true)"); pg.wait_for_timeout(60)
            V.check_topo(pg, 'home', f'{name} {theme}', fails, EXPECT); V.check_tiles(pg, 'home', f'{name} {theme}', fails, EXPECT)
            pg.evaluate(f"document.querySelectorAll({V.PLANNED_SEL!r}).forEach(d => d.open = false)")
            for pid in TOPO_PAGES + NONE_PAGES + V.SCOPE.only(reads):
                pg.evaluate(f"location.hash = '{pid}'"); V.ready(pg); pg.wait_for_timeout(120)
                if pid in V.AREA_IDS:
                    V.check_area(pg, pid, f'{name} {theme}', fails, EXPECT)
                    pg.evaluate(f"document.querySelectorAll({V.PLANNED_SEL!r}).forEach(d => d.open = true)"); pg.wait_for_timeout(60)
                tp = V.check_topo(pg, pid, f'{name} {theme}', fails, EXPECT)
                if pid in TOPO_PAGES and pid != 'new':
                    pg.evaluate(f"document.querySelectorAll('#{pid} details[data-mods]').forEach((d, k) => d.open = k < 2)"); pg.wait_for_timeout(60)
                    V.check_tiles(pg, pid, f'{name} {theme}', fails, EXPECT)
                    pg.evaluate(f"document.querySelectorAll('#{pid} details[data-mods]').forEach(d => d.open = false)")
                    if pid in V.AREA_IDS: pg.evaluate(f"document.querySelectorAll({V.PLANNED_SEL!r}).forEach(d => d.open = false)")
        ctx.close()
        t2 = time.time()
        if motion:
            ctx, pg, _ = V.new_page(p, br, errors, name + ' motion', w, h, mobile, motion=True)
            pg.evaluate("location.hash = 'new'"); V.ready(pg); pg.evaluate("location.hash = 'home'"); V.ready(pg); pg.wait_for_timeout(200)
            V.check_topo(pg, 'home', f'{name} motion', fails, EXPECT, motion=True)
            V.check_home(pg, name + ' motion', fails, EXPECT, motion=True)
            V.check_harea(pg, name + ' motion', fails)
            ctx.close()
        print(f'== {name}: home {t1 - t:.0f} s, pages {t2 - t1:.0f} s, motion {time.time() - t2:.0f} s; {len(TOPO_PAGES + NONE_PAGES)} pages + {len(reads)} reading', flush=True)
    br.close()
errs = [e for e in errors if 'fonts.g' not in e]
if errs: fails.append('console errors: ' + ' | '.join(errs[:5]))
for x in fails: print('FAIL', x[:600])
print(f'PROBE2 {"PASSED" if not fails else str(len(fails)) + " FAULTS"} in {time.time() - T:.0f} s')
