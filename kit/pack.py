"""A markdown course's pack: the loader shim that replaces generator/data/<slug>/hub.py (S-DEC2, 20 Nov 2026;
docs/decoupling.md §4). kit/build.py, kit/verify.py, kit/howbuilt.py, kit/index_check.py, kit/next_prompt.py, kit/thin.py
and kit/private_terms.py read a markdown course's data through load(c), data_dir(c) and files(c) here, never by path.

  load(c)       an object with the attribute names hub.py had (COURSES, PRE, AIMS, READINGS, ORDER, STATUS, NEXT_UNIT,
                VERSION, CHANGELOG, DONE_ROWS, AUDIT_LOG, FRAME, BUILD_*, ORDER_*, BRIEFS_LEDE, ...); a new object on every
                call (build.py fills in READINGS paths and sets WRITTEN on it)
  data_dir(c)   the folder of the course's other files (case-*.md, syllabus-flags.md, bibliography.md, research): an
                `md` path of a READINGS entry is relative to it
  files(c)      the course's data files, for private_terms.py (what it scanned in the data folder before)
  source(c)     the repo path the "How it was built" page's footer names as the data file

Two shapes, told apart by the course's `data` key in courses/<slug>/course.toml (until the last course has moved and
generator/ is removed):

  data = "generator/data/<slug>/hub.py"     the old data file, run as a module (data_dir: its folder)
  data = "courses/<slug>/course.toml"       the pack (data_dir: courses/<slug>/notes/)

The pack (one folder, no Python):

  courses/<slug>/course.toml   the registry keys (kit/courses.py) and, under ONE table `[pack]`, the course data;
                               kit/courses.py strips `pack` from the registry dict, so COURSES is unchanged by it
  courses/<slug>/briefs.md     the shared preamble and one brief per unit, word for word
  courses/<slug>/pages/*.md    the course's long copy, one block per file (below)
  courses/<slug>/notes/        everything else the course keeps: case-*.md, syllabus-flags.md, bibliography.md,
                               research, old briefs (a subfolder, so the vault globs of courses/<slug>/*.md never meet them)
  courses/<slug>/<code>-*.md   the units, as before; a unit's reading-page intro is its front matter (below)

The `[pack]` table (every key optional unless marked):

  [pack]
  source = "generator/data/<slug>/hub.py"   the path the How it was built footer names (byte identity until S-DEC3)
  course_note = "..."                       any plain string key becomes the attribute of its name upper-cased:
  order_lede = "..."                        COURSE_NOTE, ORDER_LEDE, ORDER_FOOT, BIB_NOTE, BRIEF_LABEL, BUILD_LEDE,
  order_foot = "..."                        LEARN_LEDE, TITLE, BAR, ... (a key repeating DEFAULTS below is left out)
  learn_tile = ["...", "..."]               an array of strings: a tuple
  version = "v1 · 1 Jan 2027"               only where the top changelog row does not start "v<n>. " (below)
  order = [["B1", "Opus 5.5", "off"], ...]  ORDER: (code, model, search) rows, writing order          (required)
  done_rows = [[...6 cells...], ...]        DONE_ROWS: earlier material, rows of six cells
  [pack.status]                             STATUS overrides, only where the derived string is not the typed one
  A2 = "rewritten 28 Oct"
  [[pack.courses]]                          COURSES, in order: key, name, color, slug, goal, tile, intro, outcomes (required)
  key = "A"  ...
  [[pack.courses.units]]                    the course's units, in order: code, title, scope, deliverable, and aim,
  code = "A1"  title = "..."  ...           takes, gives where the course has Aim lines (AIMS); the brief is briefs.md's
  [[pack.readings]]                         READINGS that are not a unit's: id, md (relative to notes/), course, title,
  id = "read-..."  md = "..."  ...          covers = [], name, intro
  [[pack.changelog]]                        CHANGELOG, newest first: date, text ({A}, {B} = course names)
  [[pack.audit_log]]                        AUDIT_LOG: date, text
  [[pack.template_blocks]]                  any other array of tables: a list of tuples of its values, in key order
                                            (TEMPLATE_BLOCKS: heading, html)

briefs.md: a `## Preamble` section (PRE; `{GOAL}` is filled with the course goal) and one `## <code>` section per unit,
each section's text between the blank line after its heading and the next heading, its final newlines dropped. Text above
the first `## ` is a note for the reader and is not read. A brief holds no line that starts with `## `.

pages/<name>.md: the block NAME (name upper-cased, '-' as '_'), the file's text less its final newline: FRAME (frame.md),
BUILD_BODY, BUILD_PICK, BRIEFS_LEDE, LEARNING_NOTE, ORDER_NOTES, TEMPLATE_NOTE. The blocks are theme-class HTML, which
Markdown cannot express (classes, inline styles, the exact whitespace), so each file holds its block as raw HTML, which
Markdown passes through; the build prints the file's text unchanged, no Markdown conversion (byte identity is the proof).

Derived, never typed (decoupling §4):
  STATUS      every unit filed in the vault: "written <d Mon>" from its front matter `written` (YYYY-MM-DD), unless
              [pack.status] gives the code
  NEXT_UNIT   the first code of ORDER with no file in the vault; "—" when every one is filed
  READINGS    [pack.readings], then one entry per filed unit whose front matter has `intro`, in the courses' unit
              order: id "read-<code lower>", course (its course's key), title (front matter `title`, else the unit's),
              covers [code], name (front matter `name`, else "<code> · <title>"), intro. A filed unit without `intro`
              gets build.py's default page, as before
  VERSION     "<v> · <d Mon YYYY>" from the top changelog row: its text's leading "v<n>. " and its date; [pack]
              `version` where the row has none (only VERSION's first part, "v<n>", is printed: the changelog's label)
  AIMS        {code: (aim, takes, gives)} from the units that carry them
  WRITTEN     set by build.py, as before

DEFAULTS below are the engine's generic copy (identical in every course when it moved); a course key overrides one.
"""
import datetime, importlib.util, json, pathlib, re, tomllib, types

ROOT = pathlib.Path(__file__).resolve().parent.parent

DEFAULTS = dict(
    BUILD_LEDE='Method, model rules, and the pages that hold the briefs and the sources. Nothing here is course content.',
    LEARN_LEDE='Read here. Everything about how the units get written lives in Build.',
    BRIEF_LABEL='Opus brief',
    BIB_NOTE='Every link cited in the written material, alphabetical by title. New units add to this list; a source that fails a staleness check is marked here.',
    LEARNING_NOTE='', BUILD_PICK='', FRAME='',
)
# the [pack] keys that are not a plain attribute
_SPECIAL = {'source', 'version', 'order', 'done_rows', 'status', 'courses', 'readings'}


def is_pack(c):
    return c['data'].endswith('.toml')


def data_dir(c):
    p = ROOT / c['data']
    return p.parent / 'notes' if is_pack(c) else p.parent


def source(c):
    """The data file the How it was built footer names."""
    if not is_pack(c):
        return c['data']
    return _toml(c)['pack'].get('source', c['data'])


def files(c):
    """The course's data files (not its units): before, the .py and .md files of the data folder; now course.toml,
    briefs.md, pages/*.md and the .md files directly in notes/."""
    p = ROOT / c['data']
    if not is_pack(c):
        return sorted(f for f in p.parent.iterdir() if f.suffix in ('.py', '.md'))
    out = [p] + [f for f in [p.parent / 'briefs.md'] if f.exists()]
    out += sorted((p.parent / 'pages').glob('*.md'))
    out += sorted(f for f in data_dir(c).glob('*.md')) if data_dir(c).is_dir() else []
    return out


def _toml(c):
    with open(ROOT / c['data'], 'rb') as f:
        return tomllib.load(f)


def front(path):
    """A Markdown file's front matter (the same reading as howbuilt.front)."""
    m = re.match(r'---\n(.*?)\n---\n', path.read_text(encoding='utf-8'), re.S)
    return {k: re.sub(r'^(["\'])(.*)\1$', r'\2', v.strip()) for k, v in re.findall(r'^(\w+):\s*(.*)$', m.group(1), re.M)} if m else {}


def vault(c):
    """{code: (path, front matter)} of the units filed in the course's vault."""
    out = {}
    v = ROOT / c['vault'] if isinstance(c['vault'], str) else c['vault']
    for f in sorted(v.glob('*.md')) if v.is_dir() else []:
        fm = front(f)
        if fm.get('code'):
            out[fm['code']] = (f, fm)
    return out


def briefs(path):
    """briefs.md: {section name: text}."""
    parts = re.split(r'(?m)^## (.+)\n\n', path.read_text(encoding='utf-8'))
    return {parts[i].strip(): parts[i + 1].rstrip('\n') for i in range(1, len(parts), 2)}


def status_text(written):
    d = datetime.date.fromisoformat(written)
    return f'written {d.day} {d:%b}'


def version(changelog, typed=None):
    if changelog:
        dt, text = changelog[0][0], changelog[0][1]
        m = re.match(r'(v[\d.]+)\. ', text)
        if m:
            d = datetime.date.fromisoformat(dt[:10])
            return f'{m.group(1)} · {d.day} {d:%b %Y}'
    if typed is None:
        raise SystemExit('a pack needs [pack] version when its top changelog row does not start "v<n>. "')
    return typed


def _value(v):
    if isinstance(v, list) and v and all(isinstance(x, dict) for x in v):
        return [tuple(x.values()) for x in v]
    if isinstance(v, list) and v and all(isinstance(x, list) for x in v):
        return [tuple(x) for x in v]
    if isinstance(v, list) and all(isinstance(x, str) for x in v):
        return tuple(v)
    return v


def _old(c):
    spec = importlib.util.spec_from_file_location('hub_' + c['id'].replace('-', '_'), ROOT / c['data'])
    d = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(d)
    return d


def load(c):
    """The course's data as an object with hub.py's attribute names (a fresh object on every call)."""
    if not is_pack(c):
        return _old(c)
    path = ROOT / c['data']
    pk = _toml(c).get('pack')
    if pk is None:
        raise SystemExit(f'{c["data"]}: no [pack] table')
    d = types.SimpleNamespace(**DEFAULTS)
    for k, v in pk.items():
        if k not in _SPECIAL:
            setattr(d, k.upper(), _value(v))
    for f in sorted((path.parent / 'pages').glob('*.md')):
        t = f.read_text(encoding='utf-8')
        setattr(d, f.stem.upper().replace('-', '_'), t[:-1] if t.endswith('\n') else t)
    bf = briefs(path.parent / 'briefs.md')
    if 'Preamble' not in bf:
        raise SystemExit(f'{c["data"]}: briefs.md has no "## Preamble" section')
    d.PRE = bf['Preamble']
    d.AIMS = {}
    d.COURSES = []
    for sc in pk['courses']:
        units = []
        for u in sc.get('units', []):
            if u['code'] not in bf:
                raise SystemExit(f'{c["data"]}: briefs.md has no "## {u["code"]}" section')
            units.append((u['code'], u['title'], u['scope'], u['deliverable'], bf[u['code']]))
            if 'aim' in u:
                d.AIMS[u['code']] = (u['aim'], u['takes'], u['gives'])
        d.COURSES.append(dict({k: v for k, v in sc.items() if k != 'units'}, units=units))
    d.ORDER = [tuple(o) for o in pk['order']]
    d.DONE_ROWS = [tuple(r) for r in pk.get('done_rows', [])]
    d.CHANGELOG = getattr(d, 'CHANGELOG', [])
    d.AUDIT_LOG = getattr(d, 'AUDIT_LOG', [])
    d.VERSION = version(d.CHANGELOG, pk.get('version'))
    # derived from the vault: STATUS, NEXT_UNIT, the units' READINGS
    v = vault(c)
    over = pk.get('status', {})
    d.STATUS = {code: over.get(code) or status_text(fm['written']) for code, (f, fm) in v.items()}
    d.NEXT_UNIT = next((o[0] for o in d.ORDER if o[0] not in v), '—')
    d.READINGS = [dict(r) for r in pk.get('readings', [])]
    for sc in d.COURSES:
        for u in sc['units']:
            if u[0] in v and 'intro' in v[u[0]][1]:
                fm = v[u[0]][1]
                title = fm.get('title', u[1])
                d.READINGS.append(dict(id=f'read-{u[0].lower()}', course=sc['key'], title=title, covers=[u[0]],
                                       name=fm.get('name', f'{u[0]} · {title}'), intro=fm['intro']))
    return d


# ---- filing (kit/thin.py insert, S-DEC2) -------------------------------------------------------------------------------

def toml_str(v):
    """A TOML string: a literal string where it can be, else a basic string (JSON's escapes are TOML's)."""
    if "'" not in v and not re.search(r'[\x00-\x1f\x7f]', v):
        return f"'{v}'"
    return json.dumps(v, ensure_ascii=False)


def insert(c, rec, get):
    """thin.py insert's records.json for a pack: {path: new text}. `get(path)` gives a file's current text (thin.py keeps
    the old text to restore). reading -> the unit's front matter (`intro`, and `name` where it is not "<code> · <title>");
    status -> nothing when it is the derived "written <d Mon>", else a line under [pack.status]; hub_changelog -> a new
    [[pack.changelog]] above the first. next_unit and version are derived: thin.py checks them after the insert."""
    out = {}
    path = ROOT / c['data']
    code = rec['code']
    v = vault(c)
    if ('reading' in rec or 'status' in rec) and code not in v:
        raise ValueError(f'{code} has no file in {c["vault"]}: put the unit, with its front matter, in the vault first')
    d = load(c)
    units = {u[0]: (sc['key'], u) for sc in d.COURSES for u in sc['units']}
    if code not in units:
        raise ValueError(f'{code} is not a unit of {c["data"]}')
    if 'reading' in rec:
        r = rec['reading']
        f, fm = v[code]
        title = fm.get('title', units[code][1][1])
        want = dict(id=f'read-{code.lower()}', course=units[code][0], title=title, covers=[code])
        for k, x in want.items():
            if r.get(k) != x:
                raise ValueError(f'reading.{k} must be {x!r} (derived from the unit), not {r.get(k)!r}')
        if 'intro' in fm:
            raise ValueError(f'{f.name} already has an intro')
        intro = r['intro']
        if intro != intro.strip() or '\n' in intro or re.match(r'^(["\']).*\1$', intro):
            raise ValueError('reading.intro must be one line, without outer quotes or spaces')
        t = get(f)
        m = re.match(r'---\n(.*?)\n---\n', t, re.S)
        add = (f'\nname: {r["name"]}' if r['name'] != f'{code} · {title}' else '') + f'\nintro: {intro}'
        out[f] = t[:m.end(1)] + add + t[m.end(1):]
    if 'status' in rec and rec['status'] != status_text(v[code][1]['written']):
        t = out.get(path) or get(path)
        if t.count('\n[pack.status]\n') != 1:
            raise ValueError(f'{c["data"]}: no [pack.status] table for the status {rec["status"]!r}')
        i = t.index('\n[pack.status]\n') + len('\n[pack.status]\n')
        out[path] = t[:i] + f'{code} = {toml_str(rec["status"])}\n' + t[i:]
    if 'hub_changelog' in rec:
        t = out.get(path) or get(path)
        block = f"[[pack.changelog]]\ndate = {toml_str(rec['date'])}\ntext = {toml_str(rec['hub_changelog'])}\n"
        if '\n[[pack.changelog]]\n' in t:
            i = t.index('\n[[pack.changelog]]\n') + 1
            out[path] = t[:i] + block + t[i:]
        else:
            out[path] = t.rstrip('\n') + '\n\n' + block
    return out
