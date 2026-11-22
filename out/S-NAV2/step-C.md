# S-NAV2 step C · the tablet and desktop layouts

Model: Opus 5.5 (`claude-opus-5-5`), a fresh agent. 22 Nov 2026. Nothing committed, pushed or landed; `kit/baseline.json`
not re-recorded; `kit/land.py` not run; `kit/verify-hashes.json` untouched. All changes are uncommitted in the working
tree, on top of HEAD 4a825a3 (steps A and B landed).

## Verdict

Done, CSS only. No markup, `kit/build.py`, `kit/viz.py` or `kit/shell.js` change. Two things the spec asks for cannot be
done in CSS alone. Each has its closest CSS-only layout built, and each is listed under NEEDS PEDRO. The phone (below
768 px, every width of the drawer range up to 767 px) is pixel- and layout-identical to the start build.

## NEEDS PEDRO

1. **A sidebar from 900 px (tablet landscape, 900 to 1099 px).**
   - Why it needs a script change: `kit/shell.js` makes the drawer a sidebar only at `(min-width:1100px)` (`wide`,
     `syncWide`, `closeDrawer` set `aria-hidden` from it).
   - What CSS alone would give: a sidebar at 900 to 1099 px stays `aria-hidden="true"`, so it is visible and clickable
     but hidden from a screen reader. That is an accessibility fault, so it was not done.
   - What was built instead: 900 to 1099 px keeps the drawer and gets the rest of the tablet landscape layout (wide homes,
     three columns where the width allows, the wide hero layout, the capped hero).
   - The fix, if Pedro wants it: one line in `shell.js`, `matchMedia('(min-width:1100px)')` to `(min-width:900px)`, plus
     the theme's sidebar rules from 900 px. Not done.
   - A 1280 x 800 tablet (the Y700) is 1100 px or wider, so it already gets the 240 px sidebar.
2. **The outline lists the unit's sections, not its subsections.**
   - What it is: the on-this-page outline at a unit's right is the unit's own section menu, `.secmenu` > `ol.seclist`,
     one entry per h2, with the Sources links and "Whole unit" under it. It is shown beside the section bar with the
     `::details-content` pseudo-element.
   - What is missing: the h3 subsections have no entries in any markup, so listing them needs a build change (a nested
     list in `mdcourse.reading`).
   - Browser support: `::details-content` is in Chrome 131+, Safari 18.4+ and recent Firefox. It sits behind
     `@supports selector(::details-content)`; a browser without it keeps the section menu as before, and no space is
     reserved.

## What changed

- **`design/theme.css`, copied to `kit/shell.css`.** `cmp` is identical and `rot_check` is OK. The changes:
  - Version 6.22 header entry and the Contents line for section 6.
  - One new block at the end of section 6 (`/* S-NAV2 step C ... */`), placed before section 7.
  - No existing rule was edited.
  - Every new rule sits under a media query of 768 px or wider, or under `@container (min-width:960px)`. The body is the
    only container on that path, so a phone never reaches it.
- **`kit/verify.py`**, only what the existing 1280 x 800 checks need now that 1280 x 800 is the tablet landscape layout.
  Each change is commented `S-NAV2 step C`:
  - `SIDE` 300 → 240.
  - `HOME_JS`: the hero layer's left edge is 240 at 1100 px or wider under 860 px tall, and 0 for a desktop home.
  - `HOME_JS` and `check_tiles`: the tile columns expected are 3 when the body's content width (beside the sidebar) is
    960 px or more, else 2.
  - Desktop pass: the home cards are expected in 3 columns.
- **Rebuilt outputs.** `kit/academy/index.html` (the inlined theme only), `kit/README.md` (size table: the shell 620 KB →
  628 KB) and `editions/greece/index.html`. The marketing-ai site was rebuilt too (ignored by git).

## The layouts (theme.css section 6, the S-NAV2 step C block)

### Tablet portrait, 768 to 899 px

- The drawer stays.
- `main` and `.top-in` lose their 760 px cap, so the column is the screen's width less 16 px gutters (768 px gives
  736 px, against 728 before).
- Tiles stay two across.
- Course homes and area pages: the hero is at least `max(370px, 50cqw - 22px)` (the tall layout's bound). At 768 that
  is 370, unchanged.
- The home's hero: `min(70svh, 100cqw - 22px)`, so the square tall layout's sides stay whole. At 768 x 1024 it is
  unchanged.
- A hero with contours is a flex column: the crumbs at its top, the copy at its foot, the contours between, as on the
  home. This keeps a bound-tall hero from leaving an empty band under its stats.

### Tablet landscape, 900 to 1099 px, and 1100 px or wider under 860 px tall

- The homes (the Academy home, the area pages and the course homes) widen to 1080 px. Reading and other pages keep 760 px.
- Tiles:
  - Three across once the width beside the sidebar reaches 960 px (`@container`), two below.
  - A lone tile stays half the grid (`width: calc(150% + 6px)`).
  - Two tiles take a third each.
- Every hero's contours use the wide layout from 900 px (it was 1100). A landscape frame is about 2.5:1, and the square
  tall layout would need a hero half the width tall.
- The Academy home's hero is `40cqw - 22px`, not 70% of the screen. At 1280 x 800 the hero is 394 px and the first
  tiles' titles and stats sit above the fold (shot).
- From 1100 px the sidebar is 240 px (was 300) and holds both navs, as before.
- Running text in a wide home's `.howto` keeps a 72ch measure.

### Desktop, 1100 px or wider and 860 px tall or more

- **The top bar** runs across the screen:
  - `.dhead`, the brand, is fixed at the top left over the sidebar.
  - `nav.main-nav` is fixed in the bar beside it: horizontal, 44 px targets, the reader's area marked by a 2 px rule in
    its tone.
  - Then theme, previous and next at the right.
- **What stands down:** `.cur` (the current-page line) and `#homeB`. The main nav's Home, the sidebar's highlighted item
  and the page's own crumbs carry them.
- **The sidebar** (`--side: clamp(240px, 18vw, 300px)`) starts under the bar and holds only `nav.sub-nav`.
  - On the home and its site pages (What's new, the Changelog, the Backlog, Figure kinds) the sub-nav is `[hidden]`, so
    `body:has(.sub-nav[hidden])` drops the sidebar: no padding, the drawer `visibility:hidden`, its brand and main nav
    `visible`. Those pages take the full width.
- **The column** is centred:
  - 860 px for every page; the homes 1200 px, tiles three across.
  - A reading page's text keeps its 68ch, so its figures, tables, bands and section bar run wider than the text: about
    828 px against about 600.
- **The outline** sits at the right of a unit page (`--toc: clamp(200px, 16vw, 280px)`, reserved as the body's right
  padding only while a report panel is shown):
  - The section menu's `::details-content` is absolutely positioned beside the sticky section bar, so it sticks with it.
  - It is at most the window's height less the bar, and scrolls on its own.
  - The current section is marked by `aria-current`, which `shell.js` already sets.
  - The menu's summary takes no clicks there, and its chevron is hidden.
- **The Academy home's hero** is `clamp(40cqw - 22px, 62svh, 54cqw - 22px)`:
  - 558 px at 1440 x 900;
  - 746 px at 1920 x 1080, held up by the 40cqw bound, since there is no sidebar on the home.

### Choices taken (recorded)

- **The main nav stays in the sidebar on a tablet landscape screen.** The spec puts it in the top bar only for the
  desktop.
- **No sidebar where there is no sub-nav (desktop).** Otherwise the home would show an empty 260 px column.
- **Wide hero layout from 900 px**, not 1100.
- **Two tiles in a three-column grid take a third each.** Only the lone tile is held to half (P90).

## The heroes (P-HK1, the bound at every width)

A hero's layer is W = 100cqw of the body (the width beside the sidebar) by H = the hero + 22 px. It is drawn slice.

| Layout | viewBox | Shows its view when | Bound written |
|---|---|---|---|
| Course home and area page, wide | 1000 x 500 | H ≥ .4 W | `max(370px, 40cqw - 22px)` from 900 px |
| Course home and area page, tall | 1000 x 1000 | H ≥ .5 W | `max(370px, 50cqw - 22px)`, 768 to 899 px |
| What's new, wide | 1000 x 270 | its frame that shape: H ≈ .27 W | `27cqw - 22px` from 900 px |
| The Academy home, wide | 1000 x 571 | between 40cqw and 54cqw | as above |

What's new is the reason it needs its own bound. With no bound its 1920 px hero cut the rings of the day 2026-11-01. With
the course homes' 40cqw bound its sides were cut instead (the day 2026-10-22), since a taller frame crops a 1000 x 270
drawing at the sides.

Course-home and area hero heights:

| Viewport | Width beside the sidebar | Hero |
|---|---|---|
| 1024 x 768 | 1024 | 388 px |
| 1280 x 800 | 1040 | 394 px |
| 1440 x 900 | 1181 | 450 px |
| 1920 x 1080 | 1620 | 626 px |

**Byte budgets (P-NAV1): no change to any page's bytes but the shell's CSS.** The heroes' drawings are unchanged
(nav_diff_check: 2417 drawings the same), so no hero layer, page or the shell passes a size limit. The shell is 628 KB
against the 1 MB limit, and the largest hero layer is unchanged under 20 KB. P-NAV1's raise stands.

## Tests

- **`python3 kit/baseline.py --check`**, after the final change:
  - academy: 460 files, 2 differ (`README.md`, `academy/index.html`);
  - greece: 82 files, 1 differs (`editions/greece/index.html`);
  - 0 added, 0 removed.
  - `academy/index.html` outside its `<style>` is byte-identical to the start build, and its `<style>` equals
    `design/theme.css`. `README.md` differs only in the shell's size-table row.
- **`python3 kit/nav_diff_check.py --build HEAD --now-tree /home/claude/learning`** (marketing-ai built in the tree
  first): NAV DIFF CHECK PASSED.

  | Edition | Classes that differ | Reading pages identical |
  |---|---|---|
  | academy | theme CSS 1, size table 1 | 566 |
  | greece | theme CSS 1 | 162 |
  | marketing-ai | theme CSS 1 | 76 |

  All 2417 + 712 + 307 drawings are the same.
- **Phone identity** (`/tmp/snc/scripts/phone_cmp2.py`): the start build (HEAD 4a825a3, copied before any change) against
  the current build.
  - Scope: 12 pages (home, track-history, greece, m23, ux-ia, read-ia3, new, changelog, backlog, syllabus, ux-ia-briefs,
    read-sce1) at 320 x 640, 360 x 780, 390 x 844, 430 x 932 and 767 x 1024, dark and light, reduced motion.
  - What is compared: each page's whole computed layout (every element's box and 35 computed properties), a full-page
    screenshot, and the drawer opened (layout and screenshot).
  - A difference had to persist in three fresh tries. Result: 120 page views, 0 differ, 1 transient retry.
  - An earlier single-try run showed 1 to 3 timing flakes, each in a different place (a figure's cue line on a hidden
    section, the drawer shot).
  - The last theme edit (the hero's flex column in the 768 to 899 px block) came after this run. It sits inside
    `@media (min-width:768px) and (max-width:899.98px)`, so it cannot reach 767 px or less.
  - `PHONE_EXPECTED` (step A's expected phone differences) is unchanged, since this step adds none.
- **Full `verify.py` in a throwaway copy** (`/tmp/snc/repo`, not the clone, so no `verify-hashes.json` was written to
  the repo):
  - It ran with the theme as of the main layout work, before the header comment and the 768 to 899 px hero flex.
  - Two FAILs, both from the copy not being rebuilt: the README size table, and `rot` (shell.css not yet copied in the
    copy).
  - Everything else passed: tablet 768, desktop 1280 x 800, phone, motion, contrast, separators, reliefs, nav, history,
    debug.
  - After the rebuild here, `rot_check.py` is OK and the size table is the build's.
- **Narrow probes after the final change** (scripts in `/tmp/snc/scripts/`, importing verify.py's own checks; nothing
  recorded):
  - `topo_probe.py`: check_home, check_topo, check_tiles and check_area on the home, the sampled course homes, every area
    page and What's new, dark and light, reduced motion, with the motion poses at 0, .25, .5, .75 and 1 (plus
    texts_contrast).
    - Viewports: 768 x 1024, 800 x 1100, 1280 x 800, 1440 x 900 and 1920 x 1080. 0 faults.
    - At 1024 x 768 the only faults are "layout shown is wide, expected tall": the check's `desk = w >= 1100`, while the
      wide layout now starts at 900 (step D).
    - greece and marketing-ai at 1280 x 800, 1440 x 900 and 1920 x 1080: 0 faults.
  - `panels_probe.py` (verify's `check_panels`: every panel with every `<details>` open; no sideways scroll, gaps of at
    least 6 px, targets of at least 44 px): 301 panels at 768 x 1024, 1024 x 768, 1440 x 900 and 1920 x 1080, 0 faults.
  - `wide_probe.py`: 18 pages at 1920 x 1080, 1440 x 900, 1280 x 800, 1024 x 768, 800 x 1100, 900 x 700, 1100 x 860
    and 1099 x 900, dark and light. 0 faults:
    - no sideways scroll;
    - no h1, h2, h3, figure, table, tile, section bar or hero past the column, the screen or the sidebar;
    - no clipped heading;
    - nothing under the outline;
    - the outline, sidebar and top bar where the spec puts them (printed: e.g. 1440 x 900 read-ia3: sidebar 259, top
      bar 0..1440, main nav fixed at the top, outline 1189..1380, column 860 from 304);
    - the same for greece and marketing-ai.
- **Other checks:**
  - `rot_check.py`: OK.
  - `private_terms.py`: 0 private terms, OK.
  - `index_check.py`: matches.
  - `verify.py --full`: not run (as instructed).
- **Screenshots** (my own review; not in the commit): `/tmp/snc/shots-final/`, 24 shots, 5.6 MB.
  - Pages: home, track-history, ux-ia (course home), read-ia3 (unit).
  - Viewports: 1440 x 900, 1280 x 800 and 800 x 1100, dark and light.
  - Scrolled desktop unit pages (the outline beside the stuck bar, a wide figure) are in `/tmp/snc/shots3/`.
- **Fixed after looking:**
  - The 3-column lone tile (was a third; now half).
  - An over-long measure in a wide course home's "What you will be able to do" box (now 72ch).
  - The bound-tall area hero leaving an empty band under its stats (the copy now sits at the hero's foot).
  - What's new's hero (its own 27cqw bound).

## For step D (verify.py's new viewports and checks)

- **Layout expectations:**
  - `check_topo`'s and `HOME_JS`'s `desk = w >= 1100` (which layout is shown) should be `>= 900`.
  - The sidebar should be expected only from 1100 px:
    - 240 px under 860 px tall;
    - `clamp(240px, 18vw, 300px)` at 860 px or taller;
    - none on a desktop home or site page.
- **Navigation:**
  - `check_nav`'s "from 1100 px both navs stand in the sidebar" holds only under 860 px tall. On a desktop, the main nav
    is fixed in the top bar (top 0, left `--side`) and the sub-nav is in the sidebar.
  - `.cur` and `#homeB` are `display:none` on a desktop.
- **Columns:**
  - The desktop column is 860 px (homes 1200 px); tablet landscape homes are 1080 px.
  - The desktop pass's "main column about 760" and 68ch-measure checks hold at 1280 x 800, not on a desktop.
- **The outline:** check `.panel[data-kind="report"] .secmenu::details-content` (or `ol.seclist`'s box): beside the
  section bar, inside the window, not over the column. On desktops only, and only where `::details-content` is
  supported.
- **Tiles:** three across when the body's content width is 960 px or more (already in `HOME_JS` and `check_tiles`); a
  lone tile half; two tiles a third each.
- **The hero bound to check at 1024, 1280 and 1920 px:** course and area heroes at least `max(370, .4 W - 22)` once wide
  and `max(370, .5 W - 22)` from 768 to 899 px; What's new at least `.27 W - 22`; the Academy home between
  `.4 W - 22` and `.54 W - 22`.
- **Focus order on a desktop:** top bar buttons, then the main nav, then the sidebar, then the content (DOM order; the
  main nav is visually left of the theme button). Not a fault, but step D or the checker may want to note it.

## For the main chat (landing)

- The `drop:` entries come from `git diff -U0 HEAD`.
  - Replaced lines: `kit/verify.py` (the 5 changed lines), `kit/README.md` (the shell row), `kit/academy/index.html`
    (the contents lines of the inlined theme), and `design/theme.css` / `kit/shell.css` (the two Contents lines for
    section 6).
  - Everything else in the theme is added.
- `design/README.md` and `kit/CHANGELOG.md` do not yet record 6.22 (left to the close, as for 6.20 and 6.21).
  `design/README.md`'s section 6 row ("Desktop from 1100 px: `--side` 300 px") and its "Checks before republishing"
  paragraph ("a 300 px sidebar") are now false.
- `kit/verify.py`'s docstring still says "Desktop: the drawer is a persistent 300 px sidebar". Left for step D, which
  rewrites those checks.
