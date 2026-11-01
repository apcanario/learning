"""Browser checks for academy/, the Academy site (run after build.py).

python3 verify.py [--shots DIR] [--page ID ...]
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
accordion) and the Backlog page; the same panel checks again in the light theme. Tablet: the drawer is still a drawer (off screen until the menu button, 360 px, backdrop).
Desktop: the drawer is a persistent 300 px sidebar (no backdrop, no menu button, current item highlighted, scrolls on
its own) and the top bar spans the content column. Figures (P44): at phone width every figure draws at its natural size
and its frame scrolls to the whole drawing; the cue line shows exactly on the frames that overflow (phone and desktop). With --shots, saves dark and light screenshots (the top 2,600 px, captured from a viewport that tall, P35) at the three widths
of home, Rome and one Rome report, plus every panel id given with --page (a new unit's reading page, a new course home),
and (P41) each figure in a --page panel on its own: <width>-<panel>-fig-<nn>-<kind>-<theme>.png.
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
Centred drawings (P50): every sitemap, objects, decision, states and wireflow figure whose drawing starts more than 12 units
in carries data-x0 where it starts, so a phone frame opens on it.
Figure keys (P52): every viz block in the vault, every history figure declaration, every course home figure and every
examples block uses only the keys viz.VIZ_KEYS documents for its kind, and viz.render leaves the block it draws unchanged.
Opening notes (P73): a markdown unit's text before its first heading is a closed accordion after Sources, "The writer's
opening note", on every unit that has one and on none that has not; section 1 opens on its heading; a deep link lands.
Last, index_check.py: docs/courses-index.md against the syllabi, provenance, the vault and the data files (A5).
"""
import sys, json, pathlib, re, threading, functools, html as H
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
import index_check   # (P39: the browser gets the theme fonts from fonts/, never the network)
from courses import COURSES, THEMES
import viz, viz_examples   # P55: the examples page's hard cases and the blocks that must stop the build
# each track and its course cards as the home must show them, from courses.py (A5: a new course needs no edit here)
HOME_TRACKS = [t['name'] + ':' + ','.join(
    ['#' + c['home_id'] for c in COURSES if c['family'] == 'history' and c['theme'] == t['id']]
    + ['#' + f"{c.get('prefix', c['id'])}-{k.lower()}" for c in COURSES if c['family'] == 'markdown'
       for k, (tr, _) in c['tracks'].items() if tr == t['id']]) for t in THEMES]

R = pathlib.Path(__file__).resolve().parent
SITE = R / 'academy'
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
    const svg = f.querySelector('svg'); if (!svg || f.clientWidth === 0) return; n++;
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
  });
  return {n, over, bad: bad.slice(0, 8)};
}'''

SHOT_H = 2600
def shoot(pg, path, w, h):
    """The top SHOT_H px of the page (P35, 1 Nov 2026). A full-page capture renders the whole document before it clips,
    which on a long unit at device scale 3 took 80 s (DD-B3, about 10,300 words) and failed past the timeout on longer
    pages; the viewport is made SHOT_H tall and captured as it is, then put back, so the time no longer grows with the
    page."""
    pg.set_viewport_size({'width': w, 'height': SHOT_H}); pg.wait_for_timeout(120)
    pg.screenshot(path=str(path), full_page=False, timeout=60000)
    pg.set_viewport_size({'width': w, 'height': h}); pg.wait_for_timeout(60)

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

def new_page(p, br, errors, name, w, h, mobile):
    ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=3 if mobile else 1,
                         is_mobile=mobile, has_touch=mobile)  # a real phone or tablet honours the viewport tag
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
    # every report and syllabus panel, a markdown course's briefs and bibliography pages, a history course home (a
    # course panel whose label is a numbered course; Brand + AI homes are lettered and stay) and every course's
    # "How it was built" page leave the shell (A2, P20, P22, A4)
    must = [h for h in heads if ' data-kind="report"' in h or ' data-kind="syllabus"' in h or re.search(r' id="(briefs-[a-z]+|[a-z-]+-briefs|[a-z-]+-bibliography|[a-z-]+-built)"', h)
            or (' data-kind="course"' in h and re.search(r' data-u="COURSE \d', h)) or ' id="viz-examples"' in h]
    kept = [h[:80] for h in must if ' data-src="' not in h]
    if kept: fails.append(f'split: {len(kept)} panels should be fetched but are in the shell: {kept[:2]}')
    if len(srcs) != len(must): fails.append(f'split: {len(must)} panels should be fetched but {len(srcs)} carry data-src')
    noanch = [h[:80] for h in must if ' data-src="' in h and ' data-kind="report"' not in h and ' data-anchors="' not in h]
    if noanch: fails.append(f'split: fetched panels without data-anchors: {noanch[:2]}')
    stubs = re.findall(r'(<section class="panel[^"]*"[^>]* data-src="[^"]+"[^>]*>)(.*?)</section>', shell, re.S)
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
    table = re.search(r'<!-- sizes:start -->\n(.*?)<!-- sizes:end -->', (R / 'README.md').read_text(), re.S)
    kb = lambda n: f'{n / 1024:,.0f} KB' if n < 1024 * 1024 else f'{n / 1024 / 1024:.2f} MB'
    if not table: fails.append('README.md has no size table (sizes:start/sizes:end)')
    else:
        rows = {r.split(' | ')[0].strip('| '): r for r in table.group(1).splitlines()}
        want = {'Shell (`index.html`)': f'| 1 | {kb(size)} | {kb(size)} |'}
        for ctx, fs in by.items():
            want[next((k for k in rows if f'(`{ctx}/`)' in k), ctx)] = f'| {len(fs)} | {kb(sum(n for n, _ in fs))} | {kb(max(fs)[0])} | largest `{max(fs)[1]}`'
        bad = [k for k, v in want.items() if k not in rows or v not in rows[k]]
        if bad: fails.append(f'README.md size table does not match the files: {bad} (rebuild)')
    vx = SITE / 'viz-examples.html'   # V1: the figure examples page, one figure of every kind in viz.py
    if not vx.exists(): fails.append('viz-examples.html: missing (viz_examples.py, run from build.py)')
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
        if kind == 'timeline':                               # P58 (by eye): no stem runs through another event's text
            import viz as V
            stems = [(float(a), float(b), float(c)) for a, b, c in re.findall(r'<line class="viz-stem" x1="([-\d.]+)" y1="([-\d.]+)" x2="[-\d.]+" y2="([-\d.]+)"', svg)]
            for c, x, y, a, t in re.findall(r'<text class="viz-(label|date)" x="([-\d.]+)" y="([-\d.]+)" text-anchor="(\w+)">(.*?)</text>', svg):
                x, y, t = float(x), float(y), H.unescape(re.sub(r'<[^>]+>', '', t))
                w = V._tw(t, 12, 'sans') if c == 'label' else V._tw(t, 10.5, 'mono')
                x0 = {'start': x, 'middle': x - w / 2, 'end': x - w}[a]
                if any(x0 + 1 < sx < x0 + w - 1 and y1 < y - 4 < y2 for sx, y1, y2 in stems):
                    bad.append(f'{where}: a stem runs through the text "{t}"')
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
        if c['family'] == 'markdown' and (R.parent / c['vault']).is_dir():
            for f in sorted((R.parent / c['vault']).glob('*.md')):
                for i, m in enumerate(viz._FENCE.finditer(f.read_text()), 1):
                    one(f'{c["vault"]}/{f.name} block {i}', json.loads(m.group(1)))
        elif c['family'] == 'history':
            for f in sorted((R / c['id']).glob('r-*.html')):
                for i, m in enumerate(viz._FIG.finditer(f.read_text()), 1):
                    one(f'{c["id"]}/{f.name} figure {i}', json.loads(m.group(2)), m.group(1))
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
    sec = fresh_land(pg, 'rm12-2', retried)
    if sec[0] != 'rm12' or not sec[1] or not -5 <= sec[2] <= 200: fails.append(f'split: #rm12-2 on a fresh load gave panel {sec[0]}, section found {sec[1]}, top {sec[2]}')
    # a syllabus is a stub too (P20): empty until opened, fetched once, its prompts and copy buttons present
    stub = pg.evaluate("(() => { const p = document.getElementById('rome-syllabus'); return [p.getAttribute('data-src'), p.innerHTML.length, (p.getAttribute('data-anchors') || '').split(' ').includes('rs-u3')]; })()")
    if stub != ['rome/syllabus.html', 0, True]: fails.append(f'split: #rome-syllabus before opening is {stub}, expected an empty stub fetching rome/syllabus.html with its anchors')
    pg.evaluate("location.hash = 'rome-syllabus'"); ready(pg)
    got = pg.evaluate("[document.getElementById('rome-syllabus').hasAttribute('data-loaded'), document.querySelectorAll('#rome-syllabus article.smod pre').length, document.querySelectorAll('#rome-syllabus button.copy').length]")
    if not (got[0] and got[1] >= 80 and got[1] == got[2]): fails.append(f'split: #rome-syllabus after opening (loaded, prompts, copy buttons) = {got}')
    pg.evaluate("location.hash = 'rome'"); ready(pg); pg.evaluate("location.hash = 'rome-syllabus'"); ready(pg)
    if hits.get('/rome/syllabus.html') != 1: fails.append(f'split: rome/syllabus.html fetched {hits.get("/rome/syllabus.html")} times, expected once')
    # a link into an unopened syllabus (a unit anchor) and into unopened briefs (a brief's card), on a fresh load
    for h, want in (('rs-u3', 'rome-syllabus'), ('s-m23', 'syllabus'), ('b-a2', 'briefs-a'), ('b-b3', 'briefs-b'), ('greece-u3', 'greece'), ('rome-u1', 'rome')):
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
    stub = pg.evaluate("(() => { const p = document.getElementById('rome'); return [p.getAttribute('data-src'), (p.getAttribute('data-anchors') || '').split(' ').includes('rome-u3')]; })()")
    if stub != ['rome/home.html', True]: fails.append(f'split: #rome stub is {stub}, expected rome/home.html with its unit-card anchors')
    pg.evaluate("localStorage.clear()"); pg.goto(URL + '#greece'); pg.reload(); ready(pg); pg.wait_for_timeout(100)
    hm = pg.evaluate("[document.getElementById('greece').hasAttribute('data-loaded'), document.querySelectorAll('#greece details.ucard').length, document.querySelectorAll('#greece details.ucard[open]').length, document.querySelector('#greece .hbtn.cont').hidden, document.querySelector('#greece .hbtn.start').hidden]")
    if not (hm[0] and hm[1] >= 10 and hm[2] == 1 and hm[3] and not hm[4]): fails.append(f'split: #greece on a fresh load (loaded, cards, cards open, continue hidden, start shown) = {hm}')
    n0 = hits.get('/greece/home.html', 0)   # fetched once on this load (earlier fresh loads fetched it too)
    pg.evaluate("location.hash = 'm23'"); ready(pg); pg.evaluate("location.hash = 'greece'"); ready(pg); pg.wait_for_timeout(50)
    hm = pg.evaluate("[document.querySelector('#greece .hbtn.cont').hidden, document.querySelector('#greece .hbtn.cont b').textContent, document.querySelector('#greece .hbtn.start').hidden]")
    if hm[0] or not hm[1].startswith('2.3 ') or not hm[2]: fails.append(f'split: #greece continue after reading 2.3 (continue hidden, label, start hidden) = {hm}')
    if hits.get('/greece/home.html', 0) != n0: fails.append(f'split: greece/home.html fetched again on a second visit ({hits.get("/greece/home.html")} in all)')
    fail['home'] = True
    pg.evaluate("location.hash = 'rome'"); ready(pg)
    st = pg.evaluate("[document.getElementById('rome').hasAttribute('data-failed'), !!document.querySelector('#rome a.hbtn[data-target=\"rome\"]')]")
    if st != [True, True]: fails.append(f'split: failed course-home fetch state (failed, retry button) = {st}')
    fail['home'] = False
    pg.click('#rome a.hbtn[data-target="rome"]'); ready(pg); pg.wait_for_timeout(50)
    if not pg.evaluate("document.getElementById('rome').hasAttribute('data-loaded') && document.querySelectorAll('#rome details.ucard').length > 5"): fails.append('split: retry after a failed course-home fetch did not load the home')
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
    const svg = f.querySelector('svg'), vb = svg.viewBox.baseVal, T = 0.6;
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

def check_figures(br, fails):
    """The examples page (V1) through the shell: VX_FIGS figures, one per kind, and the geometry of each (FIG_JS)."""
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
        check_reading(br, fails)

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
        pg.click('#home a.hbtn[href="#changelog"]'); pg.wait_for_timeout(80)
        step('changelog', dict(id='changelog', nav='root', u='ACADEMY', t='Changelog', arrows=False))
        pg.click('#homeB'); pg.wait_for_timeout(80)
        pg.click('#home a.course[href="#rome"]'); pg.wait_for_timeout(80)
        step('rome home', dict(id='rome', nav='rome', u='COURSE 2', t='Rome', arrows=True, prev=False, next=True))
        rome_reps = pg.eval_on_selector_all('#rome a.hrow', 'as => as.map(a => a.dataset.target)')
        if rome_reps:
            pg.evaluate("document.querySelectorAll('#rome details.ucard').forEach(d => d.open = true)")
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
        for cid in ('greece', 'rome'):
            pg.evaluate(f"location.hash = '{cid}-built'"); pg.wait_for_timeout(50)
            step(f'{cid} how it was built', dict(id=f'{cid}-built', nav=cid, t='How it was built', arrows=True))
            nrow = pg.evaluate(f"document.querySelectorAll('#{cid}-built tr[data-mod]').length")
            nrep = pg.evaluate(f"document.querySelectorAll('nav[data-navctx=\"{cid}\"] .dunit a.ditem[data-target]').length")
            if nrow != nrep or not nrow: fails.append(f'{cid}-built: {nrow} report rows for {nrep} written reports')
        pg.evaluate(f"location.hash = '{first}'" if rome_reps else "location.hash = 'rome'"); pg.wait_for_timeout(50)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        step('home again', dict(id='home', nav='root', arrows=False, cont=(lambda c: c.startswith('Continue reading Rome · ')) if rome_reps else (lambda c: True)))
        pg.click('#home a.course[href="#greece"]'); pg.wait_for_timeout(80)
        step('greece home', dict(id='greece', nav='greece', u='COURSE 1', t='Greece', prev=False, cont='(hidden)'))
        pg.evaluate("document.querySelectorAll('#greece details.ucard').forEach(d => d.open = true)")
        pg.click('#greece a.hrow[data-target="m23"]'); pg.wait_for_timeout(80)
        step('greek report', dict(id='m23', nav='greece', u='GREECE · UNIT 2 · 2.3', arrows=True, prev=True, next=True))
        pg.click('#nextB'); pg.wait_for_timeout(50)
        step('greek next', dict(id='m24', nav='greece'))
        greek_last = pg.eval_on_selector_all('nav[data-navctx="greece"] .dunit a.ditem[data-target]', 'as => as.map(a => a.dataset.target)')[-1]
        pg.evaluate(f"location.hash = '{greek_last}'"); pg.wait_for_timeout(50)
        step('greek last', dict(id=greek_last, nav='greece', next=False))
        pg.evaluate("location.hash = 'm24'"); pg.wait_for_timeout(50)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        step('home last', dict(id='home', cont=lambda c: c.startswith('Continue reading Greece · 2.4')))
        if rome_reps:
            pg.click('#home a.course[href="#rome"]'); pg.wait_for_timeout(80)
            step('rome home resumes rome', dict(id='rome', cont=lambda c: c.startswith('Continue ') and 'Greece' not in c and c != '(hidden)'))
        pg.click('#menuB'); pg.wait_for_timeout(250)
        dr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dtop .ditem .t')].map(t => t.textContent)")
        if rome_reps and dr[:3] != ['Academy', 'Rome: course home', 'Syllabus and prompts']: fails.append(f'rome drawer top: {dr}')
        pg.click('#closeB'); pg.wait_for_timeout(200)
        # the Brand + AI courses (A under Marketing, B under Technology, A3): each its own drawer context with a Units group
        # and a "How it is built" group; written units open reading pages inside the site (never a link out); the reading
        # page is a report (prev/next, continue); the briefs, build order, audits, bibliography and changelog are pages too
        for bid, short, key in (('brand-a', 'Personal brand', 'A'), ('brand-b', 'Building with AI', 'B')):
            pg.click('#homeB'); pg.wait_for_timeout(80)
            pg.click(f'#home a.course[href="#{bid}"]'); pg.wait_for_timeout(80)
            step(f'{bid} home', dict(id=bid, nav=bid, u=f'COURSE {key}', t=short, arrows=True, prev=False))
            pg.click('#menuB'); pg.wait_for_timeout(250)
            gr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dunit')].map(u => u.querySelector('.ut').textContent + (u.classList.contains('closed') ? ':closed' : ':open'))")
            if gr != ['Units:open', 'How it is built:closed']: fails.append(f'{bid} drawer groups on arrival: {gr}')
            pg.click('#closeB'); pg.wait_for_timeout(200)
            ba = pg.evaluate(f"[...document.querySelectorAll('#{bid} a.hrow')].map(a => a.getAttribute('href'))")
            if not ba or not all(h.startswith('#read-') for h in ba): fails.append(f'{bid} written units do not open reading pages: {ba[:3]}')
            # navigation never leaves the site: no artifact link in a hero, a button row or the drawer (a unit's own citations may cite one)
            ext = pg.evaluate(f"[...document.querySelectorAll('.panel[data-ctx=\"{bid}\"] .hero a, .panel[data-ctx=\"{bid}\"] .hlinks a, .panel[data-ctx=\"{bid}\"] .hrows a.hrow:not([target]), [data-navctx=\"{bid}\"] a')].filter(a => a.getAttribute('href').startsWith('http')).map(a => a.href)")
            if ext: fails.append(f'{bid} navigation links out of the site: {ext[:3]}')
            pg.click(f'#{bid} a.hrow[href="{ba[0]}"]'); pg.wait_for_timeout(80)
            step(f'{bid} reading', dict(id=ba[0][1:], nav=bid, u=lambda u: u.startswith(short.upper() + ' · '), arrows=True, prev=True))
            for pid, t in ((f'{bid}-build', 'How it is built'), (f'{bid}-order', 'Build order'), (f'briefs-{key.lower()}', 'Briefs'), (f'{bid}-audits', 'Audits'), (f'{bid}-bibliography', 'Bibliography'), (f'{bid}-changelog', 'Changelog')):
                pg.evaluate(f"location.hash = '{pid}'"); pg.wait_for_timeout(50)
                step(f'{bid} {t}', dict(id=pid, nav=bid, t=t))
            # A4: the course's "How it was built" page, generated: one row per written unit, read from the front matter
            pg.evaluate(f"location.hash = '{bid}-built'"); pg.wait_for_timeout(50)
            step(f'{bid} How it was built', dict(id=f'{bid}-built', nav=bid, t='How it was built'))
            nrow = pg.evaluate(f"document.querySelectorAll('#{bid}-built tr[data-unit]').length")
            if nrow != len(ba) or not pg.evaluate(f"document.getElementById('{bid}-built').hasAttribute('data-loaded')"):
                fails.append(f'{bid}-built: {nrow} unit rows for {len(ba)} written units, or not fetched through the shell')
            pg.click('#homeB'); pg.wait_for_timeout(80)
            step(f'home after {bid}', dict(id='home', cont=lambda c: c.startswith('Continue reading ' + short + ' · ')))
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
        if dr != ['Home', 'Changelog', 'Backlog']: fails.append(f'root drawer top: {dr}')
        gr = pg.evaluate("[...document.querySelectorAll('[data-navctx=\"root\"] .dunit')].map(u => u.querySelector('.ut').textContent + (u.classList.contains('closed') ? ':closed' : ':open'))")
        # a track's group is open once a page in it was visited in this run (shell.js show()); the ones the run above
        # visited (greece, rome, brand-a, brand-b) are open, any other track from courses.py starts closed
        seen = {'history', 'marketing', 'technology'}
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
        # the backlog page renders the queue and the chats done
        pg.evaluate("location.hash = 'backlog'"); pg.wait_for_timeout(50)
        step('backlog', dict(id='backlog', nav='root', u='ACADEMY', t='Backlog', arrows=False))
        nt = pg.evaluate("document.querySelectorAll('#backlog table').length")
        if nt < 3: fails.append(f'backlog page: {nt} tables, expected the lanes, the proposed rows and the chats done')
        # the home lists every live course under its track, in courses.py order (history courses, then markdown courses)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        tr = pg.evaluate("[...document.querySelectorAll('#home .track')].map(t => t.querySelector('h2').textContent + ':' + [...t.querySelectorAll('.cgrid a.course')].map(a => a.getAttribute('href')).join(','))")
        if tr != HOME_TRACKS: fails.append(f'home tracks: {tr}, courses.py gives {HOME_TRACKS}')
        h1 = pg.evaluate("[...document.querySelectorAll('.panel[data-kind=\"course\"] h1, #home h1')].map(h => h.textContent)")
        if any(' in the order' in t or t.startswith('The courses') for t in h1): fails.append(f'course titles not self-evident: {h1}')
        title = pg.title()
        if title != 'Academy': fails.append(f'page title {title!r}, expected Academy')
        for label, s in log: print(f'  {label:28} {s["id"]:14} nav={s["nav"]:7} {s["u"]} | {s["t"][:40]} | arrows={s["arrows"]} prev={s["prev"]} next={s["next"]} | {s["cont"][:60]}')
        rp = rome_reps[3] if len(rome_reps) > 3 else (rome_reps[0] if rome_reps else 'rome-syllabus')
        ctx.close()

        # ---- tablet: wider column, two-column cards, the drawer still a drawer -----------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'tablet', 768, 1024, True)
        if lay[0] != 768: fails.append(f'tablet layout {lay}: expected width 768')
        check_panels(pg, 'tablet', fails)
        pg.evaluate("location.hash = 'rome'"); ready(pg); pg.wait_for_timeout(50)
        t = pg.evaluate('''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
          return {off: r.right <= 0, menu: getComputedStyle(document.getElementById('menuB')).display !== 'none',
                  main: document.querySelector('main').getBoundingClientRect().width,
                  cols: getComputedStyle(document.querySelector('#rome .ucards')).gridTemplateColumns.split(' ').length,
                  home: getComputedStyle(document.querySelector('#home .track .cgrid')).gridTemplateColumns.split(' ').length}; }''')
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
        small = pg.evaluate(TARGET_JS, '#rome')
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
                  home: getComputedStyle(document.querySelector('#home .track .cgrid')).gridTemplateColumns.split(' ').length,
                  ml: getComputedStyle(document.querySelector('#home .ml-grid')).gridTemplateColumns.split(' ').length}; }''')
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

        if SHOTS:
            SHOTS.mkdir(parents=True, exist_ok=True)
            for name, w, h, mobile in VIEWPORTS:
                ctx, pg, _ = new_page(p, br, [], name, w, h, mobile)
                for theme in ('dark', 'light'):
                    pg.evaluate(f"localStorage.setItem('hellas-theme', '{theme}')")
                    for pid in ['home', 'rome', rp] + [x for x in PAGES if x not in ('home', 'rome', rp)]:
                        pg.evaluate(f"localStorage.removeItem('pm-sec-{pid}')")   # P68: each shot opens on section 1
                        pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(250); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(50)
                        shoot(pg, SHOTS / f'{name}-{pid}-{theme}.png', w, h)
                        if pid in PAGES and pg.query_selector(f'[id="{pid}"] .report.steps'):   # P68: the reading states the top does not show
                            for state, js in READING_SHOTS:
                                pg.evaluate(js, pid); pg.wait_for_timeout(200)
                                pg.screenshot(path=str(SHOTS / f'{name}-{pid}-{state}-{theme}.png'))
                            pg.evaluate("(pid) => { const p = document.getElementById(pid); p.querySelectorAll('details').forEach(d => d.open = false); const w = p.querySelector('.stepbar .whole'); if (w.getAttribute('aria-pressed') === 'true') w.click(); [...p.querySelectorAll('.seclist a')][0].click(); window.scrollTo(0, 0); }", pid)
                        if pid in PAGES:   # P41: each figure of a --page panel, as the reader sees it in its frame
                            for k, fig in enumerate(pg.query_selector_all(f'[id="{pid}"] figure.viz')):
                                kind = ([c for c in fig.get_attribute('class').split() if c.startswith('viz-') and c != 'viz-wide'] or ['viz-figure'])[0][4:]
                                fig.evaluate("f => { const s = f.closest('.sec'), p = f.closest('.panel'); if (s && !s.classList.contains('on')) p.querySelector('.seclist a[data-step=\"' + s.dataset.step + '\"]').click(); }")   # P68: its section shown first
                                fig.scroll_into_view_if_needed(); pg.wait_for_timeout(30)
                                fig.screenshot(path=str(SHOTS / f'{name}-{pid}-fig-{k + 1:02d}-{kind}-{theme}.png'), timeout=120000)
                            pg.evaluate('window.scrollTo(0, 0)')
                ctx.close()
            # V1: each figure of the examples page as the reader sees it in its frame, then one sheet per width and theme
            for name, w, h, mobile in VIEWPORTS:
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
                        sheet = Image.new('RGB', (max(i.width for i in ims), sum(i.height for i in ims) + 12 * len(ims)), (10, 10, 12) if theme == 'dark' else (245, 245, 247))
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
    print('\n'.join('FAIL ' + f for f in fails) if fails else 'ALL CHECKS PASSED')
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main())
