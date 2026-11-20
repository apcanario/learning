"""Fail if a private term reaches a public course (G-0, 11 Nov 2026; docs/public-courses.md; extends backlog row P29).

python3 kit/private_terms.py            every public course: its vault, its data folder and its built pages (but built.html),
                                        and docs/site-log.md, the source of the Backlog and Changelog pages (S-PAGES)
python3 kit/private_terms.py <file>...  only these files (a writer's or a checker's draft)

The public courses are the courses (courses/<id>/course.toml) named in PUBLIC. The terms are kit/private-terms.txt: one per line,
whole word, case-insensitive; "warn:" lines are printed and do not fail. Prints OK and exits 0 when nothing fails.
verify.py runs check() and fails the build on any hit.

S-SCE0 (19 Nov 2026; docs/supply-chain-execution-syllabus.md §6, proposal P-SCE2): a course with `dated_lists=True` in
its course.toml (supply-chain-execution) may name the owner's employer as one entry of a dated list taken from an analyst
report or a filing, and nowhere else. The employer's terms are the "employer:" lines of private-terms.txt (its name and its
product names). On that course's files (its vault, its data folder, its built pages; or any file given with --course <id>)
an employer term fails anywhere but inside a dated list: a Markdown list or table (lines starting "- ", "* ", "1. " or "|"),
or a built page's <ul>, <ol> or table, whose lead-in line (the last line before it that is not part of it) names an analyst
firm or a filing (DATED_BY) and a year. Every other course is checked exactly as before: an employer term that is also a
plain line of the file fails there anywhere, and one that is only an "employer:" line is not checked there.
"""
import pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
PUBLIC = ('personal-brand', 'building-with-ai', 'sport-psychology', 'supply-chain-execution')
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


DATED = set()   # S-SCE0: the files of the courses with dated_lists=True, filled by files()


def files():
    sys.path.insert(0, str(R))
    from courses import COURSES
    import pack
    out = []
    for c in COURSES:
        if c['id'] not in PUBLIC:
            continue
        mine = sorted((ROOT / c['vault']).glob('*.md'))
        mine += pack.files(c)              # S-DEC2: its data files (the pack's, or the old data folder's .py and .md)
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


def scan(fs):
    fail, warn = terms()
    F, W = rx(fail), rx(warn)
    emp = employer()
    E = rx(emp) if emp else None
    low = {x.lower() for x in emp}
    hits, warns = [], []
    for f in fs:
        lines = pathlib.Path(f).read_text(encoding='utf-8').splitlines()
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
    fs = [pathlib.Path(a) for a in args] or files()
    hits, warns = scan(fs)
    for w in warns:
        print('warn', w)
    for h in hits:
        print('FAIL', h)
    print(f'{len(fs)} files, {len(hits)} private terms, {len(warns)} warnings' + ('' if hits else ': OK'))
    sys.exit(1 if hits else 0)
