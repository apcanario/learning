---
kind: corrections-check
row: W-BW9
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [BW6, BW8]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

The checker's report, verbatim from its reply (the harness refused it a report file), saved before any change was applied.

Model: claude-opus-5-5 (Opus 5.5)

The write to /home/claude/w-bw9/corr1/out/report.md was refused ("Subagents should return findings as text"), so the full report is below. A script confirmed that every Current block occurs exactly once in its file. No viz block is touched.

Summary: 7 PASS and 0 FAIL (5 in BW6, 2 in BW8); 0 syllabus conflicts; 2 not-a-text-change items (BW2 Fable versions, BW1 fork default). Outside scope: flag F50 now names a verification subagent that the page no longer carries; the fork default bears on BW6's fresh-check advice; BW8's Deliverable Claude Code step 1 has one phrase that may belong to the scheduled-tasks page; the correction's "v2.1.196" for scheduled tasks is not on the skills page.

---

Model: claude-opus-5-5 (Opus 5.5)

# Corrections check, row W-BW9 (Building with AI), 16 Nov 2026

Sources read today under the web rule (WebSearch first; WebFetch only on a URL that search returned verbatim):

- *Best practices for Claude Code*, page at https://code.claude.com/docs/en/best-practices?ref=t01.li (returned by search) and the .md copy at https://code.claude.com/docs/en/best-practices.md (returned by search). The two differ, as contradiction 1 says. The .md copy still carries all of BW6's quotes word for word ("won't be biased toward code it just wrote", "not the reasoning that produced the change", "so the agent doing the work isn't the one grading it", "will usually report some, even when the work is sound", "If you can't verify it, don't ship it"). The page carries none of them.
- *Extend Claude with skills*, page at https://code.claude.com/docs/en/skills (returned by search), read in two parts (offset 0 and offset 100000).
- *Models overview*, .md copy at https://platform.claude.com/docs/en/models/overview.md (search did not return the English page itself).
- *Model configuration* (Claude Code), .md copy at https://code.claude.com/docs/en/model-config.md (search did not return the English page itself). The fetch covered the first 100,000 of 126,212 characters.
- *Create custom subagents*, page at https://code.claude.com/docs/en/sub-agents (returned by search), read in two parts (offset 0 and offset 100000).

Contradiction 1 gives Changes 1 to 5 (BW6). Contradiction 3 gives Changes 6 and 7 (BW8). Contradictions 2 and 4 are not text changes.

## Change 1

Contradiction 1, BW6 §4, "What a fresh context removes". This is merged with the §8 table row (Change 3) because both rest on the same quotes. The sentence quotes three phrases that are only in the .md copy. Change 3 moves the §8 row to the page, so §4 has to quote the page as well, or the two would contradict each other. The rest of the paragraph does not change.

File: BW6-research-and-verification.md
Current:
```
Anthropic's Claude Code guide says a fresh context improves review because Claude "won't be biased toward code it just wrote", and that a reviewer in a fresh subagent context sees the work and the criteria it is given, "not the reasoning that produced the change"; its pattern for a second opinion is a verification subagent that tries to refute the result, "so the agent doing the work isn't the one grading it" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md), read 16 Nov 2026; vendor, documented practice).
```
Replacement:
```
Anthropic's Claude Code guide says that `/code-review` reviews the diff "in a fresh subagent that never saw your conversation. It isn't swayed by the reasoning that produced the code", and that, while handing the same task to a subagent does not make the answer better, "A fresh reviewer does help, because it hasn't seen your reasoning" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices?ref=t01.li), read 16 Nov 2026; vendor, documented practice).
```
Result: PASS. The page says: "By someone who didn't write the code: in the terminal, [`/code-review`](https://code.claude.com/docs/en/code-review-local) reviews the diff in a fresh subagent that never saw your conversation. It isn't swayed by the reasoning that produced the code." Its table of outdated advice says: "Handing the same task to a subagent doesn't make the answer any better. A fresh reviewer does help, because it hasn't seen your reasoning, which is a different thing from delegating." Source: https://code.claude.com/docs/en/best-practices?ref=t01.li, read 16 Nov 2026.
Syllabus: no conflict. The BW6 brief quotes neither the old wording nor the new. Flag F50 (not a brief) says BW9 covers "Claude Code's verification subagent", which BW6 no longer names after this change. See Notes 1.

## Change 2

Contradiction 1, BW6 §4, "What a fresh checker adds of its own".

File: BW6-research-and-verification.md
Current:
```
The same guide warns that a reviewer prompted to find gaps "will usually report some, even when the work is sound", and that chasing every finding leads to over-engineering (*Best practices for Claude Code*, read 16 Nov 2026; vendor).
```
Replacement:
```
The same guide warns that "A reviewer that's asked to find problems will always find *something*", and that fixing every finding ends in "extra abstraction layers and tests for cases that can't happen" (*Best practices for Claude Code*, read 16 Nov 2026; vendor).
```
Result: PASS. The page says: "Don't drop the `skip style` part of that prompt. A reviewer that's asked to find problems will always find *something*. If you fix every finding, you end up with extra abstraction layers and tests for cases that can't happen." Source: https://code.claude.com/docs/en/best-practices?ref=t01.li, read 16 Nov 2026.
Syllabus: no conflict

## Change 3

Contradiction 1, BW6 §8 table, the review row. The page has no verification subagent that tries to refute the result; only the .md copy has it ("a fresh model try to refute the result"). The other cells of the row do not change.

File: BW6-research-and-verification.md
Current:
```
| A fresh context or subagent for review; a verification subagent that tries to refute the result (§4) | [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md) |
```
Replacement:
```
| A fresh subagent for review, one that never saw the conversation (§4) | [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices?ref=t01.li) |
```
Result: PASS. The page says `/code-review` "reviews the diff in a fresh subagent that never saw your conversation", and "A fresh reviewer does help, because it hasn't seen your reasoning". A search of the page text for "refut" finds nothing. Source: https://code.claude.com/docs/en/best-practices?ref=t01.li, read 16 Nov 2026.
Syllabus: no conflict

## Change 4

Contradiction 1, BW6 Deliverable step I. The page does not carry "If you can't verify it, don't ship it". The replacement quotes the page's equivalent condition, which matches question 1 of the test ("a check that returns pass or fail").

File: BW6-research-and-verification.md
Current:
```
Anthropic's Claude Code guide puts it in eight words: "If you can't verify it, don't ship it" (*Best practices for Claude Code*, read 16 Nov 2026; vendor).
```
Replacement:
```
Anthropic's Claude Code guide states the condition for leaving an agent to work unwatched: "Give Claude something it can run that comes back pass or fail. Once it has that, it can keep going on its own and you don't have to watch" (*Best practices for Claude Code*, read 16 Nov 2026; vendor).
```
Result: PASS. The page's tip reads: "Give Claude something it can run that comes back pass or fail. Once it has that, it can keep going on its own and you don't have to watch." Source: https://code.claude.com/docs/en/best-practices?ref=t01.li, read 16 Nov 2026.
Syllabus: no conflict. The BW6 brief requires "the verifiability test BW9 uses to decide what to delegate". The test and its four questions are unchanged.

## Change 5

Contradiction 1, BW6 Sources entry. After Changes 1 to 4, no claim in BW6 rests on the .md copy. Flag F41's rule is that each unit names the exact URL it read.

File: BW6-research-and-verification.md
Current:
```
- Anthropic. *Best practices for Claude Code*. Claude Code documentation (vendor). https://code.claude.com/docs/en/best-practices.md
```
Replacement:
```
- Anthropic. *Best practices for Claude Code*. Claude Code documentation (vendor). https://code.claude.com/docs/en/best-practices?ref=t01.li
```
Result: PASS. The page at this URL carries every quote in Changes 1 to 4 (see their results). Source: https://code.claude.com/docs/en/best-practices?ref=t01.li, read 16 Nov 2026.
Syllabus: no conflict

## Change 6

Contradiction 3, BW8 §1: the address only. I checked every BW8 claim that cites *Extend Claude with skills* (§1, §2, §3, §8, the two viz captions and Deliverable Claude Code steps 1 to 3) against the page. All hold on the page except one phrase in Deliverable step 1 (Notes 3). Quotes from the page: "**Custom commands have been merged into skills.**"; disable-model-invocation: "Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`. Also prevents the skill from being preloaded into subagents and from running when a session-scoped scheduled task fires with the skill as its prompt"; "Create a skill when you keep pasting the same instructions, checklist, or multi-step procedure into chat, or when a section of CLAUDE.md has grown into a procedure rather than a fact"; personal skills: "All your projects on this machine, but not Cowork or cloud sessions"; project skills: "Sessions in this repository, but not cloud threads in a project"; synced skills: "Syncing in terminal sessions requires Claude Code v2.1.273 or later"; "each entry's combined text is capped at 1,536 characters regardless of budget. The cap is configurable with `skillListingMaxDescChars`"; "The budget scales at 1% of the model's context window. When the listing overflows, Claude Code drops descriptions starting with the skills you invoke least"; "Claude Code reads the frontmatter only when the opening `---` is the file's first line"; "If the YAML between the markers doesn't parse, the skill still loads with no fields set"; "so `/skill-name` still works but Claude can't match against your `description`"; troubleshooting: "1. Check the description includes keywords users would naturally say 2. Verify the skill appears in `What skills are available?` 3. Try rephrasing your request…", and for a skill that triggers too often, "Make the description more specific" and "Add `disable-model-invocation: true`"; "**Claude skipped a rule that must hold every time**: move the rule into a hook"; "Claude Code does not re-read the skill file on later turns"; after compaction, "keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens."

File: BW8-skills-and-automation.md
Current:
```
Claude Code documentation](https://code.claude.com/docs/en/skills.md), read 16 Nov 2026; vendor).
```
Replacement:
```
Claude Code documentation](https://code.claude.com/docs/en/skills), read 16 Nov 2026; vendor).
```
Result: PASS. The page says: "**Custom commands have been merged into skills.**" On `disable-model-invocation`: "Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`." Source: https://code.claude.com/docs/en/skills, read 16 Nov 2026.
Syllabus: no conflict. Flag F69's rule is to cite and read the page. Flag F65's facts are confirmed on the page.

## Change 7

Contradiction 3, BW8 Sources entry.

File: BW8-skills-and-automation.md
Current:
```
- Anthropic. *Extend Claude with skills*. Claude Code documentation. https://code.claude.com/docs/en/skills.md
```
Replacement:
```
- Anthropic. *Extend Claude with skills*. Claude Code documentation. https://code.claude.com/docs/en/skills
```
Result: PASS. Every BW8 claim that cites this source holds on the page (quotes under Change 6), apart from the phrase in Notes 3, which was not checked. Source: https://code.claude.com/docs/en/skills, read 16 Nov 2026.
Syllabus: no conflict

## Not a text change 1

Contradiction 2 (BW2 §2, Appendix, against Claude Code's naming of Fable 5.1). BW2's claims stand. *Models overview* (.md copy, read 16 Nov 2026) still lists Claude Fable 5.2 first among the latest models, at "$8 / input MTok, $40 / output MTok", with Claude Fable 5.1 at "$10 / MTok" input and "$50 / MTok" output in the "All models" table. BW2 says nothing about what Claude Code's `/model fable` selects. The two vendor pages describe different things: the API lineup, and Claude Code's alias. *Model configuration* (.md copy, read 16 Nov 2026) says: "Unless you set `ANTHROPIC_DEFAULT_FABLE_MODEL`, the `fable` alias resolves to Fable 5.1, except in Claude apps gateway sessions, where `fable` and `best` resolve to Fable 5." In the part read, it does not mention Fable 5.2. Nothing in BW2 contradicts either page.
Proposed flag. Units affected: BW9, BW10, DD-BW1, and any later unit that names the Fable version selected in Claude Code. Flag: Source (two vendor pages, two scopes). On 16 Nov 2026 Anthropic's API lineup (*Models overview*) has Fable 5.2 at the top, and Fable 5.1 among all models. Claude Code's *Model configuration* and *Best practices* say `/model fable` selects Fable 5.1 (Fable 5 in Claude apps gateway sessions). Proposed change: none to the briefs. A unit that names the model behind a Claude Code alias cites *Model configuration* and dates it; a unit that names the API lineup cites *Models overview*; neither carries one page's version into a claim about the other. BW2 unchanged.

## Not a text change 2

Contradiction 4 (BW1 §8, Agents row, "a subagent in its own window, fresh unless forked from the conversation"). The row is accurate as written. *Create custom subagents* (read 16 Nov 2026) says: "Each subagent starts with a fresh, isolated context window. … The exception is a fork, which inherits the parent conversation instead of starting fresh." BW1 does not say that a fresh window is the default. The default the correction raises is real: "Claude can start a fork on its own while fork mode is on, as it is by default", and "Fork mode is on by default from Claude Code v2.1.302, and in an interactive terminal session from v2.1.232" (same page). *Best practices* (page) says: "Side tasks get forked while fork mode is on (the default)." Saying so in BW1 would add a claim and a source to a table read on 15 Nov 2026 against *How Claude Code works*. That goes beyond correcting the row, and BW9 owns subagents (BW1 §8 itself sends agents to BW9).
Proposed flag. Units affected: BW9 (§4), BW6 (§4 and Deliverable steps E and F, the fresh check), BW8 (Deliverable, any subagent run), BW10, DD-BW1. Flag: Need (fork default). In Claude Code, fork mode is on by default (v2.1.302; interactive terminal from v2.1.232). While it is on, side tasks Claude starts itself are forks that inherit the whole conversation, so "use a subagent to review" can produce a reviewer that has seen the writing. Proposed change: none to the briefs. BW9 states the fork default, dated, next to its non-fork description. Any unit that relies on a fresh-context check names a way to get one that is not a fork (a custom subagent, `/code-review`, a new session, or fork mode off with `CLAUDE_CODE_FORK_SUBAGENT=0`). BW1 unchanged.

## Notes

1. ⚠ Flag F50 says BW9 "covers what BW6 only names: Claude Code's verification subagent, its /goal condition and Stop hook (Best practices for Claude Code, read 16 Nov 2026)". The verification subagent "that tries to refute the result" is only in the .md copy. The page names `/goal`, the Stop hook and `/code-review` in a fresh subagent. If Changes 1 and 3 are applied, F50's wording needs updating so that BW9 does not take a pattern that is no longer on the page.
2. ⚠ The fork default (Not a text change 2) bears on BW6's own advice. A fresh-context check run as "a subagent" inside the writing session may now be a fork that has seen the writing, unless fork mode is off or a named, non-fork subagent is used. No BW6 text is changed here, because that is outside the corrections' scope.
3. BW8 Deliverable, Claude Code step 1 ("loads … in scheduled runs that clone it", under "read 16 Nov 2026: *Extend Claude with skills*"). The skills page fetch did not find this phrase; the page says only that "each run starts as a fresh cloud session". BW8 §6 sources "works on a fresh clone" to the scheduled-tasks page. The step's attribution may belong to that page. Not checked further: no correction names it.
4. Contradiction 3 states that disable-model-invocation blocks running from a scheduled task's fire "from v2.1.196". On the skills page read today, v2.1.196 appears only in the note on the `/context` Skills row ("Before v2.1.196, the row counted the full text of every description"). The scheduled-task sentence carries no version. BW8 does not state v2.1.196, so BW8 is unaffected. BW9's own use of that version should be checked.
5. *Models overview* and *Model configuration* were read as .md copies, because search did not return the English pages themselves. The pages were not checked.
