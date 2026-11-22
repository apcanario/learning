# S-NAV2 · step E · the fresh check's should-fix findings applied

Model: Opus 5.5 (`claude-opus-5-5`), a fresh agent. 22 Nov 2026. Nothing committed, pushed, landed or re-recorded; no `verify.py --full`. No unit, brief or vault change; no markup or `build.py` logic change (comments only).

## Changes

1. **Top bar cut at 1100 to about 1140 px (finding 1).** In `design/theme.css` (copied to `kit/shell.css`), desktop block of section 6:
   - `.main-nav` is now its own container (`container-type:inline-size`), and `scrollbar-width:none` became `thin`. If the bar ever overflows, the scrollbar shows.
   - Container steps:
     - Under 920 px: items get 8 px sides.
     - Under 800 px: 6 px sides, a 6 px gap and 13 px type.
     - With nine items or more (eight areas) and under 1000 px: the tighter step, and the area square is hidden (`:has(>.ditem:nth-child(9))`). The active area keeps its rule in its tone.
   - Real six areas: 615 px of 704 at 1100, 615/744 at 1140, 689/884 at 1280, 745/1025 at 1440.
   - The eight-area probe: 664/704 at 1100 and 934/1025 at 1440.
   - A sweep every 4 px from 1100 to 1920 (real and probe) found no overflow.
   - **New check `check_topbar`** in `kit/verify.py`, called from `main()` before `check_layouts`.
     - Viewports: 1100, 1120, 1140, 1280 and 1440 x 900, and 1920 x 1080. Dark and light; the home and the first area page; the real areas and a probe of 8 (`TOPBAR_PROBE`, copies of the first areas appended).
     - It checks that the nav is fixed and does not scroll, that no item is cut or past the nav's edge, and that the nav ends left of the buttons.
     - It has a `body=` hook for fail-tests.
   - **Fail-test.** The shell was served with HEAD's theme (the old rule): 24 faults. Eight of them are with the real areas at 1100 and 1120 ("745 px of items in 704", "Supply Chain 854..977"); the other 16 are the probe. 1140 is within 1 px, as the checker measured. With the new theme: 0 faults.
2. **Greece one-track fold (finding 2).** Not changed: it is BUGS 1, flagged to Pedro.
3. **`?debug` in the artifact frame (finding 3).** Nothing in code.
4. **Stale docs.**
   - `kit/build.py` 566 and 1045-1046: tall below 900 px and wide from it (1100 px before 6.22). Comments only.
   - `kit/verify.py` motion-sheet comment and label: n x 3 s cycle, n the words. 18 s with six areas; words 1 to 5 are posed and the sixth is not (`check_harea` samples every word). The label prints the real cycle and the word index.
   - The `kit/README.md` `build.py` row: the areas cycling one at a time over n x 3 s (`--n`, `len(THEMES)`), and tall below 900 px.
   - The `kit/README.md` `verify.py` row: the widths now include 1024 x 768 and 1920 x 1080, `check_layouts` at six viewports and `check_topbar`. `--shots` now includes the shot layouts.
   - `design/theme.css` section 4h: the 70% holds below 900 px only, with a pointer to section 6.
   - `design/README.md` "Checks before republishing": `--shots` and `--layout-shots`; `PHONE_REF` is re-pinned deliberately by a row that changes the phone (checker note 5, design/README half); `check_topbar`.
   - At `PHONE_REF`, a one-line comment: the phone CSS is frozen at this commit for the byte-identity check, and must be re-pinned deliberately when a row changes the phone's design.
   - **Shot layouts.** `layout_shots(br, out)` in `verify.py`:
     - What it shoots: the first screen of the home, the first area page (`track-history`), a course home (`greece`) and a unit page (`m23`, Greece 2.3).
     - Layouts: desktop 1440x900, tablet-landscape 1280x800 and tablet-portrait 800x1100; dark and light; reduced motion; scale 1.
     - Output: `<page>-<layout>-<theme>.png`.
     - How to run it: `--shots DIR` writes these into DIR too, and `python3 kit/verify.py --layout-shots DIR` writes only these. The second runs no check and records nothing.
     - Documented in the module docstring and usage line.
   - **24 shots** generated into `/tmp/snc/shots-pedro/` (outside the repo).

## Tests

- `python3 kit/baseline.py --check`: 3 files differ.
  - academy: `academy/index.html` and `README.md`. The shell is identical to HEAD's outside its `<style>`. README.md's diff is the size table (shell 628 to 630 KB, site 24.75 to 24.76 MB) plus the two doc rows above.
  - greece: `editions/greece/index.html`, the inlined theme.
  - No reading page differs.
- `out/S-NAV2/step-D-probe.py --only layouts,phone,nav1024,nav1280,nav1920`: PROBE PASSED.
  - Phone identity: 24 views byte for byte as 445b0c4, 0 retries.
  - Layouts: 0 faults at all six viewports. The fold at 1024x768 and 1280x800 holds (stats at 710 and 716), and the hero bounds are unchanged.
- `check_topbar`, run alone (`/tmp/se/tb.py`): PASSED. With the old rule: 24 faults.
- `rot_check.py`: OK. `cmp design/theme.css kit/shell.css`: identical.

## For the main chat

- Working tree: `design/README.md`, `design/theme.css`, `kit/README.md`, `kit/academy/index.html`, `kit/build.py`, `kit/shell.css`, `kit/verify.py`. `kit/verify-hashes.json` was already modified before this step.
- `kit/baseline.json` is not re-recorded.
- The theme's version line was not bumped; this is a change within 6.22's block. Bump it at the close if the theme keeps a version per change.
- Checker note 5's other half is not done here: the method.md §7 and skills line is a doc outside this step's files.
