"""Cohesion checks for new reports against the rest of their course (run before publishing).

python3 crosscheck.py rome 7.1 7.2 7.3      # the new reports
python3 crosscheck.py rome                  # every report in the course

Prints, for the given reports:
  1. every cross-reference ("module X.Y", "Greek module X.Y", "deep dive module X.Y") with its context,
     marked WRITTEN or NOT YET, so each claim about a written report can be checked against that report;
  2. passages shared with any other report of the course (7-word shingles, 3 or more in common);
  3. dispute boxes that share four or more proper names with a dispute box elsewhere (possible duplicates).
It reports candidates; reading the target and deciding is the maintainer's job.
"""
import re, sys, html, pathlib, itertools
from courses import HISTORY as COURSES

R = pathlib.Path(__file__).resolve().parent
cid, ids = sys.argv[1], sys.argv[2:]
course = next(c for c in COURSES if c['id'] == cid)
other = next((c for c in COURSES if c['id'] != cid), None)
key = lambda p: [int(x) for x in p.stem[2:].split('.')]
reps = {p.stem[2:]: p for p in sorted((R / course['frags']).glob('r-*.html'), key=key)}
mine = ids or list(reps)
other_written = {p.stem[2:] for p in (R / other['frags']).glob('r-*.html')} if other else set()
other_name = ({'greece': 'Greek'}.get(other['id'], other['id'].capitalize())) if other else ''

def text(p, body_only=False):
    s = p.read_text(encoding='utf8')
    if body_only:
        s = s.split('<h2>Self-test</h2>')[0]
    return html.unescape(re.sub(r'<[^>]+>', ' ', s))

print('== 1. cross-references ==')
pat = re.compile(r'(%s modules?|deep dive modules?|modules?)\s+((?:\d+\.\d+)(?:(?:,\s*|\s+and\s+|\s+to\s+|–)\d+\.\d+)*)' % re.escape(other_name), re.I)
for i in mine:
    t = re.sub(r'\s+', ' ', text(reps[i], True))
    for m in pat.finditer(t):
        cross = m.group(1).lower().startswith(other_name.lower()) if other_name else False
        for tid in re.findall(r'\d+\.\d+', m.group(2)):
            if tid == i and not cross:
                continue
            ok = (tid in other_written) if cross else (tid in reps)
            label = f"{other_name + ' ' if cross else ''}{tid}"
            print(f"[{i}] -> {label:<12} {'WRITTEN' if ok else 'NOT YET'} …{t[max(0, m.start() - 130):m.end() + 30]}…")

print('\n== 2. shared passages (7-word shingles) ==')
def shingles(p):
    w = re.findall(r"[a-z0-9']+", text(p).lower())
    return {tuple(w[k:k + 7]) for k in range(len(w) - 6)}
sh = {k: shingles(p) for k, p in reps.items()}
for i in mine:
    for j in reps:
        if j == i or (j in mine and j < i):
            continue
        c = sh[i] & sh[j]
        if len(c) >= 3:
            ex = ' | '.join(' '.join(x) for x in sorted(c)[:3])
            print(f'{len(c):3d} {i} ~ {j}: {ex}')

print('\n== 3. dispute boxes with four or more shared names ==')
stop = {'Where', 'Some', 'Most', 'Both', 'None', 'That', 'This', 'Whether', 'Their', 'Others', 'Each', 'Since', 'Rome', 'Roman', 'Romans', 'Greek', 'Greece', 'Italy',
        'Journal', 'Studies', 'History', 'Livy', 'Plutarch', 'Polybius', 'Appian', 'Cicero', 'Dionysius', 'Caesar', 'Velleius', 'Sallust',
        'Suetonius', 'Tacitus', 'Annals', 'Pliny', 'Augustus', 'Diodorus', 'Varro', 'Ovid', 'Virgil', 'Herodotus', 'Thucydides', 'Natural'}
def boxes(k):
    s = reps[k].read_text(encoding='utf8')
    for m in re.finditer(r'<aside class="dispute">(.*?)</aside>', s, re.S):
        t = html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
        yield set(re.findall(r'\b([A-Z][a-z]{3,})\b', t)) - stop, t[:140]
allb = {k: list(boxes(k)) for k in reps}
for i in mine:
    for j in reps:
        if j == i or (j in mine and j < i):
            continue
        for (na, ta), (nb, tb) in itertools.product(allb[i], allb[j]):
            common = na & nb
            if len(common) >= 4:
                print(f'{i} ~ {j}: {sorted(common)[:8]}\n   {i}: {ta}\n   {j}: {tb}')
