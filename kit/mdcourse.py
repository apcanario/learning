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


HTML_TAGS = {'a', 'abbr', 'b', 'br', 'cite', 'code', 'del', 'dfn', 'em', 'i', 'ins', 'kbd', 'mark', 'q', 's', 'small', 'span',
             'strong', 'sub', 'sup', 'u', 'var', 'img', 'wbr'}
VOID = {'br', 'img', 'wbr'}
TAG = re.compile(r'<(/?)([A-Za-z][\w-]*)([^<>]*)>')


def literal_brackets(src):
    """A placeholder written in angle brackets in running text (B4's "| <code> ·", B5's <date>) is text, not a tag:
    left raw, Markdown passes it to the page as an element, which hides it and (an unclosed <code>) swallows the rest
    of the unit (found 1 Nov 2026, P68). Outside fenced blocks and code spans, a bracketed word that is not an inline
    HTML element, or an element opened without its close in the same paragraph, or closed without its opening, is
    escaped so the reader sees it as written. Real inline HTML (<em>...</em>) is left alone, and so is every indented
    line (Markdown already shows an indented code block's brackets as text)."""
    def fix(par):
        parts = re.split(r'(`+[^`]*?`+)', par)          # code spans stay as written
        txt = '\x00'.join(parts[0::2])
        def esc(m):
            close, name = m.group(1), m.group(2).lower()
            if name in HTML_TAGS and (name in VOID or (re.search(rf'<{name}[\s>]', txt[:m.start()], re.I) if close
                                                        else re.search(rf'</{name}\s*>', txt[m.end():], re.I))):
                return m.group(0)
            return '&lt;' + m.group(0)[1:]
        txt = TAG.sub(esc, txt).split('\x00')
        parts[0::2] = txt
        return ''.join(parts)
    out, par, fence = [], [], False
    for ln in src.split('\n'):
        if re.match(r'\s*(```|~~~)', ln) or fence or not ln.strip() or re.match(r'( {4}|\t)', ln):   # indented code too
            if par:
                out.append(fix('\n'.join(par))); par = []
            if re.match(r'\s*(```|~~~)', ln):
                fence = not fence
            out.append(ln)
        else:
            par.append(ln)
    if par:
        out.append(fix('\n'.join(par)))
    return '\n'.join(out)


def render_md(src):
    """A unit file (method.md §7: front matter, then Markdown ending with the deliverable and a Sources list) to
    theme-classed HTML. Returns (body html, toc html, links {url: title})."""
    src = re.sub(r'\A---\n.*?\n---\n', '', src, flags=re.S)
    src = re.sub(r'^# .*\n', '', src, count=1, flags=re.M)   # the unit's own title line; the page has its h1
    src, figs = viz.extract_md(src)     # A8: ```viz fences become drawings
    src = literal_brackets(src)
    links = {}
    for t, u in re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', src):
        links.setdefault(u, t)
    body = markdown.markdown(src, extensions=['tables'])
    body = viz.restore_md(body, figs)
    body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    body = body.replace('<a href=', '<a target="_blank" rel="noopener" href=')
    return body, links


# ---- P68 · the reading layout (1 Nov 2026) -------------------------------------------------------------------------
# One rule for every unit and report of every course (this family's reading pages and build.py's history reports):
# content first (the one-line scope, then section 1), one section at a time (a sticky bar with "Section n of N", a
# progress bar, the section menu and a "Whole unit" toggle; next and previous at each section's end), each h2 a numbered
# band, and process last (Sources, then "How this unit was made", two closed accordions after the text). The text is
# never changed: the sections are the h2s the unit already has, cut where they stand; shell.js does the stepping.
PROCESS_H2 = re.compile(r'^(?:sources|(?:writer.s )?unsure list|fresh check\b.*)$', re.I)
H2 = re.compile(r'<h2 id="([^"]+)">(.*?)</h2>', re.S)
FRESH = re.compile(r'<(li|p)>(Fresh check\b.*?)</\1>\s*', re.S)


def plain(h):
    return H.unescape(re.sub(r'<[^>]+>', '', h)).strip()


def sections(body):
    """A body whose top-level h2s carry ids, cut at each h2: (text before the first h2, [(id, heading html, html after
    it up to the next h2)]). Each piece must close every block it opens, or the cut was not at the top level."""
    cuts = list(H2.finditer(body))
    pre = body[:cuts[0].start()] if cuts else body
    out = []
    for k, m in enumerate(cuts):
        end = cuts[k + 1].start() if k + 1 < len(cuts) else len(body)
        out.append((m.group(1), m.group(2), body[m.end():end]))
    for _, _, x in out + [('', '', pre)]:
        for tag in ('div', 'section', 'details', 'figure', 'ul', 'ol', 'table', 'blockquote'):
            assert len(re.findall(rf'<{tag}[\s>]', x)) == len(re.findall(rf'</{tag}>', x)), f'P68: an h2 inside a <{tag}>; the section cut would break it'
    return pre, out


def band(sid, head, k):
    """An h2 drawn as a numbered band: the numeral is the section's place (01, 02 ...); a heading 'X · title' shows X
    as the kicker above its title, except a bare number equal to the place, which the numeral already shows."""
    m = re.match(r'^(.*?)\s+·\s+(.*)$', head, re.S)
    kick, title = (m.group(1).strip(), m.group(2)) if m else ('', head)
    if kick.isdigit() and int(kick) == k + 1:
        kick = ''
    return (f'<h2 id="{sid}" class="band"><span class="bn" aria-hidden="true">{k + 1:02d}</span>'
            f'<span class="bh">{f"<span class=bk>{kick}</span>" if kick else ""}<span class="bt">{title}</span></span></h2>'), kick, title


def reading(pid, body, scope, sources, made, nsrc=None, chev=''):
    """The reading layout for one page. body: the unit's HTML with ids on its h2s and the process sections already
    taken out; scope: the one-line scope (html, may be empty); sources: the Sources list (html, may be empty);
    made: [(heading, html, id or None)] for "How this unit was made". Returns (the scope line for the header, the
    sticky bar and the stepped text, which follow the header, and the two accordions)."""
    pre, secs = sections(body)
    if not secs:                                  # a page with no h2 is one section
        secs, pre = [(f'{pid}-0', '', pre)], ''
    n = len(secs)
    items, steps = [], []
    for k, (sid, head, html_) in enumerate(secs):
        b, kick, title = band(sid, head, k) if head else ('', '', 'The unit')
        items.append((sid, kick, title))
    for k, (sid, head, html_) in enumerate(secs):
        b = band(sid, head, k)[0] if head else ''
        nav = ''
        if k > 0:
            nav += f'<a class="sprev" href="#{items[k - 1][0]}" data-step="{k - 1}"><span>Previous · {k} of {n}</span><b>{e(plain(items[k - 1][2]))}</b></a>'
        if k < n - 1:
            nav += f'<a class="snext" href="#{items[k + 1][0]}" data-step="{k + 1}"><span>Next · {k + 2} of {n}</span><b>{e(plain(items[k + 1][2]))}</b></a>'
        else:
            nav += f'<a class="snext send" href="#{pid}-sources" data-acc><span>End of the unit</span><b>Sources and how it was made</b></a>'
        steps.append(f'<section class="sec" data-step="{k}">{pre if k == 0 else ""}{b}{html_}<nav class="secnav" aria-label="Sections">{nav}</nav></section>')
    menu = ''.join(f'<li><a href="#{sid}" data-step="{k}"><span class="n">{k + 1:02d}</span><span class="t">{(e(plain(kick)) + " · ") if kick else ""}{e(plain(t))}</span></a></li>'
                   for k, (sid, kick, t) in enumerate(items))
    bar = (f'<div class="stepbar" data-n="{n}"><details class="secmenu"><summary><span class="sh"><span class="sof">Section <b>1</b> of {n}</span>'
           f'<span class="stt">{e(plain(items[0][2]))}</span></span>{chev}</summary><ol class="seclist">{menu}</ol>'
           f'<div class="secx"><a href="#{pid}-sources" data-acc>Sources</a><a href="#{pid}-made" data-acc>How this unit was made</a>'
           f'<button class="whole" type="button" aria-pressed="false">Whole unit</button></div></details><div class="sprog" aria-hidden="true"><i></i></div></div>')
    head = f'<p class="scope">{scope}</p>' if scope else ''
    cnt = f'<span class="an">{nsrc}</span>' if nsrc else ''
    src = (f'<details class="acc src" id="{pid}-sources"><summary><span class="at">Sources</span>{cnt}</summary><div class="accb">{sources or "<p>No source list on file for this page.</p>"}</div></details>')
    mk = ''.join((f'<h3 id="{i}">' if i else '<h3>') + f'{h}</h3>{x}' for h, x, i in made if x)
    howm = (f'<details class="acc made" id="{pid}-made"><summary><span class="at">How this unit was made</span>'
            f'<span class="an">{len([1 for _, x, _ in made if x])} parts</span></summary><div class="accb">{mk}</div></details>')
    return head, bar + f'<div class="report steps">{"".join(steps)}</div>', f'<div class="process">{src}{howm}</div>'


def brief_box(text, label='Copy brief'):
    return f'<div class="pbox"><pre>{e(text)}</pre><div class="pbar"><button class="copy" type="button">{label}</button></div></div>'


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
    frame = getattr(d, 'FRAME', '') if sc is courses[0] else ''      # the frame is shown on the data file's first course
    P.append(panel(ctx, 'course', f'''
  <header class="hero">
    {crumbs(('Academy', 'home'), (t['name'], 'track-' + m['theme']), (course_crumb[0], None))}
    {eyebrow((f'COURSE {key}', col), (c['short'], None), (m['status'].upper(), 'var(--gold)'))}
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
    unit_of = {u[0]: u for x in courses for u in x['units']}
    for r in readings:
        pills = ''.join(f'<span class="pill live">{x}</span>' for x in r['covers'])
        code = r['covers'][0] if r['covers'] else ''
        # P68: the process sections leave the text for the end: Sources to its accordion; the unsure list, any fresh
        # check (its own h2, or the line the writer added to the unsure list), the provenance paragraph and the brief
        # to "How this unit was made"
        pre, secs = sections(r['body'])
        text, src, src_id, unsure, fresh = [], '', None, [], []
        for sid, head, x in secs:
            ph = plain(head)
            if not PROCESS_H2.match(ph):
                text.append(f'<h2 id="{sid}">{head}</h2>{x}')
            elif ph.lower() == 'sources':
                src, src_id = x, sid
            elif ph.lower().startswith('fresh check'):
                fresh.append((head, x, sid))
            else:
                lines = ''.join(f'<p>{ln}</p>' for _, ln in FRESH.findall(x))
                x = re.sub(r'<(ul|ol)>\s*</\1>', '', FRESH.sub('', x))
                unsure.append((head, x, sid))
                if lines:
                    fresh.append(('Fresh check', lines, None))
        u = unit_of.get(code)
        made = [('Provenance', f'<p>{r["intro"]}</p>', None)] + unsure + fresh + ([('The brief', brief_box(u[4]), None)] if u else [])
        head, steps, end = reading(r['id'], pre + ''.join(text), e(u[2]) if u else '', src, made, src.count('<li>'), chev)
        if src_id:            # the Sources heading's old id still lands, on the accordion's title
            end = end.replace('<span class="at">Sources</span>', f'<span class="at" id="{src_id}">Sources</span>', 1)
        P.append(panel(r['id'], 'report', f'''
  <header class="phead">
    {crumbs(('Academy', 'home'), course_crumb, (code or r['name'], None))}
    {(eyebrow((ulabel, col), (code, None)) if code else eyebrow((ulabel, col))).replace('</div>', ' ' + pills + '</div>') if pills else (eyebrow((ulabel, col), (code, None)) if code else eyebrow((ulabel, col)))}
    <h1>{e(r['title'])}</h1>
    {head}
  </header>
  {steps}
  {end}
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
