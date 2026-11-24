---
code: SCE6
title: The warehouse system as a product
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-24
search: on
intro: SCE6 treats the warehouse system as a product. It sets the textbook's definition of a warehouse management system against the analyst's, with core and extended capabilities; describes how the one analyst report read divides the market (by kind of vendor and by warehouse complexity, not by tiers); compares deployment models (multi-tenant SaaS, single-tenant and hosted, on the customer's own servers) and who upgrades under each; draws the line between configuration and customisation and why it matters years later; names the integrations every site needs (ERP, carriers, automation, labels and printing); sets out the capability list W1 to W29; works Halvern Warehouse (fictional) through it; gives the real market as one dated analyst list; shows how to place a real product line on the map yourself; and sets common claim C8 ("cloud software means no more upgrades") against the evidence. Its deliverable is the capability map form, Halvern's warehouse line mapped (29 rows: 6 module, 8 core assumed, 15 open), and the template. Written 24 Nov 2026 by Opus 5.5 with search on (all references read on 24 Nov 2026), then given a fresh check by a separate Opus 5.5 agent (fix: 0 errors, 7 should-fix, 7 minor), all 14 findings applied. Held: none. Known gaps: Gartner's current WMS Magic Quadrant (29 April 2026) could not be opened, so the vendor list is the 1 June 2022 edition's, read in a reprint through a fetch tool and not every part of it; it is four years old. No analyst report opened sorts the market into tiers, and Gartner's "Midmarket Context" piece was not opened. The one textbook opened is Bartholdi and Hackman (release 0.98, 2017), so much of the definition and the capability list is graded practice; Richards' Warehouse Management was not opened. Light (2001) was read in abstract only. No independent source was found that measures upgrade effort or cost in the cloud against on-premises, so C8 ends "no independent source found". No source was opened on label printer formats or printing integration. Halvern's core capabilities are this unit's assumption, not register facts. The placement of the fictional vendors on Gartner's vendor types, and the "case" value in the capability map form, wait on the owner (F53, F54).
---

# SCE6 · The warehouse system as a product

SCE2 to SCE5 followed goods, records and people through the building. This unit turns to the software as something sold: how it is defined, how its market is divided, how it is delivered and changed, what it must connect to, and how to place any vendor's product line on the operation. Grades follow SCE1's key (section 10 there): every claim that carries a number, a mechanism or a recommendation ends with [independent], [analyst], [vendor-reported] or [practice]. Lines marked as this unit's inference, or as working descriptions, carry no grade; they rest on the graded sources they name. Every current fact (an analyst's date, a list, a count) carries the date it was read: all were read on 24 November 2026.

Two limits hold through the unit. The current analyst evaluation of this market, Gartner's *Magic Quadrant for Warehouse Management Systems* of 29 April 2026, could not be opened (section 8), so the analyst material read is the edition of 1 June 2022, in a reprint (read through a fetch tool, not every part of it). And the one textbook opened on warehouse software as a product is Bartholdi and Hackman's *Warehouse & Distribution Science* (release 0.98, 2017), chapter 4, so much of sections 1, 4 and 6 is graded practice.

## 1. What a warehouse management system is, and how the definitions differ

**The textbook's definition.** Bartholdi and Hackman define a warehouse management system (WMS) by what it knows and records. It "knows about every item in the warehouse", receives customer orders and transforms them into pick lists, and tracks the assembly of each order (ch. 4 introduction) ([Bartholdi & Hackman, *Warehouse & Distribution Science*, release 0.98, 2017](https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf)) [practice]. Its most fundamental job is to record receipt of inventory into the warehouse and register its shipment out (§4.1) [practice]; to that it adds a **stock locator system**, which manages an inventory of storage locations as well as of product, "down to and including the forks of individual forklift trucks" (§4.2) [practice]. Their summary is one sentence: the core of a WMS "is a database of skus and a stock locator system" (§4.6) [practice]. In the same chapter they say that most systems manage transactions and do not optimise decisions; the user, or a consultant, chooses rules from the modules supplied, or the software is customised (§4.6.1, read through a summary of the passage) [practice].

**The analyst's definition.** Gartner's glossary defines a WMS as "a software application that helps manage and intelligently execute the operations of a warehouse, distribution or fulfillment center", and lists fifteen capabilities: receiving, put-away, stock locating, inventory management, cycle counting, task interleaving, wave planning, order allocation, order picking, replenishment, packing, shipping, labor management, yard management and automated materials handling equipment interfaces ([Gartner glossary, "Warehouse Management System (WMS)", undated, read 24 Nov 2026](https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/warehouse-management-system-wms)) [analyst]. Gartner's review market page adds two things. "WMS operations natively exploit mobile devices along with bar codes" and potentially RFID (radio-frequency identification: tags read by radio) "to form the transactional foundation of warehouse management", which enables directed work; and Gartner splits **core** capabilities (to receive, put away, store, count, pick, pack and ship) from **extended** ones, "additional integrated functionality offered by WMS providers beyond core WMS", such as managing labour or optimising where inventory is located ([Gartner Peer Insights, "Warehouse Management Systems Reviews and Ratings", features updated May 2026, read 24 Nov 2026](https://www.gartner.com/reviews/market/warehouse-management-systems?months=12)) [analyst].

**How they differ**, as this unit's reading of the three:

- **Record or execution.** The textbook puts the record at the centre (a database and a locator) and says most systems do not optimise. Gartner's definitions put execution at the centre ("intelligently execute", "directed work activity") and fold optimisation into the category.
- **A fixed core or a moving boundary.** The textbook gives one core. Gartner's extended capabilities are defined by what "WMS providers" offer, so the category grows when vendors add modules. Labour, yard and equipment interfaces sit inside Gartner's glossary list; in the textbook labour and yard management are high-end features, and equipment interfaces are not on its menu (section 6).
- **The device.** Only Gartner's review page writes the mobile device and the bar code into the definition. SCE5 §3 treats the device as a working condition.

For a product team the practical consequence, as this unit's inference: when a buyer, a seller and an analyst say "WMS" they may mean three different scopes. Ask which definition a requirements list, a contract or an evaluation uses before comparing two products on it.

## 2. The tiers of the market, as the analysts describe them

**What the analyst material opened uses instead of tiers.** You will hear products sorted into tiers (entry, mid-market, enterprise). The one analyst evaluation read here does not use that word. Gartner's *Magic Quadrant for Warehouse Management Systems* of 1 June 2022 (read in a reprint; vendors license Gartner's reprints, the course's working assumption from SCE1 §8) divides the market two ways ([Gartner, Magic Quadrant for WMS, 1 June 2022, ID G00755323, reprint](https://dam.infor.com/api/public/content/d8957bc1ac164bf1843965deeaa7e26a?v=d2e94df6)) [analyst]:

- **By kind of vendor.** It says the market "breaks down into five types of vendors": "Application mega vendors", "SCM suite vendors" (SCM: supply chain management), "Specialist WMS suite vendors", "Material handling equipment/automation vendors" and "Independent WMS component vendors"; the first four are covered by the Magic Quadrant and the fifth is not (Market Description) [analyst].
- **By the warehouse.** It grades warehouse operations on a complexity model of five levels, "with Level 1 being the most basic and Levels 4 and 5 being the most complex and automated"; it says "the preponderance of warehouse operations are Level 3 or below", and that warehouses at Level 3 and below "do not require, nor would they normally use, the most advanced functionality" (Market Considerations) [analyst]. The part of the report read does not define Levels 2, 3 and 4 one by one.

```viz
{"kind": "tree", "title": "The vendor types in Gartner's 2022 WMS Magic Quadrant", "root": {"label": "WMS market (Gartner, 1 June 2022)", "tone": 1, "children": [{"label": "Application mega vendors", "tone": 2}, {"label": "SCM suite vendors", "tone": 3}, {"label": "Specialist WMS suite vendors", "tone": 4}, {"label": "Material handling equipment / automation vendors", "tone": 5}, {"label": "Independent WMS component vendors (not covered)", "tone": 6}]}, "caption": "Section 2 of this unit. The five types of vendor named in the Market Description of Gartner's Magic Quadrant for Warehouse Management Systems, 1 June 2022 (ID G00755323), read in a reprint on 24 November 2026; the report covers the first four. No vendor is placed in any type here."}
```

Two points follow, as this unit's inference. The analyst sorts by **who sells** and by **how complex the building is**; it does not sort products by the size of the customer, which is what "entry" and "enterprise" usually mean in a sales conversation. Customer size appears in two places: several vendor entries describe a vendor's fit for midmarket or small and midsize customers, and the Honorable Mention section names no vendor and points to a separate Gartner piece, "Midmarket Context", which was not opened (Vendor Strengths and Cautions; Honorable Mention) [analyst]. And because most operations sit at Level 3 or below, most warehouse operations, in Gartner's model, do not need the most advanced functionality that an evaluation of the most capable products rewards.

**How big the market is, and how spread.** The 2022 report forecast the market "to grow to over $4 billion by 2026", with a five-year compound annual growth rate "of over 13%" (Market Considerations) [analyst]. That is Gartner's forecast as of June 2022. This unit opened no later figure; the seed bibliography lists a Gartner market share analysis dated 20 May 2026 (A4), which was not opened. Bartholdi and Hackman wrote, in the 2017 release, that "there are over 300 WMS vendors in the US alone" and that the largest companies held less than 20% of the market (§4.4) [practice: the text gives no source for either figure]. Gartner's review market page listed 140 products on 24 November 2026 (Peer Insights) [analyst]. An evaluation covers far fewer: the 2022 Magic Quadrant gave strengths and cautions for 17 vendors (section 8), and its inclusion rules required, among other things, a share of revenue or customers outside the vendor's home region and sales and implementation resources in three or more regions, and excluded standalone component providers and vendors concentrated in one geography (Inclusion and Exclusion Criteria, read through a summary) [analyst]. So a vendor that sells only in one country, or only one module, is absent from the list by rule, whatever its product does.

**The fictional vendors on these types.** The case register gives three: Halvern Systems (fictional) sells order, warehouse and transport software and nothing else; Varnby Software (fictional) sells an ERP with warehouse and transport as modules of it; Kestrow (fictional) sells one warehouse system, to smaller distributors and online sellers on a single site (case register). On the 2022 types, Halvern is read here as a suite vendor of execution software, Varnby as an application vendor whose warehouse system is a module of its ERP, and Kestrow as a specialist (this unit's placement; the register does not use the analyst's types). These are case facts and evidence of nothing in the world.

## 3. Deployment: cloud, hosted, on your own servers

Three ways of running a warehouse system recur in sales and in evaluations. The standards body's definitions give the vocabulary.

- **Cloud subscription, shared (multi-tenant software as a service).** In NIST's definition of software as a service (SaaS), the customer "does not manage or control the underlying cloud infrastructure including network, servers, operating systems, storage", nor individual application capabilities, apart from limited user-specific configuration settings; the provider's resources are "pooled to serve multiple consumers using a multi-tenant model" ([Mell & Grance, *The NIST Definition of Cloud Computing*, NIST SP 800-145, September 2011, section 2](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)) [independent, for what the standard defines].
- **Hosted, dedicated.** NIST's **private cloud** is infrastructure "provisioned for exclusive use by a single organization", run by the organisation, a third party or both, on or off premises (section 2) [independent]. Gartner's 2022 report names the same split for warehouse software: "dedicated or multitenant cloud SaaS" is one of the factors behind a vendor's position (Market Considerations) [analyst].
- **On the customer's own servers (on-premises).** The customer runs the software in its own building or data centre. Corvane (fictional) runs its warehouse system "about twelve years old on its own servers", near the end of its vendor's support (case register).

**What each means for upgrades**, from the sources opened:

- **Multi-tenant SaaS.** Because the customer controls neither the servers nor the application's capabilities (NIST) [independent], the provider applies a new version to everyone on the shared service; the customer does not choose whether the code changes, only, at most, the settings it controls (this unit's inference from NIST's definition; no source opened states how warehouse-software providers schedule releases, beyond Gartner's 2022 note that some vendors' architecture "allows continuous upgrades" (section 10)).
- **Dedicated hosting.** NIST's private cloud is for one organisation's exclusive use (NIST SP 800-145, section 2) [independent], so a hosted instance can run a version of its own (this unit's inference); whether a given provider lets a hosted customer stay on an older version is a contract question, unsourced here.
- **Own servers.** The customer, or a partner it pays, installs each upgrade. Corvane's position, a system near the end of its vendor's support, is where that leads when upgrades are not taken (case register; the link is this unit's reading).

What the analyst wrote about the choice, in 2022: in Gartner's estimate (no sample stated), close to 70% of new customers preferred cloud "if the economics are reasonable", while "a little over a quarter of completed deployments are cloud, with around 8% multitenant cloud" (Context) [analyst]; and "the impact of deployment models has diminished as the majority of WMS vendors now offer some form of cloud strategy", while "there remains a continuing debate among vendors and buyers on whether multitenant SaaS is demonstrably better than dedicated cloud" (Evaluation Criteria) [analyst]. It also wrote that service "contributes to implementation success and overall customer satisfaction, as well as impacting upgrade cycles and TCO" (total cost of ownership) (Evaluation Criteria) [analyst]. Common claim C8, that cloud software means no more upgrades, is set against these sources in section 10.

## 4. Configuration and customisation, and why the line matters years later

**The two words.** **Configuration** changes what the software does by setting the parameters its maker provides: a rule, a threshold, a screen layout, a label format. **Customisation** (also modification) changes or adds code, so the software does something its maker did not ship. A peer-reviewed systematic review of ERP customisation (26 papers, from 1,542 database hits, 2024) describes configuration as "Parametrization": "Configuring functions through standard software parameters" ([Abendroth, Bender & Gronau, ICEIS 2024, pp. 17–27](https://doi.org/10.5220/0012305500003690), read at [SciTePress](https://scitepress.org/Papers/2024/123055/123055.pdf)) [independent]. The review reports that Brehm, Heinzl and Markus (2001) used "tailoring" to cover both configuration and modification and set out seven tailoring types, adding extended reporting, workflow programming and interfaces (Abendroth et al., section 2) [practice: Brehm et al. not opened here, reported by the review]. The boundary is not sharp in practice: the review's own definition of technical customisation takes in configuration changes as well.

**Why the line matters to the customer years later.** Three sources point the same way.

- Light's two case studies of ERP projects found that "to avoid invalidating maintenance and development support from the ERP vendor", most organisations reengineer their processes to fit the software; some customisation is typically required; and while customisations can give real benefits, whether one is viable needs careful consideration "given its potential impact upon future maintenance" ([Light, 2001, *Journal of Software Maintenance and Evolution* 13(6), 415–429, abstract](https://doi.org/10.1002/smr.240)) [independent: two cases, abstract only].
- The 2024 review states that heavy technical modification leads to increased cost in implementation and in the maintenance phase after it, and that cloud ERPs, "especially SaaS solutions, often have limited opportunities for deep customization"; across 20 years of studies it finds "a shift from ERP code modification in on-premises systems to interface and integration customization" (Abendroth et al., sections 1, 5.5, abstract) [independent].
- For warehouse systems specifically, Bartholdi and Hackman say that a WMS often outlives the language it was written in, so many combine several languages and are hard to maintain or customise, and that most vendors will customise for a price and usually keep the intellectual property in the customisation (§4.6.1, read through a summary; "Most vendors will customize their WMS for the right price" is their sentence) [practice].

Both studies are of ERP software; applying them to warehouse systems is this unit's inference, supported in direction by the textbook's one-paragraph account. What follows for the customer, as this unit's inference from the three: every customisation is a piece of code that must be carried through each later upgrade, tested again, and, where the vendor owns it, paid for again; and on a shared SaaS service, where the customer controls little beyond settings (NIST), much of what was once customised becomes either configuration or a separate program joined through an interface. A product that offers more configuration moves cost out of the customer's future upgrades; a product that needs customisation to fit an operation moves cost into them. SCE14 takes up how implementers decide, and SCE16 prices it.

## 5. The integrations every site needs

A warehouse system is never alone. Four connections recur at every site; for each, what crosses, and what a source says.

**The ERP.** The ERP (enterprise resource planning system; SCE1's working definition: the company's financial and master-data system) sends what should arrive and what must be shipped, and takes back what did. Bartholdi and Hackman: the receipt "drives the paying of bills to suppliers upstream", and the shipment drives "the sending of invoices downstream to the consignee" (§4.1) [practice]; WMS vendors have the advantage that they are "already connected to financial systems" (§4.5) [practice]. In SCE2 §7 the warehouse system receives the expected receipt (purchase order lines) from the ERP and needs the item master (identifiers, pack, dimensions). The textbook lists "EDI capability" (electronic data interchange, the exchange of business messages in standard formats between companies' systems) among advanced features (§4.3) [practice]. Varnby's (fictional) "No integration to build" is the claim a vendor makes when the warehouse system is a module of the ERP (case register); SCE10 sets it against the seams.

**Carriers.** Goods leave with a carrier's label and on a carrier's manifest (the list of parcels or units handed to the carrier). Bartholdi and Hackman list "Carton manifesting" and "Trailer manifesting" among high-end features and "Parcel shipping" among advanced ones (§4.3) [practice]. Corvane (fictional) books carriers through each carrier's own portal (case register), so in SCE3 deliverable C its labels come from the portals, a gap a carrier connection closes (SCE3's reading). The carrier connection sits on the boundary with the transport system (SCE7, SCE8).

**Automation.** Gartner's glossary includes "automated materials handling equipment interfaces" in the WMS (glossary) [analyst]; its 2022 report lists "Automated material handling equipment (MHE) interfaces" among extended capabilities and "material handling automation integration" among the things it assesses (Market Description; Evaluation Criteria) [analyst]. SCE5 §7 sets out the layers between the WMS and the machine (WMS, WES, WCS, equipment) and the dispute over which owns release and task assignment. For the product, the integration is the line where that dispute is settled for one site.

**Labels and printing.** Every logistic unit leaving or arriving needs a label the next party can scan. In GS1's guideline, the SSCC (serial shipping container code) is "the single mandatory element for all logistic labels" (§3.2); usually "the shipper of the goods will create the logistic label"; a carrier or receiver that adds to a label is responsible for its own data (§9.1); a label holds up to three segments, for carrier, customer and supplier (§2.3); and the despatch advice (advance ship notice, ASN) should list each unit's SSCC and contents, so that a scanned SSCC can be matched with it (§§9.3.7, 9.5.3) ([GS1 Logistic Label Guideline, release 1.3, July 2019](https://ref.gs1.org/guidelines/logistic-label)) [independent, for what the guideline says]. The warehouse system therefore issues the SSCC, prints the label at the packing or palletising station, and sends the same number in the electronic notice; the printers themselves, and the format each takes, are a configuration task at every site (this unit's inference; no source on printer formats was opened). GS1 is a global standards body; which message names a region uses (despatch advice or ASN) was not checked here (SCE2 §3.1).

## 6. The capability list

The functions of SCE2 to SCE5, restated as a list a buyer would recognise. Each line names its operation step (with the unit that teaches it) and the sources that name the capability. The analyst terms are Gartner's glossary list (section 1) [analyst] and the extended capabilities of its 2022 report [analyst]; the textbook terms are Bartholdi and Hackman's "menu of features", in three groups: basic, high-end and advanced (§4.3) [practice]. The grouping and the IDs are this unit's; deliverable A uses them.

| ID | Operation step (unit) | Capability | Named as a capability by |
|---|---|---|---|
| W1 | Inbound: order and notice (SCE2 §3.1) | Take expected receipts from the ERP and advance notices from suppliers | B&H §4.1 [practice]; GS1 §9.3.7 [independent] |
| W2 | Inbound: appointment and dock (SCE2 §3.2) | Appointment scheduling and dock doors | B&H basic [practice]; Gartner 2022, "dock scheduling" [analyst] |
| W3 | Inbound: yard (SCE2 §3.2) | Yard management | B&H high-end [practice]; Gartner glossary [analyst] |
| W4 | Inbound: check and count (SCE2 §3.4) | Receiving: check, count and record receipt | B&H basic, §4.1 [practice]; Gartner glossary [analyst] |
| W5 | Inbound: quality hold (SCE2 §3.5; SCE4 §3) | Quality hold and release | B&H basic, "Quality assurance" [practice] |
| W6 | Inbound and outbound: labels (SCE2 §3.6; SCE3 §6) | Issue SSCCs and print logistic labels | GS1 §§3.2, 9.1 [independent] |
| W7 | Inbound: cross-dock (SCE2 §3.7) | Flow-through processing | B&H high-end [practice] |
| W8 | Inbound: put-away (SCE2 §3.8) | Directed put-away and location choice | B&H basic, §4.2 [practice]; Gartner glossary [analyst] |
| W9 | Storage (SCE2 §§4–5; SCE4 §1) | Stock locator: every location and its contents | B&H basic, "Location tracking", §4.2 [practice]; Gartner glossary, "stock locating" [analyst] |
| W10 | Storage and control (SCE4 §§1–3) | Stock attributes and statuses (lot, date, status, owner); rotation by date | Gartner glossary, "inventory management" [analyst]; the attributes are SCE4's working list |
| W11 | Storage: replenishment (SCE2 §6) | Replenishment of forward locations | B&H high-end [practice]; Gartner glossary [analyst] |
| W12 | Control: counting (SCE4 §5) | Cycle counting and adjustments | B&H high-end [practice]; Gartner glossary [analyst] |
| W13 | Control: slotting (SCE4 §6) | Slotting | B&H advanced, "Sku slotting" [practice]; Gartner 2022 [analyst] |
| W14 | Control: returns (SCE4 §7) | Receive and grade returns | B&H high-end, "Returns" [practice] |
| W15 | Control: traceability (SCE4 §8) | Lot traceability: by lot, locations, receipts and shipments | SCE4 §8 (US drug and food rules) [independent]; not named in B&H's menu or Gartner's list |
| W16 | Outbound: release (SCE3 §2) | Order allocation and release, by wave or continuously | Gartner glossary, "order allocation", "wave planning" [analyst]; B&H high-end, "Wave management" [practice] |
| W17 | Outbound: pick (SCE3 §3) | Directed picking on a handheld | B&H basic, "Picking"; high-end, "RF-directed operation" [practice]; Gartner glossary [analyst] |
| W18 | Outbound: pick (SCE3 §3; SCE5 §3) | Voice picking | Gartner 2022 [analyst] |
| W19 | Outbound: pick and sort (SCE3 §§3.3, 3.6) | Pick and put to light | B&H high-end [practice] |
| W20 | Outbound and inbound: travel (SCE2 §3.8; SCE3 §4) | Task interleaving | B&H high-end [practice]; Gartner glossary [analyst] |
| W21 | Outbound: sort, check, pack (SCE3 §§5–6) | Packing and consolidation, with checks | B&H basic [practice]; Gartner glossary, "packing" [analyst] |
| W22 | Outbound: ship (SCE3 §§6–7) | Shipping: register shipment out, carrier labels, carton and trailer manifests, parcel | B&H basic, "Shipping"; high-end, manifesting; advanced, "Parcel shipping" [practice]; Gartner glossary [analyst] |
| W23 | Outbound: value-added work | Value-added services (kitting, light manufacturing) | B&H high-end [practice]; Gartner 2022 [analyst] |
| W24 | The floor: labour (SCE5 §4) | Labour management: standards and tracking | B&H high-end [practice]; Gartner glossary [analyst] |
| W25 | The floor: machines (SCE5 §§6–7) | Interfaces to automation (WCS, WES, equipment) | Gartner glossary [analyst]; Gartner 2022 [analyst] |
| W26 | Across the site: billing (SCE1 §5) | Billing clients by activity (logistics providers) | Gartner 2022, "Third-party logistics (3PL) billing" [analyst] |
| W27 | Across the site: several buildings | Multi-site view | B&H advanced, "Multi-DC view" [practice] |
| W28 | Across the site: integration (section 5) | EDI and interfaces to the ERP and carriers | B&H advanced, "EDI capability"; §4.1 [practice] |
| W29 | Across the site: change (section 4) | Configurability | B&H high-end [practice] |

Two lines in the list have no measurement behind them anywhere in this course: which capabilities a given operation needs, and which are worth paying for. The 2022 report's complexity levels (section 2) are the analyst's answer to the first [analyst]; no independent source on either was opened.

## 7. Worked example: Halvern Warehouse (fictional) on the capability list

Halvern Systems (fictional) sells order, warehouse and transport software and nothing else, to retailers, distributors and logistics providers, mid-sized to large; it delivers by cloud subscription, with implementation by its own services team and by partners; and it says of itself "One vendor for execution" (case register). Its warehouse line is **Halvern Warehouse** (the core system) with six modules: **Labour**, **Voice**, **Yard**, **Slotting**, **Automation Connect** and **Client Billing** (case register). Everything in this section is a case fact or this unit's placement of one; none of it is evidence about any real product, and no real vendor is meant.

**Placing the modules.** Each module name meets one line of the list (deliverable B gives every line):

- Labour on W24 (labour management, SCE5 §4).
- Voice on W18 (voice picking, SCE3 §3, SCE5 §3).
- Yard on W3 (yard management, SCE2 §3.2).
- Slotting on W13 (slotting, SCE4 §6).
- Automation Connect on W25 (interfaces to automation, SCE5 §7).
- Client Billing on W26 (billing clients by activity, the need of Tandric Logistics (fictional), which is paid per pallet in, per pick and per pallet stored per week; case register).

**Placing the core.** The register names Halvern Warehouse as the core system and says nothing of what the core does. This unit places Gartner's core capabilities (to receive, put away, store, count, pick, pack and ship; Peer Insights [analyst]) in it, lines W1, W4, W8, W9, W12, W17, W21 and the shipment record of W22, as an assumption, and lists the assumption in its notes for the register. Every other line is open: the register does not say whether Halvern Warehouse does appointments (W2), quality holds (W5), labels (W6), cross-docking (W7), stock statuses and dates (W10), replenishment (W11), returns (W14), traceability (W15), release (W16), light-directed work (W19), interleaving (W20), value-added work (W23), multi-site views (W27), EDI (W28) or configurability (W29).

**What the map shows that the module list does not**, as this unit's reading:

- **The modules sit on the edges.** All six meet capabilities that Gartner's 2022 report names as extended (labour management, voice picking, yard management, slotting, MHE interfaces, 3PL billing) [analyst]. The record that every other line depends on (W4, W8, W9, W12) is in the core, assumed.
- **Two lines cross into the other lines of the suite.** Returns appear in the register as a module of Halvern Order, the order line, together with Store Fulfilment (case register); whether the warehouse core receives and grades the goods (W14) is open. Carrier labels and manifests (W22) could sit in Halvern Warehouse or in Halvern Transport, whose modules are Rating and Tendering, Fleet Routing, Tracking, Freight Audit and Claims (case register). Those are seam questions for SCE10.
- **The case operations' trouble lands on open lines.** Ostrel Foods' (fictional) short-dated stock found too late needs dates on the stock record (W10) and pick by date (SCE2 §9); Corvane's (fictional) web orders promised from stock the centre cannot find touch counting (W12) and the locator (W9) (case register; SCE4 deliverable A). Of these, the register places only the core.

```viz
{"kind": "matrix", "title": "Halvern's warehouse line on the capability list (fictional)", "cols": ["Inbound", "Storage and control", "Outbound", "The floor", "Across the site"], "rows": [{"label": "Halvern Warehouse (core)", "tone": 1, "cells": ["assumed", "assumed", "assumed", null, null]}, {"label": "Labour", "tone": 2, "cells": [null, null, null, "W24", null]}, {"label": "Voice", "tone": 2, "cells": [null, null, "W18", null, null]}, {"label": "Yard", "tone": 2, "cells": ["W3", null, null, null, null]}, {"label": "Slotting", "tone": 2, "cells": [null, "W13", null, null, null]}, {"label": "Automation Connect", "tone": 2, "cells": [null, null, null, "W25", null]}, {"label": "Client Billing", "tone": 2, "cells": [null, null, null, null, "W26"]}], "legend": [{"mark": "W..", "means": "the capability line of section 6 that the module's name meets"}, {"mark": "assumed", "means": "core lines placed by this unit (W1, W4, W8, W9, W12, W17, W21, part of W22); the register names the core but not its functions"}], "caption": "Section 7 and deliverable B of this unit. Module names from the case register (Halvern Systems, fictional); capability lines from section 6. Case facts, evidence of nothing about any real product."}
```

## 8. The real market: one dated list

The course names real vendors only in a dated list from a named analyst report or an audited filing, every vendor on the list alike, with no vendor assessed, ranked, compared or recommended (course brief).

**The current report could not be reproduced here.** Gartner's index showed the *Magic Quadrant for Warehouse Management Systems* last updated 29 April 2026 and its companion *Critical Capabilities* last updated 30 April 2026, both with a refresh date of 30 April 2027 ([Gartner, Magic Quadrant and Critical Capabilities index, read 24 Nov 2026](https://www.gartner.com/magic-quadrant)) [analyst]. Gartner's abstract page for the 2026 report refused the fetch on 24 November 2026, and no reprint of it was found by search, so this unit could read neither its text nor its list of vendors. Read it at Gartner's document page ([gartner.com/en/documents/7780053](https://www.gartner.com/en/documents/7780053)) or in a reprint a vendor has licensed; when you do, note the date, how you read it, and every vendor it names.

**The most recent edition this unit could read** is the 2022 report, in a reprint; no edition between 2022 and 2026 was opened here. Its list is four years old. It is given here as that report's list, dated 2022; it does not describe the current market.

The vendors evaluated in Gartner's Magic Quadrant for Warehouse Management Systems, 1 June 2022 (ID G00755323; analysts S. Tunstall, D. Klappich, R. Narang), read in a reprint on 24 November 2026, as headed in its Vendor Strengths and Cautions section; its Market Overview says Gartner considered over 70 WMS providers and that these 17 qualified [analyst]:

- Blue Yonder
- Ehrhardt Partner Group (EPG)
- Generix Group
- Infor
- Körber
- Made4net
- Manhattan Associates
- Mantis
- Mecalux
- Oracle
- Reply
- SAP
- Softeon
- SSI SCHAEFER
- Synergy Logistics
- Tecsys
- Vinculum

Three things to keep in mind when you read such a list, as this unit's inference from section 2 and SCE1 §8. Inclusion is by the analyst's rules, which in 2022 left out component vendors and single-region vendors by design. The list gives no placement here, and the course does not reproduce placements. And Gartner's own guidance is to use an evaluation to narrow a list and not to decide on it alone (SCE1 §8, C10).

## 9. Placing a real product line on the map yourself

The course maps no real vendor's product line. It gives you the method and the form (deliverable C) to do it from a vendor's public pages.

**The method**, in this unit's steps (the course's own; no source tests them):

1. **Collect the pages.** The product line's overview, each module's page, the documentation index or release notes if public, and any dated release about the line. Record each address and the date you read it.
2. **List the modules as the vendor names them.** Copy the names exactly; note which are sold as separate products and which as modules, where the pages say so.
3. **Place each module's claims on the capability list.** One row per capability a page claims, with the module that claims it. A claim with no capability on the list gets a row of its own, marked as new.
4. **Grade every row vendor-reported** and date it. A vendor's description of itself is evidence of what it claims, never of what the product does (course brief; SCE1 §10).
5. **Mark the gaps.** Every capability line no page claims is written as "no public claim found", which is different from "not offered".
6. **Check elsewhere what can be checked.** An analyst report that covers the product, read and dated, can confirm that the analyst assessed it, at analyst grade; a peer-review site can give what a counted number of reviewers say, graded vendor-reported (SCE1 §7).

```viz
{"kind": "flow", "title": "Mapping a real product line from public pages", "steps": [{"label": "Collect the pages", "note": "address and date for each"}, {"label": "List the modules", "note": "the vendor's own names"}, {"label": "Place each module's claims", "note": "on lines W1 to W29"}, {"label": "Grade every row", "note": "vendor-reported, dated"}, {"label": "Mark the gaps", "note": "no public claim found"}, {"label": "Check elsewhere", "note": "analyst, peer reviews, each graded"}], "caption": "The six steps of section 9 of this unit, which are the course's own method; the grade rule is SCE1's key (section 10 there) and the capability lines are section 6 of this unit."}
```

**What such pages cannot show**, as this unit's inference from the grade key and the sections above:

- **Whether the feature works as described**, at what volume, or on which device. A page is the vendor's claim (SCE1 §7).
- **Whether a capability is standard, configured or customised.** The pages rarely say whether a customer had a feature built for it; section 4 explains why that matters for every later upgrade.
- **Which deployment a capability needs.** A capability may exist in the on-premises version and not in the shared cloud service, or the reverse; check that each page describes the version you are mapping.
- **Price.** For a private company, no price, discount or revenue appears in this course unless it published it (course brief). Where you need one, write "no public figure".
- **Who uses it.** Named customers on a vendor's pages are the ones the vendor chose (SCE1 §9).
- **Where its boundary with the vendor's other lines runs.** Halvern's returns and carrier labels (section 7) show the kind of question pages leave open.

## 10. C8: "Cloud software means no more upgrades"

**The claim as it circulates.** Cloud software means no more upgrades (course list, C8). One instance, named here only as the claim under examination: a trade-magazine article by Roberto Michel in *Modern Materials Handling* says cloud warehouse systems bypass "the need for big upgrade projects" and that vendors "regularly send out updates to the system to keep users on the latest software" ([Michel, "The pluses propelling cloud warehouse management systems (WMS)", no date shown, read 24 Nov 2026](https://www.mmh.com/article/the_pluses_propelling_cloud_warehouse_management_systems_wms/software_tech)). The same article says the software still changes, through updates.

**What the sources opened show.**

- NIST's definition places control of the application with the provider in SaaS; the customer keeps only limited user-specific configuration settings (section 3) [independent]. The upgrade still happens; who performs it and who decides when move to the provider (this unit's inference).
- Gartner wrote in 2022 that service affects "upgrade cycles and TCO" and that whether multitenant SaaS is "demonstrably better than dedicated cloud" is a continuing debate (section 3) [analyst]. That is an analyst's view; it reports no measurement. The same report's Market Overview says some vendors had rewritten their WMS on a microservices architecture "that allows continuous upgrades" in a multitenant cloud [analyst]; read with NIST, the upgrades arrive continuously from the provider (this unit's inference).
- The ERP review finds that SaaS limits deep customisation and that customisation has moved to interfaces and integrations (section 4) [independent]. Each interface is something the customer must keep working through the provider's changes (this unit's inference).
- Light's two cases found that a customisation needs careful consideration for its potential impact on future maintenance (section 4) [independent: abstract only].

**What the evidence shows.** No source opened says upgrades end in the cloud. The sources describe a change in who performs the upgrade, who chooses its timing, and what the customer must test and maintain (its configuration and its interfaces). No independent source was found that measures upgrade effort or cost for warehouse systems in the cloud against those on a customer's own servers. **No independent source found** for the claim.

## 11. What SCE14 takes from this unit

The implementation topics this unit raises, for SCE14 to treat with implementers and administrators as users:

- **Configuration choices**: who sets the rules of release, put-away, replenishment and counting, and who may change them (sections 4, 6).
- **Customisations**: which are made, who owns them, and what they cost at each upgrade (section 4).
- **The four integrations**: ERP, carriers, automation, labels and printing, each built and tested (section 5).
- **Master data**: the item master and the location records the system needs before go-live (SCE2 §7; section 5).
- **Upgrades under each deployment**: who applies them, when, and what the customer tests each time (sections 3, 10).
- **The gap lines** of a capability map: capabilities the operation needs that no module claims (section 7; deliverable B).

## 12. Glossary lines

| Term | Working definition | Source |
|---|---|---|
| Core WMS capabilities | Receive, put away, store, count, pick, pack and ship | Gartner Peer Insights [analyst] |
| Extended WMS capabilities | Functions WMS providers offer beyond the core, such as labour management or slotting | Gartner Peer Insights; Gartner 2022 [analyst] |
| Stock locator system | The part of a WMS that manages storage locations as an inventory alongside product | B&H §4.2 [practice] |
| Warehouse complexity level | Gartner's five-level grading of warehouse operations, Level 1 the most basic, Levels 4 and 5 the most complex and automated | Gartner 2022 [analyst] |
| Software as a service (SaaS) | Software run by the provider, the customer controlling only limited user-specific settings | NIST SP 800-145 [independent] |
| Multi-tenant | One provider's resources pooled to serve several customers | NIST SP 800-145 [independent] |
| Dedicated (private) cloud; hosted | Infrastructure for one organisation's exclusive use, run by it or a third party, on or off premises | NIST SP 800-145 [independent]; "dedicated" in Gartner 2022 [analyst] |
| On-premises | Software run on the customer's own servers | Working definition |
| Upgrade | Moving a running system to a newer version of the vendor's software | Working definition |
| Configuration (parametrisation) | Changing what software does through the parameters its maker provides | Abendroth et al. 2024 [independent] |
| Customisation (modification) | Changing or adding code so the software does what its maker did not ship | Working definition; Abendroth et al. 2024 [independent] |
| Tailoring | Configuration and modification together (Brehm et al.'s term, as reported) | Abendroth et al. 2024 [practice: origin not opened] |
| Total cost of ownership (TCO) | What a customer pays for a system over its life | Named in Gartner 2022 [analyst]; definition is the course's; SCE16 |
| Electronic data interchange (EDI) | Exchange of business messages in standard formats between companies' systems | Named in B&H §4.3 [practice]; definition is the course's |
| Manifest | The list of parcels or units handed to a carrier | Named in B&H §4.3 [practice]; definition is the course's |
| Serial shipping container code (SSCC) | The serial number of a logistic unit, the one mandatory element of a GS1 logistic label | GS1 Logistic Label Guideline §3.2 [independent] |
| Capability map | A table placing a vendor's modules on the operation's capability lines, with source, date and grade | This unit, deliverable A |

## On a site visit

SCE6 is not an operations unit, so the visit is to colleagues in sales, services and product. Ask:

- **Which definition of a WMS do our requirements lists and contracts use: the textbook's record, Gartner's core, or Gartner's core plus extended?** (Section 1.)
- **Which of our modules does the analyst count as core, and which as extended?** And which analyst edition, dated, read in a reprint or in abstract? (Sections 1, 2, 8.)
- **Which deployments do we offer, and who applies an upgrade in each? Can a hosted customer stay on an older version, and on what terms?** (Section 3.)
- **For our last few implementations, what was configured and what was customised, and who owns the customisations?** (Section 4.)
- **Which of the four integrations (ERP, carriers, automation, labels and printing) did each recent customer have built, and by whom?** (Section 5.)
- **Where does our warehouse line end and our transport or order line begin for returns and carrier labels?** (Section 7.)
- **When we say a cloud customer will not need upgrades, what do we mean, and what does the customer still test at each release?** (Section 10.)

## Self-check

1. **How do Bartholdi and Hackman define the core of a WMS, and how does Gartner's glossary definition differ?**
   The textbook's core is a database of SKUs and a stock locator system, and it says most systems manage transactions without optimising. Gartner's glossary defines a WMS as software that helps manage and intelligently execute a warehouse's operations and lists fifteen capabilities, including labour, yard and equipment interfaces (section 1).
2. **What does Gartner's review page call core and what extended?**
   Core: receive, put away, store, count, pick, pack and ship. Extended: additional functionality WMS providers offer beyond the core, such as managing labour or optimising the locating of inventory (section 1).
3. **Does the 2022 Magic Quadrant sort the market into tiers?**
   No. It names five types of vendor (application mega vendors, SCM suite vendors, specialist WMS suite vendors, MHE and automation vendors, independent component vendors; the last not covered) and grades warehouses on five complexity levels; most operations are Level 3 or below (section 2).
4. **In NIST's definition of SaaS, what does the customer control?**
   Neither the infrastructure nor the application's capabilities, only limited user-specific configuration settings; resources are pooled across customers in a multi-tenant model (section 3).
5. **Why does a customisation matter at every later upgrade?**
   Light's ERP cases found customisations need careful consideration of their impact on future maintenance; the 2024 review finds heavy modification raises maintenance cost and that SaaS limits deep customisation; Bartholdi and Hackman say vendors customise for a price and usually keep the intellectual property (section 4).
6. **What must the warehouse system do so that a scanned pallet label matches the electronic notice?**
   Issue the SSCC, print it on the label (the one mandatory element), and list each unit's SSCC and contents in the despatch advice, so the scan can be matched with it (GS1; section 5).
7. **Which lines of the capability list do Halvern's (fictional) six modules meet, and what does the register leave open?**
   Labour W24, Voice W18, Yard W3, Slotting W13, Automation Connect W25, Client Billing W26. The register names the core but not its functions; this unit assumes the core capabilities there, and leaves fifteen lines open, among them returns and carrier labels, which may sit in the order or transport line (section 7).
8. **A colleague says cloud software means no more upgrades. What do you answer?**
   No source opened says so. NIST puts control of the application with the provider, so the upgrade moves to the provider; the customer still keeps its settings and interfaces working; no independent source measures upgrade effort in the cloud against on-premises (section 10).

## Deliverable

### A. The capability map form

The fields are fixed here; SCE8, SCE9 and SCE17 reuse them in this order. One row per capability line a vendor's material claims, or that the operation needs and nothing claims.

| # | Field | What goes in it |
|---|---|---|
| 1 | Operation step | The step of the operation, with the unit that teaches it (SCE1's map; SCE2 to SCE5 for the warehouse) |
| 2 | Capability | The line of the capability list (section 6 here: ID and name), or a new line marked "new" |
| 3 | Module that claims it | The vendor's own name for the product or module, exactly as written; "no public claim found" where none does |
| 4 | Source and date | The page, document or register the claim comes from, and the date it was read |
| 5 | Grade | vendor-reported for a vendor's own material; analyst for an analyst report, with how it was read; independent only for an audited filing about the vendor's own figures; "case" for a fictional vendor's register entry |
| 6 | Gap or question | What the source leaves open: version, deployment, boundary with another line, configured or customised |

### B. Halvern's warehouse line, mapped (fictional)

Vendor: Halvern Systems (fictional). Line: Halvern Warehouse (core system) with modules Labour, Voice, Yard, Slotting, Automation Connect, Client Billing; delivery by cloud subscription; implementation by its own services team and by partners (case register). Source for every row: the case register, Halvern Systems (fictional), read 24 November 2026. Grade for every row: **case** (a fictional vendor's register entry; for a real vendor these rows would be vendor-reported). "Assumed" marks this unit's placement in the core, listed in the notes for the register.

| # | Operation step | Capability | Module that claims it | Source and date | Grade | Gap or question |
|---|---|---|---|---|---|---|
| 1 | Inbound: order and notice (SCE2 §3.1) | W1 Expected receipts and advance notices | Halvern Warehouse (core), assumed | Case register, 24 Nov 2026 | case | Which ERP messages it takes is not in the register (W28) |
| 2 | Inbound: appointment and dock (SCE2 §3.2) | W2 Appointment scheduling and dock doors | No claim in the register | Case register, 24 Nov 2026 | case | In Yard or in the core? |
| 3 | Inbound: yard (SCE2 §3.2) | W3 Yard management | Yard | Case register, 24 Nov 2026 | case | none |
| 4 | Inbound: check and count (SCE2 §3.4) | W4 Receiving | Halvern Warehouse (core), assumed | Case register, 24 Nov 2026 | case | none beyond the assumption |
| 5 | Inbound: quality hold (SCE2 §3.5) | W5 Quality hold and release | No claim in the register | Case register, 24 Nov 2026 | case | Needs statuses (W10) |
| 6 | Inbound and outbound: labels (SCE2 §3.6; SCE3 §6) | W6 SSCCs and logistic labels | No claim in the register | Case register, 24 Nov 2026 | case | Printing configured at each site (section 5) |
| 7 | Inbound: cross-dock (SCE2 §3.7) | W7 Flow-through processing | No claim in the register | Case register, 24 Nov 2026 | case | none |
| 8 | Inbound: put-away (SCE2 §3.8) | W8 Directed put-away and location choice | Halvern Warehouse (core), assumed | Case register, 24 Nov 2026 | case | none beyond the assumption |
| 9 | Storage (SCE2 §§4–5; SCE4 §1) | W9 Stock locator | Halvern Warehouse (core), assumed | Case register, 24 Nov 2026 | case | none beyond the assumption |
| 10 | Storage and control (SCE4 §§1–3) | W10 Stock attributes, statuses, rotation by date | No claim in the register | Case register, 24 Nov 2026 | case | Ostrel's (fictional) short-dated stock depends on it; owner per record needed by Tandric (fictional) |
| 11 | Storage: replenishment (SCE2 §6) | W11 Replenishment of forward locations | No claim in the register | Case register, 24 Nov 2026 | case | none |
| 12 | Control: counting (SCE4 §5) | W12 Cycle counting and adjustments | Halvern Warehouse (core), assumed | Case register, 24 Nov 2026 | case | Who may approve an adjustment is a configuration question (SCE4 §5) |
| 13 | Control: slotting (SCE4 §6) | W13 Slotting | Slotting | Case register, 24 Nov 2026 | case | A re-slot moves records too (SCE4 §6) |
| 14 | Control: returns (SCE4 §7) | W14 Receive and grade returns | No claim in the warehouse line; Halvern Order lists Returns | Case register, 24 Nov 2026 | case | Which line grades and puts away returned goods? (SCE10) |
| 15 | Control: traceability (SCE4 §8) | W15 Lot traceability | No claim in the register | Case register, 24 Nov 2026 | case | Needs lots on every move (W10) |
| 16 | Outbound: release (SCE3 §2) | W16 Order allocation and release | No claim in the register | Case register, 24 Nov 2026 | case | Core, or the WES layer (SCE5 §7)? |
| 17 | Outbound: pick (SCE3 §3) | W17 Directed picking on a handheld | Halvern Warehouse (core), assumed | Case register, 24 Nov 2026 | case | none beyond the assumption |
| 18 | Outbound: pick (SCE3 §3; SCE5 §3) | W18 Voice picking | Voice | Case register, 24 Nov 2026 | case | none |
| 19 | Outbound: pick and sort (SCE3 §§3.3, 3.6) | W19 Pick and put to light | No claim in the register | Case register, 24 Nov 2026 | case | In Automation Connect? |
| 20 | Outbound and inbound: travel (SCE2 §3.8; SCE3 §4) | W20 Task interleaving | No claim in the register | Case register, 24 Nov 2026 | case | none |
| 21 | Outbound: sort, check, pack (SCE3 §§5–6) | W21 Packing and consolidation, with checks | Halvern Warehouse (core), assumed | Case register, 24 Nov 2026 | case | none beyond the assumption |
| 22 | Outbound: ship (SCE3 §§6–7) | W22 Shipping, carrier labels, manifests, parcel | Shipment record: Halvern Warehouse (core), assumed; labels and manifests: no claim | Case register, 24 Nov 2026 | case | Warehouse or Halvern Transport? (SCE10) |
| 23 | Outbound: value-added work | W23 Value-added services | No claim in the register | Case register, 24 Nov 2026 | case | none |
| 24 | The floor: labour (SCE5 §4) | W24 Labour management | Labour | Case register, 24 Nov 2026 | case | Standards set how (SCE5 §4)? |
| 25 | The floor: machines (SCE5 §§6–7) | W25 Interfaces to automation | Automation Connect | Case register, 24 Nov 2026 | case | Which layer owns release and task assignment (SCE5 §7)? |
| 26 | Across the site: billing (SCE1 §5) | W26 Billing clients by activity | Client Billing | Case register, 24 Nov 2026 | case | Billing depends on every activity being recorded (Tandric's disputed invoices, register) |
| 27 | Across the site: several buildings | W27 Multi-site view | No claim in the register | Case register, 24 Nov 2026 | case | none |
| 28 | Across the site: integration (section 5) | W28 EDI and interfaces to the ERP and carriers | No claim in the register | Case register, 24 Nov 2026 | case | Halvern's "One vendor for execution" covers its own three lines; the ERP is outside them |
| 29 | Across the site: change (section 4) | W29 Configurability | No claim in the register | Case register, 24 Nov 2026 | case | What is configured and what customised under cloud subscription (sections 3, 4) |

Below the table: six lines claimed by a named module (3, 13, 18, 24, 25, 26); eight placed in the core by assumption (1, 4, 8, 9, 12, 17, 21, part of 22); fifteen with no claim in the register. The open question for SCE10 is which of Halvern's three lines holds returns (row 14) and carrier labels (row 22).

### C. Template: the capability map

Fill one row per capability line for a real vendor's warehouse line. Keep the IDs of section 6 so later units can refer to them; add a row marked "new" for a claim the list lacks.

Vendor: ______ (name as on its pages) · Line: ______ (core product and modules, the vendor's names) · Deployment the pages describe: ______ (shared cloud, dedicated hosting, own servers; which version) · Date filled: ______ · Pages read: ______ (each address with the date read)

| # | Operation step | Capability | Module that claims it | Source and date | Grade | Gap or question |
|---|---|---|---|---|---|---|
| 1 | Inbound: order and notice (SCE2 §3.1) | W1 Expected receipts and advance notices | ______ (the module's name exactly as written, or "no public claim found") | ______ (page title, address, date read) | ______ (vendor-reported for the vendor's own pages) | ______ (version, deployment, boundary, configured or customised) |
| 2 | Inbound: appointment and dock | W2 Appointment scheduling and dock doors | ______ | ______ | ______ | ______ |
| 3 | Inbound: yard | W3 Yard management | ______ | ______ | ______ | ______ |
| 4 | Inbound: check and count | W4 Receiving | ______ | ______ | ______ | ______ |
| 5 | Inbound: quality hold | W5 Quality hold and release | ______ | ______ | ______ | ______ |
| 6 | Inbound and outbound: labels | W6 SSCCs and logistic labels | ______ | ______ | ______ | ______ |
| 7 | Inbound: cross-dock | W7 Flow-through processing | ______ | ______ | ______ | ______ |
| 8 | Inbound: put-away | W8 Directed put-away and location choice | ______ | ______ | ______ | ______ |
| 9 | Storage | W9 Stock locator | ______ | ______ | ______ | ______ |
| 10 | Storage and control | W10 Stock attributes, statuses, rotation by date | ______ | ______ | ______ | ______ |
| 11 | Storage: replenishment | W11 Replenishment of forward locations | ______ | ______ | ______ | ______ |
| 12 | Control: counting | W12 Cycle counting and adjustments | ______ | ______ | ______ | ______ |
| 13 | Control: slotting | W13 Slotting | ______ | ______ | ______ | ______ |
| 14 | Control: returns | W14 Receive and grade returns | ______ | ______ | ______ | ______ |
| 15 | Control: traceability | W15 Lot traceability | ______ | ______ | ______ | ______ |
| 16 | Outbound: release | W16 Order allocation and release | ______ | ______ | ______ | ______ |
| 17 | Outbound: pick | W17 Directed picking on a handheld | ______ | ______ | ______ | ______ |
| 18 | Outbound: pick | W18 Voice picking | ______ | ______ | ______ | ______ |
| 19 | Outbound: pick and sort | W19 Pick and put to light | ______ | ______ | ______ | ______ |
| 20 | Outbound and inbound: travel | W20 Task interleaving | ______ | ______ | ______ | ______ |
| 21 | Outbound: sort, check, pack | W21 Packing and consolidation, with checks | ______ | ______ | ______ | ______ |
| 22 | Outbound: ship | W22 Shipping, carrier labels, manifests, parcel | ______ | ______ | ______ | ______ |
| 23 | Outbound: value-added work | W23 Value-added services | ______ | ______ | ______ | ______ |
| 24 | The floor: labour | W24 Labour management | ______ | ______ | ______ | ______ |
| 25 | The floor: machines | W25 Interfaces to automation | ______ | ______ | ______ | ______ |
| 26 | Across the site: billing | W26 Billing clients by activity | ______ | ______ | ______ | ______ |
| 27 | Across the site: several buildings | W27 Multi-site view | ______ | ______ | ______ | ______ |
| 28 | Across the site: integration | W28 EDI and interfaces to the ERP and carriers | ______ | ______ | ______ | ______ |
| 29 | Across the site: change | W29 Configurability | ______ | ______ | ______ | ______ |
| new | ______ (the step it belongs to) | ______ (the vendor's claim, in your words) | ______ | ______ | ______ | ______ |

**Steps for filling it from a real vendor's public pages** (section 9):

1. Search for the vendor's product pages, module pages, documentation index and dated releases about the line. Open each at the vendor's own address; record the address and the date.
2. Copy the vendor's names for the core product and each module into the header, exactly as written.
3. For each page, find each capability it claims and write the module's name in that line's "Module that claims it" field. A claim that fits no line goes in a "new" row.
4. In "Source and date", give the page's own headline, its address and the date you read it.
5. Grade every row **vendor-reported**. An analyst report that you read, dated, may add a line of its own at analyst grade, saying how you read it; it does not change the vendor's rows.
6. Write "no public claim found" in every line no page claims; it does not mean the capability is absent.
7. In "Gap or question", note what the page leaves open: which version or deployment it describes, whether the capability is standard, configured or customised, and where it meets the vendor's other lines.
8. Below the table, count the lines claimed, the lines with no claim found and the new lines, and write the open questions for the seams (SCE10) and for implementation (SCE14). Write no price unless the vendor published it; otherwise "no public figure".

## Sources

All addresses opened on 24 November 2026; the source log gives what was read at each.

- Abendroth, A., Bender, B. & Gronau, N. (2024). The Evolution of Original ERP Customization: A Systematic Literature Review of Technical Possibilities. In *Proceedings of the 26th International Conference on Enterprise Information Systems (ICEIS 2024)*, vol. 1, 17–27. https://doi.org/10.5220/0012305500003690 (read at https://scitepress.org/Papers/2024/123055/123055.pdf)
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapter 4. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- Gartner. Glossary, "Warehouse Management System (WMS)". Undated. https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/warehouse-management-system-wms
- Gartner. Magic Quadrant and Critical Capabilities index (no headline shown), read 24 November 2026. https://www.gartner.com/magic-quadrant
- Gartner. "Magic Quadrant for Warehouse Management Systems". S. Tunstall, D. Klappich, R. Narang. Published 1 June 2022, ID G00755323. Reprint. https://dam.infor.com/api/public/content/d8957bc1ac164bf1843965deeaa7e26a?v=d2e94df6
- Gartner. "Magic Quadrant for Warehouse Management Systems", 29 April 2026. Not opened (the abstract page refused the fetch); named as where to read the current list. https://www.gartner.com/en/documents/7780053
- Gartner Peer Insights. "Warehouse Management Systems Reviews and Ratings". Features updated May 2026. https://www.gartner.com/reviews/market/warehouse-management-systems?months=12
- GS1. *GS1 Logistic Label Guideline*, release 1.3, ratified July 2019. https://ref.gs1.org/guidelines/logistic-label
- Light, B. (2001). The maintenance implications of the customization of ERP software. *Journal of Software Maintenance and Evolution: Research and Practice* 13(6), 415–429. https://doi.org/10.1002/smr.240 (abstract, read at https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software)
- Mell, P. & Grance, T. *The NIST Definition of Cloud Computing*. NIST Special Publication 800-145, September 2011. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
- Michel, R. "The pluses propelling cloud warehouse management systems (WMS)". *Modern Materials Handling*, no date shown. Named as the claim under examination (C8). https://www.mmh.com/article/the_pluses_propelling_cloud_warehouse_management_systems_wms/software_tech

## Unsure list

# Unsure: SCE6

1. Every quotation was taken from a fetch tool's extraction and not re-read against a second copy; the 2022 Gartner reprint was read through a fetch tool in targeted passes, not every part verbatim: the writer read characters 0–100,000 of 131,630; the applier read characters 100,000–131,630 only for the Market Overview and Context quotations now in sections 3, 8 and 10. The fetch tool returned the Context figures (section 3) as separate fragments; that "a little over a quarter of completed deployments are cloud, with around 8% multitenant cloud" is one contiguous phrase was not checked.
2. The 2022 report's inclusion rules (share of revenue or customers outside the home region, resources in three or more regions, exclusion of component and single-geography vendors) were read through the tool's summary, not quoted; their exact terms were not checked.
3. The 2022 report's Market Overview states that Gartner considered over 70 WMS providers and that only the 17 vendors highlighted provided the evidence; the 17 are taken from the Vendor Strengths and Cautions headings. The Magic Quadrant figure is an image the tool could not read, so the 17 were not checked against it.
4. Bartholdi and Hackman §4.6.1 (customisation for a price, the vendor keeping the intellectual property, most systems managing transactions without optimising) was read through the tool's paraphrase except the one quoted sentence; page 36 was not re-read.
5. The Gartner glossary page for the WMS showed no headline and no date; the Sources title "Warehouse Management System (WMS)" is the glossary term, not a headline read on the page.
6. Light (2001): the abstract was read at the author's university repository, which offered no full text; the DOI 10.1002/smr.240 comes from a bibliographic index (University of Utah) and was not resolved at the publisher.
7. Abendroth et al. (2024): that Brehm, Heinzl and Markus (2001) set out seven tailoring types is the review's report; the original was not opened.
8. The Modern Materials Handling article shows no date in what was read, and its byline (Roberto Michel, senior editor) is as the tool reported it.
9. Gartner's index dates (WMS Magic Quadrant 4/29/26, Critical Capabilities 4/30/26, refresh 4/30/27) are as the page served them on 24 Nov 2026; the 2026 report itself was not opened.
10. The placement of Halvern's (fictional) core capabilities (W1, W4, W8, W9, W12, W17, W21, part of W22) is this unit's assumption, not a register fact; deliverable B marks it "assumed".

Object: none

Fresh check 2026-11-24 (claude-opus-5-5): fix · 0 errors, 7 should-fix, 7 minor; all applied; report audits/supply-chain-execution/fresh-check-SCE6.md
