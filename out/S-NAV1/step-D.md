# S-NAV1 · Step D · motion: the swell, on every line illustration

Model: Opus 5.5 (claude-opus-5-5), a fresh agent. 22 Nov 2026.

## Verdict

Done. Pedro: "the core will stay the same... the outward lines are moving away from the core proportionally to their
distance to the core", on everything drawn by `kit/viz.py` (heroes of the home, area homes, course homes and What's
new; tile patches; section separators; object reliefs), "instead of the zoom out animation". `topo-turn`, the whole-layer
`topo-breathe`, `--topo-turn`, `--topo-cycle`, the layers' overscan (`--ox`, `--oy`) and `TOPO_TURN`/`TOPO_GROW` in
`kit/build.py` (and `REL_TURN`/`REL_GROW` in `viz.py`) are gone. Every line now swells about its own rise's core; the
innermost line never moves. Every check passed on academy, greece and marketing-ai. No commit, no push, no land.py;
`kit/baseline.json` and `kit/verify-hashes.json` untouched; no unit, brief, vault or course file changed.

## The design

**The swell.** One animation, `topo-swell`, on every line (`path`) of a drawing:
`scale(1)` to `scale(1 + --d × --topo-grow)` about `transform-origin: var(--o)` (`transform-box: view-box`, so `--o` is
in the drawing's own units), over `--topo-breath` (6 s) each way, ease-in-out, alternating, delayed by
`--ph × -2 × --topo-breath` (each drawing's own phase, inherited by its lines, so a drawing moves as one).
`--topo-grow` is now the outermost line's growth, `.1` (it was the whole layer's scale, 1.1): the outer lines reach 1.1,
as the breath did. Transform only. Under reduced motion nothing animates. Circles (a spot ring, a planned unit's dashed
ring) never move.

**`--d` in a contour drawing (heroes, patches, separators; `viz._ct_field`).** For rise k, let lo_k and hi_k be the
lowest and highest contour level of the lines it dominates. A line at level L dominated by k alone has
`d = (hi_k − L) / (hi_k − lo_k)` (0 when hi_k = lo_k: a rise of one level, whose only line is its innermost) and
`--o` = k's core, its peak `at` (rounded to the unit). Written to two decimals (`.43`, `1`); `--d` 0 is not written
(`.topo-l{--d:0}`).

**Shared lines.** A contour line whose stretches are dominated by more than one rise gets one origin and one d for the
whole line: weights w_k = the length of the line each rise dominates; `o = Σ w_k·core_k / Σ w_k`,
`d = Σ w_k·d_k(L) / Σ w_k`. Every stretch of the line carries the same `--d` and `--o` strings, so every stretch has
the identical transform at every pose and no join can open. Stretches of one tone are drawn as one run (the course
homes, patches and separators are one tone, so their shared lines have no joins at all); only stretches of different
tones (the home's areas, What's new's days) remain separate paths meeting at a join. A shared line is never closed
with `z`, so `z` still counts a rise's own rings (verify's ring counts and ct_fit's own-ring rule are unchanged).

**Markup.** Each rise `g.ct-rise` carries `style="--o:Xpx Ypx"` (its core) when one of its moving lines uses it; one
`path` per (d, origin): a level's own lines share both; a shared line's path carries `--d` and its own `--o`.

**Object reliefs (`viz.rel_lines`).** The contour level is the distance. A piece is an outline ring (lv 0) inside an even
number of other outline rings (odd: a hole). Its core is the centre of the box of its deepest level's rings. Every line
in the piece (its outline, its holes, its levels) scales about that core with `d = (deepest − lv) / (deepest − lowest
halo level)`: deepest 0 (fixed), the outline moving (deepest/(deepest+2)), the outer halo 1. A halo ring round several
pieces takes the area-weighted blend of their cores and d's; a halo ring round none (one in a hole) takes the piece it
lies in. Markup: `<g style="--o:...">` per origin, `path.rl-in`/`path.rl-out` with `--d`.

## Frame clearances recomputed

- `viz.swell_box(points, d, o)`: a line's box over every pose (at rest and at scale 1 + d·GROW about o; a scale moves
  each point along its ray, so the two ends bound every pose). `contours_rings` now returns each rise's own-ring box and
  every line's extent over the swell; `data-box` on a hero rise is that box.
- `build.py`: `turned_inside`/`turned_clear` (turn ±3° and grow 1.1 about the drawing's centre) become `swell_inside`/
  `swell_clear`, plain box tests on those boxes. `ct_fit` (course homes, area homes, What's new), `patch_block` (tile
  patches) and `sep_block` (separators) fit against them; their spreads change accordingly.
- `viz.rel_frame`: the relief's frame is the box of every line over the swell plus `REL_PAD` (14) on each side (+1 for
  the rounded origins); it was the drawing turned and grown about its centre (amphora: 771 × 1130, was about 826 × 1164).
- Hero layers: no overscan; `.topo-l` fills its frame (`left:0;top:0;width:100%;height:100%`).
- Hero min-height (theme 6, P-DEC20): with no overscan a 2:1 layout shows from `.5 − H/W`, a square one from
  `.5 − H/(2W)`; the wide view's top (.1) needs H = .4·980 = 392 px at 1280 and the tall view's (.25) H = .5·768 = 384 px
  at 768; less the 22 px above the hero: `min-height:370px` (was 380).
- verify.py budgets: unchanged (hero layer 20 KB, separators 6 KB + 135 B per rise over 38, reliefs 12 KB, check_topo's
  layer 20 KB).

## Budgets and the interval-from-budget rule (recorded)

- **Home hero.** The per-line `--d`/`--o` pushed the layer past `HERO_BUDGET` (19 KB) at the floor. `hero_interval`
  (P-HERO1) did its job: academy's interval rose from 24,500 to between 28,900 and 29,700 words a level (History 20 → 17
  levels, Marketing 7 → 5, Technology 8 → 7, UX 6 → 5, Sports 5 → 4); the layer is 19,392 B (was 19,444). The check is
  not loosened. Academy's build takes about 197 s (was 162): the scan draws one layer per hundred words above the floor.
- **Object reliefs.** The wall (24 bricks, ten levels each) could not fit 12 KB at any simplification (the attributes
  alone are about 10 KB). The repo's rule applied to reliefs: `REL_EPS` (6 units) is the most a relief is simplified
  before its inside levels are thinned instead (every k-th level kept, k = 2, 3, ...; outline and halo always drawn),
  as the hero's interval rises from its budget. Only the wall thins (11,472 B); every other outline fits at k = 1.
- Separators and patches fit their budgets by the existing simplification step (same-tone shared lines are one path).

## What changed

- `kit/viz.py`: `swell_scale`, `swell_box`, `_dfmt`; `_ct_field` keeps each whole line with its stretches, computes d,
  origin and the shared-line blend, merges same-tone stretches, boxes over the swell; `contours` writes `--o`/`--d`;
  `GROW` from the theme; `rel_lines`, `_in_poly`, `_poly_area`, `rel_frame(w, h, lines)`, `relief` with `_relief_at`
  and `REL_EPS`; `REL_TURN`, `REL_GROW` gone; comments and docstrings.
- `kit/build.py`: `TOPO_TURN`, `TOPO_GROW` gone; `swell_inside`, `swell_clear`; callers and docstrings.
- `design/theme.css` = `kit/shell.css` (cmp clean): version 6.18; tokens (`--topo-turn`, `--topo-cycle` gone,
  `--topo-grow:.1`); `.topo-l` without overscan; `.topo path{transform-box:view-box;transform-origin:var(--o,0 0)}`;
  `topo-swell` keyframes and rule; `topo-turn`, `topo-breathe` gone; patch and relief rules without `--ox/--oy`;
  course hero `min-height:370px`; 4i, separator and relief comments.
- `kit/shell.js`: unchanged (the motion is CSS alone).
- `kit/verify.py`: `GROW`, `BTIME`, `SWELL` from the theme (TURN, CYCLE gone); `SWELL_AT_JS` and `POSE_JS`/`pose()` pose
  the swell (0 at rest, 1 at the top, its phase honoured); the home's motion check (the area words and one swell on each
  line of the shown layout and every patch, `SWELL_LINES_JS`); `check_topo` (one swell per line, nothing else); `SEP_JS`
  and `REL_JS` (a swell on each line, transform only, poses; REL_JS accepts `g` per origin and `style` with `--d`); the
  phone speed check measures the furthest-moving point in the home's frame (`SWELL_AMP_JS`); motion-sheet tags; the new
  `check_swell` (`LINES_JS`, `SWELL_JS`, `swell_pages`, `SWELL_WIDTHS`) run from `main()` after `check_reliefs`;
  docstring.
- `kit/verify_scope.py`: docstring paragraph only.

`check_swell` (with motion, per page, 320/390/768/1280, dark and light): only transform and opacity animate on the
page, only the area words and the contour lines; every line of every shown drawing swells, one phase per drawing;
every `--d` in 0..1, a relief's outer halo 1, a contour drawing's outermost line moving, an innermost line 0; a rise's
own lines move about its core (`data-at`); at the five poses (0, .25, .5, .75, 1) every join (an end of an open stretch
on the end of another path's stretch in the same drawing) opens at most 0.5 px, every patch's, separator's and relief's
lines stay in their frame, every fitted hero's own rings stay in its frame above the fade (from 390 px; not the home,
whose hero is not fitted, as check_topo); at the top every innermost line is unmoved and every other at exactly
1 + d × grow. Under reduced motion: no CSS animation at all on the page.

## Tests

- `baseline.py --check` clean before any change. After: 328 files differ, 0 added, 0 removed (academy 246 incl.
  README.md, greece 81); all in `expected-D.txt`. No upstream-added line removed: no `drop:` entries.
- Diff sort (`/tmp/snav1d/scripts/sortdiff.py`, against builds taken before the change, academy, greece and
  marketing-ai): 356 files changed; with `svg.topo-l` content, a relief's `--ar` and the inlined `<style>` stripped,
  every one is byte-identical (353 SVG line attributes only, 3 shells also theme CSS). No other difference.
- Narrow checks (`/tmp/snav1d/scripts/swell.py`, importing verify.py, never recording): `check_swell`, then
  `check_topo` reduced and with motion at the five poses, `check_home` with motion (incl. hero contrast at every pose),
  `texts_contrast` at every pose, `SEP_JS` and `REL_JS`, at 320, 390, 768, 1280 px, dark and light:
  - academy (home, track-history, greece, new, m01): SWELL CHECKS PASSED, no console error.
  - greece (home, greece, new, m01; one track, so no area page): SWELL CHECKS PASSED.
  - marketing-ai (home, track-marketing, personal-brand-pb, new, read-pb1): SWELL CHECKS PASSED (after the outermost-d
    rule below).
- Join check, widest gap at each pose (0, .25, .5, .75, 1), every page, edition, width and theme: **0.000 px**. Joins
  found: academy home 13, What's new 18; marketing-ai home 2; every other drawing 0 (one tone: shared lines are one path).
- Clearances (closest line inside its frame over all poses): academy home 2.4 px (patches), track-history 5.0,
  greece 2.0, new 38.8, m01 2.2 (separators 2.2 px at 320, relief 3.5 px); greece edition similar; marketing-ai
  read-pb1 1.4 px.
- Swell speed, home at 390 px: peaks at 9.0 px/s (33.6 px each way), inside 2 to 12.
- `check_reliefs` whole (123 mapped pages, 4 widths, dark/light, with and without motion): passed.
- Shots: `/tmp/snav1d/shots/` (home, Greece, m01 at pose 0 and 1, 390 and 1280): the core rings still, outer lines out.
- `index_check.py`: OK. `private_terms.py`: OK. `verify.py --full` not run (as instructed).

## Open choices (taken, recorded)

1. **Normalisation per rise**, by the levels of the lines it dominates (not the global top): every rise's innermost is 0.
2. **Blend weights** are the length each rise dominates on the shared line.
3. **One-level rises** keep d 0 (innermost rule wins), so a line shared with one blends below 1. check_swell therefore
   asks a contour drawing's outermost line only to move, and the relief's halo to be exactly 1.
4. **Same-tone stretches merged** into one path held by the rise dominating most of it, drawn unclosed; rises still
   count only their own rings (`z`). This also keeps the separators in budget.
5. **Circles do not move**: spot rings (at the core) and planned rings (no height).
6. **Reliefs**: degenerate piece with no inner level would hold its outline still (none in the library); the wall
   thins its levels (k > 1) by the budget rule.
7. **Home hero ring clearance** is not checked (it never was; its rises are placed, not fitted). Below 390 px, as
   before, a hero's rings are reported, not failed.
8. **Hero min-height 370 px**: the old formula without the overscan; a course home hero between 370 and 380 px
   (Building with AI) is 4 px shorter.

## For the row's close (outside this step's files)

- `design/README.md` (version history, section 4i row, token table `--topo-turn`/`--topo-cycle`, `turned_inside`).
- `kit/README.md` build row text: "turning and growing", `turned_inside`, `turned_clear`, "24,500 for academy,
  19,388 B" (now about 29,000+; 19,392 B).
- `kit/p94_extract.py` and `kit/p95_shots.py` (old row tools) still parse `--topo-turn` / pose `topo-turn`; p94_extract
  fails at import now. Not in this step's files.
- Performance note: the motion is now hundreds of SVG path transforms (home 82 lines, a course home up to 325), which
  Chromium paints on the main thread, where the old layer transform was composited. The phone LCP / long-task print in
  the full verify will show it; nothing measured here failed.

## Blockers

None. No permission check refused a script.
