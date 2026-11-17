# p84-2 figure re-check (P84 timeline spans)

Checker: claude-opus-5-5. Read: figures.md, text/*.md around each marker and the sections each caption names, and the sheets listed at the end. Nothing outside the packet was opened.

## Verdicts

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-0.1 fig 1 (m01) | FIX | Spans, years and events match "Material sources" and "The archaic poets" (Knossos c. 1400–1370, tomb cult 8th c. = 800–701, Homer c. 750–700; Troy VI c. 1300, Alaksandu c. 1280, 1209/8, Pylos c. 1200, VIIa c. 1180). CHANGE does what it says. Label "Tomb cult at Mycenaean graves (8th c. BC), 800–701 BC" (52 chars) is longer than the visible frame at 390 and 320, so no scroll position shows it whole (R2), and it says the century twice. |
| greece/r-0.1 fig 2 (m01) | FIX | Every span matches the text (Homeric Hymns 7th–5th c. = 700–401, Aristarchus 2nd c. BC = 200–101, Apollodorus 1st or 2nd c. AD = AD 1–200, Hyginus 2nd c. AD or later = AD 101–200, Pausanias c. AD 150–180, Plutarch c. AD 45–120, the tragedians, historians and Pindar as given). Guides pass behind label plates correctly. Labels for Homer (55 chars), Pausanias (49), Apollodorus (48), Aristarchus (48) and Hyginus (46) are wider than the visible frame at 320, and Homer and Pausanias at 390 too, so they cannot be read whole (R2). Minor: Hyginus' "or later" end is drawn closed at AD 200. The label keeps "or later", so this is acceptable. |
| greece/r-11.1 fig 1 (m111) | PASS | Archelaus c. 413–399, Amyntas III 393–370/69 (drawn to 370), Philip at Thebes about 368–365, and the five table events all match. Readable at every width. |
| greece/r-12.7 fig 1 (m127) | FIX | All years match the table. But Cleanthes 331/0–230/29 and Diogenes of Babylon c. 230–c. 150 share lane 1 in the same tone, abutting at 230, so they draw as one bar from 331 to 150 labelled "Cleanthes" inside, with Diogenes' label hanging off its right end. This happens at every width and in both themes (R1). The caption names only one split year, but four are drawn at their first year. |
| greece/r-3.4 fig 1 (m34) | FIX | 462 BC, 250 BC (mid third century, caption says so) and Valerius Flaccus c. AD 70–90 all match. The bar sits on the axis correctly. Label "Valerius Flaccus, Argonautica (c. AD 70–90)" (43 chars) is never whole at 320 (R2). It is fine at 390 and 1280. |
| greece/r-5.5 fig 3 (m55) | FIX | Events and spans match (Peisistratus from the third attempt c. 546 to death 527/6, Hippias 527/6 to 511/10, drawn at first years as the caption says; 632, 621/0, 594/3, 566/5, 561/0, 514, 508/7, 506, 501/0, 487). Label "Peisistratus rules after the third attempt, 546–527 BC" (54 chars) is never whole at 320 or 390 (R2). Minor: the Peisistratus and Hippias bars abut in one lane at 527. They are told apart by two tones and by labels on opposite sides, so this is readable. R1 would separate them anyway. |
| greece/r-6.5 fig 1 (m65) | PASS | All five Sophists match the table, Antiphon is omitted as the caption says, and the in-bar labels are drawn as written ("to" form). Readable at all widths. |
| greece/r-6.5 fig 3 (m65) | FIX | The years match "Aristotle" (born 384, Academy 367–347, Macedon from 343/2, Lyceum 335/4 to 323, Chalcis 323–322, dies 322). The labels repeat their own start year, as in "Lyceum (335/4), 335–323 BC" and "Macedon, tutor to Alexander (343/2), 343–335 BC". The Macedon label is never whole at 320. The span "Assos, then Mytilene, 347–343" is not in the caption: the text gives no dates for it and orders it between Plato's death and 343/2. |
| greece/r-8.2 fig 1 (m82) | PASS | The four wars match the table: c. 595–585, c. 449–447, 356–346 and 339–338. Minor: the Fourth War (one year) draws as a hairline bar but is visible at all widths. Minor: "First Sacred War" is labelled in full while the others read only "Second", "Third" and "Fourth". This is acceptable. |
| greece/r-9.2 fig 1 (m92) | PASS | Parthenon 447–438, Propylaea 437–432, Nike temple c. 427–424 and Erechtheion c. 421–406 match, as do the events 480, c. 449/8 and 438. Minor: the Propylaea label (39 chars) is at the limit at 320. |
| rome/r-0.2 fig 1 (rm02) | FIX | All roads and colonies match. The Via Egnatia label prints as "Via Egnatia (c.), 146–120 BC": the "c." is stranded in brackets ahead of the years it qualifies. |
| rome/r-0.2 fig 2 (rm02) | PASS | All provinces match the list. Caesar's Gaul 58–50 is drawn as a span. Desktop also scrolls, and every label is whole in some frame. |
| rome/r-0.2 fig 3 (rm02) | PASS | Caesar at the Rhine 58–55, Carrhae 53, the standards 20, AD 9, AD 14 and AD 117 all match. |
| rome/r-13.7 fig 3 (rm137) | PASS | Heir 138–161, with Lucius 161–169, away from Rome 169–176 and the second expedition 178–180 match, as do all events. Minor: heir and with-Lucius abut in lane 0 but are in two tones with separate labels. R1 would separate them. |
| rome/r-4.4 fig 3 (rm44) | FIX | The span 147–139 is Viriathus' war (from 147 he "beat a series of praetors", and he was killed in 139), but the label "Viriathus, 147–139 BC" reads as his lifespan. All events match. |
| rome/r-6.4 fig 1 (rm64) | FIX | Cantabrian War 26–19 and Pannonia conquered 12–9 match. "Bastarnae, 29–28 BC" names a people and reads as their dates. The span is Crassus' campaign against them (Dio 51.24). |
| rome/r-6.4 fig 2 (rm64) | FIX | Drusus beyond the Rhine 12–9 and all events match. "Germanicus, AD 14–16" reads as Germanicus' lifespan. The text dates his campaigns ("Germanicus' campaigns of AD 14–16"). |

Counts: PASS 7, FIX 10.

## Fixes

### R1 (renderer): two spans that touch must not share a lane
The lane packer puts a span in a lane when its start is at or after the previous span's end. When the end of one span equals the start of the next (230 in m127, 527 in m55, 161 in rm137, 347 in m65 fig 3), the two bars join into one block. When they share a tone (m127: Cleanthes and Diogenes of Babylon, both blue), they read as one period under one label. Change: treat spans as overlapping unless the gap between them is at least the minimum label gap in pixels (or simply when end >= next start). Spans that touch then go to separate lanes. If a lane must be shared, leave a visible gap of at least 4 px between the bars. Applies to m127 (required), and also changes m55, m65 fig 3 and rm137 (currently readable).

### R2 (renderer): a side label wider than the visible frame must wrap
At 320 px (about 250 px clear between the edge fades) a mono side label of more than about 38 characters can never be seen whole at any scroll position. At 390 px the limit is about 48 characters. These limits are worked out from the sheets' character widths. The frames are samples, so a label near the limit may fit between two frames. Change: when a span's side label (the plate beside its bar) is wider than the frame's clear width at the rendered width, break it onto two lines on the plate. The label text goes on the first line and the years on the second (break at the last ", " before the years, or at the last space that fits). Grow the lane height for that lane only. Applies to m01 fig 1, m01 fig 2, m34 fig 1, m55 fig 3 and m65 fig 3 (the last is also covered by its label changes below).

### greece/r-0.1 fig 1 (m01)
- R2.
- Span label: "Tomb cult at Mycenaean graves (8th c. BC)" → "Tomb cult at Mycenaean graves (8th c.)". It then prints as "Tomb cult at Mycenaean graves (8th c.), 800–701 BC". If the renderer treats the century as naming both ends, it prints as written.

### greece/r-0.1 fig 2 (m01)
- R2. If R2 is not taken, shorten the labels in the declaration:
  - "Homer, Iliad and Odyssey (conventionally c. 750–700 BC)" → "Homer (conventionally c. 750–700 BC)"
  - "Pausanias, Description of Greece (c. AD 150–180)" → "Pausanias (c. AD 150–180)"
  - "Apollodorus, Library (1st or 2nd c. AD)" → "Apollodorus' Library (1st or 2nd c. AD)"
  - "Aristarchus, editor of Homer (2nd c. BC)" → "Aristarchus (2nd c. BC)"
  - "Hyginus, Fabulae (2nd c. AD or later)" → "Hyginus (2nd c. AD or later)"

### greece/r-12.7 fig 1 (m127)
- R1.
- Caption: replace "A split year (334/3) is drawn at its first year and keeps its form in the label;" with "Split years (334/3, 331/0, 262/1, 230/29) are drawn at their first year and keep their form in the labels;".

### greece/r-3.4 fig 1 (m34)
- R2. If R2 is not taken: span label "Valerius Flaccus, Argonautica (c. AD 70–90)" → "Valerius Flaccus (c. AD 70–90)".

### greece/r-5.5 fig 3 (m55)
- R2. If R2 is not taken: span label "Peisistratus rules after the third attempt" → "Peisistratus, third rule". It then prints as "Peisistratus, third rule, 546–527 BC".

### greece/r-6.5 fig 3 (m65)
- Span label "Macedon, tutor to Alexander (343/2)" → "Tutor to Alexander, 343/2–335/4 BC". This names both ends, so it is drawn as written.
- Span label "Lyceum (335/4)" → "Lyceum, 335/4–323 BC".
- Caption: add after "...drawn at their first year.": "Assos, then Mytilene, which the text places between Plato's death and Macedon without dates of its own, is drawn from 347 to 343."

### rome/r-0.2 fig 1 (rm02)
- Span label "Via Egnatia (c.)" → "Via Egnatia, c. 146–120 BC". This names both ends, so it is drawn as written.

### rome/r-4.4 fig 3 (rm44)
- Span label "Viriathus" → "Viriathus' war". It prints as "Viriathus' war, 147–139 BC".

### rome/r-6.4 fig 1 (rm64)
- Span label "Bastarnae" → "Crassus against the Bastarnae". It prints as "Crassus against the Bastarnae, 29–28 BC".

### rome/r-6.4 fig 2 (rm64)
- Span label "Germanicus" → "Germanicus' campaigns". It prints as "Germanicus' campaigns, AD 14–16".

## Sheets opened
For every one of the 17 figures I opened the desktop (1280) light and dark sheets and the phone (390) light sheet in full, every frame. I also opened these:
- phone (390) dark: m127 fig 1.
- 320 light, every frame: m01 fig 2 and m55 fig 3.
- 320 light, the drawing area of every frame: m34 fig 1, m65 fig 3, m92 fig 1 and m01 fig 1.
- zoomed desktop crops: m01 fig 2 (guides and plates), m127 (lane 1), m34 (Valerius bar) and rm137 (top lanes).
