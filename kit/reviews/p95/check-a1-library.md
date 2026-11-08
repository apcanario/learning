Verdict: FIX

Scope: every file in p95-checkA/ (outlines.json in full, the 3 licence files, grep-lines.md in full, relief-measures.md, both contact sheets, and the SVGs, with the amphora, camera, sitemap and wax-tablet SVGs read in full and all 54 grepped for leftover rects, groups, strokes or transforms).

## 1. Licences and credits

- **should-fix · all Phosphor and Tabler outlines (MIT).** The caption line ("Icon: Phosphor Icons, phosphoricons.com, MIT", "Icon: Paweł Kuna, Tabler Icons, MIT") names the right copyright holder: licence-phosphor-icons_core.txt:5 says "Copyright (c) 2023 Phosphor Icons" and licence-tabler_tabler-icons.txt:5 says "Copyright (c) 2020-2026 Paweł Kuna". But MIT also requires that "the above copyright notice and this permission notice shall be included in all copies or substantial portions" (line 14 of both files). A one-line caption does not do that. Fix: publish the two LICENSE texts on Academy (a credits or licences page linked from each relief caption) or embed them in the shipped assets.
- **minor · game-icons outlines.** The credit follows the row's format, and each author matches the folder and the contributor list (Delapouite, Lorc and Skoll are at licence-game-icons_icons.txt:7, 8 and 22). None of these authors is marked CC0. CC BY 3.0 also asks for a link to the licence where reasonably practicable. Consider linking "CC BY 3.0" in the caption. "A stylised outline" already signals the adaptation.
- No outline is a logo, brand mark or recognisable character. eagle (lorc/eagle-emblem) is a generic heraldic eagle.

## 2. Sources and commits

- All three licence files were read at the same commits the outlines record: game-icons 82d9488…, phosphor 2b75f3a…, tabler 58f6053…. Every outline has repository, path, commit and url.
- The SVGs look like unedited set files. The game-icons files keep the set's `fill="#fff"` path with no background path left. The Phosphor files are the standard `fill="currentColor"` 256-unit files. Tabler's sitemap still carries its unicode/version header comment. No rect, group, stroke or transform appears anywhere. `background_removed` is set correctly for each set.

## 3. Fit to course and texts

### Errors

- **error · flask (brand-b).** The keywords "lab" and "labs" only hit AI organisations and the AI-industry sense. grep-lines.md:490–492 shows "Thinking Machines Lab", "a lab study" and "labs train on them". No text names a flask or any laboratory object. Fix: drop the outline.
- **error · robot (brand-b).** grep-lines.md:503 is "X refused the fetch (robots rule)", a robots.txt homonym. Line 504 is a quoted metaphor ("less Iron Man robots and more Iron Man suits"). The course never discusses a robot. Fix: drop it.
- **error · black-belt (brand-a).** Both lines that match are the magazine *Black Belt*, a publication title (grep-lines.md:290–291), not a belt. No text names the object. Section 4 also flags its relief. Fix: drop it.

### Should-fix

- **should-fix · brand-a reaches ten only by double-counting a camera.** camera and video-camera have the same keyword hits and the same texts with the same counts (outlines.json:2349–2367 vs 2392–2410). "video camera" itself appears in none of the lines, and the camera the texts mean is a phone on a tripod (A5:22). Without black-belt, brand-a has 10 entries but 9 distinct objects (gi, camera, microphone, phone, calendar, bar-chart, receipt, envelope, folder). Fix: keep one camera, which fits better as video-camera, and add at least one more brand-a outline whose object the units name.
- **should-fix · brain (brand-b).** The hits are idioms or a skill name: "brain dumps", "pick your brain", `brain-dump-processor` (grep-lines.md:470–476). Only DD-B3:73 names the organ, in passing. The texts do not discuss the object. Drop it, or keep it only with an honest caption. After flask and robot go, brand-b has 11; without brain it has 10, which is borderline.
- **should-fix · tag (ux-ia).** The 601 lines are inflated by JSON `"label":` keys in diagram data. All eight lines sampled are of that kind (grep-lines.md:368–375). The IA texts mean labels as words and "type tags" in the notation (IA3:233), not a physical price tag. Fix: count only prose uses, and make depicts honest, for example "a tag, the sign for labels".
- **should-fix · map (ux-ia).** The texts mean a diagram: site maps, the "object map", "The Perqo surfaces map" (grep-lines.md:552–559). Line 554 uses "map" as a verb ("how the labels map to the model"). "A folded map" is the sign for these, not the thing. Fix: depicts "a folded map, the sign for the course's maps", and drop the verb uses from the counts.
- **should-fix · barbell and fork-knife (ux-ia).** These are signs, not the objects the texts name. The texts name a gym membership and the Meals benefit category (grep-lines.md:607–625), yet the captions say only "a barbell" and "a fork and a knife". Fix: "a barbell, the sign for a gym" and "a fork and a knife, the sign for meals", as envelope, bell and magnifier already do.
- **should-fix · ionic-column (greece).** The keyword "Ionic" matches the Ionic-Attic dialect (0.2:116, 124, 207; 10.11:152). "column" matches a table column (1.2:37, "its Markers column"). The texts list counts these files: 0.2 has 4 hits and 10.11 has 1, and the philosophy units 12.1, 12.2 and 12.6 are probably "Ionic" philosophy too. Fix: match "Ionic column(s)", "column(s)" in the architectural sense only, and drop files that only use the homonyms. 9.1, with 31 hits, still carries the outline.
- **should-fix · theatre-masks (greece).** "mask/masks" matches the gold death-masks and the Mask of Agamemnon (0.3:81, 166; 1.2:13, 17; 10.2:130, 144, 186). Those are funeral masks, not theatre masks. Fix: drop 0.3, 1.2 and 10.2 from texts and keep 6.4, 2.2:202 ("the mask and the theatre") and any other files that really mean the stage.
- **should-fix · wax-tablet (rome).** The lines shown are the Pyrgi gold sheets, the Iguvine bronze tablets and the Marsiliana ivory alphabet tablet (grep-lines.md:246–253). None of those is a wax writing tablet. Fix: list only files naming writing or wax tablets (perhaps 9.2 Vindolanda, 2.4 wills; check them), and say "a wax writing tablet" in depicts.
- **should-fix · terminal (brand-b).** B2's 7 hits, the largest entry, are all the benchmark name "Terminal-Bench" (grep-lines.md:459–464). Fix: drop B2. The real uses at B5:88 and B8:140 ("terminal session") remain.

### Minor

- **minor · gladius.** depicts says "the gladius", but none of the sampled lines contains "gladius". Most are "sword" generically or the idiom "fire and sword" (1.6:43, 10.1:38). Confirm a text names the gladius, or say "a short sword".
- **minor · homonyms in rome lists.**
  - eagle: "eagle-owl" (10.1:52).
  - wolf: "Hieronymus Wolf" (0.3:165).
  - bridge: metaphors "bridge and barrier" (0.2:81) and "the bridge to the Middle Ages" (10.2:112).
  - columns: "Copy the first two columns" (0.3:33).
  - Remove those files or lines from the counts.
- **minor · laurels.** "wreath" also matches oak, myrtle and ivy wreaths (11.1:45, 11.4:95). The listed files remain valid through "laurel".
- **minor · receipt (brand-a).** In A7, "receipts" means revenue (A7:38, 189), a homonym. A8 carries the outline.
- **minor · clock (brand-b).** The texts mean time-based triggers ("fire on the clock"). Consider "a clock, the sign for scheduled times".
- **minor · centurion-helmet.** "helmet" also matches Villanovan and Etruscan crested helmets (1.1:20, 33; 1.2:133). That is acceptable but loose.

### Course counts after the errors

- greece: 13
- rome: 13
- ux-ia: 15
- brand-b: 11 (10 without brain)
- brand-a: 9 distinct objects, which falls short of ten

## 4. Busy reliefs

- **should-fix · black-belt, labyrinth, columns.** On both contact sheets their contour lines merge into solid bands and read as filled shapes, not reliefs. The labyrinth is solid red, the belt a solid teal ring, the columns solid purple. relief-measures.md shows why: steps of 1.44 px (black-belt, which also has 512 lines for one region, a sign that its contours break into fragments), 1.36 px (labyrinth) and 2.56 px (columns). They pass the row's numeric tests (0 thin parts, few regions), but the README's visual criterion ("lines merging into solid bands") fails them. Fix: reject them, or give the tool a minimum step and reject any silhouette that cannot meet it. ionic-column (3.22 px), owl (3.02 px, 169 lines) and wax-tablet (3.6 px, 133 lines, a dense hatched block on the sheet) are borderline; look at them at reading size.
- **minor · tool definition.** relief-measures.md:16–17 counts a thin part only if it runs at least 8% of the width. The row's rule ("a part thinner than 3% of its width") has no length condition. Either state this as an interpretation of the row or align the tool with it.
- The rejected list gives a reason for each candidate. The aqueduct, which the row names, is rejected as busy with 2 thin parts; I cannot verify the measure from this folder. The "not the object" rejections (column-vase, galley, arch-bridge, laurel-crown) are reasoned.

## 5. Other

- **minor · caption printing.** Every depicts value starts lowercase ("an amphora…"). If the template does not capitalise, captions start with a lowercase letter. Appositive depicts values also read awkwardly in the template: "An envelope, the sign for email, a stylised outline." and "A short sword, the gladius, a stylised outline." Consider capitalising, and restructuring sign captions to "…, drawn as a stylised outline" or similar.
- **minor · texts include a research report.** `generator/data/brand-ai/audience-growth-across-platforms.md` is counted for brand-a (gi, calendar, envelope). It is a report, not a unit. The row allows "units or reports", so this is acceptable if intended.
