Verdict: FIX

The separators meet every number the row sets: count and words, contour interval, size, viewBox and fit, clearance, place, phases, tone and the theme rules. The one should-fix is outside the drawing itself. Fixing the renderer for this row changed the word counts and stats shown on ten units, and the section count of one, which the row says must not change.

**Findings**

1. **should-fix: unit stats changed, against the row.** The row says: "The words of a section, a unit's stats and a course's hours do not change." README.md ("Since the earlier checks", bullet 4) says the renderer now builds lists and code blocks properly, and that the counts shown follow from that:
   - A1: 5,280 to 5,269
   - A2: 5,621 to 5,604
   - A4: 6,024 to 6,006
   - A9: 6,678 to 6,650
   - DD-A1: 7,365 to 7,334
   - B5: 8,648 to 8,642
   - B7: 7,482 to 7,483
   - DD-B1: 7,435 to 7,422, and from 10 sections to 9
   - DD-B3: 8,948 to 8,792
   - IA1: 5,412 to 5,399

   A section disappearing from DD-B1 also changes its section numbering, its "n of N" labels and its links. B7's count went up when fences stopped rendering as paragraphs, which nothing here explains. The fix may well be right, but it is a change the row forbids, made inside a row that does not cover it.
   - Fix: record the renderer change as its own row (proposed, with these numbers) and get Pedro's confirmation, or revert it.
   - None of the before or after numbers can be checked from these files. No extract covers A1, A4, DD-A1, DD-B1 or DD-B3, and the shots show only the current counts (m61 "2,765 WORDS", rm11 "2,739 WORDS").

2. **minor: some "paragraphs" are labels.** They count by the row's rule (a top-level `<p>`), but they add dots, not hills.
   - read-b7.md §10: ¶8–¶14 are script chapter labels ("1 · Hook · 00:00–00:30", 5 words) and ¶24 is "Body" (1 word).
   - read-a5.md §6: ¶2–¶4 "Once a season:", "Before every session:", "After the session:" (3 words each).
   - read-b5.md §7: ¶11 "Should trigger:" (2 words).
   - The result is that read-b7 §10, with 34 rises, reads as a dotted chain. See cuts-more/320-read-b7-sep10-dark.png and 1280-read-b7-sep10-light.png: two small blobs, a run of dots, then one hill. It is horizontal and clear, so it works, but it is the weakest match to "topographical abstract illustrations".
   - Nothing to fix under this row; mention it to Pedro if he wants labels left out.

3. **minor: a spot ring can sit inside the next paragraph's hill.** In read-ia1.md §6, ¶1 (15 words) has its spot ring at cx=200. ¶2's outer ring starts at x≈127, so ¶1 shows as a dot inside ¶2's hill (cuts/320-read-ia1-sep06-light.png). Order is kept, but the reader cannot tell it is its own rise. The same thing happens wherever many small paragraphs share one ridge (read-ia1 §1, read-a2 §2, read-ia2 §1). This follows the decision recorded in the README, so it is noted, not raised.

4. **minor: the smallest spot rings render as dots.** Rings of r=3 are 6 units across, about 1.8 px at 390 and 1.6 px at 320. They read as specks, not rings: m61 §4 ¶3 in cuts/320-m61-sep04-dark.png, read-b7 §10, read-a5 §6. There are 18 of them across 12 of the extracted pages. Acceptable as spot heights.

5. **minor: Information architecture in dark is faint.** The lines are rgb(69,123,157) at 0.62 (cuts/390-read-ia1-sep01-dark.png, shots/1280-read-ia1-whole-dark.png). They are visible but the weakest on the site. This was already decided and is reported only for completeness.

**What checks out (against the 10 items)**

- **1. Count and words.** 23 pages; 188 separators, 188 sections with a paragraph, 188 rise groups, each starting at ¶1.
  - Each "Rises" line matches its "Top-level paragraphs" word list in order and count. I compared these by eye on m61, read-a2, read-b7 §8–10, read-a5 §6, read-ia1 and read-ia2 §1, and by grep elsewhere.
  - Every section with no paragraph (quiz, carry-forward, a bare `ol`) has "No separator".
  - The children lists leave out h3/h4, ul/ol, pre, blockquote, figure, div.tbl, p.viz-cue and aside.dispute, and have no unexpected element types.
  - No paragraph text shows "- " or "1. " list marks or code fences.
  - Every rise with 0 rings in its path has a spot ring. There are no empty paths or empty groups.
- **2. Tone.**
  - Greece: ct-t1, rgb(255,107,107).
  - Rome and Building with AI: ct-t5, rgb(155,93,229).
  - Personal brand: ct-t3, rgb(42,157,143).
  - Information architecture: ct-t4, rgb(69,123,157).
  - Lines equal the page tone in all 188. They match each page's accent in the shots. The course home heroes are not in the folder, so that comparison could not be made.
- **3. Contour interval.** The levels are floor(words / (largest/5.5)), checked by hand:
  - m61 §1 (70, 29, 78 → 4, 2, 5) and §4 (123, 122, 7 → 5, 5, 0).
  - read-a2 §8: 43, 7, 23, 9, 32, 6, 49, 11, 36, 34 → 4, 0, 2, 1, 3, 0, 5, 1, 4, 3.
  - read-b7 §10 sample (51→2, 37→1, 77→3, 21→0, 122→5).
  - read-a5 §6, read-ia1 §1/§7, read-ia2 §6 (13 of max 27 → 2), read-a9 §10, rm127 §6.
  - All correct; every section's largest paragraph stands at 5.
- **4. Size and frame.**
  - Largest separators: read-b7 §10 at 6,118 B and read-ia2 §1 at 6,086 B, both within 6,144 (site checker: largest 6,118).
  - All viewBox 0 0 1200 170, xMidYMid meet.
  - The frame at 390 px is 358 × 50.7 (= 1200:170) at x=16 in all 940 pose rows, which is the column's width. The shots and cuts at 320, 768 and 1280 match the button row width.
- **5. Clearance.** No negative values in 940 pose rows. The minimum is 1.8 px (read-ia1 §6, read-a9 §2 and §5, m106, rm112); the site checker reports a 1.3 px minimum.
- **6. Place.** Every separator is followed by nav.secnav, every one is aria-hidden true, and the SVGs have no text and are focusable="false".
- **7. Phases.** Distinct on every page checked; for example m61 0, .444 … .556; read-ia6 has 11 distinct values.
- **8. Look.**
  - In all 27 images viewed, the separators read as horizontal contour drawings between the text and the next and previous, in both themes.
  - None is clipped or overlaps, and none is too strong.
  - "Whole unit" (rm11 390 dark, m61 1280 light, ia1 1280 dark): the separator stands between its section and the next band.
  - One-section view: it closes its section before the next and previous, or before "End of the unit".
  - No sideways overflow shows in any image; the frame is overflow:hidden. Scroll width itself is not in the files.
- **9. Theme rules.**
  - `.topo.topo-patch.topo-sep{aspect-ratio:1200 / 170;margin:30px 0 0}` and `.topo.topo-sep .topo-l{opacity:var(--topo-s)}`.
  - --topo-s is defined in all three token blocks (.62 dark, .6 light) and colour comes through --c / --viz-n.
  - The only literals are spacing and the ratio.
  - It follows the 4i rule of the same specificity and so wins.
  - The 30 px margin matches .secnav's 30 px.
  - The move: rotate ±3deg over 10 s, scale 1 to 1.1 over 6 s, ease-in-out, alternate, transform only with origin 50% 50%, composition replace/add, and only under prefers-reduced-motion:no-preference.
- **10.** The site checker's figures add up: 1,591 + 330 = 1,921 sections, and 1,591 × 4 widths × 2 themes × 5 poses = 63,640 poses.

**What I checked**

- Read 37 files in full or in part:
  - README.md, theme-section-9.css, verify-seps.txt and extract/choice.txt.
  - Extracts m61, read-a2, read-b7, read-a5, read-ia1 and read-ia2 (some only in part).
  - 27 images from shots/, cuts/ and cuts-more/.
- Ran structured searches over all 23 extract .md files.
- Did not open the .json extracts, and viewed only a sample of the cuts (not every width and theme of every separator).
- Could not check from these files: the unit word counts and course hours before and after, the course home heroes' colours, and page scroll width.