Verdict: FIX

Scope: everything in p95-checkA3/. I read all of outlines.json, grep-lines.md, relief-measures.md, the three licence files, both contact sheets, previous-report.md and changes.md, and grepped all 48 SVGs. There are 48 SVGs for 48 outlines. Each SVG has exactly one `fill=` and no rect, g, transform, stroke, image or text, so each is a single unedited path.

## Earlier findings: status

1. **theatre-masks (should-fix): only partly resolved.** 10.2, 2.6 and 5.4 are gone, but other files still count a mask that is not a theatre mask. See new finding 1.
2. **video-camera: resolved.** depicts is "a video camera (the sign for filming)".
3. **credit-card: resolved.** The keywords are now "Perqo card", "credit card" and "payment card", and the lines name the card itself (for example IA1:123 "spend with the Perqo card", IA4:198 "O-09 card … Perqo card").
4. **microphone: resolved.** depicts is "a microphone".
5. **bar-chart: resolved by removal.** The rejection reason is true.
   - Personal brand (brand-a) now has exactly 10 outlines. It has no margin left: losing one more drops it below the row's minimum.
6. **gladius: resolved.** 10.1's one remaining hit is Pyramus falling on his sword, which is a real sword.
7. **bridge: not resolved, although changes.md says it was.** See new finding 2.
8. **receipt (DD-A2): partly resolved.** See minor finding 3.
9. **centurion-helmet: resolved.** depicts is "a crested Roman helmet".
10. **database: resolved.** The B6 Cochrane hits are gone.
11. **Counts include non-prose: partly resolved.**
    - Fixed: the front matter is gone (magnifier's first hit is now IA1:13), and link targets are stripped.
    - Still counted, all minor:
      - **A bare URL written in the prose:** A3:60 "help.instagram.com/iphone-app/…" counts for phone through the keyword "iPhone".
      - **Bibliography entry titles:**
        - money: A2:237 "…ways to earn money" and A7:329 "…makes the most money…"
        - phone: A2:249 "phones are common" and A3:251 "Touchscreen Phones"
        - sitemap: IA1:226
    - **Not addressed:** "Two Waves Books", a publisher's name (IA1:44, grep-lines.md:534), still counts for books. The earlier report named it; changes.md does not mention it.
    - No outline loses its place over this.
12. **phone: resolved.** The form-field uses are excluded, and the ux-ia lines shown are all the device.
13. **gi caption: resolved.**
14. **New caption form: sound.** Every caption now prints "<depicts>, a stylised outline drawn as a relief from an icon. <credit>." I checked it against every depicts value (the "(the sign for …)" ones, "the wooden horse", "books on a shelf", "a karate gi with its jacket belted") and each reads correctly. The added words also cover CC BY 3.0's requirement to say the work has been adapted.

## New findings

### Should-fix

1. **should-fix · theatre-masks (greece): texts still count masks that are not theatre masks.**
   - **9.2 (count 3): all three hits are the Mycenaean gold mask.** It is named "the Mask" or "the mask", which the excludes for "Mask of Agamemnon" and "gold masks" do not catch:
     - 9.2:82 (grep-lines.md:124): "Schliemann tampered with or planted the Mask; … the mask is stylistically odd"
     - 9.2:142 (grep-lines.md:125): "The mask dates to about 1550–1500 BC"
   - **7.3:112 (grep-lines.md:123):** "the aristocratic funeral with its ancestral masks" is the Roman wax ancestor masks (*imagines*). The exclude "wax masks?" does not catch "ancestral masks".
   - **2.2:187 (grep-lines.md:119):** "the mask on a pillar in women's rites" is a Dionysiac cult mask, not a theatre mask.
   - **9.3 (count 2):** its lines are not among the eight shown, so I cannot check them.
   - **What still carries the outline:** 6.4 (tragedy and comedy) and 2.2:183 "the mask and the theatre". The outline stays and Greece keeps 12 outlines.
   - **Fix:** drop 9.2 and 7.3 (and check 9.3) from `texts.greece`, or add excludes "the Mask\b", "The mask dates", "mask is stylistically", "ancestral masks?" and "mask on a pillar".

2. **should-fix · bridge (rome): the timber bridges are still counted, and changes.md says they were taken out.**
   - **What went wrong:** the exclude "Pons Sublicius" removes the name only. The word "bridge" on the same line still counts.
   - **0.2:29 (grep-lines.md:217):** "Livy gives the first bridge, the wooden  , to Ancus Marcius". The blank is where the name was cut. 0.2 still counts 1.
   - **1.6:42 (grep-lines.md:219):** Horatius "held the far end of the  , … until the bridge fell behind him". This is the same timber bridge, and 1.6 still counts 1.
   - **New homonym, 4.2:34 (grep-lines.md:221):** "*The Boarding-Bridge of the Romans*" is a book title about the corvus, a ship's boarding plank, not an arched stone bridge. 4.2 counts 1.
   - **What carries the outline:** the Milvian Bridge files (0.3, 8.2, 8.3, 10.5) and Trajan's Danube bridge (7.3).
   - **Fix:**
     - Drop 0.2, 1.6 and 4.2 from `texts.rome`, or make the excludes match the whole sentence or line.
     - Add "Boarding-Bridge".
     - Correct changes.md, which says the timber bridges were taken out.
   - **Also check:** whether other excludes leave the keyword alive in the same way.

### Minor

3. **minor · receipt (brand-a): two hits are other senses of the word.**
   - DD-A2:256 (grep-lines.md:359) "banked receipts pay for the runway" is the revenue sense again. The new excludes do not catch it.
   - A8:213 (grep-lines.md:357) "14-day withdrawal from receipt" means receiving the goods, not a slip of paper.
   - **Fix:** exclude "banked receipts" and "from receipt". DD-A2 still stands on 245 "before the first invoice". A8 carries the outline in either case.

4. **minor · laurels (greece, rome): depicts says "a laurel wreath", but several texts name the tree or a sprig.**
   - Tree or plant: Daphne "becomes the laurel" (3.7:30), the "sacred laurel" on the palace (rome 12.3:22), a "laurel grove" (12.5:42), "a sprig of laurel" (11.7:52), and the laurel Virgil's mother dreamed of (12.1:14).
   - Wreath files that fit: greece 8.3 (the Pythian prize) and rome 7.3:86 "laurel leaves from his garland".
   - **Fix:** depicts "laurel (a wreath)", or keep the plant-only files out of `texts`. This is the same kind of issue as the centurion-helmet finding last round.

5. **minor · owl (greece).** 5.3:103 "from about 515, the owls" names the Athenian coins. The coins carry an owl, so the caption is not false, but the page is about coinage. Optional: keep 5.3 out, or accept it as is.

6. **minor · outlines.json "about".** It says the count takes out "figure declarations and each outline's excludes". Since this round it also takes out the front matter, link targets and URLs. Update the sentence so the record says what is stripped.

## Checks that pass

- **Licences and credits:**
  - **game-icons:** Delapouite, Lorc and Skoll are all in license.txt and none is marked CC0. The credits follow the row's form exactly, and `licence_url` is the CC BY 3.0 deed.
  - **MIT sets:** the credits name the copyright holders, "Phosphor Icons" (licence-phosphor-icons_core.txt:5) and "Paweł Kuna" (licence-tabler_tabler-icons.txt:5). `licence_url` points to the LICENSE at the commit taken.
- **Sources:** every outline records repository, path, commit and url.
  - The commits match the licence files: 82d9488…, 2b75f3a… and 58f6053….
  - `background_removed` is true for game-icons and false for the MIT sets.
  - Every outline is a filled variant.
- **Logos and characters:** no outline is a logo, a brand mark or a recognisable character.
- **Busy reliefs:**
  - On both contact sheets no relief merges into solid bands or breaks into scattered pieces.
  - The densest are owl (169 lines, step 3.02 px), ionic-column (99 lines, step 3.22 px), wooden-horse (13 regions) and laurels. Their lines stay separate.
  - Every outline has 0 thin parts and at most 13 regions.
  - The rejections give true, rule-based reasons:
    - Aqueduct, roman-shield, sundial, ruins, spartan-helmet, sphinx, chariot and barn-owl are rejected for thin parts.
    - Coins is rejected for 45 regions.
    - Maze, columns and black-belt are rejected for a step under 3 px.
    - The rest are rejected as not the object.
- **Course counts as filed:**

| Course | Outlines | Fit after the findings above |
|---|---|---|
| greece | 12 | 12 |
| rome | 11 | 11 |
| brand-a | 10 | 10 (no margin) |
| brand-b | 12 | 12 |
| ux-ia | 15 | 15 |

  None of the findings above removes an outline. Each one corrects the texts or a caption.
