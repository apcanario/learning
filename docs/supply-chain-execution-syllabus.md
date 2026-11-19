# Supply Chain Execution for Product Teams · syllabus

Drafted 19 Nov 2026 in a design chat on Fable 5.2, first as a private course, then reworked the same day as a **public** one. **Not in the repo.** Nothing was committed, published to Academy or written to the Project. Seven files make the course's starting state:

| File | What it is | Goes to |
|---|---|---|
| `syllabus.md` | This file: frame, goal, outcomes, units, order, sourcing part, decisions | `docs/supply-chain-execution-syllabus.md` and the hub fields |
| `units_data.py` | `PRE`, the 20 units with their briefs, `AIMS` | `generator/data/supply-chain-execution/units_data.py`, unchanged |
| `case-facts.md` | The fictional operations and the fictional vendors | `generator/data/supply-chain-execution/case-facts.md` |
| `bibliography.md` | Seed references checked for existence, leads, and the list of common claims | `generator/data/supply-chain-execution/bibliography.md` |
| `prompts.md` | This course's parts of the writing rows' prompt, and the carry-forward rule | `docs/supply-chain-execution-prompts.md`, then `docs/BACKLOG.md` rows through `kit/next_prompt.py` |
| `track-coming-soon.md` | Four courses to come in the track, each with a scope line and a teaser | `kit/courses.py`, as coming soon, and `docs/courses-index.md` |
| `setup-prompt.md` | The setup row's prompt, pasted into a Sonnet 5.5 chat with the zip | Used once; saved in the backlog row S-SCE0 |

## 1 · Frame

**Pick: operations first, then people, then money. Warehouse gets the most room.**

- A screen cannot be improved without knowing the physical event behind it.
- Product work needs buyers and costs, not only workflows.
- The warehouse has the deepest research and the most roles.

**Override if:** readers turn out to work mostly on transport or orders; then Part 2 grows and Part 1 loses a unit.

**What the course is for.** Learning the domain: how warehouses, transport and orders run, who works in them, how the software that runs them is bought, and what it costs. It is the first course of a new public track, Supply Chain. No unit is interview preparation.

**Out of scope.** AI features and any vendor's AI layer. They sit on top of the three systems; the course teaches the systems and the work underneath them.

**No real vendor is assessed.** Worked product examples use fictional vendors. Real vendors appear only as the source of a public statement or as entries in a dated list from an analyst report or a filing, all alike. The reader gets the method and the templates to map and compare real products themselves.

**Where the evidence pushes back.** The operations research on warehouses is solid and old: much of it predates e-commerce at scale. Transport and order management have less of it. Almost everything about the software itself comes from vendors or from analysts whose reports vendors license. Private vendors publish no prices, revenue by product or win rates. Why deals are won or lost has almost no independent evidence. The course grades every claim, so "vendor-reported" and "practice" will appear often, and some sections will say "no independent source found".

## 2 · Identity

| | |
|---|---|
| Title | Supply Chain Execution for Product Teams |
| Code | SCE (units SCE1 to SCE18, DD-SCE1, DD-SCE2) |
| `kit/courses.py` entry | `supply-chain-execution`, family `markdown` |
| Data | `generator/data/supply-chain-execution/` |
| Vault | `courses/supply-chain-execution/` |
| Fresh checks | `audits/supply-chain-execution/` |
| Track | New: Supply Chain (no existing track fits) |
| Reader | Someone who builds, sells or implements order, warehouse or transport software, or is moving into that work, with no operations background. In the preamble |
| Kind | A public course, the fourth: an exception to the single-reader rule. `docs/public-courses.md` and its rules apply, rule 4 (source units) apart, as there are none |

Unit codes run from SCE1. The plan page read on 18 and 19 Nov numbered the opening unit SCE0; every code here is that plan's code plus one.

## 3 · Goal and outcomes

**Goal.** By the end, the reader can take any screen, feature or roadmap item in order, warehouse or transport software, say what physical work it stands for, who uses it and who pays for it, and argue from that what the product should do.

| # | Outcome, measurable | Delivered by |
|---|---|---|
| 1 | Walks one order from promise to delivery and names, at every step, the physical event, the system, the user role and the common failure, without notes | SCE1 to SCE10, DD-SCE2 |
| 2 | For a given feature, writes a two-sided case: each buyer card's reason to pay and each role card's reason to use or avoid it, with the grade of the evidence | SCE5, SCE8, SCE9, SCE11 to SCE15, DD-SCE1 |
| 3 | Builds a competitor sheet and a total-cost model for a real market from public sources, and writes a product strategy memo that rests on them | SCE6, SCE16, SCE17, SCE18 |

## 4 · Units

Briefs are in `units_data.py`. Every unit ends with its deliverable built in full on the case, then as a template; before it, "On a site visit" and "Self-check".

| # | Code | Title | Ships | Search |
|---|---|---|---|---|
| | | **Opening** | | |
| 1 | SCE1 | The map, the words and the evidence | Execution map, glossary, grade key | on |
| | | **Part 1 · The warehouse** | | |
| 2 | SCE2 | Inbound and storage | Inbound flow map, failure list | off |
| 3 | SCE3 | Outbound: release, pick, pack, ship | Picking-method decision table, outbound flow map | off |
| 4 | SCE4 | Inventory and control | Inventory-error cause tree, count plan | off |
| 5 | SCE5 | The floor: people, devices and machines | Five warehouse role cards | off |
| 6 | SCE6 | The warehouse system as a product | Capability map of a warehouse product line | on |
| | | **Part 2 · Transport and orders** | | |
| 7 | SCE7 | Transportation in practice | Shipment lifecycle map | off |
| 8 | SCE8 | The transport system as a product | Transport role cards, shipper-versus-provider comparison | on |
| 9 | SCE9 | Order management | Order lifecycle map, order role cards | on |
| 10 | SCE10 | The seams | System-of-record table, handoff failure catalogue | off |
| | | **Part 3 · The business** | | |
| 11 | SCE11 | The buying committee | Buyer cards | on |
| 12 | SCE12 | The sale | Stage-by-stage sheet | on |
| 13 | SCE13 | Users by role | Full role card set, conflict matrix | off |
| 14 | SCE14 | Implementers and administrators | Implementation timeline, two role cards | off |
| 15 | SCE15 | Demo versus shift | Two-sided case template, three worked cases | off |
| 16 | SCE16 | Money | Total-cost model | on |
| 17 | SCE17 | Reading the field | Competitor sheet method, worked sheets on fictional vendors | on |
| 18 | SCE18 | Capstone: one strategy memo | Worked memo, memo template | off |
| | | **Deep dives** | | |
| 19 | DD-SCE1 | Deep dive: the logistics provider's business | Contract-to-cash flow, provider cards | on |
| 20 | DD-SCE2 | Deep dive: peak and exceptions | Exception catalogue, peak readiness checklist | off |

**Shape.** The `new-course` skill asks for eight to ten core units and two or three deep dives. This course has eighteen and two, by the subject's own logic: three systems, each needing the operation before the product, then a business part. The skill's two standing deep dives, the comparables and the hard numbers, are core units here (SCE17 and SCE16) because the capstone depends on them.

## 5 · Order and search

- **Order:** syllabus order, SCE1 to SCE18, then DD-SCE1, then DD-SCE2. No interleaving: no two units build the same asset.
- **Gate:** after SCE6 the queue stops for Pedro to read the six units (decision D3). The row still delivers SCE7's prompt, marked not to be run until he says go.
- **Carry-forward rule:** any error found in a filed unit, before, during or after a later unit is written, goes into the next prompt and is fixed there first; anything that bears on a unit not yet written is printed in that unit's prompt; every delivery ends with the next unit's prompt holding those corrections and any updated guideline (`prompts.md` section 4).
- **Search on** for the nine units that state current market or company facts: SCE1, SCE6, SCE8, SCE9, SCE11, SCE12, SCE16, SCE17, DD-SCE1. Each owes a staleness check six months after it is written.
- **Search off** for the eleven units on operations and synthesis. Off still means every reference is opened before it is cited; it means the writer does not go looking for current facts.

## 6 · Sourcing: the course's part

To be added to `docs/sourcing-standard.md` as **Part 8 · Supply Chain Execution for Product Teams** by the setup row. Part 1 applies as well.

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed research; a standard textbook cited by edition and chapter; an industry association's report or survey with its sample and year; an analyst report by firm, title and date; an audited company filing; a standards body's own page; a vendor's own page, release or documentation, dated.
- [ ] No video, podcast, social-media post, unsigned blog, comparison or lead-generation site, or press rewrite of a release is cited as a source; one may be named only as the claim under examination.
- [ ] Every claim carries one of the four grades (independent, analyst, vendor-reported, practice), and the grade follows SCE1's key.
- [ ] An analyst report says how it was read: in full, in a public reprint, or in abstract. A claim that rests on an abstract alone says so.
- [ ] No real vendor is assessed, ranked, compared or recommended, and no real vendor's product line is mapped.
- [ ] A real vendor is named only to attribute a dated public statement to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every vendor on the list given alike.
- [ ] Worked product examples use only the fictional vendors of `case-facts.md`, labelled "(fictional)"; no fictional vendor is said or hinted to stand for a real one.
- [ ] A peer-review site is cited by market for what its reviewers say, with the number of reviews, never to assess a named vendor.
- [ ] A number says whose figure it is, the sample and the year. No price, revenue or win rate of a private company appears unless that company published it.
- [ ] A study's finding states its sample, setting and design; a finding from one site or industry applied to another is labelled as the unit's inference.
- [ ] A common claim on the course's list is named as a claim and set against its evidence, or against "no independent source found".
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read and the date.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
- [ ] Every fact about Corvane, Ostrel Foods, Tandric Logistics, Halvern Systems, Varnby Software and Kestrow is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his employer, his role or his work appears (`python3 kit/private_terms.py` prints OK).
- [ ] Nothing treats AI features; no unit is framed as interview preparation; no craft method is taught.
- [ ] Where the search flag is on, every analyst list, market figure and filing figure carries the date it was read.
- [ ] The deliverable is built in full on the case the brief names and then given as a template whose blanks say what goes in them.
- [ ] "On a site visit" and "Self-check" are present, and every Self-check answer agrees with the body.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper.

## 7 · Models and chats

- This syllabus: Fable 5.2, as the Project sets for course design.
- The setup row, S-SCE0: a thin main chat on Sonnet 5.5 that launches a fresh Opus 5.5 registrar, a fresh Opus 5.5 registration checker and, if there are findings, a fresh Opus 5.5 applier.
- Every writing row: a thin main chat on Sonnet 5.5. Writer, fresh checker, applier, filer and corrections checker are each a fresh Opus 5.5 agent.
- No safety reader: this course has no unit where a mistake could harm a person.
- As a public course it takes rule 13 of `docs/public-courses.md` (a quality review when a unit collects more flags than the rule allows). That adds agents on some rows.
- Cost: twenty rows at five agents or more. The gate after SCE6 exists so that depth and cost are judged on six units before fourteen more are paid for.

## 8 · Decisions taken in this chat

Each stands unless vetoed.

| # | Decision | Override |
|---|---|---|
| D1 | A public course, built and deployed like the other public courses (Pedro, 19 Nov 2026) | Keep it out of the public deploy |
| D2 | One course of twenty units in three parts, the first of a new track, Supply Chain | Three shorter courses in the track (six, four and ten units), if the kit handles units that build on another course's |
| D3 | A gate after SCE6: the queue stops for a read | No gate; run all twenty |
| D4 | Three fictional operations as the running case | One operation followed through the course |
| D5 | No real vendor is assessed or mapped; three fictional vendors carry the product examples; real vendors appear only as sources of statements or in dated lists | Real vendors mapped and compared, at the cost of the owner publishing an assessment of his own industry |
| D6 | AI is out of scope | An AI deep dive as a twenty-first unit |
| D7 | Four evidence grades: independent, analyst, vendor-reported, practice | Five, splitting association surveys from peer-reviewed research |
| D8 | Search on for nine units; every unit opens every reference | All twenty on, at eleven more staleness checks |
| D9 | The setup row runs in a thin Sonnet 5.5 chat with Opus 5.5 agents, as the writing rows do | One Opus 5.5 chat, as the sport psychology setup ran |
| D10 | Reliefs wait for a later row, as rule 10 of the public courses | Register ten outlines in the setup row |
| D11 | Unit codes start at SCE1, one above the plan page's | Keep SCE0, if the kit accepts it |
| D12 | Four courses are listed in Academy as coming soon in the track, with a teaser each: planning, automation and robotics, AI in execution, last mile and omni-channel (Pedro, 19 Nov 2026). A course on the logistics provider's business is left off: it is promised only if DD-SCE1 proves too thin | List none until each has a syllabus |

## 9 · Proposals

- **P-SCE1 · For Pedro, by hand.** Before the course is shared outside Academy, read your employer's policy on outside publishing. The course assesses no vendor and says nothing about you, so the exposure is small; it is still supply chain teaching published by someone in the industry. ⚠ None on the build; it only bears on when you share the link.
- **P-SCE2.** The setup row confirms `kit/private_terms.py` passes on the course's pages and adds to its term list, for this course's pages, the owner's employer and its product names, so that no unit can name them outside a dated analyst list. ⚠ Touches a check every public course relies on.
- **P-SCE3.** The setup row derives the writing rows' prompt from `docs/sport-psychology-prompts.md` as it stands in the repo, replacing its course-specific parts with those in `prompts.md`. This chat did not open the repo. ⚠ None if the template is copied, not edited in place.
- **P-SCE4.** The setup row searches the six coined names (Corvane, Ostrel, Tandric, Halvern, Varnby, Kestrow) and replaces any that matches a real company in the field, in every file. ⚠ None. (Note, S-SCE0, 19 Nov 2026: the fifth name as coined and searched was "Brindle Software"; it matched a real software maker and was replaced by "Varnby Software" in every file, this line included.)
- **P-SCE5.** `docs/sourcing-standard.md` gains Part 8 (section 6 above), and `docs/public-courses.md` gains the course. ⚠ Both are files other rows read.
- **P-SCE6 · For Pedro, by hand.** The gate: after W-SCE6, read SCE1 to SCE6 and say go, change or stop. ⚠ Delays fourteen rows until answered.
- **P-SCE7 · For Pedro, by hand.** The Project instructions' Purpose line names the courses; this one is not in it. ⚠ None.
- **P-SCE8.** Row G-R-SCE, *proposed*: the course's reliefs, after the last unit. Candidate objects: a pallet, a roll cage, a reach truck, a handheld scanner, a shipping label, a pallet rack, a tote, a conveyor, a box truck, a shipping container. ⚠ None.
- **P-SCE9.** The standing rules (the carry-forward rule and the source-credibility floor) are written into `docs/method.md` and the repo's copy of the `new-course` skill, so no later course has to be told them. ⚠ Touches the method every chat reads; it adds a section and changes none.

- **P-SCE10.** Each coming-soon course needs its own design chat on Fable before any row is queued for it; the listing promises a course, not a date. ⚠ A public page will name four courses that do not exist yet.

## 10 · What was checked and what was not

- Checked on 19 Nov 2026: that each of the 26 journal and handbook references exists and that its authors, title, journal, year, volume and pages are as Crossref records them (26 records read one by one; a 27th did not resolve and was moved to the leads); that the three books, the association reports and the analyst reports exist, by search, each at the address in `bibliography.md`. Entries seen only as cited by another page are marked secondhand, and one is marked not opened.
- Checked: `units_data.py` parses; it has 20 units and 20 `AIMS` entries; every unit an aim "takes" comes earlier in the order; every unit code in `bibliography.md` exists; no file names the Project's owner or his employer.
- Not checked: what any source says. The briefs name topics, not findings, for that reason.
- Not checked: the repo. No file was read from it. The paths above follow the sport psychology course's, as mirrored in the Project.
- Not checked: whether the six coined names collide with real companies (P-SCE4).
