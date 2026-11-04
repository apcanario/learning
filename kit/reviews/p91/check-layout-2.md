**Findings**

1. **should-fix**: IA2's title on What's new is wrapped in literal straight double quotes: `"The shapes IA takes: the artefact catalogue and the course notation"`. No other row has quotes. Seen in `desktop-new-light-part2-of2.png` and `tablet-new-light-part4-of4.png`, under the 30 Oct 2026 heading. The quotes are most likely stored in the title data, so the same title may carry them wherever else IA2 is shown.

2. **minor**: On What's new the "≈ date approximate" marker is not always on its own line. Sometimes it follows straight on from the model text on the same line, and sometimes it drops to a line of its own. So "Fable 5.1 ≈ date approximate" can read as part of the model name.
   - Same line: 5.2 Marius and Sulla (`360-new-light-part7-of14.png`); 10.4 and 10.7–10.12 (`360-new-light-part10-of14.png`); 11.7 and 11.3 (`360-new-light-part9-of14.png`, `360-new-dark-part9-of14.png`); the Greek history and mythology "Start" course row (`360-new-light-part14-of14.png`, `360-new-dark-part14-of14.png`).
   - Own line: 5.3, 6.1 and 6.2 in the same part 7 shot, and every Greece row reviewed only by Fable 5.1.
   - Fix: set the marker on a line of its own every time.

3. **minor**: The course chip "USER EXPERIENCE · COURSE IA" wraps after the separator, leaving "·" dangling at the end of the first line.
   - Seen at 320, 360, 390, 768 and 1280, in both themes: `phone320-home-light-part4-of5.png`, `phone360-home-dark-part4-of5.png`, `phone-home-light-part4-of5.png`, `tablet-home-light-part4-of5.png`, `desktop-home-light-part2-of2.png`.
   - Only 430 keeps it on one line (`phone430-home-light-part3-of4.png`).
   - Fix: keep each chip segment together, or allow the line break only before the dot.

4. **minor**: The Changelog site link splits the date "22 / October 2026" across two lines at 360 (`phone360-home-dark-part4-of5.png`), 320 (`phone320-home-light-part4-of5.png`), 768 (`tablet-home-light-part4-of5.png`) and 1280 (`desktop-home-light-part2-of2.png`). A non-breaking space between the day and the month would stop it.

**Confirmed**

- **Hero:** the headline "Academy" and the lede "Every self-study course in one place. Pick up where you left off." are unchanged at every width, in both themes.
  - The totals appear on the desktop only (56 units written, 49 hours of reading, 5 courses live), set big beside the headline. None at 768 or on the phones.
  - The totals agree with the shelf and the cards: 13+14+11+11+7 = 56 units, and 16+18+5.0+5.5+4.5 = 49 hours.
  - The shelf sits right under the lede and is whole: every course block is present (Greece 13, Rome 14, Planned 8, Personal brand 11, Building with AI 11, Information architecture 7 of 15 with all 15 spines), followed by the legend line.
- **Phone first screen** (320, 360, 390 and 430, both themes): the top 1,280–1,864 px of part 1 holds only the headline, the lede and the shelf. At 390 and 430 the shelf runs past 1,864 px; at 320 and 360 it fills the whole of part 1. Nothing else enters the first screen.
- **Nothing removed is back:** there is no Continue button and no sitemap figure anywhere on the home, at any width.
- **Tracks:** four sections in order (History, Marketing, Technology, User Experience).
  - Each card has the chip row (track · course), a status pill (complete, or in progress), the title, a tile line of at most two lines, and three stats (units written, in all, hours of reading).
  - There is no progress meter and no button on any card.
  - Layout: one column at 320–430; two columns at 768 and 1280. History shows two cards side by side; Marketing, Technology and User Experience each show their one card at half width.
- **After the tracks:**
  - "How every course works" is closed (+).
  - The site links (Backlog, Figure kinds, Changelog) are one to a row at 320–430 and three across at 768 and 1280.
  - The heading reads "New since 2 Nov", which is the day of its oldest row. It has six unit rows, newest first: IA7, IA6, IA5, IA4, IA3 (3 Nov), then DD-B2 (2 Nov). These match What's new's first six rows exactly.
  - Under it is one link, "What's new", and it is the last thing on the page at every width.
- **What's new:**
  - The breadcrumbs read "Academy › What's new" and the title is "What's new". The eyebrow reads "157 history reports · 29 units · 5 courses · since 22 Oct 2026".
  - Rows are grouped under day headings, newest first: 3 Nov, 2 Nov, 1 Nov … 30 Oct, 28 Oct, 25 Oct, 24 Oct, 22 Oct.
  - Each row has a left rule in its course's colour, the unit code and title, the course and the model, and a pill (unit, report or course).
  - Each course row sits directly under its first unit or report: Building a Marketable Personal Brand under A1, Using AI to Build a Brand under B1, Information Architecture under IA1, Roman history under 0.1 (24 Oct), Greek history under 0.1 (22 Oct).
  - Approximate dates are marked "≈ date approximate" on the multi-day-session history rows (the Rome 5.x–6.x rows and all 22 Oct Greece rows).
- **Light theme:** a warm grey-cream page, cards slightly lighter, near-black ink. I saw no pure-white surface on either page.
- **Edges and scroll:** nothing is cut at any edge on either page, at any width or theme; the desktop totals end at about 1,248 px of 1,280. No shot shows anything wider than the viewport, so I found no sign of sideways scroll.
- **Dark theme:** the same structure and order as light at every width.

**Renderer notes**

- Finding 1 is almost certainly in the title data (quotes kept when the title was parsed), not in the template. Strip surrounding quotes when the title is read, or fix the source, so other places IA2's title shows are clean too.
- The "≈ date approximate" marker looks like an inline span after the model text. Making it a block element fixes finding 2 everywhere at once.
- Link titles, such as the What's new card's "Every unit and report filed and / every course started, by day", break well short of the card's width even at 430 and 768. That looks like balanced wrapping. It is acceptable, but it is why a date can split as in finding 4.
- At 320 and 360 the three card stats wrap to two lines on some cards and not others, depending on the digit widths ("5.0 h of reading" drops to a second line on the Marketing and Technology cards at 360, while the History cards stay on one line). All three stats are present, so this is not a fault.
- I could not compare the What's new title block with the Changelog page's, because there is no Changelog shot in the folder.

FIX
