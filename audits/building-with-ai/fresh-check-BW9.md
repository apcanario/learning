---
audit: fresh check
unit: BW9 · Agents
course: building-with-ai · Building with AI
model: Opus 5.5 (claude-opus-5-5)
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
verdict: keep · 0 errors, 7 should-fix, 11 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW9 · keep · 0 errors, 7 should-fix, 11 minor

Model: claude-opus-5-5 (Opus 5.5)

(The harness refused writing /home/claude/w-bw9/checker/out/report.md ("Subagents should return findings as text"), so the full report follows.)

# Fresh check · BW9 "Agents" · Building with AI · 16 Nov 2026

**Packet read:** unit.md, brief.txt, notes.md, unsure.md, sourcing-standard.md (Parts 1 and 6), case-academy.md and audit-units-SKILL.md. There is no audit report (skip).

**How sources were opened:** every web source was opened on 16 Nov 2026 from a URL that a WebSearch in this agent returned. "Unverifiable" means search did not return the page or the fetch was refused.

**Current strings:** each Current below was checked by script and occurs exactly once in unit.md.

## Findings

[should-fix] [attribution] §8 The primary sources; Current: "and wrote that the obvious fix, separating instructions from data, is "extremely difficult, if not impossible, to implement" on current models"; Problem: the quoted words are not in the post of 12 Sep 2022. They come from an update to that post dated 13 April 2023. They refer to Willison's own proposed fix ("parameterized prompts"), not to the general idea of separating instructions from data. As written, the sentence dates the quotation to 2022; Fix: "and, in an update of 13 April 2023, wrote that the fix he had proposed, passing instructions and data to the model separately ("parameterized prompts"), is "extremely difficult, if not impossible, to implement on the current architecture of large language models""; Basis: Willison, Prompt injection attacks against GPT-3, https://www.simonwillison.net/2022/Sep/12/prompt-injection

[should-fix] [attribution] §7 Review gates; Current: "- **Human intervention for high-risk actions.** OpenAI's guide to building agents, as Maginative reports it, calls human intervention "a critical safeguard, especially for high-risk actions", and recommends layered guardrails and a single agent before several ([McKay, *How to Build AI Agents: A Detailed, Practical Guide from OpenAI*, Maginative, 17 Apr 2025](https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/), read 16 Nov 2026; a report of a vendor guide; the quoted words are Maginative's, and the guide itself was not opened for this unit)."; Problem: Part 1 says a source is cited for what it says itself, not for what a reporter says about it. A search does return the guide (cdn.openai.com PDF), and its own words differ from Maginative's paraphrase: "critical safeguard" is tied to improving real-world performance, and high-risk actions are one of two named triggers. The quoted words in the unit are Maginative's paraphrase; Fix: "- **Human intervention for high-risk actions.** OpenAI's guide to building agents calls human intervention "a critical safeguard enabling you to improve an agent's real-world performance" and names high-risk actions as one of its two triggers: "Actions that are sensitive, irreversible, or have high stakes should trigger human oversight". It calls guardrails "a layered defense mechanism" and recommends that you "maximize a single agent's capabilities first" ([OpenAI, *A practical guide to building agents*](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), read 16 Nov 2026; vendor, documented practice; the guide carries no date)."; Basis: OpenAI, A practical guide to building agents, https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf ; McKay, Maginative, https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/ (there the phrase is the article's paraphrase, not a quotation)

[should-fix] [attribution] Sources; Current: "- McKay, C. *How to Build AI Agents: A Detailed, Practical Guide from OpenAI*. Maginative, 17 April 2025 (a report of OpenAI's guide). https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/"; Problem: this goes with the finding above. Once §7 cites the guide itself, the reporter is no longer cited and must leave the list (Part 1: nothing listed that the unit does not cite); Fix: "- OpenAI. *A practical guide to building agents* (PDF, undated). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf"; Basis: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf

[should-fix] [accuracy] §4 What a subagent is; Current: "A subagent can start subagents of its own, "up to three layers below the main conversation" by default (same page)."; Problem: §4, and the Box 5(c) and guard 9 that rest on it, describe only a subagent that starts fresh ("doesn't see your conversation history"; "It cannot ask you"). Anthropic's pages say a forked subagent starts with a copy of the conversation. They also say Claude's own side tasks are forked while fork mode is on, which is the default. The writer recorded this (notes, Contradictions 4), but the unit never says it; Fix: "A subagent can start subagents of its own, "up to three layers below the main conversation" by default (same page). The exception is a fork, which "starts with a copy of your conversation so far" (*How Claude Code works*, read 16 Nov 2026); Claude's own side tasks are forked while fork mode is on, which is the default (*Best practices for Claude Code*, read 16 Nov 2026). What follows describes a subagent that starts fresh: the kind you define and brief yourself."; Basis: https://code.claude.com/docs/en/how-claude-code-works ; https://code.claude.com/docs/en/best-practices?ref=t01.li ("Side tasks get forked while fork mode is on (the default).")

[should-fix] [accuracy] §7 opening paragraph; Current: "**Deterministic**: hooks, deny rules, the sandbox, managed settings, tests, branch protection, a person who approves the merge;"; Problem: the page does not count every hook as deterministic. It says: "A `prompt` or `agent` hook asks *another model* to decide, so it isn't deterministic either. For real enforcement, use a `command` or `http` hook." Its table also lists "the sandbox in strict mode", not the sandbox in general. A reader building the "must never happen" rule on this list would take a prompt hook for enforcement; Fix: "**Deterministic**: command and http hooks (a hook that asks another model to decide is not), deny rules, the sandbox in strict mode, managed settings, tests, branch protection, a person who approves the merge;"; Basis: Anthropic, Best practices for Claude Code, https://code.claude.com/docs/en/best-practices?ref=t01.li

[should-fix] [figure] Deliverable Part 1, decision figure; Current: "  {"label": "no", "to": {"outcome": "Chat drafts; you decide", "tone": 3}},"; Problem: Box 3 has three exits in the text, and the figure merges two of them. It folds "No, but one can be written" (write the check first, then return to box 3) into "Chat drafts; you decide". The figure therefore sends a task whose check can be written away from agents, which the prose rule does not do; Fix: "  {"label": "no, and none can be written", "to": {"outcome": "Chat drafts; you decide", "tone": 3}},\n  {"label": "no, but one can be written", "to": {"outcome": "Write the check first", "tone": 4}},"; Basis: unit, Box 3 ("→ **No, but one can be written** (a script with no test, a format with no validator): write the check first, as its own small task, then return to box 3.")

[should-fix] [label] Deliverable Part 2, guard 16; Current: "| 16 | After two failed corrections, a new session with a rewritten brief (§7) | Figures are re-checked by a new agent after each fix (§6) |"; Problem: Part 2 says "The case column holds only what the case file records". The case file (§6) records that a failed figure was fixed and checked again by a new agent. It records no rule of a new session with a rewritten brief after two failed corrections, yet the cell reads as though the case holds the guard; Fix: "| 16 | After two failed corrections, a new session with a rewritten brief (§7) | A failed figure was fixed and checked again by a new agent each time (§6); a rule on rewriting a brief after two failed corrections [NOT IN CASE FILE] |"; Basis: Academy case file §6

[minor] [accuracy] §8 What the vendors say and measure; Current: "With the model alone, Claude Opus 4.5 was successfully attacked in 8.0% of attempts; with its improved safeguards, 1.4%;"; Problem: the post computes the attack success rate "as a percentage of attacks encountered by each model", not of attempts. Its headline figure of 1% is the 1.4% rounded, which settles unsure item 3; Fix: "With the model alone, Claude Opus 4.5's attack success rate was 8.0%; with its improved safeguards, 1.4%, which the post's headline rounds to 1%;"; Basis: Anthropic, Mitigating prompt injections in browser use, 24 Nov 2025, https://anthropic.com/research/prompt-injection-defenses

[minor] [accuracy] §8 What the vendors say and measure; Current: "vendor, measured internally, Claude for Chrome, 100 attempts per environment)"; Problem: the page states a sample size and the unit omits it ("Sample sizes range from about 2,200 to 3,200 attempts per bar"); Fix: "vendor, measured internally, Claude for Chrome; an adaptive attacker given 100 attempts per environment, about 2,200 to 3,200 attempts per bar)"; Basis: https://anthropic.com/research/prompt-injection-defenses

[minor] [attribution] Sources; Current: "- Anthropic. *Mitigating prompt injections in browser use*. 24 November 2025. https://anthropic.com/research/prompt-injection-defenses"; Problem: the headline on the page is "Mitigating the risk of prompt injections in browser use". The unit's title is the page's meta title; Fix: "- Anthropic. *Mitigating the risk of prompt injections in browser use* (page title: Mitigating prompt injections in browser use). 24 November 2025. https://anthropic.com/research/prompt-injection-defenses"; Basis: https://anthropic.com/research/prompt-injection-defenses

[minor] [accuracy] §8 What the vendors say and measure; Current: "calls it "a frontier, challenging research problem" and gives users three moves:"; Problem: the page lists four "Steps you can take to stay safer". The fourth is "Stay informed and follow security best practices", so "three moves" reads as the whole list; Fix: "calls it "a frontier, challenging research problem" and, among four steps for users, gives three that bear on agents:"; Basis: OpenAI, Understanding prompt injections, 7 Nov 2025, https://openai.com/index/prompt-injections/

[minor] [label] §8 The primary sources; Current: "preprint as read, demonstrations rather than a rate)"; Problem: this answers unsure item 5. The paper was published after peer review in the Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec 2023), pp. 79–90, DOI 10.1145/3605764.3623985, with Abdelnabi listed first; Fix: "preprint as read; also published in the Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec 2023), pp. 79–90; demonstrations rather than a rate)"; Basis: https://researchr.org/publication/AbdelnabiGMEHF23 ; https://arxiv.org/abs/2302.12173v2

[minor] [accuracy] §3 What follows for someone who cannot read the code; Current: "Anthropic's own legal team, the same PDF reports, weighed the "security implications of deep MCP integrations" before building further."; Problem: the PDF says the legal department's product lawyers immediately identify these implications. "Before building further" is not in the source; Fix: "Anthropic's own legal team, the same PDF reports, saw at once the "security implications of deep MCP integrations"."; Basis: https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf

[minor] [accuracy] §2 Verifiability; Current: "In a post of 17 November 2025 he writes"; Problem: search did not return the bearblog address, so the date cannot be checked there (unverifiable). The same text with the quoted words appeared as Karpathy's post on X dated 16 Nov 2025 (threadreader; Willison's weblog of 16 Nov 2025); Fix: "In a post of November 2025 (first on X on 16 November) he writes"; Basis: https://threadreaderapp.com/thread/1990116666194456651.html ; https://simonwillison.net/2025/Nov/16/andrej-karpathy/

[minor] [coverage] §2 The slider; Current: "from his keynote at Y Combinator's AI Startup School in June 2025"; Problem: the brief asks for the slider "from its primary source", which is the recording. The unit says openly that its quotations rest on a third-party transcription (unsure 1; Needs 3). Search did not return the transcription address, so it was not opened (unverifiable). Latent Space's write-up, published 17 June 2025 and describing the talk as given "today", confirms the "Autonomy Slider" and the fast generation–verification loop; Fix: "from his keynote at Y Combinator's AI Startup School on 17 June 2025"; Basis: Latent Space, https://latent.space/s3

[minor] [style] §7 Version control; Current: "- **A branch is a copy you can discard.** A run works on its own branch or worktree; you keep it by merging, or delete it whole."; Problem: "worktree" is used in §5, §7, Box 5, Box 7 and guard 4 and is never explained for a reader who does not write code; Fix: "- **A branch is a copy you can discard.** A run works on its own branch or worktree (a worktree is a separate folder for one branch, so parallel runs do not touch each other's files; *How Claude Code works*); you keep it by merging, or delete it whole."; Basis: https://code.claude.com/docs/en/how-claude-code-works ("git worktrees, which create separate directories for individual branches")

[minor] [style] §8 The working rule; Current: "He adds that MCP encourages users to mix tools from different sources (same post)"; Problem: "MCP" appears in §3 and §8 and is never explained for this reader. The sentence also paraphrases Willison's own words "mix and match tools from different sources"; Fix: "He adds that MCP (the Model Context Protocol, by which connectors and tool servers plug into an assistant) "encourages users to mix and match tools from different sources" (same post)"; Basis: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ ; https://code.claude.com/docs/en/security?web=1 ("Model Context Protocol (MCP) servers")

[minor] [accuracy] §2 permission-mode table; Current: "| `dontAsk` | File reads in your working directories and pre-approved tools; anything that would prompt is denied | Locked-down CI and scripts |"; Problem: the page's cell goes on: "though a mod you installed can still approve some of those calls". Without it, the unit makes dontAsk a harder wall than the vendor states; Fix: "| `dontAsk` | File reads in your working directories and pre-approved tools; anything that would prompt is denied, though a mod you installed can still approve some of those calls | Locked-down CI and scripts |"; Basis: https://code.claude.com/docs/en/permission-modes

## Confirmed

**How Claude Code works** (https://code.claude.com/docs/en/how-claude-code-works):
- "Tools are what make Claude Code agentic"; without tools Claude only responds with text; with them it reads, edits, runs commands, searches the web and uses external services.
- "gather context, take action, and verify results"; "chaining dozens of actions together"; "agentic harness".
- Esc stops the running action; a queued message is read before the next step.
- "anything you can do from the command line", including writing docs and researching topics.
- Remote actions "can't be checkpointed".
- Claude can use git.

**Choose a permission mode** (https://code.claude.com/docs/en/permission-modes):
- The six-mode table; the third column is verbatim.
- Auto mode is the starting mode from v2.1.283; on earlier versions only on Pro, Max and Team.
- The classifier quote; "does not guarantee safety"; "Boundaries are not stored as rules"; "For a hard guarantee, add a deny rule instead".
- Plan mode: "runs shell commands to explore" and "does not edit your source".
- The bypassPermissions quotes.
- Auto mode pauses after 3 blocks in a row or 20 in total.

**Create custom subagents** (https://code.claude.com/docs/en/subagents):
- The definition; "only this system prompt plus basic environment details"; "doesn't see your conversation history"; "up to three layers below the main conversation".
- The tools allowlist; permissionMode is ignored under bypassPermissions, acceptEdits and auto.
- AskUserQuestion is on the list of removed tools.
- The Explore quote; Plan is read-only; general-purpose has every tool.
- The when-to-use quotes.
- "count toward the same usage limits"; "each subagent spends tokens of its own while it runs".
- The skills field injects full content at startup.

**Best practices for Claude Code** (https://code.claude.com/docs/en/best-practices?ref=t01.li). Every quotation the unit takes from this page was found verbatim:
- Checks and evidence: "Claude stops when the work looks done"; "makes you the test suite"; "comes back pass or fail"; the five example checks; "Claude can close that loop itself"; evidence means the command and its output.
- Subagents: "doesn't make the answer any better"; "A fresh reviewer does help…"; "not a smarter answer"; "mostly tokens"; a fresh subagent can be slower; model: haiku for simple jobs.
- Usage and batch work: /usage by subagent on Pro, Max, Team and Enterprise; --allowedTools, dontAsk and "anything else that would have prompted"; --max-turns; OK or FAIL; "Try it on three files first"; /batch with 5 to 30 units, a worktree and a PR each.
- Unattended runs: "nobody tells it" and "the wrong assumption"; /loop and goal checks keep spending; three or twenty blocks; "repeated blocks don't pause…".
- Controls: "no guarantee that it'll follow your instructions"; deny rules apply before the classifier; "enforced by Claude Code rather than requested in a prompt"; ".env" and "migrations" examples; worktrees "disappear…"; "What stops it?" with its caps.
- Review: /code-review "fresh subagent that never saw your conversation"; "will always find something"; "can't take back"; "two failed corrections…".
- The five questions; "watch the first few runs…"; "alongside git rather than replacing it"; "driven by content Claude read rather than by you".
- The writer's Contradictions 1 and 2 are confirmed on this page version: it carries "pass or fail" and "always find *something*", and it names "Claude Fable 5.1".

**Other Claude Code pages:**
- Checkpointing, all four bullets: https://code.claude.com/docs/en/checkpointing
- Manage costs: agent teams "approximately 7x more tokens than standard sessions when teammates run in plan mode"; each teammate has its own context window; each active teammate consumes tokens until it exits; /usage attribution by subagent on paid plans: https://code.claude.com/docs/en/costs?ref=t01.li
- Security: "no system is completely immune to all attacks"; the listed protections; the five untrusted-content practices: https://code.claude.com/docs/en/security?web=1
- Scheduled tasks: usage "the same way interactive sessions do"; claude/ branches; "a rule that access can bypass doesn't block a run's push"; connectors included by default, "Remove any the task doesn't need", "including writes", "appears as you"; the fired prompt "can't act as approval or consent…"; API fire text wrapped and labelled as untrusted: https://code.claude.com/docs/en/web-scheduled-tasks
- Skills: preload; disable-model-invocation also blocks subagent preload and, from v2.1.196, scheduled fires; "does not re-read the skill file on later turns"; 5,000 per skill and 25,000 combined after compaction: https://code.claude.com/docs/en/skills?m=1

**Studies, posts and other vendors:**
- Hadfield et al., 13 Jun 2025 (https://www.anthropic.com/engineering/multi-agent-research-system): all six authors; 4× and 15× ("In our data"; no method given); 90.2% with an Opus 4 lead and Sonnet 4 subagents against a single Opus 4, on an internal eval; breadth-first fit; shared-context poor fit; the coding line; "Agents are stateful and errors compound"; "agents duplicate work, leave gaps, or fail to find necessary information".
- Anthropic browser post, 24 Nov 2025 (https://anthropic.com/research/prompt-injection-defenses): Opus 4.5 at 8.0% and 1.4%; 100 attempts per environment; Claude for Chrome; "far from a solved problem".
- How Anthropic teams use Claude Code, 24 Jul 2025 (https://claude.com/resources/articles/how-anthropic-teams-use-claude-code): the phone tree, the React applications, "without understanding the code themselves", the product design loop.
- The PDF (https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf): "As a nontechnical team of one"; the finance sentence; "Save your state… 30 minutes"; "slot machine"; "Regularly commit your work…"; "security implications of deep MCP integrations".
- METR 2025, 10 Jul 2025 (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/): 16 developers, 246 issues, multi-year repositories, Cursor Pro with Claude 3.5/3.7 Sonnet; 19% slower; "AI makes them slower"; 24% expected and 20% believed; the caveats.
- METR 2026, 24 Feb 2026 (https://metr.org/blog/2026-02-24-uplift-update/): "an unreliable signal of the current productivity effect of AI tools"; developers declining to work without AI; raw estimates lean to a speed-up (−18% and −4%).
- Willison 2022 (https://www.simonwillison.net/2022/Sep/12/prompt-injection): 12 Sep 2022; he names the attack; Goodside's input; "The obvious parallel here is SQL injection".
- Willison 2025 (https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): 16 Jun 2025; the three legs; "LLMs follow instructions in content"; "avoid that lethal trifecta combination entirely"; "95% is very much a failing grade"; MCP mixing tools.
- Greshake et al. (https://arxiv.org/abs/2302.12173v2): six authors; v2 of 5 May 2023; the abstract quotes; Bing GPT-4 Chat, code completion and synthetic apps; data theft and worming.
- OpenAI prompt-injection post, 7 Nov 2025 (https://openai.com/index/prompt-injections/): "a frontier, challenging research problem"; "to only the sensitive data or credentials it needs"; explicit instructions; review confirmations.
- Karpathy, Verifiability: the quoted words match his X post of 16 Nov 2025 (https://threadreaderapp.com/thread/1990116666194456651.html). The bearblog page itself is unverifiable.
- Karpathy keynote: YC AI Startup School, 17 June 2025, and the "Autonomy Slider" concept (https://latent.space/s3). The three exact quotations are unverifiable because search did not return the transcription.
- Gemini CLI:
  - Subagents run in a "separate context loop" that "saves tokens in your main conversation history"; restricted tools; nothing on billing: https://geminicli.com/docs/core/subagents/
  - Checkpointing is off by default; a shadow Git repository in the home directory; snapshots before approved changes; /restore: https://www.geminicli.com/docs/cli/checkpointing
  - Sandboxing isolates shell commands and file changes; enabled by a flag, a variable or a setting; the default is not stated. Headline "Sandboxing in Gemini CLI": https://www.geminicli.com/docs/cli/sandbox. The unit's form of this address was not itself returned by search.

**Academy case file.** Every case fact in §9 and in Parts 1–3 matches the file:
- §1: private repository; two-place publishing; the index check.
- §2: one context per unit and why; the checker never edits; findings verified; the owner confirms; the fresh agents from BW7.
- §3: five tracks; 23 of 91; rewritten the same day.
- §5: 36, 28 and 58.
- §6: two dropped; the eighth check.
- §7: the lost writers; the transcripts; "fable"; the private terms; BW1's reply; the script.
- §9.

The "(Academy case)" label on first use (§9), the anecdote label and every [NOT IN CASE FILE] marker are correct.

## (6) Errata and pointers

There is no audit report and nothing to apply. I could not open pointers to BW1, BW2 (including routing-table row 8), BW3, BW5, BW6, BW7 or BW8 in this packet, so they are unverifiable. They agree with the brief's Takes and Gives lines and with the case file wherever those touch them. Part 3's "Sonnet 5.5, medium" is consistent with the best-practice page (Sonnet for routine work; 5.5 models default to medium effort).

## (7) Figures

1. **Flow, §1: PASS.**
   - Every label and note is in the §1 list: "Chat"/"one reply", "Chat with search"/"a short loop", "Research"/"searches which build on each other", "Claude Code session"/"file and shell tools", "Subagents"/"each with its own window", "Scheduled task"/"nobody watching".
   - The caption names the sections, the units and the dated vendor page.
   - Flow fits an ordered sequence.
2. **Compare, §4: PASS.**
   - The values 1, 4 and 15 and the three labels trace to §1 ("taking a chat as 1, an agent is about 4 and a multi-agent system about 15").
   - The caption gives the source, the date and the vendor label, and says why 7× is left out.
   - Compare fits.
3. **Decision, Deliverable Part 1: FIX.**
   - All labels are in the box text, the kind fits, and the caption is complete.
   - Box 3's "No" merges two exits, so a task whose check can be written is routed to "Chat drafts; you decide".
   - The replacement is in the findings list (exact Current and Fix); it adds the branch {"label": "no, but one can be written", "to": {"outcome": "Write the check first", "tone": 4}} and relabels the first "no" as "no, and none can be written". The caption is unchanged.

## (8) Writer's Source errors

None were listed, so there is nothing to confirm. Contradictions 1, 2 and 4 are confirmed on the live pages; item 4 led to the §4 should-fix.

## (9) Sourcing standard, Parts 1 and 6

**Met:**
- Claims are sourced where made. The §7 git bullets are labelled as the unit's own summary (stated opinion).
- Every opened source can be opened and is dated.
- Every quotation opened is exact.
- Each number says whose it is.
- Nothing invented was found.
- Every fact that can change is dated 16 Nov 2026.
- The Sources list matches the citations. The McKay line changes if the OpenAI fix is applied.
- Every practice carries an evidence grade.
- Studies name their models and tasks, and transfers are marked as inference.
- "On other tools" is present, with vendor pages or "not checked" or "none found". It names what is Claude-specific only generally, which is thin but acceptable.
- The case rules hold, and no private course or term appears.
- The deliverable is built on the case and then as templates with described blanks.
- The unit is not advice without evidence.

**Not met:**
- "The source says what the claim says" fails in four places: the Willison update date, "before building further", "three moves" and all hooks counted as deterministic.
- "Reporter kept separate": OpenAI's guide is reachable and should be cited itself.
- "Figure adds no fact": figure 3 drops a branch.

## (10) Persona read

The unit reads in order for an experienced professional who may not write code. Several terms are never explained:
- "worktree" and "MCP" (minors filed);
- "CI", "fan-out" (Box 5d) and "PreToolUse";
- "hook" and "deny rule", which §7 explains by kind but not by what they are.

Earlier units may define these (unverifiable). Nothing assumes a private course. The only names are the cited authors and the case file's "the owner".

## (11) Attribution pass

**Titles:** all match their headlines except the Anthropic browser post, whose heading is "Mitigating the risk of prompt injections in browser use" (minor). Karpathy's *Verifiability* page is unverifiable.

**Quotations against speakers:** all hold, with two exceptions:
- Willison's "extremely difficult" quotation is from his April 2023 update, not the 2022 post.
- Maginative's phrase is not OpenAI's (the unit says so; the fix replaces it).

**Figures against the page that states them for that thing:** all PASS.
- Vendor pages: 4× and 15× (chat baseline), 7× (standard session, plan mode), 90.2%, 8.0% and 1.4%, 5,000 and 25,000, v2.1.283, v2.1.196, 5–30, and 3 and 20.
- METR: 19%, 24%, 20%, 16 and 246.
- Case file: 36, 28, 58, and 23 of 91.

Verdict: BW9 · keep · 0 errors, 7 should-fix, 11 minor
