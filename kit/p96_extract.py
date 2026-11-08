"""P96 (8 Nov 2026) · the two fresh checkers' folders, by script, so each sees only what it is given.

  checker H (Greece and Rome)            for its courses: every reading page, with its relief (outline, deciding
  checker M (Personal brand, Building     sentence and the paragraph round it) or none (its section headings and the
  with AI, Information architecture)      lines of its text that name any outline of the library, at most three for
                                          each of the four it names most); the library (every outline: what it
                                          depicts, the courses it serves, its keywords, spare or not; the rejected
                                          candidates and why); the contact sheet, dark and light; the shots of a
                                          sample of its pages (p95_shots.py: 390 and 1280 px, dark and light, five poses)

    python3 p96_extract.py <contact sheet folder> <shots folder> <checker H folder> <checker M folder>
"""
import json, pathlib, re, shutil, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
LIB = ROOT / 'design' / 'outlines'
sys.path.insert(0, str(R))
import p95_library as L   # noqa: E402
import p96_uses as U      # noqa: E402

GROUPS = {'H': ['greece', 'rome'], 'M': ['brand-a', 'brand-b', 'ux-ia']}


def title(f):
    t = f.read_text(encoding='utf-8')
    m = re.search(r'^title:\s*(.+)$', t, re.M) or re.search(r'^#\s+(.+)$', t, re.M)
    return m.group(1).strip() if m else f.stem


def paragraph(t, words, cap=1400):
    ps = re.split(r'\n\s*\n', t)
    for i, p in enumerate(ps):
        if words in p:
            if p.lstrip().startswith('#') and i + 1 < len(ps):   # a heading decided it: the paragraph under it too
                p = p + '\n\n' + ps[i + 1]
            p = p.strip().replace('*', '')
            if len(p) > cap:
                i = max(0, p.find(words.replace('*', '')) - cap // 2)
                p = ('…' if i else '') + p[i:i + cap] + '…'
            return p
    return ''


def library(out):
    lib = json.loads((LIB / 'outlines.json').read_text())
    g = ['# The outline library', '', f'{len(lib["outlines"])} outlines. Each is drawn as a relief (the contact sheet) and captioned "<depicts>, a stylised outline drawn as a relief from an icon. <credit>." A sign is said to be one, "(the sign for …)". "spare": in the library, on no page yet.', '',
         '| id | depicts | courses | keywords | spare |', '|---|---|---|---|---|']
    for o in lib['outlines']:
        g.append(f'| {o["id"]} | {o["depicts"]} | {", ".join(o["courses"])} | {", ".join(o["keywords"])} | {o.get("spare", "")} |')
    g += ['', '## Rejected candidates', '']
    g += [f'- {r["source"]["repository"]} {r["source"]["path"]}: {r["reason"]}' for r in lib['rejected']]
    (out / 'library.md').write_text('\n'.join(g) + '\n', encoding='utf-8')
    return lib


def mapping(courses, lib, out):
    P = U.pages()
    M = {pid: (oid, w) for pid, oid, w in U.MAP}
    named = {}
    for o in lib['outlines']:
        for c, lst in o['texts'].items():
            for f, n in lst:
                named.setdefault((c, f), []).append((n, o))
    g = ['# The mapping', '', 'Every reading page of your courses, in order: its relief (the outline, how often its prose names the outline by its keywords, the deciding sentence, and the paragraph round it) or none (its section headings, and the lines of its text that name an outline of the library, at most three for each of the four it names most, with the count). The rules: a page gets at most one relief, only where its text discusses an object at length, not in passing; one outline may serve several pages, but not two neighbouring reports of one unit where the second text allows another (a pair allowed is listed with its reason).', '']
    key = lambda pid: [int(x) if x.isdigit() else x for x in re.split(r'[.\-]', P[pid][2])]
    for c in courses:
        g += [f'## {U.NAMES[c]}', '']
        for pid in sorted([p for p in P if P[p][0] == c], key=key):
            _, f, code = P[pid]
            t = L.prose(f, '')
            rel = f.relative_to(ROOT).as_posix()
            g.append(f'### {code} · {title(f)} (`{pid}`)')
            if pid in M:
                oid, w = M[pid]
                o = next(x for x in lib['outlines'] if x['id'] == oid)
                n = len(re.findall(r'\b(?:' + '|'.join(re.escape(k) for k in o['keywords']) + r')\b', L.prose(f, oid), re.I))
                g += [f'**Relief: {oid}** ({o["depicts"]}); its prose names it {n} times.', '',
                      f'Deciding sentence: {U.sentence(t, w)}', '', 'The paragraph round it:', '', '> ' + paragraph(t, w).replace('\n', '\n> '), '']
            else:
                heads = [h.strip('# ').strip() for h in re.findall(r'^#{2,3} .+$', t, re.M)]
                g += ['**None.**', '', 'Headings: ' + ' / '.join(heads[:20]), '']
                top = sorted(named.get((c, rel), []), key=lambda x: -x[0])[:4]
                if not top:
                    g += ['Its text names no outline of the library.', '']
                for n, o in top:
                    rx = re.compile(r'\b(?:' + '|'.join(re.escape(k) for k in o['keywords']) + r')\b', re.I)
                    ss = [s.strip().replace('*', '') for s in re.split(r'(?<=[.!?])\s+|\n+', L.prose(f, o['id'])) if rx.search(s)][:3]
                    g.append(f'- {o["id"]} ({o["depicts"]}), named {n} times:')
                    g += [f'  - {s[:300]}' for s in ss]
                g.append('')
        for (a, b), why in U.NEIGHBOURS_OK.items():
            if P[a][0] == c:
                g += [f'**Neighbours sharing an outline:** {a} and {b}: {why}.', '']
    (out / 'mapping.md').write_text('\n'.join(g), encoding='utf-8')


def main():
    sheet, shots, outs = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), [pathlib.Path(x) for x in sys.argv[3:5]]
    for (k, courses), out in zip(GROUPS.items(), outs):
        if out.exists():
            shutil.rmtree(out)
        (out / 'shots').mkdir(parents=True)
        lib = library(out)
        mapping(courses, lib, out)
        for t in ('dark', 'light'):
            shutil.copy(sheet / f'contact-sheet-{t}.png', out / f'contact-sheet-{t}.png')
        mine = {pid for pid, (c, _, _) in U.pages().items() if c in courses}
        n = 0
        for f in shots.glob('*.png'):
            if f.name.split('-pose')[0].rsplit('-', 2)[0] in mine or f.name.split('-pose')[0] in mine:
                shutil.copy(f, out / 'shots' / f.name); n += 1
        print(f'{out}: mapping.md, library.md, the contact sheet, {n} shots')


if __name__ == '__main__':
    main()
