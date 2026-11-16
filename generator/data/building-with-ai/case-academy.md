# Academy case file

The only source of facts about the running case of the course Building with AI. Compiled on 11 Nov 2026 from the Learning Project's own records (`docs/courses-index.md`, `docs/method.md`, `docs/CHANGELOG.md`, the audit log of the private courses' data file), with private details removed: the owner is "the owner", the two private courses are "the marketing course" and "the AI course", and nothing here says what they contain about him. A unit cites this file as "Academy case file" with the section. A unit that needs a fact this file does not hold lists it as a need; the fact is added here from the records, by the chat that files the unit, never by a writer.

One project by one person is an anecdote. Nothing below is evidence about AI tools in general.

## 1 · What it is

- Academy is a library of self-study courses, built by one person with Claude in October and November 2026 and published as one website with one design.
- At 11 Nov 2026 it holds five written courses in four subjects: two history courses (78 and 79 long-form reports), a marketing course (11 units), an AI course (11 units) and a UX course (15 units): 194 units.
- A unit is a long-form report in Markdown, 2,000 to 6,000 words by guide (the longest UX unit is about 16,900 words), with its sources cited in place and a closing deliverable built in full.
- Everything lives in one private repository: the course texts, the briefs, the build scripts, the method, a backlog and a changelog. The site is built from the repository by script; no page is styled by hand.

## 2 · The method, as run

- **Syllabus first.** A course starts as a goal in one sentence, three measurable outcomes, eight to twelve core units and two or three deep dives, each unit with a one-line scope, a named deliverable and a brief.
- **One brief per unit, never reworded.** A shared preamble (the reader, the goal, the sourcing standard, the tone) is joined to each unit's own brief, so every context is self-contained.
- **One context per unit.** Each unit is written in a new chat or a fresh agent context that sees only its brief and the units already filed. The stated reason: leaked context is how a course starts repeating itself.
- **The writer's own pass.** Before handing in, the writer runs the sourcing checklist and lists up to ten claims it could not verify.
- **A fresh check.** A separate context that has not seen the unit written checks every cited claim against its source and the deliverable against the brief. It writes findings (error, should-fix, minor) and never edits. A maintainer verifies each finding and applies it as an exact replacement.
- **A sample audit every four units.** One claim is drawn from every section of each unit and checked against its source. A unit with more than one sampled claim in ten failing is audited in full. Verdicts: pass, full audit, rewrite.
- **A staleness check** six months after any unit written with live search.
- **Models.** One model (Opus 5.5) writes; a different model (Fable 5.1) audits. The model that wrote each unit is recorded.
- **A backlog and a changelog.** Every chat works one row of the backlog; a finished row moves to the changelog; a task the work uncovers is added as a proposed row and is not worked until the owner confirms it; each chat ends by writing the prompt for the next.

## 3 · What the first audit found

- The first three marketing units were written from one research report produced by research agents across five tracks.
- Audit 1 sampled them: one of eight sampled claims failed, which triggered a full audit. Of 91 claims, 23 failed and none was stale. Nothing was invented and no conclusion flipped.
- The verdict was rewrite, for two reasons: the three deliverables did not exist, and two table rows rested on figures the cited vendor pages did not contain.
- The pattern the audit named: qualifiers the source does not carry.
- The same audit passed the first AI unit: seven of seven sampled claims held.
- Consequence: the three units were rewritten from their briefs the same day, and from then on every unit of that family got a fresh check before filing.

## 4 · What the second audit found

- Audit 2 covered four units: 28 claims sampled, 96 checked in all. No sampled claim failed; one incidental claim failed (a miscited caption).
- Ten claims were stale, all in one unit and all from one cause: an independent benchmark published a new index version the day before the unit read its leaderboard.
- All four units passed; 26 errata were applied the same day.

## 5 · Errors at the fresh check, per unit

The 36 units that got a fresh check before filing (the marketing, AI and UX courses; the first AI unit predates the rule). Counts are the checker's findings on the writer's handed-in draft.

| Course | Unit | Checker | Verdict | Errors | Should-fix | Minor |
|---|---|---|---|---|---|---|
| Marketing | A9 | Fable 5.1 | fix | 2 | 15 | 8 |
| Marketing | A2 | Fable 5.1 | fix | 3 | 13 | 11 |
| Marketing | A6 | Fable 5.1 | fix | 1 | 9 | 7 |
| AI | B2 | Fable 5.1 | fix | 3 | 10 | 14 |
| AI | B3 | Fable 5.1 | fix | 1 | 4 | 9 |
| AI | B4 | Fable 5.1 | fix | 0 | 7 | 9 |
| Marketing | A1 | Fable 5.1 | fix | 1 | 4 | 6 |
| AI | DD-B3 | Fable 5.1 | fix | 1 | 3 | 9 |
| Marketing | A3 | Fable 5.1 | keep | 0 | 1 | 9 |
| AI | B5 | Fable 5.1 | fix | 1 | 4 | 5 |
| Marketing | A4 | Fable 5.1 | fix | 2 | 3 | 8 |
| Marketing | A5 | Opus 5.5 | fix | 1 | 4 | 8 |
| AI | B7 | Opus 5.5 | fix | 1 | 4 | 8 |
| Marketing | A7 | Opus 5.5 | keep | 0 | 3 | 6 |
| Marketing | A8 | Opus 5.5 | fix | 2 | 8 | 7 |
| AI | B6 | Opus 5.5 | fix | 3 | 8 | 12 |
| AI | B8 | Opus 5.5 | rewrite | 4 | 4 | 4 |
| Marketing | DD-A1 | Opus 5.5 | fix | 3 | 6 | 6 |
| AI | DD-B1 | Opus 5.5 | fix | 0 | 10 | 14 |
| Marketing | DD-A2 | Opus 5.5 | fix | 0 | 5 | 5 |
| AI | DD-B2 | Opus 5.5 | fix | 3 | 4 | 5 |
| UX | IA1 | Opus 5.5 | keep | 0 | 4 | 7 |
| UX | IA2 | Opus 5.5 | fix | 3 | 10 | 17 |
| UX | IA3 | Fable 5.1 | keep | 0 | 2 | 6 |
| UX | IA4 | Fable 5.1 | fix | 2 | 18 | 9 |
| UX | IA5 | Fable 5.1 | fix | 2 | 3 | 5 |
| UX | IA6 | Fable 5.1 | fix | 2 | 4 | 11 |
| UX | IA7 | Fable 5.1 | fix | 0 | 6 | 3 |
| UX | IA8 | Fable 5.1 | fix | 1 | 3 | 9 |
| UX | IA9 | Fable 5.1 | fix | 1 | 3 | 8 |
| UX | IA10 | Fable 5.1 | fix | 3 | 3 | 3 |
| UX | IA11 | Fable 5.2 | fix | 2 | 13 | 10 |
| UX | IA12 | Fable 5.2 | fix | 3 | 8 | 13 |
| UX | DD-IA1 | Fable 5.2 | fix | 2 | 12 | 20 |
| UX | DD-IA2 | Fable 5.2 | fix | 2 | 11 | 7 |
| UX | DD-IA3 | Fable 5.2 | fix | 3 | 8 | 5 |

- Totals: 58 errors, 237 should-fix, 303 minor across 36 units.
- 8 of the 36 drafts had no error at the fresh check; 28 had at least one.
- A count kept in one AI unit at the time it was written: fifteen of the first twenty drafts had an error at first check.
- Kinds of error the reports name: a figure the cited page does not carry; an author named wrongly; a law that had changed; a quotation the page does not hold; a count that did not add up; a product fact that differed between two of the vendor's own pages.

## 6 · Figures

- Units declare figures as data; a script draws them. A separate agent checks each figure against the unit's text: every label and number must already be in the text.
- A figure that failed was fixed and checked again by a new agent. Early rule: a figure that fails three times is dropped (two were). Later rule, set by the owner: figures are never dropped; they are fixed until they pass. One sitemap figure passed on its eighth check.

## 7 · What failed in operation

- Writer agents were lost to container restarts: one deep dive lost two writers, and the third resumed from the second's working files.
- Some sessions kept no agent transcript on disk, so scripted checks of what each agent had read could not run; the agents' own reports stood in their place.
- A session's model named "fable" resolved to a newer version than the method names, so the checks it ran were recorded as owed again on the named version.
- A structure audit of the project itself (the source of unit BW4) made seventeen findings, among them: project instructions that carried procedures and paraphrased the method file, and private terms reaching a public build.

## 8 · One person's usage, reviewed

- The owner's chats in the project were reviewed for one deep dive: 53 chats over six days (the project's whole history at the time).
- By model, read from commit trailers: 31 chats ran on Opus, 18 on Fable, 4 on both.
- Each ask was classified by task type, model, outcome and number of turns. The labels were applied by hand; "accepted" was a proxy; 14 endings were not seen.
- The review produced ten changes, ranked, each tied to a count.

## 9 · What the record does not hold

- No measure of hours or money spent per unit.
- No control: no unit was written without the method to compare.
- No second project and no second person.
- Audits 3 onward of the marketing, AI and UX courses had not run at 11 Nov 2026.
§7 · BW1 of this course (15 Nov 2026) was checked from a Claude Code session on claude.ai (claude.ai/code, recorded in its fresh-check report); the checker was a separate context that read only its packet, its write of its report was refused, and the chat saved the report from the checker's reply. The record does not say which plan the project runs on, whether memory was on, or any token or window measure for a unit.
§2 · This course (Building with AI) names its reader in its shared preamble: an experienced professional who reasons and writes well, uses a chat assistant with no method, may not write code, and brings one real project. Its goal in one sentence: by the end of the course the reader can say what the model saw when an output fails; brief a task so that the first output is usable and keep a project structure that does not rot; verify AI-written work by sample before trusting it; and decide what to hand to an agent, with one real project of their own specified and running (the course's data file, 11 Nov 2026).
§2 · Syllabus flags (this course's syllabus-flags file): a chat that writes a unit raises a flag for each contradiction between units or briefs and each need the syllabus does not meet; a flag that would change a brief waits for a syllabus review that the owner confirms; the file sets no fixed date for a review. At 16 Nov 2026, before BW5's flags were added, 34 flags had been raised (at the course's creation and by BW1 to BW4): 26 open, 7 carried, 1 resolved by a correction; none had been resolved by a syllabus review.
§1 · Publishing (the course's data file, Build page; the filing rules of 15 Nov 2026): after a unit is filed, the course's data file is updated and the site is rebuilt by script, verified and published in two places, first as an artifact on claude.ai and then on GitHub Pages. A script checks the course index after each filing chat inserts its records and restores every file if the check fails.
§7 · A private-terms check exists (the course's data file): no private term may appear in this public course's data folder, checked by a script against a list, and this course's fresh checker also checks each unit against that list. The record does not say when the check was added relative to the structure audit.
§2 · From BW7 of this course (16 Nov 2026), the fresh check's findings were applied by a separate agent context, the applier, running Opus 5.5, which may add companion edits a finding implies; writer, checker, applier, filer and corrections checker were each a fresh agent (the row's record). The record does not say who applied the findings for the earlier units of §5.
§1 · Layout (the course index and this course's data file, 16 Nov 2026): the repository keeps one course index, with a table per course giving each unit's status, model, search setting and file path and a count of units written, and a table of the staleness checks due; this course's build order is a list in its data file (unit, model, search), with the next unit named there. The record does not say whether the repository holds files named INDEX.md, INSTRUCTIONS.md or BUILD-ORDER.md in BW4's and BW5's form.
