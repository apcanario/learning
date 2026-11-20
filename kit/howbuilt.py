"""A4 of docs/academy.md: one generated "How it was built" page per course.

Every fact on the page is read from a file at build time; nothing on it is typed here. The words this module adds
are headings, column labels and the sentences that say where each fact comes from.

  the method in force       the brand's [howbuilt] `method` doc (academy: docs/method.md) section 1 (the course family's
                            column, `method_columns`, and the common rule)
  the sources policy        the brand's `sourcing` doc (academy: docs/sourcing-standard.md), Part 1 and the course's own
                            part (`sourcing_part`, else the brand's `sourcing_parts`); a brand without them shows neither
  history courses           courses/<course>/inputs/provenance.json (model per report, dates, the course's artefacts)
                            and kit/provenance.json (the kit's artefacts, review_notes); kit/reviews/<folder>/
                            (the quality pass and the fresh checks: verdict per report, date and model from BRIEF.md);
                            kit/audits/<course>-*.md (the Fable audits: date and model from their "Run with" line,
                            verdict, mean and factual errors from each scorecard); courses/<course>/bibliography/r-<id>.md
  markdown courses          courses/<slug>/*.md front matter (code, title, model, written, search); the data file's
                            AUDIT_LOG, STATUS and DONE_ROWS; audits/<slug>/fresh-check-<code>.md front matter

Links to files point at the file in the repo on GitHub (the repo is private: they open for its owner). P24 (Pedro, 16 Nov
2026): the audit files stay private, and every page says so in one line (PRIVATE), above its first file link.
The site's Changelog page stays the cross-course record.
"""
import calendar, datetime, html, json, pathlib, re, subprocess
import pack   # S-DEC2: a markdown course's data file, for the footer
from courses import HISTORY, path as cpath, provenance   # S-DEC5: a history course's inputs in its folder

e = html.escape
KIT = pathlib.Path(__file__).resolve().parent
REPO = KIT.parent
DOCS = REPO / 'docs'
REVIEW_KIND = {'2026-quality-pass': 'Quality pass', 'units-9-13': 'Fresh check'}   # labels for the two review folders
# S-DEC5 (20 Nov 2026): the brand's [howbuilt] table, set by build.py: `method` (the repo path of the method doc whose
# section 1 is "The method in force") with `method_columns` (its table's column for each course family), `sourcing`
# (the sourcing standard's path) with `sourcing_parts` (each family's part). A brand without them gets neither section
# and no link to either doc in the footer; the column names and parts were typed here before (FAMILY_COL, SOURCING_PART)
HB = {}


def _github():
    """The repo's GitHub address and branch, from git; files are linked there."""
    def git(*a):
        try:
            return subprocess.run(['git', '-C', str(REPO), *a], capture_output=True, text=True, check=True).stdout.strip()
        except Exception:
            return ''
    url = git('remote', 'get-url', 'origin')
    url = re.sub(r'\.git$', '', re.sub(r'^git@github\.com:', 'https://github.com/', url))
    url = re.sub(r'https://[^@/]+@', 'https://', url)
    head = git('symbolic-ref', '--short', 'refs/remotes/origin/HEAD')
    return url, (head.split('/', 1)[1] if '/' in head else 'main')

GH, BRANCH = _github()
# S-DEC3: the site name and the repo link base come from the edition's brand (brands/<name>.toml `name`, `repo`):
# build.py sets SITE_NAME and GH before it builds a page; GH from git stays the default for the other tools
SITE_NAME = None


def gh(path, label=None):
    """A link to a repo file on GitHub; path is relative to the repo root; the label defaults to the file name."""
    p = pathlib.PurePosixPath(path)
    return f'<a href="{e(GH)}/blob/{BRANCH}/{e(str(p))}" target="_blank" rel="noopener">{e(label or p.name)}</a>'


def date_long(iso):
    d = datetime.date.fromisoformat(iso)
    return f'{d.day} {d.strftime("%B")} {d.year}'


def plus_months(iso, n):
    """The date n months after iso (the staleness rule, method.md §6), clamped to the month's last day."""
    d = datetime.date.fromisoformat(iso)
    y, m = divmod(d.month - 1 + n, 12)
    y, m = d.year + y, m + 1
    return datetime.date(y, m, min(d.day, calendar.monthrange(y, m)[1])).isoformat()


def front(path):
    """A Markdown file's front matter as a dict (flat key: value lines). A value in matching quotes is read without them
    (P91: IA2's quoted title showed its quotes on What's new and the shelf)."""
    m = re.match(r'---\n(.*?)\n---\n', path.read_text(encoding='utf-8'), re.S)
    return {k: re.sub(r'^(["\'])(.*)\1$', r'\2', v.strip()) for k, v in re.findall(r'^(\w+):\s*(.*)$', m.group(1), re.M)} if m else {}


# ---- shared sections: the method and the sources policy, read from docs/ ----------------------------------------

def method_rows(family):
    """docs/method.md section 1: (topic, this family's practice, common rule), parsed from its table."""
    txt = (REPO / HB['method']).read_text(encoding='utf-8')
    sec = re.search(r'^## 1 · .*?$(.*?)^## ', txt, re.S | re.M).group(1)
    rows = [[c.strip() for c in ln.strip().strip('|').split('|')] for ln in sec.split('\n') if ln.startswith('|')]
    head, body = rows[0], rows[2:]
    i = head.index(HB['method_columns'][family])
    j = head.index('Common rule')
    return [(r[0], r[i], r[j]) for r in body]


def sourcing_parts(family, part=None):
    """docs/sourcing-standard.md: [(heading, lines)] for Part 1 and the family's part (or the course's own `sourcing_part`)."""
    txt = (REPO / HB['sourcing']).read_text(encoding='utf-8')
    out = []
    for m in re.finditer(r'^## (Part \d[^\n]*)\n(.*?)(?=^## |\Z)', txt, re.S | re.M):
        if m.group(1).startswith(('Part 1', part or HB['sourcing_parts'][family])):
            out.append((m.group(1), [ln.replace('- [ ] ', '- ') for ln in m.group(2).split('\n')]))
    return out


def method_decisions():
    """docs/method.md section 1: each decision's name, its pick and its override line (with any 'Triggered' note)."""
    txt = (REPO / HB['method']).read_text(encoding='utf-8')
    sec = re.search(r'^## 1 · .*?$(.*?)^## ', txt, re.S | re.M).group(1)
    return re.findall(r'^\*\*([^*]+?)\.\*\* Pick: (.*?)$.*?^Override if: (.*?)$', sec, re.S | re.M)


def method_section(family, md_inline):
    if not HB.get('method'):
        return ''
    col = HB['method_columns'][family]
    doc = pathlib.PurePosixPath(HB['method']).name
    rows = ''.join(f'<tr><td>{md_inline(t)}</td><td>{md_inline(a)}</td><td>{md_inline(b)}</td></tr>' for t, a, b in method_rows(family))
    picks = ''.join(f'<li><strong>{md_inline(n)}.</strong> Pick: {md_inline(p)} <em>Override if:</em> {md_inline(o)}</li>' for n, p, o in method_decisions())
    return (f'<details class="howto rules"><summary><h2>The method in force</h2><span>{e(doc)} §1</span></summary>'
            f'<p class="hnote">From {gh(HB["method"])} §1: where {e(col)}\'s own method differed from the other course family\'s, and the common rule that holds now. Units written before the merge stay valid as they were written.</p>'
            f'<div class="report"><div class="tbl"><table><thead><tr><th>Topic</th><th>{e(col)} before the merge</th><th>Common rule, in force</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div></div>'
            f'<details class="prompt"><summary>The decisions and their overrides</summary><div class="report"><ul>{picks}</ul></div></details></details>')


def sources_section(family, md_blocks, part=None):
    if not HB.get('sourcing'):
        return ''
    parts = ''.join(f'<details class="prompt"><summary>{e(h)}</summary><div class="report">{md_blocks(lines)}</div></details>' for h, lines in sourcing_parts(family, part))
    return (f'<details class="howto rules"><summary><h2>The sources policy</h2><span>{e(pathlib.PurePosixPath(HB["sourcing"]).name)}</span></summary>'
            f'<p class="hnote">From {gh(HB["sourcing"])}: Part 1 applies to every course, the second part to this one. A unit must pass both.</p>{parts}</details>')


SET_NAME = {'game-icons': 'game-icons.net', 'phosphor': 'Phosphor Icons', 'tabler': 'Tabler Icons'}
SET_LIC = {'game-icons': 'CC BY 3.0, as its repository states it', 'phosphor': 'MIT, its copyright and permission notice', 'tabler': 'MIT, its copyright and permission notice'}


def credits_section(pages, course):
    """P95: "Illustration credits": every object relief shown on this course's reading pages (pages: panel id to its
    label), from design/outlines/uses.json, with the caption printed under it (its credit), the source file and the
    commit it was taken at, from outlines.json; the size of the library for this course; and (P95 check A: the MIT
    licence asks that its notice go with every copy) each set's licence file in full, from design/outlines/licences/."""
    import mdcourse
    lib = [o for o in mdcourse._LIB.values() if course in o['courses']]
    rows = ''
    for pid, label in pages.items():
        oid = mdcourse.USES.get(pid)
        if not oid:
            continue
        o = mdcourse._LIB[oid]
        s = o['source']
        rows += (f'<li><a href="#{pid}" data-target="{pid}">{e(label)}</a>: {e(mdcourse.relief_caption(o))} Taken from '
                 f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["repository"])}, {e(s["path"])}</a> at {e(s["commit"][:7])}.</li>')
    sets = sorted({mdcourse._LIB[mdcourse.USES[pid]]['set'] for pid in pages if pid in mdcourse.USES})
    lic = ''.join(f'<details class="howto rules"><summary><h2>Licence: {e(SET_NAME[k])}</h2><span>{e(SET_LIC[k])}</span></summary>'
                  f'{mdcourse.brief_box((mdcourse.OUTLINES / "licences" / f"{k}.txt").read_text(encoding="utf-8").strip(), "Copy licence")}</details>' for k in sets)
    n = len(lib)
    note = (f'<p class="hnote">The pages of this course that show an object relief, each an outline from an open icon set drawn as the '
            f'lines of a relief map of its silhouette, credited as its licence asks. The library ({gh("design/outlines/outlines.json")}) '
            f'holds {n} outline{"s" if n != 1 else ""} for this course, each taken because its texts name the object.</p>')
    return (f'<section class="howto" style="--hc:var(--teal)"><h2>Illustration credits</h2>{note}'
            + (f'<ul>{rows}</ul>' if rows else '<p>No reading page of this course shows a relief yet.</p>') + '</section>' + lic)


PRIVATE = ('<p class="hnote" data-private="">The audit and review files linked here are kept in a private repository and open '
           'only for the site\'s owner.</p>')   # P24 (16 Nov 2026): nothing private is published; the links stay, and say so


def flags_section(flags):
    body = '<ul>' + ''.join(f'<li>{f}</li>' for f in flags) + '</ul>' if flags else '<p>None open.</p>'
    return f'<section class="howto edge" style="--hc:var(--red)"><h2>Flags still open</h2>{body}</section>'


def stats(items):
    return f'<div class="stats" data-n="{len(items)}">' + ''.join(f'<div><b>{e(str(v))}</b><span>{e(t)}</span></div>' for v, t in items) + '</div>'


def panel(pid, ctx, color, label, body, kind='build'):
    return (f'<section class="panel stack" id="{pid}" data-ctx="{ctx}" data-kind="{kind}" data-t="How it was built" data-u="{e(label)}" '
            f'data-c="{color}" data-split="built" style="--cc:{color}" hidden>{body}</section>')


def doc_links():
    """The footer's links to the brand's method and sourcing docs (HB), those it names."""
    return [gh(HB[k]) for k in ('method', 'sourcing') if HB.get(k)]


def footer(sources):
    return (f'<p class="hnote">Generated by <code>kit/build.py</code> from {", ".join(sources)}. Nothing on this page is typed by hand; '
            f'a change to it is a change to one of those files. What was done, area by area, is in the '
            f'<a href="#changelog" data-target="changelog">Changelog</a>.</p>')


# ---- history courses ---------------------------------------------------------------------------------------------

def _review_folders():
    """Each kit/reviews/<folder>: its label, date and model (from BRIEF.md's first paragraph)."""
    out = []
    for d in sorted((KIT / 'reviews').iterdir()):
        brief = d / 'BRIEF.md'
        if not d.is_dir() or not brief.exists():
            continue
        m = re.search(r'(?:Session of|Sessions from) (\d{1,2} \w+ \d{4}), run with (.+?)\.(?:\s|$)', brief.read_text(encoding='utf-8'))
        out.append(dict(folder=d.name, path=d, label=REVIEW_KIND.get(d.name, d.name), date=m.group(1) if m else '', model=m.group(2) if m else ''))
    return out


def _run_line(txt):
    """An audit file's 'Run with <model>, <date>' line: (model, date)."""
    m = re.search(r'^Run with ([^,]+), (\d{1,2} \w+ \d{4})', txt, re.M)
    return (m.group(1), m.group(2)) if m else ('', '')


def _scorecard(txt):
    """A Fable scorecard: verdict word, mean and factual errors (None where the file does not give one)."""
    v = re.search(r'^## Verdict\s*\n+(.+)$', txt, re.M)
    verdict = re.match(r'\s*(\w+)', v.group(1)).group(1).lower() if v else None
    mean = None
    s = re.search(r'^## (?:\d+ )?Scores\s*\n(.*?)(?=^## )', txt, re.S | re.M)
    if s:
        rows = [ln for ln in s.group(1).split('\n') if ln.startswith('|') and not ln.startswith('|--')]
        if len(rows) >= 2:
            mean = rows[1].strip().strip('|').split('|')[-1].strip()
    err = re.search(r'Factual errors:\s*(\d+)', v.group(1)) if v else None
    return verdict, mean, (int(err.group(1)) if err else None)


def _audits(course):
    """kit/audits/<course>-*.md: [{path, id (13.2), title, model, date, reports (ids the file is about), scorecard}]."""
    out = []
    for f in sorted((KIT / 'audits').glob(f'{course}-*.md'), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', p.name)]):
        txt = f.read_text(encoding='utf-8')
        model, date = _run_line(txt)
        aid = re.match(rf'{course}-(\d+\.\d+)', f.name).group(1)
        rep = re.search(r'-r-([\d.]+(?:-[\d.]+)?)\.md$', f.name)
        ids = rep.group(1).split('-') if rep else []
        title = re.match(r'#\s*(.*)', txt).group(1) if txt.startswith('#') else f.name
        out.append(dict(path=f, id=aid, title=title, model=model, date=date, reports=ids, scorecard=_scorecard(txt) if ids and 'Scores' in txt else None))
    return out


def history_page(c, crumbs, theme, md_inline, md_blocks, flagged, unchecked):
    """The "How it was built" panel of a history course; c is the course dict after build.py:load."""
    cid, prov = c['id'], c['prov']
    PROV = provenance()   # S-DEC5: kit/provenance.json with each history course's own part
    own = json.loads(cpath(c, 'provenance').read_text(encoding='utf-8')).get('artefacts', {})
    folders = _review_folders()
    audits = _audits(cid)
    by_report = {}
    for a in audits:
        for i in a['reports']:
            by_report.setdefault(i, []).append(a)

    def rel(p):
        return p.relative_to(REPO).as_posix()

    # who wrote each report, and every check run on it
    models = {}
    groups = ''
    for u, name, why, mods in c['units']:
        written = [m for m in mods if m[0] in c['done']]
        if not written:
            continue
        rows = ''
        for mid, t, w in written:
            model = prov.get(mid, c['default_model'])
            models[model] = models.get(model, 0) + 1
            # P91 (4 Nov 2026): the report's written date, from provenance.json's `written` map (p91_dates.py: the work
            # session that filed it, from CHANGELOG.md); a session that ran over several days gives its first day, marked
            when = PROV.get('written', {}).get(cid, {}).get(mid)
            approx = mid in PROV.get('written_approx', {}).get(cid, [])
            when = f'<br><small>{e(date_long(when))}{" (approximate: its session ran over several days)" if approx else ""}</small>' if when else '<br><small>date not recorded</small>'
            pills = (' <span class="pill unck">unchecked</span>' if unchecked(model) else '')
            checks = []
            for fo in folders:
                f = fo['path'] / f'{cid}-{mid}.md'
                if f.exists():
                    v = re.search(r'^Verdict:\s*(\w+)', f.read_text(encoding='utf-8'), re.M)
                    checks.append(f'{fo["label"]} ({e(fo["model"])}, {e(fo["date"])}): {e(v.group(1)) if v else "no verdict line"} · {gh(rel(f))}')
            for a in by_report.get(mid, []):
                sc = a['scorecard']
                what = ''
                if sc:
                    what = ': ' + ', '.join(x for x in [sc[0], f'mean {sc[1]}' if sc[1] else '', (f'{sc[2]} factual error{"s" if sc[2] != 1 else ""}' if sc[2] is not None else '')] if x)
                checks.append(f'Audit {e(a["id"])} ({e(a["model"])}, {e(a["date"])}){what} · {gh(rel(a["path"]))}')
            files = []
            for fo in folders:
                f = fo['path'] / f'{cid}-{mid}-writer.md'
                if f.exists():
                    files.append(f'writer\'s unsure list {gh(rel(f))}')
            b = cpath(c, 'bibliography') / f'r-{mid}.md'
            if b.exists():
                files.append(f'bibliography {gh(rel(b))}')
            rows += (f'<tr data-mod="{e(mid)}"><td><a href="#{c["slug"](mid)}" data-target="{c["slug"](mid)}">{e(mid)}</a> {e(t)}</td><td>{e(model)}{pills}{when}</td>'
                     f'<td>{"<br>".join(checks) if checks else "none on file"}</td><td>{"<br>".join(files) if files else "none"}</td></tr>')
        groups += (f'<details class="prompt"><summary>Unit {e(u)} · {e(name)} · {len(written)} of {len(mods)} written</summary>'
                   f'<div class="report"><div class="tbl"><table><thead><tr><th>Report</th><th>Written with, and when</th><th>Checks and audits</th><th>Files</th></tr></thead>'
                   f'<tbody>{rows}</tbody></table></div></div></details>')

    # the course's own material other than reports, and the kit-wide material, from provenance.json artefacts
    # S-DEC5: the course's own artefacts are the ones in its own provenance file; their keys are labels of what was
    # edited when (`courses.py:GREECE` names the file the course's dict sat in then), kept as they were
    own_keys = [k for k in PROV.get('artefacts', {}) if k in own]
    def art_rows(keys):
        return ''.join(f'<tr><td><code>{e(k)}</code></td><td>{e(PROV["artefacts"][k]["model"])}</td><td>{e(PROV["artefacts"][k].get("review", ""))}</td><td>{e(PROV["artefacts"][k]["what"])}</td></tr>' for k in keys)
    art_head = '<thead><tr><th>Item</th><th>Model</th><th>Review</th><th>What</th></tr></thead>'
    others = {k for h in HISTORY for k in json.loads(cpath(h, 'provenance').read_text(encoding='utf-8')).get('artefacts', {})}
    other_keys = [k for k in PROV.get('artefacts', {}) if k not in others]

    # audits and checks run, newest information from the files themselves
    arows = ''.join(f'<div class="logrow"><span class="dt">{e(a["date"])}</span><span><strong>{e(a["id"])}</strong> · {e(a["title"])} · {e(a["model"])}'
                    f'{" · " + e(a["scorecard"][0]) if a["scorecard"] and a["scorecard"][0] else ""} · {gh(rel(a["path"]))}</span></div>' for a in audits)
    for fo in folders:
        n = sum(1 for f in fo['path'].glob(f'{cid}-*.md') if re.fullmatch(rf'{cid}-[\d.]+\.md', f.name))
        if n:
            arows += f'<div class="logrow"><span class="dt">{e(fo["date"])}</span><span><strong>{e(fo["label"])}</strong> · {n} {c["short"]} file{"s" if n != 1 else ""} · {e(fo["model"])} · {gh(rel(fo["path"] / "BRIEF.md"), "the brief")}</span></div>'

    # flags still open
    flags = []
    # S-NOAUDIT (15 Nov 2026): the Fable stage is closed, so nothing is flagged for want of a Fable 5.1 review
    un = [i for i in c['index'] if unchecked(prov.get(i, ''))]
    if un:
        flags.append(f'Registered before their fresh check: {", ".join(un)}.')
    # review notes that name this course
    word = c.get('notes_match') or re.escape(c['short'])   # course.toml `notes_match` (M6, S-DEC4): a regex; absent, the course's short name
    notes = [n for n in PROV.get('review_notes', []) if re.search(word, n)]
    notes_html = ''.join(f'<li>{e(n)}</li>' for n in notes)

    reviewed = sum(1 for i in c['index'] if 'reviewed with Fable 5.1' in prov.get(i, c['default_model']))
    by_model = ' · '.join(f'{n} {e(m)}' for m, n in sorted(models.items(), key=lambda x: -x[1]))
    color = c['color']
    t = theme[c['theme']]
    body = f'''
  <header class="hero">
    {crumbs((SITE_NAME, 'home'), (c['short'], c['home_id']), ('How it was built', None))}
    <div class="eyebrow"><span class="u" style="--c:{color}">{c['label']}</span> · <span class="u" style="--c:var(--gold)">HOW IT WAS BUILT</span> · from provenance.json, the reviews and the audits</div>
    <h1>{e(c['short'])}: how it was built</h1>
    <p class="lede">The model that wrote each of the {c['nrep']} reports, every check and audit run on it with its verdict, the flags still open, and the rules the course was written to. Reports by provenance: {by_model}.</p>
    {stats([(c['nrep'], f'of {c["content_mods"]} reports written'), (sum(1 for i in c['index'] if prov.get(i, c['default_model']).startswith('Fable 5.1')), 'written with Fable 5.1'), (reviewed, 'reviewed with Fable 5.1')])}
  </header>
  {PRIVATE}
  {flags_section(flags)}
  <h2 class="hsec">Who wrote what, and the checks run</h2>
  <p class="hnote">One table per syllabus unit. "Written with" is the report's entry in {gh(c["provenance"])}. Checks come from the review folders ({", ".join(gh(rel(fo["path"] / "BRIEF.md"), fo["label"].lower() + " brief") for fo in folders)}) and the Fable audits in <code>kit/audits/</code>. Under the model is the date the report was filed, from the same file's <code>written</code> map: the date of the work session that filed it, read from the Changelog (P91); where that session ran over several days, its first day, marked approximate.</p>
  <div>{groups}</div>
  <section class="howto" style="--hc:var(--gold)"><h2>Audits and checks run</h2>{f'<div class="logrows">{arows}</div>' if arows else '<p>None yet.</p>'}</section>
  <details class="howto rules"><summary><h2>Course material other than reports</h2><span>{len(own_keys)} item{"s" if len(own_keys) != 1 else ""}</span></summary>
    <div class="report"><div class="tbl"><table>{art_head}<tbody>{art_rows(own_keys)}</tbody></table></div></div>
    <p class="hnote">Shared by the history courses (the kit's spec, brief, code, reviews, audits and bibliographies):</p>
    <div class="report"><div class="tbl"><table>{art_head}<tbody>{art_rows(other_keys)}</tbody></table></div></div>
  </details>
  <details class="howto rules"><summary><h2>Review notes</h2><span>{len(notes)} naming {e(c['short'])}</span></summary><ul>{notes_html}</ul></details>
  {credits_section({c['slug'](i): i for i in c['index']}, cid)}
  {method_section('history', md_inline)}
  {sources_section('history', md_blocks)}
  {footer([gh(c['provenance']), '<code>kit/reviews/</code>', '<code>kit/audits/</code>', *doc_links()])}'''
    return panel(f'{c["home_id"]}-built', cid, color, c['label'], body)


# ---- markdown courses ----------------------------------------------------------------------------------------------

def _audit_log_units(d):
    """The data file's AUDIT_LOG: [(date, name, {code: verdict}, files mentioned)] from each row's text."""
    out = []
    for dt, txt in d.AUDIT_LOG:
        name = re.match(r'\s*([^(.]+?)\s*\(', txt)
        seg = re.search(r'Units?:\s*(.*?)\.\s', txt)
        codes = re.findall(r'(?<![\w-])((?:DD-)?[A-Z]+\d+)(?![\w])', seg.group(1)) if seg else []
        verdicts = {}
        for who, what in re.findall(r'<strong>([^<:]+):(.*?)</strong>', txt):
            v = re.findall(r'\b(PASS|REWRITE|FULL AUDIT)\b', what)
            for code in re.findall(r'(?:DD-)?[A-Z]+\d+', who):
                if v:
                    verdicts[code] = v[-1]
        files = re.findall(r'<code>(audits/[^<]+)</code>', txt)
        out.append((dt, name.group(1) if name else 'Audit', {c: verdicts.get(c, 'named') for c in codes}, files))
    return out


def markdown_page(m, crumbs, theme, md_inline, md_blocks):
    """The "How it was built" panel of a markdown Academy course; m is a course dict from build.py:md_courses."""
    c, sc, d = m['parent'], m['sc'], m['parent']['hub']
    ctx, key, col = m['id'], sc['key'], m['color']
    vault = c['vault']                                     # courses/<slug>/, the source of the units (A5)
    slug = vault.name
    adir = REPO / 'audits' / slug
    codes = [u[0] for u in sc['units']]
    titles = {u[0]: u[1] for u in sc['units']}

    units = {}
    misfiled = []
    for code, (f, fm) in c['vault_units'].items():         # read once by build.py:load_markdown
        if code not in codes:
            continue
        parts = fm.get('course', '').split(' · ')
        if len(parts) > 1 and parts[1] == key:
            units[code] = dict(fm, path=f)
        else:
            misfiled.append(code)
    checks = {}
    for f in sorted(adir.glob('fresh-check-*.md')):
        fm = front(f)
        code = f.stem[len('fresh-check-'):]
        if code in codes:
            checks[code] = dict(fm, path=f)
    log = _audit_log_units(d)
    audited = {}
    for dt, name, vs, files in log:
        for code, v in vs.items():
            if code in codes:
                audited.setdefault(code, []).append((dt, name, v, files))

    def rel(p):
        return p.relative_to(REPO).as_posix()

    def audit_files(files):
        return ''.join(' · ' + gh(fp) for fp in files if (REPO / fp).exists() and not pathlib.PurePosixPath(fp).name.startswith('fresh-check-'))

    rows, flags, models = '', [], {}
    in_order = [x[0] for x in d.ORDER]
    order = [x for x in in_order if x in units] + [x for x in codes if x in units and x not in in_order]
    for code in order:
        u = units[code]
        models[u['model']] = models.get(u['model'], 0) + 1
        rid = d.WRITTEN.get(code)
        name = f'<a href="#{rid}" data-target="{rid}">{e(code)}</a> {e(u["title"])}' if rid else f'{e(code)} {e(u["title"])}'
        st = d.STATUS.get(code, '')
        made = f'{e(u["model"])} · {e(date_long(u["written"]))} · search {e(u["search"])}{" · " + e(st) if st else ""}'
        ch = []
        if code in checks:
            k = checks[code]
            ch.append(f'Fresh check ({e(k.get("model", ""))}, {e(date_long(k["date"]))}): {e(k.get("verdict", ""))} · {gh(rel(k["path"]))}'
                      + (f' · <a href="{e(k["chat"])}" target="_blank" rel="noopener">chat</a>' if k.get('chat', '').startswith('https://') else ''))
        else:
            ch.append('no fresh check on file')
        for dt, an, v, files in audited.get(code, []):
            ch.append(f'{e(an)} ({e(dt)}): {e(v)}' + audit_files(files))
            if v == 'REWRITE' and 'rewritten' not in st:
                flags.append(f'{e(code)}: {e(an)} verdict REWRITE is open; no new unit starts until it is rewritten.')
        due = plus_months(u['written'], 6) if u.get('search') == 'on' else ''
        if due:
            ch.append(f'staleness check due {e(date_long(due))}')
        rows += (f'<tr data-unit="{e(code)}"><td>{name}<br>{gh(rel(u["path"]), "vault file")}</td><td>{made}</td><td>{"<br>".join(ch)}</td></tr>')

    stale = sorted((plus_months(units[x]['written'], 6), x) for x in order if units[x].get('search') == 'on')
    if stale:
        flags.append('Staleness checks owed (search on, six months after writing): ' + '; '.join(f'{e(x)} on {e(date_long(dd))}' for dd, x in stale) + '.')
    if misfiled:
        flags.append(f'Filed in <code>courses/{slug}/</code> with a front-matter <code>course</code> line that does not name course {e(key)}: {", ".join(misfiled)}.')

    # earlier material for this course (DONE_ROWS), and the superseded readings kept as the record
    earlier = [r for r in d.DONE_ROWS if any(x in codes for x in re.findall(r'(?:DD-)?[A-Z]+\d+', r[1]))]
    earlier_html = ''.join(f'<li><strong>{e(r[1])}</strong> · {e(r[2])} · {e(r[3])} · search {e(r[4])} · {e(r[5])}</li>' for r in earlier)
    kept = [r for r in d.READINGS if r['course'] == key and not r['covers']]
    earlier_html += ''.join(f'<li>Kept as the record: <a href="#{r["id"]}" data-target="{r["id"]}">{e(r["title"])}</a></li>' for r in kept)

    # audit files for this course: its fresh checks, and every other audit file a log row naming its units cites
    arows = ''.join(f'<div class="logrow"><span class="dt">{e(dt)}</span><span><strong>{e(name)}</strong> · {", ".join(e(x) + ": " + e(v) for x, v in vs.items() if x in codes)}{audit_files(files)}</span></div>'
                    for dt, name, vs, files in log if any(x in codes for x in vs))
    arows += ''.join(f'<div class="logrow"><span class="dt">{e(checks[x].get("date", ""))}</span><span><strong>Fresh check</strong> · {e(checks[x].get("unit", x))} · {e(checks[x].get("model", ""))} · {e(checks[x].get("verdict", ""))} · {gh(rel(checks[x]["path"]))}</span></div>'
                     for x in order if x in checks)

    by_model = ' · '.join(f'{n} {e(mm)}' for mm, n in sorted(models.items(), key=lambda x: -x[1]))
    label = m['short'].upper()
    body = f'''
  <header class="hero">
    {crumbs((SITE_NAME, 'home'), (f"Course {key} · {m['short']}", ctx), ('How it was built', None))}
    <div class="eyebrow"><span class="u" style="--c:{col}">{e(label)}</span> · <span class="u" style="--c:var(--gold)">HOW IT WAS BUILT</span> · from the units' front matter and the audit log</div>
    <h1>{e(m['short'])}: how it was built</h1>
    <p class="lede">The model that wrote each of the {len(order)} written units, when, with or without search, every fresh check and audit run on it with its verdict, the flags still open, and the rules the course is written to. Units by model: {by_model or 'none yet'}.</p>
    {stats([(len(order), f'of {len(codes)} units written'), (sum(1 for x in order if x in checks), 'fresh-checked'), (sum(1 for x in order if x in audited), 'in an audit')])}
  </header>
  {PRIVATE}
  {flags_section(flags)}
  <h2 class="hsec">Who wrote what, and the checks run</h2>
  <p class="hnote">One row per written unit, in writing order. Model, date and search flag are the unit's front matter in <code>courses/{e(slug)}/</code>; status is the data file's STATUS; fresh checks are <code>audits/{e(slug)}/fresh-check-&lt;code&gt;.md</code>; audits are the data file's AUDIT_LOG, the record of the audits run before the Fable stage closed (S-NOAUDIT, 15 Nov 2026). Sources cited by the units are on the <a href="#{ctx}-bibliography" data-target="{ctx}-bibliography">Bibliography</a> page.</p>
  <div class="report"><div class="tbl"><table><thead><tr><th>Unit</th><th>Written</th><th>Checks and audits</th></tr></thead><tbody>{rows}</tbody></table></div></div>
  {f'<section class="howto" style="--hc:var(--orange)"><h2>Earlier material</h2><ul>{earlier_html}</ul></section>' if earlier_html else ''}
  <section class="howto" style="--hc:var(--gold)"><h2>Audits and checks run</h2>{f'<div class="logrows">{arows}</div>' if arows else '<p>None yet.</p>'}</section>
  {credits_section(m.get('pages', {}), ctx)}
  {method_section('markdown', md_inline)}
  {sources_section('markdown', md_blocks, c.get('sourcing_part'))}
  {footer([f'<code>courses/{e(slug)}/</code> front matter', f'<code>audits/{e(slug)}/</code>', gh(rel(REPO / pack.source(c))) + ' (AUDIT_LOG, STATUS, DONE_ROWS)', *doc_links()])}'''
    return panel(f'{ctx}-built', ctx, col, label, body)
