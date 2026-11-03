"""One EPUB 3 of an edition (P71 (2), 1 Nov 2026): `python3 build.py --epub <edition>` builds the edition (P70) and then
writes `editions/<edition>.epub` from the same sources, so the same files can be read as an ebook.

What goes in, per course of the edition, in syllabus or build order:
  history course    each written report: its vault file (courses/<course>/<id>-<slug>.md, P71-3), every ```viz block drawn to SVG
                    by viz.py, then its Sources (the curated bibliography/<course>/r-<id>.md, as the site's Sources)
  markdown course   each filed unit from its vault: the text from the first heading on, every ```viz block drawn by
                    viz.py; its own ## Sources section ends it
Left out: everything about how a unit was made ("How this unit was made", the writer's opening note, the prompt, the
checks), the site's navigation and the Academy pages that are process (the edition's `omit`).

Styling: nothing is styled by hand. The book's stylesheet is cut from design/theme.css (the rules a report's text and
figures use, the light palette's tokens written in), and each figure's SVG carries the styles the theme gives it,
read from a browser that renders it with the theme (light), so a figure draws the same in a reader that has no CSS
variables. The theme's fonts (kit/fonts, SIL OFL) are embedded.
"""
import re, html, json, uuid, zipfile, pathlib, datetime, shutil
import markdown
import viz
import vault

R = pathlib.Path(__file__).resolve().parent
THEME = R.parent / 'design' / 'theme.css'

# the theme rules a report's text and figures use, and the properties a reading system honours
KEEP_SEL = re.compile(r'^(\.report (h2|h3|p|ul|ol|li|blockquote|strong|table|th|td|tr:last-child td)|\.tbl|pre\.tree|\.dispute( strong| p)?|\.quiz li|\.mono|\.viz|\.viz figcaption|\.viz-title)$')
KEEP_PROP = {'font-size', 'font-weight', 'font-style', 'font-family', 'margin', 'padding', 'padding-left', 'border', 'border-left',
             'border-top', 'border-bottom', 'border-collapse', 'color', 'background', 'line-height', 'letter-spacing',
             'text-transform', 'text-align', 'vertical-align', 'width', 'font-variant-numeric'}


def tokens():
    """The light palette's tokens from theme.css (:root[data-theme="light"] over :root), with var() resolved."""
    css = THEME.read_text()
    tok = {}
    for block in (re.search(r'^:root\{(.*?)\}', css, re.S | re.M).group(1), re.search(r':root\[data-theme="light"\]\{(.*?)\}', css, re.S).group(1)):
        for k, v in re.findall(r'(--[\w-]+):([^;]+);', block):
            tok[k] = v.strip()
    for k, v in re.findall(r'(--viz-\d):([^;}]+)', css):
        tok[k] = v.strip()
    def res(v, depth=0):
        return re.sub(r'var\((--[\w-]+)\)', lambda m: res(tok.get(m.group(1), ''), depth + 1) if depth < 6 else '', v)
    return {k: res(v) for k, v in tok.items()}


def stylesheet():
    css, tok = THEME.read_text(), tokens()
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'@media[^{]*\{([^{}]*\{[^{}]*\})*\s*\}', '', css)   # media blocks are the site's layout, not the text's
    out = [f'body{{font-family:{tok["--sans"]};color:{tok["--fg"]};background:{tok["--bg"]};line-height:1.6;margin:0 4%}}',
           f'h1{{font-size:1.6em;line-height:1.25;margin:0 0 .3em}}',
           f'.scope{{color:{tok["--muted"]};margin:0 0 1.5em}}',
           f'.eyebrow{{font-family:{tok["--mono"]};font-size:.75em;letter-spacing:.06em;text-transform:uppercase;color:{tok["--muted"]}}}',
           f'a{{color:{tok["--teal"]}}}',
           f'.viz svg{{max-width:100%;height:auto}}']
    for sels, body in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        keep = [s.strip() for s in sels.split(',') if KEEP_SEL.match(s.strip())]
        if not keep:
            continue
        decl = []
        for d in body.split(';'):
            if ':' not in d:
                continue
            k, v = [x.strip() for x in d.split(':', 1)]
            if k in KEEP_PROP and 'color-mix' not in v:
                v = re.sub(r'var\((--[\w-]+)\)', lambda m: tok.get(m.group(1), m.group(0)), v)
                if 'var(' not in v:
                    decl.append(f'{k}:{v}')
        if decl:
            out.append(f'{",".join(keep)}{{{";".join(decl)}}}')
    return '\n'.join(out) + '\n' + fontfaces()


def fontfaces():
    """@font-face rules for the embedded theme fonts, read from kit/fonts/fonts.css (the same files verify.py serves)."""
    src = (R / 'fonts' / 'fonts.css').read_text()
    return re.sub(r'url\(https://fonts\.gstatic\.com/learning-vendored/([^)]+)\)', r'url(fonts/\1)', re.sub(r'/\*.*?\*/', '', src, flags=re.S))


SVG_PROPS = ['fill', 'stroke', 'stroke-width', 'stroke-dasharray', 'stroke-linejoin', 'stroke-linecap', 'opacity', 'font-family',
             'font-size', 'font-weight', 'font-style', 'letter-spacing', 'text-transform', 'font-variant-ligatures']
INLINE_JS = r'''(props) => {
  document.querySelectorAll('figure.viz').forEach((f, k) => {
    const svg = f.querySelector('svg'); if (!svg) return;
    f.querySelectorAll('.viz-stick, svg.viz-alt').forEach(e => e.remove());   // P83: the phone-only label column and phone drawing have no place in a reader
    const mk = svg.querySelector('marker'); let mid = null;
    if (mk) { mid = 'vizhead-' + f.dataset.fig; }
    svg.querySelectorAll('*').forEach(el => {
      if (el.closest('defs') && el.tagName !== 'path') return;
      const cs = getComputedStyle(el), st = [];
      props.forEach(p => { const v = cs.getPropertyValue(p); if (v && v !== 'normal' && v !== 'none' || (p === 'fill' || p === 'stroke') && v === 'none') st.push(p + ':' + v); });
      const me = cs.getPropertyValue('marker-end');
      if (me && me !== 'none' && mid) el.setAttribute('marker-end', 'url(#' + mid + ')');
      el.removeAttribute('class'); el.setAttribute('style', st.join(';'));
    });
    if (mk) mk.setAttribute('id', mid);
    svg.removeAttribute('data-x0'); svg.setAttribute('style', 'font-family:' + getComputedStyle(svg).fontFamily);
  });
  return [...document.querySelectorAll('section.chapter')].map(s => new XMLSerializer().serializeToString(s));
}'''


def chapters(courses, md_units):
    """[(file stem, nav label, course label, unit label, inner html)] in reading order."""
    out = []
    for c in courses:
        for u, name, why, mods in c['units']:
            for mid, title, w in mods:
                if mid not in c['index']:
                    continue
                frag = vault.report_html(c, mid)     # P71-3: the report's Markdown in the vault, figures drawn
                frag = re.sub(r'<(/?)(html|head|body|!doctype[^>]*)>', '', frag, flags=re.I)
                frag = re.sub(r'<style.*?</style>|<script.*?</script>', '', frag, flags=re.S | re.I)
                frag = re.sub(r'\sstyle="[^"]*"', '', frag)
                frag = re.sub(r'<a\b[^>]*href="#[^"]*"[^>]*>(.*?)</a>', r'\1', frag, flags=re.S)   # no link into the site
                bib = R / 'bibliography' / c['id'] / f'r-{mid}.md'
                src = ''
                if bib.exists():
                    bt = re.sub(r'\A# .*\n', '', bib.read_text(encoding='utf-8'))
                    src = markdown.markdown(bt).replace('<h2>', '<h3>').replace('</h2>', '</h3>')
                src = f'<section class="sources"><h2>Sources</h2>{src or "<p>No source list on file for this report.</p>"}</section>'
                head = (f'<p class="eyebrow">{html.escape(c["short"])} · Unit {u} · {html.escape(name)}</p>'
                        f'<h1>{mid} · {html.escape(c["index"][mid]["title"])}</h1>'
                        + (f'<p class="scope">{html.escape(w)}</p>' if w else ''))
                out.append((f'{c["id"]}-{mid.replace(".", "-")}', f'{mid} {c["index"][mid]["title"]}', c['short'], f'Unit {u} · {name}',
                            f'{head}<div class="report">{frag}</div>{src}'))
    for m, code, title, path in md_units:
        text = path.read_text(encoding='utf-8')
        text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
        text = text[text.find('\n## ') + 1:] if '\n## ' in text else text   # the opening note before the first heading is process
        text, figs = viz.extract_md(text)
        body = viz.restore_md(markdown.markdown(text, extensions=['tables', 'fenced_code']), figs)
        body = re.sub(r'<a\b[^>]*href="#[^"]*"[^>]*>(.*?)</a>', r'\1', body, flags=re.S)
        out.append((f'{m["id"]}-{code.lower()}', f'{code} {title}', m['short'], m['short'],
                    f'<p class="eyebrow">{html.escape(m["short"])} · {html.escape(code)}</p><h1>{html.escape(title)}</h1><div class="report">{body}</div>'))
    return out


def serialise(chs, css):
    """Each chapter as XHTML (XMLSerializer), its figures carrying their computed styles, read in Chromium."""
    from playwright.sync_api import sync_playwright
    body = ''.join(f'<section class="chapter" data-k="{k}">{h}</section>' for k, (_, _, _, _, h) in enumerate(chs))
    fig = [0]
    def tag(m):
        fig[0] += 1
        return m.group(0).replace('<figure ', f'<figure data-fig="{fig[0]}" ', 1)
    body = re.sub(r'<figure class="viz[^"]*"', tag, body)
    page = f'<!doctype html><html data-theme="light"><head><meta charset="utf-8"><style>{(R / "shell.css").read_text()}</style></head><body>{body}</body></html>'
    tmp = R / 'editions' / '_epub.html'
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(page)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(200)
        xs = pg.evaluate(INLINE_JS, SVG_PROPS)
        br.close()
    tmp.unlink()
    out = []
    for x in xs:
        x = re.sub(r'^<section[^>]*>|</section>$', '', x)
        x = re.sub(r' data-(fig|k)="\d+"', '', x)
        x = x.replace(' xmlns="http://www.w3.org/1999/xhtml"', '')
        out.append(x)
    return out


def write(name, ed, courses, md_units):
    chs = chapters(courses, md_units)
    css = stylesheet()
    xs = serialise(chs, css)
    path = R / 'editions' / f'{name}.epub'
    uid = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, f'https://apcanario.github.io/academy/#{name}'))
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    title = ed['title']
    fonts = sorted(f.name for f in (R / 'fonts').glob('*.woff2'))
    def xhtml(t, body, nav=False):
        return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
                f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en-GB" lang="en-GB">'
                f'<head><meta charset="utf-8"/><title>{html.escape(t)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>'
                f'<body>{body}</body></html>\n')
    # nav: course, then unit, then report
    tree, last = [], (None, None)
    for (stem, label, course, unit, _) in chs:
        if not tree or tree[-1][0] != course:
            tree.append((course, []))
        units = tree[-1][1]
        if not units or units[-1][0] != unit:
            units.append((unit, []))
        units[-1][1].append((stem, label))
    nav_ol = '<ol>' + ''.join(
        f'<li><span>{html.escape(cn)}</span><ol>' + ''.join(
            f'<li><a href="{us[0][0]}.xhtml">{html.escape(un)}</a><ol>' + ''.join(f'<li><a href="{s}.xhtml">{html.escape(l)}</a></li>' for s, l in us) + '</ol></li>'
            for un, us in units) + '</ol></li>' for cn, units in tree) + '</ol>'
    nav = xhtml('Contents', f'<nav epub:type="toc" id="toc"><h1>Contents</h1>{nav_ol}</nav>')
    words = sum(len(re.sub(r'<[^>]+>', ' ', h).split()) for *_, h in chs)
    cover = xhtml(title, f'<p class="eyebrow">Academy · edition</p><h1>{html.escape(title)}</h1>'
                         f'<p class="scope">{len(chs)} reports, {words:,} words. Each report ends with its sources. Built {now[:10]} from the course files by kit/epub.py.</p>')
    items = [('cover', 'cover.xhtml', 'application/xhtml+xml', ''), ('nav', 'nav.xhtml', 'application/xhtml+xml', ' properties="nav"'),
             ('css', 'style.css', 'text/css', '')]
    items += [(f'c{k}', f'{stem}.xhtml', 'application/xhtml+xml', ' properties="svg"' if '<svg' in xs[k] else '') for k, (stem, *_) in enumerate(chs)]
    items += [(f'f{k}', f'fonts/{f}', 'font/woff2', '') for k, f in enumerate(fonts)]
    opf = ('<?xml version="1.0" encoding="utf-8"?>\n<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="en-GB">'
           f'<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="uid">{uid}</dc:identifier><dc:title>{html.escape(title)}</dc:title>'
           f'<dc:language>en-GB</dc:language><dc:creator>Academy</dc:creator><meta property="dcterms:modified">{now}</meta></metadata>'
           '<manifest>' + ''.join(f'<item id="{i}" href="{h}" media-type="{t}"{p}/>' for i, h, t, p in items) + '</manifest>'
           '<spine><itemref idref="cover"/><itemref idref="nav"/>' + ''.join(f'<itemref idref="c{k}"/>' for k in range(len(chs))) + '</spine></package>\n')
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w') as z:
        z.writestr(zipfile.ZipInfo('mimetype'), 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml', '<?xml version="1.0" encoding="utf-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>\n', compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/content.opf', opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/nav.xhtml', nav, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/cover.xhtml', cover, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/style.css', css, compress_type=zipfile.ZIP_DEFLATED)
        for k, (stem, label, *_rest) in enumerate(chs):
            z.writestr(f'OEBPS/{stem}.xhtml', xhtml(label, xs[k]), compress_type=zipfile.ZIP_DEFLATED)
        for f in fonts:
            z.write(R / 'fonts' / f, f'OEBPS/fonts/{f}', compress_type=zipfile.ZIP_STORED)
    print(f'epub {name}: {path.relative_to(R)}, {len(chs)} chapters, {words:,} words, {sum(x.count("<svg") for x in xs)} figures, {path.stat().st_size / 1024 / 1024:.2f} MB')
    return path
