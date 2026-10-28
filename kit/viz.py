"""Figures for Academy (A8, 28 Oct 2026): four primitives that a unit or a course home declares as data and build.py
renders as inline SVG, styled only by design/theme.css section 4i (classes, tokens, no attributes with colours).

The contract a writer uses:

  In a history fragment (kit/<course>/r-<id>.html):
    <figure class="viz" data-viz="timeline"><script type="application/json">{ ... }</script><figcaption>...</figcaption></figure>
  In a markdown unit (courses/<course>/<code>-<slug>.md), a fenced block:
    ```viz
    { "kind": "timeline", "caption": "...", ... }
    ```
  In courses.py, a course's `figure` entry: the same object, drawn on the course home.

A figure's numbers and names are claims: they are sourced like any other claim in the unit, and the caption says where
they come from. The kinds and their fields:

  timeline  {"kind": "timeline", "start": -1000, "end": 476, "ticks": [-750, -500, ...], "events": [{"at": -753, "label": "Foundation"}, ...],
             "spans": [{"from": -753, "to": -509, "label": "Kings", "tone": 1}, ...]}      years: negative BC, positive AD
  compare   {"kind": "compare", "unit": "%", "max": 100, "rows": [{"label": "Instagram", "value": 61}, ...]}   horizontal bars
  tree      {"kind": "tree", "root": {"label": "Chaos", "children": [{"label": "Gaia", "children": [...]}]}}    top-down
  flow      {"kind": "flow", "steps": [{"label": "Quaestor", "note": "age 30"}, ...]}                            left to right, wraps

Every kind takes "caption" (shown under the figure; keep the source in it) and "title" (optional, drawn above).
"""
import html as H
import json
import re
import textwrap

W = 700            # drawing width in user units; the SVG scales to the column
TONES = 6          # --viz-1 … --viz-6 map to the house accents in theme.css


def esc(s):
    return H.escape(str(s), quote=True)


def yr(y):
    y = int(y)
    return f'{-y} BC' if y < 0 else f'AD {y}' if y < 1000 else str(y)


def _svg(w, h, body, cls, title, caption):
    t = f'<p class="viz-title">{esc(title)}</p>' if title else ''
    c = f'<figcaption>{caption}</figcaption>' if caption else ''
    return (f'<figure class="viz viz-{cls}">{t}<div class="viz-scroll"><svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title or cls)}">{body}</svg></div>{c}</figure>')


def _wrap(s, n):
    return textwrap.wrap(str(s), n) or ['']


def timeline(d):
    start, end = d['start'], d['end']
    spans, events, ticks = d.get('spans', []), d.get('events', []), d.get('ticks', [])
    W = max(700, 64 * len(events))          # a dense timeline widens and scrolls sideways inside its figure
    L, R = 40, W - 40
    def x(y):
        return L + (R - L) * (y - start) / (end - start)
    body = ''
    y0 = 24
    if spans:
        for k, s in enumerate(spans):
            tone = s.get('tone', k % TONES + 1)
            x1, x2 = x(s['from']), x(s['to'])
            body += f'<rect class="viz-span viz-t{tone}" x="{x1:.1f}" y="{y0}" width="{x2 - x1:.1f}" height="18"/>'
            body += f'<text class="viz-spanlabel" x="{(x1 + x2) / 2:.1f}" y="{y0 + 13}" text-anchor="middle">{esc(s["label"])}</text>'
        y0 += 30
    axis = y0 + 22                           # tick labels sit above the axis, events hang below it
    body += f'<line class="viz-axis" x1="{L}" y1="{axis}" x2="{R}" y2="{axis}"/>'
    for t in ticks:
        tx = x(t)
        anchor = 'start' if tx < L + 20 else ('end' if tx > R - 20 else 'middle')
        body += f'<line class="viz-tick" x1="{tx:.1f}" y1="{axis - 6}" x2="{tx:.1f}" y2="{axis}"/><text class="viz-ticklabel" x="{tx:.1f}" y="{axis - 10}" text-anchor="{anchor}">{esc(yr(t))}</text>'
    # events: alternate rows below the axis so labels never collide; each event is a dot, a stem and a two-line label
    rows = 3 if len(events) <= 8 else 4
    lane_h = 44
    for k, e in enumerate(events):
        lane = k % rows
        ex = x(e['at'])
        ty = axis + 36 + lane * lane_h
        body += f'<line class="viz-stem" x1="{ex:.1f}" y1="{axis}" x2="{ex:.1f}" y2="{ty - 12}"/>'
        body += f'<circle class="viz-dot viz-t{e.get("tone", 1)}" cx="{ex:.1f}" cy="{axis}" r="4"/>'
        anchor = 'start' if ex < L + 60 else ('end' if ex > R - 60 else 'middle')
        lines = [yr(e['at'])] + _wrap(e['label'], 22)[:2]
        for i, ln in enumerate(lines):
            cls = 'viz-date' if i == 0 else 'viz-label'
            body += f'<text class="{cls}" x="{ex:.1f}" y="{ty + i * 13}" text-anchor="{anchor}">{esc(ln)}</text>'
    h = axis + 36 + rows * lane_h + 4
    return _svg(W, h, body, 'timeline', d.get('title'), d.get('caption'))


def compare(d):
    rows = d['rows']
    mx = d.get('max') or max(r['value'] for r in rows)
    unit = d.get('unit', '')
    lab_w = 170
    bar_x = lab_w + 10
    bar_w = W - bar_x - 70
    rh = 30
    body = ''
    for k, r in enumerate(rows):
        y = 8 + k * rh
        wv = bar_w * float(r['value']) / mx
        body += f'<text class="viz-label" x="{lab_w}" y="{y + 15}" text-anchor="end">{esc(r["label"])}</text>'
        body += f'<rect class="viz-track" x="{bar_x}" y="{y + 5}" width="{bar_w}" height="14"/>'
        body += f'<rect class="viz-bar viz-t{r.get("tone", 1)}" x="{bar_x}" y="{y + 5}" width="{wv:.1f}" height="14"/>'
        body += f'<text class="viz-value" x="{bar_x + wv + 8:.1f}" y="{y + 16}">{esc(r.get("display", f"{r['value']}{unit}"))}</text>'
    h = 8 + len(rows) * rh + 4
    return _svg(W, h, body, 'compare', d.get('title'), d.get('caption'))


def tree(d):
    """Top-down tree. Each node is a box; leaves are laid out left to right and parents centred over their children."""
    node_w, node_h, gx, gy = 112, 34, 10, 44
    root = d['root']
    pos = {}
    cursor = [0]
    def layout(n, depth):
        kids = n.get('children', [])
        if kids:
            xs = [layout(k, depth + 1) for k in kids]
            cx = (xs[0] + xs[-1]) / 2
        else:
            cx = cursor[0] + node_w / 2
            cursor[0] += node_w + gx
        pos[id(n)] = (cx, depth)
        return cx
    layout(root, 0)
    width = max(cursor[0], node_w)
    depth_max = max(dp for _, dp in pos.values())
    scale = min(1, W / width)
    body = ''
    def draw(n):
        cx, dp = pos[id(n)]
        x = cx * scale - node_w * scale / 2
        y = 8 + dp * (node_h + gy)
        for k in n.get('children', []):
            kx, kd = pos[id(k)]
            body_add = f'<path class="viz-edge" d="M{cx * scale:.1f},{y + node_h} C{cx * scale:.1f},{y + node_h + gy / 2} {kx * scale:.1f},{y + node_h + gy / 2} {kx * scale:.1f},{y + node_h + gy}"/>'
            nonlocal body; body += body_add
            draw(k)
        tone = n.get('tone', min(dp + 1, TONES))
        body += f'<rect class="viz-node viz-t{tone}" x="{x:.1f}" y="{y}" width="{node_w * scale:.1f}" height="{node_h}" rx="2"/>'
        lines = _wrap(n['label'], max(8, int(17 * scale)))[:2]
        for i, ln in enumerate(lines):
            body += f'<text class="viz-nodelabel" x="{cx * scale:.1f}" y="{y + (15 if len(lines) == 1 else 13) + i * 13 + (6 if len(lines) == 1 else 0)}" text-anchor="middle">{esc(ln)}</text>'
    draw(root)
    h = 8 + (depth_max + 1) * (node_h + gy) - gy + 8
    return _svg(W, h, body, 'tree', d.get('title'), d.get('caption'))


def flow(d):
    steps = d['steps']
    per_row = d.get('per_row', 4)
    bw, bh, gap, rowh = 150, 54, 26, 80
    body = ''
    for k, s in enumerate(steps):
        r, c = divmod(k, per_row)
        x = 8 + c * (bw + gap)
        y = 8 + r * rowh
        tone = s.get('tone', 1)
        body += f'<rect class="viz-node viz-t{tone}" x="{x}" y="{y}" width="{bw}" height="{bh}" rx="2"/>'
        body += f'<text class="viz-nodelabel" x="{x + 12}" y="{y + 22}">{esc(s["label"])}</text>'
        if s.get('note'):
            body += f'<text class="viz-note" x="{x + 12}" y="{y + 40}">{esc(s["note"])}</text>'
        if k < len(steps) - 1:
            if c < per_row - 1:
                body += f'<path class="viz-arrow" d="M{x + bw + 4},{y + bh / 2} L{x + bw + gap - 6},{y + bh / 2}"/>'
            else:
                body += f'<path class="viz-arrow" d="M{x + bw / 2},{y + bh + 2} L{x + bw / 2},{y + rowh - 6} L{8 + bw / 2},{y + rowh - 6} L{8 + bw / 2},{y + rowh - 2}"/>'
    rows = (len(steps) + per_row - 1) // per_row
    w = 8 + min(len(steps), per_row) * (bw + gap) - gap + 8
    h = 8 + rows * rowh - (rowh - bh) + 8
    return _svg(max(w, 320), h, body + '<defs><marker id="vizhead" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="viz-head" d="M0,0 L10,5 L0,10 z"/></marker></defs>', 'flow', d.get('title'), d.get('caption'))


KINDS = {'timeline': timeline, 'compare': compare, 'tree': tree, 'flow': flow}


def render(d):
    """One figure object to HTML. A kind not in KINDS, or bad data, is an error: a figure that cannot draw is a bug, not a blank."""
    try:
        return KINDS[d['kind']](d)
    except KeyError as e:
        raise SystemExit(f'viz: unknown kind or missing field {e} in figure {json.dumps(d)[:120]}')


_FIG = re.compile(r'<figure class="viz" data-viz="([\w-]+)">\s*<script type="application/json">(.*?)</script>\s*(?:<figcaption>(.*?)</figcaption>)?\s*</figure>', re.S)
_FENCE = re.compile(r'^```viz\n(.*?)\n```$', re.S | re.M)


def render_html(frag):
    """Replace every figure declaration in a history fragment with its drawing."""
    def sub(m):
        d = json.loads(m.group(2)); d.setdefault('kind', m.group(1))
        if m.group(3) and not d.get('caption'):
            d['caption'] = m.group(3)
        return render(d)
    return _FIG.sub(sub, frag)


def extract_md(src):
    """Pull ```viz fences out of a markdown source before it is rendered; returns (source with placeholders, {token: html})."""
    figs = {}
    def sub(m):
        tok = f'VIZFIG{len(figs)}VIZ'
        figs[tok] = render(json.loads(m.group(1)))
        return f'\n\n{tok}\n\n'
    return _FENCE.sub(sub, src), figs


def restore_md(body, figs):
    for tok, h in figs.items():
        body = body.replace(f'<p>{tok}</p>', h).replace(tok, h)
    return body
