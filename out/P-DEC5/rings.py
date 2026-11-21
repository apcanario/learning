"""Diagnose: a course home's hero frame and each rise's data-box against it, desktop motion, at the five poses."""
import sys
root = sys.argv[1]; ed = sys.argv[2]; pid = sys.argv[3]
sys.argv = ['verify.py', '--edition', ed]
sys.path.insert(0, root + '/kit')
import verify as V
from playwright.sync_api import sync_playwright
JS = r"""(pid) => { const t = document.querySelector('#' + pid + ' > header.hero > .topo'); const h = t.parentElement;
 const fr = t.getBoundingClientRect(); const sv = [...t.querySelectorAll(':scope > svg.topo-l')].find(s => getComputedStyle(s).display !== 'none');
 const m = sv.getScreenCTM(); const out = {frame: [fr.left, fr.top, fr.width, fr.height], hero: h.getBoundingClientRect().height, vb: sv.getAttribute('viewBox'), par: sv.getAttribute('preserveAspectRatio'), layout: sv.getAttribute('data-layout'), rises: []};
 sv.querySelectorAll('g.ct-rise[data-box]').forEach(g => { const b = g.getAttribute('data-box').split(' ').map(Number);
   const p0 = new DOMPoint(b[0], b[1]).matrixTransform(m), p1 = new DOMPoint(b[2], b[3]).matrixTransform(m);
   out.rises.push([g.getAttribute('data-label'), b, +(p0.y - fr.top).toFixed(1), +(fr.top + .9 * fr.height - p1.y).toFixed(1), +(p0.x - fr.left).toFixed(1), +(fr.right - p1.x).toFixed(1)]); });
 out.lines = [...h.querySelectorAll('h1, .lede, p')].slice(0, 4).map(e => [e.tagName, e.className, Math.round(e.getBoundingClientRect().height)]);
 return out; }"""
with sync_playwright() as p:
    br = p.chromium.launch(); errors = []
    ctx, pg, _ = V.new_page(p, br, errors, 'desktop motion', 1280, 800, False, motion=True)
    pg.evaluate(f"location.hash = '{pid}'"); V.ready(pg); pg.wait_for_timeout(250)
    for p_ in V.POSES:
        V.pose(pg, p_)
        r = pg.evaluate(JS, pid)
        if p_ == 0: print('frame', [round(x, 1) for x in r['frame']], 'hero', r['hero'], r['layout'], r['vb'], r['par'], r['lines'])
        print('pose', p_, 'worst top/bottom-fade/left/right margins:', [min(x[i] for x in r['rises']) for i in (2, 3, 4, 5)], [x for x in r['rises'] if min(x[2:]) < 0.5])
    br.close()
