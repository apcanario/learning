Verdict: FIX

The separators themselves meet the row on every point I could test: count, words, tone, interval, size, frame, clearance, place, phases and theme rules. The verdict is FIX for three should-fixes. One is in P94's own output: sections with very many paragraphs draw as a dotted line with a few round blobs, not a horizontal topography. The other two are older faults that are not P94's work but show up in the cuts and the extracts I was asked to judge.

**Findings**

1. **should-fix**: Sections with many paragraphs become dots and round blobs instead of a horizontal topography.
   - File: `extract/read-b7.md`, §10. It has 38 rises at 6,117 B, just under the 6,144 B limit.
   - 27 of the 38 rises are spot rings.
   - Several of the rest are only broken dashes:
     - ¶2: `M152 104l16 8M160 100l8 4`
     - ¶18: `M560 101l24-5`
     - ¶26: `M768 79l5 1z`, which is 5 units long, about 1.5 px at 390.
   - The large rises are packed into narrow slots and stand tall or round, not horizontal:
     - ¶4 (165 words) spans x 176–256 and y 40–116.
     - ¶3 spans x 128–216 and y 52–112.
   - The same happens in `extract/read-ia2.md` §1 (25 rises). ¶1 spans x 98–184 and y 56–112; ¶14 spans x 591–704 and y 43–118.
   - Pedro asked for "paragraph separators (the ones that are more horizontal)". These two drawings will not read that way at 390 px, where 1 unit is about 0.3 px.
   - No cut of these pages was supplied, so this comes from the coordinates only.
   - Fix: past some number of rises, give each rise a wider, flatter footprint (let rises overlap, or flatten the vertical scale). Drop strokes under about 10 units. Produce cuts of read-b7 §10 and read-ia2 §1 for review.

2. **should-fix** (older fault in section 9's next and previous buttons, outside P94): at 320 px the "PREVIOUS · n OF 11/10" label runs past the button's right border.
   - Seen in `cuts/320-m61-sep04-dark.png` and `-light.png` ("3 OF 11"), `cuts/320-m61-sep09-light.png` ("8 OF 11") and `cuts/320-rm11-sep05-dark.png` ("4 OF 10"). Single-digit totals fit (`cuts/320-read-ia1-sep07-dark.png`).
   - Cause: `.secnav a span{white-space:nowrap}` inside `.secnav a{flex:1 1 40%;min-width:0}`.
   - Fix: let the span wrap at the "·", or shorten the label below about 340 px. This needs its own backlog row.

3. **should-fix** (older fault in the unit's text, outside P94): a broken code fence in `read-b7.md` §10 is shown as a paragraph and drawn as a rise.
   - ¶22 (36 words) reads "```\nA · Swiss-grid (aligned left, …) row 1, light blue, small: SEASON 1 · EP. 3 …" (`extract/read-b7.json` line 1837).
   - The literal "```" shows that the block was not turned into a `<pre>`. ¶23 ("B · HUD/glitch …") looks like the rest of it.
   - Because of this, a code block is counted as paragraphs and raises the section's rise count.
   - Fix: repair the fenced block in the source or in mdcourse.py, then rebuild. The section's paragraph count and its separator will change.

4. **minor**: Rises below one level are sometimes drawn with a ring as well as their spot ring.
   - `extract/read-ia6.md` §6 ¶3: 24 words against an interval of 26.9 (0 levels), yet the path holds a closed ring `M504 79l-6 1 22 2 14-2-6-3-8-1z` around the spot at (520,80) r=5.
   - `extract/read-b8.md` §1: ¶8 (26 words, interval 27.3) has `M776 88l-6 0z`; ¶10 (27 words) has `M952 80l-5 0 13 1 22-1z…`.
   - `extract/read-b1.md` §1 ¶4: 46 words, 1 level, but 2 rings; the second is `M792 80l-1 0z`.
   - Likely cause: the neighbouring hills lift these rises over the next contour line.
   - Fix: clamp each rise's contours at its own level, or drop the spot ring when a ring is drawn.

5. **minor**: Separators carry zero-area pieces of path.
   - 27 closed one- or two-step slivers across the 23 pages, for example `M1064 94l0 3z` (read-b7), `M832 87l0 1 1 0z` (read-ia2), `M792 80l-1 0z` (read-b1), `M1032 80l-1 0z` (read-ia3).
   - There is also a 41-unit stroke through a spot ring: `M1036 80l9 40` on read-b7 §10 ¶37, a 0-level rise.
   - These waste bytes and can render as specks.
   - Fix: filter subpaths below a minimum length or area in the simplify step.

6. **minor**: The Information architecture separators are the faintest in dark mode.
   - Lines are rgb(69,123,157) at .62 on near-black, about 2.3:1 by my arithmetic. Rome is about 2.5:1 and Greece about 3.3:1.
   - They are visible but weak in `cuts/1280-read-ia1-sep07-dark.png` and `cuts/768-read-ia1-sep04-dark.png`. They are decorative and aria-hidden, so no contrast rule is broken.
   - Possible fix: a per-tone `--topo-s`, or a check by eye.

7. **minor**: A separator whose paragraphs are mostly short reads as scattered dots.
   - `cuts/1280-read-ia1-sep07-dark.png` and `-light.png`: rises of 19, 4, 23, 4 and 11 words give four dots and a lens, with one hill at the right.
   - This follows the data and is to spec. I note it for the look question only.

8. **minor**: `extract/choice.txt` gives read-ia6's separators as 22,104 bytes. The extract's eleven sizes add up to 22,658, which matches `verify-seps.txt`. The choice note looks stale; the choice of page is still correct.

9. **minor**: The pose count in `verify-seps.txt` does not show the without-motion pass. 63,680 = 1,592 × 4 widths × 2 themes × 5 poses exactly, so it says "with and without motion" without counting it.

**Checked and correct**

1. **Count and words:** 188 sections had a top-level paragraph and all 188 have exactly one separator. The 22 without (`ol.quiz`, `ol.carry`, a bare `ol`) have none. The rises match each section's paragraph count, order and word counts. `p.viz-cue`, `h3`, `h4`, `blockquote`, `pre`, `aside`, `figure` and `div.tbl` are left out. I hand-counted four paragraphs (m61 §1 ¶2 = 29, m61 §2 ¶3 = 51, m61 §4 ¶3 = 7, read-ia1 §7 ¶2 = 4) and all match.
2. **Tone:** the lines are in the page's tone on every page: Greece rgb(255,107,107) `ct-t1`, Rome and Brand + AI B rgb(155,93,229) `ct-t5`, Brand + AI A rgb(42,157,143) `ct-t3`, Information architecture rgb(69,123,157) `ct-t4`.
3. **Contour interval:** I checked about 60 rises by arithmetic across 13 sections, including edge cases. Examples: read-ia2 §6, interval 4.909, 20 words gives 4 and 3 words gives 0; read-ia5 §2, 188 words gives 4.008 and so 4; read-b8 §1, 26 and 27 words give 0.95 and 0.99 and so 0. All are right.
4. **Size and frame:** the largest is 6,117 B, under the 6,144 limit. Every separator has viewBox `0 0 1200 170` with `xMidYMid meet`. At 390 the frame is 358 × 50.7 in all 940 pose rows, which is the 390 column less 2 × 16 px at 1200:170.
5. **Clearance:** no value is negative in the 940 pose rows. The smallest are 1.8 px (m106, rm112) and 1.9 px (rm03, read-a9); the site check reports 1.3 px.
6. **Place:** every separator is followed directly by `nav.secnav`, has `aria-hidden="true"` and `focusable="false"`, and holds no text.
7. **Phases:** they are distinct on every page; for example m61 runs 0, .444, .889, .333, .778, .222, .667, .111, .556.
8. **Move:** the animation count is twice the separator count on every page (both animations run). The CSS keeps it to transform only, gates it on `prefers-reduced-motion:no-preference`, and turns about 50% 50%.
9. **Theme section 9:**
   - `.topo.topo-patch.topo-sep{aspect-ratio:1200 / 170;margin:30px 0 0}` matches `.secnav`'s 30 px.
   - The opacity is the token `--topo-s` (.62 dark, .6 light). This rule ties on specificity with `--topo-p` and wins because it comes later.
   - Nothing else is ad hoc.
10. **Cuts and shots:** every one I opened shows a thin horizontal contour drawing clear of the text above and the buttons below, not clipped, with nothing overlapping it and no sideways scroll.

**Could not check**
- "Whole unit" view: no shot. From the CSS, `.secnav` is hidden and the separator ends the section, 34 px before the next band.
- Light-theme opacity: the extract was read in dark (0.62).
- Course-home hero tones: no course home is in the folder.
- Whether word counts, unit stats and course hours are unchanged: there is no before-state.
- read-b7 §10 and read-ia2 §1: no cuts were supplied.

Separators print in print view; the row does not mention print.

I read 4 top files (README, theme-section-9.css, verify-seps.txt, choice.txt) and all 23 extract `.md` files: 8 directly and all 23 through searches of every section, separator, rise and pose line, plus part of `read-b7.json`. I opened 8 of the 24 shots and 17 of the 192 cuts, covering all three pages, all four widths and both themes.