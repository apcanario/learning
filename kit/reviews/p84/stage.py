"""P84/P109: stage the figure re-checkers' packets by script. Each packet holds, per figure: the page's text without its
figures (the vault file with every ```viz block replaced by a marker), the figure's caption, and the frames sheets
verify.py's frames() saved for it (320, 390 and 1280 px, dark and light). A course-home or examples figure, which has no
unit text, gets its declaration and (Rome's home) the report it draws on.
usage: python3 stage.py <changed list> <shots dir> <packets root> <prefix> <n agents>"""
import json, pathlib, re, shutil, sys
R = pathlib.Path('/home/claude/learning')
changed, shots, root, prefix, n = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4], int(sys.argv[5])
sys.path.insert(0, str(R / 'kit'))
VIZ = re.compile(r'```viz\n(.*?)```', re.S)
idx = (R / 'kit/academy/index.html').read_text()
src2pid = {src: pid for pid, src in re.findall(r'<section class="panel[^"]*" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)}

def vault(page):
    m = re.match(r'(greece|rome)/r-([\d.]+)\.html$', page)
    if m: return next((R / 'courses' / m.group(1)).glob(m.group(2) + '-*.md'))
    m = re.match(r'([\w-]+)/read-([\w-]+)\.html$', page)
    if m:
        code = m.group(2).upper()
        for d in (R / 'courses').iterdir():
            hits = list(d.glob(code + '-*.md'))
            if hits: return hits[0]
    return None

items = []
for line in open(changed):
    m = re.match(r'(\S+) figure (\d+) \((\w+)\)', line)
    if m: items.append((m.group(1), int(m.group(2)), m.group(3)))
pages = sorted({p for p, _, _ in items}, key=lambda p: [x for x, _, _ in items].index(p))
groups = [[] for _ in range(n)]
for i, p in enumerate(pages):                                    # whole pages per agent, balanced by figure count
    min(groups, key=lambda g: sum(1 for x in items if x[0] in g)).append(p)
for gi, g in enumerate(groups, 1):
    out = root / f'{prefix}-{gi}'
    if out.exists(): shutil.rmtree(out)
    (out / 'text').mkdir(parents=True); (out / 'sheets').mkdir(); (out / 'out').mkdir()
    lines = [f'# Figures to re-check ({prefix}-{gi})\n']
    for page in g:
        pid = src2pid[page]
        figs = [x for x in items if x[0] == page]
        v = vault(page)
        decls = []
        if v:
            src = v.read_text(); decls = [json.loads(b) for b in VIZ.findall(src)]
            k = [0]
            def mark(mm):
                k[0] += 1; return f'[Figure {k[0]} is drawn here; see its caption and sheets if it is in your list]\n'
            (out / 'text' / f'{pid}.md').write_text(VIZ.sub(mark, src))
        elif page == 'rome/home.html':
            import courses
            decls = [courses.ROME['figure']]
            r31 = next((R / 'courses/rome').glob('3.1-*.md'))
            (out / 'text' / f'{pid}--source-rome-3.1.md').write_text(VIZ.sub('[a figure of the report]\n', r31.read_text()))
        else:
            import viz_examples
            decls = [e[-1] for e in viz_examples.EXAMPLES + viz_examples.CASES]
        for page_, k, kind in figs:
            cap = ''
            d = decls[k - 1] if len(decls) >= k else decls[0]
            assert d['kind'] == kind, (page, k, kind, len(decls))
            cap = d.get('caption', '')
            sheets = sorted(shots.glob(f'*-{pid}-fig-{k:02d}-{kind}-frames-*.png'))
            for s in sheets: shutil.copy(s, out / 'sheets' / s.name)
            lines.append(f'## {page} figure {k} ({kind}) · panel {pid}\n')
            lines.append(f'- Text: ' + (f'text/{pid}.md (marker "[Figure {k} ...]" shows where it sits)' if v else 'see the declaration below') + '\n')
            lines.append(f'- Sheets ({len(sheets)}): ' + ', '.join('sheets/' + s.name for s in sheets) + '\n')
            if cap: lines.append(f'- Caption: {cap}\n')
            if not v:
                lines.append(f'- Declaration (no unit text: the figure is drawn from this block' + (', and its caption names Rome 3.1, given in text/' if page == 'rome/home.html' else '; the page shows the block itself') + '):\n\n```json\n' + json.dumps(d, ensure_ascii=False, indent=1) + '\n```\n')
            lines.append('\n')
    (out / 'figures.md').write_text(''.join(lines))
    print(out, len(g), 'pages', sum(1 for x in items if x[0] in g), 'figures', len(list((out / 'sheets').glob('*.png'))), 'sheets')
