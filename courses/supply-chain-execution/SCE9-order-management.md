---
code: SCE9
title: Order management
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-27
search: on
intro: How a promise to a customer is made and kept across locations, and who works the orders: where orders come from; availability across warehouses, stores and stock in transit; the promise as a date and a place, with the US and EU delivery rules; sourcing, splits, backorders and substitutions; collect in store and ship from store; what sharing availability with customers was found to do; changes, cancellations and returns; the four order roles; the analyst definition of distributed order management; Halvern's (fictional) order line on the lifecycle and on capability lines O1 to O25; the vendors of Gartner's November 2026 evaluation as a dated list. Deliverable: the order lifecycle map for a Corvane (fictional) web order shipped from a store, in SCE7's form; four order role cards on Corvane's staff; Halvern's order line in SCE6's capability map form; three templates; glossary lines. How it was made: written 27 Nov 2026 by Opus 5.5 with live search, then a fresh check, a quality review and three applier rounds, each a fresh Opus 5.5 agent; Hübner, Holzapfel and Kuhn's page numbers were re-read by an applier against the printed page heads. The unit is long: more than 16,000 words. Known gaps: Gartner's two November 2026 reports were read only as abstract pages; Acimovic and Graves (2015), Xu, Allgor and Graves (2005), Gallino and Moreno (2014, at a bibliographic index after the publisher refused), Ishfaq et al. (2016) and Cui et al. (2024) were read in abstract only, and Hoang and Breugelmans (2023) to about three-quarters of its length. Not opened: Xu, Allgor and Graves (2009), the publisher's copy of Gallino and Moreno, the full text of Acimovic and Graves, the US rule's text (16 CFR Part 435), Article 13 of the EU consumer rights directive, Directive (EU) 2024/825, the EFTA record of Directive (EU) 2023/2673 and a university summary of Cui et al. Directive (EU) 2023/2673 was read in the Council's text as adopted (PE-CONS 37/23), not in the Official Journal, because the EUR-Lex pages came back empty. Sections 2 to 4 and 8, on availability, the promise, sourcing rules and order states, rest on practice and the course's working description where the research is silent; no textbook account of order management was opened. Kellogg Insight, the school's staff-written account of Gallino and Moreno's study, is kept as the source of the study's setting until the owner decides whether it may stand. Two of the four role cards name people (Lena, Oskar) this unit adds to the case register.
---

# SCE9 · Order management

SCE1 drew the order system at the top of the map: take the order, promise, source. This unit opens those three steps up and follows the order to the customer's door and back. Grades follow SCE1's key (section 10 there): every claim that carries a number, a mechanism or a recommendation ends with [independent], [analyst], [vendor-reported] or [practice]. A public authority's own account of a rule is graded practice, as SCE7 grades it, until flag F18 is decided; the text of a standard or a law is graded independent for what it says. Lines marked as this unit's inference or reading, or as working descriptions, carry no grade; they rest on the graded sources they name. Every reference was opened on 27 November 2026; the source log (sources.md) gives what was read at each.

Two limits hold through the unit. Order management has less research behind it than warehousing or transport, and much of this unit rests on the course's working description, with no source behind it: where a section does, it says so. And the analyst evaluation of this market, Gartner's *Magic Quadrant for Distributed Order Management* of 12 November 2026, was read only as its abstract page; the unit states nothing about it beyond what that page states.

The unit uses twelve steps for one order, numbered so that the deliverable and SCE10 can refer to them:

1. **Take the order.** 2. **Check availability.** 3. **Promise.** 4. **Source.** 5. **Release to the location.** 6. **Pick.** 7. **Pack and label.** 8. **Hand over** (to a carrier, or to the customer at a counter). 9. **Track and inform.** 10. **Deliver.** 11. **Return.** 12. **Refund.** A change or cancellation (row C in the deliverable) can arrive at any step before 8.

Steps 1 to 4 refine SCE1's first three map steps. At a distribution centre, steps 5 to 8 are SCE3's outbound steps (release to staging and loading); steps 8 to 10 are SCE7's steps 6 to 8 (pick up, track, deliver). This is the course's own sequence; no source opened sets out an order lifecycle in these terms.

## 1. Where orders come from

**The channels.** An order reaches the order system from one of four places, in this course's working list: a **website** (the retailer's own online shop), a **store** (a customer at a till, or a store associate placing an order for a customer), a **marketplace** (a third party's online shop on which the retailer sells, which passes the order on; no source on marketplace orders was opened, so this is a working definition) and a **business customer** (a company buying for its own use or for resale). Corvane (fictional), a fashion retailer, has 60 stores in four European countries and one website, with an order system for the website (case register). Ostrel Foods (fictional), a food distributor, takes orders by phone, by a web shop and from its sales staff, with a cut-off in the late afternoon (case register).

**Consumer and business orders.** The trade shorthand is **B2C** (business to consumer) and **B2B** (business to business). Gartner's companion report to its 2026 evaluation of distributed order management evaluates 14 vendors "across five use cases"; its abstract page lists, without labelling them, five headings that read as those use cases: B2B (Other), B2B (Wholesale/Distribution/CPG), B2B + B2C, E-Commerce, and Unified Commerce ([Gartner, *Critical Capabilities for Distributed Order Management*, 12 Nov 2026, abstract](https://www.gartner.com/en/documents/8631633)) [analyst, abstract only]. (CPG is consumer packaged goods.) The evaluation's own abstract says "A convergence across B2B and B2C channels is shaping the current market" ([Gartner, *Magic Quadrant for Distributed Order Management*, 12 Nov 2026, abstract](https://www.gartner.com/en/documents/8617033)) [analyst, abstract only]. The abstract does not say what converges.

**The business order as a document.** A business order is usually a **purchase order** (PO): the buyer's document stating what it orders, at what price, for delivery where and when. Business partners can exchange it by **electronic data interchange** (EDI), structured messages sent system to system. Two standards publish these messages:

- **X12**, a standards body (which regions use its messages was left unsourced by SCE7 and SCE8, and is here). Its 850 transaction set "establishes the data contents of the Purchase Order"; it is not to be used for purchase order changes or acknowledgments ([X12, 850](https://x12.org/node/4392)) [independent, for what the standard says]. The supplier answers with an 855, which "acknowledges each line item": each line accepted, accepted with a change (price, a rescheduled date, a reduced quantity, a substituted product) or rejected; the buyer answers changes with an 860 change request, accepting them or cancelling ([X12, Example 02: Purchase Order Acknowledgment with Minor Changes](https://x12.org/examples/004010x358/example-2-purchase-order-acknowledgment-minor-changes)) [independent, for what the published example shows].
- **GS1's EANCOM** (whether EANCOM is a subset of UN/EDIFACT was left unverified by SCE7, and is here). Its ORDERS message specifies goods ordered "under conditions agreed between the seller and the buyer"; GS1 recommends one purchase order per delivery, location and time, and allows deliveries to several locations in one order, which it calls split deliveries, as well as blanket orders, call-offs and rush orders ([GS1, EANCOM 2002 S3, ORDERS](https://gs1.org/sites/gs1/files/docs/eancom/ean02s3/part2/orders/intro.htm)) [independent]. The response, ORDRSP, can show the supplier's acceptance "of all, or part, or none" of the order and the changes it needs, which the buyer acknowledges with a new order referring to the original ([GS1, EANCOM 2002 S3, ORDRSP](https://gs1.org/sites/gs1/files/docs/eancom/ean02s3/part2/ordrsp/intro.htm)) [independent].

**How the two differ**, as this unit's reading of the sources above, with the course's working terms:

| | Consumer order (B2C) | Business order (B2B) |
|---|---|---|
| Arrives as | A website or marketplace checkout, a store till, a phone call | A purchase order: EDI (X12 850, EANCOM ORDERS), a portal, e-mail, phone or a sales representative |
| Size | Few lines; Corvane's web orders are one to three items (register) | Many lines; a store order "might comprise hundreds or thousands of items" (Bartholdi and Hackman, as read in SCE1 §5) [practice] |
| Answer to the customer | A confirmation and a promised date (section 3) | A line-by-line acknowledgment: accepted, changed, rejected (X12 855; EANCOM ORDRSP) [independent] |
| Price | The published price at checkout | Agreed terms between buyer and seller (EANCOM ORDERS) [independent]; the price can change in the acknowledgment (X12 855) [independent] |
| Payment | At or before shipment, typically by card (working) | On invoice and credit terms (working; no source opened) |
| Changes | The consumer cancels or returns (sections 8, 9) | The supplier proposes changes and the buyer accepts or cancels (X12 855 and 860) [independent] |
| Delivery | One address, or a store for collection | One or several locations, call-offs against a blanket order (EANCOM ORDERS) [independent] |
| Rules that protect the buyer | Consumer law (sections 3, 9) | The contract between the parties (working; a legal question for counsel) |

**What the system does at this step.** Takes in the order, checks it for completeness, and records it with its channel. O*NET, the US Department of Labor's occupational database, lists among an order clerk's tasks to "Review orders for completeness" and to verify customer and order information ([O*NET, Order Clerks, 43-4151.00, updated 2026](https://onetonline.org/link/summary/43-4151.00)) [practice]. **Common failure:** an order that arrives by phone or e-mail and is keyed by hand, or not recorded at all; Ostrel's substitutions agreed by phone and not recorded are the register's case (case register). **Measure:** no source opened defines an order-capture measure; the course's working one is orders keyed by hand over all orders.

## 2. Availability: what can be sold, and where it is

**The terms.** **Available-to-promise** (ATP) is the quantity that can still be committed to new orders; **available-to-ship** is the quantity that can leave now (SCE1 glossary: the terms are named in Gartner's definition; the definitions are the course's). Gartner's market definition makes "Enterprise Inventory for available-to-promise and available-to-ship items in the supply chain" a mandatory feature of distributed order management, with inventory allocated on the basis of on-hand, in-process or in-transit stock ([Gartner Peer Insights, "Distributed Order Management Systems (Transitioning to Distributed Order Management) Reviews and Ratings", mandatory features updated July 2025](https://www.gartner.com/reviews/market/distributed-order-management-systems)) [analyst]. **On-hand** stock is on a shelf now; **in-process** stock is being received, moved or packed; **in-transit** stock is on its way between locations, from a supplier or to a store (working definitions; the page names the three without defining them).

**The physical event.** None: availability is a calculation over records held elsewhere. At Corvane, stock sits in one distribution centre and in 60 stores, and a web order can be filled from either (case register, added from the Supply Chain Planning course).

**What the system does**, as working description: it adds up each item's records by location (the warehouse system's for the centre, each store's for the shelves, open purchase orders and transfers for stock on its way), subtracts what is already promised to open orders, and offers the rest to the website. A system can also hold back a quantity at each location so that a few miscounted units do not become broken promises. No source opened describes or tests such a reserve, so the course calls it an **availability buffer** and treats it as a working term.

**How it commonly fails.** Availability is only as good as the location records under it. Corvane's known trouble is web orders promised from stock the centre cannot find (case register); SCE4 §9 follows one such error from **phantom stock** (units the record shows and the shelf does not hold) to a broken promise. In the research SCE4 opened, store studies found 31% to 65% of records wrong, on different definitions, and no study reported a comparable share for a warehouse, so store and warehouse records cannot be ranked from it (SCE4 §10, as SCE1 C4 summarises it) [independent]. In one study of omni-channel retailers (retailers whose store and distance channels overlap from the customer's point of view; in multi-channel retailing they do not, and the channels are not physically linked: Hübner, Holzapfel & Kuhn's definition, 2016, p. 258) in German-speaking countries, fashion retailers explained that their many sizes and colours leave few units of each in a store, that items are tried on or put in baskets, and that misplaced items are hard to find ([Hübner, Holzapfel & Kuhn, 2016, p. 279](https://doi.org/10.1007/s40685-016-0034-7)) [independent: interviews, see section 4 for the design]. The same study names real-time access to store inventory among what store fulfilment requires (p. 279) [independent]. So a store's record is a weak base for a promise: the store studies found between a third and two-thirds of their records wrong, and Hübner et al.'s fashion retailers gave reasons why (this unit's inference from SCE4 and Hübner et al.; no study opened compares store and warehouse records on one measure).

**Measure.** No source opened defines an availability measure. The course's working measure is the **promise failure rate**: lines promised that could not be filled from the location chosen, over all lines promised. Gartner's definition ties the system to "targeted service levels for order fill rate" (Peer Insights DOM page) [analyst]; **order fill rate**, orders filled completely as a share of all, is APQC's measure (SCE3 §12) [practice].

## 3. The promise: a date and a place

**What is promised.** A promise has two parts: a **date** (or a window) and a **place** (an address, or a store for collection). The system computes the date from where the goods are, the time to pick and pack there, the location's **cut-off** (the latest order time that still makes the day's departure; SCE3 §8) and the carrier's transit time (working description; no source opened sets out the calculation).

**What the research found about the promise itself.** Cui, Lu, Sun and Golden worked with an online retailer selling customised photo products across the United States: they varied the delivery estimates shown on the site while keeping physical delivery speed unchanged, and compared outcomes by difference-in-differences (the change in outcomes where the estimates were changed set against the change, over the same period, where they were not; the abstract does not say how the two were formed). A faster promise raised sales and profits; it also raised product returns and lowered customer retention ([Cui, Lu, Sun & Golden, 2024, abstract](https://doi.org/10.1287/msom.2021.0174)) [independent: one retailer, one product category; abstract only, which gives no effect sizes]. The promise is therefore a lever with a cost on both sides (this unit's reading of the abstract). Applying the finding to fashion or to Corvane is this unit's inference.

**What the rules say, by region.** Where an operation sells to consumers, the law sets a floor under the promise.

- **United States.** The Federal Trade Commission's guide to its Mail, Internet, or Telephone Order Merchandise Rule says a seller must have a reasonable basis for any shipping time it states or implies, and, if it states none, a reasonable basis to expect shipment within 30 days (50 days where the buyer applies for the seller's own credit); if it cannot ship on time it must seek the buyer's consent to the delay, giving a revised date and explaining how to cancel; a required refund must be prompt and full, within seven working days for most payment methods, and store credit cannot replace it; the rule requires no records, but the seller bears the burden of proving it complies ([FTC, "Business Guide to the FTC's Mail, Internet, or Telephone Order Merchandise Rule", September 2011, edited January 2025](https://ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule)) [practice: the agency's account; the rule's text, 16 CFR Part 435, was not opened]. The guide does not say whether business buyers are covered.
- **European Union.** The consumer rights directive requires the trader to deliver "not later than 30 days from the conclusion of the contract", unless the parties agreed otherwise; if it does not, the consumer calls on it to deliver within an additional period appropriate to the circumstances, and if it still does not, may terminate the contract and be reimbursed without undue delay (Directive 2011/83/EU, Art. 18(1) to (3), [legislation.gov.uk's copy](https://www.legislation.gov.uk/eudr/2011/83/article/18), corresponding to the consolidated text of 1 July 2018) [independent, for what the text says]. That copy applies no amendment made after 31 December 2020. The European Commission lists three amending directives: Directive (EU) 2019/2161, in application from 28 May 2022; Directive (EU) 2023/2673, from 19 June 2026; and Directive (EU) 2024/825, which the page says "will enter into application on 27 September 2026" ([European Commission, "Consumer rights directive"](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en?prefLang=fr), read 27 Nov 2026) [practice]. Directive 2019/2161 inserts an Article 9(1a), under which Member States may extend the 14-day withdrawal period to 30 days for contracts concluded during a trader's unsolicited visit to a consumer's home or an excursion the trader organises, amends Article 9(2) to match, and does not amend Article 18 (Directive (EU) 2019/2161, Art. 4(8), [legislation.gov.uk's copy](https://legislation.gov.uk/eudr/2019/2161/article/4/adopted/data.pdf)) [independent, for what the text says]. Directive 2023/2673 does not amend Articles 9 or 18; its Article 1(3) inserts an Article 11a under which, "for distance contracts concluded by the means of an online interface", the trader provides a withdrawal function labelled "withdraw from contract here" or an "unambiguous corresponding formulation", "continuously available throughout the withdrawal period" (Directive (EU) 2023/2673, Art. 1(3), read in the text as adopted by the European Parliament and the Council, [PE-CONS 37/23, Council of the European Union, 11 October 2023](https://data.consilium.europa.eu/doc/document/PE-37-2023-INIT/en/pdf), not in the Official Journal text, which EUR-Lex returned as an empty page on 27 Nov 2026) [independent, for what the text says]. The Commission page gives its application from 19 June 2026 [practice]. Whether Directive 2024/825 changes Articles 9 or 18 was not confirmed on 27 Nov 2026 (not opened). Member States transpose a directive into national law; the national text was not opened.

Which rule binds a given operation, and what it requires of the order record, is a question for the operation's legal advisers and the national consumer authority. What both sources ask of the software, as this unit's reading: a promised date with a basis behind it, a record of when the promise was made and changed, and a way to tell the customer of a delay and to cancel and refund.

**What makes the promise wrong**, step by step, as this unit's reading of earlier units:

| Cause | Where it starts | Evidence |
|---|---|---|
| The stock is not where the record says | Step 2, availability | SCE4 §§4, 9 [independent for store record accuracy]; Corvane's known trouble (register) |
| The order misses the location's cut-off | Step 5, release | SCE3 §8 (cut-offs) [practice] |
| The store does not pick in time, or declines the order | Steps 5 to 7, at a store | Hübner et al. 2016 on in-store picking [independent]; Corvane's store staff have no process (register) |
| The carrier refuses or runs late | Steps 8 to 10 | SCE7 §§4, 10 [independent for US truckload refusals; no parcel source] |
| The promise was set faster than the operation runs | Step 3 | Cui et al. 2024, abstract [independent] |

**Measure.** The course's working **promise accuracy**: orders delivered (or ready for collection) by the promised date, over all orders. SCE7 §11's on-time delivery is the carrier's share of it. APQC's perfect order counts on-time delivery as one factor (SCE3 §12) [practice].

## 4. Sourcing: choosing the location that ships

**The decision.** **Sourcing** (in order management, also called order routing or allocation) chooses which location fills each line of an order. Gartner's definition makes "Order Orchestration that optimizes order routing and inventory allocation" mandatory, and describes it as determining "the best fulfillment location based on service level and cost components", using business rules configured in a hierarchy (the page's definition paragraph) so that fulfilment can be optimised by "channels, consumers, geographies and other criteria" (Peer Insights DOM page, July 2025) [analyst]. The page does not list the rules.

**The rules**, as the course's working list; no source opened lists them, so this is the course's working description, with no source behind it: exclude locations that cannot ship the item or the delivery method; prefer a location that holds every line, to avoid a split, and, for a centre-first retailer, try the distribution centre before any store; prefer the nearest location to the address, or the cheapest to ship from; protect a store's last units, or its display stock; cap how many orders a store takes a day; and break ties by stock level or by the date stock is expected.

**What the research on online fulfilment decisions found.**

- **Cost now against cost later.** Acimovic and Graves, working with an online retailer, frame the decision as where each item ships from, by which shipping method, and whether a multi-item order is split. A rule that takes the cheapest option for each order ignores what that choice does to the stock left for later orders. Their heuristic adds to the immediate outbound shipping cost an estimate of future shipping costs, taken from the dual values of a transportation linear program; on industry data it captured 36% of the gap to a clairvoyant benchmark (one that knows all future orders), for outbound shipping costs about 1% lower, with no loss of customer service and no rise in holding cost, and the partner implemented it across its North American stock-keeping units after a pilot ([Acimovic & Graves, 2015, abstract](https://doi.org/10.1287/msom.2014.0505)) [independent: one retailer's data; abstract only].
- **Reconsidering the decision.** An earlier MIT working paper with Graves as co-author calls real-time assignment of orders to fulfilment centres or drop shippers "necessarily myopic", because it cannot see future orders or replenishments, and studies re-evaluating assignments periodically with heuristics that minimise the total number of shipments, tested on a major e-tailer's data ([Xu, Allgor & Graves, 2005, MIT IMST working paper, abstract](https://dspace.mit.edu/handle/1721.1/7443)) [practice: a working paper; its 2009 journal version could not be opened]. A **drop shipper** is a supplier that ships direct to the retailer's customer.
- **Where retailers ship from.** In Hübner, Holzapfel and Kuhn's exploratory study of 28 omni-channel retailers (non-food, headquartered in German-speaking countries; 43 managers interviewed over about six months, plus five logistics providers), nearly three-quarters supplied store and customer orders only through distribution centres, nine of ten used one central centre for online orders, and about one-tenth regularly shipped online orders from stores; integrated centres (one stock for stores and online) and separate ones were equally common (2016, pp. 267–268, 274, 277–278) [independent: interviews, 28 retailers, one region, not quantified by design]. Ishfaq, Defee, Gibson and Raja, from 50 interviews with supply chain executives of large retailers and secondary data, found online sales, the size of the distribution network, sales associates per store and years in online retail strongly associated with the fulfilment method a retailer used, and retailers with large store networks integrating store and centre inventory ([2016, abstract](https://doi.org/10.1108/IJPDLM-02-2015-0032)) [independent: an association; abstract only].

**The trade-offs**, as this unit's inference from these sources and SCE4 §9:

- **Cost against speed.** The nearest location ships fastest; the deepest stock or the cheapest rate may be further away. Acimovic and Graves add a third term: what this order's choice costs later orders.
- **Splitting.** A **split shipment** sends one order in more than one delivery (SCE4 glossary). It can keep the promise date when no single location holds every line, at the cost of two shipments, and the customer receives two parcels at two times (SCE4 §9).
- **Store against centre.** A store is close to the customer, holds a record the store studies found often wrong (section 2), and is a less efficient place to pick than a centre in Hübner et al.'s account (section 6).

Corvane's sourcing decision for one web order, drawn from the working rules above:

```viz
{"kind": "decision", "title": "Which location fills a web order (working rules)", "root": {"q": "Can the distribution centre fill every line by the promised date?", "tone": 3, "branches": [{"label": "yes", "to": {"outcome": "Ship from the centre: one parcel", "tone": 2}}, {"label": "no", "to": {"q": "Can one store fill every line, within its daily cap?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "Ship from that store", "tone": 5}}, {"label": "no", "to": {"q": "Can the lines be split across locations?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "Split shipment: two parcels", "tone": 1}}, {"label": "no", "to": {"outcome": "Backorder, substitute or cancel the line", "tone": 6}}]}}]}}]}, "caption": "The course's working sourcing rules of section 4 of this unit, applied in the order a centre-first retailer might set them. No source opened lists sourcing rules; the split as a decision is from Acimovic and Graves (2015, abstract) and SCE4 section 9. Case: Corvane (fictional)."}
```

**What the system does.** Applies the rules to each line, records the location chosen and the reason, and sends the line to that location (step 5). **Common failure:** the rule picks a store whose record shows a unit the shelf does not hold, and the line comes back (sections 2 and 6). **Measure:** the course's **split rate**, orders sent in more than one shipment over all orders, and **outbound shipping cost per order**, the measure Acimovic and Graves's heuristic lowered [independent, abstract].

## 5. Backorders and substitutions

When no location can fill a line by the promised date, the order system has three answers: wait, offer something else, or cancel the line.

**Backorder.** A **backorder** is an ordered line waiting for stock (SCE4 glossary); WERC, the warehousing benchmark association, names backorders as a percentage of total lines among its survey measures (SCE3 §12, SCE4 §10) [practice]. For a consumer order, a backorder is a delay to the promise, and the rules of section 3 apply: in the FTC's account, the seller seeks the buyer's consent to the delay and offers cancellation with a prompt refund [practice]; under the EU directive, delivery after 30 days or the agreed date opens the consumer's route to termination (Art. 18) [independent]. For a business order, the supplier reports the change in its acknowledgment: in X12's published example a line is "accepted but the quantity has been changed (reduced)" or accepted with its required-by date rescheduled, and the order is held until the buyer answers (X12 example 02) [independent]. In EANCOM, the response can accept part of the order (ORDRSP) [independent].

**Substitution.** A **substitution** sends a different item in place of the one ordered. In business ordering it is a recognised line outcome: X12's example shows a line accepted with "a line item substitution", a different part number, which the buyer accepts or rejects with its 860 (X12 example 02) [independent]. In consumer ordering, the one study opened on it is Hoang and Breugelmans's simulated online purchase experiment with UK online grocery shoppers (3,405 households in two waves, a hypothetical retailer): shoppers accepted a substitute more often when it matched the attribute that dominates the category (flavour in categories whose products differ on attributes that cannot be ranked, such as cereals or crisps; brand in categories whose products can be ranked by quality, such as margarine or ketchup: the authors' horizontally and vertically differentiated categories), and much more often when they had bought the substitute before, 73.05% against 39.80% in the first wave and 84.04% against 56.24% in the second ([Hoang & Breugelmans, 2023, full text](https://doi.org/10.1016/j.jretai.2022.06.006)) [independent: a simulated purchase, not field data; the authors note the hypothetical setting could bias answers]. The study measures acceptance only, not cancellations, returns or whether customers came back. That a customer's purchase history should drive the substitute offered is this unit's inference from it, for grocery.

**Case.** Ostrel Foods (fictional) shows the business side: substitutions agreed by phone and not recorded are one of its known troubles (case register), so the order record says one item and the delivery carries another. Corvane's (fictional) register gives no substitution practice.

**What the system does.** Holds the line with an expected date and tells the customer (backorder); offers or applies a substitute under a rule or with the customer's consent, and records both items (substitution); or cancels the line and refunds. **Common failure:** a substitute applied with no record, as at Ostrel, so that invoicing, returns and the next availability check all read the wrong item (this unit's inference). **Measure:** backorders as a percentage of total lines (WERC) [practice]; substitutes accepted over substitutes offered (the course's).

## 6. Store fulfilment: collect in store and ship from store

**The two services.** **Collect in store** (also click-and-collect, or buy online, pick up in store, BOPS): the customer orders online and collects at a store. The goods come either from the store's own shelf or from a distribution centre delivered to the store. **Click-and-reserve** is the variant in which the store holds items from its own stock for the customer to see and pay for. **Ship from store**: a store picks an online order from its shelves and ships it to the customer's address. (Definitions as Hübner et al. 2016 use the services, sections 6.2.2 ("Retailers' outlets") and 6.3 ("Archetypes of omni-channel destination concepts"), page range not confirmed [independent]; the names vary by retailer.)

**How common they were.** In Hübner, Holzapfel and Kuhn's 28 retailers, almost 70% had store pickup, about one-fifth used click-and-reserve from store stock, and about one-tenth regularly shipped online orders from stores; all retailers' same-day orders shipped from stores, though only about one-fifth prioritised same-day delivery (pp. 278–279, 282) [independent: interviews, German-speaking countries, non-food]. Retailers usually charged no shipping fee for store pickup, to bring customers into the stores, and former mail-order retailers saw it as costly, bearing the shipping cost instead of earning a fee for home delivery; one fashion retailer called it its "major growth driver" (p. 282) [independent: the authors' account and an interviewee's view].

**What it asks of a shop.** From the same study, store fulfilment needs extra handling effort by store staff, dedicated space for picking and packing that is then not available to show goods, real-time access to store inventory and an integrated ERP system; pickup adds in-store handling effort and, where the retailer charges no fee for it, a shipping cost the customer would have paid for home delivery (p. 279; for pickup, section 6.3, p. 282, page of the handling-effort point not confirmed) [independent]. The authors judged in-store picking less efficient than picking in a distribution centre, and a logistics manager at a department store retailer told them: "In-store picking is our main cost driver" (p. 279) [independent: an interviewee's statement]. The study did not assess who performs the operations, or their profitability (p. 291) [independent], so it gives no time per order and no cost per order. Ishfaq et al. found the number of sales associates per store among the attributes strongly associated with which fulfilment method a retailer used ([2016, abstract](https://doi.org/10.1108/IJPDLM-02-2015-0032)) [independent: an association, abstract only].

**What it asks of the staff.** O*NET's Retail Salespersons occupation, with "Sales Associate" among its sample titles, lists 24 tasks, none of them about online orders; the nearest are to "Place special orders or call other stores to find desired items" and to "Exchange merchandise for customers and accept returns" ([O*NET, 41-2031.00, updated 2026](https://www.onetonline.org/link/summary/41-2031.00)) [practice]. In the US occupational description, then, picking and shipping web orders is outside the associate's listed work (this unit's reading). At Corvane (fictional), store staff are asked to ship web orders with no process for it, and Freya is the store associate who ships web orders from a store (case register).

**Ship from store, step by step**, in the operations pattern, as working description except where a source is named:

| Step | Physical event | People | What the system does | Common failure | Measure |
|---|---|---|---|---|---|
| 5 Release | The order reaches the store | Store associate (Freya at Corvane, register) | Sends the order to a store device or screen; starts a clock (working) | Nobody sees it during trading hours (working) | Time from release to acceptance (course's) |
| 6 Pick | The associate finds the item on the shop floor or in the stockroom | Store associate | Shows the item, size, colour and expected location (working) | Item not found: tried on, put in a basket or misplaced (Hübner et al., p. 279) [independent]; the store declines the order (working) | Store rejection rate: orders a store declines or cannot fill, over orders sent to it (course's) |
| 7 Pack and label | Packed in the stockroom, carrier label printed | Store associate | Prints the label; records the parcel (working) | No space set aside for packing, which store fulfilment needs (Hübner et al., p. 279) [independent]; no label printer (working) | Orders packed by the carrier's collection time (course's) |
| 8 Hand over | Carrier collects at the store, or the customer collects at the counter | Associate; carrier's driver; customer | Records the hand-over; tells the customer the parcel is on its way or ready (working) | Collection missed; parcel not found at the counter (working) | Pickup ready time: order to ready-for-collection (course's) |

**What breaks for the rest of the network**, as this unit's inference: a store that declines an order sends it back to sourcing (section 4), often to a split or a later date, and the store's availability record keeps offering the item until someone corrects it. SCE4 §9 traces the same loop from a short pick in the centre.

## 7. What sharing availability with customers was found to do

**The study.** Gallino and Moreno studied a retailer's introduction of buy online, pick up in store, using the retailer's own data. After the service started, online sales fell and store sales and store traffic rose. They identify two effects: **cross-selling**, as collecting customers bought more in the store, and **channel shift**, as some online customers moved to the stores and non-customers became store customers. They attribute the shift to more research online, purchase offline (ROPO) behaviour, supported by changes in cart abandonment and conversion rates in both channels, and argue that analysing one channel's data alone can mislead ([Gallino & Moreno, 2014, abstract, read at RePEc](https://doi.org/10.1287/mnsc.2014.1951)) [independent: one retailer; abstract only, read at a bibliographic index because the publisher's page refused the fetch]. The paper's title calls the mechanism sharing reliable inventory availability information; that a customer who sees the local store holds the item goes and buys it there is this unit's reading of the title.

**The setting.** Kellogg Insight, the Kellogg School's publication, described the study in July 2013, before the paper appeared: a home-goods retailer (housewares, home accessories, furniture) with more than 80 stores in the United States and Canada, which began offering buy online, pick up in store across the US in October 2011, while its four Canadian stores did not; one year of data; two comparisons, shoppers near a store against shoppers far from one, and US stores against Canadian stores ([Kellogg Insight, "Shop Online, Pick Up in Store?", 1 July 2013](https://insight.kellogg.northwestern.edu/article/shop_online_pick_up_in_store/amp)) [practice: the school's account; no percentages given]. Total sales rose, as the store gains exceeded the online decline (same page) [practice].

**What it does and does not show**, as this unit's reading: one home-goods retailer in North America, studied by comparing groups with and without the service (in Kellogg Insight's account); it shows what offering the service, and with it store availability, did to where customers bought, and says nothing of what a wrong store record does (section 2). Applying it to Corvane (fictional), a fashion retailer in Europe, is inference. The same availability figure that sources an order (section 4) is also a message to the customer, and a wrong one sends a customer to an empty shelf.

## 8. Changes and cancellations after the order

**What can change.** After the order is placed, the customer may change the address, the delivery method, a size, or a quantity, or cancel a line or the whole order; the seller may change the date, split the order, substitute or cancel (sections 3 and 5). A **cancellation** is the end of an order or a line before it is handed over; after hand-over, the customer's route is a return (section 9). These are working definitions.

**What the rules and standards say.** In the FTC's account of the US rule, buyers can cancel before shipment, and a required refund is prompt and full [practice]. In business ordering, a buyer's change travels as an X12 860 change request, accepting the supplier's changes or cancelling (X12 example 02) [independent]; in EANCOM, the buyer acknowledges a supplier's changes by sending a new order that refers to the original (ORDRSP page) [independent].

**Why the step matters.** A change is easy before release and hard after it, because after release the order is work on someone's device: a pick list in the centre (SCE3 §2), a task on a store screen (section 6), a label on a parcel (working description; no source opened measures the cost of a late change). The order system has to reach the location that holds the work, and the location has to stop it. The states an order passes through, with the moments a cancellation can still stop it:

```viz
{"kind": "states", "per_row": 4, "start": "placed", "states": [{"id": "placed", "label": "Placed", "note": "step 1", "tone": 3}, {"id": "promised", "label": "Promised", "note": "steps 2 to 3", "tone": 3}, {"id": "sourced", "label": "Sourced", "note": "step 4", "tone": 3}, {"id": "released", "label": "Released", "note": "step 5", "tone": 4}, {"id": "cancelled", "label": "Cancelled and refunded", "note": "row C", "tone": 1, "end": true}, {"id": "picked", "label": "Picked and packed", "note": "steps 6 to 7", "tone": 4}, {"id": "handed", "label": "Handed over", "note": "step 8", "tone": 2}, {"id": "delivered", "label": "Delivered", "note": "steps 9 to 10", "tone": 2}, {"id": "returned", "label": "Returned and refunded", "note": "steps 11 to 12", "tone": 5, "end": true}], "transitions": [{"from": "placed", "to": "promised"}, {"from": "promised", "to": "sourced"}, {"from": "sourced", "to": "released"}, {"from": "released", "to": "sourced", "label": "store declines"}, {"from": "placed", "to": "cancelled", "label": "cancel"}, {"from": "promised", "to": "cancelled", "label": "cancel"}, {"from": "sourced", "to": "cancelled", "label": "cancel"}, {"from": "released", "to": "picked"}, {"from": "released", "to": "cancelled", "label": "stop the work"}, {"from": "picked", "to": "cancelled", "label": "stop the work"}, {"from": "picked", "to": "handed"}, {"from": "handed", "to": "delivered"}, {"from": "delivered", "to": "returned", "label": "return"}], "caption": "The states of one order through the twelve steps of this unit (sections 1 to 9): a store's decline sends the order back to sourcing (section 6); a cancellation is simple before release and needs the location to stop the work after it (section 8); after hand-over the customer's route is a return (section 9). States and transitions are this course's working description; no source opened draws an order's states."}
```

**People.** The customer service agent takes customer changes (section 10; working); at Corvane, Jonas answers customers about shipments in transit and about items missing from web orders (case register). **Common failure:** the cancellation reaches the order system and not the location, so the parcel ships and comes back as a return (this unit's inference). **Measure:** the course's **cancellation rate** (lines cancelled over lines ordered, split by who cancelled: the customer or the seller) and **late changes**, changes received after release.

## 9. Returns, from the customer's side

SCE4 §7 took returns from the warehouse's side: receiving, grading, disposition. This section takes the customer's.

**The right to return, by region.** In the EU, a consumer has "a period of 14 days to withdraw from a distance or off-premises contract", and for goods the period runs from the day the consumer, or a third party other than the carrier indicated by the consumer, acquires physical possession of the goods (Directive 2011/83/EU, Art. 9(1), 9(2)(b), [legislation.gov.uk's copy](https://www.legislation.gov.uk/eudr/2011/83/article/9)) [independent, for what the text says]. Where goods ordered in one order are delivered separately, the period runs from possession of the last of them (Art. 9(2)(b), same copy) [independent], so a split shipment (section 4) moves the end of the window. Article 16 lists exceptions to the right, among them goods made to the consumer's specifications or clearly personalised, goods liable to deteriorate or expire rapidly, and sealed goods not suitable for return for health protection or hygiene reasons once unsealed after delivery (Directive 2011/83/EU, Art. 16(c) to (e), [legislation.gov.uk's copy](https://www.legislation.gov.uk/eudr/2011/83/article/16/data.htm?view=plain), which showed no version statement) [independent, for what the text says]. The article on reimbursement (Art. 13) could not be opened, so this unit gives no refund period under the directive. This unit's searches found no US federal rule giving a right to return goods bought online, and opened none; US return terms are not treated here; whether a state law or the seller's own policy binds a sale is a question for the operation's legal advisers. In the EU, which Member State's transposition binds a sale is a question for the operation's legal advisers and the national consumer authority.

**How retailers take returns back.** In Hübner, Holzapfel and Kuhn's 28 retailers, all offered returns by parcel carrier and about half also accepted online orders returned in stores; almost three-quarters processed returns only at the distribution centre, fewer than 20% used a dedicated returns centre, and about one-tenth mixed store and centre processing (2016, pp. 285–286) [independent: interviews, 28 retailers, not quantified by design]; the authors also write that some fashion retailers post return rates of 40–50%, giving no source or measurement for the figure (p. 283) [practice]. Processing returns in the store puts the item back on sale faster and saves transport, at the cost of space, IT requirements and higher processing cost than in a centre, and needs the ERP synchronised so that store inventory is updated (section 7.3, Table 6 on p. 287) [independent]. The authors name a quick refund across all channels as the target (p. 290) [independent: the authors' recommendation, from interviews].

**What the customer does and sees**, in the operations pattern, as working description except where named:

| Step | Physical event | What the system does | Common failure | Measure |
|---|---|---|---|---|
| Ask | The customer asks to return, online or at a store | Checks the order, the item and the return window; issues a return authorisation and a label (working) | Window computed from the order date instead of the delivery date, or from the first parcel of a split order instead of the last (this unit's inference from Art. 9(2)(b)) | Returns requested over items delivered: the **return rate** (course's) |
| Send or bring | Parcel to the carrier, or the item to a store | Records the return in transit, or at the store's till (working) | Store does not record a web return (working; SCE4 §7 on returns put away without a transaction) | Days from request to receipt (course's) |
| Receive and grade | The centre or store opens and checks it | SCE4 §7: match to the order, hold, grade, disposition [working description there; the disposition routes are SCE4's working list] | Item not matched to its order (SCE4 §7) | Days from receipt to refund (course's) |
| Refund | Money back to the customer | Triggers the refund to the original payment (working) | Refund waits for a grade the customer cannot see (working) | Refund cycle time: request to refund (course's) |

**The link to the promise.** Cui et al.'s faster promise raised returns (section 3; abstract) [independent], so in that study the promise and the return rate moved together. Corvane (fictional) has returns from web and from stores (case register); whether a web order can be returned to a store is not in the register.

## 10. Who works the orders

The brief names four roles. Job titles vary by company and country. O*NET describes two of them, and a third in part; it is a US source, graded practice (a public authority's account). The research opened on the people who work orders is thin: Hübner et al. interviewed eight e-commerce managers among their 43, but did not assess who performs the operations (pp. 268, 291) [independent]. The rest is working description; the cards in the deliverable mark each line.

**Customer service agent.** Answers customers about their orders: where an order is, why it is late, what can change, how to return. O*NET's Customer Service Representatives lists "Customer Service Agent" among its sample titles, and tasks that include conferring with customers "to provide information about products or services", keeping records of interactions, resolving complaints "by performing activities such as exchanging merchandise, refunding money", referring unresolved grievances, and recommending improvements in products, packaging, shipping, service or billing; its software list includes customer relationship management and contact centre software ([O*NET, 43-4051.00, updated 2026](https://www.onetonline.org/link/summary/43-4051.00)) [practice]. In the order system: looks up status, changes an address or delivery method before release, cancels a line, issues a refund or a return authorisation (working). Measured on: no source opened defines it; working: contacts handled, contacts resolved at the first contact, and "where is my order" contacts, the kind order management can reduce. At Corvane (fictional), Jonas answers customers about shipments in transit and about items missing from web orders (case register).

**E-commerce operations.** Runs the online orders day to day: watches orders that have not moved, chases a store or the centre, handles exceptions, reports on fill, delay and cancellation (working). No O*NET occupation for the role was opened; the nearest, Order Clerks, has tasks to "Check inventory records to determine availability of requested merchandise", to inform customers of shipping dates and "any anticipated delays", to confer with warehouse or common carrier personnel "to expedite or trace shipments", and to "Calculate and compile order-related statistics" ([O*NET, 43-4151.00, updated 2026](https://onetonline.org/link/summary/43-4151.00)) [practice]; that these fall to an e-commerce team is this unit's reading. Measured on: working, promise accuracy, split rate, seller cancellations, store rejection rate. At Corvane (fictional), Lena runs the online orders (this unit's case fact, listed in the notes).

**Store associate.** Sells on the shop floor and, in a store that fulfils online orders, picks, packs, hands over and takes returns. O*NET's Retail Salespersons lists no task about online orders (section 6) [practice]; store fulfilment adds handling effort and needs space and real-time store inventory (Hübner et al., p. 279) [independent]. Measured on: working, orders packed by the carrier's collection time, rejection rate, pickup ready time. How store sales targets treat online orders a store fills was not sourced; Kellogg Insight reports Moreno's suggestion of the reverse case, rewarding the online team when an online-originated sale closes in a store (2013) [practice: a researcher's suggestion]. At Corvane, Freya ships web orders from a store, with no process for it (case register).

**The person who sets the rules.** Configures availability buffers, sourcing order and store caps, substitution rules and the promise calculation. Gartner's definition says the rules are set by "configuration of business rules in a hierarchical manner" (Peer Insights DOM page) [analyst], so someone holds and changes them; no source opened names the role, and in some companies it may sit in e-commerce operations, planning or IT (working). The work is to edit rules, test them on past orders and watch their effect on cost, split rate and promise accuracy; Acimovic and Graves's heuristic is a rule whose effect was measured on industry data before a pilot (section 4) [independent, abstract]. At Corvane, Oskar sets the order rules (this unit's case fact, listed in the notes).

| Role | Steps worked | Basis |
|---|---|---|
| Customer service agent | 9 Track and inform; C Change or cancel; 11 Return; 12 Refund | O*NET 43-4051.00 [practice]; working |
| E-commerce operations | Exceptions at 2 to 5; 9; reports on all steps | O*NET 43-4151.00 as nearest [practice]; working |
| Store associate | 5 to 8 at a store; 11 at the till | O*NET 41-2031.00 [practice]; Hübner et al. 2016 [independent]; working |
| Rule setter | 2 to 4, by configuration | Gartner DOM definition [analyst]; working |

## 11. What a distributed order management system is, as analysts define it

**The market definition.** Gartner defines distributed order management (DOM) "as the software that orchestrates and optimizes the order fulfillment process"; DOM "utilizes inventory throughout the supply chain network to deliver targeted service levels for order fill rate" and "provides optimal on-time, cost-effective order fulfillment", with orchestration relying on business rules configured in a hierarchy by "channels, consumers, geographies and other criteria", using available-to-promise and available-to-ship inventory levels, and tracking order status across the supply chain (Peer Insights DOM page) [analyst]. Its mandatory features, updated July 2025, are three (same page) [analyst]:

- **Order orchestration**, which "optimizes order routing and inventory allocation" and determines the best fulfilment location on service level and cost;
- **Enterprise inventory**, for available-to-promise and available-to-ship items, allocated on on-hand, in-process or in-transit stock;
- **Order visibility**, tracking order status through the supply chain and communicating it to other systems and to customers.

The page shows no common features. It lists 71 products and shows no total count of reviews (read 27 Nov 2026) [analyst]; what reviewers there say is graded vendor-reported, because vendors can invite their own customers to review (SCE1 §7).

**The 2026 evaluation.** Gartner's *Magic Quadrant for Distributed Order Management*, published 12 November 2026, read in abstract on Gartner's own page: "Distributed order management systems help optimize and manage the customer fulfillment process"; "A convergence across B2B and B2C channels is shaping the current market"; and the research is for supply chain technology leaders evaluating vendors in the DOM market (Gartner abstract) [analyst, abstract only]. The page names no analysts and no document ID. Its companion, *Critical Capabilities for Distributed Order Management*, same date, "evaluates 14 DOM vendors across five use cases" (section 1) [analyst, abstract only]. Vendors license reprints of Gartner's reports (the course's working assumption, SCE1 §8); no reprint was opened here.

**What the definition leaves out**, as this unit's reading of the page set against sections 1 to 9: it names no promise date (only availability), no backorder or substitution handling, no store fulfilment work (the store appears only as inventory), no changes or cancellations, and no returns or refunds. A product that does all of these is still a DOM by the definition; one that does only the three mandatory features is also one. Gartner's execution glossary generally excludes order management from supply chain execution (SCE1 §1) [analyst], while it evaluates DOM in an evaluation of its own: the course places order management on the line between planning and execution, as SCE1 §1 did. No source opened describes a reporting or analytics feature for DOM.

## 12. Halvern's order line on the lifecycle

Halvern Systems (fictional) sells order, warehouse and transport software and nothing else, to retailers, distributors and logistics providers, mid-sized to large, by cloud subscription, and says of itself "One vendor for execution" (case register). Its order line is **Halvern Order** (the core system) with five modules: **Availability**, **Promising**, **Sourcing Rules**, **Store Fulfilment** and **Returns** (register). Varnby Software (fictional) has no separate order system, and Kestrow (fictional) sells a warehouse system with a Returns module (register). Everything in this section is a case fact or this unit's placement of one; none of it is evidence about any real product, and no real vendor is meant.

**On the twelve steps**, as this unit's placement: Availability at step 2; Promising at step 3; Sourcing Rules at step 4, and at re-sourcing after a store declines; Store Fulfilment at steps 5 to 8 when a store fills the order; Returns at step 11. This unit adds one assumption, listed in the notes: the core holds order capture (step 1), order status and notifications (step 9) and changes and cancellations (row C), as SCE6 and SCE8 placed the analyst's core capabilities in Halvern's warehouse and transport cores. At a distribution centre, picking, packing and the shipment record (steps 6 to 8) sit in Halvern Warehouse's core by SCE6's assumption (deliverable B rows 17, 21, 22), and release is open there (SCE6's register row); tracking at step 9 is Halvern Transport's Tracking module, which SCE7 §5 placed at its own step 7.

```viz
{"kind": "matrix", "title": "Halvern's order line on the order lifecycle (fictional)", "cols": ["1 Take", "2 Availability", "3 Promise", "4 Source", "5 Release", "6 Pick", "7 Pack", "8 Hand over", "9 Inform", "10 Deliver", "11 Return", "12 Refund", "C Change"], "rows": [{"label": "Halvern Order (core)", "tone": 1, "cells": ["assumed", null, null, null, null, null, null, null, "assumed", null, null, null, "assumed"]}, {"label": "Availability", "tone": 3, "cells": [null, "placed", null, null, null, null, null, null, null, null, null, null, null]}, {"label": "Promising", "tone": 3, "cells": [null, null, "placed", null, null, null, null, null, null, null, null, null, null]}, {"label": "Sourcing Rules", "tone": 4, "cells": [null, null, null, "placed", null, null, null, null, null, null, null, null, null]}, {"label": "Store Fulfilment", "tone": 2, "cells": [null, null, null, null, "store", "store", "store", "store", null, null, null, null, null]}, {"label": "Returns", "tone": 5, "cells": [null, null, null, null, null, null, null, null, null, null, "placed", null, null]}], "legend": [{"mark": "placed", "means": "this unit's placement of a register module on the step"}, {"mark": "store", "means": "placed on the step when a store fills the order; at a centre the step is Halvern Warehouse's"}, {"mark": "assumed", "means": "this unit's assumption: the core holds the step"}], "caption": "Section 12 of this unit. Module names from the case register (Halvern Systems, fictional); steps from this unit's lifecycle (opening and sections 1 to 9); the placements and the core's assumed steps are this unit's. Step 10 is the carrier's and step 12 has no module. Case facts, evidence of nothing about any real product."}
```

**What the placement shows**, as this unit's reading:

- **Refund has no module.** Returns claims step 11; who triggers the refund and where it is paid (the order system, the payment provider, the ERP) is open, as freight payment was in SCE8 §6. It is a seam for SCE10.
- **Business orders have no module.** Halvern names distributors among its customers (register), and a distributor's orders arrive as purchase orders with line-by-line acknowledgments and changes (section 1). The register gives no module for EDI order intake, acknowledgment or change (lines O4 and O20 below).
- **Backorders and substitutions are unplaced.** They could sit in Promising or Sourcing Rules; the register does not say.
- **One returns module, two sides of the return.** Halvern Order has Returns; Halvern Warehouse does not list one (register; SCE6 §7). The customer's return (this unit), a web return taken at a store's till, and the warehouse's receipt and grading (SCE4 §7) may sit in one line or in two.

## 13. The order capability list

The functions of this unit, restated as lines a buyer would recognise, numbered O1 onward so that they do not collide with SCE6's W1 to W29 or SCE8's T1 to T24 (in SCE6's form, as decided for this unit). Each line names its step and the sources that name it. The grouping and the IDs are this unit's; deliverable C uses them.

| ID | Step (section) | Capability | Named as a capability by |
|---|---|---|---|
| O1 | 1 Take (1) | Web order capture | Course's (section 1); no analyst list names it |
| O2 | 1 Take (1) | Store-placed orders for a customer | O*NET 41-2031.00, special orders [practice] |
| O3 | 1 Take (1) | Marketplace order intake | Working; no source opened |
| O4 | 1 Take, C (1, 5, 8) | Business orders by EDI: purchase order, acknowledgment, change | X12 850, 855, 860 [independent]; EANCOM ORDERS, ORDRSP [independent]; B2B use cases, Gartner Critical Capabilities 2026, abstract [analyst] |
| O5 | 2 Availability (2) | Enterprise inventory: on-hand, in-process, in-transit, by location | Gartner DOM, mandatory [analyst] |
| O6 | 2 Availability (2, 7) | Availability published to channels and shown by store | Gartner DOM, order visibility to customers [analyst]; Gallino and Moreno 2014 [independent] |
| O7 | 2 Availability (2) | Availability buffer by location and item | Working; no source opened |
| O8 | 3 Promise (3) | Promise date and place, with its basis recorded | FTC guide, reasonable basis [practice]; EU Art. 18 [independent] |
| O9 | 3 Promise, 5 (3, 5) | Delay notice, consent and cancellation offer | FTC guide [practice]; EU Art. 18 [independent] |
| O10 | 4 Source (4) | Sourcing rules in a hierarchy | Gartner DOM, mandatory [analyst] |
| O11 | 4 Source (4) | Cost-based sourcing that counts the cost to later orders | Acimovic and Graves 2015, abstract [independent] |
| O12 | 4 Source (4) | Split decision and the number of shipments | Acimovic and Graves 2015 [independent]; Xu et al. 2005 [practice] |
| O13 | 4 Source, 5 (4, 6) | Re-sourcing a line declined or short | Working; SCE4 §9 |
| O14 | 5 Backorder (5) | Backorder with expected date | X12 855 date reschedule [independent]; WERC measure [practice] |
| O15 | 5 Substitution (5) | Substitution rules and consent | X12 855 substitution [independent]; Hoang and Breugelmans 2023 [independent] |
| O16 | 5 to 8 Store (6) | Store fulfilment: task list, pick, decline, pack, label | Hübner et al. 2016 [independent] |
| O17 | 8 Collect (6) | Collect in store: ready notice, counter hand-over | Hübner et al. 2016 [independent] |
| O18 | 5 Store (6) | Store capacity caps and opening hours | Working; no source opened |
| O19 | 9 Inform (11) | Order status and customer notifications | Gartner DOM, mandatory [analyst] |
| O20 | C Change (8) | Changes and cancellations passed to the location holding the work | X12 860 [independent]; FTC guide [practice]; working for the propagation |
| O21 | 11 Return (9) | Customer return: authorisation, window, label, return to a store | EU Art. 9 [independent]; Hübner et al. 2016 [independent] |
| O22 | 12 Refund (9) | Refund trigger | FTC guide, prompt refund [practice]; Hübner et al., quick refund [independent] |
| O23 | All (10) | Customer service desktop: order view and actions | O*NET 43-4051.00 [practice]; working |
| O24 | 2 to 4 (10) | Rule administration and testing on past orders | Working; no source opened |
| O25 | All (3, 4, 6, 8) | Order measures: fill rate, promise accuracy, split rate, cancellations | Gartner DOM, order fill rate [analyst]; APQC (SCE3 §12) [practice]; the rest course's |

Six lines (O1, O3, O7, O13, O18, O24), and the propagation of a change in O20, are named by no source opened. Gartner's three mandatory features cover O5, O10 and O19, and O6 in part; every other line rests on a standard, a rule, a study or the course's working description. No source opened measures which lines an operation needs, or which are worth paying for.

## 14. The real market: one dated list

The course names real vendors only in a dated list from a named analyst report or an audited filing, every vendor on the list alike, with no vendor assessed, ranked, compared or recommended (course brief).

The vendors named in Gartner's *Magic Quadrant for Distributed Order Management*, 12 November 2026, as listed on Gartner's abstract page under "Included in Full Research" (Vendor Strengths and Cautions), read on 27 November 2026; the report itself was not read [analyst, abstract page only]:

- Blue Yonder
- Fluent Commerce
- fulfillmenttools
- IBM
- Infios
- Kbrw
- KIBO Commerce
- Manhattan Associates
- OneStock
- Oracle
- Pipe17
- Retail Unity
- Salesforce
- SAP

The companion *Critical Capabilities for Distributed Order Management*, same date, lists the same 14 names on its abstract page (read 27 Nov 2026) [analyst]. The abstract does not say how many vendors Gartner considered or what the inclusion rules were, so this unit gives neither. The list gives no placement, and the course does not reproduce placements; Gartner's own guidance is to use an evaluation to narrow a list and not to decide on it alone (SCE1 §8, C10) [analyst]. To map any of these vendors' order products, use the method of SCE6 §9 and template D3 below, from the vendor's public pages, every row graded vendor-reported.

## On a site visit

At a retailer's e-commerce operations desk, its customer service team and one store that fulfils online orders, look for, and ask:

- **Where does each channel's order arrive, and which ones are keyed by hand?** Website, stores, marketplaces, business customers by EDI, phone or e-mail (section 1).
- **Which stock does the website sell from: the centre only, the stores, stock on its way?** How often does a store's count reach the order system, and what buffer is held back (section 2)?
- **How is the promised date computed, and who changes the calculation?** What share of orders arrived by the promised date last month (section 3)?
- **Show me the sourcing rules.** In what order are they applied, who last changed them, and what was tested before the change (sections 4, 10)?
- **What happens to a line no location can fill: backorder, substitute or cancel, and who decides?** (Section 5.)
- **At the store: where is an online order picked and packed, by whom, at what time of day, and what happens when the item is not on the shelf?** How many orders did this store decline last week (section 6)?
- **What does the website show about store stock, and how often has a customer arrived to an empty shelf?** (Section 7.)
- **How late can a customer cancel, and how does the cancellation reach the store or the centre?** (Section 8.)
- **Can a web order be returned to a store, and how is the refund triggered?** (Section 9.)
- **What is each of the four roles measured on, and which screens does each one use?** (Section 10.)

## Self-check

1. **How does a business order differ from a consumer order in the messages exchanged?**
   A business order is a purchase order, often sent by EDI (X12 850, EANCOM ORDERS), answered line by line with an acknowledgment that can accept, change (price, date, quantity, substitute) or reject each line (X12 855, EANCOM ORDRSP), and changed or cancelled by the buyer with an 860 or a new order; a consumer gets a confirmation and a promised date (section 1).
2. **Which stock does Gartner's definition say distributed order management allocates from?**
   On-hand, in-process or in-transit stock, as available-to-promise and available-to-ship, across the supply chain network (sections 2, 11).
3. **What did Cui, Lu, Sun and Golden find when a retailer promised faster delivery without delivering faster?**
   At an online retailer selling customised photo products across the United States, where the shown delivery estimates were varied, the faster promise raised sales and profits, and also raised returns and lowered customer retention (section 3; abstract only).
4. **What do the US and EU rules opened here require when goods cannot be delivered as promised?**
   In the FTC's account of the US rule: a reasonable basis for any shipping time, 30 days if none is stated, a delay notice seeking consent with a way to cancel, and a prompt full refund. Under the EU directive: delivery within 30 days unless agreed otherwise, then an additional period, then the right to terminate and be reimbursed (section 3).
5. **What did Acimovic and Graves's fulfilment heuristic add to the cheapest-option rule, and what did it achieve?**
   An estimate of the future shipping cost of each choice, from a transportation linear program; on industry data it captured 36% of the gap to a clairvoyant benchmark, about 1% lower outbound shipping cost, with no loss of service and no rise in holding cost (section 4; abstract only).
6. **What does store fulfilment ask of a shop, according to Hübner, Holzapfel and Kuhn, and how common was ship from store?**
   Extra handling effort, space for picking and packing, real-time store inventory and an integrated ERP; about one-tenth of their 28 retailers shipped online orders from stores regularly, almost 70% offered store pickup, and one manager called in-store picking the main cost driver (section 6).
7. **What did Gallino and Moreno find when a retailer let customers buy online and pick up in store, and where?**
   At one retailer, online sales fell and store sales and traffic rose, through cross-selling and a shift of customers to stores, attributed to research online, purchase offline (abstract only); in Kellogg Insight's account of the study, the retailer sold home goods in North America and total sales rose (section 7).
8. **When does the EU withdrawal period for goods start, and how do the 28 retailers studied take returns back?**
   On the day the consumer, or a third party other than the carrier indicated by the consumer, acquires physical possession of the goods, for 14 days; all retailers offered parcel returns, about half accepted online orders in stores, and almost three-quarters processed returns only at the distribution centre (section 9).

## Deliverable

Four parts: A, the order lifecycle map for one Corvane (fictional) web order that ships from a store; B, four order role cards on Corvane's staff; C, Halvern's order line on capability lines O1 to O25, in SCE6's capability map form; D, the templates for all three; then E, glossary lines. Cells cite this unit's sections in brackets, an earlier unit's section, "register" for a case fact, or "working" for a working description that rests on no source and is listed in the notes where it adds to the register.

### A. The order lifecycle map: a Corvane web order shipped from a store (fictional)

The map takes the form of SCE7's shipment lifecycle map, as this unit's brief asks: six columns, **Step**, **Party**, **Document**, **System touchpoint**, **Common failure**, **Measure**, with Party in place of SCE2's People and Document in place of Data needed (flag F69). It keeps this unit's twelve step numbers and row C, so SCE10 can join rows 5 to 8 to the warehouse (SCE3 deliverable C, rows 1 to 8, for an order the centre fills) and rows 8 to 10 to transport (SCE7 §6, steps 6 to 8). A failure listed is one to look for; it is no claim that Corvane has it, unless it says "known trouble".

Corvane (fictional): a fashion retailer with 60 stores in four European countries and one website; one 28,000 m² distribution centre; web orders of one to three items; web peak about four times a normal week from mid-November to early January; an ERP, a warehouse system about twelve years old, an order system for the website, carriers booked through each carrier's own portal; stock held in the centre and in the stores, and a web order can be filled from either; known trouble includes web orders promised from stock the centre cannot find and store staff asked to ship web orders with no process for it (case register). People: Jonas, customer service agent; Freya, store associate who ships web orders from a store; Helene, chief financial officer (register). Assumed for this map, and listed in the notes: a two-item web order to a home address in the store's country, both items held by one store, the centre short of one of them, so the order system sources the whole order to the store; a parcel carrier collects from the store, booked in that carrier's portal.

| # | Step | Party | Document | System touchpoint | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Take the order | Web customer, through Corvane's website | Order and its confirmation to the customer (working) | Order system for the website (register) | Checkout data incomplete (1, working) | None sourced |
| 2 | Check availability | No person; the order system | Availability by location: the centre's from the warehouse system; how store stock reaches the order system is not in the register | Order system reads the warehouse system (register: both exist); the store's stock record is not in the register | Phantom stock in the centre (register: known trouble); store records often wrong in the store studies (2; SCE4 §10) | Promise failure rate (2) |
| 3 | Promise | Customer sees the date and the address | Promised date on the confirmation (3) | Order system (register) | Date promised from stock that is not there (register: known trouble); promise faster than the store and carrier run (3) | Promise accuracy (3) |
| 4 | Source | The rules; who sets them is not in the register | Sourcing decision: location and reason (4) | Order system (register) | A store chosen whose shelf lacks the item (2, 6) | Split rate; outbound shipping cost per order (4) |
| 5 | Release to the location | Freya, store associate (register) | The store's web order task (working) | How a store receives web orders is not in the register | Store staff asked to ship web orders with no process for it (register: known trouble); nobody sees the order during trading (6, working) | Time from release to acceptance (6, course's) |
| 6 | Pick | Freya (register) | Pick list or screen (working) | Not in the register | Item tried on, put in a basket or misplaced (6, Hübner et al.); the store declines and the line is re-sourced to another location, so two parcels (SCE4 §9's chain run the other way; this unit's reading) | Store rejection rate (6, course's) |
| 7 | Pack and label | Freya (register) | Carrier label | Each carrier's own portal (register; its use from a store is this unit's reading) | No space set aside for packing (6, Hübner et al.); no label printer (working) | Orders packed by the carrier's collection time (6, course's) |
| 8 | Hand over | Freya; the carrier's driver | Collection scan or receipt (working) | Each carrier's own portal (register) | Collection missed, so the promise slips a day (6, working) | On-time pickup (SCE7 §11) |
| 9 | Track and inform | Carrier reports; Jonas answers the customer (register) | Status messages to the customer (working) | Each carrier's portal (register); order status in the order system (11, Gartner order visibility) | Customer asks before Corvane knows; the order record shows stock that was not there (SCE4 §9) | "Where is my order" contacts (10, working) |
| 10 | Deliver | Carrier; the customer | Proof of delivery (SCE7 §6, course term) | Carrier's portal (register) | Delivered after the promised date (3) | Promise accuracy (3); on-time delivery (SCE7 §11) |
| 11 | Return | Customer; whether to a store or the centre is not in the register (register: returns from web and from stores) | Return authorisation and label (9, working) | Not in the register | Return window counted from the order date, not delivery (9, Art. 9(2)(b), reading); a web return taken at a store and not recorded (9; SCE4 §7) | Return rate (9, course's) |
| 12 | Refund | Helene answers for the financial record (SCE1's working placement of settlement, extended here to the refund; notes) | Refund to the original payment (working) | ERP (SCE1 working placement); which system triggers the refund is not in the register | Refund waits for a grade the customer cannot see (9, working) | Refund cycle time (9, course's) |
| C | Change or cancel | Customer asks; Jonas acts (register: he answers customers about their orders, reading) | Change or cancellation request (8) | Order system; how it reaches Freya's store is not in the register | Cancellation reaches the order system and not the store, so the parcel ships and returns (8) | Cancellation rate; late changes (8, course's) |

Where the decision touches this map: Corvane is deciding whether to buy order and transport systems from the same vendor as its warehouse system (register). On this map an order line would take over rows 2 to 5, C and 11, and a store fulfilment module rows 5 to 8 at the store; for example Halvern Order's (fictional) Availability, Promising, Sourcing Rules, Store Fulfilment and Returns modules (section 12). Row 12 and the store's stock record in row 2 are the open seams for SCE10.

### B. Four order role cards, Corvane (fictional)

The form is SCE5's role card (SCE5 deliverable A), nine fields in its order. The case register names two of the four people (Jonas, Freya); this unit names the other two, Lena (e-commerce operations) and Oskar (the person who sets the order rules), as case facts listed in the notes for the register.

**Card 1 · Jonas, customer service agent, Corvane (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Jonas; customer service agent; Corvane [register]; answers customers about shipments in transit and about items missing from web orders [register, added by SCE1 and SCE4]; card set by SCE9 |
| 2 | Measured on | Contacts handled; contacts resolved without a second contact; "where is my order" contacts as a share of all [working]; no source opened defines the measures |
| 3 | Conditions | Desk or contact centre; web volume about four times a normal week from mid-November to early January [register]; the calls follow every broken promise (3; SCE4 §9) |
| 4 | Device | Desktop: the order system and each carrier's portal [register: both exist]; customer relationship management and contact centre software are in O*NET's software list for the occupation (10) [practice] |
| 5 | Top tasks | Answer "where is it" from the order system and the carrier's portal; take changes and cancellations (C); issue return authorisations and refunds (11, 12); keep a record of each contact; resolve complaints by exchange or refund (O*NET 43-4051.00, 10) [practice] |
| 6 | What goes wrong | Items missing from web orders [register]; promises made from stock the centre cannot find [register: known trouble]; a split order arriving as two parcels at two times (SCE4 §9) |
| 7 | What they do about it | Looks in two systems; chases the store or the centre; refunds or re-orders by hand [working]; refers unresolved grievances to designated departments (O*NET, 10) [practice] |
| 8 | What they would ask of the software | One order view with the location chosen, the reason, and the carrier's status; a cancellation that reaches the store and says whether the work was stopped; a refund state the customer can be told [working] (O19, O20, O22, O23) |
| 9 | Hands to and depends on | Depends on the order system's record, the carriers' status and the stores' answers; hands exceptions to e-commerce operations and refunds to finance [working] |

**Card 2 · Freya, store associate, Corvane (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Freya; store associate who ships web orders from a store; Corvane [register]; answers for web orders sourced to a store (SCE1 map step 3) [register]; card set by SCE9 |
| 2 | Measured on | Web orders packed by the carrier's collection time; store rejection rate; pickup ready time [working]; how her store's sales targets count web orders it fills is not in the register |
| 3 | Conditions | Shop floor and stockroom during trading hours; serving customers in the store at the same time; peak from mid-November to early January [register]; extra handling and dedicated space are what Hübner et al. found store fulfilment needs (6) [independent]; whether Freya's store has the space is not in the register |
| 4 | Device | Not in the register; working: a store device or screen showing web orders, a label printer, each carrier's portal [register: carriers booked in their own portals; their use from a store is this unit's reading] |
| 5 | Top tasks | See the web order; find the item on the floor or in the stockroom; confirm or decline; pack; print the label; hand to the carrier's driver; take web returns at the till (6, 9) [working]; exchange merchandise and accept returns (O*NET 41-2031.00, 6) [practice] |
| 6 | What goes wrong | No process for shipping web orders [register: known trouble]; the item has been tried on, put in a basket or misplaced (6, Hübner et al.) [independent]; the carrier collects before the parcel is ready [working] |
| 7 | What they do about it | Searches, then declines the order, so it is re-sourced (SCE4 §9) [register, working] |
| 8 | What they would ask of the software | Orders shown with the item's likely place in the store; one step to decline with a reason; a cap on orders sent in busy hours; the collection time on the screen [working] (O13, O16, O18) |
| 9 | Hands to and depends on | Depends on the store's stock record and the sourcing rules; hands parcels to the carrier and declined orders back to the order system [working]; customers' questions go to Jonas [working] |

**Card 3 · Lena, e-commerce operations, Corvane (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Lena; runs Corvane's online orders day to day [this unit's case fact, listed in the notes]; card set by SCE9 |
| 2 | Measured on | Promise accuracy, split rate, cancellations by the seller, store rejection rate (3, 4, 6, 8) [working, the course's measures]; order fill rate (APQC, SCE3 §12) [practice] |
| 3 | Conditions | Desk; the website's volume about four times a normal week in peak [register] |
| 4 | Device | Desktop: the order system and reports from it [working] |
| 5 | Top tasks | Watch orders that have not moved; chase a store or the centre; re-source or cancel by hand; report on fill and delay [working]; check inventory records, tell customers of delays, confer with warehouse and carrier staff to expedite or trace shipments, compile order statistics (O*NET 43-4151.00, nearest occupation, 10) [practice] |
| 6 | What goes wrong | Promises from stock the centre cannot find [register: known trouble]; stores without a process [register: known trouble]; orders declined by stores (6) [working] |
| 7 | What they do about it | Works a list of stuck orders by hand; asks the rule setter to stop sourcing to a store [working] |
| 8 | What they would ask of the software | An exception queue by cause (declined, short, at risk); each order's sourcing reason; a way to take a store out of sourcing for a day [working] (O13, O18, O25) |
| 9 | Hands to and depends on | Depends on Freya's stores, the centre (Tobias's outbound shift, register) and the carriers; hands customer messages to Jonas and rule changes to the rule setter [working] |

**Card 4 · Oskar, the person who sets the rules, Corvane (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Oskar; configures the order system's availability, promise and sourcing rules [this unit's case fact, listed in the notes]; card set by SCE9 |
| 2 | Measured on | Outbound shipping cost per order (4) [working]; the measure Acimovic and Graves's heuristic lowered (abstract) [independent]; split rate; promise accuracy; store workload against caps [working] |
| 3 | Conditions | Desk; changes made before each season and before peak [working; the register gives two main seasons and the peak dates] |
| 4 | Device | Desktop: the order system's rule screens [working] |
| 5 | Top tasks | Set which locations may ship what and in what order; set availability buffers and store caps; set substitution rules; test a change on past orders; watch its effect (4, 10) [working]; rules are configured in a hierarchy by channels, consumers, geographies (Gartner DOM, 11) [analyst] |
| 6 | What goes wrong | A rule that sends orders to stores that cannot fill them (6) [working]; promises from stock the centre cannot find [register: known trouble] |
| 7 | What they do about it | Raises the buffer, removes a store from sourcing, or changes the order of locations [working] |
| 8 | What they would ask of the software | A test of a rule on last month's orders before it goes live; the effect of a rule on cost, split rate and store load, per rule; a record of who changed what and when [working] (O7, O10, O11, O24) |
| 9 | Hands to and depends on | Depends on the stock records (Carla, inventory controller, for the centre [register]; the stores' records, not in the register); hands rules to the order system, and their effects to e-commerce operations and to Edda, vice-president supply chain [register: her role; the hand-over is working] |

### C. Halvern's order line, mapped (fictional)

The form is SCE6's capability map (SCE6 deliverable A), six fields in its order; the capability lines are section 13's O1 to O25. Vendor: Halvern Systems (fictional). Line: Halvern Order (core system) with modules Availability, Promising, Sourcing Rules, Store Fulfilment and Returns; delivery by cloud subscription; implementation by its own services team and by partners (register). Source for every row: the case register, Halvern Systems (fictional), read 27 November 2026, with this unit's placements (section 12). Grade for every row: **case**, the form value SCE1's key now names for a row that rests on the case register (SCE1 §10; flag F54, decided); it is not a grade of evidence, and for a real vendor these rows would be vendor-reported. "Assumed" marks this unit's placement in the core, listed in the notes.

| # | Operation step | Capability | Module that claims it | Source and date | Grade | Gap or question |
|---|---|---|---|---|---|---|
| 1 | 1 Take (1) | O1 Web order capture | Halvern Order (core), assumed | Case register, 27 Nov 2026 | case | Which website or shop platform it takes orders from is not in the register |
| 2 | 1 Take (1) | O2 Store-placed orders for a customer | No claim in the register | Case register, 27 Nov 2026 | case | Inside Store Fulfilment? |
| 3 | 1 Take (1) | O3 Marketplace order intake | No claim in the register | Case register, 27 Nov 2026 | case | none |
| 4 | 1 Take, C (1, 8) | O4 Business orders by EDI | No claim in the register | Case register, 27 Nov 2026 | case | Halvern names distributors as customers; X12 or EANCOM, or neither? |
| 5 | 2 Availability (2) | O5 Enterprise inventory | Availability | Case register, 27 Nov 2026 | case | Reads stores' stock from which system? In-transit stock? |
| 6 | 2 Availability (2, 7) | O6 Availability published by store | Availability, by this unit's placement | Case register, 27 Nov 2026 | case | Shown to customers, or to channels only? |
| 7 | 2 Availability (2) | O7 Availability buffer | No claim in the register | Case register, 27 Nov 2026 | case | Inside Availability? |
| 8 | 3 Promise (3) | O8 Promise date and place | Promising | Case register, 27 Nov 2026 | case | Uses carriers' transit times from Halvern Transport? (SCE10) |
| 9 | 3 Promise (3, 5) | O9 Delay notice and cancellation offer | No claim in the register | Case register, 27 Nov 2026 | case | Inside Promising? |
| 10 | 4 Source (4) | O10 Sourcing rules in a hierarchy | Sourcing Rules | Case register, 27 Nov 2026 | case | none beyond the placement |
| 11 | 4 Source (4) | O11 Cost-based sourcing counting later orders | No claim in the register | Case register, 27 Nov 2026 | case | Rules only, or optimisation? |
| 12 | 4 Source (4) | O12 Split decision | Sourcing Rules, by this unit's placement | Case register, 27 Nov 2026 | case | none |
| 13 | 4, 5 (4, 6) | O13 Re-sourcing a declined or short line | Sourcing Rules, by this unit's placement | Case register, 27 Nov 2026 | case | Triggered by Halvern Warehouse's short pick (SCE4 §9; SCE10)? |
| 14 | 5 Backorder (5) | O14 Backorder with expected date | No claim in the register | Case register, 27 Nov 2026 | case | Promising or Sourcing Rules? |
| 15 | 5 Substitution (5) | O15 Substitution rules and consent | No claim in the register | Case register, 27 Nov 2026 | case | Ostrel's unrecorded substitutions show the need (register) |
| 16 | 5 to 8 Store (6) | O16 Store fulfilment work | Store Fulfilment | Case register, 27 Nov 2026 | case | On which store device? |
| 17 | 8 Collect (6) | O17 Collect in store | Store Fulfilment, by this unit's placement | Case register, 27 Nov 2026 | case | none |
| 18 | 5 Store (6) | O18 Store capacity caps | No claim in the register | Case register, 27 Nov 2026 | case | Inside Sourcing Rules or Store Fulfilment? |
| 19 | 9 Inform (11) | O19 Order status and notifications | Halvern Order (core), assumed | Case register, 27 Nov 2026 | case | Takes carrier status from Halvern Transport's Tracking? (SCE10) |
| 20 | C Change (8) | O20 Changes and cancellations to the location | Halvern Order (core), assumed | Case register, 27 Nov 2026 | case | Reaches Halvern Warehouse's released work, and a store's? (SCE10) |
| 21 | 11 Return (9) | O21 Customer return | Returns | Case register, 27 Nov 2026 | case | Returns to a store? Grading in Halvern Warehouse, which lists no Returns module (SCE6 §7)? |
| 22 | 12 Refund (9) | O22 Refund trigger | No claim in the register | Case register, 27 Nov 2026 | case | Order system, payment provider or ERP? (SCE10) |
| 23 | All (10) | O23 Customer service desktop | No claim in the register | Case register, 27 Nov 2026 | case | In the core? |
| 24 | 2 to 4 (10) | O24 Rule administration and testing | No claim in the register | Case register, 27 Nov 2026 | case | Inside Sourcing Rules? |
| 25 | All (3, 4, 6, 8) | O25 Order measures | No claim in the register | Case register, 27 Nov 2026 | case | none |

Below the table: five lines placed on the module whose register name matches the line (rows 5, 8, 10, 16, 21); four more placed on a module by this unit's reading (rows 6, 12, 13, 17); three placed in the core by assumption (rows 1, 19, 20); thirteen with no claim in the register. Against Gartner's three mandatory features (section 11), Halvern's register covers order orchestration (row 10) and enterprise inventory (row 5) by module and order visibility (row 19) only by assumption. For a retailer such as Corvane (fictional), the open lines that matter first are the buffer (row 7), store caps (row 18) and the refund (row 22); for a distributor such as Ostrel Foods (fictional), business orders by EDI (row 4) and substitutions (row 15). The open questions for SCE10 are where store stock is read from, who triggers the refund, and how a change reaches released work.

### D. Templates

**D1. The order lifecycle map.** Fill one row per step for a real operation, or for a product by naming the screen or module at each step. Keep the step numbers and row C; add a row where the operation has a step the map lacks, and say why. Mark each cell's grade (independent, analyst, vendor-reported, practice) or "observed" for what you saw yourself.

Operation or product: ______ (name; kind of company: retailer, wholesaler or distributor, manufacturer; channels) · Region: ______ (North America, Europe or other; which consumer rules apply, and the body asked) · Order kind: ______ (consumer or business; channel; fulfilled from a centre, a store or a supplier) · Date filled: ______ · Sources used: ______ (each with its grade)

| # | Step | Party | Document | System touchpoint | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Take the order | ______ (customer and channel) | ______ (order, purchase order, EDI message, confirmation) | ______ (the system whose order record wins) | ______ (what is keyed by hand or lost) | ______ (the site's own, or none found) |
| 2 | Check availability | ______ (none, or who overrides) | ______ (which locations' records, which stock states) | ______ (where each location's stock comes from) | ______ (phantom stock; stale store records) | ______ (promise failure rate) |
| 3 | Promise | ______ (who sees the promise) | ______ (date, place, and its basis) | ______ (which system computes it) | ______ (promise faster than the operation) | ______ (promise accuracy) |
| 4 | Source | ______ (who sets the rules) | ______ (decision and reason) | ______ (where the rules live) | ______ (a location that cannot fill) | ______ (split rate; shipping cost per order) |
| 5 | Release to the location | ______ (who receives the order there) | ______ (pick list, store task) | ______ (warehouse system, store device) | ______ (order not seen in time) | ______ (time to acceptance) |
| 6 | Pick | ______ (operator or associate) | ______ (list or screen) | ______ (which system) | ______ (item not found; declined) | ______ (rejection rate; pick accuracy) |
| 7 | Pack and label | ______ | ______ (label, packing slip) | ______ (where labels print) | ______ (no space, no printer) | ______ (packed by collection time) |
| 8 | Hand over | ______ (driver, collecting customer) | ______ (scan, receipt, signature) | ______ (carrier system, store counter) | ______ (collection missed) | ______ (on-time pickup; pickup ready time) |
| 9 | Track and inform | ______ (who answers the customer) | ______ (status messages) | ______ (where status lands) | ______ (customer asks first) | ______ ("where is my order" contacts) |
| 10 | Deliver | ______ (carrier; customer) | ______ (proof of delivery) | ______ (where proof is stored) | ______ (late against the promise) | ______ (promise accuracy; on-time delivery) |
| 11 | Return | ______ (customer; where it is taken) | ______ (authorisation, label; the rule's window) | ______ (which system records it) | ______ (wrong window; unrecorded store return) | ______ (return rate) |
| 12 | Refund | ______ (who answers for it) | ______ (refund, credit note) | ______ (order system, payment provider, ERP) | ______ (refund waits) | ______ (refund cycle time) |
| C | Change or cancel | ______ (who asks, who acts) | ______ (change request; X12 860 or equivalent) | ______ (how it reaches released work) | ______ (work not stopped) | ______ (cancellation rate; late changes) |

Below the table: the consumer and contract rules that bear on the promise, the cancellation and the return, and the body they were put to (______); the steps the operation runs at a store, a centre or a supplier (______); and the step where the operation's known trouble starts (______).

**D2. The order role card.** Copy one per role. Every line ends with its source in brackets: a section with its grade, "register", "observed" for what you saw yourself, or "working".

| # | Field | Fill in |
|---|---|---|
| 1 | Who | ______ (first name or role label; role: customer service agent, e-commerce operations, store associate, rule setter, or another; company; region) |
| 2 | Measured on | ______ (each measure with whose definition: promise accuracy, split rate, rejection rate, contacts, fill rate, cost per order) |
| 3 | Conditions | ______ (where and when: desk, contact centre, shop floor; trading hours; peak) |
| 4 | Device | ______ (desktop, store device, phone; the systems and screens used) |
| 5 | Top tasks | ______ (three to five, by time spent, each with its lifecycle step number) |
| 6 | What goes wrong | ______ (the failures met most often, with the step where they start) |
| 7 | What they do about it | ______ (workaround, second system, phone call, escalation, and who else is involved) |
| 8 | What they would ask of the software | ______ (requests that follow from fields 2 to 7, each with the O line it touches; mark working until users confirm) |
| 9 | Hands to and depends on | ______ (roles upstream and downstream: stores, centre, carriers, finance, customers) |

**D3. The order capability map.** Fill one row per line for a real vendor's order line, from its public pages, by the steps of SCE6 §9. Keep the O IDs; add a row marked "new" for a claim the list lacks. Every bare blank in rows 2 to 25 and in the "new" row takes what row 1's blank in the same column says.

Vendor: ______ (name as on its pages) · Line: ______ (core product and modules, the vendor's names) · Customers its pages name: ______ (retailers, wholesalers, manufacturers; B2C, B2B or both) · Deployment the pages describe: ______ · Date filled: ______ · Pages read: ______ (each address with the date read)

| # | Operation step | Capability | Module that claims it | Source and date | Grade | Gap or question |
|---|---|---|---|---|---|---|
| 1 | 1 Take | O1 Web order capture | ______ (the module's name exactly as written, or "no public claim found") | ______ (page title, address, date read) | ______ (vendor-reported for the vendor's own pages) | ______ (version, deployment, B2C or B2B, boundary with the warehouse or transport line, configured or customised) |
| 2 | 1 Take | O2 Store-placed orders for a customer | ______ | ______ | ______ | ______ |
| 3 | 1 Take | O3 Marketplace order intake | ______ | ______ | ______ | ______ |
| 4 | 1 Take, C | O4 Business orders by EDI | ______ | ______ | ______ | ______ |
| 5 | 2 Availability | O5 Enterprise inventory | ______ | ______ | ______ | ______ |
| 6 | 2 Availability | O6 Availability published by store | ______ | ______ | ______ | ______ |
| 7 | 2 Availability | O7 Availability buffer | ______ | ______ | ______ | ______ |
| 8 | 3 Promise | O8 Promise date and place | ______ | ______ | ______ | ______ |
| 9 | 3 Promise | O9 Delay notice and cancellation offer | ______ | ______ | ______ | ______ |
| 10 | 4 Source | O10 Sourcing rules in a hierarchy | ______ | ______ | ______ | ______ |
| 11 | 4 Source | O11 Cost-based sourcing counting later orders | ______ | ______ | ______ | ______ |
| 12 | 4 Source | O12 Split decision | ______ | ______ | ______ | ______ |
| 13 | 4, 5 | O13 Re-sourcing a declined or short line | ______ | ______ | ______ | ______ |
| 14 | 5 Backorder | O14 Backorder with expected date | ______ | ______ | ______ | ______ |
| 15 | 5 Substitution | O15 Substitution rules and consent | ______ | ______ | ______ | ______ |
| 16 | 5 to 8 Store | O16 Store fulfilment work | ______ | ______ | ______ | ______ |
| 17 | 8 Collect | O17 Collect in store | ______ | ______ | ______ | ______ |
| 18 | 5 Store | O18 Store capacity caps | ______ | ______ | ______ | ______ |
| 19 | 9 Inform | O19 Order status and notifications | ______ | ______ | ______ | ______ |
| 20 | C Change | O20 Changes and cancellations to the location | ______ | ______ | ______ | ______ |
| 21 | 11 Return | O21 Customer return | ______ | ______ | ______ | ______ |
| 22 | 12 Refund | O22 Refund trigger | ______ | ______ | ______ | ______ |
| 23 | All | O23 Customer service desktop | ______ | ______ | ______ | ______ |
| 24 | 2 to 4 | O24 Rule administration and testing | ______ | ______ | ______ | ______ |
| 25 | All | O25 Order measures | ______ | ______ | ______ | ______ |
| new | ______ (the step it belongs to) | ______ (the vendor's claim, in your words) | ______ | ______ | ______ | ______ |

Below the table, count the lines claimed, the lines with no public claim found and the new lines; write which of Gartner's three mandatory features (rows 5, 10, 19) the pages claim; and write the open questions for the seams (SCE10). Write no price unless the vendor published it; otherwise "no public figure".

### E. Glossary lines

Added to the working glossary of SCE1 to SCE8.

| Term | Working definition | Region | Source |
|---|---|---|---|
| Channel | Where an order comes from: website, store, marketplace, business customer | Both | Course term (1) |
| Marketplace | A third party's online shop on which a retailer sells, which passes the order on | Both | Working definition; no source opened |
| B2C; B2B | Business to consumer; business to business | Both | Gartner Critical Capabilities 2026, abstract, uses both [analyst]; definitions the course's |
| Purchase order (PO) | A buyer's document ordering goods under agreed conditions | Both | EANCOM ORDERS [independent]; X12 850 [independent] |
| Electronic data interchange (EDI) | Structured business messages exchanged system to system | Both | Course term; X12, GS1 [independent] for the messages |
| X12 850, 855, 860 | Purchase order; purchase order acknowledgment; purchase order change request | Published by X12; regional use not sourced | X12 [independent] |
| EANCOM ORDERS, ORDRSP | Purchase order message; purchase order response message | GS1 EANCOM; regional use not sourced | GS1 [independent] |
| On-hand, in-process, in-transit stock | Stock on a shelf now; being received, moved or packed; on its way between locations | Both | Named in Gartner DOM definition [analyst]; definitions the course's |
| Availability buffer | Stock held back from what a location offers, against record errors | Both | Working term; no source opened |
| Phantom stock | Units the record shows and the shelf does not hold | Both | SCE4 §4 |
| Promise | A date (or window) and a place given to the customer for an order | Both | Course term (3) |
| Cut-off | The latest order time that still makes the day's departure | Both | SCE3 §8 |
| Sourcing (order routing, allocation) | Choosing which location fills each line of an order | Both | Gartner DOM, "order routing and inventory allocation" [analyst] |
| Order orchestration | Gartner's term for routing orders and allocating inventory to the best fulfilment location on service level and cost | Both | Gartner DOM [analyst] |
| Drop shipper | A supplier that ships direct to the retailer's customer | Both | Course term; named in Xu et al. 2005 [practice] |
| Split shipment | One order sent in more than one delivery | Both | SCE4 glossary |
| Backorder | An ordered line waiting for stock | Both | SCE4 glossary |
| Substitution | Sending a different item in place of the one ordered | Both | X12 855 example [independent]; Hoang and Breugelmans 2023 [independent] |
| Collect in store (click-and-collect; BOPS) | The customer orders online and collects at a store | Both | Hübner et al. 2016 [independent]; Gallino and Moreno 2014 [independent] |
| Click-and-reserve | A store holds items from its own stock for the customer to see and pay for | Europe (the study's sample) | Hübner et al. 2016 [independent] |
| Ship from store | A store picks an online order from its shelves and ships it | Both | Hübner et al. 2016 [independent] |
| Research online, purchase offline (ROPO) | Customers looking online and buying in a store | Both | Gallino and Moreno 2014 [independent] |
| Cancellation | The end of an order or a line before hand-over | Both | Working definition (8) |
| Right of withdrawal | The EU consumer's 14 days to withdraw from a distance contract, from physical possession of the goods | EU | Directive 2011/83/EU Art. 9 [independent] |
| Return authorisation | The seller's acceptance of a return request, with a label or instructions | Both | Working term (9) |
| Distributed order management (DOM) | Software that orchestrates and optimises fulfilment across the network, with order orchestration, enterprise inventory and order visibility as mandatory features | Both | Gartner Peer Insights, July 2025 [analyst]; as in SCE1's glossary |
| Order fill rate | Orders filled completely, as a share of all | Both | APQC (SCE3 §12) [practice]; named in Gartner DOM [analyst] |
| Promise accuracy; promise failure rate | Orders delivered or ready by the promised date, over all; lines that could not be filled from the location promised, over all | Both | Course's (2, 3) |
| Split rate; store rejection rate; pickup ready time | Orders in more than one shipment, over all; orders a store declines or cannot fill, over orders sent to it; time from order to ready for collection | Both | Course's (4, 6) |
| Capability line (O1 to O25) | One order function on the course's list, used in a capability map | This course | This unit, section 13 |

## Sources

All addresses opened on 27 November 2026; the source log (sources.md) gives what was read at each. Sources cited only through earlier units (Bartholdi and Hackman; APQC; WERC; the store record studies) are listed in SCE1, SCE3 and SCE4.

- Acimovic, J. & Graves, S. C. (2015). Making Better Fulfillment Decisions on the Fly in an Online Retail Environment. *Manufacturing & Service Operations Management* 17(1), 34–51. https://doi.org/10.1287/msom.2014.0505 (abstract, read at https://pubsonline.informs.org/doi/10.1287/msom.2014.0505; record at https://dspace.mit.edu/handle/1721.1/99448)
- Cui, R., Lu, Z., Sun, T. & Golden, J. M. (2024). Sooner or Later? Promising Delivery Speed in Online Retail. *Manufacturing & Service Operations Management* 26(1), 233–251. https://doi.org/10.1287/msom.2021.0174 (abstract, read at https://pubsonline.informs.org/doi/fpi/10.1287/msom.2021.0174)
- European Commission. "Consumer rights directive". Undated page. https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en?prefLang=fr
- European Union. Directive 2011/83/EU of the European Parliament and of the Council of 25 October 2011 on consumer rights, Articles 9 and 18, in legislation.gov.uk's copy (latest available revised text, corresponding to the consolidated version of 1 July 2018). https://www.legislation.gov.uk/eudr/2011/83/article/9 ; https://www.legislation.gov.uk/eudr/2011/83/article/18 ; Article 16, same site, plain view (no version statement shown on the page): https://www.legislation.gov.uk/eudr/2011/83/article/16/data.htm?view=plain
- European Union. Directive (EU) 2019/2161 of the European Parliament and of the Council of 27 November 2019 on better enforcement and modernisation of Union consumer protection rules, Article 4, in legislation.gov.uk's copy (as adopted). https://legislation.gov.uk/eudr/2019/2161/article/4/adopted/data.pdf
- European Union. Directive (EU) 2023/2673 of the European Parliament and of the Council of 22 November 2023 amending Directive 2011/83/EU as regards financial services contracts concluded at a distance and repealing Directive 2002/65/EC, Article 1(3) (inserting Article 11a), read in the text as adopted, PE-CONS 37/23, Council of the European Union, 11 October 2023, not in the Official Journal text (EUR-Lex returned an empty page on 27 Nov 2026). https://data.consilium.europa.eu/doc/document/PE-37-2023-INIT/en/pdf
- Gallino, S. & Moreno, A. (2014). Integration of Online and Offline Channels in Retail: The Impact of Sharing Reliable Inventory Availability Information. *Management Science* 60(6), 1434–1451. https://doi.org/10.1287/mnsc.2014.1951 (abstract, read at https://econpapers.repec.org/RePEc:inm:ormnsc:v:60:y:2014:i:6:p:1434-1451)
- Gartner. "Gartner Magic Quadrant for Distributed Order Management". Abstract page. 12 November 2026. https://www.gartner.com/en/documents/8617033
- Gartner. "Critical Capabilities for Distributed Order Management". Abstract page. 12 November 2026. https://www.gartner.com/en/documents/8631633
- Gartner Peer Insights. "Distributed Order Management Systems (Transitioning to Distributed Order Management) Reviews and Ratings". Mandatory features updated July 2025. https://www.gartner.com/reviews/market/distributed-order-management-systems
- GS1. EANCOM 2002 S3, Part II, "ORDERS Purchase order message". https://gs1.org/sites/gs1/files/docs/eancom/ean02s3/part2/orders/intro.htm
- GS1. EANCOM 2002 S3, Part II, "ORDRSP Purchase order response message". https://gs1.org/sites/gs1/files/docs/eancom/ean02s3/part2/ordrsp/intro.htm
- Hoang, D. & Breugelmans, E. (2023). "Sorry, the product you ordered is out of stock": Effects of substitution policy in online grocery retailing. *Journal of Retailing* 99(1), 26–45. https://doi.org/10.1016/j.jretai.2022.06.006 (full text, published version, read at https://eprints.leedsbeckett.ac.uk/id/eprint/8738/8/SorryTheProductYouOrderedIsOutOfStockEffectsOfSubstitutionPolicyInOnlineGroceryRetailingPV-HOANG.pdf)
- Hübner, A., Holzapfel, A. & Kuhn, H. (2016). Distribution systems in omni-channel retailing. *Business Research* 9(2), 255–296. https://doi.org/10.1007/s40685-016-0034-7 (full text, read at https://link.springer.com/content/pdf/10.1007/s40685-016-0034-7.pdf)
- Ishfaq, R., Defee, C. C., Gibson, B. J. & Raja, U. (2016). Realignment of the physical distribution process in omni-channel fulfillment. *International Journal of Physical Distribution & Logistics Management* 46(6/7), 543–561. https://doi.org/10.1108/IJPDLM-02-2015-0032 (abstract, read at https://emerald.com/insight/content/doi/10.1108/IJPDLM-02-2015-0032/full/html)
- Ross, V. Kellogg Insight, Kellogg School of Management. "Shop Online, Pick Up in Store?". 1 July 2013. https://insight.kellogg.northwestern.edu/article/shop_online_pick_up_in_store/amp
- O*NET OnLine, US Department of Labor. "Customer Service Representatives", 43-4051.00. Updated 2026. https://www.onetonline.org/link/summary/43-4051.00
- O*NET OnLine. "Order Clerks", 43-4151.00. Updated 2026. https://onetonline.org/link/summary/43-4151.00
- O*NET OnLine. "Retail Salespersons", 41-2031.00. Updated 2026. https://www.onetonline.org/link/summary/41-2031.00
- US Federal Trade Commission. "Business Guide to the FTC's Mail, Internet, or Telephone Order Merchandise Rule". September 2011, edited January 2025. https://ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule
- X12. "850". Undated. https://x12.org/node/4392
- X12. "Example 02: Purchase Order Acknowledgment with Minor Changes". Undated. https://x12.org/examples/004010x358/example-2-purchase-order-acknowledgment-minor-changes
- Xu, P. J., Allgor, R. & Graves, S. C. (2005). The Benefits of Re-Evaluating Real-Time Fulfillment Decisions. MIT Innovation in Manufacturing Systems and Technology (IMST) working paper, January 2005 (abstract). https://dspace.mit.edu/handle/1721.1/7443

## Unsure list

claude-opus-5-5

# Unsure: SCE9

1. Hübner, Holzapfel and Kuhn (2016): every percentage, page number and quotation ("In-store picking is our main cost driver", "major growth driver") comes from a fetch tool's extraction of the Springer PDF in two passes, not re-read against a second copy; the issue number 9(2) is the seed bibliography's Crossref record, not shown in the PDF read. Page numbers were re-read on 27 Nov 2026 against the PDF's printed running heads, which close each page in the extraction (the last, 296, follows the last reference): located passages moved one page later; where a passage was not located, its section is named and the page marked not confirmed.
2. Gallino and Moreno (2014): the abstract was read at RePEc's EconPapers, not at the publisher (the INFORMS page refused); the setting (home-goods retailer, more than 80 stores, US and Canada, October 2011, four Canadian stores) comes from Kellogg Insight's 2013 article, written before publication, by Valerie Ross (named in the page's "About the Writer" section; the byline credits the research of Santiago Gallino and Antonio Moreno-Garcia).
3. Gartner's abstract page for the DOM Magic Quadrant (12 Nov 2026): the 14 vendor names, the three summary sentences and the absence of analyst names and document ID come from the fetch tool's reading of the page; the Critical Capabilities page's five use cases likewise.
4. Gartner Peer Insights DOM page: the definition's quotations, "mandatory features updated July 2025", 71 products and the absence of common features and of a total review count are from the extraction.
5. Cui, Lu, Sun and Golden (2024): abstract only; the setting (an online retailer selling customised photo products across the United States), the design (disclosed delivery estimates varied with physical speed unchanged) and the difference-in-differences identification are from the abstract, re-read at the publisher on 27 Nov 2026; the abstract does not use the words "field experiment"; no effect sizes were read.
6. Hoang and Breugelmans (2023): 100,000 of about 132,000 characters were read; the acceptance percentages (73.05%, 39.80%, 84.04%, 56.24%) are from the extraction; the unit's gloss of horizontally and vertically differentiated categories (attributes that cannot be ranked; products ranked by quality) is a paraphrase; the study's categories are breakfast cereals, frozen pizza and crisps (horizontal) and margarine and ketchup (vertical).
7. Directive 2011/83/EU Arts. 9 and 18 were read in legislation.gov.uk's copy, which corresponds to the consolidated text of 1 July 2018 and has no amendments after 31 December 2020; Directive 2019/2161 was read (it inserts Article 9(1a) and amends 9(2); it does not amend Article 18); Directive 2023/2673 was read in the Council's text as adopted (PE-CONS 37/23), not in the Official Journal, and amends neither article; whether 2024/825 changes either article was not confirmed.
8. FTC guide: the 30-day and 50-day periods, the seven-working-day refund and the burden of proof are the agency's account; the rule's text (16 CFR Part 435) was not opened.
9. X12: the 855 and 860 behaviour comes from a published example in guide 004010X358, whose industry scope was not confirmed; the 850 quotation is from the extraction of X12's page.
10. Acimovic and Graves (2015): "36%" and "about 1%" are from the abstract as extracted; Xu, Allgor and Graves (2005) is graded practice as a working paper, and its 2009 journal version could not be opened to see whether the findings changed.

Object: none

Fresh check 2026-11-27 (claude-opus-5-5): fix · 1 error, 13 should-fix, 27 minor; report `audits/supply-chain-execution/fresh-check-SCE9.md`
