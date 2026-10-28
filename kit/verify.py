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
a Brand + AI course and its reading and build pages, the drawer groups (tracks open by default, a course's units as an
accordion) and the Backlog page; the same panel checks again in the light theme. Tablet: the drawer is still a drawer (off screen until the menu button, 360 px, backdrop).
Desktop: the drawer is a persistent 300 px sidebar (no backdrop, no menu button, current item highlighted, scrolls on
its own) and the top bar spans the content column. With --shots, saves dark and light screenshots at the three widths
of home, Rome and one Rome report, plus every panel id given with --page (a new unit's reading page, a new course home).
"""
import sys, json, pathlib, re, threading, functools
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

R = pathlib.Path(__file__).resolve().parent
SITE = R / 'academy'
SHELL_MAX = 1024 * 1024   # A2: the shell stays under 1 MB
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
SERVER = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=SERVER.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{SERVER.server_port}/index.html'
# the visible panel holds its content: a panel in the shell at once, a report once its fetch has landed (or failed)
READY_JS = """() => { const p = [...document.querySelectorAll('.panel')].find(p => !p.hidden);
  return !!p && (!p.hasAttribute('data-src') || p.hasAttribute('data-loaded') || p.hasAttribute('data-failed')); }"""
def ready(pg):
    pg.wait_for_function(READY_JS, timeout=15000)
SHOTS = pathlib.Path(sys.argv[sys.argv.index('--shots') + 1]) if '--shots' in sys.argv else None
PAGES = [a for i, a in enumerate(sys.argv) if i > 0 and sys.argv[i - 1] == '--page']   # extra panels to screenshot
GAP = 6
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

def check_panels(pg, label, fails):
    """Every panel, every <details> open: horizontal scroll, 6 px gaps, 44 px targets. Returns (tightest gap, panel count)."""
    ids = pg.eval_on_selector_all('.panel', 'ps => ps.map(p => p.id)')
    worst = []
    for pid in ids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(30)
        if pg.evaluate(f"document.getElementById('{pid}').hasAttribute('data-failed')"): fails.append(f'{label} {pid}: the report did not load')
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) details').forEach(d => d.open = true)")
        sw = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.clientWidth]')
        if sw[0] > sw[1]: fails.append(f'{label} {pid}: horizontal scroll {sw}')
        res = pg.evaluate(BOX_JS, [f'#{pid}', GAP])
        if res['nbad']: fails.append(f'{label} {pid}: {res["nbad"]} boxes closer than {GAP}px: ' + '; '.join(res['bad']))
        small = pg.evaluate(TARGET_JS, f'#{pid}')
        if small: fails.append(f'{label} {pid}: {len(small)} targets under 44px: ' + '; '.join(small[:6]))
        worst.append((res['min'], pid, res['n']))
    m = min(worst)
    print(f'{label}: panels checked: {len(ids)}; tightest stacked gap {m[0]}px ({m[1]})')
    return m[0], len(ids)

def new_page(p, br, errors, name, w, h, mobile):
    ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=3 if mobile else 1,
                         is_mobile=mobile, has_touch=mobile)  # a real phone or tablet honours the viewport tag
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=''))
    ctx.route('**/fonts.gstatic.com/**', lambda r: r.abort())
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
    # every report and syllabus panel, a markdown course's briefs and bibliography pages, and a history course home (a
    # course panel whose label is a numbered course; Brand + AI homes are lettered and stay) leave the shell (A2, P20, P22)
    must = [h for h in heads if ' data-kind="report"' in h or ' data-kind="syllabus"' in h or re.search(r' id="(briefs-[a-z]+|[a-z-]+-bibliography)"', h)
            or (' data-kind="course"' in h and re.search(r' data-u="COURSE \d', h))]
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
        by.setdefault(x.split('/')[0], []).append((len((SITE / x).read_bytes()), x))
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
    big = max((n, x) for fs in by.values() for n, x in fs)
    print(f'split: shell {size / 1024:,.0f} KB (limit 1,024 KB), {len(on_disk)} fetched files in {len(by)} folders, largest {big[1]} {big[0] / 1024:,.0f} KB')
    for ctx, fs in by.items():
        print(f'  {ctx + "/":10} {len(fs):3} files {sum(n for n, _ in fs) / 1024:7,.0f} KB, largest {max(fs)[1]} {max(fs)[0] / 1024:,.0f} KB')

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
    pg.click('#m23 .pager a.next'); ready(pg)
    if pg.evaluate("location.hash") != '#m24' or hits.get('/greece/r-2.4.html') != 1: fails.append(f'split: pager to #m24: hash {pg.evaluate("location.hash")}, fetched {hits.get("/greece/r-2.4.html")} times')
    # a section link into a report not yet opened, on a fresh load
    pg.goto(URL + '#rm12-2'); pg.reload(); ready(pg); pg.wait_for_timeout(300)
    sec = pg.evaluate("(() => { const el = document.getElementById('rm12-2'); const p = [...document.querySelectorAll('.panel')].find(p => !p.hidden); return [p.id, !!el, el ? Math.round(el.getBoundingClientRect().top) : null]; })()")
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
        pg.goto(URL + '#' + h); pg.reload(); ready(pg); pg.wait_for_timeout(300)
        sec = pg.evaluate(f"(() => {{ const el = document.getElementById('{h}'); const p = [...document.querySelectorAll('.panel')].find(p => !p.hidden); return [p.id, !!el, el ? Math.round(el.getBoundingClientRect().top) : null]; }})()")
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
    print('split: stubs empty until opened; fetched once, kept and the next report prefetched; links into an unopened report, syllabus, briefs page and course home; failed fetch and retry (report and course home); a course home\'s continue button')
    ctx.close()

def main():
    errors, fails = [], []
    check_files(fails)
    with sync_playwright() as p:
        br = p.chromium.launch()
        check_split(br, fails)

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
        if gr != ['History:open', 'Marketing:open', 'Technology:open']: fails.append(f'root drawer groups: {gr}')
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
        # the home lists every live course under its track, in order: History (Greece, Rome), Marketing (A), Technology (B)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        tr = pg.evaluate("[...document.querySelectorAll('#home .track')].map(t => t.querySelector('h2').textContent + ':' + [...t.querySelectorAll('.cgrid a.course')].map(a => a.getAttribute('href')).join(','))")
        if tr != ['History:#greece,#rome', 'Marketing:#brand-a', 'Technology:#brand-b']: fails.append(f'home tracks: {tr}')
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
        mw = float(s['measure'].replace('px', '')) if s['measure'].endswith('px') else 0  # 68ch resolves to about 690 px
        if not 560 <= mw <= 720: fails.append(f'desktop: report measure {s["measure"]}, expected 68ch (560 to 720 px)')
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
                        pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(250); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(50)
                        pg.screenshot(path=str(SHOTS / f'{name}-{pid}-{theme}.png'), full_page=True, clip={'x': 0, 'y': 0, 'width': w, 'height': 2600})
                ctx.close()
            print('screenshots in', SHOTS)
        br.close()
    errs = [e for e in errors if 'fonts.g' not in e]
    if errs: fails.append('console errors: ' + ' | '.join(errs[:5]))
    print('\n'.join('FAIL ' + f for f in fails) if fails else 'ALL CHECKS PASSED')
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main())
