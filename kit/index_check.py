"""Check docs/courses-index.md against the sources it summarises (docs/academy.md A5).

python3 index_check.py            prints every mismatch, exit 1 if there is one; "courses-index.md matches the sources" otherwise
verify.py runs it too, so ALL CHECKS PASSED includes the index.

The index stays a hand-written Markdown file (its notes, review rows and batch plans have no other home), but every
fact in it that has a source is checked here, so it cannot drift from what the build reads:

  every unit and module   one row each, in the course's table; title as in its syllabus (history) or data file (markdown);
                          rows numbered 1, 2, 3 ... in table order (review and audit rows carry ✓ or —)
  written or not          history: the module is in the course's prompts index; markdown: its file is in the vault
  model                   history: kit/provenance.json (the default model when absent); markdown: the vault file's front
                          matter, or the data file's ORDER for a unit not yet written
  status                  history: written, written · reviewed or written · reviewed (sampled), from provenance (no
                          report is flagged for Fable review since S-NOAUDIT, 15 Nov 2026);
                          markdown: starts "written" (or "rewritten") once filed, "not written" before
  search                  markdown: front matter, or ORDER before writing; history: off
  path                    written: the vault file (both families since P71-3), and every path the cell
                          names exists; not written: the vault path it will be filed at (method.md §7 slug)
  counts                  the "N of M" line above each course's table
  staleness table         one row per filed search-on unit, written date and due date (written + six months)

Not checked: the free text of the notes. (The audit counters were removed with the Fable stage, S-NOAUDIT, 15 Nov 2026.)
"""
import html, importlib.util, json, pathlib, re, sys, unicodedata

KIT = pathlib.Path(__file__).resolve().parent
REPO = KIT.parent
INDEX = REPO / 'docs' / 'courses-index.md'
ARCHIVE = REPO / 'docs' / 'courses-index-archive.md'   # P30-F17 (17 Nov 2026): the finished courses' sections


def index_text():
    """The live index and the archive of finished courses, read as one index."""
    return INDEX.read_text(encoding='utf-8') + ('\n' + ARCHIVE.read_text(encoding='utf-8') if ARCHIVE.exists() else '')
sys.path.insert(0, str(KIT))
from courses import HISTORY, MARKDOWN          # noqa: E402
from howbuilt import front, plus_months        # noqa: E402
import pack                                    # noqa: E402

MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ALIAS = {'gen/': 'generator/', 'vault/': 'courses/'}


def short_date(iso):
    y, m, d = iso.split('-')
    return f'{int(d)} {MON[int(m) - 1]} {y}'


def slug(title):
    """method.md §7: lower case, words joined by hyphens, accents and punctuation dropped."""
    t = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode()
    t = re.sub(r"['\u2019]", '', t)
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')


def sections(txt):
    """{heading: body} for every ## and ### heading."""
    out, parts = {}, re.split(r'^(#{2,3} .+)$', txt, flags=re.M)
    for h, body in zip(parts[1::2], parts[2::2]):
        out[h.lstrip('#').strip()] = body
    return out


def table(body):
    """The first Markdown table in a section: (header cells, rows of cells)."""
    lines = [ln for ln in body.splitlines() if ln.startswith('|')]
    if len(lines) < 2:
        return [], []
    cells = lambda ln: [c.strip() for c in ln.strip().strip('|').split('|')]
    return cells(lines[0]), [cells(ln) for ln in lines[2:]]


def paths_in(cell):
    """Repo paths named in backticks in a cell (bare file names and elided paths skipped)."""
    out = []
    for p in re.findall(r'`([^`]+)`', cell):
        if '/' not in p or '…' in p or ' ' in p:
            continue
        for a, b in ALIAS.items():
            if p.startswith(a):
                p = b + p[len(a):]
        out.append(p)
    return out


def check_paths(label, cell, fails):
    for p in paths_in(cell):
        if not (REPO / p).exists():
            fails.append(f'{label}: path {p} does not exist')


def numbering(label, rows, fails):
    nums = [r[0] for r in rows if re.fullmatch(r'\d+', r[0])]
    if nums != [str(i) for i in range(1, len(nums) + 1)]:
        fails.append(f'{label}: rows not numbered 1 to {len(nums)} in order ({", ".join(nums[:6])} ...)')


def history(c, secs, fails):
    head = next((h for h in secs if h.startswith(f'{c["short"]} (course')), None)
    if not head:
        return fails.append(f'no "### {c["short"]} (course N)" section')
    syl = (KIT / c['syllabus']).read_text()
    mods = {}
    for m in re.finditer(r'<section class="unit" id="u(\d+)"[^>]*>(.*?)</section>', syl, re.S):
        u, body = m.groups()
        for a, t in re.findall(r'data-id="([\d.]+)">.*?<h3>(.*?)</h3>', body, re.S):
            mods[a] = (u, html.unescape(t))
    idx = json.load(open(KIT / c['prompts']))
    prov = json.load(open(KIT / 'provenance.json')).get(c['id'], {})
    content = [a for a, (u, _) in mods.items() if u != c['audit_unit']]
    written = [a for a in content if a in idx]
    hdr, rows = table(secs[head])
    col = {h: i for i, h in enumerate(hdr)}
    lab = f'{c["short"]}'
    numbering(lab, rows, fails)
    seen = {}
    for r in rows:
        a = r[col['Module']]
        if a not in mods:
            continue
        seen[a] = seen.get(a, 0) + 1
        u, title = mods[a]
        L = f'{lab} {a}'
        if r[col['Title']] != title:
            fails.append(f'{L}: title "{r[col["Title"]]}", syllabus has "{title}"')
        if u == c['audit_unit']:
            continue
        st, model, search, path = r[col['Status']], r[col['Model']], r[col['Search']], r[col['Path']]
        if search != 'off':
            fails.append(f'{L}: search "{search}", history modules are search off')
        if a in idx:
            pv = prov.get(a, c['default_model'])
            if model != pv.split(',')[0].strip():
                fails.append(f'{L}: model "{model}", provenance has "{pv}"')
            want = ('reviewed (sampled)' if 'reviewed with Fable 5.1 (sampled)' in pv else
                    'reviewed' if 'reviewed with Fable 5.1' in pv else '')
            got = ('reviewed (sampled)' if 'reviewed (sampled)' in st else 'reviewed' if 'reviewed' in st else
                   'flagged' if 'flagged' in st else '')
            if not st.startswith('written') or got != want:
                fails.append(f'{L}: status "{st}", provenance "{pv}" means "written{" · " + want if want else ""}"')
            want = f'{c["vault"]}/{a}-{slug(title)}.md'          # P71-3: the report is its vault file
            if f'`{want}`' not in path:
                fails.append(f'{L}: path should name `{want}`')
        else:
            if not st.startswith('not written'):
                fails.append(f'{L}: status "{st}", but the module is not in {c["prompts"]}')
            want = f'courses/{c["id"]}/{a}-{slug(title)}.md'
            if f'`{want}`' not in path:
                fails.append(f'{L}: path should name the vault path `{want}`')
            continue                                   # a path not yet written cannot exist
        check_paths(L, path, fails)
    for a in mods:
        if seen.get(a, 0) != 1:
            fails.append(f'{lab} {a}: {seen.get(a, 0)} rows, expected one')
    want = f'{len(written)} of {len(content)} content reports'
    if want not in secs[head] or f'{len(mods)} modules with the audit unit' not in secs[head]:
        fails.append(f'{lab}: the line above the table should say "{want}" and "{len(mods)} modules with the audit unit"')


def markdown(c, secs, fails, stale_want):
    head = c['short']
    if head not in secs:
        return fails.append(f'no "## {head}" section')
    d = pack.load(c)                    # S-DEC2: the course's pack
    units = {u[0]: (sc['key'], u[1]) for sc in d.COURSES for u in sc['units']}
    order = {o[0]: o for o in d.ORDER}
    vault = {}
    for f in sorted((REPO / c['vault']).glob('*.md')):
        fm = front(f)
        if fm.get('code'):
            vault[fm['code']] = (f, fm)
    hdr, rows = table(secs[head])
    col = {h: i for i, h in enumerate(hdr)}
    numbering(head, rows, fails)
    seen = {}
    for r in rows:
        code = r[col['Unit']]
        L = f'{head} {code}'
        if code not in units:
            check_paths(L, r[col['Path']], fails)
            continue
        seen[code] = seen.get(code, 0) + 1
        key, title = units[code]
        st, model, search, path = r[col['Status']], r[col['Model']], r[col['Search']], r[col['Path']]
        if r[col['Title']] != title:
            fails.append(f'{L}: title "{r[col["Title"]]}", data file has "{title}"')
        if r[col['Course']] != key:
            fails.append(f'{L}: course "{r[col["Course"]]}", data file has {key}')
        if code in vault:
            f, fm = vault[code]
            if not re.match(r'(re)?written\b', st):
                fails.append(f'{L}: status "{st}", but {f.relative_to(REPO)} is filed')
            if model != fm.get('model'):
                fails.append(f'{L}: model "{model}", front matter has "{fm.get("model")}"')
            if search.split(' ')[0] != fm.get('search'):
                fails.append(f'{L}: search "{search}", front matter has "{fm.get("search")}"')
            if f'`{f.relative_to(REPO)}`' not in path:
                fails.append(f'{L}: path should name `{f.relative_to(REPO)}`')
            chk = REPO / 'audits' / (REPO / c['vault']).name / f'fresh-check-{code}.md'
            if chk.exists() and str(chk.relative_to(REPO)) not in r[col['Status']] + path:
                fails.append(f'{L}: the row should name its fresh check `{chk.relative_to(REPO)}`')
        else:
            if not st.startswith('not written'):
                fails.append(f'{L}: status "{st}", but no file for {code} is in {c["vault"]}/')
            if code in order and (model != order[code][1] or search != order[code][2]):
                fails.append(f'{L}: model/search "{model}"/"{search}", ORDER has "{order[code][1]}"/"{order[code][2]}"')
            want = f'{c["vault"]}/{code}-{slug(title)}.md'
            if f'`{want}`' not in path:
                fails.append(f'{L}: path should name the vault path `{want}`')
            continue
        check_paths(L, path, fails)
    for code in units:
        if seen.get(code, 0) != 1:
            fails.append(f'{head} {code}: {seen.get(code, 0)} rows, expected one')
    want = f'{len(vault)} of {len(units)} written'
    if want not in secs[head]:
        fails.append(f'{head}: the line above the table should say "{want}"')
    for code, (f, fm) in vault.items():
        if fm.get('search') == 'on' and fm.get('written'):
            stale_want[code] = (short_date(fm['written']), short_date(plus_months(fm['written'], 6)))


def check():
    fails, stale_want = [], {}
    if not INDEX.exists():
        return [f'{INDEX.relative_to(REPO)} is missing']
    secs = sections(index_text())
    for c in HISTORY:
        history(c, secs, fails)
    for c in MARKDOWN:
        markdown(c, secs, fails, stale_want)
    st = next((h for h in secs if h.startswith('Staleness checks due')), None)
    if not st:
        fails.append('no "## Staleness checks due" section')
    else:
        _, rows = table(secs[st])
        got = {r[0]: r for r in rows}
        for code, (w, due) in stale_want.items():
            if code not in got:
                fails.append(f'staleness: no row for {code} (written {w}, due {due})')
            elif not got[code][1].startswith(w) or got[code][2] != due:
                fails.append(f'staleness {code}: "{got[code][1]}" / "{got[code][2]}", expected written {w}, due {due}')
        for code in got:
            if code not in stale_want:
                fails.append(f'staleness: row for {code}, which is not a filed search-on unit')
    return fails


if __name__ == '__main__':
    f = check()
    print('\n'.join('FAIL ' + x for x in f) if f else 'courses-index.md matches the sources')
    sys.exit(1 if f else 0)
