# P-HERO1 · the home hero's interval derived from a size budget, with a density floor

Agent: claude-opus-5-5 (fresh agent, P-HERO1 only). Nothing committed, pushed, landed or published.

This is the second pass, corrected by the HK-1 fix pass (fresh Opus 5.5 agent applying `checker.md`: E1, S1, S2, M1 to M5); the corrections are marked "HK-1 fix" below.

This is the second pass. The first pass let the budget push the interval down as well as up. That took greece from 10 levels to 40, an unintended visual change, so the coordinator asked for a floor.

## What changed
- `kit/build.py`
  - `HERO_INTERVAL = 24000` (hand-raised: W-DD-SP2 22,000 to 23,000, W-SCE1 to 24,000) is gone.
  - New `HERO_INTERVAL_MIN = 24000`: the floor. HK-1 fix (S1): it is not a measured design density. P92 drew the hero at 22,000 (`kit/reviews/p92/check-hero-3.md`); 24,000 is W-SCE1's hand-raised value, frozen as the floor by decision so that no edition's hero moves (at 22,000 greece's and every other edition's would). The comment now says so, and that History stands 21 levels at 24,000 (it said "about 20").
  - New `HERO_BUDGET = 19 * 1024`: the only place to change the budget. The rule is in the comment above both constants.
  - `HERO_TOPO` is declared with `interval=None`. Once its phase is set, `hero_interval(HERO_TOPO)` returns the interval and the layer drawn at it. That layer is reused as `hero_topo`, so the hero is not drawn twice.
- `kit/README.md` (the `build.py` row): "a contour every 22,000 words (`HERO_INTERVAL`)" was already out of date. It now describes `HERO_INTERVAL_MIN`, `HERO_BUDGET` and the derivation.
- Unchanged: `verify.py` (its 20 KB stays the hard limit), `docs/decoupling.md` (its HERO_INTERVAL note is a dated historical record), CSS, and everything else.

## The rule
The hero's interval is `HERO_INTERVAL_MIN`, unless the contour layer would be more than `HERO_BUDGET` bytes at that interval. The layer is the `div.topo` with both layouts, tall and wide, at its own phase, measured as verify.py measures it: `new Blob([topo.outerHTML]).size`, the browser's re-serialisation, which writes each self-closed `<path/>` and `<circle/>` with its end tag (`build.py` `sep_bytes`). HK-1 fix (E1): the first version measured the source string, 88 B less for academy's layer (12 paths, 2 circles), so it took 24,400, whose layer is 19,516 B as verify counts, over the 19,456 B budget. The words counted are the written units of the courses that the edition being built holds.

When the layer is over budget at the minimum, the interval becomes the smallest whole hundred of words above the minimum at which the layer fits. The budget only ever raises the interval, never lowers it.

How it is found:
- One drawing when the minimum fits.
- Otherwise one drawing at the largest area's words rounded up (the coarsest interval); if the layer does not fit even there, the build stops with a message.
- Then a scan upward from the minimum in steps of 100, the first interval that fits. HK-1 fix (M1): the first version bisected, assuming the layer shrinks at every step; it shrinks overall but grows by 5 to 87 B at six steps between 22,000 and 30,000, so a bisection could return a larger interval than the smallest.
- Each interval is drawn once (memoised).

Cost: academy needs 7 drawings (24,000, the coarsest, 24,100 to 24,500), about 3 s at 0.43 s a drawing; the bisection drew 14, about 6 s. So the scan adds no time today; each further 100 words the interval rises adds one drawing. greece needs one drawing.

Why the step is 100 words: with 1,000 the interval would be 25,000; with 100 it is 24,500, which is closer to 24,000.

## Derived intervals with today's data
**academy: 24,500** (HK-1 fix; 24,400 before). At 24,000 the layer is 19,913 B as verify counts, over the 19 KB budget (19,456 B), so the budget raises it.

Sizes measured by redrawing the same hero (academy brand, phase 0); "verify" is the outerHTML measure the build now uses:

| Interval | 24,000 | 24,100 | 24,200 | 24,300 | 24,400 | 24,500 | 25,000 |
|---|---|---|---|---|---|---|---|
| Source string, B | 19,825 | 19,732 | 19,607 | 19,566 | 19,428 | 19,300 | 18,995 |
| As verify counts, B | 19,913 | 19,820 | 19,695 | 19,654 | 19,516 | **19,388** | 19,083 |

Checked in Chromium on the rebuilt `kit/academy/index.html`: `new Blob([topo.outerHTML]).size` of the hero's layer is 19,388 B, equal to the build's measure.

The visual change at 24,500 (the same ring counts as at 24,400):
- History (510,493 words): 21 to 20 rings.
- Marketing 7, Technology 8, UX 6, Sports 5, Supply Chain 0 (7,150 words): no change.

**greece: 24,000.** The layer is 5,159 B at the minimum, so the interval stays at the minimum and the output is unchanged.

## Measured hero sizes (div.topo; source string and verify.py's outerHTML Blob measure)

HK-1 fix (E1): the first version said verify.py's Blob measure "ran about 40 B lower". That was wrong: it runs higher, by 6 B for each self-closed path and 8 B for each self-closed circle (88 B for academy's layer, 12 for greece's, 24 for marketing-ai's, 28 for the template edition's; greece's and academy's also checked in Chromium).

| Edition | Interval | Source, B | As verify counts, B |
|---|---|---|---|
| academy (start) | 24,000 | 19,825 | 19,913 |
| academy (now) | 24,500 | 19,300 | 19,388 |
| greece (start and now) | 24,000 | 5,159 | 5,171 |
| marketing-ai (start and now) | 24,000 | 4,356 | 4,380 |
| template edition `fieldnotes` (start and now) | 24,000 | 773 | 801 |

All are under 20 KB (20,480 B).

## Built files that differ from the start
- `python3 kit/baseline.py --check` (exit 1):
  - academy: 459 files, 2 changed.
    - `academy/index.html`: only the hero's `div.topo` is redrawn (now at 24,500). `diff -rq` against /tmp/start/academy shows this file alone.
    - `README.md`: the hand-edited `build.py` row. The size table is unchanged.
  - greece: 82 files, 0 differ.
- greece was also built at the start commit in a throwaway worktree (/tmp/wt, since removed) and compared with `diff -rq` against `kit/editions/greece`: byte-identical.
- HK-1 fix (M3): marketing-ai and the template edition `fieldnotes` were built at the start commit (`git archive 9447f39` in `/tmp/hk1m3/start`) and on the working tree (`/tmp/hk1m3/now`), the template edition recreated in each by `out/DEC-C/p_dec11_template.py`. Both stay at 24,000 with their hero layers byte-identical; each differs from its start in `index.html` alone, by P-DEC20's rule (`out/HK-1/m3_editions.py`, output `m3_editions.txt`).
- verify.py was not run.
