"""Assemble the Academy site in academy/ from the course data in courses.py: academy/index.html, the shell (home,
drawer, course homes, syllabi, build pages, changelog, backlog), and one file per report, fetched by the shell on
navigation (docs/academy.md A2): academy/<course>/r-<id>.html for a history report, academy/<course>/<reading id>.html
for a markdown course's reading page. The size table in README.md is regenerated on every build.

The root home is Academy (docs/academy.md, A1): every course of both families. History courses (Greece, Rome) are
built from their kit folders; a markdown course (Brand + AI) is built by mdcourse.py from its data file
(generator/data/<slug>/hub.py, AD5) into one Academy course per course in that file (AD6, A3): a course home, a
reading page per written unit, and the "How it is built" pages (method, build order, briefs, audits, bibliography,
changelog). The site also renders the Project's backlog and chat changelog (docs/) as a Backlog page.

Each course has a syllabus file, a fragments folder, a prompts index (the modules with a written report),
a colour and a short name. Greece keeps its original panel ids (#greece, #syllabus, #m23); later courses
are namespaced (#rome, #rome-syllabus, #rm01).
"""
import json, re, html, pathlib, importlib.util
from courses import COURSES, HISTORY, MARKDOWN, NEXT, THEMES
import mdcourse

R = pathlib.Path(__file__).resolve().parent
PROV = json.load(open(R / 'provenance.json'))
ICON_CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>'


def wc(frag):
    body = re.split(r'<h2>\s*Self-test', frag)[0]
    return len(re.sub(r'<[^>]+>', ' ', body).split())


def unchecked(model):
    """A report registered before its fresh check ran carries '(unchecked)' in its provenance and an 'unchecked' pill on the site."""
    return 'unchecked' in model


PILL_UNCK = '<span class="pill unck" title="Written, not yet checked by a fresh reviewer">unchecked</span>'
PILL_NEXT = '<span class="pill next" title="Queued for the next writing session">next</span>'


def flagged(model):
    """Anything whose provenance does not mention Fable 5.1 (written with it, or reviewed with it) is flagged for Fable review."""
    return 'Fable 5.1' not in model


def yr(y):
    return f'{-y} BC' if y < 0 else f'AD {y}'


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
    c['first'] = next(iter(c['index']))  # the first written report, where a new reader starts
    c['prov'] = PROV.get(c['id'], {})
    c['slug'] = lambda i, p=c['prefix']: p + i.replace('.', '')

    panels, total = [], 0
    ucol = c['unit_colors']
    for i, meta in c['index'].items():
        frag = (R / c['frags'] / f'r-{i}.html').read_text()
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
        toc = ''.join(f'<a href="#{sid}">{t}</a>' for sid, t in frag_ids)
        model = c['prov'].get(i, c['default_model'])
        audit = f' · flagged for Fable 5.1 review (unit {c["audit_unit"]} audit)' if flagged(model) else ''
        panels.append(f'''
<section class="panel" id="{sl}" data-unit="{u}" data-ctx="{c['id']}" data-kind="report" hidden>
  <header class="phead">
    {crumbs(('Academy', 'home'), (c['short'], c['home_id']), (f'Unit {u}', f'{c["home_id"]}-u{u}'), (i, None))}
    <div class="eyebrow"><span class="u" style="--c:{c['color']}">{c['label']}</span> · <span class="u" style="--c:{ucol[u]}">UNIT {u}</span> · {c['umap'][u][0]} · <span class="mono">{i}</span> · {n:,} words{' ' + PILL_UNCK if unchecked(model) else ''}</div>
    <h1>{html.escape(meta['title'])}</h1>
    <nav class="toc" aria-label="Sections">{toc}</nav>
  </header>
  <div class="report">{frag}</div>
  <p class="prov">Written with {model}{audit}</p>
  <details class="prompt"><summary>The prompt this answers</summary><pre>{html.escape(meta['prompt'])}</pre></details>
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
           f'<a class="ditem dhome" href="#{c["syl_id"]}" data-target="{c["syl_id"]}"><span class="n">§</span><span class="t">Syllabus and prompts</span></a></div>')
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
<section class="panel home" id="{c['home_id']}" data-ctx="{c['id']}" data-kind="course" data-t="{c['short']}" data-u="COURSE {c['num']}" data-c="{c['color']}" style="--cc:{c['color']}" hidden>
  <header class="hero">
    {crumbs(('Academy', 'home'), (THEME[c['theme']]['name'], 'track-' + c['theme']), (f"Course {c['num']} · {c['short']}", None))}
    <div class="eyebrow"><span class="u" style="--c:{c['color']}">{c['eyebrow']}</span> · Personal Mythology{' · <span class="u" style="--c:var(--gold)">IN PROGRESS</span>' if c['status'] != 'available' else ' · <span class="u" style="--c:var(--teal)">COMPLETE</span>'}</div>
    <h1>{c['h1']}</h1>
    <p class="lede">{fill(c['lede'], c)}</p>
    <div class="stats" data-n="4"><div><b>{c['nrep']}</b><span>of {c['content_mods']} reports written</span></div><div><b>{c['units_complete']}</b><span>of {nunits} units complete</span></div><div><b>{c['words']//1000}k</b><span>words so far</span></div><div><b>{hours(c['words'])}</b><span>hours of reading</span></div></div>
    <div class="hlinks"><a class="hbtn cont" href="#{c['home_id']}" data-course="{c['id']}" hidden><span>Continue</span><b></b></a><a class="hbtn start" href="#{c['slug'](c['first'])}" data-target="{c['slug'](c['first'])}"><span>Start the course</span><b>{c['first']} {html.escape(c['index'][c['first']]['title'])}</b></a><a class="hbtn alt" href="#{c['syl_id']}" data-target="{c['syl_id']}"><span>Syllabus</span><b>All {c['total_mods']} prompts, copyable</b></a></div>
    {c['flag']}
  </header>

  <section class="era">
    <div class="era-h"><h2>{c['era_title']}</h2><span>{c['era_range']}</span></div>
    <div class="ribbon" role="img" aria-label="{c['era_aria']}">{ribbon}</div>
    <div class="ticks" aria-hidden="true">{ticks}</div>
    <p class="era-note">{c['era_note']}</p>
    <ul class="legend">{legend}</ul>
  </section>

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
<section class="panel syl" id="{c['syl_id']}" data-ctx="{c['id']}" data-kind="syllabus" data-t="Syllabus and prompts" data-u="{c['label']}" data-c="var(--gold)" style="--cc:{c['color']}" hidden>
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
    label = 'Continue' if status != 'available' else 'Open the course'
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
    """A markdown course's data file (generator/data/<slug>/hub.py): its courses, units, written set and status."""
    spec = importlib.util.spec_from_file_location('hubdata_' + c['id'], R.parent / c['data'])
    d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
    c['hub'] = d
    c['data_dir'] = (R.parent / c['data']).parent
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
        out.append(dict(id=f'brand-{sc["k"]}', home_id=f'brand-{sc["k"]}', parent=c, sc=sc, theme=theme, short=short, key=sc['key'],
                        name=sc['name'], color=sc['color'], units=sc['units'], done=done, nunits=len(sc['units']), nwritten=len(done),
                        status='in progress', card=sc['tile']))
    return out


for c in MARKDOWN:
    load_markdown(c)
MD = [m for c in MARKDOWN for m in md_courses(c)]
for m in MD:
    m['panels'], m['nav'], m['nbib'] = mdcourse.build(m, crumbs, THEME, PILL_NEXT, ICON_CHEV)

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
cl_link = (f'<div class="hlinks"><a class="hbtn alt" href="#changelog" data-target="changelog"><span>Changelog</span><b>{len(cl_sessions)} sessions {cl_since}, newest first</b></a>'
           f'<a class="hbtn alt" href="#backlog" data-target="backlog"><span>Backlog</span><b>The queue of chats, and the chats done</b></a></div>')

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


ALL_UNITS = sum(m['nwritten'] for m in MD)
N_LIVE = len(HISTORY) + len(MD)
tracks = ''
for t in THEMES:
    hist = [c for c in HISTORY if c['theme'] == t['id']]
    mds = [m for m in MD if m['theme'] == t['id']]
    cards = ''.join(root_card(c) for c in hist) + ''.join(md_card(m) for m in mds)
    n = len(hist) + len(mds)
    count = f'{n} course{"s" if n != 1 else ""}'
    if hist: count += f' · {sum(c["nrep"] for c in hist)} reports'
    if mds: count += f' · {sum(m["nwritten"] for m in mds)} of {sum(m["nunits"] for m in mds)} units'
    if t['id'] == 'history': count += f' · {len(NEXT)} coming'
    extra = ''
    if t['id'] == 'history':
        extra = f'''
  <details class="howto rules">
    <summary><h2>Why history and myth together</h2><span>the method of the track</span></summary>
    <div class="ml-grid">
      <div class="ml"><span class="gk">μῦθος</span><b>mythos</b><p>In Homer, simply what someone says with authority: a speech, a command, a tale. By the fifth century it had come to mean the story you cannot check.</p></div>
      <div class="ml"><span class="gk">λόγος</span><b>logos</b><p>A word, a count, an account. By the same century it meant the argued explanation, the one that gives its reasons and invites you to test them.</p></div>
    </div>
    <p>The Greeks drew that line themselves. Herodotus calls his work a <em>historiē</em>, an inquiry, and still reports what the Persians and Egyptians told him. Thucydides warns that his history leaves out the <em>mythōdes</em>, the storylike, and will seem less pleasant for it (1.22). Plato expels the poets from his ideal city and then ends the <em>Republic</em> with a myth of his own.</p>
    <p>The tidy story of a clean progress "from mythos to logos" (the title of Wilhelm Nestle's book of 1940) is now itself treated as a modern myth: the Greeks never stopped telling myths; their philosophers used them, their historians argued with them, and their cities were governed by them. So each course reads a culture's myths and its history together, asks who told each story and what they gained by it, and keeps the evidence in view. The aim is not to debunk the myths but to understand them as well as the history. Later courses point back to earlier ones where they touch: Rome to Greece's units 7 and 10, Persia to units 6 and 11, Egypt to units 1 and 7.</p>
  </details>
  <p class="hnote">Coming next, in the intended order: the two civilisations that border the Greek story, then the northern and insular traditions, then East Asia. Open any course to see its planned scope.</p>
  <div class="soonlist">{soon_cards}</div>'''
    tracks += f'''
  <section class="track" id="track-{t['id']}" style="--c:{t['color']}">
    <header class="thead"><div class="ttx"><span class="cname">Track</span><h2>{html.escape(t['name'])}</h2><p>{html.escape(t['lede'])}</p></div><span class="tmeta">{count}</span></header>
    <div class="cgrid">{cards}</div>{extra}
  </section>'''

roothome = f'''
<section class="panel root" id="home" data-ctx="root" data-kind="root" data-t="Academy" data-u="HOME" data-c="var(--red)" hidden>
  <header class="hero">
    <div class="eyebrow"><span class="u" style="--c:var(--red)">ACADEMY</span> · {N_LIVE} courses live · {len(NEXT)} coming · one reader</div>
    <h1>Academy</h1>
    <p class="lede">Every self-study course in one place, grouped by track. Each course is written one unit at a time to the same method and the same sourcing standard, audited every four units, and read in order. Pick up where you left off, or open a track.</p>
    <div class="stats" data-n="4"><div><b>{N_LIVE}</b><span>courses live</span></div><div><b>{ALL_REPORTS + ALL_UNITS}</b><span>reports and units written</span></div><div><b>{ALL_WORDS//1000}k</b><span>words on the history track</span></div><div><b>{hours(ALL_WORDS)}</b><span>hours of reading</span></div></div>
    <div class="hlinks hl-root"><a class="hbtn cont" href="#home" data-long hidden><span>Continue reading</span><b></b></a>{''.join(f'<a class="hbtn alt" href="#track-{t["id"]}"><span>Track</span><b>{html.escape(t["name"])}</b></a>' for t in THEMES)}</div>
  </header>
  {tracks}

  <details class="howto rules">
    <summary><h2>How every course works</h2><span>the constants</span></summary>
    <ol>
      <li><strong>One reader.</strong> Every course is written for the same person and read in order, on a phone, with the citations checked.</li>
      <li><strong>Sources first.</strong> A unit names its sources and says where they disagree; a claim that cannot be sourced is marked unsourced or left out.</li>
      <li><strong>One unit per chat, built in full.</strong> Each unit is written from a published brief or prompt, in its own chat, with its closing artefact: a self-test and carry-forward ideas for the history courses, a shipped deliverable for Brand + AI.</li>
      <li><strong>Audited every four units.</strong> After every four units written in a hub, a stratified sample of claims is checked against its sources with a second model; a unit that fails gets a full audit. The model that wrote each unit is recorded.</li>
      <li><strong>An open syllabus.</strong> Every prompt and brief is published with its course, so any unit can be regenerated, extended or checked.</li>
    </ol>
  </details>
  {cl_link}
</section>'''

panels = [roothome, changelog, backlog]
for c in HISTORY:
    panels += [course_home(c), syllabus(c)] + c['report_panels']
for m in MD:
    panels += m['panels']

# A2 · the split: every report panel (a history report, a markdown course's reading page) leaves the shell. The shell
# keeps an empty stub with the panel's attributes and data-src, the report's path relative to the shell; the panel's
# inner HTML becomes that file, fetched by shell.js on navigation. Files: academy/<ctx>/r-<id>.html for a history
# report, academy/<ctx>/<reading id>.html for a markdown course.
SITE = R / 'academy'
STEM = {c['slug'](i): f'r-{i}' for c in HISTORY for i in c['index']}
REPORTS = {}
def split(p):
    s = p.strip()
    head = s[:s.index('>') + 1]
    if ' data-kind="report"' not in head:
        return p
    pid, ctx = re.search(r' id="([^"]+)"', head).group(1), re.search(r' data-ctx="([^"]+)"', head).group(1)
    assert head.endswith(' hidden>') and s.endswith('</section>'), pid
    src = f'{ctx}/{STEM.get(pid, pid)}.html'
    assert src not in REPORTS, src
    REPORTS[src] = s[len(head):-len('</section>')].strip() + '\n'
    return '\n' + head[:-len(' hidden>')] + f' data-src="{src}" hidden></section>'
panels = [split(p) for p in panels]
import shutil
if SITE.exists():
    shutil.rmtree(SITE)   # a report that left the build must leave the site too
for src, body in REPORTS.items():
    (SITE / src).parent.mkdir(parents=True, exist_ok=True)
    (SITE / src).write_text(body)

def root_nav_track(t):
    hist = [c for c in HISTORY if c['theme'] == t['id']]
    mds = [m for m in MD if m['theme'] == t['id']]
    out = ''
    out += ''.join(f'<a class="ditem dcourse" href="#{c["home_id"]}" data-target="{c["home_id"]}" style="--c:{c["color"]}"><span class="n">{c["num"]}</span><span class="t">{c["short"]}<small>{c["card_units"]} units · {c["nrep"]} {"reports" if c["status"] == "available" else "of " + str(c["content_mods"]) + " reports"}</small></span></a>' for c in hist)
    if t['id'] == 'history':
        out += ''.join(f'<div class="dsoon" style="--c:{col}"><span class="n">{k + len(HISTORY) + 1}</span><span class="t">{html.escape(s)}</span><span class="pill">soon</span></div>' for k, (s, _, col, _, _) in enumerate(NEXT))
    out += ''.join(f'<a class="ditem dcourse" href="#{m["home_id"]}" data-target="{m["home_id"]}" style="--c:{m["color"]}"><span class="n">{m["key"]}</span><span class="t">{html.escape(m["short"])}<small>{m["nwritten"]} of {m["nunits"]} units</small></span></a>' for m in mds)
    n = len(hist) + len(mds)
    # a collapsible group (open by default; the reader's choice is remembered): the track label carries its colour
    return (f'<div class="dunit closed" data-unit="track:{t["id"]}" data-open data-ulabel="{html.escape(t["name"]).upper()}" style="--c:{t["color"]}">'
            f'<button class="duh" type="button" aria-expanded="false"><span class="un">■</span><span class="ut">{html.escape(t["name"])}</span><span class="cnt">{n}</span>{ICON_CHEV}</button><div class="ditems">{out}</div></div>')

root_nav = ('<nav class="dlist" data-navctx="root" aria-label="Courses"><div class="dtop"><a class="ditem dhome" href="#home" data-target="home"><span class="n">⌂</span><span class="t">Home</span></a><a class="ditem dhome" href="#changelog" data-target="changelog"><span class="n">≡</span><span class="t">Changelog</span></a><a class="ditem dhome" href="#backlog" data-target="backlog"><span class="n">☐</span><span class="t">Backlog</span></a></div>'
            + ''.join(root_nav_track(t) for t in THEMES) + '</nav>')
navs = root_nav + ''.join(drawer(c) for c in HISTORY) + ''.join(m['nav'] for m in MD)

CSS = open(R / 'shell.css').read()
JS = open(R / 'shell.js').read()

page = f'''<meta charset="utf-8">
<title>Academy</title>
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
  <div class="dfoot mono">{N_LIVE} courses · {ALL_REPORTS} reports · {ALL_WORDS:,} words · {ALL_UNITS} units</div>
</aside>
<main>
{''.join(panels)}
</main>
<script>{JS}</script>
'''
SITE.mkdir(exist_ok=True)
(SITE / 'index.html').write_text(page)
OLD = R / 'personal-mythology.html'   # the single-file page before the split (A2); gone for good
if OLD.exists():
    OLD.unlink()

# the size table in README.md (between the markers), regenerated on every build; verify.py checks it against the files
def kb(n):
    return f'{n / 1024:,.0f} KB' if n < 1024 * 1024 else f'{n / 1024 / 1024:.2f} MB'
rows = [('Shell (`index.html`)', 1, len(page.encode()), len(page.encode()), 'home, drawer, course homes, syllabi, build pages, changelog, backlog')]
for ctx, name in [(c['id'], c['short']) for c in HISTORY] + [(m['id'], m['short']) for m in MD]:
    fs = [len(v.encode()) for k, v in REPORTS.items() if k.startswith(ctx + '/')]
    big = max(((len(v.encode()), k) for k, v in REPORTS.items() if k.startswith(ctx + '/')), default=(0, ''))
    rows.append((f'{name} (`{ctx}/`)', len(fs), sum(fs), big[0], f'largest `{big[1]}`' if big[1] else ''))
allb = sum(r[2] for r in rows)
SIZE_TABLE = ('| Part | Files | Total | Largest file | Note |\n|---|---|---|---|---|\n'
              + ''.join(f'| {a} | {n} | {kb(t)} | {kb(l)} | {note} |\n' for a, n, t, l, note in rows)
              + f'| Whole site | {sum(r[1] for r in rows)} | {kb(allb)} | | the artifact page is capped at 16 MB; the shell must stay under 1 MB |\n')
readme = (R / 'README.md').read_text(encoding='utf-8')
readme = re.sub(r'(<!-- sizes:start -->\n).*?(<!-- sizes:end -->)', lambda mm: mm.group(1) + SIZE_TABLE + mm.group(2), readme, flags=re.S)
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
            n = wc((R / c['frags'] / f'r-{i}.html').read_text())
            q.append(f'| {i} | {c["index"][i]["title"]} | {mdl} | {n:,} |')
q += ['', '## Notes for the reviewer', ''] + [f'- {n}' for n in PROV.get('review_notes', [])]
open(R / 'FABLE-REVIEW.md', 'w').write('\n'.join(q) + '\n')
from biblio import write_all as _biblio
print(f'bibliography: {_biblio()} unit files')
print(' · '.join(f"{c['short']}: {c['nrep']}/{c['content_mods']} reports, {c['words']:,} words" for c in HISTORY)
      + ''.join(f" · {c['short']}: {c['nwritten']}/{c['nunits']} units" for c in MARKDOWN), f'· shell {kb(len(page.encode()))}, {len(REPORTS)} report files, site {kb(allb)}')
print(REVIEW_LINE)
