"""Course data for build.py. Each live course is a dict; NEXT lists the courses still to come.

Every course has a `family`: 'history' (Greece, Rome and the eight to come: HTML fragments per module in the kit,
a syllabus with prompts, provenance.json) or 'markdown' (Brand + AI: units as Markdown in the vault, `vault`, read
directly since A5; the course data under generator/data/<slug>/, `data`). The root home is Academy and lists every
course of both families (docs/academy.md, A1). A markdown course is built by mdcourse.py from its data file into one
Academy course per course in that file (A3). A new course of either family is a folder plus an entry here (A5).

Text fields may use these placeholders, filled per course at build time:
{content_mods} modules excluding the audit unit · {total_mods} all modules · {nrep} reports written · {kwords} thousands of words written
"""

# Tracks: the Academy home and the root drawer group courses by subject. Every course names its track.
THEMES = [
    dict(id='history', name='History', color='var(--red)',
         lede='The history and mythology of one culture at a time, read together: who told each story, what they gained by it, and what the evidence says. Long sourced reports with disputes named, a self-test and a syllabus you can rerun.'),
    dict(id='marketing', name='Marketing', color='var(--teal)',
         lede='Building a personal brand from the record of what you actually do: audience, platform economics, cadence, benchmarks. Every unit sourced to platform data or peer-reviewed work and ending in a shipped deliverable.'),
    dict(id='technology', name='Technology', color='var(--purple)',
         lede='Working with AI models as tools: which model for which task, how to brief, how to keep a project from rotting, how to verify what the machine wrote before you trust it.'),
    dict(id='ux', name='User Experience', color='var(--blue)',
         lede='The practice of UX design, written to be handed to other designers: how to read, build and edit the structure behind a product at any scale, where that work sits in the product cycle and the business, and how to deliver it when the inputs are missing. Every unit sourced to the field\'s standard works and research, rich in figures, ending in a shipped deliverable.'),
]

GREECE = dict(
    id='greece', family='history', theme='history', num=1, short='Greece', label='GREECE', name='Greek history and mythology', color='var(--red)',
    syllabus='greek-syllabus.html', frags='greece', prompts='prompts-greece.json', prefix='m',
    home_id='greece', syl_id='syllabus', syl_anchor='s',
    unit_colors={'0': 'var(--gold)', '1': 'var(--orange)', '2': 'var(--purple)', '3': 'var(--red)', '4': 'var(--orange)', '5': 'var(--teal)', '6': 'var(--blue)', '7': 'var(--purple)', '8': 'var(--gold)', '9': 'var(--teal)', '10': 'var(--red)', '11': 'var(--blue)', '12': 'var(--gold)', '13': 'var(--teal)'},
    sections={'0': 'Core course', '10': 'Deep dives', '13': 'Quality'},
    audit_unit='13', default_model='Fable 5.1',
    parts=[
        ("I", "Ground rules", ["0", "1"], "c. 3000 to 800 BC", "Where the evidence comes from, how the land shaped everything, and the Bronze Age world that the myths half remember."),
        ("II", "The myths", ["2", "3", "4"], "set in the Bronze Age, told from c. 750 BC", "Gods, heroes and the war at Troy, read as a later Greece told them, with each story's sources and the city that gained from it."),
        ("III", "The history", ["5", "6", "7"], "800 BC to AD 529", "From the first poleis to the closing of the Academy: Sparta and Athens, Persia, the long war, Alexander, the kingdoms and Rome."),
        ("IV", "Practice and legacy", ["8", "9"], "across the whole span", "What Greeks did at altars and in houses, what they built and painted, and how all of it reached you. Ends with the capstone exam."),
        ("+", "Deep dives", ["10", "11", "12"], "optional", "The Trojan War, Alexander and Greek philosophy taken to the depth the survey could not reach. Best after the units they extend, or after the capstone."),
        ("✓", "Quality audit", ["13"], "run when ready", "A check on the course itself. The later reports were written with a different model; this unit audits them against a rubric drawn from the core course and fixes what falls short."),
    ],
    eras=[("Bronze Age", -3000, -1200, "var(--orange)", "unit 1, and the setting of the myths in units 2–4"),
          ("Dark Age", -1200, -800, "var(--dim)", "module 1.3"),
          ("Archaic", -800, -480, "var(--teal)", "unit 5"),
          ("Classical", -480, -323, "var(--blue)", "unit 6"),
          ("Hellenistic", -323, -31, "var(--purple)", "unit 7"),
          ("Roman", -31, 529, "var(--red)", "modules 7.3 and 7.4")],
    era_title='3,500 years, to scale', era_range='3000 BC → AD 529',
    era_aria='Timeline from 3000 BC to AD 529, to scale: the Bronze Age takes half; the Classical age is a thin slice.',
    ticks=[('3000 BC', '0'), ('1200 BC', f'{(1800/3529)*100:.1f}%'), ('AD 1', f'{(3000/3529)*100:.1f}%'), ('529', '100%')],
    era_note='The Classical age that most people mean by "ancient Greece" is the narrow blue slice: about 150 years. The myths are set in the long orange band and were written down in the teal one.',
    eyebrow='COURSE 1 · GREECE',
    h1='Greek history and mythology',
    lede='Four parts and three deep dives, {content_mods} modules, plus a quality audit. History and myth are interleaved on purpose: the myths only make sense once you know which society was telling them and why. Every module is a long-form report with named primary sources, the places where ancient accounts disagree, a ten-question self-test and three ideas to carry forward.',
    rules='''<li><strong>Parts I to IV in order.</strong> Each report assumes the ones before it. Part I is the foundation; skipping it is how the gaps got there. Part IV ends with a capstone exam across the whole course.</li>
      <li><strong>Deep dives when you want them.</strong> Unit 10 (Troy) extends unit 4, unit 11 (Alexander) extends module 6.7, and unit 12 (Greek philosophy) extends modules 5.6, 6.5, 7.2 and 7.4. Take each straight after the material it extends, or after the capstone.</li>
      <li><strong>One or two a sitting.</strong> A report is about 3,000 words, fifteen to twenty minutes. More than two a day and the self-tests stop meaning anything.</li>
      <li><strong>Self-test before moving on.</strong> Under 7 of 10, re-read. The carry-forward ideas at the end of each report are the ones later reports lean on.</li>
      <li><strong>A study text, not scripture.</strong> Citations are given so you can check them against the primary sources. Where sources disagree, the report says so in a red-edged box.</li>''',
    rules_count='five rules',
    spine='''<p>The reports keep naming these. Read the primary ones at least once each, in this order, any decent translation: Hesiod (Theogony, Works and Days) · Homer (Iliad, then Odyssey) · Apollodorus, The Library (Robin Hard's Oxford translation; keep it open through Part II) · Aeschylus' Oresteia, Sophocles' Theban plays, Euripides' Medea and Bacchae · Herodotus · Thucydides · Plato (Apology, Symposium, Republic; with unit 6 and deep dive 12) · Diogenes Laertius, books 6, 7 and 10 (with deep dive 12) · Plutarch's Lives as each name comes up · Pausanias, book 1.</p>
    <p>Secondary, three only: Robin Hard, The Routledge Handbook of Greek Mythology; Walter Burkert, Greek Religion; Robin Osborne, Greece in the Making, with Simon Hornblower, The Greek World 479 to 323.</p>''',
    closing='Greece is the first course. Rome, the second, is in progress; eight more are coming: Egypt, Persia, Norse, Celtic, English, Scottish, Chinese, Japanese.',
    card='From the Bronze Age palaces to the closing of the Academy, with the gods, the heroes and the Trojan War read against the societies that told them. Ten core units in four parts, three deep dives on Troy, Alexander and Greek philosophy, and a capstone exam.',
    figure=dict(kind='tree', title='Hesiod\'s line of descent, Chaos to the six Olympian siblings',
        caption='The first beings and the two generations that follow, as module 2.1 reads them in Hesiod, <em>Theogony</em> 116–138 (Chaos, Gaia, Tartarus, Eros, Erebus, Nyx; Gaia bears Ouranos), 132–138 (the Titans, Kronos last) and 453–458 (the six children of Kronos and Rhea, Zeus last). Erebus and Nyx, the Mountains, Pontos and the other Titans are left out for room.',
        root=dict(label='Chaos', tone=6, children=[
            dict(label='Gaia', tone=2, children=[dict(label='Ouranos', tone=4, children=[dict(label='Kronos and Rhea', tone=5, children=[
                dict(label='Hestia', tone=1), dict(label='Demeter', tone=1), dict(label='Hera', tone=1), dict(label='Hades', tone=1), dict(label='Poseidon', tone=1), dict(label='Zeus', tone=1)])])]),
            dict(label='Tartarus', tone=2), dict(label='Eros', tone=2)])),
    card_units=13, status='available',
)

ROME = dict(
    id='rome', family='history', theme='history', num=2, short='Rome', label='ROME', name='Roman history and mythology', color='var(--purple)',
    syllabus='roman-syllabus.html', frags='rome', prompts='prompts-rome.json', prefix='rm',
    home_id='rome', syl_id='rome-syllabus', syl_anchor='rs',
    unit_colors={'0': 'var(--gold)', '1': 'var(--orange)', '2': 'var(--purple)', '3': 'var(--teal)', '4': 'var(--red)', '5': 'var(--orange)', '6': 'var(--purple)', '7': 'var(--blue)', '8': 'var(--teal)', '9': 'var(--gold)', '10': 'var(--blue)', '11': 'var(--red)', '12': 'var(--purple)', '13': 'var(--gold)', '14': 'var(--teal)'},
    sections={'0': 'Core course', '11': 'Deep dives', '14': 'Quality'},
    audit_unit='14', default_model='Opus 5.5',
    parts=[
        ("I", "Ground rules and origins", ["0", "1", "2"], "c. 1000 to 509 BC, and the gods throughout", "Where the evidence comes from, the land and peoples of Italy, the legends Rome told about its birth, and the religion everything after it ran on."),
        ("II", "The Republic", ["3", "4", "5"], "509 to 30 BC", "From the expulsion of the kings to Actium: the conquest of Italy, Carthage and the East, then a century of reformers, generals and civil war."),
        ("III", "The Empire", ["6", "7", "8"], "31 BC to AD 476, and on to 1453", "Augustus and the Principate, the third-century crisis and the Christian empire, to the last emperor in the West and the eastern empire that outlived him."),
        ("IV", "Practice and legacy", ["9", "10"], "across the whole span", "Law, the army, the household and the city; Ovid, the imperial writers, the art, and how all of it reached you. Ends with the capstone exam."),
        ("+", "Deep dives", ["11", "12", "13"], "optional", "The fall of the Republic, the Aeneid and Roman philosophy taken to the depth the survey could not reach. Best after the material they extend, or after the capstone."),
        ("✓", "Quality audit", ["14"], "run when ready", "A check on the course itself. The syllabus and every report so far were written with Opus 5.5 and are flagged for review with Fable 5.1; this unit runs that review: the Greek rubric, the cross-references back to Greece, the syllabus itself, and fixes for what falls short."),
    ],
    eras=[("Iron Age Italy", -1000, -753, "var(--orange)", "modules 1.1 and 1.2"),
          ("Regal period", -753, -509, "var(--gold)", "modules 1.3 to 1.6, all of it legend written down five centuries later"),
          ("Early and middle Republic", -509, -133, "var(--teal)", "units 3 and 4"),
          ("Late Republic", -133, -27, "var(--red)", "unit 5 and deep dive 11"),
          ("Principate", -27, 284, "var(--purple)", "units 6 and 7, and module 8.1"),
          ("Late empire", 284, 476, "var(--blue)", "unit 8; the eastern empire runs on to 1453")],
    era_title='1,500 years, to scale', era_range='1000 BC → AD 476',
    era_aria='Timeline from 1000 BC to AD 476, to scale: the regal period is a sixth of it; the late Republic is a thin red slice.',
    ticks=[('1000 BC', '0'), ('509 BC', f'{(491/1476)*100:.1f}%'), ('AD 1', f'{(1000/1476)*100:.1f}%'), ('476', '100%')],
    era_note='The late Republic that most people mean by "ancient Rome" is the thin red slice: about a century. The kings in the gold band were written about by Romans living in it, five hundred years after the fact. The eastern empire that kept the Roman name until 1453 runs off the right-hand edge.',
    eyebrow='COURSE 2 · ROME',
    h1='Roman history and mythology',
    lede='Four parts and three deep dives, {content_mods} modules, plus a quality audit. History and myth are interleaved more tightly than in the Greek course, because Rome told its myths as history: the legends sit inside the periods that produced them. Every module is a long-form report with named primary sources, the places where the accounts disagree, a ten-question self-test and three ideas to carry forward.',
    rules='''<li><strong>Parts I to IV in order.</strong> Each report assumes the ones before it. Part I matters more here than in Greece: the evidence for Rome's first four centuries is late and partisan, and every later report assumes you know how late. Part IV ends with a capstone exam.</li>
      <li><strong>Deep dives when you want them.</strong> Unit 11 (the fall of the Republic) extends unit 5; unit 12 (the Aeneid) extends module 6.3 and, for Aeneas, module 1.3; unit 13 (Roman philosophy) extends modules 4.5, 5.6, 7.3 and 10.2. Take each straight after the material it extends, or after the capstone.</li>
      <li><strong>Greece behind you.</strong> Rome points back to the Greek course instead of repeating it: Greek 7.3 and 7.4 for the Greek side of the conquest, 2.2 for the Olympians, 9.3 and 10.12 for reception. Open the Greek module when a report names it.</li>
      <li><strong>One or two a sitting, self-test before moving on.</strong> Under 7 of 10, re-read. The carry-forward ideas are the ones later reports lean on.</li>
      <li><strong>A study text, not scripture.</strong> Citations are given so you can check them against the primary sources. Where sources disagree, the report says so in a red-edged box.</li>''',
    rules_count='five rules',
    spine='''<p>The reports keep naming these. Read the primary ones at least once each, in this order, any decent translation: Livy, books 1 to 5 and then 21 to 30 · Polybius, books 1 to 6 · Virgil, Aeneid (book 8 with module 1.3) · Ovid, Fasti, then Metamorphoses · Sallust, The War with Catiline · Caesar, The Gallic War · Cicero, selected letters (Shackleton Bailey's translation) and the Second Philippic · Plutarch's Roman Lives as each name comes up · Augustus, Res Gestae · Tacitus, Annals · Suetonius, The Twelve Caesars · Seneca, Letters to Lucilius (a selection), Epictetus, Handbook, and Marcus Aurelius, Meditations (with deep dive 13) · Ammianus Marcellinus, books 14 to 31.</p>
    <p>Secondary, three only: T. J. Cornell, The Beginnings of Rome; Mary Beard, John North and Simon Price, Religions of Rome; Mary Beard, SPQR, with Peter Heather, The Fall of the Roman Empire.</p>''',
    closing='Rome is the second course, after Greece. Eight more are coming: Egypt, Persia, Norse, Celtic, English, Scottish, Chinese, Japanese.',
    card='From the huts on the Palatine to the last emperor in the West, with the gods, the founding legends and the Aeneid read against the city that told them. Eleven core units in four parts, three deep dives on the fall of the Republic, the Aeneid and Roman philosophy, and a capstone exam.',
    figure=dict(kind='timeline', title='The Struggle of the Orders: what the plebs won, and when', start=-500, end=-160, ticks=[-500, -400, -300, -200],
        caption='Dates as module 3.1 gives them, from Livy (Varronian years): the tribunate after the secession of 494; the Twelve Tables 451–449; the quaestorship opened in 421 and first held by plebeians in 409; the consulship from the Licinian-Sextian laws, Lucius Sextius consul in 366; the first plebeian dictator 356 and censor 351; the Publilian laws 339; the lex Ogulnia opening the pontificate and augurate in 300; the secession of 287; both consuls plebeian for the first time in 172.',
        spans=[dict(**{'from': -494, 'to': -449, 'label': 'Tables', 'tone': 6}), dict(**{'from': -449, 'to': -367, 'label': 'consular tribunes', 'tone': 4}), dict(**{'from': -367, 'to': -287, 'label': 'offices open', 'tone': 5})],
        events=[dict(at=-494, label='Tribunes of the plebs', tone=6), dict(at=-451, label='Twelve Tables', tone=6), dict(at=-421, label='Quaestorship opened', tone=4),
                dict(at=-409, label='First plebeian quaestors', tone=4), dict(at=-366, label='Sextius consul', tone=5), dict(at=-356, label='First plebeian dictator', tone=5),
                dict(at=-351, label='First plebeian censor', tone=5), dict(at=-339, label='Publilian laws', tone=5), dict(at=-300, label='Lex Ogulnia: priesthoods', tone=5),
                dict(at=-287, label='Secession; lex Hortensia', tone=1), dict(at=-172, label='Both consuls plebeian', tone=1)]),
    card_units=14, status='in progress',
    # modules queued for the next writing session: shown with a 'next' pill until written
    next_up=['11.7', '11.8', '12.1', '12.2', '12.3', '12.4', '12.5', '12.6', '12.7', '12.8', '13.3', '13.4', '13.5', '13.6', '13.7', '13.8'],
)

BRAND_AI = dict(
    id='brand-ai', family='markdown', short='Brand + AI', label='BRAND + AI', name='Brand + AI: two courses for one reader', color='var(--teal)',
    home_id='brand-ai', status='in progress',
    prefix='brand',               # panel ids brand-a, brand-b (a new markdown course defaults to its id)
    legacy_ids=True,              # keeps #briefs-a and #b-a2 from A3; a new course gets #<id>-<key>-briefs, #<id>-<key>-b-<code>
    # each course in the data file's COURSES becomes its own Academy course: key -> (track, short name for the top bar and drawer)
    tracks={'A': ('marketing', 'Personal brand'), 'B': ('technology', 'Building with AI')},
    # content and status come from the hub's own data file; build.py reads it, nothing here is typed by hand
    data='generator/data/brand-ai/hub.py',
    vault='courses/brand-ai',     # the filed units (method.md §7); a unit is written when its file is here (A5)
    eyebrow='BRAND + AI',
    card='A · Building a Marketable Personal Brand and B · Using AI to Build a Brand. Who pays, for what, how long it takes; which model for which task, how to brief, where the setup leaks. Every unit sourced and ending in a shipped deliverable.',
)

UX = dict(
    id='ux', family='markdown', short='User Experience', label='USER EXPERIENCE', name='User Experience: courses for other designers', color='var(--blue)',
    home_id='ux', status='in progress',
    # panel ids default to <id>-<key>: ux-ia, ux-ia-briefs, ux-ia-b-ia1 (no prefix, no legacy_ids)
    tracks={'IA': ('ux', 'Information architecture')},
    data='generator/data/ux/hub.py',
    vault='courses/ux',             # the filed units (method.md §7); the folder appears with the first one (A5)
    sourcing_part='Part 4',         # sourcing-standard.md: this family's own part (howbuilt.py)
    eyebrow='USER EXPERIENCE',
    card='IA · Information Architecture, for a mid-level UX designer: what IA is, the shapes it takes, four levels of complexity built on one fictional product, where it sits in the product cycle and the business, how to validate it, and how to deliver it when the research, the content or the stakeholders are missing.',
)

COURSES = [GREECE, ROME, BRAND_AI, UX]

# Editions (P70, 1 Nov 2026): a build of Academy with only some courses, from the same sources, theme, shell and rules.
# `courses`: the ids of the courses it holds (None: every course); `omit`: what it leaves out, by panel kind
# ('changelog', 'backlog', 'build': a course's "How it was built" and build pages, 'figures': the Figure kinds page)
# and 'planned' (the planned courses on the home); `site`: the folder build.py writes, relative to kit/.
# `python3 build.py --edition <name>` builds one; the full Academy is the edition 'academy' and the default.
EDITIONS = {
    'academy': dict(title='Academy', courses=None, omit=(), site='academy'),
    'greece': dict(title='Academy · Greece', courses=('greece',), omit=('changelog', 'backlog', 'build', 'figures', 'planned'),
                   site='editions/greece', artifact='https://claude.ai/artifact/M9g881qokC98jC5VEo1Tk3',   # P80: its own private artifact
                   # P80: the edition's own constants where the shared line names a course it does not hold (Brand + AI)
                   rules={'One unit per chat, built in full.': 'Each report is written from its published prompt, in its own chat, with its closing artefact: a ten-question self-test and three ideas to carry forward.'}),
}
HISTORY = [c for c in COURSES if c['family'] == 'history']
MARKDOWN = [c for c in COURSES if c['family'] == 'markdown']

NEXT = [
 ("Egypt", "Egyptian history and mythology", "var(--gold)",
  "Three thousand years, thirty-one dynasties, and a religion the Greeks themselves treated as the oldest in the world. Predynastic unification, the Old Kingdom and the pyramids, the Middle and New Kingdoms, Akhenaten, Ramesses and the Sea Peoples, the Late Period and Persian rule, the Ptolemies you met in unit 7; then the cosmogonies of Heliopolis, Memphis and Hermopolis, the Osiris cycle, the solar journey, ma'at, the Book of the Dead and the afterlife, temple and priesthood, and how to read hieroglyphs enough to recognise a cartouche.",
  "Pyramid Texts · Coffin Texts · Book of the Dead · the Shabaka Stone · Herodotus book 2 · Wilkinson, The Rise and Fall of Ancient Egypt · Assmann, The Search for God in Ancient Egypt"),
 ("Persia", "Persian history and mythology", "var(--blue)",
  "The other side of units 6 and 11, told from Persepolis rather than Athens. Elam and the Medes, Cyrus and the Achaemenid empire, Darius and Xerxes as the Persians saw them, the satrapal system, Zoroaster and the Avesta, Ahura Mazda and the dualist cosmos, the Parthians, the Sasanians and their wars with Rome, the Zoroastrian apocalyptic, then the Shahnameh as the national epic that fused myth and history into one narrative of kings.",
  "Behistun inscription · the Avesta (Gathas, Yashts) · Herodotus · Xenophon, Cyropaedia · Firdausi, Shahnameh · Briant, From Cyrus to Alexander · Boyce, Zoroastrians"),
 ("Norse", "Viking and Norse history and mythology", "var(--teal)",
  "The Scandinavian Iron Age and the Viking expansion, 793 to 1066 and beyond: raids, trade routes to Byzantium and Baghdad, the settlement of Iceland, Greenland and Vinland, the Danelaw, Normandy, the Rus, the conversion. Then the mythology as the two Eddas preserve it: Ymir and the world's making, Yggdrasil and the nine worlds, Odin, Thor, Loki, Freyja and the Vanir war, the death of Baldr, Ragnarok, the heroic legends of Sigurd and the Volsungs, and the problem of a pagan mythology written down by Christians two centuries late.",
  "Poetic Edda · Snorri, Prose Edda · Heimskringla · Saga of the Volsungs · Egil's Saga · Njal's Saga · Price, Children of Ash and Elm · Lindow, Norse Mythology"),
 ("Celts", "Celtic history and mythology", "var(--purple)",
  "Hallstatt and La Tène, the Celtic expansion across Europe, the sack of Rome and Delphi, Gaul and Caesar's conquest, the druids as the Greeks and Romans described them, Roman Britain, then the two literary survivals: the Irish cycles (the Mythological Cycle and the Tuatha Dé Danann, the Ulster Cycle and Cú Chulainn, the Fenian Cycle, the Kings' Cycle) and the Welsh Mabinogion, with the question of how much is pre-Christian myth and how much medieval literature.",
  "Caesar, Gallic War · Lebor Gabála Érenn · Táin Bó Cúailnge · the Mabinogion · Cunliffe, The Ancient Celts · Koch, Celtic Culture"),
 ("England", "English history and mythology", "var(--orange)",
  "From Roman Britain and the Anglo-Saxon settlement through Alfred, the Conquest, the Angevins, Magna Carta, the Wars of the Roses, the Tudors and the Reformation, the Civil War, and the making of the constitutional state. Alongside it the legendary matter: Beowulf and the Germanic inheritance, Bede's England, Geoffrey of Monmouth's invented history and the Arthurian cycle from Nennius to Malory, Robin Hood, the Green Man, and how England manufactured a national past.",
  "Beowulf · Bede · the Anglo-Saxon Chronicle · Geoffrey of Monmouth · Malory, Le Morte d'Arthur · Tombs, The English and Their History · Morris, The Anglo-Saxons"),
 ("Scotland", "Scottish history and mythology", "var(--teal)",
  "Picts, Scots, Britons and Angles; Dál Riata and the kingdom of Alba; Macbeth as he was; the Wars of Independence, Wallace and Bruce; the Stewarts, the Reformation and Knox, the Union of Crowns and of Parliaments, the Jacobite risings, the Clearances, the Enlightenment. Then the mythology and legend: the Pictish stones, the Celtic saints (Columba, Iona), the Fenian material in Gaelic Scotland, the kelpies, selkies and the Sìth, the Border ballads, Ossian and the eighteenth-century invention of Highland tradition.",
  "Adomnán, Life of Columba · the Declaration of Arbroath · Barbour, The Brus · the Child Ballads · Macpherson's Ossian · Devine, The Scottish Nation · Fraser, From Caledonia to Pictland"),
 ("China", "Chinese history and mythology", "var(--gold)",
  "The Shang and the oracle bones, the Zhou and the Mandate of Heaven, the Warring States and the hundred schools, Qin unification, the Han, the period of division, Tang, Song, Yuan, Ming and Qing down to 1911. Then the mythology, which China kept largely in philosophy and ritual rather than epic: Pangu and Nüwa, the Three Sovereigns and Five Emperors, Yu and the flood, the Queen Mother of the West, the Jade Emperor and the bureaucratic heaven, Daoist immortals, Buddhist arrivals, and the great vernacular novels as a late mythology (Journey to the West, Investiture of the Gods).",
  "Shijing · Shangshu · Sima Qian, Records of the Grand Historian · Shanhaijing · Zhuangzi · Journey to the West · Lewis, The Early Chinese Empires · Birrell, Chinese Mythology"),
 ("Japan", "Japanese history and mythology", "var(--red)",
  "Jōmon and Yayoi, the Yamato state and the Chinese model, Nara and Heian court culture, the rise of the warriors, Kamakura, the Mongol invasions, the Sengoku wars and unification, Tokugawa isolation, Meiji. Then the mythology as the Kojiki and Nihon Shoki set it down to legitimise the imperial house: Izanagi and Izanami, Amaterasu and the cave, Susanoo and the serpent, the descent of Ninigi, Jimmu; Shinto as practice, kami and shrines, the Buddhist synthesis, the yōkai tradition, and the Tale of the Heike as a national epic of defeat.",
  "Kojiki · Nihon Shoki · Man'yōshū · Tale of Genji · Tale of the Heike · Totman, A History of Japan · Breen and Teeuwen, A New History of Shinto"),
]
