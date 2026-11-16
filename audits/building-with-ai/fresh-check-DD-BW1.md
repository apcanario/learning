---
audit: fresh check
unit: DD-BW1 · Deep dive: how the best practitioners work
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgR36FFxqBvGbNsHzyhJ
verdict: fix · 3 errors, 20 should-fix, 12 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: DD-BW1 · fix · 3 error, 20 should-fix, 12 minor

claude-opus-5-5. The harness refused the write to out/findings.md ("Subagents should return findings as text"), so the full report follows verbatim.

# Fresh check · DD-BW1 · Deep dive: how the best practitioners work

Checker: Opus 5.5 (claude-opus-5-5), isolated agent context, 16 Nov 2026. Packet only; live search; WebFetch only on addresses a search in this agent returned.

## Findings

[error] [figure] §1.6 figure 2 (compare); Current: ""rows": [{"label": "#1 baseline, 29 Jan", "value": 3.04, "tone": 4}, {"label": "#2, 2 Feb", "value": 2.91, "tone": 4}, {"label": "#3, 5 Feb", "value": 2.76, "tone": 4}, {"label": "#4 dataset change, 4 Mar""; Problem: entries #1 to #3 (3.04, 2.91, 2.76 h; 29 Jan, 2 Feb, 5 Feb) are not in the unit's text, which gives only entries 4, 5 and 6; the figure adds facts. (The values are right on the README.); Fix: ""rows": [{"label": "#4 dataset change, 4 Mar""; Basis: unit §1.6 text ("entry 4 (4 March 2026, a change of dataset) at 2.02 hours, entry 5 (9 March) at 1.80 hours ... entry 6 (14 March) at 1.65 hours"); https://github.com/karpathy/nanochat
[minor] [figure] §1.6 figure 2 caption; Current: ""caption": "Hours for a nanochat run to beat GPT-2's score, by leaderboard entry, 2026 (§1.6)."; Problem: once rows 1 to 3 go, the caption should say which entries it shows; Fix: ""caption": "Hours for a nanochat run to beat GPT-2's score, leaderboard entries 4 to 6, 4 to 14 March 2026 (§1.6)."; Basis: https://github.com/karpathy/nanochat
[error] [figure] §1.4 figure 1 (bars); Current: "he went from about 80% manual coding and 20% agents in November to about 80% agent coding in December"; Problem: the figure's labels "November 2025" and "December 2025" and its December "Manual" value of 20 are not in the text (no year, no December 20%). The thread gives the December remainder as "20% edits+touchups" and November's manual share as "manual+autocomplete"; Fix: "he went from about 80% manual coding (with autocomplete) and 20% agents in November 2025 to about 80% agent coding and 20% edits and touch-ups in December 2025"; Basis: https://threadreaderapp.com/thread/2015883857489522876.html (thread dated "Jan 26"; status 2015883857489522876 decodes to 26 Jan 2026)
[error] [figure] §3.5 (matrix figure §4, row "Jagged frontier experiment", cell "BW7 §4"); Current: "Grade: measured; GPT-4 in 2023, consulting tasks. Transfer: the mechanism"; Problem: the matrix says BW7 §4 teaches the jagged-frontier experiment; nothing in the unit's text says so (BW7 §4 appears only as "BW7 §4's options stage"). Also missing here: who the study was written for (brief: "who it was written for" for every method); Fix: "Grade: measured; GPT-4 in 2023, consulting tasks; BW7 §4 already cites it. Written for: researchers and managers of knowledge work. Transfer: the mechanism"; Basis: unit line of the matrix row; notes.md Contradictions 1 (BW7's table row "Dell'Acqua et al., HBS working paper, 2023"); https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
[should-fix] [accuracy] §1.2; Current: "From his keynote at Y Combinator's AI Startup School, San Francisco, 17 June 2025, as a third-party automatic transcription prints it"; Problem: the cited transcription gives no date or venue; the date 17 June is unsourced. Y Combinator's own page gives the event as 16-17 June in San Francisco; the day of his talk was not found; Fix: "From his keynote at Y Combinator's AI Startup School, San Francisco, 16–17 June 2025 ([Y Combinator, *Join us at AI Startup School — June 16-17*](https://www.ycombinator.com/blog/ai-startupschool), read 16 Nov 2026; the day of his talk was not found), as a third-party automatic transcription prints it"; Basis: https://www.ycombinator.com/blog/ai-startupschool; https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html
[minor] [accuracy] Deliverable card K2; Current: "YC AI Startup School keynote, 17 Jun 2025, via"; Problem: same unsourced day; Fix: "YC AI Startup School keynote, 16–17 Jun 2025, via"; Basis: https://www.ycombinator.com/blog/ai-startupschool
[minor] [attribution] Sources; Current: "(third-party automatic transcription of the keynote of 17 June 2025)"; Problem: same unsourced day; the event page is not listed; Fix: "(third-party automatic transcription of the keynote at AI Startup School, San Francisco, 16–17 June 2025; dates from Y Combinator, *Join us at AI Startup School — June 16-17*, https://www.ycombinator.com/blog/ai-startupschool)"; Basis: https://www.ycombinator.com/blog/ai-startupschool
[should-fix] [accuracy] Interests (opening); Current: "Karpathy joined Anthropic's pre-training team on 19 May 2026, to lead a new group using Claude to speed up pre-training research"; Problem: TechCrunch, dated 19 May 2026, says he "started this week" and "will start a team focused on using Claude to accelerate pre-training research"; 19 May is the article's date, not a stated start date; Fix: "Karpathy started at Anthropic, on its pre-training team, in the week of 19 May 2026, and is to start a team using Claude to accelerate pre-training research"; Basis: https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/
[minor] [accuracy] Interests; Current: "Every Karpathy source below predates the move."; Problem: the nanochat README (its disclosure policy and leaderboard) was read in its current form on 16 Nov 2026; the policy's date is not shown, so it cannot be said to predate May 2026; Fix: "Every Karpathy source below predates the move, except possibly the nanochat README, read in its current form (its policy carries no date)."; Basis: https://github.com/karpathy/nanochat
[should-fix] [attribution] §2.1; Current: "[*Building effective AI agents*, Anthropic Engineering, 19 Dec 2024]"; Problem: the page's headline as shown (H1) is "Building effective agents"; "Building effective AI agents" is only its HTML title and og:title. notes.md Contradictions 2 rests on the tab title; Fix: "[*Building effective agents*, Anthropic Engineering, 19 Dec 2024]"; Basis: https://anthropic.com/engineering/building-effective-agents
[should-fix] [attribution] Sources; Current: "Erik S. and Zhang, B. *Building effective AI agents*."; Problem: as above; Fix: "Erik S. and Zhang, B. *Building effective agents*."; Basis: https://anthropic.com/engineering/building-effective-agents
[should-fix] [accuracy] §3.4; Current: "Willison now opens each agent-written pull request with a short paragraph he chose himself, which carries"; Problem: Willison says "I don't always write the introduction myself—sometimes the agent has given me what I need already"; the paragraph is "carefully selected", not always his own words; Fix: "Willison now opens each agent-written pull request with a short paragraph he selects himself (sometimes words the agent gave him), which carries"; Basis: https://simonwillison.net/2026/nov/9/details-summary
[minor] [accuracy] §3.4; Current: "whose summary line names the model and effort, so a reader sees at once which part a person wrote"; Problem: he writes "I use the model name and often the effort level"; and since the opener may be agent-written, the person's part is the one he vouches for, not always the one he wrote; Fix: "whose summary line names the model and often the effort level, so a reader sees at once which part a person vouches for"; Basis: https://simonwillison.net/2026/nov/9/details-summary
[minor] [deliverable] Part 2 rule 4; Current: "the part you wrote comes first, and model-written text is marked with the model"; Problem: W4 supports a part you select and vouch for coming first, not one you wrote; Fix: "the part you chose and vouch for comes first, and model-written text is marked with the model"; Basis: https://simonwillison.net/2026/nov/9/details-summary
[should-fix] [deliverable] Part 2 rule 6, Academy cell; Current: "The case is agent-heavy by design; with no control"; Problem: "agent-heavy by design" is not in the case file; the brief forbids inferring a case fact. The file does record that writer, checker, applier and filer were each a fresh agent (§2); Fix: "Writer, fresh checker, applier and filer are each a fresh agent (§2); with no control"; Basis: case-academy.md §2 ("From BW7 of this course ... writer, checker, applier, filer and corrections checker were each a fresh agent")
[should-fix] [figure] §4 matrix caption; Current: "Grades and transfers from the sections cited in each row; units by code."; Problem: the rows cite no sections; the caption must name where the data comes from; Fix: "Grades, transfers and core units from §1 to §4 of this unit; units by code."; Basis: unit §4 figure
[should-fix] [style] §3.4 heading; Current: "### 3.4 · New since 29 October 2026: label what the model wrote (Willison, 9 November)"; Problem: 29 October 2026 is the date of the private source unit; a reader of this course cannot know why that date matters; Fix: "### 3.4 · New in November 2026: label what the model wrote (Willison, 9 November)"; Basis: brief ("never refer to the private course or its units")
[should-fix] [style] §3.5; Current: "**New since 29 October 2026: the model does not judge its own work (Mollick, 9 November).**"; Problem: same; Fix: "**New in November 2026: the model does not judge its own work (Mollick, 9 November).**"; Basis: brief
[should-fix] [coverage] §1.3; Current: "Grade: stated opinion. Transfer: complete. BW1 and BW4 are built on the idea"; Problem: the brief asks for who each method was written for; §1.3 does not say; Fix: "Grade: stated opinion. Written for: people building LLM applications (his "industrial-strength LLM app"). Transfer: complete. BW1 and BW4 are built on the idea"; Basis: https://simonwillison.net/2025/Jun/27/context-engineering/
[should-fix] [coverage] §1.5; Current: "His subject is what models can be trained to do. Grade: stated opinion, built on an argument about training."; Problem: no "Written for"; Fix: "His subject is what models can be trained to do. Written for: anyone asking which tasks and jobs AI will automate first (his "task/job"). Grade: stated opinion, built on an argument about training."; Basis: https://simonwillison.net/2025/Nov/16/andrej-karpathy/
[should-fix] [coverage] §1.6 disclosure; Current: "Grade: documented practice (a policy in force on a public repository). Transfer: whole"; Problem: no "Written for"; Fix: "Grade: documented practice (a policy in force on a public repository). Written for: contributors to the repository. Transfer: whole"; Basis: https://github.com/karpathy/nanochat
[should-fix] [coverage] §2.2; Current: "The page reports no benchmark. Grade: documented practice, vendor."; Problem: no "Written for"; Fix: "The page reports no benchmark. Written for: developers building agents. Grade: documented practice, vendor."; Basis: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
[should-fix] [coverage] §2.5; Current: "Grade: vendor data, internal benchmark, method not published. Transfer:"; Problem: no "Written for"; Fix: "Grade: vendor data, internal benchmark, method not published. Written for: developers prompting GPT-4.1. Transfer:"; Basis: https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide
[should-fix] [coverage] §3.2; Current: "Grade: documented practice. Transfer: context (BW4)"; Problem: no "Written for"; Fix: "Grade: documented practice. Written for: programmers. Transfer: context (BW4)"; Basis: https://simonwillison.net/2025/Mar/11/using-llms-for-code/
[should-fix] [coverage] §3.3; Current: "Transfer: whole, to any chat with connectors. BW9 box 1 is this test."; Problem: no "Written for"; the post addresses "end users ... mixing tools"; Fix: "Written for: users and builders of agents that mix tools. Transfer: whole, to any chat with connectors. BW9 box 1 is this test."; Basis: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
[should-fix] [coverage] §3.4; Current: "Grade: documented practice, one practitioner, days old. Transfer: whole."; Problem: no "Written for"; Fix: "Grade: documented practice, one practitioner, days old. Written for: programmers who open pull requests. Transfer: whole."; Basis: https://simonwillison.net/2026/nov/9/details-summary
[should-fix] [coverage] §3.5 Mollick; Current: "Grade: stated opinion, on his own projects; anecdote, one person. Transfer: whole."; Problem: no "Written for"; Fix: "Grade: stated opinion, on his own projects; anecdote, one person. Written for: his newsletter's general readers. Transfer: whole."; Basis: https://www.oneusefulthing.org/p/fable-52-and-jagged-agi
[should-fix] [coverage] §3.6; Current: "Grades: documented practice (Reed an anecdote; Spec Kit and Kiro vendor tools)."; Problem: no "Written for"; Fix: "Grades: documented practice (Reed an anecdote; Spec Kit and Kiro vendor tools). Written for: programmers."; Basis: https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/; https://kiro.dev/blog/introducing-kiro/
[should-fix] [coverage] §3.7; Current: "What survives for knowledge work (this unit's inference)."; Problem: no "Written for" for the four papers; Fix: "Written for: machine-learning researchers. What survives for knowledge work (this unit's inference)."; Basis: https://arxiv.org/pdf/2201.11903; https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html
[minor] [style] §1.7; Current: "This course's running example, the Academy case (Academy case), runs it this way"; Problem: the first-use label doubles the name; Fix: "This course's running example, Academy (Academy case), runs it this way"; Basis: brief ("Label the case '(Academy case)' on its first use")
[minor] [accuracy] Deliverable card K3; Current: "X post, 25 Jun 2025, via Willison, 27 Jun 2025 (§1.3)"; Problem: the day 25 June is not in the body or on Willison's page, which gives no date for Karpathy's post; Fix: "X post, June 2025, via Willison, 27 Jun 2025 (§1.3)"; Basis: https://simonwillison.net/2025/Jun/27/context-engineering/
[minor] [attribution] Sources; Current: "- Thread Reader App, reproduction of Andrej Karpathy's X thread of 26 January 2026."; Problem: the page's headline is "Thread by @karpathy on Thread Reader App" (unsure item 2); Fix: "- Thread Reader App. *Thread by @karpathy on Thread Reader App* (reproduction of Andrej Karpathy's X thread of 26 January 2026)."; Basis: https://threadreaderapp.com/thread/2015883857489522876.html
[minor] [label] §2.3; Current: "on current Claude models effort is the lever, set in the model menu (BW2 §3)"; Problem: a product fact without the date it was read (Part 6); §6 dates the same fact; Fix: "on current Claude models effort is the lever, set in the model menu (BW2 §3, read 15 Nov 2026)"; Basis: unit §6 ("Effort, set in the model menu (BW2 §3, read 15 Nov 2026)")
[minor] [label] §3.7; Current: "effort sets how much of it there is (BW2 §3)"; Problem: as above; Fix: "effort sets how much of it there is (BW2 §3, read 15 Nov 2026)"; Basis: unit §6
[minor] [accuracy] §3.5 Autor et al.; Current: "randomised 133 patent lawyers to a custom drafting assistant or none for three months"; Problem: the abstract describes a pre-registered RCT of 133 lawyers with treated and control groups; it does not say the controls had no assistant at all; Fix: "randomised 133 patent lawyers between access to a custom drafting assistant and a control group, for three months"; Basis: https://nber.org/papers/w35720

## Confirmed

- TechCrunch headline, byline (Rebecca Bellan and Lorenzo Franceschi-Bicchierai) and date 19 May 2026; pre-training team; team using Claude for pre-training research — https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/
- Willison, 19 Mar 2025, title exact; Karpathy's tweet reproduced in full ("Andrej's original tweet in full"); "vibe coding", "forget that the code even exists"; Willison dates it "February 6th"; definition "building software with an LLM without reviewing the code it writes"; "not the same thing as writing code with the help of LLMs"; "if I couldn't explain exactly what it does to somebody else"; "Think about how much harm the code you are writing could cause" (sentence continues "if it has bugs or security vulnerabilities") — https://simonwillison.net/2025/Mar/19/vibe-coding/
- Vibe coding MenuGen, 27 Apr 2025: "100% of the code was written by Cursor+Claude"; "kept hallucinating deprecated APIs, model names, and input/output conventions"; "kind of messy and not a good idea for anything of actual importance" — https://karpathy.bearblog.dev/vibe-coding-menugen/
- yt-transcribe page title exact; "you are in charge of the autonomy slider"; generation/verification; "make this loop go as fast as possible"; "keep the AI on the leash"; "I always go in small incremental chunks"; "kind of like working memory"; GUI helps humans audit faster — https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html
- AI Startup School, San Francisco, 16–17 June 2025 — https://www.ycombinator.com/blog/ai-startupschool
- Context engineering, 27 Jun 2025: "+1 for "context engineering" over "prompt engineering""; "delicate art and science of filling the context window"; list of task descriptions, few-shot, RAG, related data, tools, state and history, compacting; Lütke "describes the core skill better" — https://simonwillison.net/2025/Jun/27/context-engineering/
- Dwarkesh, 17 Oct 2025, title exact; "my sweet spot"; "fairly unique repository"; "too much memory from all the typical ways of doing things"; "way too over-defensive"; "It's just not net useful."; "the decade of agents"; boilerplate; tokenizer rewritten in Rust from his Python with tests — https://dwarkesh.com/p/andrej-karpathy
- Thread of 26 Jan (2026 by status-ID decode): 80/20 November, 80% agents December; "biggest change to my basic coding workflow" in ~2 decades; "watch them like a hawk"; wrong assumptions; "don't seek clarifications, they don't surface inconsistencies"; "still a little too sycophantic"; "bloat abstractions"; dead code; 1000 lines to "100 lines"; "Don't tell it what to do, give it success criteria and watch it go."; "imperative to declarative"; generation and discrimination; "atrophy" — https://threadreaderapp.com/thread/2015883857489522876.html
- Verifiability, Willison 16 Nov 2025, post on X: "the new most predictive feature to look at is verifiability"; resettable / efficient / rewardable parentheticals verbatim — https://simonwillison.net/2025/Nov/16/andrej-karpathy/ (search also returned the feeds. address the unit cites)
- nanochat: "Current AI policy: disclosure"; "declare any parts that had substantial LLM contribution"; leaderboard #4 2.02 h (4 Mar 2026, ClimbMix dataset), #5 1.80 h "autoresearch round 1" (9 Mar), #6 1.65 h "autoresearch round 2" (14 Mar); 8XH100 node; 11% and 18% (checked: 10.9%, 18.3%) — https://github.com/karpathy/nanochat
- autoresearch: "trains for 5 minutes, checks if the result improved, keeps or discards, and repeats"; "the single file the agent edits" (train.py); prepare.py holds data preparation and evaluation; "This keeps the scope manageable and diffs reviewable."; ~12 experiments/hour, "approx 100 experiments while you sleep"; not comparable across platforms; "essentially a super lightweight "skill""; 36 commits — https://github.com/karpathy/autoresearch
- llm-wiki gist, created 4 Apr 2026; immutable sources; "The LLM owns this layer entirely"; "(e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex)"; "10-15 wiki pages"; lint wording; index "a catalog of everything in the wiki"; log "an append-only record of what happened and when"; ~100 sources, "avoids the need for embedding-based RAG infrastructure"; "rediscovering knowledge from scratch on every question"; "You never (or rarely) write the wiki yourself" — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Building effective agents: byline "Erik S. and Barry Zhang", 19 Dec 2024; all four quotations; five workflow patterns — https://anthropic.com/engineering/building-effective-agents
- Effective context engineering: authors Rajasekaran, Dixon, Ryan, Hadfield (Applied AI team), 29 Sep 2025; all quotations; no benchmark — https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI practical guide: no date; all quotations verbatim — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- GPT-4.1 Prompting Guide: MacCallum and Lee, 14 Apr 2025, archived; "more literally than its predecessors"; "close to 20%"; "by 4%"; "both the beginning and end" — https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide
- What is agentic engineering?: definition and "unreviewed, prototype-quality LLM-generated code"; updated metadata 15 Mar 2026 — https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering
- Anti-patterns: one named anti-pattern; "Don't file pull requests with code you haven't reviewed yourself"; "rude to expect someone else to read text that you haven't read" (continues "and validated yourself") — https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns
- Willison, 6 May 2026, title exact; "the thing where you're not looking at the code at all"; no longer reviewing every line — https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering
- Willison, 11 Mar 2025: managing context; cut-offs; options; "digital intern"; testing cannot be outsourced — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- Lethal trifecta, 16 Jun 2025, title exact; three legs verbatim; "avoid that lethal trifecta combination entirely"; "95% is very much a failing grade" — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Willison, 9 Nov 2026, title exact; "my human judgement as to what is definitely worth their time"; <details> with model name in summary — https://simonwillison.net/2026/nov/9/details-summary
- Mollick, 9 Nov 2026, title exact; Claude Fable 5.2, Anthropic; "my feedback along the way turned out to matter a lot"; peer reviewer (GPT-6 Pro) "twice found issues"; "the AI did not notice these problems itself"; critics did not ask about length or repetition; "the part Fable does least reliably" — https://www.oneusefulthing.org/p/fable-52-and-jagged-agi
- Dell'Acqua et al., WP 24-013, 22 Sep 2023; nine authors (Dell'Acqua, Mollick and seven others); pre-registered; 758 consultants; 12.2%, 25.1%, more than 40%; "19 percentage points less likely to produce correct solutions" — https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
- Organization Science version: abstract "19% less likely"; volume and date not shown; DOI 10.1287/orsc.2025.21838 — https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838?af=R
- Autor et al., NBER w35720, Sep 2026, rev. Oct 2026; seven authors; conducted by Google; pre-registered; 133 patent lawyers; custom assistant; 0.34 SD (10 days), 0.38 (90 days); 0.32 later without AI, 0.45 seniors, juniors no average gain — https://nber.org/papers/w35720
- Reed, 16 Feb 2025: three steps, spec.md; "small, iterative chunks that build on each other"; "The success really depends on how well step 2 went." — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
- Spec Kit: Den Delimarsky, 2 Sep 2025, title exact; "the specification becomes the source of truth"; "small, reviewable chunks" — https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit
- Kiro: Nikhil Swaminathan and Deepak Singh, 14 Jul 2025; EARS acceptance criteria, design, tasks sequenced by dependencies and linked to requirements — https://kiro.dev/blog/introducing-kiro/
- Wei et al., NeurIPS 2022, arXiv 2201.11903v6; "a range of arithmetic, commonsense, and symbolic reasoning tasks" — https://arxiv.org/pdf/2201.11903
- Sprague et al., ICLR 2025, title exact; "over 100 papers"; "20 datasets across 14 models"; "primarily on tasks involving math or logic"; equals-sign sentence — https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html
- ReAct: hallucination and error propagation; "absolute success rate of 34% and 10% respectively"; ICLR camera-ready — https://arxiv.org/abs/2210.03629
- Self-consistency: GSM8K +17.9%, SVAMP +11.0%, AQuA +12.2%; ICLR 2023 — https://arxiv.org/abs/2203.11171
- Create custom subagents: "starts with a fresh, isolated context window"; fork "inherits the parent conversation"; fork mode "on by default" in local sessions; `CLAUDE_CODE_FORK_SUBAGENT` set to `0` — https://code.claude.com/docs/en/sub-agents
- OpenAI Reasoning models: "`reasoning.effort` parameter guides the model on how much to think"; values vary by model — https://developers.openai.com/docs/guides/reasoning
- GEMINI.md page, headline exact; "define them once in a context file"; `context.fileName` can include AGENTS.md — https://geminicli.com/docs/cli/gemini-md/
- Gemini CLI subagents: Jack Wotherspoon and Abhi Patel, 15 Apr 2026; "Each subagent operates within its own separate context window" — https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/
- Case facts in Part 2 (rules 1–5, 7–10) and the Deliverable intro match case-academy.md §1, §2, §5, §6, §9 (28 of 36 drafts with an error; checkers Fable 5.1, Opus 5.5, Fable 5.2; index check restores files; figures fixed until they pass).

Unverifiable (not FAIL):
- §2.3 / card A3, Cherny, *Claude Code: Best practices for agentic coding*, https://www.anthropic.com/research/claude-code-best-practices: no search in this agent returned that address (a second search was refused by the harness); the /engineering/claude-code-best-practices address a search returned lands on the current docs page "Best practices for Claude Code", with no author and none of the quoted lines. All §2.3 quotations, the 18 April 2025 date, the byline and the "no longer maintained" note are unverified here.
- §6 Gemini cell, *Gemini thinking*, https://ai.google.dev/gemini-api/docs/generate-content/thinking: the fetch redirected (302 to aistudio.google.com) and was not followed; "dynamic thinking by default" and `thinkingLevel` not checked.
- Vibe-coding X status decoding to 2 February 2025: the unit does not print the status number, so the arithmetic cannot be repeated from the unit.

## (1) Coverage

- Every method of the source unit, rebuilt from primary sources: covered (as far as the unit and notes show; the source unit was not in the packet).
- Practices a secondary source attributes without the author's own words discarded: covered (K10, K11, M1 named and not used).
- New methods with a named author and primary source since 29 Oct 2026: covered (Willison 9 Nov; Mollick 9 Nov), plus Autor et al.
- For every method, what it claims: covered.
- What evidence it rests on: covered.
- Who it was written for: thin. Given for §1.1, §1.2, §1.4 (January), §1.6 autoresearch, §1.7, §2.1, §2.3, §2.4, §3.1; missing for §1.3, §1.5, §1.6 disclosure, §2.2, §2.5, §3.2–§3.7 (findings above).
- Grade: covered.
- Transfer decided case by case, software-only methods left there: covered (autoresearch, EARS, keyword ladder).
- Which methods the ten core units already teach, by code: covered (§4 matrix and paragraph; §5 against BW9).
- Deliverable: method cards (author, primary source with date, claim, grade, transfers / does not): covered. Ten operating rules, each traced to a card: covered.
- Preamble items: "On other tools" section: covered. Case labelled "(Academy case)" on first use: covered (awkward doubling, minor). Deliverable built twice (case, then template): covered. Product facts dated: mostly; two undated pointers (minor).

## (5) Deliverable

Present in full: 29 method cards (K1–K11, A1–A3, O1–O2, W1–W4, M1–M3, S1–S3, P1–P3), a ten-rule table with cards, grade, a record column and an Academy column, and two templates (a blank card and the rules table with blanks that say what goes in them). It follows from the evidence: each rule cites cards whose sections hold the support, the grades are no stronger than those cards (only rule 10 claims measurement, with the 2022–2024 caveat). Rule 4's "the part you wrote" stretches W4 (minor finding). Rule 6's case cell infers a case fact (should-fix). Usable alone: yes. The template's columns point to the reader's BW2, BW4, BW5, BW6 and BW9 outputs, which a reader of the course has.

## (7) Figures

1. Figure 1, kind bars (grouped), §1.4. Labels "Manual", "Agents": text "80% manual coding and 20% agents". "November 2025", "December 2025": the text has "November" and "December" but no year. Values 80/20 November: text "about 80% manual coding and 20% agents in November". 80 agents December: "about 80% agent coding in December". 20 manual December: not in text. Caption: says what it shows, names §1.4 and the source (thread via Thread Reader App), labels it a self-report. Kind fits (two numbers compared over two periods). FIX: the text change in the §1.4 finding (years and the December 20%). With it applied the JSON stands as is.
2. Figure 2, kind compare, §1.6. Rows #4, #5, #6 traced: "entry 4 (4 March 2026, a change of dataset) at 2.02 hours, entry 5 (9 March) at 1.80 hours labelled "autoresearch round 1", entry 6 (14 March) at 1.65 hours, "autoresearch round 2"". Rows #1 "baseline, 29 Jan" 3.04, #2 "2 Feb" 2.91, #3 "5 Feb" 2.76: not in the text, so error. Caption names §1.6 and the README source. Kind fits (numbers compared; a line would also fit). FIX, replacement JSON:
```viz
{"kind": "compare", "unit": " h", "max": 2.5, "decimals": 2, "rows": [{"label": "#4 dataset change, 4 Mar", "value": 2.02, "tone": 4}, {"label": "#5 autoresearch round 1, 9 Mar", "value": 1.8, "tone": 2}, {"label": "#6 autoresearch round 2, 14 Mar", "value": 1.65, "tone": 2}], "caption": "Hours for a nanochat run to beat GPT-2's score, leaderboard entries 4 to 6, 4 to 14 March 2026 (§1.6). From the leaderboard in the README of karpathy/nanochat, read 16 Nov 2026: one project, one metric, his own record."}
```
(The two findings above apply this as exact replacements; max is left at 3.5 there, and 2.5 is optional.)
3. Figure 3, kind matrix, §4. Rows and grades traced to §1–§3 ("Grade: ..." lines); transfers traced to each "Transfer:" line ("throwaway only" §1.1; "scripts only" §1.6; "with a change" §1.7; "literalness" §2.5; "mechanism" §3.5; "pattern" §3.6; "self-consistency" §3.7; "most" summarises §2.3). Core units traced: BW9 §3 (§1.1), BW9 §2 (§1.2), BW4 (§1.3), "BW9 §6, part" (§4 paragraph), "BW6, BW9 §2" (§1.5), "none" ×4 (§4 paragraph), "BW4, part" (§4), "BW7 §1, BW9" (§2.1), "BW1, BW3, BW4" (§2.2), "BW6, BW9" (§2.3), "BW9 §7" (§2.4), "BW3" (§2.5), "BW4, BW6" (§3.2), "BW9 §8" (§3.3), "BW2 §5, BW6" (§3.5 "BW2 §5"; BW6 §4 as the unit's separate-checker unit, §1.4 and §2.3), "BW5" (§3.6), "BW6 §4, part" (§3.7, §4). "BW7 §4" for the jagged-frontier row: not in the text, so error (fixed by the §3.5 finding). Caption: "from the sections cited in each row" is wrong, because no row cites a section (should-fix, replacement caption in the findings). Kind fits (items by attributes). FIX: text finding §3.5 and caption finding.

## (8) Writer's source errors (notes.md)

1. Sprague et al. is published in ICLR 2025, not only a preprint: confirmed. The ICLR proceedings page lists it under International Conference on Learning Representations 2025 with the same title and authors. https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html
2. *Effective context engineering* names its authors (Rajasekaran, Dixon, Ryan, Hadfield, Applied AI team): confirmed on the page (with contributors Ayub, Moran, Rueb, Jennings). https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
3. The April 2025 post opens at /research/claude-code-best-practices with "Written by Boris Cherny", 18 April 2025, no longer maintained: not confirmed (unverifiable). No search in this agent returned that address, so it was not fetched. The /engineering/ address a search did return lands on the current docs page, with no author named.

Source errors: 2 confirmed, 1 not confirmed.

## (9) Sourcing standard

Part 1, per claim:
- Sourced where made: yes, except the YC day (§1.2) and K3's 25 June (findings).
- Source openable with author, title, locator, date: yes. Undated items (OpenAI PDF, Willison guides, READMEs) are marked as such.
- Source says what the claim says: yes, with these exceptions: TechCrunch "joined on 19 May" (stretch); Willison 9 Nov "he chose himself" and "which part a person wrote" (stretch); rule 4 (minor); Autor "or none" (minor).
- Reporter kept separate from claim: yes. Willison, Thread Reader and yt-transcribe are named as reproductions.
- Number says whose figure: yes throughout (his figures, vendor internal, study).
- View attached to a named person only when argued: yes (M1 and K10 withheld).
- Quotation marks exact: yes on every quotation checked. Truncated sentences keep exact words (Willison "harm", "rude"). The §2.3 quotations are unverified.
- Nothing invented: nothing found invented.
- Figures add no fact: no. Figure 1 (year, December 20), figure 2 (rows 1–3) and figure 3 (BW7 §4) add facts (errors).
- Illustrations: none.

Part 1, per unit:
- Unsourced claims said or left out: yes (§1.8, M1, `program.md`).
- Search on, changeable facts dated: yes, all reads dated 16 Nov 2026. Two Claude effort facts point to BW2 without a date (minor).
- Sources list complete, nothing uncited listed: yes. The YC event page should be added if the §1.2 fix is applied.
- Closing material agrees with the body: yes, except rule 4 (minor) and the rule 6 case cell.

Part 6:
- Number, mechanism or recommendation sourced: yes.
- Source types labelled: preprint: Autor "not peer-reviewed", NBER WP; Dell'Acqua WP plus journal: yes. Vendor labelled and dated: yes. Practice labelled: yes.
- Evidence grade per method: yes.
- Study names its models and task; transfer called inference: yes (§3.5, §3.7, §6 closing line).
- Product facts dated on the vendor page: mostly. §2.3 and §3.7 effort lines are undated (minor). §6 cells dated by the section's lead line.
- "On other tools" section: present, with vendor docs cited or "not checked". The Gemini thinking page was not reachable for this checker (redirect).
- Claims carried from the private source re-verified: as far as visible, yes (each read 16 Nov 2026).
- No private-course reader detail, no reference to the private course: none found by reading. "29 October 2026" ×2 is the source unit's date, opaque to this reader (should-fix). `kit/private_terms.py` not run (outside the packet).
- Academy facts from the case file, cited, labelled, anecdote, never sole support: yes, except rule 6's "agent-heavy by design" (not in the file).
- No uncited figures or invented items: yes.
- Deliverable on the case, then template: yes.
- Not advice without evidence: passes.
- Links as links: yes.

## (10) Read as the brief's persona

- "New since 29 October 2026" (§3.4, §3.5) assumes the reader knows why that date matters. It is the private source unit's date. Fixes above.
- "Academy case file §1, §2 …" and "(case file §9)": the reader cannot open the case file. The brief requires this citation form, so no finding.
- "Fable 5.2" (§3.5): readable, since Mollick's title and "Anthropic's" identify it.
- BW codes and section numbers assume the core units, which the brief allows ("reads in order").
- Nothing else assumes private knowledge. No name, city, health detail or personal tool of the private reader appears.

Verdict: DD-BW1 · fix · 3 error, 20 should-fix, 12 minor
