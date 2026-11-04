## Findings
1. **All six shots, the end of the page (phone part07–08, tablet part06, desktop part03): three links under New since, not one.** Under "New since" there are three link boxes: CHANGELOG ("54 sessions since 22 October 2026, newest first"), BACKLOG ("The queue of chats, and the chats done") and FIGURE KINDS ("Every figure a unit can declare, with its block"). Rule 4 asks for one link, to the full changelog. The Backlog and Figure kinds boxes should go.
2. **Phone dark and phone light, part08: link text cut off.** On the phone the text in those boxes is cut short with an ellipsis: "54 sessions since 22…", "The queue of chats, …", "Every figure a unit c…". This breaks rule 6 (nothing cut). Fixing finding 1 leaves only the changelog box, but its text still needs to fit or wrap.
3. **All six shots, the first New since row: no track and model line.** The first row (date "3 to 4 Nov", item "User Experience IA7 (U-7)", pill "session") has the second line "Session 54 · the kit changelog". Rule 4 asks for a track and model line on every row. The other five rows have one ("Information architecture · Opus 5.5"). This is minor, but the rule says "each".

## Confirmed
- **Order (rules 1–4), all 6 shots:** the hero (headline "Academy", the lede word for word, the map card with its caption ending "This build: 4 Nov 2026."), then the Continue button, then History, Marketing, Technology and User Experience, then "How every course works", then New since, then the link boxes. All four track sections have their coloured header (TRACK label, title, lede, meta line, coloured rule).
- **No eyebrow above the headline, all 6:** none. The only thing above the headline is "HOME / Academy" in the top bar, which is not under review.
- **No resume card, no "Start here", no track tiles, all 6:** none of them seen anywhere.
- **Continue button in the hero, all 6:** it sits straight under the map card. It reads "▶ NEWEST UNIT" and then "Information architecture · IA7 Level 3 · the backoffice". It is coral with dark text in dark mode, red with light text in light mode. Nothing else comes between it and the map.
- **One card style, all 6:** every card has the same layout: coloured top bar, course chip, status pill, title, blurb, stat row, progress bar with "% WRITTEN", one button.
- **Card count:** 5 cards in every shot (Greek, Roman, Building a Marketable Personal Brand, Using AI to Build a Brand, Information Architecture).
- **Exactly three stats, no reports or words count, all 6:** every card shows "N units written · N in all · N h of reading": Greek 13/13/16, Roman 14/14/18, Brand 11/11/5.0, Using AI 11/11/5.5, IA 7/15/4.5. No card shows reports or words.
- **Blurbs, all 6:** each blurb is one sentence on two lines at every width, with no ellipsis and no clipped line.
- **Columns:**
  - Phone dark and light: one column.
  - Tablet dark and light: two columns. Greek and Roman sit side by side. Marketing, Technology and UX each have one half-width card with the right half empty.
  - Desktop dark and light: the same as the tablet.
- **Fold-outs inside History, all 6:** "Why history and myth together" and "Planned" (8 courses) both sit inside the History panel, below its cards.
- **New since, all 6:** "How every course works" comes first, then New since at the bottom. Every shot has 6 rows: the session row, then IA7, IA6, IA5, IA4 and IA3, each with a date, an item and a pill. No totals line at the very bottom.
- **Light theme (phone, tablet, desktop):**
  - The page is a warm grey-cream.
  - Cards and the map card are a slightly lighter cream.
  - Track panels carry soft tints (rose, sage, lilac, grey).
  - Borders and lines are a shade darker than the paper.
  - Text is near-black.
  - Accents (red, teal, violet, blue, ochre) are bright and readable.
  - No white surface anywhere.
- **Edges, overlap, legibility (rule 6):** nothing overlaps and nothing runs off the side, with no sign of sideways scrolling at any width. All text is readable apart from finding 2.

## Renderer notes
- Light theme, text on buttons: the text on the red Continue button, the "Open the course" buttons and the filled course chips looks very light. By eye I cannot tell pure white from a pale cream on a saturated background. A pixel sample would settle it against rule 5.
- Each track header has a meta line: History "2 courses · 157 reports · 8 planned"; the others "1 course · N of N units". This is not on a card and not at the bottom, so it breaks no rule. But the History line shows a reports count, which the reader may not want, given the card rule.
- The Roman card uses violet as its accent, the same colour as the Technology track, while Greek uses the History red. Same card style, so not a fault, but the colours don't map one-to-one to tracks.
- The IA card's button reads "Continue" and the other cards' read "Open the course". The hero also has a Continue button, so the label appears twice on the page.
- The chip "USER EXPERIENCE · COURSE IA" wraps to two lines on all three widths. It is not cut.
- The date "3 to 4 Nov" wraps to two lines in the first New since row at all widths.
- Desktop: the sidebar panel ends at about y=800 and plain page colour runs below it. The sidebar is not under review.
- Each card's top accent bar ends in a small slanted corner at the right, and it sits just under the track's own coloured rule, so two coloured lines stack.

## Verdict
FIX
