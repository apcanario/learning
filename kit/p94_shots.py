"""P94 (8 Nov 2026): the before and after shots of three reading pages (Greece 6.1, Rome 1.1, Information architecture
IA1), and, after, each section separator cut out of its page.

  python3 p94_shots.py before            the start of each page at 390 and 1280 px, dark and light -> reviews/p94/before/
  python3 p94_shots.py after             the same -> reviews/p94/after/, and every separator of each page at 320, 390,
                                         768 and 1280 px, dark and light, cut with the end of the text above it and the
                                         next and previous below -> reviews/p94/after/cuts/
  python3 p94_shots.py cuts DIR PAGE...  the cuts of other pages into DIR (the fresh checker's folder)

The site is served from academy/ (the build), the fonts from the vendored copy, as verify.py does; reduced motion, so
every drawing stands at rest."""
import sys, pathlib, threading, functools
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

R = pathlib.Path(__file__).resolve().parent
PAGES = ['m61', 'rm11', 'read-ia1']
FONTS = R / 'fonts'
FONT_CSS = (FONTS / 'fonts.css').read_text()


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve(site):
    s = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(site)))
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return f'http://127.0.0.1:{s.server_port}/index.html'


def font_file(route):
    f = FONTS / route.request.url.rsplit('/', 1)[1]
    if f.suffix == '.woff2' and f.exists():
        route.fulfill(status=200, content_type='font/woff2', body=f.read_bytes(), headers={'Access-Control-Allow-Origin': '*'})
    else:
        route.abort()


def context(br, w, h):
    mobile = w < 1100
    ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2 if mobile else 1, is_mobile=mobile,
                         has_touch=mobile, color_scheme='dark', reduced_motion='reduce')
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
    ctx.route('**/fonts.gstatic.com/**', font_file)
    return ctx


def open_page(pg, url, pid, theme):
    pg.goto(url + '#home'); pg.wait_for_timeout(200)
    pg.evaluate(f"localStorage.clear(); localStorage.setItem('hellas-theme', '{theme}')")
    pg.goto(url + '#' + pid); pg.reload()
    pg.wait_for_function(f"() => document.fonts.status === 'loaded' && !document.getElementById('{pid}').hidden && document.querySelector('#{pid} .report.steps.stepping')")
    pg.wait_for_timeout(300)
    pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(60)


def tops(br, url, out, widths):
    out.mkdir(parents=True, exist_ok=True)
    for w, h in widths:
        ctx = context(br, w, h); pg = ctx.new_page()
        for pid in PAGES:
            for theme in ('dark', 'light'):
                open_page(pg, url, pid, theme)
                pg.screenshot(path=str(out / f'{w}-{pid}-{theme}.png'))
                # and the end of section 1, where the separator stands, its next and previous at the screen's foot
                pg.evaluate(f"document.querySelector('#{pid} .sec.on > .secnav').scrollIntoView({{block: 'end'}}); window.scrollBy(0, 12)"); pg.wait_for_timeout(80)
                pg.screenshot(path=str(out / f'{w}-{pid}-end1-{theme}.png'))
                # "Whole unit": the first separator standing between its section and the next
                pg.evaluate(f"document.querySelector('#{pid} .stepbar .whole').click()"); pg.wait_for_timeout(100)
                pg.evaluate(f"(() => {{ const t = document.querySelector('#{pid} .topo-sep'); window.scrollTo(0, t.getBoundingClientRect().top + scrollY - innerHeight / 2); }})()"); pg.wait_for_timeout(80)
                pg.screenshot(path=str(out / f'{w}-{pid}-whole-{theme}.png'))
                pg.evaluate(f"document.querySelector('#{pid} .stepbar .whole').click()"); pg.wait_for_timeout(60)
                print('shot', out / f'{w}-{pid}-{theme}.png')
        ctx.close()


CUT_JS = r"""(k) => { const s = [...document.querySelectorAll('.panel:not([hidden]) .report.steps > .sec')].filter(x => x.querySelector(':scope > .topo-sep'))[k];
  const t = s.querySelector(':scope > .topo-sep'), prev = t.previousElementSibling, nav = s.querySelector(':scope > .secnav');
  const a = prev.getBoundingClientRect(), b = (nav || t).getBoundingClientRect();
  return [Math.max(0, a.bottom - Math.min(a.height, 90) + scrollY), b.bottom + 8 + scrollY, +s.dataset.step]; }"""


def cuts(br, url, out, pages, widths=((320, 640), (390, 844), (768, 1024), (1280, 800))):
    """Each separator of each page, one section at a time (the reader's view): the last lines of the text above it,
    the separator, and the next and previous below."""
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for w, h in widths:
        ctx = context(br, w, h); pg = ctx.new_page()
        for pid in pages:
            for theme in ('dark', 'light'):
                open_page(pg, url, pid, theme)
                secs = pg.evaluate(f"[...document.querySelectorAll('#{pid} .report.steps > .sec')].map(s => !!s.querySelector(':scope > .topo-sep'))")
                k = 0
                for step, has in enumerate(secs):
                    if not has:
                        continue
                    pg.evaluate(f"[...document.querySelectorAll('#{pid} .seclist a')][{step}].click()"); pg.wait_for_timeout(120)
                    y0, y1, _ = pg.evaluate(CUT_JS, k)
                    full = pg.evaluate('document.documentElement.scrollHeight')
                    pg.screenshot(path=str(out / f'{w}-{pid}-sep{step + 1:02d}-{theme}.png'), full_page=True,
                                  clip=dict(x=0, y=y0, width=w, height=min(y1, full) - y0))
                    k += 1; n += 1
        ctx.close()
    print(f'{n} cuts in {out}')


if __name__ == '__main__':
    mode = sys.argv[1]
    url = serve(R / 'academy')
    with sync_playwright() as p:
        br = p.chromium.launch()
        if mode == 'before':
            tops(br, url, R / 'reviews/p94/before', ((390, 844), (1280, 800)))
        elif mode == 'after':
            tops(br, url, R / 'reviews/p94/after', ((390, 844), (1280, 800)))
            cuts(br, url, R / 'reviews/p94/after/cuts', PAGES)
        elif mode == 'cuts':
            cuts(br, url, pathlib.Path(sys.argv[2]), sys.argv[3:])
        br.close()
