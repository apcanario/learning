"""S-NAV1 step E (22 Nov 2026) · the row's test: every difference between two builds sorted into its class, and every
reading page's text unchanged once its navigation and its line drawings are stripped.

  python3 kit/nav_diff_check.py START NOW [--edition E ...]
        START and NOW are two repo roots (a clone or a git worktree), each already built (kit/baseline.py's build of
        each edition compared); compares the files each edition's build writes
  python3 kit/nav_diff_check.py --build COMMIT [--now REV] [--edition E ...] [--keep]
        makes two temporary git worktrees under /tmp (COMMIT, and REV, default HEAD), builds every edition compared in
        each with that tree's own kit/baseline.py build(), compares them, then removes the worktrees (--keep leaves them)

Editions compared: academy, greece and marketing-ai (EDITIONS below), or those given with --edition. Exit 0 when every
difference is classified and every reading page is identical; 1 otherwise, each failure printed with its file and context.

What is compared, per edition (as kit/baseline.py outputs(): the files each build writes): the site folder
(courses.py EDITIONS[e]['site']); for academy also kit/README.md, kit/bibliography/ and each history course's
bibliography folder. A file added or removed is a failure; a non-HTML file that differs is a failure, except kit/README.md
when every changed line is a row of the build's size table (class "size table", see below).

The classification is structural, not a pattern over the text. Each HTML file is tokenised by html.parser (start tag,
end tag, text, character reference, comment, declaration), each token kept as its exact source slice, so the tokens
put back together are the file byte for byte. While tokenising, a stack of open elements gives every token its
outermost "region": the first ancestor (or the element itself) that matches one of these rules, in this order:

  shell JS      the <script> in the shell (index.html) that holds the inlined kit/shell.js (the longer script; the
                small theme-preload <script> is not a region, so any change to it fails)
  theme CSS     the <style> in the shell's head (design/theme.css = kit/shell.css, inlined)
  nav markup    aside#drawer (the drawer: its head and the old nav.dlist lists, or div.dlist with nav.main-nav and
                nav.sub-nav), any nav.main-nav or nav.sub-nav outside it, and every nav.crumbs
  the home      section#home (its hero, tiles, rules, links: the whole home panel)
  area pages    section#track-<id> that is a panel (class "panel"): the new area pages
  SVG lines     a line illustration: an element whose class has a token topo or topo-* (heroes' layers, tile patches,
                separators), or a relief wrapper (class token relief or rel-*), or an <svg> whose class has topo-l;
                the region is the whole element: its start tag (style with --ph, --ar), its <svg>, paths, groups,
                --d, --o, transforms and classes. A guard: the text inside it (data tokens outside tags) must be
                identical, else the difference is not "line attributes" and fails.

Regions do not nest: inside the home, a tile's patch belongs to the home. Each region gets a key: panels their id,
navs their class (the drawer "drawer"), the scripts and styles their order, crumbs and line drawings their order
among the regions of their class in the file. The tokens outside every region, with each region replaced by one
placeholder token (class, key), form the file's residue. The two residues are aligned by difflib.SequenceMatcher on
the exact token slices: every unequal stretch must consist of placeholders only, and a placeholder only on one side
(a region added or removed) must be of a class that may come or go (nav markup, area pages); anything else is an
"other" difference and fails, printed with its file, the tokens and ten tokens of context. WHITESPACE rule: in an
unequal stretch holding a region that came or went (nav markup, area pages), text tokens that are whitespace only (the
line break the build writes between panels) go with it; whitespace in any other stretch fails. A region on both sides
whose place moved counts once for its class. A region present on
both sides is compared token by token; each unequal stretch counts once for its class. The counts are per edition:
files touched and stretches per class.

The reading-page test: every panel of the shell other than the home and the area pages (section.panel with an id),
and every fetched HTML file of the site (a report, unit, course home, syllabus, briefs, bibliography or How it was
built page; new.html, changelog.html and viz-examples.html included), is put back together from its tokens without
every <nav> element (crumbs, any nav) and every <svg> element, and without the style attribute of a line-illustration
wrapper's start tag (a relief's --ar and a drawing's --ph sit there, outside the <svg>); the result must be byte
identical between START and NOW. A panel or file present on one side only fails.

The size table: kit/README.md, written by build.py, holds a table of the site's file sizes between the markers it
writes; a README difference passes only if each changed line on both sides lies inside that table (README_TABLE).
"""
import argparse, difflib, os, pathlib, re, shutil, subprocess, sys, tempfile
from html.parser import HTMLParser

K = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(K))
from courses import EDITIONS as _ED, HISTORY, path as cpath

EDITIONS = ('academy', 'greece', 'marketing-ai')
CLASSES = ('shell JS', 'theme CSS', 'nav markup', 'the home', 'area pages', 'SVG lines', 'size table')
MAY_COME_OR_GO = {'nav markup', 'area pages'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
CONTEXT = 10


def outputs(edition):
    """The roots one edition's build writes, relative to the repo root (kit/baseline.py outputs())."""
    roots = ['kit/' + _ED[edition]['site']]
    if edition == 'academy':
        roots += ['kit/README.md', 'kit/bibliography'] + [os.path.relpath(cpath(c, 'bibliography'), K.parent) for c in HISTORY]
    return roots


def files(tree, edition):
    out = {}
    for r in outputs(edition):
        p = tree / r
        if p.is_file():
            out[r] = p
        elif p.is_dir():
            for f in sorted(p.rglob('*')):
                if f.is_file() and '__pycache__' not in f.parts:
                    out[f.relative_to(tree).as_posix()] = f
    return out


# ---- tokens --------------------------------------------------------------------------------------------------------

class Tok:
    __slots__ = ('kind', 'tag', 'attrs', 'raw', 'region', 'depth_tags')

    def __init__(s, kind, tag, attrs, raw):
        s.kind, s.tag, s.attrs, s.raw, s.region, s.depth_tags = kind, tag, attrs, raw, None, ()


class Tokeniser(HTMLParser):
    """Every construct of the file as a token holding its exact source slice (start offset to the next construct)."""

    def __init__(s, text):
        super().__init__(convert_charrefs=False)
        s.text, s.marks = text, []
        s.lines = [0]
        for m in re.finditer('\n', text):
            s.lines.append(m.end())
        s.feed(text)
        s.close()
        toks = []
        for k, (off, kind, tag, attrs) in enumerate(s.marks):
            end = s.marks[k + 1][0] if k + 1 < len(s.marks) else len(text)
            toks.append(Tok(kind, tag, attrs, text[off:end]))
        assert ''.join(t.raw for t in toks) == text, 'tokens do not rebuild the file'
        s.toks = toks

    def _mark(s, kind, tag=None, attrs=None):
        ln, col = s.getpos()
        off = s.lines[ln - 1] + col
        if s.marks and s.marks[-1][0] == off:   # a construct reported twice at one offset (never expected): keep the first
            return
        s.marks.append((off, kind, tag, dict(attrs or ())))

    def handle_starttag(s, t, a): s._mark('start', t, a)
    def handle_startendtag(s, t, a): s._mark('startend', t, a)
    def handle_endtag(s, t): s._mark('end', t)
    def handle_data(s, d): s._mark('data')
    def handle_entityref(s, n): s._mark('data')
    def handle_charref(s, n): s._mark('data')
    def handle_comment(s, d): s._mark('comment')
    def handle_decl(s, d): s._mark('decl')
    def handle_pi(s, d): s._mark('decl')
    def unknown_decl(s, d): s._mark('decl')


def classes_of(a):
    return (a.get('class') or '').split()


def is_line_drawing(tag, a):
    c = classes_of(a)
    return any(x == 'topo' or x.startswith('topo-') for x in c) and tag != 'path' and tag != 'g' \
        or any(x == 'relief' or x.startswith('rel-') for x in c) and tag not in ('path', 'g') \
        or tag == 'svg' and 'topo-l' in c


def region_rule(tag, a, shell, kind):
    """The class an element opens, or None. kind: 'script' when it is the shell's inlined shell.js."""
    c = classes_of(a)
    if shell and tag == 'script' and kind == 'shelljs':
        return 'shell JS'
    if shell and tag == 'style':
        return 'theme CSS'
    if tag == 'aside' and a.get('id') == 'drawer':
        return 'nav markup'
    if tag == 'nav' and ({'main-nav', 'sub-nav', 'crumbs'} & set(c)):
        return 'nav markup'
    if tag == 'section' and a.get('id') == 'home':
        return 'the home'
    if tag == 'section' and (a.get('id') or '').startswith('track-') and 'panel' in c:
        return 'area pages'
    if is_line_drawing(tag, a):
        return 'SVG lines'
    return None


def regions(text, shell):
    """Tokens with their outermost region set: (class, key) or None."""
    toks = Tokeniser(text).toks
    # the shell's inlined shell.js: the longest <script>
    script_k, best = None, -1
    for k, t in enumerate(toks):
        if t.kind == 'start' and t.tag == 'script' and k + 1 < len(toks) and toks[k + 1].kind == 'data' and len(toks[k + 1].raw) > best:
            script_k, best = k, len(toks[k + 1].raw)
    stack, cur, depth_at, ordinals = [], None, None, {}
    for k, t in enumerate(toks):
        if t.kind == 'start':
            if cur is None:
                cls = region_rule(t.tag, t.attrs, shell, 'shelljs' if k == script_k else None)
                if cls:
                    if cls in ('the home', 'area pages'):
                        key = t.attrs.get('id')
                    elif cls == 'nav markup' and t.tag == 'aside':
                        key = 'drawer'
                    elif cls == 'nav markup' and not ({'main-nav', 'sub-nav'} & set(classes_of(t.attrs))):
                        ordinals[cls + 'crumbs'] = ordinals.get(cls + 'crumbs', 0) + 1
                        key = 'crumbs-%d' % ordinals[cls + 'crumbs']
                    elif cls == 'nav markup':
                        key = [x for x in classes_of(t.attrs) if x in ('main-nav', 'sub-nav')][0]
                    else:
                        ordinals[cls] = ordinals.get(cls, 0) + 1
                        key = '%s-%d' % (t.tag, ordinals[cls])
                    cur, depth_at = (cls, key), len(stack)
            t.region = cur
            if t.tag not in VOID:
                stack.append(t.tag)
            continue
        t.region = cur
        if t.kind == 'end':
            # close up to the matching open element (html.parser does not repair; the build writes balanced markup)
            if t.tag in stack:
                while stack:
                    if stack.pop() == t.tag:
                        break
            if cur is not None and len(stack) <= depth_at:
                cur = None
    return toks


def residue(toks):
    out, regs = [], {}
    for t in toks:
        if t.region is None:
            out.append(t.raw)
        else:
            if t.region not in regs:
                regs[t.region] = []
                out.append(('REGION',) + t.region)
            regs[t.region].append(t)
    return out, regs


def show(seq, i, j):
    return ''.join(x if isinstance(x, str) else '[%s %s]' % (x[1], x[2]) for x in seq[max(0, i):j])


def text_of(ts):
    return [t.raw for t in ts if t.kind == 'data']


def classify_html(rel, a, b, counts, fails):
    shell = rel.endswith('/index.html') or rel == 'index.html'
    ra, ga = residue(regions(a, shell))
    rb, gb = residue(regions(b, shell))
    touched = set()
    sm = difflib.SequenceMatcher(None, ra, rb, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        side = ra[i1:i2] + rb[j1:j2]
        others = [x for x in side if isinstance(x, str)]
        # the line break the build writes between two panels belongs to the panel added or removed with it: whitespace
        # alone is let pass only beside a region that came or went in the same stretch (WHITESPACE rule, docstring)
        came = [x for x in side if not isinstance(x, str) and (x in ra) != (x in rb) and x[1] in MAY_COME_OR_GO]
        if others and came and all(not x.strip() for x in others):
            others = []
        if others:
            fails.append('%s: other difference (%s) outside every class:\n    start: ...%s>>>%s<<<%s...\n    now:   ...%s>>>%s<<<%s...' % (
                rel, op, show(ra, i1 - CONTEXT, i1)[-300:], show(ra, i1, i2)[:600], show(ra, i2, i2 + CONTEXT)[:300],
                show(rb, j1 - CONTEXT, j1)[-300:], show(rb, j1, j2)[:600], show(rb, j2, j2 + CONTEXT)[:300]))
            continue
        for x in side:
            if isinstance(x, str):
                continue
            if (x in ra) == (x in rb):   # a region on both sides, moved: its class
                counts[x[1]] = counts.get(x[1], 0) + 1
                touched.add(x[1])
            else:   # a region on one side only: added or removed
                if x[1] in MAY_COME_OR_GO:
                    counts[x[1]] = counts.get(x[1], 0) + 1
                    touched.add(x[1])
                else:
                    fails.append('%s: %s region %s %s' % (rel, x[1], x[2], 'removed' if x in ra else 'added'))
    for key in set(ga) & set(gb):
        ta, tb = [t.raw for t in ga[key]], [t.raw for t in gb[key]]
        if ta == tb:
            continue
        cls = key[0]
        if cls == 'SVG lines' and text_of(ga[key]) != text_of(gb[key]):
            fails.append('%s: line drawing %s changed its text: %r -> %r' % (rel, key[1], text_of(ga[key])[:5], text_of(gb[key])[:5]))
            continue
        n = sum(1 for op in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes() if op[0] != 'equal')
        counts[cls] = counts.get(cls, 0) + n
        touched.add(cls)
    # residues that differ only by moved placeholders of a region present both sides are still placeholders: counted above
    return touched


# ---- the reading pages ----------------------------------------------------------------------------------------------

def stripped(toks):
    """The tokens put back together without every <nav> and <svg> element and without a line wrapper's style."""
    out, skip = [], []
    for t in toks:
        if skip:
            if t.kind == 'start' and t.tag == skip[-1][0]:
                skip[-1][1] += 1
            elif t.kind == 'end' and t.tag == skip[-1][0]:
                skip[-1][1] -= 1
                if not skip[-1][1]:
                    skip.pop()
            continue
        if t.kind == 'start' and t.tag in ('nav', 'svg'):
            skip.append([t.tag, 1])
            continue
        if t.kind == 'startend' and t.tag in ('nav', 'svg'):
            continue
        if t.kind in ('start', 'startend') and 'style' in t.attrs and is_line_drawing(t.tag, t.attrs):
            out.append(re.sub(r'\s+style=("[^"]*"|\'[^\']*\'|[^\s>]+)', '', t.raw, count=1))
            continue
        out.append(t.raw)
    return ''.join(out)


def panels(text):
    """The shell's panels other than the home and the area pages: id -> stripped text."""
    toks = Tokeniser(text).toks
    out, k = {}, 0
    while k < len(toks):
        t = toks[k]
        if t.kind == 'start' and t.tag == 'section' and 'panel' in classes_of(t.attrs) and t.attrs.get('id'):
            pid, depth, j = t.attrs['id'], 1, k + 1
            while j < len(toks) and depth:
                if toks[j].tag == 'section':
                    depth += 1 if toks[j].kind == 'start' else -1 if toks[j].kind == 'end' else 0
                j += 1
            if pid != 'home' and not pid.startswith('track-'):
                out[pid] = stripped(toks[k:j])
            k = j
            continue
        k += 1
    return out


def first_diff(a, b):
    i = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    return i, a[max(0, i - 120):i + 200], b[max(0, i - 120):i + 200]


# ---- README size table ----------------------------------------------------------------------------------------------

def table_lines(text):
    """Line numbers of kit/README.md's size table: the markdown table rows of the section build.py writes (the block of
    | rows that names index.html)."""
    lines, out = text.split('\n'), set()
    k = 0
    while k < len(lines):
        if lines[k].startswith('|'):
            j = k
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            if any('index.html' in x or 'shell' in x.lower() for x in lines[k:j]) and any(re.search(r'\d[\d,.]* ?(KB|kB|B|MB)\b', x) for x in lines[k:j]):
                out |= set(range(k, j))
            k = j
        else:
            k += 1
    return out


def readme_ok(a, b):
    la, lb = a.split('\n'), b.split('\n')
    ta, tb = table_lines(a), table_lines(b)
    bad = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
        if op != 'equal' and not (set(range(i1, i2)) <= ta and set(range(j1, j2)) <= tb):
            bad.append((la[i1:i2], lb[j1:j2]))
    return bad


# ---- one edition ----------------------------------------------------------------------------------------------------

def check(start, now, edition):
    fa, fb = files(start, edition), files(now, edition)
    counts, fails, touched = {}, [], {}
    reading = {'same': 0, 'kinds': {}}
    for rel in sorted(set(fa) - set(fb)):
        fails.append('%s: removed' % rel)
    for rel in sorted(set(fb) - set(fa)):
        fails.append('%s: added' % rel)
    for rel in sorted(set(fa) & set(fb)):
        a, b = fa[rel].read_bytes(), fb[rel].read_bytes()
        html = rel.endswith('.html')
        if a != b:
            if rel == 'kit/README.md':
                bad = readme_ok(a.decode(), b.decode())
                if bad:
                    fails += ['kit/README.md: a change outside the size table: %r -> %r' % x for x in bad]
                else:
                    counts['size table'] = counts.get('size table', 0) + 1
                    touched.setdefault('size table', set()).add(rel)
            elif html:
                for c in classify_html(rel, a.decode(), b.decode(), counts, fails):
                    touched.setdefault(c, set()).add(rel)
            else:
                fails.append('%s: a non-HTML file differs' % rel)
        if not html:
            continue
        ta, tb = a.decode(), b.decode()
        if rel.endswith('/index.html') and rel.count('/') <= 3 and '<main' in ta:
            pa, pb = panels(ta), panels(tb)
            for pid in sorted(set(pa) ^ set(pb)):
                fails.append('%s#%s: panel only %s' % (rel, pid, 'at start' if pid in pa else 'now'))
            for pid in sorted(set(pa) & set(pb)):
                if pa[pid] == pb[pid]:
                    reading['same'] += 1
                    reading['kinds']['shell panel'] = reading['kinds'].get('shell panel', 0) + 1
                else:
                    i, x, y = first_diff(pa[pid], pb[pid])
                    fails.append('%s#%s: reading text differs at %d:\n    start: %r\n    now:   %r' % (rel, pid, i, x, y))
        else:
            sa, sb = stripped(Tokeniser(ta).toks), stripped(Tokeniser(tb).toks)
            kind = 'fetched page'
            if sa == sb:
                reading['same'] += 1
                reading['kinds'][kind] = reading['kinds'].get(kind, 0) + 1
            else:
                i, x, y = first_diff(sa, sb)
                fails.append('%s: reading text differs at %d:\n    start: %r\n    now:   %r' % (rel, i, x, y))
    return counts, touched, fails, reading, (len(fa), len(fb), sum(1 for r in set(fa) & set(fb) if fa[r].read_bytes() != fb[r].read_bytes()))


# ---- --build --------------------------------------------------------------------------------------------------------

def git(*a, cwd=K.parent):
    r = subprocess.run(['git', *a], cwd=cwd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit('git %s failed: %s' % (' '.join(a), r.stderr.strip()))
    return r.stdout.strip()


def build_tree(rev, editions, keep_dir):
    d = pathlib.Path(tempfile.mkdtemp(prefix='nav-diff-', dir=keep_dir))
    d.rmdir()
    git('worktree', 'add', '--detach', str(d), rev)
    for e in editions:
        r = subprocess.run([sys.executable, '-c', 'import sys; sys.path.insert(0, "."); import baseline; print(round(baseline.build(%r)))' % e],
                           cwd=d / 'kit', capture_output=True, text=True)
        if r.returncode:
            sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
            raise SystemExit('%s: build of %s failed' % (rev, e))
        print('built %s at %s in %s s' % (e, rev[:12], r.stdout.strip()))
    return d


def main():
    ap = argparse.ArgumentParser(usage='python3 kit/nav_diff_check.py <start-tree> <now-tree> | --build <start-commit> [--now REV] [--edition E ...] [--keep]')
    ap.add_argument('trees', nargs='*')
    ap.add_argument('--build')
    ap.add_argument('--now', default='HEAD')
    ap.add_argument('--edition', action='append', choices=EDITIONS)
    ap.add_argument('--keep', action='store_true')
    o = ap.parse_args()
    eds = o.edition or list(EDITIONS)
    made = []
    if o.build:
        if o.trees:
            ap.error('give two trees or --build, not both')
        start = build_tree(git('rev-parse', o.build), eds, '/tmp'); made.append(start)
        now = build_tree(git('rev-parse', o.now), eds, '/tmp'); made.append(now)
    elif len(o.trees) == 2:
        start, now = (pathlib.Path(x).resolve() for x in o.trees)
    else:
        ap.error('give <start-tree> <now-tree>, or --build <start-commit>')
    bad = 0
    try:
        for e in eds:
            counts, touched, fails, reading, (na, nb, nd) = check(start, now, e)
            print('== %s: %d files at start, %d now, %d differ' % (e, na, nb, nd))
            for c in CLASSES:
                if c in counts:
                    print('  %-11s %4d stretches in %3d files' % (c, counts[c], len(touched.get(c, ()))))
            print('  reading pages identical once nav and SVG are stripped: %d (%s)' % (
                reading['same'], ', '.join('%s %d' % kv for kv in sorted(reading['kinds'].items()))))
            for f in fails:
                print('  FAIL ' + f)
            print('  %s: %s' % (e, 'OK' if not fails else '%d unclassified or changed' % len(fails)))
            bad += len(fails)
    finally:
        if made and not o.keep:
            for d in made:
                git('worktree', 'remove', '--force', str(d))
            git('worktree', 'prune')
    print('NAV DIFF CHECK PASSED' if not bad else 'NAV DIFF CHECK FAILED: %d' % bad)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
