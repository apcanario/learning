---
code: SCE1
title: The map, the words and the evidence
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-21
search: on
intro: What it is: the course's opening unit. It draws the line between planning and execution, walks one order from promise to delivery as an eleven-step map (twelve rows with inbound), says what the warehouse, transport and order systems and the ERP each hold as their own record, names the neighbouring systems and the kinds of company that run these operations, lists Gartner's analyst categories with their dates (no vendor named), shows how an analyst evaluation is made and paid for (Forrester's Wave method in full, Gartner's in part), and sets the four-grade key (independent, analyst, vendor-reported, practice) that every later unit uses. Section 11 states the fourteen common claims; C1, C2 and C10 are set against what was opened here, C4 against SCE4, C3, C5 and C6 against SCE5, and C8 against SCE6; the other six are marked "not searched here" with the unit that tests each. Deliverable: Corvane's (fictional) execution map, a 39-row working glossary, the grade key with one worked example per grade, and the map as a blank template. How it was made: written 21 Nov 2026 with web search on by a fresh claude-opus-5-5 writer, launched without worktree isolation because the harness denied it (its isolation was the packet folder); fresh-checked by a separate claude-opus-5-5 agent, verdict fix (1 error, 2 should-fix, 24 minor), whose report was saved by the main chat because the checker's Write was refused; findings applied by a claude-opus-5-5 applier, which applied 24 and held 3 (f1, f4, f20). The main chat overrode the f1 hold after re-reading Gartner's index (the Product-Centric Cloud ERP refresh is 2 Nov 2026; the hold rested on a misread) and applied it with three companion edits (the Magic Quadrant FAQ clause in section 8, the Truckload glossary row, the FAQ in Sources). f4 stays held: the Distributed Order Management row of Gartner's index ("none shown", next refresh 23 Nov 2026) was seen by the writer and the applier but not by the checker or the main chat, so that row and the sentence setting it against the abstract are unverified. f20 needs no text change unless the brief replacement for section 11 is vetoed. Filed by a claude-opus-5-5 filer. Known gaps, references not opened: Gartner's Magic Quadrant methodology page (refused the fetch), so Gartner's evaluation criteria are not described beyond the FAQ's two axes and four quadrants; Gartner's content compliance (reprint) policy (refused), so the statement that vendors license Gartner reprints rests on the course brief only; Gartner's ERP glossary page (refused), so the ERP row and glossary line are working definitions; DeHoratius & Raman (2008), seed W8 (not opened); release 0.98.1 of Bartholdi & Hackman named in the seed (release 0.98 of 2017 was read instead); Frazelle, World-Class Warehousing (1996), the origin of both 55% figures (not traced, so both are graded practice); Tompkins et al. (2003), the origin of de Koster et al.'s Fig. 4 (not opened; the chart's travel share could not be read and no number is given from it); the full 2026 MHI and Deloitte Annual Industry Report (only its announcement was read, which states no sample); any source for the warehouse control and execution systems (WCS, WES), marked not sourced here (SCE5 §7 sources both at analyst grade); any source for what a transportation management system holds or how a carrier is paid (SCE7 opened both on 24 Nov 2026, and the TMS row, its tracking and settlement cells in the matrix, the settle step and four glossary rows now cite SCE7's sources; tendering in the TMS and payment in the ERP stay working placements); any source for the US commercial bill of lading (only FAR 47.001, the federal procurement definition, was read); and CMR Art. 1(1), read only in part. Abstract-only claims: Meyr, Wagner & Rohde (2015), that advanced planning systems are built from several modules each covering a range of planning tasks (section 1); Gartner's 2024 methodology note, that Magic Quadrants are visual snapshots of a market's direction, maturity and participants, to be read with the companion Critical Capabilities report and used to narrow a list, "don't base your decision on this evaluation only" (section 8, C10); Gartner's Distributed Order Management Magic Quadrant, its date of 12 Nov 2026 and its sentence on B2B and B2C convergence (section 6, deliverable C); de Vries, de Koster & Stam (2016), that competition-based incentives raised productivity in parallel picking and cooperation-based ones in zone picking, with no effect on quality (C6, deliverable C; the 2015 working paper, read in SCE5, reports error rates that differed by condition); de Koster et al. (2007), whose figure of "as much as 55%" for picking cost appears in the abstract without a source (C2); and Light (2001), that a customisation needs careful consideration for its potential impact on future maintenance (C8, read in abstract by SCE6). Quotations were taken from a fetch tool's extraction and not re-read against a second copy; whether MHI owns MHI Solutions magazine was not confirmed.
---

# SCE1 · The map, the words and the evidence

Every claim in this unit that carries a number, a mechanism or a recommendation ends with its grade in square brackets: [independent], [analyst], [vendor-reported] or [practice]. Section 10 defines the four grades, and the deliverable gives the key with one worked example each. Where this unit could not open a source for something, it says so, and the claim carries no grade because it is not made as a claim. A line marked as this unit's inference, or as the course's own line, carries no grade; it rests on the graded sources it names.

## 1. Execution and planning: where the line runs

Analysts sort supply chain software into planning and execution, and you will meet that split in every evaluation, every sales deck and most job titles in this field. Gartner's glossary entry opens: "Supply chain execution (SCE) is focused on execution-oriented applications", and names warehouse management systems, transportation management systems and global trade management systems among them, together with real-time decision support (dynamic routing and sourcing) and supply chain visibility systems ([Gartner, "Supply Chain Execution (SCE)", glossary, read 21 Nov 2026](https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/supply-chain-execution-sce)) [analyst]. The same entry says order management is sometimes included in execution and that Gartner generally excludes it [analyst].

Planning sits on the other side. A standard text on planning software describes advanced planning systems as built from several software modules, each covering a certain range of planning tasks ([Meyr, Wagner & Rohde, "Structure of Advanced Planning Systems", in Stadtler, Kilger & Meyr (eds.), *Supply Chain Management and Advanced Planning*, 5th ed., Springer, 2015, pp. 99–106, abstract read](https://rd.springer.com/chapter/10.1007/978-3-642-55309-7_5)) [practice]. Gartner evaluates planning software in its own Magic Quadrants (its dated evaluations of the vendors in one software market; section 8), separate from its warehouse, transport and order evaluations: on 21 November 2026 its index listed three *Supply Chain Planning Solutions* evaluations (discrete industries, process industries, and retail and distribution-intensive industries), the first two last updated 18 March 2026 ([Gartner, Magic Quadrant and Critical Capabilities index, read 21 Nov 2026](https://www.gartner.com/magic-quadrant)) [analyst].

This course works with one line, which is its own and not taken from any source: **planning** decides quantities, places and times ahead of the work (how much stock, where, by when); **execution** carries out a particular order, shipment or task on a particular day, and records what physically happened. A planning screen usually shows totals; an execution screen usually shows one order, one pallet, one truck.

Why the line matters for product work, as this unit's inference from the categories above:

- **Buyers evaluate the two separately.** Because the analyst evaluations are separate, a buyer can shortlist a planning product and an execution product from different evaluations, and a product team is compared against the products in its own category.
- **Order management sits on the line.** Gartner generally leaves order management out of execution, yet evaluates distributed order management in a Magic Quadrant of its own (section 6). The order system makes the promise to the customer, which is a decision about the future, and then tracks a real order, which is execution. SCE9 takes this up.
- **Execution software answers to the floor.** Execution records are meant to match physical events (section 2), so an execution product is judged by whether its record agrees with the shelf, the dock and the truck.

## 2. One order, from promise to delivery

This is the map every later unit places itself on. It is drawn at the level of a map only: each step gets one line here and a unit of its own later. The map has eleven steps from order to return, plus the inbound steps (receiving and put-away) that feed every promise; the deliverable gives the inbound pair a row of its own (row 5), so its table has twelve rows and, from Pick on, its numbers run one higher than this list's; later units and the case register cite the deliverable's numbers. The steps are the ones a web order or a store order passes through at a retailer such as Corvane (fictional), a fashion retailer with one distribution centre serving 60 stores and a website (case register).

1. **Take the order.** A customer or a store asks for goods. Corvane's web orders come into an order system for the website (case register).
2. **Promise.** The order system says whether, and when, the goods can be supplied. Gartner's definition of distributed order management (DOM) says the software uses inventory levels for both available-to-promise and available-to-ship ([Gartner Peer Insights, "Distributed Order Management Systems (Transitioning to Distributed Order Management) Reviews and Ratings", definition, read 21 Nov 2026](https://www.gartner.com/reviews/market/distributed-order-management-systems)) [analyst]. **Available-to-promise** (ATP) is the quantity that can still be committed to new orders; **available-to-ship** is the quantity that can leave now.
3. **Source.** The order system chooses which location ships. In Gartner's definition, DOM orchestrates fulfilment using inventory throughout the network, by business rules configured hierarchically by channel, consumer, geography and other criteria (same page) [analyst].
4. **Release to the warehouse.** The warehouse management system (WMS) turns customer orders into pick lists and schedules picking and shipping ([Bartholdi & Hackman, *Warehouse & Distribution Science*, release 0.98, 2017, ch. 4 and §3.3](https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf)) [practice].
5. **Pick.** An operator, or a machine, takes the goods from their storage location. Order picking appears among a warehouse's main activities, after receiving, transfer and put-away, and before accumulation or sortation (grouping picked goods by order or destination), cross-docking (moving goods from receiving to shipping without storing them) and shipping ([de Koster, Le-Duc & Roodbergen, 2007, §2.1](https://doi.org/10.1016/j.ejor.2006.07.009)) [practice].
6. **Pack and ship.** The order is checked, packed and loaded (SCE3 takes steps 4 to 6); Bartholdi and Hackman's outbound sequence is order-picking, then checking, packing and shipping (ch. 3) [practice].
7. **Plan and tender the transport.** Someone decides how the goods travel and offers the load to a carrier. For truckload freight (a vehicle dedicated to one shipper's shipment from origin to destination; Sheffi 2004, as SCE7 §2 cites it), a shipper's annual bid produces a **routing guide** for each lane: a primary carrier and backup carriers in order, with their contract prices, and the spot market when the guide is exhausted (Acocella, Caplice & Sheffi 2020, as read in SCE7 §3) [practice]. A **tender** is the offer of one load to one carrier.
8. **Carry and track.** The carrier moves the goods; visibility systems report where they are. Gartner counts supply chain visibility systems as execution software (glossary, section 1) [analyst].
9. **Deliver.** The goods reach the customer or store, and a document confirms the hand-over (region note below).
10. **Settle.** Money moves: the customer is invoiced, the carrier is paid. On the inbound side, Bartholdi and Hackman note that the receipt the WMS records is what "drives the paying of bills to suppliers upstream" (§4.1) [practice]. SCE7 §6 sources the carrier's side for the US: under 49 CFR Part 377 (2009 edition) a motor carrier extending credit presents its freight bill within 7 days and the default credit period is 15 days, a tariff allowing no more than 30 calendar days; Gartner's TMS definition places the check of the invoice against the expected charge in the transport system [analyst]. No European rule was opened.
11. **Return.** Goods come back. Gartner lists returns among the typical modules of warehouse software (glossary) [analyst].

Two inbound steps, which SCE2 takes, feed every promise: **receiving** (goods arrive and are recorded) and **put-away** (goods are moved to a storage location the system knows). Bartholdi and Hackman's rule is that product should be "scanned at all key decision points" so that the record keeps up with the goods (ch. 3 introduction) [practice]. A promise made from stock the record shows and the shelf does not is the failure Corvane (fictional) already has: web orders promised from stock the centre cannot find (case register). SCE4 traces how records go wrong.

```viz
{"kind": "flow", "title": "One order, promise to delivery", "steps": [{"label": "Take the order"}, {"label": "Promise", "note": "available-to-promise"}, {"label": "Source", "note": "which location ships"}, {"label": "Release", "note": "orders to pick lists"}, {"label": "Pick"}, {"label": "Pack and ship"}, {"label": "Plan and tender", "note": "routing guide"}, {"label": "Carry and track"}, {"label": "Deliver"}, {"label": "Settle"}, {"label": "Return"}], "caption": "The eleven order-to-return steps of the execution map in section 2 of this unit, in order (the inbound steps are described in the text, not drawn). Step names are this course's; the notes come from the sources cited in section 2: Gartner's DOM definition (Peer Insights, read 21 Nov 2026), Bartholdi and Hackman, Warehouse & Distribution Science, release 0.98 (2017), ch. 4, and Acocella, Caplice and Sheffi (2020), as read in SCE7 §3."}
```

**Region note.** The document that confirms a road shipment differs by region. For international carriage of goods by road in vehicles for reward, the CMR Convention, done at Geneva on 19 May 1956, requires the contract of carriage to be confirmed by a consignment note made out in three original copies signed by sender and carrier, though the note's absence, irregularity or loss does not affect the contract's existence or validity (Arts. 4 and 5(1)) ([United Nations, CMR Convention, UN Treaty Collection text](https://treaties.un.org/doc/Treaties/1961/07/19610702%2001-56%20AM/Ch_XI_B_11.pdf)) [independent]. In the United States, the Federal Acquisition Regulation, which governs the federal government's own purchasing (this unit opened no source for the commercial definition), defines the **bill of lading** as a transportation document used as a receipt of goods, as documentary evidence of title, for clearing customs, and generally as a contract of carriage ([FAR 47.001, effective 13 Mar 2026](https://www.acquisition.gov/index%2Ephp/far/47.001)) [independent]. Which countries are party to the Convention is listed in the UN Treaty Collection; this unit did not check the list, so it does not say which European countries apply it. Which document a given shipment needs, and what it obliges anyone to do, is a legal question: put it to the operation's transport or legal team, or to the national body that administers the convention.

## 3. What each system holds as its own

A product team's most useful question about any system is which facts it is the **system of record** for: the one place whose copy wins when two copies disagree. SCE10 builds the full system-of-record table; this section gives the map-level version.

| System | What it holds as its own | Steps it runs | Basis and grade |
|---|---|---|---|
| **Order management system** (OMS; Gartner's term is distributed order management, DOM) | The customer order, its promise and its status across the network | Take the order, promise, source; tracks status through the chain | Gartner DOM definition [analyst] |
| **Warehouse management system** (WMS) | Every item in the building, every storage location and its address, every customer order's pick lists and their progress | Release, receive, put away, store, count, pick, pack, ship; returns as a module | Gartner WMS definition [analyst]; Bartholdi & Hackman ch. 4 [practice] |
| **Transportation management system** (TMS) | Carrier sourcing, the shipment plan (consolidation, mode, route, carrier), carrier communications, tracking events, and the expected charge settlement checks invoices against | Plan and tender, carry and track; the check of the carrier's invoice | Gartner TMS market definition, Peer Insights, features updated April 2026 [analyst] (SCE7 §5); tendering is not named in the definition, and paying the carrier is not in it |
| **Enterprise resource planning** (ERP) | Working placement only: the financial record (invoices, supplier bills, the general ledger), the item master, purchase and sales orders as accounting documents | Settle | No source opened in this unit for ERP's scope; the WMS receipt that triggers supplier payment is Bartholdi & Hackman §4.1 [practice] |

The WMS row rests on two sources. Gartner defines a WMS as software that helps manage and execute the operations of a warehouse, distribution centre (DC) or fulfilment centre (FC), with core capabilities to receive, put away, store, count, pick, pack and ship goods, built on mobile devices with bar codes and potentially RFID (radio-frequency identification tags) as its transactional foundation ([Gartner Peer Insights, "Warehouse Management Systems Reviews and Ratings", definition, updated May 2026, read 21 Nov 2026](https://www.gartner.com/reviews/market/warehouse-management-systems?months=12)) [analyst]. Bartholdi and Hackman write that a typical WMS knows about every item in the warehouse and all its storage locations and their addresses, receives customer orders and turns them into pick lists, and tracks the assembly of each order (ch. 4 introduction) [practice].

Where the ERP stops is the boundary you will argue about most, and this unit leaves it as a working placement because no ERP definition could be opened (Gartner's glossary page refused the fetch; see the source log). Two sourced points mark it. First, warehouse transactions feed the ERP's money: a receipt pays a supplier (Bartholdi & Hackman §4.1) [practice]. Second, the WMS sends summary data upward to a larger supply chain system, while it handles the item-by-item detail itself (ch. 4 introduction) [practice]. The fictional vendors show the two ways the boundary is sold: Varnby Software (fictional) sells warehouse and transport as modules of its ERP and says of itself "No integration to build"; Halvern Systems (fictional) sells order, warehouse and transport systems and nothing else, and says "One vendor for execution" (case register). Each line is evidence of what the vendor claims; SCE10 and SCE16 set the claims against evidence.

```viz
{"kind": "matrix", "title": "Which system runs which step", "cols": ["Promise", "Source", "Release", "Receive, store", "Pick, pack, ship", "Tender", "Track", "Settle", "Return"], "rows": [{"label": "Order system (DOM)", "tone": 3, "cells": ["holds", "holds", null, null, null, null, "status", null, null]}, {"label": "Warehouse system (WMS)", "tone": 2, "cells": [null, null, "holds", "holds", "holds", null, null, "receipt", "module"]}, {"label": "Transport system (TMS)", "tone": 4, "cells": [null, null, null, null, null, "working", "holds", "check", null]}, {"label": "ERP", "tone": 1, "cells": [null, null, null, null, null, null, null, "working", null]}], "legend": [{"mark": "holds", "means": "a source cited in section 3 places the step in this system"}, {"mark": "status", "means": "tracks order status (Gartner DOM definition)"}, {"mark": "receipt", "means": "the WMS receipt triggers supplier payment (Bartholdi and Hackman, 4.1)"}, {"mark": "module", "means": "listed as a typical module (Gartner SCE glossary)"}, {"mark": "check", "means": "matches expected charges against actual (Gartner TMS definition, April 2026)"}, {"mark": "working", "means": "this course's working placement, not yet sourced"}], "caption": "The map-level system-of-record placements of section 3 of this unit. Sources: Gartner's DOM and WMS market definitions (Peer Insights, read 21 Nov 2026), Gartner's TMS market definition (Peer Insights, features updated April 2026, opened by SCE7 on 24 Nov 2026), Gartner's SCE glossary entry (read 21 Nov 2026) and Bartholdi and Hackman, Warehouse & Distribution Science, release 0.98 (2017), ch. 4. Cells marked working are not sourced in this unit."}
```

## 4. The neighbouring systems

You will hear five more names. Gartner's glossary treats several of them as typical modules of warehouse software: labour management, yard and dock management, returns and inventory control ([Gartner, SCE glossary](https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/supply-chain-execution-sce)) [analyst]. Whether one is sold as a separate system or as a module is the vendor's packaging choice: Halvern Warehouse (fictional) lists Labour, Voice, Yard, Slotting, Automation Connect and Client Billing modules, and Kestrow WMS (fictional) lists only Mobile, Parcel Shipping and Returns (case register).

- **Labour management.** Measures and plans the work of people in the building. Gartner counts managing labour among extended WMS capabilities (WMS definition) [analyst]; Bartholdi and Hackman list labour management among the features of high-end WMS products and note that a WMS tracks worker productivity (ch. 4) [practice]. SCE5 treats the floor.
- **Yard management.** Manages trailers and dock doors outside the building. Bartholdi and Hackman note that a WMS may talk to a yard management system (ch. 4 introduction) [practice]; Gartner lists yard and dock management as a warehouse module (glossary) [analyst].
- **Warehouse control system (WCS) and warehouse execution system (WES).** Software between the WMS and automated equipment such as conveyors and sorters. This unit opened no acceptable source defining either term (the one page found was an unsigned blog, set aside in the source log), so it places them on the map below the WMS, next to the machines. SCE5 §7 gives an analyst's definitions: a WCS controls "the flow of goods across fixed automation", a WES orchestrates "the timing and location of warehouse workflows", and most embedded WES sit in the WMS (Scriven, Interact Analysis, 22 Feb 2023) [analyst]. No peer-reviewed or standards-body definition was found.
- **Visibility tools.** Report where shipments and goods are. Gartner counts visibility systems as execution software (glossary) [analyst]. Whether any tool shows the whole chain is common claim C11, tested in SCE8.
- **Global trade management (GTM).** Handles trade compliance and international logistics; Gartner lists it beside WMS and TMS (glossary) [analyst]. This course does not treat it further.

## 5. Who runs these operations

Four kinds of company run warehouses and freight. They differ in what they ship, to whom, and who pays for the operation. Bartholdi and Hackman's types of warehouse give the warehouse side (§1.2) [practice]:

- **Retailers.** A retail distribution centre supplies product to stores, and a typical store order "might comprise hundreds or thousands of items" (§1.2, p. 8) [practice]; an e-commerce centre receives small orders from individuals (p. 9) [practice]. Corvane (fictional) runs both flows from one building: store replenishment by carton and single item, and web orders of one to three items (case register).
- **Manufacturers.** Ship their own products to customers, often through warehouses tied to the ERP that runs production. This unit opened no source describing manufacturers' warehouses as a type; Varnby Software (fictional) names manufacturers and wholesalers already on its ERP as its customers (case register), which is the claim the course will test in SCE16 and SCE17.
- **Wholesalers and distributors.** Buy from producers and sell to businesses. Ostrel Foods (fictional), a food distributor, delivers chilled, frozen and ambient goods to about 600 delivery points a day with its own 40 vehicles (case register). Bartholdi and Hackman describe perishables warehouses as distinctive in that product dwells within for very short times, frequently only hours (§1.2, p. 9) [practice].
- **Logistics providers.** Run warehouses or arrange freight for other companies. Bartholdi and Hackman: "The 3PL provider might service multiple customers from one facility" (§1.2, p. 9) [practice]; a **third-party logistics provider** (3PL) is the company to which another outsources warehousing. Gartner evaluates third-party logistics providers as a market of their own, a separate Magic Quadrant last updated 5 March 2026 (index, read 21 Nov 2026) [analyst]. Tandric Logistics (fictional) runs one warehouse for nine clients and is paid per activity for warehousing, and its invoices are disputed when activity was not recorded (case register). DD-SCE1 develops this.

At map level the difference that matters is **who the software's customer is**. A retailer, manufacturer or distributor buys execution software to run its own goods; a logistics provider buys it to run other companies' goods, and at Tandric (fictional) each client brings its own rules and reports (case register); this unit opened no source on whether that holds for logistics providers generally.

## 6. How analysts describe the market

This unit names analyst categories only. It lists no vendor from any of them and maps no product.

On 21 November 2026, Gartner's index of Magic Quadrants and Critical Capabilities listed these categories that touch this course, with the last-updated dates the index gave ([Gartner index](https://www.gartner.com/magic-quadrant)) [analyst]:

| Category (Gartner's name) | Magic Quadrant last updated | Next refresh shown |
|---|---|---|
| Warehouse Management Systems | 29 Apr 2026 | 30 Apr 2027 |
| Transportation Management Systems | 30 Mar 2026 | 22 Apr 2027 |
| Distributed Order Management | none shown | 23 Nov 2026 |
| Supply Chain Management Suites | 11 Aug 2026 | 11 Aug 2027 |
| Supply Chain Planning Solutions (three industry variants) | 18 Mar 2026 (two variants) | 7 Apr 2027 |
| Third-Party Logistics | 5 Mar 2026 | 20 Jan 2027 |
| Global Trade Compliance Solutions | none shown | 30 Nov 2026 |
| Cloud ERP for Product-Centric Enterprises | 13 Oct 2025 | 2 Nov 2026 |

The index and the report disagree on one date: Gartner's own abstract page for the Distributed Order Management Magic Quadrant is dated 12 November 2026 ([Gartner, abstract](https://www.gartner.com/en/documents/8617033)) [analyst], while the index read nine days later still showed no last-updated date for it. Its Peer Insights market page carries the heading "Transitioning to Distributed Order Management" (DOM page, read 21 Nov 2026). Date every analyst fact you use, and give the date of the page you read it on.

Three things follow for reading the field. A category is the analyst's choice of boundary, and the boundaries move: order management is outside Gartner's execution glossary yet has its own Magic Quadrant. A product can sit in more than one category, as a suite does. And the categories describe software sold, not operations run, so a reader still has to place each category on the map of section 2.

## 7. The kinds of evidence and what each can show

| Kind | What it can show | What it cannot show | Grade |
|---|---|---|---|
| Peer-reviewed operations research | A finding with its design, sample and setting stated, checked by reviewers | That the finding holds at another site or in another industry; a correlation does not show cause | independent |
| Industry association survey | What a stated sample of respondents reports, in a stated year | Anything about operations outside the sample; anything when no sample is stated | independent if the sample is stated; otherwise practice (section 10) |
| Audited company filing | That company's own figures (revenue, costs, customers it discloses) | Anything about competitors or the market beyond the filer | independent, for the filer's own figures |
| Standard, treaty or regulation | What the text itself requires or defines | How the rule is applied in practice | independent, for what the text says |
| Analyst report | The firm's assessment of a market and its vendors at a date, by its own method | What a product does on your floor; the full report is usually paid for | analyst |
| Vendor material | What the vendor claims | What the product does | vendor-reported |
| Peer-review site | What reviewers of a stated count say | How a product performs; the reviewer sample may be vendor-invited | vendor-reported |
| Textbook or practitioner account | How the work is commonly done | Any rate or share, unless it reports a measurement | practice |

Two examples show the limits. The 2026 MHI Annual Industry Report, *Rewiring the Future: A Supply Chain Playbook for Innovation*, prepared with Deloitte, was announced as "based on a survey of supply chain leaders", and the announcement gives no sample size, roles or regions ([MHI Solutions magazine, 26 Jun 2026](https://www.mhisolutionsmag.com/index.php/2026/06/26/new-mhi-and-deloitte-report-finds-ai-is-biggest-disruptor-of-supply-chains-over-the-next-decade/)). Under this course's key, a figure from that announcement is graded practice until the report's sample is read. Its headline finding concerns artificial intelligence, which this course does not treat.

On peer-review sites, Gartner's Peer Insights lets vendors invite their own customers to review, through a custom link; Gartner says it does not endorse incentives, asks that any be nominal (under $25) and offered to all invited customers, and itself gives the first 50 approved reviews a $25 gift card ([Gartner Peer Insights, "Review Sourcing", read 21 Nov 2026](https://blogs.gartner.com/reviews-pages/tpt-faq/review-sourcing/)) [analyst]. Because a vendor can choose whom to invite, this course grades what reviewers say as vendor-reported. The course also cites a review market only with its count of reviews; the warehouse market page read on 21 November 2026 listed 140 products and showed no total review count (WMS page) [analyst], so no count can be given here.

## 8. How an analyst evaluation is made and paid for

**Gartner.** Gartner's research-methodology page for the Magic Quadrant refused the fetch on 21 November 2026, so the quadrant itself is covered only in part: this unit does not describe Gartner's evaluation criteria beyond the two measures and four quadrants named below, or its reprint terms, and uses Forrester's Wave, a different evaluation whose method could be read in full, for the steps. Gartner's FAQ on the Magic Quadrant, served at a gartner.com subdomain, names the two measures a vendor is placed on, Ability to Execute and Completeness of Vision, and four quadrants, Leaders, Challengers, Visionaries and Niche Players; the page gives no date and does not mention reprints ([Gartner, "FAQ: How Markets and Vendors Are Evaluated in Gartner Magic Quadrants", read 21 Nov 2026](https://gcom.pdo.aws.gartner.com/en/about/magic-quadrant-faq)) [analyst]. What could be read:

- Gartner's methodology note describes Magic Quadrants as visual snapshots, in-depth analyses and actionable advice on a market's direction, maturity and participants, recommends reading the note together with a Magic Quadrant and its companion Critical Capabilities report, and advises using it to narrow a list of providers: "don't base your decision on this evaluation only" ([Gartner, "How Markets and Vendors Are Evaluated in Gartner Magic Quadrants", 19 Mar 2024, abstract read](https://www.gartner.com/en/documents/5292963)) [analyst].
- Gartner's Office of the Ombuds states that inclusion is determined solely by whether a vendor meets the inclusion criteria, that evaluated vendors may be clients or not, that analysts do not discuss specific scores or methodology with vendors, and that "Client status never influences the outcome or inclusion in our evaluative research" ([Gartner, "How Gartner Experts Work With Vendors", 30 Jun 2025](https://www.gartner.com/en/about/ombuds/news/how-gartner-experts-work-with-vendors)) [analyst].
- On money, Gartner states that technology providers buy its services and exhibit space at its conferences, that "the vast majority of our revenue comes from end users of technology", and that it has guidelines to prevent implied endorsement when its research is republished or quoted; the page does not give the terms ([Gartner, "Independence and Objectivity", read 21 Nov 2026](https://www.gartner.com/en/research/methodologies/independence-and-objectivity)) [analyst].

**Forrester**, whose method page could be read in full, shows the steps such an evaluation goes through ([Forrester, "The Forrester Wave Methodology", last modified 28 Apr 2026](https://www.forrester.com/marketing/policies/forrester-wave-methodology.html)) [analyst]:

1. The analyst sets the inclusion criteria that decide which vendors are evaluated.
2. The analyst drafts evaluation criteria at kickoff, puts them in the vendor questionnaire, and weights them at scoring; Forrester intends these criteria to be differentiating, rather than exhaustive.
3. Vendors supply three inputs: a questionnaire, a strategy and product demo session, and reference customers, whom Forrester interviews or surveys.
4. Analysts score each criterion against a written scale; vendors that gave all inputs may comment on their scores and profile before the scorecard is final; a courtesy preview goes out about five days before publication, when no new information is accepted.
5. Forrester may evaluate vendors that do not take part, and notes participation in the report.
6. The graphic places vendors in three bands, Leader, Strong Performer and Contender; for Waves begun on or after 1 July 2024 and publishing in the fourth quarter of 2024, customer feedback replaced market presence on the graphic.

Forrester's citation rules show how the report reaches you. A company must be a Forrester subscriber or buy reprint rights to cite a Wave, and must have bought reprint rights to post it on its website; it may not cite its physical placement on the graphic; and a slide showing the graphic to a live audience must carry, legibly, the disclaimer "Forrester does not endorse any company, product, or service depicted in the Forrester Wave" ([Forrester, "Forrester Wave Citation Guidelines"](https://www.forrester.com/staticassets/marketing/about/Forrester_Wave_Citation_Guidelines.pdf)) [analyst]. Gartner's reprint terms could not be read (its content compliance page refused the fetch), so the course's working assumption, from the course brief, is that vendors license the reprints you find on their sites; SCE17 checks it.

What this means for you, as this unit's inference: a Forrester Wave read on a vendor's website is a copy the vendor bought reprint rights for and chose to post (for Gartner, the course's working assumption until SCE17 checks it), so you read the full report and the date, and note which vendors the same report covers on equal terms. When only the abstract is open to you, you state only what the abstract states.

## 9. How to read a vendor case study

A vendor case study is graded vendor-reported, whatever numbers it carries: it is evidence of what the vendor and its customer agreed to publish. The questions below follow from the grade key (section 10) and are this unit's own; no source was opened that tests them.

- **Who measured, and how?** A number with no stated measure, period or baseline cannot be checked. A before-and-after figure needs the before period, the after period, and what else changed in between (new building, new staff, new season).
- **Is the customer named and dated?** An unnamed customer cannot be followed up; a dated one can be checked against later public statements.
- **Who chose the story?** The vendor picks which customers to feature. Gartner's own review rules recognise the same selection problem when they ask vendors to offer any incentive to all invited customers, and not only satisfied ones (section 7) [analyst].
- **What would transfer?** A result at one site is the unit's inference if applied to another: a retailer's result says nothing about a food distributor's night shift until a source shows it does.

Worked on the case register: Kestrow (fictional) says of itself "Live in weeks". Graded vendor-reported, the line is evidence that Kestrow claims short go-lives. It says nothing about how long Tandric's (fictional) slipped go-live would have taken with Kestrow WMS (fictional).

## 10. The four grades

The key below is designed so that two readers given the same source and claim reach the same grade. It grades by the **origin** of a claim, decided by four questions asked in order; the first "yes" decides.

1. **Did a vendor write it, sponsor it, or choose who answered?** Yes: **vendor-reported**. This covers a vendor's pages, releases, documentation, case studies and sponsored surveys, and peer-review content where vendors can invite reviewers.
2. **Is it published by a named analyst firm?** Yes: **analyst**. This covers reports, their abstracts, and the firm's own definitions and glossaries. Give the firm, the title, the date, how it was read (in full, in a reprint, in abstract) and the note that vendors license reprints.
3. **Is it the source's own finding, in peer-reviewed research, an industry association survey that states its sample, an audited filing (for the filer's own figures), or the text of a standard, treaty or regulation (for what it says)?** Yes: **independent**. If the source repeats a number from another work, grade the origin; if the origin cannot be opened, grade the claim practice and say the origin was not traced.
4. **Otherwise: practice.** A textbook's or practitioner's account of how the work is done, a figure with no measurement behind it in the text read, and an association figure whose sample is not stated.

One claim carries one grade. A sentence that rests on two sources of different grades is split, or carries the grade of the source that holds its number.

```viz
{"kind": "decision", "title": "Grading a claim", "root": {"q": "Did a vendor write it, sponsor it or choose who answered?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "vendor-reported", "tone": 4}}, {"label": "no", "to": {"q": "Published by a named analyst firm?", "tone": 3, "branches": [{"label": "yes", "to": {"outcome": "analyst", "tone": 3}}, {"label": "no", "to": {"q": "Own finding: peer-reviewed, survey with sample, audited filing, or standard's text?", "tone": 2, "branches": [{"label": "yes", "to": {"outcome": "independent", "tone": 2}}, {"label": "repeats a number", "to": {"outcome": "grade the origin; untraced is practice", "tone": 5}}, {"label": "no", "to": {"outcome": "practice", "tone": 1}}]}}]}}]}, "caption": "The grade key of section 10 of this unit, as a decision: the first yes decides. The rule is this course's own; its categories follow the course brief's four grades."}
```

## 11. The common claims, set against their evidence

The course keeps a list of claims that circulate in the industry. Each is stated here as it circulates; the right-hand column says what this unit opened, and which unit tests it. "Not searched here" means this unit did not look and makes no finding.

| # | Claim as it circulates | What this unit found | Tested in |
|---|---|---|---|
| C1 | Travel is about half of an order picker's time. | Bartholdi and Hackman give travel as 55% of order-picking time and credit it to Frazelle's *World-Class Warehousing* (1996) (§3.3) [practice]. De Koster et al. write that travel "is often the dominant component" and reproduce a chart of a picker's time from Tompkins et al. (2003), a textbook ([2007, §2.3](https://doi.org/10.1016/j.ejor.2006.07.009)) [practice]. Both trace to textbooks; no measurement study was opened, and no independent source found. | SCE3 |
| C2 | Order picking is more than half of a warehouse's operating cost. | De Koster et al.'s abstract says picking cost is "estimated to be as much as 55% of the total warehouse operating expense", with no source in the abstract [practice]; Bartholdi and Hackman say it "typically accounts for about 55%", crediting Frazelle (1996) (§3.3) [practice]. "As much as" is an upper bound, which the circulating version drops. No independent source found. | SCE3 |
| C3 | Labour is the largest cost in a warehouse. | Tested in SCE5 §8: in US Census Service Annual Survey data for 2012, gross annual payroll was about a third of warehousing firms' total expense ($7,975 million of $23,883 million) [independent]; employers' benefit costs, a separate line, were $1,895 million, so payroll with benefits was about 41% (this unit's arithmetic); of the other lines, only "all other operating expenses" ($4,388 million) was opened; the remaining $9,625 million was not, so "largest" is not shown. No independent source found that ranks labour against every other cost. | SCE5 |
| C4 | Good sites run at 99.9% inventory accuracy. | Tested in SCE4 §10: no independent source opened there reports the share of warehouse records that match the shelf, at 99.9% or any other level; the one distribution-centre study (Kull et al. 2013, read in full in the author's version) measures inaccuracy as a percentage of each SKU's on-hand stock instead [independent]. A 2025 vendor infographic presenting WERC's 2025 report gives best in class for count accuracy by location as at or above 99.5%, no sample stated [vendor-reported]. Store studies found 31% to 65% of records wrong, on different definitions [independent]. | SCE4 |
| C5 | Voice picking brings accuracy to 99.9% or raises productivity by a fixed percentage. | Tested in SCE5 §3: one field experiment (101 participants) found pick by voice performing better than RF-terminal picking, with no percentage in its abstract ([de Vries, de Koster & Stam, 2016, IJPR, abstract](https://doi.org/10.1080/00207543.2015.1064184)) [independent]; no source opened gives 99.9%. No independent source found for either number. | SCE5 |
| C6 | Gamification raises warehouse productivity by a stated percentage. | Tested in SCE5 §§4–5: the one percentage opened ("up to 7%") is a vendor's, with no basis given [vendor-reported]; independent work is exploratory (eight UK warehouse managers interviewed; 17 pickers surveyed) [independent]. A related controlled field experiment found that competition-based incentives raised productivity in parallel picking and cooperation-based ones in zone picking ([de Vries, de Koster & Stam, 2016, abstract](https://doi.org/10.1111/poms.12547)) [independent]; its abstract reports no effect on quality, while the 2015 working paper reported error rates that differed by condition (SCE5 §4). It does not test gamification. No independent source found for a productivity percentage. | SCE5 |
| C7 | Most warehouse or ERP system implementations fail or overrun. | Not searched here. | SCE14 |
| C8 | Cloud software means no more upgrades. | Tested in SCE6 §10: no source opened says upgrades end in the cloud. NIST's definition of SaaS (SP 800-145, 2011) leaves the customer no control of the underlying infrastructure or of individual application capabilities, apart from limited user-specific application configuration settings [independent], so the upgrade moves to the provider (inference); Gartner's 2022 WMS Magic Quadrant, read in a reprint, says service affects "upgrade cycles and TCO", calls multitenant against dedicated cloud a continuing debate, and says some vendors' microservices architecture "allows continuous upgrades" [analyst]; an ERP review finds SaaS often limits deep customisation and that customisation has shifted to interfaces and integrations (Abendroth et al. 2024) [independent], and Light (2001, abstract only) found that a customisation needs careful consideration for its potential impact on future maintenance [independent]. No independent source found for the claim. | SCE6 |
| C9 | One platform from one vendor lowers total cost. | Not searched here. The case register's Halvern Systems (fictional) and Varnby Software (fictional) state versions of it (section 3). | SCE10, SCE16 |
| C10 | The vendor in the Leaders quadrant is the best choice. | The analyst firms do not make the claim. Gartner advises using a Magic Quadrant to narrow a list, and "don't base your decision on this evaluation only" (2024 note, abstract) [analyst]; Forrester's required disclaimer says it does not endorse any company in a Wave [analyst]. No independent source was found, in this unit's searches, that tests whether buyers who chose a Leader fared better. | SCE17 |
| C11 | A control tower gives end-to-end visibility. | Not searched here. Gartner counts visibility systems as execution software (glossary) [analyst]; that says nothing about reach. | SCE8 |
| C12 | A stated share of truck miles is driven empty. | Not searched here. | SCE7 |
| C13 | Buyers decide on the demonstration. | Not searched here. | SCE12 |
| C14 | Users will work around any system they dislike. | Not searched here. | SCE13 |

## On a site visit

SCE1 is not an operations unit, so its visit is to colleagues in sales, services and product. Ask:

- **Which of the map's steps does our product hold as its own record, and which does it only display?** The answer places the product on the map (sections 2 and 3).
- **Which analyst categories list our product, under which names, and with what report date?** Then ask whether the team read each report in full, in a licensed reprint, or in abstract (sections 6 and 8).
- **Where does our product hand off to the ERP, and which system's record wins at settlement?** (Section 3.)
- **Are labour, yard, automation control and returns separate products or modules of ours, and which do customers buy from someone else?** (Section 4.)
- **When we quote a customer result, who measured it, over what period, against what baseline?** (Section 9.)
- **Which kind of company is each of our main customers: retailer, manufacturer, distributor or logistics provider?** A logistics provider runs other companies' goods; Tandric (fictional) bills its clients per activity, which changes what it needs from the record (section 5).

## Self-check

1. **Gartner's glossary entry on supply chain execution names which systems, and what does it say about order management?**
   Warehouse, transport and global trade management systems, with real-time decision support and visibility systems; order management is sometimes included, and Gartner generally excludes it (section 1).
2. **What does Gartner's DOM definition say the order system uses inventory for?**
   For both available-to-promise and available-to-ship, while orchestrating fulfilment across the network by hierarchical business rules and tracking order status (sections 2 and 3).
3. **A colleague says picking is "more than half" of warehouse cost. What do the sources opened here say?**
   De Koster et al.'s abstract says it is estimated to be as much as 55%, with no source in the abstract; Bartholdi and Hackman say about 55%, crediting a 1996 textbook. Both are practice by origin, and "as much as" is an upper bound (section 11, C2).
4. **What does a routing guide hold?**
   For each lane, the primary carrier and backups in order with their contract prices; the spot market is used when the guide is exhausted (section 2; SCE7 §3).
5. **Name the map's steps in order and say which system holds the record at each.**
   Take the order, promise and source (order system); release, receive and put away, pick, and pack and ship (warehouse system); plan and tender, and carry and track (transport system: Gartner's TMS definition places planning and tracking there; tendering is a working placement); deliver (section 3 places it in no system); settle (the check of the carrier's invoice in the transport system, on Gartner's TMS definition; payment in the ERP, a working placement); return (a typical warehouse module in Gartner's glossary) (sections 2 and 3; deliverable A).
6. **What are the three inputs Forrester takes from a vendor in a Wave, and what may a vendor not cite?**
   A questionnaire, a strategy and product demo session, and reference customers; a vendor may not cite its physical placement on the graphic (section 8).
7. **A survey announcement gives a percentage but no sample. What grade does it get, and why?**
   Practice, because the key grades an association figure independent only when its sample is stated (sections 7 and 10).
8. **Why does this course grade peer-review site content vendor-reported?**
   Because vendors can invite their own customers to review, as Gartner's review-sourcing rules state (section 7).

## Deliverable

### A. Corvane's execution map (fictional)

Corvane (fictional): one 28,000 m² distribution centre, 60 stores in four European countries, one website; about 18,000 items counted by size and colour; peak from mid-November to early January with web volume about four times a normal week (case register). Systems: an ERP, a warehouse system about twelve years old on its own servers and near the end of its vendor's support, an order system for the website, and carriers booked through each carrier's own portal (case register). Owners are named only where the case register's roles make the owner plain; cells the register does not fill say so.

| # | Step | Physical event | System at Corvane | Owner | Known trouble (case register) |
|---|---|---|---|---|---|
| 1 | Take the order | A web customer orders one to three items; a store needs replenishment | Order system for the website (web); not in the register for store orders | Not in the register | none recorded |
| 2 | Promise | The website tells the customer the item is available | Order system for the website | Not in the register | Web orders promised from stock the centre cannot find |
| 3 | Source | The order is assigned to the centre or to a store | Order system for the website | Store fulfilment: Freya, store associate | Store staff asked to ship web orders with no process for it |
| 4 | Release | Orders become pick work for the shift | Warehouse system | Tobias, outbound shift supervisor | none recorded |
| 5 | Receive and put away | Supplier goods arrive and go to locations | Warehouse system | Carla, inventory controller, for the stock record | Stock the record shows and the shelf does not (this unit's reading of the step 2 trouble) |
| 6 | Pick | An operator takes the items from their location | Warehouse system | Mina, operator, web picking | Same as step 2 at the shelf (this unit's reading) |
| 7 | Pack and ship | Items are checked, packed, loaded by carton or single item | Warehouse system | Tobias, outbound shift supervisor | none recorded |
| 8 | Plan and tender | A carrier is booked for each shipment | Each carrier's own portal; no transport system | Not in the register | none recorded |
| 9 | Carry and track | The carrier moves the goods; status is checked | Not in the register (carriers are booked through each carrier's own portal) | Jonas, customer service, answers the customer | none recorded |
| 10 | Deliver | Goods reach the customer or the store | Carrier | Carrier | none recorded |
| 11 | Settle | Customer and carrier money moves | ERP (working placement) | Helene, chief financial officer, for the financial record | none recorded |
| 12 | Return | Web and store returns come back | Not in the register | Not in the register | none recorded |

Site and decision owners across the map: Marek, site manager of the centre; Ravi, IT director, for the systems; Edda, vice-president supply chain, who sponsors the replacement; the decision is whether to replace the warehouse system and whether to buy order and transport systems from the same vendor (case register). On the map, the decision covers steps 1 to 9 and 12, and the open question for SCE10 is which system will hold steps 2, 3 and 8.

### B. Working glossary

Later units extend this list; each term is defined as this unit uses it, with its source where one was opened.

| Term | Working definition | Source |
|---|---|---|
| Supply chain execution (SCE) | Software and work that carry out particular orders, shipments and tasks and record what physically happened | Gartner SCE glossary [analyst]; course line (section 1) |
| Supply chain planning | Deciding quantities, places and times ahead of the work | Course line (section 1); Meyr et al. [practice] |
| Order management system (OMS); distributed order management (DOM) | Software that takes orders, promises them, chooses the shipping location by rules and tracks order status | Gartner DOM definition [analyst] |
| Available-to-promise (ATP) | The quantity that can still be committed to new orders | Named in Gartner DOM definition [analyst]; definition is the course's |
| Available-to-ship | The quantity that can leave now | Named in Gartner DOM definition [analyst]; definition is the course's |
| Warehouse management system (WMS) | Software that runs receiving, put-away, storage, counting, picking, packing and shipping in a building, item by item and location by location | Gartner WMS definition [analyst]; Bartholdi & Hackman ch. 4 [practice] |
| Transportation management system (TMS) | Software for multimodal sourcing, planning and execution of transport, with visibility, settlement and analytics | Gartner TMS market definition, April 2026 [analyst] (SCE7 §5) |
| Enterprise resource planning (ERP) | The company's financial and master-data system | Working definition; not sourced in this unit |
| System of record | The one system whose copy of a fact wins when copies disagree | Course term |
| Distribution centre (DC); fulfilment centre (FC) | A warehouse that ships to stores or businesses (DC) or to consumers (FC) | Gartner WMS definition names both [analyst]; the distinction is the course's |
| Receiving | Recording goods that arrive | Bartholdi & Hackman ch. 3 [practice] |
| Put-away | Moving received goods to a known storage location | Bartholdi & Hackman ch. 3 [practice] |
| Order picking | Taking ordered goods from storage | de Koster et al. §2.1 [practice] |
| Cross-docking | Moving goods from receiving to shipping without storing them | Named in de Koster et al. §2.1 [practice]; definition is the course's |
| Sortation | Grouping picked goods by order or destination | Named in de Koster et al. §2.1 [practice]; definition is the course's |
| Labour management | Measuring and planning the work of people in the building | Gartner WMS definition and SCE glossary [analyst]; Bartholdi & Hackman ch. 4 [practice] |
| Yard management | Managing trailers and dock doors outside the building | Gartner SCE glossary [analyst]; Bartholdi & Hackman ch. 4 [practice] |
| Warehouse control system (WCS); warehouse execution system (WES) | WCS: software that controls the flow of goods across fixed automation. WES: software that controls the timing and location of warehouse workflows; most embedded WES sit in the WMS | Scriven, Interact Analysis, 2023 [analyst], as read in SCE5 §7 |
| Visibility tool | Software that reports where shipments and goods are | Gartner SCE glossary [analyst] |
| Global trade management (GTM) | Software for trade compliance and international logistics | Gartner SCE glossary [analyst] |
| Carrier | The company that moves the goods | Course term |
| Shipper | The company whose goods are moved and which buys the carriage | Course term (also SCE7 §1) |
| Routing guide | A shipper's catalogue of carrier assignments, prices and priority for its lanes | Acocella et al. 2020 [practice] (SCE7 §3) |
| Tender | The offer of one load to one carrier, which accepts or rejects it | Acocella, Caplice & Sheffi 2020 [practice] (SCE7 §3) |
| Truckload (TL; FTL in Europe, working term) | A vehicle dedicated to one shipper's shipment from origin to destination | Sheffi 2004 [practice] (SCE7 §2) |
| Consignment note (CMR) | The document confirming an international road carriage contract under the CMR Convention | CMR Arts. 4–5 [independent] |
| Bill of lading | A transport document used as receipt, evidence of title and contract of carriage (US federal definition) | FAR 47.001 [independent] |
| Third-party logistics provider (3PL) | A company that runs warehousing or freight for other companies; textbooks differ on whether it must own the assets (Rodrigue, 6th ed., ch. 7, defines a 3PL as an asset-based company and a 4PL as a non-asset-based provider that mainly provides organisational expertise) [practice] | Bartholdi & Hackman §1.2 [practice] |
| Magic Quadrant; Wave | Gartner's and Forrester's dated evaluations of a software market's vendors | Gartner 2024 note [analyst]; Forrester method [analyst] |
| Reprint | A licensed copy of an analyst report distributed by a vendor | Forrester citation guidelines [analyst] |
| Evidence grade | One of independent, analyst, vendor-reported, practice (part C) | This unit |
| Lane (freight) | A one-way movement from an origin to a destination, with its shipments, that a shipper buys carriage for | Sheffi 2004 [practice] (SCE7 §3) |
| Radio-frequency identification (RFID) | Tags read by radio, used beside bar codes to identify goods | Named in Gartner WMS definition [analyst]; definition is the course's |
| Critical Capabilities | Gartner's companion report to a Magic Quadrant, meant to be read with it | Named as the companion report in Gartner 2024 note, abstract [analyst]; definition is the course's |
| Item master | The record of every item the company stocks or sells | Working definition; not sourced in this unit |
| General ledger | The company's main book of accounts | Working definition; not sourced in this unit |
| Replenishment | Resupplying a store, or a pick location, with stock | Course term; SCE2 sources the pick-location sense |
| Slotting | Assigning each item to a storage location | Course term; SCE2 adds the forward-area sense |
| Go-live | The day a new system starts running the operation | Course term |

### C. The grade key

Ask the questions in order; the first yes decides (section 10).

| Grade | Definition | The test | Worked example |
|---|---|---|---|
| **Independent** | The source's own finding in peer-reviewed research; an industry association survey with its sample stated; an audited filing, for the filer's own figures; the text of a standard, treaty or regulation, for what it says | Not written, sponsored or sample-selected by a vendor; not an analyst firm's; the claim is the source's own, or traced to an origin that is | de Vries, de Koster and Stam (2016) report a controlled field experiment, in a warehouse built for order-picking research, finding parallel picking more productive under competition-based incentives and zone picking under cooperation-based ones, with no effect on quality ([abstract](https://doi.org/10.1111/poms.12547)). Grade: independent. The 2015 working paper reported error rates that differed by condition (SCE5 §4), so "no effect on quality" is the abstract's. The abstract does not state the sample, so the unit says so; applying the result to Corvane's (fictional) web picking is the unit's inference. |
| **Analyst** | Material published by a named analyst firm: a report, its abstract, the firm's definitions | Firm, title, date and how it was read are given, with the note that vendors license reprints | Gartner's *Magic Quadrant for Distributed Order Management*, dated 12 November 2026, read in abstract: "A convergence across B2B and B2C channels is shaping the current market." ([abstract](https://www.gartner.com/en/documents/8617033)). (B2B: sales to businesses; B2C: sales to consumers.) Grade: analyst, abstract only; the unit states nothing about the report beyond the abstract. Vendors license Gartner's reprints (the course's working assumption, section 8), so a copy on a vendor's site is one that vendor chose to post. |
| **Vendor-reported** | Anything a vendor wrote, sponsored or selected the respondents of: pages, releases, documentation, case studies, sponsored surveys, peer reviews it can invite | Dated, and read as evidence of the claim only | Kestrow (fictional) says of itself "Live in weeks" (case register). Grade: vendor-reported; it shows Kestrow claims short go-lives, not how long a go-live takes. |
| **Practice** | A textbook's or practitioner's account of how the work is done with no measurement behind it; a repeated number whose origin is such an account or cannot be traced; a survey figure with no sample stated | None of the above three applies | Bartholdi and Hackman give travel as 55% of order-picking time, crediting Frazelle's 1996 textbook (§3.3). Grade: practice: a textbook figure, with no measurement described in the text read. |

### D. The execution map as a template

Fill one row per step for a real operation or product. Keep the step numbers so later units can refer to them; add a row where the operation has a step the map lacks, and say why. In rows 2 to 12, the System, Owner, Known trouble and Grade blanks take what row 1 describes for each column.

Operation or product: ______ (name; kind of company: retailer, manufacturer, wholesaler or distributor, logistics provider; region) · Date filled: ______ · Sources used: ______ (each with its grade)

| # | Step | Physical event | System that holds the record | Owner | Known trouble | Grade of what you wrote |
|---|---|---|---|---|---|---|
| 1 | Take the order | ______ (what arrives, from whom, through which channel) | ______ (the system whose order record wins) | ______ (the role that answers for the step) | ______ (a failure you saw or a source reports) | ______ (independent, analyst, vendor-reported or practice, by part C) |
| 2 | Promise | ______ (what is promised to the customer, and when) | ______ | ______ | ______ | ______ |
| 3 | Source | ______ (which location ships, chosen how) | ______ | ______ | ______ | ______ |
| 4 | Release | ______ (when orders become floor work) | ______ | ______ | ______ | ______ |
| 5 | Receive and put away | ______ (what arrives, where it goes) | ______ | ______ | ______ | ______ |
| 6 | Pick | ______ (who or what picks, by what method) | ______ | ______ | ______ | ______ |
| 7 | Pack and ship | ______ (checks, packing, loading) | ______ | ______ | ______ | ______ |
| 8 | Plan and tender | ______ (how a carrier is chosen and booked) | ______ (a transport system, a carrier portal, or none) | ______ | ______ | ______ |
| 9 | Carry and track | ______ (who moves the goods, who sees where they are) | ______ | ______ | ______ | ______ |
| 10 | Deliver | ______ (the hand-over and its document: consignment note, bill of lading, other) | ______ | ______ | ______ | ______ |
| 11 | Settle | ______ (who is invoiced, who is paid) | ______ (usually the ERP; confirm) | ______ | ______ | ______ |
| 12 | Return | ______ (what comes back, from where) | ______ | ______ | ______ | ______ |

Below the table: the decision the operation or product team faces (______), the steps it covers (______), and the open question about which system will hold which step (______).

## Sources

All addresses opened on 21 November 2026, except the four entries marked as opened or read by SCE6 and the four marked as opened by SCE7, all on 24 November 2026, whose reading SCE6's and SCE7's source logs record, and the one marked as opened by SCE8 on 27 November 2026, whose reading SCE8's source log records; the source log gives what was read at each of the others.

- Abendroth, A., Bender, B. & Gronau, N. (2024). The Evolution of Original ERP Customization: A Systematic Literature Review of Technical Possibilities. In *Proceedings of the 26th International Conference on Enterprise Information Systems (ICEIS 2024)*, vol. 1, 17–27. https://doi.org/10.5220/0012305500003690 (read at https://scitepress.org/Papers/2024/123055/123055.pdf; opened by SCE6, 24 November 2026)
- Acocella, A., Caplice, C. & Sheffi, Y. (2020). Elephants or goldfish?: An empirical analysis of carrier reciprocity in dynamic freight markets. *Transportation Research Part E: Logistics and Transportation Review* 142, 102073. https://doi.org/10.1016/j.tre.2020.102073 (read in full in the author's copy at https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2021-01/Acocella_Sheffi_Publication%202020.pdf; opened by SCE7, 24 November 2026)
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 1, 3, 4 and bibliography. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- de Koster, R., Le-Duc, T. & Roodbergen, K. J. (2007). Design and control of warehouse order picking: A literature review. *European Journal of Operational Research* 182(2), 481–501. https://doi.org/10.1016/j.ejor.2006.07.009 (read in the version of record at https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf)
- de Vries, J., de Koster, R. & Stam, D. (2015). Aligning order picking methods, incentive systems, and regulatory focus to increase performance. ERIM Report Series ERS-2015-009-LIS. https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf
- de Vries, J., de Koster, R. & Stam, D. (2016). Exploring the role of picker personality in predicting picking performance with pick by voice, pick to light and RF-terminal picking. *International Journal of Production Research* 54(8), 2260–2274. https://doi.org/10.1080/00207543.2015.1064184 (abstract, read at https://research.vu.nl/en/publications/2b68e9a2-c4f6-4c92-93be-9409a9f29a7f)
- de Vries, J., de Koster, R. & Stam, D. (2016). Aligning Order Picking Methods, Incentive Systems, and Regulatory Focus to Increase Performance. *Production and Operations Management* 25(8), 1363–1376. https://doi.org/10.1111/poms.12547 (abstract)
- Forrester. "The Forrester Wave Methodology". Last modified 28 April 2026. https://www.forrester.com/marketing/policies/forrester-wave-methodology.html
- Forrester. "Forrester Wave™ Citation Guidelines". Undated. https://www.forrester.com/staticassets/marketing/about/Forrester_Wave_Citation_Guidelines.pdf
- Gartner. "How Markets and Vendors Are Evaluated in Gartner Magic Quadrants". M. (Reinhart) Flewelling, T. Weaver, D. Black. 19 March 2024 (abstract). https://www.gartner.com/en/documents/5292963
- Gartner. "FAQ: How Markets and Vendors Are Evaluated in Gartner Magic Quadrants". Undated. https://gcom.pdo.aws.gartner.com/en/about/magic-quadrant-faq
- Gartner. "Gartner Magic Quadrant for Distributed Order Management". 12 November 2026 (abstract). https://www.gartner.com/en/documents/8617033
- Gartner. Magic Quadrant and Critical Capabilities index (no headline shown), read 21 November 2026. https://www.gartner.com/magic-quadrant
- Gartner. "Magic Quadrant for Warehouse Management Systems". S. Tunstall, D. Klappich, R. Narang. Published 1 June 2022, ID G00755323. Reprint, read by SCE6 on 24 November 2026. https://dam.infor.com/api/public/content/d8957bc1ac164bf1843965deeaa7e26a?v=d2e94df6
- Gartner. "Supply Chain Execution (SCE)", glossary entry, undated. https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/supply-chain-execution-sce
- Gartner. "Independence and Objectivity", undated. https://www.gartner.com/en/research/methodologies/independence-and-objectivity
- Gartner, Office of the Ombuds. "How Gartner Experts Work With Vendors". 30 June 2025. https://www.gartner.com/en/about/ombuds/news/how-gartner-experts-work-with-vendors
- Gartner Peer Insights. "Distributed Order Management Systems (Transitioning to Distributed Order Management) Reviews and Ratings". Features updated July 2025. https://www.gartner.com/reviews/market/distributed-order-management-systems
- Gartner Peer Insights. "Transportation Management Systems Reviews and Ratings", market definition. Features updated April 2026. https://www.gartner.com/reviews/market/transportation-management-systems (opened by SCE7, 24 November 2026)
- Gartner Peer Insights. "Warehouse Management Systems Reviews and Ratings". Features updated May 2026. https://www.gartner.com/reviews/market/warehouse-management-systems?months=12
- Gartner Peer Insights. "Review Sourcing", undated. https://blogs.gartner.com/reviews-pages/tpt-faq/review-sourcing/
- Light, B. (2001). The maintenance implications of the customization of ERP software. *Journal of Software Maintenance and Evolution: Research and Practice* 13(6), 415–429. https://doi.org/10.1002/smr.240 (abstract, read at https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software; opened by SCE6, 24 November 2026)
- Mell, P. & Grance, T. *The NIST Definition of Cloud Computing*. NIST Special Publication 800-145, September 2011. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf (opened by SCE6, 24 November 2026)
- Meyr, H., Wagner, M. & Rohde, J. "Structure of Advanced Planning Systems". In Stadtler, H., Kilger, C. & Meyr, H. (eds.), *Supply Chain Management and Advanced Planning*, 5th ed. Springer, Berlin, Heidelberg, 2015, pp. 99–106 (abstract). https://doi.org/10.1007/978-3-642-55309-7_5 (read at https://rd.springer.com/chapter/10.1007/978-3-642-55309-7_5)
- MHI Solutions magazine. "New MHI and Deloitte Report Finds AI is Biggest Disruptor of Supply Chains Over the Next Decade". 26 June 2026. Named as the claim under examination. https://www.mhisolutionsmag.com/index.php/2026/06/26/new-mhi-and-deloitte-report-finds-ai-is-biggest-disruptor-of-supply-chains-over-the-next-decade/
- Rodrigue, J.-P. *The Geography of Transport Systems*, 6th edition. Routledge, 2024. ISBN 9781032380407. Chapter 7, "Trade, Logistics and Freight Distribution", §7.4, page "Key Drivers for Third and Fourth Party Logistics Providers". https://transportgeography.org/contents/chapter7/logistics-freight-distribution/3pl-4pl-logistics/ (the author's online text of the edition; opened by SCE8, 27 November 2026)
- Scriven, R. (Interact Analysis). "Warehouse Execution Systems vs. Warehouse Control Systems". *Supply & Demand Chain Executive*, 22 February 2023. https://www.sdcexec.com/home/article/22724398/interact-analysis-warehouse-execution-systems-vs-warehouse-control-systems
- Sheffi, Y. (2004). Combinatorial Auctions in the Procurement of Transportation Services. *Interfaces* 34(4), 245–252. https://doi.org/10.1287/inte.1040.0075 (read in full in the author's copy at https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2018-07/10_CombinatorialAuctionsInTheProcurementOfTransportationServices.pdf; opened by SCE7, 24 November 2026)
- United Nations. Convention on the Contract for the International Carriage of Goods by Road (CMR), Geneva, 19 May 1956. Arts. 1, 4, 5. https://treaties.un.org/doc/Treaties/1961/07/19610702%2001-56%20AM/Ch_XI_B_11.pdf
- United States. Code of Federal Regulations, Title 49, Part 377, "Payment of transportation charges", 1 October 2009 edition. https://www.govinfo.gov/content/pkg/CFR-2009-title49-vol5/pdf/CFR-2009-title49-vol5-part377.pdf (opened by SCE7, 24 November 2026)
- United States. Federal Acquisition Regulation, 47.001 "Definitions". Effective 13 March 2026. https://www.acquisition.gov/index%2Ephp/far/47.001
- US Census Bureau. Service Annual Survey, warehousing and storage (NAICS 493), employer firms: total expense, gross annual payroll, all other operating expenses, as published by the Federal Reserve Bank of St. Louis (FRED). https://fred.stlouisfed.org/data/EXPEF493ALLEST ; https://fred.stlouisfed.org/data/EXPGAPEF493ALLEST.txt ; https://fred.stlouisfed.org/data/EXPECFEF493ALLEST ; https://fred.stlouisfed.org/data/EXPAOOEF493ALLEST

## Unsure list

# Unsure: SCE1

1. Quotations from Gartner, Forrester, de Koster et al., Bartholdi & Hackman and MHI were taken from a fetch tool's extraction of each page and were not re-read against a second copy; the exact wording (for example "Client status never influences the outcome or inclusion in our evaluative research") should be checked on the pages.
2. The Gartner glossary entry "Supply Chain Execution (SCE)" was read at gcom.pdo.aws.gartner.com, a gartner.com subdomain; that it matches the www.gartner.com glossary was not confirmed.
3. The Gartner index (https://www.gartner.com/magic-quadrant) shows no headline; the dates in §6 are as the page served them on 21 Nov 2026, including the blank last-updated date for Distributed Order Management against the abstract's 12 Nov 2026.
4. De Koster et al. (2007) Fig. 4 is credited to Tompkins et al. (2003); the travel share in the chart could not be read from the extracted text, so the unit gives no number from it.
5. Bartholdi & Hackman's 55% figures (cost share and travel share) are credited to their reference [21], Frazelle, World-Class Warehousing (1996), as the extracted PDF gave it.
6. That MHI Solutions magazine is MHI's own publication is not stated on the page read.
7. Forrester's statement that customer feedback replaced market presence on the Wave graphic for Waves begun on or after 1 July 2024 rests on one reading of the method page.
8. CMR Art. 1(1) was read only in part; that the Convention covers international carriage between countries party to it rests on its title and the part read.
9. De Vries et al. (2016): the setting, "a warehouse erected especially for the purposes of order picking research", is from the abstract; the country and sample were not stated there.
10. The Gartner Peer Insights WMS market page was read with the query "?months=12"; its product count (140) and the absence of a total review count may differ on the page without the query.

Object: none

Fresh check 2026-11-21 (claude-opus-5-5): fix · 1 error, 2 should-fix, 24 minor; 25 applied, f4 held, f20 no change; report `audits/supply-chain-execution/fresh-check-SCE1.md`

Correction 24 Nov 2026, found by the quality review (W-SCE4; report audits/supply-chain-execution/quality-review-SCE1-2026-11-24.md and quality-review-SCE2-2026-11-24.md; checked in audits/supply-chain-execution/corrections-2026-11-24-QR-SCE1-SCE2.md)

Correction 2026-11-24, found by the SCE4 fresh check and quality review

Correction 24 Nov 2026, found by the W-SCE5 fresh check and quality review (C-SCE5-1 to C-SCE5-9, with C-SCE5-3 amended and the SCE1 Sources list completed), checked by a fresh Opus 5.5 agent in W-SCE6; report audits/supply-chain-execution/corrections-2026-11-24-C-SCE5.md.

Correction 24 Nov 2026, found by SCE6 (row W-SCE6) and its corrections check (row W-SCE7): the C8 row of section 11 now gives what SCE6 section 10 found, the intro's count of claims follows it, and Sources gains the four references the row cites; report `audits/supply-chain-execution/corrections-2026-11-24-C-SCE6.md`.

Correction 25 Nov 2026, found by SCE7 (the writer's contradictions; checked by a fresh Opus 5.5 agent, report audits/supply-chain-execution/corrections-2026-11-25-C-SCE7.md)

Correction 27 Nov 2026, found by SCE8 (the writer's contradictions; checked by a fresh Opus 5.5 agent, report audits/supply-chain-execution/corrections-2026-11-27-C-SCE8.md)

Correction 27 Nov 2026, found by the fresh check of SCE8 (Writer's contradictions, gap 2: the Shipper row's source cell pointed to SCE7 §1, which points back here; report audits/supply-chain-execution/fresh-check-SCE8.md)
