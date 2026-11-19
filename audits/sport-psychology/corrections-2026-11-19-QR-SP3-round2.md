---
check: round 2 corrections check of the alternatives of corrections-2026-11-19-QR-SP3.md, W-DD-SP2, 19 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file)
note: the agent's Change N is the item N of its packet (round 1 was Change 1, 2, 6, 7, 10, 11, 12, then New 2, New 3); round 1's Change 9 stays as written, not listed
---

Model: claude-opus-5-5
Totals: I checked 9 items. 8 pass (1, 2, 3, 4, 5, 6, 7, 8) and 1 fails with an Alt (9). I propose 6 new changes:
- New 1 and New 2 must go in for Change 2 to pass.
- New 3 and New 4 must go in for Changes 6 to 9.
- New 5 and New 6 are optional; they came out of checking item 5.

A script counted every Current: each occurs exactly once in files/SP3-motivation-and-the-climate-you-create.md and 0 times in SP1.

Web: I ran WebSearch first, then WebFetch only on URLs a search returned, on 19 Nov 2026.
- Opened:
  - the copy of Deci et al. 1999 at leeds-faculty.colorado.edu/dahe7472/deci%201999.pdf;
  - the authors' manuscript of Bartholomew et al. 2009 (research.birmingham.ac.uk/files/2920310/...pdf) and its University of Birmingham record;
  - the copy of Meeusen et al. 2013 (sportgeneeskunde.com/...ECSS-ACSM.pdf), both parts of the file;
  - Smoll et al. 2007 (jyd.pitt.edu/ojs/jyd/article/view/358/344);
  - the copy of Mossman et al. (selfdeterminationtheory.org/.../InPress_MossmanSlempEtAl_Autonomy.pdf).
- Not checked: the University of Melbourne record of Mossman et al., which served a bot check.

## Change 1
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
practice, for the reward rule alone, which no study opened tests, rule 2]
```
Replacement:
```
weak, positive, for the reward rule alone: tested only in laboratory or laboratory-like experiments with children and college students, none described as in sport (Deci et al., 1999), rule 5; for athletes, inference]
```
Result: PASS. What the copy shows:
- The studies were run in the laboratory or under laboratory-like conditions.
- Participants are coded as children or college students.
- The one physical task is a balance board (Orlick and Mosher, 1978), and the paper does not describe it as sport.
- Tangible rewards lowered intrinsic motivation, so the direction is positive for the rule.
- Rule 5 and the inference label follow SP1 section 9.
Quote: "either in the laboratory or under well-controlled, laboratory-like conditions" (Deci et al., 1999, leeds-faculty.colorado.edu copy)
Syllabus: no conflict. Flag F35 says SP3 states no effect of rewards; this change overtakes it, and the filer should note that.

## Change 2
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
the two reviews by Bartholomew and colleagues (2009, 2011) could not be opened at a publisher's page, PubMed or a DOI address, and nothing is reported from them.
```
Replacement:
```
the 2011 paper by Bartholomew and colleagues could not be opened, and nothing is reported from it. The 2009 review was read in full on the authors' manuscript in the University of Birmingham's repository, not the publisher's version (quality review and corrections check, 19 Nov 2026). It is a literature review of the parental, educational and, to a lesser extent, sport literatures that proposes a preliminary taxonomy of six controlling strategies: tangible rewards, controlling feedback, excessive personal control, intimidation, promoting ego-involvement (including public evaluation and normative comparison) and conditional regard. It notes a lack of extensive empirical research on these strategies, calls for longitudinal studies, and states that there had been no empirical research on conditional regard in sport ([Bartholomew et al., 2009, author manuscript read](https://doi.org/10.1080/17509840903235330)). It adds no controlled test, so the grade below stands.
```
Result: PASS, but only together with New 1 and New 2.
- Every fact holds on the manuscript:
  - "literature review of the relevant parental, educational, and to a lesser extent, sport literatures";
  - "preliminary taxonomy of six controlling strategies", with the six headings as listed;
  - ego-involving environments "stress competition, public evaluation, normative comparisons";
  - "Further research, in particular longitudinal studies, is also needed";
  - the DOI is printed.
- New 1 is needed because the source is not in Sources.
- New 2 is needed because note 6 would otherwise contradict it.
Quote: "the lack of extensive empirical research on coaches' controlling motivational strategies"; "no empirical research on the use of conditional regard in the context of sport" (research.birmingham.ac.uk/files/2920310)
Syllabus: no conflict. Flags F5, F31 and F184 still say the 2009 review is unopened; the filer updates them, and no brief changes.

## Change 3
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
*Medicine & Science in Sports & Exercise* 2013 (first page 186).
```
Replacement:
```
*Medicine & Science in Sports & Exercise* 2013;45(1):186–205.
```
Result: PASS. The copy's footers run from 186 to 205, and the article code 4501-0186 gives volume 45, issue 1. Apply it together with Change 4, which says where these numbers came from.
Quote: "0195-9131/13/4501-0186/0"; last footer "Medicine & Science in Sports & Exercise 205" (sportgeneeskunde.com copy)
Syllabus: no conflict

## Change 4
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
volume, issue and last page not verified;
```
Replacement:
```
volume 45 and issue 1 read from the copy's article code (0195-9131/13/4501-0186) and pages 186 to 205 from its page footers, by the corrections check, 19 Nov 2026, not the publisher's record;
```
Result: PASS. The copy has no "Vol." or "No." label. Footers 186 to 205 are confirmed across both parts of the file.
Quote: "0195-9131/13/4501-0186/0" (sportgeneeskunde.com copy, first page)
Syllabus: no conflict

## Change 5
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
adds two behaviours to avoid: withholding reinforcement for effort, and punishing mistakes
```
Replacement:
```
adds, among other behaviours to avoid, withholding reinforcement for effort, punishing mistakes, and giving instruction in a hostile, demeaning, harsh, sarcastic or degrading manner
```
Result: PASS. It is a paraphrase, with no quotation marks.
- The source names "nonreinforcement of positive behaviors and effort" and "mistake-contingent punishment".
- Its Don'ts list corrective instruction "in a hostile, demeaning, or harsh manner" and instruction "in a sarcastic or degrading manner".
- The same Don'ts include "Don't use physical measures, such as running laps", which bears on section 4's grade for exercise as punishment: see New 5 and New 6.
Quote: "Give corrective instruction in a hostile, demeaning, or harsh manner." (jyd.pitt.edu/ojs/jyd/article/view/358/344, Appendix A)
Syllabus: no conflict

## Change 6
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
Meta-analysis of 131 samples in sport and exercise; correlational; ages not in abstract (
```
Replacement:
```
Meta-analysis of 131 samples in sport and exercise; correlational; abstract and a copy of the published article read; sample ages not reported (
```
Result: PASS. The copy gives no summary of sample ages; its only age figure is the correlation between age and autonomy support (k = 6). Apply it with Changes 7 to 9 and New 3.
Quote: "We found no evidence of moderation based on athletes' age" (selfdeterminationtheory.org copy)
Syllabus: no conflict

## Change 7
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
if they are mainly exercisers, rule 5 makes it weak; no causal claim.]
```
Replacement:
```
if they are mainly exercisers, rule 5 makes it weak; no causal claim. A copy of the published online-first article (https://selfdeterminationtheory.org/wp-content/uploads/2022/02/InPress_MossmanSlempEtAl_Autonomy.pdf, not the publisher's page, read by the quality review and the corrections check, 19 Nov 2026) reports no rating of the primary studies' quality, heterogeneity of I² = 86% for autonomous motivation, no moderation by athletes' age or by whether a study took place in a sport or an exercise context, and no share of athlete and exerciser samples; rule 3 cannot be met, so the grade is moderate.]
```
Result: PASS.
- The cover page is Taylor & Francis's, with DOI 10.1080/1750984X.2022.2031252 and "Published online: 02 Feb 2022".
- There is no rating of study quality or risk of bias.
- I² = 86% for autonomous motivation (k = 66, Table 1).
- Moderation by age and by sport or exercise context was tested and not found.
- No counts of athlete and exerciser samples are given.
- Rule 3 fails on study quality and rule 4 gives moderate. The bracket keeps its condition about exercisers, and it agrees with Changes 8 and 9.
Quote: "or whether the study took place in a sport or an exercise context" (selfdeterminationtheory.org copy)
Syllabus: no conflict

## Change 8
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
one meta-analysis read in abstract, its sensitivity analyses and study quality not seen, rule 4
```
Replacement:
```
one meta-analysis, read in abstract and on a copy of the published article, which labels no analysis as a sensitivity analysis and rates no study quality, rule 4
```
Result: PASS. No analysis is labelled a sensitivity analysis. Publication bias was checked by comparing published with unpublished studies and by Egger's test. No study quality is rated. It agrees with Change 7.
Quote: "Results showed little evidence for publication bias." (selfdeterminationtheory.org copy)
Syllabus: no conflict

## Change 9
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
(abstract read at the publisher's page, https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252, 17 Nov 2026; authors, volume, issue, pages and year not verified: taken from the course's seed list, not shown on the page opened)
```
Replacement:
```
(abstract read at the publisher's page, https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252, 17 Nov 2026; full text read on a copy of the published online-first article, https://selfdeterminationtheory.org/wp-content/uploads/2022/02/InPress_MossmanSlempEtAl_Autonomy.pdf, not the publisher's page, by the quality review and the corrections check, 19 Nov 2026, which shows the authors, title, journal, DOI and online date of 2 February 2022; volume, issue and pages, shown on neither page, taken from the course's seed list and not verified)
```
Result: FAIL.
- The copy shows the authors, title, journal, DOI and "Published online: 02 Feb 2022", as stated.
- The issue year 2024 in the Sources entry is shown on neither page.
- The Proposed text drops "year" from what is unverified, so 2024 would stand as checked.
- The University of Melbourne record served a bot check and was not checked.

Alt:
```
(abstract read at the publisher's page, https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252, 17 Nov 2026; full text read on a copy of the published online-first article, https://selfdeterminationtheory.org/wp-content/uploads/2022/02/InPress_MossmanSlempEtAl_Autonomy.pdf, not the publisher's page, by the quality review and the corrections check, 19 Nov 2026, which shows the authors, title, journal, DOI and online date of 2 February 2022; volume, issue, pages and the issue year 2024, shown on neither page, taken from the course's seed list and not verified)
```
Quote: "Published online: 02 Feb 2022" (selfdeterminationtheory.org copy, cover page; no volume, issue or pages)
Syllabus: no conflict

## New 1
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
- Bergeron MF, Mountjoy M, Armstrong N, et al.
```
Replacement:
```
- Bartholomew KJ, Ntoumanis N, Thøgersen-Ntoumani C. A review of controlling motivational strategies from a self-determination theory perspective: implications for sports coaches. *International Review of Sport and Exercise Psychology* 2009;2(2):215–233. https://doi.org/10.1080/17509840903235330 (full text read on the authors' manuscript, https://research.birmingham.ac.uk/files/2920310/Ntoumanis_2009_International_Review_of_Sport_and_Exercise_Psychology.pdf, not the publisher's version, by the quality review and the corrections check, 19 Nov 2026; author order from the manuscript's title page; journal, volume, issue, pages and DOI from the University of Birmingham's research record, https://research.birmingham.ac.uk/en/publications/a-review-of-controlling-motivational-strategies-from-a-self-deter, which lists the authors in a different order, not the publisher's record)
- Bergeron MF, Mountjoy M, Armstrong N, et al.
```
Result: PASS. Change 2 needs it: Part 1 and Part 7 require every cited source to be in Sources with its source log. Skip it if a round-1 change already added the entry. The initials "KJ" are not verified, because the manuscript gives only "Kimberley Bartholomew"; use "Bartholomew K" if the filer cannot confirm them.
Quote: "Volume: 2 · Issue: 2 · Pages: 215-233 · DOI: 10.1080/17509840903235330" (research.birmingham.ac.uk record)
Syllabus: no conflict

## New 2
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
Bartholomew et al. (2009, 2011) could not be opened at a publisher's page, PubMed or a DOI address; the harsh-coaching regrade
```
Replacement:
```
Bartholomew et al. (2011) could not be opened; the 2009 review was read on the authors' manuscript, not the publisher's version, and adds no controlled test; the harsh-coaching regrade
```
Result: PASS. Change 2 needs it, so that note 6 no longer says the 2009 review was unopened.
Quote: "A limitation of this paper is the lack of extensive empirical research" (research.birmingham.ac.uk/files/2920310)
Syllabus: no conflict

## New 3
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
Mossman et al. was read in abstract only; the ages of its samples and the share of athletes are unknown, and the "moderate" grade was set without seeing sensitivity analyses or study quality.
```
Replacement:
```
Mossman et al. was read in abstract and on a copy of the published online-first article, not the publisher's page; it reports no sample ages, no share of athletes and exercisers, no analysis labelled a sensitivity analysis and no rating of study quality, so rule 3 cannot be met and the grade is moderate, or weak if its samples are mainly exercisers.
```
Result: PASS. Changes 6 to 8 need it, so that note 4 no longer says the article was read in abstract only.
Quote: "Published online: 02 Feb 2022" (selfdeterminationtheory.org copy)
Syllabus: no conflict

## New 4
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
Mossman et al. (authors, volume, pages from the seed list)
```
Replacement:
```
Mossman et al. (volume, issue, pages and issue year from the seed list; authors shown on a copy of the published online-first article, not the publisher's page)
```
Result: PASS. Change 9 needs it, so that note 1 agrees with the source log.
Quote: "Lara H. Mossman, Gavin R. Slemp, Kelsey J. Lewis, Rachel H. Colla & Paul O'Halloran" (selfdeterminationtheory.org copy)
Syllabus: no conflict

## New 5
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
Do not use exercise as punishment [practice; no study opened tests it; the qualitative accounts are from adults, so for under-18s inference]
```
Replacement:
```
Do not use exercise as punishment [weak, positive, for the package: the coach programme in section 3, tested as a whole, told coaches "Don't use physical measures, such as running laps." (Smoll et al., 2007), rule 5; the guideline alone untested; ages 9 to 15, so for 16 to 25 inference; the qualitative accounts are from adults]
```
Result: PASS. This is optional and came out of checking item 5. Rule 2 does not fit: the package that was tested included this guideline, as it included the punishing-mistakes guideline, which the paragraph just above grades weak for the package. Apply it with New 6.
Quote: "Don't use physical measures, such as running laps." (jyd.pitt.edu/ojs/jyd/article/view/358/344, Appendix A)
Syllabus: no conflict. DD-SP1's brief covers exercise as punishment, but the packet has no filed DD-SP1 unit to compare against.

## New 6
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
| C6 | Uses exercise as punishment | Adams 2024; [practice] |
```
Replacement:
```
| C6 | Uses exercise as punishment | Smoll 2007; Adams 2024; [weak, for the package] |
```
Result: PASS. This is optional and goes in only with New 5, so that the self-audit row agrees with section 4, as row C5 already does.
Quote: "Don't use physical measures, such as running laps." (jyd.pitt.edu/ojs/jyd/article/view/358/344, Appendix A)
Syllabus: no conflict
