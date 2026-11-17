Verdict: SP1 · fix · 0 error, 11 should-fix, 12 minor

Model: claude-opus-5-5. Quality review of SP1 (round 5), 17 Nov 2026. The harness refused out/report.md, so this is the full report for the chat to save as-is. I opened every source in this agent, each at an address that a WebSearch in this agent returned. PubMed pages came back empty and were not checked. I did not use PMC copies.

## Findings

[should-fix] [style: reviewer note in reader's text] Section 6, first paragraph; Current: "The other half of the brief's item, how far psychological *variables* (traits and states) relate to performance, is not covered here and is held open under flag F2 until the review is opened at journals.plos.org. It covers *interventions*, from three meta-analyses that were opened."; Problem: this tells the reader about a flag number, a brief and a fetch target, which are process notes. "It" also has no clear referent; Fix: "How far psychological *variables* (traits and states) relate to performance is not covered in this unit. This section covers *interventions*, from three meta-analyses that were opened."; Basis: task rule (no editing instruction or reviewer note in the reader's text); flags.md F2.

[should-fix] [style: editing instruction in reader's text] Section 8, "Harsh coaching builds toughness"; Current: "The reviews by Bartholomew et al. (2009, 2011) in the course list could not be opened; DD-SP1 must open them."; Problem: "must open them" is an instruction to a later writer; Fix: "The reviews by Bartholomew et al. (2009, 2011) in the course list could not be opened and carry no claim here; DD-SP1 returns to them."; Basis: task rule; flags.md F5, F27.

[should-fix] [grade] Deliverable A, Milan's card, "What I do"; Current: "Replace "just relax" with specific, practised cues that say what to do [practice; the ironic-effects review in section 8 tested instructions about what to avoid, not this one]."; Problem: rule 2 gives practice only when no study of any design tests the claim. Studies do test instructional cues: a meta-analysis on the APS journal page "Self-Talk and Sports Performance" (*Perspectives on Psychological Science*) reports "A total of 32 studies yielding 62 effect sizes" and "instructional self-talk was more effective for fine tasks rather than gross tasks". So [practice] does not follow section 9; Fix: "Replace "just relax" with a specific, practised cue that says what to do [weak, positive; the ironic-effects review in section 8 tested instructions about what to avoid; a meta-analysis of self-talk in sport that tests such cues was not opened for this unit, and SP5 grades it]."; Basis: https://www.psychologicalscience.org/journals/perspectives/1745691611413136/ (abstract; authors and year not shown on the page); unit section 9, rule 2.

[should-fix] [accuracy: claim not verifiable, not marked] Section 7, growth mindset; Current: "([Sisk et al., 2018, abstract read](https://doi.org/10.1177/0956797617739704))"; Problem: I could not open Sisk et al. at any accepted address. The fetch of the APS journal page was refused, SAGE returned a client error and PubMed was blank. So k = 273, N = 365,915, k = 43, N = 57,155 and the quotation "Overall effects were weak for both meta-analyses" could not be verified, and the unit does not mark them "not verified"; Fix: "([Sisk et al., 2018, abstract read; not verified](https://doi.org/10.1177/0956797617739704))"; Basis: not opened (https://www.psychologicalscience.org/journals/psychological-science/0956797617739704/ refused; https://journals.sagepub.com/doi/abs/10.1177/0956797617739704 client error).

[should-fix] [bibliography: field unverified, not marked; reviewer note] Sources, Sisk et al.; Current: "(abstract read on the journal's page at the Association for Psychological Science, which shows title and abstract only; authors, year, volume and pages are from the fresh check's record and were not shown on the page opened)"; Problem: I could not verify the authors, the year, 29(4) or pages 549–571. "The fresh check's record" is a process note in the reader's text; Fix: "(abstract read on the journal's page at the Association for Psychological Science, which shows title and abstract only; authors, year, volume and pages not shown on the page opened: not verified)"; Basis: as above, not opened.

[should-fix] [bibliography: field unverified, not marked] Sources, Gouttebarge et al.; Current: "*British Journal of Sports Medicine* 2021;55(1):30–37. https://doi.org/10.1136/bjsports-2020-102411 (abstract read; consensus)"; Problem: the BJSM abstract page shows the 15 authors and the title but no volume, issue or pages. No search returned a publisher page that carries 55(1):30–37; Fix: "*British Journal of Sports Medicine* 2021;55(1):30–37. https://doi.org/10.1136/bjsports-2020-102411 (abstract read; consensus; volume, issue and pages not shown on the page opened: not verified)"; Basis: https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract

[should-fix] [bibliography: field unverified, not marked] Sources, Brown & Fletcher; Current: "(abstract read; volume and pages not shown on the page opened, from the course's seed list)"; Problem: pages 77–99 are not shown at the publisher. Volume 47(1) is only inferred from a cover-image address; Fix: "(abstract read; volume and pages not shown on the page opened, from the course's seed list: not verified)"; Basis: https://www.springermedizin.de/effects-of-psychological-and-psychosocial-interventions-on-sport/12118340

[should-fix] [bibliography: field unverified, not marked] Sources, Abt et al.; Current: "(editorial; authors, title, volume and pages not shown on the page opened, taken from a university repository record)"; Problem: a repository record is neither the publisher's page nor Crossref. The Taylor & Francis page shows the body only and PubMed was blank; Fix: "(editorial; authors, title, volume and pages not shown on the page opened, taken from a university repository record: not verified)"; Basis: https://informahealthcare.com/doi/full/10.1080/02640414.2020.1776002 (body only); https://pubmed.ncbi.nlm.nih.gov/32558628/ (empty, not checked).

[should-fix] [bibliography: field unverified, not marked] Sources, Güllich & Barth; Current: "*Sports Medicine* 2024;54(3):697–710. https://doi.org/10.1007/s40279-023-01957-3"; Problem: the publisher's PDF header reads "Sports Medicine (2024) 54:697–710" and gives no issue number, so issue 3 is unverified; Fix: "*Sports Medicine* 2024;54:697–710 (issue number not shown on the page opened: not verified). https://doi.org/10.1007/s40279-023-01957-3"; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf

[should-fix] [bibliography: fields unverified, not marked; reviewer note] Sources, Fletcher & Sarkar; Current: "(abstract and notes read; the page opened shows no authors, title, journal, volume or pages: they are given as SP3 gives them, from the course's seed list)"; Problem: none of the fields could be verified at the publisher, whose page shows only the notes and their citations. "As SP3 gives them" is a process note; Fix: "(abstract and notes read; the page opened shows no authors, title, journal, volume or pages; they are from the course's seed list: not verified)"; Basis: https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496

[should-fix] [flag naming SP1, stale] flags.md F11 (this Current occurs once, in flags.md); Current: "Ego depletion carries no grade and the grade key's contested row has no worked example until they are applied."; Problem: the unit now grades ego depletion [contested] by rule 1 on Vohs et al. (2021), and the contested row uses it as its worked example. Sisk et al. has been read in abstract. The flag states facts about SP1 that are no longer true; Fix: "Vohs et al. (2021) and Sisk et al. (2018) have since been read in abstract; ego depletion is graded [contested] on Vohs et al. alone and the contested row's worked example rests on it; the fixes needing Hagger et al. (2016), Ranehill et al. (2015) and Lochbaum et al. (2022) stay held."; Basis: unit.md sections 7 and 8; Deliverable C, contested row.

[minor] [population] Section 2, Hu et al.; Current: "Chinese provinces, aged 10 to over 25, found"; Problem: the oldest group is "25+", so 25-year-olds are included; Fix: "Chinese provinces, aged 10 to 25 and over, found"; Basis: https://frontiersin.org/articles/10.3389/fpsyg.2023.1106916/full (10–14 n = 32, 15–19 n = 114, 20–24 n = 68, 25+ n = 38).

[minor] [population] Deliverable B, claim 3, row 2; Current: "aged 10 to over 25, 32 of them aged 10 to 14"; Problem: same as the finding above; Fix: "aged 10 to 25 and over, 32 of them aged 10 to 14"; Basis: as above.

[minor] [population: inference label] Section 8, ironic effects; Current: "[weak, positive; DD-SP3 regrades it from the primary studies]"; Problem: this general recommendation comes from samples with a mean age of 21.78, only one study included under-18s, and the readers coach athletes aged 10 to 25. The inference label is missing here, although Milan's card carries it; Fix: "[weak, positive; samples mostly adults, so for athletes under 18 an inference; DD-SP3 regrades it from the primary studies]"; Basis: https://informahealthcare.com/doi/full/10.1080/1750984X.2023.2193966 ("The mean age of the participants across all studies was 21.78"; "K = 1 reported participants younger than 18").

[minor] [label: abstract only] Deliverable C, practice row; Current: "([Gouttebarge et al., 2021](https://doi.org/10.1136/bjsports-2020-102411)). Practice (consensus)."; Problem: this claim rests on the abstract alone and does not say so here, although section 2 does; Fix: "([Gouttebarge et al., 2021, abstract read](https://doi.org/10.1136/bjsports-2020-102411)). Practice (consensus)."; Basis: Part 7 ("a claim that rests on an abstract alone says so").

[minor] [grade] Deliverable A, Dani's card, "What I do"; Current: "including the question of her weight class, which she has raised once [practice]."; Problem: the unit's own sources test this climate claim with correlational studies: controlling style against need satisfaction (Hu et al., 2023, ages 10 to 25+) and against need thwarting (Morales-Sánchez et al., 2020, ages 12 to 17). Rule 2 says a claim tested only by correlational studies is not practice; Fix: "including the question of her weight class, which she has raised once [weak, positive, for an association: the surveys in sections 2 and 8 link a controlling style to lower need satisfaction and need thwarting; correlational]."; Basis: section 9, rule 2; https://mdpi.com/1660-4601/17/13/4909; Hu page above.

[minor] [bibliography: outdated note] Sources, Reinebo et al.; Current: " (issue number not shown on the page opened: not verified)"; Problem: the issue is now verified. The Springer Medizin page shows "Issue 2/2024", and the publisher's PDF header gives "Sports Medicine (2024) 54:347–373"; Fix: ""; Basis: https://www.springermedizin.de/effects-of-psychological-interventions-to-enhance-athletic-perfo/26143846; https://link.springer.com/content/pdf/10.1007/s40279-023-01931-z.pdf

[minor] [bibliography: outdated note] Sources, Bartura et al.; Current: "(abstract and parts of the body text read; authors, volume, issue and pages not shown on the page opened: not verified)"; Problem: the publisher's supplementary-material page shows the four authors and the title. Only the volume, issue and pages remain unverified; Fix: "(abstract and parts of the body text read; authors as on the publisher's supplementary-material page; volume, issue and pages not shown on the pages opened: not verified)"; Basis: https://informahealthcare.com/doi/suppl/10.1080/1750984X.2023.2193966?scroll=top

[minor] [bibliography / source log] Sources, Barrett et al.; Current: "(read on the publisher's summary page and the journal's abstract page only; co-authors, volume and pages not shown there, taken from the course's seed list: not verified)"; Problem: the APS summary page shows all five authors and "Volume 20, Number 1". Source log row 2 records the summary page only ("abstract not shown"), which contradicts "the journal's abstract page"; Fix: "(read on the publisher's summary page only, which shows the five authors and volume 20, number 1; pages not shown there, taken from the course's seed list: not verified)"; Basis: https://www.psychologicalscience.org/publications/emotional-expressions-reconsidered-challenges-to-inferring-emotion-from-human-facial-movements.html; sources-log.md row 2.

[minor] [bibliography: outdated note] Sources, Rupprecht et al.; Current: "(abstract and parts of the body text read; title, authors, volume and pages not shown on the page opened, taken from the course's seed list: not verified)"; Problem: the publisher's supplementary page shows the authors, the title, 2021 and pages 39–64. Only the volume and issue remain unverified; Fix: "(abstract and parts of the body text read; authors, title and pages 39–64 as on the publisher's supplementary-material page; volume and issue not shown on the pages opened: not verified)"; Basis: https://informahealthcare.com/doi/suppl/10.1080/1750984X.2021.1944271

[minor] [flag naming SP1, stale] flags.md F5 (this Current occurs once, in flags.md); Current: "SP1's entry on harsh coaching rests on one cross-sectional study (Hu et al., 2023)."; Problem: the entry now rests on three single-measurement surveys and on the notes in Fletcher & Sarkar (2016); Fix: "SP1's entry on harsh coaching rests on three single-measurement surveys (Hu et al., 2023; Morales-Sánchez et al., 2020; Gómez-López et al., 2020) and the notes of Fletcher & Sarkar (2016); the Bartholomew reviews remain unopened (F27)."; Basis: unit.md section 8; Deliverable B, claim 3.

[minor] [flag naming SP1, status] flags.md F12 (this Current occurs once, in flags.md); Current: "regrade SP1's entry to agree with SP2, citing Tervo-Clemmens et al. (2023). No brief changes. | open |"; Problem: this has been applied. Section 8 grades the entry [weak, against the claim] and cites Tervo-Clemmens et al. (2023); Fix: "regrade SP1's entry to agree with SP2, citing Tervo-Clemmens et al. (2023). No brief changes. | carried (SP1 section 8 now grades it [weak, against the claim], citing Tervo-Clemmens et al., 2023) |"; Basis: unit.md section 8, "The brain finishes developing at 25".

[minor] [flag naming SP1, status] flags.md F15 (this Current occurs once, in flags.md); Current: "at SP1's next corrections pass. No brief changes. | open |"; Problem: this has been applied. The paragraph under the grade key now says when a consensus statement is graded by rule 2 and when by rules 3 to 5, with the IOC division and SP2's sleep hours as examples; Fix: "at SP1's next corrections pass. No brief changes. | carried (SP1 Deliverable C, the paragraph under the grade key) |"; Basis: unit.md Deliverable C, last paragraph.

## Passes

- **Claims:** I opened every cited source except Sisk et al., which I could not open. Every other claim I checked passes; the list is under Confirmed.
- **Bibliography:** every entry exists. Six have unmarked fields I could not verify: Sisk, Gouttebarge, Brown & Fletcher, Abt, Güllich & Barth (issue) and Fletcher & Sarkar. Four entries carry outdated notes: Reinebo, Bartura, Barrett and Rupprecht. No reference is missing.
- **Source log:** all 30 Sources entries have a row (rows 1–15 and 18–32). Every claim that rests on an abstract says so, except the practice row of Deliverable C. Log row 2 and the Barrett entry disagree.
- **Grades:** I checked every grade against rules 1 to 5.
  - Power pose [weak] holds. PeerJ does not say this study was pre-registered (it mentions pre-registration only for other studies), and it is single-site.
  - Güllich & Barth [strong, for the association] holds. The CIs exclude zero, the subgroups agree, and the paper says "The quality of primary studies was high". The authors do not flag heterogeneity in the text; I² of about 75% appears only in Table 2.
  - Imagery [moderate] holds: the meta-analysis in athletes has low GRADE certainty.
  - Ego depletion [contested] holds by rule 1.
  - Two grades do not follow rule 2: Milan's cue [practice] (should-fix) and Dani's climate [practice] (minor).
- **Population:** every finding names its sample. One inference label is missing in section 8, and "over 25" appears twice where the source has "25+".
- **Scope and safety:** pass.
  - Nothing teaches assessment, diagnosis or treatment.
  - Dani's card makes no weight comment and gives no calorie figure or target weight.
  - Legal duties are put as questions, each with a body to consult.
  - The information-not-advice line is present.
  - No real athlete, coach or club is named.
- **Any sport:** pass, at the limit. By mention: football 5 (Milan's card, claim 1, Morales-Sánchez twice, Harris), judo 3, 400 m 2, tennis 2, handball 2, mixed 1 (Martin). That makes football 5 of 15, exactly a third, which is not above it. The examples cover an individual sport, a team sport, a weight-class sport (judo) and an endurance sport. I could not run kit/private_terms.py.
- **Part 7, line by line:**
  - Sourced where made: pass.
  - Source types: pass. An editorial, a practitioner article and two narrative reviews are labelled as outside the listed types, and no grade rests on them.
  - No banned source: pass.
  - Every reference in the source log: pass.
  - Sources match the publisher's record: fix (see Bibliography).
  - Every recommendation graded: pass.
  - Grades follow the key: fix (two).
  - Sample and design stated: pass.
  - Inference labelled: fix (one).
  - Effect sizes in the source's own terms: pass.
  - Popular claims named and set against evidence: pass for those present.
  - Coach's part: pass.
  - Weight and self-harm: pass.
  - Law: pass.
  - Real persons: pass.
  - Three kinds of sport: pass.
  - Case athletes labelled "(fictional)" on first use and agreeing with case-register.md: pass. SP1's added facts are in the register.
  - Private terms: not run.
  - Search flag: does not apply to SP1.
  - Deliverable built on the case, then as a template: pass.
  - Not advice without evidence: pass.
  - DOI links: pass.
- **Brief and deliverable completeness:**
  - Every brief item is covered except how far psychological variables relate to performance (Lochbaum not opened, F2), so that item is thin.
  - The scope card has its blanks for country, federation and club.
  - The claim-check sheet is worked in full on three claims and has its template.
  - The grade key has one worked example per grade.
  - The text before Sources runs to about 7,500 words, against the brief's 2,000–6,000. The brief also says "do not cut to a target", so this is reported, not counted as a finding.
  - I could not check coverage against the brief's list of popular claims, because bibliography.md is not in the packet.
- **Figures:** all four viz blocks parse as JSON. viz.py cannot render them here because design/theme.css is not in the packet, so F10 stays open.
  1. Matrix, section 2: PASS. Every row label is in section 2, the caption names the section and the sources, and items by roles fits a matrix.
  2. Range, section 6: PASS. All six points and their CIs match lines 77–79, the caption names the sources, and estimates with intervals fit a range.
  3. Compare, section 8: PASS. The values 1.7, 5.9, 14.4 and 28.7 match line 105, and the caption names the section and the source.
  4. Decision, section 9: PASS. The branches follow rules 1 to 5 in order, and the caption says what the figure shows and where it comes from.
- **Flags naming SP1:** F1, F2, F3, F4, F7, F8, F9, F10, F14 and F46 agree with the unit. F11 and F5 are stale. F12 and F15 have been applied but are still open. F27 is superseded but consistent with the unit.
- **Reviewer notes in the reader's text:** two in the body (section 6 and section 8) and two in Sources (Sisk and Fletcher & Sarkar), all listed above. The closing unsure list and its fresh-check and correction lines are the method's own appendage; I have not reported them.

## Could not verify

- Sisk et al. 2018: every claim and every bibliographic field. The APS fetch was refused, SAGE returned a client error and PubMed was blank, so it is not checked.
- Gouttebarge et al. 2021: volume 55, issue 1, pages 30–37.
- Brown & Fletcher 2017: pages 77–99. Volume 47(1) is inferred from an image address only.
- Abt et al. 2020: authors, title, 38(17) and pages 1933–1935.
- Güllich & Barth 2024: issue 3.
- Fletcher & Sarkar 2016: every bibliographic field.
- Fields the unit already marks "not verified" and that remain unverified:
  - Barrett: pages.
  - Macnamara: authors, volume, pages.
  - Vohs: co-authors, volume, pages.
  - Bartura: volume, issue, pages.
  - Rupprecht: volume, issue.
- Not in the packet: the brief's list of popular claims (bibliography.md), kit/private_terms.py, and design/theme.css for rendering.

## Confirmed

- **AASP guide** (undated; the document does not name its issuer).
  - Two routes: "do not usually become licensed psychologists"; "most often become licensed psychologists".
  - Clinical areas include eating disorders.
  - "to practice in your state"; "Each state has its own licensure requirements".
  - https://appliedsportpsych.org/site/assets/documents/HowToChooseASportPsychConsultant.pdf
- **Gouttebarge et al. 2021**
  - Built from narrative and systematic reviews, a survey of N = 360 athletes and a modified Delphi process.
  - SMHAT-1 is for licensed or registered professionals, for elite athletes aged 16 and over.
  - SMHRT-1 was "developed for athletes and their entourage"; the tools aim at timely referral.
  - 15 authors.
  - https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract
- **Brown & Fletcher 2017**
  - RCTs only.
  - Post-test: k = 35, n = 997, g = 0.57 (0.22–0.92).
  - Follow-up: k = 8, n = 189, g = 1.16 (0.25–2.08).
  - Effects greatest when coach-delivered; "moderate positive effect"; "may last at least a month"; no ages given.
  - springermedizin.de page above.
- **Hu et al. 2023**
  - 252 athletes in six provinces; the age groups as listed; team and individual sports; cross-sectional.
  - r = −0.356; chain through constrained commitment; the direct path is not significant.
  - All bibliographic fields.
  - Frontiers page above.
- **Reinebo et al. 2024**
  - 111 studies; 25 pooled (37 effects) in five meta-analyses.
  - PST g = 0.83 (0.21–1.45); MAAB g = 0.67 (0.01–1.32); imagery g = 0.75 (0.14–1.36).
  - No synthesis stays significant after the restriction.
  - 54 of 111 (48.65%) university athletes; mean ages about 19–35; the call for RCTs.
  - 54(2):347–373; authors.
- **Rupprecht et al.**
  - 33 articles, 61 samples, 112 effect sizes.
  - SMC 0.31 (0.18–0.44); g = 0.64 (0.45–0.83; 42 ES); g = 0.70 (0.24–1.16; 19 ES).
  - Ages 11–40; no significant moderators; a small-study effect; the p-uniform sentence.
  - Samples: 16 under 10, 32 of 10–19, 13 over 20.
  - Authors, title, pages 39–64, 2021.
  - https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271
- **Abt et al., content**
  - "randomly selected 120 papers submitted"; median 19 (11); "only 12" with an a priori power calculation; the three consequences; it is an editorial.
- **Lakens 2013**
  - d as the standardised mean difference; 0.2, 0.5, 0.8; "these values are arbitrary and should not be interpreted rigidly".
  - Common-language effect size; d = 1.13 gives 79%.
  - https://www.frontiersin.org/articles/10.3389/fpsyg.2013.00863/full
- **Martin et al. 2025**
  - 33 studies; 37,370 participants aged 18 and over; 5,113 athletes, including wrestlers, ultra-runners and wheelchair rugby players.
  - Mixed findings; "the nature of cross-sectional studies limits conclusions on causality"; the conscientiousness sentence.
  - One study reports "16.7% were 17–19 years".
- **Metzler & Grèzes 2019**
  - 82 men aged 17–32, recruited through a participant pool and student job sites; 81 analysed; 2 min × 3.
  - No posture difference in any of the three hormones; no behavioural or feelings-of-power measures.
  - "we did not replicate the effects reported by Carney, Cuddy & Yap (2010)"; not stated to be pre-registered; PeerJ 7:e6726.
  - https://peerj.com/articles/6726
- **Vohs et al. 2021** (content and title)
  - k = 36, N = 3,531; d = 0.06; data 4 times more likely under the null, prior δ = 0.30.
  - Exploratory d = 0.08; fatigue moderates.
  - APS page above.
- **Yeager et al. 2019**
  - 12,490 students, "age 14–15 years", in 65 schools; two sessions of about 25 min; a pre-registered analysis plan.
  - n = 6,320, B = 0.10 (0.04–0.16), effect size 0.11; peer norms moderate.
  - Nature 573:364–369.
- **Bethlehem et al. 2022**
  - 123,984 scans of 101,457 people from more than 100 studies; ages 115 days post-conception to 100 years.
  - Peaks at 1.7, 5.9, 14.4 and 28.7, with bootstrap CIs; Nature 604:525–533.
- **Tervo-Clemmens et al. 2023**
  - 10,766 people aged 8–35; two longitudinal and two cross-sectional datasets; 23 measures from 17 tasks.
  - The quotation; athletic status not stated; all bibliographic fields.
- **Barrett et al. 2019, content:** the conclusion as summarised; the accompanying Cowen et al. article on face, voice and body; the five authors; volume 20(1).
- **Macnamara et al. 2016, content:** 18% overall and 1% among elite athletes; elite athletes did not start earlier; 10,000 hours is not mentioned.
- **Güllich & Barth 2024**
  - k = 51, N = 6,233, 82% male, studies 2009–2022.
  - Junior d = −0.53 (−0.74 to −0.32); senior d = 0.56 (0.40 to 0.72).
  - The "opposite" quotation; robust across individual and team sports and across levels; high-quality primary studies.
- **Dekker et al. 2012**
  - 242 teachers (137 UK, 105 NL).
  - 93% and 96%, 91% and 86%, 48% and 46%; the general-knowledge sentence.
  - All bibliographic fields.
- **Bartura et al.**
  - 24 studies before January 2022; 1,152 participants across 17 studies; 5 experimental and 19 quasi-experimental.
  - Participants: 12 novices, 8 national-level, 1 elite; mean age 21.78; one study under 18.
  - Narrative synthesis with no meta-analysis; the Wegner sentence; authors and title.
- **Morales-Sánchez et al. 2020:** 103 boys aged 12–17 at one club, measured once; β = 0.53 and 0.66; all bibliographic fields.
- **Gómez-López et al. 2020:** 479 players (250 boys, 229 girls) aged 16–17; the ego-climate definition; β = 0.37, 0.44, 0.51 and −0.22; all bibliographic fields.
- **Fletcher & Sarkar, content:** both quotations in note 7.
- **Steffen et al. 2022:** a Review with no search method (narrative); the quotations; "amygdala hijack" is absent; all bibliographic fields.
- **Berridge 2018:** a Review; wanting, not liking; dopamine does not reliably raise pleasure ratings; the "hedonic reputation" quotation.
- **Mustile et al. 2024:** 21 of 24 analysed, aged 18–44; overlap; the "additional cortical resources" quotation; all bibliographic fields.
- **Deng et al. 2024:** 9 trials, 548 participants aged 9–18; g = 0.99 (0.68–1.30); low certainty; the full author names.
- **Lin et al. 2017**
  - 51 papers (56 studies); the populations; four twin studies; "Approximately 50%".
  - Two PST programmes, with no control groups stated; "lack of empirical support"; "remain speculative".
  - All bibliographic fields.
- **Sturt et al. 2012:** 10 studies; 5 RCTs with 22–106 participants; the quotation; "limited quantity and quality"; all bibliographic fields.
- **Harris et al. 2018:** 43 studies of 7 devices; one soccer study (passing improved; dribbling and shooting did not); limited independent replication; the quotation.
