## Shelf check (P91, Academy home): result FIX

I read BRIEF.md, data-extract.json and shelf-markup.html in full. I looked at all 20 screenshots in shots/ and at both rise sheets. Two should-fix findings and five minor ones.

## Findings

1. **Should-fix. On the three narrowest phones the "Newest" label is not beside the lit spine.**
   - Files: shots/phone320-home-{dark,light}-part2-of8.png, shots/phone360-home-{dark,light}-part2-of7.png, shots/phone-home-{dark,light}-part2-of7.png.
   - At 320, 360 and 390 px the label "← Newest · IA7 · 3 Nov" wraps onto the next row of the Information architecture group. There it sits under IA1 to IA6, with the ghost spines IA8 and after to its right.
   - Its arrow points left, at empty space at the column edge. The lit IA7 is up and to the right of it.
   - It is correctly beside IA7 at 430 px, on the tablet and on the desktop.
   - Cause: the label is a flex item inside `.shelf-books`, between IA7 and IA8, so it wraps like a spine.

2. **Should-fix. The two rise sheets come from a different build than the one being checked.**
   - Files: desktop-rise-dark.png, desktop-rise-light.png.
   - In both frames the history volume's label reads "Planned courses", and the volume sits on its own row under Greece. In shelf-markup.html and in the desktop shots (shots/desktop-home-*-part1-of2.png) the label is "Planned" and the volume sits beside Rome.
   - The caption counts also disagree: 70 animations in dark, 66 in light.
   - The rise does show: at 160 ms Greece U0 to U6 are rising and the rest of the shelf is empty; the end frame is at rest with the label in. But this does not show the current build rising. Re-shoot both frames from the current build.

3. **Minor. Rome and Building with AI are the same colour.**
   - Both use `--viz-5`, so one purple appears in two tracks (History and Technology).
   - This matches the site, which also gives Rome purple on its course card and in the sidebar. On the shelf, though, it weakens the colour grouping by track.

4. **Minor. Narrow-phone glow overlap.**
   - Same files as finding 1. Because the label wraps, IA7's glow spills over the top of the ghost IA8 directly below it.

5. **Minor. Markdown unit titles repeat their code.**
   - shelf-markup.html, e.g. `title="A1 · Personal brand · A1 · Positioning: …"`, and the same in every B and IA title.
   - Hover tooltips and screen readers say the code twice.
   - History titles ("U0 · Greece · unit 0 · Foundations") do not have this problem.

6. **Minor. The "8 planned" volume is weak as a label and does nothing when tapped.**
   - shelf-markup.html: its `title` lists the eight cultures but not the count. The count is only in `aria-label` and the visible text.
   - It is a `div`, so tapping it does nothing. The brief does not ask for a link, but the History track's "Planned" list would be the obvious target.

7. **Minor. Faint grey text in dark theme on the desktop.**
   - shots/desktop-home-dark-part1-of2.png: the "8 planned" text and the ghost spine codes are small grey on near-black. They can be read, but they are the faintest text on the shelf.

## Confirmed

- **Spine counts and order match `sources_shelf`.** Greece has 13 (U0 to U12), Rome 14 (U0 to U13), Personal brand 11, Building with AI 11, Information architecture 15. Every spine is in source order, grouped by History, Marketing, Technology and User Experience. Each course name and count sits under its group: 13 of 13, 14 of 14, 11 of 11, 11 of 11, 7 of 15.
- **Written and planned match the sources.** All 56 written spines are solid. IA8 to IA12 and DD-IA1 to DD-IA3 are ghosts: dashed outline, no fill, in both themes. The eight planned history courses are one ghost volume labelled "8 planned", whose `aria-label` lists Egypt, Persia, Norse, Celts, England, Scotland, China and Japan.
- **Links.** Every `href` and `data-target` equals its `opens` value. History spines go to `greece-uN` / `rome-uN`, markdown spines to `read-…`, planned spines to `ux-ia-b-…`. The newest label links to `#new` (`data-target="new"`). Every spine has a `title` and `aria-label` that name its code and title.
- **The lit spine is right.** It is IA7 (`spine lit`), the newest unit (2026-11-03). Its glow is in its course colour in both themes. The label text is exactly "Newest · IA7 · 3 Nov", with the arrow `aria-hidden`.
- **Heights follow word count.** `--h` is linear in words, (w − 5079) / (40190 − 5079), with B1 at 0 and Greece U10 at 1. The ordering is never inverted, equal word counts get equal values (Greece U0 and IA4, both 8613, both 0.101), and every spine I sampled checks out.
- **Measured sizes match the theme.**
  - Desktop: Greece U10 is 210 px, A1 about 61 px, B3 about 84 px, IA7 about 92 px. This fits the 60 to 210 px range.
  - Tablet: U10 is 104 px.
  - Phones: U10 is 104 px, A1 about 45 px, the IA ghosts about 52 px. This fits the 44 to 104 px range.
  - Width: spines are 24 CSS px on phone and tablet and about 26 px on the desktop. No spine is under 24 × 44.
- **Planned spines use the course mean.** Their words are 66866 / 7 = 9552, the mean of the written IA units, as the note in data-extract.json says.
- **Totals.**
  - The three: 56 units written is 13 + 14 + 11 + 11 + 7; 5 courses live; 49 hours, since the written words total 733,666, which is about 48.9 h at 250 words a minute.
  - Course cards: Greece 16 h, Rome 18 h, Personal brand 5.0 h, Building with AI 5.5 h all agree with the extract's words.
  - On the desktop the totals are set big beside the headline in both themes.
- **Full-bleed desktop.** The shelf runs from the sidebar edge (about 332 px) to about 1248 px, well wider than the track sections below it, which are about 728 px. The volume and the "Courses live" total stay inside 1280.
- **No clipping and no sideways scroll.** In both themes at 320, 360, 390 and 430 px every row ends inside the 16 px gutter: at 360, Greece's first row ends at about 320 px; at 430, Rome U13 ends at about 404 px and IA8 at about 412 px. On phones the course spines wrap into rows inside the column, and only the headline, lede and shelf show above the tracks.
- **Legible in both themes.** Codes on spines read in both themes: dark text on light fills in dark mode, white on dark fills in light mode. Ghost codes, course labels, counts, track names and the volume text are all legible.
- **Rise animation.** Spines carry a stagger index, `--i` 0 to 64 in order, with the volume at 27. The desktop static shots are at rest, which fits reduced-motion capture.

## Renderer notes

- **Phone shots are three times CSS size, not twice.** The brief is wrong here: the phone files are 960, 1080, 1170 and 1290 px wide for 320 to 430 px viewports. The tablet (1536 for 768) is twice, and the desktop is at CSS size. I measured the phones at 3×; at 2× they would wrongly appear to break the 44 to 104 px range.
- **Fix for finding 1.** Keep the lit spine and its label together in a wrapper that does not wrap, so the label stays on IA7's row. Or, on narrow widths, drop the "←" (or use "↑") and place the label after the group so it does not fall between written and planned spines.
- **The rise looks slow for a "short" stagger.** At 160 ms only about seven indices have started, roughly 23 ms apart. That puts the last spine's start near 1.5 s. Shortening the step would make it read as "short".
- **Things I could not check from these files.** Whether the `#greece-uN`, `#rome-uN`, `#read-…`, `#ux-ia-b-…` and `#new` targets exist on the page; the shelf markup alone does not show it.
- **No totals on the tablet.** At 768 px there are none. The brief only specifies desktop and phone, so this is not counted as a finding.
- **Underline widths differ by group.** A group's base line spans its spines when they fit on one row (Marketing, Technology) and the full column when they wrap. This is consistent behaviour, just uneven to look at.

FIX
