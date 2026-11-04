## Findings
None.

## Confirmed
**Sources used:** rules.md, data.md, figure.html, and all eight PNGs: phone dark and light (part01 and part02 of each), tablet dark and light, desktop dark and light.

**Boxes in the wide svg (viewBox 700 x 289)** each match data.md:
- **Root:** "Academy", class viz-t6 (gold), as data.md says.
- **Tracks, in courses.py order:**
  - History, viz-t1 (red)
  - Marketing, viz-t3 (teal)
  - Technology, viz-t5 (purple)
  - User Experience, viz-t4 (blue)
  
  Each track tone matches data.md and the colours in rules.md.
- **History courses (viz-t1):**
  - "Greek history and" / "mythology", with "13 of 13 units" (13 of 13 in the data)
  - "Roman history and" / "mythology", with "14 of 14 units" (14 of 14)
- **Planned box under History:** "8 planned", classes viz-t1 and viz-dash. data.md lists 8 planned courses (Egypt to Japan), all in History.
- **Marketing course:** "Personal brand", "11 of 11 units", viz-t3 (11 of 11).
- **Technology course:** "Building with AI", "11 of 11 units", viz-t5 (11 of 11).
- **User Experience course:** "Information" / "architecture", "7 of 15 units", viz-t4 (7 of 15, in progress).
- **Nothing extra.** There are no other boxes. data.md lists 0 "coming soon" courses, and none is drawn. No planned box appears under a track that has no planned courses.
- **Geometry:** every box lies inside the viewBox (x from 25 to 675 of 700; lowest edge at 281 of 289). The connector lines meet the centres of the root and track boxes (x 350; 91, 257, 423, 589). The History trunk at x 35 reaches the Greek box (y 132), the Rome box (200.5) and the planned box (266).

**Boxes in the phone svg (svg.viz-alt, viewBox 328 x 518.5)** are the same 1 root, 4 tracks, 5 courses and 1 planned box:
- The tones, names and counts are identical to the wide drawing.
- Course names sit on one line here (for example "Greek history and mythology").
- Boxes reach x 320 of 328 at most; the lowest edge is at 510.5 of 518.5.
- The trunk at x 18 meets the middle of each track box (y 63, 252, 346.5, 441). The branch lines at x 38 reach every course box and the planned box.

**Links:** five `<a class="viz-a">` in each svg, and href equals data-target in every one:
- Greek history and mythology goes to #greece / greece.
- Roman history and mythology goes to #rome / rome.
- Personal brand goes to #brand-a / brand-a.
- Building with AI goes to #brand-b / brand-b.
- Information architecture goes to #ux-ia / ux-ia.

All five ids are in data.md's list of panel ids. Each aria-label matches the course name. The root, the four track boxes and the planned box have no link in either svg, which is what rules.md asks for (it names links only on course boxes).

**Legibility, phone (390 px), dark and light:**
- One frame, "frame 1 of 1 (the whole figure fits)", and the phone drawing is shown.
- Every box sits inside the frame with a right margin, and there is no sideways overflow.
- Every label and count is whole and readable. Nothing overlaps or is cut.
- The planned box is clearly dashed in red in both themes.
- Track colours read as red, teal, purple and blue, with the root in gold.
- The caption runs on across the part01/part02 boundary of the sheet. Read together, the two parts give it whole, ending "This build: 4 Nov 2026."

**Legibility, tablet (768 px) and desktop (1280 px), dark and light:**
- One frame each, "the whole figure fits", and the wide drawing is shown.
- All four tracks sit in a row with their courses below.
- The two-line labels ("Greek history and / mythology", "Roman history and / mythology", "Information / architecture") wrap inside their boxes.
- "User Experience" fits its box. All counts are readable.
- The dashed planned box is clearly dashed. Nothing is cut or overlapping, and the colours are as rules.md says in both themes.

**Caption:** "Drawn by kit/viz.py from the course data (kit/courses.py, each course's counts, provenance.json) when the site is built. This build: 4 Nov 2026." It says the map is drawn from the course data at build time and dates the build. The date matches data.md (4 Nov 2026).

## Renderer notes
- On the desktop frames (1x), the "N of M units" lines are set small in a monospace face. They are readable on the sheet but are the smallest text in the figure.
- In dark mode the connector lines are low-contrast (faint grey on near-black). They are still visible. Rules.md sets nothing for the lines.
- The phone drawing's track boxes end further left (x 300) than its course boxes (x 320). This is a stepped layout, not a fault.
- Both svgs carry the generic aria-label "sitemap". The wrapper has an empty data-alt attribute, and the wide svg carries data-x0="17". None of these shows in the render.
- On the course boxes, the connector meets the first text line rather than the vertical middle of the box. This is consistent across the figure.

## Verdict
PASS
