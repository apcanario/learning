# Case register: AI in Supply Chain Execution

The course reuses the track's three fictional operations and three fictional vendors, so a reader of both courses meets one case. This file is the course's own register: the setup row builds it by copying `courses/supply-chain-execution/notes/case-facts.md` as it stands on that day (its operations, people, vendors and "Added by units" rows), then appending the sections below. After that the two registers are separate files; a fact a unit of this course invents is appended here only.

Everything here is invented. Nothing in this file is evidence for a claim about the world, and no figure here is a benchmark.

Rules for every unit (in addition to the copied file's):
- No case operation is ever said to use a real vendor's product or a real company's model. A model behind a fictional feature is "a language model from an outside provider" or "a model trained on the customer's own history".
- No fictional vendor or feature stands for a real one. A unit never says or hints which real product one resembles.
- Every fictional claim below is a specimen for AIE11's claim sheet. It is never repeated as a finding.
- The setup row searches each new coined feature name once with the vendor name ("Halvern Assist", "Varnby Advisor", "Kestrow Smart Slotting") and renames any that matches a real product in logistics or enterprise software, in every file.

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
| Kestrow Smart Slotting | Kestrow WMS | Re-slots fast movers nightly |

## Added for this course: six fictional claims (specimens for AIE11)

Invented wording, written to show the kinds of claim. None is true of anything.

| # | Vendor | The claim as it appears on the fictional vendor's page | Kind it is meant to show |
|---|---|---|---|
| K1 | Halvern | "AI-powered wave planning" (the function is the rule-based wave builder it has sold for years) | A relabelled function |
| K2 | Halvern | "Assist resolves seven in ten carrier exceptions without a person" | A demonstration figure with no comparison |
| K3 | Halvern | "A fashion retailer cut picker travel by 22% in an eight-week pilot" | A pilot result with no baseline stated |
| K4 | Kestrow | "Smart Slotting cuts travel by a third" (from a simulation on one customer's order history) | A simulated result stated as a result |
| K5 | Varnby | "AI built into the ERP: no data to move, no risk" | A claim about risk with nothing to test |
| K6 | Varnby | "Our customers call Advisor a game changer" | A customer quotation |

## Added by units

Empty until the first unit of this course is filed. One row per fact: unit, operation, fact.

| Unit | Operation | Fact |
|---|---|---|
