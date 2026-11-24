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
