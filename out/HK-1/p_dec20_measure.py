# measure each course home's hero and its topo frame at a window width (default 1280 x 800), dark
import sys, subprocess, time, re, pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(sys.argv[1]); W = int(sys.argv[2]) if len(sys.argv) > 2 else 1280
port = 8700 + (abs(hash(str(root))) % 200)
srv = subprocess.Popen([sys.executable, '-m', 'http.server', str(port), '-d', str(root)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
ids = re.findall(r'<section class="panel[^>]*?id="([^"]+)"[^>]*data-kind="course"', (root/'index.html').read_text())
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport=dict(width=W, height=800))
        for i in ids:
            pg.goto(f'http://127.0.0.1:{port}/index.html#{i}'); pg.wait_for_function("(i) => { const s = document.getElementById(i); return s && !s.hidden && (!s.hasAttribute('data-src') || s.hasAttribute('data-loaded')) && document.fonts.status === 'loaded'; }", arg=i, timeout=15000); pg.wait_for_timeout(300)
            r = pg.evaluate("""(i) => { const s = document.getElementById(i); const h = s && s.querySelector('.hero'); if (!h) return null;
              const t = h.querySelector('.topo'); const hr = h.getBoundingClientRect(); const tr = t ? t.getBoundingClientRect() : null;
              return [hr.height, tr ? tr.width : null, tr ? tr.height : null, getComputedStyle(h).minHeight]; }""", i)
            print(i, r)
        b.close()
finally:
    srv.terminate()
