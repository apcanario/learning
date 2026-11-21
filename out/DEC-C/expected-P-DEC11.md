# P-DEC11 · expected differences (written before the main-tree diff, 21 Nov 2026)

The change (tried in the probe copy `/tmp/probe-dec11`):

- `kit/build.py`: the wide `COURSE_TOPO` layout gains `small=(2, (.04, .17, .96, .76))`; `ct_fit` holds a hero of two
  rises or fewer to that view instead of `(.04, .1, .96, .84)`. Only the spread `ct_fit` settles on can change, and only
  for a course home whose hero layer has one or two rises. `NEW_TOPO` (What's new) has no `small` key: unchanged.
- `kit/verify.py`: `SETTLE_JS` and a new `lands()`: not a build input; no built file can change from it.
- Docs (`docs/decoupling.md` §6, `README.md` Known limits, `docs/BACKLOG.md` P-DEC11 row): not build outputs of the
  manifest (`kit/baseline.py` hashes `kit/README.md`, which this row does not touch).

Which course homes have two or fewer rises, by script (`out/DEC-C/p_dec11_rises.py`, from the markdown course data and
from the built site's wide hero layouts; outputs saved beside this file):

- academy: **none** (`p_dec11_rises-academy.out`: 0 course homes; the smallest layer has 11 rises, brand-a and brand-b;
  supply-chain-execution has no layer, no unit written).
- greece: **none** (`p_dec11_rises-greece.out`; 13 and 14 rises).
- (fieldnotes, probe only: home-composting-hc, 2 rises; `p_dec11_rises-fieldnotes-probe.out`.)

Expected, therefore:

1. **academy: byte-identical to the post-P-DEC8 state** (the committed `kit/academy/` at 8f931ec). `baseline.py --check`
   lists exactly P-DEC8's 4 files and no other:
   `academy/building-with-ai-bw/built.html`, `academy/sport-psychology-sp/built.html`,
   `academy/supply-chain-execution-sce/built.html`, `academy/ux-ia/built.html`; each of the 4 with the same sha256 as
   before this row's change (no further change).
2. **greece: 0 differ.**
3. Any other difference fails the row.
