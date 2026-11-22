# Case register: Supply Chain Planning for Product Teams

Three fictional companies and three fictional software vendors carry the course's worked examples. Everything here is invented. Nothing in this file is evidence for a claim about the world, and no figure here is a benchmark.

Written 21 Nov 2026 by the design chat (Fable 5.2) against `courses/supply-chain-execution/notes/case-facts.md` as it stood at commit abe5590. Corvane, Ostrel Foods and Varnby Software are the same companies as in the Supply Chain Execution course; their filed facts are repeated here unchanged and the planning facts are added under them. Where the two files ever differ on a shared fact, the Execution register wins.

Rules for every unit:
- Label each company "(fictional)" on first use in the unit.
- Take facts only from this file. A fact a unit invents is listed in its notes and appended to "Added by units" at filing.
- No case company is ever said to use a real vendor's product. Their systems are "the planning system", "the ERP", "the spreadsheet"; where a unit needs a named product, it is one of the fictional vendors' below.
- No fictional vendor stands for a real one. A unit never says or hints which real company one resembles.
- Names of people are first names only. They are roles to hang a card on, not characters.
- Tandric Logistics, Halvern Systems and Kestrow belong to the Execution course and are not named in this one.
- The names Pellward, Lathmoor and Ebbfield were coined for this course. The design chat searched each once on 21 Nov 2026 and found no company of that name in retail, appliances, food or software; the setup row searches each once more and replaces any that matches before a unit is written.

## Corvane (fictional): a fashion retailer

Filed facts, from the Execution register, unchanged:

| Fact | Value |
|---|---|
| What it sells | Clothing and accessories, own label, mid-priced |
| Channels | 60 stores in four European countries, one website |
| Distribution | One distribution centre of 28,000 m², one shift pattern of two shifts, a third in peak |
| Range | About 18,000 items (size and colour counted separately), two main seasons a year |
| Flows | Store replenishment by carton and by single item; web orders of one to three items; returns from web and from stores |
| Peak | Mid-November to early January; web volume about four times a normal week |
| Systems | An ERP, a warehouse system about twelve years old on its own servers, an order system for the website, carriers booked through each carrier's own portal |

Planning facts, added for this course:

| Fact | Value |
|---|---|
| Buying | Most of each season's range is ordered six to nine months ahead from suppliers in Asia and Turkey; a small part is bought close to the season from nearer suppliers |
| Range life | About a third of the range carries over between seasons (basics); the rest is new each season and has no sales history of its own; four smaller drops a year sit inside the two main seasons |
| Stock | Held in the distribution centre and in the 60 stores; a web order can be filled from either |
| Planning today | A merchandise financial plan in spreadsheets; first allocation to stores by store grade; store replenishment of basics proposed by the ERP and edited by allocators; end-of-season markdown decided in a weekly trading meeting |
| Known trouble | Stores graded on last year's sales receive the wrong sizes; basics run out in the best stores while slow stores hold them; markdown starts late |
| What it is deciding | Whether to buy a retail planning system, and whether allocation or the financial plan comes first |

People (the first three are the Execution register's):

| Name | Role |
|---|---|
| Edda | Vice-president, supply chain; sponsors the purchase |
| Helene | Chief financial officer |
| Ravi | IT director |
| Signe | Head of merchandise planning |
| Lorenzo | Merchandise planner, womenswear |
| Agnes | Allocator |
| Tomasz | Demand planner, basics and web |

## Ostrel Foods (fictional): a food distributor

Filed facts, from the Execution register, unchanged:

| Fact | Value |
|---|---|
| What it does | Buys from producers and delivers to restaurants, canteens and small shops |
| Range | About 4,500 items: chilled, frozen and ambient; most carry a date |
| Distribution | One warehouse with three temperature zones; picking by the case onto roll cages; work starts in the evening for delivery next morning |
| Delivery | Its own fleet of 40 vehicles, about 600 delivery points a day, fixed routes adjusted daily |
| Orders | By phone, by a web shop and from sales staff, with a cut-off in the late afternoon |
| Known trouble | Short-dated stock found too late; substitutions agreed by phone and not recorded; drivers returning with refused goods |
| Systems | An ERP with a warehouse module, a routing tool for the fleet, paper delivery notes on some routes |

Planning facts, added for this course:

| Fact | Value |
|---|---|
| Demand | A few hundred fast items and a long tail of slow items ordered by a few customers each; a strong weekly pattern, holiday peaks, and supplier promotions several times a year |
| Supply | Producers deliver on fixed days with minimum orders; chilled items have shelf lives counted in days |
| Planning today | One demand planner and a team of buyers who each own a set of suppliers; reorder proposals from the ERP, often overridden; forecast accuracy reported monthly at total level only |
| Known trouble | Waste on chilled items after promotions; shortages on slow items that matter to a few large customers; buyers do not trust the ERP's proposals |
| What it is deciding | Whether to buy a planning system for demand and replenishment |

People (the first is the Execution register's):

| Name | Role |
|---|---|
| Aart | Operations director; sponsors the purchase |
| Wim | Demand planner |
| Greta | Senior buyer, chilled |
| Samir | Replenishment analyst |
| Marta | Commercial manager, plans promotions |
| Joris | Finance director |

## Pellward (fictional): a maker of small kitchen appliances

New in this course.

| Fact | Value |
|---|---|
| What it makes | Kettles, toasters and blenders, assembled in one plant in Europe |
| Customers | Retailers, and its own web shop; two large retail customers send their own forecasts |
| Range | A few hundred finished items; two or three new models a year replace old ones |
| Components | Heating elements, motors and electronics from Asia with lead times of months; plastics and packaging from nearby suppliers with lead times of weeks |
| Demand | Seasonal, with a peak before the year-end holidays, and driven by retailers' promotions |
| Stock | Makes to stock; finished goods in one warehouse |
| Planning today | A monthly sales and operations meeting that mostly reviews last month; a master schedule kept in the ERP; requirements planning run weekly; component shortages handled by phone and spreadsheet |
| Known trouble | Sales, finance and operations each bring a different number; long-lead components ordered on a forecast nobody owns; the schedule changes daily in peak |
| What it is deciding | Whether its monthly process needs a planning system or a better meeting |

People:

| Name | Role |
|---|---|
| Elin | Demand planner |
| Otto | Master scheduler |
| Chiara | Supply planner |
| Pavel | Production scheduler |
| Ines | Material buyer |
| Hugo | Sales and operations planning lead; owns the monthly process |
| Vera | Sales director |
| Anton | Finance director |
| Birgit | Operations director; chairs the monthly meeting |

## The fictional vendors

Used wherever a unit maps a product line or builds a competitor sheet. Every module name is generic on purpose. No size, price, customer count or revenue is given for any of them until a unit needs one, and then it is added here marked fictional.

### Lathmoor (fictional): a planning suite specialist

| Fact | Value |
|---|---|
| Kind | Sells planning software and nothing else |
| Customers it names | Distributors, manufacturers and retailers, mid-sized to large |
| Line | Lathmoor Planning, with modules: Demand (statistical and machine-learning forecasting, planner review), Inventory (service targets and safety stock, one site or many), Replenishment (order proposals), Supply (master scheduling and requirements for manufacturers), Plan Review (the monthly cycle, scenarios) |
| Delivery | Cloud subscription; implementation by its own services team and by partners |
| What it says of itself | "One plan, from forecast to order" |

### Ebbfield (fictional): a retail planning specialist

| Fact | Value |
|---|---|
| Kind | Sells planning software to retailers only |
| Line | Ebbfield Retail, with modules: Merchandise Plan, Assortment, Allocation, Store Replenishment, Markdown |
| What it says of itself | "Built by merchants" |

### Varnby Software (fictional): an ERP vendor with planning modules

Filed facts, from the Execution register, unchanged: sells an ERP; names manufacturers and wholesalers already on its ERP as customers; says of itself "No integration to build".

| Fact | Value |
|---|---|
| Planning line, added for this course | Varnby Planning, sold with the ERP: a demand forecasting module, requirements planning, and a planning workbench; no separate retail planning |

## Added by units

Empty until the first unit is filed. One row per fact: unit, company, fact.

| Unit | Company | Fact |
|---|---|---|
