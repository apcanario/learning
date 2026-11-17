<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
PASS 11, FIX 1
FIX: greece/r-10.3 fig 2 (m103). The two century span labels have no "BC". Add it to the declaration; no renderer change.
Report: the harness refused the write to /home/claude/packets/r4-2/out/report.md, so the full report follows.

---

# Figure re-check r4-2 (round 4: P84 timelines)

Model: claude-opus-5-5

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-1.1 fig 1 (m11) | PASS | All five phases match the table, with Evans's phases in brackets and the dates c. 3100–1900, 1900–1700, 1700–1450, 1450–1300 and 1300–1050. The title carries the "c.". Labels carry their years, long labels break, dashed guides break at bars and plates, and gridlines run from the ticks. Readable at 1280, 390 and 320, dark and light. Minor: "Final Palatial (LM II – LM / IIIA2)" breaks inside the Evans phase name. A break before "(" would read better, but it is not needed. |
| greece/r-10.3 fig 2 (m103) | FIX | Two span labels name a century with no era: "Sixth century: …" and "Fourth century: …". The renderer correctly draws them as written, so the drawing shows no BC, unlike the century labels corrected this round. Everything else matches "Are the Trojans foreign?" and "Hecuba and Andromache after Troy" (480, c. 424, 415). Minor: the text does not state the 400 end of the "After the Persian Wars" span; it is inferred from "by the fourth century". Acceptable. |
| greece/r-11.8 fig 2 (m118) | PASS | 323 BC (from the astronomical diary), 321 BC, 48 BC, AD 215, the 270s and 390s spans, AD 365 and c. AD 390 all match the text. The decade labels are drawn as written. At 1280 the figure scrolls 972 px, and every label is whole in at least one frame. Minor: the 323 and 321 dots overlap by about half a dot. Both labels are staggered and readable. |
| greece/r-11.8 fig 3 (m118) | PASS | Every date matches "The modern Alexanders": Droysen 1833 and the 1836–1843 span, Tarn 1926 and 1948, Badian 1958, Lane Fox 1973, Green 1974, Bosworth 1988 and 1996, Worthington and Cartledge 2004. Minor: the 1973 and 1974 dots partly overlap. The labels are staggered and readable. |
| greece/r-4.3 fig 4 (m43) | PASS | Every vase and text matches its section: c. 670, c. 600, c. 570, 570–560, c. 540 (two items), c. 530, 520–470 (two spans), 500–470, c. 460, probably 440s, 431, c. 424, 415 and 409. "probably 440s" is drawn as written. The labels are staggered and readable at every width. |
| greece/r-5.3 fig 2 (m53) | PASS | The five tyrannies carry the table's dates in brackets. Pheidon is left out, as the caption says. At 320 the in-bar labels can each be read whole by scrolling. |
| greece/r-5.3 fig 4 (m53) | PASS | The c. 640–560 span, c. 600, c. 550 and from c. 515 match "Coinage from Lydia". At 320 the in-bar span label is whole in frame 2. |
| greece/r-7.4 fig 1 (m74) | PASS | 146 BC, 44 BC, 27 BC–AD 15, AD 15–44, AD 44–67 and AD 67 match the section. No year 0. Minor: at 320, "Returned to the senate, AD 44–67" is not whole in any of the captured frames. It is about 230 px wide, so it fits whole at a scroll position between frames 3 and 4. |
| rome/r-1.4 fig 1 (rm14) | PASS | 753, about 200 BC, the 180s and 170s BC span, the about 27–25 BC span, from 7 BC and about AD 100 match the text. The qualifiers now sit in the event dates. Gridlines break at the Livy label. |
| rome/r-11.8 fig 3 (rm118) | PASS | The six republics, 88–81, 59–53, 53–49, 49–44 and 43–33, and the events 180, 139 and 88 all match Flower's sequence, in order. 367/6 stays in the label and is drawn at 366, as the caption says. Minor: the "450 BC" tick label is pulled inward to stay in frame and sits close to "400 BC" at 1280 and 390. They do not overlap. |
| rome/r-3.1 fig 2 (rm31) | PASS | 449, 445, the 444–367 span, 443, 421, 409, 405 and 400 match the section and its Livy references. The in-bar label breaks onto two lines in a taller bar and is whole at 320 (frame 3). |
| viz-examples fig 19 | PASS | Every case in CHANGE behaves as specified:<br>– "Kings, 753–509 BC": years appended.<br>– "A reign, c. 670–640 BC": date after a comma.<br>– "Siege, 41–40" and "A decade (280s)": drawn as written.<br>– "A principate, 27 BC–AD 14": no year 0, and the tick at 1 reads "AD 1".<br>– The long label breaks onto three lines, with "4th century BC" whole on the last line.<br>– Guides and gridlines break at labels and bars.<br>Readable at every width. |

## FIX

### greece/r-10.3 fig 2 (m103): change the declaration

Change these two span labels:

- `"label": "Sixth century: Trojans drawn as hoplites"` → `"label": "Sixth century BC: Trojans drawn as hoplites"`
- `"label": "Fourth century: the cap a Trojan uniform"` → `"label": "Fourth century BC: the cap a Trojan uniform"`

No renderer change is needed.

## Not in this packet

There was nothing to check for two items in CHANGE: no Greek 1.2 figure 3 (the "1952" ascender check) and no matrix (P109) figures.

## Sheets opened (all under /home/claude/packets/r4-2/sheets/)

- **Desktop 1280, dark and light:** all 12 figures. Also zoomed crops of rm14, rm31, viz-examples, and m118 fig 2 frames 1 and 4.
- **Phone 390, light:** every frame of all 12 figures.
- **Phone 320, light:** m11, m53 fig 2, m53 fig 4, m74, rm14, rm31 and viz-examples.
- **Phone 390, dark:** a check of all 12 figures together; nothing differed from light.
- **Phone 320, dark:** not opened. The 320 light sheets showed nothing marginal that dark mode would change.

My crops were written only to /tmp/crops; nothing was published and nothing was written outside the packet.
