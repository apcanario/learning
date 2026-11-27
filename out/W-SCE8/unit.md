---
code: SCE8
title: The transport system as a product
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-27
search: on
intro: SCE8 treats the transport system as a product. It reads the 2026 analyst definition of a transportation management system (mandatory and common features, who counts as a customer, the shippers' lens of the evaluation) against Gartner's glossary entry; sets beside it the markets for visibility, freight audit and payment, own-fleet routing and trade compliance; describes the five roles that work in a transport system (transport planner, dispatcher, carrier representative, freight auditor, analyst); sets the shipper, for whom freight is a cost, against the logistics provider or broker, who earns a margin on each load; shows what the carrier connection (EDI messages, portals, direct integration) means for the people at each end; places Halvern's (fictional) transport line on SCE7's lifecycle; gives the 2026 Magic Quadrant's vendor list as a dated list; says what public pages and peer reviews can and cannot show; and sets common claim C11 ("a control tower gives end-to-end visibility") against the evidence. Its deliverable is five transport role cards on Ostrel's and Tandric's staff, a shipper-versus-provider comparison table, Halvern's transport line mapped on capability lines T1 to T24 in SCE6's form, and the templates.
---

# SCE8 · The transport system as a product

SCE7 walked one shipment from plan to payment. This unit turns to the software that holds that walk: how the analysts define it, what is sold beside it, who works in it, and why the same product is bought for two different businesses. Grades follow SCE1's key (section 10 there): every claim that carries a number, a mechanism or a recommendation ends with [independent], [analyst], [vendor-reported] or [practice]. Lines marked as this unit's inference or reading, or as working descriptions, carry no grade; they rest on the graded sources they name. A public authority's own account of a rule or of its own occupational data is graded practice, as SCE7 grades it, until flag F18 is decided. Every current fact (an analyst's date, a list, a count) was read on 27 November 2026.

Two limits hold through the unit. The analyst report read is Gartner's *Magic Quadrant for Transportation Management Systems* of 30 March 2026, in a reprint posted by one of the vendors it covers; Gartner's own abstract page failed to load, and the reprint was read through a fetch tool in passes, with its graphic not rendered. And the research opened on the people in a transport office is thin: the role descriptions rest mostly on the US Department of Labor's occupational database and on the case register, and say so.

## 1. What a transportation management system is, as analysts define it

**The 2026 evaluation's definition.** Gartner defines transportation management systems (TMSs) as software that supports "multimodal sourcing, planning and execution" of the physical transport of goods across the supply chain ([Gartner, *Magic Quadrant for Transportation Management Systems*, 30 March 2026, ID G00832918, reprint](https://lp.shipsy.ai/hubfs/Shipsy%20Content%20Library/Gartner/Gartner%20MQ%20TMS%202026.pdf)) [analyst]. Vendors license reprints of Gartner's reports (the course's working assumption, SCE1 §8); this copy is one that a listed vendor chose to post. The report's **mandatory features**, which every evaluated product must have, are:

- **Freight sourcing and procurement**, to procure capacity from third parties "by supporting bid management and optimization" [analyst];
- **Planning**, to take in orders and produce a shipment plan, "including order and shipment consolidation, mode selection, route determination and carrier selection" [analyst];
- **Execution**, "to take the shipment plan and enable communications with carriers" [analyst];
- **Visibility**, to track and trace shipments from pickup to final delivery [analyst];
- **Settlement**, to match expected transportation charges against actual charges [analyst];
- **Analytics** embedded in the product, availability as a stand-alone, self-service application, and all of this on the vendor's own technology [analyst].

Its **common features**, which many products have and the evaluation does not require, are analytics beyond the embedded kind, appointment and dock scheduling, "Private fleet vehicle routing and scheduling/dispatching", parcel carrier selection and manifesting, transportation modelling, forecasting, 3D load building, and direct integration to carrier networks [analyst]. Gartner's review-site definition, updated April 2026, gives the same opening sentence and the same mandatory list ([Gartner Peer Insights, "Transportation Management Systems Reviews and Ratings"](https://www.gartner.com/reviews/market/transportation-management-systems)) [analyst], so SCE7 §5, which read that page, and this report agree.

**Gartner's glossary entry says something else.** It defines a TMS as used "to plan freight movements", to "do freight rating and shopping across all modes", to select the route and carrier, and to "manage freight bills and payments" ([Gartner glossary, TMS entry, undated](https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/tms-transportation-management-system)) [analyst]. Two differences matter, as this unit's reading of the two texts:

- **Payment.** The glossary puts freight bills *and payments* in the TMS. The 2026 report's mandatory list stops at settlement, the check of the charge, and a keyword search of its definition, overview and criteria found no "payment" outside one vendor's profile [analyst]. SCE1 placed payment in the ERP as a working placement; the glossary is the first source in the course that places it in the transport system (flag F6; notes).
- **Rating.** The glossary names freight rating; the 2026 report names neither rating nor tendering in its definition, overview or criteria (same keyword search) [analyst]. Tendering is folded, at most, into "communications with carriers". Where the tender and the carrier's answer are held therefore stays a working placement (flag F64; section 5 adds what the standards body says).

**Who counts as a customer, and for whom the evaluation is written.** The report's Market Overview opens by saying it "evaluates vendors based on the evolving needs of shippers" [analyst]. Its inclusion rules count a customer as a single legal entity holding a contract for the TMS directly with the vendor, and "Gartner does not count customers of reseller partners or service provider clients" [analyst]. To qualify, a vendor needed, among other thresholds, at least 50 live TMS technology customers, at least $10 million in TMS technology revenue in the previous fiscal year, a three-year compound annual customer and revenue growth rate of at least 20%, customers in at least seven industries (the report gives 3PLs as one example of an industry) and at least 10 live customers headquartered outside its home region; the product had to support truckload, less-than-truckload, parcel and ocean, and its capabilities had to be generally available by 31 October 2025 [analyst]. Two consequences, as this unit's inference: a logistics provider that runs a TMS for nine clients counts as one customer, its clients as none; and a vendor that serves one country, or one mode, is outside the evaluation by rule, as SCE6 §2 found for warehouse software.

**Where a textbook stands.** A standard transport text, Novack, Gibson and Coyle's *Transportation: A Global Supply Chain Perspective* (9th edition, Cengage, 2019), treats transportation software and the TMS in chapter 3, according to its publisher's contents page ([Cengage](https://cengage.com/c/new-edition/9781337406642)); the chapter was not read, so it carries nothing here (flag F73).

## 2. What sits beside it

Four kinds of software touch the same shipments. Gartner keeps a separate review market, with its own definition, for three of them; the fourth is in SCE1's glossary.

- **Visibility.** Gartner defines the real-time transportation visibility platform (RTTVP) market as platforms that provide real-time location "and status insights into orders once they have left the warehouse"; mandatory features are basic tracking of location and status in transit, road visibility among other modes, messages and alerts on delays and status changes, a predicted arrival time computed from live and historical data and outside factors such as traffic and weather, independent of the ETA other parties give, and a product sold and implemented on its own ([Gartner Peer Insights, RTTVP market, features updated March 2025](https://www.gartner.com/reviews/market/real-time-transportation-visibility-platforms)) [analyst]. The page listed 46 products [analyst]. The TMS evaluation makes tracking mandatory in the TMS itself (section 1), so the same event can be held by two products (this unit's inference).
- **Freight audit and payment (FAP).** Gartner describes FAP services as invoice collection, preaudit, processing, payment and analytics of transportation invoices across multiple modes and regions ([Gartner Peer Insights, FAP providers market](https://external.pi.gpi.aws.gartner.com/reviews/market/freight-audit-and-payment-providers)) [analyst]; the page listed 42 products and showed no features date. The word is *services*: a shipper can buy the audit and the payment as work done by someone else, while the TMS's settlement capability checks the charge (section 1). Which of the two holds the paid record is a seam question for SCE10.
- **Routing for own fleets.** Gartner defines a vehicle routing and scheduling (VRS) solution as an application that creates vehicle routes and schedules under multiple constraints and service requirements while minimising fleet costs and mileage; its mandatory features are scenario modelling, territory planning, real-time routing, dispatch, dynamic routing and static routing ([Gartner Peer Insights, VRS market, features updated July 2026](https://www.gartner.com/reviews/market/vehicle-routing-and-scheduling)) [analyst]; the page listed 79 products. The TMS evaluation lists private fleet routing and dispatch as a common TMS feature (section 1) [analyst]. SCE7 §8 explains why the problem is different from bought freight.
- **Global trade management (GTM).** Trade compliance and international logistics, which Gartner lists beside the warehouse and transport systems in its execution glossary (SCE1 §4) [analyst]. This course does not treat it further.

Read together, the definitions place the lifecycle's steps in different products:

```viz
{"kind": "matrix", "title": "Which definition names which transport step", "cols": ["Procure", "Plan", "Rate", "Tender", "Track", "Check charges", "Pay", "Fleet routing"], "rows": [{"label": "TMS, 2026 Magic Quadrant", "tone": 4, "cells": ["mandatory", "mandatory", null, null, "mandatory", "mandatory", null, "common"]}, {"label": "TMS, Gartner glossary", "tone": 4, "cells": [null, "named", "named", null, null, "bills", "named", null]}, {"label": "Visibility platform (RTTVP)", "tone": 3, "cells": [null, null, null, null, "mandatory", null, null, null]}, {"label": "Freight audit and payment", "tone": 2, "cells": [null, null, null, null, null, "named", "named", null]}, {"label": "Vehicle routing and scheduling", "tone": 5, "cells": [null, null, null, null, null, null, null, "mandatory"]}], "legend": [{"mark": "mandatory", "means": "a mandatory feature in the definition"}, {"mark": "common", "means": "a common feature of the 2026 TMS evaluation"}, {"mark": "named", "means": "named in the definition, with no mandatory or common list"}, {"mark": "bills", "means": "the glossary's 'manage freight bills'"}], "caption": "Sections 1 and 2 of this unit. Sources: Gartner, Magic Quadrant for Transportation Management Systems, 30 March 2026 (reprint); Gartner glossary, TMS entry (undated); Gartner Peer Insights market definitions for real-time transportation visibility platforms (March 2025), freight audit and payment providers (no date shown) and vehicle routing and scheduling (July 2026), all read 27 November 2026. Tender is named by none of them."}
```

## 3. Who works in a transport system

The brief names five roles. Job titles vary by company and region. The US Department of Labor's occupational database, O*NET, describes three of them from its own task statements; it is a US source, and what it says is graded practice (a public authority's account). The rest is working description, and the cards in the deliverable mark each line.

### 3.1 Transport planner

**What the work is.** Turns orders into shipments or routes: consolidates, picks the mode and the carrier, or builds the day's routes for an own fleet. Planning in Gartner's mandatory list is exactly that: consolidation, mode selection, route determination and carrier selection (section 1) [analyst]. O*NET has no "transport planner" occupation; "Load Planner" is a sample job title under Cargo and Freight Agents, whose core tasks include to "Negotiate and arrange transport of goods with shipping or freight companies" and to "Determine method of shipment" and prepare the shipping documents ([O*NET, 43-5011.00, updated 2026](https://www.onetonline.org/link/details/43-5011.00)) [practice]; and among logistics analysts' supplemental tasks is to reorganise shipping schedules "to consolidate loads, maximize vehicle usage" ([O*NET, 13-1081.02, updated 2026](https://www.onetonline.org/link/details/13-1081.02)) [practice].

**What they do in the system.** Release orders into a plan, accept or change the proposed consolidation, choose or confirm the carrier, and send the tender (SCE7 §6, steps 1 to 3). For an own fleet, build and publish routes. Working description.

**Measured on.** Vehicle fill and freight cost per unit, both the course's definitions (SCE7 §11); for an own fleet, routes built on time and vehicles used. No source opened defines a planner's measures.

**In the case.** Sofia (fictional) builds Ostrel Foods' next day's routes for 40 vehicles and about 600 delivery points (case register). At Tandric Logistics (fictional), Priya's freight desk tenders loads to carriers (register), so the planner's tender work sits with her there; SCE7 deliverable B has her planning the load (this unit follows that reading).

### 3.2 Dispatcher

**What the work is.** Runs the day once the plan is out. O*NET describes dispatchers as workers who schedule and dispatch crews, equipment or service vehicles to move materials, freight or passengers, using radio, phone or computer to send assignments and compile progress reports; "Truck Dispatcher" is a sample title, and the tasks include to "Prepare daily work and run schedules" and to monitor equipment locations and use to coordinate service and schedules ([O*NET, 43-5032.00, updated 2026](https://www.onetonline.org/link/summary/43-5032.00)) [practice]. O*NET's software list for the occupation includes route navigation, mobile location-based services, map creation and geographic information software, and names no transport management system (same page) [practice].

**What they do in the system.** Watch vehicles against the plan, change stops or sequence during the day, record exceptions from drivers. Dispatch and real-time routing are mandatory features of Gartner's VRS market (section 2) [analyst], so for an own fleet the dispatcher's screen is likely to be a routing product's (this unit's inference). For bought freight, the dispatcher's counterpart watches carriers' status events instead (section 5).

**Measured on.** On-time delivery (the course's definition, SCE7 §11). Working.

**In the case.** Nuno (fictional) handles Ostrel's day's calls from drivers and customers (register); Ostrel's drivers return with refused goods, and some routes still run on paper delivery notes (register).

### 3.3 Carrier representative

**What the work is.** The person at the carrier who answers the shipper's or provider's system: accepts or refuses a tender, gives a pickup time, reports status, sends the invoice. No O*NET occupation or other source opened describes the role, so everything about it is working description, except the messages it answers. In X12, the US-based standards body for electronic data interchange, the 214 message "can be used by a transportation carrier" to give shippers, consignees and their agents the status of shipments in dates, times, locations, route and identifying numbers ([X12, 214](https://x12.org/node/4214)) [independent, for what the standard says]; the 210 is "used both as a motor carrier invoice to request payment" and as detail of a shipment's charges ([X12, 210](https://x12.org/node/4210)) [independent]. The tender (204) and the answer (990) are section 5's and SCE7 §6's.

**Measured on.** By the party tendering: whether it accepts, measured as the primary carrier acceptance ratio, and whether it picks up and delivers on time (SCE7 §§4, 11). In the one large study SCE7 read, weekly primary acceptance averaged 81.9% in a soft US truckload market and 68.5% in a tight one (Acocella, Caplice and Sheffi 2020, as read in SCE7 §4) [independent]. By its own employer: no source opened.

**In the case.** The register names no carrier staff. The card in the deliverable is for the person at a carrier who answers Priya's tenders at Tandric (fictional), unnamed.

### 3.4 Freight auditor

**What the work is.** Checks each carrier invoice against what was agreed and releases it for payment, or disputes it. In Gartner's terms the check is the TMS's settlement capability, matching expected against actual charges (section 1) [analyst], and the whole job can be bought as a freight audit and payment service (section 2) [analyst]. O*NET has no freight-audit occupation; its nearest, Billing and Posting Clerks, includes "Pre Audit Clerk" among sample titles and tasks such as computing "shipment charges, or rates for goods or services" to complete billing documents ([O*NET, 43-3021.00, updated 2026](https://www.onetonline.org/link/summary/43-3021.00)) [practice]; none of its tasks names freight or carriers (same page).

**What they do in the system.** Open the invoice, see it matched against the tender, the rate and any recorded extras (waiting time, re-delivery), approve or query (SCE7 §6, steps 9 to 11). Working description.

**Measured on.** The course's invoice match rate (SCE7 §11). No independent study of freight invoice error rates was found (SCE7 §6, step 10), and none was found here.

**In the case.** Priya (fictional) checks carriers' invoices at Tandric (register); Tandric's invoices are disputed when activity was not recorded (register).

### 3.5 Analyst

**What the work is.** Turns the transport record into measures and recommendations. O*NET's Logistics Analysts lists "Transportation Analyst" among sample titles; its core tasks include to "Prepare reports on logistics performance measures", to compute metrics "such as on-time delivery rates", to provide ongoing analyses of "transportation costs" and to "Contact carriers for rates or schedules", and a supplemental task is to maintain freight rate databases (O*NET, 13-1081.02) [practice]. APQC, the benchmarking association, keeps an outbound-transport cost measure, "Total Cost to Operate Outbound Transportation per $1,000 in Revenue" ([APQC](https://www.apqc.org/knowledge-base/documents/total-cost-operate-outbound-transportation-1000-revenue)) [practice: the measure's name; its definition was not on the page read] (flag F77).

**What they do in the system.** Run the embedded analytics that Gartner makes mandatory (section 1) [analyst], export data, and prepare the bid that sets next year's routing guide (SCE7 §3). Working description.

**Measured on.** No source opened. Working: the reports delivered, and whether the recommendations moved cost or service.

**In the case.** The register has no analyst. At Tandric (fictional), Olu answers the clients' questions and sends their reports (register); this unit treats that report work as the analyst's role there (this unit's reading, listed in the notes).

| Role | Steps of SCE7 §6 worked | Basis |
|---|---|---|
| Transport planner | 1 Plan, 2 Rate, 3 Tender | Gartner planning [analyst]; O*NET 43-5011.00 [practice]; working |
| Dispatcher | Own-fleet day; 7 Track; 8 Deliver | O*NET 43-5032.00 [practice]; Gartner VRS [analyst]; working |
| Carrier representative | 4 Answer, 5 Book a dock, 7 Track, 9 Invoice | X12 214, 210 [independent]; working |
| Freight auditor | 9 Invoice, 10 Check, 11 Pay | Gartner settlement and FAP [analyst]; working |
| Analyst | Reports on all steps; next year's bid | O*NET 13-1081.02 [practice]; working |

## 4. Two kinds of customer: the shipper and the provider

**The shipper.** For a shipper, freight is a cost of selling its own goods. It buys carriage (SCE7 §1), or runs its own vehicles, and the measures it watches are what it pays and the service it gets: freight cost per unit, on-time delivery, carrier acceptance (SCE7 §11). The 2026 evaluation is written from this side: it evaluates vendors "based on the evolving needs of shippers" (section 1) [analyst]. Corvane (fictional) books carriers in each carrier's portal, with no transport system; Ostrel Foods (fictional) runs its own fleet with a routing tool (case register).

**The logistics provider or broker.** For a provider, freight is what it sells. Tandric's (fictional) freight desk arranges loads with outside carriers for clients, owns no trucks, and is paid for freight at a margin over what the carrier is paid (register). In US law a broker is a person, other than a motor carrier, who arranges motor carrier transportation for compensation (49 U.S.C. §13102(2), as read in SCE7 §1) [independent]. O*NET lists "Freight Broker" as a sample title of Cargo and Freight Agents, and its Freight Forwarders' core tasks include to "Negotiate shipping rates with freight carriers", to "Prepare invoices or cost quotations for freight transportation" and to "Pay or arrange for payment of freight" ([O*NET, 43-5011.01, updated 2026](https://onetonline.org/link/details/43-5011.01)) [practice]: one person both buys the carriage and sells it on. MIT's FreightLab names shippers, carriers and brokers as the three parties its freight research works for ([MIT CTL, FreightLab](https://ctl.mit.edu/research/freightlab)) [practice]. Textbook vocabulary does not settle the categories: Rodrigue's *Geography of Transport Systems* calls a third-party logistics provider "an asset-based company" offering logistics services, and a fourth-party provider non-asset-based, mainly providing organisational expertise ([Rodrigue, 6th edition, Routledge, 2024, ch. 7](https://transportgeography.org/contents/chapter7/logistics-freight-distribution/3pl-4pl-logistics/)) [practice]; by that test Tandric, with a warehouse and no trucks, is asset-based in warehousing and not in freight (this unit's reading).

**What the margin does to the record.** Because the provider earns the difference between two prices, each load carries two rates (the client's price and the carrier's), two invoices (the carrier's to Tandric and Tandric's to the client) and two disputes (SCE7 deliverable B, rows 2 and 9 to 12). In the United States the margin is also a record the other parties can ask for: the current rule gives "the parties to a brokered freight transaction" a right to review the broker's record of it, and a notice of proposed rulemaking would require brokers to keep those records electronically, itemise all charges and fees, and provide them within 48 hours of a request by the shipper, the motor carrier or any other party ([FMCSA, Docket FMCSA-2023-0257, Transparency in Property Broker Transactions](https://www.fmcsa.dot.gov/regulations/docket-no-fmcsa-2023-0257-rin-2126-ac63-transparency-property-broker-transactions)) [practice: the agency's account of the current rule and of a proposal]. Whether the proposal became final was not checked here, and whether Tandric is a broker in law, and what it must disclose, is a question for its legal advisers and the national regulator (SCE7 §1).

**What shippers say they want from providers.** In the *2025 Third-Party Logistics Study*, sponsored by NTT DATA and Penske Logistics, with a survey that closed in July 2024, shipper respondents named as must-have technologies from their 3PLs control tower visibility (68%), transportation management planning (54%) and transportation management scheduling (53%); 55% of 3PL respondents said their IT services include control tower visibility, and the share of shippers satisfied with 3PLs' IT capabilities was 87% ([2025 Third-Party Logistics Study](https://us.nttdata.com/en/-/media/nttdataamerica/files/gated-asset/1555533-NTT-DATA-3PL-Study-2025.pdf)) [vendor-reported: a sponsored survey; the total number of respondents was not found in the text read, which gives shares by group: shipper users 44%, non-users 9%, 3PL or 4PL respondents 27%]. For a provider, then, transport planning and visibility are things it sells to its clients, which a shipper only uses (this unit's inference from a sponsored survey).

**What small providers can spend.** One mixed-methods study of small and medium-sized Italian 3PLs (a postal survey of 1,992 firms with 153 usable responses, focus groups, and seven case companies) found "a relatively low level of ICT expenditure", that only 38% of the sample offered track and trace, partly because customers did not demand it, that ICT products and services were seen as not aligned with small 3PLs' needs, and that lack of technology skills was a major constraint ([Evangelista, McKinnon & Sweeney, 2013](https://doi.org/10.1108/IMDS-10-2012-0374), author's manuscript read in full) [independent]. Applying it to providers outside Italy, or to 2026, is this unit's inference.

**Where the two pull apart**, as this unit's reading of the sources above and the register:

- **Rates on both sides.** A shipper's TMS holds what it pays; a provider's holds what it pays and what it charges, and the margin between them per load.
- **Many customers inside one system.** Each of Tandric's nine clients wants its own rules and reports, and a new client is expected to be live within weeks of signature (register). A shipper configures one company.
- **The client as a user.** Tandric has a client portal (register); the client sees the provider's data. A shipper's customers see, at most, a delivery date.
- **Billing.** A shipper pays invoices; a provider pays and issues them, and its invoices are disputed when activity was not recorded (register).
- **Who the analyst counts.** The evaluation counts the provider as one customer and its clients as none, and is written around shippers' needs (section 1) [analyst]. A provider reading it reads a shipper's evaluation.

Deliverable B sets these out row by row. DD-SCE1 develops the provider's business.

## 5. How the system connects to carriers, and what that means for the people

Three kinds of connection carry the same conversation between the system and a carrier: the tender, the answer, the status and the bill.

**Electronic data interchange (EDI).** X12's 204 Motor Carrier Load Tender allows "shippers or other interested parties to offer (tender) a shipment" to a full-load (truckload) motor carrier, with scheduling, equipment, commodities and instructions; it is not used for less-than-truckload bills of lading, pickup notifications or manifests ([X12, 204](https://x12.org/node/4207)) [independent, for what the standard says]. The carrier answers with a 990 (SCE7 §6, step 3) [independent], reports status with a 214, and bills with a 210 (section 3.3) [independent]. In GS1's EANCOM subset of UN/EDIFACT messages, IFTSTA carries transport status (SCE7 §6, step 7) [independent]. Which regions use which standard was not sourced (SCE7 §7). On the standard's wording, the tender is the shipper's or another interested party's message, which places the tender with whoever runs the shipper's side: Tandric's desk, or a shipper's transport system (this unit's reading; flag F64).

```viz
{"kind": "swimlanes", "lanes": [{"id": "tms", "label": "Shipper's or provider's transport system", "tone": 4}, {"id": "carrier", "label": "Carrier", "tone": 3}], "steps": [{"id": "t204", "lane": "tms", "col": 0, "label": "Tender", "note": "X12 204"}, {"id": "t990", "lane": "carrier", "col": 1, "label": "Accept or refuse", "note": "X12 990"}, {"id": "t214", "lane": "carrier", "col": 2, "label": "Status", "note": "X12 214; IFTSTA"}, {"id": "t210", "lane": "carrier", "col": 3, "label": "Invoice", "note": "X12 210"}, {"id": "check", "lane": "tms", "col": 4, "label": "Check charges", "note": "settlement"}, {"id": "pay", "lane": "tms", "col": 5, "label": "Pay", "note": "TMS or ERP"}], "links": [{"from": "t204", "to": "t990", "label": "offer"}, {"from": "t990", "to": "t214"}, {"from": "t214", "to": "t210"}, {"from": "t210", "to": "check"}, {"from": "check", "to": "pay"}], "caption": "The messages between a transport system and a carrier, section 5 of this unit. Sources: X12's pages for the 204, 210 and 214 transaction sets (read 27 November 2026) and SCE7 section 6 for the 990 and IFTSTA; settlement from Gartner's 2026 TMS evaluation; payment's place is open (TMS in Gartner's glossary, ERP in SCE1's working placement)."}
```

**Portals.** A carrier that does not exchange EDI can be worked through a web portal: the shipper books in the carrier's portal, as Corvane (fictional) does today (register), or the carrier answers in a portal the shipper's or provider's system offers (working description; no source opened describes such portals). **Direct integration to carrier networks**, connecting a large number of external carriers, is a common feature of the 2026 evaluation (section 1) [analyst]; the report's wording does not say by which technology.

**How many carriers there are to connect.** In the United States, of 787,189 active carriers registered with the Federal Motor Carrier Safety Administration at the end of 2023, 418,526 had one power unit (a truck or tractor, in this course's gloss), 123,353 had two, 168,507 had three to ten, 56,715 had 11 to 100 and 5,062 more than 100; 735,895 were interstate freight carriers ([FMCSA, *2024 Pocket Guide to Large Truck and Bus Statistics*, July 2025, data from a 29 December 2023 snapshot](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/FMCSA%20Pocket%20Guide%202024-v6%20508%20.pdf)) [independent: official registration statistics]. About 53% had one power unit and about 90% ten or fewer (this unit's arithmetic, all carrier types). No source opened says how many of them exchange EDI, and no European figure was opened. A transport system that tenders to small carriers will meet many with no EDI at all (this unit's inference).

**What the connection means for each role**, as this unit's reading:

- **Planner.** With EDI, a tender goes out and an answer comes back into the record; without it, the planner phones or e-mails, waits, and keys the answer. The acceptance ratio (section 3.3) is computable only from answers the system recorded.
- **Dispatcher or tracking desk.** Status arrives as 214 or IFTSTA events, or as calls. A missing event leaves the customer told nothing (SCE7 §10).
- **Carrier representative.** Works in every customer's channel at once: one shipper's EDI, another's portal, a broker's phone call. Each customer's system is one more place to answer.
- **Freight auditor.** A 210 can be matched against the tender automatically; a paper or PDF invoice is keyed first.

## 6. Halvern's transport line on SCE7's lifecycle

Halvern Systems (fictional) sells order, warehouse and transport software and nothing else, to retailers, distributors and logistics providers, mid-sized to large, by cloud subscription, and says of itself "One vendor for execution" (case register). Its transport line is **Halvern Transport** (the core system) with five modules: **Rating and Tendering**, **Fleet Routing**, **Tracking**, **Freight Audit** and **Claims** (register). Everything in this section is a case fact or a placement of one; none of it is evidence about any real product, and no real vendor is meant.

**On SCE7's steps**, SCE7 §5 placed the modules: Rating and Tendering at steps 2 to 4, Tracking at step 7, Freight Audit at steps 10 and 11, Claims at step 12, and Fleet Routing in own-fleet routing, outside bought freight (register, added by SCE7). This unit adds one assumption: the core holds the shipment plan of step 1 (consolidation, mode and carrier selection), the first of Gartner's mandatory planning capabilities (section 1) [analyst], as SCE6 placed Gartner's core warehouse capabilities in Halvern Warehouse's core; it is listed in the notes for the register.

```viz
{"kind": "matrix", "title": "Halvern's transport line on the shipment lifecycle (fictional)", "cols": ["1 Plan", "2 Rate", "3 Tender", "4 Answer", "5 Dock", "6 Pick up", "7 Track", "8 Deliver", "9 Invoice", "10 Check", "11 Pay", "12 Claim", "Own fleet"], "rows": [{"label": "Halvern Transport (core)", "tone": 1, "cells": ["assumed", null, null, null, null, null, null, null, null, null, null, null, null]}, {"label": "Rating and Tendering", "tone": 4, "cells": [null, "placed", "placed", "placed", null, null, null, null, null, null, null, null, null]}, {"label": "Tracking", "tone": 3, "cells": [null, null, null, null, null, null, "placed", null, null, null, null, null, null]}, {"label": "Freight Audit", "tone": 2, "cells": [null, null, null, null, null, null, null, null, null, "placed", "placed", null, null]}, {"label": "Claims", "tone": 5, "cells": [null, null, null, null, null, null, null, null, null, null, null, "placed", null]}, {"label": "Fleet Routing", "tone": 6, "cells": [null, null, null, null, null, null, null, null, null, null, null, null, "placed"]}], "legend": [{"mark": "placed", "means": "SCE7 section 5's placement of a register module"}, {"mark": "assumed", "means": "this unit's assumption: the core holds the shipment plan"}], "caption": "Section 6 of this unit. Module names from the case register (Halvern Systems, fictional); steps from SCE7 section 6; placements from SCE7 section 5, the core's from this unit. Steps 5, 6, 8 and 9 have no module. Case facts, evidence of nothing about any real product."}
```

**What the placement shows**, as this unit's reading:

- **Four steps have no module.** Booking a dock (5), pickup (6), delivery and its proof (8) and the carrier's invoice coming in (9). Halvern lists a Yard module in its warehouse line and none in its transport line (register; SCE7 §9), so the appointment may sit in the warehouse product. Whether Freight Audit takes in the invoice (step 9) or only checks it is open.
- **Freight Audit's name claims the check.** SCE7 placed it at payment too (step 11); the register's name says audit, and Gartner's glossary puts payment in the TMS (section 1). Whether Halvern pays carriers, or hands the approved invoice to the ERP, is a question for its pages, not answerable from the register.
- **Nothing in the transport line bills a client.** Halvern's warehouse line has Client Billing, for billing clients by activity (register; SCE6 §7). Tandric (fictional) is paid for freight at a margin (register), so it needs a client price and a client invoice for each load; the register gives no module that holds either. Halvern names logistics providers among its customers (register); whether its line serves the provider's half of the record is the open question deliverable C ends on.
- **Tracking or a visibility platform.** Gartner treats tracking both as a TMS capability and as a separate market (section 2); Halvern's Tracking module claims the step and says nothing of predicted arrival times or alerts.

## 7. The transport capability list

The functions of SCE7 and this unit, restated as lines a buyer would recognise, numbered T1 onward so that they do not collide with SCE6's W1 to W29 (flag F62). Each line names its lifecycle step (SCE7 §6, or the section that teaches it) and the sources that name it. The grouping and the IDs are this unit's; deliverable C uses them.

| ID | Step (unit) | Capability | Named as a capability by |
|---|---|---|---|
| T1 | Buying capacity (SCE7 §3) | Freight sourcing: bids, lanes, the routing guide | Gartner 2026, mandatory [analyst] |
| T2 | 1 Plan (SCE7 §6) | Order intake and shipment planning: consolidation, mode, route, carrier selection | Gartner 2026, mandatory [analyst]; Gartner glossary [analyst] |
| T3 | 1 Plan | 3D load building | Gartner 2026, common [analyst] |
| T4 | 2 Rate | Rating: contract rates, tariffs, freight class | Gartner glossary, "freight rating and shopping" [analyst] |
| T5 | 3 Tender, 4 Answer | Tendering and the carrier's answer | X12 204, 990 [independent]; within "communications with carriers", Gartner 2026 [analyst] |
| T6 | 4 Answer (SCE7 §3) | Routing-guide cascade to backups and spot | Acocella et al. 2020, as SCE7 §3 reads it [practice]; no analyst list names it |
| T7 | 5 Book a dock | Appointment and dock scheduling | Gartner 2026, common [analyst] |
| T8 | Mode: parcel (SCE7 §2) | Parcel carrier selection and manifesting | Gartner 2026, common [analyst] |
| T9 | 7 Track | Tracking: carrier status events | Gartner 2026, mandatory [analyst]; X12 214 [independent] |
| T10 | 7 Track | Predicted arrival times and alerts | Gartner RTTVP, mandatory [analyst] |
| T11 | 8 Deliver | Proof of delivery record | SCE7 §6, course term |
| T12 | 9 Invoice | Freight invoice intake | X12 210 [independent] |
| T13 | 10 Check | Settlement: expected against actual charges | Gartner 2026, mandatory [analyst]; Gartner FAP [analyst] |
| T14 | 11 Pay | Freight payment | Gartner glossary [analyst]; Gartner FAP [analyst] |
| T15 | 12 Claim | Claims for loss, damage and delay | SCE7 §6, step 12 (the rules) [independent]; no analyst list names it |
| T16 | Own fleet (SCE7 §8) | Private fleet routing and scheduling | Gartner 2026, common [analyst]; Gartner VRS, mandatory [analyst] |
| T17 | Own fleet (SCE7 §8) | Dispatch and same-day changes | Gartner 2026, common [analyst]; Gartner VRS, mandatory [analyst] |
| T18 | Carriers (section 5) | Direct integration to carrier networks | Gartner 2026, common [analyst] |
| T19 | Carriers (section 5) | Portal for carriers without EDI | Working; no source opened |
| T20 | Reports (section 3.5) | Transport analytics: on-time, cost by mode | Gartner 2026, mandatory [analyst] |
| T21 | Reports (section 3.5) | Transport modelling and forecasting | Gartner 2026, common [analyst] |
| T22 | Provider (section 4) | Client pricing and freight billing of clients | Case register (Tandric); no analyst list names it |
| T23 | Provider (section 4) | Many clients in one system: their own rules, reports and portal | Case register (Tandric); no analyst list names it |
| T24 | Beside the system (section 2) | Trade compliance | Gartner SCE glossary, as SCE1 §4 reads it [analyst] |

Three lines (T6, T22, T23) are needs the analyst definitions read here do not name; two of them are the provider's. No source opened measures which lines an operation needs, or which are worth paying for.

## 8. The real market: one dated list

The course names real vendors only in a dated list from a named analyst report or an audited filing, every vendor on the list alike, with no vendor assessed, ranked, compared or recommended (course brief).

The vendors evaluated in Gartner's *Magic Quadrant for Transportation Management Systems*, 30 March 2026 (ID G00832918; analysts B. Johns, O. Sanchez Duran, M. Jain), read in a reprint on 27 November 2026, as headed in its Vendor Strengths and Cautions section; the report says no vendors were added and one, Aptean, was dropped as it did not meet the inclusion criteria [analyst]:

- Alpega
- Bluerock TMS
- Blue Yonder
- C.H. Robinson
- E2open
- Infios
- Manhattan Associates
- Oracle
- Pando
- SAP
- Shipsy
- Shipwell
- Tesisquare
- TMSfirst
- Uber Freight
- vTradEx

The reprint did not say how many vendors Gartner considered. The list gives no placement here, and the course does not reproduce placements. Gartner's own guidance is to use an evaluation to narrow a list and not to decide on it alone (SCE1 §8, C10) [analyst]. The seed bibliography also names an IDC MarketScape for transportation management systems in 2026 (A7); IDC's own page for it was not found by search, only vendors' releases about it, so this unit gives nothing from it.

## 9. What public pages and peer reviews can and cannot show

**Peer reviews.** Gartner's TMS review market listed 92 products on 27 November 2026 and showed no total count of reviews; each product listing carries its own count of ratings (Peer Insights TMS page) [analyst]. Vendors can invite their own customers to review (SCE1 §7), so this course grades what reviewers say vendor-reported. What a market page can give is what a counted number of reviewers of a named kind (industry, company size, role, where the page shows them) say about products in that market. It cannot give how a product performs, whether it suits a provider or a shipper unless reviewers say which they are, or a ranking (this unit's inference from SCE1 §7).

**Vendors' pages and listings.** The product descriptions on the same market page claim, between them, load tendering, freight auditing and payment, and automated tendering (Peer Insights TMS page) [vendor-reported]: the vendors put in their TMS products what the analyst's mandatory list leaves unnamed. That is evidence of what they claim (flag F64). The method and the cautions of SCE6 §9 apply unchanged: collect the pages with their dates, list the modules in the vendor's own names, place each claim on lines T1 to T24, grade every row vendor-reported, and write "no public claim found" where no page claims a line.

**What the pages cannot show**, as this unit's inference, in addition to SCE6 §9's list:

- **Which customer the product was built for.** A page that lists shippers, carriers and brokers as users does not say whether a broker's two-sided rate (T22) or many clients in one system (T23) exist.
- **How the carriers are connected.** A count of connected carriers does not say by EDI, by portal or by a third party's network, or what a small carrier must do to answer (section 5).
- **Where payment happens.** A page that claims "freight payment" may mean the TMS approves, a service pays, or the ERP pays (sections 1, 2).
- **The analyst report itself.** Two vendors' landing pages for the 2026 report, opened for this unit, held no report text, only the offer of a copy on request; such a page states only the vendor's own placement, which this course does not repeat.

## 10. C11: "A control tower gives end-to-end visibility"

**The claim as it circulates.** A control tower, one screen fed by every party's data, shows the whole chain from order to delivery (course list, C11).

**What the sources opened show.**

- **The analyst's definitions bound visibility.** Gartner's visibility-platform market covers orders "once they have left the warehouse" (section 2) [analyst]; its TMS evaluation requires tracking from pickup to final delivery (section 1) [analyst]. The visibility each describes starts at the warehouse door or at pickup; neither covers the goods before they leave. The 2026 TMS report says vendors are "enhancing their control-tower-like capabilities", and the phrase "end-to-end visibility" does not appear in it (keyword search of the reprint) [analyst]. One vendor profile in the report describes automated agents inside a control tower; AI features are outside this course.
- **Buyers ask for it.** In the sponsored 2025 Third-Party Logistics Study, 68% of shipper respondents named control tower visibility a must-have technology from their 3PLs, and 55% of 3PLs said they offer it (section 4) [vendor-reported]. That measures demand and offer; it says nothing of reach.
- **One study looked inside.** Staudt et al. combined a scoping review of 32 papers on control towers with semi-structured interviews of four employees at three large multinational companies in Brazil (mining, refrigeration and engines, civil construction). They define a control tower as a technology-enabled platform that integrates real-time data with analytics and organisational knowledge; they found that two of the three companies had not yet incorporated real-time tracking or visibility layers, that end-to-end supply chain management was not identified in the cases, and that legacy systems, data quality and interoperability mean "full integration remains a distant goal" ([Staudt, Lopes, Corrêa, Bouzon & Di Mascolo, 2026, full text](https://doi.org/10.14488/1980-5411.20250126)) [independent: qualitative, three companies, one country]. Applying it to other companies is this unit's inference.

**What the evidence shows.** No source opened shows that a control tower gives end-to-end visibility. The analyst definitions draw visibility from pickup or from the warehouse door onward; the one independent study found visibility layers missing in two of three companies and end-to-end management in none. **No independent source found** for the claim. What a product team can ask of any "end-to-end" claim is which parties' data feeds it, by which connection (section 5), and from which step to which (SCE7 §6).

## On a site visit

SCE8 is not an operations unit, so the visit is to colleagues in sales, services and product. Ask:

- **Which definition of a TMS do our requirements and contracts use: the 2026 evaluation's mandatory list, the glossary's, or our own?** In particular, do we claim payment, or only the check (section 1)?
- **Do our customers count as shippers or as providers, and how many of each?** For a provider, how many of its clients use our system through it, and does any analyst count them (section 1)?
- **Where does a tender go, and where does the carrier's answer land?** EDI, our portal, the carrier's portal, e-mail (section 5)?
- **How many of our customers' carriers answer by EDI, and what does a carrier with one truck do?** (Section 5.)
- **Can one load carry two rates and two invoices, the carrier's and the client's, with the margin between them?** (Section 4; T22.)
- **Can a provider keep each client's rules, reports and portal apart, and bring a new client live within weeks?** (Section 4; T23.)
- **When we say "end-to-end visibility", from which step to which, and from whose data?** (Section 10.)
- **Which analyst report do we cite, of which date, and did we read it in full, in a reprint or in abstract?** (Sections 8, 9.)

## Self-check

1. **What does Gartner's 2026 TMS evaluation make mandatory, and what does it leave out that the glossary includes?**
   Freight sourcing and procurement, planning, execution (communications with carriers), visibility, settlement, embedded analytics, stand-alone availability, the vendor's own technology. The glossary adds freight rating and the management of freight bills and payments; neither text names tendering (section 1).
2. **For whom does the 2026 evaluation say it is written, and how does it count a provider's clients?**
   It evaluates vendors on the evolving needs of shippers, and it counts a customer as one legal entity contracting directly with the vendor; it does not count service provider clients (section 1).
3. **Name the markets Gartner keeps beside the TMS for visibility, freight audit and own-fleet routing, and one boundary of each.**
   Real-time transportation visibility platforms, for orders once they have left the warehouse; freight audit and payment, services from invoice collection to payment; vehicle routing and scheduling, routes and schedules for a fleet, with dispatch mandatory (section 2).
4. **Which X12 messages pass between a transport system and a carrier, and what is each for?**
   204, the shipper's or another party's load tender to a truckload carrier; 990, the answer; 214, the carrier's shipment status; 210, the carrier's invoice and charge detail (sections 3.3, 5).
5. **Why does a provider's record differ from a shipper's for the same load?**
   The provider is paid at a margin, so each load has the client's price and the carrier's rate, two invoices and two possible disputes; in the US the parties to a brokered transaction may review the broker's record (section 4).
6. **What did the small-3PL study in Italy find about technology?**
   With 153 usable survey responses, focus groups and seven cases: low ICT spending, track and trace offered by 38%, partly because customers did not ask, ICT seen as not aligned with small 3PLs' needs, and lack of skills as a major constraint (section 4).
7. **Where does Halvern's transport line leave the lifecycle open?**
   No module at booking a dock, pickup, delivery or the incoming invoice; payment only by SCE7's placement of Freight Audit; nothing that prices or bills a provider's client (section 6).
8. **A colleague says a control tower gives end-to-end visibility. What do you answer?**
   No source opened shows it. Gartner's visibility definitions start at pickup or the warehouse door; the one independent study, of three Brazilian multinationals, found visibility layers missing in two and end-to-end management in none (section 10).

## Deliverable

Four parts: A, the five transport role cards; B, the shipper-versus-provider comparison table; C, Halvern's transport line on the capability lines T1 to T24, in SCE6's capability map form; D, the templates for all three; then E, glossary lines. Cells cite this unit's sections in brackets, an earlier unit's section, "register" for a case fact, or "working" for a working description that rests on no source and is listed in the notes where it adds to the register.

### A. Five transport role cards, Ostrel Foods and Tandric Logistics (fictional)

The form is SCE5's role card (SCE5 deliverable A), nine fields in its order. Ostrel Foods (fictional) is a food distributor with its own fleet of 40 vehicles, about 600 delivery points a day on fixed routes adjusted daily, a routing tool for the fleet and paper delivery notes on some routes (register). Tandric Logistics (fictional) is a logistics provider whose freight desk arranges full and part loads with outside carriers for clients, with no trucks of its own, paid for freight at a margin over what the carrier is paid; it runs a transport system for the freight desk and a client portal (register).

**Card 1 · Sofia, transport planner, Ostrel Foods (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Sofia; transport planner, builds the next day's routes; Ostrel Foods [register]. SCE5 set her card as the warehouse's planner (card 4); this card sets her as a transport role, SCE8. Ostrel's transport is own-account in European terms, private carriage in US terms (SCE7 register note) |
| 2 | Measured on | Routes built by the time picking starts; vehicles used of the 40 [register, added by SCE5; working]; vehicle fill (SCE7 §11, the course's definition) |
| 3 | Conditions | Desk work between the late-afternoon order cut-off and the evening start of picking [register, SCE5] |
| 4 | Device | Desktop: the routing tool and the ERP [register] |
| 5 | Top tasks | Take the day's orders after cut-off; build routes for about 600 delivery points; adjust the fixed routes; hand the route list to the warehouse and to Nuno [register; SCE5 card 4]. Consolidating loads to use vehicles fully is an O*NET logistics-analyst task (3.1) [practice] |
| 6 | What goes wrong | Late orders after cut-off; routes changed after picking has begun [register, SCE5, working]; drivers return with refused goods [register] |
| 7 | What they do about it | Re-plans and tells Ilse, team lead in chilled picking, which routes moved [register, SCE5, working] |
| 8 | What they would ask of the software | Which routes are already being picked, on the planning screen; fill per vehicle as the route is built; refused goods by route from the day before [working]. The features a routing product claims for her work: static, dynamic and real-time routing, territory planning, scenario modelling (Gartner VRS, 2) [analyst, the market's definition, no product meant] |
| 9 | Hands to and depends on | Depends on the order cut-off; hands routes to Ilse's team and to Nuno [register; SCE5] |

**Card 2 · Nuno, dispatcher, Ostrel Foods (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Nuno; dispatcher, handles the day's calls from drivers and customers; Ostrel Foods [register]; card set by SCE8 |
| 2 | Measured on | On-time delivery (SCE7 §11, the course's definition); refused goods per route [working] |
| 3 | Conditions | The delivery day, after the night's picking; calls from 40 drivers and from customers [register]; dispatchers may use radio, phone or computer to send assignments (O*NET 43-5032.00, 3.2) [practice] |
| 4 | Device | Phone and a desktop; whether he works in the routing tool is not in the register [working] |
| 5 | Top tasks | Answer drivers' calls; answer customers' calls; change stops during the day (SCE7 §8, reading of the register); record refusals and substitutions; monitor vehicles against the run schedule (O*NET, 3.2) [practice] |
| 6 | What goes wrong | Drivers returning with refused goods; substitutions agreed by phone and not recorded; paper delivery notes on some routes [register] |
| 7 | What they do about it | Takes it by phone, notes it, tells Sofia and the warehouse [working] |
| 8 | What they would ask of the software | A refusal or substitution entered by the driver at the door, on the route record; each vehicle's position against its stops; a change to a route that reaches the driver [working]. Dispatch and real-time routing are mandatory features of Gartner's VRS market (2) [analyst] |
| 9 | Hands to and depends on | Depends on Sofia's routes and on Ilse's shorts and substitutes (SCE5 register note); hands refusals back to the warehouse and to the customer [working] |

**Card 3 · The carrier representative who answers Tandric's tenders (fictional; not named in the register)**

| # | Field | Content |
|---|---|---|
| 1 | Who | The person at a road carrier who answers the loads Tandric's freight desk tenders; the register names no carrier staff, so the card carries no name [working]; card set by SCE8 |
| 2 | Measured on | By the party tendering: primary acceptance ratio and on-time pickup and delivery (SCE7 §§4, 11); weekly primary acceptance averaged 81.9% in a soft US truckload market and 68.5% in a tight one in the 2020 study (SCE7 §4) [independent]. By the carrier: not sourced |
| 3 | Conditions | Answers many customers at once, each through its own channel (5, reading); in the US at the end of 2023 about 53% of FMCSA-registered carriers had one power unit and about 90% ten or fewer (5) [independent, US only; the shares this unit's arithmetic] |
| 4 | Device | The carrier's own system receiving 204 tenders and returning 990 answers, or the tendering party's portal, or e-mail and phone (5) [working] |
| 5 | Top tasks | Accept or refuse each tender; agree a pickup time; send status (X12 214); send the invoice (X12 210) (3.3, 5) [independent for the messages; the tasks working] |
| 6 | What goes wrong | Tenders with short lead time (SCE7 §6, step 3); trucks waiting at the dock (SCE7 §9); invoices disputed for charges the system did not expect (SCE7 §6, step 10) |
| 7 | What they do about it | Refuses the load; charges detention; re-sends the invoice with proof [working] |
| 8 | What they would ask of the software | One way to answer every customer; tenders with enough lead time to plan a truck; the invoice's status visible after sending [working] |
| 9 | Hands to and depends on | Depends on Priya's tenders and Tandric's dock times [register: Priya tenders; Anke runs the site]; hands to the carrier's drivers and its own billing [working] |

**Card 4 · Priya, freight auditor, Tandric Logistics (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Priya; freight desk, tenders loads to carriers and checks their invoices; Tandric Logistics [register]. This card takes the invoice half of her job; the tender half is the planner's work at Tandric (3.1). Card set by SCE8 |
| 2 | Measured on | Invoice match rate (SCE7 §11, the course's, from Gartner's settlement capability); client invoices disputed (register: known trouble) [working] |
| 3 | Conditions | Desk work on both sides of every load: the carrier's bill to Tandric and Tandric's bill to the client [register; SCE7 deliverable B] |
| 4 | Device | Desktop: the transport system for the freight desk [register] |
| 5 | Top tasks | Match each carrier invoice (an X12 210 or a paper or PDF bill) to the tender and the rate; query extra charges (waiting, re-delivery); carry agreed extras to the client's invoice; release for payment (3.4, 5) [working]; computing shipment charges is an O*NET billing-clerk task (3.4) [practice] |
| 6 | What goes wrong | Invoices disputed because activity was not recorded [register]; detention or extra charges not passed on to the client (SCE7 deliverable B, row 10, reading) |
| 7 | What they do about it | Holds the invoice; asks the carrier for proof and the warehouse for dock times [working] |
| 8 | What they would ask of the software | The carrier's invoice matched against the tender and the rate on arrival; each accepted extra linked to a line on the client's invoice; the dock times on the load record (T12, T13, T22) [working] |
| 9 | Hands to and depends on | Depends on carriers' invoices and on dock times from Anke's site [register; working]; hands approved invoices to payment, which the register does not place, and client queries to Olu [working] |

**Card 5 · Olu, analyst (client reporting), Tandric Logistics (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Olu; client services, answers the clients' questions and sends their reports; Tandric Logistics [register]. The register has no transport analyst; this card treats the report work as the analyst's role at Tandric (3.5, this unit's reading). Card set by SCE8 |
| 2 | Measured on | Reports sent on time to each client; client questions answered [working]. The measures in the reports: on-time delivery and freight cost per unit (SCE7 §11); computing on-time delivery rates is an O*NET logistics-analyst task (3.5) [practice] |
| 3 | Conditions | Desk; nine clients, each wanting its own rules and reports [register] |
| 4 | Device | Desktop: the transport system and the client portal [register] |
| 5 | Top tasks | Build each client's freight report; answer tracking questions from the transport system and the portal (SCE7 deliverable B, row 7); analyse transportation costs (O*NET, 3.5) [practice] |
| 6 | What goes wrong | Each client wants its own reports [register]; the client asks before Tandric knows (SCE7 deliverable B, row 7) |
| 7 | What they do about it | Builds reports by hand for each client [working] |
| 8 | What they would ask of the software | A report defined once per client and run on a schedule; a portal view the client can read for itself; status events in the record before the client calls (T9, T20, T23) [working] |
| 9 | Hands to and depends on | Depends on Priya's checked costs and on carriers' status messages [register; working]; hands to the clients and to Karin, commercial director [register; working] |

### B. Shipper versus provider: the comparison table

The shipper side uses Ostrel Foods (own fleet) and Corvane (buys carriage through carriers' portals), both fictional; the provider side uses Tandric Logistics (fictional). A row marked "reading" is this unit's reading of the register and the sources named.

| # | Need | Shipper: Ostrel Foods, Corvane (fictional) | Provider: Tandric Logistics (fictional) | Where the needs pull apart | Basis |
|---|---|---|---|---|---|
| 1 | What freight is to the company | A cost: Ostrel's fleet costs its own vehicles, drivers and fuel; Corvane pays each carrier's rate | Revenue at a margin over what the carrier is paid | The provider watches margin per load; the shipper watches cost per unit | Register; SCE7 §8, §11 |
| 2 | Who is the system's customer | The shipper itself | Tandric; its nine clients use the data through the portal | The analyst counts Tandric once and its clients not at all | Gartner 2026 [analyst] (1) |
| 3 | Rates held | One side: carrier rates (Corvane), or none for Ostrel's own fleet | Two sides on every load: the client's price and the carrier's rate | The margin needs both in one record (T22) | SCE7 deliverable B, row 2; register |
| 4 | What a refused tender costs | A higher rate down the routing guide or on spot | The same, out of a fixed client price: the margin shrinks | The provider bears the backup premium unless the contract passes it on | SCE7 §4 [independent]; SCE7 deliverable B, row 4 (reading) |
| 5 | Rules and configuration | One company's rules | Each client wants its own rules and reports | Many configurations inside one system (T23) | Register |
| 6 | Onboarding | Once, at go-live | A new client expected live within weeks of signature; Luis configures each | Speed of setting up a client is a provider's measure | Register |
| 7 | Visibility, and for whom | For Ostrel's own customers, through Nuno; for Corvane's customers, through Jonas, from carriers' portals | For each client, through Olu and the portal | The provider sells visibility; shippers name control tower visibility a must-have from their 3PLs (68%, sponsored survey) | Register; SCE7 deliverable B, row 7; 3PL Study 2025 [vendor-reported] (4) |
| 8 | Invoice check | The carrier's invoice against the agreed rate (Corvane: in the ERP, a working placement); none for Ostrel's own fleet | The carrier's invoice against the tender, then Tandric's invoice to the client | Two invoices per load, and disputes on both | Register; SCE7 deliverable A row 10, B rows 9 and 10 |
| 9 | Paying and being paid | Pays carriers (Corvane) | Pays the carrier and is paid by the client | Cash timing between the two | SCE7 deliverable B, row 11 (reading) |
| 10 | Records the other party can see | In the US, a shipper using a broker is a party who may review the broker's record of the transaction | If Tandric is a broker in US law (a legal question), its record of each load, margin included, can be reviewed by the parties; a proposal would require electronic records within 48 hours | The provider's margin is visible on request; the shipper's costs are its own | FMCSA notice [practice] (4) |
| 11 | Fleet | Ostrel: own vehicles, routing and dispatch | No trucks; outside carriers only | The own-fleet shipper needs routing (T16, T17); the provider needs a carrier network (T18, T19) | Register; Gartner VRS [analyst] (2) |
| 12 | Contract horizon | With carriers, US truckload contracts usually last one to two years (SCE7 §3); Ostrel's and Corvane's are not in the register | With clients, two to three years | The provider's contract with the client outlasts its contracts with carriers (reading) | Register; Sheffi 2004 as read in SCE7 §3 [practice] |
| 13 | Analyst lens | The 2026 evaluation is written around shippers' needs | Read for a provider, the evaluation has no criterion named for client billing or many clients in the parts read | A provider translates a shipper's evaluation | Gartner 2026 [analyst] (1) |
| 14 | Technology spend | Not in the register | Not in the register; small Italian 3PLs reported low ICT spending and saw ICT as not aligned with their needs | Applying the Italian finding to Tandric is inference | Evangelista et al. 2013 [independent] (4) |
| 15 | Measures | Freight cost per unit, on-time delivery, primary acceptance (Corvane); routes built, vehicles used (Ostrel) | Margin per load: no public figure; invoice disputes; client report deadlines [working] | Different first numbers on the same screen | SCE7 §11; register; SCE5 card 4 |

### C. Halvern's transport line, mapped (fictional)

The form is SCE6's capability map (SCE6 deliverable A), six fields in its order; the capability lines are section 7's T1 to T24 (flag F62). Vendor: Halvern Systems (fictional). Line: Halvern Transport (core system) with modules Rating and Tendering, Fleet Routing, Tracking, Freight Audit and Claims; delivery by cloud subscription; implementation by its own services team and by partners (register). Source for every row: the case register, Halvern Systems (fictional), and SCE7 §5's placements (register, added by SCE7), read 27 November 2026. Grade for every row: **case**, the form value SCE6 set for a fictional vendor's register entry (flag F54; for a real vendor these rows would be vendor-reported). "Assumed" marks this unit's placement in the core, listed in the notes.

| # | Operation step | Capability | Module that claims it | Source and date | Grade | Gap or question |
|---|---|---|---|---|---|---|
| 1 | Buying capacity (SCE7 §3) | T1 Freight sourcing: bids, lanes, routing guide | No claim in the register | Case register, 27 Nov 2026 | case | Rating and Tendering holds rates; who runs the annual bid is open |
| 2 | 1 Plan (SCE7 §6) | T2 Order intake and shipment planning | Halvern Transport (core), assumed | Case register, 27 Nov 2026 | case | Takes orders from Halvern Order or from the warehouse's shipment record (SCE6 W22)? (SCE10) |
| 3 | 1 Plan | T3 3D load building | No claim in the register | Case register, 27 Nov 2026 | case | none |
| 4 | 2 Rate | T4 Rating | Rating and Tendering | Case register; SCE7 §5, 27 Nov 2026 | case | One rate side or two (T22)? |
| 5 | 3 Tender, 4 Answer | T5 Tendering and the carrier's answer | Rating and Tendering | Case register; SCE7 §5, 27 Nov 2026 | case | By X12 204 and 990, a portal, or both (T18, T19)? |
| 6 | 4 Answer (SCE7 §3) | T6 Routing-guide cascade to backups and spot | No claim in the register | Case register, 27 Nov 2026 | case | Inside Rating and Tendering? |
| 7 | 5 Book a dock | T7 Appointment and dock scheduling | No claim in the transport line; Halvern Warehouse lists Yard | Case register, 27 Nov 2026 | case | Which line's appointment wins (SCE7 §9; SCE10)? |
| 8 | Mode: parcel | T8 Parcel carrier selection and manifesting | No claim in the register | Case register, 27 Nov 2026 | case | Warehouse line or transport line (SCE6 row 22)? |
| 9 | 7 Track | T9 Tracking: status events | Tracking | Case register; SCE7 §5, 27 Nov 2026 | case | By X12 214, IFTSTA or a visibility platform? |
| 10 | 7 Track | T10 Predicted arrival times and alerts | No claim in the register | Case register, 27 Nov 2026 | case | Inside Tracking, or bought beside it (section 2)? |
| 11 | 8 Deliver | T11 Proof of delivery record | No claim in the register | Case register, 27 Nov 2026 | case | Tandric cannot bill a client without it (SCE7 deliverable B, row 8) |
| 12 | 9 Invoice | T12 Freight invoice intake | No claim in the register | Case register, 27 Nov 2026 | case | Inside Freight Audit? |
| 13 | 10 Check | T13 Settlement: expected against actual charges | Freight Audit | Case register; SCE7 §5, 27 Nov 2026 | case | none beyond the placement |
| 14 | 11 Pay | T14 Freight payment | Freight Audit, by SCE7 §5's placement | Case register; SCE7 §5, 27 Nov 2026 | case | The name claims audit; Halvern pays, or the ERP does? (SCE10) |
| 15 | 12 Claim | T15 Claims for loss, damage and delay | Claims | Case register; SCE7 §5, 27 Nov 2026 | case | Against carriers only, or a provider's client against the provider too (SCE7 deliverable B, row 12)? |
| 16 | Own fleet (SCE7 §8) | T16 Private fleet routing and scheduling | Fleet Routing | Case register; SCE7 §5, 27 Nov 2026 | case | none |
| 17 | Own fleet (SCE7 §8) | T17 Dispatch and same-day changes | No claim in the register | Case register, 27 Nov 2026 | case | Inside Fleet Routing? Nuno's work depends on it (card 2) |
| 18 | Carriers (section 5) | T18 Direct integration to carrier networks | No claim in the register | Case register, 27 Nov 2026 | case | Halvern's "One vendor for execution" names its own three lines, not carriers |
| 19 | Carriers (section 5) | T19 Portal for carriers without EDI | No claim in the register | Case register, 27 Nov 2026 | case | What a carrier with one truck does (card 3) |
| 20 | Reports (section 3.5) | T20 Transport analytics | No claim in the register | Case register, 27 Nov 2026 | case | Mandatory in Gartner's definition (section 1); in the core? |
| 21 | Reports (section 3.5) | T21 Transport modelling and forecasting | No claim in the register | Case register, 27 Nov 2026 | case | none |
| 22 | Provider (section 4) | T22 Client pricing and freight billing of clients | No claim in the transport line; Halvern Warehouse lists Client Billing, by activity | Case register, 27 Nov 2026 | case | Does Client Billing bill freight at a margin? Tandric needs it (deliverable B, rows 3, 8) |
| 23 | Provider (section 4) | T23 Many clients in one system | No claim in the register | Case register, 27 Nov 2026 | case | Halvern names logistics providers as customers; nothing in the register serves them in transport |
| 24 | Beside the system (section 2) | T24 Trade compliance | No claim; Halvern sells order, warehouse and transport only | Case register, 27 Nov 2026 | case | Bought from another vendor, if needed |

Below the table: seven lines claimed by a named module (rows 4, 5, 9, 13, 15, 16, and 14 by SCE7's placement); one placed in the core by assumption (row 2); sixteen with no claim in the register. For a shipper such as Corvane (fictional), the open lines that matter first are the dock (row 7), parcel (row 8) and invoice intake (row 12); for a provider such as Tandric (fictional), the two provider lines (rows 22, 23) and the carrier portal (row 19). The open questions for SCE10 are where the dock appointment, carrier labels and payment are held; for DD-SCE1, whether a suite that names logistics providers among its customers serves the provider's half of the record.

### D. Templates

**D1. The transport role card.** Copy one per role. Every line ends with its source in brackets: a section with its grade, "register", "observed" for what you saw yourself, or "working".

| # | Field | Fill in |
|---|---|---|
| 1 | Who | ______ (first name or role label; role: transport planner, dispatcher, carrier representative, freight auditor, analyst, or another; company; whether shipper, carrier or provider; region) |
| 2 | Measured on | ______ (each measure with whose definition: vehicle fill, cost per unit, on-time delivery, primary acceptance, invoice match, margin per load; "no public figure" for a private company's margin) |
| 3 | Conditions | ______ (hours and the day's rhythm: before cut-off, during delivery, month end; how many customers, carriers or clients at once) |
| 4 | Device | ______ (desktop, phone, the system and screen used; EDI, portal, e-mail or phone for each counterpart) |
| 5 | Top tasks | ______ (three to five, by time spent, each with the SCE7 §6 step number) |
| 6 | What goes wrong | ______ (the failures met most often, with the step where they start) |
| 7 | What they do about it | ______ (workaround, phone call, spreadsheet, escalation, and who else is involved) |
| 8 | What they would ask of the software | ______ (requests that follow from fields 2 to 7, each with the T line it touches; mark working until users confirm) |
| 9 | Hands to and depends on | ______ (roles upstream and downstream, inside the company, at carriers and at clients) |

**D2. Shipper versus provider.** One row per need; keep rows 1 to 15 and add rows the operation has.

Shipper: ______ (name; own fleet or bought carriage; region) · Provider: ______ (name; broker, forwarder or logistics provider in its own words; whether it owns vehicles) · Date filled: ______ · Sources: ______ (each with its grade)

| # | Need | Shipper | Provider | Where the needs pull apart | Basis |
|---|---|---|---|---|---|
| 1 | What freight is to the company | ______ (a cost: what it pays, per unit or per load) | ______ (revenue: how it is paid, margin or fee) | ______ (the first number each watches) | ______ (source and grade, or "register", "observed") |
| 2 | Who is the system's customer | ______ (who contracts with the vendor) | ______ (who contracts; who uses it through the provider) | ______ | ______ |
| 3 | Rates held | ______ (carrier rates; tariffs; none for own fleet) | ______ (client price and carrier rate) | ______ | ______ |
| 4 | What a refused tender costs | ______ | ______ | ______ | ______ |
| 5 | Rules and configuration | ______ | ______ (per client) | ______ | ______ |
| 6 | Onboarding | ______ | ______ (time to bring a client live) | ______ | ______ |
| 7 | Visibility, and for whom | ______ | ______ | ______ | ______ |
| 8 | Invoice check | ______ | ______ (carrier's and client's) | ______ | ______ |
| 9 | Paying and being paid | ______ | ______ | ______ | ______ |
| 10 | Records the other party can see | ______ (the rule and the body to ask) | ______ | ______ | ______ |
| 11 | Fleet | ______ | ______ | ______ | ______ |
| 12 | Contract horizon | ______ (with carriers) | ______ (with clients; with carriers) | ______ | ______ |
| 13 | Analyst lens | ______ (the report, date and how read) | ______ | ______ | ______ |
| 14 | Technology spend | ______ (published figure, or "no public figure") | ______ | ______ | ______ |
| 15 | Measures | ______ | ______ | ______ | ______ |

**D3. The transport capability map.** Fill one row per line for a real vendor's transport line, from its public pages, by the steps of SCE6 deliverable C. Keep the T IDs; add a row marked "new" for a claim the list lacks. Every bare blank in rows 2 to 24 and in the "new" row takes what row 1's blank in the same column says.

Vendor: ______ (name as on its pages) · Line: ______ (core product and modules, the vendor's names) · Customers its pages name: ______ (shippers, carriers, brokers, logistics providers) · Deployment the pages describe: ______ · Date filled: ______ · Pages read: ______ (each address with the date read)

| # | Operation step | Capability | Module that claims it | Source and date | Grade | Gap or question |
|---|---|---|---|---|---|---|
| 1 | Buying capacity (SCE7 §3) | T1 Freight sourcing: bids, lanes, routing guide | ______ (the module's name exactly as written, or "no public claim found") | ______ (page title, address, date read) | ______ (vendor-reported for the vendor's own pages) | ______ (version, deployment, shipper or provider, connection, boundary with another line) |
| 2 | 1 Plan | T2 Order intake and shipment planning | ______ | ______ | ______ | ______ |
| 3 | 1 Plan | T3 3D load building | ______ | ______ | ______ | ______ |
| 4 | 2 Rate | T4 Rating | ______ | ______ | ______ | ______ |
| 5 | 3 Tender, 4 Answer | T5 Tendering and the carrier's answer | ______ | ______ | ______ | ______ |
| 6 | 4 Answer | T6 Routing-guide cascade to backups and spot | ______ | ______ | ______ | ______ |
| 7 | 5 Book a dock | T7 Appointment and dock scheduling | ______ | ______ | ______ | ______ |
| 8 | Mode: parcel | T8 Parcel carrier selection and manifesting | ______ | ______ | ______ | ______ |
| 9 | 7 Track | T9 Tracking: status events | ______ | ______ | ______ | ______ |
| 10 | 7 Track | T10 Predicted arrival times and alerts | ______ | ______ | ______ | ______ |
| 11 | 8 Deliver | T11 Proof of delivery record | ______ | ______ | ______ | ______ |
| 12 | 9 Invoice | T12 Freight invoice intake | ______ | ______ | ______ | ______ |
| 13 | 10 Check | T13 Settlement: expected against actual charges | ______ | ______ | ______ | ______ |
| 14 | 11 Pay | T14 Freight payment | ______ | ______ | ______ | ______ |
| 15 | 12 Claim | T15 Claims for loss, damage and delay | ______ | ______ | ______ | ______ |
| 16 | Own fleet | T16 Private fleet routing and scheduling | ______ | ______ | ______ | ______ |
| 17 | Own fleet | T17 Dispatch and same-day changes | ______ | ______ | ______ | ______ |
| 18 | Carriers | T18 Direct integration to carrier networks | ______ | ______ | ______ | ______ |
| 19 | Carriers | T19 Portal for carriers without EDI | ______ | ______ | ______ | ______ |
| 20 | Reports | T20 Transport analytics | ______ | ______ | ______ | ______ |
| 21 | Reports | T21 Transport modelling and forecasting | ______ | ______ | ______ | ______ |
| 22 | Provider | T22 Client pricing and freight billing of clients | ______ | ______ | ______ | ______ |
| 23 | Provider | T23 Many clients in one system | ______ | ______ | ______ | ______ |
| 24 | Beside the system | T24 Trade compliance | ______ | ______ | ______ | ______ |
| new | ______ (the step it belongs to) | ______ (the vendor's claim, in your words) | ______ | ______ | ______ | ______ |

Below the table, count the lines claimed, the lines with no public claim found and the new lines; write which of the provider lines (22, 23) and carrier lines (18, 19) the pages claim; and write the open questions for the seams (SCE10). Write no price unless the vendor published it; otherwise "no public figure".

### E. Glossary lines

Added to the working glossary of SCE1 to SCE7.

| Term | Working definition | Region | Source |
|---|---|---|---|
| Transportation management system (TMS), 2026 evaluation | Software for multimodal sourcing, planning and execution of transport, with visibility, settlement and embedded analytics as mandatory features | Both | Gartner 2026 [analyst] |
| Mandatory and common features | In a Gartner evaluation, what every product must have, and what many have without being required | Both | Gartner 2026 [analyst] |
| Shipper | A company whose goods move, for which freight is a cost | Both | SCE1; this unit (4) |
| Logistics provider; broker | A company that arranges freight for others and earns on each load; in US law a broker arranges motor carriage for compensation | US legal term (broker); both | 49 U.S.C. §13102(2) as read in SCE7 [independent]; register |
| Fourth-party logistics provider (4PL) | In one textbook's terms, a non-asset-based provider that mainly supplies organisational expertise | Textbook usage | Rodrigue, 6th ed., ch. 7 [practice] |
| Real-time transportation visibility platform (RTTVP) | Software giving real-time location and status of orders once they have left the warehouse, with alerts and predicted arrival times | Both | Gartner Peer Insights, March 2025 [analyst] |
| Freight audit and payment (FAP) | Services of invoice collection, preaudit, processing, payment and analytics of transport invoices | Both | Gartner Peer Insights [analyst] |
| Vehicle routing and scheduling (VRS) | Software that builds a fleet's routes and schedules under constraints, with dispatch | Both | Gartner Peer Insights, July 2026 [analyst] |
| Control tower | A platform integrating real-time data with analytics and organisational knowledge (one study's definition); a selling term with no agreed reach | Both | Staudt et al. 2026 [independent] |
| Transport planner | The person who turns orders into shipments or routes and chooses mode and carrier | Both | Working; Gartner planning [analyst] |
| Dispatcher | The person who runs the day's vehicles and changes the plan as calls come in | Both; O*NET is US | O*NET 43-5032.00 [practice] |
| Carrier representative | The carrier's person who answers tenders, sends status and bills | Both | Working |
| Freight auditor | The person who checks carrier invoices against what was agreed | Both | Working; Gartner settlement [analyst] |
| Transportation analyst | The person who turns the transport record into measures and recommendations | Both; O*NET is US | O*NET 13-1081.02 [practice] |
| X12 204, 990, 214, 210 | Load tender; response to a load tender; carrier shipment status; carrier freight invoice | Published by X12; regional use not sourced | X12 [independent]; SCE7 for 990 |
| Power unit | A truck or tractor counted in a carrier's fleet | US statistics | FMCSA pocket guide [independent]; definition the course's gloss |
| Capability line (T1 to T24) | One transport function on the course's list, used in a capability map | This course | This unit, section 7 |

## Sources

All addresses opened on 27 November 2026; the source log (sources.md) gives what was read at each.

- APQC. "Total Cost to Operate Outbound Transportation per $1,000 in Revenue". Undated. https://www.apqc.org/knowledge-base/documents/total-cost-operate-outbound-transportation-1000-revenue
- Evangelista, P., McKinnon, A. & Sweeney, E. (2013). Technology adoption in small and medium-sized logistics providers. *Industrial Management & Data Systems* 113(7), 967–989. https://doi.org/10.1108/IMDS-10-2012-0374 (author's manuscript read at https://publications.aston.ac.uk/id/eprint/22288/1/Technology_adoption_in_small_and_medium_sized_logistics_providers.pdf; record at https://research.aston.ac.uk/en/publications/technology-adoption-in-small-and-medium-sized-logistics-providers/)
- Gartner. "Magic Quadrant for Transportation Management Systems". B. Johns, O. Sanchez Duran, M. Jain. 30 March 2026, ID G00832918. Reprint. https://lp.shipsy.ai/hubfs/Shipsy%20Content%20Library/Gartner/Gartner%20MQ%20TMS%202026.pdf
- Gartner. Glossary, "TMS (transportation management system)" (no headline shown). Undated. https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/tms-transportation-management-system
- Gartner Peer Insights. "Freight Audit and Payment Providers Reviews and Ratings". No features date shown. https://external.pi.gpi.aws.gartner.com/reviews/market/freight-audit-and-payment-providers
- Gartner Peer Insights. "Real-Time Transportation Visibility Platforms Reviews and Ratings". Features updated March 2025. https://www.gartner.com/reviews/market/real-time-transportation-visibility-platforms
- Gartner Peer Insights. "Transportation Management Systems Reviews and Ratings". Features updated April 2026. https://www.gartner.com/reviews/market/transportation-management-systems
- Gartner Peer Insights. "Vehicle Routing and Scheduling Reviews and Ratings". Features updated July 2026. https://www.gartner.com/reviews/market/vehicle-routing-and-scheduling
- MIT Center for Transportation & Logistics. "FreightLab". Undated. https://ctl.mit.edu/research/freightlab
- Novack, R. A., Gibson, B. & Coyle, J. J. *Transportation: A Global Supply Chain Perspective*, 9th edition. Cengage, 2019. ISBN 9781337406642. Publisher's page, contents only. https://cengage.com/c/new-edition/9781337406642
- NTT DATA and Penske Logistics (sponsors). *2025 Third-Party Logistics Study*: "Navigating Change: Insights Into Evolving Dynamics in Supply Chain". https://us.nttdata.com/en/-/media/nttdataamerica/files/gated-asset/1555533-NTT-DATA-3PL-Study-2025.pdf
- O*NET OnLine, US Department of Labor. "Billing and Posting Clerks", 43-3021.00. Updated 2026. https://www.onetonline.org/link/summary/43-3021.00
- O*NET OnLine. "Cargo and Freight Agents", 43-5011.00. Updated 2026. https://www.onetonline.org/link/details/43-5011.00
- O*NET OnLine. "Dispatchers, Except Police, Fire, and Ambulance", 43-5032.00. Updated 2026. https://www.onetonline.org/link/summary/43-5032.00
- O*NET OnLine. "Freight Forwarders", 43-5011.01. Updated 2026. https://onetonline.org/link/details/43-5011.01
- O*NET OnLine. "Logistics Analysts", 13-1081.02. Updated 2026. https://www.onetonline.org/link/details/13-1081.02
- Rodrigue, J.-P. *The Geography of Transport Systems*, 6th edition. Routledge, New York, 2024. ISBN 9781032380407. Chapter 7: "7.4 – Logistics and Freight Distribution" and "Key Drivers for Third and Fourth Party Logistics Providers". https://transportgeography.org/contents/chapter7/logistics-freight-distribution/ ; https://transportgeography.org/contents/chapter7/logistics-freight-distribution/3pl-4pl-logistics/
- Staudt, F. H., Lopes, E. de J., Corrêa, A. C., Bouzon, M. & Di Mascolo, M. (2026). Supply chain control tower implementation: overcoming challenges and driving success in large multinational companies. *Production* 36, e20250126. https://doi.org/10.14488/1980-5411.20250126 (full text read at https://scielo.br/j/prod/a/99Lvbdfx9npmc998DYb57yc/?lang=en)
- US Federal Motor Carrier Safety Administration. *2024 Pocket Guide to Large Truck and Bus Statistics*, RRC-24-002, July 2025. https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/FMCSA%20Pocket%20Guide%202024-v6%20508%20.pdf
- US Federal Motor Carrier Safety Administration. "[Docket No. FMCSA-2023-0257] RIN 2126-AC63 Transparency in Property Broker Transactions". Notice of proposed rulemaking, undated page. https://www.fmcsa.dot.gov/regulations/docket-no-fmcsa-2023-0257-rin-2126-ac63-transparency-property-broker-transactions
- X12. "204: Motor Carrier Load Tender". Undated. https://x12.org/node/4207
- X12. "210" (Motor Carrier Freight Details and Invoice). Undated. https://x12.org/node/4210
- X12. "214" (Transportation Carrier Shipment Status Message). Undated. https://x12.org/node/4214

## Unsure list

claude-opus-5-5

# Unsure: SCE8

1. Gartner's 2026 TMS Magic Quadrant was read in a vendor-posted reprint through a fetch tool, in passes; the 16 vendor names, the thresholds (50 customers, $10 million, 20%, seven industries, 10 outside the home region, 31 October 2025) and all quotations come from that extraction and were not re-read against a second copy; the graphic did not render.
2. That the 2026 report names no "tender", "rating" or "payment" outside vendor profiles rests on the fetch tool's keyword search of the reprint, not on a line-by-line reading.
3. Gartner's glossary TMS entry was read at gcom.pdo.aws.gartner.com, a gartner.com subdomain, and is undated; that it matches the www.gartner.com glossary was not confirmed.
4. The freight audit and payment market page was read at external.pi.gpi.aws.gartner.com and showed no features date; its definition sentence was given in part by the extraction.
5. The *2025 Third-Party Logistics Study*: the total number of respondents was not found in the text read; the percentages (68%, 54%, 53%, 55%, 87%) are from the extraction; an "82%" outsourcing figure seen in one pass could not be confirmed in the second and is not used.
6. FMCSA's broker-transparency notice: whether the proposal became a final rule was not checked, and the current text of 49 CFR §371.3 was not read directly; the unit states only the agency's account.
7. FMCSA pocket guide: the fleet-size figures cover all carrier types, not interstate freight carriers alone; the 53% and 90% shares are this unit's arithmetic; graded independent as official registration statistics, which could be graded practice if F18 is decided that way.
8. Staudt et al. (2026): that two of the three companies lacked real-time tracking or visibility layers, and that end-to-end management was not identified in the cases, come from the extraction of the SciELO full text, whose reference list was truncated.
9. O*NET: the dispatcher summary page showed 5 of 12 tasks; quotations from all five O*NET pages are from the extraction.
10. Evangelista, McKinnon & Sweeney (2013) was read in the author's manuscript; the 38% track-and-trace figure and "customers did not demand it" were not compared with the published version.

Object: none

Fresh check 2026-11-27 (claude-opus-5-5): fix · 1 errors, 4 should-fix, 11 minor; report `audits/supply-chain-execution/fresh-check-SCE8.md`
