# P-DEC15 · expected differences (written before any code change or diff, 21 Nov 2026)

Decision under test: What's new scales per edition, derived from the edition's largest day.
`kit/build.py` keeps `NEW_INTERVAL = 11000` and gains `new_interval(top)`: `NEW_INTERVAL` when the largest day reaches
`10 * NEW_INTERVAL` (110,000 words), else `max(1, top // 10)` (integer, so the largest day stands at least 10 levels:
`top // (top // 10) >= 10`, and at most 19, inside 10 to 25). Only `new_layer` (What's new's hero, written into
`new.html` only) passes through it; the course homes' and the home's intervals are untouched.

Largest days, by script (`out/DEC-C/p_dec15_days.py`, read from each built `new.html`; output
`out/DEC-C/p_dec15_days-before.out`):

- academy: 221,673 words (22 Oct 2026) -> interval 11,000, unchanged.
- greece: 221,673 words -> interval 11,000, unchanged.
- marketing-ai: 79,671 words (16 Nov 2026) -> interval 7,967 (was 11,000); levels 7 -> 10 on the largest day
  (other days 5->7, 3->4, 0->0, 4->6).

Expected, therefore:

1. **academy:** `python3 kit/baseline.py --check` lists exactly P-DEC8's 4 files and no other
   (`academy/building-with-ai-bw/built.html`, `academy/sport-psychology-sp/built.html`,
   `academy/supply-chain-execution-sce/built.html`, `academy/ux-ia/built.html`), each with the same sha256 as before
   this row. `kit/academy/new.html` byte-identical. `kit/README.md` (a manifest output) is not edited by this row unless
   its prose is false; if its prose is edited, it is listed here as a hand edit and proved to differ only in that prose.
2. **greece:** 0 differ (`new.html` byte-identical).
3. **marketing-ai** (built before and after in `/tmp`): exactly one file differs, `new.html` (What's new's hero layer:
   the `interval` and the contour lines; the rises' labels and words unchanged); every other file byte-identical.
4. Any other difference fails the row.
