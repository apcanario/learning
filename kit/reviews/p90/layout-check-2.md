## Findings
None. Two judgement calls that I did not count as faults are listed first under Renderer notes, so you can decide whether they break the rules.

## Confirmed
Shots read: phone dark and light (8 parts each), tablet dark and light (6 parts each), desktop dark and light (3 parts each). Every part was read in order.

**Card and New since counts (the same in all six shots):**
- 5 course cards: Greek history and mythology, Roman history and mythology, Building a Marketable Personal Brand, Using AI to Build a Brand, Information Architecture.
- 6 New since rows.

**1. Top-to-bottom order and the hero** (phone, tablet, desktop; dark and light)
- The order is: headline "Academy", then the lede "Every self-study course in one place. Pick up where you left off.", then the map of Academy, then the Continue button, then the four tracks, then "How every course works", then the Backlog and Figure kinds links, then New since, then the changelog link.
- There is no eyebrow above the headline. The "HOME / Academy" text belongs to the top bar, which is not under review.
- The map is a box diagram on a bordered card surface, with its caption ("The map of Academy: … This build: 4 Nov 2026.").
  - On the phone it is drawn as a vertical tree.
  - On tablet and desktop it is a horizontal tree.
- The Continue button sits directly under the map, before the History section. It reads "▶ NEWEST UNIT / Information architecture · IA7 Level 3 · the backoffice", which is the newest unit, as the fresh-visit rule requires.
- There is no resume card and no "Start here".

**2. No track tiles, no totals line**
- There is no row of track buttons in any shot.
- The page ends with the changelog link ("CHANGELOG / 54 sessions since 22 October 2026, newest first") and empty page below it. There is no line of totals.

**3. The four track sections**
- History, Marketing, Technology and User Experience each have a coloured "TRACK" label, a large heading, a tinted section background and an accent rule. This holds in all six shots.

**4. One card style**
- Every card has the same structure:
  - a coloured accent bar on top
  - a coloured tag (for example "HISTORY · COURSE 1") and a status pill ("complete" or "in progress")
  - the title, then the blurb
  - a stat row
  - a progress bar with "N% WRITTEN" under it
  - an "Open the course" button in the track's colour
- It is the same at every width and in both themes.

**5. Exactly three stats, no reports or words count on a card**
- Every card's stat row shows exactly three stats, in this order: units written, in all, h of reading.
  - Greek: 13 / 13 / 16
  - Roman: 14 / 14 / 18
  - Personal Brand: 11 / 11 / 5.0
  - Using AI: 11 / 11 / 5.5
  - IA: 7 / 15 / 4.5
- No card shows a reports count or a words count.

**6. Blurbs**
- Each blurb is one sentence on two lines, ending in a full stop, with nothing cut off. This holds on phone, tablet and desktop in both themes.
  - Greek: "Bronze Age palaces … against history."
  - Roman: "The Palatine huts … against history."
  - Personal Brand: "Who pays … changes."
  - Using AI: "Which model … leaks."
  - IA: "How to read … system map."

**7. Columns**
- Phone (390 px): every track stacks its cards in one column.
- Tablet (768 px) and desktop (1280 px):
  - History shows its two cards side by side.
  - Marketing, Technology and User Experience each show one half-width card with the right half empty.
- Both themes match.

**8. Fold-outs**
- "Why history and myth together" ("the method of the track") and "Planned" ("8 courses, in the intended order") are both inside the History section's tinted background in all six shots.
- "How every course works" ("the constants") sits after the four tracks.

**9. New since**
- New since is at the bottom, after the Backlog and Figure kinds links. Each of the 6 rows has a date, an item, a track and model line, and a pill:
  1. 3 to 4 Nov · User Experience IA7 (U-7) · Session 54 · Academy · Opus 5.5 · session
  2. 3 Nov · IA7 · Level 3 · the backoffice · Information architecture · Opus 5.5 · unit
  3. 3 Nov · IA6 · Level 2 · the client app · Information architecture · Opus 5.5 · unit
  4. 3 Nov · IA5 · Level 1 · the sales and product website · Information architecture · Opus 5.5 · unit
  5. 3 Nov · IA4 · Organisation systems: schemes, structures, objects, taxonomies · Information architecture · Opus 5.5 · unit
  6. 3 Nov · IA3 · How people find and understand things · Information architecture · Opus 5.5 · unit
- Under the rows there is exactly one link, to the changelog.

**10. Light theme paper and ink** (phone, tablet and desktop light)
- The page is a warm grey-cream.
- Cards, the map surface, fold-outs and the New since panel are a slightly lighter cream, not white.
- Track sections are lightly tinted creams: rose for History, sage for Marketing, lilac for Technology, grey-blue for User Experience.
- Lines are a shade darker than the paper. Text is near-black.
- The accents are bright and legible: red, violet, deep teal, blue, and amber-brown for the fold-out labels and the "in progress" and "session" pills.
- I saw no pure white on any surface.
- Text on the filled buttons ("Open the course", the Continue button, the coloured tags) is very pale. That fits #f5f2eb, but by eye I cannot tell #f5f2eb from #ffffff on a saturated fill (see the third renderer note).

**11. Edges, overlap, legibility** (all shots)
- No ellipsis, no clipped text, nothing overlapping, and no sign of sideways scrolling: the content sits inside equal gutters at every width.
- All text is legible in both themes, including the small monospace meta text on desktop.

## Renderer notes
- **Judgement call: the History header shows "157 reports".** The History track header (not a card) reads "2 courses · 157 reports · 8 planned". The rule bans reports counts on cards only, so I did not count this as a fault. The other tracks' headers read "1 course · N of M units".
- **Judgement call: a fourth number under each card's progress bar.** Each card has a "100% WRITTEN" / "47% WRITTEN" line under the bar. I read it as the bar's caption rather than a fourth stat, because the stat row itself has exactly three. If "exactly three stats" is meant strictly, this line would count as a fourth number.
- **Button text colour cannot be checked by eye.** To confirm the light-theme button text is #f5f2eb and not #fff, check the computed colour in the DOM.
- **The Continue button says "NEWEST UNIT", not "Continue".** It is labelled "▶ NEWEST UNIT", not "Continue …". That matches the fresh-visit state; the rule names the button by what it does, not by its label text.
- **The session row's model line wraps on the phone.** In row 1 of New since, "Opus 5.5" breaks so that "5.5" sits on its own line. It is legible and not cut.
- **The IA tag wraps to two lines at every width.** "USER EXPERIENCE · COURSE IA" wraps inside its box. Nothing is cut, but the tag is taller than on the other cards.
- **A small artifact at the top-right of each card.** The coloured accent bar on top of each card ends in a slight diagonal past the card's right border (about 1 to 2 CSS px). It is visible in all shots and is not a clipping of content.
- **The desktop sidebar stops short.** It ends at about 800 px tall, with page background below it. The sidebar is not under review.
- **The two link cards sit side by side on the phone.** Backlog and Figure kinds are in two columns at 390 px, with no clipping. The one-column rule covers course cards only.

## Verdict
PASS
