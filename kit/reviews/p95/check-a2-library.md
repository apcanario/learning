Verdict: FIX

Scope: everything in p95-checkA2/. I read outlines.json in full, all of grep-lines.md, relief-measures.md, the three licence files, both contact sheets, previous-report.md and changes.md. I read the gi, microphone and sitemap SVGs in full and grepped all 49 SVGs for rect, g, transform, stroke and a background square. There are 49 SVGs for 49 outlines: 20 game-icons (each a single `fill="#fff"` path, no background square) and 29 Phosphor or Tabler (`currentColor`). None has a rect, group, transform or stroke.

## Earlier findings: status

- **MIT notice (should-fix): resolved.** Every MIT outline has `licence_url` set to its set's LICENSE at the commit taken, and changes.md says the full licence texts print under "Illustration credits". I cannot see that page from this folder.
- **CC BY link (minor): resolved.** `licence_url` points to the CC BY 3.0 deed on all 20 game-icons outlines.
- **flask, robot, black-belt (errors): resolved.** All three are removed and listed under `rejected` with true reasons.
- **Camera counted twice (should-fix): resolved.** The photo camera is rejected; picture and money are added. brand-a has 11 entries for 11 distinct objects. The video-camera caption still needs a fix (new finding 2 below).
- **brain (should-fix): resolved.** Rejected; plug added.
- **tag, map, barbell, fork-knife, clock: resolved.** Each depicts is now a "(the sign for …)" caption. The tag lines are now prose uses of label/labels/tags. The verb uses of map are gone.
- **ionic-column: resolved.** The keywords are now specific. Both hits name the object: 9.1:163 "Doric from an Ionic column" and 9.2:23 "Ionic temple".
- **theatre-masks: only partly resolved.** See new finding 1.
- **wax-tablet: resolved by removal.** The reason is plausible. I cannot check the Roman texts from here.
- **terminal: resolved.** Terminal-Bench is excluded. B2:167 is left with "long agentic terminal tasks", which is acceptable.
- **gladius: resolved.** depicts is now "a short sword". One metaphor remains (minor finding 6).
- **Rome homonyms: mostly resolved.** One bridge metaphor is left (minor finding 7).
- **laurels and receipt (A7): resolved.** The receipt revenue homonym survives in DD-A2 (minor finding 8).
- **centurion-helmet: settled, but only half soundly.** See minor finding 9.
- **Busy black-belt, labyrinth (maze) and columns: resolved.** All three are rejected with step-based reasons. The 3 px minimum step is a reasonable working of "merging into solid bands". Owl (3.02 px) and ionic-column (3.22 px) look readable on both sheets.
- **Thin-part definition: settled soundly.** The 8% run is now stated in relief.py as the reading of "a part". It is an interpretation of the row, written down, which is what was asked.
- **Caption printing: resolved.** One awkward caption remains (minor finding 13).
- **Research report counted for brand-a: settled soundly.** It is published as one of the course's reading pages, and the row allows reports.

## New findings

### Should-fix

1. **should-fix · theatre-masks (greece).**
   - **Problem:** The excludes catch "gold masks" but not the same mask named without the adjective. 10.2 is still in the texts (count 2), and both lines shown are the Mycenaean gold mask:
     - grep-lines.md:118: 10.2:109 "…and the mask from Grave V. … 'I have gazed upon the face of Agamemnon'"
     - grep-lines.md:119: 10.2:113 "questioned the mask's authenticity on its upturned moustache"
   - **Other lines that are not theatre masks:**
     - 2.6:65 (grep-lines.md:122): the Gorgoneion and "Humbaba masks"
     - 5.4:61 (grep-lines.md:123): Artemis Orthia's "grotesque masks", which are votives
   - **Fix:** Drop 10.2, 2.6 and 5.4 from `texts.greece`, or add excludes for "mask from Grave", "mask's authenticity", "Humbaba masks" and "grotesque masks". 6.4, 9.2 and 2.2:190 still carry the outline.

2. **should-fix · video-camera (brand-a).**
   - **Problem:** No line names a video camera. The camera the texts mean is the phone on a tripod (A5:22 "The phone on a tripod. One static camera"). The other hits are the idiom "on camera" or "to-camera" (A1:102, A1:136, A4:48, A4:180, A5:34). The library's own rejection of camera-fill says so: "the texts' camera is the phone filming, kept as the video camera". So the camcorder is a sign for filming, but its caption reads as the object itself.
   - **Fix:** depicts "a video camera (the sign for filming)", as for the other signs.

3. **should-fix · credit-card (ux-ia).**
   - **Problem:** All eight lines shown match "card payment", which is the transaction type, not the card (grep-lines.md:588–595, e.g. "transaction, type card payment" and "Purchase is a card payment"). The object the outline depicts, the Perqo card, is in the texts: IA1:131 "spend with the Perqo card" (grep-lines.md:376) and IA4:215 "The Perqo card can be frozen". The keywords miss it.
   - **Fix:** Use "Perqo card" (and "card" in that sense) as keywords and drop "card payment". Otherwise make depicts "a payment card (the sign for card payments)".

### Minor

4. **minor · microphone (brand-a).** depicts says "a stand microphone". The texts' microphone is "One lavalier microphone… the one piece of kit bought for sound" (A5:27, grep-lines.md:294) and the phone's own mic (A5:34). Fix: depicts "a microphone".

5. **minor · bar-chart (brand-a).** Every hit is a passing "chart(s)", and four of the ten are a source title repeated in citation and bibliography: "charts as of 28 May 2025" at A7:27, A7:357, A9:103 and A9:278 (grep-lines.md:358–361). No text says "bar chart" or discusses one. It passes the "at least one text names it" rule only weakly. brand-a still has 10 without it.

6. **minor · gladius.** 10.1:32 "Jupiter's anger, fire, sword and time" (grep-lines.md:177) is the same idiom as "fire and sword" in another form. Add it to the excludes.

7. **minor · bridge.** Two smaller problems:
   - 4.2:22 "would hold the bridge to Italy" (grep-lines.md:224) is a metaphor. The exclude "bridge to the" does not catch it, and 4.2 counts 3.
   - Caesar's Rhine bridges (11.6, 5.4) and the Pons Sublicius (0.2, 1.6) were timber, not the "arched stone bridge" depicted. The Milvian Bridge files (0.3, 8.3, 10.5) carry the outline.
   - **Fix:** Exclude "bridge to Italy" and drop the timber-bridge files from `texts.rome`.

8. **minor · receipt (brand-a).** DD-A2's five hits are the revenue sense: "Tier receipts" (DD-A2:187), "trailing receipts" (:208) and "two quarters of receipts" (:251), at grep-lines.md:370–372. This is the homonym already fixed for A7. A8 carries the outline. Drop DD-A2.

9. **minor · centurion-helmet (settlement only half sound).**
   - **What holds:** The settlement's reason is that the Villanovan and Etruscan helmets are crested helmets, as the outline is. That covers the shape.
   - **What does not:** depicts is "a centurion's crested helmet", so the caption misnames the helmet on 1.1, 1.2 and 1.5. Examples are the Villanovan "crested helmet" (1.1:20, 24), Hiero's "Tyrrhenian spoils" helmet (1.2:127) and the Servian class table (1.5:93).
   - **Fix:** depicts "a crested Roman helmet", or keep those files out of `texts`.

10. **minor · database (brand-b).** B6's two hits are both the journal title *Cochrane Database of Systematic Reviews* (B6:110, 283). That is a publication name, the same kind of hit as *Black Belt*. Drop B6; the outline still stands on B1, B2 and DD-B1.

11. **minor · counts include non-prose.**
    - The front matter is counted: magnifier's first hit is IA1:7 `search: off` (grep-lines.md:610).
    - URLs and bibliography entries are counted:
      - money: A2:245 "earn-money" and A7:50's URL slug
      - book: DD-B3:525, where the only hit is in "/books/741805"
      - books: "Two Waves Books" and rosenfeldmedia.com/books
    - **Effect:** outlines.json's "about" says counts are of the prose, so this contradicts it. No outline loses its place.
    - **Fix:** Strip front matter and link targets before counting.

12. **minor · phone (ux-ia).** IA5:244 and IA5:463 are "the phone field" and "a phone number" on a form, not the device. IA6 carries the outline.

13. **minor · caption printing, gi.** "A karate gi, its jacket belted, a stylised outline." stacks two appositives. Use "a karate gi with its jacket belted".

## Checks that pass

- **Licences and credits:**
  - Every game-icons author (Delapouite, Lorc, Skoll) is in license.txt, and none is marked CC0.
  - The game-icons credits follow the row's format exactly.
  - The MIT credits name the holders in the LICENSE files: "Phosphor Icons" (licence-phosphor-icons_core.txt:5) and "Paweł Kuna" (licence-tabler_tabler-icons.txt:5).
  - Each set's licence file is at the commit its outlines record: 82d9488…, 2b75f3a… and 58f6053….
- **Brands and characters:** No outline is a logo, a brand mark or a recognisable character.
- **Sources:** Every outline has repository, path, commit and url. `background_removed` is true for game-icons and false for the MIT sets. Every outline is a filled variant.
- **Busy reliefs:**
  - On both contact sheets no relief merges into solid bands or breaks into a scatter of pieces.
  - The densest are owl (169 lines), ionic-column, wooden-horse (13 regions) and laurels, and their lines stay separate.
  - Every outline has 0 thin parts and at most 13 regions.
  - Every rejection gives a reason, and the reasons given for the not-the-object rejections hold up.
- **Course counts as filed:**

| Course | Outlines | After fixing findings 1–3 |
|---|---|---|
| greece | 12 | 12 |
| rome | 11 | 11 |
| brand-a | 11 | 11 |
| brand-b | 12 | 12 |
| ux-ia | 15 | 15 |

  Every course stays at ten or more even if bar-chart and database (minor findings 5 and 10) were dropped.
