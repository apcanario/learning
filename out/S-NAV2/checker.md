# S-NAV2 · fresh check of the whole diff 445b0c4..HEAD

Model: Opus 5.5 (`claude-opus-5-5`), a fresh agent that had not seen the work. 22 Nov 2026. No repo file edited but this one; nothing committed, pushed, landed or re-recorded; no `verify.py --full`.

## Verdict

The row's built work holds: Fix 1, Fix 2, the four layouts, phone identity and reading-page identity are confirmed by my own probes. One layout bug (should-fix 1) is missed by the new checks. The remaining findings are about the docs the close must update and the open items for Pedro. Nothing is blocking.

## What I ran myself

- `python3 kit/baseline.py --check`: academy 460 files, 0 differ; greece 82 files, 0 differ; clean.
- `kit/nav_diff_check.py --build 445b0c4 --now-tree .` (marketing-ai built first): NAV DIFF CHECK PASSED.
  - academy: shell JS 1, theme CSS 1, the home 1 (the `--n` attribute), size table 1; 566 reading pages identical; 2417 drawings the same.
  - greece: 162 reading pages identical. marketing-ai: 76 identical.
- Changed files from 445b0c4 to HEAD: `design/README.md`, `design/theme.css`, `kit/CHANGELOG.md`, `kit/README.md`, `kit/academy/index.html`, `kit/baseline.json`, `kit/build.py`, `kit/shell.css` (cmp identical to the theme), `kit/shell.js`, `kit/verify-hashes.json`, `kit/verify.py`, and `out/S-NAV2/*`.
  - No unit, brief or vault file changed, and no page has its own CSS.
  - `build.py`'s only change is Fix 1 (`--n` on `p.harea`, an assert, a comment).
- Fix 1 probe (`/tmp/ck/probe.py`). Every animation was paused and stepped every 50 ms over two cycles.
  - Coverage: academy (the real 6 words) and greece (n = 1), plus clones of the line with n = 1, 3, 4 and 8. Viewports 320x640, 390x844, 768x1024, 1024x768, 1280x800 and 1920x1080.
  - Result: exactly one word above opacity .5 at every sample (max 1, min 1). Each word was shown 3000 ms a cycle. Overlap was at most 350 ms, or 0 at n = 1.
  - Greece's one word is shown steadily.
  - Under reduced motion `.harea` is `display:none`, the static line shows, and no animation runs.
  - A new area needs no CSS edit: `--n` comes from `len(THEMES)`.
- Fix 2: I read the diff of `go()`, popstate, hashchange and `saveY`.
  - Without `?debug`, `DBG` is null. The only added work is a string assignment of `br`, and `n0 = 0`.
  - Branches, calls and fallbacks are identical to 445b0c4, so Pages behaviour is unchanged.
- Layout probe (`/tmp/ck/lay.py`):
  - Coverage: 8 pages (home, track-history, greece, ux-ia, read-ia3, m23, new, changelog) at 320, 360, 390, 800x1100, 1024x768, 1280x800, 1440x900 and 1920x1080, dark and light.
  - No horizontal scroll anywhere.
  - No heading, figure or table past the screen above 390 px. At 320 to 390 px one table in read-ia3 is wider than the screen; it sits inside its scrolling `.tbl` frame, as at the start build.
  - Dark and light give identical geometry.
  - Drawer at 800 and 1024. A 240 px sidebar with both navs at 1280x800.
  - Desktop: a top bar with the main nav. The sidebar is 259 px at 1440 and 300 px at 1920, and only on pages with a sub-nav. The outline sits beside the column on unit pages only. Its links are focusable, clicking one routes, and `aria-current` moves.
  - Hero heights: home 388, 394 and 746 px; areas 388, 394 and 626 px (at 1024, 1280 and 1920).
  - Academy fold: stats end at 710/768 and 716/800.
- Negative controls (`/tmp/ck/neg.py`, faults injected through a route over the served shell; verify.py's own functions):
  - `check_layouts`: with the desktop outline hidden and the home hero forced to 900 px, it reported 22 faults (no outline, fold, hero bound).
  - `check_phone_identity`: with `@media (max-width:400px){.hero h1{letter-spacing:.03em}}`, 16 views differed.
  - `check_harea`: with the old 12 s rule, 50 faults. The control run without the injection gave 0.
  - Control `step-D-probe.py --only phone`: 24 views identical, PROBE PASSED.

## Findings

### 1 · should-fix · design/theme.css:988 (`.main-nav` in the desktop block) · the desktop top bar cuts the last area with no cue between 1100 and about 1140 px wide

- **What is wrong.** The main nav is fixed from `--side` to `right: calc(3 * 44px + 24px)`, with `overflow-x:auto` and the scrollbar hidden (`scrollbar-width:none`). At 1100x860 the nav's client width is 704 px and its content is 745 px. "Supply Chain" is cut at the bar's right edge, and nothing shows that it scrolls.
  - The cut stops at about 1141 px wide.
  - A seventh area would widen the range.
- **Evidence.** `/tmp/ck/mn.py`: at 1100x860, `scrollWidth` 745 against `clientWidth` 704, and the last item's right edge at 977 against the nav's at 944. Screenshot `/tmp/ck/1100x860.png` shows "Supply Ch" cut under the theme button. At 1180 px and wider it fits.
- **Why the checks missed it.** `kit/verify.py:3365` `LAYOUTS` has no desktop viewport near 1100 px (1440 and 1920 only), and `check_layouts` does not compare the main nav's `scrollWidth` with its `clientWidth`.
- **Fix.** Drop the item gap or padding below about 1200 px, or let the items wrap or shrink. Also add 1100x860 to `LAYOUTS` and a check that the main nav does not overflow.

### 2 · should-fix · kit/verify.py:3437-3438 (the fold rule) · the spec's fold test is relaxed for a one-track edition, so greece misses it

- **What is wrong.** The row's test is "the first tiles visible above the fold on a tablet landscape home". For a one-track edition the check only requires the tile row to start 44 px above the fold.
- **Evidence.** Greece at 1024x768: the row starts at 668, the title ends at 782 and the stats at 888. At 1280x800: 675, 789 and 895. These match step-D.md BUGS 1 exactly. Cause confirmed: `#home > .track > .thead` stands between the 388 to 394 px hero and the grid.
- **Status.** Flagged to Pedro with a ⚠ proposal, which is correct. The close must carry it as a proposal row, not as done. Greece is a published edition (row text: "Republish the greece artifact the same way if its files changed").

### 3 · should-fix · kit/shell.js:279 (`?debug` on `location.search` only) · Fix 2 may be unreachable in the artifact

- **What is wrong.** The readout turns on only when the frame's own query carries `debug`. Step B could not confirm that `https://claude.ai/artifact/<slug>?debug` passes the query into the sandboxed frame (step-B.md, "How to activate it").
- **Why it matters.** If it does not, Pedro's test returns nothing and costs a round trip.
- **Fix.** Before asking Pedro, the main chat should open the published artifact with `?debug` and see whether the panel appears. If it does not, say so in the reply rather than send him to test. The row allows only `?debug`, so any other trigger is Pedro's call.

### 4 · should-fix · docs the row made false (§8 close)

- **kit/build.py:566 and 1045-1046.** "tall below 1100 px, wide from it" and "(from 1100 px, across the full width beside the sidebar)". Since 6.22 the wide layout starts at 900 px. Comments only.
- **kit/verify.py:4144 and 4161.**
  - "the home's area line at 0, 3, 6, 9 and 12 s of its cycle" and the sheet label `of its 12 s cycle`. With six areas the cycle is 18 s, and the five poses (k x 3 s) never show the sixth word.
  - The label should read n x 3 s. Optionally add a pose at 15 s, or note it.
- **kit/README.md:70.** The `build.py` row says "the four areas of knowledge cycling under it". This was already stale with six tracks, and it is the thing Fix 1 changed.
- **kit/README.md:102.** The `verify.py` row says "at three widths". It now runs 1024x768 and 1920x1080 as well, plus `check_layouts` at six viewports.
- **design/theme.css, section 4h comment (about line 450).** "stands 70% of the screen tall" now holds only below 900 px. Section 6's new block says otherwise; worth a pointer.
- **design/README.md:97 and kit/README.md.** `--shots DIR` "saves the three widths" (390, 768, 1280). The row's shots need 1440x900, 1280x800 and 800x1100, so the main chat must use `p95_shots.py` or another script. Not a code fault, a reminder.

### 5 · note · kit/verify.py:3562 (`PHONE_REF`) · the phone's CSS is now frozen at theme 6.19 for every future verify run

- **What it means.** `check_phone_identity` runs on every verify and fails on any future theme change that touches the phone, until someone moves `PHONE_REF`. That includes a deliberate one, such as a new component styled for phones.
- **Where it is documented.** In the verify.py comment (line 3561) only.
- **What to add.** One line in `design/README.md` "Checks before republishing", and in `docs/method.md` §7 or the `file-unit` and `new-course` skills where they describe a theme change. Otherwise the next style row hits an unexplained FAIL.

### 6 · note · kit/verify.py:3530 · the home's frame budget is unproven against the fault

- `FRAME_P50_MAX` is 32 ms for the home.
- The negative control (step-D.md) injected the missing pause observer only on course homes (30.8 to 32.6 ms against 22). The home's faulted median was not measured. A fault on the home could sit under 32 ms, since its clean median already reaches 28.3.
- Step D states this as a calibration choice; the doubt is mine.

### 7 · note · design/theme.css:983-994 · desktop focus order differs from visual order

- On a desktop the theme and arrow buttons (`.top`) come before the main nav in the DOM. Visually, the main nav sits to their left.
- Step C noted it. WCAG 2.4.3 allows it if the order is meaningful. Recorded for the close's proposals.

### 8 · note · design choices that differ from the spec's letter (recorded by step C; correctly flagged)

- **No sidebar from 900 to 1099 px (NEEDS PEDRO 1). Confirmed.**
  - `kit/shell.js:51` is `matchMedia('(min-width:1100px)')`. `closeDrawer` and `syncWide` set `aria-hidden` from it, so a CSS-only sidebar there would be visible but hidden from a screen reader.
  - The fix is that line plus moving the theme's sidebar rules to 900 px, as stated.
- **Outline lists h2 sections, not h3 (NEEDS PEDRO 2). Confirmed.**
  - At 1440x900 the outline shows 7 entries (h2), Sources, the writer's note, How this unit was made and Whole unit.
  - CSS cannot generate entries from headings, so this follows the spec's own fallback ("build it from the existing section navigation ... and flag it").
- **No sidebar on a desktop home or site page.** The spec says "a persistent left sidebar for the sub-nav". These pages have no sub-nav (it is `[hidden]`), so there is nothing to show. The main nav still starts at `--side`, which leaves an empty brand-width gap left of it (shot `/tmp/ck/1440x900-home-dark.png`). Acceptable, and recorded.
- **Main nav stays in the sidebar at 1100+ px under 860 px tall.** The spec puts the top bar on the desktop only. Consistent.

### 9 · note · open items for the close (not faults of the steps)

- **Rows to close.** P-NAV1, P-NAV2 and P-NAV4 are recorded in `kit/CHANGELOG.md` and `design/README.md`, but their rows are still in `docs/BACKLOG.md` (lines 1695, 1696 and 1698). P-HK1 (line 1690) is done by this row: the bound is in container units, and the check runs at 1024, 1280 and 1920. P-NAV3 stays as Pedro's iPhone check: WebKit was blocked by egress (403 on `cdn.playwright.dev`), as step D states. P-NAV7 waits on the readout.
- **Uncommitted working-tree change.** `kit/verify-hashes.json` has an uncommitted change: the greece and marketing-ai records, from the `--edition` runs. Commit it with the close.
- **Before publishing.** "Before publishing, stop" (shots to Pedro, his word) is not yet done, as expected at this point.
