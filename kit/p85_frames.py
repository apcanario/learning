"""P85 (1 Nov 2026): every frame of a figure, as a reader scrolls it sideways: each frame shot, stacked top to bottom, with
its number, desktop and phone, dark and light. python3 p85_frames.py <academy dir> <out dir> <panel>:<figure n> ...   (dark and light)"""
import sys, pathlib, threading, functools, http.server, socketserver
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

KIT = pathlib.Path(__file__).resolve().parent
FONTS = KIT / 'fonts'
FONT_CSS = (FONTS / 'fonts.css').read_text()
SITE, OUT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)


def serve(d):
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(d))
    h.log_message = lambda *a: None
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 0), h)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s.server_address[1]


def font_file(route):
    f = FONTS / route.request.url.rsplit('/', 1)[1]
    if f.suffix == '.woff2' and f.exists():
        route.fulfill(status=200, content_type='font/woff2', body=f.read_bytes(), headers={'Access-Control-Allow-Origin': '*'})
    else:
        route.abort()


port = serve(SITE)
with sync_playwright() as p:
    br = p.chromium.launch()
    for spec in sys.argv[3:]:
        pid, n = spec.split(':'); n = int(n)
        for (wname, w, dpr, mob) in (('phone', 390, 2, True), ('desktop', 1280, 1, False)):
          for theme in ('dark', 'light'):
            ctx = br.new_context(viewport={'width': w, 'height': 900}, device_scale_factor=dpr, is_mobile=mob, has_touch=mob)
            ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
            ctx.route('**/fonts.gstatic.com/**', font_file)
            ctx.add_init_script(f"try{{localStorage.setItem('hellas-theme','{theme}')}}catch(e){{}}")
            pg = ctx.new_page()
            pg.goto(f'http://127.0.0.1:{port}/index.html#{pid}')
            pg.wait_for_function("() => { const p=document.getElementById('%s'); return p && !p.hidden && p.querySelector('.report') && document.fonts.status==='loaded'; }" % pid, timeout=20000)
            pg.evaluate("() => { const b=document.querySelector('.panel:not([hidden]) .stepbar .whole'); if (b && b.getAttribute('aria-pressed')!=='true') b.click(); }")
            pg.evaluate("() => { for (const el of document.querySelectorAll('*')) { const p = getComputedStyle(el).position; if (p === 'sticky' || p === 'fixed') el.style.setProperty('position', 'static', 'important'); } }")
            pg.wait_for_timeout(300)
            figs = pg.query_selector_all('.panel:not([hidden]) .report figure.viz')
            fig = figs[n - 1]
            fig.scroll_into_view_if_needed()
            sw, cw = fig.evaluate("f => { const s=f.querySelector('.viz-scroll'); return [s.scrollWidth, s.clientWidth]; }")
            shots, x = [], 0
            while True:
                fig.evaluate(f"f => {{ f.querySelector('.viz-scroll').scrollLeft = {x}; }}")
                pg.wait_for_timeout(250)
                tmp = OUT / f'_{pid}-{n}-{theme}-{len(shots)}.png'
                fig.screenshot(path=str(tmp)); shots.append(tmp)
                if x + cw >= sw:
                    break
                x = min(x + cw - 40, sw - cw)      # each frame overlaps the last by 40 px, as a thumb scroll would
            ims = [Image.open(s) for s in shots]
            W = max(i.width for i in ims); H = sum(i.height + 40 for i in ims)
            sheet = Image.new('RGB', (W, H), (128, 128, 128)); d = ImageDraw.Draw(sheet); y = 0
            for k, im in enumerate(ims):
                d.text((6, y + 10), f'{wname} frame {k + 1} of {len(ims)}' + (' (scrolled sideways)' if len(ims) > 1 else ' (the whole figure fits)'), fill=(0, 0, 0)); y += 40
                sheet.paste(im, (0, y)); y += im.height
            sheet.save(OUT / f'{wname}-frames-{pid}-fig-{n:02d}-{theme}.png')
            for s in shots:
                s.unlink()
            ctx.close()
            print(pid, n, wname, theme, len(ims), 'frames', f'(drawing {sw} px, frame {cw} px)')
    br.close()
