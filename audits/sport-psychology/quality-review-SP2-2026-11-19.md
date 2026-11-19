---
code: SP2
kind: quality-review (rule 13)
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgR35wf5wmG58AbjrCFw
note: report returned as the agent reply (harness blocked its file write) and saved verbatim by the chat
---

claude-opus-5-5

# Quality review: SP2 · The developing athlete, 10 to 25

Rule 13 quality review (flag F177). Fresh agent, live search, 19 Nov 2026. Unit read as it stands in files/; not edited.

"Opened" below means read at the publisher's page, PubMed or the DOI address, as agent-rules.txt and the brief require. A reading on a repository copy, library record or database record is reported as "not opened" and gives no PASS, even where the copy matches the unit.

References: 27 Sources entries. Opened 19: Albaladejo-Saura (MDPI), Arain (Dove Press), Bergeron (BJSM), Crone & Dahl (Springer page), Foulkes & Blakemore (Springer page), Gallant & Bélanger (Frontiers), Ghadirzadeh (elsevier.es), Güllich & Barth (Springer PDF), Güllich et al. 2023 (Springer PDF), Güllich et al. 2022 (APS journal page, abstract), Haddad (Frontiers), Lloyd (NSCA's own server), Paruthi 2016 (PubMed), Paruthi 2016b (AASM), Sanchis-Sanchis (Frontiers), Smith (springermedizin.de, abstract), Tervo-Clemmens (nature.com), Tzioumakis (Frontiers), Watson (AASM, dual-published JCSM version). Not opened 8: Bethlehem, Macnamara, Stambulova and Lorenz & Kray (read only on copies of the published articles, all matching the unit); Somerville and Sawyer (library records only; PubMed served reCAPTCHA); Cobley and Boccia (the DOI addresses redirected; not followed, not retried).

## 1. Claims: PASS
Every claim checked against an opened source holds; no claim was found wrong. The claims that rest on the 8 references not opened are listed under "Could not verify".

## 2. Bibliography: PASS
No field error was found in any entry that could be opened. Fields that could not be checked (Bergeron pages, Güllich et al. 2022 volume and pages, Smith volume and pages, Lorenz & Kray volume, Stambulova online date, Crone & Dahl issue) are listed under "Could not verify". The unit already marks the last two as not verified.

## 3. Source log: FIX
Every abstract-only claim says so. Somerville (2016), Sawyer et al. (2018) and Boccia et al. (2017) were never opened at a publisher's page, PubMed or DOI address, yet claims rest on them. The brief says such a reference "carries no claim" (flags F23 and F42, both open).

## 4. Grades: FIX
All five grades are used as SP1's key words them. Two grades do not match the unit's own evidence statement: the section 9 multi-sport grade note, and the sleep action in Dani's note.

## 5. Population: FIX
Samples and designs are named throughout. One table cell applies a finding in non-athletes (Ghadirzadeh et al., 2025) to 13- to 15-year-olds without the inference label.

## 6. Scope and safety: PASS
The unit teaches no assessment, diagnosis or treatment. It gives no weight-loss method, calorie figure or target weight, and describes no method of self-harm. No law is stated as the reader's, and the disclaimer is in the first paragraph. No real athlete, coach or club is named. Mood, eating (Dani's snack) and injury (Sara's hamstring) each say where the coach's part ends and who takes over.

## 7. Any sport: PASS
Examples by sport, each section mention counted once, with the deliverable included and the case athletes counted: football 6, athletics 4, judo 2, swimming 2, basketball 1, handball 1, ice hockey 1, tennis 1. That is 18 in all. Football is 6 of 18, exactly a third and not above it. This count includes Tzioumakis (grassroots football) and the section 9 child who plays tennis, football and swims. Without those two, football is 4 of 15 (27%), as in F25. Kinds of sport: individual, team, weight-class and endurance are all present. Nothing personal to anyone is in the text. `kit/private_terms.py` is outside the packet and was not run.

## Findings

[should-fix] [label] Section 9; Current: "(one meta-analysis in athletes, read in abstract, its intervals and study quality not seen, rule 4); the age boundaries are practice, untested]"; Problem: The grade note contradicts the unit's own source line in the same section and unsure-list item 1. Both say the full text was read on a copy, that its senior contrasts have intervals excluding zero, and that it reports no study-quality rating. The grade (moderate, rule 4) does not change; Fix: "(one meta-analysis in athletes, abstract read at the journal's page and full text on a copy of the published article, not the publisher's page; its senior contrasts' intervals exclude zero and it reports no study-quality rating, rule 4); the age boundaries are practice, untested]"; Basis: unit section 9 and unsure list item 1; abstract at https://www.psychologicalscience.org/journals/perspectives/1745691620974772/

[should-fix] [label] Deliverable B, Dani's Sleep row; Current: "Action: ask, once, privately, how long she usually sleeps on school nights [weak; inference]"; Problem: Section 8 grades asking about sleep as practice (rule 2) and keeps weak for the hours only. Milan's row grades the same action practice; Fix: "Action: ask, once, privately, how long she usually sleeps on school nights [practice; the hours above are weak, inference]"; Basis: unit section 8, "What to do" paragraph; SP1 key as restated in the brief

[should-fix] [label] Deliverable A, 13 to 15, What to watch; Current: "[weak, for the association (Ghadirzadeh et al., 2025); practice for the route]"; Problem: Ghadirzadeh et al. sampled girls and women, not athletes. Section 2 labels its use "inference for athletes", but this cell applies it to 13- to 15-year-old athletes without the label, which the brief and Part 7 require; Fix: "[weak, for the association (Ghadirzadeh et al., 2025; girls and women, not athletes); inference; practice for the route]"; Basis: https://www.elsevier.es/en-revista-clinics-22-articulo-the-association-between-age-at-S1807593225001139

[should-fix] [coverage] Deliverable A, 10 to 12, What to hold back; Current: "More than 8 months a year in one sport (NSCA) [practice; NSCA consensus; the studies behind it were not opened]."; Problem: Flag F154 is open. The NSCA gives the limit for "youth", which it defines as children and adolescents up to 18. Section 9 says youth, but the table puts the limit only at 10 to 12, and SP10 follows the table. A one-cell edit makes them agree; Fix: "More than 8 months a year in one sport (NSCA; the statement sets this for all youth to 18, so it holds in the next two bands too) [practice; NSCA consensus; the studies behind it were not opened]."; Basis: Lloyd et al. (2016), https://dxpprod.nsca.com/globalassets/education/nsca_position_statement_on_ltad.pdf (definition of youth; p. 1500)

[should-fix] [coverage] Section 6; Current: "For 16 to 25, no source on emotion regulation was opened; that band is unsourced here."; Problem: Flag F55 is open. SP4 now grades two sources at 16 to 25 (both weak, per F19's status), and SP2 does not point the reader to them. The fix makes no claim of SP4's evidence; this reviewer did not open those sources; Fix: "For 16 to 25, no source on emotion regulation was opened for this unit; SP4 grades two studies at those ages (weak) and the reader should take that band from SP4."; Basis: syllabus-flags.md F19 (status) and F55

[should-fix] [attribution] Section 4; Current: "Somerville (2016) asks neuroscientists to settle how brain maturation is defined and measured, and names no age at which it ends ([Somerville, 2016, abstract read](https://doi.org/10.1016/j.neuron.2016.10.059))."; Problem: The abstract was read only on a library record. That is not the publisher's page, PubMed or the DOI address, so by the brief the reference carries no claim (F23, open). The record this reviewer reached matches the unit's wording. The examination of "25" stands without it; Fix: "Somerville (2016) could not be opened at a publisher's page, PubMed or its DOI address; only a library record was seen, so no claim rests on it ([Somerville, 2016, not opened](https://doi.org/10.1016/j.neuron.2016.10.059))."; Basis: brief, sourcing standard; https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_1852784554 (not an accepted address)

[should-fix] [attribution] Section 4; Current: "Sawyer et al. (2018) propose defining adolescence as 10 to 24 years, since "continued growth has lifted its endpoint age well into the 20s"; their abstract does not mention the brain ([Sawyer et al., 2018, abstract read](https://doi.org/10.1016/S2352-4642%2818%2930022-1))."; Problem: This is the same case as Somerville: the abstract was read only on a repository record. PubMed served reCAPTCHA, and the record matches the quotation. By the brief the reference carries no claim until it is opened at an accepted address (F23). The preceding sentence ("were read in abstract only, on library records") should then say "were not opened"; Fix: "Sawyer et al. (2018) could not be opened at a publisher's page, PubMed or its DOI address; only a repository record was seen, so no claim rests on it ([Sawyer et al., 2018, not opened](https://doi.org/10.1016/S2352-4642%2818%2930022-1))."; Basis: brief; https://eres.library.adelaide.edu.au/dspace/handle/2440/124427 (not an accepted address)

[should-fix] [attribution] Section 10, A late developer of 17; Current: "(Boccia et al., 2017: one retrospective study in athletes, rule 5; correlational)"; Problem: Boccia et al. (2017) has never been opened at the publisher's page or DOI address (F42, open). For this reviewer too, the DOI redirected and was not followed. The section 10 paragraph and Sources disclose this, but the grade notes that carry its claim into advice do not: this one, Deliverable A's 13-to-15 "What to ask for", Milan's "What I ask for" and Sara's "What I hold back". Mark each one the same way. Cutting the notes would leave the rate-of-improvement advice at practice; Fix: "(Boccia et al., 2017: one retrospective study in athletes, rule 5; correlational; read only on a repository copy, not at the publisher's page, so not verified under the course's rule)"; Basis: brief ("a reference that could not be opened carries no claim"); syllabus-flags.md F42

[minor] [attribution] Section 3; Current: "([Cobley et al., 2009, abstract read on a sport-literature database record, not the publisher's page](https://doi.org/10.2165/00007256-200939030-00005))"; Problem: Sources says the abstract was first read at the DOI address on 17 Nov 2026 and re-read on the database record on 18 Nov. The in-text label gives only the database record, so the two disagree. This reviewer could not open it: the DOI redirected; Fix: "([Cobley et al., 2009, abstract read at the DOI address on 17 Nov 2026 and re-read on a sport-literature database record, not the publisher's page](https://doi.org/10.2165/00007256-200939030-00005))"; Basis: unit Sources entry for Cobley et al. (2009)

[minor] [style] Section 6; Current: "His pattern is a question for SP4 and SP5, not something to wait out."; Problem: The brief bars 'not X but Y' constructions, and this contrast is of that form; Fix: "SP4 and SP5 take up his pattern now."; Basis: brief, Tone

## Brief and deliverable
- Every Cover item is present. Self-image under pubertal timing (F16) and emotion regulation at 16 to 25 are stated as unsourced, which the sourcing rule allows.
- Deliverable A has four bands by four columns, and every cell is graded. Deliverable B is built in full for Dani, Milan and Sara, then as a template whose blanks say what goes in them. Met.
- Case facts agree with case-facts.md, including the SP2 additions. Training ages are correct (6 and 8 years). Each athlete is labelled (fictional) on first use, and none is used as evidence.
- Length: about 7,400 words without the viz blocks (about 5,000 before the deliverable), over the brief's 2,000 to 6,000. The excess is the tables and the in-text provenance notes added by the correction rounds. No finding is raised, because none of it is padding; a later pass could move provenance into Sources.
- Part 7, line by line: met except the reference-not-opened line (Somerville, Sawyer, Boccia), the inference line (one cell) and the private-terms script (not run here).
- Read as the coach in the preamble: the "What to do" lines and both tools are usable without psychology training. Dani's weight-class line keeps the coach out of weight talk.

## Flags naming SP2
- F4, F12, F13, F14, F15, F16, F17, F18, F19, F21, F25, F26, F28, F47, F48: dealt with or carried as their status says.
- F20, F151, F157: Park et al. (2013) still not opened; the unit says so.
- F22, F107: Cobley still abstract only, and the DOI redirected for this reviewer too.
- F23: open (findings above).
- F42: open (finding above).
- F55: not applied (finding above).
- F93: settled. Frontiers full text, Table 7, gives the 9-to-12 group the higher latent score (58.99 against 54.7, partial η² 0.02), while the abstract says the opposite. SP2 is correct, and F93 can close.
- F133, F152: not applied. That needs Walsh et al. (2021) opened, which was not done here. SP2's adult wording matches Watson et al. (2015).
- F154: not applied (finding above).
- F177: this review.

## Could not verify
- "pooled 38 studies published from 1984 to 2007 (253 independent samples, 14 sports, 16 countries)" and the rest of the Cobley paragraph: not opened.
- "Of those in the top 4% as adults, 10% to 25% had been top-level at 16, except in women's high jump (59%)": Boccia, not opened.
- "(1,266 and 1,442 men, 898 and 1,258 women)": Boccia, not opened.
- "The top-level adults reached their personal bests later, and improved faster each year, than the rest of the sample": Boccia, not opened.
- "performance before the age of 16 is not a good predictor of adult performance": Boccia, not opened.
- "Its published correction replaces two figures, on age at personal best and on rate of improvement": not opened.
- "Somerville (2016) asks neuroscientists to settle how brain maturation is defined and measured": library record only; it matches.
- "continued growth has lifted its endpoint age well into the 20s": library record only; it matches.
- All Bethlehem figures in section 4 and the viz: matched on the published version at escholarship.org; not opened at nature.com.
- "(an estimate the full text bases on six effect sizes from 228 athletes)" and "mentions 10,000 hours only in describing an earlier study of violinists": Purdue copy only. The copy also has "over 10,000 twins", which is not about practice.
- Section 7, all ISSP claims (six layers, transition kinds, "months to years", four phases, the dual-career definition, the 126-study review): matched on the published version in the JYX repository; not the publisher's page.
- "A balloon-pumping risk task with 184 participants aged about 9 to 19": Saarland repository copy only; it matches.
- "Performance changed fastest from about 10 to 15, less from 15 to 18": not specifically checked.
- "which the authors do not discuss" (Güllich & Barth heterogeneity): I² 74.94 and 74.83 confirmed; the rest not checked.
- "links it to overuse injury": the NSCA text read says "increased risk of injury"; "overuse" not found.
- Bergeron 2015, pp. 843–851: not shown.
- Güllich et al. 2022, 17(1):6–29: not shown.
- Smith 2018, 48:1451–1478, and its correction 48:1989–1990: not shown.
- Stambulova "(online 10 March 2020)": the repository date is 16 March 2020.
- Lorenz & Kray, volume 51: not shown (the unit already marks this).
- Arain et al. (2013) full text: not shown. Whether its body names an age such as 25 is unchecked; the abstract names none.
- Güllich et al. 2022 full-text intervals (unsure item 1): copy only.

## Confirmed
- NSCA: all four quotations verbatim; "training age" absent; 30(6):1491–1509 and authors. https://dxpprod.nsca.com/globalassets/education/nsca_position_statement_on_ltad.pdf
- IOC: November 2014 meeting; "first two decades"; biological clocks; VO2 +80% and +150%; girls ahead on cycling peak power to about 12 through earlier maturation; selection between 9 and 15; the gradient favouring early-maturing males; no late-maturing-girl sport named; older outperform younger; 8.5–9.5 h; injury and insufficient sleep; tailored schedules; avoid early specialisation; post-puberty specialisers have fewer injuries and play longer; diversification; the talent-system disconnect; elite success "highly unlikely"; burnout and dropout. https://bjsm.bmj.com/content/49/13/843.full
- Albaladejo-Saura 2021: 13 studies; SMDs 0.37–2.31, 0.17–2.31 and 0.96–1.19; no samples or sports in the abstract. https://mdpi.com/1660-4601/18/1/328
- Ghadirzadeh 2025: 13 studies, 434,838, 5 cohort and 8 cross-sectional; OR 1.36 (1.20–1.53); adolescents 1.34 (1.15–1.56); late menarche not significant; heterogeneity; publication bias; confounders; female only. https://www.elsevier.es/en-revista-clinics-22-articulo-the-association-between-age-at-S1807593225001139
- Smith 2018: 57, 308, 25 sports, 1984–2016; OR 1.25 (1.21–1.30), small; the moderators as stated. https://www.springermedizin.de/relative-age-effects-across-and-within-female-sport-contexts-a-s/15531364
- Tervo-Clemmens 2023: 10,766, ages 8–35, four datasets, 23 measures from 17 tasks, adult levels at 18–20, over 95% of change before 18, individual variation; 14:6922. https://www.nature.com/articles/s41467-023-42540-8.pdf
- Foulkes & Blakemore 2018: the quotation; SES, culture and peers; 21(3):315–323. https://link.springer.com/article/10.1038/s41593-018-0078-4
- Crone & Dahl 2012: cognitive-control evidence "relatively inconsistent"; limbic responses peaking in mid-adolescence; the heuristic model; 13:636–650. https://link.springer.com/article/10.1038/nrn3313
- Arain 2013: the abstract names no end age; 9:449–461. https://www.dovepress.com/maturation-of-the-adolescent-brain-peer-reviewed-fulltext-article-NDT
- Haddad 2014: 40 adolescents aged 11–18; 28 adults aged 20–38, 4 excluded; photographs of fictitious peers; d 0.95; no within-group test. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.01476/full
- Sanchis-Sanchis 2020: all section 6 figures and the quotation. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.00946/pdf
- Paruthi 2016b: 13 voting members including a moderator, RAND, 864 articles, the hours and associations; 12(11):1549–1561. https://aasm.org/resources/pdf/pediatricsleepdurationmethods.pdf . Paruthi 2016, 12(6):785–786. https://pubmed.ncbi.nlm.nih.gov/27250809/
- Watson 2015: 7 or more hours; the harms; more than 9 "may be appropriate for young adults"; 15 experts, 5,314 articles; dual publication, Sleep 38(6):843–844. https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf
- Güllich 2022 abstract: 51 reports, 477 effect sizes, 6,096 athletes, 772 world-class; the patterns as stated. https://www.psychologicalscience.org/journals/perspectives/1745691620974772/
- Gallant & Bélanger 2021: 38 studies, 33 DMSP; tenet 1 supported by 8 of 8; tenet 2 by 6 studies, 5 cross-sectional; the quotation; 71% cross-sectional; mostly elite athletes. https://www.frontiersin.org/articles/10.3389/fspor.2021.741495/full
- Güllich & Barth 2024: 51 effect sizes, 6,233 athletes, 82% male, 2009–2022, nine countries; both d values with their CIs and k; high quality; turnover figures; 54:697–710. https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf
- Güllich 2023: 110 samples (38,383) and 79 (22,961); "largely two disparate populations"; 7.2%/92.8% in the abstract only; no meta-analysis; 53:1201–1217. https://link.springer.com/content/pdf/10.1007/s40279-023-01840-1.pdf
- Tzioumakis 2026: title, authors, 17:1563931; players aged 10–15; autonomy support rose briefly and was "not sustained"; disempowering climate fell. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full

Verdict: SP2 · fix · 0 error, 8 should-fix, 2 minor
