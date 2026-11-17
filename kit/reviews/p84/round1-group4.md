# p84-4 figure re-check (P84 timeline spans)

Checker: claude-opus-5-5. 17 figures. PASS 13, FIX 4.

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-1.1 fig 1 (m11) | PASS | All five spans match the table (3100–1900, 1900–1700, 1700–1450, 1450–1300, 1300–1050), Evans phases in brackets as the caption says. Minor: at 390 px the Postpalatial and Final Palatial labels sit left of their bars and scroll in before the bars; their years make them readable. |
| greece/r-10.3 fig 2 (m103) | FIX | The Phrygian-cap span prints "480–401 BC"; 401 is not in the text (see below). The rest is right: sixth century 600–500, fourth century 400–300, events after 480, c. 424, 415. Minor: "Sixth century: Trojans drawn as hoplites" sits to the right of its bar, under the 480–401 bar; at 390 px frame 1 the 480–401 label sits over the sixth-century bar. Both resolve once scrolled. |
| greece/r-11.6 fig 1 (m116) | PASS | Spans 329–327, 327–326, 326–325, 325–324 and events 330 and spring 329 match the table. Minor: the Swat/Punjab and Indus labels sit beside their bars, over the next span's range; they carry their years, and the plates hide the guides behind them. |
| greece/r-12.8 fig 2 (m128) | PASS | Timon c. 320–230, Arcesilaus c. 316–241, Carneades 214/13–129/8, Philo 159/8–84/3; events c. 268, 155, 110/09, 88. All are in the text. Minor: span labels are drawn as written, without "BC", while event labels carry it. |
| greece/r-12.8 fig 4 (m128) | PASS | Plotinus 204/5–270, Porphyry c. 234–c. 305, Iamblichus c. 245–c. 325, Proclus 412–485; events AD 200 (a guess), 415, 529, 532, after 565. All match the text. Minor: the dashed guides of the Iamblichus and Porphyry bars pass across the lower bars, but they cross no text. |
| greece/r-6.1 fig 1 (m61) | PASS | Cambyses 530–522 and Darius 522–486. Events c. 550, c. 546, 539, by 500 and 490 match the text. |
| greece/r-6.6 fig 1 (m66) | PASS | The Thirty 404–403, Corinthian War 395–387, Olynthian campaign 382–379; Spartan hegemony 404–371 (from 404, ended by Leuctra, as the text says); all events match. At 320 and 390 px the plates hide the guides behind them. |
| greece/r-6.6 fig 3 (m66) | FIX | Renderer: the end guide of the Third Sacred War (346) is drawn over Philip's bar and through its label, between "359" and "336" (visible at 1280 px and 390 px). Spans 359–336 and 356–346 and all events are right. |
| greece/r-8.4 fig 2 (m84) | FIX | The relief span prints "Family-group reliefs (from c. 430), 430–317 BC": the start is given twice and the second time without the c. "Stelai almost vanish (c. 500–430)" and the events 394/3 and 317 are right. Minor: the vanish label sits beside its bar, under the reliefs bar; its years make it readable. |
| personal-brand-pb/read-dd-pb1 fig 2 | FIX | The span label "Anderson: pilot job, 2016–2020" names the wrong thing: the bar is the period when he ran the channel and the pilot job together (Sep 2016 to Mar 2020, as the caption says and §6 gives), not the pilot job, which began before it. All events match the text (Aug 2012, about Jan 2014, by 11 Nov 2015, 19 Sep 2016, 20 Jun 2017, Mar 2020, 5 Aug 2020, Sep 2020, 18 Mar 2021, 9 Apr 2023, 4 Jun 2025). |
| rome/r-1.1 fig 1 (rm11) | PASS | Terramare 1650–1150, Proto-Villanovan 1200–950, Villanovan 900–720, as the text gives them. Minor: at 390 px the upper-lane labels sit over the lower bars; their years make them readable. |
| rome/r-11.4 fig 2 (rm114) | PASS | Perusine war 41–40 ("siege lines round Perusia in 41–40"); all 15 events are where the text dates them. |
| rome/r-12.4 fig 4 (rm124) | PASS | Augustine's Confessions about 397–400 and Marlowe's Dido probably written 1587–1593 are spans; the events match the text and the caption. Minor: the ticks read "AD 400/600/800" and then "1000/1200..." without AD. On phone the deep event-label stack leaves the early frames mostly empty. |
| rome/r-2.5 fig 2 (rm25) | PASS | Altars overturned 58–48 BC; all events match. Minor: "Pompeii quake" (AD 62) is cited to CIL X 846, which records the temple rebuilt after the quake. |
| rome/r-5.1 fig 2 (rm51) | PASS | Gaius tribune 123–122 ("Tribune for 123 and 122"); events 137, 133, 129, 125, 122, 121, 120 match. |
| rome/r-7.2 fig 2 (rm72) | PASS | Masada falls 73 or 74 and Circus arch 80–81 are spans; the events 66, 67, 70, 71 match. Minor: both are uncertain or short dates drawn as bars, and their labels say so. |
| rome/r-7.2 fig 3 (rm72) | PASS | Vespasian 69–79, Titus 79–81, Domitian 81–96; the events 73 (censor 73–74), 80, 83, 85, 89, 96 match. Minor: the Titus label sits beside its short bar, under Domitian's; its years make it readable. |

## FIX 1 — greece/r-10.3 fig 2 (m103)

Declaration, the Phrygian-cap span: change its "date" end from 401 to 400 (`"480–401"` → `"480–400"`). The label then prints "After the Persian Wars: Paris in Phrygian cap, 480–400 BC". The text gives the start (after 480) and says that "by the fourth century" the cap was a uniform; 400 is the boundary the fourth-century bar already uses, and 401 appears nowhere in the text. If the renderer needs the bars to differ, keep the end and change the label instead, to one that names both ends in the text's words: "After the Persian Wars to the fourth century: Paris in Phrygian cap".

## FIX 2 — greece/r-6.6 fig 3 (m66)

Renderer: a bar's dashed end guide drops to the axis straight through any bar in a lower lane, and through that bar's label. A guide must pass behind lower-lane bars, or break where it crosses them, so that it never crosses another bar's label. Here the 346 guide of the Third Sacred War (lane 1) cuts through "PHILIP'S REIGN, 359–336 BC" (lane 0). The same fix tidies the guides that cross bars without touching text in m128 fig 4 and rm11 fig 1. No declaration change.

## FIX 3 — greece/r-8.4 fig 2 (m84)

Declaration, the relief span's label: `"Family-group reliefs (from c. 430)"` → `"Family-group reliefs, c. 430–317"`. A label that names both ends is drawn as written, as "Arcesilaus, c. 316–241" is in m128. That removes the doubled 430 and keeps the c. that the text and caption ask for.

## FIX 4 — personal-brand-pb/read-dd-pb1 fig 2

Declaration, the Anderson span's label: `"Anderson: pilot job"` → `"Anderson: channel and pilot job, Sep 2016–Mar 2020"`, which names both ends as the caption and §6 date them. If the renderer does not take month-year ends as naming both ends, use `"Anderson: channel and pilot job together"`, which prints with ", 2016–2020" appended.

## Sheets opened

- m11: desktop light, desktop dark, phone (390) light
- m103: desktop light, desktop dark, phone light
- m116: desktop light and dark, phone light
- m128 fig 2: desktop light and dark, phone light
- m128 fig 4: desktop light and dark, phone light
- m61: desktop light and dark, phone light
- m66 fig 1: desktop light and dark, phone light (one frame zoomed), phone320 light
- m66 fig 3: desktop light and dark (zoomed), phone light (zoomed)
- m84: desktop light and dark, phone light
- read-dd-pb1: desktop light and dark, phone light, phone320 dark
- rm11: desktop light and dark, phone light
- rm114: desktop light and dark, phone light (frame 4 zoomed)
- rm124: desktop light and dark (both frames zoomed), phone light (frames 1, 3 and 4)
- rm25: desktop light and dark, phone light
- rm51: desktop light and dark, phone light
- rm72 fig 2: desktop light and dark, phone light
- rm72 fig 3: desktop light and dark, phone light

Phone dark and most 320 px sheets were not opened: nothing at 390 px light was marginal enough to need them, except where listed.
