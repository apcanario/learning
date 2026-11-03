---
code: DD-B2
title: Deep dive: his unknown unknowns
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-11-02
search: off
---

# DD-B2 · Deep dive: his unknown unknowns

## 1 · Method, and what it cannot see

**The evidence is this Project's own chat history, read through three past-chat tools.** `recent_chats` lists chats by when they were last updated, with each chat's title, its first message, a stretch of its opening or closing turns and, for some chats, a summary. `conversation_search` finds a spot by topic, across the Project or inside one chat. `read_conversation` opens one chat at a spot and returns a few turns with the chat's total turn count. The tools see only chats in this Project. Nothing else was used: no usage page, no settings screen, no repository. Every count below comes from a script (`count.py` and `count2.py`, run over a working table of the chats typed from the tool results) and says what it is over. The working files are not published.

**The brief asked for "by Fable"; the course owner set that aside on 31 October 2026 and ran every row of stages 1 to 4 on Opus 5.5, DD-B2 included, with a Fable 5.1 fresh check and the final audit (Audit 6) owed to the later Fable stage; the chat history stays the evidence because the brief's point is a reading of what he did, which the past-chat tools give any model.** The evidence was gathered across two agent runs before this one, the first lost to a container restart; the second run's working files were taken over, its count script re-run and its figures checked against those files, two model fields corrected from commit trailers in its saved reads, and a few more spots opened where a count needed it.

**The window holds six days.** The brief asks for 4 August to 2 November 2026. Listing backwards from 2 November, the list stops at a chat whose first message was sent at 05:42 on 28 October; a further call for anything updated before that returned nothing, and a call for anything after 17:00 on 2 November returned only the last chat already listed. Three listing calls (20, 20 and 13 chats; the second run's) covered the window, and two more in this run found nothing outside it. So the list is complete for the Project, and the Project's history in the window is **53 chats, first message 28 October 05:42 to last update 2 November 17:51 (local time)**. Work done before 28 October, including the history courses' writing, is not in these tools' reach. Every rate in this unit is a six-day rate, from a week of heavy building, and none should be read as a habit over a season.

**What was read, and what was inferred.**

| Field | How it was obtained | Coverage |
|---|---|---|
| Date, first message | Listing (first human message, with its timestamp) | 53 of 53 |
| Task type | Read from the first message and the visible turns, labelled by hand into seven types | 53 of 53 |
| Turns | The total turn count the tools report | 53 of 53 |
| Model | Read only: a commit trailer naming the model, the ask itself naming it, or the filed unit's front matter; never guessed | 53 of 53 (a search inside each chat for its commit trailers, with the saved reads) |
| Effort | Nothing in the history records it | 0 of 53 |
| Outcome | The last visible reply reports the row done, or the unit is in the vault | 39 of 53; 14 "not read" |
| Opened beyond the listing | `read_conversation` on 16 chats (the first nine in time and seven later ones picked because a count needed them); search hits inside 7 more | 23 of 53 |

The 16 chats opened are not a random sample: they are the early chats, where whole asks were visible, plus chats opened to settle one field. For the 30 neither opened nor searched, every field comes from the listing's title, first message and snippet, and for 19 chats in all from the tool's summary. A **turn** is one message on either side; a two-turn chat is one ask and one answer. In a chat that runs agents, each agent's completion notice arrives as a turn, so a high turn count there measures agent traffic, not his messages: chat 39 reports 134 turns with one visible message from him. **Accepted** cannot be read: the history records no verdict of his. The proxy is that a unit was filed (7 chats) or that the chat's last reply reports its row done and no later message from him in it corrects it (32 chats); 14 chats' endings were not seen. Of the 12 follow-up messages from him visible across all chats, one redirects the order of work (site rows before units) and none rejects an output.

## 2 · What he asked for, on what, and how it went

**Seven task types.** Unit writing (Brand + AI and User Experience units, and orchestrator chats whose agents write them) 15 chats; infrastructure (the Academy build, the repository, publishing, the method and skill files) 15; figure passes 7; audits and fresh checks 6; status questions 6; syllabus design 2; history-module writing 2 (`count.py`, over 53 chats).

```viz
{"kind": "compare", "unit": "", "max": 15, "rows": [{"label": "Unit writing", "value": 15, "tone": 3}, {"label": "Infrastructure", "value": 15, "tone": 4}, {"label": "Figure passes", "value": 7, "tone": 4}, {"label": "Audits and fresh checks", "value": 6, "tone": 2}, {"label": "Status questions", "value": 6, "tone": 5}, {"label": "Syllabus design", "value": 2, "tone": 5}, {"label": "History-module writing", "value": 2, "tone": 3}], "caption": "Chats by task type, 28 October to 2 November 2026. §2 of this unit; the writer's tally (count.py) over the Project's 53 chats, task type labelled by hand from each chat's first message and visible turns."}
```

**Models.** Of the 53 chats, 31 show Opus 5.5, 18 Fable 5.1 and four both (an Opus trailer and a Fable one: chats 24, 43, 48 and 52); a search inside each chat for its commit trailers, with the trailers in the saved reads, finds a model for all 53. None ran on Sonnet 5.5 or Haiku 5.5 (0 of 53). Effort is recorded in none.

| Task type | Opus 5.5 | Fable 5.1 | Switched | Median turns |
|---|---|---|---|---|---|
| Unit writing (15) | 14 | 0 | 1 | 12 |
| Infrastructure (15) | 5 | 8 | 2 | 8 |
| Figure passes (7) | 6 | 1 | 0 | 33 |
| Audits (6) | 1 | 5 | 0 | 2.5 |
| Status (6) | 3 | 2 | 1 | 10 |
| Syllabus (2) | 0 | 2 | 0 | 10 |
| History writing (2) | 2 | 0 | 0 | 50.5 |

*(`count.py` crosstab and median turns by task, over 53 chats; model read from the commit trailers a search inside each chat returns and those in the saved reads; a chat with trailers of both models counts as switched.)*

```viz
{"kind": "bars", "mode": "stacked", "unit": "", "series": [{"name": "Opus 5.5", "tone": 3}, {"name": "Fable 5.1", "tone": 2}, {"name": "Switched", "tone": 4}], "rows": [{"label": "Unit writing", "values": [14, 0, 1]}, {"label": "Infrastructure", "values": [5, 8, 2]}, {"label": "Figure passes", "values": [6, 1, 0]}, {"label": "Audits", "values": [1, 5, 0]}, {"label": "Status", "values": [3, 2, 1]}, {"label": "Syllabus", "values": [0, 2, 0]}, {"label": "History writing", "values": [2, 0, 0]}], "caption": "The model each chat ran on, by task type. §2 of this unit; the tally over 53 chats, model read from the commit trailers a search inside each chat returns and those in the saved reads; a chat with both models' trailers counts as switched."}
```

**Turns.** 872 turns in all; median 8, from 2 to 134. Eleven chats took two turns, one ask and one usable answer: four unit drafts (B1, A9, A6, B2), three fresh checks or audits, four infrastructure rows. Ten took 30 turns or more, and seven of those ten ran agents or are history writing; the figure passes' median is 33 (`count.py`, over 53 chats).

**How long chats stayed open.** From first message to last update, the median chat was open 0.9 hours; nine were open three hours or more, the longest 20.2 hours (a unit-writing orchestrator, 43 turns), then 9.9 hours (a figure pass, 40 turns) and 8.6 hours (three units by agents, 20 turns) (`count2.py`, over 53 chats; open time is not active time).

**What the record of first drafts adds.** Twenty of the 21 filed units carry a fresh-check record (B1 has none). Fifteen of those twenty had at least one finding of error severity at their first fresh check. Fable 5.1 ran 11 of the checks and found an error in 9; Opus 5.5 ran 9 and found an error in 6. All nine Opus checks are dated 2 November 2026 and say a Fable 5.1 check is owed (`count.py`, over the vault's fresh-check lines). That updates B6 §2's count (eleven of fourteen) with six more units, and keeps its conclusion: a careful first draft is rarely clean.

## 3 · Where he asked badly

**Terse asks that named a code, and codes that collided.** Six asks were one line naming a row ("Execute" and a code), all in the first 33 chats. Two of them named a code that meant two things. In chat 23 (28 Oct), "A4" was both a Brand + AI unit and an Academy-lane row; the model ran the Academy row and said that if he meant the unit, it gets its own chat. In chat 27 (28–29 Oct), "B1, B2 and B3" were backlog rows B-1 to B-3, which were units B3, B4 and A1: three units in one chat, by agents, after which the one-chat-per-unit rule was rewritten (P31) to allow it. The backlog now names rows with a hyphen (B-13, A-5), which keeps them apart from unit codes. **Already fixed:** asks that were terse or opened with a status question number 11 in chats 1 to 33 and none in chats 34 to 53, where every ask is a full specification or a pasted prompt (`count2.py`).

**Asking "what's next" in the chat that then does the work.** Five chats opened with a status question (median 10 turns); in two of them the answer turned into work in the same chat, one on a three-word "do it here". DD-B3 rule 6 and B8 rule 12 put one task in a chat. The last status-opened chat began on 29 October at 17:43 (`count.py`); after it, chats end by writing the paste-ready prompt for the next row into the backlog and the reply; 13 chats' listing blocks carry such a prompt (`count2.py`, listing blocks). The habit has already changed.

**Several rows in one ask.** Sixteen asks name two or more backlog rows; their chats' median is 11.5 turns, against 8 for the 31 chats that name one (`count.py`; correlational, small numbers, and multi-row chats are also the agent chats, so the turn gap is partly agent notices). Since P31, several units in one chat are allowed when each is written by a fresh agent; the asks that bundle a unit with unrelated infrastructure rows (a renderer fix, a skill change, a site layout) are the ones B8 rule 12 still argues against.

**Model and effort never stated as effort.** The model can be read in all 53 chats, from commit trailers found by searching inside each; effort in none. No ask contains "think hard" or a similar phrase, so DD-B3 rule 10's first half holds; its second half, effort set in the menu, cannot be checked because nothing records the setting. B2's routing table gives an effort for every row and B8 rule 11 sets both before the first message. Without a record, a later audit cannot tell whether the table was followed.

**What the asks did well.** Eight of the 17 asks visible at length (1,000 characters or more) set the build's pass line, `verify.py` "ALL CHECKS PASSED", as the test of done: DD-B3 rule 2, a criterion a stranger could check. Four figure-chat asks give the agents an attempt cap ("fails twice" and the figure is dropped): DD-B1 rule 25. The adder agents' brief in chat 39, opened at a search hit, names the three files the agent may read, says it may read nothing else, states the rules and asks for a reply under 120 words: DD-B1 rule 26, a subagent brief complete because it cannot ask (`count2.py`; search inside chat 39).

**Restating the procedure in every prompt.** Thirteen of the 16 row asks read in full restate the publish procedure step by step: read the artifact, publish once with its url, the files list, then `deploy.sh`; seven of the asks visible at length carry the words "publish once". Those quoted in the listing (chats 36, 39, 45 and 49 among them) also say "End per `docs/method.md` §8", which already holds the closing steps (`count.py`, `count2.py`, listing snippets). Each copy is about a paragraph of every 4,000-character prompt, and each copy can drift from the others and from the method, the failure B4 F7 found in the project instructions.

## 4 · Where the tool was wrong for the job

**Fable 5.1 spent on infrastructure.** Twenty-two chats ran on Fable 5.1 in whole or part. Five were audits or fresh checks; the other seventeen were infrastructure (10, counting two switches), three status questions (one a switch), two syllabus chats, a figure pass and a unit-writing orchestrator (a switch) (a search inside each chat for its commit trailers, with the saved reads). Eighteen of the 22 began on 28 October; one began on 29 October, two on 1 November and one on 2 November, none on 30 October. B2's routing table gives Fable one row, audits, because a model other than the writer's counters self-preference and because "On Pro every Fable run is billed in usage credits at API rates; on Max it competes for half the weekly limit" (B2 Deliverable; B8 §1 re-read the plans on 2 November 2026). The sequence the history shows: an ask confirmed on 29 October for an overnight figure pass (sent on 30 October, chat 36) records that he is low on Fable and moves the Fable check to a later row; the Fable work was deferred to one row (P49); and the nine fresh checks run on 2 November all ran on Opus with a Fable check owed (§2). The history gives the order of events and no measured cause: it shows no usage figures, and B8 §1 says no page publishes how many tokens a window holds.

```viz
{"kind": "compare", "unit": "", "max": 18, "rows": [{"label": "28 Oct", "value": 18, "tone": 2}, {"label": "29 Oct", "value": 1, "tone": 2}, {"label": "30 Oct", "value": 0, "tone": 2}, {"label": "1 Nov", "value": 2, "tone": 2}, {"label": "2 Nov", "value": 1, "tone": 2}], "caption": "Chats run on Fable 5.1, in whole or part, by the day they began. §4 of this unit; the 22 Fable chats among the Project's 53, model read from the commit trailers a search inside each chat returns and those in the saved reads."}
```

**No routing row for most of the work.** Thirty of the 53 chats are of task types B2's routing table has no row for: infrastructure 15, figure passes 7, status 6, syllabus 2 (`count.py`). B2 was written for his recurring brand tasks (journal entries, units, audits, messages, posts) and says of code only that "For his generator scripts and parsers, Sonnet is enough on this evidence" (B2 §8, vendor benchmarks). In the history, the infrastructure went to whichever model the chat was opened on: Fable in 8 of 15, Opus in 5, both in 2. One reply, writing the prompt for a skill-and-method row, put in it "Model: any (Fable 5.1 or Sonnet 5.5 is enough; no search)"; no chat that can be read ran on Sonnet. This is the unknown unknown the brief asked for: the routing table looks complete because it covers the brand, and most of the six days went to the machine that publishes it.

**Fan-outs kept on the first model after the check had passed.** DD-B1's decision rule, box 6: "A new loop runs first on Opus 5.5 with its check. It moves to Sonnet 5.5 once the check passes on repeat runs." The figure pass ran over the filed Brand + AI units on 30 October (chat 36), the 59 Rome reports (chat 37) and the 78 Greek reports (chat 39), with an adder, a checker and a re-checker per report. In chat 39 alone the Greek pass ran 78 adders, 78 checkers and 62 re-checkers; 266 figures were proposed, 166 passed the first check, 95 got a fix, 94 of those passed the re-check, and 6 were dropped (search inside chat 39). The agents named in the saved reads ran on Opus: 199 agent calls in chat 40 (a figure chat) and 37 in chat 45 (an infrastructure chat), every one with model "opus" (saved reads of chats 40 and 45). By the Greek pass the same adder-and-checker loop had already run over two sets of reports; box 6 says that is when the workers move to Sonnet with the checker kept, and the drop rate (6 of 266) is the measure to watch when they do.

**Where the routing held.** Audits: five of six ran on Fable, the sixth an Opus orchestrator that ran a Fable agent, median 2.5 turns. Unit writing: 14 of 15 on Opus; the fifteenth (chat 52) carries Opus and Fable trailers. On the rows B2 covers, he followed B2.

## 5 · Where he did by hand what a skill already does

**The closing procedure, typed into every prompt.** B5 §6's test for a skill is four questions: not needed in every chat; more than one sentence of procedure in order; recurring at least weekly the same way; each step checkable by something other than his taste. The publish-and-close sequence passes all four: it is nine ordered steps (build, verify, read the artifact, publish once, deploy, move the row, propose rows, rewrite the Project copies, write the next prompt), 13 of the 16 row asks read in full spell it out within six days, and each step has a check (`verify.py`, the publish result, `gh run`, the diff of the mirrors). A skill named `file-unit` already exists for filing a unit (B5 §3); the infrastructure rows have no equivalent and carry the steps as prose instead.

**The next prompt, written by hand by a model.** Thirteen chats' listing blocks carry a paste-ready prompt for the next row, saved into the backlog (`count2.py`). That is good practice by DD-B3 rule 8 (the vault is the memory), and it is a template filled from the same parts each time: the row, the model, the files, the done test, the closing procedure. A template file in the repository, with the closing procedure kept once in a skill and pointed to, would leave each new prompt with only what is new.

**Pasting what a chat can read by path.** Seven chats on 28 October carried a whole unit pasted into the ask (the five measured run from 49,594 to 53,516 characters); the last began at 07:48 that day, and every later chat clones the repository and reads the files by path (`count.py`). B8 rule 16 says never paste what a chat can read by path, because a paste is re-sent on every later turn. In these seven the cost was smaller than that rule's mechanism suggests: four of them were two-turn chats, so the paste was sent once. The cost that applied was the window: some 50,000 characters of unit beside the method files, which B1 §2's attention mechanism says competes for the model's attention. Already fixed.

**Account memory in a published Project.** In six chats the visible turns show the model calling the memory tool (`count.py`, over the saved reads and snippets). B8 rule 22 says "Use account memory" stays off in the Learning Project, whose output is published, and B4 F13 found account memory flowing into it. Whether the setting is off now cannot be read from the history.

## 6 · Where he paid for research he did not need

**Re-fetching what an audit had just checked.** On the morning of 28 October, Audit 1 (chat 2) opened 81 distinct source URLs while checking the A2, A6 and A9 material in full. The A9 rewrite that followed (chat 3) opened 43 distinct URLs, 34 of them among Audit 1's; the A6 rewrite (chat 5) opened 45, 15 of them Audit 1's (`count2.py`, over the URLs in the saved reads of chats 1 to 9). The rewrites' asks told them to re-verify by search any figure carried over. B8 rule 18 says a fact is searched once, filed with its source and date, and searched again only at its staleness check. An audit that has just confirmed a claim at its source has done that search; the rewrite needed only the failed claims and the new ones.

**Re-fetching that is not waste.** The A6 fresh checker (chat 7) opened 46 URLs, 37 of them already opened by the A6 writer. That overlap is the design: DD-B3 rule 3 has the check run in a context that did not see the writing, and B6 Deliverable D has the checker open the cited page itself. Cutting it would cut the check that found an error in 15 of 20 first drafts (§2).

**Parallel research agents.** Four early chats ran five or six parallel agents for research or fact-checking: an audit, two fresh checks and one unit draft (saved reads and summaries of chats 2, 6, 8 and 10). DD-B1's rule sends reading across many sources with a summary as the result to read-only subagents (box 5c), and puts an agent run at about four times a chat's tokens and a multi-agent run at about fifteen (DD-B1 §8, citing Anthropic's 2025 figures; vendor). For a fresh check of one unit, the fan-out bought speed at that multiple; for Audit 1's full check of 91 claims it fits the rule. The history does not show what any of these runs cost, so this finding stays out of the ranked changes.

## 7 · The filed rules, tested against the history

**DD-B3's ten operating rules.**

| Rule | Verdict from the history | Basis |
|---|---|---|
| 1 Delegate what can be checked | Agrees | Checks named in the asks; fresh checks on 20 of 21 units |
| 2 Every brief ends with how to tell it is done | Agrees for row asks | 8 of 17 asks seen at length set `verify.py`'s pass as the test |
| 3 The writer never checks its own work | Agrees | 20 of 21 units fresh-checked in another context |
| 4 File only what I could explain | Not testable | Nothing in the history records his reading |
| 5 Vibe coding for scripts I delete | Not testable | Same |
| 6 Small pieces, one at a time | Partly contradicted | 16 multi-row asks; one-row asks are shorter (correlational) |
| 7 Unattended runs have four guards; never on course units | Contradicted in plan | The figure passes over filed units were confirmed on 29 Oct as an overnight run (asks of chats 36, 37); a later reply calls that line "now just history", and the two ran on the morning of 30 Oct, chat 36 with a message from him in it |
| 8 The vault is the memory | Agrees | The row asks seen in full open by cloning the repository; 13 chats save the next prompt into its row |
| 9 Never the trifecta | Not tested | The history does not show which tools each chat held |
| 10 No "think harder"; effort in the menu | First half agrees; second untestable | No such phrase in any ask; effort never recorded |

**B8's usage rules 11 to 24.** Rule 11 (model and effort before the first message): four chats' commits carry two models, and effort is never recorded. Rule 12 (one task per chat): partly contradicted, as rule 6. Rule 13 (a long chat after a break becomes a new chat with a handoff note): nine chats stayed open three hours or more, one 20.2 hours; open time is not active time, so this is a flag, not a finding. Rule 16 (never paste what a chat can read by path): contradicted on 28 October, followed since. Rule 18 (a fact searched once): contradicted by the A9 rewrite (§6). Rule 21 (check usage first) and DD-B1's rule 28 (the week's unit and audit before optional agent runs): the history shows Fable running short on 29 October and the Fable checks deferred while optional figure passes ran on 30 October; whether the figure passes, on Opus, drew the same pool as Fable depends on the plan (B8 §1). Rule 22 (memory off in this Project): the memory tool was called in six chats. Rules 14, 15, 17, 19, 20, 23 and 24 cannot be tested from the history.

**DD-B1's rules 25 to 28, and its decision rule.** Rule 25 (a stop in every agent prompt) agrees: four figure-chat asks drop a figure that fails twice. Rule 26 (a complete subagent brief) agrees on the one adder brief seen. Rule 27 (commit, then a branch or worktree) is contradicted: of the 39 chats whose asks are held as text, one names a branch and none a worktree; ten chats began while an earlier one was still open (14 overlapping pairs by first-message and last-update times, an upper bound); on 2 November one chat reverted its own merge because another session was alive and mid-unit on the same repository, and on 29 October one found that "another chat beat this one to it" (`count.py`, `count2.py`; listing snippets of chats 34 and 52). Rule 28 is discussed under B8.

The decision rule, applied to the 20 chats that ran agents (unit writing 9, audits 4, figure passes 4, infrastructure 2, history 1; `count2.py`): box 3 (a pass/fail check) and box 5 (shape) fit what he did, a read-only fan-out for checking and a same-change fan-out for figures, staged one course after another, which is box 5d's "two or three files first" at the scale of courses. Box 6 was not followed (§4). Box 8 would have failed on its line "The result lands on a branch he merges or deletes", and a failed line sends the run to a session he watches; the two passes planned for the night ran on the morning of 30 October instead, in sessions that handed back to him. Box 2 says publishing and deploying are actions he does himself, because no checkpoint or git revert can undo them; in the history, 13 of the 16 row asks read in full have the session publish and deploy to the public Pages site. The code of a deploy can be reverted; what a public page showed cannot be unshown, and B4 F15 found six private terms in the build that `deploy.sh` pushes (29 Oct). The history contradicts box 2, and B4 F15 shows what the box guards against. Whether `verify.py` now runs B4's private-terms check before a deploy cannot be read from the history.

**B2, B1, B5 and B6.** B2's table held on its rows and has none for 30 of 53 chats (§4). B1's mental model predicted both costs seen: a long chat re-sends its history every turn, and a 50,000-character paste crowds the window. B5's skills were used where they exist; the closing procedure and the next prompt are the by-hand work (§5). B6's fresh checks earned their place (15 of 20 first drafts with an error); the research paid twice was the rewrite re-searching what an audit had confirmed (§6).

## 8 · What this reading can and cannot carry

Beyond §1's limits: the six days were a week spent building the course machine, so the mix of tasks will not be a normal week's; a second reader could label a few chats differently, most likely between infrastructure and figure passes; the URL counts cover only the parts of the nine early chats whose saved reads hold their tool calls; and no count is a cost, since the history holds no usage figures. The ten changes are ranked by the size of the count each rests on and the share of the work it touches, which is the writer's judgement on those counts.

## Deliverable · Personal gap report: ten changes, ranked

Over the Project's 53 chats, 28 October to 2 November 2026; counts by the writer's scripts over the working table, model read for every chat from its commit trailers, outcome read where shown and otherwise recorded as not read. Each change names its count, what the count is over, the rule it bears on, the change in words to act on, and what would show it worked.

**1 · Fable only for checking.**
*Count:* 17 of the 22 chats run on Fable 5.1 in whole or part were not audits or fresh checks; 18 of the 22 began on 28 October; an ask confirmed on 29 October records him low on Fable, and all 9 fresh checks run on 2 November ran on Opus with a Fable check owed. *Bears on:* B2's routing table, Audits row; B8 rule 21; DD-B1 rule 28.
*Change:* Open a Fable chat only for an audit, a fresh check or a staleness check. Every other row, whatever is open, runs on Opus or Sonnet by change 2. Clear the nine owed Fable checks before any new Fable use.
*Worked if:* over the next four weeks every Fable chat is an audit or a check, and no new fresh check is recorded as "Opus, Fable owed".

**2 · A routing row for the machine.**
*Count:* 30 of 53 chats are of task types B2's table has no row for (infrastructure 15, figure passes 7, status 6, syllabus 2); the 15 infrastructure chats ran on Fable 8, Opus 5, both 2; no chat ran on Sonnet or Haiku (0 of 53). *Bears on:* B2's routing table and its §8 on code.
*Change:* Add three rows to the routing table. Build and site rows with a `verify.py` pass as their test: Sonnet 5.5, medium; escalate to Opus once if verify fails twice on the same cause. Method, skill and design-decision rows: Opus 5.5, high (efforts by analogy with B2's rows; untested). Figure and other fan-out agents: as change 3.
*Worked if:* every infrastructure prompt names its row's model and effort, and B2's one-line escalation log shows how often Sonnet had to hand up.

**3 · Move a fan-out down once its check has passed.**
*Count:* 7 figure chats, median 33 turns, 6 on Opus; in the Greek pass alone 218 agents (78 adders, 78 checkers, 62 re-checkers), after the same loop had run over the Brand + AI units and the 59 Rome reports; every agent call in the two saved reads that show one (199 and 37) ran on Opus; 6 of 266 figures dropped. *Bears on:* DD-B1's decision rule, box 6.
*Change:* After a fan-out's loop has run over two sets with its check passing, run its workers on Sonnet 5.5 and keep the checker on Opus. Compare the drop and fix rates with the Opus run before moving more.
*Worked if:* the next fan-out on Sonnet drops no more than about 2% of its proposals (6 of 266 on Opus) and its checker's fix rate does not rise.

**4 · No session deploys to the public site without the private-terms check.**
*Count:* 13 of the 16 row asks read in full have the session publish and deploy to the public Pages site; B4 F15 found six private terms in the build `deploy.sh` pushes. *Bears on:* DD-B1's decision rule, box 2; B4 F15 and its check 6.
*Change:* Make B4's private-terms check a step of `verify.py` that fails the build, with the terms file kept outside both repositories. A session may run `deploy.sh` only after ALL CHECKS PASSED with that step in it; until the step exists, he runs the deploy himself after looking at the diff.
*Worked if:* the next deploy's verify output names the private-terms step and its pass, and a planted test term makes the build fail.

**5 · One writer to `main` at a time.**
*Count:* 10 of 53 chats began while an earlier one was still open (14 overlapping pairs, an upper bound); one chat reverted its own merge because another session was mid-unit; one found another chat had already done its work; of the 39 asks held as text, one names a branch and none a worktree. *Bears on:* DD-B1 rule 27; DD-B3 rule 6.
*Change:* Before opening a second session on the repository, check the first has pushed its last commit. When two must run together, the second works on a branch named for its row and its last step is a rebase and merge after the other has landed.
*Worked if:* no revert of another session's work and no "already done by another chat" in the next month.

**6 · Model and effort in the first line, and in the changelog.**
*Count:* the model can be read in all 53 chats, but only by searching inside each one for its commit trailers; effort in 0 of 53. *Bears on:* B8 rule 11; B2's effort column; the method's rule to record the model that actually wrote each unit.
*Change:* Every prompt opens with one line, "Model: X, effort: Y", set in the menu before sending; every changelog row records both, and every agent call names its model.
*Worked if:* a re-run of this count reads model and effort for every chat after the change.

**7 · The closing procedure in one skill, pointed to.**
*Count:* 13 of the 16 row asks read in full restate the publish procedure; 7 carry "publish once"; those quoted in the listing also point to the method's §8; 13 chats end by writing the next prompt by hand. *Bears on:* B5 §6's four questions (all four pass); B4 F7 on paraphrased procedure.
*Change:* Put build, verify, publish, deploy, row close, mirror rewrite and next-prompt writing in one skill in the repository, with a template for the next prompt. Every prompt then ends with one line: "Close per the skill." Keep in the prompt only what this row changes.
*Worked if:* the next prompts lose the restated paragraph, and no publish in the next month is forced, doubled or sent to a new artifact.

**8 · Carry an audit's confirmed claims forward instead of re-searching them.**
*Count:* the A9 rewrite opened 43 distinct URLs, 34 of them already opened by Audit 1 that morning; the A6 rewrite 45, 15 of them Audit 1's; the rewrite asks told the writer to re-verify by search any figure carried over. *Bears on:* B8 rule 18; B6 Deliverable A.
*Change:* In a rewrite brief after an audit, list the claims the audit confirmed with its date and tell the writer to carry them over unchanged; search only the claims it failed and any new ones. Leave the fresh checker's own re-opening of sources alone.
*Worked if:* the next post-audit rewrite opens only URLs outside the audit's confirmed list, and its fresh check finds no error in a carried-over claim.

**9 · No overnight plan without a branch.**
*Count:* two figure-pass asks were written for an overnight run over filed course units; of the 39 asks held as text, one names a branch, though the Rome and Greek passes worked on side branches (`p43-rome-wip`, `n5-p57-wip`; the project's changelog, P62 and P65); both runs went ahead on the morning of 30 October instead. *Bears on:* DD-B3 rule 7 ("Never on course units"); DD-B1 box 8.
*Change:* An unattended run is planned only for work outside filed units, and only when its prompt names the branch it lands on, its attempt cap and its pass line. A pass over filed units runs where he watches it.
*Worked if:* every unattended run in the next month names a branch, and none touches a filed unit.

**10 · Account memory off in this Project.**
*Count:* the model called the memory tool in 6 of 53 chats, all in the parts of the chats that were read. *Bears on:* B8 rule 22; B4 F13.
*Change:* Turn off "Use account memory" for the Learning Project now, and say in the project instructions that no chat reads memory.
*Worked if:* no memory call appears in the next ten chats opened at their first turns.

**Flagged, not ranked:** nine of 53 chats stayed open three hours or more, one 20.2 hours over 43 turns (`count2.py`); open time is not active time, so this bears on B8 rules 13 and 14 only if a re-count with activity times confirms it.

**Already fixed in the window, so not ranked:** terse and status-opened asks (11 in chats 1 to 33, none in 34 to 53); whole units pasted into asks (7, the last at 07:48 on 28 October); row codes that collided with unit codes (2, before the hyphenated row names).

## Sources

All sources are this Project's chat history, read through the past-chat tools on 2 and 3 November 2026 across three agent runs, and the course's filed units. No web source was used (search off; no search made).

- The Project's chat history, 28 October 2026 05:42 to 2 November 2026 17:51 local time: 53 chats listed with `recent_chats`; 16 opened with `read_conversation`; spots inside 7 more found with `conversation_search`. Chats are referred to by the writer's index number (1 to 53, in order of first message) and date; the history is private.
- The writer's tallies: `count.py` and `count2.py` over the working table of the 53 chats and the fresh-check lines of the filed units (working files, not published).
- Filed units used: B1 · Mental model (§2, §5); B2 · Choosing the model (§2, §8, Deliverable); B4 · Context engineering (F7, F13, F15 and its check 6); B5 · Skills and automation (§3, §6); B6 · Research and verification (§2, Deliverables A and D); B8 · Cost, limits, hygiene (§1, Deliverable rules 11 to 24); DD-B1 · Deep dive: agents (§8, rules 25 to 28, Deliverable); DD-B3 · Deep dive: how the best practitioners use the tool (Deliverable B, rules 1 to 10); and the fresh-check records of the 20 filed units that carry one.

## Writer's unsure list

1. Turn counts are the tools' total_turns, recorded by the second run; their definition (one message either side, agent notices included) is inferred from chats where both sides can be counted.
2. Task type is a hand label; infrastructure and figure passes overlap in about three chats.
3. "Accepted" is a proxy (filed, or reported done and not corrected); 14 chats' endings were not seen.
4. Each chat's model is read from the commit trailers a search inside it returns and those in the saved reads; a chat whose commits all came from agents could hide its own model.
5. The 10 overlapping chats are counted from first message to last update, which overstates overlap when a chat sat idle.
6. URL overlaps come from the parts of chats 1 to 9 that were read, not their full tool histories.
7. That every agent call in chats 40 and 45 ran on "opus" rests on the saved reads, which cover one turn range each.
8. Whether Fable on his plan draws usage credits or a share of the weekly limit is not stated in any filed unit for his account; §4 and change 1 hold either way.
9. The memory-tool count (6) comes from visible turns only; chats not opened may hold more.
10. Chats 24, 43, 48 and 52 carry Opus and Fable trailers (the writer and the fresh checker each found one of the two in chats 24 and 48); either may be an agent of the other model inside the chat rather than a switch of the chat's model.
