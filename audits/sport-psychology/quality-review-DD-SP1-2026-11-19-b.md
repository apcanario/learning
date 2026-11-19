---
code: DD-SP1
kind: quality-review (rule 13)
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgQzDra5WhwrnjTVBqy8
note: second review of the day (F205); report returned as the agent reply (harness blocked its file write) and saved verbatim by the chat
---
Verdict: DD-SP1 · fix · 0 errors, 6 should-fix, 7 minor
Model: claude-opus-5-5

The harness refused to write out/report.md, so the whole report is given here. Review date 19 Nov 2026, live search. I read only the packet files and used no memory, connector or project tool. Every fetch was of a URL that a search in this agent returned verbatim. One fetch redirected (PMC, Willson 2022) and one returned a browser-check page; both count as not checked and neither was retried.

## Pass 1 · Claims: FIX
Opened and checked:
- Mountjoy 2016, full text at bjsm.bmj.com/content/50/17/1019. Every quotation the unit takes from it is verbatim.
- Full text: Adams 2024, Zach 2024, Willson 2025, Li J 2025, Li H 2025, McCleery 2025, Parent 2023, Ríos 2022, St-Pierre 2022, Wilson & Rhind 2022, de Bie 2024.
- Vertommen 2016, abstract only. Fletcher & Sarkar 2016, notes only.
- Eight NSPCC Sport pages, the Home Office factsheet, Sport Integrity Australia, Abuse-Free Sport.
- The Center for SafeSport's 2025 MAAPP page (Parts I, III, IV) and the USOPC adoption PDF.

Not opened:
- Tuakli-Wosornu 2024, full text. Only the abstract on the Edge Hill record was reachable. Every quotation and page number from this statement is unverified, and the abstract contradicts the unit's method wording (finding 1).
- Willson 2022, full text. Only the PubMed abstract was reachable.

FIX: findings 1, 2, 7, 8, 9.

## Pass 2 · Bibliography: PASS with minor
Checked field by field and correct:
- Mountjoy: author list.
- Tuakli-Wosornu: 14 authors, order, 58(22):1322–1344, DOI.
- Adams, de Bie, Li H, Li J, McCleery, Parent, Ríos, St-Pierre.
- Willson 2025: vol 6, published 10 Jan 2025.
- Wilson & Rhind: 11(8):322. Zach: 14(6):486. Vertommen: 51:223–236.
- Low: 15(1):3–18, online 18 Jan 2023. Kent: pp. 691–712, online 25 Feb 2021.
- Bartholomew 2009 and 2011, Gervis & Dunn, Stirling & Kerr.

Not checked:
- Willson 2022: pages and online date.
- Fletcher & Sarkar, Kegelaers, Bartholomew 2010: fields.
- DOIs that the records did not show.

Every reference exists. Finding 13 concerns the MAAPP address.

## Pass 3 · Source log: PASS with minor
- sources.md is not in the packet, so the log itself was not checked.
- Abstract-only claims are labelled: Vertommen and Fletcher & Sarkar.
- Every Sources entry is cited in the text.
- The "carrying no claim" heading conflicts with section 8's table (finding 10).

## Pass 4 · Grades: FIX
- Section 4 grades the performance claim weak, but no study the unit opened measured performance (finding 3).
- Section 8 grades exclusion and silence [practice] while citing a correlational association. SP1's rule 2 says that is not practice (finding 4).

## Pass 5 · Population: PASS
Each finding gives its sample and design, and correlations are called correlations. Transfers to under-18s are labelled as inference in sections 2, 4, 7 and 8.

## Pass 6 · Scope and safety: FIX
- Disclaimer present. Nothing teaches assessment or treatment, and the unit says where the coach's part ends.
- No weight-loss method or figure. No self-harm method.
- Laws are attributed to the body that states them and put as questions.
- No real person is named.
- One exception: Deliverable C's adult-athlete row overrides an adult's decision with no source, and does not put it as a question (finding 5).
- private_terms.py is not in the packet and was not run.

## Pass 7 · Any sport: PASS
A mention count is consistent with F196: football 9, judo 8, athletics 7, others 8, of 32. Deliverable A has four comments per squad. No sport supplies more than a third. Nothing in the unit is recognisable as a real person.

## Part 7 line by line
- Every item passes, except: grades (findings 3, 4), law as a question (finding 5), the source log (not in packet) and private terms (not run).
- Abuse-Free Sport and Sport Integrity Australia rely on the preamble's blanket read date of 19 Nov 2026.
- The unit does not read as advice without evidence.

## Read as the coach
Usable. The card, the conduct code and the decision table each work on their own. The unit is about 10,460 words before the Deliverable (F198).

## Brief coverage
- All 18 Cover items are present. One is thin: the research categories of emotional abuse, because Stirling & Kerr and Gervis & Dunn were not opened (F185).
- The deliverable is built in full, with templates.
- "Gives": body and weight are kept outside the card (finding 11, F182).

## Flags
- F5, F31, F184: carried and stated.
- F8, F14, F47: the key is applied, with the [practice] convention.
- F78, F79, F82, F180: section 8.
- F86, F158, F197: carried, recorded on the unsure list.
- F101, F124: section 17.
- F102: none used.
- F121, F134: section 11.
- F123: not needed.
- F139: sections 14 and 15.
- F168: Deliverable E.
- F182: open.
- F185, F188–F191, F195, F196, F198: recorded.
- F200: the abstract says Delphi (finding 1).
- F201: the 14 authors and MAAPP Parts I, III and IV are now confirmed. The Tuakli-Wosornu quotations are still unverified.
- F205: this review.

## Figures
1. Range figure, section 3: PASS. Numbers are in the text, the caption is right and the kind fits. Values are unverified at source.
2. Grouped bars, section 3: PASS. Numbers are in the text and the caption warns against comparing the two surveys. The Willson 2022 values are unverified at source.
3. Decision figure, Deliverable C: FIX (finding 6).

## FINDINGS
1. [should-fix] [accuracy] section 1
   - Current: "and a RAND/UCLA appropriateness process with 80% agreement set in advance as consensus"
   - Problem: the abstract says "following a Delphi protocol with ≥80% agreement defined a priori"; it does not mention RAND/UCLA.
   - Fix: "and statements voted on under a Delphi protocol with at least 80% agreement set in advance as consensus (abstract)"
   - Basis: https://research.edgehill.ac.uk/en/publications/ioc-consensus-statement-interpersonal-violence-and-safeguarding-i/
2. [should-fix] [accuracy] section 11
   - Current: "One-on-one transport needs advance written consent, and another adult or at least two other minors present unless an exception applies."
   - Problem: in the USOPC adoption, section 9.1A gives annual written consent and accompaniment as alternatives, joined by "or:". The unit makes them both required. The Center PDF the unit cites was not found by search.
   - Fix: "One-on-one transport needs advance written consent from a parent or guardian, given at least once a year; otherwise another adult or at least two other minors must be present, unless an exception applies."
   - Basis: https://maapp.uscenterforsafesport.org/wp-content/uploads/2025/01/USOPC_MAAPP_01.01.25.pdf
3. [should-fix] [label] section 4
   - Current: "Against it: [weak, against the claim; rule 5: correlational studies in athletes, mostly adults or older adolescents, no meta-analysis of controlling coaching opened, no controlled test; for athletes under 18 partly inference]."
   - Problem: neither added study measured performance, so the weak grade rests on wellbeing alone.
   - Fix: "Against it, on wellbeing: [weak, against the claim; rule 5: correlational studies in athletes, mostly adults or older adolescents, no meta-analysis of controlling coaching opened, no controlled test; for athletes under 18 partly inference]. On performance: no study opened tests it either way."
   - Basis: https://doi.org/10.3389/fspor.2024.1406775; https://doi.org/10.3389/fpsyg.2025.1643356
4. [should-fix] [label] section 8
   - Current: "Do not use exclusion or silence as a sanction [practice; exclusion and silence as such untested; the association of controlling behaviour with need thwarting and burnout is SP3's, graded weak there]."
   - Problem: SP1's rule 2 says correlational evidence is not practice. Section 4 grades the same kind of evidence weak.
   - Fix: "Do not use exclusion or silence as a sanction [weak, against; rule 5: SP3's correlational association of controlling behaviour, withheld attention among it, with need thwarting and burnout in 12- to 17-year-old boys; exclusion and silence as such untested]."
   - Basis: SP1 section 9, rule 2 (filed/SP1)
5. [should-fix] [scope] Deliverable C
   - Current: "| Their choice; you pass on a concern to [the club welfare officer] when the harm happened while they were under 18 or the person has contact with children | Their decision; yes if the harm happened before 18 or for any risk to minors |"
   - Problem: this is an unsourced reporting duty that overrides an adult's choice, and it is not put as a question.
   - Fix: "| Their choice; if the harm happened while they were under 18, or the person has contact with children, ask [the club welfare officer] what you must pass on | Their decision; ask the welfare officer if the harm happened before 18 or there may be a risk to minors |"
   - Basis: sourcing-standard.md Part 7
6. [should-fix] [figure] Deliverable C
   - Current: "{"label": "someone else's, or a pattern", "to": {"outcome": "Raise it; ask the welfare officer; report if repeated", "tone": 5}}"
   - Problem: the coach's own pattern goes to "Raise it", but the table and section 5 send it to the welfare officer.
   - Fix: "{"label": "someone else's, once", "to": {"outcome": "Raise it; ask the welfare officer; report if repeated", "tone": 5}}, {"label": "a pattern, mine or anyone's", "to": {"outcome": "Welfare officer, told by you", "tone": 1}}"
   - Basis: the unit, section 5 and Deliverable C's last row
7. [minor] [accuracy] section 16
   - Current: "of the 40 that completed the self-audit"
   - Problem: the paper does not say 40 completed a self-audit. 40 is the count per safeguard in Table 6.
   - Fix: "of the 40 that rated each safeguard (Table 6)"
   - Basis: https://mdpi.com/2076-0760/11/8/322
8. [minor] [attribution] section 13
   - Current: "with a 16- or 17-year-old in their care"
   - Problem: the page says "they are responsible for".
   - Fix: "with a 16- or 17-year-old they are responsible for"
   - Basis: https://sport.nspcc.org.uk/resource-library/best-practice/abuse-of-positions-of-trust-within-sport/
9. [minor] [attribution] section 14
   - Current: "a coach telling the victim to "work harder" did nothing to stop it"
   - Problem: these are the athlete's reported words, not the coach's.
   - Fix: "a coach telling the victim, as she reported it, that all she had to do was work harder did nothing to stop it"
   - Basis: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.819981/full
10. [minor] [attribution] Sources
    - Current: "**Named in the text, not opened for this unit, carrying no claim**"
    - Problem: section 8 carries the consequences from Kent, Kegelaers and Low, as SP6 reports them.
    - Fix: "**Named in the text, not opened for this unit; carrying no claim of their own (section 8's rows are SP6's report of three of them)**"
    - Basis: the unit, section 8
11. [minor] [coverage] section 5
    - Current: "It is also how DD-SP2 will run comments about weight and body"
    - Problem: section 5 puts body and weight outside the card, so this sentence contradicts it (F182).
    - Fix: "It is also the test DD-SP2 starts from for comments about weight and body (F182)"
    - Basis: brief.txt; flags.txt F182
12. [minor] [accuracy] section 8
    - Current: "psychological interventions for anxiety in athletes aged 14 to 23"
    - Problem: the paper's Table 1 includes groups aged 19–30 and one with mean age 25.4.
    - Fix: "psychological interventions for anxiety in athletes (aged 14 to 23 as the authors state it, though their table includes older groups)"
    - Basis: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1621635/full
13. [minor] [attribution] Sources
    - Current: "https://uscenterforsafesport.org/wp-content/uploads/2024/01/2025-MAAPP.pdf"
    - Problem: no search returned this address.
    - Fix: mark unverified, adding after the URL: " (address not re-found at review on 19 Nov 2026; the Center's page https://uscenterforsafesport.org/2025-maapp gives the same Parts)"
    - Basis: https://uscenterforsafesport.org/2025-maapp

## UNVERIFIED
- Tuakli-Wosornu 2024 (full text not opened):
  - s1: three quotations, pages 1322, 1324, 1328–1329, and the "None of the reviewed articles…" quotation (p. 1335).
  - s2: Table 1 definitions (p. 1326).
  - s3 and figure 1: the prevalence ranges and the caution quotation.
  - s4: "Diminished sport and academic performance" and "Safe sporting environments…".
  - s6: "passive inactions…" and Table 4.
  - s14: the hazing and bullying estimates.
  - s16: three quotations.
- Willson 2022 (s3, figure 2, Sources): 75%, 68.8%, 60.2%, 20.5%, 14.3%, mean age 27.7, response rate 16%, pages, online date.
- Mountjoy (s2, Sources): Box 1 on page 3 of the online-first version; volume, issue and pages against Crossref.
- s4: SP3's two studies (cross-unit).
- s7, s17: SP7's claims (cross-unit).
- s15: the International Safeguards document.
- Sources: bibliographic fields for Fletcher & Sarkar, Kegelaers and Bartholomew 2010.
- s11: the NSPCC away-day page.

## Confirmed
- Mountjoy 2016: all quotations, including Box 1, "This definition equally applies to coaches and athlete entourages", the core-of-all-forms statement, bystander effect, grooming, rough-and-tumble handling, and "with implementation". https://bjsm.bmj.com/content/50/17/1019
- Tuakli-Wosornu 2024: 15-member panel, ≥80% agreement, 14 authors, citation. https://research.edgehill.ac.uk/en/publications/ioc-consensus-statement-interpersonal-violence-and-safeguarding-i/
- Adams 2024: 20 athletes, mean age 26.0, nine sports; "dumb and stupid"; yelling; humiliation; neglected development; bear crawls "until somebody would throw up"; 45-minute sprints; punishment tied to performance accepted, other punishment called abusive; power and control. https://www.frontiersin.org/articles/10.3389/fspor.2024.1428682/full
- Zach 2024: n = 440, mean age 27.6, 14 interviewed; about 30%, about half, about 28%; jump rope for 2.5 hours; three quotations; harm recognised after stopping; "yelling spurred". https://www.mdpi.com/2076-328X/14/6/486/htm
- Vertommen 2016: 38%, 11%, 14%, and the groups reporting more. https://research.wur.nl/en/publications/interpersonal-violence-against-children-in-sport-in-the-netherlan/
- Willson 2022: n = 995, perpetrators, women reported more. https://www.pubmed.gov/34549664/
- Parent 2023: 983 aged 14–18, convenience sample, six schools; 59.2%, 23.8%, 10.6%; 54.0% inconsistent with its count of 228. https://mdpi.com/2076-0760/12/6/336
- Willson 2025: n = 794, over 16, mean age 27.85; r = −.32, .31, .25; the quoted themes; performance not measured. https://www.frontiersin.org/articles/10.3389/fspor.2024.1406775/full
- Li J 2025: n = 301, three waves, r = 0.536, performance not measured. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1643356/full
- Fletcher & Sarkar 2016: both quotations from the notes; no test of the programme. https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496
- Ríos 2022: 11 people aged 17–27, bullied at 10–16; "took it as a joke"; coaches rarely ended the bullying. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.819981/full
- McCleery 2025: 332 reflections, one private school, 2019–2023, running as punishment, "not generalizable". https://www.mdpi.com/2673-995X/5/1/12
- Li H 2025: 24 trials, pressure-training footballers, no harm outcome. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1621635/full
- de Bie 2024: "must not be used as an excuse"; nothing measured. https://www.frontiersin.org/articles/10.3389/fpsyg.2024.1501014/full
- St-Pierre 2022: all eight percentages, 1967–2020, male coaches, "tip of the iceberg". https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.856798/pdf
- NSPCC Sport:
  - Physical contact (7 Aug 2025): https://sport.nspcc.org.uk/resource-library/best-practice/physical-contact-and-young-people-in-sport/
  - Online safety (14 Feb 2025): https://sport.nspcc.org.uk/help-advice/topics/online-safety/
  - Grooming (16 June 2025): https://sport.nspcc.org.uk/resource-library/best-practice/protecting-children-in-sport-from-grooming-and-sexual-abuse/
  - Positions of trust (2 Jan 2024): https://sport.nspcc.org.uk/resource-library/best-practice/abuse-of-positions-of-trust-within-sport/
  - Changing facilities (6 Aug 2026): https://sport.nspcc.org.uk/resource-library/best-practice/safe-use-of-changing-facilities/
  - Overnight trips (28 June 2022): https://sport.nspcc.org.uk/resource-library/best-practice/overnight-trips-and-international-travel/
  - Deal with a concern, quotation and route: https://sport.nspcc.org.uk/help-advice/deal-with-a-concern/
  - Sept 2025 news page: https://sport.nspcc.org.uk/news-and-blogs/2025-09-free-training-about-new-law-on-reporting-child-sexual-abuse/
- Home Office factsheet (30 Sept 2026): regulated activity, England, coaches named, no start date. https://www.gov.uk/government/publications/crime-and-policing-act-2026-factsheets/crime-and-policing-act-2026-independent-inquiry-into-child-sexual-abuse-recommendations-factsheet
- Sport Integrity Australia: https://www.sportintegrity.gov.au/what-we-do/safeguarding/safeguarding-reporting
- Abuse-Free Sport: https://abuse-free-sport.ca/about
- MAAPP 2025 model: Part I reporting mechanism; Part III; Part IV gifts and social media; 8:00 a.m. to 8:00 p.m.; coaches should not massage. https://uscenterforsafesport.org/2025-maapp
- MAAPP as adopted by the USOPC: "observable and interruptible", individual sessions, hotel room, room checks, locker-room recording, "Open and Transparent". https://maapp.uscenterforsafesport.org/wp-content/uploads/2025/01/USOPC_MAAPP_01.01.25.pdf
- Wilson & Rhind 2022: the eight safeguards; about 400 contacted, 50 analysed; 42.5–72.5%; two safeguards under half. https://mdpi.com/2076-0760/11/8/322
- Bibliographic records:
  - Low: https://researchportal.hw.ac.uk/en/publications/pressure-training-from-research-to-applied-practice/
  - Kent: https://informahealthcare.com/doi/full/10.1080/10413200.2020.1868618
  - Bartholomew 2009: https://research-portal.uea.ac.uk/en/publications/a-review-of-controlling-motivational-strategies-from-a-self-deter/
  - Bartholomew 2011: https://ueaeprints.uea.ac.uk/id/eprint/64358/
  - Gervis & Dunn: https://www.ojp.gov/ncjrs/virtual-library/abstracts/emotional-abuse-elite-child-athletes-their-coaches
  - Stirling & Kerr: https://ibl.kb.nl/article/0000000120356//4/4
- Deliverable A counts: questions 1 and 6 are failed by 8 comments each, question 3 by 7 (recounted).
