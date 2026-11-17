---
code: BW9
title: Agents
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: on
---

# BW9 · Agents

This unit was written with search on. Every page it cites was found by a web search and read on 16 November 2026 at the address the search returned; every product fact (a feature, a mode, a limit, a default) carries that date, and most documentation pages show no date of their own. A page that refused the fetch, failed to load or redirected elsewhere is marked "not checked" and was not retried. Each practice carries an evidence grade, as in BW1 to BW8: **measured** (a study or test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. Every study names the models and the task it tested; carrying its finding to a current model or to your work is this unit's inference, and is said to be. Four earlier units are used by name and not restated: BW5's flag-and-review rule, BW6's verifiability test (Deliverable, step I), BW7's gates and its rules for the final pass and for steps that can be re-run, and BW8's skill form.

**Interests.** This unit was written by an Anthropic model, and most of its product sources are Anthropic's own pages: a vendor describing its product. Nothing was weighted to favour them; you should still know.

## 1 · What an agent is, against a chat

BW1 §8 placed agents among the layers of an assistant: the same model reading the same kind of window, except that it fills much of that window itself, with the results of its own actions. BW7 §1 gave Anthropic's distinction between a workflow, whose steps you fix in advance, and an agent, which directs its own steps. This section adds the three properties that make the difference practical.

**Tools.** Anthropic's Claude Code documentation draws the line plainly: "Tools are what make Claude Code agentic"; without them, Claude can only respond with text. With tools it can read your files, edit them, run commands, search the web and act in connected services ([Anthropic, *How Claude Code works*, Claude Code documentation](https://code.claude.com/docs/en/how-claude-code-works), read 16 Nov 2026; vendor). A chat answers from what is in its window; an agent can change things outside it.

**A loop.** The same page describes three phases, "gather context, take action, and verify results", which blend and repeat; Claude decides each step "based on what it learned from the previous step, chaining dozens of actions together" (same page). Each tool result goes back into the window and shapes the next step, so the number of steps is not fixed when you start. The page calls the layer around the model that supplies the tools and manages what it sees the "agentic harness" (same page).

**Autonomy.** The model chooses each next step. How many of those steps happen without your approval is a setting, and you can interrupt at any point: in Claude Code, `Esc` stops the running action, and a message typed while Claude works is read before its next step (same page).

The line between a chat and an agent is graded, and the grades are features you already use:

- **A chat** gives one reply from the material in its window (BW1 §1).
- **A chat with search** runs a short loop: it searches, reads, and may search again (BW6 §1).
- **Research** on claude.ai is a lead agent that runs searches which build on each other (BW6 §1).
- **A Claude Code session** adds file and shell tools on a folder or repository, with a permission mode that sets what runs without asking (§2).
- **Subagents** are further contexts that a session starts, each with its own window, returning a summary (§4).
- **A scheduled task** runs the same loop with nobody watching (BW8 §6).

```viz
{"kind": "flow", "per_row": 2, "steps": [
 {"label": "Chat", "note": "one reply", "tone": 3},
 {"label": "Chat with search", "note": "a short loop", "tone": 3},
 {"label": "Research", "note": "searches which build on each other", "tone": 2},
 {"label": "Claude Code session", "note": "file and shell tools", "tone": 2},
 {"label": "Subagents", "note": "each with its own window", "tone": 4},
 {"label": "Scheduled task", "note": "nobody watching", "tone": 1}],
 "caption": "§1: the grades from a chat to an unattended agent, in the order of the list in §1, each a feature this course has already met (BW1 §1, BW6 §1, BW8 §6) or meets here (§2, §4). Claude Code's loop and tools from Anthropic, How Claude Code works, read 16 Nov 2026 (vendor)."}
```

**What the loop costs.** Two properties change when a loop replaces a reply. Errors compound: Anthropic's engineers, describing their multi-agent research system, head one section "Agents are stateful and errors compound". And tokens multiply: on their measurements, "agents typically use about 4× more tokens than chat interactions", and "multi-agent systems use about 15× more tokens than chats": taking a chat as 1, an agent is about 4 and a multi-agent system about 15 ([Hadfield, Zhang, Lien, Scholz, Fox and Ford, *How we built our multi-agent research system*, Anthropic Engineering, 13 Jun 2025](https://www.anthropic.com/engineering/multi-agent-research-system), read 16 Nov 2026; vendor, internal measurement on Anthropic's 2025 system, method not published). Whether the ratios hold for current models is not stated on any page read (BW6 records the same caveat). Everything below is about when the extra rungs pay for themselves.

## 2 · The autonomy slider, and verifiability as the test of what to delegate

### The slider

The term is Andrej Karpathy's, from his keynote at Y Combinator's AI Startup School on 17 June 2025. Describing a coding tool that ranges from completing a line to changing a whole repository, he said "you are in charge of the autonomy slider", and he argued that products should have one. His working rule is to "keep the AI on the leash": "I always go in small incremental chunks", so that each piece can be verified, because the model generates and the human verifies, and that loop should go as fast as possible ([transcription of *Andrej Karpathy: Software Is Changing (Again)*, yt-transcribe](https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html), read 16 Nov 2026; a third-party automatic transcription of the talk, which was not watched for this unit; stated opinion, a practitioner's account of his own practice). The primary source is the recording; the quotations rest on the transcription.

In Claude Code the slider is the permission mode. As of 16 Nov 2026 Anthropic's page lists six ([Anthropic, *Choose a permission mode*, Claude Code documentation](https://code.claude.com/docs/en/permission-modes), read 16 Nov 2026; vendor):

| Mode | What runs without asking | Best for (the page's words) |
|---|---|---|
| `default` (Manual) | Reads only | Reviewing every action yourself, sensitive work |
| `acceptEdits` | Reads, file edits, and common filesystem commands | Iterating on code you're reviewing |
| `plan` | Reads, plus classifier-approved commands when auto mode is available | Exploring a codebase before changing it |
| `auto` | Everything, with background safety checks | Long tasks, reducing prompt fatigue |
| `dontAsk` | File reads in your working directories and pre-approved tools; anything that would prompt is denied, though a mod you installed can still approve some of those calls | Locked-down CI and scripts |
| `bypassPermissions` | Everything | Isolated containers and VMs only |

Three facts from the same page decide how far you move the slider.

1. **The starting point is high.** With Claude Code v2.1.283 or later, auto mode is the built-in starting mode for interactive terminal and VS Code sessions; on earlier versions, only on Pro, Max and Team plans. In auto mode "A separate classifier model reviews actions before they run", blocking anything that escalates beyond your request, targets unrecognised infrastructure or "appears driven by hostile content Claude read". The page's own caveat: auto mode "does not guarantee safety", and is for tasks where you trust the general direction, not a replacement for review on sensitive operations.
2. **A boundary stated in the chat is not a rule.** The classifier treats one as a block signal, but "Boundaries are not stored as rules": it re-reads them from the transcript, so compaction can remove them. "For a hard guarantee, add a deny rule instead." That is BW1 §6's point, that no instruction layer is enforced, applied to an agent.
3. **Plan mode holds back edits, not commands.** In plan mode Claude "runs shell commands to explore" and writes a plan, and "does not edit your source" until you approve.

### Verifiability

Karpathy's second contribution names the test. In a post of November 2025 (first on X on 16 November) he writes that a task can be automated well when its environment is "resettable (you can start a new attempt)", "efficient (a lot attempts can be made)" and rewardable, with "some automated process to reward any specific attempt"; and that "Software 2.0 easily automates what you can verify" ([Karpathy, *Verifiability*](https://karpathy.bearblog.dev/verifiability/), read 16 Nov 2026; stated opinion; the page names no author, and the blog is Karpathy's). His subject is what neural networks can be trained to do; applying it to what you hand an agent is this unit's inference, and Anthropic's own advice makes the same cut for agents: "Claude stops when the work looks done", and without a check it can run, "In practice that makes you the test suite"; so "Give Claude something it can run that comes back pass or fail" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices), read 16 Nov 2026; vendor, documented practice). The page's examples of a check are a test file, a build's exit code, a linter, a script that diffs output against a fixture, and a browser screenshot beside the mockup.

BW6's Deliverable, step I, turned this into four questions you answer per task: can the output be broken into checkable claims or does it come with a pass-or-fail check; can a context that did not do the work run that check; does checking cost clearly less than doing; and is the residual risk acceptable. This unit uses those questions as they stand. What it adds is the link to the slider (stated opinion, on the sources above):

- **No check and none can be written:** the task stays at the chat end of the slider. A chat drafts and you decide, at a human gate (BW7 §3).
- **A check you run by reading:** a session you watch, in small chunks, as Karpathy describes.
- **A check that runs without you:** the task may move up the slider, as far as the guardrails in §7 allow.

Verifiability decides how far a task may go; the permission mode, the scope and the stop are how you hold it there.

## 3 · What a coding agent lets someone who does not write code build, and what it does not

Claude Code is sold for code, and its documentation says it can help with "anything you can do from the command line", writing docs and researching topics among them (*How Claude Code works*, read 16 Nov 2026). For a reader who does not write code, the useful question is narrower: what can you build that you cannot read?

**What the vendor's own teams report** (vendor; anecdotes, several teams, no measurement method published). Anthropic's account of its internal use, of 24 July 2025, says its legal team built prototype "phone tree" systems to route colleagues to the right lawyer; its data scientists built "entire React applications for visualizing RL model performance", working "without understanding the code themselves"; and its product designers set Claude to write a feature, run tests and iterate, then reviewed the result ([Anthropic, *How Anthropic teams use Claude Code*](https://claude.com/resources/articles/how-anthropic-teams-use-claude-code), read 16 Nov 2026). The longer PDF of the same title adds a growth marketer working "As a nontechnical team of one", says that "Finance teams with no coding experience can now execute complex data workflows independently", and gives the data scientists' method: "Save your state before letting Claude work, let it run for 30 minutes", then keep the result or start again; "Treat it like a slot machine" ([Anthropic, *How Anthropic teams use Claude Code*, PDF](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf), read 16 Nov 2026; vendor). Every one of these is a small internal tool whose output its builder can judge by looking at it: a router that sends you to a lawyer or not, a chart that shows the data or not, an ad that reads right or not.

**What the one controlled study found** (measured, on a different population). METR ran a randomised trial with 16 experienced open-source developers on 246 real issues in repositories they had worked on for years, using mainly Cursor Pro with Claude 3.5 and 3.7 Sonnet. With AI allowed, the tasks took 19% longer: "AI makes them slower". The developers had expected a 24% speed-up and, afterwards, still believed they had gained 20% ([METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, 10 Jul 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), read 16 Nov 2026; measured; the authors say the result may not apply to less experienced developers or unfamiliar code). Its follow-up on late-2025 tools gives raw estimates that lean toward a speed-up, and METR itself calls them "an unreliable signal of the current productivity effect of AI tools", partly because developers declined to work without AI ([METR, *We are Changing our Developer Productivity Experiment Design*, 24 Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/), read 16 Nov 2026). The study does not measure people who cannot code. What carries over (this unit's inference) is the gap between felt and measured speed: an agent's progress feels faster than it is, which is a reason to judge the output against a check you fixed before you started, not against how the session felt.

**What follows for someone who cannot read the code** (stated opinion, on the two sources above and §2):

- **You can build** a tool whose output you can check without reading its code: a script whose result you compare with a fixture you made by hand, a page you look at, a table you recount, a file that a second script validates. The check carries the whole weight, because your review of the code is missing.
- **You cannot build safely** anything whose failure you would not see: code that handles other people's data, sends or publishes, pays, deletes, or runs where you cannot watch it. Anthropic's own legal team, the same PDF reports, saw at once the "security implications of deep MCP integrations".
- **You need version control before you need anything else.** The slot-machine method works only because the state was saved first; the PDF's engineers say the same: "Regularly commit your work as Claude makes changes". §7 explains what git gives someone who does not write code.

## 4 · Subagents and isolated contexts: why they help and what they cost

### What a subagent is

Anthropic's page defines subagents as "specialized AI assistants that handle specific types of tasks". Each runs in its own context window, with its own system prompt, tools and permissions; it receives "only this system prompt plus basic environment details like the working directory", and it "doesn't see your conversation history", the skills already invoked or the files already read; it returns a summary ([Anthropic, *Create custom subagents*, Claude Code documentation](https://code.claude.com/docs/en/subagents), read 16 Nov 2026; vendor). A subagent can start subagents of its own, "up to three layers below the main conversation" by default (same page). The exception is a fork, which "starts with a copy of your conversation so far" (*How Claude Code works*, read 16 Nov 2026); Claude's own side tasks are forked while fork mode is on, which is the default (*Best practices for Claude Code*, read 16 Nov 2026). What follows describes a subagent that starts fresh: the kind you define and brief yourself.

Four facts on that page decide how you use them:

1. **The tool list is the scope that holds.** A subagent's `tools` field is an allowlist. Its `permissionMode` is weaker: when the main conversation is in `bypassPermissions`, `acceptEdits` or auto mode, the subagent runs in that mode and Claude Code ignores the one you set.
2. **It cannot ask you.** `AskUserQuestion`, the tool by which Claude asks you a question, is on the page's list of tools removed from every subagent. A subagent that meets a gap in its brief guesses or stops. Anthropic's research team saw the first: without detailed task descriptions, "agents duplicate work, leave gaps, or fail to find necessary information" (Hadfield et al., read 16 Nov 2026; vendor).
3. **The built-in readers are read-only.** Explore, "A fast, read-only agent optimized for searching and analyzing codebases", and Plan both have read-only tools, with Write and Edit denied; the general-purpose subagent has every tool available to subagents.
4. **When to use one.** Stay in the main conversation when the task needs back-and-forth, when "Multiple phases share significant context", or for a quick, targeted change; use a subagent when the task "produces verbose output you don't need in your main context", when you want tool restrictions enforced, or when the work is self-contained and can return a summary.

### Why they help

Two reasons, each documented. **Isolation keeps noise out of your window**: the subagent's tool calls stay in its context and you get back the summary (*How Claude Code works*). **A fresh context reviews better** because it has not seen the reasoning that produced the work; BW6 §4 gives the evidence and its limits. Anthropic's best-practice page now draws the line between the two sharply: handing the same task to a subagent "doesn't make the answer any better", while "A fresh reviewer does help, because it hasn't seen your reasoning" (*Best practices for Claude Code*, read 16 Nov 2026; vendor). By default a subagent is the same model or a smaller one on the same task, so you get parallelism or a fresh pair of eyes, "but not a smarter answer" (same page).

### What they cost, as the vendor publishes it (read 16 Nov 2026)

- **Each subagent spends its own tokens against your limit.** Its requests "count toward the same usage limits as your main conversation", and "each subagent spends tokens of its own while it runs" (*Create custom subagents*). "What they cost you is mostly tokens" (*Best practices for Claude Code*).
- **A fresh subagent may be slower.** It first has to gather context your conversation already had, so it can end up slower than doing the task where you are (same page).
- **The multipliers.** Anthropic's research system: agents about 4×, multi-agent systems about 15× a chat's tokens (Hadfield et al., 2025; vendor). Its multi-agent design beat a single Claude Opus 4 agent, with Claude Sonnet 4 subagents under an Opus 4 lead, by 90.2% on an internal research evaluation; the post says the gain is for breadth-first questions with independent directions, that tasks where every agent needs the same context are a poor fit, and that "most coding tasks involve fewer truly parallelizable tasks than research" (same post; vendor, internal evaluation). Claude Code's agent teams, several Claude Code instances each with its own context window, use "approximately 7x more tokens than standard sessions" when teammates run in plan mode ([Anthropic, *Manage costs effectively*, Claude Code documentation](https://code.claude.com/docs/en/costs), read 16 Nov 2026; vendor). The two pages measure against different baselines (a chat; a standard Claude Code session), so the figures are not comparable with each other.
- **What lowers it.** Set `model: haiku` on a subagent whose job is simple, such as collecting the files that import a module or checking links; ask for short summaries; read `/usage`, which on Pro, Max, Team and Enterprise breaks usage down by subagent (*Best practices for Claude Code*; *Manage costs effectively*). Which tier a task needs is BW2's routing table; this unit does not restate it.

```viz
{"kind": "compare", "unit": "×", "max": 16, "rows": [
 {"label": "Chat", "value": 1, "tone": 3},
 {"label": "Agent", "value": 4, "tone": 2},
 {"label": "Multi-agent system", "value": 15, "tone": 1}],
 "caption": "§1 and §4: tokens used, as a multiple of a chat interaction, on Anthropic's own measurement of its 2025 research system (Hadfield et al., How we built our multi-agent research system, Anthropic Engineering, 13 Jun 2025, read 16 Nov 2026; vendor, method not published). Claude Code's agent-team figure (about 7× a standard session) is left out because its baseline differs."}
```

### What a subagent loads, and how BW8's skill reaches it

BW8's skill form (BW8, Deliverable, and its §2 to §6) is what an agent in this unit loads when it needs a procedure. Four facts about that path, re-read on 16 Nov 2026 on Anthropic's *Extend Claude with skills* ([Claude Code documentation](https://code.claude.com/docs/en/skills); vendor):

- A subagent given a skill in its `skills` field has the skill's full content injected at startup, unlike a skill that loads when a request matches its description (same page).
- `disable-model-invocation: true` keeps Claude from loading a skill on its own, also prevents the skill from being preloaded into subagents, and from running when a session-scoped scheduled task fires with the skill as its prompt. A skill you mark this way cannot be handed to an agent.
- An invoked skill's text enters the conversation once and "Claude Code does not re-read the skill file on later turns"; the page's advice is to write guidance that must hold throughout a task as standing instructions.
- After compaction Claude Code re-attaches the most recent invocation of each skill, keeping its first 5,000 tokens, within a combined 25,000; older skills can drop out. A long agent run that invoked many skills may lose the earliest.

So a skill an agent runs puts its stop condition and its **Never** list at the top, inside the first 5,000 tokens, as BW8's form already does (inference from the page above).

## 5 · What agents do well

Three kinds of work have documented gains, and they share one property: a result that can be checked without trusting the agent.

**Parallel research.** Anthropic's research system is the measured case: the 90.2% gain above, on breadth-first questions with several independent directions (Hadfield et al.; vendor, internal evaluation). The fit is narrow on the same page: not tasks whose parts depend on each other, and fewer parallel parts in coding. In this course that work is already routed: BW6 §1 sends a question with several independent directions to Research and its report through the sampling rule.

**Repetitive edits.** One change, the same each time, across many files. Anthropic's best-practice page gives the method for a script loop: a prompt run once per file, `--allowedTools` to pre-approve the tools the change needs, `--permission-mode dontAsk` to refuse "anything else that would have prompted", `--max-turns` to cap each run, and a reply of OK or FAIL; "Try it on three files first", see what goes wrong, fix the prompt, then run the rest (*Best practices for Claude Code*, read 16 Nov 2026; documented practice). For one large mechanical change, `/batch` splits the work into 5 to 30 units, shows you the plan, runs each unit in its own worktree and opens a pull request for each (same page). The check for an edit of this kind can be a script: a search for the old text that returns nothing.

**Builds with tests.** The central claim of the same page: give Claude something that comes back pass or fail and "Claude can close that loop itself", making the change, running the check and fixing what broke before running it again (same page; documented practice). For someone who does not write code the equivalent is a fixture: a small input and the output you checked by hand, against which the agent's script is diffed (§3).

What the three share is BW6's step I, questions 1 and 2: a check exists and a context that did not do the work can run it.

## 6 · What they quietly wreck

Three failures look like success until someone checks.

**Silent wrong assumptions.** Anthropic's page describes the unattended case: while you watch, a missing piece of context costs a message or two; in a run started before bed, "nobody tells it", and you find out the next morning that it "spent the whole night building on the wrong assumption" (*Best practices for Claude Code*, read 16 Nov 2026; vendor). Subagents make the mechanism concrete, since they cannot ask (§4), and Anthropic's research team saw vague briefs produce duplicated work and gaps (Hadfield et al.). The same page's figure of speech for the opposite failure is worth keeping: "Claude stops when the work looks done" (§2). An agent's report that it is done is a claim, and the page asks you to request evidence: the command it ran and its output.

**Overwriting.** An agent writes files, and the undo has holes. Claude Code snapshots files before Claude's own edits, but, as of 16 Nov 2026 ([Anthropic, *Checkpointing*, Claude Code documentation](https://code.claude.com/docs/en/checkpointing), read 16 Nov 2026; vendor):

- "A file that only Bash commands changed isn't tracked and stays as it is."
- After most subagent runs, rewinding restores only files Claude had already edited in your conversation; "The subagent's edits to other files stay."
- Manual changes and edits from other concurrent sessions are normally not captured.
- Checkpoints are for session-level recovery; for permanent history the page says to keep using version control.

Beyond files: "Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed" (*How Claude Code works*). A message sent, a page published, a record deleted in a connected service: nothing in the session reverses them.

**Cost blowups.** Each multiplier is documented, and none shows while it runs.

- Agents and multi-agent systems use several times a chat's tokens, and every subagent's requests count toward the same limit (§4).
- Background work keeps spending: a `/loop`, a goal's check after every turn and Claude's own subagents all keep sending requests while you are not typing (*Best practices for Claude Code*); each active agent-team teammate consumes tokens until it exits (*Manage costs effectively*).
- Unattended runs keep going. In a terminal, auto mode pauses after three blocks in a row or twenty in total; in a non-interactive run, "repeated blocks don't pause the run the way they do in a terminal" (*Best practices for Claude Code*).
- Scheduled tasks "draw down subscription usage the same way interactive sessions do" ([Anthropic, *Automate work with scheduled tasks*, Claude Code documentation](https://code.claude.com/docs/en/web-scheduled-tasks), read 16 Nov 2026; vendor), and claude.ai, Claude Code and Claude Desktop count toward one limit (BW2 §6). How to keep a project inside its plan's limits is BW10.

## 7 · Guardrails: scopes, dry runs, review gates, and version control

Anthropic's best-practice page sorts every control into two kinds (read 16 Nov 2026; vendor). **Non-deterministic**: your prompt, your instruction file, a skill, the auto-mode classifier; the model reads them, "there's no guarantee that it'll follow your instructions". **Deterministic**: command and http hooks (a hook that asks another model to decide is not), deny rules, the sandbox in strict mode, managed settings, tests, branch protection, a person who approves the merge; Claude Code applies them whatever the model decided. Deny rules and pre-tool hooks run before the classifier sees an action, so a deny rule blocks in auto mode as it does everywhere else (same page). The rule this unit draws (stated opinion, on that page and on §2): **anything that must never happen is held by a deterministic control; the prompt states it as well, but never alone.** No single control is enough on the vendor's own account: auto mode "does not guarantee safety" (§2), and the security page ends its list of protections with "no system is completely immune to all attacks" ([Anthropic, *Security*, Claude Code documentation](https://code.claude.com/docs/en/security), read 16 Nov 2026; vendor). Guards are stacked.

### Scopes and permissions: what the agent may touch

- **Tools.** A subagent's `tools` allowlist (§4); on a script, `--allowedTools` with `--permission-mode dontAsk` (§5). A task whose output is a report gets read-only tools, which is "enforced by Claude Code rather than requested in a prompt" (*Best practices for Claude Code*).
- **Files.** One folder or file it may change, named in the brief and held by a deny rule on the paths it may not touch. The best-practice page's examples of rules that belong outside the instruction file are "Never read .env" and "Don't touch the migrations folder" (same page).
- **Branch.** A worktree or a branch of its own. Cloud scheduled tasks push to a `claude/` branch unless the prompt says otherwise, and branch protection limits that only if your connected access cannot bypass it: "a rule that access can bypass doesn't block a run's push" (*Automate work with scheduled tasks*).
- **Connectors.** None unless the task needs one. A scheduled task includes all your connectors by default; "Remove any the task doesn't need", because Claude can use an included one "including writes", and anything done through them "appears as you" (same page).
- **Mode.** `bypassPermissions` only in "isolated environments like containers, VMs, or dev containers without internet access", since it "offers no protection against prompt injection or unintended actions" (*Choose a permission mode*).

### Dry runs: effects you can throw away

- **Plan mode** for intent: a plan, and no edits to your source until you approve; it still runs commands to explore (§2).
- **The first three** of a batch, checked, before the rest (§5).
- **A branch or worktree run**, merged or deleted whole; subagent worktrees "disappear when the subagent finishes without changes" (*Best practices for Claude Code*).
- **A fixed budget.** `--max-turns` or `--max-budget-usd` on a script, a spend limit on your account; the page lists them under "What stops it?" (same page). In a prompt, a maximum number of attempts and what to do on reaching it.

### Review gates: who signs off

- **A check that runs**, pass or fail, before you look (§2).
- **A reviewer that did not write the work.** Claude Code's `/code-review` reviews the diff "in a fresh subagent that never saw your conversation". Tell it what to skip: "A reviewer that's asked to find problems will always find something", and fixing every finding produces extra layers and tests for cases that cannot happen (*Best practices for Claude Code*, read 16 Nov 2026). BW6 §4 and §6 cover what a fresh checker adds and how to check it.
- **You, at the gates BW7 placed.** BW7 §3 puts a human gate after any stage whose output fixes everything downstream, before anything irreversible, and at BW5's boundaries, where the flags raised during the work are decided (BW5 §9). Those gates stay where BW7 put them when a stage is handed to an agent; an agent run ends at a gate, it does not pass one.
- **Never an agent: the final pass and the steps that cannot be re-run.** BW7 §5 makes the final pass yours and never a model's; BW7 §6 marks a stage that sends, publishes or posts as not re-runnable, to run once, after the final pass. Neither is delegated. The best-practice page's fifth question reaches the same place from the vendor's side: who signs off, "a person approving the merge, the deploy, or anything else you can't take back". A scheduled task's own prompt cannot stand in for that person: the fired prompt "can't act as approval or consent for actions during the run" (*Automate work with scheduled tasks*).
- **Two misses, then a new brief.** "after two failed corrections run `/clear` and write a better prompt instead of a third" (*Best practices for Claude Code*).
- **Human intervention for high-risk actions.** OpenAI's guide to building agents calls human intervention "a critical safeguard enabling you to improve an agent's real-world performance" and names high-risk actions as one of its two triggers: "Actions that are sensitive, irreversible, or have high stakes should trigger human oversight". It calls guardrails "a layered defense mechanism" and recommends that you "maximize a single agent's capabilities first" ([OpenAI, *A practical guide to building agents*](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), read 16 Nov 2026; vendor, documented practice; the guide carries no date).

### The five questions before a run goes unattended

Anthropic's page asks five questions of any run you leave (*Best practices for Claude Code*, read 16 Nov 2026; documented practice): "Does it know what done looks like?"; "Can it check its own work?"; "What's it allowed to touch?"; "What stops it?"; "Where does the result go, and who signs off?". It adds a warning for cloud tasks: protect your main branch with a rule the task cannot bypass, and "watch the first few runs of anything new before trusting it unattended" (same page). Box 7 of the Deliverable is these questions, with two lines added from §8 and from BW8 §6.

### Version control as the undo, for someone who does not write code

Checkpoints miss shell edits, most subagent edits and other sessions' edits (§6), and the page says they "work alongside git rather than replacing it" (*Best practices for Claude Code*). Git is a record of saved states of a folder. In plain terms (this unit's summary of standard use, stated opinion, with the vendor pages cited for what they say):

- **A commit is a saved state.** Before any agent run, save one. Anything the run does after it can be thrown away by returning to it, whichever tool made the change. That is the "Save your state" of the slot-machine method (§3).
- **A branch is a copy you can discard.** A run works on its own branch or worktree (a worktree is a separate folder for one branch, so parallel runs do not touch each other's files; *How Claude Code works*); you keep it by merging, or delete it whole.
- **A diff is what changed.** You do not need to read code to read a diff of a text file, and a diff of a code file tells you which files the agent touched, which is a check of its scope.
- **What git cannot undo** is anything outside the folder: a sent message, a publish, a write through a connector, a deployment (§6). Those stay with you.

You do not need to run git yourself to use this. You can ask the agent to commit before it starts and to work on a branch, and Claude Code can use git as one of its tools (*How Claude Code works*); the commit you ask for in the prompt is non-deterministic, so the branch rule that holds is the deterministic one on the repository (above).

## 8 · Injected instructions in material an agent reads

An agent reads material you did not write: web pages, documents, emails, issues, other people's files. If that material contains instructions, the model may follow them. This is prompt injection, and it is the one risk in this unit that a careful brief cannot remove.

**The primary sources.** Simon Willison named the attack on 12 September 2022, after Riley Goodside showed that a translation prompt could be overridden by an input reading "Ignore the above directions"; Willison drew "The obvious parallel" with SQL injection, and, in an update of 13 April 2023, wrote that the fix he had proposed, passing instructions and data to the model separately ("parameterized prompts"), is "extremely difficult, if not impossible, to implement on the current architecture of large language models" ([Willison, *Prompt injection attacks against GPT-3*, 12 Sep 2022](https://www.simonwillison.net/2022/Sep/12/prompt-injection), read 16 Nov 2026; practice). Kai Greshake and colleagues then showed the indirect form, the one that matters for agents: LLM-integrated applications "blur the line between data and instructions", and an attacker who cannot reach your prompt can still succeed by "strategically injecting prompts into data likely to be retrieved". They demonstrated it against Bing's GPT-4-powered chat, code-completion engines and synthetic GPT-4 applications, with impacts including data theft and self-spreading "worming" ([Greshake, Abdelnabi, Mishra, Endres, Holz and Fritz, *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, arXiv:2302.12173v2, 5 May 2023](https://arxiv.org/abs/2302.12173v2), read 16 Nov 2026; preprint as read; also published in the Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec 2023), pp. 79–90; demonstrations rather than a rate).

**The working rule.** Willison's lethal trifecta of 16 June 2025 turns the mechanism into a test. An agent that combines access to your private data, exposure to untrusted content, and the ability to communicate externally can be tricked into sending your data to an attacker, because "LLMs follow instructions in content" and cannot reliably tell instructions apart by where they came from; his advice is to "avoid that lethal trifecta combination entirely", and he is sceptical of filters, since "in web application security 95% is very much a failing grade" ([Willison, *The lethal trifecta for AI agents: private data, untrusted content, and external communication*, 16 Jun 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), read 16 Nov 2026; stated opinion of a named practitioner). He adds that MCP (the Model Context Protocol, by which connectors and tool servers plug into an assistant) "encourages users to mix and match tools from different sources" (same post), which is how a chat with connectors can gather all three legs without anyone deciding to.

**What the vendors say and measure** (vendor, read 16 Nov 2026):

- **Anthropic** measured its own browser agent against an adaptive attacker. With the model alone, Claude Opus 4.5's attack success rate was 8.0%; with its improved safeguards, 1.4%, which the post's headline rounds to 1%; the post says "prompt injection is far from a solved problem" ([Anthropic, *Mitigating prompt injections in browser use*, 24 Nov 2025](https://anthropic.com/research/prompt-injection-defenses); vendor, measured internally, Claude for Chrome; an adaptive attacker given 100 attempts per environment, about 2,200 to 3,200 attempts per bar). The number is for browser use with Anthropic's own attacker; it says nothing about your setup except that the rate is not zero.
- **Claude Code's** security page lists its protections (permission prompts, network commands not auto-approved, web fetch passed through "a separate model call over the page" for most fetches, trust checks for new folders and MCP servers) and five practices for untrusted content, among them "Avoid piping untrusted content directly to Claude" and using virtual machines when interacting with external web services (*Security*). Auto mode's classifier blocks actions that look "driven by content Claude read rather than by you" (*Best practices for Claude Code*). `bypassPermissions` offers no protection against it (§7). A scheduled task's API trigger wraps the text it receives in a block labelled as untrusted data (*Automate work with scheduled tasks*).
- **OpenAI** calls it "a frontier, challenging research problem" and, among four steps for users, gives three that bear on agents: limit an agent's access "to only the sensitive data or credentials it needs", give specific instructions in place of broad latitude, and review confirmations before accepting them ([OpenAI, *Understanding prompt injections: a frontier security challenge*, 7 Nov 2025](https://openai.com/index/prompt-injections/); vendor).

**What follows** (stated opinion, on the sources above). Before an agent runs, list what it can read, what private material it holds and what it can send, publish or post. If all three are present, remove one, starting with the ability to send. A web-reading research agent holds no private material and can send nothing; a script that edits your files reads nothing from outside. The dangerous agent is the useful-sounding one that reads your inbox, browses the web and can reply. That is box 1 of the Deliverable, and it comes first because no check after the fact recovers data that has left.

## 9 · The Academy case: its agent failures and the rules that followed

Academy (Academy case) is a library of self-study courses built by one person with Claude in October and November 2026, with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9). It is one project by one person: everything below is an anecdote, and none of it is evidence about agents in general (case file §9: no control, no second project).

The case is agent-heavy by design: each unit is written in a new chat or a fresh agent context that sees only its brief and the units already filed, for the stated reason that leaked context is how a course starts repeating itself (case file §2); from BW7 of this course, writer, checker, applier, filer and corrections checker were each a fresh agent (case file §2, note of 16 Nov 2026). The failures its record holds, and what followed each:

| Failure (case file) | What followed (case file) | Reading against this unit (stated opinion) |
|---|---|---|
| Three units written from one research report produced by research agents across five tracks; Audit 1 found 23 of 91 claims failing, the three deliverables missing, and qualifiers the sources do not carry (§3) | The three units rewritten the same day; every later unit of that family checked by a fresh context before filing (§3) | The research was parallel work with a check, but the check came after units were built on it. Box 8 puts it before anything is kept (§5, §7) |
| Writer drafts with errors: 28 of 36 drafts had at least one error at the fresh check, 58 errors in all (§5) | The fresh check runs before filing; it never edits, and each finding is verified before it is applied (§2) | "Looks done" is not done (§6); the gate is a context that did not write the work (§7) |
| Writer agents lost to container restarts; one deep dive lost two, and the third resumed from the second's working files (§7) | The lost transcripts were checked by script; no rule adopted after the lost writers is recorded (§7, §9, lines added 17 Nov 2026) | Work that lives in files survives the agent; BW7 §2's hand-offs as files are the rule this suggests |
| Some sessions kept no agent transcript, so scripted checks of what each agent had read could not run; the agents' own reports stood in (§7) | Where a session kept no transcript, the record says so and the model recorded is the one each agent stated (§7, added 17 Nov 2026) | An agent's report of its own work is a claim (§6); BW7 §7's log keeps evidence of what was read |
| A session's model named "fable" resolved to a newer version than the method names (§7) | Its checks were recorded as owed again on the named version (§7) | Record what ran, not what was asked for (BW7 §7) |
| BW1's checker could not write its report; the chat saved the report from the checker's reply (§7, note) | Recorded in the unit's check record (§7, note); no rule recorded [NOT IN CASE FILE] | The report survived only in the reply: the hand-off went through conversation instead of a file (BW7 §2) |
| Private terms reached a public build (§7) | A script checks this course's data folder against a list of private terms, and the fresh checker checks each unit against it; the script that fails the build on a private term in a public course was added on 11–12 Nov 2026, when the two public courses were created, after the structure audit of 29 Oct 2026 (§7, added 17 Nov 2026) | Publishing is a step no agent passes alone (§7); a deterministic check sits before it |
| Figures failed their check by a separate agent; under an early rule, a figure failing three times was dropped (two were) (§6) | The owner's later rule: figures are fixed until they pass; one sitemap passed on its eighth check (§6) | A loop with a pass-or-fail check, re-run by a new agent each time (§5) |
| (Safeguard, not a failure) A script checks the course index after each filing chat inserts its records, and restores every file if the check fails (§1, note) | In place at filing (§1, note) | A deterministic undo of a scoped write (§7) |


**What the case cannot show.** No unit was written without the method, so nothing here shows that the fresh agents and checks beat a lighter setup; there is no measure of hours or money per unit (case file §9). The record does not say which permission mode the agents ran in, or whether any agent met injected instructions (case file §9). Filing and writing rows from 10 Nov 2026 on ran as Claude Code sessions on claude.ai attached to the Project; no scheduled task appears in the records; and the method has a checkpoint commit follow every agent (§7, lines added 17 Nov 2026).

## 10 · On other tools

The principles of §1 to §9 are stated for any agent: a loop with tools, a setting for how much runs without you, verifiability as the test of what to delegate, isolated contexts that cost tokens, an undo that stops at the edge of the folder, injected instructions in what the agent reads, and deterministic controls for anything that must never happen. The detail is Claude's. Read on 16 Nov 2026; pages that redirected or failed are "not checked" and were not retried.

| Claim in this unit | Claude | ChatGPT and OpenAI | Gemini and Google |
|---|---|---|---|
| Permission modes as the autonomy setting (§2) | [*Choose a permission mode*](https://code.claude.com/docs/en/permission-modes) | Not checked: Codex's approvals and sandboxing pages redirected to another site on 16 Nov 2026 | Sandboxing isolates shell commands and file changes from your system, switched on by a flag, a variable or a setting; the page does not say whether it is on by default: [*Sandboxing in Gemini CLI*](https://geminicli.com/docs/cli/sandbox/) |
| Subagents: own context, restricted tools, tokens (§4) | [*Create custom subagents*](https://code.claude.com/docs/en/subagents); [*Manage costs effectively*](https://code.claude.com/docs/en/costs) | Not checked: Codex's subagents page redirected on 16 Nov 2026 | Subagents run in an independent context loop that "saves tokens in your main conversation history", with a restricted set of tools; no billing statement on the page: [*Subagents*](https://geminicli.com/docs/core/subagents/) |
| Checkpoints and their limits; version control as the undo (§6, §7) | [*Checkpointing*](https://code.claude.com/docs/en/checkpointing) | Not checked (Codex pages redirected) | Checkpointing is disabled by default; when on, it commits a snapshot to a shadow Git repository in your home directory before approved file changes, restored with `/restore`: [*Checkpointing*](https://www.geminicli.com/docs/cli/checkpointing) |
| Prompt injection: guidance to users (§8) | [*Security*](https://code.claude.com/docs/en/security); [*Mitigating prompt injections in browser use*](https://anthropic.com/research/prompt-injection-defenses) | Limit access, give specific instructions, review confirmations: [*Understanding prompt injections*](https://openai.com/index/prompt-injections/) | No equivalent found on the pages read |
| A general agent in the chat app (§1) | Claude Code on the web, claude.ai/code (*How Claude Code works*) | Not checked: the ChatGPT agent help page failed to load on 16 Nov 2026 | Not checked for this unit |
| Scheduled, unattended runs (§6, §7) | [*Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks) | As BW8 §9 records: not checked | As BW8 §9 records: Schedules in Gemini Apps |

The studies in §3 and §8 name their own models (METR: Claude 3.5 and 3.7 Sonnet in Cursor; Greshake: GPT-4 systems; Anthropic's browser test: Claude models). Willison's and Karpathy's arguments are about language models in general.

## Deliverable · An agent-use decision rule, a guardrail checklist, and a brief for a first agent task

Three parts, each built in full on the Academy case and then given as a template. Part 1 is the decision rule in prose, with the line that holds on every path, drawn as a decision figure, and then run over the case's own tasks. Part 2 is the guardrail checklist, filled in for the case. Part 3 is the brief for a first agent task on the case. Part 4 holds the three templates, each blank saying what goes in it. Every box traces to the section named beside it; the rule as a whole is this unit's synthesis (stated opinion). Product facts are as read on 16 Nov 2026. DD-BW1 tests practitioners' methods against Part 1; BW10 costs the rules in Parts 1 and 2.

### Part 1 · The agent-use decision rule

Start at box 1 with a task you are about to hand to a model. Follow the arrows and stop at the first outcome you reach. If the task is one stage of a BW7 pipeline, run the rule once per stage, never once for the whole pipeline.

**Box 1 · All three trifecta legs?** Would the agent hold, at the same time, private material (your files, your accounts, other people's data), untrusted content (web pages, other people's messages or documents, anything you did not write) and a way to send, publish or post?
→ **Yes:** stop. Remove one leg, the way out first, then the private material, and start again at box 1.
→ **No:** box 2.
*(§8; Willison, 2022 and 2025; Greshake et al., 2023.)*

**Box 2 · Irreversible step?** Does the task include a step that no commit or checkpoint can undo: sending, publishing, posting, deleting outside the folder, paying, deploying, writing through a connector? And is any step BW7's final pass?
→ **Yes:** you do that step yourself, after your final pass. Only the part before it goes on to box 3.
→ **No:** box 3.
*(§6, §7; BW7 §5 and §6; How Claude Code works; Best practices for Claude Code, question 5.)*

**Box 3 · Pass/fail check a context can run?** Answer BW6's step I, questions 1 and 2: does the output come with a check that returns pass or fail, or break into claims a context that did not do the work can check against their sources?
→ **No, and none can be written** (a judgement, a choice of what to cut, a line in your voice): no agent. A chat drafts and you decide, at a human gate.
→ **No, but one can be written** (a script with no test, a format with no validator): write the check first, as its own small task, then return to box 3.
→ **Yes:** box 4.
*(§2, §5; Karpathy, Verifiability; BW6 step I; BW7 §3.)*

**Box 4 · Tools over dependent steps?** Does the work need tools over several steps, each depending on the last result: reading or changing files, running code, searching and reading?
→ **No, one answer from material in hand:** a chat, briefed by BW3.
→ **No, a question with several independent directions, worth a report:** Research, then BW6's sampling rule before anything is built on it.
→ **Yes:** box 5.
*(§1, §5; BW6 §1.)*

**Box 5 · Shape.** Which describes the work?
→ **(a) One change you could state in a sentence:** one session, no subagents.
→ **(b) Several phases sharing context (plan, build, test):** one session, plan mode first, no subagents.
→ **(c) Reading across many files, the result a summary:** a read-only subagent, with a complete brief, because it cannot ask.
→ **(d) The same change across many files:** a fan-out with allowed tools and `dontAsk`, on a branch or in worktrees; three files first, checked, then the rest.
Each shape takes its model from your BW2 routing table; a read-only subagent doing a simple job is the small tier's documented use.
Then box 6.
*(§4, §5; Create custom subagents; Best practices for Claude Code; BW2.)*

**Box 6 · Runs while you are not watching?** A scheduled task, a background or overnight run, a script loop?
→ **No:** a session you watch, in the mode the shape needs (plan for (b), Manual or auto otherwise). Go to box 8.
→ **Yes:** box 7.
*(§2, §6; BW8 §6.)*

**Box 7 · All five questions answered?** Every line must be true.
- It knows what done looks like: a goal, a spec, a failing test to turn green.
- It can check its own work: the check from box 3, run by the agent.
- What it may touch is held by a deterministic control: a tool list, a deny rule, `dontAsk`, a worktree, one branch it may push to, protected by a rule your access cannot bypass.
- Something stops it: a turn or spend cap, and an attempt cap in the prompt with what to do on reaching it.
- The result lands on a branch or in a report, and a person signs off.
- It holds no connector it does not need, and box 1 still holds for everything it can reach.
- Nothing in it waits on consent its own prompt would have to give.
→ **Any line false:** run it as a session you watch (box 6, "No").
→ **All true:** run it unattended, and watch its first few runs.
*(§7, the five questions; Automate work with scheduled tasks; BW8 §6.)*

**Box 8 · Before anything is kept.** The check has passed and you have its evidence (the command and its output). A reviewer that did not write the work has read the diff for gaps in correctness or the stated requirements, told to skip style. Anything to be published or filed has passed BW6's sampling rule and your final pass (BW7 §5). Flags the agent raised wait for your next BW5 boundary. After two failed corrections at any point, a new session with a rewritten brief.
*(§7; Best practices for Claude Code; BW5 §9; BW6; BW7 §3, §5.)*

**On every path.** Save a commit before any run, and let the run work on its own branch or worktree, because git is the undo and checkpoints are not (§6, §7). Never `bypassPermissions` outside an isolated container without internet access (§7). Every run carries its stop, and a brief complete enough that it never needs to ask (§4, §7).

```viz
{"kind": "decision", "title": "Agent or not", "root": {"q": "All three trifecta legs?", "tone": 4, "branches": [
 {"label": "yes", "to": {"outcome": "Stop: remove one leg", "tone": 1}},
 {"label": "no", "to": {"q": "Pass/fail check a context can run?", "tone": 4, "branches": [
  {"label": "no, and none can be written", "to": {"outcome": "Chat drafts; you decide", "tone": 3}},
  {"label": "no, but one can be written", "to": {"outcome": "Write the check first", "tone": 4}},
  {"label": "yes", "to": {"q": "Tools over dependent steps?", "tone": 4, "branches": [
   {"label": "no", "to": {"outcome": "A chat, or Research", "tone": 3}},
   {"label": "yes", "to": {"q": "Runs while you are not watching?", "tone": 4, "branches": [
    {"label": "no", "to": {"outcome": "A session you watch", "tone": 2}},
    {"label": "yes", "to": {"q": "All five questions answered?", "tone": 4, "branches": [
     {"label": "no", "to": {"outcome": "A session you watch", "tone": 2}},
     {"label": "yes", "to": {"outcome": "Run it unattended", "tone": 2}}]}}]}}]}}]}}]},
 "caption": "Deliverable Part 1: the spine of the agent-use decision rule, boxes 1, 3, 4, 6 and 7, from §2, §4 to §8 of this unit (Willison, 2025; Karpathy, Verifiability; BW6 step I; Anthropic, Best practices for Claude Code, its five questions, read 16 Nov 2026). Box 2 (irreversible steps), box 5 (shape), box 8 (before anything is kept) and the line on every path are in the text and not drawn."}
```

**The rule run over the Academy case.** Each row is a task the case file records, put through the boxes. The task and its facts are the case file's; the path and the outcome are this rule's reading of them (stated opinion), and where a box needs a fact the case file lacks, the row says so.

| Case task (case file) | Box 1 | Box 2 | Box 3 | Boxes 4 to 7 | Outcome under this rule | What the case did (case file) |
|---|---|---|---|---|---|---|
| Writing a unit from its brief, with sources cited in place (§1, §2) | Private repository (§1) and web pages read with search on; a way out only if the writer can publish; where transcripts were kept, writers used search and fetch and no connector, memory, Projects or Artifact tool (§7) | No, if the writer only writes a draft file | Yes: claims cited in place (§1); a fresh context checks them (§2) | Several phases sharing context: shape (b), one context per unit; watched or not: several writing rows ran unattended overnight or with the owner away (§2, §7) | An agent, one per unit, no publish tool, its draft kept only after box 8 | One new chat or fresh agent per unit (§2); fresh check before filing (§3, §5) |
| The fresh check (§2) | As the writer | No: it writes findings and never edits (§2) | Yes for each finding, which a maintainer verifies before applying (§2) | Reading a whole unit against its sources: a read-only agent | An agent, read-only, whose findings are claims checked before they are applied | A separate context that never edits (§2); from BW7, a fresh agent (§2, note) |
| Applying the findings (§2) | No web needed | No | Yes: each finding is applied as an exact replacement, which a diff shows (§2) | Edits across one file: shape (a) | An agent, its write scope one file, the diff read by a checker that did not apply it | From BW7, a separate applier agent, then a corrections checker (§2, note) |
| The figure check (§6) | No web needed | No | Yes: every label and number must already be in the text (§6), which a script can test | Many files, a summary back: shape (c) | An agent, read-only; better still a script, which Part 3 briefs | A separate agent; failed figures fixed and re-checked by a new agent (§6) |
| Research across several tracks (§3) | Web only, if it holds no private material | No | Yes, but only by sampling its claims (BW6) | Several independent directions: Research | Research, then BW6's sampling rule before any unit is written from it | Three units written from it; Audit 1 then failed 23 of 91 claims (§3) |
| Filing, rebuilding, publishing (§1, note) | Private repository and a public site | **Yes:** publishing reaches the public (§1, note) | The build is checked by script (§1, note) | Filing and the build are scripted steps | You publish, after your final pass; scripts and agents may file and build | The site is built by script, verified, and published in two places (§1, note); the session that works the row publishes and deploys, told to in 13 of 16 row asks read in full (§7) |
| Confirming a proposed task (§2) | n/a | n/a | No check can be written: a judgement | n/a | No agent: the owner decides | A proposed row is not worked until the owner confirms it (§2) |

### Part 2 · The guardrail checklist, on the Academy case

One line per guard, answered yes or no before a run. The case column holds only what the case file records; a blank the case cannot fill says so.

| # | Guard (section) | Academy case |
|---|---|---|
| 1 | No agent holds all three trifecta legs; the way out is removed first (§8) | Where transcripts were kept: writers used search and fetch and no connector, memory, Projects or Artifact tool; page checkers used only read, glob and grep inside their folder; figure re-checkers used no web tool (§7). Whether any agent held all three legs is not recorded |
| 2 | Steps that publish, send or cannot be re-run are done by a person, after the final pass (§7; BW7 §5, §6) | Publishing follows filing, a rebuild and a verify (§1, note); the session that works the row starts it, told to in 13 of 16 row asks read in full (§7); several writing rows were published without waiting for the owner (§2) |
| 3 | The task has a pass/fail check a context that did not do the work can run (§2; BW6 step I) | Yes for units and figures: a fresh check (§2) and a figure check (§6) |
| 4 | A commit is saved before the run, and the run works on its own branch or worktree (§7) | A checkpoint commit follows every agent; the history courses' figure passes worked on side branches; of 39 row asks held as text, one names a branch and none a worktree (§7) |
| 5 | The agent's tools are an allowlist; a report-only task has read-only tools (§4, §7) | The fresh check never edits (§2); how that is enforced is not recorded; where transcripts were kept, a script checked each agent's tool use (§7) |
| 6 | Paths it must not touch are held by a deny rule or hook, not only by the brief (§7) | [NOT IN CASE FILE] |
| 7 | No connector it does not need (§7) | Eight connectors were connected and no Project procedure used one, a finding that still applied on 16 Nov 2026 (§7, structure audit F14); where transcripts were kept, writers used no connector (§7) |
| 8 | Never `bypassPermissions` outside an isolated container without internet (§7) | Permission mode not recorded; one check ran in a Claude Code session on claude.ai (§7, note) |
| 9 | The brief is complete enough that the agent never needs to ask; one context per task (§4) | One self-contained brief per unit, never reworded (§2) |
| 10 | Every run has a stop: a turn or spend cap, and an attempt cap with what to do on reaching it (§6, §7) | Figure passes ran at most eight agents at a time and dropped a figure that failed twice; the public marketing course's re-run auditors were held to 40 searches each; four figure-pass asks gave an attempt cap (§7); no spend cap is recorded (§9) |
| 11 | Work is written to files as it goes, so a lost agent can be resumed (§9; BW7 §2) | The third writer resumed from the second's working files (§7) |
| 12 | The log records the model that ran and what the agent read (§9; BW7 §7) | Model recorded (§2); a "fable" session recorded as owed again (§7); transcripts missing in some sessions (§7) |
| 13 | A reviewer that did not write the work reads the output before it is kept (§7) | Fresh check before filing on 36 units (§5) |
| 14 | A deterministic check guards anything public (§7) | A private-terms script and the fresh checker's list check (§7, note); an index check that restores every file if it fails (§1, note) |
| 15 | An unattended run has passed all of box 7, and its first runs are watched (§7) | No scheduled task existed on the setup of 28 Oct 2026 or appears in the records of 16 Nov 2026; several rows ran unattended overnight or with the owner away instead (§7) |
| 16 | After two failed corrections, a new session with a rewritten brief (§7) | A failed figure was fixed and checked again by a new agent each time (§6); a rule on rewriting a brief after two failed corrections [NOT IN CASE FILE] |

### Part 3 · A brief for a first agent task, on the Academy case

The task: replace a judgement the case gives to an agent, the figure check (case file §6: every label and number in a figure must already be in the unit's text), with a script an agent writes and runs, so that the check moves from "a reader agrees" to pass or fail (§2). It is a good first task because it passes box 1 (no web, no connector, nothing sent), box 2 (it writes a script and a report, and changes no unit), and box 3 by construction (a fixture with a planted error is the check). It is written in BW3's brief form, with the lines an agent needs added; the folder of filed units is the one the case file names (§1, notes of 16 Nov 2026), and the report's date is marked to be filled before the brief is sent.

    TASK: Write and run a script that lists, for each figure block in the named units, every label and number that does not appear in the unit's text outside the figure.

    READER: the course's maintainer, who does not read code and will read the report, not the script. The report decides which figures go back to their writer (Academy case file §6).

    OUTPUT: two files and nothing else.
    - checks/figure_labels.py: reads one or more unit files; prints, per figure, each label or number not found in the text, or "clean".
    - reports/figure-labels-[FILL: date].md: one section per unit, one line per missing label with the figure's caption, and a last line "units: N · figures: N · missing: N".

    SCOPE AND TOOLS (held by the session's settings, stated here as well):
    - May read: courses/building-with-ai/ and checks/fixtures/.
    - May write: checks/figure_labels.py, checks/fixtures/, reports/ only.
    - May run: python3 on the script and its fixtures. No other commands.
    - Must not edit any unit, any brief or anything in courses/building-with-ai/. No web, no connectors, no git push.
    - Mode: dontAsk with an allowed-tools list for the above, on a branch named claude/figure-labels.

    CONSTRAINTS:
    - A label counts as present if it appears in the unit's text with the same words, ignoring case and markdown emphasis; a number counts as present if the same digits appear.
    - Report; never fix. A missing label is a finding for the maintainer, not an edit.
    - Avoid: changing a unit to make a check pass; widening the match until everything passes.

    CHECK (run before you report done):
    - Fixture A, checks/fixtures/clean.md: a unit whose every figure label is in its text. The script prints "clean".
    - Fixture B, checks/fixtures/planted.md: the same unit with one label changed inside its figure only. The script prints exactly that label.
    - Both results, with the commands and their output, go at the top of the report.

    STOP:
    - At most three attempts to make both fixtures pass. If they still fail, stop, write what you tried and the last output into the report, and make no other change.
    - If anything in this brief is unclear or a folder is missing, do not guess: stop and write the question at the top of the report.

    DONE WHEN:
    - Both fixtures give the expected output, shown in the report.
    - The report lists every unit named, with a count line.
    - git diff shows changes only under checks/ and reports/.
    - Nothing was published, pushed or sent.

    RESULT AND SIGN-OFF: the branch claude/figure-labels, merged or deleted by the maintainer after reading the report and the diff's file list.

    MATERIAL:
    <material>
    Units to check: every file in courses/building-with-ai/, one per unit, named by its code and title
    </material>

    TASK (again): Write and run the script, prove it on both fixtures, report, and change nothing else.

    Model: BW2 routing table, row 8 (a code change): mid · Sonnet 5.5, medium, read 15 Nov 2026.

**Before you send it** (the checklist of Part 2, for this task): commit saved; branch named; tools allowlisted; no connector; the stop and the "do not guess" line present; you will read the report and the diff's file list before merging. If the agent's report says "clean" for every unit on its first run, read the fixture results first: a script that passes everything has not been shown to catch anything until fixture B fails it (BW6 §6).

### Part 4 · Templates for your project

**4a · The decision rule, for your tasks.** One row per task you are thinking of handing over; run each stage of a BW7 pipeline as its own row.

| Task | Box 1: trifecta legs held | Box 2: irreversible steps (kept by you) | Box 3: the check, and who can run it | Box 5: shape | Box 6/7: watched, or all five answered | Outcome |
|---|---|---|---|---|---|---|
| [FILL: the task, by its name in your BW2 routing table or BW7 pipeline] | [FILL: private material it would hold · untrusted content it would read · ways it could send, publish or post; "none" where none] | [FILL: each step that sends, publishes, posts, deletes, pays, deploys or writes through a connector; or "none"] | [FILL: the test, script, fixture or source check; "none, judgement" if none can be written; "to write" if one can] | [FILL: a one-sentence change · phases sharing context · read-only summary · same change across many files] | [FILL: "watched", or each of the five questions with its answer] | [FILL: no agent · chat or Research · session you watch · unattended run] |

On every path: [FILL: where your commits live and the branch rule your agent runs cannot bypass]; never `bypassPermissions` outside [FILL: your isolated container, or "never"]; every run's stop is [FILL: your default turn cap, spend cap and attempt cap].

**4b · The guardrail checklist.** Copy the sixteen guards of Part 2. In the second column write, for your project, how each is held: [FILL: the setting, rule, file or habit that holds it, and whether it is deterministic (a setting, a rule, a script) or non-deterministic (a line in a prompt)]. Any guard held only by a line in a prompt and marked "must never happen" is moved to a deterministic control before the first unattended run.

**4c · A brief for your first agent task.**

    TASK: [FILL: the verb of the artefact, then the artefact; one task].

    READER: [FILL: who reads the output and what they will decide from it].

    OUTPUT: [FILL: each file the agent may create, with its path and form; "and nothing else"].

    SCOPE AND TOOLS:
    - May read: [FILL: folders or files].
    - May write: [FILL: the fewest paths possible].
    - May run: [FILL: the commands, or "none"].
    - Must not: [FILL: the paths, tools, connectors and actions it must not use; also held by FILL: the deny rule, tool list or mode that enforces each].
    - Mode and branch: [FILL: the permission mode, and the branch or worktree it works on].

    CONSTRAINTS:
    - [FILL: what the output must contain, stated positively].
    - Report; never [FILL: the action it must leave to you: publish, send, fix, merge].
    - Avoid: [FILL: named patterns, e.g. "changing the input to make the check pass"].

    CHECK: [FILL: the command it runs, and what pass looks like; a fixture with a planted error if the check is new].

    STOP:
    - At most [FILL: number] attempts; then [FILL: what it writes, and where].
    - If anything is unclear, do not guess: stop and write the question at [FILL: where].

    DONE WHEN:
    - [FILL: the check's result, shown with its command and output].
    - [FILL: the diff touches only the paths it may write].
    - Nothing was published, pushed or sent.

    RESULT AND SIGN-OFF: [FILL: the branch or report it lands on, and who reads it before anything is kept].

    MATERIAL:
    <material>
    [FILL: the files or list it works on, or "none"]
    </material>

    TASK (again): [FILL: the TASK line, repeated, with "and change nothing else"].

    Model: [FILL: the row of your BW2 routing table, with its tier, effort and the date read].

## Sources

All web pages read on 16 November 2026 at the address a web search returned. Vendor pages are labelled vendor in the text.

- Anthropic. *How Claude Code works*. Claude Code documentation. https://code.claude.com/docs/en/how-claude-code-works
- Anthropic. *Choose a permission mode*. Claude Code documentation. https://code.claude.com/docs/en/permission-modes
- Anthropic. *Create custom subagents*. Claude Code documentation. https://code.claude.com/docs/en/subagents
- Anthropic. *Checkpointing*. Claude Code documentation. https://code.claude.com/docs/en/checkpointing
- Anthropic. *Best practices for Claude Code*. Claude Code documentation. https://code.claude.com/docs/en/best-practices
- Anthropic. *Manage costs effectively*. Claude Code documentation. https://code.claude.com/docs/en/costs
- Anthropic. *Security*. Claude Code documentation. https://code.claude.com/docs/en/security
- Anthropic. *Automate work with scheduled tasks*. Claude Code documentation. https://code.claude.com/docs/en/web-scheduled-tasks
- Anthropic. *Extend Claude with skills*. Claude Code documentation. https://code.claude.com/docs/en/skills
- Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. and Ford, D. *How we built our multi-agent research system*. Anthropic Engineering, 13 June 2025. https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic. *Mitigating the risk of prompt injections in browser use* (page title: Mitigating prompt injections in browser use). 24 November 2025. https://anthropic.com/research/prompt-injection-defenses
- Anthropic. *How Anthropic teams use Claude Code*. 24 July 2025. https://claude.com/resources/articles/how-anthropic-teams-use-claude-code
- Anthropic. *How Anthropic teams use Claude Code* (PDF). https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf
- Karpathy, A. *Verifiability*. 17 November 2025. https://karpathy.bearblog.dev/verifiability/
- yt-transcribe. *Andrej Karpathy: Software Is Changing (Again) - transcription by yt-transcribe* (third-party transcription of the Y Combinator AI Startup School talk). https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html
- METR. *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. 10 July 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR. *We are Changing our Developer Productivity Experiment Design*. 24 February 2026. https://metr.org/blog/2026-02-24-uplift-update/
- Willison, S. *Prompt injection attacks against GPT-3*. 12 September 2022. https://www.simonwillison.net/2022/Sep/12/prompt-injection
- Willison, S. *The lethal trifecta for AI agents: private data, untrusted content, and external communication*. 16 June 2025. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T. and Fritz, M. *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. arXiv:2302.12173v2, 5 May 2023 (preprint as read). https://arxiv.org/abs/2302.12173v2
- OpenAI. *Understanding prompt injections: a frontier security challenge*. 7 November 2025. https://openai.com/index/prompt-injections/
- OpenAI. *A practical guide to building agents* (PDF, undated). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- Google. *Subagents*. Gemini CLI documentation. https://geminicli.com/docs/core/subagents/
- Google. *Sandboxing in Gemini CLI*. Gemini CLI documentation. https://geminicli.com/docs/cli/sandbox/
- Google. *Checkpointing*. Gemini CLI documentation. https://www.geminicli.com/docs/cli/checkpointing
- Academy case file (`generator/data/building-with-ai/case-academy.md`), §1, §2, §3, §5, §6, §7, §9.
- Units of this course cited by section: BW1 (§1, §6, §8), BW2 (§6; routing table, row 8), BW3 (the brief form), BW5 (§9), BW6 (§1, §4, §6; Deliverable, step I), BW7 (§1, §2, §3, §5, §6, §7), BW8 (§2 to §6, §9; Deliverable), BW10 (pointer only).

## Unsure list

1. Karpathy's keynote (§2): the quotations ("you are in charge of the autonomy slider", "keep the AI on the leash", "I always go in small incremental chunks") rest on a third-party automatic transcription (yt-transcribe, billmill.org), read through a fetch summary; the recording was not watched, and the talk's exact date (June 2025) was not verified on a Y Combinator page.
2. Several pages were read through fetch summaries, not line by line: Create custom subagents (definition, removed-tools list including AskUserQuestion, "up to three layers"), Choose a permission mode (the six-mode table and its quoted lines), Hadfield et al. (4×, 15×, 90.2%, "Agents are stateful and errors compound"), Willison 2022 and 2025, Greshake et al. abstract, Karpathy's Verifiability, both METR posts, both versions of How Anthropic teams use Claude Code, OpenAI's prompt-injection post, and the three Gemini CLI pages. Full page text was read for How Claude Code works, Checkpointing, Best practices for Claude Code, Manage costs effectively, Security and Automate work with scheduled tasks.
3. Mitigating prompt injections in browser use (§8): the fetch summary gave a table (Opus 4.5: 8.0% model only, 1.4% with improved safeguards) and also called the article's headline figure "1%"; the unit uses the table's 1.4%. Whether the headline 1% is a rounded figure or a different measurement was not checked.
4. Best practices for Claude Code, Manage costs effectively, Security and Extend Claude with skills are cited and were read at their bare addresses, without a query string. The .md copies were not read (flags F41, F69, F70).
5. Greshake et al.: the arXiv abstract page as read names no venue; the unit cites it as a preprint (v2, 5 May 2023). Whether it was later published at a peer-reviewed venue was not checked.
6. The OpenAI guide's position on human intervention is cited through Maginative's report (17 Apr 2025); OpenAI's guide (PDF) was not returned by a search and was not opened. The quoted words are Maginative's.
7. METR's 2025 study tested experienced developers; the unit's transfer to readers who do not write code (that felt speed outruns measured speed) is inference, and METR's 2026 update calls its newer raw data unreliable.
8. Building effective agents (Anthropic) refused the fetch on 16 Nov 2026 and was not retried; the workflow/agent distinction rests on BW7 §1's reading of the same day, and the unit quotes nothing from it.
9. The decision rule (Part 1), the guardrail checklist (Part 2) and the figure-label brief (Part 3) are untested: no agent was run on them for this unit, and whether a script can match figure labels as Part 3 specifies depends on the unit format, which the case file does not describe.
10. Version control in plain terms (§7) is this unit's summary of standard git use, not taken from a cited page; the vendor pages cited there support only that checkpoints miss shell and subagent edits, work alongside git, and that Claude Code can use git as a tool.
Object: none

Fresh check 2026-11-16 (Opus 5.5 (claude-opus-5-5)): keep · 0 errors, 7 should-fix, 11 minor; report `audits/building-with-ai/fresh-check-BW9.md`

Correction 2026-11-16, found by the corrections check of row W-BW9 (`audits/building-with-ai/corrections-2026-11-16-BW9-r2-BW8-BW9.md`, Change 2: no version on the page).

Correction 2026-11-16, corrections C-BW9-1 and C-BW9-2, worked at W-BW10 step 1b (`audits/building-with-ai/corrections-2026-11-16-BW10-C-BW9.md`).

Correction 2026-11-16 (second round), W-BW10 step 1b (`audits/building-with-ai/corrections-2026-11-16-BW10-r2-BW6-BW9.md`, Changes 4 to 11): bare page addresses (F70); §8's list of the Security page's protections now as that page states them.

*Correction, 17 November 2026: changed by this course's syllabus review (BW-1, row S-BW) after a corrections check by a fresh Opus 5.5 agent (audits/building-with-ai/corrections-2026-11-17-S-BW.md); see the course's changelog for what changed.*

Correction 17 Nov 2026 (CP-4), found by W-SP1, each change checked by a fresh Opus 5.5 agent against case-academy.md
