# AI in Supply Chain Execution · syllabus

Drafted 21 Nov 2026 in a design chat on Fable 5.2. The repo was read at commit `abe5590` and not changed; row S-AIE0 filed this document on 23 Nov 2026 (section 10). A markdown course family of its own, the third course of the Supply Chain track (listed there as coming soon since 19 Nov 2026, decision D12 of the first course). Eight files make its starting state:

| File | What it is | Goes to |
|---|---|---|
| `syllabus.md` | This file: frame, goal, outcomes, units, order, bundles, sourcing part, decisions | `docs/ai-in-supply-chain-execution-syllabus.md` |
| `briefs.md` | The shared preamble and the 14 briefs | `courses/ai-in-supply-chain-execution/briefs.md`, unchanged |
| `units.toml` | Goal, order, search flags, and each unit's title, scope, deliverable, Aim, Takes, Gives | The `[pack]` table of `courses/ai-in-supply-chain-execution/course.toml` |
| `case-facts.md` | What this course adds to the track's fictional case | `courses/ai-in-supply-chain-execution/notes/case-facts.md`, after the first course's register |
| `bibliography.md` | 72 seed references checked for existence (of the 72 entries, checked in full (Crossref record read, or entry's own record/page read): 37 Crossref + 14 page read = 51, plus 11 carried from the first course's seed list (checked there on 19 Nov 2026, not re-read here); checked in part (search listing or a page that did not give the record): 9 (not counted as checked); not opened: 1. Leads, not found: 0), and the 16 common claims | `courses/ai-in-supply-chain-execution/notes/bibliography.md` |
| `prompts.md` | Writer rules, the checker's eight passes, each row's paragraph, the carry-forward rule, the run plan | `docs/ai-in-supply-chain-execution-prompts.md` |
| `setup-prompt.md` | The setup row's prompt: it registers the course and writes no unit | Pasted once into a Sonnet 5.5 chat |
| `starter.txt` | The two lines that start, and resume, every writing chat | Pasted once per bundle |

## 1 · Frame

**Pick: the decision first, the technique second, the claim third.**

- Every AI feature in this software makes or supports one operational decision.
- Four technique families fail in four different ways; the label hides which.
- Most evidence is simulation or vendor-told; the course grades and tags it.

**Override if:** you want a course about generative AI and agents only; then AIE2 and AIE3 shrink to one unit and AIE4 grows to three.

**What the course is for.** Being able to look at a claimed AI feature and say what it decides, what kind of technique does the work, what a person still decides, who pays when it is wrong, and how good the evidence is. It delivers what the track's listing promised on 19 Nov 2026, word for word.

**Stands on its own files.** It reuses the track's fictional case and assumes the ground of Supply Chain Execution for Product Teams, and it never points to that course's units by code. So it does not wait for that course to be finished, and its packets need nothing the kit does not already stage.

**Out of scope.** Demand forecasting and inventory planning (the planning course). Robots and their control software (the automation course). How to build a model, write a prompt or design an interface.

**No real vendor is assessed.** The first course's rule, unchanged, extended to companies that provide AI models. The fictional vendors gain fictional AI features and six fictional claims.

**Where the evidence pushes back.**
- The solid work is decades of optimisation research; it was not called AI when it was written.
- Machine learning for batching, slotting and routing is published mostly as simulation on synthetic or historical data. Field experiments in execution work are few: the seed list holds two in warehouses.
- The human-factors research comes from cockpits, control rooms and clinics. Its transfer to a dispatch desk is an inference, and the units say so.
- For generative features and agents in execution software there is, as far as this chat saw, no independent field study. The field evidence is from customer support and consulting. Expect "vendor-reported" and "no independent source found" often in AIE4.
- The statistics that circulate ("80% fail", "95% of pilots") lead back to interviews, polls and predictions. AIE11 traces four of them.
- The law is moving: secondary pages report that the EU's high-risk dates were pushed back in 2026. Units read the texts and date them.

## 2 · Identity

| | |
|---|---|
| Title | AI in Supply Chain Execution |
| Code | AIE (units AIE1 to AIE13, DD-AIE1) |
| Course entry | `courses/ai-in-supply-chain-execution/course.toml`, family `markdown` |
| Vault and data | `courses/ai-in-supply-chain-execution/` (`briefs.md`, `notes/`, `pages/`) |
| Fresh checks | `audits/ai-in-supply-chain-execution/` |
| Track | Supply Chain (exists); the course leaves the track's `planned` list |
| Reader | The first course's reader, who now knows its ground; in the preamble |
| Kind | A public course: `docs/public-courses.md` applies, rule 4 (source units) apart |
| Rows | S-AIE0 (setup), W-AIE1 to W-AIE13, W-DD-AIE1 |

## 3 · Goal and outcomes

**Goal.** By the end, the reader can take any claimed AI feature in order, warehouse or transport software and say which decision it makes or supports, which kind of technique is doing the work, what a person still decides, who carries the cost when it is wrong, and how strong the evidence is that it works.

| # | Outcome, measurable | Delivered by |
|---|---|---|
| 1 | Given a feature description, names the decision, places it in one of four families and on one of five rungs, and says what the person still decides, so that a second reader using the keys agrees | AIE1 to AIE4, AIE6 to AIE8 |
| 2 | For a decision automated at a given rung, writes the override sheet and the risk register: who carries the cost, how the error is noticed, which text governs it where | AIE9, AIE10, DD-AIE1 |
| 3 | Grades a vendor's AI claim on the claim sheet, designs a pilot that could show it false, and writes a feature brief that rests on both | AIE5, AIE11, AIE12, AIE13 |

## 4 · Units

Briefs are in `briefs.md`. Every unit ends with its deliverable built in full on the case, then as a template; before it, "In a demo or a pilot review" and "Self-check".

| # | Code | Title | Ships | Search |
|---|---|---|---|---|
| | | **Opening** | | |
| 1 | AIE1 | What counts as AI here | Family key, five-rung ladder, grade and setting key, decision map | on |
| | | **Part 1 · The techniques** | | |
| 2 | AIE2 | Optimisation and rules: the AI that was already there | Decision inventory | off |
| 3 | AIE3 | Prediction: what machine learning adds | Prediction sheet, four worked | off |
| 4 | AIE4 | Generative models and agents | Agent permission sheet, two worked | on |
| | | **Part 2 · The evidence and the operation** | | |
| 5 | AIE5 | The field evidence, read in full | Evidence table, "a study you can lean on" sheet | off |
| 6 | AIE6 | In the warehouse | Six decision cards | off |
| 7 | AIE7 | In transport | Six decision cards, shipper-against-provider table | off |
| 8 | AIE8 | In order management | Five decision cards, one traced promise | off |
| | | **Part 3 · People, risk and proof** | | |
| 9 | AIE9 | The person in the loop | Override sheet, cost-carrier matrix | off |
| 10 | AIE10 | Risk, rules and accountability | Risk register, questions for counsel and vendor | on |
| 11 | AIE11 | Reading an AI claim | Claim sheet, ten claims worked | on |
| 12 | AIE12 | Money and the pilot | Pilot plan, cost-line table | on |
| 13 | AIE13 | Capstone: one feature, argued | Worked feature brief, template, checklist | off |
| | | **Deep dive** | | |
| 14 | DD-AIE1 | Deep dive: algorithmic management on the floor | Transparency sheet, questions for representatives and counsel | on |

**Shape.** The `new-course` skill asks for eight to ten core units and two or three deep dives, the comparables and the hard numbers always. This course has thirteen and one, by the subject's own logic: three technique families, three systems, then people, risk and proof. The comparables are core (AIE11) and so are the hard numbers (AIE5 and AIE12), because the capstone depends on them. AIE5 would be a deep dive anywhere else; it is placed before the operation units so that they cite eight studies from one checked table and do not each re-read and re-describe them. That removes the largest source of corrections the first course's rows have shown: the same source described twice, differently.

## 5 · Order, search and chats

- **Order:** syllabus order, AIE1 to AIE13, then DD-AIE1. No interleaving: no two units build the same asset.
- **The chats.** Setup runs alone and writes no unit. Then the course is written in chats of four units, in writing order; the last chat takes what is left and closes the course.

| Chat | Rows | Units | Started by |
|---|---|---|---|
| Setup | S-AIE0 | none: files the design, builds, verifies, publishes | `setup-prompt.md` |
| Bundle 1 | W-AIE1 to W-AIE4 | AIE1, AIE2, AIE3, AIE4 | the starter |
| Bundle 2 | W-AIE5 to W-AIE8 | AIE5, AIE6, AIE7, AIE8 | the starter |
| Bundle 3 | W-AIE9 to W-AIE12 | AIE9, AIE10, AIE11, AIE12 | the starter |
| Bundle 4 | W-AIE13, W-DD-AIE1 | AIE13, DD-AIE1, then every correction and flag still open | the starter |

- **The starter**, the same two lines for every writing chat; it also resumes a chat that stopped part-way:

```
Clone apcanario/learning (shallow, push access).
AI in Supply Chain Execution, next bundle. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. Run `python3 kit/next_prompt.py --course ai-in-supply-chain-execution --bundle 4` and work what it prints in full, unattended.
```

  If `kit/next_prompt.py` has no `--course` option when setup runs, the setup row's reply gives the same two lines with `--row W-AIE1 --bundle 4`, and each later reply names its own first row.
- **Every pasted prompt opens with** `Clone apcanario/learning (shallow, push access).` and says nothing else about cloning.
- **Each chat** is a thin Sonnet 5.5 main chat with fresh Opus 5.5 agents. Each unit is checked, filed, landed and published before the next begins, so a chat that stops strands nothing. The bundle boundaries are the course's parts, so every chat starts where its units' dependencies are already filed.
- **No gate rows.** A point where Pedro reads before more is written sits on a bundle boundary; his starting the next chat is the go. Nothing for him to close by hand.
- **Closing.** The last chat works every correction and flag still open itself, and delivers a closing prompt only if something remains, saying why.
- **Replies.** A chat's one reply ends with the starter in a code block, not a long prompt. A task is left for Pedro only where no agent can do it. Proposals are worked in the next row unless he vetoes them.
- **Search on** for six units that state current facts: AIE1, AIE4, AIE10, AIE11, AIE12, DD-AIE1. Each owes a staleness check six months after it is written. **Search off** for eight; off still means every reference is opened before it is cited.
- **Carry-forward rule:** `prompts.md` section 4, with the course's names. The run plan's rules are `prompts.md` section 5.

## 6 · Sourcing: the course's part

To be added to `docs/sourcing-standard.md` as the next free part by the setup row: **Part 10**, since Part 9 was taken by Supply Chain Planning for Product Teams (registered 22 Nov 2026). Part 1 applies as well.

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed research, including peer-reviewed proceedings named as such; a preprint, labelled; a standard textbook cited by edition and chapter; a standards body's own page; the text of a law or regulation at its issuing body's page, or a regulator's own release or order; an industry association's report or survey with its sample and year; a research report of a university centre or an independent research organisation, labelled as a report, with its method; an analyst report or release by firm, title and date; an audited company filing; a vendor's, a model provider's or a consultancy's own page, documentation or survey, dated.
- [ ] No video, podcast, social-media post, unsigned blog, comparison or lead-generation site, law-firm or consultancy summary of a law, or press report of a study or a release is cited as a source; one may be named only as the claim under examination.
- [ ] Every claim carries one of the four grades (independent, analyst, vendor-reported, practice), and the grade follows AIE1's key. A consultancy's survey is vendor-reported. An analyst's prediction is called a prediction.
- [ ] Every claim about performance carries one setting tag (field trial, field observation, simulation, benchmark, demonstration, none), and the tag follows AIE1's key. No simulated or benchmarked result is written as if it had been measured in an operation.
- [ ] A preprint is called a preprint and is never the only support for a recommendation.
- [ ] A study's finding states its setting, sample, design, what was compared with what, the period and who measured; the effect is in the source's own terms; a correlation is called a correlation.
- [ ] A finding from another kind of work (a call centre, a consultancy, a hospital, a cockpit) applied to execution work is labelled as the unit's inference.
- [ ] A result obtained with a named model or version says which; its transfer to a current model is labelled as the unit's inference.
- [ ] Every feature discussed is placed in one family and on one rung by AIE1's keys, or the unit says why it sits across two.
- [ ] An analyst report says how it was read: in full, in a public reprint, or in abstract. A claim that rests on an abstract alone says so.
- [ ] No real vendor or model provider is assessed, ranked, compared or recommended, and no real vendor's product line or AI feature is mapped.
- [ ] A real vendor or model provider is named only to attribute a dated public statement or its own documentation to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every entry given alike. A company named by a peer-reviewed study as its setting is named as that setting only.
- [ ] Worked examples use only the fictional vendors, features and claims of `case-facts.md`, labelled "(fictional)"; none is said or hinted to stand for a real one; no fictional claim is repeated as a finding.
- [ ] A number says whose figure it is, the sample and the year. No price, revenue or win rate of a private company appears unless that company published it.
- [ ] A common claim on the course's list is named as a claim and set against its evidence, or against "no independent source found"; a circulating statistic is traced to the work that first reported it.
- [ ] A legal point names its jurisdiction, cites the text or the authority's own page with the date it was read, and is put as a question with the body to consult; the unit says it is information, not legal advice.
- [ ] A claim about jobs, pace, injury or surveillance rests on peer-reviewed work, a regulator or a named report with its method. Nothing teaches covert monitoring of an identified worker or the avoidance of a duty to inform or consult.
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read and the date.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
- [ ] Every fact about Corvane, Ostrel Foods, Tandric Logistics, Halvern Systems, Varnby Software and Kestrow is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his employer, its products, his role or his work appears (`python3 kit/private_terms.py` prints OK).
- [ ] No unit points to a unit of another course by code; no unit is framed as interview preparation; no model-building, prompt-writing, design or sales method is taught; no mathematics beyond arithmetic and no code.
- [ ] Where the search flag is on, every law, date, standard, analyst list, survey figure and product fact carries the date it was read.
- [ ] The deliverable is built in full on the case the brief names and then given as a template whose blanks say what goes in them.
- [ ] "In a demo or a pilot review" and "Self-check" are present, and every Self-check answer agrees with the body.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper.

## 7 · Models and chats

- This syllabus: Fable 5.2, as the Project sets for course design.
- The setup chat and every writing chat: a thin main chat on Sonnet 5.5. Registrar, registration checker, writer, fresh checker, applier, filer and corrections checker are each a fresh Opus 5.5 agent on a packet.
- No safety reader: no unit teaches anything that could harm a person. DD-AIE1's two prohibitions are in the preamble and in the checker's passes.
- Rule 13 of `docs/public-courses.md` (the quality review) applies and runs inside the bundle when a unit's flags call for it.
- Cost: fourteen writing rows at five agents or more, in four writing chats after one setup chat. AIE5 exists to make the later rows cheaper.

## 8 · Decisions taken in this chat

Each stands unless vetoed.

| # | Decision | Override |
|---|---|---|
| D1 | A public course in the Supply Chain track, keeping the title and promise the track's listing already shows | A private course |
| D2 | Thirteen core units and one deep dive | Ten and two: merge AIE7 with AIE8, drop AIE12 into AIE11, split AIE5 back into a deep dive |
| D3 | Four technique families, with generative models and agents as one of them | A course on generative AI and agents only |
| D4 | The course stands on its own files and does not wait for the first course to finish | Take the first course's role and buyer cards by code, and start after its last unit |
| D5 | The track's fictional case, reused, with fictional AI features and six fictional claims | A new case |
| D6 | The first course's vendor rule, extended to AI model providers | Real AI features mapped and compared, at the cost of the owner publishing an assessment of his own industry |
| D7 | The track's four evidence grades kept, plus a setting tag on every performance claim | A fifth grade for simulations |
| D8 | AIE5 reads eight field studies in full before the operation units | Keep it as a deep dive written last |
| D9 | Setup alone, then four chats of four units from one starter; no gate row: a read sits on a bundle boundary and starting the next chat is the go | Bundles of two, at twice the pastes |
| D10 | A flag that would change a brief is settled at the start of the next writing chat by a fresh Opus 5.5 agent, as an exact replacement, and listed in that chat's reply for veto; the writing agent itself still never rewords a brief | Brief changes wait for your confirmation, as in the first course |
| D11 | A task is left for Pedro only where no agent can do it; none is planned. The outside-publishing check of the first course (its P-SCE1) covers the track | Add a read-before-sharing task |
| D12 | Reliefs wait for a later row, as rule 10 of the public courses | Register ten outlines in the setup row |
| D13 | Search on for six units | All fourteen on, at eight more staleness checks |

## 9 · Proposals (worked by the setup row unless vetoed)

- **P-AIE1.** `docs/sourcing-standard.md` gains the course's part (section 6), and `docs/public-courses.md` gains the course. ⚠ Both are files other rows read.
- **P-AIE2.** `kit/next_prompt.py`: one change only, the course added to `QUEUE`. No `HOLDS` or `GATES` entry. The setup row prints another course's row before and after and confirms the two are byte-identical. ⚠ Touches the script every public course's prompt comes from; the byte check is the guard. The starter uses `--course`; if the script has no such option on the day, the starter falls back to `--row`, and nothing is added to the script for it.
- **P-AIE3.** `kit/private_terms.py` already holds the owner's employer and its product names (the first course's P-SCE2). The setup row confirms the list covers the employer's AI product name and adds it if not. ⚠ Touches a check every public course relies on.
- **P-AIE4.** The setup row searches the three new feature names and renames any that matches a real product. ⚠ None.
- **P-AIE5.** The course leaves `planned` in `catalog.toml` and joins `course_order` after the first course; `docs/courses-index.md` gains its section and its line under "Courses to come (Supply Chain)" goes. ⚠ A public page changes: the course's tile turns from coming soon to in progress.
- **P-AIE6.** Row G-R-AIE, *proposed*: the course's reliefs, after the last unit. Candidate objects: a handheld scanner, a pallet, a tote, a box truck, a shipping label, a roll cage, a dock door, a conveyor, a delivery note, a wearable terminal. ⚠ None.
- **P-AIE7.** If the first course's syllabus review settles its flags F8, F9 and F18 (how to grade a regulator's page and a treaty's text), the same wording is copied into AIE1's key by the correction route. ⚠ None; the preamble here already grades a law's text and a regulator's statement independent.

## 10 · What was checked and what was not

- Checked on 21 Nov 2026: 36 journal, proceedings and NIST references at Crossref, one record each, authors, title, journal, year, volume, issue and pages as the record gives them. Three DOIs recalled from memory failed (one resolved to a different paper, one did not resolve, one was not tried) and those entries are marked not checked. 10 entries found by web search; 3 seen only secondhand; 12 named from memory and not checked; 11 taken from the first course's seed list, checked there on 19 Nov. Those 25 looked for again on 23 Nov 2026 (row S-AIE0); now, of the 72 entries, checked in full (Crossref record read, or entry's own record/page read): 37 Crossref + 14 page read = 51, plus 11 carried from the first course's seed list (checked there on 19 Nov 2026, not re-read here); checked in part (search listing or a page that did not give the record): 9 (not counted as checked); not opened: 1. Leads, not found: 0.
- Checked: `units.toml` parses; 14 units; its order matches the 14 brief sections; "Search before writing" is in exactly the six search-on briefs.
- Read in the repo at commit `abe5590`: the first course's syllabus, briefs, case register, seed bibliography, flags and prompts document; `docs/method.md`, `docs/sourcing-standard.md`, `docs/public-courses.md` (outline), `kit/next_prompt.py` (its bundle option), `catalog.toml` (this course's listing), `courses/_template/course.toml`.
- Not checked: what any source says. The briefs name topics and kinds of study, never findings, for that reason.
- Not checked: whether `kit/thin.py` and `kit/next_prompt.py` need more than P-AIE2 to run a second course of this build. The setup row's registration check finds out.
- Not checked: whether the three new feature names collide with real products (P-AIE4).
- Done by row S-AIE0 (23 Nov 2026): Part 10 of `docs/sourcing-standard.md`, from section 6 of this syllabus (the design named Part 9; Part 9 was taken by Supply Chain Planning for Product Teams on 22 Nov 2026, so Part 10 stands wherever the design said Part 9; `briefs.md` names no part and is unchanged).
- Checked by row S-AIE0 (P-AIE4): "Halvern Assist", "Varnby Advisor" and "Kestrow Smart Slotting" were each searched once on 23 Nov 2026. The first two matched no product. "Smart Slotting" is the name of real slotting products and services in logistics, so the Kestrow feature is "Kestrow Nightly Re-slot" in every file of the course (the case register's feature table and claim K4); a search for the new name found no product under it.
