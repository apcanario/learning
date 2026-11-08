"""P95 (8 Nov 2026) · the object reliefs' tool: an outline from the library (design/outlines/, one SVG each, listed with
its source and credit in outlines.json) drawn as the lines of a relief map of its own silhouette. Run when an outline
is added, not by the build, so the build stays pure Python: it reads the JSON this writes.

For each outline: the SVG is rendered in the session's Chromium (Playwright) at 512 px, white on black, and thresholded
to a silhouette; its signed distance field is taken (scipy.ndimage.distance_transform_edt inside and outside, inside
positive), and contoured (skimage.measure.find_contours) at even steps: the outline itself and up to seven levels inside
it, a step a ninth of the deepest distance (so up to 8 levels inside, the outline counted), and two faint halo levels
outside at the same step. Each line is simplified with viz.py's RDP (_ct_simplify), the whole normalised to a box whose
longer side is 1000 units, and written to design/outlines/<id>.json. viz.py's kind `relief` draws it.

It also measures how busy a silhouette is (the row's rule: a part thinner than 3% of its width, or more than 40
separate regions, is a busy relief and the outline is rejected): `regions`, the separate pieces of the silhouette; `thin`,
the thin parts, each a piece the silhouette loses to an opening by a disc 1.5% of its width across in radius (so under
3% thick) that runs at least 8% of its width (a short corner the disc rounds off is not a part: the row's "a part
thinner than 3% of its width" read as a part, not a corner); and, after the first fresh check (P95), a step under
MIN_STEP px at 512 px, where a silhouette drawn in thin strokes packs its levels so close they merge into solid bands.

    python3 relief.py                 every outline in outlines.json
    python3 relief.py amphora owl     those outlines
    python3 relief.py --probe a.svg   only the measures of SVG files (selecting an outline), nothing written
"""
import json, math, pathlib, sys

import numpy as np
from scipy import ndimage
from skimage import measure, morphology

import viz

R = pathlib.Path(__file__).resolve().parent
LIB = R.parent / 'design' / 'outlines'
PX = 512            # the render's size
PAD = 96            # the field's margin round the render, so the halo is never cut off
IN_LEVELS = 8       # the outline and up to seven levels inside it
OUT_LEVELS = 2      # the halo
STEP_DIV = 9        # a step is the deepest distance over this
EPS = .8            # RDP tolerance at the render's scale, in pixels (about 1.6 units of 1000)
BOX = 1000          # the longer side of the normalised drawing
MAX_REGIONS, THIN, THIN_RUN = 40, .03, .08
MIN_STEP = 3.0     # P95 check A: a step under 3 px at 512 px (lines closer than about 0.6% of the width) merges into solid bands: busy

PAGE = '''<!doctype html><html><head><style>html,body{margin:0;background:#000}
svg{display:block;width:512px;height:512px;color:#fff}</style></head><body>%s</body></html>'''


def render(svg, page):
    """The silhouette of an SVG at PX by PX, as a boolean array (True inside)."""
    import io
    from PIL import Image
    s = svg[svg.index('<svg'):]
    page.set_content(PAGE % s)
    img = Image.open(io.BytesIO(page.screenshot(clip=dict(x=0, y=0, width=PX, height=PX)))).convert('L')
    return np.array(img) > 127


def busy(mask):
    """(regions, thin parts) of a silhouette, by the rule in the module docstring."""
    _, regions = ndimage.label(mask)
    ys, xs = np.nonzero(mask)
    w = (xs.max() - xs.min() + 1) if len(xs) else PX
    r = max(1, round(w * THIN / 2))
    opened = morphology.opening(mask, morphology.disk(r))
    lost, n = ndimage.label(mask & ~opened)
    thin = 0
    for sl in ndimage.find_objects(lost):
        if sl is None:
            continue
        ext = math.hypot(sl[0].stop - sl[0].start, sl[1].stop - sl[1].start)
        if ext >= THIN_RUN * w:
            thin += 1
    return int(regions), thin


def field(mask):
    m = np.pad(mask, PAD)
    return ndimage.distance_transform_edt(m) - ndimage.distance_transform_edt(~m)


def lines(mask):
    """The relief's lines: [(level, points [(x, y)], closed)], in the padded render's pixels; the step and depth."""
    f = field(mask)
    depth = float(f.max())
    step = depth / STEP_DIV
    out = []
    levels = [k * step for k in range(IN_LEVELS)] + [-k * step for k in range(1, OUT_LEVELS + 1)]
    for k, lv in zip(list(range(IN_LEVELS)) + [-k for k in range(1, OUT_LEVELS + 1)], levels):
        for c in measure.find_contours(f, lv if lv else 1e-6):
            pts = [(float(x), float(y)) for y, x in c]
            closed = len(pts) > 2 and math.dist(pts[0], pts[-1]) < 1e-6
            if closed:
                pts = pts[:-1]
            p = viz._ct_simplify(pts, closed, EPS)
            if len(p) >= (3 if closed else 2):
                out.append((k, p, closed))
    return out, step, depth


def normalise(ls):
    xs = [x for _, p, _ in ls for x, _ in p]
    ys = [y for _, p, _ in ls for _, y in p]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys)
    k = BOX / max(x1 - x0, y1 - y0)
    w, h = round((x1 - x0) * k), round((y1 - y0) * k)
    return w, h, [dict(lv=lv, closed=c, pts=[[round((x - x0) * k), round((y - y0) * k)] for x, y in p]) for lv, p, c in ls]


def main():
    from playwright.sync_api import sync_playwright
    args = sys.argv[1:]
    probe = '--probe' in args
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        page = br.new_page(viewport=dict(width=PX, height=PX))
        if probe:
            for f in [a for a in args if a != '--probe']:
                mask = render(pathlib.Path(f).read_text(), page)
                rg, th = busy(mask)
                st = float(field(mask).max()) / STEP_DIV
                print(f'{pathlib.Path(f).name}: regions {rg}, thin parts {th}, step {st:.2f} px' + (' BUSY' if rg > MAX_REGIONS or th or st < MIN_STEP else ''))
            return
        lib = json.loads((LIB / 'outlines.json').read_text())
        for o in lib['outlines']:
            if args and o['id'] not in args:
                continue
            mask = render((LIB / o['file']).read_text(), page)
            rg, th = busy(mask)
            ls, step, depth = lines(mask)
            w, h, norm = normalise(ls)
            data = dict(id=o['id'], width=w, height=h, levels_in=IN_LEVELS, levels_out=OUT_LEVELS,
                        render=dict(px=PX, depth_px=round(depth, 2), step_px=round(step, 2), regions=rg, thin_parts=th),
                        lines=norm)
            (LIB / f'{o["id"]}.json').write_text(json.dumps(data, separators=(',', ':')) + '\n')
            busy_ = rg > MAX_REGIONS or th or step < MIN_STEP
            print(f'{o["id"]}: {w}x{h}, {len(norm)} lines, depth {depth:.1f} px, step {step:.2f} px, regions {rg}, thin parts {th}'
                  + (' BUSY' if busy_ else ''))
            assert not busy_, f'{o["id"]}: a busy relief; reject it in p95_library.py'
        br.close()


if __name__ == '__main__':
    main()
