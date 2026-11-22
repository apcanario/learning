# S-NAV2 step A · Fix 1, the area words overlap in the home hero

Model: Opus 5.5 (`claude-opus-5-5`), a fresh agent. 22 Nov 2026. Nothing committed, pushed or landed; `kit/baseline.json` not re-recorded; `kit/land.py` not run. All changes are uncommitted in the working tree.

## Cause (confirmed)

`design/theme.css` 4h ran every `.harea-w` on `harea 12s ... calc(var(--k) * 3s - .4s)` with 25% windows: four words. `catalog.toml` has six tracks (history, marketing, technology, ux, sports, supply-chain), so words 5 and 6 started at 12 s and 15 s, inside the same 12 s cycle, over words 1 and 2. The new check reproduces the bug: with the old rule put back into the page it finds two words above opacity .5 at 244 sampled times (Sports with History, Supply Chain with Marketing), three drawn at once, and words shown 0, 0, 5800, 6000, 0, 0 ms a cycle.

## The reading taken (recorded): any n, CSS only, no ceiling

A keyframe's offsets cannot take `var()`, so per-n keyframes would need a ceiling and a CSS edit past it. Instead the window is in the easing: `linear()` easing stops accept `calc()` and `var()`, and an easing's output can rise and fall. So:

- `kit/build.py` writes `style="--n:<len(THEMES)>"` on `p.harea` (and asserts at least one area).
- The theme, inside `@media (prefers-reduced-motion:no-preference)`, now also inside `@supports (animation-timing-function:linear(clamp(0, 1, 1), 1 calc(50% * .12), 0))`:
  - `--hw: calc(100% / var(--n))` (one word's share), `--hs: clamp(0, 2 - var(--n), 1)` (the start value: 0, or 1 when there is one area, so a lone word stays put with no blink at the cycle's turn);
  - two animations a word, `harea` (opacity 0 to 1) and `harea-y` (translateY .3em to -.3em), over `calc(var(--n) * 3s)`, delay `calc(var(--k) * 3s - .4s)` as before, infinite, both;
  - easings `linear(var(--hs), 1 calc(var(--hw) * .12), 1 var(--hw), 0 calc(var(--hw) * 1.12), 0)` for opacity and `linear(calc(var(--hs) * .5), .5 calc(var(--hw) * .12), .5 var(--hw), 1 calc(var(--hw) * 1.12), 1)` for the rise. At n = 4 these are exactly 6.5's keyframes (in by 3%, held to 25%, out by 28%); for any n the fade is .36 s, the hold to 3 s, so two words cross for .36 s and never more.
  - Two animations because one CSS easing cannot draw an opacity that rises and falls and a transform that only rises (the keyframe easing applies per segment, and opacity clamps before interpolation).
- Reduced motion: unchanged, the static line shows and nothing moves. A browser without `linear()` stops in `calc()` (before Chrome 113, Firefox 112, Safari 17.2) falls back the same way: the static line, nothing moving.
- Measured in Playwright's Chromium (157.0.8103.78): `linear(0 0%, 1 2%, 1 16.6667%, 0 18.6667%, 0 100%)` at n = 6, duration 18 s.
- Greece (one track): `--n:1`. Its word is now shown steadily. Before, it was shown 3 s of every 12 s and blank for 9 s, which was already a fault of the 6.5 rule.

## Files changed

- `design/theme.css`, copied to `kit/shell.css` (`cp`, the repo's convention, design/README.md step 2; `cmp` identical; `rot_check.py` OK). Section 4h: the media block, the new comment, the two keyframes (`harea`, `harea-y`) in place of the old `harea`. A header entry, Version 6.20. The section 4h description changed from "the four areas" / "names all four" to "the areas" / "names them all".
- `kit/build.py`: `hero_areas` writes `--n`, an assert, and a comment. Only the markup attribute changed.
- `kit/verify.py`:
  - New `check_harea` with `HAREA_JS`, run in the home's motion pass at every viewport it already uses (320x640, 360x780, 430x932, 390x844, 768x1024, 1280x800; dark only, since opacity does not depend on the theme), right after `check_home(... motion=True)`.
  - It checks the real line (`--n` equals its word count, the tracks), then a probe: a copy of the line inserted beside it with 3, 4 and 8 words, its `--n` set to match, measured and removed. The DOM only; the catalog is untouched.
  - Each line is sampled every 50 ms over two cycles, with every animation paused at the time. Each word must run `harea` and `harea-y` over n x 3 s. At every sample at most one word is above opacity .5, and exactly one except at a cross-fade's middle. Three words are never drawn at once. Two are drawn together (opacity over .01) for at most the .36 s cross-fade plus one sample. Each word is shown 3 s a cycle, in turn, and has no transform while fully shown.
  - Updated for two animations a word: check_home's count of the other animations (now `harea` and `harea-y` on each word), check_topo's and SWELL_JS's allowed names (`harea-y` added).
  - New constant `PHONE_EXPECTED`, the expected differences on the phone beside the phone byte-identity check: the inlined theme CSS, and the home hero's area line (`--n` on `p.harea` and its animation). No byte-identity check existed yet in `verify.py`, so the later step that builds it should read this constant. The docstring has a paragraph on the new check, and its "four areas" wording is corrected.
- Rebuilt outputs, written by `baseline.py --check`'s build: `kit/academy/index.html`, `kit/README.md` (size table: the shell 611 KB to 613 KB, the theme's comments), the greece and marketing-ai sites (ignored by git).

## Tests

- `python3 kit/baseline.py --check`: academy 460 files, 2 changed (`README.md`, `academy/index.html`); greece 82 files, 1 changed (`editions/greece/index.html`); 0 added, 0 removed. These are the expected files.
- `python3 kit/nav_diff_check.py --build HEAD --now-tree /home/claude/learning` (start tree = HEAD 445b0c4, clean before any change):
  - academy: theme CSS 1 stretch, the home 1 stretch, size table 1. 566 reading pages identical; 2417 drawings the same. OK.
  - greece: theme CSS 1, the home 1. 162 pages identical; 712 drawings. OK.
  - marketing-ai was not built in the working tree by baseline.py. After `build.py --edition marketing-ai`, `--edition marketing-ai` gives theme CSS 1, the home 1, 76 pages identical, 307 drawings. PASSED.
- "The home" stretch is only the attribute. A token diff of `kit/academy/index.html` against HEAD, with the `<style>` block left out, is the one change `<p class="harea" aria-hidden="true">` to `<p class="harea" aria-hidden="true" style="--n:6">`.
- Narrow verify, without `--full`. verify.py has no single-check flag, so a probe script outside the repo (`/tmp/sna/harea_probe.py`) imports `verify` and calls `check_harea` at all six viewports with motion:
  - real 6 words: 720 samples, each word shown 3000 ms, overlap at most 350 ms;
  - probes of 3, 4 and 8: 360, 480 and 960 samples, 3000 ms each, overlap at most 350 ms;
  - `check_home` with motion at 320x640, with `check_harea` again after it;
  - `check_home` under reduced motion at 320x640: the static line shown, the cycling line hidden, no animation;
  - PROBE PASSED, no console errors.
- Greece (`--edition greece`), 320 and 1280: one word, opacity 1 throughout, overlap 0; the probes pass.
- Negative test (`/tmp/sna/harea_neg.py`): the old 6.5 rule injected into the page fails on the real line and on every probe, as listed under Cause.
- `rot_check.py`: OK.

## For the main chat

- Landing: `baseline.py` re-record, plus `drop:` entries for the replaced lines of `design/theme.css`, `kit/shell.css`, `kit/verify.py`, `kit/build.py`, `kit/README.md` and `kit/academy/index.html`.
- The phone's expected differences are in `PHONE_EXPECTED`.
- `design/README.md` and `kit/CHANGELOG.md` do not yet record 6.20. The 6.5 paragraph's "12 s a cycle" is a historical record, kept. Add a line at close.
- Not run: `verify.py --full`, `index_check.py`, `private_terms.py` (left to the landing).
