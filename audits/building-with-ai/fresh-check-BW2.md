---
audit: fresh check
unit: BW2 · Choosing the model and the effort
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-15
chat: https://claude.ai/code/session_01KMmgQxzcKees9HpTU63jhW
verdict: fix · 1 errors, 5 should-fix, 10 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW2 · fix · 1 error, 5 should-fix, 10 minor

Checker: Opus 5.5 (claude-opus-5-5), isolated agent working only from the packet, live search on, 15 Nov 2026. The harness refused the write to out/report.md, so the full report follows here. The unit was not edited.

# BW2 · Fresh check

Brief: brief.txt. Sourcing: Part 1 and Part 6. Audit errata: none for this course, so that step was skipped.

## (1) Coverage
- Cost per task rather than per token: covered (§1).
- Tiers as a pattern that outlives any lineup: covered (§2).
- What effort and thinking settings do, from the vendors' documentation: covered (§3).
- Where quality differences show and where they do not, with benchmark limits (who ran it, which version, which date): covered (§4).
- Self-preference, and why a check runs on a different model or in a fresh context: covered (§5).
- Subscription against the API: covered (§6).
- Rule for re-deciding when the lineup changes: covered (§7).
- "On other tools" section: covered (§8).
- Dated appendix: covered. It has the Claude lineup with prices and plan limits, an OpenAI pointer row (API only; ChatGPT plans are said to be unread) and a Google pointer row.
- Deliverable: covered. It has ten tasks on the case, each with tier, effort, reason and override trigger, then the template with blank rows.

## Findings
[error] [figure] §7, decision figure; Current: "OpenAI's guide advises evaluating effort levels against your own evals ([*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md)); grade: documented practice."; Problem: two of the figure's labels, "Does it cost less, or use less of the plan?" and "Keep the row; re-date it", are not in the unit's text. The figure's branch that changes a row only when the new option is as good and cheaper is not in the text either. Rule 4 lists what to compare but never states this decision, and no rule says to re-date a kept row. A figure may add no fact. Fix: "OpenAI's guide advises evaluating effort levels against your own evals ([*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md)); grade: documented practice. If the new option is as good on all three when checked, and costs less or uses less of the plan, change the row and log it (step 6); otherwise keep the row and re-date it with the day you re-read the pages (stated opinion)."; Basis: sourcing-standard Part 1 (a figure adds no fact); unit §7.

[should-fix] [accuracy] §6, "What a subscription buys"; Current: "Two of the vendor's pages disagreed on the day; check the plan page on the day you buy."; Problem: Anthropic's own help article on Ultra settles the conflict. This check found it by search and read it on 15 Nov 2026. It says "The Max 20x plan is now called the Ultra plan": $200 a month, 10x Pro weekly usage, no five-hour limit for verified accounts. So the claude.com/max copy is current, and the ?hsLang=en copy and the Max price article are out of date. Fix: "Anthropic's help article on Ultra, read the same day, says the Max 20x plan is now called the Ultra plan ([Claude Help Center, *What is the Ultra plan?*](https://support.claude.com/en/articles/17728952), read 15 Nov 2026), so the second copy and the Max price article are out of date; check the plan page on the day you buy."; Basis: https://support.claude.com/en/articles/17728952

[should-fix] [accuracy] §6, "How usage is metered"; Current: "Every plan has a session limit that resets five hours after your first message, and paid plans"; Problem: this contradicts the unit's own §6 and appendix, and Anthropic's plan page and Ultra article: Ultra on a verified account has no five-hour limit. Fix: "Every plan except Ultra on a verified account has a session limit that resets five hours after your first message ([*What is the Ultra plan?*](https://support.claude.com/en/articles/17728952)), and paid plans"; Basis: https://claude.com/pricing/max ; https://support.claude.com/en/articles/17728952

[should-fix] [label] §5, "The case"; Current: "So a checker of the same model as the writer, in a fresh context, still found errors in two thirds of the drafts it read."; Problem: the case file records the checker of each draft (§5) but not the writer of each draft. "Same model as the writer" rests on §2's general statement of the method (writer's unsure item 10). Fix: "So a checker of the model the method names as its writer (case file §2; the file does not record the writer of each draft), in a fresh context, still found errors in two thirds of the drafts it read."; Basis: Academy case file §2, §5.

[should-fix] [figure] §5, bars caption; Current: "The writer was Opus 5.5 (case file §2)."; Problem: same as the finding above. Fix: "The method names Opus 5.5 as the writer (case file §2); the writer of each draft is not recorded."; Basis: Academy case file §2, §5.

[should-fix] [attribution] Deliverable Part 1, row 3; Current: "The result of a fresh check, summarised for the maintainer who verifies each finding before applying it (case file §2)"; Problem: the case file says a maintainer verifies each finding. It records no summary task, and the brief forbids inferring a case fact the file does not hold. Fix: "A fresh check's findings, which a maintainer verifies one by one before applying them (case file §2); a summary of them for the maintainer is this unit's example, not a task the case file records"; Basis: Academy case file §2.

[minor] [attribution] Sources (Anthropic); Current: "- Claude Help Center. *How much does the Max plan cost?* https://support.claude.com/en/articles/11049744-how-much-does-the-max-plan-cost"; Problem: the Sources list must include the Ultra article that the §6 fix adds. Fix: "- Claude Help Center. *How much does the Max plan cost?* https://support.claude.com/en/articles/11049744-how-much-does-the-max-plan-cost\n- Claude Help Center. *What is the Ultra plan?* https://support.claude.com/en/articles/17728952"; Basis: Part 1 (the unit lists every source it cites).

[minor] [accuracy] Appendix, plans note; Current: "Limits reset five hours after the first message of a session;"; Problem: the table directly above says Ultra (verified) has no five-hour limit. Fix: "Limits reset five hours after the first message of a session, except on Ultra for verified accounts;"; Basis: https://claude.com/pricing/max ; https://support.claude.com/en/articles/17728952

[minor] [accuracy] Appendix, plans note; Current: "A second copy of the pricing page, read the same day, showed Max at 5x or 20x and no Ultra (§6)."; Problem: this leaves the conflict open although Anthropic's Ultra article settles it. Fix: "A second copy of the pricing page, read the same day, showed Max at 5x or 20x and no Ultra; Anthropic's Ultra help article says Max 20x is now called Ultra (§6)."; Basis: https://support.claude.com/en/articles/17728952

[minor] [accuracy] §4, "Compute against size"; Current: "spending more inference compute on it outperformed a model 14 times larger"; Problem: it drops two qualifiers in the abstract: the comparison is FLOPs-matched, and the compute is allocated optimally. Fix: "spending inference compute on it optimally outperformed, in a FLOPs-matched comparison, a model 14 times larger"; Basis: https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html

[minor] [attribution] §4, "Large against larger"; Current: "OSWorld 2.1 (81.8% against 80.7%)"; Problem: the launch table names the test "OSWorld 2.1 (partial)". Fix: "OSWorld 2.1 (partial) (81.8% against 80.7%)"; Basis: https://anthropic.com/news/claude-opus-5-5

[minor] [accuracy] §2, Anthropic bullet; Current: "subagent work beside the larger models"; Problem: the Haiku 5.5 page says subagent work on coding tasks, alongside Opus 5.5 and Sonnet 5.5. Fix: "subagent work on coding tasks alongside Opus 5.5 and Sonnet 5.5"; Basis: https://anthropic.com/claude-haiku-5-5

[minor] [attribution] Deliverable Part 1, row 1; Current: "Sorting the proposed rows a chat adds to the backlog; putting a checker's findings into its three grades, error, should-fix and minor (case file §2)"; Problem: in the case file the checker itself writes its findings in those grades. A separate grading step is not recorded. Fix: "Sorting the proposed rows a chat adds to the backlog (case file §2); the case file records no separate triage step, so the instance is this unit's example"; Basis: Academy case file §2.

[minor] [style] Deliverable Part 1, row 7; Current: "The research report the first three marketing units were written from"; Problem: "marketing units" points into a private course that this reader cannot open and has not been introduced to. Fix: "The research report the first three units of one of the project's courses were written from"; Basis: brief; Part 6.

[minor] [deliverable] Deliverable Part 2, intro; Current: "leave a row blank until you have one past input for it"; Problem: §7 rule 4 needs three past inputs with a known good output to re-decide a row. Fix: "leave a row blank until you have three past inputs for it whose good output you know (§7, rule 4)"; Basis: unit §7.

[minor] [label] §4, benchmark reading; Current: "- **When.** In Academy's second audit (anecdote),"; Problem: the general point rests only on the Academy anecdote, and Part 6 forbids the case being the only support for a general claim. Fix: "- **When.** The index above changed version on 27 October 2026, so a leaderboard read before that day and one read after it rank models on different tasks. In Academy's second audit (anecdote),"; Basis: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 ; Part 6.

Every Current: string above occurs exactly once in unit.md (checked by script).

## Confirmed
- Models overview: all four prices, IDs, default efforts, always-on thinking for Fable 5.2 and Opus 5.5, 1M/128K, June 2026 cutoff, positioning, the "start with Opus 5.5 … Fable 5.2 when evals at higher effort fall short" advice, and the legacy prices (Fable 5.1, Opus 5, Sonnet 5). PASS (https://platform.claude.com/docs/en/models)
- Effort page: the quotation is exact. Levels, the xhigh and max descriptions, defaults, Opus 5.5 thinking that cannot be turned off, per-model guidance with the Haiku low-effort warning, the cache rule for top-level against per-message effort, and tool-call behaviour. PASS (https://platform.claude.com/docs/en/build-with-claude/effort)
- Steering thinking: the headline. Thinking is billed as output, in full when summarised; earlier thinking blocks are billed as input; lower the effort before steering by prompt. PASS (https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?r=0)
- Pricing docs: the Haiku 5.5 tiers and the over-100K rule, cache reads, one rate across the 1M window, Batch 50%, web search $10 per 1,000, the ~30% tokenizer note, US-only 1.1x, and fast-mode prices. PASS (read on the same page in the zh-CN locale: https://platform.claude.com/docs/zh-CN/about-claude/pricing)
- What's new in Fable 5.2: "Input and output cost less than on Claude Fable 5.1". PASS
- Artificial Analysis leaderboard: all eight rows plus Gemini 4 Carbon 60/$5.48 and Argon 50/$4.97 at high. No version is shown on the leaderboard. PASS
- Artificial Analysis model pages (Opus 5.5, Sonnet 5.5, Fable 5.2): every score, time, speed (104–114 tok/s), v5.0.1, cost given only at max, and Fable low at 54. Headlines match the Sources titles. PASS
- Artificial Analysis methodology (cost-per-task definition and price basis) and the v5 announcement (27 Oct; dropped and added tests; 60% private or held-out). PASS
- All arithmetic: 7.9x, 2.6x, the effort steps, about two tasks for $20. PASS
- Opus 5.5 launch: the date, nine tests with all scores quoted, effort settings, safeguard fallbacks, Zapier, CursorBench 57.8/52.5, the two "fifth of the cost" claims, "performs at the level of Claude Fable 5.1 on most work", and the narrower gap. PASS
- Haiku 5.5 launch: the date, 1620/1840, 39.2/70.6, 57.4/64.5, Sonnet effort stated only for FrontierCode (xhigh), and the "remain better choices" statement. PASS
- Hallie post: author, role, 7 Jul 2026, the quotation, the diagnostic, the heuristic framing, the default-effort advice, and the cost-per-task and "cannot at any effort" claims. PASS
- Help centre articles on model/effort/thinking settings, usage limits, usage best practices, Fable on your plan, usage credits, and Max cost: every claim as stated. PASS
- Plans page: Pro $20/$17 ($200 up front), Max $100 5x, Ultra $200 10x weekly with no five-hour limit for verified accounts, Fable rules, Team and Enterprise seat prices. PASS (read at https://claude.com/pricing/max; the unit's claude.com/max URL was not returned by search)
- OpenAI reasoning guide: reasoning tokens billed as output and counted in the window; levels none to max; Sol defaults to medium and supports neither none nor minimal; medium vs high first; "tuning knob"; output contract; gpt-5.6-terra/luna. PASS. OpenAI pricing: four prices; Flex/Batch is half, not stated in words. PASS
- Google pricing (3.8 Flash dated change, Flash-Lite, "including thinking tokens", Batch 50%, Argon not listed), Gemini thinking (14 Oct; billing; Argon levels, default, cannot disable), and Gemini 4 Argon page (30 Oct; flagship; 1,048,576; no price). PASS
- FrugalGPT (incl. TMLR 2024), RouteLLM (ICLR abstract; GPT-4 and Mixtral, MMLU/MT Bench/GSM8K in arXiv v3), Chen et al. (ICML, PMLR 267, 9487–9499), Zheng et al., Panickssery et al., and Huang et al. (models and tasks). PASS. Huang's ICLR venue is not shown on the arXiv page read.
- Academy case file §1–§5, §7, §9 and the §7 note. Every count was recomputed from the §5 table: 19/15, 12/8, 5/5; 28 of 36; 58/237/303. PASS
- Could not verify: "earlier Opus models defaulted to high" (the page gave Opus 5 only); OpenAI's "start with its largest" (not found in the parts of the guide read); Enterprise Fable "included, per the pricing page".

## (3)–(4) Figures with owners and labels
Every number names whose figure it is, and the labels for vendor, third party, anecdote and the unit's own inference are present. The exceptions are the §5 same-model inference and §4 "When".

## (5) Deliverable
Present in full and follows from §1–§7. It can be used on its own. Fixes are needed in rows 1, 3 and 7 and in the template's input count.

## (6) Pointers
The BW1 pointers (§1, §2, §4, §5, §9) are used consistently, but BW1 is not in the packet, so its content was not confirmed. BW5, BW6, BW7 and BW10 are forward pointers and claim nothing beyond what those units will do.

## (7) Figures
1. compare (§1): PASS.
2. scatter (§3): PASS.
3. bars, grouped (§5): FIX. The caption needs the replacement in the bars-caption finding above.
4. decision (§7): FIX. The kind fits, but two labels are not in the text. Add the rule 4 sentence from the error finding; the JSON then needs no change.

## (8) Writer's Source errors
1. B2's 40% claim drops "on typical workloads at default settings": confirmed (https://anthropic.com/news/claude-opus-5-5).
2. B2 missed the illustrative labelling of the token IDs: confirmed. The "roughly 7x" caption is not labelled illustrative (https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code).

Unsure list: item 1 is resolved, because the Ultra article was readable in this check. Items 2–10 are consistent with the pages read; on item 9, the post as read says "routine".

## (9) Part 6
Passes every line except: one private-course phrase ("marketing units", row 7); the case as the only support in §4 "When"; and two instance cells that go beyond the case file (rows 1 and 3).

## (10) Reader persona
An outside professional can follow the unit. Internal vocabulary appears in rows 1 and 7 ("rows a chat adds to the backlog", "marketing units"). The only private term is "marketing units". No personal details appear.

## (11) Attribution
Sources titles match the page headlines of every page read. The three quotations are exact. Every figure matches its page except the OSWorld test name (minor).

BW2 · fix · 1 error, 5 should-fix, 10 minor · figures 2 PASS / 2 FIX · source errors 2 confirmed / 0 not confirmed
