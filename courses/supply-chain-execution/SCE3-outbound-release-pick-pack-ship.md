---
code: SCE3
title: "Outbound: release, pick, pack, ship"
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-24
search: off
intro: SCE3 follows an order from release to the trailer door. It sets out the order profile (lines per order, units per line, the spread of picks across items) and why it decides the rest; order release in waves and continuously; the picking methods one by one (one order at a time, batch, to a cart, zone and pass-along, to a conveyor and sorter, put systems, goods brought to the picker), each with what it suits and what it costs; routing; sorting and consolidation; packing, checking, staging and loading; cut-off times; where a picker's time goes, with the common claims C1 and C2 traced to the oldest source this unit could open and their ages stated; how outbound fails; what the warehouse system does at each step; and the outbound measures WERC's survey names, with the definitions that could be opened. Its deliverable is a picking-method decision table, worked for Corvane's (fictional) store and web orders and Ostrel's (fictional) case picking, two outbound flow maps in SCE2's six-column form, the templates for both, and glossary lines. Written 24 Nov 2026 by Opus 5.5 with search off (references still opened live, all on 24 Nov 2026), then given a fresh check and a quality review by separate Opus 5.5 agents (both keep), their findings applied. Known gaps: most of the unit rests on one textbook (Bartholdi and Hackman, release 0.98) and one literature review (de Koster, Le-Duc and Roodbergen, 2007), both read through a fetch tool's extraction and not re-read against the PDF, with sections cited for want of page numbers, so most claims are graded practice. Five works were read in abstract only, and every claim taken from them rests on the abstract alone: Boysen, de Koster and Weidinger (2019) on e-commerce orders and goods-to-picker systems; Gallien and Weber (2010) on wave and waveless release with a sorter (its volume and pages confirmed at a university repository, not on Crossref); Batt and Gallino (2019) on search time; Kim (2020) on cut-off times (the unit's other claims on cut-off peaks, pick-ups across the day and packing come from the 2018 report version, read in full, and whether the journal text keeps them was not checked); and Çeven's dissertation (2013) on waves and missed orders. The abstract of seed W3 (Rouwenhorst et al., 2000) was also opened and changes nothing in SCE2 (flag F22). Not opened: the origins of the 50% and 55% figures (Tompkins et al. 1996 and 2003, Frazelle 1996, Gross 1981, Drury 1988), known only as later works cite them; seed W2 (Gu, Goetschalckx and McGinnis, 2007), whose DOI redirected, left to SCE4 (flag F22); Gu, Goetschalckx and McGinnis (2010), DOI from a search only; Çeven and Gue (2017), seen as a record only; the reference behind Bartholdi and Hackman's bucket-brigade figure; WERC's 2026 report, which is paid; WERC's own definitions of its outbound measures, which sit in an online tool that was not found, so most definitions are the course's own and two rest on a vendor's white paper (Hyster-Yale, 2026, vendor-reported); and the GOV.UK chilling page whose date SCE2 gives two ways. No source was opened on carrier cut-off practice beyond one European field study, on packing-station checks beyond the textbook, on a definition of cluster picking, on the cost of goods-to-picker equipment, or on the regional terms for part loads and parcel carriers.
---

# SCE3 · Outbound: release, pick, pack, ship

Grades follow SCE1's key: every claim that carries a number, a mechanism or a recommendation ends with [independent], [analyst], [vendor-reported] or [practice]. Two sources carry most of this unit, both accounts of practice rather than measurements: Bartholdi and Hackman's textbook *Warehouse & Distribution Science* (release 0.98, revised 28 August 2017; "B&H", cited by chapter and section) and de Koster, Le-Duc and Roodbergen's review of order-picking research ([2007](https://doi.org/10.1016/j.ejor.2006.07.009); "de Koster et al.", cited by section). A number a review repeats from a study this unit did not open is graded practice, with its origin named. Lines marked as this unit's inference carry no grade.

## 1. The order profile

**What it is.** An **order** is one customer's request; an **order line** (also pick line) is one item on it, with a quantity, the **units per line**. The **order profile** is how lines per order, units per line and picks across items are distributed over a period's orders. B&H call measuring it **activity profiling**, a necessary first step to almost any significant warehouse project, because customer orders drive the system (ch. 14 opening) [practice].

**Why lines count for more than units.** B&H treat pick lines as a strong indicator of work: each line sends someone to a location, then through picking, checking, packing and shipping (§14.2.2) [practice]. A line of one unit and one of twelve cost nearly the same walk (this unit's inference).

**Three views of the profile** (B&H ch. 14), each a question for an operation's order history:

- **How picks spread across items.** ABC analysis sorts items (**SKUs**, as SCE2 defines them) into a small fraction with most activity (A), a middle group (B) and the bulk with little (C) (§14.2.1) [practice]. B&H report the rule of thumb "Twenty percent of the skus account for 80 percent of the activity", with no measurement across warehouses; in their worked example the 5,000 busiest SKUs take over 75% of picks, their argument for a fast-pick area (§14.2.2, Figure 14.1) [practice].
- **How many lines each order carries.** B&H recommend the complete distribution of lines per order, not its average (§14.2.2) [practice]. In their example (Figure 14.4), about two-thirds of orders are single-line yet take only about one-third of picks [practice]: one unnamed warehouse, predicting nothing about another.
- **Which orders make the work.** The share of picks by order size (§14.2.2) [practice]; B&H's Question 14.3 asks "What size order accounts for most of the picking in the warehouse?"

**Why the profile decides the rest.** When orders are small, travel can be cut by picking several in one tour (de Koster §6) [practice]; how much routing matters depends on order size (B&H §10.3.2) [practice]. So the profile picks the method, the method sets the release rule and the sorting, and the sorting sets packing and staging space (this unit's inference, from sections 2 to 7).

**What e-commerce changed.** Boysen, de Koster and Weidinger's survey says e-commerce retailers must assemble many time-critical orders of a few lines and low quantities, to which traditional picker-to-parts warehouses are often ill-suited ([2019, abstract read](https://doi.org/10.1016/j.ejor.2018.08.023)) [practice].

Corvane (fictional), a fashion retailer, ships web orders of one to three items and replenishes 60 stores by carton and single item; Ostrel Foods (fictional), a food distributor, picks cases onto roll cages for about 600 delivery points a day (case register). Neither register entry gives a lines-per-order distribution.

## 2. Order release: waves and continuous

**The physical event.** None at first: release is the moment orders in the system become floor work, as pick lists, handheld tasks or lights on a rack (SCE1 §2, step 4). In B&H's account the warehouse management system (WMS) turns customer orders into pick lists organised for easy retrieval, tracks each order's assembly (ch. 4 introduction) [practice] and coordinates it "to meet shipping schedules" (ch. 4) [practice].

**Waves.** De Koster et al. use **wave picking** when orders for a common destination are released together for picking in several areas of the warehouse, usually combined with batch picking (§2.2) [practice]. Çeven's dissertation defines a wave as a large group of orders picked and packed together, sorted for individual customers, and shipped, and says that when the number and timing of waves are not planned systematically, missed orders and upset customers result ([Çeven, Auburn University, 2013, abstract read](https://etd.auburn.edu/handle/10415/3716)) [practice]. B&H list wave management among a WMS's high-end features (§4.3) [practice], without describing it.

**Continuous (waveless) release.** Orders are released one by one, or in small groups, as capacity frees. Gallien and Weber studied the choice with an automated sorter, on detailed flow data from a large US online retailer ([2010, abstract read at the publisher](https://doi.org/10.1287/msom.1100.0291)) [independent]. Their abstract says wave release is prevalent where there is an automated sorter; that continuous release presents several advantages but needs more expensive technology and carries the possibility of congestion-induced collapse (gridlock) at the sorter [practice] (the abstract's framing, not a finding of the study). In their simulations, the best waveless policy gave larger or equal throughput than the best wave-based policy in every scenario considered [independent]. One retailer's data, with a sorter, in simulation: this unit does not apply it to a building without one.

**People.** At Corvane (fictional), Tobias, the outbound shift supervisor, answers for release (case register, added by SCE1). Who releases at Ostrel (fictional) is not in the register.

**Common failure.** Releasing an order whose stock is not at the **pick face** (the forward location a picker takes from; course term), so the picker finds it empty or short; releasing too much at once, so aisles and the sorter congest (section 10).

```viz
{"kind": "flow", "title": "Outbound, from release to departure", "per_row": 4, "steps": [{"label": "Release", "note": "orders become pick lists or tasks"}, {"label": "Pick", "note": "by the method the profile suits"}, {"label": "Sort and consolidate", "note": "where batching or zoning split orders", "tone": 3}, {"label": "Check and pack", "note": "order complete and accurate"}, {"label": "Label", "note": "carrier label; SSCC on a logistic unit"}, {"label": "Stage", "note": "if loaded in reverse delivery order"}, {"label": "Load", "note": "onto the vehicle, in stop order where staged"}, {"label": "Ship", "note": "trailer scanned at departure", "tone": 2}], "caption": "The outbound steps of sections 2 to 7 of this unit, in order. Step names are this course's; the notes come from de Koster, Le-Duc and Roodbergen (2007), sections 2.2 and 5, and Bartholdi and Hackman, Warehouse & Distribution Science, release 0.98 (2017), chapter 4 introduction and sections 3.4 and 3.5, as cited in those sections; the SSCC note is from GS1's Logistic Label Guideline as SCE2 section 3.6 sets it out (section 6 of this unit)."}
```

## 3. The picking methods, one by one

**Order picking** is taking the ordered goods from their storage locations (SCE1 glossary). De Koster et al. sort the systems first by who moves: in **picker-to-parts** systems the picker travels to the goods, and in **parts-to-picker** systems the goods are brought to the picker (§2.2) [practice]. Picker-to-parts is, on the authors' own experience, "over 80% of all order-picking systems in Western Europe" (§2.2) [practice]: an estimate for one region, with no survey behind it.

Then they sort by how orders are grouped:

### 3.1 One order at a time (discrete picking)

**What it is.** One picker picks one order in one tour. De Koster et al. note it is also called single-order picking, discrete picking or pick-by-order (§6) [practice].

**What it suits.** Orders large enough to fill a tour alone; each tote holds one order, so no sorting follows (this unit's inference from de Koster §6, §2.2).

**What it costs.** Travel per line is high when orders are small, because every tour covers the building for a few lines (de Koster §6) [practice].

### 3.2 Batch picking

**What it is.** One picker picks several orders in one tour, by article. De Koster et al. define **order batching** as grouping orders into sub-sets, each retrieved in one picking tour, formed by **proximity** of pick locations or by **time windows** (orders arriving in the same interval) (§6; the criteria after Choe and Sharp, 1991) [practice]. Batching raises **pick density** (picks per unit of distance travelled), which cuts travel per pick (B&H ch. 5 introduction) [practice].

**What it suits.** Small orders: "when orders are small", picking several in one tour can reduce travel (de Koster §6) [practice].

**What it costs.** The batch must be split back into orders, either on the cart while picking (sort-while-pick) or after picking has finished (pick-and-sort) (de Koster §2.2) [practice]. Good batches need computing: order batching is NP-hard, so most studies develop heuristics (de Koster §6) [practice], while time-window batching needs little analysis (Choe and Sharp, 1991, below) [practice]. De Koster et al. give no single figure for the saving, and report that even simple batching methods improve markedly on first-come first-served (§6, after De Koster et al., 1999) [practice].

### 3.3 To a cart: sorting while picking

**What it is.** The picker pushes a cart with one tote per order and puts each item straight into its order's tote: de Koster et al.'s **sort-while-pick**, sorting on the pick cart as the picker goes (§2.2) [practice]. You will also hear "cluster picking" for it; this unit opened no source that defines that term.

**What it suits.** Small orders, batched, in a building with no sorter (this unit's inference: it is batch picking whose sorting needs only a cart).

**What it costs.** Sorting time at the shelf, and a cart's limit on how many orders a batch can hold (this unit's inference; no source opened measures either).

### 3.4 Zone picking and pass-along

**What it is.** The storage area is split into zones, each worked by its own pickers (de Koster §2.2) [practice]. An order that needs several zones is completed in one of two ways (de Koster §5) [practice]:

- **Progressive** (pass-along, **pick-and-pass**): the order travels zone to zone in a tote with its pick list until complete.
- **Parallel** (synchronised): every zone picks its part of the order at once, and the parts are merged afterwards.

**What it suits.** A large pick area or many pickers: each picker covers a smaller area, congestion falls, and pickers learn their zone's locations (de Koster §5) [practice]. Choe and Sharp's 1991 tutorial describes, as one option, progressive zoning for orders visiting few zones and synchronised zoning for large ones ([Choe and Sharp, Georgia Tech, 1991](https://www2.isye.gatech.edu/~mgoetsch/cali/Logistics%20Tutorial/order/article.htm)) [practice]. With pass-along, orders emerge in the sequence they were released (B&H §3.3) [practice].

**What it costs.** The main disadvantage, for de Koster et al.: orders are split and must be consolidated again before shipment (§5) [practice]. Pass-along zone-picking "requires all the work of balancing an assembly line" (B&H §3.3) [practice], and imbalance between zones hurts throughput (de Koster §5) [practice]. Synchronised zoning needs an accumulation or sortation step, and pickers may wait for one another (Choe and Sharp, 1991) [practice].

**A self-balancing variant.** In a **bucket brigade**, each picker carries work forward until someone takes it over, then goes back for more (B&H §11.1) [practice]; it balances itself (de Koster §5) [practice]. B&H report two sites: a major chain retailer's national distribution centre, where picks per person-hour rose over 30% with no change to layout or equipment, and a US recorded-music distributor, where the average pick rate rose 20% and its variance fell 90% (§11.2) [practice]. Each is one site, from work this unit did not open.

### 3.5 To a conveyor and a sorter (pick-and-sort)

**What it is.** Pickers pick batches by article onto a conveyor, and a **sorter** downstream separates the items into orders: de Koster et al.'s **pick-and-sort**, sorting after picking is finished (§2.2) [practice]. In their sorter, a wave's items arrive in random sequence, circulate, and drop into the shipping lane assigned to their order (§8) [practice].

**What it suits.** Many small orders at high volume: a sortation system lets pick lists be built purely for efficiency (B&H §5.2.1) [practice], and conveyors partition the warehouse into zones (§5.2) [practice].

**What it costs.** The equipment and its capacity: throughput depends on sorter capacity and conveyor speed, and with fewer lanes than orders, lane assignment matters and can block (de Koster §8) [practice]. Continuous release into a sorter needs more expensive technology than waves, in Gallien and Weber's framing (abstract) [practice], and risks gridlock, which their model sets release rules to hold below a chosen threshold (abstract) [independent]. This unit opened no source on what a sorter costs.

### 3.6 Put systems

**What it is.** Goods are first retrieved by article, then a picker distributes them over the customer orders (de Koster §2.2) [practice]. A **put wall**, a rack of slots one per order, is a course term; no source opened defines it.

**What it suits.** Many order lines to be picked in a short window (de Koster §2.2) [practice]. Store replenishment, one item to many stores at once, has this shape (this unit's inference).

**What it costs.** Two handlings of every unit, the retrieval and the put (this unit's inference from the definition).

### 3.7 Goods brought to the picker

**What it is.** Parts-to-picker: a machine brings the storage unit to a pick position where the picker takes what is needed; de Koster et al. name automated storage and retrieval systems (AS/RS), miniloads, vertical lift modules and carousels (§2.2) [practice]. Boysen et al.'s survey names automated picking workstations, robots and AGV-assisted picking (AGV: automated guided vehicle) among the systems suited to e-commerce (2019, abstract) [practice]. SCE5 treats the machines.

**What it suits.** Many small, time-critical orders (section 1; Boysen et al., abstract) [practice].

**What it costs.** No source opened gives a cost.

### 3.8 The methods as a decision

As a decision (table A of the deliverable gives the detail):

```viz
{"kind": "decision", "title": "Which picking method the order profile points to", "root": {"q": "One item going to many orders in a short window?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "Put system", "tone": 3}}, {"label": "no", "to": {"q": "Most orders small (few lines)?", "tone": 4, "branches": [{"label": "yes", "to": {"q": "Sorter downstream?", "tone": 3, "branches": [{"label": "yes", "to": {"outcome": "Batch, sort downstream (pick-and-sort)", "tone": 2}}, {"label": "no", "to": {"outcome": "Batch to a cart, sort while picking", "tone": 2}}]}}, {"label": "no", "to": {"q": "Area too large or busy for one picker per order?", "tone": 3, "branches": [{"label": "yes", "to": {"outcome": "Zone picking, then consolidate", "tone": 5}}, {"label": "no", "to": {"outcome": "One order at a time", "tone": 1}}]}}]}}]}, "caption": "The choices of section 3 of this unit as a decision. Each branch is a 'suits' line of sections 3.1 to 3.6 (the first question is this unit's inference from de Koster's 'many order lines in a short window', section 3.6), from de Koster, Le-Duc and Roodbergen (2007), sections 2.2, 5 and 6, and Bartholdi and Hackman (2017), section 5.2.1; the order of the questions is this unit's own. It leaves out goods-to-picker systems, whose choice turns on equipment this unit did not cost."}
```

## 4. Routing a picker through the building

**The physical event.** The picker walks or drives from location to location. **Routing** is the order of those locations and the path between them.

**The methods.** De Koster et al. describe the routes studied for a rectangular warehouse of parallel aisles (§7) [practice]:

- **S-shape** (traversal): every aisle with a pick is walked end to end.
- **Return**: each aisle with picks is entered and left from the same end.
- **Midpoint**: front-half picks are reached from the front cross aisle, back-half picks from the back.
- **Largest gap**: like midpoint, but into an aisle as far as the largest gap between picks.
- **Combined**: each aisle walked through or entered from one end, chosen aisle by aisle.
- **Optimal**: Ratliff and Rosenthal (1983) find the shortest route in a single-block rectangular warehouse in time linear in the number of aisles.

**How far heuristics fall short.** De Koster et al. report from earlier studies that the best heuristic averages 5% over optimal (Petersen, 1997; §7.1) and that S-shape routes ran 7% to 33% longer than optimal in simulations of single-block warehouses with random storage (§7.3, from 1998 studies by De Koster and co-authors) [practice]; this unit opened neither study.

**Why practice uses heuristics.** De Koster et al. give three reasons: no optimal algorithm exists for every layout; optimal routes can look illogical to pickers, who deviate from them; and a standard optimal algorithm cannot take aisle congestion into account, where a heuristic can (§7.1) [practice]. S-shape gives each aisle one direction of traffic when pick density is high enough (§7.1) [practice], like B&H's serpentine path (§10.2.1) [practice].

**What the software does.** The WMS typically gives the picker the sequence of locations, not the path (B&H §10.1) [practice], most simply by sorting pick lines by location (ch. 10) [practice]; pick-path optimisation needs shortest distances between locations, which most systems do not keep (§10.1, §10.3) [practice].

**When routing matters.** Little when all orders are of one to three items, "such as at a catalog fulfillment center", more where items are many and mostly slow and orders moderate (B&H §10.3.2) [practice]; batching lowers its value (§10.3.2) [practice].

## 5. Sorting and consolidating after the pick

**The physical event.** Items picked in batches or zones are brought back together by order or destination: SCE1's **sortation**, de Koster et al.'s order accumulation and sorting (§2.3) [practice].

**Where it happens.** On the cart (section 3.3), at a put wall (3.6), in a sorter (3.5), or at a consolidation area where the zones' parts of an order meet (3.4). Sortation equipment is typically integrated with a conveyor, downstream of picking (B&H §5.2.1) [practice].

**Why it is a step to design.** Customers want everything they ordered in as few packages as possible, so an order's pieces must be assembled (B&H §3.3) [practice] and reach packing together (§3.4) [practice]. In a sorter, lanes are released as trucks need them, and assigning orders to lanes late, just before items reach the sorter, did better than fixed assignment in the work de Koster et al. review (§8) [practice].

**What the software does.** Tracks which parts of each order have arrived, and holds the order-to-lane or order-to-slot assignment (this unit's inference from de Koster §8 and B&H ch. 4).

**Common failure.** One part of an order is late (a short pick in one zone, a tote sent to the wrong lane), and the rest waits in consolidation, taking a slot (this unit's inference).

## 6. Packing, labelling and checking

**The physical event.** The order's items are counted or scanned, put into a carton, bag or onto a pallet or roll cage, sealed and labelled.

**What the sources say.** B&H: packing is a convenient time to check that the customer order is complete and accurate (§3.4) [practice], and packed product may be scanned to register the order ready to ship (§3.4) [practice]. A label on a logistic unit carries its Serial Shipping Container Code (SSCC), as SCE2 §3.6 sets out from GS1's guideline; the same rules apply to an outbound pallet or carton (this unit's inference). Kim's report on a consumer-electronics manufacturer's European distribution centre states that in original equipment manufacturers' (OEM) warehouses packing is often the most demanding stage ([Kim, Econometric Institute Report EI2018-02](https://repub.eur.nl/pub/112492)) [practice].

**People.** Packers at a station; at Corvane (fictional), Tobias answers for pack and ship (register, added by SCE1).

**What the software does.** Shows the order's contents, takes the scans, prints the carrier label and any document, and records the unit packed (this unit's inference from B&H §3.4). Corvane books carriers through each carrier's portal (case register), so its packing station needs a link to each or a re-keyed label (this unit's reading of the register).

**Common failure.** A wrong item, or a wrong quantity, caught here or not at all; a missing item that leaves an order waiting (section 5).

## 7. Staging and loading

**The physical event.** Packed units are set down in lanes by the dock, then loaded onto the vehicle.

**What the sources say.** B&H: shipping generally handles larger units than picking, because packing has consolidated items (§3.5) [practice]; product is likely to be staged if it must be loaded in reverse order of delivery, last stop first (§3.5) [practice]; and the trailer is likely to be scanned to register its departure (§3.5) [practice]. "The shipping dock will be congested even if work flows smoothly", and downstream processes need the greater capacity to avoid bottlenecks (§16.3) [practice].

**People.** Loaders; at Ostrel (fictional), Sofia, the transport planner, builds the next day's routes, which set the loading sequence (case register); who loads is not in the register.

**What the software does.** Records each unit's staging lane and its scan onto the right vehicle, records departure and registers the shipment out, one of a WMS's fundamental records (B&H §4.1) [practice]. Documents differ by region: SCE1 §2 sets out the CMR consignment note for international road carriage and the US bill of lading; SCE7 takes them further.

**Common failure.** A unit loaded on the wrong vehicle or in the wrong sequence, so the driver handles goods twice at a stop (B&H §17.2.3, on practice in Singapore, Hong Kong and Japan: trailers "must be loaded in reverse sequence of delivery to avoid double-handling"; the general staging rule is B&H §3.5) [practice].

## 8. Cut-off times and the shape of the shift

**The terms** (the course's working definitions). An **order cut-off** is the latest time an order is accepted for a given dispatch; a **carrier departure** (or pick-up), the time a vehicle leaves the dock.

**What the sources say.** Kim's field study states that warehouses employ order cut-off times to ensure sufficient time for fulfilment ([Kim, *Computers & Industrial Engineering* 139, 2020, abstract read](https://repository.mdx.ac.uk/item/8891y)) [practice]. Its report version adds that warehouses try to postpone the cut-off to improve responsiveness, that "Such cut-off rules induce order peaks just before the cut-off time" and imbalanced workloads, and that the manufacturer's warehouse it studied dispatches retailer orders by truck at agreed pick-up times on the next working day, spread across the day (EI2018-02) [practice]. Its simulation of one European site found that a critical-ratio rule (ranking jobs by time left before they are due over work still needed; course's working definition) using the real-time job queue gave the fastest flow time (arrival to completion) of the priority rules tested (journal abstract) [independent]. De Koster et al. describe the general pressure: late orders accepted with rapid delivery promised, so picking time shrinks (§1) [practice].

**How the cut-off shapes the shift** (this unit's inference from the sources above and SCE2 §6):

- Work arrives late and in a peak (Kim) while departures stay fixed, so the hours between cut-off and departure set how much can be picked, packed and loaded.
- Work that can leave those hours does: replenishment ahead of release (SCE2 §6), and picking orders that arrived earlier.
- Waves are timed backwards from departures: the last wave for a vehicle must finish sorting and loading before it leaves (this unit's inference; Çeven's abstract sets wave timing and number against deadlines, not departures).

At Corvane (fictional), the register gives no cut-off or carrier pick-up times; peak brings about four times a normal week's web volume (case register), so the week's web work is about four times a normal week's; how it falls across departures is not in the register (this unit's reading).

**Common failure.** A **missed cut-off**: the vehicle leaves without an order, which then waits for the next departure.

## 9. Where a picker's time goes

The research reviews say less than the numbers that circulate.

**The reviews.** De Koster et al. (2007, now 19 years old) write that, though other activities may contribute substantially, travel is often the dominant component of picking time (§2.3) [practice], with a chart from Tompkins et al.'s textbook *Facilities Planning* (2003, now 23 years old) whose percentages could not be read (§2.3, Fig. 4) [practice]. B&H (2017, nine years old) tabulate, from Frazelle's *World-Class Warehousing* (1996, 30 years old): travelling 55%, searching 15%, extracting 10%, paperwork and other activities 20% of order-picking time (§3.3) [practice], and call travel "the largest component of labor in a typical distribution center" (ch. 10) [practice].

```viz
{"kind": "compare", "title": "A picker's time, as one textbook tabulates it", "unit": "%", "max": 60, "rows": [{"label": "Travelling", "value": 55, "tone": 4}, {"label": "Searching", "value": 15}, {"label": "Extracting", "value": 10}, {"label": "Paperwork and other activities", "value": 20}], "caption": "Shares of order-picking time as tabulated in Bartholdi and Hackman, Warehouse & Distribution Science, release 0.98 (2017), section 3.3, credited there to Frazelle, World-Class Warehousing (1996), which this unit did not open. Section 9 of this unit; graded practice: a textbook figure with no measurement described in the text read."}
```

**A measured study on one component.** Batt and Gallino studied pick workers in online and multichannel retail fulfilment with "chaotic storage", where dissimilar items share one location: pick times rose by as much as 16% as search got harder, the effect fell with experience, and in simulation, assignment and routing using distance, bin density and picker experience could raise productivity by about 5% ([2019, abstract read at the publisher](https://doi.org/10.1287/mnsc.2018.3059)) [independent]. The abstract states no sample and no share of time for search.

**When travel is small.** In a dense pick area travel is small and most non-value-adding work is local search (B&H ch. 11) [practice], so travel's share depends on layout, profile and method (this unit's inference).

### The common claims C1 and C2, traced

C1 and C2 are each traced to the oldest source this unit could open; the origins those sources name were not opened, so every figure below is practice by origin.

**C1: "Travel is about half of an order picker's time."**

| Source opened | Its age (24 Nov 2026) | What it says | Credits it to |
|---|---|---|---|
| Choe and Sharp, *Small Parts Order Picking: Design and Operation*, Georgia Tech, 1991 | 35 years | Travel time is a major portion of total process time; no percentage | No source |
| Dekker et al., *Quick Response Practices at the Warehouse of Ankor*, ERIM report, 2002 ([report](https://repub.eur.nl/pub/168/erimrs20020222120221.pdf)) | 24 years | "It is generally assumed that" travel between locations takes about 50% of the total time spent picking orders | Tompkins et al., 1996 (not opened; 30 years) |
| de Koster et al., 2007 | 19 years | Travel is often the dominant component; chart from Tompkins et al. (2003) | Tompkins et al., 2003 (not opened; 23 years) |
| B&H, release 0.98, 2017 | 9 years | Travelling 55% of order-picking time | Frazelle, 1996 (not opened; 30 years) |

What the evidence shows: in the sources opened, "about half" goes back to two 1996 textbooks, Tompkins et al.'s and Frazelle's, cited by later works; neither was opened, and no opened work describes a measurement behind it. Graded practice. No independent source found measures travel's share across warehouses; Batt and Gallino measure search.

**C2: "Order picking is more than half of a warehouse's operating cost."**

| Source opened | Its age | What it says | Credits it to |
|---|---|---|---|
| Choe and Sharp, 1991 | 35 years | 30% to 40% of labour cost can be associated with picking, depending on the warehouse type | Gross, 1981 (not opened; 45 years) |
| ERIM Material Handling Forum, "Order picking", undated ([page](https://erim.eur.nl/material-handling-forum/research-education/tools/calc-order-picking-time/order-picking)) | undated | Picking may consume as much as 60% of all labour activities in the warehouse | Drury, 1988 (not opened; 38 years) |
| Dekker et al., 2002 | 24 years | Picking amounts to about 55% of a warehouse's operational costs | Tompkins et al., 1996 (not opened; 30 years) |
| de Koster et al., 2007 | 19 years | "as much as 55% of the total warehouse operating expense" (abstract) | No source in the abstract |
| B&H, release 0.98, 2017 | 9 years | "Order-picking typically accounts for about 55% of warehouse operating costs" (§3.3) | Frazelle, 1996 (not opened; 30 years) |

What the evidence shows: the versions disagree on what is divided (labour cost, labour activities, operating cost) and on the number; the circulating "more than half" drops "as much as" and "typically" and mixes labour with total cost. All are practice by origin; no independent source found. The defensible statement: picking is cited as a large share of warehouse labour and cost in textbooks since at least 1981, with figures that depend on the warehouse (this unit's inference).

```viz
{"kind": "timeline", "title": "The picking-share figures and when their origins were written", "start": 1978, "end": 2026, "ticks": [1980, 1990, 2000, 2010, 2020], "events": [{"at": 1981, "label": "Gross: 30-40% of labour cost (as cited)"}, {"at": 1988, "label": "Drury: up to 60% of labour (as cited)"}, {"at": 1991, "label": "Choe and Sharp cite Gross"}, {"at": 1996, "label": "Tompkins et al.; Frazelle: 55%, travel 50-55% (as cited)"}, {"at": 2002, "label": "Dekker et al. cite Tompkins 1996"}, {"at": 2007, "label": "de Koster et al.: as much as 55%"}, {"at": 2017, "label": "Bartholdi and Hackman cite Frazelle"}], "caption": "The dates of the sources traced for claims C1 and C2 in section 9 of this unit: the works opened (Choe and Sharp 1991; Dekker et al. 2002; de Koster et al. 2007; Bartholdi and Hackman 2017; the ERIM page, undated, for Drury) and the origins they credit (Gross 1981, Drury 1988, Tompkins et al. 1996, Frazelle 1996), which were not opened. 'As cited' marks a figure known only through a later work."}
```

## 10. How outbound commonly fails

No source opened measures how often these happen.

**Short picks.** A **short pick** finds less at the location than the line asks for: the record shows stock the shelf lacks, or the pick face holds less than the line. A pick quantity larger than the forward area holds triggers a restock (B&H §8.2) [practice], and forward stockouts can disrupt picking, which is why safety stock is carried there (§8.5.2) [practice]. The order then waits in consolidation (section 5) or ships incomplete. Corvane's (fictional) known trouble, web orders promised from stock the centre cannot find (case register), shows here as a short pick (SCE1 deliverable A, this unit's reading); where the stock went is SCE4's subject.

**Replenishment arriving late.** Restocks can be made during picking or on another shift, when timing is less critical (B&H §8.2) [practice]. If the restock comes after the picker, the pick is short, or the picker waits. At Ostrel (fictional) restocking is Bram's night work, shared with put-away (deliverable C).

**Congestion.** Pickers in one aisle block each other. B&H's simplest congestion model estimates the probability of several pickers in one aisle (§7.4.2) [practice], and they warn against concentrating popular items too much (ch. 9) [practice]. Zoning, S-shape routing and a release limit act on it (sections 3.4, 4 and 2).

**Missed cut-offs.** Orders arriving in the pre-cut-off peak (Kim, EI2018-02) [practice] meet a fixed departure; if picking, sorting or packing cannot finish, the order misses the vehicle (section 8). When the number and timing of waves are not planned systematically, missed orders result (Çeven, abstract) [practice].

**Errors.** A wrong item or quantity is caught at packing, if the check is made (B&H §3.4) [practice], or at the customer. SCE4 traces what one error costs downstream.

## 11. What the warehouse system does at each step

Each of sections 2 to 7 says what the system does; deliverables C and E list the data it needs.

**The case register's fictional vendors.** Four modules of Halvern Warehouse and Kestrow WMS (both fictional) sit on outbound steps: Automation Connect at the sorter (section 3.5), Voice at picking (3), Yard at the dock (7), Parcel Shipping at packing and labelling (6). Case-register facts, graded nothing, they say nothing about real products; map a real product the same way, from its public pages, grading each line vendor-reported.

## 12. The outbound measures the benchmark surveys report

**WERC** (the Warehousing Education and Research Council) asks in its 2025 DC Measures survey for 2024 performance on a list of measures ([WERC DC Measures Survey - 2025](https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf)) [practice]. The table gives, by WERC's names, the sixteen this unit counts as outbound (the grouping is this unit's). The document gives no definitions (they sit in an online tool this unit could not find), no sample and no values, so the grade is practice, as in SCE2 §8. WERC's 2026 report, with values, is paid and was not opened: **no WERC value is given here**.

**Definitions that could be opened.**

- **APQC**, a benchmarking organisation, defines **order line fill rate** and **order fill rate** (lines, or orders, filled completely as a percentage of all; [APQC, "Order line fill rate"](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/order-line-fill-rate); [APQC, "Order fill rate"](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/order-fill-rate)) [practice], and **perfect order performance** as the product of the percentages of on-time delivery, complete orders, damage-free delivery and accurate documentation, times 100 ([APQC, "Perfect order performance"](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/perfect-order-performance)) [practice]. The pages are undated and give no data period, so no APQC value is given.
- A 2026 white paper by Hyster-Yale Materials Handling, Inc., presenting WERC's 2026 findings, defines On-Time Shipments as the percent of orders shipped at the planned time, off the dock and in transit to the final destination, and Order Picking Accuracy as the accuracy of the picking process, where errors can be caught and corrected before shipment ([Hyster-Yale, "Benchmarking and Improving Distribution Center Metrics", 2026](https://www.yale.com/4a4034/globalassets/coms/yale/north-america/documents/white-papers/yal-1558_werc2026updates_improvingdcmetricswhitepaper.pdf)) [vendor-reported]. It states no sample.

**B&H's warning about one of them.** "Pick-lines per labor hour", a popular indicator, is biased in their account ("One would expect a higher score if picking cartons instead of pieces") and not focused on the customer; order-cycle time seems more defensible to them (§15.1) [practice]. So Ostrel's cases and Corvane's eaches (both fictional) cannot be compared on lines per hour (this unit's inference).

| Measure (WERC's name) | Definition used in this course | Whose definition |
|---|---|---|
| On Time Shipments | Orders shipped at the planned time, over all orders shipped | Hyster-Yale white paper (2026) [vendor-reported]; wording the course's |
| Total Order Cycle Time, in Hours | Average time from the customer placing the order to its delivery | Course's |
| Internal Order Cycle Time, in Hours | Average time from release (or receipt of the order in the warehouse) to shipment | Course's |
| Backorders as a Percentage of Total Lines | Lines not shipped for lack of stock, over all lines ordered | Course's |
| Fill Rate - Line | Lines filled completely, over all lines | APQC [practice] |
| Fill Rate - Order | Orders filled completely, over all orders | APQC [practice] |
| Lines Picked and Shipped per Person Hour | Lines picked and shipped, over labour hours spent on them | Course's working definition (B&H's bias applies) |
| Orders Picked and Shipped per Person Hour | Orders picked and shipped, over labour hours spent on them | Course's |
| On-Time Ready to Ship | Orders packed and staged by their planned time, over all orders | Course's |
| Order Picking Accuracy | Orders (or lines) picked with no error, over all picked | Hyster-Yale white paper (2026) describes it [vendor-reported]; formula the course's |
| Perfect Order Index | On time × complete × damage free × correct documents | APQC's formula [practice] |
| Percent of Orders with On Time Delivery | Orders delivered by the promised date, over all orders | Course's |
| Shipped Complete per Customer Order | Orders shipped with every line complete, over all orders | Course's |
| Shipped Damage Free (outbound) | Orders arriving with no damage recorded, over all orders | Course's |
| Correct Documentation (ASN,Invoice, etc.) | Orders whose documents matched what was shipped, over all orders | Course's |
| Distribution Cost per Unit Shipped | Distribution cost over units shipped | Course's |

## On a site visit

Look for, and ask:

- **What does an order look like here?** The distribution of lines per order and the share of picks from single-line orders, not the average (section 1).
- **When do orders drop to the floor, and who decides?** Waves or continuous; how waves are sized and timed (section 2).
- **Watch one picker for a full tour.** Count walking, searching and time at the shelf; does the handheld give a sequence or a path (sections 4 and 9)?
- **Where do split orders meet again, and what waits there now?** (Section 5.)
- **What is checked at packing, and what happens to an error found there?** (Section 6.)
- **What are the cut-off and departure times, and which order missed its vehicle last week?** How is the shift planned back from departures (section 8)?
- **When are pick faces restocked, and do pickers wait for it?** (Section 10, SCE2 §6.)
- **Which of WERC's outbound measures does the site track, with whose definition, from which timestamps?** (Section 12; deliverable C.)

## Self-check

1. **Why do B&H measure work in pick lines rather than units?**
   Each line sends someone to a location and through picking, checking, packing and shipping (section 1).
2. **What is the main disadvantage of zone picking, in de Koster et al.'s review?**
   Orders are split and must be consolidated again before shipment (section 3.4).
3. **What did Gallien and Weber find about waveless release, and in what setting?**
   With an automated sorter and one large US online retailer's data, the best waveless policy matched or beat the best wave policy on throughput in every simulated scenario (section 2).
4. **Why do warehouses use heuristic routes rather than optimal ones, according to de Koster et al.?**
   No optimal algorithm exists for every layout; optimal routes can look illogical to pickers; standard optimal algorithms ignore aisle congestion (section 4).
5. **A colleague says travel is half of a picker's time. What do the sources opened here say?**
   It traces to two 1996 textbooks (Tompkins et al.; Frazelle), neither opened, with no measurement found; in dense pick areas travel is small (section 9, C1).
6. **When does pick-path optimisation matter least, according to B&H?**
   When all orders are for one to three items, as at a catalogue fulfilment centre, and when orders are batched (section 4).
7. **Why is "pick-lines per labor hour" biased, in B&H's account?**
   It scores higher when picking cartons than pieces and is not focused on the customer (section 12).
8. **What does an order cut-off do to the work, according to Kim's field study?**
   It induces an order peak just before the cut-off and an imbalanced workload (section 8).

## Deliverable

### A. The picking-method decision table

Read across: the profile in the first column points to the method, for the reason given, on the source named. Every row is drawn from sections 1 to 8; a row resting on this unit's inference says so.

| # | Order profile | Method it points to | Reason | Source and grade |
|---|---|---|---|---|
| 1 | Many small orders (few lines each), no sorter | Batch picking to a cart, sorting while picking | Small orders leave travel per tour high; batching raises pick density; the cart sorts without equipment | de Koster §6, §2.2; B&H ch. 5 introduction [practice]; cart choice this unit's inference |
| 2 | Many small orders, high volume, sorter available | Batch or wave picking, sorted downstream (pick-and-sort) | A sorter lets pick lists be built purely for efficiency | B&H §5.2.1; de Koster §2.2, §8 [practice] |
| 3 | Orders of one to three items | Batch; route optimisation adds little | Optimisation matters little for 1–3 item orders; batching lowers its value further | B&H §10.3.2 [practice] |
| 4 | Large orders (many lines), area small enough for one picker | One order at a time | No sorting needed; the reason to batch is absent | de Koster §6 [practice]; this unit's inference |
| 5 | Large orders, large or busy area, orders visiting few zones | Zone picking, pass-along | Smaller area per picker, less congestion; orders emerge in release sequence | de Koster §5; B&H §3.3; Choe and Sharp 1991 [practice] |
| 6 | Large orders needing many zones, short time | Zone picking in parallel, then consolidate | Zones work at once; needs accumulation or sortation | Choe and Sharp 1991; de Koster §5 [practice] |
| 7 | Many order lines in a short window (for example one item going to many stores: this unit's inference) | Put system | Suits many order lines in a short window | de Koster §2.2 [practice] |
| 8 | Many items, mostly slow, orders of moderate size | Any picker-to-parts method, with route optimisation | Optimisation is most useful here | B&H §10.3.2 [practice] |
| 9 | Picks concentrated in few items | Forward pick area for the fast items, whatever the method | A few items take most picks | B&H §14.2.2, ch. 8; SCE2 §5 [practice] |
| 10 | Many small, time-critical orders, picker-to-parts struggling | Consider goods to the picker | Picker-to-parts often ill-suited to this profile | Boysen et al. 2019, abstract [practice] |
| 11 | Orders sharing destinations and departures | Release in waves by destination or departure | Waves group orders for a common destination | de Koster §2.2; Çeven 2013 [practice] |
| 12 | High volume into an automated sorter | Consider continuous release, with a limit on what is released | Waveless matched or beat waves on throughput in one retailer's simulation; gridlock risk | Gallien and Weber 2010, abstract [independent]; applying it elsewhere is this unit's inference |

### B. The table worked on the case

Facts are from the case register; where the register is silent the cell says so, and an assumption this unit makes is marked and listed in its notes.

**Corvane (fictional), web orders.** One to three items per order; about 18,000 items counted by size and colour; peak web volume about four times a normal week; Mina, operator, picks web orders; Tobias, outbound shift supervisor, answers for release and for pack and ship (case register; Tobias's roles added by SCE1). Known trouble: web orders promised from stock the centre cannot find.

| Question | Answer for Corvane's web orders | Row and source |
|---|---|---|
| Lines per order | One to three items (register) | Row 3 |
| Method the profile points to | Batch picking; to a cart and sorted while picking if the centre has no sorter, sorted downstream if it has one. Whether it has a sorter is not in the register | Rows 1, 2 |
| Routing | Little gain from optimising routes; sequence lines by location | Row 3; B&H §10.3.2, ch. 10 |
| Release | Waves by carrier departure, or continuous; the register gives no departure times | Rows 11, 12 |
| What peak changes | About four times a normal week's web orders across the week (how they fall across departures is not in the register): batches fill faster, sorting and packing become the limit | Register; section 8 (this unit's reading) |
| Where it fails | Short picks at the shelf (the known trouble, as SCE1 read it); a missing item holds the order in sorting | Section 10 |
| Measure to watch | Fill Rate - Order; On Time Shipments; Order Picking Accuracy | Section 12 |

**Corvane (fictional), store orders.** Store replenishment by carton and by single item to 60 stores in four European countries; two main seasons a year (case register). Assumed here, not in the register: a store order covers many items across the range, and stores on one route or carrier share a departure (listed in notes).

| Question | Answer for Corvane's store orders | Row and source |
|---|---|---|
| Lines per order | Not in the register; assumed many (notes) | — |
| Method the profile points to | For items going to many stores at once (new-season allocation): a put system, retrieving by item and putting to each store's slot. For ongoing replenishment of basics: zone or one-order-at-a-time picking of each store's order | Rows 7, 4, 5 |
| Cartons versus single items | Full cartons are picked as cartons; single items are picked as eaches, a second pick flow (SCE2 §2: Corvane breaks units twice) | SCE2 §2 |
| Release | Waves by store route or carrier departure | Row 11 |
| Where it fails | A put slot full or a store's order incomplete at consolidation; cartons and eaches for one store meeting at the dock late | Sections 5, 7 |
| Measure to watch | Shipped Complete per Customer Order; Lines Picked and Shipped per Person Hour, reported separately for cartons and eaches | Section 12; B&H §15.1 |

**Ostrel Foods (fictional), case picking.** About 4,500 items, chilled, frozen and ambient, most dated; one warehouse with three temperature zones; picking by the case onto roll cages; work starts in the evening for delivery next morning; 40 vehicles, about 600 delivery points a day on fixed routes adjusted daily; orders by phone, web shop and sales staff with a cut-off in the late afternoon; Ilse leads chilled picking, Bram replenishes on nights, Sofia builds the next day's routes (case register).

| Question | Answer for Ostrel's case picking | Row and source |
|---|---|---|
| Lines per order | Not in the register | — |
| Method the profile points to | Zone picking by temperature zone (chilled, frozen, ambient), parts of each customer's order consolidated by stop at staging; within a zone, one order or one route at a time onto roll cages | Rows 5, 6; register (three zones; Ilse leads chilled picking) |
| Release | Waves by route, timed backwards from each vehicle's morning departure; the cut-off in the late afternoon fixes the order book before the evening start | Row 11; section 8; register |
| Loading | Roll cages staged by route and loaded in reverse order of delivery | B&H §3.5 |
| Dates | Pick by date rule (FEFO) where the system holds dates | SCE2 §9 |
| Where it fails | Forward location empty because Bram's replenishment and put-away share the night (register, SCE2 §6); a chilled part of an order missing at staging; a cage loaded in the wrong stop order | Sections 7, 10 |
| Measure to watch | Fill Rate - Line; On Time Shipments; Lines Picked and Shipped per Person Hour, not compared with Corvane's eaches | Section 12; B&H §15.1 |

### C. The outbound flow map

Six columns, as SCE2 fixed them: **Step**, **People**, **System touchpoint**, **Data needed**, **Common failure**, **Measure**. Cells cite this unit's sections in brackets or the case register; a cell the register does not fill says so. A failure listed is one to look for, not a claim the operation has it, unless it says "known trouble".

**Corvane (fictional), web and store orders**

| # | Step | People | System touchpoint | Data needed | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Release | Tobias, outbound shift supervisor (register) | Warehouse system turns orders into pick lists, by wave or continuously (2) | Order lines, carrier or store route, departure times; stock at the pick face | Orders released whose stock is not at the face (2, 10) | Internal Order Cycle Time (12) |
| 2 | Pick | Mina, operator, web picking (register); store picking not in the register | Sequence of locations to the handheld; batch or put task (3, 4) | Locations per size and colour; quantities; batch or slot assignment | Short pick; known trouble: stock the centre cannot find (register, 10) | Lines Picked and Shipped per Person Hour; Order Picking Accuracy (12) |
| 3 | Replenish forward | Not in the register | Trigger and task (SCE2 §6) | Forward capacity, trigger | Restock after the picker (10) | Backorders as a Percentage of Total Lines (12) |
| 4 | Sort and consolidate | Not in the register | Tracks each order's parts; cart, put wall or sorter (3.3, 3.5, 3.6, 5) | Order-to-slot or lane assignment | One part missing; order waits (5) | Shipped Complete per Customer Order (12) |
| 5 | Check and pack | Tobias answers for pack and ship (register) | Shows order contents; takes scans; records packed (6) | Order contents; carton rules | Wrong item or quantity not caught (6) | Order Picking Accuracy (12) |
| 6 | Label | Not in the register | Carrier label from each carrier's portal (register, 6) | Carrier, service, address; SSCC for cartons to stores (SCE2 §3.6) | Label re-keyed by hand from a portal (6, reading of register) | Correct Documentation (12) |
| 7 | Stage and load | Not in the register | Staging lane; load scan (7) | Lanes by carrier or store route; vehicle | Unit on the wrong vehicle (7) | On-Time Ready to Ship (12) |
| 8 | Ship | Not in the register; Jonas answers customers once goods are in transit (register) | Departure scan; shipment recorded out (7) | Departure time | Missed cut-off in peak (8) | On Time Shipments (12) |

**Ostrel Foods (fictional)**

| # | Step | People | System touchpoint | Data needed | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Release | Not in the register | Warehouse module releases by route after the late-afternoon cut-off (assumed; notes) (2, 8) | Orders by route and stop; route departure times from Sofia's plan (register) | Late orders and phoned substitutions not in the release (register: substitutions not recorded) | Internal Order Cycle Time (12) |
| 2 | Pick | Ilse, team lead, chilled picking (register); other pickers not in the register | Case picks by zone onto roll cages (3.4) | Locations by temperature zone; dates for FEFO (SCE2 §9) | Short pick; short-dated stock found too late (register: known trouble) | Lines Picked and Shipped per Person Hour (12) |
| 3 | Replenish forward | Bram, reach-truck driver, nights (register) | Trigger and task (SCE2 §6) | Forward capacity and trigger by zone | Replenishment and put-away compete for Bram (SCE2 §6, reading of register) | Backorders as a Percentage of Total Lines (12) |
| 4 | Consolidate by stop | Not in the register | Tracks each order's zone parts (5) | Order-to-cage and cage-to-stop assignment | Chilled or frozen part missing at staging (5) | Shipped Complete per Customer Order (12) |
| 5 | Check | Not in the register | Records the order ready (6) | Order contents; substitutions | Substitution agreed by phone not on the order (register) | Order Picking Accuracy (12) |
| 6 | Label and document | Not in the register | Delivery note; paper on some routes (register) | Customer, stop, contents | Paper note not matching the cage (6) | Correct Documentation (12) |
| 7 | Stage and load | Not in the register; Sofia's routes set the sequence (register) | Staging lane by route; load scan in reverse stop order (7) | Stop sequence per vehicle | Cage loaded out of stop order (7) | On-Time Ready to Ship (12) |
| 8 | Ship | Drivers; Nuno, dispatcher, takes their calls (register) | Departure recorded (7) | Vehicle, route | Late departure; drivers returning with refused goods (register: known trouble), whose cause may start at pick or check | On Time Shipments; Percent of Orders with On Time Delivery (12) |

### D. Template: the picking-method decision table

Fill one block per order flow (web, store, trade customer, other) for a real operation, or for a product by naming the screen or setting that holds each answer. Mark each answer's grade (independent, analyst, vendor-reported, practice) or "observed".

Operation or product: ______ (name; kind of company; region) · Order flow: ______ · Period of the data: ______ · Sources used: ______ (each with its grade)

| Question | Answer | Row of table A it points to | Source and grade |
|---|---|---|---|
| Lines per order | ______ (the distribution, not the average: share of single-line orders, share of picks by order size) | ______ | ______ |
| Units per line | ______ (eaches, cases or pallets; typical quantity) | ______ | ______ |
| Spread of picks across items | ______ (share of picks from the busiest items) | ______ | ______ |
| Orders per day and per peak day | ______ | ______ | ______ |
| Cut-off and departure times | ______ (each order cut-off; each carrier or route departure) | ______ | ______ |
| Equipment for sorting | ______ (none, carts, put wall, sorter) | ______ | ______ |
| Zones | ______ (temperature, product type, building area) | ______ | ______ |
| Method chosen | ______ | ______ | ______ |
| Release rule | ______ (waves by what; or continuous, with what limit) | ______ | ______ |
| Where it fails | ______ (short picks, late replenishment, congestion, missed cut-offs, other) | ______ | ______ |
| Measure to watch | ______ (WERC name, and whose definition) | ______ | ______ |

### E. Template: the outbound flow map

Fill one row per step. Keep the step numbers; add a row where the operation has a step the map lacks, and say why.

Operation or product: ______ (name; kind of company; region) · Goods shipped: ______ (eaches, cases, pallets; dated; temperature zones) · Date filled: ______ · Sources used: ______ (each with its grade)

| # | Step | People | System touchpoint | Data needed | Common failure | Measure |
|---|---|---|---|---|---|---|
| 1 | Release | ______ (who releases, which shift) | ______ (waves or continuous; which system) | ______ (order fields; departures; stock at the face) | ______ (what is released without stock) | ______ (internal order cycle time, or the site's own) |
| 2 | Pick | ______ (who picks, which method) | ______ (paper, handheld, voice, light; sequence or path) | ______ (locations, quantities, batch or slot) | ______ (short picks, search, wrong item) | ______ (lines per person hour; picking accuracy) |
| 3 | Replenish forward | ______ (who restocks, which hours) | ______ (trigger, task) | ______ (capacity, trigger) | ______ (restock after the picker) | ______ (backorders; the site's own) |
| 4 | Sort and consolidate | ______ (who, where) | ______ (cart, put wall, sorter, consolidation area) | ______ (slot or lane assignment) | ______ (what waits, and for what) | ______ (shipped complete) |
| 5 | Check and pack | ______ (who) | ______ (what is scanned, what is printed) | ______ (contents, carton rules) | ______ (errors not caught) | ______ (picking accuracy) |
| 6 | Label and document | ______ (who) | ______ (carrier label source; document) | ______ (carrier, service, SSCC, document type by region) | ______ (re-keyed or wrong labels) | ______ (correct documentation) |
| 7 | Stage and load | ______ (who) | ______ (lanes; load scan) | ______ (lanes, vehicle, stop sequence) | ______ (wrong vehicle or sequence) | ______ (on-time ready to ship) |
| 8 | Ship | ______ (who records departure) | ______ (departure scan; shipment record) | ______ (departure time) | ______ (missed cut-off) | ______ (on time shipments) |

Below the table: the release rule and who sets it (______), the hours between each cut-off and its departure (______), what peak multiplies and by how much (______, with source), and the step where the operation's known trouble shows (______).

### F. Glossary lines

Added to SCE1's and SCE2's working glossary; each term as this unit uses it.

| Term | Working definition | Source |
|---|---|---|
| Order line; pick line | One item on an order, with its quantity | Course term; B&H §14.2 [practice] |
| Order profile; activity profiling | The distribution of lines per order, units per line and picks across items; its measurement | B&H ch. 14 [practice] |
| ABC analysis | Sorting items into the few with most activity, a middle group, and the many with little | B&H §14.2.1 [practice] |
| Order release | The moment orders become floor work | Course term; B&H ch. 4 [practice] |
| Wave; wave picking | Orders released together, often for a common destination, then picked, sorted and shipped | de Koster §2.2; Çeven 2013 [practice] |
| Continuous (waveless) release | Orders released one by one or in small groups as capacity frees | Gallien and Weber 2010 [practice]; wording the course's |
| Picker-to-parts; parts-to-picker (goods to the picker) | The picker travels to the goods; the goods are brought to the picker | de Koster §2.2 [practice] |
| Discrete picking | One picker, one order, one tour | de Koster §6 [practice] |
| Batch picking; order batching | Several orders picked in one tour; grouping orders into such sets | de Koster §6 [practice] |
| Pick density | Picks per unit of travel | B&H ch. 5 introduction [practice]; wording the course's |
| Sort-while-pick | Sorting a batch into orders on the pick cart | de Koster §2.2 [practice] |
| Zone picking | Pickers assigned to parts of the storage area | de Koster §2.2, §5 [practice] |
| Pick-and-pass (progressive zoning) | An order passed from zone to zone until complete | de Koster §5 [practice] |
| Parallel (synchronised) zoning | Zones pick parts of an order at once, merged afterwards | de Koster §5 [practice] |
| Bucket brigade | Pickers carry work forward until someone takes it over | B&H §11.1 [practice] |
| Pick-and-sort; sorter | Batch picking with sorting into orders downstream, often by a conveyor sorter | de Koster §2.2, §8 [practice] |
| Put system; put wall | Goods retrieved by article and distributed over orders; a rack of order slots for it | de Koster §2.2 [practice]; put wall the course's term |
| Routing; S-shape; largest gap | The order and path of a pick tour; two heuristics for it | de Koster §7 [practice] |
| Order accumulation | Bringing the parts of an order back together | de Koster §2.3 [practice] |
| Staging (outbound) | Setting packed units down by the dock before loading | B&H §3.5 [practice] |
| Short pick | A pick that finds less at the location than the line asks for | Course term |
| Order cut-off | The latest time an order is accepted for a given dispatch | Course term; Kim 2020 [practice] |
| Carrier departure; pick-up time | The time a vehicle leaves the dock | Course term; Kim EI2018-02 [practice] |
| Order fill rate; order line fill rate | Orders, or lines, filled completely over all orders or lines | APQC [practice] |
| Perfect order | On time × complete × damage free × correct documents | APQC [practice] |

## Notes: facts for the case register

| Unit | Operation | Fact |
|---|---|---|
| SCE3 | Corvane | Assumed: a store order covers many items across the range. |
| SCE3 | Corvane | Assumed: stores on one route or carrier share a departure. |
| SCE3 | Ostrel Foods | Assumed: the warehouse module releases by route after the late-afternoon cut-off. |

## Sources

All addresses opened on 24 November 2026; the source log (sources.md) gives what was read at each.

- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 16, 17 and bibliography. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- de Koster, R., Le-Duc, T. & Roodbergen, K. J. (2007). Design and control of warehouse order picking: A literature review. *European Journal of Operational Research* 182(2), 481–501. https://doi.org/10.1016/j.ejor.2006.07.009 (read in the version of record at https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf)
- Boysen, N., de Koster, R. & Weidinger, F. (2019). Warehousing in the e-commerce era: A survey. *European Journal of Operational Research* 277(2), 396–411. https://doi.org/10.1016/j.ejor.2018.08.023 (abstract, read at https://repub.eur.nl/pub/110234 and https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/)
- Gallien, J. & Weber, T. (2010). To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter. *Manufacturing & Service Operations Management* 12(4), 642–662. https://doi.org/10.1287/msom.1100.0291 (abstract, read at https://pubsonline.informs.org/doi/10.1287/msom.1100.0291; authors from https://dspace.mit.edu/handle/1721.1/65618)
- Batt, R. J. & Gallino, S. (2019). Finding a Needle in a Haystack: The Effects of Searching and Learning on Pick-Worker Performance. *Management Science* 65(6), 2624–2645. https://doi.org/10.1287/mnsc.2018.3059 (abstract, read at https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2018.3059)
- Kim, T. Y. (2020). Improving warehouse responsiveness by job priority management: A European distribution centre field study. *Computers & Industrial Engineering* 139. https://doi.org/10.1016/j.cie.2018.12.011 (abstract excerpts, read at https://repository.mdx.ac.uk/item/8891y)
- Kim, T. Y. (2018). Improving warehouse responsiveness by job priority management: A European distribution centre field study. Econometric Institute Report EI2018-02, Erasmus University Rotterdam. https://repub.eur.nl/pub/112492 (full text read at https://repub.eur.nl/pub/112492/Repub_112492.pdf)
- Çeven, E. (2013). *Wave Release Strategies for Order Fulfillment Systems with Deadlines*. Dissertation, Industrial and Systems Engineering, Auburn University (abstract). https://etd.auburn.edu/handle/10415/3716
- Choe, K. & Sharp, G. (1991). *Small Parts Order Picking: Design and Operation*. School of Industrial and Systems Engineering, Georgia Institute of Technology. https://www2.isye.gatech.edu/~mgoetsch/cali/Logistics%20Tutorial/order/article.htm
- Dekker, R., de Koster, M. B. M., Van Kalleveen, H. & Roodbergen, K. J. (2002). *Quick Response Practices at the Warehouse of Ankor*. ERIM Report Series ERS-2002-19-LIS, Erasmus University Rotterdam. https://repub.eur.nl/pub/168/erimrs20020222120221.pdf
- Erasmus Research Institute of Management, Material Handling Forum. "Order picking". Undated. https://erim.eur.nl/material-handling-forum/research-education/tools/calc-order-picking-time/order-picking
- WERC. "WERC DC Measures Survey - 2025". https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf
- APQC. "Order line fill rate". Open Standards Benchmarking measure page, undated. https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/order-line-fill-rate
- APQC. "Order fill rate". Open Standards Benchmarking measure page, undated. https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/order-fill-rate
- APQC. "Perfect order performance". Open Standards Benchmarking measure page, undated. https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/perfect-order-performance
- Hyster-Yale Materials Handling, Inc. "Benchmarking and Improving Distribution Center Metrics". White paper, 2026. Vendor-reported. https://www.yale.com/4a4034/globalassets/coms/yale/north-america/documents/white-papers/yal-1558_werc2026updates_improvingdcmetricswhitepaper.pdf

## Unsure list

# Unsure: SCE3

1. Every quotation from Bartholdi & Hackman and de Koster et al. ("over 80% of all order-picking systems in Western Europe"; "requires all the work of balancing an assembly line"; "the shipping dock will be congested even if work flows smoothly"; "One would expect a higher score if picking cartons instead of pieces"; "it is the largest component of labor in a typical distribution center") was taken from a fetch tool's extraction and not re-read against the PDF; page numbers were not available, so sections are cited.
2. Section placements in B&H ch. 14 were re-read by the applier on 24 Nov 2026 against the chapter's headings: pick lines as "a strong indicator of work", Figure 14.1 and Figure 14.4 sit in §14.2.2; the 20/80 rule in §14.2.1; "a necessary first step" in the chapter's opening. Cited accordingly. Release 0.98's title page reads "Revised August 28, 2017".
3. The bucket-brigade figures (over 30% picks per person-hour at a chain retailer's national DC; 20% pick rate and 90% lower variance at a US recorded-music distributor, B&H §11.2) are the extraction's reading; the reference behind the first ([6]) was not opened.
4. Gallien & Weber: the publisher page showed no authors, volume or pages; authors come from MIT DSpace (2008 working-paper record); 12(4), 642–662 (2010) was confirmed by the fresh check at LBS Research Online, not on Crossref.
5. Kim (2020): the claims on cut-off peaks, pick-up times spread across the day and packing being often the most demanding stage come from the 2018 report version (EI2018-02), not the journal article; that the journal text keeps them was not checked; the next-working-day pick-ups were re-read in the report by the applier on 24 Nov 2026 ("OEM warehouses usually dispatch retailer orders by truck on agreed pick-up times on the next working day"). The author's full name (Thai Young Kim) is from the report record.
6. Choe & Sharp (1991): the page gives a 1991 Georgia Tech Research Corporation copyright and no venue; whether it was published elsewhere was not checked. Its attribution of "30% to 40% of the labor cost" to Gross (1981) is as the extraction gave it.
7. Dekker et al. (2002): "about 50%" travel and "about 55%" of operational costs are both credited to Tompkins et al. (1996) as the extraction read them; whether the report cites the 1996 edition or another was not checked against its reference list.
8. The ERIM "Order picking" page is undated and shows no author; the 60% (Drury 1988) figure is as extracted. The Georgia Tech "Importance of Order Picking" page (63%, no source) was cut from the unit as carrying no evidence.
9. WERC 2025 survey: the grouping of measures into "outbound" is this unit's; the measure names are as extracted, including "Correct Documentation (ASN,Invoice, etc.)" with no space after the comma.
10. Hyster-Yale white paper: its date (2026, code 082026) and the two definitions are as extracted; that it reproduces WERC's own wording was not confirmed.
11. Re-read by the applier on 24 Nov 2026: B&H §10.1 ("most WMSs do not maintain this level of information") and §10.3 on shortest distances; Batt & Gallino's abstract names "online and multichannel retailing"; RePEc spells the surname "Çeven" (Çeven & Gue, 2017), the Auburn record "Ceven".

Object: the pick list, as orders become a picker's tour (sections 2 to 4)

Fresh check 2026-11-24 (claude-opus-5-5): keep · 0 errors, 8 should-fix, 14 minor; report `audits/supply-chain-execution/fresh-check-SCE3.md`
