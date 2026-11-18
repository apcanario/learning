---
check: corrections check of the findings of quality-review-SP2-2026-11-18.md, W-SP4, 18 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file)
---

Model: claude-opus-5-5
Summary: 12 changes. 5 PASS (6, 7, 8, 9, 10). 2 FAIL, each with an Alt (11, 12). 5 not checked and not applied (1–5), because the doi.org fetches were refused. 0 New. 1 Records item. No file was changed; the working folder was only read. Every Current occurs exactly once in files/SP2-the-developing-athlete-10-to-25.md (checked by script).

## Change 1
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
([Cobley et al., 2009, abstract read; not verified, because the DOI address later redirected](https://doi.org/10.2165/00007256-200939030-00005))
```
Replacement:
```
([Cobley et al., 2009, abstract read](https://doi.org/10.2165/00007256-200939030-00005))
```
Result: FAIL (not checked). A WebSearch returned https://www.doi.org/10.2165/00007256-200939030-00005, but the WebFetch of it was refused (permission denied). By the web rule I did not retry it or fetch a copy. The claim stays marked as it is. Not applied.
Quote: none (source not opened)
Syllabus: no brief conflict. F22 (open) asks for Cobley to be opened at SP2's next corrections pass. Flag text: "C-SP2 quality-review Changes 1–4 (Cobley et al., 2009) held: the DOI address could not be fetched by the verifying agent on 18 Nov 2026; F22 stays open."

## Change 2
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
in sport overall it rests on Cobley et al. (2009), which is not verified, so it carries no grade]
```
Replacement:
```
in sport overall, moderate (Cobley et al., 2009: one meta-analysis in athletes, read in abstract, which calls the effects small and gives no pooled figure, rule 4)]
```
Result: FAIL (not checked). It depends on Change 1, and the source was not opened. Not applied.
Quote: none
Syllabus: same as Change 1 (F22).

## Change 3
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
the same in sport overall (Cobley et al., 2009) is not verified;
```
Replacement:
```
moderate in sport overall (Cobley et al., 2009);
```
Result: FAIL (not checked). It depends on Change 1. Not applied.
Quote: none
Syllabus: same as Change 1. The SP2 brief requires each table cell to be graded, and the current text already says Cobley is not verified, so leaving it unchanged is consistent with the brief.

## Change 4
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
(abstract read at the DOI address, 17 Nov 2026; on a later attempt the DOI address redirected, so the abstract's content and the authors, volume, issue and pages are not verified)
```
Replacement:
```
(abstract read at the DOI address, 17 Nov 2026, and again by the quality review, 18 Nov 2026, which confirmed its content, the first three authors, volume, issue and pages)
```
Result: FAIL (not checked). The DOI fetch was refused, so the confirmation cannot be stated. Not applied.
Quote: none
Syllabus: same as Change 1.

## Change 5
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
its content not read; the article's authors, volume and issue are not verified)
```
Replacement:
```
its content not read for this unit; the first six authors, volume, issue and article number confirmed at the DOI address by the quality review, 18 Nov 2026)
```
Result: FAIL (not checked). A search returned https://doi.org/10.1371/journal.pone.0170744, but the WebFetch was refused (permission denied). I did not retry it and did not use the repository copies (UCL, RePEc) instead. Not applied.
Quote: none
Syllabus: no brief conflict. Unsure-list item 11 and F42 stay as they are. Flag text: "Boccia et al. (2017) metadata still not confirmed at its DOI address (fetch refused 18 Nov 2026)."

## Change 6
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
40 adolescents aged 11 to 18 and 24 adults aged 20 to 38 (28 recruited, 4 excluded)
```
Replacement:
```
40 adolescents aged 11 to 18 and 24 adults (28 recruited, aged 20 to 38; 4 excluded)
```
Result: PASS. The full text was opened at https://www.frontiersin.org/articles/10.3389/fpsyg.2014.01476/pdf. The 20–38 range belongs to the 28 adults recruited. Four were excluded, and the analysis has F(1, 62), which fits 40 + 24.
Quote: "28 adults (14 females; aged 20–38; M = 25.07, SD = 4.65)"
Syllabus: no conflict with any brief, filed unit or the register.

## Change 7
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
"accounted for only 1% of the variance in performance among elite-level performers";
```
Replacement:
```
"accounted for only 1% of the variance in performance among elite-level performers" (an estimate the full text bases on six effect sizes from 228 athletes);
```
Result: PASS. Opened https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2016-the-relationship-between-deliberate-practice-and-performance-in-sports-a-meta-analysis.pdf, a copy of the published PDF. Table 1 has the row "Elite 6 228". The paper says "participants"; they are elite sports performers, so "athletes" is accurate.
Quote: "elite category in the present meta-analysis: effect sizes = 6, N = 228"
Syllabus: no conflict. SP1 §8 gives the same 1% figure without a sample, and the change leaves SP1 untouched.

## Change 8
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
The paper mentions 10,000 hours only in describing an earlier study of violinists, not as a finding of its own.
```
Replacement:
```
In its full text, read on a copy of the published PDF, not the publisher's page, the paper mentions 10,000 hours only in describing an earlier study of violinists.
```
Result: PASS. Same copy as Change 7. The paper uses "10,000" twice. One is the violinists (Ericsson et al., 1993). The other is "over 10,000 twins" (Mosing et al., 2014), which is not hours. Neither is a finding of the meta-analysis.
Quote: "the 'best' violinists had accumulated over 10,000 hr of deliberate practice"
Syllabus: no conflict.

## Change 9
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
[weak; IOC consensus summary (Bergeron et al., 2015), rule 5]
```
Replacement:
```
[weak; IOC consensus summary (Bergeron et al., 2015), rule 5; inference]
```
Result: PASS against SP1's key, which is the basis the reviewer cited. SP2's unsure-list item 10 says the growth studies are outside the athlete populations. The cell applies them to 10- to 12-year-olds. The IOC statement opened at https://www.sportaus.gov.au/__data/assets/pdf_file/0004/689647/IOC_consensus_statement_on_youth_athletic_development.pdf (a copy) does say what the cell attributes to it.
Quote: SP1 key: "added whenever the grade comes from adults, students or non-athletes and is applied to an athlete under 18". IOC: "Girls often outscore boys until ∼12 years of age"
Syllabus: no brief conflict. It is consistent with F8 (SP1's key used unchanged) and does not touch F48.

## Change 10
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
2015;49(13):843–851 (last page not verified).
```
Replacement:
```
2015;49(13):843–851 (pages as printed on a copy of the statement).
```
Result: PASS. The sportaus.gov.au copy prints the volume and the pages. The British Library record https://eld.bl.uk/catalog/100139398785_0x000001, returned by search, gives volume 49, issue 13, 2015-06-17, pages 843–851.
Quote: "Br J Sports Med 2015;49:843–851."
Syllabus: no conflict. It matches the seed bibliography entry C1.

## Change 11
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
2022;51(9):1693–1707 (volume and pages not verified).
```
Replacement (reviewer's):
```
2022;51(9):1693–1707 (volume not verified).
```
Alt:
```
2022;51(9):1693–1707 (issue and pages from an index record, https://ouci.dntb.gov.ua/works/4NrMaE84; volume not verified).
```
Result: FAIL, with the Alt proposed. The OUCI record (returned by search, then opened) gives issue 9 and pages 1693–1707, with no volume. It is an index record, not the publisher's or Crossref's record that sourcing standard Part 7 requires. Dropping "pages not verified" with no qualifier overstates what was checked. The Alt says what was actually opened. Not applied; the Alt would need its own pass.
Quote: "№ 9" … "1693-1707" (OUCI record; volume not stated)
Syllabus: no conflict.

## Change 12
File: files/SP2-the-developing-athlete-10-to-25.md
Current:
```
were "7.2% identical and 92.8% disparate"
```
Replacement (reviewer's):
```
were "7.2% identical and 92.8% disparate" (figures from its abstract; the full text does not show the calculation)
```
Alt:
```
were "7.2% identical and 92.8% disparate" (figures from its abstract; the figure behind them was not seen)
```
Result: FAIL, with the Alt proposed. I opened https://link.springer.com/content/pdf/10.1007/s40279-023-01840-1.pdf, returned by search. The figures are in the abstract. The full text does give the formula (section 2.2) and the inputs: 10.8% prospective and 18.0% retrospective in the text and Table 4. The pair itself is shown only in Figure 3, which is an image. So "the full text does not show the calculation" overreaches. The Alt uses the wording the Sources entry already has. Not applied.
Quote: "international-level U17/18 juniors and international-level seniors were 7.2% identical"
Syllabus: no conflict.

## Records
If Change 9 is applied, append to SP2's reading-page known gaps, unsure-list item 10:
```
Quality review (W-SP4, 18 Nov 2026): the cell now carries the label inference, by SP1's key.
```
No other Records change, because Changes 1–5 are not applied and items 4 and 11 stay as they are.

Flags for the next syllabus review:
- F22 stays open. "Cobley et al. (2009) could not be fetched at its DOI address by the verifying agent on 18 Nov 2026 (refused). Quality-review Changes 1–4 are held until it is opened."
- "Boccia et al. (2017) Sources-entry metadata change held: DOI address fetch refused 18 Nov 2026."
