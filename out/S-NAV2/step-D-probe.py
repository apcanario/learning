"""Run S-NAV2 step D's new checks alone: python3 probe.py [--edition NAME] [--only a,b,...]"""
import sys, time
only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None
sys.argv = sys.argv[:1] + (['--edition', sys.argv[sys.argv.index('--edition') + 1]] if '--edition' in sys.argv else [])
import pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'kit'))
import verify as V
from playwright.sync_api import sync_playwright
fails = []
with sync_playwright() as p:
    br = p.chromium.launch()
    steps = [('nav1024', lambda: V.check_nav(br, fails, 1024, 768)), ('nav1920', lambda: V.check_nav(br, fails, 1920, 1080)),
             ('nav1280', lambda: V.check_nav(br, fails, 1280, 800)),
             ('layouts', lambda: V.check_layouts(br, fails)), ('frames', lambda: V.check_frames(br, fails)),
             ('phone', lambda: V.check_phone_identity(br, fails)), ('webkit', lambda: V.check_webkit(p, fails))]
    for name, f in steps:
        if only and name not in only: continue
        t = time.time(); n = len(fails); f()
        print(f'== {name}: {time.time() - t:.0f} s, {len(fails) - n} faults', flush=True)
    br.close()
for x in fails: print('FAIL', x[:700])
print('PROBE', 'PASSED' if not fails else f'{len(fails)} FAULTS')
