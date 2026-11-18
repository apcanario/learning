---
check: corrections C-SP2 (SP2; flags F22, F23, F42), W-SP4, 18 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file); only the fence labels "```Current" and "```Replacement" are written as "Current:" and "Replacement:" lines above a plain fence, so `thin.py correct` can read them
---

Model: claude-opus-5-5

Summary: 9 changes: 7 PASS, 0 FAIL, 2 not checked (Changes 2 and 9); 0 New. Every Current below occurs exactly once in files/SP2-the-developing-athlete-10-to-25.md: a script counted each exact string, and every count was 1. No brief changes. Checks dated 18 Nov 2026.

Conditions of this check:
- The session's permission classifier refused several WebFetch calls, each counted not checked and not retried:
  - www.doi.org for Cobley;
  - pubmed.gov and PMC for Boccia's correction;
  - mdpi.com for Albaladejo-Saura.
- doi.org for Boccia returned a 302 redirect to journals.plos.org: not checked, not followed.
- PubMed served a reCAPTCHA page for Güllich et al. (2022).

On copies: Changes 3 to 5 and 7 to 8 rest on copies of the published PDFs on university sites, not the publisher's page. The unit already does the same for the NSCA statement, read on the NSCA's own server. Each replacement names the copy's address and says it is not the publisher's page. If the applier holds that (d) requires the publisher's page, do not apply these five; the claims then stay as filed, and nothing else depends on them.

## Change 1
File: files/SP2-the-developing-athlete-10-to-25.md (Sources, Boccia et al., 2017). Correction (f).
Current:
```
its PubMed record checked (address not recorded), which says only that it corrects this article; its content not read)
```
Replacement:
```
its content not read; the article's authors, volume and issue are not verified)
```
Result: PASS
Quote: sourcing-standard.md Part 7: "with the address opened, what was read (abstract or full text) and the date". The PubMed check has no recorded address, so it is dropped. The article was never opened, so its authors, volume and issue are marked not verified. This check could not open it either (doi.org redirected; PMC and PubMed were refused).
Syllabus: no conflict. The SP2 brief does not name Boccia.

## Change 2
File: files/SP2-the-developing-athlete-10-to-25.md (Sources, Lorenz & Kray, 2022). Correction (f).
Current:
```
2022;51(9):1693–1707 (volume and pages not verified)
```
Replacement:
```
2022;51(9):1693–1707 (issue not verified)
```
Result: not checked. Do not apply; the entry stays as filed.
Quote: none. No search returned the link.springer.com page. The Saarland repository PDF that search did return (https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/33069/1/Lorenz-Kray2022_Article_ExploreWithMePeerObservationDe.pdf) shows the journal and DOI but no volume, issue or pages.
Syllabus: no conflict.
Flag text: "SP2 Sources, Lorenz & Kray (2022): quality review e saw volume 51 and pages 1693–1707 at link.springer.com; C-SP2's check could not reach that page, so the entry still marks volume and pages not verified. Open the publisher's page at the next corrections pass and apply 'issue not verified'."

## Change 3
File: files/SP2-the-developing-athlete-10-to-25.md (section 9, "The 10,000 hours, tested"). Correction (b).
Current:
```
[Macnamara et al., 2016, abstract read](https://doi.org/10.1177/1745691616635591)
```
Replacement:
```
[Macnamara et al., 2016](https://doi.org/10.1177/1745691616635591)
```
Result: PASS. The full text, on the copy named in Change 5, confirms:
- 18% of the variance overall;
- the 1% among elite-level performers, verbatim;
- no earlier start for high-level athletes: a non-significant 0.11 years, from 24 effect sizes, N = 1,477.

The section 9 grade rests on Güllich et al. (2022), so there is no regrade.
Quote: see Change 4 (one quote per source).
Syllabus: no conflict. Under the unit's convention, a source read in full carries no "abstract read" mark.

## Change 4
File: files/SP2-the-developing-athlete-10-to-25.md (section 9). Correction (b).
Current:
```
The abstract does not mention 10,000 hours.
```
Replacement:
```
The paper mentions 10,000 hours only in describing an earlier study of violinists, not as a finding of its own.
```
Result: PASS
Quote: "had accumulated over 10,000 hr of deliberate practice" (Macnamara et al., 2016, full text, describing the earlier violinist study)
Syllabus: no conflict. The brief asks for "early specialisation against sampling, from ... the studies of who becomes a champion". The unit's conclusion is unchanged: no opened source states 10,000 hours as a threshold.

## Change 5
File: files/SP2-the-developing-athlete-10-to-25.md (Sources, Macnamara et al., 2016). Correction (b).
Current:
```
(abstract read at the journal's page, https://www.psychologicalscience.org/journals/perspectives/1745691616635591/, 17 Nov 2026; that page shows no authors, volume, pages or DOI, which are from Crossref)
```
Replacement:
```
(abstract read at the journal's page, https://www.psychologicalscience.org/journals/perspectives/1745691616635591/, 17 Nov 2026; full text read on a copy of the published PDF, https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2016-the-relationship-between-deliberate-practice-and-performance-in-sports-a-meta-analysis.pdf, not the publisher's page, 18 Nov 2026, which gives the authors, volume, issue, pages and DOI as above)
```
Result: PASS. The PDF gives Macnamara BN, Moreau D, Hambrick DZ; *Perspectives on Psychological Science* 2016;11(3):333–350; 10.1177/1745691616635591. All match the entry.
Quote: see Change 4.
Syllabus: no conflict.

## Change 6
File: files/SP2-the-developing-athlete-10-to-25.md (Sources, Güllich et al., 2023). Correction (d).
Current:
```
(abstract and results read at the publisher's page, link.springer.com, 17 Nov 2026)
```
Replacement:
```
(full text read at the publisher's page, https://link.springer.com/content/pdf/10.1007/s40279-023-01840-1.pdf, 18 Nov 2026; the 7.2% and 92.8% figures are taken from its abstract, as the figure behind them was not seen)
```
Result: PASS. The full text confirms:
- 110 prospective samples (38,383 juniors) and 79 retrospective samples (22,961 seniors);
- "largely two disparate populations";
- the authors, *Sports Medicine* 53:1201–1217 and the DOI;
- a pooling of counts and percentages, not a meta-analysis of effect sizes, so [weak, rule 5] stands.

"7.2% identical and 92.8% disparate" is in the abstract; the body's Figure 3 was not in the text seen.
Quote: "Prospective studies included 110 samples with 38,383 junior athletes."
Syllabus: no conflict.

## Change 7
File: files/SP2-the-developing-athlete-10-to-25.md (section 5). Correction (d).
Current:
```
[Crone & Dahl, 2012, abstract and key points read](https://doi.org/10.1038/nrn3313)
```
Replacement:
```
[Crone & Dahl, 2012](https://doi.org/10.1038/nrn3313)
```
Result: PASS. The full text, on the copy named in Change 8, supports the section's account:
- prefrontal studies "show both increases and decreases in activation";
- adolescents consistently show increased striatal activation to reward;
- subcortical activation peaks in mid-adolescence;
- the model's flexibility is "generally adaptive", with vulnerabilities in some incentive situations.

One reservation, not a change: on social feedback (social rejection) the full text is more mixed than on reward. The unit's list follows the abstract and key points, which quality review e confirmed.
Quote: "developmental neuroimaging studies do not support a simple model of frontal cortical immaturity"
Syllabus: no conflict.

## Change 8
File: files/SP2-the-developing-athlete-10-to-25.md (Sources, Crone & Dahl, 2012). Correction (d).
Current:
```
https://doi.org/10.1038/nrn3313 (abstract and key points read at the publisher's page, 17 Nov 2026)
```
Replacement:
```
https://doi.org/10.1038/nrn3313 (abstract and key points read at the publisher's page, 17 Nov 2026; full text read on a copy of the published PDF, https://developingadolescent.semel.ucla.edu/assets/uploads/research/resources/publicatie_Nature_Eveline_Crone_2012.pdf, not the publisher's page, 18 Nov 2026)
```
Result: PASS. The copy gives volume 13, first page 636 and DOI 10.1038/nrn3313. It shows no issue number; the entry already marks the issue not verified.
Quote: see Change 7.
Syllabus: no conflict.

## Change 9
File: files/SP2-the-developing-athlete-10-to-25.md (section 3). Correction (a).
Current:
```
[Cobley et al., 2009, abstract read; not verified, because the DOI address later redirected](https://doi.org/10.2165/00007256-200939030-00005)
```
Replacement:
```
none: stays as filed
```
Result: not checked. Two searches returned no publisher (Springer/Adis) or PubMed address, only catalogue records. The www.doi.org address that search did return was refused by the permission classifier (not retried). No male-sport effect size is added. Section 3's bracket and Deliverable A keep Cobley marked not verified.
Quote: none.
Syllabus: no conflict.
Flag text: "F22 stays open: Cobley et al. (2009) not opened at C-SP2 (no publisher or PubMed address returned by search; DOI fetch refused). Open at the publisher's page at SP2's next corrections pass and add the male-sport effect if the text gives it."

## Not changed: checked or not reachable

- (b) Somerville (2016) and Sawyer et al. (2018): searches returned no cell.com or thelancet.com page, only catalogues and press. Not opened; section 4 already says so; no regrade.
- (b) Güllich et al. (2022): no full text returned, and PubMed gave reCAPTCHA. Stays "abstract read" with the moderate grade as filed.
- F23 stays open for Güllich et al. (2022), Somerville (2016) and Sawyer et al. (2018).
- (c) Boccia et al. (2017) and its correction e0178662: not opened (doi.org redirected; PMC5441632 and pubmed.gov/28542583 refused). Section 10, Deliverable A (13 to 15) and the Milan and Sara notes stay marked not verified as filed. Quality review e's three wording fixes are already in the unit. F42 stays open for Boccia.
- (d) Albaladejo-Saura et al. (2021): mdpi.com fetch refused. Stays "abstract read".
- (d) Arain et al. (2013): the dovepress full-text address served the abstract only. Fields 9:449–461 and the DOI are confirmed, and no end age is named ("Adolescence is the developmental epoch during which children become adults"). Stays "abstract read".
- (d) Foulkes & Blakemore (2018): search returned only an accepted-manuscript repository copy. Not opened; stays as filed.
- (d) Smith et al. (2018): springermedizin.de served the abstract only (login wall). OR 1.25 (1.21 to 1.30) confirmed. Stays "abstract read".
- (e) IOC: https://bjsm.bmj.com/content/49/13/843.full opened in full.
  - It cites ref. 43 for sleep: "with a recommended optimal level of sleep of 8.5–9.5 h.43".
  - It cites a single reference, ref. 30, for girls' cycling peak power to about 12.
  - The page's reference list was empty, so neither cited work could be identified or opened. Both stay marked (unsure list items 3 and 10).

## Records

Reading page, SP2, known gaps. This text replaces the SP2 entries. If Changes 3 to 8 are not applied, keep Crone & Dahl, Macnamara et al. and Güllich et al. (2023) listed as read in abstract.

"Known gaps (corrections check C-SP2, 18 Nov 2026):
- Relative age in male sport: Cobley et al. (2009) read only in abstract and not verified; no size of the effect in male sport is given.
- Boccia et al. (2017), the jumping-events study, and its published correction were not opened. Nothing in the unit rests on them, and where they are named they are marked not verified.
- Somerville (2016) and Sawyer et al. (2018) were not opened; the '25' claim is examined without them.
- Read in abstract only:
  - Güllich et al. (2022): the moderate grade for multi-sport practice was set without its intervals or study quality;
  - Albaladejo-Saura et al. (2021);
  - Arain et al. (2013);
  - Foulkes & Blakemore (2018), whose quotation the latest checks have not verified;
  - Smith et al. (2018).
- The IOC statement's sources for 8.5 to 9.5 hours of adolescent sleep (its ref. 43) and for girls' cycling peak power to about 12 (its ref. 30) were not opened.
- Lorenz & Kray (2022): volume and pages not verified.
- Not opened here, and left to later units: Malina et al. (2015), DD-SP2; Park et al. (2013), SP10; Walsh et al. (2021), SP8; emotion regulation from 16 to 25, SP4."

Source tally:
- Opened in full (5):
  - Güllich et al. 2023, Springer PDF;
  - Bergeron et al. 2015, bjsm full page, references not shown;
  - Macnamara et al. 2016, Purdue copy;
  - Crone & Dahl 2012, UCLA copy;
  - Lorenz & Kray 2022, Saarland repository PDF, which showed no volume or pages.
- Abstract only (2): Arain et al. 2013, dovepress; Smith et al. 2018, springermedizin.
- Not opened (10): Cobley; Boccia; Boccia's correction; Somerville; Sawyer; Güllich et al. 2022; Albaladejo-Saura; Foulkes & Blakemore; IOC ref. 43; IOC ref. 30.
