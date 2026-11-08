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
    'game-icons': dict(repo='game-icons/icons', clone='game-icons_icons', licence='CC BY 3.0', site='game-icons.net', licence_file='license.txt',
                       bg=re.compile(r'<path d="M0 0h512v512H0z"/>')),
    'phosphor': dict(repo='phosphor-icons/core', clone='phosphor-icons_core', licence='MIT', author='Phosphor Icons', site='phosphoricons.com', licence_file='LICENSE',
                     bg=re.compile(r'<rect width="256" height="256" fill="none"\s*/>')),
    'tabler': dict(repo='tabler/tabler-icons', clone='tabler_tabler-icons', licence='MIT', author='Paweł Kuna', site='Tabler Icons', licence_file='LICENSE',
                   bg=re.compile(r'<path stroke="none" d="M0 0h24v24H0z" fill="none"\s*/>')),
}
ALLOWED = ['CC BY 3.0', 'CC0 1.0', 'MIT', 'ISC']

# id, set, path in its repository, what it depicts (with its article, as the caption starts), the courses it serves, its keywords
L = [
    ('amphora', 'game-icons', 'delapouite/amphora.svg', 'an amphora', ['greece', 'rome'], ['amphora', 'amphorae', 'amphoras']),
    ('temple', 'game-icons', 'delapouite/greek-temple.svg', 'a classical temple front', ['greece', 'rome'], ['temple', 'temples']),
    ('ionic-column', 'game-icons', 'delapouite/ionic-column.svg', 'an Ionic column', ['greece'], ['Ionic column', 'Ionic columns', 'Ionic capital', 'Ionic capitals', 'Ionic order', 'Ionic temple', 'Ionic temples']),
    ('trireme', 'game-icons', 'delapouite/trireme.svg', 'an oared warship under sail', ['greece', 'rome'], ['trireme', 'triremes', 'quinquereme', 'quinqueremes', 'warship', 'warships', 'galley', 'galleys']),
    ('lyre', 'game-icons', 'lorc/lyre.svg', 'a lyre', ['greece'], ['lyre', 'lyres']),
    ('owl', 'game-icons', 'lorc/owl.svg', 'an owl', ['greece'], ['owl', 'owls']),
    ('olive', 'game-icons', 'delapouite/olive.svg', 'olive (a branch)', ['greece'], ['olive', 'olives']),
    ('laurels', 'game-icons', 'lorc/laurels.svg', 'laurel (a wreath)', ['greece', 'rome'], ['laurel', 'laurels']),
    ('theatre-masks', 'game-icons', 'lorc/drama-masks.svg', 'two theatre masks', ['greece'], ['mask', 'masks']),
    ('wooden-horse', 'game-icons', 'delapouite/trojan-horse.svg', 'the wooden horse', ['greece', 'rome'], ['wooden horse', 'Trojan horse']),
    ('centaur', 'game-icons', 'delapouite/centaur.svg', 'a centaur', ['greece'], ['centaur', 'centaurs']),
    ('minotaur', 'game-icons', 'lorc/minotaur.svg', 'the Minotaur', ['greece'], ['Minotaur']),
    ('centurion-helmet', 'game-icons', 'delapouite/centurion-helmet.svg', 'a crested helmet', ['rome'], ['helmet', 'helmets']),
    ('gladius', 'game-icons', 'skoll/gladius.svg', 'a short sword', ['rome'], ['gladius', 'sword', 'swords']),
    ('toga', 'game-icons', 'delapouite/roman-toga.svg', 'a figure in a toga', ['rome'], ['toga', 'togas']),
    ('eagle', 'game-icons', 'lorc/eagle-emblem.svg', 'an eagle with spread wings', ['greece', 'rome'], ['eagle', 'eagles', 'aquila']),
    ('wolf', 'game-icons', 'lorc/wolf-head.svg', "a wolf's head", ['rome'], ['wolf', 'she-wolf', 'wolves']),
    ('bridge', 'game-icons', 'delapouite/stone-bridge.svg', 'an arched stone bridge', ['rome'], ['bridge', 'bridges']),
    ('torch', 'game-icons', 'delapouite/torch.svg', 'a burning torch', ['rome'], ['torch', 'torches']),
    ('gi', 'game-icons', 'delapouite/kimono.svg', 'a karate gi with its jacket belted', ['brand-a'], ['gi', 'gis', 'kimono', 'dogi', 'karate apparel']),
    ('video-camera', 'phosphor', 'assets/fill/video-camera-fill.svg', 'a video camera (the sign for filming)', ['brand-a'], ['video camera', 'camera', 'cameras']),
    ('picture', 'phosphor', 'assets/fill/image-fill.svg', 'a picture (the sign for a thumbnail)', ['brand-a', 'brand-b'], ['thumbnail', 'thumbnails']),
    ('money', 'phosphor', 'assets/fill/money-fill.svg', 'a banknote (the sign for money)', ['brand-a'], ['money', 'monetisation', 'revenue']),
    ('microphone', 'phosphor', 'assets/fill/microphone-fill.svg', 'a microphone', ['brand-a'], ['microphone', 'microphones', 'mic', 'mics']),
    ('phone', 'phosphor', 'assets/fill/device-mobile-fill.svg', 'a phone', ['brand-a', 'ux-ia'], ['phone', 'phones', 'smartphone', 'smartphones', 'iPhone']),
    ('calendar', 'phosphor', 'assets/fill/calendar-blank-fill.svg', 'a calendar', ['brand-a', 'brand-b'], ['calendar', 'calendars']),
    ('tag', 'phosphor', 'assets/fill/tag-fill.svg', 'a tag (the sign for labels)', ['ux-ia'], ['tag', 'tags', 'label', 'labels']),
    ('receipt', 'phosphor', 'assets/fill/receipt-fill.svg', 'a receipt', ['brand-a', 'ux-ia'], ['receipt', 'receipts', 'invoice', 'invoices']),
    ('envelope', 'phosphor', 'assets/fill/envelope-simple-fill.svg', 'an envelope (the sign for email)', ['brand-a', 'brand-b', 'ux-ia'], ['email', 'emails', 'envelope']),
    ('folder', 'phosphor', 'assets/fill/folder-fill.svg', 'a folder', ['brand-a', 'brand-b'], ['folder', 'folders']),
    ('terminal', 'phosphor', 'assets/fill/terminal-window-fill.svg', 'a terminal window (the sign for Claude Code)', ['brand-b'], ['terminal', 'terminals', 'Claude Code']),
    ('plug', 'phosphor', 'assets/fill/plug-fill.svg', 'a plug (the sign for a plugin)', ['brand-b'], ['plugin', 'plugins']),
    ('servers', 'phosphor', 'assets/fill/hard-drives-fill.svg', 'two stacked servers', ['brand-b'], ['server', 'servers']),
    ('clock', 'phosphor', 'assets/fill/clock-fill.svg', 'a clock (the sign for scheduled tasks)', ['brand-b'], ['clock', 'clocks', 'scheduled task', 'scheduled tasks']),
    ('book', 'phosphor', 'assets/fill/book-open-fill.svg', 'an open book', ['brand-b'], ['book', 'books']),
    ('checklist', 'phosphor', 'assets/fill/list-checks-fill.svg', 'a checklist', ['brand-b', 'ux-ia'], ['checklist', 'checklists']),
    ('database', 'phosphor', 'assets/fill/database-fill.svg', 'a database', ['brand-b'], ['database', 'databases']),
    ('laptop', 'phosphor', 'assets/fill/laptop-fill.svg', 'a laptop', ['brand-b'], ['laptop', 'laptops', 'computer', 'computers']),
    ('map', 'phosphor', 'assets/fill/map-trifold-fill.svg', "a folded map (the sign for the course's maps)", ['ux-ia'], ['map', 'maps']),
    ('sitemap', 'tabler', 'icons/filled/sitemap.svg', 'a sitemap', ['ux-ia'], ['sitemap', 'sitemaps']),
    ('tree', 'phosphor', 'assets/fill/tree-structure-fill.svg', 'a tree diagram', ['ux-ia'], ['tree', 'trees', 'hierarchy', 'hierarchies']),
    ('books', 'phosphor', 'assets/fill/books-fill.svg', 'books on a shelf', ['ux-ia'], ['book', 'books', 'library', 'libraries', 'librarian', 'librarians']),
    ('bicycle', 'phosphor', 'assets/fill/bicycle-fill.svg', 'a bicycle', ['ux-ia'], ['bike', 'bikes', 'bicycle', 'bicycles', 'cycling']),
    ('barbell', 'phosphor', 'assets/fill/barbell-fill.svg', 'a barbell (the sign for a gym)', ['ux-ia'], ['gym', 'gyms', 'barbell']),
    ('fork-knife', 'phosphor', 'assets/fill/fork-knife-fill.svg', 'a fork and a knife (the sign for meals)', ['ux-ia'], ['meal', 'meals', 'lunch']),
    ('credit-card', 'phosphor', 'assets/fill/credit-card-fill.svg', 'a payment card', ['ux-ia'], ['Perqo card', 'credit card', 'credit cards', 'payment card', 'payment cards']),
    ('bell', 'phosphor', 'assets/fill/bell-fill.svg', 'a bell (the sign for notifications)', ['ux-ia'], ['notification', 'notifications', 'bell']),
    ('magnifier', 'phosphor', 'assets/fill/magnifying-glass-fill.svg', 'a magnifying glass (the sign for search)', ['brand-b', 'ux-ia'], ['search', 'magnifying glass']),
    # P96 (8 Nov 2026): the outlines the roll-out's texts call for and the library lacked, each for the page whose
    # deciding sentence is in design/outlines/uses-why.md; measured by relief.py --probe before they were taken
    ('greek-helmet', 'game-icons', 'lorc/crested-helmet.svg', 'a crested Greek helmet', ['greece'], ['helmet', 'helmets']),
    ('vase', 'game-icons', 'delapouite/painted-pottery.svg', 'a painted vase', ['greece', 'rome'], ['vase', 'vases', 'lekythos', 'lekythoi', 'krater', 'kraters']),
    ('ostrakon', 'game-icons', 'delapouite/broken-pottery.svg', 'a broken pot (the sign for the sherds of ostracism)', ['greece'], ['ostracism', 'ostracised', 'ostraka', 'ostrakon', 'sherd', 'sherds', 'potsherd', 'potsherds']),
    ('bull', 'game-icons', 'lorc/bull-horns.svg', "a bull's horns", ['greece', 'rome'], ['bull', 'bulls']),
    ('hydra', 'game-icons', 'lorc/hydra.svg', 'the Hydra', ['greece'], ['Hydra']),
    ('ram', 'game-icons', 'delapouite/ram-profile.svg', 'a ram', ['greece'], ['ram', 'fleece']),
    ('scroll', 'game-icons', 'lorc/scroll-unfurled.svg', 'a scroll', ['greece', 'rome'], ['scroll', 'scrolls', 'papyrus', 'papyri', 'book-roll', 'book-rolls']),
    ('tablet', 'game-icons', 'delapouite/wax-tablet.svg', 'an inscribed tablet', ['greece', 'rome'], ['tablet', 'tablets']),
    ('coins', 'game-icons', 'delapouite/two-coins.svg', 'two coins', ['greece', 'rome'], ['coin', 'coins', 'coinage', 'coinages']),
    ('horse', 'game-icons', 'lorc/horse-head.svg', "a horse's head", ['greece', 'rome'], ['horse', 'horses', 'cavalry']),
    ('wall', 'game-icons', 'delapouite/stone-wall.svg', 'a stone wall', ['greece', 'rome'], ['wall', 'walls']),
    ('winged-sandal', 'game-icons', 'lorc/wingfoot.svg', 'a winged sandal', ['greece'], ['winged sandals', 'sandals']),
    ('sun', 'game-icons', 'lorc/sun.svg', 'the sun', ['rome'], ['Sun', 'Sol', 'Helios']),
    ('scales', 'game-icons', 'lorc/scales.svg', 'a pair of scales (the sign for the law)', ['rome', 'brand-a'], ['law', 'laws']),
    ('bough', 'game-icons', 'lorc/tree-branch.svg', 'a leafy bough', ['rome'], ['bough', 'boughs']),
    ('dagger', 'game-icons', 'lorc/plain-dagger.svg', 'a dagger', ['rome'], ['dagger', 'daggers']),
    ('libation', 'game-icons', 'lorc/pouring-chalice.svg', 'a cup pouring out (the sign for a libation)', ['greece', 'rome'], ['libation', 'libations']),
    ('film-slate', 'phosphor', 'assets/fill/film-slate-fill.svg', 'a clapperboard (the sign for a video)', ['brand-a'], ['video', 'videos', 'vlog', 'vlogs', 'episode', 'episodes']),
    ('audience', 'phosphor', 'assets/fill/users-three-fill.svg', 'three people (the sign for an audience)', ['brand-a'], ['audience', 'audiences']),
    ('notebook', 'phosphor', 'assets/fill/notebook-fill.svg', 'a notebook (the sign for the record)', ['brand-a'], ['the record', 'a record']),
    ('chart', 'phosphor', 'assets/fill/trend-up-fill.svg', 'a rising trend line (the sign for growth benchmarks)', ['brand-a'], ['benchmark', 'benchmarks']),
    ('piggy-bank', 'phosphor', 'assets/fill/piggy-bank-fill.svg', 'a piggy bank (the sign for savings)', ['brand-a'], ['savings', 'runway']),
    ('context-window', 'phosphor', 'assets/fill/app-window-fill.svg', 'an app window (the sign for the context window)', ['brand-b'], ['context window', 'context windows']),
    ('cost', 'phosphor', 'assets/fill/coins-fill.svg', 'coins (the sign for cost)', ['brand-b'], ['cost', 'costs', 'price', 'prices', 'pricing']),
    ('chat', 'phosphor', 'assets/fill/chat-text-fill.svg', 'a speech bubble (the sign for a chat)', ['brand-b'], ['chat', 'chats']),
    ('stack', 'phosphor', 'assets/fill/stack-fill.svg', 'a stack of layers (the sign for the layers of context)', ['brand-b'], ['layer', 'layers']),
    ('battery', 'phosphor', 'assets/fill/battery-medium-fill.svg', 'a half-charged battery (the sign for usage limits)', ['brand-b'], ['limit', 'limits', 'usage']),
    ('pen-nib', 'phosphor', 'assets/fill/pen-nib-fill.svg', 'a pen nib (the sign for writing a brief)', ['brand-b'], ['brief', 'briefs']),
    ('key', 'phosphor', 'assets/fill/key-fill.svg', 'a key (the sign for permissions)', ['ux-ia'], ['permission', 'permissions']),
]
# P95 check A: what a keyword also matches that is not the object (a homonym, a title, another kind of the thing), taken
# out of each line before counting
EXCLUDE = {
    'theatre-masks': [r'death[- ]masks?', r'(?:gold(?:en)?|funeral|funerary|burial|wax|ancestral) masks?', r'Agamemnon', r'Schliemann', r'shaft graves', r'Grave \w+', r"mask's authenticity", r'mask dates', r'stylistically odd', r'Humbaba', r'grotesque masks?', r'mask on a pillar'],
    'terminal': [r'Terminal-Bench'],
    'eagle': [r'eagle-owls?'],
    'wolf': [r'Hieronymus Wolf'],
    'bridge': [r'bridge and barrier', r'bridge to the', r'bridge to Italy', r'bridge between', r'Rhine bridges?', r'bridges? (?:over|across) the Rhine', r'Pons Sublicius', r'Sublician bridge', r'bridge of boats', r'Boarding-Bridge'],
    'gladius': [r'fire and sword', r'fire, sword'],
    'receipt': [r'Receipts inside', r'net receipts', r'Tier receipts', r'trailing receipts', r'quarters of receipts', r'banked receipts', r'from receipt'],
    'map': [r'\bmaps? (?:to|onto|into|them)\b', r'does not map'],
    'books': [r'Two Waves Books'],
    'toga': [r'In toga candida'],
    'servers': [r'MCP servers?'],
    'database': [r'Cochrane Database'],
    'phone': [r'phone (?:fields?|numbers?|line|volume)', r'from a phone'],
    # P96
    'ram': [r'battering', r'\brams? (?:of|on) (?:a|the|her|their)\b', r'\bramm', r'bronze rams?'],
    'horse': [r'wooden horse', r'Trojan horse'],
    'wall': [r'walls? of (?:the )?(?:world|text)', r'without walls', r'wall of (?:text|silence)'],
    'scales': [r'\bin[- ]law\b', r'law of (?:signs|nature|averages)', r'Laws\b(?= of Plato| \()', r'\bOn the Laws\b'],
    'chat': [r'\bchat (?:with|about) (?:a|his) friend'],
}
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
    # P95 check A (first fresh check of the library), each taken at first and then removed:
    ('game-icons', 'lorc/maze.svg', 'busy: its walls a step of 1.4 px at 512 px, so its levels merge into solid bands (relief.py: a step under 3 px)'),
    ('game-icons', 'delapouite/ancient-columns.svg', 'busy: a step of 2.6 px at 512 px, its levels merge into solid bands'),
    ('game-icons', 'delapouite/black-belt.svg', 'busy (a step of 1.4 px, 512 lines) and not the object: the texts name only the magazine Black Belt'),
    ('phosphor', 'assets/fill/flask-fill.svg', 'not the object: "lab" names AI laboratories, never a flask'),
    ('phosphor', 'assets/fill/robot-fill.svg', 'not the object: "robots" is the robots.txt rule and a quoted metaphor'),
    ('phosphor', 'assets/fill/brain-fill.svg', 'not the object: "brain dump", "pick your brain", a skill\'s name; the organ only in passing'),
    ('phosphor', 'assets/fill/chart-bar-fill.svg', 'not the object: the texts name charts only in passing and in a source\'s title, never a bar chart (second check of the library)'),
    ('phosphor', 'assets/fill/camera-fill.svg', 'a second camera: the texts\' camera is the phone filming, kept as the video camera'),
    # P96: measured for a page of the roll-out and not taken
    ('game-icons', 'skoll/pegasus.svg', 'busy: 1 thin part (Greece 3.6 discusses Pegasus; it gets no relief)'),
    ('game-icons', 'cathelineau/medusa-head.svg', 'busy: 5 thin parts and a step of 2.5 px (Greece 3.1 takes the winged sandal instead)'),
    ('game-icons', 'caro-asercion/philosopher-bust.svg', 'busy: 2 thin parts; and the philosophy reports discuss no bust'),
    ('game-icons', 'delapouite/caduceus.svg', 'busy: 16 regions, 2 thin parts'),
    ('game-icons', 'delapouite/harp.svg', 'busy: 4 thin parts; and a harp, not the lyre the texts name'),
    ('game-icons', 'delapouite/papyrus.svg', 'busy: 14 thin parts, a step of 2.2 px (lorc/scroll-unfurled.svg taken for the scroll)'),
    ('game-icons', 'lorc/heavy-lightning.svg', 'busy: 3 thin parts'),
    ('game-icons', 'delapouite/sheep.svg', 'busy: 2 thin parts (delapouite/ram-profile.svg taken for the Golden Fleece)'),
    ('game-icons', 'delapouite/charging-bull.svg', 'busy: 4 thin parts (lorc/bull-horns.svg taken)'),
    ('game-icons', 'lorc/cyclops.svg', 'not the object: an eye in an oval reads as an eye, not the Cyclops of Greece 4.4 and 10.7'),
    ('game-icons', 'sbed/arena.svg', 'not the object: no amphitheatre a reader would recognise (Rome 9.4 gets none)'),
    ('game-icons', 'delapouite/lighthouse.svg', 'not the object: a modern lighthouse, not the Pharos of Greece 7.2'),
    ('game-icons', 'lorc/wine-glass.svg', 'not the object: a modern wine glass, not the krater or kylix of Greece 8.5'),
    ('game-icons', 'lorc/sacrificial-dagger.svg', 'busy: 2 thin parts (lorc/plain-dagger.svg taken for Rome 11.7)'),
    ('game-icons', 'lorc/bull.svg', 'not the object: as a silhouette only the horns, the eyes and a nose ring stand, no head (contact sheet); lorc/bull-horns.svg taken'),
    ('game-icons', 'lorc/stone-tablet.svg', 'not the object: its relief reads as a rock, not a tablet (contact sheet); delapouite/wax-tablet.svg taken'),
    ('phosphor', 'assets/fill/cow-fill.svg', 'not the object: a cartoon cow, not a bull'),
    ('phosphor', 'assets/fill/cards-fill.svg', 'not the object: its relief reads as nested rectangles, not cards (contact sheet); Building with AI DD-B3 gets none'),
    ('phosphor', 'assets/fill/cards-three-fill.svg', 'not the object: a box under two bars, not a card'),
    ('game-icons', 'lorc/broken-tablet.svg', 'not the object: its relief reads as a shattered polygon round a spiral, broken rock, not a tablet (P96 check H1); delapouite/wax-tablet.svg taken for the inscribed tablets of Greece 1.2 and 8.2'),
    ('game-icons', 'willdabeast/round-shield.svg', 'not the object: a planked wooden shield with rivets, not the worked bronze shields of Achilles (Greece 10.1) and Aeneas (Rome 12.7), nor the bronze-faced aspis of Greece 5.3; all three get none (P96 checks H1, H2)'),
    ('game-icons', 'delapouite/viking-shield.svg', 'busy (3 thin parts, a step of 2.6 px) and not the object: a Viking shield'),
    ('game-icons', 'skoll/tablet.svg', 'not the object: a tablet computer'),
    ('phosphor', 'assets/fill/chart-line-up-fill.svg', 'not the object as a relief: the filled frame with the line cut out reads as a maze in a box (P96 check M1); trend-up-fill.svg taken'),
    ('phosphor', 'assets/fill/gauge-fill.svg', 'not the object as a relief: a filled dome with the needle cut out reads as a maze, not a dial (P96 check M3); battery-medium-fill.svg taken'),
    ('phosphor', 'assets/fill/speedometer-fill.svg', 'not the object as a relief: the same dome with its needle cut out'),
    ('game-icons', 'delapouite/speedometer.svg', 'busy: 1 thin part'),
    ('phosphor', 'assets/fill/calculator-fill.svg', 'not the object: Brand DD-A2 names savings and a runway, never a calculator'),
]
# P96: outlines in the library that no reading page shows yet, kept for the texts that name them (verify.py: every
# outline is in use in design/outlines/uses.json or listed here)
SPARE = {
    'centurion-helmet': 'its Rome pages name a helmet in passing (P96 check H1: Rome 1.1, 9.2, 12.3); kept',
    'laurels': 'Greece 3.7 names the laurel tree, not a wreath (P96 check H1); kept',
    'toga': 'Rome 3.2 names the toga in one story among many (P96 check H1); kept',
    'amphora': 'Greece 4.3 names it most and shows the wooden horse; Rome 1.2 names the Tyrrhenian amphorae and shows the vase; kept for a later text',
    'ionic-column': 'two Greek texts name the order in passing; kept',
    'owl': 'named in passing in three Greek texts; kept',
    'torch': 'Rome 12.4 takes the short sword; kept',
    'bridge': 'Rome 8.3 names the Milvian Bridge twice, in passing; kept',
    'video-camera': 'Personal brand A5 takes the phone; kept',
    'microphone': 'Personal brand A5 takes the phone; kept',
    'gi': 'Personal brand A7 names the gi in passing and discusses money at length (P96 checks M1, M2); kept for a unit on the brand\'s products',
    'lyre': 'Greece 2.2 and 5.6 name the lyre in passing (P96 checks H1, H2); kept',
    'receipt': 'Personal brand A8 takes the scales; kept for Information architecture',
    'folder': 'named in passing; kept',
    'servers': 'named in passing; kept',
    'plug': 'Building with AI B5 takes the clock, its scheduled tasks discussed at length, where plugins are named in passing (P96 check M1); kept',
    'book': 'named in passing; kept',
    'checklist': 'kept for a deliverable that is a checklist',
    'database': 'named in passing; kept',
    'laptop': 'named in passing; kept',
    'tag': 'Information architecture: kept for the units on labelling still to come',
    'bicycle': 'Information architecture: kept for the Perqo units still to come',
    'barbell': 'Information architecture: kept for the Perqo units still to come',
    'fork-knife': 'Information architecture: kept for the Perqo units still to come',
    'credit-card': 'Information architecture: kept for the Perqo units still to come',
}


def credit(s, author):
    if s == 'game-icons':
        return f'Icon: {author}, game-icons.net, CC BY 3.0'
    return f'Icon: {SETS[s]["author"]}, {SETS[s]["site"]}, {SETS[s]["licence"]}'


FIG = re.compile(r'^```viz\n.*?\n```$|<figure\b.*?</figure>', re.S | re.M)


def prose(f, oid):
    """P95 check A: a text as prose: its figure declarations (```viz blocks, history figures) taken out, whose JSON keys
    ("label") and data are not the text naming an object, and each outline's EXCLUDE patterns taken out."""
    t = FIG.sub(' ', f.read_text(encoding='utf-8'))
    t = re.sub(r'\A---\n.*?\n---\n', ' ', t, flags=re.S)        # the front matter (search: off)
    t = re.sub(r'\]\([^)\s]*\)|https?://\S+|\b[\w.-]+\.(?:com|org|net|io|ai|dev|edu|gov|co)/\S*', ' ', t)   # link targets and URLs, bare ones too (a slug such as earn-money)
    t = re.sub(r'^##\s+Sources\b.*?(?=^## |\Z)', ' ', t, flags=re.S | re.M)   # P95 check A4: a unit's source list (its titles are not its prose)
    t = re.sub(r'(?<=\d)\.(?=\d)', '\x00', t)
    t = re.sub(r'\b(c|ca|no|vol|pp|p|cf|e\.g|i\.e)\.', lambda m: m.group(1).replace('.', '\x00') + '\x00', t, flags=re.I)   # a decimal point or an abbreviation's stop ends no sentence
    for x in EXCLUDE.get(oid, []):   # P95 check A3: the whole sentence that holds a homonym goes, not only its name
        t = re.sub(r'[^.\n]*(?:' + x + r')[^.\n]*', ' ', t, flags=re.I)
    t = t.replace('\x00', '.')
    return t


def hits(course, kws, oid=''):
    rx = re.compile(r'\b(?:' + '|'.join(re.escape(k) for k in kws) + r')\b', re.I)
    out = []
    for f in TEXTS[course]:
        n = len(rx.findall(prose(f, oid)))
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
        if s == 'game-icons':   # P96 check H4: an ancient outline serves every history course whose texts name it
            courses = courses + [c for c in ('greece', 'rome') if c not in courses and hits(c, kws, oid)]
        texts = {c: hits(c, kws, oid) for c in courses}
        for c, t in texts.items():
            assert t, f'{oid}: no text of {c} names it'
        out.append(dict(id=oid, file=f'{oid}.svg', depicts=what, courses=courses, keywords=kws,
                        source=dict(repository=st['repo'], path=path, commit=commits[s], url=f'https://github.com/{st["repo"]}/blob/{commits[s]}/{path}'),
                        author=author, licence=st['licence'], credit=credit(s, author), set=s,
                        licence_url='https://creativecommons.org/licenses/by/3.0/' if st['licence'] == 'CC BY 3.0' else f'https://github.com/{st["repo"]}/blob/{commits[s]}/{st["licence_file"]}', background_removed=bool(n), excludes=EXCLUDE.get(oid, []), texts=texts, **({'spare': SPARE[oid]} if oid in SPARE else {})))
    lic = LIB / 'licences'
    lic.mkdir(exist_ok=True)
    for k, st in SETS.items():   # each set's licence file as its repository holds it at the commit taken, for the credits page
        f = st['licence_file']
        txt = subprocess.run(['git', '-C', str(src / st['clone']), 'show', f'HEAD:{f}'], capture_output=True, text=True, check=True).stdout
        (lic / f'{k}.txt').write_text(txt, encoding='utf-8')
    rej = [dict(source=dict(repository=SETS[s]['repo'], path=p, commit=commits[s]), reason=why) for s, p, why in REJECTED]
    lib = dict(about='P95 (8 Nov 2026): the outline library. Each outline is a file from an open icon set on GitHub, taken '
                     'unchanged but for the background square a set adds (removed by kit/p95_library.py), because a course\'s texts '
                     'discuss the object: "texts" lists, for each course it serves, every file whose text names it (its keywords) '
                     'with the count. kit/relief.py turns each into <id>.json, which viz.py\'s kind "relief" draws. A caption prints '
                     '"<depicts>, a stylised outline drawn as a relief from an icon. <credit>.", the licence linked; verify.py checks it is printed exactly. A count is '
                     'of the prose: the front matter, a unit\'s Sources section, figure declarations, link targets and URLs are taken out first, and every sentence '
                     'that holds one of the outline\'s "excludes" (a homonym, a title, another kind of the thing). licences/ holds '
                     'each set\'s licence file at the commit taken.',
               allowed_licences=ALLOWED, outlines=out, rejected=rej)
    (LIB / 'outlines.json').write_text(json.dumps(lib, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    per = {c: sum(1 for o in out if c in o['courses']) for c in TEXTS}
    print(f'{len(out)} outlines, {len(rej)} rejected; per course {per}')


if __name__ == '__main__':
    main()
