---
audit: stratified-sample audit (Audit 2)
unit: B2 · Choosing the model; B3 · Prompting that holds up; B4 · Context engineering; A1 · Positioning: the journey as a format
course: brand-ai · A and B
model: Fable 5.1 (search on)
date: 2026-10-29
chat: own Fable 5.1 agent context, not shown the writing, in session https://claude.ai/code/session_01KMmgQxKYpiNhvdU89G4hYp
verdict: B2 PASS (1 FAIL incidental, 10 STALE; errata B2-1 to B2-25) · B3 PASS · B4 PASS · A1 PASS (erratum A1-1, P33); all errata applied the same day
---

# Audit 2 · Brand + AI · B2, B3, B4, A1

Fable 5.1, 29 October 2026, live search. Read first: `docs/sourcing-standard.md` Parts 1 and 2; `docs/method.md` §5–§6; the four units in full; the five fresh-check reports (for provenance only; nothing reused). No file edited. Repository at `de82d77`; B4's figures re-measured at the commit it cites, `b4fea09`, after deepening the clone.

**Provenance.** All four units were written by Opus 5.5 and fresh-checked by Fable 5.1 (B2 after filing under P18, the others before filing; A1 §6 rewritten and re-checked separately). The sample does not split by provenance.

**Sample.** Recorded before checking: one claim per numbered section plus the deliverable. Claims checked beyond the sample while opening the same sources are listed under "Also checked" and counted in the totals; the decision rule is applied to the sample only.

---

## B2 · Choosing the model (search on, written 28 Oct 2026)

| § | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| 1 | Opus 5.5 beats Fable 5.1 on all nine tests in Anthropic's table: Terminal-Bench 4.0 66.4% (xhigh) v 55.8%, GDPval-AA v2.1 1846 v 1735, HLE 67.7% v 65.6% | anthropic.com/claude-opus-5-5 | PASS | Nine rows, all nine favour Opus 5.5; figures exact |
| 2 | Fable on Pro outside limits, on credits; on Max up to half the weekly limit, drains the pool faster; Team/Enterprise premium seats include it, standard seats pay credits; article dated 2 Sep 2026 | support.claude.com/en/articles/15424964 | PASS | Exact |
| 3 | Haiku 5.5 cliff at 100K counts cache reads and writes; other models bill the full 1M at one rate; batch 50% off; web search $10 per 1,000; 4.7+ tokenizer ~30% more tokens | platform.claude.com/docs/en/about-claude/pricing | PASS | All quoted on the page |
| 4 | Gemini 4 Argon $2/$10 to 30 Nov 2026, $4/$20 from 1 Dec; 3.8 Flash $0.75/$3.75 to 31 Dec, $1.50/$7.50 from 1 Jan 2027; output includes thinking | ai.google.dev/gemini-api/docs/pricing | PASS | Exact |
| 5 | Artificial Analysis leaderboard, accessed 28 Oct 2026: Opus 5.5 low–max 42/51/54/56/58 at $0.55/$1.34/$1.82/$3.46/$5.98; Sonnet, Haiku, Fable, Sol, Luna, Argon, 3.8 Flash, DeepSeek rows; four readings | artificialanalysis.ai/leaderboards/models | STALE | The leaderboard now carries Intelligence Index v5.0 (announced 27 Oct 2026, artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5). Today: Opus 5.5 35/48/52/57/58 at $0.98/$2.45/$3.46/$6.05/$10.04; Sonnet 5.5 25/30/41/50/54 at $0.51/$0.78/$1.64/$4.09/$10.02; Haiku 5.5 19/25/30/34/36 at $0.04/$0.09/$0.16/$0.25/$0.41; Fable 5.1 38/43/47/50/49 at $4.49/$5.58/$7.56/$10.89/$13.04; GPT-6.1 Sol high 50 $0.59, max 55 $1.27; GPT-6 Luna max 28 $0.15; Gemini 4 Argon high 50 $3.84; Gemini 3.8 Flash high 31 $7.77; DeepSeek V4.1 Flash max 32 $0.60. The fresh check of 28 Oct confirmed the unit's figures as exact that day, so they were true when written. All four readings hold in direction on the new figures (see Errata) |
| 6 | FrugalGPT: prices differ by two orders of magnitude; cascade matches GPT-4 with up to 98% cost reduction; RouteLLM cuts cost by more than half; Snell et al.: smaller model with test-time compute beats one 14x larger on problems where it has non-trivial success | arxiv 2305.05176; ICLR 2025 proceedings (RouteLLM); arxiv 2408.03314 | PASS | RouteLLM abstract says "over 2 times", consistent with "more than half" |
| 7 | Defaults: API Opus 5.5 and Haiku 5.5 medium, Sonnet 5.5 and Fable 5.1 high, Opus 5 high; apps Sonnet 5.5 medium; Fable 5.1 medium on claude.ai and Cowork, high in Claude Code | Effort page; Models overview; Sonnet 5.5 and Fable 5.1 launch pages | PASS | Exact |
| 8 | AA-Omniscience v1.1 (3,000 questions, six domains; wrong answers penalised, abstention not): Fable 5.1 highest accuracy 68%; Opus 5.5 highest index 48 v 46 Fable and Argon; Argon lowest hallucination 4% | artificialanalysis.ai/evaluations/omniscience | STALE | Fable accuracy 68% and Argon 4% still lead. Highest index is now Gemini 4 Carbon (High), 54, which the page lists as of 29 Oct 2026; Opus 5.5 stays at 48 |
| Del | Course-units row: Opus leads Sonnet by 10 index points at default effort; medium→high adds 3 points for 36% more; Journal row: Sonnet at medium is 36% of Opus's per-task cost | leaderboard (§5, §7, §8) | STALE | On today's figures: 48 v 30 (18 points); medium→high +4 points for 41% more ($2.45→$3.46); Sonnet medium $0.78 is 32% of Opus medium $2.45. Picks unchanged |

Also checked (14): Opus 5.5 launch date, 40% cost claim, "about a fifth" claims v Opus 5 and GPT-6 Astra, five-hour limit increase with no figure (PASS); Models overview positioning strings, 1M/128K/Jun 2026, start-with-Opus advice (PASS); Pro usage 45 messages / 200 sentences / Claude Code shares the limit (PASS); Max 5x $100, 20x $200, 225/900, 200K on every plan (PASS); claude.com/pricing $20/$17, no euro prices (PASS); usage credits prepaid at API rates (PASS); Steering thinking: billed as output in full, prior thinking billed as input, cache invalidated on effort change with the two exceptions, lower effort before prompting (PASS); Effort page: behavioural signal, xhigh >30 min, Haiku low/high guidance, Opus 5.5 thinking cannot be disabled (PASS); Help Center effort labels, thinking cannot be switched off in the apps, defaults marked in menu (PASS); Fable 5.1 launch: same model as Mythos 5.1, trusted-access programmes, routing to Opus, ~25% cheaper than Fable 5, GDPval-AA v2 1853 (PASS); Haiku 5.5 launch figures 1620/1840, 1578/1824, 39.2%/70.6%, 46.4%, 57.4%, Sonnet-or-Opus recommendation (PASS); Sonnet 5.5 launch 1846/1844, 1822/1811, 67.7/64.5, 70.6, 54.4/52.1 xhigh, pre-release bug note, "careful judgment" (PASS); OpenAI pricing, GPT-6.1 Sol five effort levels with medium default and separate-model treatment, The Next Web 22 Sep (PASS); DeepSeek yuan prices, peak hours, 1M/384K, `reasoning_effort` example (PASS); Argon model page levels, 1,048,576 and 65,536, updated 14 Oct 2026, Google blog rollout order (PASS); Zheng et al. >80% and biases, Panickssery et al. self-preference and linear correlation, Chen et al. overthinking (PASS); **Claude Code post (Hallie, 7 Jul 2026): the diagram caption reads "The high effort path generates roughly 7x more tokens to reach a higher confidence answer" and carries no disclaimer; the "for illustration purposes only… do not represent real benchmark data" labels are on the two cost-curve charts, and "IDs shown are illustrative" is on the tokenizer figure. The unit's statement that "the post labels its curves illustrative" as the reason the seven-times figure "is not evidence" is a miscite: FAIL (incidental, §7 and unsure item 10).**

Failure rate: sample 0 of 9 FAIL (3 STALE); with the incidental finding 1 of 23 checked. Decision rule: no full audit.

**Deliverable.** Present in full; ten task rows with model, effort, reason and override; five rules; usable alone. Every "Why" cites a section; the three third-party numbers in it are the stale ones above, and the picks survive the new figures (Opus still leads Sonnet at medium, now by more; Sonnet medium still a third of Opus medium). The staleness-check date (28 April 2027) is six months out, but the Artificial Analysis layer went stale in a day; the deliverable's own rule "re-read the prices" should name the index too.

**Course goal and standard.** Moves the reader to a routing decision with the evidence graded (vendor / third-party vendor / peer-reviewed / own record). Nothing reads as advice without evidence; syntheses are marked as the writer's. Standard met, with the §7 miscite and the stale figures as the exceptions.

**Verdict: PASS**, errata below (one FAIL, one block of STALE replacements).

---

## B3 · Prompting that holds up (search off, written 28 Oct 2026)

| § | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| 1 | Zheng et al.: 162 roles, 2,410 factual questions, four model families; persona did not improve performance; best persona per question helped; automatic selection no better than random | aclanthology.org/2024.findings-emnlp.888 | PASS | Exact, pages 15126–15154 |
| 2 | IFScale: 20 models, seven providers, up to 500 keyword-inclusion instructions, best models 68% at 500, bias toward earlier instructions; NeurIPS 2025 workshop poster | arxiv 2507.11538; neurips.cc/virtual/2025/122417 | PASS | Exact |
| 3 | LIFEBench: 26 models, 16–8,192 words, English and Chinese; "most models reasonably follow short-length instructions but deteriorate sharply beyond a certain threshold"; almost all fall short of vendor-claimed max lengths | arxiv 2505.16234; NeurIPS 2025 D&B | PASS | Exact |
| 4 | Laban et al.: 200,000+ simulated conversations, "an average drop of 39% across six generation tasks", quotes on early assumptions and not recovering; 15 models incl. Claude 3.7 Sonnet, GPT-4.1, o3, Gemini 2.5 Pro; §7.4 advises consolidating into one instruction and starting a new conversation | arxiv 2505.06120 (abstract and HTML) | PASS | 15 models confirmed in the paper body; §7.4 wording confirmed |
| 5 | Anthropic: for 20K+ token inputs, documents at top, query at end; "Queries at the end can improve response quality by up to 30 percent in tests, especially with complex, multidocument inputs" | Prompting best practices | PASS | Exact; no method published, as the unit says |
| Del | Template 5: YouTube A/B test takes up to three titles or thumbnails and picks the winner on watch time | support.google.com/youtube/answer/16391400 | PASS | "up to 3", "highest watch time", optimised over CTR |

Also checked (22): "brilliant but new employee", colleague test, role "focuses Claude's behavior and tone", 3–5 examples, "Tell Claude what to do instead of what not to do" with the markdown example, ellipsis/TTS and "generalize from the explanation", "can you suggest some changes", "more than the task strictly requires", "Might skip detailed summaries", "removing markdown from your prompt", "The more precisely you explain", chaining "inspect intermediate outputs" (all PASS, exact); Opus 5.5 guide: "mostly swaps one default", "name specific patterns", "check which styles the first result used", "tends to get to work quickly", remove think-carefully lines in chat, "completion condition up front" (PASS); Fable 5.1 guide: "one complete example of a correct response", rationale sentence, "the scope is the deliverable" (PASS); Sonnet 5.5 guide open-ended quote (PASS); Claude blog 10 Nov 2025 three quotes (PASS); Effective context engineering: all seven quotes and the 29 Sep 2025 date (PASS); Google prompt strategies four quotes, updated 13 Oct 2026 (PASS); OpenAI help article four quotes, relative date only (PASS); OpenAI API guide three quotes (PASS); Claude Code Memory: "concrete enough to verify", 2-space example, "may pick one arbitrarily", specific-and-concise sentence (PASS); personalisation article quotes and no precedence (PASS); Reduce hallucinations three recommendations (PASS); Define success criteria "accurate sentiment classification" (not opened; unverifiable is not claimed since the page was not needed for the sample); Min et al. "barely hurts performance", 12 models, three drivers (PASS); Jang et al. inverse scaling, PMLR 203 52–62 (PASS); Chia et al. no figure, no venue (PASS); Levy et al. two quotes, pages (PASS); Shi et al. GSM-IC quote, ignore-instruction mitigation (PASS).

Failure rate: 0 of 6 sampled; 0 of 28 checked.

**Deliverable.** Ten templates, each with a worked example, all built in full; the conventions, model lines and avoid-lists trace to sections; usable alone. Model lines without a B2 row are marked as analogies. Template 2's worked example is this audit's own prompt and matches `method.md` §6 verbatim.

**Course goal and standard.** Vendor guidance, research and his setup are labelled throughout; every quotation checked is the source's exact words; syntheses are marked. No advice without evidence found. Standard met.

**Verdict: PASS.** No errata.

---

## B4 · Context engineering (search off, written 29 Oct 2026)

| § | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| 1 | Skills: name and description at startup, ~100 tokens per skill; SKILL.md body under 5k tokens when a request matches; bundled files cost nothing until read | platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | PASS | Exact |
| 2 | Seven filed units 358,052 characters; 137 history reports 3,484,164 (Unicode, by script, at `b4fea09`) | repository | PASS | Reproduced exactly at `b4fea09` (seven units 358,052; `kit/greece` + `kit/rome` r-*.html 137 files, 3,484,164). At `de82d77` the vault holds eight units, 420,524 |
| 3 | Project instructions 4,421 characters, 675 words (C locale), 27 lines; knowledge 33 files, 907,260 characters; five-file set 79,332 | repository | PASS | 4,421 / 675 / 27 and 79,332 reproduced at `b4fea09`; the five units in the knowledge 242,926 reproduced. The 33-file total was not re-summed (the Project file list is not in the repository); the fresh check reproduced it |
| 4 | "Try starting a new conversation if you're approaching your usage limit in a longer chat"; cached project content counts less, caches expire after inactivity | support.claude.com/en/articles/11647753; 9797557 (22 Sep 2026) | PASS | Exact |
| 5 | Claude Code: "if two instructions contradict each other, Claude may pick one arbitrarily"; prompt audit looks for "instructions written for older models, references to files or commands that don't exist, and files that contradict each other" | code.claude.com/docs/en/memory | PASS | Exact |
| Del | F12: the stratified-sample prompt (1,547 characters) in `method.md` §6 is identical to the copy in `hub.py` | repository | PASS | 1,547 characters, identical at `b4fea09` |

Also checked (14): personalisation and projects articles quotes (PASS); RAG article quotes and 10 Sep 2026 date, "can automatically convert back to context-based processing" (PASS); What are skills? three quotes, 22 Sep 2026 (PASS); memory article: topics, per-project memory, "alongside", "Use account memory" toggle, amount unstated (PASS); tool access: three modes with definitions, Auto default, the two table rows, 16 Mar 2026 (PASS); "Tools and connectors are token-intensive", remove unused project files (PASS); scheduled tasks page: "a saved Claude Code configuration…", "self-contained and explicit…", "unattended, repeatable, and tied to a clear outcome", research preview, sub-hourly rejected, env vars visible to anyone using the environment, connectors included by default, subscription usage (all PASS, exact); Effective context engineering quotes (PASS); Claude Code Memory "facts Claude should hold in every session" and "move it to a skill" (PASS); GitHub integration adds files to project knowledge, "Sync now" (PASS); GitHub docs "may still be accessible elsewhere" (PASS); F8 four prose lists at `method.md` line 114, `SETUP.md` line 38, `hub.py` lines 127 and 139 (PASS, verbatim); F11 `build.py` line 733 reads `shell.css`, `cmp` silent (PASS); F10 rows B-1 and B-3 in `docs/BACKLOG.md` at `b4fea09` (PASS; closed since by `f565373`).

Failure rate: 0 of 6 sampled; 0 of 20 checked.

**Deliverable.** Present in full: method, layer table, 17 findings each with layer, evidence, fix and effort, revised instructions, six-check rot script with a scheduled-task prompt, ranked fix list. Every measured number I re-ran reproduces. Usable without the unit. F10 is already closed by later commits; the finding stays correct for its dated commit.

**Course goal and standard.** Product documentation, vendor guidance and observations are labelled; analogies from Claude Code to claude.ai are marked each time; effort figures are declared estimates. No advice without evidence. Standard met.

**Verdict: PASS.** No errata.

---

## A1 · Positioning: the journey as a format (search off, written 28 Oct 2026; §6 revised 29 Oct)

| § | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| 1 | Ries and Trout: "Positioning is what you do to the mind of the prospect, not what you do to the product"; "The mind rejects complexity"; the Frame's six-pieces test | grahammann.net book notes; `hub.py` FRAME | PASS | Both quotations on the notes page; Frame wording exact (secondary source, labelled) |
| 2 | OverseerOS, 21 Aug 2026: 1,620 videos, 163 channels, 1M+ views, 5+ per channel; 97.5%; median 20.0%; 91 channels, 4.53M v 4.65M, labelled exploratory; quoted conclusion | overseeros.com/blog/stick-to-one-niche-youtube | PASS | Exact; the page itself says observational, correlation not causation, as the unit's limits do |
| 3 | A6's playbook sets "hold one recognisable format per season" as YouTube rule 6 and the entry-door choice as rule 1 | A6 Deliverable lines 160, 165 | PASS | Exact |
| 4 | YouTube: name change "twice within a 14-day period", "Changing your name will remove your verification badge"; handle 3–30 characters, separators not at start or end; Data API 30-character channel title, 1,000-character description | support.google.com/youtube/answer/2657964, 11585688; developers.google.com/youtube/v3/docs/channels | PASS | Exact. The 30 characters is `brandingSettings.channel.title`; the unit says "channel title", which is what that property is |
| 5 | Creator table: Boyd 2.93M · 197 · 476,842,692 (Social Blade 17 Oct); Khare 5.5M · 277 · 926,028,639 (24 Oct); D'Avella 4.05M · 471 · 337,159,760 (vidIQ 26 Oct); Goal Guys 562,000 · 236 · 87,724,487 (28 Oct); Yes Theory 10.2M · 459 · 1,348,045,772 (26 Oct) | Social Blade, vidIQ | PASS (Boyd row unverifiable at its source) | Social Blade Mike Boyd refused the fetch (as it did the fresh check); vidIQ shows 2.93M · 197 · 476,918,067 for 28 Oct, consistent. Khare, Yes Theory, Goal Guys exact; Social Blade's Khare table now ends 25 Oct with the same views. D'Avella is dated and live (now 337,214,753, 28 Oct), not stale by the unit's own dating rule |
| 6 | Episode 1 11 Oct 2026, 4:06; episode 2 13 Oct 2026, 5:54, recorded ten days before the Global Cup; channel 17 subscribers, 11 videos; "Sometimes you win, sometimes you learn" earliest 10 Sep 2007 tweet, Maxwell book 2013 | YouTube watch pages; `audits/brand-ai/evidence/A1-episodes-2026-10-29.md`; barrypopik.com | PASS (episode 1 page unverifiable today) | Episode 2 title, channel, date and "10 days out" confirmed on YouTube; episode 1's watch page was rate-limited on both tries, so its details rest on the saved evidence file, which carries player data and captions. Popik page exact |
| Del | Channel description 794 characters, bio 121 (by script); Instagram 150/30 from Bitly (updated 29 Sep 2026); YouTube keeps handles "distinct from channel names" | unit text; bitly.com; YouTube handles page | PASS | 794 and 121 reproduced (code-block content without the trailing newline); Bitly modified-time 29 Sep 2026; quotation exact |

Also checked (18): YouTube 13615784 three quotations and their viewer categories (PASS); SEJ 4 Mar 2024 Beaupré "not overemphasize historical data if that data isn't particularly predictive" (PASS, fair paraphrase); Aaker and Keller abstract on fit and quality, CiteDrive showing 2018 (PASS, the unit's unsure item 6 covers it); Bottomley and Holden seven replications, quotation, 38(4) 494–500 (PASS); Laughing Squid 30 Dec 2016 description and six skills (PASS); Skillshare 24,394 students (PASS); OutlierKit 0.3 uploads/week, 11 Jul 2026 (PASS); Wikipedia Khare: series description exact, 2018 uncited, 2M April 2020 sourced to her tweet (PASS); TheTVDB nine 2019 "30 days" titles, eight dated 1 or 7 Jan (PASS); Rosetta 30 Mar and 9 Jun 2026 (PASS); vidIQ D'Avella zero change over 28 days, Goal Guys +1,000, Yes Theory +100,000 (PASS; vidIQ's windows have rolled forward one to three days, the unit's are dated); A9 §8 pivot claim and A9 quarter-3 date 3 Aug 2027 (PASS); A2/A6 pointers (PASS); YouTube handle quotation (PASS).

Failure rate: 0 of 7 sampled; 0 of 25 checked; 2 unverifiable at source.

**Deliverable.** Present in full: one sentence, 60-word expansion, test, three-option table with a pick in his decision format, YouTube description and Instagram bio with counted lengths. Follows §1–§6 and claims nothing unchecked. One line in §4 (option 3) now contradicts the deliverable: P33, erratum below.

**Course goal and standard.** The brief's claim is graded by source class and cut to what the evidence supports; survivors are labelled anecdote, OverseerOS as vendor, the transfer from brand-extension research as the writer's. No advice without evidence. Standard met.

**Verdict: PASS**, one erratum (P33).

---

## The three most consequential errors

1. **B2's third-party numbers went stale the day after writing.** Artificial Analysis moved its leaderboard to Intelligence Index v5.0 (announced 27 Oct 2026; the leaderboard still showed the old figures on 28 Oct, as the fresh check confirmed). Every index score and cost per task in §5, §7, §8 and two rows of the routing table is now different: Opus 5.5 at max costs $10.04 a task, not $5.98; Opus at medium scores 48 and Sonnet at medium 30, not 51 and 41. The picks survive; the stated gaps and ratios do not. The unit's own "where sources disagree" paragraph was describing the switch without knowing it.
2. **B2 §7 discards the Claude Code post's "roughly 7x" token figure on a false ground.** The post labels its cost-curve charts illustrative, not the diagram that carries the 7x caption. The figure is still just one unmeasured example, so the conclusion is right, but the source is misreported in two places (§7 and unsure item 10).
3. **A1 §4 option 3 still says "Handles built on a full name are often free (my inference; not checked)"** after §6 and the deliverable established that the handle @apcanario is already his on YouTube and Instagram. An unchecked guess sits beside a checked fact that answers it (P33).

**Bibliography:** add Artificial Analysis, "Announcing Artificial Analysis Intelligence Index v5", 27 October 2026, https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 (B2); no source to mark failed; Social Blade's Mike Boyd page is unverifiable by fetch (two audits running), keep vidIQ beside it.

**Changelog:** Audit 2 (Fable 5.1, 29 Oct 2026): B2, B3, B4, A1 sampled, 28 sampled claims and 96 checked in all; 1 FAIL (B2 §7 miscite, incidental), 10 STALE (all B2, one cause: Intelligence Index v5.0), 2 unverifiable; all four PASS; errata for B2 (stale figures, 7x miscite) and A1 (P33) to apply.

---

## Errata

Each "Current" occurs exactly once in its unit (checked with grep). Apply in order within a unit.

### B2 · Choosing the model

**B2-1** (§5, table row)
Current: `| Opus 5.5 (low / medium / high / xhigh / max) | 42 / 51 / 54 / 56 / 58 | $0.55 / $1.34 / $1.82 / $3.46 / $5.98 |`
Fix: `| Opus 5.5 (low / medium / high / xhigh / max) | 35 / 48 / 52 / 57 / 58 | $0.98 / $2.45 / $3.46 / $6.05 / $10.04 |`
Basis: https://artificialanalysis.ai/leaderboards/models, read 29 Oct 2026 (Intelligence Index v5.0).

**B2-2** (§5, table row)
Current: `| Sonnet 5.5 (low / medium / high / xhigh / max) | 36 / 41 / 47 / 52 / 56 | $0.35 / $0.48 / $0.88 / $2.01 / $5.46 |`
Fix: `| Sonnet 5.5 (low / medium / high / xhigh / max) | 25 / 30 / 41 / 50 / 54 | $0.51 / $0.78 / $1.64 / $4.09 / $10.02 |`
Basis: same.

**B2-3** (§5, table row)
Current: `| Haiku 5.5 (low / medium / high / xhigh / max) | 29 / 34 / 38 / 41 / 43 | $0.02 / $0.05 / $0.08 / $0.12 / $0.21 |`
Fix: `| Haiku 5.5 (low / medium / high / xhigh / max) | 19 / 25 / 30 / 34 / 36 | $0.04 / $0.09 / $0.16 / $0.25 / $0.41 |`
Basis: same.

**B2-4** (§5, table row)
Current: `| Fable 5.1 (low / medium / high / xhigh / max) | 47 / 49 / 51 / 53 / 53 | $2.37 / $2.98 / $3.91 / $5.98 / $7.63 |`
Fix: `| Fable 5.1 (low / medium / high / xhigh / max) | 38 / 43 / 47 / 50 / 49 | $4.49 / $5.58 / $7.56 / $10.89 / $13.04 |`
Basis: same.

**B2-5** (§5, table row)
Current: `| GPT-6.1 Sol (high / max) | 50 / 52 | $0.32 / $0.72 |`
Fix: `| GPT-6.1 Sol (high / max) | 50 / 55 | $0.59 / $1.27 |`
Basis: same.

**B2-6** (§5, table row)
Current: `| GPT-6 Luna (max) | 38 | $0.07 |`
Fix: `| GPT-6 Luna (max) | 28 | $0.15 |`
Basis: same.

**B2-7** (§5, table row)
Current: `| Gemini 4 Argon (high) | 53 | $1.62 |`
Fix: `| Gemini 4 Argon (high) | 50 | $3.84 |`
Basis: same.

**B2-8** (§5, table row)
Current: `| Gemini 3.8 Flash (high) | 41 | $3.49 |`
Fix: `| Gemini 3.8 Flash (high) | 31 | $7.77 |`
Basis: same.

**B2-9** (§5, table row)
Current: `| DeepSeek V4.1 Flash (max) | 45 | $0.26 |`
Fix: `| DeepSeek V4.1 Flash (max) | 32 | $0.60 |`
Basis: same.

**B2-10** (§5, table lead-in date)
Current: `accessed 28 Oct 2026):`
Fix: `accessed 28 Oct 2026, figures updated to Intelligence Index v5.0 on 29 Oct 2026 after Audit 2):`
Basis: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 (27 Oct 2026).

**B2-11** (§5, reading 1)
Current: `At medium effort it costs 2.8 times as much per task; at max, Sonnet costs 91% of what Opus costs and scores two points lower.`
Fix: `At medium effort it costs 3.1 times as much per task; at max, Sonnet costs the same as Opus (99.8%) and scores four points lower.`
Basis: arithmetic on B2-1 and B2-2 ($2.45 / $0.78; $10.02 / $10.04; 58 against 54).

**B2-12** (§5, reading 2)
Current: `Haiku 5.5 at max scores 43 against Opus 5.5 at low's 42, for 38% of the cost.`
Fix: `Haiku 5.5 at max scores 36 against Opus 5.5 at low's 35, for 42% of the cost.`
Basis: arithmetic on B2-1 and B2-3 ($0.41 / $0.98).

**B2-13** (§5, reading 3)
Current: `Gemini 3.8 Flash is 2.7 times cheaper per token than Argon and costs 2.2 times more per task, scoring 12 points lower.`
Fix: `Gemini 3.8 Flash is 2.7 times cheaper per token than Argon and costs 2.0 times more per task, scoring 19 points lower.`
Basis: arithmetic on B2-7 and B2-8 ($7.77 / $3.84; 50 against 31).

**B2-14** (§5, reading 4)
Current: `Around an index of 50 to 51: GPT-6.1 Sol at high costs $0.32, Opus 5.5 at medium $1.34 (4.2 times Sol), Fable 5.1 at high $3.91 (12 times Sol).`
Fix: `Around an index of 47 to 50: GPT-6.1 Sol at high costs $0.59, Opus 5.5 at medium $2.45 (4.2 times Sol), Gemini 4 Argon at high $3.84 (6.5 times Sol), Fable 5.1 at high $7.56 (12.8 times Sol).`
Basis: arithmetic on B2-1, B2-4, B2-5, B2-7.

**B2-15** (§5, "Where sources disagree")
Current: `**Where sources disagree.** Artificial Analysis's model page for Opus 5.5 gives $10.04 per task at max effort and names index v5.0 with nine evaluations ([model page](https://artificialanalysis.ai/models/claude-opus-5-5)); its leaderboard gives $5.98 for the same configuration ([leaderboard](https://artificialanalysis.ai/leaderboards/models)); its methodology page names v4.3.2 with ten evaluations ([methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)). This unit uses the leaderboard because it reports every model and effort level on one page, so the ratios above are at least internally consistent. The absolute dollar figures should be read as approximate.`
Fix: `**Where sources disagreed.** On 28 October 2026 Artificial Analysis's model page for Opus 5.5 gave $10.04 per task at max effort under index v5.0 with nine evaluations ([model page](https://artificialanalysis.ai/models/claude-opus-5-5)), while its leaderboard still gave $5.98 under the previous index ([leaderboard](https://artificialanalysis.ai/leaderboards/models)) and its methodology page named v4.3.2 with ten evaluations ([methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)). The disagreement was the changeover to Intelligence Index v5.0, announced on 27 October 2026 ([Artificial Analysis, *Announcing Intelligence Index v5*](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)); by 29 October all three pages carried v5.0, and the table above was updated to it in Audit 2. The v5.0 index drops GDPval-AA and adds private coding and science tests, so its scores are not comparable with the figures the unit cited on 28 October. The absolute dollar figures should still be read as approximate; the index will move again.`
Basis: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5; https://artificialanalysis.ai/methodology/intelligence-benchmarking (v5.0, nine evaluations, read 29 Oct 2026).

**B2-16** (§7, step costs)
Current: `Opus 5.5 from low to max costs 10.9 times as much per task for 16 more points; medium to high costs 36% more for 3 points; high to xhigh costs 1.9 times more for 2 points; xhigh to max 1.7 times more for 2 points. Sonnet 5.5 from low to max costs 15.6 times more`
Fix: `Opus 5.5 from low to max costs 10.2 times as much per task for 23 more points; medium to high costs 41% more for 4 points; high to xhigh costs 1.7 times more for 5 points; xhigh to max 1.7 times more for 1 point. Sonnet 5.5 from low to max costs 19.6 times more`
Basis: arithmetic on B2-1 and B2-2.

**B2-17** (§7, Claude Code diagram; FAIL)
Current: `The Claude Code post's diagram shows a high-effort path using roughly seven times the tokens of a low-effort one, but the post labels its curves illustrative ([Claude blog](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code)), so that figure is not evidence.`
Fix: `The Claude Code post's diagram caption says the high-effort path "generates roughly 7x more tokens" for one prompt; the post gives no measurement behind it, and the only visuals it labels illustrative are its two cost-curve charts ([Claude blog](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code)), so that figure is one unmeasured example, not evidence.`
Basis: https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code (caption: "Same prompt, two effort levels. The high effort path generates roughly 7x more tokens to reach a higher confidence answer."; the curve charts: "Curves are for illustration purposes only… They do not represent real benchmark data.").

**B2-18** (§8, default-effort gap)
Current: `Opus 5.5 at medium scores 51, Sonnet 5.5 at medium 41, and Sonnet needs max effort (56, at $5.46 a task) to come within two points of Opus at max`
Fix: `Opus 5.5 at medium scores 48, Sonnet 5.5 at medium 30, and Sonnet needs max effort (54, at $10.02 a task) to come within four points of Opus at max`
Basis: B2-1, B2-2.

**B2-19** (§8, AA-Omniscience)
Current: `Opus 5.5 has the highest overall index, 48, against 46 for Fable 5.1 and Gemini 4 Argon`
Fix: `Gemini 4 Carbon at high, listed by 29 October 2026, has the highest overall index, 54; Opus 5.5 has 48, against 46 for Fable 5.1 and Gemini 4 Argon`
Basis: https://artificialanalysis.ai/evaluations/omniscience, read 29 Oct 2026.

**B2-20** (Deliverable, Journal entries row)
Current: `about a third of Opus's per-task cost at medium (36%, §5)`
Fix: `about a third of Opus's per-task cost at medium (32%, §5)`
Basis: B2-1, B2-2 ($0.78 / $2.45).

**B2-21** (Deliverable, Course units row)
Current: `at default effort Opus leads Sonnet by 10 index points (third-party, §8); medium to high adds 3 points for 36% more cost per task (§7)`
Fix: `at default effort Opus leads Sonnet by 18 index points (third-party, §8); medium to high adds 4 points for 41% more cost per task (§7)`
Basis: B2-1, B2-2.

**B2-22** (Writer's unsure list, item 1)
Current: `1. **Artificial Analysis figures disagree with themselves.** The leaderboard gives Opus 5.5 at max $5.98 per task; the model page gives $10.04. The model page names index v5.0 with nine evaluations; the methodology page names v4.3.2 with ten. The meaning of "with fallback" in the model labels is not explained on the pages read. Every §5 and §7 ratio rests on the leaderboard.`
Fix: `1. **Artificial Analysis figures changed the day after writing.** On 28 October the leaderboard gave Opus 5.5 at max $5.98 per task and the model page $10.04; the gap was the changeover to Intelligence Index v5.0, and Audit 2 (29 October) replaced every §5, §7, §8 and deliverable figure with the v5.0 values. The meaning of "with fallback" in the model labels is not explained on the pages read. Every §5 and §7 ratio rests on the leaderboard as read on 29 October 2026.`
Basis: as B2-15.

**B2-23** (Writer's unsure list, item 2)
Current: `**Gemini 3.8 Flash at $3.49 per task, above Argon's $1.62,**`
Fix: `**Gemini 3.8 Flash at $7.77 per task, above Argon's $3.84,**`
Basis: B2-7, B2-8.

**B2-24** (Writer's unsure list, item 10)
Current: `its advice is general, and its seven-times token figure is labelled illustrative by its author.`
Fix: `its advice is general, and its seven-times token figure is a single diagram caption with no measurement behind it.`
Basis: as B2-17.

**B2-25** (Sources)
Current: `- Artificial Analysis. *LLM Leaderboard*. Accessed 28 October 2026 (vendor dataset). https://artificialanalysis.ai/leaderboards/models`
Fix: `- Artificial Analysis. *LLM Leaderboard*. Accessed 28 October 2026; figures re-read 29 October 2026 under Intelligence Index v5.0 (vendor dataset). https://artificialanalysis.ai/leaderboards/models
- Artificial Analysis. *Announcing Artificial Analysis Intelligence Index v5*. 27 October 2026. https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5`
Basis: the article URL above.

### B3 · Prompting that holds up

None.

### B4 · Context engineering

None.

### A1 · Positioning: the journey as a format

**A1-1** (§4, option 3; backlog P33)
Current: `Handles built on a full name are often free (my inference; not checked).`
Fix: `The handle is already his: @apcanario on YouTube and, per the episode descriptions, on Instagram (§6).`
Basis: `audits/brand-ai/evidence/A1-episodes-2026-10-29.md` (channel header and both descriptions, read 29 Oct 2026); https://www.youtube.com/watch?v=o5fitxW62Ng (channel "Pedro Canário", confirmed 29 Oct 2026).

---

Audit 2 summary: claims checked 96, FAIL 1, STALE 10, unverifiable 2; verdicts B2 PASS (errata B2-1 to B2-25), B3 PASS, B4 PASS, A1 PASS (erratum A1-1).
