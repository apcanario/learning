"""P84 round 1 FIXes applied to figure declarations as exact replacements (each current text must occur once in its
file). Usage: python3 apply_round1.py (from the repo root). Prose is never touched: every current text is inside a viz block."""
import pathlib, re, sys
R = pathlib.Path('.')
E = [
 ('courses/greece/3.3-*', '"label": "c. 570–510: Heracles outnumbers every other figure on Attic black-figure"', '"label": "Heracles leads Attic black-figure", "date": "c. 570–510 BC"'),
 ('courses/greece/3.3-*', '"label": "c. 510–500: Theseus cycle cups appear (Neils: earliest in the 520s)"', '"label": "Theseus cycle cups", "date": "c. 510–500 BC"'),
 ('courses/greece/3.3-*', '"label": "Bacchylides 17 and 18, probably 480s or 470s"', '"label": "Bacchylides 17 and 18", "date": "480s or 470s BC"'),
 ('courses/greece/3.3-*', '"label": "c. 440–430: Codrus Painter cup, BM E 84"', '"label": "Codrus Painter cup, BM E 84", "date": "c. 440–430 BC"'),
 ('courses/greece/12.7-*', 'A split year (334/3) is drawn at its first year and keeps its form in the label;', 'Split years (334/3, 331/0, 262/1, 230/29) are drawn at their first year and keep their form in the labels;'),
 ('courses/greece/6.5-*', '"label": "Macedon, tutor to Alexander (343/2)"', '"label": "Tutor to Alexander, 343/2–335/4 BC"'),
 ('courses/greece/6.5-*', '"label": "Lyceum (335/4)"', '"label": "Lyceum, 335/4–323 BC"'),
 ('courses/greece/6.5-*', '343/2 and 335/4 are drawn at their first year."', '343/2 and 335/4 are drawn at their first year. Assos, then Mytilene, which the text places between Plato\'s death and Macedon without dates of its own, is drawn from 347 to 343."'),
 ('courses/greece/3.5-*', '"label": "Sophocles\'s three Theban plays"', '"label": "Sophocles\'s three Theban plays", "date": "c. 442–401 BC"'),
 ('courses/greece/5.6-*', '"label": "Theognis, 6th c. (date uncertain)"', '"label": "Theognis, 6th c. (600–501 BC)"'),
 ('courses/greece/10.3-*', '{"from": -480, "to": -401, "label": "After the Persian Wars: Paris in Phrygian cap"', '{"from": -480, "to": -400, "label": "After the Persian Wars: Paris in Phrygian cap"'),
 ('courses/greece/8.4-*', '"label": "Family-group reliefs (from c. 430)"', '"label": "Family-group reliefs, c. 430–317"'),
 ('courses/greece/1.2-*', '"label": "LH I, high chronology (from c. 1700)"', '"label": "LH I, high chronology"'),
 ('courses/greece/7.3-*', '"ticks": [-282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271]', '"ticks": [-281, -280, -279, -278, -277, -276, -275, -274, -273, -272]'),
 ('courses/greece/7.3-*', '"ticks": [-280, -250, -200, -150, -100, -50, -30]', '"ticks": [-280, -250, -200, -150, -100, -50]'),
 ('courses/greece/10.10-*', '"label": "Troy VIIa (VIi)"', '"label": "Troy VIIa"'),
 ('courses/greece/10.5-*', '"label": "Cult appears (7th century)"', '"label": "Cult appears (7th century, 700–601 BC)"'),
 ('courses/greece/10.5-*', '"label": "Stele to Menelaus (5th century)"', '"label": "Stele to Menelaus (5th century, 500–401 BC)"'),
 ('courses/greece/5.3-*', '"label": "Chigi olpe: earliest clear picture of massed ranks (c. 650–640)"', '"label": "Chigi olpe (c. 650–640)"'),
 ('courses/greece/7.4-*', '"label": "Returned to the senate (44)"', '"label": "Returned to the senate"'),
 ('courses/rome/0.2-*', '"label": "Via Egnatia (c.)"', '"label": "Via Egnatia, c. 146–120 BC"'),
 ('courses/rome/4.4-*', '"label": "Viriathus"', '"label": "Viriathus\' war"'),
 ('courses/rome/6.4-*', '"label": "Bastarnae"', '"label": "Crassus against the Bastarnae"'),
 ('courses/rome/6.4-*', '"label": "Germanicus"', '"label": "Germanicus\' campaigns"'),
 ('courses/rome/0.3-*', '{"at": -1000, "label": "First graves in the Forum"}', '{"at": -1000, "date": "c. 1000 BC", "label": "First graves in the Forum"}'),
 ('courses/rome/0.3-*', '{"at": -451, "label": "Twelve Tables"}', '{"at": -451, "date": "451–450 BC", "label": "Twelve Tables"}'),
 ('courses/rome/0.3-*', '"label": "conquest, civil war"', '"label": "conquest and civil war"'),
 ('courses/rome/0.3-*', '"label": "crisis, late empire"', '"label": "crisis and late empire"'),
 ('courses/rome/0.3-*', '"label": "convention"', '"label": "convention", "date": "31 or 27 BC"'),
 ('courses/rome/13.8-*', '"label": "The book becomes a classic, seventeenth and eighteenth centuries"', '"label": "Becomes a classic, 17th–18th centuries"'),
 ('courses/rome/1.3-*', ' "start": -400,', ' "start": -400,\n "ticks": [-400, -300, -200, -100],'),
 ('courses/rome/1.4-*', '"label": "Ennius"', '"label": "Ennius\' Annales, 180s and 170s BC"'),
 ('courses/rome/1.4-*', '"label": "Livy (about)"', '"label": "Livy, about 27–25 BC"'),
 ('courses/rome/11.6-*', '"label": "Reddé and von Schnurbein"', '"label": "Reddé and von Schnurbein\'s excavations"'),
 ('courses/rome/9.3-*', '"label": "Spartacus"', '"label": "Spartacus\' war"'),
 ('courses/personal-brand/DD-PB1-*', '"label": "Anderson: pilot job"', '"label": "Anderson: channel and pilot job, Sep 2016–Mar 2020"'),
]
for g, old, new in E:
    f = next(R.glob(g)); s = f.read_text()
    n = s.count(old)
    if n != 1: sys.exit(f'{f}: {n} matches for {old[:60]!r}')
    blocks = [m.span() for m in re.finditer(r'```viz\n.*?```', s, re.S)]
    i = s.index(old)
    if not any(a <= i < b for a, b in blocks): sys.exit(f'{f}: {old[:60]!r} is not inside a viz block')
    f.write_text(s.replace(old, new)); print('ok', f.name, old[:50])
