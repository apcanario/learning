---
audit: quality review
unit: SCE9
model: claude-opus-5-5
date: 2026-11-28
chat: https://claude.ai/code/session_01KMmgR1zm5V3ijatCgRUBSN
row: W-SCE10 (step 1b, flag F117)
note: the packet's brief.txt was SCE10's brief, not SCE9's (thin.py stage checker takes the row's unit); pass 7 could not check the deliverable against SCE9's own brief wording. The W-SCE9 quality review (quality-review-SCE9-2026-11-27.md) had the right brief.
---

Verdict: SCE9 · keep · 0 error, 5 should-fix, 9 minor

## Findings

[should-fix] [case] §3 "What makes the promise wrong" table; Current: "| Cause | Where it starts | Evidence |"; Problem: the column headed Evidence lists "Corvane's known trouble (register)" (row 1) and "Corvane's store staff have no process (register)" (row 3), so the case is shown as evidence for claims about the world; Fix: "| Cause | Where it starts | Evidence; the case's example (fictional, not evidence) |"; Basis: brief preamble ("the case is never evidence for a claim about the world"); sourcing-standard.md Part 8; case-facts.md rules.

[should-fix] [attribution] §13 row O6; Current: "| Availability published to channels and shown by store | Gartner DOM, order visibility to customers [analyst]; Gallino and Moreno 2014 [independent] |"; Problem: Gartner's mandatory feature reads "Order Visibility by tracking order status throughout the supply chain and communicating with other systems and consumers or customers". It covers order status, not availability, so it does not name O6; Fix: "| Availability published to channels and shown by store | Gallino and Moreno 2014, abstract [independent]; Gartner's order visibility covers order status, not availability (this unit's reading) [analyst] |"; Basis: Gartner Peer Insights DOM page, mandatory features (updated July 2025), opened 28 Nov 2026.

[should-fix] [attribution] §13 closing paragraph; Current: "Gartner's three mandatory features cover O5, O10 and O19, and O6 in part"; Problem: the same stretch as the O6 row; Fix: "Gartner's three mandatory features cover O5, O10 and O19"; Basis: as above.

[should-fix] [accuracy] §8; Current: "buyers can cancel before shipment"; Problem: in the FTC guide, the buyer's option to cancel comes with the delay notices the seller must send when it cannot ship on time ("some means for the customer to choose to cancel at your expense"; refund when "the customer exercises any option to cancel before you ship"). The guide states no general right to cancel before shipment; Fix: "a buyer told of a delay can choose to cancel before shipment"; Basis: FTC Business Guide to the Mail, Internet, or Telephone Order Merchandise Rule (Sept 2011, edited Jan 2025), opened 28 Nov 2026.

[should-fix] [coverage] front matter, length; Current: "The unit is long: more than 16,000 words."; Problem: the body through the Self-check is about 9,800 words (lines 11 to 326, viz JSON excluded), against the brief's "2,000–6,000 words". F17 asks only whether the range covers the deliverable; the body alone exceeds it; Fix: "The unit is long: more than 16,000 words; the body through the Self-check is about 9,800, above the brief's 2,000–6,000 (flag F17 asks whether the range covers the deliverable; the body alone exceeds it)."; Basis: word count; brief preamble; flags-all.md F17.

[minor] [accuracy] §4 Acimovic and Graves; Current: "and the partner implemented it across its North American stock-keeping units after a pilot"; Problem: the abstract excerpts read at the publisher say "our industrial partner has implemented the metric as well as a version of the heuristic that it is applying to every fulfillment decision for each of its stock keeping units in North America"; no pilot was seen; Fix: "and the partner has implemented the metric and a version of the heuristic, which it applies to every fulfilment decision for its North American stock-keeping units"; Basis: pubsonline.informs.org/doi/10.1287/msom.2014.0505, abstract excerpts, 28 Nov 2026.

[minor] [accuracy] §10 rule setter; Current: "before a pilot"; Problem: as above; Fix: "before the partner implemented it"; Basis: as above.

[minor] [pointer] §1 GS1 bullet; Current: "(whether EANCOM is a subset of UN/EDIFACT was left unverified by SCE7, and is here)"; Problem: SCE7 calls EANCOM "GS1's EANCOM subset" and left unverified whether IFTSTA is a UN/EDIFACT message, not EANCOM's status; Fix: "(SCE7 left unverified whether IFTSTA is a UN/EDIFACT message; this unit does not verify EANCOM's relation to UN/EDIFACT either)"; Basis: filed SCE7 §6 step 7 and glossary row IFTSTA.

[minor] [label] §14; Current: "lists the same 14 names on its abstract page (read 27 Nov 2026) [analyst]"; Problem: the grade does not say it rests on an abstract page; Fix: "lists the same 14 names on its abstract page (read 27 Nov 2026) [analyst, abstract page only]"; Basis: Part 8; gartner.com/en/documents/8631633, opened 28 Nov 2026.

[minor] [style] Unsure list; Current: "claude-opus-5-5\n\n# Unsure: SCE9"; Problem: the writer agent's model-id line (F82) was pasted into the body at line 589; Fix: "# Unsure: SCE9"; Basis: flags-all.md F82.

[minor] [record] Unsure list, last line; Current: "fix · 1 error, 13 should-fix, 27 minor; report `audits/supply-chain-execution/fresh-check-SCE9.md`"; Problem: the line lacks "all applied", which audit-units §3 requires, and F85's completed quality review is not recorded; Fix: "fix · 1 error, 13 should-fix, 27 minor; all applied; report `audits/supply-chain-execution/fresh-check-SCE9.md`\nQuality review 2026-11-27 (claude-opus-5-5): fix · 1 error, 3 should-fix, 7 minor; all applied or recorded; report `audits/supply-chain-execution/quality-review-SCE9-2026-11-27.md`"; Basis: audit-units-SKILL.md §3; F85.

[minor] [pointer] Deliverable E; Current: "| Phantom stock | Units the record shows and the shelf does not hold | Both | SCE4 §4 |"; Problem: SCE4 §4's term is "phantom inventory"; "phantom stock" is SCE4 §9's wording; Fix: "| Phantom stock | Units the record shows and the shelf does not hold | Both | SCE4 §4 (as \"phantom inventory\") and §9 |"; Basis: filed SCE4 §4 and §9.

[minor] [case] Deliverable A, closing paragraph; Current: "Corvane is deciding whether to buy order and transport systems from the same vendor as its warehouse system (register)."; Problem: the register says "Whether to replace the warehouse system, and whether to buy order and transport systems from the same vendor"; "as its warehouse system" is SCE1's reading, and the replacement half is dropped; Fix: "Corvane is deciding whether to replace its warehouse system and whether to buy order and transport systems from the same vendor (register; SCE1 reads it as one vendor for all three)."; Basis: case-facts.md; Added by units, SCE1 row 6.

[minor] [pointer] §3; Current: "the latest order time that still makes the day's departure; SCE3 §8"; Problem: SCE3 §8 defines an order cut-off as "the latest time an order is accepted for a given dispatch"; Fix: "the latest time an order is accepted for a given dispatch; SCE3 §8"; Basis: filed SCE3 §8.

[minor] [style] Sources; Current: "- Ross, V. Kellogg Insight, Kellogg School of Management."; Problem: the entry is out of alphabetical order, between Ishfaq and O*NET; Fix: "- Kellogg Insight, Kellogg School of Management (writer: Ross, V.)."; Basis: Sources list order.

## Pass 1 · References exist and match

All 22 Sources entries exist. Matches checked on 28 Nov 2026:
- Cui et al., MSOM 26(1) 233–251: match (RePEc and publisher).
- Gallino & Moreno, MS 60(6) 1434–1451: match (RePEc).
- Hoang & Breugelmans, JR 99(1) 26–45: match (IDEAS and repository PDF).
- Hübner et al., Business Research 9, 255–296: match (Springer PDF); issue 2 from the IDEAS identifier only.
- Ishfaq et al., IJPDLM 46(6/7) 543–561: match (Emerald).
- Xu, Allgor & Graves (2005), MIT IMST working paper, Jan 2005: match.
- Acimovic & Graves, MSOM 17(1) 34–51: exists. Volume and pages are from the RePEc identifier in search results; the MIT record and the RePEc page refused the fetch, not checked.
- Gartner MQ and Critical Capabilities pages, 12 Nov 2026, and the Peer Insights DOM page heading: match.
- X12 850 and Example 02: match.
- EANCOM ORDERS: match. ORDRSP: fetch refused, not checked.
- FTC guide: match.
- Directive 2011/83 Arts. 9, 16 and 18 on legislation.gov.uk (the revised text, consolidated 1 Jul 2018; Art. 16 has no version statement): match.
- PE-CONS 37/23, dated 11 Oct 2023: match.
- The Commission page (undated), Kellogg Insight (1 Jul 2013, Valerie Ross) and the three O*NET pages ("Updated 2026"): match.
- Directive 2019/2161 Art. 4: fetch refused, not checked.

## Pass 2 · Claims against sources

PASS:
- Every quoted Gartner definition phrase, the mandatory features, no common features, 71 products and no review total. Order visibility includes communicating with "consumers or customers".
- The MQ abstract's three sentences, no analysts or document ID, and the 14 names in order. The companion's "14 DOM vendors across five use cases" and the same 14 names; the five headings the unit gives are the last five of 18 unlabelled headings, fairly worded as the unit's reading.
- Cui et al.: setting, design, difference-in-differences, findings.
- Acimovic & Graves: 36%, about 1%, no loss of service or rise in holding cost.
- Xu et al. (2005), in full.
- Hübner et al.: every figure, quotation and page checked:
  - Design: 43 managers with eight from e-commerce (p. 268); six-month period (p. 267).
  - Network: p. 274; p. 277; p. 278; p. 279.
  - Store work and pickup: "main cost driver" from a department-store logistics manager (p. 279); real-time store inventory (p. 279); pickup almost 70% and "major growth driver" (p. 282).
  - Returns: 40% to 50% (p. 283); pp. 285–287; quick reimbursement (p. 290).
  - Limitations: p. 291.
  - Definitions: p. 258.
- Ishfaq et al.; Gallino & Moreno's abstract; Kellogg Insight's setting, "total sales rose" and Moreno's suggestion.
- Hoang & Breugelmans: 3,405 households (2,113 and 1,292), UK, the four percentages, the bias caveat.
- X12 850 and Example 02; EANCOM ORDERS, including "split deliveries".
- FTC guide: all points except the stretch reported above.
- EU Arts. 9(1), 9(2)(b), 16(c) to (e) and 18(1) to (3).
- The Commission page's three dates.
- PE-CONS: Art. 11a wording, and Arts. 9 and 18 not amended.
- All O*NET quotes and counts.

## Pass 3 · Grades

The grades follow SCE1 §10:
- Analyst for Gartner, with abstract-only stated except the one minor gap above.
- Practice for O*NET, the FTC and the Commission (public-authority accounts, F18), for the Xu working paper, for Kellogg Insight (F115) and for Hübner's unsourced 40% to 50%.
- Independent for texts of standards and law, for what they say, and for peer-reviewed findings.
- "case" as a form value in deliverable C.
- Abstract-only readings are said. No vendor statement is used.

## Pass 4 · Vendors

PASS:
- Real vendors appear only in the §14 dated list of 14. The list is whole, in the abstract page's order and given alike, with no placements. I confirmed against Gartner's page that it is a real analyst list copied whole, as F1 requires at this pass.
- No real vendor is named elsewhere, and no study retailer is named. No private figures appear. The fictional vendors are labelled and not tied to real ones.

## Pass 5 · The case

All Corvane, Ostrel, Halvern, Varnby and Kestrow facts match case-facts.md, including the units' added rows, and each is labelled fictional on first use. Tandric is not used. Lena and Oskar are now in the register's SCE9 rows, with F106 open. Exceptions: the §3 Evidence column (should-fix) and the decision wording (minor).

## Pass 6 · Scope and tone

- No AI features, no interview framing, no craft method, nothing about the owner. The employer appears only as one entry of the F1-form list.
- Legal points are put as questions to advisers or the national authority. No "not X but Y" constructions. Terms are defined on first use.
- A stray model-id line sits in the Unsure list (minor).

## Pass 7 · Deliverable and figures

**The brief is missing.** /tmp/w10/qr9/brief.txt is SCE10's brief ("Unit SCE10, The seams"), not SCE9's. I could not check the deliverable against SCE9's brief wording, only against the brief as flags F69, F105 and F106 quote it ("an order lifecycle map in the form of SCE7's"; four role cards on Corvane's staff) and as the unit states it.

**Built in full:**
- A: lifecycle map, 12 steps plus row C, SCE7's six columns.
- B: four cards in SCE5's nine fields.
- C: 25 rows in SCE6's six fields.
- D1 to D3: templates whose blanks say what goes in them.
- E: glossary.

"On a site visit" and "Self-check" are present, and all eight answers agree with the body. Q7 depends on Kellogg Insight (F115).

**Figures:**
1. §4, decision tree. Every label traces to the text and the caption gives section and basis. PASS.
2. §8, states. Every label traces to the text and the caption says working description. PASS.
3. §12, matrix. Placements match §12 and the register. PASS.

## Part 8, line by line

All items pass except:
- Source kinds: Kellogg Insight, a school's account of its faculty's study, is not a Part 8 kind (F115 open).
- Grades: the O6 attribution stretch.
- Case: used as evidence in §3.
- Private terms: kit/private_terms.py is not in the packet and was not run; the unit passes by reading.
Every Sources entry appears in sources.md.

## Pointers to filed units

Checked and agreeing:
- SCE1: §1, §5, §7, §8, §10, §11 C4, glossary.
- SCE3: §2, §12, deliverable C rows 1 to 8.
- SCE4: §7, §9, §10, glossary.
- SCE5: deliverable A.
- SCE6: §7, §9, deliverable A, deliverable B rows 17, 21, 22.
- SCE7: §4, §5, §6 steps 6 to 8, §11, deliverable form.
- SCE8: §6.

Not agreeing:
- SCE3 §8, cut-off wording (minor).
- SCE7 on EANCOM and UN/EDIFACT (minor).
- SCE4 §4 term (minor).
- SCE2's "fixed for SCE3, SCE7 and SCE9" is SCE2's error, held in F105.

## Could not verify

- The Acimovic & Graves abstract on three points: the three decisions (ship-from location, method, split), "dual values of a transportation linear program", and "after a pilot". None appeared in the excerpts read; the MIT and RePEc pages refused.
- Directive 2019/2161 Art. 4(8). Fetch refused.
- EANCOM ORDRSP: "of all, or part, or none" and the new order referring to the original. Fetch refused.
- Whether Directive 2024/825 amends Arts. 9 or 18. A EUR-Lex consolidated version dated 27 Sep 2026 was found, but the page came back empty.
- The exact X12 wording "accepted but the quantity has been changed (reduced)" is confirmed in substance only.
- Hübner et al. issue number: from the IDEAS identifier only.

## Flags

**Flags naming SCE9 that the unit was given:**
- Dealt with: F1 (confirmed here), F13 (as far as a unit can), F44 SCE9 part, F54 and F93, F62, F69.
- F85: the review was done, but it is not recorded in the unit (minor finding).
- F17 (every SCE unit): not dealt with; the body exceeds 6,000 words (should-fix).
- F18: followed.
- F82: not dealt with; a stray model-id line remains.

**Raised by SCE9 and still open:** F105 to F112, F114, F115 and F117. These are owner or later-unit decisions; the unit states each where relevant. F113 and F116 affect SCE10 only.

**New for the maintainer:**
- The packet's brief.txt is SCE10's brief. Give the next SCE9 check the right brief, and check that no other step used this one.
- F115 still holds Self-check Q7.
- Run kit/private_terms.py at filing.

**References:** opened and read: 25. Fetch refused, not checked: 5 (Acimovic MIT record and RePEc page, GS1 ORDRSP, Directive 2019/2161 Art. 4, EUR-Lex consolidated 2011/83 returned empty).
