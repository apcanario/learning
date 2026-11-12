Model: claude-opus-5-5

All 13 Rome figures pass; there are no FAILs. I could not save REPORT.md to /tmp/p98/recheck/rome/ because the write tool refused it ("Subagents should return findings as text"), so the report is here only.

Scope: the 13 Rome figures listed in FIGURES.txt (row P98 renderer change: compare and bars). For each I read where it sits in *-text.md, its line in *-captions.txt, and three frame sheets: 320 px in one theme, 390 px in the other theme, and 1280 px in one theme. I zoomed the 1280 px sheets for rm01, rm23, rm54 and rm94 to check where values sit against the track ends. I used only files in /tmp/p98/recheck/rome/ (plus scratch crops in /tmp/p98crop/).

| figure | 320 | 390 | 1280 | verdict | note |
|---|---|---|---|---|---|
| r-0.1 fig 1 (compare) | dark ok | light ok | dark ok | PASS | 5.5 / 3 / 7 / 8.5 centuries match l.14: "five and a half centuries … the first consuls three centuries … seven centuries after Romulus; Plutarch nearly eight and a half". On phones, 3 sits on its track and the others beyond. At 1280 px, 5.5 and 7 sit on the track and 8.5 beyond. |
| r-11.1 fig 3 (compare) | light ok | dark ok | light ok | PASS | 3,800 / 10,000 / 10,000 / 337,022 match l.85: "Comitium held some 3,600 to 3,800 … the Forum perhaps 10,000 … seldom exceeded 10,000, against a census of 337,022 citizens in 164". The three small values sit on the track; 337,022 sits beyond. |
| r-11.3 fig 3 (bars, stacked) | dark ok | light ok | dark ok | PASS | 12/6 = 18, 13/4 = 17, 13/3 = 16 match l.76: "thirty-eight votes to thirteen … senators twelve to six, equites thirteen to four, tribuni aerarii thirteen to three". The orders' sizes (eighteen, seventeen, sixteen) also match. Totals sit after the bars. |
| r-11.5 fig 1 (compare) | light ok | dark ok | dark ok | PASS | 435 / 426 / 27 / 26 letters and the date spans match the table at l.16–21. 435 and 426 sit beyond the track at every width; 27 and 26 sit on it. |
| r-11.6 fig 2 (bars, grouped) | dark ok | light ok | light ok | PASS | 368,000 and 300,000 match l.81 ("368,000 in all"; Plutarch "gives 300,000"). 80,000 matches l.67 "80,000 picked men". 258,000 matches l.69 "250,000 infantry and 8,000 cavalry, 258,000 in all". 170,000 and 300,000 match l.87. All values sit after their bars. |
| r-2.3 fig 3 (compare) | dark ok | light ok | dark ok | PASS | 304 / 355 / 445 / 365 days match l.67 ("304 days", "355 days") and l.69 ("gave 46 BC 445 days, then … a year of 365"). On phones every value sits beyond the track. At 1280 px, 304, 355 and 365 sit on the track and 445 beyond. |
| r-4.3 fig 2 (bars, stacked) | light ok | dark ok | dark ok | PASS | 50,000 + 9,000 = 59,000 matches l.30 "50,000 foot and 9,000 horse". 12,000 + 8,000 + 6,000 = 26,000 matches l.32 "12,000 African and 8,000 Iberian infantry and at most 6,000 cavalry". The totals match l.136 "about 59,000 … about 26,000", and the caption flags "at most". See minor 1. |
| r-4.3 fig 3 (bars, grouped) | dark ok | light ok | light ok | PASS | 80,000 / 6,000 against 40,000 / 10,000 matches l.50 "some 80,000 infantry and 6,000 cavalry against Hannibal's 40,000 foot and 10,000 horse". |
| r-5.4 fig 1 (compare) | light ok | dark ok | dark ok | PASS | 400,000 / 1,000,000 / 1,000,000 / 1,192,000 match l.38: "more than 400,000 … a million killed … a million killed … 1,192,000 killed". On phones, 400,000 sits on the track and the rest sit clear beyond its end. At 1280 px, 400,000 and both 1,000,000 values sit on the track and 1,192,000 beyond. |
| r-5.5 fig 3 (bars, grouped) | dark ok | light ok | dark ok | PASS | 500 / 250 (Plutarch) and 170 / 230 (Orosius) match l.73: "Antony 500 warships … Octavian's 250 warships … Orosius 6.19 gives Antony 170 ships against Octavian's 230". |
| r-8.3 fig 2 (bars, grouped) | light ok | dark ok | light ok | PASS | 90,000 / 8,000 against 170,000 / 18,000 matches l.24 "90,000 foot and 8,000 horse against Maxentius' 170,000 and 18,000 (2.15.1–2)". |
| r-9.2 fig 1 (compare) | dark ok | light ok | light ok | PASS | 1,200 three times, 600 and 300 match l.20 "1,200 each of velites, hastati and principes, and 600 triarii … 300 cavalry". 600 sits beyond the track on phones and on it at 1280 px. 300 sits on the track; the 1,200 values sit beyond. |
| r-9.4 fig 4 (bars, stacked) | light ok | dark ok | dark ok | PASS | 21 / 9 / 4 = 34 matches l.60 "thirty-four fights, twenty-one wins, nine draws and four reprieves". The total sits after the bar. |

Checks that hold for every figure:
- **Fit:** every sheet is "frame 1 of 1 (the whole figure fits)". At 320 and 390 px every bar and value is whole in the opening frame, and nothing scrolls, overlaps or is cut.
- **Track edges:** no value crosses the end of its grey track at any width checked.
- **Captions:** each says what the figure shows, which section it comes from, and its source.
- **Themes:** labels and values are legible in dark and light.

Minor (not faults):
1. minor: r-4.3 fig 2. At 320 and 390 px only the 50,000 segment has its value printed inside the bar. The 9,000, 12,000, 8,000 and 6,000 segments are unlabelled there, though 1280 px shows them. Nothing is cut, the totals are printed and the text gives every part.
2. minor: r-11.3 fig 3, r-9.4 fig 4 and r-4.3 fig 2 are stacked bars with no grey track. For them, check (d) only means the total sits after the bar, which holds.
3. minor: three labels are approximations, each explained in its caption:
   - r-0.1 fig 1: "8.5 centuries" stands for "nearly eight and a half".
   - r-11.1 fig 3: the Comitium bar uses 3,800, the upper end of 3,600–3,800.
   - r-5.4 fig 1: "Velleius (over)" stands for "more than 400,000".
