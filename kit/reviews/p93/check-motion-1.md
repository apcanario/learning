**Findings**

1. **Error.** On What's new, the 30 Oct rise is missing from the tall layout, and the tall layout is what shows below 1100 px (every phone and the tablet). The data gives 2026-10-30 with 14,178 words, 0 levels and 0 rings in "tall". In "wide" it has 1 level and 1 ring. The built markup confirms it: the tall `g.ct-rise[data-label="2026-10-30"]` has `data-rings="0"` and an empty `<path d=""/>`. At a contour every 14,000 words, 14,178 words is one level. This breaks the row's own choice ("its smallest, 30 Oct … one, so no listed day is flat") and "one rise per day it lists". The wide version is also weak: its one "ring" is `M585 120l0 2z`, a 2 px stub rather than a visible ring. Fix: the tall and wide layouts should get the same level count from the same interval, and a one-level day should draw an actual small closed ring in both. (data-summary.json "new * reduced/motion" → layouts.tall; hero-markup.html, What's new hero.)

2. **Minor.** The same unit sometimes gets a different level count in the two layouts. Rome U11 (31,767 words) has 4 levels in tall and 5 in wide. With Rome's interval of 34,974/5.5 ≈ 6,359 words, 31,767 is 4.996 levels, so the two layouts round it differently. Each layout should take its levels from one shared computation. (data-summary.json "rome * reduced", layouts.)

3. **Minor.** On the home at 390 px, the User Experience rise reaches past the frame or into the fade at poses 0.75 and 1, in both dark and light. At rest it is inside. The cause is P93's growth to 1.06. The home's rise places are given (P92), so I raise this only because check 4 says "every rise inside a 390 px phone's view". (data-summary.json "home 390px dark/light motion" → poses[3,4].hero_rises_outside.) The cases at 768 px (User Experience) and 1280 px (History, at rest) come from P92's layout and fall under the givens.

4. **Minor, outside this row.** verify-lines.txt line 8 reads "contrast (light, phone): 8652 texts … lowest 4.29:1 (rm01 span.bn)". That is a Rome reading page, not a topography. It is under 4.5 and is not among the FAIL lines the note accounts for. Someone should confirm that span.bn is large text or decorative, or else open a row for it.

5. **Minor, judgement.** At `--topo-a` .16, the blue rises on Information architecture in the dark theme barely read at desktop sheet scale. Planned rings and the IA5–IA7 rises are just discernible. Red (Greece, the home), the light theme and the What's new rises read clearly. They are faint by the given rule, so I note it rather than fail it.

6. **Not checkable.** "Each day's rise in the tone of the course that filed the most words that day": the sources give only each day's total, not words per course per day, so I could not verify the tones. The tones shown match `day_tones` (red, purple, purple, teal, purple, blue, purple, purple, blue).

**Confirmed**

- **The move.** The theme sets `--topo-turn` 3deg, `--topo-grow` 1.06 and `--topo-cycle` 120s, with ease-in-out, infinite alternate, origin 50% 50%. Only transform is animated. The phase is set per drawing through `--ph` and only under `prefers-reduced-motion:no-preference`.
  - The pose matrices agree. Pose 0 is `matrix(0.99863,-0.0523…)`, which is −3° at scale 1. Pose 1 is `matrix(1.05855,0.05548…)`, which is +3° at scale 1.06. The sheets label the poses −3.00°/1.000, −2.23°/1.008, 0°/1.030, +2.23°/1.052 and +3.00°/1.060, which is consistent with easing.
  - Every page with a topography has every drawing at its own point in the cycle. For example, Greece at 390 has 15 drawings at progress 0.003, 0.07, 0.136 … 0.936, evenly spread; the home has 14 drawings at 0.002 … 0.931.
  - With motion allowed, the only animations are `topo-l` (transform) and the home's P92 area line `harea-w` (opacity and transform).
  - Under reduced motion, the animation list is empty on every page at every width and theme (no "reduced" run lists one).
- **No edge or corner shows.** `cover_bad_at_rest` and `hero_cover_bad` are empty in every run and pose. Patch margins stay positive: the lowest is 1.1 px with motion (ux-ia and brand-b) and 8 to 11 px at rest. The patch ratio is 4 everywhere. The sheets show no visible layer edge.
- **Layers against their sources.**
  - Greece has 13 rises (U0–U12), Rome 14, Personal brand 11 (A1–A9, DD-A1, DD-A2), Building with AI 11 and Information architecture 15. All are in order, and each rise's words equal the source exactly.
  - Information architecture's 8 planned units (IA8–IA12, DD-IA1–3) have null levels and are drawn as dashed `circle r=15`.
  - Every written rise with two or more levels closes at least two rings of its own in both layouts (none with two or more levels closes fewer).
  - What's new has 9 days in date order with the source totals. Its largest day, 22 Oct (221,673 words), stands 15 levels, within 10 to 25.
  - One layout shows per width: tall below 1100 px, wide at 1280 px.
  - Every layer is aria-hidden="true" and holds no text. Sizes are 14,298 B (home), 8,277 (Greece), 9,810 (Rome), 10,881 (Personal brand), 9,978 (Building with AI), 8,247 (Information architecture) and 10,608 (What's new), all under 20 KB.
  - The Changelog, the Backlog and the Figure kinds page have no topography (`any_topography` 0).
  - Strokes are in the course roles: Greece red, Rome and course B purple, course A teal, Information architecture blue.
- **Rises inside the 390 px view.** No course home and not What's new has a rise outside the frame or into the fade at 390 px, at rest or at any pose. At 320 and 360 px some do (Greece and Rome U0/U4/U8/U12, Information architecture IA1/IA5, What's new 22 Oct and 3 Nov), which the row accepts.
- **Legibility at every pose.**
  - Course homes and What's new: the lowest text is 4.57:1, the "Start the course" label on the opaque blue button of Information architecture, dark. The lowest lede is 4.64:1 (Building with AI, light, 320 px, pose 0.5). The lowest eyebrow ("COMPLETE") is 4.84:1, and What's new's lede is at least 4.69:1. Every normal text is at least 4.5:1 and every large text at least 3:1.
  - Home: the area words, which count as large text, are at least 3.54:1 dark and 3.75:1 light. The lede is 5.87 dark and 5.50 light.
  - contrast.py reports all P92 and P93 token pairs passing at .16, including two stacked lines (muted text over them at 3.60 dark, 4.28 light).
- **Look.** The sweep is slow (120 s each way) and small (±3°, up to 6% growth). It reads as a calm drift with no lockstep between drawings. The fade at the hero's foot is soft, the stats boxes and buttons stay opaque over the lines, and the hero's text keeps its column.

**Renderer notes**

- The tall sheets were shown to me downscaled: the desktop sheets at about 0.65 to 0.84 and the phone sheet at about 0.5. At that size the faint dark-theme lines, especially blue, are close to the limit of what I can see, so finding 5 is a judgement made at reduced resolution.
- I could not watch the motion. My verdict on "slow and calm" rests on the parameters and on the five static poses.
- I viewed a sample of the images: the desktop home dark, Greece light and Information architecture dark sheets, part 1 of the phone Information architecture dark sheet, the desktop What's new dark hero and the phone What's new light hero. For every other page, width and pose I relied on data-summary.json and verify-lines.txt.

**FIX**

The error in finding 1 stands: on every phone and the tablet, What's new draws no rise for 30 Oct.