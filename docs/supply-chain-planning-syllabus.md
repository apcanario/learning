# Supply Chain Planning for Product Teams · syllabus

Designed 21 Nov 2026 on Fable 5.2. The repo was read at commit abe5590 and not changed; row S-SCP0 files this document.

## 1 · Frame

Designed 21 Nov 2026 on Fable 5.2, in a chat. The repo was read at commit abe5590 and not changed. A new markdown course, id `supply-chain-planning`, key SCP, the second course of the Supply Chain track.

**Pick:** teach planning as a cascade of decisions, from a demand forecast to a released order, with demand and inventory given seven of the sixteen core units.

- Every planning screen serves one decision on one horizon; that is the map.
- Demand and inventory are common to retailers, distributors and manufacturers.
- The reader's craft needs the decision and its owner, not the mathematics.

**Override if:** the reader's product work is mainly in manufacturing scheduling; then SCP9 splits into two units and SCP10 shrinks.

### Where the evidence pushes back

- **Concepts only against a quantitative subject.** Forecasting and inventory are mathematics. A unit without calculation can slide into vocabulary. The preamble's rule (what goes in, what comes out, what it assumes, when it fails; what moves a quantity and in which direction) is the guard, and the fresh checker fails a method that is only named (flag F4).
- **The value of planning software is mostly vendor-told.** Independent measurement of what a planning system returns is thin. SCP15 and DD-SCP2 are briefed to say so and to list what was searched.
- **The process evidence is weak by design.** Research on sales and operations planning is mostly single-company cases and surveys; SCP11 is briefed to state the designs.
- **Competition results travel badly.** The forecasting competitions used particular datasets; applying them to a company's own demand is an inference, and SCP3 is briefed to label it.
- **Published company cases are survivors.** DD-SCP1 is briefed to look for published failures and say what it found.
- **The seed bibliography says only that its entries exist.** 42 of 46 were checked on 21 Nov 2026 (40 against Crossref's record, one at its publisher's page, one in a library catalogue); 4 are not opened and say so. Nobody has checked what any entry says.

## 2 · Identity

| | |
|---|---|
| Title | Supply Chain Planning for Product Teams |
| Code | SCP (units SCP1 to SCP16, DD-SCP1, DD-SCP2) |
| Course entry | `supply-chain-planning`, family `markdown` |
| Data | `courses/supply-chain-planning/course.toml` (`[pack]`), `briefs.md`, `notes/` |
| Vault | `courses/supply-chain-planning/` |
| Fresh checks | `audits/supply-chain-planning/` |
| Track | Supply Chain, its second course; listed in `catalog.toml` as planned since 19 Nov 2026 |
| Reader | Someone who builds, sells or implements supply chain planning software, or is moving into that work, with no planning background. In the preamble |
| Kind | A public course: an exception to the single-reader rule. `docs/public-courses.md` and its rules apply, rule 4 (source units) apart, as there are none |

## 3 · Goal and outcomes

**Goal:** by the end, the reader can take any screen, feature or roadmap item in planning software, say which planning decision it serves and on what horizon, who makes that decision and with what data, how it commonly goes wrong, and argue from that what the product should do.

- **Outcome 1 · Decisions.** Lays out the planning cascade from demand forecast to released order for a retailer, a distributor and a manufacturer and names, at every step, the decision, its horizon, the role, the data and the common failure, without notes (SCP1 to SCP12).
- **Outcome 2 · Evidence.** For any claim about a forecasting method, an inventory policy or a planning process, says what kind of evidence stands behind it, gives its grade, and says what a fair test would need (SCP1, SCP3 to SCP5, SCP8, SCP15, DD-SCP1, DD-SCP2).
- **Outcome 3 · Product.** Maps a planning product line onto the cascade, writes role cards for its users and a value case a finance reader would accept, and writes a product strategy memo that rests on them (SCP13 to SCP16).

## 4 · Units

| # | Code | Title | Scope | Deliverable | Search |
|---|---|---|---|---|---|
| | | **Opening** | | | |
| 1 | SCP1 | The planning map, the words and the evidence | What supply chain planning is, the decisions it is made of and their horizons, where each kind of system sits, and how to grade what researchers, analysts and vendors say. | planning map + working glossary + the grade key | on |
| | | **Part 1 · Demand** | | | |
| 2 | SCP2 | Demand and its data | What demand is as against sales, the shapes it takes, what moves it, and the data a demand plan rests on. | demand profile sheet | off |
| 3 | SCP3 | Forecasting methods | The families of forecasting method, from baselines to machine learning: what each takes, assumes and gets wrong, and what the competitions found. | method selection table | off |
| 4 | SCP4 | Forecast error and what it is used for | How forecast error is measured, why two accuracy figures rarely compare, and what the error is for downstream. | measurement plan | off |
| 5 | SCP5 | Judgment, overrides and the demand planner | What planners change in a forecast and with what effect, how functions agree on one number, and the demand planner as a role. | override policy + demand planner role card | off |
| | | **Part 2 · Inventory** | | | |
| 6 | SCP6 | Why inventory exists and how much | The reasons stock is held, service as a target, and what moves the amount of stock a service level needs. | inventory purpose map + service policy table | off |
| 7 | SCP7 | Replenishment | When to order and how much: the standard policies, the constraints that override them, and what people and bad records do to the rule. | replenishment policy decision table + flow map | off |
| 8 | SCP8 | The network: stock in more than one place | Where stock is held across sites, how shortage is shared, and what the bullwhip research did and did not find. | stock positioning map + bullwhip cause table | off |
| | | **Part 3 · Supply and the plan** | | | |
| 9 | SCP9 | Supply planning for makers | How a manufacturer turns a demand plan into a production schedule and purchase orders: bills of material, the master schedule, requirements planning and capacity. | planning cascade map + four role cards | off |
| 10 | SCP10 | Retail and distribution planning | What a retailer and a distributor plan before and after stock is ordered: the financial plan, assortment, allocation, promotions and markdown. | season plan calendar + promotion planning sheet + retail role cards | off |
| 11 | SCP11 | Sales and operations planning | The monthly cycle that agrees one plan for demand, supply and money: its steps, its roles, its incentives and its evidence. | cycle calendar + decision log + role and conflict table | off |
| 12 | SCP12 | Where the plan meets execution | How a plan becomes orders, what has to come back from the floor, and what happens to the plan when the day goes wrong. | plan-to-execution handoff table + exception table | off |
| | | **Part 4 · The product, its users and its buyers** | | | |
| 13 | SCP13 | The planning system as a product | The planning system as something built and sold: modules, the data model, the engine, the planner's screen, and a product line mapped onto the cascade. | capability map of a planning product line | on |
| 14 | SCP14 | Planners as users | Every planning role set side by side: how planners work, what makes them trust or ignore a recommendation, and the conflicts between roles. | full role card set + conflict matrix | off |
| 15 | SCP15 | Buying planning software: what differs | Who buys planning software, how its value is claimed and tested, why projects stall, and the kinds of vendor in the market. | value-case sheet + fair-test checklist + competitor sheet | on |
| 16 | SCP16 | Capstone: one planning product memo | One opportunity argued in full from the course's own material, as a model for the memo the reader writes on real work. | worked strategy memo + memo template | off |
| | | **Deep dives** | | | |
| 17 | DD-SCP1 | Deep dive: planning as companies have published it | Five to seven planning practices real companies have put in print, each read for what was done, what was claimed, and who is telling it. | comparables table + case reading sheet | on |
| 18 | DD-SCP2 | Deep dive: the hard numbers | Every number that circulates in planning traced to its origin, and the numbers the field does not have. | evidence ledger + list of missing numbers | on |

Each unit's Aim, Takes and Gives lines are in `course.toml`; its brief is in `briefs.md`.

## 5 · Order, chats and search

SCP1 to SCP16 in reading order, then DD-SCP1, then DD-SCP2. No interleaving: no two units build the same asset. The eighteen writing rows go after the Supply Chain Execution rows (accepted by the owner, 21 Nov 2026).

### Chats

The owner's instruction of 21 Nov 2026: as many units a chat as is reasonable, as little by hand as possible, and then less risk. One setup chat and five writing chats, each a thin Sonnet 5.5 chat with fresh Opus 5.5 agents. A writing chat runs its units one after the other (`kit/next_prompt.py --bundle 4`; method §4, P31); each unit is checked, filed, landed and published before the next begins, so a chat that stops strands nothing.

1. Setup: row S-SCP0 alone. It writes no unit and touches the prompt printer only to add the course to its queue.
2. Chat 1: SCP1 to SCP4.
3. Chat 2: SCP5 to SCP8. This boundary is the read point: the owner reads SCP1 to SCP8, and starting chat 3 is his go. No gate row and nothing to close by hand.
4. Chat 3: SCP9 to SCP12.
5. Chat 4: SCP13 to SCP16.
6. Chat 5: DD-SCP1 and DD-SCP2, then the closing corrections in the same chat.

The writing chats start from one starter that never changes; `--course` finds the course's first unit not yet filed, so the same starter also resumes a chat that stopped part-way:

`Clone apcanario/learning (shallow, push access). Supply Chain Planning, next bundle. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. Run `python3 kit/next_prompt.py --course supply-chain-planning --bundle 4` and work what it prints in full, unattended.`

The `--course` option, the clone line in other courses' prompts and the bundle hand-over are the work of a separate row, S-PROMPT1, run on its own so that a mistake in the printer cannot land inside a course's setup. If S-PROMPT1 has not run when setup ends, setup's reply gives the starter with `--row W-SCP1` instead.

Four units a chat is a pick, not a measurement: bundles of two and three have run in this repo. If a chat stops early, its filed units stay published and the same line carries on from the next one.

By hand, in total: one paste of the setup prompt, five pastes of the starter, and reading SCP1 to SCP8. A unit's reply leaves a task for the owner only where no agent can do it; a proposal is worked in the next row unless he vetoes it.

- **Carry-forward rule:** `docs/method.md` §9, in full, in the prompts document.
- **Search on** for the five units that state current market or company facts: SCP1, SCP13, SCP15, DD-SCP1, DD-SCP2. Each owes a staleness check six months after it is written.
- **Search off** for the thirteen units on planning decisions and synthesis. Off still means every reference is opened before it is cited.

## 6 · Sourcing: the course's part

Added to `docs/sourcing-standard.md` as Part 9:

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed research; the published results of a forecasting competition; a standard textbook cited by edition and chapter; an industry association's report or survey with its sample and year; an analyst report by firm, title and date; an audited company filing; a standards body's own page; a vendor's own page, release or documentation, dated.
- [ ] No video, podcast, social-media post, unsigned blog, comparison or lead-generation site, or press rewrite of a release is cited as a source; one may be named only as the claim under examination.
- [ ] Every claim carries one of the four grades (independent, analyst, vendor-reported, practice), and the grade follows SCP1's key.
- [ ] A finding states what kind of evidence it is (forecasting competition, field experiment, laboratory experiment, simulation, single-company case study, survey), with its data, setting and year; a simulation is not presented as a field result; a correlation is called a correlation.
- [ ] A finding from one industry, company or dataset applied to another is labelled as the unit's inference.
- [ ] No formula and no worked calculation appears; a method is described by what goes in, what comes out, what it assumes and when it fails. A number is a sourced finding in its source's own terms, or a case fact marked fictional.
- [ ] Statistical, machine-learning and optimisation methods are treated on published evidence. Nothing treats generative AI, language-model assistants or agents; a vendor's word "AI" is reported as the vendor's word.
- [ ] An analyst report says how it was read: in full, in a public reprint, or in abstract. A claim that rests on an abstract alone says so.
- [ ] No real vendor is assessed, ranked, compared or recommended, and no real vendor's product line is mapped.
- [ ] A real vendor is named only to attribute a dated public statement to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every vendor on the list given alike.
- [ ] Worked product examples use only the fictional vendors of `case-facts.md`, labelled "(fictional)"; no fictional vendor is said or hinted to stand for a real one.
- [ ] A real company's planning practice is described only from a peer-reviewed paper, a published case with named authors or its own audited filing; an account co-written by the company's staff or its software supplier is labelled an interested party's account.
- [ ] A book or article by someone who sells the method it describes is labelled an interested party's account.
- [ ] A peer-review site is cited by market for what its reviewers say, with where any count was read, never to assess a named vendor.
- [ ] A number says whose figure it is, the sample and the year. No price, revenue or win rate of a private company appears unless that company published it. No return, saving or payback is promised to the reader.
- [ ] A common claim on the course's list is named as a claim and set against its evidence, or against "no independent source found".
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read (abstract, reprint or full text) and the date; the edition or release cited is the one opened.
- [ ] The source log gives every reference's kind of venue (peer-reviewed journal, academic or professional publisher's book, forecasting competition, association, analyst firm, audited filing, standards body, vendor) and any commercial interest its authors have in what they describe.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal or publisher, year, volume, pages, DOI.
- [ ] Every fact about Corvane, Ostrel Foods, Pellward, Lathmoor, Ebbfield and Varnby Software is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his employer, his role or his work appears (`python3 kit/private_terms.py` prints OK).
- [ ] No unit is framed as interview preparation; no craft method is taught.
- [ ] Where the search flag is on, every analyst list, market figure, filing figure and vendor page carries the date it was read.
- [ ] The deliverable is built in full on the case the brief names and then given as a template whose blanks say what goes in them.
- [ ] "In the planning meeting" and "Self-check" are present, and every Self-check answer agrees with the body.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper.

## 7 · Models and chats

- This syllabus: Fable 5.2, as the Project sets for course design.
- The setup row, S-SCP0: a thin main chat on Sonnet 5.5 that launches fresh Opus 5.5 agents.
- Every writing row: a thin main chat on Sonnet 5.5. Writer, fresh checker, applier, filer and corrections checker are each a fresh Opus 5.5 agent.
- No safety reader: this course has no unit where a mistake could harm a person.
- Cost: eighteen units at five agents or more each, in five writing chats after the setup chat. The boundary after SCP8 exists so that depth and cost are judged on eight units before ten more are paid for.

## 8 · Decisions taken in this chat

### Decisions of the Project's owner (21 Nov 2026)

1. Centre of gravity: demand and inventory.
2. Concepts only: no formula and no worked calculation in any unit.
3. Statistical forecasting, machine learning and optimisation are in, as methods judged on published evidence. Generative AI, assistants, agents and vendors' AI branding are out.
4. The commercial side is compressed to what differs from execution software: one unit on the product, one on users, one on buying.

### Decisions of the design

5. Sixteen core units and two deep dives. The skill's guide is eight to ten core units; the subject's own logic needs more, as it did for Supply Chain Execution: three kinds of company plan differently and the cascade has twelve steps worth a unit each.
6. Standalone: assumes no other course. It shares the Execution course's world (Corvane, Ostrel Foods), its four evidence grades, its vendor rule and its fictional-vendor rule, so a reader of both meets one system.
7. A third case company, Pellward, a manufacturer: the Execution case has none, and supply planning cannot be taught without one. Tandric Logistics is left out.
8. Three fictional vendors, one per kind of planning vendor: Lathmoor and Ebbfield are new; the third is Varnby Software, the Execution course's ERP vendor, given a planning line. Halvern Systems sells execution software "and nothing else" in that register, so it has none.
9. The grade key adds one requirement the Execution course did not have: every finding states its kind of evidence (competition, field experiment, laboratory experiment, simulation, case study, survey). Planning research is full of simulations; a reader must not take one for a field result.
10. Real companies may appear as documented cases from peer-reviewed or published accounts, labelled where the company co-wrote them. This is new against the Execution course and is confined to operating companies; the vendor rule is unchanged. Accepted by the owner, 21 Nov 2026, with decision 9.
11. Search on for SCP1, SCP13, SCP15, DD-SCP1 and DD-SCP2 only. The domain units rest on textbooks and published research that do not move in six months.
12. Deep dives: the comparables (DD-SCP1, published company accounts) and the hard numbers (DD-SCP2). No third.
13. Lessons of the Execution course's first two units are built into the briefs: the length range covers the body only; SCP1 lists the common claims and marks the unit that tests each; the grade rulings for peer-review sites, unsampled surveys, repeated numbers and standards are in the preamble; the edition cited is the edition opened.

## 9 · Proposals

None open. The owner accepted, on 21 Nov 2026: real companies as documented cases with the kind-of-evidence rule; the read point after SCP8; the queue position; bundles of four; and the plain clone line `Clone apcanario/learning (shallow, push access).` at the head of every session's prompt. To lower risk the same day, setup runs alone and writes no unit, and the changes to `kit/next_prompt.py` beyond adding this course to its queue (the `--course` option, the clone line in other courses' prompts, bundles that name their course) moved to a row of their own, S-PROMPT1.

## 10 · What was checked and what was not

- Checked on 21 Nov 2026: that 40 references exist and that their authors, title, journal or publisher, year, volume, issue and pages are as Crossref records them (read one by one); one book at its publisher's page; one book in a university library catalogue. Four entries are marked not opened.
- Checked: the case register against `courses/supply-chain-execution/notes/case-facts.md` at commit abe5590; the catalogue line and colour for this course in `catalog.toml`; the form of the Execution course's syllabus, prompts document and bibliography.
- Checked: `course-pack.toml` parses; it has 18 units and 18 order rows; `briefs.md` has a Preamble and 18 briefs.
- Checked once by web search: that Pellward, Lathmoor and Ebbfield are not names of companies in retail, appliances, food or software. One search each is not proof.
- Not checked: what any source says. The briefs name topics, not findings, for that reason.
- Not checked: `kit/pack.py`'s schema against `course-pack.toml`, the build, `index_check.py`, `private_terms.py`. Row S-SCP0 runs them.
- Checked by row S-SCP0 on 22 Nov 2026: the case register's Filed facts in `courses/supply-chain-planning/notes/case-facts.md` against the Execution register, `courses/supply-chain-execution/notes/case-facts.md`; seven Filed facts that differed were restored to the Execution register's wording (commit 158f511).
- Checked by row S-SCP0 on 22 Nov 2026, once by web search each: Pellward, Lathmoor and Ebbfield; no real company of those names in retail, appliances, food or software was found, and no name was changed. One search each is not proof.
- Checked by row S-SCP0: the bibliography's existence checks. The 42 entries checked on 21 Nov 2026 were not re-checked. The four marked not opened were tried once each on 22 Nov 2026 at the publisher's or issuing body's page: R1 opened (ASCM's SCOR DS page); R3 opened in part (Gartner's supply chain planning glossary entry; its sales and operations planning entry and Magic Quadrant method pages not opened); S3 not opened (the publisher's ebook page returned no record); R2 not opened (Gartner's document page refused the fetch). The count is now 43 checked for existence, R3 in part (one of its pages opened), 2 not opened (S3, R2). What any source says was not checked.
- Done by row S-SCP0: Part 9 of `docs/sourcing-standard.md`, from section 6 of this syllabus.
