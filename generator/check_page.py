"""Check a built hub page at three widths, dark and light: horizontal overflow per panel, boxed elements closer
than 6 px, interactive targets under 44 px, console errors; the drawer still a drawer on the tablet, a persistent
sidebar on the desktop (design/theme.css section 6).

    python3 check_page.py hubs/brand-and-ai-courses.html            # panels are .panel (default)
    python3 check_page.py some-old-page.html .view                  # another panel selector
    python3 check_page.py hubs/brand-and-ai-courses.html .panel 9999 --shots DIR   # also save screenshots

Widths: phone 400x860, tablet 768x1024, desktop 1280x800. Opens every panel and every <details>; prints a JSON
report of failures per width and theme ("{}" plus empty error lists means clean) and a last line, ALL CHECKS PASSED
or FAIL. Inline links inside running text are exempt (WCAG 2.5.8). Needs Playwright with Chromium.
"""
import sys, json, asyncio, os, pathlib
from playwright.async_api import async_playwright

args = [a for a in sys.argv[1:] if a != '--shots' and (sys.argv.index(a) == 0 or sys.argv[sys.argv.index(a) - 1] != '--shots')]
page_path = os.path.abspath(args[0])
sel = args[1] if len(args) > 1 else '.panel'
maxn = int(args[2]) if len(args) > 2 else 9999
SHOTS = pathlib.Path(sys.argv[sys.argv.index('--shots') + 1]) if '--shots' in sys.argv else None
GAP = 6
SIDE = 300
VIEWPORTS = [('phone', 400, 860, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]

JS_IDS = "(sel)=>[...document.querySelectorAll(sel)].map(p=>p.id.replace(/^v-/,''))"
JS_CHECK = r"""
() => {
  const W = document.documentElement.clientWidth;
  const res = {scrollW: document.documentElement.scrollWidth, W, over: [], small: []};
  const all = [...document.querySelectorAll('body *')];
  const dr = document.getElementById('drawer'), dOn = dr && dr.getBoundingClientRect().left >= 0;
  for (const el of all) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    // ignore anything inside a scroll container that scrolls horizontally
    let p = el.parentElement, inScroll = false;
    while (p) { const ps = getComputedStyle(p); if (/(auto|scroll|hidden)/.test(ps.overflowX) && p.scrollWidth > p.clientWidth + 1) { inScroll = true; break; } p = p.parentElement; }
    if (!inScroll && r.right > W + 1 && cs.position !== 'fixed') res.over.push((el.tagName + '.' + el.className).slice(0, 60) + ' r=' + Math.round(r.right));
    const inter = el.matches('a[href],button,summary,input,select,[role=button]');
    if (inter && (dOn || !el.closest('.drawer')) && !el.closest('.side[hidden]')) {
      // inline links inside running text are exempt (WCAG 2.5.8 inline exception)
      const inline = el.tagName === 'A' && cs.display === 'inline';
      if (!inline && (r.height < 43.5 || r.width < 24)) res.small.push((el.tagName + '.' + el.className + ' "' + (el.textContent || '').trim().slice(0, 24) + '"').slice(0, 80) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
    }
  }
  res.over = [...new Set(res.over)].slice(0, 12);
  res.small = [...new Set(res.small)].slice(0, 15);
  return res;
}
"""
# boxed elements (bordered, or filled with rounded corners) stacked closer than GAP px, inside the visible panel
JS_GAP = r'''([scope, gap]) => {
  const root = document.querySelector(scope); if (!root) return {min: 0, bad: []};
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
      const d = e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).join('.') : '');
      bad.push(`${d(a)} | ${d(b)} gap ${g.toFixed(1)}`);
    }
  }
  return {min: Math.round(min * 10) / 10, bad: bad.slice(0, 12)};
}'''
JS_DRAWER = r'''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
  return {left: r.left, w: r.width, h: r.height, vh: innerHeight, on: d.classList.contains('on'), hidden: d.getAttribute('aria-hidden'),
          menu: getComputedStyle(document.getElementById('menuB')).display, backdrop: getComputedStyle(document.getElementById('backdrop')).display,
          mainLeft: document.querySelector('main').getBoundingClientRect().left, mainW: document.querySelector('main').getBoundingClientRect().width,
          topLeft: document.querySelector('.top').getBoundingClientRect().left,
          active: (d.querySelector('.ditem.is-active') || {}).getAttribute ? d.querySelector('.ditem.is-active').getAttribute('data-target') : null}; }'''

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        out, tight = {}, {}
        for name, w, h, mobile in VIEWPORTS:
            for theme in ('dark', 'light'):
                ctx = await b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1, color_scheme=theme, is_mobile=mobile, has_touch=mobile)
                await ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=''))
                await ctx.route('**/fonts.gstatic.com/**', lambda r: r.abort())
                pg = await ctx.new_page()
                errs = []
                pg.on('pageerror', lambda e: errs.append(str(e)))
                pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'fonts.g' not in m.text else None)
                await pg.goto('file://' + page_path)
                ids = (await pg.evaluate(JS_IDS, sel))[:maxn]
                mins = []
                for i in ids:
                    await pg.evaluate("h=>{location.hash=h}", '#' + i)
                    await pg.wait_for_timeout(60)
                    # open every details so hidden content is measured too
                    await pg.evaluate("()=>document.querySelectorAll('details').forEach(d=>d.open=true)")
                    r = await pg.evaluate(JS_CHECK)
                    g = await pg.evaluate(JS_GAP, ['#' + i, GAP])
                    mins.append((g['min'], i))
                    key = f'{name}:{theme}:{i}'
                    if r['scrollW'] > r['W'] or r['over'] or r['small'] or g['bad']:
                        r['gaps'] = g['bad']; out[key] = r
                tight[f'{name}:{theme}'] = min(mins) if mins else None
                # the drawer: a drawer below 1100 px (off screen, menu button, backdrop when open), a sidebar from 1100 px
                await pg.evaluate("h=>{location.hash=h}", '#' + (ids[1] if len(ids) > 1 else ids[0])); await pg.wait_for_timeout(60)
                d = await pg.evaluate(JS_DRAWER)
                if name == 'desktop':
                    bad = []
                    if d['left'] != 0 or d['w'] != SIDE or d['h'] < d['vh'] - 1: bad.append(f'sidebar not at the left edge, {SIDE} px, full height')
                    if d['menu'] != 'none' or d['backdrop'] != 'none': bad.append('menu button or backdrop shown')
                    if d['hidden'] != 'false': bad.append(f'aria-hidden={d["hidden"]}')
                    if d['mainLeft'] < SIDE or d['topLeft'] != SIDE: bad.append(f'content or top bar under the sidebar (main {d["mainLeft"]}, top {d["topLeft"]})')
                    if not 740 <= d['mainW'] <= 768: bad.append(f'main column {d["mainW"]} px, expected about 760')
                    if not d['active']: bad.append('no current item highlighted')
                    if bad: out[f'{name}:{theme}:sidebar'] = bad
                else:
                    bad = []
                    if d['left'] >= 0 and d['w'] > 0 and d['left'] + d['w'] > 0: bad.append('drawer on screen before the menu button is pressed')
                    if d['menu'] == 'none': bad.append('menu button hidden')
                    if name == 'tablet' and not 740 <= d['mainW'] <= 768: bad.append(f'main column {d["mainW"]} px, expected about 760')
                    await pg.click('#menuB'); await pg.wait_for_timeout(300)
                    d2 = await pg.evaluate(JS_DRAWER)
                    if d2['left'] != 0 or not d2['on']: bad.append('drawer did not open')
                    g = await pg.evaluate(JS_GAP, ['#drawer', GAP])
                    if g['bad']: bad.append('drawer gaps: ' + '; '.join(g['bad']))
                    r = await pg.evaluate(JS_CHECK)
                    if r['small']: bad.append('drawer targets: ' + '; '.join(r['small'][:6]))
                    await pg.click('#closeB'); await pg.wait_for_timeout(300)
                    if bad: out[f'{name}:{theme}:drawer'] = bad
                if SHOTS:
                    SHOTS.mkdir(parents=True, exist_ok=True)
                    for i in ids[:2]:
                        await pg.evaluate("h=>{location.hash=h}", '#' + i); await pg.wait_for_timeout(100); await pg.evaluate('window.scrollTo(0,0)')
                        await pg.screenshot(path=str(SHOTS / f'{name}-{i}-{theme}.png'), full_page=True, clip={'x': 0, 'y': 0, 'width': w, 'height': 2600})
                out[f'{name}:{theme}:errors'] = errs
                await ctx.close()
        await b.close()
        print(json.dumps(out, indent=1))
        print('tightest stacked gap:', ', '.join(f'{k} {v[0]}px ({v[1]})' for k, v in tight.items() if v))
        bad = [k for k, v in out.items() if v]
        print('FAIL ' + ', '.join(bad) if bad else 'ALL CHECKS PASSED')
        return 1 if bad else 0

sys.exit(asyncio.run(main()))
