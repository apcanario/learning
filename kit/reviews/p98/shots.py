"""P98: verify.py's frames() for every compare or bars figure P98 changed, at 320, 390 and 1280 px, dark and light.
usage: python3 shots.py <changed.txt> <outdir>"""
import sys, re, pathlib
changed, outdir = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], '--shots', outdir]
sys.path.insert(0, '/home/claude/learning/kit')
import verify as V
from playwright.sync_api import sync_playwright
out = pathlib.Path(outdir); out.mkdir(parents=True, exist_ok=True)
idx = (V.SITE / 'index.html').read_text()
src2pid = {src: pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)}
want = {}
for line in open(changed):
    m = re.match(r'(\S+) figure (\d+) \((\w+)\)', line)
    if m: want.setdefault(src2pid[m.group(1)], []).append((int(m.group(2)), m.group(3)))
with sync_playwright() as p:
    br = p.chromium.launch()
    for name, w, h in (('phone320', 320, 640), ('phone', 390, 844), ('desktop', 1280, 800)):
        ctx, pg, _ = V.new_page(p, br, [], name, w, h, w < 768)
        for theme in ('dark', 'light'):
            pg.evaluate(f"localStorage.setItem('hellas-theme', '{theme}')")
            for pid, figs in want.items():
                pg.goto(V.URL + '#' + pid); pg.reload(); V.ready(pg); pg.wait_for_timeout(200)
                all_ = pg.query_selector_all(f'[id="{pid}"] figure.viz')
                for k, kind in figs:
                    fig = all_[k - 1]
                    assert f'viz-{kind}' in fig.get_attribute('class'), (pid, k, kind)
                    fig.evaluate("f => { const s = f.closest('.sec'), p = f.closest('.panel'); if (s && !s.classList.contains('on')) p.querySelector('.seclist a[data-step=\"' + s.dataset.step + '\"]').click(); for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true; }")
                    pg.wait_for_timeout(150)
                    V.frames(pg, fig, out / f'{name}-{pid}-fig-{k:02d}-{kind}-frames-{theme}.png', f'{pid} figure {k} ({kind}), {w} px, {theme}')
        ctx.close()
    br.close()
print(len(list(out.glob('*-frames-*.png'))), 'sheets in', out)
