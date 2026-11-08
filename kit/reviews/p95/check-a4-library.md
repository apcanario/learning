Verdict: FIX

I read everything in p95-checkA4/: README.md, outlines.json (48 outlines and 21 rejections), grep-lines.md, relief-measures.md, the three licence files, previous-report.md, changes.md and both contact sheets. I also grepped all 48 SVGs and opened sitemap.svg and bridge.svg. One should-fix (centurion-helmet) holds the verdict at FIX; everything else is minor.

## Earlier findings: status

1. **theatre-masks (should-fix): resolved.**
   - `texts.greece` is now 6.4 (count 4) and 2.2 (count 1).
   - The grep lines are 2.2:183 "the mask and the theatre" and 6.4:16, 20 and 26 (grep-lines.md:118–121). All four name theatre masks.
   - 9.2, 9.3 and 7.3 are gone, and so is the 2.2 cult mask.
2. **bridge (should-fix): resolved.**
   - `texts.rome` is 8.3, 0.3, 10.5, 7.3, 8.2 and 9.2. Every line is the Milvian Bridge, except 7.3:30, which is Trajan's Danube bridge (grep-lines.md:213–219).
   - 0.2, 1.6 and 4.2 are gone, and "Boarding-Bridge" is in `excludes`.
   - changes.md is now accurate.
3. **receipt (minor): resolved.** "banked receipts" and "from receipt" are excluded. The brand-a lines left are recibos, invoices and "the first invoice" (grep-lines.md:348–352).
4. **laurels (minor): resolved in outlines.json, but the contact sheet is stale.** See minor finding 2.
5. **owl (minor): settled, and the reason is sound.** The 5.3 Athenian coins carry the owl, and the caption claims only "an owl".
6. **Non-prose (minor): partly resolved; the settlement is mostly sound.**
   - Done: the bare URL is gone (no help.instagram line under phone), and "Two Waves Books" is excluded.
   - Bibliography titles are settled on "no outline's place rests on them". That holds for each outline, but one file entry rests only on a title. See minor finding 3.
7. **"about" (minor): resolved.** It now lists the front matter, figure declarations, link targets, URLs and every sentence that holds an exclude.

## New findings

### Should-fix

1. **should-fix · centurion-helmet (rome): the keyword "centurion" names a rank, not the helmet, and the caption does not say so.**
   - **Evidence:**
     - grep-lines.md:163 (10.4:78): "*Rome* (HBO and BBC) followed two centurions", a TV series' soldiers.
     - grep-lines.md:164 (11.2:47): "Octavian's centurions went to the Senate".
     - grep-lines.md:165 (11.2:51): "every centurion offered to equip a horseman".
     - None of these names a helmet. The README's criterion 3 asks that a sign-for keyword be honest in the caption. The caption is "a crested Roman helmet", with no "(the sign for …)".
   - **A second problem:** the helmet lines in 1.1 (1.1:12, 16, 112, grep-lines.md:158–160) are Villanovan and Iron Age crested helmets from before Rome, so "Roman" is wrong on that page. The same goes for the Etruscan helmet at 1.2:119.
   - **Fix, either:**
     - drop "centurion" and "centurions" from `keywords` and re-run the count (helmet files such as 1.1, 1.2, 1.5 and 12.3 still carry it); or
     - make depicts "a crested helmet (the sign for a centurion)".
   - In either case, drop "Roman" or keep the pre-Roman files out.
   - Rome keeps 11 outlines either way.

### Minor

1. **minor · terminal (brand-b): the whole-sentence exclude breaks on decimals.**
   - grep-lines.md:414 (B2:159) reads "…against Sonnet 5. .0, long agentic terminal tasks…". The splitter cut the sentence at "5.5" and "2.0", removed only the fragment holding "Terminal-Bench", and left "terminal tasks" from the same benchmark sentence counted.
   - This contradicts changes.md, which says the whole sentence goes.
   - **Fix:** don't split sentences on a period between digits (nor after "c." or "no."), and re-run every count.
   - Terminal still stands on B5, B8 and DD-B1. Other excludes may have left fragments the same way; 8.3:16's ". ." (grep-lines.md:217) shows the cut, and there it was clean.
2. **minor · laurels: the contact sheets were not regenerated after the depicts change.**
   - Both sheets still print "laurels · a laurel wreath". outlines.json says "laurel (a wreath)".
   - **Fix:** rebuild the sheets, and confirm the reading pages' captions come from the current JSON.
3. **minor · phone (brand-a): the A2 entry rests only on a source title.**
   - A2's count is 1, and its only line is A2:249, the Pew title "…phones are common…" (grep-lines.md:298).
   - Other entries also count titles, but each of those files has prose that names the object too:
     - minotaur 1.1:78, MacGillivray's *Minotaur* (2000), a book title
     - toga 10.5:213, Cicero's *In toga candida*, a speech title
     - calendar B4:191, "Google Calendar", a product name
   - **Fix:** drop A2 from `texts.brand-a` for phone, or exclude bibliography-entry lines.
4. **minor · map (ux-ia): the verb "map" is counted.**
   - IA3:248 "the Help centre's search does not map them" (grep-lines.md:548) escapes the exclude `maps? (?:to|onto|into)`. It is very likely IA3's single counted map hit.
   - **Fix:** add "map them" or a broader verb exclude. Map stands on 134 other hits.
5. **minor · olive: the same kind of issue as laurels.**
   - depicts is "an olive branch", but the texts name the tree and the crop as well:
     - 10.7:160, the bed built round an olive trunk
     - 10.5:74, an uprooted sapling
     - 0.2:35 and 0.2:118, olives as a crop
   - For consistency with laurels: depicts "olive (a branch)".
6. **minor · grep-lines.md header is out of date.** Line 3 says only "figure declarations and the outline's excludes taken out". It should match the updated "about".
7. **minor · busy reliefs: the sheets cannot settle two cases.**
   - At the sheets' resolution, the ionic-column volutes (step 3.22 px), the laurels and the centurion-helmet crest look near-solid in the light sheet. The dark sheet shows separate lines.
   - The measures pass the rule: 0 thin parts, regions ≤13, and every step ≥3.02 px.
   - Worth one look at full size on a phone-width reading page before publishing. Not a rejection on current evidence.

## Checks that pass

- **Licences and credits:**
  - game-icons: Delapouite, Lorc and Skoll are listed in license.txt, and none is marked CC0. Every credit has the row's form, "Icon: <author>, game-icons.net, CC BY 3.0", and `licence_url` is the CC BY 3.0 deed.
  - MIT sets: the credits name the copyright holders, "Phosphor Icons" (licence-phosphor-icons_core.txt:5) and "Paweł Kuna" (licence-tabler_tabler-icons.txt:5).
  - No outline is a logo, a brand mark or a recognisable character.
- **Sources:**
  - Every outline has its repository, path, commit and url.
  - The commits match the licence files: 82d9488…, 2b75f3a… and 58f6053….
  - `background_removed` is true for game-icons and false for Phosphor and Tabler.
  - The game-icons SVGs are one white-filled path, and the Phosphor ones one path with currentColor.
  - sitemap.svg is the Tabler file as published: its version comment and four filled paths.
  - No SVG has a rect, g, transform, stroke, image or text.
  - All are filled variants.
- **Captions:** "<depicts>, a stylised outline drawn as a relief from an icon. <credit>." reads correctly for every depicts value, including "laurel (a wreath)".
- **Rejections:** the reasons are true and rule-based.
  - Thin parts: aqueduct, roman-shield, sundial, ruins, spartan-helmet, sphinx, chariot and barn-owl.
  - 45 regions: coins.
  - A step under 3 px: maze, ancient-columns and black-belt.
  - Not the object, with stated reasons: the rest.
- **Course counts:**

| Course | Outlines | Fit after the findings above |
|---|---|---|
| greece | 12 | 12 |
| rome | 11 | 11 |
| brand-a | 10 | 10 (no margin) |
| brand-b | 12 | 12 |
| ux-ia | 15 | 15 |

  No finding removes an outline. Each one corrects texts, a keyword or a caption.

Nothing for memory.
