"""P95 (8 Nov 2026) · the two fresh checkers' folders, by script, so each sees only what it is given.

  checker A (the library)   outlines.json, every outline's SVG, the three sets' licence files as their repositories
                            hold them at the commits recorded, the contact sheet (dark and light), and the grep lines:
                            for each outline and each course it serves, the lines of that course's texts that name it
                            (its keywords), at most eight per course, each with its file and line number
  checker B (the pilots)    for each page uses.json maps: the built page as the site fetches it, its text as plain
                            text, the lines of its text that name the object, the outline's entry in outlines.json;
                            the shots (p95_shots.py) at six widths, dark and light, and the five poses; theme.css's
                            relief rules (section 9) and its tokens

    python3 p95_extract.py <icon clones folder> <contact sheet folder> <shots folder> <checker A folder> <checker B folder>
"""
import html, json, pathlib, re, shutil, subprocess, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
LIB = ROOT / 'design' / 'outlines'
sys.path.insert(0, str(R))
import p95_library   # noqa: E402  the course texts and the sets

LICENCE_FILES = {'game-icons/icons': ('game-icons_icons', 'license.txt'), 'phosphor-icons/core': ('phosphor-icons_core', 'LICENSE'),
                 'tabler/tabler-icons': ('tabler_tabler-icons', 'LICENSE')}


def grep_lines(course, kws, oid='', cap=8):
    rx = re.compile(r'\b(?:' + '|'.join(re.escape(k) for k in kws) + r')\b', re.I)
    out = []
    for f in p95_library.TEXTS[course]:
        for n, ln in enumerate(p95_library.prose(f, oid).splitlines(), 1):   # its prose: figure data and the outline's excludes taken out (line numbers of the prose)
            if rx.search(ln):
                s = ln.strip()
                m = rx.search(s)
                a = max(0, m.start() - 140)
                out.append(f'{f.relative_to(ROOT).as_posix()}:{n}: {"…" if a else ""}{s[a:a + 300]}{"…" if len(s) > a + 300 else ""}')
    return out[:cap], len(out)


def checker_a(clones, sheet, out):
    out.mkdir(parents=True, exist_ok=True)
    (out / 'svg').mkdir(exist_ok=True)
    lib = json.loads((LIB / 'outlines.json').read_text())
    shutil.copy(LIB / 'outlines.json', out / 'outlines.json')
    for o in lib['outlines']:
        shutil.copy(LIB / o['file'], out / 'svg' / o['file'])
    for repo, (cl, f) in LICENCE_FILES.items():
        txt = subprocess.run(['git', '-C', str(clones / cl), 'show', f'HEAD:{f}'], capture_output=True, text=True, check=True).stdout
        sha = subprocess.run(['git', '-C', str(clones / cl), 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
        (out / f'licence-{cl}.txt').write_text(f'{repo} at {sha}, file {f}:\n\n{txt}')
    for t in ('dark', 'light'):
        shutil.copy(sheet / f'sheet-{t}.png', out / f'contact-sheet-{t}.png')
    g = ['# Grep lines', '', 'For each outline and each course it serves: the lines of that course\'s texts that name it (its keywords, whole words, any case), at most eight per course, with the total; read from the prose (figure declarations and the outline\'s excludes taken out, so a line number may differ from the file\'s where a figure stood above it).', '']
    for o in lib['outlines']:
        g.append(f'## {o["id"]} · {o["depicts"]} · keywords: {", ".join(o["keywords"])}')
        for c in o['courses']:
            lines, n = grep_lines(c, o['keywords'], o['id'])
            g.append(f'### {c}: {n} lines in all')
            g += [f'- {x}' for x in lines]
        g.append('')
    (out / 'grep-lines.md').write_text('\n'.join(g), encoding='utf-8')
    rel = ['# The relief tool and its measures', '', (R / 'relief.py').read_text().split('"""')[1], '',
           '| id | width x height | lines | depth px | step px | regions | thin parts |', '|---|---|---|---|---|---|---|']
    for o in lib['outlines']:
        d = json.loads((LIB / f'{o["id"]}.json').read_text())
        r = d['render']
        rel.append(f'| {o["id"]} | {d["width"]} x {d["height"]} | {len(d["lines"])} | {r["depth_px"]} | {r["step_px"]} | {r["regions"]} | {r["thin_parts"]} |')
    (out / 'relief-measures.md').write_text('\n'.join(rel) + '\n', encoding='utf-8')


def checker_b(shots, out):
    out.mkdir(parents=True, exist_ok=True)
    (out / 'shots').mkdir(exist_ok=True)
    lib = {o['id']: o for o in json.loads((LIB / 'outlines.json').read_text())['outlines']}
    uses = json.loads((LIB / 'uses.json').read_text())['uses']
    shutil.copy(LIB / 'uses.json', out / 'uses.json')
    shell = (R / 'academy' / 'index.html').read_text()
    for pid, oid in uses.items():
        src = re.search(rf'<section class="panel[^"]*" id="{pid}"[^>]*data-src="([^"]+)"', shell).group(1)
        page = (R / 'academy' / src).read_text()
        (out / f'{pid}-page.html').write_text(page)
        text = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', ' ', page, flags=re.S))))
        (out / f'{pid}-text.txt').write_text(text)
        o = lib[oid]
        rx = re.compile(r'\b(?:' + '|'.join(re.escape(k) for k in o['keywords']) + r')\b', re.I)
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if rx.search(s)]
        (out / f'{pid}-object.md').write_text(f'# {pid}: the sentences of the page that name {o["depicts"]} (keywords {", ".join(o["keywords"])}), {len(sents)} in all\n\n'
                                              + '\n'.join(f'- {s}' for s in sents) + f'\n\n## Its entry in outlines.json\n\n```json\n{json.dumps(o, indent=1, ensure_ascii=False)}\n```\n')
    for f in sorted(shots.glob('*.png')):
        shutil.copy(f, out / 'shots' / f.name)
    th = (ROOT / 'design' / 'theme.css').read_text()
    keep = [ln for ln in th.splitlines() if re.search(r'relief|--topo-|topo-l\{|\.topo\{|\.topo-l|figcaption|@keyframes topo|prefers-reduced-motion:no-preference\)\{\.topo', ln)]
    (out / 'theme-relief-rules.css').write_text('/* the lines of design/theme.css that bear on the relief: its tokens, the topography rules it shares, its own rules (section 9) */\n' + '\n'.join(keep) + '\n')


if __name__ == '__main__':
    a = [pathlib.Path(x) for x in sys.argv[1:6]]
    checker_a(a[0], a[1], a[3])
    checker_b(a[2], a[4])
    print('written', a[3], a[4])
