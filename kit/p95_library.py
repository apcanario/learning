"""P95 (8 Nov 2026) · the outline library: design/outlines/<id>.svg and design/outlines/outlines.json, made by script from
open icon sets cloned from GitHub (a clone with --depth 1 --filter=blob:none --no-checkout, then only these files read
with git show), never typed or drawn: the only change to a file is the background square a set adds, removed here.

Each outline is taken because a course's texts discuss the object: for each course it serves, every file of that course
whose text names it (its keywords, whole words, any case) is recorded with its count in outlines.json, and an outline
no text of a course names does not serve that course. The busy ones (relief.py's measures: a part thinner than 3% of
its width, more than 40 separate regions) and the ones whose drawing is not what the texts call the object are listed
under "rejected" with the reason.

    python3 p95_library.py <folder holding the four clones>    writes the SVGs and outlines.json (then run relief.py)
"""
import json, pathlib, re, subprocess, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
LIB = ROOT / 'design' / 'outlines'
V = ROOT / 'courses'
TEXTS = {   # where each course's texts are (the files Academy reads its reading pages from)
    'greece': sorted((V / 'greece').glob('*.md')),
    'rome': sorted((V / 'rome').glob('*.md')),
    'brand-a': sorted((V / 'brand-ai').glob('A*.md')) + sorted((V / 'brand-ai').glob('DD-A*.md'))
               + [ROOT / 'generator/data/brand-ai/audience-growth-across-platforms.md'],
    'brand-b': sorted((V / 'brand-ai').glob('B*.md')) + sorted((V / 'brand-ai').glob('DD-B*.md')),
    'ux-ia': sorted((V / 'ux').glob('*.md')),
}
SETS = {
    'game-icons': dict(repo='game-icons/icons', clone='game-icons_icons', licence='CC BY 3.0', site='game-icons.net',
                       bg=re.compile(r'<path d="M0 0h512v512H0z"/>')),
    'phosphor': dict(repo='phosphor-icons/core', clone='phosphor-icons_core', licence='MIT', author='Phosphor Icons', site='phosphoricons.com',
                     bg=re.compile(r'<rect width="256" height="256" fill="none"\s*/>')),
    'tabler': dict(repo='tabler/tabler-icons', clone='tabler_tabler-icons', licence='MIT', author='Paweł Kuna', site='Tabler Icons',
                   bg=re.compile(r'<path stroke="none" d="M0 0h24v24H0z" fill="none"\s*/>')),
}
ALLOWED = ['CC BY 3.0', 'CC0 1.0', 'MIT', 'ISC']

# id, set, path in its repository, what it depicts (with its article, as the caption starts), the courses it serves, its keywords
L = [
    ('amphora', 'game-icons', 'delapouite/amphora.svg', 'an amphora', ['greece', 'rome'], ['amphora', 'amphorae', 'amphoras']),
    ('temple', 'game-icons', 'delapouite/greek-temple.svg', 'a classical temple front', ['greece', 'rome'], ['temple', 'temples']),
    ('ionic-column', 'game-icons', 'delapouite/ionic-column.svg', 'an Ionic column', ['greece'], ['Ionic', 'column', 'columns']),
    ('trireme', 'game-icons', 'delapouite/trireme.svg', 'an oared warship under sail', ['greece', 'rome'], ['trireme', 'triremes', 'quinquereme', 'quinqueremes', 'warship', 'warships', 'galley', 'galleys']),
    ('lyre', 'game-icons', 'lorc/lyre.svg', 'a lyre', ['greece'], ['lyre', 'lyres']),
    ('owl', 'game-icons', 'lorc/owl.svg', 'an owl', ['greece'], ['owl', 'owls']),
    ('olive', 'game-icons', 'delapouite/olive.svg', 'an olive branch', ['greece'], ['olive', 'olives']),
    ('laurels', 'game-icons', 'lorc/laurels.svg', 'a laurel wreath', ['greece', 'rome'], ['laurel', 'laurels', 'wreath', 'wreaths']),
    ('theatre-masks', 'game-icons', 'lorc/drama-masks.svg', 'two theatre masks', ['greece'], ['mask', 'masks']),
    ('wooden-horse', 'game-icons', 'delapouite/trojan-horse.svg', 'the wooden horse', ['greece'], ['wooden horse', 'Trojan horse']),
    ('centaur', 'game-icons', 'delapouite/centaur.svg', 'a centaur', ['greece'], ['centaur', 'centaurs']),
    ('minotaur', 'game-icons', 'lorc/minotaur.svg', 'the Minotaur', ['greece'], ['Minotaur']),
    ('labyrinth', 'game-icons', 'lorc/maze.svg', 'a labyrinth', ['greece'], ['labyrinth', 'labyrinths', 'maze']),
    ('centurion-helmet', 'game-icons', 'delapouite/centurion-helmet.svg', "a centurion's crested helmet", ['rome'], ['centurion', 'centurions', 'helmet', 'helmets']),
    ('gladius', 'game-icons', 'skoll/gladius.svg', 'a short sword, the gladius', ['rome'], ['gladius', 'sword', 'swords']),
    ('toga', 'game-icons', 'delapouite/roman-toga.svg', 'a figure in a toga', ['rome'], ['toga', 'togas']),
    ('eagle', 'game-icons', 'lorc/eagle-emblem.svg', 'an eagle with spread wings', ['rome'], ['eagle', 'eagles', 'aquila']),
    ('wolf', 'game-icons', 'lorc/wolf-head.svg', "a wolf's head", ['rome'], ['wolf', 'she-wolf', 'wolves']),
    ('bridge', 'game-icons', 'delapouite/stone-bridge.svg', 'an arched stone bridge', ['rome'], ['bridge', 'bridges']),
    ('wax-tablet', 'game-icons', 'delapouite/wax-tablet.svg', 'a writing tablet', ['rome'], ['tablet', 'tablets']),
    ('columns', 'game-icons', 'delapouite/ancient-columns.svg', 'three broken columns', ['rome'], ['column', 'columns']),
    ('torch', 'game-icons', 'delapouite/torch.svg', 'a burning torch', ['rome'], ['torch', 'torches']),
    ('gi', 'game-icons', 'delapouite/kimono.svg', 'a karate gi, its jacket belted', ['brand-a'], ['gi', 'gis', 'kimono', 'dogi']),
    ('black-belt', 'game-icons', 'delapouite/black-belt.svg', 'a tied belt', ['brand-a'], ['belt', 'belts', 'black belt']),
    ('camera', 'phosphor', 'assets/fill/camera-fill.svg', 'a camera', ['brand-a'], ['camera', 'cameras']),
    ('video-camera', 'phosphor', 'assets/fill/video-camera-fill.svg', 'a video camera', ['brand-a'], ['video camera', 'camera', 'cameras']),
    ('microphone', 'phosphor', 'assets/fill/microphone-fill.svg', 'a microphone', ['brand-a'], ['microphone', 'microphones', 'mic', 'mics', 'lav', 'lavalier']),
    ('phone', 'phosphor', 'assets/fill/device-mobile-fill.svg', 'a phone', ['brand-a', 'ux-ia'], ['phone', 'phones', 'smartphone', 'smartphones', 'iPhone']),
    ('calendar', 'phosphor', 'assets/fill/calendar-blank-fill.svg', 'a calendar', ['brand-a', 'brand-b'], ['calendar', 'calendars']),
    ('tag', 'phosphor', 'assets/fill/tag-fill.svg', 'a tag', ['ux-ia'], ['tag', 'tags', 'label', 'labels']),
    ('bar-chart', 'phosphor', 'assets/fill/chart-bar-fill.svg', 'a bar chart', ['brand-a'], ['chart', 'charts', 'bar chart']),
    ('receipt', 'phosphor', 'assets/fill/receipt-fill.svg', 'a receipt', ['brand-a', 'ux-ia'], ['receipt', 'receipts', 'invoice', 'invoices']),
    ('envelope', 'phosphor', 'assets/fill/envelope-simple-fill.svg', 'an envelope, the sign for email', ['brand-a', 'brand-b', 'ux-ia'], ['email', 'emails', 'envelope']),
    ('folder', 'phosphor', 'assets/fill/folder-fill.svg', 'a folder', ['brand-a', 'brand-b'], ['folder', 'folders']),
    ('terminal', 'phosphor', 'assets/fill/terminal-window-fill.svg', 'a terminal window', ['brand-b'], ['terminal', 'terminals']),
    ('brain', 'phosphor', 'assets/fill/brain-fill.svg', 'a brain', ['brand-b'], ['brain', 'brains']),
    ('servers', 'phosphor', 'assets/fill/hard-drives-fill.svg', 'two stacked servers', ['brand-b'], ['server', 'servers']),
    ('flask', 'phosphor', 'assets/fill/flask-fill.svg', 'a laboratory flask', ['brand-b'], ['flask', 'lab', 'labs']),
    ('clock', 'phosphor', 'assets/fill/clock-fill.svg', 'a clock', ['brand-b'], ['clock', 'clocks']),
    ('robot', 'phosphor', 'assets/fill/robot-fill.svg', "a robot's head", ['brand-b'], ['robot', 'robots']),
    ('book', 'phosphor', 'assets/fill/book-open-fill.svg', 'an open book', ['brand-b'], ['book', 'books']),
    ('checklist', 'phosphor', 'assets/fill/list-checks-fill.svg', 'a checklist', ['brand-b', 'ux-ia'], ['checklist', 'checklists']),
    ('database', 'phosphor', 'assets/fill/database-fill.svg', 'a database', ['brand-b'], ['database', 'databases']),
    ('laptop', 'phosphor', 'assets/fill/laptop-fill.svg', 'a laptop', ['brand-b'], ['laptop', 'laptops', 'computer', 'computers']),
    ('map', 'phosphor', 'assets/fill/map-trifold-fill.svg', 'a folded map', ['ux-ia'], ['map', 'maps']),
    ('sitemap', 'tabler', 'icons/filled/sitemap.svg', 'a sitemap', ['ux-ia'], ['sitemap', 'sitemaps']),
    ('tree', 'phosphor', 'assets/fill/tree-structure-fill.svg', 'a tree diagram', ['ux-ia'], ['tree', 'trees', 'hierarchy', 'hierarchies']),
    ('books', 'phosphor', 'assets/fill/books-fill.svg', 'books on a shelf', ['ux-ia'], ['book', 'books', 'library', 'libraries', 'librarian', 'librarians']),
    ('bicycle', 'phosphor', 'assets/fill/bicycle-fill.svg', 'a bicycle', ['ux-ia'], ['bike', 'bikes', 'bicycle', 'bicycles', 'cycling']),
    ('barbell', 'phosphor', 'assets/fill/barbell-fill.svg', 'a barbell', ['ux-ia'], ['gym', 'gyms', 'barbell']),
    ('fork-knife', 'phosphor', 'assets/fill/fork-knife-fill.svg', 'a fork and a knife', ['ux-ia'], ['meal', 'meals', 'lunch']),
    ('credit-card', 'phosphor', 'assets/fill/credit-card-fill.svg', 'a payment card', ['ux-ia'], ['credit card', 'credit cards', 'payment card', 'card payment']),
    ('bell', 'phosphor', 'assets/fill/bell-fill.svg', 'a bell, the sign for notifications', ['ux-ia'], ['notification', 'notifications', 'bell']),
    ('magnifier', 'phosphor', 'assets/fill/magnifying-glass-fill.svg', 'a magnifying glass, the sign for search', ['ux-ia'], ['search', 'magnifying glass']),
]
# taken from the sets and measured, then not used: busy (relief.py's measures) or not the object the texts name
REJECTED = [
    ('game-icons', 'delapouite/aqueduct.svg', 'busy: 2 thin parts (under 3% of its width, running 8% of it or more)'),
    ('game-icons', 'delapouite/roman-shield.svg', 'busy: 8 thin parts'),
    ('game-icons', 'delapouite/coins.svg', 'busy: 45 separate regions'),
    ('game-icons', 'lorc/sundial.svg', 'busy: 4 thin parts'),
    ('game-icons', 'delapouite/ancient-ruins.svg', 'busy: 17 regions and 6 thin parts'),
    ('game-icons', 'delapouite/spartan-helmet.svg', 'busy: 1 thin part'),
    ('game-icons', 'delapouite/greek-sphinx.svg', 'busy: 1 thin part'),
    ('game-icons', 'cathelineau/chariot.svg', 'busy: 1 thin part'),
    ('game-icons', 'caro-asercion/barn-owl.svg', 'busy: 2 thin parts; lorc/owl.svg taken instead'),
    ('game-icons', 'delapouite/column-vase.svg', 'not the object: a vase standing on an Ionic capital, not a krater as the texts describe one'),
    ('game-icons', 'delapouite/galley.svg', 'not the object: its masts and yards read as a later ship, not an ancient galley; the trireme serves Rome too'),
    ('game-icons', 'delapouite/arch-bridge.svg', 'not the object: a modern arch with a hung deck, not a Roman stone bridge'),
    ('game-icons', 'lorc/laurel-crown.svg', 'not the object: a crown inside the wreath; lorc/laurels.svg taken instead'),
]


def credit(s, author):
    if s == 'game-icons':
        return f'Icon: {author}, game-icons.net, CC BY 3.0'
    return f'Icon: {SETS[s]["author"]}, {SETS[s]["site"]}, {SETS[s]["licence"]}'


def hits(course, kws):
    rx = re.compile(r'\b(?:' + '|'.join(re.escape(k) for k in kws) + r')\b', re.I)
    out = []
    for f in TEXTS[course]:
        n = len(rx.findall(f.read_text(encoding='utf-8')))
        if n:
            out.append([f.relative_to(ROOT).as_posix(), n])
    return sorted(out, key=lambda x: -x[1])


def main():
    src = pathlib.Path(sys.argv[1])
    LIB.mkdir(parents=True, exist_ok=True)
    commits = {k: subprocess.run(['git', '-C', str(src / v['clone']), 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip() for k, v in SETS.items()}
    out = []
    for oid, s, path, what, courses, kws in L:
        st = SETS[s]
        raw = subprocess.run(['git', '-C', str(src / st['clone']), 'show', f'HEAD:{path}'], capture_output=True, text=True, check=True).stdout
        svg, n = st['bg'].subn('', raw)
        author = path.split('/')[0].replace('-', ' ').title() if s == 'game-icons' else st['author']
        (LIB / f'{oid}.svg').write_text(svg, encoding='utf-8')
        texts = {c: hits(c, kws) for c in courses}
        for c, t in texts.items():
            assert t, f'{oid}: no text of {c} names it'
        out.append(dict(id=oid, file=f'{oid}.svg', depicts=what, courses=courses, keywords=kws,
                        source=dict(repository=st['repo'], path=path, commit=commits[s], url=f'https://github.com/{st["repo"]}/blob/{commits[s]}/{path}'),
                        author=author, licence=st['licence'], credit=credit(s, author), background_removed=bool(n), texts=texts))
    rej = [dict(source=dict(repository=SETS[s]['repo'], path=p, commit=commits[s]), reason=why) for s, p, why in REJECTED]
    lib = dict(about='P95 (8 Nov 2026): the outline library. Each outline is a file from an open icon set on GitHub, taken '
                     'unchanged but for the background square a set adds (removed by kit/p95_library.py), because a course\'s texts '
                     'discuss the object: "texts" lists, for each course it serves, every file whose text names it (its keywords) '
                     'with the count. kit/relief.py turns each into <id>.json, which viz.py\'s kind "relief" draws. A caption prints '
                     '"<depicts>, a stylised outline. <credit>."; verify.py checks the credit is printed exactly.',
               allowed_licences=ALLOWED, outlines=out, rejected=rej)
    (LIB / 'outlines.json').write_text(json.dumps(lib, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    per = {c: sum(1 for o in out if c in o['courses']) for c in TEXTS}
    print(f'{len(out)} outlines, {len(rej)} rejected; per course {per}')


if __name__ == '__main__':
    main()
