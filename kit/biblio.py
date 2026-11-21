"""Sources and bibliography per unit, extracted from the reports (the vault files, P71-3; vault.py) for future checks.

python3 biblio.py            writes unit-<n>.md for every course and unit into the course's `bibliography` folder
                             (course.toml; courses/<course>/bibliography/ since S-DEC5) and kit/bibliography/README.md (run by build.py)
python3 biblio.py rome 5     prints one unit

Machine-extracted from the citations the reports carry inline (Pedro's rule, 27 October 2026: every unit keeps its
sources and bibliography). It is a check aid, not a finished bibliography: it lists what each report cites, grouped
as ancient works (author, work, locators), ancient authors cited by bare locator, modern works (name, title, year) and
corpora or inscriptions, with the reports that cite each. A curated bibliography written by the report's writer, when
one exists, sits beside it as r-<id>.md (see AGENT-SPEC.md) and is linked from the unit file. The text this writes names
`courses/<course>/bibliography/...`, the folder's place from the repo root since S-DEC5 (P-DEC6, 21 Nov 2026; until then
it said `bibliography/<course>/...`, the path from kit/ before S-DEC5).
"""
import sys, re, html, json, pathlib
from collections import defaultdict
from courses import HISTORY as COURSES, path as cpath
import vault

R = pathlib.Path(__file__).resolve().parent
OUT = R / 'bibliography'   # the README only; each course's files go to its `bibliography` folder (S-DEC5)
YEAR = r'(?:1[5-9]\d\d|20\d\d)'
NAME = r"(?:[A-Z][\w'’\-]*\.? ){0,3}[A-Z][\w'’\-]+(?: (?:de|van|von|della|du|di|le) [A-Z][\w'’\-]+)?"
LOC = r'\d+(?:[.:]\d+)*[a-e]?(?: ?[–-] ?\d+(?:[.:]\d+)*[a-e]?)?(?:, \d+(?:[.:]\d+)*[a-e]?(?: ?[–-] ?\d+(?:[.:]\d+)*[a-e]?)?)*'
CORPORA = r'\b(ILS|ILLRP|CIL|IG|SEG|ML|RRC|RIC|RPC|BMCRE|FGrH|FRHist|DK|SVF|LS|KAI|CTh|CJ|AE|RIB|OGIS|SIG|P\.\s?Oxy\.|P\.\s?Köln|BNJ|HN Italy|TLE|ET)\b\s*(?:[IVX]+[.\d]*\s*)?[\d][\d./,–\- ]*\d?'
ANCIENT_AUTHORS = ('Livy|Appian|Dio|Polybius|Plutarch|Velleius|Sallust|Cicero|Suetonius|Tacitus|Dionysius|Pliny|Valerius Maximus|'
    'Orosius|Eutropius|Gellius|Strabo|Josephus|Herodotus|Thucydides|Xenophon|Pausanias|Diodorus|Justin|Florus|Frontinus|Memnon|'
    'Varro|Festus|Macrobius|Servius|Augustine|Lactantius|Eusebius|Zosimus|Ammianus|Herodian|Caesar|Nepos|Ovid|Virgil|Horace|'
    'Propertius|Tibullus|Lucan|Juvenal|Martial|Seneca|Epictetus|Aulus Gellius|Censorinus|Solinus|Aristotle|Plato|Homer|Hesiod|'
    'Apollodorus|Pindar|Aeschylus|Sophocles|Euripides|Aristophanes|Demosthenes|Isocrates|Lysias|Arrian|Curtius|Athenaeus|'
    'Diogenes Laertius|Sextus|Plotinus|Proclus|Simplicius|Stobaeus|Photius|Procopius|Agathias|Jerome|Lucretius|Statius|Silius|'
    'Valerius Flaccus|Quintilian|Fronto|Aelian|Dionysius of Halicarnassus|Philostratus|Lucian|Hyginus|Nonnus|Quintus Smyrnaeus|'
    'Zonaras|Malalas|Jordanes|Cassiodorus|Sidonius|Symmachus|Ausonius|Claudian|Prudentius|Tertullian|Minucius Felix|Origen|Porphyry|'
    'Iamblichus|Marinus|Damascius|Olympiodorus|Priscus|Hydatius|Marcellinus|Victor|Aurelius Victor|Obsequens|Julius Obsequens|'
    'Asconius|Ennius|Naevius|Cato|Fabius Pictor|Piso|Antias|Valerius Antias|Licinius Macer|Claudius Quadrigarius|Timaeus|Callias|'
    'Hieronymus|Phylarchus|Posidonius|Panaetius|Fabius|Nicolaus|Pompeius Trogus|Res Gestae|Periochae|Epitome')

def text_of(frag):
    t = re.sub(r'<(?!/?em\b)[^>]+>', ' ', frag)
    t = html.unescape(t)
    return re.sub(r'[ \t]+', ' ', t)

def extract(frag):
    t = text_of(frag)
    anc, bare, mod, corp = defaultdict(set), defaultdict(set), set(), set()
    # ancient: [Author, ]<em>Work</em> locators
    for m in re.finditer(r'(?:(%s),? )?<em>([^<]{2,70})</em>,? (%s)' % (NAME, LOC), t):
        author, work, loc = m.group(1) or '', m.group(2).strip(), m.group(3).strip(' ,.;')
        if re.fullmatch(YEAR, loc) or re.fullmatch(r'(ILS|ILLRP|CIL|IG|SEG|ML|RRC|RIC|RPC|FGrH|FRHist|DK|SVF|LS|KAI|CTh|CJ|AE|RIB|OGIS|SIG|BNJ|TLE|ET|JRS|CQ|JHS|Historia|Hermes|ANRW|JRA|CAH|BMCR|PBSR|ZPE|AJP|CP|TAPA|Phoenix|Klio|Chiron|Athenaeum|Latomus|MEFRA|REL|RhM)', work): continue
        if author and author.split()[-1] in ('The', 'In', 'A', 'On', 'By', 'For', 'Of', 'And', 'But', 'At', 'With', 'From', 'Where', 'See', 'Compare', 'Thus', 'So', 'Yet'): author = ''
        if author and not re.search(r'\b(%s)\b' % ANCIENT_AUTHORS, author) and author.split()[-1] not in ('Pseudo', 'Ps'):
            # a capitalised word before the title that is not an author (e.g. "In", a place): keep the work, drop the author
            if author not in ('Cicero', 'Plutarch') and len(author.split()) > 1 and not re.search(r'\b(%s)\b' % ANCIENT_AUTHORS, author):
                author = ''
        anc[(author, work)].add(loc)
    # modern: Name (<em>Title</em>, YEAR) | Name ("Title", [<em>Journal</em>] YEAR) | Name (YEAR) | Name's <em>Title</em> (YEAR)
    for m in re.finditer(r'(%s)(?:\'s|’s)? \((?:<em>([^<]+)</em>|"([^"]+)"|“([^”]+)”)?[^()]*?(%s)[a-c]?\)' % (NAME, YEAR), t):
        name, title, year = m.group(1), (m.group(2) or m.group(3) or m.group(4) or ''), m.group(5)
        if re.search(r'\b(%s)\b' % ANCIENT_AUTHORS, name): continue
        if name.split()[-1] in ('In', 'The', 'A', 'On', 'By', 'For', 'Of', 'And', 'But', 'At', 'With', 'From', 'Where'): continue
        mod.add((name, title.strip(), year))
    for m in re.finditer(r'(%s)(?:\'s|’s) <em>([^<]+)</em> \((%s)\)' % (NAME, YEAR), t):
        if not re.search(r'\b(%s)\b' % ANCIENT_AUTHORS, m.group(1)): mod.add((m.group(1), m.group(2).strip(), m.group(3)))
    # bare author + locator, no work named
    for m in re.finditer(r'\b(%s),? (\d+(?:\.\d+)+(?:[–-]\d+(?:\.\d+)*)?)' % ANCIENT_AUTHORS, t):
        bare[m.group(1)].add(m.group(2))
    for m in re.finditer(CORPORA, t):
        corp.add(re.sub(r'\s+', ' ', m.group(0).strip(' ,.;')))
    # a work cited without its author takes the author it has elsewhere in the same report, when there is exactly one
    for (a, w) in [k for k in anc if not k[0]]:
        owners = {k[0] for k in anc if k[0] and k[1] == w}
        if len(owners) == 1:
            anc[(owners.pop(), w)] |= anc.pop(('', w))
    return anc, bare, mod, corp

def lockey(s):
    """Natural sort for a locator ('1.2' before '1.10'); the raw string breaks any tie so the order is total."""
    return ([int(x) if x.isdigit() else x for x in re.split(r'(\d+)', s)], s)

def unit_md(c, u, ids):
    idx = json.load(open(cpath(c, 'prompts')))
    lines = [f"# {c['short']} unit {u}: sources cited", '',
             f"Machine-extracted by `biblio.py` from the inline citations of the {len(ids)} report{'s' if len(ids) != 1 else ''} in unit {u} on every build; a check aid, not a finished bibliography. A curated `{cpath(c, 'bibliography').relative_to(R.parent).as_posix()}/r-<id>.md`, where one exists, is linked under its report.", '']
    for i in ids:
        if not vault.report_path(c, i): continue
        anc, bare, mod, corp = extract(vault.report_html(c, i, draw=False))
        cur = cpath(c, 'bibliography') / f'r-{i}.md'
        lines += [f"## {i} {idx.get(i, {}).get('title', '')}", '']
        if cur.exists(): lines += [f"Curated bibliography: `{cpath(c, 'bibliography').relative_to(R.parent).as_posix()}/r-{i}.md`.", '']
        lines += ['### Ancient works']
        for (a, w), locs in sorted(anc.items(), key=lambda x: (x[0][0] or '~', x[0][1])):
            lines.append(f"- {(a + ', ') if a else ''}*{w}* {'; '.join(sorted(locs, key=lockey))}")
        if bare:
            lines += ['', '### Ancient authors cited by locator only (work named earlier in the sentence or implied)']
            for a, locs in sorted(bare.items()): lines.append(f"- {a} {'; '.join(sorted(locs, key=lockey))}")
        lines += ['', '### Modern works']
        for name, title, year in sorted(mod, key=lambda x: (x[0].split()[-1], x[2], x[1], x[0])):
            lines.append(f"- {name}, {('*' + title + '* ') if title else ''}({year})" if title else f"- {name} ({year}): title not given in the report")
        if corp:
            lines += ['', '### Corpora and inscriptions', ''] + [f'- {x}' for x in sorted(corp)]
        lines.append('')
    return '\n'.join(lines) + '\n'

def units_of(c):
    syl = cpath(c, 'syllabus').read_text()
    units = defaultdict(list)
    for i in re.findall(r'data-id="([\d.]+)"', syl):
        u = i.split('.')[0]
        if u != str(c['audit_unit']): units[u].append(i)
    return units

def write_all():
    n = 0
    for c in COURSES:
        d = cpath(c, 'bibliography'); d.mkdir(parents=True, exist_ok=True)
        for u, ids in units_of(c).items():
            have = [i for i in ids if vault.report_path(c, i)]
            if not have: continue
            (d / f'unit-{u}.md').write_text(unit_md(c, u, have)); n += 1
    (OUT / 'README.md').write_text('# Bibliography\n\nOne file per unit and course (`courses/<course>/bibliography/unit-<n>.md`), regenerated by `build.py` through `biblio.py` from the citations inside the reports: ancient works with their locators, authors cited by bare locator, modern works with title and year, corpora and inscriptions, per report. Machine-extracted, so a check aid rather than a finished bibliography; where a report has a curated `r-<id>.md` beside these (written by its writer or a later pass), the unit file links to it. Kept so that every claim can be re-checked against its source later.\n')
    return n

if __name__ == '__main__':
    if len(sys.argv) == 3:
        c = next(x for x in COURSES if x['id'] == sys.argv[1])
        ids = [i for i in units_of(c)[sys.argv[2]] if vault.report_path(c, i)]
        print(unit_md(c, sys.argv[2], ids))
    else:
        print(f'bibliography: {write_all()} unit files written to courses/<course>/bibliography/, the README to {OUT.relative_to(R.parent)}/')
