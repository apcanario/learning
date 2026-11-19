"""Browser checks for academy/, the Academy site (run after build.py).

python3 verify.py [--edition NAME] [--shots DIR] [--page ID ...]
The site is a shell plus one file per report (docs/academy.md A2), since P20 one file per syllabus and per Brand + AI
briefs and bibliography page, and since P22 one file per history course home, so it is served over local HTTP from
academy/, as the artifact and Pages serve it, and every pass that measures a fetched panel first navigates to it
through the shell and waits for the fetch. The split itself is checked: every report, syllabus, briefs, bibliography
and history course home panel is an empty stub whose data-src file exists, no file in academy/ is left unreferenced,
a report is fetched once and kept, a section link into an unopened report, syllabus, briefs page or course home
(a unit card) loads it, a failed fetch shows the retry state (a report and a course home, whose continue button and
unit cards arrive with the fetch), the shell is under 1 MB and the size table in README.md matches the files.
Three widths (design/theme.css section 6): phone 390x844, tablet 768x1024, desktop 1280x800. On every panel of every
width, with every <details> opened: no horizontal scroll, no boxed elements closer than 6 px, no interactive target
under 44 px tall (inline links in running text exempt), no console error. Phone: the drawer in each context and the
navigation context (drawer, title, arrows, continue) across home -> Rome -> report -> home -> Greece -> report ->
a Brand + AI course and its reading and build pages, every course's "How it was built" page (A4: fetched through the
shell, one row per written report or unit), the drawer groups (tracks open by default, a course's units as an
accordion) and the Backlog page; the same panel checks again in the light theme. The Backlog and Changelog pages
(S-PAGES, 15 Nov 2026; check_site_log): rendered from docs/site-log.md alone, every entry in its area and order, newest
first on the Changelog, in plain words with no private term, at 320, 390 and 1280 px, dark and light, without sideways scroll. Tablet: the drawer is still a drawer (off screen until the menu button, 360 px, backdrop).
Desktop: the drawer is a persistent 300 px sidebar (no backdrop, no menu button, current item highlighted, scrolls on
its own) and the top bar spans the content column. Figures (P44): at phone width every figure draws at its natural size
and its frame scrolls to the whole drawing; the cue line shows exactly on the frames that overflow (phone and desktop). With --shots, saves dark and light screenshots (the top 2,600 px, captured from a viewport that tall, P35; the home whole, P90; P92: and the hero's motion sheets, five moments of the area line and the drift, at 390 and 1280 px) at the three widths
of home, What's new (P91; the home and What's new at 320, 360 and 430 px too), Rome and one Rome report, plus every panel id given with --page (a new unit's reading page, a new course home),
and (P41) each figure in a --page panel on its own: <width>-<panel>-fig-<nn>-<kind>-<theme>.png, the figure as its frame
opens; and (P89, p85_frames.py folded in) every frame a reader scrolls that figure across, stacked and numbered in one
sheet: <width>-<panel>-fig-<nn>-<kind>-frames-<theme>.png, at each width, dark and light.
Matrix figures at 320 px (C1, 15 Nov 2026): every matrix that scrolls a 320 px frame keeps a label column in view, at
most 45% of the frame, sticky at its edge and as tall as the drawing (check_matrix_320).
Compare figures on a phone (P97, 12 Nov 2026): every compare figure at 320 and 390 px opens with its longest bar and
its value whole in the frame (its phone drawing, svg.viz-alt).
Figure geometry (FIG_JS; V1, every kind since P55): on the examples page (one figure per kind, then one hard case per
drawing fault P55 fixed, and the blocks that must stop the build) and, in the phone pass, on every panel with figures:
nothing outside the drawing, text inside its box or bar, no two boxes or labels overlapping, no free label over a box.
Links into an unopened panel on a fresh load are measured once the anchor has settled, with one retry (P56).
Reading layout (P68): every unit and report opens on its scope, then the bar and the text, with nothing about how it
was made before the text; each reads one section at a time, every section reached by next, previous and the menu, with
"Section n of N" and the progress bar right at each step; "Whole unit" shows them all; Sources and "How this unit was
made" are closed accordions after the text, and Sources opens from its links; on one page of each course a deep link
to a section and to Sources lands on a fresh load, and Continue and a reload resume at the section last read. The
panel checks measure each reading page whole.
Opening trees (P79): every tree wider than its 358-unit phone frame opens (at data-x0 or data-xr, as shell.js does)
with its root box whole and a box of a lower level in view.
Centred drawings (P50): every sitemap, objects, decision, states and wireflow figure whose drawing starts more than 12 units
in carries data-x0 where it starts, so a phone frame opens on it.
Figure keys (P52): every viz block in the vault, every history figure declaration, every course home figure and every
examples block uses only the keys viz.VIZ_KEYS documents for its kind, and viz.render leaves the block it draws unchanged.
Opening notes (P73): a markdown unit's text before its first heading is a closed accordion after Sources, "The writer's
opening note", on every unit that has one and on none that has not; section 1 opens on its heading; a deep link lands.
Home (P92, 4 Nov 2026; P91's shelf, P90's map and Continue gone), at 320, 360, 390, 430, 768 and 1280 px, dark and
light, with reduced motion emulated, and once more at every width with motion allowed: the hero holds the contour
layer and the copy, nothing else: the headline "Academy"; the area line, the four areas in courses.py's order, each in
its tone, aria-hidden, no link or focus stop in it; the static line naming all four in their tones, for a screen
reader, and the line shown under reduced motion (with motion allowed the cycling line shows and the static line is for
a screen reader only); the lede; the quiet link "What's new · <code> · <day>" naming the newest dated unit, to #new, at
least 44 px tall, outlined, not filled. The contour layer: aria-hidden, no text, at most 20 KB, one layout shown (tall
below 1100 px, wide from it), running the full width beside the sidebar while the copy keeps the column; in each layout
one rise per area, its words the area's words as the sources give them (home_expect: a history unit's reports counted
from the vault, a markdown unit from its reading page), standing in the order of its words, in the area's tone. On a
phone the hero is 60 to 80% of the screen and the first area's heading starts inside it; no live totals, no shelf, no
Continue, no map, no eyebrow; the area headers from 768 px the label, the name, the lede and the count, below it the
name only; every tile the chip row with its pill, the title, a tile line of at most two lines, three stats and its own
contour patch (aria-hidden, 4:1, inside the tile; one rise per written unit with its words as the sources give them,
each planned unit marked planned), the whole tile the link and no other link in it; one tile style (P93: History's
planned courses are ghost tiles, checked with every tile by check_tiles); one column below
768 px, two from 768, a track's only tile half the width; History's two folded blocks; the order hero, the area
sections, the constants, the site links (Backlog, Figure kinds, Changelog), New since (What's new's first six rows, its
heading naming its oldest day) and one link to #new, last; no sideways scroll. Every text of the hero is measured
against the pixels under it (the contour lines and the page, shot with the texts made transparent): 4.5:1, 3:1 for
large text. With motion allowed the hero's texts are measured at the five poses of the move (P93; P92's drift, at both
ends and the middle, is gone) with each area word shown in turn. With
reduced motion no animation runs on the home; with motion allowed only transform and opacity animate
(document.getAnimations(), each effect's keyframes), the four area words, the shown contour layout and (P93) every shown
tile's patch.
At 390 px with motion allowed the fresh load's LCP and longest task are printed. On the desktop a history tile, a
markdown tile, the IA tile and the What's new link are clicked and each lands on its page. What's new (P91), at the
same widths: every dated unit and every course start once, newest first, as home_expect orders them, grouped by day
under its heading, each row linking to a page that exists, the approximate dates (provenance.json's written_approx)
marked and no other; its breadcrumbs and title. The root drawer's top rows: Home, What's new, Changelog, Backlog.
Contrast (P90): in the light theme, every text in the home, What's new (P91), the drawer, the changelog and backlog, each course
home and one reading page of each course, at phone width with every <details> open, reaches 4.5:1 against the
background it sits on (3:1 for large text), the text's opacity and every tint it sits on composited, and no text
and no background under it is pure white; figures are left to the figure checks.
Topographies and tiles (P93, 4 Nov 2026), at 320, 360, 390, 430, 768 and 1280 px, dark and light: each course home and
What's new carries a contour layer behind its hero (check_topo), against the sources (home_expect: a course home one
rise per unit of the course in its order, a written unit by its words, a planned unit flat; What's new one rise per
day it lists, oldest first, its words the units' and reports' filed that day, the largest day 10 to 25 levels high),
aria-hidden, textless, at most 20 KB, one layout shown, each written rise closing min(2, its levels) rings of its own,
each rise's own rings inside the frame and above its fade, the frame covered by the turned layout; every tile patch
4:1 with its lines inside its frame; no topography on the Changelog, the Backlog, the Figure kinds page or a reading
page. Every tile on every page (check_tiles) has the same classes and fields (the chip of two parts, the status pill,
the title, a line of at most two lines while closed and whole when opened, three stats, its own patch; a planned
course's ghost no stats and one dashed ring), a history unit's tile opens to its module rows with its modules, words
and hours from the vault, a markdown unit's links to its reading page (its brief while it is not written) with its
sections and words from that page, each section's own text counted; one column below 768 px, two from it, a lone tile
half the width; nothing past an edge, no sideways scroll. With motion allowed, on every one of these pages and the
home, every running animation animates only transform or opacity, every shown contour drawing moves (the theme's
topo-turn: a turn of --topo-turn each way and a growth to --topo-grow over --topo-cycle, read from shell.css), each at
its own point of the cycle, and at five poses of the sweep (its two ends, its quarters and its middle; on the home with
each area word shown in turn) every layer covers its frame, every rise and patch stays inside it and every text over
a topography keeps 4.5:1 (3:1 large) against the pixels under it; under reduced motion no animation runs on any of
them. At 390 px with motion allowed, LCP and the longest task are printed for the home, Greece's home and What's new.
With --shots: the home, What's new and the five course homes at the six widths, and the motion sheets of the home,
Greece and Information architecture at the five poses, 390 and 1280 px.
Section separators (P94, 8 Nov 2026), on every reading page at 320, 390, 768 and 1280 px, dark and light, under reduced
motion and with motion allowed (check_seps): every section with a top-level paragraph ends on one separator, last before
its next and previous, and a section without one has none; its rises, one per paragraph in order, carry the words read
from the page (the cue shell.js puts under a wide figure left out); div.topo.topo-patch.topo-sep, aria-hidden, textless,
at most 6 KB, its lines in the page's tone, its frame 1200:170 and the column's width, 20 px clear at least of the text
above and of the next and previous below (in "Whole unit", of the next section); with motion allowed a turn and a
breath on each, transform only, each at its own phase, and at five poses of the turn at the top of the breath every
line inside its frame; none moving under reduced motion; no page wider than the screen. The other topography checks
leave the separators to this one.
Object reliefs (P95, 8 Nov 2026; check_reliefs): the outline library (design/outlines/outlines.json) holds at least ten
outlines for each of the five courses, each with every field, an allowed licence named in its credit, its SVG and its
relief JSON, and a text of each course it serves naming it; every reading page maps a relief exactly when uses.json
maps it one; and each mapped page at 320, 390, 768 and 1280 px, dark and light, with and without motion: the relief under
the scope line as the header's last block, before the section bar; its caption printed exactly (what it shows, "a
stylised outline drawn as a relief from an icon", the credit) with the licence linked to its text; div.topo.relief
aria-hidden and textless, one svg.topo-l with only path.rl-in and path.rl-out (class and d), at most 12 KB, in the page's
tone, the halo fainter; its frame at the drawing's aspect, the column's width or 280 px tall (340 from 768 px); a turn
and a breath by transform only, at a phase none of the page's separators has, and at five poses of the turn at the top
of the breath every line inside its frame; nothing moving under reduced motion; the page's text naming the object; no
page wider than the screen.
Last, index_check.py: docs/courses-index.md against the syllabi, provenance, the vault and the data files (A5).
Then rot_check.py (P30-F11, P30-F16): kit/shell.css is design/theme.css, no live instruction names a retired thing, and
every staleness date past or due within 30 days is printed as a warning.
"""
import sys, json, pathlib, re, threading, functools, math, html as H
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
import index_check   # (P39: the browser gets the theme fonts from fonts/, never the network)
import private_terms   # G-0: the public courses carry no private term
import rot_check   # P30-F11, P30-F16: the theme copy, retired instructions, staleness dates due
from courses import COURSES, THEMES, EDITIONS, NEXT
# P70: --edition checks an edition's folder the same way, over the courses and pages it holds (default: the full Academy)
EDITION = sys.argv[sys.argv.index('--edition') + 1] if '--edition' in sys.argv else 'academy'
if EDITION not in EDITIONS:
    raise SystemExit(f'no edition {EDITION!r} in courses.py EDITIONS: {", ".join(EDITIONS)}')
ED = EDITIONS[EDITION]
OMIT = set(ED['omit'])
if ED['courses'] is not None:
    COURSES = [c for c in COURSES if c['id'] in ED['courses']]
    _tracks = {c.get('theme') for c in COURSES} | {tr for c in COURSES for tr, _ in c.get('tracks', {}).values()}
    THEMES = [t for t in THEMES if t['id'] in _tracks]
HAS = {c['id'] for c in COURSES}
ROME, BRAND = 'rome' in HAS, 'brand-ai' in HAS
import viz, viz_examples   # P55: the examples page's hard cases and the blocks that must stop the build
# each track and its course cards as the home must show them, from courses.py (A5: a new course needs no edit here)
# G-0 (12 Nov 2026): a markdown course with no unit filed is not live and has no tile on the home (home_expect says the
# same); a unit's file is named by its code, the course's key and a number (A9, DD-IA2, PB1)
def _live(c, k):
    v = pathlib.Path(__file__).resolve().parent.parent / c['vault']
    return any(v.glob(f'{k}[0-9]*.md')) or any(v.glob(f'DD-{k}[0-9]*.md'))
HOME_TRACKS = [t['name'] + ':' + ','.join(
    ['#' + c['home_id'] for c in COURSES if c['family'] == 'history' and c['theme'] == t['id']]
    + ['#' + f"{c.get('prefix', c['id'])}-{k.lower()}" for c in COURSES if c['family'] == 'markdown'
       for k, (tr, _) in c['tracks'].items() if tr == t['id'] and _live(c, k)]) for t in THEMES]

R = pathlib.Path(__file__).resolve().parent
SITE = R / ED['site']
SHELL_MAX = 1024 * 1024   # A2: the shell stays under 1 MB
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
class Server(ThreadingHTTPServer):
    def handle_error(self, request, client_address):   # a fetch the browser dropped on navigating away is not a fault
        if not isinstance(sys.exc_info()[1], (BrokenPipeError, ConnectionResetError)): super().handle_error(request, client_address)
SERVER = Server(('127.0.0.1', 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=SERVER.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{SERVER.server_port}/index.html'
# the visible panel holds its content: a panel in the shell at once, a report once its fetch has landed (or failed)
READY_JS = """() => { if (document.fonts.status !== 'loaded') return false; const p = [...document.querySelectorAll('.panel')].find(p => !p.hidden);
  return !!p && (!p.hasAttribute('data-src') || p.hasAttribute('data-loaded') || p.hasAttribute('data-failed')); }"""
def ready(pg):
    pg.wait_for_function(READY_JS, timeout=15000)
SHOTS = pathlib.Path(sys.argv[sys.argv.index('--shots') + 1]) if '--shots' in sys.argv else None
PAGES = [a for i, a in enumerate(sys.argv) if i > 0 and sys.argv[i - 1] == '--page']   # extra panels to screenshot
GAP = 6
VX_KINDS = 16  # the examples page carries one figure per kind: four from A8, seven for the IA course (V1), four data kinds
               # and the numeric matrix (P44)
VX_FIGS = VX_KINDS + len(viz_examples.CASES)   # then one hard case per drawing fault P55 fixed
VIEWPORTS = [('phone', 390, 844, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]
HOME_WIDTHS = [('phone320', 320, 640, True), ('phone360', 360, 780, True), ('phone430', 430, 932, True)]   # P91: the home only
# P91: where a tapped link landed (P92: a tile, the What's new link): [visible panel, its target inside it, the target's top, a <details> target open, the viewport height]
LAND_JS = '''(t) => { const v = [...document.querySelectorAll('.panel')].find(p => !p.hidden), e = document.getElementById(t);
  return [v && v.id, !!e && !!v && v.contains(e), e ? Math.round(e.getBoundingClientRect().top) : null, e && e.tagName === 'DETAILS' ? e.open : null, innerHeight]; }'''
SIDE = 300  # desktop sidebar width (theme.css --side)

BOX_JS = r'''([scope, gap]) => {
  const root = document.querySelector(scope);
  const els = [];
  root.querySelectorAll('*').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || cs.display === 'inline') return;  // inline code in running text is not a box
    const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return;
    const b = ['Top','Bottom','Left','Right'].every(s => parseFloat(cs['border'+s+'Width']) > 0 && cs['border'+s+'Style'] !== 'none');
    const bg = cs.backgroundColor, hasBg = bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent';
    if (b || (hasBg && parseFloat(cs.borderTopLeftRadius) > 0)) els.push([el, r]);
  });
  const bad = []; let min = 1e9;
  for (let i = 0; i < els.length; i++) for (let j = i + 1; j < els.length; j++) {
    const [a, ra] = els[i], [b, rb] = els[j];
    if (a.contains(b) || b.contains(a)) continue;
    const hov = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
    if (hov <= 1) continue;
    let g;
    if (ra.bottom <= rb.top + 0.5) g = rb.top - ra.bottom; else if (rb.bottom <= ra.top + 0.5) g = ra.top - rb.bottom; else g = -1;
    if (g < min) min = g;
    if (g < gap - 0.1) {
      const d = e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).join('.') : '') + (e.id ? '#' + e.id : '');
      bad.push(`${d(a)} | ${d(b)} gap ${g.toFixed(1)}`);
    }
  }
  return {n: els.length, min: Math.round(min * 10) / 10, bad: bad.slice(0, 12), nbad: bad.length};
}'''

# interactive targets under 44 px tall or 24 px wide, in the visible panel and in the drawer when it is on screen;
# inline links inside running text are exempt (WCAG 2.5.8 inline exception)
TARGET_JS = r'''(scope) => {
  const small = [];
  const dr = document.getElementById('drawer'), dOn = dr && dr.getBoundingClientRect().left >= 0;
  const roots = [document.querySelector(scope)]; if (dOn) roots.push(dr);
  roots.forEach(root => { if (!root) return; root.querySelectorAll('a[href],button,summary,input,select,[role=button]').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const r = el.getBoundingClientRect(); if (r.width === 0 && r.height === 0) return;
    if (el.tagName === 'A' && cs.display === 'inline') return;
    if (el.closest('.dunit.closed .ditems')) return;
    if (r.height < 43.5 || r.width < 24) small.push((el.tagName + '.' + el.className + ' "' + (el.textContent || '').trim().slice(0, 24) + '"').slice(0, 80) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
  }); });
  return [...new Set(small)].slice(0, 15);
}'''

# P44: at phone width every figure draws at its natural size (one SVG unit to one CSS pixel) inside its .viz-scroll
# frame; the frame's scroll reaches the whole drawing (scrolled to the end, the drawing's right edge is inside the frame);
# the cue line under the frame shows exactly when the drawing is wider than the frame, and such a frame starts faded on
# the right (data-more="r"). At desktop width (figures scale to the column) the cue and the fade show only on a figure
# wider than its frame and on no other. Runs on the visible panel after its <details> are opened (two frames for shell.js to mark).
FRAME_JS = r'''async ([scope, phone]) => {
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const bad = []; let n = 0, over = 0;
  document.querySelectorAll(scope + ' .viz-scroll').forEach(f => {
    const svg = [...f.querySelectorAll(':scope > svg')].find(s => s.getBoundingClientRect().width > 0); if (!svg || f.clientWidth === 0) return; n++;   // P83: the drawing shown at this width
    const fig = f.closest('figure'), kind = [...fig.classList].find(c => c.startsWith('viz-') && c !== 'viz-wide');
    const nat = svg.viewBox.baseVal.width, w = svg.getBoundingClientRect().width;
    if (phone && Math.abs(w - nat) > 0.6) bad.push(`${kind}: drawn ${w.toFixed(1)} px wide, natural ${nat}`);
    f.scrollLeft = f.scrollWidth;
    const fr = f.getBoundingClientRect(), sr = svg.getBoundingClientRect();
    if (sr.right > fr.right + 1 || f.scrollWidth < Math.floor(w) - 1) bad.push(`${kind}: scroll ${f.scrollWidth} px does not reach the drawing (${w.toFixed(0)} px)`);
    f.scrollLeft = 0; f.dispatchEvent(new Event('scroll'));
    const o = w > f.clientWidth + 1, cue = f.nextElementSibling;
    const shown = !!cue && cue.classList.contains('viz-cue') && !cue.hidden && cue.offsetHeight > 0;
    if (o) over++;
    if (o !== shown) bad.push(`${kind}: drawing ${w.toFixed(0)} px in a ${f.clientWidth} px frame, cue ${shown ? 'shown' : 'not shown'}`);
    if (o && f.getAttribute('data-more') !== 'r') bad.push(`${kind}: an overflowing frame at its start is marked ${f.getAttribute('data-more')}, expected r`);
    if (!o && f.hasAttribute('data-more')) bad.push(`${kind}: a frame that fits is marked ${f.getAttribute('data-more')}`);
    // P83 (3 Nov 2026): on a phone a bars figure and a one- or two-a-row flow fit their frame; a matrix or compare wider than
    // its frame keeps its label column (.viz-stick) at the frame's left edge however far it is scrolled
    if (phone && o && (kind === 'viz-bars' || kind === 'viz-flow' && [...svg.querySelectorAll('rect.viz-node')].filter(r => +r.getAttribute('y') === 8).length <= 2))
      bad.push(`${kind}: ${w.toFixed(0)} px wide, so it scrolls a ${f.clientWidth} px phone frame (P83: it fits)`);
    const st = f.querySelector('.viz-stick');
    if (phone && o && (kind === 'viz-matrix' || kind === 'viz-compare') && !st) bad.push(`${kind}: scrolls with no label column (.viz-stick) to keep in view (P83)`);
    if (phone && st && getComputedStyle(st).display !== 'none') {
      f.scrollLeft = f.scrollWidth; const sr2 = st.getBoundingClientRect(), fr2 = f.getBoundingClientRect(), ss = st.querySelector('svg');
      if (Math.abs(sr2.left - fr2.left) > 1) bad.push(`${kind}: the label column sits ${(sr2.left - fr2.left).toFixed(0)} px from the frame edge when scrolled to the end (P83: sticky)`);
      if (ss && Math.abs(ss.getBoundingClientRect().height - svg.getBoundingClientRect().height) > 1) bad.push(`${kind}: the label column is not as tall as the drawing`);
      f.scrollLeft = 0; f.dispatchEvent(new Event('scroll'));
    }
  });
  return {n, over, bad: bad.slice(0, 8)};
}'''

# P91 (4 Nov 2026); P92 (4 Nov 2026): what the home and What's new must show, read here from the sources, not from the
# build: each live course's units in order (a history course's syllabus units, the audit unit left out, written when
# every module is in its prompts index; a markdown course's units from its data file, written when its vault file is
# filed) with their words (a history unit's: its reports' words, each counted from its vault file as build.py counts
# a report, before the Self-test, figures left out; a markdown unit's: its reading page as published, from its first
# section to the end of its text), each area's words (its live courses' units), every dated unit (vault front matter
# `written`; provenance.json's `written` map for a history report, `written_approx` marking an approximate one) and
# each course's start (its first dated unit), newest first, ties on a day by build order.
FIGBLOCK = re.compile(r'<figure class="viz[ "].*?</figure>', re.S)
def _wc(frag):
    body = re.split(r'<h2>\s*Self-test', FIGBLOCK.sub(' ', frag))[0]
    return len(re.sub(r'<[^>]+>', ' ', body).split())
def home_expect():
    import importlib.util, vault
    prov = json.load(open(R / 'provenance.json'))
    from howbuilt import front
    courses, dated, areas = {}, [], []
    for t in THEMES:
        aw = 0
        for c in COURSES:
            if c['family'] == 'history' and c['theme'] == t['id']:
                syl = (R / c['syllabus']).read_text()
                idx = json.load(open(R / c['prompts']))
                units = [(u, re.findall(r'data-id="([\d.]+)">', body)) for u, body in re.findall(r'<section class="unit" id="u(\d+)"[^>]*>(.*?)</section>', syl, re.S)]
                order = [m for _, ms in units for m in ms]
                def rw(m):
                    f = vault.report_html(c, m, draw=False)
                    f = re.sub(r'<(/?)(html|head|body|!doctype[^>]*)>', '', f, flags=re.I)
                    f = re.sub(r'<style.*?</style>|<script.*?</script>', '', f, flags=re.S | re.I)
                    return _wc(re.sub(r'\sstyle="[^"]*"', '', f))
                us, tiles = [], []
                for u, ms in units:
                    tiles.append((f'U{u}', [(m, rw(m) if m in idx else None) for m in ms]))   # P93: every unit's tile, the audit unit's too
                    if u == c['audit_unit']:
                        continue
                    done = all(m in idx for m in ms)
                    us.append((f'U{u}', sum(rw(m) for m in ms) if done else None))
                aw += sum(rw(m) for m in idx if m in order)
                courses[c['home_id']] = dict(short=c['short'], units=us, tiles=tiles, family='history', tone=c['color'])
                ap = set(prov.get('written_approx', {}).get(c['id'], []))
                for m, d in prov.get('written', {}).get(c['id'], {}).items():
                    if m in idx:
                        dated.append(dict(date=d, rank=order.index(m), home=c['home_id'], code=m, pid=c['prefix'] + m.replace('.', ''), approx=m in ap, course=c['short'], words=rw(m)))
        for c in COURSES:
            if c['family'] != 'markdown':
                continue
            spec = importlib.util.spec_from_file_location('hubv_' + c['id'], R.parent / c['data'])
            d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
            vlt = {}
            for f in (sorted((R.parent / c['vault']).glob('*.md')) if (R.parent / c['vault']).is_dir() else []):
                fm = front(f)
                if fm.get('code'): vlt[fm['code']] = fm
            rid = {r['covers'][0]: r['id'] for r in d.READINGS if 'md' not in r and r.get('covers')}
            order = [o[0] if isinstance(o, (tuple, list)) else o for o in getattr(d, 'ORDER', [])]
            for sc in d.COURSES:
                tr, short = c['tracks'][sc['key']]
                if tr != t['id'] or not any(u[0] in vlt for u in sc['units']):
                    continue                                   # a course with nothing filed is not live: no tile
                pid = f'{c.get("prefix", c["id"])}-{sc["key"].lower()}'
                read = lambda code: rid.get(code, f'read-{c["id"]}-{code.lower()}')
                def secs(code):   # P93: each section's own text (not its next and previous buttons or its band's numeral)
                    page = (SITE / pid / f'{read(code)}.html')
                    page = page if page.exists() else next(SITE.glob(f'*/{read(code)}.html'))
                    body = page.read_text(encoding='utf-8').split('<div class="report steps">', 1)[1].split('<div class="process"', 1)[0]
                    parts = re.findall(r'<section class="sec" data-step="\d+">(.*?)</section>(?=<section class="sec"|</div>)', body, re.S)
                    return [_wc(re.sub(r'<span class="bn"[^>]*>.*?</span>', ' ', re.sub(r'<nav class="secnav".*?</nav>', ' ', x, flags=re.S), flags=re.S)) for x in parts]
                sw = {u[0]: secs(u[0]) for u in sc['units'] if u[0] in vlt}
                us = [(u[0], sum(sw[u[0]]) if u[0] in vlt else None) for u in sc['units']]
                aw += sum(w for _, w in us if w)
                courses[pid] = dict(short=short, units=us, tiles=[(u[0], sw.get(u[0])) for u in sc['units']], family='markdown', tone=sc['color'],
                                    pages={u[0]: read(u[0]) for u in sc['units'] if u[0] in vlt}, briefs={u[0]: (f'{pid}-b-' if not c.get('legacy_ids') else 'b-') + u[0].lower() for u in sc['units']})
                for k, u in enumerate(sc['units']):
                    if u[0] in vlt and vlt[u[0]].get('written'):
                        dated.append(dict(date=str(vlt[u[0]]['written']), rank=order.index(u[0]) if u[0] in order else len(order) + k, home=pid,
                                          code=u[0], pid=read(u[0]), approx=False, course=short, words=sum(sw[u[0]])))
        areas.append(dict(name=t['name'], color=t['color'], words=aw))
    dated.sort(key=lambda x: (x['date'], x['rank']), reverse=True)
    rows = [dict(x, kind='unit') for x in dated]
    for home in dict.fromkeys(x['home'] for x in dated):
        f = min((x for x in dated if x['home'] == home), key=lambda x: (x['date'], x['rank']))
        k = next(i for i, r in enumerate(rows) if r['kind'] == 'unit' and r['home'] == home and r['code'] == f['code'])
        rows.insert(k + 1, dict(f, kind='course', pid=home))   # below its first unit
    days, dom = {}, {}
    tone_of = {h: e['tone'] for h, e in courses.items()}
    for x in dated:
        days[x['date']] = days.get(x['date'], 0) + x['words']
        dom.setdefault(x['date'], {}); dom[x['date']][tone_of[x['home']]] = dom[x['date']].get(tone_of[x['home']], 0) + x['words']
    return dict(courses=courses, areas=areas, newest=dated[0] if dated else None, rows=rows, days=sorted(days.items()),
                day_tones=[max(dom[d], key=dom[d].get) for d in sorted(days)])

# P92 (4 Nov 2026): the home's layout, read on the visible home panel at one width. Returns what was found and the
# faults (bad); check_home compares the hero, the tiles and New since with home_expect().
HOME_JS = r'''([tones, opt]) => {   // P93: opt says what the edition holds (an edition may omit the planned courses and the site links)
  const h = document.getElementById('home'), bad = [], out = {bad};
  const phone = innerWidth < 768, desk = innerWidth >= 1100, de = document.documentElement;
  const vis = e => !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().width > 0;
  const hero = h.querySelector(':scope > header.hero.hhome');
  if (!hero) { bad.push('no hero (header.hero.hhome)'); return out; }
  const resolves = t => !!document.getElementById(t) || [...document.querySelectorAll('.panel[data-anchors]')].some(p => (' ' + p.getAttribute('data-anchors') + ' ').includes(' ' + t + ' '));
  for (const [sel, what] of [['.hbtn.cont, .hbtn.start, [data-long]', 'a Continue button'], ['figure.viz', 'the map (a figure)'], ['.resume, .rmeter', 'the resume card'],
                             ['.tjump', 'the track tiles'], ['.totals, .htot, .htop', 'live totals'], ['.meter', 'a progress meter'], ['.cgo', 'a card button'],
                             ['.shelf, .spine, .shelf-lit', 'the shelf (P91)'], ['.eyebrow', 'an eyebrow line']])
    if (h.querySelector(sel)) bad.push(`the home still has ${what} (${sel})`);
  out.hero = [...hero.children].map(e => e.tagName.toLowerCase() + '.' + [...e.classList].join('.')).join(' ');
  if (out.hero !== 'div.topo div.hcopy') bad.push(`the hero holds ${out.hero}, expected the contour layer and the copy`);
  const copy = hero.querySelector(':scope > .hcopy');
  out.copy = copy ? [...copy.children].map(e => e.tagName.toLowerCase() + '.' + [...e.classList].join('.')).join(' ') : '';
  if (out.copy !== 'h1. p.harea p.harea-all p.lede a.hnew') bad.push(`the hero's copy runs ${out.copy}, expected the headline, the area line, the static line, the lede and the link`);
  const h1 = copy && copy.querySelector(':scope > h1'); if (!h1 || h1.textContent !== 'Academy') bad.push('the headline is not "Academy"');
  // the area line: the four names, in order, each in its tone, hidden from a screen reader; the static line for one
  const al = copy && copy.querySelector('.harea'), st = copy && copy.querySelector('.harea-all');
  const probe = document.createElement('span'); hero.appendChild(probe);
  const tone = v => { probe.style.color = v; return getComputedStyle(probe).color; };
  out.words = al ? [...al.querySelectorAll('.harea-w')].map(w => [w.textContent, getComputedStyle(w).color]) : [];
  out.tones = tones.map(tone); probe.remove();
  if (!al || al.getAttribute('aria-hidden') !== 'true') bad.push('the cycling area line is not hidden from a screen reader');
  if (al && [...al.querySelectorAll('a, button, [tabindex]')].length) bad.push('the area line holds a link or a focus stop');
  out.static = st ? (() => { const c = st.cloneNode(true); c.querySelectorAll('.hsr').forEach(x => x.remove()); return c.textContent; })() : null;   // as seen; the screen reader's commas left out
  out.staticSr = st ? [...st.querySelectorAll('.harea-dot')].map(d => [d.querySelector('[aria-hidden="true"]') ? 1 : 0, d.querySelector('.hsr') ? d.querySelector('.hsr').textContent : null]) : [];
  out.staticTones = st ? [...st.children].filter(e => !e.classList.contains('harea-dot')).map(e => getComputedStyle(e).color) : [];
  out.staticAria = st ? st.getAttribute('aria-hidden') : 'missing';
  out.lineShown = vis(al); out.staticShown = !!st && st.getBoundingClientRect().width > 2 && getComputedStyle(st).clipPath === 'none';
  const lede = copy && copy.querySelector('.lede'); out.lede = lede ? lede.textContent : null;
  // the quiet link: names the newest unit and its day, to #new, at least 44 px, outlined, not filled
  const ln = copy && copy.querySelector('a.hnew');
  if (ln) { const cs = getComputedStyle(ln), r = ln.getBoundingClientRect();
    const vt = e => { const c = e.cloneNode(true); c.querySelectorAll('.hsr').forEach(x => x.remove()); return c.textContent; };   // as seen
    out.linkSr = [...ln.querySelectorAll(':scope > span > [aria-hidden="true"]')].length === 2 && [...ln.querySelectorAll('.hsr')].length === 2;
    out.link = [vt(ln.querySelector('span')), ln.getAttribute('href'), ln.getAttribute('data-target'), Math.round(r.height), cs.backgroundColor, cs.borderTopStyle, parseFloat(cs.borderTopWidth)];
    if (r.height < 43.5) bad.push(`the What's new link is ${r.height.toFixed(0)} px tall, under 44`);
    if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)') bad.push(`the What's new link is filled (${cs.backgroundColor}), not outlined`);
    if (cs.borderTopStyle === 'none' || !(parseFloat(cs.borderTopWidth) > 0)) bad.push('the What\'s new link has no outline');
    if (!out.linkSr) bad.push('the What\'s new link\'s dots are not aria-hidden with a comma for a screen reader');
    if (ln.getAttribute('href') !== '#new' || ln.getAttribute('data-target') !== 'new') bad.push('the What\'s new link does not open #new'); }
  else bad.push('no quiet link to What\'s new');
  // the contour layer: aria-hidden, no text, one layout shown (tall below 1100 px, wide from it), one rise per area
  const topo = hero.querySelector(':scope > .topo');
  if (topo) {
    out.topoBytes = new Blob([topo.outerHTML]).size;
    if (topo.getAttribute('aria-hidden') !== 'true') bad.push('the contour layer is not aria-hidden');
    if (topo.querySelector('text, title, desc') || topo.textContent.trim()) bad.push('the contour layer holds text');
    const shown = [...topo.querySelectorAll('svg.topo-l')].filter(vis);
    out.layout = shown.map(s => s.getAttribute('data-layout'));
    if (out.layout.join() !== (desk ? 'wide' : 'tall')) bad.push(`the contour layout shown is ${out.layout}, expected ${desk ? 'wide' : 'tall'}`);
    out.layouts = [...topo.querySelectorAll('svg.topo-l')].map(s => [s.getAttribute('data-layout'), [...s.querySelectorAll('g.ct-rise, g.ct-plan')].map(g => [g.getAttribute('data-label'), g.classList.contains('ct-plan') ? null : +g.getAttribute('data-words'), +g.getAttribute('data-rings'), getComputedStyle(g.querySelector('path, circle')).stroke, [...g.querySelectorAll('path')].map(e => e.getAttribute('d')).join('').split('z').length - 1])]);
    const tr = topo.getBoundingClientRect(), m = document.querySelector('main').getBoundingClientRect(), cr = copy.getBoundingClientRect();
    out.topoBox = [Math.round(tr.left), Math.round(tr.right), Math.round(cr.left), Math.round(cr.right), Math.round(m.left), Math.round(m.right)];
    if (Math.abs(tr.left - (desk ? 300 : 0)) > 1 || Math.abs(tr.right - de.clientWidth) > 1) bad.push(`the contour layer spans ${tr.left.toFixed(0)}..${tr.right.toFixed(0)}, not the full width beside the sidebar (${desk ? 300 : 0}..${de.clientWidth})`);
    if (cr.left < m.left + 15 || cr.right > m.right - 15) bad.push(`the hero's text runs ${cr.left.toFixed(0)}..${cr.right.toFixed(0)}, outside the column ${m.left.toFixed(0)}..${m.right.toFixed(0)}`);
  } else bad.push('no contour layer');
  // the hero's height: on a phone 60 to 80% of the screen, the first area's heading starting inside the first screen
  const hr = hero.getBoundingClientRect(); out.heroH = [Math.round(hr.height), innerHeight, Math.round(100 * hr.height / innerHeight)];
  if (phone && (hr.height < .6 * innerHeight || hr.height > .8 * innerHeight)) bad.push(`the hero is ${out.heroH[2]}% of the screen, not 60 to 80%`);
  const kids = [...h.children], tracks = kids.filter(e => e.classList.contains('track'));
  const th = tracks.length && tracks[0].querySelector('.thead h2');
  out.first = th ? Math.round(th.getBoundingClientRect().top + scrollY) : null;
  if (phone && th && out.first + 10 > innerHeight) bad.push(`the first area's heading starts at ${out.first} px, not inside the first screen (${innerHeight} px)`);
  // nothing sideways, nothing on the hero past the screen
  out.scroll = [de.scrollWidth, de.clientWidth];
  if (de.scrollWidth > de.clientWidth) bad.push(`the page scrolls sideways (${de.scrollWidth} in ${de.clientWidth} px)`);
  copy && copy.querySelectorAll('*').forEach(e => { if (e.closest('.harea-all') && getComputedStyle(e.closest('.harea-all')).clipPath !== 'none') return;   // the static line, clipped for a screen reader
    const r = e.getBoundingClientRect(); if (r.width && (r.right > de.clientWidth + .5 || r.left < -.5)) bad.push(`${e.className || e.tagName} on the hero runs off the screen`); });
  // the order: hero, the area sections, the constants, the site pages, New since, its one link
  out.order = kids.map(e => e.tagName.toLowerCase() + '.' + [...e.classList].join('.')).join(' ');
  const want = ['header.hero.hhome', ...tracks.map(() => 'section.track'), 'details.howto.rules', ...(opt.site ? ['div.hlinks'] : []), 'section.recent', 'div.hlinks'].join(' ');
  if (out.order !== want) bad.push(`the home runs ${out.order}`);
  // the area headers: from 768 px the label, the name, the lede and the count; below it the name only
  out.heads = tracks.map(t => { const hd = t.querySelector('.thead'); return [t.id, vis(hd.querySelector('.cname')), vis(hd.querySelector('h2')), vis(hd.querySelector('p')), vis(hd.querySelector('.tmeta'))]; });
  out.heads.forEach(([id, c, n, p, m]) => { const ok = phone ? (n && !c && !p && !m) : (n && c && p && m);
    if (!ok) bad.push(`${id}: its header shows label ${c}, name ${n}, lede ${p}, count ${m}; ${phone ? 'below 768 px the name only' : 'from 768 px all four'}`); });
  const site = kids[kids.length - 3], rec = h.querySelector(':scope > .recent'), last = kids[kids.length - 1];
  out.site = site ? [...site.querySelectorAll('a')].map(a => a.getAttribute('href')) : [];
  if (!rec) bad.push('no New since');
  else {
    out.rows = [...rec.querySelectorAll('.hrow')].map(r => [r.getAttribute('data-kind'), r.getAttribute('data-target')]);
    out.since = rec.querySelector('h2').textContent;
    [...rec.querySelectorAll('.hrow')].forEach(r => { if (!r.querySelector('.t small') || !r.querySelector('.pill') || !r.querySelector('.n')) bad.push('a New since row without its date, its course and model line or its pill');
      if (!resolves(r.getAttribute('data-target'))) bad.push(`a New since row links to #${r.getAttribute('data-target')}, no page`); });
    const ln2 = last && last.querySelectorAll('a');
    if (!ln2 || ln2.length !== 1 || ln2[0].getAttribute('href') !== '#new') bad.push('New since is not followed, last on the page, by one link, to What\'s new');
  }
  h.querySelectorAll('.hbtn b, .hbtn span').forEach(el => { if (el.getBoundingClientRect().width > 0 && el.scrollWidth > el.clientWidth + 1) bad.push(`a button's text is cut short: "${el.textContent.trim().slice(0, 40)}"`); });
  // the tiles: every one the same fields, its own contour patch, the whole tile the link
  const cards = [...h.querySelectorAll('.track .cgrid > a.course.live')];
  out.cards = cards.map(c => { const p = c.querySelector(':scope > .topo.topo-patch'), s = p && p.querySelector('svg');
    return {home: c.getAttribute('data-target'), href: c.getAttribute('href'),
            rises: p ? [...p.querySelectorAll('g.ct-rise')].map(g => [g.getAttribute('data-label'), +g.getAttribute('data-words')]) : null,
            rings: p ? [...p.querySelectorAll('g.ct-rise')].map(g => [+g.getAttribute('data-words'), +g.getAttribute('data-rings')]) : null,
            plan: p ? [...p.querySelectorAll('g.ct-plan')].map(g => g.getAttribute('data-label')) : null,
            aria: p && p.getAttribute('aria-hidden'), stroke: p && p.querySelector('path') ? getComputedStyle(p.querySelector('path')).stroke : null,
            tone: getComputedStyle(c).getPropertyValue('--c').trim(), pw: p ? Math.round(p.getBoundingClientRect().width) : 0, cw: Math.round(c.querySelector('.ctitle').parentElement.clientWidth),
            ph: p ? Math.round(p.getBoundingClientRect().height) : 0, sw: s ? Math.round(s.getBoundingClientRect().width) : 0}; });
  cards.forEach(c => {
    const name = c.querySelector('.ctitle').textContent;
    const kidc = [...c.children].map(e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className : '')).join(' ');
    if (kidc !== 'div.ctop span.ctitle p div.cstats div.topo topo-patch') bad.push(`${name}: the tile holds ${kidc}, expected the chip row, the title, the tile line, the stats and the patch`);
    const n = c.querySelectorAll('.cstats > span').length; if (n !== 3) bad.push(`${name}: ${n} stats, expected 3`);
    const ctop = c.querySelector('.ctop'); if (!ctop || !ctop.querySelector('.cname') || !ctop.querySelector('.pill')) bad.push(`${name}: no chip and status pill`);
    const pp = c.querySelector(':scope > p'), lh = parseFloat(getComputedStyle(pp).lineHeight);
    if (pp.scrollHeight > pp.clientHeight + 1) bad.push(`${name}: the tile line is clipped (${pp.scrollHeight} px of ${pp.clientHeight})`);
    if (Math.round(pp.clientHeight / lh) > 2) bad.push(`${name}: the tile line runs to ${Math.round(pp.clientHeight / lh)} lines`);
    if (c.scrollWidth > c.clientWidth + 1) bad.push(`${name}: the tile scrolls sideways`);
    if (c.querySelectorAll('a').length) bad.push(`${name}: a link inside the tile (the whole tile is the link)`);
    const p = c.querySelector('.topo-patch');
    if (p) { const r = p.getBoundingClientRect(), cr = c.getBoundingClientRect();
      if (Math.abs(r.width / r.height - 4) > .05) bad.push(`${name}: the patch is ${r.width.toFixed(0)} x ${r.height.toFixed(0)}, not 4:1`);
      if (r.left < cr.left || r.right > cr.right + .5) bad.push(`${name}: the patch runs out of its tile`); }
  });
  if (new Set(cards.map(c => c.className)).size > 1) bad.push('the course tiles are not one style');
  tracks.forEach(t => {
    const g = t.querySelector('.cgrid'), cs = [...g.querySelectorAll(':scope > a.course')];
    const cols = (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(g).gridTemplateColumns);
    if (phone && cols !== 1) bad.push(`${t.id}: ${cols} columns below 768 px`);
    if (!phone && cols !== 2) bad.push(`${t.id}: ${cols} column(s) from 768 px, expected 2`);
    if (!phone && cs.length === 1) {
      const gw = g.getBoundingClientRect().width, cw = cs[0].getBoundingClientRect().width, gap = parseFloat(getComputedStyle(g).columnGap) || 0;
      if (Math.abs(cw - (gw - gap) / 2) > 2) bad.push(`${t.id}: its only tile is ${cw.toFixed(0)} px of a ${gw.toFixed(0)} px grid, expected half`);
    }
    if (t.id === 'track-history' && (!t.querySelector('details.howto.rules:not(.planned)') || (opt.planned && !t.querySelector('details.planned#planned-courses')))) bad.push('History lost "Why history and myth together" or its folded Planned list');
  });
  // what runs: with reduced motion nothing on the home; with motion allowed only transform and opacity, none on a tile
  out.anims = document.getAnimations().filter(a => a.animationName && a.effect && a.effect.target && h.contains(a.effect.target)).map(a => {   // P93: animations; the transitions of a hover or the theme switch are not
    const t = a.effect.target, props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k)).filter(k => !['offset', 'computedOffset', 'easing', 'composite'].includes(k)))];
    return [t.className && typeof t.className === 'string' ? t.className : (t.getAttribute('class') || t.tagName), props, a.playState, !!t.closest('.course'), a.animationName]; });
  return out;
}'''
MON3 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# P92: the hero's texts against the pixels actually under them (the contour lines, the page), in the theme in use: each
# text's box and colour are read, every text of the copy is made transparent, the hero is shot, and each text's colour
# is measured against every pixel in its box (4.5:1, 3:1 for large text); the texts are put back.
HERO_TEXTS_JS = r'''() => { const out = [], copy = document.querySelector('#home .hcopy');
  copy.querySelectorAll('h1, .harea-w, .harea-all > span, .lede, .hnew > span').forEach(e => { const cs = getComputedStyle(e), r = e.getBoundingClientRect();
    if (!r.width || cs.display === 'none' || (e.closest('.harea-all') && getComputedStyle(e.closest('.harea-all')).clipPath !== 'none')) return;   // the static line read by a screen reader only
    const size = parseFloat(cs.fontSize), large = size >= 24 || (size >= 18.66 && parseInt(cs.fontWeight) >= 700);
    out.push({what: (e.className || e.tagName.toLowerCase()) + ' "' + e.textContent.trim().slice(0, 18) + '"', color: cs.color, large, x: r.left, y: r.top, w: r.width, h: r.height}); });
  return out; }'''
def hero_contrast(pg, label, fails, motion=False):
    """P92: with motion allowed, every moment that matters; P93: at the five poses of the slow move (POSES: its two ends,
    its quarters and its middle) and, at each, each area word in turn (its animation set to the middle of its showing),
    every animation paused there."""
    if not motion:
        return _hero_contrast(pg, label, fails)
    names = pg.evaluate("[...document.querySelectorAll('#home .harea-w')].map(w => w.textContent)")
    for p in POSES:
        for k, nm in enumerate(names):
            pose(pg, p, k * 3000 + 1500)
            _hero_contrast(pg, f'{label} (pose {p:g} of the sweep, {nm} shown)', fails, only=k)
    pg.evaluate("() => document.getAnimations().forEach(a => a.play())")

def _hero_contrast(pg, label, fails, only=None):
    from PIL import Image
    import io
    pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(60)
    items = pg.evaluate(HERO_TEXTS_JS)
    if only is not None:   # the cycling words: only the one shown at this moment
        ws = [i for i in items if i['what'].startswith('harea-w')]
        items = [i for i in items if not i['what'].startswith('harea-w')] + ws[only:only + 1]
    pg.evaluate("""() => { const s = document.createElement('style'); s.id = 'p92hide'; s.textContent = '#home .hcopy, #home .hcopy * {color: transparent !important; border-color: transparent !important; transition: none !important}'; document.head.appendChild(s); }""")
    pg.wait_for_timeout(60)
    img = Image.open(io.BytesIO(pg.screenshot())).convert('RGB')
    pg.evaluate("document.getElementById('p92hide').remove()")
    k = img.width / pg.evaluate('innerWidth')
    def lum(c):
        f = lambda v: (v / 255) / 12.92 if v / 255 <= 0.04045 else ((v / 255 + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])
    worst, each = [99, ''], []
    for it in items:
        fg = [float(v) for v in re.findall(r'[\d.]+', it['color'])[:3]]
        lf = lum(fg)
        box = img.crop((int(it['x'] * k), int(it['y'] * k), int((it['x'] + it['w']) * k), int((it['y'] + it['h']) * k)))
        lo = 99
        for c, _ in [(c, n) for n, c in box.getcolors(box.width * box.height or 1) or []]:
            lb = lum(c); r = (max(lf, lb) + .05) / (min(lf, lb) + .05)
            lo = min(lo, r)
        need = 3 if it['large'] else 4.5
        if lo < worst[0]: worst = [round(lo, 2), it['what']]
        each.append(f'{it["what"].split(chr(34))[1] if chr(34) in it["what"] else it["what"]} {lo:.2f}/{need:g}')
        if lo < need - .005: fails.append(f'home {label}: {it["what"]} reaches {lo:.2f}:1 over the contours under it (needs {need}:1)')
    print(f'home {label} ({pg.evaluate("innerWidth")} px): hero texts over the contours, {len(items)} measured pixel by pixel, lowest {worst[0]}:1 ({worst[1]}); each (lowest/needed): ' + '; '.join(each))

def check_home(pg, label, fails, expect, motion=False):
    """P92: the home's layout at one width (HOME_JS): the hero (the headline, the area line and its static line, the
    lede, the quiet link, the contour layer, its rises against the sources), its height, the area headers, the tiles and
    their patches against the sources, the order, New since as What's new's first six rows; and what animates."""
    pg.evaluate("location.hash = 'home'"); ready(pg); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(160)
    # a theme switched by the test fades the tiles' colours (section 7's .15 s transitions): read the page once they are done
    pg.wait_for_function("() => !document.getAnimations().some(a => typeof CSSTransition !== 'undefined' && a instanceof CSSTransition && a.playState === 'running')", timeout=5000)
    r = pg.evaluate(HOME_JS, [[a['color'] for a in expect['areas']], {'planned': 'planned' not in OMIT, 'site': any(k not in OMIT for k in ('backlog', 'figures', 'changelog'))}])
    fails += [f'home {label}: {b}' for b in r['bad']]
    names = [a['name'] for a in expect['areas']]
    if [w for w, _ in r.get('words', [])] != names: fails.append(f'home {label}: the area line reads {[w for w, _ in r.get("words", [])]}, THEMES gives {names}')
    if [c for _, c in r.get('words', [])] != r.get('tones'): fails.append(f'home {label}: the area words are coloured {[c for _, c in r.get("words", [])]}, their tones are {r.get("tones")}')
    if r.get('static') != ' · '.join(names).replace(' · ', ' · '): fails.append(f'home {label}: the static line reads {r.get("static")!r}')
    if r.get('staticTones') != r.get('tones'): fails.append(f'home {label}: the static line\'s words are coloured {r.get("staticTones")}, not their tones')
    if r.get('staticSr') != [[1, ',']] * (len(names) - 1): fails.append(f'home {label}: the static line\'s dots are not aria-hidden with a comma for a screen reader: {r.get("staticSr")}')
    if r.get('staticAria') is not None: fails.append(f'home {label}: the static line is hidden from a screen reader ({r.get("staticAria")})')
    if motion and (not r.get('lineShown') or r.get('staticShown')): fails.append(f'home {label}: with motion allowed the cycling line shows {r.get("lineShown")} and the static line {r.get("staticShown")}, expected the cycling line only')
    if not motion and (r.get('lineShown') or not r.get('staticShown')): fails.append(f'home {label}: under reduced motion the cycling line shows {r.get("lineShown")} and the static line {r.get("staticShown")}, expected the static line only')
    if r.get('lede') != 'Every self-study course in one place. Pick up where you left off.': fails.append(f'home {label}: the lede reads {r.get("lede")!r}')
    nw = expect['newest']
    want_link = f"What's new · {nw['code']} · {int(nw['date'][8:])} {MON3[int(nw['date'][5:7]) - 1]}" if nw else None
    if r.get('link') and r['link'][0] != want_link: fails.append(f'home {label}: the What\'s new link reads {r["link"][0]!r}, expected {want_link!r}')
    if (r.get('topoBytes') or 0) > 20 * 1024: fails.append(f'home {label}: the hero\'s contour SVG is {r["topoBytes"]} bytes, over 20 KB')
    for name, rs in r.get('layouts', []):
        got = [(l, w) for l, w, _, _, _ in rs]
        want = [(a['name'], a['words'] or None) for a in expect['areas']]
        if got != want: fails.append(f'home {label}: the {name} contours give the rises {got}, the sources give {want}')
        rings = [k for _, w, k, _, _ in rs if w]
        byw = [k for _, k in sorted((w, k) for _, w, k, _, _ in rs if w)]
        for l, w, k, _, z in rs:   # P92 check: every rise reads as a rise, its own top rings closed, not only a stretch of another's
            if w and z < min(2, k): fails.append(f'home {label}: the {name} rise {l} closes {z} ring(s) of its own, under {min(2, k)}')
        if byw != sorted(byw): fails.append(f'home {label}: the {name} rises stand {rings} levels high, not in the order of their words')
        if [s for _, _, _, s, _ in rs] != r.get('tones'): fails.append(f'home {label}: the {name} rises are drawn in {[x[3] for x in rs]}, not their areas\' tones')
    got = {c['home']: c for c in r.get('cards', [])}
    if list(got) != list(expect['courses']): fails.append(f'home {label}: the tiles are {list(got)}, the sources give {list(expect["courses"])}')
    for home, e in expect['courses'].items():
        c = got.get(home)
        if not c: continue
        want_r = [(k, w) for k, w in e['units'] if w]
        if [tuple(x) for x in (c['rises'] or [])] != want_r: fails.append(f'home {label}: {e["short"]}\'s patch has the rises {c["rises"]}, the sources give its written units {want_r}')
        if (c['plan'] or []) != [k for k, w in e['units'] if not w]: fails.append(f'home {label}: {e["short"]}\'s patch marks {c["plan"]} planned, the sources {[k for k, w in e["units"] if not w]}')
        if c['aria'] != 'true': fails.append(f'home {label}: {e["short"]}\'s patch is not aria-hidden')
        byw = [k for _, k in sorted(c['rings'] or [])]
        if byw != sorted(byw): fails.append(f'home {label}: {e["short"]}\'s patch rises stand {[k for _, k in c["rings"]]} levels high, not in the order of their words')
        if c['href'] != '#' + home: fails.append(f'home {label}: {e["short"]}\'s tile links to {c["href"]}')
    want_rows = [[x['kind'], x['pid']] for x in expect['rows'][:6]]
    if r.get('rows') != want_rows: fails.append(f'home {label}: New since lists {r.get("rows")}, What\'s new leads with {want_rows}')
    if expect['rows'][:6] and r.get('since') != f"New since {int(expect['rows'][5]['date'][8:])} {MON3[int(expect['rows'][5]['date'][5:7]) - 1]}":
        fails.append(f'home {label}: New since\'s heading reads {r.get("since")!r}, its oldest row is {expect["rows"][5]["date"]}')
    want_site = [x for x, k in (('#backlog', 'backlog'), ('#viz-examples', 'figures'), ('#changelog', 'changelog')) if k not in OMIT]
    if r.get('site') != want_site: fails.append(f'home {label}: the site links above New since are {r.get("site")}, expected {want_site}')
    an = r.get('anims', [])
    if motion:
        if [a for a in an if any(p not in ('transform', 'opacity') for p in a[1])]: fails.append(f'home {label}: an animation runs on more than transform and opacity: {[a for a in an if any(p not in ("transform", "opacity") for p in a[1])]}')
        nb = sum(1 for a in an if a[4] == 'topo-breathe')   # P93 follow-up: every drawing breathes, as it turns
        if nb != sum(1 for a in an if a[4] == 'topo-turn'): fails.append(f'home {label}: {nb} drawings breathe, {sum(1 for a in an if a[4] == "topo-turn")} turn')
        an = [a for a in an if a[4] != 'topo-breathe']
        kinds = sorted({a[0].split()[0] for a in an})
        npatch = pg.evaluate("document.querySelectorAll('#home .topo.topo-patch').length")   # a patch in the closed Planned list is not drawn, but its move runs
        if kinds != ['harea-w', 'topo-l'] or sum(1 for a in an if a[0].startswith('harea-w')) != len(names) or sum(1 for a in an if a[0].startswith('topo-l')) != 1 + npatch:
            fails.append(f'home {label}: with motion allowed the animations are {[(a[0], a[1]) for a in an]}, expected the {len(names)} area words, the shown contour layout and every tile\'s patch ({npatch}; P93)')
    elif an: fails.append(f'home {label}: under reduced motion {len(an)} animations run: {an[:3]}')
    print(f'home {label}: hero {r.get("heroH")} (px, screen, %), copy {r.get("copy")!r}; area line {[w for w, _ in r.get("words", [])]}, shown {r.get("lineShown")}, static shown {r.get("staticShown")}; '
          f'link {r.get("link") and r["link"][:4]}; contours {r.get("topoBytes")} B, layout {r.get("layout")}, rises {[(l, k, z) for _, rs in r.get("layouts", [])[:1] for l, _, k, _, z in rs]}; '
          f'tiles {[(c["home"], len(c["rises"] or []), len(c["plan"] or [])) for c in r.get("cards", [])]}; heads {[x[1:] for x in r.get("heads", [])][:1]}; '
          f'first area at {r.get("first")} px; New since {len(r.get("rows") or [])} rows; animations {len(an)}; page {r.get("scroll")}')
    hero_contrast(pg, label, fails, motion)
    return r

# P93 (4 Nov 2026): a page's topography at the pose it is in: its hero's layer (header.hero > .topo) and every visible
# tile patch. For each: bytes, aria-hidden, no text, the layouts shown, each layout's rises (label, words or null for a
# planned one, levels, stroke, own closed rings) and, on the shown layout, (a) whether the frame is covered: each corner of
# the frame mapped back through the layout's transform (its computed matrix about its origin) into the layout's own box;
# (b) for a hero, which rises' own rings (data-box, through the SVG's screen matrix) leave the frame or reach into its
# fade (its last 10%); (c) for a patch, whether every line stays inside its frame. And every animation on the page with
# its properties and its directed progress.
TOPO_JS = r"""(pid) => {
  const P = document.getElementById(pid), out = {pid, patches: []};
  if (!P) return out;
  const vis = e => !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().width > 0;
  const covered = (svg, frame) => {
    const cs = getComputedStyle(svg), fr = frame.getBoundingClientRect();
    const lx = parseFloat(cs.left), ly = parseFloat(cs.top), lw = parseFloat(cs.width), lh = parseFloat(cs.height);
    const o = cs.transformOrigin.split(' ').map(parseFloat);
    const M = cs.transform === 'none' ? new DOMMatrix() : new DOMMatrix(cs.transform), I = M.inverse();
    const bad = [];
    for (const [qx, qy] of [[0, 0], [fr.width, 0], [0, fr.height], [fr.width, fr.height]]) {
      const v = I.transformPoint(new DOMPoint(qx - lx - o[0], qy - ly - o[1]));
      const x = v.x + o[0], y = v.y + o[1];
      if (x < -0.5 || y < -0.5 || x > lw + 0.5 || y > lh + 0.5) bad.push([Math.round(qx), Math.round(qy), Math.round(x), Math.round(y)]);
    }
    return {bad, size: [Math.round(lw), Math.round(lh), Math.round(fr.width), Math.round(fr.height)], m: cs.transform};
  };
  const rises = svg => [...svg.querySelectorAll('g.ct-rise, g.ct-plan')].map(g => { const pa = g.querySelector('path, circle');
    return [g.getAttribute('data-label'), g.classList.contains('ct-plan') ? null : +g.getAttribute('data-words'), g.classList.contains('ct-plan') ? null : +g.getAttribute('data-rings'),
            getComputedStyle(pa).stroke, g.classList.contains('ct-plan') ? 0 : ([...g.querySelectorAll('path')].map(e => e.getAttribute('d')).join('').split('z').length - 1)]; });
  const one = (t, hero) => {
    const r = {bytes: new Blob([t.outerHTML]).size, aria: t.getAttribute('aria-hidden'), text: !!(t.querySelector('text, title, desc') || t.textContent.trim()),
               shown: [...t.querySelectorAll(':scope > svg.topo-l')].filter(vis).map(x => x.getAttribute('data-layout')),
               layouts: [...t.querySelectorAll(':scope > svg.topo-l')].map(x => [x.getAttribute('data-layout'), rises(x)]), ph: getComputedStyle(t).getPropertyValue('--ph').trim()};
    const sv = [...t.querySelectorAll(':scope > svg.topo-l')].find(vis);
    if (sv) {
      r.cover = covered(sv, t);
      const fr = t.getBoundingClientRect(), m = sv.getScreenCTM();
      if (hero) {
        r.outside = [];
        sv.querySelectorAll('g.ct-rise[data-box]').forEach(g => { const b = g.getAttribute('data-box').split(' ').map(Number);   // P93 follow-up: data-box is the rings at the top of the breath
          for (const [x, y] of [[b[0], b[1]], [b[2], b[1]], [b[0], b[3]], [b[2], b[3]]]) { const q = new DOMPoint(x, y).matrixTransform(m);
            if (q.x < fr.left - .5 || q.x > fr.right + .5 || q.y < fr.top - .5 || q.y > fr.top + .9 * fr.height + .5) { r.outside.push(g.getAttribute('data-label')); break; } } });
        r.frame = [Math.round(fr.left), Math.round(fr.right), Math.round(fr.top + scrollY), Math.round(fr.height)];
      } else {
        let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        sv.querySelectorAll('path, circle').forEach(e => { const b = e.getBoundingClientRect(); if (!b.width && !b.height) return; x0 = Math.min(x0, b.left); y0 = Math.min(y0, b.top); x1 = Math.max(x1, b.right); y1 = Math.max(y1, b.bottom); });
        r.lines = [x0 - fr.left, y0 - fr.top, fr.right - x1, fr.bottom - y1].map(v => Math.round(v * 10) / 10);
        r.ratio = Math.round(fr.width / fr.height * 1000) / 1000;
      }
    }
    return r;
  };
  const hl = P.querySelector(':scope > header.hero > .topo');
  out.hero = hl ? one(hl, true) : null;
  out.anyTopo = P.querySelectorAll('.topo:not(.topo-sep):not(.relief)').length; out.allPatches = P.querySelectorAll('.topo.topo-patch:not(.topo-sep)').length;   // P94: a reading page's section separators are checked by check_seps; P96: its relief by check_reliefs
  P.querySelectorAll('.topo.topo-patch:not(.topo-sep)').forEach(t => { if (vis(t)) out.patches.push(one(t, false)); });
  out.anims = document.getAnimations().filter(a => a.animationName && a.effect && a.effect.target && P.contains(a.effect.target) && !a.effect.target.closest('.topo-sep')).map(a => {   // animations, not the transitions of a hover or the theme switch
    const t = a.effect.target, props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k)).filter(k => !['offset', 'computedOffset', 'easing', 'composite'].includes(k)))];
    return [(t.getAttribute('class') || t.tagName).split(' ')[0], props, a.playState, a.animationName || '', a.effect.getComputedTiming().progress, !!t.closest('.topo-patch')]; });
  return out;
}"""

# P93: every tile of a page (.course.live): its kind (a link, a disclosure, a ghost), its fields, its patch, its link or
# its rows, the grid it stands in, and anything cut
TILES_JS = r"""(pid) => {
  const P = document.getElementById(pid), out = {tiles: [], grids: [], bad: []};
  if (!P) return out;
  const vis = e => !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().width > 0;
  const phone = innerWidth < 768;
  P.querySelectorAll('.course.live').forEach(t => {
    if (!vis(t)) return;
    const disc = t.tagName === 'DETAILS', box = disc ? t.querySelector(':scope > summary') : t;
    const kids = [...box.children].map(e => e.tagName.toLowerCase() + ((e.getAttribute('class') || '') ? '.' + e.getAttribute('class').split(' ').join('.') : '')).join(' ');
    const p = box.querySelector(':scope > p'), lh = p ? parseFloat(getComputedStyle(p).lineHeight) : 1;
    const patch = box.querySelector(':scope > .topo.topo-patch'), pr = patch && patch.getBoundingClientRect(), tr = t.getBoundingClientRect();
    const sv = patch && patch.querySelector('svg');
    const name = (box.querySelector('.ctitle') || {}).textContent || '?';
    const r = {name, kind: t.classList.contains('ghost') ? 'ghost' : disc ? 'disc' : t.tagName === 'A' ? 'link' : 'other', cls: [...t.classList].filter(c => !['ghost', 'pending'].includes(c)).join(' '),
      mods: [...t.classList].filter(c => ['ghost', 'pending'].includes(c)), spots: sv ? [...sv.querySelectorAll('g.ct-rise')].filter(g => g.querySelector('.ct-spot')).map(g => g.getAttribute('data-label')) : null,
      unseen: sv ? [...sv.querySelectorAll('g.ct-rise')].filter(g => +g.getAttribute('data-rings') === 0 && !g.querySelector('.ct-spot')).map(g => g.getAttribute('data-label')) : null,
      kids, chip: [...box.querySelectorAll('.ctop > .cname > .cpart')].map(x => x.textContent), pill: box.querySelector('.ctop > .pill') ? box.querySelector('.ctop > .pill').textContent : null,
      stats: [...box.querySelectorAll('.cstats > span')].map(x => [x.querySelector('b') ? x.querySelector('b').textContent : null, x.textContent.replace(x.querySelector('b') ? x.querySelector('b').textContent : '', '').trim()]),
      lines: p ? Math.round(p.getBoundingClientRect().height / lh) : 0, ids: t.getAttribute('data-mods'),   /* as painted (P93 check: a stretched line showed a third line under its clamp) */ clipped: p ? p.scrollHeight > p.clientHeight + 1 : false, open: disc ? t.open : null,
      href: t.getAttribute('href'), target: t.getAttribute('data-target'),
      rows: disc ? t.querySelectorAll(':scope > .hrows > .hrow').length : null,
      rises: sv ? [...sv.querySelectorAll('g.ct-rise')].map(g => [g.getAttribute('data-label'), +g.getAttribute('data-words')]) : null,
      plan: sv ? [...sv.querySelectorAll('g.ct-plan')].map(g => g.getAttribute('data-label')) : null,
      aria: patch && patch.getAttribute('aria-hidden'), stroke: sv && sv.querySelector('path, circle') ? getComputedStyle(sv.querySelector('path, circle')).stroke : null,
      tone: getComputedStyle(t).getPropertyValue('--c').trim(),
      pw: pr ? Math.round(pr.width) : 0, ph: pr ? Math.round(pr.height) : 0, pin: pr ? (pr.left >= tr.left - .5 && pr.right <= tr.right + .5) : false,
      sw: t.scrollWidth > t.clientWidth + 1, w: Math.round(tr.width)};
    box.querySelectorAll('.ctitle, .cname, .cstats > span').forEach(e => { if (e.getBoundingClientRect().right > tr.right + .5) out.bad.push(`${name}: ${e.className || e.tagName} runs past the tile's edge`); });
    if (t.querySelector('a') && !disc) out.bad.push(`${name}: a link inside a linked tile`);
    out.tiles.push(r);
  });
  P.querySelectorAll('.cgrid').forEach(g => { if (!vis(g)) return;
    const ts = [...g.children].filter(e => e.classList.contains('course')), gw = g.getBoundingClientRect().width, gap = parseFloat(getComputedStyle(g).columnGap) || 0;
    const gr = g.getBoundingClientRect();
    if (g.querySelector(':scope > details.course.live[open]')) ts.forEach(t => { if (t.tagName !== 'DETAILS' || t.open) return; const st = t.querySelector(':scope > summary > .cstats'); if (st && parseFloat(getComputedStyle(st).marginTop) > 1) out.bad.push(`${t.querySelector('.ctitle') ? t.querySelector('.ctitle').textContent.trim() : t.className}: closed beside an open tile, yet stretched (${Math.round(parseFloat(getComputedStyle(st).marginTop))} px of slack above its stats)`); });   // P93, after the publish
    ts.forEach(t => { const r = t.getBoundingClientRect(); if (r.left < gr.left - .5 || r.right > gr.right + .5) out.bad.push(`${t.querySelector('.ctitle') ? t.querySelector('.ctitle').textContent.trim() : t.className}: the tile runs ${Math.round(Math.max(gr.left - r.left, r.right - gr.right))} px past its grid`); });   // P93 check 3: a column widened past its grid by a part that would not wrap
    out.grids.push([(t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(g).gridTemplateColumns), ts.length, ts.length === 1 ? Math.round(ts[0].getBoundingClientRect().width) : null, Math.round((gw - gap) / 2)]); });
  const de = document.documentElement; out.scroll = [de.scrollWidth, de.clientWidth];
  return out;
}"""

_TM = re.search(r'--topo-turn:([\d.]+)deg;--topo-cycle:([\d.]+)s;[^\n]*\n\s*--topo-grow:([\d.]+);--topo-breath:([\d.]+)s', (R / 'shell.css').read_text())
TURN, CYCLE, GROW, BTIME = float(_TM.group(1)), float(_TM.group(2)) * 1000, float(_TM.group(3)), float(_TM.group(4)) * 1000   # P93: the turn and (follow-up, 5 Nov) the breath, from the theme
POSES = (0, .25, .5, .75, 1)   # the two ends of the sweep, its quarters and its middle
def eased(p):
    """CSS ease-in-out, cubic-bezier(.42, 0, .58, 1), at the point p of the sweep: the share of the move made."""
    lo, hi = 0.0, 1.0
    for _ in range(60):
        t = (lo + hi) / 2
        x = 3 * (1 - t) ** 2 * t * .42 + 3 * (1 - t) * t * t * .58 + t ** 3
        lo, hi = (t, hi) if x < p else (lo, t)
    t = (lo + hi) / 2
    return 3 * (1 - t) * t * t + t ** 3
POSE_JS = r"""([p, ta, cyc, bt]) => { document.getAnimations().forEach(a => { if (!a.animationName) { a.finish(); return; }   // a transition (a hover, the theme switch) is let run out: paused half-way it would outrank every rule
  a.pause();
  if (a.animationName === 'topo-turn') { const d = a.effect.getTiming().delay; let t = p * cyc + d; if (t < 0) t = 2 * cyc - p * cyc + d; a.currentTime = t; }
  else if (a.animationName === 'topo-breathe') { let t = a.effect.getTiming().delay + .9999 * bt; if (t < 0) t += 2 * bt; a.currentTime = t; }   // P93 follow-up: every drawing at the top of its breath
  else if (ta !== null) a.currentTime = ta; }); }"""
def pose(pg, p, ta=None):
    """Every contour drawing on the page paused at the point p (0 to 1) of its sweep, its own phase taken into account;
    the area words (the home) at ta ms of their cycle."""
    pg.evaluate(POSE_JS, [p, ta, CYCLE, BTIME]); pg.wait_for_timeout(80)

# the texts of a hero over a topography (a course home's, What's new's), as the eye reads them: every element of the
# hero with a text of its own, its colour, the opacity it is drawn at and whether it is large text
HERO_ALL_JS = r"""(pid) => { const h = document.querySelector('#' + pid + ' > header.hero'), out = [];
  h.querySelectorAll('*').forEach(e => { if (e.closest('.topo')) return;
    if (![...e.childNodes].some(t => t.nodeType === 3 && t.textContent.trim())) return;
    const cs = getComputedStyle(e), r = e.getBoundingClientRect(); if (!r.width || cs.display === 'none' || cs.visibility !== 'visible' || e.closest('[hidden]')) return;
    let op = 1; for (let x = e; x && x !== h; x = x.parentElement) op *= parseFloat(getComputedStyle(x).opacity);
    const size = parseFloat(cs.fontSize), large = size >= 24 || (size >= 18.66 && parseInt(cs.fontWeight) >= 700);
    out.push({what: (e.getAttribute('class') || e.tagName.toLowerCase()) + ' "' + e.textContent.trim().slice(0, 18) + '"', color: cs.color, op, large,
              sep: !!e.closest('[aria-hidden="true"]'), x: r.left, y: r.top, w: r.width, h: r.height}); });
  return out; }"""

def _lum(c):
    f = lambda v: (v / 255) / 12.92 if v / 255 <= 0.04045 else ((v / 255 + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])

def texts_contrast(pg, pid, label, fails, tag=''):
    """P93: a hero's texts against the pixels under them, as on the home (P92): every text made transparent, the hero
    shot, each text's colour (at the opacity it is drawn with) measured against every pixel in its box: 4.5:1, 3:1 for
    large text. Returns the lowest ratio."""
    from PIL import Image
    import io
    pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(40)
    items = pg.evaluate(HERO_ALL_JS, pid)
    pg.evaluate("""(pid) => { const s = document.createElement('style'); s.id = 'p93hide'; s.textContent = '#' + pid + ' > header.hero *:not(.topo):not(.topo *) {color: transparent !important; text-decoration-color: transparent !important; transition: none !important}'; document.head.appendChild(s); }""", pid)
    pg.wait_for_timeout(50)
    hb = pg.evaluate(f"(() => {{ const r = document.querySelector('#{pid} > header.hero').getBoundingClientRect(); return Math.ceil(r.bottom + scrollY); }})()")
    img = Image.open(io.BytesIO(pg.screenshot(full_page=True, clip=dict(x=0, y=0, width=pg.evaluate('innerWidth'), height=hb)))).convert('RGB')   # the hero whole, past the screen's foot on a short phone
    pg.evaluate("document.getElementById('p93hide').remove()")
    k = img.width / pg.evaluate('innerWidth')
    worst, each = [99, ''], []
    for it in items:
        nums = [float(v) for v in re.findall(r'[\d.]+', it['color'])]
        fg = [v * 255 for v in nums[:3]] if it['color'].startswith('color(') else nums[:3]   # a color-mix() computes as color(srgb r g b), 0 to 1
        a = it['op'] * (nums[3] if len(nums) > 3 else 1)
        box = img.crop((int(it['x'] * k), int(it['y'] * k), int((it['x'] + it['w']) * k), int((it['y'] + it['h']) * k)))
        lo = 99
        for _, c in box.getcolors(box.width * box.height or 1) or []:
            col = [fg[i] * a + c[i] * (1 - a) for i in range(3)]
            l1, l2 = _lum(col), _lum(c)
            lo = min(lo, (max(l1, l2) + .05) / (min(l1, l2) + .05))
        need = 3 if it['large'] else 4.5
        if lo < worst[0]: worst = [round(lo, 2), it['what']]
        each.append(f'{it["what"][:28]} {lo:.2f}/{need:g}')
        if lo < need - .005:
            fails.append(f'{pid} {label}{tag}: {it["what"]} reaches {lo:.2f}:1 over the contours under it (needs {need}:1)')
    print(f'{pid} {label}{tag} ({pg.evaluate("innerWidth")} px): hero texts over the contours, {len(items)} measured pixel by pixel, lowest {worst[0]}:1 ({worst[1]})')
    return worst[0]

def check_topo(pg, pid, label, fails, expect, motion=False, phase=True):
    """P93: one page's topography against the sources: the hero's layer (a course home: one rise per unit of the course
    in its order, a written unit by its words, a planned one flat; What's new: one rise per day it lists, oldest first,
    its words that day's; the largest day standing 10 to 25 levels), aria-hidden, no text, at most 20 KB, one layout
    shown (tall below 1100 px, wide from it), each written rise closing min(2, levels) rings of its own, in its tone,
    the frame covered at the pose it is in, each rise's own rings inside the frame and above the fade (at 390 px: inside
    the phone's view); every patch 4:1, its lines inside its frame; with motion allowed only transform or opacity
    animating, every drawing at its own point of the cycle; under reduced motion nothing running. Returns the layer's
    info."""
    r = pg.evaluate(TOPO_JS, pid)
    w = pg.evaluate('innerWidth')
    desk = w >= 1100
    h = r.get('hero')
    want = None
    if pid == 'new':
        want = [(d, wd) for d, wd in expect['days']]
    elif pid in expect['courses']:
        want = [(k, wd) for k, wd in expect['courses'][pid]['units']]
    if want is not None:
        if not h: fails.append(f'{pid} {label}: no topography behind the hero')
        else:
            if h['aria'] != 'true': fails.append(f'{pid} {label}: the hero\'s layer is not aria-hidden')
            if h['text']: fails.append(f'{pid} {label}: the hero\'s layer holds text')
            if h['bytes'] > 20 * 1024: fails.append(f'{pid} {label}: the hero\'s layer is {h["bytes"]} bytes, over 20 KB')
            if h['shown'] != (['wide'] if desk else ['tall']): fails.append(f'{pid} {label}: the layout shown is {h["shown"]}, expected {"wide" if desk else "tall"}')
            for name, rs in h['layouts']:
                got = [(l, wd) for l, wd, _, _, _ in rs]
                if got != want: fails.append(f'{pid} {label}: the {name} layout gives the rises {got[:4]}..., the sources {want[:4]}...')
                for l, wd, k, _, z in rs:
                    if wd and z < min(2, k): fails.append(f'{pid} {label}: the {name} rise {l} closes {z} ring(s) of its own, under {min(2, k)}')
                strokes = [st for _, _, _, st, _ in rs]
                want_t = expect['day_tones'] if pid == 'new' else None
                if pid != 'new' and len(set(strokes)) != 1: fails.append(f'{pid} {label}: the {name} rises are drawn in {set(strokes)}, not the course\'s one tone')
                if pid == 'new' and len(strokes) == len(want_t) and any(pg.evaluate(f"(() => {{ const e = document.createElement('i'); e.style.color = '{c}'; document.body.appendChild(e); const v = getComputedStyle(e).color; e.remove(); return v; }})()") != st for c, st in zip(want_t, strokes)):
                    fails.append(f'{pid} {label}: the days are drawn in {strokes}, not each in the tone of the course that filed the most words that day ({want_t})')
                if pid == 'new':
                    top = max(rs, key=lambda x: x[1] or 0)
                    if not 10 <= top[2] <= 25: fails.append(f'{pid} {label}: its largest day ({top[0]}) stands {top[2]} levels, not 10 to 25')
            c = h.get('cover') or {}
            if c.get('bad'): fails.append(f'{pid} {label}: the frame\'s corners {c["bad"]} fall outside the turned layout {c.get("size")}: an edge of the drawing shows')
            if h.get('outside') and w >= 390: fails.append(f'{pid} {label}: the rises {h["outside"]} have rings outside the frame or in its fade')
            elif h.get('outside') and not motion: print(f'{pid} {label}: below 390 px the rises {h["outside"]} reach past the narrower window (the row sets 390 px)')
    for k, pt in enumerate(r['patches']):
        if pt['aria'] != 'true' or pt['text']: fails.append(f'{pid} {label}: patch {k + 1} is not aria-hidden or holds text')
        if pt.get('lines') and min(pt['lines']) < -.5: fails.append(f'{pid} {label}: patch {k + 1}\'s lines leave its frame by {[-x for x in pt["lines"] if x < 0]} px')
        if pt.get('ratio') and abs(pt['ratio'] - 4) > .05: fails.append(f'{pid} {label}: patch {k + 1} is {pt["ratio"]}:1, not 4:1')
    an = r['anims']
    if motion:
        odd = [a for a in an if any(x not in ('transform', 'opacity') for x in a[1])]
        if odd: fails.append(f'{pid} {label}: an animation runs on more than transform and opacity: {odd[:3]}')
        tp = [a for a in an if a[3] == 'topo-turn']
        nt = (1 if h else 0) + r['allPatches']
        if len([a for a in an if a[3] == 'topo-breathe']) != nt: fails.append(f'{pid} {label}: {len([a for a in an if a[3] == "topo-breathe"])} drawings breathe, the page has {nt} (P93 follow-up)')
        if len(tp) != nt: fails.append(f'{pid} {label}: {len(tp)} contour drawings move, the page has {nt}')
        # each drawing at its own point of the cycle: the phases build.py gives (--ph), at least 0.9 / n apart for the n
        # drawings of the page (P93 follow-up: at a 10 s sweep the measured progress also carried when each drawing was
        # first shown, a fifth of a second for the tiles in History's Planned list opened after the home, so the check
        # reads the phases themselves; the animations' running is checked above)
        phs = sorted(float(x['ph']) for x in ([h] if h else []) + r['patches'] if x.get('ph'))
        close = [(a, b) for a, b in zip(phs, phs[1:]) if b - a < .9 / max(nt, 1)]
        if phase and (close or len(phs) < len(r['patches']) + (1 if h else 0)): fails.append(f'{pid} {label}: drawings share or lack a phase ({close[:3]}; {len(phs)} phases)')
    elif an: fails.append(f'{pid} {label}: under reduced motion {len(an)} animations run: {an[:2]}')
    if want is None and pid != 'home' and r['anyTopo']: fails.append(f'{pid} {label}: a topography on a page that has none')
    return r

def check_tiles(pg, pid, label, fails, expect):
    """P93: every tile of a page the same fields and its own patch, against the sources: a history unit's tile (its
    modules as rises by their words, the modules written, in all and its hours) opens to its module rows; a markdown
    unit's (its sections by their words; sections, words, hours) links to its reading page, or its brief while it is not
    written; a planned course's ghost (the chip, the title, its scope, no stats, one dashed ring); one class set; a line
    of two lines at most while closed; one column below 768 px, two from it, a lone tile half the width; nothing past
    an edge, no sideways scroll."""
    r = pg.evaluate(TILES_JS, pid)
    w = pg.evaluate('innerWidth')
    fails += [f'{pid} {label}: {b}' for b in r['bad']]
    if r['scroll'][0] > r['scroll'][1]: fails.append(f'{pid} {label}: the page scrolls sideways {r["scroll"]}')
    ts = r['tiles']
    if len({t['cls'] for t in ts}) > 1: fails.append(f'{pid} {label}: the tiles are not one style: {sorted({t["cls"] for t in ts})}')
    for t in ts:
        nm = t['name']
        base = 'div.ctop span.ctitle p' + ('' if t['kind'] == 'ghost' else ' div.cstats') + ' div.topo.topo-patch' + (' svg.chev' if t['kind'] in ('disc', 'ghost') else '')
        if t['kids'] != base: fails.append(f'{pid} {label}: {nm}: the tile holds {t["kids"]}, expected {base}')
        if len(t['chip']) != 2: fails.append(f'{pid} {label}: {nm}: its chip has {len(t["chip"])} parts')
        if t['kind'] != 'ghost' and not t['pill']: fails.append(f'{pid} {label}: {nm}: no status pill')
        if t['kind'] != 'ghost' and len(t['stats']) != 3: fails.append(f'{pid} {label}: {nm}: {len(t["stats"])} stats, expected 3')
        if not t['open'] and t['lines'] > 2: fails.append(f'{pid} {label}: {nm}: its line runs to {t["lines"]} lines')
        if t['open'] and t['clipped']: fails.append(f'{pid} {label}: {nm}: opened, its line is still cut short')
        if t['aria'] != 'true': fails.append(f'{pid} {label}: {nm}: its patch is not aria-hidden')
        if not t['pin'] or abs(t['pw'] / max(t['ph'], 1) - 4) > .06: fails.append(f'{pid} {label}: {nm}: its patch is {t["pw"]} x {t["ph"]}, not 4:1 inside the tile')
        if t['sw']: fails.append(f'{pid} {label}: {nm}: the tile scrolls sideways')
        if t['unseen']: fails.append(f'{pid} {label}: {nm}: the written parts {t["unseen"]} draw no ring of their own (P93 check: a part under one level takes a spot ring)')
        if (t['kind'] == 'ghost') != ('ghost' in t['mods']): fails.append(f'{pid} {label}: {nm}: a ghost tile without the ghost class, or the reverse')
    for cols, n, lone, half in r['grids']:
        if w < 768 and cols != 1: fails.append(f'{pid} {label}: a tile grid in {cols} columns below 768 px')
        if w >= 768 and cols != 2: fails.append(f'{pid} {label}: a tile grid in {cols} column(s) from 768 px')
        if w >= 768 and lone is not None and abs(lone - half) > 2: fails.append(f'{pid} {label}: a lone tile {lone} px wide, half the grid is {half}')
    e = expect['courses'].get(pid)
    if e:
        units = [t for t in ts if t['kind'] in ('disc', 'link') or (t['kind'] == 'other')]
        if len(units) != len(e['tiles']): fails.append(f'{pid} {label}: {len(units)} unit tiles, the sources give {len(e["tiles"])} units')
        for t, (code, parts) in zip(units, e['tiles']):
            if e['family'] == 'history':
                want_r = [(m, wd) for m, wd in parts if wd]
                want_p = [m for m, wd in parts if wd is None]
                done = len(want_r)
                if t['kind'] != 'disc': fails.append(f'{pid} {label}: {code}: a history unit tile that is not a disclosure')
                if t['rows'] != len(parts): fails.append(f'{pid} {label}: {code}: {t["rows"]} module rows, {len(parts)} modules')
                if [x[0] for x in t['stats']] != [str(done), str(len(parts)), f'{sum(wd for _, wd in want_r) / 250 / 60:.1f}']: fails.append(f'{pid} {label}: {code}: its stats read {t["stats"]}')
            else:
                want_r = [(f'{code} §{j + 1}', wd) for j, wd in enumerate(parts or [])]
                want_p = [] if parts else [code]
                href = '#' + (e['pages'][code] if parts else e['briefs'][code])
                if t['kind'] != 'link' or t['href'] != href: fails.append(f'{pid} {label}: {code}: the tile links to {t["href"]}, expected {href}')
                ww = sum(parts or [])
                if [x[0] for x in t['stats']] != [str(len(parts or [])), f'{ww:,}', f'{ww / 250 / 60:.1f}']: fails.append(f'{pid} {label}: {code}: its stats read {t["stats"]}')
            if [tuple(x) for x in t['rises'] or []] != want_r: fails.append(f'{pid} {label}: {code}: its patch gives {t["rises"]}, the sources {want_r}')
            if ('pending' in t['mods']) != (not want_r): fails.append(f'{pid} {label}: {code}: marked pending {"pending" in t["mods"]}, but {len(want_r)} of its parts are written')
            if (t['plan'] or []) != want_p: fails.append(f'{pid} {label}: {code}: its patch marks {t["plan"]} planned, the sources {want_p}')
    if pid == 'home':
        gh = [t for t in ts if t['kind'] == 'ghost']
        plans = [n[1] for t in THEMES for n in (NEXT if t['id'] == 'history' else t.get('planned', []))]   # S-SPORTS: a track's own planned courses too
        if gh and [t['name'] for t in gh] != plans: fails.append(f'home {label}: the ghost tiles are {[t["name"] for t in gh]}, courses.py plans {plans}')
        for t in gh:
            if t['stats'] or t['rises'] or len(t['plan'] or []) != 1: fails.append(f'home {label}: the ghost {t["name"]} shows stats {t["stats"]} or rises, or not one dashed ring ({t["plan"]})')
    return r

# P91: What's new (#new), fetched through the shell: every dated unit and every course start once, newest first,
# grouped by day under the day's heading, each row linking to a page that exists, approximate dates marked
NEW_JS = r'''() => {
  const p = document.getElementById('new'), bad = [], out = {bad};
  const resolves = t => !!document.getElementById(t) || [...document.querySelectorAll('.panel[data-anchors]')].some(q => (' ' + q.getAttribute('data-anchors') + ' ').includes(' ' + t + ' '));
  const crumbs = p.querySelector('.hero .crumbs'), cr = crumbs ? [...crumbs.children].filter(e => !e.classList.contains('sep')).map(e => e.textContent).join(' › ') : '';
  if (cr !== "Academy › What's new") bad.push(`the breadcrumbs read "${cr}", not Academy › What's new`);
  if (!p.querySelector('.hero h1') || p.querySelector('.hero h1').textContent !== "What's new") bad.push('no "What\'s new" title');
  const days = [...p.querySelectorAll(':scope > section.newday')];
  out.days = days.map(d => d.getAttribute('data-day'));
  out.rows = [];
  days.forEach(d => { const day = d.getAttribute('data-day'), hd = d.querySelector(':scope > h2');
    if (!hd || !hd.textContent.trim()) bad.push(`the day ${day} has no heading`);
    d.querySelectorAll('a.hrow').forEach(r => { const t = r.getAttribute('data-target');
      out.rows.push([r.getAttribute('data-kind'), t, r.getAttribute('data-date'), r.hasAttribute('data-approx'), !!r.querySelector('.approx'), r.getAttribute('href') === '#' + t]);
      if (r.getAttribute('data-date') !== day) bad.push(`#${t} sits under ${day} but is dated ${r.getAttribute('data-date')}`);
      if (!resolves(t)) bad.push(`a row links to #${t}, no page`);
      if (!r.querySelector('.pill') || !r.querySelector('.t small')) bad.push(`#${t}: a row without its pill or its course and model line`); }); });
  if (new Set(out.days).size !== out.days.length) bad.push('a day appears twice');
  for (let i = 1; i < out.days.length; i++) if (out.days[i] >= out.days[i - 1]) { bad.push(`the days are not newest first (${out.days[i - 1]} then ${out.days[i]})`); break; }
  const de = document.documentElement; if (de.scrollWidth > de.clientWidth) bad.push(`the page scrolls sideways (${de.scrollWidth} in ${de.clientWidth} px)`);
  return out;
}'''

def check_new(pg, label, fails, expect):
    """P91: What's new against home_expect()'s rows: each once, in order, grouped by day, approximate dates marked."""
    pg.evaluate("location.hash = 'new'"); ready(pg); pg.wait_for_timeout(80)
    r = pg.evaluate(NEW_JS)
    fails += [f"what's new {label}: {b}" for b in r['bad']]
    got = [(k, t) for k, t, *_ in r['rows']]
    want = [(x['kind'], x['pid']) for x in expect['rows']]
    if len(set(got)) != len(got): fails.append(f"what's new {label}: a row appears twice")
    if got != want: fails.append(f"what's new {label}: {len(got)} rows, first {got[:4]}; the sources give {len(want)}, first {want[:4]}")
    ap = {x['pid'] for x in expect['rows'] if x['approx'] and x['kind'] == 'unit'}
    apc = {x['pid'] for x in expect['rows'] if x['approx'] and x['kind'] == 'course'}
    for k, t, d, da, mark, hr in r['rows']:
        if (t in (ap if k == 'unit' else apc)) != da: fails.append(f"what's new {label}: #{t} ({k}) marked approximate {da}, the sources say {not da}")
        if da != mark: fails.append(f"what's new {label}: #{t} carries data-approx {da} but its ≈ mark {mark}")
        if not hr: fails.append(f"what's new {label}: #{t}'s href is not its target")
    print(f"what's new {label}: {sum(1 for x in r['rows'] if x[0] == 'unit')} unit rows, {sum(1 for x in r['rows'] if x[0] == 'course')} course rows, "
          f"{sum(1 for x in r['rows'] if x[3])} approximate, on {len(r['days'])} days")

# P90: WCAG contrast of every text against the background it sits on, the light theme's tokens in use. A text's colour
# is composited with its alpha and the opacity of its ancestors; its background is every background colour under it
# (a tint over a card over the page) composited from the page up. SVG text (figures) is left out.
CONTRAST_JS = r'''(scope) => {
  const parse = c => {
    let m = c.match(/^rgba?\(([^)]+)\)/);
    if (m) { const v = m[1].split(/[\s,\/]+/).filter(Boolean).map(Number); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; }
    m = c.match(/^color\(srgb ([^)]+)\)/);
    if (m) { const v = m[1].split(/[\s\/]+/).filter(Boolean).map(Number); return [v[0] * 255, v[1] * 255, v[2] * 255, v.length > 3 ? v[3] : 1]; }
    return null; };
  const over = (a, b) => [0, 1, 2].map(i => a[i] * a[3] + b[i] * (1 - a[3])).concat([1]);
  const lum = c => { const f = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]); };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  const hex = c => '#' + c.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  const roots = [...document.querySelectorAll(scope)];
  const bad = []; let n = 0, min = 99, minAt = '';
  roots.forEach(root => root.querySelectorAll('*').forEach(el => {
    if (el.closest('svg')) return;
    if (![...el.childNodes].some(t => t.nodeType === 3 && t.textContent.trim())) return;
    const cs = getComputedStyle(el); if (cs.visibility !== 'visible') return;
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return;
    if (el.closest('[disabled]')) return;
    let fg = parse(cs.color); if (!fg) return;
    let op = 1, bgs = [];
    for (let e = el; e; e = e.parentElement) {
      const s = getComputedStyle(e); op *= parseFloat(s.opacity);
      const b = parse(s.backgroundColor); if (b && b[3] > 0) { bgs.push(b); if (b[3] >= 1) break; }
    }
    let bg = [255, 255, 255, 1];
    for (let i = bgs.length - 1; i >= 0; i--) bg = i === bgs.length - 1 && bgs[i][3] >= 1 ? bgs[i] : over(bgs[i], bg);
    const col = over([fg[0], fg[1], fg[2], fg[3] * op], bg);
    const size = parseFloat(cs.fontSize), large = size >= 24 || (size >= 18.66 && parseInt(cs.fontWeight) >= 700);
    const k = ratio(col, bg), need = large ? 3 : 4.5; n++;
    const d = el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/).join('.') : '');
    if (k < min) { min = k; minAt = d; }
    if (k < need - 0.005) bad.push(`${d} "${el.textContent.trim().slice(0, 24)}" ${hex(col)} on ${hex(bg)} ${k.toFixed(2)}:1`);
    if (fg[0] > 254.5 && fg[1] > 254.5 && fg[2] > 254.5) bad.push(`${d} "${el.textContent.trim().slice(0, 24)}" is pure white text (P90: none in light)`);
    if (bgs.some(c => c[0] > 254.5 && c[1] > 254.5 && c[2] > 254.5 && c[3] > 0)) bad.push(`${d} "${el.textContent.trim().slice(0, 24)}" sits on pure white (P90: none in light)`);
  }));
  return {n, min: Math.round(min * 100) / 100, minAt, bad: [...new Set(bad)].slice(0, 12), nbad: new Set(bad).size};
}'''

def check_contrast(pg, fails):
    """P90: the light theme's contrast on the home, the drawer, the changelog and backlog, each course home and the
    first reading page of each course, at phone width, every <details> open."""
    pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')"); pg.wait_for_timeout(50)
    firsts = pg.evaluate("""() => { const seen = {}, out = []; document.querySelectorAll('.panel[data-kind="report"]').forEach(p => {
      const c = p.getAttribute('data-ctx'); if (!seen[c]) { seen[c] = 1; out.push(p.id); } }); return out; }""")
    homes = pg.evaluate("[...document.querySelectorAll('.panel[data-kind=\"course\"]')].map(p => p.id)")
    pids = [x for x in ['home', 'new', 'changelog', 'backlog'] if x not in OMIT] + homes + firsts   # P91: What's new
    worst, total = [99, ''], 0
    for pid in pids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(40)
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) .stepbar .whole[aria-pressed=\"false\"]').forEach(b => b.click())")
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) details').forEach(d => d.open = true)"); pg.wait_for_timeout(40)
        r = pg.evaluate(CONTRAST_JS, f'#{pid}')
        total += r['n']
        if r['min'] < worst[0]: worst = [r['min'], f'{pid} {r["minAt"]}']
        if r['nbad']: fails.append(f'contrast light {pid}: {r["nbad"]} texts under 4.5:1 (3:1 large): ' + '; '.join(r['bad']))
    pg.click('#menuB'); pg.wait_for_timeout(250)
    pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed')); document.querySelectorAll('#drawer details').forEach(d => d.open = true)")
    r = pg.evaluate(CONTRAST_JS, '#drawer'); total += r['n']
    if r['min'] < worst[0]: worst = [r['min'], f'drawer {r["minAt"]}']
    if r['nbad']: fails.append(f'contrast light drawer: {r["nbad"]} texts under 4.5:1: ' + '; '.join(r['bad']))
    pg.click('#closeB'); pg.wait_for_timeout(250)
    pg.evaluate("localStorage.removeItem('hellas-theme'); document.documentElement.removeAttribute('data-theme')")
    print(f'contrast (light, phone): {total} texts on {len(pids)} panels and the drawer, lowest {worst[0]}:1 ({worst[1]})')

SHOT_H = 2600
def shoot(pg, path, w, h):
    """The top SHOT_H px of the page (P35, 1 Nov 2026). A full-page capture renders the whole document before it clips,
    which on a long unit at device scale 3 took 80 s (DD-B3, about 10,300 words) and failed past the timeout on longer
    pages; the viewport is made SHOT_H tall and captured as it is, then put back, so the time no longer grows with the
    page."""
    pg.set_viewport_size({'width': w, 'height': SHOT_H}); pg.wait_for_timeout(120)
    pg.screenshot(path=str(path), full_page=False, timeout=60000)
    pg.set_viewport_size({'width': w, 'height': h}); pg.wait_for_timeout(60)

def frames(pg, fig, path, label):
    """P89 (2 Nov 2026; p85_frames.py folded in): every frame a reader scrolls a figure across, shot in turn and stacked
    top to bottom with its number, so a checker sees the whole drawing as the reader meets it. The frames run from where
    the drawing starts (data-x0px, set by shell.js on a centred drawing, else 0) to its right edge, each half a frame
    on from the last, so anything up to half a frame wide (a box, a label) is whole in at least one frame, as it is to a
    reader who scrolls on; a figure that fits its frame is one frame. While they are shot,
    sticky bars are made static (they keep their place in the flow) and fixed ones hidden, so none covers the figure;
    both are put back after and the frame is scrolled back to where it opened. Returns the number of frames."""
    from PIL import Image, ImageDraw, ImageFont
    sc = fig.query_selector('.viz-scroll')
    if not sc:
        return 0
    pg.evaluate("""() => { for (const el of document.querySelectorAll('body *')) { const p = getComputedStyle(el).position;
      if (p === 'sticky' && !el.closest('.viz-scroll')) { el.dataset.p89 = 's'; el.style.setProperty('position', 'static', 'important'); }   // P83: a figure's own label column stays sticky, so the sheets show it as the reader sees it
      else if (p === 'fixed') { el.dataset.p89 = 'f'; el.style.setProperty('visibility', 'hidden', 'important'); } } }""")
    fig.scroll_into_view_if_needed(); pg.wait_for_timeout(60)
    sw, cw, x_open, x0 = sc.evaluate("s => [s.scrollWidth, s.clientWidth, s.scrollLeft, +s.getAttribute('data-x0px') || 0]")
    x, xs, shots = min(x0, x_open), [], []
    # W-BW8 (16 Nov 2026): beside a sticky label column (and its 36 px fades) the clear room is narrower than the frame; the
    # step is a third of that room, so a matrix column up to two thirds of it is clear of both fades in at least one frame
    # (BW8 figure 4's Desktop column was under a fade in every half-frame stop at 360 and 390 px)
    stick = sc.evaluate("s => { for (const e of s.children) if (e.matches('.viz-stick,.viz-stickn') && getComputedStyle(e).display !== 'none') return e.getBoundingClientRect().width; return 0; }")
    step = max(cw // 2, 1) if not stick else max((cw - int(stick) - 72) // 3, 16)
    while True:
        sc.evaluate(f's => {{ s.scrollLeft = {x}; }}'); pg.wait_for_timeout(120)
        x = sc.evaluate('s => s.scrollLeft'); xs.append(x)
        tmp = path.with_name(f'_{path.stem}-{len(shots)}.png')
        fig.screenshot(path=str(tmp), timeout=120000); shots.append(tmp)
        if x + cw >= sw - 1 or len(shots) >= 60:
            break
        x = min(x + step, sw - cw)
    sc.evaluate(f's => {{ s.scrollLeft = {x_open}; }}')
    pg.evaluate("() => { for (const el of document.querySelectorAll('[data-p89]')) { el.style.removeProperty(el.dataset.p89 === 's' ? 'position' : 'visibility'); delete el.dataset.p89; } }")
    ims = [Image.open(s) for s in shots]
    scale = max(1, round(ims[0].width / fig.evaluate('f => f.getBoundingClientRect().width')))   # the device scale
    font, band = ImageFont.load_default(size=12 * scale), 40 * scale
    sheet = Image.new('RGB', (max(i.width for i in ims), sum(i.height + band for i in ims)), (128, 128, 128))
    d, y, n = ImageDraw.Draw(sheet), 0, len(ims)
    for k, (im, xk) in enumerate(zip(ims, xs)):
        note = 'the whole figure fits' if n == 1 else f'scrolled to {xk} of {sw - cw} px; opens at {x_open}'
        d.text((6 * scale, y + 4 * scale), label, fill=(0, 0, 0), font=font)
        d.text((6 * scale, y + 21 * scale), f'frame {k + 1} of {n} ({note})', fill=(0, 0, 0), font=font)
        y += band; sheet.paste(im, (0, y)); y += im.height
    sheet.save(path)
    for s in shots:
        s.unlink()
    return n

def check_panels(pg, label, fails):
    """Every panel, every <details> open: horizontal scroll, 6 px gaps, 44 px targets. Returns (tightest gap, panel count)."""
    ids = pg.eval_on_selector_all('.panel', 'ps => ps.map(p => p.id)')
    worst, frames, figs = [], [0, 0], [0, 0]
    for pid in ids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(30)
        if pg.evaluate(f"document.getElementById('{pid}').hasAttribute('data-failed')"): fails.append(f'{label} {pid}: the report did not load')
        # P68: a reading page is measured whole (its "Whole unit" toggle), so every section is checked as before
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) .stepbar .whole[aria-pressed=\"false\"]').forEach(b => b.click())")
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) details').forEach(d => d.open = true)")
        sw = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.clientWidth]')
        if sw[0] > sw[1]: fails.append(f'{label} {pid}: horizontal scroll {sw}')
        res = pg.evaluate(BOX_JS, [f'#{pid}', GAP])
        if res['nbad']: fails.append(f'{label} {pid}: {res["nbad"]} boxes closer than {GAP}px: ' + '; '.join(res['bad']))
        if label.startswith('phone') or label == 'desktop':
            fr = pg.evaluate(FRAME_JS, [f'#{pid}', label.startswith('phone')])
            frames[0] += fr['n']; frames[1] += fr['over']
            if fr['bad']: fails.append(f'{label} {pid}: figure frames: ' + '; '.join(fr['bad']))
        if label == 'phone':   # P55: the figure geometry (FIG_JS) of every figure on every panel, once (it does not depend on the width)
            fg = pg.evaluate(FIG_JS, f'#{pid}')
            figs[0] += fg['n']; figs[1] += fg['n'] > 0
            if fg['bad']: fails.append(f'{label} {pid}: figure geometry: ' + '; '.join(fg['bad'][:8]))
        small = pg.evaluate(TARGET_JS, f'#{pid}')
        if small: fails.append(f'{label} {pid}: {len(small)} targets under 44px: ' + '; '.join(small[:6]))
        worst.append((res['min'], pid, res['n']))
    m = min(worst)
    print(f'{label}: panels checked: {len(ids)}; tightest stacked gap {m[0]}px ({m[1]})'
          + (f'; {frames[0]} figure frames at natural size, {frames[1]} scrolling with the cue' + (f'; geometry of {figs[0]} figures on {figs[1]} panels checked' if label == 'phone' else '') if label.startswith('phone') else
             f'; {frames[0]} figure frames, {frames[1]} wider than their frame with the cue, the rest without' if label == 'desktop' else ''))
    return m[0], len(ids)

FONTS = R / 'fonts'
FONT_CSS = (FONTS / 'fonts.css').read_text()
def font_file(route):
    f = FONTS / route.request.url.rsplit('/', 1)[1]
    if '/learning-vendored/' in route.request.url and f.suffix == '.woff2' and f.exists():
        route.fulfill(status=200, content_type='font/woff2', body=f.read_bytes(), headers={'Access-Control-Allow-Origin': '*'})
    else:
        route.abort()

def new_page(p, br, errors, name, w, h, mobile, motion=False):
    ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=3 if mobile else 1,
                         is_mobile=mobile, has_touch=mobile,  # a real phone or tablet honours the viewport tag
                         color_scheme='dark',                 # P92: the site's default theme; a pass without the toggle is dark (Playwright's default system setting is light, so every 'dark' pass before P92 measured the light theme)
                         reduced_motion='no-preference' if motion else 'reduce')   # P91: every measure and shot sees the home at rest; P92: one pass with motion allowed
    # the theme fonts, from the vendored copy in fonts/ (P39): the page measures and draws what a reader's phone does
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
    ctx.route('**/fonts.gstatic.com/**', font_file)
    pg = ctx.new_page()
    pg.on('console', lambda m: errors.append(f'{name}: {m.text}') if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errors.append(f'{name}: {e}'))
    pg.goto(URL + '#home'); pg.wait_for_timeout(300)
    lay = pg.evaluate('[document.documentElement.clientWidth, visualViewport.scale]')
    return ctx, pg, lay

def check_files(fails):
    """The split on disk: every stub's file exists, nothing in academy/ is unreferenced, the shell is under 1 MB, and
    README.md's size table is the one build.py would write for these files."""
    shell = (SITE / 'index.html').read_text()
    heads = re.findall(r'<section class="panel[^"]*"[^>]*>', shell)
    srcs = [m.group(1) for h in heads for m in [re.search(r' data-src="([^"]+)"', h)] if m]
    # every report and syllabus panel, a markdown course's briefs and bibliography pages, every course home (P22 the
    # history homes; P93 the markdown ones, whose unit tiles and topography would have filled the shell) and every
    # course's "How it was built" page leave the shell (A2, P20, P22, A4, P93)
    must = [h for h in heads if ' data-kind="report"' in h or ' data-kind="syllabus"' in h or re.search(r' id="(briefs-[a-z]+|[a-z-]+-briefs|[a-z-]+-bibliography|[a-z-]+-built)"', h)
            or ' data-kind="course"' in h or ' id="viz-examples"' in h or ' id="new"' in h or ' id="changelog"' in h]   # G-0: the changelog too   # P91: What's new is fetched too; P93: every course home, a markdown course's too
    kept = [h[:80] for h in must if ' data-src="' not in h]
    if kept: fails.append(f'split: {len(kept)} panels should be fetched but are in the shell: {kept[:2]}')
    if len(srcs) != len(must): fails.append(f'split: {len(must)} panels should be fetched but {len(srcs)} carry data-src')
    noanch = [h[:80] for h in must if ' data-src="' in h and ' data-kind="report"' not in h and ' data-anchors="' not in h]
    if noanch: fails.append(f'split: fetched panels without data-anchors: {noanch[:2]}')
    stubs = re.findall(r'(<section class="panel[^"]*"[^>]* data-src="[^"]+"[^>]*>)(.*?)</section>', shell, re.S)
    for h in heads:                                          # P24 (16 Nov 2026): every How-it-was-built page says its audit files are private
        m = re.search(r' id="([a-z0-9-]+-built)"[^>]* data-src="([^"]+)"', h)
        if m and (SITE / m.group(2)).exists():
            pg = (SITE / m.group(2)).read_text(); i, j = pg.find('data-private=""'), pg.find('https://github.com/')
            if i < 0 or (j >= 0 and j < i):
                fails.append(f'{m.group(1)}: no line saying its audit files are private above its first file link (P24)')
    full = [h for h, body in stubs if body.strip()]
    if full: fails.append(f'split: {len(full)} stubs still hold content: {full[0][:80]}')
    on_disk = sorted(str(f.relative_to(SITE)) for f in SITE.rglob('*.html') if f.name != 'index.html')
    missing = sorted(set(srcs) - set(on_disk)); orphans = sorted(set(on_disk) - set(srcs))
    if missing: fails.append(f'split: {len(missing)} fetched files missing: {missing[:3]}')
    if orphans: fails.append(f'split: {len(orphans)} files in academy/ no stub fetches: {orphans[:3]}')
    if any(re.search(r'<(style|script|html|body)\b', (SITE / x).read_text(), re.I) for x in on_disk): fails.append('split: a fetched file carries a style, script or document tag')
    size = len(shell.encode())
    if size >= SHELL_MAX: fails.append(f'split: shell is {size:,} bytes, over the 1 MB limit')
    by = {}
    for x in on_disk:
        by.setdefault(x.split('/')[0] if '/' in x else '.', []).append((len((SITE / x).read_bytes()), x))   # V1: root pages under ./
    table = re.search(r'<!-- sizes:start -->\n(.*?)<!-- sizes:end -->', (R / 'README.md').read_text(), re.S) if EDITION == 'academy' else True
    kb = lambda n: f'{n / 1024:,.0f} KB' if n < 1024 * 1024 else f'{n / 1024 / 1024:.2f} MB'
    if not table: fails.append('README.md has no size table (sizes:start/sizes:end)')
    elif table is True: print(f'edition {EDITION}: no size table (README.md keeps the full Academy\'s)')
    else:
        rows = {r.split(' | ')[0].strip('| '): r for r in table.group(1).splitlines()}
        want = {'Shell (`index.html`)': f'| 1 | {kb(size)} | {kb(size)} |'}
        for ctx, fs in by.items():
            want[next((k for k in rows if f'(`{ctx}/`)' in k), ctx)] = f'| {len(fs)} | {kb(sum(n for n, _ in fs))} | {kb(max(fs)[0])} | largest `{max(fs)[1]}`'
        bad = [k for k, v in want.items() if k not in rows or v not in rows[k]]
        if bad: fails.append(f'README.md size table does not match the files: {bad} (rebuild)')
    vx = SITE / 'viz-examples.html'   # V1: the figure examples page, one figure of every kind in viz.py
    if 'figures' in OMIT:
        if vx.exists(): fails.append(f'edition {EDITION}: viz-examples.html is built though the edition leaves it out')
    elif not vx.exists(): fails.append('viz-examples.html: missing (viz_examples.py, run from build.py)')
    else:
        nfig = len(re.findall(r'<figure class="viz ', vx.read_text()))
        if nfig != VX_FIGS: fails.append(f'viz-examples.html: {nfig} figures, expected {VX_FIGS}')
        print(f'viz-examples.html: {nfig} figures')
    big = max((n, x) for fs in by.values() for n, x in fs)
    print(f'split: shell {size / 1024:,.0f} KB (limit 1,024 KB), {len(on_disk)} fetched files in {len(by)} folders, largest {big[1]} {big[0] / 1024:,.0f} KB')
    for ctx, fs in by.items():
        print(f'  {ctx + "/":10} {len(fs):3} files {sum(n for n, _ in fs) / 1024:7,.0f} KB, largest {max(fs)[1]} {max(fs)[0] / 1024:,.0f} KB')

# P58 (30 Oct 2026): the drawing faults the Greek retrofit's checkers met, read from every built figure on every page
# (the shell and each fetched file), so a figure that would show one fails the build. See viz.py's P58 contract.
QUAL = re.compile(r'(?:^|[\s(\[])(c\.|ca\.|by|after|before|from|until)$', re.I)
TEXT_RE = re.compile(r'<text class="([\w-]+)" x="([-\d.]+)" y="([-\d.]+)"[^>]*>(.*?)</text>', re.S)
def _texts(svg):
    import html as H
    return [(m.group(1), float(m.group(2)), float(m.group(3)), H.unescape(re.sub(r'<[^>]+>', '', m.group(4)))) for m in TEXT_RE.finditer(svg)]
def _year(t):
    """A tick label as a signed year (P63): 750 BC or 750 BCE is -750, AD 14 or 14 CE is 14, 1453 is 1453."""
    m = re.fullmatch(r'(\d+) (BC|BCE)', t.strip()) or re.fullmatch(r'(?:AD )?(\d+)(?: CE)?', t.strip())
    return None if not m else -int(m.group(1)) if m.re.pattern.endswith('BCE)') else int(m.group(1))
PHONE_FRAME = 358                                      # P79: a 390 px phone's figure frame (16 px gutters)
def figure_rules(page, name):
    """The P58 faults (and P63's date lines) in one built page's figures, as messages (empty when it has none)."""
    import html as H
    bad, n = [], 0
    prose = re.sub(r'<figure class="viz.*?</figure>', '', page, flags=re.S)
    prose = re.sub(r'<div class="process">.*?<div class="pager">', '', prose, flags=re.S)   # P68: the text, not its sources
    bce = len(re.findall(r'\bBCE\b', prose)) > len(re.findall(r'\bBC\b', prose))
    for m in re.finditer(r'<figure class="viz viz-([\w-]+)[^"]*">(.*?)</figure>', page, re.S):
        kind, svg = m.group(1), m.group(2); n += 1
        where, tx = f'{name} figure {n} ({kind})', _texts(svg)
        if kind == 'timeline':
            for (c1, x1, y1, t1), (c2, x2, y2, t2) in zip(tx, tx[1:]):
                if c1 == c2 == 'viz-label' and x1 == x2 and 0 < y2 - y1 < 20 and QUAL.search(t1) and re.match(r'[(\[]?\d', t2):
                    bad.append(f'{where}: a wrapped event label parts "{t1.split()[-1]}" from its number ("{t1}" / "{t2}")')
            for i, (c, x, y, t) in enumerate(tx):
                if c != 'viz-date':
                    continue
                lab = ' '.join(t2 for c2, x2, y2, t2 in tx[i + 1:i + 8] if c2 == 'viz-label' and x2 == x and 0 < y2 - y < 100)
                if any(g.group(1) in t and 'c.' not in t for g in re.finditer(r'\bc\.\s?(\d+)', lab)):
                    bad.append(f'{where}: the date line "{t}" drops the "c." its label keeps ("{lab}"): give the event "date"')
                if re.search(r'\(c\.\)|\(date approx', lab) and 'c.' not in t:
                    bad.append(f'{where}: the label "{lab}" marks its date approximate because the date line cannot: give the event "date"')
                if any(g.group(1) in t and '/' not in t for g in re.finditer(r'\b(\d+)/(\d+)', lab)):
                    bad.append(f'{where}: the date line "{t}" drops the split year its label keeps ("{lab}"): give the event "date"')
            # P63 (1 Nov 2026): a date line names the year its dot stands at (read from the tick labels), or a century or
            # span of years that contains it; the year is never printed where the text gives only a century.
            ticks = [(x, _year(t)) for c, x, y, t in tx if c == 'viz-ticklabel' and _year(t) is not None]
            if len({x for x, _ in ticks}) >= 2:
                (xa, ya), (xb, yb) = ticks[0], ticks[-1]
                for cx, t in re.findall(r'<circle class="viz-dot[^"]*" cx="([-\d.]+)"[^>]*/>\s*<text class="viz-date"[^>]*>(.*?)</text>', svg):
                    at = ya + (float(cx) - xa) * (yb - ya) / (xb - xa)
                    t = H.unescape(re.sub(r'<[^>]+>', '', t))
                    if not any(viz.date_names(t, round(at) + k) for k in (-1, 0, 1) if round(at) + k):
                        bad.append(f'{where}: the date line "{t}" names neither the year its dot stands at ({round(at)}) nor a century or span that contains it')
        if kind == 'timeline' and 'viz-span ' in svg:         # P84 (16 Nov 2026): a span is a period on the axis, not a key
            ax = re.search(r'<line class="viz-axis" x1="[-\d.]+" y1="([-\d.]+)"', svg)
            guides = [(float(a), float(b)) for a, b in re.findall(r'<line class="viz-spanend" x1="([-\d.]+)" y1="[-\d.]+" x2="[-\d.]+" y2="([-\d.]+)"', svg)]
            groups = re.findall(r'<g data-span="(-?\d+) (-?\d+)" data-text="([^"]*)">(.*?)</g></g>', svg, re.S)
            if len(groups) != svg.count('class="viz-span '):
                bad.append(f'{where}: a span drawn without its data-span group (rebuild with the P84 viz.py)')
            for a, b, want, inner in groups:
                got = ' '.join(t for c, x, y, t in _texts(inner) if c in ('viz-spanlabel', 'viz-spanside'))
                if got != H.unescape(want):
                    bad.append(f'{where}: the span {a} to {b} is labelled {got!r}, not {H.unescape(want)!r}')
                if not viz.span_names(got, a, b):
                    bad.append(f'{where}: the span label {got!r} does not carry its years ({a} to {b})')
                r = re.search(r'<rect class="viz-span[^"]*" x="([-\d.]+)" y="[-\d.]+" width="([-\d.]+)"', inner)
                x1, x2 = float(r.group(1)), float(r.group(1)) + float(r.group(2))
                for gx in (x1, x2):
                    if not ax or not any(abs(g - gx) < 2 and abs(y2 - float(ax.group(1))) < 0.2 for g, y2 in guides):   # round 2: an abutting bar stops 1.5 short of its guide
                        bad.append(f'{where}: the span {got!r} has no guide from its end at {gx:.0f} to the axis')
        if kind == 'timeline':                               # P58 (by eye): no stem runs through another event's text
            import viz as V
            stems = [(float(a), float(b), float(c)) for a, b, c in re.findall(r'<line class="viz-stem" x1="([-\d.]+)" y1="([-\d.]+)" x2="[-\d.]+" y2="([-\d.]+)"', svg)]
            for c, x, y, a, t in re.findall(r'<text class="viz-(label|date)" x="([-\d.]+)" y="([-\d.]+)" text-anchor="(\w+)">(.*?)</text>', svg):
                x, y, t = float(x), float(y), H.unescape(re.sub(r'<[^>]+>', '', t))
                w = V._tw(t, 12, 'sans') if c == 'label' else V._tw(t, 10.5, 'mono')
                x0 = {'start': x, 'middle': x - w / 2, 'end': x - w}[a]
                if any(x0 + 1 < sx < x0 + w - 1 and y1 < y - 4 < y2 for sx, y1, y2 in stems):
                    bad.append(f'{where}: a stem runs through the text "{t}"')
        if kind == 'tree':                                   # P79: a tree wider than its phone frame opens on its root
            wv = float(re.search(r'viewBox="0 0 ([\d.]+)', svg).group(1))
            if wv > PHONE_FRAME:
                nodes = [tuple(map(float, r)) for r in re.findall(r'<rect class="viz-node[^"]*" x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)"', svg)]
                rx, ry, rw = min(nodes, key=lambda r: (r[1], r[0]))
                x0 = re.search(r'<svg [^>]*?data-x0="([\d.]+)"', svg); xr = re.search(r'<svg [^>]*?data-xr="([\d.]+)"', svg)
                at = min(wv - PHONE_FRAME, max(0, float(x0.group(1)) - 12 if x0 else 0, float(xr.group(1)) - PHONE_FRAME if xr else 0))
                if not (at - 0.5 <= rx and rx + rw <= at + PHONE_FRAME + 0.5):
                    bad.append(f'{where}: a {wv:.0f}-unit tree opens its {PHONE_FRAME}-unit phone frame at {at:.0f}, but its root box spans '
                               f'{rx:.0f} to {rx + rw:.0f}: the first screen shows no root (P79: data-xr)')
                elif not any(at < x + w and x < at + PHONE_FRAME for x, y, w in nodes if y > ry):
                    bad.append(f'{where}: the phone frame opens on the root alone, with no box of a lower level in view')
        if kind in viz.X0_KINDS:                             # P50: a centred drawing names where it starts
            lft, x0 = viz._left(svg), re.search(r'<svg [^>]*?data-x0="([\d.]+)"', svg)
            if lft is not None and lft - 8 > 12 and (not x0 or abs(float(x0.group(1)) - (lft - 8)) > 2):
                bad.append(f'{where}: the drawing starts at {lft:.0f} but the svg ' + (f'names data-x0="{x0.group(1)}"' if x0 else 'carries no data-x0') + ', so a phone frame opens on the margin')
        if bce and kind in ('timeline', 'range') and any(c in ('viz-date', 'viz-ticklabel', 'viz-value') and re.search(r'\b(BC|AD)\b', t) for c, x, y, t in tx):
            bad.append(f'{where}: BC/AD in a figure on a page whose prose writes BCE/CE: set "era": "BCE"')
        if kind == 'range':
            rows = re.split(r'<g data-row="\d+">', svg)[1:]
            if not rows:
                bad.append(f'{where}: a range drawn without its rows (rebuild with the P58 viz.py)')
            for r in rows:
                vals = [t.split(' · ')[0] for c, x, y, t in _texts(r) if c == 'viz-value']
                dup = sorted({v for v in vals if vals.count(v) > 1})
                if dup:
                    bad.append(f'{where}: one range row prints {dup[0]!r} {vals.count(dup[0])} times')
            for e in re.finditer(r'<g data-end="([-\d.]+)"><g data-box=""><rect class="viz-lblbg" x="([-\d.]+)" y="[-\d.]+" width="([-\d.]+)"', svg):
                ex, px, pw = map(float, e.groups())
                if not px - 0.6 <= ex <= px + pw + 0.6:
                    bad.append(f'{where}: a range end label ({px:.0f} to {px + pw:.0f}) does not sit under its end at {ex:.0f}')
            bad += [f'{where}: "{t}": a word unit takes the singular for 1' for c, x, y, t in tx if c == 'viz-value' and re.match(r'1 [a-z]*[^s]s\b', t)]
        if kind == 'objects':
            if svg.count('class="viz-lblbg"') != len(re.findall(r'<g data-box="" data-text=', svg)):
                bad.append(f'{where}: a link label drawn without its data-text, so its lines cannot be checked (rebuild with the P58 viz.py)')
            for g in re.finditer(r'<g data-box="" data-text="([^"]*)">(.*?)</g>', svg, re.S):
                want = ' '.join(H.unescape(g.group(1)).split())
                got = ' '.join(t for c, x, y, t in _texts(g.group(2)) if c == 'viz-linklabel')
                if ' '.join(got.split()) != want:
                    bad.append(f'{where}: the link label {want!r} is cut across lines as {got!r}')
        if kind == 'tree':
            vb = re.search(r'viewBox="0 0 ([\d.]+) ', svg)
            xs = [(float(a), float(w)) for a, w in re.findall(r'<rect class="viz-node[^"]*" x="([-\d.]+)" y="[-\d.]+" width="([\d.]+)"', svg)]
            if vb and xs:
                W_, lo, hi = float(vb.group(1)), min(a for a, w in xs), max(a + w for a, w in xs)
                if hi - lo < W_ - 24 and abs(lo - (W_ - hi)) > 1.5:
                    bad.append(f'{where}: a narrow tree is not centred (margins {lo:.0f} and {W_ - hi:.0f})')
    return bad, n
def check_viz_keys(fails):
    """P52 (1 Nov 2026): every ```viz block in the vault of each markdown course, every figure declaration in a history
    report, every course home figure in courses.py and every block on the examples page carries only the keys
    viz.VIZ_KEYS documents for its kind (a typo or an undocumented key is a figure that does not draw what it says),
    and rendering a block leaves it as it was (viz.render works on a copy)."""
    bad, n = [], 0
    def one(where, d, kind=None):
        nonlocal n
        n += 1
        if kind: d.setdefault('kind', kind)
        bad.extend(f'{where}: {b}' for b in viz.check_keys(d))
    for c in COURSES:
        if (R.parent / c['vault']).is_dir():     # P71-3: a history course's reports are vault Markdown too
            for f in sorted((R.parent / c['vault']).glob('*.md')):
                for i, m in enumerate(viz._FENCE.finditer(f.read_text()), 1):
                    one(f'{c["vault"]}/{f.name} block {i}', json.loads(m.group(1)))
        if c.get('figure'): one(f'courses.py {c["id"]} figure', json.loads(json.dumps(c['figure'])))
    for key, *_, block in viz_examples.EXAMPLES + [(k, w, b) for k, w, b in viz_examples.CASES]:
        before = json.dumps(block, sort_keys=True)
        one(f'viz-examples {key}', json.loads(before)); viz.render(block)
        if json.dumps(block, sort_keys=True) != before: bad.append(f'viz-examples {key}: viz.render changed the block it was given')
    fails += ['figure keys: ' + b for b in bad[:20]]
    print(f'figure keys (P52): {n} blocks read, {len(bad)} undocumented keys')

def check_notes(fails):
    """P73 (1 Nov 2026): a markdown unit's text before its first heading is read at the end, in its own closed accordion,
    "The writer's opening note" (#<pid>-note), between Sources and "How this unit was made": present, closed and
    holding that text on every unit that has an opening, absent on one that has none; section 1 no longer carries it."""
    import mdcourse
    bad, have, none = [], 0, 0
    for c in COURSES:
        if c['family'] != 'markdown' or not (R.parent / c['vault']).is_dir(): continue
        for f in sorted((R.parent / c['vault']).glob('*.md')):
            src = f.read_text()
            m = re.match(r'---\n(.*?)\n---\n', src, re.S)
            if not m: continue
            code = re.search(r'^code:\s*(\S+)', m.group(1), re.M)
            if not code: continue
            built = list(SITE.glob(f'*/read-{code.group(1).lower()}.html'))
            if not built: continue
            pid, page = 'read-' + code.group(1).lower(), built[0].read_text()
            opening = re.sub(r'^#\s.*$', '', src[m.end():].split('\n## ', 1)[0], flags=re.M).strip()
            words = ' '.join(re.sub(r'[*_`\[\]()]', '', opening).split()[:6])
            note = re.search(rf'<details class="acc note"( open)? id="{pid}-note">(.*?)</details>', page, re.S)
            order = [x for x in re.findall(r'<details class="acc (src|note|made)"', page)]
            if opening:
                have += 1
                if not note: bad.append(f'{pid}: the opening note is missing'); continue
                if note.group(1): bad.append(f'{pid}: the opening note is open by default')
                if order != ['src', 'note', 'made']: bad.append(f'{pid}: the accordions run {order}, expected Sources, the note, How this unit was made')
                body = re.sub(r'<[^>]+>', '', note.group(2))
                if words and ' '.join(re.sub(r'[*_`\[\]()]', '', H.unescape(body)).split()).find(words.split()[0]) < 0:
                    bad.append(f'{pid}: the opening note does not hold the unit\'s opening ("{words}…")')
                sec0 = re.search(r'<section class="sec" data-step="0">(.*?)</section>', page, re.S)
                if sec0 and not sec0.group(1).lstrip().startswith('<h2'):
                    bad.append(f'{pid}: section 1 still opens on text before its heading')
            else:
                none += 1
                if note: bad.append(f'{pid}: an opening note on a unit with no opening')
    fails += ['opening note: ' + b for b in bad]
    print(f'opening notes (P73): {have} units with an opening, each with its closed note after Sources; {none} without, none shown')

def check_figure_rules(fails):
    bad, n = [], 0
    for f in [SITE / 'index.html'] + sorted(x for x in SITE.rglob('*.html') if x.name != 'index.html'):
        b, k = figure_rules(f.read_text(), str(f.relative_to(SITE))); bad += b; n += k
    fails += ["figure rules: " + b for b in bad[:20]]
    print(f'figure rules (P58): {n} built figures read, {len(bad)} faults')

# P56 (30 Oct 2026): a link into an unopened panel lands once the fetch is in and the shell has scrolled to the anchor,
# which can take longer than a fixed wait (#s-m23 once measured at top 7319, then passed on a re-run). SETTLE_JS waits,
# frame by frame for up to 3 s, until the anchor's top has held still for 5 frames inside the landing band (-5..200),
# and returns [panel, found, top]; fresh_land() measures that way and, if it is still off, reloads and measures once more.
SETTLE_JS = '''async (id) => { let last = null, same = 0; const t0 = performance.now();
  while (performance.now() - t0 < 3000) { await new Promise(r => requestAnimationFrame(r));
    const el = document.getElementById(id), t = el ? Math.round(el.getBoundingClientRect().top) : null;
    same = (t !== null && t === last) ? same + 1 : 0; last = t;
    if (same >= 5 && t >= -5 && t <= 200) break; }
  const el = document.getElementById(id), p = [...document.querySelectorAll('.panel')].find(p => !p.hidden);
  return [p && p.id, !!el, el ? Math.round(el.getBoundingClientRect().top) : null]; }'''

def fresh_land(pg, h, retried):
    """Open URL#h on a fresh load and return [visible panel, anchor found, anchor top] once the anchor has settled;
    one retry (a second fresh load) when it has not landed, recorded in retried."""
    for attempt in (0, 1):
        pg.goto(URL + '#' + h); pg.reload(); ready(pg)
        sec = pg.evaluate(SETTLE_JS, h)
        if sec[1] and sec[2] is not None and -5 <= sec[2] <= 200:
            return sec
        if attempt == 0: retried.append(f'#{h} (top {sec[2]})')
    return sec

# P68 · the reading layout, on one reading page (a unit or a report) already shown: content first (the header with its
# scope, then the bar, then the text; nothing about how the page was made before the text), process last (the two
# accordions after the text, Sources then "How this unit was made", both closed), and the stepper: one section shown
# at a time, "Section n of N" and the progress bar right at every step, next from the first section to the last and
# previous back, the menu reaching every section, "Whole unit" showing all of them and returning to one.
STEP_JS = r'''(pid) => {
  const p = document.getElementById(pid), out = [];
  const r = p.querySelector('.report.steps'), bar = p.querySelector('.stepbar');
  if (!r || !bar || !r.classList.contains('stepping')) return {n: 0, bad: ['no stepper on the page']};
  const secs = [...r.children].filter(s => s.classList.contains('sec')), n = secs.length;
  const vis = () => secs.map((s, i) => s.offsetHeight > 0 ? i : -1).filter(i => i >= 0);
  const want = (k, how) => { const v = vis();
    if (v.length !== 1 || v[0] !== k) out.push(`${how}: sections shown [${v}], expected [${k}]`);
    const sof = bar.querySelector('.sof').textContent.trim(); if (sof !== `Section ${k + 1} of ${n}`) out.push(`${how}: the bar reads "${sof}"`);
    const w = parseFloat(bar.querySelector('.sprog i').style.width); if (!(Math.abs(w - 100 * (k + 1) / n) < 0.1)) out.push(`${how}: progress ${w}%`); };
  const kids = [...p.children], ph = p.querySelector('.phead'), proc = p.querySelector('.process');
  if (kids.indexOf(bar) !== kids.indexOf(ph) + 1 || kids.indexOf(r) !== kids.indexOf(bar) + 1) out.push('not header, bar, text in that order');
  if (!ph.querySelector('h1 + .scope') && (!pid.startsWith('read-') || ph.querySelector('.eyebrow .pill.live'))) out.push('no scope line under the title');
  if (p.querySelector('.phead .prov, .phead .lede, .phead + .lede, .report .prov, .phead .toc')) out.push('process text or the old chips before the text');
  if (+bar.dataset.n !== n || bar.querySelectorAll('.seclist a').length !== n) out.push(`menu ${bar.querySelectorAll('.seclist a').length} items, bar ${bar.dataset.n}, sections ${n}`);
  if (secs.some(s => !s.querySelector(':scope > h2.band .bn'))) out.push('a section without its numbered band');
  const acc = proc ? [...proc.children].map(d => (d.classList.contains('src') ? 'src' : d.classList.contains('note') ? 'note' : d.classList.contains('made') ? 'made' : d.tagName) + (d.open ? ' open' : '')) : [];
  if (!proc || kids.indexOf(proc) !== kids.indexOf(r) + 1 || !['src,made', 'src,note,made'].includes(acc.join())) out.push(`after the text: ${acc.join() || 'nothing'}, expected Sources, the opening note where there is one, then How this unit was made, all closed`);
  want(+p.dataset.step || 0, 'on opening');
  if (+p.dataset.step) [...bar.querySelectorAll('.seclist a')][0].click();
  want(0, 'menu to 1');
  if (n > 1 && (proc.offsetHeight > 0 || p.querySelector(':scope > .pager').offsetHeight > 0)) out.push('the accordions or the next-unit cards show before the last section');
  for (let k = 1; k < n; k++) { secs[k - 1].querySelector(':scope > .secnav .snext').click(); want(k, `next to ${k + 1}`); }
  if (secs[n - 1].querySelector(':scope > .secnav .snext:not(.send)')) out.push('the last section has a next-section button');
  if (proc.offsetHeight === 0) out.push('the accordions are not shown after the last section');
  for (let k = n - 2; k >= 0; k--) { secs[k + 1].querySelector(':scope > .secnav .sprev').click(); want(k, `previous to ${k + 1}`); }
  [...bar.querySelectorAll('.seclist a')].forEach((a, k) => { a.click(); want(k, `menu item ${k + 1}`); });
  bar.querySelector('.whole').click(); if (vis().length !== n) out.push(`"Whole unit" shows ${vis().length} of ${n} sections`);
  bar.querySelector('.whole').click(); if (vis().length !== 1) out.push(`after "Whole unit" off, ${vis().length} sections shown`);
  [...bar.querySelectorAll('.seclist a')][0].click();
  return {n, bad: out};
}'''
# a link into Sources (the menu's, then the one at the end of the last section) opens its accordion and brings it into view
SRC_JS = r'''async (pid) => {
  const p = document.getElementById(pid), d = document.getElementById(pid + '-sources'), out = [];
  const seen = async () => { await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); const t = d.getBoundingClientRect().top; return d.open && t > -5 && t < innerHeight - 40; };
  p.querySelector('.secmenu').open = true; p.querySelector('.secx a[href="#' + pid + '-sources"]').click();
  if (!await seen()) out.push(`the menu's Sources link: open ${d.open}, top ${Math.round(d.getBoundingClientRect().top)}`);
  d.open = false; const secs = p.querySelectorAll('.report.steps > .sec');
  [...p.querySelectorAll('.seclist a')].pop().click();
  secs[secs.length - 1].querySelector('.secnav .send').click();
  if (!await seen()) out.push(`the last section's Sources link: open ${d.open}, top ${Math.round(d.getBoundingClientRect().top)}`);
  d.open = false; [...p.querySelectorAll('.seclist a')][0].click(); window.scrollTo(0, 0);
  return out;
}'''

# P68: with --shots, a --page reading page is also shot in the states its top does not show, one viewport each: the
# section menu open, the end of section 1 (its next button), section 2 just opened by it, the end of the last section
# with the two accordions closed, the two accordions open (at Sources, then at "How this unit was made"), and
# "Whole unit" mid-page
READING_SHOTS = [
    ('2-menu', "(pid) => { window.scrollTo(0, 0); document.querySelector('#' + pid + ' .secmenu').open = true; }"),
    ('3-end-of-1', "(pid) => { const p = document.getElementById(pid); p.querySelector('.secmenu').open = false; p.querySelector('.sec.on .secnav').scrollIntoView({block: 'end'}); }"),
    ('4-section-2', "(pid) => { const a = document.querySelector('#' + pid + ' .sec.on .snext'); if (a) a.click(); }"),
    ('5-last-end', "(pid) => { const p = document.getElementById(pid); [...p.querySelectorAll('.seclist a')].pop().click(); window.scrollTo(0, document.documentElement.scrollHeight); }"),
    ('6-process-open', "(pid) => { const p = document.getElementById(pid); p.querySelectorAll('.process details').forEach(d => d.open = true); document.getElementById(pid + '-sources').scrollIntoView(); }"),
    ('6a-note-open', "(pid) => { const n = document.getElementById(pid + '-note'); if (n) n.scrollIntoView(); }"),
    ('6b-made-open', "(pid) => { document.getElementById(pid + '-made').scrollIntoView(); }"),
    ('7-whole', "(pid) => { const p = document.getElementById(pid); p.querySelectorAll('.process details').forEach(d => d.open = false); p.querySelector('.stepbar .whole').click(); window.scrollTo(0, document.documentElement.scrollHeight * 0.4); }"),
]

# P94 (8 Nov 2026) · the section separators: on one reading page, every section's top-level paragraphs and their
# words, read from the page (each <p> child of the section; its words its text nodes split at white space, a tag a
# break, as build.py's wc counts), against its separator: one separator in a section with a paragraph, none in one
# without, standing last before the next and previous; div.topo.topo-patch.topo-sep, aria-hidden, textless, at most
# 6 KB; one rise per paragraph in order, its data-words that paragraph's words; every line in the page's tone (the
# panel's --cc); the frame 1200:170 and the column's width; in one-section view the text above and the next and
# previous below at least 20 px clear, in "Whole unit" the text above and the next section's band; then, with motion
# allowed, each separator's turn and breath (transform only) and at five poses of the turn, at the top of the breath,
# every line inside its frame; the page no wider than the screen.
SEP_JS = r"""([pid, poses, cyc, bt, motion]) => {
  const P = document.getElementById(pid), out = {secs: 0, seps: 0, none: 0, bytes: 0, maxb: 0, bad: [], ph: [], anims: 0, poses: 0};
  if (!P) { out.bad.push('no page'); return out; }
  const r = P.querySelector('.report.steps'), bar = P.querySelector('.stepbar'), whole = bar.querySelector('.whole');
  const words = e => { let t = ''; const walk = n => { for (const c of n.childNodes) { if (c.nodeType === 3) t += c.data; else if (c.nodeType === 1) { t += ' '; walk(c); t += ' '; } } }; walk(e); return t.split(/\s+/).filter(Boolean).length; };
  const probe = document.createElement('i'); P.appendChild(probe); probe.style.color = 'var(--cc)'; const tone = getComputedStyle(probe).color; probe.remove();
  const secs = [...r.children].filter(x => x.classList.contains('sec')); out.secs = secs.length;
  const seps = [];
  secs.forEach((sec, k) => {
    const paras = [...sec.children].filter(e => e.tagName === 'P' && !e.classList.contains('viz-cue')).map(words).filter(n => n > 0);   // the cue shell.js puts under a figure or table wider than its frame is the figure's, not a paragraph
    const ts = sec.querySelectorAll('.topo'), t = sec.querySelector(':scope > .topo-sep');
    if (!paras.length) { out.none++; if (ts.length) out.bad.push(`section ${k + 1}: no paragraph, yet ${ts.length} drawing(s)`); return; }
    if (ts.length !== 1 || !t) { out.bad.push(`section ${k + 1}: ${paras.length} paragraphs, ${ts.length} drawings, separator ${!!t}`); return; }
    out.seps++; seps.push([k, t]);
    if (t.className !== 'topo topo-patch topo-sep' || t.tagName !== 'DIV') out.bad.push(`section ${k + 1}: the separator is ${t.tagName}.${t.className}`);
    if (!t.nextElementSibling || !t.nextElementSibling.matches('nav.secnav')) out.bad.push(`section ${k + 1}: the separator is not last before the next and previous`);
    if (t.getAttribute('aria-hidden') !== 'true') out.bad.push(`section ${k + 1}: the separator is not aria-hidden`);
    if (t.textContent.trim() || t.querySelector('text, title, desc')) out.bad.push(`section ${k + 1}: the separator holds text`);
    const b = new Blob([t.outerHTML]).size; out.bytes += b; out.maxb = Math.max(out.maxb, b);
    if (b > 6144) out.bad.push(`section ${k + 1}: the separator is ${b} bytes, over 6 KB`);
    const gs = [...t.querySelectorAll('svg.topo-l g.ct-rise')], got = gs.map(g => +g.getAttribute('data-words'));
    if (t.querySelectorAll('svg.topo-l').length !== 1 || t.querySelector('g.ct-plan')) out.bad.push(`section ${k + 1}: ${t.querySelectorAll('svg.topo-l').length} layouts, or a planned ring`);
    const blank = gs.filter(g => !g.querySelector('circle.ct-spot') && !(g.querySelector('path') && g.querySelector('path').getAttribute('d'))).map(g => g.getAttribute('data-label'));   // P94 check: every paragraph shows
    if (blank.length) out.bad.push(`section ${k + 1}: rises ${blank.join(' ')} draw nothing`);
    if (got.join() !== paras.join()) out.bad.push(`section ${k + 1}: rises by words ${got.join(',')}, its paragraphs ${paras.join(',')}`);
    const st = [...new Set([...t.querySelectorAll('path, circle')].map(e => getComputedStyle(e).stroke))];
    if (st.length !== 1 || st[0] !== tone) out.bad.push(`section ${k + 1}: lines in ${st.join(' ')}, the page's tone ${tone}`);
    out.ph.push(parseFloat(getComputedStyle(t).getPropertyValue('--ph')));
  });
  // one section at a time: each separator between its text and its next and previous
  const links = [...bar.querySelectorAll('.seclist a')];
  seps.forEach(([k, t]) => { links[k].click();
    const fr = t.getBoundingClientRect(), up = t.previousElementSibling.getBoundingClientRect(), nav = t.nextElementSibling.getBoundingClientRect(), col = secs[k].getBoundingClientRect();
    if (!fr.width) { out.bad.push(`section ${k + 1}: the separator does not show in its section`); return; }
    if (Math.abs(fr.width / fr.height - 1200 / 170) > .05) out.bad.push(`section ${k + 1}: the separator is ${(fr.width / fr.height).toFixed(3)}:1, not 1200:170`);
    if (Math.abs(fr.width - col.width) > 1) out.bad.push(`section ${k + 1}: the separator is ${fr.width.toFixed(1)} px wide in a ${col.width.toFixed(1)} px column`);
    t.nextElementSibling.querySelectorAll('a').forEach(a => { const sp = a.querySelector('span'), ar = a.getBoundingClientRect(), pr = parseFloat(getComputedStyle(a).paddingRight);   // P94 check: a label past its button
      if (sp && (sp.scrollWidth > sp.clientWidth + 1 || sp.getBoundingClientRect().right > ar.right - pr + .5 || sp.getBoundingClientRect().left < ar.left - .5)) out.bad.push(`section ${k + 1}: "${sp.textContent}" runs past its button`); });
    if (fr.top - up.bottom < 20 || nav.top - fr.bottom < 20) out.bad.push(`section ${k + 1}: the separator ${Math.round(fr.top - up.bottom)} px under the text and ${Math.round(nav.top - fr.bottom)} px over the next and previous (20 at least)`);
  });
  links[0].click();
  // "Whole unit": every separator between its section and the next
  whole.click();
  seps.forEach(([k, t]) => { const fr = t.getBoundingClientRect(), nx = secs[k + 1];
    if (!fr.width) out.bad.push(`section ${k + 1}: no separator shown in "Whole unit"`);
    else if (nx && nx.getBoundingClientRect().top - fr.bottom < 20) out.bad.push(`section ${k + 1}: in "Whole unit" the separator is ${Math.round(nx.getBoundingClientRect().top - fr.bottom)} px over the next section`); });
  out.scroll = [document.documentElement.scrollWidth, document.documentElement.clientWidth];
  // the move
  const an = document.getAnimations().filter(a => a.effect && a.effect.target && a.effect.target.closest && a.effect.target.closest('#' + pid + ' .topo-sep'));
  out.anims = an.length;
  if (!motion) { if (an.length) out.bad.push(`${an.length} animations run on the separators under reduced motion`); }
  else {
    seps.forEach(([k, t]) => { const l = t.querySelector('svg.topo-l'), mine = an.filter(a => a.effect.target === l).map(a => a.animationName).sort().join();
      if (mine !== 'topo-breathe,topo-turn') out.bad.push(`section ${k + 1}: the separator's animations are [${mine}], not a turn and a breath`); });
    an.forEach(a => { const props = [...new Set(a.effect.getKeyframes().flatMap(f => Object.keys(f)).filter(x => !['offset', 'computedOffset', 'easing', 'composite'].includes(x)))];
      if (props.some(x => x !== 'transform')) out.bad.push(`a separator animates ${props.join(',')}, not transform alone`); });
    for (const p of poses) {
      an.forEach(a => { a.pause();
        if (a.animationName === 'topo-turn') { const d = a.effect.getTiming().delay; let t = p * cyc + d; if (t < 0) t = 2 * cyc - p * cyc + d; a.currentTime = t; }
        else { let t = a.effect.getTiming().delay + .9999 * bt; if (t < 0) t += 2 * bt; a.currentTime = t; } });
      out.poses++;
      seps.forEach(([k, t]) => { const fr = t.getBoundingClientRect(); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        t.querySelectorAll('path, circle').forEach(e => { const q = e.getBoundingClientRect(); if (!q.width && !q.height) return; x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); });
        const m = [x0 - fr.left, y0 - fr.top, fr.right - x1, fr.bottom - y1];
        if (Math.min(...m) < -.5) out.bad.push(`section ${k + 1}: at pose ${p} its lines leave the frame by ${m.filter(v => v < 0).map(v => (-v).toFixed(1))} px`);
        out.minclear = Math.min(out.minclear === undefined ? 1e9 : out.minclear, ...m); });
    }
    an.forEach(a => a.play());
  }
  whole.click(); links[0].click(); window.scrollTo(0, 0);
  return out;
}"""

SEP_WIDTHS = [('phone320', 320, 640, True), ('phone', 390, 844, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]

def check_seps(br, fails):
    """P94: every reading page at 320, 390, 768 and 1280 px, dark and light, under reduced motion and with motion
    allowed: SEP_JS on each (the separators against the sections' paragraphs, their place, size, tone and bytes, and
    with motion their move and their lines inside the frame at the five poses); no sideways scroll at 320 px. Prints
    the count and bytes."""
    errs, bad = [], []
    tot = dict(seps=0, none=0, bytes=0, secs=0, poses=0)
    per_page, low = {}, 1e9
    for name, w, h, mobile in SEP_WIDTHS:
        ctx, pg, _ = new_page(None, br, errs, f'seps {name}', w, h, mobile, motion=True)
        ids = pg.eval_on_selector_all('.panel[data-kind="report"]', 'ps => ps.map(p => p.id)')
        for pid in ids:
            pg.evaluate("localStorage.removeItem('hellas-theme'); document.documentElement.removeAttribute('data-theme')")
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                for motion in (False, True):
                    pg.emulate_media(reduced_motion='no-preference' if motion else 'reduce'); pg.wait_for_timeout(20)
                    r = pg.evaluate(SEP_JS, [pid, list(POSES), CYCLE, BTIME, motion])
                    tag = f'{pid} {name} {theme}{" motion" if motion else ""}'
                    bad += [f'{tag}: {b}' for b in r['bad'][:3]]
                    if r['scroll'][0] > r['scroll'][1]: bad.append(f'{tag}: the page is {r["scroll"][0]} px wide on a {r["scroll"][1]} px screen')
                    if motion:
                        phs = sorted(r['ph']); n = len(phs)
                        close = [(a, b) for a, b in zip(phs, phs[1:]) if b - a < .9 / max(n, 1)]
                        if close or any(x != x for x in phs): bad.append(f'{tag}: separators share or lack a phase ({close[:3]})')
                        if 'minclear' in r: low = min(low, r['minclear'])
                        tot['poses'] += r['poses'] * r['seps']
                    if name == 'phone' and theme == 'dark' and not motion:
                        tot['seps'] += r['seps']; tot['none'] += r['none']; tot['bytes'] += r['bytes']; tot['secs'] += r['secs']
                        per_page[pid] = (r['bytes'], r['seps'], r['maxb'])
        pg.emulate_media(reduced_motion='reduce')
        ctx.close()
    fails += ['separators ' + b for b in bad[:30]]
    if len(bad) > 30: fails.append(f'separators: {len(bad) - 30} more')
    if errs: fails.append('separators: console errors: ' + ' | '.join(errs[:3]))
    big = max(per_page.items(), key=lambda x: x[1][0]) if per_page else ('', (0, 0, 0))
    print(f'separators: {len(per_page)} reading pages, {tot["secs"]} sections, {tot["seps"]} separators, {tot["none"]} sections without a paragraph and so without one; '
          f'{tot["bytes"]:,} bytes in all, the largest {max((v[2] for v in per_page.values()), default=0):,} B, the page with most {big[0]} ({big[1][0]:,} B over {big[1][1]}); '
          f'checked at {", ".join(str(x[1]) for x in SEP_WIDTHS)} px, dark and light, with and without motion; {tot["poses"]:,} separator poses with motion allowed, the closest line {low:.1f} px from its frame')
    return tot, per_page

# P95 (8 Nov 2026) · the object reliefs: the library (design/outlines/) and every page uses.json maps
OUTL = R.parent / 'design' / 'outlines'
REL_FIELDS = ('id', 'file', 'depicts', 'courses', 'keywords', 'source', 'author', 'licence', 'licence_url', 'credit', 'texts')
REL_COURSES = ('greece', 'rome', 'brand-a', 'brand-b', 'ux-ia', 'personal-brand-pb', 'building-with-ai-bw')
REL_WIDTHS = [('phone320', 320, 640, True), ('phone', 390, 844, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]
REL_JS = r"""([pid, poses, cyc, bt, motion, want]) => {
  const P = document.getElementById(pid), out = {bad: [], bytes: 0, poses: 0};
  if (!P) { out.bad.push('no page'); return out; }
  const figs = P.querySelectorAll('figure.relief-fig'), f = figs[0], hd = P.querySelector(':scope > header.phead');
  if (figs.length !== 1 || !f) { out.bad.push(`${figs.length} relief figures`); return out; }
  if (f.parentElement !== hd) out.bad.push('the relief is not in the page header');
  const sc = hd.querySelector(':scope > p.scope');
  if (sc && !(sc.compareDocumentPosition(f) & Node.DOCUMENT_POSITION_FOLLOWING)) out.bad.push('the relief is not under the scope line');
  if (f.nextElementSibling) out.bad.push('the relief is not the header\'s last block');
  if (!hd.nextElementSibling || !hd.nextElementSibling.matches('.stepbar')) out.bad.push('the section bar does not follow the header');
  if (f.dataset.outline !== want.id) out.bad.push(`outline ${f.dataset.outline}, mapped ${want.id}`);
  const t = f.querySelector(':scope > div.topo.relief'), cap = f.querySelector(':scope > figcaption');
  if (!t || f.children.length !== 2 || !cap) { out.bad.push('the figure is not one drawing and its caption'); return out; }
  if (cap.textContent.trim() !== want.caption) out.bad.push(`caption "${cap.textContent.trim()}", expected "${want.caption}"`);
  if (!cap.textContent.includes(want.credit)) out.bad.push('the credit is not printed exactly');
  const la = cap.querySelectorAll('a');
  if (la.length !== 1 || la[0].getAttribute('href') !== want.lic || la[0].textContent !== want.licence) out.bad.push('the licence is not linked to its text');
  if (t.className !== 'topo relief' || t.getAttribute('aria-hidden') !== 'true') out.bad.push(`the drawing is ${t.className}, aria-hidden ${t.getAttribute('aria-hidden')}`);
  if (t.textContent.trim() || t.querySelector('text, title, desc')) out.bad.push('the drawing holds text');
  const svgs = t.querySelectorAll('svg'), sv = svgs[0];
  if (svgs.length !== 1 || !sv.classList.contains('topo-l')) out.bad.push(`${svgs.length} svgs, or not svg.topo-l`);
  const paths = [...sv.children];
  if (!paths.length || paths.some(p => p.tagName !== 'path' || !['rl-in', 'rl-out'].includes(p.getAttribute('class')) || [...p.attributes].some(a => !['class', 'd'].includes(a.name)))) out.bad.push('the drawing holds more than rl-in and rl-out paths with a class and a d');
  if (!sv.querySelector('path.rl-in') || !sv.querySelector('path.rl-out')) out.bad.push('no outline or no halo');
  out.bytes = new Blob([t.outerHTML]).size;
  if (out.bytes > 12288) out.bad.push(`the drawing is ${out.bytes} bytes, over 12 KB`);
  const probe = document.createElement('i'); P.appendChild(probe); probe.style.color = 'var(--cc)'; const tone = getComputedStyle(probe).color; probe.remove();
  const st = [...new Set(paths.map(p => getComputedStyle(p).stroke))];
  if (st.length !== 1 || st[0] !== tone) out.bad.push(`lines in ${st.join(' ')}, the page's tone ${tone}`);
  const op = parseFloat(getComputedStyle(sv).opacity), ho = parseFloat(getComputedStyle(sv.querySelector('path.rl-out')).strokeOpacity), io = parseFloat(getComputedStyle(sv.querySelector('path.rl-in')).strokeOpacity);
  if (!(op > 0 && op < 1) || !(ho < io)) out.bad.push(`the layer at ${op}, the halo at ${ho} of the lines' ${io}`);
  // the frame: the drawing's aspect, the column's width at most, 280 px tall at most on a phone (340 from 768)
  const fr = t.getBoundingClientRect(), col = hd.getBoundingClientRect(), vb = sv.viewBox.baseVal;
  out.w = fr.width; out.h = fr.height;
  if (Math.abs(fr.width / fr.height - vb.width / vb.height) > .02) out.bad.push(`frame ${(fr.width / fr.height).toFixed(3)}:1, drawing ${(vb.width / vb.height).toFixed(3)}:1`);
  if (fr.width > col.width + .5) out.bad.push(`frame ${fr.width.toFixed(1)} px in a ${col.width.toFixed(1)} px column`);
  const maxh = innerWidth < 768 ? 280 : 340;
  if (fr.height > maxh + .5) out.bad.push(`frame ${fr.height.toFixed(1)} px tall, over ${maxh}`);
  if (Math.abs(fr.height - maxh) > .5 && Math.abs(fr.width - col.width) > .5) out.bad.push(`frame ${fr.width.toFixed(1)} x ${fr.height.toFixed(1)}: neither the column's width nor ${maxh} px tall`);
  out.scroll = [document.documentElement.scrollWidth, document.documentElement.clientWidth];
  const an = document.getAnimations().filter(a => a.effect && a.effect.target === sv);
  out.anims = an.map(a => a.animationName).sort().join();
  if (!motion) { if (an.length) out.bad.push(`${an.length} animations under reduced motion`); }
  else {
    if (out.anims !== 'topo-breathe,topo-turn') out.bad.push(`animations [${out.anims}], not a turn and a breath`);
    an.forEach(a => { const props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k)).filter(x => !['offset', 'computedOffset', 'easing', 'composite'].includes(x)))];
      if (props.some(x => x !== 'transform')) out.bad.push(`animates ${props.join(',')}, not transform alone`); });
    out.ph = parseFloat(getComputedStyle(t).getPropertyValue('--ph'));
    out.sepph = [...P.querySelectorAll('.topo-sep')].map(s => parseFloat(getComputedStyle(s).getPropertyValue('--ph')));
    for (const p of poses) {
      an.forEach(a => { a.pause();
        if (a.animationName === 'topo-turn') { const d = a.effect.getTiming().delay; let x = p * cyc + d; if (x < 0) x = 2 * cyc - p * cyc + d; a.currentTime = x; }
        else { let x = a.effect.getTiming().delay + .9999 * bt; if (x < 0) x += 2 * bt; a.currentTime = x; } });
      out.poses++;
      const r = t.getBoundingClientRect(); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      paths.forEach(e => { const q = e.getBoundingClientRect(); x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); });
      const m = [x0 - r.left, y0 - r.top, r.right - x1, r.bottom - y1];
      if (Math.min(...m) < -.5) out.bad.push(`at pose ${p} its lines leave the frame by ${m.filter(v => v < 0).map(v => (-v).toFixed(1))} px`);
      out.minclear = Math.min(out.minclear === undefined ? 1e9 : out.minclear, ...m);
    }
    an.forEach(a => a.play());
  }
  // the page's text names the object
  const txt = P.querySelector('.report.steps').textContent;
  if (!new RegExp('\\b(?:' + want.kw.map(k => k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')\\b', 'i').test(txt)) out.bad.push('the page\'s text does not name the object');
  return out;
}"""


def check_reliefs(br, fails):
    """P95, P96: the outline library (at least ten outlines for each course, each with every field, an allowed licence, its
    SVG and its relief JSON, and a text of each course it serves naming it); every page uses.json maps (in this
    edition) at 320, 390, 768 and 1280 px, dark and light, with and without motion (REL_JS: its place under the scope
    line before the section bar, its caption and credit printed exactly, classes only, aria-hidden and textless, at most
    12 KB, the page's tone, the halo fainter, its frame, a turn and a breath by transform only at a phase of its own, its
    lines inside the frame at five poses at the top of the breath, still under reduced motion, the page's text naming
    the object, no sideways scroll); and no other reading page holding a relief."""
    import mdcourse
    lib = json.loads((OUTL / 'outlines.json').read_text())
    allowed = set(lib['allowed_licences'])
    bad, per = [], {c: 0 for c in REL_COURSES}
    for o in lib['outlines']:
        miss = [k for k in REL_FIELDS if not o.get(k)] + [k for k in ('repository', 'path', 'commit') if not o.get('source', {}).get(k)]
        if miss: bad.append(f'{o.get("id")}: no {", ".join(miss)}')
        if o.get('licence') not in allowed: bad.append(f'{o.get("id")}: licence {o.get("licence")!r} not in {sorted(allowed)}')
        if o.get('licence') not in o.get('credit', ''): bad.append(f'{o.get("id")}: the credit does not name its licence')
        for f in (o['file'], f'{o["id"]}.json'):
            if not (OUTL / f).exists(): bad.append(f'{o["id"]}: {f} missing')
        for c in o['courses']:
            per[c] = per.get(c, 0) + 1
            if not o['texts'].get(c): bad.append(f'{o["id"]}: no text of {c} names it')
    thin = {c: n for c, n in per.items() if n < 10}
    if thin: bad.append(f'the library holds fewer than ten outlines for {thin}')
    print(f'reliefs: the library holds {len(lib["outlines"])} outlines ({", ".join(f"{c} {n}" for c, n in per.items())}), {len(lib["rejected"])} rejected; licences {sorted({o["licence"] for o in lib["outlines"]})}')
    # every reading page on disk: a relief where uses.json maps one, none elsewhere
    pages = {}
    shell = (SITE / 'index.html').read_text()
    for m in re.finditer(r'<section class="panel[^"]*" id="([^"]+)"[^>]*data-kind="report"[^>]*data-src="([^"]+)"', shell):
        pages[m.group(1)] = (SITE / m.group(2)).read_text()
    mapped = {pid: oid for pid, oid in mdcourse.USES.items() if pid in pages}
    # P96: the roll-out. Every course keeps at least ten outlines in use (a course with fewer than ten reading pages, as
    # many as it has pages with a relief, each its own); every outline is in use or marked spare, not both; every
    # mapped page has its deciding sentence in uses-why.md
    if len(mapped) == len(mdcourse.USES):   # the full site, not an edition
        crs = {}
        for pid in pages:
            c = ('greece' if pid.startswith('m') else 'rome' if pid.startswith('rm') else None) or next((k for k in REL_COURSES if (SITE / k / f'{pid}.html').exists()), None)
            crs.setdefault(c, []).append(pid)
        inuse = {}
        for c, pids in crs.items():
            if c is None:   # a course with no REL_COURSES entry (Sport Psychology for Coaches until row G-R-SP, public-courses.md rule 10) shows no relief
                continue
            ids = {mapped[p] for p in pids if p in mapped}
            need = 10 if len(pids) >= 10 else sum(1 for p in pids if p in mapped)
            inuse[c] = len(ids)
            if len(ids) < need: bad.append(f'{c}: {len(ids)} outlines in use, fewer than {need}')
        used = set(mapped.values())
        for o in lib['outlines']:
            if o['id'] not in used and not o.get('spare'): bad.append(f'{o["id"]}: neither in use nor marked spare')
            if o['id'] in used and o.get('spare'): bad.append(f'{o["id"]}: in use and marked spare')
        why = (OUTL / 'uses-why.md').read_text()
        for pid, oid in mapped.items():
            if not re.search(r'\(`' + re.escape(pid) + r'`\) \| ' + re.escape(oid) + r' \| \d+ \| \S', why): bad.append(f'{pid}: no deciding sentence for {oid} in uses-why.md')
        print(f'reliefs: outlines in use per course {", ".join(f"{c} {n}" for c, n in inuse.items())}; {len(used)} of {len(lib["outlines"])} in use, '
              f'{sum(1 for o in lib["outlines"] if o.get("spare"))} spare; {len(mapped)} deciding sentences in uses-why.md')
    for pid, h in pages.items():
        n = h.count('<figure class="relief-fig"')
        if n != (1 if pid in mapped else 0): bad.append(f'{pid}: {n} reliefs, {"1" if pid in mapped else "none"} mapped')
    errs, low, phs = [], 1e9, []
    sizes = {}
    lb = {o['id']: o for o in lib['outlines']}
    for name, w, h, mobile in REL_WIDTHS:
        ctx, pg, _ = new_page(None, br, errs, f'reliefs {name}', w, h, mobile, motion=True)
        for pid, oid in mapped.items():
            o = lb[oid]
            want = dict(id=oid, caption=mdcourse.relief_caption(o), credit=o['credit'], kw=o['keywords'], lic=o['licence_url'], licence=o['licence'])
            pg.evaluate("localStorage.removeItem('hellas-theme'); document.documentElement.removeAttribute('data-theme')")
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                for motion in (False, True):
                    pg.emulate_media(reduced_motion='no-preference' if motion else 'reduce'); pg.wait_for_timeout(20)
                    r = pg.evaluate(REL_JS, [pid, list(POSES), CYCLE, BTIME, motion, want])
                    tag = f'{pid} {name} {theme}{" motion" if motion else ""}'
                    bad += [f'{tag}: {b}' for b in r['bad'][:4]]
                    if r.get('scroll') and r['scroll'][0] > r['scroll'][1]: bad.append(f'{tag}: the page is {r["scroll"][0]} px wide on a {r["scroll"][1]} px screen')
                    if motion and 'minclear' in r:
                        low = min(low, r['minclear'])
                        if any(abs(r['ph'] - x) < 1e-6 for x in r['sepph']): bad.append(f'{tag}: the relief shares a phase with a separator')
                    sizes[pid] = r['bytes']
                    if theme == 'dark' and not motion: phs.append(f'{pid} {name} {r.get("w", 0):.0f}x{r.get("h", 0):.0f}')
        pg.emulate_media(reduced_motion='reduce')
        ctx.close()
    fails += ['reliefs ' + b for b in bad[:30]]
    if len(bad) > 30: fails.append(f'reliefs: {len(bad) - 30} more')
    if errs: fails.append('reliefs: console errors: ' + ' | '.join(errs[:3]))
    print(f'reliefs: {len(mapped)} mapped pages ({", ".join(f"{p} {o} {sizes.get(p, 0):,} B" for p, o in mapped.items())}), {len(pages) - len(mapped)} reading pages without one; '
          f'checked at {", ".join(str(x[1]) for x in REL_WIDTHS)} px, dark and light, with and without motion; frames {"; ".join(phs)}; '
          f'the closest line {low:.1f} px from its frame over the poses with motion')


def check_reading(br, fails):
    """P68 on every unit and report of every course, at phone width: STEP_JS and SRC_JS on each; then, on one page of
    each course, a deep link to a section and to Sources on a fresh load, and Continue resuming at the section."""
    errs = []
    ctx, pg, _ = new_page(None, br, errs, 'reading', 390, 844, True)
    pg.evaluate('localStorage.clear()')
    ids = pg.eval_on_selector_all('.panel[data-kind="report"]', 'ps => ps.map(p => p.id)')
    nsec, bad = 0, []
    for pid in ids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(20)
        res = pg.evaluate(STEP_JS, pid); nsec += res['n']
        bad += [f'{pid}: {b}' for b in res['bad'][:4]]
        bad += [f'{pid}: {b}' for b in pg.evaluate(SRC_JS, pid)]
    fails += ['reading ' + b for b in bad[:20]]
    # one page per course: deep links and Continue
    sample = []
    for c in COURSES:
        ctxs = [c['home_id']] if c['family'] == 'history' else [f"{c.get('prefix', c['id'])}-{k.lower()}" for k in c['tracks']]
        for cx in ctxs:
            rs = [i for i in ids if pg.evaluate(f"document.getElementById('{i}').dataset.ctx") == cx]
            if rs: sample.append((cx, rs[len(rs) // 2]))
    retried, landed, notes = [], 0, 0
    for cx, pid in sample:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
        n = pg.evaluate(f"document.querySelectorAll('#{pid} .report.steps > .sec').length")
        if n < 2: continue
        k = min(2, n - 1)
        sid = pg.evaluate(f"document.querySelectorAll('#{pid} .report.steps > .sec')[{k}].querySelector('h2').id")
        pg.evaluate('localStorage.clear()')
        sec = fresh_land(pg, sid, retried)
        st = pg.evaluate(f"[+document.getElementById('{pid}').dataset.step, [...document.querySelectorAll('#{pid} .report.steps > .sec')].filter(s => s.offsetHeight > 0).length]")
        if sec[0] != pid or not sec[1] or not -5 <= sec[2] <= 200 or st != [k, 1]: fails.append(f'reading: deep link #{sid} gave panel {sec[0]}, top {sec[2]}, step and sections shown {st}, expected {pid} at section {k + 1}')
        else: landed += 1
        # the accordion is at the page's end, so on a short section it lands in view rather than at the top
        pg.goto(URL + f'#{pid}-sources'); pg.reload(); ready(pg); sec = pg.evaluate(SETTLE_JS, f'{pid}-sources')
        op = pg.evaluate(f"!!document.getElementById('{pid}-sources') && document.getElementById('{pid}-sources').open")
        if sec[0] != pid or not op or sec[2] is None or not -5 <= sec[2] <= 844 - 60: fails.append(f'reading: deep link #{pid}-sources gave panel {sec[0]}, top {sec[2]}, the accordion open {op}')
        # P73: the writer's opening note, where the page has one, is closed until a link opens it, and a deep link lands
        if pg.evaluate(f"!!document.getElementById('{pid}-note')"):
            pg.goto(URL + f'#{pid}'); pg.reload(); ready(pg)
            if pg.evaluate(f"document.getElementById('{pid}-note').open"): fails.append(f'reading: #{pid}-note is open before any link opens it')
            pg.goto(URL + f'#{pid}-note'); pg.reload(); ready(pg); sec = pg.evaluate(SETTLE_JS, f'{pid}-note')
            op = pg.evaluate(f"document.getElementById('{pid}-note').open")
            if sec[0] != pid or not op or sec[2] is None or not -5 <= sec[2] <= 844 - 60: fails.append(f'reading: deep link #{pid}-note gave panel {sec[0]}, top {sec[2]}, the note open {op}')
            else: notes += 1
        # Continue: read to section n, leave for the course home, come back through its Continue button; then a reload
        j = n - 1
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
        pg.evaluate(f"[...document.querySelectorAll('#{pid} .seclist a')][{j}].click()")
        pg.evaluate(f"location.hash = '{cx}'"); ready(pg); pg.wait_for_timeout(50)
        pg.click(f'#{cx} .hbtn.cont'); ready(pg); pg.wait_for_timeout(50)
        st = pg.evaluate(f"[[...document.querySelectorAll('.panel')].find(p => !p.hidden).id, +document.getElementById('{pid}').dataset.step, [...document.querySelectorAll('#{pid} .report.steps > .sec')].findIndex(s => s.offsetHeight > 0)]")
        if st != [pid, j, j]: fails.append(f'reading: Continue on {cx} after reading section {j + 1} of {pid} gave (panel, step, section shown) {st}')
        pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(50)
        st = pg.evaluate(f"[+document.getElementById('{pid}').dataset.step, [...document.querySelectorAll('#{pid} .report.steps > .sec')].findIndex(s => s.offsetHeight > 0)]")
        if st != [j, j]: fails.append(f'reading: reloading #{pid} after section {j + 1} gave (step, section shown) {st}')
    if errs: fails.append('reading: console errors: ' + ' | '.join(errs[:3]))
    if retried: print(f'reading: fresh-load anchors that landed only on the retry: {", ".join(retried)}')
    print(f'reading: {len(ids)} units and reports, {nsec} sections, each reached by next, previous and the menu, "Whole unit" on and off, '
          f'both accordions closed after the text and Sources opened by its links; deep links to a section ({landed} of {len(sample)}), to Sources and to the opening note ({notes}), '
          f'and Continue and a reload resuming at the section, on one page of each course ({", ".join(p for _, p in sample)})')
    ctx.close()

def check_split(br, fails):
    """In the browser: a stub is empty until opened, its file is fetched once and kept, a section link into an unopened
    report loads it and lands on the section, a failed fetch shows the retry state and the retry loads it."""
    hits, fail = {}, {'on': False}
    def handler(route):
        u = route.request.url.split(str(SERVER.server_port), 1)[1]
        hits[u] = hits.get(u, 0) + 1
        if fail['on'] and u == '/greece/r-2.5.html': route.fulfill(status=503, body='down'); return
        if fail.get('home') and u == '/rome/home.html': route.fulfill(status=503, body='down'); return
        route.continue_()
    errs = []
    ctx, pg, _ = new_page(None, br, errs, 'split', 390, 844, True)
    ctx.route('**/*.html', handler)
    stub = pg.evaluate("(() => { const p = document.getElementById('m23'); return [p.getAttribute('data-src'), p.innerHTML.length, p.hasAttribute('data-loaded')]; })()")
    if stub != ['greece/r-2.3.html', 0, False]: fails.append(f'split: #m23 before opening is {stub}, expected an empty stub fetching greece/r-2.3.html')
    pg.evaluate("location.hash = 'm23'"); ready(pg)
    got = pg.evaluate("[document.getElementById('m23').hasAttribute('data-loaded'), document.querySelectorAll('#m23 .report h2').length, document.querySelector('#m23 .pager').children.length]")
    if not (got[0] and got[1] and got[2] == 2): fails.append(f'split: #m23 after opening (loaded, sections, pager links) = {got}')
    pg.evaluate("location.hash = 'greece'"); ready(pg); pg.evaluate("location.hash = 'm23'"); ready(pg)
    if hits.get('/greece/r-2.3.html') != 1: fails.append(f'split: greece/r-2.3.html fetched {hits.get("/greece/r-2.3.html")} times, expected once')
    pg.wait_for_timeout(700)   # the next report is fetched in the background
    if not pg.evaluate("document.getElementById('m24').hasAttribute('data-loaded')"): fails.append('split: the next report (#m24) was not prefetched')
    pg.evaluate("document.querySelector('#m23 .pager a.next').click()"); ready(pg)   # P68: the cards show after the last section; clicked as a link
    if pg.evaluate("location.hash") != '#m24' or hits.get('/greece/r-2.4.html') != 1: fails.append(f'split: pager to #m24: hash {pg.evaluate("location.hash")}, fetched {hits.get("/greece/r-2.4.html")} times')
    # a section link into a report not yet opened, on a fresh load
    retried = []
    deep, dpan = ('rm12-2', 'rm12') if ROME else ('m52-2', 'm52')   # P70: an edition without Rome checks a Greek report
    sec = fresh_land(pg, deep, retried)
    if sec[0] != dpan or not sec[1] or not -5 <= sec[2] <= 200: fails.append(f'split: #{deep} on a fresh load gave panel {sec[0]}, section found {sec[1]}, top {sec[2]}')
    # a syllabus is a stub too (P20): empty until opened, fetched once, its prompts and copy buttons present
    sy, sc, sa = ('rome-syllabus', 'rome', 'rs-u3') if ROME else ('syllabus', 'greece', 's-u3')
    stub = pg.evaluate(f"(() => {{ const p = document.getElementById('{sy}'); return [p.getAttribute('data-src'), p.innerHTML.length, (p.getAttribute('data-anchors') || '').split(' ').includes('{sa}')]; }})()")
    if stub != [f'{sc}/syllabus.html', 0, True]: fails.append(f'split: #{sy} before opening is {stub}, expected an empty stub fetching {sc}/syllabus.html with its anchors')
    pg.evaluate(f"location.hash = '{sy}'"); ready(pg)
    got = pg.evaluate(f"[document.getElementById('{sy}').hasAttribute('data-loaded'), document.querySelectorAll('#{sy} article.smod pre').length, document.querySelectorAll('#{sy} button.copy').length]")
    if not (got[0] and got[1] >= 80 and got[1] == got[2]): fails.append(f'split: #{sy} after opening (loaded, prompts, copy buttons) = {got}')
    pg.evaluate(f"location.hash = '{sc}'"); ready(pg); pg.evaluate(f"location.hash = '{sy}'"); ready(pg)
    if hits.get(f'/{sc}/syllabus.html') != 1: fails.append(f'split: {sc}/syllabus.html fetched {hits.get(f"/{sc}/syllabus.html")} times, expected once')
    # a link into an unopened syllabus (a unit anchor) and into unopened briefs (a brief's card), on a fresh load
    for h, want in (('rs-u3', 'rome-syllabus'), ('s-m23', 'syllabus'), ('b-a2', 'briefs-a'), ('b-b3', 'briefs-b'), ('greece-u3', 'greece'), ('rome-u1', 'rome')):
        if not pg.evaluate(f"!!document.getElementById('{want}')"): continue   # P70: a page the edition does not hold
        sec = fresh_land(pg, h, retried)
        if sec[0] != want or not sec[1] or not -5 <= sec[2] <= 200: fails.append(f'split: #{h} on a fresh load gave panel {sec[0]}, element found {sec[1]}, top {sec[2]}')
    # a failed fetch, then the retry
    fail['on'] = True
    pg.evaluate("location.hash = 'm25'"); ready(pg)
    st = pg.evaluate("[document.getElementById('m25').hasAttribute('data-failed'), !!document.querySelector('#m25 a.hbtn[data-target=\"m25\"]'), document.querySelector('#m25 h1') && document.querySelector('#m25 h1').textContent]")
    if not (st[0] and st[1] and st[2]): fails.append(f'split: failed fetch state (failed, retry button, title) = {st}')
    fail['on'] = False
    pg.click('#m25 a.hbtn[data-target="m25"]'); ready(pg)
    if not pg.evaluate("document.getElementById('m25').hasAttribute('data-loaded') && !!document.querySelector('#m25 .report')"): fails.append('split: retry after a failed fetch did not load the report')
    # a course home is a stub too (P22): its continue button and unit cards arrive with the fetch, and a failed fetch is retried
    stub = pg.evaluate("(() => { const p = document.getElementById('rome'); return p && [p.getAttribute('data-src'), (p.getAttribute('data-anchors') || '').split(' ').includes('rome-u3')]; })()") if ROME else ['rome/home.html', True]
    if stub != ['rome/home.html', True]: fails.append(f'split: #rome stub is {stub}, expected rome/home.html with its unit-card anchors')
    pg.evaluate("localStorage.clear()"); pg.goto(URL + '#greece'); pg.reload(); ready(pg); pg.wait_for_timeout(100)
    hm = pg.evaluate("[document.getElementById('greece').hasAttribute('data-loaded'), document.querySelectorAll('#greece details[data-mods]').length, document.querySelectorAll('#greece details[data-mods][open]').length, document.querySelector('#greece .hbtn.cont').hidden, document.querySelector('#greece .hbtn.start').hidden]")
    if not (hm[0] and hm[1] >= 10 and hm[2] == 1 and hm[3] and not hm[4]): fails.append(f'split: #greece on a fresh load (loaded, cards, cards open, continue hidden, start shown) = {hm}')
    n0 = hits.get('/greece/home.html', 0)   # fetched once on this load (earlier fresh loads fetched it too)
    pg.evaluate("location.hash = 'm23'"); ready(pg); pg.evaluate("location.hash = 'greece'"); ready(pg); pg.wait_for_timeout(50)
    hm = pg.evaluate("[document.querySelector('#greece .hbtn.cont').hidden, document.querySelector('#greece .hbtn.cont b').textContent, document.querySelector('#greece .hbtn.start').hidden]")
    if hm[0] or not hm[1].startswith('2.3 ') or not hm[2]: fails.append(f'split: #greece continue after reading 2.3 (continue hidden, label, start hidden) = {hm}')
    if hits.get('/greece/home.html', 0) != n0: fails.append(f'split: greece/home.html fetched again on a second visit ({hits.get("/greece/home.html")} in all)')
    fail['home'] = ROME   # P70: the failed course-home fetch is tried on Rome's home, unopened until here; an edition without Rome skips it
    if not ROME: print('split: no unopened course home in this edition; the failed course-home fetch is not tried')
    else: pg.evaluate("location.hash = 'rome'"); ready(pg)
    if ROME:
        st = pg.evaluate("[document.getElementById('rome').hasAttribute('data-failed'), !!document.querySelector('#rome a.hbtn[data-target=\"rome\"]')]")
        if st != [True, True]: fails.append(f'split: failed course-home fetch state (failed, retry button) = {st}')
        fail['home'] = False
        pg.click('#rome a.hbtn[data-target="rome"]'); ready(pg); pg.wait_for_timeout(50)
        if not pg.evaluate("document.getElementById('rome').hasAttribute('data-loaded') && document.querySelectorAll('#rome details[data-mods]').length > 5"): fails.append('split: retry after a failed course-home fetch did not load the home')
    other = [e for e in errs if 'fonts.g' not in e and '503' not in e]
    if other: fails.append('split: console errors: ' + ' | '.join(other[:3]))
    if retried: print(f'split: fresh-load anchors that landed only on the retry: {", ".join(retried)}')
    print('split: stubs empty until opened; fetched once, kept and the next report prefetched; links into an unopened report, syllabus, briefs page and course home; failed fetch and retry (report and course home); a course home\'s continue button')
    ctx.close()

# V1, every kind since P55 (30 Oct 2026): inside every figure, the geometry the eye would otherwise have to check.
#  1. nothing leaves the drawing: no child of the SVG and no text outside its viewBox;
#  2. every text of a box group (<g data-box>, the box its first child: a node, a plate, a bar or a span carrying its
#     label) lies inside that box;
#  3. no two boxes overlap;
#  4. no two texts overlap, and no text outside a box group overlaps a box: a label is never drawn over another label,
#     a bar or a node. A text's box is its em box, which is taller than its ink, so it is inset vertically by a fifth
#     of its height (at most 3 units) on each side before it is compared: two lines of one label sit 13 to 14 apart.
# Measured in the SVG's own units with getBBox, so the width of the page does not matter. Run on the examples page
# (every kind and every fault case P55 added) and, in the phone pass, on every panel that carries figures.
FIG_JS = r'''(sel) => {
  const out = []; const figs = [...document.querySelectorAll(sel + ' figure.viz')];
  const kindOf = f => [...f.classList].find(c => c.startsWith('viz-') && c !== 'viz-wide' && c !== 'viz-numeric').slice(4) + (f.classList.contains('viz-numeric') ? '-numeric' : '');
  const ov = (a, b) => [Math.min(a.x + a.width, b.x + b.width) - Math.max(a.x, b.x), Math.min(a.y + a.height, b.y + b.height) - Math.max(a.y, b.y)];
  const ink = b => { const i = Math.min(3, b.height / 5); return {x: b.x + 0.5, y: b.y + i, width: Math.max(0, b.width - 1), height: Math.max(0, b.height - 2 * i)}; };
  const f1 = v => v.toFixed(1), say = s => `"${s.slice(0, 28)}"`;
  figs.forEach(f => {
    const kind = kindOf(f);
    const sc = f.querySelector('.viz-scroll'), svg = [...sc.querySelectorAll(':scope > svg')].find(s => s.getBoundingClientRect().width > 0) || sc.querySelector('svg'), vb = svg.viewBox.baseVal, T = 0.6;   // P83: the drawing shown at this width
    const outside = b => b.x < -T || b.y < -T || b.x + b.width > vb.width + T || b.y + b.height > vb.height + T;
    [...svg.children].forEach(el => { if (el.tagName === 'defs') return; const b = el.getBBox();
      if (b.width + b.height === 0) return;
      if (outside(b)) out.push(`${kind}: ${el.tagName}.${el.getAttribute('class') || ''} ${say(el.textContent)} leaves the drawing (${f1(b.x)},${f1(b.y)} ${f1(b.width)}x${f1(b.height)} in ${vb.width}x${vb.height})`); });
    const texts = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim()).map(t => [t, t.getBBox()]);
    texts.forEach(([t, b]) => { if (outside(b) && t.parentNode !== svg) out.push(`${kind}: ${say(t.textContent)} leaves the drawing (${f1(b.x)}..${f1(b.x + b.width)} in ${vb.width})`); });
    const boxes = [...svg.querySelectorAll('g[data-box]')].map(g => [g, g.firstElementChild.getBBox()]);
    boxes.forEach(([g, r]) => g.querySelectorAll('text').forEach(t => { if (!t.textContent.trim()) return; const b = t.getBBox();
      if (b.x < r.x - T || b.x + b.width > r.x + r.width + T || b.y < r.y - T || b.y + b.height > r.y + r.height + T)
        out.push(`${kind}: ${say(t.textContent)} outside its box (text ${f1(b.x)}..${f1(b.x + b.width)}, ${f1(b.y)}..${f1(b.y + b.height)}; box ${f1(r.x)}..${f1(r.x + r.width)}, ${f1(r.y)}..${f1(r.y + r.height)})`); }));
    for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
      const [w, h] = ov(boxes[i][1], boxes[j][1]);
      if (w > 0.6 && h > 0.6) out.push(`${kind}: boxes overlap (${say(boxes[i][0].textContent)} and ${say(boxes[j][0].textContent)})`);
    }
    const inks = texts.map(([t, b]) => [t, ink(b), t.closest('g[data-box]')]);
    for (let i = 0; i < inks.length; i++) for (let j = i + 1; j < inks.length; j++) {
      const [w, h] = ov(inks[i][1], inks[j][1]);
      if (w > 0.6 && h > 0.6) out.push(`${kind}: labels overlap (${say(inks[i][0].textContent)} and ${say(inks[j][0].textContent)})`);
    }
    inks.forEach(([t, b, g]) => { if (g) return; boxes.forEach(([bg, r]) => { const [w, h] = ov(b, r);
      if (w > 0.6 && h > 0.6) out.push(`${kind}: ${say(t.textContent)} is drawn over the box ${say(bg.textContent)}`); }); });
  });
  return {n: figs.length, kinds: figs.map(kindOf), bad: out};
}'''

CMP_WIDTHS = [('phone320', 320, 640), ('phone', 390, 844)]
TRACK_WIDTHS = CMP_WIDTHS + [('desktop', 1280, 800)]
CMP_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-compare, figure.viz-bars')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  const bars = [...s.querySelectorAll('rect.viz-bar')].map(b => b.getBoundingClientRect()).filter(r => r.height > 0);
  const vals = [...s.querySelectorAll('text.viz-value')].map(t => t.getBoundingClientRect());
  const tracks = [...s.querySelectorAll('rect.viz-track')].map(t => t.getBoundingClientRect());
  const cross = [];
  for (const v of vals) { const cy = (v.top + v.bottom) / 2;
    const t = tracks.find(t => cy > t.top - 2 && cy < t.bottom + 2);
    if (t && v.left < t.right - 0.5 && v.right > t.right + 0.5) cross.push([v.left, v.right, t.right]); }
  out.push({n: i + 1, kind: f.classList.contains('viz-bars') ? 'bars' : 'compare', frame: [fr.left, fr.right],
            bars: bars.map(r => [r.left, r.right]), vals: vals.map(r => [r.left, r.right]), cross: cross,
            open: sc.scrollLeft, alt: s.classList.contains('viz-alt')}); }
 return out; }"""
def check_phone_figures(br, fails):
    """P97 (12 Nov 2026), widened by P98 (12 Nov 2026) from compare to bars, and from the longest bar to every bar:
    every compare and bars figure, on every page that has one, at 320 and 390 px: the drawing a phone shows (its
    svg.viz-alt) opens unscrolled with every bar and every value whole inside the frame, so the bars are seen to scale
    in one frame. And (P98) at 320, 390 and 1280 px, in the drawing the width shows: no value sits across the end of its
    grey track (wholly on it or wholly beyond its end). Before P97 a compare drew 700 units on a phone; before P98 a
    bars figure's phone drawing was 328 units and scrolled on a 320 px phone, and a value could straddle its track's end."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if (SITE / src).exists() and re.search(r'viz-(compare|bars)\b', (SITE / src).read_text())]
    n, nt, bad = 0, 0, []
    for name, w, h in TRACK_WIDTHS:
        errs = []
        phone = w < 768
        ctx, pg, _ = new_page(None, br, errs, name, w, h, phone)
        for pid in pids:
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
            for f in pg.evaluate(CMP_JS, pid):
                where = f'{pid} figure {f["n"]} ({f["kind"]}) at {w} px'
                nt += 1
                for vl, vr, tr in f['cross']:
                    bad.append(f'{where}: a value ({vl:.0f} to {vr:.0f}) sits across the end of its track ({tr:.0f})')
                if not phone:
                    continue
                n += 1
                fl, fr = f['frame']
                if not f['alt']:
                    bad.append(f'{where}: shows its wide drawing, not its phone drawing')
                if f['open'] > 0.5:
                    bad.append(f'{where}: the frame opens scrolled')
                out = [b for b in f['bars'] if b[0] < fl - 0.5 or b[1] > fr + 0.5]
                if out:
                    bad.append(f'{where}: {len(out)} bar(s) not whole in the opening frame ({fl:.0f} to {fr:.0f})')
                vout = [v for v in f['vals'] if v[0] < fl - 0.5 or v[1] > fr + 0.5]
                if vout:
                    bad.append(f'{where}: {len(vout)} value(s) run past the frame')
        if errs: fails.append(f'compare and bars {name}: console errors: ' + ' | '.join(errs[:3]))
        ctx.close()
    fails += bad
    print(f'compare and bars on a phone (P97, P98): {n} figure frames on {len(pids)} pages at 320 and 390 px, every bar and value whole in the opening frame; '
          f'{nt} drawings at 320, 390 and 1280 px checked for a value across its track\'s end; {len(bad)} faults')

MTX_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-matrix')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  if (!s) { out.push({n: i + 1, none: true}); continue; }
  const w = s.getBoundingClientRect().width, over = w > sc.clientWidth + 1;
  const st = [...sc.querySelectorAll(':scope > .viz-stick, :scope > .viz-stickn')].find(x => getComputedStyle(x).display !== 'none');
  const r = {n: i + 1, over, frame: sc.clientWidth, w, stick: st ? st.getBoundingClientRect().width : 0, cls: st ? st.className : ''};
  if (st) { sc.scrollLeft = sc.scrollWidth; await new Promise(r => setTimeout(r, 60));
    const a = st.getBoundingClientRect(), b = sc.getBoundingClientRect(), ss = st.querySelector('svg');
    r.edge = Math.abs(a.left - b.left); r.tall = ss ? Math.abs(ss.getBoundingClientRect().height - s.getBoundingClientRect().height) : 0;
    sc.scrollLeft = 0; sc.dispatchEvent(new Event('scroll')); }
  out.push(r); }
 return out; }"""


def check_matrix_320(br, fails):
    """C1 (15 Nov 2026): every matrix figure, on every page that has one, at 320 px: a drawing that scrolls keeps a label
    column in view (.viz-stickn below 361 px where the matrix has one, else .viz-stick), sticky at the frame's left edge when
    scrolled to the end, as tall as the drawing, and no wider than 45% of the frame, so cells show beside the labels before
    the sideways scroll (BW4 figure 1 showed only its labels at 320 px)."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if (SITE / src).exists() and 'viz-matrix' in (SITE / src).read_text()]
    errs, bad, n, sc = [], [], 0, 0
    ctx, pg, _ = new_page(None, br, errs, 'phone320', 320, 640, True)
    for pid in pids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
        for f in pg.evaluate(MTX_JS, pid):
            n += 1
            where = f'{pid} matrix {f["n"]} at 320 px'
            if f.get('none'):
                bad.append(f'{where}: no drawing shown'); continue
            if not f['over']:
                continue
            sc += 1
            if not f['stick']:
                bad.append(f'{where}: scrolls with no label column in view'); continue
            if f['stick'] > 0.45 * f['frame'] + 0.5:
                bad.append(f'{where}: label column {f["stick"]:.0f} px of a {f["frame"]} px frame (over 45%)')
            if f.get('edge', 0) > 1:
                bad.append(f'{where}: label column {f["edge"]:.0f} px from the frame edge when scrolled to the end')
            if f.get('tall', 0) > 1:
                bad.append(f'{where}: label column not as tall as the drawing')
    if errs: fails.append('matrix 320: console errors: ' + ' | '.join(errs[:3]))
    ctx.close()
    fails += bad
    print(f'matrix figures at 320 px (C1): {n} on {len(pids)} pages, {sc} scrolling, each with a label column at most 45% of its frame; {len(bad)} faults')


LINE_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-linechart')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  const sr = s.getBoundingClientRect();
  const parts = [...s.querySelectorAll('text, circle.viz-pt, polyline, path')].map(t => t.getBoundingClientRect()).filter(r => r.width > 0 || r.height > 0);
  out.push({n: i + 1, frame: [fr.left, fr.right], svg: [sr.left, sr.right], open: sc.scrollLeft,
            alt: s.classList.contains('viz-alt'), parts: parts.map(r => [r.left, r.right])}); }
 return out; }"""
def check_phone_lines(br, fails):
    """P123 (15 Nov 2026): every line figure, on every page that has one, at 320 and 390 px: the drawing a phone shows
    (its svg.viz-alt) is no wider than the frame, opens unscrolled, and every text, point and line of it, the y-axis
    labels, the legend and each point label included, is whole inside the frame. Before P123 a line chart drew 700
    units on a phone and scrolled, so its y-axis and title left the frame and a label could sit at its edge."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if (SITE / src).exists() and re.search(r'viz-linechart\b', (SITE / src).read_text())]
    n, bad = 0, []
    for name, w, h in CMP_WIDTHS:
        errs = []
        ctx, pg, _ = new_page(None, br, errs, name, w, h, True)
        for pid in pids:
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
            for f in pg.evaluate(LINE_JS, pid):
                where = f'{pid} line figure {f["n"]} at {w} px'
                n += 1
                fl, fr = f['frame']
                if not f['alt']:
                    bad.append(f'{where}: shows its wide drawing, not its phone drawing')
                if f['open'] > 0.5:
                    bad.append(f'{where}: the frame opens scrolled')
                if f['svg'][1] - f['svg'][0] > fr - fl + 0.5:
                    bad.append(f'{where}: the phone drawing is wider than its frame and scrolls')
                out = [b for b in f['parts'] if b[0] < fl - 0.5 or b[1] > fr + 0.5]
                if out:
                    bad.append(f'{where}: {len(out)} part(s) of the drawing outside the frame ({fl:.0f} to {fr:.0f})')
        if errs: fails.append(f'line figures {name}: console errors: ' + ' | '.join(errs[:3]))
        ctx.close()
    fails += bad
    print(f'line figures on a phone (P123): {n} figure frames on {len(pids)} pages at 320 and 390 px, every part whole in the opening frame, no sideways scroll; {len(bad)} faults')

SCATTER_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-scatter')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  const sr = s.getBoundingClientRect();
  const parts = [...s.querySelectorAll('text, circle, rect, line, polyline, path')].map(t => t.getBoundingClientRect()).filter(r => r.width > 0 || r.height > 0);
  out.push({n: i + 1, frame: [fr.left, fr.right], svg: [sr.left, sr.right], open: sc.scrollLeft,
            alt: s.classList.contains('viz-alt'), parts: parts.map(r => [r.left, r.right])}); }
 return out; }"""
def check_phone_scatters(br, fails):
    """P124 (15 Nov 2026): every scatter figure, on every page that has one, at 320 and 390 px: the drawing a phone shows
    (its svg.viz-alt) is no wider than the frame, opens unscrolled, and every text, point and line of it, the y-axis
    labels, the legend and each point label included, is whole inside the frame. Before P124 a scatter drew its natural width
    on a phone and scrolled, so its y-axis and title left the frame and a label could sit at its edge."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if (SITE / src).exists() and re.search(r'viz-scatter\b', (SITE / src).read_text())]
    n, bad = 0, []
    for name, w, h in CMP_WIDTHS:
        errs = []
        ctx, pg, _ = new_page(None, br, errs, name, w, h, True)
        for pid in pids:
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
            for f in pg.evaluate(SCATTER_JS, pid):
                where = f'{pid} scatter figure {f["n"]} at {w} px'
                n += 1
                fl, fr = f['frame']
                if not f['alt']:
                    bad.append(f'{where}: shows its wide drawing, not its phone drawing')
                if f['open'] > 0.5:
                    bad.append(f'{where}: the frame opens scrolled')
                if f['svg'][1] - f['svg'][0] > fr - fl + 0.5:
                    bad.append(f'{where}: the phone drawing is wider than its frame and scrolls')
                out = [b for b in f['parts'] if b[0] < fl - 0.5 or b[1] > fr + 0.5]
                if out:
                    bad.append(f'{where}: {len(out)} part(s) of the drawing outside the frame ({fl:.0f} to {fr:.0f})')
        if errs: fails.append(f'scatter figures {name}: console errors: ' + ' | '.join(errs[:3]))
        ctx.close()
    fails += bad
    print(f'scatter figures on a phone (P124): {n} figure frames on {len(pids)} pages at 320 and 390 px, every part whole in the opening frame, no sideways scroll; {len(bad)} faults')

def check_figures(br, fails):
    """The examples page (V1) through the shell: VX_FIGS figures, one per kind, and the geometry of each (FIG_JS)."""
    if 'figures' in OMIT:
        print(f'figures: edition {EDITION} leaves out the examples page; the figure blocks are still checked (figure keys)'); return
    errs = []
    ctx, pg, _ = new_page(None, br, errs, 'figures', 390, 844, True)
    pg.evaluate("location.hash = 'viz-examples'"); ready(pg); pg.wait_for_timeout(200)
    res = pg.evaluate(FIG_JS, '#viz-examples')
    if res['n'] != VX_FIGS: fails.append(f'viz-examples: {res["n"]} figures in the panel, expected {VX_FIGS}')
    if len(set(res['kinds'][:VX_KINDS])) != VX_KINDS: fails.append(f'viz-examples: a kind appears twice among the kinds: {res["kinds"][:VX_KINDS]}')
    # P55: every block the renderer cannot draw honestly stops the build, with a message that says what to change
    for what, block, want in viz_examples.RAISES:
        try:
            viz.render(json.loads(json.dumps(block))); fails.append(f'viz-examples: {what!r} drew; it must stop the build')
        except SystemExit as e:
            if want not in str(e): fails.append(f'viz-examples: {what!r} stopped with {e!s}, which does not say {want!r}')
    fails += ['viz-examples: ' + b for b in res['bad'][:12]]
    if errs: fails.append('viz-examples: console errors: ' + ' | '.join(errs[:3]))
    print(f'figures: {VX_KINDS} kinds and {res["n"] - VX_KINDS} hard cases on the examples page ({", ".join(res["kinds"])}); {len(res["bad"])} geometry faults; '
          f'{len(viz_examples.RAISES)} blocks stop the build as they should')
    ctx.close()

# S-PAGES (15 Nov 2026) · the Backlog and Changelog pages: a plain overview by area, rendered from docs/site-log.md alone
SL_AREAS = ['Mythology', 'Marketing', 'AI', 'UX', 'Sports', 'Academy']   # S-SP0: course SP; S-SPORTS (19 Nov 2026): Coaching renamed Sports
SL_WIDTHS = [('phone320', 320, 640, True), ('phone', 390, 844, True), ('desktop', 1280, 800, False)]
# the engine's words, which the two pages leave out (a unit's own title, such as "Agents" or "Prompting", is content)
SL_PLAIN = re.compile(r'\b(Opus|Fable|Sonnet|Haiku|subagents?|(?:fresh|isolated|writer|checker|filer|applier|correction) agents?|'
                      r'agent contexts?|audit\w*|tokens?|chats?|backlog rows?|mirrors?|Corrections section|next prompt)\b'
                      r'|\b[\w/-]+\.(?:py|md|json|css|js|sh|txt)\b', re.I)
SL_JS = """(pid) => { const p = document.getElementById(pid), w = el => el.getBoundingClientRect().width;
  const areas = [...p.querySelectorAll('section.slarea')];
  return {sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth,
    order: [...p.querySelectorAll('[data-sl="order"] table.sl tbody tr')].map(r => [...r.cells].map(c => c.textContent.trim())),
    areas: areas.map(a => ({name: a.dataset.area, rows: [...a.querySelectorAll('table.sl tbody tr')].map(r => [...r.cells].map(c => c.textContent.trim())),
                             dates: [...a.querySelectorAll('td.c-date .sld')].map(d => d.textContent.trim())})),
    over: [...p.querySelectorAll('.sltbl, td')].filter(e => e.scrollWidth > e.clientWidth + 1).length,
    code: Math.max(0, ...[...p.querySelectorAll('td.c-code')].map(w)),
    text: Math.min(9999, ...[...p.querySelectorAll('td.c-text')].map(w)),
    nowrap: [...p.querySelectorAll('td.c-text')].filter(t => getComputedStyle(t).whiteSpace === 'nowrap').length}; }"""
def site_log_rows():
    """docs/site-log.md's two tables, as build.py reads them: Next [(n, code, area, text)], Done [(iso, code, area, text)]."""
    nxt, done, sec = [], [], None
    for ln in (R.parent / 'docs' / 'site-log.md').read_text(encoding='utf-8').split('\n'):
        if ln.startswith('## '):
            sec = ln[3:].strip(); continue
        if sec in ('Next', 'Done') and ln.startswith('|') and not ln.startswith('|---'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            if c[0] not in ('#', 'Date'):
                (nxt if sec == 'Next' else done).append(tuple(c))
    return nxt, done

def check_site_log(br, fails):
    """S-PAGES (15 Nov 2026): the Backlog page holds the overall order (#, code, area, sentence: one row per entry of the
    site log's Next, in its order) and one section per area (code, sentence); the Changelog page one section per area
    (date, code, sentence), newest first, every Done entry once. Both in plain words: no model name, no engine word
    (SL_PLAIN), no file name and no private term (kit/private-terms.txt). At 320, 390 and 1280 px, dark and light: no
    sideways scroll of the page, a table or a cell; the sentence wraps; on a phone the code column at most 72 px and the
    sentence column at least 110 px."""
    if 'backlog' in OMIT and 'changelog' in OMIT:
        print(f'site log: edition {EDITION} leaves out the Backlog and Changelog pages'); return
    nxt, done = site_log_rows()
    bad = []
    # the words, on disk: the backlog panel in the shell and the changelog page beside it
    shell = (SITE / 'index.html').read_text()
    texts = {}
    if 'backlog' not in OMIT:
        m = re.search(r'<section class="panel log slog" id="backlog".*?</section>\s*(?=<section class="panel|$)', shell, re.S)
        texts['backlog'] = m.group(0) if m else ''
        if not m: bad.append('site log: the Backlog panel (.panel.log.slog#backlog) is not in the shell')
    if 'changelog' not in OMIT:
        texts['changelog'] = (SITE / 'changelog.html').read_text() if (SITE / 'changelog.html').exists() else ''
    ft, _ = private_terms.terms()
    PT = private_terms.rx(ft)
    for pid, t in texts.items():
        plain = H.unescape(re.sub(r'<[^>]+>', ' ', t))
        for m in SL_PLAIN.finditer(plain): bad.append(f'site log: the {pid} page says "{m.group(0)}" (not plain)')
        for m in PT.finditer(plain): bad.append(f'site log: the {pid} page carries the private term "{m.group(0)}"')
    seen = 0
    for name, w, h, mobile in SL_WIDTHS:
        for theme in ('dark', 'light'):
            errs = []
            ctx, pg, _ = new_page(None, br, errs, name, w, h, mobile)
            if theme == 'light':
                pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
            where = f'{w} px {theme}'
            for pid in [x for x in ('backlog', 'changelog') if x not in OMIT]:
                pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(80)
                r = pg.evaluate(SL_JS, pid)
                seen += 1
                if [a['name'] for a in r['areas']] != SL_AREAS: bad.append(f'site log {pid} at {where}: areas {[a["name"] for a in r["areas"]]}, expected {SL_AREAS}')
                if r['sw'] > r['cw']: bad.append(f'site log {pid} at {where}: the page scrolls sideways ({r["sw"]} > {r["cw"]})')
                if r['over']: bad.append(f'site log {pid} at {where}: {r["over"]} table(s) or cell(s) overflow')
                if r['nowrap']: bad.append(f'site log {pid} at {where}: {r["nowrap"]} sentence cell(s) do not wrap')
                if mobile and r['code'] > 72: bad.append(f'site log {pid} at {where}: the code column is {r["code"]:.0f} px wide (at most 72)')
                if mobile and r['text'] < 110: bad.append(f'site log {pid} at {where}: a sentence column is {r["text"]:.0f} px wide (at least 110)')
                if pid == 'backlog':
                    want = [[n, c, a, t] for n, c, a, t in nxt]
                    if r['order'] != want: bad.append(f'site log backlog at {where}: the order table has {len(r["order"])} rows, not the site log\'s {len(want)} in order')
                    for a in r['areas']:
                        wa = [[c, t] for n, c, ar, t in nxt if ar == a['name']]
                        if a['rows'] != wa: bad.append(f'site log backlog at {where}: {a["name"]} has {len(a["rows"])} rows, the site log {len(wa)}')
                else:
                    got = sorted(tuple(x[1:]) + (a['name'],) for a in r['areas'] for x in a['rows'])
                    want = sorted((c, t, a) for d, c, a, t in done)
                    if got != want: bad.append(f'site log changelog at {where}: {len(got)} entries shown, the site log has {len(want)}')
                    for a in r['areas']:
                        iso = [d for d, c, ar, t in done if ar == a['name']]
                        if a['dates'] != [short(d) for d in sorted(iso, reverse=True)]: bad.append(f'site log changelog at {where}: {a["name"]} is not newest first')
            if errs: bad.append(f'site log {where}: console errors: ' + ' | '.join(errs[:3]))
            ctx.close()
    fails += bad
    print(f'site log (S-PAGES): {len(nxt)} next and {len(done)} done in docs/site-log.md; Backlog and Changelog checked {seen} times at '
          f'{", ".join(str(x[1]) for x in SL_WIDTHS)} px, dark and light (plain words, private terms, order, areas, no sideways scroll); {len(bad)} faults')

def short(iso):
    import datetime
    return datetime.date.fromisoformat(iso).strftime('%-d %b %Y')

def main():
    errors, fails = [], []
    check_files(fails)
    check_viz_keys(fails)
    check_notes(fails)
    check_figure_rules(fails)
    with sync_playwright() as p:
        br = p.chromium.launch()
        check_split(br, fails)
        check_figures(br, fails)
        check_phone_figures(br, fails)
        check_matrix_320(br, fails)
        check_phone_lines(br, fails)
        check_phone_scatters(br, fails)
        check_reading(br, fails)
        check_seps(br, fails)
        check_reliefs(br, fails)   # P95
        check_site_log(br, fails)   # S-PAGES

        # ---- phone ------------------------------------------------------------------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'phone', 390, 844, True)
        if lay != [390, 1]: fails.append(f'phone layout {lay}: expected [390, 1] (missing viewport tag?)')
        else: print('phone layout: 390 px at scale 1')
        check_panels(pg, 'phone', fails)
        pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')"); pg.wait_for_timeout(50)
        check_panels(pg, 'phone light', fails)
        pg.evaluate("localStorage.removeItem('hellas-theme'); document.documentElement.removeAttribute('data-theme')")
        # drawer in each context, every unit expanded
        for pid in ['home', 'greece', 'rome', 'brand-a', 'brand-b']:
            if not pg.evaluate(f"!!document.getElementById('{pid}')"): continue   # P70: not in this edition
            pg.evaluate(f"location.hash = '{pid}'"); pg.wait_for_timeout(30)
            pg.click('#menuB'); pg.wait_for_timeout(250)
            pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed'))")
            res = pg.evaluate(BOX_JS, ['#drawer', GAP])
            if res['nbad']: fails.append(f'drawer@{pid}: ' + '; '.join(res['bad']))
            sw = pg.evaluate('document.getElementById("drawer").scrollWidth <= document.getElementById("drawer").clientWidth')
            if not sw: fails.append(f'drawer@{pid}: horizontal overflow')
            pg.click('#closeB'); pg.wait_for_timeout(250)

        # navigation context, from a clean slate
        pg.evaluate('localStorage.clear()'); pg.goto(URL + '#home'); pg.reload(); pg.wait_for_timeout(300)
        EXPECT = home_expect()
        check_home(pg, 'phone', fails, EXPECT)
        check_new(pg, 'phone', fails, EXPECT)
        pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
        check_home(pg, 'phone light', fails, EXPECT)
        check_contrast(pg, fails)
        pg.evaluate('localStorage.clear()'); pg.goto(URL + '#home'); pg.reload(); pg.wait_for_timeout(300)
        def state():
            ready(pg)
            return pg.evaluate('''() => ({id: [...document.querySelectorAll('.panel')].find(p => !p.hidden).id,
              nav: [...document.querySelectorAll('[data-navctx]')].filter(n => !n.hidden).map(n => n.dataset.navctx).join(','),
              u: document.getElementById('curU').textContent, t: document.getElementById('curT').textContent,
              arrows: !document.getElementById('arrows').hidden, prev: !document.getElementById('prevB').disabled, next: !document.getElementById('nextB').disabled,
              cont: [...document.querySelectorAll('.panel:not([hidden]) .hbtn.cont')].map(b => b.hidden ? '(hidden)' : b.querySelector('span').textContent + ' ' + b.querySelector('b').textContent).join('|')})''')
        log = []
        def step(label, expect):
            s = state(); log.append((label, s))
            for k, v in expect.items():
                ok = v(s[k]) if callable(v) else s[k] == v
                if not ok: fails.append(f'nav {label}: {k} = {s[k]!r}, expected {v if not callable(v) else "check"}')
        step('home', dict(id='home', nav='root', u='HOME', arrows=False))
        if 'changelog' not in OMIT:
            pg.click('#home a.hbtn[href="#changelog"]'); pg.wait_for_timeout(80)
            step('changelog', dict(id='changelog', nav='root', u='ACADEMY', t='Changelog', arrows=False))
            pg.click('#homeB'); pg.wait_for_timeout(80)
        else:   # P70: an edition without the changelog has no button to it and no panel
            if pg.evaluate("!!document.querySelector('a[href=\"#changelog\"], #changelog, a[href=\"#backlog\"], #backlog')"): fails.append(f'edition {EDITION}: a changelog or backlog page or link is built')
        rome_reps = []
        if ROME:
            pg.click('#home a.course[href="#rome"]'); pg.wait_for_timeout(80)
            step('rome home', dict(id='rome', nav='rome', u='COURSE 2', t='Rome', arrows=True, prev=False, next=True))
            rome_reps = pg.eval_on_selector_all('#rome a.hrow', 'as => as.map(a => a.dataset.target)')
        if rome_reps:
            pg.evaluate("document.querySelectorAll('#rome details[data-mods]').forEach(d => d.open = true)")
            first = rome_reps[min(4, len(rome_reps) - 1)]
            pg.click(f'#rome a.hrow[data-target="{first}"]'); pg.wait_for_timeout(80)
            step('rome report', dict(id=first, nav='rome', u=lambda u: u.startswith('ROME · UNIT ') and u.count(' · ') == 2, arrows=True))
            pg.click('#nextB'); pg.wait_for_timeout(50)
            step('rome next', dict(nav='rome', id=lambda i: i.startswith('rm') or i in ('rome', 'rome-syllabus')))
            rome_last = pg.eval_on_selector_all('nav[data-navctx="rome"] .dunit a.ditem[data-target]', 'as => as.map(a => a.dataset.target)')[-1]
            pg.evaluate(f"location.hash = '{rome_last}'"); pg.wait_for_timeout(50)
            step('rome last report', dict(id=rome_last, nav='rome', next=False))
            pg.evaluate(f"location.hash = '{rome_reps[0]}'"); pg.wait_for_timeout(50)
            pg.click('#prevB'); pg.wait_for_timeout(50)
            step('rome prev from first report', dict(id='rome-syllabus', nav='rome', u='ROME', t='Syllabus and prompts'))
            pg.evaluate(f"location.hash = '{first}'"); pg.wait_for_timeout(50)
        # A4: each history course's "How it was built" page, fetched through the shell, one row per written report
        for cid in [c for c in ('greece', 'rome') if c in HAS and 'build' not in OMIT]:
            pg.evaluate(f"location.hash = '{cid}-built'"); pg.wait_for_timeout(50)
            step(f'{cid} how it was built', dict(id=f'{cid}-built', nav=cid, t='How it was built', arrows=True))
            nrow = pg.evaluate(f"document.querySelectorAll('#{cid}-built tr[data-mod]').length")
            nrep = pg.evaluate(f"document.querySelectorAll('nav[data-navctx=\"{cid}\"] .dunit a.ditem[data-target]').length")
            if nrow != nrep or not nrow: fails.append(f'{cid}-built: {nrow} report rows for {nrep} written reports')
        if 'build' in OMIT and pg.evaluate("!!document.querySelector('[id$=\"-built\"], a[href$=\"-built\"]')"): fails.append(f'edition {EDITION}: a "How it was built" page or link is built')
        pg.evaluate(f"location.hash = '{first}'" if rome_reps else ("location.hash = 'rome'" if ROME else "location.hash = 'home'")); pg.wait_for_timeout(50)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        step('home again', dict(id='home', nav='root', arrows=False, cont=''))   # P91: no Continue on the home
        pg.click('#home a.course[href="#greece"]'); pg.wait_for_timeout(80)
        step('greece home', dict(id='greece', nav='greece', u='COURSE 1', t='Greece', prev=False, cont='(hidden)'))
        pg.evaluate("document.querySelectorAll('#greece details[data-mods]').forEach(d => d.open = true)")
        pg.click('#greece a.hrow[data-target="m23"]'); pg.wait_for_timeout(80)
        step('greek report', dict(id='m23', nav='greece', u='GREECE · UNIT 2 · 2.3', arrows=True, prev=True, next=True))
        pg.click('#nextB'); pg.wait_for_timeout(50)
        step('greek next', dict(id='m24', nav='greece'))
        greek_last = pg.eval_on_selector_all('nav[data-navctx="greece"] .dunit a.ditem[data-target]', 'as => as.map(a => a.dataset.target)')[-1]
        pg.evaluate(f"location.hash = '{greek_last}'"); pg.wait_for_timeout(50)
        step('greek last', dict(id=greek_last, nav='greece', next=False))
        pg.evaluate("location.hash = 'm24'"); pg.wait_for_timeout(50)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        step('home last', dict(id='home', cont=''))
        if rome_reps:
            pg.click('#home a.course[href="#rome"]'); pg.wait_for_timeout(80)
            step('rome home resumes rome', dict(id='rome', cont=lambda c: c.startswith('Continue ') and 'Greece' not in c and c != '(hidden)'))
        pg.click('#menuB'); pg.wait_for_timeout(250)
        dr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dtop .ditem .t')].map(t => t.textContent)")
        if rome_reps and dr[:3] != ['Academy', 'Rome: course home', 'Syllabus and prompts']: fails.append(f'rome drawer top: {dr}')
        pg.click('#closeB'); pg.wait_for_timeout(200)
        # the Brand + AI courses (A under Marketing, B under Technology, A3): each its own drawer context with a Units group
        # and a "How it is built" group; written units open reading pages inside the site (never a link out); the reading
        # page is a report (prev/next, continue); the briefs, build order, bibliography and changelog are pages too
        for bid, short, key in ((('brand-a', 'Personal brand', 'A'), ('brand-b', 'Building with AI', 'B')) if BRAND else ()):
            pg.click('#homeB'); pg.wait_for_timeout(80)
            pg.click(f'#home a.course[href="#{bid}"]'); pg.wait_for_timeout(80)
            step(f'{bid} home', dict(id=bid, nav=bid, u=f'COURSE {key}', t=short, arrows=True, prev=False))
            pg.click('#menuB'); pg.wait_for_timeout(250)
            gr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dunit')].map(u => u.querySelector('.ut').textContent + (u.classList.contains('closed') ? ':closed' : ':open'))")
            if gr != ['Units:open', 'How it is built:closed']: fails.append(f'{bid} drawer groups on arrival: {gr}')
            pg.click('#closeB'); pg.wait_for_timeout(200)
            ba = pg.evaluate(f"[...document.querySelectorAll('#{bid} a.course.live')].map(a => a.getAttribute('href'))")   # P93: the unit tiles
            if not ba or not all(h.startswith('#read-') for h in ba): fails.append(f'{bid} written units do not open reading pages: {ba[:3]}')
            # navigation never leaves the site: no artifact link in a hero, a button row or the drawer (a unit's own citations may cite one)
            ext = pg.evaluate(f"[...document.querySelectorAll('.panel[data-ctx=\"{bid}\"] .hero a, .panel[data-ctx=\"{bid}\"] .hlinks a, .panel[data-ctx=\"{bid}\"] .hrows a.hrow:not([target]), [data-navctx=\"{bid}\"] a')].filter(a => a.getAttribute('href').startsWith('http')).map(a => a.href)")
            if ext: fails.append(f'{bid} navigation links out of the site: {ext[:3]}')
            pg.click(f'#{bid} a.course.live[href="{ba[0]}"]'); pg.wait_for_timeout(80)
            step(f'{bid} reading', dict(id=ba[0][1:], nav=bid, u=lambda u: u.startswith(short.upper() + ' · '), arrows=True, prev=True))
            for pid, t in ((f'{bid}-build', 'How it is built'), (f'{bid}-order', 'Build order'), (f'briefs-{key.lower()}', 'Briefs'), (f'{bid}-bibliography', 'Bibliography'), (f'{bid}-changelog', 'Changelog')):
                pg.evaluate(f"location.hash = '{pid}'"); pg.wait_for_timeout(50)
                step(f'{bid} {t}', dict(id=pid, nav=bid, t=t))
            # A4: the course's "How it was built" page, generated: one row per written unit, read from the front matter
            pg.evaluate(f"location.hash = '{bid}-built'"); pg.wait_for_timeout(50)
            step(f'{bid} How it was built', dict(id=f'{bid}-built', nav=bid, t='How it was built'))
            nrow = pg.evaluate(f"document.querySelectorAll('#{bid}-built tr[data-unit]').length")
            if nrow != len(ba) or not pg.evaluate(f"document.getElementById('{bid}-built').hasAttribute('data-loaded')"):
                fails.append(f'{bid}-built: {nrow} unit rows for {len(ba)} written units, or not fetched through the shell')
            pg.click('#homeB'); pg.wait_for_timeout(80)
            step(f'home after {bid}', dict(id='home', cont=''))
            pg.click(f'#home a.course[href="#{bid}"]'); pg.wait_for_timeout(80)
            step(f'{bid} home resumes', dict(id=bid, cont=lambda c: c.startswith('Continue ') and c != '(hidden)'))
            pg.click('#menuB'); pg.wait_for_timeout(250)
            dr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dtop .ditem .t')].map(t => t.textContent)")
            if dr[:2] != ['Academy', f'{short}: course home']: fails.append(f'{bid} drawer top: {dr}')
            pg.click('#closeB'); pg.wait_for_timeout(200)
        # the root drawer: Home, Changelog, Backlog, then a collapsible group per track, open by default
        pg.click('#homeB'); pg.wait_for_timeout(80)
        pg.click('#menuB'); pg.wait_for_timeout(250)
        dr = pg.evaluate("[...document.querySelectorAll('[data-navctx=\"root\"] .dtop .ditem .t')].map(t => t.textContent)")
        want_top = ['Home', "What's new"] + [n for n, k in (('Changelog', 'changelog'), ('Backlog', 'backlog')) if k not in OMIT]   # P91: What's new
        if dr != want_top: fails.append(f'root drawer top: {dr}, expected {want_top}')
        gr = pg.evaluate("[...document.querySelectorAll('[data-navctx=\"root\"] .dunit')].map(u => u.querySelector('.ut').textContent + (u.classList.contains('closed') ? ':closed' : ':open'))")
        # a track's group is open once a page in it was visited in this run (shell.js show()); the ones the run above
        # visited (greece, rome, brand-a, brand-b) are open, any other track from courses.py starts closed
        seen = {'history'} | ({'marketing', 'technology'} if BRAND else set())
        want = [t['name'] + (':open' if t['id'] in seen else ':closed') for t in THEMES]
        if gr != want: fails.append(f'root drawer groups: {gr}, expected {want}')
        pg.click('[data-navctx="root"] .dunit[data-unit="track:history"] .duh'); pg.wait_for_timeout(50)
        if not pg.evaluate("document.querySelector('[data-navctx=\"root\"] .dunit[data-unit=\"track:history\"]').classList.contains('closed')"): fails.append('root drawer: the History group does not collapse')
        pg.click('[data-navctx="root"] .dunit[data-unit="track:history"] .duh'); pg.wait_for_timeout(50)
        pg.click('#closeB'); pg.wait_for_timeout(200)
        # a course drawer is an accordion: opening a second unit closes the first
        pg.evaluate("location.hash = 'greece'"); pg.wait_for_timeout(50)
        pg.click('#menuB'); pg.wait_for_timeout(250)
        pg.click('[data-navctx="greece"] .dunit[data-unit="1"] .duh'); pg.wait_for_timeout(30)
        pg.click('[data-navctx="greece"] .dunit[data-unit="2"] .duh'); pg.wait_for_timeout(30)
        op = pg.evaluate("[...document.querySelectorAll('[data-navctx=\"greece\"] .dunit:not(.closed)')].map(u => u.dataset.unit)")
        if op != ['2']: fails.append(f'greece drawer accordion: open units {op}, expected [\'2\']')
        pg.click('#closeB'); pg.wait_for_timeout(200)
        # the backlog page (S-PAGES): the overall order, then the areas, from docs/site-log.md
        if 'backlog' not in OMIT:
            pg.evaluate("location.hash = 'backlog'"); pg.wait_for_timeout(50)
            step('backlog', dict(id='backlog', nav='root', u='ACADEMY', t='Backlog', arrows=False))
            nt = pg.evaluate("document.querySelectorAll('#backlog [data-sl=\"order\"] table.sl').length")
            if nt != 1: fails.append(f'backlog page: {nt} order tables, expected one (S-PAGES; check_site_log checks the rest)')
        # the home lists every live course under its track, in courses.py order (history courses, then markdown courses)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        tr = pg.evaluate("[...document.querySelectorAll('#home .track')].map(t => t.querySelector('h2').textContent + ':' + [...t.querySelectorAll('.cgrid a.course')].map(a => a.getAttribute('href')).join(','))")
        if tr != HOME_TRACKS: fails.append(f'home tracks: {tr}, courses.py gives {HOME_TRACKS}')
        h1 = pg.evaluate("[...document.querySelectorAll('.panel[data-kind=\"course\"] h1, #home h1')].map(h => h.textContent)")
        if any(' in the order' in t or t.startswith('The courses') for t in h1): fails.append(f'course titles not self-evident: {h1}')
        title = pg.title()
        if title != ED['title']: fails.append(f'page title {title!r}, expected {ED["title"]}')
        for label, s in log: print(f'  {label:28} {s["id"]:14} nav={s["nav"]:7} {s["u"]} | {s["t"][:40]} | arrows={s["arrows"]} prev={s["prev"]} next={s["next"]} | {s["cont"][:60]}')
        rp = rome_reps[3] if len(rome_reps) > 3 else (rome_reps[0] if rome_reps else ('rome-syllabus' if ROME else 'm55'))
        TAB = 'rome' if ROME else 'greece'   # P70: the tablet pass reads the second course's home, or Greece's in an edition without Rome
        ctx.close()

        # ---- tablet: wider column, two-column cards, the drawer still a drawer -----------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'tablet', 768, 1024, True)
        if lay[0] != 768: fails.append(f'tablet layout {lay}: expected width 768')
        check_panels(pg, 'tablet', fails)
        pg.evaluate(f"location.hash = '{TAB}'"); ready(pg); pg.wait_for_timeout(50)
        t = pg.evaluate('''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
          return {off: r.right <= 0, menu: getComputedStyle(document.getElementById('menuB')).display !== 'none',
                  main: document.querySelector('main').getBoundingClientRect().width,
                  cols: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(document.querySelector('#''' + TAB + ''' .part .cgrid')).gridTemplateColumns),
                  home: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(document.querySelector('#home .track .cgrid')).gridTemplateColumns)}; }''')
        if not t['off']: fails.append('tablet: drawer is on screen before the menu button is pressed')
        if not t['menu']: fails.append('tablet: menu button hidden')
        if not 740 <= t['main'] <= 768: fails.append(f'tablet: main column {t["main"]}px, expected about 760')
        if t['cols'] != 2: fails.append(f'tablet: unit cards in {t["cols"]} column(s), expected 2')
        if t['home'] != 2: fails.append(f'tablet: course cards in {t["home"]} column(s), expected 2')
        pg.click('#menuB'); pg.wait_for_timeout(300)
        d = pg.evaluate('''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
          return {left: r.left, w: r.width, backdrop: getComputedStyle(document.getElementById('backdrop')).opacity}; }''')
        if d['left'] != 0 or not 340 <= d['w'] <= 360: fails.append(f'tablet: open drawer at {d}')
        if float(d['backdrop']) < 0.9: fails.append('tablet: backdrop not shown behind the open drawer')
        pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed'))")
        res = pg.evaluate(BOX_JS, ['#drawer', GAP])
        if res['nbad']: fails.append('tablet drawer: ' + '; '.join(res['bad']))
        small = pg.evaluate(TARGET_JS, '#' + TAB)
        if small: fails.append('tablet drawer targets: ' + '; '.join(small[:6]))
        pg.click('#closeB'); pg.wait_for_timeout(300)
        if not pg.evaluate("document.getElementById('drawer').getBoundingClientRect().right <= 0"): fails.append('tablet: drawer did not close')
        # a report, reached through the shell (P13): the column and measure once the fetch has landed
        pg.evaluate(f"location.hash = '{rp}'"); ready(pg); pg.wait_for_timeout(50)
        tr = pg.evaluate(f"""() => ({{loaded: document.getElementById('{rp}').hasAttribute('data-loaded'),
          main: document.querySelector('main').getBoundingClientRect().width,
          sw: document.documentElement.scrollWidth - document.documentElement.clientWidth,
          ps: document.querySelectorAll('#{rp} .report p').length}})""")
        if not tr['loaded'] or not tr['ps']: fails.append(f'tablet: report {rp} not loaded through the shell: {tr}')
        if not 740 <= tr['main'] <= 768 or tr['sw'] > 0: fails.append(f'tablet: report {rp} column {tr["main"]}px, horizontal scroll {tr["sw"]}px')
        print('tablet: drawer is a drawer (off screen, 360 px with backdrop when open); column', t['main'], 'px; report', rp, 'loaded through the shell,', tr['ps'], 'paragraphs')
        ctx.close()

        # ---- desktop: persistent sidebar ----------------------------------------------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'desktop', 1280, 800, False)
        if lay[0] != 1280: fails.append(f'desktop layout {lay}: expected width 1280')
        check_panels(pg, 'desktop', fails)
        pg.evaluate("location.hash = 'm23'"); ready(pg); pg.wait_for_timeout(80)
        s = pg.evaluate('''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
          const main = document.querySelector('main').getBoundingClientRect(), top = document.querySelector('.top').getBoundingClientRect();
          const act = d.querySelector('[data-navctx]:not([hidden]) .ditem.is-active');
          const list = d.querySelector('[data-navctx]:not([hidden])');
          return {left: r.left, w: r.width, h: r.height, vh: innerHeight, hidden: d.getAttribute('aria-hidden'),
                  menu: getComputedStyle(document.getElementById('menuB')).display, close: getComputedStyle(document.getElementById('closeB')).display,
                  backdrop: getComputedStyle(document.getElementById('backdrop')).display,
                  mainLeft: main.left, mainW: main.width, topLeft: top.left, topRight: top.right,
                  active: act ? act.dataset.target : null, listScroll: list ? getComputedStyle(list).overflowY : null,
                  measure: getComputedStyle(document.querySelector('#m23 .report p')).maxWidth,
                  ch68: (() => { const p = document.querySelector('#m23 .report p'), t = document.createElement('span');
                    t.style.whiteSpace = 'nowrap'; t.textContent = '0'.repeat(68); p.appendChild(t); const w = t.getBoundingClientRect().width; t.remove(); return w; })(),
                  fonts: ['DM Sans', 'Space Mono', 'Gentium Book Plus'].filter(n => ![...document.fonts].some(f => f.family.replace(/"/g, '') === n && f.status === 'loaded')),
                  home: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(document.querySelector('#home .track .cgrid')).gridTemplateColumns),
                  ml: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(document.querySelector('#home .ml-grid')).gridTemplateColumns)}; }''')
        if s['left'] != 0 or s['w'] != SIDE or s['h'] < s['vh'] - 1: fails.append(f'desktop: sidebar not at the left edge, {SIDE} px, full height: {s}')
        if s['hidden'] != 'false': fails.append(f'desktop: sidebar aria-hidden={s["hidden"]}')
        if s['menu'] != 'none' or s['close'] != 'none': fails.append(f'desktop: menu/close buttons shown ({s["menu"]}, {s["close"]})')
        if s['backdrop'] != 'none': fails.append('desktop: backdrop present')
        if s['mainLeft'] < SIDE: fails.append(f'desktop: content starts at {s["mainLeft"]}px, under the sidebar')
        if not 740 <= s['mainW'] <= 768: fails.append(f'desktop: main column {s["mainW"]}px, expected about 760')
        if s['topLeft'] != SIDE or s['topRight'] != 1280: fails.append(f'desktop: top bar spans {s["topLeft"]}..{s["topRight"]}, expected {SIDE}..1280')
        if s['active'] != 'm23': fails.append(f'desktop: sidebar does not highlight the current report ({s["active"]})')
        if s['listScroll'] != 'auto': fails.append(f'desktop: sidebar list overflow-y {s["listScroll"]}, expected auto')
        # P39: the measure is 68ch of the report's own font (DM Sans, about 744 px), and fits the 760 px column
        mw = float(s['measure'].replace('px', '')) if s['measure'].endswith('px') else 0
        if abs(mw - s['ch68']) > 2 or not 560 <= mw <= s['mainW']: fails.append(f'desktop: report measure {s["measure"]}, expected 68ch ({s["ch68"]:.0f} px) inside the {s["mainW"]:.0f} px column')
        if s['fonts']: fails.append(f'desktop: theme fonts not loaded from fonts/: {s["fonts"]}')
        if s['home'] != 2 or s['ml'] != 2: fails.append(f'desktop: home course cards {s["home"]} col, mythos/logos {s["ml"]} col, expected 2 and 2')
        # the sidebar's own targets and gaps, every unit open
        pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed'))")
        res = pg.evaluate(BOX_JS, ['#drawer', GAP])
        if res['nbad']: fails.append('desktop sidebar: ' + '; '.join(res['bad']))
        sw = pg.evaluate('document.getElementById("drawer").scrollWidth <= document.getElementById("drawer").clientWidth')
        if not sw: fails.append('desktop sidebar: horizontal overflow')
        print(f'desktop: sidebar {s["w"]} px at the left, content column {s["mainW"]} px from {s["mainLeft"]} px, current item {s["active"]}, measure {s["measure"]}')
        ctx.close()

        # P91: the home and What's new at 320, 360 and 430 px (390 is the phone pass above), tablet and desktop, dark and
        # light; P92: on the desktop a history tile, a markdown tile, the IA tile and the hero's What's new link each open
        # their page
        for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS[1:]:
            ctx, pg, _ = new_page(p, br, errors, name, w, h, mobile)
            check_home(pg, name, fails, EXPECT)
            check_new(pg, name, fails, EXPECT)
            pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
            check_home(pg, name + ' light', fails, EXPECT)
            if name == 'desktop':
                for sel in ('a.course.live[data-target="greece"]', 'a.course.live[data-target^="brand-"]', 'a.course.live[data-target^="ux-"]', 'a.hnew'):   # P92: a tile of each family and the quiet link
                    pg.evaluate("location.hash = 'home'"); ready(pg); pg.wait_for_timeout(60)
                    t = pg.evaluate(f"(() => {{ const a = document.querySelector('#home {sel}'); return a && a.getAttribute('data-target'); }})()")
                    if not t:
                        continue
                    pg.click(f'#home {sel}'); pg.wait_for_timeout(300); ready(pg); pg.wait_for_timeout(300)
                    land = pg.evaluate(LAND_JS, t)
                    if not land[1] or (land[2] is not None and not (-5 if land[0] == t else 56) <= land[2] <= land[4]) or land[3] is False:   # an id inside a page stops clear of the 56 px bar
                        fails.append(f'home desktop: tapping {sel} (#{t}) lands on {land}')
                    else:
                        print(f'home desktop: {sel} opens #{t} on {land[0]}, at {land[2]} px' + (', its card open' if land[3] else ''))
            ctx.close()

        # P93: the course homes, What's new and the pages without a topography, at every width, dark and light, under
        # reduced motion: each page's topography and tiles against the sources (check_topo, check_tiles), two history
        # unit tiles opened (their rows, their line whole); the home's tiles too
        TOPO_PAGES = [x for x in ('greece', 'rome', 'brand-a', 'brand-b', 'ux-ia') if x in HAS or x in EXPECT['courses']] + ['new']
        NONE_PAGES = [x for x in ('changelog', 'backlog', 'viz-examples') if (x != 'viz-examples' or 'figures' not in OMIT) and (x not in ('changelog', 'backlog') or x not in OMIT)]
        for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS:
            ctx, pg, _ = new_page(p, br, errors, name + ' pages', w, h, mobile)
            reads = pg.evaluate("""() => { const seen = {}, out = []; document.querySelectorAll('.panel[data-kind="report"]').forEach(p => { const c = p.getAttribute('data-ctx'); if (!seen[c]) { seen[c] = 1; out.push(p.id); } }); return out; }""")
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                pg.evaluate("location.hash = 'home'"); ready(pg); pg.wait_for_timeout(120)
                pg.evaluate("document.querySelectorAll('#planned-courses').forEach(d => d.open = true)"); pg.wait_for_timeout(60)
                check_topo(pg, 'home', f'{name} {theme}', fails, EXPECT); check_tiles(pg, 'home', f'{name} {theme}', fails, EXPECT)
                pg.evaluate("document.querySelectorAll('#planned-courses').forEach(d => d.open = false)")
                for pid in TOPO_PAGES + NONE_PAGES + reads:
                    pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
                    t = check_topo(pg, pid, f'{name} {theme}', fails, EXPECT)
                    if pid in TOPO_PAGES and pid != 'new':
                        pg.evaluate(f"document.querySelectorAll('#{pid} details[data-mods]').forEach((d, k) => d.open = k < 2)"); pg.wait_for_timeout(60)
                        tl = check_tiles(pg, pid, f'{name} {theme}', fails, EXPECT)
                        pg.evaluate(f"document.querySelectorAll('#{pid} details[data-mods]').forEach(d => d.open = false)")
                        if theme == 'dark': print(f"{pid} {name}: layer {t['hero'] and t['hero']['bytes']} B, layout {t['hero'] and t['hero']['shown']}, frame {t['hero'] and t['hero'].get('frame')}; {len(tl['tiles'])} tiles, {len(t['patches'])} patches, grids {tl['grids'][:2]}")
                    elif pid == 'new' and theme == 'dark':
                        print(f"new {name}: layer {t['hero'] and t['hero']['bytes']} B, layout {t['hero'] and t['hero']['shown']}, frame {t['hero'] and t['hero'].get('frame')}, days {[(l, k) for l, _, k, _, _ in t['hero']['layouts'][0][1]] if t['hero'] else None}")
            ctx.close()

        # P92: with motion allowed, at every width, dark and light: only transform and opacity animate, the cycling area
        # line shows and the static line is for a screen reader only; the hero's texts over the contours; and at 390 px
        # the weight of a fresh load (LCP and the longest task, from the browser's performance entries). P93: on every
        # page: every contour drawing moves (the hero's layer and every tile's patch, transform only, each at its own
        # point of the cycle; nothing else on a page without one), and at the five poses of the sweep every layer covers
        # its frame, every rise and patch stays inside it, and every text over a topography keeps its contrast; LCP and
        # the longest task on the home, a course home and What's new
        def perf_of(pg, pid):
            pg.evaluate(f"localStorage.clear(); location.hash = '{pid}'")
            pg.evaluate('''() => { window.__p92 = {lcp: 0, lt: 0, n: 0}; }''')
            pg.reload(); pg.wait_for_timeout(100)
            pg.evaluate('''() => { window.__p92 = {lcp: 0, lt: 0, n: 0};
              new PerformanceObserver(l => l.getEntries().forEach(e => { window.__p92.lcp = Math.max(window.__p92.lcp, e.startTime); })).observe({type: 'largest-contentful-paint', buffered: true});
              new PerformanceObserver(l => l.getEntries().forEach(e => { window.__p92.lt = Math.max(window.__p92.lt, e.duration); window.__p92.n++; })).observe({type: 'longtask', buffered: true}); }''')
            pg.wait_for_timeout(3000)
            return pg.evaluate('window.__p92')
        PERF = {}
        for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS:   # P92 check: every width, not two
            ctx, pg, _ = new_page(p, br, errors, name + ' motion', w, h, mobile, motion=True)
            if name == 'phone':
                for pid in ('home', 'greece', 'new'):
                    PERF[pid] = perf_of(pg, pid)
                    print(f"{pid} phone motion: LCP {PERF[pid]['lcp']:.0f} ms, longest task {PERF[pid]['lt']:.0f} ms ({PERF[pid]['n']} long tasks over 50 ms), on a fresh load from the local server")
                pg.evaluate("location.hash = 'home'"); ready(pg)
                # P93 follow-up (Pedro, 4 Nov 2026, 20:16: "The animations dont work, at least on mobile"): at 120 s a sweep the
                # move ran, at 0.6 px/s at most, and read as still. The move must be seen and still be slow: the peak speed of a
                # corner of the home's layer at 390 px, from the tokens (turn, growth, cycle; CSS ease-in-out peaks at 1.6 times
                # the average), between 2 and 8 px/s; and the layer must have moved between two reads 2 s apart
                fw, fh = pg.evaluate("(() => { const t = document.querySelector('#home .hhome > .topo'); return [t.clientWidth, t.clientHeight]; })()")
                rc = math.hypot(fw, fh) / 2
                v = 1.6 * rc * math.hypot(math.radians(2 * TURN) / (CYCLE / 1000), (GROW - 1) / (BTIME / 1000))   # the turn and the breath, each at its peak
                m0 = pg.evaluate("getComputedStyle(document.querySelector('#home .hhome > .topo .topo-tall')).transform"); pg.wait_for_timeout(2000)
                m1 = pg.evaluate("getComputedStyle(document.querySelector('#home .hhome > .topo .topo-tall')).transform")
                print(f"home phone motion: the move peaks at {v:.1f} px/s at the layer's corners ({fw} x {fh} px frame, {2 * TURN:g} degrees over {CYCLE / 1000:g} s, a breath to {GROW:g} over {BTIME / 1000:g} s); moved in 2 s: {m0 != m1}")
                if not 2 <= v <= 12: fails.append(f"home phone motion: the move peaks at {v:.1f} px/s at the layer's corners, outside 2 to 12 px/s (seen, and still slow; Pedro, 5 Nov 2026: \"it could be faster\")")
                if m0 == m1: fails.append('home phone motion: the layer did not move in 2 s')
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate("localStorage.setItem('hellas-theme', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                pg.evaluate("location.hash = 'new'"); ready(pg); pg.evaluate("location.hash = 'home'"); ready(pg); pg.wait_for_timeout(200)   # the home shown afresh, each drawing at its own phase, before any pose
                check_topo(pg, 'home', f'{name} motion {theme}', fails, EXPECT, motion=True)
                check_home(pg, name + (' motion' if theme == 'dark' else ' motion light'), fails, EXPECT, motion=True)
                for p_ in POSES:
                    pose(pg, p_, 1500)
                    check_topo(pg, 'home', f'{name} motion {theme} pose {p_:g}', fails, EXPECT, motion=True, phase=False)
                pg.evaluate("() => document.getAnimations().forEach(a => a.play())")
                for pid in TOPO_PAGES + NONE_PAGES:
                    pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(250)
                    check_topo(pg, pid, f'{name} motion {theme}', fails, EXPECT, motion=True)
                    if pid in TOPO_PAGES:
                        lows = []
                        for p_ in POSES:
                            pose(pg, p_)
                            check_topo(pg, pid, f'{name} motion {theme} pose {p_:g}', fails, EXPECT, motion=True, phase=False)
                            lows.append(texts_contrast(pg, pid, f'{name} motion {theme}', fails, f' pose {p_:g}'))
                        pg.evaluate("() => document.getAnimations().forEach(a => a.play())")
            ctx.close()

        if SHOTS:
            SHOTS.mkdir(parents=True, exist_ok=True)
            for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS:   # P91: the home and What's new at 320, 360 and 430 px too
                ctx, pg, _ = new_page(p, br, [], name, w, h, mobile)
                for theme in ('dark', 'light'):
                    pg.evaluate(f"localStorage.setItem('hellas-theme', '{theme}')")
                    COURSE_SHOTS = ['home', 'new'] + TOPO_PAGES[:-1]   # P93: the home, What's new and every course home at every width
                    for pid in ((COURSE_SHOTS + [x for x in PAGES if x not in COURSE_SHOTS]) if name.startswith('phone3') or name == 'phone430' else COURSE_SHOTS + [x for x in [TAB, rp] + PAGES if x not in COURSE_SHOTS]):
                        pg.evaluate(f"localStorage.removeItem('pm-sec-{pid}')")   # P68: each shot opens on section 1
                        if pid == 'home':   # P90: the home is shot as a fresh visit (P91: nothing on it depends on the visit, but the shot stays clean)
                            pg.evaluate(f"localStorage.clear(); localStorage.setItem('hellas-theme', '{theme}')")
                        pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(250); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(50)
                        if pid == 'home':   # P90: the home whole, to New since and the changelog link at its foot (it is a few screens long)
                            pg.screenshot(path=str(SHOTS / f'{name}-{pid}-{theme}.png'), full_page=True, timeout=120000)
                        else:
                            shoot(pg, SHOTS / f'{name}-{pid}-{theme}.png', w, h)
                        if pid in PAGES and pg.query_selector(f'[id="{pid}"] .report.steps'):   # P68: the reading states the top does not show
                            for state, js in READING_SHOTS:
                                pg.evaluate(js, pid); pg.wait_for_timeout(200)
                                pg.screenshot(path=str(SHOTS / f'{name}-{pid}-{state}-{theme}.png'))
                            pg.evaluate("(pid) => { const p = document.getElementById(pid); p.querySelectorAll('details').forEach(d => d.open = false); const w = p.querySelector('.stepbar .whole'); if (w.getAttribute('aria-pressed') === 'true') w.click(); [...p.querySelectorAll('.seclist a')][0].click(); window.scrollTo(0, 0); }", pid)
                        if pid in PAGES:   # P41: each figure of a --page panel, as the reader sees it in its frame (P91: the home has no figure; P92: its contours are not figures, and are in the home shot and the motion sheets)
                            for k, fig in enumerate(pg.query_selector_all(f'[id="{pid}"] figure.viz')):
                                kind = ([c for c in fig.get_attribute('class').split() if c.startswith('viz-') and c != 'viz-wide'] or ['viz-figure'])[0][4:]
                                fig.evaluate("f => { const s = f.closest('.sec'), p = f.closest('.panel'); if (s && !s.classList.contains('on')) p.querySelector('.seclist a[data-step=\"' + s.dataset.step + '\"]').click(); }")   # P68: its section shown first
                                fig.scroll_into_view_if_needed(); pg.wait_for_timeout(30)
                                fig.screenshot(path=str(SHOTS / f'{name}-{pid}-fig-{k + 1:02d}-{kind}-{theme}.png'), timeout=120000)
                                nf = frames(pg, fig, SHOTS / f'{name}-{pid}-fig-{k + 1:02d}-{kind}-frames-{theme}.png', f'{name} · {pid} · figure {k + 1} · {theme}')   # P89
                                print(f'shots: {name} {pid} figure {k + 1} ({kind}) {theme}: {nf} frame' + ('s' if nf != 1 else ''))
                            pg.evaluate('window.scrollTo(0, 0)')
                ctx.close()
            # P92: the hero at five moments; P93: at the five poses of the slow move (POSES: the two ends of the sweep,
            # its quarters and its middle; the home's area line at 0, 3, 6, 9 and 12 s of its cycle), at 390 and 1280 px
            # with motion allowed, dark and light, for the home, a history course home (Greece) and a markdown course
            # home (Information architecture): every animation paused and set to the pose, the hero shot, the five
            # stacked with their times in one sheet (<width>-<page>-motion-<theme>.png)
            from PIL import Image, ImageDraw, ImageFont
            for name, w, h, mobile in (('phone', 390, 844, True), ('desktop', 1280, 800, False)):
                ctx, pg, _ = new_page(p, br, [], name, w, h, mobile, motion=True)
                for pid in [x for x in ('home', 'greece', 'ux-ia') if x == 'home' or x in TOPO_PAGES]:
                    sel = '#home .hhome > .topo' if pid == 'home' else f'#{pid} > header.hero > .topo'   # the layer's own frame: from the top bar to the hero's foot, the full width beside the sidebar (the hero's box is the column), the texts on it
                    for theme in ('dark', 'light'):
                        pg.evaluate(f"localStorage.clear(); localStorage.setItem('hellas-theme', '{theme}')"); pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(500)
                        ims, tags = [], []
                        for k, p_ in enumerate(POSES):
                            pose(pg, p_, k * 3000); pg.wait_for_timeout(60)
                            tmp = SHOTS / f'_{name}-{pid}-{k}.png'
                            pg.locator(sel).screenshot(path=str(tmp), animations='allow')
                            ims.append(Image.open(tmp)); tmp.unlink()
                            tags.append(f'{name} · {pid} · {theme} · pose {k + 1} of 5: {p_:g} of the sweep ({p_ * CYCLE / 1000:.0f} s of {CYCLE / 1000:.0f} s: turn {-TURN + 2 * TURN * eased(p_):+.2f}°, scale {1 + (GROW - 1) * eased(p_):.3f})' + (f'; area line at {k * 3:.0f} s of its 12 s cycle' if pid == 'home' else ''))
                        sc = max(1, round(ims[0].width / pg.evaluate(f"document.querySelector('{sel}').getBoundingClientRect().width")))
                        font, band = ImageFont.load_default(size=12 * sc), 26 * sc
                        sheet = Image.new('RGB', (ims[0].width, sum(i.height + band for i in ims)), (128, 128, 128))
                        d, y = ImageDraw.Draw(sheet), 0
                        for im, tg in zip(ims, tags):
                            d.text((6 * sc, y + 6 * sc), tg, fill=(0, 0, 0), font=font); y += band; sheet.paste(im, (0, y)); y += im.height
                        sheet.save(SHOTS / f'{name}-{pid}-motion-{theme}.png')
                        print(f'shots: {name} {pid} motion sheet, {theme}')
                ctx.close()
            # V1: each figure of the examples page as the reader sees it in its frame, then one sheet per width and theme
            for name, w, h, mobile in (VIEWPORTS if 'figures' not in OMIT else []):
                ctx, pg, _ = new_page(p, br, [], name, w, h, mobile)
                for theme in ('dark', 'light'):
                    pg.evaluate(f"localStorage.setItem('hellas-theme', '{theme}')")
                    pg.goto(URL + '#viz-examples'); pg.reload(); ready(pg); pg.wait_for_timeout(250)
                    shots = []
                    for k, fig in enumerate(pg.query_selector_all('#viz-examples figure.viz')):
                        kind = [c for c in fig.get_attribute('class').split() if c.startswith('viz-') and c != 'viz-wide'][0][4:]
                        fig.scroll_into_view_if_needed(); pg.wait_for_timeout(30)
                        path = SHOTS / f'{name}-viz-{k + 1:02d}-{kind}-{theme}.png'
                        fig.screenshot(path=str(path)); shots.append(path)
                    try:
                        from PIL import Image
                        ims = [Image.open(x) for x in shots]
                        sheet = Image.new('RGB', (max(i.width for i in ims), sum(i.height for i in ims) + 12 * len(ims)), (10, 10, 12) if theme == 'dark' else (232, 228, 220))   # the page colour of each theme (P90: the light paper)
                        yy = 0
                        for im in ims:
                            sheet.paste(im, (0, yy)); yy += im.height + 12
                        sheet.save(SHOTS / f'{name}-viz-examples-{theme}.png')
                    except ImportError:
                        pass
                ctx.close()
            print('screenshots in', SHOTS)
        br.close()
    errs = [e for e in errors if 'fonts.g' not in e]
    if errs: fails.append('console errors: ' + ' | '.join(errs[:5]))
    ix = index_check.check()   # A5: docs/courses-index.md against the sources it summarises
    fails += ['courses-index.md: ' + x for x in ix]
    print('courses-index.md: ' + (f'{len(ix)} mismatches' if ix else 'matches the sources'))
    pt = private_terms.check()   # G-0 (11 Nov 2026): no private term in a public course's vault, data folder or built pages
    fails += ['private term in a public course: ' + x for x in pt]
    print('private terms in the public courses: ' + (f'{len(pt)} found' if pt else 'none'))
    rf, rw = rot_check.check()   # P30-F11, P30-F16 (17 Nov 2026)
    fails += ['rot: ' + x for x in rf]
    print('rot check: ' + (f'{len(rf)} failures' if rf else 'none') + ''.join('\n  warn ' + x for x in rw))
    print('\n'.join('FAIL ' + f for f in fails) if fails else 'ALL CHECKS PASSED')
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main())
