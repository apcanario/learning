---
audit: quality review
unit: SCE12 · The sale
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: Opus 5.5 (claude-opus-5-5)
date: 2026-11-28
chat: https://claude.ai/code/session_01KMmgQzMe8qwXyeLryD2JaE
verdict: fix · 1 errors, 8 should-fix, 9 minor
---

The reviewer's final report, verbatim, from its hand-back (saved by the main chat; the agent's Write was to its own packet folder). Saved before any finding was applied. Run for F137, on SCE12 as corrected by the fresh check. Möller and Salminen's Sources entry was applied in place and then moved to its alphabetical place by the chat.

claude-opus-5-5

# Quality review: SCE12 "The sale" (Supply Chain Execution for Product Teams), as corrected

Run 28 Nov 2026 by a fresh Opus 5.5 agent with live search (WebSearch, then WebFetch only on URLs those searches returned). It was not shown the writing or any earlier check. Scope: the seven passes of the fresh check (audit-units §3, with figures (7)), the brief, sourcing-standard Parts 1 and 8, case-facts.md, pointers into filed/, and flags F2, F128, F129, F130, F132, F134 and F137.

## Findings

[error] [accuracy] §4 "Who sits on the panel"; Current: "both name business, technical, financial and procurement members, as SCE11 §3 does"; Problem: the New Zealand page names neither a business owner nor a procurement member. It lists "technical specialists, cultural, financial or legal expertise". Only VITA names all four. Fix: "VITA names business, technical, financial and procurement members, as SCE11 §3 does, and New Zealand names technical and financial expertise"; Basis: NZ Government Procurement, "Setting up the evaluation panel" (pub. 5 Oct 2017, mod. 9 Feb 2021), https://procurement.govt.nz/procurement/guide-to-procurement/plan-your-procurement/setting-up-the-evaluation-panel; VITA 24.3.1.

[should-fix] [attribution] §7; Current: "An earlier paper by Möller and Salminen (Moller on the page) notes"; Problem: the copy of the article hosted by the IMP Group (papers/4788.pdf) gives the authors as Risto T. Salminen and Kristian Möller, Vol. 13(1). A citing article's reference list also gives "Saliminen, R. T. and Moller, K. 2006 … 13(1): 1–51". The landing page's order is the only source for Möller first. Fix: "An earlier paper by Salminen and Möller (the IMP Group's page lists Moller first; the copy it hosts gives Salminen first) notes"; Basis: https://impgroup.org/wp-content/uploads/wpallimport/files/papers/4788.pdf; https://informahealthcare.com/doi/ref/10.1080/15470620802024905.

[should-fix] [attribution] §7 link text; Current: "[Möller & Salminen, "Role of References in Business Marketing – Towards a Normative Theory of Referencing", *Journal of Business-to-Business Marketing* 13, 2006]"; Problem: same as above. The issue number is also missing. Fix: "[Salminen & Möller, "Role of References in Business Marketing – Towards a Normative Theory of Referencing", *Journal of Business-to-Business Marketing* 13(1), 2006]"; Basis: as above.

[should-fix] [attribution] Sources; Current: "- Möller, K. & Salminen, R. T. (2006). Role of References in Business Marketing – Towards a Normative Theory of Referencing. *Journal of Business-to-Business Marketing* 13, 1–51, as the IMP Group's page gives it"; Problem: the author order and issue do not match the hosted copy or a citing reference (Part 8: Sources entries match the record). The entry also moves to its alphabetical place under S. Fix: "- Salminen, R. T. & Möller, K. (2006). Role of References in Business Marketing – Towards a Normative Theory of Referencing. *Journal of Business-to-Business Marketing* 13(1), 1–51, as the copy on the IMP Group's site gives it (its landing page lists Moller first)"; Basis: as above.

[should-fix] [accuracy/pointer] §6 "The shift"; Current: "The people who will use the system every shift are often not in the room (SCE11 §5)."; Problem: SCE11 §5 says "nothing opened says how often warehouse users are among them" and that the users' place "varies". "Often" goes further than the unit it cites. Fix: "The people who will use the system every shift may not be in the room; nothing opened says how often they are (SCE11 §5)."; Basis: filed/SCE11 §5.

[should-fix] [pointer] §6 "The shift"; Current: "A scenario watched on a projector is not a picker's shift on a handheld (SCE5 §2)."; Problem: SCE5 §2 covers headcount and learning time. Handhelds as working conditions are SCE5 §3. Fix: "A scenario watched on a projector is not a picker's shift on a handheld (SCE5 §3)."; Basis: filed/SCE5 §§2–3.

[should-fix] [coverage: flags F129, F130] Opening limits; Current: "The analyst firms' templates are paid, so only their public pages were read."; Problem: F130 asked SCE12 to retry Gartner's buying-guide and toolkit document pages and date what it read. F129 asked it to retry Webster and Wind (1972) and Ehret et al. (2024). The unit body records neither outcome. Its searches for them returned no SAGE or ScienceDirect page (nor did this reviewer's). Fix: "The analyst firms' templates are paid, so only their public pages were read; no Gartner buying guide, toolkit or market guide was read here (flag F130). Robinson, Faris and Wind (1967) and Webster and Wind (1972) were not opened either (flag F129); section 1 gives them as Grewal et al. (2015) describe them."; Basis: syllabus-flags F129, F130; unit Sources (neither listed).

[should-fix] [attribution/style] §3 first bullet; Current: "surveyed 3,500 "global software buyers" (roles, dates and company sizes not given on the page). Gartner owned the Capterra, Software Advice and GetApp review sites; on 29 January 2026 G2 announced that it had agreed to acquire them ([G2, 29 Jan 2026](https://company.g2.com/news/g2-acquires-capterra-software-advice-getapp)) [vendor-reported]: reviews were voted"; Problem: the colon after the G2 citation makes Gartner Digital Markets' findings read as G2's. Fix: "surveyed 3,500 "global software buyers" (roles, dates and company sizes not given on the page; Gartner owned the Capterra, Software Advice and GetApp review sites, and on 29 January 2026 G2 announced that it had agreed to acquire them ([G2, 29 Jan 2026](https://company.g2.com/news/g2-acquires-capterra-software-advice-getapp)) [vendor-reported]). In that survey, reviews were voted"; Basis: Gartner Digital Markets, 2025 Software Buying Trends page; G2 release of 29 Jan 2026 (both opened).

[should-fix] [accuracy: inference scope] §3 "Who is absent by rule"; Current: "A buyer whose long list is a Magic Quadrant's vendor list has left out every single-region vendor before looking at a product (this unit's inference from SCE6)."; Problem: SCE6 read only the 2022 inclusion criteria, and says a 2026 edition exists that it could not read. The sentence applies the 2022 rule to any Magic Quadrant. Fix: "A buyer whose long list was the 2022 Magic Quadrant's vendor list had left out every single-region vendor before looking at a product (this unit's inference from SCE6; the 2026 edition's criteria were not read)."; Basis: filed/SCE6 §§2, 8.

[minor] [attribution] §1; Current: "as covering information gathering, product evaluation and negotiation, and purchase and usage; it links that process to "creeping commitment", where each choice removes some alternatives (pp. 195, 200)"; Problem: the classic-view passage runs over pp. 200–201, and "creeping commitment" is on p. 201. Fix: "as covering information gathering, product evaluation and negotiation, and purchase and usage; it links that process to "creeping commitment", where each choice removes some alternatives (pp. 195, 200–201)"; Basis: Grewal et al. 2015, https://link.springer.com/content/pdf/10.1007/s40547-015-0040-5.pdf.

[minor] [accuracy] §1; Current: "A survey of ERP selection in midsize and large organisations addressed"; Problem: the abstract describes "an empirical study concerning differences" in the selection process "between small or medium and large sized organizations". It does not call the study a survey or limit it to midsize firms. Fix: "An empirical study comparing ERP selection in small or medium-sized and large organisations addressed"; Basis: Bernroider & Koch 2001 abstract, https://emerald.com/insight/content/doi/10.1108/14637150110392746/full/html.

[minor] [coverage] §1; Current: "Their article proposing a six-stage model of the buying process for ERP software (*Industrial Marketing Management*, 2003) was not found at its publisher's page and carries nothing here."; Problem: a library record gives the DOI 10.1016/S0019-8501(03)00007-5 (IMM 32(7), 585–594). That gives the next writer a route to the publisher page. The paper bears directly on the brief's stages. Fix: "Their article proposing a six-stage model of the buying process for ERP software (*Industrial Marketing Management* 32(7), 2003; DOI 10.1016/S0019-8501(03)00007-5, as a library record gives it) was not opened at its publisher's page and carries nothing here."; Basis: https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_204478522.

[minor] [accuracy] §5; Current: "groups its rows by function (finance, grants, procurement and supply chain with an inventory subsection of 11 rows, human resources, payroll, projects, reporting, general system)"; Problem: the list leaves out section 4.7, e-government services. Fix: "groups its rows by function (finance, grants, procurement and supply chain with an inventory subsection of 11 rows, human resources, payroll, projects, e-government services, reporting, general system)"; Basis: https://birminghamal.gov/wp-content/uploads/2024/08/RFP-Section-4.pdf.

[minor] [accuracy] §8; Current: "mentions "evaluation-phase tests/pilot programs" among the teams' tasks"; Problem: on VITA's page this is a task of the subject matter experts, who "may assist business owner/customer in conducting evaluation-phase tests/pilot programs". Fix: "mentions "evaluation-phase tests/pilot programs", in which subject matter experts may assist the business owner"; Basis: VITA 24.3.1.

[minor] [accuracy] §3 third bullet; Current: "The release's other main figure concerns AI, which this course does not treat."; Problem: the release has two other main figures. One is about AI (45%). The other is not: confident buyers are twice as likely to report a high-quality deal, which bears on §10. Fix: "The release's other main figures are on AI use, which this course does not treat, and on decision confidence: confident buyers were twice as likely to report a high-quality deal."; Basis: Gartner press release, 9 Mar 2026 (opened).

[minor] [figure] Deliverable B matrix; Current: ""tone": 2, "cells": ["in", "in", "in", "scores", "in", "calls", "in", null]"; Problem: the S7 block says Ravi's team takes part "if run", but the cell says plain "in". Fix: ""tone": 2, "cells": ["in", "in", "in", "scores", "in", "calls", "if run", null]"; Basis: unit, block S7 row 2.

[minor] [sources] Sources lead line; Current: "All addresses opened on 28 November 2026; the source log gives what was read at each."; Problem: the unit cites some sources only through filed units and does not list them here: Gartner's press release of 13 Apr 2022 (SCE11), Gartner's 2024 methodology note (SCE1), Forrester RES181465 (SCE11), Olson et al. 2012 / Keil and Tiwana (SCE11). Part 1 asks that every cited source be listed. SCE9 sets the precedent of a pointer sentence. Fix: "All addresses opened on 28 November 2026; the source log gives what was read at each. Sources cited only through earlier units (Gartner's press release of 13 April 2022; Gartner's 2024 Magic Quadrant methodology note; Forrester RES181465; Olson, Johansson and de Carvalho 2012, for Keil and Tiwana) are listed in SCE1 and SCE11."; Basis: sourcing-standard Part 1; filed/SCE9 Sources line.

[minor] [style] Opening limits; Current: "what transfers is the shape of the documents, not the rules (this unit's inference)"; Problem: this is a contrastive construction of the kind the brief's tone rule bars. Fix: "what transfers is the shape of the documents; the rules stay with the public body (this unit's inference)"; Basis: brief, Tone.

## Confirmed (opened with live search, 28 Nov 2026)

- Grewal et al. 2015: BuyGrid "sequential"; "These processes are contemporaneous rather than sequential" (p. 195); classic view crediting Robinson et al. and Webster & Wind. PASS.
- Gartner, "The B2B Buying Journey": six jobs; "doesn't play out in any kind of predictable, linear order"; 17%; "5% or 6%"; undated. PASS.
- Info-Tech RFP process: seven steps; RFI/RFP advice; published 11 Aug 2020, modified 24 Jul 2023. PASS.
- Verville & Halingten 2002, *Management Decision* 40(3), 206–216: about six months; "iterative, recursive and inter-related"; "non-typical of their normal procurement practices". PASS.
- Baki & Çakar 2005, BPMJ 11(1), 75–86: fit with parent/allied systems most important, then cross-module integration, compatibility, vendor references; no sample in the abstract. PASS.
- Howcroft & Light 2008, JEIM 21(6), 597–615, quote and setting (small consultancy, CRM). PASS. Howcroft & Light 2010, JAIS 11(3), longitudinal case in a small organisation, "best technology solution". PASS.
- Gartner MQ page (gartner.co.uk), both quotes, "focussing" spelling, undated. PASS.
- Forrester Wave methodology: "a guide for buyers…"; "Forrester interviews or surveys the reference customers provided by the vendor"; last modified 28 Apr 2026. PASS.
- Gartner Peer Insights About: quote, verification, headline "Gartner acquires Pulse…". PASS.
- G2 Research Scoring Methodologies: Grid quote, 10 reviews, "should not segment…", non-incentivised reviews weighted more, published 21 Nov 2023, updated 26 Oct 2026. PASS.
- Gartner Digital Markets 2025 report: 3,500; 83%; reviews most influential; 2.5; 62%; 59%; undated. PASS. About page: a business unit of Gartner serving buyers and providers. PASS.
- G2, 29 Jan 2026: agreed to acquire Capterra, Software Advice and GetApp. PASS.
- TrustRadius release, 15 Jul 2026: 1,862 buyers and 444 vendors, January 2026; 74%; 13% with a 63% decrease since 2022; demos, trials, reviews and prior experience among the most influential, with no percentage for demos. PASS.
- Gartner, 9 Mar 2026: 646 buyers, Aug–Sep 2025, 67%. PASS (see minor finding).
- Gartner, 12 Jul 2022: 1,120; Nov–Dec 2021; three regions; 56%; peak before implementation; 7–10 months; 67% outside IT. PASS.
- Gartner, 7 May 2025: 632 buyers, Aug–Sep 2024, 74%, 2.5 times. PASS.
- Gartner, 13 Apr 2022 (URL slug 2022-03-13): 74%, 26%, 75% delays. PASS.
- Washington DES RFI, 7 Feb 2024: non-obligation quote, hosting, MFA, roadmap quote, 50-minute virtual demo, no prices, draft requirements. PASS.
- Alabama ABC RFP, 17 Jul 2024: cross-docking and cycle counting (§3.2), D365 ERP integration, cloud, 14 months, itemised fixed prices and firm fixed cost, five references (§4.18), key personnel, six-year purchase-to-own, five criteria at 20%, §7.1 test clause. PASS.
- Pinellas RFP 24-01, 12 Jan 2024: §2.4.B weights; §2.4.A; §1.13 quotes; §1.14; §1.15 five years; §2.2.O–R; C.5; Attachment B rules. PASS.
- Mississippi RFP 4459 Att. A: Sections I–IX; 99.98% (VIII); WILL COMPLY / EXCEPTION; preliminary PMP, SDD, DMP and UATP; train-the-trainer for three to five SAs; service credits. PASS.
- UK Bid Evaluation guidance, May 2021: §§3.3.2, 3.3.4, 5.1, 9.2.1, 9.3.2, 6.3.7 quotes; no issuing department named. PASS.
- VITA 24.3.1: roles; "recommended… four corners"; SMEs "cannot score"; negotiation quotes; no end users. PASS.
- Birmingham matrix: S/F/C/P/N codes; 11 inventory rows; no title, date or issuer. PASS (see minor finding).
- ARC, both pages: criteria and issues as stated; no supplier named; second page has supplier analysis and profile sections and invites engagement; undated. PASS.
- Info-Tech demo template (H. Kwok; 10 Apr 2023 / 15 Oct 2026) quote. PASS. Info-Tech 2007 note (A. Hay; 18 Dec 2007 / 3 Apr 2012) quotes and steps. PASS.
- Jalkala & Salminen 2009 (IMP, Marseille): 38 interviews, four process and IT companies, the quoted functions. PASS.
- Möller/Salminen 2006: quote "very little reported academic research on references". PASS (author order: see finding).
- Pointers: SCE1 §§7, 8, 9, 10, 11 (C10, C13 row "Not searched here → SCE12"); SCE6 §§1, 2, 3, 4, 9, 11; SCE10 §§2, 7; SCE11 §§2, 3, 3.4, 3.6, 4, 6 and cards 1–6. All say what SCE12 says they say, apart from the SCE11 §5 and SCE5 §2 findings above.
- Case facts: every Corvane, Halvern and Kestrow fact agrees with case-facts.md and its "Added by units" rows (SCE5, SCE10, SCE11). "(fictional)" appears at first use. No case operation is said to use a real product.

## Figures (pass 7)

1. Flow, §1, "The eight stages of a selection". The labels and notes trace to §§1–9: "a need and a sponsor" (§2 "It ends when someone senior agrees to sponsor"), "non-binding" (§4 "it commits the buyer to nothing"), "price, plan, partner, terms" (§9). The caption names the section and the sources (Grewal p. 195, Gartner, Verville & Halingten). A sequence suits a flow. PASS.
2. Compare, §4, Pinellas weights 40/20/20/10/10. These match §4 ("weights functional requirements 40%…10% (§2.4.B)") and the RFP. The caption names the section, source and date. Numbers compared suit a compare. PASS.
3. Matrix, Deliverable B, "Who takes part in each stage at Corvane". The cells trace to blocks S1–S8 rows 2. The caption names the section and sources. Items by sections suit a matrix. FIX (minor): Ravi's S7 cell should read "if run"; the replacement JSON fragment is given above.

## Coverage (brief)

- Stages, trigger to contract, each attributed to research and published guides: covered (§§1–9).
- Requirements list on at least two published templates, and what kind of product it rewards: covered, using four public bodies' requirement documents (Alabama, Pinellas, Mississippi, Birmingham) and ARC's guide in place of free templates. The opening limits explain why vendor, integrator and magazine templates were excluded.
- What a scripted demonstration shows and cannot show: covered (§6). C13 is tested: no independent source found.
- Analyst reports and peer reviews in a long list, as their publishers describe them: covered (§3).
- References and why they weigh: covered (§7).
- Implementation plan and partner as part of what is bought: covered (§9).
- Public evidence on wins and losses, said to be thin: covered (§10).
- What a product team can change at each stage: covered (§11).
- Questions for sales and services colleagues: covered ("On a site visit").
- Self-check: 8 questions. The answers agree with the body; Q6 and Q7 checked against §§6 and 7.
- Deliverable: present in full. The form has the brief's six fields. It is built for Corvane in eight blocks with case labels and sources per line, followed by the template with described blanks and glossary lines. It follows from the evidence: every line carries a section or a "working" label. It can be used alone.
- Safety, vendors, AI, regions, tone: no real vendor is assessed, and AI is dismissed in one sentence each time it comes up. US, UK and NZ documents are labelled by region, and legal points are put as questions for counsel. One contrastive construction is noted above.

Flags:
- F2: C13 is now tested in §6. At filing, SCE1 §11's C13 row needs SCE12's result by the correction route, as was done for C11 and C12.
- F128: met in part. VITA and NZ are opened and compared with SCE11's roles (§4), and the SCE11 correction note shows the regrading went by the correction route. No account specific to warehouse, transport or order system selection staffing was opened; §4's last sentence says so in substance.
- F129, F130: not recorded in the unit body (should-fix above).
- F132: the unit uses the register's unnamed procurement function and integrator. "Corvane's legal counsel" (S4, S8) and the vendors reaching each stage are new case assumptions; they must appear in the notes, which this review was not given.
- F134: SCE12's new references (Grewal et al., Bernroider & Koch, Baki & Çakar, the public-body documents, Jalkala & Salminen, Salminen & Möller, Info-Tech, G2, TrustRadius) are for the bibliography at filing.
- F137: this review.

## What I could not verify

- The unit's source log, notes (case facts added) and unsure list. unit.md refers to all three, but notes.md and unsure.md were empty and no source log was in the packet, so the Part 8 checks "every reference is in the source log" and "invented case facts are listed" could not be run.
- `python3 kit/private_terms.py`: not run (no kit in the packet). A read-through found nothing about the Project's owner or employer.
- Info-Tech RFI advice wording "the solutions or the viable vendors": only "in-depth knowledge of the market" was returned in the part of the page read (the fetch covered 100,000 of 141,875 characters).
- Möller/Salminen 2006 at the journal publisher (Taylor & Francis/Haworth): no publisher record was returned by search. The author order rests on the hosted PDF and one citing reference.
- Verville & Halingten 2003 (IMM) at ScienceDirect: not returned by search; only a library record.
- Webster & Wind (1972) at SAGE and Ehret, Johnston & Ritter (2024) at ScienceDirect (F129): neither page was returned by search.
- Gartner buying guides and toolkits (F130): not searched beyond the public pages the unit cites.
- Pinellas RFP: the final ~600 characters were beyond the fetch window. Gartner Digital Markets 2025 report: its survey fieldwork date is not on the page.

Verdict: fix (1 error, 8 should-fix, 9 minor; 3 figures: 2 PASS, 1 FIX)
