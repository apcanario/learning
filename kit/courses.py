"""Course data for build.py, read from the repo's data files (S-DEC1, 20 Nov 2026; docs/decoupling.md §4).

  courses/<id>/course.toml   one course: the dict build.py reads (COURSES)
  catalog.toml               `tracks` (THEMES), `next` (NEXT: the planned history courses), `course_order`, `edition_order`
  editions/<name>.toml       one edition (EDITIONS[<name>]); DEFAULT_EDITION is the first in `edition_order`
  brands/<name>.toml         one brand (BRANDS[<name>]; S-DEC3): the site name, copy, rules lines, storage keys,
                             tokens and fonts, chosen by an edition's `brand`; brand(edition) returns it
  catalog.toml `hero`        each track's place on the home hero, taken out of the track into HERO_AT[<track id>]

Adding a course is a folder: courses/<id>/course.toml (and its units). No edit here. A course folder that
`course_order` does not name comes after the named ones, sorted by id; an edition file `edition_order` does not name
likewise. Every course also gets a module name, its id upper-cased with '-' as '_' (GREECE, BRAND_AI), as before.
A folder whose name starts with '_' (courses/_template/) is not a course. A file that does not parse, a course whose
`id` is not its folder name, whose `family` is not 'history' or 'markdown', that lacks a key its family needs or whose
module name is already taken, an edition without `title` or `site` or with `courses` neither "all" nor a list, and an
order entry with no file each stop the build with the file named.

Every course has a `family`: 'history' (Greece, Rome and the eight to come: one Markdown report per module in the vault,
`vault`, since P71-3 (1 Nov 2026; vault.py, mdcourse.history_html), a syllabus with prompts, provenance and a
bibliography folder, all in the course's folder since S-DEC5 and named by `syllabus`, `prompts`, `provenance`, `bibliography`) or
'markdown' (Brand + AI: units as Markdown in the vault, `vault`, read directly since A5; the course data at `data`:
the `[pack]` table of this same course.toml, with briefs.md and pages/ beside it; kit/pack.py reads it, and this
loader drops `pack` from the dict). The root home is Academy and lists every course of both families (docs/academy.md, A1).
A markdown course is built by mdcourse.py from its data file into one Academy course per course in that file (A3).

The home card (P90, 4 Nov 2026) carries one sentence per course, two lines at most: a history course's `tile`, a
markdown course's `tiles` keyed like its `tracks` (the data file's own tile stays on the course's pages). The longer
`card` text the home carried before is gone with it.

Text fields may use these placeholders, filled per course at build time:
{content_mods} modules excluding the audit unit · {total_mods} all modules · {nrep} reports written · {kwords} thousands of words written

What TOML cannot hold, converted here, the same way every time, so the dicts equal the ones courses.py typed before:
  tuples     a course's `parts`, `eras` and `ticks` rows, its `tracks` values, a track's `planned` rows, the `next`
             rows, an edition's `courses` and `omit`: TOML arrays, made tuples (lists inside a row, such as a part's
             units, stay lists)
  None       an edition's `courses = "all"` (every course)
  key order  kept: tomllib keeps the file's order, and a course file writes a nested dict as dotted keys
             (`figure.kind = ...`) so the key keeps its place among the others
  long HTML  `rules` and `spine`: TOML multi-line literal strings ('''), the newline after the opening quotes dropped
  computed   the history timelines' `ticks` positions were f-strings; the files hold the strings they gave
"""
import json
import pathlib
import tomllib

_ROOT = pathlib.Path(__file__).resolve().parent.parent


def _fail(path, msg):
    raise SystemExit(f'{path.relative_to(_ROOT)}: {msg}')


def _load(path):
    try:
        with open(path, 'rb') as f:
            return tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
        _fail(path, e)


def _rows(v):
    return [tuple(r) for r in v]


# the keys a course file cannot do without, by family (build.py reads them before anything else)
_FAMILY_KEYS = {'history': ('syllabus', 'vault', 'prompts', 'provenance', 'bibliography'), 'markdown': ('data', 'vault', 'tracks')}
_TAKEN = {'THEMES', 'NEXT', 'COURSES', 'EDITIONS', 'HISTORY', 'MARKDOWN'}


def _course(path, d):
    folder = path.parent.name
    for k in ('id', 'family'):
        if k not in d:
            _fail(path, f'no `{k}` (required)')
    if d['id'] != folder:
        _fail(path, f'id {d["id"]!r} is not the folder name {folder!r}')
    if d['family'] not in _FAMILY_KEYS:
        _fail(path, f'family {d["family"]!r} is neither "history" nor "markdown"')
    for k in _FAMILY_KEYS[d['family']]:
        if k not in d:
            _fail(path, f'no `{k}` (required for a {d["family"]} course)')
    if d['id'].upper().replace('-', '_') in _TAKEN:
        _fail(path, f'id {d["id"]!r} would take the module name {d["id"].upper().replace("-", "_")}, which kit/courses.py already uses')
    d.pop('pack', None)      # S-DEC2: a markdown course's data, read by kit/pack.py; never part of the registry dict
    for k in ('parts', 'eras', 'ticks'):
        if k in d:
            d[k] = _rows(d[k])
    if 'tracks' in d:
        d['tracks'] = {k: tuple(v) for k, v in d['tracks'].items()}
    return d


def _edition(path, d):
    for k in ('title', 'site', 'brand'):
        if k not in d:
            _fail(path, f'no `{k}` (required)')
    if 'courses' in d:
        if d['courses'] == 'all':
            d['courses'] = None
        elif isinstance(d['courses'], list):
            d['courses'] = tuple(d['courses'])
        else:
            _fail(path, f'courses must be "all" or a list of course ids, not {d["courses"]!r}')
    if 'omit' in d:
        d['omit'] = tuple(d['omit'])
    if d['brand'] not in BRANDS:
        _fail(path, f'brand {d["brand"]!r} has no file brands/{d["brand"]}.toml')
    return d


# S-DEC3: the keys a brand file cannot do without (brands/academy.toml says what each is)
_BRAND_KEYS = ('name', 'mark', 'lede', 'repo', 'id_base', 'fonts_href', 'log_area', 'storage')
_STORAGE_KEYS = ('theme', 'tab', 'units', 'last', 'section')


def _brand(path, d):
    for k in _BRAND_KEYS:
        if k not in d:
            _fail(path, f'no `{k}` (required)')
    for k in _STORAGE_KEYS:
        if k not in d['storage']:
            _fail(path, f'no `storage.{k}` (required)')
    d.setdefault('tokens', {})
    d.setdefault('tokens_light', {})
    d.setdefault('rules', [])
    return d


def _ordered(found, order, where):
    """The names in `order`, each of which must exist, then the rest sorted."""
    missing = [n for n in order if n not in found]
    if missing:
        _fail(_ROOT / 'catalog.toml', f'{where} names {missing}, which has no file')
    return list(order) + sorted(n for n in found if n not in order)


_CATALOG = _load(_ROOT / 'catalog.toml')

# S-DEC3: a track's `hero` (its place on the home hero) leaves the track's dict for HERO_AT, so THEMES is unchanged
HERO_AT = {t['id']: tuple(t['hero']) for t in _CATALOG['tracks'] if 'hero' in t}
THEMES = [dict({k: v for k, v in t.items() if k != 'hero'}, **({'planned': _rows(t['planned'])} if 'planned' in t else {})) for t in _CATALOG['tracks']]
NEXT = _rows(_CATALOG.get('next', []))

# courses/_template/ and any other folder starting with '_' is not a course
_found = {p.parent.name: p for p in sorted((_ROOT / 'courses').glob('*/course.toml')) if not p.parent.name.startswith('_')}
COURSES = [_course(_found[n], _load(_found[n])) for n in _ordered(_found, _CATALOG.get('course_order', []), 'course_order')]
_ids = [c['id'] for c in COURSES]
if len(set(_ids)) != len(_ids):
    _fail(_ROOT / 'courses', f'course ids repeat: {sorted({i for i in _ids if _ids.count(i) > 1})}')
for _c in COURSES:
    globals()[_c['id'].upper().replace('-', '_')] = _c

BRANDS = {p.stem: _brand(p, _load(p)) for p in sorted((_ROOT / 'brands').glob('*.toml'))}

_found = {p.stem: p for p in (_ROOT / 'editions').glob('*.toml')}
EDITIONS = {n: _edition(_found[n], _load(_found[n])) for n in _ordered(_found, _CATALOG.get('edition_order', []), 'edition_order')}
DEFAULT_EDITION = next(iter(EDITIONS))


def brand(edition):
    """The brand dict an edition is built with (S-DEC3)."""
    return BRANDS[EDITIONS[edition]['brand']]

HISTORY = [c for c in COURSES if c['family'] == 'history']
MARKDOWN = [c for c in COURSES if c['family'] == 'markdown']


# S-DEC5 (20 Nov 2026): a history course's inputs live in its folder, named by its course.toml (paths from the repo
# root): `syllabus` and `prompts` (courses/<id>/inputs/), `provenance` (its own part of what kit/provenance.json held),
# `bibliography` (the curated r-<id>.md and biblio.py's unit-<n>.md). kit/provenance.json keeps the kit's own part.
def path(c, key):
    """The file or folder a course names by `key` (a path from the repo root): an absolute Path."""
    return _ROOT / c[key]


_KIT_PROV = _ROOT / 'kit' / 'provenance.json'


def provenance():
    """The provenance dict as kit/provenance.json held it before S-DEC5: {<course id>: {module: model}, 'artefacts',
    'review_notes', 'review_mark', 'written': {<course id>: {module: date}}, 'written_approx': {<course id>: [modules]}}.
    Built from kit/provenance.json (the kit's artefacts, review_notes, review_mark) and each history course's
    `provenance` file ({'reports', 'artefacts', 'written', 'written_approx'}); a course's artefacts follow the kit's."""
    kit = json.loads(_KIT_PROV.read_text(encoding='utf-8'))
    out = {c['id']: {} for c in HISTORY}
    out['artefacts'] = dict(kit.get('artefacts', {}))
    for k, v in kit.items():
        if k != 'artefacts':
            out[k] = v
    out['written'], out['written_approx'] = {}, {}
    for c in HISTORY:
        own = json.loads(path(c, 'provenance').read_text(encoding='utf-8'))
        out[c['id']] = own.get('reports', {})
        out['artefacts'].update(own.get('artefacts', {}))
        out['written'][c['id']] = own.get('written', {})
        out['written_approx'][c['id']] = own.get('written_approx', [])
    return out


def save_provenance(prov):
    """Write a dict of provenance()'s shape back: each course's part to its own file (an artefact goes to the course
    file that already holds it, a new one to kit/provenance.json), the rest to kit/provenance.json."""
    def dump(p, d):
        p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    ids = {c['id'] for c in HISTORY}
    taken = set()
    for c in HISTORY:
        f = path(c, 'provenance')
        mine = list(json.loads(f.read_text(encoding='utf-8')).get('artefacts', {})) if f.exists() else []
        taken |= set(mine)
        dump(f, {'reports': prov.get(c['id'], {}),
                 'artefacts': {k: prov['artefacts'][k] for k in mine if k in prov.get('artefacts', {})},
                 'written': prov.get('written', {}).get(c['id'], {}),
                 'written_approx': prov.get('written_approx', {}).get(c['id'], [])})
    kit = {}
    for k, v in prov.items():
        if k in ids or k in ('written', 'written_approx'):
            continue
        kit[k] = {a: x for a, x in v.items() if a not in taken} if k == 'artefacts' else v
    dump(_KIT_PROV, kit)
