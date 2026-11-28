---
audit: fresh check
unit: SCE10 · The seams
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: claude-opus-5-5
date: 2026-11-28
chat: https://claude.ai/code/session_01KMmgR1zm5V3ijatCgRUBSN
verdict: fix · 1 errors, 5 should-fix, 18 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

claude-opus-5-5
Verdict: SCE10 · fix · 1 error, 5 should-fix, 18 minor

(Writing to /tmp/w10/checker/out/report.md was refused: subagents must return the report as text. The full report follows.)

# Fresh check: SCE10 · The seams

Checker: Opus 5.5, isolated agent context, had not seen the unit written. Live search 28 Nov 2026. Each WebFetch was made only on a URL that a search in this agent returned. Two fetches were refused by the permission check (dblp record for Light et al. 2001; the AIS record for van de Weerd et al. before its search). Both records were then read at other addresses that a search had returned. Neither was retried.

## Pass 1 · References exist and match

Every Sources entry exists, so the row is not stopped.

- Alter (2014), CAIS 34, art. 55, doi 10.17705/1CAIS.03455: PASS against the AIS eLibrary record.
- Bartholdi & Hackman, release 0.98: no search returned the cited gatech PDF address, so it was not fetched. The quotations agree with SCE2 §3.4, SCE3 §7 and SCE6 §5, which quote the same passages. Listed under Could not verify.
- Directive 2011/7/EU, Art. 3, as adopted, legislation.gov.uk: PASS (page last modified 12 Dec 2020).
- Gartner Peer Insights DOM (features updated July 2025): PASS. WMS (features updated May 2026): PASS. SCM Suites (undated, 40 products): PASS. Yard Management at external.pi.gpi.aws.gartner.com (undated, 40 products): PASS. The gartner.com copy of the yard page shows 48 products and "Updated December 2025". The unit cites the other host, so there is no finding.
- GS1 EANCOM 2002 Part I §5: PASS. The page carries the phrase "United Nation's Directories for Electronic Data Interchange for Administration, Commerce and Transport" at its top.
- GS1 reference card (undated), GS1 Logistic Label Guideline release 1.3 (Jul 2019), GDSN page (undated) and GSIN page (undated): PASS.
- Ishfaq, Defee, Gibson & Raja (2016), IJPDLM 46(6/7), 543–561, doi 10.1108/IJPDLM-02-2015-0032: PASS (Emerald).
- Klaus, Rosemann & Gable (2000), ISF 2(2), 141–162, doi 10.1023/A:1026543906354: PASS (IDEAS record).
- Light, Holland, Kelly & Willis (2000), ECIS 2000, 180: PASS (AIS eLibrary: Ben Light, Christopher P. Holland, Sue Kelly, Karl Willis).
- Light, Holland & Willis (2001), BPMJ 7(3), 216–224, doi 10.1108/14637150110392683: PASS (Salford repository record).
- UNTS vol. 1208, No. 19487 (CMR Protocol, 5 July 1978): PASS.
- UN/CEFACT Rec. 20, TRADE/CEFACT/2001/20, 15 Jan 2001: PASS. UN/EDIFACT Standard Directory D.01A, TRADE/CEFACT/2001/33, 14 Feb 2001: PASS.
- van de Weerd, Vollers, Beerepoot & Fantinato (2019), 27th ECIS, Stockholm-Uppsala: PASS (paper header in the Utrecht copy).
- Woolf, "Introduction to Integration Styles": the page exists, footer by Bobby Woolf. It is the introduction to ch. 2, "Integration Styles", of Hohpe & Woolf, *Enterprise Integration Patterns* (Addison-Wesley, 2003), confirmed from the publisher's sample chapter. The Sources entry should cite the book (see Pass 2 and the findings).
- X12 pages 940, 945, 856 and About X12: PASS.

## Pass 2 · Claims against sources

Confirmed (PASS):
- 940: the depositor or another business party advises a warehouse to make a shipment, confirm a shipment, or modify or cancel a previously transmitted shipping order (x12.org/node/4444).
- 945: the warehouse advises the depositor that shipment was made; "It is used to reconcile order quantities with shipment quantities" (x12.org/node/4447).
- 856: "describe the contents and configuration of a shipment in various levels of detail", with order information, products, packaging, marking, carrier and configuration within the equipment (x12.org/node/4398).
- X12 About: ANSI-accredited, consensus-based, non-profit, chartered by ANSI for more than 40 years, more than 320 transaction standards, "Millions of entities around the world" (x12.org/about/about-x12).
- GS1 label guideline: clause [3-1], "The SSCC is the single mandatory element for all logistic labels"; [9-19], the despatch advice/ASN specifies each unit's SSCC and its trade items; [9-36], a scanned SSCC should match the despatch advice.
- GS1 card: the GTIN, GLN, SSCC, GSIN and GINC wordings, verbatim.
- GSIN page: the GSIN is "assigned by a seller and shipper of goods".
- GDSN page: certified data pools, a global registry, and "Everyone has access to the same continuously refreshed data".
- EANCOM Part I §5: "All EANCOM® 2002 messages are based on the UN/EDIFACT directory D.01B"; "GS1 is the agency controlling the subset"; UN/EDIFACT is internationally agreed standards, directories and guidelines, approved and published by UN/CEFACT.
- D.01A: "IFTSTA International multimodal status report message UNSM D4 Transport (SWG)". This resolves unsure item 7.
- Rec. 20: "the greatest possible clarity in the use of units of measure"; a single list of code elements.
- CMR Protocol Art. 2: "Compensation shall not, however, exceed 8.33 units of account per kilogram of gross weight short"; the unit of account is the SDR; came into force 28 December 1980.
- Directive Art. 3(3)(b)(i): 30 calendar days from receipt of the invoice. Art. 3(5): 60 calendar days unless expressly agreed and not grossly unfair.
- Gartner DOM, three quotations verbatim: Enterprise Inventory; Order Orchestration; Order Visibility.
- Gartner WMS: core capabilities to receive, put away, store, count and pick, pack and ship.
- Gartner SCM Suites: "a portfolio of (pre)packaged applications" spanning process clusters, including "logistics and fulfillment".
- Gartner Yard (external.pi): "supports the efficient flow of work, equipment and materials"; planning, direction and control of scheduling; unattributed section; 40 products.
- Klaus et al. abstract: historical analysis, meta-analysis of the IS literature and a survey of academic experts; a broadly agreed definition is unlikely at this stage.
- Ishfaq et al. abstract: 50 interviews of supply chain executives from large retailers; "integrating their store and DC inventories"; stores take a bigger role in fulfilment.
- Alter abstract: the theory can explain compliance and noncompliance with mandates and inform systems analysis and design.
- van de Weerd et al.: 12 team managers, four stores of a Dutch supermarket chain, March to June 2018, a survey of 292, 29 workarounds. W6 shadow administration: 159. W2 another app for the product number: 236. W1 outdated platform: 247. W28 private email for the cargo tracker: 6. Pages 5–6.
- Light et al. 2000: a global entertainment group's record company; over 10,000 SKUs; around eighty countries; two-person interviews over two years plus IT and business plans and annual accounts; around 36 months, comparable with a similarly sized single-vendor ERP implementation; "no one strategy is the 'best' for all contexts"; "the complexity of implementation"; "the likely costs of future ownership"; the vendors' upgrade claim; the vendor-exit risk.
- Light et al. 2001 abstract: compares implementation complexity, functionality, business process alignment and maintenance.
- Woolf page: the four style descriptions; "Each style has its advantages and disadvantages."

FAIL or stretch: Light et al. 2000's 80% figure and its 36 months (see [error] below). The Woolf "he believes" wording and the "simpler model" attribution (minor findings).

## Pass 3 · Grades against SCE1's key

The unit's grades agree with SCE1 §10. Standards and treaty texts are graded independent for what they say. The four Gartner definitions are graded analyst. The authors' summaries in Light et al. are graded practice, and the case finding independent. Abstract-only readings are said to be so (Ishfaq, Klaus, Alter, Light 2001). No vendor statement is graded above vendor-reported; no real vendor statement appears. "case" is not used as a grade. There is one inconsistency: the GDSN page is graded independent, while About X12, the same kind of statement (a standards body describing itself), is graded practice (minor finding).

## Pass 4 · Vendors

No real vendor is named, assessed, ranked, compared, recommended or mapped. Gartner appears only as the analyst. GS1, X12 and UN/CEFACT appear as standards bodies. No vendor list appears, and no private figures. No fictional vendor is tied to a real one. Halvern, Varnby and Kestrow are labelled (fictional), and their slogans are said to be evidence of what they claim.

Claim C9: each side's argument is attributed to a kind of party (advocates, ERP vendors as the authors report them, the authors, textbook authors, analyst), and no vendor is named. Two attribution details are minor findings below: the "simpler model" row, and the analyst row, which is a market definition rather than an argument.

The unit declines to read real vendors' documentation for the brief's "vendors' own documentation describe it" item, and puts that reading to the owner (notes, contradiction 6). The reading is defensible under the Vendors rule; coverage of that item is thin.

## Pass 5 · The case against case-facts.md

Corvane, Tandric, Ostrel, Halvern, Varnby and Kestrow are each labelled (fictional) on first use. Facts checked against the register: 60 stores in four European countries; one website; one centre; systems and portals; known trouble; the decision; Tobias, Lena, Jonas, Olu, Mina, Carla, Oskar, Ravi, Ilse, Sofia, Nuno, Aart, Bram, Luis, Dario, Anke, Karin and Priya; Ostrel's 40 vehicles and paper notes; the Halvern modules. All agree.

The case is never used as evidence. Two labels overstate what the register holds:
- Deliverable A row 12 and §10 present Yard holding W2 as a register fact. SCE6 B row 2 left it open.
- Deliverable B rows 7, 11 and 13 tag readings "(register)".

Notes item 10 already lists the Halvern placements as "placement, not a register fact".

## Pass 6 · Scope and tone

No AI features. No interview framing ("interview" appears only as a research method). No craft method taught. Nothing about the owner or employer. No "not X but Y" construction, no flattery or filler. Legal points are put as questions (§5 directive, CMR claim).

Terms: "best of breed" is used in §12 before any body definition; it is defined only in the glossary (minor). Other terms are defined or were defined in earlier units.

Operations pattern: §10 has no People and no Measure (minor). §5 is by design a list of handoffs.

## Pass 7 · Deliverable and figures

**Deliverable.** A, the system-of-record table for Corvane, has the four brief columns plus the decision column, in full; its counts are correct (16 = 4 + 11 + 1). B, the failure catalogue across the three operations, has the brief's columns plus Operation, in full; its counts are correct (5 + 9 = 14). C1 and C2 are templates whose blanks say what goes in them. D is the glossary. "On a site visit" (7 items) and "Self-check" (7 questions) are present, and every Self-check answer agrees with the body. Answer 7 agrees once the [error] fix below is applied; its wording stands.

**Figure 1, swimlanes, §1: PASS with a minor caption FIX.**
- Every label is traced: the 4 Source row of §1; the 940 in §2; the 945 and 856 in §3; 214 and IFTSTA in §4; "Invoice customer" and "Pay carrier" in §5; "label" in §1 row 7.
- The kind fits a journey across actors.
- The caption names the sections and the sources.
- The 940 note sits on every release, but §2 says the 940 fits only a message between companies (minor finding).

**Figure 2, matrix, §8: FIX.** Row 7's order-system cell "shipped?" disagrees with the §8 table, which reads "Shipped, or delivered if events flow back". The legend's "shipped?" meaning does not fit row 7. The kind fits (items by sections) and the caption is adequate.

**Corrections of filed units** (notes, Contradictions):
- 1 (IFTSTA, SCE7 §6 step 7, §7 table, glossary; SCE8 §5): every "Current" string matches the filed text verbatim, and the replacement is supported by TRADE/CEFACT/2001/33 and EANCOM Part I §5. PASS.
- 2 (CMR cap, SCE7 §6 step 12): current matches; the replacement is supported by the UNTS text. PASS.
- 3 (Directive, SCE7 §6 step 11): current matches; the replacement is supported by Art. 3(3)(b)(i) and 3(5). PASS. The replacement text compresses Art. 3(3)'s conditions (the creditor has fulfilled its obligations and has not been paid), which is acceptable.
- 4 (SCE1 §3 ERP row and glossary): both current strings match SCE1 lines 62 and 267; the replacement is supported by the Klaus abstract. PASS.
- 5 (W2, W22, T7, T8): the current cells match SCE6 §6 and SCE8 §7. It is a decision, not a correction. Moving parcel manifesting out of T8 departs from Gartner's 2026 TMS common feature "parcel carrier selection and manifesting" (SCE8 §1). The unit's §7 table states the two claims, so this is acceptable.
- Missing: deliverable A row 15 and notes item 10 put payment in the ERP. That revises SCE7 §5's register placement ("Freight Audit at steps 10 and 11", step 11 being Pay) and SCE8 deliverable C row 14 ("Freight Audit, by SCE7 §5's placement"). The Contradictions list does not record this (should-fix).

**Word count.** The body through the Self-check is about 6,100 words without the viz JSON, at or just over the brief's 6,000. The deliverable adds about 2,560 (minor; owner flag F17).

## Part 8, line by line

- [x] Claims carrying a number, mechanism or recommendation are sourced where made.
- [x] Source types are acceptable, except Woolf: a practitioner's web page, which should be cited as the book by edition and chapter (should-fix).
- [x] No video, podcast, social post, unsigned blog, comparison site or press rewrite.
- [x] Every graded claim has one grade, per SCE1's key (one minor inconsistency, GDSN).
- [x] Analyst reports say how they were read. Only Peer Insights definitions are used; the MQ for SCM Suites is not used. Abstract-only claims are said to be so.
- [x] No real vendor is assessed, ranked, compared, recommended or mapped.
- [x] Real vendors named only per the rule: none are named.
- [x] Worked product examples use only the fictional vendors, labelled.
- [x] Peer-review sites: no reviews are cited.
- [x] Numbers say whose they are, with sample and year. No private company figures.
- [x] Study findings give sample, setting and design. Cross-setting application is labelled as inference (§11, §12).
- [x] Common claims: C9 is set against its evidence ("No independent source found"). C14 is pointed to SCE13.
- [x] Every Sources entry is in the source log with address, what was read and date.
- [x] Sources entries match the publisher's or index records (Woolf entry: should-fix to cite the book).
- [~] Case facts are labelled and agree with the register, never used as evidence. Labels in A row 12 and B rows 7, 11 and 13 need correcting.
- [x] Nothing about the owner or employer. `kit/private_terms.py` was not run here (not available in this context); a manual scan found nothing.
- [x] No AI, no interview framing, no craft method.
- [x] Search flag on: analyst definitions and filings carry read dates.
- [x] Deliverable built on the case, then as templates with blanks explained.
- [x] On a site visit and Self-check present, and they agree.
- [x] The unit does not read as advice without evidence.
- [x] Links given as links, DOIs for papers.

## Findings

[error] [accuracy] §12, "What the evidence shows"; Current: "It built a best-of-breed system from several vendors' packages, with at least 80% of the functionality from packages, and took about 36 months, which the authors judge comparable to a single-vendor ERP project of similar size;"
- Problem: The 80% is the project's selection rule: a package was used where it "would meet" at least 80% of desired functionality. It is not a measured share of the built system. The 36 months is "to date", in a project still running when the paper was written.
- Fix: "It built a best-of-breed system from several vendors' packages, under a rule agreed with senior managers that a package was used where it would meet at least 80% of the desired functionality, and had taken about 36 months when the paper was written, which the authors judge comparable to a similarly sized single-vendor ERP implementation;"
- Basis: Light, Holland, Kelly & Willis, ECIS 2000, full text, https://salford-repository.worktribe.com/OutputFile/1499857 ("when this was the case, at least 80% of desired functionality would be met by the software"; "The project has actually taken around 36 months to date.").

[should-fix] [attribution] §6, table, row "Item: pack and dimensions"; Current: "A carton too small at the pack station (SCE3 §6); a parcel billed at a size the shipper did not expect (SCE7 §10)"
- Problem: Neither pointer says this. SCE3 §6 does not mention carton size. SCE7 §10 lists "Charges the system did not expect" and nothing about parcel size.
- Fix: "A carton too small at the pack station; a parcel billed at a size the shipper did not expect (this unit's inference; SCE2 §7 lists pack and dimensions in the item master the warehouse system needs)"
- Basis: filed SCE3 §6; SCE7 §10 table; SCE2 §7 ("Item master: identifiers, pack ..., dimensions").

[should-fix] [label] Deliverable A, row 12, last column; Current: "| Warehouse line, Yard module (W2; register) |"
- Problem: The register lists a Yard module but no appointment capability. SCE6 deliverable B row 2 left W2 open ("In Yard or in the core?"), and notes item 10 calls this a placement, not a register fact.
- Fix: "| Warehouse line, Yard module (W2; this unit's placement: the register lists Yard, SCE6 B row 2 left W2 open; notes 10) |"
- Basis: case-facts.md, Halvern Systems; filed SCE6 deliverable B rows 2–3.

[should-fix] [coverage] Deliverable A, row 15, last column; Current: "| Approved charge in the transport line (Freight Audit); payment in the ERP (7; working) |"
- Problem: This revises a filed placement without saying so. The register row added by SCE7 places Freight Audit at steps 10 and 11 (11 = Pay), and SCE8 deliverable C row 14 gives T14 Freight payment to Freight Audit "by SCE7 §5's placement". The notes' Contradictions do not list it.
- Fix: "| Approved charge in the transport line (Freight Audit); payment in the ERP (7; working; revises SCE7 §5's placement of Freight Audit at steps 10 and 11 and SCE8 deliverable C, row 14; notes) |". Add a Contradictions item proposing that SCE7 §5 and SCE8 C row 14 cross-refer to SCE10 §7, and that the register row "SCE7 | Halvern Systems" be marked as revised for step 11.
- Basis: filed SCE7 §5; SCE8 deliverable C row 14; case-facts.md, Added by units, SCE7/Halvern.

[should-fix] [figure] §8, Figure 2 (matrix); Current: `{"label": "7 Delivered", "tone": 2, "cells": ["shipped?", "closed", "delivered"]}], "legend": [{"mark": "shipped?", "means": "only if the warehouse's or carrier's message reached the order system"}, {"mark": "one short", "means": "known to the warehouse system before any other system"}]`
- Problem: The §8 table's moment 7 reads "Shipped, or delivered if events flow back". The figure's "shipped?" and its legend say that the order system shows shipped only if a message arrived, which is the opposite of the table.
- Fix: `{"label": "7 Delivered", "tone": 2, "cells": ["delivered?", "closed", "delivered"]}], "legend": [{"mark": "shipped?", "means": "only if the warehouse's ship confirmation reached the order system"}, {"mark": "delivered?", "means": "only if the carrier's events reached the order system; otherwise still shipped"}, {"mark": "one short", "means": "known to the warehouse system before any other system"}]`
- Basis: unit §8 table, rows 5 and 7.

[should-fix] [attribution] §9, "Four styles"; Current: "([Woolf, \"Introduction to Integration Styles\", Enterprise Integration Patterns site](https://www.enterpriseintegrationpatterns.com/IntegrationStylesIntro.html)) [practice]"
- Problem: A practitioner's web page is not on Part 8's list of sources. The text is the introduction to ch. 2 of a standard text, which should be cited by edition and chapter.
- Fix: "([Hohpe & Woolf, *Enterprise Integration Patterns*, Addison-Wesley, 2003, ch. 2, \"Integration Styles\", introduction by Woolf, read at the authors' site](https://www.enterpriseintegrationpatterns.com/IntegrationStylesIntro.html)) [practice]"
- Basis: publisher's sample chapter, https://ptgmedia.pearsoncmg.com/images/0321200683/samplechapter/hohpech02.pdf (Chapter 2, "Integration Styles"); sourcing-standard Part 8, item 2.

[minor] [attribution] Sources, Woolf entry; Current: "- Woolf, B. Introduction to Integration Styles. Enterprise Integration Patterns (Hohpe & Woolf). https://www.enterpriseintegrationpatterns.com/IntegrationStylesIntro.html"
- Problem: The entry should be the book, by edition and chapter.
- Fix: "- Hohpe, G. & Woolf, B. (2003). *Enterprise Integration Patterns*. Addison-Wesley, ch. 2, \"Integration Styles\"; introduction by Woolf read at https://www.enterpriseintegrationpatterns.com/IntegrationStylesIntro.html"
- Basis: as above.

[minor] [accuracy] §9; Current: "The author writes that each style has advantages and disadvantages, and that he believes messaging is often the best (same page) [practice]."
- Problem: The page says "we believe it is often the best style"; the chapter says "we consider Messaging to be generally the best approach".
- Fix: "The authors write that each style has its advantages and disadvantages, and that they believe messaging is often the best style (same page) [practice]."
- Basis: https://www.enterpriseintegrationpatterns.com/IntegrationStylesIntro.html

[minor] [label] §10, "Who holds the truth"; Current: "at Halvern (fictional) that would be the warehouse line, which lists Yard, as the register places it (this unit's reading)"
- Problem: The register places the Yard module, not the appointment.
- Fix: "at Halvern (fictional) that would be the warehouse line, whose Yard module is in the register; that Yard holds the appointment (W2) is this unit's placement, as SCE6 deliverable B, row 2, left it open"
- Basis: case-facts.md; SCE6 B row 2.

[minor] [coverage] §10; Current: "**How it fails.** A carrier booked for a time the dock cannot serve,"
- Problem: The operations pattern asks for people and a measure; §10 gives neither.
- Fix: "**People and measure.** The warehouse's dock team and the transport planner (working); SCE7 §11's dwell time and detention measure the wait.\n\n**How it fails.** A carrier booked for a time the dock cannot serve,"
- Basis: brief, Operations pattern; filed SCE7 §11 (Dwell time; Detention).

[minor] [attribution] §12, table row 1; Current: "| A single vendor gives a simpler model of IT infrastructure that promises synergies | Advocates of single-vendor ERP, as the authors summarise them |"
- Problem: In the full text read here, the authors state it in their own discussion ("Single vendor ERP systems offer a simpler model of IT infrastructure and one that promises multiple synergies"). This is the fetch tool's reading; confirm against the PDF.
- Fix: "| A single vendor gives a simpler model of IT infrastructure that promises synergies | The authors, stating the case for single-vendor ERP |"
- Basis: Salford full text, https://salford-repository.worktribe.com/OutputFile/1499857

[minor] [attribution] §12, "Gives up with one vendor"; Current: "(the concern that a customer \"may be left waiting for the next upgrade\", Light et al.) [practice]"
- Problem: The concern is voiced by "some managers in our study" about their ERP vendor.
- Fix: "(the concern of some managers in the authors' study that they \"may be left waiting for the next upgrade\" from their ERP vendor, Light et al.) [practice]"
- Basis: as above.

[minor] [label] §6, "Keeping copies the same"; Current: "[independent, for what GS1 says the network does]"
- Problem: A standards body describing its own service. §9 grades X12's statement about itself practice, so this grade is inconsistent with it.
- Fix: "[practice: a standards body's description of its own service, as section 9 grades X12's]"
- Basis: SCE1 §10, question 3; unit §9.

[minor] [style] §12 intro; Current: "Each side's argument, attributed to the kind of party that makes it:"
- Problem: "best of breed" is used in the body before it is defined; it is defined only in the glossary.
- Fix: "**Best of breed** is buying each function from the vendor whose package fits it best and joining the packages (glossary). Each side's argument, attributed to the kind of party that makes it:"
- Basis: brief, Frame ("define each term on first use").

[minor] [attribution] §12, "Gains with one vendor"; Current: "names its own three lines, not the ERP or the carriers (SCE6 deliverable B, row 28)."
- Problem: SCE6 B row 28 names only the ERP. The carriers point is SCE8 C row 18.
- Fix: "names its own three lines, not the ERP (SCE6 deliverable B, row 28) or the carriers (SCE8 deliverable C, row 18)."
- Basis: filed SCE6 B row 28; SCE8 C row 18.

[minor] [label] Deliverable B, row 7; Current: "| Ilse, at staging (register) | Sofia re-plans; Ilse moves cages (register, SCE5) |"
- Problem: Notes item 7 calls this a reading of SCE5's rows. The register does not say Ilse sees it at staging or moves cages.
- Fix: "| Ilse, at staging (reading of SCE5's register rows; notes 7) | Sofia re-plans (register, SCE5); Ilse moves cages (reading; notes 7) |"
- Basis: case-facts.md, SCE5 rows on Sofia.

[minor] [label] Deliverable B, row 11; Current: "| Anke's site records it; Karin settles the dispute (register) |"
- Problem: The register has Karin sign client contracts and sponsor purchases, not settle invoice disputes.
- Fix: "| Anke's site records it; Karin settles the dispute (working: the register has her sign client contracts) |"
- Basis: case-facts.md, Tandric people.

[minor] [label] Deliverable B, row 13; Current: "| The carrier; Priya chases it (register) |"
- Problem: Not in the register; notes item 9 marks it working.
- Fix: "| The carrier; Priya chases it (working; notes 9) |"
- Basis: case-facts.md; notes item 9.

[minor] [accuracy] §2, "What the software does"; Current: "Both definitions name allocation or inventory, so the seam is"
- Problem: The WMS definition names storing and counting, not "allocation" or "inventory".
- Fix: "The DOM definition names inventory and allocation, and the WMS definition names storing and counting, so the seam is"
- Basis: Gartner Peer Insights WMS page (core capabilities "receive, put away, store, count and pick, pack and ship").

[minor] [attribution] §12, table, analyst row; Current: "| A supply chain management suite is \"a portfolio of (pre)packaged applications\" spanning several process clusters, logistics and fulfilment among them | Analyst |"
- Problem: A market definition, not an argument for either side.
- Fix: "| (A definition, not an argument) A supply chain management suite is \"a portfolio of (pre)packaged applications\" spanning several process clusters, logistics and fulfilment among them | Analyst, defining the market |"
- Basis: Gartner Peer Insights SCM Suites page.

[minor] [label] §9, message table; Current: "| Warehouse to transport and receiver | 856 Ship Notice/Manifest; 945 Warehouse Shipping Advice | Despatch advice (GS1 label guideline) | SSCC, GSIN |"
- Problem: The column is headed UN/EDIFACT or EANCOM. The label guideline names the business message "Despatch Advice / ASN", not an EANCOM message, and no EANCOM message page was opened.
- Fix: "| Warehouse to transport and receiver | 856 Ship Notice/Manifest; 945 Warehouse Shipping Advice | Despatch advice, as GS1's label guideline names it; its EANCOM message not opened here | SSCC, GSIN |"
- Basis: GS1 Logistic Label Guideline r1.3, clause [9-19].

[minor] [figure] §1, Figure 1 caption; Current: "messages from X12's pages for 940, 945 and 856 (read 28 November 2026),"
- Problem: The 940 note sits on every release, but §2 says the 940 is a message between companies; inside one company the facts cross an internal interface.
- Fix: "messages from X12's pages for 940, 945 and 856 (read 28 November 2026; the 940 and 945 between companies, such as a logistics provider and its clients, section 2),"
- Basis: unit §2.

[minor] [coverage] §7, "What the vendors' documentation says"; Current: "**What the vendors' documentation says.** This unit opened none."
- Problem: The brief item "as ... the vendors' own documentation describe it" is covered thinly, by choice (notes, contradiction 6).
- Fix: none in the unit. The owner decides notes contradiction 6.
- Basis: brief; Vendors rule.

[minor] [style] Whole body; Current: (length) the body through the Self-check is about 6,100 words.
- Problem: At or just over the brief's 2,000–6,000. Filed units set the precedent.
- Fix: none required; record under flag F17.
- Basis: brief.

## Confirmed

Every PASS line under Pass 2, each with its source URL as cited in the unit, plus:
- §1's join of SCE9 rows 5–8 to SCE3 C rows 1–8 and rows 8–10 to SCE7 §6 steps 6–8 (filed SCE9 opening and deliverable A).
- SCE7 §6 step names and steps 9–12; SCE7 §9 (dock, FMCSA); SCE7 §11 on-time pickup; SCE7 deliverable A rows 5, 9–11; deliverable B rows 5–8 and 10.
- SCE8 §1 glossary "manage freight bills and payments"; SCE8 §5's 214 and 210; T7 and T8; deliverable C rows 7 and 8.
- SCE6 W2, W9, W14 and W22 sources; SCE6 §5 carrier connection; SCE6 B rows 14 and 22.
- SCE3 §2, §7 and §12 measures; SCE3 C rows 1–8.
- SCE4 §4 phantom stock and §9 chain; SCE4 §2 rotation.
- SCE9 §3 promise accuracy, §8 cancellation failure, §9 return authorisation, §10 "where is my order"; deliverable A rows 2, 9, 11 and 12.
- SCE1 §3 ERP row and §10 grade key; C9 and C14 rows.

## Could not verify

- Bartholdi & Hackman release 0.98, ch. 4, pp. 33–36 (the quotations in §3, §5, §7 and §12): no search returned the cited address, so it was not fetched. They agree with filed SCE2, SCE3 and SCE6.
- Directive 2011/7/EU: whether later acts amended Art. 3 (unsure item 6). Not checked.
- The CMR Protocol's list of states party. Not checked.
- The GINC page (gs1.org/ginc): not opened. The GINC wording on the reference card was verified.
- Light et al. 2000: whether the "simpler model" sentence is the authors' own view or their summary of advocates. The repository copy was read through the fetch tool only.
- Gartner's TMS market page, ERP glossary, and 2026 SCM Suites MQ and Critical Capabilities. The unit states nothing from them and relies on SCE7 and SCE8 for TMS content; not re-checked.
- Unsure item 9 (§7's dock and parcel rows taken from SCE6 §6 and SCE8 §7): the cross-references match the filed units. The underlying B&H §4.3 and the Gartner 2022 WMS and 2026 TMS reports were not opened here.
- `kit/private_terms.py`: not run (not available in this context).

SCE10 · fix · 1 error, 5 should-fix, 18 minor
