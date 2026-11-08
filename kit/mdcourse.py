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
import html as H, json, re
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
    # P94 check: 'fenced_code', so a fenced block the writer wrote at the top level is the code block it is (without it
    # A1's bio drafts, B7's two thumbnail styles and DD-B1's skill file showed as paragraphs with their fences, a "> "
    # line of B7's as a quotation and DD-B1's "---" as a heading, a section of its own named "```")
    body = markdown.markdown(src, extensions=['tables', 'fenced_code'])
    body = viz.restore_md(body, figs)
    body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    body = body.replace('<a href=', '<a target="_blank" rel="noopener" href=')
    return body, links


# ---- P71-3 · a history report in Markdown (1 Nov 2026) --------------------------------------------------------------
# Greece and Rome moved into the vault as Markdown (docs/p71-3.md). A report's file holds its text, its figure
# declarations (```viz) and its trees (```tree); history_html turns it into the fragment build.py and epub.py lay out,
# the same HTML the kit's r-<id>.html fragments held before. The forms (and what each becomes):
#   ## / ###                       h2 / h3
#   a paragraph opening **Where sources disagree.**     the dispute box, <aside class="dispute">
#   > quotation                     <blockquote>, its text not wrapped in a paragraph; consecutive quoted paragraphs,
#                                   which Markdown joins into one quotation, are one <blockquote> each
#   a pipe table                    <div class="tbl"><table>
#   1. question, then indented paragraphs, the first opening "Answer:" or "Model answer:"
#                                   a Self-test item: the question, then the answer in a closed <details> whose summary
#                                   is that label; a list of such items is <ol class="quiz">
#   the numbered list under ## Carry forward           <ol class="carry">
#   ```tree … ```                   <pre class="tree">, the drawing kept character for character (indented under a list
#                                   item, it belongs to that item)
#   ```viz … ```                    the figure, drawn by viz.py ("caption" holds the caption, inline HTML as in Brand + AI)
# History lists are tight: an item's paragraphs are not wrapped in <p> (an indented block keeps the item together in the
# source and is joined back into it). <sup> and <sub>, which Markdown has no form for, stay inline as written.
HIST_ANSWER = re.compile(r'^<p>(Answer|Model answer):\s*', re.S)
HIST_TREE = re.compile(r'^( *)```tree\n(.*?)\n\1```[ \t]*$', re.S | re.M)


def _declare(src):
    """```viz fences as the history figure declarations check.py reads (draw=False): each block's JSON, its caption
    moved into the figcaption."""
    figs = {}
    def sub(m):
        d = json.loads(m.group(1))
        cap = d.pop('caption', '') or ''
        tok = f'VIZFIG{len(figs)}VIZ'
        figs[tok] = (f'<figure class="viz" data-viz="{H.escape(str(d.get("kind", "")))}"><script type="application/json">'
                     f'{json.dumps(d, ensure_ascii=False)}</script><figcaption>{cap}</figcaption></figure>')
        return f'\n\n{tok}\n\n'
    return viz._FENCE.sub(sub, src), figs


def history_html(src, draw=True):
    """A history report's vault file (front matter, Markdown) to its fragment HTML: figures drawn, or with draw=False
    left as declarations (<figure class="viz" data-viz><script type="application/json">, check.py's form)."""
    src = re.sub(r'\A---\n.*?\n---\n', '', src, flags=re.S)
    src = re.sub(r'\A\s*# .*\n', '', src, count=1)
    src, figs = viz.extract_md(src) if draw else _declare(src)
    trees = {}

    def tree(m):
        ind, body = m.group(1), m.group(2)
        body = '\n'.join(ln[len(ind):] if ln.startswith(ind) else ln for ln in body.split('\n'))
        tok = f'TREEPRE{len(trees)}TREE'
        trees[tok] = f'<pre class="tree">{H.escape(body, quote=False)}</pre>'
        return f'{ind}{tok}'
    src = HIST_TREE.sub(tree, src)
    src = literal_brackets(src)
    body = markdown.markdown(src, extensions=['tables'])
    for tok, h in trees.items():
        body = body.replace(f'<p>{tok}</p>', h).replace(tok, h)
    body = viz.restore_md(body, figs)
    body = re.sub(r'<p>(<strong>Where sources disagree\.</strong>.*?)</p>', r'<aside class="dispute">\1</aside>', body, flags=re.S)
    body = re.sub(r'<blockquote>\s*((?:<p>.*?</p>\s*)+)</blockquote>',
                  lambda m: '\n'.join(f'<blockquote>{p}</blockquote>' for p in re.findall(r'<p>(.*?)</p>', m.group(1), re.S)), body, flags=re.S)

    def lst(m):
        tag, inner = m.group(1), m.group(2)
        quiz = False
        items = []
        for li in re.findall(r'<li>(.*?)</li>', inner, re.S):
            li = li.strip()
            blocks = re.findall(r'<p>.*?</p>|<blockquote>.*?</blockquote>|<pre class="tree">.*?</pre>', li, re.S) if li.startswith('<') else []
            if blocks and len(blocks) > 1 and HIST_ANSWER.match(blocks[1]):
                quiz = True
                lab = HIST_ANSWER.match(blocks[1]).group(1)
                ans = [HIST_ANSWER.sub('<p>', blocks[1], count=1)] + blocks[2:]
                items.append(f'<li>{blocks[0][3:-4]}<details><summary>{lab}</summary>{"".join(ans)}</details></li>')
            elif blocks:
                items.append('<li>' + '\n'.join(b[3:-4] if b.startswith('<p>') else b for b in blocks) + '</li>')
            else:
                items.append(f'<li>{li}</li>')
        cls = ' class="quiz"' if quiz else ''
        return f'<{tag}{cls}>\n' + '\n'.join(items) + f'\n</{tag}>'
    body = re.sub(r'<(ol|ul)>(.*?)</\1>', lst, body, flags=re.S)
    body = re.sub(r'(<h2>Carry forward</h2>\s*)<ol>', r'\1<ol class="carry">', body)
    body = re.sub(r'(<(?:thead|tr)>|</t[hd]>)\n(?=<(?:tr|t[hd]|/tr)\b)', r'\1', body)      # a table row on one line, as written
    body = re.sub(r'</tr>\n</thead>', '</tr></thead>', body)
    body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    return body


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


_URL = re.compile(r'(?:https?://|www\.)[^\s<>"]+')


def url_breaks(h):
    """P72 (1 Nov 2026): in the text of an html fragment (never inside a tag), a URL written out in full gets break
    points: after each slash and before each dot, so on a phone it wraps there rather than at an arbitrary letter."""
    def brk(m):
        u = m.group(0)
        return re.sub(r'(?<=/)(?=[^/])', '<wbr>', re.sub(r'(?<=[^.])\.(?=[^.\s])', '<wbr>.', u))
    return re.sub(r'>([^<]+)<', lambda m: '>' + _URL.sub(brk, m.group(1)) + '<', f'>{h}<')[1:-1]


_TAG = re.compile(r'<(/?)([a-zA-Z][\w-]*)\b[^>]*?(/?)>', re.S)
_VOID = {'br', 'img', 'wbr', 'hr', 'input', 'meta', 'link', 'source', 'col', 'area', 'base', 'embed', 'track'}


def top_paras(x):
    """P94: the words of each top-level <p> of a section's own text (x: the html between its band and its next and
    previous), in order, by section_text's rule (the tags taken out, the rest split at white space); a paragraph inside
    anything else (a list, a table, a figure, a quote, a box) is not one, and an empty one is left out."""
    out, depth, start = [], 0, None
    for m in _TAG.finditer(x):
        close, tag, selfc = m.group(1), m.group(2).lower(), m.group(3)
        if tag in _VOID or selfc:
            continue
        if not close:
            if depth == 0 and tag == 'p':
                start = m.end()
            depth += 1
        else:
            depth -= 1
            if depth == 0 and tag == 'p' and start is not None:
                n = len(re.sub(r'<[^>]+>', ' ', x[start:m.start()]).split())
                if n:
                    out.append(n)
                start = None
    return out


def reading(pid, body, scope, sources, made, nsrc=None, chev='', note=False, sep=None):
    """The reading layout for one page. body: the unit's HTML with ids on its h2s and the process sections already
    taken out; scope: the one-line scope (html, may be empty); sources: the Sources list (html, may be empty);
    made: [(heading, html, id or None)] for "How this unit was made". Returns (the scope line for the header, the
    sticky bar and the stepped text, which follow the header, and the two accordions).
    P73 (1 Nov 2026; Pedro: "put the method text at the end like the sources, collapsed in its own section"): with
    note, the text a unit puts before its first h2 leaves section 1 and becomes a third closed accordion after the
    text, "The writer's opening note" (id <pid>-note), between Sources and "How this unit was made". The words are the
    unit's own, unchanged; only where they are read moves."""
    pre, secs = sections(body)
    opening = ''
    if note and secs and re.sub(r'<[^>]+>|\s', '', pre):
        opening, pre = pre, ''
    if not secs:                                  # a page with no h2 is one section
        secs, pre = [(f'{pid}-0', '', pre)], ''
    n = len(secs)
    items, steps = [], []
    for k, (sid, head, html_) in enumerate(secs):
        b, kick, title = band(sid, head, k) if head else ('', '', 'The unit')
        items.append((sid, kick, title))
    # P94: each section with a paragraph ends on its separator (sep: {'block': build.py's sep_block bound to the course's
    # tone, given the section's paragraphs' words, its phase and its name; 'phases': build.py's phases}), each at its own
    # point of the cycle over the page's separators; a section with no top-level paragraph has none
    paras = [top_paras((pre if k == 0 else '') + html_) for k, (_, _, html_) in enumerate(secs)] if sep else [[] for _ in secs]
    ph = iter(sep['phases'](sum(1 for p in paras if p))) if sep else None
    for k, (sid, head, html_) in enumerate(secs):
        b = band(sid, head, k)[0] if head else ''
        nav = ''
        if k > 0:
            nav += f'<a class="sprev" href="#{items[k - 1][0]}" data-step="{k - 1}"><span>Previous · {k} of {n}</span><b>{e(plain(items[k - 1][2]))}</b></a>'
        if k < n - 1:
            nav += f'<a class="snext" href="#{items[k + 1][0]}" data-step="{k + 1}"><span>Next · {k + 2} of {n}</span><b>{e(plain(items[k + 1][2]))}</b></a>'
        else:
            nav += f'<a class="snext send" href="#{pid}-sources" data-acc><span>End of the unit</span><b>Sources and how it was made</b></a>'
        topo = sep['block'](paras[k], next(ph), sid) if paras[k] else ''
        steps.append(f'<section class="sec" data-step="{k}">{pre if k == 0 else ""}{b}{html_}{topo}<nav class="secnav" aria-label="Sections">{nav}</nav></section>')
    menu = ''.join(f'<li><a href="#{sid}" data-step="{k}"><span class="n">{k + 1:02d}</span><span class="t">{(e(plain(kick)) + " · ") if kick else ""}{e(plain(t))}</span></a></li>'
                   for k, (sid, kick, t) in enumerate(items))
    bar = (f'<div class="stepbar" data-n="{n}"><details class="secmenu"><summary><span class="sh"><span class="sof">Section <b>1</b> of {n}</span>'
           f'<span class="stt">{e(plain(items[0][2]))}</span></span>{chev}</summary><ol class="seclist">{menu}</ol>'
           f'<div class="secx"><a href="#{pid}-sources" data-acc>Sources</a>'
           + (f'<a href="#{pid}-note" data-acc>The writer\'s opening note</a>' if opening else '')
           + f'<a href="#{pid}-made" data-acc>How this unit was made</a>'
           f'<button class="whole" type="button" aria-pressed="false">Whole unit</button></div></details><div class="sprog" aria-hidden="true"><i></i></div></div>')
    head = f'<p class="scope">{scope}</p>' if scope else ''
    cnt = f'<span class="an">{nsrc}</span>' if nsrc else ''
    src = (f'<details class="acc src" id="{pid}-sources"><summary><span class="at">Sources</span>{cnt}</summary><div class="accb">{url_breaks(sources) if sources else "<p>No source list on file for this page.</p>"}</div></details>')
    opn = (f'<details class="acc note" id="{pid}-note"><summary><span class="at">The writer\'s opening note</span></summary>'
           f'<div class="accb">{opening}</div></details>') if opening else ''
    mk = ''.join((f'<h3 id="{i}">' if i else '<h3>') + f'{h}</h3>{x}' for h, x, i in made if x)
    howm = (f'<details class="acc made" id="{pid}-made"><summary><span class="at">How this unit was made</span>'
            f'<span class="an">{len([1 for _, x, _ in made if x])} parts</span></summary><div class="accb">{mk}</div></details>')
    return head, bar + f'<div class="report steps">{"".join(steps)}</div>', f'<div class="process">{src}{opn}{howm}</div>'


def aims_text(d, code):
    """S-1 (3 Nov 2026): the unit's aim and dependency lines from the course data's AIMS, or '' where a course has none."""
    a = getattr(d, 'AIMS', {}).get(code)
    return f'Aim: {a[0]}\nTakes: {a[1]}.\nGives: {a[2]}.' if a else ''


def aims_html(d, code):
    a = getattr(d, 'AIMS', {}).get(code)
    return (f'<p class="why"><b>Aim</b> {e(a[0])}</p><p class="why"><b>Takes</b> {e(a[1])}. <b>Gives</b> {e(a[2])}.</p>') if a else ''


def open_brief(d, sc, u):
    """The copyable brief of an unwritten unit: PRE with the course goal, the aim lines where the course has them, the unit's brief.
    Built here and nowhere else; a chat that stages a writer's brief calls this (S-1)."""
    lines = aims_text(d, u[0])
    return d.PRE.replace('{GOAL}', sc['goal']) + '\n\n' + (lines + '\n\n' if lines else '') + u[4]


def brief_box(text, label='Copy brief'):
    return f'<div class="pbox"><pre>{e(text)}</pre><div class="pbar"><button class="copy" type="button">{label}</button></div></div>'


def section_text(x):
    """P93: a reading page's section as its text: without its next and previous buttons (nav.secnav) and its band's
    numeral (span.bn, aria-hidden), which are the page's, not the unit's words."""
    return re.sub(r'<span class="bn"[^>]*>.*?</span>', ' ', re.sub(r'<nav class="secnav".*?</nav>', ' ', x, flags=re.S), flags=re.S)


def build(m, crumbs, theme, pill_next, chev, kit):
    """Panels and the drawer nav for one markdown Academy course. m is a course dict from build.py:md_courses
    (parent = the data file's course with .hub = the module). kit (P93): build.py's tile, patch, hero layer, word count,
    hours, phases and tones, so a markdown course's home draws its tiles and topography as every other page does.
    Sets m['secw'] (each written unit's section words, in order) and m['wby'] (its words, their sum). Returns (panels
    list, nav html, bibliography size)."""
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
        made = [('Provenance', f'<p>{r["intro"]}</p>', None)] + unsure + fresh + ([('The brief', brief_box((aims_text(d, code) + '\n\n' + u[4]) if aims_text(d, code) else u[4]), None)] if u else [])
        head, steps, end = reading(r['id'], pre + ''.join(text), e(u[2]) if u else '', src, made, src.count('<li>'), chev, note=True,
                                   sep=kit['sep'](kit['tone'].get(col, 4)))   # P94: each section's separator, in the course's tone
        if code:   # P93: each section's own words (its text, not its next and previous buttons or its band's numeral)
            m.setdefault('secw', {})[code] = [kit['wc'](section_text(x)) for x in re.findall(r'<section class="sec" data-step="\d+">(.*?)</section>(?=<section class="sec"|</div>$)', steps.split('<div class="report steps">', 1)[1] + '', re.S)]
            m.setdefault('wby', {})[code] = sum(m['secw'][code])
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

    # ---- course home (P93: after the reading pages, whose sections give each unit's words) --------------------
    # each unit a tile (Pedro: "make this new tile style propagate across the site"): the chip (the course and the
    # unit) with its status pill, the title, its scope in two lines, three stats (sections, words, hours of reading)
    # and its patch (its sections as rises by their words; a unit not yet written one flat ring), the whole tile the
    # link to its reading page (a unit not yet written: to its brief); the hero's topography, one rise per unit
    pt = lambda col: kit['tone'].get(col, 4)
    ph = kit['phases'](1 + len(sc['units']))
    hero_rises = [(code, m['wby'].get(code)) for code, *_ in sc['units']]
    top = max((w for _, w in hero_rises if w), default=0)
    layer = kit['hero'](hero_rises, pt(col), top / 5.5, kit['topo'], ph[0]) if top else ''
    tiles = ''
    for k, (code, title, scope, *_) in enumerate(sc['units']):
        if code in read_of:
            sw = m['secw'][code]
            tiles += kit['tile']([m['short'], code], col, title, e(scope), stats=[(len(sw), 'sections'), (f'{sum(sw):,}', 'words'), (kit['hours'](sum(sw)), 'h of reading')],
                                 pill=kit['pill']('written'), patch=kit['patch']([(f'{code} §{j + 1}', w) for j, w in enumerate(sw)], pt(col), ph[k + 1]),
                                 href='#' + read_of[code]['id'])
        else:
            tiles += kit['tile']([m['short'], code], col, title, e(scope), stats=[(0, 'sections'), (0, 'words'), (kit['hours'](0), 'h of reading')],
                                 pill=pill_next if code == d.NEXT_UNIT else '<span class="pill">soon</span>',
                                 patch=kit['patch']([(code, None)], pt(col), ph[k + 1]), href=f'#{BP}{code.lower()}', cls=' pending')
    pct = round(100 * m['nwritten'] / m['nunits'])
    audits = ''.join(f'<li><strong>{e(dt)}</strong> · {txt}</li>' for dt, txt in d.AUDIT_LOG)
    start = (f'<a class="hbtn start" href="#{read_of[first[0]]["id"]}" data-target="{read_of[first[0]]["id"]}"><span>Start the course</span><b>{e(first[0] + " " + first[1])}</b></a>' if first
             else f'<a class="hbtn start" href="#{BR}" data-target="{BR}"><span>Open the course</span><b>No unit written yet · the briefs</b></a>')
    frame = getattr(d, 'FRAME', '') if sc is courses[0] else ''      # the frame is shown on the data file's first course
    P.insert(0, panel(ctx, 'course', f'''
  <header class="hero has-topo">
    {layer}
    {crumbs(('Academy', 'home'), (t['name'], 'track-' + m['theme']), (course_crumb[0], None))}
    {eyebrow((f'COURSE {key}', col), (c['short'], None), (('COMPLETE', 'var(--teal)') if m['status'] == 'available' else (m['status'].upper(), 'var(--gold)')))}
    <h1>{e(m['name'])}</h1>
    <p class="lede">{sc['intro']}</p>
    <div class="stats" data-n="4"><div><b>{m['nwritten']}</b><span>of {m['nunits']} units written</span></div><div><b>{pct}%</b><span>of the course</span></div><div><b>{len(d.AUDIT_LOG)}</b><span>audit{'s' if len(d.AUDIT_LOG) != 1 else ''} run</span></div><div><b>{e(d.NEXT_UNIT)}</b><span>next unit to write</span></div></div>
    <div class="hlinks"><a class="hbtn cont" href="#{ctx}" data-course="{ctx}" hidden><span>Continue</span><b></b></a>{start}<a class="hbtn alt" href="#{BR}" data-target="{BR}"><span>Briefs</span><b>Every unit's brief, copyable</b></a></div>
  </header>
  <section class="howto edge" style="--hc:var(--blue)"><h2>What you will be able to do</h2><p>{e(sc['goal'][0].upper() + sc['goal'][1:])}</p><ul>{sc['outcomes']}</ul><p class="over">{d.COURSE_NOTE}</p></section>
  <h2 class="hsec">Units, in writing order</h2>
  <div class="cgrid">{tiles}</div>
  <details class="howto rules"><summary><h2>Audits run</h2><span>{len(d.AUDIT_LOG)} · next {e(d.NEXT_AUDIT)}</span></summary><ul>{audits}</ul></details>
  {frame}
  <a class="hbtn alt wide" href="#{ctx}-build" data-target="{ctx}-build"><span>How it is built</span><b>Method, build order, briefs, audits, sources, changelog.</b></a>
  <a class="hbtn alt wide" href="#{ctx}-built" data-target="{ctx}-built"><span>How it was built</span><b>The model behind each unit, every check and audit with its verdict, the flags still open.</b></a>
  <a class="hbtn alt wide" href="#home" data-target="home"><span>Academy</span><b>Back to every course.</b></a>''', t=m['short'], u=f'COURSE {key}', cls='home', split='home'))   # P93: fetched, as a history course home is (P22), so its tiles and topography never weigh on the shell


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
        full = brief if is_done else open_brief(d, sc, u)
        read = f'<a class="rlink" href="#{read_of[code]["id"]}" data-target="{read_of[code]["id"]}">Read the unit →</a>' if code in read_of else ''
        cards += (f'<article class="smod{" deep" if deep else ""}" id="{BP}{code.lower()}" style="--c:{ucol}"><div class="smod-top"><span class="code">{code}</span><h3>{e(title)}</h3>{pill}</div>'
                  f'<p class="why">{e(scope)}</p>{aims_html(d, code)}<p class="ships"><b>Ships</b>{e(ships)}</p>{read}'
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
