"""Verify by scope (S-DEC4, 20 Nov 2026): which pages verify.py checks, and the record of the last passed run.

verify.py keeps, per edition, a hash of every page's sources in kit/verify-hashes.json and in its default (scoped) run
checks only the pages whose sources changed since the last run that ended ALL CHECKS PASSED, plus the pages that always
run (the home, What's new, the Changelog and the Backlog) and the edition-wide checks (files and the shell, figure keys,
opening notes, figure rules, the split, navigation, the home at every width, contrast of the home, private terms, the
rot check, index_check).

A page's sources (page_hash):
  - what the build made of it: its section in the shell (index.html, the panel and everything in it) and the file it
    fetches (data-src), so a change in any source the build reads for it (course.toml, briefs.md, pages/*.md, the vault,
    docs it renders) that reaches the page is seen, and one that does not reach it is not;
  - the source files the checks hold it against: a unit or report page its own unit file in courses/<id>/ (front matter
    and body; a history report its module's file) and, for a markdown unit, its entry in briefs.md; every other page of
    a course (its home, briefs, build order, changelog, bibliography, syllabus, How it was built) every file under
    courses/<id>/ (course.toml, briefs.md, pages/, notes/, inputs/, bibliography/ and the units, whose words its tiles
    and tables count). A unit page with no unit file of its own (read-audience-growth, from brand-ai's notes/) counts
    as a course page.
A page of no course (the home, What's new, Changelog, Backlog, Figure kinds, an area page) has only the first.
S-NAV1 step B (21 Nov 2026): an area page (data-kind="area", track-<id>, in an edition of two or more tracks) runs in
every run, as the home does: it shows its track's course tiles, which every filing in the track changes.
S-NAV1 step C (21 Nov 2026): the navigation, nav.main-nav and nav.sub-nav, sits in the shell's drawer outside every
panel, so it reaches no page's hash; its checks (verify.py check_nav, the drawer boxes on the home, every area page and
each changed page's course) are edition-wide and run in every run. A page's context (data-ctx) names its section's group
of the sub-nav: a course's id, or "root" for the home, its site pages and the area pages (whose group is their own id).

What every page depends on (GLOBAL) forces the full run when it changed: kit/*.py, kit/shell.js, kit/shell.css,
design/theme.css, kit/fonts/, catalog.toml, the edition's editions/<name>.toml and its brand's brands/<name>.toml.
A first run with no record for the edition is a full run; `--full` always is. The record is written only after ALL
CHECKS PASSED, so a failed run never marks a page as checked. kit/verify-hashes.json is committed with the site: a
chat clones the repo, so a record left out of git would make every chat's first run a full one. A record that is
missing, unreadable or of the wrong shape for the edition gives a full run, and the first line says which.
Tool versions (Python markdown, Playwright, Chromium) are not hashed: run `--full` after a tool upgrade.
"""
import hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE = ROOT / 'kit' / 'verify-hashes.json'
ALWAYS = ('home', 'new', 'changelog', 'backlog')   # the site pages every run checks
PANEL = re.compile(r'<section class="panel[^"]*" id="([^"]+)"([^>]*)>')
SEC = re.compile(r'<(/?)section\b')


def _sha(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(p if isinstance(p, bytes) else str(p).encode())
        h.update(b'\0')
    return h.hexdigest()


def global_files(edition, brand_name):
    """The files every page depends on, repo-relative, sorted."""
    fs = [p for p in (ROOT / 'kit').glob('*.py')]
    fs += [ROOT / 'kit' / 'shell.js', ROOT / 'kit' / 'shell.css', ROOT / 'design' / 'theme.css', ROOT / 'catalog.toml',
           ROOT / 'editions' / f'{edition}.toml', ROOT / 'brands' / f'{brand_name}.toml']
    fs += [p for p in (ROOT / 'kit' / 'fonts').rglob('*') if p.is_file()]
    return sorted(str(p.relative_to(ROOT)) for p in fs if p.is_file())


def panels(shell):
    """{panel id: (its attributes, its section in the shell, balanced)}"""
    out = {}
    for m in PANEL.finditer(shell):
        depth, i = 0, m.start()
        for t in SEC.finditer(shell, m.start()):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                i = shell.find('>', t.end()) + 1
                break
        out[m.group(1)] = (m.group(2), shell[m.start():i])
    return out


def _front(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    return m.group(1) if m else ''


def unit_files(course):
    """{page id: [unit files]} of a course: a markdown unit read-<code>, a history report <prefix><module>."""
    out = {}
    for f in sorted((ROOT / course['vault']).glob('*.md')):
        m = re.search(r'^code:\s*"?([^"\s]+)', _front(f.read_text()), re.M)
        if not m: continue
        code = m.group(1)
        pid = course['prefix'] + code.replace('.', '') if course['family'] == 'history' else 'read-' + code.lower()
        out.setdefault(pid, []).append(f)
    return out


def brief_entry(course, code):
    f = ROOT / 'courses' / course['id'] / 'briefs.md'
    if not f.exists(): return ''
    m = re.search(rf'^## {re.escape(code)}\n(.*?)(?=^## |\Z)', f.read_text(), re.S | re.M)
    return m.group(1) if m else ''


class Scope:
    """The run's mode and its pages. pages is None in a full run, else the set of page ids to check."""

    def __init__(self, site, edition, brand_name, courses, sub_pages, full=False, state=STATE):
        self.site, self.edition, self.state_path = site, edition, state
        self.globals = {f: _sha((ROOT / f).read_bytes()) for f in global_files(edition, brand_name)}
        shell = (site / 'index.html').read_text() if (site / 'index.html').exists() else ''
        self.pages_now = {}
        ctx_course = {p: c for c in courses for p in sub_pages(c)}
        units = {c['id']: unit_files(c) for c in courses}
        course_all = {c['id']: _sha(*[x for p in sorted((ROOT / 'courses' / c['id']).rglob('*')) if p.is_file()
                                      for x in (str(p.relative_to(ROOT)), p.read_bytes())]) for c in courses}
        self.kind, self.ctx = {}, {}   # page id: unit, course or site; page id: its context (data-ctx), its sub-nav group's id unless root
        self.areas = []   # S-NAV1 step B: the area pages, checked in every run as the home is
        for pid, (attrs, frag) in panels(shell).items():
            parts = [frag]
            src = re.search(r' data-src="([^"]+)"', attrs)
            if src and (site / src.group(1)).exists(): parts.append((site / src.group(1)).read_bytes())
            kind = re.search(r' data-kind="([^"]+)"', attrs); kind = kind.group(1) if kind else ''
            if kind == 'area': self.areas.append(pid)
            ctx = re.search(r' data-ctx="([^"]+)"', attrs); c = ctx_course.get(ctx.group(1)) if ctx else None
            self.ctx[pid] = ctx.group(1) if ctx else 'root'
            self.kind[pid] = 'unit' if kind == 'report' else ('course' if c else 'site')
            if c and kind == 'report':
                fs = units[c['id']].get(pid, [])
                if not fs: parts += ['course ' + c['id'], course_all[c['id']]]   # a unit page with no unit file of its own (brand-ai's notes page)
                for f in fs:
                    parts += [str(f.relative_to(ROOT)), f.read_bytes()]
                    if c['family'] == 'markdown':
                        code = re.search(r'^code:\s*"?([^"\s]+)', _front(f.read_text()), re.M).group(1)
                        parts += ['brief ' + code, brief_entry(c, code)]
            elif c:
                parts += ['course ' + c['id'], course_all[c['id']]]
            self.pages_now[pid] = _sha(*parts)
        self.unreadable = False
        st = self._load()
        rec = st.get(edition)
        bad = rec is not None and not (isinstance(rec, dict) and isinstance(rec.get('global'), dict) and isinstance(rec.get('pages'), dict))
        if bad: rec = None
        self.changed = []
        if full:
            self.pages, self.mode = None, 'full: --full'
        elif not shell:
            self.pages, self.mode = None, f'full: {site.name}/index.html missing'
        elif self.unreadable or bad:
            self.pages, self.mode = None, f'full: {state.name} unreadable or malformed for edition {edition}'
        elif not rec:
            self.pages, self.mode = None, f'full: no passed run recorded for edition {edition} ({state.name})'
        else:
            gch = sorted(f for f in set(self.globals) | set(rec.get('global', {})) if self.globals.get(f) != rec['global'].get(f))
            if gch:
                self.pages = None
                self.mode = 'full: ' + ', '.join(gch[:4]) + (f' and {len(gch) - 4} more' if len(gch) > 4 else '') + ' changed'
            else:
                old = rec.get('pages', {})
                self.changed = [p for p in self.pages_now if old.get(p) != self.pages_now[p]]
                self.pages = set(self.changed) | {p for p in ALWAYS if p in self.pages_now} | set(self.areas)
                n_u = [p for p in self.changed if self.kind[p] == 'unit']
                n_c = [p for p in self.changed if self.kind[p] == 'course']
                n_s = [p for p in self.changed if self.kind[p] == 'site' and p not in ALWAYS and p not in self.areas]
                what = []
                if n_u: what.append(f'{len(n_u)} unit' + ('s' if len(n_u) != 1 else '') + f' ({", ".join(n_u)})')
                if n_c: what.append(f'{len(n_c)} course page' + ('s' if len(n_c) != 1 else '') + f' ({", ".join(n_c)})')
                if n_s: what.append(f'{len(n_s)} site page' + ('s' if len(n_s) != 1 else '') + f' ({", ".join(n_s)})')
                self.mode = ('scoped: ' + (', '.join(what) if what else 'no page changed') + ' + home'
                             + f'; {len(self.pages)} of {len(self.pages_now)} pages checked'
                             + f' ({", ".join([p for p in ALWAYS if p in self.pages_now] + self.areas)} always), and the edition-wide checks')

    def _load(self):
        try:
            st = json.loads(self.state_path.read_text())
        except FileNotFoundError:
            return {}
        except (ValueError, UnicodeDecodeError):
            self.unreadable = True
            return {}
        if not isinstance(st, dict):
            self.unreadable = True
            return {}
        return st

    @property
    def full(self):
        return self.pages is None

    def has(self, pid):
        """Is this page checked in this run?"""
        return self.pages is None or pid in self.pages

    def only(self, ids):
        return [i for i in ids if self.has(i)]

    def save(self):
        """After ALL CHECKS PASSED only: record every page's sources as checked (an unchanged page's hash is the one the
        record already held)."""
        st = self._load()
        st[self.edition] = {'global': dict(sorted(self.globals.items())), 'pages': dict(sorted(self.pages_now.items()))}
        tmp = self.state_path.with_suffix('.tmp')
        tmp.write_text(json.dumps(dict(sorted(st.items())), indent=1) + '\n')
        tmp.replace(self.state_path)
