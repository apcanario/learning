---
check: corrections C-SP1 (SP1; flags F10 (not this agent's), F11, F23), W-SP4, 18 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file); only the fence labels "```Current" and "```Replacement" are written as "Current:" and "Replacement:" lines above a plain fence, so `thin.py correct` can read them
---

Model: claude-opus-5-5

Summary: 19 changes: 15 PASS, 0 FAIL, 4 not checked; 1 New item (no unit change). No syllabus conflict. Date of all reads: 18 Nov 2026. Unit: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md. Every Current below occurs exactly once in it (script count).

Note on the held fixes. The Current strings of the held fixes in fresh-check-SP1.md no longer occur in the unit, because the unit was revised in R-SP1. So each change below is drafted against the unit as filed, not copied from the fresh check (New 1).

## Source log
Every address below was returned verbatim by a search in this agent.
- Lochbaum 2022: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0263408. Full text at the publisher. (The DOI address redirected; the redirect was not followed.)
- Gouttebarge 2021: https://pmc.ncbi.nlm.nih.gov/articles/PMC7788187. Full text at PubMed Central.
- Barrett 2019: https://pmc.ncbi.nlm.nih.gov/articles/PMC6640856. Full text in part (first 100,000 of 580,800 characters) at PubMed Central.
- Bartura 2024: https://informahealthcare.com/doi/full/10.1080/1750984X.2023.2193966. Full text; no journal, volume or pages shown.
- Rupprecht 2024: https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271. Full text; no bibliographic block shown.
- Güllich & Barth 2024: Springer PDF (no issue number shown), then https://pmc.ncbi.nlm.nih.gov/articles/PMC10978645/, which gives 54(3).
- Reinebo 2024: https://link.springer.com/content/pdf/10.1007/s40279-023-01931-z.pdf. Full text; authors and 54, 347–373 shown, no issue number.
- Brown & Fletcher 2017: https://link.springer.com/10.1007/s40279-016-0552-7. Abstract only (subscription preview).
- Fletcher & Sarkar 2016: informahealthcare full-text address. Abstract and notes only.
- Not opened:
  - Ranehill 2015: SAGE client_error; APS page refused by the permission check.
  - Hagger 2016: no publisher, PubMed or DOI address returned.
  - Vohs 2021: no publisher, PubMed or DOI address returned.
  - Sisk 2018: SAGE client_error; PubMed reCAPTCHA.
  - Macnamara 2016: no SAGE or PubMed address returned; APS domain refused.
  - Abt 2020: PubMed reCAPTCHA.
- Not used: author and repository copies.
- PubMed Central is treated here as PubMed's full-text archive. If the next review does not accept that, Changes 4–7, 9–11 and 14 become "not checked".

## Change 1
File: unit, section 6
Current:
```
The 2022 systematic review of meta-analyses on sport psychology and performance in the course's seed list (Lochbaum et al., 2022) could not be opened at its publisher's page, PubMed or DOI address, so it is not verified here; this section reports none of its figures. How far psychological *variables* (traits and states) relate to performance is not covered in this unit. This section covers *interventions*, from three meta-analyses that were opened.
```
Replacement:
```
**Psychological variables.** A 2022 systematic review of 30 meta-analyses published from 1983 to 2021, covering 16 sport psychology constructs, found that variables expected to help performance (among them cohesion, confidence and mindfulness) had a moderate positive effect, *d* = 0.51, and variables expected to harm it (among them cognitive anxiety, depression and an ego climate) a small negative one, *d* = −0.21. Neither the quality of the meta-analyses nor whether their studies were interventions or correlational significantly moderated these effects. Of the 30 meta-analyses, 14 pooled correlational studies, 13 intervention studies and three a mix or mostly cross-sectional studies; where the pooled studies are correlational, the effect is a correlation. Participants ranged from children and adolescents to college-aged volunteers and elite athletes, and the review gives no ages for each meta-analysis ([Lochbaum et al., 2022](https://doi.org/10.1371/journal.pone.0263408)). The rest of this section covers *interventions*, from three meta-analyses that were opened.
```
Result: PASS
Quote: "were shown to have a moderate beneficial effect (d = 0.51)". The full text also gives: 30 meta-analyses, 1983 to January 2021, 16 constructs, d = −0.21, the named examples, no significant moderation by quality or design, the 13/14/2/1 split, and the participant range. The Limitations section says "only 12" were exclusively intervention-based.
Syllabus: No conflict. The SP1 brief asks for "what the reviews of meta-analyses say about how far psychological variables and interventions relate".

## Change 2
File: unit, Sources
Current:
```
- Macnamara BN, Moreau D, Hambrick DZ. The relationship
```
Replacement:
```
- Lochbaum M, Stoner E, Hefner T, Cooper S, Lane AM, Terry PC. Sport psychology and performance meta-analyses: A systematic review of the literature. *PLoS ONE* 2022;17(2):e0263408. https://doi.org/10.1371/journal.pone.0263408 (full text read on the publisher's page, https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0263408, 18 Nov 2026)
- Macnamara BN, Moreau D, Hambrick DZ. The relationship
```
Result: PASS
Quote: as Change 1. The PLOS page shows the authors and 17(2):e0263408.
Syllabus: No conflict.

## Change 3
File: unit, Unsure list
Current:
```
1. Section 6: the review of meta-analyses (Lochbaum et al. 2022, PLOS ONE) could not be opened, so the unit says nothing on how far psychological variables relate to performance; the brief's item is covered for interventions only.
```
Replacement:
```
1. Section 6: the review of meta-analyses (Lochbaum et al. 2022, PLOS ONE) was read in full on its publisher's page on 18 Nov 2026; it gives no ages for each meta-analysis, 14 of its 30 meta-analyses pooled correlational studies, and its Results (13) and Limitations (12) give different counts of intervention-based meta-analyses.
```
Result: PASS
Quote: as Change 1.
Syllabus: No conflict. This follows from Change 1.

## Change 4
File: unit, section 2
Current:
```
built from narrative and systematic reviews, a survey of 360 active and former elite athletes and a modified Delphi consensus process.
```
Replacement:
```
built from narrative and systematic reviews, a survey of 360 people (active and former elite athletes, coaches in elite sport and representatives of sport governing bodies; the paper does not say how many were athletes) and a modified Delphi consensus process.
```
Result: PASS (correction). The abstract says all 360 were athletes; the Methods do not.
Quote: "coaches in elite sports or (iii) representatives of sport governing bodies". The full text also confirms: SMHAT-1 is for licensed or registered professionals and for athletes aged 16 and over; SMHRT-1 was "developed for athletes and their entourage"; the aims are earlier recognition and timely referral; 55(1):30–37; 15 authors.
Syllabus: No conflict. The grade is unchanged.

## Change 5
File: unit, section 2
Current:
```
The stated aim is earlier recognition and timely referral ([Gouttebarge et al., 2021, abstract read](https://doi.org/10.1136/bjsports-2020-102411)).
```
Replacement:
```
The stated aim is earlier recognition and timely referral ([Gouttebarge et al., 2021, full text read](https://doi.org/10.1136/bjsports-2020-102411)).
```
Result: PASS
Quote: as Change 4.
Syllabus: No conflict.

## Change 6
File: unit, Deliverable C, practice row
Current:
```
([Gouttebarge et al., 2021, abstract read](https://doi.org/10.1136/bjsports-2020-102411)). Practice (consensus).
```
Replacement:
```
([Gouttebarge et al., 2021, full text read](https://doi.org/10.1136/bjsports-2020-102411)). Practice (consensus).
```
Result: PASS
Quote: as Change 4. The full text reports a Delphi process and a pilot in 281 footballers. It reports no test of the division against another, so "no study opened tests it" stands.
Syllabus: No conflict. The grade-key example is unchanged.

## Change 7
File: unit, Sources (Gouttebarge)
Current:
```
(abstract read; consensus; volume, issue and pages not shown on the page opened: not verified)
```
Replacement:
```
(consensus; full text read at PubMed Central, https://pmc.ncbi.nlm.nih.gov/articles/PMC7788187, 18 Nov 2026, which shows volume 55, issue 1, pages 30–37 and fifteen authors; published online 18 September 2020)
```
Result: PASS
Quote: as Change 4.
Syllabus: No conflict.

## Change 8
File: unit, Sources (Brown & Fletcher)
Current:
```
(abstract read; volume and pages not shown on the page opened, from the course's seed list: not verified)
```
Replacement:
```
(abstract read on the publisher's page, https://link.springer.com/10.1007/s40279-016-0552-7, 18 Nov 2026, which shows volume 47, issue 1, pages 77–99; full text not available there)
```
Result: PASS. The fields are confirmed. The body claims stay "abstract read".
Quote: "there was some evidence that effects were greatest in coach-delivered interventions". The abstract also confirms k 35/N 997, g 0.57 (0.22–0.92) and k 8/N 189, g 1.16 (0.25–2.08). No ages are given.
Syllabus: No conflict.

## Change 9
File: unit, section 8 (faces)
Current:
```
([Barrett et al., 2019, publisher's summary page read](https://doi.org/10.1177/1529100619832930))
```
Replacement:
```
([Barrett et al., 2019, publisher's summary page and the first part of the full text read](https://doi.org/10.1177/1529100619832930))
```
Result: PASS. The part read confirms the conclusion and does not mention sport. The sentence on the accompanying article stays on the summary page's authority.
Quote: facial movements are not "sufficiently reliable and specific across contexts, individuals, and cultures".
Syllabus: No conflict. The grade is unchanged, and SP7 builds on it as before.

## Change 10
File: unit, Sources (Barrett)
Current:
```
(read on the publisher's summary page only, which shows the five authors and volume 20, number 1; pages not shown there, taken from the course's seed list: not verified)
```
Replacement:
```
(publisher's summary page read, which shows the five authors and volume 20, number 1; the first part of the full text read at PubMed Central, https://pmc.ncbi.nlm.nih.gov/articles/PMC6640856, 18 Nov 2026, which shows pages 1–68)
```
Result: PASS
Quote: as Change 9. The page shows 20(1):1–68.
Syllabus: No conflict.

## Change 11
File: unit, Unsure list
Current:
```
8. Section 8, faces: Barrett et al. (2019) was read only on the publisher's summary page; the conclusion is paraphrased from that summary.
```
Replacement:
```
8. Section 8, faces: Barrett et al. (2019) was read on the publisher's summary page and, on 18 Nov 2026, in its first part (about a sixth of the text) at PubMed Central, which confirms the conclusion; the accompanying article is known from the summary page only.
```
Result: PASS
Quote: as Change 9.
Syllabus: No conflict.

## Change 12
File: unit, Sources (Bartura)
Current:
```
(abstract and parts of the body text read; authors as on the publisher's supplementary-material page; volume, issue and pages not shown on the pages opened: not verified)
```
Replacement:
```
(full text read on the publisher's page, https://informahealthcare.com/doi/full/10.1080/1750984X.2023.2193966, 18 Nov 2026; authors as on the publisher's supplementary-material page; journal, volume, issue and pages not shown on the pages opened: not verified)
```
Result: PASS. The fields stay marked. The body claims are confirmed: 24 studies in 17 articles; 1,152 participants; 50% novices; 33% highly trained; 1 elite; mean age 21.78; one under-18 study; 5 experimental and 19 quasi-experimental. The text does not say which experimental studies used athletes, so grading by rule 5 stands.
Quote: "findings (k = 22; 92%) align with Wegner's theory".
Syllabus: No conflict. DD-SP3 still regrades this.

## Change 13
File: unit, Sources (Rupprecht)
Current:
```
(abstract and parts of the body text read; title, authors, year, volume, issue and pages not shown on the pages opened, taken from the course's seed list: not verified)
```
Replacement:
```
(full text read on the publisher's page, https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271, 18 Nov 2026; title, authors, year, volume, issue and pages not shown there, taken from the course's seed list: not verified)
```
Result: PASS. The body claims are confirmed:
- 112 effect sizes from 61 samples
- SMC 0.31 (0.18–0.44)
- g 0.64 (0.45–0.83) and g 0.70 (0.24–1.16), the latter from 19 effect sizes
- 16, 32 and 13 samples of fewer than 10, 10 to 19, and more than 20 participants
- no moderation by age, gender or skill
- a small-study effect in the pre-to-post data
- p-uniform found no evidence of publication bias
Quote: "Athletes' age ranged from 11 to 40 years in the included samples."
Syllabus: No conflict. The moderate worked example is unchanged.

## Change 14
File: unit, Sources (Güllich & Barth)
Current:
```
*Sports Medicine* 2024;54:697–710 (issue number not shown on the page opened: not verified).
```
Replacement:
```
*Sports Medicine* 2024;54(3):697–710 (issue number from PubMed Central, https://pmc.ncbi.nlm.nih.gov/articles/PMC10978645/, 18 Nov 2026).
```
Result: PASS
Quote: "Sports Med. 2023 Nov 3;54(3):697–710"
Syllabus: No conflict.

## Change 15
File: unit, Unsure list
Current:
```
7. Sources entries with details not shown on the page opened: ironic-effects review (authors, volume, pages), J Sports Sci editorial (authors, headline), tennis imagery meta-analysis (author surnames), Rupprecht et al. (title, authors, volume, pages from the seed list), Gouttebarge et al., Brown & Fletcher, Barrett et al. (volume, pages from the seed list), Reinebo et al. and Güllich & Barth (issue numbers).
```
Replacement:
```
7. Sources entries with details not shown on a page opened: ironic-effects review (journal, volume, issue, pages; authors from the supplementary-material page), J Sports Sci editorial (authors, headline), tennis imagery meta-analysis (author surnames), Rupprecht et al. (title, authors, year, volume, issue, pages from the seed list), Reinebo et al. (issue number), Vohs et al. (co-authors, volume, pages), Sisk et al. and Macnamara et al. (authors, volume, pages). Gouttebarge et al., Brown & Fletcher, Barrett et al. and Güllich & Barth were confirmed on 18 Nov 2026.
```
Result: PASS
Quote: as Changes 7, 8, 10 and 14. The Reinebo publisher PDF shows no issue number.
Syllabus: No conflict.

## Change 16 (held: Ranehill 2015)
File: unit, section 7
Current:
```
The replication in the course list (Ranehill et al., 2015) could not be opened at its publisher's page, PubMed or DOI address, so it is not verified here and carries no claim.
```
Replacement:
```
None. The six Ranehill fixes stay held.
```
Result: not checked (SAGE client_error; APS page refused). The claim stays marked.
Quote: none.
Syllabus: No conflict. Flag: "F11 (Ranehill) stays open: not opened at SAGE or APS on 18 Nov 2026; the six power-posing fixes stay held and must be redrafted against the filed text. No brief changes."

## Change 17 (held: Hagger 2016; Vohs 2021 in full)
File: unit, section 7
Current:
```
The earlier multilab replication (Hagger et al., 2016) could not be opened and carries no claim.
```
Replacement:
```
None. The Hagger fixes stay held. The Vohs text stays "abstract read".
```
Result: not checked. Search returned no publisher, PubMed or DOI address for either paper.
Quote: none.
Syllabus: No conflict. The contested grade-key example is unchanged. Flag: "F11 (Hagger, Vohs) stays open: no publisher/PubMed/DOI address found on 18 Nov 2026; [contested] rests on the Vohs abstract alone. No brief changes."

## Change 18 (held: Sisk 2018 in full)
File: unit, section 7
Current:
```
([Sisk et al., 2018, abstract read; not verified](https://doi.org/10.1177/0956797617739704))
```
Replacement:
```
None. The two growth-mindset fixes stay held.
```
Result: not checked (SAGE client_error; PubMed reCAPTCHA).
Quote: none.
Syllabus: No conflict. Flag: "F11 (Sisk) stays open; no pooled effect size given. No brief changes."

## Change 19 (F23: Macnamara 2016 in full)
File: unit, section 8
Current:
```
([Macnamara et al., 2016, abstract read](https://doi.org/10.1177/1745691616635591))
```
Replacement:
```
None. No regrade.
```
Result: not checked (no SAGE or PubMed address; APS refused).
Quote: none.
Syllabus: No conflict. Flag: "F23 (Macnamara, SP1) stays open; the 10,000-hour line stays 'no peer-reviewed source found'. Somerville, Sawyer and Güllich et al. (2022) are SP2's. No brief changes."

## New 1
File: files/fresh-check-SP1.md
Current: none (finding about the held fixes, not unit text)
Replacement: none
Result: PASS (finding). A script count shows the held-fix Current strings (e.g. "The original replication in the course list could not be opened for this unit.") occur 0 times in the filed unit.
Quote: n/a
Syllabus: No conflict. Flag: "Held fixes of fresh-check-SP1.md (Hagger/Vohs, Ranehill, Sisk) were written against an earlier SP1 text; when their sources are opened they are redrafted against the filed text, not applied as written. No brief changes."

## Not changed
- Fletcher & Sarkar: abstract and notes again only. Note 7's wording is confirmed. The entry stays marked.
- Abt 2020: not checked; stays marked.
- Reinebo: authors and pages are confirmed. The issue number stays marked.

## Records
The reading page's known gaps should read:
1. Section 6: the review of meta-analyses (Lochbaum et al., 2022) was read in full; it gives no ages for each meta-analysis, and 14 of its 30 meta-analyses pooled correlational studies.
2. Section 7, power posing: rests on Metzler & Grèzes (2019), one randomised test of the hormone claim with a different posture schedule; Ranehill et al. (2015) could not be opened (18 Nov 2026: SAGE page failed).
3. Section 7, ego depletion: graded [contested] on Vohs et al. (2021) read in abstract only (co-authors, volume and pages not verified); Hagger et al. (2016) not opened (18 Nov 2026: no publisher, PubMed or DOI address found).
4. Section 7, grit and growth mindset: Credé et al. (2017) not opened; Sisk et al. (2018) read in abstract only, which gives no pooled effect size, so none is given (18 Nov 2026: SAGE and PubMed could not be opened); grit's overlap with conscientiousness is as Martin et al. (2025) report it, citing earlier work not opened.
5. Section 8, 10,000 hours: Macnamara et al. (2016) read in abstract only (18 Nov 2026: full text not reachable at a publisher, PubMed or DOI address); the 10,000-hour figure as a rule has no peer-reviewed source found. The "strong" worked example rests on one meta-analysis (Güllich & Barth, 2024) and the unit's rule 3.
6. Section 2, scope line: the coach-role Delphi (Bissett et al., 2020) not opened; the five jobs rest on the IOC tools (Gouttebarge et al., 2021, now read in full), one meta-analysis read in abstract (Brown & Fletcher, 2017) and one study. Graded practice.
7. Sources entries with details not shown on a page opened: ironic-effects review (journal, volume, issue, pages), J Sports Sci editorial (authors, headline), tennis imagery meta-analysis (author surnames), Rupprecht et al. (title, authors, year, volume, issue, pages), Reinebo et al. (issue number), Vohs et al., Sisk et al. and Macnamara et al. (authors, volume, pages).
8. Section 8, faces: Barrett et al. (2019) read on the publisher's summary page and in its first part at PubMed Central; the accompanying article is known from the summary page only.
9. Section 8, ironic effects: Bartura et al. (read in full) report 5 experimental and 19 quasi-experimental studies but do not say which experimental studies used athletes, so rule 4 cannot be applied and the claim is graded weak by rule 5; Wegner's original papers not opened.
10. Section 8, amygdala hijack and mental toughness: "no peer-reviewed source found" reflects a short search in a session where most PubMed, PMC and APS pages could not be fetched; a fuller search may find sources.
11. Section 8, harsh coaching: Fletcher & Sarkar (2016) read in abstract and notes only; the Bartholomew et al. reviews (2009, 2011) not opened (DD-SP1, F31).

Flags: F11's Lochbaum part is closable once Changes 1–3 are applied. F11 stays open for Hagger, Vohs (full), Ranehill and Sisk (full). F23 stays open for Macnamara (SP1). F10 was not part of this check.
