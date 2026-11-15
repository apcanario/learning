# The public courses

Two courses written to be shared with anyone, adapted from the private courses Brand + AI A and B. Decided by Pedro on 11 Nov 2026 (backlog row G-0). This file holds the decisions and the rules of the rows that write them; `kit/next_prompt.py` prints each row's paste-ready prompt from it and from the course data.

## 1 · What was decided

| Decision | Pick | Pedro |
|---|---|---|
| Structure | Two new courses, each in its own data folder and vault; courses A and B stay untouched as his editions | Confirmed 11 Nov 2026: "new courses in new folders so that we can separate them afterwards" |
| Place on the site | Each sits in the track of its private original (Marketing, Technology) for now; his editions move to a private environment later | Confirmed 11 Nov 2026 |
| Audits | None: the Fable stage is closed, so no four-unit audit and no Fable 5.1 fresh check runs; the Opus 5.5 fresh check of every unit before filing stands | Confirmed 11 Nov 2026 ("the audits will run later"); closed 15 Nov 2026, S-NOAUDIT ("let's stop with the fable audits") |
| Personal-brand course's worked case | One fictional creator, Mara Venn, with a register of invented facts | Proposed 11 Nov 2026, not objected to; override: his own account as the public case |
| AI course's tool stance | Principles tool-neutral, worked on Claude, every product fact dated, an "On other tools" section per unit | Proposed 11 Nov 2026, not objected to; override: readers mostly on another assistant |
| AI course's worked case | Academy itself, from a case file with private details removed | Proposed 11 Nov 2026, not objected to; override: he does not want the audit record public (P24) |

## 2 · The two courses

| | PB · Building a Personal Brand on Instagram and YouTube | BW · Building with AI |
|---|---|---|
| `kit/courses.py` entry | `personal-brand` | `building-with-ai` |
| Data | `generator/data/personal-brand/` | `generator/data/building-with-ai/` |
| Vault | `courses/personal-brand/` | `courses/building-with-ai/` |
| Fresh checks | `audits/personal-brand/` | `audits/building-with-ai/` |
| Sourcing | `sourcing-standard.md` Parts 1 and 5 | Parts 1 and 6 |
| Units | 10 core in four parts, 2 deep dives | 10 core in three parts, 3 deep dives |
| Adapted from | Course A; each unit's Takes line names its source units | Course B; each unit's Takes line names its source units |
| Case | Mara Venn, fictional: `case-facts.md` | Academy, real: `case-academy.md` |
| Flags | `syllabus-flags.md` | `syllabus-flags.md` |

The reader of each is the persona in its preamble (`PRE` in its `units_data.py`). `reader.md` is unchanged. With the User Experience family these are the Project's exceptions to its single-reader rule.

## 3 · Rules every writing row follows

1. **One unit per chat, in syllabus order.** The writing order is the reading order. A unit starts only when every earlier unit of its course is filed.
2. **Opus 5.5 writes; a separate Opus 5.5 context checks.** No Fable audit or Fable fresh check follows (S-NOAUDIT, 15 Nov 2026). The chat only stages, applies, files, builds, publishes and records.
3. **The brief is never reworded.** It is built with `kit/mdcourse.py`'s `open_brief`: the preamble, the Aim, Takes and Gives lines, the unit brief.
4. **Source units are material, never authority.** The writer is given the private units its Takes line names, with their fresh-check reports. It re-verifies every claim it carries over at the claim's source. Nothing rests on a source unit alone.
5. **Mistakes are corrected where they sit.** The writer lists every mistake it finds in a source unit; the fresh checker verifies that list. A verified mistake is fixed in the private unit as an exact replacement, with a dated note in that unit and a line in its hub's changelog. A mistake found in a filed public unit is fixed the same way. Each is named in the reply.
6. **Contradictions and needs are flagged, never silently absorbed.** The writer lists (a) where its evidence contradicts a filed unit of its course or the brief of an unwritten one, and (b) what the unit needed that the syllabus does not give, or what a later unit must now cover or avoid. The chat appends each to the course's `syllabus-flags.md` with the units affected and a proposed change. No brief is changed by the chat that raises a flag. A flag that names a later unit is passed to that unit's writer by `kit/next_prompt.py`. If a flag means the next unit cannot be written as briefed, the reply says so in its first line, and the next prompt is a syllabus review instead of a unit.
7. **A syllabus review** is its own row, added when Pedro asks for one or a flag blocks a unit: it reads every open flag, proposes each brief change as an exact replacement, and applies only what Pedro confirms; `units_data.py` changes only there. It runs on the best model the session has.
8. **No private term reaches a public course.** `python3 kit/private_terms.py` must print OK before filing; `verify.py` runs it on the vault, the data folder and the built pages (but each course's generated "How it was built" page, which quotes `method.md` and links the private repository on every course: P24). The terms are `kit/private-terms.txt`. A writer never refers to the private course or its units.
9. **The case stays consistent.** PB: every fact a unit invents about Mara is appended to `case-facts.md` at filing. BW: a unit takes facts about Academy only from `case-academy.md`; a fact it needs and the file lacks is a need, added to the file from the Project's records by the filing chat, never by a writer.
10. **Reliefs wait.** The two courses are not yet in the outline library (it needs ten outlines that a course's own texts name). Until row G-R registers them, a public unit's page shows no relief; the writer's `Object:` line is kept in the changelog row for G-R.
11. **Everything is pushed.** Each chat commits and pushes `apcanario/learning`, publishes Academy to its artifact once, runs `deploy.sh` for GitHub Pages, rewrites the Project copies, and ends with the next row's prompt in a code block.
12. **Proposals are dealt with in the chat that raises them** (Pedro, 12 Nov 2026, 21:22 and 21:31). Nothing a chat uncovers is left as a proposal for a later chat: every correction to a filed unit or a record, and every kit fix it needs, is made in that chat before it closes. A writer's contradiction whose remedy is a change to a filed unit's text, not a brief, is such a correction. Three limits keep a correction from adding errors or pulling the chat off its unit: only the text it names changes; a fresh Opus 5.5 agent checks each change against its source and against the syllabus (the briefs of the units it touches and of every unwritten unit that relies on it, the filed units, the register) before it is applied, its report saved first; a change that fails, needs a brief changed or would contradict another filed unit is not applied and becomes a flag for the next syllabus review (rule 7). What the check turns up is worked the same way, once more, in the same chat. Only two kinds stay *proposed*: a brief change, which Pedro confirms in a syllabus review, and a task only Pedro can do. A correction still open after that, or left by a row that stopped, goes into the Corrections section of `docs/BACKLOG.md`, and the next prompt works it first. `kit/next_prompt.py` prints these steps (1b and 7b) into every prompt.

## 4 · By hand

- The claude.ai Project instructions still name one reader and two course families. They need a line for the public courses and their exception to the single-reader rule (row P38 already asks for the same edit for User Experience). Pedro edits the Project instructions; a chat cannot.
- P24 (the audit files open only for Pedro) and P29 (private terms in the pages of the private courses on the public site) are his decisions and are untouched by these rows.
