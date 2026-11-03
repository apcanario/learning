"""Assemble the Academy site in academy/ from the course data in courses.py: academy/index.html, the shell (home,
drawer, course homes, build pages, changelog, backlog), and one file per report, fetched by the shell on navigation
(docs/academy.md A2): academy/<course>/r-<id>.html for a history report, academy/<course>/<reading id>.html for a
markdown course's reading page. Since P20 each syllabus (academy/<course>/syllabus.html) and a markdown course's briefs
and bibliography pages (academy/<course>/briefs.html, bibliography.html) are fetched the same way. The size table in
README.md is regenerated on every build.

The root home is Academy (docs/academy.md, A1): every course of both families. History courses (Greece, Rome) are
built from their kit folders; a markdown course (Brand + AI) is built by mdcourse.py from its data file
(generator/data/<slug>/hub.py, AD5) into one Academy course per course in that file (AD6, A3): a course home, a
reading page per written unit, and the "How it is built" pages (method, build order, briefs, audits, bibliography,
changelog). The site also renders the Project's backlog and chat changelog (docs/) as a Backlog page.

Each course has a syllabus file, its reports in the vault (courses/<course>/, Markdown since P71-3; vault.py), a prompts index (the modules with a written report),
a colour and a short name. Greece keeps its original panel ids (#greece, #syllabus, #m23); later courses
are namespaced (#rome, #rome-syllabus, #rm01).
"""
import json, re, html, pathlib, importlib.util
import markdown
from courses import COURSES, HISTORY, MARKDOWN, NEXT, THEMES, EDITIONS
import sys
# P70: an edition filters the course list here, before anything renders; the full Academy is the edition 'academy'
EDITION = sys.argv[sys.argv.index('--edition') + 1] if '--edition' in sys.argv else 'academy'
if '--epub' in sys.argv:   # P71 (2): `--epub <edition>` builds that edition, then its EPUB (epub.py)
    EDITION = sys.argv[sys.argv.index('--epub') + 1]
if EDITION not in EDITIONS:
    raise SystemExit(f'no edition {EDITION!r} in courses.py EDITIONS: {", ".join(EDITIONS)}')
ED = EDITIONS[EDITION]
OMIT = set(ED['omit'])
if ED['courses'] is not None:
    COURSES = [c for c in COURSES if c['id'] in ED['courses']]
    HISTORY = [c for c in HISTORY if c['id'] in ED['courses']]
    MARKDOWN = [c for c in MARKDOWN if c['id'] in ED['courses']]
    _tracks = {c['theme'] for c in HISTORY} | {tr for c in MARKDOWN for tr, _ in c['tracks'].values()}
    THEMES = [t for t in THEMES if t['id'] in _tracks]
if 'planned' in OMIT:
    NEXT = []
import mdcourse
import vault
import howbuilt
import viz
import viz_examples

R = pathlib.Path(__file__).resolve().parent
PROV = json.load(open(R / 'provenance.json'))
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
    syl = (R / c['syllabus']).read_text()
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
    idx = json.load(open(R / c['prompts']))
    c['index'] = {k: idx[k] for k in order if k in idx}
    c['done'] = set(c['index'])
    c['first'] = next(iter(c['index']), None)  # the first written report, where a new reader starts (None in a new course)
    c['prov'] = PROV.get(c['id'], {})
    c['slug'] = lambda i, p=c['prefix']: p + i.replace('.', '')

    panels, total = [], 0
    ucol = c['unit_colors']
    for i, meta in c['index'].items():
        frag = vault.report_html(c, i)   # P71-3: the report's Markdown in the vault, rendered to its fragment, figures drawn
        # strip anything that violates the fragment contract
        frag = re.sub(r'<(/?)(html|head|body|!doctype[^>]*)>', '', frag, flags=re.I)
        frag = re.sub(r'<style.*?</style>|<script.*?</script>', '', frag, flags=re.S | re.I)
        frag = re.sub(r'\sstyle="[^"]*"', '', frag)
        u = i.split('.')[0]
        n = wc(frag); total += n
        sl = c['slug'](i)
        frag_ids = []
        def addid(m):
            t = m.group(1)
            sid = f'{sl}-{len(frag_ids)}'
            frag_ids.append((sid, t))
            return f'<h2 id="{sid}">{t}</h2>'
        frag = re.sub(r'<h2>(.*?)</h2>', addid, frag)
        model = c['prov'].get(i, c['default_model'])
        audit = f' · flagged for Fable 5.1 review (unit {c["audit_unit"]} audit)' if flagged(model) else ''
        # P68: the reading layout (mdcourse.reading): the module's syllabus line as the scope, its curated bibliography
        # as Sources, and its provenance, the writer's unsure list, its checks and audits and its prompt as
        # "How this unit was made"
        why = next((w for mid, _, w in c['umap'][u][2] if mid == i), '')
        bib = R / 'bibliography' / c['id'] / f'r-{i}.md'
        src, nsrc = '', 0
        if bib.exists():
            bt = re.sub(r'\A# .*\n', '', bib.read_text(encoding='utf-8'))
            nsrc = len(re.findall(r'^\s*- ', bt, re.M))
            src = markdown.markdown(bt).replace('<h2>', '<h3>').replace('</h2>', '</h3>').replace('<a href=', '<a target="_blank" rel="noopener" href=')
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
        made = [('Provenance', f'<p>Written with {html.escape(model)}{audit}.</p>', None), ("Writer's unsure list", unsure, None),
                ('Checks and audits', f'<ul>{"".join(checks)}</ul>' if checks else '', None),
                ('The prompt this answers', mdcourse.brief_box(meta['prompt'], 'Copy prompt'), None)]
        scope, steps, end = mdcourse.reading(sl, frag, html.escape(why), src, made, nsrc, ICON_CHEV)
        panels.append(f'''
<section class="panel" id="{sl}" data-unit="{u}" data-ctx="{c['id']}" data-kind="report" data-split="r-{i}" style="--cc:{c['color']}" hidden>
  <header class="phead">
    {crumbs(('Academy', 'home'), (c['short'], c['home_id']), (f'Unit {u}', f'{c["home_id"]}-u{u}'), (i, None))}
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
    # everything not written with the course's exempt model is flagged for Fable 5.1 review
    flagged_ids = [i for i in c['index'] if flagged(c['prov'].get(i, c['default_model']))]
    # syllabus entries: the exact file name means the whole syllabus; a key that starts with it ("greek-syllabus.html (unit 12 ...)")
    # is a partial entry, named by its flag_label (or "part of the syllabus")
    parts = []
    for k, v in PROV.get('artefacts', {}).items():
        if k.startswith(c['syllabus']) and flagged(v.get('model', '')):
            label = v.get('flag_label') or ('the syllabus' if k == c['syllabus'] else 'part of the syllabus')
            if label not in parts:
                parts.append(label)
    if flagged_ids:
        parts.append(f'{len(flagged_ids)} of its {c["nrep"]} reports' if len(flagged_ids) < c['nrep'] else ('its report' if c['nrep'] == 1 else f'all {c["nrep"]} reports'))
    c['flag'] = (f'<p class="prov flag">Flagged for Fable 5.1 review: {" and ".join(parts)} written with Opus 5.5. See unit {c["audit_unit"]}.</p>' if parts else '')
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
        dkey = u if c['id'] == 'greece' else f'{c["id"]}:{u}'
        out += f'<div class="dunit closed" data-unit="{dkey}" data-ulabel="{c["label"]} · UNIT {u}" style="--c:{col}"><button class="duh" type="button" aria-expanded="false"><span class="un">UNIT {u}</span><span class="ut">{html.escape(name)}</span><span class="cnt">{cnt}</span>{ICON_CHEV}</button><div class="ditems">'
        for mid, t, w in mods:
            if mid in c['done']:
                pill = PILL_UNCK if unchecked(c['prov'].get(mid, '')) else ''
                out += f'<a class="ditem" href="#{c["slug"](mid)}" data-target="{c["slug"](mid)}"><span class="n">{mid}</span><span class="t">{html.escape(t)}</span>{pill}</a>'
            else:
                pill = PILL_NEXT if mid in c.get('next_up', ()) else '<span class="pill">soon</span>'
                out += f'<div class="dsoon"><span class="n">{mid}</span><span class="t">{html.escape(t)}</span>{pill}</div>'
        out += '</div></div>'
    top = (f'<div class="dtop"><a class="ditem dhome" href="#home" data-target="home"><span class="n">←</span><span class="t">Academy</span></a>'
           f'<a class="ditem dhome" href="#{c["home_id"]}" data-target="{c["home_id"]}"><span class="n">⌂</span><span class="t">{c["short"]}: course home</span></a>'
           f'<a class="ditem dhome" href="#{c["syl_id"]}" data-target="{c["syl_id"]}"><span class="n">§</span><span class="t">Syllabus and prompts</span></a>'
           + ('' if 'build' in OMIT else f'<a class="ditem dhome" href="#{c["home_id"]}-built" data-target="{c["home_id"]}-built"><span class="n">✓</span><span class="t">How it was built</span></a>') + '</div>')
    return f'<nav class="dlist" data-navctx="{c["id"]}" data-accordion aria-label="{c["short"]} course" hidden>{top}{out}</nav>'


def ucard(c, u):
    name, why, mods = c['umap'][u]; col = c['unit_colors'][u]
    have = [m for m in mods if m[0] in c['done']]; pct = round(100 * len(have) / len(mods))
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
    return f'<details class="ucard{"" if have else " pending"}" id="{c["home_id"]}-u{u}" data-mods="{ids}" style="--c:{col}"><summary class="uch"><span class="un">UNIT {u}</span><span class="uh">{html.escape(name)}</span><span class="st">{status}</span><span class="bar" aria-hidden="true"><i style="width:{pct}%"></i></span><span class="uwhy">{html.escape(why)}</span>{ICON_CHEV}</summary><div class="hrows">{rows}</div></details>'


THEME = {t['id']: t for t in THEMES}
def crumbs(*items):
    """Breadcrumb trail: (label, target panel id) pairs; the last item is the current page and has no link."""
    out = []
    for label, tgt in items:
        out.append(f'<a href="#{tgt}" data-target="{tgt}">{html.escape(str(label))}</a>' if tgt else f'<span aria-current="page">{html.escape(str(label))}</span>')
    return '<nav class="crumbs" aria-label="You are here">' + '<span class="sep" aria-hidden="true">›</span>'.join(out) + '</nav>'

def hours(words):
    """Reading time at about 230 words a minute, as a short label."""
    h = words / 230 / 60
    return f'{h:.0f}' if h >= 10 else f'{h:.1f}'


def course_home(c):
    parts = ''
    for num, title, us, when, ctx in c['parts']:
        nmods = sum(len(c['umap'][u][2]) for u in us)
        parts += f'<section class="part{" deep" if num == "+" else ""}"><header class="phd"><span class="pnum">{num}</span><div class="ptx"><div class="pmeta"><span>{"Unit " + us[0] if len(us) == 1 else "Units " + us[0] + "–" + us[-1]}</span><span>{nmods} modules</span><span>{when}</span></div><h2>{title}</h2><p>{ctx}</p></div></header><div class="ucards">{"".join(ucard(c, u) for u in us)}</div></section>'
    E = c['eras']
    ribbon = ''.join(f'<span class="seg" style="flex-grow:{e[2]-e[1]};--c:{e[3]}" title="{e[0]}"></span>' for e in E)
    legend = ''.join(f'<li style="--c:{e[3]}"><i></i><b>{e[0]}</b><span class="yr">{yr(e[1])} – {yr(e[2])}</span><span class="un2">{e[4]}</span></li>' for e in E)
    ticks = ''.join(f'<span style="left:{p}">{t}</span>' for t, p in c['ticks'])
    nunits = len(c['units']) - 1
    return f'''
<section class="panel home" id="{c['home_id']}" data-ctx="{c['id']}" data-kind="course" data-split="home" data-t="{c['short']}" data-u="COURSE {c['num']}" data-c="{c['color']}" style="--cc:{c['color']}" hidden>
  <header class="hero">
    {crumbs(('Academy', 'home'), (THEME[c['theme']]['name'], 'track-' + c['theme']), (f"Course {c['num']} · {c['short']}", None))}
    <div class="eyebrow"><span class="u" style="--c:{c['color']}">{c['eyebrow']}</span> · Personal Mythology{' · <span class="u" style="--c:var(--gold)">IN PROGRESS</span>' if c['status'] != 'available' else ' · <span class="u" style="--c:var(--teal)">COMPLETE</span>'}</div>
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
  <a class="hbtn alt wide" href="#home" data-target="home"><span>Academy</span><b>{c['closing']}</b></a>
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
    {crumbs(('Academy', 'home'), (c['short'], c['home_id']), ('Syllabus', None))}
    <div class="eyebrow"><span class="u" style="--c:{c['color']}">{c['label']}</span> · <span class="u" style="--c:var(--gold)">SYLLABUS</span> · {c['total_mods']} modules · every prompt in full</div>
    <h1>{c['short']}: syllabus and prompts</h1>
    <p class="lede">This is the complete syllabus the reports were generated from. Each module has its drop-in prompt; copy it into a new chat to regenerate a report yourself, extend one, or compare a fresh answer against the one here. Where a report exists it is linked.</p>
    {c['flag']}
  </header>
  <section class="howto"><h2>How to run it</h2>{c['syl_intro']}</section>
  <nav class="toc" aria-label="Units">{''.join(f'<a href="#{a}-u{u}">{u} · {html.escape(n)}</a>' for u, n, _, _ in c['units'])}</nav>
  {s}
</section>'''


def card(theme, color, short, title, blurb, meta, done, total, status, href, external=False):
    """A catalogue card: track chip, title, blurb, meta row, progress meter, status, button. Same shape for every course."""
    pct = round(100 * done / total) if total else 0
    pill = '<span class="pill live">complete</span>' if status == 'available' else f'<span class="pill prog">{status}</span>'
    label = 'Continue' if status == 'in progress' else ('Open the syllabus' if status == 'coming soon' else 'Open the course')
    tgt = '' if external else f' data-target="{href[1:]}"'
    return f'''<a class="course live" href="{href}"{tgt} style="--c:{color}">
    <div class="ctop"><span class="cname">{html.escape(theme)} · {html.escape(short)}</span>{pill}</div>
    <span class="ctitle">{html.escape(title)}</span>
    <p>{blurb}</p>
    <div class="cstats">{meta}</div>
    <div class="meter"><span class="bar" aria-hidden="true"><i style="width:{pct}%"></i></span><span>{pct}% written</span></div>
    <span class="cgo">{label}</span>
  </a>'''


def root_card(c):
    meta = f'<span><b>{c["card_units"]}</b> units</span>'
    meta += f'<span><b>{c["nrep"]}</b> reports</span>' if c['status'] == 'available' else f'<span><b>{c["nrep"]}</b> of {c["content_mods"]} reports</span>'
    meta += f'<span><b>{c["words"]//1000}k</b> words</span><span><b>{hours(c["words"])}</b> h reading</span>'
    return card(THEME[c['theme']]['name'], c['color'], f'Course {c["num"]}', c['name'], c['card'], meta, c['nrep'], c['content_mods'], c['status'], f'#{c["home_id"]}')


for c in HISTORY:
    load(c)

ALL_REPORTS = sum(c['nrep'] for c in HISTORY)
ALL_WORDS = sum(c['words'] for c in HISTORY)
G = HISTORY[0]


def load_markdown(c):
    """A markdown course: its data file (generator/data/<slug>/hub.py: courses, units, briefs, audit log, status) and
    its filed units, read from the vault (courses/<slug>/, A5). A unit is written when its file is in the vault with
    front matter; the data file's READINGS add a page's intro and top-bar name, and its research pages (an `md` path
    relative to the data folder). WRITTEN is derived here, never typed."""
    spec = importlib.util.spec_from_file_location('hubdata_' + c['id'], R.parent / c['data'])
    d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
    c['hub'] = d
    c['data_dir'] = (R.parent / c['data']).parent
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
        pid = f'{c.get("prefix", c["id"])}-{sc["k"]}'   # brand-a, brand-b; a new course: <id>-<key>
        legacy = c.get('legacy_ids')                   # Brand + AI keeps the anchors it had at A3 (#briefs-a, #b-a2)
        out.append(dict(id=pid, home_id=pid, briefs_id=f'briefs-{sc["k"]}' if legacy else f'{pid}-briefs',
                        brief_anchor='b-' if legacy else f'{pid}-b-', parent=c, sc=sc, theme=theme, short=short, key=sc['key'],
                        name=sc['name'], color=sc['color'], units=sc['units'], done=done, nunits=len(sc['units']), nwritten=len(done),
                        status=('available' if len(done) == len(sc['units']) else 'in progress') if done else 'coming soon', card=sc['tile']))   # a course with no unit filed is coming soon; every unit filed is complete ('available', as a finished history course is; A-5, 3 Nov 2026)
    return out


for c in MARKDOWN:
    load_markdown(c)
MD = [m for c in MARKDOWN for m in md_courses(c)]
for m in MD:
    m['panels'], m['nav'], m['nbib'] = mdcourse.build(m, crumbs, THEME, PILL_NEXT, ICON_CHEV)


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
    report's date from provenance.json's `written` map ({course: {module: ISO date}}), which P23 fills (none yet).
    Each entry: (date, course short, colour, code, title, panel id, model)."""
    out = []
    for m in MD:
        vault = m['parent']['vault_units']
        for u in m['units']:
            if u[0] in vault:
                fm = vault[u[0]][1]
                if fm.get('written'):
                    out.append((fm['written'], m['short'], m['color'], u[0], fm.get('title', u[1]), m['parent']['written'][u[0]], fm.get('model', '')))
    for c in HISTORY:
        for i, d in PROV.get('written', {}).get(c['id'], {}).items():
            if i in c['index']:
                out.append((d, c['short'], c['color'], i, c['index'][i]['title'], c['slug'](i), c['prov'].get(i, c['default_model'])))
    return sorted(out, key=lambda x: x[0], reverse=True)


DATED = dated_units()
RECENT = DATED[:5]


def totals():
    return dict(live=len(HISTORY) + sum(1 for m in MD if m['status'] != 'coming soon'), coming=len(NEXT) + sum(1 for m in MD if m['status'] == 'coming soon'), reports=sum(c['nrep'] for c in HISTORY),
                units=sum(m['nwritten'] for m in MD), words=sum(c['words'] for c in HISTORY))


TOTALS = totals()


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


CL = (R / 'CHANGELOG.md').read_text(encoding='utf-8').split('\n')
cl_title, cl_intro, cl_secs = CL[0][2:], [], []
for ln in CL[1:]:
    if ln.startswith('## '):
        cl_secs.append((ln[3:], []))
    elif cl_secs:
        cl_secs[-1][1].append(ln)
    else:
        cl_intro.append(ln)
cl_sessions = [s for s in cl_secs if re.match(r'\d', s[0])]
CL_ACCENTS = ['var(--red)', 'var(--orange)', 'var(--gold)', 'var(--teal)', 'var(--blue)', 'var(--purple)']
cl_since = re.match(r'(\d+)(?: to \d+)? (\w+) (\d{4})', cl_sessions[-1][0]) if cl_sessions else None
cl_since = f'since {cl_since.group(1)} {cl_since.group(2)} {cl_since.group(3)}' if cl_since else ''
cl_cards = ''
for k, (head, body) in enumerate(cl_sessions):
    parts = head.split(' · ')
    date, sess, title = (parts + ['', ''])[:3]
    num = re.search(r'\d+', sess)
    col = CL_ACCENTS[(int(num.group()) - 1) % len(CL_ACCENTS)] if num else 'var(--gold)'
    cl_cards += (f'<details class="clog" style="--c:{col}"{" open" if k == 0 else ""}><summary><span class="cd">{html.escape(date)}</span>'
                 f'<span class="cs">{html.escape(sess)}</span><span class="ct">{md_inline(title)}</span></summary><div class="cb">{md_blocks(body)}</div></details>')
cl_other = ''.join(f'<section class="howto clsec"><h2>{md_inline(h)}</h2>{md_blocks(b)}</section>' for h, b in cl_secs if (h, b) not in cl_sessions)
changelog = f"""
<section class="panel log" id="changelog" data-ctx="root" data-kind="changelog" data-t="{html.escape(cl_title)}" data-u="ACADEMY" data-c="var(--gold)" hidden>
  <header class="hero">
    {crumbs(('Academy', 'home'), ('Changelog', None))}
    <div class="eyebrow"><span class="u" style="--c:var(--gold)">CHANGELOG</span> · {len(cl_sessions)} sessions {cl_since}</div>
    <h1>{html.escape(cl_title)}</h1>
    {md_blocks(cl_intro).replace('<p>', '<p class="lede">', 1)}
  </header>
  {cl_other}
  <h2 class="hsec">Sessions, newest first</h2>
  <div class="clogs">{cl_cards}</div>
</section>"""
cl_link = ''.join(([] if 'changelog' in OMIT else [f'<a class="hbtn alt" href="#changelog" data-target="changelog"><span>Changelog</span><b>{len(cl_sessions)} sessions {cl_since}, newest first</b></a>'])
                  + ([] if 'backlog' in OMIT else [f'<a class="hbtn alt" href="#backlog" data-target="backlog"><span>Backlog</span><b>The queue of chats, and the chats done</b></a>'])
                  + ([] if 'figures' in OMIT else [f'<a class="hbtn alt" href="#viz-examples" data-target="viz-examples"><span>Figure kinds</span><b>Every figure a unit can declare, with its block</b></a>']))
cl_link = f'<div class="hlinks">{cl_link}</div>' if cl_link else ''

# the backlog page: docs/BACKLOG.md (the queue) and docs/CHANGELOG.md (the chats done), rendered as they are
def md_sections(path):
    """A docs/ markdown file as (title, intro lines, [(heading, lines)]) split on '## ' headings."""
    L = path.read_text(encoding='utf-8').split('\n')
    title, intro, secs = L[0][2:], [], []
    for ln in L[1:]:
        if ln.startswith('## '):
            secs.append((ln[3:], []))
        elif secs:
            secs[-1][1].append(ln)
        else:
            intro.append(ln)
    return title, intro, secs

DOCS = R.parent / 'docs'
bl_title, bl_intro, bl_secs = md_sections(DOCS / 'BACKLOG.md')
dc_title, dc_intro, dc_secs = md_sections(DOCS / 'CHANGELOG.md')
dc_rows = sum(1 for ln in (DOCS / 'CHANGELOG.md').read_text(encoding='utf-8').split('\n') if ln.startswith('| ') and not ln.startswith('| Date') and not ln.startswith('|---'))
bl_body = ''.join(f'<section class="howto clsec" style="--hc:var(--orange)"><h2>{md_inline(h)}</h2>{md_blocks(b)}</section>' for h, b in bl_secs)
dc_body = f'<section class="howto clsec" style="--hc:var(--gold)"><h2>{md_inline(dc_title)}</h2>{md_blocks(dc_intro)}</section>' + ''.join(f'<section class="howto clsec" style="--hc:var(--gold)"><h2>{md_inline(h)}</h2>{md_blocks(b)}</section>' for h, b in dc_secs)
backlog = f"""
<section class="panel log" id="backlog" data-ctx="root" data-kind="backlog" data-t="{html.escape(bl_title)}" data-u="ACADEMY" data-c="var(--orange)" hidden>
  <header class="hero">
    {crumbs(('Academy', 'home'), ('Backlog', None))}
    <div class="eyebrow"><span class="u" style="--c:var(--orange)">BACKLOG</span> · the queue of chats · {dc_rows} chats done</div>
    <h1>{html.escape(bl_title)}</h1>
    {md_blocks(bl_intro).replace('<p>', '<p class="lede">', 1)}
  </header>
  {bl_body}
  <h2 class="hsec">Chats done</h2>
  {dc_body}
</section>"""

soon_cards = ''.join(f'<details class="course soon" style="--c:{col}"><summary><span class="cname">{html.escape(short)}</span><span class="ctitle">{html.escape(name)}</span><span class="pill">coming soon</span></summary><p class="nscope">{html.escape(scope)}</p><p class="nspine"><span>Spine</span>{html.escape(spine)}</p></details>' for short, name, col, scope, spine in NEXT)


def md_card(m):
    meta = f'<span><b>{m["nunits"]}</b> units</span><span><b>{m["nwritten"]}</b> written</span><span><b>{len(m["parent"]["hub"].AUDIT_LOG)}</b> audit{"s" if len(m["parent"]["hub"].AUDIT_LOG) != 1 else ""}</span>'
    return card(THEME[m['theme']]['name'], m['color'], f'Course {m["key"]}', m['name'], html.escape(m['card']), meta, m['nwritten'], m['nunits'], m['status'], f'#{m["home_id"]}')


ALL_UNITS = TOTALS['units']
N_LIVE = TOTALS['live']
tracks = ''
track_jump = ''
for t in THEMES:
    hist = [c for c in HISTORY if c['theme'] == t['id']]
    mds = [m for m in MD if m['theme'] == t['id']]
    cards = ''.join(root_card(c) for c in hist) + ''.join(md_card(m) for m in mds)
    soon = [m for m in mds if m['status'] == 'coming soon']   # a markdown course with nothing written is planned, not live
    n = len(hist) + len(mds) - len(soon)
    count = f'{n} course{"s" if n != 1 else ""}' if n else f'{len(soon)} course{"s" if len(soon) != 1 else ""} coming soon'
    if hist: count += f' · {sum(c["nrep"] for c in hist)} reports'
    if mds: count += f' · {sum(m["nwritten"] for m in mds)} of {sum(m["nunits"] for m in mds)} units'
    if t['id'] == 'history' and NEXT: count += f' · {len(NEXT)} planned'
    elif soon and n: count += f' · {len(soon)} coming soon'
    jump = (f'{n} live' + (f' · {len(NEXT)} planned' if t['id'] == 'history' and NEXT else '') + (f' · {len(soon)} coming soon' if soon else '')) if n else (f'{len(soon)} coming soon' if soon else 'planned')
    track_jump += f'<a class="hbtn alt" href="#track-{t["id"]}" style="--c:{t["color"]}"><span>Track</span><b>{html.escape(t["name"])}</b><small>{jump}</small></a>'
    extra = ''
    if t['id'] == 'history':
        planned = '' if not NEXT else f"""
  <details class="howto rules planned">
    <summary><h2>Planned</h2><span>{len(NEXT)} courses, in the intended order</span></summary>
    <p class="hnote">The two civilisations that border the Greek story, then the northern and insular traditions, then East Asia. Open a course to see its scope and spine.</p>
    <div class="soonlist">{soon_cards}</div>
  </details>"""
        extra = f"""
  <details class="howto rules">
    <summary><h2>Why history and myth together</h2><span>the method of the track</span></summary>
    <div class="ml-grid">
      <div class="ml"><span class="gk">μῦθος</span><b>mythos</b><p>In Homer, simply what someone says with authority: a speech, a command, a tale. By the fifth century it had come to mean the story you cannot check.</p></div>
      <div class="ml"><span class="gk">λόγος</span><b>logos</b><p>A word, a count, an account. By the same century it meant the argued explanation, the one that gives its reasons and invites you to test them.</p></div>
    </div>
    <p>The Greeks drew that line themselves. Herodotus calls his work a <em>historiē</em>, an inquiry, and still reports what the Persians and Egyptians told him. Thucydides warns that his history leaves out the <em>mythōdes</em>, the storylike, and will seem less pleasant for it (1.22). Plato expels the poets from his ideal city and then ends the <em>Republic</em> with a myth of his own.</p>
    <p>The tidy story of a clean progress "from mythos to logos" (the title of Wilhelm Nestle's book of 1940) is now itself treated as a modern myth: the Greeks never stopped telling myths; their philosophers used them, their historians argued with them, and their cities were governed by them. So each course reads a culture's myths and its history together, asks who told each story and what they gained by it, and keeps the evidence in view. The aim is not to debunk the myths but to understand them as well as the history. Later courses point back to earlier ones where they touch: Rome to Greece's units 7 and 10, Persia to units 6 and 11, Egypt to units 1 and 7.</p>
  </details>{planned}"""
    tracks += f"""
  <section class="track" id="track-{t['id']}" style="--c:{t['color']}">
    <header class="thead"><div class="ttx"><span class="cname">Track</span><h2>{html.escape(t['name'])}</h2><p>{html.escape(t['lede'])}</p></div><span class="tmeta">{count}</span></header>
    <div class="cgrid">{cards}</div>{extra}
  </section>"""

# the resume card: the reader's last report (shell.js, from localStorage) or, until there is one, the newest dated unit
# (else the first report of the first course in progress). data-progress carries each course's progress for the meter.
_prog = {c['home_id']: dict(pct=c['pct'], done=c['nrep'], of=c['content_mods'], what='reports') for c in HISTORY}
_prog.update({m['home_id']: dict(pct=m['pct'], done=m['nwritten'], of=m['nunits'], what='units') for m in MD})
if RECENT:
    _d, _short, _col, _code, _title, _pid, _model = RECENT[0]
    fallback = f'<a class="hbtn start" href="#{_pid}" data-target="{_pid}"><span>Start here · newest unit</span><b>{html.escape(_short)} · {html.escape(_code)} {html.escape(_title)}</b></a>'
else:
    _c = next((c for c in HISTORY if c['status'] != 'available' and c['first']), HISTORY[0])
    fallback = f'<a class="hbtn start" href="#{_c["slug"](_c["first"])}" data-target="{_c["slug"](_c["first"])}"><span>Start here</span><b>{_c["short"]} · {_c["first"]} {html.escape(_c["index"][_c["first"]]["title"])}</b></a>'

# new since: the dated units, newest first, and the latest kit session
recent_rows = ''
if cl_sessions and 'changelog' not in OMIT:
    _head = cl_sessions[0][0].split(' · ')
    _date, _sess, _title = (_head + ['', ''])[:3]
    recent_rows += f'<a class="hrow" href="#changelog" data-target="changelog"><span class="n">{html.escape(re.sub(r'(\w{3})\w* \d{4}$', r'\1', _date))}</span><span class="t">{md_inline(_title)}<small>{html.escape(_sess)} · the kit changelog</small></span><span class="pill prog">session</span></a>'
for d, short, col, code, title, pid, model in RECENT:
    recent_rows += f'<a class="hrow" href="#{pid}" data-target="{pid}" style="--c:{col}"><span class="n">{short_date(d).replace(" 2026", "")}</span><span class="t">{html.escape(code)} · {html.escape(title)}<small>{html.escape(short)}{" · " + html.escape(model) if model else ""}</small></span><span class="pill live">unit</span></a>'
# "How every course works": the constants. P80 (1 Nov 2026): an edition replaces any line that names a course it does
# not hold with its own (EDITIONS[...]['rules'], keyed by the line's bold head); the full Academy keeps these as written.
RULE_LINES = [
    ('One reader.', 'Every course is written for the same person and read in order, on a phone, with the citations checked.'),
    ('Sources first.', 'A unit names its sources and says where they disagree; a claim that cannot be sourced is marked unsourced or left out.'),
    ('One unit per chat, built in full.', 'Each unit is written from a published brief or prompt, in its own chat, with its closing artefact: a self-test and carry-forward ideas for the history courses, a shipped deliverable for Brand + AI.'),
    ('Audited every four units.', 'After every four units written in a hub, a stratified sample of claims is checked against its sources with a second model; a unit that fails gets a full audit. The model that wrote each unit is recorded.'),
    ('An open syllabus.', 'Every prompt and brief is published with its course, so any unit can be regenerated, extended or checked.'),
]
_own = ED.get('rules', {})
if set(_own) - {h for h, _ in RULE_LINES}:
    raise SystemExit(f'EDITIONS[{EDITION!r}] rules name no constants line: {sorted(set(_own) - {h for h, _ in RULE_LINES})}')
RULES = '\n'.join(f'      <li><strong>{h}</strong> {_own.get(h, t)}</li>' for h, t in RULE_LINES)
roothome = f"""
<section class="panel root" id="home" data-ctx="root" data-kind="root" data-t="Academy" data-u="HOME" data-c="var(--red)" hidden>
  <header class="hero resume" data-progress='{json.dumps(_prog)}'>
    <div class="eyebrow"><span class="u" style="--c:var(--red)">ACADEMY</span> · {N_LIVE} course{"s" if N_LIVE != 1 else ""} live{f" · {TOTALS['coming']} planned" if TOTALS['coming'] else ""} · one reader</div>
    <h1>Academy</h1>
    <p class="lede">Every self-study course in one place. Pick up where you left off.</p>
    <div class="hlinks hl-root"><a class="hbtn cont" href="#home" data-long hidden><span>Continue reading</span><b></b><span class="rmeter"><span class="bar" aria-hidden="true"><i></i></span><span class="pct mono"></span></span></a>{fallback}</div>
  </header>

{f'''  <section class="recent">
    <h2 class="hsec">New since</h2>
    <div class="hrows">{recent_rows}</div>
  </section>
''' if recent_rows else ''}
  <nav class="tjump" aria-label="Tracks">{track_jump}</nav>
  {tracks}

  <details class="howto rules">
    <summary><h2>How every course works</h2><span>the constants</span></summary>
    <ol>
{RULES}
    </ol>
  </details>
  <p class="totals mono">{N_LIVE} course{"s" if N_LIVE != 1 else ""}{f" · {TOTALS['reports']} reports" if HISTORY else ""}{f" · {TOTALS['units']} units" if MD else ""} · {TOTALS['words']:,} words · {hours(TOTALS['words'])} h of reading</p>
  {cl_link}
</section>"""

# A4 · "How it was built": one generated page per course (howbuilt.py), every fact read from a file
for c in HISTORY:
    c['built'] = howbuilt.history_page(c, crumbs, THEME, md_inline, md_blocks, flagged, unchecked)
for m in MD:
    m['panels'].append(howbuilt.markdown_page(m, crumbs, THEME, md_inline, md_blocks))

panels = [roothome, changelog, backlog]
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

def root_nav_track(t):
    hist = [c for c in HISTORY if c['theme'] == t['id']]
    mds = [m for m in MD if m['theme'] == t['id']]
    out = ''
    out += ''.join(f'<a class="ditem dcourse" href="#{c["home_id"]}" data-target="{c["home_id"]}" style="--c:{c["color"]}"><span class="n">{c["num"]}</span><span class="t">{c["short"]}<small>{c["card_units"]} units · {c["nrep"]} {"reports" if c["status"] == "available" else "of " + str(c["content_mods"]) + " reports"}</small></span></a>' for c in hist)
    out += ''.join(f'<a class="ditem dcourse" href="#{m["home_id"]}" data-target="{m["home_id"]}" style="--c:{m["color"]}"><span class="n">{m["key"]}</span><span class="t">{html.escape(m["short"])}<small>{m["nwritten"]} of {m["nunits"]} units</small></span></a>' for m in mds)
    if t['id'] == 'history' and NEXT:
        # the planned courses fold into one row; open it to see them in order
        out += (f'<details class="dplan"><summary class="dsoon"><span class="n">+{len(NEXT)}</span><span class="t">planned, in order</span>{ICON_CHEV}</summary>'
                + ''.join(f'<div class="dsoon" style="--c:{col}"><span class="n">{k + len(HISTORY) + 1}</span><span class="t">{html.escape(s)}</span><span class="pill">soon</span></div>' for k, (s, _, col, _, _) in enumerate(NEXT)) + '</details>')
    n = len(hist) + len(mds)
    # a collapsible group: closed unless the reader opened it; shell.js opens the track of the last report read (else the first)
    return (f'<div class="dunit closed" data-unit="track:{t["id"]}" data-ulabel="{html.escape(t["name"]).upper()}" style="--c:{t["color"]}">'
            f'<button class="duh" type="button" aria-expanded="false"><span class="un">■</span><span class="ut">{html.escape(t["name"])}</span><span class="cnt">{n}</span>{ICON_CHEV}</button><div class="ditems">{out}</div></div>')

root_nav = ('<nav class="dlist" data-navctx="root" aria-label="Courses"><div class="dtop"><a class="ditem dhome" href="#home" data-target="home"><span class="n">⌂</span><span class="t">Home</span></a>'
            + ('' if 'changelog' in OMIT else '<a class="ditem dhome" href="#changelog" data-target="changelog"><span class="n">≡</span><span class="t">Changelog</span></a>')
            + ('' if 'backlog' in OMIT else '<a class="ditem dhome" href="#backlog" data-target="backlog"><span class="n">☐</span><span class="t">Backlog</span></a>') + '</div>'
            + ''.join(root_nav_track(t) for t in THEMES) + '</nav>')
navs = root_nav + ''.join(drawer(c) for c in HISTORY) + ''.join(m['nav'] for m in MD)

CSS = open(R / 'shell.css').read()
JS = open(R / 'shell.js').read()

page = f'''<meta charset="utf-8">
<title>{ED['title']}</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Gentium+Book+Plus&display=swap">
<style>{CSS}</style>
<script>try{{var t=localStorage.getItem('hellas-theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<header class="top">
  <div class="top-in">
    <button class="ib" id="menuB" type="button" aria-label="Open contents" aria-expanded="false" aria-controls="drawer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <a class="ib" id="homeB" href="#home" aria-label="Academy home"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h5v-6h4v6h5V10"/></svg></a>
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
  <div class="dhead"><div class="brand">ACA<span>/</span>DEMY</div><button class="ib" id="closeB" type="button" aria-label="Close contents"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
  {navs}
</aside>
<main>
{''.join(panels)}
</main>
<script>{JS}</script>
'''
# P70: in an edition, a link to a page it lacks is not a link: a navigation button or row to it is dropped, any other
# link (a pointer in a report's text into a course the edition does not hold) is kept as its plain text
if EDITION != 'academy':
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
rows = [('Shell (`index.html`)', 1, len(page.encode()), len(page.encode()), 'home, drawer, Brand + AI course homes and build pages, changelog, backlog')]
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
if EDITION == 'academy':   # P70: the repo's files are the full Academy's; an edition writes only its folder
    (R / 'README.md').write_text(readme, encoding='utf-8')

# the Fable review queue, regenerated from provenance.json on every build so it never goes stale
q = ['# Fable review queue', '', 'Generated by `build.py` from `provenance.json`; do not edit by hand. Everything below was written with a model other than Fable 5.1 and is flagged for review with Fable 5.1. Run the reviews with Fable 5.1 through each course\'s audit unit. When an item has been reviewed and fixed, change its entry in `provenance.json` to `"Opus 5.5, reviewed with Fable 5.1"` (or to `"Fable 5.1"` if it was regenerated); anything that mentions Fable 5.1 drops off this list and loses its flag on the site.', '']
from review_due import status as review_status
REVIEW_DUE, REVIEW_LINE = review_status()
q += [f'**{REVIEW_LINE}**', '']
q += ['## Course material other than reports', '', '| Item | Model | What | Review |', '|---|---|---|---|']
q += [f'| `{k}` | {v["model"]} | {v["what"]} | {v["review"]} |' for k, v in PROV.get('artefacts', {}).items() if flagged(v['model'])]
for c in HISTORY:
    fl = [(i, c['prov'].get(i, c['default_model'])) for i in c['index'] if flagged(c['prov'].get(i, c['default_model']))]
    q += ['', f'## {c["short"]} reports ({len(fl)} flagged, audit unit {c["audit_unit"]})', '']
    if fl:
        q += ['| Module | Title | Model | Words |', '|---|---|---|---|']
        for i, mdl in fl:
            n = wc(vault.report_html(c, i))
            q.append(f'| {i} | {c["index"][i]["title"]} | {mdl} | {n:,} |')
q += ['', '## Notes for the reviewer', ''] + [f'- {n}' for n in PROV.get('review_notes', [])]
if EDITION == 'academy':
    open(R / 'FABLE-REVIEW.md', 'w').write('\n'.join(q) + '\n')
    from biblio import write_all as _biblio
    print(f'bibliography: {_biblio()} unit files')
else:
    print(f'edition {EDITION}: {SITE.relative_to(R)}')
print(' · '.join(f"{c['short']}: {c['nrep']}/{c['content_mods']} reports, {c['words']:,} words" for c in HISTORY)
      + ''.join(f" · {c['short']}: {c['nwritten']}/{c['nunits']} units" for c in MARKDOWN), f'· shell {kb(len(page.encode()))}, {len(REPORTS)} fetched files, site {kb(allb)}')
print(REVIEW_LINE)
if '--epub' in sys.argv:
    import epub
    _mdu = []
    for c in MARKDOWN:
        _order = [u[0] if isinstance(u, (tuple, list)) else u for u in getattr(c['hub'], 'ORDER', [])]
        for code, (f, fm) in sorted(c['vault_units'].items(), key=lambda kv: _order.index(kv[0]) if kv[0] in _order else 999):
            _mdu.append((c, code, fm.get('title', code), f))
    epub.write(EDITION, ED, HISTORY, _mdu)
