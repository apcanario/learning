Verdict: PASS

The files show no errors and nothing that needs fixing. There are three minor findings, listed after the checks.

## Checks against the row

1. **Count and words: pass.**
   - The extract covers 23 pages and 209 sections. 188 sections have at least one top-level `p`, and each of those has exactly one `div.topo.topo-patch.topo-sep`. The other 21 (quiz, carry and one plain `ol`) have no top-level `p` and no separator.
   - In every section, the number of rises (`g.ct-rise` with a `data-label="¶n"`) equals the paragraph count, and each `data-words` matches that paragraph's words, in order.
   - I counted the plain `p` entries in the children lists by hand for read-ia1 section 1 (16) and read-b7 section 10 (34); both match.
   - `p.viz-cue`, `blockquote`, `aside.dispute`, `ul`/`ol`, `pre`, `div.tbl`, `figure.viz` and `h3`/`h4` are all left out.
   - No paragraph text in the extracts shows a leading "- " list mark or a fence.
   - read-b5 section 3 has paragraphs that open "1. ", "2. " … "5. ". They read as bold lead-ins, in the same style as that section's "The decision cluster." and "What his four repository skills do differently.", so counting them as paragraphs looks right. The unit's source text is not in the folder, so I could not confirm this.
   - verify-seps.txt is consistent: 1,921 sections = 1,591 separators + 330 without a paragraph.
2. **Tone: pass.** Lines match each page's tone in all 188 separators:
   - Greece rgb(255,107,107) (`ct-t1`)
   - Rome rgb(155,93,229) (`ct-t5`)
   - Personal brand rgb(42,157,143) (`ct-t3`)
   - Building with AI rgb(155,93,229) (`ct-t5`)
   - Information architecture rgb(69,123,157) (`ct-t4`)

   The history reports use the course colour, not the unit colour. The shots show this: m61 is red while the "UNIT 6" label is blue, and rm11 is purple while "UNIT 1" is orange.
3. **Contour interval: pass on every sample.** Levels = floor(words ÷ (largest ÷ 5.5)):
   - m61 section 1 (interval 14.18): 70→4, 29→2, 78→5.
   - m61 section 4 (22.36): 123→5, 122→5, 7→0.
   - read-ia1 section 1 (28.55): all 16 rises match, for example 64→2, 89→3, 127→4, 137→4, 111→3.
   - read-ia2 section 6 (4.91): 27→5, 20→4, 9→1, 3→0, 6→1, 13→2.
   - read-b7 section 9 (11.45): 47→4, 19→1, 63→5.
   - read-b7 section 10 (22.18): 51→2, 37→1, 77→3, 69→3, 21→0, 28→1.
   - read-a5 section 6 (13.82): 29→2, 38→2, 23→1.
   - read-b8 section 1 (27.27): 77→2, 123→4, 124→4, 35→1, 27→0.
4. **Size and frame: pass.**
   - Largest separators in the extract: read-b7 section 10 at 6,118 B, read-ia2 at 6,086 B, read-ia1 at 5,231 B, all at or under 6,144. verify-seps.txt gives 6,118 B as the largest on the site.
   - All 188 have `viewBox 0 0 1200 170` and `xMidYMid meet`.
   - At 390 px the frame is 16, 358 × 50.7 in all 940 pose rows. That is the column (390 − 2×16), and 358/50.7 = 7.06 = 1200/170.
   - At 1280 px the cuts show the frame spanning the column, from the left edge of the previous button to the right edge of the next (about 426–1154 px).
5. **Clearance: pass.** None of the 940 pose rows has a negative or zero clearance. The smallest are 1.8 px (read-ia1 section 6, read-a9, m106, rm112) and 1.9 px (rm03, read-a9). verify-seps.txt reports 1.3 px over 63,640 poses. The json transforms show the pose rotations at about ±3° with scale 1.1, so the poses really are at the top of the breath.
6. **Place: pass.** Every separator is `followed by nav.secnav`, carries `aria-hidden="true"` and has no text node or `title`/`desc`/`text` element.
7. **Phases: pass.** Phases are distinct on every page, evenly spaced at k/N (m61 in ninths, read-ia6 in elevenths, and so on).
8. **Look: pass.** I looked at the cuts and shots at 320, 390, 768 and 1280 px in both themes, across m61, rm11, read-ia1, read-b7, read-b8, read-a2 and read-dd-b3.
   - Every separator reads as a flat, horizontal contour band between the text and the next/previous buttons, clear of both.
   - Nothing is clipped or overlaps, and the next/previous labels fit at 320 px.
   - In "Whole unit" view the separator sits between a section and the next band (390-m61-whole-dark, 1280-rm11-whole-light, 1280-read-ia1-whole-dark).
   - The cuts show no sideways overflow. They cannot prove there is no horizontal scroll; verify-seps.txt says nothing about scroll either way.
   - The IA blue in dark is the faintest, as the README already accepts.
9. **Theme rules: pass.**
   - The separator rule adds only `aspect-ratio:1200 / 170` (the row's geometry) and `margin:30px 0 0` (spacing).
   - Opacity comes from its own token, `--topo-s`: .62 in dark and .6 in both light blocks. Stroke comes from `--c`, set from `--viz-N`.
   - The turn is ±`--topo-turn` (3deg) over `--topo-cycle` (10s), ease-in-out, alternating. The breath is 1 to `--topo-grow` (1.1) over `--topo-breath` (6s), added on top. Transform only, about the centre, and only under `prefers-reduced-motion:no-preference`.
   - Spacing is consistent with section 9: `.secnav` keeps its 30px top margin, so the separator has 30 px above it and 30 px below. In "Whole unit" the next section starts 34 px below.

## Findings

1. **minor: small closed rings can still look like dashes on a phone.**
   - read-b7 section 10, rise ¶25: closed path `M800 95l-2 1 2 2 8 2 9-4-1-5z`, about 19 × 9 units, so roughly 2.2 px tall at 320 px. In cuts-more/320-read-b7-sep10-light.png it shows as a short dash in the row of dots.
   - read-ia1 section 7, rise ¶3: `M496 80l8 4 8 0 16 0 16-4-8-4-8-2-16 2z`, 48 × 10 units. In cuts/320-read-ia1-sep07-light.png and cuts/390-read-ia1-sep07-light.png it shows as a thin lens.

   Both pass the stated cut-off (6 both ways, 8 either way), so this is not wrong against the row. If wanted, raise the minimum height to about 12 units, or replace such a ring with the spot ring.
2. **minor: the largest paragraphs often draw no closed ring of their own.**
   - 36 rises standing 5 levels have "0 rings in its path, a spot ring", across 16 of the 23 pages.
   - read-ia1 section 3: the 200-word and 193-word paragraphs both have only spot rings on one long merged ridge (cuts/390-read-ia1-sep03-dark.png).
   - read-ia2 section 6: the 27-word paragraph, the section's largest, draws no ring, while the 13-word ¶7 draws closed rings.

   The README already accepts this. I note it only because, in these sections, a reader cannot see which paragraph is largest. No fix is required by the row.
3. **minor: one separator is close to the size cap.** read-b7 section 10 is 6,118 B, 26 B under the limit. Any later edit to that section that adds a paragraph will need further simplification.

## What I checked and how many files

I read the README, theme-section-9.css, verify-seps.txt, extract/choice.txt, m61.md and read-ia1.md in full, parts of read-b7, read-b8, read-a5, read-ia2, read-b5 and m106, and part of rm11.json. I searched all 23 extract .md files and two .json files for children lists, paragraph counts, separator lines, rises, phases, bytes, spot-ring radii, pose clearances and path or attribute content.

I viewed 45 images: 22 from cuts/, 15 from cuts-more/ and 8 from shots/.

I could not check:
- the units' source markdown (for the b5 numbered lead-ins);
- any page or width beyond the extracts, cuts and verify-seps.txt summary;
- horizontal scroll, other than visually in the cuts.

Nothing new about the user for memory came up.