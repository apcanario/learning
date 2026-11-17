Verdict: SP1 · fix · 0 error, 7 should-fix, 7 minor

Model: claude-opus-5-5. Quality review of SP1 (F46, rule 13), run on 17 Nov 2026 with live search (round 4). Every source was opened again in this agent. WebFetch was used only on URLs that a search in this agent returned verbatim. The harness refused the write to out/report.md, so the full report follows here.

## Findings

[should-fix] [grade] §8, "Learning styles…"; Current: "Do not sort athletes by learning style or by brain side [practice; the studies that test learning styles were not opened, graded as flag F14 directs until they are]."; Problem: Rule 2 gives practice only when "no study of any design … tests the claim". The unit says itself that studies test learning styles, so rule 2 does not fit. F14 covers a different case: a recommendation whose only opened source is a consensus statement resting on studies that were not opened. No consensus statement is cited here. Dekker et al. measure teachers' belief and do not test learning styles. The grade follows no rule of §9, so it fails the Part 7 line "the grade follows SP1's key".; Fix: "Whether sorting athletes by learning style or by brain side helps or harms is not graded here: the studies that test learning styles were not opened for this unit (not verified), so no rule of section 9 can be applied; a later unit that opens them grades it."; Basis: unit §9 rule 2; flags.md F14; https://www.frontiersin.org/articles/10.3389/fpsyg.2012.00429/full (Dekker et al.: a survey of 242 teachers, not a test).

[should-fix] [population] §6, closing paragraph; Current: "Mental-skills interventions improve performance [moderate, positive]; later units grade each skill on its own."; Problem: The grade comes mostly from adult and university samples. In Reinebo et al., 54 of 111 studies were in university athletes and the mean ages ran from about 19 to 35. Brown & Fletcher's abstract gives no ages. The reader coaches athletes aged 10 to 25, and SP1's further rule says such a grade "applied to an athlete under 18 carries the label inference". The label is missing here.; Fix: "Mental-skills interventions improve performance [moderate, positive; from samples mostly aged 18 and over, so for athletes under 18 an inference]; later units grade each skill on its own."; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01931-z.pdf; unit §9, the further rules.

[should-fix] [attribution] §2, first bullet; Current: "and, for the assessment tool, a modified Delphi process (consensus)"; Problem: The BJSM abstract page names a "modified Delphi consensus process" but does not say it applied to the assessment tool only. The restriction could not be verified and is not marked. It also conflicts with Deliverable C, which says the IOC built the division "into its two mental health tools by a consensus process".; Fix: "and a modified Delphi consensus process"; Basis: https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract

[should-fix] [bibliography] Sources, Rupprecht et al.; Current: "*International Review of Sport and Exercise Psychology* 2024;17(1):39–64 (online 2021). https://doi.org/10.1080/1750984X.2021.1944271"; Problem: The publisher's page (informahealthcare.com) shows no title, authors, journal, volume, issue, pages or year. The source log says these fields come from the seed list. The Sources entry does not say so and does not mark them not verified.; Fix: "*International Review of Sport and Exercise Psychology* 2024;17(1):39–64 (online 2021). https://doi.org/10.1080/1750984X.2021.1944271 (abstract and parts of the body text read; title, authors, volume and pages not shown on the page opened, taken from the course's seed list: not verified)"; Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271

[should-fix] [bibliography] Sources, Bartura et al.; Current: "*International Review of Sport and Exercise Psychology* 2024;17(2):1378–1417 (online 11 April 2023). https://doi.org/10.1080/1750984X.2023.2193966"; Problem: The publisher's page shows the title and the online date, 11 Apr 2023, which are confirmed. It shows no authors, volume, issue or pages, and the source log records that the earlier review could not confirm them either. The entry does not mark them not verified.; Fix: "*International Review of Sport and Exercise Psychology* 2024;17(2):1378–1417 (online 11 April 2023). https://doi.org/10.1080/1750984X.2023.2193966 (abstract and parts of the body text read; authors, volume, issue and pages not shown on the page opened: not verified)"; Basis: https://informahealthcare.com/doi/full/10.1080/1750984X.2023.2193966

[should-fix] [bibliography] Sources, Macnamara et al.; Current: "*Perspectives on Psychological Science* 2016;11(3):333–350. https://doi.org/10.1177/1745691616635591 (abstract read)"; Problem: The APS journal page shows the title and abstract only, with no authors, volume or pages. PubMed and SAGE could not be reached. The entry does not mark these fields not verified.; Fix: "*Perspectives on Psychological Science* 2016;11(3):333–350. https://doi.org/10.1177/1745691616635591 (abstract read on the journal's page at the Association for Psychological Science, which shows title and abstract only; authors, volume and pages not shown on the page opened: not verified)"; Basis: https://www.psychologicalscience.org/journals/perspectives/1745691616635591/

[should-fix] [bibliography] Sources, Barrett et al.; Current: "*Psychological Science in the Public Interest* 2019;20(1):1–68. https://doi.org/10.1177/1529100619832930 (read on the publisher's summary page only)"; Problem: The APS summary page and the PSPI abstract page give the title and "Barrett and colleagues". Neither shows the co-authors, volume, issue or pages. The source log takes these from the seed list's Crossref record, which was not opened here. The entry does not mark them not verified.; Fix: "*Psychological Science in the Public Interest* 2019;20(1):1–68. https://doi.org/10.1177/1529100619832930 (read on the publisher's summary page and the journal's abstract page only; co-authors, volume and pages not shown there, taken from the course's seed list: not verified)"; Basis: https://www.psychologicalscience.org/publications/emotional-expressions-reconsidered-challenges-to-inferring-emotion-from-human-facial-movements.html; https://www.psychologicalscience.org/journals/pspi/1529100619832930/

[minor] [bibliography] Sources, Reinebo et al.; Current: "*Sports Medicine* 2024;54(2):347–373."; Problem: Volume 54 and pages 347–373 are confirmed on the Springer PDF. The issue number is not shown there, and the PMC page served a reCAPTCHA (not checked).; Fix: "*Sports Medicine* 2024;54(2):347–373 (issue number not shown on the page opened: not verified)."; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01931-z.pdf

[minor] [bibliography] Sources, Metzler & Grèzes; Current: "Metzler, Grèzes (initials not shown on the page opened)."; Problem: The authors' full names are on the PubMed Central copy: Hannah Metzler and Julie Grèzes.; Fix: "Metzler H, Grèzes J."; Basis: https://pmc.ncbi.nlm.nih.gov/articles/PMC6585898 (PubMed Central; PeerJ's own page gives "Metzler & Grèzes" only)

[minor] [grade] Deliverable B, claim 1, Grade row; Current: "(rule 5: one controlled study, outside sport, not a replication)"; Problem: §8 says, correctly, that the study "reports that it did not replicate the original hormonal effects", and the paper says "we did not replicate the effects reported by Carney, Cuddy & Yap (2010)". Calling it "not a replication" contradicts §8. The grade is still right: the article does not state a preregistration and the study ran at a single site, so rule 1 does not apply.; Fix: "(rule 5: one controlled study, outside sport; it reports that it did not replicate the original hormonal effects, but it is not stated to be pre-registered and is not multi-site, so rule 1 does not apply)"; Basis: https://peerj.com/articles/6726; https://pmc.ncbi.nlm.nih.gov/articles/PMC6585898

[minor] [attribution] §3, correlational studies; Current: "say exactly this about their own evidence"; Problem: The preceding sentence says correlational studies cannot show which variable causes which "or rule out a third factor". Martin et al. say only that their mostly cross-sectional evidence leaves causality open ("future research is needed to elucidate whether a causal relationship exists"). "Exactly this" stretches what they say.; Fix: "say that their evidence cannot settle whether the relationship is causal"; Basis: https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1563382/full

[minor] [attribution] §6, first bullet; Current: "Brown & Fletcher pooled randomised controlled trials in athletes against no treatment or placebo."; Problem: The meta-analysis pools "psychological and psychosocial interventions", so the g = 0.57 and g = 1.16 figures cover both. The bullet's heading and the §6 figure label call them psychological interventions only.; Fix: "Brown & Fletcher pooled randomised controlled trials of psychological and psychosocial interventions in athletes against no treatment or placebo."; Basis: https://www.springermedizin.de/effects-of-psychological-and-psychosocial-interventions-on-sport/12118340

[minor] [attribution] §7, ego depletion; Current: "than under the effect the authors had expected"; Problem: The abstract compares the null with an informed-prior hypothesis (δ = 0.30, SD = 0.15). It does not describe that hypothesis as what the authors expected.; Fix: "than under the informed-prior hypothesis of an effect of about δ = 0.30"; Basis: https://www.psychologicalscience.org/journals/psychological-science/0956797621989733/

[minor] [label] §8, harsh coaching; Current: "A practitioner article on developing resilience, which reports no test of its own,"; Problem: A practitioner article is not one of the source types in Part 7. The unit labels the other non-listed sources (Abt et al.'s editorial; the Steffen and Berridge narrative reviews) as outside the list, with no grade resting on them. This one is not labelled.; Fix: "A practitioner article on developing resilience (outside the source types the course lists; no grade rests on it), which reports no test of its own,"; Basis: sourcing-standard.md Part 7, line 2; https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496

Each Current string was checked by script and occurs exactly once in unit.md.

## Seven passes
- **Claims:** 30 cited sources. 29 were opened at a publisher's page or DOI address (Gouttebarge's volume and pages also at PubMed Central). Sisk et al. was opened at its APS journal page in abstract only. Every number in the unit traces to its source except the points listed above. One page was refused (see Could not verify).
- **Bibliography:** All 30 references exist. Unmarked fields that could not be verified: Rupprecht, Bartura, Macnamara, Barrett (should-fix) and Reinebo's issue (minor). No reference is invented.
- **Source log:** All 30 Sources entries have a log row (1–15, 18–32; rows 16 and 17 are opened but not cited). Every claim that rests on an abstract alone says so in the unit: Brown & Fletcher, Gouttebarge, Sisk, Vohs, Macnamara, Barrett (summary), Fletcher & Sarkar (abstract and notes).
- **Grades:** §9 matches grade-key-SP1-section9.md word for word (checked by diff). Each grade was checked against the rules and the evidence. Correct: Güllich & Barth [strong, association] (rule 3 holds: CI excludes zero; robust across programme type, level and sport type; "The quality of primary studies was high"; I² ≈ 75% appears in Table 2 but the authors do not flag it; Macnamara agrees). Also correct: Rupprecht [moderate], Reinebo/Brown & Fletcher [moderate], imagery [moderate], ego depletion [contested], power pose, grit, growth mindset, harsh coaching, NLP, brain training, faces, the age-25 claim [weak], ironic effects [weak], scope line [practice]. Wrong: learning styles (should-fix).
- **Population:** Each finding names its sample. Missing: the inference label on the §6 general grade (should-fix). The IOC division applied to 11–17-year-olds, power posing, and the ironic-effects advice on Milan's card all carry the inference label.
- **Scope and safety:** Pass. Nothing teaches assessment, diagnosis or treatment. Dani's skipped snack is noticed and referred with no comment on weight. There is no weight-loss method, calorie figure, target weight or self-harm method. Legal and consent duties are put as questions with the body to ask. The disclaimer is in the opening lines. No real athlete, coach or club is named; Wegner is named as a theorist only.
- **Any sport:** About 11 distinct sport examples: judo (Dani), football (Milan; Morales-Sánchez; the NeuroTracker soccer study), 400 m (Sara), tennis (Deng), handball (Gómez-López), and wrestling, ultra-running and wheelchair rugby (Martin). Football has 3 of about 11, under a third. Individual, team, weight-class and endurance sports all appear. Whether the unit contains anything about the Project's owner could not be checked: private_terms.py is outside the packet.

## Part 7, line by line
1. Sourced where made: pass, except the §2 Delphi scope (finding).
2. Source types: the editorial, two narrative reviews and AASP's undated guide are labelled; the practitioner article is not (finding).
3. No video or press source: pass.
4. Source log and abstract-only claims: pass.
5. Sources match the publisher's record: four entries with unmarked fields (findings).
6. Grades follow the key: learning styles fails (finding).
7. Sample and design stated, correlation called correlation: pass.
8. Inference label: §6 (finding).
9. Effect sizes in the source's terms with their samples: pass.
10. Popular claims set against their evidence: pass for the claims in the unit; the course list itself is not in the packet.
11. Coach's part: pass.
12. Weight and self-harm: pass.
13. Law and disclaimer: pass.
14. Named persons: pass.
15. Three kinds of sport, none above a third: pass.
16. Case facts: pass. Every fact about Dani, Milan and Sara matches case-register.md, and all three are labelled "(fictional)" on first use (line 16). Sara's "any medical staff her federation provides" is conditional and adds no fact.
17. Private terms: not checked.
18. Search flag: off for SP1, so not applicable.
19. Deliverable on the case, then a template: pass.
20. Reads as advice without evidence: no.
21. Links as DOI links: pass.

## Brief and deliverable completeness
Covered: the professions and titles, put as questions; the coach's part and where it ends; the kinds of evidence; effect size, sample and control group; small, adult samples; the replication cases; the popular claims; the five grades; the five questions.

Thin, and disclosed in the unit:
- How far psychological variables relate to performance (Lochbaum not opened, F2).
- Grit's replication case rests on a systematic review, not a replication or meta-analysis (Credé not opened).
- The coach's role "as the literature defines it" rests on the IOC abstract and two studies (F3).

Deliverable:
- Scope card built in full for all three athletes, plus a template with country, federation and club blanks.
- Claim-check sheet worked in full on three claims, plus a template.
- Grade key with one worked example per grade.

## Flags naming SP1
- F12: applied in the unit. The age-25 entry is regraded [weak, against the claim] with Tervo-Clemmens et al. (2023). The flag can close.
- F15: applied in the unit, in the last paragraph of Deliverable C (IOC division under rule 2; SP2's sleep hours under rule 5). The flag can close.
- F27: applied. §8 adds Morales-Sánchez, Gómez-López and the Fletcher & Sarkar notes. F5 stays open for Bartholomew et al.
- F11: partly overtaken. Vohs et al. has been opened, so ego depletion now carries [contested] and the contested row has a worked example. Ranehill, Hagger and Lochbaum stay held. Sisk is applied in abstract. The flag's text needs updating.
- F14: misapplied to learning styles (finding).
- F10: figures not rendered here; viz.py needs design/theme.css, which is outside the packet.
- F46: this review.
- F9: met in the unit. F2, F3, F4 and F5 are disclosed in the unit.

## Figures (7)
1. matrix, §2 — PASS. Every label traces to §2's scope line ("shape the climate, teach skills…, notice…, hold a first conversation, and refer"; "You do not run screening questionnaires, name a condition, or start a treatment"). The caption names the section and sources. The kind fits roles by jobs.
2. range, §6 — PASS. All six point estimates and CIs match §6 (0.57/0.22–0.92; 1.16/0.25–2.08; 0.83/0.21–1.45; 0.67/0.01–1.32; 0.75/0.14–1.36; 0.70/0.24–1.16). The kind fits competing estimates. The label "Psychological interventions" carries the same narrowing as the minor attribution finding; if that finding is applied, the first two labels may read "Psychological and psychosocial interventions, post-test / follow-up (Brown & Fletcher)".
3. compare, §8 — PASS. 1.7, 5.9, 14.4 and 28.7 match §8 and Bethlehem et al. The caption names the section and source.
4. decision, §9 — PASS. The branches follow rules 1 to 5 in order. The caption names the section and says what is the preamble's and what is the unit's.

None was rendered (F10).

## Could not verify
- Metzler & Grèzes PeerJ PDF (https://peerj.com/articles/6726.pdf): fetch refused, not checked. The claims were checked on the PeerJ article page and PMC instead.
- Gómez-López et al. at PMC: redirected, not checked. Opened at mdpi.com instead.
- Reinebo et al. at PMC: reCAPTCHA, not checked. Sisk et al. at PubMed: reCAPTCHA, not checked. Abt et al. at PubMed: empty page, not checked.
- Issue numbers for Reinebo (2) and Brown & Fletcher (springermedizin shows 1/2017; volume 47 and pages 77–99 not shown).
- Bibliographic fields not shown on any accepted page opened:
  - Authors, volume and pages for Sisk, Vohs, Macnamara, Rupprecht and Bartura.
  - Authors, title, volume and pages for Abt (the editorial's text was confirmed).
  - All fields for Fletcher & Sarkar.
- Author lists of Lin et al. and Steffen et al. were not shown in the fetch summaries (titles, journals and DOIs confirmed).
- Not opened, because no search returned an accepted address: Ranehill 2015, Hagger 2016, Lochbaum 2022, Credé 2017, Bissett 2020, and Pashler 2008 (sought as a source for the learning-styles fix).
- The course's popular-claims list (bibliography.md) and private_terms.py are not in the packet, so list completeness and owner-privacy could not be checked.
- The figures were not rendered.

## Confirmed
- AASP guide (https://appliedsportpsych.org/site/assets/documents/HowToChooseASportPsychConsultant.pdf): two routes; "do not usually become licensed psychologists"; "most often become licensed psychologists"; eating disorders and drug abuse; "Each state has its own licensure requirements"; undated, issuer not named.
- Gouttebarge et al. (https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract): SMHAT-1 for "sports medicine physicians and other licensed/registered health professionals", ages 16 and over; SMHRT-1 "developed for athletes and their entourage"; N = 360; reviews and modified Delphi; timely referral; BJSM 55(1):30–37 (PMC7788187).
- Brown & Fletcher (springermedizin.de page above): k = 35, n = 997, g = 0.57 (0.22–0.92); k = 8, n = 189, g = 1.16 (0.25–2.08); 1–4 weeks; no-treatment or placebo comparisons; coach-delivered; "moderate positive effect"; "may last at least a month".
- Hu et al. (https://www.frontiersin.org/articles/10.3389/fpsyg.2023.1106916/pdf): 252 athletes in six provinces; age bands 32/114/68/38; team and individual sports; cross-sectional; negative correlation with basic psychological needs; chain through constrained commitment; direct effect not significant.
- Reinebo et al. (Springer PDF): 111 studies, 25 studies with 37 effects in five syntheses; PST 0.83 (0.21–1.45), MA 0.67 (0.01–1.32), imagery 0.75 (0.14–1.36), parallel-group; not significant after removing non-randomised trials and subjective outcomes; 54/111 (48.65%) university athletes; mean ages about 19–35; call for RCTs; 54:347–373.
- Martin et al. (Frontiers page): 33 studies, 37,370 adults aged 18 and over, 5,113 athletes, the sports named; mostly cross-sectional; perseverance of effort "highly correlated with conscientiousness".
- Lakens (Frontiers page): d as standardised mean difference; 0.2/0.5/0.8; "these values are arbitrary and should not be interpreted rigidly"; common language effect size; d = 1.13 gives 79%.
- Rupprecht et al. (informahealthcare page): 33 articles, 61 samples, 112 effect sizes; SMC 0.31 (0.18–0.44); g 0.64 (0.45–0.83); g 0.70 (0.24–1.16) from 19 effect sizes; samples 16/32/13; ages 11–40; no moderators; small-study effect in pre–post only; p-uniform.
- Abt et al. editorial (informahealthcare page): 120 papers submitted to the journal, median sample 19, 12 with an a priori power calculation; underpowered studies overestimate effects and are less replicable.
- Metzler & Grèzes (peerj.com/articles/6726, PMC6585898): 82 men aged 17–32, 81 analysed; participant pool and student job sites; 2 min × 3 in one session; no posture effect on testosterone, cortisol or progesterone; no behavioural power measures; "we did not replicate the effects reported by Carney".
- Vohs et al. (APS page): 36 labs, 3,531 participants; d = 0.06, not significant; about 4 times more likely under the null; exploratory d = 0.08; larger with fatigue.
- Sisk et al. (APS page): k = 273, N = 365,915; k = 43, N = 57,155; weak overall effects; low-SES and academically at-risk students.
- Yeager et al. (nature.com): 12,490 ninth-graders aged about 14–15; 65 schools; two sessions of about 25 minutes; n = 6,320; 0.10 (0.04–0.16), standardised 0.11; peer norms; pre-registered; Nature 573:364–369.
- Bethlehem et al. (nature.com): 123,984 scans, 101,457 participants, more than 100 studies, 115 days post-conception to 100 years; peaks 1.7, 5.9 (total cortical GMV), 14.4 and 28.7 years with bootstrap CIs; Nature 604:525–533.
- Tervo-Clemmens et al. (Nature Communications PDF): 4 datasets (2 longitudinal, 2 cross-sectional), N = 10,766, ages 8–35; 23 measures from 17 tasks; "stabilizing to adult-levels in late adolescence (18–20 years old)"; 14:6922.
- Barrett et al. (APS pages): facial configurations not reliable or specific; accompanying Cowen et al. article on face, voice and body.
- Macnamara et al. (APS page): 18% of variance overall, 1% among elite performers; high-skill athletes did not start earlier.
- Güllich & Barth (Springer PDF, PMC10978645): 51 effect sizes, 6,233 athletes, 82% male, 2009–2022; d −0.53 (−0.74 to −0.32) junior, 0.56 (0.40–0.72) senior; quoted "opposite" sentence; robust across programme types, levels and sports; high-quality primary studies; 54(3):697–710.
- Dekker et al. (Frontiers page): 242 teachers (137 UK, 105 NL); 93/96, 91/86, 48/46; "More general knowledge also predicted an increased belief in neuromyths."
- Bartura et al. (informahealthcare page): 24 studies before January 2022; 1,152 participants in 17 studies; 5 experimental and 19 quasi-experimental; about half novices, a third national-level, one elite; mean age 21.78; one under-18 study; no pooling; the quoted Wegner sentence; online 11 Apr 2023.
- Morales-Sánchez et al. (mdpi.com): 103 male footballers aged 12–17 at one club; single questionnaire session; β 0.53 and 0.66; 17(13):4909.
- Gómez-López et al. (mdpi.com): 479 players (250 boys, 229 girls) aged 16–17; ego climate definition; β 0.37, 0.44, 0.51, −0.22; 17(2):592.
- Fletcher & Sarkar (informahealthcare page): note 7, "toughening-up" and "the unethical and inappropriate imposition of adversity"; no test reported.
- Steffen et al. (Frontiers page): triune regions "function relatively independently" (the unit paraphrases "fairly", unquoted); "does not accurately explain how the brain functions"; emotion and cognition interdependent; no purely emotional or cognitive circuits; no "hijack".
- Berridge (Frontiers page): "Dopamine then failed to live up to its hedonic reputation." (exact); wanting versus liking in rats; L-DOPA does not raise pleasure ratings.
- Mustile et al. (Frontiers PDF): 24 recruited, 21 analysed, ages 18–44; walking, imagery and counting; both quoted phrases; 18:1412307.
- Deng et al. (mdpi.com): 9 controlled trials, 548 tennis players aged 9–18; accuracy g 0.99 (0.68–1.30) from 8 studies; speed 0.25 (−0.03 to 0.54); low certainty; authors' full names confirmed.
- Lin et al. (Frontiers PDF): 51 papers (56 studies); military candidates; four twin studies; the 50% sentence; Gucciardi programmes "worked to increase subsequent ratings of MT", controls not stated; "lack of empirical support"; "remain speculative".
- Sturt et al. (bjgp.org): 10 studies (5 RCTs, 5 pre–post); RCT samples 22–106; the quoted conclusion; limited quantity and quality; 62(604):e757–e764; DOI.
- Harris et al. (Frontiers PDF): 43 studies, 7 devices; one soccer study (passing improved; dribbling and shooting did not); small samples; developer ties; the quoted sentence.
