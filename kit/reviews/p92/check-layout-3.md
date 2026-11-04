**Findings**

1. **Minor:** the hours-of-reading figure is written two ways across the tiles. Greece shows "16" and Rome "18" as whole numbers. Brand A shows "5.0", Brand B "5.5" and IA "4.5", each with one decimal, including the trailing ".0". The figures themselves are right: at 250 words a minute, the source words give 16.4, 17.6, 4.95, 5.47 and 4.46 hours. Because every tile is meant to show the same fields the same way, a single format would read more evenly, either one decimal everywhere ("16.4", "17.6") or whole numbers everywhere. Rests on: home-markup.html (`.cstats`), data-extract.json `sources`, every shot.

No error or should-fix stands.

**Confirmed**

- **Order** (`built.order`, all 24 runs, and the shots): hero, then the History, Marketing, Technology and User Experience sections, then "How every course works" (folded), the site links, New since, and the one What's new link last.
- **Area headers**
  - Below 768 px, `heads` is [false, true, false, false] for all four areas at 320, 360, 390 and 430 px in both themes: the name only. The header has no rule of its own; the first tile's 3 px rule in the tone closes it.
  - From 768 px, `heads` is all true. The shots show "TRACK", the name, the lede, the count and a 2 px rule in the tone.
  - Counts: "2 courses · 157 reports · 8 planned" (the sidebar shows 78 + 79 reports), "1 course · 11 of 11 units" twice, and "1 course · 7 of 15 units", which matches 7 written and 8 null units in the sources.
- **Tiles**
  - There are five live tiles in their sections: Greek and Roman history and mythology under History, Building a Marketable Personal Brand, Using AI to Build a Brand, and Information Architecture.
  - Every tile has the same fields: chip (area and course), status pill under it, title, a tile line of at most two lines (none clipped in any shot), three stats, and the patch.
  - Each whole tile is an `a.course.live` linking to its course home. Verify opens #greece, #brand-a and #ux-ia.
  - Stats match the sources: 13/13, 14/14, 11/11, 11/11, 7/15. Area word totals add up: Greece 246,589 + Rome 263,904 = 510,493.
- **Patches**
  - In every run, each tile's `rises` matches its course's written units and words in `sources`, code for code. `plan` is empty except IA, where it is IA8–IA12 and DD-IA1–3, matching the null units. The markup carries the same labels, words and `data-rings`.
  - Within each course, rings never fall as words rise: Greece 1–5, Rome 1–5, Brand A 3–5, Brand B 2–5, IA 2–5.
  - The drawing is static: `anims` is empty under reduced motion, and in the motion runs only the hero's layer and the area words are listed. It is aria-hidden in every run.
  - The stroke equals the tone in every run, in both themes. Rome and Brand B share purple (#9b5de5 dark, #7400fe light).
  - Size: the patch width equals the tile's content width (pw = cw minus the card's padding), and the height is width/4 (60, 70, 77, 83 and 77 px). The drawing is the same viewBox 0 0 720 180 at every width.
- **History blocks:** "Why history and myth together" and "Planned" (8 courses, folded) come after the History tiles, inside that section. Below 768 px each block's sub-label sits under its title (at 430 px too). From 768 px it sits beside the +.
- **New since:** the six rows match `new_since_rows` in order (IA7, IA6, IA5, IA4, IA3, DD-B2). The heading "New since 2 Nov" names the oldest day. Rows carry their course tone as a left rule. One What's new link (`hlinks[data-one]`) comes last.
- **Site links:** one to a row at 320–430 px; three across at 768 and 1280 px.
- **Grid:** one column on a phone; two from 768 px (Greece and Rome side by side, same height). The lone tiles in Marketing, Technology and User Experience are half-width at 768 and 1280 px.
- **Light theme:** a warm grey-cream page, cards a step lighter, near-black ink, no pure white anywhere. The area bands are the tone tints (given).
- **Nothing cut or scrolling sideways:** `scroll` equals the width at every width. No text is cut at an edge in any shot, and the hero copy sits in the lower part of the hero. The first area's header shows on the first screen at every width (first area at 568/640 px, 666/780, 711/844, 772/932, 858/1024, 701/800). No patch's paths reach the viewBox edge (y about 16–164 of 180).
- **Verify:** verify-home-lines.txt ends with ALL CHECKS PASSED.

**Renderer notes**

- Patches differ in look across courses: Greece and Rome are scattered small islands, while Brand A and Brand B are dense, merged chains. This follows from the given rule (contours step by the course's own largest unit, and Brand A's smallest unit is 62% of its largest). I report it as observed, not as a fault.
- The dark theme's blue IA patch (#457b9d at the patch opacity) is the faintest of the five, but it is legible in every dark shot. It is decorative and aria-hidden.
- The patch drawings are not exactly centred: left and right margins vary by about 30–60 of 720 viewBox units. That is a few CSS px at 320 px and not visible as a fault.
- Verify's link checks cover the Greece, Brand A, IA and What's new links but not the Rome or Brand B tiles. Both of those tiles have correct hrefs in the markup (#rome, #brand-b).
- Outside this check's scope, for the hero checker: the lede says "Pick up where you left off.", but by P91 the home has no Continue.
- At 1280 px the sidebar stops at the first screen's height, which is the full-page capture, as given.

**PASS**
