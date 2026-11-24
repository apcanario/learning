---
code: SCE4
title: Inventory and control
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-24
search: off
intro: SCE4 covers the stock record. It sets out inventory held by location and the attributes stored with it (lot, serial number, expiry date, status, owner), rotation by date, holds and quarantine as a regulated process, what the research on inventory record inaccuracy found and in which settings, counting, slotting, returns, traceability and recalls, and one error followed through a fictional case from short pick to service call. It ends with the inventory measures WERC names. Its deliverable is a cause tree for inventory errors at Corvane (fictional), a count plan for Ostrel Foods (fictional), the templates for both, and glossary lines. Written 24 Nov 2026 by Opus 5.5 with search off (references still opened live, all on 24 Nov 2026), then given a fresh check (fix: 3 errors, 18 should-fix, 12 minor) and a quality review (fix: 2 errors, 14 should-fix, 10 minor) by separate Opus 5.5 agents, their findings applied: all 33 of the fresh check's, with 4 extra fixes, and 25 of the quality review's 26. Held: the quality review's f25, that the unit depends on facts that change (FDA's food traceability compliance dates, the eCFR version date) and could be search on; it stays off as the course's convention, left to a syllabus decision (flag F41). Known gaps: the empirical studies of record inaccuracy that could be opened and that report a share of records wrong are all of retail stores; the one distribution-centre study (Kull et al. 2013, read in full in the author's version) measures inaccuracy as a percentage of on-hand stock instead. DeHoratius and Raman (2008), Kök and Shang (2007), Fleisch and Tellkamp (2005) and Guide et al. (2006) on returns were read in abstract only. The quarantine and returns process is sourced from US drug regulation only. No source was opened on who may make an adjustment or on the general routes a returned item can take. WERC's definitions were not found, so its measures carry the course's working definitions; one has a vendor's description (Hyster-Yale, 2025, vendor-reported).
---

# SCE4 · Inventory and control

Every claim that carries a number, a mechanism or a recommendation ends with a grade from SCE1's key (SCE1 §10): [independent], [analyst], [vendor-reported] or [practice]. Lines marked as this unit's inference carry no grade. One point holds throughout: every study this unit could open that reports how many records were wrong was carried out in **retail stores**; the one distribution-centre study, Kull et al. (2013, section 9), read in full in the author's version, measures inaccuracy as a percentage of on-hand stock and gives no share of records wrong. Applying a store finding to a warehouse is this unit's inference, and the unit says so each time.

## 1. Inventory at the level of a location

**The record.** A warehouse system holds stock as quantities of a SKU (SCE2 §2) at a **location**. A location is an addressed place where goods can be: a rack position, a shelf bin, a staging lane, a forklift. Bartholdi and Hackman's standard is that "a good WMS will track every place that product can be, down to and including the forks of individual forklift trucks" (§4.2) [practice]. This continuously updated record is the **perpetual inventory**, also called **book inventory**. What is actually there is the **physical inventory**. The rest of this unit is about the gap between the two.

**The attributes that travel with it.** One quantity at one location is not enough. Each record also carries attributes. Which of them a site needs depends on its goods and its rules:

- **Lot (batch)**: the production or receipt group a unit belongs to. US drug rules require a lot or control number on the product that "permits determination of the history of the manufacture and control of the batch" ([21 CFR 211.130(c)](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)) [independent]. In EU food law, as Ireland's food safety authority states it, the legal minimum is one step up and one step down, and recording the batch is best practice (SCE2 §9).
- **Serial number**: an identifier for one unit. GS1 states that an individual trade item may be identified uniquely by combining its Global Trade Item Number (GTIN) with a serial number, and that serialisation makes it possible to trace individual products through the supply chain ([GS1 support, modified 28 Aug 2024](https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-)) [independent]. GS1's SSCC serialises a logistic unit, not an item (SCE2 §3.6).
- **Expiry date**: the date by which the product must be used. Drug products must bear an expiration date set by stability testing ([21 CFR 211.137](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)) [independent]. What food dates mean differs between the EU and the US (SCE2 §9).
- **Status**: whether the stock may be allocated to orders (section 3).
- **Owner**: whose goods they are. In a multi-client warehouse such as Tandric Logistics' (fictional) site, with nine clients on one shared warehouse system (case register), the same SKU can belong to different clients. That needs an owner on every record. This is a working description; no source on owner as an attribute was opened.

The system therefore keys stock on SKU, location, lot, date, status and owner, and every transaction (receipt, move, pick, adjustment) must say which combination it changes (this unit's inference). A record that is right on quantity but wrong on lot or status is still wrong for a recall or a hold.

## 2. Rotation rules built on dates

A **rotation rule** decides which unit of a SKU leaves first. SCE2 §9 defined the two common ones from Bartholdi and Hackman: **FIFO** (first in, first out: oldest receipt first) and **FEFO** (first expired, first out: earliest date first) [practice]. US drug rules require "a procedure whereby the oldest approved stock of a drug product is distributed first", and "Deviation from this requirement is permitted if such deviation is temporary and appropriate" ([21 CFR 211.150(a)](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)) [independent]. "Approved" matters: stock on hold does not count as the oldest, whatever its date.

What the system needs for this, as this unit's inference: the date on every location record, captured at receipt (SCE2 §9). It needs a rule per SKU or owner saying FIFO or FEFO, and pick directions that name the location holding the right date. A picker who takes the nearest pallet instead of the directed one breaks rotation, and splits the record too, because two locations are now wrong (section 4). Ostrel Foods' (fictional) known trouble, short-dated stock found too late (case register), is the failure this rule exists to prevent. The register does not say whether its dates are missing, unrotated or unreported.

## 3. Stock statuses: holds and quarantine

SCE2 §3.5 left the quality hold as a working description because no source describing it as a process had been opened (flag F23). US drug rules describe it as one. 21 CFR Part 211 governs the manufacture of finished drugs; its quarantine sections (211.82 to 211.89) cover incoming components, containers and closures, and holding and distribution are in 211.142 and 211.150. They are a regulated setting, so applying them to food or fashion, or to a distribution warehouse, is this unit's inference.

**The process in 21 CFR Part 211** ([eCFR, up to date as of 16 June 2026](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)):

1. **At receipt**, each container is examined before acceptance for labelling, damage, broken seals and contamination (211.82(a)) [independent].
2. **Quarantine**: received components "shall be stored under quarantine until they have been tested or examined", and are then released (211.82(b)) [independent]. Each lot is "withheld from use" until the quality control unit has sampled, tested or examined it and released it (211.84(a)) [independent].
3. **Release or reject.** Rejected material "shall be identified and controlled under a quarantine system" designed to prevent its use (211.89) [independent].
4. **Retest.** Approved material is retested or re-examined when necessary, for example after long storage or exposure to heat, and approved or rejected again (211.87) [independent].
5. **In the warehouse**, written procedures must cover "Quarantine of drug products before release by the quality control unit" and storage conditions of temperature, humidity and light (211.142) [independent].
6. **Returns** are "identified as such and held" (211.204; section 7) [independent].

**What this means for the record.** A **status** is an attribute that keeps stock in the record while controlling whether it can be allocated. This course's working list of statuses is: available, quarantine (awaiting test or inspection), rejected, damaged, returned awaiting grading, expired. Only quarantine, rejected and returned-held come from the regulation; the rest are working terms. A status change is a transaction. The regulation's "released by the quality control unit" means the system must record who changed it and when (this unit's inference). Bartholdi and Hackman list quality assurance among a WMS's basic features (§4.3) [practice] but do not describe it.

```viz
{"kind": "states", "per_row": 4, "start": "received", "states": [{"id": "received", "label": "Received", "note": "examined at receipt", "tone": 3}, {"id": "quarantine", "label": "Quarantine", "note": "withheld until tested", "tone": 4}, {"id": "available", "label": "Available", "note": "may be allocated", "tone": 2}, {"id": "shipped", "label": "Shipped", "note": "lot on the record", "end": true, "tone": 2}, {"id": "rejected", "label": "Rejected", "note": "controlled under quarantine", "tone": 5}, {"id": "returned", "label": "Returned, held", "note": "identified as such", "tone": 4}, {"id": "destroyed", "label": "Destroyed", "note": "unless proven fit", "end": true, "tone": 5}], "transitions": [{"from": "received", "to": "quarantine", "label": "store"}, {"from": "quarantine", "to": "available", "label": "release"}, {"from": "available", "to": "shipped", "label": "pick, ship"}, {"from": "quarantine", "to": "rejected", "label": "reject"}, {"from": "available", "to": "quarantine", "label": "retest"}, {"from": "returned", "to": "destroyed", "label": "doubt"}, {"from": "returned", "to": "available", "label": "proven fit"}], "caption": "Stock statuses as US drug rules describe them, from sections 3, 7 and 8 of this unit: 21 CFR 211.82, 211.84, 211.87, 211.89, 211.150, 211.196 and 211.204 (eCFR, up to date as of 16 June 2026). The retest path back to quarantine is this unit's reading of 211.87. A returned product goes back to stock only if examination proves it meets standards (section 7). A regulated setting, written for drug manufacturers; using it for other goods or in a distribution warehouse is this unit's inference."}
```

## 4. How the record goes wrong

**The empirical research.** The study the seed bibliography names for this unit is DeHoratius and Raman ([2008](https://doi.org/10.1287/mnsc.1070.0789)), read here in abstract only (flag F12). **Sample and setting**: nearly 370,000 inventory records from 37 stores of one retailer. **Design**: an empirical analysis using hierarchical linear modelling, which splits the variance between levels. **Findings**: 65% of the records were inaccurate. 26.4% of the variance in **inventory record inaccuracy** (IRI: the record differing from what is physically there) lay between product categories and 2.7% between stores. Inventory auditing practices were associated with lower inaccuracy, and store complexity and distribution structure with higher. The covariates explain 67.6% and 69.0% of the variance across stores and categories [independent]. These are correlations, in stores; the abstract does not say how "inaccurate" was thresholded.

Two later store studies give comparable shapes:

- **ECR Community report** (Rekik, Syntetos & Glock, [October 2019](https://orca.cardiff.ac.uk/142664/1/84486%20ECR%20Inventory%20Inaccuracy%20Report.pdf)). Seven European retailers in four countries, 91 stores, 233,318 SKUs analysed, with stocktake audits (full counts, section 5) as the reference. About 59.54% of audited SKUs did not match the system: 63.39% in grocery and general merchandise, 54.08% in fashion, and from 6.20% to 73.33% by retailer [independent]. Any difference "even if the difference is just a single unit" counted; there was no tolerance band [independent].
- **DeHoratius, Holzapfel, Kuhn, Mersereau and Sternbeck** ([2023](https://doi.org/10.1287/msom.2022.1119), full text). Ten stores of one European drugstore chain, about 500 items in nine categories, counted by student teams in spring 2017. In the week-3 count, 31% of items had non-zero discrepancies, with stores ranging from 19% to 45% [independent].

```viz
{"kind": "compare", "unit": "%", "max": 100, "rows": [{"label": "DeHoratius & Raman 2008: 37 stores, one retailer", "value": 65, "tone": 4}, {"label": "ECR report 2019: 91 stores, seven retailers", "value": 59.54, "tone": 4}, {"label": "DeHoratius et al. 2023: 10 stores, week-3 count", "value": 31, "tone": 3}], "caption": "Share of store inventory records found not to match the shelf in three studies, from section 4 of this unit: DeHoratius and Raman (2008, abstract), Rekik, Syntetos and Glock for ECR (2019), DeHoratius et al. (2023). All three are retail stores, not warehouses, and their samples, periods and thresholds differ, so the bars are not a trend or a benchmark."}
```

**Which way the record is wrong.** DeHoratius et al. (2023) define a discrepancy as "system inventory recorded minus actual inventory found". The record showing more than the shelf is **phantom inventory**; the record showing less is **hidden inventory**. An **unknown out-of-stock** is a shelf that is empty while the system shows stock [independent]. The ECR report signs it the other way round: positive when the physical stock is higher than the record [independent]. Check the sign convention before comparing two figures.

**The causes named.** The ECR report lists "incorrect manual adjustments of stock records, employee or customer theft, damage or spoilage", plus wrong shipments, check-out errors and misplacement [practice]. In one retailer's data it found that manually removing stock from the record "seems to lead to positive inventory discrepancies over time", and adding stock the opposite [independent: one retailer]. Fleisch and Tellkamp's simulation of a three-echelon (three-tier: for example supplier, warehouse, store) retail chain builds its model on records drifting through "low process quality, theft, and items becoming unsaleable" ([2005, abstract](https://doi.org/10.1016/j.ijpe.2004.02.003)) [practice: a model premise, not a measurement]. For warehouses, Bartholdi and Hackman name one mechanism: with shared storage, order-pickers take product from convenient locations, "creating discrepancies between book and physical inventory at two locations" (§2.4) [practice].

**Where each enters a warehouse** (this unit's inference, from SCE2, SCE3 and the causes above). Each cause enters at a step and shows up later:

| Cause | Enters at | Shows as |
|---|---|---|
| Miscount or wrong item at receipt | Check and count (SCE2 §3.4) | Phantom or hidden stock from the first day |
| Put to a location other than the one recorded | Put-away (SCE2 §3.8) | Two wrong locations: one phantom, one hidden |
| Taken from the wrong location | Picking or replenishment (SCE2 §6, SCE3 §3) | As above, and broken rotation |
| **Short pick** (less at the location than the line asks for, SCE3 §10) confirmed as full | Picking (SCE3 §10) | Phantom stock of what was ordered persists while the order ships short |
| **Wrong pick** (wrong item or size taken) | Picking (SCE3 §10) | Hidden stock of what was ordered; phantom stock of what was taken (section 9) |
| Damage or spoilage not recorded | Anywhere | Phantom stock |
| Theft | Anywhere | Phantom stock |
| Return put back without a transaction | Returns (section 7) | Hidden stock |
| Wrong adjustment | Counting (section 5) | Either direction |

No study opened here measures how often each cause occurs in a warehouse.

## 5. Counting

**Two kinds of count.** A **full count** (physical inventory; the ECR report's "stocktake") counts every location at once. A **cycle count** counts a selected part of the stock on a schedule or a trigger while the site keeps working. Bartholdi and Hackman list cycle counting among a WMS's high-end features (§4.3) [practice]. Their book names it only as a topic of chapter 18, which is headed "In preparation": "Cycle-counting: What to count and when, to reconcile book and physical inventories" (ch. 18) [practice]. Whether a site's financial statements need a full count, and when, is a question for its auditors and finance team.

**Why counts are not done once.** Records drift after a count. In the ECR report's second experiment, run at one retailer, a first stocktake was corrected and the later ones were recorded without correcting the records. The report found that "negative inaccuracies clearly accumulate over time" (in its sign: physical below record), while positive ones stayed fairly stable [independent]. In its first experiment, test stores that were counted mid-study and had their records corrected to the count had higher sales over the following 12 weeks than control stores whose records were not corrected: from 3.83% to 8.38% by retailer, a simple average of 5.98% [independent]. These are stores; for a warehouse, the result would show as fewer short picks, which is this unit's inference.

**What to count.** DeHoratius et al. (2023) compared rules for choosing which items to count. They worked at a set **counting depth**, the share of items counted. Seven rules ranked items by one index each: sales since the last count; recorded stock, highest first or lowest first; past error; forecast sales; days since the last sale relative to the forecast; and days since the last count. Two more ranked them by a model of the true stock [independent]. High-activity rules, which favour items with high sales, high recorded stock or past errors, detected discrepancies best: the best policies uncovered "over twice the discrepancies detected by random selection". A low-activity rule, ranking items by low recorded stock, found over eight times the unknown out-of-stocks that random selection found [independent]. The ECR report's immediate advice is to "concentrate on high discrepancy fast movers" [independent]. Kök and Shang's model counts when the recorded quantity falls below a threshold, and finds that policy near optimal in a numerical study ([2007, abstract](https://doi.org/10.1287/msom.1060.0136)) [independent: a model]. DeHoratius et al. also describe **zero-balance walks**, in which store staff walk the aisles noting empty locations. Citing Mosconi et al. (2004), which was not opened here, they say such walks can bias records towards negative discrepancies [practice: origin not opened].

**Triggers a warehouse system can raise**, as this unit's working list built from the above: on a schedule (by sales or activity class); when the recorded quantity reaches zero or a threshold (Kök and Shang); when a picker reports a short pick, which checks the location while the error is fresh; and after an exception, a move or a **re-slot** (moving SKUs to new locations, section 6). The short-pick and move triggers are this unit's inference; no source opened tests them.

**Who counts, and what an adjustment is.** An **adjustment** is a transaction that changes the record to match a count, with a reason code saying why. No source opened here says who should count or who may approve an adjustment. The ECR report names manual adjustments as a cause and, in one retailer's data, found discrepancies following them [independent]; that is why the question matters. A common working arrangement, unsourced, is to separate the person who counts from the person who approves. Above a value or quantity limit, a supervisor or the inventory controller approves, and the system logs every adjustment by user. Which approvals a company's own controls require is a question for its finance team and auditors.

## 6. Slotting

**What it is.** Bartholdi and Hackman: "Slotting refers to the careful placement of individual cases within the warehouse"; it "may be thought of as layout in the small" (ch. 9) [practice]. A detailed layout, "usually called a 'slotting'", accounts for the geometry of storage (§8.1) [practice]. SCE2's glossary used the word more broadly, for assigning SKUs to locations, including which go forward (SCE2 §5); Bartholdi and Hackman also use it that way, reporting that they "slotted over 6,000 SKUs" when sizing a forward area (§8.6) [practice]. The research literature treats that broader decision as **storage assignment**: "a set of rules which can be used to assign products to storage locations" (de Koster et al. [2007, §4](https://doi.org/10.1016/j.ejor.2006.07.009)) [practice].

**What it is meant to save.** Bartholdi and Hackman's aims are to "Squeeze more product into available space" and to put popular or heavy items at waist level (ch. 9) [practice]. They report that their own slotting of over 6,000 SKUs for a major chain retailer cut the flow rack its national distribution centre needed from 325 to 285 bays (§8.6) [practice: a textbook report, no measurement design given]. Storing product by family can help, and it also "creates some possible inefficiencies" (§9.3) [practice].

**How the literature treats the policies.** De Koster et al. (§4) [practice] set out the policies:

- **Random storage**: high space utilisation (a low space requirement), at the cost of more travel; it works only under computer control.
- **Closest open location**.
- **Dedicated storage**: the lowest space utilisation of all policies, because a location stays reserved for its product even when that product is out of stock.
- **Full turnover**: fast movers nearest the depot. Its weakness is that "demand rates vary constantly and the product assortment changes frequently", so each change means "a large amount of reshuffling of stock".
- **Class-based storage**: classes by activity, each in its own area, random within it.

They cite Petersen et al. (2004), a simulation finding full turnover better than class-based storage on travel distance, and Roll and Rosenblatt (1983) finding that grouped storage needs more space. Neither origin was opened here.

**Why it belongs in a unit on control.** Every re-slot is a move transaction for each unit moved, and moves are where a location record can split (section 4) (this unit's inference). Corvane (fictional) has two main seasons a year, and about a third of its range carries over between them (case register). Each season therefore brings many SKUs needing new locations (this unit's reading). A slotting change that is not followed by a count of the moved locations moves the errors along with the stock (this unit's inference). Halvern Warehouse (fictional) sells Slotting as a module (case register); that fact is graded nothing and says nothing about real products.

## 7. Returns

**Volume.** Bartholdi and Hackman: returns "run about 5% in retail", and in e-commerce "returns run 25–30%" (§3.7) [practice: no source given]. They also say returns "are expensive to handle (up to ten times the cost of shipping the product out)" (§3.4) [practice]. Neither figure has a measurement behind it in the text read. Guide, Souza, Van Wassenhove and Blackburn put US commercial returns (any reason, within 90 days of sale) above US$100 billion a year. They argue that much of a returned product's value erodes through long processing delays, and model this as a queueing network that includes the marginal value of time ([2006, abstract](https://doi.org/10.1287/mnsc.1060.0522)) [practice: the origin of the figure is not stated in the abstract].

**Receiving a return.** The return arrives as a parcel from a customer or a carton from a store. Corvane (fictional) handles both (case register). The system matches it to the original order where it can, records the item and quantity, and puts it into a held status until graded (working description, unsourced). US drug rules require returned products to be "identified as such and held". The return record holds the name, the lot number, the reason, the quantity and the disposition ([21 CFR 211.204](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211)) [independent].

**Grading.** **Grading** means inspecting a return and assigning a condition, and from it a **disposition** (where the item goes next). For drugs, the rule is strict: if the conditions of storage or shipping cast doubt on the product, it "shall be destroyed unless examination, testing, or other investigations prove" that it meets standards (211.204) [independent]. Products exposed to improper storage in disasters or accidents "shall not be salvaged and returned to the marketplace" (211.208) [independent].

**The routes.** No general source on disposition routes was opened here. As this course's working list, a returned item can go:

- back to sellable stock;
- to stock at a lower grade or price;
- back to the supplier;
- to repair or repacking;
- to a liquidator;
- to recycling or destruction.

Each route is a status change and, where the item is put back, a put-away. For two fashion retailers whose positive discrepancies (physical above record, in its sign) exceeded the negative, the ECR report suggests this "may be attributed to product returns" [independent: stores; an explanation offered, not tested]. A return put on a shelf without its transaction creates hidden stock (section 4).

## 8. Traceability and recalls

A **recall** is the withdrawal of a lot from customers and from stock. **Traceability** is the ability to say where a lot came from and where it went. At the level of what the system must answer, the sources opened give these requirements:

- **Where did each lot go?** US drug distribution records must hold the product, the consignee's (receiver's) name and address, the date and quantity shipped, and the lot or control number (211.196) [independent]. There must be "a system by which the distribution of each lot of drug product can be readily determined", "to facilitate its recall if necessary" (211.150(b)) [independent].
- **Where did it come from, and where did it go next?** For food in the EU, the legal minimum is one step up and one step down, as SCE2 §9 sets out from Ireland's food safety authority [practice].
- **How fast, and in what form?** FDA's food traceability rule, for foods on its list, requires records of **key data elements** (KDEs) for **critical tracking events** (CTEs). The events include shipping, receiving and transformation. It requires a **traceability lot code** (TLC), "a descriptor, often alphanumeric, used to uniquely identify a traceability lot", and a traceability plan. Records go to FDA within 24 hours of a request, or within a reasonable time FDA agrees to. In an outbreak, a recall or another threat, an electronic sortable spreadsheet must be sent within 24 hours ([FDA rule page, modified 4 November 2026](https://fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods)) [practice: the regulator's summary, not the rule text]. On the compliance date, the page states that the original date was 20 January 2026 and that FDA proposed a 30-month extension to 20 July 2028. It says Congress directed FDA not to enforce the rule before that date. Another section of the page still gives January 2026. Whether and when the rule binds an operation is a question for its regulatory counsel.

What this asks of the warehouse record, as this unit's inference: the lot must be captured at receipt (section 1, SCE2 §9) and carried on every move. Lots must be recorded at pick and ship, because a lot inferred from the FIFO rule is wrong whenever a picker takes another pallet (section 2). The system must answer three queries quickly: by lot, every location and status now; by lot, every shipment out; by lot, the receipt it came in on. A record that is accurate on quantity but mixed on lot cannot answer the first query without a count.

## 9. How one inventory error travels: Corvane (fictional)

SCE3 §10 left two errors at the start of this chain: the **short pick** (less at the location than the line asks for) and the wrong pick. Corvane is a fashion retailer with one distribution centre and 60 stores. A web order can be filled from either the centre or a store. Its known trouble is web orders promised from stock the centre cannot find (case register). The steps follow; each says whose action it is and what the record does.

1. **The promise.** The order system promises a customer's two-item web order from the centre's stock. The centre's record shows two units of one size at a pick location; the shelf holds none. The record is phantom stock (section 4).
2. **The short pick.** Mina, who picks web orders (case register), finds the location empty and reports the line short. The other item is picked. A good system now counts the location (section 5) and corrects the record, so that the next order is not promised the same phantom units (this unit's inference).
3. **The split shipment.** A **split shipment** sends one order in more than one delivery. The order system can re-source the missing line to a store. Freya, a store associate, ships web orders from a store with no process for it (case register). The customer receives two parcels at two times, and Corvane pays two shipments (this unit's inference).
4. **The broken promise.** If no store has the size, the line is cancelled or backordered. The **backorder** is the line waiting for stock (WERC's measure, section 10). The promise made at step 1 is broken.
5. **The service call.** The customer calls. Jonas, the customer service agent, answers customers about shipments in transit (case register), and here the call is about a missing item. He sees the order system's record, and the order system was told the stock was there (this unit's inference).

**The wrong pick.** If Mina takes the adjacent size instead, the record of the ordered size drops while its units stay on the shelf (hidden stock). The record of the size taken stays high while its unit leaves (phantom stock). The packing check may catch it (SCE3 §6). If it does not, the customer gets the wrong size, and the return comes back through section 7, where its grading decides whether the item returns to stock. One wrong pick has made two record errors, a return and probably a service call (this unit's inference).

**What it costs.** No public figure was found for the cost of one short or wrong pick in a warehouse. The evidence is indirect: from stores, from a textbook, and from one study of a retailer's distribution-centre records which gives no cost per error:

- Correcting store records to a count raised sales in the ECR report's first experiment (section 5) [independent].
- Kull, Barratt, Sodero and Rabinovich, writing about multichannel retailers that fill store and direct orders "from their distribution centers", found, in one distribution centre serving both channels of a midsize US apparel retailer (540 observations of 27 SKUs in each channel over 10 consecutive business days) and a simulation built on those data, that daily variation in record inaccuracy "increases inventory levels while also decreasing service levels", and that store and direct channels are affected differently ([2013](https://doi.org/10.1111/jbl.12019), author's version, full text) [independent]. The paper measures inaccuracy as a percentage of each SKU's actual on-hand stock and reports no share of records wrong and no cost per error.
- Bartholdi and Hackman's returns cost is a textbook bound (section 7) [practice].

```viz
{"kind": "flow", "per_row": 5, "steps": [{"label": "Phantom stock", "note": "record 2, shelf 0", "tone": 4}, {"label": "Promise", "note": "order system, from the record"}, {"label": "Short pick", "note": "Mina reports the line", "tone": 4}, {"label": "Count and adjust", "note": "location checked, record corrected", "tone": 2}, {"label": "Split shipment", "note": "line re-sourced to a store"}, {"label": "Backorder or cancel", "note": "if no store has it"}, {"label": "Service call", "note": "Jonas answers", "tone": 5}], "caption": "One error's path through Corvane (fictional), from section 9 of this unit: the case register's people and its known trouble, SCE3 section 10's short pick, and section 5's count on a short pick. The path and the order of steps are this unit's inference; no step is measured."}
```

## 10. The inventory measures the benchmark surveys report

WERC's 2025 survey asks for 2024 performance on the measures below; the names are exactly WERC's ([WERC DC Measures Survey - 2025](https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf)) [practice]. As SCE2 §8 and SCE3 §12 found, the document gives no definitions (they sit in pop-ups in WERC's online tool), no sample and no values. Two further searches on 24 Nov 2026 found no WERC definitions page (flags F20, F28). **No WERC value is given here**, and the definitions below are the course's own. A vendor's description exists for one of them: a 2025 infographic by Hyster-Yale Materials Handling, Inc., attributing its metrics to WERC's 2025 DC Measures Report, defines inventory count accuracy by location as "The accuracy, by location, of the physical inventory compared to the reported inventory" and gives best in class as at or above 99.5%; it states no sample ([Hyster-Yale, "Top 12 distribution center metrics", 2025](https://www.yale.com/globalassets/coms/yale/north-america/documents/white-papers/snack-drawer/YALE-1520_WERC-DC-Metrics-infographic.pdf)) [vendor-reported]. It is a vendor's page, not WERC's.

| Measure (WERC's name) | Working definition (course's) |
|---|---|
| Inventory Count (Percent by Location) | Locations whose count matched the record, over locations counted |
| Days on Hand - Finished Goods Inventory | Finished-goods stock divided by average daily shipments |
| Inventory Days of Supply | Inventory divided by average daily cost of goods sold (WERC's cash-to-cash block) |
| Backorders as a Percentage of Total Lines | Lines not shipped for lack of stock, over all lines ordered (as SCE3 §12) |
| Order Picking Accuracy | Orders or lines picked with no error, over all picked (as SCE3 §12) |
| Average and Peak Warehouse Capacity Used; Cube Utilization; Pallets Per Square Feet; Honeycomb Percentage | Space measures: positions or volume occupied, over available; honeycombing as SCE2 §4 defines it |

APQC, a benchmarking organisation, defines **inventory accuracy** as the absolute value of the sum of the variance between physical inventory and perpetual inventory, in percent. Its page shows a sample of 4,283 and no values ([APQC, "Inventory accuracy"](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/inventory-accuracy)) [practice]. Note that the two definitions measure different things. WERC's name counts locations; APQC's sums variances. A summed variance lets overs cancel unders, while a location count does not (this unit's inference).

**Common claim C4: "Good sites run at 99.9% inventory accuracy."** As it circulates, the claim gives one number without a definition. What the evidence opened here shows:

- No independent source opened here reports the share of warehouse records that match the shelf, at 99.9% or any other level. Kull et al. (2013), in one apparel retailer's distribution centre (27 SKUs per channel, 10 business days), measured inaccuracy as a percentage of each SKU's on-hand stock: average bias of −2.27% in the direct channel and −0.71% in the store channel, and average daily variability of 5.78% and 12.04% [independent]. That is a different measure from a share of accurate records.
- A 2025 infographic by Hyster-Yale Materials Handling, Inc., presenting WERC's 2025 report, gives best in class for inventory count accuracy by location as at or above 99.5%, with no sample stated (section 10) [vendor-reported].
- The store studies opened here that report a rate found 65%, about 59.54% and 31% of records not matching. They used different samples, periods and thresholds (section 4) [independent].
- The ECR report counts a one-unit difference as an error [independent]. A figure computed with a tolerance band, by value, or with overs netted against unders is not the same measure.

Before comparing a quoted accuracy figure, ask four things: by location, by SKU or by value; with what tolerance; netted or absolute; counted how (this unit's inference). No independent source found supports the claim as stated.

## On a site visit

At the stock and the counting desk, look for and ask:

- **Pick one location and read its record.** Does the record show SKU, quantity, lot, date, status and owner? Compare it with the shelf (section 1).
- **What is on hold now, since when, and who released the last lot?** Is quarantine stock physically apart or only flagged (section 3)?
- **Does the handheld direct the picker to a dated location, and what happens if the picker takes another?** (Section 2.)
- **What triggers a count here?** Ask for a schedule, a zero or low balance, a short pick, a re-slot. Who counts, and are they the people who picked (section 5)?
- **Show me last week's adjustments by reason code and by user.** Who approves an adjustment, and above what limit (section 5)?
- **When was the last re-slot, and were the moved locations counted afterwards?** (Section 6.)
- **Follow one return from the dock to its disposition.** Ask where it waits, who grades it, and how long it takes (section 7).
- **Name a lot and ask for every location and every customer shipment that holds it.** Time the answer (section 8).
- **Which of WERC's inventory measures does the site report, by whose definition, and does it net overs against unders?** (Section 10.)

## Self-check

1. **What did DeHoratius and Raman (2008) find, and in what setting?**
   Nearly 370,000 records from 37 stores of one retailer; 65% inaccurate. Auditing practices were associated with lower inaccuracy, and store complexity and distribution structure with higher. These are correlations from an abstract (section 4).
2. **What does "phantom inventory" mean in DeHoratius et al. (2023), and why check the sign before comparing two studies?**
   The record shows more than the shelf. The ECR report signs discrepancies the other way round (section 4).
3. **What do US drug rules require before received material may be used?**
   It is stored under quarantine until tested or examined and released by the quality control unit. Rejected material is controlled under a quarantine system (section 3).
4. **What happened to store records after a count in the ECR experiment?**
   Negative inaccuracies (physical below record) accumulated over time; positive ones stayed fairly stable (section 5).
5. **Which count-selection rules beat random selection in DeHoratius et al. (2023), and by how much?**
   High-activity rules, such as ranking by sales, found the most discrepancies, the best over twice what random selection found. A rule ranking by low recorded stock found over eight times the unknown out-of-stocks (section 5).
6. **What weakness of full-turnover storage do de Koster et al. name?**
   Demand and the assortment keep changing, so each change means reshuffling stock (section 6).
7. **What must a US drug distribution record hold for a recall?**
   The product, the consignee's name and address, the date and quantity shipped, and the lot or control number. The distribution of each lot must be readily determinable (section 8).
8. **A colleague says good warehouses run at 99.9% accuracy. What do you answer?**
   No independent source opened here reports a warehouse rate. Measured store studies found 31% to 65% of records wrong. Ask by what unit, with what tolerance, and whether overs are netted against unders (section 10).

## Deliverable

### A. Cause tree for inventory errors: Corvane (fictional)

Corvane (fictional) is a fashion retailer with 60 stores in four European countries and one website. It has one 28,000 m² distribution centre and about 18,000 items, counting size and colour separately. Its flows are store replenishment by carton and single item, web orders of one to three items, and returns from web and stores. It has about 140 staff in a normal week and about 260 in peak, the difference from agencies. Its warehouse system is about twelve years old and near the end of its vendor's support. Known trouble: web orders promised from stock the centre cannot find (case register). People: Carla, inventory controller, answers for the stock record at receiving and put-away; Mina picks web orders; Tobias supervises outbound; Jonas works in customer service; Freya ships web orders from a store (case register).

The tree has four branches, one per stage where an error can enter. Each row is a cause to look for at Corvane, not a finding that it occurs there. "Finds it" names who notices first in the chain of section 9; where the register names no one, the cell says so.

| Branch | Cause | Where it enters | Where it shows in the system | Who finds it |
|---|---|---|---|---|
| **1. Inbound** | 1.1 Carton count accepted unchecked, or the wrong size or colour recorded (SCE2 §3.4) | Check and count | Phantom stock of one size, hidden stock of another, from the first day | Mina at a short pick; Carla at a count (assumption) |
| | 1.2 Carton put to a location other than the one scanned (SCE2 §3.8) | Put-away | Two wrong locations | Mina at a short pick; whoever counts the second location |
| | 1.3 Goods left in staging the record does not know (SCE2 §3.3) | Unload | Stock received but at no location | Not in the register |
| **2. Storage and moves** | 2.1 Forward location restocked from the wrong reserve location (SCE2 §6) | Replenishment | Reserve location phantom; forward location over | Not in the register |
| | 2.2 Seasonal re-slot moves stock without a count afterwards (section 6) | Re-slotting | Errors carried to new locations | Carla, if moved locations are counted (assumption) |
| | 2.3 Picker takes from a convenient location, not the directed one (B&H §2.4) | Picking | Two locations wrong | Next picker at either location |
| **3. Picking and packing** | 3.1 Short pick confirmed as full (SCE3 §10) | Picking | Phantom stock persists; order ships short | Customer, then Jonas |
| | 3.2 Wrong size or colour taken (section 9) | Picking | Ordered size hidden, taken size phantom | Packer, if checked (SCE3 §6); else the customer |
| | 3.3 Damaged unit set aside without a status change (section 3) | Picking or packing | Phantom stock | Not in the register |
| **4. Returns and adjustments** | 4.1 Web or store return put back to a shelf without a transaction (section 7) | Returns | Hidden stock | A count; the ECR report suggests fashion overs may come from returns (section 7) |
| | 4.2 Return put back at the wrong grade or location (section 7) | Grading | Wrong status or location | Not in the register |
| | 4.3 Adjustment made to match a miscount (section 5) | Counting | Correct record made wrong | Next count of the location |
| | 4.4 Theft (section 4) | Anywhere | Phantom stock | A count |

How the known trouble maps: "promised from stock the centre cannot find" is phantom stock. The phantom-stock causes are 1.1, 1.2, 2.1, 2.3, 3.1, 3.2, 3.3 and 4.4 (this unit's reading of the register). Which of them dominates at Corvane is not in the register. A count by reason code at the locations of short picks would show it (section 5).

### B. Count plan: Ostrel Foods (fictional)

Ostrel Foods (fictional) is a food distributor with about 4,500 items, chilled, frozen and ambient, most of them dated. It has one warehouse with three temperature zones, picks by the case onto roll cages, and starts work in the evening for delivery the next morning. Its systems are an ERP with a warehouse module. Known trouble: short-dated stock found too late; substitutions agreed by phone and not recorded; drivers returning with refused goods. People: Bram, reach-truck driver for put-away and replenishment on nights; Ilse, team lead for chilled picking; Aart, operations director (case register). Chilled items have shelf lives counted in days, and demand is a few hundred fast items and a long tail of slow ones (case register, from Supply Chain Planning).

Every choice below is a design decision for the case, drawn from sections 2, 3 and 5. The count windows and the roles assigned are this unit's assumptions (listed in the notes).

| Element | Plan | Basis |
|---|---|---|
| What a count records | Case quantity, lot and date at each location; each count records zone and status | Sections 1, 2; dates are what Ostrel's trouble turns on |
| Discrepancy rule | Any difference of one case, or any date or lot mismatch, is a discrepancy; no tolerance | ECR's no-tolerance definition (section 4) |
| Sign | Record minus physical: positive is phantom | DeHoratius et al. 2023 (section 4) |
| Scheduled counts: chilled | Fast chilled items counted by rotation, at a set depth each day, ranked by recent sales and past error | Section 5 (DeHoratius et al. 2023; ECR fast movers) |
| Scheduled counts: frozen and ambient | Long-tail items ranked by days since last count | Section 5 (DeHoratius et al. 2023: days since the last count) |
| Trigger: date | Any location whose earliest date falls within the item's shelf-life window, counted and checked for date | Section 2; Ostrel's known trouble |
| Trigger: zero or low balance | Location counted when the record reaches zero or a threshold | Section 5 (Kök and Shang, a model; DeHoratius et al. 2023, citing Mosconi et al. 2004, say zero-balance walks can bias records towards negative discrepancies) |
| Trigger: short pick | Location counted the same night when a picker reports a short case | Section 5 (inference), section 9 |
| Trigger: substitution | Where a phoned substitution was shipped, both items' locations counted next window | Ostrel's known trouble; section 4 (wrong pick) |
| Trigger: refused goods | Goods a driver brings back held as returned, graded, then put away with a transaction; location counted | Sections 3, 7; Ostrel's known trouble |
| When | Scheduled counts in the daytime, before picking starts in the evening; trigger counts within the shift | Assumption; register: work starts in the evening |
| Who counts | A counter who did not pick or put away the location that day; not Bram for his own put-aways | Section 5 (working arrangement, unsourced) |
| Adjustments | Each with a reason code (miscount at receipt, put-away error, pick error, damage, expiry, theft, unknown); above a limit, approval by Aart or someone he names who neither picks nor puts away (assumption); all logged by user | Section 5; who approves is Ostrel's control decision for its finance team |
| Holds | Expired or doubtful stock moved to a held status at the count, never adjusted out unrecorded | Section 3 (US drug rules applied to food: this unit's inference) |
| Measures | WERC's Inventory Count (Percent by Location) and Backorders as a Percentage of Total Lines, with the course's definitions; discrepancies by reason code and zone | Section 10 |
| Review | Aart reviews weekly: discrepancies by reason, short picks, short-dated stock found by date trigger versus at the customer | Register (Aart, operations director); measures from section 10 |

### C. Template: cause tree for inventory errors

Fill one row per cause for a real operation, or for a product by naming the screen or transaction where each cause enters and shows. Mark each cell's grade (independent, analyst, vendor-reported, practice) or "observed".

Operation or product: ______ (name; kind of company; region) · Goods: ______ (eaches, cases, pallets; dated; serialised; owners) · Date filled: ______ · Sources used: ______ (each with its grade)

| Branch | Cause | Where it enters | Where it shows in the system | Who finds it |
|---|---|---|---|---|
| 1. Inbound | ______ (miscount, wrong item, wrong location, unrecorded staging) | ______ (the step and its screen) | ______ (phantom, hidden, wrong lot, wrong status) | ______ (the role that notices first) |
| 2. Storage and moves | ______ (replenishment, re-slot, convenient-location picks) | ______ | ______ | ______ |
| 3. Picking and packing | ______ (short pick confirmed, wrong pick, damage unrecorded) | ______ | ______ | ______ |
| 4. Returns and adjustments | ______ (returns without transaction, wrong grade, wrong adjustment, theft) | ______ | ______ | ______ |

Below the table: the operation's known trouble and which causes produce it (______); the evidence of which cause dominates, with its grade (______, or "not known"); the count that would find out (______).

### D. Template: count plan

Operation: ______ (name; kind; region) · Items and zones: ______ · Shifts and quiet windows: ______ · Date filled: ______

| Element | Plan | Basis (source and grade, or "assumption") |
|---|---|---|
| What a count records | ______ (quantity; lot; date; status; owner) | ______ |
| Discrepancy rule | ______ (tolerance or none; by unit, case or value) | ______ |
| Sign convention | ______ (record minus physical, or the reverse) | ______ |
| Scheduled counts | ______ (which items, at what depth, ranked by what) | ______ |
| Triggers | ______ (zero or low balance; short pick; date; move or re-slot; exception) | ______ |
| When | ______ (windows outside picking; full count date, if any, and who requires it) | ______ |
| Who counts | ______ (role; separated from whom) | ______ |
| Adjustments | ______ (reason codes; approval limits; who approves; log) | ______ (the company's finance team and auditors decide approvals) |
| Holds | ______ (what goes on hold at a count, who releases) | ______ |
| Measures | ______ (WERC name; whose definition; netted or absolute) | ______ |
| Review | ______ (who, how often, what they look at) | ______ |

### E. Glossary lines

Added to SCE1's, SCE2's and SCE3's working glossary; each term as this unit uses it.

| Term | Working definition | Source |
|---|---|---|
| Location | An addressed place where goods can be, down to a forklift's forks | B&H §4.2 [practice] |
| Perpetual (book) inventory; physical inventory | The continuously updated record; what is actually there | Course terms; B&H ch. 18 names book and physical [practice] |
| Lot; batch | The production or receipt group a unit belongs to | 21 CFR 211.130 [independent] |
| Serial number | An identifier for one unit; with a GTIN, it identifies one trade item | GS1 support page [independent] |
| Status | An attribute controlling whether stock may be allocated | Course term; 21 CFR 211.82–211.89 [independent] for quarantine and rejected |
| Owner | Whose goods a record holds, in a multi-client site | Course term; not sourced |
| Rotation rule; FIFO; FEFO | Which unit leaves first: oldest receipt, or earliest date | SCE2 §9; 21 CFR 211.150(a) [independent] |
| Quarantine; hold | Stock kept in the record but withheld from use until released | 21 CFR 211.82(b), 211.84(a) [independent] |
| Inventory record inaccuracy (IRI) | The record differing from what is physically there | DeHoratius & Raman 2008 [independent] |
| Phantom inventory; hidden inventory | Record above physical; record below physical | DeHoratius et al. 2023 [independent] |
| Unknown out-of-stock | Empty shelf while the system shows stock | DeHoratius et al. 2023 [independent] |
| Full count; stocktake; physical inventory | Every location counted at once | Course term; ECR report [independent] |
| Cycle count | A selected part of the stock counted on a schedule or trigger | Course term; B&H §4.3 [practice] |
| Counting depth | The share of items counted | DeHoratius et al. 2023 [independent] |
| Zero-balance walk | Staff walk the aisles noting empty locations | DeHoratius et al. 2023 [practice] |
| Adjustment | A transaction changing the record to match a count, with a reason | Course term |
| Slotting | Careful placement of cases in locations; "layout in the small"; B&H also use it for assigning SKUs to locations (§8.6) | B&H ch. 9, §8.6 [practice] |
| Storage assignment; random, dedicated, full-turnover, class-based | Rules assigning products to locations, and the main policies | de Koster et al. 2007 §4 [practice] |
| Wrong pick | A pick that takes the wrong item or size | Course term |
| Split shipment | One order sent in more than one delivery | Course term |
| Backorder | An ordered line waiting for stock | Course term; WERC names the measure [practice] |
| Grading; disposition | Inspecting a return and assigning its condition; where it goes next | Course terms; 21 CFR 211.204 records disposition [independent] |
| Recall; traceability | Withdrawing a lot; saying where a lot came from and went | Course terms; 21 CFR 211.150(b) [independent] |
| Traceability lot code (TLC); key data elements (KDEs); critical tracking events (CTEs) | FDA food rule's lot identifier, the data recorded, and the events they are recorded at | FDA rule page [practice] |
| Inventory accuracy (APQC) | Absolute value of the summed variance between physical and perpetual inventory, percent | APQC [practice] |

## Notes: facts for the case register

| Unit | Operation | Fact |
|---|---|---|
| SCE4 | Corvane | When a picker reports a short pick on a web order, the order system can re-source the missing line to a store, where Freya ships it, so the customer receives two parcels (section 9; worked chain, this unit's inference). |
| SCE4 | Corvane | Jonas also answers customers about items missing from web orders (section 9). |
| SCE4 | Corvane | Carla counts locations after short picks and after re-slots (deliverable A; assumption). |
| SCE4 | Corvane | Each season brings many SKUs needing new locations (section 6; this unit's reading of the two seasons and the one-third carry-over). |
| SCE4 | Ostrel Foods | Scheduled counts run in the daytime, before evening picking; trigger counts run within the shift (deliverable B; assumption). |
| SCE4 | Ostrel Foods | A counter did not pick or put away the location that day; adjustments above a limit are approved by Aart or someone he names (deliverable B; assumption). |
| SCE4 | Ostrel Foods | Aart reviews count results weekly (deliverable B; assumption). |

## Sources

All addresses opened on 24 November 2026; the source log (sources.md) gives what was read at each.

- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 2, 3, 4, 8, 9, 18. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- Guide, V. D. R., Jr., Souza, G. C., Van Wassenhove, L. N. & Blackburn, J. D. (2006). Time Value of Commercial Product Returns. *Management Science* 52(8), 1200–1214. https://doi.org/10.1287/mnsc.1060.0522 (abstract, read at https://econpapers.repec.org/RePEc:inm:ormnsc:v:52:y:2006:i:8:p:1200-1214; a 2005 working-paper version is at https://drum.lib.umd.edu/items/76d3af97-f39a-4e91-9e7e-19fceb1806f1/full)
- de Koster, R., Le-Duc, T. & Roodbergen, K. J. (2007). Design and control of warehouse order picking: A literature review. *European Journal of Operational Research* 182(2), 481–501. https://doi.org/10.1016/j.ejor.2006.07.009 (read in the version of record at https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf)
- DeHoratius, N. & Raman, A. (2008). Inventory Record Inaccuracy: An Empirical Analysis. *Management Science* 54(4), 627–641. https://doi.org/10.1287/mnsc.1070.0789 (abstract, read at https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.1070.0789)
- DeHoratius, N., Holzapfel, A., Kuhn, H., Mersereau, A. J. & Sternbeck, M. (2023). Evaluating Count Prioritization Procedures for Improving Inventory Accuracy in Retail Stores. *Manufacturing & Service Operations Management* 25(1), 288–306. https://doi.org/10.1287/msom.2022.1119 (full text, read at https://pubsonline.informs.org/stoken/default+domain/IAC-INNOVATION-IN-RETAIL/full/10.1287/msom.2022.1119)
- Fleisch, E. & Tellkamp, C. (2005). Inventory Inaccuracy and Supply Chain Performance: A Simulation Study of a Retail Supply Chain. *International Journal of Production Economics* 95(3), 373–385. https://doi.org/10.1016/j.ijpe.2004.02.003 (abstract, read at https://www.alexandria.unisg.ch/21602/)
- Kök, A. G. & Shang, K. H. (2007). Inspection and Replenishment Policies for Systems with Inventory Record Inaccuracy. *Manufacturing & Service Operations Management* 9(2), 185–205. https://doi.org/10.1287/msom.1060.0136 (abstract, read at https://pubsonline.informs.org/doi/fpi/10.1287/msom.1060.0136)
- Kull, T. J., Barratt, M., Sodero, A. C. & Rabinovich, E. (2013). Investigating the Effects of Daily Inventory Record Inaccuracy in Multichannel Retailing. *Journal of Business Logistics* 34(3), 189–208. https://doi.org/10.1111/jbl.12019 (author's version, full text, read at https://core.ac.uk/download/213060804.pdf; record at https://epublications.marquette.edu/mgmt_fac/252)
- Rekik, Y., Syntetos, A. A. & Glock, C. H. *Inventory Inaccuracy in Retailing: Does it Matter?* ECR Community Shrinkage & On-Shelf Availability Group, October 2019. https://orca.cardiff.ac.uk/142664/1/84486%20ECR%20Inventory%20Inaccuracy%20Report.pdf
- APQC. "Inventory accuracy". Open Standards Benchmarking measure page, undated. https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/inventory-accuracy
- United States. Code of Federal Regulations, Title 21, Part 211, "Current Good Manufacturing Practice for Finished Pharmaceuticals", §§ 211.82, 211.84, 211.87, 211.89, 211.130, 211.137, 211.142, 211.150, 211.196, 211.204, 211.208. eCFR, up to date as of 16 June 2026. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211
- US Food and Drug Administration. "FSMA Final Rule on Requirements for Additional Traceability Records for Certain Foods". Modified 4 November 2026. https://fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods
- WERC. "WERC DC Measures Survey - 2025". https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf
- GS1. "How does 'serialisation' differ from 'unique identification' in the GS1 System?" GS1 support article, modified 28 August 2024. https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-
- Hyster-Yale Materials Handling, Inc. "Top 12 distribution center metrics" (infographic, from WERC's 2025 DC Measures Report), © 2025. Vendor-reported. https://www.yale.com/globalassets/coms/yale/north-america/documents/white-papers/snack-drawer/YALE-1520_WERC-DC-Metrics-infographic.pdf

## Unsure list

# Unsure: SCE4

1. The ECR Community report (Rekik, Syntetos & Glock, 2019) is graded independent as an association report with its sample stated; it was commissioned by an industry group whose members are retailers and suppliers, and it was read at Cardiff University's repository, not on ECR's own page.
2. ECR Experiment I: the "benefit resulting from the stocktake" of 3.83% to 8.38% (average 5.98%) is given in the unit as higher sales in counted test stores than in uncounted control stores; the exact comparison basis was read through an extraction and not confirmed in the report's tables.
3. DeHoratius et al. (2023): the list of count-selection rules (sales, recorded decreases or increases, past error, forecast sales, days since last count, two model-based) is the unit's paraphrase of rule names read through an extraction.
4. DeHoratius & Raman (2008): which of 67.6% and 69.0% is "across stores" and which "across categories" follows the abstract's order as extracted.
5. Every Bartholdi & Hackman quotation (§2.4 "creating discrepancies between book and physical inventory at two locations"; §4.2; ch. 9 "Slotting refers to..."; §3.4 "up to ten times"; §3.7 "about 5% in retail", "25–30%"; ch. 18) and the §8.6 figure of 325 to 285 bays came from a fetch tool's extraction and were not re-read against the PDF.
6. The title of 21 CFR Part 211, "Current Good Manufacturing Practice for Finished Pharmaceuticals", was taken from search-result addresses, not read as a heading on the eCFR page.
7. Fleisch & Tellkamp (2005) is graded practice because the causes are the model's premise, not a measurement; a reader of SCE1's key could grade it independent.
8. The FDA traceability page is internally inconsistent on the compliance date (2028 proposed and enforcement-deferred; January 2026 still stated elsewhere on the page); the unit reports both.
9. Kull et al. (2013): read in full in the author's version (core.ac.uk); the study is of one distribution centre of a midsize US apparel retailer, as the unit now says. The sign convention of its bias figures (Equation 1) was not checked.
10. Blackburn, Guide, Souza & Van Wassenhove (2005): the repository's metadata lists Blackburn alone and its page lists four authors in another order; the unit lists all four alphabetically.

Object: the inventory record of one storage location (SKU, quantity, lot, date, status, owner), sections 1 and 4

Fresh check 2026-11-24 (claude-opus-5-5): fix · 3 errors, 18 should-fix, 12 minor; report audits/supply-chain-execution/fresh-check-SCE4.md
