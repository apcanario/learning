"""HK-1 · prove that every built file that differs from the start differs ONLY by its intended change.

Run from anywhere:  python3 -I out/HK-1/prove_expected.py   (after `python3 kit/baseline.py --check` has rebuilt both editions)

Start versions:
  academy  /tmp/start/academy (the start build), each file checked against the start commit's kit/baseline.json
  greece   /tmp/start/greece-start (built at the start commit in a throwaway worktree), each file checked likewise
  README   `git show START:kit/README.md`, checked against the start commit's kit/baseline.json
  shell    `git show START:kit/shell.css`
The manifest is the start commit's (`git show START:kit/baseline.json`), whatever kit/baseline.json now holds (it may
have been re-recorded). HK-1 fix pass: 2b proves the hero layers are the drawings themselves (M2), and 5 compares the
README's two changed lines exactly (M4). 2b execs kit/build.py up to its hero_interval line (that part writes nothing).
Reads only; writes nothing. Exit 0 if every check passes, 1 on any FAULT.
"""
import difflib, hashlib, json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
K = REPO / 'kit'
START = '9447f39'
START_ACADEMY = pathlib.Path('/tmp/start/academy')
START_GREECE = pathlib.Path('/tmp/start/greece-start')
GREECE_SITE = 'editions/greece'
FAULTS = []

EXPECTED = {   # manifest path (relative to kit/) -> causes
    'academy/index.html': ['P-HERO1 hero layer', 'P-DEC20 CSS'],
    'editions/greece/index.html': ['P-DEC20 CSS'],
    'README.md': ['P-HERO1 build.py row', 'size table Shell row'],
    **{f'academy/{c}/built.html': ['P-DEC21 Audit cadence cell'] for c in (
        'brand-a', 'brand-b', 'building-with-ai-bw', 'personal-brand-pb', 'sport-psychology-sp',
        'supply-chain-execution-sce', 'ux-ia')},
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git_show(path):
    return subprocess.run(['git', 'show', f'{START}:{path}'], cwd=REPO, capture_output=True, check=True).stdout


def fault(msg):
    FAULTS.append(msg)
    print('  FAULT:', msg)


def ok(msg):
    print('  ok:', msg)


def start_bytes(rel):
    if rel == 'README.md':
        return git_show('kit/README.md')
    if rel.startswith('academy/'):
        return (START_ACADEMY / rel[len('academy/'):]).read_bytes()
    if rel.startswith(GREECE_SITE + '/'):
        return (START_GREECE / rel[len(GREECE_SITE) + 1:]).read_bytes()
    return None   # a bibliography file: none is expected to change


# 0 · the start versions are the manifest's, and which files differ now
print('0 · start versions and the list of differing files')
manifest = json.loads(git_show('kit/baseline.json'))['editions']
print(f'  info: the manifest used is {START}\'s kit/baseline.json; the working kit/baseline.json is '
      + ('the same' if (K / 'baseline.json').read_bytes() == git_show('kit/baseline.json') else 're-recorded since (not used here)'))
differ = {}
for ed, files in manifest.items():
    bad_start = 0
    for rel, h in files.items():
        sb = start_bytes(rel)
        if sb is not None and sha(sb) != h:
            bad_start += 1
            fault(f'{ed}: start version of {rel} does not match the manifest')
    (ok if not bad_start else fault)(f'{ed}: start versions of all {len(files)} manifest files match the start manifest'
                                     if not bad_start else f'{ed}: {bad_start} start versions mismatch')
    for rel, h in files.items():
        p = K / rel
        if not p.exists():
            differ[rel] = 'removed'
        elif sha(p.read_bytes()) != h:
            differ[rel] = 'changed'
    roots = [K / 'academy', K / 'README.md', K / 'bibliography'] if ed == 'academy' else [K / GREECE_SITE]
    if ed == 'academy':
        roots += sorted({(K / r).parent for r in files if r.startswith('../') and '/bibliography/' in r})
    for root in roots:
        for f in ([root] if root.is_file() else sorted(x for x in root.rglob('*') if x.is_file())):
            rel = pathlib.Path(f.resolve()).relative_to(REPO).as_posix()
            rel = rel[4:] if rel.startswith('kit/') else '../' + rel
            if '__pycache__' not in rel and rel not in files:
                differ[rel] = 'added'
for rel, how in sorted(differ.items()):
    print(f'  {how:8} {rel}')
unexpected = sorted(set(differ) - set(EXPECTED))
missing = sorted(set(EXPECTED) - set(differ))
for r in unexpected:
    fault(f'{r} differs ({differ[r]}) and is not on the expected list')
for r in missing:
    fault(f'{r} is on the expected list but does not differ')
if not unexpected and not missing:
    ok(f'{len(differ)} files differ, exactly the {len(EXPECTED)} expected; 0 added, 0 removed; no bibliography file')

old_shell = git_show('kit/shell.css').decode()
new_shell = (K / 'shell.css').read_text(encoding='utf-8')
theme = (REPO / 'design/theme.css').read_text(encoding='utf-8')


def replace_shell(new_text, label):
    """The new shell CSS, inlined verbatim, swapped for the start's; returns the text or None."""
    n = new_text.count(new_shell)
    if n != 1:
        fault(f'{label}: new kit/shell.css occurs {n} times (want 1)')
        return None
    return new_text.replace(new_shell, old_shell)


print('\n1 · the P-DEC20 CSS change itself (kit/shell.css, not in the manifest)')
(ok if new_shell == theme else fault)('kit/shell.css == design/theme.css' if new_shell == theme
                                      else 'kit/shell.css differs from design/theme.css')
ops = list(difflib.SequenceMatcher(None, old_shell.splitlines(True), new_shell.splitlines(True), autojunk=False).get_opcodes())
removed = [o for o in ops if o[0] in ('replace', 'delete')]
added = [o for o in ops if o[0] == 'insert']
nl = new_shell.splitlines(True)
added_text = ''.join(''.join(nl[o[3]:o[4]]) for o in added)
if removed:
    fault(f'kit/shell.css: {len(removed)} hunks change or remove start lines')
else:
    ok(f'kit/shell.css: lines added only, {len(added)} hunks, {sum(o[4] - o[3] for o in added)} lines, '
       f'{len(added_text.encode())} B; nothing removed')
for o in added:
    for line in nl[o[3]:o[4]]:
        print('    +', line.rstrip()[:140])
def code(css):   # the CSS with every comment removed, one token stream
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)


# the header line sits inside the file's opening comment, so compare the comment-free CSS of the whole files
co, cn = code(old_shell).splitlines(), code(new_shell).splitlines()
code_ops = [o for o in difflib.SequenceMatcher(None, co, cn, autojunk=False).get_opcodes() if o[0] != 'equal']
code_added = [l.strip() for t, i1, i2, j1, j2 in code_ops for l in cn[j1:j2] if l.strip()]
code_removed = [l.strip() for t, i1, i2, j1, j2 in code_ops for l in co[i1:i2] if l.strip()]
good = code_added == ['.panel.home>.hero.has-topo{min-height:380px}'] and not code_removed
(ok if good else fault)(f'comments aside, the CSS differs by one added rule {code_added} and nothing removed'
                        if good else f'comment-free CSS: added {code_added}, removed {code_removed}')
first_added = nl[added[0][3]] if added else ''
(ok if added and 'Version 6.16' in first_added and new_shell.index(first_added) < new_shell.index('*/') else fault)(
    'the "Version 6.16" line is inside the file\'s opening comment (a comment, not CSS)')
blk = new_shell[:new_shell.index('.panel.home>.hero.has-topo{min-height:380px}')]
media = blk[blk.rindex('@media'):].split('{')[0].strip()
(ok if media == '@media (min-width:768px)' else fault)(f'the rule sits in the block {media!r}')


def topo_layer(text, label):
    m = list(re.finditer(r'<div class="topo"[^>]*>.*?</svg></div>', text, flags=re.S))
    if len(m) != 1:
        fault(f'{label}: {len(m)} div.topo layers (want 1)')
        return None
    return m[0]


def rises(layer):
    out = {}
    for svg in re.finditer(r'<svg class="topo-l topo-(\w+)".*?</svg>', layer, flags=re.S):
        lay = svg.group(1)
        for g in re.finditer(r'<g class="ct-rise (ct-t\d+)" data-label="([^"]*)" data-words="(\d+)" data-rings="(\d+)"'
                             r'([^>]*)>(.*?)</g>', svg.group(0), flags=re.S):
            paths = re.findall(r'<path d="([^"]*)"', g.group(6))
            out[(lay, g.group(2))] = dict(words=int(g.group(3)), rings=int(g.group(4)), attrs=g.group(5),
                                         body=g.group(6), subpaths=sum(p.count('M') for p in paths))
        out[(lay, '_bytes')] = len(svg.group(0).encode())
    return out


print('\n2 · academy/index.html (P-HERO1 hero layer + P-DEC20 CSS)')
s_old = (START_ACADEMY / 'index.html').read_text(encoding='utf-8')
s_new = (K / 'academy/index.html').read_text(encoding='utf-8')
(ok if s_old.count(old_shell) == 1 else fault)(f'start file holds the start kit/shell.css verbatim once ({s_old.count(old_shell)})')
s_sw = replace_shell(s_new, 'academy/index.html')
if s_sw is not None:
    ok('new file holds the new kit/shell.css verbatim once; swapped for the start\'s')
    to, tn = topo_layer(s_old, 'start'), topo_layer(s_sw, 'new')
    if to and tn:
        if to.start() != tn.start():
            fault(f'the hero layer starts at a different offset ({to.start()} vs {tn.start()}): something before it changed')
        a = s_old[:to.start()] + '<!--TOPO-->' + s_old[to.end():]
        b = s_sw[:tn.start()] + '<!--TOPO-->' + s_sw[tn.end():]
        if a == b:
            ok('start == new once the CSS is swapped back and the one div.topo layer is replaced by a placeholder')
        else:
            d = [l for l in difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm='', n=0)][:12]
            fault('academy/index.html differs outside the CSS and the hero layer:\n      ' + '\n      '.join(x[:160] for x in d))
        lo, ln = to.group(0), tn.group(0)
        print(f'    hero layer bytes: start {len(lo.encode())}, new {len(ln.encode())} ({len(ln.encode()) - len(lo.encode()):+d})')
        head_o, head_n = lo[:lo.index('<svg')], ln[:ln.index('<svg')]
        (ok if head_o == head_n else fault)(f'div.topo opening tag unchanged: {head_n}')
        ro, rn = rises(lo), rises(ln)
        (ok if set(ro) == set(rn) else fault)(f'same layouts and rises in both ({len([k for k in rn if k[1] != "_bytes"])} rise groups)')
        print('    layout  rise            words    rings start>new  subpaths start>new  group')
        for key in sorted(k for k in rn if k[1] != '_bytes'):
            o, n = ro.get(key), rn[key]
            if o is None:
                continue
            same = o['body'] == n['body'] and o['attrs'] == n['attrs']
            print(f'    {key[0]:6}  {key[1]:14} {n["words"]:8}  {o["rings"]:3} > {n["rings"]:<3}       '
                  f'{o["subpaths"]:4} > {n["subpaths"]:<4}       {"identical" if same else "redrawn"}')
            if o['words'] != n['words']:
                fault(f'{key}: words changed {o["words"]} > {n["words"]}')
        for lay in ('tall', 'wide'):
            print(f'    {lay} svg bytes: {ro[(lay, "_bytes")]} > {rn[(lay, "_bytes")]}')
        hist = [rn[k]['rings'] - ro[k]['rings'] for k in rn if k[1] == 'History']
        others = [k for k in rn if k[1] not in ('History', '_bytes') and rn[k]['rings'] != ro[k]['rings']]
        (ok if hist == [-1, -1] and not others else fault)(
            'ring counts: History 21 > 20 in both layouts, every other rise unchanged' if hist == [-1, -1] and not others
            else f'ring counts changed unexpectedly: History {hist}, others {others}')
        dsize = len(s_new.encode()) - len(s_old.encode())
        want = len(added_text.encode()) + len(ln.encode()) - len(lo.encode())
        (ok if dsize == want else fault)(f'file size {len(s_old.encode())} > {len(s_new.encode())} ({dsize:+d} B) '
                                         f'= CSS {len(added_text.encode()):+d} + hero {len(ln.encode()) - len(lo.encode()):+d}')

print('\n2b · the hero layers are the drawings themselves (HK-1 M2)')
BUDGET = 19 * 1024
FLOOR = 24000


def vbytes(h):   # verify.py's measure, new Blob([topo.outerHTML]).size: each self-closed element with its end tag
    return len(re.sub(r'<(\w+)([^<>]*?)/>', r'<\1\2></\1>', h).encode())


def build_prefix():
    """kit/build.py run up to the line that derives the hero's interval (that part writes nothing): its namespace."""
    import os
    src = (K / 'build.py').read_text(encoding='utf-8')
    cut = 'HERO_INTERVAL, hero_topo = hero_interval(HERO_TOPO)'
    if src.count(cut) != 1:
        fault(f'kit/build.py: the line {cut!r} occurs {src.count(cut)} times (want 1)')
        return None
    argv, cwd = sys.argv, os.getcwd()
    sys.argv, g = ['build.py'], {'__name__': 'hk1_prove', '__file__': str(K / 'build.py')}
    sys.path.insert(0, str(K))
    os.chdir(K)
    try:
        exec(compile(src[:src.index(cut)], str(K / 'build.py'), 'exec'), g)
    finally:
        sys.argv = argv
        os.chdir(cwd)
    return g


lay_old = topo_layer(s_old, 'start')
lay_new = topo_layer(s_new, 'new')
g = build_prefix() if lay_old and lay_new else None
if g:
    viz, T = g['viz'], g['HERO_TOPO']
    (ok if (g['HERO_INTERVAL_MIN'], g['HERO_BUDGET']) == (FLOOR, BUDGET) else fault)(
        f'build.py: HERO_INTERVAL_MIN {g["HERO_INTERVAL_MIN"]:,}, HERO_BUDGET {g["HERO_BUDGET"]:,} (want {FLOOR:,}, {BUDGET:,})')
    at_floor = viz.render(dict(T, interval=FLOOR))
    (ok if lay_old.group(0) == at_floor else fault)(f'start layer == viz.render(HERO_TOPO, interval={FLOOR:,}) '
                                                    f'({len(at_floor.encode()):,} B; {vbytes(at_floor):,} B as verify counts)')
    # the smallest whole hundred from the floor up whose drawing is within the budget as verify counts, by a full scan
    k, drawing = FLOOR, at_floor
    while vbytes(drawing) > BUDGET:
        k += 100
        drawing = viz.render(dict(T, interval=k))
    iv, layer = g['hero_interval'](T)
    (ok if iv == k else fault)(f'build.py hero_interval() gives {iv:,}; a full scan from {FLOOR:,} in steps of 100 gives {k:,}')
    (ok if lay_new.group(0) == drawing == layer else fault)(
        f'new layer == viz.render(HERO_TOPO, interval={k:,}) ({len(drawing.encode()):,} B; {vbytes(drawing):,} B as verify counts, '
        f'budget {BUDGET:,})')
    (ok if k == FLOOR or vbytes(drawing) <= BUDGET < vbytes(viz.render(dict(T, interval=k - 100))) else fault)(
        f'{k:,} fits and {k - 100:,} does not ({vbytes(viz.render(dict(T, interval=k - 100))):,} B as verify counts)')

print('\n3 · editions/greece/index.html (P-DEC20 CSS only)')
g_old = (START_GREECE / 'index.html').read_text(encoding='utf-8')
g_new = (K / GREECE_SITE / 'index.html').read_text(encoding='utf-8')
g_sw = replace_shell(g_new, 'greece index.html')
if g_sw is not None:
    if g_sw == g_old:
        ok('start == new once the new kit/shell.css is swapped for the start\'s (hero layer byte-identical too)')
    else:
        d = [l for l in difflib.unified_diff(g_old.splitlines(), g_sw.splitlines(), lineterm='', n=0)][:12]
        fault('greece index.html differs outside the CSS:\n      ' + '\n      '.join(x[:160] for x in d))
    print(f'    size {len(g_old.encode())} > {len(g_new.encode())} ({len(g_new.encode()) - len(g_old.encode()):+d} B)')

print('\n4 · the seven built.html (P-DEC21 Audit cadence cell)')
ROW = re.compile(r'(<tr><td>Audit cadence</td><td>[^<]*</td><td>)(.*?)(</td></tr>)', flags=re.S)
cells = set()
for rel in [r for r in EXPECTED if r.endswith('/built.html')]:
    o = start_bytes(rel).decode()
    n = (K / rel).read_text(encoding='utf-8')
    mo, mn = ROW.findall(o), ROW.findall(n)
    if len(mo) != 1 or len(mn) != 1:
        fault(f'{rel}: Audit cadence rows start {len(mo)}, new {len(mn)} (want 1 each)')
        continue
    a, b = ROW.sub(r'\1CELL\3', o), ROW.sub(r'\1CELL\3', n)
    if a == b:
        ok(f'{rel}: identical once the cell is replaced ({len(n.encode()) - len(o.encode()):+d} B)')
    else:
        fault(f'{rel}: differs outside the Audit cadence cell')
    cells.add((mo[0][1], mn[0][1]))
if len(cells) == 1:
    (old_c, new_c), = cells
    ok('the same old and new cell in all seven')
    print('    old:', old_c)
    print('    new:', new_c)
else:
    fault(f'{len(cells)} different (old, new) cell pairs across the seven files')

print('\n5 · README.md (kit/README.md)')
r_old = git_show('kit/README.md').decode()
r_new = (K / 'README.md').read_text(encoding='utf-8')
lo_, ln_ = r_old.splitlines(), r_new.splitlines()
sm = difflib.SequenceMatcher(None, lo_, ln_, autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != 'equal']
s0, s1 = ln_.index('<!-- sizes:start -->'), ln_.index('<!-- sizes:end -->')
in_table, outside = [], []
for tag, i1, i2, j1, j2 in ops:
    if tag != 'replace' or i2 - i1 != j2 - j1:
        fault(f'README.md: a {tag} hunk (lines {i1}-{i2} > {j1}-{j2}), not a line-for-line replacement')
        continue
    for i, j in zip(range(i1, i2), range(j1, j2)):
        (in_table if s0 < j < s1 else outside).append((lo_[i], ln_[j]))
print(f'    {len(in_table)} line(s) changed in the size table, {len(outside)} outside it')
for o, n in in_table:
    print('    table -', o)
    print('    table +', n)


def kb(x):
    return f'{x / 1024:,.0f} KB' if x < 1024 * 1024 else f'{x / 1024 / 1024:.2f} MB'


shell_ok = len(in_table) == 1 and in_table[0][0].startswith('| Shell (`index.html`) |') and \
    in_table[0][0] == f'| Shell (`index.html`) | 1 | {kb(len(s_old.encode()))} | {kb(len(s_old.encode()))} | home, drawer, the build pages of the markdown courses, backlog |' and \
    in_table[0][1] == f'| Shell (`index.html`) | 1 | {kb(len(s_new.encode()))} | {kb(len(s_new.encode()))} | home, drawer, the build pages of the markdown courses, backlog |'
(ok if shell_ok else fault)(f'size table: only the Shell row changed, and both rows match the files '
                            f'({len(s_old.encode())} B = {kb(len(s_old.encode()))}, {len(s_new.encode())} B = {kb(len(s_new.encode()))})'
                            if shell_ok else 'size table: change is not exactly the Shell row recomputed from the files')
# HK-1 M4: exact. The build.py row is the start row with one phrase replaced by P-HERO1's text below; the Shell row is
# the start row with both sizes recomputed from the files; every other byte of the file is the start's.
OLD_PHRASE = 'a contour every 22,000 words (`HERO_INTERVAL`), in two fixed layouts'
NEW_PHRASE = ("a contour every `HERO_INTERVAL` words, derived when the site is built (P-HERO1, 21 Nov 2026: the floor "
              "`HERO_INTERVAL_MIN`, 24,000, W-SCE1's value kept so that no edition's hero moves (P92 drew 22,000), or the "
              "smallest whole hundred of words above it, found by a scan upward from it (the layer shrinks as the interval "
              "grows overall, not at every step), at which the layer, both layouts, is within `HERO_BUDGET`, 19 KB as "
              "`verify.py` measures it (the outerHTML, each self-closed element with its end tag), under its 20 KB limit; "
              "24,500 for academy, 19,388 B, and 24,000 for greece, marketing-ai and the template edition that day), in two "
              "fixed layouts")
SHELL = '| Shell (`index.html`) | 1 | {0} | {0} | home, drawer, the build pages of the markdown courses, backlog |'
old_rows = [i for i, l in enumerate(lo_) if l.startswith('| `build.py` |')]
old_shell_rows = [i for i, l in enumerate(lo_) if l.startswith('| Shell (`index.html`) |')]
if len(old_rows) != 1 or len(old_shell_rows) != 1 or lo_[old_rows[0]].count(OLD_PHRASE) != 1:
    fault('README.md start: not exactly one build.py row holding the old phrase and one Shell row')
else:
    want = lo_[:]
    want[old_rows[0]] = lo_[old_rows[0]].replace(OLD_PHRASE, NEW_PHRASE)
    want[old_shell_rows[0]] = SHELL.format(kb(len(s_new.encode())))
    (ok if lo_[old_shell_rows[0]] == SHELL.format(kb(len(s_old.encode()))) else fault)(
        'the start Shell row is the start index.html\'s size')
    want_text = '\n'.join(want) + ('\n' if r_old.endswith('\n') else '')
    if want_text == r_new:
        ok('README.md == the start file with exactly the build.py row (one phrase replaced by P-HERO1\'s text) and the '
           'Shell row (recomputed) changed; every other byte identical')
    else:
        d = [l for l in difflib.unified_diff(want_text.splitlines(), r_new.splitlines(), lineterm='', n=0)][:8]
        fault('README.md is not exactly the expected file:\n      ' + '\n      '.join(x[:160] for x in d))
    wt = subprocess.run(['git', 'diff', '--numstat', START, '--', 'kit/README.md'], cwd=REPO, capture_output=True, text=True).stdout.split()
    print(f'    git diff {START} kit/README.md: +{wt[0]} -{wt[1]} lines (the build.py row and the Shell row)')

print('\nSUMMARY')
by = {}
for rel, cs in EXPECTED.items():
    for c in cs:
        by.setdefault(c, []).append(rel)
for c, rs in by.items():
    print(f'  {c}: {len(rs)} file(s): {", ".join(rs)}')
print(f'  distinct files differing: {len(differ)} (expected {len(EXPECTED)})')
print(f'  VERDICT: {"PASS, every difference is intended" if not FAULTS else f"FAULT ({len(FAULTS)})"}')
for f in FAULTS:
    print('   -', f.splitlines()[0])
sys.exit(1 if FAULTS else 0)
