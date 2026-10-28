"""Check a built page at 400 px, dark and light: horizontal overflow per panel, interactive targets under 44 px.

    python3 check_page.py hubs/brand-and-ai-courses.html            # panels are .panel (default)
    python3 check_page.py some-old-page.html .view                  # another panel selector

Opens every panel and every <details>; prints a JSON report of failures ("{}" plus empty error lists means clean).
Inline links inside running text are exempt (WCAG 2.5.8). Needs Playwright with Chromium.
"""
import sys, json, asyncio
from playwright.async_api import async_playwright

import os
page_path = os.path.abspath(sys.argv[1])
sel = sys.argv[2] if len(sys.argv) > 2 else '.panel'
maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

JS_IDS = "(sel)=>[...document.querySelectorAll(sel)].map(p=>p.id.replace(/^v-/,''))"
JS_CHECK = r"""
() => {
  const W = document.documentElement.clientWidth;
  const res = {scrollW: document.documentElement.scrollWidth, W, over: [], small: []};
  const all = [...document.querySelectorAll('body *')];
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
    if (inter && !el.closest('.drawer:not(.on), .side[hidden]')) {
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

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        out = {}
        for theme in ('dark', 'light'):
            ctx = await b.new_context(viewport={'width': 400, 'height': 860}, device_scale_factor=1, color_scheme=theme, is_mobile=True, has_touch=True)
            pg = await ctx.new_page()
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto('file://' + page_path)
            ids = (await pg.evaluate(JS_IDS, sel))[:maxn]
            for i in ids:
                await pg.evaluate("h=>{location.hash=h}", '#' + i)
                await pg.wait_for_timeout(60)
                # open every details so hidden content is measured too
                await pg.evaluate("()=>document.querySelectorAll('details').forEach(d=>d.open=true)")
                r = await pg.evaluate(JS_CHECK)
                key = f'{theme}:{i}'
                if r['scrollW'] > r['W'] or r['over'] or r['small']:
                    out[key] = r
            out[f'{theme}:errors'] = errs
            await ctx.close()
        await b.close()
        print(json.dumps(out, indent=1))

asyncio.run(main())
