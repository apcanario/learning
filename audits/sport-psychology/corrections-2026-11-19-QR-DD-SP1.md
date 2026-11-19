---
check: corrections check of the findings of quality-review-DD-SP1-2026-11-19-b.md, W-DD-SP2, 19 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file)
---

Model: claude-opus-5-5
Totals: 13 findings checked: 12 PASS, 1 FAIL (Change 13, Alt given). 20 New changes for UNVERIFIED items. Currents counted by script: each occurs once in files/DD-SP1-the-coachs-line-with-minors.md, except Change 13's (twice).
Web: WebSearch first for every source; fetched only addresses returned verbatim by a search. Opened: research.edgehill.ac.uk and repository.lboro.ac.uk records (2024 IOC abstract); olympics.com IOC news page; maapp.uscenterforsafesport.org USOPC_MAAPP_01.01.25.pdf; uscenterforsafesport.org/2025-maapp; frontiersin.org (Willson 2025, Li 2025, Ríos 2022, Li Yang & Wang 2025, Hu 2023); mdpi.com/2076-0760/11/8/322 (Wilson & Rhind) and mdpi.com/1660-4601/17/13/4909 with its mdpi-res PDF (Morales-Sánchez); sport.nspcc.org.uk positions-of-trust and away-day-trips pages; bjsm.bmj.com/content/50/17/1019 (Mountjoy 2016). Not checked: pmc.ncbi.nlm.nih.gov PMC9554369 (reCAPTCHA page); www.pubmed.gov/34549664 and www.ncbi.nlm.nih.gov/pmc PMC9554369 (redirected, not followed); informahealthcare pages for Fletcher & Sarkar and Kegelaers (no citation shown). No search returned the IOC copy or the BJSM page of Tuakli-Wosornu et al. (2024), the SAGE page of Willson et al. (2022), or the Center's 2025-MAAPP.pdf address. uscenterforsafesport.org/wp-content/uploads/2025/01/MAAPP-Jan-2025.pdf was opened; it is a press release, not the policies.
Verified, no change needed: SP3's two studies (Morales-Sánchez 2020: 103 male footballers aged 12 to 17, CCBS with "negative conditional support" as an indicator; Hu 2023: 252 athletes, age groups 10–14 to 25 and above, cross-sectional); NSPCC away-day page (last updated 24 Nov 2022); MAAPP 2025 Parts I to IV, and the Part I, III and IV rules the unit cites (Center's page); Mountjoy 2016 quotations and Box 1 (BJSM page); SP7's 6-of-80 and untested repair (s17), which match F101. Fletcher & Sarkar and Bartholomew 2010 bibliographic fields are already marked unchecked in the unit, so no change is proposed for them.
(The harness refused the write to out/report.md; this is the whole report.)

## Change 1
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
and a RAND/UCLA appropriateness process with 80% agreement set in advance as consensus
```
Replacement:
```
and statements voted on under a Delphi protocol with at least 80% agreement set in advance as consensus (abstract)
```
Result: PASS (the abstract, on two repository records, says Delphi and ≥80% a priori and does not mention RAND/UCLA. The BJSM page and the IOC copy were not returned by any search, so F200's RAND/UCLA reading in the full text was not checked. "(abstract)" keeps the claim to what was read.)
Quote: "following a Delphi protocol with ≥80% agreement defined a priori as reaching consensus" (research.edgehill.ac.uk record; repository.lboro.ac.uk record)
Syllabus: no conflict (settles F200 for the abstract)

## Change 2
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
One-on-one transport needs advance written consent, and another adult or at least two other minors present unless an exception applies.
```
Replacement:
```
One-on-one transport needs advance written consent from a parent or guardian, given at least once a year; otherwise another adult or at least two other minors must be present, unless an exception applies.
```
Result: PASS (the Center's own 2025 MAAPP, Part III, Transportation, lists a and b as alternatives after "unless an exception exists or:". The USOPC adoption, s. 9.1 A, has the same text.)
Quote: "Observable and Interruptible, unless an exception exists or:" then a. consent "obtained at least annually" (uscenterforsafesport.org/2025-maapp, Part III, Transportation A.1)
Syllabus: no conflict

## Change 3
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
Against it: [weak, against the claim; rule 5: correlational studies in athletes, mostly adults or older adolescents, no meta-analysis of controlling coaching opened, no controlled test; for athletes under 18 partly inference].
```
Replacement:
```
Against it, on wellbeing: [weak, against the claim; rule 5: correlational studies in athletes, mostly adults or older adolescents, no meta-analysis of controlling coaching opened, no controlled test; for athletes under 18 partly inference]. On performance: no study opened tests it either way.
```
Result: PASS (neither added study measured performance. Willson et al. (2025) measured satisfaction, eating-disorder and self-harm indicators. Li et al. (2025) measured burnout, with performance discussed only as background. SP1's and SP3's grade of weak, against, stands, which fits F183.)
Quote: Li et al. 2025: athletic performance "was not a measured variable" (frontiersin.org, 10.3389/fpsyg.2025.1643356, Measures; fetch-tool summary)
Syllabus: no conflict

## Change 4
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
Do not use exclusion or silence as a sanction [practice; exclusion and silence as such untested; the association of controlling behaviour with need thwarting and burnout is SP3's, graded weak there].
```
Replacement:
```
Do not use exclusion or silence as a sanction [weak, against; rule 5: SP3's correlational association of controlling behaviour, withheld attention among it, with need thwarting and burnout in 12- to 17-year-old boys; exclusion and silence as such untested].
```
Result: PASS (SP1 section 9, rule 2: a claim tested only by correlational studies "is not practice". Morales-Sánchez et al. (2020) model "negative conditional support", the withholding of attention and affection, as an indicator of controlling style. The grade matches section 4's [weak, against].)
Quote: "A claim tested only by correlational studies has no controlled test but is not practice" (SP1, section 9, rule 2)
Syllabus: no conflict

## Change 5
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
| Their choice; you pass on a concern to [the club welfare officer] when the harm happened while they were under 18 or the person has contact with children | Their decision; yes if the harm happened before 18 or for any risk to minors |
```
Replacement:
```
| Their choice; if the harm happened while they were under 18, or the person has contact with children, ask [the club welfare officer] what you must pass on | Their decision; ask the welfare officer if the harm happened before 18 or there may be a risk to minors |
```
Result: PASS (the current text states an unsourced duty. Part 7 requires a reporting duty to be put as a question with the body to consult. The table's template row "Your duties" already sends this to section 15's questions.)
Quote: "a legal or reporting duty is a question with the body to consult" (sourcing-standard.md, Part 7)
Syllabus: no conflict (SP9, section 6 is cited in the row but is not in the packet, so it was not checked)

## Change 6
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
{"label": "someone else's, or a pattern", "to": {"outcome": "Raise it; ask the welfare officer; report if repeated", "tone": 5}}
```
Replacement:
```
{"label": "someone else's, once", "to": {"outcome": "Raise it; ask the welfare officer; report if repeated", "tone": 5}}, {"label": "a pattern, mine or anyone's", "to": {"outcome": "Welfare officer, told by you", "tone": 1}}
```
Result: PASS (the figure now matches section 5 and Deliverable C's colleague row and last row. The edited block parses as JSON by script. Whether kit/viz.py draws four branches was not checked: viz.py is not in the packet.)
Quote: "A pattern of failures, yours or anyone's, is a concern for the welfare officer" (the unit, section 5)
Syllabus: no conflict

## Change 7
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
of the 40 that completed the self-audit
```
Replacement:
```
of the 40 that rated each safeguard (Table 6)
```
Result: PASS (the text never says how many completed the self-audit. Table 6 gives n = 40 for each safeguard, with 42.5% to 72.5% fully in place, two of them under half.)
Quote: Table 6: "Overall rating from self-audit measure of the eight International Safeguards", each "40 (100%)" (mdpi.com/2076-0760/11/8/322)
Syllabus: no conflict

## Change 8
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
with a 16- or 17-year-old in their care
```
Replacement:
```
with a 16- or 17-year-old they are responsible for
```
Result: PASS
Quote: "with a 16‑ or 17‑year‑old they are responsible for" (sport.nspcc.org.uk, abuse-of-positions-of-trust-within-sport, last updated 02 Jan 2024)
Syllabus: no conflict

## Change 9
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
a coach telling the victim to "work harder" did nothing to stop it
```
Replacement:
```
a coach telling the victim, as she reported it, that all she had to do was work harder did nothing to stop it
```
Result: PASS (the words are the participant's, Anna, basketball, reporting what the coach said)
Quote: "he answered that all I had to do was work harder" (frontiersin.org, 10.3389/fpsyg.2022.819981, Results)
Syllabus: no conflict

## Change 10
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
**Named in the text, not opened for this unit, carrying no claim**
```
Replacement:
```
**Named in the text, not opened for this unit; carrying no claim of their own (section 8's rows are SP6's report of three of them)**
```
Result: PASS (section 8's table attributes its rows to Low et al., Kent et al. and Kegelaers et al., "as SP6 reports" them)
Quote: "the rows are SP6's report, not this unit's finding" (the unit, section 8)
Syllabus: no conflict

## Change 11
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
It is also how DD-SP2 will run comments about weight and body
```
Replacement:
```
It is also the test DD-SP2 starts from for comments about weight and body (F182)
```
Result: PASS (section 5 puts body and weight outside the card. F182 leaves the mapping to DD-SP2's writer, and DD-SP2's brief takes "the comment test DD-SP2 maps weight pressure onto".)
Quote: "DD-SP2's writer is given this flag and decides whether to map weight pressure" (syllabus-flags.md, F182)
Syllabus: no conflict (agrees with DD-SP1's Gives line and DD-SP2's brief)

## Change 12
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
psychological interventions for anxiety in athletes aged 14 to 23
```
Replacement:
```
psychological interventions for anxiety in athletes (aged 14 to 23 as the authors state it, though their table includes older groups)
```
Result: PASS (Table 1 lists Dana et al. 19–30, Ali 20–25 and Mehrsafar et al. mean 25.4)
Quote: "A total of 853 participants aged 14 to 23 years were included" (frontiersin.org, 10.3389/fpsyg.2025.1621635, section 3.2)
Syllabus: no conflict

## Change 13
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
https://uscenterforsafesport.org/wp-content/uploads/2024/01/2025-MAAPP.pdf
```
Replacement:
```
https://uscenterforsafesport.org/wp-content/uploads/2024/01/2025-MAAPP.pdf (address not re-found at review on 19 Nov 2026; the Center's page https://uscenterforsafesport.org/2025-maapp gives the same Parts)
```
Result: FAIL (the Current occurs twice: section 5's link and the Sources entry. The substance holds: no search returned the PDF address, and the Center's page gives Parts I to IV and the rules the unit cites. Alt anchors the change on the Sources entry, which occurs once.)
Alt:
Current: `Effective 1 Jan 2025. https://uscenterforsafesport.org/wp-content/uploads/2024/01/2025-MAAPP.pdf`
Replacement: `Effective 1 Jan 2025. https://uscenterforsafesport.org/wp-content/uploads/2024/01/2025-MAAPP.pdf (address not re-found at review on 19 Nov 2026; the Center's page https://uscenterforsafesport.org/2025-maapp gives the same Parts)`
Quote: "Part III: Required Policies for One-on-One Interactions"; "Effective Date: January 1, 2025" (uscenterforsafesport.org/2025-maapp)
Syllabus: no conflict

## New 1
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
[Tuakli-Wosornu et al., 2024, consensus, pp. 1322, 1324, 1328 to 1329, read on the IOC's copy]
```
Replacement:
```
[Tuakli-Wosornu et al., 2024, consensus, pp. 1322, 1324, 1328 to 1329, read on the IOC's copy; quotations and pages not re-checked at review, 19 Nov 2026]
```
Result: PASS (marks unverified: no search returned the IOC copy or the BJSM page, and none of these phrases is in the abstract)
Quote: the abstract has none of "immense power", "pressured to tolerate", "hierarchical structures" (research.edgehill.ac.uk record)
Syllabus: no conflict

## New 2
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
(Tuakli-Wosornu et al., 2024, p. 1335)
```
Replacement:
```
(Tuakli-Wosornu et al., 2024, p. 1335; not re-checked at review, 19 Nov 2026)
```
Result: PASS (marks unverified; the phrase is not in the abstract)
Quote: "None of the reviewed articles" does not appear in the abstract (research.edgehill.ac.uk record)
Syllabus: no conflict

## New 3
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
The 2016 statement's definitions (Box 1, page 3 of the online-first version) and the 2024 statement's (Table 1, p. 1326) are set side by side below
```
Replacement:
```
The 2016 statement's definitions (Box 1) and the 2024 statement's (Table 1, p. 1326; the 2024 column not re-checked at review, 19 Nov 2026) are set side by side below
```
Result: PASS (Box 1 and its definitions were re-checked on the BJSM page. Its page in the online-first PDF and the 2024 Table 1 were not.)
Quote: Box 1 "Definitions adopted in the IOC Consensus Statement" (bjsm.bmj.com/content/50/17/1019)
Syllabus: no conflict

## New 4
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
(Tuakli-Wosornu et al., 2024, pp. 1326 to 1327). The statement warns that
```
Replacement:
```
(Tuakli-Wosornu et al., 2024, pp. 1326 to 1327; ranges and quotation not re-checked at review, 19 Nov 2026). The statement warns that
```
Result: PASS (marks unverified; the abstract gives no prevalence figures)
Quote: the abstract's numbers are counts of voting statements, "Of 48 voting statements" (research.edgehill.ac.uk record)
Syllabus: no conflict

## New 5
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
as the 2024 IOC consensus statement's scoping review reports them (Tuakli-Wosornu et al., 2024, pp. 1326 to 1327), from section 3 of this unit.
```
Replacement:
```
as the 2024 IOC consensus statement's scoping review reports them (Tuakli-Wosornu et al., 2024, pp. 1326 to 1327; not re-checked at review, 19 Nov 2026), from section 3 of this unit.
```
Result: PASS (figure 1 caption; the block parses as JSON after the edit, by script)
Quote: as New 4
Syllabus: no conflict

## New 6
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
can go hand in hand" (p. 1337).
```
Replacement:
```
can go hand in hand" (p. 1337; this and the outcome above not re-checked at review, 19 Nov 2026).
```
Result: PASS (marks the section 4 items unverified; neither phrase is in the abstract)
Quote: "Diminished sport and academic performance" and "Safe sporting environments" do not appear in the abstract (research.edgehill.ac.uk record)
Syllabus: no conflict

## New 7
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
(Table 4, p. 1330).
```
Replacement:
```
(Table 4, p. 1330; both not re-checked at review, 19 Nov 2026).
```
Result: PASS (marks the section 6 quotation and Table 4 unverified)
Quote: "passive inactions" does not appear in the abstract (research.edgehill.ac.uk record)
Syllabus: no conflict

## New 8
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
across the studies it reviewed (Tuakli-Wosornu et al., 2024, p. 1327).
```
Replacement:
```
across the studies it reviewed (Tuakli-Wosornu et al., 2024, p. 1327; not re-checked at review, 19 Nov 2026).
```
Result: PASS (marks the section 14 hazing and bullying estimates unverified)
Quote: as New 4
Syllabus: no conflict

## New 9
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
(Tuakli-Wosornu et al., 2024, pp. 1334 to 1335).
```
Replacement:
```
(Tuakli-Wosornu et al., 2024, pp. 1334 to 1335; the three quotations not re-checked at review, 19 Nov 2026).
```
Result: PASS (marks the section 16 quotations unverified)
Quote: "awareness that these policies exist", "under-resourced", "had not been empirically assessed" absent from abstract (research.edgehill.ac.uk record)
Syllabus: no conflict

## New 10
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
(Tuakli-Wosornu et al., 2024, pp. 1328 to 1329). A comment the athlete cannot answer
```
Replacement:
```
(Tuakli-Wosornu et al., 2024, pp. 1328 to 1329; not re-checked at review, 19 Nov 2026). A comment the athlete cannot answer
```
Result: PASS (section 5, question 6 reuses section 1's quotation, which was not re-checked)
Quote: as New 1
Syllabus: no conflict

## New 11
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
the issue number 22 is Crossref's; not read on the publisher's page)
```
Replacement:
```
the issue number 22 is Crossref's; not read on the publisher's page; quotations and page numbers not re-checked at review on 19 Nov 2026, when no search returned the IOC copy or the publisher's page; a repository record of the abstract gives 58(22):1322–1344)
```
Result: PASS (marks unverified in Sources)
Quote: "Volume: 58 · Issue: 22 · Pages: 1322–1344" (research.edgehill.ac.uk record)
Syllabus: no conflict

## New 12
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
([Willson et al., 2022, full text read](https://doi.org/10.1177/08862605211045096))
```
Replacement:
```
([Willson et al., 2022, full text read; figures not re-checked at review, 19 Nov 2026](https://doi.org/10.1177/08862605211045096))
```
Result: PASS (marks the 75%, 68.8%, 60.2%, 20.5%, 14.3%, mean age 27.7 and 16% unverified. PMC served a reCAPTCHA page, PubMed redirected, and no search returned the SAGE page.)
Quote: none obtained (PMC9554369: "Checking your browser before accessing pmc.ncbi.nlm.nih.gov")
Syllabus: no conflict

## New 13
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
current and recently retired Canadian national team athletes, mean age 27.7, response rate 16% (Willson et al., 2022).
```
Replacement:
```
current and recently retired Canadian national team athletes, mean age 27.7, response rate 16% (Willson et al., 2022; figures not re-checked at review, 19 Nov 2026).
```
Result: PASS (figure 2 caption; the block parses as JSON after the edit, by script)
Quote: as New 12
Syllabus: no conflict

## New 14
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
(full text read on the publisher's page; first published online 22 Sept 2021)
```
Replacement:
```
(full text read on the publisher's page; first published online 22 Sept 2021; volume, pages, online date and figures not re-checked at review on 19 Nov 2026)
```
Result: PASS (marks the Sources fields unverified)
Quote: as New 12
Syllabus: no conflict

## New 15
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
(full text read on the publisher's page, https://bjsm.bmj.com/content/50/17/1019, and the online-first PDF, whose Box 1 is on its page 3; volume, issue and pages as Crossref gives them, not shown on the pages read)
```
Replacement:
```
(full text read on the publisher's page, https://bjsm.bmj.com/content/50/17/1019, whose address gives volume 50, issue 17, first page 1019; Box 1 and the quotations re-checked there at review on 19 Nov 2026; the end page 1029 and Box 1's page in the online-first PDF not re-checked)
```
Result: PASS (the BJSM page shows Box 1 and every quotation the unit takes from it, but not the citation fields. The address gives 50/17/1019.)
Quote: Box 1 "Definitions adopted in the IOC Consensus Statement" (bjsm.bmj.com/content/50/17/1019)
Syllabus: no conflict

## New 16
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
SP7's state-response table already lists it among the responses to avoid with an overconfident athlete (SP7, Deliverable B).
```
Replacement:
```
SP7's state-response table already lists it among the responses to avoid with an overconfident athlete (SP7, Deliverable B; not re-checked against SP7 at review).
```
Result: PASS (marks unverified: SP7 is not in the packet, and no flag records it)
Quote: none (cross-unit; SP7 not in packet)
Syllabus: no conflict

## New 17
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
shows the squad that a mistake is survivable (SP7, section 11).
```
Replacement:
```
shows the squad that a mistake is survivable (SP7, section 11; not re-checked against SP7 at review).
```
Result: PASS (marks unverified, as New 16. SP7's claims in section 17 match F101 and need no change.)
Quote: "only 6 of 80 papers on coach-athlete conflict studied interpersonal conflict directly" (syllabus-flags.md, F101; supports s17 only)
Syllabus: no conflict

## New 18
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
https://doi.org/10.1080/10413200.2019.1630864 (named as SP6 reports it)
```
Replacement:
```
https://doi.org/10.1080/10413200.2019.1630864 (named as SP6 reports it; volume, issue and pages not checked against the publisher's record for this unit)
```
Result: PASS (marks unverified: the informahealthcare page returned shows references only, and no other publisher record was returned)
Quote: none (page held only the References section)
Syllabus: no conflict

## New 19
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
The *International Safeguards for Children in Sport* (2014) are the course's frame
```
Replacement:
```
The *International Safeguards for Children in Sport* (cited by Wilson and Rhind, 2022, as International Working Group, 2016) are the course's frame
```
Result: PASS (the document was not opened. The only opened source dates it 2016 and names the body differently, so the 2014 date and the group's name are unsourced.)
Quote: "The International Safeguards for Children in Sport (International Working Group 2016) are:" (mdpi.com/2076-0760/11/8/322)
Syllabus: no conflict

## New 20
File: files/DD-SP1-the-coachs-line-with-minors.md
Current:
```
International Safeguarding Children in Sport Working Group. *International Safeguards for Children in Sport*. 2014 (not opened; its eight safeguards are named from Wilson & Rhind, 2022)
```
Replacement:
```
International Working Group. *International Safeguards for Children in Sport*. 2016, as Wilson & Rhind (2022) cite it (not opened; its eight safeguards are named from Wilson & Rhind, 2022)
```
Result: PASS (as New 19. The eight safeguards in section 15 match Wilson and Rhind's list word for word.)
Quote: reference list: "International Working Group. 2016. International Safeguards for Children in Sport." (mdpi.com/2076-0760/11/8/322)
Syllabus: no conflict
