"""P96 (8 Nov 2026) · the reliefs rolled out: which reading page shows which outline of the library, and why.

MAP holds, for every reading page given a relief, its panel id, the outline (design/outlines/outlines.json) and the
words of the sentence that decided it: the sentence in the page's own prose (p95_library.prose: the front matter, figure
declarations, link targets, URLs and a unit's Sources taken out) that shows the text discussing the object at length,
not in passing. A page not in MAP gets no relief: its text discusses no object at length. This script finds each
deciding sentence in the text (it stops if the words are not there, or if the page does not name the outline by one of
its keywords), checks the rules (at most one relief a page; an outline not on two neighbouring reports of one unit; at
least ten outlines in use in every course with ten pages or more, and in every course with fewer, every page that
discusses an object; every outline in use or marked spare) and writes:

    design/outlines/uses.json     panel id -> outline, which mdcourse.reading draws
    design/outlines/uses-why.md   each page's outline and its deciding sentence; the pages with none, with the
                                  outline their text names most and how often

    python3 p96_uses.py
"""
import json, pathlib, re, sys

import p95_library as L

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
LIB = ROOT / 'design' / 'outlines'
NAMES = {'greece': 'Greece', 'rome': 'Rome', 'brand-a': 'Personal brand', 'brand-b': 'Building with AI', 'ux-ia': 'Information architecture'}

# panel id, outline, the words of its deciding sentence (as they stand in the page's prose)
MAP = [
    # Greece
    ('m01', 'vase', 'Tens of thousands of mythical images from the seventh to the fourth centuries BC'),
    ('m11', 'bull', 'dominates: bull-leaping on seals'),
    ('m12', 'tablet', 'burned in a single fire that baked its 1,100 tablets'),
    ('m26', 'centaur', 'Centaurs: the sin of Ixion'),
    ('m24', 'eagle', 'a long-winged eagle sent to eat his liver'),
    ('m31', 'winged-sandal', 'From the nymphs he received the winged sandals'),
    ('m32', 'hydra', 'Many-headed snake reared by Hera'),
    ('m33', 'minotaur', 'for the Labyrinth and the Minotaur'),
    ('m34', 'ram', 'The Fleece: Athamas, Ino, Phrixus and Helle'),
    ('m43', 'wooden-horse', "builds the Wooden Horse"),
    ('m51', 'temple', 'The first temples and the Geometric style'),
    ('m53', 'coins', 'The earliest coins are electrum'),
    ('m55', 'ostrakon', 'Ostracism was first used in 487'),
    ('m61', 'trireme', 'build two hundred warships'),
    ('m63', 'wall', 'bring the population inside the walls'),
    ('m64', 'theatre-masks', 'Masks let three men play twelve roles'),
    ('m72', 'scroll', 'Ptolemaic papyri from before about 150 BC'),
    ('m81', 'temple', "housed the god's image and treasure"),
    ('m82', 'tablet', 'over four thousand lead tablets'),
    ('m83', 'olive', 'gave a wreath of wild olive'),
    ('m62', 'ostrakon', 'every citizen could scratch a name on a sherd'),
    ('m84', 'vase', 'The characteristic fifth-century vessel is the white-ground'),
    ('m91', 'vase', 'reach a peak on the Chigi Vase'),
    ('m92', 'temple', 'Temple of Athena Nike'),
    ('m104', 'wooden-horse', 'The Palladium and the horse are the two exploits'),
    ('m105', 'gladius', 'Menelaus goes for Helen with drawn sword and drops it at the sight of her'),
    ('m106', 'greek-helmet', 'that helmet frightens Astyanax'),
    ('m1010', 'wall', 'great limestone walls with towers and gates'),
    ('m112', 'horse', 'The fight on the bank was a cavalry melee'),
    ('m117', 'coins', 'Coins and the Porus medallions'),
    ('m121', 'scroll', 'The Strasbourg papyrus is a roll'),
    ('m125', 'coins', 'Debased Sinopean coins of about 350'),
    ('m126', 'wall', "Diogenes of Oinoanda's wall"),
    # Rome
    ('rm11', 'tablet', 'seven bronzes found at Gubbio in 1444'),
    ('rm12', 'vase', 'Most of the finest Attic black- and red-figure vases in museums came from Etruscan graves'),
    ('rm14', 'wolf', 'A she-wolf coming down to drink heard the crying'),
    ('rm15', 'temple', 'as a platform carrying a temple of roughly 34 by 38 metres'),
    ('rm16', 'tablet', 'The Pyrgi tablets (module 1.2) record about 500 BC'),
    ('rm22', 'temple', 'The temple of Jupiter Optimus Maximus'),
    ('rm25', 'bull', 'Mithras: the bull, the cave and the grades'),
    ('rm31', 'scales', 'The Decemvirate and the Twelve Tables'),
    ('rm33', 'wall', 'The lasting answer was the wall'),
    ('rm35', 'coins', "Rome's first silver coins were didrachms"),
    ('rm42', 'trireme', 'Rome ordered 100 quinqueremes and 20 triremes'),
    ('rm43', 'horse', 'put the Roman cavalry by the river'),
    ('rm55', 'trireme', 'On 2 September Antony brought the fleet out'),
    ('rm62', 'temple', 'The house on the Palatine and the temple of Apollo'),
    ('rm64', 'coins', 'Reinhard Wolters argued that the coins cannot exclude a later date'),
    ('rm71', 'tablet', 'The bronze from Lyon (CIL XIII 1668) preserves part of the speech'),
    ('rm72', 'temple', 'the temple of Jupiter Best and Greatest burned'),
    ('rm74', 'scroll', 'A damaged Greek papyrus at Giessen'),
    ('rm75', 'coins', 'The coinage tied the system together'),
    ('rm81', 'sun', 'he dedicated a temple of Sol in Rome'),
    ('rm82', 'coins', 'The coinage was rebuilt about 294'),
    ('rm83', 'sun', 'The coins hedge too'),
    ('rm84', 'temple', 'Julian ordered the temples opened'),
    ('rm91', 'scales', 'Custom made law'),
    ('rm92', 'tablet', 'a certified copy on two bronze tablets sealed by seven witnesses'),
    ('rm95', 'temple', 'The temple platform'),
    ('rm103', 'temple', 'Etruria gave the temple'),
    ('rm104', 'eagle', 'when he gave his regiments eagles'),
    ('rm117', 'dagger', 'with his dagger drawn'),
    ('rm122', 'wooden-horse', 'The Greeks feign departure and leave the horse'),
    ('rm124', 'gladius', 'She falls on the sword'),
    ('rm125', 'bough', 'A golden bough hides in a dark tree'),
    ('rm135', 'libation', 'The libation to Jupiter the Liberator'),
    # Personal brand
    ('read-a1', 'film-slate', 'The two vlog episodes against the positioning'),
    ('read-a2', 'audience', 'The brief defines the audience by four traits'),
    ('read-a3', 'calendar', 'Deliverable 2 · The 12-week calendar from 3 November 2026'),
    ('read-a4', 'notebook', 'The record of failures, and the record becoming the content'),
    ('read-a5', 'phone', 'The phone on a tripod'),
    ('read-a6', 'envelope', 'always own your readers'),
    ('read-a7', 'money', '2027 money comes from two places'),
    ('read-a8', 'scales', 'The employment contract: what the law allows'),
    ('read-a9', 'chart', 'The median growth rate in the 1,000–9,999 band'),
    ('read-dd-a1', 'film-slate', 'people responded to the very first video he posted'),
    ('read-audience-growth', 'audience', 'Conversion from audience to buyer runs at'),
    ('read-dd-a2', 'piggy-bank', 'Every month of an exit is paid from savings'),
    # Building with AI
    ('read-b1', 'context-window', 'The context window is the one thing you control'),
    ('read-b2', 'cost', 'Cost per task'),
    ('read-b3', 'pen-nib', 'A brief survives when someone with no context can act on it'),
    ('read-b4', 'stack', 'The layers in claude.ai, and what belongs in each'),
    ('read-b5', 'clock', 'Scheduled tasks: what they can and cannot touch'),
    ('read-b6', 'magnifier', 'Ask, search or deep research'),
    ('read-b7', 'picture', 'Thumbnail copy in the'),
    ('read-b8', 'battery', 'What burns usage for no gain'),
    ('read-dd-b1', 'terminal', 'Claude Code and subagents in practice'),
    ('read-dd-b2', 'chat', "The evidence is this Project's own chat history"),
    # Information architecture
    ('read-ia1', 'books', 'The second line is library science'),
    ('read-ia2', 'map', 'adds the lines between them, each with a verb and a count'),
    ('read-ia3', 'magnifier', 'Search versus browse'),
    ('read-ia4', 'tree', 'a tree, a set of independent facets'),
    ('read-ia5', 'sitemap', 'the content inventory, the sitemap and the page-template catalogue'),
    ('read-ia6', 'bell', 'Refusing notifications loses nothing that cannot be found'),
    ('read-ia7', 'key', 'Roles and permissions as an IA layer'),
]


# neighbours that share an outline because the second text allows no other (the row's "where the text allows another")
NEIGHBOURS_OK = {
}


def pages():
    """Every reading page: panel id -> (course, its file, its code), from the vault as Academy reads it."""
    out = {}
    for c, files in L.TEXTS.items():
        for f in files:
            if f.parent.name == 'greece' or f.parent.name == 'rome':
                code = f.name.split('-')[0]
                out[('m' if c == 'greece' else 'rm') + code.replace('.', '')] = (c, f, code)
            elif f.parent.parent.name == 'courses':
                code = re.match(r'(DD-[AB]\d|[A-Z]+\d+)', f.name).group(1)
                out['read-' + code.lower()] = (c, f, code)
            else:                                   # generator/data/brand-ai/audience-growth-across-platforms.md
                out['read-audience-growth'] = (c, f, 'research')
    return out


def sentence(t, words):
    for s in re.split(r'(?<=[.!?])\s+|\n+', t):
        if words in s:
            return re.sub(r'^[#\s|-]+|[\s|]+$', '', s.replace('*', '')).strip()
    return None


def main():
    lib = {o['id']: o for o in json.loads((LIB / 'outlines.json').read_text())['outlines']}
    P = pages()
    bad, rows, uses = [], [], {}
    for pid, oid, words in MAP:
        if pid in uses: bad.append(f'{pid}: two reliefs')
        if pid not in P: bad.append(f'{pid}: no such reading page'); continue
        c, f, code = P[pid]
        o = lib.get(oid)
        if not o: bad.append(f'{pid}: {oid} is not in the library'); continue
        if c not in o['courses']: bad.append(f'{pid}: {oid} does not serve {c}')
        t = L.prose(f, oid)
        s = sentence(L.prose(f, ''), words)
        if not s: bad.append(f'{pid}: "{words}" is not in its prose')
        n = len(re.findall(r'\b(?:' + '|'.join(re.escape(k) for k in o['keywords']) + r')\b', t, re.I))
        if not n: bad.append(f'{pid}: its text names {oid} by none of its keywords')
        uses[pid] = oid
        rows.append((c, pid, code, oid, n, s))
    # neighbours: two reports of one unit, next to each other, with one outline
    def unit_key(pid):
        c, f, code = P[pid]
        if c in ('greece', 'rome'):
            u, m = code.split('.')
            return (c, int(u)), int(m)
        return None, None
    for pid, oid in uses.items():
        k, m = unit_key(pid)
        if k is None: continue
        for p2, o2 in uses.items():
            k2, m2 = unit_key(p2)
            if k2 == k and m2 == m + 1 and o2 == oid and (pid, p2) not in NEIGHBOURS_OK: bad.append(f'{pid} and {p2}: neighbours with one outline ({oid})')
    per = {c: sorted({oid for pid, oid in uses.items() if P[pid][0] == c}) for c in NAMES}
    npages = {c: sum(1 for v in P.values() if v[0] == c and v[2] != 'research') for c in NAMES}
    for c, ids in per.items():
        if len(ids) < min(10, npages[c]): bad.append(f'{NAMES[c]}: {len(ids)} outlines in use, fewer than ten')
    used = set(uses.values())
    for oid, o in lib.items():
        if oid not in used and not o.get('spare'): bad.append(f'{oid}: neither in use nor marked spare')
        if oid in used and o.get('spare'): bad.append(f'{oid}: in use and marked spare')
    if bad:
        print('\n'.join(bad)); sys.exit(1)
    (LIB / 'uses.json').write_text(json.dumps(dict(
        about='P95: each reading page that shows an object relief, by its panel id (a history report m43, rm14; a markdown unit '
              'read-a5), and the outline it shows (outlines.json). P95 mapped three pilot pages; P96 (8 Nov 2026) rolled the reliefs '
              'out to every report and unit whose text discusses an object at length, written by kit/p96_uses.py, which records '
              'each page\'s deciding sentence in uses-why.md. A unit filed later is mapped here when it is filed (skills/file-unit), or recorded as none.',
        uses=uses), indent=1, ensure_ascii=False) + '\n')
    # the pages with none: the outline their text names most (outlines.json's counts), and how often
    named = {}
    for o in lib.values():
        for c, lst in o['texts'].items():
            for f, n in lst:
                named.setdefault(f, []).append((n, o['id']))
    out = ['# Which page shows which relief, and why', '',
           'Written by `kit/p96_uses.py` (P96, 8 Nov 2026) from its `MAP`; `uses.json` is written with it. For each reading page given a relief, '
           'the outline and the sentence of the page\'s own text that decided it: the text discusses that object at length, not in passing '
           '("names" is how often the page\'s prose names the outline by its keywords). A page with none discusses no object at length; '
           'the outline its text names most is given with its count. A unit filed after P96 is added here by its filing (`skills/file-unit`).', '']
    for c in NAMES:
        mine = [r for r in rows if r[0] == c]
        nonep = sorted([(v[2], pid) for pid, v in P.items() if v[0] == c and pid not in uses],
                       key=lambda x: [int(p) if p.isdigit() else p for p in re.split(r'[.\-]', x[0])])
        out += [f'## {NAMES[c]}', '',
                f'{len(mine)} pages with a relief, {len(per[c])} outlines in use ({", ".join(per[c])}); {len(nonep)} page{"" if len(nonep) == 1 else "s"} with none.', '',
                '| Page | Outline | Names | Deciding sentence |', '|---|---|---|---|']
        key = lambda r: [int(p) if p.isdigit() else p for p in re.split(r'[.\-]', r[2])]
        for _, pid, code, oid, n, s in sorted(mine, key=key):
            out.append(f'| {code} (`{pid}`) | {oid} | {n} | {s.replace("|", "/")} |')
        out += ['', '**None:** ' + ('every page has one' if not nonep else '; '.join(
            f'{code} (`{pid}`)' + (lambda m: f', {m[1]} {m[0]}' if m else ', no outline named')(max(named.get(P[pid][1].relative_to(ROOT).as_posix(), []), default=None))
            for code, pid in nonep)) + '.', '']
        out += [f'**Shared by neighbours:** {a} and {b}: {why}.' for (a, b), why in NEIGHBOURS_OK.items() if P[a][0] == c] + ['']
    spare = [(oid, o['spare']) for oid, o in lib.items() if o.get('spare')]
    out += ['## Spare outlines', '', 'In the library and on no page yet, kept for the texts that name them (`spare` in `outlines.json`):', '']
    out += [f'- **{oid}**: {why}' for oid, why in spare] + ['']
    (LIB / 'uses-why.md').write_text('\n'.join(out))
    tot = sum(len(v) for v in per.values())
    print(f'{len(uses)} pages with a relief, {len(P) - len(uses)} with none; outlines in use per course '
          + ', '.join(f'{NAMES[c]} {len(v)}' for c, v in per.items()) + f'; {len(used)} of {len(lib)} outlines in use, {len(spare)} spare')


if __name__ == '__main__':
    main()
