Verdict: FIX

The second check's findings are all resolved. The verdict is FIX because of two new should-fix findings that the earlier checks did not raise. First, Greece 5.3 has no relief, but it has a whole section on coinage. Second, the keyword scan only matches outlines against the courses listed for them in library.md, so it never looked for some objects in the other course. I can only see headings and keyword excerpts, not the full texts, so findings 1 and 2 are should-fix, not error.

Findings

1. **should-fix: Greece 5.3 (`m53`), no relief. Its coinage section seems to call for the coins outline.**
   - Evidence from mapping.md: the page has a heading "Coinage from Lydia" and names coins 9 times. That is more than Greece 7.1 (5), 11.7 (4) and 12.5 (7), which all have the coins relief.
   - The lines quoted treat the coins as objects: "Greek cities followed: Aegina's silver 'turtles' from about 550, Corinth's Pegasi, Athens' Wappenmünzen and, from about 515, the owls"; "no Greek coined before the mid-sixth century".
   - changes-2 removed the helmet for good reason, but did not test the page against the coins outline. The neighbour rule allows it, since 5.2 and 5.4 have no relief.
   - Fix: read the "Coinage from Lydia" section. If it describes the first coins at length (Lydian electrum, the turtles, the owls), give 5.3 the coins relief with a sentence from that section as its deciding sentence. Otherwise record why it gets none.

2. **should-fix: the keyword scan misses outlines that are not listed for a course.** Each outline's "courses" column in library.md limits which texts it is matched against. So no Rome page was checked against tablet or vase, and no Greece page against eagle. Some headings suggest a dedicated section on one of these objects:
   - **Rome 7.1 (`rm71`):** a section headed "The Lyon tablet", Claudius' speech on bronze. A bronze inscribed tablet is the kind of thing the tablet outline shows. Its neighbour 7.2 has the temple, so the tablet would be allowed.
   - **Rome 9.2 (`rm92`):** "The soldier's life: tablets and tombstones" (the writing tablets of the frontier). Its neighbours are 9.1 (scales) and 9.3 (none).
   - **Rome 1.6 (`rm16`):** a section headed "The Pyrgi tablets" (inscribed gold sheets).
   - **Rome 1.2 (`rm12`):** a section headed "Metals, princes and the vase trade". The lines quoted name the "Tyrrhenian" amphorae and Nikosthenes' amphorae made for the Etruscan market.
   - **Greece 2.4 (`m24`):** a section headed "The Prometheus cycle: Mekone, fire, the eagle, Heracles". The eagle outline is Rome-only, so this page was never matched against it.
   - Fix: add Rome to the tablet and vase rows and Greece to the eagle row, rerun the mapping for these pages, and decide each from its full text. A dedicated section that describes the object gets the relief, if the neighbour rule allows it; otherwise record the reason it gets none.

3. **minor: Greece 7.1 (`m71`), coins.** The new deciding sentence, "Almost all this chronology rests on coins.", is the right kind of sentence. But the paragraph round it turns straight to Tarn and Narain and never describes a coin, so this remains the thinnest coins page. Fix: if the text describes the Bactrian or Indo-Greek coin types anywhere, quote that paragraph.

4. **minor: Greece 5.5 (`m55`), ostrakon.** changes-2 keeps the relief because the text defines ostracism and dates its first use to 487 in a "Where sources disagree" paragraph. mapping.md still quotes only the tribes-and-demes paragraph, so the support cited is not on the record. Fix: quote the "Where sources disagree" paragraph in mapping.md.

5. **minor: library.md, courses column.** The libation row lists Greece, but no Greece page uses it. This only matters once finding 2 changes the columns: make sure they record which courses each outline is matched against, not which courses use it.

Second-report findings
1. Greece 2.2: resolved (no relief; lyre marked spare).
2. Greece 5.3: resolved (helmet removed; the round-shield rejection now names 5.3). A separate coins question is finding 1 above.
3. Greece 5.5: resolved by the reason given (see minor finding 4).
4. Greece 10.6: resolved (kept, as the check allowed).
5. Rome 3.3: resolved (the deciding sentence "The lasting answer was the wall." and its paragraph are about the wall).
6. Rome 8.1: resolved (the deciding sentence is on the temple of Sol of 274; the paragraph is about the Sun).
7. Rome 6.4 and Greece 7.1: resolved (Rome 6.4 now rests on the Kalkriese coin-dating dispute; Greece 7.1 is still thin, minor finding 3).
8. Rome 1.6: resolved for the dagger. Its Pyrgi tablets section is part of finding 2.
9. library.md stale notes: resolved (stone-tablet now names wax-tablet; the arena note says Rome 9.4 gets none).
10. Greece 3.1: resolved (no change needed; it is legible with its caption).

Neighbour rule and counts
- No two neighbouring reports of one unit share an outline. Rome 8.1 and 8.3 both use the sun, but 8.2 (coins) sits between them.
- Greece has 19 outlines in use: vase, bull, tablet, centaur, winged-sandal, hydra, minotaur, ram, wooden-horse, temple, ostrakon, trireme, wall, theatre-masks, coins, scroll, olive, greek-helmet, horse.
- Rome has 16: wolf, temple, bull, scales, wall, coins, trireme, horse, scroll, sun, eagle, dagger, wooden-horse, gladius, bough, libation.
- Both stay at ten or more.

What I checked
- check-1-report.md with changes-1.md, and check-2-report.md with changes-2.md, each finding against its change.
- All of mapping.md, Greece and Rome:
  - every relief page, for the fit of its deciding sentence and paragraph;
  - every page with none, for its headings and keyword lines.
- library.md: the outline table, its courses and spare notes, and the rejected list.
- Both contact sheets. Every outline in use reads as its caption. The winged sandal is the weakest; the coins read as two discs, one seen at an angle.
- Page shots:
  - Greece: m12 (1280 dark), m31 (390 light), m32 (1280 dark), m34 (390 dark), m55 (390 light), m71 (390 light, 1280 dark), m72 (390 light), m1010 (390 dark).
  - Rome: rm25 (390 light), rm31 (390 light), rm33 (390 light), rm55 (390 dark), rm81 (390 dark), rm117 (390 dark), rm125 (390 dark).
  - In each, the relief sits under the title and standfirst with its caption and CC BY 3.0 credit, readable in both themes. The sign captions say they are signs (scales, ostrakon).
- Pose shots: m71 at 1, rm81 at 0.5, rm117 at 0.5. All render cleanly.
- I used only Read, Glob and Grep, inside /home/claude/p96/check-h3, and wrote nothing.
