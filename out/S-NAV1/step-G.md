# S-NAV1 · Step G · the fresh check's findings applied

Model: Opus 5.5 (claude-opus-5-5), a fresh agent. 22 Nov 2026.

## Verdict

Done. Findings 1 to 6, 8 and 9 are applied. All three editions were built. The narrow checks passed on academy, greece
and marketing-ai at 320, 390, 768 and 1280 px, dark and light. The checks were swell, topo, home, relief (with the
wall), nav, history and the new pause check. `nav_diff_check.py` passes against the start build on all three
editions. Every drawing draws the same levels as at the start, except the home tiles that step B replaced.

Two budgets were raised. Each is marked ⚠ for Pedro below. No other check was loosened.

The rest is left to the main chat: no commit, push or `land.py` was run, and `kit/baseline.json` and
`kit/verify-hashes.json` are untouched. No unit, brief, vault or course file changed. No permission check refused a
script.

## Finding 1 (blocking) · off-screen drawings pause

**The change**
- `kit/shell.js`: one IntersectionObserver watches every `.topo`: hero layers, tile patches, separators and reliefs.
  - It watches the drawings in the page at load, and a fetched panel's drawings when the panel lands (`watchTopo` in
    `load()`).
  - It marks a drawing outside the viewport `.off` and unmarks it when it comes into view.
  - A WeakSet keeps any drawing from being observed twice. Nothing is written to the DOM except the class.
  - Without IntersectionObserver nothing happens, and every drawing runs as before.
- `design/theme.css` = `kit/shell.css`, version 6.19: `.topo.off path{animation-play-state:paused}` (4i), plus the
  version entry and the 4i comment.
  - A paused drawing keeps its pose and goes on from there. A drawing moves as one, so no join opens.
  - Under reduced motion nothing animates, so the class changes nothing.
  - A hidden panel never intersects, so its drawings are `.off` too.
- `kit/verify.py`: the byte and class checks now read a drawing without the runtime `.off`. These are the home's
  `topoBytes`, TOPO_JS bytes, the tile children in the home and tile checks, the separator's class and bytes, and the
  relief's class and bytes. Without this, an off-screen drawing would gain 4 bytes and fail a class string.

**The new check: `check_pause(br, fails, w=390, h=844, theme='dark')`, run from `main()` after `check_swell`**
- It looks at the home, then a course home at its top and scrolled to its last moving drawing, then goes back home
  through `history.back()`.
- It does this at the top level and inside a sandboxed iframe (`allow-scripts allow-same-origin`).
- Each look is two samples 300 ms apart:
  - every drawing in view is not `.off`, its swells are `running`, and their `currentTime` advances;
  - every drawing out of view is `.off`, its swells are `paused`, and their `currentTime` does not change;
  - no drawing of a hidden panel is unmarked.
- Under reduced motion, no swell exists, whether the page is scrolled or not.
- Negative control: with IntersectionObserver removed by an init script, the check fails 82 times ("a patch out of
  view is on, its swells running, moving").

**Frame timing**

Measured with the checker's method: 390 px, mobile, 4× CPU throttle, motion allowed, 5 s of requestAnimationFrame.

| Page | start | step D (pre-fix) | step G |
|---|---|---|---|
| greece (course home) | 301 frames, p50 16.7 ms, long tasks 0 ms | 179, 33.3 ms, 286 ms | 300, 16.7 ms, 0 ms |
| rome (course home) | 301, 16.7 ms, 0 ms | 190, 33.3 ms, 105 ms | 300, 16.7 ms, 0 ms |
| home | 300, 16.7 ms (p95 16.8), 0 ms | 287, 16.7 ms (p95 33.2), 0 ms | 299, 16.7 ms (p95 16.8), 0 ms |

The checker's proposed long-task budget check was not added. The task asked for the pause check, and the pause check
covers the cause.

## Finding 2 · the home hero's levels: back to the start's, budget raised ⚠

**Cutting bytes first.** At 24,500 words a level, academy's layer is 23,124 B. Of that:
- 2,128 B are the new `style` attributes (`--d`, and `--o` on 31 shared-line paths);
- about 1,566 B are the per-level path tags: 99 paths, where the start drew 12.

Even with no `style` attribute at all, the layer would be 20,996 B. That is over the 19,456 B budget and over verify's
20,480 B cap. Every byte-saving option that leaves the drawing unchanged was weighed, and none brings it under:
- dropping `px` from `--o` needs two variables of the same length;
- one `--d` per `<g>` saves nothing, since a level is already one path;
- shorter variable names cannot get shorter (the names are already one letter);
- rounding `--d` to one decimal changes the motion.

So no cut was applied.

**The raise, ⚠ for a proposal in the row's close:**
- `kit/build.py`: `HERO_BUDGET` goes from 19,456 to 23,124 B (+3,668). This is the smallest budget at which the scan
  stops at the start's interval:
  - at 24,500 the layer is 23,124 B, so 24,500 fits;
  - at 24,400 it is 23,254 B, and at 24,000 to 24,300 it is 23,439 to 23,884 B, so none of those fits.
- `kit/verify.py`: a new `HOME_TOPO_MAX` goes from 20,480 to 24,148 B (+3,668). This keeps P-HERO1's 1 KB of headroom.
  - It applies to the home's hero only. Course homes, area pages and What's new keep their 20 KB.
- Comments in both files record the old values and the reason.

**Result**
- Academy is drawn at 24,500 words a level again, as at the start. Step D had 29,000.
- Levels at start → step D → step G:
  - History 20 → 17 → 20
  - Marketing 7 → 5 → 7
  - Technology 8 → 7 → 8
  - UX 6 → 5 → 6
  - Sports 5 → 4 → 5
- The layer measures 23,124 B in the browser, and its levels equal the start's on every layout.
- Greece (5,826 B) and marketing-ai (5,071 B) are unchanged at 24,000.
- Academy's build is back to about 157 s; it was about 197 s with the scan.

## Finding 3 · the wall relief's rings: back to the start's, budget raised ⚠

**Cutting bytes first.** An inside line (the outline and the levels inside it) now carries no class: only the halo is
`path.rl-out`. The changes:
- theme: `.topo.relief path{stroke:var(--c)}`;
- `viz._relief_at`;
- verify's REL_JS: an inside path has no class (`path:not([class])`), a halo path is `rl-out`, and nothing else is
  allowed.

The rendering is unchanged. The cut saves 15 B per inside path: the wall at every level, unsimplified, went from
19,781 to 17,821 B (−1,960). It still cannot fit 12,288 B without thinning.

**The raise, ⚠ for a proposal:**
- `viz.REL_MAX` goes from 12,288 to 17,821 B (+5,533). This is the smallest budget at which the wall is drawn as at
  the start: every level (k = 1) and no simplification (eps 0).
- REL_JS's cap now reads `viz.REL_MAX`, the same number.

**Result**
- The wall on greece r-6.3, r-10.10, r-12.6 and rome r-3.3 (m63, m1010, m126, rm33) has 164 inside rings again, as at
  the start. Step D had 84. The halo has 41.
- In the browser it measures 17,496 B. Its closest line is 3.6 px inside its frame at 320 px.
- One budget cannot reproduce every outline's start simplification. ionic-column needs 14,101 B at its start eps of
  1.95, while laurels at the eps before its own start eps (2.535) is 13,426 B.
- At 17,821, three outlines that no page uses are now drawn finer than at the start. Their inside rings, start → now:
  - ionic-column: eps 1.95 → 0, 72 → 73 rings;
  - owl: eps 2.535 → 0, 77 → 116 rings (the specks that simplification had dropped come back);
  - laurels: eps 2.535 → 0, 70 → 70 rings.
- If a page ever maps one of these three, the drawing will differ from the start's.
- No outline is drawn coarser than at the start.
- `REL_EPS` and the thinning path from step D stay in the code. No outline in the library reaches them now.

## Finding 4 · `nav_diff_check.py` now sees what a drawing draws

**The drawing digest**
- Every line drawing in every HTML file is keyed by its file, the panel that holds it, its kind (hero, patch, sep or
  relief) and its ordinal. This includes drawings inside the home and the area pages.
- Each drawing is reduced to a digest that ignores `--d`, `--o`, `<g>` grouping, how lines are merged into paths,
  simplification and coordinates:
  - for a contour drawing: per layout, each rise in order with its label and `data-rings`, and each planned ring;
  - for a relief: its inside rings and lines, and its halo rings and lines.

**What it reports**
- A changed digest is the class "drawing content". It fails unless `--expect FILE` names it.
- A drawing present on one side only is listed and fails, unless it is expected or sits on an area page.
- A changed viewBox counts as "drawing frame" and does not fail. Step D re-derived every frame.
- Changes to a rise's own closed rings (z) and spot rings count as "drawing refit" and do not fail.
  - They depend on the spread each drawing is fitted with, which step D refit to the swell (checker finding 12).
  - `--refit-out FILE` lists them.
- A new option, `--now-tree DIR`, compares a built working tree against `--build COMMIT`'s worktree.

**The run:** `nav_diff_check.py --build 797b1d4 --now-tree . --expect out/S-NAV1/drawings-expected.txt --refit-out /tmp/sg/refit.txt` built the start in a /tmp worktree and removed it afterwards.

| Edition | Drawings with the same levels | Exceptions (all expected) | Frames changed | Refit changes |
|---|---|---|---|---|
| academy | 2,382 | 52 | 123 | 1,557 |
| greece | 712 | 0 | 33 | 488 |
| marketing-ai | 301 | 6 | 23 | 181 |

- The expected exceptions are the home's tile patches, because step B made the tiles one per area, and the new area
  pages' drawings. `out/S-NAV1/drawings-expected.txt` lists 23 academy keys and 2 marketing-ai keys, with the reason.
- The result was NAV DIFF CHECK PASSED. All the earlier classes and the reading-page test pass as before: 566, 162
  and 76 pages are identical.
- Control: run on the checker's pre-fix trees (`/tmp/ck`), the new class fails on exactly findings 2 and 3:
  - the home hero, 20 → 17 levels and the like;
  - the four wall pages in academy and the three in greece, 164 → 84 inside rings;
  - the step B home tiles.
- On the refit count: separators make up most of it (2,144 of the refit lines across editions). A greece build with
  the separator byte cap lifted (SEP_MAX 10^7, in a /tmp copy) drew all 661 separators with the same own and spot
  rings as the capped build. So the byte budget does not cause them; the refit does.
  - Patches have no byte step.
  - Course heroes' byte step (`ct_fit`) only simplifies lines. That was not separately probed.

## Finding 5 · relief outlines that never moved

- `viz.rel_lines` `dist()` now uses `dl = max(deep, 1)`. A piece with no level inside its outline gets an outline
  d of 1/(1 − lo) > 0, and its halo keeps 1. The docstring says so.
- New check in `check_swell`: every lv-0 line of every outline in the library has d > 0 as the page writes it (two
  decimals).
  - Result: "every outline of the 81 in the library moves".
  - This covers trireme (m61, rm42, rm55), bough (rm125), and toga and amphora, which no page uses.

## Findings 8 and 9 (minor)

- **Finding 8:** a capture-phase click listener calls `saveY()` synchronously for every `a[href^="#"]`. The pager
  cards, which the browser follows itself, now save their entry's y even inside the 200 ms debounce.
- **Finding 9:** `go()` uses `replaceState` instead of `pushState` when the target is an id inside the panel already
  shown. In a one-track edition this is the area entry's `#track-<id>` on the home.
  - `check_nav` gained a test for an edition of one track: tapped on the home, the entry leaves the home at
    `#track-<id>` with `history.length` unchanged. It passed on greece at all 8 width and theme passes.
  - The existing test still passes: from a course page the entry leaves the page, pushes an entry, and back returns.

## Finding 6 · docs updated (no unit, brief, vault, BACKLOG, CHANGELOG or site-log)

- `design/README.md`:
  - a current-state paragraph after the 6.8 record, covering the two-level nav, the area pages, the swell, `.off`,
    the classless relief paths and `REL_MAX`;
  - the `--topo-turn`/`--topo-cycle` token row removed;
  - the `--topo-grow` row now `.1` with its meaning;
  - the 4 Components row names `topo-swell` and `.topo.off`;
  - the 3 Layout row names `nav.main-nav` and `nav.sub-nav`;
  - the `viz.py` paragraph describes the relief markup and budget.
- `kit/README.md`, prose only:
  - `build.py` row: the `HERO_BUDGET`/`HOME_TOPO_MAX` sentence and its numbers, the swell instead of "turning and
    growing", `swell_inside`, `swell_clear`;
  - `shell.css`/`shell.js` row: the two-level nav, history entries, the pause;
  - `verify.py` row: the home cap, the frame covered at every pose of the swell, the separators' swell, and one
    sentence on `check_history`, `check_nav`, `check_swell` and `check_pause`.
  - The build rewrote the size table itself.
- `catalog.toml` header: `course_order` now covers the area pages; `tracks` now describes area pages and the
  main/sub-nav; `extra` is shown on the area page; `planned_drawer` now applies to the track's sub-nav group.
- `docs/decoupling.md`: one note under P-DEC20 on the step D min-height (370 px, the formula without the overscan).
- `kit/viz.py`: the `contours` docstring no longer mentions "the frame's overscan for the turn"; the `relief` and
  `rel_lines` docstrings are updated.
- `kit/verify.py`: the module docstring covers the relief rule and budget, the outline check and `check_pause`. The
  `check_reliefs`, `check_nav` and `check_swell` docstrings are updated too.

**Left for the main chat (files this step may not touch):**
- `docs/BACKLOG.md:229` and `:1683` (P-HK1) still give a min-height formula with `sin(var(--topo-turn))`.
- `kit/p94_extract.py` and `kit/p95_shots.py` still parse or pose `topo-turn`, as step D noted.

## Finding 7 · not in this step

`verify.py --full` was not run, as instructed. The narrow checks ran on greece and marketing-ai as well as academy.

## Tests

- **Builds:** `baseline.py --check` built academy (157 s) and greece (39 s). `build.py --edition marketing-ai` passed.
- **`baseline.py --check`:** 159 files differ from the landed HEAD's manifest, none added and none removed:
  - academy 125, which is `index.html`, `README.md` and the 123 reading pages with a relief;
  - greece 34.
  - All 159 are listed in `out/S-NAV1/expected-G.txt`.
- **Narrow checks:** `/tmp/sg/scripts/narrow.py`, which is step D's `swell.py` plus REL_JS on a wall page,
  `check_pause` and `check_nav` at each width and theme, and `check_history`. It imports `verify.py` and never writes
  a record. It ran at 320, 390, 768 and 1280 px, dark and light, with and without motion.
  - academy (home, track-history, greece, new, m01, wall m63): SWELL CHECKS PASSED, no console error, every join at
    0.000 px at the five poses.
  - greece (home, greece, new, m01, wall m63): SWELL CHECKS PASSED.
  - marketing-ai (home, track-marketing, personal-brand-pb, new, read-pb1): SWELL CHECKS PASSED.
  - history: back and forward restore page and y at the top level, with pushState refused and in the iframe, on all
    three editions.
  - The home swell peaks at 9.1 px/s on a phone, inside the 2 to 12 px/s range.
- **`nav_diff_check.py`:** PASSED, as described under finding 4.
- **`index_check.py`:** "courses-index.md matches the sources".
- **`private_terms.py`:** 131 files, 0 private terms, OK.
- **`cmp design/theme.css kit/shell.css`:** identical.

## Files changed

- Code: `kit/shell.js`, `design/theme.css` = `kit/shell.css`, `kit/viz.py`, `kit/build.py`, `kit/verify.py`,
  `kit/nav_diff_check.py`.
- Docs: `design/README.md`, `kit/README.md`, `catalog.toml`, `docs/decoupling.md`.
- New in `out/S-NAV1/`: `step-G.md`, `expected-G.txt`, `drawings-expected.txt`.
- Rebuilt outputs: `kit/academy/` and `kit/README.md`'s size table. The `kit/editions/` builds are ignored by git.
- `out/S-NAV1/landing-report.md` was already modified before this step; it was not touched.

## Blockers

None.
