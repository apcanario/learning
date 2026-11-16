---
audit: fresh check
unit: BW5 · Specifying a project
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-15
chat: https://claude.ai/code/session_01KMmgQxb5xyzkrLHQ6hh6WQ
verdict: fix · 1 errors, 5 should-fix, 12 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW5 · fix · 1 errors, 5 should-fix, 12 minor

Model: claude-opus-5-5

(The harness refused the report file at /tmp/bw5/c/out/report.md, so the whole report follows.)

# Fresh check · BW5 · Specifying a project

Packet: /tmp/bw5/c (unit.md, brief.txt, notes.md, unsure.md, sourcing-standard.md Part 1 and Part 6, case-academy.md). No audit report: skipped. Live search on, 15 Nov 2026. Every URL fetched was returned verbatim by a WebSearch in this run. One fetch redirected (OpenAI Codex GitHub review page). It was not retried and counts as not checked.

## Findings

[error] [figure] §1 (bars figure); Current: "on a single run the gain was 4.2 points and not significant, and the spec-first runs used 1.38 times the tokens"; Problem: the bars figure plots 41.1/36.9 (one run), 48.9/46.4 (branch coverage) and 74.4/74.8 (line coverage), and none of those six numbers is in the unit's text, so the figure adds facts. The numbers themselves are right (Tufano et al. table: detect@1 36.9% to 41.1%, p=0.3075; branch 46.4% to 48.9%, p=0.0034; line 74.8% to 74.4%, p=0.3659); Fix: "on a single run it was 41.1% against 36.9%, a gain of 4.2 points and not significant; branch coverage was 48.9% against 46.4% (p = 0.0034) and line coverage 74.4% against 74.8%, not significant; and the spec-first runs used 1.38 times the tokens"; Basis: Tufano et al., arXiv 2608.17177 v2, https://arxiv.org/pdf/2608.17177
[should-fix] [accuracy] §10; Current: "It shows the method can be run across 194 units by one person."; Problem: a stretch of the case file. 194 is the library's total (§1), but the method as described, with a fresh check before filing, was applied to 36 units (§5), and only two sample audits had run (§9); Fix: "It shows one person running the method across five courses and 194 units, with a fresh check before filing on 36 of them (Academy case file §1, §5)."; Basis: Academy case file §1, §5, §9
[should-fix] [accuracy] §1; Current: "BW3 §5 sets out Laban and colleagues' measurement:"; Problem: the sentence carries numbers (39%, six tasks, fifteen models) sourced only through another unit. Part 1 asks for the source where the claim is made. The figures match the paper ("an average drop of 39% across six generation tasks"; 15 LLMs, Fig. 1 and §5); Fix: "BW3 §5 sets out Laban and colleagues' measurement ([Laban et al., *LLMs Get Lost In Multi-Turn Conversation*, arXiv 2505.06120, 9 May 2025](https://arxiv.org/pdf/2505.06120); preprint):"; Basis: https://arxiv.org/pdf/2505.06120
[should-fix] [figure] §4 (matrix caption); Current: "Read from the Gives lines of this course's map (§4 of this unit); BW5's Gives line names every later unit."; Problem: the figure's data sit in the Deliverable 1b table, not in §4, so the caption names the wrong section; Fix: "Data from the build order in Deliverable 1b of this unit, read from the Gives lines of this course's map; BW5's Gives line names every later unit."; Basis: unit, Deliverable 1b
[should-fix] [deliverable] Deliverable 1a; Current: "The method's full procedure: `method/` (BW4, Part 1)."; Problem: the unit says elsewhere that BW4's folders are its Deliverable Part 3, and it points to the rules file as "(BW4, Part 3)". `method/` is not among the BW4 names the writer says were kept (notes F30: INDEX.md, INSTRUCTIONS.md, records/, the rules folder, archive/). The line also reads as Academy's real layout, which the case file does not hold (notes F27); Fix: "The method's full procedure: the rules folder (BW4, Part 3; the case file does not record Academy's own layout)."; Basis: unit §0 and 2e; notes.md F27, F30
[should-fix] [coverage] §11; Current: "| Not searched for this unit | Not searched for this unit |"; Problem: the brief requires each Claude-specific claim to cite the other vendors' documentation "or says that no equivalent was found". "Not searched" does neither. Google documents a Gemini equivalent. The OpenAI Codex review page redirected in this check and was not read; Fix: "| Not checked: OpenAI's Codex code-review page could not be read on 15 Nov 2026 | Gemini CLI subagents, each operating \"within its own separate context window\" ([Wotherspoon and Patel, *Subagents have arrived in Gemini CLI*, Google Developers Blog, 15 Apr 2026](https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/); vendor, read 15 Nov 2026) |"; Basis: https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/
[minor] [attribution] Sources; Current: "- Lacan, O. *Keep a Changelog*"; Problem: needs a Sources entry if the Laban citation is added to §1; Fix: "- Laban, P., Hayashi, H. et al. *LLMs Get Lost In Multi-Turn Conversation*. arXiv 2505.06120 v1, 9 May 2025. https://arxiv.org/pdf/2505.06120 (preprint)\n- Lacan, O. *Keep a Changelog*" (\n = new line); Basis: https://arxiv.org/pdf/2505.06120
[minor] [attribution] Sources; Current: "- Young, J. *Effective harnesses for long-running agents*."; Problem: needs a Sources entry if the Gemini CLI citation is added to §11; Fix: "- Wotherspoon, J. and Patel, A. *Subagents have arrived in Gemini CLI*. Google Developers Blog, 15 April 2026. https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/ (vendor)\n- Young, J. *Effective harnesses for long-running agents*." (\n = new line); Basis: https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/
[minor] [accuracy] §9; Current: "and warns that changes kept in separate documents make the record harder to follow (Ubl, 2020)."; Problem: a stretch. Ubl observes that changes are often isolated into new documents, likens this to "the US constitution with a bunch of amendments", and recommends linking them from the original. He does not warn that the record is harder to follow; Fix: "and notes that in practice changes often go into separate documents, like amendments to a constitution, which should then be linked from the original (Ubl, 2020)."; Basis: https://www.industrialempathy.com/posts/design-docs-at-google/
[minor] [accuracy] §6; Current: "a **Status** (proposed, accepted, superseded)"; Problem: Nygard's status values also include "deprecated", so the list reads as complete when it is not; Fix: "a **Status** (proposed, accepted, deprecated, superseded)"; Basis: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
[minor] [accuracy] §11; Current: "converted to skills, for personal accounts ("; Problem: the page gives these dates for personal accounts of users 18 and over; under-18 accounts convert later; Fix: "converted to skills, for personal accounts of users 18 and over ("; Basis: https://support.google.com/gemini/answer/18560919
[minor] [accuracy] §1; Current: "the fixed versions of 90 historical Google production bugs"; Problem: the paper's dataset is "90 historical bug-fixes from Google's Internal Issue Tracking System"; "production" is not in the source; Fix: "the fixed versions of 90 historical bugs from Google's internal issue tracker"; Basis: https://arxiv.org/pdf/2608.17177
[minor] [figure] §1 (bars caption); Current: "writing tests for 90 Google production bugs"; Problem: same as above, "production" is not in the source; Fix: "writing tests for 90 historical Google bugs"; Basis: https://arxiv.org/pdf/2608.17177
[minor] [figure] §9 (states figure); Current: "{\"from\": \"raised\", \"to\": \"open\", \"label\": \"logged\"}"; Problem: the transition label "logged" is not in §9's text. It carries no fact, but under the figure rule every label must trace to the text; Fix: "{\"from\": \"raised\", \"to\": \"open\", \"label\": \"waits for a boundary\"}"; Basis: unit §9 step 2, "A flag waits for a boundary."
[minor] [accuracy] §5; Current: "The fresh check compares the unit with its brief (Academy case file §2)."; Problem: the case file says the check covers "every cited claim against its source and the deliverable against the brief"; Fix: "The fresh check compares the unit's claims with their sources and its deliverable with its brief (Academy case file §2)."; Basis: Academy case file §2
[minor] [label] Deliverable 1d; Current: "Length is inside the 2,000 to 6,000-word guide, or the unit's notes say why the topic needed more (§1)."; Problem: case file §1 holds the guide but not the notes clause, so the clause is cited to a section that does not hold it; Fix: "Length is inside the 2,000 to 6,000-word guide (§1), or the unit's notes say why the topic needed more (this unit's proposal)."; Basis: Academy case file §1
[minor] [style] §6; Current: "A session's model named \"fable\" resolved"; Problem: a public reader has not been told what "fable" is. The case file names Fable 5.1 as the auditing model; Fix: "A session's model named \"fable\" (Fable 5.1 is the project's auditing model, Academy case file §2) resolved"; Basis: Academy case file §2, §7
[minor] [deliverable] Deliverable 1c; Current: "READER: [NOT IN CASE FILE: the course's reader, as the preamble states it]"; Problem: 1c works the unit block on BW5 itself, and the writer holds this course's own preamble. That preamble is not a fact about Academy that the case file must supply. Leaving it blank makes the worked brief mostly empty. The same applies to the GOAL and TONE lines, the "Cover, in order" line, and the sentence above the block. The writer chose this deliberately (notes, Contradictions 2); the maintainer decides; Fix: "READER: an experienced professional who already reasons and writes well, uses a chat assistant most days with no method, may not write code, and brings one real project to build through the course; reads in order, on a phone, checks the citations, wants depth rather than a primer (this course's preamble)"; Basis: brief.txt preamble

## Confirmed

- Reed, 16 Feb 2025: three steps; "one question at a time"; spec.md; "small, iterative chunks that build on each other"; prompt_plan.md; todo.md checked off by the codegen tool; "The success really depends on how well step 2 went" (step 2 = Planning); "This is working well NOW…". https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
- Delimarsky, GitHub Blog, 2 Sep 2025: all five quotations verbatim; /specify, /plan, /tasks. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit
- Swaminathan and Singh, 14 Jul 2025: EARS acceptance criteria; design doc; the "generates tasks and sub-tasks…links each to requirements" quotation. https://kiro.dev/blog/introducing-kiro/
- Claude Code best practices (read 15 Nov 2026): SPEC.md interview; "start a fresh session to execute it"; "clean context focused entirely on implementation"; the files/interfaces/out-of-scope/verification sentence; "Time spent making the spec precise…"; "If you could describe the diff in one sentence, skip the plan"; "Claude stops when the work looks done"; "will usually report some, even when the work is sound"; "Chasing every finding leads to over-engineering"; "A fresh context improves code review…"; AskUserQuestion; plan mode; Writer/Reviewer; subagents. https://code.claude.com/docs/en/best-practices.md
- Tufano et al., arXiv 2608.17177 v2, 21 Aug 2026: ten Google authors; Gemini 3 Flash; same harness; 90 bugs; detect@5 63.2% against 53.4%, p=0.0352; detect@1 +4.2 points, n.s.; 1.38 times the tokens; SpecOps '26 in the ACM reference. https://arxiv.org/pdf/2608.17177
- Kwa et al., arXiv 2503.14499 v3, 25 Feb 2026: title; the 50% time-horizon definition; "doubled approximately every seven months since 2019"; software and research tasks. https://arxiv.org/html/2503.14499v3
- Young, 26 Nov 2025: "Written by Justin Young"; all quotations; JSON over Markdown; no published success figures. https://anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic Prompting best practices (read 15 Nov 2026): Opus 4.5 and 4.6 overengineering sentence; "Only make changes…"; "Don't add features…"; first window "to set up a framework"; "Review progress.txt, tests.json, and the git logs"; heading "Overeagerness". https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Böckeler, 15 Oct 2025, Thoughtworks: four quotations verbatim. https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Ubl, 6 Jul 2020: non-goals definition; "The system shouldn't crash"; 10–20 pages, 1–3-page mini doc; worth it only when the problem is ambiguous; "If the designed system hasn't shipped yet, then definitely update the doc". https://www.industrialempathy.com/posts/design-docs-at-google/
- Nygard, 15 Nov 2011: "It's better to avoid either blind acceptance or blind reversal."; "the forces at play"; "one or two pages"; superseded records kept. The "Decision" and "Consequences" phrases were consistent with the fetch, which only paraphrased them. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Scrum Guide, Nov 2020: all seven quoted phrases verbatim. https://www.scrumguides.org/scrum-guide.html
- Keep a Changelog 1.1.0: definition, purpose, Unreleased section. https://keepachangelog.com/en/1.1.0/
- Friel, 7 Oct 2025: all ExecPlans quotations ("Every ExecPlan is a living document"; "Contributors are required to revise it as progress is made, as discoveries occur…"). https://developers.openai.com/cookbook/articles/codex_exec_plans
- Ballinger, Kornder and Aitbayev, 17 Dec 2025: "formalize your intent"; "Once you approve the plan, run `/conductor:implement`"; no decision log. https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/
- Kotha et al., 7 Aug 2025, archived: "Prompting for less eagerness"; reasoning_effort; tool-call budgets. https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
- Google Gems to skills: read-only 17 Nov 2026, removed 17 Dec 2026, converted to skills, page undated. https://support.google.com/gemini/answer/18560919
- Laban et al. (via BW3 §5): 39% drop, six tasks, 15 LLMs. https://arxiv.org/pdf/2505.06120
- Academy case facts in §3, §5–§10 and Deliverable 1a–1f all match case-academy.md §1–§9: 2,000–6,000 words, 16,900; 194 units; syllabus shape; Audit 1 (1 in 8, 23 of 91, rewrite); Audit 2 passed; 36 checked, 28 with an error, 58/237/303; figure rule changed, two dropped, eighth check; writers lost and resumed; "fable"; no control.

## (7) Figures

1. bars · §1 · **FIX** (error). "Spec first", "Baseline", "Bugs caught in any of 5 runs" and 63.2/53.4 trace to "the spec-first agent's tests caught 63.2% of the bugs against 53.4% for the baseline". The numbers 41.1/36.9, 48.9/46.4 and 74.4/74.8 are not in the text. Apply the §1 text fix (error finding), and the JSON then stands. Also apply the caption fix "90 historical Google bugs". The caption names §1 and the source; bars fits numbers compared.
2. matrix · §4 · **FIX** (should-fix, caption). All eight rows match the Deliverable 1b table (for example, "| 8 | BW8 · Skills and automation | BW4, BW5, BW6, BW7 |"). Replacement caption: "The core units of this course as a dependency grid: each row takes from the columns marked. Data from the build order in Deliverable 1b of this unit, read from the Gives lines of this course's map; BW5's Gives line names every later unit. Every mark sits left of the row's own unit: nothing takes from a later unit." Matrix is acceptable for this shape.
3. states · §9 · **FIX** (minor). Every state, note and transition traces to §9's steps 1–3 ("raises a **flag**", "A flag waits for a boundary", "At the boundary, every open flag is decided", "Accept it, change it, or refuse it", "new version, with a decision-log entry", "recorded as refused, with the reason"), except "logged". Replace it with `{"from": "raised", "to": "open", "label": "waits for a boundary"}`. The caption is fine, and states fits a lifecycle.
4. flow · §10 · **PASS**. All eight steps and notes trace to the §10 bullets and to §7 ("a finished row moves to the changelog"). The caption names §10 and case file §2 and says it is an anecdote; flow fits a sequence.

## (8) Writer's Source errors (notes.md)

1. Claude Code: **confirmed**. The page reads "Once the spec is complete, start a fresh session to execute it."
2. Reed, test-driven: **confirmed**. Both the TDD and the non-TDD prompts read "break it down into small, iterative chunks that build on each other."
3. Reed, "across sessions": **not confirmed**. The page reads "Your codegen tool should be able to check off the `todo.md` while processing. This is good for keeping state across sessions." DD-B3's original wording is supported, so drop this correction. BW5's own text is correct.
4. Kiro: **confirmed**. The page holds "generates tasks and sub-tasks, sequences them correctly based on dependencies, and links each to requirements". The first proposed replacement is ungrammatical ("which it "sequences them…""), so use the unquoted variant.

## (9) Sourcing standard

Part 1
- Sourced in place: yes, except the Laban numbers, which come only through BW3 (should-fix).
- Openable: yes.
- Source says what the claim says: yes, with stretches at §10 "194 units", Ubl "harder to follow", the §5 description of the fresh check, and "production bugs".
- Reporter kept separate: yes.
- Whose figure: yes. "BW4's reading rate" could not be checked here.
- Views attributed correctly: yes.
- Exact quotation marks: yes for everything checked.
- Nothing invented: yes.
- Figures add no fact: no for the bars figure (error); the "logged" label is minor.
- P95 illustrations: not applicable.
- Per unit: unsourced claims are marked [NOT IN CASE FILE]; facts are dated; the Sources list is complete for what is cited directly; the closing material agrees with the body, except the 1d clause.

Part 6
- Grades: present in §1–§9.
- Preprint, vendor and practice labels: present.
- Study models and task, transfer called inference: yes for Tufano, METR and Laban.
- Product facts dated: yes.
- "On other tools": present, but two cells say "Not searched" and one says "Not checked" (should-fix for the review row; the ChatGPT plan-approval cell is honest but still a gap against the brief).
- Private course: no reference to DD-B3, the private course or its reader was found.
- Academy case: facts are cited by section; "(Academy case)" appears at first use in the §2 table; the anecdote label appears from §3 on; the case is never the sole support for a general claim.
- Deliverable on the case, then as templates: present (1a–1f, 2a–2e), with many [NOT IN CASE FILE] blanks (writer's Contradiction 2).
- Advice backed by evidence: passes.
- Links given as links: yes.

## (10) Read as the course's reader

- "fable" (§6, 1e D5) is never explained.
- "that family" (§6, §10, 1e D2) is the case file's internal word for a course and is undefined. Suggest "that course and those after it".
- "fresh check" is used in §5 before §10 defines it. Add "(§10)" at the first use.
- `method/` and `briefs/<course>/` in 1a read as Academy's real paths (should-fix above).
- BW2 row 10, BW3 template 7 and BW4's reading rate rely on earlier public units, which is acceptable.
- No private names, tools or reader details appear.

## (6) Pointers

Pointers to BW3 (§1, §3, §5, template 7, the brief form, conventions) and BW4 (§2, §4, §5, Part 3) are plausible from the Takes line. Pointers to BW1 §2, BW1 §7, BW2 §7 and BW2 row 10 are plausible as cross-references in a course read in order. Note that BW5's own 1b lists BW1 as giving only to BW3, BW4 and BW6, and BW2 only to BW7 and BW10, so these cross-references sit outside the grid BW5 draws itself. This is not an error. "BW4, Part 1" in 1a conflicts with the unit's "Part 3" elsewhere (should-fix). No BW unit could be opened from the packet, so these are checked for plausibility only.

## (2) Unsure list

1. Tufano: PASS. Branch coverage is significant (p=0.0034); the error fix adds it to the text.
2. METR: PASS.
3. Young: PASS.
4. Nygard: PASS, with "deprecated" missing (minor).
5. Scrum: PASS.
6. The Opus 4.5 and 4.6 note: PASS; the page names only those two.
7. Böckeler date: PASS.
8. Gems: PASS for adult personal accounts (minor).
9. ChatGPT: still not checked.
10. Build order: unverifiable, since the course map is not in the packet. The table and matrix are internally consistent, and nothing takes from a later unit.

Verdict: BW5 · fix · 1 errors, 5 should-fix, 12 minor
