"""P97 probe: for every compare figure on every page, at 320 and 390 px, does the opening frame show the longest bar whole?
usage: python3 probe.py <site dir> <out.json>"""
import sys, re, json, pathlib, functools, threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
site = pathlib.Path(sys.argv[1])
class Q(SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Q, directory=str(site)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{srv.server_port}/index.html'
idx = (site / 'index.html').read_text()
panels = []
for m in re.finditer(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx):
    pid, src = m.groups()
    if 'viz-compare' in (site / src).read_text():
        panels.append(pid)
if 'viz-compare' in idx:
    for m in re.finditer(r'<section class="panel" id="([^"]+)"', idx):
        pass
JS = """async () => { const out = []; const p = [...document.querySelectorAll('.panel')].find(p => !p.hidden);
 const figs = [...p.querySelectorAll('figure.viz-compare')];
 for (const [i, f] of figs.entries()) { const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click(); await new Promise(r => setTimeout(r, 150)); for (const d of document.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120)); const sc = f.querySelector('.viz-scroll');
  const svgs = [...sc.querySelectorAll(':scope > svg')].filter(s => getComputedStyle(s).display !== 'none');
  const s = svgs[0]; const bars = [...s.querySelectorAll('rect.viz-bar')];
  const fr = sc.getBoundingClientRect(); let best = null;
  bars.forEach(b => { const r = b.getBoundingClientRect(); if (!best || r.width > best.width) best = r; });
  const vals = [...s.querySelectorAll('text.viz-value')].map(t => t.getBoundingClientRect());
  const vmax = vals.length ? Math.max(...vals.map(v => v.right)) : 0;
  out.push({i: i + 1, frame: [Math.round(fr.left), Math.round(fr.right)], sw: sc.scrollWidth, cw: sc.clientWidth,
    bar: best ? [Math.round(best.left), Math.round(best.right)] : null, vright: Math.round(vmax),
    whole: !!best && best.left >= fr.left - 0.5 && best.right <= fr.right + 0.5,
    fits: sc.scrollWidth <= sc.clientWidth + 1, alt: s.classList.contains('viz-alt'),
    font: s.querySelector('text') ? getComputedStyle(s.querySelector('text')).fontSize : null,
    scale: s.getBoundingClientRect().width / (+s.getAttribute('width')), sl: sc.scrollLeft}); } return out; }"""
res = {}
with sync_playwright() as p:
    br = p.chromium.launch()
    for w in (320, 390):
        ctx = br.new_context(viewport={'width': w, 'height': 800}, device_scale_factor=1, is_mobile=True, has_touch=True)
        pg = ctx.new_page(); pg.goto(URL + '#home'); pg.wait_for_timeout(300)
        for pid in panels:
            pg.evaluate(f"location.hash = '{pid}'")
            pg.wait_for_function("""() => { const p = [...document.querySelectorAll('.panel')].find(p => !p.hidden);
              return !!p && (!p.hasAttribute('data-src') || p.hasAttribute('data-loaded') || p.hasAttribute('data-failed')); }""", timeout=15000)
            pg.wait_for_timeout(150)
            res[f'{w}:{pid}'] = pg.evaluate(JS)
        ctx.close()
    br.close()
pathlib.Path(sys.argv[2]).write_text(json.dumps(res, indent=1))
tot = sum(len(v) for v in res.values()); bad = sum(1 for v in res.values() for f in v if not f['whole'])
print(f'{len(panels)} panels, {tot} compare frames, {bad} without the longest bar whole')
