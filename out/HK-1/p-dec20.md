# P-DEC20 · a minimum course-home hero height, so a course of six to ten units passes the motion check

Agent: claude-opus-5-5 (fresh agent, P-DEC20 only), 21 Nov 2026. Clone `/home/claude/learning`, on top of P-HERO1's
uncommitted `kit/build.py` (left as it was). Nothing committed, pushed, landed or published; `kit/land.py` not run.

## Change
- `design/theme.css` (copied to `kit/shell.css`, byte-equal): in the tablet block `@media (min-width:768px)`,
  `.panel.home>.hero.has-topo{min-height:380px}` with the derivation in a comment; header line "Version 6.16, 21 Nov 2026
  (P-DEC20)". Course homes only (`.panel.home`: every history and markdown course home); What's new (`.panel.log`) and
  the root home (`.hhome`) untouched. No page gets its own CSS; `kit/build.py` and `kit/verify.py` untouched by this row.
- Records: `README.md` Known limits (the six-to-ten clause replaced), `docs/decoupling.md` §6 "Notes on P-DEC20".
  BACKLOG, CHANGELOGs and `claude/` mirrors left to the main chat's §8 close.
- Evidence kept in `out/HK-1/`: `p_dec20_geo.py` (the geometry), `p_dec20_probe.py` (probe setup, refuses the main tree),
  `p_dec20_measure.py` (hero heights by Playwright), `p_dec20_runs.txt` (the verify results). No dummy unit, edition or
  build output is in the repo; the probes are `/tmp/probe-dec20`, `/tmp/probe-dec20-sce`, `/tmp/probe-dec20-before`.

## How the value was chosen (computed, not guessed)
The layer's frame is the hero plus the 22 px above it (`.topo{top:-22px}`), full width beside the sidebar: 980 px at a
1280 px window, 768 at 768. The layer's svg is the frame plus the overscan (`--ox = 100cqh·sin(turn)/2 + 1px`, `--oy`
likewise from the width), `preserveAspectRatio slice`, and the frame fades over its last 10%. `ct_fit` places every
ring inside its layout's view: wide `(.04, .1, .96, .84)`, tall `(.25, .25, .75, .7)`.

Working it through, a frame W x H shows a 2:1 (wide) layout from `y = .5 − H/(W + 2·ox)` to `.5 + .8H/(W + 2·ox)`, and
a square (tall) one from `.5 − H/(2(W + 2·ox))` to `.5 + .4H/(W + 2·ox)`. So:
- desktop, wide: the view's top (.1) is shown when `H ≥ .4(W + 2)/(1 − .4·sin 3°)` = **401.2 px at W 980**;
- tablet, tall: the whole view (.25 to .7) when `H ≥ .5(W + 2)/(1 − .5·sin 3°)` = **395.4 px at W 768**.

`p_dec20_geo.py` (P-DEC11's `p_dec11_geo.py` with that exact band in place of its `.5 ± H/1000` approximation; n equal
rises of 1,200 words placed by build.py's own `ct_fit`, n = 1 to 24):

| Frame | Layout | Rises outside |
|---|---|---|
| 980 x 347 | wide | 6 to 24 |
| 980 x 390 | wide | 6 to 10, 17 to 24 |
| 980 x 398 | wide | 6, 17 to 24 |
| 980 x 400 | wide | 17, 18, 22 to 24 |
| 980 x 402 to 430 | wide | none |
| 768 x 347 | tall | 1, 5 to 24 |
| 768 x 395, 402 | tall | none |

The wide view's foot (.84) lies in the fade below a 427 px frame, but no ring of 1 to 24 rises reaches it (the box ends
at .66), so the top is the binding edge. A frame of 402 (hero 380) clears both bounds; 380 is the smallest whole pixel.

Note: 17 to 24 rises also fail at 398 to 400 px. Academy's 20-unit courses are not hit today (their heroes are 427 to
478 px), but SCE, once its lede or brand gave a hero under 400, would have; the minimum covers it too.

## Effect on today's course homes (measured, `p_dec20_measure.py`, Chromium, 1280 x 800 and 768 x 1024)
Hero heights are the same at 768 and 1280 (the column is 760 px from 768 up):

| Course home | Hero before | After |
|---|---|---|
| brand-b (Brand + AI B) | 376.2 | **380 (+3.8 px)** |
| brand-a | 394.7 | unchanged |
| greece, rome, ux-ia | 427.2 | unchanged |
| building-with-ai-bw | 452.7 | unchanged |
| personal-brand-pb, supply-chain-execution-sce | 471.2 | unchanged |
| sport-psychology-sp | 478.2 | unchanged |

At 767 px and below nothing changes (brand-b 376.2, `min-height:auto`). The extra 3.8 px sit at the foot of brand-b's
hero, under its buttons; the layer itself (bytes) is unchanged. Zero change for brand-b was not possible: its 398 px
frame is under the 401.2 bound (it passes today only because it has 11 rises).

## Scope widened to the tablet (stated)
The row names the desktop check. The fieldnotes probe showed the tablet failing the same way (start CSS, six units: 10
tablet motion failures besides the desktop's; P-DEC11's two-unit test passed there). The same 380 px clears the
tablet's bound (395.4), so the rule sits in the 768 px block, not the 1100 px one. The alternative, desktop only, would
leave a six-to-ten-unit course failing verify at 768 px.

## Proof 1 · the template edition `fieldnotes`
Editions are `editions/<name>.toml` (courses, omit, site, brand); `courses/_template/` is the pack the `new-course`
skill copies. The template test (course home-composting, edition and brand `fieldnotes`) is recreated in a repo copy by
`out/DEC-C/p_dec11_template.py`; `p_dec20_probe.py fieldnotes <copy> <n>` adds HC3..HCn (about 1,250 words each, each on
its own day: on one day the dummies made What's new's tall layout unfittable, a probe artefact). Then
`build.py --edition fieldnotes` and `verify.py --edition fieldnotes --full`.

- Start CSS (`/tmp/probe-dec20-before`), n = 6, 8, 10: 12 / 10 / 12 desktop and 10 / 10 / 12 tablet motion failures
  ("the rises ['HC2', 'HC3'] have rings outside the frame or in its fade"). Hero 325 px, frame 347.
- P-DEC20 CSS (`/tmp/probe-dec20`), n = 6, 7, 8, 9, 10: 0 desktop, 0 tablet motion failures; hero 380, frame 402. The
  only FAIL in each run is the probe's own `docs/courses-index.md` line ("should say 'n of n written'"), not touched by
  the setup script.

## Proof 2 · SCE
SCE has SCE1 written (9,760 words; the instruction's "0 written" is out of date). `p_dec20_probe.py sce <copy> <n>`
writes SCE2..SCEn as copies of SCE1's text under their own code and title, and `editions/sce-probe.toml` (SCE alone,
academy brand, marketing-ai's rules) so a full verify takes minutes, not 29. n = 6 to 10, P-DEC20 CSS: the course home
(20 rises, n written) shows 0 motion failures and no "rings outside" at any width; 20 pose checks at desktop and tablet
ran each time. The other FAILs (93 to 111) are all probe artefacts: the academy brand's private term in a one-course
edition, the omitted build pages and planned tiles, the dummies' missing courses-index rows, the home's Supply Chain
track rise at phone widths (the dummies' 98,000 words), and a font the edition does not use. SCE's hero is 471 px, so
the minimum does not touch it; it passes with or without this row.

## Rebuild and differences from /tmp/start/academy
`cd kit && python3 build.py` (2 m 29 s), then `python3 kit/build.py --edition greece`; `python3 kit/baseline.py --check`:
academy 459 files, 2 differ; greece 82 files, 1 differs.
- `kit/academy/index.html`: `diff -rq` against /tmp/start/academy lists this file alone. Proved by script: with the two
  CSS additions (the 6.16 header line and the P-DEC20 rule) removed, it equals the start file outside the home's hero
  `div.topo`, which is P-HERO1's (19,825 to 19,428 B, as `p-hero1.md`). The shell CSS is inline in `index.html`; no
  course home's own markup or fetched file changes.
- `kit/README.md`: P-HERO1's `build.py` row, plus the regenerated size table's Shell row, 551 KB to 552 KB (this row's
  CSS adds 1,153 B, P-HERO1's layer takes 397).
- `kit/editions/greece/index.html` (not tracked in git): with the two CSS additions removed its sha256 is db170f09d852b84a…,
  the baseline manifest's own; so the CSS only.

## Not done / left
- `verify.py --full` on academy, greece and marketing-ai not run on the changed tree (the HK-1 test step runs them). Only
  brand-b's home changes visibly.
- Wider windows (⚠, recorded in decoupling §6): the frame's width follows the window but the hero's height is set by its
  text, so a window wider than 1280 px shows less of the wide layout's height (1920 px: W 1620, band from about .23 for
  a 449 px frame) and a tablet wider than 768 px less of the tall one's. That holds for today's homes too; verify checks
  768 and 1280 only. A min-height in container units (`calc(.4 * (100cqw + 2px) / (1 - .4 * sin(var(--topo-turn))) - 22px)`)
  would hold at every width, but it would raise every course home on a wide window. Proposal, not done.

Model: Opus 5.5 (claude-opus-5-5).
