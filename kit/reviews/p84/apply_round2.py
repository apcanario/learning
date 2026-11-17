"""P84 and P109 round 2 FIXes applied to figure declarations as exact replacements (each current text must occur once in its
file). Usage: python3 apply_round1.py (from the repo root). Prose is never touched: every current text is inside a viz block."""
import pathlib, re, sys
R = pathlib.Path('.')
E = [
 ('courses/brand-ai/A8-*', '{"mark": "confirms", "tone": 2}, null, null, null, null]}', '{"mark": "acts", "tone": 2}, null, null, null, null]}'),
 ('courses/brand-ai/A8-*', '{"mark": "confirms", "means": "a contabilista certificado confirms it", "tone": 2}', '{"mark": "acts", "means": "a contabilista certificado does the line or confirms it, and owns R3 and R8", "tone": 2}'),
 ('courses/greece/0.1-*', ', {"from": -200, "to": -101, "label": "Aristarchus, editor of Homer (2nd c. BC)", "tone": 4}', ''),
 ('courses/greece/0.1-*', 'the Homeric Hymns; Aristarchus and the scholia)', 'the Homeric Hymns)'),
 ('courses/greece/6.3-*', '"label": "The Thirty; Phyle (winter 404/3)"', '"label": "The Thirty, 404–403 BC; Phyle seized winter 404/3"'),
 ('courses/personal-brand/DD-PB2-*', '0 until her own RPM', '0 until both thresholds met'),
 ('courses/rome/1.3-*', '{"at": -390, "label": "Gallic sack (approx.)"}', '{"at": -390, "label": "Gallic sack (approx.), reported by Heraclides"}'),
 ('courses/greece/5.3-*', '"label": "Athens: Peisistratids (561/0–510, interrupted)"', '"label": "Athens: Peisistratids, interrupted (561/0–510)"'),
 ('courses/greece/7.4-*', '"label": "Imperial command with Macedonia and Moesia (15–44)"', '"label": "Imperial command with Macedonia and Moesia (AD 15–44)"'),
 ('courses/rome/8.5-*', '{"label": "Sueves", "tone": 2, "cells": ["411", null, null, null]}', '{"label": "Sueves", "tone": 2, "cells": [{"mark": "411", "tone": 4}, null, null, null]}'),
 ('courses/rome/8.5-*', '{"label": "Alans", "tone": 3, "cells": [null, "411", "411", null]}', '{"label": "Alans", "tone": 3, "cells": [null, {"mark": "411", "tone": 4}, {"mark": "411", "tone": 4}, null]}'),
 ('courses/rome/8.5-*', '{"label": "Siling Vandals", "tone": 5, "cells": [null, null, null, "411"]}', '{"label": "Siling Vandals", "tone": 5, "cells": [null, null, null, {"mark": "411", "tone": 4}]}'),
 ('courses/ux/IA6-*', "Blank cells: none, as in B.5's table.", 'A blank cell is \\"none\\" in B.5\'s table.'),
 ('courses/rome/11.5-*', 'From the sections The new man and his consulship to Tullia, philosophy, the Philippics and death, 45–43:', 'From the sections “The new man and his consulship” to “Tullia, philosophy, the <em>Philippics</em> and death, 45–43”:'),
 ('courses/rome/12.7-*', 'From the sections The \\"Harvard school\\" and the pessimistic reading, The optimistic or Augustan school and Further voices and the end of the binary:', 'From the sections “The ‘Harvard school’ and the pessimistic reading”, “The optimistic or Augustan school” and “Further voices and the end of the binary”:'),
 ('courses/ux/IA3-*', "Tone 3 is the app; tone 6 marks a place this review expects a failed look; every 'may look here' is assumed, to be tested.", "'Covered' cells take the app's tone; each 'may look here' marks a place this review expects a failed look, and every one is assumed, to be tested."),
 ('courses/ux/IA4-*', '{"mark": "tone 5", "means": "a catalogue term, shared across surfaces", "tone": 5}', '{"mark": "term", "means": "a catalogue term, shared across surfaces", "tone": 5}'),
 ('courses/ux/IA4-*', '{"mark": "tone 3", "means": "a cross-listing in the app, assumed", "tone": 3}', '{"mark": "also listed", "means": "a cross-listing in the app, assumed", "tone": 3}'),
 ('courses/ux/IA4-*', 'Rows tone 5, shared terms; tone 3 marks a cross-listing shown in the app, assumed and untested (IA3, section 3.3; rule R6).', "Each row's cells give the item's shared catalogue terms; a filled cell in the last column is a cross-listing shown in the app, assumed and untested (IA3, section 3.3; rule R6)."),
 ('courses/greece/6.7-*', '"label": "Generals wear diadems (by 306–305)"', '"label": "Generals wear diadems, by 306–305"'),
]
for g, old, new in E:
    f = next(R.glob(g)); s = f.read_text()
    n = s.count(old)
    if n != 1: sys.exit(f'{f}: {n} matches for {old[:60]!r}')
    blocks = [m.span() for m in re.finditer(r'```viz\n.*?```', s, re.S)]
    i = s.index(old)
    if not any(a <= i < b for a, b in blocks): sys.exit(f'{f}: {old[:60]!r} is not inside a viz block')
    f.write_text(s.replace(old, new)); print('ok', f.name, old[:50])
