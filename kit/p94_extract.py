"""P94 (8 Nov 2026): the fresh checker's extract of the section separators. For each page given (the three shot
pages and twenty more chosen by script across the five courses, seeded, so the choice repeats), from the built site
in a browser at 390 px with motion allowed, every section: its top-level paragraphs (their text and words, read from
the page), its separator's HTML, its rises (label, words, the contour levels it stands, its own closed rings), and its
frame and the box of all its lines at the five poses of the turn at the top of the breath, in CSS pixels, with the
clearance each side. Writes <out>/extract/<page>.md (to read) and <out>/extract/<page>.json, and
<out>/extract/choice.txt (how the pages were chosen).

  python3 p94_extract.py OUT"""
import sys, json, random, pathlib, re
from playwright.sync_api import sync_playwright
import p94_shots as S

R = pathlib.Path(__file__).resolve().parent
TURN_CSS = (R / 'shell.css').read_text()
_TM = re.search(r'--topo-turn:([\d.]+)deg;--topo-cycle:([\d.]+)s;[^\n]*\n\s*--topo-grow:([\d.]+);--topo-breath:([\d.]+)s', TURN_CSS)
TURN, CYC, GROW, BT = float(_TM.group(1)), float(_TM.group(2)) * 1000, float(_TM.group(3)), float(_TM.group(4)) * 1000
POSES = (0, .25, .5, .75, 1)

JS = r"""([pid, poses, cyc, bt]) => {
  const P = document.getElementById(pid), r = P.querySelector('.report.steps'), whole = P.querySelector('.stepbar .whole');
  const words = e => { let t = ''; const walk = n => { for (const c of n.childNodes) { if (c.nodeType === 3) t += c.data; else if (c.nodeType === 1) { t += ' '; walk(c); t += ' '; } } }; walk(e); return t.split(/\s+/).filter(Boolean); };
  whole.click();
  const probe = document.createElement('i'); P.appendChild(probe); probe.style.color = 'var(--cc)'; const tone = getComputedStyle(probe).color; probe.remove();
  const secs = [...r.children].filter(x => x.classList.contains('sec')).map((sec, k) => {
    const h = sec.querySelector(':scope > h2'), t = sec.querySelector(':scope > .topo-sep');
    const kids = [...sec.children].map(e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).join('.') : ''));
    const paras = [...sec.children].filter(e => e.tagName === 'P' && !e.classList.contains('viz-cue')).map(e => { const w = words(e); return {words: w.length, text: e.textContent.trim()}; }).filter(p => p.words);
    const o = {k: k + 1, heading: h ? h.textContent.replace(/\s+/g, ' ').trim() : '', children: kids, paras, sep: null};
    if (t) {
      const l = t.querySelector('svg');
      o.sep = {html: t.outerHTML, bytes: new Blob([t.outerHTML]).size, cls: t.className, aria: t.getAttribute('aria-hidden'), ph: getComputedStyle(t).getPropertyValue('--ph').trim(),
        next: t.nextElementSibling ? t.nextElementSibling.tagName.toLowerCase() + '.' + t.nextElementSibling.className : null,
        viewBox: l.getAttribute('viewBox'), fit: l.getAttribute('preserveAspectRatio'), tone, stroke: getComputedStyle(t.querySelector('path, circle')).stroke, opacity: getComputedStyle(l).opacity,
        rises: [...l.querySelectorAll('g.ct-rise')].map(g => ({label: g.getAttribute('data-label'), words: +g.getAttribute('data-words'), levels: +g.getAttribute('data-rings'),
          rings: g.querySelector('path').getAttribute('d').split('z').length - 1, spot: !!g.querySelector('.ct-spot')})), poses: []};
    }
    return [o, t];
  });
  const an = document.getAnimations().filter(a => a.effect && a.effect.target && a.effect.target.closest && a.effect.target.closest('#' + pid + ' .topo-sep'));
  for (const p of poses) {
    an.forEach(a => { a.pause();
      if (a.animationName === 'topo-turn') { const d = a.effect.getTiming().delay; let t = p * cyc + d; if (t < 0) t = 2 * cyc - p * cyc + d; a.currentTime = t; }
      else { let t = a.effect.getTiming().delay + .9999 * bt; if (t < 0) t += 2 * bt; a.currentTime = t; } });
    secs.forEach(([o, t]) => { if (!t) return; const fr = t.getBoundingClientRect(); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      t.querySelectorAll('path, circle').forEach(e => { const q = e.getBoundingClientRect(); if (!q.width && !q.height) return; x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); });
      const f = v => Math.round(v * 10) / 10;
      o.sep.poses.push({pose: p, frame: [f(fr.left), f(fr.top), f(fr.width), f(fr.height)], lines: [f(x0), f(y0), f(x1 - x0), f(y1 - y0)],
                        clear: {left: f(x0 - fr.left), top: f(y0 - fr.top), right: f(fr.right - x1), bottom: f(fr.bottom - y1)},
                        transform: getComputedStyle(t.querySelector('svg')).transform}); });
  }
  an.forEach(a => a.play()); whole.click();
  return {pid, title: P.querySelector('h1').textContent.trim(), width: innerWidth, anims: an.map(a => a.animationName), sections: secs.map(([o]) => o)};
}"""


def choose(ids):
    """The three shot pages, then twenty more: four from each course (seeded with 94), the page holding the section with
    the most paragraphs and the page whose separators weigh most replacing two of them where they are not already in."""
    by = {}
    for i in ids:
        c = 'greece' if re.fullmatch(r'm\d+', i) else 'rome' if i.startswith('rm') else 'ux-ia' if i.startswith('read-ia') or i.startswith('read-dd-ia') \
            else 'brand-a' if i.startswith('read-a') or i.startswith('read-dd-a') else 'brand-b'
        by.setdefault(c, []).append(i)
    rnd = random.Random(94)
    pick = []
    for c in sorted(by):
        pool = [x for x in by[c] if x not in S.PAGES]
        pick += rnd.sample(pool, min(4, len(pool)))
    return pick, by


def main(out):
    out = pathlib.Path(out) / 'extract'
    out.mkdir(parents=True, exist_ok=True)
    url = S.serve(R / 'academy')
    with sync_playwright() as p:
        br = p.chromium.launch()
        ctx = br.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True, color_scheme='dark', reduced_motion='no-preference')
        ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=S.FONT_CSS))
        ctx.route('**/fonts.gstatic.com/**', S.font_file)
        pg = ctx.new_page(); pg.goto(url + '#home'); pg.wait_for_timeout(300)
        ids = pg.eval_on_selector_all('.panel[data-kind="report"]', 'ps => ps.map(p => p.id)')
        extra, by = choose(ids)
        # the extremes, read from the build: the section with most paragraphs and the heaviest page
        sizes = {}
        for f in (R / 'academy').glob('*/*.html'):
            h = f.read_text()
            seps = re.findall(r'<div class="topo topo-patch topo-sep".*?</div>', h, re.S)
            if seps:
                stem = f.stem   # a fetched file is a panel's inside: r-6.1 in greece/ is m61, in rome/ rm11; read-x is read-x
                pid = ({'greece': 'm', 'rome': 'rm'}[f.parent.name] + stem[2:].replace('.', '')) if stem.startswith('r-') else stem
                sizes[pid] = (sum(len(x.encode()) for x in seps), max(x.count('class="ct-rise') for x in seps))
        most = max(sizes, key=lambda k: sizes[k][1]); heavy = max(sizes, key=lambda k: sizes[k][0])
        for k, x in enumerate((most, heavy)):
            if x not in extra and x not in S.PAGES:
                course = [c for c, v in by.items() if x in v][0]
                drop = [y for y in extra if y in by[course]][-1 - k]
                extra[extra.index(drop)] = x
        pages = S.PAGES + extra
        (out / 'choice.txt').write_text(
            'The three shot pages: ' + ', '.join(S.PAGES) + '.\n'
            'Twenty more, four from each course, drawn with random.Random(94) from its reading pages other than the shot pages; then '
            f'the page holding the section with most paragraphs ({most}, {sizes[most][1]} rises) and the page whose separators weigh '
            f'most ({heavy}, {sizes[heavy][0]:,} bytes) put in place of a drawn page of their course where they were not drawn: '
            + ', '.join(extra) + '.\nPages per course: ' + ', '.join(f'{c} {len(v)}' for c, v in sorted(by.items())) + '.\n')
        for pid in pages:
            pg.evaluate(f"location.hash = '{pid}'")
            pg.wait_for_function(f"() => document.fonts.status === 'loaded' && !document.getElementById('{pid}').hidden && document.querySelector('#{pid} .report.steps.stepping')")
            pg.wait_for_timeout(150)
            d = pg.evaluate(JS, [pid, list(POSES), CYC, BT])
            (out / f'{pid}.json').write_text(json.dumps(d, indent=1, ensure_ascii=False))
            md = [f'# {pid} · {d["title"]}', '', f'Read at {d["width"]} px with motion allowed. Animations on the separators: {len(d["anims"])} '
                  f'({", ".join(sorted(set(d["anims"])))}). Poses: the turn at {", ".join(str(x) for x in POSES)} of its sweep, each at the top of the breath.', '']
            for s in d['sections']:
                md += [f'## Section {s["k"]} · {s["heading"]}', '', 'Children, in order: ' + ' '.join(s['children']), '',
                       f'Top-level paragraphs: {len(s["paras"])}' + (f' (words: {", ".join(str(p["words"]) for p in s["paras"])})' if s['paras'] else ''), '']
                for j, p in enumerate(s['paras']):
                    md.append(f'{j + 1}. ({p["words"]} words) {p["text"]}')
                md.append('')
                if not s['sep']:
                    md += ['No separator.', '']
                    continue
                sp = s['sep']
                md += [f'Separator: class "{sp["cls"]}", aria-hidden {sp["aria"]}, {sp["bytes"]:,} bytes, phase {sp["ph"]}, followed by {sp["next"]}; '
                       f'viewBox {sp["viewBox"]} ({sp["fit"]}); the page\'s tone {sp["tone"]}, its lines {sp["stroke"]} at opacity {sp["opacity"]}.', '',
                       'Rises: ' + '; '.join(f'{r["label"]} {r["words"]} words, {r["levels"]} levels, {r["rings"]} rings in its path' + (', a spot ring' if r['spot'] else '') for r in sp['rises']), '',
                       '| Pose | Frame (x, y, w, h) | Lines (x, y, w, h) | Clear left, top, right, bottom |', '|---|---|---|---|']
                for q in sp['poses']:
                    c = q['clear']
                    md.append(f'| {q["pose"]} | {", ".join(str(v) for v in q["frame"])} | {", ".join(str(v) for v in q["lines"])} | {c["left"]}, {c["top"]}, {c["right"]}, {c["bottom"]} |')
                md += ['', 'Its HTML:', '', '```html', sp['html'], '```', '']
            (out / f'{pid}.md').write_text('\n'.join(md))
            print('extract', pid, sum(1 for s in d['sections'] if s['sep']), 'separators')
        br.close()


if __name__ == '__main__':
    main(sys.argv[1])
