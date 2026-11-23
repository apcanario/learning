# Case register: AI in Supply Chain Execution

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

## This course's additions: AI in Supply Chain Execution

Everything above is `courses/supply-chain-execution/notes/case-facts.md` as it stood on 23 Nov 2026 (commit 6a0e15b), copied by row S-AIE0 with only its title line changed; its "Added by units" table above is that course's and takes no new row from this course. Everything below is this course's own, from its design of 21 Nov 2026. After the copy the two registers are separate files: a fact a unit of this course invents is appended to the last table of this file, "Added by units" below, and nowhere else.

Rules for every unit (in addition to the copied file's):
- No case operation is ever said to use a real vendor's product or a real company's model. A model behind a fictional feature is "a language model from an outside provider" or "a model trained on the customer's own history".
- No fictional vendor or feature stands for a real one. A unit never says or hints which real product one resembles.
- Every fictional claim below is a specimen for AIE11's claim sheet. It is never repeated as a finding.
- The setup row searches each new coined feature name once with the vendor name ("Halvern Assist", "Varnby Advisor", "Kestrow Smart Slotting") and renames any that matches a real product in logistics or enterprise software, in every file. (S-AIE0, 23 Nov 2026: "Halvern Assist" and "Varnby Advisor" matched no product; "Smart Slotting" is the name of real slotting products and services in logistics, so Kestrow's feature was renamed "Kestrow Nightly Re-slot", a name that search found no product under.)

## Added for this course: people

| Name | Operation | Role |
|---|---|---|
| Ines | Corvane | Continuous-improvement analyst in the distribution centre: owns the labour standards, the slotting reviews and the reports |
| Teun | Ostrel Foods | Warehouse planner: plans the evening's labour and the pick sequence |

## Added for this course: how decisions are made today

| Operation | Decision | Today |
|---|---|---|
| Corvane | Slotting | Reviewed by Ines twice a year at season change, from a spreadsheet |
| Corvane | Batching and release | Waves built by the warehouse system on fixed rules; Tobias re-orders them by hand near carrier cut-offs |
| Corvane | Task assignment | Tobias and the team leads, from a board; no labour module |
| Corvane | Labour for a shift | Marek and Ines, from last year's volumes and the agency's notice period |
| Corvane | Delivery promise on the website | A fixed number of days by country, set in the order system |
| Corvane | Which location ships a web order | The distribution centre unless it shows no stock; then the nearest store, by a rule |
| Ostrel Foods | Route building | Sofia, in the routing tool, from fixed routes adjusted each afternoon |
| Ostrel Foods | Short-dated stock | Found by Ilse's team during picking; no report ahead of time |
| Ostrel Foods | Substitutions | Agreed by phone by Nuno or the sales staff |
| Tandric Logistics | Carrier choice for a load | Priya, from a routing guide per client and her own knowledge of carriers |
| Tandric Logistics | Freight invoice checks | Priya, line by line against the agreed rate |
| Tandric Logistics | Client questions | Olu, by email and the client portal |

## Added for this course: the fictional AI features

Every module name is generic on purpose. "Family" and "rung" are left for the units to assign from AIE1's keys.

### Halvern Systems (fictional)

| Feature | Sold with | What Halvern says it does |
|---|---|---|
| Slotting suggestions | Halvern Warehouse, Slotting module | Proposes moves each week from recent picks |
| Task assignment | Halvern Warehouse, Labour module | Sends each operator the next task and reorders the queue through the shift |
| Labour forecast | Halvern Warehouse, Labour module | Predicts the hours each area needs for the next shifts |
| Predicted arrival | Halvern Transport, Tracking module | Gives an arrival time for each shipment and flags the late ones |
| Invoice anomaly flags | Halvern Transport, Freight Audit module | Marks carrier invoices that depart from the agreed rate or from past invoices |
| Predicted promise date | Halvern Order, Promising module | Shows a delivery date per order line from past deliveries |
| Halvern Assist | All three lines | Answers questions in plain language over the customer's operational data and drafts messages |
| Freight-desk agent | Halvern Transport, add-on | Reads carrier emails, proposes or books a carrier, and chases missing documents |

### Varnby Software (fictional)

| Feature | Sold with | What Varnby says it does |
|---|---|---|
| Varnby Advisor | The ERP, across modules | Answers questions and proposes transactions inside the ERP |

### Kestrow (fictional)

| Feature | Sold with | What Kestrow says it does |
|---|---|---|
| Kestrow Nightly Re-slot | Kestrow WMS | Re-slots fast movers nightly |

## Added for this course: six fictional claims (specimens for AIE11)

Invented wording, written to show the kinds of claim. None is true of anything.

| # | Vendor | The claim as it appears on the fictional vendor's page | Kind it is meant to show |
|---|---|---|---|
| K1 | Halvern | "AI-powered wave planning" (the function is the rule-based wave builder it has sold for years) | A relabelled function |
| K2 | Halvern | "Assist resolves seven in ten carrier exceptions without a person" | A demonstration figure with no comparison |
| K3 | Halvern | "A fashion retailer cut picker travel by 22% in an eight-week pilot" | A pilot result with no baseline stated |
| K4 | Kestrow | "Nightly Re-slot cuts travel by a third" (from a simulation on one customer's order history) | A simulated result stated as a result |
| K5 | Varnby | "AI built into the ERP: no data to move, no risk" | A claim about risk with nothing to test |
| K6 | Varnby | "Our customers call Advisor a game changer" | A customer quotation |

## Added by units

Empty until the first unit of this course is filed. One row per fact: unit, operation, fact.

| Unit | Operation | Fact |
|---|---|---|
