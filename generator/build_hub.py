"""Build a course hub from its data folder, styled by design/theme.css.

    python3 build_hub.py data/brand-ai          -> hubs/brand-and-ai-courses.html

A hub has two halves: Learn (courses overview, one page per course, reading pages for written
material) and Build (how we build, build order, briefs per course, audits, bibliography, hub
template, changelog). The data folder holds the content (hub.py and the files it names); this
script holds the page structure; design/theme.css holds every style. The theme is inlined at build
time because a published artifact cannot load an external stylesheet: edit theme.css, rebuild,
republish, and the change reaches every hub.

Needs Python 3 and the `markdown` package (pip install markdown) for reading pages.
"""
import html as H, pathlib, re, runpy, sys
import markdown

GEN = pathlib.Path(__file__).resolve().parent
THEME = GEN.parent / 'design' / 'theme.css'
JS = GEN / 'hub.js'
ICON = {
    'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    'back': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg>',
    'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h5v-6h4v6h5V10"/></svg>',
    'sun': '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    'moon': '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    'close': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
}
e = H.escape


def build(data_dir):
    D = runpy.run_path(str(data_dir / 'hub.py'))
    C = D['COURSES']
    for c in C:
        c['k'] = c['key'].lower()
    LC, BC = D['LEARN_C'], D['BUILD_C']
    # a unit is written when hub.py maps it to a reading page (WRITTEN) or its brief is a WRITTEN note (v5.1 style)
    done = lambda u: u[0] in D['WRITTEN'] or u[4].startswith('WRITTEN')
    for c in C:
        c['done'] = sum(map(done, c['units']))
    written = sum(c['done'] for c in C)
    total = sum(len(c['units']) for c in C)
    every = D['AUDIT_EVERY']
    until = every - (written % every)
    titles = {u[0]: u[1] for c in C for u in c['units']}
    course_of = {u[0]: c for c in C for u in c['units']}
    names = {c['key']: c['name'] for c in C}

    # ---- reading pages and bibliography -----------------------------------------------
    links, readings = {}, []
    for r in D['READINGS']:
        src = (data_dir / r['md']).read_text(encoding='utf-8')
        src = re.sub(r'\A---\n.*?\n---\n', '', src, flags=re.S)   # filing front matter (method.md §7)
        src = re.sub(r'^# .*\n', '', src, count=1)
        for t, u in re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', src):
            links.setdefault(u, t)
        body = markdown.markdown(src, extensions=['tables'])
        body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
        body = body.replace('<a href=', '<a target="_blank" rel="noopener" href=')
        heads = []
        def hid(m, r=r):
            sid = f"{r['id']}-{len(heads)}"
            heads.append((sid, m.group(1)))
            return f'<h2 id="{sid}">{m.group(1)}</h2>'
        body = re.sub(r'<h2>(.*?)</h2>', hid, body)
        r['body'], r['toc'] = body, ''.join(f'<a href="#{s}">{t}</a>' for s, t in heads)
        readings.append(r)
    biblio = sorted(links.items(), key=lambda x: x[1].lower())

    # ---- pieces --------------------------------------------------------------------------
    def eyebrow(*parts):
        return '<div class="eyebrow">' + ' · '.join(f'<span class="u" style="--c:{col}">{e(t)}</span>' if col else e(t) for t, col in parts) + '</div>'

    def hero(eb, h1, lede, extra=''):
        lp = '<p class="lede">' + lede + '</p>' if lede else ''
        return f'<header class="hero">{eb}<h1>{h1}</h1>{lp}{extra}</header>'

    def meter(c):
        pct = round(100 * c['done'] / len(c['units']))
        return f'<div class="meter" style="--c:{c["color"]}"><span class="bar" aria-hidden="true"><i style="width:{pct}%"></i></span><span>{c["done"]}/{len(c["units"])} units written</span></div>'

    def unit_card(c, u, with_brief):
        code, title, scope, ships, brief = u
        is_done = done(u)
        deep = code.startswith('DD')
        col = 'var(--gold)' if deep else c['color']
        pill = '<span class="pill live">written</span>' if is_done else '<span class="pill">not written</span>'
        act = ''
        if not with_brief:
            act = (f'<a class="rlink" href="#{D["WRITTEN"][code]}">Read the unit →</a>' if is_done
                   else f'<a class="rlink dim" href="#briefs-{c["k"]}">Not written yet · brief in Build</a>')
        bh = ''
        if with_brief:
            full = brief if is_done else D['PRE'].replace('{GOAL}', c['goal']) + '\n\n' + brief
            bh = (f'<details class="prompt"><summary>{e(D["BRIEF_LABEL"])}</summary><div class="pbox"><pre>{e(full)}</pre>'
                  f'<div class="pbar"><button class="copy" type="button">Copy brief</button></div></div></details>')
        return (f'<article class="smod{" deep" if deep else ""}" id="{"b" if with_brief else "u"}-{code.lower()}" style="--c:{col}">'
                f'<div class="smod-top"><span class="code">{code}</span><h3>{e(title)}</h3>{pill}</div>'
                f'<p class="why">{e(scope)}</p><p class="ships"><b>Ships</b>{e(ships)}</p>{act}{bh}</article>')

    def panel(pid, u, t, col, body, nav=None):
        dn = ' data-nav="' + nav + '"' if nav else ''
        return f'<section class="panel stack" id="{pid}" data-u="{e(u)}" data-t="{e(t)}" data-c="{col}"{dn} hidden>{body}</section>'

    def logrows(rows):
        return '<div class="logrows">' + ''.join(f'<div class="logrow"><span class="dt">{e(d)}</span><span>{t}</span></div>' for d, t in rows) + '</div>'

    P = []
    bar = D['BAR']

    # ---- Home ---------------------------------------------------------------------------
    tiles = (f'<a class="course live" href="#learn" style="--c:{LC}"><div class="ctop"><span class="cname">Learn</span></div>'
             f'<span class="ctitle">{D["LEARN_TILE"][0]}</span><p>{D["LEARN_TILE"][1]}</p><ul>'
             + ''.join(f'<li>{c["key"]} · {e(c["name"])} — {c["done"]}/{len(c["units"])} written</li>' for c in C) + '</ul></a>'
             f'<a class="course live" href="#build" style="--c:{BC}"><div class="ctop"><span class="cname">Build</span></div>'
             f'<span class="ctitle">{D["BUILD_TILE"][0]}</span><p>{D["BUILD_TILE"][1]}</p><ul>'
             f'<li>Next to write: {D["NEXT_UNIT"]} ({next((m for k, m, s in D["ORDER"] if k == D["NEXT_UNIT"]), "Opus 5.5")})</li><li>Next audit: {D["NEXT_AUDIT"]}</li><li>{len(biblio)} sources on file</li></ul></a>')
    stats = (f'<div class="stats" data-n="4"><div><b>{written}/{total}</b><span>units written</span></div><div><b>{D["AUDITS_RUN"]}</b><span>audits run</span></div>'
             f'<div><b>{until}</b><span>unit{"s" if until != 1 else ""} until next audit</span></div><div><b>{D["NEXT_UNIT"]}</b><span>next to write</span></div></div>')
    P.append(panel('home', f'{bar}', 'Home', LC,
                   hero(eyebrow((bar, LC), ('Home', None)), D['HOME_H1'], D['HOME_LEDE']) + f'<div class="cgrid">{tiles}</div>' + stats + D['FRAME']))

    # ---- Learn ----------------------------------------------------------------------------
    cards = ''.join(f'<a class="course live" href="#course-{c["k"]}" style="--c:{c["color"]}"><div class="ctop"><span class="cname">Course {c["key"]}</span></div>'
                    f'<span class="ctitle">{e(c["name"])}</span><p>{e(c["tile"])}</p>{meter(c)}</a>' for c in C)
    wm = ''.join(f'<a class="hrow" href="#{r["id"]}" style="--c:{next((c for c in C if c["key"]==r["course"]), {"color":"var(--red)"})["color"]}"><span class="n">{r["course"]}</span><span class="t">{e(r["title"])}<small>{("covers " + " · ".join(r["covers"])) if r["covers"] else "superseded record"}</small></span></a>' for r in readings)
    P.append(panel('learn', f'{bar} · LEARN', 'Courses', LC,
                   hero(eyebrow(('LEARN', LC)), 'The courses', D['LEARN_LEDE']) + f'<div class="cgrid">{cards}</div>'
                   + f'<h2 class="hsec">Written material</h2><div class="hrows">{wm}</div><p class="hnote">{D["LEARN_NOTE"]}</p>'))

    for c in C:
        goal = (f'<section class="howto edge" style="--hc:var(--blue)"><h2>Goal</h2><p>{c["goal"][0].upper() + c["goal"][1:]}</p><ul>{c["outcomes"]}</ul>'
                f'<p class="over">{D["COURSE_NOTE"]}</p></section>')
        units = '<div class="smods">' + ''.join(unit_card(c, u, False) for u in c['units']) + '</div>'
        P.append(panel(f'course-{c["k"]}', f'{bar} · LEARN', f'Course {c["key"]}', c['color'],
                       hero(eyebrow(('LEARN', LC), (f'COURSE {c["key"]}', c['color'])), e(c['name']), c['intro'], meter(c)) + goal + units
                       + f'<p class="hnote">To write a unit, or to see its brief, go to <a href="#briefs-{c["k"]}">Build · Briefs · course {c["key"]}</a>.</p>'))

    for r in readings:
        c = next(x for x in C if x['key'] == r['course'])
        pills = ''.join(f'<span class="pill live">{x}</span>' for x in r['covers'])
        head = (f'<a class="rlink" href="#course-{c["k"]}">← {e(c["name"])}</a>'
                + eyebrow(('LEARN', LC), (f'COURSE {c["key"]}', c['color']), ('written material', None)).replace('</div>', ' ' + pills + '</div>')
                + f'<h1>{e(r["title"])}</h1><nav class="toc" aria-label="Sections">{r["toc"]}</nav>')
        P.append(panel(r['id'], f'{bar} · LEARN', r['name'], c['color'],
                       f'<header class="hero phead">{head}</header><p class="lede">{r["intro"]}</p><div class="report">{r["body"]}</div>', nav=f'course-{c["k"]}'))

    # ---- Build -----------------------------------------------------------------------------
    blinks = [('order', '1·2', 'Build order with models', f'{total - written} units to go')]
    blinks += [(f'briefs-{c["k"]}', f'P·{c["key"]}', f'Briefs · {c["name"]}', f'{len(c["units"]) - c["done"]} open') for c in C]
    blinks += [('audits', 'AU', 'Audits and audit prompts', f'next {D["NEXT_AUDIT"]}'), ('bibliography', 'BIB', 'Bibliography', f'{len(biblio)} sources'),
               ('template', 'T', 'Hub template', 'for the next project'), ('changelog', 'LOG', 'Changelog', D['VERSION'].split(' · ')[0])]
    rows = ''.join(f'<a class="hrow" href="#{h}" style="--c:{BC}"><span class="n">{n}</span><span class="t">{t}<small>{s}</small></span></a>' for h, n, t, s in blinks)
    P.append(panel('build', f'{bar} · BUILD', 'How we build', BC,
                   hero(eyebrow(('BUILD', BC)), 'How the courses get made', D['BUILD_LEDE'])
                   + D['LEARNING_NOTE'] + f'<section class="howto" style="--hc:{BC}"><h2>Build pages</h2><div class="hrows">{rows}</div></section>'
                   + D['BUILD_PICK'] + D['BUILD_BODY']))

    trs, n = [], written
    for d in D['DONE_ROWS']:
        trs.append('<tr class="done">' + ''.join(f'<td>{x}</td>' for x in d) + '</tr>')
    for code, model, search in D['ORDER']:
        n += 1
        col = course_of[code]['color']
        st = D.get('STATUS', {}).get(code, '')
        trs.append(f'<tr{" class=\"done\"" if st else ""}><td>{n}</td><td class="code" style="--c:{col}">{code}</td><td>{e(titles[code])}</td><td>{model}</td><td>{search}</td><td>{e(st)}</td></tr>')
        if n % every == 0:
            a = D['AUDIT_ROW']
            trs.append(f'<tr class="audit"><td>✓</td><td class="code">Audit {n // every}</td><td>{a[0]}</td><td>{a[1]}</td><td>{a[2]}</td><td>{a[3]}</td></tr>')
    f = D['FINAL_AUDIT']
    trs.append(f'<tr class="audit"><td>✓</td><td class="code">{f[0]}</td><td>{f[1]}</td><td>{f[2]}</td><td>{f[3]}</td><td>{f[4]}</td></tr>')
    table = ('<div class="report"><div class="tbl"><table class="order"><thead><tr><th>#</th><th>Unit</th><th>Title</th><th>Model</th><th>Search</th><th>Status</th></tr></thead><tbody>'
             + ''.join(trs) + '</tbody></table></div></div>')
    P.append(panel('order', f'{bar} · BUILD', 'Build order', BC,
                   hero(eyebrow(('BUILD', BC), ('BUILD ORDER', None)), 'Building order, with models', D['ORDER_LEDE'])
                   + D['ORDER_NOTES'] + table + f'<p class="hnote">{D["ORDER_FOOT"].format(start=written + 1)}</p>'))

    for c in C:
        P.append(panel(f'briefs-{c["k"]}', f'{bar} · BUILD', f'Briefs {c["key"]}', BC,
                       hero(eyebrow(('BUILD', BC), ('BRIEFS', None), (f'COURSE {c["key"]}', c['color'])), e(c['name']), D['BRIEFS_LEDE'].format(k=c['k'], K=c['key']))
                       + '<div class="smods">' + ''.join(unit_card(c, u, True) for u in c['units']) + '</div>'))

    prompts = ''.join(f'<details class="prompt"{" open" if op else ""}><summary>{e(t)}</summary><div class="pbox"><pre>{e(p)}</pre>'
                      f'<div class="pbar"><button class="copy" type="button">Copy prompt</button></div></div></details>' for t, op, p in D['AUDIT_PROMPTS'])
    P.append(panel('audits', f'{bar} · BUILD', 'Audits', BC,
                   hero(eyebrow(('BUILD', BC), ('AUDITS', None)), 'Fable audit log and prompts', D['AUDITS_LEDE'])
                   + f'<section class="howto" style="--hc:var(--gold)"><h2>Audit log</h2>{logrows(D["AUDIT_LOG"])}</section>'
                   + f'<h2 class="hsec">Audit prompts</h2><p class="hnote">{D["AUDIT_PROMPTS_NOTE"]}</p><div>{prompts}</div>'))

    bib = ''.join(f'<a class="hrow" target="_blank" rel="noopener" href="{e(u)}"><span class="t">{e(t)}<small class="url">{e(u.split("//")[1].split("/")[0])}</small></span></a>' for u, t in biblio)
    P.append(panel('bibliography', f'{bar} · BUILD', 'Bibliography', BC,
                   hero(eyebrow(('BUILD', BC), ('BIBLIOGRAPHY', None)), f'Sources used so far ({len(biblio)})', D['BIB_NOTE']) + f'<div class="hrows">{bib}</div>'))

    blocks = ''.join(f'<section class="howto" style="--hc:var(--blue)"><h2>{e(t)}</h2>{b}</section>' for t, b in D['TEMPLATE_BLOCKS'])
    P.append(panel('template', f'{bar} · BUILD', 'Hub template', BC,
                   hero(eyebrow(('BUILD', BC), ('HUB TEMPLATE', None)), 'How to start the next course hub', D['TEMPLATE_LEDE']) + D['TEMPLATE_NOTE'] + blocks))

    cl = [(d, t.format(A=names.get('A', ''), B=names.get('B', ''))) for d, t in D['CHANGELOG']]
    P.append(panel('changelog', f'{bar} · BUILD', 'Changelog', BC,
                   hero(eyebrow(('BUILD', BC), ('CHANGELOG', None)), 'What changed, when', '') + logrows(cl)))

    # ---- drawer --------------------------------------------------------------------------
    def di(target, n, t, col, sub=False):
        return f'<a class="ditem{" sub" if sub else ""}" href="#{target}" data-target="{target}" style="--c:{col}"><span class="n">{n}</span><span class="t">{e(t)}</span></a>'
    nav = ('<nav class="dlist" aria-label="Pages"><div class="dtop">' + di('home', '⌂', 'Home', 'var(--muted)').replace('class="ditem"', 'class="ditem dhome"') + '</div>'
           + f'<div class="dsec hub" style="--c:{LC}">Learn</div>' + di('learn', 'L', 'Courses overview', LC)
           + ''.join(di(f'course-{c["k"]}', c['key'], c['name'], c['color'], True) for c in C)
           + f'<div class="dsec hub" style="--c:{BC}">Build</div>' + di('build', 'B', 'How we build', BC)
           + di('order', '1·2', 'Build order', BC, True)
           + ''.join(di(f'briefs-{c["k"]}', f'P·{c["key"]}', f'Briefs · course {c["key"]}', BC, True) for c in C)
           + di('audits', 'AU', 'Audits', BC, True) + di('bibliography', 'BIB', 'Bibliography', BC, True)
           + di('template', 'T', 'Hub template', BC, True) + di('changelog', 'LOG', 'Changelog', BC, True) + '</nav>')

    css = THEME.read_text(encoding='utf-8')
    js = JS.read_text(encoding='utf-8')
    key = D['THEME_KEY']
    page = f'''<!doctype html>
<html lang="en" data-theme-key="{key}">
<head>
<meta charset="utf-8">
<title>{e(D['TITLE'])}</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<style>
{css}
</style>
<script>try{{var t=localStorage.getItem('{key}');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
</head>
<body>
<header class="top"><div class="top-in">
  <button class="ib" id="menuB" type="button" aria-label="Open contents" aria-expanded="false" aria-controls="drawer">{ICON['menu']}</button>
  <button class="ib" id="backB" type="button" aria-label="Back">{ICON['back']}</button>
  <div class="cur" id="cur"><span class="cur-u" id="curU"></span><span class="cur-t" id="curT"></span></div>
  <a class="ib" id="homeB" href="#home" aria-label="Hub home">{ICON['home']}</a>
  <button class="ib" id="themeB" type="button" aria-label="Switch theme">{ICON['sun']}{ICON['moon']}</button>
</div></header>
<div class="backdrop" id="backdrop"></div>
<aside class="drawer" id="drawer" aria-hidden="true" aria-label="Contents">
  <div class="dhead"><div class="brand">{D['BRAND_HTML']}</div><button class="ib" id="closeB" type="button" aria-label="Close contents">{ICON['close']}</button></div>
  {nav}
  <div class="dfoot mono">{D['VERSION']} · {written}/{total} units written</div>
</aside>
<main>
{''.join(P)}
</main>
<script>
{js}
</script>
</body>
</html>
'''
    out = GEN / 'hubs' / D['OUT']
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding='utf-8')
    return out, len(page), written, total, len(biblio)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out, size, w, t, nb = build((GEN / sys.argv[1]).resolve() if not pathlib.Path(sys.argv[1]).is_absolute() else pathlib.Path(sys.argv[1]))
    print(f'wrote {out.relative_to(GEN)}: {size:,} chars · {w}/{t} units written · {nb} sources · theme {THEME.relative_to(GEN.parent)}')
