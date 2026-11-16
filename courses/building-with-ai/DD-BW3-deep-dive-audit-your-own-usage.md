---
code: DD-BW3
title: "Deep dive: audit your own usage"
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: off
---

# DD-BW3 · Deep dive: audit your own usage

This unit has you read your own chats as evidence and write, from what they show, the changes that would save you the most. It gives the method (a window, a list, four labels per ask), the four patterns worth counting, a way to test the rules of BW10 and DD-BW1 against your record, what reading your own history exposes and how to keep it contained, and one worked example from Academy (Academy case). It ends with a classification sheet, a gap report, the review as a sixty-minute procedure and a set of changes restated for any project.

It was written with search off for drafting; seven pages were read on the web on 16 November 2026 to check specific points: Anthropic's and OpenAI's export pages, Google's Gemini download page, Claude Code's sessions page, and the research cited in §1 and §5; every product fact carries that date. Vendor facts that other units of this course state (plan limits, retention periods, memory settings, caching) are not restated: the unit points to the section that states them, with the date it was read there, and you re-read the vendor's page on the day you act on it.

What it assumes, by section and without restating: the routing table you built in BW2 (Deliverable); the three common briefing failures (BW3 §6); the skill trigger test and its pass rule (BW8 §4) and the count of repeats before automating (BW8 §7); the sampling arithmetic of BW6 §5; the run log of BW7 §7; the twelve usage rules of BW10 (Deliverable Part 1) and its sections on retention and on where material belongs (BW10 §6, §7); the ten operating rules of DD-BW1 (Deliverable Part 2); and the case report and the ten-change template of DD-BW2 (Deliverable Parts 1 to 4). Grades follow the course: **measured**, **documented practice**, **stated opinion**.

## 1 · Why a review of your own chats finds what a course cannot

A course is built from evidence about other people's work: studies on tasks someone else chose, vendor guidance written for every customer at once, and in this course one real project, the Academy case. None of it knows your mix of tasks, the model you actually open for each, or where your chats go wrong.

The mix varies more than a course can assume. A usage study of ChatGPT, a working paper on a sample of its conversations classified by an automated pipeline, reports that "Practical Guidance," "Seeking Information," and "Writing" together account for nearly 80% of all conversations, and that non-work messages grew from 53% to more than 70% of usage ([Chatterji et al., *How People Use ChatGPT*, NBER Working Paper 34255, September 2025](https://www.nber.org/papers/w34255); working paper, not peer-reviewed; measured on ChatGPT consumer use). Anthropic's Clio system, which describes Claude.ai use by attributes it calls facets, among them the conversation's topic and its number of turns, was run over one million Claude.ai Free and Pro conversations ([Tamkin et al., *Clio: Privacy-Preserving Insights into Real-World AI Use*, arXiv:2412.13678, 18 December 2024](https://arxiv.org/html/2412.13678v1); preprint, vendor-authored). Both are population figures. They tell you what millions of people do on average and nothing about which of your tasks takes most of your week, which is the number every routing and usage rule in this course depends on (this unit's inference).

A second reason is structural. The rules you set for a project cover the tasks you thought of when you set them. DD-BW2 §10 found the same shape in the Academy record: the record supported the rules its stages produced numbers for, and was silent on the rest (stated opinion, DD-BW2's reading). A chat history is the one record every assistant keeps whether or not you planned to keep one, so it is the one place a task you never wrote a rule for shows up with a count.

The third reason is the evidence on recording itself. A meta-analysis of 138 randomised studies (N = 19,951) found that interventions which increased how often people monitored their progress improved goal attainment, d+ = 0.40, with larger effects when progress was physically recorded and when it was reported to others ([Harkin, Webb, Chang and colleagues, *Does Monitoring Goal Progress Promote Goal Attainment? A Meta-Analysis of the Experimental Evidence*, *Psychological Bulletin* 142(2), 2016, 198–229](https://eprints.whiterose.ac.uk/91437/); measured, on personal goals outside AI use (the repository record does not list their domains), none of them about AI tools). That an audit of your own chats works the same way is this unit's inference, not something any study has measured.

**The case** (Academy case). Academy is a library of self-study courses built by one person with Claude in October and November 2026, with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9). Its owner's chats in the project were reviewed for one deep dive: 53 chats over six days, the project's whole history at the time (case file §8). One review of one person's chats is an anecdote; §6 reads it for its method only.

**Grade of this section's claim** that a review of your own chats finds what a course cannot: stated opinion, built on measured population data that shows how much use varies and on measured evidence for recording progress in other domains.

## 2 · The method: a window, a list, four labels

The method has four steps: choose a window, list every chat in it, label every ask with four labels, then count. Each label is defined below with what it cannot tell you. The method is the one the case's review used (case file §8: each ask classified by task type, model, outcome and number of turns); the definitions, the extra columns and the limits are this unit's (stated opinion unless a source is named).

### Choose a window

A window is a period and the chats in it. Three rules (stated opinion):

1. **Long enough to hold repeats.** A task you do weekly should appear at least three times, because BW8 §7 has you count runs before automating, and the rule of three it reports extracts a procedure on its third repeat. Four weeks is the shortest window that does that for weekly work.
2. **Short enough to label in one sitting.** The sixty-minute procedure in the Deliverable gives labelling thirty minutes: sixty chats at thirty seconds each, or thirty at a minute (an estimate, unmeasured). Take the shorter of four weeks and the most recent thirty to sixty chats.
3. **Every chat in it, not the memorable ones.** Chats you remember are the ones that went unusually well or badly. If the window holds more chats than you can label, draw a sample by number, as BW6 §5 step 3 does for claims, and write down that you sampled.

Write the window down with its first and last date, and say whether it was an ordinary stretch of work. The case's window was the project's whole history at the time, six days (case file §8), so it had no selection problem; the case file does not say whether those six days were typical of later work.

### List every chat

You need a list you can check is complete. On Claude (all read 16 November 2026, vendor):

- **claude.ai.** Settings > Privacy > "Export data". Exports are available to individual users on Free, Pro, Max and Ultra; on Team or Enterprise you can export your own data once an organisation owner turns this on. The export includes "conversation data and the user data for your account", and does not include the original files you uploaded. It cannot be run from the iOS or Android app. A download link arrives by email; it "will expire 24 hours after it's created, and it may work only once" ([Claude Help Center, *Export your Claude data*](https://support.claude.com/en/articles/9450526-export-your-claude-data), labelled "Updated this week"). The page does not say what file format the export uses. BW1 §3 describes chat search on paid plans, read 15 November 2026; it finds chats by topic and does not give you a complete list.
- **Claude Code.** Each session is "a saved conversation tied to a project directory". By default transcripts are stored as JSONL at `~/.claude/projects/<project>/<session-id>.jsonl`, and the retention is 30 days unless you change the `cleanupPeriodDays` setting. `claude --resume` or `/resume` opens a session picker whose rows show the session's name, generated title, summary or first prompt, with time since last activity, git branch and file size; `Ctrl+A` widens it to every project on the machine. `/export` saves the current conversation as plain text. The desktop app, claude.ai/code and the VS Code extension each keep their own session list ([Claude Code documentation, *Manage sessions*](https://code.claude.com/docs/en/sessions)). Two consequences for a review: a window older than 30 days is gone from the command line unless you changed the setting, and a review that reads only one surface's list misses the others.

The page also warns that the transcript format "is internal to Claude Code and changes between versions", so a script that parses those files can break on any release (same page). For a review by hand, the picker and `/export` are enough.

### Label every ask

The unit of the sheet is the chat, labelled by its first **ask**, the message that sets its task. A later message in the same chat that starts a different task is an ask too: it goes in the "two tasks" column with its own task type, and that column is itself a count (§3).

**1 · Task type.** A short list of five to nine types, written down with a one-line definition each before you label anything. Take the types from your BW2 routing table, one per row, and add "other". Define each by the artefact it produces ("a table extracted from a document"), never by topic, so that two chats about the same subject but producing different things fall in different types.
*Limits.* The labels are yours and applied by hand, as the case's were (case file §8). Boundary cases will fall between two types. To see how consistent you are, relabel five chats picked by number at the end of the sitting and count how many get the same label (stated opinion; a second reader would be a stronger check, and is rarely available). Large-scale studies label with a model instead: Clio reports reconstructing the true topic distribution of a synthetic dataset with 94% accuracy, and its authors still call its outputs preliminary and in need of further validation before decisions rest on them (Tamkin et al., preprint). A model labelling your chats raises a privacy question (§5).

**2 · Model, and effort where recorded.** The model the chat actually ran on, read from a record: the model shown in the chat, a log line, a commit trailer, your BW7 run log. Never from memory. Where nothing records it, write "not recorded". Effort the same way. The case read its model from commit trailers (case file §8); its labels do not include effort.
*Limits.* What you asked for is not always what ran: in the case, a session's model named "fable" resolved to a newer version than the method named (case file §7), which is why BW7 §7 has the log record the model that ran. A chat that switched models mid-way gets both, marked as a switch.

**3 · Outcome.** One of five values, defined before you start:
- *used as is*: the output went where it was meant to go without changes of substance;
- *used after edits*: it went there after you changed it;
- *redone*: you asked again, in this chat or another, for the same output;
- *abandoned*: nothing from the chat was used;
- *not seen*: you cannot tell from the record.
*Limits.* The chat records what the model wrote, rarely what you did with it. "Used" is a proxy, as the case's "accepted" was (case file §8), and the case could not see 14 of its 53 endings (§8). Do not guess an outcome to shrink that count: "not seen" is a finding about your record.

**4 · Turns.** Count your own messages in the chat, and among them your **corrections**: messages that fix, reject or narrow what the model produced. The model's messages are not counted, because where a chat runs agents or tools the thread can hold many messages you did not trigger one by one (stated opinion; check what your tool shows).
*Limits.* Turns mix length with friction. A long chat can be a good working session and a two-message chat can be a bad answer you walked away from; read turns beside the outcome, never alone. Clio counts turns as a facet computed directly, without a model (Tamkin et al., preprint). A count needs no judgement, which makes this the most reliable of the four labels (stated opinion).

### The extra columns

Four yes-or-no columns turn the labels into the patterns of §3. Mark them while you have the chat open:

| Column | Mark it when | Pattern it feeds (§3) |
|---|---|---|
| Two tasks | the chat holds asks of two task types | badly put |
| Routing | the model or effort differs from your BW2 row for the task type | wrong tool |
| Procedure | you typed a procedure you have typed before, or a skill you have was expected and did not load | by hand |
| Repeat research | the chat searched or researched a question an earlier chat in the window already answered | paid twice |

The sequence, as one figure:

```viz
{"kind": "flow", "steps": [{"label": "Choose a window", "note": "four weeks or 30 to 60 chats, whichever is shorter"}, {"label": "List every chat", "note": "export or session list; check both ends"}, {"label": "Label every ask", "note": "task type, model, outcome, turns"}, {"label": "Mark four columns", "note": "two tasks, routing, procedure, repeat research"}, {"label": "Count", "note": "per pattern and per rule"}, {"label": "Rank changes", "note": "largest count first"}], "caption": "The review's six steps, as §2 of this unit defines them: the four labels follow the Academy case's review (Academy case file §8); the window rules, the extra columns and the ranking (DD-BW2, Deliverable Part 2) are stated opinion."}
```

## 3 · The patterns to look for

Four patterns account for most of what a review can change, because each is a cost you pay again every time the habit repeats. For each: what it looks like in the sheet, the count to take, and the unit that teaches the fix. A pattern found in one chat is a flag; it becomes a change when the count is two or more (stated opinion; §7 gives the ranking).

### An ask that was badly put

**In the sheet:** chats with two or more corrections; chats marked "two tasks"; chats whose outcome is "redone".

**Why these.** BW3 §6 names three failures the vendors' guidance and the studies converge on: asking for a plan when you wanted the thing, burying the ask, and stacking unrelated tasks in one window; it grades its one-artefact-per-brief fix documented practice. A correction is the visible cost of each: the model produced what the words asked for, and you spent a message saying what you meant. Stacked tasks show directly in the "two tasks" column.

**The count to take:** the number of chats with two or more corrections, and the share of all corrections they hold. If a few chats hold most of the corrections, read those chats' first messages side by side: the defect is usually the same one, and it is in the brief (stated opinion). Then check the type: if the heavy chats are mostly one task type, the fix is that type's brief in your BW3 set, not your briefing in general.

### A tool wrong for the job

**In the sheet:** the routing column; and, among the chats on your heaviest model, those whose task type your routing table puts lower.

**Why.** BW2's routing table assigns each recurring task a tier and an effort, with the reason. A chat that ran on another tier is either a deliberate exception or a habit, and the review cannot tell which without the count: a heavy model opened for a short reply because it was the last one selected costs the gap between the tiers each time (BW2 §1 gives the cost side; it is not restated here). The other direction counts too: a light model on a task the routing table puts higher, where the outcome is "redone".

Three related marks belong here. Research or agent runs for a task a single chat would have answered (DD-BW1 rule 6, "the simplest setup that does the job"). Connectors or tools on in a chat that called none (BW10 rule 7). And a mid-chat switch of model or effort (BW10 rule 3): count it, and read the note on rule 3 in §4 before you score it.

### Work done by hand that a saved procedure already does

**In the sheet:** the procedure column.

**Two forms.** The first is a procedure you typed into a prompt three or more times in the window: BW8 §7's count says a procedure repeated three times the same way is a candidate for a skill, a template or a script, and gives the arithmetic for whether it pays. The second is a skill you already have that did not load when the task called for it, or the wrong one that did. That second count is a misfire count, and BW8 §4 gives the pass rule for judging a skill's triggering; add each misfire you find to your skill's test set as a new row, as BW8 §4 says.

**The count to take:** for each procedure, the number of chats where you typed it; for each skill, the number of chats where it should have loaded and the number where it did.

### Research paid for twice

**In the sheet:** the repeat-research column.

**Why.** BW10 rule 6 says a question is researched once, filed with its source and date, and searched again only at its six-month check; BW10 grades it documented practice and cites the vendor's 2025 measure of how many more tokens a research run uses than a chat (BW10, Deliverable Part 1, rule 6). A question researched in two chats inside one window is that rule broken; count questions, so two chats on one question count once.

**Not every repeat is waste.** A fresh checker that re-opens the sources a writer cited is the check doing its job: DD-BW1 rule 3 has the check run in a context that did not see the writing, and BW6 §4 has the checker open each cited page itself. Mark a repeat only when the second search served the same purpose as the first.

### Where each pattern is read

```viz
{"kind": "matrix", "cols": ["Task type", "Model", "Outcome", "Turns", "Two tasks", "Routing", "Procedure", "Repeat research"], "rows": [{"label": "Badly put", "cells": [{"mark": "group", "tone": 4}, null, {"mark": "redone", "tone": 3}, {"mark": "corrections", "tone": 3}, {"mark": "yes", "tone": 3}, null, null, null]}, {"label": "Wrong tool", "cells": [{"mark": "group", "tone": 4}, {"mark": "tier", "tone": 3}, {"mark": "redone", "tone": 4}, null, null, {"mark": "yes", "tone": 3}, null, null]}, {"label": "By hand", "cells": [null, null, null, null, null, null, {"mark": "yes", "tone": 3}, null]}, {"label": "Paid twice", "cells": [null, null, null, null, null, null, null, {"mark": "yes", "tone": 3}]}], "legend": [{"mark": "yes", "means": "the column that counts the pattern", "tone": 3}, {"mark": "group", "means": "read against the task type", "tone": 4}], "caption": "Which columns of the classification sheet count each of the four patterns, as §3 of this unit defines them (stated opinion; the fixes are taught in BW2, BW3 §6, BW8 §4 and §7, BW10 rule 6)."}
```

## 4 · Testing the rules of BW10 and DD-BW1 against your record

BW10's twelve usage rules (Deliverable Part 1) and DD-BW1's ten operating rules (Deliverable Part 2) each carry a column called "What your record shows", naming what your own chats would show if you kept or broke the rule. This section turns that column into a count on your sheet. The rules are not restated: open the two tables beside this one. Each rule keeps the grade its own unit gives it, and the case adds nothing to any grade.

**Four verdicts**, adapted from DD-BW2 §10's three (stated opinion): **kept** (the sheet holds chats where the rule applied and none broke it); **broken, n** (n chats broke it); **did not arise** (no chat in the window met the situation the rule covers); **not testable** (a chat history cannot show it, or your sheet has no column for it). A rule your chats cannot test marks a gap in your record, and the gap goes to the tenth change (§7).

### BW10's twelve rules

| BW10 rule | Grade, as BW10 gives it | Count on your sheet | Testable from chats? |
|---|---|---|---|
| 1 · One task, one chat | Documented practice | Chats marked "two tasks" | Yes |
| 2 · Back after a break, a new chat | Documented practice; the claude.ai hour is stated opinion | Chats resumed after a gap longer than BW10 sets; needs timestamps in your list | Partly: only where the record shows times |
| 3 · Model and effort before the first message | Documented practice | Mid-chat switches of model; of effort, where recorded | Model yes; effort only if recorded. See the note on rule 3 below |
| 4 · A file read once, never pasted or re-uploaded | Documented practice | Chats where one file was pasted or uploaded twice | Yes, if you open the chat |
| 5 · A paste carries only what this output needs | Documented practice | Pastes much larger than what the output used | By judgement only; mark, do not count, unless obvious |
| 6 · A question researched once | Documented practice; the 15× is the vendor's 2025 measure | Questions in the repeat-research column | Yes |
| 7 · Tools and connectors off unless used | Documented practice | Chats with tools or connectors on that called none | Only where the chat shows its tools |
| 8 · Light tasks outside the project | Documented mechanism; the rule is stated opinion | Short tasks run inside a heavy project | Yes, if your list shows the project |
| 9 · Every background run has an end | Documented practice | Runs without a done-when line or cap | Partly: the prompt shows the line; the cap is a setting |
| 10 · Usage read before a heavy task; credits capped | Documented practice | Heavy tasks stopped by a limit | Partly; the cap is a setting, not in chats |
| 11 · Material where it belongs; memory settings | Stated opinion on documented settings | Private or work material found in chats | Partly: the material shows; the settings do not |
| 12 · Training and deletion decided once | Documented facts; the rule is stated opinion | None | No: it is a setting and a decision |

**A note on rule 3.** BW10's source for rule 3 says an effort change breaks the cache "on most models", not on all (BW10, Deliverable Part 1, rule 3, citing Claude Code's prompt-caching page as read 16 November 2026). Count a mid-chat effort switch as a departure from the rule, and do not score it as a cache cost until you have read that page for your model and your plan on the day of your review.

### DD-BW1's ten rules

| DD-BW1 rule | Grade, as DD-BW1 gives it | Count on your sheet | Testable from chats? |
|---|---|---|---|
| 1 · Delegate what something other than your reading can check | Stated opinion; one supporting mechanism measured on GPT-4 in 2023 | Delegated tasks whose chat names no check | Yes, from the first message |
| 2 · Brief the result, not the steps | Documented practice | Briefs with no done-when line; outcomes "redone" though the brief was met | Yes, from the first message |
| 3 · The writer never checks its own work | Documented practice, vendor; no figures | Checks asked for in the chat that wrote the draft | Yes |
| 4 · Read what you send; label what you did not write | Stated opinion; documented practice for two of its cards | Outputs used as is that went to another person | Partly: the chat does not show what you read |
| 5 · Small pieces, one at a time | Stated opinion; documented practice for two of its cards | Chats asking for several outputs | Yes |
| 6 · The simplest setup that does the job | Documented practice, vendor | Research or agent runs for one-chat tasks | Yes |
| 7 · An unattended loop has four guards | Documented practice | Background runs missing a guard | Partly, as BW10 rule 9 |
| 8 · Files are the memory | Documented practice | Facts you re-typed because they lived only in an earlier chat | Yes, by reading |
| 9 · Never the trifecta | Stated opinion on a documented attack class | Chats holding private material, untrusted content and a way out at once | Only where the chat shows its tools |
| 10 · Effort is a setting; a number that matters gets two runs | Measured, on 2022 to 2024 models; the transfer to current models is inference | Prompts asking the model to think harder; key figures taken from one draw | First half yes; effort setting only if recorded |

DD-BW1 says of its own ten that only rule 10 rests on measured studies, on older models, and that the rules as a set are its synthesis (DD-BW1, Deliverable Part 2). A count of "broken" on your sheet does not raise or lower that: it says how often your work met the situation the rule covers, which is what decides whether the rule is worth your attention.

**The case.** The case file records that the case's review classified each ask and produced ten ranked changes, each tied to a count (§8); it does not say which of the course's rules the review tested, and DD-BW2 §10 is the only reading of the case against the rules. Its verdicts come from the project's records, not its chats.

## 5 · The privacy of doing this at all

A review re-reads everything you told an assistant, and makes copies. Three copies matter.

**The export.** On claude.ai it holds every conversation and the user data for your account (Claude Help Center, *Export your Claude data*, read 16 November 2026; vendor). It lands on your disk as a download. Treat it as BW10 §7 treats drafts and working files: a private store you control, read by name when needed. Download it once, label from it, and delete it when the sheet is done; a fresh export is a few clicks away for the next review.

**A model that reads your chats for you.** Labelling by hand keeps the history where it already is. Handing the history to an assistant to label sends every chat back into a new chat, which then falls under the retention and training settings BW10 §6 lists (as read there on 16 November 2026: re-read them on the day), and, if memory is on, can write memory entries from what it reads; BW10 §6 records that deleting a chat does not delete the memory entries written from it. If you use a model, give it only the first message of each chat, trimmed of names, in a chat where memory and training are set as BW10's Template D records them (stated opinion). The vendors' own studies of usage show the standard for reading chats at scale: Clio was designed so that it works "without the need for human reviewers to read raw conversations", and keeps a cluster only if it exceeds minimum sizes for both unique accounts and conversations (Tamkin et al., preprint); the ChatGPT study classified its sample with "a privacy-preserving automated pipeline" (Chatterji et al., working paper). Those designs answer a different problem, many people's chats read by the vendor, but they show that the vendors treat reading chats as sensitive even in aggregate (this unit's reading).

**The sheet and the gap report.** Your chats name other people: clients, colleagues, family. The sheet does not need them, and the gap report should be something you could show a colleague. Three rules (stated opinion): the sheet holds labels and counts, never quotations longer than a few words; no row names a person other than you; a pattern is described by its kind ("two tasks in one chat"), never by what the chat was about when that would identify someone. If any chat in the window holds employer material, BW10 §8's five questions apply to the export and the sheet as they did to the chat.

**The case.** The case file was compiled from the project's own records "with private details removed" (case file header), and its record of the review is counts and a description of the method, with no chat quoted (§8). That is the form this unit asks of your gap report. One project; it shows the form is workable, not that it is sufficient.

## 6 · The worked example: one review of 53 chats (Academy case)

What the case file records about the review, in full (case file §8):

- The owner's chats in the project were reviewed for one deep dive: 53 chats over six days, the project's whole history at the time.
- By model, read from commit trailers: 31 chats ran on Opus, 18 on Fable, 4 on both.
- Each ask was classified by task type, model, outcome and number of turns. The labels were applied by hand; "accepted" was a proxy; 14 endings were not seen.
- The review produced ten changes, ranked, each tied to a count.

```viz
{"kind": "compare", "unit": "chats", "max": 31, "rows": [{"label": "Opus", "value": 31, "tone": 3}, {"label": "Fable", "value": 18, "tone": 2}, {"label": "Both", "value": 4, "tone": 4}], "caption": "The 53 chats of the Academy case's review by the model they ran on, read from commit trailers: §6 of this unit, from Academy case file §8. One person's six days; an anecdote, not a benchmark."}
```

**What the example shows about the method.** Four things, each a reading of §8 (stated opinion):

1. **The window had no selection problem.** It was the whole history (§8), so no chat was left out by choice. Your window will rarely be the whole history; §2's third rule is the substitute.
2. **The model was read from a record.** Commit trailers are a record the work produced for another purpose (§8). BW7 §7's run log builds the same habit on purpose. The model column covers all 53 chats: 31 + 18 + 4 = 53 (arithmetic).
3. **Outcome was the weakest label.** "Accepted" was a proxy and 14 of 53 endings were not seen (§8): about one chat in four (14 ÷ 53 = 26%, arithmetic). A label that cannot be read for a quarter of the chats can still rank changes, but every outcome-based count carries that gap.
4. **Every change was tied to a count** (§8). That is the ranking rule DD-BW2 Part 2 uses for the record's own changes, and the one §7 asks of yours.

**What it does not show.** The case file holds no breakdown of the 53 chats by task type, outcome or turns, no pattern counts, no rule verdicts, and none of the ten changes (§8). So this unit cannot set the case's list beside yours. What it can set beside your gap report is DD-BW2's case report, line by line (Deliverable, Part B), and DD-BW2's ten changes, the record's own, restated for any project (Deliverable, Part D). Nothing about the review is a benchmark: 53 chats in six days, or 18 on one model, says what one person did in one week of one project; compare your counts only with your own next review.

## 7 · From counts to ten changes

**Ranking.** Use DD-BW2 Part 2's rule: rank by the count behind each change, largest first; a change you cannot tie to a count is not on the list; ties go to the change whose failure reached a finished output (DD-BW2, Deliverable Part 2; stated opinion there) and, where that does not separate them, to the change with more corrections in the chats behind it (this unit's addition, stated opinion). Each change names the unit that teaches it and that unit's grade, as DD-BW2 Part 4's columns ask.

**What a count can carry.** Your window is small. A pattern seen in 2 of 30 chats and one seen in 4 of 30 are not reliably different rates; with counts this size, the ranking says where to look first and nothing about the size of an effect. BW6 §5 gives the arithmetic for what a small sample can and cannot show; apply its rule that a clean sample certifies nothing to a pattern you did not find: no "two tasks" chat in thirty bounds the rate, it does not prove zero (stated opinion, on BW6 §5).

**Three rules for writing a change** (stated opinion):

1. **Say it so next month can check it.** "One task per chat" is a rule; "a new chat for every task type in my routing table, and the 'two tasks' count at zero in the next review" is a change.
2. **Give it a "worked if" line**: the count in the next review that would show it worked.
3. **Reserve the tenth place for the record.** The rules your sheet marked "not testable" and the labels with the most "not recorded" cells are a change of their own: what to start recording so the next review can test them. DD-BW2 Part 4 makes the same reservation for "not recorded" lines.

**Re-run.** Repeat the review after four weeks with the same task types and the same definitions, so the two sheets can be compared column by column. Changing a definition between reviews makes the counts incomparable; if you must, relabel the first window with the new one (stated opinion).

## 8 · On other tools

The method in §2 to §7 (a window, a list, four labels, four patterns, counts tested against rules) needs nothing from a vendor except a way to list your chats, and holds for any assistant. The Claude-specific claims are the export and the Claude Code session list in §2 and the export's contents in §5. The equivalents found on the other vendors' own pages, all read 16 November 2026:

| Claim in this unit | Claude | ChatGPT (OpenAI) | Gemini (Google) |
|---|---|---|---|
| A full export of your chats (§2, §5) | Settings > Privacy > "Export data"; conversations and account data, uploaded files excluded; emailed link expires after 24 hours: [*Export your Claude data*](https://support.claude.com/en/articles/9450526-export-your-claude-data) | Settings > Data Controls > "Export data"; the export includes "your chat history in chat.html"; "The link in the email expires after 24 hours"; the article says it applies to Free and Plus users as of 11 April 2023: [*How do I export my ChatGPT history and data?*](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data) (labelled "Updated over a week ago") | Google Takeout, "My Activity" > "Gemini Apps", which the page describes as "your Gemini chats, generated media, and uploads"; downloading does not delete the data from Google's servers: [*Download your Gemini Apps data*](https://support.google.com/gemini/answer/16920332) |
| A local session list with transcripts and a 30-day default retention (§2) | [*Manage sessions*](https://code.claude.com/docs/en/sessions) | Not checked for this unit | Not checked for this unit |
| Chat search by topic (§2) | BW1 §3, read 15 Nov 2026 | Not checked for this unit (BW1 §10 covers ChatGPT's memory and chat history, not search) | Not checked for this unit (BW1 §10 covers Gemini's reference to past chats, not search) |
| Retention, training and memory settings that govern a chat used for labelling (§5) | BW10 §6, read 16 Nov 2026 | BW10 §9 | BW10 §9 |
| Large-scale classification of chats by task (§1, §2) | Clio, on Claude.ai (Tamkin et al., preprint) | Chatterji et al., on ChatGPT (working paper) | No equivalent read for this unit |

Everything else in this unit (the labels and their limits, the patterns, the rule tests, the ranking, the privacy rules) is a method that needs no product.

## Deliverable · A classification sheet, a gap report, a sixty-minute review, and changes for any project

Four parts. **Part A** is the classification sheet: its label definitions, the sheet on the Academy case as far as the case file holds it, the sheet filled in full on a neutral example whose content is invented and labelled so, and the blank template. **Part B** is the gap report, in the same three forms, set beside DD-BW2's case report line by line. **Part C** is the review as a sixty-minute procedure. **Part D** restates, for any project, the ten changes the Academy record supports, and says why the case's own review list is not among them. Product facts as read 16 November 2026; re-read the export and session pages on the day you run the review.

### Part A · The classification sheet

**The definitions, written once at the top of the sheet** (from §2; stated opinion):

| Column | Value | Defined as |
|---|---|---|
| # | 1, 2, 3 … | The chat's number in order of its first message |
| Date | Day | The date of the first message |
| Task type | One of your five to nine types, or "other" | The artefact the first ask produces, named as in your BW2 routing table |
| Model | The model, or "not recorded" | What ran, read from a record; "A → B" for a switch |
| Effort | The level, or "not recorded" | As set, read from a record |
| Outcome | Used as is · used after edits · redone · abandoned · not seen | What happened to the output; "not seen" when the record does not show it |
| My messages | Count | Your messages in the chat, the first included |
| Corrections | Count | Your messages that fix, reject or narrow an output |
| Two tasks | The second task's type, or blank | A later ask in the chat of another task type |
| Routing | Yes or blank | Model or effort differs from your routing table's row for the task type |
| Procedure | Yes or blank, with which | A procedure typed again, or an expected skill that did not load |
| Repeat research | The number of the earlier chat, or blank | The chat researched a question an earlier chat in the window answered |
| Other marks | Free text, a few words | Any rule-test mark from §4 (a file pasted twice, no check named, a check in the writing chat) |

**On the Academy case.** The case file holds the review's totals, not its rows (Academy case file §8):

| Column | Academy case (anecdote) |
|---|---|
| Window | Six days; the project's whole history at the time |
| Chats | 53 |
| Task type | Labelled by hand; counts by type not in the case file |
| Model | Read from commit trailers: Opus 31, Fable 18, both 4 |
| Effort | Not among the review's labels |
| Outcome | "Accepted", a proxy; 14 of 53 endings not seen |
| My messages, corrections | Turns counted; counts not in the case file |
| Extra columns | Not in the case file |

**On a neutral example** (neutral example, invented). An analyst writing a quarterly market report reviews two weeks of chats, sixteen in all. Their routing table, built from BW2's template, puts extraction, summaries and code changes on the mid tier and drafts, critiques and research on the large tier; they have one skill, for extraction. Every row below is invented to show the sheet at work; none is evidence.

| # | Date | Task type | Model | Effort | Outcome | My msgs | Corr. | Two tasks | Routing | Procedure | Repeat research | Other marks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | W1 Mon | Research with search | large | not recorded | used after edits | 3 | 1 | | | | | no check named |
| 2 | W1 Mon | Summary | large | not recorded | used as is | 1 | 0 | | yes | | | |
| 3 | W1 Tue | Long draft | large | not recorded | used after edits | 6 | 3 | Summary | | | | data file pasted twice |
| 4 | W1 Tue | Extraction | mid | not recorded | redone | 4 | 3 | | | skill did not load | | |
| 5 | W1 Wed | Extraction | large | not recorded | used as is | 2 | 0 | | yes | | | |
| 6 | W1 Wed | Critique | large | not recorded | used after edits | 2 | 0 | | | | | fresh chat |
| 7 | W1 Thu | Research with search | large | not recorded | used after edits | 2 | 0 | | | | 1 | |
| 8 | W1 Fri | Summary | large | not recorded | used as is | 1 | 0 | | yes | | | |
| 9 | W2 Mon | Long draft | large | not recorded | abandoned | 5 | 4 | Critique | | | | check in the writing chat |
| 10 | W2 Mon | Extraction | mid | not recorded | used as is | 3 | 1 | | | skill did not load | | |
| 11 | W2 Tue | Code change | mid | not recorded | used as is | 2 | 1 | | | | | |
| 12 | W2 Wed | Critique | large | not recorded | used after edits | 2 | 0 | | | | | fresh chat |
| 13 | W2 Wed | Research with search | large | not recorded | not seen | 1 | 0 | | | | | no check named |
| 14 | W2 Thu | Summary | large | not recorded | used as is | 1 | 0 | | yes | | | |
| 15 | W2 Thu | Long draft | large | not recorded | used after edits | 4 | 2 | | | | | data file pasted twice |
| 16 | W2 Fri | Extraction | large | not recorded | used as is | 2 | 0 | | yes | skill did not load | | |

**Tallies** (arithmetic on the invented rows): task types: extraction 4, research 3, summary 3, long draft 3, critique 2, code change 1 (16). Model: large 13, mid 3; no switches; effort not recorded in 16 of 16. Outcome: used as is 7, used after edits 6, redone 1, abandoned 1, not seen 1. My messages: 41 in all, median 2. Corrections: 15 in all; 4 chats with two or more (3, 4, 9, 15) hold 12 of the 15. Two tasks: 2. Routing: 5. Skill expected in 4 extraction chats, loaded in 1. Repeat research: 1 question. Relabel check: chats 2, 6, 9, 11 and 14, drawn by number, got the same task type on relabelling, 5 of 5.

**Template.** Copy the definitions table above to the top of your sheet, then one row per chat:

| # | Date | Task type | Model | Effort | Outcome | My msgs | Corr. | Two tasks | Routing | Procedure | Repeat research | Other marks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [*1, in order of first message*] | [*date of the first message*] | [*one of your types, defined at the top*] | [*the model that ran, from a record; "not recorded" if none*] | [*the level, from a record; "not recorded" if none*] | [*one of the five values*] | [*your messages, the first included*] | [*your messages that fix, reject or narrow*] | [*the second task's type, or blank*] | [*yes if the model or effort differs from your routing row*] | [*the procedure retyped, or the skill that did not load*] | [*the number of the earlier chat that answered it*] | [*a §4 mark in a few words; no names, no quotations*] |

Under the rows: **Tallies** [*counts per column, as in the example*]; **Relabel check** [*the five chats drawn by number, and how many kept their label*]; **Window** [*first and last date; whole history, or the share of chats sampled and how they were drawn*].

### Part B · The gap report

Five sections. Section 1 sets your record beside DD-BW2's case report (Deliverable Part 1) line by line; Section 4 uses DD-BW2 Part 4's form for the ranked changes, with a "worked if" column added (§7).

**On the Academy case** (Academy case file §8; anecdote). The case file holds what follows, and no more.

1. **Record.** Window: six days, the project's whole history at the time. Chats: 53. By model: Opus 31, Fable 18, both 4, from commit trailers. By task type, by outcome, by turns: labelled by hand, counts not in the case file. Outcome: a proxy; 14 of 53 endings not seen. *Beside DD-BW2 Part 1:* line H ("53 chats in six days at the review: 31 Opus, 18 Fable, 4 both") holds the same counts; line B records effort as not recorded (case file §9).
2. **Patterns.** Not in the case file.
3. **Rule tests.** Not in the case file.
4. **Ten changes.** Ten, ranked, each tied to a count; the list is not in the case file.
5. **Privacy.** The case file records the review as counts and a description of its method, with no chat quoted; the file was compiled "with private details removed" (header).

**On the neutral example** (neutral example, invented).

**Gap report · two weeks, 16 chats · compiled at the end of week 2.** One person's record; an anecdote, compared only with their own next review.

**1 · Record**

| Line | Value | Beside DD-BW2 Part 1 |
|---|---|---|
| Window | Two weeks; every chat in it | A: period |
| Chats, by task type | 16: extraction 4, research 3, summary 3, long draft 3, critique 2, code change 1 | A: outputs |
| By model | Large 13, mid 3; no switches | B: writer model; H: chats by model |
| Effort | Not recorded, 16 of 16 | B: effort |
| Outcome | Used as is 7, after edits 6, redone 1, abandoned 1, not seen 1 | No line; nearest is C, the check |
| Messages and corrections | 41 messages, median 2 a chat; 15 corrections, 12 of them in 4 chats | H: cost |
| Not recorded | Effort and start time, 16 of 16 chats | I: limits |

**2 · Patterns**

| Pattern | Count | Chats | Unit with the fix |
|---|---|---|---|
| Badly put: chats with two or more corrections | 4 chats, 12 of 15 corrections | 3, 4, 9, 15 | BW3 §3, §6 |
| Badly put: two tasks in one chat | 2 | 3, 9 | BW3 §6 |
| Wrong tool: off the routing table | 5 | 2, 5, 8, 14, 16 | BW2 Deliverable |
| By hand: extraction skill did not load | 3 of 4 extraction chats | 4, 10, 16 | BW8 §3, §4 |
| Paid twice: question researched again | 1 question | 7 (repeats 1) | BW10 rule 6 |

**3 · Rule tests** (verdicts from §4; grades as BW10 and DD-BW1 give them)

| Rule | Verdict | Rule | Verdict |
|---|---|---|---|
| BW10 1 | Broken, 2 (chats 3, 9) | DD-BW1 1 | Broken, 2 (chats 1, 13) |
| BW10 2 | Not testable: no times recorded | DD-BW1 2 | Not marked on this sheet |
| BW10 3 | Model kept; effort not recorded | DD-BW1 3 | Broken, 1 (chat 9); kept in chats 6, 12 |
| BW10 4 | Broken, 2 (chats 3, 15) | DD-BW1 4 | Not testable |
| BW10 5 | Not counted | DD-BW1 5 | Broken, 2 (chats 3, 9) |
| BW10 6 | Broken, 1 (chat 7) | DD-BW1 6 | Kept: research ran only on research tasks |
| BW10 7 | Not testable | DD-BW1 7 | Did not arise |
| BW10 8 | Not testable: the list shows no project | DD-BW1 8 | Broken, 1 (chat 7; as BW10 6) |
| BW10 9 | Did not arise | DD-BW1 9 | Not testable |
| BW10 10 | Not testable | DD-BW1 10 | First half kept; effort not recorded |
| BW10 11 | Not testable | | |
| BW10 12 | Not testable | | |

**4 · Changes, ranked** (DD-BW2 Part 2's rule: the count behind each, largest first; ties to the change whose failure reached a finished output, then to the one with more corrections in the chats behind it, this unit's addition; a count of one is a flag)

| # | Change | Count behind it | Unit that teaches it | Grade of the rule | Worked if, at the next review |
|---|---|---|---|---|---|
| 1 | Open summaries and extractions on the mid tier my routing table names, and write the tier in the brief's first line | 5 of 16 chats off the table (Section 2) | BW2, Deliverable Part 1 | Graded row by row in BW2 Part 1 (vendor documentation and benchmarks); its escalation rule documented practice | Routing column at 0 |
| 2 | Rewrite my long-draft brief from BW3's template 2, with an output contract and done-when lines | 4 chats hold 12 of 15 corrections; 3 of the 4 are long drafts | BW3 §3; Deliverable, template 2 | Documented practice, vendor (BW3 §3) | No long-draft chat with more than one correction |
| 3 | Rewrite the extraction skill's description, add chats 4, 10 and 16 as should-trigger rows to its test set, and rerun the test | Skill loaded in 1 of 4 chats that needed it | BW8 §3, §4 | Documented practice (BW8 §4) | Skill loads in every extraction chat |
| 4 | One task type per chat; a second task opens a new chat | 2 chats, 7 corrections between them | BW3 §6; BW10 rule 1 | Documented practice | Two-tasks column at 0 |
| 5 | Keep the data file where the chat reads it by name, once | 2 chats, 5 corrections between them | BW10 rule 4 | Documented practice | No file pasted twice |
| 6 | End every research brief with its check: the sources to open and the sample to draw | 2 chats, 1 correction between them | DD-BW1 rule 1; BW6 §5 | Stated opinion; one supporting mechanism measured on GPT-4 in 2023 | Every research chat names its check |
| 7 | None: no other pattern has a count of two | | | | |
| 8 | None | | | | |
| 9 | None | | | | |
| 10 | Log model, effort and start time for every chat in one line | Effort and time missing in 16 of 16 chats | BW7 §7 | Stated opinion (BW7 §7) | BW10 rules 2 and 3 testable |

*Flagged, not ranked (count of one):* one question researched twice (chat 7; BW10 rule 6); one critique asked in the writing chat (chat 9; DD-BW1 rule 3); one outcome not seen (chat 13).

**5 · Privacy.** Export deleted after labelling; the sheet holds no names and no quotations; the patterns are described by kind.

**Template.**

**[Your project] · gap report · [first date] to [last date], [n] chats · compiled [date].** One person's record; compared only with your own next review.

**1 · Record**

| Line | Value | Beside DD-BW2 Part 1 (or your own Part 3) |
|---|---|---|
| Window | [*dates; whole history, or the sample and how it was drawn*] | A: period |
| Chats, by task type | [*total, then the count per type*] | A: outputs |
| By model | [*count per model, and the switches*] | B; H |
| Effort | [*count per level, or "not recorded, n of n"*] | B |
| Outcome | [*count per value; "not seen" kept as its own count*] | No line; nearest is C |
| Messages and corrections | [*total and median messages; total corrections, and the share in the chats with two or more*] | H |
| Not recorded | [*each label or rule your record could not show, with its count*] | I |

**2 · Patterns**

| Pattern | Count | Chats | Unit with the fix |
|---|---|---|---|
| Badly put | [*chats with two or more corrections, and their share of all corrections; chats with two tasks*] | [*their numbers*] | [*BW3 section*] |
| Wrong tool | [*chats off your routing table, by task type*] | [*numbers*] | [*BW2 row*] |
| By hand | [*procedures typed three or more times; skill loads against chats that needed the skill*] | [*numbers*] | [*BW8 §4 or §7*] |
| Paid twice | [*questions researched in more than one chat*] | [*numbers*] | [*BW10 rule 6*] |

**3 · Rule tests.** [*BW10 rules 1 to 12 and DD-BW1 rules 1 to 10, each with one verdict from §4: kept, broken n (with the chats), did not arise, not testable; keep each rule's grade from its own table*]

**4 · Changes, ranked**

| # | Change | Count behind it | Unit that teaches it | Grade of the rule | Worked if, at the next review |
|---|---|---|---|---|---|
| 1 to 9 | [*the change, written so next month can check it*] | [*the count, and the Section 2 or 3 line it comes from; a count of one goes under "Flagged"*] | [*unit and section*] | [*as that unit grades it*] | [*the count at the next review that shows it worked*] |
| 10 | [*what to start recording, from Section 1's "not recorded" line*] | [*the number of cells it would fill*] | [*BW7 §7, or the unit for that field*] | [*as that unit grades it*] | [*the rules that become testable*] |

*Flagged, not ranked:* [*each pattern with a count of one, with its chat and rule*]

**5 · Privacy.** [*export deleted on (date); sheet checked for names and quotations; who, if anyone, has seen this report*]

### Part C · The review in sixty minutes

**The day before (not counted).** Request the export on claude.ai (Settings > Privacy > "Export data"); the link comes by email and expires 24 hours after it is created (vendor, read 16 Nov 2026). For Claude Code, nothing to request: open `/resume`, and widen with `Ctrl+A`. Have your BW2 routing table, BW10's Deliverable Part 1 and DD-BW1's Deliverable Part 2 open.

| Minutes | Step | Done when |
|---|---|---|
| 0–5 | **Set up.** Choose the window by §2's rules. Copy Part A's definitions to the top of a new sheet. Write your task types, one line each, from your routing table. | The window's dates and the task types are written down |
| 5–35 | **List and label.** One row per chat, oldest first: date, task type, model, effort, outcome, messages, corrections, then the four extra columns and any §4 mark. Thirty seconds to a minute a chat (an estimate); at more than thirty chats, keep to thirty seconds. Write "not recorded" or "not seen" rather than guess. At more than about sixty chats, draw a sample by number instead and record that you did. | Every chat in the window has a row; both ends of the list checked |
| 35–38 | **Relabel check.** Draw five chats by number, cover their task type, label them again, count matches. | The match count is written under the sheet |
| 38–45 | **Tally.** Count each column; find the chats with two or more corrections and their share of all corrections. Fill gap-report Sections 1 and 2. | Sections 1 and 2 have a number in every cell or "not recorded" |
| 45–50 | **Test the rules.** For each of BW10's twelve and DD-BW1's ten, one verdict from §4. Fill Section 3. | 22 verdicts |
| 50–57 | **Rank.** Each pattern or broken rule with a count of two or more becomes a change; rank by count, largest first; write each with its unit, grade and "worked if". Put the record change tenth. Counts of one go under "Flagged". | Section 4 filled; each change checkable next month |
| 57–60 | **Close.** Delete the export. Read the sheet once for names and quotations, and remove them. Put the next review's date in your calendar, four weeks out, with the same task types. | Section 5 filled; the next date set |

```viz
{"kind": "flow", "steps": [{"label": "Set up", "note": "0–5 min"}, {"label": "List and label", "note": "5–35 min"}, {"label": "Relabel check", "note": "35–38 min"}, {"label": "Tally", "note": "38–45 min"}, {"label": "Test the rules", "note": "45–50 min"}, {"label": "Rank", "note": "50–57 min"}, {"label": "Close", "note": "57–60 min"}], "caption": "The review as a sixty-minute procedure, the table in Part C of this unit's Deliverable. The minutes are this unit's allocation (stated opinion), not a measure."}
```

### Part D · Changes for any project

The case's review produced ten ranked changes (Academy case file §8), but the case file does not hold them, so they cannot be restated here. What the case does hold, in a filed unit of this course, is the ten changes its project record supports (DD-BW2, Deliverable Part 2), ranked by the same rule. Below, each is restated for any project, with the count on your own sheet or records that would put it on your list. They come from the case's project records (its checks, audits and failures); none comes from its chats. The grade is the one DD-BW2 gives, and the case adds nothing to it.

| # | Change, for any project | It belongs on your list when | Unit that teaches it | Grade, as DD-BW2 Part 2 gives it |
|---|---|---|---|---|
| 1 | Check every output that matters in a context that did not write it, and record for each output whether it was checked, by which model, with what result | Your sheet shows checks asked for in the writing chat, or outputs used with no check | BW6 §4; BW2 §5 | Stated opinion on measured self-preference evidence (BW2 §5); documented practice, vendor (BW6 §4; DD-BW1 rule 3) |
| 2 | Put "qualifiers and figures the source does not carry" first in every checking brief, and have the checker quote the source's sentence beside each claim it passes | Your checks find claims stretched beyond their source | BW6 §2, §3 | Stated opinion, built on measured citation-error studies (BW6 §2) |
| 3 | When one fact turns out stale, re-check every fact read from the same page or version, across everything you produced from it | A stale fact appears in your record | BW6 §5; BW1 §4 | Stated opinion (BW6 §5) |
| 4 | Record what happens to each finding of a check: applied, applied as corrected, rejected, with the reason | Your record cannot say how many findings were wrong | BW6 §6 | Stated opinion, built on vendor guidance (BW6 §4, §6) |
| 5 | Check every chart, table or figure against the text it draws from before handing in, and fix it until it passes | A drawn or computed part of your output carried a number the text did not | BW7 §6; the course's shared preamble | Stated opinion, adapted from documented practice (BW7 §6) |
| 6 | Hand work between steps as files, so a lost session loses nothing | Your record shows a session or result lost, or a result that reached a file only by copying from a chat | BW7 §2; BW9 §9 | Stated opinion, on measured and vendor sources (BW7 §2) |
| 7 | Check that each deliverable exists and meets its done-when lines before anything is built on it | Your sheet shows outputs redone because a part was missing | BW5, Deliverable 1d; BW3 | Documented practice (DD-BW1 rule 2) |
| 8 | Log the model and version that actually ran, and keep what each run read | Your model column has "not recorded" cells, or what ran differed from what you chose | BW7 §7; BW2 §7 | Stated opinion (BW7 §7) |
| 9 | Run a script that checks published output for private terms before every publish | Anything you publish is built from material that holds private terms | BW4 §7; BW10 §7 | Stated opinion (BW4 §7) |
| 10 | Record hours and usage per output, so every other change can be weighed against its cost | Your gap report's "not recorded" line includes time or usage | BW10 §1, §4; BW7 §7 | Stated opinion (DD-BW2), on BW10 §1 |

How the two lists meet: Part B's ranked changes come from your chats, Part D's from a project's record of its outputs. Where one change appears in both, as a record change does in the neutral example (Part B's tenth; Part D's eighth), rank it by the count on your own sheet, the only count about your work.

## Sources

Web sources read on 16 November 2026 at the address a search returned; product facts carry that date.

- Claude Help Center. *Export your Claude data*. Labelled "Updated this week" (vendor). https://support.claude.com/en/articles/9450526-export-your-claude-data
- Anthropic. *Manage sessions*. Claude Code documentation (vendor). https://code.claude.com/docs/en/sessions
- OpenAI Help Center. *How do I export my ChatGPT history and data?* Labelled "Updated over a week ago" (vendor). https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data
- Google. *Download your Gemini Apps data*. Gemini Apps Help (vendor). https://support.google.com/gemini/answer/16920332
- Tamkin, A., McCain, M., Handa, K., Durmus, E., Lovitt, L., Rathi, A. and colleagues. *Clio: Privacy-Preserving Insights into Real-World AI Use*. arXiv:2412.13678, 18 December 2024 (preprint; authors at Anthropic). https://arxiv.org/html/2412.13678v1
- Chatterji, A., Cunningham, T., Deming, D. J., Hitzig, Z., Ong, C., Shan, C. Y. and Wadman, K. *How People Use ChatGPT*. NBER Working Paper 34255, September 2025 (working paper). https://www.nber.org/papers/w34255
- Harkin, B., Webb, T., Chang, B. and colleagues. *Does Monitoring Goal Progress Promote Goal Attainment? A Meta-Analysis of the Experimental Evidence*. *Psychological Bulletin* 142(2), 2016, 198–229 (peer-reviewed; read at the repository record). https://eprints.whiterose.ac.uk/91437/
- Academy case file (`generator/data/building-with-ai/case-academy.md`), compiled 11 Nov 2026 with notes of 15 and 16 Nov 2026: header, §1, §2, §7, §8, §9.
- Units of this course, pointed to by section: BW1 (§3, §4, §10), BW2 (§1, §5, §7; Deliverable), BW3 (§3, §6; Deliverable, template 2), BW4 (§7), BW5 (Deliverable 1d), BW6 (§2 to §6), BW7 (§2, §6, §7), BW8 (§3, §4, §7), BW9 (§9), BW10 (§1, §4, §6 to §9; Deliverable Part 1 and Template D), DD-BW1 (Deliverable Part 2), DD-BW2 (§10; Deliverable Parts 1 to 4).

## Unsure list

1. §2, §8: *Export your Claude data* does not say what file format the export uses; the unit says so and claims no format.
2. §8: *How do I export my ChatGPT history and data?* says it applies to Free and Plus users "as of April 11, 2023"; whether the same path holds on other current ChatGPT plans was not checked.
3. §8: *Download your Gemini Apps data* does not say whether Gemini Apps Activity must be on for chats to be exported, or how work and school accounts differ; the unit claims neither.
4. §1: Harkin et al. (2016) was read at its White Rose repository record (title, journal, 138 studies, N = 19,951, d+ = 0.40, moderators), not in the full article; the moderator wording ("physically recorded", "reported or made public") is paraphrased from that record.
5. §1, §5: Chatterji et al.'s figures ("nearly 80%", 53% to more than 70%) and "privacy-preserving automated pipeline" come from the NBER abstract page; the full paper was not read, and the authors' affiliations were not checked (the unit names no affiliation).
6. §1, §2, §5: Clio's one million conversations, the turns facet, the 94% reconstruction on a synthetic dataset, the cluster thresholds and "without the need for human reviewers to read raw conversations" were read in the arXiv v1 HTML (first 100,000 of about 190,000 characters); later versions were not checked.
7. §2: the 30-day default retention of Claude Code transcripts and the picker's row contents are as *Manage sessions* read on 16 Nov 2026; the page describes the CLI only, and the desktop app, claude.ai/code and VS Code lists were not read.
8. §2, Part C: thirty seconds to a minute a chat, and the minute allocation of the sixty-minute procedure, are this unit's estimates; no source measures labelling time.
9. §2, §6: case file §8 says each ask was classified and gives "number of turns" without defining turn or ask; the unit's sheet (one row per chat, own messages and corrections counted) is its own definition and is not presented as the case's.
10. Part D: the restated changes and their grades are copied from DD-BW2 Deliverable Part 2 as filed (corrected 16 Nov 2026); if a later correction changes that table's grades, Part D must follow.
Object: none

Fresh check 2026-11-16 (Opus 5.5): fix · 1 errors, 4 should-fix, 9 minor; report `audits/building-with-ai/fresh-check-DD-BW3.md`

Correction 16 Nov 2026, found by DD-BW3's filer (flag F123, as F52, F98 and F112): §1 now describes the case in the case file's own wording; corrections check `audits/building-with-ai/corrections-2026-11-16-DD-BW3-r2-DD-BW3.md`.
