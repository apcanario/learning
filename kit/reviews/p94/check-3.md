Verdict: FIX

Most of the row is met. There is one should-fix: very thin rings that render as solid dashes on a phone. There are also three minor findings.

**Findings**

1. **should-fix: thin rings still render as solid dashes at phone width**
   - The "under 2 units across" rule still lets through rings 3 to 5 units tall. At 390 px the scale is 358/1200 ≈ 0.30 px per unit, so a 4-unit ring is about 1.2 px tall. Its two strokes merge into one filled bar, which is the flat-dash look the earlier check flagged.
   - extract/m61.md section 1, ¶2: `M584 96l-3 0 3 1 16 1 20-2-12-2z` spans x 581–620 and y 94–98, so 39 × 4 units. It shows as a solid dash in the middle rise in cuts/390-m61-sep01-dark.png and cuts/390-m61-sep01-light.png.
   - m61 section 9, ¶2: `M584 95l-6 1 6 1 16 1 22-2-14-3z` is 44 × 5 units. It shows as a dash in cuts/320-m61-sep09-light.png.
   - Rings assembled from open pieces belonging to two rises seem to escape the filter altogether. In extract/read-ia1.md section 3, ¶2 ends `M544 88l8 2 16 0 54-2M592 87l-48 1` and ¶3 ends `M622 88l-30-1`. Together they close a ring 78 × 3 units (y 87–90). It is the flat line at the centre of the lens in cuts/768-read-ia1-sep03-dark.png and cuts/1280-read-ia1-sep03-dark.png.
   - Fix: set the minimum ring thickness in CSS pixels at the narrowest width, for example at least 6–8 units so a ring is about 2 px at 320–390 px. Apply the size test to closed rings after the paths of neighbouring rises are joined, not to each sub-path alone.

2. **minor: large paragraphs with no ring of their own**
   - In the sample, 58 rises at 3–5 levels have "0 rings in its path", 29 of them at 5 levels. They show only as a spot ring inside a merged band.
   - read-ia1 section 3: ¶2 (200 words) and ¶3 (193 words) are the section's two largest paragraphs, both at 5 levels. They read as one long lens with three small circles at every width (cuts/768- and 1280-read-ia1-sep03-*.png).
   - read-ia1 section 1: all 16 rises have 0 rings. read-b7 section 8: all 8 rises have 0 rings, including the 190-word one at 5 levels.
   - This matches the intended fallback described in the README. Still, "one rise per paragraph" is readable there only through the dots.
   - Fix, if wanted: give the section's largest rise at least its innermost closed ring, so its peak shows as a peak.

3. **minor: empty paths and a misleading attribute in the markup**
   - Every rise under one level emits an empty `<path d="">`. read-b7 section 10 has 14 of them, and that separator weighs 6,107 B against the 6,144 B cap.
   - Dropping the empty paths would save about 13 B each, room that could go to less simplification. Dense, simplified separators show angular, kite-like rings, such as ¶34 in cuts-more/768-read-b7-sep10-light.png.
   - `data-rings` holds the level count, not the number of rings. read-b7 section 10, ¶21 has `data-rings="1"` with `d=""`. m61 section 2, ¶1 has `data-rings="3"` but 0 rings in its path.
   - Fix: rename the attribute to `data-levels`.

4. **minor: dark-theme Information architecture separators are faint**
   - They are the faintest on the site (cuts/1280-read-ia1-sep03-dark.png, 1280-read-ia1-sep05-dark.png) but still legible. The README already records this as a deliberate choice, and the files are consistent with that.

**Checked and correct**

- **Count and words:** All 23 extracts hold 209 sections. 188 have a separator and 21 have no top-level paragraph and no separator. The 21 are all Self-test, Carry forward and similar sections (`ol.quiz`, `ol.carry`).
  - The 931 rise labels equal the 931 paragraph entries, file by file. Sampled sections match one for one in order and words.
  - Children lists leave out `p.viz-cue`, `ul`/`ol`, `pre`, tables, figures, `aside`, `blockquote` and `h3`/`h4`, as the row asks. For example rm11 section 3 gives 3, read-b7 section 10 gives 34 with its `pre` blocks out, and read-a3 section 7 gives 2.
  - No paragraph text shows leaked "- " or "1. " list marks or code fences.
- **Tone:**
  - Greece: rgb(255,107,107), 45 separators.
  - Rome and Building with AI: rgb(155,93,229), 69 separators.
  - Personal brand: rgb(42,157,143), 32 separators.
  - Information architecture: rgb(69,123,157), 42 separators.
  - The lines equal the page's tone in every case, at opacity 0.62.
- **Contour interval:** the arithmetic holds in every sample.
  - m61 section 1 (max 78): 70→4, 29→2, 78→5.
  - m61 section 4 (max 123): 7→0.
  - m61 section 5 (max 108): 51→2, 95→4.
  - rm11 section 3 (max 148): 60→2, 108→4.
  - rm03 section 2 (max 52): 19→2.
  - read-ia1 section 1 (max 157): 64→2, 127→4, 111→3.
  - read-ia1 section 3 (max 200): 18→0, 61→1.
  - read-a5 section 6 (max 76): 38→2, 23→1.
  - read-b7 section 10 (max 122): 77→3, 25→1, 21→0.
  - rm127 section 6 (max 224): 159→3, 151→3.
- **Size and frame:**
  - The largest separators are read-b7 at 6,107 B, read-ia2 at 6,062 B and read-ia1 at 5,249 B. All are within 6,144 B, and verify-seps.txt reports 6,107 B as the site's largest.
  - Every separator has viewBox 0 0 1200 170 with xMidYMid meet.
  - All 940 pose rows have a frame of 358 × 50.7. That is the 390 px column (390 − 2 × 16), and 358 × 170/1200 = 50.7. The cuts at 1280 match the column width.
- **Clearance:** no value is negative. The smallest in the extracts is 1.8 px (read-a9, read-ia1, rm112, m106). verify-seps.txt reports 1.3 px site-wide.
- **Place:** in all 188 cases the separator is followed by `nav.secnav`, carries aria-hidden="true" and holds no text.
- **Phases:** distinct on every page, spaced k/n.
- **Look:**
  - The separators read as horizontal topographies at 320, 390, 768 and 1280 px in both themes. They sit clear of the text above and of the next and previous buttons, with nothing clipped or overlapping and no sideways scroll seen.
  - The "Previous · n of N" labels fit their buttons at 320 px.
  - In "Whole unit" view each separator stands between its section and the next band (shots/390-m61-whole-dark.png, shots/1280-read-ia1-whole-light.png).
- **Theme rules:**
  - `.topo-sep` sets only aspect-ratio 1200/170 and a 30 px top margin, which with the next and previous buttons' own 30 px gives 30 px on both sides.
  - The opacity comes from its own token, `--topo-s` (.62 dark, .6 light).
  - The move comes from section 4i: a turn of ±3° over 10 s each way, a breath from 1 to 1.1 over 6 s each way, ease-in-out, alternating, transform only, about the centre, and still under reduced motion.
  - These rules are consistent with the rest of section 9.

**Could not check:** that the units' and reports' text, displayed word counts and course hours are unchanged. No before and after source is in the folder.

**What I read:** README.md, theme-section-9.css, verify-seps.txt and extract/choice.txt in full. extract/m61.md and extract/rm11.md in full, about 230 of read-ia1.md's lines, and parts of read-a5.md, read-b7.md and read-a9.md. Grep checks across all 23 extract .md files and the .json files. 34 images from cuts/, cuts-more/ and shots/.