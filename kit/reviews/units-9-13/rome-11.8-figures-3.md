# Rome 11.8, Why the Republic fell: figure check, figure 3

Checked from `text.txt`, `captions.md` and the six images of figure 3 (desktop dark and light; phone frames 1 and 2, dark and light). Figures 1 and 2 not checked.

## Figure 3 (timeline): FIX

The dates and positions are correct, and so are the three markers. Two span labels need changing: one leaves out what the caption claims for it, and one does not use the text's wording. There is also one contrast note for the renderer (below), which is not part of this FIX.

### Trace: spans (all from "Flower: which republic fell?", text para. 61)

| Label in figure | Text | Bar position (desktop, 300 BC = x68, 50 BC = x656, 2.352 px/yr) | Result |
|---|---|---|---|
| THIRD REPUBLIC (NOBLES), 300–180 | "The third, fourth and fifth are the republics of the nobles: 300 to 180, …" | x68–350 (300–180) | OK |
| FOURTH REPUBLIC (NOBLES), 180–139 | "… 180 to 139 …" | x350–446 (180–139) | OK |
| FIFTH REPUBLIC (NOBLES), 139–88 | "… and 139 to 88" | x447–566 (139–88) | OK |
| REPUBLICAN GOVERNMENT CEASED, 88–81 | "From 88 to 81 republican government ceased." | x567–582 (88–81) | OK, in the text's words |
| SULLA'S REPUBLIC, 81–60 | "The sixth republic was Sulla's, from 81 to 60" | x583–632 (81–60) | **Fault 1** |
| ALLIANCE OF THREE, 59–53 | "the alliance of Pompey, Crassus and Caesar from 59 to 53" | x635–648 (59–53) | **Fault 2** |
| TRANSITION, 53–49 | "a transition from 53 to 49" | x649–657 (53–49) | OK |
| CAESAR'S DICTATORSHIP, 49–44 | "Caesar's dictatorship from 49 to 44" | x659–669 (49–44) | OK |
| TRIUMVIRATE, 43–33 | "the triumvirate from 43 to 33" | x673–695 (43–33) | OK |

Every span label includes its years, so each one reads as a period. The axis is marked BC.

### Trace: markers

| Marker | Text | Position | Result |
|---|---|---|---|
| 180 BC, Law fixing the ladder of office | "the law of 180 that fixed the ladder of office" (deep dive module 11.1) | x350 | OK |
| 139 BC, Ballot law | "the ballot law of 139" (deep dive module 11.1) | x447 | OK |
| 88 BC, Sulla marches on Rome | "ends the republic of the nobles with Sulla's march in 88" (module 0.3); "when a consul first led a Roman army against Rome" (para. 65) | x566 | OK |

### Trace: caption

- "The later part of Harriet Flower's sequence of republics, 300 to 33 BC": the figure begins at the third republic and leaves out the pre-republican period, the proto-republic and the first two republics. This is correct.
- "from the section Flower: which republic fell?, after Flower, Roman Republics (2010)": correct.
- "her third, fourth and fifth republics, the republics of the nobles, divided at the law of 180 … and the ballot law of 139 (deep dive module 11.1)": correct, and the module cited is the one the text cites.
- "the end of the republic of the nobles with Sulla's march in 88, which module 0.3 records": correct (text para. 61).
- "the years 88 to 81, when republican government ceased": correct.
- "Sulla's republic, the sixth, from 81 to 60": this matches the text, but the figure does not show "the sixth" (see Fault 1).
- "the alliance of Pompey, Crassus and Caesar (59–53), the transition (53–49), Caesar's dictatorship (49–44) and the triumvirate (43–33), which she counts as no republic": this matches "After it came no republic at all". The figure shows these four spans. It shows them as unnumbered, set apart from numbered republics, only once Fault 1 is fixed.
- "The text gives all these dates from Flower without a passage or page": correct. Para. 61 gives no passage or page.

### Faults and fixes

1. **The Sulla span leaves out "sixth".** The three republics of the nobles are labelled by number, but Sulla's is not. So the figure does not show that it is Flower's sixth republic, which the caption claims ("Sulla's republic, the sixth"). It also does not show that it is the last span she counts as a republic. The text says: "The sixth republic was Sulla's".
   **Fix:** relabel the span `SIXTH REPUBLIC (SULLA'S), 81–60`. The four spans after it then show as unnumbered, next to numbered republics, so the caption's "which she counts as no republic" is something the figure shows.

2. **"ALLIANCE OF THREE" does not use the text's wording.** The label restates "the alliance of Pompey, Crassus and Caesar" but replaces the names with a count.
   **Fix:** relabel the span `ALLIANCE OF POMPEY, CRASSUS AND CAESAR, 59–53`. At the label size used (about 6.8 px per character, measured on the fifth-republic label), this is about 300 px of right-aligned text ending at x≈628. It fits in the empty space to the left of the bar, with nothing above or below it to overlap.

### Readability, both themes

- Desktop, dark and light: nothing is clipped or overlapping. The labels of adjacent spans sit on separate rows. The marker labels (180, 139, 88) do not run into each other; "of office" wraps under its marker. Outside-bar labels against the background: about 6.7:1 (dark) and 8.0:1 (light). Marker labels: about 15.8:1 (dark) and 17.9:1 (light).
- Phone frames: frame 1 covers x0–390 and frame 2 covers about x374–764, so every element appears whole in at least one frame. The labels cut at the frame edges are the house rule on sideways scrolling, not a fault. In both themes the caption is cut at the frame's right edge and is read by scrolling, which is also a house rule.
- Colour carries no meaning (there is no legend). Note that it repeats across categories: the transition uses the same blue as "republican government ceased", Caesar's dictatorship the same red as the third republic, and the triumvirate the same orange as the fourth republic. With the labels this does not mislead, and nothing needs to change.

### RENDERER note (not counted in the FIX)

In the light theme, the label inside the third-republic bar is white text (255,255,255) on red (203,88,88), a contrast of about 4.1:1. That is legible but below 4.5:1, the usual minimum for small text. In the dark theme the same label is dark text on (219,93,94), about 5.4:1, which passes. The colour of in-bar text and of the bar both come from the theme or renderer, so this can only be fixed there: darken the light-theme red behind white text, or use dark text on that colour.
