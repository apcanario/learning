---
code: DD-B1
title: Deep dive: agents
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-11-02
search: off
---

# DD-B1 · Deep dive: agents

Search was off for this unit. It was used only to check Claude Code's documented behaviour (the agent loop, subagents, checkpoints, permission modes, hooks and the best-practice page), the wording of two Anthropic engineering posts, and one report of OpenAI's agent guide. Every page was found by a web search and opened on 2 November 2026 at the address the search returned; product facts carry that date. Evidence is labelled where it appears: **product documentation** (Anthropic's Claude Code pages), **vendor** (Anthropic's or OpenAI's engineering advice and internal figures, with no published method), **anecdote** (a practitioner's account of his own work), and **his setup** (what the filed units record). Sources that DD-B3 opened on 29 October 2026 and this unit did not re-open are cited "via DD-B3".

**Interests.** This unit was written by an Anthropic model, and most of its product sources are Anthropic's own pages: a vendor describing its product. Nothing was weighted to favour them; the reader should still know.

What a context window is and why every turn re-sends the history is B1; model and effort routing is B2; brief structure is B3; skills, scheduled tasks and pcblueprint's routes are B5; the sampling rule is B6; the content pipeline is B7; usage limits and privacy are B8; the practitioners' methods, graded, are DD-B3. This unit points back by number.

## 1 · What an agent is, and where a chat ends

**Tools in a loop.** Anthropic's Claude Code documentation draws the line in two sentences: "Tools are what make Claude Code agentic. Without tools, Claude can only respond with text." Given a task, Claude works through three phases, "gather context, take action, and verify results", and "decides what each step requires based on what it learned from the previous step, chaining dozens of actions together and course-correcting along the way" ([Claude Code docs, *How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works), read 2 Nov 2026; product documentation). The layer around the model that supplies the tools and manages what the model sees is what the page calls the "agentic harness". Anthropic's engineering post of December 2024 makes the same cut from the builder's side: workflows are "systems where LLMs and tools are orchestrated through predefined code paths"; agents are systems where "LLMs dynamically direct their own processes and tool usage" (Schluntz and Zhang, as DD-B3 §2.1 quotes them; vendor).

Three things separate an agent from the chat B1 described:

- **Tools.** The model can read and change things outside the window: files, commands, the web, connected services.
- **A loop.** Each tool result goes back into the window and decides the next step, so the number of steps is not fixed in advance.
- **Autonomy.** The model chooses each next step, and how much of that happens without his approval is a setting.

**The line is graded.** A claude.ai chat with web search already runs a short loop: it searches, reads what comes back and decides whether to search again, the reasoning-and-acting pattern DD-B3 §2.6 records as ReAct. Research on claude.ai is a multi-agent system: a lead agent plans and spawns subagents that search in parallel (B6 §1, citing Hadfield et al., 13 Jun 2025; vendor). Claude Code adds file and shell tools on his own repositories, and subagents with their own windows (§2). A scheduled task runs the same loop with nobody watching (B5 §4). Karpathy's name for the dial is the autonomy slider: in Cursor "you are in charge of the autonomy slider", from tab completion to whole-repository changes, and his advice is to keep the AI "on the leash" in small increments a human can verify ([YC AI Startup School talk, 17 Jun 2025](https://www.youtube.com/watch?v=LCEmiRjPEtQ), via a [third-party transcription](https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html), as DD-B3 §1.3 quotes it; stated opinion).

```viz
{"kind": "flow", "title": "The autonomy slider in his setup", "steps": [{"label": "Chat", "note": "one reply, no tools", "tone": 3}, {"label": "Chat with search", "note": "a short search loop", "tone": 3}, {"label": "Research", "note": "a lead agent and parallel subagents", "tone": 2}, {"label": "Claude Code session", "note": "file and shell tools on his repositories", "tone": 2}, {"label": "Subagents", "note": "their own windows; return a summary", "tone": 4}, {"label": "Scheduled task", "note": "runs with nobody watching", "tone": 1}], "caption": "The rungs from a chat to an unattended agent, in the order of §1 of this unit: ReAct as DD-B3 §2.6 records it; Research from B6 §1 (Hadfield et al., Anthropic Engineering, 13 Jun 2025); Claude Code and subagents from <a href=\"https://code.claude.com/docs/en/how-claude-code-works\">Claude Code docs, <em>How Claude Code works</em></a> and <a href=\"https://code.claude.com/docs/en/subagents\"><em>Subagents</em></a>, read 2 Nov 2026; scheduled tasks from B5 §4. The slider is Karpathy's term (YC talk, 17 Jun 2025, via DD-B3 §1.3)."}
```

**What the extra rungs cost.** Two properties change when a loop replaces a reply. Errors compound: Anthropic's engineering team, describing its research system, wrote "Agents are stateful and errors compound", and that "minor changes cascade into large behavioral changes" ([Hadfield et al., *How we built our multi-agent research system*, Anthropic Engineering, 13 Jun 2025](https://www.anthropic.com/engineering/multi-agent-research-system), read 2 Nov 2026; vendor). And cost multiplies: the same post measured agents at "about 4× more tokens than chat interactions" and multi-agent systems at "about 15× more tokens than chats" (vendor, measured on Anthropic's 2025 systems; whether the ratios hold for the 5.5 family is not stated anywhere read, B6 unsure item 2). Anthropic's agent post puts both in one sentence, "The autonomous nature of agents means higher costs, and the potential for compounding errors", and recommends "extensive testing in sandboxed environments, along with the appropriate guardrails" ([Schluntz and Zhang, *Building effective agents*, Anthropic, 19 Dec 2024](https://www.anthropic.com/research/building-effective-agents), read 2 Nov 2026; vendor). Its default is "finding the simplest solution possible, and only increasing complexity when needed" (same post). The rest of this unit is about when a higher rung pays for itself.

## 2 · Claude Code and subagents in practice

### What runs without asking

In Claude Code the autonomy slider is the permission mode. As of 2 November 2026 the documentation lists six ([Claude Code docs, *Permission modes*](https://code.claude.com/docs/en/permission-modes); product documentation):

| Mode | "What runs without asking" | "Best for" |
|---|---|---|
| `default` (Manual) | "Reads only" | "Reviewing every action yourself, sensitive work" |
| `acceptEdits` | "Reads, file edits, and common filesystem commands" | "Iterating on code you're reviewing" |
| `plan` | "Reads, plus classifier-approved commands when auto mode is available" | "Exploring a codebase before changing it" |
| `auto` | "Everything, with background safety checks" | "Long tasks, reducing prompt fatigue" |
| `dontAsk` | Reads in the working directories and pre-approved tools; "anything that would prompt is denied" | "Locked-down CI and scripts" |
| `bypassPermissions` | "Everything" | "Isolated containers and VMs only" |

Three facts about the modes bear on him directly.

**The starting rung is high.** Auto mode is "the built-in starting permission mode for interactive terminal and VS Code sessions" with Claude Code v2.1.283 or later, and on earlier versions only on Pro, Max and Team plans (*How Claude Code works*; *Permission modes*, "Which mode a session starts in"; the copy of the best-practice page opened at [best-practices?r=0](https://code.claude.com/docs/en/best-practices?r=0) on 2 Nov 2026 gives the plan condition alone); B5 §4 recorded that scheduled tasks start in it too. In auto mode "A separate classifier model reviews actions before they run", and the page's own caveat is that it "reduces permission prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations" (*Permission modes*).

**Stated boundaries are not rules.** In auto mode, boundaries stated in the chat "are not stored as rules. The classifier re-reads them from the transcript on each check, so a boundary can be lost if context compaction removes the message that stated it. For a hard guarantee, add a deny rule instead" (*Permission modes*). That is B1 §6's "None of these is enforced", applied to agents. The best-practice page says the same of hooks: "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens" (*Best practices*). A `PreToolUse` hook runs "Before a tool call executes. Can block it"; the hooks page also warns that a hook that times out "doesn't block the tool call", and, because a hook's `if` filter on Bash commands is best-effort, advises to "use the permission system rather than a hook to enforce a hard allow or deny" ([Claude Code docs, *Hooks*](https://code.claude.com/docs/en/hooks?frame=0), read 2 Nov 2026).

**Plan mode still runs commands.** "Plan mode tells Claude to research and propose changes without making them. Claude reads files, runs shell commands to explore, and writes a plan, but does not edit your source" until the plan is approved (*Permission modes*). It holds back edits to source files; it does not hold back every command.

### Subagents

The documentation defines subagents as "specialized AI assistants that handle specific types of tasks": "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions. It also sends its own requests, which count toward the same usage limits as your main conversation." It receives "only this system prompt plus basic environment details like the working directory", does its work in its own window "and returns only the summary" ([Claude Code docs, *Subagents*](https://code.claude.com/docs/en/subagents), read 2 Nov 2026; product documentation). Six facts from that page decide how he uses them.

1. **Built-ins.** Explore, "A fast, read-only agent optimized for searching and analyzing codebases", and Plan, used to gather context in plan mode, both have "read-only tools; Write and Edit are denied". The general-purpose subagent has "every tool available to subagents".
2. **The tool list is the scope that holds.** `tools` is an allowlist and `disallowedTools` a denylist. `permissionMode` is weaker: "When the main conversation is in `bypassPermissions`, `acceptEdits`, or auto mode, the subagent runs in that same mode and Claude Code ignores the `permissionMode` you set."
3. **Model per subagent.** `model` takes `sonnet`, `opus`, `haiku`, `fable`, a full model ID or `inherit`; the page's own cost advice is routing tasks "to faster, lower-cost models like Haiku".
4. **They cannot ask him.** `AskUserQuestion`, the tool by which Claude asks the user a question, is on the page's list of tools removed from every subagent, whatever its `tools` field says. A subagent that meets an ambiguity has two moves: guess, or stop and report. Anthropic's research post records what the first looks like: early instructions to subagents "often were vague enough that subagents misinterpreted the task", and "Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information" (Hadfield et al.; vendor).
5. **Depth and fan-out.** "By default, a subagent can spawn subagents of its own, up to three layers below the main conversation." The best-practice page documents `/batch`, which splits a change "across 5 to 30 subagents. Each subagent works in its own worktree" (*Best practices*; the copy opened adds "and opens a pull request", a later copy the same day does not). Each sends its own requests.
6. **When to use one.** The main conversation when "Multiple phases share significant context, such as planning, implementation, and testing", for "a quick, targeted change", or when the task needs back-and-forth. A subagent when the task "produces verbose output you don't need in your main context", when tool restrictions are wanted, or when "The work is self-contained and can return a summary".

A subagent is defined by a Markdown file in the repository's `.claude/agents/` (or `~/.claude/agents/` for every project) with front matter, the same pattern as a skill (B5 §1). One for his course repository, built only from the fields above:

```
---
name: vault-finder
description: Finds which filed units state a given claim or cite a given source, and returns unit, section and sentence. Read-only. Use before writing or auditing a unit that points back to earlier units.
tools: Read, Grep, Glob
model: haiku
---
Search courses/brand-ai/ for the claim or source named in the request. For each match return: the file, the section heading, the sentence, and the link it cites. Change nothing. If nothing matches, say "no match" and list the search terms tried.
```

Haiku, because the job is extraction, the work Anthropic positions Haiku 5.5 for, including "acting as a subagent beside a larger model" (B2 §1); read-only by its tool list; a stop line ("no match"), because it cannot ask. What it saves is the main window: B8 §2 counted the 17 filed units at about 360,600 tokens on 2 November 2026; there are now 20, about 424,800 tokens by the same rule (my count of 1,146,855 characters at B1 §2's 2.7 a token), and the subagent reads them in its own window. What it does not save is usage, since its requests "count toward the same usage limits". B8's rule 17 ("I read sections, never the whole vault") still binds; the subagent is how a session keeps it.

**The interactive sequence.** For a change he cannot describe in one line, the documented order is explore, plan, implement, commit, with plan mode first, and one escape: "If you could describe the diff in one sentence, skip the plan" (*Best practices*). The page's first rule is a check: "Give Claude a check it can run: tests, a build, a screenshot to compare. It's the difference between a session you watch and one you walk away from" (same page).

## 3 · His cases: pcblueprint, AIssistant, Strider

The filed units say little about the three, and this section says no more than they do.

### pcblueprint

B5 §5 describes it: his own data infrastructure ("The Protocol"), built in April 2026; a REST API serving his workouts (562 and more), biometrics and biographical archive, across three repositories (archive, website, Android app) (B5 §5, from his claude.ai session of 29 Oct 2026; his setup, observed). Its endpoints, hosting and network exposure are not documented in any filed unit (B5, unsure item 7), and no filed unit mentions its tests.

Two kinds of agent work touch it, and they get different answers.

**Agents working on its code.** A change to one of its repositories is the work Claude Code is built for, on one condition: a check that returns pass or fail (§2). Whether its repositories have tests is not documented, so the order is a test first, then the change. For B5's export script the check is a fixture: a past fortnight's figures, written out once, against which the script's output is diffed; the best-practice page names "a script that diffs output against a fixture" as a check (*Best practices*). Two rules from B8 bound the session. A Claude Code session is a chat on Anthropic's servers under the retention rules of B8 §5, and health numbers belong in the private vault, never in memory or a Project (B8 rule 22; B8 §5's table lets only changes from the publish list reach the public build). So a session on pcblueprint's code works against fixtures and does not read the archive itself (my rule, from those two). B2's routing table gives the script to Haiku 5.5 ("Haiku 5.5 writes and maintains the parsing script; the script does the parsing"), with Sonnet 5.5 after the script breaks twice on a new export format (B2, Biometrics parsing). Run as a Claude Code loop against a fixture, its first version is a new loop in box 6's sense, so it is written on Opus 5.5 with the fixture check and handed to B2's models for maintenance once the check passes on repeat runs (my rule, reconciling B2 with §7).

**Agents reading its data: the connector question B5 left here.** B5 §5 picked an export file (route 3) and wrote: "Override if: DD-B1, which owns agents, recommends a connector with a reasoned threat model; then route 1, with the connector added to chats only, never to the scheduled task." **This unit does not recommend a connector. B5's route 3, the export file, stands.** The threat model:

- *Asset.* His biometric and biographical archive (B5 §5).
- *New exposure.* Route 1 means writing an MCP wrapper around the REST API and making it reachable from the public internet, since a custom connector "must be reachable over the public internet from Anthropic's IP ranges" (B5 §5, citing the help centre's custom-connector page). The archive gains an internet-facing entry point built for this purpose; the export route needs none.
- *Inside the chat.* A chat holding the connector holds private data. Willison's lethal trifecta is private data, exposure to untrusted content and the ability to communicate externally in one agent, and his advice is to "avoid that lethal trifecta combination entirely", because guardrails that catch "95% of attacks" are "very much a failing grade" ([Willison, *The lethal trifecta for AI agents*, 16 Jun 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), via DD-B3 §2.3; stated opinion). His account has web search and connectors that can send or publish (DD-B3 §4, collision 6, from B4 F14). Under "Auto" tool access "Claude decides dynamically which connectors to load", and under "On demand" a connector loads when searched (B4 §1 and §3, citing Anthropic's tool-access article). Which connectors share a chat is therefore settled during the chat, by the model. A chat that began as a question about pace could end holding all three legs.
- *Gain.* None the export file lacks. The numbers come from code either way (B2, Biometrics parsing; B1 §5), and the export file records exactly which numbers an episode used (B5 §5).

Exposure with no gain decides it. If a need appears that a fixed export cannot meet, such as a question across the whole archive, the order is a second export script first; a connector only with read-only, aggregate-only access, in a chat with web search off and no other connector, and never in a scheduled task (my rule, from the threat model above).

### AIssistant

B5 §5 records one line about it: a personal agent built on DeepSeek and Telegram that already uses pcblueprint as a backend (observed, 29 Oct 2026); and B5's route 3 has the export script "run by him or by AIssistant". Everything else is not documented: its tools, what it reads, who can message it, whether it acts without his approval, what it costs.

Three consequences follow from that line alone.

1. **None of Claude Code's guards apply to it.** Permission modes, deny rules, hooks and checkpoints are features of Claude Code (§2). An agent built on another vendor's model and his own code has the guards its code has, and no others. Nothing in this course's evidence measures a DeepSeek model as an agent; B2 records DeepSeek's prices, window, effort setting and one composite index score (B2 §4, §5).
2. **One leg of the trifecta is documented and a second is likely.** Private data: it uses pcblueprint as a backend. A way out: Telegram is a messaging service, and an agent that can send messages can send them somewhere (my reading of Willison's "externally communicate"). The third leg, untrusted content, is undocumented: whether it reads web pages, forwarded messages, or messages from anyone but him. If it does, it holds all three, and the Deliverable's box 1 applies: one leg comes off.
3. **For the export, its model chooses nothing.** B2's rule is that numbers come from code. When AIssistant runs the export, it runs the fixed script and writes the file; it does not compose, select or summarise the numbers.

### Strider

The brief names Strider as one of his cases. No filed unit documents it: not what it does, which models it runs on, what tools or data it holds, whether it runs unattended, whether it is built on the API, or what it has cost. Nothing about it is stated here as fact.

Worked as a hypothetical, then, with every property assumed for the exercise and none taken from his system: an agent that runs many steps on its own, may split work across sub-agents, and reads the web. The questions the Deliverable would put to it:

- **Trifecta.** Reading the web is untrusted content. If it also holds private data and any way to send or publish, one leg comes off before it runs again.
- **Check.** What returns pass or fail on its output? If its output is a judgement no script can score, it fails Karpathy's "rewardable" (§4, §7), and it drafts for him to decide; autonomy does not turn its verdicts into checked results.
- **Cost.** If it is multi-agent, Anthropic's figure for its own system is about 15 times a chat's tokens (Hadfield et al.; vendor, 2025). If it runs on the API, it is billed per token at B2 §3's prices, and B8 §1 records the API and the plan's limits as separate meters (the monthly API credits "don't change your usage limits"); on that reading no plan limit stops it, and its stop has to be in its own code, "a maximum number of iterations" being Anthropic's example of a stopping condition (*Building effective agents*).
- **Model.** Most capable first, then smaller while the check still passes (§7, box 6).
- **Unattended.** If it runs while he is not watching, the gate in §6 and box 8 applies in full.

For Strider to be worked for real, he would write down the answer to each line above. Until then it is the one case in this unit with no evidence behind it.

For comparison, B5's weekly scheduled task holds one leg only: his takes, which are private drafts (B8 §5), with no web content and no connector, pushing only to a branch in his private repository (B5 §4 and §D).

```viz
{"kind": "matrix", "cols": ["Private data", "Untrusted content", "Can send or publish"], "rows": [{"label": "B5 weekly scheduled task", "cells": [{"mark": "yes (takes)", "tone": 4}, {"mark": "no", "tone": 3}, {"mark": "no (own branch)", "tone": 3}]}, {"label": "pcblueprint connector (route 1), chat with search and a send connector", "tone": 1, "cells": [{"mark": "yes", "tone": 1}, {"mark": "yes", "tone": 1}, {"mark": "yes", "tone": 1}]}, {"label": "AIssistant", "cells": [{"mark": "yes (pcblueprint)", "tone": 4}, "undocumented", {"mark": "yes (Telegram)", "tone": 4}]}, {"label": "Strider", "cells": ["undocumented", "undocumented", "undocumented"]}], "caption": "The three legs of the lethal trifecta for each case in §3 of this unit. The trifecta is Willison's (16 Jun 2025, via DD-B3 §2.3); the B5 task from B5 §4 and §D; route 1 and AIssistant from B5 §5, with the connector-loading rule from B4 §1; Telegram counted as a way out is this unit's reading; Strider's row is undocumented in every cell, since no filed unit documents it; §3 works it only as a hypothetical."}
```

## 4 · What agents do well

Three kinds of work have documented gains, and they share one property: a result that can be checked without trusting the agent.

**Parallel research.** Anthropic's research system, an Opus 4 lead agent with Sonnet 4 subagents, "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval" (Hadfield et al.; vendor, internal evaluation, method unpublished). The post says where it fits: "breadth-first queries that involve pursuing multiple independent directions simultaneously"; tasks where every agent needs the same context, or where the parts depend heavily on each other, "are not a good fit for multi-agent systems today"; and "most coding tasks involve fewer truly parallelizable tasks than research" (same post; the first two as B6 §1 quotes them). For him this is already routed: B6 Deliverable A sends a landscape question with several independent directions to Research, and the report through the sampling rule. Inside Claude Code the same pattern is the investigation subagent: "They explore in a separate context, keeping your main conversation clean for implementation" (*Best practices*).

**Repetitive edits.** One change, the same each time, across many files. The documented method is a fan-out with a trial: list the files, loop over them, and "Test on a few files, then run on all of them", refining the prompt "based on what goes wrong with the first 2-3 files"; the `--allowedTools` flag "restricts what Claude can do, which matters when you're running unattended" (*Best practices*, at the address opened); a later copy of the same page, returned by search the same day, says instead that it "pre-approves the tools the migration needs" and adds `--permission-mode dontAsk`, which "denies anything else that would need approval". Karpathy's account of where agents helped before his own switch matches: boilerplate, and porting his tokenizer to Rust from a Python version he understood, with tests, which made him feel "safer" ([Dwarkesh Podcast, 17 Oct 2025](https://www.dwarkesh.com/p/andrej-karpathy), via DD-B3 §1.5; anecdote, one codebase). His repository has this kind of work queued: B4 F8 replaces four prose copies of one list, in three files, with a pointer, and F9 corrects two files that still name a retired build script (B4, Deliverable C and §5). Each is a find-and-replace across named files, and its check can be a script: a search for the old text that returns nothing.

**Builds with tests.** The best-practice page's central claim: "Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available, and you become the verification loop"; "Give Claude something that produces a pass or fail, and the loop closes on its own" (*Best practices*). autoresearch is the far end of it: one editable file, a five-minute run, one metric, keep-or-revert, run unattended, with gains Karpathy recorded on his own nanochat leaderboard ([karpathy/autoresearch](https://github.com/karpathy/autoresearch), via DD-B3 §1.6; documented practice, self-reported result). For him the equivalents are the kit's `kit/verify.py` and `kit/index_check.py`, B5's `check_quotes.py`, and any pcblueprint script with a fixture.

What the three share is Karpathy's verifiability test as DD-B3 §1.8 sets it out: a task can be delegated when attempts are "resettable", "efficient" and "rewardable", with "some automated process to reward any specific attempt" ([Karpathy, *Verifiability*, 17 Nov 2025](https://karpathy.bearblog.dev/verifiability/), via DD-B3; stated opinion). Writing a course unit fails the third, since its check is a sampled audit by another model (DD-B3 §1.6). That is why units are written by one fresh agent per unit and checked by another that did not see the writing (P31 and the fresh check, DD-B3 §4), and never run in a loop.

## 5 · What they quietly wreck

The three failures the brief names look like success until someone checks.

**Silent wrong assumptions.** Karpathy's list from January 2026, as The Decoder reports his post: agents make wrong assumptions and build on them without checking, do not manage their confusion, do not seek clarification, do not surface inconsistencies, do not present trade-offs, do not push back, are sycophantic, bloat abstractions, leave dead code, and write constructions of about 1,000 lines that shrink to about 100 when challenged; his advice was to "watch them like a hawk" ([The Decoder, 27 Jan 2026](https://the-decoder.com/former-tesla-ai-chief-andrej-karpathy-now-codes-mostly-in-english-just-three-months-after-calling-ai-agents-useless/), via DD-B3 §1.5; stated opinion, his own account). Claude Code's subagents make the mechanism concrete: they cannot ask (§2), so a gap in the brief becomes a guess, and Anthropic's research team saw vague instructions produce misread tasks, duplicated work and gaps (Hadfield et al.; vendor). The best-practice page calls the result "The trust-then-verify gap. Claude produces a plausible-looking implementation that doesn't handle edge cases", and its fix ends "If you can't verify it, don't ship it" (*Best practices*). His own record is the measured case: when B6 counted, eleven of the fourteen filed Brand + AI units with a fresh-check line had at least one error-severity finding at their first check (B6 §2); by 2 November 2026, before this unit, it was fifteen of eighteen (my count from the fresh-check lines at the end of each unit; seven of the eighteen checks were run by Opus 5.5 with a Fable 5.1 check owed). All were written by Opus 5.5 with the sourcing standard in the brief. A careful agent's first draft is usually close and rarely clean.

**Overwriting.** An agent writes files, and the undo has holes. Claude Code snapshots files before Claude's own edits, but, as of 2 November 2026 ([Claude Code docs, *Checkpointing*](https://code.claude.com/docs/en/checkpointing); product documentation):

- "A file that only Bash commands changed isn't tracked and stays as it is. To revert it, use version control, such as Git."
- After a subagent runs, "rewinding restores only the files Claude had already edited in your conversation. The subagent's edits to other files stay."
- Manual changes and "edits from other concurrent sessions are normally not captured".
- Checkpoints are "Not a replacement for version control".

Beyond files: "Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed" (*How Claude Code works*). In his repository the files that matter most are filed units, which change only by exact-replacement errata and are never edited by an auditor (DD-B3 §4, collision 2, from `method.md` §6). An agent with write access to `courses/` that tidies a unit breaks that rule in a way no checkpoint repairs once the change is committed and built into the public site, where removed material may survive in clones and caches (B4 F15).

**Cost blowups.** Each multiplier is documented, and none shows while it runs.

- An agent uses about 4× a chat's tokens, a multi-agent system about 15× (Hadfield et al.; vendor, 2025).
- Each subagent "sends its own requests, which count toward the same usage limits as your main conversation", and "each subagent spends tokens of its own while it runs" (*Subagents*). A `/batch` of 5 to 30 subagents pays for 5 to 30 sets of requests on top of the session's own.
- The limit is shared: claude.ai, Claude Code and Claude Desktop draw on one limit (B8 §1), so an agent run that empties the week also stops the week's unit and audit.
- Fable 5.1 on Pro is paid with usage credits billed at API rates (B8 §1), so a Fable subagent on Pro costs money directly.
- Unattended runs keep going. In a non-interactive run, when the auto-mode classifier repeatedly blocks actions, "Claude Code doesn't stop the run" (*Best practices*); autoresearch's agent is told the loop "runs until the human interrupts you, period" (DD-B3 §1.6).

## 6 · Guardrails: scopes, dry runs, review gates

OpenAI's guide says of guardrails that "a single one is unlikely to provide sufficient protection" ([OpenAI, *A practical guide to building agents*](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), via DD-B3 §2.2; vendor), and Claude Code's pages say as much of each of their own layers: auto mode "does not guarantee safety", a stated boundary can be lost to compaction, a timed-out hook does not block (§2). Guards are stacked, and each below names what it stops.

### Scopes: what the agent may touch

- **Tools.** The `tools` allowlist on a subagent; on a scripted run, `--allowedTools` together with `--permission-mode dontAsk`, since `dontAsk` denies "anything that would prompt" (*Permission modes*) and `--allowedTools` alone pre-approves (§4). Read-only tools for any task whose output is a report.
- **Files.** One folder or file it may change, named in the prompt and enforced by a deny rule or a `PreToolUse` hook on the paths it may not touch; the best-practice page's own example is a hook "that blocks writes to the migrations folder". In his repository, `courses/` is outside every agent's writable scope except a filing chat's.
- **Branch.** Work on a branch, or in a worktree: `isolation: worktree` gives a subagent "an isolated copy of the repository" (*Subagents*). Branch protection on the default branch, which B5 §D already sets for the weekly task, leaves the run its `claude/` branch only.
- **Connectors.** None unless the task needs one. Scheduled tasks include all connectors by default, and can write through them (B5 §4); B8 rule 19 covers chats, and for agents every unneeded connector is removed.
- **The trifecta.** Never all three legs in one agent (Willison, via DD-B3 §2.3). It is a hard stop, so the Deliverable checks it first.
- **Mode.** `bypassPermissions` only "in isolated environments like containers, VMs, or dev containers without internet access", since it "offers no protection against prompt injection or unintended actions" (*Permission modes*). On his own machine and repositories, never.

### Dry runs: effects that can be thrown away

- **Plan mode** for intent: a plan, and no edits to source until he approves (*Permission modes*; it still runs exploratory commands, §2).
- **The first two or three** of a batch, checked, before the rest (*Best practices*; §4).
- **A branch or worktree run**, merged or deleted whole: autoresearch's keep-or-revert, "you git reset back to where you started" (DD-B3 §1.6); B5's `claude/entry-…` branch.
- **A fixed budget.** autoresearch's five minutes a run (DD-B3 §1.6); a maximum number of attempts in the prompt, as B5's weekly task has ("at most twice", B5 §D); Anthropic's "stopping conditions (such as a maximum number of iterations)" (*Building effective agents*).
- **Commit before.** Checkpoints miss Bash edits and other files a subagent changed (§5), so the working tree is committed before an agent run starts and git is the undo (my rule, from *Checkpointing*'s own advice to use version control).

### Review gates: who signs off

- **A check that runs**, pass or fail, before he looks (*Best practices*).
- **An independent reviewer.** A subagent that "sees only the diff and the criteria you give it, not the reasoning that produced the change". The page warns that a reviewer asked for gaps "will usually report some, even when the work is sound", and advises telling it "to flag only gaps that affect correctness or the stated requirements" (*Best practices*). This is DD-B3's rule 3, "The writer never checks its own work".
- **Him, on anything high-risk.** OpenAI's guide calls "Human intervention … a critical safeguard" for high-risk actions (via DD-B3 §2.2); Maginative's report of the guide adds the case "when agents repeatedly fail to accomplish tasks" ([Maginative, 17 Apr 2025](https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/), read 2 Nov 2026). Irreversible actions come first among high-risk ones, because no checkpoint or revert covers them.
- **The sampling rule and the final pass.** Anything an agent produces that will be published or filed goes through B6's sampling rule (Deliverable C; tier P when published), and anything in the content pipeline through his final pass (B7 step 9).
- **Two misses, then a new brief.** "After two failed corrections, `/clear` and write a better initial prompt incorporating what you learned" (*Best practices*); DD-B3 rule 6.

## 7 · DD-B3's flags, taken or declined

DD-B3 §5 listed what this unit should take, and its table and O1 card left the rest of OpenAI's guide here ("To DD-B1"; "Leaves: the rest to DD-B1"). Each item, with the source DD-B3 cites for it:

| Item (DD-B3's source) | Decision | Why |
|---|---|---|
| Autonomy slider (Karpathy, YC talk, 17 Jun 2025, via a third-party transcription) | Taken | It frames §1 and the Deliverable's boxes 5 to 8; Claude Code's permission modes are its settings (§2). |
| Verifiability: resettable, efficient, rewardable (Karpathy, *Verifiability*, 17 Nov 2025) | Taken as the delegation test, with one change | For him "rewardable" means a check that returns pass or fail without his reading: a test, a script, a source to open. Course units fail it and are never put in a loop (§4). Box 3. |
| autoresearch's four guards: one editable file, fixed budget, scalar metric, keep-or-revert (karpathy/autoresearch, Mar 2026) | Taken for every unattended run | They map onto scope, budget, check and revert in §6. "Scalar metric" becomes "pass/fail check", as DD-B3's operating rule 7 already wrote it. Box 8. |
| autoresearch's "NEVER STOP" | Declined | Examined below. |
| Claude Code's five questions before an unattended run (best-practice page, read 29 Oct 2026) | Taken | They are box 8's gate. See the note below on the page as read on 2 November. |
| OpenAI's "human intervention" (OpenAI guide, PDF) | Taken, in the source's own term | The guide says "high-risk actions"; DD-B3's flag wrote "irreversible". This unit uses the wider term and treats every action outside checkpoint and git reach (send, publish, delete, deploy, pay) as high-risk. Box 2. |
| The lethal trifecta as a hard stop (Willison, 16 Jun 2025) | Taken | Box 1; applied to pcblueprint and AIssistant in §3. |
| Karpathy's failure list, January 2026 (X post via The Decoder) | Taken | It is §5's catalogue and the reviewer's checklist in §6. |

**"NEVER STOP", examined.** In autoresearch the instruction is safe because everything else bounds it: each run lasts five minutes, the agent edits one file, the evaluation file is read-only, every result is kept or reverted by rule, and the human interrupts (DD-B3 §1.6). The instruction removes only the agent's own choice to stop. Moved into his setup it loses those bounds. Scheduled runs "draw down subscription usage the same way interactive sessions do" (B5 §4); that limit is shared with his units and audits (B8 §1); Fable on Pro is billed in credits (B8 §1); DD-B3 §4 (collision 4) already set it against the audit gate and 5–7 hours a week; and in a non-interactive run, repeated classifier blocks do not end the run (*Best practices*). So every agent run here carries its stop in the prompt: a maximum number of attempts, and what it does on reaching it.

**The five questions, as read on 2 November.** DD-B3 §2.1 recorded them from the best-practice page on 29 October 2026: does it know what done looks like; can it check its own work; what may it touch; what stops it; where does the result go and who signs off. The copy of the page this unit opened on 2 November, at the address search returned, did not show that list, nor the "What you can stop doing" table DD-B3 quotes from the same page. Either the page changed or the two reads saw different versions. The questions are taken on DD-B3's record; each maps to a guard in §6 whatever the page now says.

**The rest of OpenAI's guide** (DD-B3 §2.2 quotes the PDF; the O1 card adopted only human sign-off):

- **Single agent first.** Taken. The guide says to "maximize a single agent's capabilities first"; Maginative's report: teams "are encouraged to begin with single‑agent systems" and to "evolve to multi‑agent designs only when complexity demands it" (Maginative, 17 Apr 2025). It agrees with Anthropic's "simplest solution possible" (§1) and with the research post's finding that coding has fewer parallel parts (§4). In the Deliverable, subagents are a shape chosen for a reason (verbose side work, read-only investigation, a fan-out), never the default.
- **Most capable model first, then step down.** Taken for new agent loops only. The guide: "build your agent prototype with the most capable model for every task to establish a performance baseline", then try smaller models. DD-B3 noted that this reverses B2's cost-first order for small tasks. The two apply at different rungs. A chat task is short and cheap to redo, so B2 starts low. An agent loop compounds its errors (§1), and the evidence on long agentic tasks favours Sonnet 5.5 and Opus 5.5 over Haiku 5.5: on Terminal-Bench 4.0, Haiku 5.5 scores 39.2% against Opus 5.5's 66.4% (at xhigh) and Sonnet 5.5's 70.6%, which B2 §8 reads as the top two level, and Anthropic recommends Sonnet or Opus over Haiku for complex agentic coding (B2 §8; vendor). Opus 5.5 goes first because the model page's advice is to start with it when unsure (B2 §1). So a new loop runs first on Opus 5.5 with its check, moves to Sonnet 5.5 once the check passes on repeat runs, and keeps Haiku 5.5 for read-only subagents and fixed-format extraction. Box 6.
- **Evals for a baseline.** Taken, in the form he already has. The guide: "Set up evals to establish a performance baseline." His evals are the check a run must pass, recorded on the first run as its baseline; for writing, the fresh check and the four-unit audit (B6).
- **Layered guardrails.** Taken; §6 is the layers.

## 8 · Where an agent step would change B7 and B8

### B7: the pipeline stays chats

B7 runs each step in its own chat, with his check after it, and ends at step 9, his final pass (B7 §9 and Deliverable A). An agent could change the pipeline in two ways, and neither pays.

- **Chaining steps moves the gate.** Step 3's pass rewrites or cuts every `[NEW]` line before titles, the Short and Instagram are built on the final script, after his filming and edit in step 4; the email is built on the entry and the record (B7, Deliverable A, steps 3 to 8). An agent chaining steps 3, 5, 6 and 7 in one go would build three of them on lines he has not passed, and would have no edit to build on.
- **Fanning out steps 5 to 7 saves nothing he spends.** After the edit, titles, the Short and the Instagram posts each take the final script as input (steps 5, 6 and 7), so three subagents could draft them at once. His checks are the constraint, and they sit in A3's Tuesday and Wednesday slots however fast the drafts arrive (B7, Hours). The fan-out adds three sets of requests to his usage limit (§5).

**Rule (B7).** No agent runs any of B7's numbered steps; the chain's one unattended run stays B5's weekly journal-entry task (B5's step 2), which already carries the four guards and no connectors (B5 §D). One agent use fits: a read-only run of the code checks (`check_quotes.py`, the title-length count) across an episode folder, reporting failures and editing nothing. Step 9 is unchanged: nothing an agent touched is published before his final pass.

### B8: one budget row and four rules

B8's rules 11 to 24 were written for chats, and they hold for agents with three readings. Rule 11 applies per context: a subagent's model is set in its definition and not changed mid-run. Rule 17 protects the window, and a subagent protects the window while spending the same usage (§2). Rule 19 extends to agents: scheduled tasks include every connector by default, so each unneeded one is removed (B5 §4).

The budget table (B8 §4; rule 20) gains one row:

| Task | Window holds | Size | Stops at |
|---|---|---|---|
| Agent run (Claude Code, with or without subagents) | The brief, the check, files as read; each subagent its own window, returning a summary | About 4× a chat's tokens, multi-agent about 15× (vendor, 2025); every subagent's requests count toward the same limit | The check passes, or the attempt cap in the prompt, whichever comes first |

And four rules, numbered after B8's, for the way-of-working file:

> 25. **Every agent run carries its stop in the prompt:** a maximum number of attempts and what it does on reaching it. No run is told to continue until interrupted. *(Anthropic, Building effective agents; B5 §D; DD-B3 rule 6; DD-B1 §7.)*
> 26. **A subagent's brief is complete, because it cannot ask:** the task, the files, what it may not touch, what done looks like, and what to return if it cannot finish. *(Claude Code docs, Subagents; Hadfield et al.; B3.)*
> 27. **Before an agent run I commit, and the run works on a branch or in a worktree;** filed units are outside every agent's writable scope except a filing chat's. *(Claude Code docs, Checkpointing and Subagents; DD-B3 §4; B5 §D.)*
> 28. **Before an agent run I check Settings > Usage, and the week's unit and audit run before any optional agent run,** since all three draw on one limit. *(B8 §1 and rule 21; the ordering is my rule.)*

## Deliverable · The agent-use decision rule

A one-page flowchart in prose. Start at box 1 with a task about to be handed to a model, follow the arrows, and stop at the first outcome reached. Each box names the section of this unit it rests on.

**1 · Trifecta.** Would the agent hold, at the same time, private data, untrusted content (web pages, other people's messages, files from outside) and a way to send, publish or post?
→ **Yes:** stop. Remove one leg (the send or publish tool first; failing that, the private data), then start again at box 1.
→ **No:** box 2.
*(§3, §6; Willison via DD-B3 §2.3.)*

**2 · High-risk step.** Does the task end in an action no checkpoint or git revert can undo: sending, publishing, deleting, deploying, paying, writing to a remote system?
→ **Yes:** he does that action himself. Only the drafting part goes on to box 3.
→ **No:** box 3.
*(§5, §6; Claude Code docs, How Claude Code works; OpenAI via DD-B3 §2.2.)*

**3 · Check.** Can something other than his reading tell pass from fail: a test, a build, a script, a fixture, a source he can open?
→ **No, and none can be written** (a judgement, a positioning line, what to cut): no agent. A chat drafts and he decides; B2 routes the model, B3 the brief.
→ **No, but one can be written** (code without tests): write the check first, then return to box 3.
→ **Yes:** box 4.
*(§3, §4; Karpathy's verifiability via DD-B3 §1.8; Claude Code docs, Best practices.)*

**4 · Loop.** Does the task need tools over several steps, each depending on the last result: reading or changing files, running code?
→ **No, one answer from material in hand:** a chat (B2, B3).
→ **No, a research question with several independent directions, worth a report:** Research, then B6's sampling rule (B6 Deliverable A).
→ **Yes:** box 5.
*(§1, §4; B6 §1.)*

**5 · Shape.** Which describes the work?
→ **(a) One change he could describe in one sentence:** a Claude Code session, no plan, no subagents.
→ **(b) Several phases sharing context (plan, build, test):** one session, plan mode first, no subagents.
→ **(c) Reading across many files, the result a summary:** a read-only subagent (Explore, or one built like `vault-finder`), with a complete brief, because it cannot ask.
→ **(d) The same change across many files:** a fan-out, with an allowed-tools list and `dontAsk` mode, on a branch or in worktrees; two or three files first, checked, then the rest.
Then box 6.
*(§2, §4; Claude Code docs, Subagents and Best practices.)*

**6 · Model.** A new loop runs first on Opus 5.5 with its check. It moves to Sonnet 5.5 once the check passes on repeat runs. Haiku 5.5 is for read-only subagents and fixed-format extraction only. Then box 7.
*(§7; OpenAI via DD-B3 §2.2; B2 §1, §8.)*

**7 · Watching.** Will it run while he is not watching: a scheduled task, a background or overnight run, a scripted loop?
→ **No:** run it in a session he watches, in the mode the shape needs (plan for (b), Manual or auto otherwise), and go to box 9.
→ **Yes:** box 8.
*(§2; B5 §4.)*

**8 · Unattended gate.** Is every line true?
- It knows what done looks like.
- It can check its own work.
- It may touch one named folder or file and nothing else, enforced by a tool list, deny rule or hook.
- Something stops it: an attempt cap in the prompt, and what it does on reaching it.
- The result lands on a branch he merges or deletes, and he signs off.
- It holds no connector it does not need.
- It is not writing course units.

→ **Any line false:** back to box 7's "No"; run it where he watches.
→ **All true:** run it unattended.
*(§6, §7; DD-B3's five questions and four guards; B5 §D.)*

**9 · Before anything is kept.** The check has passed. A reviewer that did not write the work has read the diff for gaps in correctness or the stated requirements. Anything to be published or filed has passed B6's sampling rule, and anything in the content pipeline his final pass (B7 step 9). After two failed corrections at any point, a new session with a rewritten brief.
*(§6; Claude Code docs, Best practices; B6 Deliverable C; B7 §9; DD-B3 rule 6.)*

**On every path.** Never `bypassPermissions`. Commit before any run. Check Settings > Usage first; the week's unit and audit come before any optional agent run. *(§6; §8, rules 25 to 28.)*

```viz
{"kind": "decision", "title": "Agent or not", "root": {"q": "All three trifecta legs at once?", "tone": 4, "branches": [{"label": "yes", "to": {"outcome": "Stop: remove one leg", "tone": 1}}, {"label": "no", "to": {"q": "Pass/fail check exists?", "tone": 4, "branches": [{"label": "no", "to": {"outcome": "Chat drafts; he decides", "tone": 3}}, {"label": "yes", "to": {"q": "Tools over several dependent steps?", "tone": 4, "branches": [{"label": "no", "to": {"outcome": "Chat, or Research for a report", "tone": 3}}, {"label": "yes", "to": {"q": "Runs while he is not watching?", "tone": 4, "branches": [{"label": "no", "to": {"outcome": "Claude Code session he watches", "tone": 2}}, {"label": "yes", "to": {"q": "Every box 8 line true?", "tone": 4, "branches": [{"label": "no", "to": {"outcome": "Claude Code session he watches", "tone": 2}}, {"label": "yes", "to": {"outcome": "Unattended run", "tone": 2}}]}}]}}]}}]}}]}, "caption": "The spine of the Deliverable: boxes 1, 3, 4, 7 and 8 of this unit's decision rule, built from §3 to §7 (Willison via DD-B3 §2.3; Karpathy's verifiability via DD-B3 §1.8; B6 §1; Claude Code docs, <a href=\"https://code.claude.com/docs/en/best-practices?r=0\"><em>Best practices</em></a> and <a href=\"https://code.claude.com/docs/en/subagents\"><em>Subagents</em></a>, read 2 Nov 2026; DD-B3's five questions and four guards). Box 2 (high-risk steps), the write-the-check-first branch of box 3, box 5 (shape), box 6 (model) and box 9 (before anything is kept) are in the text and not drawn."}
```

## Sources

Web sources opened on 2 November 2026 at the address a search returned, unless marked "via DD-B3" (opened by DD-B3 on 29 October 2026, not re-opened here).

- Claude Code docs. *How Claude Code works*. https://code.claude.com/docs/en/how-claude-code-works
- Claude Code docs. *Permission modes*. https://code.claude.com/docs/en/permission-modes
- Claude Code docs. *Subagents*. https://code.claude.com/docs/en/subagents
- Claude Code docs. *Checkpointing*. https://code.claude.com/docs/en/checkpointing
- Claude Code docs. *Hooks* (opened at this address). https://code.claude.com/docs/en/hooks?frame=0
- Claude Code docs. *Best practices for Claude Code* (opened at this address; see unsure item 1). https://code.claude.com/docs/en/best-practices?r=0
- Schluntz, E. and Zhang, B. *Building effective agents*. Anthropic, 19 December 2024 (page metadata shows a later modification, 9 October 2026; vendor). https://www.anthropic.com/research/building-effective-agents
- Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. and Ford, D. *How we built our multi-agent research system*. Anthropic Engineering, 13 June 2025 (vendor). https://www.anthropic.com/engineering/multi-agent-research-system
- McKay, C. *How to Build AI Agents: A Detailed, Practical Guide from OpenAI*. Maginative, 17 April 2025 (report of the guide). https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/
- OpenAI. *A practical guide to building agents* (PDF, undated; via DD-B3). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- Willison, S. *The lethal trifecta for AI agents*, 16 June 2025 (via DD-B3). https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Karpathy, A. *Verifiability*. Blog, 17 November 2025 (via DD-B3). https://karpathy.bearblog.dev/verifiability/
- Karpathy, A. autoresearch repository (README, `program.md`), March 2026 (via DD-B3). https://github.com/karpathy/autoresearch
- Y Combinator. *Andrej Karpathy: Software Is Changing (Again)*. YouTube, 18 June 2025, talk of 17 June 2025 (via DD-B3). https://www.youtube.com/watch?v=LCEmiRjPEtQ
- Third-party automatic transcription of the YC talk, billmill.org (via DD-B3). https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html
- Patel, D. *Andrej Karpathy* (interview transcript). Dwarkesh Podcast, 17 October 2025 (via DD-B3). https://www.dwarkesh.com/p/andrej-karpathy
- The Decoder. *Former Tesla AI chief Andrej Karpathy now codes mostly in English…*, 27 January 2026 (via DD-B3). https://the-decoder.com/former-tesla-ai-chief-andrej-karpathy-now-codes-mostly-in-english-just-three-months-after-calling-ai-agents-useless/
- Filed units cited by section: B1 · Mental model (§5, §6); B2 · Choosing the model (§1, §3, §8; routing table, Biometrics parsing); B3 · Prompting that holds up (brief structure); B4 · Context engineering (§1, §3, §5; F8, F9, F14, F15; Deliverable C); B5 · Skills and automation (§1, §4, §5, Deliverable D; unsure item 7); B6 · Research and verification (§1, §2; Deliverables A and C; unsure item 2); B7 · Content pipeline (§9; Deliverable A, steps 3, 5 to 7 and 9; Hours); B8 · Cost, limits, hygiene (§1, §2, §4, §5; rules 17, 19, 20, 21, 22); DD-B3 · Deep dive: how the best practitioners use the tool (§1.3, §1.5, §1.6, §1.8, §2.1, §2.2, §2.3, §2.6, §4, §5; O1 card; operating rules 3, 6 and 7). `method.md` §6 is cited as DD-B3 §4 cites it.

## Writer's unsure list

1. **The best-practice page differed between reads.** The copy opened on 2 November 2026 (at `best-practices?r=0`, the address search returned) shows neither the five questions before an unattended run nor the "What you can stop doing" table that DD-B3 quoted on 29 October, and it still carries "Manage context aggressively", which DD-B3 reported as retired. The five questions are taken on DD-B3's record; the quotations used here from that page may come from an older or different version.
2. **Hadfield et al.'s 4×, 15× and 90.2%** are Anthropic's figures for its 2025 research system; the 90.2% is for an Opus 4 lead with Sonnet 4 subagents, and the post does not say which configuration the token ratios come from (B6 unsure item 2); all three rest on internal evaluation with no published method; whether they hold for the 5.5 family is not stated anywhere read.
3. **OpenAI's guide was not opened here.** Its quotations come from DD-B3's reading of the PDF; Maginative's report, opened, confirms single agent first, most capable model first, layered guardrails and human intervention, and does not mention evals.
4. **Willison, Karpathy (Verifiability, autoresearch, the YC talk, Dwarkesh) and The Decoder** are cited through DD-B3's quotations and were not re-opened.
5. **AIssistant's inputs, tools and approval behaviour are undocumented.** Counting Telegram as a way to communicate externally is this unit's reading of Willison's term.
6. **Strider is undocumented in every filed unit;** §3's treatment is a hypothetical and states nothing about the real system.
7. **pcblueprint's network exposure is undocumented** (B5 unsure item 7), **and no filed unit mentions its tests;** the fixture check and the "no archive in agent sessions" rule are untested against its code.
8. **Building effective agents** was opened at its `/research/` address, while DD-B3 cites the `/engineering/` address; the page shows a modification on 9 October 2026. The workflow and agent definitions used in §1, as DD-B3 quotes them, are on the copy opened (fresh check, 2 Nov 2026).
9. **Auto mode as the starting mode.** *How Claude Code works* and *Permission modes* tie it to version 2.1.283 or later, and on earlier versions to Pro, Max and Team plans; the copy of the best-practice page opened gives the plan condition alone. Which version and plan his sessions run on is not recorded in any filed unit.
10. **The `vault-finder` subagent, rules 25 to 28 and the B7 rule are untested;** whether a Haiku subagent keeps to its stop line is unmeasured, and rule 28's ordering is my rule. The *Subagents* page was read through a fetch tool that returned its first 100,000 characters only; the removed-tools list is reported from that reading.

Fresh check 2026-11-02 (Opus 5.5, own agent context; a Fable 5.1 fresh check is owed): fix · 0 errors, 10 should-fix, 14 minor; all applied, plus one same-cause fix to unsure item 7; the matrix figure fixed and re-checked; report `audits/brand-ai/fresh-check-DD-B1.md`.
