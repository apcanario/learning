"""P84 and P109 round 4 FIXes applied to figure declarations as exact replacements (each current text must occur once in its
file). Usage: python3 apply_round1.py (from the repo root). Prose is never touched: every current text is inside a viz block."""
import pathlib, re, sys
R = pathlib.Path('.')
E = [
 ('courses/greece/10.3-*', '"label": "Sixth century: Trojans drawn as hoplites"', '"label": "Sixth century BC: Trojans drawn as hoplites"'),
 ('courses/greece/10.3-*', '"label": "Fourth century: the cap a Trojan uniform"', '"label": "Fourth century BC: the cap a Trojan uniform"'),
 ('courses/greece/5.5-*', '"label": "Peisistratus rules after the third attempt", "tone": 2}', '"label": "Peisistratus rules after the third attempt", "date": "c. 546–527/6 BC", "tone": 2}'),
 ('courses/greece/5.5-*', '"label": "Hippias rules", "tone": 3}', '"label": "Hippias rules", "date": "527/6–511/10 BC", "tone": 3}'),
]
for g, old, new in E:
    f = next(R.glob(g)); s = f.read_text()
    n = s.count(old)
    if n != 1: sys.exit(f'{f}: {n} matches for {old[:60]!r}')
    blocks = [m.span() for m in re.finditer(r'```viz\n.*?```', s, re.S)]
    i = s.index(old)
    if not any(a <= i < b for a, b in blocks): sys.exit(f'{f}: {old[:60]!r} is not inside a viz block')
    f.write_text(s.replace(old, new)); print('ok', f.name, old[:50])
