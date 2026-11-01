# Rome 12.4 (Aeneid 4, Dido): figure check 3

Material: `text.txt`, `captions.md`, and the six figure 4 images (desktop dark and light; phone frames 1 and 2, dark and light). Only figure 4 was checked.

## Figure 4 (timeline): FIX

### Trace of the drawing

Axis ticks (measured on the desktop render): AD 400 at x 76.8, AD 800 at 244.0, 1200 at 410.8, 1600 at 577.7, 1900 at 702.8, which gives a linear scale of 0.4173 px a year. Dot centres turned back into years using that scale:

| Item in figure | Date label | Text ("Dido after Virgil") | Dot centre → year | Result |
|---|---|---|---|---|
| Augustine, Confessions | about 397–400 | "The Confessions (about 397–400)"; Dido at 1.13.20–21 | x 76 → ~398 (397 would be x 75.6, less than a pixel away) | OK |
| Dante, Inferno 5 | early fourteenth century | "In the second circle of the Inferno, written in the early fourteenth century"; Dido at 5.61–62, also 5.85 | x 457 → **~1310** (1300 would be x 452.5) | **Wrong position** |
| Marlowe's Dido printed | 1594 | "printed in 1594" | x 575 → ~1594 | OK |
| Dido and Aeneas at Chelsea (traditional date) | 1689 | "usually dated 1689, though a letter of 1688 already links the opera to the school"; "The traditional account … makes the opera a school piece of 1689" | x 615 → ~1689.5 | OK; "(traditional date)" keeps the text's qualifier |
| Les Troyens à Carthage staged | 1863 | "staged … as Les Troyens à Carthage at the Théâtre-Lyrique in 1863" | x 687.5 → ~1863 | OK |

The dark render gives the same positions (Dante x 457 → ~1311).

- Every name and date in the figure appears in the text. No label says more than the text does: "Inferno 5" matches the canto the text cites, "printed" and "staged" are the text's own verbs, and the Purcell label keeps the hedge.
- Items run in the text's order: Augustine, Dante, Marlowe, Purcell, Berlioz. Ovid is undated in the section and correctly left out. The other dates in the section are not drawn, and the caption limits itself to "the items drawn", so leaving them out is consistent. Those dates are Marlowe's probable writing in 1587–1593, Berlioz's libretto (1856), score (1858) and Karlsruhe staging (1890), and Pinnock and Wood's 1684.
- A timeline is the right kind of figure for five dated works.
- Legibility: nothing is clipped or overlapping in either theme, on desktop or on phone. The two phone frames together cover the whole width under the scroll rule. The 1689 label block ends above the 1863 label, and the 1863 leader line runs clear of the 1689 text. Both themes have enough contrast.

### Trace of the caption

- "Dido's reception from Augustine to Berlioz": matches the first and last items.
- "the Confessions (about 397–400)", "the Inferno (early fourteenth century)", "the printing of Marlowe's Dido (1594)": correct against the text.
- "the 1689 usually given for the Chelsea performance of Purcell's opera, drawn as the traditional date since the text adds that a letter of 1688 already links the opera to the school": correct, and it matches the label.
- "the staging of Les Troyens à Carthage at the Théâtre-Lyrique in 1863": correct against the text.
- "Ovid's Heroides are undated there and not drawn": correct.
- "none of these dates carries a cited passage": true of the dates themselves. But the caption must name, item by item, the passage the text cites for each item. The text cites passages for two of the drawn items: Augustine's Dido at Confessions 1.13.20–21, and Dante's Dido at Inferno 5.61–62, with 5.85 for "the troop where Dido is". The Dante label also points straight at canto 5. The caption names neither passage. The text cites no passage for the Marlowe, Purcell or Berlioz items; it quotes Marlowe and Tate without line references.

### Faults and fixes

1. **Dante's dot is at about 1310, not at the start of the text's period.** The text gives only "early fourteenth century". Under the house rule a period is drawn from its first year, so the dot belongs at 1300 (about x 452.5 on the desktop render, roughly 4 px left of where it is now). 1310 is a year the text never gives. **Fix:** set the Dante item's year to 1300 in the figure data, keep the label "early fourteenth century", and rebuild.

2. **The caption leaves out the passages the text cites for two items.** **Fix:** replace "none of these dates carries a cited passage" with a sentence that goes item by item, for example: "the text cites Confessions 1.13.20–21 for Augustine's Dido and Inferno 5.61–62 (with 5.85) for Dante's; it gives no passage for the Marlowe, Purcell and Berlioz items, and none of the dates carries a cited passage."

### Note (renderer, not counted)

The axis label "1900" is right-aligned to its tick at x 703, so it sits directly above the 1863 dot at x 688. The tick itself and the "1863" label under the dot leave no doubt about the date, so this is not misleading. If the label's alignment at the axis end is ever changed, that change belongs to the renderer.
