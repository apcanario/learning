# S-NAV1 · fresh check of the whole diff

Model: Opus 5.5 (claude-opus-5-5), a fresh agent that had not seen the work. 22 Nov 2026.
Scope: `git diff 797b1d479..HEAD` (b274204), checked against the row's text (`out/S-NAV1/S-NAV1.md`), items A to F.
Read only in the repo: nothing edited but this file. Both trees were exported with `git archive` to `/tmp/ck/start` and
`/tmp/ck/now` and every edition built there (`python3 build.py --edition E` in each tree's kit/). The HEAD rebuild is
byte-identical to the committed `kit/academy/` (`diff -rq`: no output).
`kit/nav_diff_check.py /tmp/ck/start /tmp/ck/now` (all three editions): NAV DIFF CHECK PASSED, the same counts as step-E.md.

## Verdict

**PASS WITH FIXES.** 1 blocking, 6 should-fix, 8 minor.

The spec items A, B and C are met. D is partly met: the motion is right in the code, but two visible losses were not
authorised, a few relief outlines stay still, and the course homes now drop frames on a throttled phone. E is partly
met: the diff sort cannot see geometry changes inside a line drawing, and no edition verify is recorded after step D.

## Item by item

### A · history: MET

- `kit/shell.js` go() (lines 262-268): when the hash changes it calls `saveY()`, then
  `history.pushState({y:0},'','#'+id)`. If pushState throws it falls back to replaceState, and if that throws too it
  leaves the address alone.
- Routing (lines 306-313): `popstate` calls `routeTo(e.state)`. `hashchange` routes only a hash that popstate has not
  already routed (the `routed` guard).
- Scroll: the scroll listener saves `{y}` into the current entry with a 200 ms debounce, `history.scrollRestoration`
  is `manual`, and `routeTo` puts `y` back once `route()`'s promise has settled. `show()` returns `load()`.
- First load: `routeTo(history.state)` only. It pushes nothing.
- Test (`kit/verify.py` 2757-2890, `check_history`, run from `main()` at 3025) at 390 px:
  - It checks that a fresh load holds as many entries as a plain page.
  - It walks home → area → course → unit by tapping the links, each page scrolled to 40% first.
  - It then calls `history.back()` once per level and checks the panel and its y (±2 px), and `forward()` to the end.
  - It also covers pushState refused (the replaceState fallback, no entry added) and a same-origin sandboxed iframe.

### B · area homes: MET

- `kit/build.py` 1190-1233 builds one `section.panel.home.area#track-<id>` per THEMES entry (`data-kind="area"`). Each
  has:
  - a hero with the lede and three stats;
  - crumbs Home › Area;
  - a band with the track's course tiles, `extra` (its own copy) and its planned courses (`track_body`).
- The home keeps its hero and gets `div.cgrid.areas`, one tile per track. Each tile carries the chip, name, lede,
  pill, courses, units written, units in all, and the patch.
- Crumbs: `crumbs()` (build.py 259-275) adds the area before any course page. The built pages read like this:
  - greece/r-2.3: Academy › History › Greece › Unit 2 › 2.3
  - brand-a/read-a1: Academy › Marketing › Course A › A1
- One track: `MULTI` is false for greece, so there is no area page and crumbs drop `track-*`.

### C · navigation: MET

- `nav.main-nav` holds Home and the tracks in catalog order. `nav.sub-nav` holds one `.sub-sec[data-navctx]` per area
  and per course. `show()` reveals only the reader's section and hides the whole sub-nav on the home and its site pages
  (`secOf`, shell.js 25 and 168-170).
- Each is built once, inside `#drawer .dlist`.
- What's new, Changelog, Backlog and Figure kinds sit at the home's foot (built index.html: `#backlog` at 35474,
  `#viz-examples` 35600, `#changelog` 35751, `#new` 37977, all after `.cgrid.areas` at 20740). None of them is in either
  nav.
- The checks are `check_nav` (verify.py 2923) at 390 dark, 390 light and 1280.

### D · motion: PARTLY

What is met:
- `topo-turn`, `topo-breathe`, `--topo-turn`, `--topo-cycle`, the overscan (`--ox`/`--oy`), `TOPO_TURN`/`TOPO_GROW` and
  `REL_TURN`/`REL_GROW` are all gone from the code. What remains are comments that record their removal.
- One animation, `topo-swell`. It runs on `.topo-l path` and only under `prefers-reduced-motion:no-preference`.
  Keyframes: transform only, `scale(1)` → `scale(1 + var(--d) * var(--topo-grow))`, with
  `transform-box:view-box; transform-origin:var(--o)`.
- `--d` per contour line (viz.py `_ct_field`) runs from 0 at each rise's highest level to 1 at its lowest.
- A shared line takes one origin and one d for the whole line (the length-weighted blend). Every stretch of it carries
  identical `--d`/`--o` strings, so no join can open. Same-tone stretches are merged into one path. verify's
  `check_swell` measured 0.000 px at five poses.
- Frame clearances:
  - patches, separators and course heroes use `swell_box`, `swell_inside` and `swell_clear`;
  - the relief frame uses `rel_frame(w, h, lines)`;
  - the course hero min-height went from 380 to 370 px, with the derivation in theme.css.
- Reliefs: the depth parity of the outline rings separates pieces from holes, and each piece has its own core. The
  deepest level has d 0 on every outline in the library and the outer halo has d 1. The library check was
  `viz.rel_lines` over every outline in `design/outlines/`.
- at-sign shows 2 pieces with 1 distinct core. Its two pieces are concentric, so their cores coincide in the geometry.
  That is not a shared-core bug.

What is not met is in findings 1 to 3 and 5.

### E · rules: PARTLY

- No path under `courses/` is in the diff, so no unit, brief or vault file changed.
- `diff design/theme.css kit/shell.css` is identical. No page got its own CSS: every built difference is classified
  and there are no other `<style>` differences.
- The reading pages are byte-identical once nav and SVG are stripped: 566 in academy, 162 in greece, 76 in
  marketing-ai (re-run on the /tmp trees).
- `kit/verify.py` has the new routes and area pages (`check_area`, `check_nav`), the history test and the swell poses
  (`check_swell`, `SWELL_AT_JS`, the POSE_JS rewrite).
- Gaps are findings 4 and 7.

### F · other: see the findings below

## Findings, ranked

### Blocking

**1. The course homes now drop frames on a mid-range phone: hundreds of SVG path transforms run on the main thread.**
- Before, one composited layer per drawing moved. Now every path animates: a course home has 350 to 370 line paths
  (greece/home 353, rome/home 357, ux-ia/home 372) and the shell holds 451.
- Chromium does not composite SVG child transforms, so style, layout and paint run on the main thread on every frame.
- Measured at 390 px, mobile, 4× CPU throttle, motion allowed, 5 s of requestAnimationFrame (`/tmp/ckscripts/perf.py`):

  | Page | Build | Frames | p50 frame | Long tasks |
  |---|---|---|---|---|
  | greece (course home) | start | 269 to 273 | 16.7 ms | 0 ms |
  | greece (course home) | HEAD | 102 to 128 | 33 to 50 ms | 0.9 to 2.3 s |
  | rome (course home) | start | 268 | 16.7 ms | 50 ms |
  | rome (course home) | HEAD | 99 to 115 | 50 ms | 1.5 to 3.0 s |
  | home, track-history, m11 | both | about the same | | |

- Long tasks of this size delay taps on the course homes.

**Fix:** pause the drawings that are off screen.
- In `kit/shell.js`, one IntersectionObserver on every `.topo` toggles a class `off`.
- In `design/theme.css` (copied to `kit/shell.css`), add `.topo.off path{animation-play-state:paused}`.
- Measured with exactly this injected (`/tmp/ckscripts/perf2.py`): greece 272 frames, p50 16.7 ms, long tasks 50 ms;
  rome 265, 16.7 ms, 52 ms. That is back to the start build.
- Not animating the d-0 paths made no measurable difference.
- Add a verify check: the longest task on a course home with motion under a 4× throttle stays under a budget.

### Should-fix

**2. The home hero lost contour levels, which the spec did not authorise.**
- The `--d`/`--o` bytes pushed the layer over `HERO_BUDGET` (19 KB, build.py 1070), so `hero_interval` raised the
  interval from 24,500 to about 29,000 words a level.
- Rings per area (`data-rings`, start → HEAD): History 20 → 17, Marketing 7 → 5, Technology 8 → 7, UX 6 → 5, Sports 5 → 4.
- Total line length: tall layout 26,546 → 21,897 units, wide 25,785 → 21,404 (−18%).
- Step D recorded it but did not raise it as a change needing Pedro's word.

**Fix:** keep the interval at the floor. Either raise `HERO_BUDGET`, and verify's 20 KB hero cap with it, by the
attribute cost (about 3 to 4 KB), or cut the bytes:
- emit `--o` only on the `g.ct-rise`;
- drop `px` from `--o` and add the unit in CSS;
- write `--d` on a `<g>` per level instead of on each path.

If neither is acceptable, write it as a proposal with a ⚠ for Pedro to veto.

**3. The wall relief was thinned to fit `REL_MAX`, which the spec did not authorise.**
- Pages: greece r-6.3, r-10.10, r-12.6 and rome r-3.3.
- Inner rings 164 → 84 (`rl-in` subpaths); line length 103,510 → 69,431 units (−33%).
- This is the new `REL_EPS` thinning path in viz.py `relief()`/`_relief_at`.

**Fix:** raise `REL_MAX` for reliefs to what the wall needs at k = 1 (about 16 KB, with verify's relief budget), or
cut the attribute bytes as in finding 2. Otherwise raise it as a ⚠ proposal.

**4. `kit/nav_diff_check.py` is too generous inside line drawings.**
- The class "SVG lines" takes the whole element: any change of path `d`, ring count, viewBox or spot passes, with only
  its text guarded.
- That is why it passed findings 2 and 3, and every refit in finding 12. The spec's class was "SVG line attributes".
- The rest of its stripping is honest:
  - the reading-page test removes every `<svg>` and `<nav>`, but a changed data figure or in-page nav would still
    fail the sort, since it sits outside every region;
  - "the home" and "area pages" are whole panels, as the spec allows.

**Fix:** inside an SVG-lines region, also compare a geometry digest that ignores `--d`, `--o`, `<g>` grouping and the
merging of runs:
- per rise, `data-rings` and its count of closed rings;
- per drawing, the viewBox and the number of `rl-in`/`rl-out` rings.

Print any change as its own class, "drawing content", which fails unless it is listed as expected.

**5. Some relief outlines do not move.**
- A piece with no level inside its outline (deepest level = 0) gets d 0 on its outline, because `rel_lines` `dist()`
  returns `(0 − lv)/(0 − lo)`, which is 0 at lv 0.
- Affected outlines:
  - trireme: 4 pieces, 43 to 48 units wide and 49 to 191 tall; on 3 academy pages;
  - amphora: both handles, 139 × 268 units; unused at present;
  - toga: 1 piece, 36 × 36;
  - bough: 1 speck.
- Spec: "the outline moves". step-D.md open choice 6 says "none in the library", which is wrong.

**Fix:** in `dist()`, use `dl = max(deep[id(r)], 1)`, so such a piece's outline gets d = 1/(1 − lo) > 0. Add to
`check_swell`: every relief outline path has d > 0.

**6. Docs the row made false.** These belong to the §8 close.
- `design/README.md:62-63`: the token rows for `--topo-turn`/`--topo-cycle`, and `--topo-grow` as `1.1`.
- `kit/README.md:70`, the build row: "turning and growing", `turned_inside`, `turned_clear`, "24,500 for academy,
  19,388 B".
- `docs/BACKLOG.md:229` and `:1683` (P-HK1): a min-height formula with `sin(var(--topo-turn))`.
- `kit/viz.py:3440`: the docstring still speaks of "the frame's overscan for the turn".
- The version-history entries in theme.css (6.6 to 6.8) are history and can stay.

**7. No edition verify is recorded after step D.**
- `out/S-NAV1/` records `--edition marketing-ai` passing after step B and step C. There is no record of
  `verify.py --edition greece` or `--edition marketing-ai` after D, which changed both editions.
- The landing reports show academy full runs only.

**Fix:** run both after the fixes above and record their first and last lines in the close.

### Minor

**8. The scroll save can miss a fast tap on a pager link.**
- The 200 ms debounce means a tap within 200 ms of the last scroll event (momentum scrolling) leaves the entry with a
  stale y.
- This affects the pager cards, `a.prev`/`a.next` (shell.js 198-199). They have no `data-target`, so they navigate
  natively and never call go().

**Fix:** call `saveY()` synchronously in a capture-phase click listener for every `a[href^="#"]`, or give the pager
links `data-target`.

**9. In a one-track edition, the main nav's area entry adds a history entry without leaving the home.**
- In greece, the History entry goes to `#track-history`, the band on the home. Tapping it pushes an entry while the
  reader stays on the home.
- The entry is never marked active there; Home is.
- Acceptable, but worth noting for S-NAV2.

**10. The real artifact frame is untested.**
- Test 3 uses a same-origin sandbox. The claude.ai artifact frame is cross-origin, so pushState may throw there (the
  fallback covers that) or may add entries to claude.ai's tab history (Back then walks the frame first).
- The publish step must report which happens, as the spec asks.

**11. WebKit is untested.**
- `var()` inside `@keyframes`, and `transform-box:view-box` with a px `transform-origin` on SVG paths, have a history
  of Safari bugs.
- Playwright here has Chromium only (`/opt/pw-browsers`).

**Fix:** check on an iPhone at publish, or add webkit to verify.

**12. The refit made visible changes that were recorded only in passing.**
- Tile patches are drawn larger: line length +9% to +95%, median +53%, across 104 patches.
- Separators: median +25%; the spot rings changed on 689 of 2,124.
- Relief viewBoxes are about 5% tighter, so the objects show larger.
- The course hero min-height went from 380 to 370 px, and the home hero is 66svh at 400 px and below (step B).

All of these follow from the new clearances. Tell Pedro in the site-log entry.

**13. Lines of d 0 carry no `--d` of their own.**
- They inherit `.topo-l{--d:0}`, so the computed value is right.
- They still run a `scale(1)` animation. No cost was measured.

**14. A rise whose innermost line is shared moves that line.**
- This happens to one-level rises merged into a neighbour: the blend gives the line d > 0.
- It contradicts "innermost does not move" only in the shared case. step D recorded it (choice 3).

**15. Safari may throttle the scroll save.**
- `saveY()` calls replaceState at every scroll stop. Safari throttles more than 100 calls in 30 s.
- The call is wrapped in try, so it is benign.

## Evidence files (in /tmp, outside the repo)

- `/tmp/ck/start`, `/tmp/ck/now`: the exported trees and their builds.
- `/tmp/ck/ndc.txt`: the nav_diff_check output.
- `/tmp/ckscripts/svgcmp.py`, `svglen.py`: the drawing content and line length comparisons.
- `/tmp/ckscripts/perf.py`, `perf2.py`: the frame timing and the fix trial.
