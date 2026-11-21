---
code: SCE2
title: Inbound and storage
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-21
search: off
intro: SCE2 follows goods from the truck at the gate to stock in a location: pallet, case and each; the purchase order and advance notice, the appointment and dock, unloading, checking and counting, quality hold, labelling, cross-docking and put-away; storage media; reserve and forward locations and replenishment; what the warehouse system does and needs at each step; the inbound measures the benchmark surveys name; and date-coded and chilled goods. Its deliverable is two inbound flow maps built on the fictional case (Ostrel Foods and Corvane), a blank flow-map template whose columns SCE3, SCE7 and SCE9 reuse, and glossary lines. Written 21 Nov 2026 by Opus 5.5 with search off (references still opened live, all on 21 Nov 2026) and fresh-checked by a separate Opus 5.5 context before filing (verdict fix; every finding applied). Known gaps: most of the unit rests on one textbook, Bartholdi and Hackman's Warehouse & Distribution Science, release 0.98, read through a tool's extraction, so most claims are graded practice, sections are cited without page numbers, and its quotations and some section placements (the SKU definition, the handling-cost sentence, Theorem 8.3, FIFO in drive-through and pallet flow rack) were not re-read against the PDF; the later release 0.98.1 was not opened; ten seed references were not opened, among them Gu, Goetschalckx and McGinnis (2007) and Rouwenhorst et al. (2000); Staudt et al. (2015) was read in abstract only, so the unit says only that its four dimensions exist; the quality hold is a working description, unsourced; the five inbound measures carry the course's working definitions, because WERC keeps its definitions in an online tool that was not opened and its 2026 report with values is paid, so no benchmark values are given; the EU and US regulation texts could not be read, so no EU or US storage-temperature rule is stated and EU date law is given only as Ireland's food safety authority states it, unchecked against the regulation; the FSAI and USDA pages are undated; whether the GS1 label rules quoted are the guideline's normative text or its summary was not confirmed; regional pallet sizes are not covered.
---

# SCE2 · Inbound and storage

Grades follow SCE1's key: every claim that carries a number, a mechanism or a recommendation ends with [independent], [analyst], [vendor-reported] or [practice]. Most of this unit's support is one textbook, Bartholdi and Hackman's *Warehouse & Distribution Science* (release 0.98, revised 28 August 2017, read as full text, in targeted passes, at the authors' Georgia Tech address), so most of it is graded practice: an account of how the work is done, with no measurement behind it. Where this unit opened no source for something, it says so and makes no claim. Lines marked as this unit's inference carry no grade.

This is the course's first unit in the operations pattern. Each step is treated as the physical event, the people doing it, what the software does, how it commonly fails, and the measure that shows it improved. The deliverable's flow map fixes the columns SCE3, SCE7 and SCE9 reuse.

## 1. What a warehouse is for

Bartholdi and Hackman open with the question "Why have a warehouse?" (§1.1) and list its uses under two headings [practice]:

- **To match supply with demand.** A warehouse holds stock against seasonal surges, unreliable transport, unreliable demand or price increases; in their words, warehouses can buffer the supply chain against collapsing demand (§1.1) [practice].
- **To consolidate.** A distributor may consolidate shipments from vendors into large shipments for downstream customers, which reduces transport cost (§1.1) [practice].

They add two further uses: **postponement**, holding product undifferentiated until nearer the customer, and centralising tasks such as price labelling (§1.1) [practice]. And they describe the **crossdock** (in this course, cross-dock), where each facility receives product from many vendors, sorts it, and prepares loads for each store (§1.1) [practice]. A cross-dock is a warehouse that consolidates without storing.

What this means for software, as this unit's inference: a warehouse system is judged on two things that pull apart. It must keep an accurate record of goods that wait (the buffer), and it must move goods through fast (the consolidation). Inbound is where both start: a pallet that is received wrongly is wrong in the record for as long as it waits, and a pallet that waits on the dock delays every order that needs it.

Bartholdi and Hackman's types of warehouse (§1.2) matter for this unit in one place: a **perishables warehouse** may handle food, fresh flowers, vaccines or other product needing refrigeration; product there dwells for very short times, frequently only hours; and such warehouses may have requirements to ship product by FIFO (first in, first out) or FEFO (first expired, first out) (§1.2) [practice]. Section 9 takes these up.

## 2. The units goods arrive in: pallet, case, each

**Stock keeping unit (SKU).** Bartholdi and Hackman define it as "the smallest physical unit of a product that is tracked by an organization" (§2.2) [practice]. Corvane (fictional), a fashion retailer, counts each size and colour as its own item and has about 18,000 of them (case register).

**Units of handling.** Goods travel in different units at different points in the chain. Bartholdi and Hackman's account: product generally flows upstream in larger units such as pallets, then to local warehouses in cases, and finally to stores in inner-packs or individual pieces (§2.2) [practice]. The course uses three words:

- **Pallet** (also unit load): a platform of goods handled as one load by a forklift.
- **Case** (also carton): a supplier's sealed box of a fixed number of units.
- **Each** (also piece, single item): one saleable unit.

Their reasoning for why the change from one unit to another is where labour goes is one sentence: "In general, the smaller the handling unit, the greater the handling cost" (ch. 3 introduction) [practice]. A pallet is moved once with one truck trip; the same goods as forty cases are forty handlings; as several hundred eaches, several hundred. Every place where a larger unit is broken into smaller ones (a pallet opened to pick cases, a case opened to pick eaches) multiplies the handlings that follow. This unit opened no study that measures the multiplier; the direction is the textbook's, and the arithmetic is this unit's illustration.

The two case operations sit at different points on that ladder. Ostrel Foods (fictional), a food distributor, picks by the case onto roll cages; Corvane (fictional) replenishes stores by carton and by single item and ships web orders of one to three items (case register). Corvane therefore breaks units twice (pallet to carton, carton to each); Ostrel once (pallet to case). This is this unit's reading of the register, and it is why later units treat their picking differently (SCE3).

## 3. The inbound sequence, step by step

Bartholdi and Hackman's inbound processes are **receiving** and **put-away**, before order-picking, checking, packing and shipping (ch. 3) [practice]. The brief's sequence below splits receiving into the steps a product team will meet as separate screens. For each: the physical event, the people, what the system does, how it fails, and its measure. Section 8 gives the measures' sources; section 7 gathers the system's work and data.

```viz
{"kind": "flow", "title": "Inbound, from order to location", "per_row": 4, "steps": [{"label": "Purchase order and advance notice", "note": "what is coming"}, {"label": "Appointment and dock", "note": "when, which door"}, {"label": "Unload", "note": "staged for put-away"}, {"label": "Check and count", "note": "exceptions noted"}, {"label": "Quality hold", "note": "where inspection applies"}, {"label": "Label", "note": "SSCC on the logistic unit"}, {"label": "Cross-dock or store", "note": "to shipping, or to put-away", "tone": 3}, {"label": "Put away", "note": "location chosen, location scanned", "tone": 2}], "caption": "The inbound steps of section 3 of this unit, in order. Step names follow the course brief; the notes come from Bartholdi and Hackman, Warehouse & Distribution Science, release 0.98 (2017), sections 1.1, 3.1, 3.2 and 4.3, and GS1's Logistic Label Guideline, release 1.3 (July 2019), as cited in section 3."}
```

### 3.1 The purchase order and the advance notice

**Physical event.** None yet: this step is paper or data. A **purchase order** (PO) is the buyer's order to a supplier; it says what should arrive. An **advance notice** says what has actually been sent.

**What the sources say.** "Receiving may begin with advance notification of the arrival of goods" (Bartholdi & Hackman §3.1) [practice]. The textbook does not use the term advance shipping notice. GS1, the standards body for barcodes and business messages, names the message "Despatch Advice / ASN" and says it should specify, for each logistic unit, its SSCC (the unit's serial number, §3.6) and the trade items it contains ([GS1 Logistic Label Guideline, release 1.3, July 2019](https://www.gs1.org/standards/gs1-logistic-label-guideline)) [independent]. **Region note:** you will meet both names, "despatch advice" and "advance ship notice" (ASN), for the same message; GS1 writes them as one name, and this unit opened no source on which region uses which, so it makes no claim about it.

**People.** The buyer who placed the PO and the supplier who sends the notice; neither works in the warehouse. The ERP holds the PO (SCE1 placed purchase orders in the ERP as a working placement).

**System.** The warehouse system receives the expected receipt from the ERP and, where the supplier sends one, the advance notice. With an advance notice that lists each pallet's SSCC, receipt can be confirmed per pallet by scan rather than per line by count; that is this unit's inference from GS1's rule, not a measured result.

**Common failure.** No notice, a late notice, or a notice that does not match the truck. This unit opened no source that measures how often; it is named as a failure the next steps must catch (section 3.4).

**Measure.** WERC asks for the percentage of supplier orders received with correct documents (section 8) [practice].

### 3.2 The appointment and the dock

**Physical event.** A truck arrives at the yard and is given a **dock door** (a loading bay where a trailer backs up to the building).

**What the sources say.** "It is not unusual for warehouses to schedule trucks to within 30-minute time windows" (§3.1) [practice]. Bartholdi and Hackman list appointment scheduling among the basic features of a warehouse management system (WMS) (§4.3) [practice], and yard management among the high-end ones (§4.3) [practice].

**People.** The supplier's or carrier's driver; at the site, whoever books appointments and assigns doors. Neither case operation's register names this person.

**System.** Holds the appointment calendar and the door assignment. SCE1 §4 places dock doors under yard management, which may be a module of the warehouse system or a separate system; it says nothing about appointments.

**Common failure.** A truck arriving outside its window, or unbooked, queues at the gate or takes a door planned for another. Named, not measured: no source was opened.

**Measure.** WERC asks for on-time receipts from suppliers (section 8) [practice].

### 3.3 Unloading

**Physical event.** "Once the product has arrived, it is unloaded and possibly staged for put away" (§3.1) [practice]. **Staging** is setting goods down in a marked floor area near the dock until the next step.

**People.** Forklift or pallet-truck drivers; at Ostrel Foods (fictional), Bram drives a reach truck for put-away and replenishment on nights (case register); who unloads is not in the register.

**System.** Records that the trailer is being unloaded and, if it tracks staging lanes as locations, where each pallet was set down. Bartholdi and Hackman's standard is that a good WMS tracks every place product can be, down to the forks of individual forklift trucks (§4.2) [practice].

**Common failure.** Goods left in staging are in the building but not in a location the record knows (this unit's inference from §4.2).

### 3.4 Checking and counting

**Physical event.** Product is inspected and exceptions noted, "such as damage, incorrect counts, wrong descriptions" (§3.1) [practice]. It "is likely to be scanned to register its arrival so that ownership is assumed" (§3.1) [practice]: the moment of receipt is the moment the goods become the buyer's on the record.

**People.** Receiving clerks or checkers. Neither register names them.

**System.** This is the step the warehouse system exists for. "The most fundamental capability of a WMS is to record receipt of inventory into the warehouse" (§4.1) [practice], and that receipt drives the paying of bills to suppliers upstream (§4.1) [practice]. The system compares what arrived with the PO and the notice, records the differences, and sends the receipt to the ERP (SCE1 §3).

**Common failure.** Damage, wrong counts and wrong descriptions are the textbook's own list (§3.1) [practice]. Two consequences follow as this unit's inference: a count accepted without checking puts an error into the stock record that every later promise inherits (Corvane's known trouble, web orders promised from stock the centre cannot find, is the kind of failure this produces; SCE4 traces it); and a receipt recorded wrongly pays the supplier wrongly.

**Measure.** Percentage of supplier orders received damage free (WERC, section 8) [practice].

### 3.5 Quality hold

**Physical event.** Goods that must be inspected before use are set aside and may not be picked until released.

**What the sources say.** Bartholdi and Hackman list quality assurance among a WMS's basic features (§4.3) [practice], without describing it. This unit opened no source that describes a quality hold as a process, so what follows is a working description, not a claim: a **hold** is a status on stock that keeps it in the record but blocks it from being allocated to orders until someone releases it.

**People.** Whoever has authority to release; neither register names one.

**System.** Puts received stock into a held status, keeps it out of available stock, and records who released it and when (working description).

**Common failure.** Held stock released without the check, or good stock forgotten on hold. Named, not measured.

**Measure.** No inbound benchmark for holds was found in the sources opened.

### 3.6 Labelling

**Physical event.** Each pallet or case is given a label the warehouse can scan, if the supplier's label is missing or unusable.

**What the sources say.** GS1 defines a **logistic unit** as any combination of trade items packaged together for storage and/or transport, such as a case, pallet or parcel, and the **SSCC** (Serial Shipping Container Code) as the number that identifies it ([GS1, SSCC page](https://www.gs1.org/standards/id-keys/sscc)) [independent]. The GS1 Logistic Label Guideline says the label allows each logistic unit to be identified uniquely, and that the one mandatory element is that unique serial number (release 1.3) [independent]. A label can carry only one batch number and only one date value; best-before, expiry and sell-by dates are optional, and where used must relate to the trade item on the label (same guideline) [independent].

**People.** Receiving staff, where the site relabels.

**System.** Prints a label with a new identifier, or reads the supplier's SSCC and links it to the pallet's contents (this unit's inference from the GS1 rule above).

**Common failure.** A pallet whose trade items carry different dates or batches cannot show them on one GS1 label: rules [4-20] and [4-24] allow one date value and one batch number per label, and rule [4-21], a best practice, says that where items with several best-before dates are loaded together the earliest date is used on the label and on the despatch advice (same guideline) [independent]; mixed-batch pallets are therefore split or labelled by the site's own scheme (this unit's inference).

### 3.7 Cross-docking: the alternative to storing

**Physical event.** Goods go from the receiving dock to the shipping dock without being put away. Section 1 gives the textbook's description (§1.1) [practice].

**System.** Bartholdi and Hackman list flow-through processing among a WMS's high-end features (§4.3) [practice]. To cross-dock, the system must know at receipt which outbound order or destination the goods are for, which means the outbound demand has to be in the system before the truck is unloaded (this unit's inference).

**Common failure.** Goods arrive for which no outbound load is ready, and so are stored after all, or wait on the dock. Named, not measured.

**Where it fits the case.** Ostrel's work starts in the evening for delivery the next morning, and Corvane replenishes 60 stores (case register). Whether either cross-docks is not in the register.

### 3.8 Put-away

**Physical event.** The pallet or case is moved from the dock to a storage location and set down.

**What the sources say.** "Before product can be put away, an appropriate storage location must be determined" (§3.2) [practice], and where it is stored largely decides how quickly it can be retrieved later (§3.2) [practice]. Choosing locations means "managing a second inventory, not of product, but of storage locations" (§3.2) [practice]. The storage location should itself be scanned to record where the product was placed (§3.2) [practice]. Put-away can take a fair amount of labour because product may travel a long way to its location (§3.2) [practice].

**People.** Lift-truck drivers. At Ostrel Foods (fictional), Bram, on nights (case register).

**System.** Directs the move. Bartholdi and Hackman name "directed put-away and directed picking" as functions of the stock locator system (§4.2) [practice]: the system chooses the location, sends the task to the driver's device, and waits for the driver to scan the location as confirmation. It can also pair a put-away with a retrieval nearby, which they describe as interleaving put-aways and retrievals to reduce deadheading, the empty travel between tasks (ch. 6) [practice]; they list task interleaving among high-end WMS features (§4.3) [practice].

**Common failure.** Goods put in a location other than the one the system recorded. The textbook's rule to scan the location (§3.2) exists to prevent it; the consequence, stock the record shows in one place and the shelf has in another, is SCE4's subject.

**Measure.** Dock-to-stock cycle time and lines received and put away per hour (section 8) [practice].

**Two cost shares you will hear.** Bartholdi and Hackman say receiving accounts for only about 10% of operating costs in a typical distribution centre, and put-away about 15%, crediting both to Frazelle's *World-Class Warehousing* (1996) and, for receiving, also his *World-Class Warehousing and Material Handling* (2002) (§3.1, §3.2; bibliography [21], [22]) [practice]. This unit did not open Frazelle, so the origin is not traced and both figures are graded practice under SCE1's key.

## 4. Storage media and when each is used

**Storage media** are the physical means of holding goods. Bartholdi and Hackman's chapter 5 and chapter 6 give the choices and the trade-off that runs through them: deeper storage needs fewer aisles and gives up direct access to each load (ch. 5, ch. 6) [practice]. "Aisles provide accessibility, not storage" (ch. 6) [practice].

- **Floor storage (block stacking).** The simplest way of storing pallets, typically arranged in lanes, one SKU per lane to avoid double-handling (§5.1.1, ch. 6) [practice]. As a lane empties, its space cannot be used by another SKU until the lane is clear; "This loss of space is called honey-combing" (§5.1.1) [practice]. Deeper lanes are more exposed to honeycombing; shallow lanes spend more space on access (ch. 6) [practice]. It suits pallets that stack: heavy, fragile or uneven pallets cannot be stacked high (ch. 6) [practice].
- **Selective (single-deep) pallet rack.** One pallet deep, each pallet reachable on its own, at the price of more aisle space (§5.1.1) [practice]. Installing rack lets pallets be stored independently of each other where they cannot be stacked (ch. 6) [practice].
- **Double-deep, drive-in and push-back rack.** Deeper rack for fewer aisles: double-deep is two single-deep racks one behind the other; drive-in lets a lift truck drive into the rack frame, floor storage for product that is not otherwise stackable; push-back lanes pull out like a drawer (§5.1.1) [practice]. Of drive-in and drive-through rack, only drive-through rack, entered from both ends, lets product move first-in-first-out (§5.1.1) [practice].
- **Pallet flow rack.** Deep lanes with slanted, roller-lined shelving: pallets are put in at one side and taken out at the other, and the textbook calls it appropriate for high-throughput facilities (§5.1.1) [practice].
- **Shelving (bin-shelving, static rack).** The most basic and least expensive storage, for slower-moving or small items (§5.1.2) [practice].
- **Flow rack (carton flow).** Tilted shelves with rollers that bring cases forward for picking; it is restocked from the back, independently of picking, so restocking never interferes with picking as it does with static shelving (§5.1.3) [practice]. The textbook's summary puts it as flow rack for cartons of faster-moving items (ch. 5) [practice].
- **Automated storage and retrieval systems (AS/RS)**, at the level of a mention: machines that store and fetch loads; in a unit-load AS/RS a stacker crane does the handling (§5.1.1) [practice]. SCE5 treats the machines.

```viz
{"kind": "matrix", "title": "Storage media: what each holds and is used for", "cols": ["Holds", "Each pallet reachable", "Fewer aisles", "First in, first out", "Used for"], "rows": [{"label": "Floor storage", "tone": 1, "cells": ["pallets", null, "deep lanes", null, "stackable pallets"]}, {"label": "Selective rack", "tone": 2, "cells": ["pallets", "yes", "no", null, "pallets stored singly"]}, {"label": "Double-deep rack", "tone": 2, "cells": ["pallets", "no", "yes", null, "fewer aisles"]}, {"label": "Drive-in rack", "tone": 2, "cells": ["pallets", "no", "yes", "drive-through only", "non-stackable pallets"]}, {"label": "Push-back rack", "tone": 2, "cells": ["pallets", "no", "yes", null, "fewer aisles"]}, {"label": "Pallet flow rack", "tone": 2, "cells": ["pallets", "no", "yes", null, "high throughput"]}, {"label": "Shelving", "tone": 3, "cells": ["small items", null, null, null, "slow or small items"]}, {"label": "Carton flow rack", "tone": 3, "cells": ["cases", null, null, null, "fast-moving cartons"]}], "legend": [{"mark": "a word", "means": "as Bartholdi and Hackman state it for that medium"}, {"mark": "blank", "means": "the source read does not say"}], "caption": "The storage media of section 4 of this unit and the properties Bartholdi and Hackman, Warehouse & Distribution Science, release 0.98 (2017), §5.1 and ch. 6, state for each. Blank cells are not stated in the source read; AS/RS is mentioned in the text and not drawn."}
```

Which medium Ostrel or Corvane uses is not in the case register.

## 5. Reserve and forward pick locations

A warehouse usually keeps more than one location per SKU. Bartholdi and Hackman's terms:

- **Reserve** (also bulk): where most of the stock is held, in large units.
- **Forward pick area** (also fast-pick area): "A particularly convenient region that is replenished from within the warehouse" (ch. 7) [practice]. Many of the most popular SKUs are stored there in relatively small amounts, so that it works as a "warehouse within the warehouse" (§8.1) [practice].

In the simplest layout, for picking cases from pallets, the forward area is the ground-floor pallet locations and the reserve is all the higher locations; popular SKUs are picked from ground level and replenished by dropping overstock pallets from above (ch. 7) [practice].

**The reasoning for a forward area.** Picks are concentrated in a small, convenient space, so pickers travel less per pick. The cost is restocking: the forward area must be replenished from reserve, and for some SKUs "the cost of restocking them can outweigh any savings in pick costs" (§8.1) [practice]. Slow-moving SKUs are better picked from reserve, which leaves forward space for the popular ones (§8.4) [practice]. So the decision is per SKU: which SKUs go forward, and how much of each.

On how much, the textbook tests two rules commonly used: give every SKU the same space (Equal Space), or the same number of days of supply (Equal Time). It shows that Equal Time requires the same total restocks as Equal Space, contrary to the belief that it reduces them, and that neither is optimal (§8.3.2, Theorem 8.3) [practice]; for two warehouses it reports that Equal Time needed about 1.45 times the restocks of the optimal allocation for 6,000 fast-moving SKUs of a major drug-store chain, and about 2.44 times for 4,000 SKUs of a telecommunications company (§8.3.3) [practice]. This unit did not read the data behind the two ratios, so they are graded practice; they show the size of the difference the rule can make, not a figure to expect.

What this means for software, as this unit's inference: a system that supports a forward area must hold two kinds of location for one SKU (forward and reserve), a capacity for each forward location, and a rule for which SKUs are assigned forward. The assignment itself is **slotting**; Halvern Warehouse (fictional) sells it as a separate Slotting module, and Kestrow WMS (fictional) lists no such module (case register). Both are facts of the case register, graded nothing, and say nothing about real products.

## 6. Replenishment and what triggers it

**Replenishment** (also restocking) is moving stock from reserve to a forward location. Bartholdi and Hackman describe three triggers:

1. **Empty location.** When a ground-level pallet location is emptied, a restocker is dispatched with a high-reach forklift to bring down a pallet of the same SKU from above (ch. 7, §7.1.1) [practice].
2. **A pick larger than what is forward.** If a pick quantity exceeds the amount in the forward area at that time, a restock is triggered (§8.2) [practice].
3. **A reorder point.** A forward reorder point per SKU triggers restocks, with safety stock held to guard against stockout in the forward area (§8.3.6, §8.5.2, exercise 8.9) [practice].

**Timing.** Restocks can happen during picking or on another shift, when timing may be less critical (§8.2) [practice]; one option is to defer all restocks until the end of the pick wave, so the forward area can be restocked without interfering with picking (ch. 7) [practice]. Extra pallets forward allow restocks to be scheduled rather than made in reaction to need (§7.1.2) [practice].

**Why it matters.** Stockouts at the forward location can disrupt order-picking, which is the reason for carrying safety stock forward (§8.5.2) [practice]. One of the textbook's exercises states a rule of at least two pallets forward for any SKU, to avoid stockouts while waiting for replenishment (exercise 7.20) [practice]; it is an exercise's premise, not a finding.

**At the case operation.** At Ostrel Foods (fictional), Bram does put-away and replenishment on nights, and picking starts in the evening (case register). Both the put-away and the replenishment work therefore compete for the same driver in the same hours (this unit's reading of the register). Pairing a put-away with a retrieval from reserve on one trip is the textbook's interleaving of put-aways and retrievals, which cuts deadheading (§6.2.1) [practice]; whether it eases Bram's nights is this unit's inference.

**System.** Bartholdi and Hackman list replenishment among high-end WMS features (§4.3) [practice]. The system computes the trigger, creates the task, directs the driver to the reserve location and then to the forward location, and asks for a scan at each (this unit's inference from §4.2's directed tasks).

## 7. What the warehouse system does at each step, and what it needs

Three mechanisms recur through sections 3 to 6.

- **Directed tasks.** The system tells a person what to do next, where, and with what; Bartholdi and Hackman's terms are directed put-away and directed picking, and RF-directed operation (tasks sent to radio-frequency terminals) among the high-end features (§4.2, §4.3) [practice].
- **Location choice.** The system allocates available locations (ch. 4 introduction) [practice]; locations may be **dedicated** (each reserved for one product only) or **shared** (a product may be stored in more than one location, and an emptied location can be reassigned) (§2.4) [practice].
- **Confirmation by scan.** Product "should be scanned at all key decision points" (ch. 3 introduction) [practice]: at arrival to register ownership (§3.1), and at the storage location to record where it went (§3.2) [practice]. Because several people update the same records at once, the record needs transaction processing to stay consistent (§4.2) [practice].

**The data it needs.** A typical WMS knows every item in the warehouse, its physical dimensions and how the vendor packs it, and every storage location with its address and dimensions (ch. 4 introduction) [practice]. Set out step by step, as this unit's working list built from the sections above:

| Step | Data the system needs |
|---|---|
| Purchase order and notice | The PO lines (item, quantity, supplier, due date); the notice's logistic units, each with its SSCC and contents (GS1) |
| Appointment and dock | Supplier or carrier, expected time window, door |
| Check and count | Item master: identifiers, pack (units per case, cases per pallet), dimensions; tolerances for over- and under-delivery |
| Quality hold | Which items or suppliers require inspection; who may release |
| Label | Label format; for dated goods, the one date type and the batch per logistic unit (GS1) |
| Cross-dock | Outbound demand by destination, known before receipt |
| Put-away | Locations with address, dimensions, type, zone; dedicated or shared rule; current contents |
| Replenishment | Forward location per SKU, its capacity, its trigger (empty, pick larger than stock, reorder point) |

The tolerance and zone fields are this unit's inference from the steps, not listed in a source.

## 8. The inbound measures the benchmark surveys report

**WERC** (the Warehousing Education and Research Council) runs an annual benchmarking survey of distribution centres. Its 2025 survey asked for calendar-2024 performance on five inbound measures ([WERC DC Measures Survey - 2025](https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf)) [practice]:

1. Dock to Stock Cycle Time, in Hours
2. Lines Received and Put-away per Hour
3. Percent of Supplier Orders Received with Correct Documents
4. Percent of Supplier Orders Received Damage Free
5. On Time Receipts - Supplier

The survey document gives no definitions (they appear in pop-ups in the online tool, which this unit did not open), no sample and no values; its profile questions ask respondents' region, with North America, Europe and Asia among the options. The grade is practice because no sample is stated in what was read. The 2026 report with values is paid or members-only and was not opened, so **no value is given here**.

**Definitions.** APQC, a benchmarking organisation, describes the measure as the average dock-to-stock cycle time in hours for supplier deliveries: the cycle begins when the business receives the delivery from the supplier and continues until the goods are put away in inventory after being recorded in its inventory management system; the page shows no formula and no values ([APQC, measure page](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/dock-stock-cycle-time-hours-supplier)) [practice]. The working definitions below are this course's own, written so that a team can compute each from a warehouse system's records; they are not WERC's wording.

| Measure (WERC's name) | Working definition | Data it needs from the system |
|---|---|---|
| Dock to Stock Cycle Time, in Hours | Average time from a delivery's arrival at the dock to its goods being recorded in a storage location and available | Arrival timestamp; put-away confirmation timestamp |
| Lines Received and Put-away per Hour | Receipt lines both received and put away, divided by the labour hours spent on them | Lines; hours booked to inbound |
| Percent of Supplier Orders Received with Correct Documents | Supplier orders whose paperwork or notice matched what arrived, over all received | A match flag per receipt |
| Percent of Supplier Orders Received Damage Free | Supplier orders received with no damage recorded, over all received | Damage exception per receipt |
| On Time Receipts - Supplier | Supplier orders arriving within their due date or window, over all received | Due date or appointment; arrival time |

**The research view.** Staudt, Alpan, Di Mascolo and Rodriguez's literature review collects operational warehouse performance indicators from published papers, classifies them by time, cost, quality and productivity, and defines them ([2015, abstract read](https://doi.org/10.1080/00207543.2015.1030466)) [independent]. On the abstract alone, this unit can say only that the four dimensions exist; the five WERC measures fall into them as one time, one productivity, two quality measures and one that is both time and quality (this unit's sorting).

## 9. Date-coded and temperature-controlled goods

Ostrel Foods (fictional) carries about 4,500 items, chilled, frozen and ambient, most of them dated, in one warehouse with three temperature zones; its known trouble is short-dated stock found too late (case register). What changes at each step:

**Dates and the rotation rule.** Perishables warehouses may have requirements to ship by **FIFO** (first in, first out: oldest receipt first) or **FEFO** (first expired, first out: earliest date first) (Bartholdi & Hackman §1.2) [practice]. Under FEFO the system must know each pallet's date, which means the date is captured at receipt (this unit's inference). Storage media differ here (section 4): a lane loaded and emptied from one end gives up its oldest pallet last (this unit's inference).

**What the date means differs by region.**

- **European Union.** Ireland's food safety authority states that under Article 24(1) of Regulation (EU) No 1169/2011, after the "use by" date a food is deemed unsafe and placing it on the market is illegal, while nothing in legislation prevents a packaged food being sold on or after its "best before" date if it is still fully acceptable ([FSAI, "Labelling Requirements and Shelf Life"](https://www.fsai.ie/Business-Advice/Running-a-Food-Business/Food-Safety-and-Hygiene/Shelf-life/Labelling)) [practice]. The grade is practice because this is the authority's guidance; the regulation's own text on EUR-Lex could not be read.
- **United States.** The USDA's Food Safety and Inspection Service states: "Except for infant formula, product dating is not required by Federal regulations." It describes "Best if Used By/Before" as a quality date and not a purchase or safety date, and "Sell-By" as telling the store how long to display the product ([USDA FSIS, "Food Product Dating"](https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/food-product-dating)) [practice]. State rules were not checked.

So a system that blocks expired stock must know which kind of date it holds; the GS1 label carries one date value, normally of the same type as the date on the product (GS1 guideline) [independent]. Which dates an operation may sell past, and when, is a legal question: put it to the operation's quality or legal team, or to the national food authority.

**Traceability: the batch.** FSAI states that Regulation (EC) No 178/2002 requires every food business to have a traceability system, with a legal minimum of one-up-one-down (what you received and from whom; what you dispatched and to whom); that "It is not necessary in law to trace to the batch level"; and that recording batch codes and quantities at goods inwards and dispatch is best practice ([FSAI, "Traceability - FAQ"](https://www.fsai.ie/business-advice/starting-a-food-business/traceability/traceability)) [practice]. For the warehouse system, recording the batch at receipt is what makes a recall of one batch possible without pulling every pallet of the item (this unit's inference).

**Temperature.** In the UK, GOV.UK's business guidance states: "Chilled food must be kept at 8°C or below," a legal requirement in England, Wales and Northern Ireland and a recommendation in Scotland; it advises putting frozen food in the freezer as soon as it is delivered ([GOV.UK, "Food hygiene for businesses: Chilling and freezing", last updated 25 Jun 2026](https://www.gov.uk/food-hygiene-businesses/chilling-and-freezing)) [practice]. The EU's hygiene regulation and the US federal rules for food warehousing could not be opened here (source log), so this unit states no rule for the EU or the US. For the inbound sequence, the consequence is this unit's inference: chilled and frozen goods cannot wait in an ambient staging lane, so the step order shortens, and the system needs each item's temperature zone and each location's zone so that it never directs a frozen pallet to an ambient location. Which temperature rule binds a given site is a legal question for the site's food safety authority.

**The short-dated failure.** Ostrel's trouble, short-dated stock found too late (case register), is the kind of failure a system produces when it does not hold dates at receipt or does not rotate by them; this is this unit's reading, and the register does not say which is the cause. SCE4 takes up how records go wrong.

## On a site visit

At the receiving dock and in storage, look for, and ask:

- **Is there an advance notice, and does it list each pallet?** Ask what share of suppliers send one, and what the receivers do when the truck does not match it (section 3.1).
- **Where are the trucks booked, and how wide are the windows?** Bartholdi and Hackman report 30-minute windows as not unusual (section 3.2).
- **Watch a pallet from trailer to location.** Count how often it is set down, and whether each place it waits is a location the system knows (sections 3.3, 3.8).
- **What do the receivers check, and what happens to an exception?** Damage, wrong count, wrong description: who records it, where, and who decides (section 3.4).
- **Is the location scanned at put-away, or only the pallet?** (Section 3.8.)
- **Which goods are on hold now, since when, and who can release them?** (Section 3.5.)
- **Where is the forward area, what triggers a restock, and who does it in which hours?** Ask whether pickers wait for replenishment, and when restocks are done relative to picking (sections 5, 6).
- **For dated goods: is the date captured at receipt, and does the system direct picks by it?** For chilled and frozen goods: how long may a pallet wait outside its zone, and who decided that (section 9).
- **Which of WERC's five inbound measures does the site track, and from which timestamps?** (Section 8.)

## Self-check

1. **Give the two headed uses of a warehouse in Bartholdi and Hackman's §1.1.**
   To match supply with demand (buffering against surges, unreliable transport, unreliable demand or price increases) and to consolidate shipments from vendors to reduce transport cost; they add postponement and centralised tasks such as price labelling (section 1).
2. **Why does labour concentrate where pallets are broken into cases and cases into eaches?**
   Because, in Bartholdi and Hackman's words, the smaller the handling unit, the greater the handling cost; each break multiplies the handlings that follow (section 2).
3. **What does a WMS record at receipt, and what does that receipt drive in the ERP?**
   The receipt of inventory into the warehouse, its most fundamental capability; the receipt drives the paying of bills to suppliers (section 3.4).
4. **What does GS1 say the despatch advice or ASN should contain?**
   For each logistic unit, its SSCC and the trade items it contains (section 3.1).
5. **What is honeycombing, and which storage choice makes it worse?**
   Space lost in a lane that cannot be used by another SKU while it empties; deeper lanes are more exposed to it (section 4).
6. **What is the trade-off in a forward pick area?**
   Picks are concentrated in a small convenient space, but the area must be restocked from reserve, and for some SKUs the restocking cost outweighs the pick savings (section 5).
7. **Name three things that trigger a replenishment in Bartholdi and Hackman's account.**
   An emptied forward location; a pick larger than the quantity forward; a forward reorder point (section 6).
8. **Under FSAI's account of EU law, may a food be sold after its use-by date, and after its best-before date?**
   Not after use-by (it is deemed unsafe); after best-before, nothing in legislation prevents it if the food is still fully acceptable (section 9).

## Deliverable: the inbound flow map

The flow map has six columns, fixed here for SCE3, SCE7 and SCE9: **Step**, **People**, **System touchpoint**, **Data needed**, **Common failure**, **Measure**. Rows are numbered so later units can refer to them. Every cell comes from this unit's sections (named in brackets) or from the case register; a cell the register does not fill says "not in the register". A failure listed for a case operation is a failure to look for there, not a claim that the operation has it, unless the cell says "known trouble".

### A. Ostrel Foods (fictional)

Ostrel Foods (fictional): a food distributor buying from producers and delivering to restaurants, canteens and small shops; about 4,500 items, chilled, frozen and ambient, most dated; one warehouse with three temperature zones; picking by the case onto roll cages, work starting in the evening for delivery the next morning; an ERP with a warehouse module; known trouble includes short-dated stock found too late (case register). People in the register who touch inbound: Bram, reach-truck driver for put-away and replenishment on nights; Ilse, team lead for chilled picking, whose pickers depend on replenishment (this unit's reading); Aart, operations director (case register).

| # | Step | People | System touchpoint | Data needed | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Purchase order and advance notice | Ostrel's buyer and the producer; not named in the register | ERP holds the PO; warehouse module receives the expected receipt and any notice (3.1) | PO lines; per pallet, SSCC, contents, batch and date (3.1, 3.6, 9) | No notice, or one that does not match the truck (3.1) | Percent of supplier orders with correct documents (8) |
| 2 | Appointment and dock | Producer's driver; door assignment not in the register | Appointment calendar and door, in the warehouse module or none (3.2) | Supplier, window, door, temperature zone of the load (3.2, 9) | Unbooked or late trucks queue; chilled loads wait (3.2, 9) | On time receipts, supplier (8) |
| 3 | Unload | Not in the register | Records unloading; staging lane as a location if tracked (3.3) | Staging locations by temperature zone (9) | Chilled or frozen goods waiting outside their zone (9, inference) | Dock-to-stock time starts here (8) |
| 4 | Check and count | Not in the register | Records the receipt against PO and notice; sends receipt to ERP for supplier payment (3.4) | Item master with case and pallet pack; date and batch per pallet (3.4, 9) | Damage, wrong count, wrong description (3.4); date not captured, so rotation cannot work (9) | Percent received damage free (8) |
| 5 | Quality hold | Not in the register | Held status that blocks allocation until released (3.5, working description) | Which items need inspection; who may release (3.5) | Released unchecked, or forgotten on hold (3.5) | No benchmark found (3.5) |
| 6 | Label | Receiving staff, where Ostrel relabels; not in the register | Reads the producer's SSCC or prints a label (3.6) | One batch and one date per logistic unit (GS1, 3.6) | Mixed pallet with two dates or batches (3.6) | Percent with correct documents (8) |
| 7 | Cross-dock or store | Not in the register | Flow-through processing where used (3.7) | Next morning's route demand, known before receipt (3.7) | No outbound load ready; whether Ostrel cross-docks is not in the register (3.7) | No benchmark found |
| 8 | Put away | Bram, reach-truck driver, nights (register) | Directed put-away by zone; scan of the location (3.8, 9) | Locations with zone, type, dimensions; FEFO rule (3.8, 9) | Wrong location; frozen pallet to a wrong zone (3.8, 9) | Dock-to-stock time; lines received and put away per hour (8) |
| 9 | Replenish forward | Bram, nights (register); Ilse, team lead, chilled picking (register), whose pickers depend on it (this unit's reading) | Trigger, task, scan at reserve and forward (6) | Forward location per item, capacity, trigger, dates for FEFO (6, 9) | Forward empty when picking starts in the evening; put-away and replenishment compete for one driver (6, reading of register) | No WERC inbound measure; stockouts at the pick face (6) |

Known trouble mapped to the rows (case register): short-dated stock found too late touches rows 4, 8 and 9, as this unit's reading (section 9).

### B. Corvane (fictional)

Corvane (fictional): a fashion retailer with 60 stores in four European countries and one website; one 28,000 m² distribution centre, two shifts and a third in peak; about 18,000 items counted by size and colour, two main seasons a year; store replenishment by carton and single item, web orders of one to three items, returns from web and stores; about 140 staff in a normal week and 260 in peak; a warehouse system about twelve years old near the end of its vendor's support; known trouble includes web orders promised from stock the centre cannot find (case register). People who touch inbound: Carla, inventory controller, answers for the stock record at receiving and put-away (register, added by SCE1); Marek, site manager (register).

| # | Step | People | System touchpoint | Data needed | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Purchase order and advance notice | Buyer and supplier; not named in the register | ERP holds the PO; warehouse system receives the expected receipt and any notice (3.1) | PO lines by size and colour; per carton or pallet, SSCC and contents (3.1, 3.6) | No notice, or one that does not match (3.1) | Percent of supplier orders with correct documents (8) |
| 2 | Appointment and dock | Supplier's driver; door assignment not in the register | Appointment calendar and door (3.2) | Supplier, window, door (3.2) | Unbooked or late trucks queue (3.2) | On time receipts, supplier (8) |
| 3 | Unload | Not in the register | Records unloading; staging as a location if tracked (3.3) | Staging locations (3.3) | Goods in staging the record does not know (3.3) | Dock-to-stock time starts here (8) |
| 4 | Check and count | Not in the register; Carla answers for the record (register) | Receipt against PO and notice; receipt to ERP (3.4) | Item master per size and colour; units per carton (3.4) | Wrong count or wrong description of size or colour (3.4) | Percent received damage free (8) |
| 5 | Quality hold | Not in the register | Held status where used (3.5, working description) | Which items need inspection; who releases (3.5) | Released unchecked, or forgotten (3.5) | No benchmark found (3.5) |
| 6 | Label | Not in the register | Reads supplier SSCC or prints a label (3.6) | Logistic unit and contents (3.6) | Label not linked to contents (3.6, inference) | Percent with correct documents (8) |
| 7 | Cross-dock or store | Not in the register | Flow-through for store replenishment where used (3.7) | Store demand by destination before receipt (3.7) | No store load ready; whether Corvane cross-docks is not in the register (3.7) | No benchmark found |
| 8 | Put away | Not in the register; Carla answers for the record (register) | Directed put-away; scan of the location (3.8) | Locations; dedicated or shared rule (3.8, 7) | Goods put where the record does not say; known trouble: stock the centre cannot find (register, as this unit's reading) | Dock-to-stock time; lines received and put away per hour (8) |
| 9 | Replenish forward | Not in the register; web pickers such as Mina, operator (register), depend on it | Trigger, task, scan (6) | Forward location per size and colour, capacity, trigger (6) | Forward location empty when a web pick arrives (6) | No WERC inbound measure; stockouts at the pick face (6) |

Corvane breaks units twice, pallet to carton and carton to each (section 2), so rows 8 and 9 carry more locations per item than at Ostrel; that is this unit's reading of the register.

### C. Template: the inbound flow map

Fill one row per step for a real operation, or for a product by naming the screen or module at each step. Keep the step numbers; add a row where the operation has a step the map lacks, and say why. Mark each cell's grade (independent, analyst, vendor-reported, practice) or "observed" for what you saw yourself.

Operation or product: ______ (name; kind of company; region, North America or Europe or other) · Goods: ______ (unit loads received: pallet, case, each; dated or not; temperature zones) · Date filled: ______ · Sources used: ______ (each with its grade)

| # | Step | People | System touchpoint | Data needed | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Purchase order and advance notice | ______ (who orders, who sends the notice) | ______ (which system holds the PO; which receives the notice, and in what message: despatch advice, ASN, other) | ______ (fields per line and per logistic unit) | ______ (what happens when the notice is missing or wrong) | ______ (correct documents, or the site's own) |
| 2 | Appointment and dock | ______ (who books, who assigns doors) | ______ (calendar, yard system or none) | ______ (window, door, load type) | ______ (what happens to an unbooked or late truck) | ______ (on-time receipts) |
| 3 | Unload | ______ (who unloads, with what truck) | ______ (is staging a location in the system?) | ______ (staging locations; temperature zones) | ______ (where goods wait that the record does not know) | ______ (start of dock-to-stock) |
| 4 | Check and count | ______ (who checks) | ______ (how the receipt is recorded and passed to the ERP) | ______ (item master fields; tolerances) | ______ (damage, count, description, other) | ______ (damage free) |
| 5 | Quality hold | ______ (who may release) | ______ (hold status; who records release) | ______ (which items or suppliers are inspected) | ______ (stock released unchecked, or left on hold) | ______ (the site's own, or none found) |
| 6 | Label | ______ (who labels) | ______ (supplier SSCC read, or own label printed) | ______ (identifier, batch, date) | ______ (missing, unreadable or mixed-content labels) | ______ (correct documents, or the site's own) |
| 7 | Cross-dock or store | ______ (who decides at the dock) | ______ (flow-through function or none) | ______ (outbound demand known when) | ______ (goods with no outbound load ready) | ______ (the site's own, or none found) |
| 8 | Put away | ______ (who drives, which shift) | ______ (directed or chosen by the driver; what is scanned) | ______ (location attributes; dedicated or shared; rotation rule) | ______ (goods put where the record does not say; wrong zone) | ______ (dock-to-stock; lines per hour) |
| 9 | Replenish forward | ______ (who restocks, which hours) | ______ (trigger; task; scans) | ______ (forward location, capacity, trigger) | ______ (forward location empty when picking needs it) | ______ (pick-face stockouts, or the site's own) |

Below the table: the storage media in use and where (______), the share of goods that cross-dock (______, with source), the legal questions about dates and temperatures and the body they were put to (______), and the step where the operation's known trouble starts (______).

### D. Glossary lines

Added to SCE1's working glossary; each term as this unit uses it.

| Term | Working definition | Source |
|---|---|---|
| Stock keeping unit (SKU) | The smallest physical unit of a product an organisation tracks | Bartholdi & Hackman §2.2 [practice] |
| Pallet; unit load | A platform of goods handled as one load by a forklift | Course term; units of handling from Bartholdi & Hackman §2.2 [practice] |
| Case; carton | A supplier's sealed box of a fixed number of units | Course term |
| Each; piece | One saleable unit | Course term; Bartholdi & Hackman §2.2 name individual pieces [practice] |
| Purchase order (PO) | The buyer's order to a supplier, saying what should arrive | Course term |
| Despatch advice; advance ship notice (ASN) | The supplier's message saying what was sent, per logistic unit | GS1 Logistic Label Guideline [independent] |
| Logistic unit | Any combination of trade items packaged together for storage or transport | GS1 SSCC page [independent] |
| Serial Shipping Container Code (SSCC) | The GS1 number that identifies one logistic unit | GS1 SSCC page [independent] |
| Dock door | A loading bay where a trailer backs up to the building | Course term |
| Staging | Setting goods down in a marked area near the dock until the next step | Course term; Bartholdi & Hackman §3.1 [practice] |
| Quality hold | A status that keeps stock in the record but blocks it from orders until released | Working description; not sourced |
| Directed task | A task the system assigns with its location, confirmed by scan | Bartholdi & Hackman §4.2 [practice] |
| Dedicated and shared storage | A location reserved for one product; or a product stored in several locations, each reassignable when empty | Bartholdi & Hackman §2.4 [practice] |
| Honeycombing | Lane space lost to other SKUs while a lane empties | Bartholdi & Hackman §5.1.1 [practice] |
| Selective, double-deep, drive-in, push-back, pallet flow rack | Pallet rack from one pallet deep and fully reachable to deep lanes with fewer aisles | Bartholdi & Hackman §5.1.1 [practice] |
| Shelving; carton flow rack | Static shelves for slow or small items; tilted roller shelves for fast cartons, restocked from the back | Bartholdi & Hackman §5.1.2–5.1.3 [practice] |
| Automated storage and retrieval system (AS/RS) | Machines that store and fetch loads | Bartholdi & Hackman ch. 5 [practice]; SCE5 |
| Reserve; bulk | Where most stock is held in large units | Bartholdi & Hackman §8.1 [practice] |
| Forward pick area; fast-pick area | A convenient area holding small amounts of popular SKUs, replenished from reserve | Bartholdi & Hackman ch. 7, §8.1 [practice] |
| Slotting | Assigning SKUs to locations, including which go forward | Course term |
| Replenishment; restock | Moving stock from reserve to a forward location | Bartholdi & Hackman ch. 7, §8.2 [practice] |
| Task interleaving | Pairing a put-away with a retrieval to cut empty travel | Bartholdi & Hackman ch. 6, §4.3 [practice] |
| Dock-to-stock cycle time | Time from a delivery's arrival to its goods being stored and available | Named by WERC and APQC [practice]; wording the course's |
| FIFO; FEFO | First in, first out; first expired, first out | Bartholdi & Hackman §1.2 [practice] |
| Use by; best before | In EU law as FSAI states it: unsafe after use-by; may be sold after best-before if fully acceptable | FSAI [practice] |
| One-up-one-down | The legal minimum of EU food traceability as FSAI states it: what came in from whom, what went out to whom | FSAI [practice] |

## Sources

All addresses opened on 21 November 2026; the source log (sources.md) gives what was read at each.

- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 1–8 and bibliography. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- APQC. "Dock-to-stock cycle time in hours for supplier deliveries". Open Standards Benchmarking measure page, undated. https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/dock-stock-cycle-time-hours-supplier
- Food Safety Authority of Ireland. "Labelling Requirements and Shelf Life". Undated. https://www.fsai.ie/Business-Advice/Running-a-Food-Business/Food-Safety-and-Hygiene/Shelf-life/Labelling
- Food Safety Authority of Ireland. "Traceability - FAQ". Undated. https://www.fsai.ie/business-advice/starting-a-food-business/traceability/traceability
- GOV.UK. "Food hygiene for businesses: Chilling and freezing". Last updated 25 June 2026. https://www.gov.uk/food-hygiene-businesses/chilling-and-freezing
- GS1. *GS1 Logistic Label Guideline*. Release 1.3, ratified July 2019. https://www.gs1.org/standards/gs1-logistic-label-guideline
- GS1. Serial Shipping Container Code (SSCC) page, no headline shown, undated. https://www.gs1.org/standards/id-keys/sscc
- Staudt, F. H., Alpan, G., Di Mascolo, M. & Rodriguez, C. M. T. (2015). Warehouse performance measurement: a literature review. *International Journal of Production Research* 53(18), 5524–5544. https://doi.org/10.1080/00207543.2015.1030466 (abstract, read at https://informahealthcare.com/doi/abs/10.1080/00207543.2015.1030466)
- USDA Food Safety and Inspection Service. "Food Product Dating". Undated. https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/food-product-dating
- WERC. "WERC DC Measures Survey - 2025". https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf

## Unsure list

# Unsure: SCE2

1. All Bartholdi & Hackman quotations ("the smaller the handling unit, the greater the handling cost"; "Receiving may begin with advance notification of the arrival of goods"; "managing a second inventory, not of product, but of storage locations"; "This loss of space is called honey-combing"; "directed put-away and directed picking"; "warehouse within the warehouse") were taken from a fetch tool's extraction of the 0.98 PDF and not re-read against the PDF itself; page numbers were not reliable in the extraction, so the unit cites sections only.
2. The SKU definition is attributed to §2.2 and the handling-cost sentence to the chapter 3 introduction as the extraction placed them; the section placement should be checked.
3. Equal Time versus Equal Space (§8.3.2, Theorem 8.3): the unit says Equal Time requires the same total restocks as Equal Space; the extraction quoted the theorem only as "Equal Time allocations require the same total restocks". The 1.45 and 2.44 ratios (§8.3.3) are given as "ratios of Equal Time to the optimal allocation"; what quantity the ratio compares was not confirmed.
4. FIFO in pallet storage: the extraction said only drive-through rack (of drive-in and drive-through) supports FIFO, and also that FIFO is discussed for pallet flow rack; the unit claims FIFO only for drive-through and draws no FIFO mark for pallet flow rack.
5. The "two pallets forward" rule is from exercise 7.20 of the textbook, as extracted; it is an exercise's premise.
6. The Staudt et al. (2015) abstract was read at an informahealthcare.com address whose extraction did not show the publisher, authors, journal or DOI; the bibliographic details are the seed's Crossref record.
7. The WERC survey document (2025) lists the five inbound measures under "2024 Level of Performance"; that the 2026 report uses the same names was not checked.
8. GOV.UK page: "updated 22 October 2026" is the page's timestamp as extracted.
9. FSAI pages are undated (footer copyright 2026 only); their statement of Article 24(1) of Reg. (EU) 1169/2011 was not checked against the regulation's text, which could not be read.
10. The GS1 Logistic Label Guideline was read at its landing page; whether the quoted rules (one batch number, one date value per label; Despatch Advice / ASN gives each unit's SSCC) are the guideline's normative text or its summary was not confirmed.

Object: the pallet, as it moves from trailer to storage location (sections 2, 3.3 to 3.8 and 4)

Fresh check 2026-11-21 (Opus 5.5): fix · 1 errors, 10 should-fix, 16 minor; report `audits/supply-chain-execution/fresh-check-SCE2.md`
