**Findings**

1. **Error: on a phone the first screen does not hold the whole shelf.** Files: `phone320-home-*-part1/2`, `phone360-home-*-part1/2`, `phone-home-*-part1/2`, `phone430-home-*-part1/2`. Nothing else appears above the shelf, so the first screen shows only the headline, the lede and the start of the shelf. But the shelf runs far past the fold. On the shots it ends at about 2,280 CSS px at 320, about 2,160 at 390 and about 1,800 at 430. That is two to three screens of 640–932 px. The first screen ends partway through Greece or Rome. Marketing, Technology and User Experience, and their captions, are all below the fold at every phone width. The cause is the spines wrapping: Greece and Rome break onto a second row at 320, 360 and 390, and every course gets its own block with a caption. If the rule means "the whole shelf on the first screen", this fails at every phone width.

2. **Should-fix: on the desktop the hero and shelf do not line up with the body column.** Files: `desktop-home-light-part1-of2`, `desktop-home-dark-part1-of2`. The headline, the lede and the shelf start about 32 CSS px right of the sidebar (x≈332). The totals run to x≈1,248. The track sections, the constants, the links and New since sit in a narrower centred column from x≈426 to about 1,154. So there are two left edges about 94 px apart, and the hero is wider than everything below it.

3. **Should-fix: the chip text wraps badly in the course cards.**
   - "USER EXPERIENCE · COURSE / IA" leaves "IA" alone on line 2 at 390 (`phone-home-dark-part5`), 768 (`tablet-home-light-part3`) and 1280 (`desktop-home-light-part2`).
   - At 320 (`phone320-home-light-part4/5/6`) "MARKETING · COURSE / A" and "TECHNOLOGY · / COURSE B" wrap the same way, and "USER EXPERIENCE / · COURSE IA" starts its second line with the dot.

   Only 430 keeps every chip on one line. The chip is a two-part label, track and course, and it should break between those parts, not inside one.

4. **Should-fix: two courses share one colour.** Rome (History · Course 2) and Building with AI (Technology · Course B) use the same violet. You can see it on the shelf, on the card chips (`tablet-home-light-part2`, `desktop-home-*`) and on the row bars in What's new (`phone-new-dark-part2/3`: the B-rows on 2 Nov and the Rome rows on 1 Nov). The rule gives each What's new row "the course's colour", but these two courses cannot be told apart by it.

5. **Should-fix: "units" counts two different things.** What's new's eyebrow says "186 UNITS · 5 COURSES" (`phone-new-*-part1`, `desktop-new-light-part1`). The home's live total says "56 UNITS WRITTEN" (`desktop-home-*-part1`). The 186 counts every history report as a unit (157 reports plus 29), and those rows carry the "unit" pill. The home counts the 27 history units, 13 + 14, plus 29. A reader moving between the two pages sees 56 units on one and 186 on the other.

6. **Should-fix: course-start rows sit above their first unit.** At the bottom of What's new, the order is 0.2 › Start (Greek history and mythology, "first unit 0.1") › 0.1 (`360-new-light-part15-of15`, `360-new-dark-part15-of15`). On 30 Oct it is IA2 › Start (Information Architecture, "first unit IA1") › IA1 (`desktop-new-light-part2-of2`). Read newest first, that puts the course starting after its first unit was filed. The Start row should be the last row of its course on that day.

7. **Minor: the model name breaks across lines.** At 390 the meta line wraps as "Information architecture · Opus / 5.5", leaving "5.5" alone. This happens on What's new (`phone-new-*-part1/2`) and in New since (`phone-home-dark-part6`). At 320 it becomes three lines, "Information / architecture · Opus / 5.5" (`phone320-new-*`, `phone320-home-light-part7`). The model name should not break.

8. **Minor: at 320 the row title column is very narrow.** The code column and the pill column leave the title about 150 CSS px. IA4's title runs to six lines in New since (`phone320-home-light-part7`) and in What's new (`phone320-new-dark-part2`).

9. **Minor: the third card stat drops to a loose second row at 320 and 360.** "h of reading" wraps with a gap of about 50 CSS px above it (`phone320-home-light-part3/4/5/6`, `phone360-home-light-part3/4/5/6`). At 390 and wider all three stats fit on one line.

10. **Minor: the History track has uneven spacing at its foot.** The gap between "Why history and myth together" and "Planned" is about twice the gap between cards, and there is a similar empty band under "Planned" (`phone430-home-light-part3`, `tablet-home-light-part2`, `desktop-home-*-part1`). It looks like an empty element or a doubled margin.

11. **Minor: the site links stay in two columns on a phone.** Changelog sits alone at half width with an empty cell beside it. At 320 its text runs to four lines (`phone320-home-light-part6`, `phone360-home-light-part6`).

12. **Minor: the "← Newest · IA7 · 3 Nov" marker comes loose when the User Experience row wraps.** At 320, 360 and 390 the marker drops to the next line, so its arrow points at empty space (`phone-home-dark-part2`, `phone320-home-light-part2`). At 430 the IA8 spine sits alone at the far right and the remaining planned spines wrap under the written ones (`phone430-home-light-part2`). Every spine is present, so the shelf is whole. The shelf's own checker should look at this.

13. **Minor: the "NEW SINCE" heading reads as unfinished.** It is a bare "New since" with nothing after it (`phone360-home-light-part6`, `desktop-home-light-part2`).

**Confirmed**

- **Hero:** the headline is "Academy" and the lede is "Every self-study course in one place. Pick up where you left off." at every width.
- **Live totals:** on the desktop they sit big beside the headline: 56 units written, 49 hours of reading, 5 courses live. These match the cards: 13+14+11+11+7 = 56; 16+18+5.0+5.5+4.5 = 49; 5 courses. The totals are absent at 768 and on phones, as the rule requires.
- **Shelf position:** it sits directly under the hero at every width, before the tracks. Every course and every spine is present.
- **Removed items:** there is no Continue button and no sitemap figure anywhere on the home, at any width or in either theme.
- **Track sections:** History, Marketing, Technology and User Experience appear in that order.
- **Course cards:** each has the chip row (track · course, plus a status pill: "complete" or "in progress"), the title, a tile line of at most two lines at every width, and three stats (units written, in all, h of reading). None has a progress meter or a button.
- **Card layout:** one column at 320–430. From 768 there are two columns: History's two cards sit side by side, and the single cards for Marketing, Technology and User Experience are half width (`tablet-home-light-part2/3`, `desktop-home-*`).
- **Order after the tracks:** "How every course works" (closed, "+"), then Backlog, Figure kinds and Changelog, then New since.
- **New since:** six rows, unit rows only, newest first: IA7, IA6, IA5, IA4 and IA3 on 3 Nov, then DD-B2 on 2 Nov. These match What's new's first six rows exactly. The What's new link is the last thing on the page at every width and in both themes.
- **What's new layout:** breadcrumbs "Academy › What's new"; title "What's new"; rows grouped under day headings (3 Nov 2026, 2 Nov 2026, 1 Nov 2026, 30 Oct 2026…), newest first. Each row has a course-colour bar, the unit code, the title, "course · model" and a pill. Unit pills are green and course pills amber.
- **Approximate dates:** the Greece rows in parts 11–15 at 360 all carry "≈ date approximate". The lede explains the ≈ convention.
- **Light theme:** warm grey-cream page, cards a little lighter, near-black ink. No pure-white surfaces are visible. Track tints are muted.
- **Dark theme:** consistent on both pages.
- **Edges:** nothing is cut at any edge, and nothing runs past the right gutter at 320–1280. The desktop sidebar ends at 800 px, but that is the screenshot, as the brief says.

**Renderer notes**

- Whether the whole card is the link cannot be checked from screenshots. Confirm in the DOM that the card is a single anchor with no nested links.
- No sideways scroll is inferred from the screenshots only: each shot is exactly 2× the viewport, or 1× on the desktop, and no content passes the gutter. Check `scrollWidth <= clientWidth` at each width.
- Spine labels in the light theme look white on the coloured spines. Pixel values cannot be read here, so check that the token is not #fff.
- In parts 11–15 at 360, the oldest Greece rows, 10.7 down to 0.1, form one block with no day heading inside it. The headings for 24 Oct and 22 Oct must therefore be in part 10 or earlier, which was not supplied. I cannot confirm that both approximate days have their own heading, or where 24 Oct stops and 22 Oct starts.
- The chip wrapping (finding 3) can be fixed by keeping track and course as separate non-breaking spans that may wrap only at the dot. The model-name break (finding 7) can be fixed by setting `white-space: nowrap` on the model.
- The extra space at the foot of the History track (finding 10) probably comes from an empty wrapper, such as a hidden "planned" list, that still gets block margin.
- Fixing the desktop alignment (finding 2) means putting the hero and shelf in the same max-width column as the body, or widening the body to match the hero.

**FIX**
