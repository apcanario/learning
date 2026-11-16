---
audit: fresh check
unit: BW8 · Skills and automation
course: building-with-ai · Building with AI
model: Opus 5.5 (claude-opus-5-5)
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
verdict: fix · 3 errors, 9 should-fix, 11 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW8 · fix · 3 errors, 9 should-fix, 11 minor

Model: claude-opus-5-5 (Opus 5.5)

The harness refused the write to /home/claude/w-bw8/checker/out/report.md ("Subagents should return findings as text"), so the full report is below. I checked that every Current string occurs exactly once in unit.md.

# Fresh check · BW8 · Skills and automation

- **What was checked:** the unit, on 16 Nov 2026, against brief.txt, sourcing-standard.md Parts 1 and 6, case-academy.md, notes.md and unsure.md. There is no audit report, so that step was skipped.
- **Web sources:** each one was found by WebSearch, then fetched from a URL that search returned.
- **Scripts:** I extracted the unit's SKILL.md, check.py and rotcheck.py and ran them locally:
  - check.py: lint, claims, sample, gate, and report on a mock report.
  - rotcheck.py: on a mock repository.

## Findings

[error] [attribution] §6; Current: "The three ways Claude Code can schedule work differ in what they reach, by the comparison table on *Run prompts on a schedule*:"; Problem: the table on *Run prompts on a schedule* gives the Desktop task's minimum interval as "1 minute" and the cloud task's permission prompts as "No (runs autonomously)". The values the sentence attributes to it ("at most hourly in its forms or every minute when Claude sets it", "starts in auto mode") come from the copy of the same table on *Schedule recurring tasks in Claude Code Desktop* ("1 minute when Claude sets it, 1 hour in the forms"; "Auto mode by default"). The facts are on a vendor page but are cited to the wrong one, and the two pages disagree; Fix: "The three ways Claude Code can schedule work differ in what they reach, by the comparison table as *Schedule recurring tasks in Claude Code Desktop* prints it ([Anthropic, Claude Code documentation](https://code.claude.com/docs/en/desktop-scheduled-tasks), read 16 Nov 2026; vendor). The copy of that table on *Run prompts on a schedule* gives the Desktop task's minimum interval as 1 minute and the cloud task's permission prompts as \"No (runs autonomously)\", so two of the vendor's own pages differ:"; Basis: https://code.claude.com/docs/en/desktop-scheduled-tasks.md (Compare scheduling options; Schedule options) and https://code.claude.com/docs/en/scheduled-tasks.md (Compare scheduling options)

[error] [figure] §1, decision figure; Current: "{"label": "yes", "to": {"outcome": "Project instruction: one rule, a line or two", "tone": 3}},"; Problem: "a line or two" appears nowhere in the unit's text. §1 says only that a project instruction is "the right home for a rule every chat must obey", and a figure may add no fact; Fix: "{"label": "yes", "to": {"outcome": "Project instruction: one rule", "tone": 3}},"; Basis: unit.md §1 ("It is the right home for a rule every chat must obey"); sourcing-standard Part 1 (a figure adds no fact)

[error] [deliverable] Deliverable B, SKILL.md Settings; Current: "- **Expected model:** large, top rung, not the writer's model: Fable 5.2, high. Override: Opus 5.5, high, recorded in the report as the writer's model."; Problem: the skill file holds dated model names. That goes against the unit's own §8 item 3 ("Model names, prices and limits belong in the project's dated files, which the skill names by path") and its Done-when line "Nothing in the skill folder is ... a dated product fact (§8)". The deliverable fails its own done-when line; Fix: "- **Expected model:** the model on rows 5 and 9 of the project's BW2 routing table, read from that file (path: `[NOT IN CASE FILE: where the case keeps its routing table]`), never the writer's model. Record in the report the model and version you ran as."; Basis: unit.md §8 item 3 and Deliverable G; https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md ("Don't include information that will become outdated")

[should-fix] [accuracy] Deliverable F, Settings; Current: "- **Schedule:** Custom, `7 7 1 * *`: 07:07 on the first of each month, a few minutes past the hour because a run set on the hour can start several minutes late. Monthly is BW4's cadence."; Problem: for a cloud scheduled task, a five-field cron expression is read in UTC ("when the expression is five fields alone, write the hours in UTC"). The run therefore fires at 07:07 UTC, not 07:07 local time. Also, Custom is chosen in the edit dialog after the task is created. This resolves the writer's unsure item 5; Fix: "- **Schedule:** Custom, `7 7 1 * *`: 07:07 UTC on the first of each month (a five-field expression is read in UTC; begin it with `CRON_TZ=<your time zone>` to write local hours), a few minutes past the hour because a run set on the hour can start several minutes late. Create the task with a preset, then choose Custom in its edit dialog. Monthly is BW4's cadence."; Basis: https://code.claude.com/docs/en/web-scheduled-tasks.md (Add a schedule trigger: Custom intervals; Cron expression time zone), read 16 Nov 2026

[should-fix] [accuracy] §2, claude.ai; Current: "Skills are on the Free, Pro, Max, Ultra, Team and Enterprise plans, and"; Problem: this is true of *Use skills in Claude*. But Anthropic's *Agent Skills* page lists custom skills on claude.ai, the kind the Deliverable uploads, as "Available on Pro, Max, Ultra, Team, and Enterprise plans", without Free. This is a product fact that differs between two of the vendor's own pages, which the unit's own skill lists as a failure kind; Fix: "Skills are on the Free, Pro, Max, Ultra, Team and Enterprise plans by the help page, while Anthropic's *Agent Skills* page lists custom skills, the kind the Deliverable uploads, on Pro, Max, Ultra, Team and Enterprise only (both read 16 Nov 2026); and"; Basis: https://support.claude.com/en/articles/12512180-use-skills ("Skills are available for users on Free, Pro, Max, Ultra, Team, and Enterprise plans"); https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md (claude.ai, Custom Skills)

[should-fix] [accuracy] §7, The case; Current: "It ran the same way each time: a context that has not seen the unit written, every cited claim against its source, findings graded and never edited (case file §2)."; Problem: the case file describes the method; it does not record that every run was the same. Its §5 shows three checker models across the 36 checks (Fable 5.1, Opus 5.5, Fable 5.2). Its §2 note says that who applied findings changed at BW7. The sentence stretches the source; Fix: "The case file describes it as one procedure: a context that has not seen the unit written, every cited claim against its source, findings graded and never edited (Academy case file §2); the checker's model varied across the 36 (Fable 5.1, Opus 5.5, Fable 5.2; §5)."; Basis: case-academy.md §2 and §5

[should-fix] [deliverable] Deliverable B, SKILL.md; Current: "Every step marked **script** is run with `scripts/check.py`, never done by eye."; Problem: every command calls `python3 scripts/check.py`, which is relative to the skill folder. In Claude Code the session's working directory is the repository root, while the skill is committed at `.claude/skills/check-against-sources/`. Claude Code's own example uses `${CLAUDE_SKILL_DIR}` "so it resolves correctly whether the skill is installed at the personal, project, or plugin level"; Fix: "Every step marked **script** is run with `scripts/check.py` in this skill's own folder (in Claude Code, `${CLAUDE_SKILL_DIR}/scripts/check.py`, because the session's working directory is the repository root), never done by eye."; Basis: https://code.claude.com/docs/en/skills.md (Generate visual output), read 16 Nov 2026

[should-fix] [label] §3, The front matter has to parse; Current: "The commonest way to break it is a colon followed by a space inside an unquoted value,"; Problem: "commonest" is a frequency claim with no source; Fix: "One way to break it (this unit's example; no page read says which way is commonest) is a colon followed by a space inside an unquoted value,"; Basis: sourcing-standard Part 6 (no uncited figures; a claim that cannot be sourced is said to be unsourced)

[should-fix] [deliverable] Deliverable G; Current: "- [ ] Nothing in the skill folder is a key, a password, a private term or a dated product fact (§8)."; Problem: check.py holds three dated product facts: CLAUDE_AI_DESC_LIMIT = 200, SPEC_DESC_LIMIT = 1024 and BODY_LINE_LIMIT = 500, each commented "read 16 Nov 2026". The folder fails this line even after the Expected-model fix. lint needs those limits to run without a network, and the line should say so; Fix: "- [ ] Nothing in the skill folder is a key, a password or a private term, and its only product facts are the three limits in `check.py` that `lint` needs to run without a network, each dated in its comment; re-read them at each rot check (§8)."; Basis: unit.md Deliverable C (check.py constants) and §8 item 3

[should-fix] [deliverable] Deliverable Part 2, Settings template; Current: "- **Expected model:** [from your BW2 routing table, rows 5 and 9: tier · model, effort, the date you read the vendor's page; a model other than the writer's]."; Problem: the blank asks the reader to write a dated model name into the skill, against §8 item 3 and the Done-when line; Fix: "- **Expected model:** [the path of your BW2 routing table; the skill reads rows 5 and 9 there, so no model name is written here; a model other than the writer's]."; Basis: unit.md §8 item 3

[should-fix] [attribution] Sources; Current: "- Anthropic. *Run prompts on a schedule*. Claude Code documentation. https://code.claude.com/docs/en/scheduled-tasks"; Problem: this goes with the §6 error. The page that carries the matrix's values must be listed; Fix: "- Anthropic. *Run prompts on a schedule*. Claude Code documentation. https://code.claude.com/docs/en/scheduled-tasks\n- Anthropic. *Schedule recurring tasks in Claude Code Desktop*. Claude Code documentation. https://code.claude.com/docs/en/desktop-scheduled-tasks"; Basis: https://code.claude.com/docs/en/desktop-scheduled-tasks.md

[should-fix] [figure] §6, matrix figure caption; Current: ""caption": "Claude Code's three ways to schedule work, by what each reaches (§6 of this unit). From Anthropic, Run prompts on a schedule, the table 'Compare scheduling options', read 16 Nov 2026 (vendor); a /loop task also expires seven days after it is created, by the same page.""; Problem: the caption names a page whose table does not carry the matrix's Desktop interval or the cloud task's "auto mode"; Fix: ""caption": "Claude Code's three ways to schedule work, by what each reaches (§6 of this unit). From Anthropic, Schedule recurring tasks in Claude Code Desktop, the table 'Compare scheduling options', read 16 Nov 2026 (vendor); the copy of the table on Run prompts on a schedule differs on two cells (§6). A /loop task also expires seven days after it is created, by Run prompts on a schedule.""; Basis: https://code.claude.com/docs/en/desktop-scheduled-tasks.md; https://code.claude.com/docs/en/scheduled-tasks.md

[minor] [attribution] §6; Current: "a recurring one expires seven days after it is created (read 16 Nov 2026; vendor)."; Problem: this goes with the §6 error. Once that sentence cites the Desktop page, the seven-day expiry needs its own page; Fix: "a recurring one expires seven days after it is created (*Run prompts on a schedule*, read 16 Nov 2026; vendor)."; Basis: https://code.claude.com/docs/en/scheduled-tasks.md (Seven-day expiry: "Recurring tasks automatically expire 7 days after creation")

[minor] [accuracy] §3, What a description cannot do; Current: "starts with "Check the description includes keywords users would naturally say", then rephrasing the request, then calling the skill by name;"; Problem: the page's second step is "Verify the skill appears in `What skills are available?`", and the sentence skips it; Fix: "starts with "Check the description includes keywords users would naturally say", then checking that the skill is listed, rephrasing the request and calling the skill by name;"; Basis: https://code.claude.com/docs/en/skills.md (Troubleshooting, Skill not triggering)

[minor] [accuracy] §3, Where sources disagree; Current: "end with a sentence that begins "Use when", which both pages' own examples do."; Problem: Anthropic's examples begin "Use when", but the agentskills.io guide's example begins "Use this skill when". The Deliverable's lint rejects that form, because it requires the string "use when"; Fix: "end with a sentence that begins "Use when", as Anthropic's examples do; the agentskills.io guide's example begins "Use this skill when", which the Deliverable's `lint` does not accept."; Basis: https://agentskills.io/skill-creation/optimizing-descriptions.md (Applying the result); https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md (Writing effective descriptions)

[minor] [attribution] §2; Current: "Anthropic's warning about installing skills is the same on both kinds of page:"; Problem: "both kinds of page" names nothing, and the quotations are cited to *Agent Skills* only; Fix: "Anthropic's developer documentation warns about installing skills:"; Basis: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md (Security considerations)

[minor] [style] §5; Current: "relative to the structure audit that found private terms in a public build (§7),"; Problem: "§7" reads as the unit's own §7, but the pointer means the case file's §7; Fix: "relative to the structure audit that found private terms in a public build (Academy case file §7),"; Basis: case-academy.md §7

[minor] [accuracy] Deliverable D, claude.ai step 1; Current: "On Team and Enterprise an owner enables it for the organisation first."; Problem: the help page says owners control this in Organization settings, and that it "is enabled by default at the organization level" on Team plans. I read this through a fetch summary; Fix: "On Team and Enterprise an owner controls it in Organization settings; on Team it is on by default (*Use skills in Claude*, read 16 Nov 2026)."; Basis: https://support.claude.com/en/articles/12512180-use-skills

[minor] [deliverable] Deliverable F, the prompt; Current: "If the script cannot run, push nothing and give its error as your last message."; Problem: rotcheck.py exits 1 whenever a step fails; tested, a swapped build order gives exit 1 with the report written. A run may read exit 1 as "cannot run" and push nothing; Fix: "If the script cannot run (it prints a Python traceback and writes no report), push nothing and give its error as your last message; an exit status of 1 with the report written means a step failed, and the branch is still pushed."; Basis: unit.md rotcheck.py docstring ("Exit 1 if a step fails"); local run on a mock repository

[minor] [deliverable] Deliverable F, on the case; Current: "Until it does, the script reports those files as missing, which is itself the first finding."; Problem: step 2 flags every file that no INDEX.md entry covers. Without index rows for `.claude/skills/` and `records/`, it flags both the committed skill and every earlier rot report; Fix: "Until it does, the script reports those files as missing, which is itself the first finding. INDEX.md also needs rows for `.claude/skills/` and `records/`, or step 2 reports the committed skill and every earlier rot report as unlisted."; Basis: unit.md rotcheck.py (step_2_3, covered); local run on a mock repository

[minor] [accuracy] Deliverable Part 1; Current: "Units are published as one website to anyone (§1), so the tier is 3."; Problem: the case file §1 says "as one website", "first as an artifact on claude.ai and then on GitHub Pages"; "to anyone" is not in it; Fix: "Units are published as one website, as an artifact on claude.ai and on GitHub Pages (Academy case file §1), so the tier is 3."; Basis: case-academy.md §1

[minor] [label] §2; Current: "([Agent Skills, *Specification*](https://agentskills.io/specification.md), read 16 Nov 2026; the format's documentation)."; Problem: "the format's documentation" is not one of Part 6's source classes, and the page names no publisher (unsure item 1). The Sources list files it as vendor; Fix: "([Agent Skills, *Specification*](https://agentskills.io/specification.md), read 16 Nov 2026; the format's documentation, whose publisher the page does not name; graded here as vendor documentation, as the Sources list files it)."; Basis: sourcing-standard Part 6; https://agentskills.io/specification.md

[minor] [deliverable] Deliverable Part 2, Scheduled task; Current: "- Schedule: [*a day of the month and a time a few minutes past the hour, written as cron: minute, hour, day of the month, then `* *`*]"; Problem: the blank does not say that a cloud task reads a five-field expression in UTC; Fix: "- Schedule: [*a day of the month and a time a few minutes past the hour, written as cron in UTC (or after `CRON_TZ=<your time zone>`): minute, hour, day of the month, then `* *`*]"; Basis: https://code.claude.com/docs/en/web-scheduled-tasks.md (Cron expression time zone)

## Confirmed

- §1: "Custom commands have been merged into skills"; `disable-model-invocation: true` means Claude cannot load the skill on its own, only `/name`. Source: https://code.claude.com/docs/en/skills.md
- §1: "keep pasting the same instructions, checklist, or multi-step procedure into chat"; "has grown into a procedure rather than a fact". Source: https://code.claude.com/docs/en/skills.md
- §1, §5, §8: the Academy case facts used (one person, Claude, Oct–Nov 2026; the structure audit's findings; the index-check and private-terms scripts). Source: case-academy.md §1, §7
- §2 skill definition: "A skill is a directory containing, at minimum, a `SKILL.md` file". Source: https://agentskills.io/specification.md
- §2 name rules, including "Must match the parent directory name". Source: https://agentskills.io/specification.md
- §2 description: 1–1,024 characters, "Describes what the skill does and when to use it". Source: https://agentskills.io/specification.md
- §2 "under 500 lines", with references one level deep. Source: https://agentskills.io/specification.md
- §2: reserved words `anthropic` and `claude`; no XML tags; "must include both what the Skill does and when Claude should use it". Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
- §2: about 100 tokens per skill at startup and a body under 5k tokens (spec and overview); for scripts, "only their output enters context" (overview).
- §2: "This feature requires code execution to be enabled"; Settings > Capabilities; Customize > Skills. Source: https://support.claude.com/en/articles/12512180-use-skills (H1 "Use skills in Claude")
- §2: "The ZIP should contain the skill folder as its root (not a subfolder)". Source: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- §2: personal skills load "but not Cowork or cloud sessions"; project skills "but not cloud threads in a project"; claude.ai account skills sync to `~/.claude/skills/synced/`, which needs v2.1.273 or later in terminal sessions. Source: https://code.claude.com/docs/en/skills.md
- §2 network: claude.ai skills have "full, partial, or no network access"; API skills have none. Source: platform.claude.com overview
- §2 box: "Custom Skills do not sync across surfaces"; Claude Code skills are "filesystem-based and separate from both claude.ai and the API". Source: platform.claude.com overview. The unit states this disagreement with the Claude Code page correctly.
- §2 security: "Use Skills only from trusted sources"; "can direct Claude to call tools or run code"; "Treat like installing software". Source: platform.claude.com overview
- §3: "the description carries the entire burden of triggering"; "Err on the side of being pushy"; "Use imperative phrasing"; a simple request "may not trigger a PDF skill even if the description matches perfectly". Source: https://agentskills.io/skill-creation/optimizing-descriptions.md
- §3: "potentially 100+ available Skills"; "provides the implementation details"; "Be specific and include key terms"; the three bad examples; "Always write in third person"; "The description is injected into the system prompt"; "can cause discovery problems"; "Processes Excel files and generates reports". Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md
- §3: the 1,536-character cap on description plus when_to_use, configurable through skillListingMaxDescChars; a budget that "scales at 1% of the model's context window"; descriptions dropped "starting with the skills you invoke least". Source: https://code.claude.com/docs/en/skills.md
- §3: "(200 characters maximum)". Source: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- §3 front matter: the opening `---` must be the file's first line; "the skill still loads with no fields set"; "can't match against your `description`". Source: https://code.claude.com/docs/en/skills.md
- §3 too-often fixes: make the description more specific, or set `disable-model-invocation: true`. Source: https://code.claude.com/docs/en/skills.md
- §3: "Try being more explicit in your request". Source: https://support.claude.com/en/articles/12512180-use-skills
- §3 and Deliverable D numbers, from a local run of the unit's own lint: description 193 characters, name 21, SKILL.md 122 lines, body 119 lines, `lint: PASS`.
- §4 method: about 20 queries, "8-10 that should trigger and 8-10 that shouldn't"; near-misses that "share keywords or concepts with your skill but actually need something different"; 3 runs each with a 0.5 threshold; roughly 60/40 train and validation; "Five iterations is usually enough"; a `claude -p` script that looks for a Skill tool call. Source: https://agentskills.io/skill-creation/optimizing-descriptions.md
- §4: "Review Claude's thinking to confirm it's loading the skill". Source: how-to-create-custom-skills
- §4 arithmetic: 1 − 0.05^(1/16) = 17.1% (recomputed as 0.1707).
- §5 degrees of freedom: low freedom where "Operations are fragile and error-prone"; "Prefer scripts for deterministic operations"; scripts are "more reliable than generated code", save tokens and keep results consistent. Source: best-practices.md
- §5: scripts are self-contained or document their dependencies, and "Include helpful error messages". Source: specification
- §6 cloud scheduled-task facts, all from https://code.claude.com/docs/en/web-scheduled-tasks.md:
  - "A cloud scheduled task, formerly a routine,"; research preview; may change.
  - Plans: Pro, Max, Team, Enterprise. Created at claude.ai/code/routines, in the desktop app, or with `/schedule`.
  - Repository cloned each run; `claude/` branch prefix; branch protection does not hold against bypassable access.
  - A run uses skills; connectors are included by default and can write; actions appear as you.
  - Trusted allowlist, with blocked requests failing with `403`; connectors bypass the allowlist.
  - Auto mode with a classifier; the fired prompt is not consent.
  - Hourly minimum; a run on the hour can start late; usage counts like interactive sessions; 100 scheduled runs an hour.
  - The prompt must be self-contained; API keys go in network secrets.
- §6: a cloud task has no local files ("No (fresh clone)"), and a recurring /loop expires after 7 days. Source: https://code.claude.com/docs/en/scheduled-tasks.md
- §7: 36 units checked, 28 with an error; no hours recorded. Source: case-academy.md §5, §9
- §7: the rule of three, attributed to Don Roberts and popularised in Fowler's *Refactoring* (1999). Source: https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)
- §7 arithmetic: 240 ÷ 15 = 16.
- §8: "Don't hardcode sensitive information (API keys, passwords)" (how-to-create-custom-skills); "Don't include information that will become outdated" and the "old patterns" section (best-practices.md); "move the rule into a hook" (skills.md).
- §9 OpenAI: *Using skills*, 10 Apr 2026: "A SKILL.md file is the skill's playbook"; @-mention; the page states no description limit, no scripts and no trigger test. Source: https://openai.com/academy/skills
- §9 Google post: by Deven Tokuno, 30 Sep 2026; "automatically run them whenever you enter a matching prompt"; `/` plus the skill name; reference files allowed; scripts not mentioned. Source: https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/
- §9 Gems timeline: read-only and converted 17 Nov 2026; removed 17 Dec 2026; Workspace business accounts March 2027; education June 2027; under-18 accounts later; 100 MB file limit; the page is undated. Source: https://support.google.com/gemini/answer/18560919
- §9 Gemini schedules: up to 10 active; a schedule uses another app only if it is connected; responses are prepared in advance. Source: https://support.google.com/gemini/answer/16316416?hl=en-GB
- Deliverable C and F scripts behave as the unit says in local runs:
  - Tier 3 draws n = 29 with seed 42.
  - The gate and report checks pass and fail as described.
  - rotcheck reports a swapped build order and lists the by-hand steps.

## (7) Figures

1. **Decision tree, §1: FIX.**
   - Traced to the text:
     - "rule every chat must obey" (§1)
     - "multi-step procedure" (§1)
     - "it is a line in the brief that needs it" (§1)
     - the count of three (§7 item 1)
     - "Write down each time you do the procedure by hand" (§7 item 1)
     - "Check that the runs were the same" (§7 item 2)
     - `disable-model-invocation` (§1)
   - Not in the text: "a line or two".
   - The caption is fine, and the kind fits.
   - Replacement: `{"label": "yes", "to": {"outcome": "Project instruction: one rule", "tone": 3}},`
2. **Comparison bars, §3: PASS.**
   - The four values all appear in §3: 193 ("The Deliverable's is 193"), 200 ("(200 characters maximum)"), 1,024 ("allow 1,024") and 1,536.
   - The caption names the section, the sources and the date; the kind fits.
3. **Flow, §5: PASS.**
   - Every label and note is in §5 or the SKILL.md steps: "sources, terms, quotations" (§5), "script, then the model adds" (step 2), "census or sample, by seed" (step 3), "form, counts, rule C5" (step 6), "BW7 §7 line" (§5), "verify, apply, publish" (step 7; §8 item 6).
   - The caption and the kind are fine.
4. **Matrix, §6: FIX (caption only).**
   - Every cell matches §6's text.
   - The caption names *Run prompts on a schedule*, whose table gives Desktop "1 minute" and cloud "No (runs autonomously)". The cells match the table on *Schedule recurring tasks in Claude Code Desktop* instead.
   - The kind fits.
   - Replacement caption: "Claude Code's three ways to schedule work, by what each reaches (§6 of this unit). From Anthropic, Schedule recurring tasks in Claude Code Desktop, the table 'Compare scheduling options', read 16 Nov 2026 (vendor); the copy of the table on Run prompts on a schedule differs on two cells (§6). A /loop task also expires seven days after it is created, by Run prompts on a schedule."

## (8) Writer's Source errors (notes.md)

1. **Headline is now "Use skills in Claude": confirmed.** The H1 of support.claude.com article 12512180 reads so. I fetched it at the slug search returned, `-use-skills`. The unit's slug, `-use-skills-in-claude`, was not fetched.
2. **"private to your individual account" is gone: confirmed.** The page now says custom skills "aren't visible to colleagues until you share them". The writer's added clause "sharing is on the Team and Enterprise plans" was **not confirmed** in my fetch.
3. **No data-persistence sentence on 16 Nov 2026: confirmed.** The page does not describe data persistence.
4. **The 1,536 cap is a configurable default** (`skillListingMaxDescChars`), and descriptions are dropped "starting with the skills you invoke least": **confirmed** on skills.md.
5. **The malformed front-matter sentence is still under Troubleshooting**, and "the skill still loads with no fields set" is in the front-matter reference: **confirmed** on skills.md.

## (9) Sourcing standard, Parts 1 and 6

### Part 1, per claim
- **Sourced where made:** yes, except "commonest" (should-fix).
- **Openable and dated:** yes.
- **The source says what the claim says:** no in four places:
  - the §6 table attribution (error);
  - the §7 "same way each time" (should-fix);
  - the §3 troubleshooting order (minor);
  - the §3 "both pages' own examples" (minor).
- **Reporter kept separate from the claim:** yes. Wikipedia is labelled as the reporter, and the book as unread.
- **Each number says whose:** yes. 17.1% and 240 ÷ 15 are marked as the unit's own arithmetic, and the minutes are labelled illustrative.
- **Views attached to named people:** correct.
- **Quotation marks hold the source's exact words:** yes for every quotation checked. The help-centre quotations were read through fetch summaries and matched.
- **Nothing invented:** none found.
- **A figure adds no fact:** fails twice. Figure 1 adds "a line or two", and figure 4's caption names the wrong page.

### Part 1, per unit
- **Unsourced claims marked:** yes; `[NOT IN CASE FILE]` is used where the case file is silent.
- **Changeable facts dated:** yes, but the cron time zone is missing (should-fix).
- **Sources list:** complete, except the Desktop page once the §6 fix is applied.
- **Closing material agrees with the body:** no. The skill file and the template put dated model names in the skill, against §8.

### Part 6
- **Recommendations sourced or graded:** yes. Design choices are labelled stated opinion.
- **Vendor sources labelled and dated:** yes. agentskills.io's class label is not one Part 6 names (minor).
- **Evidence grades:** present. Nothing is graded measured, and the unit explains why.
- **Studies:** none cited.
- **Product facts dated:** yes.
- **"On other tools":** present, and every cell is confirmed.
- **Claims carried over from the private unit:** re-read.
- **Private course:** none found. I searched for the owner's name, city, Learning Project, the private unit codes, "marketing course", "AI course", the repository name and "Mythology"; none appear.
- **Academy case:**
  - Cited by case-file section.
  - Labelled "(Academy case)" at first use, and as an anecdote.
  - Never the only support for a general claim.
  - One stretch (should-fix) and one "to anyone" not in the file (minor).
- **Deliverable:** built on the case, then given as a template whose blanks say what goes in them.
- **Advice without evidence:** no.
- **Links given as links:** yes.

## (10) Read as the brief's reader

- **Terms from earlier units:**
  - BW6 terms (rule C5, acceptance number zero, tiers, step F) and BW7 terms (stages, run-log form) are used without being restated.
  - The brief allows this, because each unit assumes the ones before it.
  - The unit's opening paragraph names the sections it relies on.
- **Model names:** "Fable 5.2", "Haiku 5.5", "row 5" and "row 9" come from BW2 and are cited to it. They are not private.
- **Command-line steps:** a non-coder must run python3, zip and git steps.
  - The template offers a claude.ai-only route and a by-hand option for the scheduled task.
  - The `${CLAUDE_SKILL_DIR}` gap (should-fix) would trip this reader in Claude Code.
- **Insider references:** no reference to a private course, its units or a personal name. The case is referred to only as Academy, the case, or the owner.

## (11) Attribution pass

### Sources titles against page headlines
- *Specification*: PASS
- *Optimizing skill descriptions*: PASS
- *Agent Skills*: PASS
- *Skill authoring best practices*: PASS
- *Extend Claude with skills*: PASS
- *Automate work with scheduled tasks*: PASS
- *Run prompts on a schedule*: PASS
- *Use skills in Claude*: PASS
- *How to create custom skills*: PASS
- *Using skills* (OpenAI, 10 Apr 2026): PASS
- Tokuno, D. (Deven Tokuno, 30 Sep 2026): PASS
- *About the transition from Gems to skills*: PASS
- *Schedules in Gemini Apps*: PASS. The search listing says "Schedule actions in Gemini Apps", but the page headline matches the unit.
- Wikipedia, *Rule of three (computer programming)*: PASS

### Quotations against speakers
All found on the named page, except the "both kinds of page" framing in §2 (minor).

### Figures against the page that states them
- These all PASS:
  - description limits: 200, 1,024, 1,536
  - skill sizes: about 100 tokens, under 5,000 tokens, 500 lines, 64 characters
  - schedule limits: 100 runs an hour, hourly minimum, 7-day /loop expiry
  - Gemini: 10 schedules, 100 MB, the Gems dates
- FAIL: the Desktop task's "1 hour in forms, 1 minute by Claude" and the cloud task's "auto mode" are attributed to *Run prompts on a schedule* but come from the Desktop page.

Verdict: BW8 · fix · 3 errors, 9 should-fix, 11 minor
