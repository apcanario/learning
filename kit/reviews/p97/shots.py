"""P97: verify.py's frames() (the --shots sheets) for every changed compare figure, at 320 and 390 px, dark and light,
plus the figure's 1280 px drawing (unchanged) for reference. usage: python3 shots.py <outdir>"""
import sys, json, pathlib, re
sys.argv = [sys.argv[0], '--shots', sys.argv[1]] if len(sys.argv) > 1 else sys.argv
sys.path.insert(0, '/home/claude/learning/kit')
import verify as V
from playwright.sync_api import sync_playwright
out = pathlib.Path(V.SHOTS); out.mkdir(parents=True, exist_ok=True)
pids = open('/tmp/p97/pids.txt').read().split()
idx = (V.SITE / 'index.html').read_text()
with sync_playwright() as p:
    br = p.chromium.launch()
    for name, w, h in (('phone320', 320, 640), ('phone', 390, 844)):
        ctx, pg, _ = V.new_page(p, br, [], name, w, h, True)
        for theme in ('dark', 'light'):
            pg.evaluate(f"localStorage.setItem('hellas-theme', '{theme}')")
            for pid in pids:
                pg.goto(V.URL + '#' + pid); pg.reload(); V.ready(pg); pg.wait_for_timeout(200)
                for k, fig in enumerate(pg.query_selector_all(f'[id="{pid}"] figure.viz')):
                    if 'viz-compare' not in fig.get_attribute('class'):
                        continue
                    fig.evaluate("f => { const s = f.closest('.sec'), p = f.closest('.panel'); if (s && !s.classList.contains('on')) p.querySelector('.seclist a[data-step=\"' + s.dataset.step + '\"]').click(); for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true; }")
                    pg.wait_for_timeout(150)
                    V.frames(pg, fig, out / f'{name}-{pid}-fig-{k + 1:02d}-compare-frames-{theme}.png', f'{pid} figure {k + 1} (compare), {w} px, {theme}')
        ctx.close()
    br.close()
print(len(list(out.glob('*.png'))), 'sheets in', out)
