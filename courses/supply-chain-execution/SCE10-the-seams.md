---
code: SCE10
title: The seams
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-28
search: off
intro: The handoffs between the order, warehouse and transport systems and the ERP, one by one: order to warehouse at release, warehouse to transport at ship confirmation and loading, transport to the customer as status, and each back to finance; the data all of them share (items, locations, customers, carriers, units of measure) and GS1's keys for them; which system holds the truth for which fact, as the textbook, the analyst definitions and the case register's fictional vendors put it, and where they disagree (stock, the dock appointment, parcel labels, carrier payment, returns); one Corvane (fictional) web order seen in three systems with three statuses; integration styles and the X12 and UN/EDIFACT messages at each seam; the yard and the dock; what users do around a broken seam, as far as one retail study goes; and common claim C9, one vendor against specialists, each side attributed to the kind of party that makes it. Deliverable: Corvane's system-of-record table, a handoff failure catalogue across the three case operations, both templates, glossary lines; two figures (the swimlanes of section 1, the matrix of section 8). How it was made: written 28 Nov 2026 by Opus 5.5 with live search (the build order lists SCE10 search off); fresh check by a fresh Opus 5.5 agent (fix: 1 error, 5 should-fix, 18 minor), 21 of 22 findings applied, the one held superseded by an extra fix, plus 6 extra fixes; quality review by a fresh Opus 5.5 agent (fix: 0 error, 8 should-fix, 14 minor), 17 applied and 5 handled outside the unit text. Known gaps: not opened: Gartner's TMS market page, its ERP glossary entry and its 2026 Magic Quadrant for Supply Chain Management Suites (each refused or failed), GS1's GINC page (refused), the TMS chapter of Novack, Gibson and Suzuki (10th ed., 2024; contents page only), and Annex III of the Commission's 2027 work programme; not re-opened here: Bartholdi and Hackman §4.3 and Gartner's 2022 WMS and 2026 TMS reports (section 7 takes them as SCE6 and SCE8 read them) and the UN/EDIFACT D.01B directory. Read in abstract only: Klaus, Rosemann and Gable (2000, at IDEAS), Light, Holland and Willis (2001, at the Salford repository's record), Ishfaq et al. (2016) and Alter (2014); Light et al. (2000) and van de Weerd et al. (2019) were read in repository copies. C9 was tested on one ERP case study (Light et al. 2000); no independent source on total cost by sourcing strategy for execution software was found, and SCE16 prices it. No real vendor's documentation was read: the brief's item on the vendors' own documentation is answered with the fictional vendors and a template, and put to the owner. Status names in section 8 are working terms; the one workaround study is set in supermarket stores. Length: the body through the Self-check is about 6,300 words, above the brief's 2,000–6,000 (F17); the deliverable adds about 2,600.
---

# SCE10 · The seams

SCE3, SCE7 and SCE9 each followed one system's part of an order. This unit follows the joins. Grades follow SCE1's key (section 10 there): every claim that carries a number, a mechanism or a recommendation ends with [independent], [analyst], [vendor-reported] or [practice]; the text of a standard, treaty or regulation is graded independent for what it says. Lines marked as this unit's inference or reading, or as working descriptions, carry no grade. Every reference was opened on 28 November 2026 unless a line says otherwise; the source log gives what was read at each.

A **seam** (course term) is a point where one system hands a fact to another and stops being the place that changes it. A **handoff** is the message, file or call that carries the fact across. Each section below takes one seam as the operations pattern asks: the physical event, the people, what the software does, how it commonly fails and the measure, where a source or the case gives one.

## 1. Where the three lifecycles join

SCE9 numbered an order's life in twelve steps, SCE3 the warehouse's outbound in eight, SCE7 a shipment's in twelve. They overlap at two places, and SCE9 named both (its opening, and deliverable A): for an order the distribution centre fills, SCE9's rows 5 to 8 are SCE3 deliverable C's rows 1 to 8, and SCE9's rows 8 to 10 are SCE7 §6's steps 6 to 8. The join, row by row, is this course's own; no source opened sets the three side by side.

| Order (SCE9) | Warehouse (SCE3 C) | Transport (SCE7 §6) | The seam |
|---|---|---|---|
| 4 Source | | | Order system chooses the centre |
| 5 Release to the location | 1 Release | | **Order to warehouse** (section 2) |
| 6 Pick | 2 Pick; 3 Replenish forward; 4 Sort and consolidate | | Inside the warehouse; a short pick goes back to the order system |
| 7 Pack and label | 5 Check and pack; 6 Label | (1 Plan, 2 Rate, 3 Tender, 4 Accept or refuse, 5 Book a dock, done ahead) | Carrier label and service come from transport |
| 8 Hand over | 7 Stage and load; 8 Ship | 6 Pick up | **Warehouse to transport** (section 3) |
| 9 Track and inform | | 7 Track | **Transport to the customer** (section 4) |
| 10 Deliver | | 8 Deliver and prove delivery | Proof of delivery back to the order |
| 11 Return; 12 Refund | (returns: SCE4 §7) | 9 to 12 Invoice, check, pay, claim | **Back to the ERP and finance** (section 5) |

SCE7's steps 1 to 5 happen while the goods are still on the shelf. For a parcel booked in a carrier's own portal, as Corvane (fictional; a fashion retailer with 60 stores, one website and one distribution centre) books its carriers (case register), steps 2 to 4 shrink to choosing a service and printing a label (this unit's reading; SCE3 deliverable C, row 6).

```viz
{"kind": "swimlanes", "lanes": [{"id": "oms", "label": "Order system", "tone": 3}, {"id": "wms", "label": "Warehouse system", "tone": 2}, {"id": "tms", "label": "Transport system or carrier", "tone": 4}, {"id": "erp", "label": "ERP", "tone": 1}], "steps": [{"id": "src", "lane": "oms", "col": 0, "label": "4 Source"}, {"id": "rel", "lane": "wms", "col": 1, "label": "Release", "note": "X12 940"}, {"id": "pack", "lane": "wms", "col": 2, "label": "Pick, pack, label"}, {"id": "plan", "lane": "tms", "col": 2, "label": "Plan, book carrier"}, {"id": "ship", "lane": "wms", "col": 3, "label": "Ship confirm", "note": "X12 945, 856"}, {"id": "pick", "lane": "tms", "col": 4, "label": "Pick up, track", "note": "214, IFTSTA"}, {"id": "stat", "lane": "oms", "col": 5, "label": "Status to customer"}, {"id": "inv", "lane": "erp", "col": 4, "label": "Invoice customer"}, {"id": "pay", "lane": "erp", "col": 6, "label": "Pay carrier"}], "links": [{"from": "src", "to": "rel", "label": "order"}, {"from": "rel", "to": "pack"}, {"from": "plan", "to": "pack", "label": "label"}, {"from": "pack", "to": "ship"}, {"from": "ship", "to": "pick", "label": "shipment"}, {"from": "ship", "to": "inv", "label": "shipped"}, {"from": "pick", "to": "stat", "label": "events"}, {"from": "pick", "to": "pay", "label": "freight bill"}], "caption": "The four seams of sections 1 to 5 of this unit, by the system that acts. Step names are this course's (SCE3 deliverable C, SCE7 section 6, SCE9 deliverable A); messages from X12's pages for 940, 945 and 856 (read 28 November 2026; the 940 and 945 between companies, such as a logistics provider and its clients, section 2), SCE8 section 5 for 214, and UN/CEFACT's D.01A directory for IFTSTA (section 4); the shipment-to-invoice link from Bartholdi and Hackman, release 0.98, section 4.1; payment in the ERP is SCE1's working placement."}
```

## 2. Order to warehouse: release and allocation

**The physical event.** None yet: a promise turns into work.

**What crosses.** The order lines (item, quantity), the ship-to address, the carrier or service, the date the goods must leave; back across, whether the lines were allocated, picked short or cancelled. X12, a standards body chartered by the American National Standards Institute ([X12, "About X12"](https://x12.org/about/about-x12)), publishes the **940 Warehouse Shipping Order**, which a depositor (the owner of goods held in a warehouse) or another business party uses to tell a warehouse to make a shipment, to confirm one, or to change or cancel a shipping order sent earlier ([X12, 940](https://x12.org/node/4444)) [independent, for what the standard says]. The 940 is a message between companies: it fits Tandric Logistics (fictional; a logistics provider running one warehouse for nine clients, case register), whose clients are depositors; inside one company the same facts cross an internal interface (this unit's reading).

**People.** At Corvane, Tobias, the outbound shift supervisor, answers for release (case register); Lena runs the online orders' exception queue (register, added by SCE9).

**What the software does.** The order system chooses the location and sends the order; the warehouse system turns it into pick lists by wave or continuously (SCE3 §2) and reports what it could not fill. Gartner's market definition of distributed order management lists as mandatory "Enterprise Inventory for available-to-promise and available-to-ship items in the supply chain" and order orchestration "that optimizes order routing and inventory allocation" ([Gartner Peer Insights, Distributed Order Management (DOM) Systems, features updated July 2025](https://external.pi.gpi.aws.gartner.com/reviews/market/distributed-order-management-systems)) [analyst]. Gartner's WMS definition gives the warehouse system the core capabilities to receive, put away, store, count, pick, pack and ship ([Gartner Peer Insights, Warehouse Management Systems, features updated May 2026](https://external.pi.gpi.aws.gartner.com/reviews/market/warehouse-management-systems)) [analyst]. The DOM definition names inventory and allocation, and the WMS definition names storing and counting, so the seam is a place where two systems each hold a view of the same stock (this unit's reading).

Stores add a second source of stock to the same seam: in a study combining 50 interviews with supply chain executives at large retailers with secondary data on firm size, store and distribution networks and online sales, Ishfaq, Defee, Gibson and Raja found retailers integrating store and distribution centre inventories as stores take a larger part in online fulfilment ([Ishfaq et al., 2016, abstract](https://doi.org/10.1108/IJPDLM-02-2015-0032)) [independent, abstract only].

**How it commonly fails.** The order system promises from a stock figure the warehouse cannot pick: Corvane's known trouble is web orders promised from stock the centre cannot find (case register), and SCE4 §9 traced the chain. A cancellation reaches the order system and not the work already released, so the parcel ships and comes back (SCE9 §8). A short pick is reported in the warehouse and not passed back, so the order shows lines that will never ship (this unit's inference from SCE4 §9).

**The measure.** No source opened measures release failures between systems. SCE3 §12's Internal Order Cycle Time and SCE9 §3's promise accuracy bracket the seam from each side.

## 3. Warehouse to transport: ship confirmation and loading

**The physical event.** Packed units are staged, scanned onto a vehicle and leave; the driver signs (SCE3 §7; SCE7 §6, step 6). The handoff runs to a clock. The order cut-off is the latest time an order is accepted for a given dispatch, and the carrier departure is the time the vehicle leaves (SCE3 §8, working definitions). An order that misses the cut-off waits for the next departure (SCE3 §8; SCE7 §10, step 6).

**What crosses.** Which units left, on which vehicle, with which carrier, at what time, and what each unit holds. Three standard messages carry it:

- X12's **856 Ship Notice/Manifest** lets the sender "describe the contents and configuration of a shipment in various levels of detail": order information, products, packaging, marking, carrier and how goods sit in the equipment ([X12, 856](https://x12.org/node/4398)) [independent, for what the standard says].
- X12's **945 Warehouse Shipping Advice** is the warehouse's reply to the 940, telling the depositor that a shipment was made; "It is used to reconcile order quantities with shipment quantities" ([X12, 945](https://x12.org/node/4447)) [independent].
- GS1's logistic label puts the **SSCC** (Serial Shipping Container Code) on every logistic unit; "The SSCC is the single mandatory element for all logistic labels", the despatch advice (advance ship notice, ASN) should give each unit's SSCC and the trade items in it, and a scanned SSCC should match the information in that message ([GS1, Logistic Label Guideline, release 1.3, July 2019](https://gs1.org/standards/gs1-logistic-label-guideline)) [independent].

The SSCC ties the label to the message (this unit's reading of GS1's guideline).

**People.** Loaders and the outbound supervisor; the carrier's driver; at the receiving end, whoever scans the units in (SCE2 §3.4).

**What the software does.** The warehouse records the shipment out, one of the records that Bartholdi and Hackman call a WMS's most basic: "shipping drives the sending of invoices downstream to the consignee" ([Bartholdi & Hackman, *Warehouse & Distribution Science*, release 0.98, 2017, §4.1, p. 34](https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf)) [practice]. The transport system, where there is one, records the shipment picked up (SCE7 §6, step 6, a working description).

**How it commonly fails.** A unit on the wrong vehicle (SCE3 §7). A label re-keyed from a carrier's portal, so the label and the warehouse's record differ: Corvane has no transport system and books every carrier in that carrier's portal (case register; SCE3 deliverable C, row 6, reads the re-keying). A notice sent with SSCCs that do not match the labels, so the receiver cannot match units to the message and counts by hand (this unit's inference from GS1's matching rule). The 945's stated purpose, reconciling ordered against shipped quantities, names one fact that can be in dispute at this seam (this unit's reading).

**The measure.** SCE3 §12's On Time Shipments and Correct Documentation sit on the warehouse side; SCE7 §11's on-time pickup on the transport side.

## 4. Transport to the customer: status

**The physical event.** The goods are in transit.

**What crosses.** Status events (picked up, in transit, delayed, delivered) from the carrier to the shipper's systems and on to the customer. X12's 214 carries carrier status in X12 (SCE8 §5). **IFTSTA**, the International multimodal status report message, is a United Nations Standard Message of UN/EDIFACT: the UN/CEFACT documentation for directory D.01A lists it with status "UNSM" from the transport sub-group ([UN/CEFACT, UN/EDIFACT Standard Directory D.01A, TRADE/CEFACT/2001/33, 14 Feb 2001](https://digitallibrary.un.org/record/433163/files/%5EE_ECE_%5ETRADE_CEFACT_2001_33-EN.pdf)) [independent]. GS1's EANCOM, the subset SCE7 §6 cited for IFTSTA, is a subset of UN/EDIFACT: "All EANCOM® 2002 messages are based on the UN/EDIFACT directory D.01B", and GS1 is the agency controlling the subset ([GS1, EANCOM 2002, Part I, §5](https://gs1.org/sites/gs1/files/docs/eancom/ean02s3/part1/part1_05.htm)) [independent]. This settles what SCE7 left unverified (flag F68; notes).

**People.** At Corvane, Jonas answers customers about shipments in transit (register); at Tandric, Olu answers clients' tracking questions (register, added by SCE7).

**What the software does.** The order system shows the customer the order's status; Gartner lists "Order Visibility by tracking order status throughout the supply chain" among DOM's mandatory features (DOM page) [analyst]. The status the customer reads is therefore a copy of the carrier's events, held in the order system (this unit's reading).

**How it commonly fails.** No event, or a late one, so the customer is told nothing (SCE7 §10). The customer asks before the company knows (SCE9 deliverable A, row 9). At Corvane, status lives in each carrier's portal (register), so Jonas reads it there, not in the order system (this unit's reading of the register).

**The measure.** SCE9 §10's "where is my order" contacts, a working measure; no source opened measures status latency.

## 5. Back to the ERP and finance

Every seam above has a fourth party: the system that keeps the money. Bartholdi and Hackman: "receipt drives the paying of bills to suppliers upstream" and shipping drives the invoices to the consignee (§4.1, p. 34) [practice]; the WMS may pass summary data to a larger supply chain system (ch. 4 introduction, p. 33) [practice]. Four handoffs follow, as this unit's reading of the filed units:

- **Shipment to customer invoice.** The ship confirmation of section 3 tells the ERP to bill (Bartholdi and Hackman §4.1) [practice]. If quantities shipped differ from quantities ordered and only one system knows, the invoice is wrong (this unit's inference from the 945's stated purpose).
- **Carrier invoice to payment.** The carrier's bill is checked against the agreed charge and paid (SCE7 §6, steps 9 to 11). For the European Union, the late-payment directive requires Member States to ensure that, where the contract fixes no date, a creditor is entitled to interest for late payment after 30 calendar days from the debtor's receipt of the invoice, and that a contractual period between businesses does not exceed 60 calendar days unless expressly agreed and not grossly unfair to the creditor (Directive 2011/7/EU, Art. 3(3)(b)(i) and 3(5), as adopted, [legislation.gov.uk copy](https://www.legislation.gov.uk/eudr/2011/7/article/3/adopted)) [independent, for what the text says]; this copy is the text as adopted in 2011. No act amending Article 3 was found by search on 28 November 2026, and the regulation the Commission proposed in 2023 to replace the directive (COM(2023) 533) had not been adopted: EUR-Lex lists the procedure as ongoing ([EUR-Lex, procedure 2023/0323/COD](https://eur-lex.europa.eu/procedure/EN/2023_323), read 28 November 2026) [practice: the EU's procedure record, not a legal text]. The Commission's 2027 work programme, adopted 4 November 2026, has an Annex III of pending proposals it intends to withdraw within six months ([European Commission, 2027 Commission work programme](https://commission.europa.eu/strategy-and-policy/strategy-documents/commission-work-programme/commission-work-programme-2027_en?prefLang=bg), read 28 November 2026) [practice]. The annex was not opened, so whether this proposal is on it is not stated. No consolidated EU text was opened, so a later amendment is not ruled out. SCE7 §6 gives the US rule. Whether either applies to a given carrier contract is a question for the finance team and its legal advisers. No independent study of freight invoice error rates was found (search of 28 Nov 2026 returned vendors' blogs and trade press only).
- **Loss and damage to a claim.** Under the CMR as amended by its Protocol of 5 July 1978, compensation "shall not, however, exceed 8.33 units of account per kilogram of gross weight short", the unit of account being the Special Drawing Right; the Protocol entered into force on 28 December 1980 ([UN Treaty Series vol. 1208, No. 19487](https://treaties.un.org/doc/Publication/UNTS/Volume%201208/volume-1208-I-19487-English.pdf)) [independent]. It applies between the states party to the Protocol, which this unit did not check; SCE7 §6 gave only the 1956 text's gold-franc cap (flag F66). Whether a claim lies is a question for the claims handler and counsel.
- **Return to refund.** SCE9 left open which system triggers the refund (its deliverable A, row 12); this unit leaves it open too, as no source opened places it.

**Who holds the money record.** SCE1 kept the ERP's scope a working definition because no definition could be opened (flag F7). Gartner's ERP glossary page refused the fetch again on 28 November 2026. The research gives a reason why a single definition is hard to cite: Klaus, Rosemann and Gable, from a historical analysis, a meta-analysis of the information systems literature and a survey of academic experts, conclude that a broadly agreed definition of ERP is unlikely at that stage ([Klaus, Rosemann & Gable, 2000, *Information Systems Frontiers* 2(2), 141–162, abstract read at a bibliographic index](https://ideas.repec.org/a/spr/infosf/v2y2000i2d10.1023_a1026543906354.html)) [independent, abstract only]. The course keeps its working line, the company's financial and master-data system, now with that finding beside it (notes).

## 6. The data every system shares

Five kinds of fact are held in every system at once: items, locations, customers, carriers and units of measure. When two copies differ, the error shows later, where someone acts on the wrong copy (this unit's inference).

**The identifiers.** GS1 publishes the keys most often used for them. On GS1's reference card: the **GTIN** (Global Trade Item Number) identifies products "at any packaging level"; the **GLN** (Global Location Number) identifies physical locations such as Ship From, Ship To and Read Point; the **SSCC** identifies logistic units such as unit loads on pallets or roll cages, and parcels; the **GSIN** (Global Shipment Identification Number) identifies a shipment of one or more logistic units intended to be delivered together; the **GINC** (Global Identification Number for Consignment) identifies a consignment of one or more logistic units, potentially of different shipments ([GS1, "GS1 Identification Keys at Your Finger Tips", undated](https://www.gs1.org/sites/default/files/docs/idkeys/gs1_id_keys_reference_card.pdf.pdf)) [independent]. GS1's GSIN page adds that a seller and shipper of goods assigns the GSIN ([GS1, GSIN](https://www.gs1.org/gsin)) [independent]. GS1's GINC page refused the fetch.

**Keeping copies the same.** GS1's Global Data Synchronisation Network (GDSN) exists so that trading partners hold the same product data: trading partners join certified data pools linked to a global registry, and "Everyone has access to the same continuously refreshed data" ([GS1, "GS1's GDSN Keeps Trading Partners' Product Data in Sync", undated](https://www.gs1.org/how-gdsn-works)) [practice: a standards body's description of its own service, as section 9 grades X12's]. No figure for how often copies differ was opened.

**Units of measure.** UN/CEFACT's Recommendation No. 20 sets one list of codes for units of measure because trade needs "the greatest possible clarity in the use of units of measure" ([UN/CEFACT, Recommendation No. 20, TRADE/CEFACT/2001/20, 15 Jan 2001](https://digitallibrary.un.org/record/431844/files/%5BE_ECE_%5DTRADE_CEFACT_2001_20-EN.pdf)) [independent]. The codes themselves sit in annexes this unit did not read.

What goes wrong when each differs, as this unit's inference from SCE2 to SCE9 (no source opened measures any of them):

| Shared fact | Typical owner | Copies | When the copies differ |
|---|---|---|---|
| Item: identifier, description | ERP (working) | Order system, warehouse system, carrier portals | An item sold on the web that the warehouse cannot find by its number; a GTIN on the box the warehouse does not know |
| Item: pack and dimensions | ERP or warehouse system | Transport system, carrier portals | A carton too small at the pack station; a parcel billed at a size the shipper did not expect (this unit's inference; SCE2 §7 lists pack and dimensions in the item master the warehouse system needs) |
| Unit of measure | ERP | Every system | An order for 12 read as 12 cases, or 12 cases picked as 12 units (SCE2 §2's pallet, case and each) |
| Location and address | ERP or order system | Warehouse, transport, carrier | Goods addressed to a store's old address; a dock door that differs between the yard plan and the warehouse |
| Customer | ERP or order system | Order system, transport, carrier | A delivery window or a refusal rule known to the dispatcher and not to the planner |
| Carrier and service | Transport system or ERP | Warehouse system, carrier portals | A label printed for a service the carrier does not run on that lane |

## 7. Which system holds the truth, and where the sources disagree

SCE1 §3 drew the map-level answer; SCE6, SCE8 and SCE9 each asked this unit a question about a line on the boundary. The sources opened here give partial answers, and they do not all agree.

**What the textbook says.** Bartholdi and Hackman give the warehouse system the item-by-item record and a summary upward to a larger supply chain system (ch. 4 introduction, p. 33) [practice]; a WMS "may even talk to other specialized software such as Yard Management Systems (YMS)" (p. 33) [practice]; and on who sells which: warehouse systems are "extending their functionality out along the supply chain" and increasingly compete with enterprise systems; "WMS's have an advantage in that they are already connected to financial systems", while "The enterprise systems have advantages where they can grow out of a manufacturing enterprise" (§4.5, p. 36) [practice].

**What the analysts say.** Gartner's DOM definition gives the order system enterprise inventory for available-to-promise and order status across the supply chain (DOM page, July 2025) [analyst]; its WMS definition gives the warehouse system receive, put away, store, count, pick, pack and ship (WMS page, May 2026) [analyst]. The two claim the same stock, at different grain: the order system across locations, the warehouse system within one (this unit's reading).

**What the vendors' documentation says.** This unit opened none. Saying what a real vendor's documentation makes the system of record for each fact would map that vendor's product line, which the course does not do (brief, Vendors). The case register's fictional vendors stand in: Varnby Software (fictional) sells warehouse and transport as modules of its ERP and says "No integration to build"; Halvern Systems (fictional) sells order, warehouse and transport systems and says "One vendor for execution"; Kestrow (fictional) sells one warehouse system and says "Live in weeks" (case register). Each line is evidence of what a vendor claims. To read a real vendor's own placement, open its integration or data-model documentation and fill deliverable C's template from it, dated and graded vendor-reported.

**Where they disagree, line by line.** Five facts are claimed by two systems in the sources or the filed units:

| Fact | Claimed by | Source | This course's placement |
|---|---|---|---|
| Stock available to sell | Order system (enterprise inventory) and warehouse system (stock locator) | Gartner DOM [analyst]; Gartner WMS [analyst]; SCE6 W9 | Warehouse system owns stock at a location; the order system owns the sellable figure it computes from those records (course's) |
| Dock appointment | Warehouse capability list W2 and transport list T7 | Bartholdi and Hackman, basic feature, as SCE6 §6 reads it [practice]; Gartner 2022 WMS, "dock scheduling" (SCE6) [analyst]; Gartner 2026 TMS, common feature (SCE8) [analyst] | W2 holds appointments at the operation's own doors; T7 holds the request for one at another party's dock (course's; flag F98) |
| Parcel label and manifest | W22 and T8 | B&H high-end and advanced features (SCE6 §6) [practice]; Gartner 2026 TMS, common (SCE8) [analyst] | W22 holds the label and manifest printed at the pack station; T8 holds the choice of parcel carrier and service (course's; flag F98) |
| Carrier payment | Transport system and ERP | Gartner's TMS glossary, "manage freight bills and payments" (SCE8 §1) [analyst]; SCE1's working placement in the ERP | The transport system owns the approved charge; the ERP owns the payment (course's, a working placement) |
| Returns | Order system (authorisation) and warehouse system (receipt and grade) | Halvern Order lists Returns (register); B&H high-end "Returns" (SCE6 W14) [practice] | Order system owns the authorisation; the warehouse system owns receipt, grade and stock; which system triggers the refund is open (section 5) (course's) |

The rule behind the course's placements, which no source opened states: the system that records the physical event owns the fact of the event; the system that decides from it owns the decision. Where a source places a capability in two lists, each list keeps the half that matches that rule, and the other cross-refers (notes, F98). The rule is this course's, offered as a working rule; it decides nothing about how any real product is built.

## 8. One order in three systems: Corvane (fictional)

SCE9's deliverable A followed a Corvane web order shipped from a store. Here the centre fills it, so the join of section 1 applies. Assumed for this worked example, and listed in the notes: a two-item web order to a home address, both items held by the centre; one item is short at the pick face; the parcel carrier collects at the centre, booked in its own portal (case register: carriers are booked in each carrier's portal). The status words are this unit's working terms; no source opened gives standard status names for any of the three systems.

| Moment | Order system | Warehouse system | Carrier portal | What Jonas sees if the customer calls |
|---|---|---|---|---|
| 1 Order accepted, centre chosen (SCE9 rows 1 to 4) | Sourced to centre | Nothing yet | Nothing | Order placed |
| 2 Released (SCE3 C row 1) | Released | Released, two lines | Nothing | Being prepared |
| 3 Short pick (SCE3 C row 2) | Released, two lines | One line picked, one short | Nothing | Being prepared; the order system does not yet know |
| 4 Packed, label printed (SCE3 C rows 5, 6) | Released (or partly shipped, if the short was passed back) | Packed, one unit | Label created | Two answers: the portal says a label exists, the order system says nothing has shipped |
| 5 Collected (SCE3 C row 8; SCE7 step 6) | Shipped, if the warehouse's ship confirmation arrived | Shipped | Collected | Shipped, but for which item |
| 6 In transit (SCE7 step 7) | Shipped | Closed | In transit | Only the portal knows where it is |
| 7 Delivered (SCE7 step 8) | Shipped, or delivered if events flow back | Closed | Delivered | One item delivered; the second item's fate depends on what the order system did at moment 3 |

```viz
{"kind": "matrix", "title": "One Corvane web order, three systems (fictional)", "cols": ["Order system", "Warehouse system", "Carrier portal"], "rows": [{"label": "1 Sourced", "tone": 3, "cells": ["sourced", null, null]}, {"label": "2 Released", "tone": 3, "cells": ["released", "released", null]}, {"label": "3 Short pick", "tone": 5, "cells": ["released", "one short", null]}, {"label": "4 Packed", "tone": 5, "cells": ["released", "packed", "label"]}, {"label": "5 Collected", "tone": 2, "cells": ["shipped?", "shipped", "collected"]}, {"label": "6 In transit", "tone": 2, "cells": ["shipped", "closed", "in transit"]}, {"label": "7 Delivered", "tone": 2, "cells": ["delivered?", "closed", "delivered"]}], "legend": [{"mark": "shipped?", "means": "only if the warehouse's ship confirmation reached the order system"}, {"mark": "delivered?", "means": "only if the carrier's events reached the order system; otherwise still shipped"}, {"mark": "one short", "means": "known to the warehouse system before any other system"}], "caption": "The statuses of section 8 of this unit for one Corvane web order filled by the centre, at seven moments. Case register (Corvane, fictional) and this unit's assumptions; moments joined to SCE3 deliverable C and SCE7 section 6; status words are this unit's working terms, not a source's."}
```

What the table shows, as this unit's reading: from moment 3 to moment 7 the three systems never agree, and each is right about its own event. The short line is known only to the warehouse system until a message carries it to the order system, which must then re-source it, cancel it or tell the customer. SCE4 §9 traced the same chain from the inventory side.

## 9. How integration is done, at the level a product person needs

**Four styles.** The *Enterprise Integration Patterns* site, in a page by Bobby Woolf, names four integration styles: **file transfer** (each application produces files of shared data for others to consume), **shared database** (the applications store the data they share in a common database), **remote procedure invocation** (each application exposes procedures that others invoke remotely; an API, application programming interface, is this course's gloss for such a procedure) and **messaging** (applications connect to a common messaging system and exchange messages) ([Hohpe & Woolf, *Enterprise Integration Patterns*, Addison-Wesley, 2003, ch. 2, "Integration Styles", introduction by Woolf, read at the authors' site](https://www.enterpriseintegrationpatterns.com/IntegrationStylesIntro.html)) [practice]. The authors write that each style has its advantages and disadvantages, and that they believe messaging is often the best style (same page) [practice]. The style decides how fast a fact crosses: a nightly file carries yesterday's stock (this unit's inference).

**The business message standards.** Two families carry the messages named in this course. X12 describes itself as an ANSI-accredited, consensus-based, non-profit organisation, chartered by ANSI for more than 40 years, with more than 320 transaction standards, and says that millions of entities around the world support X12 transactions ([X12, "About X12"](https://x12.org/about/about-x12)) [practice: a standards body's statement about itself, with no count behind "millions"]. UN/EDIFACT is, in GS1's description, a set of internationally agreed standards, directories and guidelines for electronic exchange of structured data, approved and published by UN/CEFACT (EANCOM Part I, §5) [independent]. Which regions use which family was not found on either body's page; X12 claims use around the world and UN/EDIFACT is published as an international standard. The course's earlier note, "regional use not sourced" (SCE7 §7), stands (flag F79). The messages at this unit's seams:

| Seam | X12 | UN/EDIFACT or EANCOM | GS1 key carried |
|---|---|---|---|
| Order to warehouse | 940 Warehouse Shipping Order | not opened here | GTIN, GLN |
| Warehouse to transport and receiver | 856 Ship Notice/Manifest; 945 Warehouse Shipping Advice | Despatch advice, as GS1's label guideline names it; its EANCOM message not opened here | SSCC, GSIN |
| Transport tender and answer | 204, 990 (SCE7, SCE8) | not opened here | GSIN, GINC |
| Status | 214 (SCE8) | IFTSTA | SSCC, GINC |
| Freight bill | 210 (SCE8) | not opened here | GINC |

The key-to-message column is this unit's reading of GS1's reference card against the messages' scope; no source opened maps them one to one.

## 10. The yard and the dock: a seam of its own

The dock is where the warehouse's last step and the carrier's pickup happen at once (SCE7 §9). It is also where three systems can each hold a calendar. Gartner's market page for yard management describes a yard management system (YMS) as one that "supports the efficient flow of work, equipment and materials", through the planning, direction, monitoring and control of activities such as scheduling, moving, parking, inspecting and reassigning trucks, trailers and containers ([Gartner Peer Insights, Yard Management, undated](https://external.pi.gpi.aws.gartner.com/reviews/market/yard-management)) [analyst]; the page carries this description in an unattributed "What is Yard Management?" section. Bartholdi and Hackman describe the YMS as software a WMS may talk to (p. 33) [practice].

**The physical event.** A truck arrives at the gate, waits in the yard, is called to a door, is loaded or unloaded and leaves. SCE7 §9 gives the US regulator's figures for drivers waiting at docks.

**Who holds the truth.** The appointment can be held in the warehouse system (W2), a yard system or the transport system (T7) (SCE7 §9; SCE8 deliverable C, row 7). By section 7's rule, the door and the time slot at the operation's own dock belong to whichever system records the truck's arrival and the door's use; at Halvern (fictional) that would be the warehouse line, whose Yard module is in the register; that Yard holds the appointment (W2) is this unit's placement, as SCE6 deliverable B, row 2, left it open.

**People and measure.** The warehouse's dock team and the transport planner (working); SCE7 §11's dwell time and detention measure the wait.

**How it fails.** A carrier booked for a time the dock cannot serve, because the transport planner's calendar and the warehouse's door plan are separate (this unit's inference); a truck that waits and a detention charge that reaches the freight bill without the warehouse knowing why (SCE7 §6, step 10).

## 11. What people do around a broken seam

One study opened describes workarounds in a retail setting. Van de Weerd, Vollers, Beerepoot and Fantinato observed and interviewed 12 team managers in four stores of one Dutch supermarket chain from March to June 2018, analysed its prescribed processes, and validated the 29 workarounds they found with a survey of 292 team managers across the Netherlands ([van de Weerd et al., ECIS 2019](https://aisel.aisnet.org/ecis2019_rp/183); full text read at [Utrecht University's repository](https://dspace.library.uu.nl/bitstream/handle/1874/384797/ECIS2018_Workarounds_in_Retail_V2.pdf?sequence=1)) [independent]. Among them: "Using a shadow administration for restocking planning" (159 survey respondents confirmed it), using another app to find the product number needed to order in the order app (236), "Still using the previous, outdated platform" (247), and "Needing private email to access the cargo tracker" (6) (p. 5–6) [independent]. The study covers stores and their team managers, not warehouses or transport; applying it to Corvane's centre or to a food distributor's dispatch desk is this unit's inference.

Alter's theory of workarounds treats them as a process with its own causes, and the abstract says the theory can help explain compliance and non-compliance with mandates and inform systems analysis and design ([Alter, 2014, *Communications of the AIS* 34, art. 55, abstract](https://aisel.aisnet.org/cais/vol34/iss1/55/)) [independent, abstract only].

The workarounds this course's case shows are register facts: Ostrel Foods (fictional; a food distributor with its own 40 vehicles) agrees substitutions by phone and does not record them, and runs paper delivery notes on some routes (case register). Re-keying carrier labels from portals at Corvane is SCE3's reading of the register. That spreadsheets and phone calls fill every broken seam in warehouses and transport is common in the industry; no independent source on logistics operations was found (claim C14 is SCE13's).

## 12. One vendor or specialists: common claim C9

The claim as it circulates: "One platform from one vendor lowers total cost" (C9, seed bibliography). Corvane is deciding whether to replace its warehouse system and whether to buy order and transport systems from the same vendor (case register). **Best of breed** is buying each function from the vendor whose package fits it best and joining the packages (glossary). Each side's argument, attributed to the kind of party that makes it:

| Argument | Who makes it | Source and grade |
|---|---|---|
| A single vendor gives a simpler model of IT infrastructure that promises synergies | The authors, stating the case for single-vendor ERP | Light, Holland, Kelly & Willis, ECIS 2000, Discussion and Conclusion [practice: the authors' own statement] |
| Upgrades keep the customer on current technology with less reliance on its own IT staff | Single-vendor ERP vendors ("vendors of ERP software state", as the authors report it) | Same paper [practice: the authors' report of vendors' claims] |
| Components from several vendors fit each function better, change less at once and spread the risk of one vendor leaving the market | Advocates of best of breed, as the authors summarise them | Same paper [practice] |
| Best of breed's main difficulties are "the complexity of implementation" and "the likely costs of future ownership", including keeping the links between packages | The authors | Same paper [practice] |
| Warehouse system vendors are already connected to financial systems; enterprise systems have the advantage where they grow out of manufacturing | Textbook authors | Bartholdi & Hackman §4.5 [practice] |
| (A definition, not an argument) A supply chain management suite is "a portfolio of (pre)packaged applications" spanning several process clusters, logistics and fulfilment among them | Analyst, defining the market | [Gartner Peer Insights, Supply Chain Management Suites market page, undated](https://external.pi.gpi.aws.gartner.com/reviews/market/supply-chain-management-suites) [analyst] |
| "One vendor for execution"; "No integration to build"; "Live in weeks" | Fictional vendors: a suite, an ERP vendor, a specialist | Case register (Halvern, Varnby, Kestrow; fictional); evidence of nothing about real vendors |

**What the evidence shows.** The one study found that compares the two strategies is a single case: the operations division of a record company with about 10,000 stock-keeping units and sites in about eighty countries, studied through interviews with two project staff over two years and its plans and accounts. It built a best-of-breed system from several vendors' packages, under a rule agreed with senior managers that package software would be used wherever possible and would meet at least 80% of the desired functionality, and the authors report an 80%-plus fit for each element of the system's framework; the project had taken about 36 months when the paper was written, which the authors judge comparable to a similarly sized single-vendor ERP implementation; they conclude "no one strategy is the 'best' for all contexts" (Light, Holland, Kelly & Willis, [ECIS 2000](https://aisel.aisnet.org/ecis2000/180); full text read at [Salford's repository](https://salford-repository.worktribe.com/OutputFile/1499857)) [independent: one case, two interviewees]. The authors' journal version reports the same comparison of implementation complexity, functionality, process alignment and maintenance ([Light, Holland & Willis, 2001, *Business Process Management Journal* 7(3), 216–224, abstract](https://doi.org/10.1108/14637150110392683)) [independent, abstract only]. Both concern ERP against best of breed in general, not order, warehouse and transport systems; applying them to execution software is this unit's inference. Gartner's 2026 Supply Chain Management Suites evaluation refused the fetch, so nothing from it is stated.

**C9's verdict.** No independent source found that measures the total cost of buying order, warehouse and transport systems from one vendor against buying each from a specialist. SCE16 prices it.

**What a customer gains and gives up**, as this unit's reading of the arguments above and of sections 2 to 10:

- **Gains with one vendor.** Fewer seams built by the customer: the vendor owns the messages of sections 2 to 4 inside its line, and one support contract covers them. A suite can still leave seams to the ERP (section 5) and to carriers (section 9): Halvern's "One vendor for execution" names its own three lines, not the ERP (SCE6 deliverable B, row 28) or the carriers (SCE8 deliverable C, row 18).
- **Gives up with one vendor.** The choice of the best fit for each function, and the vendor's own speed on each line; the upgrade timetable is the vendor's (the concern of some managers in the authors' study that they "may be left waiting for the next upgrade" from their ERP vendor, Light et al.) [practice].
- **Gains with specialists.** Fit per function and the risk spread across vendors (Light et al.) [practice].
- **Gives up with specialists.** The seams become the customer's: each message, each shared master record and each status mapping of section 8 is built, tested and kept by the customer or its implementer (Light et al.'s costs of future ownership) [practice].

## On a site visit

Ask to watch one order cross every seam, and ask at each:

- At release: what happens on the warehouse screen when a web order is cancelled after release? Who sees it first? (Section 2.)
- At a short pick: how long until the order system knows, and who decides between re-sourcing, cancelling and telling the customer? (Section 8.)
- At the pack station: is the carrier label printed from the warehouse system or keyed from a portal? Does its tracking number reach the order system? (Section 3.)
- At the dock: which calendar does the gatehouse use, and does the transport planner see it? (Section 10.)
- At the customer desk: where does the agent read status, the order system or the carrier's page? (Section 4.)
- In finance: which document starts the customer invoice, and which the carrier payment? (Section 5.)
- Everywhere: which spreadsheet, paper list or phone call does this step depend on? Write it down; the retail study found its workarounds by interviews and observation (section 11).

## Self-check

1. **What is a seam, and where do SCE9's order steps join the warehouse's and the shipment's?** A point where one system hands a fact to another and stops being the place that changes it. SCE9's rows 5 to 8 are SCE3 deliverable C's rows 1 to 8 for an order the centre fills, and rows 8 to 10 are SCE7 §6's steps 6 to 8 (section 1).
2. **Which X12 messages carry an order to a warehouse and the confirmation back?** The 940 Warehouse Shipping Order, which tells a warehouse to make, confirm, change or cancel a shipment; the 945 Warehouse Shipping Advice, which tells the depositor the shipment was made and reconciles ordered with shipped quantities (sections 2, 3).
3. **What ties a physical pallet to the electronic notice about it?** The SSCC: the one mandatory element on GS1's logistic label, listed per unit in the despatch advice, so that a scan can be matched to the message (section 3).
4. **Is IFTSTA a UN/EDIFACT message?** Yes: UN/CEFACT's D.01A documentation lists it as a United Nations Standard Message from the transport sub-group, and GS1's EANCOM is a subset of UN/EDIFACT (section 4).
5. **Why can the order system and the warehouse system both claim stock?** Gartner's DOM definition gives the order system enterprise inventory for available-to-promise; its WMS definition gives the warehouse system storage and counting. The course places stock at a location in the warehouse system and the sellable figure in the order system (sections 2, 7).
6. **During a short pick, which system knows first, and what does the customer see?** The warehouse system. Until a message reaches the order system, it still shows the order released, and the carrier's portal can show a label for one unit while the order system shows nothing shipped (section 8).
7. **Is it established that one vendor for order, warehouse and transport lowers total cost?** No independent source found. The one comparative case found concerns ERP against best of breed, is a single company with two interviewees, found implementation time comparable, and concludes that no strategy is best for all contexts (section 12).

## Deliverable

Four parts: A, Corvane's system-of-record table; B, the handoff failure catalogue across the three case operations; C, both templates; D, glossary lines. Cells cite this unit's sections in brackets, an earlier unit's section, "register" for a case fact, or "working" for a working description that rests on no source. A failure listed is one to look for; it is no claim that the operation has it unless it says "known trouble".

### A. System-of-record table: Corvane (fictional)

Corvane (fictional): 60 stores in four European countries and one website; one distribution centre; an ERP, a warehouse system about twelve years old on its own servers, an order system for the website, carriers booked through each carrier's own portal, no transport system; deciding whether to replace the warehouse system and whether to buy order and transport systems from the same vendor (case register). The table gives today's owner; the last column says what the decision would move.

| # | Fact | Owner (system of record) | Who else holds a copy | What breaks when they differ | If one vendor's suite is bought |
|---|---|---|---|---|---|
| 1 | Item: number, description, GTIN | ERP (working; SCE1) | Order system, warehouse system, carrier portals | A web item the centre cannot find by number; a box whose GTIN the warehouse does not know (6) | Unchanged: the ERP stays outside an execution suite (SCE6 B, row 28) |
| 2 | Item pack, dimensions, unit of measure | ERP (working) | Warehouse system; carrier portals (parcel size) | Wrong carton at packing; 12 read as 12 cases; parcel charges the shipper did not expect (6) | Unchanged; the suite takes a copy |
| 3 | Store and customer addresses | ERP for stores; order system for web customers (working) | Warehouse system (labels), carrier portals | Parcel or store delivery to an old address (6) | Order line owns web addresses; ERP still owns stores |
| 4 | Carrier and service | Each carrier's portal; the ERP holds carriers as suppliers (working; register) | Warehouse system (labels) | Label for a service the carrier does not run (6) | Moves to the transport line (T8 holds the choice; F98) |
| 5 | Web order, its lines and promise date | Order system (Gartner DOM [analyst]; register) | Warehouse system (released lines), ERP (sales record, working) | Changed or cancelled order still picked (2; SCE9 §8) | Unchanged in owner; the seam becomes the vendor's |
| 6 | Stock sellable on the web | Order system, computed (7; course's) | Warehouse system's records it is computed from | Promised from stock the centre cannot find (register: known trouble) | Unchanged in owner; one vendor's copy may refresh sooner (working) |
| 7 | Stock by location in the centre | Warehouse system (Gartner WMS [analyst]; B&H ch. 4 [practice]) | Order system (as a total), ERP (valuation, working) | Phantom stock (SCE4 §4); a total that matches while locations do not | Unchanged in owner |
| 8 | Store stock | Not in the register (how store stock reaches the order system is open; SCE9 A, row 2) | Order system | Order sourced to a store whose shelf is empty (SCE9 §6) | Open (notes) |
| 9 | Release, allocation, short pick | Warehouse system (SCE3 §2) | Order system (status) | Order shows lines that will not ship (8) | Unchanged in owner |
| 10 | Shipment record: units, SSCC, departure | Warehouse system (B&H §4.1 [practice]; GS1 [independent]) | ERP (invoice trigger), carrier portal (label) | Invoice for goods that did not ship; label and record differ (3, 5) | Unchanged; the transport line takes a copy |
| 11 | Carrier label and tracking number | Each carrier's portal, re-keyed (register; SCE3 C, row 6) | Warehouse system (if keyed), order system (if passed) | Tracking number missing from the customer's message (4) | Printed at the pack station from the warehouse line (W22; F98) |
| 12 | Dock appointment at the centre | Warehouse system, or none (SCE7 A, row 5) | Carrier's booking | Truck waits; detention reaches the freight bill unexplained (10) | Warehouse line, Yard module (W2; this unit's placement: the register lists Yard, SCE6 B row 2 left W2 open; notes 10) |
| 13 | Status in transit and proof of delivery | Each carrier's portal (register) | Order system, if events flow (working) | Customer told nothing; Jonas reads the portal (4) | Transport line (Tracking; register) owns events; the order line shows them |
| 14 | Customer payment and invoice record | ERP (SCE1 working placement) | Order system (payment reference, working) | Refund or invoice on the wrong amount (5) | Unchanged |
| 15 | Carrier invoice, approved charge, payment | ERP (SCE7 A, rows 9 to 11, working) | Carrier portals | Unexpected charges paid unchecked (SCE7 A, row 10) | Approved charge in the transport line (Freight Audit); payment in the ERP (7; working; revises SCE7 §5's placement of Freight Audit at steps 10 and 11 and SCE8 deliverable C, row 14; notes) |
| 16 | Return authorisation and refund trigger | Order system for the authorisation (SCE9 §9); the refund trigger is not in the register | Warehouse system (receipt, grade), ERP (refund) | Return received and not refunded, or refunded and not received (SCE9 A, rows 11, 12) | Order line Returns module authorises; which line grades is open (SCE6 B, row 14) |
| 17 | Carrier booking: the tender and the carrier's answer | Each carrier's portal (register; SCE7 A, rows 3, 4); no analyst definition names tendering (SCE1 §3; flags F64, F89) | Warehouse system (pickup time, if keyed) | Booked for a time the centre's dock cannot serve (10) | Transport line (Rating and Tendering; register) |

Below the table: seventeen facts; four rest on sourced placements (5, 7, 9, 10) and twelve on working placements or the register (1 to 4, 6, 11 to 17); row 8, and the refund trigger and the grading of returns in row 16, are open. The decision moves five owners (4, 11, 12, 13, 17) and one approved charge (15); it leaves the ERP's facts (1, 2, 14) where they are.

### B. Handoff failure catalogue: Corvane, Ostrel Foods and Tandric Logistics (fictional)

Ostrel Foods (fictional): a food distributor with one three-zone warehouse, its own 40 vehicles, an ERP with a warehouse module, a routing tool and paper delivery notes on some routes; known trouble: substitutions agreed by phone and not recorded, drivers returning with refused goods (case register). Tandric Logistics (fictional): one multi-client warehouse, a freight desk with no trucks, a shared warehouse system, a transport system and a client portal; known trouble: invoices disputed because activity was not recorded (case register).

| # | Handoff | Operation | Failure | Who sees it first | Who can fix it |
|---|---|---|---|---|---|
| 1 | Order to warehouse | Corvane | Web order promised from stock the centre cannot find (register: known trouble) | Mina, at the empty location (register; SCE5) | Carla corrects the record; Oskar sets the buffer (register, SCE4, SCE9) |
| 2 | Order to warehouse | Corvane | Cancellation reaches the order system, not the released work (2; SCE9 §8) | A packer on Tobias's shift, if anyone (reading of register; working) | Whoever owns the interface; Ravi, IT director (register) |
| 3 | Warehouse back to order | Corvane | Short pick not passed back; order shows lines that will not ship (8) | Lena's exception queue, if it shows; otherwise the customer (register, SCE9) | Lena re-sources or cancels (register, SCE9) |
| 4 | Warehouse to transport | Corvane | Label re-keyed from a portal differs from the shipment record (3; SCE3 C, row 6) | The carrier, at a failed scan (working) | Tobias's shift; a carrier connection removes it (SCE6 §5) |
| 5 | Transport to customer | Corvane | Status only in each carrier's portal (4; register) | Jonas, when the customer calls (register) | Not in the register; the decision would move it (A, row 13) |
| 6 | Order to warehouse | Ostrel | Substitution agreed by phone, not on the order (register: known trouble) | Ilse's picker or the driver at the door (register; SCE5) | Nuno records it; Aart decides the process (register) |
| 7 | Routing tool to warehouse module | Ostrel | Route changed after picking began, cages staged for the old route (register, SCE5: Sofia sometimes changes routes after picking has begun) | Ilse, at staging (reading of SCE5's register rows; notes 7) | Sofia re-plans (register, SCE5); Ilse moves cages (reading; notes 7) |
| 8 | Transport back to ERP | Ostrel | Refused goods return with the driver, recorded on a paper note only (register: known trouble; paper notes) | Nuno, from the driver's call (register, SCE8) | Not in the register who books the return into stock and credits the customer |
| 9 | Warehouse back to ERP | Ostrel | Short-dated stock found too late, after the order was promised (register: known trouble) | Ilse's picker (reading of register; working) | Bram and Ilse at replenishment; rotation rules (SCE4 §2) |
| 10 | Client order to warehouse | Tandric | A client's order arrives in a form the shared warehouse system does not take, and is keyed by hand (working; 2, X12 940) | Luis, at onboarding, or the warehouse team (register) | Luis configures the client; Dario administers (register) |
| 11 | Warehouse back to client billing | Tandric | Activity done and not recorded, so the client invoice is disputed (register: known trouble) | Olu, from the client's query (register) | Anke's site records it; Karin settles the dispute (working: the register has her sign client contracts) |
| 12 | Warehouse to transport | Tandric | Load not ready when the carrier arrives; detention on the bill (10; SCE7 B, rows 5, 6) | The carrier's driver; Priya, on the invoice (register) | Anke's dock plan; Priya passes the charge on or not (register, SCE7 B, row 10) |
| 13 | Transport back to finance | Tandric | Proof of delivery not returned, so the client cannot be billed (SCE7 B, row 8) | Olu or Priya (working; notes 9) | The carrier; Priya chases it (working; notes 9) |
| 14 | Transport to client | Tandric | Client asks about a load before Tandric knows (SCE7 B, row 7) | Olu (register) | The carriers' status feed; Dario for the portal (register) |

Below the table: fourteen failures; five rest on register known trouble (1, 6, 8, 9, 11) and nine on this unit's or an earlier unit's reading. DD-SCE2 extends the catalogue with peak and exceptions.

### C. Templates

**C1. System-of-record table.** One row per fact; fill it for a real operation from its own system documentation and interviews, dated.

| # | Fact | Owner (system of record) | Who else holds a copy | What breaks when they differ | If the decision under study is made |
|---|---|---|---|---|---|
| 1 | The fact, as narrow as one field or record (an item's unit of measure, a shipment's departure time) | The one system whose copy wins; its basis: a source with its grade, the operation's own documentation (dated), or "working" | Every other system holding it, and how its copy arrives (file, message, call, re-keyed) | What a person sees go wrong, where and when, and the section or source that says so | The owner after the purchase or change, or "unchanged" |

Start with the five shared kinds (items, locations, customers, carriers, units of measure), then each seam's facts (sections 2 to 5). Below the table, count the facts with a sourced owner, a working owner and none, and list the open ones.

**C2. Handoff failure catalogue.** One row per failure; fill it from a site visit (On a site visit) and the operation's incident or exception records.

| # | Handoff | Operation | Failure | Who sees it first | Who can fix it |
|---|---|---|---|---|---|
| 1 | From system, to system, and the step (SCE9, SCE3, SCE7 numbering) | The operation | What goes wrong, in the operation's words; "known trouble" only if the operation says so | The role (and name, if given) who first notices, and how: a screen, a scan, a phone call | The role who can correct this case, and the role who can stop it recurring |

Below the table, count the failures the operation reports and those you inferred, and mark the ones a purchase under study would remove.

### D. Glossary lines

| Term | Working definition | Source |
|---|---|---|
| Seam | A point where one system hands a fact to another and stops being the place that changes it | Course term (this unit) |
| Handoff | The message, file or call that carries a fact across a seam | Course term (this unit) |
| Enterprise resource planning (ERP) | The company's financial and master-data system; no broadly agreed definition in the research | Working definition; Klaus, Rosemann & Gable 2000, abstract [independent] |
| Depositor | The owner of goods held in a warehouse, who tells the warehouse to ship | X12 940 [independent]; definition is the course's |
| Warehouse Shipping Order (X12 940) | The message telling a warehouse to make, confirm, change or cancel a shipment | X12 [independent] |
| Warehouse Shipping Advice (X12 945) | The warehouse's message that a shipment was made, reconciling ordered with shipped quantities | X12 [independent] |
| Ship Notice/Manifest (X12 856) | The message describing a shipment's contents and configuration | X12 [independent] |
| Despatch advice; advance ship notice (ASN) | The message listing each logistic unit's SSCC and contents | GS1 Logistic Label Guideline [independent] |
| UN/EDIFACT | The UN's standards, directories and guidelines for electronic data interchange, published by UN/CEFACT | GS1 EANCOM Part I [independent] |
| EANCOM | GS1's subset of UN/EDIFACT, based on directory D.01B | GS1 EANCOM Part I [independent] |
| IFTSTA | UN/EDIFACT's international multimodal status report message | UN/CEFACT D.01A [independent] |
| GTIN | GS1's key for products at any packaging level | GS1 reference card [independent] |
| GLN | GS1's key for physical locations such as ship-from and ship-to | GS1 reference card [independent] |
| GSIN | GS1's key for a shipment of logistic units delivered together, assigned by the seller and shipper | GS1 reference card; GSIN page [independent] |
| GINC | GS1's key for a consignment of logistic units, possibly of different shipments | GS1 reference card [independent] |
| GDSN | GS1's network for keeping trading partners' product data the same | GS1, How GDSN works [practice] |
| Unit of measure code | A code from UN/CEFACT Recommendation No. 20's single list | UN/CEFACT [independent] |
| Integration style | File transfer, shared database, remote procedure invocation or messaging | Woolf, Enterprise Integration Patterns [practice] |
| Application programming interface (API) | A procedure one system exposes for others to call over a network | Course gloss of remote procedure invocation (section 9) |
| Yard management system (YMS) | Software for scheduling, moving, parking and inspecting trucks, trailers and containers in the yard | Gartner Peer Insights yard page [analyst]; B&H ch. 4 [practice] |
| Workaround | A way of getting the work done outside the prescribed process or system | Course gloss; Alter 2014, abstract [independent]; van de Weerd et al. 2019 [independent] |
| Best of breed | Buying each function from the vendor whose package fits it best, and joining them | Light et al. 2000, 2001 [practice] |
| Supply chain management suite | A portfolio of packaged applications spanning several supply chain process clusters | Gartner Peer Insights [analyst] |

## Sources

- Alter, S. (2014). Theory of Workarounds. *Communications of the Association for Information Systems* 34, article 55. https://doi.org/10.17705/1CAIS.03455 (abstract read at https://aisel.aisnet.org/cais/vol34/iss1/55/)
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, 2017, ch. 4, pp. 33–36. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- European Parliament and Council. Directive 2011/7/EU of 16 February 2011 on combating late payment in commercial transactions (recast), Article 3, as adopted (legislation.gov.uk copy). https://www.legislation.gov.uk/eudr/2011/7/article/3/adopted
- European Commission. Proposal for a Regulation on combating late payment in commercial transactions, COM(2023) 533, procedure 2023/0323/COD, EUR-Lex procedure page (read 28 Nov 2026). https://eur-lex.europa.eu/procedure/EN/2023_323
- European Commission. 2027 Commission work programme, adopted 4 November 2026 (Annex III, pending proposals to be withdrawn, not opened). https://commission.europa.eu/strategy-and-policy/strategy-documents/commission-work-programme/commission-work-programme-2027_en
- Gartner Peer Insights. Distributed Order Management (DOM) Systems Reviews and Ratings, market definition and features, features updated July 2025, read 28 Nov 2026. https://external.pi.gpi.aws.gartner.com/reviews/market/distributed-order-management-systems
- Gartner Peer Insights. Warehouse Management Systems, market definition, features updated May 2026, read 28 Nov 2026. https://external.pi.gpi.aws.gartner.com/reviews/market/warehouse-management-systems
- Gartner Peer Insights. Supply Chain Management Suites, market definition, undated, read 28 Nov 2026. https://external.pi.gpi.aws.gartner.com/reviews/market/supply-chain-management-suites
- Gartner Peer Insights. Yard Management Reviews and Ratings, undated, read 28 Nov 2026. https://external.pi.gpi.aws.gartner.com/reviews/market/yard-management
- GS1. EANCOM 2002, Part I, section 5, "United Nation's Directories for Electronic Data Interchange for Administration, Commerce and Transport". https://gs1.org/sites/gs1/files/docs/eancom/ean02s3/part1/part1_05.htm
- GS1. GS1 Identification Keys at Your Finger Tips (reference card), undated. https://www.gs1.org/sites/default/files/docs/idkeys/gs1_id_keys_reference_card.pdf.pdf
- GS1. GS1 Logistic Label Guideline, release 1.3, July 2019. https://gs1.org/standards/gs1-logistic-label-guideline
- GS1. GS1's GDSN Keeps Trading Partners' Product Data in Sync, undated. https://www.gs1.org/how-gdsn-works
- GS1. Global Shipment Identification Number (GSIN), undated. https://www.gs1.org/gsin
- Hohpe, G. & Woolf, B. (2003). *Enterprise Integration Patterns*. Addison-Wesley, ch. 2, "Integration Styles"; introduction by Woolf read at https://www.enterpriseintegrationpatterns.com/IntegrationStylesIntro.html
- Ishfaq, R., Defee, C. C., Gibson, B. J. & Raja, U. (2016). Realignment of the physical distribution process in omni-channel fulfillment. *International Journal of Physical Distribution & Logistics Management* 46(6/7), 543–561. https://doi.org/10.1108/IJPDLM-02-2015-0032 (abstract read)
- Klaus, H., Rosemann, M. & Gable, G. G. (2000). What is ERP? *Information Systems Frontiers* 2(2), 141–162. https://doi.org/10.1023/A:1026543906354 (abstract read at https://ideas.repec.org/a/spr/infosf/v2y2000i2d10.1023_a1026543906354.html)
- Light, B., Holland, C. P., Kelly, S. & Willis, K. (2000). Best of Breed IT Strategy: An Alternative to Enterprise Resource Planning Systems. *ECIS 2000 Proceedings*, 180. https://aisel.aisnet.org/ecis2000/180 (full text read at https://salford-repository.worktribe.com/OutputFile/1499857)
- Light, B., Holland, C. & Willis, K. (2001). ERP and best of breed: a comparative analysis. *Business Process Management Journal* 7(3), 216–224. https://doi.org/10.1108/14637150110392683 (abstract read at https://salford-repository.worktribe.com/output/1448144/erp-and-best-of-breed-a-comparative-analysis)
- United Nations. Protocol to the Convention on the Contract for the International Carriage of Goods by Road (CMR), Geneva, 5 July 1978. *United Nations Treaty Series* vol. 1208, No. 19487. https://treaties.un.org/doc/Publication/UNTS/Volume%201208/volume-1208-I-19487-English.pdf
- UN/CEFACT. Recommendation No. 20: Codes for Units of Measure Used in International Trade, TRADE/CEFACT/2001/20, 15 January 2001. https://digitallibrary.un.org/record/431844/files/%5BE_ECE_%5DTRADE_CEFACT_2001_20-EN.pdf
- UN/CEFACT. UN/EDIFACT Standard Directory D.01A and related documentation, TRADE/CEFACT/2001/33, 14 February 2001. https://digitallibrary.un.org/record/433163/files/%5EE_ECE_%5ETRADE_CEFACT_2001_33-EN.pdf
- van de Weerd, I., Vollers, P., Beerepoot, I. & Fantinato, M. (2019). Workarounds in Retail Work Systems: Prevent, Redesign, Adopt or Ignore? *Proceedings of the 27th European Conference on Information Systems (ECIS)*, Stockholm & Uppsala. https://aisel.aisnet.org/ecis2019_rp/183 (full text read at https://dspace.library.uu.nl/bitstream/handle/1874/384797/ECIS2018_Workarounds_in_Retail_V2.pdf?sequence=1)
- X12. 856 Ship Notice/Manifest. https://x12.org/node/4398
- X12. 940 Warehouse Shipping Order. https://x12.org/node/4444
- X12. 945 Warehouse Shipping Advice. https://x12.org/node/4447
- X12. About X12. https://x12.org/about/about-x12

## Unsure list

# Unsure: SCE10

1. Klaus, Rosemann and Gable (2000): the abstract was read at IDEAS/RePEc, a bibliographic index, because the DOI address was refused; its wording was not checked at Springer (section 5, glossary, notes contradiction 4).
2. Light, Holland, Kelly and Willis (2000): the full text was read at the University of Salford's repository, whose version is not stated, and the AIS eLibrary record spells the fourth author "Willis"; the quotations ("no one strategy is the 'best' for all contexts", "the complexity of implementation", "the likely costs of future ownership", "may be left waiting for the next upgrade") come from the fetch tool's extraction of that copy (section 12).
3. Light, Holland and Willis (2001): the journal abstract was read at the Salford repository's record, not at Emerald (section 12).
4. Van de Weerd et al. (2019): the survey counts per workaround (159, 236, 247, 6) and pages 5–6 are from the fetch tool's reading of the Utrecht repository copy, whose file name says ECIS2018 while the paper and the AIS record say ECIS 2019 (section 11).
5. Gartner's yard management description is from an unattributed "What is Yard Management?" section of the Peer Insights page, truncated in the fetch; graded analyst because it sits on Gartner's page (section 10, glossary).
6. Directive 2011/7/EU was read in legislation.gov.uk's copy of the text as adopted; no act amending Article 3 was found by search on 28 November 2026, and EUR-Lex lists the 2023 proposal to replace the directive (procedure 2023/0323/COD) as ongoing; no consolidated EU text was opened (section 5).
7. The UN/CEFACT D.01A documentation lists IFTSTA as a UNSM; the fetch tool reported the table's line breaks split the entry, and the D.01B directory that EANCOM uses was not itself opened (section 4).
8. GS1's reference card is undated and gives no allocating party; the GSIN's "seller and shipper" comes from GS1's GSIN page, which has no headline or date (section 6).
9. Section 7's dock and parcel rows cite Bartholdi and Hackman's §4.3 menu and Gartner's 2022 WMS and 2026 TMS reports as SCE6 §6 and SCE8 §7 read them; this unit did not re-open §4.3 or either Gartner report, and Gartner's TMS page failed here.
10. Section 9's table pairing GS1 keys with messages is this unit's reading; no source opened maps keys to X12 or UN/EDIFACT messages.

Object: none

Fresh check 2026-11-28 (claude-opus-5-5): fix · 1 error, 5 should-fix, 18 minor; all applied; report `audits/supply-chain-execution/fresh-check-SCE10.md`
Quality review 2026-11-28 (claude-opus-5-5): fix · 0 error, 8 should-fix, 14 minor; all applied; report `audits/supply-chain-execution/quality-review-SCE10-2026-11-28.md`
