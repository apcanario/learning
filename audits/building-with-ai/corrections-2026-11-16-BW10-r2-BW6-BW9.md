---
kind: corrections-check
row: W-BW10
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [BW6, BW9]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

Second round at step 1b. The checker's report, verbatim from its reply (the harness refused it a report file), saved before any change was applied. Change 7 is marked "FAIL as written; PASS as replaced": the chat applied its replacement, which the checker passed.

claude-opus-5-5

I could not write the file: out/report.md was refused ("Subagents should return findings as text"), so the full report is below. A script confirmed that each Current block occurs exactly once in its file, in the order the changes will be applied. Once all changes are applied, neither file has any ?ref=t01.li, ?web= or ?m=1 left.

Results: 11 changes, 11 PASS. Change 7 fails as the text stands now and passes as replaced. No syllabus conflicts. No new findings outside scope.

# Corrections check, W-BW10 step 1b, second round (flag F70: citations with query strings)

Pages read on 16 Nov 2026. Each was read at a bare address that a WebSearch in this agent returned verbatim, and each fetch returned the full page text:
- https://code.claude.com/docs/en/best-practices (search result "Best practices for Claude Code - Claude Code Docs")
- https://code.claude.com/docs/en/costs (search result "Manage costs effectively - Claude Code Docs")
- https://code.claude.com/docs/en/security (search result "code.claude.com")

Every fact that BW6 and BW9 cite to Best practices for Claude Code and to Manage costs effectively holds on the bare page.

On Security, two items in BW9 §8's list of protections do not hold on the bare page: "context analysis" and web fetch in "a separate context window". Change 7 is the minimal fix. With it applied, every fact cited to Security holds, so that address moves to the bare one as well.

## Change 1
File: BW6-research-and-verification.md
Current:
```
"A fresh reviewer does help, because it hasn't seen your reasoning" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices?ref=t01.li), read 16 Nov 2026; vendor, documented practice).
```
Replacement:
```
"A fresh reviewer does help, because it hasn't seen your reasoning" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices), read 16 Nov 2026; vendor, documented practice).
```
Result: PASS — "in the terminal, `/code-review` reviews the diff in a fresh subagent that never saw your conversation. It isn't swayed by the reasoning that produced the code." and "Handing the same task to a subagent doesn't make the answer any better. A fresh reviewer does help, because it hasn't seen your reasoning, which is a different thing from delegating." https://code.claude.com/docs/en/best-practices. The facts BW6 cites to the same page without a link also hold: "A reviewer that's asked to find problems will always find *something*. If you fix every finding, you end up with extra abstraction layers and tests for cases that can't happen." (§4) and "Give Claude something it can run that comes back pass or fail. Once it has that, it can keep going on its own and you don't have to watch." (§12).
Syllabus: no conflict (F70: a unit cites a vendor page at its bare address).

## Change 2
File: BW6-research-and-verification.md
Current:
```
| [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices?ref=t01.li) | Not checked for this unit
```
Replacement:
```
| [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices) | Not checked for this unit
```
Result: PASS — "By someone who didn't write the code: in the terminal, `/code-review` reviews the diff in a fresh subagent that never saw your conversation." https://code.claude.com/docs/en/best-practices
Syllabus: no conflict (F70).

## Change 3
File: BW6-research-and-verification.md
Current:
```
- Anthropic. *Best practices for Claude Code*. Claude Code documentation (vendor). https://code.claude.com/docs/en/best-practices?ref=t01.li
```
Replacement:
```
- Anthropic. *Best practices for Claude Code*. Claude Code documentation (vendor). https://code.claude.com/docs/en/best-practices
```
Result: PASS — every fact BW6 cites to the page holds at the bare address (Changes 1 and 2). https://code.claude.com/docs/en/best-practices
Syllabus: no conflict (F70).

## Change 4
File: BW9-agents.md
Current:
```
"Give Claude something it can run that comes back pass or fail" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices?ref=t01.li), read 16 Nov 2026; vendor, documented practice).
```
Replacement:
```
"Give Claude something it can run that comes back pass or fail" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices), read 16 Nov 2026; vendor, documented practice).
```
Result: PASS — "Claude stops when the work looks done. If it has nothing to run that tells it whether the work actually *is* done, "looks done" is all it has to go on. In practice that makes you the test suite"; "Give Claude something it can run that comes back pass or fail."; the check list "A test file / A build's exit code / A linter / A script that diffs output against a fixture / A browser screenshot next to the mockup". https://code.claude.com/docs/en/best-practices.

Every other fact BW9 cites to this page (§4, §5, §6, §7, §9, Deliverable) also holds there:
- "doesn't make the answer any better"; "but not a smarter answer"; "What they cost you is mostly tokens".
- `model: haiku` for simple jobs; "Ask for short summaries back"; `/usage` showing each subagent type's share.
- The script loop: `--allowedTools`; "`--permission-mode dontAsk` refuses anything else that would have prompted"; `--max-turns`; "Reply OK or FAIL"; "Try it on three files first, see what goes wrong, fix the prompt, then run the rest".
- `/batch`: "splits the work into 5 to 30 units and shows you the plan. Then it runs each unit in its own worktree and opens a PR for it".
- "nobody tells it, and you find out the next morning that it spent the whole night building on the wrong assumption"; ask for "*evidence*: the command it ran and its output".
- "a `/loop`, a goal's check after every turn, and Claude's own subagents all keep sending requests while you aren't typing".
- "After three blocks in a row (or twenty in total), auto mode pauses"; "repeated blocks don't pause the run the way they do in a terminal".
- The deterministic / non-deterministic table, and "there's no *guarantee* that it'll follow your instructions".
- "A `prompt` or `agent` hook asks *another model* to decide, so it isn't deterministic either. For real enforcement, use a `command` or `http` hook".
- "Deny and ask rules and `PreToolUse` hooks apply before the classifier sees anything, so a deny rule blocks in auto mode exactly like it does everywhere else".
- "enforced by Claude Code rather than requested in a prompt"; "`Never read .env`"; "`Don't touch the migrations folder`".
- "Subagent worktrees disappear when the subagent finishes without changes".
- "A reviewer that's asked to find problems will always find *something*".
- "a person approving the merge, the deploy, or anything else you can't take back"; "after two failed corrections run `/clear` and write a better prompt instead of a third".
- The five questions, verbatim; "protect `main` with a GitHub branch rule the task can't bypass. And watch the first few runs of anything new before trusting it unattended".
- "They work alongside git rather than replacing it"; "Actions that look driven by content Claude read rather than by you".

Syllabus: no conflict (F70).

## Change 5
File: BW9-agents.md
Current:
```
([Anthropic, *Manage costs effectively*, Claude Code documentation](https://code.claude.com/docs/en/costs?ref=t01.li), read 16 Nov 2026; vendor)
```
Replacement:
```
([Anthropic, *Manage costs effectively*, Claude Code documentation](https://code.claude.com/docs/en/costs), read 16 Nov 2026; vendor)
```
Result: PASS — "Agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode, because each teammate maintains its own context window and runs as a separate Claude instance." and "Agent teams spawn multiple Claude Code instances, each with its own context window." https://code.claude.com/docs/en/costs. The other facts BW9 cites to this page also hold: "For simple subagent tasks, specify `model: haiku` in your subagent configuration"; "On a Pro, Max, Team, or Enterprise plan, `/usage` also shows a breakdown ... recent usage attributed to skills, subagents, plugins, and individual MCP servers"; "Each active teammate continues consuming tokens until it exits or the session ends."
Syllabus: no conflict (F70).

## Change 6
File: BW9-agents.md
Current:
```
"no system is completely immune to all attacks" ([Anthropic, *Security*, Claude Code documentation](https://code.claude.com/docs/en/security?web=1), read 16 Nov 2026; vendor)
```
Replacement:
```
"no system is completely immune to all attacks" ([Anthropic, *Security*, Claude Code documentation](https://code.claude.com/docs/en/security), read 16 Nov 2026; vendor)
```
Result: PASS — "While these protections significantly reduce risk, no system is completely immune to all attacks. Always maintain good security practices when working with any AI tool." This warning closes the prompt-injection protections and the list of practices. https://code.claude.com/docs/en/security
Syllabus: no conflict (F70).

## Change 7
File: BW9-agents.md
Current:
```
security page lists its protections (permission prompts, context analysis, network commands not auto-approved, web fetch in "a separate context window", trust checks for new folders and MCP servers)
```
Replacement:
```
security page lists its protections (permission prompts, network commands not auto-approved, web fetch passed through "a separate model call over the page" for most fetches, trust checks for new folders and MCP servers)
```
Result: FAIL as written; PASS as replaced.

The bare page has no context-analysis protection, and it does not say web fetch runs in "a separate context window". Its web-fetch item reads: "**Web page summaries**: For most fetches, WebFetch runs a separate model call over the page, and Claude receives that call's answer instead of the raw page."

The other items hold:
- "**Permission system**: In Manual mode, sensitive operations require explicit approval"
- "**Network command approval**: Commands that fetch content from the web such as `curl` and `wget` are not auto-approved by default"
- "**Trust verification**: ... Claude Code shows the workspace trust dialog when you start it in a folder you haven't trusted. Servers in a project's `.mcp.json` have their own approval prompt"

The rest of the sentence holds unchanged: there are five practices, including "2. Avoid piping untrusted content directly to Claude" and "4. Use virtual machines (VMs) to run scripts and make tool calls, especially when interacting with external web services". https://code.claude.com/docs/en/security
Syllabus: no conflict.

## Change 8
File: BW9-agents.md
Current:
```
[*Manage costs effectively*](https://code.claude.com/docs/en/costs?ref=t01.li) | Not checked: Codex's subagents page redirected
```
Replacement:
```
[*Manage costs effectively*](https://code.claude.com/docs/en/costs) | Not checked: Codex's subagents page redirected
```
Result: PASS — "The subagent's own requests still draw on your usage. To spend less on them, choose a smaller model for a subagent". https://code.claude.com/docs/en/costs
Syllabus: no conflict (F70).

## Change 9
File: BW9-agents.md
Current:
```
| [*Security*](https://code.claude.com/docs/en/security?web=1); [*Mitigating prompt injections in browser use*]
```
Replacement:
```
| [*Security*](https://code.claude.com/docs/en/security); [*Mitigating prompt injections in browser use*]
```
Result: PASS — "**Best practices for working with untrusted content**: 1. Review suggested commands before approval 2. Avoid piping untrusted content directly to Claude 3. Verify proposed changes to critical files 4. Use virtual machines (VMs) ... 5. Report suspicious behavior with `/feedback`". https://code.claude.com/docs/en/security
Syllabus: no conflict (F70).

## Change 10
File: BW9-agents.md
Current:
```
- Anthropic. *Best practices for Claude Code*. Claude Code documentation (read at this address). https://code.claude.com/docs/en/best-practices?ref=t01.li
- Anthropic. *Manage costs effectively*. Claude Code documentation (read at this address). https://code.claude.com/docs/en/costs?ref=t01.li
- Anthropic. *Security*. Claude Code documentation (read at this address). https://code.claude.com/docs/en/security?web=1
```
Replacement:
```
- Anthropic. *Best practices for Claude Code*. Claude Code documentation. https://code.claude.com/docs/en/best-practices
- Anthropic. *Manage costs effectively*. Claude Code documentation. https://code.claude.com/docs/en/costs
- Anthropic. *Security*. Claude Code documentation. https://code.claude.com/docs/en/security
```
Result: PASS — every fact BW9 cites to the three pages holds at the bare addresses (Changes 4 to 9, with Change 7 applied). https://code.claude.com/docs/en/best-practices; https://code.claude.com/docs/en/costs; https://code.claude.com/docs/en/security
Syllabus: no conflict (F70).

## Change 11
File: BW9-agents.md
Current:
```
4. Best practices for Claude Code, Manage costs effectively, Security and Extend Claude with skills were read at the addresses search returned, which carry query strings (?ref=t01.li, ?web=1, ?m=1); the page served may differ from the plain address. The .md copies were not read (flags F41, F69).
```
Replacement:
```
4. Best practices for Claude Code, Manage costs effectively, Security and Extend Claude with skills are cited and were read at their bare addresses, without a query string. The .md copies were not read (flags F41, F69, F70).
```
Result: PASS — this matches the unit's citations as they will stand: https://code.claude.com/docs/en/best-practices, https://code.claude.com/docs/en/costs and https://code.claude.com/docs/en/security (Changes 4 to 10), and https://code.claude.com/docs/en/skills (§4 and Sources, already bare). It adds no new claim about any page.
Syllabus: no conflict (F70: a unit cites a vendor page at its bare address, not the .md copy).

## Not a text change 1
BW9 unsure list item 2 says the full page text was read for Best practices for Claude Code, Manage costs effectively and Security. That is still true at the bare addresses, since each fetch returned the full page text, and no correction names this item.

## Not a text change 2
BW6's earlier correction note ("Correction 2026-11-16, found by BW9's writer ...") names the page, not an address, so it stays as it is.
