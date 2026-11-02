# P87, P88 · Dio pass (checker)

A separate fresh Opus 5.5 agent, 2 Nov 2026 (row A-1), shown only the proposals (`p87-p88-dio-inventory.md`'s changes, without its reasons); its report, verbatim.

# Checker report on proposals.md (Dio citations), 2 November 2026

The checker had not seen the drafter's work. No repository file was edited. Every URL below came back from a WebSearch made by this checker. The URLs are Bill Thayer's LacusCurtius pages of Cary's Loeb (penelope.uchicago.edu).

**Grep.** Every Current text in P1–P4 occurs exactly once on the line stated. The string "(Dio Cassius 72.31.3;" occurs twice in Greek 7.4, once on line 29 and once on line 150, and the proposal covers both.

**Numbering basis.** The source is the CQ article "The book indices in the manuscripts of Cassius Dio", n. 1 (https://scispace.com/pdf/the-book-indices-in-the-manuscripts-of-cassius-dio-22o5hi0bek.pdf). It says: "the 'traditional' book numbers will be placed in brackets ( ) after Boissevain's." On LacusCurtius, the Loeb heading number is Boissevain's, and the Roman numerals in the margin give the traditional book. So the proposal's convention, and its relabelling of the bracketed number as "traditional", are correct.

## P1 · Loeb 80
Source: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/80*.html. Headed "Vol. IX p437 Epitome of Book LXXX". The margin reads "LXXIX" before chapter 1 (Avitus), and chapters 1–21 follow. The chapters then restart at "1 1 Alexander became emperor immediately after him", which is traditional Book 80, chapters 1–5. In that run: 1.1 Ulpian is given the guard; 1.2–3 Dio says he was seldom in Rome; 2.2 the praetorians kill Ulpian at night; 3.2–4.1 Artaxerxes, "as far as the Grecian Sea"; 4.2 the praetorians complain of Dio's Pannonian discipline; 5.1 Dio spends his consulship outside Rome.

| file:line | current | proposed | verdict | reason |
|---|---|---|---|---|
| rome/7.4:96 | (80(80).1.1, 2.2) | (80.1.1, 2.2) | PASS | Loeb 80 = traditional 80 for this run; 1.1 and 2.2 as above |
| rome/7.4:96 | (80(80).4.2–5.1) | (80.4.2–5.1) | PASS | 4.2 and 5.1 |
| rome/7.4:98 | (80(80).3–4) | (80.3–4) | PASS | 3.2–4.1, fear of the armies at 4.1–2 |
| rome/7.4:122 | (80(80).1.2–3) | (80.1.2–3) | PASS | 1.2–3 |
| rome/7.4:166 | (Dio 80(80).3–4) | (Dio 80.3–4) | PASS | as line 98 |
| r-7.4:7 | 80(80).1.1; … 80(80).4.2–5.1. | 80.1.1; … 80.4.2–5.1. | PASS | as above |

Note: "80(80)" is the standard scholarly form (Scott's OUP commentary is titled "Books 79(78)–80(80)"), so it was not wrong. The change only applies the house rule of one number where the two agree.

## P2 · Loeb 75
The fetch was not refused. I reached the page from an extended WebSearch: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/75*.html. Headed "Vol. IX p161 Epitome of Book LXXV".

- The margin reads "LXXIV" before "Severus, on becoming emperor": 1.1 the praetorians are banished "from Rome"; 2.5 "ruined the youth of Italy"; 6–8 Niger; 10–14 Byzantium.
- The margin then reads "LXXV" before "Such were the walls of Byzantium", and sections 1–3 follow. The page ends with "a source of constant wars and great expense to us", which falls under 3, after "Severus again made three divisions".

So Loeb 75 = traditional 74 plus 75.1–3. The next page, Loeb 76 (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/76*.html), begins at 4.1, which confirms the split.

| file:line | current | proposed | verdict | reason |
|---|---|---|---|---|
| rome/7.4:36 | (75(75).1.1, 3.2–3) | (75.1.1, 3.2–3) | PASS | Loeb 75 holds traditional 75.1–3 |
| r-7.4:7 | 75(75).3.2–3; | 75.3.2–3; | PASS | same |

The nine "75(74)" citations are confirmed. Two asides need no change:
- Dio 75(74).1.1–2 says "banished them from Rome". The "hundredth milestone" detail on 7.4:34 must rest on Herodian 2.13, which the same parenthesis cites.
- The Euphrates crossing is at 75.2.1, not 1.1. The 1.1 passage has the campaign against the Osroeni, Adiabeni and Arabians.

## P3 · Single numbers that give the traditional book
Sources:
- Loeb 72 (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/72%2A.html): margin "LXXI" directly under the heading; 31.3 salaried teachers at Athens.
- Loeb 76 (as above): 13.2 Severus "locked up the tomb of Alexander".
- Loeb 78 (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/78%2A.html): starts at 1.1, "After this Antoninus assumed the entire power", which is traditional 77; 7.1 the phalanx of 16,000; 7.3 the Aristotelians and Alexander's death.
- Loeb 61 (https://penelope.uchicago.edu/Thayer/e/roman/texts/cassius_dio/61*.html): margin "LX" before chapter 29; 31.2 Messalina "caused his [Polybius'] death"; 35.3 "Pumpkinification". Then margin "LXI".
- Loeb 62 (https://penelope.uchicago.edu/thayer/e/roman/texts/cassius_dio/62*.html): starts at 11.2 under the margin "LXI"; 12.1 "He was incited likewise by Seneca". Then margins "LXII" and "LXIII"; under LXIII, 17.5–6 Corbulo at Cenchreae.
- Loeb 63 (https://penelope.uchicago.edu/Thayer/e/roman/texts/cassius_dio/63*.html): starts at 22.1 and has no chapter 17, so the current "63.17.5–6" is wrong.
- Loeb 60 (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/60%2A.html): headed "Book LX", not an epitome. It ends at 28.7.

| file:line | current | proposed | verdict | reason |
|---|---|---|---|---|
| greece/11.8:90 | (Dio 76.13.2) | (Dio 76(75).13.2) | PASS | Loeb 76.13.2 = traditional 75.13.2 |
| greece/11.8:121 | (Dio 78.7–9; | (Dio 78(77).7–9; | PASS | Loeb 78 = traditional 77. Note: the phalanx and the Aristotelians are both in ch. 7; chs 8–9 are only general Alexander-imitation. Optional tightening: (Dio 78(77).7; |
| greece/7.4:29 | (Dio Cassius 72.31.3; | (Dio Cassius 72(71).31.3; | PASS | margin LXXI, 31.3 |
| greece/7.4:150 | (Dio Cassius 72.31.3; | (Dio Cassius 72(71).31.3; | PASS | same |
| greece r-7.4:11 | 69.16; 72.31.3. | 69.16; 72(71).31.3. | PASS | same |
| greece r-11.8:13 | 68.29–30; 76.13.2; 78.7–9. | 68.29–30; 76(75).13.2; 78(77).7–9. | PASS | as above (same optional tightening of 78(77).7) |
| rome/13.5:32 | put to death (60.31.2) | put to death (61(60).31.2) | PASS | Loeb 61, under LX, 31.2 |
| rome/13.5:46 | urged the murder (61.12.1) | urged the murder (62(61).12.1) | PASS | Loeb 62, under LXI, 12.1 |
| rome r-13.5:8 | from 60.29 on | from 61(60).29 on | FIX | See below |
| rome r-13.5:8 | 60.31.2 (Messalina | 61(60).31.2 (Messalina | PASS | as 13.5:32 |
| rome r-13.5:8 | 61.12.1 (Seneca said | 62(61).12.1 (Seneca said | PASS | as 13.5:46 |
| rome/7.1:107 | (60.35.3) | (61(60).35.3) | PASS | Loeb 61, under LX, 35.3 |
| rome r-7.1:7 | 60.35.3 (the | 61(60).35.3 (the | PASS | same |
| rome/7.1:133 | (Dio 63.17.5–6) | (Dio 62(63).17.5–6) | PASS | Loeb 62, under LXIII, 17.5–6 |
| rome r-7.1:7 | 62.16–18; 63.17.5–6. | 62.16–18; 62(63).17.5–6. | PASS | same |

**Why r-13.5:8 needs a fix.** The number change is right. But the clause it sits in reads "(Loeb book numbers; books 60–62 survive only in Byzantine epitome …". In Loeb terms, Book 60 is full text: it ends at 28.7, and the epitome starts in Loeb 61. The clause also does not explain the brackets the file will now contain. Replace the whole clause:
- Current (once): `(Loeb book numbers; books 60–62 survive only in Byzantine epitome from 60.29 on)`
- Replacement: `(Loeb book numbers, with the traditional number in brackets where the two differ; Dio survives only in Byzantine epitome from 61(60).29 on)`

Two asides need no change:
- On 7.1:133, Cary renders Corbulo's word as "Your due!", and his note glosses it "Thou art worthy". "Said only that he deserved it" is an interpretation of that word.
- On 7.4:96, Loeb 80.2.2 says Ulpian took refuge with the emperor and his mother, "but it availed him naught". "Before the emperor and his mother" is slightly stronger than the text.

## P4 · Labels
All of these are supported by the numbering basis above. Loeb 65 (https://penelope.uchicago.edu/thayer/e/roman/texts/cassius_dio/65%2A.html) has the margin "LXVI" before ch. 1, with 12.1 Helvidius and 13.2 the expulsion except Musonius. Loeb 67 (https://penelope.uchicago.edu/thayer/e/roman/texts/cassius_dio/67*.html) starts at 1.1 with no margin numeral and has 13.2 Senecio, so Loeb 67 = traditional 67. Loeb 77 (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/77*.html) starts at 1.1 with the decennalia, so it is traditional 76; Bulla is at 10.1.

| file:line | current | proposed | verdict | reason |
|---|---|---|---|---|
| rome/7.3:14 | with Boissevain's in brackets where they differ | with the traditional book number, printed in the Loeb's margin, in brackets where they differ | PASS | CQ n. 1; LacusCurtius margins |
| rome/7.4:14 | with Boissevain's in brackets, since the two editions number these books differently | (proposed) with the traditional book number, printed in the Loeb's margin, in brackets, since the two numberings differ in these books | FIX | After P1 and P2, 7.4 cites Books 75 and 80 with one number, so "since the two numberings differ in these books" is no longer true of every book. Apply instead: `with the traditional book number, printed in the Loeb's margin, in brackets where the two differ` |
| rome/13.7:16 | with Boissevain's in brackets (72(71).34) | with the traditional number from the Loeb's margin in brackets (72(71).34) | PASS | Loeb 72 has the margin LXXI |
| r-7.3:8 | with Boissevain's in brackets where they differ | with the traditional (margin) number in brackets where they differ | PASS | |
| r-7.4:7 | with Boissevain's in brackets where the two differ | with the traditional (margin) number in brackets where the two differ | PASS | |
| r-7.5:6 | Loeb book 77, Boissevain 76, | Loeb book 77, traditional 76, | PASS | Loeb 77 = traditional 76; Bulla 10.1 |
| r-13.3:23 | (Loeb numbering, Boissevain's in brackets; | (Loeb numbering, the traditional margin number in brackets; | PASS | |
| r-13.4:10 | Loeb book numbers with Boissevain's in brackets (Loeb number not verified). | Loeb book numbers with the traditional (margin) number in brackets. | PASS | Dropping "not verified" is justified: Loeb 65.12, 65.13 (margin LXVI) and 67.13.2 are confirmed |
| r-13.6:8 | (Loeb 65.13.2, Boissevain 66.13: | (Loeb 65.13.2, traditional 66.13: | PASS | |
| r-13.7:3 | Dio is cited by the Loeb book numbers with Boissevain's in brackets; | Dio is cited by the Loeb book numbers with the traditional (margin) number in brackets; | PASS | |

A caution on "printed in the Loeb's margin": LacusCurtius shows a margin numeral for Loeb 61, 62, 65, 72, 75, 76 and 80. Its Loeb 77 and 78 pages show none, although each begins afresh at ch. 1 of the traditional book. The wording is acceptable as a general description.

## P5
**Q1. 72(71).33 is right; no change.** On Loeb 72 (URL as above), the first block numbered "33" has Crispina, the senate's money and, at 33.3, the bloody spear from the temple of Bellona. A second block, also printed "33" ("Now if Marcus had lived longer…"), has "he passed away on the seventeenth of March, not as a result of the disease … but by the act of his physicians". LacusCurtius prints no section number for that block. "Go to the rising sun; I am already setting" is at ch. 34, together with the age and reign that follow it; 13.7:112 already cites 72(71).34 for both. So all of these are right as they stand:
- 7.3:99 (death)
- 13.7:112 (spear, then death)
- 13.7:114 (physicians)
- 13.7:128 (expedition and death)
- 13.7:172 (physicians)
- r-7.3:8
- r-13.7:9

**Q2. 77(76).17.4 does not name Lepcis.** Loeb 77.17.4 gives only his lifespan (65 years, 9 months, 25 days), his reign and "he was born on the eleventh of April". I searched the Loeb 73, 75, 76, 77 and 78 pages for Lepcis, Leptis, Africa and Libya, and none gives Severus' birthplace. Loeb 78's "Antoninus belonged to three races" names Africa for Caracalla, not Lepcis. The Loeb 74 page refused the fetch (robots), so Book 74 is not checked.

The city is given by *Historia Augusta*, *Severus* 1.2: "His native city was Leptis" (Magie's Loeb, https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Historia_Augusta/Septimius_Severus*.html). The bibliography r-7.4 already lists it, and 77(76).17.4 stays there for the date.
- File: courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:32
- Current (once in the file): `(Dio 77(76).17.4)`
- Replacement: `(the city, *Historia Augusta*, *Severus* 1.2; the day, Dio 77(76).17.4)`

## Counts
- P1–P4: 33 items checked. 31 PASS, 2 FIX (r-13.5:8 "from 60.29 on" clause; rome/7.4:14 wording), 0 NOT CHECKED.
- P5: Q1 current citation right (no change); Q2 one FIX (7.4:32).
- One fetch refused: the Loeb 74 page. No proposal depended on it.

## Follow-ups for the caller
1. Rome 7.1, Rome 13.5, Greek 7.4 and Greek 11.8 would gain bracketed forms such as 61(60) and 72(71), but none of them has a sentence explaining the convention. Grep finds no "Loeb" or "Boissevain" in any of the four.
2. kit/bibliography/*/unit-*.md and kit/academy/*.html also contain the old forms. They are regenerated by build.py and biblio.py, so they need a rebuild, not an edit.
