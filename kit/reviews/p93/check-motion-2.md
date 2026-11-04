**Verdict: PASS.** No error or should-fix stands. There are five minor findings, and nothing here asks for `--topo-a` to be lowered.

## Findings

1. **minor: the dark theme's blue topography barely reads** (`motion-sheets/desktop-ux-ia-motion-dark.png`, `phone-ux-ia-motion-dark-part1.png`).
   - On the Information architecture home in the dark theme, the lines are just at the edge of seeing at every pose. On a phone they show mainly as the dashed planned rings near the foot of the lede.
   - Red (Greece) and purple (Rome) dark heroes read faintly but clearly (`desktop-greece-motion-dark.png`, `heroes/tablet-rome-dark.png`). In the light theme the lines read well (`desktop-ux-ia-motion-light.png`, `heroes/phone-brand-b-light.png`).
   - Faintness is the given. My judgement is that the layer still reads, but only just for blue on dark. It cannot be raised without reopening the .16 rule.

2. **minor: the home's rises leave the frame at widths the row did not set** (`data-summary.json`).
   - At 768 px, "User Experience" is outside the frame or fade even at rest (`home 768px dark/light reduced`, `rises_outside_at_rest`).
   - At 1280 px, "History" is outside at rest, and "Marketing" joins it at poses 0.75 and 1 (`home 1280px dark motion`, line 75849).
   - These are P92's `HERO_AT` places, which this row keeps, and the row's 390 px rule is met. I report it for the record only.

3. **minor: two tile patches have a written rise with fewer than two rings of its own** (`data-extract.json`).
   - Greece U11 in its patch: 3 levels, 1 own ring (for example lines 1831–1835 and 9200–9204).
   - The "IA6 §7" rise in its patch: 2 levels, 1 own ring (lines 8172–8176).
   - The "min(2, levels)" rule is stated for the course-home topographies, and every hero rise meets it. If it was meant for patches too, these two miss it.

4. **minor: contrast is safe only because lines never stack, and that is checked at five poses** (`contrast.txt`).
   - If two lines sat on one pixel (opacity .294), the muted lede, crumbs and button labels would fall to 3.60:1 in the dark theme and 4.28:1 in the light theme. Both are under 4.5:1.
   - Nothing measured on the page comes near that: the lowest normal-size text is 4.57:1. The safety rests on the contours never overlapping, and the check covers only the five sampled poses.

5. **minor: the patches' clearance from their frame is tight at some poses** (`data-summary.json`).
   - The smallest margin with motion is 1.1 px (brand-b at 320 px, pose 1, line 8587), and several are 1.2–1.4 px.
   - No margin is zero or negative, so it passes.

## Confirmed

**The move** (`theme-excerpt.css`, `data-summary.json` → `sources.motion`, the pose transforms)
- Animation `topo-turn`: ±3°, scale 1 to 1.06, 120 s each way, ease-in-out, infinite alternate, transform-origin 50% 50%. It is applied only under `prefers-reduced-motion: no-preference`.
- The measured matrices match:
  - pose 0: −3°, scale 1.000
  - pose 0.25: about −2.22°, scale 1.008
  - pose 0.5: 0°, scale 1.030 (exactly)
  - pose 0.75: +2.23°, scale 1.052
  - pose 1: +3°, scale 1.0586
- Only transform and opacity animate anywhere. All 1,080 animation entries are `topo-l` (transform) or the home's P92 area-line word `harea-w` (opacity and transform).
- Reduced motion: no animations in all 120 reduced runs, every page and width.
- Each drawing runs at its own point of the cycle, for example progress 0.002, 0.359, 0.716, 0.071 and onward on the home, and 0.002, 0.469, 0.935 and onward on Greece.
- In the sheets the move reads slow and calm: a gentle drift and swell, nothing abrupt.

**No edge or corner shows**
- `cover_bad_at_rest` and `hero_cover_bad` are empty in all 588 entries.
- The overscan arithmetic checks out. At 320 × 868 the layout is 367 × 886, and the turned frame needs about 365 wide.
- Every patch margin is above zero; the smallest is 1.1 px.
- No edge shows in any motion sheet.

**Sources** (`data-summary.json`)
- One rise per unit, in order, with the words the sources give: Greece 13, Rome 14, Personal brand 11, Building with AI 11, Information architecture 15 (7 written, 8 planned shown as dashed rings).
- A contour every 5.5th part of the largest unit, levels rounded down. Spot checks:
  - Greece U10 (40,190): 5 levels; U0: 1
  - Rome U11: 4; U12: 5
  - Personal brand A3: 4
  - Building with AI B1: 2
  - Information architecture IA5: 4; IA6: 5
- Every written rise in both layouts closes at least min(2, its levels) rings of its own.
- What's new, at 11,000 words per contour:
  - Levels: 20, 9, 9, 4, 3, 1, 8, 5, 4. The largest day, 22 Oct, stands 20.
  - The days run in date order along the ridge, left to right in both layouts.
  - Each day is drawn in the tone of the course that filed the most words that day, matching `day_words_by_course`. For example 25 Oct is Rome purple, 28 Oct Personal brand teal, 2 Nov Building with AI purple.
- One layout shown per width: tall below 1100 px, wide at 1280 px.
- Every layer is `aria-hidden="true"` with no text.
- Layer sizes: 8,283 to 14,252 bytes, all under 20 KB.
- The Changelog, the Backlog and the Figure kinds page (`viz-examples`) have no topography at any width, theme or motion setting.

**Inside a 390 px phone's view and above the fade**
- At 390 px no course-home or What's new rise leaves the frame or reaches the fade, at rest or at any pose.
- The one exception is the home's "User Experience" ring at poses 0.75 and 1, which is the given.
- At 320 and 360 px some rises reach past the window, as the givens describe (`verify-lines.txt`).

**Legibility** (`verify-lines.txt`: no FAIL line, ends ALL CHECKS PASSED)
- No measured text falls under its bar at any pose, width or theme.
- Home area words (large text, bar 3:1):
  - Dark: lowest 3.56 (User Experience)
  - Light: lowest 3.74 at rest (Marketing, desktop); 3.77 to 4.21 across the motion poses
- Course homes:
  - Dark: lowest 4.57 ("Start the course" on its blue button, P91's on-accent figure)
  - Light: lowest 4.64 (Building with AI lede, 320 px, pose 0.5)
  - Greece: 5.5 to 5.87
- What's new: lowest 4.96 (light, 360 px, pose 1).
- The stats boxes and buttons are opaque over the lines in the images.

**Layout**
- Course-home layers span from 22 px above the hero (the top bar) to its foot, full width beside the sidebar: desktop frame x 300 to 1280.
- The home hero keeps its P92 height: [560, 800, 70] on desktop, [591, 844, 70] on a 390 px phone.

## Renderer notes

- I viewed the images downscaled: the phone sheets at about a third of their size. Lines at .16 opacity, especially blue on dark, are close to what that view can show, so finding 1 is a judgement on reduced images.
- The motion sheets show five still poses, not the animation itself. Smoothness between poses comes from the CSS (ease-in-out, alternate), not from watching it.
- I opened only some of the sheets and hero shots:
  - all four desktop motion sheets for the home and Information architecture, plus the dark desktop Greece sheet
  - the phone sheets for Information architecture (dark, part 1), the home (light) and Greece (light, part 1)
  - heroes: What's new (phone dark, desktop light), Rome (tablet dark), Building with AI (phone light)
- Everything else I judged from the data.
- The folder has no data for any reading page, so "reading pages get none" is unverified here.
- `data-summary.json` and `data-extract.json` were too large to read whole; I searched them and read sections.

**PASS**