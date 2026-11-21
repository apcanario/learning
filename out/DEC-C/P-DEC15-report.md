# P-DEC15 · What's new's scale per edition (21 Nov 2026, Opus 5.5)

## Decision

What's new scales per edition, derived from the edition's largest day (not a per-edition key).

`kit/build.py` keeps `NEW_INTERVAL = 11000` and adds `new_interval(top)`: `NEW_INTERVAL` when the largest day reaches
110,000 words (10 levels at 11,000), else `max(1, top // 10)`. Only What's new's layer (`new_layer`, written into
`new.html`) uses it. With the integer division the largest day stands `top // (top // 10)` = 10 to 19 levels, inside 10
to 25.

Reasons:
- The level is the drawing's unit, not a quantity shown to the reader (the hero is aria-hidden and textless; the words
  are on the cards), so a fixed value has no meaning across editions; what P93 asked of the page is a rise.
- Under the fixed scale a small edition drew low hills (marketing-ai 7 levels) or nothing (fieldnotes 0 levels), which
  S-DEC4 only accepted in verify.py.
- Derived rather than configured: no edition key to keep in step with filings; an edition crossing 110,000 words moves
  to academy's scale by itself; academy and greece (221,673 words) keep 11,000 and stay byte-identical.

## Files changed

- `kit/build.py`: `new_interval()` after `NEW_INTERVAL`; `new_layer` calls it with the largest of `NEW_DAYS`; the P93
  comment above `NEW_DAYS` names it.
- `kit/verify.py`: `new_interval()` repeated beside `NEW_INTERVAL = _build_const(...)` (build.py cannot be imported);
  the What's new branch of `check_topo` now holds every edition whose largest day has 10 words or more to 10 to 25
  levels and every edition to its own scale (`levels == words // new_interval`); a scaled edition's run prints its
  interval once. The "held to the scale only" branch is gone. Module docstring updated.
- `kit/README.md`: the `build.py` row said "a contour every 14,000 words, `NEW_INTERVAL`" (already stale: 11,000); now
  names 11,000 and `new_interval`. README.md Known limits says nothing about What's new: unchanged.
- `docs/decoupling.md` §6: "Notes on P-DEC15"; the S-DEC4 "What's new (decided)" bullet marked superseded.
- `out/DEC-C/`: `expected-P-DEC15.md` (written before any code change), `p_dec15_days.py` (+ `-before.out`,
  `-mai-after.out`), `p_dec15_sha-before.txt`, `p_dec15_check.py` (+ `.out`), `p_dec15_baseline-check.log`,
  `p_dec15_baseline-check-final.log`, `p_dec15_verify-{mai,greece,fn}-tail.txt`, this report.
- `docs/BACKLOG.md` not touched (row closing left to the main chat, as for P-DEC11).

## Output

- `python3 kit/baseline.py --check` (main tree), code change only: academy 4 differ, exactly P-DEC8's
  (`building-with-ai-bw`, `sport-psychology-sp`, `supply-chain-execution-sce`, `ux-ia` `built.html`); greece 0.
  After the `kit/README.md` prose edit: those 4 plus `README.md`; greece 0.
- `p_dec15_check.py`: P-DEC8's 4 files, `kit/academy/new.html` and `kit/editions/greece/new.html` carry the sha256
  recorded before the change; `kit/academy/new.html` equals HEAD's bytes; `kit/README.md` differs from HEAD only by the
  P-DEC15 phrase. PASSED.
- marketing-ai, built in `/tmp/probe-dec15` before (`/tmp/dec15-mai-before`) and after (`/tmp/dec15-mai-after`): 36
  files each, only `new.html` differs (13,727 -> 14,489 bytes). Interval 11,000 -> 7,967; rings per day (data-rings):
  11-12 5->7, 11-13 3->4, 11-14 0->0, 11-15 4->6, 11-16 7->10.
- fieldnotes (template test, `/tmp/probe-dec15-f` via `out/DEC-C/p_dec11_template.py`): largest day 1,231 words,
  interval 123, 0 -> 10 levels (both days).

## Verify (probe copies, full runs: no record for the edition there)

- `--edition marketing-ai`: ALL CHECKS PASSED; prints "a level every 7,967 words ... 10 levels".
- `--edition greece`: ALL CHECKS PASSED (fixed scale, no note).
- `--edition fieldnotes` (S-DEC5 template test): ALL CHECKS PASSED; "a level every 123 words ... 10 levels".
- Not run: `--edition academy` (not asked; its What's new is byte-identical and its branch of the rule is unchanged in
  effect: interval 11,000, held to 10 to 25). `kit/verify.py` changed, so the next scoped run of any edition is full.
- `kit/verify-hashes.json` in the main tree not updated (runs were in probes).

## Left

- An edition whose largest day is under 10 words would stand under 10 levels; verify.py exempts it from the range
  (still held to its scale). No such edition exists.
- The rule lives in two places (build.py, verify.py), as `NEW_INTERVAL` already did by reading build.py's source.
