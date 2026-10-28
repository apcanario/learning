"""Browser checks for personal-mythology.html, the Academy site (run after build.py).

python3 verify.py [--shots DIR]
Three widths (design/theme.css section 6): phone 390x844, tablet 768x1024, desktop 1280x800. On every panel of every
width, with every <details> opened: no horizontal scroll, no boxed elements closer than 6 px, no interactive target
under 44 px tall (inline links in running text exempt), no console error. Phone: the drawer in each context and the
navigation context (drawer, title, arrows, continue) across home -> Rome -> report -> home -> Greece -> report ->
Brand + AI placeholder. Tablet: the drawer is still a drawer (off screen until the menu button, 360 px, backdrop).
Desktop: the drawer is a persistent 300 px sidebar (no backdrop, no menu button, current item highlighted, scrolls on
its own) and the top bar spans the content column. With --shots, saves dark and light screenshots at the three widths.
"""
import sys, json, pathlib
from playwright.sync_api import sync_playwright

R = pathlib.Path(__file__).resolve().parent
URL = (R / 'personal-mythology.html').as_uri()
SHOTS = pathlib.Path(sys.argv[sys.argv.index('--shots') + 1]) if '--shots' in sys.argv else None
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
        pg.evaluate(f"location.hash = '{pid}'"); pg.wait_for_timeout(30)
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

def main():
    errors, fails = [], []
    with sync_playwright() as p:
        br = p.chromium.launch()

        # ---- phone ------------------------------------------------------------------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'phone', 390, 844, True)
        if lay != [390, 1]: fails.append(f'phone layout {lay}: expected [390, 1] (missing viewport tag?)')
        else: print('phone layout: 390 px at scale 1')
        check_panels(pg, 'phone', fails)
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
        # the Brand + AI courses (A under Marketing, B under Technology): each its own drawer context, no arrows, written units link out
        for bid, short, key in (('brand-a', 'Personal brand', 'A'), ('brand-b', 'Building with AI', 'B')):
            pg.click('#homeB'); pg.wait_for_timeout(80)
            pg.click(f'#home a.course[href="#{bid}"]'); pg.wait_for_timeout(80)
            step(f'{bid} home', dict(id=bid, nav=bid, u=f'COURSE {key}', t=short, arrows=False))
            ba = pg.evaluate(f"[...document.querySelectorAll('#{bid} a.hrow')].map(a => a.getAttribute('href'))")
            if not ba or not all(h.startswith('https://claude.ai/artifact/') for h in ba): fails.append(f'{bid} written units do not link to the hub: {ba[:3]}')
            pg.click('#menuB'); pg.wait_for_timeout(250)
            dr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dtop .ditem .t')].map(t => t.textContent)")
            if dr[:2] != ['Academy', f'{short}: course home']: fails.append(f'{bid} drawer top: {dr}')
            pg.click('#closeB'); pg.wait_for_timeout(200)
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
        pg.evaluate("location.hash = 'rome'"); pg.wait_for_timeout(50)
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
        print('tablet: drawer is a drawer (off screen, 360 px with backdrop when open); column', t['main'], 'px')
        ctx.close()

        # ---- desktop: persistent sidebar ----------------------------------------------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'desktop', 1280, 800, False)
        if lay[0] != 1280: fails.append(f'desktop layout {lay}: expected width 1280')
        check_panels(pg, 'desktop', fails)
        pg.evaluate("location.hash = 'm23'"); pg.wait_for_timeout(80)
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
                    for pid in ('home', 'rome', rp):
                        pg.goto(URL + '#' + pid); pg.reload(); pg.wait_for_timeout(250); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(50)
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
