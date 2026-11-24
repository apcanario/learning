---
code: SCE5
title: "The floor: people, devices and machines"
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-24
search: off
intro: SCE5 covers the people on the warehouse floor and the machines beside them. It takes the five roles one by one (operator, team lead or supervisor, inventory controller, planner, site manager): who they are, what they are measured on, their pace and conditions, and what they do when the system is wrong; then who works the floor and how long it takes to learn, devices as working conditions, labour management (standards, tracking, incentives, bucket brigades), gamification as vendors describe it, the machines a warehouse system works with, the control software (WCS, WES) and where the line to the WMS runs, and common claims C3, C5 and C6 set against the evidence. Its deliverable is the role card form, five role cards for Corvane and Ostrel Foods (fictional), the template for a card, and glossary lines. Written 24 Nov 2026 by Opus 5.5 with search off (references still opened live, all on 24 Nov 2026), then given a fresh check (fix: 2 errors, 8 should-fix, 5 minor) and a quality review (fix: 0 errors, 4 should-fix, 14 minor) by separate Opus 5.5 agents, their findings applied: all 15 of the fresh check's, with 12 extra fixes (X1 to X12), and 17 of the quality review's 18 by the applier, the eighteenth (f2, the unsure list) merged into the Unsure list by hand. Held: none. Known gaps: the research opened is thin on the people, so most of the role descriptions are working descriptions or practice. No source was opened on shift patterns, the share of temporary or agency staff, training time for warehouse roles across sites, or cold-store conditions. The register has no warehouse planner, so Ostrel Foods' transport planner, Sofia, stands in for the planner. The incentive numbers are from de Vries, de Koster and Stam's 2015 working paper; the published 2016 abstract reports no effect on quality, while the working paper reported error rates that differed by condition. Grosse et al. (2017), Grosse and Glock (2013), de Vries et al. (2016, IJPR and POMS), Azadeh et al. (2019) and Fragapane et al. (2021) were read in abstract only. No public figure for the cost of goods-to-picker equipment was found. The regional use of the ISO 6780 pallet sizes (Annex A) was not read. WCS and WES are defined from one analyst's article (Interact Analysis, 2023); no peer-reviewed or standards-body definition was found. C3 rests on US Census data for 2012, with the other expense lines not opened, so whether labour is the largest cost is not shown.
---

# SCE5 · The floor: people, devices and machines

SCE2 to SCE4 followed goods and records through the building. This unit follows the people: who does the work, what they are measured on, what they hold in their hands, and what they do when the system is wrong. Then it turns to the machines the warehouse system has to work with and the control software between the two. Grades follow SCE1's key (section 10 there): **independent**, **analyst**, **vendor-reported**, **practice**. Where a line rests on no opened source, it says so and is called a **working description**: the course's own account, graded nothing, never used as evidence.

One limit holds through the unit. The research opened is thin on the people. Grosse, Glock and Neumann's content analysis of the order-picking literature found that management-oriented efficiency criteria dominated it, with "a clear lack of attention" to human factors in the design and management of picking systems ([2017, abstract](https://doi.org/10.1080/00207543.2016.1186296)) [independent]. Most of what follows on roles is therefore a working description or practice, and the unit says which.

## 1. The roles, one by one

A warehouse's floor work is done by **operators**; the shift is run by a **team lead** or **supervisor**; the stock record is kept by an **inventory controller**; the work is planned by a **planner**; the site is run by a **site manager**. Job titles vary by company and region. This list is the course brief's, and the descriptions below are working descriptions except where a source is cited.

### 1.1 Operator

**Who.** The person who receives, puts away, replenishes, picks, packs or loads (SCE2 §3, SCE3 §3). In US federal statistics the largest occupations in the warehousing and storage industry in 2025 were stock clerks and order fillers (457,740 employed), hand laborers and freight, stock and material movers (433,060), and industrial truck and tractor operators (286,750) ([BLS, Industries at a Glance, NAICS 493](https://www.bls.gov/iag/tgs/iag493.htm), data extracted 20 Nov 2026) [independent]. These are US figures for one industry classification; this unit reads it as companies whose business is warehousing, with warehouses run by retailers and manufacturers for themselves counted in their owners' industries (not checked against the NAICS definition). No European equivalent was opened.

**Measured on.** Pace, above all. Bartholdi and Hackman write that most warehouses track picker productivity and so can report average picks per person-hour (B&H §3.3) [practice]. In their bucket-brigade chapter a site's pick rate is reported as a fraction of the **work standard**, the expected rate for a task (Fig. 11.6) [practice]; Bartholdi and Eisenstein, describing zone picking at one chain retailer's distribution centre, write that individual workers' pick rates "typically range from 50% to 200% of work standard" ([1996](https://www2.isye.gatech.edu/~jjb/bucket-brigades/papers/bbwh.pdf)) [practice: one site, the authors' report]. Accuracy is the second measure: SCE3 §12 lists WERC's picking-accuracy measure and B&H's warning that lines per labour hour is biased by unit of measure.

**Pace and conditions.** The work is physical and repetitive. Order picking is "one of the most labour- and time-intensive processes" in internal logistics (Grosse et al., 2017, abstract) [independent]. In the United States, warehousing and storage recorded 4.5 injury and illness cases (total recordable cases) per 100 full-time workers in 2025 ([BLS, Industries at a Glance, NAICS 493](https://www.bls.gov/iag/tgs/iag493.htm), data extracted 20 Nov 2026), against 2.3 total recordable cases per 100 full-time equivalent workers for private industry as a whole; the release gives warehousing's injury-only rate as 4.4, down from 4.6 in 2024 ([BLS, 18 Nov 2026](https://www.bls.gov/news.release/osh.htm)) [independent]. The release does not state the survey's sample in what was read. No source was opened on cold-store conditions (Ostrel's chilled and frozen zones), on noise, or on night work. Which rules on manual handling, working time and cold work apply to a site is a question for the national labour inspectorate (in the EU, also the EU-OSHA guidance for that country) or, in the US, OSHA.

**When the system is wrong.** The operator meets the error first: a location empty where the record says stock (SCE4 §4), a label that will not scan, a task that sends them to the wrong aisle. Their options are those the device gives them: report a short, skip, or call the team lead (SCE4 §9 traced one short pick at Corvane (fictional) to a service call). Working description.

### 1.2 Team lead or supervisor

**Who.** Runs a shift or a zone: assigns people to work, watches the backlog against the cut-off (SCE3 §8), clears exceptions. Working description.

**Measured on.** The shift's output against its plan, and its departures. The measures are SCE3 §12's (orders shipped on time, lines per person-hour) summed over the team. Working description; no source opened defines a supervisor's measures.

**Pace and conditions.** On their feet, between the floor and a screen. No source opened describes the role's day.

**When the system is wrong.** They move people between zones, hold or re-release work, and decide whether a short pick goes out short. The bucket-brigade papers show one thing supervisors do that a system does not: Bartholdi and Eisenstein report that management sequenced workers and had to "persuade workers" that local changes were not improvements ([1996](https://www2.isye.gatech.edu/~jjb/bucket-brigades/papers/bbwh.pdf)) [practice: one site].

### 1.3 Inventory controller

**Who.** Keeps the stock record true: plans counts, investigates discrepancies, posts adjustments (SCE4 §5).

**Measured on.** Inventory accuracy by WERC's measures, with SCE4 §10's caveats about definition and netting.

**When the system is wrong.** This is the role whose job is the system being wrong. Who may count and who may approve an adjustment (flag F44) was left unsourced in SCE4 §5. The nearest acceptable source opened here is a standard for public bodies: the US Government Accountability Office's draft revision of its internal control standards lists, as a control activity, "separating the responsibilities for authorizing transactions, processing and recording them, reviewing the transactions" and handling any related assets, and names physical control over "cash, securities, inventories, and equipment" (GAO-24-106889, June 2024 exposure draft, para. 10.04) [independent, for what the text says]. GAO issued the final revision (GAO-25-107721) on 15 May 2025, effective from fiscal year 2026, superseding the 2014 edition; its para. 10.04 keeps both passages quoted here ([GAO-25-107721](https://www.gao.gov/products/gao-25-107721), read 24 Nov 2026; the text read in a copy posted by Thompson Grants) [independent, for what the text says]. The standards bind US federal executive-branch entities and may be applied by state, local and nonprofit bodies (draft OV2.01, OV4.17; these paragraphs were not checked in the final text). Applying them to a company's warehouse is this unit's inference: the person who picks from a location should not be the one who approves the adjustment to it, and the person who approves should not be the one who posts it unreviewed. Which separation a company's controls require is a question for its auditors and finance team.

### 1.4 Planner

**Who.** Turns tomorrow's expected volume into a labour plan and a release plan: how many people, on which shift, in which zones, released in which order (SCE3 §2). In a site whose outbound is driven by delivery routes, the route plan sets the release (SCE3's register note on Ostrel Foods (fictional): picking is released by route after the cut-off). Working description; no source opened describes the warehouse planner's role.

**Measured on.** Whether the plan held: hours planned against hours used, work finished by cut-off. Working description.

**When the system is wrong.** A forecast of volume that is wrong leaves the plan wrong; the planner changes it by calling agencies, moving breaks or changing the release order. Working description.

### 1.5 Site manager

**Who.** Answers for the building's cost, service, safety and people.

**Measured on.** Cost per unit handled, service (on-time, accurate shipments), injuries and staff turnover. Working description; SCE16 takes up cost.

**When the system is wrong.** Decides whether a workaround becomes the process, and whether to spend on a fix. Working description.

## 2. Who works the floor, and how long it takes to learn

**Headcount and shifts.** US employment in warehousing and storage was 1,839.2 thousand in October 2026 (preliminary, seasonally adjusted) (BLS, Industries at a Glance) [independent]. No source was opened on shift patterns, on the share of temporary or agency staff in warehouses, or on peak staffing, so the unit gives no figure. The case register gives one fictional example only: Corvane's (fictional) centre runs two shifts, a third in peak, with about 140 staff in a normal week and about 260 in peak, the difference from agencies. That is a case fact, never a benchmark. Whether agency workers in a given country must be paid or treated like permanent staff is a question for that country's labour ministry or inspectorate.

**How long it takes to learn.** No source opened gives a training time for warehouse roles across sites. Three narrower findings:

- **Learning happens and can be modelled.** Grosse and Glock ran an experimental study at a manufacturer of household products and found that "learning occurs in order picking"; several learning-curve models fitted the data, and two gave unrealistic results ([2013, abstract](https://doi.org/10.1108/JMTM-03-2012-0036)) [independent: one site; the abstract gives no learning rates].
- **Experience reduces search time.** Batt and Gallino found the effect of hard search on pick times fell with experience (SCE3 §9, abstract) [independent].
- **Some work methods need almost no training.** At the chain retailer, the authors described the bucket-brigade rule to the workers in fifteen minutes, and "within a half-hour they were picking comfortably"; the authors also say temporary workers "can become productive more quickly" under the method (Bartholdi & Eisenstein, 1996) [practice: one site, the authors' report].

For a product team, the gap matters: claims about how fast a new or seasonal worker becomes productive on a device or screen rest, in what was opened, on single sites.

```viz
{"kind": "compare", "title": "Total recordable injury and illness cases per 100 full-time workers, US, 2025", "unit": "", "max": 5, "rows": [{"label": "Warehousing and storage", "value": 4.5}, {"label": "Private industry, all", "value": 2.3}], "caption": "Section 1.1 of this unit. Data: US Bureau of Labor Statistics, Survey of Occupational Injuries and Illnesses: warehousing and storage from Industries at a Glance, NAICS 493 (data extracted 20 November 2026); private industry from the news release of 18 November 2026. US only."}
```

## 3. Devices as working conditions

A device is where the operator meets the system. Each one fixes what the operator carries, where their eyes and hands are, and how they confirm a task. The descriptions are working descriptions; the research findings are cited.

| Device | What the operator does with it | Working description of the condition it sets |
|---|---|---|
| Paper list | Reads the next line, marks it done | Hands busy with the list; no confirmation until keyed in later |
| Handheld scanner (RF terminal) | Reads the task on a screen, scans location and item to confirm | One hand holds the device; eyes move between screen and shelf |
| Vehicle-mounted terminal | Screen fixed on a reach or fork truck | Driver reads while seated; the task list follows the truck |
| Wearable (ring scanner, wrist screen) | Scans with a finger-mounted reader | Both hands nearly free; small screen |
| Voice | Hears the location, speaks a check digit and quantity | Hands and eyes free; the pace is set by the dialogue |
| Pick-to-light | A light on the location shows where and how many; a button confirms | Fixed to the rack; suits zones with many picks close together |
| Desktop | Supervisors, planners and controllers at a screen | Seated; the place where exceptions are cleared |

**What the research studied.** One field experiment compared the tools directly. De Vries, de Koster and Stam ran 101 participants (academic students, vocational students and professional pickers) through pick by voice, RF-terminal picking and pick to light, with three picking methods. Their results "suggest that (PbV) performs better than RF-terminal picking"; personality traits (Neuroticism, Extraversion, Conscientiousness) and age predicted performance with voice and RF terminals; and higher productivity "appears to be possible without sacrificing quality" ([2016, IJPR, abstract](https://doi.org/10.1080/00207543.2015.1064184)) [independent: one experiment, abstract only]. The abstract does not give the size of the difference.

**What it has not studied, in what was opened.** No opened study measures vehicle-mounted terminals, wearables or desktop screens; none follows a device over months on a working site; none measures fatigue or injury by device. Grosse et al.'s finding that human factors are largely absent from picking research (2017, abstract) [independent] is the general form of this gap. Grosse et al.'s full text, which would say which human factors were studied, was not opened; only its abstract was read.

**C5, the voice claim.** The claim as it circulates: voice picking brings accuracy to 99.9% or raises productivity by a fixed percentage. The one independent study opened found voice performing better than RF terminals in an experiment, without stating a percentage in its abstract (above) [independent]. No source opened gives 99.9% accuracy for voice; one vendor page that might have stated a figure served no article text (source log). No independent source found for either number.

## 4. Labour management: standards, tracking, incentives

**Engineered standards.** A **labour standard** (or work standard) is the expected time or rate for a task; an **engineered** standard is one built from measured elements of the task (travel, reach, scan) for each task's conditions. B&H report pick rates as a fraction of the work standard (Fig. 11.6) [practice]. No textbook or study defining engineered standards was opened, so the definition is a working one. On a vendor's website, an article dated 3 June 2021 says labour management systems "based on engineered labor standards have some of the attributes of gamification, but not all of them" ([Banker, Manhattan Associates website](https://www.manh.com/our-insights/resources/articles/key-attributes-robust-gamification-program-in-labor-management)) [vendor-reported].

**Performance tracking.** The system records each task's start, finish and user, so a rate per person per hour can be set against the standard (B&H §3.3, picks per person-hour) [practice]. Gartner's glossary definition of a warehouse management system lists "labor management" among its capabilities ([Gartner glossary, WMS](https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/warehouse-management-system-wms), read 24 Nov 2026) [analyst; vendors license Gartner's reprints].

**Incentives and picking methods: what the research found.** De Vries, de Koster and Stam ran a controlled field experiment "in a warehouse erected especially for the purposes of order picking research", crossing three manual picker-to-parts methods (parallel, zone and dynamic zone picking) with two incentive systems ([2016, POMS, abstract](https://doi.org/10.1111/poms.12547)) [independent]. In the 2015 working-paper version, read in full, the design was 3×2 between subjects with 142 participants in 48 teams of three: 28 university students, 39 professional warehouse employees and 75 vocational logistics students. A **competition-based** system paid an individual bonus to the top four performers; a **cooperation-based** system paid a team bonus to the best team. Each team had a 10-minute practice run and a 10-minute recorded run, every team on the same set of orders, with order lines counted per participant ([de Vries et al., 2015](https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf)) [independent].

The findings, in the published abstract: in parallel picking, where each picker completes whole orders, competition raised productivity; in zone picking, where pickers hand orders on, cooperation did; this was "especially pronounced" for pickers with a dominant promotion focus; prevention-focused pickers were more productive in zone picking under cooperation; and "No effects on order picking quality were identified" (2016, abstract) [independent]. The 2015 working paper, the source of the numbers that follow, reported error rates that differed by condition (zone picking: least-squares means of 19.1% of orders with an error under competition, 31.6% under cooperation) and said it investigated quality "from a more exploratory perspective"; whether the published full text keeps these results was not checked. In the working paper's model estimates (least-squares means of order lines picked per participant), parallel pickers reached 53.9 under competition against 46.84 under cooperation, which the paper indexes as a 15.2% gain; zone pickers reached 47.58 under cooperation against 35.37 under competition, indexed as a 34.3% gain; dynamic zone reached 41.03 under competition against 43.91 under cooperation, "hardly any differences" (2015) [independent]. Sample and setting matter: 20 minutes per team, a purpose-built warehouse, and students as well as professionals. Applying the result to a working site with eight-hour shifts is the reader's inference to test, and a bonus scheme's legality and fairness are questions for the employer's legal and HR advisers.

```viz
{"kind": "bars", "title": "Order lines picked in the recorded run, by method and incentive (least-squares means)", "mode": "grouped", "unit": "", "series": [{"name": "Competition-based", "tone": 4}, {"name": "Cooperation-based", "tone": 2}], "rows": [{"label": "Parallel", "values": [53.9, 46.84]}, {"label": "Zone", "values": [35.37, 47.58]}, {"label": "Dynamic zone", "values": [41.03, 43.91]}], "decimals": 2, "caption": "Section 4 of this unit. Least-squares means of order lines picked per participant in a 10-minute recorded run, 142 participants in 48 teams, in a warehouse built for picking research. Data: de Vries, de Koster and Stam, ERIM working paper ERS-2015-009-LIS (2015), the version before the 2016 POMS article."}
```

**Bucket brigades (flag F44).** A **bucket brigade** changes how work is divided among pickers: each picker carries work forward "until someone takes over your work; then go back for more" (B&H §11.1) [practice]. Sequenced from slowest to fastest, the line rebalances itself (B&H Theorem 11.1); otherwise it may "sputter" (§11.1) [practice]. B&H §11.2 reports a major retailer's national distribution centre where picks per person-hour rose over 30% with no change to layout, equipment or control system, and a major US distributor of recorded music where the average pick rate rose about 20% and its variance fell about 90% (Figs 11.6, 11.7) [practice]. Bartholdi and Eisenstein's paper on the first site says pick rates "reached sustained levels over 30% greater than the previous historical averages", that the change needed "no changes to a typical warehouse management system", and that at the music distributor an operations manager reported an increase in pick rate of over 50% within a day (1996) [practice: one site each, the authors' report]. The two documents give different figures for the music distributor (20% average in the book; over 50% within a day as a manager reported it in the paper); they measure different things over different periods. For software, the point is what the method removes: no one computes a balance of work across zones (B&H §11.2) [practice].

## 5. Gamification as vendors describe it

**What vendors say.** Two vendor pages were opened; each gets one sentence here. One vendor page (undated, © 2026) says gamification "uses game mechanics and rewards/recognition tools to digitally engage employees", through leaderboards, badges, points, rewards or challenges, and that its product "can improve warehouse productivity by up to 7%", with no basis stated ([a warehouse-software vendor, "What is warehouse gamification?"](https://www.infios.com/en/supply-chain-solutions/gamification/what-is-gamification)) [vendor-reported]. The article dated 3 June 2021 on another vendor's website (Banker, section 4) quotes Peter Schnorbach, senior director of product management at Manhattan Associates, saying that a labour management system "has no gamification", that a program can be built around one (posting results, rewarding high performers), and that without transparency and real-time feedback such programs "tend to fall short" [vendor-reported]. Both are evidence of what vendors claim. Neither is evidence of what a product does.

**What independent work found.** Bahr, Mavrogenis and Sweeney screened 47 articles from one database and found "only five" on gamification in warehousing; they interviewed eight UK warehousing managers (one a head of logistics), each with at least four years' experience, and found interest and significant barriers (resources, efficacy over time, ethics). They call the study exploratory and say generalisation "is impossible" ([2021, accepted manuscript](https://doi.org/10.1080/13675567.2021.1892042)) [independent]. They report Bräuer and Mazarakis's warehouse experiments with badges and leaderboards as finding that competitive elements could have unintended negative side effects, such as a feeling of incompetence among workers (Bahr et al., §2.4) [practice: origin not opened]. Putz, Hofbauer and Mates surveyed 17 full-time pickers at one Austrian shipping company in 2018 with vignettes; the pickers rated individual and group gamified feedback about alike for fun, performance and motivation ([2019](https://ceur-ws.org/Vol-2359/paper14.pdf)) [independent: 17 respondents, stated preferences].

**C6, the gamification claim.** As it circulates: gamification raises warehouse productivity by a stated percentage. The one percentage opened ("up to 7%") is a vendor's, with no basis given [vendor-reported]. No independent test of gamification's effect on warehouse productivity was opened. The nearest independent evidence is de Vries et al.'s (section 4): the same competitive incentive raised productivity in one picking method and lowered it in another. That supports asking, of any leaderboard, which work method it is used with. No independent source found for a productivity percentage.

## 6. The machines a warehouse system works with

The review literature describes the machines; it says less about the people next to them. What each changes for people and software is stated from the reviews where possible and otherwise as this unit's inference.

**Pallets: the unit the machines are built around (flag F24).** ISO 6780:2003 lists six plan sizes for flat pallets in intercontinental handling: rectangular 1200 × 800 mm, 1200 × 1000 mm and 1219 × 1016 mm (48 × 40 in), and square 1067 × 1067, 1100 × 1100 and 1140 × 1140 mm (clause 4.1, Tables 1 and 2) [independent, for what the standard says]. ISO's page says the standard was last reviewed and confirmed in 2026 ([ISO 6780:2003](https://www.iso.org/standard/30524.html), read 24 Nov 2026). The standard gives each size's regional use in its Annex A, which was not in the part read. So this unit does not say which size dominates in Europe or North America; racking, conveyors and robots are specified to the pallet the region uses, and a product that stores pallet dimensions should not assume one (this unit's inference).

**Conveyors and sorters.** SCE3 §3.5 sets out pick-and-sort: pickers pick in batches to a conveyor and a sorter divides items into orders. For people, picking becomes batch work by article and the order is assembled downstream; for software, the warehouse system releases batches and someone must tell the sorter which lane each item goes to (SCE3 §3.5) [practice].

**Goods-to-person.** SCE3 §3.7 names parts-to-picker systems: automated storage and retrieval systems (AS/RS), miniloads, vertical lift modules, carousels. Azadeh, de Koster and Roy's review covers newer robotised systems, including shuttle-based storage and retrieval, shuttle-based compact storage and **robotic mobile fulfilment** (robots that carry storage racks to stations). In their abstract such systems need little space, adapt to changing demand and can run around the clock; many are used in practice with little academic study; and standard decisions (layout, storage assignment, batching, routing) need revisiting for robotised warehouses ([2019, abstract](https://doi.org/10.1287/trsc.2018.0873)) [independent: a review, abstract only, summarised]. For people, the picker stops walking and works at a station at the machine's pace; for software, the system must decide which storage unit comes to which station when (this unit's inference from SCE3 §3.7 and the review's list of decisions). **Cost (flag F44):** no public figure was found for the cost of goods-to-person equipment; the price of a private supplier's system is not stated.

**Mobile robots.** Fragapane, de Koster, Sgarbossa and Strandhagen contrast two kinds. In an **automated guided vehicle (AGV)** system "a central unit takes control of scheduling, routing, and dispatching decisions for all AGVs"; **autonomous mobile robots (AMRs)** "can communicate and negotiate independently with other resources" and so decentralise decisions ([2021, abstract](https://doi.org/10.1016/j.ejor.2021.01.019)) [independent: a review, abstract only]. For people, robots share aisles with walking pickers; for software, the difference is where the decision lives: in a central controller, or spread across robots that a warehouse system can only give tasks to (this unit's inference from the abstract).

## 7. The control software, and where the line runs

**The terms (flag F5).** An analyst at Interact Analysis defines **warehouse control systems (WCS)** as systems "used to control the flow of goods across fixed automation", and **warehouse execution software (WES)** as software "used to optimize workflows by controlling the timing and location of order processing"; a WES "orchestrates the timing and location of warehouse workflows in order to optimize throughput" ([Scriven, *Supply & Demand Chain Executive*, 22 Feb 2023](https://www.sdcexec.com/home/article/22724398/interact-analysis-warehouse-execution-systems-vs-warehouse-control-systems)) [analyst: a signed article by the firm's analyst in a trade magazine, read in full; not an analyst report, used because no listed kind of source defining either term was found]. No peer-reviewed or standards-body definition of either term was found.

**Where the line is drawn.** In the same article, WES that "sit above the WCS" are called embedded WES, and "most eWES solutions are truly 'embedded' into the WMS", while some are sold standalone [analyst]. Gartner's glossary definition of a WMS includes "task interleaving, wave planning", "labor management, yard management and automated materials handling equipment interfaces" [analyst]. Read together: the WMS holds the stock record and each order's pick lists and progress, while the customer order itself sits in the order system (SCE1 §3); the WCS drives the equipment; the WES decides when and where work flows; and the two analyst sources place parts of that middle layer inside the WMS. This unit found no source that settles which layer owns release, task assignment or the robot queue.

**Where it is disputed.** The dispute is over the middle decisions: release and wave planning (SCE3 §2), which station or robot gets which task, and which person does what next. A WMS vendor can claim them as WMS functions (Gartner's list includes wave planning and labour management); an automation supplier can claim them as WES. The AGV and AMR contrast moves the same line further down: with AMRs, some dispatch decisions sit in the robots themselves (Fragapane et al., 2021, abstract) [independent]. This paragraph is the unit's reading of the three sources.

**On the case register.** Halvern Warehouse (fictional) sells an Automation Connect module; Kestrow WMS (fictional) has none. Case facts, graded nothing; they say nothing about real products. Map a real product the same way: read its public pages for which of release, task assignment and equipment control it claims, and grade each line vendor-reported.

```viz
{"kind": "flow", "title": "Layers between the order and the machine", "steps": [{"label": "WMS", "note": "stock record, pick lists; per Gartner also wave planning, labour, equipment interfaces"}, {"label": "WES", "note": "timing and location of workflows; embedded WES sit above the WCS, most inside the WMS"}, {"label": "WCS", "note": "flow of goods across fixed automation"}, {"label": "Equipment", "note": "conveyors, sorters, AS/RS, shuttles"}], "caption": "Section 7 of this unit. The layers as Interact Analysis's analyst describes them (Scriven, 22 February 2023) with Gartner's glossary definition of a WMS (read 24 November 2026). The boundaries are the sources' and are disputed; mobile robots (AMRs) can hold some decisions themselves (Fragapane et al., 2021)."}
```

## 8. C3: is labour the largest cost in a warehouse?

**The claim as it circulates.** Labour is the largest cost in a warehouse.

**What was opened.** The US Census Bureau's Service Annual Survey, a probability sample of US firms with paid employees ([methodology](https://census.gov/programs-surveys/sas/technical-documentation/methodology.html)), reported for the warehousing and storage industry (NAICS 493) in 2012: total expense $23,883 million, gross annual payroll $7,975 million, and all other operating expenses $4,388 million (Census Bureau data as published by FRED: [total](https://fred.stlouisfed.org/data/EXPEF493ALLEST), [payroll](https://fred.stlouisfed.org/data/EXPGAPEF493ALLEST.txt), [other](https://fred.stlouisfed.org/data/EXPAOOEF493ALLEST)) [independent]. Payroll was about a third of total expense (this unit's arithmetic: 7,975 / 23,883). The total-expense series was discontinued after 2012. Payroll excludes employers' benefit costs, which the same survey put at $1,895 million in 2012 ([FRED, EXPECFEF493ALLEST](https://fred.stlouisfed.org/data/EXPECFEF493ALLEST)) [independent]; payroll and benefits together were about 41% of total expense (this unit's arithmetic: 9,870 / 23,883). The other detail lines (rent, depreciation and the rest, $9,625 million together by subtraction) were not opened, so whether labour is the largest single line is not shown.

**What the evidence shows.** In the one independent series opened, payroll alone was about a third of US warehousing firms' total expense in 2012, larger than the "all other operating expenses" line. The industry is firms whose business is warehousing; in-house warehouses and Europe are not covered, and applying the share to them is inference. SCE3 traced the related claim that picking is over half of operating cost (C2) to textbooks [practice]. No independent source found that ranks labour against every other cost of a warehouse.

```viz
{"kind": "compare", "title": "US warehousing and storage firms, expense lines opened, 2012 ($ million)", "unit": "", "max": 12000, "rows": [{"label": "Gross annual payroll", "value": 7975}, {"label": "All other operating expenses", "value": 4388}, {"label": "Employer's cost for fringe benefits", "value": 1895}, {"label": "Other lines, not opened (by subtraction)", "value": 9625}], "caption": "Section 8 of this unit. Total expense was $23,883 million. Data: US Census Bureau, Service Annual Survey, NAICS 493, employer firms, as published by FRED (series EXPEF493ALLEST, EXPGAPEF493ALLEST, EXPECFEF493ALLEST, EXPAOOEF493ALLEST); the third bar is this unit's subtraction and mixes several lines."}
```

## 9. The common claims of this unit

| # | Claim as it circulates | What this unit found | Grade of the best evidence |
|---|---|---|---|
| C3 | Labour is the largest cost in a warehouse. | US Census data, 2012: payroll about a third of warehousing firms' total expense, payroll with benefits about 41%; other lines not opened; no source ranks all lines (section 8). | independent (partial) |
| C5 | Voice picking brings accuracy to 99.9% or raises productivity by a fixed percentage. | One field experiment (101 participants): voice performed better than RF terminals, no percentage in the abstract; no source opened gives 99.9% (section 3). No independent source found for either number. | independent (abstract) |
| C6 | Gamification raises warehouse productivity by a stated percentage. | One vendor's "up to 7%", no basis; independent work is exploratory (eight managers; 17 pickers); an incentive experiment shows competition helps or hurts by picking method (sections 4, 5). No independent source found for a percentage. | vendor-reported |

## On a site visit

- **Walk one picker's hour.** Watch the device: how many hands it takes, where the eyes go, how a task is confirmed, what happens on a short (sections 1.1, 3).
- **Ask what the standard is for that task, and how it was set.** Measured elements or last year's average? What rate counts as 100% (section 4)?
- **Ask how bonuses are paid, and to whom.** Individual or team, and with which picking method; set the answer against de Vries et al. (section 4).
- **Look for a leaderboard.** What it ranks, who sees it, and whether anyone has measured its effect here (section 5).
- **Ask who approves an adjustment, and whether that person ever picks or counts the location** (section 1.3).
- **Ask how long a new agency worker takes to reach standard on each device, and how that was measured** (section 2).
- **At the automation, ask which system decides which tote goes to which station, and which system owns the order when the machine stops.** Ask for the interface list between the WMS and the control software (sections 6, 7).
- **Read the pallet labels and the rack specification: which pallet size is the building built for** (section 6)?

## Self-check

1. **What did Grosse, Glock and Neumann (2017) find about the order-picking literature?**
   Management-oriented efficiency criteria dominated it, and there was a clear lack of attention to human factors (introduction and section 3; abstract).
2. **In de Vries et al.'s incentive experiment, which incentive raised productivity with which method, and what happened to quality?**
   Competition-based with parallel picking; cooperation-based with zone picking. The published abstract reports no effects on quality; the 2015 working paper reported error rates that differed by condition (section 4).
3. **What are the sample and setting of that experiment, and why does it matter?**
   142 participants in 48 teams (working paper), students and professionals, 10-minute recorded runs in a warehouse built for research. A working site with full shifts is a different setting, so the result is a hypothesis there (section 4).
4. **What does the one opened study say about voice against RF terminals?**
   In a field experiment with 101 participants, voice performed better than RF-terminal picking, and higher productivity appeared possible without losing quality. The abstract gives no percentage; no source opened supports 99.9% (section 3).
5. **What does a bucket brigade need from the warehouse system?**
   In Bartholdi and Eisenstein's report, no changes to a typical WMS; the workers balance the work themselves when sequenced slowest to fastest (section 4).
6. **How does Interact Analysis's analyst separate a WCS from a WES?**
   A WCS controls the flow of goods across fixed automation; a WES controls the timing and location of workflows. Most embedded WES sit in the WMS (section 7).
7. **How does an AMR differ from an AGV system for the software above it?**
   In an AGV system a central unit schedules, routes and dispatches; AMRs negotiate independently and decentralise decisions (section 6; Fragapane et al., abstract).
8. **A colleague says labour is the largest cost in a warehouse. What do you answer?**
   In US Census data for 2012, payroll was about a third of warehousing firms' total expense; payroll with benefits was about 41%; the other lines were not opened, so "largest" is not shown (section 8).

## Deliverable

### A. The role card form

The fields are fixed here; SCE8, SCE9, SCE11 and SCE13 reuse them in this order. Every line carries its source in brackets: a section of this course with its grade, "register" for a case fact, or "working" for a working description.

| # | Field | What goes in it |
|---|---|---|
| 1 | Who | First name, role, operation, and the unit that set the card |
| 2 | Measured on | The measures the person is judged by, with whose definition |
| 3 | Conditions | Pace, physical setting, shift, hazards |
| 4 | Device | What they hold or sit at, and how they confirm work |
| 5 | Top tasks | Three to five, in the order of time spent |
| 6 | What goes wrong | The failures they meet most, with the unit that traces them |
| 7 | What they do about it | Their workaround or escalation today |
| 8 | What they would ask of the software | Requests that follow from fields 2 to 7; working, until a user study supports them |
| 9 | Hands to and depends on | The roles upstream and downstream of them |

### B. Five cards, Corvane and Ostrel Foods (fictional)

**Card 1 · Mina, operator, Corvane (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Mina; operator, picks web orders, two years in the job; Corvane's distribution centre [register]; card set by SCE5 |
| 2 | Measured on | Picks per person-hour against a standard; picking accuracy (B&H §3.3 [practice]; SCE3 §12) |
| 3 | Conditions | Two-shift pattern, a third in peak; walking aisles to forward locations; web peak about four times a normal week from mid-November to early January [register]; warehousing injury and illness rate above private industry's in US data (section 1.1 [independent], US only) |
| 4 | Device | Handheld scanner showing a sequence of locations; scans location and item (SCE3 deliverable C [practice]; section 3 [working]) |
| 5 | Top tasks | Walk to location; find size and colour; scan; put to cart or tote; report shorts (SCE3 §3, §9) |
| 6 | What goes wrong | Stock the record shows but the shelf does not hold (register; SCE4 §9); hard search in mixed locations (SCE3 §9, Batt & Gallino [independent]) |
| 7 | What they do about it | Report a short pick; the order may be re-sourced to a store (SCE4 §9 [register, working]) |
| 8 | What they would ask of the software | A short-pick entry that takes one step; a location shown with what else is in it; a rate that counts the work done on shorts [working] |
| 9 | Hands to and depends on | Depends on replenishment of forward locations [register, SCE2]; hands to packing and to Tobias, outbound supervisor [register] |

**Card 2 · Ilse, team lead, chilled picking, Ostrel Foods (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Ilse; team lead, chilled picking; Ostrel Foods [register]; card set by SCE5 |
| 2 | Measured on | Routes picked complete by departure; picking accuracy by case (SCE3 §8, §12) [working] |
| 3 | Conditions | Evening work for next-morning delivery; chilled zone; picking by the case onto roll cages [register]. No source opened on cold-store working conditions; rules on cold work are a question for the national labour inspectorate |
| 4 | Device | Handheld or voice for her pickers; a desktop or handheld to watch the route backlog [working] |
| 5 | Top tasks | Assign pickers to routes; watch progress against departure; clear shorts; check date codes on short-dated stock (SCE2 §9, SCE3 §8) |
| 6 | What goes wrong | Short-dated stock found too late; substitutions agreed by phone and not recorded [register]; pickers waiting on replenishment from Bram (SCE2 register note) |
| 7 | What they do about it | Moves pickers between routes; sends a short or a substitute and tells the dispatcher [working] |
| 8 | What they would ask of the software | A substitution recorded at the pick, not after; a route view by departure time; a team rate that fits zone handoffs (section 4: cooperation suited zone picking in one experiment [independent]) [working] |
| 9 | Hands to and depends on | Depends on Bram's replenishment [register]; hands staged cages to loading [register, SCE3 register note]; tells Nuno, dispatcher, of shorts and substitutes [working] |

**Card 3 · Carla, inventory controller, Corvane (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Carla; inventory controller; Corvane [register]; card set by SCE5 |
| 2 | Measured on | Inventory accuracy by WERC's measures, with the definition and netting stated (SCE4 §10) |
| 3 | Conditions | Desk and floor; counts after short picks and re-slots [register, SCE4] |
| 4 | Device | Desktop for reports and adjustments; handheld for counts [working] |
| 5 | Top tasks | Plan counts; count or assign counts after shorts and re-slots; investigate; post adjustments with reason codes (SCE4 §5) |
| 6 | What goes wrong | Stock the centre cannot find [register]; new SKUs each season needing locations [register, SCE4 §6] |
| 7 | What they do about it | Trigger counts on short picks; adjust with a reason code (SCE4 §5) |
| 8 | What they would ask of the software | Adjustments that cannot be approved by the person who counted or picked the location (section 1.3, GAO-25-107721 para. 10.04 [independent], applied by inference); a list of locations touched since the last count [working] |
| 9 | Hands to and depends on | Depends on Mina's short reports; answers for the stock record (SCE1 register); reports to Marek [working] |

**Card 4 · Sofia, transport planner, Ostrel Foods (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Sofia; transport planner, builds the next day's routes; Ostrel Foods [register]. The register has no warehouse planner; at Ostrel picking is released by route (SCE3 register note), so her route plan is the warehouse's release plan. Card set by SCE5 |
| 2 | Measured on | Routes built by the time picking starts; vehicles used of the 40 [register; working] |
| 3 | Conditions | Desk work between the late-afternoon cut-off and the evening start [register] |
| 4 | Device | Desktop: the routing tool and the ERP [register] |
| 5 | Top tasks | Take the day's orders after cut-off; build routes for about 600 delivery points; adjust fixed routes; hand the route list to the warehouse (register; SCE3 register note) |
| 6 | What goes wrong | Late orders after cut-off; routes changed after picking has begun [working] |
| 7 | What they do about it | Re-plans and tells Ilse which routes moved [working] |
| 8 | What they would ask of the software | The warehouse's progress by route on her screen; a warning when a change hits a route already being picked [working] |
| 9 | Hands to and depends on | Depends on the order cut-off; hands routes to Ilse's team [SCE3 register note] and to Nuno [working] |

**Card 5 · Marek, site manager, Corvane (fictional)**

| # | Field | Content |
|---|---|---|
| 1 | Who | Marek; site manager of the distribution centre; Corvane [register]; card set by SCE5 |
| 2 | Measured on | Cost per unit handled, on-time and accurate shipments, injuries, staff turnover [working] |
| 3 | Conditions | About 140 staff in a normal week and about 260 in peak, the difference from agencies [register] |
| 4 | Device | Desktop reports [working] |
| 5 | Top tasks | Staff peak; set standards and any bonus scheme; approve workarounds; prepare the replacement of a warehouse system near end of vendor support [register for the system and the decision; Marek's tasks working] |
| 6 | What goes wrong | Web orders promised from stock the centre cannot find; store staff shipping web orders without a process [register] |
| 7 | What they do about it | Adds counts and staff in peak [working] |
| 8 | What they would ask of the software | Rates by person and task against standards that fit the picking method (section 4 [independent]); time for an agency worker to reach standard (section 2: no cross-site source) [working] |
| 9 | Hands to and depends on | Answers to Edda, vice-president, supply chain [working; the register does not say who the site manager reports to] |

### C. Template: the role card

Copy one per role. Every line ends with its source in brackets.

| # | Field | Fill in |
|---|---|---|
| 1 | Who | ______ (first name or role label; role; operation; site; the unit or study that set the card) |
| 2 | Measured on | ______ (each measure by its owner's definition: whose, unit of measure, netted or not) |
| 3 | Conditions | ______ (shift and hours; pace; temperature, height, weight handled; hazards; the injury rate for the industry and country, with source and year) |
| 4 | Device | ______ (handheld, vehicle-mounted, wearable, voice, light, desktop; how work is confirmed) |
| 5 | Top tasks | ______ (three to five, by time spent, observed on site where possible) |
| 6 | What goes wrong | ______ (the failures met most often; where in the flow map they start) |
| 7 | What they do about it | ______ (workaround, escalation, or paper record; who else is involved) |
| 8 | What they would ask of the software | ______ (requests that follow from fields 2 to 7; mark working until users confirm) |
| 9 | Hands to and depends on | ______ (roles upstream and downstream, by name or role) |

### D. Glossary lines

| Term | Definition | Source |
|---|---|---|
| Work standard (labour standard) | Expected time or rate for a task, against which a person's rate is reported | B&H Fig. 11.6 [practice]; definition working |
| Engineered labour standard | A standard built from measured task elements for each task's conditions | Working; no defining source opened |
| Bucket brigade | Each picker carries work forward until someone takes it over, then goes back for more | B&H §11.1 [practice] |
| Competition-based incentive | Individual bonus to top performers | de Vries et al. 2015 [independent] |
| Cooperation-based incentive | Team bonus to the best team | de Vries et al. 2015 [independent] |
| Pick by voice | Picking directed by spoken instructions, confirmed by speech | de Vries et al. 2016 IJPR (names the tool) [independent]; description working |
| Pick to light | Lights on locations show where and how many; a button confirms | Working; tool named in de Vries et al. 2016 IJPR |
| Warehouse control system (WCS) | Software that controls the flow of goods across fixed automation | Scriven, Interact Analysis, 2023 [analyst] |
| Warehouse execution system (WES) | Software that controls the timing and location of warehouse workflows | Scriven, Interact Analysis, 2023 [analyst] |
| Automated guided vehicle (AGV) | Vehicle whose scheduling, routing and dispatching a central unit controls | Fragapane et al. 2021 [independent] |
| Autonomous mobile robot (AMR) | Robot that negotiates with other resources and decides for itself | Fragapane et al. 2021 [independent] |
| Robotic mobile fulfilment | Robots that carry storage racks to pick stations | Azadeh et al. 2019 (system named) [independent]; description working |
| ISO 6780 pallet sizes | 1200 × 800, 1200 × 1000, 1219 × 1016 (48 × 40 in), 1067, 1100, 1140 mm square | ISO 6780:2003 [independent] |
| Gamification | Game mechanics (points, leaderboards, badges, challenges) used to engage workers | Vendor page [vendor-reported] |

## Notes: facts for the case register

Working descriptions in deliverable B, not in case-facts.md; each is this unit's assumption.

- Corvane: Mina confirms picks with a handheld scanner showing a sequence of locations (card 1; from SCE3 deliverable C).
- Corvane: Carla uses a desktop for reports and adjustments and a handheld for counts, and reports to Marek (card 3).
- Corvane: Marek, site manager, answers to Edda; he staffs the peak, sets standards and any bonus scheme, approves workarounds and prepares the warehouse-system replacement (card 5).
- Ostrel Foods: Ilse's pickers use handhelds or voice; Ilse watches the route backlog on a desktop or handheld and tells Nuno of shorts and substitutes (card 2).
- Ostrel Foods: Sofia's route list is the warehouse's release plan; she works at a desk between the cut-off and the evening start, on the routing tool and the ERP, is measured on routes built by the time picking starts and vehicles used, and hands routes to Ilse's team and to Nuno; routes are sometimes changed after picking has begun (card 4).

## Sources

All addresses opened on 24 November 2026; the source log (sources.md) gives what was read at each.

- Azadeh, K., de Koster, R. & Roy, D. (2019). Robotized and Automated Warehouse Systems: Review and Recent Developments. *Transportation Science* 53(4), 917–945. https://doi.org/10.1287/trsc.2018.0873 (abstract, read at https://repub.eur.nl/pub/119543)
- Bahr, W., Mavrogenis, V. & Sweeney, E. (2021). Gamification of warehousing: exploring perspectives of warehouse managers in the UK. *International Journal of Logistics Research and Applications*, published online 25 February 2021. https://doi.org/10.1080/13675567.2021.1892042 (authors' accepted manuscript, read at https://publications.aston.ac.uk/id/eprint/42403/1/gamification_2020_authors_revision_2_openaccess.pdf)
- Banker, S. "Key Attributes of a Robust Gamification Program in Labor Management". Manhattan Associates website, 3 June 2021. Vendor-reported. https://www.manh.com/our-insights/resources/articles/key-attributes-robust-gamification-program-in-labor-management
- Bartholdi, J. J., III & Eisenstein, D. D. *Bucket Brigades: A Self-Balancing Order-Picking System for a Warehouse*. 1 August 1996. https://www2.isye.gatech.edu/~jjb/bucket-brigades/papers/bbwh.pdf
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, 2017. §3.3, ch. 11. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- de Vries, J., de Koster, R. & Stam, D. (2015). Aligning order picking methods, incentive systems, and regulatory focus to increase performance. ERIM Report Series ERS-2015-009-LIS. https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf
- de Vries, J., de Koster, R. & Stam, D. (2016). Aligning Order Picking Methods, Incentive Systems, and Regulatory Focus to Increase Performance. *Production and Operations Management* 25(8), 1363–1376. https://doi.org/10.1111/poms.12547 (abstract, read at https://repub.eur.nl/pub/96216)
- de Vries, J., de Koster, R. & Stam, D. (2016). Exploring the role of picker personality in predicting picking performance with pick by voice, pick to light and RF-terminal picking. *International Journal of Production Research* 54(8), 2260–2274. https://doi.org/10.1080/00207543.2015.1064184 (abstract, read at https://research.vu.nl/en/publications/2b68e9a2-c4f6-4c92-93be-9409a9f29a7f)
- Fragapane, G., de Koster, R., Sgarbossa, F. & Strandhagen, J. O. (2021). Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda. *European Journal of Operational Research* 294(2), 405–426. https://doi.org/10.1016/j.ejor.2021.01.019 (abstract, read at https://repub.eur.nl/pub/134773)
- Gartner. "Warehouse Management System (WMS)". Glossary entry on a gartner.com host (gcom.pdo.aws.gartner.com); the page shows no title or glossary name, so the label is the course's; read 24 November 2026. Analyst. https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/warehouse-management-system-wms
- Grosse, E. H. & Glock, C. H. (2013). An experimental investigation of learning effects in order picking systems. *Journal of Manufacturing Technology Management* 24(6), 850–872. https://doi.org/10.1108/JMTM-03-2012-0036 (abstract, read at the publisher's page)
- Grosse, E. H., Glock, C. H. & Neumann, W. P. (2017). Human factors in order picking: a content analysis of the literature. *International Journal of Production Research* 55(5), 1260–1276. https://doi.org/10.1080/00207543.2016.1186296 (abstract, read at https://econpapers.repec.org/RePEc:taf:tprsxx:v:55:y:2017:i:5:p:1260-1276)
- A warehouse-software vendor. "What is warehouse gamification?" Undated (© 2026). Vendor-reported. https://www.infios.com/en/supply-chain-solutions/gamification/what-is-gamification
- International Organization for Standardization. ISO 6780:2003, *Flat pallets for intercontinental materials handling — Principal dimensions and tolerances*, 2nd edition; confirmed 2026. https://www.iso.org/standard/30524.html (clause 4.1 read in a reseller's sample: https://cdn.standards.iteh.ai/samples/30524/ec0a6ce1ee454b98b00c8551c8ecb7df/ISO-6780-2003.pdf)
- Putz, L.-M., Hofbauer, F. & Mates, M. (2019). A vignette study among order pickers about the acceptance of gamification. GamiFIN Conference 2019, CEUR-WS Vol-2359. https://ceur-ws.org/Vol-2359/paper14.pdf
- Scriven, R. (Interact Analysis). "Warehouse Execution Systems vs. Warehouse Control Systems". *Supply & Demand Chain Executive*, 22 February 2023. https://www.sdcexec.com/home/article/22724398/interact-analysis-warehouse-execution-systems-vs-warehouse-control-systems
- US Bureau of Labor Statistics. "Employer-Reported Workplace Injuries and Illnesses – 2025". News release, 18 November 2026 (private-industry total recordable case rate; warehousing and storage injury-only rate). https://www.bls.gov/news.release/osh.htm ; archived copy https://www.bls.gov/news.release/archives/osh_11182026.htm
- US Bureau of Labor Statistics. "Warehousing and Storage: NAICS 493". Industries at a Glance, data extracted 20 November 2026 (employment, occupations, and the 2025 total recordable case rate of 4.5 per 100 full-time workers). https://www.bls.gov/iag/tgs/iag493.htm
- US Census Bureau. Service Annual Survey, warehousing and storage (NAICS 493), employer firms: total expense, gross annual payroll, all other operating expenses, as published by the Federal Reserve Bank of St. Louis (FRED). https://fred.stlouisfed.org/data/EXPEF493ALLEST ; https://fred.stlouisfed.org/data/EXPGAPEF493ALLEST.txt ; https://fred.stlouisfed.org/data/EXPECFEF493ALLEST ; https://fred.stlouisfed.org/data/EXPAOOEF493ALLEST
- US Census Bureau. "Service Annual Survey Methodology". https://census.gov/programs-surveys/sas/technical-documentation/methodology.html
- US Government Accountability Office. *Standards for Internal Control in the Federal Government*, exposure draft of the 2024 revision, GAO-24-106889, June 2024. https://www.gao.gov/assets/880/872514.pdf
- US Government Accountability Office. *Standards for Internal Control in the Federal Government*, GAO-25-107721, May 2025, effective from fiscal year 2026; supersedes GAO-14-704G (2014). https://www.gao.gov/products/gao-25-107721 (product page; para. 10.04 read in a copy at https://www.thompsongrants.com/sites/grants/files/advisory_files/gao-25-107721.pdf)

## Unsure list

1. de Vries et al. (2015 working paper): the sample breakdown (142; 28/39/75; 48 teams), the least-squares means of order lines picked (53.9, 46.84, 47.58, 35.37, 41.03, 43.91; the raw means in the paper's Table 6 differ) and the 15.2% and 34.3% gains are the fetch tool's extraction of the working paper; whether the published POMS article keeps the same numbers was not checked.
2. de Vries et al. (2016, POMS): the published abstract reports no effects on quality, while the working paper's tables, as extracted, show error rates differing by condition; which holds in the published full text is not known.
3. de Vries et al. (2016, IJPR): "performs better" is from the abstract; the size of the voice advantage and whether it held for each picking method were not read.
4. BLS: resolved at the fresh check. The release's 4.4 (4.6 in 2024) for warehousing and storage is the injury-only rate; the Industries at a Glance page gives 4.5 total recordable cases (injuries and illnesses) per 100 full-time workers for 2025. The unit sets IAG's 4.5 against the release's private-industry total recordable rate of 2.3; both are from the Survey of Occupational Injuries and Illnesses.
5. Census Service Annual Survey via FRED: the 2012 figures (total expense, payroll, employer's cost for fringe benefits); the "all other operating expenses" figure ($4,388 million) could not be re-fetched at the quality review, so the $9,625 million by subtraction rests on the first fetch; the FRED pages carry no notes, and the Census table itself was not opened.
6. Gartner glossary definition: read at a gcom.pdo.aws.gartner.com host whose page showed no title; that it is the current Gartner glossary entry is assumed, and the Sources title is the course's label.
7. Scriven (Interact Analysis, 2023): whether the author was Interact Analysis staff is not stated on the page; the article is graded analyst on its byline.
8. ISO 6780:2003 sizes were read in a reseller's sample of the standard, not on ISO's own page; the "confirmed 2026" status is from ISO's page.
9. Bahr et al. (2021): journal volume, issue and pages were not shown; the year is the online date. Bräuer and Mazarakis's finding is known only as Bahr et al. report it.
10. Bartholdi & Eisenstein (1996): the paper has no venue on the page; the training times and the temporary-worker remark are the authors' report from one site.
11. Seed W2 (Gu, Goetschalckx & McGinnis 2007, EJOR 177(1) 1–21, https://doi.org/10.1016/j.ejor.2006.02.025): a fresh search on 24 Nov 2026 returned only index records and the DOI address, which redirects to Elsevier's linking hub; not checked; no open copy found by SCE2, SCE3, SCE4 or SCE5 (flag F39 closes for W2).
12. Regional use of the ISO 6780 pallet sizes (Annex A) was not read; flag F24 stays open for regional pallet sizes.
13. Abstract-only: Grosse et al. (2017), Grosse & Glock (2013), de Vries et al. (2016, IJPR and POMS), Azadeh et al. (2019), Fragapane et al. (2021).
14. Not opened: the GAO exposure draft's paragraphs OV2.01 and OV4.17 in the final text; the Census Service Annual Survey's other expense lines; Bräuer and Mazarakis (reported through Bahr et al.); Grosse et al.'s full text.
Object: the handheld scanner (RF terminal), section 3

Fresh check 2026-11-24 (claude-opus-5-5): fix · 2 errors, 8 should-fix, 5 minor; report audits/supply-chain-execution/fresh-check-SCE5.md
Quality review 2026-11-24 (claude-opus-5-5): fix · 0 errors, 4 should-fix, 14 minor; report audits/supply-chain-execution/quality-review-SCE5-2026-11-24.md
