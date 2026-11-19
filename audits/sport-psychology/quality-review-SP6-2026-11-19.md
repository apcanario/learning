---
code: SP6
kind: quality-review (rule 13)
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgQzDra5WhwrnjTVBqy8
note: report returned as the agent reply (harness blocked its file write) and saved verbatim by the chat
---
Verdict: SP6 · fix · 1 error, 5 should-fix, 5 minor
Model: claude-opus-5-5

The harness refused the write to out/report.md, so the whole report follows. This is a quality review (rule 13) of SP6, dated 19 Nov 2026, run with live search. Every fetch was of a URL that a search in this agent returned verbatim. The unit was not edited, and no memory or project context was used.

## 1. Claims: FIX
I opened the source behind every cited claim; the addresses are listed under Confirmed. All the claims hold except one. Section 3's table says forfeits in the pooled studies were "always combined with other stressors". Table 1 of Low et al. (2021) codes each of its 4 forfeit studies with a forfeit only (E1). The full text of the choking-interventions review is now open at the publisher's page. It confirms the sample details the unit took from SP4's reading, and it gives per-technique counts that the unit says were "not seen".

## 2. Bibliography: PASS (one field unverified)
I checked all 13 entries field by field against a publisher, PMC, university repository, journal-page or issue-listing record. All match, and every reference exists. One field is unsettled: the author order of Low et al. (2021). The Heriot-Watt and LJMU records and the manuscript put Sandercock second; the Essex record puts Freeman second. The APA record was not reached, so F81 stays open.

## 3. Source log: FIX
- Claims that rest on an abstract alone say so (Oudejans & Pijpers; Stoker 2016; Soligard; Gröpel & Mesagno).
- Every Sources entry is cited in the text.
- Section 6 cites full-text figures "from SP4's reading, not re-read for this unit". That breaks Part 1's rule on citing a reporter for the source's claim. The figures are true; the fix is to cite them from the full text.

## 4. Grades: PASS, with should-fix items
- Pressure training [moderate]: holds under rule 4.
- Routines [moderate]: holds under rule 4.
- Debrief [weak]: holds under rule 5.
- Coping skills [weak]: holds under rule 5.
- Consequences and judgement [weak]: holds under rule 5, but the basis is two studies, and the unit names one.
- Section 6 rows say "count not seen". The full text gives the counts: quiet eye 7, left-hand contractions 5, dual and task-irrelevant cues 9, analogy and implicit learning 7.
- No technique is graded strong, as F64 requires.

## 5. Population: PASS
Every finding names its sample and design. Transfers to under-18s are labelled inference, and transfers to 19 to 25 and to 10-year-olds are labelled "outside the sampled ages", per F77.

## 6. Scope and safety: PASS
- Nothing teaches assessment, diagnosis or treatment. Exposure is called a clinician's treatment, and distress is routed to SP4's table and the scope card.
- There is no weight method, calorie figure or target weight; rule 8 keeps weight, food and the body out of the drills.
- Nothing describes self-harm, no law is stated, the disclaimer is present, and no real person is named.

## 7. Any sport: PASS
I counted about 24 examples: football about 5, athletics about 5, judo about 4, swimming 3, tennis 2, volleyball 2, basketball 2, gymnastics 1. None is above a third. `kit/private_terms.py` is not in the packet and was not run; I saw no detail about the owner.

## Part 7, line by line
- PASS on every line except these:
  - Source log: FIX.
  - Grades: PASS, subject to the should-fix items.
  - Bibliography: F81 unverified.
  - Owner terms: not run.
  - Search flag: off, so not applicable.
- Case facts agree with case-facts.md, including all of SP6's added facts.

## Coach's reading
The unit is usable as written. The rules and the ladder are plainly labelled as the unit's own practice. Section 12 and the week-4 cells of Deliverable A are dense with conditions but correct.

## Brief and deliverable
Every brief item is covered (sections 1 to 10). The deliverable is complete:
- the four-week block for both Dani's and Milan's squads;
- Sara's routine builder;
- both templates.

## Flags naming SP6
- **Met:** F52, F64, F65, F76, F78, F79 (read with F180), F82, F84, F85, F87, F88, F89. F77 and F80 are met as stated and wait on S-SP1.
- **F81:** unresolved.
- **F83:** the review's full text is reachable at https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134. It gives no count for reappraisal, which appears only inside the acclimatisation section.
- **F86:** partly met. The choking review is now opened. Bell et al. (2013) is still not opened. A Bangor record and a published correction to Bell et al. exist; I did not open them.
- **F105:** partly met. Low et al. (2021) name Bell et al. (2013) as both the elite-youth cricket sample and the study that measured competition performance (M1).
- **F106:** unmet; the APA record was not returned.
- **F187:** the ESSA position statement was found: Schweickle et al., *Sports Medicine*, online 10 Jun 2026, doi 10.1007/s40279-026-02472-x, abstract only (https://researchportal.scu.edu.au/esploro/outputs/journalArticle/Performance-Under-Pressure-in-Sport-A/991013385949902368). It supports pressure training and pre-performance routines, says nothing on youth or harm, and changes no grade. The 2025 scoping review was not sought.
- **F94:** not SP6's to fix. **F164, F169:** information only.

## Figures
1. Range, section 2: PASS. Every value is in the text, the caption names the sections and sources, and the kind fits.
2. Compare, section 3: PASS. The values 1.83, 2.8, 4.5 and 4.9 are confirmed.
3. Flow, section 9: PASS.
4. Decision, section 9: PASS. Its outcomes match the step-down list.

## FINDINGS
[error] [accuracy] section 3; Current: "Forfeits appeared in 4 and rewards in 6 of the 14 pooled studies, always combined with other stressors (Low et al., 2021)."; Problem: Table 1 codes all 4 forfeit studies (Bell 2013 cricket; three police studies) with a forfeit as the only stressor; rewards (6) are always paired with judgement.; Fix: "Forfeits appeared in 4 of the 14 pooled studies, each time as the only stressor coded (one elite youth cricket study, three police studies), and rewards in 6, always paired with judgement (Low et al., 2021)."; Basis: Low et al. 2021 Table 1, https://repository.essex.ac.uk/26305/3/PressureTrainingForPerformanceDomains.pdf

[should-fix] [attribution] section 6; Current: "abstract read on the German sport science index LIDA, not the publisher's page](https://doi.org/10.1080/1750984X.2017.1408134)). SP4 read more of the same review (SP4's reading, not re-read for this unit): 62% of its studies used experienced athletes, mean ages were 20 to 40 in 68% of studies, golf was the most common sport, only four studies analysed real competition, and most experiments were rated of medium quality."; Problem: The figures are cited from another unit's reading. The full text is now reachable; it confirms them and gives per-technique counts.; Fix: "abstract read on the German sport science index LIDA; full text read at the publisher's page by the quality review, 19 Nov 2026](https://doi.org/10.1080/1750984X.2017.1408134)). The full text adds: 29 of the 47 studies (62%) used experienced athletes, mean ages were 20 to 40 in 68% of the intervention studies, golf was the most common sport (15 studies), only four studies (9%) analysed real competition, and none of the experimental studies met all of the quality appraisal's criteria, 34 of them meeting half. By technique it counts 10 studies of acclimatisation, 7 of pre-performance routines, 7 of quiet eye, 5 of left-hand contractions, 9 of dual tasks and other task-irrelevant cues, and 7 of analogy and implicit learning."; Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134

[should-fix] [label] section 6; Current: "no separate quiet-eye estimate was read, and a null moderator does not show an equal effect; this review's count per technique not seen]"; Problem: The count is now seen: 7 studies, reported among the interventions most often effective.; Fix: "no separate quiet-eye estimate was read, and a null moderator does not show an equal effect; this review counted 7 quiet-eye studies and lists quiet eye among the interventions most often reported effective]"; Basis: same URL

[should-fix] [label] section 6; Current: "pooled 7 left-hand handgrip samples among its stand-alone routines; as for quiet eye]"; Problem: The review's count for this technique, 5 studies, is now known.; Fix: "pooled 7 left-hand handgrip samples among its stand-alone routines; as for quiet eye; this review counted 5 left-hand contraction studies]"; Basis: same URL

[should-fix] [label] section 6; Current: "[weak, mixed; a systematic review read in abstract, number of studies per technique not seen, rule 5;"; Problem: The stated reason is out of date. The count is 9 studies, but they are pooled with other task-irrelevant cues and the direction per study was not read.; Fix: "[weak, mixed; one systematic review that counts 9 studies of dual tasks and other task-irrelevant cues together, the direction in each not read, so rule 4's three agreeing studies are not shown, rule 5;"; Basis: same URL

[should-fix] [attribution] Sources; Current: "(abstract read on the LIDA index record, https://lida.sport-iat.de/ta/Record/4055257, which shows"; Problem: The source log must record the full-text reading.; Fix: "(full text read at the publisher's page, https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134, by the quality review, 19 Nov 2026, which shows no author byline; abstract read on the LIDA index record, https://lida.sport-iat.de/ta/Record/4055257, which shows"; Basis: same URL

[minor] [coverage] preamble; Current: "Two papers in the course's reading could not be opened and carry no claim: a two-year pressure-training study in elite young cricketers, and the full text of the choking-interventions review (its abstract was read on an index page)."; Problem: The review's full text has now been opened.; Fix: "One paper in the course's reading could not be opened and carries no claim: a two-year pressure-training study in elite young cricketers. The full text of the choking-interventions review, read by the writer only in abstract on an index page, was read at the publisher's page by the quality review (19 Nov 2026)."; Basis: same URL

[minor] [coverage] section 2; Current: "that study could not be opened for this unit."; Problem: The meta-analysis names the study. Naming it links it to section 11's cricket study and answers F105.; Fix: "that study, the elite youth cricket sample (Bell et al., 2013), could not be opened for this unit."; Basis: Low et al. 2021 Results and Table 1, https://repository.essex.ac.uk/26305/3/PressureTrainingForPerformanceDomains.pdf

[minor] [label] section 3; Current: "[weak, for consequences and judgement creating felt pressure; one study of six adults, so for under-18s an inference;"; Problem: The netball study the unit cites (15 adult internationals) also found that consequences, including judgement, raised pressure. The grade does not change.; Fix: "[weak, for consequences and judgement creating felt pressure; two within-subject studies of adult elite athletes, six shooters and 15 netball players (Stoker et al., 2019; Stoker et al., 2017), so for under-18s an inference;"; Basis: https://repository.essex.ac.uk/26359/1/Maynard%20Effect%20of%20manipulating%20training%20demands%20elite%20netball.pdf

[minor] [style] section 6; Current: "(teaching a movement by one image, such as "swing like a pendulum")"; Problem: The quotation marks imply the source's words, but this is the unit's own example.; Fix: "(teaching a movement by one image; this unit's example: swinging like a pendulum)"; Basis: sourcing-standard.md Part 1; https://lida.sport-iat.de/ta/Record/4055257

[minor] [coverage] unsure list; Current: "3. Section 6: Gröpel & Mesagno (2019) read only as an abstract on an index record that does not show the authors (the authors are confirmed on the University of Vienna's sport psychology news page); the number of studies per technique was not seen, so every single-technique grade that rests on this review alone is weak; quiet eye and left-hand contractions take section 5's moderate grade for single-element routines from the routines meta-analysis. The sample details (62% experienced, mean ages 20 to 40 in 68%, golf, four in competition, medium quality) are SP4's reading, not re-read in this session."; Problem: The item is out of date once the fixes above are applied.; Fix: "3. Section 6: Gröpel & Mesagno (2019) read by the writer only as an abstract on an index record that does not show the authors (the authors are confirmed on the University of Vienna's sport psychology news page); the full text was read at the publisher's page by the quality review (19 Nov 2026), which confirmed the sample details and gave per-technique counts; the secondary-task, analogy, goal-setting and reappraisal grades stay weak because the direction in each study was not read; quiet eye and left-hand contractions take section 5's moderate grade for single-element routines, with the review's counts of 7 and 5 studies."; Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134

## UNVERIFIED
- Sources: the author order of Low et al. (2021), because the APA record was not reached.
- Section 2, Kegelaers: "team vulnerabilities fell in one group". The interaction at p = .013 is confirmed; which group fell is not.
- Section 2, Kegelaers: the quote "a careful balance between sufficient challenge and support" is confirmed, but my reading places it in the discussion, not the "introduction".
- Section 2, Kent: "three times over 18 weeks". The sessions were at baseline, 6 and 12 weeks within an 18-week programme; I did not reconcile the two.
- Section 2, Low 2021: "unclear in most domains, with one study high on several". The randomised studies were mostly unclear and Beseler was high in some domains; the non-randomised studies were mostly low or unclear.
- Section 11 and F86: Bell et al. (2013) was not opened.
- Cross-references to SP1 to SP5 could not be checked, because those units are not in the packet.

## Confirmed
- s1 Oudejans & Pijpers 2009, all details: https://research.vu.nl/en/publications/training-with-anxiety-has-a-positive-effect-on-expert-perceptual--2/
- s2 Low 2021, every figure in sections 2 and 3: the definition, inclusion criteria, 394/399 participants, the sports, g, CIs and I², subgroups, moderators, Egger P = .12, retention, the competition study, limitations, and judgement 8, rewards 6, environmental 3: https://repository.essex.ac.uk/26305/3/PressureTrainingForPerformanceDomains.pdf
- s2 Kent 2021, all details including χ² = 7.15, p = .028, the 68 and 26 retested, "partial" and the contract recommendation: https://eprints.glos.ac.uk/9339/1/9339-Kent-(2021)-Implementing-a-pressure-training-program.pdf
- s2 Kegelaers 2021, sample, design, sessions and qualitative reports: https://core.ac.uk/download/387931251.pdf
- s3 Stoker 2016: https://ijsp-online.com/abstract/view/47/262
- s3 Stoker 2019, conditions, means, and judgement and task scores lower than baseline: https://researchonline.ljmu.ac.uk/id/eprint/13095/1/Effect%20of%20pressure%20training%20manipulations%20pressure.pdf
- s3 Stoker 2017: https://repository.essex.ac.uk/26359/1/Maynard%20Effect%20of%20manipulating%20training%20demands%20elite%20netball.pdf
- s3, s4, s8, s10 Low 2023, every claim and quote: https://researchonline.ljmu.ac.uk/id/eprint/18698/3/Pressure%20Training%20From%20Research%20to%20Applied%20Practice.pdf
- s5 Rupprecht 2024, every figure: https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271
- s6 Gröpel & Mesagno, abstract claims and SP4's figures: https://lida.sport-iat.de/ta/Record/4055257 and https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134
- s8 Soligard 2016: https://dspace.lboro.ac.uk/2134/22957
- s8 Tranaeus 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11258162/
- s10 Tannenbaum & Cerasoli 2013, all claims including the CI note: https://cebma.org/assets/Uploads/Tannenbaum-Cerasoli.pdf
- Bibliographic records:
  - https://researchportal.hw.ac.uk/en/publications/pressure-training-for-performance-domains-a-meta-analysis/
  - https://researchportal.hw.ac.uk/en/publications/pressure-training-from-research-to-applied-practice/
  - https://repository.essex.ac.uk/25648/
  - https://repository.essex.ac.uk/26359/
  - https://idrottsforum.org/journal-of-applied-sport-psychology-volume-34-2022-issue-4/ (Kent 34(4):691–712)
  - https://informahealthcare.com/doi/suppl/10.1080/1750984X.2021.1944271
  - https://nih.brage.unit.no/nih-xmlui/handle/11250/2408720?show=full

References opened: all 13 Sources entries, plus the ESSA 2026 abstract. Not opened: Bell et al. 2013; the APA record of Low 2021; PubMed for Tannenbaum (the fetch failed); the Victoria University and Sheffield Hallam repositories (blocked).
