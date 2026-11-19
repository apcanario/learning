---
audit: fresh check
unit: DD-SP1 · Deep dive: the coach's line with minors
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgR35wf5wmG58AbjrCFw
verdict: fix · 2 errors, 16 should-fix, 7 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: DD-SP1 · fix · error 2, should-fix 16, minor 7

Model: claude-opus-5-5. The harness refused the write to out/report.md, so the whole report is below.

# Fresh check · DD-SP1 · Deep dive: the coach's line with minors

Checked 19 Nov 2026 with live search against these files: sourcing-standard.md Parts 1 and 7, brief.txt, audit-units-SKILL.md, unsure.md, notes.md, sources.md and case-facts.md. No audit report exists for this course, so the errata item was skipped.

An address counts as opened only if a search in this agent returned it and the fetch succeeded. The full text of Tuakli-Wosornu et al. (2024) was not opened: the BJSM page failed, and no search returned the IOC copy. Every claim that rests only on it is reported as "not opened".

## (1) Coverage
- **Covered:**
  - s1: power and the room to object.
  - s2: the IOC definitions (one error, below).
  - s3: prevalence, with samples and limits.
  - s4: harsh coaching, the selected sample and challenge-and-support.
  - s5: the seven-question test.
  - s6: bystanders.
  - s7: humour.
  - s8: punishment and exclusion.
  - s9: favouritism.
  - s10: contact.
  - s11: one-to-one, travel, changing rooms and lifts.
  - s12: messaging.
  - s13: gifts and grooming.
  - s14: other coaches, parents, bullying and initiation.
  - s15: routes and the International Safeguards for Children in Sport (ISCS).
  - s16: policy on paper.
  - s17: repair.
  - Deliverables A to E, built on the case squads and then as templates.
  - Flags F78, F79, F82, F101 and F168.
- **Thin:**
  - Research categories of emotional abuse: Stirling & Kerr and Gervis & Dunn were not opened; the unit says so.
  - Bartholomew reviews (F5, F31): not opened; stated.
  - Published critique of the challenge-and-support model: none found; stated.
  - ISCS document: not opened.
- **Missing:** none.
- **DD-SP2 hand-over:** body and weight are put outside the card. This is stated as a contradiction in notes.md.
- **Length:** about 10,100 words before the Deliverable, against the brief's 2,000 to 6,000.

## Findings
[error] [accuracy] s2; Current: "The 2016 statement uses "emotional" and "psychological" interchangeably and lists the behaviours athletes report:"; Problem: the statement notes that some definitions use the two terms interchangeably, then chooses "psychological" because the psyche is more than emotions; Fix: "The 2016 statement notes that some definitions use "emotional" and "psychological" interchangeably, and itself uses "psychological"; it lists the behaviours athletes report:"; Basis: Mountjoy et al. 2016, https://bjsm.bmj.com/content/50/17/1019
[error] [figure] Deliverable C, decision viz; Current: "{"q": "Disclosure, anything sexual, physical harm, punishment, or section 13's signs?""; Problem: a parent's abuse, bullying and initiation rites go down the "fails the card" branch to "report if repeated", where table C says Yes, the same day; the figure also narrows the table's punishment-or-humiliation row; Fix: "{"q": "Disclosure, anything sexual, physical harm, a coach's punishment or humiliation, a parent's abuse, bullying, an initiation, or section 13's signs?""; Basis: the unit's table C, rows 1 to 9
[should-fix] [label] Deliverable B, Touch row; Current: "hamstring treatment only by Sara's physiotherapist (case register)"; Problem: case-facts.md has no physiotherapist for Sara; this is an invented fact, attributed to the register and missing from notes.md; Fix: "hamstring treatment only by a physiotherapist (*added*)" (and add it to notes.md Case facts); Basis: case-facts.md
[should-fix] [accuracy] s16; Current: "most rated all eight safeguards fully in place"; Problem: Table 6 shows 42.5% to 72.5% of organisations rating each safeguard fully in place, under half for safeguards 6 and 8; Fix: "between 42.5% and 72.5% rated each safeguard fully in place, under half for two of the eight (Table 6)"; Basis: Wilson & Rhind 2022, https://mdpi.com/2076-0760/11/8/322
[should-fix] [accuracy] s13; Current: "("break small rules to see if they're challenged")"; Problem: not the exact words, so the quotation marks are wrong; Fix: "("breaking small rules to see if they're challenged")"; Basis: NSPCC Sport grooming page, updated 16 Jun 2025, https://sport.nspcc.org.uk/resource-library/best-practice/protecting-children-in-sport-from-grooming-and-sexual-abuse/
[should-fix] [attribution] s13; Current: "Signs the NSPCC page lists, as it states them:"; Problem: only gifts and secrecy are on the page's list of signs; messaging, rule-testing, building trust and being indispensable are described as abusers' tactics; Fix: "Signs and tactics the NSPCC page describes:"; Basis: same page
[should-fix] [attribution] s8; Current: "that is the issuing body's statement for the United Kingdom, not a statement of the law where you coach"; Problem: the page names no jurisdiction; Fix: "that is the issuing body's statement, made without naming the jurisdiction it covers, and not a statement of the law where you coach"; Basis: NSPCC Sport physical contact page, updated 7 Aug 2025, https://sport.nspcc.org.uk/resource-library/best-practice/physical-contact-and-young-people-in-sport/
[should-fix] [accuracy] s15 (STALE); Current: "its status since then was not checked for this unit"; Problem: the search flag is on, and the duty is now in the Crime and Policing Act 2026; Fix: "a UK government factsheet on the Crime and Policing Act 2026 (updated 30 Sept 2026, read 19 Nov 2026) says the duty applies in England to people in regulated activity with children, gives sports coaches as an example, and gives no date for it to take effect ([Home Office, *Crime and Policing Act 2026: Independent Inquiry into Child Sexual Abuse recommendations factsheet*](https://www.gov.uk/government/publications/crime-and-policing-act-2026-factsheets/crime-and-policing-act-2026-independent-inquiry-into-child-sexual-abuse-recommendations-factsheet)); whether it applies to you is a question for your federation's safeguarding lead" (and add a Sources entry and a sources.md row for it); Basis: that page; NSPCC Sport page of 22 May 2026, https://sport.nspcc.org.uk/news-and-blogs/2026-05-updates-to-reporting-sexual-abuse-and-dbs-checks/
[should-fix] [accuracy] s1; Current: "power and control was one of three themes in what they described as emotional abuse"; Problem: the paper has four elements, and power and control is the frame participants used to explain their coaches' behaviour; Fix: "power and control was one of the four elements of what they described as emotional abuse, the frame they used to explain their coaches' behaviour"; Basis: Adams et al. 2024, https://www.frontiersin.org/articles/10.3389/fspor.2024.1428682/full
[should-fix] [accuracy] s4; Current: "Two of the opened studies point the same way: athletes recognised harm only after they stopped"; Problem: Zach et al. report this for some participants only; Willson et al. (2025) report it from earlier studies, not as their own finding; Fix: "Two of the opened studies point the same way: some athletes recognised harm only after they stopped, as Zach et al. report from their interviews and Willson et al. report from earlier studies"; Basis: https://mdpi.com/2076-328X/14/6/486 ; https://www.frontiersin.org/articles/10.3389/fspor.2024.1406775/full
[should-fix] [accuracy] s3; Current: "What the figures do show, on every sample opened:"; Problem: the unit drops Parent et al.'s psychological figure, and the Vertommen abstract has no neglect figure and no perpetrators; Fix: "What the figures show, on the samples opened that report them:"; Basis: the unit's s3; Vertommen abstract, https://research.wur.nl/en/publications/interpersonal-violence-against-children-in-sport-in-the-netherlan/
[should-fix] [accuracy] s1; Current: "as the IOC statement says for children (Mountjoy et al., 2016)"; Problem: the statement says consent cannot apply to children in its section on sexual harassment and abuse; extending it to anything a minor "agreed" to is a stretch; Fix: "as the IOC statement says of sexual harassment and abuse of children, and as this unit applies to the rest of your conduct (Mountjoy et al., 2016)"; Basis: https://bjsm.bmj.com/content/50/17/1019
[should-fix] [deliverable] Deliverable A, comment 5; Current: "| 2 and 4 (a run as punishment; selection as a threat), 6 |"; Problem: the athlete can change whether they miss the standard, so the comment does not fail question 2; Fix: "| 4 (a run as punishment; selection as a threat), 6 |"; Basis: s5 question 2
[should-fix] [deliverable] Deliverable E2; Current: "comment 5's kind, card questions 2, 4 and 6"; Problem: follows from the comment 5 fix; Fix: "comment 5's kind, card questions 4 and 6"; Basis: as above
[should-fix] [deliverable] Deliverable A, comment 12; Current: "| 3, 5, and the conduct code:"; Problem: a private message passes question 3 (private or in front of others?); the privacy problem is already named under the conduct code; Fix: "| 5, and the conduct code:"; Basis: s5 question 3 and card row 3
[should-fix] [deliverable] Deliverable A, count sentence; Current: "questions 1 (about the person), 3 (in front of others) and 6 (no room to answer back) are each failed by eight"; Problem: after the comment 12 fix, question 3 is failed by seven comments (1, 2, 3, 6, 7, 9, 10); Fix: "questions 1 (about the person) and 6 (no room to answer back) are each failed by eight, and question 3 (in front of others) by seven"; Basis: recount of the table
[should-fix] [style] s5; Current: "Any "no" to questions 1, 2, 3, 4 or 5, or "no" to question 6, means rewrite before you say it."; Problem: questions 1 and 3 in s5 are either/or and cannot be answered "no"; question 7 fails on "yes"; question 6 is repeated; the card in Deliverable A is worded so that "no" always means fail; Fix: "Asked as the card in Deliverable A words them, any "no" to questions 1 to 6 means rewrite before you say it; a "no" to question 7 (it is part of a pattern) means repair and, for anyone's pattern, the welfare officer."; Basis: s5 and the Deliverable A card
[should-fix] [label] s8; Current: "[weak, against, for the association of controlling behaviour with need thwarting and burnout, SP3's grade; practice, for exclusion and silence as such]"; Problem: two grades on one recommendation, where the brief requires one; Fix: "[practice; exclusion and silence as such untested; the association of controlling behaviour with need thwarting and burnout is SP3's, graded weak there]"; Basis: brief.txt preamble on evidence grades
[minor] [accuracy] s8; Current: "A narrative review of pressure training in music asserts that it can protect wellbeing"; Problem: the review puts this as a hypothesis ("can be hypothesized"); Fix: "A narrative review of pressure training in music hypothesises that it can protect wellbeing"; Basis: https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1501014/pdf
[minor] [accuracy] s12; Current: "which it defines as copying or including the parent or guardian"; Problem: the policy also allows another adult family member or another adult participant; Fix: "which it defines as copying or including a parent or guardian, another adult family member or another adult participant"; Basis: https://uscenterforsafesport.org/2025-maapp
[minor] [accuracy] s1; Current: "a scoping review and a RAND/UCLA appropriateness process"; Problem: not opened in this check; the abstract on the Edge Hill repository record says "a Delphi protocol"; Fix (if the full text does not name RAND/UCLA): "a scoping review and a Delphi vote"; Basis: https://research.edgehill.ac.uk/en/publications/ioc-consensus-statement-interpersonal-violence-and-safeguarding-i/ (repository record, not the publisher)
[minor] [style] s8 table; Current: "(Kent et al., 2021)"; Problem: Sources gives 2022; Fix: "(Kent et al., 2022)"; Basis: https://informahealthcare.com/doi/full/10.1080/10413200.2020.1868618 (pp. 691 to 712, online 25 Feb 2021)
[minor] [style] s8 table; Current: "Practitioner article (Low et al., 2023)"; Problem: Sources gives 2024; Fix: "Practitioner article (Low et al., 2024)"; Basis: the unit's Sources entry
[minor] [label] Deliverable B; Current: "shown on a cone, a ball or himself"; Problem: the register does not give the sex of Milan's coach (D2 also assumes it), and it is not listed in notes.md; Fix: "shown on a cone, a ball or on the coach's own body"; Basis: case-facts.md
[minor] [coverage] whole unit; Current: "# DD-SP1 · Deep dive: the coach's line with minors"; Problem: about 10,100 words before the Deliverable, against the brief's 2,000 to 6,000, and this is not recorded; Fix: heading unchanged, and add to unsure.md: "11. Length: about 10,100 words before the Deliverable, above the brief's 2,000 to 6,000; the brief names some twenty-five topics."; Basis: brief.txt

## Claims pass
- **PASS:**
  - Mountjoy 2016: the definitions in Box 1, "power differentiated relationship", "stem from abuses of power relations", consent and children, "cared for, protected and supervised", "at the core of all other forms", the list of behaviours, the bystander effect, passive attitudes, the contact-sport pretext, grooming, and "with implementation".
  - Vertommen 2016: 38%, 11% and 14%; over 4,000 adults; risk groups (repository abstract).
  - Willson 2022: perpetrators and sex differences (PubMed abstract).
  - Willson 2025: 794 athletes over 16, mean age 27.85; r = −.316, .311, .252.
  - Li J et al. 2025: 301 athletes, three waves three weeks apart, r = 0.536, performance not measured.
  - Li, Yang & Wang 2025: 24 trials, 853 athletes aged 14 to 23, one football pressure-training study (Tassi et al. 2023), no harm outcome.
  - Parent 2023: 983 adolescents; 59.2%, 23.8%, 10.6%. The 54.0% figure is inconsistent with its count (228/967 = 23.6%), so the unit is right to leave it out.
  - Zach 2024: all figures and all five quotations; mixed methods.
  - Adams 2024: sample and quotations; the punishment distinction; the authors' conclusion that abuse cannot be identified from behaviour alone.
  - Ríos 2022: all claims.
  - St-Pierre 2022: all percentages, 1967 to 2020, mean age 13.6, "tip of the iceberg".
  - McCleery 2025: all claims.
  - Wilson & Rhind 2022: names of the eight safeguards, 50 of 400 organisations, self-report, attrition, Hawthorne effect.
  - de Bie 2024: narrative review; "must not be used as an excuse".
  - Fletcher & Sarkar 2016: both quotations from note 7; no test of effects.
  - MAAPP 2025: all rules cited from Parts III and IV.
  - NSPCC Sport pages: physical contact (quotations), online safety, Deal with a concern, changing facilities, positions of trust, proposed law (STALE as to status).
  - Sport Integrity Australia page and Abuse-Free Sport page.
- **FAIL:**
  - Mountjoy on "interchangeably".
  - Adams on "three themes".
  - Wilson & Rhind on "most rated all eight".
  - NSPCC: "United Kingdom" and the inexact quotation.
- **STALE:** the England reporting duty.
- **Not opened:**
  - Every claim resting only on the Tuakli-Wosornu 2024 full text.
  - Willson 2022 percentages.
  - MAAPP Part I.

## Figures (7)
1. **range, s3. PASS.** Labels and the values 21–79, 4–66, 0.5–78 and 27–69 match the s3 text. The caption names s3, the source and the caution, and the kind fits. The source figures themselves were not opened.
2. **grouped bars, s3. PASS.** The values 38, 11, 14 and 60.2, 14.3, 20.5 match s3. The caption names s3, both sources and why they are not comparable, and the kind fits.
3. **decision, Deliverable C. FIX.** Use this replacement JSON:
{"kind": "decision", "caption": "The report-or-not rule of Deliverable C of this unit, read top-down. The rows and their order are the unit's own [practice]; that you need not decide whether abuse has taken place before passing on a concern is NSPCC Sport's guidance (Deal with a concern, read 19 Nov 2026); the definitions behind the second question are the IOC consensus statements' (Mountjoy et al., 2016; Tuakli-Wosornu et al., 2024), section 2.", "root": {"q": "Could a child be in danger now?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "Emergency number now; then the welfare officer", "tone": 1}}, {"label": "no", "to": {"q": "Disclosure, anything sexual, physical harm, a coach's punishment or humiliation, a parent's abuse, bullying, an initiation, or section 13's signs?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "Welfare officer, the same day; write it down", "tone": 1}}, {"label": "no", "to": {"q": "A comment that fails the card?", "tone": 4, "branches": [{"label": "mine, once", "to": {"outcome": "Repair (D)", "tone": 3}}, {"label": "a colleague's, or a pattern", "to": {"outcome": "Raise it; ask the welfare officer; report if repeated", "tone": 5}}, {"label": "no", "to": {"outcome": "Coaching: no report", "tone": 2}}]}}]}}]}}

## Other passes
- **Figures say whose figure (3):** pass. The "five correlational studies" in s4 depends on SP3's count, which I could not see.
- **Labels (4):** pass. Correlations, accounts, inference and illustrations are all labelled, apart from the two invented case facts above.
- **Deliverable (5):** complete and usable alone. Two places do not follow from the body: figure 3, and comments 5 and 12.
- **Pointers (6):** the pointers to SP7 step 5, SP6 rule 2, the SP1/SP3 grade, SP9's phrase and SP8's "Sleeve first" match notes.md and the register. The other SP3, SP7 and SP10 pointers are not quoted in notes.md, so I could not check them.
- **Bibliography:**
  - These match their publisher pages: Adams, de Bie, Li H, Li J, McCleery, Parent, Ríos, St-Pierre, Willson 2025, Wilson & Rhind, Zach.
  - Mountjoy: authors, title and 50(17) p. 1019 are confirmed; the end page is unverified.
  - Tuakli-Wosornu: 58(22):1322–1344 and the DOI match a repository record. It has 14 authors; sources.md wrongly says 25.
  - Unverified: the Willson 2022 and Fletcher & Sarkar volume and pages; Kent vol. 34(4), 2022 (pages and online date confirmed).
  - Existence only: Kegelaers, Low, Stirling & Kerr.
  - Not checked: Bartholomew ×3, Gervis & Dunn.
  - No reference was found not to exist.
- **Source log:** every Sources entry has a row in sources.md. Abstract-only claims are flagged in the unit.
- **Grades:** the s4 grade [weak, against] fits the key, and the [practice] grades fit. One recommendation has a double grade (finding above).
- **Population:** every study names its sample. Transfers to under-18s are labelled as inference in s2, s4, s7 and s8.
- **Scope and safety:**
  - Nothing teaches assessment, diagnosis, treatment or investigation.
  - No weight-loss method, calorie figure or target weight, and no self-harm method.
  - No law is stated as the reader's. The one exception is the jurisdiction NSPCC does not name (finding).
  - No real person is named.
  - Definitions are quoted with their Box or Table and page.
  - Nothing promises secrecy, and the burden of reporting stays with the coach, not the child.
- **Any sport:**
  - Counting every example: football 14 of 40 (35%), judo 9, athletics 7, others 10.
  - Counting the s8 source rows as evidence rather than examples: football 11 of 37 (30%).
  - The excess comes from the E rows that SP10 reserves for Milan's plan. This is borderline and I propose no edit.
  - I could not check for anything the Project's owner would recognise: kit/private_terms.py is not in the packet.
- **Part 7, line by line:** met, except for the findings above.
- **Read as the coach in the preamble:** a coach could be misled in two places: figure 3, and the yes/no direction of the s5 instruction.

## Confirmed
- Mountjoy et al. 2016: Box 1 definitions, the power and consent passages, the list of behaviours, bystanders, grooming and implementation. https://bjsm.bmj.com/content/50/17/1019
- Vertommen et al. 2016: 38%, 11%, 14%. https://research.wur.nl/en/publications/interpersonal-violence-against-children-in-sport-in-the-netherlan/
- Willson et al. 2022: perpetrators and sex differences. https://www.pubmed.gov/34549664/
- Willson et al. 2025: sample and r values. https://www.frontiersin.org/articles/10.3389/fspor.2024.1406775/full
- Li J et al. 2025. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1643356/full
- Li, Yang & Wang 2025. https://www.frontiersin.org/articles/10.3389/fpsyg.2025.1621635/full
- Parent et al. 2023. https://mdpi.com/2076-0760/12/6/336
- Zach et al. 2024. https://mdpi.com/2076-328X/14/6/486
- Adams et al. 2024 (except the themes count). https://www.frontiersin.org/articles/10.3389/fspor.2024.1428682/full
- Ríos et al. 2022. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.819981/full
- St-Pierre et al. 2022. https://www.frontiersin.org/articles/10.3389/fpsyg.2022.856798/pdf
- McCleery et al. 2025. https://www.mdpi.com/2673-995X/5/1/12
- Wilson & Rhind 2022 (names, sample). https://mdpi.com/2076-0760/11/8/322
- de Bie et al. 2024. https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1501014/pdf
- Fletcher & Sarkar 2016, note 7. https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496
- MAAPP 2025. https://uscenterforsafesport.org/2025-maapp
- NSPCC Sport pages:
  - https://sport.nspcc.org.uk/resource-library/best-practice/physical-contact-and-young-people-in-sport/
  - https://sport.nspcc.org.uk/help-advice/topics/online-safety/
  - https://sport.nspcc.org.uk/resource-library/best-practice/protecting-children-in-sport-from-grooming-and-sexual-abuse/
  - https://sport.nspcc.org.uk/help-advice/deal-with-a-concern/
  - https://sport.nspcc.org.uk/resource-library/best-practice/safe-use-of-changing-facilities/
  - https://sport.nspcc.org.uk/resource-library/best-practice/abuse-of-positions-of-trust-within-sport/
  - https://sport.nspcc.org.uk/news-and-blogs/2025-09-free-training-about-new-law-on-reporting-child-sexual-abuse/
- Sport Integrity Australia. https://www.sportintegrity.gov.au/what-we-do/safeguarding/safeguarding-reporting
- Abuse-Free Sport. https://abuse-free-sport.ca/about
- Kent et al.: pages and online date. https://informahealthcare.com/doi/full/10.1080/10413200.2020.1868618

## Could not verify
- Tuakli-Wosornu et al. 2024 full text: Table 1, all prevalence ranges (so the range figure's numbers), all quotations and pages in s1, s3, s4, s6, s14 and s16, and RAND/UCLA.
- Willson 2022: the percentages, mean age 27.7, response rate 16%, and volume and pages.
- Mountjoy: the end page, and the Box 1 page in the online-first PDF.
- Fletcher & Sarkar: bibliographic details.
- Kent 34(4) and 2022; Kegelaers and Low details; Bartholomew ×3; Gervis & Dunn; Stirling & Kerr details.
- MAAPP Part I, and room checks by two adults.
- Whether the unit's NSPCC addresses resolve. They differ from the ones my searches returned (resource-library and help-advice paths).
- The SP3, SP7 and SP10 pointers not quoted in notes.md.
- The owner's private terms.
- notes.md does not list comment 3 ("Watch Dani…") among its case illustrations; it lists the parallel ones for Milan and Sara.

Verdict: DD-SP1 · fix · error 2, should-fix 16, minor 7
