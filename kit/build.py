"""Assemble the Academy site in academy/ from the course data kit/courses.py loads: academy/index.html, the shell (home,
drawer, course homes, build pages, changelog, backlog), and one file per report, fetched by the shell on navigation
(docs/academy.md A2): academy/<course>/r-<id>.html for a history report, academy/<course>/<reading id>.html for a
markdown course's reading page. Since P20 each syllabus (academy/<course>/syllabus.html) and a markdown course's briefs
and bibliography pages (academy/<course>/briefs.html, bibliography.html) are fetched the same way. The size table in
README.md is regenerated on every build.

The root home is Academy (docs/academy.md, A1): every course of both families. History courses (Greece, Rome) are
built from their kit folders; a markdown course (Brand + AI) is built by mdcourse.py from its data file
(kit/pack.py: courses/<slug>/course.toml [pack], briefs.md, pages/; AD5, S-DEC2) into one Academy course per course in that file (AD6, A3): a course home, a
reading page per written unit, and the "How it is built" pages (method, build order, briefs, bibliography,
changelog). The site also renders the Project's backlog and chat changelog (docs/) as a Backlog page.

Each course has a syllabus file, its reports in the vault (courses/<course>/, Markdown since P71-3; vault.py), a prompts index (the modules with a written report),
a colour and a short name. Greece keeps its original panel ids (#greece, #syllabus, #m23); later courses
are namespaced (#rome, #rome-syllabus, #rm01).
"""
import json, re, html, pathlib, importlib.util, math
import markdown
from courses import COURSES, HISTORY, MARKDOWN, THEMES, EDITIONS, HERO_AT as _HERO_AT, LOG_AREAS, DEFAULT_EDITION, brand, path as cpath, provenance, sub_page_id
import sys
# P70: an edition filters the course list here, before anything renders; the full site is the default edition (the first
# in catalog.toml `edition_order`)
EDITION = sys.argv[sys.argv.index('--edition') + 1] if '--edition' in sys.argv else DEFAULT_EDITION
if '--epub' in sys.argv:   # P71 (2): `--epub <edition>` builds that edition, then its EPUB (epub.py)
    EDITION = sys.argv[sys.argv.index('--epub') + 1]
if EDITION not in EDITIONS:
    raise SystemExit(f'no edition {EDITION!r} in courses.py EDITIONS: {", ".join(EDITIONS)}')
ED = EDITIONS[EDITION]
B = brand(EDITION)   # S-DEC3: the edition's brand (brands/<name>.toml): every site string, the rules lines, keys, tokens, fonts
SITE_NAME = B['name']
OMIT = set(ED['omit'])
if ED['courses'] is not None:
    COURSES = [c for c in COURSES if c['id'] in ED['courses']]
    HISTORY = [c for c in HISTORY if c['id'] in ED['courses']]
    MARKDOWN = [c for c in MARKDOWN if c['id'] in ED['courses']]
    _tracks = {c['theme'] for c in HISTORY} | {tr for c in MARKDOWN for tr, _ in c['tracks'].values()}
    THEMES = [t for t in THEMES if t['id'] in _tracks]
import mdcourse
import pack
import vault
import howbuilt
import viz
import viz_examples
viz.set_metrics(B)   # P-DEC5: figure text is sized with the brand's --sans and --mono faces (DM Sans, Space Mono by default)
mdcourse.SITE_NAME = howbuilt.SITE_NAME = viz_examples.SITE_NAME = SITE_NAME   # S-DEC3
howbuilt.GH = B['repo']   # S-DEC3: the brand's repo link base, not the clone's remote
howbuilt.HB = B.get('howbuilt', {})   # S-DEC5: the brand's method and sourcing docs for the How it was built pages

R = pathlib.Path(__file__).resolve().parent
PROV = provenance()   # S-DEC5: kit/provenance.json with each history course's own part (courses.py)
ICON_CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>'


FIGBLOCK = re.compile(r'<figure class="viz[ "].*?</figure>', re.S)



def eyebrow_segs(*parts):
    """P72 (1 Nov 2026): an eyebrow line as segments that wrap whole (theme 4a .seg): a segment moves to the next line
    rather than breaking inside ("2,796 / WORDS", "UNIT / 5"), and the dot after it stays on its line."""
    segs = [f'<span class="seg">{p}&nbsp;·</span>' for p in parts[:-1]] + [f'<span class="seg">{parts[-1]}</span>']
    return ' '.join(segs)

def wc(frag):
    """Words in a report's body (before the Self-test). Figure blocks, declared or drawn, are left out (P41): adding a
    figure never changes a report's word count."""
    body = re.split(r'<h2>\s*Self-test', FIGBLOCK.sub(' ', frag))[0]
    return len(re.sub(r'<[^>]+>', ' ', body).split())


def unchecked(model):
    """A report registered before its fresh check ran carries '(unchecked)' in its provenance and an 'unchecked' pill on the site."""
    return 'unchecked' in model


PILL_UNCK = '<span class="pill unck" title="Written, not yet checked by a fresh reviewer">unchecked</span>'
PILL_NEXT = '<span class="pill next" title="Queued for the next writing session">next</span>'


def flagged(model):
    """Anything whose provenance does not mention Fable 5.1 (written with it, or reviewed with it) is flagged for Fable review."""
    return 'Fable 5.1' not in model


def start_btn(c):
    """The course home's Start button: the first written report, or the syllabus while nothing is written (a new course)."""
    if c['first'] is None:
        return f'<a class="hbtn start" href="#{c["syl_id"]}" data-target="{c["syl_id"]}"><span>Start the course</span><b>Nothing written yet: the syllabus</b></a>'
    f = c['first']
    return f'<a class="hbtn start" href="#{c["slug"](f)}" data-target="{c["slug"](f)}"><span>Start the course</span><b>{f} {html.escape(c["index"][f]["title"])}</b></a>'


def yr(y):
    return f'{-y} BC' if y < 0 else f'AD {y}'


# P68: the review folders and audits a report's "How this unit was made" lists (read as howbuilt.py reads them)
REVIEW_FOLDERS = howbuilt._review_folders()
AUDITS = {}
for _c in HISTORY:
    for _a in howbuilt._audits(_c['id']):
        for _i in _a['reports']:
            AUDITS.setdefault(_c['id'], {}).setdefault(_i, []).append(_a)
    AUDITS.setdefault(_c['id'], {})


def load(c):
    """Parse a course's syllabus and prompts index; build its report panels."""
    syl = cpath(c, 'syllabus').read_text()
    units = []
    for m in re.finditer(r'<section class="unit" id="u(\d+)"[^>]*>.*?<h2>(.*?)</h2>.*?<p class="unit-why">(.*?)</p>(.*?)</section>', syl, re.S):
        u, name, why, body = m.groups()
        mods = [(a, html.unescape(t), html.unescape(w)) for a, t, w in re.findall(r'data-id="([\d.]+)">.*?<h3>(.*?)</h3>.*?<p class="why">(.*?)</p>', body, re.S)]
        units.append((u, html.unescape(name), html.unescape(why), mods))
    c['units'] = units
    c['umap'] = {u: (n, w, mods) for u, n, w, mods in units}
    c['total_mods'] = sum(len(x[3]) for x in units)
    c['content_mods'] = sum(len(x[3]) for x in units if x[0] != c['audit_unit'])
    c['all_prompts'] = {a: html.unescape(p) for a, p in re.findall(r'data-id="([\d.]+)">.*?<pre>(.*?)</pre>', syl, re.S)}
    intro = re.search(r'<section class="intro">(.*?)</section>', syl, re.S).group(1)
    c['syl_intro'] = re.sub(r'<h2>.*?</h2>', '', intro, count=1, flags=re.S).replace('<span class="tag">copy</span>', '<em>copy prompt</em>')
    order = [m[0] for x in units for m in x[3]]
    idx = json.load(open(cpath(c, 'prompts')))
    c['index'] = {k: idx[k] for k in order if k in idx}
    c['done'] = set(c['index'])
    c['first'] = next(iter(c['index']), None)  # the first written report, where a new reader starts (None in a new course)
    c['prov'] = PROV.get(c['id'], {})
    c['slug'] = lambda i, p=c['prefix']: p + i.replace('.', '')

    panels, total = [], 0
    c['wby'] = {}   # P91: each report's words (P92: for its unit's rise in the course tile's contour patch)
    ucol = c['unit_colors']
    for i, meta in c['index'].items():
        frag = vault.report_html(c, i)   # P71-3: the report's Markdown in the vault, rendered to its fragment, figures drawn
        # strip anything that violates the fragment contract
        frag = re.sub(r'<(/?)(html|head|body|!doctype[^>]*)>', '', frag, flags=re.I)
        frag = re.sub(r'<style.*?</style>|<script.*?</script>', '', frag, flags=re.S | re.I)
        frag = re.sub(r'\sstyle="(?!(?:--stickn?:[0-9.]+px;?)+")[^"]*"', '', frag)   # C1 (15 Nov 2026): a figure frame's --stick/--stickn stays, so a history matrix keeps its label column on a phone
        u = i.split('.')[0]
        n = wc(frag); total += n; c['wby'][i] = n
        sl = c['slug'](i)
        frag_ids = []
        def addid(m):
            t = m.group(1)
            sid = f'{sl}-{len(frag_ids)}'
            frag_ids.append((sid, t))
            return f'<h2 id="{sid}">{t}</h2>'
        frag = re.sub(r'<h2>(.*?)</h2>', addid, frag)
        model = c['prov'].get(i, c['default_model'])
        # P68: the reading layout (mdcourse.reading): the module's syllabus line as the scope, its curated bibliography
        # as Sources, and its provenance, the writer's unsure list, its checks and audits and its prompt as
        # "How this unit was made"
        why = next((w for mid, _, w in c['umap'][u][2] if mid == i), '')
        bib = cpath(c, 'bibliography') / f'r-{i}.md'
        src, nsrc = '', 0
        if bib.exists():
            bt = re.sub(r'\A# .*\n', '', bib.read_text(encoding='utf-8'))
            nsrc = len(re.findall(r'^\s*- ', bt, re.M))
            src = markdown.markdown(mdcourse.list_breaks(bt)).replace('<h2>', '<h3>').replace('</h2>', '</h3>').replace('<a href=', '<a target="_blank" rel="noopener" href=')
        checks = []
        for fo in REVIEW_FOLDERS:
            f = fo['path'] / f'{c["id"]}-{i}.md'
            if f.exists():
                v = re.search(r'^Verdict:\s*(\w+)', f.read_text(encoding='utf-8'), re.M)
                checks.append(f'<li>{html.escape(fo["label"])} ({html.escape(fo["model"])}, {html.escape(fo["date"])}): {html.escape(v.group(1)) if v else "no verdict line"} · {howbuilt.gh(f.relative_to(R.parent).as_posix())}</li>')
        for a in AUDITS[c['id']].get(i, []):
            sc = a['scorecard']
            what = (': ' + ', '.join(x for x in [sc[0], f'mean {sc[1]}' if sc[1] else '', (f'{sc[2]} factual error{"s" if sc[2] != 1 else ""}' if sc[2] is not None else '')] if x)) if sc else ''
            checks.append(f'<li>Audit {html.escape(a["id"])} ({html.escape(a["model"])}, {html.escape(a["date"])}){html.escape(what)} · {howbuilt.gh(a["path"].relative_to(R.parent).as_posix())}</li>')
        unsure = ''.join(markdown.markdown(f.read_text(encoding='utf-8')) for fo in REVIEW_FOLDERS for f in [fo['path'] / f'{c["id"]}-{i}-writer.md'] if f.exists())
        made = [('Provenance', f'<p>Written with {html.escape(model)}.</p>', None), ("Writer's unsure list", unsure, None),
                ('Checks and audits', f'<ul>{"".join(checks)}</ul>' if checks else '', None),
                ('The prompt this answers', mdcourse.brief_box(meta['prompt'], 'Copy prompt'), None)]
        scope, steps, end = mdcourse.reading(sl, frag, html.escape(why), src, made, nsrc, ICON_CHEV,
                                             sep=sep_kit(_TONE[c['color']]))   # P94: each section's separator, in the course's colour (its home's hero's tone)
        panels.append(f'''
<section class="panel" id="{sl}" data-unit="{u}" data-ctx="{c['id']}" data-kind="report" data-split="r-{i}" style="--cc:{c['color']}" hidden>
  <header class="phead">
    {crumbs((SITE_NAME, 'home'), (c['short'], c['home_id']), (f'Unit {u}', f'{c["home_id"]}-u{u}'), (i, None))}
    <div class="eyebrow">{eyebrow_segs(f'<span class="u" style="--c:{c["color"]}">{c["label"]}</span>', f'<span class="u" style="--c:{ucol[u]}">UNIT {u}</span>', c['umap'][u][0], f'<span class="mono">{i}</span>', f'{n:,} words')}{' ' + PILL_UNCK if unchecked(model) else ''}</div>
    <h1>{html.escape(meta['title'])}</h1>
    {scope}
  </header>
  {steps}
  {end}
  <div class="pager"></div>
</section>''')
    c['report_panels'] = panels
    c['nrep'] = len(panels)
    c['words'] = total
    c['units_complete'] = sum(1 for x in units if x[0] != c['audit_unit'] and all(m[0] in c['done'] for m in x[3]))
    c['flag'] = ''   # S-NOAUDIT (15 Nov 2026): the Fable stage is closed, so no report or syllabus is flagged for Fable review
    return c


def fill(s, c):
    return s.format(content_mods=c['content_mods'], total_mods=c['total_mods'], nrep=c['nrep'], kwords=c['words'] // 1000)


def drawer(c):
    out = ''
    for u, name, why, mods in c['units']:
        if u in c['sections']:
            out += f'<div class="dsec">{c["sections"][u]}</div>'
        col = c['unit_colors'][u]; have = sum(1 for m in mods if m[0] in c['done'])
        cnt = f'{have}/{len(mods)}' if have < len(mods) else str(len(mods))
        dkey = c.get('unit_key', '{id}:{unit}').format(id=c['id'], unit=u)   # course.toml `unit_key` (M6, S-DEC4): greece keeps its legacy '{unit}'
        out += f'<div class="dunit closed" data-unit="{dkey}" data-ulabel="{c["label"]} · UNIT {u}" style="--c:{col}"><button class="duh" type="button" aria-expanded="false"><span class="un">UNIT {u}</span><span class="ut">{html.escape(name)}</span><span class="cnt">{cnt}</span>{ICON_CHEV}</button><div class="ditems">'
        for mid, t, w in mods:
            if mid in c['done']:
                pill = PILL_UNCK if unchecked(c['prov'].get(mid, '')) else ''
                out += f'<a class="ditem" href="#{c["slug"](mid)}" data-target="{c["slug"](mid)}"><span class="n">{mid}</span><span class="t">{html.escape(t)}</span>{pill}</a>'
            else:
                pill = PILL_NEXT if mid in c.get('next_up', ()) else '<span class="pill">soon</span>'
                out += f'<div class="dsoon"><span class="n">{mid}</span><span class="t">{html.escape(t)}</span>{pill}</div>'
        out += '</div></div>'
    # S-NAV1 step C: the course's group of the sub-nav (its pages, then its units); the way back to the site is the main
    # nav's (Home and the areas), so the group no longer opens on a link to the home
    top = (f'<div class="dtop"><a class="ditem dhome" href="#{c["home_id"]}" data-target="{c["home_id"]}"><span class="n">⌂</span><span class="t">{c["short"]}: course home</span></a>'
           f'<a class="ditem dhome" href="#{c["syl_id"]}" data-target="{c["syl_id"]}"><span class="n">§</span><span class="t">Syllabus and prompts</span></a>'
           + ('' if 'build' in OMIT else f'<a class="ditem dhome" href="#{c["home_id"]}-built" data-target="{c["home_id"]}-built"><span class="n">✓</span><span class="t">How it was built</span></a>') + '</div>')
    return f'<div class="sub-sec" data-navctx="{c["id"]}" data-accordion role="group" aria-label="{c["short"]} course" hidden>{top}{out}</div>'


def unit_tile(c, u, phase=None):
    """A history unit on its course home (P93: a tile, Pedro "make this new tile style propagate across the site"): the
    chip (the course and the unit) with its status pill, the unit's name, its why in two lines, three stats (modules
    written, in all, hours of reading) and its patch (its modules as rises by their words, one not yet written flat);
    the tile is the summary of a disclosure that opens to the unit's module rows, as the unit card did."""
    name, why, mods = c['umap'][u]; col = c['unit_colors'][u]
    have = [m for m in mods if m[0] in c['done']]
    queued = any(m[0] in c.get('next_up', ()) for m in mods)
    status = 'complete' if len(have) == len(mods) else ('in progress' if have else ('not run yet' if u == c['audit_unit'] else ('next session' if queued else 'coming soon')))
    rows = ''
    for mid, t, w in mods:
        if mid in c['done']:
            pill = PILL_UNCK if unchecked(c['prov'].get(mid, '')) else ''
            rows += f'<a class="hrow" href="#{c["slug"](mid)}" data-target="{c["slug"](mid)}"><span class="n">{mid}</span><span class="t">{html.escape(t)}<small>{html.escape(w)}</small></span>{pill}</a>'
        else:
            pill = PILL_NEXT if mid in c.get('next_up', ()) else '<span class="pill">soon</span>'
            rows += f'<div class="hrow soon"><span class="n">{mid}</span><span class="t">{html.escape(t)}<small>{html.escape(w)}</small></span>{pill}</div>'
    ids = ' '.join(c['slug'](m[0]) for m in mods)
    words = sum(c['wby'].get(m[0], 0) for m in have)
    patch = patch_block([(m[0], c['wby'].get(m[0]) if m[0] in c['done'] else None) for m in mods], _TONE.get(col, _TONE[c['color']]), phase)
    return tile([c['short'], f'Unit {u}'], col, name, html.escape(why), stats=[(len(have), 'modules written'), (len(mods), 'in all'), (hours(words), 'h of reading')],
                pill=status_pill(status), patch=patch, disclosure=f'<div class="hrows">{rows}</div>', cls='' if have else ' pending',
                attrs=f' id="{c["home_id"]}-u{u}" data-mods="{ids}"')


THEME = {t['id']: t for t in THEMES}
# S-NAV1 step B (21 Nov 2026; Pedro: "the homepage with just the entry points for each area, and then a sub homepage for
# the courses within that area"): an edition of two or more tracks has an area level, one page `track-<id>` per track
# (area_page below), between the home and its courses; an edition of one track (greece) skips it: its home lists the
# track's courses as before and no crumb names the area. AREA_OF: each course page's id (a history course's home, a
# markdown sub-course's) to its track.
MULTI = len(THEMES) > 1
AREA_OF = {c['home_id']: c['theme'] for c in HISTORY} | {sub_page_id(c, k): tr for c in MARKDOWN for k, (tr, _) in c['tracks'].items()}
def crumbs(*items):
    """Breadcrumb trail: (label, target panel id) pairs; the last item is the current page and has no link.
    S-NAV1 step B: Home › Area › Course › Unit. Where an edition has area pages (MULTI), a crumb that links to a course
    page is preceded by its area's (the track's name, to track-<id>) unless the trail already names it; in an edition of
    one track a crumb to track-<id> (a course home names its area) is left out, as there is no area page."""
    seq = []
    for label, tgt in items:
        if tgt and tgt.startswith('track-') and not MULTI:
            continue
        a = AREA_OF.get(tgt) if MULTI and tgt else None
        if a and not (seq and seq[-1][1] == 'track-' + a):
            seq.append((THEME[a]['name'], 'track-' + a))
        seq.append((label, tgt))
    out = []
    for label, tgt in seq:
        out.append(f'<a href="#{tgt}" data-target="{tgt}">{html.escape(str(label))}</a>' if tgt else f'<span aria-current="page">{html.escape(str(label))}</span>')
    return '<nav class="crumbs" aria-label="You are here">' + '<span class="sep" aria-hidden="true">›</span>'.join(out) + '</nav>'

def hours(words):
    """Reading time at 250 words a minute (P90, 4 Nov 2026: one rate for every course, history and markdown), as a
    short label."""
    h = words / 250 / 60
    return f'{h:.1f}'   # P92 check: one decimal on every tile and course home (16.4 beside 5.0, not 16 beside 5.0)


# P93 (4 Nov 2026) · the topographies across the site (Pedro, on P92's home: "Can we animate that topographical
# illustration, very slow, expanding and rotating movements, across the board, and expand that to other pages"). Every
# drawing is viz.py's home kind `contours`, declared here from the data: the home's hero (HERO_TOPO, P92), each course
# home's hero (one rise per unit of the course), What's new's hero (one rise per day it lists), and the patch of every
# tile (a course's units, a history unit's modules, a markdown unit's sections; a planned course one dashed ring). The
# theme (4i) swells each one slowly (S-NAV1 step D: each line about its rise's core, by its distance from it; the turn
# and the whole-layer breath are gone); `phase` starts each drawing of a page at its own point of the cycle.
_TONE = {'var(--red)': 1, 'var(--orange)': 2, 'var(--teal)': 3, 'var(--blue)': 4, 'var(--purple)': 5, 'var(--gold)': 6}


def phases(n):
    """The starting points of the cycle (0 to 1, as a fraction of one sweep) for the n drawings of one page: k/n of the
    way, taken in a stride order so that neighbours on the page differ by more than 1/n; no two drawings of a page
    start at the same point, so none moves in lockstep with another."""
    if n <= 1:
        return [0.0] * n
    st = max(1, round(n * .382))
    while math.gcd(st, n) != 1:
        st += 1
    return [((k * st) % n) / n for k in range(n)]


def ct_lattice(n, box, W, H):
    """n places in a box (fractions of the layout), in order: rows of cells as square as the box allows, every other
    row shifted half a cell and read the other way (a serpentine), so each unit stands beside the one before it."""
    x0, y0, x1, y1 = box
    bw, bh = (x1 - x0) * W, (y1 - y0) * H
    best = None
    for c in range(1, n + 1):
        r = -(-n // c)
        cw, ch = bw / (c + (.5 if r > 1 else 0)), bh / r
        if best is None or min(cw, ch) > best[0] + 1e-9:
            best = (min(cw, ch), c, r, cw, ch)
    _, c, r, cw, ch = best
    out = []
    for k in range(n):
        row, col = divmod(k, c)
        if row % 2:
            col = c - 1 - col
        x = x0 * W + (col + .5 + (.5 if row % 2 else 0)) * cw
        y = y0 * H + (row + .5) * ch
        out.append([round(x / W, 4), round(y / H, 4)])
    return out


def ct_ridge(n, box, W, H):
    """n places in order along a ridge across a box: evenly from left to right, swinging gently above and below its
    middle (What's new's days, oldest at the left)."""
    x0, y0, x1, y1 = box
    return [[round(x0 + (x1 - x0) * (k + .5) / n, 4), round((y0 + y1) / 2 + (y1 - y0) * .32 * math.sin(k * 1.9), 4)] for k in range(n)]


def ct_fit(rises, iv, specs, maxbytes=19500):
    """The layouts for a hero's layer: for each spec (name, width, height, box, place), the rises placed by `place`, then
    the widest spread (from under half the distance between the two nearest places, stepping down by a tenth) at which every
    written rise closes min(2, its levels) rings of its own and its own rings stand inside the spec's view (the part of
    the layout every width it serves shows, above the fade; verify.py checks each on the built page); then the lines simplified a step
    further until the whole layer is at most maxbytes. Returns the layouts; stops the build if no spread holds."""
    lays = []
    for sp in specs:
        W, H, box = sp['width'], sp['height'], sp['box']
        view = sp['small'][1] if 'small' in sp and len(rises) <= sp['small'][0] else sp['view']   # P-DEC11
        at = sp['place'](len(rises), box, W, H)
        near = min((math.hypot((a[0] - b[0]) * W, (a[1] - b[1]) * H) for i, a in enumerate(at) for b in at[i + 1:]), default=W / 4)
        s = near / 2.2 / W
        for _ in range(24):
            lay = dict(name=sp['name'], width=W, height=H, spread=round(s, 4), grid=sp.get('grid', 5), simplify=.8, at=at)
            rr = viz.contours_rings(dict(kind='contours', interval=iv, rises=rises, layouts=[lay]))[sp['name']]
            inside = all(swell_inside(b, W, H, view=view) for _, _, _, b in rr)   # at every pose of the swell (the boxes are its extremes)
            if inside and all(own >= min(2, lv) for _, lv, own, _ in rr):
                break
            s *= .9
        else:
            raise SystemExit(f'build.py ct_fit: no spread lets every rise close its own rings in layout {sp["name"]} ({[r["label"] for r in rises][:3]}...)')
        lays.append(lay)
    blk = dict(kind='contours', interval=iv, rises=rises, layouts=lays)
    while len(viz.render(blk).encode()) > maxbytes:
        for lay in lays:
            lay['simplify'] = round(lay['simplify'] * 1.25, 3)
        if lays[0]['simplify'] > 6:
            raise SystemExit('build.py ct_fit: the layer stays over its byte limit even simplified')
    return lays


_TT = (pathlib.Path(__file__).resolve().parent.parent / 'design/theme.css').read_text()
# S-NAV1 step D (22 Nov 2026): the turn (topo-turn, --topo-turn, TOPO_TURN) and the whole-layer breath are gone. Every line
# of a drawing swells about its own rise's core by 1 + d x --topo-grow (viz.swell_box), so viz.contours_rings gives each
# rise's own rings' box and every line's extent over every pose of the swell already; the checks here are plain boxes.


def swell_inside(b, W, H, pad=6, view=None):   # P93 check: 6 units (about 2.5 px on a 320 px phone's patch; at 3 the closest came to 1.1 px)
    """Whether a box (x0, y0, x1, y1) in a W x H drawing, already taken over every pose of the swell (viz.swell_box: the
    box contours_rings gives), stays inside it, pad units clear (or inside view, fractions of the drawing: a hero's
    window). P93's turned_inside, which turned and grew the box here, before S-NAV1 step D."""
    lo_x, lo_y, hi_x, hi_y = (view[0] * W, view[1] * H, view[2] * W, view[3] * H) if view else (pad, pad, W - pad, H - pad)
    return lo_x <= b[0] and b[2] <= hi_x and lo_y <= b[1] and b[3] <= hi_y


def swell_clear(b, W, H, pad=6):
    """P94 (turned_clear until S-NAV1 step D): swell_inside split by direction: whether the box (over every pose of the
    swell) stays pad units clear of the drawing's left and right edges, and of its top and bottom (both are true exactly when swell_inside is)."""
    return pad <= b[0] and b[2] <= W - pad, pad <= b[1] and b[3] <= H - pad


def patch_block(rises, tone, phase=None):
    """A tile's contour patch (a course's units, a history unit's modules, a markdown unit's sections; P92 for a course):
    rises [(label, words or None)], one per part in order, a written part by its words, a planned one flat (a dashed
    ring); a contour every 5.5th part of the largest, so every patch reads at one density (the stats give the size);
    4:1, the tile's width. P93: the spread .40 over the parts, narrowed by a tenth until no line reaches the patch's
    edge and every part's rings stay inside the frame at every pose of the swell (swell_inside); a planned course (no
    part written) is one dashed ring at the patch's centre."""
    top = max((w for _, w in rises if w), default=0)
    lay = dict(name='patch', width=720, height=180, spread=round(.40 / len(rises), 4), grid=6, simplify=.5,
               **(dict(at=[[.5, .5]]) if len(rises) == 1 else {}))
    blk = dict(kind='contours', patch=True, rises=[dict(label=k, tone=tone, **(dict(words=w) if w else dict(planned=True))) for k, w in rises], layouts=[lay])
    if top:
        blk['interval'] = top / 5.5
        for _ in range(30):
            rr = viz.contours_rings(blk)
            ext = rr[('patch', 'extent')]
            if not rr[('patch', 'edge')] and (ext is None or swell_inside(ext, 720, 180)) and all(swell_inside(b, 720, 180) for _, _, _, b in rr['patch']):
                break
            lay['spread'] = round(lay['spread'] * .9, 4)
        else:
            raise SystemExit(f'build.py patch_block: no spread keeps the patch of {rises[0][0]}... clear of its frame')
    if phase is not None:
        blk['phase'] = round(phase, 3)
    return viz.render(blk)


# P94 (8 Nov 2026; Pedro, 5 Nov 2026, 09:12: "These topographical abstract illustrations are great. We could use them as
# paragraph separators (the ones that are more horizontal)"; the plan's part A): every section of every reading page ends
# with a horizontal topography drawn from its paragraphs, before its next and previous.
SEP_W, SEP_H = 1200, 170   # the separator's layout: the column's width at 1200 by 170 units (about 7:1)
SEP_BOX = (.1, .42, .9, .58)   # where its rises stand: along a ridge across the frame, swinging gently about its middle
SEP_MAX = 6 * 1024   # bytes, at most
SEP_FREE, SEP_PER = 38, 135   # W-SCE2 (21 Nov 2026): a rise costs about 125 bytes before any line (its <g>, label, words, spot), so a
# section of over SEP_FREE paragraphs gets SEP_PER bytes more for each one beyond (SCE2 §3, 44 paragraphs: no simplifying brings
# it under 6 KB); verify.py's separator check allows the same
SEP_SY, SEP_STRETCH, SEP_STRETCH_MIN = 24, 6, 2.5   # the hills' first spread across the ridge, in units, and how far each is drawn out along it, at most and at least


def sep_block(paras, tone, phase=None, label=''):
    """A section's separator: paras [words of each top-level paragraph of the section, in order], one rise each along a
    ridge (ct_ridge, as What's new's days), in the course's tone, a contour every 5.5th of the section's largest
    paragraph (as a tile's patch steps by its largest part); 1200 by 170 units fitted whole in its frame (meet). Its
    spread is fitted as patch_block fits a tile's patch, narrowed by a tenth until no line reaches the frame and every
    rise's rings and every line stay clear of it at every pose of the swell (swell_inside, on the boxes
    viz.contours_rings takes over the swell: at rest and at its top): its hills start SEP_SY units across the ridge and drawn out along it as far as the
    next rise (stretch, at most SEP_STRETCH times), so neighbours meet in one ridge; where a pose takes a line past the
    top or bottom the hills are lowered, past an end they are drawn out less (then lowered once at SEP_STRETCH_MIN); then its lines are
    simplified a step further until it is at most SEP_MAX bytes, plus SEP_PER for each rise over SEP_FREE (no rise is ever dropped). Each rise is labelled by its
    place (¶1, ¶2 ...); label, the section's id, seeds their outlines (the ripple), so each separator's are its own."""
    n, top = len(paras), max(paras)
    at = ct_ridge(n, SEP_BOX, SEP_W, SEP_H)
    # the first spread tried (the hills' height across the ridge): SEP_SY units; along the ridge each hill is drawn out
    # (stretch) to under half the distance between two neighbours, so neighbours meet in one ridge, at most SEP_STRETCH
    # times its height and never less than round
    gap = (SEP_BOX[2] - SEP_BOX[0]) * SEP_W / n
    # P94 check: every hill drawn out at least SEP_STRETCH_MIN times its height, so a ridge of many paragraphs stays a
    # flat ridge (at 38 rises, round hills in narrow slots read as dots and blobs); along the ridge as far as about the
    # next rise, so neighbours meet; across it SEP_SY units, or less where the ridge is dense
    stretch = max(SEP_STRETCH_MIN, min(SEP_STRETCH, gap / SEP_SY))
    lay = dict(name='ridge', width=SEP_W, height=SEP_H, spread=round(min(SEP_SY, 1.1 * gap / stretch) / SEP_W, 5), grid=8, simplify=.8, at=at,
               stretch=round(stretch, 3))
    blk = dict(kind='contours', patch=True, sep=True, interval=top / 5.5, seed=label,
               rises=[dict(label=f'¶{k + 1}', words=w, tone=tone) for k, w in enumerate(paras)], layouts=[lay])
    for _ in range(80):
        rr = viz.contours_rings(blk)
        boxes = [b for _, _, _, b in rr['ridge']] + ([rr[('ridge', 'extent')]] if rr[('ridge', 'extent')] else [])
        cl = [swell_clear(b, SEP_W, SEP_H) for b in boxes]
        ok_x, ok_y = all(x for x, _ in cl), all(y for _, y in cl)
        if ok_x and ok_y and not rr[('ridge', 'edge')]:
            break
        if not ok_y:   # too tall at some pose: lower every hill (the spread across the ridge)
            lay['spread'] = round(lay['spread'] * .9, 5)
        if not ok_x or rr[('ridge', 'edge')]:   # too long: draw the hills out less (never under round)
            if lay['stretch'] > SEP_STRETCH_MIN:
                lay['stretch'] = round(max(SEP_STRETCH_MIN, lay['stretch'] * .9), 3)
            elif ok_y:
                lay['spread'] = round(lay['spread'] * .9, 5)
    else:
        raise SystemExit(f'build.py sep_block: no spread keeps the separator of {label} clear of its frame')
    assert all(swell_inside(b, SEP_W, SEP_H) for b in boxes)
    if phase is not None:
        blk['phase'] = round(phase, 3)
    out = viz.render(blk)
    cap = SEP_MAX + SEP_PER * max(0, n - SEP_FREE)
    while sep_bytes(out) > cap:
        lay['simplify'] = round(lay['simplify'] * 1.25, 3)
        if lay['simplify'] > 60:   # W-PB8 (13 Nov 2026): raised from 12 so a section of 38 paragraphs (PB8 §6) still fits SEP_MAX; no rise dropped
            raise SystemExit(f'build.py sep_block: the separator of {label} ({paras}) stays over {cap} bytes even simplified')
        out = viz.render(blk)
    return out


def sep_bytes(h):
    """P94: a separator's size as the page holds it (verify.py measures the element's outerHTML): the HTML parser writes
    every self-closed SVG element with an end tag, <path d=".."></path>, a few bytes more than the source's <path/>."""
    return len(re.sub(r'<(\w+)([^<>]*?)/>', r'<\1\2></\1>', h).encode())


def sep_kit(tone):
    """P94: what mdcourse.reading needs to end each section on its separator, in the tone given."""
    return dict(block=lambda paras, ph, label: sep_block(paras, tone, ph, label), phases=phases, tone=tone)   # P95: the tone, for the page's relief too


# A course home's hero layer (P93): the tall layout a square, its rises (box) and their own rings (view) where both a
# phone's portrait hero (390 px: about 390 x 590 to 760 with the 22 px above it) and the tablet's landscape one (768 x
# 400 to 480) show them, above the fade (the phone's window is x .24 to .76 on the tallest hero, the tablet's, on the shortest hero
# (Building with AI, 376 + 22 px), y .24 to .76, faded from .71); the wide one 2:1, as wide as the 1280 px hero (980 x 400 to 480), its rises above the stat
# boxes as far as their number allows. What's new's hero is flatter (about 390 x 360 on a phone, 980 x 260 from 768
# px), so its tall layout is 1.6:1 (a phone shows x .16 to .84, the tablet y .22 to .78, faded from .72) and its wide
# one 3.7:1.
# P-DEC11 (21 Nov 2026): `small` = (n, view): a hero of n rises or fewer is held to that view instead. One or two rises stand
# in one row, their spread set by the width between them, so their rings are the tallest any course draws (two: about 45%
# of the layout's height) and reach the top and the fade of a hero shorter than the 400 px the view assumes (a course
# with a one-line lede: the template test's home-composting, 980 x 347 at 1280 px, shows y .153 to .847, faded from
# .778; 10 desktop motion failures). Its view is the band a 330 px hero shows: y .17 to .76 (.17 + .9 x .66). Academy's
# course homes (11 to 15 rises, heroes 398 to 500 px) keep their view and their bytes.
COURSE_TOPO = [dict(name='tall', width=1000, height=1000, box=(.29, .27, .71, .67), view=(.25, .25, .75, .7), place=ct_lattice),
               dict(name='wide', width=1000, height=500, box=(.1, .12, .9, .66), view=(.04, .1, .96, .84), place=ct_lattice,
                    small=(2, (.04, .17, .96, .76)))]
NEW_TOPO = [dict(name='tall', width=1000, height=625, box=(.24, .3, .76, .64), view=(.18, .27, .82, .67), place=ct_ridge),
            dict(name='wide', width=1000, height=270, box=(.17, .26, .83, .66), view=(.1, .12, .9, .8), place=ct_ridge)]   # views with a margin for a shorter hero (an edition's eyebrow is a line shorter)
NEW_INTERVAL = 11000    # words between two of What's new's contour levels: its largest day (22 Oct 2026, 221,673 words) stands 20, inside the 10 to 25 the row sets (verify.py checks it), and its smallest (30 Oct, 14,178) 1.29 levels, a ring of its own that reads (at 14,000 it stood 1.01 levels, a 2 px ring; P93 check)


def new_interval(top):
    """P-DEC15 (21 Nov 2026): What's new's interval for an edition whose largest day is top words. NEW_INTERVAL where
    that day reaches 10 levels at it (110,000 words: academy and greece, byte-identical); else a tenth of the day,
    rounded down (at least 1), so a smaller edition's largest day also stands 10 levels (top // (top // 10) is 10 to
    19) and its What's new shows a rise (marketing-ai: 79,671 words, 7,967 a level; it stood 7 at 11,000; the template
    test's fieldnotes stood 0). verify.py repeats this rule."""
    return NEW_INTERVAL if top >= 10 * NEW_INTERVAL else max(1, int(top) // 10)


# P-DEC5 (21 Nov 2026): a brand's --sans changes how many lines a hero's lede takes, and so the hero's height. The
# lede's measure is 62ch, and ch is the face's "0": Source Sans 3's (0.497 em) is narrower than DM Sans' (0.684 em), so
# the measure narrows by more than the text does and a lede of five lines in DM Sans takes seven (Personal Brand: a 471
# px hero becomes 522). The wide layout is fitted for heroes of 400 to 480 px (above); a taller one is drawn larger
# (slice) and its sides cut off, so the end rises' rings left the frame (verify.py's desktop motion poses). course_topo
# takes the extra lines into account: in DM Sans' metrics (any edition whose brand keeps them) it returns COURSE_TOPO
# itself, so Academy's layers are unchanged.
_LEDE = {k: v for rule in re.findall(r'(?<![\w.-])\.lede\{([^}]*)\}', _TT) for k, v in re.findall(r'([\w-]+):([^;]+)', rule)}
LEDE_CH, LEDE_PX, LEDE_LH = float(_LEDE['max-width'].removesuffix('ch')), float(_LEDE['font-size'].removesuffix('px')), float(_LEDE['line-height'])
HERO_TALL = 480 + 22   # the tallest hero frame (hero and the 22 px above it) the wide layout is fitted for


def lede_lines(text, adv):
    """Lines a hero's lede takes at its measure (LEDE_CH of the face's "0"), wrapped at spaces, in the advances adv
    (viz's per-1000-em table for the --sans face at 400)."""
    words = html.unescape(re.sub(r'<[^>]+>', '', text)).split()
    w = lambda s: sum(adv.get(ch) or 900 for ch in s) / 1000 * LEDE_PX
    measure, sp = LEDE_CH * w('0'), w(' ')
    n, line = (1 if words else 0), 0.0
    for x in words:
        add = w(x) if not line else sp + w(x)
        if line and line + add > measure:
            n, line = n + 1, w(x)
        else:
            line += add
    return n


def course_topo(lede):
    """COURSE_TOPO for a course home whose lede is lede: as it stands if the brand's --sans wraps it in no more lines than
    DM Sans does (always, in DM Sans' metrics); else its wide layout's box and view drawn in towards the middle by the
    ratio of the tallest hero the layout is fitted for to that hero with the extra lines, as a slice into a taller frame
    shows that much less of the layout's width. P-DEC11's `small` view (a hero of one or two rises) is drawn in by the same
    ratio, so the two compose."""
    extra = (lede_lines(lede, viz._ADV['sans']) - lede_lines(lede, viz._DEFAULT[0]['sans'])) * LEDE_PX * LEDE_LH
    if extra <= 0:
        return COURSE_TOPO
    k = HERO_TALL / (HERO_TALL + extra)
    pull = lambda f: (round(.5 - (.5 - f[0]) * k, 4), f[1], round(.5 + (f[2] - .5) * k, 4), f[3])
    small = lambda sp: dict(small=(sp['small'][0], pull(sp['small'][1]))) if 'small' in sp else {}   # P-DEC11's band of one or two rises, drawn in alike
    return [sp if sp['name'] != 'wide' else dict(sp, box=pull(sp['box']), view=pull(sp['view']), **small(sp)) for sp in COURSE_TOPO]


def hero_layer(rises, tone, iv, specs, phase=0.0):
    """A hero's topography (a course home's, What's new's): rises [(label, words or None)] and their tone (one for all,
    or one per rise); the layer with its two layouts (tall below 1100 px, wide from it), placed and sized by ct_fit."""
    tones = tone if isinstance(tone, list) else [tone] * len(rises)
    rs = [dict(label=k, tone=t, **(dict(words=w) if w else dict(planned=True))) for (k, w), t in zip(rises, tones)]
    lays = ct_fit(rs, iv, specs)
    return viz.render(dict(kind='contours', interval=iv, rises=rs, layouts=lays, phase=round(phase, 3)))


def course_home(c):
    # P93: the hero's topography (one rise per unit of the course, as its tile's patch) and every unit a tile, each
    # drawing of the page starting at its own point of the cycle
    rises = unit_rises(c)
    top = max((w for _, w in rises if w), default=0)
    ph = phases(1 + sum(len(us) for _, _, us, _, _ in c['parts']))
    layer = hero_layer(rises, _TONE[c['color']], top / 5.5, course_topo(fill(c['lede'], c)), ph[0]) if top else ''
    parts, k = '', 1
    for num, title, us, when, ctx in c['parts']:
        nmods = sum(len(c['umap'][u][2]) for u in us)
        tiles = ''
        for u in us:
            tiles += unit_tile(c, u, ph[k]); k += 1
        parts += f'<section class="part{" deep" if num == "+" else ""}"><header class="phd"><span class="pnum">{num}</span><div class="ptx"><div class="pmeta"><span>{"Unit " + us[0] if len(us) == 1 else "Units " + us[0] + "–" + us[-1]}</span><span>{nmods} modules</span><span>{when}</span></div><h2>{title}</h2><p>{ctx}</p></div></header><div class="cgrid">{tiles}</div></section>'
    E = c['eras']
    ribbon = ''.join(f'<span class="seg" style="flex-grow:{e[2]-e[1]};--c:{e[3]}" title="{e[0]}"></span>' for e in E)
    legend = ''.join(f'<li style="--c:{e[3]}"><i></i><b>{e[0]}</b><span class="yr">{yr(e[1])} – {yr(e[2])}</span><span class="un2">{e[4]}</span></li>' for e in E)
    ticks = ''.join(f'<span style="left:{p}">{t}</span>' for t, p in c['ticks'])
    nunits = len(c['units']) - 1
    return f'''
<section class="panel home" id="{c['home_id']}" data-ctx="{c['id']}" data-kind="course" data-split="home" data-t="{c['short']}" data-u="COURSE {c['num']}" data-c="{c['color']}" style="--cc:{c['color']}" hidden>
  <header class="hero has-topo">
    {layer}
    {crumbs((SITE_NAME, 'home'), (THEME[c['theme']]['name'], 'track-' + c['theme']), (f"Course {c['num']} · {c['short']}", None))}
    <div class="eyebrow"><span class="u" style="--c:{c['color']}">{c['eyebrow']}</span>{(' · ' + c['family_label']) if c.get('family_label') else ''}{' · <span class="u" style="--c:var(--gold)">IN PROGRESS</span>' if c['status'] != 'available' else ' · <span class="u" style="--c:var(--teal)">COMPLETE</span>'}</div>
    <h1>{c['h1']}</h1>
    <p class="lede">{fill(c['lede'], c)}</p>
    <div class="stats" data-n="4"><div><b>{c['nrep']}</b><span>of {c['content_mods']} reports written</span></div><div><b>{c['units_complete']}</b><span>of {nunits} units complete</span></div><div><b>{c['words']//1000}k</b><span>words so far</span></div><div><b>{hours(c['words'])}</b><span>hours of reading</span></div></div>
    <div class="hlinks"><a class="hbtn cont" href="#{c['home_id']}" data-course="{c['id']}" hidden><span>Continue</span><b></b></a>{start_btn(c)}<a class="hbtn alt" href="#{c['syl_id']}" data-target="{c['syl_id']}"><span>Syllabus</span><b>All {c['total_mods']} prompts, copyable</b></a></div>
    {c['flag']}
  </header>

  <section class="era">
    <div class="era-h"><h2>{c['era_title']}</h2><span>{c['era_range']}</span></div>
    <div class="ribbon" role="img" aria-label="{c['era_aria']}">{ribbon}</div>
    <div class="ticks" aria-hidden="true">{ticks}</div>
    <p class="era-note">{c['era_note']}</p>
    <ul class="legend">{legend}</ul>
  </section>
  {viz.render(c['figure']) if c.get('figure') else ''}

  <details class="howto rules">
    <summary><h2>How to read it</h2><span>{c['rules_count']}</span></summary>
    <ol>
      {c['rules']}
    </ol>
  </details>

  {parts}

  <details class="howto rules">
    <summary><h2>The reading spine</h2><span>primary and secondary</span></summary>
    {c['spine']}
  </details>
  <a class="hbtn alt wide" href="#{c['home_id']}-built" data-target="{c['home_id']}-built"><span>How it was built</span><b>The model behind each report, every check and audit with its verdict, the flags still open.</b></a>
  <a class="hbtn alt wide" href="#home" data-target="home"><span>{html.escape(SITE_NAME)}</span><b>{c['closing']}</b></a>
</section>'''


def syllabus(c):
    s = ''
    a = c['syl_anchor']
    for u, name, why, mods in c['units']:
        col = c['unit_colors'][u]
        s += f'<section class="sunit" id="{a}-u{u}" style="--c:{col}"><div class="unit-head"><span class="n">UNIT {u}</span><h2>{html.escape(name)}</h2></div><p class="unit-why">{html.escape(why)}</p><div class="smods">'
        for mid, t, w in mods:
            if mid in c['done']:
                link = f'<a class="rlink" href="#{c["slug"](mid)}" data-target="{c["slug"](mid)}">read the report</a>' + (' ' + PILL_UNCK if unchecked(c['prov'].get(mid, '')) else '')
            else:
                link = '<span class="pill next">next session</span>' if mid in c.get('next_up', ()) else '<span class="pill">report coming soon</span>'
            s += f'<article class="smod" id="s-{c["slug"](mid)}"><div class="smod-top"><span class="code">{mid}</span><h3>{html.escape(t)}</h3></div><p class="why">{html.escape(w)}</p><div class="pbox"><pre>{html.escape(c["all_prompts"][mid])}</pre><div class="pbar"><button class="copy" type="button">copy prompt</button>{link}</div></div></article>'
        s += '</div></section>'
    return f'''
<section class="panel syl" id="{c['syl_id']}" data-ctx="{c['id']}" data-kind="syllabus" data-split="syllabus" data-t="Syllabus and prompts" data-u="{c['label']}" data-c="var(--gold)" style="--cc:{c['color']}" hidden>
  <header class="hero">
    {crumbs((SITE_NAME, 'home'), (c['short'], c['home_id']), ('Syllabus', None))}
    <div class="eyebrow"><span class="u" style="--c:{c['color']}">{c['label']}</span> · <span class="u" style="--c:var(--gold)">SYLLABUS</span> · {c['total_mods']} modules · every prompt in full</div>
    <h1>{c['short']}: syllabus and prompts</h1>
    <p class="lede">This is the complete syllabus the reports were generated from. Each module has its drop-in prompt; copy it into a new chat to regenerate a report yourself, extend one, or compare a fresh answer against the one here. Where a report exists it is linked.</p>
    {c['flag']}
  </header>
  <section class="howto"><h2>How to run it</h2>{c['syl_intro']}</section>
  <nav class="toc" aria-label="Units">{''.join(f'<a href="#{a}-u{u}">{u} · {html.escape(n)}</a>' for u, n, _, _ in c['units'])}</nav>
  {s}
</section>'''


def tile(parts, color, title, line, stats=None, pill='', patch='', href=None, disclosure=None, cls='', attrs=''):
    """P93 (4 Nov 2026, Pedro: "make this new tile style propagate across the site"): the one tile, everywhere a course
    or a unit is listed: the chip (its parts, a break allowed only between them) with the status pill under it, the
    title, a two-line line, three stats (or none: a planned course's ghost), its own contour patch, and either the whole
    tile the link (href) or, for a history unit, a disclosure whose summary is the tile and which opens to its module
    rows (disclosure: the html under the summary). cls adds a modifier: ' ghost' (a planned course or unit, dashed),
    ' pending' (a unit not yet written). Every field is a class of theme 4f and 4h (.course.live and its children)."""
    chip = '<span class="cname">' + ' '.join(f'<span class="cpart">{html.escape(x)}{" ·" if k < len(parts) - 1 else ""}</span>' for k, x in enumerate(parts)) + '</span>'
    stats = f'<div class="cstats">{"".join(f"<span><b>{v}</b> {html.escape(l)}</span>" for v, l in stats)}</div>' if stats else ''
    inner = f'<div class="ctop">{chip}{pill}</div><span class="ctitle">{html.escape(title)}</span><p>{line}</p>{stats}{patch}'
    st = f' style="--c:{color}"'
    if disclosure is not None:
        return f'<details class="course live{cls}"{attrs}{st}><summary>{inner}{ICON_CHEV}</summary>{disclosure}</details>'
    if href:
        tgt = f' data-target="{href[1:]}"' if href.startswith('#') else ''
        return f'<a class="course live{cls}" href="{href}"{tgt}{attrs}{st}>{inner}</a>'
    return f'<div class="course live{cls}"{attrs}{st}>{inner}</div>'


def status_pill(status):
    return {'complete': '<span class="pill live">complete</span>', 'available': '<span class="pill live">complete</span>',
            'written': '<span class="pill live">written</span>', 'in progress': '<span class="pill prog">in progress</span>',
            'next session': PILL_NEXT, 'next': PILL_NEXT}.get(status, f'<span class="pill">{html.escape(status)}</span>')


def card(theme, color, short, title, blurb, done, total, words, status, href, external=False, patch=''):
    """A course's tile on the home (P90, P91, P92; P93: built by tile()): the chip (track and course) with the status
    pill, the title, the one-sentence tile line (two lines at most), the same three stats for every course (units
    written, of the total, hours of reading at 250 words a minute) and the course's own contour patch (tile_patch);
    the whole tile is the link."""
    return tile([theme, short], color, title, blurb, stats=[(done, 'units written'), (total, 'in all'), (hours(words), 'h of reading')],
                pill=status_pill('available' if status == 'available' else status), patch=patch, href=href)


def root_card(c, phase=None):
    return card(THEME[c['theme']]['name'], c['color'], f'Course {c["num"]}', c['name'], html.escape(c['tile']), c['units_complete'], c['card_units'], c['words'], c['status'], f'#{c["home_id"]}', patch=tile_patch(c, phase))


for c in HISTORY:
    load(c)



def load_markdown(c):
    """A markdown course: its data (kit/pack.py: the course's pack, courses/<slug>/course.toml [pack] with briefs.md
    and pages/: courses, units, briefs, audit log, status) and
    its filed units, read from the vault (courses/<slug>/, A5). A unit is written when its file is in the vault with
    front matter; the data's READINGS add a page's intro and top-bar name, and its research pages (an `md` path
    relative to the data folder, pack.data_dir). WRITTEN is derived here, never typed."""
    d = pack.load(c)
    c['hub'] = d
    c['data_dir'] = pack.data_dir(c)
    c['vault'] = R.parent / c['vault']
    codes = {u[0]: (sc, u) for sc in d.COURSES for u in sc['units']}
    vault = {}
    for f in sorted(c['vault'].glob('*.md')):
        fm = howbuilt.front(f)
        if not fm.get('code'):
            continue
        if fm['code'] not in codes:
            raise SystemExit(f'{f.relative_to(R.parent)}: code {fm["code"]} is not a unit of {c["data"]}')
        if fm['code'] in vault:
            raise SystemExit(f'{f.relative_to(R.parent)}: a second vault file for {fm["code"]}')
        vault[fm['code']] = (f, fm)
    c['vault_units'] = vault
    readings, by_code = [], {}
    for r in d.READINGS:
        if 'md' in r:                                  # research or other written material kept in the data folder
            r['path'] = c['data_dir'] / r['md']
        else:                                          # a unit's reading page: its text is the vault file
            code = r['covers'][0]
            if code not in vault:
                raise SystemExit(f'{c["data"]}: READINGS {r["id"]} covers {code}, which has no file in {c["vault"].relative_to(R.parent)}/')
            r['path'] = vault[code][0]
        for x in r['covers']:
            by_code[x] = r['id']
        readings.append(r)
    for code, (f, fm) in vault.items():                # a filed unit without a READINGS entry still gets its page
        if code not in by_code:
            sc, u = codes[code]
            r = dict(id=f'read-{c["id"]}-{code.lower()}', path=f, course=sc['key'], title=fm.get('title', u[1]), covers=[code],
                     name=f'{code} · {fm.get("title", u[1])}',
                     intro=f'Unit {code}, written {fm.get("written", "(date not recorded)")} by {fm.get("model", "(model not recorded)")}, search {fm.get("search", "not recorded")}.')
            readings.append(r)
            by_code[code] = r['id']
    # A-4 (2 Nov 2026): reading pages in the course's own unit order, research pages after them, as the sidebar
    # lists them; the pager's Previous unit and Next unit follow this order (it followed the data file's order before)
    pos = {u[0]: i for sc in d.COURSES for i, u in enumerate(sc['units'])}
    readings.sort(key=lambda r: ('md' in r, pos.get(r['covers'][0], len(pos)) if r.get('covers') else len(pos)))
    d.READINGS[:] = readings
    d.WRITTEN = {code: by_code[code] for code in vault}
    c['subcourses'] = d.COURSES
    c['written'] = d.WRITTEN
    c['nunits'] = sum(len(sc['units']) for sc in d.COURSES)
    c['nwritten'] = sum(1 for sc in d.COURSES for u in sc['units'] if u[0] in d.WRITTEN)
    c['readings'] = {r['id']: r for r in d.READINGS}
    return c


def md_courses(c):
    """One Academy course per course in the data file, each under its own track."""
    d = c['hub']
    out = []
    for sc in d.COURSES:
        sc['k'] = sc['key'].lower()
        theme, short = c['tracks'][sc['key']]
        done = [u for u in sc['units'] if u[0] in c['written']]
        pid = sub_page_id(c, sc['key'])   # brand-a, brand-b; a new course: <id>-<key>
        legacy = c.get('legacy_ids')                   # Brand + AI keeps the anchors it had at A3 (#briefs-a, #b-a2)
        out.append(dict(id=pid, home_id=pid, briefs_id=f'briefs-{sc["k"]}' if legacy else f'{pid}-briefs',
                        brief_anchor='b-' if legacy else f'{pid}-b-', parent=c, sc=sc, theme=theme, short=short, key=sc['key'],
                        name=sc['name'], color=sc['color'], units=sc['units'], done=done, nunits=len(sc['units']), nwritten=len(done),
                        status=('available' if len(done) == len(sc['units']) else 'in progress') if done else 'coming soon',
                        tile=c.get('tiles', {}).get(sc['key'], sc['tile'])))   # P90: course.toml's `tiles` sentence for the home card   # a course with no unit filed is coming soon; every unit filed is complete ('available', as a finished history course is; A-5, 3 Nov 2026)
    return out


for c in MARKDOWN:
    load_markdown(c)
MD = [m for c in MARKDOWN for m in md_courses(c)]
MDKIT = dict(wc=wc, tile=tile, patch=patch_block, hero=hero_layer, hours=hours, phases=phases, tone=_TONE, topo=COURSE_TOPO, pill=status_pill, sep=sep_kit)
for m in MD:
    m['panels'], m['nav'], m['nbib'] = mdcourse.build(m, crumbs, THEME, PILL_NEXT, ICON_CHEV, dict(MDKIT, topo=course_topo(m['sc']['intro'])))   # P-DEC5: the hero's layouts for its lede in the brand's face
    # P90 (4 Nov 2026): a markdown course's words, as a history course's are counted (wc, figures left out), for the
    # hours of reading on its home card. P93: each written unit's words are its reading page's sections, each counted
    # as its text alone (mdcourse.section_text: not its next and previous buttons or its band's numeral, which P90's
    # count from the report's opening tag took in, with the tag's own `steps">`), set by mdcourse.build as m['wby']
    # and m['secw'] (the sections in order, for the unit tile's patch)
    m['wby'] = {u[0]: m['wby'][u[0]] for u in m['done']}
    m['words'] = sum(m['wby'].values())


# Derived fields (backlog row "Academy build: derived fields", 28 Oct 2026). Every number the home, the drawer and the
# track headers show comes from here, so no two places can disagree.
def next_unit(c):
    """A history course's next module to write: the first in syllabus order without a report, the audit unit excluded."""
    for u, _, _, mods in c['units']:
        if u == c['audit_unit']:
            continue
        for mid, t, _ in mods:
            if mid not in c['done']:
                return mid, t
    return None


def md_next(m):
    """A markdown course's next unit to write: the first in its build order without a vault file."""
    for u in m['units']:
        if u[0] not in m['parent']['written']:
            return u[0], u[1]
    return None


for c in HISTORY:
    c['next'] = next_unit(c)
    c['pct'] = round(100 * c['nrep'] / c['content_mods']) if c['content_mods'] else 0
for m in MD:
    m['next'] = md_next(m)
    m['pct'] = round(100 * m['nwritten'] / m['nunits']) if m['nunits'] else 0


def dated_units():
    """Every written unit with a recorded date, newest first: a markdown unit's `written` front-matter field; a history
    report's date from provenance.json's `written` map ({course: {module: ISO date}}), filled by p91_dates.py from the
    work session that filed it (P91, 4 Nov 2026; its `written_approx` lists the reports whose session ran over several
    days, whose date is that session's first day and is marked approximate).
    Each entry a dict: date, rank, course (short name), cname (full name), color, code, title, pid (its page), model,
    approx, home (the course home's panel id).
    P90 (4 Nov 2026): units filed on the same day are ordered by the course's build order (a markdown course's ORDER in
    its data file, else its unit order; a history course's syllabus order), the later first, so the newest filed unit
    leads (four IA units share 2026-11-03, and the sort, stable on the vault's file order, put IA3 first)."""
    out = []
    for m in MD:
        vault = m['parent']['vault_units']
        order = [o[0] if isinstance(o, (tuple, list)) else o for o in getattr(m['parent']['hub'], 'ORDER', [])]
        for k, u in enumerate(m['units']):
            if u[0] in vault:
                fm = vault[u[0]][1]
                if fm.get('written'):
                    rank = order.index(u[0]) if u[0] in order else len(order) + k
                    out.append(dict(date=str(fm['written']), rank=rank, course=m['short'], cname=m['name'], color=m['color'], code=u[0],
                                    title=fm.get('title', u[1]), pid=m['parent']['written'][u[0]], model=fm.get('model', ''), approx=False, home=m['home_id'], hist=False,
                                    words=m['wby'].get(u[0], 0)))   # P93: for What's new's topography, as the cards count them
    for c in HISTORY:
        pos = list(c['index'])
        ap = set(PROV.get('written_approx', {}).get(c['id'], []))
        for i, d in PROV.get('written', {}).get(c['id'], {}).items():
            if i in c['index']:
                out.append(dict(date=d, rank=pos.index(i), course=c['short'], cname=c['name'], color=c['color'], code=i, title=c['index'][i]['title'],
                                pid=c['slug'](i), model=c['prov'].get(i, c['default_model']), approx=i in ap, home=c['home_id'], hist=True, words=c['wby'].get(i, 0)))
    return sorted(out, key=lambda x: (x['date'], x['rank']), reverse=True)


DATED = dated_units()


def whats_new():
    """P91 (4 Nov 2026) · What's new (Pedro: "units and courses"): every dated unit (DATED) and every course started,
    newest first. A course starts on the day its first unit was filed (the earliest date; on that day the first in its
    build order); its row sits directly below that unit's row (read newest first, the course begins with it), and is
    approximate when that unit's date is."""
    rows = [dict(x, kind='unit') for x in DATED]
    firsts = {}
    for x in DATED:
        f = firsts.get(x['home'])
        if f is None or (x['date'], x['rank']) < (f['date'], f['rank']):
            firsts[x['home']] = x
    for home, f in firsts.items():
        k = next(i for i, r in enumerate(rows) if r is not None and r['kind'] == 'unit' and r['home'] == home and r['code'] == f['code'])
        rows.insert(k + 1, dict(f, kind='course', title=f['cname'], first=f['code']))   # P91 check: below its first unit, the older event
    return rows


WHATSNEW = whats_new()
RECENT = WHATSNEW[:6]


def short_date(iso):
    """2026-10-28 → 28 Oct 2026."""
    try:
        import datetime
        return datetime.date.fromisoformat(iso).strftime('%-d %b %Y')
    except Exception:
        return iso

# the changelog page, built from CHANGELOG.md (the file is the source; the page is a rendering of it)
def md_inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2">\1</a>', t)
    return t


def md_list(items):
    h, depth = '', 0
    for lvl, txt in items:
        if lvl + 1 > depth:
            while depth < lvl + 1:
                h += '<ul>'; depth += 1
        else:
            h += '</li>'
            while depth > lvl + 1:
                h += '</ul></li>'; depth -= 1
        h += f'<li>{md_inline(txt)}'
    h += '</li>'
    while depth > 1:
        h += '</ul></li>'; depth -= 1
    return h + '</ul>'


def md_blocks(lines):
    """The subset CHANGELOG.md uses: ### headings, paragraphs, '- ' lists nested by two spaces, pipe tables."""
    out, i, bullet = [], 0, re.compile(r'\s*- ')
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
        elif ln.startswith('### '):
            out.append(f'<h3>{md_inline(ln[4:])}</h3>'); i += 1
        elif ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            out.append('<div class="tbl"><table><thead><tr>' + ''.join(f'<th>{md_inline(c)}</th>' for c in rows[0]) + '</tr></thead><tbody>'
                       + ''.join('<tr>' + ''.join(f'<td>{md_inline(c)}</td>' for c in r) + '</tr>' for r in rows[2:]) + '</tbody></table></div>')
        elif bullet.match(ln):
            items = []
            while i < len(lines) and bullet.match(lines[i]):
                items.append(((len(lines[i]) - len(lines[i].lstrip(' '))) // 2, lines[i].strip()[2:])); i += 1
            out.append(md_list(items))
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(('### ', '|')) and not bullet.match(lines[i]):
                para.append(lines[i].strip()); i += 1
            out.append(f'<p>{md_inline(" ".join(para))}</p>')
    return ''.join(out)


# S-PAGES (15 Nov 2026) · the Changelog and Backlog pages, rendered from docs/site-log.md alone: a plain overview by area
# for an ordinary reader, not the engine's records. docs/BACKLOG.md, docs/CHANGELOG.md and kit/CHANGELOG.md stay in the
# repo and are not on the site. The file holds two pipe tables: "## Next" (#, Code, Area, What it is), in the overall
# order, and "## Done" (Date, Code, Area, What happened), dates as YYYY-MM-DD; method.md §8 says who writes them.
SL_AREAS = [*LOG_AREAS,   # (name, what it holds, the track whose tone it takes): catalog.toml `log_areas`, the order of the per-area tables
    (*B['log_area'], None)]   # S-DEC3: the site's own area (brands/<name>.toml `log_area`)
SL_TONE = {n: next((t['color'] for t in THEMES if t['id'] == tid), 'var(--gold)') for n, _, tid in SL_AREAS}


def site_log(path):
    """docs/site-log.md as (next, done): next [(n, code, area, sentence)] in order; done [(iso, code, area, sentence)]."""
    import datetime
    nxt, done, sec = [], [], None
    for k, ln in enumerate(path.read_text(encoding='utf-8').split('\n'), 1):
        if ln.startswith('## '):
            sec = ln[3:].strip()
            continue
        if sec not in ('Next', 'Done') or not ln.startswith('|') or ln.startswith('|---'):
            continue
        c = [x.strip() for x in ln.strip().strip('|').split('|')]
        if c[0] in ('#', 'Date'):
            continue
        assert len(c) == 4 and all(c), f'site-log.md:{k}: an entry has four cells, none empty: {ln}'
        assert c[2] in SL_TONE, f'site-log.md:{k}: area {c[2]!r} is not one of {list(SL_TONE)}'
        if sec == 'Next':
            assert c[0] == str(len(nxt) + 1), f'site-log.md:{k}: Next is numbered 1, 2, 3 with no gap ({c[0]})'
            nxt.append(tuple(c))
        else:
            datetime.date.fromisoformat(c[0])   # raises on a date that is not YYYY-MM-DD
            done.append(tuple(c))
    return nxt, done


# S-DEC3: an edition that leaves out both pages does not read the site log (it is the default edition's record)
SL_NEXT, SL_DONE = site_log(R.parent / 'docs' / 'site-log.md') if not {'changelog', 'backlog'} <= OMIT else ([], [])
# newest first; on one day the entry lower in the file (written later) first
SL_DONE_SORTED = [e for _, e in sorted(enumerate(SL_DONE), key=lambda ke: (ke[1][0], ke[0]), reverse=True)]
cl_title, bl_title = 'Changelog', 'Backlog'
cl_since = f'since {short_date(min(e[0] for e in SL_DONE))}' if SL_DONE else ''


def sl_table(cls, head, rows):
    """One overview table: the column classes come from cls (one per column), so theme.css sizes each column."""
    th = ''.join(f'<th class="{c}">{html.escape(h)}</th>' for c, h in zip(cls, head))
    tb = ''.join('<tr>' + ''.join(f'<td class="{c}">{v}</td>' for c, v in zip(cls, r)) + '</tr>' for r in rows)
    return f'<div class="tbl sltbl"><table class="sl"><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>'


def sl_area(name):
    return f'<span class="sla" style="--c:{SL_TONE[name]}">{html.escape(name)}</span>'


def sl_section(name, held, body, kind):
    return (f'<section class="howto slarea" data-area="{html.escape(name)}" data-sl="{kind}" style="--hc:{SL_TONE[name]}">'
            f'<h2>{html.escape(name)}</h2><p class="slheld">{html.escape(held)}</p>{body}</section>')


cl_body = ''
for name, held, _ in SL_AREAS:
    rows = [(f'<span class="sld">{short_date(d)}</span>', f'<span class="slc">{html.escape(c)}</span>', md_inline(t))
            for d, c, a, t in SL_DONE_SORTED if a == name]
    cl_body += sl_section(name, held, sl_table(('c-date', 'c-code', 'c-text'), ('Date', 'Code', 'What happened'), rows)
                          if rows else '<p class="slnone">Nothing yet.</p>', 'done')
changelog = f"""
<section class="panel log slog" id="changelog" data-ctx="root" data-kind="changelog" data-t="{cl_title}" data-u="{html.escape(SITE_NAME.upper())}" data-c="var(--gold)" hidden>
  <header class="hero">
    {crumbs((SITE_NAME, 'home'), ('Changelog', None))}
    <div class="eyebrow"><span class="u" style="--c:var(--gold)">CHANGELOG</span> · {len(SL_DONE)} items {cl_since}</div>
    <h1>{cl_title}</h1>
    <p class="lede">What has been done, area by area, newest first: each unit written, each course started or finished, and each change to the site a reader can see. What is still to come is in the <a href="#backlog" data-target="backlog">Backlog</a>.</p>
  </header>
  {cl_body}
</section>"""
# P91 (4 Nov 2026): the home's other site pages (the backlog; the figure kinds, which has no drawer row; the changelog,
# which joins them) sit above New since, so What's new is the one link under it
site_links = ''.join(([] if 'backlog' in OMIT else [f'<a class="hbtn alt" href="#backlog" data-target="backlog"><span>Backlog</span><b>What comes next, in order and by area</b></a>'])
                  + ([] if 'figures' in OMIT else [f'<a class="hbtn alt" href="#viz-examples" data-target="viz-examples"><span>Figure kinds</span><b>Every figure a unit can declare, with its block</b></a>'])
                  + ([] if 'changelog' in OMIT else [f'<a class="hbtn alt" href="#changelog" data-target="changelog"><span>Changelog</span><b>What has been done, by area, newest first</b></a>']))
site_links = f'<div class="hlinks">{site_links}</div>' if site_links else ''

# the backlog page (S-PAGES): the overall order first, then one table per area, from docs/site-log.md's Next alone
bl_order = sl_table(('c-n', 'c-code', 'c-area', 'c-text'), ('#', 'Code', 'Area', 'What it is'),
                    [(n, f'<span class="slc">{html.escape(c)}</span>', sl_area(a), md_inline(t)) for n, c, a, t in SL_NEXT])
bl_body = ''
for name, held, _ in SL_AREAS:
    rows = [(f'<span class="slc">{html.escape(c)}</span>', md_inline(t)) for n, c, a, t in SL_NEXT if a == name]
    bl_body += sl_section(name, held, sl_table(('c-code', 'c-text'), ('Code', 'What it is'), rows)
                          if rows else '<p class="slnone">Nothing queued.</p>', 'next')
backlog = f"""
<section class="panel log slog" id="backlog" data-ctx="root" data-kind="backlog" data-t="{bl_title}" data-u="{html.escape(SITE_NAME.upper())}" data-c="var(--orange)" hidden>
  <header class="hero">
    {crumbs((SITE_NAME, 'home'), ('Backlog', None))}
    <div class="eyebrow"><span class="u" style="--c:var(--orange)">BACKLOG</span> · {len(SL_NEXT)} items next · {len(SL_DONE)} done</div>
    <h1>{bl_title}</h1>
    <p class="lede">What comes next: first everything in the order it will be done, then the same items area by area. What is done is in the <a href="#changelog" data-target="changelog">Changelog</a>.</p>
  </header>
  <h2 class="hsec">In order</h2>
  <section class="slorder" data-sl="order">{bl_order}</section>
  {bl_body}
</section>"""

# P92 (4 Nov 2026) · the home's topography (Pedro, 13:16: "SVG contours from the data, each area a rise by its words").
# viz.py's home kind "contours", declared here from the course data and drawn when the site is built. The hero: one
# rise per area of knowledge (THEMES, in order), its height the words written in its live courses (a history course's
# reports, a markdown course's reading pages, as the cards count them), a contour every HERO_INTERVAL words, in two
# fixed layouts: tall (below 1100 px; every rise inside the part of the square drawing a phone's hero shows) and wide
# (from 1100 px, across the full width beside the sidebar). Each course tile: one rise per unit of the course in its
# order (a history course's syllabus units, the audit unit left out; a markdown course's units), a written unit by its
# words, a planned one flat (a dashed ring), a contour every 5.5th part of the course's largest unit, so every tile reads at
# the same density (the spread keeps a neighbour's tail under a level, so a unit's rings rise with its words); the tile's
# numbers say the rest.
NEWEST = DATED[0] if DATED else None
# P-HERO1 (21 Nov 2026): the interval is derived, not raised by hand (W-DD-SP2 took it from 22,000 to 23,000, W-SCE1 to
# 24,000, each time the layer passed verify.py's 20 KB). HERO_INTERVAL_MIN is the floor: the hero is never drawn finer.
# 24,000 is not a measured design density: P92 drew the hero at 22,000 (kit/reviews/p92/check-hero-3.md); 24,000 is the
# value W-SCE1 raised it to by hand, frozen as the floor by decision (HK-1, 21 Nov 2026) so that no edition's hero moves
# (at 22,000 greece's and every other edition's would). At 24,000 History's 510k words stand 21 levels up, an area of 67k
# two. The rule: the hero's interval is HERO_INTERVAL_MIN, or, where the contour layer (the div.topo with both layouts,
# tall and wide, at its phase) would be more than HERO_BUDGET bytes there, the smallest whole hundred of words above it
# at which the layer is at most HERO_BUDGET, for the written units of the courses the edition being built holds. The
# bytes are verify.py's (new Blob([topo.outerHTML]).size): the layer as the browser re-serialises it, each self-closed
# <path/> and <circle/> written out with its end tag (sep_bytes), 88 B more than the source string for academy's layer.
# hero_interval: one drawing when the floor fits; else one at the coarsest interval, then a scan upward from the floor,
# one drawing (about 0.43 s) per hundred words (academy: 7 drawings, about 3 s; the bisection it replaced drew 14),
# because the layer shrinks overall as the interval grows but not at every step (academy: +5 to +87 B at six steps of
# 22,000 to 30,000), so a bisection could step over the smallest. The budget only ever raises the
# interval above the floor. HERO_BUDGET is the one place to change the budget: 23,124 B since S-NAV1 step G (19 KB before),
# so verify.py's HOME_TOPO_MAX (24,148 B; 20 KB before) stays the hard limit with 1 KB of headroom. As units are written the interval grows with the words by itself (academy, 21 Nov
# 2026: 24,500, History 20 levels, 19,388 B as verify counts; greece: 24,000, in budget).
HERO_INTERVAL_MIN = 24000   # the floor (words between two contour levels): W-SCE1's value, frozen at HK-1; P92 drew 22,000
HERO_BUDGET = 23124         # bytes of the layer as verify.py measures it (outerHTML), 1 KB under verify.py's HOME_TOPO_MAX
# S-NAV1 step G (checker finding 2; a proposal for Pedro to veto): 19 KB (19,456) until step D gave every line of the
# swell its own path and --d (and a shared line its --o): at 19 KB academy's interval rose from 24,500 to 29,000 words a
# level (History 20 -> 17 levels). No cut of those attributes that leaves the drawing unchanged fits (without any style
# at all the layer is 20,996 B at 24,500), so the budget is raised by the least that draws the hero as before: 23,124 B,
# academy's layer at 24,500 (at 24,400 it is 23,254 B, so the scan still stops at 24,500), +3,668 B; verify.py's cap
# rose by the same, 20,480 -> 24,148.
# _HERO_AT (S-DEC3: catalog.toml, each track's `hero`; kit/courses.py HERO_AT): where each area's rise stands (fractions
# of the layout's width and height), tall and wide. P92 checks: every rise inside a 390 px phone's view (x .27 to .73)
# and above the fade, each small rise closing two rings of its own (verify.py checks it), Marketing clear of the sidebar
# at both ends of the drift. P93: keyed by area, so an edition that holds fewer areas takes its areas' places
if [t['id'] for t in THEMES if t['id'] not in _HERO_AT]:
    raise SystemExit(f'catalog.toml: the tracks {[t["id"] for t in THEMES if t["id"] not in _HERO_AT]} have no `hero` (their place on the home hero): give each one')
HERO_AT = {'tall': [_HERO_AT[t['id']][0] for t in THEMES], 'wide': [_HERO_AT[t['id']][1] for t in THEMES]}
AREA_WORDS = {t['id']: sum(c['words'] for c in HISTORY if c['theme'] == t['id']) + sum(m['words'] for m in MD if m['theme'] == t['id'] and m['status'] != 'coming soon')
              for t in THEMES}
HERO_TOPO = dict(kind='contours', interval=None,   # hero_interval(), once the phase is known
                 rises=[dict(label=t['name'], tone=_TONE[t['color']], **(dict(words=AREA_WORDS[t['id']]) if AREA_WORDS[t['id']] else dict(planned=True))) for t in THEMES],
                 layouts=[dict(name='tall', width=1000, height=1000, spread=.095, at=HERO_AT['tall']),
                          dict(name='wide', width=1000, height=571, spread=.095, at=HERO_AT['wide'])])


def unit_rises(c):
    """A course's units in order for its tile's patch: (code, words or None when the unit is not written)."""
    if 'units' in c and 'umap' in c:                    # a history course: its syllabus units, the audit unit left out
        out = []
        for u, name, why, mods in c['units']:
            if u == c['audit_unit']:
                continue
            done = all(m[0] in c['done'] for m in mods)
            out.append((f'U{u}', sum(c['wby'].get(m[0], 0) for m in mods) if done else None))
        return out
    return [(u[0], m_w) for u in c['units'] for m_w in [c['wby'].get(u[0]) if u[0] in c['parent']['written'] else None]]


def tile_patch(c, phase=None):
    """The course tile's contour patch: its units in order (unit_rises), by patch_block."""
    us = unit_rises(c)
    if not any(w for _, w in us):
        return ''
    return patch_block(us, _TONE[c['color']], phase)


def ghost_tile(theme, short, name, col, scope, spine, phase=None, label='Spine'):
    """P93: a planned course on the home, a ghost tile (the chip, the title, its scope in two lines, no stats, a
    dashed patch: one flat ring, nothing written), the summary of a disclosure that opens to its spine, its scope then
    shown whole (theme 4h), as the planned course's row showed both."""
    return tile([theme, short], col, name, html.escape(scope), patch=patch_block([(short, None)], _TONE[col], phase),
                disclosure=f'<p class="nspine"><span>{html.escape(label)}</span>{html.escape(spine)}</p>', cls=' ghost')


def md_card(m, phase=None):
    return card(THEME[m['theme']]['name'], m['color'], f'Course {m["key"]}', m['name'], html.escape(m['tile']), m['nwritten'], m['nunits'], m['words'], m['status'], f'#{m["home_id"]}', patch=tile_patch(m, phase))


# P93: the home's drawings in page order (the hero, each live course's tile, each track's planned courses), each
# starting at its own point of the cycle
PLANNED = {t['id']: ([] if 'planned' in OMIT else t.get('planned', [])) for t in THEMES}   # S-SPORTS: a track's own planned courses (P-DEC12: History's too, the `next` rows before)
HOME_PH = iter(phases(1 + (len(THEMES) if MULTI else len(HISTORY) + sum(1 for m in MD if m['status'] != 'coming soon') + sum(len(v) for v in PLANNED.values()))))   # G-0: one phase per drawing on the home; a course with nothing filed has none; S-NAV1 step B: with area pages, the hero and one tile per track
HERO_TOPO['phase'] = round(next(HOME_PH), 3)


def hero_interval(topo, step=100):
    """P-HERO1: HERO_INTERVAL_MIN if the layer viz.render(topo) draws there is at most HERO_BUDGET bytes as verify.py
    measures it (sep_bytes: the outerHTML the browser writes, every self-closed element with its end tag); else the
    smallest whole `step` of words above it at which it is, found by a scan upward from the floor (the size is not
    monotone in the interval, so no bisection), after one drawing at the largest area's words rounded up (where every
    rise stands at most one level) proves some interval fits; returns (interval, the layer drawn at it)."""
    drawn = {}
    def fits(k):
        if k not in drawn:
            drawn[k] = viz.render(dict(topo, interval=k * step))
        return sep_bytes(drawn[k]) <= HERO_BUDGET
    lo = HERO_INTERVAL_MIN // step   # a whole number of steps
    if fits(lo):
        return lo * step, drawn[lo]
    top = max(lo + 1, -(-max((r.get('words', 0) for r in topo['rises']), default=0) // step))
    if not fits(top):
        raise SystemExit(f'the home hero\'s contour layer is {sep_bytes(drawn[top]):,} bytes (outerHTML) at {top * step:,} words a level, over HERO_BUDGET ({HERO_BUDGET:,}): no interval keeps it in budget')
    # the scan draws each step from the floor up (about 0.43 s per 100 words): 7 drawings at 24,500, about 62 (27 s) at
    # 30,000. Size is not strictly falling as the interval grows, so a bisection could skip the smallest fit (HK-1 M1).
    k = next(k for k in range(lo + 1, top + 1) if fits(k))
    return k * step, drawn[k]


HERO_INTERVAL, hero_topo = hero_interval(HERO_TOPO)
HERO_TOPO['interval'] = HERO_INTERVAL
def track_body(t, ph):
    """A track's course tiles, its own copy and its folded planned courses, and its count line, each drawing taking the
    next phase of ph in page order (its history courses' tiles, its planned courses' ghosts, its markdown courses'
    tiles: the order the home has drawn them in since P93). Returns (the tiles, the copy and planned list, the count,
    the courses: [(label, words or None)] its history and live markdown courses by their words, its coming-soon markdown
    courses and its planned courses flat)."""
    hist = [c for c in HISTORY if c['theme'] == t['id']]
    mds = [m for m in MD if m['theme'] == t['id']]
    cards = ''.join(root_card(c, next(ph)) for c in hist)
    own_cards = ''.join(ghost_tile(t['name'], short, name, col, scope, spine, next(ph), t.get('planned_label', 'Spine')) for short, name, col, scope, spine in PLANNED[t['id']])
    soon = [m for m in mds if m['status'] == 'coming soon']   # a markdown course with nothing written is planned, not live
    # G-0 (12 Nov 2026): such a course has no tile on the home (verify.py's home_expect: "a course with nothing filed is
    # not live: no tile"; its patch would be empty); it is counted as coming soon here and listed in the drawer
    cards += ''.join(md_card(m, next(ph)) for m in mds if m not in soon)
    n = len(hist) + len(mds) - len(soon)
    count = f'{n} course{"s" if n != 1 else ""}' if n else f'{len(soon)} course{"s" if len(soon) != 1 else ""} coming soon'
    if hist: count += f' · {sum(c["nrep"] for c in hist)} reports'
    if mds: count += f' · {sum(m["nwritten"] for m in mds)} of {sum(m["nunits"] for m in mds)} units'
    if soon and n: count += f' · {len(soon)} coming soon'
    if PLANNED[t['id']]: count += f' · {len(PLANNED[t["id"]])} ' + (f'more {t["planned_heading"].lower()}' if t.get('planned_heading') else 'planned')   # S-SCE0: a track may call its planned courses "coming soon"
    # P-DEC12: a track's own copy is the page its catalog.toml `extra` names (raw HTML, the file's text less its final
    # newline), shown above its planned courses; the History track's "Why history and myth together" is pages/track-history.md
    extra = '\n' + cpath(t, 'extra').read_text(encoding='utf-8').removesuffix('\n') if t.get('extra') else ''
    if PLANNED[t['id']]:   # S-SPORTS: a track's own planned courses, folded; P-DEC12: History's too (the `next` rows before), its anchor `planned_anchor`
        extra += f"""
  <details class="howto rules planned" id="{t.get('planned_anchor', 'planned-' + t['id'])}">
    <summary><h2>{html.escape(t.get('planned_heading', 'Planned'))}</h2><span>{len(PLANNED[t['id']])} courses, in the intended order</span></summary>
    <p class="hnote">{html.escape(t.get('planned_note', ''))}</p>
    <div class="cgrid">{own_cards}</div>
  </details>"""   # own_planned
    live = [m for m in mds if m not in soon]
    rises = ([(c['short'], c['words'] or None) for c in hist] + [(m['short'], m['words'] or None) for m in live]
             + [(m['short'], None) for m in soon] + [(short, None) for short, *_ in PLANNED[t['id']]])
    units = (sum(c['units_complete'] for c in hist) + sum(m['nwritten'] for m in live), sum(c['card_units'] for c in hist) + sum(m['nunits'] for m in live))
    return cards, extra, count, rises, dict(n=n, units=units, words=sum(c['words'] for c in hist) + sum(m['words'] for m in live),
                                            status='complete' if all(c['status'] == 'available' for c in hist) and all(m['status'] == 'available' for m in live) and not soon and not PLANNED[t['id']] else 'in progress')


tracks = ''
AREA_PANELS = []
if not MULTI:   # an edition of one track: the home lists its courses under the track's header, as before S-NAV1
    for t in THEMES:
        cards, extra, count, _, _ = track_body(t, HOME_PH)
        tracks += f"""
  <section class="track" id="track-{t['id']}" style="--c:{t['color']}">
    <header class="thead"><div class="ttx"><span class="cname">Track</span><h2>{html.escape(t['name'])}</h2><p>{html.escape(t['lede'])}</p></div><span class="tmeta">{count}</span></header>
    <div class="cgrid">{cards}</div>{extra}
  </section>"""
else:
    # S-NAV1 step B: the home shows one tile per track (the chip "Area" and its name, the status pill, the name, its
    # lede in two lines, three stats: its live courses, their units written and in all, and its patch: one rise per
    # course of the track, a live course by its words, a course coming soon or planned flat); each tile opens the area
    # page, track-<id>: a hero over the same courses' topography (crumbs Home › Area, the eyebrow AREA with its count, the
    # name, the lede, three stats), then the track's band: its course tiles, its own copy and its folded planned courses,
    # as the home showed them before. Each page's drawings take their phases in page order (the hero first, at 0).
    area_tiles = ''
    for t in THEMES:
        aph = iter(phases(1 + sum(1 for c in HISTORY if c['theme'] == t['id']) + sum(1 for m in MD if m['theme'] == t['id'] and m['status'] != 'coming soon') + len(PLANNED[t['id']])))
        hero_ph = next(aph)
        cards, extra, count, rises, st = track_body(t, aph)
        top = max((w for _, w in rises if w), default=0)
        tone = _TONE[t['color']]
        layer = hero_layer(rises, tone, top / 5.5, course_topo(html.escape(t['lede'])), hero_ph) if top else ''
        aid = 'track-' + t['id']
        AREA_PANELS.append(f"""
<section class="panel home area" id="{aid}" data-ctx="root" data-kind="area" data-t="{html.escape(t['name'])}" data-u="AREA" data-c="{t['color']}" style="--cc:{t['color']}" hidden>
  <header class="hero has-topo">
    {layer}
    {crumbs((SITE_NAME, 'home'), (t['name'], None))}
    <div class="eyebrow">{eyebrow_segs(f'<span class="u" style="--c:{t["color"]}">AREA</span>', *count.split(' · '))}</div>
    <h1>{html.escape(t['name'])}</h1>
    <p class="lede">{html.escape(t['lede'])}</p>
    <div class="stats" data-n="3"><div><b>{st['n']}</b><span>course{"s" if st['n'] != 1 else ""}</span></div><div><b>{st['units'][0]}</b><span>of {st['units'][1]} units written</span></div><div><b>{hours(st['words'])}</b><span>hours of reading</span></div></div>
  </header>
  <section class="track" style="--c:{t['color']}">
    <div class="cgrid">{cards}</div>{extra}
  </section>
</section>""")
        area_tiles += tile(['Area', t['name']], t['color'], t['name'], html.escape(t['lede']),
                           stats=[(st['n'], 'courses' if st['n'] != 1 else 'course'), (st['units'][0], 'units written'), (st['units'][1], 'in all')],
                           pill=status_pill(st['status']), patch=patch_block(rises, tone, next(HOME_PH)) if top else '', href='#' + aid)
    tracks = f"""
  <div class="cgrid areas">{area_tiles}</div>"""

# What's new (P91): every unit filed and every course started, newest first, grouped by day; and its first six rows
# as New since at the foot of the home
def _model(m):
    """A model's name with its version held to it (Opus 5.5 never breaks as Opus / 5.5); a long provenance still wraps."""
    return re.sub(r'\b(Opus|Fable|Sonnet|Haiku) (\d)', r'\1&nbsp;\2', html.escape(m))


def new_row(x, home=False):
    """One row of What's new (home=False: the code in the first column, the day is the group's heading) or of New
    since (home=True: the day in the first column). A unit row links to its page, a course row to the course home."""
    ap = ' <span class="approx" title="Its work session ran over several days; this is the session\'s first day">≈ date approximate</span>' if x['approx'] else ''
    day = ('≈ ' if x['approx'] else '') + short_date(x['date']).rsplit(' ', 1)[0]
    if x['kind'] == 'course':
        tgt, n = x['home'], (day if home else 'Start')
        t = f'{html.escape(x["title"])}<small>Course started · first {"report" if x["hist"] else "unit"} {html.escape(x["first"])}{" · " + _model(x["model"]) if x["model"] else ""}{ap}</small>'
        pill = '<span class="pill prog">course</span>'
    else:
        tgt, n = x['pid'], (day if home else html.escape(x['code']))
        t = (f'{html.escape(x["code"]) + " · " if home else ""}{html.escape(x["title"])}'
             f'<small>{html.escape(x["course"])}{" · " + _model(x["model"]) if x["model"] else ""}{ap}</small>')
        pill = f'<span class="pill live">{"report" if x["hist"] else "unit"}</span>'   # P91 check: a history course's units hold reports
    return (f'<a class="hrow" href="#{tgt}" data-target="{tgt}" data-kind="{x["kind"]}" data-date="{x["date"]}"{" data-approx" if x["approx"] else ""} '
            f'style="--c:{x["color"]}"><span class="n">{n}</span><span class="t">{t}</span>{pill}</a>')
recent_rows = ''.join(new_row(x, True) for x in RECENT)
_days = []
for x in WHATSNEW:
    if not _days or _days[-1][0] != x['date']:
        _days.append((x['date'], []))
    _days[-1][1].append(x)
nu = sum(1 for x in WHATSNEW if x['kind'] == 'unit' and not x['hist'])
nr = sum(1 for x in WHATSNEW if x['kind'] == 'unit' and x['hist'])
nc = sum(1 for x in WHATSNEW if x['kind'] == 'course')
# P93: What's new's topography (Pedro: "expand that to other pages"): one rise per day it lists, oldest at the left,
# its height the words filed that day (the units' and reports' words, as the cards count them), a contour every
# NEW_INTERVAL words (P-DEC15: new_interval, a tenth of the largest day in an edition whose largest is under 110,000),
# along a ridge; each day's rise in the tone of the course that filed the most words that day, as its rows carry their
# courses' tones
NEW_DAYS = [(d, sum(x['words'] for x in xs if x['kind'] == 'unit')) for d, xs in reversed(_days)]
def _day_tone(xs):
    by = {}
    for x in xs:
        if x['kind'] == 'unit':
            by[x['color']] = by.get(x['color'], 0) + x['words']
    return _TONE[max(by, key=by.get)]
NEW_TONES = [_day_tone(xs) for d, xs in reversed(_days)]
new_layer = hero_layer(NEW_DAYS, NEW_TONES, new_interval(max(w for _, w in NEW_DAYS)), NEW_TOPO) if NEW_DAYS else ''
whatsnew = f"""
<section class="panel log" id="new" data-ctx="root" data-kind="new" data-t="What's new" data-u="{html.escape(SITE_NAME.upper())}" data-c="var(--gold)" hidden>
  <header class="hero has-topo">
    {new_layer}
    {crumbs((SITE_NAME, 'home'), ("What's new", None))}
    <div class="eyebrow">{eyebrow_segs(*['<span class="u" style="--c:var(--gold)">WHAT\'S NEW</span>', f'{nr} history reports', f'{nu} units', f'{nc} courses'] + ([f'since {howbuilt.date_long(WHATSNEW[-1]["date"])}'] if WHATSNEW else []))}</div>
    <h1>What's new</h1>
    <p class="lede">Every unit and every history report filed, and every course started, newest first, by the day it was filed. A history report is dated by the work session that filed it; where that session ran over several days, by its first day, marked ≈. What else was done is in the Changelog.</p>
  </header>
  {''.join(f'<section class="newday" data-day="{d}"><h2 class="hsec">{short_date(d)}</h2><div class="hrows">{"".join(new_row(x) for x in xs)}</div></section>' for d, xs in _days)}
</section>"""
# P92 (4 Nov 2026) · the hero's area line (Pedro: the area word cycling under "Academy", each in its colour): the four
# areas of knowledge stacked in one cell, shown in turn by the theme's keyframes (opacity and transform, no script),
# hidden from a screen reader, which reads the static line after it; under reduced motion the static line shows and
# nothing moves. And the quiet link to What's new, naming the newest unit and its day, as P91's shelf label did.
hero_areas = ('<p class="harea" aria-hidden="true">' + ''.join(f'<span class="harea-w" style="--c:{t["color"]};--k:{k}">{html.escape(t["name"])}</span>' for k, t in enumerate(THEMES)) + '</p>'
              + '<p class="harea-all">' + '<span class="harea-dot"><span aria-hidden="true">&nbsp;·</span><span class="hsr">,</span> </span>'.join(f'<span style="--c:{t["color"]}">{html.escape(t["name"])}</span>' for t in THEMES) + '</p>')
_sep = '<span aria-hidden="true"> ·</span><span class="hsr">,</span> '   # P92 check: the dot never read aloud; a comma for the pause
hero_new = (f'<a class="hnew" href="#new" data-target="new"><span>What\'s new{_sep}{html.escape(NEWEST["code"])}{_sep}{short_date(NEWEST["date"]).rsplit(" ", 1)[0]}</span>'
            '<span class="hnew-a" aria-hidden="true">→</span></a>') if NEWEST else ''
new_link = '<div class="hlinks" data-one><a class="hbtn alt" href="#new" data-target="new"><span>What\'s new</span><b>Every unit and report filed and every course started, by day</b></a></div>'
# "How every course works": the constants (S-DEC3: the brand's [[rules]], or the edition's own; brands/academy.toml says
# how). P80 (1 Nov 2026): a line that names a course the edition does not hold is never shown: its first alt that fits
# is, and a line with nothing that fits stops the build.
_HELD = {c['id'] for c in COURSES}
_FAMS = {c['family'] for c in COURSES}
def _fits(v):
    return set(v.get('names', ())) <= _HELD and ('families' not in v or _FAMS <= set(v['families']))
def _rule(line):
    for v in [line] + line.get('alt', []):
        if _fits(v):
            return v['text']
    raise SystemExit(f'edition {EDITION!r}: the rules line {line["head"]!r} names a course the edition does not hold and has no alt that fits: '
                     f'give it one in brands/{ED["brand"]}.toml or the edition its own [[rules]]')
RULE_LINES = ED.get('rules') or B['rules']
if not RULE_LINES:
    raise SystemExit(f'edition {EDITION!r}: no rules lines in brands/{ED["brand"]}.toml or in the edition')
RULES = '\n'.join(f'      <li><strong>{r["head"]}</strong> {_rule(r)}</li>' for r in RULE_LINES)
roothome = f"""
<section class="panel root" id="home" data-ctx="root" data-kind="root" data-t="{html.escape(SITE_NAME)}" data-u="HOME" data-c="var(--red)" hidden>
  <header class="hero hhome">
    {hero_topo}
    <div class="hcopy">
      <h1>{html.escape(SITE_NAME)}</h1>
      {hero_areas}
      <p class="lede">{B['lede']}</p>
      {hero_new}
    </div>
  </header>
  {tracks}

  <details class="howto rules">
    <summary><h2>How every course works</h2><span>the constants</span></summary>
    <ol>
{RULES}
    </ol>
  </details>
  {site_links}
{f'''
  <section class="recent">
    <h2 class="hsec">New since {short_date(RECENT[-1]['date']).rsplit(' ', 1)[0] if RECENT else ''}</h2>
    <div class="hrows">{recent_rows}</div>
  </section>
  {new_link}''' if recent_rows else ''}
</section>"""

# A4 · "How it was built": one generated page per course (howbuilt.py), every fact read from a file
for c in HISTORY:
    c['built'] = howbuilt.history_page(c, crumbs, THEME, md_inline, md_blocks, flagged, unchecked)
for m in MD:
    m['panels'].append(howbuilt.markdown_page(m, crumbs, THEME, md_inline, md_blocks))

panels = [roothome, *AREA_PANELS, changelog, backlog]   # S-NAV1 step B: the area pages, in the shell (no fetch), after the home
for c in HISTORY:
    panels += [course_home(c), c['built'], syllabus(c)] + c['report_panels']
for m in MD:
    panels += m['panels']
if OMIT:   # P70: an edition leaves out these panel kinds
    panels = [p for p in panels if re.search(r' data-kind="([^"]+)"', p).group(1) not in OMIT]

# A2 · the split: every report panel (a history report, a markdown course's reading page) leaves the shell, and so
# (P20) does every syllabus and a markdown course's briefs and bibliography pages, and (P22) every history course
# home (<ctx>/home.html). A panel that leaves carries data-split="<stem>" from its builder; the shell keeps an empty
# stub with the panel's attributes and data-src, the file's path relative to the shell (<ctx>/<stem>.html); the
# panel's inner HTML becomes that file, fetched by shell.js on navigation. A stub that is not a report also carries
# data-anchors, the ids inside its file, so a link into it (#rs-u3, #b-a2, #greece-u3) can load it first.
SITE = R / ED['site']
REPORTS = {}
def split(p):
    s = p.strip()
    head = s[:s.index('>') + 1]
    m = re.search(r' data-split="([^"]+)"', head)
    if not m:
        return p
    pid, ctx = re.search(r' id="([^"]+)"', head).group(1), re.search(r' data-ctx="([^"]+)"', head).group(1)
    assert head.endswith(' hidden>') and s.endswith('</section>'), pid
    src = f'{ctx}/{m.group(1)}.html'
    assert src not in REPORTS, src
    body = s[len(head):-len('</section>')].strip() + '\n'
    REPORTS[src] = body
    head = head.replace(m.group(0), '')
    ids_in = re.findall(r' id="([^"]+)"', body)
    anchors = '' if ' data-kind="report"' in head else f' data-anchors="{" ".join(ids_in)}"'
    return '\n' + head[:-len(' hidden>')] + f' data-src="{src}"{anchors} hidden></section>'
panels = [split(p) for p in panels]
import shutil
if SITE.exists():
    shutil.rmtree(SITE)   # a file that left the build must leave the site too
for src, body in REPORTS.items():
    (SITE / src).parent.mkdir(parents=True, exist_ok=True)
    (SITE / src).write_text(body)
# V1 · the figure examples page (viz_examples.py): one figure of every kind, fetched like a report from the shell's root
if 'figures' not in OMIT:
    panels.append(viz_examples.write(SITE, crumbs))
# P91 · What's new, a page beside the shell like the Figure kinds page (academy/new.html, fetched on navigation), so its
# rows (every unit and course) never weigh on the shell; second in the panel order, after the home
_wn_head = whatsnew.strip()[:whatsnew.strip().index('>') + 1]
_wn_body = whatsnew.strip()[len(_wn_head):-len('</section>')].strip() + '\n'
(SITE / 'new.html').write_text(_wn_body)
panels.insert(1, '\n' + _wn_head[:-len(' hidden>')] + f' data-src="new.html" data-anchors="{" ".join(re.findall(r' id="([^"]+)"', _wn_body))}" hidden></section>')
# G-0 (12 Nov 2026) · the changelog leaves the shell too (academy/changelog.html, fetched on navigation, like What's new):
# at 422 KB it was the largest panel, and with it the shell stood 7 KB under its 1 MB limit, so the next unit filed
# would have failed verify.py's size check
if 'changelog' not in OMIT:
    _k = next(i for i, p in enumerate(panels) if re.match(r'\s*<section class="panel[^"]*" id="changelog"', p))
    _cl = panels[_k].strip()
    _cl_head = _cl[:_cl.index('>') + 1]
    _cl_body = _cl[len(_cl_head):-len('</section>')].strip() + '\n'
    (SITE / 'changelog.html').write_text(_cl_body)
    panels[_k] = '\n' + _cl_head[:-len(' hidden>')] + f' data-src="changelog.html" data-anchors="{" ".join(re.findall(r' id="([^"]+)"', _cl_body))}" hidden></section>'

# S-NAV1 step C (21 Nov 2026): the navigation is two levels, built once, each a single element with stable classes, so
# S-NAV2 places them with CSS alone: nav.main-nav, Home and the areas (THEMES, catalog order), and nav.sub-nav, the
# section the reader is in, one group (.sub-sec, data-navctx) per section, of which shell.js shows the current one: an
# area page's courses (data-navctx track-<id>), a course's pages and units (data-navctx the course's ctx); none on the
# home or the site pages under it (What's new, the Changelog, the Backlog, Figure kinds), which the home's foot links.
# Both sit in the drawer's list (.dlist), as the one root list and the course lists did. An edition of one track has
# no area page: its area entry goes to the track's band on the home (#track-<id>, the home's own section), and it has
# no area group in the sub-nav. Each area entry names the course sections it holds (data-secs), so shell.js marks the
# area the reader is in.
def area_courses(t):
    """The track's group of the sub-nav, shown on its area page: its live courses (history, then markdown, as the area
    page's tiles) and, where the track asks for it (`planned_drawer`), its planned courses folded under them."""
    hist = [c for c in HISTORY if c['theme'] == t['id']]
    mds = [m for m in MD if m['theme'] == t['id']]
    out = ''.join(f'<a class="ditem dcourse" href="#{c["home_id"]}" data-target="{c["home_id"]}" style="--c:{c["color"]}"><span class="n">{c["num"]}</span><span class="t">{c["short"]}<small>{c["card_units"]} units · {c["nrep"]} {"reports" if c["status"] == "available" else "of " + str(c["content_mods"]) + " reports"}</small></span></a>' for c in hist)
    out += ''.join(f'<a class="ditem dcourse" href="#{m["home_id"]}" data-target="{m["home_id"]}" style="--c:{m["color"]}"><span class="n">{m["key"]}</span><span class="t">{html.escape(m["short"])}<small>{m["nwritten"]} of {m["nunits"]} units</small></span></a>' for m in mds)
    n = len(hist) + len(mds)
    if t.get('planned_drawer') and PLANNED[t['id']]:
        # P-DEC12: a track's planned courses (catalog.toml `planned_drawer`, History's) fold into one row, numbered on
        # from the track's courses; open it to see them in order
        out += (f'<details class="dplan"><summary class="dsoon"><span class="n">+{len(PLANNED[t["id"]])}</span><span class="t">planned, in order</span>{ICON_CHEV}</summary>'
                + ''.join(f'<div class="dsoon" style="--c:{col}"><span class="n">{k + n + 1}</span><span class="t">{html.escape(s)}</span><span class="pill">soon</span></div>' for k, (s, _, col, _, _) in enumerate(PLANNED[t['id']])) + '</details>')
    return f'<div class="sub-sec" data-navctx="track-{t["id"]}" role="group" aria-label="{html.escape(t["name"])} courses" style="--c:{t["color"]}" hidden><div class="ditems">{out}</div></div>'

def main_item(t):
    secs = ' '.join([c['id'] for c in HISTORY if c['theme'] == t['id']] + [m['id'] for m in MD if m['theme'] == t['id']])
    return (f'<a class="ditem darea" href="#track-{t["id"]}" data-target="track-{t["id"]}" data-secs="{secs}" style="--c:{t["color"]}">'
            f'<span class="n">■</span><span class="t">{html.escape(t["name"])}</span></a>')

main_nav = ('<nav class="main-nav" aria-label="Main"><a class="ditem dhome" href="#home" data-target="home"><span class="n">⌂</span><span class="t">Home</span></a>'
            + ''.join(main_item(t) for t in THEMES) + '</nav>')
sub_nav = ('<nav class="sub-nav" aria-label="In this section" hidden>' + (''.join(area_courses(t) for t in THEMES) if MULTI else '')
           + ''.join(drawer(c) for c in HISTORY) + ''.join(m['nav'] for m in MD) + '</nav>')
navs = f'<div class="dlist">{main_nav}{sub_nav}</div>'

CSS = open(R / 'shell.css').read()
# S-DEC3: the brand's tokens, appended to the theme as CSS custom properties ([tokens] both themes, [tokens_light] light)
def _decl(t):
    return ';'.join(f'--{k}:{v}' for k, v in t.items())
if B['tokens']:
    CSS += f':root{{{_decl(B["tokens"])}}}\n'
if B['tokens_light']:
    CSS += (f'@media (prefers-color-scheme:light){{:root:not([data-theme="dark"]){{{_decl(B["tokens_light"])}}}}}\n'
            f':root[data-theme="light"]{{{_decl(B["tokens_light"])}}}\n')
# S-DEC3: shell.js names its localStorage keys as __STORE_<KEY>__; the brand's [storage] fills them
STORE = B['storage']
JS = open(R / 'shell.js').read()
for _k, _v in STORE.items():
    JS = JS.replace(f'__STORE_{_k.upper()}__', _v)
assert '__STORE_' not in JS, 'shell.js names a storage key the brand does not give'
# S-DEC5: a brand with `strip_comments = true` leaves the comments of design/theme.css (shell.css) and shell.js out of its
# shell: they are the maintainer's notes (dates, rows, private names). A brand without it (academy) keeps them, byte for byte
if B.get('strip_comments', True):
    CSS = re.sub(r'/\*.*?\*/', '', CSS, flags=re.S)
    JS = re.sub(r'^[ \t]*//[^\n]*\n', '', JS, flags=re.M)   # whole-line comments only: a // inside a line may be a string

page = f'''<meta charset="utf-8">
<title>{ED['title']}</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="{B['fonts_href']}">
<style>{CSS}</style>
<script>try{{var t=localStorage.getItem('{STORE['theme']}');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<header class="top">
  <div class="top-in">
    <button class="ib" id="menuB" type="button" aria-label="Open contents" aria-expanded="false" aria-controls="drawer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <a class="ib" id="homeB" href="#home" aria-label="{html.escape(SITE_NAME)} home"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h5v-6h4v6h5V10"/></svg></a>
    <div class="cur" id="cur"><span class="cur-u" id="curU"></span><span class="cur-t" id="curT"></span></div>
    <button class="ib" id="themeB" type="button" aria-label="Switch theme"><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
    <div class="arrows" id="arrows">
      <button class="ib" id="prevB" type="button" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg></button>
      <button class="ib" id="nextB" type="button" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg></button>
    </div>
  </div>
</header>
<div class="backdrop" id="backdrop"></div>
<aside class="drawer" id="drawer" aria-hidden="true" aria-label="Contents">
  <div class="dhead"><div class="brand">{B['mark']}</div><button class="ib" id="closeB" type="button" aria-label="Close contents"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
  {navs}
</aside>
<main>
{''.join(panels)}
</main>
<script>{JS}</script>
'''
# P70: in an edition, a link to a page it lacks is not a link: a navigation button or row to it is dropped, any other
# link (a pointer in a report's text into a course the edition does not hold) is kept as its plain text
if EDITION != DEFAULT_EDITION:
    _ids = set(re.findall(r' id="([^"]+)"', page)) | {i for b in REPORTS.values() for i in re.findall(r' id="([^"]+)"', b)}
    _nav = re.compile(r'<a class="(?:[^"]*\b(?:hbtn|ditem|hrow)\b[^"]*)"[^>]* href="#([^"]+)"[^>]*>.*?</a>', re.S)
    _any = re.compile(r'<a\b[^>]* href="#([^"]+)"[^>]*>(.*?)</a>', re.S)
    def _unlink(s):   # the markup only: the shell's scripts build links of their own and are left as they are
        parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
        for k in range(0, len(parts), 2):
            parts[k] = _nav.sub(lambda mm: mm.group(0) if mm.group(1) in _ids else '', parts[k])
            parts[k] = _any.sub(lambda mm: mm.group(0) if mm.group(1) in _ids else mm.group(2), parts[k])
        return ''.join(parts)
    page = _unlink(page)
    for src, body in REPORTS.items():
        (SITE / src).write_text(_unlink(body))
SITE.mkdir(parents=True, exist_ok=True)
(SITE / 'index.html').write_text(page)
OLD = R / 'personal-mythology.html'   # the single-file page before the split (A2); gone for good
if OLD.exists():
    OLD.unlink()

# the size table in README.md (between the markers), regenerated on every build; verify.py checks it against the files
def kb(n):
    return f'{n / 1024:,.0f} KB' if n < 1024 * 1024 else f'{n / 1024 / 1024:.2f} MB'
rows = [('Shell (`index.html`)', 1, len(page.encode()), len(page.encode()), 'home, drawer, the build pages of the markdown courses, backlog')]
for ctx, name in [(c['id'], c['short']) for c in HISTORY] + [(m['id'], m['short']) for m in MD]:
    fs = [len(v.encode()) for k, v in REPORTS.items() if k.startswith(ctx + '/')]
    big = max(((len(v.encode()), k) for k, v in REPORTS.items() if k.startswith(ctx + '/')), default=(0, ''))
    rows.append((f'{name} (`{ctx}/`)', len(fs), sum(fs), big[0], f'largest `{big[1]}`' if big[1] else ''))
_root = sorted((len(f.read_bytes()), f.name) for f in SITE.glob('*.html') if f.name != 'index.html')   # V1: pages beside the shell
if _root:
    rows.append(('Root pages (`./`)', len(_root), sum(n for n, _ in _root), _root[-1][0], f'largest `{_root[-1][1]}`'))
allb = sum(r[2] for r in rows)
SIZE_TABLE = ('| Part | Files | Total | Largest file | Note |\n|---|---|---|---|---|\n'
              + ''.join(f'| {a} | {n} | {kb(t)} | {kb(l)} | {note} |\n' for a, n, t, l, note in rows)
              + f'| Whole site | {sum(r[1] for r in rows)} | {kb(allb)} | | the artifact page is capped at 16 MB; the shell must stay under 1 MB |\n')
readme = (R / 'README.md').read_text(encoding='utf-8')
readme = re.sub(r'(<!-- sizes:start -->\n).*?(<!-- sizes:end -->)', lambda mm: mm.group(1) + SIZE_TABLE + mm.group(2), readme, flags=re.S)
if EDITION == DEFAULT_EDITION:   # P70: the repo's files are the full Academy's; an edition writes only its folder
    (R / 'README.md').write_text(readme, encoding='utf-8')

# S-NOAUDIT (15 Nov 2026): the Fable review queue (FABLE-REVIEW.md) and the review_due.py line are retired with the Fable stage
if EDITION == DEFAULT_EDITION:
    from biblio import write_all as _biblio
    print(f'bibliography: {_biblio()} unit files')
else:
    print(f'edition {EDITION}: {SITE.relative_to(R)}')
print(' · '.join(f"{c['short']}: {c['nrep']}/{c['content_mods']} reports, {c['words']:,} words" for c in HISTORY)
      + ''.join(f" · {c['short']}: {c['nwritten']}/{c['nunits']} units" for c in MARKDOWN), f'· shell {kb(len(page.encode()))}, {len(REPORTS)} fetched files, site {kb(allb)}')
if '--epub' in sys.argv:
    import epub
    _mdu = []
    for c in MARKDOWN:
        _order = [u[0] if isinstance(u, (tuple, list)) else u for u in getattr(c['hub'], 'ORDER', [])]
        for code, (f, fm) in sorted(c['vault_units'].items(), key=lambda kv: _order.index(kv[0]) if kv[0] in _order else 999):
            _mdu.append((c, code, fm.get('title', code), f))
    epub.write(EDITION, ED, HISTORY, _mdu, B)
