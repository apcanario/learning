---
code: SCE7
title: Transportation in practice
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-24
search: off
intro: Who moves freight and how they are paid, and one road shipment followed from plan to payment: the parties and their US and European names, the modes, how truckload capacity is bought and why carriers refuse loads, what the transport system holds, the documents by region, and the shipment lifecycle map built for two fictional operations.
---

# SCE7 · Transportation in practice

Grades follow SCE1's key: every claim that carries a number, a mechanism or a recommendation ends with [independent], [analyst], [vendor-reported] or [practice]. The text of a treaty, statute or regulation is graded independent for what it says, as SCE1 does; a public authority's own account of a law or of its own study is graded practice until flag F18 is decided. Official statistics whose survey design the statistical office states are graded independent, as SCE1 graded US Census data. Lines marked as this unit's inference carry no grade. Where no source was opened, the unit says so and the line is the course's working description and makes no claim. Every reference was opened on 24 November 2026, except two added at the fresh check and opened on 25 November 2026 (ICAO's 2024 revised limits; the UN Treaty Collection's status page for the 1978 CMR Protocol) and three added by correction and opened on 28 November 2026 (UN/CEFACT TRADE/CEFACT/2001/33; the 1978 CMR Protocol in the UN Treaty Series; Directive 2011/7/EU, Article 3); the source log gives what was read at each.

The course's map (SCE1 §2) gives transport two steps, "plan and tender" and "carry and track", and a share of "settle". This unit opens those steps up. Region matters more here than in the warehouse units: the same job carries a different legal name, and the same shipment a different document, in the United States and in Europe. Each term below says where it belongs.

## 1. The parties and what each sells

**Shipper.** The company whose goods move and which buys the carriage (SCE1 glossary). **Consignee.** The party the goods are delivered to; the CMR Convention, which governs international road carriage for reward where the places of taking over and delivery are in two countries, at least one of them a contracting country (Art. 1(1)), requires the consignee's name and address on the consignment note (Art. 6(1)(e)) ([UN, CMR](https://treaties.un.org/doc/Treaties/1961/07/19610702%2001-56%20AM/Ch_XI_B_11.pdf)) [independent].

**Carrier.** The company that moves the goods. US federal law defines a **motor carrier** as a person providing motor vehicle transportation for compensation (49 U.S.C. §13102(14), 2019 edition) ([US Code](https://www.govinfo.gov/content/pkg/USCODE-2019-title49/html/USCODE-2019-title49-subtitleIV-partB-chap131-sec13102.htm)) [independent]. European statistics call the same business **hire or reward** transport, commercial road freight, and set it against **own account** transport, done by vehicles owned by companies whose main business is something else, such as manufacturing, construction or trade ([Eurostat, road_go metadata](https://ec.europa.eu/eurostat/cache/metadata/en/road_go_esms.htm)) [independent]. Eurostat's survey metadata calls the carriers it samples **hauliers** ([Eurostat, road_go metadata](https://ec.europa.eu/eurostat/cache/metadata/en/road_go_esms.htm)) [independent].

**Broker** (a US legal term). A person, other than a motor carrier, who sells, offers, negotiates for, or holds itself out as providing or "arranging for, transportation by motor carrier for compensation" (§13102(2)) [independent]. A broker sells the arrangement; the truck belongs to someone else. In one large US dataset, 194 of the 1,640 primary carriers that shippers contracted with were non-asset firms, the rest asset-based ([Acocella, Caplice & Sheffi, 2020](https://doi.org/10.1016/j.tre.2020.102073)) [independent]: a shipper's routing guide can hold firms that own no trucks.

**Freight forwarder.** The word means two things. In US road law, a freight forwarder holds itself out to the public to provide transportation for compensation, assembles and consolidates shipments and breaks them down for delivery, takes responsibility for the goods from receipt to destination, and uses a regulated carrier for part of the move (§13102(8)) [independent]. In international trade, FIATA, the federation of forwarders' associations, describes the forwarder as the party who ensures that internationally traded goods move from origin to destination, and its 2004 definition of forwarding services runs from carriage, consolidation, storage, handling, packing and distribution to customs, insurance and collecting payment or documents ([FIATA, "About Freight Forwarding"](https://fiata.org/about-freight-forwarding/)) [practice]. So a European or Asian "forwarder" may sell a whole international chain, while a US "freight forwarder" is a narrower legal category (this unit's reading of the two sources).

**Logistics provider.** A company that runs warehousing or arranges freight for other companies (SCE1 §5). Tandric Logistics (fictional), a logistics provider, has a freight desk that arranges full and part loads with outside carriers for clients, owns no trucks, and is paid for freight at a margin over what the carrier is paid (case register). In US terms that desk does what §13102(2) calls brokering (this unit's reading); whether Tandric is a broker or a forwarder in law, and what licence it needs, is a question for the national transport regulator, not one this course answers.

**Private fleet.** A shipper that moves its own goods in its own vehicles. US law calls it a **motor private carrier**: a person, other than a motor carrier, hauling property it owns, leases or holds, to further its business (§13102(15)) [independent]; in Europe it is own-account transport (Eurostat, above) [independent]. Ostrel Foods (fictional), a food distributor with 40 vehicles of its own (case register), is one. Section 8 takes it up.

| Party | What it sells | US term | European or international term |
|---|---|---|---|
| Shipper | Nothing in this transaction; it buys carriage | Shipper | Shipper; sender on the CMR note (Art. 5) |
| Consignee | Nothing; it receives | Consignee | Consignee (CMR Art. 6) |
| Carrier | Capacity and the move itself | Motor carrier (§13102(14)) | Haulier; hire or reward transport (Eurostat) |
| Broker | The arrangement of a carrier's transport | Broker (§13102(2)) | No legal term sourced here |
| Forwarder | Consolidation and responsibility for the move; internationally, the whole chain and its paperwork | Freight forwarder (§13102(8)), a narrow category | Forwarder (FIATA) |
| Logistics provider | Warehousing, freight arrangement, or both, for other companies | Third-party logistics provider (SCE1) | Same |
| Private fleet | Nothing; it carries its own goods | Motor private carrier (§13102(15)) | Own-account transport (Eurostat) |

## 2. The modes and what decides the choice

A **mode** is the kind of carriage. The course uses six, with these working definitions where no source was opened:

- **Full truckload** (FTL, or TL in the US). One vehicle carries one shipper's shipment from one origin to one destination: in truckload operations the truck is generally dedicated to a single shipment ([Sheffi, 2004](https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2018-07/10_CombinatorialAuctionsInTheProcurementOfTransportationServices.pdf)) [practice].
- **Less-than-truckload** (LTL, a US term) and **groupage** (the term you will hear in Europe; this unit opened no source for it, so it is a working term). Carriers "consolidate many smaller shipments on a single truck" (Sheffi, 2004) [practice]. In the US, LTL freight is classified under the National Motor Freight Classification (NMFC), which gives each commodity a class from 50 to 500 on four characteristics: density, handling, stowability and liability; the class sets what an LTL shipment costs, denser and easier freight taking a lower class and a lower price, and misclassified freight draws reclassification charges ([NMFTA, Classification](https://nmfta.org/standards/classification/)) [practice]. No European equivalent was opened.
- **Parcel.** Individual cartons, each labelled and sorted through a carrier's network. Sheffi groups parcel with LTL as consolidating carriers (2004) [practice]; the rest is the course's working definition.
- **Intermodal.** A container or trailer moved by two or more modes, typically road and rail, without the goods being handled at the change. Working definition: the Eurostat, ITF and UNECE *Glossary for transport statistics* (5th edition, 2019, 744 definitions) defines intermodal terms, but only its product page could be opened ([Eurostat](https://ec.europa.eu/eurostat/web/products-manuals-and-guidelines/-/ks-gq-19-004)).
- **Ocean.** Containers or bulk by sea. This unit opened no source on ocean carriage or its documents.
- **Air.** Cargo by air, under the air waybill (section 7).

**What decides the choice.** One literature review of European studies (published 1990 to 2009 in English or Scandinavian languages, drawing on interviews and surveys of transport buyers, modelling studies excluded) found the core factors to be cost, transport time, reliability and transport quality; once basic quality requirements are met, the decision rests mostly on price; and buyers are generally unwilling to pay extra for lower environmental impact ([Flodén, Bärthel & Sorkina, 2010, abstract](https://research.chalmers.se/en/publication/122890)) [practice: abstract only, and whether the proceedings are peer-reviewed was not confirmed]. A North American review (Meixell & Norbis, 2008) could not be opened. To those factors the physical facts add one more, as this unit's inference from Sheffi's definitions: **shipment size**. A shipment that fills a vehicle goes truckload; one that does not either pays to travel alone or waits to be consolidated with others.

| Mode | What travels | How it is priced (where sourced) | Region notes |
|---|---|---|---|
| Parcel | Single cartons | Not sourced here | Parcel carriers in both regions |
| LTL / groupage | Pallets or part loads consolidated with other shippers' | US: by NMFC class (NMFTA) [practice] | "LTL" US; "groupage" Europe (working term) |
| Full truckload | One shipper's load, one vehicle | Contract rate per lane, or spot (section 3) | "TL" US; "FTL" or "full load" Europe (working terms) |
| Intermodal | Container or trailer on road and rail | Not sourced here | Working definition |
| Ocean | Containers or bulk | Not sourced here | No source opened |
| Air | Cargo, by weight | Not sourced here; liability by weight (section 7) | Montreal Convention, international |

## 3. Buying truckload capacity: contract and spot

Most of what has been studied about buying freight is about US truckload. This section follows two papers read in full and one in abstract.

**The annual bid.** Large shippers buy truckload services through **requests for proposals** (RFPs). The shipper estimates the coming year's freight, often from the previous year's movements, and sends carriers a list of **lanes**, each "a one-way movement from an origin to a destination" with its expected shipments; bids are usually sealed, single-round and evaluated lane by lane; contracts usually last one to two years (Sheffi, 2004) [practice].

**Why lanes interact.** A carrier's cost to serve one lane depends on the rest of the traffic in its network. A carrier that takes many loads into a city strands trucks and drivers there and must send them out empty; a load in the opposite direction (Sheffi's back-and-forth movement; **backhaul** is the course's term) balances the equipment, and a closed loop of lanes raises its use (Sheffi, 2004) [practice]. That is why some shippers let carriers bid on packages of lanes (a **combinatorial auction**). Sheffi reports that shippers using combinatorial auctions save "three to 15 percent of transportation costs while maintaining or increasing their service levels", adds that the saving is hard to attribute to the auction format, and that fewer than 10 percent of lanes in typical auctions are in packages [practice: no measurement design is described].

**The routing guide.** The bid's result is a **routing guide** per lane. The shipper usually makes the lowest bidder the **primary carrier** and keeps other bidders as **backup carriers**, in order; contract prices are private; volume and frequency commitments bind neither side, and only the price binds the carrier (Acocella, Caplice & Sheffi, 2020) [practice: the paper's description of the market it studies]. Scott, Parker and Craighead state the same from the other side: in for-hire truckload contracts "there is typically no legally binding obligation or penalty for either party to offer or accept a load" ([2017, abstract](https://doi.org/10.1287/trsc.2016.0677)) [practice: the abstract's description of the market]. Whether a given contract binds either party is a legal question for the parties' counsel; the sources describe the common practice, not any contract.

**Tendering, and what happens on refusal.** Each load is offered (**tendered**) to the primary carrier, which accepts or rejects it. On a rejection the shipper offers the load to the next backup in the guide, and when the guide is exhausted, to the **spot market**, where the price is set load by load (Acocella et al., 2020) [practice]. Spot is dearer: in one large national shipper's data, spot truckload prices averaged about 62% above contract rates (Scott et al., 2017, abstract) [independent].

The cascade as a decision, from section 3's sources:

```viz
{"kind": "decision", "title": "Where a truckload tender goes", "root": {"q": "Primary carrier accepts the tender?", "tone": 3, "branches": [{"label": "yes", "to": {"outcome": "Moves at the contract rate", "tone": 2}}, {"label": "no", "to": {"q": "A backup carrier in the routing guide accepts?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "Moves at the backup's rate", "tone": 5}}, {"label": "guide exhausted", "to": {"outcome": "Spot market, priced load by load", "tone": 1}}]}}]}, "caption": "The tender cascade of section 3 of this unit: primary carrier, backups in routing-guide order, then the spot market. Sources: Acocella, Caplice and Sheffi (2020), Transportation Research Part E 142, read in full; Scott, Parker and Craighead (2017), Transportation Science 51(4), abstract. US truckload only."}
```

**Where this holds.** Both papers study US truckload. This unit opened no study of how European shippers buy full loads, so applying the cascade to Europe is this unit's inference.

## 4. Why carriers refuse loads: what the research found

**The study read in full.** Acocella, Caplice and Sheffi (2020) analysed 1,933,299 US dry-van, long-haul (over 250 miles) truckload loads from 71 shippers, tendered to 1,640 primary carriers (1,446 asset-based, 194 non-asset; the text elsewhere says 1,650), between September 2015 and May 2019, from a managed services provider's data [independent]. Their measure is the **primary carrier acceptance ratio** (PAR): the share of loads offered to the primary carrier in a week that it accepts. They split the period into market phases. In the soft market (15 April 2016 to 14 April 2017) the average weekly PAR was 81.9% and the average accepted cost per load $1,155.9; in the tight market (1 October 2017 to 30 September 2018), 68.5% and $1,420.7 [independent].

```viz
{"kind": "compare", "title": "Primary carriers' acceptance, soft and tight US truckload markets", "unit": "%", "max": 100, "rows": [{"label": "Soft market, Apr 2016 to Apr 2017", "value": 81.9}, {"label": "Tight market, Oct 2017 to Sep 2018", "value": 68.5}], "caption": "Average weekly primary carrier acceptance ratio (PAR) in two market phases, section 4 of this unit. Source: Acocella, Caplice and Sheffi (2020), Transportation Research Part E 142, 102073: 1,933,299 US dry-van long-haul loads, 71 shippers, Sept 2015 to May 2019."}
```

**What went with refusal.** In the tight market, carriers accepted more of a shipper's loads when the shipper's price stood higher against the market rate for the lane, when its weekly volume varied less, when it offered loads in more weeks of the year, and when drivers waited less at the destination; larger shippers saw lower acceptance (Acocella et al., 2020) [independent]. What a shipper had done in the earlier soft market (its pricing, consistency, performance) did not, in general, predict tight-market acceptance: carriers acted, in the authors' word, like goldfish, with short memories, responding to current behaviour [independent]. When the primary refused, the load cost more: the ratio of the average accepted price after a rejection to the price on acceptance (the **backup premium**) was 1.009 in the soft market and 1.182 in the tight one [independent]. These are associations in observational data and show no cause, and the authors state that their models have low predictive power and lack bid timing and contracted volumes [independent].

**The study read in abstract.** Scott, Parker and Craighead (2017), on one large national shipper's transaction data, found that operational and economic factors drive freight rejection, that the shipper-carrier relationship deters it, and that primary and secondary carriers respond differently [independent, abstract only]. The abstract does not name the factors or state the sample size, so this unit does not.

**What it means for software**, as this unit's inference: the rejection is an event in the shipper's transport system (section 6, step 4), the acceptance ratio is computed from those events, and the levers the 2020 study associates with acceptance (price against market, volume steadiness, offer frequency, dwell at the dock) sit partly in procurement and partly in the warehouse's dock.

## 5. What the transport system holds

SCE1 §3 places the transport system's row on the definition opened here (flag F6). Gartner defines transportation management systems (TMSs) as software supporting "multimodal sourcing, planning and execution of the physical transport of goods" across the supply chain, and lists as mandatory: sourcing capacity from third-party carriers through bid management and optimisation; planning (order and shipment consolidation, mode selection, route determination, carrier selection); execution (turning the shipment plan into carrier communications); visibility (tracking shipments from pickup to delivery); settlement, "Settlement capabilities to match expected transportation charges against actual charges"; and embedded analytics on measures such as on-time performance and cost by mode ([Gartner Peer Insights, TMS market, features updated April 2026](https://www.gartner.com/reviews/market/transportation-management-systems)) [analyst]. The page did not list freight audit and payment, or tendering and rating, as named mandatory items.

So the transport system's own record, on this definition, is the carrier sourcing and its rates, the shipment plan, the carrier communications that execute it, the tracking events, and the expected charge that settlement checks the invoice against. Holding the tender and the carrier's answer there is this unit's reading of "communications with carriers"; the definition does not name tendering, and SCE1 §3 keeps it a working placement. Paying the carrier is not in the definition; where the payment is held was SCE10's question, and SCE10 §7 keeps SCE1's working placement: the transport system holds the approved charge, the ERP the payment (working).

**On the case register's fictional vendors.** Halvern Transport (fictional) lists Rating and Tendering, Fleet Routing, Tracking, Freight Audit and Claims modules; Varnby Transport (fictional) is sold with Varnby's ERP (case register). On section 6's steps, as this unit's placement: Rating and Tendering at steps 2 to 4, Tracking at step 7, Freight Audit at step 10 and at step 11 up to the approved charge, the payment itself being in the ERP (SCE10 §7, deliverable A row 15; working), Claims at step 12, and Fleet Routing in section 8's problem, outside bought freight. These are register facts, graded nothing, and say nothing about any real product.

## 6. The life of one shipment, step by step

Twelve steps, from plan to claim, for a bought road shipment. For each: the physical event, the people, what the system does, how it commonly fails, and the measure, where a source or the case register gives them. Where a step below leaves one out, section 10 gives every step's common failure, section 11 defines the measures, and the deliverable's maps give each step's party, system touchpoint and measure, or say that none is sourced. Where no source was opened, the step is the course's working description and says so.

**1. Plan and consolidate.** *Event:* none yet; orders become shipments. *People:* a transport planner at the shipper. *System:* consolidates orders into shipments and selects mode and carrier, both mandatory TMS planning capabilities in Gartner's definition [analyst]. *Failure:* orders released to the warehouse too late for the carrier's departure (SCE3 §8). *Measure:* vehicle fill (working definition, section 11).

**2. Rate.** *Event:* none; the shipment is priced. *System:* applies the contract rate for the lane from the routing guide (section 3); for LTL in the US, the freight class (section 2). *Failure:* a wrong class or missing rate, which surfaces later as an invoice that does not match (NMFTA on reclassification charges) [practice]. *Measure:* none sourced.

**3. Tender.** *Event:* the load is offered to a carrier. *System:* sends the tender. The standards body X12 publishes transaction set 204, Motor Carrier Load Tender, and 990, Response to a Load Tender ([X12, 990](https://x12.org/node/4450)) [independent]; which regions use X12 was not sourced here. Carriers may also be booked in a carrier's own portal, as Corvane (fictional) books them (case register). *Failure:* tender sent with too little lead time; the 2020 study measures tender lead time as one of its variables (Acocella et al.) [practice: the paper's definition].

**4. Accept or refuse.** *Event:* the carrier commits a truck, or declines. *System:* records the answer and moves the tender down the routing guide on a refusal (section 3). *Failure:* refusal, and the cost that follows (section 4). *Measure:* primary carrier acceptance ratio (section 11).

**5. Book a dock.** *Event:* a pickup time and door are agreed at the shipper's site, and a delivery time at the consignee's. SCE2 §3.2 reports 30-minute appointment windows as not unusual at receiving docks, from Bartholdi and Hackman [practice]. *Failure:* the truck arrives to a busy dock and waits (section 9). *Measure:* dwell time (section 11).

**6. Pick up.** *Event:* the goods are loaded and the driver signs for them. *Documents:* the consignment note or bill of lading (section 7). *System:* the warehouse records departure (SCE3 §7); the transport system records the shipment as picked up (working description). *Failure:* a missed pickup or a load not ready (SCE3 §8). *Measure:* on-time pickup (section 11).

**7. Track.** *Event:* the goods are in transit. *System:* receives status events; Gartner's definition calls for tracking from pickup to final delivery [analyst]. One standard message for this is IFTSTA, the international multimodal status report message (a United Nations Standard Message of UN/EDIFACT, listed in UN/CEFACT's D.01A documentation, [TRADE/CEFACT/2001/33](https://digitallibrary.un.org/record/433163/files/%5EE_ECE_%5ETRADE_CEFACT_2001_33-EN.pdf) [independent]; GS1's EANCOM subset uses directory D.01B), which in GS1's EANCOM subset reports the transport status, or a change in it, between agreed parties, including exceptions and their reasons ([GS1, EANCOM 2002 S3, IFTSTA](https://www.gs1.org/sites/gs1/files/docs/eancom/ean02s3/part2/iftsta/intro.htm)) [independent]. *Failure:* no event, or a late one, so the customer is told nothing (working description). *Measure:* none sourced.

**8. Deliver and prove delivery.** *Event:* the consignee takes the goods and signs. Under the CMR, the second copy of the note accompanies the goods (Art. 5(1)), and if the consignee takes delivery without checking the goods with the carrier or without a reservation (at delivery for apparent loss or damage; in writing within seven days, Sundays and public holidays excepted, for loss or damage that is not apparent), taking delivery is prima facie evidence that the goods arrived in the condition the note describes (Art. 30(1)) [independent]. **Proof of delivery** (POD) is the signed record of the hand-over (course term). *Failure:* a signature without a check, which weakens a later claim (this unit's inference from Art. 30). *Measure:* on-time delivery (section 11).

**9. Invoice.** *Event:* none; the carrier bills. In the US, the 2009 edition of the federal rules on payment of transportation charges requires a motor carrier extending credit to present its **freight bill** within 7 days of receiving a prepaid shipment or delivering a collect one, Saturdays, Sundays and holidays excluded, and to state the payment due date and any late-payment terms on the bill (49 CFR §377.205) ([CFR 2009](https://www.govinfo.gov/content/pkg/CFR-2009-title49-vol5/pdf/CFR-2009-title49-vol5-part377.pdf)) [independent]. Whether the current text is the same was not checked. No European rule was opened.

**10. Check against the agreed rate.** *Event:* none; the bill is compared with what was agreed. *System:* settlement matches expected charges against actual ones (Gartner) [analyst]. *People:* a freight desk or accounts payable; at Tandric (fictional), Priya tenders loads and checks carriers' invoices (case register). *Failure:* extra charges for waiting, reclassification or re-delivery that the system did not expect (this unit's inference from steps 2 and 5). *Measure:* invoice match rate (section 11). No independent study of freight invoice error rates was found.

**11. Pay.** *Event:* money moves. Under the same 2009 US rules, the default credit period is 15 days from the day after the bill is presented, and a tariff may set another but not longer than 30 calendar days (49 CFR §377.203) [independent]. For the European Union, Directive 2011/7/EU requires Member States to ensure that, where the contract fixes no date, the creditor is entitled to interest for late payment after 30 calendar days from the debtor's receipt of the invoice, and that a contractual payment period between businesses does not exceed 60 calendar days unless expressly agreed and not grossly unfair to the creditor (Art. 3(3)(b)(i), 3(5), as adopted; [legislation.gov.uk copy](https://www.legislation.gov.uk/eudr/2011/7/article/3/adopted)) [independent]; the text read is the 2011 text as adopted, so a later amendment is not ruled out (SCE10 §5). Which rules apply to a given carrier relationship is a question for the finance team and its legal advisers. *System:* the ERP pays, on SCE1's working placement.

**12. Claim for loss or damage.** *Event:* goods arrive short or damaged. In the US, a carrier must issue a receipt or bill of lading and is liable for the actual loss or injury to the property; failure to issue the document does not change that liability; and it may not allow less than 9 months to file a claim or 2 years to sue (49 U.S.C. §14706(a)(1), (e)(1)) ([US Code](https://uscode.house.gov/us/usc/119-136/t49/s14706/)) [independent]. Under the CMR, the carrier is liable for total or partial loss, damage and delay between taking over and delivery (Art. 17(1)), compensation is capped by weight (Art. 23(3), in the 1956 text 25 gold francs per kilogram of gross weight short), and the limitation period is one year, three for wilful misconduct (Art. 32(1)) [independent]. A Protocol of 5 July 1978, in force since 28 December 1980 ([UN Treaty Collection, status of the Protocol](https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-11-a.en.pdf)) [independent], replaced the Art. 23(3) cap for the countries party to it with 8.33 units of account per kilogram of gross weight short, the unit of account being the Special Drawing Right (Protocol, Art. 2, [UNTS vol. 1208, No. 19487](https://treaties.un.org/doc/Publication/UNTS/Volume%201208/volume-1208-I-19487-English.pdf)) [independent]; which countries are party was not checked. Whether a claim lies in a given case is a legal question for the claims handler and counsel.

The steps across the parties:

```viz
{"kind": "swimlanes", "lanes": [{"id": "shipper", "label": "Shipper and its transport system", "tone": 3}, {"id": "carrier", "label": "Carrier", "tone": 4}, {"id": "consignee", "label": "Consignee", "tone": 2}], "steps": [{"id": "plan", "lane": "shipper", "col": 0, "label": "1 Plan", "note": "consolidate"}, {"id": "rate", "lane": "shipper", "col": 1, "label": "2 Rate", "note": "routing guide"}, {"id": "tender", "lane": "shipper", "col": 2, "label": "3 Tender", "note": "X12 204"}, {"id": "accept", "lane": "carrier", "col": 3, "label": "4 Accept or refuse", "note": "X12 990"}, {"id": "dock", "lane": "shipper", "col": 4, "label": "5 Book a dock"}, {"id": "pickup", "lane": "carrier", "col": 5, "label": "6 Pick up", "note": "CMR note or BOL"}, {"id": "track", "lane": "carrier", "col": 6, "label": "7 Track", "note": "status events"}, {"id": "deliver", "lane": "consignee", "col": 7, "label": "8 Deliver", "note": "proof of delivery"}, {"id": "invoice", "lane": "carrier", "col": 8, "label": "9 Invoice", "note": "freight bill"}, {"id": "claim", "lane": "consignee", "col": 8, "label": "12 Claim", "note": "loss or damage"}, {"id": "check", "lane": "shipper", "col": 9, "label": "10 Check", "note": "expected vs actual"}, {"id": "pay", "lane": "shipper", "col": 10, "label": "11 Pay"}], "links": [{"from": "plan", "to": "rate"}, {"from": "rate", "to": "tender"}, {"from": "tender", "to": "accept", "label": "offer"}, {"from": "accept", "to": "dock"}, {"from": "dock", "to": "pickup"}, {"from": "pickup", "to": "track"}, {"from": "track", "to": "deliver"}, {"from": "deliver", "to": "invoice"}, {"from": "deliver", "to": "claim", "label": "if short"}, {"from": "invoice", "to": "check"}, {"from": "check", "to": "pay"}], "caption": "The twelve steps of a bought road shipment in section 6 of this unit, by the party that acts. Step names are this course's; the notes come from the sources cited in sections 3, 6 and 7: Acocella, Caplice and Sheffi (2020) for the routing guide, X12's 990 page, the CMR Convention (1956 text), 49 U.S.C. 14706, 49 CFR Part 377 (2009 edition) and Gartner's TMS market definition (Peer Insights, April 2026)."}
```

## 7. The documents that travel with it, by region

| Document | Where it belongs | What it is | Source |
|---|---|---|---|
| CMR consignment note | International road carriage where taking-over and delivery are in two countries, at least one a contracting country (Art. 1(1)); contracting countries are listed by the UN Treaty Collection and were not checked here | Confirms the contract of carriage; its absence or loss does not affect the contract's validity (Art. 4); three originals signed by sender and carrier: the sender keeps one, one goes with the goods, the carrier keeps one (Art. 5(1)); lists sender, carrier, consignee, places and dates, description, packages, gross weight, charges and customs instructions (Art. 6(1)); prima facie evidence of the contract and of the carrier's receipt (Art. 9(1)) | CMR [independent] |
| Electronic consignment note (e-CMR) | Contracting parties to an additional protocol to the CMR | A UN Secretariat note of 13 December 2007 circulates the text of an additional protocol concerning the electronic consignment note ([UN Digital Library, ECE/TRANS/2008/14](https://digitallibrary.un.org/record/619052)); which countries are party was not checked | UN record [practice] |
| Electronic freight transport information (eFTI) | European Union | Member State authorities must accept freight information shared electronically by operators through certified eFTI platforms; road, rail, inland waterway and air; applies in full from 9 July 2027 ([European Commission, "The eFTI Regulation"](https://transport.ec.europa.eu/transport-themes/logistics-and-multimodal-transport/efti-regulation_en)) | Commission page [practice] (flag F18) |
| Bill of lading | United States (domestic motor carriage) | A carrier must issue a receipt or bill of lading for property it receives (49 U.S.C. §14706(a)(1)); SCE1 gives the federal procurement definition (FAR 47.001) | US Code [independent] |
| Freight bill | United States | The carrier's bill for charges, presented within 7 days, with due date and late-payment terms (49 CFR §377.205, 2009 edition) | CFR [independent] |
| Load tender and response (X12 204, 990) | Published by X12; regional use not sourced | The tender and the carrier's answer as EDI messages | X12 [independent] |
| Status report (IFTSTA) | UN/EDIFACT (UN/CEFACT D.01A documentation); GS1's EANCOM subset, directory D.01B; regional use not sourced | Transport status or a change in it, between agreed parties | GS1; UN/CEFACT TRADE/CEFACT/2001/33 [independent] |
| Air waybill | International carriage by air under the Montreal Convention (1999) | Delivered for the carriage of cargo, or replaced by another record of the carriage, with a cargo receipt to the consignor on request (Art. 4); three original parts, for the carrier, the consignee and the consignor (Art. 7(1)); cargo liability limited in the 1999 text to 17 Special Drawing Rights per kilogram unless value is declared (Art. 22(3)); under the five-yearly review of Art. 24, ICAO gives the revised cargo limit as 26 SDR from 28 December 2024 ([ICAO, 2024 revised limits](https://www.icao.int/sites/default/files/secretariat/legal/LEB%20Treaty%20Collection%20Documents/2024_Revised_Limits_of_Liability_Under_the_Montreal_Convention_of_1999_en.pdf)) [independent]; complaints for damage within 14 days of receipt, for delay within 21 days (Art. 31(2)) ([OJ L 194, 18.7.2001](https://eur-lex.europa.eu/eli/convention/2001/539/oj/eng)) | Convention [independent], as published in 2001; ICAO's 2024 revised limits [independent] |
| Ocean bill of lading | International sea carriage | No source opened | none |
| National road consignment notes inside one European country | National law | No source opened | none |

Which document a given shipment needs is a legal question: put it to the operation's transport or customs team, or to the national body that administers the convention or regulation.

## 8. Own fleets and delivery routes: a different problem

A shipper with its own vehicles does not tender, accept or pay a carrier's freight bill. Its problem is to decide, each day, which vehicle visits which customers in which order. Operations research calls this the **vehicle routing problem** (VRP), introduced fifty years before Laporte's 2009 review by Dantzig and Ramser as "The Truck Dispatching Problem", whose study has produced exact algorithms and heuristics ([Laporte, 2009, abstract](https://doi.org/10.1287/trsc.1090.0301)) [practice].

Ostrel Foods (fictional) shows the difference. It runs 40 vehicles to about 600 delivery points a day on fixed routes adjusted daily, with a routing tool for the fleet and paper delivery notes on some routes; Sofia, the transport planner, builds the next day's routes, and Nuno, the dispatcher, handles the day's calls from drivers and customers; drivers return with refused goods (case register). Set against section 6, as this unit's reading:

| Bought freight (section 6) | Own fleet (Ostrel) |
|---|---|
| Tender, accept or refuse, carrier's rate | No tender; the cost is the fleet's own (vehicles, drivers, fuel) |
| One shipment, one origin, one destination | One route, dozens of stops, an order of visits |
| The carrier's invoice is checked against the rate | No freight bill; the delivery note and the refused goods come back with the driver |
| Claim against the carrier | Refusals and shortages are the shipper's own problem at the door |
| Planner chooses a carrier | Planner (Sofia) builds routes; dispatcher (Nuno) changes them during the day |

Halvern Transport's (fictional) Fleet Routing module sits here, outside the tender steps (case register; this unit's placement).

## 9. The yard and the dock: where warehouse and transport meet

The dock is where the warehouse's last step (SCE3 §7, staging and loading) and the carrier's pickup meet, and where the warehouse's inbound appointment (SCE2 §3.2, the second step of SCE2's flow map) meets the inbound carrier. SCE1 §4 places yard management (trailers and dock doors outside the building) beside the warehouse system, as a module or a separate system.

**Waiting at the dock.** The US Federal Motor Carrier Safety Administration describes **detention** as delays in the start of loading and unloading, and reports from its 2014 study that drivers met detention at about 1 in 10 stops, averaging 1.4 hours beyond the 2-hour standard, with average dwell of 3.4 hours; medium-sized carriers met it at 19% of stops, about twice large carriers' 9% ([FMCSA, last updated 3 Oct 2025](https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations)) [practice: the agency's summary of its study; sample not stated on the page]. The page also reports figures from a 2018 Inspector General study on crashes and drivers' earnings; that study was not opened, so its figures are not repeated here.

**Why it matters to the shipper.** In the 2020 study, each extra hour drivers waited at the destination in the tight market went with lower acceptance of that shipper's loads (Acocella et al.) [independent: an association]. The dock is therefore a transport cost even when the warehouse owns it (this unit's inference).

**Who owns the dock.** The appointment can sit in the warehouse system, a yard system or the transport system; SCE2 §3.2 finds it among the basic WMS features in Bartholdi and Hackman [practice], and Halvern lists a Yard module in its warehouse line and none in its transport line (case register). Which system's appointment wins is one of SCE10's seams; SCE10 §7 places appointments at the operation's own doors in the warehouse system and requests for one at another party's dock in the transport system (course's).

## 10. How each step commonly fails

| Step | Common failure | Evidence |
|---|---|---|
| 1 Plan | Shipment built after the carrier's cut-off | SCE3 §8 (Kim's field study on cut-offs [practice]; the missed cut-off is SCE3's working description); no transport-side source |
| 2 Rate | Wrong class or missing rate | NMFTA on reclassification charges [practice] |
| 3 Tender | Short lead time | Lead time is a variable in Acocella et al.; it was not a significant predictor of tight-market acceptance [independent] |
| 4 Accept or refuse | Refusal; load moves down the guide or to spot at a premium | Acocella et al. 2020 [independent]; Scott et al. 2017, abstract [independent] |
| 5 Book a dock | Truck waits; detention | FMCSA summary of its 2014 study [practice] |
| 6 Pick up | Load not ready; missed departure | SCE3 §§7–8 [practice] |
| 7 Track | No status, so the customer is told nothing | No source opened |
| 8 Deliver | Signed without a check; reservation not made in time | CMR Art. 30 sets the time limits [independent]; no measurement found |
| 9 Invoice | Late bill, or a bill without the terms | 49 CFR §377.205 (2009) sets what is required [independent]; no measurement found |
| 10 Check | Charges the system did not expect | No independent source found |
| 11 Pay | Paid outside the agreed period | 49 CFR §377.203 (2009) [independent]; no measurement found |
| 12 Claim | Claim filed late or without proof | 49 U.S.C. §14706(e); CMR Arts. 30, 32 [independent]; no measurement found |

Of the twelve, only refusal has been measured in the research this unit opened.

## 11. The transport measures in common use, by definition

No association's definitions of transport measures could be opened (APQC's transport cost page returned an error), so most definitions below are the course's own, and the table says whose each is.

| Measure | Definition | Whose definition |
|---|---|---|
| Primary carrier acceptance ratio (PAR) | Loads the primary carrier accepts, over loads offered to it, per week | Acocella et al. 2020 [practice: the paper's definition] |
| Tender rejection rate | 1 minus PAR | Course's, from Acocella et al. |
| Backup premium | Average accepted price when the primary rejects, over the average when it accepts | Acocella et al. 2020 [practice: the paper's definition] |
| Dwell time | Hours a driver waits at origin or destination | Acocella et al. 2020 [practice: the paper's definition] |
| Detention | Delay in the start of loading or unloading; FMCSA's 2014 study reports detention as time beyond a 2-hour standard | FMCSA [practice] |
| On-time pickup | Pickups made within the agreed window, over all pickups | Course's |
| On-time delivery | Deliveries made within the promised window, over all deliveries; APQC's perfect order uses on-time delivery as one factor (SCE3 §12) | Course's |
| Vehicle fill | Load carried, by weight, volume or pallet places, over the vehicle's capacity | Course's |
| Empty running | Vehicle-kilometres run empty, over all vehicle-kilometres | Eurostat's measure (section 13) |
| Cost per mile | Average cost to operate a truck per mile: $2.336 in 2025, ATRI's industry average | ATRI, release of 15 Jul 2026 [practice: sample not stated on the release] |
| Freight cost per unit | Freight spend over units, orders or weight shipped | Course's |
| Invoice match rate | Carrier invoices matching the expected charge, over all invoices | Course's, from Gartner's settlement capability [analyst] |
| Claims ratio | Shipments with a loss or damage claim, over all shipments | Course's |
| Tonne-kilometre | Weight of goods times distance travelled, per goods operation | Eurostat metadata [independent] |

## 12. National logistics cost figures

The Council of Supply Chain Management Professionals (CSCMP), an association, publishes the annual *State of Logistics Report*, produced for it by Kearney and presented by Penske Logistics. CSCMP's page states that in the 2026 report, released on 16 June, US business logistics costs came to $2.4 trillion, 7.8% of national GDP, against $2.6 trillion and 8.7% in 2025 ([CSCMP, "State of Logistics Report"](https://cscmp.org/CSCMP/Educate/State_of_Logistics_Report.aspx)) [practice: an estimate, its method not stated on the page]. The page does not say which calendar year each figure measures, and gives no split between transport, inventory carrying and administration; the report itself is sold and was not read. [Kearney's published summary of the 2026 report](https://www.kearney.com/documents/d/asset-library-291362522/2026-state-of-logistics-key-takeaways) gives no cost figures and covers AI in logistics, which this course does not treat. No European or national figure for logistics costs was opened, so none is given.

## 13. Common claim C12: "A stated share of truck miles is driven empty"

**As it circulates.** A percentage of truck miles, or kilometres, driven with nothing on board, often given without a year, a region or a definition.

**What the evidence shows.**

- **European Union.** In 2020, about a fifth (20%) of EU road freight vehicle-kilometres were driven by empty vehicles: 24% in national transport and 13% in international; Cyprus was highest at 44%, Belgium lowest at 6%; Malta does not report, and Italy and Romania had no data on empty vehicle-kilometres (Eurostat, 10 December 2021) [independent]. The figures come from sample surveys of goods vehicles registered in each reporting country, under Regulation (EU) No 70/2012, excluding vehicles with a load capacity below 3.5 tonnes (Eurostat metadata) [independent]. No later Eurostat figure for the empty share was found (the later Eurostat news items on road freight that were opened give none), so 2020 is the latest year given here.
- **United States.** The American Transportation Research Institute (ATRI), the trucking industry's research institute, reported in July 2025 that empty miles rose to an average of 16.7%, without stating the year measured ([ATRI, 1 July 2025](https://truckingresearch.org/2025/07/new-atri-report-shows-trucking-profitability-severly-squeezed-by-high-costs-low-rates/)) [practice: the carriers surveyed are not stated on the release]. Its 2026 release says only that deadhead mileage "remained elevated" in 2025, with no share ([ATRI, 15 July 2026](https://truckingresearch.org/2026/07/new-atri-report-details-accelerating-costs-and-low-profitability-despite-cuts/)), and the excerpt of ATRI's 2026 report that this unit could read had no empty-mile figure.

```viz
{"kind": "compare", "title": "Share of EU road freight vehicle-kilometres run empty, 2020", "unit": "%", "max": 50, "rows": [{"label": "National transport", "value": 24}, {"label": "All road freight", "value": 20}, {"label": "International transport", "value": 13}], "caption": "Empty vehicle-kilometres as a share of all road freight vehicle-kilometres in the EU in 2020, by kind of transport, section 13 of this unit. Source: Eurostat, 'A fifth of road freight kilometres by empty vehicles', 10 December 2021 (Malta not reporting, Italy and Romania without data); coverage of vehicles of 3.5 t load capacity and over from Eurostat's road_go metadata (last updated 22 July 2026)."}
```

**Verdict.** A stated share can be supported, but only with its region, year, vehicle class and measure attached. The EU figure is official statistics on vehicle-kilometres of heavier goods vehicles; the US figure is an industry institute's survey average with its sample not stated on the page read. The two are not comparable, and neither says how much empty running could be avoided: Sheffi's account of repositioning (section 3) shows why some is built into one-directional flows [practice]. Eurostat notes that empty journeys are more common in domestic transport, where distances are typically shorter, and links Cyprus's share to port and construction traffic that mostly moves one way (Eurostat, 2021) [practice: the office's comment, not a measurement].

## On a site visit

At the transport office and the dock, look for, and ask:

- **Who plans the day's shipments, and when?** How long between the warehouse's release and the carrier's pickup (section 6, step 1; SCE3 §8)?
- **Where does the routing guide live, and when was it last bid?** Contract length, lanes, how many backups per lane (section 3).
- **How are loads tendered: EDI, a portal, e-mail or the phone?** What happens to a refusal, and who sees it first (section 6, steps 3 and 4)?
- **What was last month's primary acceptance, and what did refused loads cost against contract?** (Sections 4 and 11.)
- **Watch the dock for an hour.** How long do trucks wait, who records it, and who pays detention (section 9)?
- **Which document leaves with each load, paper or electronic, and who keeps the signed copy?** (Section 7.)
- **Who checks carrier invoices, against what, and what share are disputed?** (Section 6, steps 10 and 11.)
- **For an own fleet: who builds the routes, when, with what tool, and who changes them during the day?** (Section 8.)

## Self-check

1. **What does a US broker sell, and how does US law define one?**
   The arrangement of transport by a motor carrier for compensation, by a person who is not itself a motor carrier (49 U.S.C. §13102(2); section 1).
2. **How do large shippers buy truckload capacity, according to Sheffi (2004)?**
   Through RFPs: the shipper estimates the coming year's freight, sends carriers a list of lanes, evaluates sealed single-round bids lane by lane, and signs contracts usually of one to two years (section 3).
3. **What happens when a primary carrier rejects a tender?**
   The shipper offers the load to the next backup in the routing guide, and when the guide is exhausted, to the spot market; in one large shipper's data spot averaged about 62% above contract (sections 3 and 4).
4. **What did Acocella, Caplice and Sheffi find about carriers' acceptance, and on what data?**
   On 1,933,299 US dry-van long-haul loads from 71 shippers (2015 to 2019), weekly primary acceptance averaged 81.9% in the soft market and 68.5% in the tight one; tight-market acceptance was associated with current price against market, volume steadiness, offer frequency and destination dwell, not with past behaviour (section 4).
5. **Which TMS capability checks a carrier's invoice, in Gartner's definition?**
   Settlement, which matches expected transportation charges against actual charges (section 5).
6. **Under the CMR, how many original consignment notes are there, and who holds each?**
   Three, signed by sender and carrier: the sender keeps the first, the second goes with the goods, the carrier keeps the third (section 7).
7. **What time limits does US law set as a minimum for claims against a motor carrier?**
   A carrier may not allow less than 9 months to file a claim or 2 years to bring a civil action (49 U.S.C. §14706(e); section 6, step 12).
8. **A colleague says a third of truck kilometres are run empty. What do the sources opened here say?**
   Eurostat put the EU share at 20% of vehicle-kilometres in 2020 (24% national, 13% international); ATRI reported in July 2025 that US empty miles averaged 16.7%, year measured and sample not stated; neither supports a third without a region, year and definition (section 13).

## Deliverable: the shipment lifecycle map

The map has six columns: **Step**, **Party**, **Document**, **System touchpoint**, **Common failure**, **Measure**. It reuses SCE2's flow-map form, with Party in place of People and Document in place of Data needed, and keeps section 6's twelve step numbers so SCE8 can place a product on them and SCE10 can join step 6 to the warehouse's last row (SCE3 deliverable C, row 8). Cells cite this unit's sections in brackets or the case register; a cell the register does not fill says so. A failure listed is one to look for; it is no claim that the operation has it, unless it says "known trouble".

### A. A Corvane store delivery (fictional)

Corvane (fictional): a fashion retailer with 60 stores in four European countries, one website and one 28,000 m² distribution centre; carriers are booked through each carrier's own portal, with no transport system; an ERP (case register). Settlement is held in the ERP, with Helene, chief financial officer, answering for the financial record (register, added by SCE1, a working placement); Tobias answers for pack and ship (register). The register does not say where the centre is; with one centre serving four countries, some store deliveries cross a border, so the CMR applies to those where the Convention's conditions are met (this unit's inference, listed in the notes). Assumed for this map, and listed in the notes: one store's replenishment goes as one shipment with a contracted road carrier, booked in that carrier's portal.

| # | Step | Party | Document | System touchpoint | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Plan and consolidate | Corvane, as shipper; the planner is not in the register | None yet | Warehouse system's shipment record (SCE3 C, row 8); no transport system (register) | Store order released too late for the carrier's pickup (6, SCE3 §8) | Vehicle fill (11) |
| 2 | Rate | Corvane and the carrier | Carrier's rate in its portal; whether rates are contracted is not in the register | Each carrier's portal (register) | Rate not visible before booking (6, reading of register) | Freight cost per unit (11) |
| 3 | Tender | Corvane books; who books is not in the register | Booking in the portal | Each carrier's portal (register); keyed by hand is this unit's reading, as SCE3 C, row 6 reads labels | Re-keying errors; booking with short notice (6) | None sourced |
| 4 | Accept or refuse | Carrier | Booking confirmation | Carrier's portal | Refusal in peak, re-booked at a higher price (4, as this unit's inference for Europe) | PAR; backup premium (11) |
| 5 | Book a dock | Tobias's outbound shift at the centre (reading of register: he supervises outbound); store not in the register | Pickup time | Warehouse system, or none (9) | Truck waits at the centre's door (9) | Dwell time (11) |
| 6 | Pick up | Carrier's driver; Tobias answers for pack and ship (register) | CMR consignment note for cross-border stores (7); national documents not sourced | Departure scan in the warehouse system (SCE3 §7) | Missed cut-off in peak (SCE3 §8) | On-time pickup (11) |
| 7 | Track | Carrier; store staff ask; not in the register | None | Each carrier's portal (register) | No status for the store (6) | None sourced |
| 8 | Deliver and prove delivery | Store staff, as consignee; not named in the register | Signed CMR copy that travelled with the goods (7) | Not in the register | Signed without a count; reservation not made within CMR limits (6, step 8) | On-time delivery (11) |
| 9 | Invoice | Carrier | Carrier's invoice | ERP (SCE1 working placement) | Charges not visible at booking (6) | None sourced |
| 10 | Check against the agreed rate | Not in the register | Invoice against the portal booking | ERP; no settlement capability (register has no transport system) | Unexpected charges paid unchecked (6, step 10) | Invoice match rate (11) |
| 11 | Pay | Helene answers for the financial record (register, SCE1 working placement) | Payment | ERP (SCE1 working placement) | Paid late or early against terms (6, step 11) | None sourced |
| 12 | Claim | Corvane, from the store's report; who files is not in the register | Reservation on the CMR note; written claim (7) | Not in the register | Reservation missing, so the claim is weak (6, step 12) | Claims ratio (11) |

Where the decision touches this map: Corvane is deciding whether to buy order and transport systems from the same vendor as its warehouse system (register). On this map a transport system would take over steps 1 to 4, 7 and 10 from the portals and the ERP; for example Halvern Transport's (fictional) Rating and Tendering, Tracking and Freight Audit modules (section 5).

### B. A load Tandric arranges for a client (fictional)

Tandric Logistics (fictional): a logistics provider running one multi-client warehouse for nine clients and a freight desk that arranges full and part loads with outside carriers for clients, with no trucks of its own; paid for freight at a margin over what the carrier is paid; a warehouse system shared by all clients, a transport system for the freight desk and a client portal; known trouble includes invoices disputed because activity was not recorded (case register). People: Priya, freight desk, tenders loads and checks carriers' invoices; Olu, client services; Anke, site manager; Karin, commercial director (register). The register does not give Tandric's region, so the document column gives both. Assumed for this map, and listed in the notes: a full load for one of the seven pallet-storing clients, from Tandric's warehouse to that client's customer.

| # | Step | Party | Document | System touchpoint | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Plan and consolidate | Client orders; Priya plans the load (register: freight desk) | Client's order, through the client portal (reading of register) | Transport system for the freight desk; warehouse system for the pick (register) | Client order arrives after the desk has booked the day's trucks (6, step 1) | Vehicle fill (11) |
| 2 | Rate | Priya; Karin signs client contracts (register) | Two rates: the price to the client and the carrier's rate; Tandric's margin is the difference (register) | Transport system (5) | Client price set without the carrier rate known (reading of register) | Freight cost per unit; margin per load, no public figure (11) |
| 3 | Tender | Priya (register) | Tender; in X12 EDI, a 204 (6, step 3) | Transport system (register; 5) | Short lead time (6, step 3) | None sourced |
| 4 | Accept or refuse | Carrier | Acceptance or refusal; in X12, a 990 (6, step 3) | Transport system | Refusal, load moves to a backup or spot, and the margin shrinks (4; reading of register) | PAR; backup premium (11) |
| 5 | Book a dock | Anke's site (register) | Pickup appointment | Warehouse system shared by all clients, or the transport system (9) | Truck waits at Tandric's door; detention charged (9) | Dwell time (11) |
| 6 | Pick up | Carrier's driver; Tandric's warehouse staff | CMR consignment note if international in Europe; bill of lading in the US (7) | Warehouse system records departure (SCE3 §7) | Load not ready at pickup (6, step 6) | On-time pickup (11) |
| 7 | Track | Carrier reports; Olu answers the client (register) | Status messages, IFTSTA or other (6, step 7) | Transport system; client portal (register) | Client asks before Tandric knows (6, step 7) | None sourced |
| 8 | Deliver and prove delivery | Client's customer, as consignee | Signed copy of the note or bill of lading (7) | Transport system, from the carrier | Proof of delivery not returned, so the client cannot be billed (reading of register) | On-time delivery (11) |
| 9 | Invoice | Carrier bills Tandric; Tandric bills the client (register: paid at a margin) | Carrier's invoice; Tandric's invoice to the client | Transport system; how the client is billed is not in the register | Client invoice disputed because activity was not recorded (register: known trouble, stated for invoices generally; its reach to freight is this unit's reading) | Invoice match rate (11) |
| 10 | Check against the agreed rate | Priya (register) | Carrier invoice against the tender and rate | Transport system's settlement (5) | Detention or extra charges not passed on to the client (reading of register) | Invoice match rate (11) |
| 11 | Pay | Tandric pays the carrier; the client pays Tandric | Payment | Not in the register | Carrier paid before the client pays Tandric (reading of register) | None sourced |
| 12 | Claim | Client claims against Tandric; Tandric against the carrier (reading) | Reservation and written claim (7) | Not in the register | Time limit missed between the two claims (6, step 12) | Claims ratio (11) |

Where Tandric's role differs: Tandric sits between client and carrier on every money step (2, 9, 10, 11, 12), so each failure there is also a dispute with the client. Whether Tandric's freight desk is a broker or a forwarder in law, and what it owes the client on a claim, is a question for Tandric's legal advisers and the national regulator (section 1).

### C. Template: the shipment lifecycle map

Fill one row per step for a real operation, or for a product by naming the screen or module at each step. Keep the step numbers; add a row where the operation has a step the map lacks, and say why. Mark each cell's grade (independent, analyst, vendor-reported, practice) or "observed" for what you saw yourself.

Operation or product: ______ (name; kind of company: shipper, carrier, broker, forwarder, logistics provider) · Region: ______ (North America, Europe or other; national or international carriage) · Mode: ______ (parcel, LTL or groupage, full truckload, intermodal, ocean, air; own fleet) · Date filled: ______ · Sources used: ______ (each with its grade)

| # | Step | Party | Document | System touchpoint | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Plan and consolidate | ______ (who plans, when) | ______ (the order or shipment record) | ______ (which system consolidates and picks the mode) | ______ (what arrives too late to plan) | ______ (vehicle fill, or the site's own) |
| 2 | Rate | ______ (who sets and who sees the rate) | ______ (contract, tariff, freight class, spot quote) | ______ (where rates are held) | ______ (missing or wrong rate) | ______ (freight cost per unit) |
| 3 | Tender | ______ (who tenders) | ______ (EDI message, portal booking, e-mail) | ______ (the system that sends it) | ______ (lead time, re-keying) | ______ (the site's own, or none found) |
| 4 | Accept or refuse | ______ (which carriers, in what order) | ______ (acceptance or refusal message) | ______ (where the routing guide lives) | ______ (refusal and what it costs) | ______ (PAR; backup premium) |
| 5 | Book a dock | ______ (who books, at both ends) | ______ (appointment) | ______ (warehouse, yard or transport system) | ______ (waiting, detention) | ______ (dwell time) |
| 6 | Pick up | ______ (driver; loader) | ______ (CMR note, bill of lading, other, by region) | ______ (departure record; which system) | ______ (load not ready, missed departure) | ______ (on-time pickup) |
| 7 | Track | ______ (who reports, who asks) | ______ (status message or portal) | ______ (where events land) | ______ (no status) | ______ (the site's own, or none found) |
| 8 | Deliver and prove delivery | ______ (consignee) | ______ (signed copy; electronic proof) | ______ (where proof is stored) | ______ (signed without a check; reservation missed) | ______ (on-time delivery) |
| 9 | Invoice | ______ (who bills whom) | ______ (freight bill; invoice to a client) | ______ (where invoices arrive) | ______ (late or incomplete bill) | ______ (the site's own) |
| 10 | Check against the agreed rate | ______ (who checks) | ______ (invoice against what record) | ______ (settlement in the transport system, the ERP, or by hand) | ______ (unexpected charges) | ______ (invoice match rate) |
| 11 | Pay | ______ (who pays, on what terms) | ______ (payment) | ______ (the system that pays) | ______ (paid outside terms) | ______ (the site's own) |
| 12 | Claim | ______ (who claims against whom) | ______ (reservation, written claim) | ______ (where claims are held) | ______ (time limit missed, proof missing) | ______ (claims ratio) |

Below the table: the legal questions about documents, liability, claim limits and payment terms, and the body they were put to (______); which steps the operation runs with its own fleet instead (______, see section 8); and the step where the operation's known trouble starts (______).

### D. Glossary lines

Added to the working glossary of SCE1 to SCE3; each term as this unit uses it, with where it belongs.

| Term | Working definition | Region | Source |
|---|---|---|---|
| Consignee | The party goods are delivered to | Both; named on the CMR note | CMR Art. 6 [independent] |
| Motor carrier | A person providing motor vehicle transportation for compensation | US legal term | 49 U.S.C. §13102(14) [independent] |
| Haulier; hire or reward transport | A commercial road freight carrier; its transport | Europe (statistics) | Eurostat [independent] |
| Own account transport; motor private carrier | A company carrying its own goods in its own vehicles | Europe; US | Eurostat; §13102(15) [independent] |
| Broker | One who arranges motor carrier transport for compensation, not being a motor carrier | US legal term | §13102(2) [independent] |
| Freight forwarder | US: a consolidator taking responsibility for the move and using a carrier; internationally: the party that ensures traded goods move origin to destination | US legal term; international usage | §13102(8) [independent]; FIATA [practice] |
| Mode | The kind of carriage: parcel, LTL or groupage, full truckload, intermodal, ocean, air | Both | Course term |
| Full truckload (FTL; TL) | A vehicle dedicated to one shipper's shipment, origin to destination | FTL Europe (working term), TL US | Sheffi 2004 [practice]; as in SCE1's glossary |
| Less-than-truckload (LTL); groupage | Smaller shipments of several shippers consolidated on one vehicle | LTL US; groupage Europe (working term) | Sheffi 2004 [practice] |
| Freight class; NMFC | The class (50 to 500) that sets an LTL shipment's price, from density, handling, stowability, liability | US | NMFTA [practice] |
| Intermodal | A container or trailer moved by two or more modes without handling the goods | Both | Working definition |
| Lane | A one-way movement from an origin to a destination, with its shipments, that a shipper buys carriage for | Both | Sheffi 2004 [practice]; as in SCE1's glossary |
| Request for proposals (RFP); bid | The shipper's periodic invitation to carriers to price its lanes | US research | Sheffi 2004 [practice] |
| Combinatorial auction; package bid | A bid on a group of lanes priced together | US research | Sheffi 2004 [practice] |
| Backhaul | A load in the opposite direction that saves an empty return | Both | Course term; the idea from Sheffi 2004 [practice] |
| Routing guide | Per lane, the primary carrier and backups in order, with their prices | US research | Acocella et al. 2020 [practice]; as in SCE1's glossary |
| Primary carrier; backup carrier | The lane's first-choice carrier; the next ones in the guide | US research | Acocella et al. 2020 [practice] |
| Tender | The offer of one load to one carrier, which accepts or rejects it | Both | Acocella et al. 2020 [practice]; as in SCE1's glossary |
| Primary carrier acceptance ratio (PAR) | Loads the primary accepts over loads offered, weekly | US research | Acocella et al. 2020 [practice] |
| Spot market | Carriage priced load by load, outside the contract | Both | Acocella et al. 2020 [practice] |
| Backup premium | Price paid after a rejection over the price on acceptance | US research | Acocella et al. 2020 [practice] |
| Load tender (204); response (990) | X12 EDI transaction sets for offering a load and answering | Published by X12; regional use not sourced | X12 [independent] |
| IFTSTA | International multimodal status report message for transport events | UN/EDIFACT, in GS1's EANCOM subset; regional use not sourced | GS1 EANCOM [independent]; UN/CEFACT TRADE/CEFACT/2001/33 [independent] |
| Proof of delivery (POD) | The signed record of the hand-over | Both | Course term |
| Reservation (CMR) | The consignee's notice of loss or damage, at delivery or within seven days if not apparent | International road, CMR | CMR Art. 30 [independent] |
| Freight bill | A motor carrier's bill for its charges | US | 49 CFR §377.205 (2009) [independent] |
| Settlement | Matching expected transport charges against actual ones | Both | Gartner TMS definition [analyst] |
| Claim (loss or damage) | A demand on the carrier for goods lost, damaged or delayed | Both; rules by region | 49 U.S.C. §14706; CMR Arts. 17, 32 [independent] |
| Air waybill | The cargo document of international air carriage, in three original parts | International, Montreal Convention | Montreal Convention Arts. 4, 7 [independent] |
| eFTI | EU rules requiring authorities to accept electronic freight information from certified platforms, in full from 9 July 2027 | EU | European Commission page [practice] |
| Detention | Delay in the start of loading or unloading | US usage | FMCSA [practice] |
| Dwell time | Hours a driver waits at origin or destination | US research | Acocella et al. 2020 [practice] |
| Empty running; empty miles; deadhead | Distance a goods vehicle runs with no load | "Empty running" Europe; "empty miles", "deadhead" US | Eurostat [independent]; ATRI [practice] |
| Vehicle-kilometre; tonne-kilometre | Distance run by a vehicle; weight times distance per goods operation | Europe (statistics) | Eurostat [independent] |
| Vehicle routing problem (VRP) | Choosing which vehicle visits which stops in which order | Both | Laporte 2009, abstract [practice] |
| Transportation management system (TMS) | Software for multimodal sourcing, planning and execution of transport, with visibility, settlement and analytics | Both | Gartner TMS definition [analyst]; as in SCE1's glossary |

## Sources

All addresses opened on 24 November 2026, except ICAO's 2024 revised limits and the UN Treaty Collection's status page for the 1978 CMR Protocol, opened on 25 November 2026, and UN/CEFACT TRADE/CEFACT/2001/33, the 1978 CMR Protocol's UN Treaty Series text and Directive 2011/7/EU Article 3, opened on 28 November 2026 by correction; the source log (sources.md) gives what was read at each.

- Acocella, A., Caplice, C. & Sheffi, Y. (2020). Elephants or goldfish?: An empirical analysis of carrier reciprocity in dynamic freight markets. *Transportation Research Part E: Logistics and Transportation Review* 142, 102073. https://doi.org/10.1016/j.tre.2020.102073 (read in full in the author's copy at https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2021-01/Acocella_Sheffi_Publication%202020.pdf)
- American Transportation Research Institute. "New ATRI Report Shows Trucking Profitability Severely Squeezed by High Costs, Low Rates". 1 July 2025. https://truckingresearch.org/2025/07/new-atri-report-shows-trucking-profitability-severly-squeezed-by-high-costs-low-rates/
- American Transportation Research Institute. "New ATRI Report Details Accelerating Costs and Low Profitability Despite Cuts". 15 July 2026. https://truckingresearch.org/2026/07/new-atri-report-details-accelerating-costs-and-low-profitability-despite-cuts/
- Council of Supply Chain Management Professionals. "State of Logistics Report". Undated page. https://cscmp.org/CSCMP/Educate/State_of_Logistics_Report.aspx
- European Commission, Mobility and Transport. "The eFTI Regulation". Undated. https://transport.ec.europa.eu/transport-themes/logistics-and-multimodal-transport/efti-regulation_en
- European Parliament and Council. Directive 2011/7/EU of 16 February 2011 on combating late payment in commercial transactions (recast), Article 3, as adopted (legislation.gov.uk copy). https://www.legislation.gov.uk/eudr/2011/7/article/3/adopted
- European Union. Convention for the Unification of Certain Rules for International Carriage by Air (Montreal, 28 May 1999). OJ L 194, 18.7.2001, pp. 39–49. https://eur-lex.europa.eu/eli/convention/2001/539/oj/eng
- Eurostat. "A fifth of road freight kilometres by empty vehicles". Eurostat News, 10 December 2021. https://ec.europa.eu/eurostat/web/products-eurostat-news/-/ddn-20211210-1
- Eurostat. "Road freight statistics (road_go)", reference metadata, last updated 22 July 2026. https://ec.europa.eu/eurostat/cache/metadata/en/road_go_esms.htm
- Eurostat. "Glossary for transport statistics, 5th edition, 2019" (the page's headline, its dashes written here as commas). Product page, 25 July 2019. https://ec.europa.eu/eurostat/web/products-manuals-and-guidelines/-/ks-gq-19-004
- FIATA. "About Freight Forwarding". Undated. https://fiata.org/about-freight-forwarding/
- Flodén, J., Bärthel, F. & Sorkina, E. (2010). Factors influencing transport buyer's choice of transport service – A European literature review. *12th WCTR Proceedings* (abstract). https://research.chalmers.se/en/publication/122890
- Gartner Peer Insights. "Transportation Management Systems Reviews and Ratings", market definition, features updated April 2026. https://www.gartner.com/reviews/market/transportation-management-systems
- GS1. EANCOM 2002 S3, Part II, "IFTSTA: International multimodal status report message". https://www.gs1.org/sites/gs1/files/docs/eancom/ean02s3/part2/iftsta/intro.htm
- International Civil Aviation Organization. "2024 Revised Limits of Liability Under the Montreal Convention of 1999". https://www.icao.int/sites/default/files/secretariat/legal/LEB%20Treaty%20Collection%20Documents/2024_Revised_Limits_of_Liability_Under_the_Montreal_Convention_of_1999_en.pdf
- Kearney. 2026 State of Logistics key takeaways. 2026. https://www.kearney.com/documents/d/asset-library-291362522/2026-state-of-logistics-key-takeaways
- Laporte, G. (2009). Fifty Years of Vehicle Routing. *Transportation Science* 43(4), 408–416. https://doi.org/10.1287/trsc.1090.0301 (abstract, read at https://www.gerad.ca/en/papers/G-2009-43)
- NMFTA. "Classification - NMFTA". Undated. https://nmfta.org/standards/classification/
- Scott, A., Parker, C. & Craighead, C. W. (2017). Service Refusals in Supply Chains: Drivers and Deterrents of Freight Rejection. *Transportation Science* 51(4), 1086–1101. https://doi.org/10.1287/trsc.2016.0677 (abstract)
- Sheffi, Y. (2004). Combinatorial Auctions in the Procurement of Transportation Services. *Interfaces* 34(4), 245–252. https://doi.org/10.1287/inte.1040.0075 (read in full in the author's copy at https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2018-07/10_CombinatorialAuctionsInTheProcurementOfTransportationServices.pdf)
- United Nations. Convention on the Contract for the International Carriage of Goods by Road (CMR), Geneva, 19 May 1956. Arts. 1, 4, 5, 6, 9, 17, 23, 30, 32. https://treaties.un.org/doc/Treaties/1961/07/19610702%2001-56%20AM/Ch_XI_B_11.pdf
- United Nations. Protocol to the Convention on the Contract for the International Carriage of Goods by Road (CMR), Geneva, 5 July 1978. *United Nations Treaty Series* vol. 1208, No. 19487. Art. 2. https://treaties.un.org/doc/Publication/UNTS/Volume%201208/volume-1208-I-19487-English.pdf
- United Nations Economic Commission for Europe. Additional Protocol to the CMR: note by the Secretariat. ECE/TRANS/2008/14, 13 December 2007. UN Digital Library record. https://digitallibrary.un.org/record/619052
- United Nations Treaty Collection. Status of the Protocol to the Convention on the Contract for the International Carriage of Goods by Road (CMR), Geneva, 5 July 1978, chapter XI.B-11(a). https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-11-a.en.pdf
- UN/CEFACT. UN/EDIFACT Standard Directory D.01A and related documentation, TRADE/CEFACT/2001/33, 14 February 2001. https://digitallibrary.un.org/record/433163/files/%5EE_ECE_%5ETRADE_CEFACT_2001_33-EN.pdf
- United States. Code of Federal Regulations, Title 49, Part 377, "Payment of transportation charges", revised as of 1 October 2009. https://www.govinfo.gov/content/pkg/CFR-2009-title49-vol5/pdf/CFR-2009-title49-vol5-part377.pdf
- United States. United States Code, 2019 edition, Title 49, §13102 "Definitions". https://www.govinfo.gov/content/pkg/USCODE-2019-title49/html/USCODE-2019-title49-subtitleIV-partB-chap131-sec13102.htm
- United States. United States Code, Title 49, §14706 "Liability of carriers under receipts and bills of lading", current through Public Law 119-136. https://uscode.house.gov/us/usc/119-136/t49/s14706/
- US Federal Motor Carrier Safety Administration. "Impact of Driver Detention Time on Safety and Operations". Last updated 3 October 2025. https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations
- X12. "990 Response to a Load Tender". Undated. https://x12.org/node/4450

## Unsure list

claude-opus-5-5

# Unsure: SCE7

1. All quotations ("arranging for, transportation by motor carrier for compensation"; "consolidate many smaller shipments on a single truck"; "a one-way movement from an origin to a destination"; "three to 15 percent of transportation costs while maintaining or increasing their service levels"; "there is typically no legally binding obligation or penalty for either party to offer or accept a load"; "multimodal sourcing, planning and execution of the physical transport of goods"; "Settlement capabilities to match expected transportation charges against actual charges"; "remained elevated") were taken from a fetch tool's extraction and not re-read against a second copy.
2. Acocella, Caplice and Sheffi (2020): the figures (1,933,299 loads, 71 shippers, 1,640 primary carriers, PAR 81.9% and 68.5%, $1,155.9 and $1,420.7, backup premium 1.009 and 1.182) and the period dates come from the extraction of the author's copy; that the data came from a managed services provider rather than a broker was read in that extraction only.
3. CSCMP's page: which calendar year the 2026 report's $2.4 trillion and 7.8% measure, and whether "In 2025" refers to the 2025 report or to the year 2025, was not stated; the unit reports them as the 2026 and 2025 reports' figures.
4. 49 CFR Part 377: only the 2009 edition was read; the 7-day presentation and 15-day and 30-day credit periods may have changed since.
5. 49 U.S.C. §13102: the 2019 edition was read; later amendments to the definitions of broker and freight forwarder were not checked.
6. CMR Art. 23(3): the 1956 text gives 25 gold francs per kilogram; the 1978 Protocol's Art. 2 (8.33 units of account, the Special Drawing Right) was read in the UN Treaty Series copy on 28 November 2026 (correction from SCE10); which countries are party to it was not checked (flag F66).
7. Flodén, Bärthel and Sorkina (2010): graded practice because the peer-review status of the WCTR proceedings was not confirmed; the abstract was read at Chalmers' research portal, not at a publisher.
8. Sheffi (2004): the "three to 15 percent" savings range is graded practice because the extraction showed no measurement design behind it; whether the author had a commercial interest in auction software was not checked.
9. ATRI's 16.7% empty miles: the release does not state the year measured, the sample or how empty miles are defined, and the 2026 report's empty-mile figure for 2025 was not in the part of the report returned.
10. The Eurostat glossary's product-page headline contains dashes that the unit writes as commas, under the course's no-em-dash rule; the title is otherwise the page's own.

Object: the CMR consignment note (section 7, with section 6 steps 6, 8 and 12)

Fresh check 2026-11-25 (claude-opus-5-5): keep · 0 errors, 4 should-fix, 14 minor; report `audits/supply-chain-execution/fresh-check-SCE7.md`

Correction 27 Nov 2026, found by the corrections check of SCE8's contradictions (checked by a fresh Opus 5.5 agent, report audits/supply-chain-execution/corrections-2026-11-27-C-SCE8-SCE7.md)
