"""P84 and P109 round 3 FIXes applied to figure declarations as exact replacements (each current text must occur once in its
file). Usage: python3 apply_round1.py (from the repo root). Prose is never touched: every current text is inside a viz block."""
import pathlib, re, sys
R = pathlib.Path('.')
E = [
 ('courses/greece/10.5-*', '"label": "Cult appears (7th century, 700–601 BC)"', '"label": "Cult appears (7th century BC)"'),
 ('courses/greece/10.5-*', '"label": "Stele to Menelaus (5th century, 500–401 BC)"', '"label": "Stele to Menelaus (5th century BC)"'),
 ('courses/brand-ai/A8-*', '{"label": "Disclosure (R17–R18)", "tone": 4, "cells": [{"mark": "owns", "tone": 3}, null, null, null, null, {"mark": "label", "tone": 2}]}', '{"label": "Disclosure (R17–R18)", "tone": 4, "cells": [{"mark": "owns", "tone": 3}, null, {"mark": "if DGC writes", "tone": 5}, null, null, {"mark": "label", "tone": 2}]}'),
 ('courses/brand-ai/A8-*', '{"mark": "optional", "means": "a lawyer only if he wants the reading confirmed", "tone": 5},', '{"mark": "optional", "means": "a lawyer only if he wants the reading confirmed", "tone": 5},\n  {"mark": "if DGC writes", "means": "a lawyer only if the DGC writes about it", "tone": 5},'),
 ('courses/rome/1.4-*', '{"at": -200, "label": "Fabius Pictor (about)"}', '{"at": -200, "date": "about 200 BC", "label": "Fabius Pictor"}'),
 ('courses/rome/1.4-*', '{"at": -7, "label": "Dionysius (from)"}', '{"at": -7, "date": "from 7 BC", "label": "Dionysius"}'),
 ('courses/rome/1.4-*', '{"at": 100, "label": "Plutarch (about)"}', '{"at": 100, "date": "about AD 100", "label": "Plutarch"}'),
 ('courses/rome/3.4-*', 'Dated colony foundations named in this report, citizen colonies marked, the rest Latin, from the section Colonies and roads as instruments of control, with dates from The First and Second Samnite Wars, 343–304 and Sentinum and the end of Samnite independence, 298–264; the report cites Livy 8.22–23 for Fregellae and no passage for the other dates.', 'Dated colony foundations named in this report, citizen colonies marked, the rest Latin: the citizen colonies\' dates and the span of about nineteen Latin colonies, 334–263, from the section Colonies and roads as instruments of control; the Latin colonies\' dates from The First and Second Samnite Wars, 343–304 and Sentinum and the end of Samnite independence, 298–264; the report cites Livy 8.22–23 for Fregellae and no passage for the other dates.'),
 ('courses/personal-brand/DD-PB2-*', '{"label": "Own digital product", "tone": 3, "cells": ["since 8 Jun 2027", {"mark": "her count only", "tone": 3}, "her net sales"]}', '{"label": "Own digital product", "tone": 4, "cells": ["since 8 Jun 2027", {"mark": "her count only", "tone": 3}, "her net sales"]}'),
 ('courses/rome/13.4-*', '"date": "93, after August"', '"date": "AD 93, after August"'),
]
for g, old, new in E:
    f = next(R.glob(g)); s = f.read_text()
    n = s.count(old)
    if n != 1: sys.exit(f'{f}: {n} matches for {old[:60]!r}')
    blocks = [m.span() for m in re.finditer(r'```viz\n.*?```', s, re.S)]
    i = s.index(old)
    if not any(a <= i < b for a, b in blocks): sys.exit(f'{f}: {old[:60]!r} is not inside a viz block')
    f.write_text(s.replace(old, new)); print('ok', f.name, old[:50])
