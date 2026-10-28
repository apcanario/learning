"""The markdown course family for build.py (docs/academy.md A3): Brand + AI, and any course whose units are
Markdown files and whose content is a data file in the shape of generator/data/brand-ai/hub.py (AD5).

One Academy course per entry in the data file's COURSES (AD6), each its own drawer context, with:
  the course home        goal, outcomes, progress, the units in writing order, the audits run
  one reading page       per written unit (the unit's Markdown on the theme classes), the course's "reports"
  How it is built        the shared method page, the build order with models, this course's briefs (copyable),
                         the audit log and prompts, the bibliography collected from this course's units, the
                         course's changelog
The hub pages of generator/build_hub.py (retired at A3) are the origin of these; the data file is unchanged.
Needs the `markdown` package (pip install markdown).
"""
import html as H, re
import markdown
import viz


def _words(n):
    """0–99 as an English word, for ledes."""
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
            'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if n < 20: return ones[n]
    if n < 100: return tens[n // 10] + ('' if n % 10 == 0 else '-' + ones[n % 10])
    return str(n)

e = H.escape


def render_md(src):
    """A unit file (method.md §7: front matter, then Markdown ending with the deliverable and a Sources list) to
    theme-classed HTML. Returns (body html, toc html, links {url: title})."""
    src = re.sub(r'\A---\n.*?\n---\n', '', src, flags=re.S)
    src = re.sub(r'^# .*\n', '', src, count=1, flags=re.M)   # the unit's own title line; the page has its h1
    src, figs = viz.extract_md(src)     # A8: ```viz fences become drawings
    links = {}
    for t, u in re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', src):
        links.setdefault(u, t)
    body = markdown.markdown(src, extensions=['tables'])
    body = viz.restore_md(body, figs)
    body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    body = body.replace('<a href=', '<a target="_blank" rel="noopener" href=')
    return body, links


def build(m, crumbs, theme, pill_next, chev):
    """Panels and the drawer nav for one markdown Academy course. m is a course dict from build.py:md_courses
    (parent = the data file's course with .hub = the module). Returns (panels list, nav html, bibliography size)."""
    c, sc, d = m['parent'], m['sc'], m['parent']['hub']
    ctx, k, col, key = m['id'], sc['k'], m['color'], sc['key']
    courses = d.COURSES
    done = lambda u: u[0] in d.WRITTEN
    C_DONE = {x['key']: sum(map(done, x['units'])) for x in courses}
    written = sum(C_DONE.values())
    total = sum(len(x['units']) for x in courses)
    titles = {u[0]: u[1] for x in courses for u in x['units']}
    course_of = {u[0]: x for x in courses for u in x['units']}
    ulabel = m['short'].upper()
    BR, BP = m['briefs_id'], m['brief_anchor']        # briefs-a and b-a2 for Brand + AI; <id>-briefs and <id>-b-a1 otherwise

    def panel(pid, kind, body, t=None, u=None, cls='stack', split=None):
        """split names the file stem when the panel leaves the shell as a fetched file (build.py's split, A2 and P20)."""
        tu = (f' data-t="{e(t)}"' if t else '') + (f' data-u="{e(u)}"' if u else '') + (f' data-split="{split}"' if split else '')
        return f'<section class="panel{(" " + cls) if cls else ""}" id="{pid}" data-ctx="{ctx}" data-kind="{kind}"{tu} data-c="{col}" style="--cc:{col}" hidden>{body}</section>'

    def eyebrow(*parts):
        return '<div class="eyebrow">' + ' · '.join(f'<span class="u" style="--c:{cc}">{e(t)}</span>' if cc else e(t) for t, cc in parts) + '</div>'

    def logrows(rows):
        return '<div class="logrows">' + ''.join(f'<div class="logrow"><span class="dt">{e(dt)}</span><span>{t}</span></div>' for dt, t in rows) + '</div>'

    # ---- reading pages (this course's units), bibliography from their links -------------------------
    readings, links = [], {}
    for r in d.READINGS:
        if r['course'] != key:
            continue
        src = r['path'].read_text(encoding='utf-8')   # set by build.py:load_markdown (vault or data folder)
        body, lk = render_md(src)
        for u, t in lk.items():
            links.setdefault(u, t)
        heads = []
        def hid(mm, r=r):
            sid = f"{r['id']}-{len(heads)}"
            heads.append((sid, mm.group(1)))
            return f'<h2 id="{sid}">{mm.group(1)}</h2>'
        body = re.sub(r'<h2>(.*?)</h2>', hid, body)
        r['body'], r['toc'] = body, ''.join(f'<a href="#{s}">{t}</a>' for s, t in heads)
        readings.append(r)
    biblio = sorted(links.items(), key=lambda x: x[1].lower())
    read_of = {code: r for r in readings for code in r['covers']}
    first = next((u for u in sc['units'] if u[0] in read_of), None)

    t = theme[m['theme']]
    course_crumb = (f"Course {key} · {m['short']}", ctx)
    P = []

    # ---- course home ------------------------------------------------------------------------
    rows = ''
    for code, title, scope, *_ in sc['units']:
        if code in read_of:
            rid = read_of[code]['id']
            rows += f'<a class="hrow" href="#{rid}" data-target="{rid}"><span class="n">{code}</span><span class="t">{e(title)}<small>{e(scope)}</small></span></a>'
        else:
            pill = pill_next if code == d.NEXT_UNIT else '<span class="pill">soon</span>'
            rows += f'<div class="hrow soon"><span class="n">{code}</span><span class="t">{e(title)}<small>{e(scope)}</small></span>{pill}</div>'
    pct = round(100 * m['nwritten'] / m['nunits'])
    audits = ''.join(f'<li><strong>{e(dt)}</strong> · {txt}</li>' for dt, txt in d.AUDIT_LOG)
    start = (f'<a class="hbtn start" href="#{read_of[first[0]]["id"]}" data-target="{read_of[first[0]]["id"]}"><span>Start the course</span><b>{e(first[0] + " " + first[1])}</b></a>' if first
             else f'<a class="hbtn start" href="#{BR}" data-target="{BR}"><span>Open the course</span><b>No unit written yet · the briefs</b></a>')
    frame = getattr(d, 'FRAME', '') if key == 'A' else ''
    P.append(panel(ctx, 'course', f'''
  <header class="hero">
    {crumbs(('Academy', 'home'), (t['name'], 'track-' + m['theme']), (course_crumb[0], None))}
    {eyebrow((f'COURSE {key}', col), ('Brand + AI', None), ('IN PROGRESS', 'var(--gold)'))}
    <h1>{e(m['name'])}</h1>
    <p class="lede">{sc['intro']}</p>
    <div class="stats" data-n="4"><div><b>{m['nwritten']}</b><span>of {m['nunits']} units written</span></div><div><b>{pct}%</b><span>of the course</span></div><div><b>{len(d.AUDIT_LOG)}</b><span>audit{'s' if len(d.AUDIT_LOG) != 1 else ''} run</span></div><div><b>{e(d.NEXT_UNIT)}</b><span>next unit to write</span></div></div>
    <div class="hlinks"><a class="hbtn cont" href="#{ctx}" data-course="{ctx}" hidden><span>Continue</span><b></b></a>{start}<a class="hbtn alt" href="#{BR}" data-target="{BR}"><span>Briefs</span><b>Every unit's brief, copyable</b></a></div>
  </header>
  <section class="howto edge" style="--hc:var(--blue)"><h2>What you will be able to do</h2><p>{e(sc['goal'][0].upper() + sc['goal'][1:])}</p><ul>{sc['outcomes']}</ul><p class="over">{d.COURSE_NOTE}</p></section>
  <h2 class="hsec">Units, in writing order</h2>
  <div class="hrows">{rows}</div>
  <details class="howto rules"><summary><h2>Audits run</h2><span>{len(d.AUDIT_LOG)} · next {e(d.NEXT_AUDIT)}</span></summary><ul>{audits}</ul></details>
  {frame}
  <a class="hbtn alt wide" href="#{ctx}-build" data-target="{ctx}-build"><span>How it is built</span><b>Method, build order, briefs, audits, sources, changelog.</b></a>
  <a class="hbtn alt wide" href="#{ctx}-built" data-target="{ctx}-built"><span>How it was built</span><b>The model behind each unit, every check and audit with its verdict, the flags still open.</b></a>
  <a class="hbtn alt wide" href="#home" data-target="home"><span>Academy</span><b>Back to every course.</b></a>''', t=m['short'], u=f'COURSE {key}', cls='home'))

    # ---- reading pages ----------------------------------------------------------------------
    for r in readings:
        pills = ''.join(f'<span class="pill live">{x}</span>' for x in r['covers'])
        code = r['covers'][0] if r['covers'] else ''
        P.append(panel(r['id'], 'report', f'''
  <header class="phead">
    {crumbs(('Academy', 'home'), course_crumb, (code or r['name'], None))}
    {(eyebrow((ulabel, col), (code, None)) if code else eyebrow((ulabel, col))).replace('</div>', ' ' + pills + '</div>') if pills else (eyebrow((ulabel, col), (code, None)) if code else eyebrow((ulabel, col)))}
    <h1>{e(r['title'])}</h1>
    <nav class="toc" aria-label="Sections">{r['toc']}</nav>
  </header>
  <p class="lede">{r['intro']}</p>
  <div class="report">{r['body']}</div>
  <div class="pager"></div>''', cls='', split=r['id']))

    # ---- How it is built ----------------------------------------------------------------------
    bid = f'{ctx}-build'
    pages = [(bid, 'M', 'How we build', 'procedure, models, review rule'), (f'{ctx}-order', '1·2', 'Build order with models', f'{total - written} units to go'),
             (BR, f'P·{key}', f'Briefs · course {key}', f'{len(sc["units"]) - C_DONE[key]} open'), (f'{ctx}-audits', 'AU', 'Audits and audit prompts', f'next {d.NEXT_AUDIT}'),
             (f'{ctx}-bibliography', 'BIB', 'Bibliography', f'{len(biblio)} sources'), (f'{ctx}-changelog', 'LOG', 'Changelog', d.VERSION.split(' · ')[0]),
             (f'{ctx}-built', '✓', 'How it was built', 'models, checks, audits, flags')]   # the page itself is howbuilt.py's (A4)
    prow = ''.join(f'<a class="hrow" href="#{h}" data-target="{h}" style="--c:{col}"><span class="n">{n}</span><span class="t">{tt}<small>{e(s)}</small></span></a>' for h, n, tt, s in pages)
    bc = (('Academy', 'home'), course_crumb)
    P.append(panel(bid, 'build', f'''
  <header class="hero">{crumbs(*bc, ('How it is built', None))}{eyebrow((ulabel, col), ('HOW IT IS BUILT', None))}<h1>How the course gets made</h1><p class="lede">{d.BUILD_LEDE}</p></header>
  {d.LEARNING_NOTE}<section class="howto" style="--hc:{col}"><h2>Build pages</h2><div class="hrows">{prow}</div></section>
  {d.BUILD_PICK}{d.BUILD_BODY}''', t='How it is built', u=ulabel))

    # build order (shared across the data file's courses; numbered as docs/courses-index.md numbers the units)
    filed = sum(1 for cc, _, _ in d.ORDER if cc in d.STATUS)
    start_n = written - filed
    remaining = len(d.ORDER) - filed   # derived from ORDER and STATUS; never typed in the data file (P15)
    order_lede = f'{_words(remaining).capitalize()} {"unit remains" if remaining == 1 else "units remain"}. {d.ORDER_LEDE}'
    trs, n = [], start_n
    for row in d.DONE_ROWS:
        trs.append('<tr class="done">' + ''.join(f'<td>{x}</td>' for x in row) + '</tr>')
    for i, (code, model, search) in enumerate(d.ORDER):
        n += 1
        st = d.STATUS.get(code, '')
        trs.append(f'<tr{" class=\"done\"" if st else ""}><td>{n}</td><td class="code" style="--c:{course_of[code]["color"]}">{code}</td><td>{e(titles[code])}</td><td>{model}</td><td>{search}</td><td>{e(st)}</td></tr>')
        if n % d.AUDIT_EVERY == 0 and i < len(d.ORDER) - 1:
            a = d.AUDIT_ROW
            trs.append(f'<tr class="audit"><td>✓</td><td class="code">Audit {n // d.AUDIT_EVERY}</td><td>{a[0]}</td><td>{a[1]}</td><td>{a[2]}</td><td>{a[3]}</td></tr>')
    f = d.FINAL_AUDIT
    trs.append(f'<tr class="audit"><td>✓</td><td class="code">{f[0]}</td><td>{f[1]}</td><td>{f[2]}</td><td>{f[3]}</td><td>{f[4]}</td></tr>')
    table = ('<div class="report"><div class="tbl"><table class="order"><thead><tr><th>#</th><th>Unit</th><th>Title</th><th>Model</th><th>Search</th><th>Status</th></tr></thead><tbody>' + ''.join(trs) + '</tbody></table></div></div>')
    P.append(panel(f'{ctx}-order', 'build', f'''
  <header class="hero">{crumbs(*bc, ('Build order', None))}{eyebrow((ulabel, col), ('BUILD ORDER', None))}<h1>Building order, with models</h1><p class="lede">{order_lede}</p></header>
  {d.ORDER_NOTES}{table}<p class="hnote">{d.ORDER_FOOT.format(start=start_n + 1)}</p>''', t='Build order', u=ulabel))

    # briefs (this course)
    cards = ''
    for u in sc['units']:
        code, title, scope, ships, brief = u
        is_done = done(u); deep = code.startswith('DD')
        ucol = 'var(--gold)' if deep else col
        pill = '<span class="pill live">written</span>' if is_done else '<span class="pill">not written</span>'
        full = brief if is_done else d.PRE.replace('{GOAL}', sc['goal']) + '\n\n' + brief
        read = f'<a class="rlink" href="#{read_of[code]["id"]}" data-target="{read_of[code]["id"]}">Read the unit →</a>' if code in read_of else ''
        cards += (f'<article class="smod{" deep" if deep else ""}" id="{BP}{code.lower()}" style="--c:{ucol}"><div class="smod-top"><span class="code">{code}</span><h3>{e(title)}</h3>{pill}</div>'
                  f'<p class="why">{e(scope)}</p><p class="ships"><b>Ships</b>{e(ships)}</p>{read}'
                  f'<details class="prompt"><summary>{e(d.BRIEF_LABEL)}</summary><div class="pbox"><pre>{e(full)}</pre><div class="pbar"><button class="copy" type="button">Copy brief</button></div></div></details></article>')
    lede = d.BRIEFS_LEDE.format(k=k, K=key).replace(f'Learn · Course {key}', f'Course {key}').replace(f'href="#course-{k}" data-target="course-{k}"', f'href="#{ctx}" data-target="{ctx}"')
    P.append(panel(BR, 'build', f'''
  <header class="hero">{crumbs(*bc, ('Briefs', None))}{eyebrow((ulabel, col), ('BRIEFS', None))}<h1>{e(sc['name'])}: the briefs</h1><p class="lede">{lede}</p></header>
  <div class="smods">{cards}</div>''', t='Briefs', u=ulabel, split='briefs'))

    # audits
    prompts = ''.join(f'<details class="prompt"{" open" if op else ""}><summary>{e(tt)}</summary><div class="pbox"><pre>{e(p)}</pre><div class="pbar"><button class="copy" type="button">Copy prompt</button></div></div></details>' for tt, op, p in d.AUDIT_PROMPTS)
    P.append(panel(f'{ctx}-audits', 'build', f'''
  <header class="hero">{crumbs(*bc, ('Audits', None))}{eyebrow((ulabel, col), ('AUDITS', None))}<h1>Fable audit log and prompts</h1><p class="lede">{d.AUDITS_LEDE}</p></header>
  <section class="howto" style="--hc:var(--gold)"><h2>Audit log</h2>{logrows(d.AUDIT_LOG)}</section>
  <h2 class="hsec">Audit prompts</h2><p class="hnote">{d.AUDIT_PROMPTS_NOTE}</p><div>{prompts}</div>''', t='Audits', u=ulabel))

    # bibliography
    bib = ''.join(f'<a class="hrow" target="_blank" rel="noopener" href="{e(u)}"><span class="t">{e(tt)}<small class="url">{e(u.split("//")[1].split("/")[0])}</small></span></a>' for u, tt in biblio)
    P.append(panel(f'{ctx}-bibliography', 'build', f'''
  <header class="hero">{crumbs(*bc, ('Bibliography', None))}{eyebrow((ulabel, col), ('BIBLIOGRAPHY', None))}<h1>Sources used so far ({len(biblio)})</h1><p class="lede">{d.BIB_NOTE}</p></header>
  <div class="hrows">{bib}</div>''', t='Bibliography', u=ulabel, split='bibliography'))

    # changelog (the data file's own, shared across its courses)
    names = {x['key']: x['name'] for x in courses}
    cl = [(dt, tt.format(A=names.get('A', ''), B=names.get('B', ''))) for dt, tt in d.CHANGELOG]
    P.append(panel(f'{ctx}-changelog', 'build', f'''
  <header class="hero">{crumbs(*bc, ('Changelog', None))}{eyebrow((ulabel, col), ('CHANGELOG', None))}<h1>What changed, when</h1><p class="lede">The course's own record, newest first; the site's changelog is on the Academy home.</p></header>
  {logrows(cl)}''', t='Changelog', u=ulabel))

    # ---- drawer -------------------------------------------------------------------------------
    units = ''
    for code, title, *_ in sc['units']:
        if code in read_of:
            units += f'<a class="ditem" href="#{read_of[code]["id"]}" data-target="{read_of[code]["id"]}"><span class="n">{code}</span><span class="t">{e(title)}</span></a>'
        else:
            pill = pill_next if code == d.NEXT_UNIT else '<span class="pill">soon</span>'
            units += f'<div class="dsoon"><span class="n">{code}</span><span class="t">{e(title)}</span>{pill}</div>'
    # readings that cover no unit (a superseded research page kept as the record) are listed after the units
    for r in readings:
        if not r['covers']:
            units += f'<a class="ditem" href="#{r["id"]}" data-target="{r["id"]}"><span class="n">·</span><span class="t">{e(r["name"])}</span></a>'
    bitems = ''.join(f'<a class="ditem" href="#{h}" data-target="{h}"><span class="n">{n}</span><span class="t">{tt}</span></a>' for h, n, tt, _ in pages)
    def group(gid, name, cnt, body, open_):
        return (f'<div class="dunit closed" data-unit="{ctx}:{gid}"{" data-open" if open_ else ""} data-ulabel="{ulabel}" style="--c:{col}"><button class="duh" type="button" aria-expanded="false"><span class="ut">{name}</span><span class="cnt">{cnt}</span>{chev}</button><div class="ditems">{body}</div></div>')
    nav = (f'<nav class="dlist" data-navctx="{ctx}" aria-label="{e(m["short"])} course" hidden>'
           f'<div class="dtop"><a class="ditem dhome" href="#home" data-target="home"><span class="n">←</span><span class="t">Academy</span></a>'
           f'<a class="ditem dhome" href="#{ctx}" data-target="{ctx}"><span class="n">⌂</span><span class="t">{e(m["short"])}: course home</span></a></div>'
           + group('units', 'Units', f'{m["nwritten"]}/{m["nunits"]}', units, True)
           + group('build', 'How it is built', str(len(pages)), bitems, False) + '</nav>')
    return P, nav, len(biblio)
