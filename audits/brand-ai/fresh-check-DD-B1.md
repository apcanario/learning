---
audit: fresh check
unit: DD-B1 · Deep dive: agents
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5 (search off; a Fable 5.1 fresh check is owed, deferred by Pedro 31 Oct 2026 to the Fable stage)
date: 2026-11-02
chat: own Opus 5.5 agent context, not shown the writing or the writer's report (P31), in session https://claude.ai/code/session_01KMmgQy3HYd2oKQ5Wn6HLVA
verdict: fix · 0 errors, 10 should-fix, 14 minor; against filed units: B5 1 minor
---

# Fresh check · DD-B1 · Deep dive: agents

The checker's final report follows verbatim, extracted by script from its hand-back (its `SubagentHandback` message).

**This fresh check of DD-B1 was run by Opus 5.5. A Fable 5.1 fresh check is still owed.** The course owner deferred Fable 5.1 checks to a later stage on 31 Oct 2026, and this report does not replace that check.

## Read first
- **The unit.** `diff` shows that `/tmp/claude-0/-home-claude/5a6d8118-b9a3-5d7a-b345-b6780150344f/scratchpad/b13/check/DD-B1-check-copy.md` is identical to `/home/claude/learning/courses/brand-ai/DD-B1-deep-dive-agents.md`. I read all 353 lines. I opened nothing else under `b13/` and no transcripts.
- **`docs/sourcing-standard.md`.** Parts 1 and 2.
- **The brief, built by script.** It is `units_data.PRE` (identical to `hub.PRE`) with `{GOAL}` replaced by `hub.GOAL_B`, a blank line, then field 5 of DD-B1's entry in `hub.COURSES[1]['units']`. `hub.ORDER` gives DD-B1 as ('Opus 5.5', search 'off'), which matches the front matter.
- **Audits.** `audits/brand-ai/audit-1.html` (converted to text) and `audit-2.md`.
- **Filed units, in full or by section.**
  - DD-B3 in full.
  - B5: §1, §4, §5, Deliverable D and the unsure list.
  - B8: §1 to §5 and rules 11 to 24.
  - B7: §9 and Deliverable A steps 0 to 9.
  - B6: §1, §2 and Deliverable A.
  - B2: §1, §2, §8 and the routing table.
  - B4: §1, F8, F9, F14 and F15.
  - B1 §6.
  - The fresh-check line at the end of every filed unit.
- **Other files.** `docs/method.md` (§7 header, §4 search list) and `docs/BACKLOG.md` / `CHANGELOG.md` for the status of F8 and F9.

## Method
- **Web rule.** I ran WebSearch first every time and fetched only URLs that a search in this context returned, copied exactly. I fetched no URL taken from the unit or typed from memory. I used no memory, Projects, connector, browser or Artifact tool.
- **Redirects.** No fetch reported a redirect.
- **Failed or partial fetches.**
  - The billmill transcription of the YC talk was never returned by a search. The one transcript page that was returned (feedbagel) does not carry the quotations. The YC quotations are therefore unverifiable (not checked).
  - On the autoresearch repository, only the README was visible, not `program.md`. "NEVER STOP", "until the human interrupts you, period" and "git reset" are therefore unverifiable (not checked).
  - The *Permission modes*, *Subagents*, *Hooks* and Dwarkesh pages were truncated at 100,000 characters. Every item checked was inside that range.
- **The OpenAI guide.** The PDF itself was not returned by search. OpenAI's own guide page (openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/), which was returned, reproduces the quotations.
- **Two copies of the best-practice page.** Search returned both `best-practices?r=0` (the unit's copy) and `best-practices?curius=2107`. They differ (see findings).
- **Uniqueness check.** I checked every Current with `grep -F -c` on the check copy, or with Python `str.count` where quotes, backticks or arrows would break the shell. Every one returns 1. The Current against B5 was checked the same way in B5 and returns 1.
- **Calculations.** I re-ran every calculation in Python (see Calculations below).

## (1) Coverage
- **Agent against chat (tools, loops, autonomy):** covered (§1).
- **Claude Code and subagents in practice:** covered (§2).
- **His own cases:**
  - pcblueprint: covered.
  - AIssistant: thin. Only one line is documented, and the unit says so.
  - Strider: thin. It is undocumented, so the unit works it as a hypothetical and says so.
- **What agents do well:** parallel research, repetitive edits and builds with tests are all covered (§4).
- **What they quietly wreck:** silent wrong assumptions, overwriting and cost blowups are all covered (§5).
- **Guardrails:** scopes, dry runs and review gates are all covered (§6).
- **Deliverable:** covered. It is a nine-box prose flowchart plus an "on every path" line.
- **Length.** The body runs to about 7,400 words, leaving out figures and Sources but counting the unsure list. That is above the brief's 2,000–6,000 guide, as DD-B3 and B5 also are. I found no padding to cut, so this gets no finding.

## (2) to (6) Findings
- [should-fix | accuracy] §2 "The starting rung is high"
  - Current: `Auto mode is "the built-in starting permission mode for interactive terminal and VS Code sessions" on current versions (*How Claude Code works*), and on Pro, Max and Team plans by the best-practice page ([Claude Code docs, *Best practices*](https://code.claude.com/docs/en/best-practices?r=0), read 2 Nov 2026);`
  - Problem: The pages do not give two rival conditions. *How Claude Code works* and *Permission modes* ("Which mode a session starts in") both say auto is the starting mode "With Claude Code v2.1.283 or later" and, on earlier versions, only on Pro, Max and Team plans. The `?r=0` copy gives only the plan condition. A later copy of the same page says the same as the other two pages.
  - Fix: `Auto mode is "the built-in starting permission mode for interactive terminal and VS Code sessions" with Claude Code v2.1.283 or later, and on earlier versions only on Pro, Max and Team plans (*How Claude Code works*; *Permission modes*, "Which mode a session starts in"; the copy of the best-practice page opened at [best-practices?r=0](https://code.claude.com/docs/en/best-practices?r=0) on 2 Nov 2026 gives the plan condition alone);`
  - Basis: https://code.claude.com/docs/en/how-claude-code-works ; https://code.claude.com/docs/en/permission-modes ; https://code.claude.com/docs/en/best-practices?curius=2107
- [minor | accuracy] Writer's unsure list, item 9 (same cause)
  - Current: `9. **Auto mode as the starting mode.** *How Claude Code works* ties it to version 2.1.283 or later; the best-practice page ties it to Pro, Max and Team plans. Which version and plan his sessions run on is not recorded in any filed unit.`
  - Fix: `9. **Auto mode as the starting mode.** *How Claude Code works* and *Permission modes* tie it to version 2.1.283 or later, and on earlier versions to Pro, Max and Team plans; the copy of the best-practice page opened gives the plan condition alone. Which version and plan his sessions run on is not recorded in any filed unit.`
  - Basis: as above.
- [should-fix | figure] §5 Silent wrong assumptions
  - Current: `His own record is the measured case: of the fourteen filed Brand + AI units with a fresh-check line, eleven had at least one error-severity finding at their first check, all written by Opus 5.5 with the sourcing standard in the brief (B6 §2).`
  - Problem: The citation of B6 is correct, but the count is B6's and is out of date. On 2 Nov 2026, before DD-B1, 18 filed units carry a fresh-check line. Fifteen of them had at least one error: A1, A2, A4, A5, A6, A8, A9, B2, B3, B5, B6, B7, B8, DD-A1 and DD-B3. The three with none are A3, A7 and B4. Seven of the 18 checks were run by Opus 5.5.
  - Fix: `His own record is the measured case: when B6 counted, eleven of the fourteen filed Brand + AI units with a fresh-check line had at least one error-severity finding at their first check (B6 §2); by 2 November 2026, before this unit, it was fifteen of eighteen (my count from the fresh-check lines at the end of each unit; seven of the eighteen checks were run by Opus 5.5 with a Fable 5.1 check owed). All were written by Opus 5.5 with the sourcing standard in the brief.`
  - Basis: the fresh-check lines in `courses/brand-ai/*.md`; B6 §2, line 182.
- [should-fix | attribution] §3 pcblueprint, agents working on its code
  - Current: `and health numbers live in the private vault and nowhere else (B8 rule 22).`
  - Problem: B8 rule 22 keeps health numbers out of memory and Projects ("health, other people's data and drafts live in the private vault"). It does not say "nowhere else". B8 §5's table lets "Change only, from the publish list" reach the public build, and pcblueprint itself holds the numbers.
  - Fix: `and health numbers belong in the private vault, never in memory or a Project (B8 rule 22; B8 §5's table lets only changes from the publish list reach the public build).`
  - Basis: B8 rule 22 and the §5 table.
- [should-fix | deliverable] §3 pcblueprint, the model for the script
  - Current: `The model is B2's: "Haiku 5.5 writes and maintains the parsing script; the script does the parsing", with Sonnet 5.5 after the script breaks twice on a new export format (B2, Biometrics parsing).`
  - Problem: §3 runs this script as a Claude Code loop with a fixture check. That makes it a new agent loop, and box 6 and §7 say a new loop "runs first on Opus 5.5". §3 and the Deliverable give different first models for the same task. B2 §8 itself also says "For his generator scripts and parsers, Sonnet is enough".
  - Fix: `B2's routing table gives the script to Haiku 5.5 ("Haiku 5.5 writes and maintains the parsing script; the script does the parsing"), with Sonnet 5.5 after the script breaks twice on a new export format (B2, Biometrics parsing). Run as a Claude Code loop against a fixture, its first version is a new loop in box 6's sense, so it is written on Opus 5.5 with the fixture check and handed to B2's models for maintenance once the check passes on repeat runs (my rule, reconciling B2 with §7).`
  - Basis: B2 routing table and §8, line 254; DD-B1 box 6.
- [should-fix | accuracy] §7 "Most capable model first"
  - Current: `and the evidence on long agentic tasks favours the larger models: on Terminal-Bench 4.0, Haiku 5.5 scores 39.2% against Opus 5.5's 66.4% (at xhigh) and Sonnet 5.5's 70.6%, and Anthropic recommends Sonnet or Opus over Haiku for complex agentic coding (B2 §8; vendor). So a new loop runs first on Opus 5.5 with its check,`
  - Problem: In the cited figures Sonnet scores above Opus, and B2 §8 reads the two as "level". The figures favour Sonnet and Opus over Haiku. They do not single out Opus. Opus goes first on another ground, which B2 §1 records: the model page advises starting with Opus 5.5 when unsure.
  - Fix: `and the evidence on long agentic tasks favours Sonnet 5.5 and Opus 5.5 over Haiku 5.5: on Terminal-Bench 4.0, Haiku 5.5 scores 39.2% against Opus 5.5's 66.4% (at xhigh) and Sonnet 5.5's 70.6%, which B2 §8 reads as the top two level, and Anthropic recommends Sonnet or Opus over Haiku for complex agentic coding (B2 §8; vendor). Opus 5.5 goes first because the model page's advice is to start with it when unsure (B2 §1). So a new loop runs first on Opus 5.5 with its check,`
  - Basis: B2 §1, line 29; B2 §8, line 254.
- [should-fix | accuracy] §8 B7, "Chaining steps moves the gate"
  - Current: ``Step 3's pass rewrites or cuts every `[NEW]` line before titles, the Short, Instagram and the email are built on the script (B7, Deliverable A, step 3). An agent running steps 3 to 8 in one go would build all four on lines he has not passed.``
  - Problem: B7 step 8 (email) takes "the latest entry; in an episode week, the record … ; the links", not the script. Step 4 is his filming and edit ("no model"), and steps 5 to 7 take the final script after the edit. "Steps 3 to 8 in one go" therefore includes a human step, and the agent would affect three outputs, not four.
  - Fix: ``Step 3's pass rewrites or cuts every `[NEW]` line before titles, the Short and Instagram are built on the final script, after his filming and edit in step 4; the email is built on the entry and the record (B7, Deliverable A, steps 3 to 8). An agent chaining steps 3, 5, 6 and 7 in one go would build three of them on lines he has not passed, and would have no edit to build on.``
  - Basis: B7 Deliverable A, steps 3 to 8.
- [should-fix | accuracy] §6 Scopes, Tools
  - Current: ``- **Tools.** The `tools` allowlist on a subagent, `--allowedTools` on a scripted run (§2, §4).``
  - Problem: A later copy of the best-practice page, returned by search on 2 Nov, gives `--allowedTools` as pre-approving. It reads: "The `--allowedTools` flag pre-approves the tools the migration needs, and `--permission-mode dontAsk` denies anything else that would need approval". *Permission modes* has dontAsk deny "anything that would prompt". On its own, the flag is not a restriction, and this is a product fact that is changing.
  - Fix: ``- **Tools.** The `tools` allowlist on a subagent; on a scripted run, `--allowedTools` together with `--permission-mode dontAsk`, since `dontAsk` denies "anything that would prompt" (*Permission modes*) and `--allowedTools` alone pre-approves (§4).``
  - Basis: https://code.claude.com/docs/en/best-practices?curius=2107 ; https://code.claude.com/docs/en/permission-modes
- [should-fix | deliverable] Deliverable, box 5(d) (same cause)
  - Current: `→ **(d) The same change across many files:** a fan-out, with an allowed-tools list, on a branch or in worktrees; two or three files first, checked, then the rest.`
  - Fix: ``→ **(d) The same change across many files:** a fan-out, with an allowed-tools list and `dontAsk` mode, on a branch or in worktrees; two or three files first, checked, then the rest.``
  - Basis: as above.
- [minor | accuracy] §4 Repetitive edits (same cause)
  - Current: ``the `--allowedTools` flag "restricts what Claude can do, which matters when you're running unattended" (*Best practices*)``
  - Fix: ``the `--allowedTools` flag "restricts what Claude can do, which matters when you're running unattended" (*Best practices*, at the address opened); a later copy of the same page, returned by search the same day, says instead that it "pre-approves the tools the migration needs" and adds `--permission-mode dontAsk`, which "denies anything else that would need approval"``
  - Basis: as above.
- [minor | accuracy] §2 Subagents, item 5
  - Current: ``The best-practice page documents `/batch`, which splits a change "across 5 to 30 subagents. Each subagent works in its own worktree and opens a pull request" (*Best practices*).``
  - Problem: "and opens a pull request" is on the `?r=0` copy but not on the later copy.
  - Fix: ``The best-practice page documents `/batch`, which splits a change "across 5 to 30 subagents. Each subagent works in its own worktree" (*Best practices*; the copy opened adds "and opens a pull request", a later copy the same day does not).``
  - Basis: both copies above.
- [should-fix | figure] §3, matrix figure, Strider row (public-site rule)
  - Current: `{"label": "Strider (hypothetical)", "cells": ["undocumented", {"mark": "yes (reads the web)", "tone": 4}, "undocumented"]}`
  - Problem: The matrix sets real cases side by side. A "yes" cell gives Strider, a named system of his, a property no filed unit records. A reader on a phone sees it as a fact. The prose labels it hypothetical, so I judged this a should-fix and not a breach. The caller may escalate it.
  - Fix: `{"label": "Strider", "cells": ["undocumented", "undocumented", "undocumented"]}`
  - Basis: brief; no filed unit documents Strider (grep of `courses/brand-ai/`).
- [should-fix | figure] §3, matrix caption (same cause)
  - Current: `Strider's row is the hypothetical stated in §3, since no filed unit documents it.`
  - Fix: `Strider's row is undocumented in every cell, since no filed unit documents it; §3 works it only as a hypothetical.`
  - Basis: as above.
- [minor | label] §3 Strider, prose (same cause)
  - Current: `Worked as a hypothetical, then: an agent of his own design that runs many steps on its own, may split work across sub-agents, and reads the web. The questions the Deliverable would put to it:`
  - Fix: `Worked as a hypothetical, then, with every property assumed for the exercise and none taken from his system: an agent that runs many steps on its own, may split work across sub-agents, and reads the web. The questions the Deliverable would put to it:`
  - Basis: as above.
- [minor | accuracy] §3 AIssistant, consequence 1
  - Current: `Nothing in this course's evidence measures a DeepSeek model as an agent; B2 records DeepSeek's prices only.`
  - Problem: B2 also records DeepSeek's window, its effort control and an Artificial Analysis index score (§4, §5).
  - Fix: `Nothing in this course's evidence measures a DeepSeek model as an agent; B2 records DeepSeek's prices, window, effort setting and one composite index score (B2 §4, §5).`
  - Basis: B2 lines 103–114 and 145.
- [minor | label] §3 AIssistant, consequence 2
  - Current: `2. **Two legs of the trifecta are documented.**`
  - Problem: Only the private-data leg is documented. The way-out leg is the unit's own reading, which the next sentences say.
  - Fix: `2. **One leg of the trifecta is documented and a second is likely.**`
  - Basis: B5 §5; the unit's own "(my reading …)".
- [minor | attribution] §3 pcblueprint
  - Current: `Its endpoints, hosting, network exposure and test coverage are not documented in any filed unit (B5, unsure item 7).`
  - Problem: B5's unsure item 7 names endpoints, hosting and network exposure. It does not name tests.
  - Fix: `Its endpoints, hosting and network exposure are not documented in any filed unit (B5, unsure item 7), and no filed unit mentions its tests.`
  - Basis: B5 unsure item 7.
- [minor | accuracy] §2 "Stated boundaries are not rules"
  - Current: `because a hook's matching filter is best-effort`
  - Problem: The page says this of the Bash `if` filter specifically: "Because the `if` filter is best-effort, use the permission system rather than a hook …".
  - Fix: ``because a hook's `if` filter on Bash commands is best-effort``
  - Basis: https://code.claude.com/docs/en/hooks?frame=0
- [minor | figure] §5 Cost blowups
  - Current: ``A `/batch` of 5 to 30 subagents pays 5 to 30 times.``
  - Problem: No baseline is given. Each subagent's spend depends on its task.
  - Fix: ``A `/batch` of 5 to 30 subagents pays for 5 to 30 sets of requests on top of the session's own.``
  - Basis: *Subagents* ("each subagent spends tokens of its own while it runs").
- [minor | figure] §2, after the `vault-finder` block
  - Current: `B8 §2 counted the 17 filed units at about 360,600 tokens, and the subagent reads them in its own window.`
  - Problem: The attribution to B8 is correct, but the count is now stale. There are 20 filed units, 1,146,855 characters.
  - Fix: `B8 §2 counted the 17 filed units at about 360,600 tokens on 2 November 2026; there are now 20, about 424,800 tokens by the same rule (my count of 1,146,855 characters at B1 §2's 2.7 a token), and the subagent reads them in its own window.`
  - Basis: script count of `courses/brand-ai/*.md`.
- [minor | attribution] Writer's unsure list, item 2
  - Current: `2. **Hadfield et al.'s 4×, 15× and 90.2%** are Anthropic's figures for its 2025 research system (Opus 4 lead, Sonnet 4 subagents), from an internal evaluation with no published method;`
  - Problem: The post ties the Opus 4 lead with Sonnet 4 subagents to the 90.2% figure. It does not say which configuration the token ratios come from, as B6's unsure item 2 notes.
  - Fix: `2. **Hadfield et al.'s 4×, 15× and 90.2%** are Anthropic's figures for its 2025 research system; the 90.2% is for an Opus 4 lead with Sonnet 4 subagents, and the post does not say which configuration the token ratios come from (B6 unsure item 2); all three rest on internal evaluation with no published method;`
  - Basis: https://www.anthropic.com/engineering/multi-agent-research-system ; B6 unsure item 2.
- [minor | accuracy] Writer's unsure list, item 8
  - Current: ``8. **Building effective agents** was opened at its `/research/` address, while DD-B3 cites the `/engineering/` address; the page shows a modification on 9 October 2026, so DD-B3's quotations of the workflow and agent definitions, used in §1, were not re-checked on the copy opened.``
  - Problem: Both definitions are on the `/research/` copy, word for word, so the item can be closed.
  - Fix: ``8. **Building effective agents** was opened at its `/research/` address, while DD-B3 cites the `/engineering/` address; the page shows a modification on 9 October 2026. The workflow and agent definitions used in §1, as DD-B3 quotes them, are on the copy opened (fresh check, 2 Nov 2026).``
  - Basis: https://www.anthropic.com/research/building-effective-agents
- [minor | style] §8 B7, "Fanning out"
  - Current: `The model's minutes are not the constraint; his checks are, and they sit in A3's Tuesday and Wednesday slots either way (B7, Hours).`
  - Problem: This is a "not X but Y" construction, which the brief excludes.
  - Fix: `His checks are the constraint, and they sit in A3's Tuesday and Wednesday slots however fast the drafts arrive (B7, Hours).`
  - Basis: brief, Tone.
- [minor | accuracy] §8 Rule (B7)
  - Current: `**Rule (B7).** No agent runs B7's steps beyond B5's weekly step-2 task,`
  - Problem: B5's step 2 is the journal entry. B7's step 2 is the record, so the two numberings collide.
  - Fix: `**Rule (B7).** No agent runs any of B7's numbered steps; the chain's one unattended run stays B5's weekly journal-entry task (B5's step 2),`
  - Basis: B5 §4 and §D; B7 Deliverable A, steps 1 and 2.

**Against another filed unit**
- [minor | coverage] `/home/claude/learning/courses/brand-ai/B5-skills-and-automation.md` §5 pcblueprint
  - Current: `Override if: DD-B1, which owns agents, recommends a connector with a reasoned threat model; then route 1, with the connector added to chats only, never to the scheduled task.`
  - Problem: The pointer still reads true. DD-B1 now answers it by name, so the open condition can be closed.
  - Fix: `Override if: DD-B1, which owns agents, recommends a connector with a reasoned threat model; then route 1, with the connector added to chats only, never to the scheduled task. (DD-B1 §3, 2 Nov 2026, set out the threat model and does not recommend one; route 3 stands.)`
  - Basis: DD-B1 §3.

**(5) Deliverable.** The Deliverable is present in full: nine boxes, each pointing to its sections, and an "on every path" line. It follows from §1 to §8, apart from two points fixed above: the guard in box 5(d) and the first model for the pcblueprint script against box 6. It can be used alone.

**(6) Errata applied.**
- Audit 1 has no errata for B1 and nothing that touches DD-B1.
- Audit 2's B2 errata changed the Artificial Analysis figures and the 7x figure. DD-B1 uses neither. A grep for the pre-errata values (42/51…, $1.34, "seven times", "10 index points", 36%, 2.8 times) finds none.
- DD-B1 uses B2's Terminal-Bench figures 39.2%, 66.4% and 70.6%. Audit 2 checked these as PASS.
- Erratum A1-1 does not apply.

## (7) Figures
1. **flow, §1, "The autonomy slider in his setup": PASS.**
   - Every label traces to the text:
     - "already runs a short loop"
     - "a lead agent plans and spawns subagents that search in parallel"
     - "file and shell tools on his own repositories"
     - "subagents with their own windows" and "returns only the summary"
     - "runs the same loop with nobody watching"
   - The caption names §1 and every source.
   - A flow suits an ordered sequence of rungs.
2. **matrix, §3, trifecta legs by case: FIX** (the should-fix above).
   - Every other cell traces to the text:
     - "holds one leg only: his takes … no web content and no connector, pushing only to a branch"
     - "could end holding all three legs"
     - "Private data: it uses pcblueprint as a backend" and "A way out: Telegram"
   - Replacement row: `{"label": "Strider", "cells": ["undocumented", "undocumented", "undocumented"]}`. Replacement caption sentence: `Strider's row is undocumented in every cell, since no filed unit documents it; §3 works it only as a hypothetical.`
   - The kind (items by sections) is right.
3. **decision, Deliverable, "Agent or not": PASS.**
   - The nodes match boxes 1, 3, 4, 7 and 8. The outcomes quote the boxes: "stop. Remove one leg", "A chat drafts and he decides", "a chat … Research", "run it in a session he watches".
   - The caption says what is left out (box 2, the check-first branch of box 3, boxes 5, 6 and 9) and names its sources.
   - A decision suits a rule with branches.

## Calculations
- The unit's 360,600 tokens, attributed to B8 §2: 973,729 ÷ 2.7 = 360,640 ✓.
- The vault today: 20 files, 1,146,855 characters ÷ 2.7 = 424,761 tokens. Without DD-B1 it is 19 files, 1,092,027 characters, 404,454 tokens.
- Eleven of fourteen is 78.6%. The current count is fifteen of eighteen, 83.3% (my count).
- Terminal-Bench 4.0: Opus minus Haiku is 27.2 points; Sonnet minus Opus is 4.2 points. Sonnet is ahead of Opus.
- "1,000 lines … to about 100" is a ratio of 10 (as The Decoder reports it).
- The rules are numbered 25 to 28 after B8's 24 ✓.
- "/batch … 5 to 30 times" has no baseline (finding above).
- The unit has no other arithmetic.

## Public-site rules
- **No credential, endpoint, host, IP, port, domain or network detail.** B5's "on his NAS" is omitted, which is correct. "Network exposure" is said to be undocumented.
- **Employer:** not mentioned.
- **Private persons:** none named. Karpathy, Willison, Schluntz, Zhang, Hadfield et al. and McKay are public authors.
- **pcblueprint:** the description matches B5 §5 word for word ("The Protocol", April 2026, 562 and more workouts, three repositories, observed 29 Oct 2026).
- **AIssistant:** matches B5's one line, and the rest is marked undocumented.
- **Strider:** the prose says repeatedly that it is undocumented and hypothetical. The matrix cell "yes (reads the web)" is the one point where an invented property sits next to the real cases. I judged it a should-fix (fix above) and not a breach, because the row is labelled hypothetical.
- **Result:** no error-level breach found.

## Pointers
- **B5 §5 (line 229), override condition.** DD-B1 answers it by name: "This unit does not recommend a connector. B5's route 3, the export file, stands." It gives a four-part threat model: asset, new exposure, inside the chat, gain. The fallback (read-only, aggregate-only, chats only, never a scheduled task) agrees with B5's "chats only, never to the scheduled task". The quotation of B5 is exact. B5's pointer still reads true. A minor finding above closes it.
- **DD-B3 §5 (line 233).** Each item is taken or declined by name in DD-B1 §7's table:
  - autonomy slider: taken
  - verifiability: taken, with "rewardable" made specific
  - autoresearch and its four guards: taken
  - "NEVER STOP": declined and examined
  - five questions: taken, on DD-B3's record, with a note that the page now lacks them
  - OpenAI human intervention: taken
  - lethal trifecta: taken
  - Karpathy's January 2026 failure list: taken

  What DD-B1 attributes to DD-B3 is what DD-B3 says: §1.3, §1.5, §1.6, §1.8, §2.1, §2.2, §2.3 and §2.6; collisions 2, 4 and 6; rules 3, 6 and 7; the O1 card; "irreversible" in the flag; "reverses B2's cost-first order".
  - On the five questions: both copies of the best-practice page returned on 2 Nov lack the list, and lack the "What you can stop doing" table, and both still carry "Manage context aggressively". This confirms the unit's unsure item 1. I cannot check the 29 Oct page, so I make no finding against DD-B3. The Fable stage should re-check DD-B3 §2.1 and card A3.
- **DD-B3's table row "OpenAI agents guide · To DD-B1" and card O1 ("Leaves: the rest to DD-B1").** DD-B1 takes these by name: single agent first, most capable model first, evals, layered guardrails. The guide's own words, on OpenAI's guide page, confirm each quotation. The guide lists "irreversible" inside "high-risk", so DD-B1's choice of the wider term is accurate. Both pointers still read true.
- **B7.** B7 keeps every step in its own chat and ends at step 9. DD-B1 keeps that and adds no agent step. The rule does not contradict B7. Two lines misdescribe B7's step inputs and numbering (findings above). B7 names no DD-B1 pointer.
- **B8.** The added rules are numbered 25 to 28, continuing correctly from rule 24. The added budget row agrees with B8's 4× and 15×. The readings of rules 11, 17 and 19 do not contradict B8, and the quotation of rule 17 is exact. Rule 28 builds on rule 21. B8's pointers still read true. Its own 17-unit count is now stale, but that belongs to B8's own staleness check.
- **Other mentions of DD-B1 in `courses/brand-ai/`:** DD-B3 lines 142, 193, 227, 233 and 351 (all covered above) and B5 line 229. There are no others.

## Confirmed
- *How Claude Code works*:
  - "Tools are what make Claude Code agentic. Without tools, Claude can only respond with text."
  - The three phases, and "decides what each step requires …"
  - "agentic harness"
  - "Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed"
  - https://code.claude.com/docs/en/how-claude-code-works
- *Permission modes*:
  - Six modes, with every quoted cell exact: Reads only; Reads, file edits, and common filesystem commands; plan; auto; dontAsk; bypassPermissions
  - "A separate classifier model reviews actions before they run"
  - "does not guarantee safety …"
  - The boundaries/compaction/deny-rule passage
  - The plan-mode sentence
  - bypassPermissions: "isolated environments like containers, VMs, or dev containers without internet access" and "offers no protection against prompt injection or unintended actions"
  - Non-interactive `-p` runs: "Claude Code doesn't stop the run"
  - https://code.claude.com/docs/en/permission-modes
- *Subagents*: every quotation in §2 items 1 to 6, including:
  - the definition, the own-window passage and "same usage limits"
  - "only this system prompt plus basic environment details"
  - "returns only the summary"
  - the Explore and Plan descriptions, "read-only tools; Write and Edit are denied", general-purpose
  - the allowlist and denylist, the permissionMode override, and the model values including `fable`
  - "lower-cost models like Haiku"
  - `AskUserQuestion` removed from every subagent
  - "up to three layers"
  - when to use the main conversation and when a subagent
  - "each subagent spends tokens of its own"
  - `isolation: worktree`, `.claude/agents/` and `~/.claude/agents/`
  - https://code.claude.com/docs/en/subagents
- *Checkpointing*: all four quoted limits are exact. https://code.claude.com/docs/en/checkpointing
- *Hooks*: "Before a tool call executes. Can block it"; a timed-out hook "doesn't block the tool call"; "use the permission system rather than a hook to enforce a hard allow or deny". https://code.claude.com/docs/en/hooks?frame=0
- *Best practices*, `?r=0` copy: every quotation the unit uses is present on it:
  - the check tip, the "looks done" passage, the fixture-diff check
  - the hooks "advisory/deterministic" line and the migrations-folder hook
  - explore/plan/implement/commit and "describe the diff in one sentence"
  - the subagent investigation tip
  - "Test on a few files…", "first 2-3 files"
  - auto `-p` "doesn't stop the run"
  - the reviewer passage and its callout
  - the trust-then-verify gap
  - "After two failed corrections…"
  - the plan condition for auto
  - https://code.claude.com/docs/en/best-practices?r=0
- Hadfield et al., 13 Jun 2025, six authors:
  - "Agents are stateful and errors compound"; "minor changes cascade…"
  - 4×, 15×, 90.2%, with an Opus 4 lead and Sonnet 4 subagents
  - "breadth-first…"; "not a good fit…"; "fewer truly parallelizable…"
  - "vague enough that subagents misinterpreted the task"; "duplicate work, leave gaps…"
  - Vendor label correct.
  - https://www.anthropic.com/engineering/multi-agent-research-system
- Schluntz and Zhang: published 19 Dec 2024, modified 9 Oct 2026; "higher costs, and the potential for compounding errors"; "sandboxed environments…"; "simplest solution possible…"; "stopping conditions (such as a maximum number of iterations)"; both definitions. https://www.anthropic.com/research/building-effective-agents
- Maginative, Chris McKay, 17 Apr 2025: "begin with single‑agent systems"; "evolve to multi‑agent designs only when complexity demands it"; "when agents repeatedly fail to accomplish tasks"; no mention of evals (confirms unsure item 3). https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/
- OpenAI guide, all five quotations: "maximize a single agent's capabilities first"; "most capable model … baseline"; "Set up evals…"; "a single one is unlikely…"; "Human intervention is a critical safeguard…", with "high-risk actions" covering "sensitive, irreversible, or have high stakes". https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- Willison, 16 Jun 2025: the three legs; "avoid that lethal trifecta combination entirely"; "95% of attacks"; "very much a failing grade". https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Karpathy, *Verifiability*, 17 Nov 2025: "resettable", "efficient", "rewardable … some automated process to reward any specific attempt". https://karpathy.bearblog.dev/verifiability/
- Dwarkesh, 17 Oct 2025: boilerplate; Rust tokenizer from a Python version "I fully understand"; "I have tests so I feel safer". Anecdote label correct. https://dwarkesh.com/p/andrej-karpathy
- The Decoder, 27 Jan 2026: the full failure list as the unit gives it; "watch them like a hawk". https://the-decoder.com/former-tesla-ai-chief-andrej-karpathy-now-codes-mostly-in-english-just-three-months-after-calling-ai-agents-useless/
- karpathy/autoresearch README: the 5-minute keep-or-discard loop; `train.py` "the single file the agent edits"; `prepare.py` not modified; `program.md` a "super lightweight 'skill'". https://github.com/karpathy/autoresearch . "NEVER STOP", "until the human interrupts you, period" and "git reset" are unverifiable (not checked); they agree with DD-B3 §1.6.
- YC talk, "autonomy slider" and "on the leash": unverifiable (not checked). Both agree with DD-B3 §1.3.
- Filed-unit statements checked against the units:
  - B1 §6: "None of these is enforced"
  - B2 §1: "acting as a subagent beside a larger model"; B2 §8: Terminal-Bench and the Sonnet-or-Opus recommendation; B2's Biometrics parsing row
  - B4 §1: Auto, "decides dynamically", On demand; F8 (four copies in three files, still open); F9(e) (two files still name `build_hub.py`); F14; F15 (clones and caches)
  - B5 §4: auto mode at the start of runs, connectors included by default with writes, "draw down subscription usage the same way"; B5 §5: route 1 and the custom-connector quotation, route 3 "run by him or by AIssistant"; B5 §D: branch protection, "at most twice", no connectors, the four guards
  - B6 §1: lead agent and parallel subagents; B6 Deliverable A routing; tier P
  - B7: step 9 final pass; steps 5 to 7 take the final script; Hours
  - B8 §1: one shared limit; Fable on Pro paid in credits at API rates; API credits "don't change your usage limits"; B8 §2: 17 units ≈ 360,600 tokens; rule 17 quotation; rules 11, 19, 21 and 22 as read
  - DD-B3: every section, collision, rule and card cited
  - `kit/verify.py` and `kit/index_check.py` exist
- Front matter: per method §7. Model Opus 5.5 and search off, both matching `hub.ORDER`.

## Verdict
`DD-B1 · verdict fix · 0 errors, 10 should-fix, 14 minor`. Against other filed units: B5 has 1 minor.

**Maintainer's note (2 Nov 2026, the orchestrating chat of row B-13).** The checker's transcript was checked by script: no memory, Projects, past-chat, connector, Artifact or `mcp__*` tool; all 19 WebFetch calls on URLs a WebSearch in its own context had returned, copied exactly; no redirect met (one script hit on the word "redirect" was the fetch summary saying the page was not redirected); nothing opened under the writer's packet, its hand-back or any agent transcript. Every finding was verified before it was applied, each as an exact replacement whose Current occurred once in its file (Python `str.count`), all 25 by one script reading the pairs from this report. How each was verified:

- Findings 1 and 2 (auto mode as the starting mode): a search returned `code.claude.com/docs/en/best-practices.md` and `permission-modes?embedable=true`; both fetched read "With Claude Code v2.1.283 or later, auto mode is the built-in starting permission mode for interactive terminal and VS Code sessions … On earlier versions, … only on Pro, Max, and Team plans." Applied as given.
- Findings 8, 9 and 10 (`--allowedTools`): the same best-practice fetch reads "The `--allowedTools` flag pre-approves the tools the migration needs, and `--permission-mode dontAsk` denies anything else that would need approval"; the permission-modes fetch gives dontAsk as "anything that would prompt is denied". Applied as given.
- Finding 11 (`/batch`): the same fetch reads "Each subagent works in its own worktree." with no pull request. Applied as given.
- Finding 18 (hooks): a search returned `code.claude.com/docs/en/hooks`; the fetch reads "Because the `if` filter is best-effort, use the permission system rather than a hook to enforce a hard allow or deny", in the section on how `if` patterns match Bash commands. Applied as given.
- Finding 21 (Hadfield et al.): a search returned `anthropic.com/engineering/multi-agent-research-system`; the fetch ties the 90.2% to an Opus 4 lead with Sonnet 4 subagents and gives the 4× and 15× with no configuration; B6's unsure item 2 says the same. Applied as given.
- Finding 22 (Building effective agents): a search returned `anthropic.com/research/building-effective-agents`; the fetch carries both definitions as DD-B3 quotes them, published 19 Dec 2024, modified 9 Oct 2026. Applied as given.
- Findings 3 and 20 (counts): re-run by script on the vault. Eighteen filed units before DD-B1 carry a fresh-check line (B1 has none); fifteen had at least one error; A3, A7 and B4 had none; seven checks ran on Opus 5.5 (A5, A7, A8, B6, B7, B8, DD-A1). The vault is 20 files, 1,146,855 characters, 424,761 tokens at 2.7 a token. Applied as given.
- Findings 4 to 7, 15 to 17, 19, 23 and 24 (against filed units): each read in the unit cited. B8 rule 22 (line 251) keeps health numbers out of memory and Projects and does not say "nowhere else", and B8 §5's table (line 197) lets "Change only, from the publish list" reach the public build. B2's Biometrics-parsing row (line 323) gives Haiku 5.5 and the Sonnet fallback, while DD-B1's box 6 starts a new loop on Opus 5.5, so the two disagreed. B2 §1 (line 29) records the model page's advice to start with Opus 5.5 when unsure, and B2 §8 (line 254) reads Sonnet and Opus as level. B7 Deliverable A gives step 4 as his frame and edit with no model, steps 5 to 7 as taking the final script, and step 8 as taking the entry and the record. B2 records DeepSeek's window, effort control and one index score (lines 103 to 145). B5's unsure item 7 names endpoints, hosting and network exposure, with no tests. B5's step 2 is the journal entry (line 172). Finding 23 is a "not X but Y" construction the brief excludes. All applied as given.
- Findings 12 to 14 (Strider in the matrix): no filed unit documents Strider (grep of `courses/brand-ai/`), and a "yes" cell beside real cases reads as fact. Applied as given; the figure goes to a re-check (below).
- Finding 25 (B5 §5's override): DD-B1 §3 answers it by name and does not recommend a connector. Applied as given to B5.
- **Same cause, applied by the maintainer:** DD-B1's unsure item 7 repeated finding 17's attribution ("pcblueprint's test coverage and network exposure are undocumented (B5 unsure item 7)"). It now reads that its network exposure is undocumented (B5 unsure item 7) and no filed unit mentions its tests.
- **Dated note to another filed unit:** DD-B1's unsure item 1 and this check found that the best-practice page as read on 2 November no longer shows the five questions or the "What you can stop doing" table that DD-B3 §2.1 recorded on 29 October, and still carries "Manage context aggressively". The fetch above confirmed this (the Markdown copy carries neither the list nor the table, and leads with "Give Claude a check it can run"). DD-B3 §2.1 now carries a dated note pointing to DD-B1 §7. Its record of 29 October stands; the Fable stage re-checks it with DD-B3 (P49).
- **Pointers read again:** B5 §5 (now closed by name), DD-B3 §5's DD-B1 paragraph, DD-B3's table row and O1 card, B7 and B8: each reads true with DD-B1 filed. No other filed unit names DD-B1.


## Figure re-check 1 (2 Nov 2026, a separate Opus 5.5 agent given the unit without its figures, the captions and figure 2's frames sheets at phone, tablet and desktop, dark and light; report verbatim)

Figure 2 re-check (matrix, §3, after §3's "Strider" and "For comparison" paragraphs, line 131 of unit-without-figures.md). All six frame sheets opened. The kind fits the data: four cases by three trifecta legs is a matrix.

Traced to the text:
- Column heads `PRIVATE DATA` / `UNTRUSTED CONTENT` / `CAN SEND OR PUBLISH` come from l.100: "private data, exposure to untrusted content and the ability to communicate externally", and from box 1 (l.255): "a way to send, publish or post". OK.
- Row `B5 weekly scheduled task` = `yes (takes)` / `no` / `no (own branch)` comes from l.129: "B5's weekly scheduled task holds one leg only: his takes, which are private drafts (B8 §5), with no web content and no connector, pushing only to a branch in his private repository (B5 §4 and §D)". OK.
- Row `pcblueprint connector (route 1), chat with search and a send connector` = `yes` ×3 comes from l.99–100: "Route 1 means writing an MCP wrapper…"; "His account has web search and connectors that can send or publish (DD-B3 §4, collision 6, from B4 F14)"; "A chat that began as a question about pace could end holding all three legs." OK.
- Row `AIssistant` = `yes (pcblueprint)` / `undocumented` / `yes (Telegram)` comes from l.112: "Private data: it uses pcblueprint as a backend. A way out: Telegram is a messaging service… The third leg, untrusted content, is undocumented". OK, but see item 1.
- Row `Strider` = `undocumented` ×3 comes from l.117: "No filed unit documents it: not what it does, … what tools or data it holds". OK. The earlier problem is fixed, and the caption now matches.
- Caption: the date "16 Jun 2025" and "DD-B3 §2.3" match l.100. "B5 §4 and §D" matches l.129. "B5 §5" matches l.99 and l.107. "B4 §1" is in l.100. The caption says what the figure shows and names §3.
- Rendering: on desktop and tablet, in both themes, the whole figure fits in one frame. Text sits inside its boxes, nothing overlaps, the caption is under the figure, and the row labels are readable. On phone, in both themes, it takes 3 frames of sideways scroll with a "scroll sideways for the whole figure" hint. The caption is under the figure and nothing overlaps.

Findings:

1. [minor] [figure] AIssistant row, third cell. Current: `yes (Telegram)`. Problem: the text hedges this leg. Its heading reads "One leg of the trifecta is documented and a second is likely" and it calls the Telegram leg "my reading of Willison's 'externally communicate'". The cell states it as a plain yes, in the same form as the documented `yes (pcblueprint)`. The caption says so ("Telegram counted as a way out is this unit's reading"), but a reader scanning the cell does not see that. Fix: cell text `likely (Telegram)`.

2. [minor] [figure] Cell colours. Current: in row 2 the three `yes` cells are red. In row 1, `yes (takes)` is the neutral blue-grey, and the `no` cells are green. In the AIssistant row, `yes (pcblueprint)` and `yes (Telegram)` are the same blue-grey as `undocumented`. Problem: colour seems to mark the whole row (all three legs held = red), not each cell's value, and the caption does not say so. A reader who reads colour per cell will see AIssistant's two yes cells as the same kind of cell as "undocumented". Fix: either colour by value (one tint for yes, green for no, neutral for undocumented), or add to the caption: `Red marks a case that holds all three legs; green marks a leg that is absent.`

3. [minor] [figure] Caption sources. Current: `the B5 task from B5 §4 and §D; route 1 and AIssistant from B5 §5, with the connector-loading rule from B4 §1;`. Problem: the caption leaves out three sources the figure's cells rest on in the text:
   - "takes" as private data rests on B8 §5 (l.129).
   - The "search and a send connector" in the route-1 row rests on DD-B3 §4, collision 6, from B4 F14 (l.100).
   - l.100 cites the connector-loading rule as "B4 §1 and §3", not only §1.

   Fix: `the B5 task from B5 §4 and §D, its takes as private data from B8 §5; route 1 and AIssistant from B5 §5, the account's search and send connectors from DD-B3 §4 (collision 6, from B4 F14), and the connector-loading rule from B4 §1 and §3;`

4. [minor] [figure] Phone width, frames 2 and 3, both themes. Current: when scrolled, the row-label column leaves the view. Frame 2 shows only the fragments `1), chat` / `ector`, and frame 3 shows no row labels, so the third column (`CAN SEND OR PUBLISH`) is never on screen with the case it belongs to. Problem: the row labels are readable only in frame 1. A phone reader has to remember the row order to read the send leg. Fix: make the row-label column sticky at phone width, or shorten the row-2 label (e.g. `Route 1 chat (pcblueprint connector, search, send connector)`) so more of the cells fit beside it. Either way, a style change goes through theme.css, not ad hoc.

5. [minor] [text] §3, l.86. Current: `The filed units say little about the three, and this section says no more than they do.` Problem: the section, and the figure built from it, go beyond the filed units in places it labels itself: "my reading of Willison's…" (l.112), "my rule, from those two" (l.94), "my rule, from the threat model above" (l.103), and the Strider hypothetical. The opening sentence says it does not. Fix: `The filed units say little about the three; this section adds nothing to them except what it marks as its own reading or rule, and a hypothetical for Strider.`

No errors: every label and the date in the figure trace to §3's text, and nothing a reader sees contradicts it.

Figure 2 (matrix, §3): PASS (0 errors, 0 should-fix, 5 minor: 4 figure, 1 text)

**Maintainer's note on the figure re-check (2 Nov 2026).** The re-checker's transcript was checked by script: no web, memory, Projects, connector or Artifact tool; every file it opened inside its packet. Figure 2 passed (0 errors, 0 should-fix, 5 minor). Each minor was verified against the unit and the desktop shot before it was applied as an exact replacement: (1) the AIssistant send cell now reads "likely (Telegram)", since §3 heads the leg as likely and calls it its own reading; (2) the shot shows the AIssistant "yes" cells in the same neutral tint as "undocumented" and only the route-1 row in red, so the caption now says "Red marks a case that holds all three legs; green marks a leg that is absent"; (3) the caption now names B8 §5 (takes as private data), DD-B3 §4 collision 6 from B4 F14 (the account's search and send connectors) and B4 §1 and §3, as §3's text cites them; (5) §3's opening sentence now says the section adds to the filed units only what it marks as its own reading or rule, and a hypothetical for Strider. Minor 4 (the row labels scroll out of view at 390 px) is the renderer change already queued as P83 (a sticky label column for a matrix at phone width), a proposed row awaiting Pedro's confirmation; it is recorded there, no new row. Separately, at filing the flow figure (figure 1) was set to two boxes a row (`per_row: 2`, layout only, no label changed) so it fits a phone column without sideways scrolling. Figures 1 (flow) and 3 (decision) passed the fresh check; figure 2 (matrix) was fixed and passed its re-check. None dropped.
