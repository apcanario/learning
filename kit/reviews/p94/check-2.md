Verdict: FIX

**Findings**

1. **error**: list text is counted as paragraph words, so some rises stand for lists. The row leaves lists out. On several pages, though, a list that follows a lead-in line with no blank line between them is rendered inside the `<p>`, keeping its literal "- " or "1. " marks. Its words then go into that paragraph's rise, and sometimes that rise sets the section's contour interval.
   - Evidence from the extract (paragraph text as read in the browser):
     - `extract/read-a2.md` §8 ¶6. The lead-in "At zero hours, with the reason:" is 6 words. The ¶6 text also holds seven lines starting "- TikTok. …", so ¶6 is counted at 121 words. That makes it the section's largest paragraph: it sets the interval at 121/5.5 = 22 and stands 5 levels. ¶2 (39 words), ¶4 (43) and ¶8 (49, "1. Instagram drops to zero…") have the same problem.
     - `read-ia1.md` §6 ¶3 (220 words, the "What IA is not." line plus four "- " items), ¶4 (54) and ¶5 (104).
     - `read-b5.md` §5 ¶3 (71) and ¶10 (38).
     - `read-a9.md` §10 ¶5–¶12, including nested "  - " items (¶12 is 188 words and sets that section's interval).
   - The children lists show no `ul`/`ol` after these paragraphs (for example read-a2 §8: `h2.band p p p p p div.tbl p.viz-cue figure.viz.viz-bars p p p p p`), so the lists really are inside the `p`.
   - This is the same kind of fault as the fenced-code fix: the renderer should treat a list that directly follows a paragraph line as a list. Fixing it will change those units' displayed word counts, as the fence fix did, and the separators then need rebuilding.
   - I could not confirm from the cuts how these paragraphs look on screen.

2. **should-fix**: some rises draw nothing at all, so their paragraph is not visible. Eight rises in the sample have one or more contour levels but an empty path (`<path d="">`) and no spot ring:
   - read-a2 §3 ¶4 (40 words, 1 level)
   - read-a2 §8 ¶5 (32 words, 1 level) and ¶7 (49 words, **2** levels)
   - read-ia1 §6 ¶4 (54 words, 1 level)
   - read-ia5 §2 ¶4 (48 words, 1 level)
   - read-ia6 §3 ¶7 (61 words, 1 level)
   - read-b5 §7 ¶2 (25 words, 1 level) and ¶4 (20 words, 1 level)

   Their level rings have merged into the neighbouring rises' lines, which are credited to the neighbours. In `cuts/390-read-ia1-sep06-light.png`, ¶2–¶5 read as one long hill, with ¶4 not identifiable. This breaks "one rise per paragraph" and "simplified further rather than drop a rise". Fix: give a rise a mark wherever it has no line of its own, for example the spot ring that under-one-level rises already get, or a ring kept at its own peak.

3. **should-fix**: zero-height "rings" survive and can suppress a spot ring. The sliver filter drops only rings under 6 units in both directions, so closed paths with zero height still pass. Examples:
   - `M776 88l-6 0z` (read-b8 §1 ¶8)
   - `M344 88l32 0z` (rm03 §4 ¶1)
   - `M912 80l17 0z` (rm11)
   - `M184 88l19 0z` and `M688 88l21 0z` (read-ia6 §3)
   - `M944 88l12 0z` (read-ia6)
   - `M544 80l8 0z` (read-ia1 §1)
   - `M400 96l11 0z` (read-ia5)
   - `M352 96l12 0z` (read-ia3)
   - `M280 88l6 0z` (rm03)

   They draw as dashes, not rings; one is visible in `cuts-more/768-read-a1-sep03-light.png`. In read-b8 §1, ¶8 (26 words, 0 levels) and ¶10 (27 words, `M952 80l-5 0 13 1 22-1z`, 1 unit tall) count as "a ring of its own", so they get no spot ring. ¶8 shows only as a 6-unit dash, about 1.8 px at 390 px. Fix: drop a closed ring when either dimension is under the threshold (or its area is about zero), and give the rise its spot ring in that case.

4. **minor**: the README and the extract disagree on read-b7 §10. The README says it "holds 36 paragraphs"; `extract/read-b7.md` and `extract/choice.txt` both say 34. Counting `p` in its children list gives 34, so the README figure looks stale from before the fence fix.

5. **minor**: the Information architecture separators are faint in dark mode: rgb(69,123,157) at 0.62 on near-black, as in `cuts/1280-read-ia1-sep06-dark.png`. They are still visible and decorative, and this was left on purpose (README); noted only.

**Passes**

- **Count:** in the 23 extracted pages, 209 sections. All 188 sections with a top-level paragraph have exactly one separator; the 21 with none (self-test, carry forward, m93 §9 reading list) have no separator. Every separator has one `g.ct-rise` per paragraph, labelled in order, with matching `data-words`. `p.viz-cue`, `pre`, `blockquote`, `aside`, `figure`, `div.tbl`, `ul` and `ol` are all excluded.
- **Interval, checked by arithmetic on about 80 rises:** m61 §1/4/5/8/9; read-b7 §8/9/10; read-b8 §1; read-a2 §1/6/7/8; read-a9 §10; read-ia1 §1; read-b5 §5. Every level equals floor(words ÷ (largest ÷ 5.5)). For example, b7 §10 interval 22.18: 77→3, 69→3, 21→0.
- **Tone:** each page's lines are its tone. Greece is ct-t1 (255,107,107), Rome and Building with AI ct-t5 (155,93,229), Personal brand ct-t3 (42,157,143), Information architecture ct-t4 (69,123,157). Rome's lines match the purple of its band and buttons in the shots.
- **Size and frame:** the largest in the sample is 5,897 B; site-wide the largest is 5,961 B (`verify-seps.txt`), both under 6,144. Every separator has viewBox 0 0 1200 170 with xMidYMid meet. The frame is 358 × 50.7 at 390 px (ratio 7.06, against 1200/170 = 7.06), the column's width, and the 1280 cuts span the text column.
- **Clearance:** all 940 pose rows are positive. The closest in the sample is 1.8 px (rm03, read-a9, m106, rm112); site-wide it is 1.3 px. The pose transforms show 3 degrees at a scale of 1.1.
- **Place:** every separator is aria-hidden, contains no text element, and is followed by `nav.secnav`. In "Whole unit" view it stands between a section and the next band (shots).
- **Phases:** distinct on every one of the 23 pages.
- **Theme:** opacity comes from `--topo-s` (.62 dark, .6 light), tone from `--viz-n`, and `aspect-ratio` 1200/170. The only literal values are the 30 px margins, which are spacing.
- **Move:** turn and breath as the theme specifies, transform only, about the centre, nothing under reduced motion.
- **Look:** at 320, 390, 768 and 1280, dark and light, the separators read as a horizontal topography with clear space above and below. Nothing is clipped or overlapping, there is no sideways scroll, and the next/previous labels fit at 320.

**Not checked:** that unit stats, course hours and text are unchanged, and the counts for dd-b1 and a1 (no extract for those pages).

**What I read:** `README.md`, `theme-section-9.css`, `verify-seps.txt` and `extract/choice.txt`. All 23 extract `.md` files through searches across them, `m61.md` in full, the relevant parts of read-a2, read-b7, read-b8, read-ia1, read-b5 and read-a9, and part of `rm11.json`. 22 images: 5 shots, 11 cuts and 6 cuts-more.