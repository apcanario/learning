# Rome 13.5 (Seneca): figure check 3, figure 1

Checked from `text.txt`, `captions.md` and the six PNGs only: desktop dark and light, phone frames 1–2 dark and light. Figure 2 was not in the material and is not checked.

## Figure 1 (timeline): FIX

### Trace: events

| Figure label | Text | Result |
|---|---|---|
| c. 4–1 BC · Born at Corduba (modern estimate) | "born at Corduba … some time between about 4 and 1 BC; no ancient source gives the year, and modern estimates are inferences" (§1) | OK. "c." carries "about"; the range is drawn on its first year (house rule). |
| about 31 · Return from Egypt (modern dating) | "Modern biographers … date his return to that voyage, about 31; Seneca says neither outright" (§2; voyage at Helvia 19.4–7) | OK |
| AD 39 · Nearly killed by Gaius (Dio) | "that nearly killed him … (Dio 59.19.7–8, under 39)" (§2) | OK. "(Dio)" shows whose dating it is. |
| October 54 · Nero emperor | "When Nero succeeded in October 54" (§4, no passage for the date) | OK |
| AD 56 · Suffect consul | "Seneca was suffect consul in 56." (§4, no passage) | OK |
| AD 58 · Suillius' attack | "In 58 … Publius Suillius … attacked Seneca openly … (Annals 13.42)" (§5) | OK |
| March 59 · Agrippina killed | "In March 59, when the collapsing boat had failed, Nero summoned the two men … (Annals 14.7)"; the letter "afterwards" (14.11.3); "the murder" (Dio 61.12.1); "After killing his mother" (15.62) | OK. The text dates the killing and calls it a murder, though it does not narrate the killing itself. |
| AD 64 · Second request to retire | "After the fire of 64 he asked again to retire … (15.45.3)" (§6) | OK |
| AD 65 · Death at his villa | "found him at a villa four miles from Rome" (15.60–61, death section) | **Fault.** The text says "a villa" and never says the villa was Seneca's. "his" is a claim the text does not make. |

### Trace: spans

| Span label | Text | Result |
|---|---|---|
| CORSICA, 41–49 | Heading "Corsica, 41–49"; exiled "within months of Claudius' accession in 41" (Dio 60.8.5); recalled "In 49" (Annals 12.8.2); "eight years there" | OK. Drawn from the AD 41 tick to the AD 49 tick. |
| TUTOR AND MINISTER, 49–62 | Recall and tutorship 49 (Annals 12.8.2); heading "Tutor and minister"; "Burrus died in 62, and with him … Seneca's power broke" (14.52) | OK |
| WITHDRAWAL, 62–65 | Heading "Withdrawal, 62–65" (14.52–56, 15.45) | OK |

Each span label carries its years, so it reads as a period.

### Caption

- "first six sections": the text has 13 "## " sections. The first six are Corduba, Illness, Corsica, Tutor and minister, The fortune, and Withdrawal, and every dated item in the figure comes from them or from "The death in 65". Nothing in the figure comes from "The works". The count is correct.
- The caption names a passage for each item, and each matches the text: birth (modern estimate, no ancient source); Egypt (after Helvia 19; the text cites 19.2 and 19.4–7); Gaius (Dio 59.19.7–8); exile (Dio 60.8.5); recall and tutorship (Annals 12.8; text 12.8.2); Suillius (13.42); Agrippina (14.7–11; text 14.7, 14.11.3); withdrawal (14.52–56; 15.45, which covers the AD 64 second request); death (15.60–64).
- The caption says the October 54 accession and the consulship of 56 are given without a passage. That is correct: these are the only drawn dates the text gives with no passage.
- The caption claims nothing that the figure does not show.

### Positions and legibility

- From pixel measurement of the desktop render, the scale is 9 px per year. Events from AD 31 on sit on their years to within 1 px, and the spans start and end on the 41, 49, 62 and 65 positions.
- Both themes are legible. No label is clipped, and none overlaps another label or a leader line. The leaders at 56, 58, 59, 64 and 65 pass clear of the labels to their left. Bar colours and dots read on both backgrounds.
- Phone frames 1–2 together cover the whole figure and caption with overlap. The sideways scroll is a house rule.
- Note (renderer, not counted against the figure): the "1 BC" tick sits 98 px left of AD 10 where 90 px would be expected. The scale counts a year 0, so the 1 BC tick and the birth dot sit one year (about 9 px) too far left relative to the AD dates. On a "c. 4–1 BC" estimate this cannot mislead a reader. Whoever maintains the timeline renderer should apply a BC year-zero correction (BC year y → y + 1 before scaling).

### Fix

Change the last event's label from "Death at his villa" to **"Death at a villa"**, which is the text's wording ("found him at a villa four miles from Rome"). Alternatively, add to the text that the villa was his own (Tacitus' *suburbano rure*) with its passage. No other change is needed.
