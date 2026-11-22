# S-NAV2 step D · verify.py's new viewports and layout checks; the docs for 6.20 to 6.22

Model: Opus 5.5 (`claude-opus-5-5`), a fresh agent. 22 Nov 2026. Nothing committed, pushed or landed; `kit/baseline.json`
not re-recorded; `kit/land.py` not run; `verify.py --full` not run; `kit/verify-hashes.json` untouched. All changes are
uncommitted in the working tree, on top of HEAD e7f2a1b (steps A, B and C landed).

## Verdict

Done. Every new check passes on academy, greece and marketing-ai; each was shown to catch its fault (negative controls
below). One layout bug found and not fixed (BUGS 1: not a one-line theme fix, a design choice for Pedro). WebKit could
not be installed here: the egress policy blocks Playwright's download hosts, so the WebKit pass prints one line and
P-NAV3 stays Pedro's check on an iPhone.

## Files changed

- `kit/verify.py` (the only code file):
  - **Expectations moved to theme 6.22** (step C's notes):
    - `HOME_JS` and `check_topo`: the wide contour layout from 900 px (was 1100). This is the "expected tall" fault at
      1024 x 768 that step C saw.
    - `HOME_JS`: the home's layer starts beside a 240 px sidebar only from 1100 px under 860 px tall (was any `desk`
      width under 860 px tall, which would have expected a sidebar at 1024 x 768).
    - `HOME_JS` and `check_tiles`: three tile columns are expected when the body's **content box** is 960 px or more.
      Step C read the body's border box, which includes the sidebar's padding: it was right at 1280 x 800 only by
      chance, and would be wrong at 1100 to 1199 px under 860 px tall.
  - **`check_nav`**: a desktop branch (1100 px and 860 px tall or more). The main nav must be fixed in the top bar (top
    0, within the bar, from the sidebar's edge), and the sub-nav in the sidebar under the bar. The tablet landscape
    branch (1100 px or wider, under 860 px tall) now also checks that the main nav stays inside the 240 px sidebar. It
    runs at 1024 x 768 and 1920 x 1080 as well as at 390 x 844 (dark and light) and 1280 x 800.
  - **New viewports in the existing passes.** `NEW_VIEWPORTS` (1024 x 768, 1920 x 1080) are added to:
    - the home and What's new pass (`check_home`, `check_new`, dark and light, and the desktop taps at 1280 only, as
      before);
    - the topography, tile and area pass (`check_topo`, `check_tiles`, `check_area`, dark and light, every sampled page,
      the reading pages);
    - a home-only motion pass (`check_topo` with motion, `check_home` with motion and its texts at the five poses,
      `check_harea`).
    
    The panel checks (`check_panels`: every panel, every `<details>` open; no sideways scroll, 6 px gaps, 44 px targets)
    also run at 1920 x 1080 ('wide1920'). The 1280 x 800 pass keeps its label 'desktop' (other code reads it); its
    comment and the docstring say it is the tablet landscape layout since 6.22.
  - **New `check_layouts`**:
    - **Viewports:** 390 x 844, 800 x 1100, 1024 x 768, 1280 x 800, 1440 x 900 and 1920 x 1080, dark.
    - **Pages:** the home, What's new, the Changelog, the first area page, a history and a markdown course home, and the
      first reading page of every course (15 pages in academy).
    - **The regions, by `layout_of(w, h)`:**
      - **Phone, portrait and 900 to 1099 px:** the drawer off screen with its menu button and `aria-hidden`; no
        sidebar; the top bar the screen's width; the main nav inside the closed drawer; no outline.
      - **1100 px or wider, under 860 px tall:** the 240 px sidebar at 0 (`aria-hidden` false, no menu button); the top
        bar from 240 px; both navs in the sidebar; the column beside it; no outline.
      - **Desktop:** the top bar across the screen, with the main nav fixed in it from `side_px` (`clamp(240, 18vw,
        300)`). On a page with a sub-nav: the sidebar of that width, the sub-nav in it under the bar, and the column
        beside it. On a page without one: no sidebar and no body padding.
      - **The outline, on a desktop:** on every reading page it is beside the column and inside the window, read once
        the section bar is stuck, with its height capped by the `::details-content` max-height. It appears only where
        the browser supports `::details-content`. No other page has one.
    - **No sideways scroll.**
    - **`CLIP_JS`**, with the reading page whole and every `<details>` open but the section menu. No h1, h2, h3, figure
      or table may:
      - run past the column or the screen, or sit under the sidebar or the outline;
      - be a heading that hides its overflow and is cut;
      - be a figure frame that clips its drawing (overflow-x not auto or scroll).
      
      A table is measured by its scrolling frame (`.tbl`).
    - **The fold:** at 1024 x 768 and 1280 x 800, the home's first row of tiles shows its titles and stats above the
      fold. In a one-track edition the row must start at least 44 px above it (BUGS 1).
    - **The hero bound (P-HK1):** at 1024, 1280 and 1920 px, on the home, What's new, every area page and every sampled
      course home. W is the width beside the sidebar:
      - a course home or area page: at least `max(370, .4 W - 22)`, or `.5 W - 22` below 900 px;
      - What's new: at least `.27 W - 22`;
      - the home: between `.4 W - 22` and `.54 W - 22`.
  - **New `check_frames`:** S-NAV1's checker's 4x CPU throttle frame test (`out/S-NAV1/checker.md` finding 1, its
    `perf.py`). It ran at 1280 x 800 on the home, the first area page and the sampled history and markdown course homes:
    `Emulation.setCPUThrottlingRate` 4, motion allowed, 5 s of requestAnimationFrame. The test is not in verify.py
    before this step and its script is gone, so it is rebuilt from the checker's description. The budget is set from
    measurements (see Tests): `FRAME_P50_MAX = (22, 32)` ms (a course or area home, the home), `LONGTASK_MAX = 250` ms.
  - **New `check_phone_identity`:** the phone byte identity, using `PHONE_EXPECTED`. How it is derived (a stored fixture
    of computed layout would not survive the next unit filed):
    - nav_diff_check proved that S-NAV2's every built difference is the theme CSS, the shell JS (the `?debug` readout,
      inert without `?debug`) and `--n` on `p.harea` (inert under the old CSS).
    - So the current `index.html` served with `PHONE_REF`'s `kit/shell.css` in its `<style>` *is* the start build's
      phone. `PHONE_REF` = 445b0c4, S-NAV2's `land.py start`, theme 6.19. The brand's tokens and comment strip are
      applied as `build.py` applies them.
    - The two are compared on five pages: the home, the first area page, a course home, a reading page (with its drawer
      open as well) and What's new.
    - Sizes and themes: 320 x 640 dark, 360 x 780 dark, 390 x 844 dark and light, all under reduced motion.
    - What is compared: every element of the bar, the drawer and the shown panel (its box and 35 computed properties),
      the page's scroll size and a full-page screenshot hash. Everything must be identical, and a difference must
      persist in three tries.
    - The result line prints `PHONE_EXPECTED` beside it: the theme CSS itself, and the area line's motion, which reduced
      motion does not run and `check_harea` checks.
    - It reads `PHONE_REF` with `git show`, and first fetches the one commit if the clone is shallow. If that cannot be
      read, it fails with the reason. A later row that changes the phone on purpose sets `PHONE_REF` to its own start.
  - **New `check_webkit`** (P-NAV3): `check_history` (`go()`'s pushes, popstate on back and forward, the scroll save,
    the replaceState fallback, the sandboxed iframe) and `check_pause` (`.topo.off`, top level and iframe) run in
    Playwright's WebKit, with their faults prefixed `webkit:`. If WebKit does not launch, it prints one line and returns.
  - **`main()`:** calls `check_nav` at 1024 x 768 and 1920 x 1080, `check_layouts`, `check_frames`,
    `check_phone_identity` and `check_webkit`, after the existing nav calls.
  - **Docstrings:** the module docstring (the three widths and the 1920 panel pass; the 1280 x 800 pass's 240 px
    sidebar; the home, topography and navigation widths; tall below 900 px; three columns from 960 px; the area-line
    widths; a new paragraph for step D and how to run a subset), and the docstrings of `check_topo`, `check_tiles` and
    `check_nav`.
- **`design/README.md`:**
  - a "Since 6.20 to 6.22 (S-NAV2)" paragraph: 6.20, 6.21 and 6.22 as steps A, B and C landed them; the P-NAV1, P-NAV2
    and P-NAV4 decisions;
  - the section 6 row of "What is in the file" (made false by step C: 300 px, desktop from 1100 px);
  - "Checks before republishing" (300 px sidebar, the widths, the new checks).
- **`kit/CHANGELOG.md`:** one "Where things stand" entry, S-NAV2 steps A to D: themes 6.20, 6.21 and 6.22, step D's
  checks, and P-NAV1 (kept, closed), P-NAV2 (kept, closed) and P-NAV4 (no action, closed). The row's close adds its own.
- **`out/S-NAV2/step-D-probe.py` and `step-D-probe2.py`:** the subset runners the docstring names.
  - `step-D-probe.py [--edition E] [--only nav1024,nav1920,nav1280,layouts,frames,phone,webkit]` runs step D's checks
    alone.
  - `step-D-probe2.py [--edition E] [--vp name,w,h,mobile ...] [--motion]` runs the home, topography, tile and area
    passes (and the home's motion) at given viewports, as `main()` does.
- **Not changed:** the theme, `kit/shell.css`, `kit/build.py`, `kit/shell.js`, any unit, brief or vault file.

## BUGS

1. **A one-track edition's home: the first tiles' titles and stats fall below the fold on a tablet landscape screen.**
   - Where: edition greece, `#home .track .cgrid > a.course` (the first tile).
     - At 1024 x 768: the tile row starts at 668 px, its title ends at 782 and its stats at 888 (fold 768).
     - At 1280 x 800: 675, 789 and 895 (fold 800).
   - Cause: in a one-track edition the track's band header (`#home > .track > .thead`: label, name, lede, count, about
     145 px) stands between the hero (388 to 394 px, its P-HK1 bound) and the tiles. Academy and marketing-ai have area
     tiles directly under the hero and pass: lowest stats at 710 of 768 and 716 of 800.
   - Not a one-line fix. Shrinking the hero breaks P-HK1's bound (its drawing's view), and hiding the band's lede or
     count on a landscape screen changes the design. Both are for Pedro.
   - The check: for a one-track home it requires only that the tile row starts 44 px above the fold, and prints where
     the title and stats end. The strict rule holds for every multi-track edition.
   - Proposal for the close: ⚠ a one-track home's band header compacted at tablet landscape (for example the lede
     hidden from 900 px under 860 px tall); every one-track edition's home changes there.

No other check exposed a layout fault.

## Tests

### New checks across academy (`step-D-probe.py`, no `--only`)

| Check | Time | Faults |
|---|---|---|
| nav 1024 x 768, 1920 x 1080, 1280 x 800 | 4, 4, 3 s | 0 (31 pages each) |
| layouts | 27 s | 0 |
| frames | 27 s | 0 |
| phone identity | 50 s | 0 |
| webkit | 0 s | skipped, one line |

- **Layouts:** 15 pages and 334 headings, figures and tables at each of the six viewports. Sidebar 240 px at
  1280 x 800, 259 at 1440 x 900, 300 at 1920 x 1080.
- **Fold:** 1024 x 768, lowest stats at 710 of 768; 1280 x 800, at 716 of 800.
- **Hero bound:**
  - 1024: home 388, new 254, the six area pages 388, greece and rome 427, brand-a and brand-b 388, ux-ia 427;
  - 1280: home 394, new 259, areas 394, course homes 394 to 427;
  - 1920: home 746, new 496, areas and course homes 626.
- **Frames, 1280 x 800, 4x:**
  - the home: 205 frames, p50 23.9 ms;
  - track-history, greece and brand-a: p50 16.7 to 17.5 ms;
  - no long task.
- **Phone identity:** 24 views, 0 differ, 0 retries.

### The existing passes at the new viewports (`step-D-probe2.py --motion`)

- At 1024 x 768 and 1920 x 1080, academy: home and What's new dark and light, 15 topography pages plus 9 reading pages
  dark and light, and the home's motion with `check_harea` (6 words and probes of 3, 4 and 8, each shown 3000 ms,
  overlap at most 350 ms). PASSED in 52 s.
- The same at 768, 1280 and 390 px, to prove the moved expectations change nothing there: PASSED in 43 s.
- The panel checks at 1920 x 1080: 301 panels, tightest gap 6 px, 0 faults, 223 s.

### Editions

- **`--edition greece`:**
  - probe: PASSED, after the one-track fold rule (BUGS 1);
    - layouts: 4 pages, 39 elements per viewport;
    - frames: home and greece 16.6 to 16.7 ms;
    - phone identity: 20 views, 0 differ;
    - nav: 0 faults at all three sizes;
  - probe2 `--motion`: PASSED in 13 s.
- **`--edition marketing-ai`:**
  - probe: PASSED;
    - layouts: 6 pages, 92 elements;
    - fold: 710 of 768 and 716 of 800;
    - frames: 16.5 to 16.6 ms;
    - phone identity: 24 views, 0 differ;
  - probe2 `--motion`: PASSED in 20 s.

### Negative controls (`/tmp/snd/neg.py`, `frames_neg.py`)

- **Faults injected into the served shell's CSS:**
  - the top bar moved below 1100 px;
  - the outline hidden on a desktop;
  - an outline forced at 1280 x 800;
  - a sidebar forced on a desktop home;
  - the home's hero 760 px tall;
  - h1 nowrap and hidden;
  - figure frames `overflow-x:hidden`.
- **What check_layouts reported:** 87 faults across every class:
  - top bar 45;
  - no outline 18;
  - outline where none 9;
  - sidebar without a sub-nav 6;
  - fold 2;
  - hero bound 2;
  - heading cut 14;
  - frame clips 33.
- **Phone identity**, with the reference theme given one extra rule (`.lede{letter-spacing:.02em}`): 4 of 6 views fail
  at 390 px.
- **Frames**, with the pause observer removed (S-NAV1's fault), 4x at 1280 x 800: greece 30.8 ms, rome 30.8 ms, ux-ia
  32.6 ms. All are over the 22 ms course-home budget.

### The frame budget, how it was set

- The home's median is paint-bound on this GPU-less machine. It varies from run to run: 21.1 to 28.3 ms throttled, and
  16.9 to 21.8 ms unthrottled.
- The build before 6.22 (step C's start copy) measured the same at 1280 x 800: 21.1 to 25.3 ms in three runs, against
  21.7 to 23.9 now. So 6.22 adds no cost.
- A single absolute budget cannot separate the home's paint from the fault (30.8 or more). A ratio to the unthrottled
  run was tried and was flaky too.
- Hence two budgets: 22 ms for a course or area home and 32 ms for the home. Long tasks are 0 in every measured run;
  the limit is 250 ms.

### WebKit (P-NAV3)

- `python3 -m playwright install webkit` failed: the proxy returned 403 `request blocked: no rule or allowlist entry
  allows host` for `cdn.playwright.dev` and `playwright.download.prss.microsoft.com`. Not retried. No system
  dependencies were tried, since there is no browser to run them with.
- `check_webkit` prints: `webkit: not available here (BrowserType.launch: Executable doesn't exist at
  /opt/pw-browsers/webkit-2359/pw_run.sh); history, the scroll save and the pause observer left to an iPhone (P-NAV3)`.
- Its pass was dry-run with Chromium standing in for WebKit (`/tmp/snd/wk_dry.py`). History home > track-history >
  greece > m01, the backs and the forward each restoring their scroll; the fallback and the iframe; pause, 10 in view
  and 74 out of view. It passes, so the code path works once WebKit is installed.
- The row's P-NAV3 stays Pedro's check on an iPhone.

### Other

- **`python3 kit/baseline.py --check`:** academy 460 files, 0 differ; greece 82 files, 0 differ; clean. Step D changes
  no built output.
- **`git diff --stat`:** `kit/verify.py`, `design/README.md` and `kit/CHANGELOG.md`, plus the two new `out/S-NAV2`
  scripts and this file. `out/S-NAV2/landing-report.md` was already modified before this step and was not touched by it.

## Time added to verify.py

| Run | Added | Of which |
|---|---|---|
| A full run (a theme or kit change; about 36 min at step C) | about 6.5 min | the 1920 x 1080 panel pass 3.7 min; phone identity 0.9; the passes at the two new viewports 0.9; layouts 0.5; frames 0.5; nav 0.15 |
| A scoped run | about 3 min | the panel pass at 1920 takes only the scoped pages; the rest is edition-wide |

## For the main chat

- **Landing:** `drop:` entries from `git diff -U0 HEAD` for the replaced lines:
  - `kit/verify.py`: the docstring lines, `HOME_JS`'s `phone`/`desk` line, its layout comment, `side` and `want`
    lines, `check_topo`'s docstring line and `desk` line, `check_tiles`' `want` line and docstring, `check_nav`'s
    `else:` branch and docstring, and the three `main()` loop headers and the nav call block;
  - `design/README.md`: the section 6 row and the "Checks before republishing" paragraph.
  
  `kit/CHANGELOG.md` only gains a line. No built file changes, so `baseline.py` needs no re-record for this step,
  unless the main chat does it anyway.
- **`verify.py --full`** (the main chat's) now runs the new checks. WebKit prints its one line.
- **To flag to Pedro:**
  - **BUGS 1:** the greece home's fold, ⚠ proposal.
  - **P-NAV3:** WebKit could not be installed here (egress blocked); the iPhone check stays his.
  - Step C's NEEDS PEDRO 1 and 2 are unchanged. The check encodes the drawer at 900 to 1099 px and an outline of
    sections only. If Pedro takes the 900 px sidebar, `layout_of` and `side_px` move with it.
- **For the checker:**
  - The 1280 x 800 pass keeps the label 'desktop'.
  - `PHONE_REF` is S-NAV2's start; after this row lands, a later row that means to change the phone moves it.
  - The phone identity check needs `git` and the one commit (it fetches it into a shallow clone).
