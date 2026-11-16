claude-opus-5-5

# Figure 2 re-check (BW5 §4 dependency matrix): PASS

1. Labels and marks against the text. Every mark matches the "Takes from" column of Deliverable 1b, with no mark missing and none extra:
   - "| 3 | BW3 · Briefing | BW1 |" → BW3: BW1
   - "| 4 | BW4 · Context engineering | BW1 |" → BW4: BW1
   - "| 5 | BW5 · Specifying a project | BW3, BW4 |" → BW5: BW3, BW4
   - "| 6 | BW6 · Research and verification | BW1, BW3, BW5 |"
   - "| 7 | BW7 · Pipelines | BW2, BW3, BW5 |"
   - "| 8 | BW8 · Skills and automation | BW4, BW5, BW6, BW7 |"
   - "| 9 | BW9 · Agents | BW5, BW6, BW7, BW8 |"
   - "| 10 | BW10 · Cost, limits, privacy | BW2, BW5, BW9 |"
   The column labels BW1 to BW9 and the row labels BW3 to BW10 all appear in that table. The figure has no numbers. The legend's "Gives line" comes from 1b: "each Takes entry is read from the Gives lines of the units named". BW1 and BW2 take from nothing, so they have no rows. The DD units are left out, which matches the caption's "core units".
2. Caption. It says what the figure shows ("dependency grid: each row takes from the columns marked") and names the section and the source ("build order in Deliverable 1b of this unit, read from the Gives lines of this course's map"). Its claim that every mark sits to the left of the row's own unit holds, and it matches 1b's line "every 'Takes from' entry sits higher in the table than its own row".
3. Legend key colour. A pixel sample of the key and of a marked cell gives the same value in each theme: dark rgb(31,44,54) for both, and light rgb(182,204,213) for both, at 1280 and 320 px. By eye they also match in all twelve shots (320, 390 and 1280; dark and light; start and end).
4. Clipping and overlap. Nothing is clipped or overlapping. At 320 and 390 px the row labels BW3 to BW10 stay pinned at the left when the figure is scrolled to the end. Cells that pass under the pinned label column fade out on purpose; this is the scroll fade, not a clip. The "scroll sideways" hint shows at narrow widths. At 1280 px the whole grid fits, and the start and end shots are identical.
5. Kind. A matrix fits this figure: the items are units, laid out against the units they take from.
