# Prompts: AI in Supply Chain Execution

- **Setup**, once: `setup-prompt.md`, pasted into a new chat on **Sonnet 5.5**. It runs the setup row **S-AIE0** alone: it files the design, builds, verifies and publishes, and writes no unit.
- **Writing chats**, on **Sonnet 5.5**: each starts from the course's two-line starter (section 5, point 2) and writes up to four units, rows W-AIE1 to W-AIE13 and W-DD-AIE1 in order. Thin chats that stage, launch fresh **Opus 5.5** agents, run scripts and record, and never open a unit, a report or a brief.

The writing template is not rewritten here. The repo holds a working one for a course of the same build and the same track, in `docs/supply-chain-execution-prompts.md` (the code block under "Rows W-SCE1 to W-DD-SCE2", with every correction its rows have made to it up to the day of setup). S-AIE0 copies it and replaces its course-specific parts with sections 1 to 5 below: its opening clone sentence, replaced by the line of section 5, point 1; the course's name, code, slug, paths and sourcing part; the writer rules with section 1; the checker's passes with section 2; the row table with section 3; the carry-forward rule with section 4; its step on the next prompt and its Reply, which follow section 5, points 7 and 8. Everything else in the template (the thin chat's rules, the agents and their order, the scripts, the checkpoint commits, landing with `kit/land.py`, rule 13's quality review, the close) stays as the repo has it.

## 1 · Writer rules

The writer is one fresh Opus 5.5 agent with its packet and nothing else.

1. **Open before citing.** Every reference is found by a search and read at its publisher's page, its DOI address or the issuing body's own page before it carries a claim. The seed bibliography says only that an entry exists; twelve of its entries were not checked even for that.
2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (abstract, reprint or full text), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the work's own title, never a slug; a figure is cited to the work that first reports it, never to one that repeats it; each Sources entry is checked against the publisher's record before hand-in.
3. **Fewer, better.** Prefer one source read in full to three read in abstract. Do not cite to decorate. If a section's support is one textbook's account, grade it practice and say so.
4. **Grade and tag every claim** by AIE1's keys: one grade on every claim that carries a number, a mechanism or a recommendation; one setting tag on every claim about performance. From AIE2 on, the keys arrive in the packet inside AIE1. Never write a simulated or benchmarked result as if it had been measured in an operation.
5. **Report a study whole.** Setting, sample, design, what was compared with what, the period, who measured, the effect in the source's own terms. From AIE6 on, a study in AIE5's table is cited from that table; re-open the source only for a point the table does not cover, and if the source and the table disagree, that is a correction (rule 13).
6. **Label every transfer.** A finding from other work, another industry or an older model, applied to execution software, is "the unit's inference".
7. **Families and rungs.** Place every feature the unit discusses in one family and on one rung by AIE1's keys, or say why it sits across two. Do not coin a fifth family or a sixth rung: a feature that fits none is a flag.
8. **Vendors and model providers.** Assess, rank, compare or recommend none, and map no real product line or AI feature. Name one only to attribute a dated public statement or its own documentation to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every entry alike. A company a peer-reviewed study names as its setting is named as that setting only. Worked examples use Halvern Systems, Varnby Software and Kestrow and their fictional features and claims, labelled fictional. Never say or hint which real company or product a fictional one resembles.
9. **Analysts, surveys, statistics.** Say how each report was read. If only the abstract or a release could be opened, the unit states only what that states. A consultancy's survey is vendor-reported. A prediction is called a prediction. A statistic is followed to the work that first reported it, or the unit says the origin was not found.
10. **Law.** Name the jurisdiction. Read the text or the authority's own page on the day and date it. Never cite a law firm's or a consultancy's summary. Put every legal point as a question with the body to consult.
11. **The case** comes from `case-facts.md` only; invented facts go in the notes. No case operation uses a real product or a real company's model.
12. **Scope.** No demand forecasting or inventory planning; no robots or their control; no method taught; no mathematics beyond arithmetic; no code; no interview framing; no pointer to another course's unit by code; nothing about the Project's owner, his employer, its products, his role or his work. No method for covert monitoring of a person and nothing on avoiding a duty to inform or consult.
13. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/notes.md` (a contradiction or a mistake under **Contradictions**, a mistake with the quoted passage, what is wrong, the source and the exact replacement; a need under **Needs**), naming every unit it affects and with a proposed change, so that the filer writes it into `syllabus-flags.md` in that file's form. It is carried by section 4. The writer never rewords a brief.
14. **The two closing sections** before the deliverable: "In a demo or a pilot review" and "Self-check", every answer drawn from the unit's sourced text.
15. **Hand-in.** The unit, `out/unit.md` (front matter, the unit, the deliverable, Sources); `out/sources.md`; `out/notes.md` with three lists, each item naming the unit codes it touches, an empty list written as "none": **Case facts** (rule 11), **Contradictions** and **Needs** (rule 13); the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, the number of references opened and not opened). `out/stats.json` is not the writer's: the chat writes it with `python3 kit/thin.py stats`.

## 2 · The fresh checker's eight passes

One fresh Opus 5.5 agent that has not seen the unit written, with live search. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.

1. **References exist and match.** Every Sources entry against its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
2. **Claims against sources.** Every cited claim opened and read against its source; "unverifiable" where the source will not open, never a pass. A statistic is checked at the work that first reported it.
3. **Grades and setting tags.** Each grade and each tag against AIE1's keys; a vendor's, a model provider's or a consultancy's statement never carries more than vendor-reported; an abstract-only reading is said to be one; no simulation or benchmark is written as a field result; a preprint is called one; a prediction is called one.
4. **Studies and transfers.** Every study reported with its setting, sample, design, comparison, period and measurer; every transfer from other work, another industry or an older model labelled as the unit's inference; from AIE6 on, every description of a study in AIE5's table agrees with that table.
5. **Families and rungs.** Each feature's family and rung against AIE1's keys; no new family or rung.
6. **Vendors and the case.** No real vendor or model provider assessed, ranked, compared, recommended or mapped; each named only as writer rule 8 allows; every list complete and alike; no private company's unpublished figure; every case fact against `case-facts.md`, labelled fictional, never used as evidence; no fictional claim repeated as a finding; nothing tied to a real company.
7. **Scope, law and tone.** Writer rules 10 and 12, line by line; every legal point with its jurisdiction, its text or authority, its date and its question; the preamble's tone rules; terms defined on first use.
8. **Deliverable and figures.** The deliverable against the brief's wording, built in full and then as a template; "In a demo or a pilot review" and "Self-check" present and agreeing with the body; every figure's labels and numbers traced to the text.

It also runs the unit against the course's part of the sourcing standard line by line and reads it as the reader in the preamble would.

## 3 · This row in particular

One paragraph per row, appended to the template by `next_prompt.py`.

| Row | Paragraph |
|---|---|
| W-AIE1 | Search on. This unit sets the family key, the ladder, the grade key and the setting-tag key that every later unit receives: define each so that two readers would agree, with a worked example each and two borderline cases decided. Read each definition of an AI system at its issuing body's own page; the standards are paid, so cite only what the body's page shows. State all sixteen common claims, set against only what this unit opens, each marked with the unit that tests it. |
| W-AIE2 | Search off. The decision inventory is the list AIE6 to AIE8 walk: fix its columns here. A deployment account written by the deploying company's own staff is vendor-reported for its results, whatever journal it is in. |
| W-AIE3 | Search off. Tag every result by setting; most learning-for-optimisation results are simulations. Claims C10, C11 and C15 belong here. |
| W-AIE4 | Search on. Features are given as types, never as claims about a named product. Read every model provider's documentation on the day, date it, and give the providers alike. Claims C4, C5, C12 and C14 belong here. Say plainly where no independent field study of a generative feature in execution software was found. |
| W-AIE5 | Search off. Read each of the eight studies in full text and say exactly what was read where full text would not open. The table's columns are reused by every later unit: fix them here. Describe no finding from memory. |
| W-AIE6 | Search off. Sets the decision card form reused by AIE7 and AIE8: fix its fields here. Cite the studies from AIE5's table. Claim C1 belongs here, in AIE7 and in AIE12. |
| W-AIE7 | Search off. Keep the shipper and the provider apart throughout. Say which region a document or a practice belongs to. |
| W-AIE8 | Search off. Order management has the least research of the three: say plainly where a section rests on practice or on vendors alone. |
| W-AIE9 | Search off. The human-factors research comes from other settings: state each study's setting and date, and label the transfer. Claims C7, C8, C9 and C13 belong here. |
| W-AIE10 | Search on. Every legal text is read at its issuing body's page today and dated; the EU dates changed in 2026, so take none from the seed bibliography's note. If an official page will not open, try the Official Journal's PDF found by search; if that fails, say "not opened" and state nothing from it. |
| W-AIE11 | Search on. Follow C2, C3, C4 and C6 each to its original and report the method, the sample and what was measured; if an original cannot be opened, the claim is "origin not opened". Real vendors appear as a dated list only. Claim C16 belongs here. |
| W-AIE12 | Search on. No private company's price. Every figure in the cost table is marked fictional. Claims C1 and C10 are closed here. |
| W-AIE13 | Search off. The worked brief uses only the course's sourced evidence and the case register; every figure marked fictional or sourced. Claim C12 is closed here. |
| W-DD-AIE1 | Search on. Law by jurisdiction, each text read today at its issuing body's page. Claims about pace, injury or jobs only from a regulator, peer-reviewed work or a named report with its method. The last unit: after it is filed, this same chat works every correction and flag still open (section 4, point 7). |

## 4 · The carry-forward rule (Pedro, standing; `docs/method.md` §9)

Nothing found goes unrecorded or waits for a later audit. It applies to every row of this course, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or Pedro.
2. **About a unit already filed.** It goes into the next row's prompt as a correction, with the unit, the passage, what is wrong and the source. The next row fixes it first, before it writes its own unit: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About a unit not yet written.** It becomes a flag in `syllabus-flags.md` naming every unit it affects, and it is printed in each of those units' prompts as a guideline for the writer. A flag that would change a brief is proposed, never applied by the row that raised it (section 5, point 6, says when it is settled).
4. **About the unit being written.** It is fixed in the same row before filing. What cannot be fixed (a source that will not open) is cut or marked unverified in the unit, and carried as in 2.
5. **Every row hands on to the next.** The next row's prompt is never typed or pasted: `kit/next_prompt.py` prints it when that row starts, in the same chat or the next one, from the repo as it then stands, so it already holds every correction still open on a filed unit, every open flag that names the unit, every carried proposal, and any guideline of this document that a row showed needs updating, with the update made. A row that finds a rule of the template wrong or unworkable corrects it in `docs/ai-in-supply-chain-execution-prompts.md` and says what it changed. What a chat's reply ends with is the starter (section 5, point 8).
6. **Nothing is dropped silently.** A correction or flag leaves the next prompt only when it is resolved, with the row and the report that resolved it written beside it.
7. **The last chat closes the course itself.** After W-DD-AIE1 is filed, the same chat works every correction and flag still open in the course, each checked by a fresh agent as in 2. It delivers a closing prompt only if something remains, and says why each remaining item could not be closed.

## 5 · The run plan

1. **The clone line.** Every prompt meant to be pasted into a session opens with exactly this line, and says nothing else about cloning, attaching the repo, registering it or approval:

   `Clone apcanario/learning (shallow, push access).`

   That holds for `setup-prompt.md`, for the starter and for the first line of this document's writing template. A chat that already holds the clone does not clone again.
2. **One starter for the course.** Every writing chat starts from the same two lines, which also resume a chat that stopped part-way:

   ```
   Clone apcanario/learning (shallow, push access).
AI in Supply Chain Execution, next bundle. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. Run `python3 kit/next_prompt.py --course ai-in-supply-chain-execution --bundle 4` and work what it prints in full, unattended.
   ```

   If `kit/next_prompt.py` has no `--course` option, the second line's command is `python3 kit/next_prompt.py --row <the first unit not yet filed> --bundle 4`, the row named by the reply that gives it. A bare `--bundle 4` is never used for this course: it takes the first unfiled row of the whole queue, which may be another course's.
3. **Setup runs alone.** S-AIE0 files the design, builds, verifies and publishes, and writes no unit. In `kit/next_prompt.py` it only adds the course to `QUEUE`, and it checks that another course's row prints byte-identical before and after. No `HOLDS` or `GATES` entry is made for this course.
4. **Bundles of four, in writing order.** Each writing chat is a thin Sonnet 5.5 main chat with fresh Opus 5.5 agents and takes the next four units not yet filed; the last chat takes what is left. As planned:

   | Chat | Rows |
   |---|---|
   | Setup | S-AIE0 |
   | Bundle 1 | W-AIE1, W-AIE2, W-AIE3, W-AIE4 |
   | Bundle 2 | W-AIE5, W-AIE6, W-AIE7, W-AIE8 |
   | Bundle 3 | W-AIE9, W-AIE10, W-AIE11, W-AIE12 |
   | Bundle 4 | W-AIE13, W-DD-AIE1, then the closing corrections |

   Each unit is written, fresh-checked, applied, filed, landed and published before the next begins, each by its own new packet folder and its own fresh writer, checker, applier and filer, so a chat that stops strands nothing. A chat that stops part-way is resumed by the starter, and the bundles after it shift by the units it left; nothing else changes.
5. **No gate rows.** Nothing in the queue waits for Pedro. A point where he reads before more is written sits on a bundle boundary, and his starting the next chat is the go. There is nothing for him to close by hand.
6. **Brief changes.** At the start of every writing chat after the first, before its first row's corrections, one fresh Opus 5.5 agent reads every open flag that proposes a change to a brief not yet written and decides each against the syllabus: apply it as an exact replacement in `briefs.md`, or decline it with the reason. Its report is saved as `audits/ai-in-supply-chain-execution/brief-review-<date>.md`, every change is listed in the chat's reply under "Brief changes, for veto", and a brief already written is never changed this way. The writing agents still never reword a brief.
7. **Unattended, and when to stop.** The chat never asks a question; where a prompt says ask, it takes the most reasonable reading and records it. It stops, leaves what is finished published and pushed, and says in the first line of its reply which row stopped and why, only when: the permission check refuses the repo's scripts; a writer or checker states a model that is not claude-opus-5-5; a unit gets a second `rewrite`; a reference that does not exist cannot be removed without emptying a section the brief requires; or the chat has been compacted or is close to the end of its context, in which case it finishes and closes the row in hand first. A flag never stops a bundle unless it makes the next brief unwritable as it stands.
8. **One reply for the whole chat.** Per row, what its own Reply paragraph asks, under the row's name. Then: the brief changes made, for veto; every proposal raised, each with what it does and a ⚠ on any disruption elsewhere (proposals are worked in the next row unless Pedro vetoes them); tasks for Pedro, left only where no agent can do the task, the expected answer being "none"; the backlog hand-off. The reply ends with the starter in a code block, never a long prompt. The last chat's reply ends with "course closed", or with the closing prompt of section 4, point 7.
9. **Beside other work.** Other chats may be landing on `main` while a bundle runs. Every row lands with `kit/land.py`, rebuilds from the landed HEAD before publishing, reads the live artifact first and never forces a publish.
10. **Recorded.** The chats are in the order section of `docs/ai-in-supply-chain-execution-syllabus.md`, and the writing rows in `docs/BACKLOG.md` are grouped under the same four bundle headings.
