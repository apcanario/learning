"""Fail if a private term reaches a public course (G-0, 11 Nov 2026; docs/public-courses.md; extends backlog row P29).

python3 kit/private_terms.py            every public course: its vault, its data folder and its built pages (but built.html),
                                        and docs/site-log.md, the source of the Backlog and Changelog pages (S-PAGES)
python3 kit/private_terms.py <file>...  only these files (a writer's or a checker's draft)

The public courses are the entries of kit/courses.py named in PUBLIC. The terms are kit/private-terms.txt: one per line,
whole word, case-insensitive; "warn:" lines are printed and do not fail. Prints OK and exits 0 when nothing fails.
verify.py runs check() and fails the build on any hit.
"""
import pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
PUBLIC = ('personal-brand', 'building-with-ai', 'sport-psychology')


def terms():
    fail, warn = [], []
    for ln in (R / 'private-terms.txt').read_text(encoding='utf-8').splitlines():
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        (warn if ln.startswith('warn:') else fail).append(ln[5:].strip() if ln.startswith('warn:') else ln)
    return fail, warn


def rx(ts):
    return re.compile(r'(?<![\w@.-])(?:' + '|'.join(re.escape(t) for t in sorted(ts, key=len, reverse=True)) + r')(?![\w-])', re.I)


def files():
    sys.path.insert(0, str(R))
    from courses import COURSES
    out = []
    for c in COURSES:
        if c['id'] not in PUBLIC:
            continue
        out += sorted((ROOT / c['vault']).glob('*.md'))
        out += sorted(f for f in (ROOT / c['data']).parent.iterdir() if f.suffix in ('.py', '.md'))
        # built.html is left out: the "How it was built" page is generated from docs/method.md and links the private
        # repository by its owner's handle on every course; what it shows publicly is row P24's decision
        out += sorted(f for f in (R / 'academy').glob(f'{c["id"]}-*/*.html') if f.name != 'built.html')
    # S-PAGES (15 Nov 2026): the site log, the one source of Academy's Backlog and Changelog pages; verify.py's
    # check_site_log scans the two built pages for the same terms
    out += [ROOT / 'docs' / 'site-log.md']
    return out


def scan(fs):
    fail, warn = terms()
    F, W = rx(fail), rx(warn)
    hits, warns = [], []
    for f in fs:
        for n, ln in enumerate(pathlib.Path(f).read_text(encoding='utf-8').splitlines(), 1):
            for m in F.finditer(ln):
                hits.append(f'{f}:{n}: {m.group(0)}')
            for m in W.finditer(ln):
                warns.append(f'{f}:{n}: {m.group(0)}')
    return hits, warns


def check():
    """For verify.py: the failing hits across every public course."""
    return scan(files())[0]


if __name__ == '__main__':
    fs = [pathlib.Path(a) for a in sys.argv[1:]] or files()
    hits, warns = scan(fs)
    for w in warns:
        print('warn', w)
    for h in hits:
        print('FAIL', h)
    print(f'{len(fs)} files, {len(hits)} private terms, {len(warns)} warnings' + ('' if hits else ': OK'))
    sys.exit(1 if hits else 0)
