---
check: quality review of SP1 (rule 13), W-SP4, 18 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file)
---

Model: claude-opus-5-5 (Opus 5.5).

I ran the quality review of SP1 (W-SP4, 18 Nov 2026) on the whole unit, with live search. I edited nothing in the unit. My only file is the scratch script `/tmp/w-sp4/pk-qSP1/out/check.py`, which confirmed that each Current string below occurs exactly once in the unit.

**Findings**

1. [should-fix] [grade] Deliverable A, Milan's card; Current: "Replace "just relax" with a specific, practised cue that says what to do [weak, positive; for a 17-year-old an inference, the review's samples being mostly adults; the ironic-effects review in section 8 tested instructions about what to avoid; a meta-analysis of self-talk in sport that tests such cues was not opened for this unit, and SP5 grades it]"; Problem: no opened source tests this recommendation. Bartura et al. tested avoidant instructions, and "just relax" is not one; the self-talk studies were not opened. A grade of weak, positive is a stretch. Under the F14 convention (studies not opened) the grade is practice; Fix: "Replace "just relax" with a specific, practised cue that says what to do [practice; the studies behind it were not opened: the ironic-effects review in section 8 tested instructions about what to avoid, and a meta-analysis of self-talk in sport that tests such cues was not opened for this unit; SP5 grades it]"; Basis: Bartura et al. abstract, https://acikerisim.uludag.edu.tr/entities/publication/79a5441e-8143-4c36-88ff-5f31c5dbb4cc/full; syllabus-flags F14.
2. [should-fix] [figure] §9, decision figure; Current: ""q": "Failed replication, or reviews that disagree?""; Problem: rule 1 is narrower than this question. It needs a pre-registered or multi-site replication, or reviews with opposite conclusions. As drawn, the figure would grade any failed replication contested; Fix: ""q": "Pre-registered or multi-site replication failed, or two reviews reach opposite conclusions?""; Basis: the unit's own §9 rule 1 and the contested row of Deliverable C.
3. [should-fix] [source type, Part 7] §5; Current: "**The studies are small.** An editorial in the *Journal of Sports Sciences* reported that in a random sample of 120 papers submitted to the journal, the median sample size was 19, and only 12 of the 120 reported a power calculation made before the study ([Abt et al., 2020, editorial, reporting the editors' own audit of submissions; not a listed source type](https://doi.org/10.1080/02640414.2020.1776002)). The sample covers sport and exercise science as a whole. The editorial explains that small samples miss real effects more often, overestimate the effects they do find, and replicate less often. Inside sport psychology,"; Problem: these numbers and this mechanism rest on a source that the unit itself says is not a listed type, which Part 7 item 2 forbids. The figures are right (120 papers, median 19, 12 power calculations); Fix: "**The studies are small.** Inside sport psychology,"; Basis: sourcing-standard Part 7; https://informahealthcare.com/doi/full/10.1080/02640414.2020.1776002.
4. [should-fix] [bibliography] Sources; Current: "- Abt G, Boreham C, Davison G, Jackson R, Nevill A, Wallace E, Williams M. Power, precision, and sample size estimation in sport and exercise science research. *Journal of Sports Sciences* 2020;38(17):1933–1935. https://doi.org/10.1080/02640414.2020.1776002 (editorial; authors, title, volume and pages not shown on the page opened, taken from a university repository record: not verified)" plus the newline after it; Problem: once finding 3 is applied, this entry is no longer cited; Fix: "" (delete the line). Basis: Part 1, "nothing is listed that it does not cite". If the maintainer keeps finding 3's text instead, the title and 38(17):1933–1935 match the LIDA record https://lida.sport-iat.de/twm/Record/4065818. That record lists no authors.
5. [minor] [accuracy] §8, imagery; Current: "*g* = 0.99 (95% CI 0.68 to 1.30), with low certainty ("; Problem: the abstract rates the certainty "low to very low"; Fix: "*g* = 0.99 (95% CI 0.68 to 1.30), with certainty the authors rate low to very low ("; Basis: https://mdpi.com/2076-328X/14/3/207.
6. [minor] [population] Deliverable B, claim 3; Current: "Dani is 14: the sample includes her band."; Problem: Hu et al.'s youngest band is 10 to 14, not the course's 13 to 15; Fix: "Dani is 14: the sample's youngest band (10 to 14) includes her age."; Basis: https://frontiersin.org/articles/10.3389/fpsyg.2023.1106916/full.
7. [minor] [scope] Deliverable A, Dani's card; Current: "I raise the concern with her parents and with the person below."; Problem: the card commits to telling the parents before it answers its own question "Who may I speak to about a minor's health, and with whose consent?"; Fix: "I raise the concern with the person below, and with her parents as that person advises."; Basis: the brief's scope rule and the card's own question line.
8. [minor] [grade] §7; Current: "Grade: [contested] by rule 1."; Problem: there is no direction beside the grade, which §9 requires; Fix: "Grade: [contested, no effect shown in the preregistered analyses] by rule 1."; Basis: §9, "The direction goes beside the grade"; Vohs et al. abstract, https://www.psychologicalscience.org/journals/psychological-science/0956797621989733/.
9. [minor] [grade] §8; Current: "for sport performance, no peer-reviewed source found [contested]."; Problem: same as finding 8; Fix: "for sport performance, no peer-reviewed source found [contested, no effect shown in the preregistered analyses]."; Basis: as finding 8.
10. [minor] [grade] §8, grit; Current: "the associations with competitive performance in that review are mixed and mostly cross-sectional [weak, positive, for an association]"; Problem: "positive" overstates the competitive-performance results, which the review calls mixed; Fix: "the associations with competitive performance in that review are mixed and mostly cross-sectional [weak, positive for physical activity, mixed for competitive performance; associations only]"; Basis: https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1563382/full.
11. [minor] [source log] Unsure list item 6; Current: "the five jobs rest on the IOC tools' abstract, one meta-analysis and one study."; Problem: out of date. Gouttebarge et al. is now read in full (see Sources), and Brown & Fletcher was read in abstract only; Fix: "the five jobs rest on the IOC tools' paper (full text read 18 Nov 2026), one meta-analysis read in abstract and one survey."; Basis: https://pmc.ncbi.nlm.nih.gov/articles/PMC7788187.
12. [minor] [bibliography] Sources, Vohs et al.; Current: "*Psychological Science* 2021. https://doi.org/10.1177/0956797621989733"; Problem: the entry has no volume or pages; Fix: "*Psychological Science* 2021;32(10):1566–1581 (volume, issue and pages from a university repository record, https://digitalcommons.unf.edu/unf_faculty_publications/1132, read 18 Nov 2026; not the publisher's record). https://doi.org/10.1177/0956797621989733"; Basis: that record.

**Confirmed** (the claim matches the source)
- AASP guidance: the two routes; sport-science graduates usually not licensed; the psychology route can treat eating disorders and substance problems; check licensing; rules differ by state; undated (AASP PDF).
- Gouttebarge et al. 2021: survey of 360 with no breakdown; reviews plus modified Delphi; SMHAT-1 for licensed or registered professionals, elite athletes aged 16+; the SMHRT-1 quote; timely referral; BJSM 55(1):30–37, 15 authors (PMC7788187).
- Brown & Fletcher 2017: 35 studies, 997 participants, g 0.57 (0.22–0.92); 8 studies, 189 participants, g 1.16 (0.25–2.08); follow-up 1–4 weeks; greatest effect when coach-delivered; RCTs against no treatment or placebo; "moderate", "at least a month"; 47(1):77–99; no ages given (springermedizin; Bath portal).
- Hu et al. 2023: 252 athletes, six provinces, 32 aged 10–14, 38 aged 25+; cross-sectional; mediation chain; direct effect not significant; bibliographic fields correct (Frontiers).
- Reinebo et al. 2024: 111 studies; 54 with university athletes (48.65%); mean ages about 19.1–35; 25 studies and 37 effects in 5 meta-analyses; g 0.83, 0.67, 0.75 with the stated CIs; effects not significant after the sensitivity analyses; RCTs asked for; 54:347–373; issue number not shown (Springer PDF).
- Martin et al. 2025: 33 studies; 37,370 participants; about 5,113 athletes; wrestlers, ultra-runners, wheelchair rugby; results mixed; mostly cross-sectional; the conscientiousness statement; a 17–19 subsample; authors correct (Frontiers).
- Lakens 2013: the "arbitrary…rigidly" quote; the 0.2/0.5/0.8 labels; the CL definition; d 1.13 gives 79% (Frontiers).
- Rupprecht et al. 2024: 61 samples; 112 effect sizes; ages 11–40; 16/32/13 by sample size; SMC 0.31 (0.18–0.44); g 0.64 (0.45–0.83); g 0.70 (0.24–1.16) from 19 effect sizes; no moderators; small-study effect in pre-post; p-uniform result; 17(1):39–64 (informahealthcare; LIDA record).
- Abt et al. 2020: 120 papers, median 19, 12 a priori power calculations, the consequences of small samples (informahealthcare); title and 38(17):1933–1935 (LIDA).
- Lochbaum et al. 2022: 30 meta-analyses, 1983–2021, 16 constructs; d 0.51 and −0.21 with the examples; quality and design not moderators; authors; 17(2) (DOAJ abstract).
- Metzler & Grèzes 2019: 82 men aged 17–32; 81 analysed; participant pool and job sites; 2 min × 3; no hormone difference by posture; no behavioural power measures; did not replicate Carney et al.; not stated as pre-registered; PeerJ 7:e6726.
- Vohs et al. 2021: 36 labs; 3,531 participants; d 0.06; about 4× under the null with prior δ 0.30; exploratory d 0.08; larger with fatigue; no participant description (APS page).
- Sisk et al. 2018: k 273 / N 365,915; k 43 / N 57,155; the "Overall effects were weak" quote; low-SES / at-risk moderators; no pooled effect size in the abstract (APS page). Fields 29(4):549–571 and authors match the lab-hosted PDF.
- Yeager et al. 2019: 12,490 ninth-graders aged 14–15; 65 schools; 2 × ~25 min sessions; n 6,320; 0.10 (0.04–0.16); 0.11 SD; peer norms; pre-registered; 573:364–369 (nature.com).
- Bethlehem et al. 2022: 123,984 scans from 101,457 people; prenatal to 100 years; 100+ studies; peaks 1.7 / 5.9 / 14.4 / 28.7 with bootstrap CIs (eScholarship PDF); 604:525–533 (Cornell CBIC record; the eScholarship copy gives 532).
- Tervo-Clemmens et al. 2023: four datasets (two longitudinal, two cross-sectional); N 10,766; ages 8–35; 23 measures; the "18–20" quote; 14:6922; authors correct (nature.com PDF).
- Barrett et al. 2019: the review's conclusion; the accompanying Cowen et al. article on face, voice and body; 20(1); five authors (APS page).
- Macnamara et al. 2016: 18% / 1%; higher-skill athletes did not start younger (APS page); pages 333–350 (LIDA).
- Güllich & Barth 2024: k 51; 6,233 athletes; 82% male; 2009–2022; the "opposite" quote; holds across sport types and levels; high-quality studies; 54:697–710 (Springer).
- Dekker et al. 2012: 242 teachers in the UK and NL; 93/96, 91/86, 48/46; more brain knowledge, more myths; 3:429 (Frontiers).
- Bartura et al.: 24 studies before Jan 2022; 17 articles; 1,152 participants; half novice studies; a third highly trained; one elite; mean age about 21.8; one study under 18; 5 experimental and 19 quasi-experimental (21% / 79%) (Uludağ repository).
- Morales-Sánchez et al. 2020: 103 male players aged 12–17; one club; controlling style → thwarting → burnout; 17(13):4909 (MDPI).
- Gómez-López et al. 2020: 479 players aged 16–17; regional teams; ego climate → fear of failure → anxiety and lower self-confidence; cross-sectional; 17:592 (CORE PDF of the article).
- Fletcher & Sarkar 2016: the footnote on "extreme challenge-no support" environments; the "unethical and inappropriate imposition of adversity" quote; no empirical test (informahealthcare); fields 7(3):135–157 (NTU repository).
- Steffen et al. 2022: triune model rejected; emotion and cognition interdependent; no pure circuits; 13:802606 (Frontiers).
- Berridge 2018: wanting, not liking; the "hedonic reputation" quote; raising dopamine does not reliably raise human pleasure ratings; 9:1647 (Frontiers).
- Mustile et al. 2024: 21 adults; similarities between imagined and real walking, plus additional cortical resources for imagery; 18:1412307 (Stirling PDF).
- Lin et al. 2017: 51 papers / 56 studies; the populations; four twin studies; the "Approximately 50%" quote; two PST programmes in athletes (youth) with no controls stated; "lack of empirical support"; "speculative" (Huddersfield PDF).
- Sturt et al. 2012: 10 studies; 5 RCTs with n 22–106; the conclusion quote; authors including Metcalfe; 62(604):e757–e764 (BJGP).
- Harris et al. 2018: 43 studies; 7 devices; one soccer study (passing improved, dribbling and shooting did not); small samples; little independent replication; the quote; 9:709 (Frontiers).
- Case facts: every fact about Dani, Milan and Sara matches case-facts.md, including the six SP1 additions. "(fictional)" is on first use. The case is never used as evidence.

**Fresh-check prompt (audit-units §3)**
- (1) Coverage: every item of the brief is covered. Grit is thin: it rests on a physical-activity review, not on a replication or meta-analysis of grit (Credé et al. not opened, and no flag records that). I could not check that the popular claims match the seed list in full, because bibliography.md is not in this folder.
- (2) Accuracy: see Confirmed and Not verified.
- (3) Figures: every number says whose figure it is.
- (4) Labels: correlations, editorial, narrative reviews and abstract-only reads are all labelled.
- (5) Deliverable: present in full, both on the case and as templates.
- (6) Errata: the last round's notes are applied. In flags F2 and F11, the Lochbaum part is now done; those flags are out of date.
- (7) Figures:
  - Figure 1, matrix, §2: PASS.
  - Figure 2, range, §6: PASS (every value matches the text).
  - Figure 3, compare, §8: PASS.
  - Figure 4, decision, §9: FIX (finding 2).

**Passes**
- Claims: 31 sources opened; no FAIL. Two small wording issues (findings 5 and 10). The items I could not open are under Not verified.
- Bibliography: every entry I opened matches field by field. Vohs is incomplete (finding 12). Bartura (volume, issue, pages), Reinebo and Güllich (issue) and Deng (age, g) were not checked at the publisher. Bethlehem's last page differs between the two records (532 vs 533).
- Source log: the unit file has no source log. About 18 Sources entries (for example Berridge, Bethlehem, Dekker, Deng, Hu, Martin, Yeager) state neither what was read nor the date. The unit's notes say those rows are in a separate log, which is not in my folder, so I could not check them. Every abstract-only claim in the unit says so: Brown & Fletcher, Vohs, Sisk, Macnamara, Fletcher & Sarkar.
- Grades: one grade does not follow the key (finding 1); two have no direction (findings 8 and 9). Everything else follows the rules as written. The strong example rests on a single meta-analysis (open as F1 and unsure-list item 5).
- Population: every finding names its sample. Transfers to younger athletes are labelled as inference (§2, §6, §7, §8, the cards).
- Scope and safety: PASS, apart from finding 7. Nothing teaches assessment, diagnosis or treatment. No weight method or figure, no self-harm method, no law stated as the reader's. No real person is named as an example of failure.
- Any sport: about 16 examples. Football about 5 (≈31%, under a third). Judo 2, athletics 2, handball 2, tennis 2, wrestling, ultra-running and wheelchair rugby 1 each. No owner-identifying detail found.
- Part 7, line by line: these fail:
  - Source type: the Abt editorial (findings 3 and 4). The two narrative reviews (Steffen, Berridge) and the practitioner article (Fletcher & Sarkar) are not listed types either, but each is labelled with "no grade rests on it".
  - Source-log line: not checkable here.
  - Grade-follows-key line: finding 1.

  Every other line passes. Read as the coach in the preamble would, the unit is dense but usable, and nothing reads as advice without evidence.
- Brief and flags: the brief and deliverable are met in full. Flags given to SP1:
  - Dealt with in the unit: F5/F27, F6, F9, F12, F15.
  - Correctly left open: F3, F11 (Ranehill, Hagger), F23, F47, F48.
  - F2 and the Lochbaum part of F11 are now done, but the flag rows have not been updated.
  - F10 (rendering) is a filing step; not checkable here.

**Not verified**
- Lochbaum et al.: the counts of 14 / 13 / 3 by type; the participant range; "no ages per meta-analysis". The PLOS page was reached only by a redirect and PMC returned a captcha.
- Deng et al.: g 0.99 (0.68–1.30) and ages 9–18. Neither is in the abstract; the full text at PMC returned a captcha. These also appear in §5 and §8.
- Bartura et al.: 17(2):1378–1417.
- Brown & Fletcher: whether every pooled study was an RCT (the abstract says RCTs were searched for).
- Ranehill 2015, Hagger 2016, Credé 2017, Bissett 2020, Bartholomew 2009/2011, Wegner: not opened by me (the unit cites none of them for a claim).
- Completeness against the seed list's popular claims.
- The external source log.

Verdict: SP1 · fix · 0 error, 4 should-fix, 8 minor
