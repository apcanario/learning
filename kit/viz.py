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
            optional per event "date" (its date line as the unit writes it, P58) and per figure "era": "BCE"
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
            P90 (4 Nov 2026): optional per node "href" (a panel id: the box is a link to it) and "dashed": true (a
            dashed, untinted box: a planned page); optional "phone": {"stack_from": 1}, a second drawing of the same
            root as wide as a phone frame (PHONE_FRAME), shown below 768 px in place of the wide one (svg.viz-alt).
            P91 (4 Nov 2026): the Academy home no longer draws its map with them (P91's bookshelf, then P92's
            topography, took its place); the three keys stay, documented, for any unit's sitemap that links its boxes,
            marks a planned page or needs a phone drawing.
  objects   {"kind": "objects", "objects": [{"id": "claim", "title": "Claim", "attrs": ["amount", ...],
             "actions": ["-> approve", ...], "tone": 2}, ...], "rows": [["company", "policy", null], ...],
             "links": [{"from": "company", "to": "policy", "label": "sets", "from_card": "1", "to_card": "1..*"}]}
            boxes placed in the grid "rows" gives (null is an empty cell; at most 4 columns); a link is a line with a
            label and a cardinality at each end; a link that would cross a third box raises (move a box); optional
            per link "dir": "to" or "from" (P66), the end its label reads towards, drawn as a small triangle.
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
  range     {"kind": "range", "unit": "%", "unit_one": null, "years": false, "era": "BC", "min": 0, "max": 100, "ticks": [...], "rows": [{"label": "...", "low": 45,
             "high": 70, "point": 58, "low_src": "Pew 2024", "high_src": "Ofcom 2025", "tone": 4}, ...]}
            competing estimates: per row a low-to-high bar, an optional point estimate (a diamond, its value above it)
            and under the bar each end's value with its source tag; one axis for every row.
  matrix    with "numeric": true: cells are numbers (or null), shaded in five steps of the figure's "tone" between
            min and max (default the data's); a legend gives each step's range ("scale_label" names it).

The home kind (P92, 4 Nov 2026; it replaced P91's bookshelf, `shelf`, whose kind, keys and classes are gone): the
Academy home's topography, declared by build.py from the course data and drawn as SVG at build time, not one of the
figure kinds a unit declares (the Figure kinds page shows those):

  contours  {"kind": "contours", "interval": 22000, "patch": false,
             "rises": [{"label": "History", "words": 510493, "tone": 1}, {"label": "IA8", "tone": 4, "planned": true}, ...],
             "layouts": [{"name": "tall", "width": 1000, "height": 1000, "spread": 0.095, "grid": 5, "simplify": 0.6,
                          "at": [[0.5, 0.52], [0.26, 0.22], ...]}, ...]}
            one rise per written entry of "rises", its height its "words": the field is a sum of smooth bumps (a
            Gaussian whose outline two angular harmonics push in and out, the phases from the label, so the drawing is
            the same on every build), each bump's peak exactly its words and its spread "spread" times the layout's
            width times the cube root of its words over the largest's (a bigger rise is also wider); the field is
            sampled every "grid" units, cut at every multiple of "interval" words by marching squares, each line
            simplified to within "simplify" units and written in whole-unit relative steps; each stretch of a line is
            drawn in the tone of the rise that dominates it there (<g class="ct-rise ct-t{tone}"> per rise, with
            data-label, data-words and data-rings, the levels its own words stand above; P93: each peak on a grid node, and a
            written rise under one level marked by a spot ring, <circle class="ct-spot">, so every written part shows). A "planned": true entry needs no
            words: it is flat, a small dashed ring (<g class="ct-plan">), in no line. Each layout is one <svg
            class="topo-l topo-{name}" data-layout="{name}"> (preserveAspectRatio slice: it covers its frame); "at"
            places each rise (fractions of the width and height, one per rise, in order); without it the rises stand in
            order along the width, 6% clear at each side, evenly spaced, alternately above and below the middle. The layer is <div class="topo">
            ("patch": true adds topo-patch), aria-hidden, with no text in it; the theme (4h, 4i) gives every stroke and
            opacity, shows one layout per width and drifts the hero's, never a patch's. The hero declares two layouts
            (tall below 1100 px, wide from it), one rise per area of knowledge (its words written); each course tile one
            layout, "patch", one rise per unit of the course, a planned unit flat. A rise without a label or tone, a
            written rise without words, an "at" that does not give one point per rise, or no written rise raises.

On a phone (below 768 px) every figure draws at its natural size, one SVG unit to one CSS pixel, and scrolls sideways
inside its frame (.viz-scroll), never the page; shell.js fades the edge that has more drawing and shows the line
"scroll sideways for the whole figure" under a figure only when its drawing is wider than its frame.

Every kind takes "caption" (shown under the figure; keep the source in it) and "title" (optional, drawn above), and
"tone" (1 to 6, the house accents) on any node, box, lane, step, screen or cell. A kind that cannot draw its data
raises SystemExit and stops the build: a figure that cannot draw is a bug, not a blank. The IA kinds measure their text
in the theme's fonts and wrap it inside its box, which grows to fit; every box and its text are one <g data-box>, which
verify.py checks on the examples page (text inside its box, no two boxes overlapping, nothing outside the drawing).

Contract changes at P55 (30 Oct 2026), from the faults the Rome retrofit's checkers met (kit/reviews/p43-rome-notes.md).
The rule: a label that cannot fit moves, or the drawing widens and scrolls; it is never clipped, shrunk or cut; a block
the renderer cannot draw honestly stops the build with a message that says what to change.
  every kind  a field that takes a list (events, spans, rows, attrs, actions, lines, cells, children, ...) given a bare
              string stops the build (an object's attrs as a string drew one letter per line). A year prints as
              753 BC, AD 14 or 1453, and a year 0 (a tick, an event, a value) stops the build: there is no year 0, so
              put it at -1 (1 BC) or 1 (AD 1). A unit of three letters or more is a word and prints after a space
              ("1,200 men"); shorter ones (%, k, m, bn) print against the number ("61%", "1.5m").
  timeline    a span's label is drawn inside its bar only when it fits there with 6 units either side; otherwise beside
              the bar, right or left, in the muted mono of a column head. Spans sit in lanes: a span takes the first
              lane where its bar overlaps no other bar (bars may abut) and its outside label keeps 6 units from
              everything there, so spans that overlap in time never share a lane. The drawing widens (and scrolls)
              until every span label fits beside its bar, every event label fits inside it and neighbouring tick
              labels are 8 units apart; past 2,400 units (or twice its starting width) it stops the build instead,
              naming the two ticks too close to label both. Ticks, events and spans outside start..end stop the build. Each span is a
              <g data-box>, with its label when the label is inside it.
  compare     row labels are measured and wrapped in a column as wide as the widest line (up to 240, LABEL_COL); values
              take thousands separators (and "decimals" when given) and the value column is measured; values must be
              0 to max. Each row grows with its label. P97 (12 Nov 2026): it also carries a phone drawing (svg.viz-alt,
              PHONE_NARROW = 258 units, shown below 768 px), its labels pinned at the left (wrapped at 112) when that
              leaves the bars 96 units, else above each bar, so the longest bar is whole in the opening phone frame.
  line        P123 (15 Nov 2026): it also carries a phone drawing (svg.viz-alt, PHONE_NARROW = 258 units, shown below 768 px),
              drawn from the same data, so its y-axis, legend, title and point labels open whole in a 320 px phone's frame
              and it never scrolls; a label with no room at that width falls back to "labels": "ends" in that drawing only.
              verify.py's check_phone_lines checks every line figure at 320 and 390 px.
  scatter     P124 (15 Nov 2026): it also carries a phone drawing (svg.viz-alt, PHONE_NARROW = 258 units, shown below 768 px),
              drawn from the same data, so its y-axis, title and point labels open whole in a 320 px phone's frame and it never
              scrolls; in that drawing x ticks are thinned, labels wrap at half the width and the plot is retried taller (up
              to 3 times its "height", in steps of an eighth) when a label has no room. verify.py's check_phone_scatters checks every scatter at 320 and 390 px.
  bars        the same label column as compare (it wrapped at 160 inside a 172 column). P98 (12 Nov 2026): its phone
              drawing is PHONE_NARROW (258) units wide, as a compare's, so every bar and its value open whole on a
              320 px phone. Bars draw no track, so P98's value rule (below) does not apply to them.
  compare     P98 (12 Nov 2026): a value sits wholly on its track or wholly beyond the track's end (_val_x), in both
              drawings, never across the track's edge.
  tree        boxes keep their size: 112 units, or wider when one word of a label needs it, so no word is broken; every
              label is wrapped in full (it was cut at two lines) and a level's boxes grow to its longest label. A tree
              more than 15 % wider than 700 keeps its size on a desktop and scrolls (viz-wide); one just over 700 (six
              leaves, 738) still scales to the column there. It used to shrink, to 64 units at ten leaves.
              Every node is a <g data-box>.
  range       "years": true prints every value, tick and point as a year; without it, a range whose values are whole
              numbers and include a negative one stops the build (add "years", or "decimals" for real quantities).
              Tick labels at the ends anchor inward so they stay inside the drawing.
Contract changes at P58 (30 Oct 2026), from the faults the Greek retrofit's checkers met (kit/reviews/p43-greece-notes.md),
under the same rule: a label moves or the drawing widens; it is never clipped or cut.
  timeline    an event may carry "date", the date line as the unit writes it ("c. 600 BC", "476/5 BC", "c. 500, or after
              490 BC"), printed in place of the bare year that "at" gives; "at" stays the year it is placed at (the first,
              for a split year) and the text must contain that year, or the build stops. So a label no longer repeats its
              date to keep a "c.": give the event "date" and keep the label to the event. A figure may set "era": "BCE"
              (default "BC") to print 753 BCE, 14 CE in its ticks and date lines, as a unit that writes BCE/CE does; a
              "date" in the other notation stops the build. Wrapping never parts "c.", "ca.", "by", "after", "before",
              "from" or "until" from the number after it ("(c. 185)" stays on one line). No event's stem runs through
              another event's date or label: when the label directions cannot keep every stem clear (events a few years
              apart beside a wide label), every direction of the events caught is tried, then the drawing widens until
              none is crossed (to its widest, 2,400 or twice its start).
  range       a row whose low equals its high is one value: it draws as a point (a diamond, no bar) with its value printed
              once under it, with one source tag (both sources, comma-separated, when they differ); a "point" on such a row
              prints nothing above it. Every end label sits under the value it names: its plate spans its end of the bar
              (inward when both fit under the bar, else centred on each end, else meeting at the bar's middle, else the
              high one a line lower); each label group carries data-end, its end's x, and each row is a <g data-row>.
              A word unit takes the singular for 1: "unit_one" when given (e.g. "man" for "men"), else the unit less a
              final "s" ("1 head"); a word unit not ending in "s" with a value of 1 and no "unit_one" stops the build.
              "era" as for timeline, with "years": true.
  objects     a link label on a level line wraps in the gap between its columns; the gap widens (all gaps alike) until
              the label's longest word fits with 6 units either side, and when the boxes would fall under 110 the
              drawing widens and scrolls; a word is never cut. A diagonal link's label wraps no narrower than its
              longest word. U-9 (9 Nov 2026): a level gap also widens until the two counts at its ends stand apart.
  tree        a tree narrower than the 700-unit drawing (a one-child chain, a short branch) is centred in it; its svg
              carries data-x0, where the drawing starts, and a phone frame (natural size, scrolling) opens there.
Contract change at P63 (1 Nov 2026), under the same rule:
  timeline    an event's "date" may name a century or a span without its year, as the unit gives it ("mid-seventh
              century", "late eighth century BC", "c. 670–640"): it prints as written and is drawn at "at", which must
              lie inside the century or span it names (date_names), or the build stops. The year is never printed
              where the text gives none. verify.py checks every built date line against the year its dot stands at.
Contract change at P79 (1 Nov 2026):
  tree        the svg carries data-xr, the root box's right edge plus 8; a phone frame narrower than the drawing opens at
              the further right of data-x0 (P58) and the point that puts its right edge at data-xr, so the root is in
              view on the first screen. verify.py checks that every tree wider than its phone frame opens with its root whole.
Contract change at P78 (1 Nov 2026):
  objects     the "dir" mark is a narrow isosceles triangle (14 units base to tip, 6 across the base), so it reads towards
              its object on a line at any angle at 390 px. On a level line it sits at the label plate's right end (the plate
              keeps 18 units for it, was 12, and a level gap widens by as much); on a slanted or vertical line it sits on the
              line itself, past the plate on the side of its object with 12 units of line between them (4 where a short line
              has no room), so the line runs on both sides of it and it never reads as the arrowhead of a line cut by the
              plate; plate and mark are each kept clear. The P66 mark was 8 by 8 and on a slanted line read as pointing either way (IA2's cross-surface map).
Contract change at P66 (1 Nov 2026):
  objects     a link may carry "dir": "to" or "from": a small solid triangle at the end of its label, pointing at the
              object the label reads towards (UML's reading-direction mark), for a label that cannot read left to right
              on a level line or top to bottom otherwise. Every line is drawn before any label, and each label sits on its
              own line at the point nearest the middle whose plate is at least 14 units clear of every crossing, every
              other line and every label placed before it (else the clearest), and covers no box, count or other label; when every point covers a
              crossing, a box or a label, the build stops (move a box). A level gap widens for a mark as for a long word.
Contract change at P53 (1 Nov 2026):
  matrix      each column is as wide as its widest cell (a mark on one line) or its header (its longest
              word, or the whole header up to 140), at least 56, not an equal share of the 700-unit width; columns that
              need more than the width share it, the narrower keeping their size and the wider wrapping, and under 70 each the drawing widens
              and scrolls as before. A matrix narrower than the width draws at its own width (class viz-fit: natural size
              at every width, never stretched to the column), at least 320 units and wide enough for its widest legend item.
              U-9 (9 Nov 2026): no shared column is narrower than its longest word or hyphen-split piece, in its header
              or its cells; a column below it takes the width from the columns above theirs, in proportion.
Contract change at P84 (16 Nov 2026), from Rome 11.4 and 11.5 (spans read as a legend key, not as periods):
  timeline    a span is a period on the axis. Lane 0 sits just above the axis and the other lanes stack upwards; each
              bar's two ends drop to the axis by a dashed guide (.viz-spanend), and with spans the tick labels stand above
              the top lane, a gridline (.viz-grid) running from each to the axis. Every span label carries its years: a
              label that names both ends (the years as numbers, an abbreviated run such as 1914–18, or a century, as
              date_names reads them) is drawn as written; otherwise the span's optional "date" (its dates as the unit writes
              them, "c. 670–640 BC", which must name both ends in the figure's era) or its years as yr prints them (58–57 BC,
              27 BC–AD 14, AD 14–37, 2018–2020) follow it after a comma; a span with no label draws its years alone. A label
              beside its bar sits on a plate of the card colour (.viz-lblbg). A lane is taken only where the span's guides
              cross no outside label below it and no guide from above crosses its own (_guides_clear), unless no lane allows
              that. The timeline has one drawing at every width (it scrolls in its phone frame), so the rule holds on the
              phone and the desktop alike. Each span is <g data-span="from to" data-text="label as drawn">; verify.py checks
              every span label names its years (span_names) and every bar end has its guide to the axis. A timeline
              without spans is drawn as before.
              Round 2 (17 Nov 2026), from the 141 figures' re-checks (kit/reviews/p84/): a label also names its years by a
              decade ("1360s", "480s or 470s"), an ordinal century written "c." ("8th c. BC") or a split year ("367/6"), and
              a century drawn to its round end year (the ninth century BC drawn 900 to 800) names it; a label that names a
              date but not both ends stops the build, so a year is never printed twice. A side label wider than SPAN_WRAP
              (220 units) breaks onto lines, its years on the last, and its lane grows to fit; two spans abutting in one lane
              are drawn 1.5 units short of the year they share; guides and gridlines break where they would cross a bar or a
              plate; an edge-pinned tick label keeps 8 units from its neighbour (the drawing widens); span labels keep their
              case (.viz-spanlabel, and .viz-spanside beside the bar), since capitals turned "VIi" into "VII".
Contract change at P109 (16 Nov 2026):
  matrix      a matrix is drawn wide (keeps its size and scrolls on a desktop) only when its drawing is wider than 700; one
              whose columns had to share the width but whose drawing is 700 or less scales to the column (PB8 figure 4
              overflowed its 698 px frame by 2 px, and the second frame's fade lay over its keys). A legend key's tone is
              the tone of the cells it explains: a cell takes its row's tone unless it gives its own, so a mark whose key
              has another tone is given that tone in its cell.
              Round 2 (17 Nov 2026), from the P109 re-check (kit/reviews/p109/): the keys are drawn in their own svg under
              the frame, svg.viz-key (and svg.viz-keyn, the narrow-label drawing's keys, shown with it below 768 px), so they
              never scroll with the grid, clip at its left edge or sit under a fade; the grid's svg ends under its last row. A
              matrix up to 15 % wider than 700 scales to the column on a desktop, as a tree does (Rome 3.1 figure 3, 765
              units, lost its row labels when it scrolled there).
Contract change at P50 (1 Nov 2026): sitemap, objects, decision, states and wireflow centre their drawing in the
  700-unit width; their svg carries data-x0 (where the drawing starts, less 8) as a narrow tree's does since P58, so a
  phone frame opens on the drawing. Desktop scaling is unchanged. verify.py checks that every figure of these kinds
  whose drawing starts more than 12 units in carries data-x0 within 2 units of it.
verify.py (P58) also reads every built figure for these: no event label line ending in "c.", "by", "after" (and the
like) with its number on the next line; no date line that drops a "c." or a split year the label carries; no BC/AD
in a figure on a page whose prose writes BCE/CE; no value printed twice in one range row, and every range end label
spanning its end; no "1 <word>s"; every objects link label's lines joining back to whole words; a narrow tree centred;
no timeline stem through another event's text.
Contract change at P52 (1 Nov 2026): render draws a deep copy of the block it is given, so the renderer's working keys
(_t, _h, ...) never reach a unit; VIZ_KEYS lists every kind's documented keys at every level, and verify.py reads every
```viz block in the vault, every history figure declaration, every course home figure and every examples block against it.
verify.py (P55) runs its figure checks on every figure of every page, every kind: nothing outside the drawing, every
text inside its box (a node, a plate, a bar or span carrying its label), no two boxes overlapping, no two texts
overlapping and no free text over a box; the examples page carries one hard case per fault above.
"""
import copy
import html as H
import itertools
import json
import math
import pathlib
import re
import textwrap
import zlib

W = 700            # drawing width in user units; the SVG scales to the column
PHONE_NARROW = 258  # P97 (12 Nov 2026): the scroll frame of a figure on a 320 px phone (the same gutters, padding and border); a compare's phone drawing is this wide, so it never scrolls on any phone
NARROW_FRAME = 258  # C1 (15 Nov 2026): the scroll frame of a figure on a 320 px phone
NARROW_LW = 100     # C1: a matrix's label column in the drawing shown at 360 px and below (its sticky copy 108 px of that frame)
PHONE_FRAME = 328  # P83 (3 Nov 2026): the scroll frame of a figure on a 390 px phone (16 px gutters, the figure's 14 px padding and 1 px border); a drawing this wide or narrower never scrolls there
TONES = 6          # --viz-1 … --viz-6 map to the house accents in theme.css


def esc(s):
    return H.escape(str(s), quote=True)


ERAS = ('BC', 'BCE')


def yr(y, kind='timeline', era='BC'):
    """A year as a figure prints it: 753 BC, AD 14, 1453; with era "BCE" (P58), 753 BCE, 14 CE, 1453. There is no
    year 0 (1 BC is followed by AD 1), so a label at 0 cannot be printed honestly and stops the build (P55)."""
    y = int(y)
    if y == 0:
        _fail(kind, 'a year 0 would be printed, and there is no year 0 (1 BC is followed by AD 1): '
                    'put the tick, event or value at -1 (1 BC) or 1 (AD 1)')
    if era == 'BCE':
        return f'{-y} BCE' if y < 0 else f'{y} CE' if y < 1000 else str(y)
    return f'{-y} BC' if y < 0 else f'AD {y}' if y < 1000 else str(y)


def _era(d, kind):
    """A figure's era notation (P58): "BC" (BC/AD, the default) or "BCE" (BCE/CE), as the unit's prose writes it."""
    e = d.get('era', 'BC')
    if e not in ERAS:
        _fail(kind, f'"era" is "BC" (BC/AD) or "BCE" (BCE/CE), got {e!r}')
    return e


# P58: a qualifier that belongs to the number after it ("c. 670", "by 500", "after 490") is never left at the end of a
# line with the number on the next: the space between them is made unbreakable while the line is wrapped.
_GLUE = re.compile(r'(?<![^\s(\[])(c\.|ca\.|by|after|before|from|until)\s+(?=[(\[]?\d)', re.I)


def _glue(s):
    return _GLUE.sub(lambda m: m.group(1) + '\u00a0', str(s))


def _unglue(lines):
    return [ln.replace('\u00a0', ' ') for ln in lines]


# P63 (1 Nov 2026): a date the unit gives only by century or span ("mid-seventh century", "late eighth century BC",
# "c. 670–640") is printed as the unit writes it, drawn at "at", which must lie inside what it names.
_ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth',
        'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth']
_ORDS = {w: i + 1 for i, w in enumerate(_ORD)} | {'twenty-first': 21}
_CENT = re.compile(r'\b(twenty-first|' + '|'.join(_ORD) + r'|\d{1,2}(?:st|nd|rd|th))\b(?!\s+(?:half|quarter|third)\b)(?=[^.;,]*?\bcentur(?:y|ies)\b)', re.I)
_SPAN = re.compile(r'(\d{2,4})\s*(?:–|-|to)\s*(\d{1,4})')


def date_names(t, at):
    """P63: whether a date line names the year "at": it contains the year as a number, or names a century (or a run of
    centuries: "seventh to sixth century") or a span of years ("c. 670–640", "670 to 640") that contains it. The
    centuries count backwards before AD 1: the seventh century BC is 700 to 601 BC."""
    at = int(at)
    if str(abs(at)) in t:
        return True
    cs = [_ORDS.get(m.lower(), None) or int(re.match(r'\d+', m).group()) for m in _CENT.findall(t)]
    if cs:
        lo, hi = min(cs), max(cs)
        if at < 0:
            return -100 * hi <= at <= -100 * (lo - 1) - 1
        return 100 * (lo - 1) + 1 <= at <= 100 * hi
    for a, b in _SPAN.findall(t):
        a, b = int(a), int(b)
        if b < 100 <= a:                                    # an abbreviated end: 670–40 is 670 to 640
            b = int(str(a)[:len(str(a)) - len(str(b))] + str(b))
        if min(a, b) <= abs(at) <= max(a, b):
            return True
    return False


def _date_text(e, era, kind='timeline'):
    """An event's date line (P58): its own "date" text when it has one, else its year as yr prints it. The text keeps
    what the unit says (c. 600 BC, 476/5 BC, c. 500, or after 490): it must contain the event's year as a number and
    use the figure's era notation."""
    if 'date' not in e:
        return yr(e['at'], kind, era)
    t = e['date']
    if not isinstance(t, str) or not t.strip():
        _fail(kind, f'the event {e.get("label")!r}: "date" must be the date as the unit writes it, e.g. "c. 600 BC"')
    if not date_names(t, e['at']):
        _fail(kind, f'the event {e.get("label")!r} at {e["at"]}: its date {t!r} does not contain the year {abs(int(e["at"]))}, '
                    'nor name a century or a span of years that contains it; set "at" to the year the date names (its first, '
                    'for a split year), or inside the century or span it names')
    wrong = r'\b(BC|AD)\b' if era == 'BCE' else r'\b(BCE|CE)\b'
    if re.search(wrong, t):
        _fail(kind, f'the event {e.get("label")!r}: its date {t!r} mixes notations; the figure\'s era is {era} '
                    '(set "era" to "BCE" for BCE/CE)')
    return t


def _unit(u):
    """A unit as printed after a number (P55): a word (three letters or more: men, words, days, ships) takes a space,
    "1,200 men"; a symbol or an abbreviation (%, k, m, bn, ×) is printed against the number, "61%", "1.5m"."""
    u = str(u or '')
    return ' ' + u if len(u) >= 3 and u[0].isalpha() else u


# P50 (1 Nov 2026): the kinds that centre a narrower drawing in the 700-unit width (as a narrow tree does since P58)
# name where the drawing starts, data-x0, so a phone frame (natural size, scrolling) opens on it, not on the margin.
X0_KINDS = ('sitemap', 'objects', 'decision', 'states', 'wireflow')
_TXT_RE = re.compile(r'<text class="([\w-]+)" x="([-\d.]+)"[^>]*?(?:text-anchor="(\w+)")?[^>]*>(.*?)</text>', re.S)


def _left(body):
    """The leftmost x anything in a drawing reaches: a rect's x, a line's or path's points, a circle's edge, a text's
    left end (its anchor and measured width, at the widest of the theme's text roles). None for an empty body."""
    xs = [float(v) for v in re.findall(r'<rect[^>]*? x="([-\d.]+)"', body)]
    xs += [float(v) for v in re.findall(r' x[12]="([-\d.]+)"', body)]
    xs += [float(c) - float(r) for c, r in re.findall(r'<circle[^>]*? cx="([-\d.]+)"[^>]*? r="([\d.]+)"', body)]
    for dd in re.findall(r' (?:d|points)="([^"]*)"', body):
        xs += [float(a) for a in re.findall(r'(-?[\d.]+),-?[\d.]+', dd)]
    for m in _TXT_RE.finditer(body):
        t = H.unescape(re.sub(r'<[^>]+>', '', m.group(4)))
        w = _tw(t, 12, 'sansb') if 'mono' not in m.group(1) else _tw(t, 10.5, 'mono')
        xs.append(float(m.group(2)) - {'middle': w / 2, 'end': w}.get(m.group(3) or 'start', 0))
    return min(xs) if xs else None


def _svg(w, h, body, cls, title, caption, wide=False, x0=None, xr=None, stick=None, alt=None, narrow=None, keys=None):
    """stick (P83, 3 Nov 2026): (width, svg body) of the label column a matrix, a numeric matrix or a compare keeps in
    view while a phone frame scrolls: a copy of the labels on a card-coloured plate, drawn after the main svg in a
    .viz-stick holder that the theme shows only below 768 px, sticky at the frame's left edge (aria-hidden: the
    main svg carries the same labels). The frame carries --stick so the left fade starts past the column.
    alt (P83): (width, height, body) of a second drawing of the same data for a phone, emitted after the main svg as
    svg.viz-alt; the theme shows it below 768 px and the main svg above (the frame carries data-alt).
    narrow (C1, 15 Nov 2026): (width, height, body, stick or None) of a matrix drawn with a narrow label column, emitted as
    svg.viz-altn with its own sticky copy in .viz-stickn; the theme shows it at 360 px and below in place of the main svg
    and its column (the frame carries data-altn and --stickn)."""
    if x0 is None and cls in X0_KINDS:
        lft = _left(body)
        x0 = max(0, lft - 8) if lft is not None and lft - 8 > 4 else None
    t = f'<p class="viz-title">{esc(title)}</p>' if title else ''
    if caption:                                              # H-2: a number range never breaks at its dash (141–150)
        caption = re.sub(r'>([^<]*)<', lambda m: '>' + re.sub(r'(\d)([–-])(?=\d)', '\\1\u2060\\2\u2060', m.group(1)) + '<', f'>{caption}<')[1:-1]
    c = f'<figcaption>{caption}</figcaption>' if caption else ''
    st, sv = '', ''
    if stick and stick[0] > 0:
        sw, sh = _r(stick[0]), _r(stick[2]) if len(stick) > 2 and stick[2] else h   # the plate covers the rows only, never a legend under them
        st = f' style="--stick:{sw}px"'
        sv = (f'<div class="viz-stick" aria-hidden="true"><svg viewBox="0 0 {sw} {h}" width="{sw}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
              f'<rect class="viz-lblbg" x="0" y="0" width="{sw}" height="{sh}"/>{stick[1]}</svg></div>')
    av = ''
    if alt:
        aw, ah, ab = alt
        st += ' data-alt=""'
        av = f'<svg class="viz-alt" viewBox="0 0 {aw} {ah}" width="{aw}" height="{ah}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title or cls)}">{ab}</svg>'
    nv = ''
    if narrow:
        nw, nh, nb, nst = narrow
        st += ' data-altn=""'
        nv = f'<svg class="viz-altn" viewBox="0 0 {nw} {nh}" width="{nw}" height="{nh}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title or cls)}">{nb}</svg>'
        if nst and nst[0] > 0:
            ns, nsh = _r(nst[0]), _r(nst[2]) if len(nst) > 2 and nst[2] else nh
            st = st.replace(' style="', f' style="--stickn:{ns}px;') if ' style="' in st else st + f' style="--stickn:{ns}px"'
            nv += (f'<div class="viz-stickn" aria-hidden="true"><svg viewBox="0 0 {ns} {nh}" width="{ns}" height="{nh}" xmlns="http://www.w3.org/2000/svg">'
                   f'<rect class="viz-lblbg" x="0" y="0" width="{ns}" height="{nsh}"/>{nst[1]}</svg></div>')
    sv = nv + sv
    kv = ''                                                  # P109 round 2: a matrix's keys, under the frame, never scrolled or faded
    for kk, kc in zip(keys or (), ('viz-key', 'viz-keyn')):
        if kk:
            kv += f'<svg class="{kc}" viewBox="0 0 {kk[0]} {kk[1]}" width="{kk[0]}" height="{kk[1]}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="key">{kk[2]}</svg>'
    if kv and keys[1] is None and keys[0]:
        kv = kv.replace('class="viz-key"', 'class="viz-key viz-key1"', 1)
    return (f'<figure class="viz viz-{cls}{" viz-wide" if wide else ""}">{t}<div class="viz-scroll"{st}><svg viewBox="0 0 {w} {h}" width="{w}" height="{h}"{f' data-x0="{x0:.0f}"' if x0 else ''}{f' data-xr="{xr:.0f}"' if xr else ''} '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title or cls)}">{body}</svg>{av}{sv}</div>{kv}{c}</figure>')


def _wrap(s, n, px=None, size=12, font='sans', ls=0.0):
    """Wrap at n characters (the four A8 kinds), or, given px, at that measured width in the theme's own fonts (the IA
    kinds): a word wider than px is broken inside, so a line never exceeds px and text never overflows its box."""
    if px is None:
        return textwrap.wrap(str(s), n) or ['']
    lines, cur = [], ''
    for word in str(s).split():
        while _tw(word, size, font, ls) > px:                      # a word too long for the line: break it, after a
            hy = [i + 1 for i, ch in enumerate(word[:-1]) if ch == '-' and _tw(word[:i + 1], size, font, ls) <= px]
            k = hy[-1] if hy else max(1, max(i for i in range(1, len(word) + 1) if _tw(word[:i], size, font, ls) <= px or i == 1))   # hyphen first
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


def _lane_free(o, placed):
    """A span option clears a lane when its bar overlaps no bar there (bars may abut: one reign ends as the next begins)
    and its outside label, if any, keeps 6 units from every bar and outside label there."""
    def apart(p, q, gap):
        return p[1] <= q[0] + gap or q[1] <= p[0] + gap
    for q in placed:
        if not apart(o[1], q[1], 0.5):
            return False
        for lab, other in ((o[2], q[1]), (o[2], q[2]), (q[2], o[1])):
            if lab and other and not (lab[1] + 6 <= other[0] or other[1] + 6 <= lab[0]):
                return False
    return True


def _guides_clear(o, lane, placed_all):
    """P84: a span's end guides drop from its bar to the axis through every lane below it. A lane is clear of guides when
    no guide below crosses an outside label placed lower, and no guide from a span placed higher crosses this one's."""
    def hit(lab, xs):
        return lab and any(lab[0] - 3 <= gx <= lab[1] + 3 for gx in xs)
    for ql, q in placed_all:
        if ql < lane and hit(q[2], o[1]):
            return False
        if ql > lane and hit(o[2], q[1]):
            return False
    return True


_DEC = re.compile(r'\b(\d{2,3})0s\b')
_CENTC = re.compile(r'\b(\d{1,2})(?:st|nd|rd|th)(?:\s*(?:–|-|to|or)\s*(\d{1,2})(?:st|nd|rd|th))?\s+c\.')
_SPLIT = re.compile(r'\b(\d{2,4})/(\d{1,2})\b')
_DATED = re.compile(r'\b\d{3,4}(?:s\b|/\d{1,2}\b|\b)|\b\d{2}0s\b|\(\d{2}\)|\b\d{1,2}(?:st|nd|rd|th)\s+c(?:\.|entur)|\b(?:' + '|'.join(_ORD) + r')\s+centur', re.I)


def _names_year(t, y):
    """P84 round 2: whether a span label names the year y: date_names (the year, a run such as 1914–18, a century in words
    or "7th century"), or a decade ("1360s", "480s or 470s": 1360s is 1360 to 1369, the 440s BC 449 to 440 BC), an
    ordinal century abbreviated "c." ("8th c. BC", "1st–2nd c."), or a split year ("367/6" names 367 and 366)."""
    y = int(y)
    if date_names(t, y):
        return True
    for m in _DEC.finditer(t):
        d = int(m.group(1)) * 10
        if (y < 0 and -(d + 9) <= y <= -d) or (y > 0 and d <= y <= d + 9):
            return True
    cs = [(int(m.group(1)), int(m.group(2) or m.group(1))) for m in _CENTC.finditer(t)]
    ws = [_ORDS.get(w.lower()) or int(re.match(r'\d+', w).group()) for w in _CENT.findall(t)]
    if ws:
        cs.append((min(ws), max(ws)))
    for lo, hi in cs:                                        # a span drawn to a round year ends a century inclusively: the
        lo, hi = min(lo, hi), max(lo, hi)                    # ninth century BC drawn 900 to 800 BC names both its ends
        if (y < 0 and -100 * hi <= y <= -100 * (lo - 1)) or (y > 0 and 100 * (lo - 1) <= y <= 100 * hi):
            return True
    for m in _SPLIT.finditer(t):
        a_, b_ = m.group(1), m.group(2)
        if abs(y) in (int(a_), int(a_[:len(a_) - len(b_)] + b_)):
            return True
    return False


def span_names(t, a, b):
    """P84: whether a drawn span label names both its years (verify.py reads it back from the built figure)."""
    return _names_year(t, a) and _names_year(t, b)


def span_text(s, era='BC', kind='timeline'):
    """P84 (16 Nov 2026): a span's label as drawn, carrying its years. A label that already names both its ends (span_names:
    the years as numbers, an abbreviated run such as 1914–18, a decade, a century, a split year) is drawn as written; a label
    that names a date but not both ends stops the build (give the span its "date", or take the date out of the label, so a
    year is never printed twice). Otherwise its "date" (the span's dates as the unit writes them, which must name both ends)
    or its years as yr prints them (58–57 BC, 27 BC–AD 14, AD 14–37, 2018–2020) follow it after a comma. A span with no label
    is drawn with its years alone."""
    a, b = int(s['from']), int(s['to'])
    lab = str(s.get('label') or '').strip()
    if lab and span_names(lab, a, b):
        return lab
    if lab and _DATED.search(lab):
        _fail(kind, f'the span {lab!r} ({a} to {b}) names a date but not both its years: drop the date from the label and '
                    'give the span "date", or make the label name both ends')
    if 'date' in s:
        t = s['date']
        if not isinstance(t, str) or not t.strip() or not span_names(t, a, b):
            _fail(kind, f'the span {lab!r} ({a} to {b}): its "date" {t!r} must name both its years, e.g. "c. 670–640 BC"')
        wrong = r'\b(BC|AD)\b' if era == 'BCE' else r'\b(BCE|CE)\b'
        if re.search(wrong, t):
            _fail(kind, f'the span {lab!r}: its date {t!r} mixes notations; the figure\'s era is {era}')
        yrs = t.strip()
    else:
        ya, yb = yr(a, kind, era), yr(b, kind, era)
        suf = ' BCE' if era == 'BCE' else ' BC'
        if ya.endswith(suf) and yb.endswith(suf):
            yrs = f'{ya[:-len(suf)]}–{yb}'
        elif ya.startswith('AD ') and yb.startswith('AD '):
            yrs = f'{ya}–{yb[3:]}'
        elif ya.endswith(' CE') and yb.endswith(' CE'):
            yrs = f'{ya[:-3]}–{yb}'
        else:
            yrs = f'{ya}–{yb}'
    return f'{lab}, {yrs}' if lab else yrs


SPAN_WRAP = 220   # P84 round 2: a label beside its bar wider than this breaks onto lines, so a 320 px phone frame shows it whole


def span_lines(t):
    """P84 round 2: a span label beside its bar, as lines: one line when it is SPAN_WRAP units or less; else its text and
    its years on two lines, the text wrapped further if needed. Round 3 (17 Nov 2026): the trailing date is kept whole on the
    last line: a final parenthesis that names a year, decade or century ("(c. 1950–1450)", "(146 or 27 BC–AD 330)"), else what
    follows the last comma when it holds a number; a date wider than SPAN_WRAP itself breaks only after a dash or "or"."""
    w = lambda u: _tw(u, 10, 'mono', 0.4)
    if w(t) <= SPAN_WRAP:
        return [t]
    wrap = lambda u: _wrap(u, 0, SPAN_WRAP, 10, 'mono', 0.4)
    head, unit = t, None
    m = re.search(r'\s(\([^()]*\d[^()]*\))$', t)
    if m:
        head, unit = t[:m.start()], m.group(1)
    elif ', ' in t and re.search(r'\d', t.rpartition(', ')[2]):
        h_, _, unit = t.rpartition(', ')
        head = h_ + ','
    if not unit or w(unit) > SPAN_WRAP:                   # no date at the end, or one too long to keep whole: wrap by width
        return wrap(t)
    if w(unit) <= SPAN_WRAP:
        tail = [unit]
    else:
        parts = re.split(r'(?<=–)|(?<= or )', unit)
        tail, cur = [], ''
        for p_ in parts:
            if cur and w(cur + p_) > SPAN_WRAP:
                tail.append(cur.rstrip()); cur = p_
            else:
                cur += p_
        tail.append(cur.rstrip())
    hl = wrap(head) if head.strip() else []
    if hl and w(hl[-1] + ' ' + tail[0]) <= SPAN_WRAP:       # round 4: the date joins the last line when both fit on it
        hl[-1] = hl[-1] + ' ' + tail[0]; tail = tail[1:]
    return hl + tail


def _span_lanes(spans, x, Wd, texts=None):
    """P55: timeline spans in lanes. A span's label is drawn inside its bar when it fits there with 6 units either side,
    else beside the bar (right or left, the side that sits over fewer other bars) on a plate of the card colour; each span
    takes the first lane _lane_free allows, so spans that overlap in time never share a lane. P84: lane 0 sits on the
    axis and lanes stack upwards; a lane is taken only when the span's end guides cross no outside label below it and
    no guide from above crosses its own label (_guides_clear), unless no lane up to one per span allows that.
    Returns [(span index, lane, side, label x0, label x1)], or None when a label fits on neither side (the caller widens)."""
    texts = texts or [str(s.get('label') or '') for s in spans]
    out, lanes, placed_all = [], [], []
    order = sorted(range(len(spans)), key=lambda k: (spans[k]['from'], spans[k]['to'], k))
    for k in order:
        s = spans[k]
        x1, x2 = x(s['from']), x(s['to'])
        tin = _tw(texts[k], 10, 'mono', 0.4)                 # mono: the width does not depend on case
        tw = max(_tw(ln, 10, 'mono', 0.4) for ln in span_lines(texts[k])) if texts[k] else 0
        opts = []                                            # (side, bar, outside label or None, label x0, x1)
        win = tin if tin <= SPAN_WRAP else max(_tw(ln, 10, 'mono', 0.4) for ln in span_lines(texts[k]))   # round 3: an in-bar label
        if not texts[k] or win + 12 <= x2 - x1:              # wider than a 320 px frame breaks onto lines inside a taller bar
            opts.append(('in', (x1, x2), None, (x1 + x2 - win) / 2, (x1 + x2 + win) / 2))
        if x2 + 6 + tw <= Wd - 4:
            opts.append(('right', (x1, x2), (x2 + 2, x2 + 10 + tw), x2 + 6, x2 + 6 + tw))
        if x1 - 6 - tw >= 4:
            opts.append(('left', (x1, x2), (x1 - 10 - tw, x1 - 2), x1 - 6 - tw, x1 - 6))
        if not opts:
            return None
        bars_ = [(x(t['from']), x(t['to'])) for j, t in enumerate(spans) if j != k]
        blocks = lambda o: sum(1 for a, b in bars_ if a < o[4] + 6 and o[3] - 6 < b)   # bars an outside label would sit over
        pick = None
        for strict_ in (True, False):
            lane = 0
            while lane <= len(spans):
                while lane >= len(lanes):
                    lanes.append([])
                free = [o for o in opts if _lane_free(o, lanes[lane]) and (not strict_ or _guides_clear(o, lane, placed_all))]
                if free:
                    pick = (lane, min(free, key=lambda o: (o[0] != 'in', blocks(o) if o[0] != 'in' else 0, opts.index(o))))
                    break
                lane += 1
            if pick:
                break
        lane, o = pick
        lanes[lane].append(o); placed_all.append((lane, o)); out.append((k, lane, o[0], o[3], o[4]))
    while lanes and not lanes[-1]:
        lanes.pop()
    return sorted(out)


def timeline(d):
    K = 'timeline'
    start, end = d['start'], d['end']
    spans, events, ticks = d.get('spans', []), d.get('events', []), d.get('ticks', [])
    if not end > start:
        _fail(K, f'end ({end}) must be later than start ({start})')
    for t in ticks:
        if not start <= t <= end:
            _fail(K, f'the tick {t} lies outside start..end ({start}..{end}); drop it or widen the range')
        yr(t)
    for e in events:
        if not start <= e['at'] <= end:
            _fail(K, f'the event {e.get("label")!r} at {e["at"]} lies outside start..end ({start}..{end}); widen the range')
        yr(e['at'])
    for s in spans:
        if not start <= s['from'] < s['to'] <= end:
            _fail(K, f'the span {s.get("label")!r} ({s["from"]} to {s["to"]}) must run forwards inside start..end ({start}..{end})')
    era = _era(d, K)
    dates = [_date_text(e, era) for e in events]
    stext = [span_text(s, era, K) for s in spans]                # P84: every span label carries its years
    wrap = lambda s: _unglue(_wrap(_glue(s), 22))
    tlab = [yr(t, K, era) for t in ticks]
    tw_max = max((_tw(t, 10.5, 'mono') for t in tlab), default=0)
    # P55: the drawing widens (and scrolls) until every label fits: a span label beside its bar, every event label inside
    # the drawing, and neighbouring tick labels 8 units apart. It starts at 700, or 64 per event for a dense timeline.
    # P58 (by eye): when no choice of directions keeps every stem clear of the labels above it (events a few years
    # apart, near an edge), the drawing widens, as P55 widens it for its labels, until none is crossed or it reaches
    # its widest; past that it keeps the layout with the fewest crossings.
    Wmin, tried, final = 0, None, False
    W0 = max(700, 64 * len(events))
    while True:
        W = max(W0, Wmin)
        for _ in range(40):
            L, R = 40, W - 40
            ast = lambda y: y + 1 if y < 0 else y            # P84 round 3: astronomical years, so no year 0 lies between 1 BC and AD 1
            x = lambda y: L + (R - L) * (ast(y) - ast(start)) / (ast(end) - ast(start))
            txs = sorted(x(t) for t in ticks)
            need = max([(tw_max + 8) / (b - a) for a, b in zip(txs, txs[1:]) if b > a] + [1])
            # P84 round 2: a tick label pinned to an edge (anchored start or end) must also keep 8 units from its neighbour
            ext = []
            for t_, tl_ in sorted(zip(ticks, tlab)):
                tx_, w_ = x(t_), _tw(tl_, 10.5, 'mono')
                a0 = tx_ if tx_ < L + 20 else (tx_ - w_ if tx_ > R - 20 else tx_ - w_ / 2)
                ext.append((a0, a0 + w_))
            if any(q[0] - p_[1] < 8 for p_, q in zip(ext, ext[1:])):
                need = max(need, 1.15)
            lanes = _span_lanes(spans, x, W, stext) if spans else []
            ev_w = max((max([_tw(dt, 10.5, 'mono')] + [_tw(ln, 12) for ln in wrap(e['label'])]) for e, dt in zip(events, dates)), default=0)
            if lanes is not None and need <= 1 and ev_w <= W - 8:
                break
            W = math.ceil(W * max(need, 1.15) / 10) * 10
            if W > max(2400, 2 * W0):                            # past this a reader cannot follow it on a phone
                if need > 1:
                    a_, b_ = min(((p, q) for p, q in zip(sorted(ticks), sorted(ticks)[1:])), key=lambda pq: pq[1] - pq[0])
                    _fail(K, f'the ticks {a_} and {b_} are too close to label both ({yr(a_)}, {yr(b_)}); drop one or space the ticks out')
                _fail(K, 'a span or event label does not fit even with the drawing at its widest; shorten it')
        body = ''
        # P84 (16 Nov 2026): spans sit in lanes tied to the axis: lane 0 just above it, the others stacked upwards, each
        # bar's ends dropped to the axis by a dashed guide; with spans, the tick labels stand above the top lane and a
        # gridline runs from each down to the axis. A timeline without spans is drawn as before.
        nl = (max(lane for _, lane, *_ in lanes) + 1) if spans else 0
        if spans:
            # P84 round 2 (17 Nov 2026): a lane is as tall as its tallest label (a side label of more than SPAN_WRAP units
            # breaks onto lines); two spans that abut in one lane are drawn 1.5 units short of the year they share, so they
            # never read as one bar; guides and gridlines break where they would cross a bar or a label's plate.
            sl = {k: span_lines(stext[k]) for k, lane, side, l0, l1 in lanes}
            bh = {k: (18 if side != 'in' or len(sl[k]) == 1 else 13 * len(sl[k]) + 6) for k, lane, side, l0, l1 in lanes}
            lh = [24] * nl
            for k, lane, side, l0, l1 in lanes:
                lh[lane] = max(lh[lane], 13 * len(sl[k]) + 11, bh[k] + 6)
            top = 22 if ticks else 6
            ly = {}
            yy_ = top
            for ln in range(nl - 1, -1, -1):
                ly[ln] = yy_; yy_ += lh[ln]
            axis = yy_ + 4
            lane_of_k = {k: lane for k, lane, *_ in lanes}
            geo, obst = {}, []
            for k, lane, side, l0, l1 in lanes:
                s_ = spans[k]
                x1, x2 = x(s_['from']), x(s_['to'])
                b1 = x1 + (1.5 if any(lane_of_k[j] == lane and j != k and spans[j]['to'] == s_['from'] for j in lane_of_k) else 0)
                b2 = x2 - (1.5 if any(lane_of_k[j] == lane and j != k and spans[j]['from'] == s_['to'] for j in lane_of_k) else 0)
                yy = ly[lane]
                ph = 13 * len(sl[k]) + 3
                geo[k] = (x1, x2, b1, b2, yy, ph)
                obst.append((b1, b2, yy, yy + bh[k]))
                if side != 'in':
                    obst.append((l0 - 4, l1 + 4, yy + 1, yy + 1 + ph))
            def vline(cls, gx, y1, y2):
                cuts = sorted((max(o[2] - 1, y1), min(o[3] + 1, y2)) for o in obst if o[0] - 0.5 <= gx <= o[1] + 0.5 and o[3] > y1 and o[2] < y2)
                out, cur = '', y1
                for c1, c2 in cuts:
                    if c1 > cur + 1:
                        out += f'<line class="{cls}" x1="{gx:.1f}" y1="{cur:.1f}" x2="{gx:.1f}" y2="{c1:.1f}"/>'
                    cur = max(cur, c2)
                if y2 > cur + 1:
                    out += f'<line class="{cls}" x1="{gx:.1f}" y1="{cur:.1f}" x2="{gx:.1f}" y2="{y2:.1f}"/>'
                return out
            for t in ticks:
                body += vline('viz-grid', x(t), top - 4, axis)
            for k, lane, side, l0, l1 in lanes:
                x1, x2, b1, b2, yy, ph = geo[k]
                for gx in (x1, x2):
                    body += vline('viz-spanend', gx, yy + bh[k], axis)
            for k, lane, side, l0, l1 in lanes:
                s_ = spans[k]
                tone = _tone(s_, k % TONES + 1, K)
                x1, x2, b1, b2, yy, ph = geo[k]
                rect = f'<rect class="viz-span viz-t{tone}" x="{b1:.1f}" y="{yy}" width="{max(b2 - b1, 0.5):.1f}" height="{bh[k]}"/>'
                g = f'<g data-span="{int(s_["from"])} {int(s_["to"])}" data-text="{esc(stext[k])}">'
                if side == 'in':
                    body += g + _g(rect + ''.join(f'<text class="viz-spanlabel" x="{(x1 + x2) / 2:.1f}" y="{yy + 13 + 13 * i}" text-anchor="middle">{esc(ln)}</text>' for i, ln in enumerate(sl[k] if bh[k] > 18 else [stext[k]]))) + '</g>'
                else:
                    tw = l1 - l0
                    plate = f'<rect class="viz-lblbg" x="{l0 - 4:.1f}" y="{yy + 1}" width="{tw + 8:.1f}" height="{ph}"/>'
                    txt = ''.join(f'<text class="viz-spanside" x="{l0:.1f}" y="{yy + 13 + 13 * i}">{esc(ln)}</text>' for i, ln in enumerate(sl[k]))
                    body += g + _g(rect) + _g(plate + txt) + '</g>'
        else:
            axis = 24 + 22                       # tick labels sit above the axis, events hang below it
        body += f'<line class="viz-axis" x1="{L}" y1="{axis}" x2="{R}" y2="{axis}"/>'
        for t, tl in zip(ticks, tlab):
            tx = x(t)
            anchor = 'start' if tx < L + 20 else ('end' if tx > R - 20 else 'middle')
            ty = 14 if spans else axis - 10
            body += f'<line class="viz-tick" x1="{tx:.1f}" y1="{axis - 6}" x2="{tx:.1f}" y2="{axis}"/><text class="viz-ticklabel" x="{tx:.1f}" y="{ty}" text-anchor="{anchor}">{esc(tl)}</text>'
        # events (P40, 29 Oct 2026): each label faces right from its stem, left to it or centres on it, in a row below the
        # axis. Given the directions, a label sits below every event whose stem it would cover (so that stem ends above it)
        # and in the first such row its neighbours leave free; the directions are then improved one event at a time until
        # nothing is gained: first no stem through a label, then as few rows as possible. Each label is the date, then the
        # text wrapped at 22.
        lab = {}
        for k, e in enumerate(events):
            lines = [dates[k]] + wrap(e['label'])
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
        strict = lambda b: sum(1 for k in range(n) for j in range(n) if j != k and b[2][k][0] + 1 < lab[j][0] < b[2][k][1] - 1 and b[1][k] < b[1][j])
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
        # P58 (by eye): labels that cover each other's stems in a ring (two events a few years apart, a wide label beside
        # them) defeat a one-at-a-time search: whichever sits lower, its stem runs through another. Search every direction
        # for the events still caught in a crossing and their neighbours (up to 3^7 layouts), keeping the best
        if strict(best):
            b0, bx = best[1], best[2]
            bad = {k for k in range(n) for j in range(n) if j != k and bx[k][0] - 4 <= lab[j][0] <= bx[k][1] + 4 and b0[k] < b0[j]}
            near = lambda k, j: j != k and (bx[k][0] - 4 <= lab[j][0] <= bx[k][1] + 4 or bx[j][0] - 4 <= lab[k][0] <= bx[j][1] + 4)
            for _ in range(2):
                bad |= {j for k in bad for j in range(n) if near(k, j)}
            bad = sorted(bad, key=lambda k: lab[k][0])[:7]
            for combo in itertools.product(('start', 'middle', 'end'), repeat=len(bad)):
                if not all(fits(k, a) for k, a in zip(bad, combo)):
                    continue
                trial = dict(anch); trial.update(zip(bad, combo))
                got = layout(trial)
                if got[0] < best[0]:
                    anch, best = trial, got
                    if not strict(best):
                        break
        _, lane_of, box = best
        if tried is None or strict(best) < tried[0]:
            tried = (strict(best), W)
        if not strict(best) or final:
            break
        if W >= max(2400, 2 * W0):                           # at its widest: draw the width that crossed least
            if tried[1] == W:
                break
            Wmin, final = tried[1], True
            continue
        Wmin = math.ceil(W * 1.15 / 10) * 10
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
    return _svg(W, h, body, 'timeline' + (' viz-snug' if 700 < W <= 1.15 * 700 else ''), d.get('title'), d.get('caption'))   # round 3: a few units over the column scales to it


LABEL_COL = 240    # P55: the widest a compare or bars label column grows before its labels wrap


def _row_labels(rows, kind):
    """P55: compare and bars row labels, measured and wrapped at LABEL_COL; the column is as wide as its widest line
    plus 12, so a label is never clipped and wraps only when it is wider than the column can grow."""
    labs = [_lines(r['label'], T_LABEL, LABEL_COL) for r in rows]
    return labs, max(_width(l, T_LABEL) for l in labs) + 12


def compare(d):
    """Horizontal bars against a shared maximum, one per row, on a track. P55: labels wrap in a column that grows to
    fit them; values print with thousands separators and a word unit after a space; the value column is measured."""
    K = 'compare'
    rows = d['rows']
    for r in rows:
        if _num(r.get('value'), K, f'the value of {r.get("label")!r}') < 0:
            _fail(K, f'the value of {r["label"]!r} is negative; compare draws values of 0 or more')
    mx = d.get('max') or max(r['value'] for r in rows)
    if not mx > 0:
        _fail(K, 'max must be above 0')
    if any(r['value'] > mx for r in rows):
        _fail(K, f'a value is above max ({mx}); raise max or drop it to use the largest value')
    unit, dec = _unit(d.get('unit', '')), d.get('decimals')
    labs, LW = _row_labels(rows, K)
    vals = [str(r['display']) if r.get('display') is not None else _fmt(r['value'], dec) + unit for r in rows]
    VW = max(_tw(v, 10.5, 'mono') for v in vals) + 14
    bar_x = 8 + LW
    bar_w = W - 8 - bar_x - VW
    if bar_w < 160:
        _fail(K, f'the labels and values leave the bars {bar_w:.0f} units; shorten the labels or the "display" values')
    body, y, stick = '', 8, ''
    for r, lab, v in zip(rows, labs, vals):
        rh = max(30, len(lab) * 14 + 12)
        wv = bar_w * float(r['value']) / mx
        cy = y + rh / 2
        lt = _text(lab, T_LABEL, bar_x - 10, cy - len(lab) * 7, 'end')
        body += lt; stick += lt
        body += f'<rect class="viz-track" x="{bar_x}" y="{cy - 7:.1f}" width="{bar_w:.1f}" height="14"/>'
        body += f'<rect class="viz-bar viz-t{_tone(r, 1, K)}" x="{bar_x}" y="{cy - 7:.1f}" width="{wv:.1f}" height="14"/>'
        body += f'<text class="viz-value" x="{_val_x(bar_x, wv, bar_w, v):.1f}" y="{cy + 3.8:.1f}">{esc(v)}</text>'
        y += rh
    alt = _compare_phone(rows, vals, mx, K)
    return _svg(W, _r(y + 4), body, 'compare', d.get('title'), d.get('caption'), stick=None if alt else (bar_x - 4, stick), alt=alt)


def _val_x(bar_x, wv, bar_w, v):
    """P98 (12 Nov 2026): the x of a value printed after its bar on a track. It sits 8 units past the bar's end when it
    fits wholly on the track there (4 units clear of the track's end); otherwise it sits wholly beyond the track's end
    (6 units past it), so the track's edge never cuts through a number. The value column (VW, the widest value plus 14)
    leaves room for that in every drawing."""
    x, end = bar_x + wv + 8, bar_x + bar_w
    if x + _tw(v, 10.5, 'mono') > end - 4:
        x = max(x, end + 6)
    return x


COMPARE_PHONE_LABEL = 112   # P97: the widest a compare's pinned label column grows in its phone drawing before its labels wrap
COMPARE_PHONE_BAR = 96      # P97: the shortest track the pinned layout keeps on a phone; below it the labels go above their bars


def _compare_phone(rows, vals, mx, K):
    """P97 (12 Nov 2026): a compare's phone drawing, PHONE_NARROW units wide, emitted as svg.viz-alt (shown below 768 px
    in place of the 700-unit one), so the longest bar, its value and every label are whole in the figure's opening frame
    on a 320 or a 390 px phone, at the drawing's own size (text never scaled down). The label column stays pinned at the
    left, wrapped at COMPARE_PHONE_LABEL, when it leaves the bars COMPARE_PHONE_BAR units or more; otherwise each label
    sits above its bar, which then runs the drawing's width. Bars keep one scale, the figure's max, as in the wide one."""
    PW = PHONE_NARROW
    VW = max(_tw(v, 10.5, 'mono') for v in vals) + 14
    labs = [_lines(r['label'], T_LABEL, COMPARE_PHONE_LABEL) for r in rows]
    LW = max(_width(l, T_LABEL) for l in labs) + 12
    bar_x, body, y = 8 + LW, '', 8
    bar_w = PW - 8 - bar_x - VW
    if bar_w >= COMPARE_PHONE_BAR:                                # pinned: the label column at the left, as on a desktop
        for r, lab, v in zip(rows, labs, vals):
            rh = max(30, len(lab) * 14 + 12)
            wv, cy = bar_w * float(r['value']) / mx, y + rh / 2
            body += _text(lab, T_LABEL, bar_x - 10, cy - len(lab) * 7, 'end')
            body += f'<rect class="viz-track" x="{bar_x}" y="{cy - 7:.1f}" width="{bar_w:.1f}" height="14"/>'
            body += f'<rect class="viz-bar viz-t{_tone(r, 1, K)}" x="{bar_x}" y="{cy - 7:.1f}" width="{wv:.1f}" height="14"/>'
            body += f'<text class="viz-value" x="{_val_x(bar_x, wv, bar_w, v):.1f}" y="{cy + 3.8:.1f}">{esc(v)}</text>'
            y += rh
    else:                                                         # stacked: each label above its bar, the bar the drawing's width
        bar_x, bar_w = 8, PW - 16 - VW
        for r, v in zip(rows, vals):
            lab = _lines(r['label'], T_LABEL, PW - 16)
            body += _text(lab, T_LABEL, bar_x, y, 'start')
            y += len(lab) * 14 + 2
            wv = bar_w * float(r['value']) / mx
            body += f'<rect class="viz-track" x="{bar_x}" y="{y:.1f}" width="{bar_w:.1f}" height="14"/>'
            body += f'<rect class="viz-bar viz-t{_tone(r, 1, K)}" x="{bar_x}" y="{y:.1f}" width="{wv:.1f}" height="14"/>'
            body += f'<text class="viz-value" x="{_val_x(bar_x, wv, bar_w, v):.1f}" y="{y + 10.8:.1f}">{esc(v)}</text>'
            y += 14 + 12
    return (PW, _r(y + 4), body)


def tree(d):
    """Top-down tree. Each node is a box; leaves are laid out left to right and parents centred over their children.
    P55: the boxes keep their size (112 units, or wider when one word of a label needs it, so no word is ever broken);
    each label is measured and wrapped in full inside its box, and a level's boxes grow to its longest label. A tree
    more than 15 % wider than 700 keeps its size and scrolls in its frame (it used to shrink, to 64 units at ten leaves)."""
    K = 'tree'
    gx, gy, pad = 10, 44, 6
    root = d['root']
    nodes = []
    def walk(n, depth):
        if not isinstance(n.get('label'), str) or not n['label'].strip():
            _fail(K, f'every node needs a label: {json.dumps(n)[:80]}')
        nodes.append((n, depth))
        for k in n.get('children', []):
            walk(k, depth + 1)
    walk(root, 0)
    longest = max(_tw(w, 12, 'sansb') for n, _ in nodes for w in n['label'].split())
    node_w = max(112, math.ceil(longest + 2 * pad + 2))
    lab = {id(n): _lines(n['label'], T_NODE, node_w - 2 * pad) for n, _ in nodes}
    depth_max = max(dp for _, dp in nodes)
    lvl_h = [max(34, max(len(lab[id(n)]) for n, dp in nodes if dp == k) * 14 + 12) for k in range(depth_max + 1)]
    lvl_y = [8 + sum(lvl_h[:k]) + k * gy for k in range(depth_max + 1)]
    pos = {}
    cursor = [8]
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
    width = cursor[0] - gx + 8
    off = 0
    if width < W:                                            # P58: a tree narrower than the drawing (a one-child chain)
        off = (W - width) / 2                                # is centred in it, not drawn against its left edge; the svg
        pos = {k: (cx + off, dp) for k, (cx, dp) in pos.items()}   # carries data-x0, where the drawing starts, so a phone
                                                             # frame (natural size, scrolling) opens on it, not on the margin
    body = ''
    def draw(n):
        nonlocal body
        cx, dp = pos[id(n)]
        x, y, h = cx - node_w / 2, lvl_y[dp], lvl_h[dp]
        for k in n.get('children', []):
            kx, kd = pos[id(k)]
            ky = lvl_y[kd]
            body += f'<path class="viz-edge" d="M{cx:.1f},{y + h} C{cx:.1f},{(y + h + ky) / 2:.1f} {kx:.1f},{(y + h + ky) / 2:.1f} {kx:.1f},{ky}"/>'
            draw(k)
        tone = _tone(n, min(dp + 1, TONES), K)
        lines = lab[id(n)]
        body += _g(f'<rect class="viz-node viz-t{tone}" x="{x:.1f}" y="{y}" width="{node_w}" height="{h}" rx="2"/>'
                   + _text(lines, T_NODE, cx, y + (h - len(lines) * 14) / 2, 'middle'))
    draw(root)
    # P79 (1 Nov 2026): the svg also carries data-xr, the root box's right edge plus 8: a phone frame narrower than the
    # drawing opens with the root in view (the frame's right edge at data-xr, or at data-x0 if that is further right), so
    # a wide tree whose root stands over the middle (Greece's Hesiod tree) opens on its boxes, not on empty upper rows.
    return _svg(max(W, _r(width)), _r(lvl_y[-1] + lvl_h[-1] + 8), body, 'tree', d.get('title'), d.get('caption'), wide=width > W * 1.15,
                x0=off, xr=pos[id(root)][0] + node_w / 2 + 8)


def flow(d):
    """P42: each step's label and note are measured and wrapped to the box (as the IA kinds are), and the boxes of a row
    grow to its tallest step, so a long note never runs out of its box on a phone."""
    steps = d['steps']
    per_row = d.get('per_row', 4)
    bw, gap, pad, vgap = 150, 26, 12, 26
    if per_row <= 2:                                         # P83: a flow laid out for a phone (per_row 1 or 2) fits its frame
        bw = (PHONE_FRAME - 16 + gap) // per_row - gap       # 143 at two a row (8 + 2 × 143 + 26 + 8 = 328)
    T_NOTE = ('viz-note', 'mono', 10.5, 0, 13)
    inner = bw - 2 * pad
    laid = [(_lines(s['label'], T_NODE, inner), _lines(s['note'], T_NOTE, inner) if s.get('note') else []) for s in steps]
    def bh_of(lab, note):
        return pad + len(lab) * T_NODE[4] + (4 + len(note) * T_NOTE[4] if note else 0) + pad
    rows = (len(steps) + per_row - 1) // per_row
    rh = [max(bh_of(*laid[k]) for k in range(r * per_row, min(len(steps), (r + 1) * per_row))) for r in range(rows)]
    ry = [8 + sum(rh[:r]) + r * vgap for r in range(rows)]
    body = ''
    for k, s in enumerate(steps):
        r, c = divmod(k, per_row)
        x, y, bh = 8 + c * (bw + gap), ry[r], rh[r]
        tone = s.get('tone', 1)
        lab, note = laid[k]
        box = f'<rect class="viz-node viz-t{tone}" x="{x}" y="{y}" width="{bw}" height="{bh}" rx="2"/>'
        box += _text(lab, T_NODE, x + pad, y + pad)
        if note:
            box += _text(note, T_NOTE, x + pad, y + pad + len(lab) * T_NODE[4] + 4)
        body += _g(box)
        if k < len(steps) - 1:
            if c < per_row - 1:
                body += f'<path class="viz-arrow" d="M{x + bw + 4},{y + bh / 2} L{x + bw + gap - 6},{y + bh / 2}"/>'
            else:
                ym = y + bh + vgap / 2
                body += f'<path class="viz-arrow" d="M{x + bw / 2},{y + bh + 2} L{x + bw / 2},{ym} L{8 + bw / 2},{ym} L{8 + bw / 2},{ry[r + 1] - 4}"/>'
    w = 8 + min(len(steps), per_row) * (bw + gap) - gap + 8
    h = ry[-1] + rh[-1] + 8
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


def _balanced(s, role, px):
    """H-2: the lines of _lines(s, role, px), wrapped at the narrowest width that keeps their number, so a wrapped
    text ends on a fair line rather than one word alone ("in / smoke")."""
    lines = _lines(s, role, px)
    if len(lines) < 2:
        return lines
    lo, hi = px * 0.4, px
    while hi - lo > 2:
        mid = (lo + hi) / 2
        if len(_lines(s, role, mid)) == len(lines) and max(_tw(w, role[2], role[1], role[3]) for w in str(s).split()) <= mid:
            hi = mid
        else:
            lo = mid
    return _lines(s, role, hi)


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


def _plate(lines, role, cx, cy, lo=4, hi=None, text=None):
    """A connector's label on a plate of the card colour, centred on (cx, cy) and kept inside [lo, hi]. With text (the
    label as given, P58), the group carries it as data-text, so verify.py can check its lines join back to whole words."""
    lh = role[4]
    w, h = _width(lines, role) + 8, len(lines) * lh + 4
    x = cx - w / 2
    if hi is not None:
        x = min(x, hi - w)
    x = max(x, lo)
    inner = (f'<rect class="viz-lblbg" x="{x:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}"/>'
             + _text(lines, role, x + w / 2, cy - h / 2 + 2, 'middle'))
    return f'<g data-box="" data-text="{esc(text)}">{inner}</g>' if text is not None else _g(inner)


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
    parent, indented on a spine, which keeps a deep site legible at phone width. Depth is unlimited.
    P90 (4 Nov 2026): a node's optional "href" (a panel id) draws its box as a link to that panel, an <a> with
    data-target as the drawer's links are (shell.js delegates the click); "dashed": true draws a dashed, untinted box
    (a planned page or course). An optional top-level "phone": {"stack_from": n} adds a second drawing of the same root
    for a phone, PHONE_FRAME units wide with its boxes as wide as that allows, emitted as svg.viz-alt (the frame carries
    data-alt; the theme shows it below 768 px and the wide drawing from 768 px), so it never scrolls there."""
    K = 'sitemap'
    root = d['root']
    body, h = _sitemap_body(root, d.get('stack_from', 2), W, 132)
    alt = None
    ph = d.get('phone')
    if ph is not None:
        if not isinstance(ph, dict):
            _fail(K, 'phone must be an object, e.g. {"stack_from": 1}')
        sf = ph.get('stack_from', 1)
        depth = _sitemap_depth(root)
        nw = PHONE_FRAME - 16 - 20 * max(0, depth - max(sf, 1) + 1)   # each stacked level indents 20 units
        if nw < 132:
            _fail(K, f'the phone drawing needs boxes {nw} units wide; stack fewer levels or lower phone.stack_from')
        ab, ah = _sitemap_body(root, sf, PHONE_FRAME, nw)
        alt = (PHONE_FRAME, ah, ab)
    return _svg(W, h, body, 'sitemap', d.get('title'), d.get('caption'), alt=alt)


def _sitemap_depth(n, depth=0):
    """The depth of the deepest node under n (the root is 0)."""
    return max([depth] + [_sitemap_depth(c, depth + 1) for c in (n.get('children') or [])])


def _sitemap_body(root, stack_from, Wd, NW):
    """The sitemap drawing of root, Wd units wide with boxes NW wide: (body, height). The working keys go on a copy."""
    K = 'sitemap'
    root = copy.deepcopy(root)
    GX, GY, IND, SG, G = 14, 36, 20, 10, 16                # sibling gap, level gap, stack indent, stack gap, gutter
    TXT = NW - 16
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
        dash = ' viz-dash' if n.get('dashed') else ''
        s = f'<rect class="viz-node viz-t{n["_t"]}{dash}" x="{bx:.1f}" y="{by:.1f}" width="{NW}" height="{n["_h"]:.1f}" rx="2"/>'
        yy = by + 8
        if tag:
            s += _text(tag, T_TAG, bx + 8, yy); yy += len(tag) * 12 + 2
        s += _text(lab, T_NODE, bx + 8, yy); yy += len(lab) * 14
        if note:
            s += _text(note, T_SMALL, bx + 8, yy + 2)
        g = _g(s)
        if n.get('href'):                                    # P90: the box links to a panel, as the drawer's items do
            t = str(n['href']).lstrip('#')
            if not re.fullmatch(r'[\w-]+', t):
                _fail(K, f'href must be a panel id, got {n["href"]!r}')
            g = f'<a class="viz-a" href="#{t}" data-target="{t}" aria-label="{esc(n["label"])}">{g}</a>'
        return g

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

    prep(root, 0, 1)
    measure(root, 0, Wd - 16)
    lines, boxes = draw(root, (Wd - root['_w']) / 2, 8)
    return lines + boxes, _r(8 + root['_bh'] + 8)


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


def _cross(p, q, r, s, end=6):
    """Where segments p-q and r-s cross, away from their ends (two lines meeting at a box are not a crossing)."""
    d = (q[0] - p[0]) * (s[1] - r[1]) - (q[1] - p[1]) * (s[0] - r[0])
    if abs(d) < 1e-9:
        return None
    t = ((r[0] - p[0]) * (s[1] - r[1]) - (r[1] - p[1]) * (s[0] - r[0])) / d
    u = ((r[0] - p[0]) * (q[1] - p[1]) - (r[1] - p[1]) * (q[0] - p[0])) / d
    L1, L2 = math.hypot(q[0] - p[0], q[1] - p[1]), math.hypot(s[0] - r[0], s[1] - r[1])
    if end / L1 < t < 1 - end / L1 and end / L2 < u < 1 - end / L2:
        return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
    return None


def _dist_rect(pt, r):
    """How far a point lies from a rectangle (0 inside it)."""
    dx = max(r[0] - pt[0], 0, pt[0] - r[0] - r[2])
    dy = max(r[1] - pt[1], 0, pt[1] - r[1] - r[3])
    return math.hypot(dx, dy)


def _rect_gap(r, o):
    """The gap between two rectangles (0 when they touch or overlap)."""
    dx = max(o[0] - (r[0] + r[2]), r[0] - (o[0] + o[2]), 0)
    dy = max(o[1] - (r[1] + r[3]), r[1] - (o[1] + o[3]), 0)
    return math.hypot(dx, dy)


def _seg_rect(p, q, r):
    """How far a segment passes from a rectangle (0 when it crosses it), sampled along the segment."""
    if _hits(p, q, r, 0):
        return 0
    n = max(2, int(math.hypot(q[0] - p[0], q[1] - p[1]) / 4))
    return min(_dist_rect((p[0] + (q[0] - p[0]) * k / n, p[1] + (q[1] - p[1]) * k / n), r) for k in range(n + 1))


def _inside(pt, r, pad=0):
    return r[0] - pad <= pt[0] <= r[0] + r[2] + pad and r[1] - pad <= pt[1] <= r[1] + r[3] + pad


def _overlap(r, o, pad=0):
    return r[0] < o[0] + o[2] + pad and o[0] < r[0] + r[2] + pad and r[1] < o[1] + o[3] + pad and o[1] < r[1] + r[3] + pad


# P78 (1 Nov 2026): the reading-direction mark is a narrow isosceles triangle, 14 units from base to tip and 6 across
# the base, so its tip reads towards its object on a line at any angle at 390 px (the P66 mark, 8 by 8, read as no
# direction on a slant). A plate keeps DIRW units at its right end for it.
DIR_TIP, DIR_BACK, DIR_HALF = 7.5, 6.5, 3
DIRW = 18
DIR_GAP = 12                                             # P78: the line runs at least this far between plate and mark


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
        for f in ('attrs', 'actions'):                      # P55: a bare string here drew one letter per line
            v = o.get(f, [])
            if not isinstance(v, list) or not all(isinstance(a, str) and a.strip() for a in v):
                _fail(K, f'{o["id"]!r}: {f} must be a list of strings, one per line, e.g. ["amount", "date"]; got {json.dumps(v)[:60]}')
        objs[o['id']] = o
    grid = d['rows']
    cols = max(len(r) for r in grid)
    GY = 72
    # P58: a link label on a level line hangs in the gap between its two columns and wraps at that width; the gap
    # widens until the label's longest word fits (it was cut mid-word, "conced" / "es", in a 56-unit gap), and the
    # drawing widens and scrolls when the boxes would get narrower than 110.
    cell = {oid: (ri, c) for ri, row in enumerate(grid) for c, oid in enumerate(row) if oid is not None}
    GX = 56
    for e in d.get('links', []):
        pa, pb = cell.get(e.get('from')), cell.get(e.get('to'))
        if e.get('label') and pa and pb and pa[0] == pb[0] and abs(pa[1] - pb[1]) == 1:
            word = max(_tw(w, T_LINK[2], T_LINK[1]) for w in str(e['label']).split())
            GX = max(GX, math.ceil(word + 12 + 8 + (DIRW if e.get('dir') else 0)))   # P66: room for the direction mark
        if pa and pb and pa[0] == pb[0] and abs(pa[1] - pb[1]) == 1 and (e.get('from_card') or e.get('to_card')):   # U-9: the two counts
            GX = max(GX, math.ceil(16 + _tw(e.get('from_card') or '', 10, 'mono') + _tw(e.get('to_card') or '', 10, 'mono') + 6))   # of a level line never meet (IA7's "0..*0..*")
    Wd = W
    bw = min(220, (Wd - 16 - GX * (cols - 1)) / cols)
    if bw < 110:
        if cols > 4:
            _fail(K, f'{cols} columns leave boxes {bw:.0f} wide; use at most 4 per row')
        bw = 110
        Wd = math.ceil(16 + cols * bw + GX * (cols - 1))
    TXT = bw - 16
    x0 = (Wd - (cols * bw + GX * (cols - 1))) / 2
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
    # P66 (1 Nov 2026): every line first, so each label can be placed knowing where the lines cross. A label sits on
    # its own line at the first of a few points from the middle outwards where its plate covers no crossing, no other
    # line, no box, no count and no other label; a link may carry "dir": "to" or "from", a small solid triangle at the
    # end of its label that points at the object the label reads towards (the reading-direction mark of UML).
    segs = []
    for e in d.get('links', []):
        a, b = rects.get(e.get('from')), rects.get(e.get('to'))
        if not a or not b or a == b:
            _fail(K, f'a link needs two different objects: {json.dumps(e)[:80]}')
        if e.get('dir') not in (None, 'to', 'from'):
            _fail(K, f'a link\'s "dir" is "to" or "from" (the end its label reads towards), got {e.get("dir")!r}')
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
        segs.append((e, a, b, P, Q))
    cross = [pt for i, s1 in enumerate(segs) for s2 in segs[i + 1:] for pt in [_cross(s1[3], s1[4], s2[3], s2[4])] if pt]
    links, taken = '', [r for r in rects.values()]
    plates = []
    for e, a, b, P, Q in segs:
        links += _line([P, Q], 'viz-link')
        L = math.hypot(Q[0] - P[0], Q[1] - P[1])
        ux, uy = (Q[0] - P[0]) / L, (Q[1] - P[1]) / L
        nx, ny = -uy, ux
        if ny > 0 or (ny == 0 and nx > 0):
            nx, ny = -nx, -ny                                # cardinalities above the line, or left of a vertical one
        for end, pt, sgn, own in (('from_card', P, 1, a), ('to_card', Q, -1, b)):
            if e.get(end):
                tw = _tw(e[end], 10, 'mono')
                along = 8 + abs(ux) * tw / 2 + abs(uy) * 8
                off = 11 + abs(uy) * tw / 2
                cx, cy = pt[0] + sgn * ux * along + nx * off, pt[1] + sgn * uy * along + ny * off
                ox, oy, ow, oh = own                         # N7: on a slanted line near a box's corner the
                if (ox - tw / 2 - 2 < cx < ox + ow + tw / 2 + 2 and oy - 9 < cy < oy + oh + 9):   # count fell on the
                    cx, cy = cx - 2 * nx * off, cy - 2 * ny * off                                    # box: other side
                links += f'<text class="viz-small" x="{cx:.1f}" y="{cy + 3.6:.1f}" text-anchor="middle">{esc(e[end])}</text>'
                taken.append((cx - tw / 2, cy - 6, tw, 12))
        if e.get('label'):
            level = abs(uy) < 0.01
            if level:                                        # a level line: the label hangs under it
                lab = _lines(e['label'], T_LINK, max(40, L - 12 - (DIRW if e.get('dir') else 0)))
            else:
                lab = _lines(e['label'], T_LINK, max(min(bw, 150), max(_tw(w, T_LINK[2], T_LINK[1]) for w in str(e['label']).split()) + 1))
            onl = bool(e.get('dir')) and not level           # P78: on a slanted or vertical line the mark sits on the line
            pw, ph = _width(lab, T_LINK) + 8 + (DIRW if e.get('dir') and level else 0), len(lab) * 12.5 + 4
            sx, sy = ((ux, uy) if e.get('dir') == 'to' else (-ux, -uy)) if e.get('dir') else (0, 0)
            def variants(mx, my, r):
                """For a label plate r on its line at (mx, my): [(plate drawn, area kept clear, text box, mark centre)].
                Without a mark, or on a level line, the plate itself (the level mark at its right end). On any other line,
                the mark on the line just past the plate on its object's side ('out'), or, where that has no room, inside
                the plate grown along the line's steeper axis on that side, still on the line ('in')."""
                if not onl:
                    return [(r, [r], r, (r[0] + r[2] - DIRW / 2 - 2, r[1] + r[3] / 2) if e.get('dir') else None)]
                out = []
                ts = [t for v, lo, hi, c in ((sx, r[0], r[0] + r[2], mx), (sy, r[1], r[1] + r[3], my)) if abs(v) > 1e-6
                      for t in [((hi if v > 0 else lo) - c) / v] if t >= 0]
                inside = r[0] <= mx <= r[0] + r[2] and r[1] <= my <= r[1] + r[3]
                for gap in (DIR_GAP, 4):                     # line on both sides of the mark; 4 only where 12 has no room
                    k = (min(ts) if inside and ts else 0) + gap + DIR_BACK
                    tx, ty = mx + sx * k, my + sy * k
                    mb = (min(tx + sx * DIR_TIP, tx - sx * DIR_BACK) - DIR_HALF, min(ty + sy * DIR_TIP, ty - sy * DIR_BACK) - DIR_HALF)
                    mb = mb + (abs(sx) * (DIR_TIP + DIR_BACK) + 2 * DIR_HALF, abs(sy) * (DIR_TIP + DIR_BACK) + 2 * DIR_HALF)
                    out.append((r, [r, mb], r, (tx, ty)))
                if abs(sy) >= abs(sx):                       # steep: the plate grows up or down by DIRW
                    g = (r[0], r[1] - DIRW if sy < 0 else r[1], r[2], r[3] + DIRW)
                    ty = g[1] + DIRW / 2 + 1 if sy < 0 else g[1] + g[3] - DIRW / 2 - 1
                    tx = mx + (ty - my) * sx / sy
                    tb = (r[0], r[1] if sy > 0 else r[1], r[2], r[3])
                    if g[0] + DIR_HALF + 1 <= tx <= g[0] + g[2] - DIR_HALF - 1:
                        out.append((g, [g], tb, (tx, ty)))
                else:                                        # shallow: the plate grows left or right by DIRW
                    g = (r[0] - DIRW if sx < 0 else r[0], r[1], r[2] + DIRW, r[3])
                    tx = g[0] + DIRW / 2 + 1 if sx < 0 else g[0] + g[2] - DIRW / 2 - 1
                    ty = my + (tx - mx) * sy / sx
                    if g[1] + DIR_HALF + 1 <= ty <= g[1] + g[3] - DIR_HALF - 1:
                        out.append((g, [g], r, (tx, ty)))
                return out
            best = None
            for t in (0.5, 0.42, 0.58, 0.34, 0.66, 0.27, 0.73, 0.2, 0.8):
                mx, my = P[0] + (Q[0] - P[0]) * t, P[1] + (Q[1] - P[1]) * t
                cx, cy = (mx, my + 4 + ph / 2) if level else (mx, my)
                x = max(4, min(cx - pw / 2, Wd - 4 - pw))
                for vi, (plate, Rs, tb, mc) in enumerate(variants(mx, my, (x, cy - ph / 2, pw, ph))):
                    if any(R[0] < 2 or R[0] + R[2] > Wd - 2 for R in Rs):
                        continue                             # the plate and its mark, each kept clear (P78)
                    hard = sum(1 for R in Rs for c in cross if _inside(c, R, 6)) + sum(1 for R in Rs for o in taken + plates if _overlap(R, o, 2))
                    soft = sum(1 for R in Rs for e2, _, _, P2, Q2 in segs if e2 is not e and _hits(P2, Q2, R, 2))
                    clear = min([_dist_rect(c, R) for R in Rs for c in cross] + [_seg_rect(P2, Q2, R) for R in Rs for e2, _, _, P2, Q2 in segs if e2 is not e]
                                + [_rect_gap(R, o) for R in Rs for o in plates] + [99])    # and from every label already placed
                    score = (hard, soft, vi, clear < 14, -min(clear, 14), abs(t - 0.5))   # the mark's own line first (P78), then 14 clear, then the middle
                    if best is None or score < best[0]:
                        best = (score, plate, Rs, tb, mc)
            if best is None or best[0][0]:
                _fail(K, f'the label of {e["from"]} - {e["to"]} ({e["label"]!r}) has no place on its line clear of every crossing, '
                         'box and other label; move a box')
            _, (x, top, pw, ph), Rs, tb, mc = best
            plates += Rs
            mark = ''
            if mc:                                           # the reading-direction mark (P78): a narrow isosceles, tip
                tx, ty = mc                                  # DIR_TIP ahead of its centre, base DIR_BACK behind, 2 x DIR_HALF wide
                mark = (f'<path class="viz-head" d="M{tx + sx * DIR_TIP:.1f},{ty + sy * DIR_TIP:.1f} '
                        f'L{tx - sx * DIR_BACK - sy * DIR_HALF:.1f},{ty - sy * DIR_BACK + sx * DIR_HALF:.1f} '
                        f'L{tx - sx * DIR_BACK + sy * DIR_HALF:.1f},{ty - sy * DIR_BACK - sx * DIR_HALF:.1f} z"/>')
            tw_ = tb[2] - (DIRW if e.get('dir') and level else 0)
            links += (f'<g data-box="" data-text="{esc(e["label"])}"><rect class="viz-lblbg" x="{x:.1f}" y="{top:.1f}" width="{pw:.1f}" height="{ph:.1f}"/>'
                      + _text(lab, T_LINK, tb[0] + tw_ / 2, tb[1] + 2, 'middle') + mark + '</g>')
    return _svg(Wd, _r(y - GY + 8), links + body, 'objects', d.get('title'), d.get('caption'), wide=Wd > W * 1.15)


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


def matrix(d, narrow=None):
    """A labelled grid: row labels down the left, column labels across the top, each cell a short mark or word on a
    field of its tone (an empty cell is blank); an optional legend under the grid says what each mark means."""
    K = 'matrix'
    cols, rows = d['cols'], d['rows']
    if not cols or not rows:
        _fail(K, 'a matrix needs cols and rows')
    if d.get('numeric'):
        return _heat(d, narrow)
    LW = min(240, max(90, max(_tw(r['label'], 12) for r in rows) + 20))   # H-2: a row label keeps to one line up to 240
    n = len(cols)
    # P53 (1 Nov 2026): each column is as wide as its widest cell (a mark on one line) or its header (its longest word,
    # or the whole header up to 140), not a share of the 700-unit width; when the columns need more than the width
    # they share it, the narrow ones keeping their size and the long ones wrapping, and below 70 each the drawing widens.
    # A matrix narrower than the width is drawn at its own width (viz-fit), so on a phone it does not scroll for margin.
    for r in rows:
        if len(r.get('cells', [])) != n:
            _fail(K, f'row {r.get("label")!r} has {len(r.get("cells", []))} cells for {n} columns')
    mark = lambda c: c if isinstance(c, str) else (c or {}).get('mark', '') if isinstance(c, dict) else ''
    nat = []
    for k, c in enumerate(cols):
        hw = max(max(_tw(w, 10, 'mono', 0.4) for w in str(c).split()), min(_tw(str(c), 10, 'mono', 0.4), 140)) + 14
        cl = max([_tw(mark(r['cells'][k]), 10.5, 'mono') + 18 for r in rows if mark(r['cells'][k])] or [0])
        nat.append(math.ceil(max(56, hw, cl)))
    avail = W - 16 - LW
    if sum(nat) <= avail:
        cws = nat
    else:
        cws, left, rest = list(nat), avail, sorted(range(n), key=lambda k: nat[k])
        while rest and nat[rest[0]] <= left / len(rest):
            left -= nat[rest[0]]; rest.pop(0)
        tot = sum(nat[k] for k in rest)                      # the long ones share what is left in proportion to their text
        for k in rest:
            cws[k] = left * nat[k] / tot
    wide = min(cws) < 70 and sum(nat) > avail
    words = lambda t, f, sz, ls=0: max([_tw(w, sz, f, ls) for w in str(t).split()] or [0])   # the widest word, unbroken
    if not wide:                                             # U-9: no column below its longest word (IA6's B.5 split
        piece = lambda s, sz=10.5, ls=0: max([_tw(w, sz, 'mono', ls) for w in re.split(r'\s+|(?<=-)', str(s)) if w] or [0])   # a hyphen may break
        floor = [math.ceil(max([piece(c, 10, 0.4) + 14] + [piece(mark(r['cells'][k])) + 15 for r in rows]))
                 for k, c in enumerate(cols)]                # "notification / s"): a narrow one takes width from the
        lack = sum(max(0, floor[k] - cws[k]) for k in range(n))   # columns above their floor, in proportion to their surplus
        over = {k: cws[k] - floor[k] for k in range(n) if cws[k] > floor[k]}
        if lack and sum(over.values()) >= lack:
            tot = sum(over.values())
            for k in range(n):
                cws[k] = floor[k] if cws[k] < floor[k] else cws[k] - lack * over.get(k, 0) / tot
    if wide:                                                 # too many columns for the width: each takes the narrowest width
        cws = [max(70, math.ceil(max([words(c, 'mono', 10, 0.4) + 14] + [words(mark(r['cells'][k]), 'mono', 10.5) + 18 for r in rows])))
               for k, c in enumerate(cols)]
    # what the columns leave goes first to headers that would wrap, until each sits on one line, then to the row
    # labels (H-2: a header or label was left with one word on a line of its own beside empty width)
    slack = W - 16 - LW - sum(cws)
    for k, c in enumerate(cols):
        grow = min(max(0, math.ceil(_tw(str(c), 10, 'mono', 0.4) + 14) - cws[k]), slack)
        if 0 < grow and slack > 0:
            cws[k] += grow; slack -= grow
    LW = max(LW, min(max(_tw(r['label'], 12) for r in rows) + 20, W - 16 - sum(cws)))
    # a label column whose labels wrap keeps only the width its balanced lines need; what it frees goes to the columns
    # whose cells wrap, up to their one-line width
    labs = [_balanced(r['label'], T_LABEL, LW - 12) for r in rows]
    need = max(90, math.ceil(max(_width(l, T_LABEL) for l in labs)) + 20)
    if need < LW:
        free, LW = LW - need, need
        short = {k: nat[k] - cws[k] for k in range(n) if nat[k] > cws[k] + 1}
        tot = sum(short.values())
        for k, v in short.items():
            cws[k] += min(v, free * v / tot)
    # when the columns share the width and a cell runs to more lines than its row's others need, width moves to its
    # column from columns that can give it without adding a line anywhere (H-2: "dentils" alone on a third line)
    if not wide and sum(nat) > avail:
        def nlines(k, w):
            return max([len(_balanced(mark(r['cells'][k]), T_MARK, w - 14)) for r in rows if mark(r['cells'][k])] or [1])
        def relieve(k, cur):                                 # try to save column k one line; True if done
            lo, hi = cws[k], nat[k]
            if hi - lo < 1:
                return False
            while hi - lo > 2:                               # the narrowest width that saves this column a line
                mid = (lo + hi) / 2
                lo, hi = (mid, hi) if nlines(k, mid) >= cur[k] else (lo, mid)
            if nlines(k, hi) >= cur[k]:
                return False
            need, spare = hi - cws[k], {}
            for j in range(n):
                if j != k:
                    w, hmin = cws[j], max(56, words(cols[j], 'mono', 10, 0.4) + 14)   # never below its header's longest word
                    while w - 2 >= hmin and nlines(j, w - 2) <= cur[j] and cws[j] - (w - 2) < need:
                        w -= 2
                    spare[j] = cws[j] - w
            if sum(spare.values()) < need:
                return False
            for j, v in spare.items():
                take = min(v, need); cws[j] -= take; need -= take
            cws[k] = hi
            return True
        for _ in range(16):
            cur = [nlines(k, cws[k]) for k in range(n)]
            if not any(relieve(k, cur) for k in sorted(range(n), key=lambda j: -cur[j]) if cur[k] > 1):
                break
    if narrow is not None and LW > narrow:                   # C1 (15 Nov 2026): the drawing a phone of 360 px and below shows keeps
        LW = narrow                                          # its row labels in a narrow column, wrapped to more lines, so the
        labs = [_balanced(r['label'], T_LABEL, LW - 12) for r in rows]   # sticky copy leaves room for the cells beside it
    if narrow is not None:                                   # C1 re-check: no column wider than the room right of the sticky
        room = NARROW_FRAME - (8 + LW) - 12                  # column, so a scrolled-to-the-end frame shows the last column whole
        cws = [min(cw, max(room, math.ceil(max([words(c, 'mono', 10, 0.4) + 14] + [words(mark(r['cells'][k]), 'mono', 10.5) + 18 for r in rows]))))
               for k, (cw, c) in enumerate(zip(cws, cols))]  # but never below the column's longest word
    leg = [_tw(i.get('mark', ''), 10.5, 'mono') + 16 + 8 + min(220, _tw(i.get('means', ''), 11)) + 18 for i in d.get('legend') or []]
    Wd = max(16 + LW + sum(cws), NARROW_FRAME) if narrow is not None else max(16 + LW + sum(cws), min(W, max(leg or [0]) + 16), 320)   # C1: the narrow drawing's legend wraps inside the 320 px frame
    xs = [8 + LW + sum(cws[:k]) for k in range(n)]
    heads = [_balanced(c, T_COL, cws[k] - 10) for k, c in enumerate(cols)]
    hh = max(len(h) for h in heads) * 12 + 12
    body = ''.join(_text(h, T_COL, xs[k] + cws[k] / 2, hh - 6 - len(h) * 12, 'middle') for k, h in enumerate(heads))
    y, stick = 8 + hh, ''
    for r in rows:
        rt = _tone(r, 4, K)
        cells = []
        for k, c in enumerate(r['cells']):
            if c is None or c == '':
                cells.append(([], rt))
            elif isinstance(c, str):
                cells.append((_balanced(c, T_MARK, cws[k] - 14), rt))
            else:
                cells.append((_balanced(c.get('mark', ''), T_MARK, cws[k] - 14) if c.get('mark') else [], _tone(c, rt, K)))
        lab = labs[rows.index(r)]
        rh = max(32, max(len(m) for m, _ in cells) * 13 + 14, len(lab) * 14 + 12)
        lt = _text(lab, T_LABEL, 8, y + (rh - len(lab) * 14) / 2)
        body += lt; stick += lt
        for k, (m, t) in enumerate(cells):
            x, cw = xs[k], cws[k]
            cls = f'viz-band viz-t{t}' if m else 'viz-track'
            body += _g(f'<rect class="{cls}" x="{x + 2:.1f}" y="{y + 2:.1f}" width="{cw - 4:.1f}" height="{rh - 4:.1f}"/>'
                       + _text(m, T_MARK, x + cw / 2, y + (rh - len(m) * 13) / 2, 'middle'))
        y += rh
    grid_h = y + 2
    key = None
    if d.get('legend'):
        y += 14
        ky0, kb0 = y - 8, len(body)   # P109 round 2: the keys are drawn in their own svg, outside the scroller
        x, lrow = 8, 24
        LWd = min(Wd, NARROW_FRAME - 36 if narrow is not None else PHONE_FRAME)   # C1 re-check: the narrow drawing's legend fits a 320 px frame   # W-DD-PB1 (13 Nov 2026): a drawing wider than the phone frame keeps its legend inside the frame's width, so the first frame shows every key whole
        for item in d['legend']:
            m, means = item.get('mark', ''), item.get('means', '')
            mw = _tw(m, 10.5, 'mono') + 16
            room = LWd - 16 - mw - 8 - 18                    # a key's text keeps to one line when the drawing has room
            if narrow is not None and max([_tw(w, 11) for w in str(means).split()] or [0]) + 4 > room:
                # C1 re-check: in the 320 px drawing a key whose words do not fit beside its band sits on rows of its own, the text under the band
                txt = _lines(means, T_ATTR, LWd - 16 - 18)
                if x > 8:
                    x, y, lrow = 8, y + lrow + 8, 24
                body += _g(f'<rect class="viz-band viz-t{_tone(item, 4, K)}" x="{x:.1f}" y="{y:.1f}" width="{mw:.1f}" height="24"/>'
                           + _text([m], T_MARK, x + mw / 2, y + 5.5, 'middle')) + _text(txt, T_ATTR, 8, y + 30)
                x, y, lrow = 8, y + 30 + len(txt) * 14 + 8, 24
                continue
            txt = _lines(means, T_ATTR, room if _tw(means, 11) <= room else min(220, room))
            iw = mw + 8 + _width(txt, T_ATTR) + 18
            if x > 8 and x + iw > LWd - 8:
                x, y, lrow = 8, y + lrow + 8, 24
            if narrow is not None and len(txt) == 3:          # C1 re-check: in the 320 px drawing a three-line key hangs from its band's top too
                body += _g(f'<rect class="viz-band viz-t{_tone(item, 4, K)}" x="{x:.1f}" y="{y:.1f}" width="{mw:.1f}" height="24"/>'
                           + _text([m], T_MARK, x + mw / 2, y + 5.5, 'middle')) + _text(txt, T_ATTR, x + mw + 8, y - 2)
                x += iw
                lrow = max(lrow, len(txt) * 14)
                continue
            body += _g(f'<rect class="viz-band viz-t{_tone(item, 4, K)}" x="{x:.1f}" y="{y:.1f}" width="{mw:.1f}" height="24"/>'
                       + _text([m], T_MARK, x + mw / 2, y + 5.5, 'middle')) + _text(txt, T_ATTR, x + mw + 8, y + 12 - (len(txt) * 7 if len(txt) <= 3 else 14))   # U-7: a key of four lines or more starts at its band's top and hangs down, never up over the row above
            x += iw
            lrow = max(lrow, len(txt) * 14)
        y += lrow
        key = (_r(LWd), _r(y + 8 - ky0), f'<g transform="translate(0,{-ky0:.1f})">{body[kb0:]}</g>')
        body, y = body[:kb0], grid_h - 2
    if narrow is not None:
        return _r(Wd), _r(y + 8), body, (8 + LW, stick, grid_h), key
    nar, keyn = None, None
    if Wd > NARROW_FRAME:   # C1: a second drawing for 360 px and below, with its own narrow column (or narrower columns)
        nw, nh, nb, nst, keyn = matrix(d, narrow=NARROW_LW)
        nar = (nw, nh, nb, nst if nw > NARROW_FRAME else None)
    # P109 (16 Nov 2026): a matrix whose columns had to share the width but whose drawing still fits it (PB8 figure 4, 700 units)
    # is not wide: it scales to the column like any other, and never overflows a 698 px desktop frame by 2 px under its fade.
    # P109 round 2 (17 Nov 2026): and one less than 15 % wider than 700 scales too, as a tree does (Rome 3.1 figure 3, 765 units,
    # lost its row labels when scrolled on a desktop, where the label column is not sticky).
    return _svg(_r(Wd), _r(y + 8), body, 'matrix' + (' viz-fit' if Wd < W - 24 else ''), d.get('title'), d.get('caption'), wide=wide and Wd > W * 1.15,
                stick=(8 + LW, stick, grid_h) if Wd > NARROW_FRAME else None, narrow=nar, keys=(key, keyn))   # C1: a column wherever a 320 px frame scrolls


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
    # U-13 (10 Nov 2026): a label between two states in a row wraps at gap - 8; a word wider than that was broken inside
    # ("informati / on"). The gap widens to the longest word of any transition label, and is unchanged where all fit.
    lw = max((_tw(w, T_LINK[2], T_LINK[1], T_LINK[3]) for tr in d.get('transitions', []) for w in str(tr.get('label', '')).split()), default=0)
    gap = max(gap, math.ceil(lw) + 8)
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


def _line_draw(d, W):
    """One drawing of a line chart, W units wide: (width, height, body). line() draws it twice, wide and for a phone."""
    K = 'line'
    xs, series = d.get('x'), d.get('series')
    if not xs or not series:
        _fail(K, 'a line chart needs x and series')
    n = len(xs)
    numeric = all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in xs)
    if numeric and any(b <= a for a, b in zip(xs, xs[1:])):
        _fail(K, 'numeric x values must increase')
    years, unit, dec = d.get('years', False), _unit(d.get('unit', '')), d.get('decimals')
    fx = (lambda v: yr(v, K)) if (years and numeric) else (lambda v: _fmt(v) if numeric else str(v))
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
    return W, _r(H), grid + body + marks + labs


def line(d):
    """One or more named series over an ordered x (years, periods or any ordered labels), each point labelled with its
    value (or only the first and last), optional annotations as dashed verticals with a note, and a legend.
    P123 (15 Nov 2026): two drawings, as compare and bars have. The wide one is W (700) units, scaled to the column at
    768 px and up; the phone one is PHONE_NARROW (258) units wide, the frame of a 320 px phone, drawn from the same data
    and shown below 768 px, so the y-axis, the legend, the title and every point label are in the opening frame and the
    chart never scrolls on a phone. A label that cannot find room at 258 units falls back to labels "ends" for the phone
    drawing only; a figure that cannot draw at that width raises, as at any width."""
    import copy as _c
    w, h, body = _line_draw(_c.deepcopy(d), W)
    try:
        pw, ph, pb = _line_draw(_c.deepcopy(d), PHONE_NARROW)
    except SystemExit:
        if d.get('labels', 'all' if len(d.get('x') or []) <= 8 else 'ends') in ('ends', 'none'):
            raise
        dd = _c.deepcopy(d); dd['labels'] = 'ends'
        pw, ph, pb = _line_draw(dd, PHONE_NARROW)
    return _svg(w, h, body, 'linechart', d.get('title'), d.get('caption'), alt=(pw, ph, pb))


def _bars_wide(d):
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
    unit, dec = _unit(d.get('unit', '')), d.get('decimals')
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
    labs, LW = _row_labels(rows, K)
    vals = [_fmt(v, dec) + unit for r, t in zip(rows, tot) for v in (r['values'] + [t])]
    VW = max(_tw(v, 10.5, 'mono') for v in vals) + 12
    bx, bw = 8 + LW, W - 8 - (8 + LW) - VW
    if bw < 160:
        _fail(K, f'the labels and values leave the bars {bw:.0f} units; shorten the labels')
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
    return body + base + marks, W, _r(y - 14 + 8)




def _bars_phone(d):
    """Grouped or stacked horizontal bars across categories: one bar per series in each row (grouped) or one bar of
    segments (stacked); values at the bar ends (a stacked bar's total at its end, a segment's value inside it when it
    fits); a legend names the series. P83 (3 Nov 2026): the row label sits above its bars and the drawing is as wide as
    a phone's figure frame (PHONE_NARROW since P98, 12 Nov 2026: a 320 px phone's frame; PHONE_FRAME before), so on a phone a bar, its value and its label are always in view together; on a
    wider screen the drawing keeps that size (viz-fit) instead of stretching to the column."""
    K = 'bars'
    series, rows = d.get('series'), d.get('rows')
    mode = d.get('mode', 'grouped')
    if mode not in ('grouped', 'stacked'):
        _fail(K, 'mode is "grouped" or "stacked"')
    if not series or not rows:
        _fail(K, 'bars need series and rows')
    ns = len(series)
    unit, dec = _unit(d.get('unit', '')), d.get('decimals')
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
    Wd = PHONE_NARROW   # P98 (12 Nov 2026): was PHONE_FRAME (328), which scrolled on a 320 px phone
    labs = [_lines(r['label'], T_LABEL, Wd - 16) for r in rows]
    vals = [_fmt(v, dec) + unit for r, t in zip(rows, tot) for v in (r['values'] + [t]) if v is not None]
    VW = max(_tw(v, 10.5, 'mono') for v in vals) + 12
    bx, bw = 8, Wd - 8 - 8 - VW
    if bw < 120:
        _fail(K, f'the values leave the bars {bw:.0f} units; shorten the "unit" or drop decimals')
    body, top = '', 8
    lg, lh = _legend([(s['name'], s['_t'], 'bar') for s in series], top, Wd, K)
    body += lg; top += lh + 12
    y, marks = top, ''
    BH, BG = (12, 3) if mode == 'grouped' else (20, 0)
    for r, lab, t in zip(rows, labs, tot):
        marks += _text(lab, T_LABEL, bx, y)
        by = y + len(lab) * 14 + 4
        if mode == 'grouped':
            for k, (s, v) in enumerate(zip(series, r['values'])):
                yy = by + k * (BH + BG)
                if v is None:
                    continue
                wv = bw * v / mx
                if wv > 0:
                    marks += f'<rect class="viz-bar viz-t{s["_t"]}" x="{bx:.1f}" y="{yy:.1f}" width="{wv:.1f}" height="{BH}"/>'
                marks += f'<text class="viz-value" x="{bx + wv + 6:.1f}" y="{yy + BH / 2 + 3.8:.1f}">{esc(_fmt(v, dec) + unit)}</text>'
            block = ns * BH + (ns - 1) * BG
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
            block = BH
        y = by + block + 14
    base = _line([(bx, top - 2), (bx, y - 12)], 'viz-base')
    return body + base + marks, Wd, _r(y - 14 + 8)




def bars(d):
    """Grouped or stacked horizontal bars. Two drawings (P83, 3 Nov 2026, Pedro: "it should be responsive"): the wide one,
    labels in a column at the left, 700 units, scaled to the column at 768 px and up; and the phone one, the row label
    above its bars, as wide as a 320 px phone's frame (PHONE_NARROW since P98), shown below 768 px so the chart never scrolls there. Both
    are drawn from the same data by _bars_wide and _bars_phone; the theme shows one at a time."""
    import copy as _c
    body, w, h = _bars_wide(_c.deepcopy(d))
    pb, pw, ph = _bars_phone(_c.deepcopy(d))
    return _svg(w, h, body, 'bars', d.get('title'), d.get('caption'), alt=(pw, ph, pb))


def _scatter_draw(d, W, height=None, wrap=150):
    """One drawing of a scatter, W units wide: (width, height, body). scatter() draws it twice, wide and for a phone."""
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
        ax[a] = dict(lo=min(lo, t[0]), hi=max(hi, t[-1]), ticks=t, unit=_unit(o.get('unit', '')), dec=o.get('decimals'),
                     label=o.get('label', ''), years=o.get('years', False))
    tl = lambda a, v: yr(v, K) if ax[a]['years'] else _fmt(v, ax[a]['dec']) + ax[a]['unit']
    L = 8 + max(_tw(tl('y', t), 10.5, 'mono') for t in ax['y']['ticks']) + 8
    R, top = W - 12, 8
    body = ''
    if ax['y']['label']:
        body += _text([ax['y']['label']], T_COL, 8, top); top += 18
    PT, PH = top + 6 + (14 if W < 400 else 0), height or d.get('height', 340)   # P124: a phone's drawing leaves 14 units above the plot, where the label of a point on the top edge sits
    PB = PT + PH
    X = lambda v: L + (v - ax['x']['lo']) / (ax['x']['hi'] - ax['x']['lo']) * (R - L)
    Y = lambda v: PB - (v - ax['y']['lo']) / (ax['y']['hi'] - ax['y']['lo']) * PH
    for t in ax['y']['ticks']:
        body += _line([(L, Y(t)), (R, Y(t))], 'viz-grid') + f'<text class="viz-ticklabel" x="{L - 6:.1f}" y="{Y(t) + 3.6:.1f}" text-anchor="end">{esc(tl("y", t))}</text>'
    xt = ax['x']['ticks']
    if W < 400:                                              # P124: on a phone's drawing keep every k-th x tick, the fewest that leaves 6 units between two tick labels
        for k_ in range(1, len(xt)):
            keep = xt[::k_] if (len(xt) - 1) % k_ == 0 else xt[::k_] + [xt[-1]]
            if all(X(b) - _tw(tl('x', b), 10.5, 'mono') / 2 - (X(a) + _tw(tl('x', a), 10.5, 'mono') / 2) >= 6 for a, b in zip(keep, keep[1:])):
                xt = keep; break
        else:
            xt = [xt[0], xt[-1]]
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
            if _clash(rect, dots, 1) and W < 400:            # P124: on a phone's drawing the name moves along its own quadrant to the first spot that covers no point
                y_lo, y_hi = (PT, qy) if vy == 't' else (qy, PB)
                for dy_ in range(0, int(y_hi - y_lo) + 1, 6):
                    for dx_ in range(0, int(hi_x - lo_x) + 1, 6):
                        r_ = (rect[0] + (dx_ if hx == 'l' else -dx_), rect[1] + (dy_ if vy == 't' else -dy_), w, h)
                        if lo_x <= r_[0] and r_[0] + w <= hi_x and y_lo <= r_[1] and r_[1] + h <= y_hi and not _clash(r_, dots + plates, 1):
                            rect = r_; break
                    else:
                        continue
                    break
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
        lab = _lines(p['label'], T_LABEL, wrap)
        w, h = _width(lab, T_LABEL) + 8, len(lab) * 14 + 4
        cands = []
        for dist in ((8, 16, 28, 44) if W < 400 else (8, 16, 28)):
            cands += [(x_ + dist + w / 2, y_), (x_ - dist - w / 2, y_), (x_, y_ - dist - h / 2), (x_, y_ + dist + h / 2),
                      (x_ + dist / 2 + w / 2, y_ - dist / 2 - h / 2), (x_ - dist / 2 - w / 2, y_ - dist / 2 - h / 2),
                      (x_ + dist / 2 + w / 2, y_ + dist / 2 + h / 2), (x_ - dist / 2 - w / 2, y_ + dist / 2 + h / 2)]
        spot = next((c for c in cands if L + 2 <= c[0] - w / 2 and c[0] + w / 2 <= W - 4 and PT - (18 if W < 400 else 4) <= c[1] - h / 2 and c[1] + h / 2 <= PB - 2
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
    return W, _r(H), body + marks + labs


def scatter(d):
    """Labelled points on two numeric axes with gridlines at the ticks, optional quadrant lines with a name in each
    quadrant's outer corner; each label is placed where it covers no point, no other label and no quadrant name.
    P124 (15 Nov 2026): two drawings, as line, compare and bars have. The wide one is W (700) units, scaled to the column
    at 768 px and up; the phone one is PHONE_NARROW (258) units wide, the frame of a 320 px phone, drawn from the same
    data and shown below 768 px, so the y-axis, the title and every point label are in the opening frame and the chart
    never scrolls on a phone. For the phone drawing only, x ticks are thinned to keep their labels apart, labels wrap
    at half the width, and a drawing that cannot place a label or a quadrant name is retried taller (in steps of an eighth, up to 3 times "height"), then raises, as at any width."""
    import copy as _c
    w, h, body = _scatter_draw(_c.deepcopy(d), W)
    base, err = d.get('height', 340), None
    for mult in [1 + k / 8 for k in range(21)]:
        try:
            pw, ph, pb = _scatter_draw(_c.deepcopy(d), PHONE_NARROW, round(base * mult), min(150, (PHONE_NARROW - 24) // 2))
            break
        except SystemExit as e:
            err = e
    else:
        raise err
    return _svg(w, h, body, 'scatter', d.get('title'), d.get('caption'), alt=(pw, ph, pb))


def range_(d):
    """Competing estimates: per row, a label, then a bar from the lowest to the highest estimate with an optional point
    estimate (its value above it), and under the bar each end's value with a short source tag, aligned to its end of
    the bar (inside the bar's span when both fit, else outside it). A shared axis with gridlines runs under the rows.
    P55: with "years": true every value is a year and prints as one (264 BC, AD 14; no year 0); without it, a range
    whose values are all whole numbers and include a negative one stops the build, since it reads as years BC printed
    as negative numbers: add "years": true, or "decimals" if the values are quantities below zero."""
    K = 'range'
    rows = d.get('rows')
    if not rows:
        _fail(K, 'a range needs rows')
    unit, dec, years = _unit(d.get('unit', '')), d.get('decimals'), d.get('years', False)
    era = _era(d, K)
    # P58: a word unit takes the singular for 1 ("1 head", not "1 heads"): "unit_one" when given, else the unit less a
    # final s; a word unit that does not end in s ("men") needs "unit_one" before a value of 1 can print.
    one = d.get('unit_one')
    if one is None and unit.startswith(' ') and unit.endswith('s') and not unit.endswith('ss'):
        one = unit[1:-1]
    one = _unit(one) if one is not None else None
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
    if not years and dec is None and min(vs) < 0 and all(float(v).is_integer() for v in vs):
        _fail(K, 'the values include negative whole numbers, which print as "-264": if they are years, add "years": true '
                 '(they print as 264 BC); if they are quantities, give "decimals"')
    lo, hi = d.get('min', min(vs) if years else min(0, min(vs))), d.get('max', max(vs))
    ticks = d.get('ticks') or _ticks(lo, hi)
    lo, hi = min(lo, ticks[0]), max(hi, ticks[-1])
    PL, PR = 24, W - 24
    X = lambda v: PL + (v - lo) / (hi - lo) * (PR - PL)
    def num(v):
        if years:
            return yr(v, K, era)
        u = unit
        if unit.startswith(' ') and v == 1:
            if one is None:
                _fail(K, f'a value of 1 would print as "1{unit}": give "unit_one", the singular of {unit.strip()!r}')
            u = one
        return _fmt(v, dec) + u
    tag = lambda v, src: num(v) + (f' · {src}' if src else '')
    def plate(cx, lines, top):                               # an end label centred under x = cx, kept inside the drawing
        w = _width(lines, T_VAL) + 8
        return (min(max(4, cx - w / 2), W - 4 - w), top, w, 17)
    under = lambda rc, cx: rc[0] - 0.5 <= cx <= rc[0] + rc[2] + 0.5
    y, marks, plates = 8, '', []
    for k, r in enumerate(rows):
        row0 = len(marks)
        t = _tone(r, d.get('tone', 4), K)
        lab = _lines(r['label'], T_LABEL, W - 16)
        marks += _text(lab, T_LABEL, 8, y)
        y += len(lab) * 14 + 4
        single = r['low'] == r['high']
        if r.get('point') is not None and not single:
            pv = [num(r['point'])]
            pw = _width(pv, T_VAL)
            px_ = min(max(X(r['point']), 8 + pw / 2), W - 8 - pw / 2)
            marks += _text(pv, T_VAL, px_, y, 'middle')
            y += 14
        x1, x2 = X(r['low']), X(r['high'])
        if not single:
            marks += f'<rect class="viz-rangebar viz-t{t}" x="{x1:.1f}" y="{y:.1f}" width="{x2 - x1:.1f}" height="10"/>'
        if r.get('point') is not None or single:                # P58: a single value is drawn as a point
            cx = X(r['point'] if r.get('point') is not None else r['low'])
            marks += f'<path class="viz-est" d="M{cx:.1f},{y - 2:.1f} L{cx + 7:.1f},{y + 5:.1f} L{cx:.1f},{y + 12:.1f} L{cx - 7:.1f},{y + 5:.1f} z"/>'
        y += 14
        if single:                                            # P58: one value, printed once, with one source tag
            srcs = list(dict.fromkeys(x for x in (r.get('low_src'), r.get('high_src')) if x))
            lt = [tag(r['low'], ', '.join(srcs))]
            a = plate(x1, lt, y)
            marks += f'<g data-end="{x1:.1f}">' + _plate_at(a, lt, T_VAL) + '</g>'
            y += 17
        else:
            # P58: each end's label sits under the value it names (its plate spans the bar's end): reading inward when
            # both fit under the bar, else centred on each end, else meeting at the bar's middle, else the high one a
            # line lower, centred on its end.
            lt, ht = [tag(r['low'], r.get('low_src'))], [tag(r['high'], r.get('high_src'))]
            lw, hw = _width(lt, T_VAL) + 8, _width(ht, T_VAL) + 8
            mid = (x1 + x2) / 2
            tries = [((x1 - 4, y, lw, 17), (x2 + 4 - hw, y, hw, 17)),
                     (plate(x1, lt, y), plate(x2, ht, y)),
                     ((max(4, mid - 2 - lw), y, lw, 17), (min(W - 4 - hw, mid + 2), y, hw, 17)),
                     (plate(x1, lt, y), plate(x2, ht, y + 18))]
            a, b = next(((a, b) for a, b in tries if not _clash(a, [b], 2) and under(a, x1) and under(b, x2)), tries[-1])
            marks += (f'<g data-end="{x1:.1f}">' + _plate_at(a, lt, T_VAL) + '</g>'
                      + f'<g data-end="{x2:.1f}">' + _plate_at(b, ht, T_VAL) + '</g>')
            y = max(a[1] + a[3], b[1] + b[3])
        marks = marks[:row0] + f'<g data-row="{k}">' + marks[row0:] + '</g>'
        y += 16
    grid = ''
    for tk in ticks:
        grid += _line([(X(tk), 8), (X(tk), y - 8)], 'viz-grid')
        tl = yr(tk, K, era) if years else _fmt(tk, dec) + unit
        hw = _tw(tl, 10.5, 'mono') / 2
        anchor = 'start' if X(tk) - hw < 4 else ('end' if X(tk) + hw > W - 4 else 'middle')
        grid += f'<text class="viz-ticklabel" x="{X(tk):.1f}" y="{y + 6:.1f}" text-anchor="{anchor}">{esc(tl)}</text>'
    H = y + 14
    if d.get('xlabel'):
        grid += f'<text class="viz-colhead" x="{PR:.1f}" y="{H + 6:.1f}" text-anchor="end">{esc(d["xlabel"])}</text>'
        H += 16
    return _svg(W, _r(H), grid + marks, 'range', d.get('title'), d.get('caption'))


def _heat(d, narrow=None):
    """matrix with "numeric": true: each cell a number (or null for blank) on one of five shades of the figure's tone,
    shaded by value between min and max (default the data's); a legend under the grid gives each shade's range."""
    K = 'matrix'
    cols, rows = d['cols'], d['rows']
    tone = _tone(d, 4, K)
    unit, dec = _unit(d.get('unit', '')), d.get('decimals')
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
    if narrow is not None and LW > narrow:                   # C1: the drawing for 360 px and below
        LW = narrow
    if narrow is not None:                                   # C1 re-check: no column wider than the room right of the sticky column
        cw = min(cw, NARROW_FRAME - (8 + LW) - 12)
    Wd = 16 + LW + n * cw
    heads = [_lines(c, T_COL, cw - 10) for c in cols]
    hh = max(len(h) for h in heads) * 12 + 12
    body = ''.join(_text(h, T_COL, 8 + LW + (k + 0.5) * cw, hh - 6 - len(h) * 12, 'middle') for k, h in enumerate(heads))
    y, stick = 8 + hh, ''
    for r in rows:
        lab = _lines(r['label'], T_LABEL, LW - 12)
        rh = max(32, len(lab) * 14 + 12)
        lt = _text(lab, T_LABEL, 8, y + (rh - len(lab) * 14) / 2)
        body += lt; stick += lt
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
    grid_h = y + 2
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
        if x + w > (min(Wd, NARROW_FRAME - 20) if narrow is not None else Wd) - 8:   # C1 re-check: the narrow drawing's scale fits a 320 px frame
            x, y = 8, y + 30
        body += _g(f'<rect class="viz-t{tone} viz-h{i + 1}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="24"/>' + _text([txt], role, x + w / 2, y + 5.5, 'middle'))
        x += w + 4
    y += 24
    if narrow is not None:
        return _r(Wd), _r(y + 8), body, (8 + LW, stick, grid_h)
    nar = None
    if Wd > NARROW_FRAME:   # C1: as matrix()
        nw, nh, nb, nst = _heat(d, narrow=NARROW_LW)
        nar = (nw, nh, nb, nst if nw > NARROW_FRAME else None)
    return _svg(_r(Wd), _r(y + 8), body, 'matrix viz-numeric', d.get('title'), d.get('caption'), wide=wide,
                stick=(8 + LW, stick, grid_h) if Wd > NARROW_FRAME else None, narrow=nar)   # C1: a column wherever a 320 px frame scrolls


# P92 (4 Nov 2026) · the Academy home's topography: contour lines drawn from the course data (the module docstring, "The
# home kind"). Pure Python, so the build needs nothing installed: a sum of smooth bumps sampled on a grid, its contour
# lines found by marching squares, each line simplified (Ramer-Douglas-Peucker) and written with whole-unit relative
# path steps, each stretch of a line in the tone of the rise that dominates it.
CT_RIPPLE = (.16, .09)
SEP_FLAT = 8    # P94 checks 2 and 3: a separator's closed ring under 8 units across either way (2.4 px at 390 px, its two strokes merging into one bar) is a dash, not a ring, and is dropped; the test is on the whole contour line, before it is shared out among the rises
SEP_SPOT = 5    # P94 check 4: a separator's spot ring is at least 5 units in radius (10 across, 3 px at 390 px), a ring rather than a speck
SEP_SPECK = 6   # P94 check: a separator's closed ring under 6 units both ways (about 1.5 px on a 320 px phone) is a speck and is dropped   # the bump's outline: two angular harmonics, so a rise reads as land, not a target; its peak is unchanged


def _ct_bump(r, cx, cy, sx, sy, salt=''):
    """One rise as a function of (x, y): its words at its centre, falling off as a Gaussian whose outline is pushed in
    and out by two harmonics of the angle, their phases from the rise's label (the same drawing on every build), after
    the block's seed where it has one (P94: a section separator's rises are labelled by their place, the seed is the
    section, so each separator's outlines are its own)."""
    seed = zlib.crc32((str(salt) + str(r.get('label', ''))).encode())
    p1, p2 = (seed % 628) / 100, ((seed // 628) % 628) / 100
    h, (a1, a2) = float(r['words']), CT_RIPPLE
    def f(x, y):
        dx, dy = (x - cx) / sx, (y - cy) / sy
        q = dx * dx + dy * dy
        if q > 40:
            return 0.0
        t = math.atan2(dy, dx)
        m = 1 + a1 * math.sin(2 * t + p1) + a2 * math.sin(3 * t + p2)
        return h * math.exp(-q / (2 * m * m))
    return f


def _ct_march(F, nx, ny, g, L):
    """Marching squares at level L over F[j][i] (the point (i*g, j*g)): the contour as polylines [(points, closed)].
    Points sit on grid edges, interpolated linearly; a saddle is resolved by the cell's mean; segments are joined by
    the grid edge they share, so each line is continuous."""
    def ip(ax, ay, bx, by, va, vb):
        t = (L - va) / (vb - va) if vb != va else .5
        return (ax + (bx - ax) * t, ay + (by - ay) * t)
    PAIRS = {1: (('l', 't'),), 2: (('t', 'r'),), 3: (('l', 'r'),), 4: (('r', 'b'),), 6: (('t', 'b'),), 7: (('l', 'b'),),
             8: (('b', 'l'),), 9: (('b', 't'),), 11: (('b', 'r'),), 12: (('r', 'l'),), 13: (('r', 't'),), 14: (('t', 'l'),)}
    adj, pts = {}, {}
    for j in range(ny - 1):
        r0, r1 = F[j], F[j + 1]
        for i in range(nx - 1):
            v0, v1, v2, v3 = r0[i], r0[i + 1], r1[i + 1], r1[i]          # top left, top right, bottom right, bottom left
            c = (v0 > L) | (v1 > L) << 1 | (v2 > L) << 2 | (v3 > L) << 3
            if c == 0 or c == 15:
                continue
            x0, y0, x1, y1 = i * g, j * g, (i + 1) * g, (j + 1) * g
            def e(k):
                if k == 't': key, p = ('h', i, j), (lambda: ip(x0, y0, x1, y0, v0, v1))
                elif k == 'r': key, p = ('v', i + 1, j), (lambda: ip(x1, y0, x1, y1, v1, v2))
                elif k == 'b': key, p = ('h', i, j + 1), (lambda: ip(x0, y1, x1, y1, v3, v2))
                else: key, p = ('v', i, j), (lambda: ip(x0, y0, x0, y1, v0, v3))
                if key not in pts:
                    pts[key] = p()
                return key
            if c in (5, 10):
                mid = (v0 + v1 + v2 + v3) / 4 > L
                pr = ((('l', 't'), ('r', 'b')) if not mid else (('l', 'b'), ('r', 't'))) if c == 5 else \
                     ((('t', 'r'), ('b', 'l')) if not mid else (('t', 'l'), ('b', 'r')))
            else:
                pr = PAIRS[c]
            for a, b in pr:
                ka, kb = e(a), e(b)
                adj.setdefault(ka, []).append(kb); adj.setdefault(kb, []).append(ka)
    seen, lines = set(), []
    def walk(start):
        line, cur, prev = [start], start, None
        seen.add(start)
        while True:
            nb = [k for k in adj[cur] if k != prev and k not in seen]
            if not nb:
                return line
            prev, cur = cur, nb[0]; seen.add(cur); line.append(cur)
    for k in adj:                                   # open lines first, from an end (they meet the drawing's edge)
        if len(adj[k]) == 1 and k not in seen:
            lines.append(([pts[x] for x in walk(k)], False))
    for k in adj:
        if k not in seen:
            lines.append(([pts[x] for x in walk(k)], True))
    return lines


def _ct_rdp(p, eps):
    if len(p) < 3:
        return p
    (ax, ay), (bx, by) = p[0], p[-1]
    dx, dy = bx - ax, by - ay
    n = math.hypot(dx, dy)
    best, k = -1.0, 0
    for i in range(1, len(p) - 1):
        x, y = p[i]
        dd = abs(dy * x - dx * y + bx * ay - by * ax) / n if n > 1e-9 else math.hypot(x - ax, y - ay)
        if dd > best:
            best, k = dd, i
    if best <= eps:
        return [p[0], p[-1]]
    return _ct_rdp(p[:k + 1], eps)[:-1] + _ct_rdp(p[k:], eps)


def _ct_simplify(p, closed, eps):
    if not closed:
        return _ct_rdp(p, eps)
    k = max(range(len(p)), key=lambda i: (p[i][0] - p[0][0]) ** 2 + (p[i][1] - p[0][1]) ** 2)   # a ring split at its far point
    return _ct_rdp(p[:k + 1], eps)[:-1] + _ct_rdp(p[k:] + [p[0]], eps)[:-1]


def _ct_d(runs):
    """Polylines as one path's d: an absolute move, then whole-unit relative steps (rounded on the absolute points,
    so no error builds up), z for a closed ring."""
    out = []
    for p, closed in runs:
        q = [(round(x), round(y)) for x, y in p]
        r = [q[0]] + [b for a, b in zip(q, q[1:]) if b != a]
        if len(r) < 2:
            continue
        out.append((f'M{r[0][0]} {r[0][1]}l' + ' '.join(f'{b[0] - a[0]} {b[1] - a[1]}' for a, b in zip(r, r[1:]))).replace(' -', '-') + ('z' if closed else ''))
    return ''.join(out)


def _ct_layout(d, K, lay, n):
    """Where each rise stands in a layout: its "at" list (fractions of the width and height, one per rise), or, without
    one, the rises in order along the width (6% kept clear at each side), evenly spaced, alternately a little above and below
    the middle."""
    at = lay.get('at')
    if at is None:
        return [(.06 + .88 * (k + .5) / n, .5 + (.14 if k % 2 else -.14)) for k in range(n)]   # 6% kept clear at each side
    if not isinstance(at, list) or len(at) != n or not all(isinstance(a, list) and len(a) == 2 and all(0 <= v <= 1 for v in a) for a in at):
        _fail(K, f'layout {lay.get("name")!r}: "at" must give one [x, y] (0 to 1) per rise, {n} of them')
    return at


def _ct_check(d):
    K = 'contours'
    rises, iv, lays = d.get('rises'), d.get('interval'), d.get('layouts')
    if not rises:
        _fail(K, 'rises must be a non-empty list of {"label", "words", "tone"}')
    if not lays:
        _fail(K, '"layouts" must list at least one {"name", "width", "height", "spread"}')
    for k, r in enumerate(rises):
        if not r.get('label'):
            _fail(K, f'rises[{k}]: no label')
        _tone(r, None, K)
        if not r.get('planned') and not (isinstance(r.get('words'), (int, float)) and r['words'] > 0):
            _fail(K, f'rises[{k}] ({r["label"]}): a written rise needs its words, more than 0')
    live = [k for k, r in enumerate(rises) if not r.get('planned')]
    if live and (not isinstance(iv, (int, float)) or iv <= 0):
        _fail(K, '"interval" (the words between two contour levels) must be a positive number')
    if not live and not d.get('patch'):
        _fail(K, 'no written rise: nothing to draw (only a patch may be all planned: a ghost tile)')
    return rises, iv, lays, live


def _ct_field(d, lay, rises, iv, live):
    """One layout's field and lines: (W, H, at, sp, per-rise runs, levels per rise, own closed rings per rise, box of
    each rise's own rings, whether a line reaches the layout's edge). P93: split out of contours() so build.py can size and place rises from these numbers."""
    K = 'contours'
    W, H, g = lay.get('width'), lay.get('height'), lay.get('grid', 5)
    if not all(isinstance(v, (int, float)) and v > 0 for v in (W, H, g, lay.get('spread'))):
        _fail(K, f'layout {lay.get("name")!r}: width, height, spread and grid must be positive numbers')
    at = _ct_layout(d, K, lay, len(rises))
    # P93 check: each written rise's peak stands on a grid node, so the sampled field there holds at least its words
    # (between nodes a rise barely over a level lost that level: What's new's 30 Oct, 14,178 words at 14,000 a level)
    at = [[round(a[0] * W / g) * g / W, round(a[1] * H / g) * g / H] if k in live else a for k, a in enumerate(at)]
    sp, eps = lay['spread'], lay.get('simplify', .6)
    per = {k: [] for k in live}
    lv_of, own, box = {}, {}, {}
    if not live:
        return W, H, at, sp, per, lv_of, own, box, False
    wmax = max(rises[k]['words'] for k in live)
    # a rise's spread grows with the cube root of its words (a bigger hill is wider), the same in x and y; P94: in x
    # times the layout's stretch, where it has one (a section separator's hills drawn out along its ridge)
    st = lay.get('stretch', 1)
    fs = {k: _ct_bump(rises[k], at[k][0] * W, at[k][1] * H, st * sp * W * (rises[k]['words'] / wmax) ** (1 / 3),
                      sp * W * (rises[k]['words'] / wmax) ** (1 / 3), d.get('seed', '')) for k in live}
    nx, ny = int(W // g) + 1, int(H // g) + 1
    # P94: each rise sampled only inside the window where its bump can be above 0 (q <= 40, so within sqrt(40) of its
    # spread of its peak); outside it _ct_bump returns 0.0 anyway, so the field is the same, node for node, and the
    # 1,900 section separators of the reading pages build in seconds, not minutes
    Cw, F = {}, [[0.0] * nx for _ in range(ny)]
    for k, f in fs.items():   # in the order of the rises, so each node's sum is the same sum as before, its zeros left out
        rad = 6.33 * sp * W * (rises[k]['words'] / wmax) ** (1 / 3) + g
        rx = 6.33 * st * sp * W * (rises[k]['words'] / wmax) ** (1 / 3) + g
        i0, i1 = max(0, int((at[k][0] * W - rx) // g)), min(nx - 1, int((at[k][0] * W + rx) // g) + 1)
        j0, j1 = max(0, int((at[k][1] * H - rad) // g)), min(ny - 1, int((at[k][1] * H + rad) // g) + 1)
        rows = [[f(i * g, j * g) for i in range(i0, i1 + 1)] for j in range(j0, j1 + 1)]
        Cw[k] = (i0, i1, j0, j1, rows)
        for j, row in zip(range(j0, j1 + 1), rows):
            Fj = F[j]
            for i, v in zip(range(i0, i1 + 1), row):
                Fj[i] += v
    def val(k, i, j):
        i0, i1, j0, j1, rows = Cw[k]
        return rows[j - j0][i - i0] if (j0 <= j <= j1 and i0 <= i <= i1) else 0.0
    top = max(max(row) for row in F)
    edge = max(F[0] + F[-1] + [r[0] for r in F] + [r[-1] for r in F]) >= iv   # P93: a contour reaches the layout's edge
    def dom(p):
        i, j = min(nx - 1, max(0, round(p[0] / g))), min(ny - 1, max(0, round(p[1] / g)))
        return max(live, key=lambda k: val(k, i, j))
    for lv in range(1, int(top // iv) + 1):
        for p, closed in _ct_march(F, nx, ny, g, lv * iv):
            p = _ct_simplify(p, closed, eps)
            if len(p) < 2:
                continue
            if closed and d.get('sep'):   # P94 check: a separator drops a ring smaller than a speck (M792 80l-1 0z) or flat as a dash (M344 88l32 0z)
                rw, rh = max(x for x, _ in p) - min(x for x, _ in p), max(y for _, y in p) - min(y for _, y in p)
                if (rw < SEP_SPECK and rh < SEP_SPECK) or min(rw, rh) < SEP_FLAT:
                    continue
            ds = [dom(x) for x in p]
            if len(set(ds)) == 1:
                per[ds[0]].append((p, closed)); continue
            seq, dd = (p + [p[0]], ds + [ds[0]]) if closed else (p, ds)
            run, who = [seq[0]], dd[0]
            for x, w in zip(seq[1:], dd[1:]):   # a stretch per dominating rise; neighbours share their boundary point
                run.append(x)
                if w != who:
                    per[who].append((run, False)); run, who = [x], w
            per[who].append((run, False))
    for k in live:
        lv_of[k] = int(rises[k]['words'] // iv)   # P93 check: its own height in levels, one count for every layout (with the field at its peak Rome's U11, 4.996 levels, read 4 in one layout and 5 in the other)
        rings = [p for p, closed in per[k] if closed]
        own[k] = len([1 for p in rings if len({(round(x), round(y)) for x, y in p}) >= 2])
        if _ct_spotted(d, lv_of[k], own[k]):   # P93 check: a part under one level is marked by a spot ring at its peak (spot_r), its box that ring's; P94 check: in a separator, any rise with no ring of its own (one under a level its neighbours have not ringed, or one whose rings merged into its neighbours' lines)
            sr = _ct_spot_r(rises[k], sp, W, wmax, d.get('sep'))
            rings = [[(at[k][0] * W - sr, at[k][1] * H - sr), (at[k][0] * W + sr, at[k][1] * H + sr)]]
        xs = [x for p in rings for x, _ in p] or [at[k][0] * W]
        ys = [y for p in rings for _, y in p] or [at[k][1] * H]
        box[k] = (min(xs), min(ys), max(xs), max(ys))
    return W, H, at, sp, per, lv_of, own, box, edge


def _ct_spotted(d, lv, own):
    """Whether a written rise is marked by a spot ring: in a tile's patch or a hero, when it stands under one level (P93);
    in a section separator (P94 checks), whenever it closes no ring of its own, so every paragraph shows."""
    return own == 0 if d.get('sep') else lv == 0


def _ct_spot_r(r, sp, W, wmax, sep=False):
    """P93 check: the radius of the spot ring that marks a written rise standing under one level (its words below the
    interval, so no contour passes round it): half its spread, at least 3 units; as a map marks a spot height."""
    return max(SEP_SPOT if sep else 3.0, .5 * sp * W * (r['words'] / wmax) ** (1 / 3))


def contours_rings(d):
    """P93: for each layout, each written rise's (label, levels its peak stands above, own closed rings, box of its own
    rings in the layout's units), so a declaration can be checked before it is drawn (build.py sizes and places the
    course homes' and What's new's rises with it: every written rise closing min(2, levels) rings of its own; and a
    tile's patch, its lines clear of the frame); and under the key (name, 'edge') whether any line reaches the edge."""
    rises, iv, lays, live = _ct_check(d)
    out = {}
    for lay in lays:
        W, H, at, sp, per, lv_of, own, box, edge = _ct_field(d, lay, rises, iv, live)
        out[lay.get('name')] = [(rises[k]['label'], lv_of[k], own[k], box[k]) for k in live]
        out[(lay.get('name'), 'edge')] = edge
        xy = [pt for k in live for run, _ in per[k] for pt in run]
        out[(lay.get('name'), 'extent')] = (min(x for x, _ in xy), min(y for _, y in xy), max(x for x, _ in xy), max(y for _, y in xy)) if xy else None   # P93: every line's box
    return out


def contours(d):
    """The topography (the module docstring, "The home kind"): one rise per entry of "rises", its height its words, in
    every layout; returns the layer's HTML. A written rise is a <g class="ct-rise ct-t{tone}"> holding every stretch of
    contour line it dominates, with data-label, data-words, data-rings (the contour levels its own words stand above,
    the same in every layout; P93),
    data-at (its peak, in the layout's units) and data-box (the box of its own closed rings, P93: verify.py maps both
    to the screen to check every rise in view); a planned one ("planned": true) a dashed ring, <g class="ct-plan">, flat
    (no height, in no line). P93: a patch may be all planned (a planned course's ghost tile, a planned unit), its rings
    only; a patch's layout is fitted whole inside its frame (meet), so the frame's overscan for the turn never crops a
    rise, where the hero's layouts cover theirs (slice). P94: with "sep" the patch is a section separator (the layer
    .topo.topo-patch.topo-sep; its rises carry no data-at or data-box, which only a hero's checks read, so it keeps to
    6 KB); "seed" salts every rise's outline (a separator labels its rises by place, ¶1, ¶2 ..., and is seeded by its
    section); a layout's "stretch" draws each hill out along x by that factor (a separator's hills meet in one ridge)."""
    rises, iv, lays, live = _ct_check(d)
    svgs = []
    for lay in lays:
        W, H, at, sp, per, lv_of, own, box, edge = _ct_field(d, lay, rises, iv, live)
        body = ''
        for k, r in enumerate(rises):
            t = r.get('tone')
            tc = f' ct-t{t}' if t else ''
            if r.get('planned'):
                rr = max(2.0, min(sp * W * .55, .22 * min(W, H)))   # P93: a lone planned ring (spread over one rise) stays inside a 4:1 patch
                body += (f'<g class="ct-plan{tc}" data-label="{esc(r["label"])}" data-at="{at[k][0] * W:.0f} {at[k][1] * H:.0f}"><circle cx="{at[k][0] * W:.0f}" cy="{at[k][1] * H:.0f}" '
                         f'r="{rr:.0f}"/></g>')
                continue
            bx = ' '.join(f'{v:.0f}' for v in box[k])
            spot = (f'<circle class="ct-spot" cx="{at[k][0] * W:.0f}" cy="{at[k][1] * H:.0f}" r="{_ct_spot_r(r, sp, W, max(rises[j]["words"] for j in live), d.get('sep')):.0f}"/>'
                    if _ct_spotted(d, lv_of[k], own[k]) else '')   # P93 check: a written part under one level still shows, as a spot ring
            where = '' if d.get('sep') else f' data-at="{at[k][0] * W:.0f} {at[k][1] * H:.0f}" data-box="{bx}"'   # P94: a separator keeps to 6 KB; its place and box serve no check
            dd = _ct_d(per[k])
            path = '' if (d.get('sep') and not dd) else f'<path d="{dd}"/>'   # P94 check 3: a separator's spot-only rise carries no empty path
            body += (f'<g class="ct-rise{tc}" data-label="{esc(r["label"])}" data-words="{round(r["words"])}" data-rings="{lv_of[k]}"'
                     f'{where}>{path}{spot}</g>')
        nm = esc(lay.get('name', ''))
        fit = 'meet' if d.get('patch') else 'slice'
        svgs.append(f'<svg class="topo-l topo-{nm}" data-layout="{nm}" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid {fit}" '
                    f'xmlns="http://www.w3.org/2000/svg" focusable="false">{body}</svg>')
    cls = 'topo' + (' topo-patch' if d.get('patch') else '') + (' topo-sep' if d.get('sep') else '')   # P94: a section separator is a patch drawn across the column
    ph = d.get('phase')
    st = f' style="--ph:{ph:g}"' if isinstance(ph, (int, float)) else ''
    return f'<div class="{cls}" aria-hidden="true"{st}>{"".join(svgs)}</div>'


# P95 (8 Nov 2026; Pedro, 5 Nov 2026: "we can even fetch svg outlines of things ... and then use the topographical
# method and animation to illustrate the articles") · the object relief: an outline from the library (design/outlines/,
# each a sourced file with its credit in outlines.json) drawn as the lines of a relief map of its own silhouette, the
# outline and the levels inside it solid (path.rl-in), two faint halo levels outside it (path.rl-out), in the page's tone.
# kit/relief.py computes the lines once, when an outline is added (the silhouette's distance field, contoured at even
# steps), and writes <id>.json; this draws that JSON, so the build stays pure Python. The frame is the drawing's box
# grown so that, turned to either end of the turn at the top of the breath about its centre (the move every contour
# drawing makes, read from the theme), every line stays REL_PAD units clear of it; its aspect goes to the page as --ar.
_THEME = (pathlib.Path(__file__).resolve().parent.parent / 'design' / 'theme.css').read_text()
REL_TURN = float(re.search(r'--topo-turn:([\d.]+)deg', _THEME).group(1))
REL_GROW = float(re.search(r'--topo-grow:([\d.]+);', _THEME).group(1))
REL_PAD = 14        # units of the 1000-unit drawing kept clear of the frame at every pose (about 4 px at 280 px tall)
REL_MAX = 12 * 1024  # bytes, as the page holds the element (the parser writes <path ...></path>)
REL_SPECK = 8       # a closed ring under this many units both ways (about 2 px at 280 px) is a speck, dropped


def rel_bytes(h):
    """A drawing's size as the page holds it: the HTML parser writes a self-closed SVG element with an end tag."""
    return len(re.sub(r'<(\w+)([^<>]*?)/>', r'<\1\2></\1>', h).encode())


def rel_frame(w, h):
    """The frame (W, H) round a w by h drawing, so that the drawing turned by +/- REL_TURN and grown to REL_GROW about
    its centre stays REL_PAD units inside it."""
    a = math.radians(REL_TURN)
    c, s = math.cos(a), math.sin(a)
    return round(REL_GROW * (w * c + h * s) + 2 * REL_PAD), round(REL_GROW * (w * s + h * c) + 2 * REL_PAD)


def relief(d):
    """The relief layer: div.topo.relief (aria-hidden, textless) holding one svg.topo-l in the tone's class, its lines in
    two paths, rl-out (the halo) and rl-in (the outline and the levels inside it); --ph its phase, --ar the frame's
    aspect. The lines are simplified further (viz's RDP) until the element is at most REL_MAX bytes as the page holds
    it. The caption is the page's, outside the drawing (mdcourse.reading)."""
    o = d['outline']
    w, h, lines = o['width'], o['height'], o['lines']
    if not lines or not all(isinstance(v, (int, float)) and v > 0 for v in (w, h)):
        _fail('relief', f'outline {o.get("id")!r}: no lines or no size')
    W, H = rel_frame(w, h)
    ox, oy = (W - w) / 2, (H - h) / 2
    t = d.get('tone')
    tc = f' ct-t{t}' if t else ''
    ph = d.get('phase')
    st = f' style="--ph:{ph:g};--ar:{W / H:.4f}"' if isinstance(ph, (int, float)) else f' style="--ar:{W / H:.4f}"'
    eps = 0
    while True:
        runs = {'out': [], 'in': []}
        for ln in lines:
            p = [(x + ox, y + oy) for x, y in ln['pts']]
            if eps:
                p = _ct_simplify(p, ln['closed'], eps)
            if len(p) < (3 if ln['closed'] else 2):
                continue
            if ln['closed']:
                xs, ys = [x for x, _ in p], [y for _, y in p]
                if max(xs) - min(xs) < REL_SPECK and max(ys) - min(ys) < REL_SPECK:
                    continue
            runs['out' if ln['lv'] < 0 else 'in'].append((p, ln['closed']))
        body = ''.join(f'<path class="rl-{k}" d="{_ct_d(runs[k])}"/>' for k in ('out', 'in') if runs[k])
        out = (f'<div class="topo relief" aria-hidden="true" data-outline="{esc(o.get("id", ""))}"{st}><svg class="topo-l{tc}" viewBox="0 0 {W} {H}" '
               f'preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" focusable="false">{body}</svg></div>')
        if rel_bytes(out) <= REL_MAX:
            return out
        eps = 1.5 if not eps else eps * 1.3
        if eps > 40:
            _fail('relief', f'outline {o.get("id")!r} stays over {REL_MAX} bytes even simplified')


KINDS = {'timeline': timeline, 'compare': compare, 'tree': tree, 'flow': flow,
         'sitemap': sitemap, 'objects': objects, 'decision': decision, 'matrix': matrix,
         'states': states, 'swimlanes': swimlanes, 'wireflow': wireflow,
         'line': line, 'bars': bars, 'scatter': scatter, 'range': range_}
# P92: the home kind, the topography (P91's shelf is gone), not on the Figure kinds page (viz_examples.py shows one
# example of every kind in KINDS)
HOME_KINDS = {'contours': contours, 'relief': relief}   # P95: the object relief, on a reading page under its scope line


_LISTS = {'rises', 'layouts', 'at', 'events', 'spans', 'ticks', 'rows', 'steps', 'objects', 'attrs', 'actions', 'lines', 'cols', 'cells', 'series',
          'points', 'states', 'transitions', 'screens', 'links', 'lanes', 'children', 'branches', 'legend', 'values',
          'annotations', 'yticks', 'xticks', 'names'}


def _lists(o, kind, path='figure'):
    """P55: a field that holds a list given a bare string instead was drawn one letter per line (an object's attrs);
    any such field anywhere in the figure stops the build and says which."""
    if isinstance(o, dict):
        for k, v in o.items():
            if k in _LISTS and isinstance(v, str):
                _fail(kind, f'{path}.{k} must be a list, e.g. ["{v[:20]}"], not the string {v[:40]!r}')
            _lists(v, kind, f'{path}.{k}')
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _lists(v, kind, f'{path}[{i}]')


# P52 (1 Nov 2026): the documented keys of every kind, at every level of a block. A block is data a writer declares;
# the renderer works on a copy (render's deepcopy), so its working keys (_t, _h, ...) never reach a unit, and verify.py
# (check_viz_keys) reads every ```viz block and every history figure declaration against this table. A key in a block
# that is not here is either undocumented or a typo: either way the figure does not draw what the block says.
# Each kind maps a node's name to its keys; a key whose value is an object or a list of objects names the node it holds
# in NODE_OF (per kind, falling back to the key itself), and the top level is ".".
COMMON = {'kind', 'caption', 'title'}
_TREE = {'label', 'tone', 'children'}
VIZ_KEYS = {
    'timeline': {'.': {'start', 'end', 'ticks', 'events', 'spans', 'era'},
                 'events': {'at', 'label', 'date', 'tone'}, 'spans': {'from', 'to', 'label', 'date', 'tone'}},
    'compare': {'.': {'unit', 'max', 'decimals', 'rows'}, 'rows': {'label', 'value', 'display', 'tone'}},
    'tree': {'.': {'root'}, 'root': _TREE, 'children': _TREE},
    'flow': {'.': {'steps', 'per_row'}, 'steps': {'label', 'note', 'tone'}},
    'sitemap': {'.': {'root', 'stack_from', 'phone'}, 'phone': {'stack_from'},
                'root': {'label', 'type', 'note', 'tone', 'children', 'href', 'dashed'},
                'children': {'label', 'type', 'note', 'tone', 'children', 'href', 'dashed'}},
    'objects': {'.': {'objects', 'rows', 'links'}, 'objects': {'id', 'title', 'attrs', 'actions', 'tone'},
                'links': {'from', 'to', 'label', 'from_card', 'to_card', 'dir'}},
    'decision': {'.': {'root'}, 'root': {'q', 'outcome', 'tone', 'branches'}, 'branches': {'label', 'to'},
                 'to': {'q', 'outcome', 'tone', 'branches'}},
    'matrix': {'.': {'cols', 'rows', 'legend', 'numeric', 'tone', 'min', 'max', 'decimals', 'unit', 'scale_label'},
               'rows': {'label', 'tone', 'cells'}, 'cells': {'mark', 'tone'}, 'legend': {'mark', 'means', 'tone'}},
    'states': {'.': {'states', 'transitions', 'per_row', 'start'}, 'states': {'id', 'label', 'note', 'tone', 'end'},
               'transitions': {'from', 'to', 'label'}},
    'swimlanes': {'.': {'lanes', 'steps', 'links'}, 'lanes': {'id', 'label', 'tone'},
                  'steps': {'id', 'lane', 'col', 'label', 'note', 'tone'}, 'links': {'from', 'to', 'label'}},
    'wireflow': {'.': {'screens', 'links', 'per_row'}, 'screens': {'id', 'title', 'tone', 'lines'},
                 'lines': {'bar', 'block', 'button'}, 'links': {'from', 'to', 'label'}},
    'line': {'.': {'x', 'years', 'era', 'unit', 'series', 'annotations', 'labels', 'min', 'max', 'yticks', 'xticks',
                   'decimals', 'height', 'xlabel', 'ylabel'},
             'series': {'name', 'values', 'tone'}, 'annotations': {'at', 'label'}},
    'bars': {'.': {'mode', 'unit', 'series', 'rows', 'max', 'decimals'}, 'series': {'name', 'tone'},
             'rows': {'label', 'values'}},
    'scatter': {'.': {'x', 'y', 'points', 'quadrants', 'height'},
                'axis': {'label', 'min', 'max', 'ticks', 'unit', 'decimals', 'years'},
                'points': {'label', 'x', 'y', 'tone'}, 'quadrants': {'x', 'y', 'names'}},
    'range': {'.': {'unit', 'unit_one', 'years', 'era', 'min', 'max', 'ticks', 'decimals', 'xlabel', 'rows'},
              'rows': {'label', 'low', 'high', 'point', 'low_src', 'high_src', 'tone'}},
    # P92: the home's topography (HOME_KINDS), the hero's and each course tile's
    'contours': {'.': {'interval', 'rises', 'layouts', 'patch', 'phase', 'sep', 'seed'}, 'rises': {'label', 'words', 'tone', 'planned'},
                 'layouts': {'name', 'width', 'height', 'spread', 'grid', 'simplify', 'at', 'stretch'}},
    # P95: the object relief (HOME_KINDS): an outline's JSON from design/outlines/ (kit/relief.py), the page's tone, its phase
    'relief': {'.': {'outline', 'tone', 'phase'}},
}
NODE_OF = {'scatter': {('.', 'x'): 'axis', ('.', 'y'): 'axis'}}


def check_keys(d, kind=None):
    """P52: every key in a figure block that the table above does not document, as messages (empty when none)."""
    kind = kind or (d.get('kind') if isinstance(d, dict) else None)
    if kind not in VIZ_KEYS:
        return [f'unknown kind {kind!r}']
    spec, bad = VIZ_KEYS[kind], []

    def walk(o, node, path):
        if isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, node, f'{path}[{i}]')
            return
        if not isinstance(o, dict):
            return
        allowed = spec[node] | (COMMON if node == '.' else set())
        for k, v in o.items():
            if k not in allowed:
                bad.append(f'{path}.{k}: not a documented key of {kind}' + (f' {node}' if node != '.' else ''))
                continue
            sub = NODE_OF.get(kind, {}).get((node, k), k)
            if sub in spec and (isinstance(v, dict) or (isinstance(v, list) and any(isinstance(x, (dict, list)) for x in v))):
                walk(v, sub, f'{path}.{k}')
    walk(d, '.', 'figure')
    return bad


def render(d):
    """One figure object to HTML. A kind not in KINDS, or bad data, is an error: a figure that cannot draw is a bug, not a blank.
    P52: it draws a deep copy, so the renderer's working keys never reach the block it was given (a unit, a course entry)."""
    d = copy.deepcopy(d)
    try:
        _lists(d, d.get('kind'))
        return (HOME_KINDS.get(d['kind']) or KINDS[d['kind']])(d)
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
