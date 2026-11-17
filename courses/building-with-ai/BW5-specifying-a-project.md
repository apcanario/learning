---
code: BW5
title: Specifying a project
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-15
search: on
---

# BW5 · Specifying a project

This unit was written with search on; every source it cites was read on 15 November 2026, and every product fact carries that reading date. Each practice carries an evidence grade, as in BW1 to BW4: **measured** (a study or test with numbers), **documented practice** (a vendor or a named practitioner says to do it and shows how; nobody measured it) or **stated opinion**. Most of what follows is documented practice. One study measured a spec-first method, on software tests; carrying it to your project is this unit's inference, and is said to be. The brief form is BW3's (Deliverable, "The brief form"); the folders, instruction file and index are BW4's (Deliverable, Part 3). This unit specifies a project into them and uses both by name.

## 1 · Why the specification comes before the building

A specification is the text that says what the finished project is, written before any part of it is built, and kept as the thing every part is checked against. The practice now called spec-driven development has named authors and primary sources, and they agree on the shape.

**Harper Reed (16 February 2025).** A three-step workflow: a chat model asks you "one question at a time" until it can write a developer-ready specification, saved as `spec.md`; a reasoning model turns the spec into a plan of "small, iterative chunks that build on each other", saved as `prompt_plan.md`, with a checklist, `todo.md`, that the code tool ticks off; then the plan is executed prompt by prompt. His own view of where the result is decided: "The success really depends on how well step 2 went", step 2 being the plan. He dates the advice himself: "This is working well NOW, it will probably not work in 2 weeks, or it will work twice as well" ([Reed, *My LLM codegen workflow atm*, 16 Feb 2025](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)). Grade: documented practice; one practitioner's account, an anecdote.

**GitHub Spec Kit (2 September 2025).** Den Delimarsky's announcement states the premise: "With AI the specification becomes the source of truth and determines what gets built." The toolkit runs `/specify` (the agent writes the full spec from a high-level prompt), `/plan` (a technical plan), then `/tasks`, which "generates small, reviewable chunks that each solve a specific piece of the puzzle". The post gives the mechanism in one line: models are "exceptional at pattern completion, but not at mind reading", so a vague request forces the model to guess unstated requirements. GitHub calls the toolkit "our experiment" ([Delimarsky, *Spec-driven development with AI: Get started with a new open source toolkit*, GitHub Blog, 2 Sep 2025](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit)). Grade: documented practice, vendor tool.

**AWS Kiro (14 July 2025).** Nikhil Swaminathan and Deepak Singh: Kiro expands one prompt into user stories, each with acceptance criteria in EARS notation; then a design document; then it "generates tasks and sub-tasks, sequences them correctly based on dependencies, and links each to requirements" ([Swaminathan and Singh, *Introducing Kiro*, 14 Jul 2025](https://kiro.dev/blog/introducing-kiro/)). Grade: documented practice, vendor tool.

**Anthropic's Claude Code documentation (read 15 Nov 2026).** For larger features: have Claude interview you, write "a complete spec to SPEC.md", then "start a fresh session to execute it", because the new session "has clean context focused entirely on implementation". The page says what the best specs hold: they "name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step", and "Time spent making the spec precise pays off more than time spent watching the implementation" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md), read 15 Nov 2026). Grade: documented practice, vendor.

**Why the order matters: the mechanism.** Two sourced effects make a spec written first worth more than the same requirements given as the work goes.

1. *A brief given in pieces does worse than the same brief given whole.* BW3 §5 sets out Laban and colleagues' measurement ([Laban et al., *LLMs Get Lost In Multi-Turn Conversation*, arXiv 2505.06120, 9 May 2025](https://arxiv.org/pdf/2505.06120); preprint): across six generation tasks and fifteen models, giving the instruction across turns instead of at once cost an average of 39%, and the models' early guesses were built on and never retracted. A spec is the whole instruction, written before the first turn. Measured, on models none of which is current (BW3 §5); the transfer to a project of many chats is this unit's inference.
2. *A fresh context needs something to start from.* BW4 §4: across chats nothing persists except what a layer re-inserts, so a project that works one context per part needs the requirements in a file. The spec is that file.

**The one measurement of a spec-first method.** Michele Tufano and nine Google colleagues gave the same agent harness and model (Gemini 3 Flash) the job of writing tests for the fixed versions of 90 historical bugs from Google's internal issue tracker, with and without a first step in which the agent writes the code's pre- and post-conditions in natural language. Counting a bug as caught when any of five runs caught it, the spec-first agent's tests caught 63.2% of the bugs against 53.4% for the baseline, a gain of 9.8 points (p = 0.035); on a single run it was 41.1% against 36.9%, a gain of 4.2 points and not significant; branch coverage was 48.9% against 46.4% (p = 0.0034) and line coverage 74.4% against 74.8%, not significant; and the spec-first runs used 1.38 times the tokens ([Tufano et al., *Grounding AI Agents in Contracts: An Empirical Evaluation of Spec-Driven Test Generation*, arXiv 2608.17177 v2, 21 Aug 2026](https://arxiv.org/pdf/2608.17177); preprint, which states acceptance at the SpecOps '26 workshop). Measured; one model, one task (software tests), one company's code. That a written statement of intent before the work raises the share of correct output in a report or a course is this unit's inference from it, and nothing has measured it.

```viz
{
  "kind": "bars",
  "mode": "grouped",
  "unit": "%",
  "max": 100,
  "decimals": 1,
  "series": [{"name": "Spec first", "tone": 2}, {"name": "Baseline", "tone": 4}],
  "rows": [
    {"label": "Bugs caught in any of 5 runs", "values": [63.2, 53.4]},
    {"label": "Bugs caught, 1 run (n.s.)", "values": [41.1, 36.9]},
    {"label": "Branch coverage", "values": [48.9, 46.4]},
    {"label": "Line coverage (n.s.)", "values": [74.4, 74.8]}
  ],
  "caption": "One measured spec-first method: an agent on Gemini 3 Flash writing tests for 90 historical Google bugs, with and without first writing pre- and post-conditions. n.s.: not significant. From §1 of this unit; Tufano et al., arXiv 2608.17177 v2, 21 Aug 2026 (preprint)."
}
```

**The case against, from the same literature.** Birgitta Böckeler of Thoughtworks tried Kiro, Spec Kit and Tessl and reported three costs: on a small bug, Kiro's workflow "was like using a sledgehammer to crack a nut"; the spec files were long enough that "I'd rather review code than all these markdown files"; and the agent still did not keep to the spec, in both directions: "I frequently saw the agent ultimately not follow all the instructions", and "I also saw the agent go way overboard because it was too eagerly following instructions" ([Böckeler, *Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl*, martinfowler.com, 15 Oct 2025](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). Grade: documented practice; one practitioner's trial, an anecdote. Claude Code's page sets the lower bound: planning adds overhead, and "If you could describe the diff in one sentence, skip the plan" (read 15 Nov 2026). Malte Ubl, on Google's design docs, makes the same cut from outside AI: a design doc is overhead, worth writing where the problem is ambiguous, and of little value where it is not ([Ubl, *Design Docs at Google*, 6 Jul 2020](https://www.industrialempathy.com/posts/design-docs-at-google/); documented practice).

What follows from all of this (stated opinion, built on the sources above): write a spec when the project has more parts than one context can finish, or when you could not state the result in one sentence. Keep it short enough to read whole, because a spec nobody reads is a spec the model does not get either. And expect the model to drift from it anyway, which is why every part is checked against it (§5, BW6).

## 2 · What a spec holds for a knowledge-work project

Spec-driven development was written for software. Its tools ask for interfaces, data schemas and test suites. A report, a course, a body of research or a content operation has none of those, and needs five things in their place. Each is in one or more of the sources; the set of five, for knowledge work, is this unit's synthesis (stated opinion).

| Part | What it says | Where it comes from |
|---|---|---|
| **The reader** | Who reads the output, what they already know, what they will do with it | BW3 §1: the reader is the first part of any brief that survives |
| **The goal, in one sentence** | What exists when the project is finished | BW3 template 7: "Goal: one sentence"; the syllabus of Academy (Academy case), this course's running example, starts from one (Academy case file §2) |
| **Measurable outcomes** | Three to five things that will be true at the end, each one you can check | Kiro's acceptance criteria for each user story (§1); OpenAI's ExecPlans: "Acceptance should be phrased as behavior a human can verify" ([Friel, *Using PLANS.md for multi-hour problem solving*, OpenAI Cookbook, 7 Oct 2025](https://developers.openai.com/cookbook/articles/codex_exec_plans); vendor) |
| **Non-goals** | What a reasonable person might expect the project to do, and it will not | Ubl: non-goals are things "that could reasonably be goals, but are explicitly chosen not to be goals", which leaves out negated goals such as "The system shouldn't crash" (Ubl, 2020); Claude Code: the best specs "state what is out of scope" (§1) |
| **A definition of done** | The checks a part must pass before it counts as finished | The Scrum Guide: "The Definition of Done is a formal description of the state of the Increment" when it meets the product's quality measures, and work that does not meet it "cannot be released or even presented" ([Schwaber and Sutherland, *The 2020 Scrum Guide*, Nov 2020](https://www.scrumguides.org/scrum-guide.html); documented practice) |

**Non-goals do the most work per word.** A model given a gap fills it with the most probable reading (BW1 §7). For a project, the most probable reading of "a course on X" includes quizzes, a glossary and a summary at the end of every unit. Each of those is a part nobody asked for and somebody must then check. One line naming it as a non-goal removes it from every unit at once. Böckeler's agent that went "way overboard" (§1) and Anthropic's own note that Claude Opus 4.5 and Opus 4.6 have a tendency "to overengineer by creating extra files, adding unnecessary abstractions, or building in flexibility that wasn't requested" ([Anthropic, *Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), read 15 Nov 2026; vendor) are the failure a non-goal list prevents.

**A definition of done is a list of checks you can run.** Claude Code's page puts the reason plainly: "Claude stops when the work looks done", and without a check it can run, "looks done" is the only signal available (read 15 Nov 2026). In software the check is a test. In knowledge work it is a line you can run by reading: every claim with a number has a source in the same sentence; the deliverable is built in full; the word count is inside the range. BW3 §3 calls these DONE WHEN lines and puts them in every brief. The spec holds the ones that apply to every part; each brief adds the ones for its own part.

**One page.** The sources disagree on length: Ubl puts a large design doc at 10 to 20 pages and allows a "mini design doc" of 1 to 3 for incremental work; Michael Nygard's decision records are "one or two pages" ([Nygard, *Documenting Architecture Decisions*, 15 Nov 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). This unit's limit is one page, about 400 words (stated opinion), for two reasons from earlier units: the spec is joined to every part's brief, so its length is paid in every context (BW4 §2); and it must be read whole at every review (§9), which at BW4's reading rate takes under two minutes. Anything longer is a sign that a procedure or a part's detail has crept in; procedures belong in a rules file (BW4, Part 3) and part detail belongs in that part's brief (§5).

## 3 · Cutting the project into units one context can finish

A unit is the smallest part of the project that produces one named artefact, can be built in one context from its brief and the units before it, and can be checked on its own. The three conditions come from different sources.

**One context.** METR timed how long tasks take the humans who do them, then measured which of those tasks frontier models finish. Its measure is the "50% time horizon", "the time humans typically take to complete tasks that AI models can complete with 50% success rate". Success falls steadily as tasks get longer, and the horizon "has doubled approximately every seven months since 2019" ([Kwa et al., *Measuring AI Ability to Complete Long Software Tasks*, arXiv 2503.14499 v3, 25 Feb 2026](https://arxiv.org/html/2503.14499v3); preprint; measured on software and research tasks). The transfer is this unit's inference: a smaller unit is likelier to be finished well, and the right size moves as models improve, so the cut is re-checked at each review. BW1 §2 covers the second limit, the window itself: accuracy falls as the context fills, measured on older models.

**One artefact, one at a time.** Anthropic's engineers gave an agent a large build across many sessions and reported two failures: it "tended to try to do too much at once", and later sessions would see the progress made and "declare the job done". Their fix was a feature list written in the first session and a rule that each later session works "on only one feature at a time" ([Young, *Effective harnesses for long-running agents*, Anthropic Engineering, 26 Nov 2025](https://anthropic.com/engineering/effective-harnesses-for-long-running-agents); vendor; documented practice, no figures published). Anthropic's prompting guide gives the same split for any work longer than one window: use the first context window "to set up a framework", then "use future context windows to iterate on a todo-list" (*Prompting best practices*, read 15 Nov 2026). Reed's chunks "build on each other"; Spec Kit's are "small, reviewable" (§1).

**Checkable on its own.** A unit that only "explores" or "considers" leaves nothing to check; BW3's template 7 already forbids it ("Every part produces a named artefact"). A unit whose done-check needs a later unit to exist cannot be filed when it is finished.

Four tests, then, for each unit on your list (stated opinion, built on the sources above):

1. It names one artefact, built in full inside the unit.
2. Its brief, the spec and what it takes from earlier units fit in one context with room for the work. It takes each earlier unit's named deliverable; if it needs more than three earlier units read in full, the cut is wrong.
3. Its done-when lines can be run on it alone.
4. You could say in one sentence what it adds that no earlier unit has.

**The case.** Academy, a library of self-study courses built by one person with Claude in October and November 2026 (Academy case file §1), sizes a unit as a long-form report of 2,000 to 6,000 words by guide, with a closing deliverable built in full, and starts each course with eight to twelve core units and two or three deep dives (Academy case file §1, §2). The guide is a guide: the longest unit of one course ran to about 16,900 words (§1). One project, an anecdote; it shows the sizing run across 194 units, and says nothing about whether another size would have done better, since the record has no control (§9).

## 4 · The build order and its dependencies

Once the units exist as a list, put them in the order they can be built. A unit can be built only after every unit it takes from is finished and checked. That is the whole rule. Kiro states it as a feature, tasks sequenced "based on dependencies" (§1); Reed states it as chunks that "build on each other".

Write each dependency down in two directions. **Takes** names the earlier units this one reads. **Gives** names what later units will take from it, so it is built for them. This course uses the pair on every unit; its course map gives each unit's Aim and Gives line. Read as a grid, the map shows two things a list hides: which units carry the most later work, and whether anything takes from a unit that comes after it.

```viz
{
  "kind": "matrix",
  "cols": ["BW1", "BW2", "BW3", "BW4", "BW5", "BW6", "BW7", "BW8", "BW9"],
  "rows": [
    {"label": "BW3", "cells": ["takes", null, null, null, null, null, null, null, null]},
    {"label": "BW4", "cells": ["takes", null, null, null, null, null, null, null, null]},
    {"label": "BW5", "cells": [null, null, "takes", "takes", null, null, null, null, null]},
    {"label": "BW6", "cells": ["takes", null, "takes", null, "takes", null, null, null, null]},
    {"label": "BW7", "cells": [null, "takes", "takes", null, "takes", null, null, null, null]},
    {"label": "BW8", "cells": [null, null, null, "takes", "takes", "takes", "takes", null, null]},
    {"label": "BW9", "cells": [null, null, null, null, "takes", "takes", "takes", "takes", null]},
    {"label": "BW10", "cells": [null, "takes", null, null, "takes", null, null, null, "takes"]}
  ],
  "legend": [{"mark": "takes", "means": "the row's unit is built against the column's Gives line", "tone": 4}],
  "caption": "The core units of this course as a dependency grid: each row takes from the columns marked. Data from the build order in Deliverable 1b of this unit, read from the Gives lines of this course's map; BW5's Gives line names every later unit. Every mark sits left of the row's own unit: nothing takes from a later unit."
}
```

Three rules follow (stated opinion):

- **No mark to the right.** If a unit needs something only a later unit produces, either move it or move the thing it needs into an earlier unit.
- **Heavy columns first, and checked hardest.** A unit many others take from carries its errors into all of them. In this course BW5's column is the heaviest by design, which is why its deliverable is the form everything later is built against.
- **Deep dives last.** They take from the core; nothing in the core takes from them. Academy's syllabus shape puts two or three deep dives after the core units (Academy case file §2).

## 5 · One brief per unit, never reworded once work has started

Each unit gets one brief, written from the spec before the unit is built. BW3 gave the form (TASK, READER, OUTPUT, CONSTRAINTS, EXAMPLES, DONE WHEN, MATERIAL, TASK again) and, in template 7, the two stages of plan-then-build that this section applies to a whole project. Two things are added here: what goes into a unit's brief beyond BW3's form, and the rule that keeps it fixed.

**Shared preamble plus unit brief.** Academy joins a shared preamble (the reader, the goal, the sourcing standard and the tone) to each unit's own brief, so every context is self-contained (Academy case file §2). The preamble is the spec's reader, goal and definition of done, written once; the unit brief is the unit's Aim (what the reader can do after it), Takes, Gives, what it covers in order and its deliverable. Every context gets both and nothing else from the project, which is OpenAI's test for a plan, applied to a brief: "Every ExecPlan must be fully self-contained", meaning it "contains all knowledge and instructions needed for a novice to succeed" (Friel, 2025; vendor).

**Why the brief is never reworded.** Three reasons, each sourced.

1. *The check needs a fixed target.* The fresh check compares the unit's claims with their sources and its deliverable with its brief (Academy case file §2). A brief edited during the work leaves the checker comparing the output with a text the writer never saw.
2. *Models edit what they are allowed to edit.* Anthropic's harness kept its feature list in JSON because models were less likely to change or overwrite it than Markdown, and told every session that "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality" (Young, 2025; vendor). The brief is your test; the rule protects it from the writer too.
3. *Spec Kit names the spec the source of truth* (§1). A source of truth that changes silently is not one.

**This rule and BW3's restart rule.** BW3's conventions say: if the first output misses, change the brief and open a new chat. That holds for a one-off task. In a specified project, the change goes through §9: the miss is recorded as a flag, the brief is changed at a boundary as a new version with a decision-log entry (§6), and the unit restarts in a new context from the new version. The brief still changes; it never changes inside a unit's work, and never without a record.

## 6 · The decision log

A spec says what the project is. A decision log says why it is that way and not another, so that a later chat, or you in three months, neither keeps a choice it no longer understands nor undoes one whose reason still holds. Michael Nygard put the problem in those terms in 2011: without the reasoning, a newcomer can only accept a decision blindly or reverse it blindly, and "It's better to avoid either blind acceptance or blind reversal." His format: a short title, the **Context** ("the forces at play"), the **Decision** ("our response to these forces"), a **Status** (proposed, accepted, deprecated, superseded) and the **Consequences** ("the resulting context, after applying the decision"). A reversed decision is not edited or deleted; the old record stays, marked superseded (Nygard, 2011). Grade: documented practice, software architecture. OpenAI's ExecPlans require the same thing of an agent: "Record all decisions in the `Decision Log` section", each with the decision, the rationale and the date and author (Friel, 2025; vendor).

**The case.** The Academy case file records decisions of exactly this kind, though not in this format.

- *After Audit 1.* One sampled claim in eight failed, the full audit found 23 of 91 claims failing, and the three units were rewritten; from then on every unit of that family got a fresh check before filing (Academy case file §3). Context, decision and consequence are all in the record.
- *Figures.* The early rule dropped a figure that failed its check three times, and two were dropped. The owner later replaced it: figures are never dropped; they are fixed until they pass. One sitemap figure passed on its eighth check (§6). That is a superseded decision, and the record keeps both.
- *Models.* A session's model named "fable" (Fable 5.1 is the project's auditing model, Academy case file §2) resolved to a newer version than the method names, so the checks it ran were recorded as owed again on the named version (§7).

One project, an anecdote: the case shows that the decisions worth logging are the ones a later chat would otherwise undo, and nothing about how much the log saved. The case file dates two of them: the per-unit fresh check made a rule for the marketing and AI courses after Audit 1 on 28 Oct 2026, and figures fixed until they pass, never dropped, on 3 Nov 2026 (Academy case file §2); it gives no date for the early figure rule or for the model-version decision.

**When a decision is due for re-checking.** Decisions that rest on current facts (a model, a price, a feature) go stale. This course uses one interval: six months from the day the facts were read, the same interval as Academy's staleness check for units written with live search (Academy case file §2; BW2 §7). For this unit that date is 15 May 2027.

## 7 · The backlog and the changelog, as a pair

A backlog is the queue of work not yet done; a changelog is the record of work done. Each is an old practice with a named source. The Scrum Guide's product backlog is "an emergent, ordered list of what is needed to improve the product", refined by "breaking down and further defining Product Backlog items" into smaller, more precise ones (Schwaber and Sutherland, 2020). Olivier Lacan's *Keep a Changelog* defines a changelog as "a file which contains a curated, chronologically ordered list of notable changes", kept so that people can "see precisely what notable changes have been made", with an *Unreleased* section at the top whose entries move into a dated section when they ship ([Lacan, *Keep a Changelog*, v1.1.0](https://keepachangelog.com/en/1.1.0/)). Both documented practice; neither was written for AI work.

What working with models adds is that the pair becomes the hand-off between contexts. Anthropic's harness gave each session a progress file and git history to read at the start and to write at the end (Young, 2025), and its prompting guide tells a fresh context to start by reading the progress file, the test list and the git log (*Prompting best practices*, read 15 Nov 2026; vendor). BW4 §4 gives the test: could a fresh chat do the next step from the files alone?

Used as a pair, three rules hold (stated opinion, built on the sources above):

- **Every chat works one backlog row.** The row names the unit, its brief and its done-when lines.
- **A finished row moves; it is never copied.** It leaves the backlog and enters the changelog with the date, the model that did the work and a one-line result. A row in both files is a row nobody knows the state of.
- **The chat ends by writing the next prompt.** The next chat starts from that prompt, the brief and the files.

**The case.** Academy runs this pair: every chat works one row of the backlog, a finished row moves to the changelog, and each chat ends by writing the prompt for the next; the model that wrote each unit is recorded (Academy case file §2). When writer agents were lost to container restarts, the third writer of one deep dive resumed from the second's working files (§7). Anecdote; it shows the files carrying a unit across lost sessions.

## 8 · Proposing a task against doing it

Work on one unit uncovers work on others: an error in a filed unit, a gap in the spec, a better order. A model that finds it will usually want to fix it there and then. Anthropic documents the tendency in its own models and gives the counter-instruction: "Only make changes that are directly requested or clearly necessary", and "Don't add features, refactor code, or make 'improvements' beyond what was asked" (*Prompting best practices*, read 15 Nov 2026; vendor). Its Claude Code page makes the same point about review findings: a reviewer asked to find gaps "will usually report some, even when the work is sound", and "Chasing every finding leads to over-engineering" (*Best practices for Claude Code*, read 15 Nov 2026).

The rule this unit uses (stated opinion, built on those sources): **a chat does its own row and proposes everything else.** A proposal is a new backlog row, written by the chat that found the work, with what it would do and which other parts it would touch. It is not worked in the chat that wrote it. Three reasons: the current unit's context stays on its brief (§3); the proposal gets a decision before it costs anything; and a change to a filed unit, made inside another unit's chat, would never be checked against its own brief.

**The case.** Academy's rule is the same: a task the work uncovers is added as a proposed row and is not worked until the owner confirms it (Academy case file §2). The case file holds no count of proposals made, confirmed or refused.

## 9 · How a spec is allowed to change

A spec that can never change is wrong by the third unit; a spec that changes whenever a chat wants it to is not a spec. The sources agree on a middle path: the spec changes, at fixed points, on the record.

- **The Scrum Guide** fixes the goal inside a sprint and allows clarification: "No changes are made that would endanger the Sprint Goal", while "Scope may be clarified and renegotiated with the Product Owner as more is learned"; each sprint ends with a review whose purpose is "to inspect the outcome of the Sprint and determine future adaptations" (Schwaber and Sutherland, 2020; documented practice).
- **Ubl** tells design-doc authors to update the doc when the design changes, "If the designed system hasn't shipped yet, then definitely update the doc", and notes that in practice changes often go into separate documents, like amendments to a constitution, which should then be linked from the original (Ubl, 2020).
- **Spec Kit:** "when something doesn't make sense, you go back to the spec; when a project grows complex, you refine it" (Delimarsky, 2025; vendor).
- **ExecPlans** are "a living document" that contributors "are required to revise" as discoveries occur (Friel, 2025; vendor).
- **Nygard:** a reversed decision stays in the log, marked superseded (§6).

**The flag-and-review rule** (this unit's synthesis; stated opinion, built on the five sources above). It is the rule BW7's pipelines and BW9's agents rely on.

1. **During the work, nothing in the spec or a brief changes.** A chat that finds the spec or its brief wrong does what the brief allows, and raises a **flag**: what is wrong, where it was found, and the change it proposes.
2. **A flag waits for a boundary.** A boundary is a fixed point you choose in advance: the end of a unit, or the end of a group of units.
3. **At the boundary, every open flag is decided.** Accept it, change it, or refuse it. An accepted flag changes the spec or the brief as a new version, with a decision-log entry (§6). A refused flag is recorded as refused, with the reason.
4. **Units already filed are checked against the change.** If the change makes a filed unit wrong, that becomes a proposed row (§8).
5. **No unit starts while a flag that touches it is open.**

```viz
{
  "kind": "states",
  "per_row": 3,
  "start": "raised",
  "states": [
    {"id": "raised", "label": "Raised", "note": "by the chat that found it; work goes on under the brief", "tone": 4},
    {"id": "open", "label": "Open", "note": "waiting for the next boundary", "tone": 4},
    {"id": "decided", "label": "Decided at the boundary", "tone": 2},
    {"id": "accepted", "label": "Accepted", "note": "new version + decision-log entry", "tone": 2, "end": true},
    {"id": "refused", "label": "Refused", "note": "recorded, with the reason", "tone": 1, "end": true}
  ],
  "transitions": [
    {"from": "raised", "to": "open", "label": "waits for a boundary"},
    {"from": "open", "to": "decided", "label": "boundary reached"},
    {"from": "decided", "to": "accepted", "label": "accept or change"},
    {"from": "decided", "to": "refused", "label": "refuse"}
  ],
  "caption": "The life of a flag under the flag-and-review rule of §9 of this unit: raised during the work, held open, decided at a boundary, then accepted as a new version with a decision-log entry, or refused with a reason. The rule is this unit's synthesis of the Scrum Guide (2020), Ubl (2020), Spec Kit (2025), OpenAI's ExecPlans (2025) and Nygard (2011)."
}
```

**Choosing the boundary.** Too rarely, and the work runs on a spec everyone knows is wrong; too often, and the review costs more than the units. The method of Academy sets a sample audit every four units (Academy case file §2), a natural boundary; audits 3 onward had not run at 11 Nov 2026, and on 15 Nov 2026 the owner retired the four-unit audit (§9). Beside the method's backlog and proposal rules, the case file records a flag mechanism for this course: a chat that writes a unit raises a flag for each contradiction between units or briefs and each need the syllabus does not meet, and a flag that would change a brief waits for a syllabus review that the owner confirms, with no fixed date set; at 16 Nov 2026 none of 34 flags had been resolved by such a review (§2). It records syllabus reviews on 3 Nov 2026 (the UX course) and 17 Nov 2026 (this course) (§2), and not how often the spec of a course changed.

## 10 · The Academy case's method, as the worked example

Every element of §2 to §9 appears in one project's method. This section reads it as a whole, as the case file records it, and then says what it shows and what it cannot.

```viz
{
  "kind": "flow",
  "steps": [
    {"label": "Syllabus", "note": "goal, 3 outcomes, 8–12 units + 2–3 deep dives", "tone": 1},
    {"label": "Briefs", "note": "shared preamble + one per unit, never reworded", "tone": 1},
    {"label": "Write", "note": "one context per unit", "tone": 2},
    {"label": "Writer's pass", "note": "sourcing checklist; up to 10 unsure claims", "tone": 2},
    {"label": "Fresh check", "note": "a context that did not see the writing", "tone": 3},
    {"label": "File", "note": "row moves to the changelog", "tone": 3},
    {"label": "Sample audit", "note": "every four units", "tone": 4},
    {"label": "Staleness check", "note": "six months after live search", "tone": 4}
  ],
  "caption": "Academy's method in the order a unit meets it. From §10 of this unit; Academy case file §2 (one project, an anecdote)."
}
```

- **Syllabus first.** A course starts as a goal in one sentence, three measurable outcomes, eight to twelve core units and two or three deep dives, each unit with a one-line scope, a named deliverable and a brief (Academy case file §2). That is §2's spec and §3's cut, at course level.
- **One brief per unit, never reworded,** joined to a shared preamble (§2 of the case file). That is §5.
- **One context per unit.** Each unit is written in a new chat or a fresh agent context that sees only its brief and the units already filed; the stated reason is that leaked context is how a course starts repeating itself (§2).
- **The writer's own pass** against the sourcing checklist, with up to ten claims it could not verify listed (§2).
- **A fresh check.** A separate context that has not seen the unit written checks every cited claim against its source and the deliverable against the brief, writes findings graded error, should-fix and minor, and never edits; a maintainer verifies each finding and applies it as an exact replacement (§2). Anthropic gives the same reason for separate review: "A fresh context improves code review since Claude won't be biased toward code it just wrote" (*Best practices for Claude Code*, read 15 Nov 2026; vendor).
- **A sample audit every four units**: one claim drawn from every section of each unit and checked; a unit with more than one sampled claim in ten failing is audited in full (§2). On 15 Nov 2026 the owner retired the four-unit audit, leaving the fresh check and the staleness check as the guards (§9). How to set your own threshold is BW6's subject.
- **A staleness check** six months after any unit written with live search (§2).
- **A backlog and a changelog**, with proposals held until confirmed (§2; this unit's §7 and §8).

**What the record shows.** The fresh check found work to do on almost every draft: of the 36 units that got one before filing, 28 had at least one error and 8 had none; the checkers' findings totalled 58 errors, 237 should-fix and 303 minor (Academy case file §5). The first audit, run before units of that family got a fresh check, found the failures a spec and a check are meant to catch: three units whose deliverables did not exist, and two table rows resting on figures the cited vendor pages did not contain (§3). The second audit's four units, B2, B3, B4 and A1, all passed (§4), and all four are among the 36 that had a fresh check before filing (§5); with no unit written without the method to compare (§9), nothing here says the check caused the pass.

**What it cannot show.** One project by one person; no unit was written without the method to compare; no measure of hours or money per unit (Academy case file §9). It shows one person running the method across five courses and 194 units, with a fresh check before filing on 36 of them (Academy case file §1, §5). It does not show the method beats a lighter one. That claim would need the comparison the case lacks, and the only measured comparison in this unit is Tufano and colleagues' (§1), on software tests.

## 11 · On other tools

The principles of §2 to §9 (a one-page spec, non-goals, a definition of done, units one context can finish, a build order, fixed briefs, a decision log, a backlog and changelog pair, proposals held, flags reviewed at a boundary) need no particular product. Their sources are tool-neutral (Nygard, Ubl, the Scrum Guide, Keep a Changelog) or from several vendors. What is specific to Claude, as read on 15 November 2026:

| Claim in this unit | Claude (read 15 Nov 2026) | ChatGPT and OpenAI | Gemini and Google |
|---|---|---|---|
| A spec written by interview, then built in a fresh session (§1) | Claude Code: interview with the `AskUserQuestion` tool, write `SPEC.md`, then a fresh session ([*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md)) | Codex: a self-contained `PLANS.md` "ExecPlan" written before a long task ([Friel, OpenAI Cookbook, 7 Oct 2025](https://developers.openai.com/cookbook/articles/codex_exec_plans)) | Gemini CLI: the Conductor extension, which helps you "formalize your intent" in Markdown spec and plan files before code ([Ballinger, Kornder and Aitbayev, *Conductor: Introducing context-driven development for Gemini CLI*, 17 Dec 2025](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/)) |
| Plan approved before building (§1, §5) | Claude Code's plan mode, which reads files and makes no changes until you approve (*Best practices*) | Not checked: the ChatGPT Projects help page could not be read on 15 Nov 2026 | Conductor: "Once you approve the plan, run `/conductor:implement`" (Google, 2025) |
| A decision log kept with the plan (§6) | No Claude page found that names one | ExecPlans require a `Decision Log` (Friel, 2025) | No Google page found that names one |
| Over-eager changes and the counter-instruction (§8) | Anthropic's *Prompting best practices*, "Overeagerness" | A narrower equivalent: OpenAI's GPT-5 guide, "Prompting for less eagerness", on reducing "the scope of GPT-5's agentic behavior" by lowering reasoning effort and setting tool-call budgets ([Kotha, Lee, Zakariasson and Kavanaugh, *GPT-5 prompting guide*, OpenAI Cookbook, 7 Aug 2025](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide); marked archived) | None found |
| A fresh context for review (§10) | Claude Code's writer and reviewer sessions; subagents in their own context (*Best practices*) | Not checked: OpenAI's Codex code-review page could not be read on 15 Nov 2026 | Gemini CLI subagents, each operating "within its own separate context window" ([Wotherspoon and Patel, *Subagents have arrived in Gemini CLI*, Google Developers Blog, 15 Apr 2026](https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/); vendor, read 15 Nov 2026) |

One fact for anyone keeping project rules inside a chat product's custom-instruction feature: Google's help page says Gems in the Gemini app become read-only on 17 November 2026 and are removed on 17 December 2026, converted to skills, for personal accounts of users 18 and over ([Google, *About the transition from Gems to skills*](https://support.google.com/gemini/answer/18560919), undated page, read 15 Nov 2026). Features of this kind change. The spec, the briefs and the logs belong in your own files (BW4 §5), with the product holding a mirror at most.

## Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log

Part 1 builds the five on the Academy case, as the case file records the project being specified. Part 2 gives each as a template for your project.

Two conventions, as in BW3 and BW4. Every fact about Academy comes from the Academy case file and is cited by section. Where the case file does not hold a value, the cell says `[NOT IN CASE FILE: …]`; those are blanks for the project's owner, and nothing in them is a claim. Wording that turns a case fact into a spec line, and anything marked as this unit's proposal, is this unit's (stated opinion). Files are named as in BW4's Part 3, with its inputs folder named `briefs/`; this unit adds three: `SPEC.md` and `BUILD-ORDER.md` beside `INDEX.md`, and `records/decisions.md` beside the backlog and changelog. Each is listed in `INDEX.md`, read by name.

Drafting the spec is row 10 of BW2's routing table, "A plan or spec"; route it from there.

### Part 1 · On the Academy case

#### 1a · The one-page spec (`SPEC.md`)

The case file holds no spec document for Academy as a whole. The spec below is reconstructed from what the case file records as the method's rules and the project's state; it shows what Academy's spec would have said, with its gaps marked.

> **Project.** Academy: a library of self-study courses, published as one website with one design (Academy case file §1).
>
> **Reader.** Each course names its own reader in its shared preamble (§2). Building with AI's reader: an experienced professional who reasons and writes well, uses a chat assistant with no method, may not write code, and brings one real project (§2). [NOT IN CASE FILE: the reader of the other courses.]
>
> **Goal (one sentence).** A library of self-study courses, each unit a long-form report with its sources cited in place and a closing deliverable built in full, published from one repository as one website (§1).
>
> **Measurable outcomes.**
> 1. Every course is specified before it is written: a goal in one sentence, three measurable outcomes, eight to twelve core units and two or three deep dives, each unit with a scope, a deliverable and a brief (§2).
> 2. Every unit is filed only after a fresh check by a separate context, with each finding verified and applied (§2, §3).
> 3. Every sample audit, run every four units, returns pass: no unit with more than one sampled claim in ten failing (§2).
> 4. The site is built from the repository by script; no page is styled by hand (§1).
> 5. The model that wrote each unit is recorded (§2).
>
> **Non-goals** (this unit's proposal; the case file records none).
> - [NOT IN CASE FILE: non-goals]. Proposed: no measure of time or money per unit is kept (the record holds none, §9); no unit is written outside the method for comparison (§9). Each needs the owner's decision before it is a non-goal.
>
> **Definition of done, for every unit.** See 1d.
>
> **Out of the spec, by pointer.** The method's full procedure: the rules folder (BW4, Part 3; in Academy's own layout no file named INDEX.md, INSTRUCTIONS.md or BUILD-ORDER.md appears in the records, and their equivalents are `docs/courses-index.md`, `docs/project-instructions.md` and each course's build order as a list in its data file, §1). Each course's preamble and briefs: `briefs/<course>/`. Open flags and proposals: `records/backlog.md`. Decisions: `records/decisions.md`.
>
> **Re-check by.** Six months after the facts were read, on the method's staleness interval (§2).

#### 1b · The build order (`BUILD-ORDER.md`)

The case file records the method's order (syllabus, briefs, units in order, check, file, audit every four units) and one unit list: the two private courses' 22 units in build order, with the date each was written (Academy case file §1); it gives no Takes or Gives for them. This build order is worked on this course, Building with AI, from its own course map, which you can read; each Takes entry is read from the Gives lines of the units named. The boundaries are set on the case's four-unit audit interval (Academy case file §2).

| # | Unit | Takes from | Gives to | Boundary after it |
|---|---|---|---|---|
| 1 | BW1 · Mental model | none | BW3, BW4, BW6 | |
| 2 | BW2 · Choosing the model and the effort | none | BW7, BW10 | |
| 3 | BW3 · Briefing | BW1 | BW5, BW6, BW7 | |
| 4 | BW4 · Context engineering | BW1 | BW5, BW8 | Review 1: open flags on BW1 to BW4 |
| 5 | BW5 · Specifying a project | BW3, BW4 | every later unit; BW7, BW9 | |
| 6 | BW6 · Research and verification | BW1, BW3, BW5 | BW8, BW9 | |
| 7 | BW7 · Pipelines | BW2, BW3, BW5 | BW8, BW9 | |
| 8 | BW8 · Skills and automation | BW4, BW5, BW6, BW7 | BW9 | Review 2: BW5 to BW8 |
| 9 | BW9 · Agents | BW5, BW6, BW7, BW8 | BW10, DD-BW1 | |
| 10 | BW10 · Cost, limits, privacy | BW2, BW5, BW9 | DD-BW3 | |
| 11 | DD-BW1 · How the best practitioners work | BW5, BW9 | DD-BW3 | |
| 12 | DD-BW2 · One project, with its numbers | BW5 | DD-BW3 | Review 3: BW9 to DD-BW2 |
| 13 | DD-BW3 · Audit your own usage | BW5, BW10, DD-BW1, DD-BW2 | none | Final review |

Check before starting: every "Takes from" entry sits higher in the table than its own row. It does.

#### 1c · A unit brief, on the case

Academy's brief is a shared preamble joined to a unit brief (Academy case file §2). The case file describes both and holds the text of neither; for this course it gives the reader and the goal (§2), and the rest of the preamble's contents are marked. The unit block is worked on this unit, BW5, from the Aim and Gives lines of this course's map; the rest follows BW3's form.

    SHARED PREAMBLE (identical for every unit of the course)
    READER: an experienced professional who reasons and writes well, uses a chat assistant with no method, may not write code, and brings one real project (as the case file gives it, §2)
    GOAL: by the end of the course the reader can say what the model saw when an output fails; brief a task so that the first output is usable and keep a project structure that does not rot; verify AI-written work by sample before trusting it; and decide what to hand to an agent, with one real project of their own specified and running (as the case file gives it, §2)
    SOURCING STANDARD: [NOT IN CASE FILE: the standard's text; the case file records only that a sourcing checklist exists and that the writer runs it (§2)]
    TONE: [NOT IN CASE FILE: the tone rules]

    UNIT BRIEF · BW5 · Specifying a project
    AIM: turn an idea into a one-page spec and a build order that one context per unit can finish.
    TAKES: BW3 (the brief form), BW4 (the project structure).
    GIVES: the spec and build order every later deliverable is built against; the flag-and-review rule BW7 and BW9 rely on.

    TASK: Write unit BW5 in full, with its deliverable built in full.
    READER: as in the preamble.
    OUTPUT: one Markdown file, a long-form report, 2,000 to 6,000 words by guide (Academy case file §1), with a Sources list.
    CONSTRAINTS:
    - Cover, in order: [NOT IN CASE FILE: the unit's list of topics].
    - Point to filed units by code and section; do not repeat them.
    - Do not reword this brief. If it is wrong, build what it allows and raise a flag.
    DONE WHEN: the lines in 1d, plus:
    - the deliverable is the spec, build order, brief, done-when lines and decision log, built on the case and then as templates;
    - the flag-and-review rule is stated as numbered steps.
    MATERIAL: the units already filed (BW1 to BW4) and nothing else from the project (Academy case file §2).
    TASK (again): write BW5 now.

#### 1d · Done-when lines, on the case

Every unit, from the case file's record of the method:

- [ ] The deliverable is built in full; nothing is outlined or described (§1).
- [ ] Every source is cited in place (§1).
- [ ] Length is inside the 2,000 to 6,000-word guide (§1), or the unit's notes say why the topic needed more (this unit's proposal).
- [ ] The writer has run the sourcing checklist and listed up to ten claims it could not verify (§2).
- [ ] A separate context that did not see the writing has checked every cited claim and the deliverable against the brief; each finding is verified and applied as an exact replacement (§2).
- [ ] Every figure has passed a separate check: each label and number is already in the text (§6).
- [ ] The model that wrote the unit is recorded (§2).
- [ ] The backlog row is moved to the changelog and the next prompt is written (§2).

#### 1e · The decision log (`records/decisions.md`), on the case

Format after Nygard (§6), with a re-check date added (§6). Dates the case file does not hold are marked.

| # | Title | Context | Decision | Status | Consequences | Date · re-check by |
|---|---|---|---|---|---|---|
| D1 | One context per unit | Leaked context is how a course starts repeating itself (§2) | Each unit is written in a new chat or a fresh agent context that sees only its brief and the units already filed (§2) | accepted | A unit must be buildable from files alone; lost writers can be resumed from working files (§7) | [NOT IN CASE FILE: the one-chat rule's date]; an isolated agent context counted as a new chat from 29 Oct 2026 (§2) · [NOT IN CASE FILE] |
| D2 | Fresh check before filing | Audit 1: 23 of 91 claims failed in three units; the deliverables did not exist (§3) | Every unit of that family gets a fresh check before filing (§3) | accepted | 36 units checked; 28 drafts had at least one error (§5) | 28 Oct 2026 (§2) · [NOT IN CASE FILE] |
| D3 | Drop a figure after three failures | Figures fail their check (§6) | A figure that fails three times is dropped (§6) | superseded by D4 | Two figures dropped (§6) | [NOT IN CASE FILE] |
| D4 | Figures are never dropped | Set by the owner, replacing D3 (§6) | Figures are fixed until they pass (§6) | accepted | One sitemap figure passed on its eighth check (§6) | 3 Nov 2026 (§2) · [NOT IN CASE FILE] |
| D5 | Checks run on the named model version | A session's "fable" resolved to a newer version than the method names (§7) | Checks it ran are recorded as owed again on the named version (§7) | accepted | [NOT IN CASE FILE: whether they were re-run] | [NOT IN CASE FILE] |

#### 1f · Backlog, changelog and flag rows, on the case

Row formats are this unit's proposal; the rules are the case's (§2).

    records/backlog.md
    ## Rows
    | Row | Work | Brief | Done when | Status |
    | [NOT IN CASE FILE: row id] | Write unit [code] | briefs/<course>/[code].md | 1d + the brief's own lines | next |
    ## Proposed (not worked until the owner confirms; Academy case file §2)
    | Proposal | What it does | Touches | Raised by | Decision |
    ## Flags (open until the next boundary; §9 of this unit)
    | Flag | What is wrong | Found in | Proposed change | Boundary | Decision |

    records/changelog.md
    | Date | Row | Model | Result in one line |

The case file records proposals and the backlog-to-changelog move, and for this course flags raised for each contradiction between units or briefs and each need the syllabus does not meet, a flag that would change a brief waiting for a syllabus review the owner confirms (§2); the Flags section's place in the backlog and its row format are this unit's proposal.

### Part 2 · Templates for your project

Copy each into its file, fill every blank, delete what does not apply. Each blank says what goes in it.

#### 2a · `SPEC.md` (one page, at most about 400 words)

> **Project.** [*one line: what it is*]
>
> **Reader.** [*who reads the output, what they already know, what they will do with it*]
>
> **Goal (one sentence).** [*what exists when the project is finished*]
>
> **Measurable outcomes.**
> 1. [*a thing that will be true at the end, which you can check by reading or counting*]
> 2. [*a second*]
> 3. [*a third; stop at five*]
>
> **Non-goals.**
> - [*something a reasonable person would expect this project to do, which it will not*]
> - [*a second; aim for three*]
>
> **Definition of done, for every unit.** See `BUILD-ORDER.md`, "Done when, every unit".
>
> **Out of the spec, by pointer.** [*where the rules, the briefs, the backlog and the decision log live: file paths*]
>
> **Re-check by.** [*the date six months after the facts this spec rests on were read*]

#### 2b · `BUILD-ORDER.md`

| # | Unit (code · title) | Artefact it produces | Takes from | Gives to | Boundary after it |
|---|---|---|---|---|---|
| 1 | [*code · title*] | [*the one artefact, named*] | [*earlier units, or "none"*] | [*later units, and what they take*] | [*"Review n" or blank*] |
| … | | | | | |

Checks before the first unit starts:

- [ ] Every "Takes from" entry sits higher in the table than its row.
- [ ] No unit needs more than three earlier units read in full; it takes their named deliverables.
- [ ] Each unit passes §3's four tests.
- [ ] A boundary is set at least every [*number*] units, and after the last.

**Done when, every unit:**

- [ ] [*the artefact is built in full*]
- [ ] [*a sourcing or accuracy check you can run by reading*]
- [ ] [*a length or format check*]
- [ ] [*a review by a context that did not do the work: BW6 sets how*]
- [ ] The backlog row is moved to the changelog with date, model and result; the next prompt is written.

#### 2c · Unit brief (`briefs/[code].md`), in BW3's form

    SHARED PREAMBLE (paste the same text into every brief)
    READER: [from SPEC.md: Reader]
    GOAL: [from SPEC.md: Goal]
    STANDARD: [the rules every output must meet, or a pointer to the rules file]
    TONE: [the register, and the habits to avoid]

    UNIT BRIEF · [code] · [title]
    AIM: [what the reader can do after this unit, in one sentence]
    TAKES: [the earlier units this one reads, from BUILD-ORDER.md]
    GIVES: [what later units take from this one, from BUILD-ORDER.md]

    TASK: [the verb of the artefact, then the artefact]
    OUTPUT: [the container, the layout, the length]
    CONSTRAINTS:
    - Cover, in order: [the unit's topics]
    - [what is in scope and what is out, beyond SPEC.md's non-goals]
    - Do not reword this brief. If it is wrong, build what it allows and raise a flag in records/backlog.md.
    DONE WHEN: the every-unit lines in BUILD-ORDER.md, plus:
    - [a check specific to this unit]
    MATERIAL: [the units in TAKES, and nothing else from the project]
    TASK (again): [the TASK line, repeated, if the material is long]

Version line, at the foot of the file: `v[n] · [date] · [decision-log entry that changed it, or "first version"]`.

#### 2d · `records/decisions.md`

| # | Title | Context | Decision | Status | Consequences | Date · re-check by |
|---|---|---|---|---|---|---|
| D[n] | [*a short noun phrase*] | [*what forced the choice: the facts, the constraint, the failure*] | [*what was decided, in one or two sentences*] | [*proposed, accepted, or superseded by D[n]*] | [*what is now true, including what it costs*] | [*date decided · date six months later, if it rests on facts that change*] |

Never edit an accepted row. To reverse it, add a new row and mark the old one superseded.

#### 2e · Backlog, changelog and flags (`records/backlog.md`, `records/changelog.md`)

    records/backlog.md
    ## Rows
    | Row | Work | Brief | Done when | Status |
    | [id] | [one unit or one task] | [path to its brief] | [pointer to the lines] | [next, or waiting on row id] |
    ## Proposed
    | Proposal | What it does | Touches | Raised by | Decision |
    | [id] | [the task, one line] | [other files or units it would change] | [the row that found it] | [blank until you decide: confirmed as row id, or refused, with the reason] |
    ## Flags
    | Flag | What is wrong | Found in | Proposed change | Boundary | Decision |
    | [id] | [the spec line or brief line, quoted] | [the row that found it] | [the new wording] | [the review it waits for] | [blank until the boundary: accepted as D[n], changed, or refused, with the reason] |

    records/changelog.md
    | Date | Row | Model | Result in one line |
    | [date] | [row id] | [the model that actually did the work] | [what now exists] |

**The flag-and-review rule**, to paste into your instruction file (BW4, Part 3) as one rule, or keep in your rules file and point to:

1. During the work, nothing in `SPEC.md` or a brief changes. If either is wrong, build what it allows and add a flag.
2. Flags wait for the next boundary in `BUILD-ORDER.md`.
3. At the boundary, decide every open flag: accept, change or refuse. An accepted flag makes a new version and a decision-log row.
4. Check filed units against each accepted change; a unit it makes wrong becomes a proposed row.
5. No unit starts while a flag that touches it is open.
6. A chat works its own row and proposes everything else.

## Sources

- Anthropic. *Best practices for Claude Code*. Claude Code documentation, read 15 November 2026. https://code.claude.com/docs/en/best-practices.md (vendor)
- Anthropic. *Prompting best practices*. Claude Developer Platform documentation, read 15 November 2026. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (vendor)
- Ballinger, K., Kornder, J. and Aitbayev, S. *Conductor: Introducing context-driven development for Gemini CLI*. Google Developers Blog, 17 December 2025. https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/ (vendor)
- Böckeler, B. *Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl*. martinfowler.com, 15 October 2025. https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html (practice)
- Delimarsky, D. *Spec-driven development with AI: Get started with a new open source toolkit*. GitHub Blog, 2 September 2025. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit (vendor)
- Friel, A. *Using PLANS.md for multi-hour problem solving*. OpenAI Cookbook, 7 October 2025. https://developers.openai.com/cookbook/articles/codex_exec_plans (vendor)
- Google. *About the transition from Gems to skills*. Gemini Apps Help, undated; read 15 November 2026. https://support.google.com/gemini/answer/18560919 (vendor)
- Kotha, A., Lee, J., Zakariasson, E. and Kavanaugh, E. *GPT-5 prompting guide*. OpenAI Cookbook, 7 August 2025 (marked archived). https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide (vendor)
- Kwa, T., West, B., Becker, J., Deng, A., Garcia, K. et al. *Measuring AI Ability to Complete Long Software Tasks*. arXiv 2503.14499 v3, 25 February 2026. https://arxiv.org/html/2503.14499v3 (preprint)
- Laban, P., Hayashi, H. et al. *LLMs Get Lost In Multi-Turn Conversation*. arXiv 2505.06120 v1, 9 May 2025. https://arxiv.org/pdf/2505.06120 (preprint)
- Lacan, O. *Keep a Changelog*, version 1.1.0. https://keepachangelog.com/en/1.1.0/ (practice)
- Nygard, M. *Documenting Architecture Decisions*. Cognitect blog, 15 November 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (practice)
- Reed, H. *My LLM codegen workflow atm*. 16 February 2025. https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/ (practice)
- Schwaber, K. and Sutherland, J. *The 2020 Scrum Guide*. November 2020. https://www.scrumguides.org/scrum-guide.html (practice)
- Swaminathan, N. and Singh, D. *Introducing Kiro*. Kiro blog, 14 July 2025. https://kiro.dev/blog/introducing-kiro/ (vendor)
- Tufano, M., McClure, J., Cambronero, J. et al. *Grounding AI Agents in Contracts: An Empirical Evaluation of Spec-Driven Test Generation*. arXiv 2608.17177 v2, 21 August 2026. https://arxiv.org/pdf/2608.17177 (preprint)
- Ubl, M. *Design Docs at Google*. Industrial Empathy, 6 July 2020. https://www.industrialempathy.com/posts/design-docs-at-google/ (practice)
- Wotherspoon, J. and Patel, A. *Subagents have arrived in Gemini CLI*. Google Developers Blog, 15 April 2026. https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/ (vendor)
- Young, J. *Effective harnesses for long-running agents*. Anthropic Engineering, 26 November 2025. https://anthropic.com/engineering/effective-harnesses-for-long-running-agents (vendor)
- Academy case file, §1 to §9 (compiled 11 November 2026).

## Unsure list

1. Tufano et al., arXiv 2608.17177 v2 (21 Aug 2026): the figures (63.2% against 53.4%, p = 0.035; 41.1% against 36.9% on one run; branch 48.9% against 46.4%; line 74.4% against 74.8%; 1.38 times the tokens), the reading of detect@5 as "caught by any of five runs", and the stated acceptance at SpecOps '26 were read through a fetch of the PDF, not checked against its tables directly.
2. METR, arXiv 2503.14499: the v3 date (25 Feb 2026) and the retitling to "Measuring AI Ability to Complete Long Software Tasks" are as the fetched HTML gave them; "success falls steadily as tasks get longer" paraphrases the paper's reported exponential, negative relation between human task time and success.
3. Anthropic, "Effective harnesses for long-running agents": the author is given as Justin Young (the page credits other contributors) and the date as 26 Nov 2025, both from the fetched page.
4. Nygard (2011): the status values beyond "proposed" (accepted, superseded) and the rule that a reversed record stays, marked superseded, were read as a summary of the post; only "proposed" was quoted verbatim.
5. Scrum Guide (2020): the refinement sentence is quoted only up to "Product Backlog items"; the rest is paraphrased because the fetch did not give the end of the sentence verbatim.
6. Anthropic, "Prompting best practices" (read 15 Nov 2026): the overengineering note names Claude Opus 4.5 and Opus 4.6; whether the page says the same of later models was not checked.
7. Böckeler, martinfowler.com: the date 15 Oct 2025 is from the fetched page; the article may have been revised since.
8. Google, "About the transition from Gems to skills": the page is undated; the 17 Nov 2026 and 17 Dec 2026 dates apply to personal accounts as read on 15 Nov 2026.
9. OpenAI's ChatGPT Projects help page could not be read (the fetch failed at the site), so the unit says "Not checked" for ChatGPT's plan-approval equivalent; no ChatGPT-app equivalent of a spec workflow is cited.
10. Build order (Deliverable 1b) and the dependency grid (§4): each Takes entry is read from the Gives lines of this course's map; that every later unit, including DD-BW2, takes from BW5 rests on BW5's Gives line ("every later deliverable"), not on the later units' own briefs, which were not seen.
Object: none

Fresh check 2026-11-15 (Opus 5.5): fix · 1 errors, 5 should-fix, 12 minor; 17 applied, 1 held (f18, the 1c reader line: the maintainer's call, held); report `audits/building-with-ai/fresh-check-BW5.md`

Correction 17 Nov 2026 (CP-4), found by W-SP1, each change checked by a fresh Opus 5.5 agent against case-academy.md

Correction 17 Nov 2026 (CP-5), found by the flag F124 pass and checked by a fresh Opus 5.5 agent against the Academy case file; report audits/building-with-ai/corrections-2026-11-17-CP5-BW5-BW7-BW8-DD-BW2-DD-BW3.md.

Correction 17 Nov 2026 (CP-5, second pass), found by the flag F124 pass and checked by a fresh Opus 5.5 agent against the Academy case file; report audits/building-with-ai/corrections-2026-11-17-CP5b-BW5-BW7.md.
