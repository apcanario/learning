# S-NAV1 · Step B · area homes

Model: Opus 5.5 (claude-opus-5-5), a fresh agent. 21 Nov 2026.

## Verdict

Done. An edition of two or more tracks (academy, marketing-ai) has one area page `track-<id>` per track; the home keeps
its hero and shows one tile per track; crumbs read Home › Area › Course › Unit. An edition of one track (greece) has no
area level. The history test walks home → area → course → unit with three backs and passes. No commit, no push, no
land.py, `kit/baseline.json` not re-recorded. No unit, brief, vault or course file changed; shell.js unchanged.

## What changed

**kit/build.py**
- `MULTI = len(THEMES) > 1`; `AREA_OF` maps each course page (history home, markdown sub-course) to its track.
- `crumbs()`: with MULTI, a crumb that links to a course page is preceded by its area's crumb (track name → `track-<id>`)
  unless the trail already has it. So reading pages, syllabi, How it was built and the markdown sub-pages gain the area.
  Course homes already named it. Without MULTI, a crumb to `track-*` is dropped, so greece's course home reads
  Home › Greece. mdcourse.py and howbuilt.py are unchanged because the insertion happens in the one `crumbs()` they are given.
- `track_body(t, ph)`: the old per-track loop body (course tiles, `extra`, the folded planned list, the count line),
  with the phases taken in the same order as before. It also returns the track's courses as rises and its stats.
- Single track: the home is byte-identical to before (`section.track` with its header).
- MULTI: the home's `{tracks}` slot is `<div class="cgrid areas">`, one tile per track built by `tile()`. Each tile
  shows the chip `Area · <name>`, a status pill (`complete` only when every live course is complete and none is coming
  soon or planned, else `in progress`), the name, the lede, and three stats: live courses, units written, units in all.
  Its patch has one rise per course: a live course sized by its words, a coming-soon or planned course flat. The tile
  links to `#track-<id>`. Home phases are `phases(1 + tracks)`, and the hero stays at 0.
- Area panels: `<section class="panel home area" id="track-<id>" data-ctx="root" data-kind="area" data-t=<name>
  data-u="AREA">`. Each holds:
  - a `hero has-topo` with a layer over the same rises, in the track's tone, a contour every 5.5th of the largest course;
  - crumbs Home › Area;
  - an eyebrow (AREA plus the old count line), h1, lede, and `stats data-n="3"` (courses, units written of total, hours);
  - then `section.track` holding the course tiles, `extra` and the planned `<details>` (same ids, e.g. `#planned-courses`).

  Area panels stay in the shell (not split, no fetch). They sit after the home in panel order. The shell is 591 KB.
- Root drawer (MULTI only): each track group now starts with `a.ditem.dcourse.darea` → `#track-<id>` ("<name> / the
  area's home"), so the area page is reachable from the existing nav and its group opens when it is shown. Nothing else
  in the nav changed (Step C).

**design/theme.css → kit/shell.css** (identical copies). One selector added: the ≤400 px `.panel.root .track` padding
rule also covers `.panel.area>.track`, so the band reads as it did on the home. All other styling for the new pages
already existed (`.panel.home`, `.hero.has-topo` with its 380 px minimum, `.cgrid`, `.panel.root>.cgrid`, `.track`).

**kit/verify.py**
- Globals: `AREA_IDS` (empty for one track), `MULTI`, `AREA_OF`, `HOME_GRID`.
- `home_expect()`: adds `area_pages`: for each track, name, lede, courses, planned names, and rises in build order.
- `HOME_JS` / `check_home`: an `areas` option. The order becomes hero, `div.cgrid.areas`, rules, links, New since, link.
  The first tile's title must start on the first screen. The tiles are checked against `area_pages`: rises, flat
  rings, href. The area tile's line is the lede, clamped to two lines as every closed tile's line is, so the "clipped"
  rule is off for area tiles only. The track copy and planned checks move to the area page.
- New `AREA_JS` / `check_area`. It checks the crumbs (site, then area as current), eyebrow AREA, h1, lede, page
  structure (hero, then band), course tiles in catalog order linking to their courses, `extra`, the planned list id, and
  that the home tile's stats and the hero's first two stats equal what the band holds.
- `check_topo`: an area page's hero against `area_pages` rises. `check_tiles`: an area page's ghosts are its own track's
  planned courses; with MULTI the home has none.
- `check_history`: the extension point is filled. `HIST_PATH_JS` returns two levels with area pages (home's first area
  tile, then that area's first course tile), so the walk is home → area → course → unit and the backs cover three
  levels. Change: a page with less than 250 px to scroll is scrolled to its foot instead of to 40%, and the test fails
  only under 30 px. marketing-ai's one-course area pages scroll 72 px. Academy's walk is unchanged (y=238 on track-history).
- `main()`:
  - `tap_course()`: with MULTI the navigation walk goes home tile → area page (checked as a step: nav root, AREA, name,
    no arrows) → course tile.
  - The "home tracks" check reads the home's area tiles and each area page's course tiles against `HOME_TRACKS`.
  - The tablet and desktop grid checks use `HOME_GRID`; the mythos/logos grid is found on its area page.
  - The desktop taps tap course tiles on their area page and the home's first area tile.
  - `AREA_IDS` are added to `TOPO_ALL` (topography, tiles, motion poses, hero text contrast, shots) and to
    `check_contrast`'s pages. Each area page also gets `check_area` in the pages pass.
- Docstring paragraph "Area pages (S-NAV1 step B)" added.

**kit/verify_scope.py**: area pages (`data-kind="area"`) are checked in every run, as the home is. Every filing in a
track changes their tiles. Docstring updated.

**kit/index_check.py**: not changed. It does not enumerate pages.

## Single-track edition (greece)

`MULTI` is false. The home, its `section.track#track-history`, the drawer and phases are as before (index.html differs
only by the CSS selector). No `track-*` panel is built. The one crumb that named the area (the course home's) is dropped:
Home › Greece. Reading pages had no area crumb and are unchanged. In verify every new branch is off; the history walk
stays home → course → unit.

## Tests

- `check_history` (harness importing verify.py, record not written):
  - academy: home (y=1175) → track-history (y=238) → greece (y=6500) → m01 (y=630). Back to greece 6500, track-history
    238, home 1175. Forward to m01 630. The pushState-refused walk and the sandboxed-iframe walk pass. HISTORY CHECKS PASSED.
  - greece: home → greece → m01, unchanged. PASSED.
  - marketing-ai: home → track-marketing (y=72) → personal-brand-pb → read-pb1, three backs. PASSED.
- Narrow page checks (`/tmp/snav1b/scripts/narrow.py`) at 320, 390, 768 and 1280 px, dark and light: `check_home`,
  `check_topo`/`check_tiles` on the home, then `check_area` + `check_topo` + `check_tiles` on every area page (planned
  open). With motion: every area page at the five poses with `texts_contrast`, plus the home's motion check. academy
  NARROW CHECKS PASSED, greece PASSED, marketing-ai passed (its only failures were the history scroll, since fixed).
- `main()` with the heavy per-page passes stubbed (`/tmp/snav1b/scripts/navonly.py`). This runs the nav walk through
  area pages, drawers, root drawer groups, home tracks, the tablet and desktop passes, and the desktop taps (home → area,
  area → course).
  - marketing-ai: ALL CHECKS PASSED.
  - academy and greece: one fail each, "Gentium Book Plus not loaded". This is an artifact of stubbing
    `check_panels`, which in a real run opens every panel's details (the mythos/logos block) before the font check.
    greece, with untouched code paths, shows the same.
- `python3 kit/baseline.py --check` (clean before the change): academy 262 differ, greece 2, 0 added, 0 removed.
  Listed in `out/S-NAV1/expected-B.txt`:
  - academy: `README.md` (size table), `academy/index.html`, and 260 split pages. Each was proved to differ only inside
    `<nav class="crumbs">` (the area crumb added).
  - greece: `editions/greece/index.html` (CSS) and `editions/greece/greece/home.html` (crumb dropped).
  - In index.html, every panel other than `home` and the new `track-*` differs only by crumbs, plus the drawer and CSS.
  - The drawer class was fixed after the check (`ditem darea` → `ditem dcourse darea`, same file, index.html only), so the
    list stands.
- Not run: `verify.py --full`.

## Open choices (taken, recorded)

- The area tile's line is the track's whole lede, clamped to two lines with an ellipsis, as every closed tile's line is.
  It is shown whole on the area page. The alternative was a new short `tile` key per track in catalog.toml.
- Area tile stats are live courses, units written and units in all. Planned and coming-soon courses are not counted but
  appear as flat rings. Pill: `in progress` while anything in the track is coming soon or planned (so History is
  `in progress` though Greece and Rome are complete).
- The area page has a hero over a topography (one rise per course, the track's tone), so Step D has an area hero to
  animate. It adds three stats so the hero is about as tall as a course home's.
- The area pages stay in the shell, not split into files. The shell grew from 567 to 591 KB. A fetch would have needed
  `data-anchors` for the moved `#planned-courses`.
- Panel class `panel home area`, kind `area`, ctx `root`: no prev/next arrows, root drawer shown. shell.js needed no
  change.
- The drawer entry for the area is an extra row at the head of each track group, not a link on the group header. Step C
  replaces the nav.
- `#track-<id>` ids moved from the home's sections to the area panels, so every existing link to `#track-history`
  (course home crumbs) now opens the area page.
- Docs the row makes false (design/README.md "Where the tile is used" and theme section 4h/6, catalog.toml header on
  `extra`/planned "shown on the home", `docs/method.md` if it describes the home) are outside this step's files. They
  are left for the row's close.

## Blockers

None. No permission check refused a script. Scratch harnesses and logs are in `/tmp/snav1b/` (not in the repo).
