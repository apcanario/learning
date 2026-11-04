**Findings**

1. Minor. `*-home-*` at every width, including `desktop-home-light-part2-of2`, `tablet-home-light-part3-of3` and `phone360-home-light-part4-of5`. On the Information Architecture card, the chip "USER EXPERIENCE · COURSE IA" is long enough to push the "in progress" pill onto its own line under the chip. On every other card the pill sits at the top right of the chip row. At 320 px (`phone320-home-light-part3-of5`) the Marketing and Technology pills wrap the same way, but the two History pills do not. So at the same width, the chip row looks different from card to card.

2. Minor. The three-stat line wraps differently on cards of the same width.
   - At 360 px (`phone360-home-light-part2/3/4`): Greek, Roman and IA fit on one line ("13 units written · 13 in all · 16 h of reading"). Marketing and Technology drop "5.0 / 5.5 h of reading" to a second line.
   - At 320 px: every card wraps.
   - This is within the rule (three stats are shown), but the card heights become uneven.

3. Minor. What's new's header against the Changelog's (`desktop-new-light-part1-of2` against `1280-changelog-light-part1-of7`):
   - The structure matches: breadcrumbs "Academy › What's new", a mono eyebrow, a large title "What's new", and a lede.
   - Two details differ:
     - The eyebrow's lead word, and the "ACADEMY" label in the top bar, are teal on What's new but ochre on Changelog.
     - The date reads "SINCE 22 OCT 2026" on What's new but "SINCE 22 OCTOBER 2026" on Changelog.
   - If the two pages are meant to read alike, align the colour and the date format.

4. Minor. The "How every course works" bar at 320, 360 and 390 px (`phone320-home-dark-part4-of5`, `phone360-home-light-part4-of5`). The "the constants" sub-label takes the middle column, so the title wraps to "HOW EVERY COURSE / WORKS" with a narrow sub-label beside it. The History track's two closed bars wrap the same way. Cosmetic only.

No errors and no should-fix items.

**Confirmed**

- **Hero:** headline "Academy" and the lede "Every self-study course in one place. Pick up where you left off." are as specified at every width.
- **Desktop totals:** set big beside the headline, only on the desktop: 56 units written, 49 hours of reading, 5 courses live.
  - 56 = 13 + 14 + 11 + 11 + 7.
  - 49 = 16 + 18 + 5.0 + 5.5 + 4.5.
  - The totals are absent at 320 to 768 px.
- **Shelf placement:** the shelf sits directly under the hero and is whole at every width. It has 64 spines plus the "8 planned" box:
  - Greece 13
  - Rome 14
  - Personal brand 11
  - Building with AI 11
  - Information architecture 7 written and 8 outlined
- **Phone first screen:** at 320, 360, 390 and 430 px, the top 1,280 to 1,864 px of part 1 holds only the top bar, the headline, the lede and the shelf. The shelf runs past the fold, and nothing else is in that first screen.
- **No Continue button and no sitemap figure** anywhere on the home, in either theme, at any width.
- **Track sections:** History, Marketing, Technology and User Experience, in that order. Each course card has:
  - the chip row (track · course, plus the status pill)
  - the title
  - a tile line of at most two lines at every width
  - three stats
  - no progress meter and no button
- **Card columns:**
  - One column at 320 to 430 px.
  - Two columns at 768 and 1280 px: History's two cards side by side; Marketing, Technology and UX each a half-width single card.
- **After the tracks:**
  - The constants bar, closed (+).
  - Site links Backlog, Figure kinds, Changelog: one to a row on a phone, three across at 768 and 1280 px.
  - "New since 2 Nov", whose heading names the day of its oldest row.
  - Its six rows, newest first: IA7, IA6, IA5, IA4, IA3, DD-B2. They match What's new's first six rows exactly.
  - Under them, one What's new link card, last on the page.
- **What's new rows:**
  - Every unit filed and every course started, newest first, grouped under day headings (3 Nov down to 22 Oct).
  - Each row has a left rule in its course's colour (Greece red, Rome purple, Personal brand teal, Building with AI purple, IA blue), the code, the title, "course · model", and a pill (unit / report / course).
  - Each course's "Start" row sits directly under its first unit:
    - Personal brand under A1
    - Building with AI under B1
    - Rome under 0.1
    - Greece under 0.1
    - Information Architecture under IA1 (30 Oct)
  - "≈ date approximate" appears on the multi-day-session history rows (24 Oct Rome 6.4 to 5.1; all of 22 Oct Greece, including its Start row).
  - The counts read "157 history reports · 29 units · 5 courses". 157 = 78 + 79 and 29 = 22 + 7.
- **Light theme:** a warm grey-cream page, cards barely lighter, near-black ink, no pure white seen. The track sections are faint tints of the course colour.
- **Dark theme:** consistent with light at every width.
- **Edges:** nothing is cut at any edge. Every shot is exactly 2× its CSS width (1× on desktop), with no content past the right edge, so no sideways scroll is evident.
- **Desktop layout:** the hero runs full-bleed beside the sidebar and the sections keep the 760 px column, which is the given design.

**Renderer notes**

- The shelf's "← Newest · IA7 · 3 Nov" marker is laid out inline in the spine flow. At 320, 360 and 390 px it pushes IA7 onto its own row, splitting the IA course across three rows; at 430 it splits IA8 off from IA9 to DD-IA3. This belongs to the shelf checker's remit, but it is a property of where the marker sits in the flow.
- Whether the status pill wraps depends on the chip's text length. A rule that keeps the pill on the chip's line, or always puts it on its own line, would make the cards consistent (Finding 1).
- The stats line wraps according to the width of the mono numerals: "5.0" and "4.5" are wider than "16". A fixed stat layout, or `nowrap` per stat with a consistent break point, would even out the card heights (Finding 2).
- The Changelog's "Where things stand" first bullet (session 55, P90) still describes the home as having the Academy map and the Continue button. Once this change ships, that summary is out of date, and the new session's entry should supersede it.
- The desktop sidebar ending at 800 px in the shots is the full-page capture, not the page.

PASS
