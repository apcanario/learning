---
code: DD-SP1
kind: quality-review (rule 13)
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgR35wf5wmG58AbjrCFw
note: report returned as the agent reply (harness blocked its file write) and saved verbatim by the chat
---
Verdict: QR-DD-SP1 · fix · 0 error, 14 should-fix, 9 minor
Model: claude-opus-5-5. The harness refused the write to /tmp/w/qr-DD/out/report.md, so the whole report follows. The unit was not edited.
Totals: 23 findings, 13 claim groups that could not be verified, 27 references opened and 12 not opened.

# Quality review (rule 13): DD-SP1, Deep dive: the coach's line with minors

Reviewer: claude-opus-5-5, a fresh agent with live search, 19 Nov 2026. The unit was reviewed as it stands in files/DD-SP1.md, against briefs/DD-SP1.txt, sourcing-standard.md Parts 1 and 7, case-facts.md, syllabus-flags.md and flags-given-to-unit.txt.

## Pass 1. Claims: FIX
Most claims hold at source. Four overstate what their source says (Willson et al., 2025; Ríos et al., 2022; Zach et al., 2024; Fletcher and Sarkar, 2016). The 2024 IOC statement could not be opened.

## Pass 2. Bibliography: FIX
Every journal entry that was opened matches the publisher's record. Four NSPCC Sport addresses (contact, concern, online safety, positions of trust), each cited in the text and in Sources, were never returned by search; search returns each page at a different path. One page title also differs.

## Pass 3. Source log: FIX
Claims that rest on an abstract say so (Vertommen; Fletcher and Sarkar). Section 8's table still carries consequences from three references that no unit opened at an accepted address. Kent et al.'s publisher page, which the unit says refused, opened for this review.

## Pass 4. Grades: FIX
Every technique and recommendation carries a grade from SP1's key, and each grade fits its evidence, with one exception: a recommendation in section 2 has no grade. The "five correlational studies" behind the section 4 grade cannot be counted from the text.

## Pass 5. Population: PASS
Every finding names its sample and design. Transfers from adults, students and retrospective samples to under-18s are labelled as inference.

## Pass 6. Scope and safety: PASS
- Nothing teaches assessment, diagnosis or treatment.
- No weight-loss method, calorie figure, target weight or self-harm method appears.
- Every law is given as the issuing body's statement and put as a question.
- No real person is named.
- The line saying the unit is information, not advice, is in the preamble.

## Pass 7. Any sport: PASS
Counting example instances, football supplies about 11 of 36 (31%), judo about 8, athletics about 7, and other sports about 10. Deliverable E is all football because SP10 reserves its rows on Milan's plan; if those rows are counted one by one, football comes close to a third. kit/private_terms.py is outside the packet and was not run.

## Brief, deliverable, flags and Part 7

**Brief.** Every Cover item is present. Two are met only in part, and the unit says so:
- The categories of emotional abuse: Stirling and Kerr (2008) and Gervis and Dunn (2004) were not opened.
- A published critique of the challenge-and-support model: none was found.

The length is about 10,100 words against the brief's 2,000 to 6,000 (finding below).

**Deliverable.** Parts A to D, plus E, are each built on the case squads and then given as a template.
- The twelve comments come four each from judo, football and athletics. Each is run through the card and rewritten.
- The counts of questions failed (8, 8 and 7) recount correctly.
- One rewrite and two table alternatives fail the unit's own section 8 tests (findings below).

**Case.** Every case fact checked agrees with case-facts.md. Each athlete is labelled "(fictional)" on first use, added facts are marked, and the case is never used as evidence.

**Flags.**
- F5, F27 and F31: recorded as unmet, with reasons. This review also found only repository copies of the Bartholomew papers.
- F8, F14 and F47: dealt with in the preamble.
- F34: dealt with.
- F78, F79 and F82: dealt with in section 8.
- F101: dealt with in section 17.
- F102: respected.
- F134 and F139: dealt with in section 15.
- F168: dealt with in section 18 and Deliverable E.
- F24, F38, F123 and F124: need no action from this unit.
- Not dealt with or not recorded: F86, F158, and the part of F121 and F134 about the NSPCC overnight-trips page (findings below).

**Part 7, line by line.** Passes every line except these:
- Bibliography entries: the NSPCC addresses.
- Grades: one recommendation ungraded.
- Source log: sources.md is not in the packet.
- Private terms: the script was not run.
- Dated codes: the overnight-trips page is missing.

**Read as the preamble's coach.** The unit is usable. Section 8's line is its most useful new rule, which is why its own alternatives must pass its own tests.

## Findings

- [should-fix] [accuracy] Deliverable A, comment 5; Current: "Miss the standard and your side starts the next game a goal down."; Problem: one player's miss puts the cost on his teammates, failing section 8's test 5, and the cost carries past the drill, failing test 4; Fix: "Miss the standard and the other side gets the ball, in this drill only."; Basis: the unit, section 8, tests 4 and 5
- [should-fix] [accuracy] Section 8, table, deselection row; Current: "Start the next practice game a point down"; Problem: the consequence carries past the drill, failing test 4; Fix: "Lose the point in this drill"; Basis: the unit, section 8, test 4
- [should-fix] [accuracy] Section 8, table, team-sprints row; Current: "The team starts the next scrimmage a point down"; Problem: the consequence carries past the drill, failing test 4; Fix: "The team loses the point in this drill"; Basis: the unit, section 8, test 4
- [should-fix] [attribution] Section 4, Willson et al. bullet; Current: "The authors note that athletes and coaches often justify harsh coaching as necessary for results, that some athletes said it made them work harder, and that abuse may be masked by success and recognised only after retirement"; Problem: the justification, the "work harder" accounts and recognition after retirement come from earlier studies the authors cite, not from this sample; masking by success is the authors' untested interpretation; Fix: "Citing earlier studies, the authors note that athletes and coaches often justify harsh coaching as necessary for results and that some athletes said it made them work harder; they suggest, without testing it, that abuse may be masked by success, and cite earlier studies in which athletes recognised it only after retirement"; Basis: https://frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1406775/full
- [minor] [accuracy] Section 6, Ríos et al. bullet; Current: "teammates who saw it mostly stayed out, sided with the aggressor, or "took it as a joke"; the participants linked this partly to fear of being targeted next."; Problem: the paper says bystanders "did not always react"; only one participant linked their silence to fear; Fix: "teammates who saw it often did not step in, and some sided with the aggressor or "took it as a joke"; one participant linked this to bystanders' fear of being harmed if they helped."; Basis: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.819981/full
- [minor] [attribution] Section 4, selected sample; Current: "some athletes recognised harm only after they stopped, as Zach et al. report from their interviews"; Problem: the paper reports this from one interviewee, not as a theme; Fix: "some athletes recognised harm only after they stopped, as one of Zach et al.'s interviewees said"; Basis: https://mdpi.com/2076-328X/14/6/486
- [minor] [attribution] Section 4, challenge-and-support model; Current: "The model in the course's reading holds that performance thrives where challenge and support are both high."; Problem: the abstract and notes opened do not state the model where both are high; Fix: "The model in the course's reading holds that performance thrives where challenge and support are both high; the abstract and notes opened do not state it in those words."; Basis: https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496
- [should-fix] [attribution] Section 5, question 5; Current: "updated 7 Aug 2025, read 19 Nov 2026](https://sport.nspcc.org.uk/resources-and-tools/best-practice/physical-contact-and-young-people-in-sport/)"; Problem: no search returned this address; the page is at another path; Fix: "updated 7 Aug 2025, read 19 Nov 2026](https://sport.nspcc.org.uk/resource-library/best-practice/physical-contact-and-young-people-in-sport/)"; Basis: https://sport.nspcc.org.uk/resource-library/best-practice/physical-contact-and-young-people-in-sport/
- [should-fix] [attribution] Sources, NSPCC physical contact; Current: "Updated 7 Aug 2025. https://sport.nspcc.org.uk/resources-and-tools/best-practice/physical-contact-and-young-people-in-sport/"; Problem: as above; Fix: "Updated 7 Aug 2025. https://sport.nspcc.org.uk/resource-library/best-practice/physical-contact-and-young-people-in-sport/"; Basis: as above
- [should-fix] [attribution] Section 14, another coach; Current: "undated, read 19 Nov 2026](https://sport.nspcc.org.uk/help-and-advice/deal-with-a-concern/)"; Problem: no search returned this address; the page is at /help-advice/; Fix: "undated, read 19 Nov 2026](https://sport.nspcc.org.uk/help-advice/deal-with-a-concern/)"; Basis: https://sport.nspcc.org.uk/help-advice/deal-with-a-concern/
- [should-fix] [attribution] Sources, NSPCC concern; Current: "Undated. https://sport.nspcc.org.uk/help-and-advice/deal-with-a-concern/"; Problem: as above; Fix: "Undated. https://sport.nspcc.org.uk/help-advice/deal-with-a-concern/"; Basis: as above
- [should-fix] [attribution] Section 12, NSPCC online safety; Current: "[NSPCC Sport, *Online safety and social media in sport*, updated 14 Feb 2025, read 19 Nov 2026](https://sport.nspcc.org.uk/help-and-advice/topics/online-safety-and-social-media/)"; Problem: no search returned this address; the page with these words and this date is titled "Online safety in sport" and sits at another path; Fix: "[NSPCC Sport, *Online safety in sport*, updated 14 Feb 2025, read 19 Nov 2026](https://sport.nspcc.org.uk/help-advice/topics/online-safety/)"; Basis: https://sport.nspcc.org.uk/help-advice/topics/online-safety/
- [should-fix] [attribution] Sources, NSPCC online safety; Current: "NSPCC Sport. *Online safety and social media*. Updated 14 Feb 2025. https://sport.nspcc.org.uk/help-and-advice/topics/online-safety-and-social-media/"; Problem: as above; Fix: "NSPCC Sport. *Online safety in sport*. Updated 14 Feb 2025. https://sport.nspcc.org.uk/help-advice/topics/online-safety/"; Basis: as above
- [should-fix] [attribution] Section 13, positions of trust; Current: "read 19 Nov 2026](https://sport.nspcc.org.uk/resources-and-tools/best-practice/preventing-abuse-in-positions-of-trust-in-sport-and-activity/)"; Problem: no search returned this address; the page with this title and date is at another path; Fix: "read 19 Nov 2026](https://sport.nspcc.org.uk/resource-library/best-practice/abuse-of-positions-of-trust-within-sport/)"; Basis: https://sport.nspcc.org.uk/resource-library/best-practice/abuse-of-positions-of-trust-within-sport/
- [should-fix] [attribution] Sources, NSPCC positions of trust; Current: "Updated 2 Jan 2024. https://sport.nspcc.org.uk/resources-and-tools/best-practice/preventing-abuse-in-positions-of-trust-in-sport-and-activity/"; Problem: as above; Fix: "Updated 2 Jan 2024. https://sport.nspcc.org.uk/resource-library/best-practice/abuse-of-positions-of-trust-within-sport/"; Basis: as above
- [should-fix] [coverage] Section 11, F121 and F134; Current: "SP9 dated the same body's page on away day trips (updated 24 Nov 2022) and the U.S. code's travel rule; this unit adds nothing to SP9's ratio question (SP9, section 10)."; Problem: the NSPCC overnight-trips page is neither dated nor recorded as not opened; Fix: "SP9 dated the same body's page on away day trips (updated 24 Nov 2022) and the U.S. code's travel rule; the same body's *Overnight trips and international travel* page (updated 28 June 2022, read 19 Nov 2026) puts its accommodation and emergency guidance in a downloadable document, which was not opened; this unit adds nothing to SP9's ratio question (SP9, section 10)." (and the page added to Sources); Basis: https://sport.nspcc.org.uk/resource-library/best-practice/overnight-trips-and-international-travel/
- [minor] [coverage] Unsure list, F86; Current: "7. Kent et al. (2022), Kegelaers et al. (2021) and Low et al. (2024): not opened for this unit; their consequences in section 8's table are as SP6 reports them."; Problem: F86 names this unit and is not recorded; Fix: "7. Kent et al. (2022), Kegelaers et al. (2021) and Low et al. (2024): not opened for this unit; their consequences in section 8's table are as SP6 reports them. F86's other references (Bell et al., 2013; Stoker et al., 2017; the choking-interventions review; Mesagno and Beckmann, 2017; Ivarsson et al., 2017; Rupprecht et al., 2024) were not sought for this unit: F86 carried, unmet."; Basis: syllabus-flags.md F86
- [minor] [coverage] Unsure list, F158; Current: "8. International Safeguards for Children in Sport (2014): the document was not opened; its eight safeguards are named from Wilson and Rhind (2022)."; Problem: F158 (Neely et al., 2016) names this unit and is not recorded; Fix: "8. International Safeguards for Children in Sport (2014): the document was not opened; its eight safeguards are named from Wilson and Rhind (2022). Neely et al. (2016), on deselection, was not sought for this unit: F158 carried, unmet."; Basis: syllabus-flags.md F158
- [should-fix] [coverage] Unsure list, length; Current: "11. Length: about 10,100 words before the Deliverable (about 9,800 without the figure blocks), above the brief's 2,000 to 6,000; the brief's Cover list names eighteen topics."; Problem: the unit is about 4,000 words over the brief's ceiling and no flag is raised; meeting the ceiling needs either a brief change or cuts that would drop Cover items; Fix: "11. Length: about 10,100 words before the Deliverable (about 9,800 without the figure blocks), above the brief's 2,000 to 6,000; the brief's Cover list names eighteen topics, which this unit could not cover in 6,000 words. Raised as a flag for the syllabus review; the length stands until it is decided."; Basis: briefs/DD-SP1.txt
- [minor] [label] Section 2, the coach's part; Current: "You do not decide whether what someone else did meets a definition: that is the job of the person your safeguarding route names (section 15)."; Problem: the recommendation has no grade; Fix: "You do not decide whether what someone else did meets a definition: that is the job of the person your safeguarding route names (section 15) [practice; safeguarding guidance; the studies behind it were not opened]."; Basis: SP1's grade key as the unit's preamble restates it
- [minor] [label] Section 4, grade; Current: "what has changed is that it now rests on five correlational studies in athletes instead of three"; Problem: the section names only two of SP3's three studies, so the reader cannot count five; Fix: "what has changed is that it now rests on five correlational studies in athletes instead of three (SP3's three, Hu et al., 2023, among them, and the two above)"; Basis: syllabus-flags.md F27
- [minor] [attribution] Section 8, table preamble; Current: "which read them on repository copies):"; Problem: the rows carry content from references no unit opened at an accepted address; Fix: "which read them on repository copies; the rows are SP6's report, not this unit's finding, and carry no claim beyond it):"; Basis: sourcing-standard.md Part 7
- [minor] [attribution] Sources, Kent et al.; Current: "(named as SP6 reports it; publisher's page refused)"; Problem: the publisher's page opened for this review; it gives pages 691 to 712, online 25 Feb 2021, and 82 male players with mean age 14.12, and it does not describe the consequences in section 8's table; Fix: "(named as SP6 reports it; the publisher's page, opened at review on 19 Nov 2026, gives pages 691–712, online 25 Feb 2021, 82 male academy players of mean age 14.12, and does not describe the consequences)"; Basis: https://informahealthcare.com/doi/full/10.1080/10413200.2020.1868618

## Could not verify:
- Tuakli-Wosornu et al. (2024): no IOC, publisher, PubMed or DOI address was returned by any search, so no claim citing it could be checked. Among them: "psychological violence "from 21% to 79%", physical violence "from 4% to 66%", sexual violence between 0.5% and 78%, neglect "from 27% to 69%", overall interpersonal violence 44% to 86%, hazing 50% and bullying 17% to 61%"
- Tuakli-Wosornu et al. (2024): "produced by a 15-member expert panel from a scoping review and a RAND/UCLA appropriateness process with 80% agreement set in advance as consensus"
- Tuakli-Wosornu et al. (2024): "coaches sometimes wield immense power over athletes' careers"; "athletes may feel pressured to tolerate IV in exchange for the opportunity"; "hierarchical structures and administrative procedures"; "None of the reviewed articles focused primarily on promoting IV disclosure or reporting in sport"
- Tuakli-Wosornu et al. (2024), Table 1: "regular and deliberate use of a range of words and non-physical actions"; "an act attempting to cause, or resulting in, pain and/or physical injury"; "Any sexual act, attempt to obtain a sexual act, unwanted sexual comments or advances"; "the intentional use of physical force or power against other persons"
- Tuakli-Wosornu et al. (2024): "Diminished sport and academic performance"; "Safe sporting environments and high-performance sporting success can go hand in hand"; "passive inactions such as bystanding and enabling"; "awareness that these policies exist and are safe to access is low among athletes"; also its page numbers and author list
- Willson et al. (2022): "(mean age 27.7; response rate 16%) found that 75% reported at least one experience of harm: neglect 68.8%, psychological 60.2%, sexual 20.5%, physical 14.3%". The PubMed record confirms n = 995, the order of the forms, the perpetrators and the sex difference, but not these figures; volume, issue and pages also unchecked.
- Vertommen et al. (2016): the author list, volume and pages. The figures are confirmed.
- MAAPP 2025, the Center's own PDF (not returned by any search):
  - the Part numbers cited
  - "recommends sending messages only between 8:00 a.m. and 8:00 p.m. local time"
  - "recommends against private social media connections with minor athletes"
  - "The U.S. code recommends against personal gifts and allows gifts distributed equally to all athletes (MAAPP 2025, Part IV)"
  - "recommend that coaches do not massage minor athletes": the USOPC's adopted version says coaches "cannot provide" manual therapy to minor athletes, which is a requirement, and has no rule on hours or gifts
  - "require each organisation they cover to have a mechanism to receive reports of violations" (Part I)
- NSPCC Sport, positions of trust: "since 28 June 2022". The date was not in the text returned.
- SP3's figure as restated: "with lower need satisfaction and, through it, fear of failure in 252 athletes aged 10 to 25 and over". F27 lists SP3's studies as 103 boys and 479 handball players.
- SP6 and SP10 content as restated: "players aged 11 to 18 (Kent et al., 2022)"; "Basketball academy, players of about 18 (Kegelaers et al., 2021)"; "block 2 (weeks 21 to 24)"; "before week 1, then weeks 2, 8, 14, 22, 28 and 34"
- Not opened at an accepted address: Bartholomew et al. (2009, 2010, 2011); Stirling and Kerr (2008); Gervis and Dunn (2004); Low et al. (2024); Kegelaers et al. (2021), whose abstract page shows only a correction notice, doi 10.1080/10413200.2021.1917912; the International Safeguards (2014); the 2024 IOC statement.
- The unit's source log (sources.md) is not in the packet.

## Confirmed:
- **Mountjoy et al. (2016)**, at bjsm.bmj.com/content/50/17/1019:
  - every Box 1 definition as quoted
  - "at the core of all other forms"; emotional and psychological used interchangeably
  - "stem from abuses of power relations"; "concept of consent cannot apply to children"; "need to be cared for, protected and supervised"
  - "pervasive bystander effect" ... "prevents disclosure and seeking of help"; "passive attitudes/non-intervention, denial or silence"
  - the two grooming quotations; "Close proximity, frequent group interactions and rough-and-tumble handling"; "culturally specific policy and procedures, with implementation"
  - forced inappropriate physical activity within physical abuse
  - authors; volume 50, issue 17, first page 1019
- **Vertommen et al. (2016)**: 38%, 11% and 14%, and the groups reporting more (pubmed.ncbi.nlm.nih.gov/26516053; the NSPCC research page).
- **Willson et al. (2022)**: n = 995; coaches the most common perpetrators except of sexual harm (peers); female athletes reported more (pubmed.gov/34549664).
- **Parent et al. (2023)**: 983 adolescents aged 14 to 18; 59.2%, 23.8% and 10.6%; the 54.0% figure does not match its count of 228 of 967; record checked (mdpi.com/2076-0760/12/6/336).
- **Willson et al. (2025)**: 794 athletes over 16, mean age 27.85; r = −.316, .311 and .252; performance not measured; record checked.
- **Li J et al. (2025)**: 301 student-athletes, three waves three weeks apart; r = 0.536; record checked.
- **St-Pierre et al. (2022)**: every percentage cited; "tip of the iceberg"; record checked.
- **Zach et al. (2024)**:
  - 440 adults, mean age 27.6, 14 interviewed
  - about 30%, about half, about 28%
  - all four quotations; the two and a half hours of skipping
  - record checked
- **Adams et al. (2024)**: 20 athletes, mean age 26.0, nine sports; the power-and-control frame; every quotation; the conclusion; record checked.
- **Ríos et al. (2022)**: sample; "took it as a joke"; "work harder"; record checked.
- **McCleery et al. (2025)**: 332 reflections, one school, 2019 to 2023; the findings and the limit on generalising; record checked.
- **Li H et al. (2025)**: 24 trials; anxiety and performance outcomes only; no harms reported; record checked.
- **de Bie et al. (2024)**: a narrative review; "must not be used as an excuse"; record checked.
- **Wilson and Rhind (2022)**: the eight safeguards; 400 contacted, 50 analysed, 40 in Table 6; 42.5% to 72.5% fully in place, two under half; the limits; record checked.
- **Fletcher and Sarkar (2016)**: both quotations from the notes; no test of effects reported.
- **Bartholomew et al. (2009, 2011)**: search returned only repository copies, as the unit says.
- **NSPCC Sport pages**, each date as the unit gives it:
  - physical contact (7 Aug 2025): every quotation; "unlawful", with no jurisdiction named
  - deal with a concern (undated): the "need not decide" line and the route
  - online safety (14 Feb 2025): every quotation
  - grooming (16 Jun 2025): every quotation and sign
  - positions of trust (2 Jan 2024): the offence; consent does not make it legal
  - changing facilities (6 Aug 2026): two staff of the same sex as the children
  - proposed reporting law (15 Sept 2025): key roles, England, coaches included
- **Home Office factsheet** (updated 30 Sept 2026): England; regulated activity; coaches named as an example; no start date.
- **Sport Integrity Australia**: the three-step route.
- **Abuse-Free Sport**: winding down, no new reports, link to the new programme.
- **USOPC MAAPP, effective 1 Jan 2025**: observable and interruptible; annual consent for individual sessions; transport; hotel rooms; room checks; locker-room recording; manual therapy; "Open and Transparent".
- **Case facts**: every fact checked against case-facts.md agrees.
- **Deliverable A counts**: correct (8, 8 and 7).

Verdict: QR-DD-SP1 · fix · 0 error, 14 should-fix, 9 minor
