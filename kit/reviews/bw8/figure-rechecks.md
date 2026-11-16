# BW8 figure re-checks (row W-BW8, 16 Nov 2026)

Each by a fresh Opus 5.5 agent (claude-opus-5-5) given the unit's text without its figures, the declaration with its caption, and the frames sheets of `verify.py --shots ... --page read-bw8`.

1. Figures 1 and 4 after the fresh check's fixes: figure 1 PASS; figure 4 FIX (three /loop cells not in the text; §6's closing citation; the Desktop "Minimum interval" cell never whole at 390 and 430 px). Worked by corrections checks r3 and r4 (`audits/building-with-ai/corrections-2026-11-16-BW8-r3-BW8.md`, `-r4-BW8.md`) and theme 6.12 (a matrix's narrow-label drawing on every phone).
2. Figure 4 after those: FIX, layout only (the Desktop column under an edge fade in every half-frame stop at 360 and 390 px). Worked by shortening the cell to "forms: 1 hour; Claude: 1 minute" (same facts as §6) and by `verify.py`'s frames stepping a third of the clear room beside a sticky label column.
3. Figure 4 after those: PASS at 320, 360, 390, 430, tablet and desktop, dark and light; every cell traced to §6.
