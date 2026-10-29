---
audit: fresh check
unit: DD-B3 · Deep dive: how the best practitioners use the tool
course: brand-ai · B · Using AI to Build a Brand
model: Fable 5.1 (search on)
date: 2026-10-29
chat: own Fable 5.1 agent context, not shown the writing, in session https://claude.ai/code/session_01KMmgQzb1Ye3NC2dF9LAdKc
verdict: fix · 1 error, 3 should-fix, 9 minor (all applied the same day; the ninth minor is a note with no fix)
---

# Fresh check · DD-B3 · Deep dive: how the best practitioners use the tool

Checker: Fable 5.1, isolated context, live search on, 29 October 2026. Did not see the unit written. Reports; edits nothing.

Read: sourcing-standard.md Part 1 and Part 2; the DD-B3 brief in `generator/data/brand-ai/units_data.py`; the Audit 1 report (artifact 2uA7uLCuUAGRZuUoywpaRj, full HTML read); the unit's full text; B1, B2, B3, B4 for every pointer. Every cited web source was opened or attempted on 29 October 2026; X status links were not opened (robots rule), and their dates were re-decoded from the snowflake IDs independently.

## 1 · Coverage against the brief

| Brief item | Status |
|---|---|
| "Karpathy method" is a label by others; build only from his own words; AISN 2026 treated as unsourced | covered (§1.0) |
| Vibe-coding post (Feb 2025) and later distinction from agentic engineering | covered (§1.1); the Feb 2026 renaming post not found, said so |
| "How I use LLMs" (Feb 2025) | thin, by design: chapter list only, content unverified, stated as such (§1.2) |
| Software 3.0 at YC: autonomy slider, generation–verification loop, leash, context window as lever | covered (§1.3), all four |
| Context engineering over prompt engineering (Jun 2025) | covered (§1.4) |
| Dwarkesh (Oct 2025); Jan 2026 post: 80/20 shift; reviewing as a separate skill; failure modes | covered; "reviewing as a separate skill" thin and listed unsure (see finding 4: The Decoder does carry the point as paraphrase) |
| nanochat (Oct 2025); autoresearch (Mar 2026): loop, one file, five-minute budget, keep-or-revert, ~700 run and gain | covered (§1.6) |
| LLM Knowledge Bases (Apr 2026): layers, operations, Markdown as truth, ~100 articles / 400,000 words, no vector store | covered (§1.7) |
| Sequoia AI Ascent 2026: verifiability; outsource thinking, keep understanding | covered (§1.8) |
| Move to Anthropic (May 2026) as context | covered (§1.9) |
| Anthropic: Building effective agents; Effective context engineering; Claude Code best practices | covered (§2.1) |
| OpenAI: practical guide; model prompting guides | covered; guides thin (GPT-4.1 only, rest pointed to B3 §2, §5) |
| Willison: vibe coding definition; how he uses LLMs for code; lethal trifecta | covered (§2.3) |
| Mollick: four principles; BCG experiment with sample size and where performance fell | covered (§2.4) |
| Spec-driven: Reed, Spec Kit, Kiro | covered (§2.5) |
| CoT, ReAct, self-consistency, Sprague et al. | covered (§2.6) |
| Per method: claim, evidence, written for, transfers; software-only said so | covered (§3 table, cards) |
| Already does without the name; collides with B1, B2 and later units | covered (§4) |
| Flags for B4, B5, DD-B1; DD-B1 keeps agents | covered (§5) |
| Deliverable: method cards; ten operating rules traced to cards | covered (Deliverable A, B) |

Nothing missing.

## 2 · Findings

[error] [accuracy] §2.1 Claude Code best practices; Current: `retires that advice in a table headed "What you can stop doing": those phrases "are ordinary prompt text that nudges Claude within its effort setting rather than keywords that raise it"`; Problem: "those phrases" refers back to the four words from Willison, including "ultrathink". The table row names only `think hard`, `think harder`, `be thorough`, and the same row says "`ultrathink` still works: it asks for deeper reasoning on that single turn without touching your effort setting." The page also recommends `ultrathink` in its effort section. The unit states the opposite of the source for one of the four words; Fix: `retires most of that advice in a table headed "What you can stop doing": "think hard", "think harder" and "be thorough" "are ordinary prompt text that nudges Claude within its effort setting rather than keywords that raise it", while "ultrathink still works: it asks for deeper reasoning on that single turn without touching your effort setting"`; Basis: Claude Code docs, Best practices, table "What you can stop doing" and section on effort, https://code.claude.com/docs/en/best-practices (read 29 Oct 2026).

[should-fix] [attribution] §1.8 Sequoia AI Ascent 2026; Current: `The talk video was not opened; his own written summary was`; Problem: the page's summary is not written by Karpathy. The post opens "AI generated content below for this talk follows" and explains he fed an LLM his posts and the transcript to produce a summary and a cleaned-up transcript. The unit, K2 and K10 treat it as his own prose. Also "The agents fill in the blanks" sits in the cleaned-up transcript part of the page, not the summary; Fix: `The talk video was not opened; the summary he posted was, which he labels "AI generated content below for this talk follows", produced by an LLM from the transcript and his earlier posts, and published under his name with a cleaned-up transcript`; Basis: Karpathy, Sequoia Ascent 2026 summary, 30 Apr 2026, https://karpathy.bearblog.dev/sequoia-ascent-2026/. (The same qualification applies to §1.1 `His summary of his Sequoia AI Ascent talk (30 April 2026) separates two things.` → `The LLM-generated summary of his Sequoia AI Ascent talk that he posted on 30 April 2026 separates two things.`)

[should-fix] [accuracy] §1.7 LLM Knowledge Bases; Current: `("at roughly 100 articles and 400,000 words, the LLM can navigate via summaries and index files")`; Problem: in quotation marks but not VentureBeat's words. The article reads "Karpathy notes that at a scale of ~100 articles and ~400,000 words, the LLM's ability to navigate via summaries and index files" is more than enough; Fix: `(VentureBeat: "at a scale of ~100 articles and ~400,000 words, the LLM's ability to navigate via summaries and index files" suffices)`; Basis: VentureBeat, 3 Apr 2026, https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an.

[should-fix] [coverage] §1.5 Reviewing as a separate skill; Current: `No reachable reproduction of the January 2026 post contains it.`; Problem: The Decoder, which the unit cites for the same post, carries the point in its own paraphrase: "being good at reviewing code doesn't mean you can still write it yourself, since generation and discrimination are different abilities in the brain" (not in quotation marks). The brief item can be sourced to that reporter's paraphrase instead of only a Telegram reproduction of a 2025 post; Fix: `The Decoder's report of the post carries it only as paraphrase, without quotation: being good at reviewing code does not mean you can still write it, "since generation and discrimination are different abilities in the brain" (The Decoder's wording, not marked as his).`; Basis: The Decoder, 27 Jan 2026, https://the-decoder.com/former-tesla-ai-chief-andrej-karpathy-now-codes-mostly-in-english-just-three-months-after-calling-ai-agents-useless/.

[minor] [accuracy] §1.5 January 2026; Current: `calling it the "biggest change to my basic coding workflow in ~2 decades"`; Problem: the quoted string appears only in The Decoder's meta description; the article body paraphrases ("roughly two decades of programming"); Fix: `calling it, in the article's standfirst quotation, the "biggest change to my basic coding workflow in ~2 decades"`; Basis: The Decoder, same URL.

[minor] [attribution] §2.1 Claude Code best practices; Current: `appeared on 18 April 2025 by the engineering blog's URL`; Problem: the URL (`/engineering/claude-code-best-practices`) carries no date and Willison gives none; 18 April 2025 is confirmed by later reports, not by the URL; Fix: `appeared on 18 April 2025 (date as later reports give it; Willison noted it the next day)`; Basis: Willison, 19 Apr 2025, https://simonwillison.net/2025/Apr/19/claude-code-best-practices/; Tech Bytes, https://techbytes.app/posts/claude-code-best-practices-for-agentic-coding-apr-18-2025/.

[minor] [accuracy] §2.1 Claude Code best practices; Current: `Once it has that, it can keep going on its own."`; Problem: the source sentence continues "and you don't have to watch"; the quotation closes with a full stop the source does not have there; Fix: `Once it has that, it can keep going on its own and you don't have to watch."`; Basis: Claude Code docs, Best practices, https://code.claude.com/docs/en/best-practices.

[minor] [accuracy] §2.5 Harper Reed; Current: `"This is working well NOW, it will probably not work in 2 weeks"`; Problem: the sentence continues ", or it will work twice as well"; cut mid-sentence without an ellipsis, and the cut drops the half that balances it; Fix: `"This is working well NOW, it will probably not work in 2 weeks, or it will work twice as well"`; Basis: Reed, 16 Feb 2025, https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/.

[minor] [accuracy] §1.1 Sequoia; Current: `Agentic engineering is the professional discipline of coordinating fallible agents while keeping correctness, security and maintainability`; Problem: the source list is "correctness, security, taste, and maintainability"; "taste" is dropped from a near-quotation; Fix: `Agentic engineering is the professional discipline of coordinating fallible agents while preserving "correctness, security, taste, and maintainability"`; Basis: https://karpathy.bearblog.dev/sequoia-ascent-2026/.

[minor] [attribution] §1.0; Current: `the reporting article says Karpathy has not explicitly endorsed it`; Problem: the article's full answer is "Not explicitly, but he has amplified the project" (shared it on his channels); the omission makes the distance larger than the source states; Fix: `the reporting article says Karpathy has not explicitly endorsed it, though it adds that he has shared the project`; Basis: Pillitteri, 4 May 2026, https://pasqualepillitteri.it/en/news/1872/karpathy-claude-md-trending-github-llm-coding.

[minor] [accuracy] §4 collision 2; Current: `auditors "report; do not fix"`; Problem: not method.md's exact words; §6 says "Do not fix the units; report." and "The auditor never edits a unit; it reports."; Fix: `auditors "never edit a unit"; they report`; Basis: `/home/claude/learning/docs/method.md` §6.

[minor] [attribution] §4 collision 3; Current: `whose amount per chat is undocumented (B1 §3, B4 §1)`; Problem: B1 §3 describes what memory stores and excludes; the "how much is not documented" line is in B1 §7's table and in B4 §1; Fix: `whose amount per chat is undocumented (B1 §7, B4 §1)`; Basis: `/home/claude/learning/courses/brand-ai/B1-mental-model.md` lines 61–91 and 167; B4 line 23.

[minor] [figure] §1.6 autoresearch; Current: `Repository last committed 25 March 2026`; Problem: unverifiable here (GitHub commit pages and API refused); the README page shows 36 commits and no date; keep, but it is the only repository date in the unit I could not confirm; Fix: none required; note for the maintainer; Basis: https://github.com/karpathy/autoresearch (opened; commit history not reachable).

## 3 · Figures
Every number names its owner: 80/20 (his own report, via The Decoder); ~700 / ~20 (VentureBeat paraphrase, marked unverified); 2.02 → 1.80 → 1.65 h (his leaderboard); 11% / 18% (writer's arithmetic, labelled); ~100 sources / 400,000 words (gist vs VentureBeat, separated); 907,260 characters (B4 F1); 1,000–2,000 tokens (Anthropic); 758 / 12.2% / 25.1% / 19 points / 40% / 84% vs 60–70% (SSRN, HBS, Mollick, each named); 20% / 4% (OpenAI internal, labelled vendor); 17.9 / 11.0 / 12.2 / 34 / 10 (papers). No orphan figure found.

## 4 · Labels
Vendor labelled on Anthropic (×3), OpenAI (×2), GitHub, AWS. Anecdote labelled on Reed. Measured / documented practice / stated opinion given per method and per card. The one measured study (Dell'Acqua) is an experiment, not correlational, and is graded measured with model and year. The Sequoia summary is the one label gap (finding 2).

## 5 · Deliverable
Present in full: 26 method cards (K1–K10, A1–A3, O1–O2, W1–W3, M1–M2, S1–S3, P1–P3), each with author, primary source and date, one-sentence claim, grade, adopts, leaves; then ten operating rules, each traced to cards, in a paste-ready block. Every card points to the body section it rests on; no card adds a figure the body does not carry. Rule 10 ("No 'think harder' in prompts") stands after finding 1, since it names "think harder", not "ultrathink". Usable alone.

## 6 · Errata applied; pointers
Audit 1's 23 errata all touch A2/A6/A9 (audience-growth document); DD-B3 cites none of those sources or figures, so no erratum applies. Pointers checked against the filed units: B1 §1 (200K on claude.ai), §4 (cut-off), §5 ("One good answer is one draw"), §7 (memory amount undocumented, see finding 12); B2 §2 (Fable on Pro billed in credits at API rates), §7 (adaptive thinking, always on for Opus 5.5 and Fable 5.1); B3 §1 (Zheng et al., 162 roles, 2,410 questions, EMNLP Findings 2024), §2 (OpenAI reasoning-model guidance against Anthropic's), §4 (one question per response only when blocked; "The model takes the verb literally"); B4 §1, §2 (hot/warm/cold), F1 (33 files, 907,260 characters, cut to five), F13 (account memory off), F14 (eight connectors incl. Gmail, Google Drive, Vercel, Claude in Chrome; on demand), E (weekly rot check that reports); method.md §3 (audit row after every fourth unit), §5 (fresh checker), §6. All say what the unit says they say, with the one §3/§7 slip above.

## Confirmed
- Vibe-coding post quotations ("Accept All", "don't read the diffs anymore", "with no comment", "grows beyond my usual comprehension", "throwaway weekend projects"); Willison dates it "February 6th" without year; status 1886192184808149383 decodes to 2 Feb 2025 — https://simonwillison.net/2025/Mar/19/vibe-coding/
- Willison's definition, "not the same thing" sentence, commit rule, harm/security question — same URL
- MenuGen, 27 Apr 2025: "100% of the code was written by Cursor+Claude"; hallucinated deprecated APIs; "kind of messy and not a good idea for anything of actual importance" — https://karpathy.bearblog.dev/vibe-coding-menugen/
- Sequoia post dated 30 Apr 2026: "raises the floor", "fine for prototypes and personal tools", "raises the ceiling", specify/verify, "You can outsource your thinking, but you can't outsource your understanding", "macro actions", what is worth building / what result is suspicious — https://karpathy.bearblog.dev/sequoia-ascent-2026/
- Verifiability, 17 Nov 2025: resettable / efficient / rewardable definitions verbatim; Software 1.0 / 2.0 lines; jagged domains — https://karpathy.bearblog.dev/verifiability/
- Year in review, 19 Dec 2025: Claude Code "the first convincing demonstration of what an LLM Agent looks like" — https://karpathy.bearblog.dev/year-in-review-2025/
- Dwarkesh, 17 Oct 2025: "sweet spot", "very high information bandwidth", "fairly unique repository", "too much memory", "way too over-defensive", "It's just not net useful", "feel safer", Python reference + tests for the Rust tokenizer, boilerplate, "decade of agents"; the avoided library is PyTorch DDP (a wrapper module; the word "wrapper" is the unit's) — https://www.dwarkesh.com/p/andrej-karpathy
- The Decoder, 27 Jan 2026: 80/20 November → December; "mostly programming in English"; "watch them like a hawk"; "slightly sloppy, hasty junior dev"; failure list including ~1,000 → ~100 lines; links status 2015883857489522876 (decodes 26 Jan 2026) — URL above
- Code with Andrea, 28 Jan 2026: "Don't tell it what to do, give it success criteria and watch it go" presented as his words; atrophy point as the newsletter's own summary — https://codewithandrea.com/newsletter/january-2026/
- Willison, 26 Feb 2026: "coding agents basically didn't work before December and basically work since"; linked status 2026731645169185220 decodes 25 Feb 2026 — https://feeds.simonwillison.net/2026/Feb/26/andrej-karpathy/
- SD Times, 6 May 2026: anniversary framing, no quotation, no link; other outlets (marigold.cz 08.02.2026, tianpan.co) place the post on 8 Feb 2026 with no quoted words — https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/
- How I use LLMs: channel Andrej Karpathy, published 27 Feb 2025, 22 chapters matching the unit's list, final chapter at 2:06:30 — https://www.youtube.com/watch?v=EWvNQjAaOHw
- Analytics Vidhya, 8 Mar 2025: new-chat advice is paraphrase, no quotation — https://www.analyticsvidhya.com/blog/2025/03/how-andrej-karpathy-uses-llms/
- YC video published 18 Jun 2025, keynote 17 Jun 2025, AI Startup School, San Francisco — https://www.youtube.com/watch?v=LCEmiRjPEtQ
- billmill transcription: all seven quoted phrases verbatim ("autonomy slider" ×2, "Iron Man suits", "generation … verification", "keep the AI on the leash", "small incremental chunks", "working memory"); Perplexity and GUI points are paraphrase, unquoted in the unit — https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html
- Context engineering via Willison, 27 Jun 2025: all quoted phrases verbatim; Lütke "describes the core skill better"; Karpathy status decodes 25 Jun 2025, Lütke's 19 Jun 2025 (six days earlier) — https://simonwillison.net/2025/Jun/27/context-engineering/
- Telegram css_nlp post 105: both GAN quotations present, links status 1930305209747812559 (decodes 4 Jun 2025); no calendar date shown — https://t.me/s/css_nlp?after=103
- nanochat initial commit 3a5e0bc, 2025-10-13T13:49:24Z, "initial commit"; README: "full-stack implementation … dependency-lite codebase", "~8K lines of code in 45 files", package and paste to an LLM — https://github.com/karpathy/nanochat/commit/3a5e0bc, https://api.github.com/repos/karpathy/nanochat/commits/3a5e0bc
- nanochat README disclosure policy verbatim; latest commit 3 Jul 2026 — https://github.com/karpathy/nanochat
- LEADERBOARD: run 5, 9 Mar 2026, 1.80 h "from 2.02 hours"; run 6, 14 Mar 2026, 1.65 h; autoresearch sentence verbatim; 10.9% and 18.3% check — https://github.com/karpathy/nanochat/blob/master/dev/LEADERBOARD.md
- autoresearch README: loop sentence, "the single file the agent edits", "super lightweight 'skill'", "keeps the scope manageable and diffs reviewable", ~12/hour and ~100 overnight, "not comparable to other people running on other compute platforms"; program.md: git reset rule, 0.001/20 lines, deleting-code rule, 10-minute kill and revert, "The loop runs until the human interrupts you, period.", prepare.py read-only, no new packages — https://github.com/karpathy/autoresearch, https://raw.githubusercontent.com/karpathy/autoresearch/master/program.md
- VentureBeat, 9 Mar 2026: ~700 autonomous changes over two days on depth=12, ~20 improvements transferring to larger models; links status 2031135152349524125 (decodes 9 Mar 2026) and 2030371219518931079 (decodes 7 Mar 2026) — https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai
- VentureBeat, 3 Apr 2026: "You rarely ever write or edit the wiki manually; it's the domain of the LLM"; status 2039805659525644595 decodes 2 Apr 2026 — URL above
- Gist created 4 Apr 2026: "immutable", "The LLM owns this layer entirely", CLAUDE.md/AGENTS.md, "10-15 wiki pages", index and append-only log, "~100 sources, ~hundreds of pages", "avoids the need for embedding-based RAG infrastructure", "never (or rarely)", "rediscovering knowledge from scratch on every question", lint list; no word count — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- TechCrunch, 19 May 2026: pre-training under Nick Joseph; spokesperson: a team "focused on using Claude to accelerate pre-training research"; status 2056753169888334312 decodes 19 May 2026 — https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/
- Pillitteri, 4 May 2026: Forrest Chang (Jiayuan Zhang), four principles, from the 26 Jan 2026 post; no AISN mention — URL above
- SozAI title as cited; it is the page that cites "AISN 2026"; Noqta title as cited, 17 Mar 2026 — https://sozai.app/transcript/stop-prompting-claude-karpathys-method/index.md, https://www.noqta.tn/en/blog/karpathy-autoresearch-autonomous-ai-experiments-loop-2026
- Anthropic, Building effective agents, 19 Dec 2024: workflows/agents definitions, simplest-solution line, open-ended problems, five patterns, three principles incl. "explicitly showing the agent's planning steps" — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, Effective context engineering, 29 Sep 2025: all four quoted phrases; 1,000–2,000 tokens; "substantial improvement over single-agent systems" with no figure — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Claude Code best practices (29 Oct 2026): 1M-token retirement row verbatim; reviewer "without having watched it being written"; SPEC.md interview and "start a fresh session to build from it"; "/clear plus one new prompt that folds in what you learned works better almost every time" after two failed corrections; five questions as listed — https://code.claude.com/docs/en/best-practices
- Willison, 19 Apr 2025: "think" < "think hard" < "think harder" < "ultrathink"; links anthropic.com/engineering/claude-code-best-practices; gives no post date — https://simonwillison.net/2025/Apr/19/claude-code-best-practices/
- OpenAI agents PDF: undated; all five quoted phrases present; three criteria as described; 33 pages including cover (Maginative, 17 Apr 2025, says 32) — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/
- GPT-4.1 guide, 14 Apr 2025, MacCallum and Lee, archived: "more closely and more literally", "close to 20%", "4%", beginning-and-end placement — https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide
- Willison, 11 Mar 2025: three quotations verbatim; cut-off and options points — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- Willison, 16 Jun 2025: three components, "avoid that lethal trifecta combination entirely", "95% of attacks" / "failing grade" — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Arango notes: four principles as quoted — https://jarango.com/readings/co-intelligence/; Portfolio, 2 Apr 2024 — https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/9780593716724
- SSRN, posted 18 Sep 2023: pre-registered, 758, three conditions, 12.2%, 25.1%, >40% quality, "19 percentage points", Centaurs/Cyborgs "completely integrating their task flow with the AI" — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321; HBS WP 24-013, Sep 2023, nine authors, forthcoming Organization Science; HBS abstract says "19% less likely" (unit correctly sources the percentage-point wording to SSRN) — https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- Mollick, 16 Sep 2023: "40% higher quality", 84% vs 60–70% — https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged
- Reed, 16 Feb 2025: one question at a time, spec.md, prompt_plan.md, todo.md, "success really depends on how well step 2 went", "largely a solo endeavor"; reasoning model for step 2 — URL above
- Spec Kit, 2 Sep 2025, Delimarsky: source-of-truth sentence, /specify /plan /tasks, "small, reviewable chunks", "our experiment" — https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Kiro, 14 Jul 2025, Swaminathan and Singh: EARS acceptance criteria, design document, tasks linked to requirements, free during preview — https://kiro.dev/blog/introducing-kiro/
- Wei et al., v1 28 Jan 2022, no venue on page; 540B, eight exemplars, GSM8K SOTA, arithmetic/commonsense/symbolic — https://arxiv.org/abs/2201.11903
- Yao et al., v1 6 Oct 2022, ICLR camera-ready; hallucination vs CoT; 34% and 10% absolute — https://arxiv.org/abs/2210.03629
- Wang et al., v1 21 Mar 2022, ICLR 2023; +17.9 / +11.0 / +12.2 — https://arxiv.org/abs/2203.11171
- Sprague et al., v1 18 Sep 2024, v3 7 May 2025, no venue; "over 100 papers", "20 datasets across 14 models", "primarily on tasks involving math or logic", equals-sign finding — https://arxiv.org/abs/2409.12183
- All X status dates in the unit (2 Feb 2025, 4 Jun 2025, 25 Jun 2025, 26 Jan 2026, 25 Feb 2026, 7 and 9 Mar 2026, 2 Apr 2026, 19 May 2026) re-decoded from the snowflake IDs and agree.

DD-B3 · verdict: fix · error 1 · should-fix 3 · minor 9
