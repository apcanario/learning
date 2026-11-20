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
§7 · From BW9 of this course (16 Nov 2026; the row's fresh-check and corrections reports): the fresh checker and the two corrections checkers each ran with web search and page fetch, opening only addresses a search in that agent had returned, and ran scripts (each confirmed by script that every text it proposed to replace occurs once in its file); each was refused a write of its report file and returned its report as text, which the chat saved verbatim before any change was applied. The records do not say which permission mode any agent ran in, or which tools the writer, applier, filer or figure checkers held.
§1 · Filed units (the course index, 16 Nov 2026): every filed unit is one Markdown file in a folder per course; this course's folder is courses/building-with-ai/, one file per unit named by its code and title (for example BW9-agents.md), and a unit counts as written when its file is in that folder. At 16 Nov 2026 it holds BW1 to BW9.
§2 · From BW10 of this course (16 Nov 2026; the row's record): the row's prompt asked for a main chat on a smaller model (Sonnet 5.5) that only staged packets, filed and recorded; the session ran Opus 5.5 and is recorded as such. Writer, fresh checker, applier, two corrections checkers and filer were each a fresh Opus 5.5 agent.
§5 · BW10 of this course (16 Nov 2026; its fresh-check report, checker Opus 5.5): fix, 0 errors, 7 should-fix, 11 minor. The applier applied 14 findings and held 4 whose proposed fix was itself wrong (a quotation's case, an OpenAI rate and its companion edit, a parenthetical), then wrote corrected fixes for those 4, applied in a second pass: all 18 applied.
§2 · From BW10 of this course (16 Nov 2026; the row's first corrections report): a corrections checker passed 4 of 5 replacements and failed 1 that the writer had proposed to an earlier unit of the AI course: the text it would have changed quoted another unit's claim, and the word it called wrong was not wrong; the new fact behind it went into that unit's own cell instead, and a second, fresh checker passed that replacement.
§7 · BW10 of this course (16 Nov 2026; the row's record): every agent of the row was refused a write of its report file; the chat saved the fresh checker's report verbatim from its reply.
§1 · Filed units (the course index, 16 Nov 2026, after BW10): this course's folder, courses/building-with-ai/, holds BW1 to BW10.
§5 · DD-BW1 of this course (16 Nov 2026; its fresh-check report, checker Opus 5.5): fix, 3 errors (all three in figures that carried facts the text did not), 20 should-fix, 12 minor. The applier applied 33 findings and held 2 whose proposed fix was itself incomplete or wrong (a case cell that needed 'From BW7 on'; a quotation that is about tasks), then wrote corrected fixes for those 2, applied in a second pass: all 35 applied.
§2 · DD-BW1 of this course (16 Nov 2026; the row's record): the row was the second of three rows run in one main chat; the prompt asked for a main chat on a smaller model (Sonnet 5.5) and the session ran Opus 5.5, recorded as such. Writer, fresh checker, applier, filer and two corrections checkers were each a fresh Opus 5.5 agent.
§2 · DD-BW1 of this course (16 Nov 2026; the row's corrections reports): a corrections checker passed 7 of 8 replacements the writer proposed to earlier units and failed 1, an author line, because no search returned the address the replacement cited, so it could not be checked; a second, fresh checker re-checked 2 of the 7 and passed them.
§7 · DD-BW1 of this course (16 Nov 2026; the row's record): every agent of the row was refused a write of its report file; the chat saved the reports verbatim from their replies.
§1 · Reading pages (the course's data file, 16 Nov 2026): each filed unit's reading page on the site opens with an introduction that says the unit was written by an AI model and names the model, and that a separate model in a context that had not seen the writing checked it, with the check's counts.
§9 · The record does not say whether the owner reads each unit before publishing, any budget or stop set on agent runs, which tools and connectors each agent held, or the effort setting used for each unit (DD-BW1's Need 1, 16 Nov 2026).
§1 · Filed units (the course index, 16 Nov 2026, after DD-BW1): this course's folder, courses/building-with-ai/, holds BW1 to BW10 and DD-BW1.
§5 · BW1 to BW9 of this course (15 and 16 Nov 2026; the front matter of each fresh-check report, audits/building-with-ai/fresh-check-BW1.md to fresh-check-BW9.md, checker Opus 5.5 on each), verdict and errors, should-fix, minor: BW1 fix, 1, 7, 7; BW2 fix, 1, 5, 10; BW3 fix, 0, 8, 11; BW4 fix, 2, 5, 5; BW5 fix, 1, 5, 12; BW6 fix, 1, 7, 3; BW7 fix, 2, 7, 11; BW8 fix, 3, 9, 11; BW9 keep, 0, 7, 11.
§5 · DD-BW2 of this course (16 Nov 2026; its fresh-check report, checker Opus 5.5): fix, 2 errors, 12 should-fix, 10 minor. The applier applied 21 findings and held 3 whose problem was real but whose proposed fix was wrong, then wrote 8 entries applied in a second pass (5 companion edits and corrected fixes for the 3 held): all 24 findings resolved, in 29 replacements. The checker was given the course's filed units as well as its usual packet, to check the unit's pointers.
§2 · DD-BW2 of this course (16 Nov 2026; the row's record): the row was the third of three rows run in one main chat; the prompt asked for a main chat on a smaller model (Sonnet 5.5) and the session ran Opus 5.5, recorded as such. Writer, fresh checker, applier, filer and corrections checker were each a fresh Opus 5.5 agent. The writer's packet held none of the fresh-check reports, audit reports or changelog its brief names, so the unit was written from this file and the course's filed units.
§7 · DD-BW2 of this course (16 Nov 2026; the row's record): the applier was stopped once by a server restart and resumed automatically from its transcript. Every agent of the row was refused a write of its report file; the chat saved the reports verbatim from their replies.
§1 · Filed units (the course index, 16 Nov 2026, after DD-BW2): this course's folder, courses/building-with-ai/, holds BW1 to BW10, DD-BW1 and DD-BW2.
§2 · Added 17 Nov 2026 by this course's syllabus review (BW-1, row S-BW), from the Project's records (audits/building-with-ai/syllabus-review-BW-1-records.md), private details removed; each line names its record. A unit filed before that date may still say a fact below is not in this file (carried proposal CP-4).
§1 · A second marketing course, public, of 12 units, was created on 11–12 Nov 2026 with this course (the kit changelog); this file calls it 'the public marketing course'.
§7 · Surfaces (the method's Home line, 28 Oct 2026; the AI course's B4, Deliverable A and unsure item 1, 29 Oct 2026; the project changelog's session links, 10 to 17 Nov 2026): the project's chats ran in one claude.ai Project, which holds copies of files from the repository; filing and writing rows from 10 Nov 2026 on ran as Claude Code sessions on claude.ai attached to that Project, and the Project's documents were seen there as a list by name, which may differ from what a claude.ai chat receives.
§7 · Memory (the AI course's B4, finding F13, 29 Oct 2026; the AI course's DD-B2, §5, 2 Nov 2026; the B4 fix list, 16 Nov 2026): on the Project's setup as of 28 Oct 2026 account memory flowed into the Project beside the Project's own memory store; in 6 of 53 chats reviewed for DD-B2 the visible turns show the model calling the memory tool; on 16 Nov 2026 the setting was not visible in the records.
§7 · Window and retrieval (the AI course's B4, finding F1, 29 Oct 2026, figures as corrected 15 Nov 2026): the Project's knowledge held 33 files, 907,260 characters (about 363,000 tokens at 2.5 characters a token); whether the Project ran in retrieval mode depended on the model and was not known.
§7 · Token measures (the kit changelog, 27 Oct and 14–15 Nov 2026): the history courses' curated bibliographies were written by one Sonnet 5.5 agent per unit group, 26 groups, about 4.5 million tokens; the public marketing course's four audits used 2.83M tokens for the twelve unit audits and 3.64M for every agent measured.
§7 · A failure traced to a chat's length (the project changelog, 12 Nov 2026): a chat that had filed two units could not refresh the remaining Project copies, because each needed its whole text read into the chat and the chat's context could not hold it after two units; the rest moved to a later row.
§7 · Usage limits (the kit changelog, 25 Oct 2026; the project changelog, 14 Nov 2026): the largest history writing session (28 reports) stopped twice on usage limits and resumed both times; an audit chat on 14 Nov 2026 was stopped by a shorter-window limit of the auditing model after 18% of that model's weekly allowance.
§8 · Model by task type (the AI course's DD-B2, §2 table, over the 53 chats of 28 Oct to 2 Nov 2026, model read from commit trailers): unit writing 15 chats, Opus 5.5 14, switched 1; infrastructure (build, repository, publishing, method and skill files) 15, Opus 5.5 5, Fable 5.1 8, switched 2; figure passes 7, Opus 5.5 6, Fable 5.1 1; audits and fresh checks 6, Opus 5.5 1, Fable 5.1 5; status questions 6, Opus 5.5 3, Fable 5.1 2, switched 1; syllabus design 2, Fable 5.1 2; history-module writing 2, Opus 5.5 2. None ran on Sonnet 5.5 or Haiku 5.5.
§2 · Syllabus chats (the method, 15 Nov 2026; the project changelog): from 15 Nov 2026 course design and syllabus chats run on Fable; the two public courses were created on Fable 5.2 (11–12 Nov 2026) and the UX syllabus review ran on Fable 5.1 (3 Nov 2026).
§2 · Extraction (the kit changelog, 27 Oct 2026): the curated bibliographies of the 137 history reports then written were made by Sonnet 5.5 agents, one per unit group.
§2 · Effort (the AI course's DD-B2, §1 and §3, 2 Nov 2026): the effort setting is recorded in none of the 53 chats reviewed.
§5 · Writing model of the 36 fresh-checked drafts (the course index, unit tables): every one of the 36 was written by Opus 5.5.
§3 · The research report's agents (the course index; Audit 1's provenance note, 28 Oct 2026): the research report behind the first three marketing units was written on 27 Oct 2026 across five tracks by Fable 5.1 research agents.
§4 · Auditing model (the course index; the project changelog): Audits 1 and 2 of the marketing and AI courses ran on Fable 5.1 (28 and 29 Oct 2026); the four audits of the public marketing course ran on Fable 5.2 (14–15 Nov 2026); no audit of the private courses or the UX course ran after Audit 2 (see F105).
§2 · Briefs and prompts (the method §4 and §6, 15 Nov 2026; this course's data file): a brief is the course's shared preamble, written once and never edited per unit, followed by the unit's own brief; this course's preamble and briefs are public in its data file and on its Briefs page; the staleness check is run with one fixed prompt that the method gives word for word; the private courses' briefs are not reproduced here.
§2 · Length (the kit changelog, rules set by the owner on the afternoon of 27 Oct 2026; the method §4): the owner set that length is a guide, not a law: a topic takes the words it needs; the word-count script reports the count as a note and never fails on it; padding is the fault, length is not; the rule was then carried into the method for every course.
§5 · Long units at the fresh check (the AI course's B4 fresh-check report, 29 Oct 2026): the checker counted B4 at 8,508 words against the brief's 2,000–6,000 and, on the method's length rule, found nothing in it to be padding.
§2 · Records of later units (the project changelog, 12–13 Nov 2026): several units of the public marketing course were filed "above the brief's guide", the record noting that the length rule lets the topic decide.
§7 · Structure audit F1 (B4, 29 Oct 2026): layer Project knowledge; the knowledge held 33 files, 907,260 characters, mostly files no chat needed whole (size); fix: cut it to five files and read the rest from the repository by path; severity high. Status 16 Nov 2026: still applies (filed units removed from the knowledge on 15 Nov 2026).
§7 · Structure audit F2 (B4): layer Project knowledge; the project instructions were also uploaded as a knowledge file, the same text reaching the Project twice (duplicate); fix: remove the knowledge copy; severity low. Status 16 Nov 2026: still applies (reading; no record of removal).
§7 · Structure audit F3 (B4): layer Project knowledge; the knowledge copy already lagged the repository: two units filed on 29 Oct 2026 were missing from the list seen the same day (stale); fix: stop mirroring units, refresh the rest from the repository; severity low. Status 16 Nov 2026: done (units are no longer mirrored, and every chat rewrites the copies it changes).
§7 · Structure audit F4 (B4): layers repository and knowledge; two different files carried the same name, one the queue of chats and one a writing-lane file, with 39 references by bare name in 16 files; fix: rename one and repoint the references; severity low. Status 16 Nov 2026: still applies.
§7 · Structure audit F5 (B4): layers the owner's account preferences and the project instructions; three preferences collided with the Project's work (contradiction): a format rule, a concision rule and a rule against volunteering next steps, against long-form Markdown units and the required hand-over; fix: one clause in the preferences and a scope paragraph in the instructions; severity medium. Status 16 Nov 2026: no longer applies (reading).
§7 · Structure audit F6 (B4): layers preferences and theme; the design preferences and the site's theme agreed; no fix; recorded so a later audit would not re-check it. Status 16 Nov 2026: no longer applies.
§7 · Structure audit F7 (B4): layer project instructions; the instructions (675 words) carried procedures and paraphrased the method file (duplicate); fix: replace them with rules and pointers; severity medium. Status 16 Nov 2026: still applies (the instructions had grown to 862 words).
§7 · Structure audit F8 (B4): layers method, setup file, data file; four prose copies of the list of units that search, in three versions (duplicate, contradiction); fix: point each to the course index's Search column; severity medium. Status 16 Nov 2026: still applies.
§7 · Structure audit F9 (B4): layers repository docs and data file; stale files and lines still read as current (stale): an old hand-off note, retired page blocks rendered on the site, a wrong due date, a contradictory lane heading, two references to a retired build script; fix: archive or correct each, then rebuild and publish; severity medium. Status 16 Nov 2026: still applies (one of five parts done).
§7 · Structure audit F10 (B4): layers queue and changelog; the queue and the record were behind the work: two filed units still queued, no changelog row (stale); fix: move both rows; severity medium. Status 16 Nov 2026: done.
§7 · Structure audit F11 (B4): layer build; the theme reached the build through a hand copy that no check compared; fix: build from the theme directly, or fail the verify script on a mismatch; severity low. Status 16 Nov 2026: still applies (reading).
§7 · Structure audit F12 (B4): layers method and data file; the two audit prompts lived in two files, identical that day (duplicate); fix: a rot check, then generate one copy from the other; severity low. Status 16 Nov 2026: no longer applies (reading; the sample-audit prompt retired 15 Nov 2026).
§7 · Structure audit F13 (B4): layer memory; account memory flowed into a Project whose output is published; fix: turn off account memory for the Project; severity high. Status 16 Nov 2026: still applies (reading; the setting not visible in the records).
§7 · Structure audit F14 (B4): layer connectors; eight connectors were connected and no Project procedure used one; fix: set tool access to load on demand; severity low. Status 16 Nov 2026: still applies (reading).
§7 · Structure audit F15 (B4): layer the build and the data it reads; private terms reached three files of the public build (privacy); fix: a build-time redaction list kept outside both repositories, an erratum, a verify-script check, and the owner's decision on the public repository's history; severity high. Status 16 Nov 2026: still applies (residual; a terms list and a checker exist; the erratum, the scan's scope and the decision not shown).
§7 · Structure audit F16 (B4): layer scheduled tasks; nothing checked for rot between sessions (no scheduled task); fix: a weekly scheduled rot check; severity medium. Status 16 Nov 2026: still applies.
§7 · Structure audit F17 (B4): layer the course index; the index every chat needs was 56% a finished record (size); fix: split it into a live index and an archive; severity low. Status 16 Nov 2026: still applies.
§7 · Structure audit, status (the fix list, 16 Nov 2026): of B4's seventeen findings, 12 still apply, 2 are done (F3, F10) and 3 no longer apply (F5, F6, F12); none had been worked.
§7 · Mirror lag (the AI course's B4, finding F3, 29 Oct 2026): two units filed on 29 Oct 2026 were not in the Project's knowledge list seen the same day, although the filing procedure required the re-upload.
§7 · Mirror lag (the project changelog, 28 Oct 2026): the build kit handed over to be put into the new repository was the previous session's copy, not the latest; the later session's changelog entry was restored from the live page.
§7 · Mirror lag (the project changelog, 12–13 Nov 2026): after two units were filed in one chat, ten Project copies were stale and were re-uploaded from the repository by a separate correction row the next day, the first chat's context having been unable to hold them.
§7 · Site lag (the kit changelog, 10 Nov 2026; the project changelog, 12 Nov 2026): a prompt corrected in the repository after a publish stayed uncorrected on the site's Backlog page until the next publish, the repository being canonical; on 12 Nov 2026 the published Backlog page showed a confirmed item as still proposed until the next publish.
§7 · The second publishing place behind the first (the kit changelog, 12–15 Nov 2026): in five filing sessions the site was published as the claude.ai artifact but not deployed to GitHub Pages (the repository attach refused or outside the session's set); later rows deployed it.
§7 · Mirror rule (the method §8 step 4, 15 Nov 2026): each chat that works a row rewrites the Project copies of the backlog and changelog in full, so the Project knowledge never lags the repository; units are not mirrored.
§7 · Stopped and restarted work (the project changelog and kit changelog, 2 to 16 Nov 2026): on 3 Nov 2026 the owner stopped a UX writing row before its writer had a draft, its one commit was reverted, and a syllabus review the same morning added Aim, Takes and Gives lines to every unit brief of that course and closed four briefs at their seams, which the owner approved; a writer sent its prompt with the brief left as a placeholder was stopped before its first tool call and a new one started (2 Nov 2026); a writer of the public marketing course was stopped by the owner before it saved anything and started again from scratch (13 Nov 2026); a mapping agent's first run stopped because two of its tools were not loaded, and it was resumed (16 Nov 2026).
§3 · Rewrites from the brief (the course index): the three marketing units Audit 1 failed were rewritten from their briefs on 28 Oct 2026, each in its own chat; one section of a marketing unit was rewritten on 29 Oct 2026 and re-checked.
§1 · One course's build order (the course index, 3 Nov 2026): the two private courses' 22 units in build order, with the date each was written: A9, A2, A6 and B1 (28 Oct 2026), B2 (28 Oct), B3, B4, A1, DD-B3, A3, B5, A4 (29 Oct; A1 written out of order beside B3), A5 (1 Nov), B7, A7, A8, B6, B8, DD-A1, DD-B1, DD-A2 (2 Nov), DD-B2 (3 Nov, last of both courses, since it reviews the chat history).
§2 · Decision dates (the method and the kit changelog): length a guide, not a law (27 Oct 2026); the per-unit fresh check made a rule for the marketing and AI courses after Audit 1 (28 Oct 2026); the repository as the single home (28 Oct 2026); an isolated agent context counts as a new chat (29 Oct 2026); the figure pass added to writing (29 Oct 2026); each chat writes the next row's prompt (31 Oct 2026); every new course a Markdown course (31 Oct 2026); figures fixed until they pass, never dropped (3 Nov 2026); corrections made in the chat that finds them (12 Nov 2026); the standing proposals rule, the thin main chat, units not mirrored into the Project, the end of the audit stage and the site's Backlog and Changelog drawn from one plain log (15 Nov 2026).
§5 · Findings not applied as given (the course index and the fresh-check reports' maintainer notes, 28 Oct to 10 Nov 2026): A2, one note not applied; A8, one finding held in part; DD-A1, one applied in part; DD-B2, one error applied in part and one should-fix not applied; IA3, one held in part; IA5, one in part and one needing no change; IA6, one pointer that held, not applied; IA8, the search-flag finding not applied (the flag kept off); IA10, one minor recorded at its own fix of no change; IA11, one in part; DD-IA2, three minors needing no change; DD-IA3, one minor needing no change. Every other of the 36 units' findings is recorded as applied.
§5 · This course (the project changelog, 15–16 Nov 2026): BW5, 17 applied and 1 held; BW6, 12 applied and 1 held (the search flag); BW8, 22 applied and 1 held; DD-BW3, 12 applied and 2 minor held; BW1 to BW4, BW7 and BW9 all applied.
§3 · Audit 1 (Audit 1's report, 28 Oct 2026): the three marketing units were audited as one document of nine sections, 91 cited claims in the full audit; B1 had seven sections and a deliverable.
§4 · Audit 2 (Audit 2's report, 29 Oct 2026): one claim per numbered section plus the deliverable: B2 9 sampled and 23 checked, B3 6 and 28, B4 6 and 20, A1 7 and 25.
§1 · Sections (the project changelog, 1 Nov 2026): every unit and report then on the site, 152 pages, held 1,581 sections.
§4 · The public marketing course's audits (the kit changelog, 14–15 Nov 2026): 155 claims sampled and 712 checked over twelve units.
§4 · Audit 2 (its report, 29 Oct 2026): run on 29 Oct 2026 by Fable 5.1 with live search, in its own agent context that had not seen the writing, over B2, B3, B4 and A1; B2's sample was 0 of 9 failing with 3 stale, so 3 of the 10 stale claims were among the 28 sampled and 7 were found while checking beyond the sample; the decision rule was applied to the sample only.
§4 · Later audits: the public marketing course's audits ran on Fable 5.2 (§4, Auditing model, above); for why Audits 3 onward did not run, see §9 below.
§2 · Who applied findings (the method §5; the fresh-check reports' maintainer notes; the project changelog, 28 Oct to 15 Nov 2026): until 14 Nov 2026 the findings were verified and applied by the chat that orchestrated and filed the row, recorded as "the maintainer"; that chat ran on Opus 5.5 except where the row's record names another model: Fable 5.1 in two UX rows (9 Nov and 3 Nov 2026) and Fable 5.2 in one (10 Nov 2026); from 15 Nov 2026 (this course's BW1) a separate Opus 5.5 agent, the applier, applied them.
§1 · Gates before publishing (the method, 15 Nov 2026; the kit changelog): before a publish, scripts must pass: the build's verify script, the course-index check and the private-terms check, then the publish is read back by sha256; attaching the public repository for the second publish was several times refused by the session's permission check and done only after the owner approved it.
§6 · Figure checkers' model (the kit changelog, 30 Oct 2026 on): every figure check and re-check was run by a separate Opus 5.5 agent.
§6 · How re-runs were recorded (the course index; the fresh-check reports): each figure's check count is recorded in the unit's course-index row ("passed on its third check") and in the fresh-check report's maintainer note on the re-check; a row run again is recorded as its own changelog row.
§7 · Private-terms check, start (the kit changelog, 11–12 Nov 2026): the script that fails the build on a private term in a public course was added when the two public courses were created on 11–12 Nov 2026, after the structure audit of 29 Oct 2026.
§7 · Skills (the AI course's B4, layer table, 29 Oct 2026; the project changelog, 3 Nov 2026; the method): the project kept four skills in its repository, for writing a unit, running a fresh check or audit, filing a unit and starting a course; they were installed on the owner's account under Customize > Skills by hand from files built from the repository (last on 3 Nov 2026, checked identical to the repository's copies); the method tells a chat to file with the filing skill and to run fresh checks with the checking skill.
§1 · Layout names (the method, the course index, B4 F2 and F8): no file named INDEX.md, INSTRUCTIONS.md or BUILD-ORDER.md appears in the records; their equivalents are `docs/courses-index.md` (the index), `docs/project-instructions.md` (a copy of the Project's instructions field) and each course's build order as a list in its data file.
§7 · Scheduled tasks (the AI course's B4, 29 Oct 2026; the B4 fix list, 16 Nov 2026): no scheduled task existed on the setup as of 28 Oct 2026, and none appears in the records of 16 Nov 2026; the weekly rot check B4 proposed was not created.
§7 · Unattended runs instead (the project changelog, 29 Oct to 14 Nov 2026): several rows were run as chats left unattended overnight or with the owner away, among them two figure-renderer rows (29–30 Oct 2026), two units (1–2 Nov 2026) and the public marketing course's units in pairs (12–14 Nov 2026).
§7 · Agents' tools (the kit changelog, 2 to 10 Nov 2026): where transcripts were kept, a script checked each agent's tool use: writers used search and fetch and no connector, memory, Projects or Artifact tool, each fetched address one a search had returned; page checkers used only read, glob and grep inside their folder; figure re-checkers used no web tool; the AI course's usage-review writer alone was given the past-chat tools.
§7 · Commits and branches (the method, 15 Nov 2026; the AI course's DD-B2, §7 and change 9): a checkpoint commit follows every agent; the history courses' figure passes worked on side branches; of 39 row asks held as text in the six reviewed days, one names a branch and none a worktree.
§7 · Caps (the kit changelog; DD-B2): figure passes ran at most eight agents at a time and dropped a figure that failed twice; the public marketing course's re-run auditors were held to 40 searches each; four figure-pass asks gave an attempt cap.
§7 · After lost writers and missing transcripts (the kit changelog, 3 and 10–12 Nov 2026): when the second writer was lost, a third resumed from its working files and the lost transcripts were checked by script; where a session kept no transcript on disk, the record says so and the model recorded is the one each agent stated.
§7 · Who publishes (DD-B2 §7, 2 Nov 2026; the method): the session that works the row publishes and deploys; in 13 of 16 row asks read in full the session was told to.
§7 · Where private material is kept (the B4 fix list, 16 Nov 2026; the project changelog, 17 Nov 2026): the private-terms list sits in the private repository, not in the public one the site is deployed from; the audit and review files linked from the site's How-it-was-built pages are kept in the private repository and open only to the site's owner; the usage review's working files and the chat history it read are not published.
§2 · Publishing without the owner present (the project changelog, 12–14 Nov 2026): several writing rows ran with the owner away; fresh agents wrote and checked the units, and the main chat staged, applied, filed and published them without waiting for the owner.
§7 · A publish repeated (the kit changelog, 4 Nov 2026): a layout fault found after a site change was published was fixed, rebuilt, verified and published a second time the same day; neither the change's checker nor the verify script had caught it.
§7 · A failed deploy (the kit changelog, 9 Nov 2026): one GitHub Pages run failed with no job run; an empty commit retriggered it, and its build and deploy jobs succeeded.
§7 · Publishes refused at first (the kit changelog, 2 to 10 Nov 2026): in 21 publish entries the publishing tool first refused, naming files the session had not read; the named files were read (in one entry, 191 files listed and eight compared), found equal to the build, and the publish made, never forced.
§7 · Deploys missed (the kit changelog and project changelog, 3 to 15 Nov 2026): in several sessions the second publish, to GitHub Pages, did not run because attaching the public repository was refused or denied; it ran after the owner's approval or in a later row.
§5 · Order (the course index): the §5 table's rows are the course index's build order, the marketing and AI courses' units numbered 1 to 22 with B1 left out, then the UX course's 1 to 15; the index dates each unit's writing (28 Oct to 3 Nov and 30 Oct to 10 Nov 2026), records A1 as written out of order beside B3, and gives no order within a day.
§5 · History courses (the method §1 and §5; the kit changelog, 25–27 Oct 2026): the history courses' pipeline from 25 Oct 2026 was a script check, then a fresh checker per report that had not seen it written, then a maintainer pass; when the second history course's reports were reviewed on 27 Oct 2026, its 58 then unaudited reports had been checked in three ways: a quality pass keeping them (13), a quality pass fixing them (26) and the fresh-checker pipeline (17), the capstone apart; the history review measured a mean score of 4.28 for units written without a checker and 4.8 for one unit written with one.
§5 · Second history course (the kit changelog): complete at 79 reports, all written with Opus 5.5 and all checked by a fresh agent.
§9 · Audits 3 onward (the kit changelog, 2–3 Nov 2026; the AI course's DD-B2 §4; the method, 15 Nov 2026): after Audit 2, Audits 3 to 6 of the marketing and AI courses were recorded as owed to a later stage reserved for the auditing model; an ask of 29–30 Oct 2026 records the owner low on that model's allowance and moves its check to a later row, which the review gives as the order of events, not a measured cause; on 15 Nov 2026 the owner closed that stage, retired the four-unit audit and left the fresh check and the staleness check as the guards.
§5 · The rewrite verdict (B8's fresh-check report and the course index, 2 Nov 2026): the AI course's B8 drew rewrite by the count rule (4 errors, two of one cause, each a one-sentence replacement); the maintainer read it as fix under the method's definition, all findings were applied, and the owner could overrule; the records show no rewrite and no re-check; its decision figure was dropped after its third check.
§6 · Figures added after writing (the kit changelog, 30 Oct 2026): the marketing and AI courses' twelve filed units, 38 kept and 4 dropped; the second history course, 177 kept and 18 dropped (8 after failing twice), later 180; the first history course, 266 proposed, 166 passed the first check, 95 got a fix, 94 of those passed the re-check, 6 dropped, 260 kept; each checked by a separate Opus 5.5 agent.
§6 · Figures on the site (the kit changelog): the verify script checked 509 figures on 152 pages on 30 Oct 2026 and 624 at phone width on 3 Nov 2026.
§6 · Checks to pass, per unit (the course index): each unit's row gives its figures' check counts, e.g. a sitemap figure passed on its eighth check and two matrices on their seventh.
§8 · Change 1, the auditing model only for checking: 17 of the 22 chats run on that model in whole or part were not audits or fresh checks; 18 of the 22 began on the first day; all 9 fresh checks run on the last day ran on the writing model with the auditing model's check owed.
§8 · Change 2, a routing row for the build and site work: 30 of 53 chats were of task types the routing table had no row for (infrastructure 15, figure passes 7, status 6, syllabus 2); the 15 infrastructure chats ran on the auditing model 8, the writing model 5, both 2; none of 53 ran on a smaller model.
§8 · Change 3, move a fan-out's workers down once its check has passed: 7 figure chats, median 33 turns, 6 on the writing model; in one pass alone 218 agents; every agent call in the two saved reads that show one (199 and 37) ran on the writing model; 6 of 266 figures dropped.
§8 · Change 4, no session deploys to the public site without the private-terms check: 13 of the 16 row asks read in full had the session publish and deploy to the public site, where the structure audit had found private terms in the build.
§8 · Change 5, one writer to the main branch at a time: 10 of 53 chats began while an earlier one was still open (14 overlapping pairs, an upper bound); one chat reverted its own merge because another session was mid-unit; one found another chat had done its work; of 39 asks held as text, one names a branch and none a worktree.
§8 · Change 6, model and effort in the first line and in the changelog: the model could be read in all 53 chats only by searching each for its commit trailers; effort in 0 of 53.
§8 · Change 7, the closing procedure in one skill: 13 of the 16 row asks read in full restated the publish procedure; 7 carried the same two-word publish instruction; 13 chats ended by writing the next prompt by hand.
§8 · Change 8, carry an audit's confirmed claims forward: one rewrite after an audit opened 43 distinct sources, 34 already opened by the audit that morning; another 45, 15 of them the audit's.
§8 · Change 9, no overnight plan without a branch: two figure-pass asks were written for an overnight run over filed units; of 39 asks held as text, one names a branch; both runs went ahead in the morning instead.
§8 · Change 10, account memory off in the Project: the model called the memory tool in 6 of 53 chats, in the parts read.
§8 · Ranking (DD-B2 §8): the ten are ranked by the size of the count each rests on and the share of the work it touches, the writer's judgement on those counts; one item was flagged and not ranked (9 of 53 chats open three hours or more, open time not being active time), and three habits were already fixed in the window and not ranked.
§1 · Start (the kit changelog): the first request of the work that became Academy was made on 22 Oct 2026; the first history course was built from 22 to 24 Oct 2026; the claude.ai Project's chat history starts on 28 Oct 2026, the repository being created that day.
§1 · Words (the kit changelog): the first history course about 244,000 words, the second about 264,000.
§8 · How the chats were listed (§1): through the three past-chat tools only (one lists chats by last update, one searches, one opens a chat at a spot); three listing calls (20, 20 and 13 chats) covered the window, two more found nothing outside it; 16 chats opened, spots in 7 more found by search; counts by two scripts over a table typed from the tool results.
§8 · Fields (§1): date and first message, task type (seven types, labelled by hand), turns, model (from commit trailers), effort (0 of 53: nothing records it), outcome (39 of 53; 14 not read). A turn is one message on either side; in a chat that runs agents, each agent's completion notice is a turn. "Accepted" was a proxy: a unit filed (7 chats) or the last reply reporting the row done with no later correction (32 chats).
§8 · Breakdowns (§2): task types as in §8, Model by task type, above; 872 turns in all, median 8, range 2 to 134; median turns by type: unit writing 12, infrastructure 8, figure passes 33, audits 2.5, status 10, syllabus 10, history writing 50.5; 11 chats took two turns; 10 took 30 or more.
§8 · Pattern counts (§3–§6): 6 one-line asks naming a code, 2 of them a code with two meanings; 5 chats opened with a status question; 16 asks name two or more rows (median 11.5 turns, against 8 for 31 naming one); 13 of 16 row asks read in full restate the publish procedure; 7 chats on the first day carried a whole unit pasted; 6 chats show a memory-tool call.
§8 · Rules tested (§7): the AI course's operating rules 1–10, its usage rules 11–24, its agent rules 25–28 and decision rule, and its routing table, mental model, skills and verification units, each given a verdict.
§8 · Date: the review read the history on 2 and 3 Nov 2026 across three agent runs; the unit is dated 2 Nov 2026 and was filed on 3 Nov 2026.
§8 · Typicality (DD-B2 §1 and §8): the review's writer states that the six days were a week of heavy building spent on the course machine, that every rate is a six-day rate not to be read as a habit over a season, and that the mix of tasks will not be a normal week's; work before the first day, including the history courses, is outside the tools' reach.
§8 · Working files (DD-B2 §1 and Sources; the kit changelog, 3 Nov 2026): the review's working table, chat list, tallies and scripts were kept in the writer's packet folder in the session and are not published; when two writers were lost to container restarts, the third resumed from the second's working files in the same packet; the chat history read is private.
§2 · Writing models of the history courses (the kit changelog): the first history course's 78 reports were written 55 with Fable 5.1 and 23 with Opus 5.5; the second's 79 all with Opus 5.5.
§9 · The records do not say which plan the project runs on, or any token or window measure for the writing of a single unit, or whether any failure was traced to retrieval mode (F4, F83, F109).
§9 · The records do not say what effort setting was used for any unit, check or audit: the usage review found it recorded in none of 53 chats (F18, F92, F109).
§9 · The records do not hold hours, usage or cost per unit or per row, or how often each routed task recurs (F18, F83, F109).
§9 · The records do not hold the text of a private course's unit brief, of the fresh-check prompt or of the retired sample-audit prompt; this course's own preamble and briefs and the staleness prompt are held (F19).
§9 · The records do not say whether the owner wanted the length of the longest UX unit in particular; the rule is that length is a guide (F21).
§9 · The records do not count the chats abandoned or the briefs rewritten after a miss; they record instances (F20, F29).
§9 · The records hold no spec document and no recorded non-goals for any course (F35).
§9 · The records do not total the fresh-check findings rejected or adjusted, give a false-alarm rate, or count findings by kind (F45, F102).
§9 · The records do not give the number of checkable claims in a whole unit, except the one full audit of Audit 1 (F46).
§9 · The records do not say which permission mode any agent ran in, or record a spend cap, an agent meeting injected instructions, or a rule adopted after the lost writers (F71).
§9 · The records do not say whether "Include sensitive topics in memory" or the training setting was on, or whether account memory was off after 28 Oct 2026; they hold no employer material or policy (F83).
§9 · The records do not give the model of each history fresh checker, or which of the first history course's reports had one (F104).
§9 · The records do not give the total of figures declared at one date or a typical number of checks to pass (F107).
§9 · The records do not give a total of words written across all courses (F110).
§9 · The records do not define an "ask" in the usage review (F116, F114).
§9 · The records do not say whether the usage review's working files were deleted (F118).
