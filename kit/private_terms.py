"""Fail if a private term reaches a public course (G-0, 11 Nov 2026; docs/public-courses.md; extends backlog row P29).

python3 kit/private_terms.py            every public course: its vault, its pack and its built pages (but built.html),
                                        and docs/site-log.md, the source of the Backlog and Changelog pages (S-PAGES)
python3 kit/private_terms.py <file>...  only these files (a writer's or a checker's draft, or a built edition's pages:
                                        `python3 kit/private_terms.py $(find kit/editions/<site> -type f)`)
python3 kit/private_terms.py --edition <name>   every file of that edition's built site (kit/<site>/, built.html
                                        included), whatever courses it holds (S-DEC4); edition_files(name) for verify.py,
                                        which leaves a mixed edition's private courses' folders out (P-DEC13), and
                                        their panels and drawer sections in the shell (P-DEC24, private_text); a
                                        `dated_lists` course's pages are checked as in academy's run (P-DEC10)

The no-argument run is academy's: PUBLIC (below) gives its public courses and the kit/academy glob its site. An
edition's own output is checked with --edition or explicit files. A given file that is not UTF-8 text is skipped and
named (S-DEC4); the no-argument run reads only text.

The public courses (PUBLIC) are every course whose courses/<id>/course.toml does not set `private = true` (S-DEC4). The terms are kit/private-terms.txt: one per line,
whole word, case-insensitive; "warn:" lines are printed and do not fail. Prints OK and exits 0 when nothing fails.
verify.py runs check() and fails the build on any hit.

S-SCE0 (19 Nov 2026; docs/supply-chain-execution-syllabus.md §6, proposal P-SCE2): a course with `dated_lists=True` in
its course.toml (supply-chain-execution) may name the owner's employer as one entry of a dated list taken from an analyst
report or a filing, and nowhere else. The employer's terms are the "employer:" lines of private-terms.txt (its name and its
product names). On that course's files (its vault, its pack, its built pages; or any file given with --course <id>)
an employer term fails anywhere but inside a dated list: a Markdown list or table (lines starting "- ", "* ", "1. " or "|"),
or a built page's <ul>, <ol> or table, whose lead-in line (the last line before it that is not part of it) names an analyst
firm or a filing (DATED_BY) and a year. Every other course is checked exactly as before: an employer term that is also a
plain line of the file fails there anywhere, and one that is only an "employer:" line is not checked there.
"""
import pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
sys.path.insert(0, str(R))
from courses import COURSES as _ALL
PUBLIC = tuple(c['id'] for c in _ALL if not c.get('private'))   # S-DEC4 (checker M2): every course without `private = true` in its course.toml
# S-SCE0: what a dated list's lead-in line must name (one of these, case-insensitive) besides a year
DATED_BY = ('Gartner', 'Forrester', 'IDC', 'Nucleus Research', 'MarketScape', 'Magic Quadrant', 'Value Matrix', 'analyst', 'filing', 'annual report', '10-K')


def terms():
    fail, warn = [], []
    for ln in (R / 'private-terms.txt').read_text(encoding='utf-8').splitlines():
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        if ln.startswith('employer:'):                       # S-SCE0: read by employer() only
            continue
        (warn if ln.startswith('warn:') else fail).append(ln[5:].strip() if ln.startswith('warn:') else ln)
    return fail, warn


def employer():
    """S-SCE0: the "employer:" lines of private-terms.txt, the terms a dated-list course may name only inside a dated list."""
    return [ln.strip()[9:].strip() for ln in (R / 'private-terms.txt').read_text(encoding='utf-8').splitlines()
            if ln.strip().startswith('employer:')]


_MD_ITEM = re.compile(r'^\s*(?:[-*+]\s|\d+[.)]\s|\|)')
_HTML_ITEM = re.compile(r'^\s*(?:<(?:ul|ol|li|table|thead|tbody|tr|th|td)\b|</(?:ul|ol|li|table|thead|tbody|tr|th|td)>|<div class="tbl">|</div>\s*$)')


def dated_lines(lines):
    """S-SCE0: the numbers (from 1) of the lines inside a dated list: a run of list or table lines (Markdown or built HTML)
    whose lead-in line names one of DATED_BY and a year from 1900 to 2099."""
    by = re.compile('|'.join(re.escape(x) for x in DATED_BY), re.I)
    yr = re.compile(r'\b(?:19|20)\d\d\b')
    out, lead, run_ok, in_run = set(), '', False, False
    for n, ln in enumerate(lines, 1):
        item = bool(_MD_ITEM.match(ln) or _HTML_ITEM.match(ln))
        if item:
            if not in_run:
                run_ok = bool(by.search(lead) and yr.search(lead))
                in_run = True
            if run_ok:
                out.add(n)
        elif ln.strip():
            lead, in_run = ln, False
        else:
            in_run = in_run and bool(_MD_ITEM.match(lines[n]) if n < len(lines) else False)   # a blank line inside a Markdown list
    return out


def rx(ts):
    return re.compile(r'(?<![\w@.-])(?:' + '|'.join(re.escape(t) for t in sorted(ts, key=len, reverse=True)) + r')(?![\w-])', re.I)


DATED = set()   # S-SCE0: the files of the courses with dated_lists=True, filled by files() and (P-DEC10) edition_files()
# P-DEC24 (27 Nov 2026): a mixed edition's shell files (the pages at the site's root: index.html and any other) and the
# private courses' page contexts and page ids to strip from them before the scan (edition_files fills it; scan() reads it)
STRIP = {}


def files():
    sys.path.insert(0, str(R))
    from courses import COURSES
    import pack
    out = []
    for c in COURSES:
        if c['id'] not in PUBLIC:
            continue
        mine = sorted((ROOT / c['vault']).glob('*.md'))
        mine += pack.files(c)              # S-DEC2: its data files (course.toml, briefs.md, pages/, notes/)
        mine = list(dict.fromkeys(mine))   # briefs.md is in the vault folder and in the pack: read once
        # built.html is left out: the "How it was built" page is generated from docs/method.md and links the private
        # repository by its owner's handle on every course; what it shows publicly is row P24's decision
        mine += sorted(f for f in (R / 'academy').glob(f'{c["id"]}-*/*.html') if f.name != 'built.html')
        if c.get('dated_lists'):
            DATED.update(mine)
        out += mine
    # S-PAGES (15 Nov 2026): the site log, the one source of Academy's Backlog and Changelog pages; verify.py's
    # check_site_log scans the two built pages for the same terms
    out += [ROOT / 'docs' / 'site-log.md']
    return out


def folders(c):
    """P-DEC10, P-DEC13: the top-level folders of a built site that hold a course's split pages (build.py split(): a
    page goes to <data-ctx>/): a markdown course's one per sub-course, <prefix or id>-<key> (build.py md_courses:
    brand-a, supply-chain-execution-sce), a history course's <id> (greece)."""
    if c['family'] == 'history':
        return [c['id']]   # a history course's split pages sit in <id>/, its home page id is home_id
    from courses import sub_pages
    return sub_pages(c)


def edition_files(name, skip=()):
    """S-DEC4: every file of an edition's built site, sorted (kit/<site>/, from editions/<name>.toml `site`).
    P-DEC10: the pages of an edition's course with `dated_lists` (its folders, folders()) go into DATED, as files()
    puts academy's, so scan() checks them as academy's run does. P-DEC13: `skip`, course ids whose folders are left out
    (verify.py passes the edition's `private` courses on a mixed edition); every other file, the shell included, stays."""
    sys.path.insert(0, str(R))
    from courses import EDITIONS, COURSES
    if name not in EDITIONS:
        raise SystemExit(f'--edition {name}: no editions/{name}.toml (editions: {", ".join(EDITIONS)})')
    site = R / EDITIONS[name]['site']
    if not site.is_dir():
        raise SystemExit(f'--edition {name}: {site.relative_to(ROOT)} not built (python3 kit/build.py --edition {name})')
    held = [c for c in COURSES if EDITIONS[name]['courses'] is None or c['id'] in EDITIONS[name]['courses']]
    out = sorted(f for f in site.rglob('*') if f.is_file())
    top = lambda f: f.relative_to(site).parts[0] if len(f.relative_to(site).parts) > 1 else None   # a file at the root is in no course's folder
    gone = {d for c in held if c['id'] in skip for d in folders(c)}
    out = [f for f in out if top(f) not in gone]
    if gone:   # P-DEC24: a private course's own text inside the shell is left out as its folders are (private_text)
        import verify_scope
        shell = site / 'index.html'
        pids = frozenset(pid for pid, (attrs, _) in verify_scope.panels(shell.read_text(encoding='utf-8')).items()
                         if (m := re.search(r'\bdata-ctx="([^"]*)"', attrs)) and m.group(1) in gone) if shell.is_file() else frozenset()
        STRIP.update({f: (frozenset(gone), pids) for f in out if top(f) is None and f.suffix == '.html'})
    dated = {d for c in held if c.get('dated_lists') for d in folders(c)}
    DATED.update(f for f in out if top(f) in dated)
    return out


_DIV = re.compile(r'<(/?)div\b')


def private_text(text, ctxs, pids=frozenset()):
    """P-DEC24: a shell page's text less what is a private course's own, as its folders are left out (P-DEC13):
    every panel whose data-ctx is one of `ctxs` (verify_scope.panels(), the balanced-section walk: the unsplit pages of
    that course and the stubs of its split ones), its drawer section (div.sub-sec with that data-navctx, a balanced div
    walk), and every link to one of its pages (`pids`: an <a> whose data-target is one, as the root drawer's and the
    area drawer's entries for it, its tiles on the home and its area page, and its What's new rows are; links do not
    nest, so each is cut from its tag to its </a>). What each of these may name is the course's own: its name, tile
    sentence, unit codes, titles and dates, as its course.toml and its units give them, private terms included, since
    an edition that holds a private course publishes them on that course's pages anyway. What stays scanned, and so may
    name no private term, is the shell's own text (the brand's copy, the site pages, the area and home text around the
    tiles) and every public course's. Each part cut is replaced by its newlines, so a hit elsewhere keeps its line
    number."""
    import verify_scope
    cut = []
    for m in re.finditer(r'<a\b[^>]*\bdata-target="([^"]*)"[^>]*>', text):
        if m.group(1) in pids:
            j = text.find('</a>', m.end())
            cut.append((m.start(), j + 4 if j >= 0 else m.end()))
    for pid, (attrs, frag) in verify_scope.panels(text).items():
        m = re.search(r'\bdata-ctx="([^"]*)"', attrs)
        if m and m.group(1) in ctxs:
            i = text.find(frag)
            cut.append((i, i + len(frag)))
    for m in re.finditer(r'<div\b[^>]*\bclass="sub-sec"[^>]*\bdata-navctx="([^"]*)"', text):
        if m.group(1) not in ctxs:
            continue
        depth = 0
        for t in _DIV.finditer(text, m.start()):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                cut.append((m.start(), text.find('>', t.end()) + 1))
                break
    spans = []
    for a, b in sorted(cut):   # a part inside another is cut once, with it
        if spans and a < spans[-1][1]:
            spans[-1][1] = max(spans[-1][1], b)
        else:
            spans.append([a, b])
    for a, b in reversed(spans):
        text = text[:a] + '\n' * text.count('\n', a, b) + text[b:]
    return text


def text_only(fs):
    """S-DEC4: the given files that read as UTF-8 text; each other one is named and skipped."""
    out = []
    for f in fs:
        try:
            pathlib.Path(f).read_text(encoding='utf-8')
        except UnicodeDecodeError:
            print(f'skip {f}: not UTF-8 text')
            continue
        out.append(f)
    return out


def scan(fs):
    fail, warn = terms()
    F, W = rx(fail), rx(warn)
    emp = employer()
    E = rx(emp) if emp else None
    low = {x.lower() for x in emp}
    hits, warns = [], []
    for f in fs:
        text = pathlib.Path(f).read_text(encoding='utf-8')
        if pathlib.Path(f) in STRIP:   # P-DEC24: a mixed edition's shell, less its private courses' own text
            text = private_text(text, *STRIP[pathlib.Path(f)])
        lines = text.splitlines()
        dated = pathlib.Path(f) in DATED and E is not None          # S-SCE0: the employer only in a dated list
        ok = dated_lines(lines) if dated else set()
        for n, ln in enumerate(lines, 1):
            for m in F.finditer(ln):
                if dated and m.group(0).lower() in low and n in ok:
                    continue
                hits.append(f'{f}:{n}: {m.group(0)}')
            if dated:
                for m in E.finditer(ln):
                    if n not in ok and not F.fullmatch(m.group(0)):   # a term on both kinds of line is reported once, above
                        hits.append(f'{f}:{n}: {m.group(0)}')
            for m in W.finditer(ln):
                warns.append(f'{f}:{n}: {m.group(0)}')
    return hits, warns


def check():
    """For verify.py: the failing hits across every public course."""
    return scan(files())[0]


if __name__ == '__main__':
    args = sys.argv[1:]
    if '--course' in args:                                   # S-SCE0: a draft checked as one course's page
        i = args.index('--course')
        cid = args[i + 1]
        del args[i:i + 2]
        sys.path.insert(0, str(R))
        from courses import COURSES
        if not next((c for c in COURSES if c['id'] == cid), {}).get('dated_lists'):
            print(f'--course {cid}: not a course with dated_lists; the files are checked as before')
        else:
            DATED.update(pathlib.Path(a) for a in args)
    if '--edition' in args:                                  # S-DEC4: an edition's own built pages
        i = args.index('--edition')
        if i + 1 >= len(args):
            raise SystemExit('usage: python3 kit/private_terms.py --edition <name>')
        args[i:i + 2] = [str(f) for f in edition_files(args[i + 1])]
    fs = text_only([pathlib.Path(a) for a in args]) if args else files()
    hits, warns = scan(fs)
    for w in warns:
        print('warn', w)
    for h in hits:
        print('FAIL', h)
    print(f'{len(fs)} files, {len(hits)} private terms, {len(warns)} warnings' + ('' if hits else ': OK'))
    sys.exit(1 if hits else 0)
