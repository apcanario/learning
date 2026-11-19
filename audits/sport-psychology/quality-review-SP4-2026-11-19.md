---
audit: quality review
unit: SP4 · Anxiety, arousal and performing under pressure
course: sport-psychology
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgR2iBxJPhjunwizCmdb
verdict: fix · 0 error, 6 should-fix, 4 minor (applied below)
---

The reviewer's final report, verbatim, from its hand-back. Saved before any finding was applied.

Model: claude-opus-5-5. I could not write the report to /tmp/sp10/qr-SP4/out/report.md: the tool refused the write ("Subagents should return findings as text"), so the full report is below. Save it there verbatim.
Verdict: SP4 · fix · 0 error, 6 should-fix, 4 minor

References: 28 opened (27 Sources entries plus Lochbaum & Lane 2025), 2 not opened (Smith, Smoll & Cumming 2007; Cox et al. 2003, seen only through a summary page).
Not checked (refused or blocked, not retried): PMC, scalda.mijn.bsl.nl, unimelb, x-mol.

---

Model: claude-opus-5-5. Quality review of SP4 (docs/public-courses.md section 3 rule 13; flag F147), 19 Nov 2026. Packet files only, plus live search; nothing edited, nothing published.

Verdict: SP4 · fix · 0 error, 6 should-fix, 4 minor

(Audit-units section 3 calls a unit with no errors "keep". I recorded "fix" because six should-fix edits are to be applied, as earlier SP quality reviews did with 0 errors. One should-fix is [cross-unit] and has no Fix.)

## Findings

[should-fix] [accuracy] §2, "What follows for a coach" grade; Current: "a second meta-analysis, read in abstract, calls the relationships weak); moderate, positive"; Problem: F60. The 2025 scoping review says of the anxiety meta-analyses it maps: "Three of the meta-analyses suggest a negligible or unreliable relationship with performance". The one exception is Jokela & Hanin; Woodman & Hardy and Craft et al. are among the four mapped. The unit does not tell the reader that a later review reads the same evidence as negligible or unreliable. The two agree on direction, not on size. The grade can stay [moderate] (one meta-analysis of small studies), but the disagreement must be stated; Fix: "a second meta-analysis, read in abstract, calls the relationships weak; a 2025 scoping review of sport psychology meta-analyses says that three of the anxiety meta-analyses it maps \"suggest a negligible or unreliable relationship with performance\" ([Lochbaum & Lane, 2025](https://doi.org/10.3390/sports13120420)), so the size of this association is uncertain); moderate, positive"; Basis: Lochbaum & Lane (2025), Sports 13(12):420, https://mdpi.com/3615528 (first part of the full text read)

[should-fix] [bibliography] Sources, new entry for the previous finding; Current: "- Lochbaum M, Sherburn M, Sisneros C,"; Problem: the added source needs a Sources entry with its log note; Fix: "- Lochbaum M, Lane AM. Mapping 50 years of sport psychology–performance meta-analyses: A PRISMA-ScR scoping review. *Sports* 2025;13(12):420. https://doi.org/10.3390/sports13120420 (first part of the full text read at the publisher's page, https://mdpi.com/3615528, on 19 Nov 2026 by the quality reviewer; its table of effect sizes was not in the part read)\n- Lochbaum M, Sherburn M, Sisneros C,"; Basis: https://mdpi.com/3615528

[should-fix] [bibliography] Sources, Smoll et al. (2007); Current: "*Journal of Youth Development* 2007;2(1):article 0701FA002. https://doi.org/10.5195/jyd.2007.358 (full text read at the publisher's page, https://jyd.pitt.edu/ojs/jyd/article/view/358/344, which shows no DOI: the DOI is not verified)"; Problem: the publisher's landing page gives pages 19–36 and DOI 10.5195/jyd.2007.358. The entry gives an article number instead of pages and marks a confirmed DOI as unverified; Fix: "*Journal of Youth Development* 2007;2(1):19–36. https://doi.org/10.5195/jyd.2007.358 (full text read at the publisher's page, https://jyd.pitt.edu/ojs/jyd/article/view/358/344; pages and DOI from the article's landing page, https://jyd.pitt.edu/ojs/jyd/article/view/358, read 19 Nov 2026 by the quality reviewer)"; Basis: https://jyd.pitt.edu/ojs/jyd/article/view/358

[should-fix] [label] §9, "Questionnaires you may hear of"; Current: "published in the same journal, 2003, 25, 519 to 533: [Cox et al., 2003](https://doi.org/10.1123/jsep.25.4.519))"; Problem: the source log says the paper was not read (ScienceGate showed only the title). The 17-item count comes from a San Diego State University summary page, but the text cites the paper as if it had been opened (Part 7); Fix: "published in the same journal, 2003, 25, 519 to 533: [Cox et al., 2003](https://doi.org/10.1123/jsep.25.4.519); the paper itself was not opened, and the item count is from a university summary page)"; Basis: https://coachsci.sdsu.edu:443/csa/vol125/cox.htm ("Further factor analysis resulted in a 17-item form")

[should-fix] [population] §6 table, band 19 to 25; Current: "The IOC statement reports generalised anxiety disorder in elite athletes at 6.0%"; Problem: the GAD prevalence covers elite athletes in general, not this age band, so in the 19–25 row it reads as a figure for that band; Fix: "The IOC statement reports, for elite athletes of all ages in the studies it reviews (not this band alone), generalised anxiety disorder at 6.0%"; Basis: Reardon et al. (2019) p. 672, https://www.psychiatry.wisc.edu/wp-content/uploads/2023/10/2019-Mental-health-in-elite-athletes-International-Olympic-Committee-consensus-statement-2019.pdf

[should-fix] [accuracy] §7 "Just relax" bullet and Deliverable A "What I do before"; Current: "and graded the practised what-to-do cue that replaces them [practice, as SP1 grades it]"; Problem: [cross-unit] F59. SP5 grades a planned self-talk phrase [weak, mixed] and instructional self-talk [weak, positive]. SP4 still grades the cue [practice], here and at "Replace \"just relax\" with one practised cue that says what to do [practice, as SP1 grades it]". The regrade needs SP5's sources, which are not in this packet and which I did not open, and must be made in SP1 at the same time. No Fix; Basis: syllabus-flags.md F59

[minor] [population] §5 table, distraction "Evidence for it"; Current: "70 expert athletes asked about their focus"; Problem: the sample's ages and sports are not stated, and the abstract does not give them; Fix: "70 expert athletes (ages and sports not given in the abstract) asked about their focus"; Basis: https://informahealthcare.com/doi/full/10.1080/10615806.2010.481331

[minor] [figure] §5, Gröpel & Mesagno; Current: "32% with trained novices"; Problem: the review says "12 studies (32%)", but 12 of 47 is 26%, so the source contradicts itself; Fix: "12 studies with trained novices (the review gives this as 32%; 12 of 47 is 26%)"; Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134

[minor] [accuracy] §3, Duncan et al.; Current: "the authors read this as partial support for a catastrophe model"; Problem: the manuscript's discussion calls the support partial, but its conclusion calls it strong; Fix: "the authors' discussion reads this as partial support for a catastrophe model (their conclusion calls the support strong)"; Basis: https://e-space.mmu.ac.uk/620537/8/4034137.pdf

[minor] [accuracy] §7, "Emotion regulation from 16 to 25"; Current: "both reappraisal and suppression rose over the year, and the authors suggest the change reflects new demands, such as starting upper secondary school, more than age alone"; Problem: the source says the changes are "likely to be influenced by environmental factors, rather than age", tied to "increased demands during upper secondary sport education". It also warns that the rise in suppression "should be interpreted with caution". The unit's wording is softer and leaves out the warning; Fix: "both reappraisal and suppression rose over the year (the rise in suppression, the authors say, \"should be interpreted with caution\"), and the authors attribute the change to environmental factors, such as the demands of upper secondary sport education, \"rather than age\""; Basis: https://www.mdpi.com/2075-4663/13/9/284

A script confirmed that each Current string occurs exactly once in the unit.

## Fresh check (audit-units §3)

(1) Coverage: every brief item is covered, in order (§1–§9). Reassurance is thin, and the unit says honestly that no source was opened for it. All "Gives" items are present: the profile, the normal-or-refer table, and the attention account for DD-SP3.
(2) Accuracy: no FAIL. The fixes above are wording, labels and the F60 caveat.
(3) Whose figure: PASS, except the Gröpel percentage and the band placement of the Reardon prevalence (above).
(4) Labels: PASS, except Cox (above).
(5) Deliverable: PASS. Both tools are built in full on Milan, both templates are given, and every blank says what goes in it.
(6) Errata: the earlier fresh-check and QR reports are not in the packet, so I could not check them. Cross-unit pointers could not be opened.
(7) Figures:
- Fig 1, range, §2: PASS. Every value is in §2, the caption names both sources and the section, and it says "association, not cause". The opening-frame width stays under F40.
- Fig 2, flow, §7: PASS. Every label traces to §7, §1 or §10, and the caption marks the sport examples as illustrations.
- Fig 3, decision, §8/B: PASS. Each question traces to rows 9–10, 6, 7, and 5/8, and the caption says the order is the unit's own, graded practice.

## Seven passes

Claims: FIX. Every cited claim was opened except Smith 2007 (no claim rests on it) and the Cox paper (summary page only). None fails; the wording fixes and the F60 caveat are above.

Bibliography: FIX. Checked field by field (record used in brackets):
- Woodman & Hardy (PubMed)
- Lochbaum 2022 (MDPI)
- Gómez-López (RePEc and full text)
- Hase 2025 (EXCLI)
- Hase 2019, Grossbard, Smith 2006, O'Rourke (Bath)
- Sagar (Stirling)
- Hill (Portsmouth)
- Fröjdö Regborn (MDPI)
- Robazza, Wergin, Vine (Frontiers)
- Gouttebarge (McMaster, 55(1):30–37)
- Gröpel (VU, 12(1):176–201)
- Oudejans (VU, 24:59–73)
- Rosebrock (BL, 50(3):257–268)
- Duncan (16(1):27–35)
- Arent (DVS, 74(4):436–444)
- Craft (25(1):44–65)
- Reardon (53:667–699)

Smoll needs the fix above. Not verified: Iniesta pages and author order, Roberts volume and pages, the Arent DOI, the Cox issue. No reference turned out not to exist.

Source log: FIX. Every Sources entry is cited in the text, and abstract-only reading is marked at first use, except Cox. Lochbaum & Lane needs an entry if the F60 fix is applied.

Grades: PASS. The grades follow the key as the preamble summarises it, including the F14 practice convention. F59 is the one grade that lags SP5.

Population: FIX. Samples and designs are stated for every study and inferences are labelled. The gaps are Oudejans (minor) and the Reardon prevalence row (should-fix).

Scope and safety: PASS. The unit is recognition only. It gives no weight figure and no self-harm method, puts legal duties as questions, carries an information-not-advice line, and names no real person.

Any sport: PASS. Outside the Milan deliverable the brief requires, there are 16 examples across 12 sports: athletics 3, football 2, judo 2, and one each for rowing, gymnastics, volleyball, shooting, tennis, figure skating, basketball, swimming and handball. None is above a third.

## Part 7 line by line

Every line passes, with these exceptions:
- Source log: Cox (above).
- Sources against publisher or Crossref: Smoll fails (fix above); Iniesta, Roberts, the Arent DOI and the Cox issue are unverified.
- Sample and design: the two gaps above.
- Issuing body's page: the ISSF page is not the IOC's own page (known, F54/F130).
- Links: Arent and ISSF are not DOI links (no DOI was found for Arent).
- Private terms: no owner terms are visible in the unit, but kit/private_terms.py is not in the packet, so I did not run it.

## Read as the coach

Usable. §8 and Table B give a clear line, graded, with no waiting for clinical durations. The Milan profile stands on its own. The dense grade parentheses in §2 and §4 slow reading on a phone.

## Case facts

All consistent with case-facts.md, including SP4's own added facts and those added by SP1, SP2, SP6, SP8 and SP9. One nuance: SP9 records that whether Sara's symptoms spread beyond competition "has not yet been asked", while SP4 says row 6 is met. SP4's reading rests on her five hours of sleep on ordinary nights, which is in the base entry, so the two are compatible.

## Confirmed (one per source; URLs as above)

- Woodman & Hardy: k=48, r −0.10 / 0.24, gender and standard splits (PubMed 12846532).
- Craft: "appeared weak", confidence the strongest relationship (ScienceGate).
- Lochbaum 2022: every figure in §2, including I²=64.49, the quotation on ages, and "overstated" (mdpi.com/1660-4601/19/11/6381).
- Arent & Landers: 104 participants, 20–90% HRR, 13.2% of variance, best at 60–70%, SAS somatic anxiety (sponet).
- Duncan: 18 participants, mean age 23.6, the 70/90% findings, no hysteresis (e-space.mmu).
- Vine: stress definition, BPSM, cardiac output and TPR, ACT, EMH and reinvestment named, quiet eye (Frontiers PDF).
- Hase 2019: 38 studies, the quotation (Bath).
- Hase 2025: every figure and the quotation (excli.de XML).
- Hill: the choking definition.
- Oudejans: 70 athletes, the distraction finding.
- Roberts: dual-task, gaze and paced claims.
- Gröpel: every figure except 32%.
- Wergin: single-task versus multi-task, continuous choking.
- Grossbard: 1,038 athletes aged 9–14 and the findings.
- Smith 2006: 5-item subscales, grade-4 reading level, ages 9–10.
- Sagar: nine athletes aged 14–17 and the themes.
- Gómez-López: 479 players aged 16–17 and the β values (core.ac.uk full text).
- O'Rourke: the swimmers findings.
- Iniesta: the quotation and the under-19 age limit.
- Fröjdö Regborn: 93 athletes aged 15–17, the coach-style findings, GHQ-12, "causality cannot be inferred".
- Robazza: 424 athletes aged 16–36, 71% regional, the quotation, age not analysed.
- Rosebrock: the safety-seeking model and the samples.
- Smoll: workshops, SAS-2 means, design, "more recent study" (JSEP 29, 38–58).
- Reardon: every quotation in §1, §6, §7, §8 and Table B, including the Table 4 social anxiety and panic rows on the university copy.
- Gouttebarge: SMHAT-1 users, age 16 and over, screening; SMHRT-1 "for athletes and their entourage".
- ISSF: the five red flags, recognise not diagnose, the copy permission, © 2025.
- Cox: 17 items (SDSU page).

## Flags naming SP4

- F7, F24, F38: dealt with (the source log records the addresses used).
- F8: dealt with.
- F9: dealt with; SP9's lines are correctly still open.
- F14, F47, F48: carried, correctly open.
- F19: dealt with.
- F26: dealt with.
- F33, F57: still open, correctly. The paper was not opened and nothing rests on it. Smoll et al.'s 38–58 is confirmed; the seed list's 39–59 is unsettled.
- F40: still open (kit decision).
- F53, F129: still open. The table rows match on the university copy; the publisher's page was not reached.
- F54, F130: still open, for SP9.
- F59: not dealt with (should-fix above, cross-unit).
- F60: not dealt with in the unit; this review read the scoping review and the fix is above.
- F88, F96: consistent.
- F128: still open pending the syllabus review.
- F147: worked by this review.

## Could not verify

- Smith, Smoll & Cumming 2007: not opened (no publisher page found, PubMed reCAPTCHA); pages and design unknown.
- Cox 2003: the paper itself, and its issue number.
- Iniesta-Sepúlveda 2021: pages and author order (the UCAM repository's order differs; the BSL page needs JavaScript).
- Roberts 2019: volume and pages (no citation on the publisher page; Melbourne and X-MOL pages bot-blocked).
- Arent 2003: no DOI found.
- Reardon 2019: the publisher's page and the issue number (university copy only).
- Lochbaum 2022: the PMC copy was refused; MDPI was used instead.
- Lochbaum & Lane 2025: which three meta-analyses it means is in Table 8, which I did not read.
- SP1, SP2, SP3 and SP5 pointers: those units are not in the packet.
- The earlier SP4 check reports: not in the packet.
- kit/private_terms.py: not in the packet, so not run.
