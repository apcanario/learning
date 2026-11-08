"""P95 (8 Nov 2026) · shots of the pages that show an object relief (design/outlines/uses.json), for the second fresh
checker and for Pedro: the top of each page (the header with its scope line, relief and caption, and the section bar
under it) at 320, 360, 390, 430, 768 and 1280 px, dark and light, at rest (reduced motion); and, at 390 px dark with
motion allowed, the relief alone at the five poses of the turn (0, .25, .5, .75, 1 of the sweep) at the top of the
breath, as verify.py poses it. Every shot is under 8,000 px tall.

    python3 p95_shots.py <folder>                                  every mapped page
    python3 p95_shots.py <folder> m11 read-a4 --widths 390,1280      (P96) a sample of pages, at some of the widths
"""
import functools, json, pathlib, sys, threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

R = pathlib.Path(__file__).resolve().parent
SITE = R / 'academy'
USES = json.loads((R.parent / 'design' / 'outlines' / 'uses.json').read_text())['uses']
WIDTHS = [320, 360, 390, 430, 768, 1280]
POSE_JS = r"""([p, sel]) => { const t = document.querySelector(sel), sv = t.querySelector('svg');
  const cs = getComputedStyle(document.documentElement), cyc = parseFloat(cs.getPropertyValue('--topo-cycle')) * 1000, bt = parseFloat(cs.getPropertyValue('--topo-breath')) * 1000;
  document.getAnimations().filter(a => a.effect && a.effect.target === sv).forEach(a => { a.pause();
    if (a.animationName === 'topo-turn') { const d = a.effect.getTiming().delay; let x = p * cyc + d; if (x < 0) x = 2 * cyc - p * cyc + d; a.currentTime = x; }
    else { let x = a.effect.getTiming().delay + .9999 * bt; if (x < 0) x += 2 * bt; a.currentTime = x; } }); }"""


def font_file(route):
    f = R / 'fonts' / route.request.url.rsplit('/', 1)[1]
    if f.suffix == '.woff2' and f.exists():
        route.fulfill(status=200, content_type='font/woff2', body=f.read_bytes(), headers={'Access-Control-Allow-Origin': '*'})
    else:
        route.abort()


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def main():
    from playwright.sync_api import sync_playwright
    args = sys.argv[1:]
    out = pathlib.Path(args.pop(0))
    widths = WIDTHS
    if '--widths' in args:
        i = args.index('--widths'); widths = [int(x) for x in args[i + 1].split(',')]; del args[i:i + 2]
    uses = {p: USES[p] for p in args} if args else USES
    out.mkdir(parents=True, exist_ok=True)
    srv = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(SITE)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{srv.server_port}/index.html'
    fonts = R / 'fonts'
    css = (fonts / 'fonts.css').read_text()
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        for w in widths:
            for theme in ('dark', 'light'):
                for motion in ((False, True) if (w == 390 and theme == 'dark') else (False,)):
                    ctx = br.new_context(viewport=dict(width=w, height=900), device_scale_factor=2 if w < 768 else 1, is_mobile=w < 768,
                                         has_touch=w < 768, color_scheme=theme, reduced_motion='no-preference' if motion else 'reduce')
                    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=css))
                    ctx.route('**/fonts.gstatic.com/**', font_file)   # the vendored theme fonts, as verify.py serves them
                    pg = ctx.new_page()
                    pg.goto(url + '#home'); pg.wait_for_timeout(300)
                    if theme == 'light':
                        pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                    for pid, oid in uses.items():
                        pg.evaluate(f"location.hash = '{pid}'"); pg.wait_for_timeout(900)
                        pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(100)
                        if not motion:
                            b = pg.evaluate(f"(() => {{ const r = document.querySelector('#{pid} .stepbar').getBoundingClientRect(); return Math.ceil(r.bottom + scrollY + 24); }})()")
                            pg.screenshot(path=str(out / f'{pid}-{w}-{theme}.png'), full_page=True, clip=dict(x=0, y=0, width=w, height=min(b, 3900)))
                        else:
                            sel = f'#{pid} .topo.relief'
                            for p in (0, .25, .5, .75, 1):
                                pg.evaluate(POSE_JS, [p, sel]); pg.wait_for_timeout(60)
                                pg.locator(sel).screenshot(path=str(out / f'{pid}-pose{p:g}.png'))
                    ctx.close()
        br.close()
    srv.shutdown()
    print(f'{len(list(out.glob("*.png")))} shots in {out}')


if __name__ == '__main__':
    main()
