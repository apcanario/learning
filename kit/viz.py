"""Figures for Academy (A8, 28 Oct 2026; seven IA kinds added at V1 and four data kinds at P44, 29 Oct 2026): primitives that a unit or a course home declares as data and build.py
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

The IA kinds (V1, 29 Oct 2026, for the Information Architecture course; the examples page, Academy #viz-examples,
built by viz_examples.py, shows one of each on Perqo with its block):

  sitemap   {"kind": "sitemap", "stack_from": 2, "root": {"label": "Home", "type": "home", "note": "...", "tone": 1,
             "children": [{"label": "Pricing", "type": "pricing"}, ...]}}
            top-down; "type" is the page type, drawn as a small mono tag; the root's children sit in rows that wrap
            when wider than the drawing; from depth stack_from children stack under their parent; depth unlimited.
            Default tones: the root 1, each first-level branch its own (2 to 6), inherited below it.
  objects   {"kind": "objects", "objects": [{"id": "claim", "title": "Claim", "attrs": ["amount", ...],
             "actions": ["-> approve", ...], "tone": 2}, ...], "rows": [["company", "policy", null], ...],
             "links": [{"from": "company", "to": "policy", "label": "sets", "from_card": "1", "to_card": "1..*"}]}
            boxes placed in the grid "rows" gives (null is an empty cell; at most 4 columns); a link is a line with a
            label and a cardinality at each end; a link that would cross a third box raises (move a box).
  decision  {"kind": "decision", "root": {"q": "Active contract?", "tone": 4, "branches": [{"label": "no",
             "to": {"outcome": "Not eligible", "tone": 1}}, {"label": "yes", "to": {"q": ...}}]}}
            questions are boxes, outcomes filled boxes, read top-down; branches keep their order left to right.
  matrix    {"kind": "matrix", "cols": ["Employees", ...], "rows": [{"label": "HR admin", "tone": 4,
             "cells": ["edit", {"mark": "approve", "tone": 2}, null, ...]}], "legend": [{"mark": "edit", "means": "...", "tone": 3}]}
            a cell is a short mark (string, or an object with its own tone) or null for blank; a row's cells match cols.
  states    {"kind": "states", "per_row": 4, "start": "draft", "states": [{"id": "draft", "label": "Draft", "note": "...",
             "tone": 5, "end": false}, ...], "transitions": [{"from": "draft", "to": "submitted", "label": "submit"}, ...]}
            states in the order given, in rows; "start" (default the first state; null for none) must begin a row; an
            end state has an inner ring; from == to is a loop; a transition across more than one row raises.
  swimlanes {"kind": "swimlanes", "lanes": [{"id": "app", "label": "Perqo app", "tone": 3}, ...],
             "steps": [{"id": "enrol", "lane": "app", "col": 1, "label": "Enrol", "note": "...", "tone": 3}, ...],
             "links": [{"from": "open", "to": "enrol", "label": "invites"}, ...]}
            lanes top to bottom; a step sits in its lane at "col" (from 0; one step per lane and column); a link runs
            along a lane or through the gap between columns; widens with its columns and scrolls; a link with no clear
            route raises (move a step).
  wireflow  {"kind": "wireflow", "per_row": 3, "screens": [{"id": "home", "title": "Home", "tone": 3, "lines": ["Balance",
             {"bar": 0.6}, {"block": 40}, {"button": "New claim"}]}, ...], "links": [{"from": "home", "to": "spend", "label": "..."}]}
            screens left to right, wrapping; a line is text, a placeholder bar (share of the width), a placeholder
            block (height) or a button; links route as in states.

The data kinds (P44, 29 Oct 2026; one of each on the examples page too):

  line      {"kind": "line", "x": [2019, 2020, ...], "years": true, "unit": "k", "series": [{"name": "App users",
             "values": [null, 2.5, 9, ...], "tone": 3}, ...], "annotations": [{"at": 2021, "label": "App released"}],
             "labels": "all"}
            one or more series over an ordered x (numbers spaced to scale, or strings spaced evenly); null breaks a line;
            every point labelled with its value ("all", the default up to eight x values), only the first and last
            ("ends") or none; optional min, max, yticks, xticks, decimals, height (plot, default 240), xlabel, ylabel;
            a legend when the series are named (a name is required with more than one series).
  bars      {"kind": "bars", "mode": "grouped", "unit": "%", "series": [{"name": "2024", "tone": 4}, ...],
             "rows": [{"label": "Instagram", "values": [61, 64]}, ...]}
            horizontal bars across categories, grouped (one bar per series) or "stacked" (one bar of segments, the
            total at its end, a segment's value inside it when it fits); values of 0 or more; optional max, decimals.
  scatter   {"kind": "scatter", "x": {"label": "...", "min": 0, "max": 60, "ticks": [...], "unit": "%"}, "y": {...},
             "points": [{"label": "Gym pass", "x": 38, "y": 7.9, "tone": 4}, ...],
             "quadrants": {"x": 25, "y": 7.5, "names": ["top left", "top right", "bottom left", "bottom right"]}}
            labelled points on two numeric axes with gridlines at the ticks; each label takes the nearest free spot
            around its point (covering no point, label or quadrant name), and a label with no free spot raises.
  range     {"kind": "range", "unit": "%", "min": 0, "max": 100, "ticks": [...], "rows": [{"label": "...", "low": 45,
             "high": 70, "point": 58, "low_src": "Pew 2024", "high_src": "Ofcom 2025", "tone": 4}, ...]}
            competing estimates: per row a low-to-high bar, an optional point estimate (a diamond, its value above it)
            and under the bar each end's value with its source tag; one axis for every row.
  matrix    with "numeric": true: cells are numbers (or null), shaded in five steps of the figure's "tone" between
            min and max (default the data's); a legend gives each step's range ("scale_label" names it).

On a phone (below 768 px) every figure draws at its natural size, one SVG unit to one CSS pixel, and scrolls sideways
inside its frame (.viz-scroll), never the page; shell.js fades the edge that has more drawing and shows the line
"scroll sideways for the whole figure" under a figure only when its drawing is wider than its frame.

Every kind takes "caption" (shown under the figure; keep the source in it) and "title" (optional, drawn above), and
"tone" (1 to 6, the house accents) on any node, box, lane, step, screen or cell. A kind that cannot draw its data
raises SystemExit and stops the build: a figure that cannot draw is a bug, not a blank. The IA kinds measure their text
in the theme's fonts and wrap it inside its box, which grows to fit; every box and its text are one <g data-box>, which
verify.py checks on the examples page (text inside its box, no two boxes overlapping, nothing outside the drawing).
"""
import html as H
import itertools
import json
import math
import re
import textwrap

W = 700            # drawing width in user units; the SVG scales to the column
TONES = 6          # --viz-1 … --viz-6 map to the house accents in theme.css


def esc(s):
    return H.escape(str(s), quote=True)


def yr(y):
    y = int(y)
    return f'{-y} BC' if y < 0 else f'AD {y}' if y < 1000 else str(y)


def _svg(w, h, body, cls, title, caption, wide=False):
    t = f'<p class="viz-title">{esc(title)}</p>' if title else ''
    c = f'<figcaption>{caption}</figcaption>' if caption else ''
    return (f'<figure class="viz viz-{cls}{" viz-wide" if wide else ""}">{t}<div class="viz-scroll"><svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title or cls)}">{body}</svg></div>{c}</figure>')


def _wrap(s, n, px=None, size=12, font='sans', ls=0.0):
    """Wrap at n characters (the four A8 kinds), or, given px, at that measured width in the theme's own fonts (the IA
    kinds): a word wider than px is broken inside, so a line never exceeds px and text never overflows its box."""
    if px is None:
        return textwrap.wrap(str(s), n) or ['']
    lines, cur = [], ''
    for word in str(s).split():
        while _tw(word, size, font, ls) > px:                      # a word too long for the line: break it
            k = max(1, max(i for i in range(1, len(word) + 1) if _tw(word[:i], size, font, ls) <= px or i == 1))
            if cur:
                lines.append(cur); cur = ''
            lines.append(word[:k]); word = word[k:]
        trial = f'{cur} {word}' if cur else word
        if _tw(trial, size, font, ls) <= px:
            cur = trial
        else:
            lines.append(cur); cur = word
    if cur:
        lines.append(cur)
    return lines or ['']


# Advance widths (per 1000 em) of DM Sans 400 and 600 for the characters a figure is likely to carry, read from the
# fonts the theme loads (V1, 29 Oct 2026); Space Mono is fixed at 612. _tw adds 4 % so a system fallback still fits.
_CH = ''.join(chr(c) for c in range(32, 127)) + '€£éèáàãõçíóúâêôüöäñÉÁÇ×–—’‘“”·…→←↑↓±≤≥°'
_SANS = [266, 250, 291, 804, 580, 786, 734, 159, 373, 373, 480, 550, 182, 541, 198, 392, 684, 312, 576, 591, 607, 610, 628, 534,
         608, 628, 202, 227, 550, 550, 550, 524, 1005, 664, 603, 717, 688, 565, 535, 758, 681, 234, 501, 584, 527, 841, 691, 774,
         580, 774, 594, 580, 561, 655, 669, 968, 603, 580, 541, 314, 392, 314, 622, 660, 213, 544, 626, 572, 627, 568, 340, 558,
         575, 240, 243, 504, 223, 891, 574, 593, 626, 627, 370, 502, 392, 573, 527, 763, 496, 556, 458, 427, 234, 427, 550, 771,
         601, 568, 568, 544, 544, 544, 593, 572, 223, 593, 573, 544, 568, 593, 573, 593, 544, 574, 565, 664, 717, 550, 669, 873,
         210, 210, 367, 367, 198, 566, 0, 0, 857, 857, 550, 0, 0, 343]
_SANSB = [244, 291, 344, 841, 597, 868, 767, 186, 395, 395, 503, 571, 227, 565, 236, 417, 698, 348, 577, 599, 638, 618, 633, 536,
          625, 633, 239, 263, 571, 571, 571, 534, 1034, 696, 628, 732, 701, 578, 550, 772, 704, 261, 529, 633, 549, 873, 718, 781,
          604, 781, 620, 597, 587, 676, 695, 1003, 650, 618, 567, 358, 417, 358, 661, 706, 228, 574, 646, 596, 646, 592, 362, 585,
          605, 264, 265, 556, 254, 926, 604, 605, 646, 646, 397, 523, 421, 604, 554, 803, 549, 590, 481, 458, 261, 458, 571, 784,
          620, 592, 592, 574, 574, 574, 605, 596, 254, 605, 604, 574, 592, 605, 604, 605, 574, 604, 578, 696, 732, 571, 688, 905,
          242, 242, 428, 428, 236, 652, 0, 0, 872, 880, 571, 0, 0, 357]
_ADV = {'sans': dict(zip(_CH, _SANS)), 'sansb': dict(zip(_CH, _SANSB))}


def _tw(s, size, font='sans', ls=0.0):
    """Measured width of s in user units: font is sans (DM Sans 400), sansb (600) or mono (Space Mono); ls is letter-spacing."""
    s = str(s)
    if font == 'mono':
        return len(s) * (0.612 * size + ls)
    t = _ADV[font]
    return sum(t.get(ch) or 900 for ch in s) / 1000 * size * 1.04 + len(s) * ls


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
    # events (P40, 29 Oct 2026): each label faces right from its stem, left to it or centres on it, in a row below the
    # axis. Given the directions, a label sits below every event whose stem it would cover (so that stem ends above it)
    # and in the first such row its neighbours leave free; the directions are then improved one event at a time until
    # nothing is gained: first no stem through a label, then as few rows as possible. Each label is the date, then the
    # text wrapped at 22.
    lab = {}
    for k, e in enumerate(events):
        lines = [yr(e['at'])] + _wrap(e['label'], 22)
        lab[k] = [x(e['at']), lines, max([_tw(lines[0], 10.5, 'mono')] + [_tw(ln, 12) for ln in lines[1:]])]
    n = len(events)
    def span(k, anchor):
        ex, _, w = lab[k]
        x0 = ex if anchor == 'start' else (ex - w / 2 if anchor == 'middle' else ex - w)
        return x0, x0 + w
    def layout(anch):
        box = {k: span(k, anch[k]) for k in range(n)}
        covers = {k: [j for j in range(n) if j != k and box[k][0] - 4 <= lab[j][0] <= box[k][1] + 4] for k in range(n)}
        rows, left = {}, set(range(n))
        while left:
            ready_ = [k for k in left if all(j in rows for j in covers[k])]
            k = min(ready_ or left, key=lambda k: (sum(j not in rows for j in covers[k]), lab[k][0], k))
            r = max([rows[j] + 1 for j in covers[k] if j in rows], default=0)
            while any(rows[j] == r and box[j][0] - 8 < box[k][1] and box[k][0] < box[j][1] + 8 for j in rows):
                r += 1
            rows[k] = r; left.discard(k)
        cross = sum(1 for k in range(n) for j in covers[k] if rows[k] < rows[j])
        return (cross, max(rows.values(), default=-1) + 1, sum(rows.values())), rows, box
    fits = lambda k, a: 4 <= span(k, a)[0] and span(k, a)[1] <= W - 4
    anch = {k: next((a for a in ('middle', 'start', 'end') if fits(k, a)), 'middle') for k in range(n)}
    best = layout(anch)
    for _ in range(12):
        gained = False
        for k in sorted(range(n), key=lambda k: lab[k][0]):
            for a in ('start', 'middle', 'end'):
                if a == anch[k] or not fits(k, a):
                    continue
                trial = dict(anch); trial[k] = a
                got = layout(trial)
                if got[0] < best[0]:
                    anch, best, gained = trial, got, True
        if not gained:
            break
    _, lane_of, box = best
    for k in range(n):
        lab[k] = (lab[k][0], lab[k][1], anch[k], *box[k])
    rows = max(lane_of.values(), default=0) + 1
    lane_h = 13 * max((len(v[1]) for v in lab.values()), default=1) + 5
    for k, e in enumerate(events):
        ex, lines, anchor, _, _ = lab[k]
        ty = axis + 36 + lane_of[k] * lane_h
        body += f'<line class="viz-stem" x1="{ex:.1f}" y1="{axis}" x2="{ex:.1f}" y2="{ty - 12}"/>'
        body += f'<circle class="viz-dot viz-t{e.get("tone", 1)}" cx="{ex:.1f}" cy="{axis}" r="4"/>'
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


# ---- the IA kinds (V1, 29 Oct 2026) ------------------------------------------------------------------------------
# Every box and the text it holds are one <g data-box>, whose first child is the box: verify.py checks that every text
# in the group lies inside it. Text is measured (_tw) and wrapped to the box (_wrap with px); boxes grow to their text.

# text roles: (class, font, size, letter-spacing, line height)
T_NODE = ('viz-nodelabel', 'sansb', 12, 0, 14)
T_ON = ('viz-ontone', 'sansb', 12, 0, 14)
T_TAG = ('viz-tag', 'mono', 9.5, 0.57, 12)
T_SMALL = ('viz-small', 'mono', 10, 0, 12.5)
T_ATTR = ('viz-attr', 'sans', 11, 0, 14)
T_LINK = ('viz-linklabel', 'sans', 10.5, 0, 12.5)
T_MARK = ('viz-mark', 'mono', 10.5, 0, 13)
T_COL = ('viz-colhead', 'mono', 10, 0.4, 12)
T_LABEL = ('viz-label', 'sans', 12, 0, 14)


def _fail(kind, msg):
    raise SystemExit(f'viz: {kind}: {msg}')


def _tone(o, default, kind):
    t = o.get('tone', default)
    if not isinstance(t, int) or not 1 <= t <= TONES:
        _fail(kind, f'tone must be 1 to {TONES}, got {t!r} in {json.dumps(o)[:80]}')
    return t


def _lines(s, role, px):
    _, font, size, ls, _ = role
    return _wrap(s, 0, px=px, size=size, font=font, ls=ls)


def _width(lines, role):
    _, font, size, ls, _ = role
    return max((_tw(ln, size, font, ls) for ln in lines), default=0)


def _text(lines, role, x, top, anchor='start'):
    """Lines of one role from the top of their block; each line's baseline sits in the middle of its line height."""
    cls, _, size, _, lh = role
    return ''.join(f'<text class="{cls}" x="{x:.1f}" y="{top + lh / 2 + size * 0.36 + i * lh:.1f}" text-anchor="{anchor}">{esc(ln)}</text>'
                   for i, ln in enumerate(lines))


def _g(inner):
    return f'<g data-box="">{inner}</g>'


def _plate(lines, role, cx, cy, lo=4, hi=None):
    """A connector's label on a plate of the card colour, centred on (cx, cy) and kept inside [lo, hi]."""
    lh = role[4]
    w, h = _width(lines, role) + 8, len(lines) * lh + 4
    x = cx - w / 2
    if hi is not None:
        x = min(x, hi - w)
    x = max(x, lo)
    return _g(f'<rect class="viz-lblbg" x="{x:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}"/>'
              + _text(lines, role, x + w / 2, cy - h / 2 + 2, 'middle'))


def _arrow(pts, cls='viz-link'):
    """A polyline whose last point is the tip of an arrowhead; the line stops under the head."""
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    L = math.hypot(x2 - x1, y2 - y1) or 1
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    bx, by = x2 - ux * 7, y2 - uy * 7
    d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in list(pts[:-1]) + [(bx, by)])
    return (f'<path class="{cls}" d="{d}"/><path class="viz-head" d="M{x2:.1f},{y2:.1f} L{bx - uy * 4:.1f},{by + ux * 4:.1f} '
            f'L{bx + uy * 4:.1f},{by - ux * 4:.1f} z"/>')


def _line(pts, cls='viz-line'):
    return f'<path class="{cls}" d="M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>'


def _r(v):
    return round(v, 1)


def sitemap(d):
    """Top-down site structure. The root's children sit in a row that wraps into further rows when wider than the
    drawing (a trunk in a left gutter feeds each row); from depth stack_from (default 2) children stack under their
    parent, indented on a spine, which keeps a deep site legible at phone width. Depth is unlimited."""
    K = 'sitemap'
    NW, GX, GY, IND, SG, G = 132, 14, 36, 20, 10, 16       # box width, sibling gap, level gap, stack indent, stack gap, gutter
    TXT = NW - 16
    stack_from = d.get('stack_from', 2)
    if not isinstance(stack_from, int) or stack_from < 1:
        _fail(K, 'stack_from must be a whole number of at least 1')

    def prep(n, depth, tone):
        if not isinstance(n, dict) or not n.get('label'):
            _fail(K, f'every node needs a label: {json.dumps(n)[:80]}')
        n['_t'] = _tone(n, tone, K)
        tag = _lines(n['type'], T_TAG, TXT) if n.get('type') else []
        lab = _lines(n['label'], T_NODE, TXT)
        note = _lines(n['note'], T_SMALL, TXT) if n.get('note') else []
        n['_txt'] = (tag, lab, note)
        n['_h'] = 8 + len(tag) * 12 + (2 if tag else 0) + len(lab) * 14 + (len(note) * 12.5 + 2 if note else 0) + 8
        for k, c in enumerate(n.get('children') or []):
            prep(c, depth + 1, (k % 5) + 2 if depth == 0 else n['_t'])

    def measure(n, depth, avail):
        if avail < NW:
            _fail(K, f'"{n["label"]}" is too deep to fit the drawing; lower stack_from')
        kids = n.get('children') or []
        n['_mode'] = None
        if not kids:
            n['_w'], n['_bh'] = NW, n['_h']
            return
        if depth + 1 >= stack_from:
            n['_mode'] = 'stack'
            for c in kids:
                measure(c, depth + 1, avail - IND)
            n['_w'] = max(NW, IND + max(c['_w'] for c in kids))
            n['_bh'] = n['_h'] + sum(SG + c['_bh'] for c in kids)
            return
        n['_mode'] = 'rows'
        for c in kids:
            measure(c, depth + 1, avail)
        if sum(c['_w'] for c in kids) + GX * (len(kids) - 1) > avail:
            for c in kids:
                measure(c, depth + 1, avail - G)
            lim = avail - G
        else:
            lim = avail
        rows, cur, cw = [], [], 0
        for c in kids:
            add = c['_w'] + (GX if cur else 0)
            if cur and cw + add > lim:
                rows.append(cur); cur, cw = [c], c['_w']
            else:
                cur.append(c); cw += add
        rows.append(cur)
        n['_rows'], n['_wrap'] = rows, len(rows) > 1
        n['_roww'] = [sum(c['_w'] for c in r) + GX * (len(r) - 1) for r in rows]
        n['_w'] = max(NW, (G if n['_wrap'] else 0) + max(n['_roww']))
        n['_bh'] = n['_h'] + GY + sum(max(c['_bh'] for c in r) for r in rows) + GY * (len(rows) - 1)

    def boxx(n, x):                                         # the box's left edge inside its block
        return x + (n['_w'] - NW) / 2 if n['_mode'] == 'rows' else x

    def box(n, bx, by):
        tag, lab, note = n['_txt']
        s = f'<rect class="viz-node viz-t{n["_t"]}" x="{bx:.1f}" y="{by:.1f}" width="{NW}" height="{n["_h"]:.1f}" rx="2"/>'
        yy = by + 8
        if tag:
            s += _text(tag, T_TAG, bx + 8, yy); yy += len(tag) * 12 + 2
        s += _text(lab, T_NODE, bx + 8, yy); yy += len(lab) * 14
        if note:
            s += _text(note, T_SMALL, bx + 8, yy + 2)
        return _g(s)

    def draw(n, x, y):
        bx = boxx(n, x)
        lines, boxes = '', box(n, bx, y)
        kids = n.get('children') or []
        if not kids:
            return lines, boxes
        bottom = y + n['_h']
        if n['_mode'] == 'stack':
            sx, cy, last = bx + IND / 2, bottom + SG, bottom
            for c in kids:
                l2, b2 = draw(c, bx + IND, cy)
                last = cy + min(c['_h'] / 2, 18)
                lines += l2 + _line([(sx, last), (bx + IND, last)]); boxes += b2
                cy += c['_bh'] + SG
            return _line([(sx, bottom), (sx, last)]) + lines, boxes
        pcx, gut, ry, buses = bx + NW / 2, (G if n['_wrap'] else 0), bottom + GY, []
        for r, rw in zip(n['_rows'], n['_roww']):
            rx, bus, cxs = x + gut + (n['_w'] - gut - rw) / 2, ry - GY / 2, []
            for c in r:
                l2, b2 = draw(c, rx, ry)
                ccx = boxx(c, rx) + NW / 2
                cxs.append(ccx)
                lines += l2 + _line([(ccx, bus), (ccx, ry)]); boxes += b2
                rx += c['_w'] + GX
            buses.append((bus, cxs))
            ry += max(c['_bh'] for c in r) + GY
        if not n['_wrap']:
            bus, cxs = buses[0]
            lines += _line([(pcx, bottom), (pcx, bus)]) + _line([(min(cxs + [pcx]), bus), (max(cxs + [pcx]), bus)])
        else:
            tx = x + G / 2
            lines += _line([(pcx, bottom), (pcx, buses[0][0]), (tx, buses[0][0]), (tx, buses[-1][0])])
            for k, (bus, cxs) in enumerate(buses):
                lines += _line([(tx, bus), (max(cxs + ([pcx] if k == 0 else [])), bus)])
        return lines, boxes

    root = d['root']
    prep(root, 0, 1)
    measure(root, 0, W - 16)
    lines, boxes = draw(root, (W - root['_w']) / 2, 8)
    return _svg(W, _r(8 + root['_bh'] + 8), lines + boxes, 'sitemap', d.get('title'), d.get('caption'))


def _clip(cx, cy, dx, dy, rect):
    """From a point inside rect, the parameter at which the ray (dx, dy) leaves it."""
    x, y, w, h = rect
    ts = []
    if dx > 0: ts.append((x + w - cx) / dx)
    if dx < 0: ts.append((x - cx) / dx)
    if dy > 0: ts.append((y + h - cy) / dy)
    if dy < 0: ts.append((y - cy) / dy)
    return min(ts)


def _hits(p, q, rect, pad=4):
    """Does the segment p-q pass through rect (grown by pad)? Liang-Barsky."""
    x, y, w, h = rect[0] - pad, rect[1] - pad, rect[2] + 2 * pad, rect[3] + 2 * pad
    t0, t1, dx, dy = 0.0, 1.0, q[0] - p[0], q[1] - p[1]
    for pp, qq in ((-dx, p[0] - x), (dx, x + w - p[0]), (-dy, p[1] - y), (dy, y + h - p[1])):
        if pp == 0:
            if qq < 0: return False
        else:
            t = qq / pp
            if pp < 0: t0 = max(t0, t)
            else: t1 = min(t1, t)
    return t0 < t1


def objects(d):
    """An object map: each object a box with a title band, attributes and optional actions, placed in the grid that
    "rows" gives (a row is a list of object ids; null leaves a cell empty); relationships are lines between boxes with
    a label and an optional cardinality at each end. A line that would cross a third box is an error: move a box."""
    K = 'objects'
    objs = {}
    for o in d['objects']:
        if not o.get('id') or not o.get('title'):
            _fail(K, f'every object needs an id and a title: {json.dumps(o)[:80]}')
        if o['id'] in objs:
            _fail(K, f'object {o["id"]!r} is declared twice')
        objs[o['id']] = o
    grid = d['rows']
    cols = max(len(r) for r in grid)
    GX, GY = 56, 72
    bw = min(220, (W - 16 - GX * (cols - 1)) / cols)
    if bw < 110:
        _fail(K, f'{cols} columns leave boxes {bw:.0f} wide; use at most 4 per row')
    TXT = bw - 16
    x0 = (W - (cols * bw + GX * (cols - 1))) / 2
    rects, body, y = {}, '', 8
    for row in grid:
        hs = {}
        for c, oid in enumerate(row):
            if oid is None:
                continue
            if oid not in objs:
                _fail(K, f'rows name {oid!r}, which is not an object')
            if oid in rects or oid in hs:
                _fail(K, f'{oid!r} is placed twice')
            o = objs[oid]
            o['_t'] = _tone(o, 4, K)
            title = _lines(o['title'], T_ON, TXT)
            attrs = [_lines(a, T_ATTR, TXT - 10) for a in o.get('attrs', [])]
            acts = [_lines(a, T_SMALL, TXT - 10) for a in o.get('actions', [])]
            hh = len(title) * 14 + 12
            ah = sum(len(a) * 14 for a in attrs) + sum(len(a) * 12.5 for a in acts) + (10 if attrs or acts else 0) + (10 if acts else 0) + 8
            o['_g'] = (title, attrs, acts, hh)
            hs[oid] = (c, hh + ah)
        rowh = max((h for _, h in hs.values()), default=40)
        for oid, (c, h) in hs.items():
            rects[oid] = (x0 + c * (bw + GX), y, bw, h)
        y += rowh + GY
    missing = [k for k in objs if k not in rects]
    if missing:
        _fail(K, f'objects not placed in rows: {missing}')
    for oid, (x, y0, w, h) in rects.items():
        title, attrs, acts, hh = objs[oid]['_g']
        t = objs[oid]['_t']
        s = (f'<rect class="viz-node viz-t{t}" x="{x:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{h:.1f}" rx="2"/>'
             f'<rect class="viz-solid viz-t{t}" x="{x:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{hh:.1f}" rx="2"/>'
             + _text(title, T_ON, x + 8, y0 + 6))
        yy = y0 + hh + 8
        for a in attrs:
            s += _text(a[:1], T_ATTR, x + 8, yy) + _text(a[1:], T_ATTR, x + 18, yy + 14); yy += len(a) * 14
        if acts:
            s += _line([(x + 8, yy + 5), (x + w - 8, yy + 5)]); yy += 10
            for a in acts:
                s += _text(a[:1], T_SMALL, x + 8, yy) + _text(a[1:], T_SMALL, x + 18, yy + 12.5); yy += len(a) * 12.5
        body += _g(s)
    links = ''
    for e in d.get('links', []):
        a, b = rects.get(e.get('from')), rects.get(e.get('to'))
        if not a or not b or a == b:
            _fail(K, f'a link needs two different objects: {json.dumps(e)[:80]}')
        if abs(a[1] - b[1]) < 0.5:                          # same row: a level line through the shorter box's middle
            yy = a[1] + min(a[3], b[3]) / 2
            P, Q = ((a[0] + a[2], yy), (b[0], yy)) if a[0] < b[0] else ((a[0], yy), (b[0] + b[2], yy))
        elif abs(a[0] - b[0]) < 0.5:                        # same column: a vertical line
            xx = a[0] + a[2] / 2
            P, Q = ((xx, a[1] + a[3]), (xx, b[1])) if a[1] < b[1] else ((xx, a[1]), (xx, b[1] + b[3]))
        else:                                                # otherwise centre to centre, clipped to the boxes
            ca, cb = (a[0] + a[2] / 2, a[1] + a[3] / 2), (b[0] + b[2] / 2, b[1] + b[3] / 2)
            dx, dy = cb[0] - ca[0], cb[1] - ca[1]
            ta, tb = _clip(*ca, dx, dy, a), 1 - _clip(*cb, -dx, -dy, b)
            P, Q = (ca[0] + dx * ta, ca[1] + dy * ta), (ca[0] + dx * tb, ca[1] + dy * tb)
        for oid, rc in rects.items():
            if rc not in (a, b) and _hits(P, Q, rc):
                _fail(K, f'the link {e["from"]} - {e["to"]} would cross {oid}; move one of the boxes')
        links += _line([P, Q], 'viz-link')
        L = math.hypot(Q[0] - P[0], Q[1] - P[1])
        ux, uy = (Q[0] - P[0]) / L, (Q[1] - P[1]) / L
        nx, ny = -uy, ux
        if ny > 0 or (ny == 0 and nx > 0):
            nx, ny = -nx, -ny                                # cardinalities above the line, or left of a vertical one
        for end, pt, sgn in (('from_card', P, 1), ('to_card', Q, -1)):
            if e.get(end):
                tw = _tw(e[end], 10, 'mono')
                along = 8 + abs(ux) * tw / 2 + abs(uy) * 8
                off = 11 + abs(uy) * tw / 2
                cx, cy = pt[0] + sgn * ux * along + nx * off, pt[1] + sgn * uy * along + ny * off
                links += f'<text class="viz-small" x="{cx:.1f}" y="{cy + 3.6:.1f}" text-anchor="middle">{esc(e[end])}</text>'
        if e.get('label'):
            if abs(uy) < 0.01:                               # a level line: the label hangs under it
                lab = _lines(e['label'], T_LINK, max(40, L - 12))
                h = len(lab) * 12.5 + 4
                links += _plate(lab, T_LINK, (P[0] + Q[0]) / 2, P[1] + 4 + h / 2, 4, W - 4)
            else:
                lab = _lines(e['label'], T_LINK, min(bw, 150))
                links += _plate(lab, T_LINK, (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2, 4, W - 4)
    return _svg(W, _r(y - GY + 8), links + body, 'objects', d.get('title'), d.get('caption'))


def decision(d):
    """A decision tree read top-down: question boxes, a labelled arrow per branch, outcomes as filled boxes. Branches
    keep their order left to right and each subtree is packed against its neighbour level by level, so a chain of
    questions runs down a diagonal; a tree wider than the column keeps its size and scrolls."""
    K = 'decision'
    NW, GX = 140, 18
    TXT = NW - 16

    def prep(n, depth):
        if not isinstance(n, dict):
            _fail(K, f'a branch must lead to a node: {n!r}')
        n['_d'] = depth
        if 'outcome' in n:
            n['_lines'], n['_t'] = _lines(n['outcome'], T_ON, TXT), _tone(n, 3, K)
            n['_h'] = len(n['_lines']) * 14 + 16
            return
        if 'q' not in n or not n.get('branches'):
            _fail(K, f'a node is a question with branches or an outcome: {json.dumps(n)[:80]}')
        n['_lines'], n['_t'] = _lines(n['q'], T_NODE, TXT), _tone(n, 4, K)
        n['_h'] = len(n['_lines']) * 14 + 16
        for b in n['branches']:
            if 'to' not in b:
                _fail(K, f'a branch has no "to": {json.dumps(b)[:80]}')
            b['_lab'] = _lines(b['label'], T_LINK, NW + GX - 14) if b.get('label') else []
            prep(b['to'], depth + 1)

    def lay(n):
        """Compact tidy layout: each subtree packed against its left sibling depth by depth (its contour), the
        parent centred over its first and last child; offsets are relative to the parent's centre."""
        if 'outcome' in n:
            return {0: (0.0, 0.0)}
        acc, offs = None, []
        for b in n['branches']:
            cont = lay(b['to'])
            if acc is None:
                shift = 0.0
            else:
                shift = max(acc[k][1] - cont[k][0] + NW + GX for k in cont if k in acc)
            offs.append(shift)
            moved = {k: (lo + shift, hi + shift) for k, (lo, hi) in cont.items()}
            acc = moved if acc is None else {k: (min(acc.get(k, v)[0], v[0]), max(acc.get(k, v)[1], v[1])) for k, v in {**acc, **moved}.items()}
        mid = (offs[0] + offs[-1]) / 2
        n['_offs'] = [o - mid for o in offs]
        out = {0: (0.0, 0.0)}
        for k, (lo, hi) in acc.items():
            out[k + 1] = (lo - mid, hi - mid)
        return out

    def place(n, cx):
        n['_cx'] = cx
        for b, o in zip(n.get('branches', []), n.get('_offs', [])):
            place(b['to'], cx + o)

    root = d['root']
    prep(root, 0)
    cont = lay(root)
    lo, hi = min(v[0] for v in cont.values()), max(v[1] for v in cont.values())
    place(root, -lo + NW / 2)
    span = hi - lo + NW
    levels, gaps = {}, {}
    def walk(n):
        levels[n['_d']] = max(levels.get(n['_d'], 0), n['_h'])
        for b in n.get('branches', []):
            gaps[n['_d']] = max(gaps.get(n['_d'], 48), len(b['_lab']) * 12.5 + 4 + 28)
            walk(b['to'])
    walk(root)
    tops, y = {}, 8
    for k in sorted(levels):
        tops[k] = y
        y += levels[k] + gaps.get(k, 0)
    width = span + 16
    Wd = max(W, width)
    x0 = (Wd - width) / 2 + 8
    body, links = '', ''
    def draw(n):
        nonlocal body, links
        cx, top = x0 + n['_cx'], tops[n['_d']]
        leaf = 'outcome' in n
        cls, role = ('viz-solid', T_ON) if leaf else ('viz-node', T_NODE)
        body += _g(f'<rect class="{cls} viz-t{n["_t"]}" x="{cx - NW / 2:.1f}" y="{top:.1f}" width="{NW}" height="{n["_h"]:.1f}" rx="2"/>'
                   + _text(n['_lines'], role, cx, top + 8, 'middle'))
        if leaf:
            return
        bus = top + levels[n['_d']] + 12
        for b in n['branches']:
            c = b['to']
            ccx, ctop = x0 + c['_cx'], tops[c['_d']]
            pts = [(cx, top + n['_h']), (cx, bus), (ccx, bus), (ccx, ctop)] if abs(ccx - cx) > 0.5 else [(cx, top + n['_h']), (cx, ctop)]
            links += _arrow(pts)
            if b['_lab']:
                links += _plate(b['_lab'], T_LINK, ccx, (bus + ctop - 7) / 2, 4, Wd - 4)
            draw(c)
    draw(root)
    return _svg(_r(Wd), _r(y - gaps.get(max(levels), 0) + 8), links + body, 'decision', d.get('title'), d.get('caption'), wide=Wd > W)


def matrix(d):
    """A labelled grid: row labels down the left, column labels across the top, each cell a short mark or word on a
    field of its tone (an empty cell is blank); an optional legend under the grid says what each mark means."""
    K = 'matrix'
    cols, rows = d['cols'], d['rows']
    if not cols or not rows:
        _fail(K, 'a matrix needs cols and rows')
    if d.get('numeric'):
        return _heat(d)
    LW = min(170, max(90, max(_tw(r['label'], 12) for r in rows) + 20))
    n = len(cols)
    cw = (W - 16 - LW) / n
    wide = cw < 70
    cw = max(cw, 70)
    Wd = 16 + LW + n * cw
    heads = [_lines(c, T_COL, cw - 10) for c in cols]
    hh = max(len(h) for h in heads) * 12 + 12
    body = ''.join(_text(h, T_COL, 8 + LW + (k + 0.5) * cw, hh - 6 - len(h) * 12, 'middle') for k, h in enumerate(heads))
    y = 8 + hh
    for r in rows:
        if len(r.get('cells', [])) != n:
            _fail(K, f'row {r.get("label")!r} has {len(r.get("cells", []))} cells for {n} columns')
        rt = _tone(r, 4, K)
        cells = []
        for c in r['cells']:
            if c is None or c == '':
                cells.append(([], rt))
            elif isinstance(c, str):
                cells.append((_lines(c, T_MARK, cw - 14), rt))
            else:
                cells.append((_lines(c.get('mark', ''), T_MARK, cw - 14) if c.get('mark') else [], _tone(c, rt, K)))
        lab = _lines(r['label'], T_LABEL, LW - 12)
        rh = max(32, max(len(m) for m, _ in cells) * 13 + 14, len(lab) * 14 + 12)
        body += _text(lab, T_LABEL, 8, y + (rh - len(lab) * 14) / 2)
        for k, (m, t) in enumerate(cells):
            x = 8 + LW + k * cw
            cls = f'viz-band viz-t{t}' if m else 'viz-track'
            body += _g(f'<rect class="{cls}" x="{x + 2:.1f}" y="{y + 2:.1f}" width="{cw - 4:.1f}" height="{rh - 4:.1f}"/>'
                       + _text(m, T_MARK, x + cw / 2, y + (rh - len(m) * 13) / 2, 'middle'))
        y += rh
    if d.get('legend'):
        y += 14
        x, lrow = 8, 24
        for item in d['legend']:
            m, means = item.get('mark', ''), item.get('means', '')
            mw = _tw(m, 10.5, 'mono') + 16
            txt = _lines(means, T_ATTR, min(220, W - 16 - mw - 8))
            iw = mw + 8 + _width(txt, T_ATTR) + 18
            if x > 8 and x + iw > Wd - 8:
                x, y, lrow = 8, y + lrow + 8, 24
            body += _g(f'<rect class="viz-band viz-t{_tone(item, 4, K)}" x="{x:.1f}" y="{y:.1f}" width="{mw:.1f}" height="24"/>'
                       + _text([m], T_MARK, x + mw / 2, y + 5.5, 'middle')) + _text(txt, T_ATTR, x + mw + 8, y + 12 - len(txt) * 7)
            x += iw
            lrow = max(lrow, len(txt) * 14)
        y += lrow
    return _svg(_r(Wd), _r(y + 8), body, 'matrix', d.get('title'), d.get('caption'), wide=wide)


def _gridflow(K, items, edges, per_row, bw, gap, gap_px, start=None):
    """The layout and routing shared by states and wireflow. items (each with id, _h and _draw(x, y) -> svg) are laid
    out in rows of per_row in the order given, each centred on its row's midline. An edge to the next box in the row
    (or back to the previous one) is a straight arrow in the gap, its label above (or below); any other edge leaves a
    port on the top or bottom of its box, runs along a lane in the channel between rows and enters its target's top or
    bottom; a self-transition is a loop under its box. An edge across more than one row is an error."""
    idx = {}
    for k, it in enumerate(items):
        if it['id'] in idx:
            _fail(K, f'{it["id"]!r} is declared twice')
        idx[it['id']] = k
    n = len(items)
    R, cols = (n + per_row - 1) // per_row, min(n, per_row)
    sm = 34 if start else 0
    width = 16 + sm + cols * bw + (cols - 1) * gap
    Wd = max(W, width)
    x0 = (Wd - width) / 2 + 8 + sm
    pos = {k: divmod(k, per_row) for k in range(n)}
    X = {k: x0 + pos[k][1] * (bw + gap) for k in range(n)}
    rowh = [max(items[k]['_h'] for k in range(n) if pos[k][0] == r) for r in range(R)]
    gaps, chans, loops, ports = {}, {c: [] for c in range(R + 1)}, {}, {}
    for e in edges:
        a, b = idx.get(e.get('from')), idx.get(e.get('to'))
        if a is None or b is None:
            _fail(K, f'an edge names an unknown box: {json.dumps(e)[:80]}')
        (ra, ca), (rb, cb) = pos[a], pos[b]
        e['_lab'] = e.get('label', '')
        if a == b:
            if a in loops:
                _fail(K, f'{items[a]["id"]!r} has two self-transitions; join their labels')
            loops[a] = e
            continue
        if ra == rb and abs(cb - ca) == 1:
            left, way = (a, 'f') if cb > ca else (b, 'r')
            if way in gaps.setdefault(left, {}):
                _fail(K, f'two edges in the same direction between {items[left]["id"]!r} and its neighbour')
            gaps[left][way] = e
            continue
        if ra == rb:
            ch, sa, sb = (ra + 1, 'b', 'b') if cb > ca else (ra, 't', 't')
        elif rb == ra + 1:
            ch, sa, sb = ra + 1, 'b', 't'
        elif rb == ra - 1:
            ch, sa, sb = ra, 't', 'b'
        else:
            _fail(K, f'the edge {e["from"]} -> {e["to"]} spans more than one row; reorder or change per_row')
        e.update(_a=a, _b=b, _sa=sa, _sb=sb, _ch=ch)
        chans[ch].append(e)
        ports.setdefault((a, sa), []).append((e, '_xa', b))
        ports.setdefault((b, sb), []).append((e, '_xb', a))
    if start is not None:
        if start not in idx or pos[idx[start]][1] != 0:
            _fail(K, f'the start {start!r} must be the first box of a row')
    for (k, side), lst in ports.items():
        lst.sort(key=lambda t: X[t[2]])
        lo, hi = X[k] + 12, X[k] + bw - 12 - (34 if side == 'b' and k in loops else 0)
        bias = 0.1 if side == 't' else -0.1                 # a box above and a box below in one column never share an x
        for i, (e, key, _) in enumerate(lst):
            e[key] = lo + min(0.95, max(0.05, (i + 1) / (len(lst) + 1) + bias)) * (hi - lo)
    # gap labels: room above and below each row's midline
    padT, padB = [0.0] * R, [0.0] * R
    for left, g in gaps.items():
        r = pos[left][0]
        off = 7 if len(g) == 2 else 0
        for way, e in g.items():
            e['_ll'] = _lines(e['_lab'], T_LINK, gap_px) if e['_lab'] else []
            e['_off'] = -off if way == 'f' else off
            need = len(e['_ll']) * 12.5 + 5 + off
            if way == 'f':
                padT[r] = max(padT[r], need - rowh[r] / 2 + 2)
            else:
                padB[r] = max(padB[r], need - rowh[r] / 2 + 2)
    loopband = [0.0] * R
    for k, e in loops.items():
        e['_ll'] = _lines(e['_lab'], T_LINK, 96) if e['_lab'] else []
        loopband[pos[k][0]] = max(loopband[pos[k][0]], 22 + len(e['_ll']) * 12.5 + 6)
    # lanes: each channel edge takes the first lane its label and span fit in
    lanes = {}
    for c, lst in chans.items():
        rows_ = []
        for e in lst:
            xa, xb = e['_xa'], e['_xb']
            span = abs(xb - xa)
            e['_ll'] = _lines(e['_lab'], T_LINK, max(70, min(170, span - 10))) if e['_lab'] else []
            pw = _width(e['_ll'], T_LINK) + 8 if e['_ll'] else 0
            if span < 20 and pw:
                e['_beside'] = True
                fp = (min(xa, xb) - 4, max(xa, xb) + 6 + pw + 4)
            else:
                mid = (xa + xb) / 2
                fp = (min(xa, xb, mid - pw / 2) - 6, max(xa, xb, mid + pw / 2) + 6)
            e['_fp'], e['_ph'] = fp, (len(e['_ll']) * 12.5 + 4 if e['_ll'] else 0)
        for e in sorted(lst, key=lambda e: e['_fp'][1] - e['_fp'][0]):
            for li, occ in enumerate(rows_):
                if all(e['_fp'][1] <= o[0] or e['_fp'][0] >= o[1] for o in occ):
                    occ.append(e['_fp']); e['_lane'] = li; break
            else:
                rows_.append([e['_fp']]); e['_lane'] = len(rows_) - 1
        # order the lanes to cross as few verticals as possible: an edge's end on a box above the channel rises from
        # its lane, an end on a box below drops; a lane above another crosses the lower one's rising ends inside its
        # span, and is crossed by its own dropping ends inside the lower one's span
        L = len(rows_)
        if 1 < L <= 7:
            ups = {li: [] for li in range(L)}; downs = {li: [] for li in range(L)}; spans = {li: [] for li in range(L)}
            for e in lst:
                li = e['_lane']
                spans[li].append((min(e['_xa'], e['_xb']), max(e['_xa'], e['_xb'])))
                for x, side in ((e['_xa'], e['_sa']), (e['_xb'], e['_sb'])):
                    (ups if side == 'b' else downs)[li].append(x)
            inside = lambda xs, sp: sum(1 for x in xs for lo, hi in sp if lo + 0.5 < x < hi - 0.5)
            cost = {(i, j): inside(downs[i], spans[j]) + inside(ups[j], spans[i]) for i in range(L) for j in range(L) if i != j}
            best = min(itertools.permutations(range(L)), key=lambda o: sum(cost[(o[p], o[q])] for p in range(L) for q in range(p + 1, L)))
            rank = {li: p for p, li in enumerate(best)}
            for e in lst:
                e['_lane'] = rank[e['_lane']]
        lanes[c] = [max([16] + [e['_ph'] + 8 for e in lst if e['_lane'] == li]) for li in range(L)]
    chh = {c: (sum(v) + 8 if v else 0) for c, v in lanes.items()}
    ctop, top, cy, y = {}, [0.0] * R, [0.0] * R, 8.0
    for r in range(R):
        ctop[r] = y
        y += max(chh[r], 22 if r else 0)
        top[r] = y
        cy[r] = y + padT[r] + rowh[r] / 2
        y = cy[r] + rowh[r] / 2 + padB[r] + loopband[r]
    ctop[R] = y
    y += chh[R]
    out, body = '', ''
    def lane_y(c, li):
        return ctop[c] + 4 + sum(lanes[c][:li]) + lanes[c][li] / 2
    for k in range(n):
        it = items[k]
        it['_y'] = cy[pos[k][0]] - it['_h'] / 2
        body += it['_draw'](X[k], it['_y'])
    edge_y = lambda k, side: items[k]['_y'] + (items[k]['_h'] if side == 'b' else 0)
    for c, lst in chans.items():
        for e in lst:
            ly = lane_y(c, e['_lane'])
            ya, yb = edge_y(e['_a'], e['_sa']), edge_y(e['_b'], e['_sb'])
            out += _arrow([(e['_xa'], ya), (e['_xa'], ly), (e['_xb'], ly), (e['_xb'], yb)])
            if e['_ll']:
                if e.get('_beside'):
                    w = _width(e['_ll'], T_LINK) + 8
                    out += _plate(e['_ll'], T_LINK, max(e['_xa'], e['_xb']) + 6 + w / 2, ly, 4, Wd - 4)
                else:
                    out += _plate(e['_ll'], T_LINK, (e['_xa'] + e['_xb']) / 2, ly, 4, Wd - 4)
    for left, g in gaps.items():
        r = pos[left][0]
        x1, x2 = X[left] + bw, X[left + 1]
        for way, e in g.items():
            yy = cy[r] + e['_off']
            out += _arrow([(x1, yy), (x2, yy)] if way == 'f' else [(x2, yy), (x1, yy)])
            if e['_ll']:
                lt = yy - 5 - len(e['_ll']) * 12.5 if way == 'f' else yy + 5
                out += _text(e['_ll'], T_LINK, (x1 + x2) / 2, lt, 'middle')
    for k, e in loops.items():
        x1, x2, yb = X[k] + bw - 32, X[k] + bw - 12, edge_y(k, 'b')
        out += (f'<path class="viz-link" d="M{x1:.1f},{yb:.1f} C{x1:.1f},{yb + 24:.1f} {x2:.1f},{yb + 24:.1f} {x2:.1f},{yb + 7:.1f}"/>'
                f'<path class="viz-head" d="M{x2:.1f},{yb:.1f} L{x2 - 4:.1f},{yb + 7:.1f} L{x2 + 4:.1f},{yb + 7:.1f} z"/>')
        if e['_ll']:
            cxl = min((x1 + x2) / 2, Wd - 4 - _width(e['_ll'], T_LINK) / 2)
            out += _text(e['_ll'], T_LINK, cxl, yb + 22, 'middle')
    if start is not None:
        k = idx[start]
        sy = cy[pos[k][0]]
        out += f'<circle class="viz-start" cx="{X[k] - 27:.1f}" cy="{sy:.1f}" r="5"/>' + _arrow([(X[k] - 21, sy), (X[k], sy)])
    return Wd, y + 8, out + body


def states(d):
    """A state diagram: states as rounded boxes in the order given, in rows of per_row (default 4); transitions as
    labelled arrows; a start marker before the start state (default the first; it must begin a row); an end state
    carries an inner ring; a transition from a state to itself is a loop under its box."""
    K = 'states'
    bw, gap = 116, 60
    TXT = bw - 16
    items = []
    for s in d['states']:
        if not s.get('id') or not s.get('label'):
            _fail(K, f'every state needs an id and a label: {json.dumps(s)[:80]}')
        lab = _lines(s['label'], T_NODE, TXT)
        note = _lines(s['note'], T_SMALL, TXT) if s.get('note') else []
        h = max(40, len(lab) * 14 + len(note) * 12.5 + (2 if note else 0) + 18)
        t = _tone(s, 4, K)
        def draw(x, y, s=s, lab=lab, note=note, h=h, t=t):
            r = f'<rect class="viz-node viz-t{t}" x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{h:.1f}" rx="10"/>'
            if s.get('end'):
                r += f'<rect class="viz-endring viz-t{t}" x="{x + 3:.1f}" y="{y + 3:.1f}" width="{bw - 6}" height="{h - 6:.1f}" rx="7"/>'
            bh = len(lab) * 14 + len(note) * 12.5 + (2 if note else 0)
            top = y + (h - bh) / 2
            r += _text(lab, T_NODE, x + bw / 2, top, 'middle')
            if note:
                r += _text(note, T_SMALL, x + bw / 2, top + len(lab) * 14 + 2, 'middle')
            return _g(r)
        items.append(dict(id=s['id'], _h=h, _draw=draw))
    if not items:
        _fail(K, 'a state diagram needs states')
    start = d.get('start', items[0]['id'])                 # "start": null draws no start marker
    per_row = d.get('per_row', 4)
    Wd, h, body = _gridflow(K, items, d.get('transitions', []), per_row, bw, gap, gap - 8, start)
    return _svg(_r(Wd), _r(h), body, 'states', d.get('title'), d.get('caption'), wide=Wd > W)


def wireflow(d):
    """Screens as frames with a title bar and a few content lines, laid out left to right in rows of per_row
    (default 3) and wrapping; arrows between screens carry a label. A content line is a string (text), {"bar": 0.6}
    (a placeholder bar of that share of the width), {"block": 40} (a placeholder area that tall) or {"button": "Pay"}."""
    K = 'wireflow'
    bw, gap = 150, 92
    TXT = bw - 20
    items, H = [], 0
    for s in d['screens']:
        if not s.get('id') or not s.get('title'):
            _fail(K, f'every screen needs an id and a title: {json.dumps(s)[:80]}')
        title = _lines(s['title'], T_NODE, bw - 16)
        bh = len(title) * 14 + 10
        parts, ch = [], 0
        for ln in s.get('lines', []):
            if isinstance(ln, str):
                L = _lines(ln, T_ATTR, TXT); parts.append(('text', L, len(L) * 14 + 4))
            elif 'bar' in ln:
                parts.append(('bar', max(0.1, min(1.0, float(ln['bar']))), 14))
            elif 'block' in ln:
                parts.append(('block', None, max(12, min(120, float(ln['block']))) + 6))
            elif 'button' in ln:
                L = _lines(ln['button'], T_MARK, TXT - 16); parts.append(('button', L, len(L) * 13 + 12 + 6))
            else:
                _fail(K, f'a screen line is text, bar, block or button: {json.dumps(ln)[:80]}')
            ch += parts[-1][2]
        s['_p'] = (title, bh, parts)
        H = max(H, bh + 12 + ch + 10, 190)
    for s in d['screens']:
        title, bh, parts = s['_p']
        t = _tone(s, 3, K)
        def draw(x, y, title=title, bh=bh, parts=parts, t=t):
            r = (f'<rect class="viz-screen viz-t{t}" x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{H:.1f}" rx="2"/>'
                 f'<rect class="viz-band viz-t{t}" x="{x + 2:.1f}" y="{y + 2:.1f}" width="{bw - 4}" height="{bh - 2:.1f}"/>'
                 + _text(title, T_NODE, x + 10, y + 5))
            yy = y + bh + 12
            for kind, v, h in parts:
                if kind == 'text':
                    r += _text(v, T_ATTR, x + 10, yy)
                elif kind == 'bar':
                    r += f'<rect class="viz-ph" x="{x + 10:.1f}" y="{yy + 3:.1f}" width="{TXT * v:.1f}" height="7"/>'
                elif kind == 'block':
                    r += f'<rect class="viz-ph" x="{x + 10:.1f}" y="{yy:.1f}" width="{TXT}" height="{h - 6:.1f}"/>'
                else:
                    r += (f'<rect class="viz-btn viz-t{t}" x="{x + 10:.1f}" y="{yy:.1f}" width="{TXT}" height="{h - 6:.1f}" rx="2"/>'
                          + _text(v, T_MARK, x + bw / 2, yy + 6, 'middle'))
                yy += h
            return _g(r)
        items.append(dict(id=s['id'], _h=H, _draw=draw))
    Wd, h, body = _gridflow(K, items, d.get('links', []), d.get('per_row', 3), bw, gap, gap - 10)
    return _svg(_r(Wd), _r(h), body, 'wireflow', d.get('title'), d.get('caption'), wide=Wd > W)


def swimlanes(d):
    """Lanes per actor or surface stacked top to bottom, each step placed in its lane at the column the data gives
    ("col", from 0); connectors run from step to step, across lanes through the gaps between columns, with optional
    labels. The figure widens with its columns and scrolls sideways inside its frame, like a dense timeline."""
    K = 'swimlanes'
    HW, CW, GX, LP = 112, 124, 76, 14
    lanes = d['lanes']
    lid = {}
    for k, l in enumerate(lanes):
        if not l.get('id') or not l.get('label'):
            _fail(K, f'every lane needs an id and a label: {json.dumps(l)[:80]}')
        lid[l['id']] = k
        l['_t'] = _tone(l, k % TONES + 1, K)
    sid, cell = {}, {}
    for s in d['steps']:
        if s.get('lane') not in lid or not isinstance(s.get('col'), int) or s['col'] < 0 or not s.get('label') or not s.get('id'):
            _fail(K, f'a step needs an id, a label, a known lane and a col from 0: {json.dumps(s)[:80]}')
        if s['id'] in sid:
            _fail(K, f'step {s["id"]!r} is declared twice')
        if (s['lane'], s['col']) in cell:
            _fail(K, f'two steps in lane {s["lane"]!r} at col {s["col"]}')
        sid[s['id']] = s
        cell[(s['lane'], s['col'])] = s
        s['_lab'] = _lines(s['label'], T_NODE, CW - 16)
        s['_note'] = _lines(s['note'], T_SMALL, CW - 16) if s.get('note') else []
        s['_h'] = max(36, 16 + len(s['_lab']) * 14 + (len(s['_note']) * 12.5 + 2 if s['_note'] else 0))
        s['_t'] = _tone(s, lanes[lid[s['lane']]]['_t'], K)
    ncols = max(s['col'] for s in d['steps']) + 1
    X = lambda c: 8 + HW + 16 + c * (CW + GX)
    Wd = max(W, X(ncols - 1) + CW + 16 + 8)
    heads = [_lines(l['label'], T_NODE, HW - 18) for l in lanes]
    lh = [max(56, max([s['_h'] for s in d['steps'] if s['lane'] == l['id']], default=0) + 2 * LP, len(heads[k]) * 14 + 18) for k, l in enumerate(lanes)]
    ltop, y = [], 8
    for h in lh:
        ltop.append(y); y += h
    H = y + 8
    cyl = [ltop[k] + lh[k] / 2 for k in range(len(lanes))]
    bands = ''
    for k, l in enumerate(lanes):
        bands += f'<rect class="viz-lane viz-t{l["_t"]}" x="8" y="{ltop[k]:.1f}" width="{Wd - 16:.1f}" height="{lh[k]:.1f}"/>'
        bands += _g(f'<rect class="viz-band viz-t{l["_t"]}" x="8" y="{ltop[k]:.1f}" width="{HW}" height="{lh[k]:.1f}"/>'
                    + _text(heads[k], T_NODE, 17, cyl[k] - len(heads[k]) * 7))
        if k:
            bands += _line([(8, ltop[k]), (Wd - 8, ltop[k])])
    boxes = ''
    for s in d['steps']:
        k = lid[s['lane']]
        x, yy = X(s['col']), cyl[k] - s['_h'] / 2
        s['_x'], s['_y'] = x, yy
        inner = len(s['_lab']) * 14 + (len(s['_note']) * 12.5 + 2 if s['_note'] else 0)
        top = yy + (s['_h'] - inner) / 2
        r = f'<rect class="viz-node viz-t{s["_t"]}" x="{x:.1f}" y="{yy:.1f}" width="{CW}" height="{s["_h"]:.1f}" rx="2"/>' + _text(s['_lab'], T_NODE, x + 8, top)
        if s['_note']:
            r += _text(s['_note'], T_SMALL, x + 8, top + len(s['_lab']) * 14 + 2)
        boxes += _g(r)
    def blocked(lane, c1, c2):
        lo, hi = min(c1, c2), max(c1, c2)
        return any((lane, c) in cell for c in range(lo + 1, hi))
    plans, slots = [], {}
    for e in d.get('links', []):
        A, B = sid.get(e.get('from')), sid.get(e.get('to'))
        if not A or not B or A is B:
            _fail(K, f'a link needs two different steps: {json.dumps(e)[:80]}')
        la, lb = lid[A['lane']], lid[B['lane']]
        if la == lb:
            if blocked(A['lane'], A['col'], B['col']):
                _fail(K, f'the link {e["from"]} -> {e["to"]} would cross a step in its lane')
            plans.append(('level', e, A, B, None))
        elif A['col'] == B['col']:
            if any((lanes[k]['id'], A['col']) in cell for k in range(min(la, lb) + 1, max(la, lb))):
                _fail(K, f'the link {e["from"]} -> {e["to"]} would cross a step in its column')
            plans.append(('drop', e, A, B, None))
        else:
            fwd = B['col'] > A['col']
            g1 = A['col'] if fwd else A['col'] - 1          # the gap beside A, then along B's lane
            g2 = B['col'] - 1 if fwd else B['col']          # or along A's lane, then the gap beside B
            if not blocked(A['lane'], A['col'], B['col']):   # prefer the run along A's own lane, then up or down beside B
                g = g2
            elif not blocked(B['lane'], A['col'], B['col']):
                g = g1
            else:
                _fail(K, f'the link {e["from"]} -> {e["to"]} has no clear route; move a step')
            slots.setdefault(g, []).append(len(plans))
            plans.append(('elbow', e, A, B, g))
    # ports: the links that leave or enter one side of a step are spread down that side, in the order of their other ends
    side = {}
    for p, (how, e, A, B, g) in enumerate(plans):
        if how == 'drop':
            continue
        fwd = B['col'] > A['col']
        side.setdefault((A['id'], 'r' if fwd else 'l'), []).append((p, 'a', B))
        side.setdefault((B['id'], 'l' if fwd else 'r'), []).append((p, 'b', A))
    py = {}
    for (st, _), lst in side.items():
        S = sid[st]
        lst.sort(key=lambda t: t[2]['_y'] + t[2]['_h'] / 2)
        for i, (p, end, _) in enumerate(lst):
            py[(p, end)] = S['_y'] + S['_h'] * (i + 1) / (len(lst) + 1)
    def route(p, x):
        how, e, A, B, g = plans[p]
        fwd = B['col'] > A['col']
        xa = A['_x'] + CW if fwd else A['_x']
        xb = B['_x'] if fwd else B['_x'] + CW
        return [(xa, py[(p, 'a')]), (x, py[(p, 'a')]), (x, py[(p, 'b')]), (xb, py[(p, 'b')])]
    def crossings(r1, r2):
        n = 0
        for (a1, a2) in zip(r1, r1[1:]):
            for (b1, b2) in zip(r2, r2[1:]):
                h, v = ((a1, a2), (b1, b2)) if abs(a1[1] - a2[1]) < 0.01 else ((b1, b2), (a1, a2))
                if abs(h[0][1] - h[1][1]) > 0.01 or abs(v[0][0] - v[1][0]) > 0.01:
                    continue
                hx0, hx1 = sorted((h[0][0], h[1][0])); vy0, vy1 = sorted((v[0][1], v[1][1]))
                if hx0 + 0.5 < v[0][0] < hx1 - 0.5 and vy0 + 0.5 < h[0][1] < vy1 - 0.5:
                    n += 1
        return n
    sx = {}
    for g, lst in slots.items():                        # the order of the verticals in a gap that crosses least
        xs = [X(g) + CW + GX / 2 + (i - (len(lst) - 1) / 2) * 12 for i in range(len(lst))]
        orders = itertools.permutations(lst) if len(lst) <= 6 else [lst]
        best = min(orders, key=lambda o: sum(crossings(route(o[i], xs[i]), route(o[j], xs[j])) for i in range(len(o)) for j in range(i + 1, len(o))))
        for i, p in enumerate(best):
            sx[p] = xs[i]
    links, plates, segs = '', [], []
    for p, (how, e, A, B, g) in enumerate(plans):
        if how == 'level':
            fwd = B['col'] > A['col']
            x1, x2 = (A['_x'] + CW, B['_x']) if fwd else (A['_x'], B['_x'] + CW)
            y1, y2 = py[(p, 'a')], py[(p, 'b')]
            xm = (x1 + x2) / 2
            pts = [(x1, y1), (x2, y2)] if abs(y1 - y2) < 0.5 else [(x1, y1), (xm, y1), (xm, y2), (x2, y2)]
            links += _arrow(pts); segs.append((p, pts))
            if e.get('label'):                                # the label stands above the line, in the gap
                lab = _lines(e['label'], T_LINK, abs(x2 - x1) - 10)
                links += _text(lab, T_LINK, xm, min(y1, y2) - 4 - len(lab) * 12.5, 'middle')
        elif how == 'drop':
            down = lid[B['lane']] > lid[A['lane']]
            x = A['_x'] + CW / 2
            y1, y2 = (A['_y'] + A['_h'], B['_y']) if down else (A['_y'], B['_y'] + B['_h'])
            links += _arrow([(x, y1), (x, y2)]); segs.append((p, [(x, y1), (x, y2)]))
            if e.get('label'):
                plates.append((p, _lines(e['label'], T_LINK, CW), x, y1, y2))
        else:
            pts = route(p, sx[p])
            links += _arrow(pts); segs.append((p, pts))
            if e.get('label'):
                plates.append((p, _lines(e['label'], T_LINK, GX - 12), sx[p], pts[1][1], pts[2][1]))
    # each label sits on its own vertical, at the first height (from the middle outward) where its plate covers no
    # other link, no step and no label already placed; if there is none, beside the line, left then right
    rects = [(s_['_x'], s_['_y'], CW, s_['_h']) for s_ in d['steps']]
    placed = []
    def clear(p, x, y, w, h):
        r = (x - w / 2, y - h / 2, w, h)
        if any(_hits(a1, a2, r, 1) for q, pts in segs if q != p for a1, a2 in zip(pts, pts[1:])):
            return False
        if any(x0 < r[0] + w + 2 and r[0] < x0 + w0 + 2 and y0 < r[1] + h + 2 and r[1] < y0 + h0 + 2 for x0, y0, w0, h0 in rects + placed):
            return False
        return True
    for p, lines, cx, ya, yb in plates:
        h, w = len(lines) * 12.5 + 4, _width(lines, T_LINK) + 8
        lo, hi = min(ya, yb) + h / 2 + 9, max(ya, yb) - h / 2 - 9
        mid = (ya + yb) / 2
        cands = [mid] + [mid + sgn * k * 4 for k in range(1, 60) for sgn in (1, -1)]
        spot = next(((cx + dx, c) for dx in (0, -(w / 2 + 4), w / 2 + 4) for c in cands if lo <= c <= hi and clear(p, cx + dx, c, w, h)), (cx, mid))
        placed.append((spot[0] - w / 2, spot[1] - h / 2, w, h))
        links += _plate(lines, T_LINK, spot[0], spot[1], 4, Wd - 4)
    return _svg(_r(Wd), _r(H), bands + links + boxes, 'swimlanes', d.get('title'), d.get('caption'), wide=Wd > W)


# ---- the data kinds (P44, 29 Oct 2026): line, bars, scatter, range, and matrix's numeric mode -----------------------
# Labels that could collide (point labels, legend entries, quadrant names, range tags) sit on plates (<g data-box>, a
# card-coloured rect first), so verify.py's box checks also prove that no two of them overlap. Placement tries a short
# list of positions and raises when none is free: a figure whose labels cannot be placed is a bug, not a blank.

T_VAL = ('viz-value', 'mono', 10.5, 0, 13)
T_TICK = ('viz-ticklabel', 'mono', 10.5, 0, 13)
T_QUAD = ('viz-quadname', 'mono', 10, 0.4, 12.5)
T_ONV = ('viz-onvalue', 'mono', 10.5, 0, 13)


def _num(v, kind, what):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v != v:
        _fail(kind, f'{what} must be a number, got {v!r}')
    return v


def _fmt(v, dec=None):
    """A number as the figure prints it: thousands with commas; decimals as given, or as the data carries them."""
    if dec is not None:
        return f'{v:,.{dec}f}'
    if isinstance(v, float):
        v = round(v, 9)
        if v.is_integer():
            v = int(v)
    return f'{v:,}'


def _ticks(lo, hi, n=5):
    """Round tick values covering lo..hi, about n intervals."""
    if hi <= lo:
        hi = lo + 1
    raw = (hi - lo) / n
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw)
    a, b = math.floor(lo / step + 1e-9) * step, math.ceil(hi / step - 1e-9) * step
    k = round((b - a) / step)
    return [round(a + i * step, 9) for i in range(k + 1)]


def _box(cx, cy, lines, role):
    """The rect a plate of these lines centred on (cx, cy) occupies."""
    w, h = _width(lines, role) + 8, len(lines) * role[4] + 4
    return (cx - w / 2, cy - h / 2, w, h)


def _clash(r, rects, pad=2):
    return any(x < r[0] + r[2] + pad and r[0] < x + w + pad and y < r[1] + r[3] + pad and r[1] < y + h + pad for x, y, w, h in rects)


def _plate_at(rect, lines, role):
    x, y, w, h = rect
    return _g(f'<rect class="viz-lblbg" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"/>' + _text(lines, role, x + w / 2, y + 2, 'middle'))


def _legend(items, top, width, kind):
    """Legend entries left to right, wrapping: a swatch (a bar's square or a line with its point) and the name, each one
    plate. items: [(name, tone, 'bar' or 'line')]. Returns (svg, height)."""
    x, y, s, rowh = 8, top, '', 20
    for name, tone, style in items:
        lab = _lines(name, T_LABEL, 200)
        tw = _width(lab, T_LABEL)
        iw = 8 + (22 if style == 'line' else 12) + 6 + tw + 6
        ih = max(20, len(lab) * 14 + 6)
        if x > 8 and x + iw > width - 8:
            x, y, rowh = 8, y + rowh + 4, 20
        sw_x, cy = x + 4, y + ih / 2
        sw = (f'<line class="viz-series viz-t{tone}" x1="{sw_x:.1f}" y1="{cy:.1f}" x2="{sw_x + 22:.1f}" y2="{cy:.1f}"/>'
              f'<circle class="viz-pt viz-t{tone}" cx="{sw_x + 11:.1f}" cy="{cy:.1f}" r="3.5"/>') if style == 'line' else \
             f'<rect class="viz-bar viz-t{tone}" x="{sw_x:.1f}" y="{cy - 6:.1f}" width="12" height="12"/>'
        tx = sw_x + (22 if style == 'line' else 12) + 6
        s += _g(f'<rect class="viz-lblbg" x="{x:.1f}" y="{y:.1f}" width="{iw:.1f}" height="{ih:.1f}"/>' + sw
                + _text(lab, T_LABEL, tx, cy - len(lab) * 7))
        x += iw + 10
        rowh = max(rowh, ih)
    return s, (y + rowh) - top


def line(d):
    """One or more named series over an ordered x (years, periods or any ordered labels), each point labelled with its
    value (or only the first and last), optional annotations as dashed verticals with a note, and a legend."""
    K = 'line'
    xs, series = d.get('x'), d.get('series')
    if not xs or not series:
        _fail(K, 'a line chart needs x and series')
    n = len(xs)
    numeric = all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in xs)
    if numeric and any(b <= a for a, b in zip(xs, xs[1:])):
        _fail(K, 'numeric x values must increase')
    years, unit, dec = d.get('years', False), d.get('unit', ''), d.get('decimals')
    fx = (lambda v: yr(v)) if (years and numeric) else (lambda v: _fmt(v) if numeric else str(v))
    vals = []
    for k, s in enumerate(series):
        if len(s.get('values', [])) != n:
            _fail(K, f'series {s.get("name", k)!r} has {len(s.get("values", []))} values for {n} x values')
        if len(series) > 1 and not s.get('name'):
            _fail(K, 'with more than one series every series needs a name')
        s['_t'] = _tone(s, d.get('tone', 1) if len(series) == 1 else k % TONES + 1, K)
        vals += [_num(v, K, 'a value') for v in s['values'] if v is not None]
    if not vals:
        _fail(K, 'no values to draw')
    lo = d.get('min', min(0, min(vals)))
    hi = d.get('max', max(vals))
    yt = d.get('yticks') or _ticks(lo, hi)
    lo, hi = min(lo, yt[0]), max(hi, yt[-1])
    ylab = [_fmt(t, dec) + unit for t in yt]
    L = 8 + max(_tw(t, 10.5, 'mono') for t in ylab) + 8
    R = W - 24
    body, plates, top = '', [], 8
    if d.get('ylabel'):
        body += _text([d['ylabel']], T_COL, 8, top); top += 18
    if any(s.get('name') for s in series):
        lg, lh = _legend([(s.get('name', ''), s['_t'], 'line') for s in series if s.get('name')], top, W, K)
        body += lg; top += lh + 12
    if numeric:
        span = xs[-1] - xs[0]
        px = lambda v: (L + R) / 2 if span == 0 else L + 14 + (R - L - 28) * (v - xs[0]) / span
    else:
        px = lambda i: L + (R - L) * (i + 0.5) / n
    xpos = [px(v) if numeric else px(i) for i, v in enumerate(xs)]
    # annotations: their notes in rows above the plot, each row's plates kept apart
    anns = []
    for a in d.get('annotations', []):
        at = a.get('at')
        if numeric:
            _num(at, K, 'an annotation\'s at')
            if not xs[0] <= at <= xs[-1]:
                _fail(K, f'annotation at {at} is outside the x range')
            ax = px(at)
        else:
            if at not in xs:
                _fail(K, f'annotation at {at!r} is not one of the x values')
            ax = xpos[xs.index(at)]
        lab = _lines(a.get('label', ''), T_LINK, 130)
        anns.append([ax, lab])
    arow, rows_used = [], []
    for ax, lab in anns:
        w = _width(lab, T_LINK) + 8
        cx = min(max(ax, 4 + w / 2), W - 4 - w / 2)
        r = 0
        while any(rr == r and abs(cx - ox) < (w + ow) / 2 + 6 for rr, ox, ow, _ in arow):
            r += 1
        arow.append((r, cx, w, lab))
    ann_h = 0
    if arow:
        rh = max(len(l) for *_, l in arow) * 12.5 + 8
        ann_h = (max(r for r, *_ in arow) + 1) * rh
    PT = top + ann_h + 18
    PH = d.get('height', 240)
    PB = PT + PH
    py = lambda v: PB - (v - lo) / (hi - lo) * PH
    for k, (ax, lab) in enumerate(anns):
        r, cx, w, _ = arow[k]
        h = len(lab) * 12.5 + 4
        rect = (cx - w / 2, top + r * rh, w, h)
        body += _line([(ax, rect[1] + h), (ax, PB)], 'viz-annot')
        plates.append(rect)
        body += _plate_at(rect, lab, T_LINK)
    grid = ''
    for t, tl in zip(yt, ylab):
        yy = py(t)
        grid += _line([(L, yy), (R, yy)], 'viz-base' if t == 0 else 'viz-grid')
        grid += f'<text class="viz-ticklabel" x="{L - 6:.1f}" y="{yy + 3.6:.1f}" text-anchor="end">{esc(tl)}</text>'
    # x tick labels: every x value when they fit, else every k-th (always the first and the last)
    xl = [fx(v) for v in xs]
    if numeric:
        tickx = d.get('xticks') or xs
        lab_of = {v: fx(v) for v in tickx}
        wmax = max(_tw(t, 10.5, 'mono') for t in lab_of.values())
        step = 1
        if len(tickx) > 1:
            dmin = min(b - a for a, b in zip(tickx, tickx[1:])) * (R - L - 28) / max(1e-9, xs[-1] - xs[0])
            step = max(1, math.ceil((wmax + 10) / max(dmin, 1)))
        show = [v for i, v in enumerate(tickx) if i % step == 0 or i == len(tickx) - 1]
        if len(show) > 1 and step > 1 and (px(show[-1]) - px(show[-2])) < wmax + 10:
            show.pop(-2)
        xlh = 13
        for v in show:
            body += f'<line class="viz-grid" x1="{px(v):.1f}" y1="{PB}" x2="{px(v):.1f}" y2="{PB + 4}"/><text class="viz-ticklabel" x="{px(v):.1f}" y="{PB + 16:.1f}" text-anchor="middle">{esc(lab_of[v])}</text>'
    else:
        cw = (R - L) / n
        wrapped = [_wrap(t, 0, px=max(24, cw - 6), size=10.5, font='mono') for t in xl]
        xlh = max(len(w) for w in wrapped) * 13
        for x_, w_ in zip(xpos, wrapped):
            body += _text(w_, T_TICK, x_, PB + 6, 'middle')
    # series: lines through the values (a null breaks the line), points, then labels
    segs, pts, marks = [], [], ''
    for s in series:
        run = []
        for x_, v in zip(xpos, s['values']):
            if v is None:
                if len(run) > 1:
                    segs.append((s['_t'], run))
                run = []
                continue
            run.append((x_, py(v)))
            pts.append((x_, py(v)))
        if len(run) > 1:
            segs.append((s['_t'], run))
    for t, run in segs:
        marks += _line(run, f'viz-series viz-t{t}')
    for s in series:
        for x_, v in zip(xpos, s['values']):
            if v is not None:
                marks += f'<circle class="viz-pt viz-t{s["_t"]}" cx="{x_:.1f}" cy="{py(v):.1f}" r="3.5"/>'
    mode = d.get('labels', 'all' if n <= 8 else 'ends')
    if mode not in ('all', 'ends', 'none'):
        _fail(K, 'labels is "all", "ends" or "none"')
    dots = [(x_ - 5, y_ - 5, 10, 10) for x_, y_ in pts]
    lines_all = [(a, b) for _, run in segs for a, b in zip(run, run[1:])]
    labs = ''
    for s in series:
        idx = [i for i, v in enumerate(s['values']) if v is not None]
        if mode == 'ends':
            idx = sorted({idx[0], idx[-1]}) if idx else []
        elif mode == 'none':
            idx = []
        for i in idx:
            x_, y_ = xpos[i], py(s['values'][i])
            lab = [_fmt(s['values'][i], dec) + unit]
            w, h = _width(lab, T_VAL) + 8, 17
            cands = [(x_, y_ - 13), (x_, y_ + 13), (x_ + w / 2 + 7, y_), (x_ - w / 2 - 7, y_),
                     (x_ + w / 2 + 3, y_ - 12), (x_ - w / 2 - 3, y_ - 12), (x_ + w / 2 + 3, y_ + 12), (x_ - w / 2 - 3, y_ + 12),
                     (x_, y_ - 26), (x_, y_ + 26)]
            ok = lambda r: L + 2 <= r[0] and r[0] + r[2] <= W - 4 and PT - 16 <= r[1] and r[1] + r[3] <= PB - 1 and not _clash(r, plates + dots, 1)
            free = [c for c in cands if ok((c[0] - w / 2, c[1] - h / 2, w, h))]
            clear = [c for c in free if not any(_hits(a, b, (c[0] - w / 2, c[1] - h / 2, w, h), 0) for a, b in lines_all)]
            if not free:
                _fail(K, f'no room for the label {lab[0]} at {xl[i]} in {s.get("name", "the series")!r}; use "labels": "ends" or a taller "height"')
            c = (clear or free)[0]
            rect = (c[0] - w / 2, c[1] - h / 2, w, h)
            plates.append(rect)
            labs += _plate_at(rect, lab, T_VAL)
    H = PB + 6 + xlh + 8
    if d.get('xlabel'):
        body += f'<text class="viz-colhead" x="{R:.1f}" y="{H + 6:.1f}" text-anchor="end">{esc(d["xlabel"])}</text>'
        H += 16
    # the figure's class is viz-linechart: viz-line is already the class of a structural line, and would style the figure
    return _svg(W, _r(H), grid + body + marks + labs, 'linechart', d.get('title'), d.get('caption'))


def bars(d):
    """Grouped or stacked horizontal bars across categories: one bar per series in each row (grouped) or one bar of
    segments (stacked); values at the bar ends (a stacked bar's total at its end, a segment's value inside it when it
    fits); a legend names the series."""
    K = 'bars'
    series, rows = d.get('series'), d.get('rows')
    mode = d.get('mode', 'grouped')
    if mode not in ('grouped', 'stacked'):
        _fail(K, 'mode is "grouped" or "stacked"')
    if not series or not rows:
        _fail(K, 'bars need series and rows')
    ns = len(series)
    unit, dec = d.get('unit', ''), d.get('decimals')
    for k, s in enumerate(series):
        if not s.get('name'):
            _fail(K, 'every series needs a name')
        s['_t'] = _tone(s, k % TONES + 1, K)
    for r in rows:
        if len(r.get('values', [])) != ns:
            _fail(K, f'row {r.get("label")!r} has {len(r.get("values", []))} values for {ns} series')
        for v in r['values']:
            if v is not None and _num(v, K, 'a value') < 0:
                _fail(K, 'bars draw values of 0 or more')
    tot = [sum(v or 0 for v in r['values']) for r in rows]
    big = max(tot) if mode == 'stacked' else max(v or 0 for r in rows for v in r['values'])
    mx = d.get('max') or _ticks(0, big or 1)[-1]
    labs = [_lines(r['label'], T_LABEL, 160) for r in rows]
    LW = min(172, max(_width(l, T_LABEL) for l in labs) + 12)
    vals = [_fmt(v, dec) + unit for r, t in zip(rows, tot) for v in (r['values'] + [t])]
    VW = max(_tw(v, 10.5, 'mono') for v in vals) + 12
    bx, bw = 8 + LW, W - 8 - (8 + LW) - VW
    body, top = '', 8
    lg, lh = _legend([(s['name'], s['_t'], 'bar') for s in series], top, W, K)
    body += lg; top += lh + 14
    y, marks = top, ''
    BH, BG = (12, 3) if mode == 'grouped' else (20, 0)
    for r, lab, t in zip(rows, labs, tot):
        block = ns * BH + (ns - 1) * BG if mode == 'grouped' else BH
        rh = max(block, len(lab) * 14)
        by = y + (rh - block) / 2
        marks += _text(lab, T_LABEL, bx - 10, y + (rh - len(lab) * 14) / 2, 'end')
        if mode == 'grouped':
            for k, (s, v) in enumerate(zip(series, r['values'])):
                yy = by + k * (BH + BG)
                if v is None:
                    continue
                wv = bw * v / mx
                if wv > 0:
                    marks += f'<rect class="viz-bar viz-t{s["_t"]}" x="{bx:.1f}" y="{yy:.1f}" width="{wv:.1f}" height="{BH}"/>'
                marks += f'<text class="viz-value" x="{bx + wv + 6:.1f}" y="{yy + BH / 2 + 3.8:.1f}">{esc(_fmt(v, dec) + unit)}</text>'
        else:
            xx = bx
            for s, v in zip(series, r['values']):
                if not v:
                    continue
                wv = bw * v / mx
                vt = _fmt(v, dec) + unit
                rect = f'<rect class="viz-bar viz-t{s["_t"]}" x="{xx:.1f}" y="{by:.1f}" width="{wv:.1f}" height="{BH}"/>'
                if _tw(vt, 10.5, 'mono') + 10 <= wv:
                    marks += _g(rect + _text([vt], T_ONV, xx + wv / 2, by + (BH - 13) / 2, 'middle'))
                else:
                    marks += rect
                xx += wv
            marks += f'<text class="viz-value" x="{xx + 6:.1f}" y="{by + BH / 2 + 3.8:.1f}">{esc(_fmt(t, dec) + unit)}</text>'
        y += rh + 14
    base = _line([(bx, top - 4), (bx, y - 10)], 'viz-base')
    return _svg(W, _r(y - 14 + 8), body + base + marks, 'bars', d.get('title'), d.get('caption'))


def scatter(d):
    """Labelled points on two numeric axes with gridlines at the ticks, optional quadrant lines with a name in each
    quadrant's outer corner; each label is placed where it covers no point, no other label and no quadrant name."""
    K = 'scatter'
    pts = d.get('points')
    if not pts:
        _fail(K, 'a scatter needs points')
    ax = {}
    for a in ('x', 'y'):
        o = d.get(a) or {}
        vs = [_num(p.get(a), K, f'a point\'s {a}') for p in pts]
        lo, hi = o.get('min', min(vs)), o.get('max', max(vs))
        t = o.get('ticks') or _ticks(lo, hi)
        ax[a] = dict(lo=min(lo, t[0]), hi=max(hi, t[-1]), ticks=t, unit=o.get('unit', ''), dec=o.get('decimals'),
                     label=o.get('label', ''), years=o.get('years', False))
    tl = lambda a, v: yr(v) if ax[a]['years'] else _fmt(v, ax[a]['dec']) + ax[a]['unit']
    L = 8 + max(_tw(tl('y', t), 10.5, 'mono') for t in ax['y']['ticks']) + 8
    R, top = W - 12, 8
    body = ''
    if ax['y']['label']:
        body += _text([ax['y']['label']], T_COL, 8, top); top += 18
    PT, PH = top + 6, d.get('height', 340)
    PB = PT + PH
    X = lambda v: L + (v - ax['x']['lo']) / (ax['x']['hi'] - ax['x']['lo']) * (R - L)
    Y = lambda v: PB - (v - ax['y']['lo']) / (ax['y']['hi'] - ax['y']['lo']) * PH
    for t in ax['y']['ticks']:
        body += _line([(L, Y(t)), (R, Y(t))], 'viz-grid') + f'<text class="viz-ticklabel" x="{L - 6:.1f}" y="{Y(t) + 3.6:.1f}" text-anchor="end">{esc(tl("y", t))}</text>'
    xt = ax['x']['ticks']
    for i, t in enumerate(xt):
        hw_ = _tw(tl('x', t), 10.5, 'mono') / 2
        anchor = 'start' if X(t) - hw_ < 4 else ('end' if X(t) + hw_ > W - 4 else 'middle')
        body += _line([(X(t), PT), (X(t), PB)], 'viz-grid') + f'<text class="viz-ticklabel" x="{X(t):.1f}" y="{PB + 16:.1f}" text-anchor="{anchor}">{esc(tl("x", t))}</text>'
    body += _line([(L, PB), (R, PB)], 'viz-base') + _line([(L, PT), (L, PB)], 'viz-base')
    plates, marks = [], ''
    dots = [(X(p['x']) - 5.5, Y(p['y']) - 5.5, 11, 11) for p in pts]
    q = d.get('quadrants')
    if q:
        qx, qy = X(_num(q.get('x'), K, 'quadrants.x')), Y(_num(q.get('y'), K, 'quadrants.y'))
        body += _line([(qx, PT), (qx, PB)], 'viz-quad') + _line([(L, qy), (R, qy)], 'viz-quad')
        names = q.get('names') or []
        corners = [(L + 6, PT + 6, 'l', 't'), (R - 6, PT + 6, 'r', 't'), (L + 6, PB - 6, 'l', 'b'), (R - 6, PB - 6, 'r', 'b')]
        for name, (cx, cy, hx, vy), (lo_x, hi_x) in zip(names, corners, [(L, qx), (qx, R), (L, qx), (qx, R)]):
            if not name:
                continue
            lab = _lines(name, T_QUAD, max(60, (hi_x - lo_x) / 2))
            w, h = _width(lab, T_QUAD) + 8, len(lab) * 12.5 + 4
            rect = (cx if hx == 'l' else cx - w, cy if vy == 't' else cy - h, w, h)
            if _clash(rect, dots, 1):
                _fail(K, f'the quadrant name {name!r} would cover a point; shorten it or widen the axis range')
            plates.append(rect)
            marks += _plate_at(rect, lab, T_QUAD)
    for p in pts:
        marks += f'<circle class="viz-pt viz-t{_tone(p, d.get("tone", 4), K)}" cx="{X(p["x"]):.1f}" cy="{Y(p["y"]):.1f}" r="4.5"/>'
    # labels, most crowded points first; each takes the first free spot of a ring of candidates, nearest first
    order = sorted(range(len(pts)), key=lambda i: -sum(1 for j in range(len(pts)) if math.hypot(X(pts[i]['x']) - X(pts[j]['x']), Y(pts[i]['y']) - Y(pts[j]['y'])) < 60))
    labs = ''
    for i in order:
        p = pts[i]
        if not p.get('label'):
            continue
        x_, y_ = X(p['x']), Y(p['y'])
        lab = _lines(p['label'], T_LABEL, 150)
        w, h = _width(lab, T_LABEL) + 8, len(lab) * 14 + 4
        cands = []
        for dist in (8, 16, 28):
            cands += [(x_ + dist + w / 2, y_), (x_ - dist - w / 2, y_), (x_, y_ - dist - h / 2), (x_, y_ + dist + h / 2),
                      (x_ + dist / 2 + w / 2, y_ - dist / 2 - h / 2), (x_ - dist / 2 - w / 2, y_ - dist / 2 - h / 2),
                      (x_ + dist / 2 + w / 2, y_ + dist / 2 + h / 2), (x_ - dist / 2 - w / 2, y_ + dist / 2 + h / 2)]
        spot = next((c for c in cands if L + 2 <= c[0] - w / 2 and c[0] + w / 2 <= W - 4 and PT - 4 <= c[1] - h / 2 and c[1] + h / 2 <= PB - 2
                     and not _clash((c[0] - w / 2, c[1] - h / 2, w, h), plates + dots, 1)), None)
        if spot is None:
            _fail(K, f'no room for the label {p["label"]!r}; shorten it, widen an axis range or raise "height"')
        rect = (spot[0] - w / 2, spot[1] - h / 2, w, h)
        plates.append(rect)
        labs += _plate_at(rect, lab, T_LABEL)
    H = PB + 24
    if ax['x']['label']:
        body += f'<text class="viz-colhead" x="{R:.1f}" y="{H + 4:.1f}" text-anchor="end">{esc(ax["x"]["label"])}</text>'
        H += 16
    return _svg(W, _r(H), body + marks + labs, 'scatter', d.get('title'), d.get('caption'))


def range_(d):
    """Competing estimates: per row, a label, then a bar from the lowest to the highest estimate with an optional point
    estimate (its value above it), and under the bar each end's value with a short source tag, aligned to its end of
    the bar (inside the bar's span when both fit, else outside it). A shared axis with gridlines runs under the rows."""
    K = 'range'
    rows = d.get('rows')
    if not rows:
        _fail(K, 'a range needs rows')
    unit, dec = d.get('unit', ''), d.get('decimals')
    vs = []
    for r in rows:
        if not r.get('label'):
            _fail(K, 'every row needs a label')
        lo_, hi_ = _num(r.get('low'), K, 'low'), _num(r.get('high'), K, 'high')
        if hi_ < lo_:
            _fail(K, f'row {r["label"]!r}: high is below low')
        if r.get('point') is not None and not lo_ <= _num(r['point'], K, 'point') <= hi_:
            _fail(K, f'row {r["label"]!r}: the point estimate lies outside its range')
        vs += [lo_, hi_]
    lo, hi = d.get('min', min(0, min(vs))), d.get('max', max(vs))
    ticks = d.get('ticks') or _ticks(lo, hi)
    lo, hi = min(lo, ticks[0]), max(hi, ticks[-1])
    PL, PR = 24, W - 24
    X = lambda v: PL + (v - lo) / (hi - lo) * (PR - PL)
    tag = lambda v, src: _fmt(v, dec) + unit + (f' · {src}' if src else '')
    y, marks, plates = 8, '', []
    for r in rows:
        t = _tone(r, d.get('tone', 4), K)
        lab = _lines(r['label'], T_LABEL, W - 16)
        marks += _text(lab, T_LABEL, 8, y)
        y += len(lab) * 14 + 4
        if r.get('point') is not None:
            pv = [_fmt(r['point'], dec) + unit]
            pw = _width(pv, T_VAL)
            px_ = min(max(X(r['point']), 8 + pw / 2), W - 8 - pw / 2)
            marks += _text(pv, T_VAL, px_, y, 'middle')
            y += 14
        x1, x2 = X(r['low']), X(r['high'])
        marks += f'<rect class="viz-rangebar viz-t{t}" x="{x1:.1f}" y="{y:.1f}" width="{max(x2 - x1, 3):.1f}" height="10"/>'
        if r.get('point') is not None:
            cx = X(r['point'])
            marks += f'<path class="viz-est" d="M{cx:.1f},{y - 2:.1f} L{cx + 7:.1f},{y + 5:.1f} L{cx:.1f},{y + 12:.1f} L{cx - 7:.1f},{y + 5:.1f} z"/>'
        y += 14
        lt, ht = [tag(r['low'], r.get('low_src'))], [tag(r['high'], r.get('high_src'))]
        lw, hw = _width(lt, T_VAL) + 8, _width(ht, T_VAL) + 8
        if lw + hw + 8 <= x2 - x1 + 8:                        # both tags fit under the bar: each reads inward from its end
            a, b = (x1 - 4, y, lw, 17), (x2 + 4 - hw, y, hw, 17)
        else:                                                # else outward: the low one left of the start, the high one right of the end
            a = (max(4, x1 - lw + 4), y, lw, 17)
            b = (min(W - 4 - hw, x2 - 4), y, hw, 17)
        if r['low'] == r['high'] and not r.get('low_src') and not r.get('high_src'):
            marks += _plate_at(a, lt, T_VAL); plates.append(a); y += 17
        else:
            if _clash(a, [b], 2):
                b = (b[0], y + 18, hw, 17)
            marks += _plate_at(a, lt, T_VAL) + _plate_at(b, ht, T_VAL)
            y = max(a[1] + a[3], b[1] + b[3])
        y += 16
    grid = ''
    for tk in ticks:
        grid += _line([(X(tk), 8), (X(tk), y - 8)], 'viz-grid')
        grid += f'<text class="viz-ticklabel" x="{X(tk):.1f}" y="{y + 6:.1f}" text-anchor="middle">{esc(_fmt(tk, dec) + unit)}</text>'
    H = y + 14
    if d.get('xlabel'):
        grid += f'<text class="viz-colhead" x="{PR:.1f}" y="{H + 6:.1f}" text-anchor="end">{esc(d["xlabel"])}</text>'
        H += 16
    return _svg(W, _r(H), grid + marks, 'range', d.get('title'), d.get('caption'))


def _heat(d):
    """matrix with "numeric": true: each cell a number (or null for blank) on one of five shades of the figure's tone,
    shaded by value between min and max (default the data's); a legend under the grid gives each shade's range."""
    K = 'matrix'
    cols, rows = d['cols'], d['rows']
    tone = _tone(d, 4, K)
    unit, dec = d.get('unit', ''), d.get('decimals')
    vs = []
    for r in rows:
        if len(r.get('cells', [])) != len(cols):
            _fail(K, f'row {r.get("label")!r} has {len(r.get("cells", []))} cells for {len(cols)} columns')
        vs += [_num(c, K, 'a numeric cell') for c in r['cells'] if c is not None]
    if not vs:
        _fail(K, 'a numeric matrix needs numbers')
    lo, hi = d.get('min', min(vs)), d.get('max', max(vs))
    if hi <= lo:
        hi = lo + 1
    lev = lambda v: min(5, max(1, 1 + int((v - lo) / (hi - lo) * 5 - 1e-9))) if v > lo else 1
    LW = min(170, max(90, max(_tw(r['label'], 12) for r in rows) + 20))
    n = len(cols)
    cw = (W - 16 - LW) / n
    wide = cw < 64
    cw = max(cw, 64)
    Wd = 16 + LW + n * cw
    heads = [_lines(c, T_COL, cw - 10) for c in cols]
    hh = max(len(h) for h in heads) * 12 + 12
    body = ''.join(_text(h, T_COL, 8 + LW + (k + 0.5) * cw, hh - 6 - len(h) * 12, 'middle') for k, h in enumerate(heads))
    y = 8 + hh
    for r in rows:
        lab = _lines(r['label'], T_LABEL, LW - 12)
        rh = max(32, len(lab) * 14 + 12)
        body += _text(lab, T_LABEL, 8, y + (rh - len(lab) * 14) / 2)
        for k, c in enumerate(r['cells']):
            x = 8 + LW + k * cw
            if c is None:
                body += f'<rect class="viz-track" x="{x + 2:.1f}" y="{y + 2:.1f}" width="{cw - 4:.1f}" height="{rh - 4:.1f}"/>'
                continue
            lv = lev(c)
            role = ('viz-markon',) + T_MARK[1:] if lv == 5 else T_MARK
            m = _lines(_fmt(c, dec) + unit, role, cw - 12)
            body += _g(f'<rect class="viz-t{tone} viz-h{lv}" x="{x + 2:.1f}" y="{y + 2:.1f}" width="{cw - 4:.1f}" height="{rh - 4:.1f}"/>'
                       + _text(m, role, x + cw / 2, y + (rh - len(m) * 13) / 2, 'middle'))
        y += rh
    # the scale: five shades with the range each one covers
    y += 14
    step = (hi - lo) / 5
    edges = [lo + i * step for i in range(6)]
    pd = 0 if step >= 5 else 1 if step >= 0.5 else 2
    fmt = lambda v: _fmt(v, dec) if dec is not None else _fmt(round(v, pd))
    x = 8
    body += _text([d.get('scale_label', 'scale')], T_COL, x, y + 6); x += _tw(d.get('scale_label', 'scale'), 10, 'mono', 0.4) + 12
    for i in range(5):
        role = ('viz-markon',) + T_MARK[1:] if i == 4 else T_MARK
        txt = f'{fmt(edges[i])}–{fmt(edges[i + 1])}{unit}'
        w = _tw(txt, 10.5, 'mono') + 14
        if x + w > Wd - 8:
            x, y = 8, y + 30
        body += _g(f'<rect class="viz-t{tone} viz-h{i + 1}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="24"/>' + _text([txt], role, x + w / 2, y + 5.5, 'middle'))
        x += w + 4
    y += 24
    return _svg(_r(Wd), _r(y + 8), body, 'matrix viz-numeric', d.get('title'), d.get('caption'), wide=wide)


KINDS = {'timeline': timeline, 'compare': compare, 'tree': tree, 'flow': flow,
         'sitemap': sitemap, 'objects': objects, 'decision': decision, 'matrix': matrix,
         'states': states, 'swimlanes': swimlanes, 'wireflow': wireflow,
         'line': line, 'bars': bars, 'scatter': scatter, 'range': range_}


def render(d):
    """One figure object to HTML. A kind not in KINDS, or bad data, is an error: a figure that cannot draw is a bug, not a blank."""
    try:
        return KINDS[d['kind']](d)
    except KeyError as e:
        raise SystemExit(f'viz: unknown kind or missing field {e} in figure {json.dumps(d)[:120]}')
    except (TypeError, ValueError, IndexError, AttributeError, ZeroDivisionError) as e:
        raise SystemExit(f'viz: {d.get("kind")}: the data cannot be drawn ({e}) in figure {json.dumps(d)[:120]}')


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
