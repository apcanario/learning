# Case register: Supply Chain Execution for Product Teams

Three fictional operations and three fictional software vendors carry the course's worked examples. Everything here is invented. Nothing in this file is evidence for a claim about the world, and no figure here is a benchmark.

Rules for every unit:
- Label each operation "(fictional)" on first use in the unit.
- Take facts only from this file. A fact a unit invents is listed in its notes and appended to "Added by units" at filing.
- No case operation is ever said to use a real vendor's product. Their systems are "the warehouse system", "the transport system", "the order system", "the ERP"; where a unit needs a named product, it is one of the fictional vendors' below.
- No fictional vendor stands for a real one. A unit never says or hints which real company one resembles.
- Names of people are first names only. They are roles to hang a card on, not characters.
- The names Corvane, Ostrel, Tandric, Halvern, Varnby and Kestrow were coined for this course. The setup row searches each once; a name that matches a real company in logistics, retail, food or software is replaced before any unit is written. (S-SCE0, 19 Nov 2026: one coined name matched a real software maker and was replaced; the six above are the names after that search.)

## Corvane (fictional): a fashion retailer

| Fact | Value |
|---|---|
| What it sells | Clothing and accessories, own label, mid-priced |
| Channels | 60 stores in four European countries, one website |
| Distribution | One distribution centre of 28,000 m², one shift pattern of two shifts, a third in peak |
| Range | About 18,000 items (size and colour counted separately), two main seasons a year |
| Flows | Store replenishment by carton and by single item; web orders of one to three items; returns from web and from stores |
| Peak | Mid-November to early January; web volume about four times a normal week |
| Staff in the centre | About 140 in a normal week, about 260 in peak, the difference from agencies |
| Systems | An ERP, a warehouse system about twelve years old on its own servers, an order system for the website, carriers booked through each carrier's own portal |
| Known trouble | Web orders promised from stock that the centre cannot find; store staff asked to ship web orders with no process for it; the warehouse system is near the end of its vendor's support |
| What it is deciding | Whether to replace the warehouse system, and whether to buy order and transport systems from the same vendor |

People:

| Name | Role |
|---|---|
| Mina | Operator, picks web orders, two years in the job |
| Tobias | Shift supervisor, outbound |
| Carla | Inventory controller |
| Jonas | Customer service agent |
| Freya | Store associate who ships web orders from a store |
| Edda | Vice-president, supply chain; sponsors the replacement |
| Ravi | IT director |
| Helene | Chief financial officer |
| Marek | Site manager of the distribution centre |

## Ostrel Foods (fictional): a food distributor

| Fact | Value |
|---|---|
| What it does | Buys from producers and delivers to restaurants, canteens and small shops |
| Range | About 4,500 items: chilled, frozen and ambient; most carry a date |
| Distribution | One warehouse with three temperature zones; picking by the case onto roll cages; work starts in the evening for delivery next morning |
| Delivery | Its own fleet of 40 vehicles, about 600 delivery points a day, fixed routes adjusted daily |
| Orders | By phone, by a web shop and from sales staff, with a cut-off in the late afternoon |
| Known trouble | Short-dated stock found too late; substitutions agreed by phone and not recorded; drivers returning with refused goods |
| Systems | An ERP with a warehouse module, a routing tool for the fleet, paper delivery notes on some routes |

People:

| Name | Role |
|---|---|
| Bram | Reach-truck driver, putaway and replenishment, nights |
| Ilse | Team lead, chilled picking |
| Sofia | Transport planner, builds the next day's routes |
| Nuno | Dispatcher, handles the day's calls from drivers and customers |
| Aart | Operations director |

## Tandric Logistics (fictional): a logistics provider

| Fact | Value |
|---|---|
| What it does | Runs warehousing and arranges freight for other companies |
| Site in the case | One multi-client warehouse with nine clients: seven store pallets and cases, two are online sellers needing single-item picking |
| Freight | A desk that arranges full and part loads with outside carriers for clients; no trucks of its own |
| How it is paid | Warehousing by activity (per pallet in, per pick, per pallet stored per week); freight at a margin over what the carrier is paid |
| Contracts | Two to three years; a new client is expected to be live within weeks of signature |
| Known trouble | Each client wants its own rules and reports; invoices disputed because activity was not recorded; a new client's go-live slipped |
| Systems | A warehouse system shared by all clients, a transport system for the freight desk, a client portal |

People:

| Name | Role |
|---|---|
| Anke | Site manager |
| Luis | Onboarding lead, configures the system for each new client |
| Priya | Freight desk: tenders loads to carriers and checks their invoices |
| Dario | System administrator |
| Karin | Commercial director, signs client contracts and sponsors software purchases |
| Olu | Client services, answers the clients' questions and sends their reports |

## The fictional vendors

Used wherever a unit maps a product line, builds a competitor sheet or prices a system. Every module name is generic on purpose.

### Halvern Systems (fictional): an execution specialist

| Fact | Value |
|---|---|
| Kind | Sells order, warehouse and transport software, and nothing else |
| Customers it names | Retailers, distributors and logistics providers, mid-sized to large |
| Warehouse line | Halvern Warehouse (core system), with modules: Labour, Voice, Yard, Slotting, Automation Connect, Client Billing |
| Transport line | Halvern Transport (core system), with modules: Rating and Tendering, Fleet Routing, Tracking, Freight Audit, Claims |
| Order line | Halvern Order (core system), with modules: Availability, Promising, Sourcing Rules, Store Fulfilment, Returns |
| Delivery | Cloud subscription; implementation by its own services team and by partners |
| What it says of itself | "One vendor for execution" |

### Varnby Software (fictional): an ERP vendor with execution modules

| Fact | Value |
|---|---|
| Kind | Sells an ERP; warehouse and transport are modules of it |
| Customers it names | Manufacturers and wholesalers already on its ERP |
| Lines | Varnby Warehouse and Varnby Transport, sold with the ERP; no separate order system |
| What it says of itself | "No integration to build" |

### Kestrow (fictional): a mid-market warehouse specialist

| Fact | Value |
|---|---|
| Kind | Sells one warehouse system and nothing else |
| Customers it names | Smaller distributors and online sellers, single-site |
| Line | Kestrow WMS, with modules: Mobile, Parcel Shipping, Returns |
| What it says of itself | "Live in weeks" |

## Added by units

Empty until the first unit is filed. One row per fact: unit, operation, fact.

| Unit | Operation | Fact |
|---|---|---|
| SCE1 | Corvane | Freya (store associate) answers for web orders sourced to a store (map step 3). |
| SCE1 | Corvane | Tobias (outbound shift supervisor) answers for release of orders to the shift and for pack and ship (map steps 4 and 7). |
| SCE1 | Corvane | Carla (inventory controller) answers for the stock record at receiving and put-away (map step 5). |
| SCE1 | Corvane | Jonas (customer service agent) answers customers about shipments in transit (map step 9). |
| SCE1 | Corvane | Settlement is held in the ERP, and Helene (chief financial officer) answers for the financial record (map step 11); a working placement. |
| SCE1 | Corvane | The replacement decision covers map steps 1 to 9 and 12 (SCE1's reading of "replace the warehouse system and buy order and transport systems from the same vendor"). |
| from Supply Chain Planning | Corvane | Edda (vice-president, supply chain) sponsors the purchase of a retail planning system. |
| from Supply Chain Planning | Corvane | Buying: most of each season's range is ordered six to nine months ahead from suppliers in Asia and Turkey; a small part is bought close to the season from nearer suppliers. |
| from Supply Chain Planning | Corvane | Range life: about a third of the range carries over between seasons (basics); the rest is new each season and has no sales history of its own; four smaller drops a year sit inside the two main seasons. |
| from Supply Chain Planning | Corvane | Stock: held in the distribution centre and in the 60 stores; a web order can be filled from either. |
| from Supply Chain Planning | Corvane | Planning today: a merchandise financial plan in spreadsheets; first allocation to stores by store grade; store replenishment of basics proposed by the ERP and edited by allocators; end-of-season markdown decided in a weekly trading meeting. |
| from Supply Chain Planning | Corvane | Known trouble (planning): stores graded on last year's sales receive the wrong sizes; basics run out in the best stores while slow stores hold them; markdown starts late. |
| from Supply Chain Planning | Corvane | What it is deciding (planning): whether to buy a retail planning system, and whether allocation or the financial plan comes first. |
| from Supply Chain Planning | Corvane | Signe: head of merchandise planning. |
| from Supply Chain Planning | Corvane | Lorenzo: merchandise planner, womenswear. |
| from Supply Chain Planning | Corvane | Agnes: allocator. |
| from Supply Chain Planning | Corvane | Tomasz: demand planner, basics and web. |
| from Supply Chain Planning | Ostrel Foods | Aart (operations director) sponsors the purchase of a planning system. |
| from Supply Chain Planning | Ostrel Foods | Demand: a few hundred fast items and a long tail of slow items ordered by a few customers each; a strong weekly pattern, holiday peaks, and supplier promotions several times a year. |
| from Supply Chain Planning | Ostrel Foods | Supply: producers deliver on fixed days with minimum orders; chilled items have shelf lives counted in days. |
| from Supply Chain Planning | Ostrel Foods | Planning today: one demand planner and a team of buyers who each own a set of suppliers; reorder proposals from the ERP, often overridden; forecast accuracy reported monthly at total level only. |
| from Supply Chain Planning | Ostrel Foods | Known trouble (planning): waste on chilled items after promotions; shortages on slow items that matter to a few large customers; buyers do not trust the ERP's proposals. |
| from Supply Chain Planning | Ostrel Foods | What it is deciding: whether to buy a planning system for demand and replenishment. |
| from Supply Chain Planning | Ostrel Foods | Wim: demand planner. |
| from Supply Chain Planning | Ostrel Foods | Greta: senior buyer, chilled. |
| from Supply Chain Planning | Ostrel Foods | Samir: replenishment analyst. |
| from Supply Chain Planning | Ostrel Foods | Marta: commercial manager, plans promotions. |
| from Supply Chain Planning | Ostrel Foods | Joris: finance director. |
| from Supply Chain Planning | Varnby Software | Planning line: Varnby Planning, sold with the ERP: a demand forecasting module, requirements planning, and a planning workbench; no separate retail planning. |
| SCE3 | Corvane | A store replenishment order covers many items across the range (assumption in deliverable B; the register gives no lines per store order). |
| SCE3 | Corvane | Stores on one route or carrier share a departure time (assumption in deliverable B). |
| SCE3 | Corvane | Whether the distribution centre has a sorter, carts or a put wall is not in the register; deliverable B leaves it open (a register row only if a later unit needs it). |
| SCE3 | Ostrel Foods | Picking is released by route after the late-afternoon order cut-off, and the parts of a customer's order picked in the three temperature zones are consolidated by stop at staging (working description in deliverable C). |
| SCE3 | Ostrel Foods | Roll cages are staged by route and loaded in reverse order of delivery (deliverables B and C; textbook practice applied to the register). |
| SCE2 | Corvane | Suppliers deliver by the pallet, so the centre breaks units pallet to carton and carton to each (section 2; this unit's assumption). |
| SCE2 | Ostrel Foods | Producers deliver by the pallet, so the warehouse breaks units pallet to case (section 2; this unit's assumption). |
| SCE2 | Ostrel Foods | Ilse's chilled pickers depend on Bram's replenishment (section 6, deliverable A row 9; this unit's reading). |
| SCE2 | Corvane | Mina's web picks depend on replenishment of forward locations (deliverable B row 9; this unit's reading). |
| SCE4 | Corvane | When a picker reports a short pick on a web order, the order system can re-source the missing line to a store, where Freya ships it, so the customer receives two parcels (section 9; worked chain, this unit's inference). |
| SCE4 | Corvane | Jonas also answers customers about items missing from web orders (section 9). |
| SCE4 | Corvane | Carla counts locations after short picks and after re-slots (deliverable A; assumption). |
| SCE4 | Corvane | Each season brings many SKUs needing new locations (section 6; this unit's reading of the two seasons and the one-third carry-over). |
| SCE4 | Ostrel Foods | Scheduled counts run in the daytime, before evening picking; trigger counts run within the shift (deliverable B; assumption). |
| SCE4 | Ostrel Foods | A counter did not pick or put away the location that day; adjustments above a limit are approved by Aart or someone he names (deliverable B; assumption). |
| SCE4 | Ostrel Foods | Aart reviews count results weekly (deliverable B; assumption). |
| SCE5 | Corvane | Mina is measured on picks per person-hour against a standard and on picking accuracy (card 1; working, from B&H §3.3). |
| SCE5 | Corvane | Mina uses a handheld scanner showing a sequence of locations (card 1; from SCE3 deliverable C, working). |
| SCE5 | Ostrel Foods | Ilse is measured on routes picked complete by departure and on picking accuracy by case (card 2; working). |
| SCE5 | Ostrel Foods | Ilse's pickers use handhelds or voice; Ilse watches the route backlog on a desktop or handheld (card 2; working, the register names no device). |
| SCE5 | Ostrel Foods | Ilse moves pickers between routes and reports shorts and substitutes to Nuno (card 2; working). |
| SCE5 | Corvane | Carla uses a desktop for reports and adjustments and a handheld for counts (card 3; working). |
| SCE5 | Ostrel Foods | Sofia's route plan is the warehouse's release plan; she re-plans late orders and tells Ilse which routes moved (card 4; this unit's reading of the register and SCE3's register note). |
| SCE5 | Corvane | Marek is measured on cost per unit handled, on-time and accurate shipments, injuries and staff turnover, and sets standards and any bonus scheme (card 5; working). |
| SCE5 | Corvane | Marek answers to Edda (card 5; working placement; the register does not say who the site manager reports to). |
| SCE5 | Corvane | Corvane's distribution centre has no record in the register of automation; section 7 places Halvern's Automation Connect (fictional) only as a register module, not at Corvane. |
| SCE5 | Corvane | Carla reports to Marek (card 3; working placement). |
| SCE5 | Ostrel Foods | Sofia works at a desk between the cut-off and the evening start on the routing tool and the ERP, is measured on routes built by the time picking starts and vehicles used, hands routes to Ilse's team and Nuno, and sometimes changes routes after picking has begun (card 4; working). |
| SCE5 | Corvane | Marek staffs the peak, approves workarounds and prepares the warehouse-system replacement (card 5; working) |
| SCE6 | Halvern Systems | Halvern Warehouse (core system) is assumed to hold the core capabilities: expected receipts (W1), receiving (W4), directed put-away (W8), stock locator (W9), cycle counting and adjustments (W12), directed picking on a handheld (W17), packing and consolidation (W21) and the shipment record (part of W22). The register names the core and none of its functions (section 7; deliverable B rows 1, 4, 8, 9, 12, 17, 21, 22; this unit's assumption). |
| SCE6 | Halvern Systems | The register gives no claim for Halvern Warehouse on appointments, quality holds, labels, cross-docking, stock statuses and dates, replenishment, returns, traceability, release, light-directed work, interleaving, value-added work, multi-site views, EDI or configurability; deliverable B leaves them open. Returns appear only as a Halvern Order module; carrier labels and manifests could sit in Halvern Warehouse or Halvern Transport (section 7; deliverable B rows 14, 22; open questions for SCE10). |
| SCE6 | Halvern Systems, Varnby Software, Kestrow | Placed on Gartner's 2022 vendor types: Halvern as a suite vendor of execution software, Varnby as an application vendor whose warehouse system is a module of its ERP, Kestrow as a specialist (section 2; this unit's placement, the register does not use the analyst's types; SCE17 inherits it; flag F53). |
| SCE7 | Corvane | With one distribution centre serving stores in four European countries, some store deliveries cross a border, so the CMR applies to those where its conditions are met (deliverable A; this unit's inference; the register does not say where the centre is). |
| SCE7 | Corvane | One store's replenishment goes as one shipment with a contracted road carrier, booked in that carrier's portal (deliverable A; assumption). |
| SCE7 | Corvane | Who plans and books store transport, who checks carrier invoices, and who files claims are not in the register; deliverable A leaves them open (a register row only if a later unit needs it). |
| SCE7 | Corvane | Carrier invoices are received, checked and paid in the ERP, Helene answering for the financial record (deliverable A rows 9 to 11; repeats SCE1's working placement). |
| SCE7 | Tandric Logistics | The load in deliverable B is a full load for one of the seven pallet-storing clients, from Tandric's warehouse to that client's customer (assumption). |
| SCE7 | Tandric Logistics | Client orders for freight arrive through the client portal, and Olu answers clients' tracking questions from the transport system and the portal (deliverable B rows 1 and 7; this unit's reading). |
| SCE7 | Tandric Logistics | Tandric invoices the client the freight price after delivery, and pays the carrier itself; how the client is billed for freight is otherwise not in the register (deliverable B rows 9 and 11; reading of "paid at a margin"). |
| SCE7 | Tandric Logistics | The register does not give Tandric's region, so deliverable B gives both regions' documents; a register row on region would let later units choose. |
| SCE7 | Ostrel Foods | Ostrel's deliveries are own-account transport in European terms and private carriage in US terms; its region is not in the register (section 8; reading). |
| SCE7 | Halvern Systems | On the lifecycle steps, Rating and Tendering sits at steps 2 to 4, Tracking at step 7, Freight Audit at steps 10 and 11, Claims at step 12, Fleet Routing in own-fleet routing (section 5; this unit's placement, not a register fact). Step 11 revised by SCE10 §7: Freight Audit holds the approved charge; payment in the ERP (working). |
| SCE8 | Ostrel Foods | Nuno, the dispatcher, is measured on on-time delivery and refused goods per route; he works by phone and a desktop (whether in the routing tool is not in the register), answers drivers' and customers' calls, changes stops during the day, records refusals and substitutions, and tells Sofia and the warehouse (deliverable A, card 2; working; bears on SCE13). |
| SCE8 | Ostrel Foods | Sofia, as transport planner, is also measured on vehicle fill; her other card lines repeat SCE5's register rows (deliverable A, card 1; working; bears on SCE13). |
| SCE8 | Tandric Logistics | The carriers Tandric's freight desk tenders to answer by EDI (X12 204 and 990), by a portal, or by e-mail and phone; the register names no carrier staff, so the carrier representative's card carries no name (deliverable A, card 3; working; bears on SCE13). |
| SCE8 | Tandric Logistics | Priya is measured on invoice match rate and on client invoices disputed; she matches carrier invoices to the tender and rate, queries extra charges, carries agreed extras to the client's invoice and releases invoices for payment; who pays the approved invoices is not in the register (deliverable A, card 4; working; bears on SCE13 and DD-SCE1). |
| SCE8 | Tandric Logistics | Priya also plans each load before tendering it (section 3.1; repeats SCE7 deliverable B's reading; bears on SCE13). |
| SCE8 | Tandric Logistics | Olu does the analyst's report work: he builds each client's freight report by hand, is measured on reports sent on time and questions answered, and hands reports to the clients and to Karin (deliverable A, card 5; this unit's reading of "sends their reports"; bears on SCE13). |
| SCE8 | Halvern Systems | Halvern Transport, the core system, is assumed to hold the shipment plan (T2: order intake, consolidation, mode and carrier selection); the register names the core and none of its functions (section 6; deliverable C row 2; assumption; bears on SCE10). |
| SCE8 | Halvern Systems | The register gives no claim for Halvern Transport on T1, T3, T6 to T8, T10 to T12 and T17 to T24; whether Halvern Warehouse's Client Billing bills freight at a margin is open (deliverable C; bears on SCE10 and DD-SCE1). |
| SCE9 | Corvane | Deliverable A's order is a two-item web order to a home address in the store's country; both items are held by one store and the centre is short of one, so the order system sources the whole order to the store; a parcel carrier collects at the store, booked in that carrier's own portal (deliverable A; assumption; bears on SCE10). |
| SCE9 | Corvane | Jonas (customer service agent) takes customers' changes and cancellations, issues return authorisations and refunds, works on a desktop with the order system and each carrier's portal, and is measured on contacts handled, contacts resolved at the first contact and "where is my order" contacts (deliverable B, card 1; working; bears on SCE13). |
| SCE9 | Corvane | Freya (store associate) is measured on web orders packed by the carrier's collection time, store rejection rate and pickup ready time; she sees web orders on a store device (not in the register), declines orders she cannot fill, which are then re-sourced, and takes web returns at the till (deliverable B, card 2; working; whether web returns are accepted in stores is not in the register; bears on SCE13). |
| SCE9 | Corvane | An e-commerce operations role runs the online orders day to day (exception queue, re-sourcing, reports), named Lena (this unit's name; the register names no one in the role) (deliverable B, card 3; working; bears on SCE13). |
| SCE9 | Corvane | A rule-setter role configures availability buffers, sourcing order, store caps and substitution rules, named Oskar (this unit's name; the register names no one in the role) (deliverable B, card 4; working; bears on SCE13). |
| SCE9 | Corvane | How a store receives web orders, how store stock reaches the order system, whether a web order can be returned to a store, and which system triggers a refund are not in the register; deliverable A leaves them open (a register row only if a later unit needs it; bears on SCE10). |
| SCE9 | Corvane | The refund is paid through the ERP, Helene answering for the financial record (deliverable A row 12; repeats SCE1's working placement; bears on SCE10). |
| SCE9 | Halvern Systems | On SCE9's twelve steps, Availability sits at step 2, Promising at step 3, Sourcing Rules at step 4 (with re-sourcing and the split decision), Store Fulfilment at steps 5 to 8 when a store fills the order (with collect in store), Returns at step 11 (section 12; this unit's placement, not a register fact; bears on SCE10 and SCE17). |
| SCE9 | Halvern Systems | Halvern Order (core) is assumed to hold web order capture (O1), order status and notifications (O19) and changes and cancellations passed to the location (O20) (section 12; deliverable C rows 1, 19, 20; assumption, as SCE6 and SCE8 assumed their cores; bears on SCE10). |
| SCE9 | Halvern Systems | The register gives no claim for Halvern Order on O2, O3, O4, O7, O9, O11, O14, O15, O18, O22, O23, O24 and O25; who triggers the refund (O22) and whether business orders by EDI are served (O4) are open (deliverable C; bears on SCE10 and SCE17). |
| SCE9 | Corvane | Lena runs e-commerce operations: Corvane's online orders day to day (deliverable B, card 3; section 10; this unit's case fact). |
| SCE9 | Corvane | Oskar sets the order rules: he configures the order system's availability, promise and sourcing rules (deliverable B, card 4; section 10; this unit's case fact). |
| SCE9 | Corvane | Oskar changes the order rules before each season and before peak (card 4 field 3; working, from the register's two seasons and peak dates). |
| SCE9 | Corvane | Lena depends on Tobias's outbound shift at the centre, with Freya's stores and the carriers, and hands customer messages to Jonas and rule changes to Oskar (card 3 field 9; working). |
| SCE9 | Corvane | Oskar depends on Carla's stock records for the centre and hands the effects of his rules to Lena and to Edda, vice-president supply chain (card 4 field 9; working). |
| SCE9 | Corvane | Jonas hands refunds to finance and exceptions to e-commerce operations (card 1 field 9; working). |
| SCE10 | Corvane | Section 8's worked order: a two-item web order to a home address, both items held by the distribution centre; one item short at the pick face; the parcel carrier collects at the centre, booked in its own portal (assumption; bears on DD-SCE2). |
| SCE10 | Corvane | The status words of section 8 (sourced, released, one short, packed, label created, collected, in transit, delivered, closed) are this unit's working terms for Corvane's three systems (working; bears on SCE13, SCE15). |
| SCE10 | Corvane | Owners of facts (deliverable A): the ERP holds the item master, pack and units of measure, store addresses, the customer payment record, carrier invoices and payment, and carriers as suppliers; the order system holds web customers' addresses, the web order and the sellable stock figure; each carrier's portal holds the carrier label, tracking number, transit status and proof of delivery (working placements; SCE1's ERP placement extended; bears on SCE15, SCE18). |
| SCE10 | Corvane | Ravi (IT director) owns the order-to-warehouse interface; who can make carrier status reach the order system is not in the register (deliverable B rows 2 and 5; working; bears on SCE11, SCE14). |
| SCE10 | Corvane | The carrier sees a re-keyed label's mismatch first, at a failed scan (deliverable B row 4; working; bears on DD-SCE2). |
| SCE10 | Ostrel Foods | Refused goods returned by drivers are recorded on the paper delivery note only; who books them back into stock and credits the customer is not in the register (deliverable B row 8; reading of the register's paper notes and refused goods; the open half a question for DD-SCE2). |
| SCE10 | Ostrel Foods | When Sofia changes a route after picking began, Ilse sees it first at staging and moves cages (deliverable B row 7; reading of SCE5's register rows). |
| SCE10 | Tandric Logistics | Some clients' orders arrive in a form the shared warehouse system does not take and are keyed by hand; Luis or the warehouse team sees it first (deliverable B row 10; working; SCE7 B read client orders as arriving through the client portal; bears on DD-SCE1, SCE14). |
| SCE10 | Tandric Logistics | The carrier's driver and Priya see a load not ready (Priya on the invoice), Olu or Priya see a missing proof of delivery, and Olu answers clients' status questions before Tandric knows (deliverable B rows 12 to 14; repeats SCE7 B readings; working). |
| SCE10 | Halvern Systems | On the course's placement rule (section 7; deliverable A rows 4, 11, 12, 13, 15): Halvern Warehouse's Yard module holds dock appointments at the operation's own doors (W2), the warehouse line prints parcel labels and manifests (W22), Halvern Transport holds the parcel carrier choice (T8), tracking events (Tracking) and the approved carrier charge (Freight Audit); payment stays in the ERP (this unit's placement, not a register fact; bears on SCE6, SCE8, SCE17). |
| SCE11 | Corvane | Edda (vice-president, supply chain) holds two committee roles in the warehouse-system selection: operations executive and executive sponsor; she can veto as sponsor (deliverable B, card 1; working; bears on SCE12, SCE15, SCE18). |
| SCE11 | Corvane | Ravi (IT director), Helene (chief financial officer) and Marek (site manager) sit on the selection committee; Ravi can veto on technical grounds, Helene on cost; Marek has no formal veto and his view reaches Edda (deliverable B, cards 2 to 4; working; bears on SCE12, SCE15, SCE18). |
| SCE11 | Corvane | Corvane has a procurement or purchasing function that runs the request to vendors and the contract; no one in it is named (deliverable B, card 5; working; bears on SCE12). |
| SCE11 | Corvane | An outside implementation partner would be proposed with a vendor's bid; none is named; if the vendor were Halvern Systems (fictional) it could be one of Halvern's partners (deliverable B, card 6; working, from the register's "implementation by its own services team and by partners"; bears on SCE12, SCE14). |
| SCE11 | Tandric Logistics | Karin (commercial director) is the executive sponsor of the selection and can veto (deliverable C, card 1; register for sponsoring; veto working). |
| SCE11 | Tandric Logistics | The register names no operations executive, IT leader, finance or procurement role; Anke (site manager) carries the operations voice, Dario (system administrator) stands in for the IT leader, and finance and procurement functions exist unnamed (deliverable C, cards 2 to 5; working; bears on SCE12, SCE14, DD-SCE1). |
| SCE11 | Tandric Logistics | Any outside integrator's work hands over to Luis, who configures each new client (deliverable C, card 6; working from the register; bears on SCE14). |
| SCE11 | Tandric Logistics | Luis, Priya and Olu use the systems daily and are not on the selection committee; the nine clients use the portal and sign nothing with the software vendor (deliverable C, closing line; section 4; working; bears on SCE13, SCE15). |
| SCE11 | Ostrel Foods | Aart (operations director) is read as likely both operations executive and sponsor of an execution-software purchase, as he is of the planning purchase in the planning course (section 4; inference; bears on SCE12). |
| SCE12 | Corvane | The long list for the warehouse-system replacement includes Halvern Systems (fictional) and Kestrow (fictional) (deliverable B, S2; this unit's assumption from the register's vendor rows and Corvane's two questions; bears on SCE14, SCE15, SCE17). |
| SCE12 | Corvane | The procurement function sends the RFI and runs the RFP; Edda and Ravi write the RFI questions; Edda, Ravi, Helene and Marek score their parts of the RFP (deliverable B, S3 and S4; working; bears on SCE14, SCE15). |
| SCE12 | Corvane | Corvane's legal counsel is consulted on contract terms at the RFP and the negotiation (deliverable B, S4 and S8; working; SCE11 card 5 already refers to Corvane's legal counsel; bears on SCE14, SCE16). |
| SCE12 | Corvane | Edda and Marek make the site visits; Ravi makes the reference calls on interfaces and support (deliverable B, S6; working; bears on SCE15). |
| SCE12 | Corvane | Whether Corvane runs a proof of concept is open; if it does, Ravi's team and Carla's stock records take part (deliverable B, S7; working; a register row only if SCE14 needs it). |
| SCE12 | Corvane | Whether Mina, Tobias or Carla attend the scripted demonstration is not in the register (deliverable B, S5; open; bears on SCE15). |
| SCE12 | Corvane | In negotiation, procurement leads and Edda sets the objectives, Helene can veto on cost, and the integrator, if any, is named in the implementation plan (deliverable B, S8; working, from SCE11 cards 3, 5, 6 and VITA's account in section 4; bears on SCE14, SCE16). |
| SCE12 | Corvane | Ravi takes part in the trigger; Edda and Ravi build the long list; Edda, Ravi and Marek attend the scripted demonstration (deliverable B, S1, S2, S5; working; bears on SCE15). |
