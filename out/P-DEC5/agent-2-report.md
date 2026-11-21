# P-DEC5 · agent 2 (packet 2, probe fixes) report

Model: Opus 5.5 (`claude-opus-5-5`). 21 Nov 2026. Nothing committed or pushed.

## Verdict

**Done.** Both failures are fixed at the root. The probe now gives **ALL CHECKS PASSED**, with figure geometry included. The probe was a copy of e0101f7 plus these edits, at `/tmp/pdec5b/probe`, with the probe `workbench` brand: Source Sans 3, IBM Plex Mono and `[metrics]`. `python3 kit/baseline.py --check` gives **baseline: clean** (academy 457 files, 0 differ; greece 82, 0 differ).

## Root causes

Both failures come from the face's **ch**, the width of its "0". Source Sans 3's "0" is 0.497 em and DM Sans' is 0.684 em, so every `ch` measure in the theme narrows by about 27%.

1. **Report measure.** This was a check calibrated on one face. `verify.py` requires the report's 68ch measure to be at least 560 px. In DM Sans, 68ch at 16 px is 744 px. In Source Sans 3 it is 541 px, so the measure matched its own 68ch (within 2 px) and still failed the floor.
2. **Rings outside the frame (PB1, PB7).** This was an engine assumption, not the check and not P-DEC11.
   - The hero lede's measure is `max-width:62ch` (theme). In Source Sans 3 it shrinks from 721 px to 524 px, more than the text itself narrows.
   - Personal Brand's lede then wraps to 7 lines instead of 5 (178.5 px against 127.5 px). The hero grows from 471 px to 522 px, and the frame from 493 px to 544 px.
   - `COURSE_TOPO`'s wide layout (2:1, `xMidYMid slice`) is fitted for heroes of 400 to 480 px (build.py comment). A taller frame scales the layout by its height and cuts its sides.
   - The end rises' rings then lay up to 19.6 px left of the frame (PB1) and 4.7 px right of it (PB7), at poses 0 to 0.75.
   - The check measures a real defect: the rings are cut off on screen. With the real brand (DM Sans) on the same code, the same rises keep 24 to 44 px of margin.
   - Measured with `out/P-DEC5/rings.py`, which reads each rise's `data-box` against the frame at the five poses, desktop with motion.

## The fix (diff in `out/P-DEC5/agent-2.diff`)

- **`kit/verify.py`:** the floor is `560 * viz._ADV['sans']['0'] / viz._DEFAULT[0]['sans']['0']`. In DM Sans' metrics the ratio is 684/684, so the floor is exactly 560 and academy's and greece's check is as strict as before. For Source Sans 3 the floor is 407 px. The upper bound (the column) and the 2 px match to 68ch are unchanged.
- **`kit/build.py`:**
  - `LEDE_CH`, `LEDE_PX` and `LEDE_LH` are read from the theme's `.lede` rules (62ch, 17 px, 1.5).
  - `HERO_TALL = 502` is the tallest frame the wide layout is fitted for (480 px hero plus the 22 px above it).
  - `lede_lines(text, adv)` wraps the lede greedily at spaces, at LEDE_CH of that face's "0".
  - `course_topo(lede)` counts the extra lines in the brand's `--sans` against DM Sans. If there are none, it returns `COURSE_TOPO` itself. Otherwise it draws the wide layout's box and view x-extents in towards 0.5 by `502 / (502 + extra px)`. That ratio is how much less of the layout's width a slice into the taller frame shows. Personal Brand gets two extra lines, 51 px, so k = 0.908.
  - It is used by the history `course_home` (`fill(c['lede'], c)`) and per markdown course (`dict(MDKIT, topo=course_topo(m['sc']['intro']))`). `mdcourse.py` is untouched.
  - Without a brand `[metrics]` table, both tables are DM Sans, so the extra is 0 and the output is byte-identical.
  - After the fix, PB's worst margins in the probe are 26 to 48 px (left) and 40 to 47 px (right) at every pose, as wide as the DM Sans control's. BW's are 34 to 56 px.
- **`docs/decoupling.md` §6:** one bullet added to "Notes on P-DEC5" that records both causes and both fixes.
- `brands/academy.toml` and `kit/viz.py` are unchanged; neither needed it. `kit/courses.py` is unchanged. The `kit/verify-hashes.json` change in the working tree was there before this packet started, and I did not touch it.

## Results

**Probe** (`/tmp/pdec5b/probe/kit`, `python3 verify.py --edition marketing-ai`, run after `python3 kit/build.py --edition marketing-ai`). Full output is in `out/P-DEC5/probe-verify-run3.txt`. First lines:
```
full: no passed run recorded for edition marketing-ai (verify-hashes.json)
edition marketing-ai: no size table (README.md keeps the default edition's)
viz-examples.html: 34 figures
```
Last lines:
```
ALL CHECKS PASSED

real	6m5.998s
```
0 FAIL lines.

**Control** (a copy with the real `brands/workbench.toml`, DM Sans): the PB hero margins are identical before and after the change.

**Baseline** (main tree, `python3 kit/baseline.py --check`, run on the final `build.py`; output in `out/P-DEC5/baseline-check-2.txt`):
```
academy: 457 files, 0 differ
greece: 82 files, 0 differ
baseline: clean
```

## Notes

- **Tall layout not adjusted:** the tall layout (below 1100 px) is not adjusted for the extra lines. It passed every phone and tablet check in the probe, because its slice into a portrait frame crops by the width, which the lede's height does not change.
- **What the estimate assumes:** the lede is a desktop column at least 62ch wide in DM Sans, which is true at 1280 px, the width verify checks. It also assumes the lede is the only hero text whose wrap depends on `--sans`; the h1 is serif, and the measured growth matched the lede exactly (51 px).
- **New files in `out/P-DEC5/`:** `agent-2.diff`, `rings.py` (the diagnostic), `probe-verify-run3.txt` and `baseline-check-2.txt`.
