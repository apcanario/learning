Verdict: PASS

I read everything in p95-checkA5/: README.md, outlines.json (48 outlines, 22 rejections), all of grep-lines.md, relief-measures.md, the three licence files, previous-report.md, changes.md and both contact sheets. I grepped all 48 SVGs for rect, transform, stroke, g, image, text and the 512-px background square, and found none. I also opened five SVGs (amphora, laurels, centurion-helmet, video-camera, sitemap). I found no error and no should-fix. There are three minor findings.

## Earlier findings: status

1. **centurion-helmet (should-fix): resolved.**
   - `keywords` is now only "helmet" and "helmets", and `depicts` is "a crested helmet", with no "Roman".
   - The grep lines (grep-lines.md:158–165) all name helmets: the Villanovan crested helmets in 1.1, the Tyrrhenian helmet in 1.2, the class I armour in 1.5, and the helmets of Turnus and Messapus in 12.3.
   - The caption is now true of the pre-Roman files too.
2. **Sentence splitter (minor): resolved.**
   - The B2 Terminal-Bench fragment is gone. terminal lists only B5:51, B8:98 and DD-B1:43 (grep-lines.md:414–416), which matches outlines.json:2580–2592.
   - The ". ." at 8.3:16 (grep-lines.md:217) is a whole excluded sentence removed cleanly, not a fragment left behind.
3. **Contact sheets (minor): resolved.** Both sheets print "laurels · laurel (a wreath)" and "olive · olive (a branch)".
4. **phone, A2 resting on a source title (minor): resolved.**
   - A2 is gone from `texts.brand-a` (outlines.json:2122–2135).
   - The general rule that drops the Sources section is a sound settlement.
   - See minor 1: the previous checker's list of other title-only entries had one wrong case.
5. **map as a verb (minor): resolved.**
   - IA3 no longer appears in map's `texts` (outlines.json:2930–2955).
   - The excludes now cover "maps? (to|onto|into|them)" and "does not map".
6. **olive (minor): resolved.** `depicts` is "olive (a branch)", and it covers the tree, the sapling and the crop.
7. **grep-lines.md header (minor): resolved.** Line 3 now lists everything taken out: the front matter, the Sources section, figure declarations, link targets, URLs and excludes.
8. **Busy reliefs at sheet resolution (minor): settled, and the reason is sound.**
   - Every outline passes the rule's measures: 0 thin parts, at most 13 regions, and a step of at least 3.02 px (relief-measures.md).
   - The dark sheet shows separate lines for ionic-column, owl, laurels, centurion-helmet and wolf.
   - Deferring the full-size look to P96, before any outline is placed, is reasonable. That check has to actually happen in P96.

## New findings

### Minor

1. **minor · toga (rome): the 10.5 entry rests only on a speech title.**
   - **Evidence:**
     - `texts.rome` gives 10.5 a count of 1 (outlines.json:1466–1468).
     - Its only line is 10.5:213, "Asconius' commentary on Cicero's In toga candida" (grep-lines.md:184).
     - The fourth check said each title-counted file also had prose naming the object. That was wrong for this one.
   - **Why it is minor:** the title does mean "in the whitened toga", the candidate's garment. Rome keeps toga on 24 other files.
   - **Fix:** drop 10.5 from toga's `texts`, or add "In toga candida" to `excludes`. Or leave it, with a note that the title names the garment.
2. **minor · ionic-column (greece): thin textual base.**
   - **Evidence:**
     - The outline stands on two hits (outlines.json:589–598).
     - One is a review question, 9.1:156 (grep-lines.md:44).
     - The other names an "Ionic temple" rather than a column, 9.2:16 (grep-lines.md:45).
   - **Why it is minor:** both are legitimate under the row, since an Ionic temple is built of Ionic columns. Greece has 12 outlines, so nothing hangs on it.
   - **Fix:** if the 9.1 prose discusses the orders as "Ionic" alone, a keyword such as "Ionic" restricted to the architectural sense would show the real base. Otherwise leave it.
3. **minor · servers (brand-b): source file name and depicts differ.**
   - **Evidence:**
     - The source is Phosphor `hard-drives-fill.svg` (outlines.json:2650), and `depicts` is "two stacked servers".
     - The drawing reads as two rack units, so the caption is fair.
     - One counted line, B5:148, is an "MCP server", which is software, not hardware (grep-lines.md:434).
   - **Fix:** none needed for the verdict. Optionally write `depicts` as "two stacked server units (the sign for servers)", in the same style as the other sign-for captions.

## Checks that pass

- **Licences and credits:**
  - game-icons:
    - Delapouite, Lorc and Skoll are in license.txt, and none is marked CC0 (licence-game-icons_icons.txt:7–8, 22).
    - Every credit has the form "Icon: <author>, game-icons.net, CC BY 3.0", with the CC BY 3.0 deed as `licence_url`.
    - This also meets the file's "Icons made by {author}" request.
  - Phosphor: the credit names "Phosphor Icons", the copyright holder in licence-phosphor-icons_core.txt:5.
  - Tabler: the credit names "Paweł Kuna", the copyright holder in licence-tabler_tabler-icons.txt:5.
  - The MIT `licence_url`s point to each LICENSE at the commit taken.
  - No outline is a logo, a brand mark or a recognisable character. The Minotaur and the centaur are generic mythic creatures, and the payment card is a plain card with no Perqo mark.
- **Sources and commits:**
  - All 48 outlines have a repository, path, commit and url.
  - The commits match the licence files: 82d9488…, 2b75f3a… and 58f6053….
  - `background_removed` is true only for game-icons, and no game-icons SVG keeps its background square.
  - Phosphor files are one currentColor path, game-icons files are one white path, and sitemap.svg is the Tabler filled file with its version comment.
  - All are filled variants.
- **Fit to the texts:**
  - I checked each outline's grep lines against its `depicts`. Each names the object or, where the keyword is a sign, says so in the caption:
    - the envelope for email, the bell for notifications, the magnifier for search
    - the tag for labels, the plug for a plugin, the clock for scheduled times
    - the picture for a thumbnail, the banknote for money, the barbell for a gym
    - the fork and knife for meals, the video camera for filming, the map for the course's maps
  - I found no homonym left counted.
  - The JSON counts are occurrences and grep-lines.md counts lines, so the JSON totals are equal to or above the line totals, which is consistent. For example, amphora greece is 24 occurrences against 23 lines, and centurion-helmet is 18 against 17.
- **Captions:** "<Depicts>, a stylised outline drawn as a relief from an icon. <credit>." reads correctly for every `depicts` value, including the bracketed ones, and every credit.
- **Rejections:** the reasons are true and rule-based.
  - Thin parts: aqueduct, roman-shield, sundial, ancient-ruins, spartan-helmet, greek-sphinx, chariot and barn-owl.
  - 45 separate regions: coins.
  - A step under 3 px: maze, ancient-columns and black-belt.
  - The rest are rejected as not the object, each with a stated reason.
  - On both sheets, no accepted relief shows a scatter of pieces or merged solid bands.
- **Course counts:**

| Course | Outlines | Fit after the findings above |
|---|---|---|
| greece | 12 | 12 |
| rome | 11 | 11 |
| brand-a | 10 | 10 (no margin) |
| brand-b | 12 | 12 |
| ux-ia | 15 | 15 |

Nothing for memory.
