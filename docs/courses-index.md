# Courses index

The live index: the courses in progress, the staleness dates and the courses to come; the finished courses' unit tables are in `docs/courses-index-archive.md` (P30-F17, 17 Nov 2026). Every course and every unit in the Learning Project, in build order, with status, the model that wrote it, the search flag and where the unit lives. State as of 30 October 2026 (User Experience family and course IA added 29 October, IA1 and IA2 written 30 October, IA3, IA4, IA5, IA6 and IA7 written 3 November, IA8, IA9 and IA10 9 November, IA11, IA12, DD-IA1, DD-IA2 and DD-IA3 10 November; Personal Mythology: end of the third Fable review session, plus the decisions of 28 October in `pm-status-2026-10-28.md` and `academy.md`, and A1 to A5 done: the site is Academy; Brand + AI v7.3, B2 filed, DD-B3 added, P27 figures in A2, A9, B2; Brand + AI v7.8 on 29 Oct 2026, Audit 2 run; v8.0, A3 filed; v8.1, B5 filed; v8.2, A4 filed; v8.5 to v8.7, A5, B7 and A7 filed 1–2 Nov 2026; v8.8 and v8.9, A8 and B6 filed 2 Nov 2026; v9.0, B8 filed 2 Nov 2026; v9.1, DD-A1 filed 2 Nov 2026; v9.2, DD-B1 filed 2 Nov 2026; v9.3, DD-A2 filed 2 Nov 2026, course A complete; v9.4, DD-B2 filed 3 Nov 2026, both courses complete; User Experience v5, 3 Nov 2026, the syllabus review S-1: aims and the dependency map on every brief, four briefs closed at their seams, the Perqo register; User Experience v6, 3 Nov 2026, IA3 filed; User Experience v7, 3 Nov 2026, IA4 filed; User Experience v8, 3 Nov 2026, IA5 filed; User Experience v9, 3 Nov 2026, IA6 filed; User Experience v10, 4 Nov 2026, IA7 filed; User Experience v11, 9 Nov 2026, IA8 filed; User Experience v12, 9 Nov 2026, IA9 filed; User Experience v13, 9 Nov 2026, IA10 filed; User Experience v14, 10 Nov 2026, IA11 filed; User Experience v15, 10 Nov 2026, IA12 filed; User Experience v16, 10 Nov 2026, DD-IA1 filed; User Experience v17, 10 Nov 2026, DD-IA2 filed; User Experience v18, 10 Nov 2026, DD-IA3 filed, the course's fifteen units written; Personal Brand (public) v2 and v3, 12 Nov 2026, PB1 and PB2 filed; Personal Brand v15, 15 Nov 2026, Audits 1 to 4 run). Update a row whenever a unit is filed or audited (method.md §7). `kit/index_check.py` checks every unit row, count line and staleness date against the syllabi, `kit/provenance.json`, the vault and the data files; `kit/verify.py` runs it. The notes, review rows and audit counters are not checked (the counters wait for S3).

Paths, all in the repo https://github.com/apcanario/learning: `kit/` is the Personal Mythology kit; `vault/` is `courses/`. Units not yet written show the vault path they will be filed at.

## Hubs

| Hub | Page | Link | Built from |
|---|---|---|---|
| Academy | The one site: the Academy home listing every course by track, with the Changelog and the Backlog; Greece and Rome in full (syllabi, every report); Brand + AI as two courses (A, B), each with its units, briefs, build order, bibliography and changelog; User Experience with its first course IA (coming soon, 29 Oct 2026); the eight history courses to come | https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH (version 55 onward, 28 Oct) · GitHub Pages: https://apcanario.github.io/academy/ (`kit/deploy.sh` through the public repo `apcanario/academy`) | kit `build.py` from `kit/courses.py` (`family` history or markdown; markdown through `kit/mdcourse.py`), `shell.css` = `design/theme.css`; A1, A3 and A2 of `academy.md` done 28 Oct: the build is `kit/academy/`, a shell plus one file per report fetched on navigation (sizes in `kit/README.md`); publish with `kit/publish_files.py` |

A5 done 28 Oct 2026: the Brand + AI units are read from the vault, `courses/brand-ai/` (no copy under `generator/`); a new course of either family is a folder plus a `kit/courses.py` entry (since S-DEC1, 20 Nov 2026: a folder whose `course.toml` is the entry; no existing file under `kit/` is edited (a history course adds its folder `kit/<id>/`)).

A4 done 28 Oct 2026: every course has a generated "How it was built" page (`#greece-built`, `#rome-built`, `#brand-a-built`, `#brand-b-built`; `kit/howbuilt.py`).

A3 done 28 Oct 2026: the Brand + AI courses are read in Academy (`#brand-a`, `#brand-b`; each unit at `#read-<code>`, the superseded research at `#read-audience-growth`), built by `kit/build.py` through `kit/mdcourse.py` from `vault/brand-ai/course.toml` (its `[pack]`, read by `kit/pack.py`). The Brand + AI hub artifact and the Audience Growth artifact are retired.

Retired 28 October 2026 (deleted): the standalone Hellas Syllabus and Roma Syllabus artifacts, and the three stray draft pages (r-3.2, r-3.3, r-11.6). The site's `#syllabus` and `#rome-syllabus` panels are the only published syllabi; `courses/greece/inputs/greek-syllabus.html` and `courses/rome/inputs/roman-syllabus.html` (in `kit/` until S-DEC5, 20 Nov 2026) remain as build inputs.

## Audits

The Fable stage is closed (S-NOAUDIT, 15 Nov 2026; Pedro): no further Fable audit or Fable fresh check of any course, and no audit counter. The audits that ran keep their rows in the tables below and their reports in `audits/` and `kit/audits/` as the record. Every new unit still gets its fresh check before filing (`method.md` §5), and every unit written with search on gets the staleness check six months after writing (`method.md` §6; the dates are in the staleness table).

## Staleness checks due (search-on units)

The checks of 16 May 2027 also re-read BW6's live-read product facts and DD-BW3's four export and session pages, though both units are search off (syllabus review BW-1, F51, F119).

| Unit | Written | Check due |
|---|---|---|
| A2 | 28 Oct 2026 (rewrite) | 28 Apr 2027 |
| A6 | 28 Oct 2026 (rewrite) | 28 Apr 2027 |
| A9 | 28 Oct 2026 (rewrite) | 28 Apr 2027 |
| B1 | 28 Oct 2026 (search on: Anthropic product facts) | 28 Apr 2027 |
| B2 | 28 Oct 2026 (search on: lineups, prices, plan rules, benchmarks) | 28 Apr 2027 |
| DD-B3 | 29 Oct 2026 (search on: practitioners' posts, repositories, papers) | 29 Apr 2027 |
| A8 | 2 Nov 2026 (search on: tax thresholds and rates, Segurança Social, consumer and advertising law, platform terms) | 2 May 2027 |
| B8 | 2 Nov 2026 (search on: plan limits, usage windows, prices, context windows, caching, retention, memory and Project behaviour) | 2 May 2027 |
| DD-A1 | 2 Nov 2026 (search on: creators' channel counts, dates, statements and income, from their own pages, trackers and the press) | 2 May 2027 |
| DD-IA1 | 10 Nov 2026 (search on: five products' public pages and their makers' documents, every observation dated) | 10 May 2027 |
| DD-IA2 | 10 Nov 2026 (search on: published figures on findability failure and its cost, each with its source, sample, date and label; US wage statistics) | 10 May 2027 |
| PB1 | 12 Nov 2026 (search on: YouTube and Instagram benchmarks, thresholds and the 2027 Partner Program change, vendor datasets, one equipment price) | 12 May 2027 |
| PB3 | 12 Nov 2026 (search on: platform-use surveys, the platforms' statements on discovery and reach, vendor reach, shelf-life and Shorts datasets, email benchmarks and one plan price) | 12 May 2027 |
| PB6 | 12 Nov 2026 (search on: YouTube's help pages and blog on recommendations, traffic sources, CTR, retention, Shorts, search and the 2027 Partner Program change; executive statements in the press; vendor datasets) | 12 May 2027 |
| PB7 | 12 Nov 2026 (search on: Instagram's ranking, creators and Meta pages, its head's statements in the press, the Instagram changes of 2025 and 2026, vendor datasets on reach and engagement by format) | 12 May 2027 |
| PB8 | 13 Nov 2026 (search on: YouTube's and Instagram's branded-content and copyright pages, the FTC, the CMA and ASA, the EU's consumer and data-protection texts, the ICO, the IPOs' search tools, tax pages of the EU, HMRC and the IRS, peer-reviewed work on disclosure and creator wellbeing) | 13 May 2027 |
| PB9 | 13 Nov 2026 (search on: YouTube's Partner Programme, Shopping and fan-funding pages, Instagram's and Meta's creator pages, affiliate, product, newsletter and payment platforms' fee pages, vendor and platform datasets on brand deals and paid conversion, the CMA and FTC, the EU's and UK's VAT pages, peer-reviewed work on disclosure and sponsorship load, CTT's tariff) | 13 May 2027 |
| DD-PB1 | 13 Nov 2026 (search on: creators' own sites, newsletters and channel pages, vidIQ and Social Blade-type trackers, Tubefilter, the press on six creators, Instagram's and YouTube's launch posts for Reels and Shorts) | 13 May 2027 |
| BW1 | 15 Nov 2026 (search on: Anthropic, OpenAI and Google help and API pages on context windows, memory, plans and prices; research papers; the model lineup) | 15 May 2027 |
| BW2 | 15 Nov 2026 (search on: Anthropic's models, effort, pricing, plan and help pages and launch posts; OpenAI's and Google's pricing and reasoning pages; Artificial Analysis's leaderboard and model pages; research papers; the model lineup and prices) | 15 May 2027 |
| BW5 | 15 Nov 2026 (search on: spec-driven practice and tool pages from Anthropic, GitHub, AWS Kiro, OpenAI and Google; research papers on spec-first agents and task length; design-doc, decision-record and changelog practice) | 15 May 2027 |
| BW9 | 16 Nov 2026 (search on: Claude Code's pages on how it works, permission modes, subagents, checkpointing, best practices, costs, security, skills and scheduled tasks; Anthropic's posts on its multi-agent research system, prompt-injection defences in browser use and how its teams use Claude Code; OpenAI's prompt-injection post and agent-building guide; Gemini CLI's subagents, sandboxing and checkpointing pages; METR's developer-productivity study and its 2026 update; Willison's and Karpathy's posts and Karpathy's keynote; Greshake et al. on indirect prompt injection) | 16 May 2027 |
| BW10 | 16 Nov 2026 (search on: Anthropic's pricing, usage-limit, Fable, usage-credit, context-window, research, memory, projects, incognito and sensitive-data help pages; its Privacy Center pages on retention, training and the model-improvement setting; its consumer-terms post of 2025 and memory post of 2026; Claude Code's pages on costs, prompt caching and scheduled tasks; the API's prompt-caching and Agent Skills pages; Anthropic's multi-agent research post; OpenAI's Data Controls FAQ and prompt-caching guide; Google's Gemini Apps privacy hub and limits page and the Gemini API's context-caching page) | 16 May 2027 |
| DD-BW1 | 16 Nov 2026 (search on: Karpathy's posts, talk transcription, interview, repositories and gist, read directly or through named reproductions (Willison's blog, Thread Reader App); the press on his move to Anthropic; Y Combinator's AI Startup School page; Anthropic's Building effective agents, Effective context engineering and the April 2025 Claude Code best-practices post; OpenAI's agent-building guide and GPT-4.1 prompting guide; Willison's posts and guides on vibe coding, agentic engineering, the lethal trifecta and labelling model-written pull requests; Mollick's post of 9 Nov 2026; the jagged-frontier paper and its Organization Science version; Autor et al.'s NBER paper; Reed's workflow, GitHub's Spec Kit post and Kiro's launch post; the chain-of-thought, self-consistency, ReAct and Sprague et al. papers; Claude Code's subagents page, OpenAI's reasoning page, Gemini's thinking page, Gemini CLI's GEMINI.md page and its subagents post) | 16 May 2027 |
| SP9 | 18 Nov 2026 (search on: the IOC consensus statement on mental health in elite athletes, its Mental Health in Elite Athletes Toolkit and the Sport Mental Health Recognition Tool 1 (read on the ISSF's page; the tool's PDF and the consensus's Table 4 to be tried again); the coach-role Delphi and FEPSAC's position statements; the sleep, REDs and sport-injury consensus statements; the youth-athlete prevalence, risk-factor, perfectionism and coach-wellbeing reviews and the Gouttebarge et al. (2019) meta-analysis; NSPCC Sport's and the U.S. Center for SafeSport's codes; Sport Integrity Australia's page on ADHD medication and WADA's Prohibited List) | 18 May 2027 |
| DD-SP1 | 19 Nov 2026 (search on: the IOC consensus statements on harassment and abuse (2016) and on interpersonal violence and safeguarding (2024, read on the IOC's copy); NSPCC Sport's pages on concerns, contact, changing facilities, online safety, positions of trust, grooming, overnight trips and the reporting law; the UK Home Office factsheet on the Crime and Policing Act 2026; the U.S. Center for SafeSport's 2025 MAAPP; Sport Integrity Australia's reporting page and Abuse-Free Sport's page; prevalence, coach-abuse, bullying and safeguarding-progress studies) | 19 May 2027 |
| DD-SP2 | 19 Nov 2026 (search on: the Female Athlete Triad Coalition's 2025 consensus update and the IOC's REDs consensus statement; systematic reviews of weight cycling in youth combat sports, of body image and eating disorders in athletes, of weight control in young elite athletes, of maturity prediction in youth football, of REDs biomarkers and of maturation and fitness; narrative and clinical reviews on weight cycling, eating disorders in athletes, muscularity-oriented disordered eating, gymnasts' growth and body dysmorphic disorder; primary studies of coach and parent weight pressure, rapid weight loss, eating-disorder risk and muscle dysmorphia; the weigh-in and weight rules of United World Wrestling, British Taekwondo, the Irish Judo Association and World Rowing, each dated on its own page) | 19 May 2027 |
| SCE1 | 21 Nov 2026 (search on: Gartner's supply chain execution glossary entry, Magic Quadrant index (its Distributed Order Management row, held finding f4, to be re-opened), DOM Magic Quadrant abstract, 2024 methodology note, Magic Quadrant FAQ, Ombuds and independence pages, and Peer Insights market and review-sourcing pages; Forrester's Wave methodology and citation guidelines; MIT FreightLab; the CMR Convention and FAR 47.001; the MHI and Deloitte 2026 report announcement; to try again: Gartner's Magic Quadrant method, content compliance and ERP glossary pages) | 21 May 2027 |

## Finished courses

The unit tables of the finished courses (Brand + AI, User Experience, Personal Brand, Building with AI, Sport Psychology, and Personal Mythology's Greece and Rome) are in `docs/courses-index-archive.md` since 17 Nov 2026 (P30-F17). `kit/index_check.py` checks both files as one index, `kit/thin.py` reads both and writes a row where it finds it, and their staleness dates stay in the table above. A REWRITE verdict on any unit, archived or not, is recorded in the Staleness section of this file, so the rewrite gate is read here alone.

## Supply Chain Execution (public)

The public course **SCE · Supply Chain Execution for Product Teams**, created 19 Nov 2026 (row S-SCE0; syllabus drafted the same day on Fable 5.2, `docs/supply-chain-execution-syllabus.md`): written for someone who builds, sells or implements order, warehouse or transport software, or is moving into that work, with no operations background, an exception to the single-reader rule; the reader is the persona in each brief's preamble. Adapted from nothing: no source units; a seed bibliography of 41 references, 37 checked for existence only (3 seen only secondhand, 1 not opened) (`vault/supply-chain-execution/notes/bibliography.md`). The running case is three fictional operations, Corvane, Ostrel Foods and Tandric Logistics, and three fictional vendors, Halvern Systems, Varnby Software and Kestrow (`vault/supply-chain-execution/notes/case-facts.md`). Eighteen core units in an opening and three parts, and two deep dives, in the Supply Chain track, the first of its courses. 2 of 20 written. A unit is written when its file is in `courses/supply-chain-execution/` (the folder appears with the first one). Briefs: the course's Briefs page in Academy (`vault/supply-chain-execution/briefs.md`, with the Aim lines in `vault/supply-chain-execution/course.toml`). Build order: the Build order page, in syllabus order, with a gate after SCE6 (row P-SCE6); search on for SCE1, SCE6, SCE8, SCE9, SCE11, SCE12, SCE16, SCE17 and DD-SCE1. Sourcing: `docs/sourcing-standard.md` Parts 1 and 8. Syllabus flags: `vault/supply-chain-execution/notes/syllabus-flags.md`. Decisions: `docs/public-courses.md`. Prompts: `docs/supply-chain-execution-prompts.md`, printed by `kit/next_prompt.py`. Fresh checks: `audits/supply-chain-execution/`.

| # | Unit | Course | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | SCE1 | SCE | The map, the words and the evidence | written 21 Nov 2026 (W-SCE1; fresh check `audits/supply-chain-execution/fresh-check-SCE1.md`, fix: 28 edits applied, 2 held) | Opus 5.5 | on | `courses/supply-chain-execution/SCE1-the-map-the-words-and-the-evidence.md` |
| 2 | SCE2 | SCE | Inbound and storage | written 21 Nov 2026 (W-SCE2; fresh check `audits/supply-chain-execution/fresh-check-SCE2.md`, fix: 27 edits applied, 0 held) | Opus 5.5 | off | `courses/supply-chain-execution/SCE2-inbound-and-storage.md` |
| 3 | SCE3 | SCE | Outbound: release, pick, pack, ship | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE3-outbound-release-pick-pack-ship.md` |
| 4 | SCE4 | SCE | Inventory and control | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE4-inventory-and-control.md` |
| 5 | SCE5 | SCE | The floor: people, devices and machines | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE5-the-floor-people-devices-and-machines.md` |
| 6 | SCE6 | SCE | The warehouse system as a product | not written | Opus 5.5 | on | `courses/supply-chain-execution/SCE6-the-warehouse-system-as-a-product.md` |
| 7 | SCE7 | SCE | Transportation in practice | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE7-transportation-in-practice.md` |
| 8 | SCE8 | SCE | The transport system as a product | not written | Opus 5.5 | on | `courses/supply-chain-execution/SCE8-the-transport-system-as-a-product.md` |
| 9 | SCE9 | SCE | Order management | not written | Opus 5.5 | on | `courses/supply-chain-execution/SCE9-order-management.md` |
| 10 | SCE10 | SCE | The seams | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE10-the-seams.md` |
| 11 | SCE11 | SCE | The buying committee | not written | Opus 5.5 | on | `courses/supply-chain-execution/SCE11-the-buying-committee.md` |
| 12 | SCE12 | SCE | The sale | not written | Opus 5.5 | on | `courses/supply-chain-execution/SCE12-the-sale.md` |
| 13 | SCE13 | SCE | Users by role | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE13-users-by-role.md` |
| 14 | SCE14 | SCE | Implementers and administrators | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE14-implementers-and-administrators.md` |
| 15 | SCE15 | SCE | Demo versus shift | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE15-demo-versus-shift.md` |
| 16 | SCE16 | SCE | Money | not written | Opus 5.5 | on | `courses/supply-chain-execution/SCE16-money.md` |
| 17 | SCE17 | SCE | Reading the field | not written | Opus 5.5 | on | `courses/supply-chain-execution/SCE17-reading-the-field.md` |
| 18 | SCE18 | SCE | Capstone: one strategy memo | not written | Opus 5.5 | off | `courses/supply-chain-execution/SCE18-capstone-one-strategy-memo.md` |
| 19 | DD-SCE1 | SCE | Deep dive: the logistics provider's business | not written | Opus 5.5 | on | `courses/supply-chain-execution/DD-SCE1-deep-dive-the-logistics-providers-business.md` |
| 20 | DD-SCE2 | SCE | Deep dive: peak and exceptions | not written | Opus 5.5 | off | `courses/supply-chain-execution/DD-SCE2-deep-dive-peak-and-exceptions.md` |

## Supply Chain Planning (public)

The public course **SCP · Supply Chain Planning for Product Teams**, created 22 Nov 2026 (row S-SCP0; syllabus designed 21 Nov 2026 on Fable 5.2, `docs/supply-chain-planning-syllabus.md`): written for someone who builds, sells or implements planning software with no planning background, an exception to the single-reader rule; the reader is the persona in each brief's preamble. Adapted from nothing: no source units; a seed bibliography of 46 references, 43 checked for existence only, R3 in part, 2 not opened (`vault/supply-chain-planning/notes/bibliography.md`). The running case is three fictional companies, Corvane, Ostrel Foods and Pellward, and three fictional vendors, Lathmoor, Ebbfield and Varnby Software (`vault/supply-chain-planning/notes/case-facts.md`). Sixteen core units in an opening and four parts, and two deep dives, in the Supply Chain track, the second of its courses. 0 of 18 written. A unit is written when its file is in `courses/supply-chain-planning/`. Briefs: the course's Briefs page in Academy (`vault/supply-chain-planning/briefs.md`, with the Aim lines in `vault/supply-chain-planning/course.toml`). Build order: the Build order page, in syllabus order (SCP1 to SCP16, then DD-SCP1 and DD-SCP2), with no gate; search on for SCP1, SCP13, SCP15, DD-SCP1 and DD-SCP2. Sourcing: `docs/sourcing-standard.md` Parts 1 and 9. Syllabus flags: `vault/supply-chain-planning/notes/syllabus-flags.md`. Decisions: the syllabus's §8 and `docs/public-courses.md`. Prompts: `docs/supply-chain-planning-prompts.md`, printed by `kit/next_prompt.py`. Fresh checks: `audits/supply-chain-planning/`.

| # | Unit | Course | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | SCP1 | SCP | The planning map, the words and the evidence | not written | Opus 5.5 | on | `courses/supply-chain-planning/SCP1-the-planning-map-the-words-and-the-evidence.md` |
| 2 | SCP2 | SCP | Demand and its data | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP2-demand-and-its-data.md` |
| 3 | SCP3 | SCP | Forecasting methods | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP3-forecasting-methods.md` |
| 4 | SCP4 | SCP | Forecast error and what it is used for | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP4-forecast-error-and-what-it-is-used-for.md` |
| 5 | SCP5 | SCP | Judgment, overrides and the demand planner | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP5-judgment-overrides-and-the-demand-planner.md` |
| 6 | SCP6 | SCP | Why inventory exists and how much | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP6-why-inventory-exists-and-how-much.md` |
| 7 | SCP7 | SCP | Replenishment | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP7-replenishment.md` |
| 8 | SCP8 | SCP | The network: stock in more than one place | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP8-the-network-stock-in-more-than-one-place.md` |
| 9 | SCP9 | SCP | Supply planning for makers | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP9-supply-planning-for-makers.md` |
| 10 | SCP10 | SCP | Retail and distribution planning | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP10-retail-and-distribution-planning.md` |
| 11 | SCP11 | SCP | Sales and operations planning | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP11-sales-and-operations-planning.md` |
| 12 | SCP12 | SCP | Where the plan meets execution | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP12-where-the-plan-meets-execution.md` |
| 13 | SCP13 | SCP | The planning system as a product | not written | Opus 5.5 | on | `courses/supply-chain-planning/SCP13-the-planning-system-as-a-product.md` |
| 14 | SCP14 | SCP | Planners as users | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP14-planners-as-users.md` |
| 15 | SCP15 | SCP | Buying planning software: what differs | not written | Opus 5.5 | on | `courses/supply-chain-planning/SCP15-buying-planning-software-what-differs.md` |
| 16 | SCP16 | SCP | Capstone: one planning product memo | not written | Opus 5.5 | off | `courses/supply-chain-planning/SCP16-capstone-one-planning-product-memo.md` |
| 17 | DD-SCP1 | SCP | Deep dive: planning as companies have published it | not written | Opus 5.5 | on | `courses/supply-chain-planning/DD-SCP1-deep-dive-planning-as-companies-have-published-it.md` |
| 18 | DD-SCP2 | SCP | Deep dive: the hard numbers | not written | Opus 5.5 | on | `courses/supply-chain-planning/DD-SCP2-deep-dive-the-hard-numbers.md` |

## AI in Supply Chain Execution (public)

The public course **AIE · AI in Supply Chain Execution**, created 23 Nov 2026 (row S-AIE0; syllabus designed 21 Nov 2026 on Fable 5.2, `docs/ai-in-supply-chain-execution-syllabus.md`): written for someone who builds, sells or implements order, warehouse or transport software and knows the ground of Supply Chain Execution for Product Teams, an exception to the single-reader rule; the reader is the persona in each brief's preamble. Adapted from nothing: no source units; a seed bibliography of 72 references, checked for existence only (of the 72 entries, checked in full (Crossref record read, or entry's own record/page read): 37 Crossref + 14 page read = 51, plus 11 carried from the first course's seed list (checked there on 19 Nov 2026, not re-read here); checked in part (search listing or a page that did not give the record): 9 (not counted as checked); not opened: 1. Leads, not found: 0; `vault/ai-in-supply-chain-execution/notes/bibliography.md`). The running case is the track's: three fictional operations, Corvane, Ostrel Foods and Tandric Logistics, and three fictional vendors, Halvern Systems, Varnby Software and Kestrow, with fictional AI features and six fictional claims (`vault/ai-in-supply-chain-execution/notes/case-facts.md`). Thirteen core units in an opening and three parts, and one deep dive, in the Supply Chain track, the third of its courses. 0 of 14 written. A unit is written when its file is in `courses/ai-in-supply-chain-execution/`. Briefs: the course's Briefs page in Academy (`vault/ai-in-supply-chain-execution/briefs.md`, with the Aim lines in `vault/ai-in-supply-chain-execution/course.toml`). Build order: the Build order page, in syllabus order (AIE1 to AIE13, then DD-AIE1), with no gate; search on for AIE1, AIE4, AIE10, AIE11, AIE12 and DD-AIE1. Sourcing: `docs/sourcing-standard.md` Parts 1 and 10. Syllabus flags: `vault/ai-in-supply-chain-execution/notes/syllabus-flags.md`. Decisions: the syllabus's §8 and `docs/public-courses.md`. Prompts: `docs/ai-in-supply-chain-execution-prompts.md`, printed by `kit/next_prompt.py`, in four bundles of up to four units. Fresh checks: `audits/ai-in-supply-chain-execution/`.

| # | Unit | Course | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | AIE1 | AIE | What counts as AI here | not written | Opus 5.5 | on | `courses/ai-in-supply-chain-execution/AIE1-what-counts-as-ai-here.md` |
| 2 | AIE2 | AIE | Optimisation and rules: the AI that was already there | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE2-optimisation-and-rules-the-ai-that-was-already-there.md` |
| 3 | AIE3 | AIE | Prediction: what machine learning adds | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE3-prediction-what-machine-learning-adds.md` |
| 4 | AIE4 | AIE | Generative models and agents | not written | Opus 5.5 | on | `courses/ai-in-supply-chain-execution/AIE4-generative-models-and-agents.md` |
| 5 | AIE5 | AIE | The field evidence, read in full | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE5-the-field-evidence-read-in-full.md` |
| 6 | AIE6 | AIE | In the warehouse | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE6-in-the-warehouse.md` |
| 7 | AIE7 | AIE | In transport | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE7-in-transport.md` |
| 8 | AIE8 | AIE | In order management | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE8-in-order-management.md` |
| 9 | AIE9 | AIE | The person in the loop | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE9-the-person-in-the-loop.md` |
| 10 | AIE10 | AIE | Risk, rules and accountability | not written | Opus 5.5 | on | `courses/ai-in-supply-chain-execution/AIE10-risk-rules-and-accountability.md` |
| 11 | AIE11 | AIE | Reading an AI claim | not written | Opus 5.5 | on | `courses/ai-in-supply-chain-execution/AIE11-reading-an-ai-claim.md` |
| 12 | AIE12 | AIE | Money and the pilot | not written | Opus 5.5 | on | `courses/ai-in-supply-chain-execution/AIE12-money-and-the-pilot.md` |
| 13 | AIE13 | AIE | Capstone: one feature, argued | not written | Opus 5.5 | off | `courses/ai-in-supply-chain-execution/AIE13-capstone-one-feature-argued.md` |
| 14 | DD-AIE1 | AIE | Deep dive: algorithmic management on the floor | not written | Opus 5.5 | on | `courses/ai-in-supply-chain-execution/DD-AIE1-deep-dive-algorithmic-management-on-the-floor.md` |

## Managing an Athlete's Career (public)

The public course **AC · Managing an Athlete's Career**, created 23 Nov 2026 (row S-AC0; syllabus designed 21 Nov 2026 on Fable 5.2, `docs/athlete-career-syllabus.md`): written for a coach of an athlete in an Olympic or federation sport, below the agency level, who also sponsors the athlete through a business of their own, helps them unpaid as representative, or both, an exception to the single-reader rule; the reader is the persona in each brief's preamble. Adapted from nothing: no source units; a seed bibliography of 38 references, checked for existence only (of the 38 entries, checked in full 19; checked in part 17 (not counted as checked); not opened 2; `vault/athlete-career/notes/bibliography.md`). The running case is Sport Psychology for Coaches' three athletes, Sara, Dani and Milan, with their coaches and a commercial layer: fictional sponsors, clubs and agents, and two coaches' small labels (`vault/athlete-career/notes/case-facts.md`, which agrees with that course's register). Fifteen core units in five parts, and three deep dives, in the Sports track, the second of its courses. 0 of 18 written. A unit is written when its file is in `courses/athlete-career/`. Briefs: the course's Briefs page in Academy (`vault/athlete-career/briefs.md`, with the Aim lines in `vault/athlete-career/course.toml`). Build order: the Build order page, in writing order (AC1 to AC15, then DD-AC2, DD-AC1 and DD-AC3), with no gate; search on for every unit but AC6, AC7, AC10 and AC15. Sourcing: `docs/sourcing-standard.md` Parts 1 and 11. Syllabus flags: `vault/athlete-career/notes/syllabus-flags.md`. Decisions: the syllabus's §8 and `docs/public-courses.md`. Prompts: `docs/athlete-career-prompts.md`, printed by `kit/next_prompt.py`, in five bundles of up to four units. Fresh checks: `audits/athlete-career/`.

| # | Unit | Course | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | AC1 | AC | The job, the map and the evidence | not written | Opus 5.5 | on | `courses/athlete-career/AC1-the-job-the-map-and-the-evidence.md` |
| 2 | AC2 | AC | Three hats: coach, sponsor, representative | not written | Opus 5.5 | on | `courses/athlete-career/AC2-three-hats-coach-sponsor-representative.md` |
| 3 | AC3 | AC | The rules that bind what an athlete may sell | not written | Opus 5.5 | on | `courses/athlete-career/AC3-the-rules-that-bind-what-an-athlete-may-sell.md` |
| 4 | AC4 | AC | The minor first | not written | Opus 5.5 | on | `courses/athlete-career/AC4-the-minor-first.md` |
| 5 | AC5 | AC | Funding and the season's money | not written | Opus 5.5 | on | `courses/athlete-career/AC5-funding-and-the-seasons-money.md` |
| 6 | AC6 | AC | What the athlete has to sell | not written | Opus 5.5 | off | `courses/athlete-career/AC6-what-the-athlete-has-to-sell.md` |
| 7 | AC7 | AC | Building marketability without building a persona | not written | Opus 5.5 | off | `courses/athlete-career/AC7-building-marketability-without-building-a-persona.md` |
| 8 | AC8 | AC | What a sponsor buys | not written | Opus 5.5 | on | `courses/athlete-career/AC8-what-a-sponsor-buys.md` |
| 9 | AC9 | AC | Being the sponsor: a small brand's athlete programme | not written | Opus 5.5 | on | `courses/athlete-career/AC9-being-the-sponsor-a-small-brands-athlete-programme.md` |
| 10 | AC10 | AC | Finding other sponsors for the athlete | not written | Opus 5.5 | off | `courses/athlete-career/AC10-finding-other-sponsors-for-the-athlete.md` |
| 11 | AC11 | AC | Closing and keeping a sponsor | not written | Opus 5.5 | on | `courses/athlete-career/AC11-closing-and-keeping-a-sponsor.md` |
| 12 | AC12 | AC | Contracts and image rights as questions | not written | Opus 5.5 | on | `courses/athlete-career/AC12-contracts-and-image-rights-as-questions.md` |
| 13 | AC13 | AC | Agents: the profession, the handover, and where your help stops | not written | Opus 5.5 | on | `courses/athlete-career/AC13-agents-the-profession-the-handover-and-where-your-help-stops.md` |
| 14 | AC14 | AC | The career alongside and after sport | not written | Opus 5.5 | on | `courses/athlete-career/AC14-the-career-alongside-and-after-sport.md` |
| 15 | AC15 | AC | Capstone: the one-year career plan | not written | Opus 5.5 | off | `courses/athlete-career/AC15-capstone-the-one-year-career-plan.md` |
| 16 | DD-AC2 | AC | Deep dive: hard numbers, what the money is | not written | Opus 5.5 | on | `courses/athlete-career/DD-AC2-deep-dive-hard-numbers-what-the-money-is.md` |
| 17 | DD-AC1 | AC | Deep dive: comparables, documented careers below the agency level | not written | Opus 5.5 | on | `courses/athlete-career/DD-AC1-deep-dive-comparables-documented-careers-below-the-agency-level.md` |
| 18 | DD-AC3 | AC | Deep dive: Portugal, end to end | not written | Opus 5.5 | on | `courses/athlete-career/DD-AC3-deep-dive-portugal-end-to-end.md` |

## Egypt

The private course **EG · Egyptian history and mythology**, created 23 Nov 2026 (row S-EG0; syllabus designed 21 Nov 2026 on Fable 5.2, `docs/egypt-syllabus.md`): the third course of Personal Mythology, after Greece and Rome, read by the Project's own reader (`docs/reader.md`), on the History track. A markdown course (P71; syllabus decision D6), not the history family's form: its modules are EG1 to EG57 and DD-EG1 to DD-EG21 (decision D7), filed as `courses/egypt/<code>-<slug>.md`, in Personal Mythology's module anatomy (`kit/AGENT-SPEC.md`, its Egypt section). Written under the source-credibility floor (`docs/method.md` §9): no source units; a seed bibliography of 70 references, checked for existence only (of the 70 entries, checked in full 30; checked in part 40 (not counted as checked); not opened 0; struck 0; `vault/egypt/notes/bibliography.md`); no case register. Fifty-seven core modules in twelve syllabus units, and three deep dives of seven (the pyramids, Amarna, the afterlife books). 0 of 78 written. A module is written when its file is in `courses/egypt/`. Briefs: the course's Briefs page in Academy (`vault/egypt/briefs.md`, with the Takes lines in `vault/egypt/course.toml`). Build order: the Build order page, in code order (EG1 to EG57, then DD-EG1 to DD-EG21), with no gate; the search flag means a staleness check is owed, on for EG18, EG46, EG55, EG56 and DD-EG5. Sourcing: `docs/sourcing-standard.md` Parts 1 and 12. Syllabus flags: `vault/egypt/notes/syllabus-flags.md`. Decisions: the syllabus's §8. Prompts: `docs/egypt-prompts.md`, printed by `kit/next_prompt.py`, in twenty bundles of up to four modules. Fresh checks: `audits/egypt/`.

| # | Unit | Course | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | EG1 | EG | How we know anything: the sources and the evidence key | not written | Opus 5.5 | off | `courses/egypt/EG1-how-we-know-anything-the-sources-and-the-evidence-key.md` |
| 2 | EG2 | EG | The land: river, flood, desert and neighbours | not written | Opus 5.5 | off | `courses/egypt/EG2-the-land-river-flood-desert-and-neighbours.md` |
| 3 | EG3 | EG | The timeline spine and how the dates are made | not written | Opus 5.5 | off | `courses/egypt/EG3-the-timeline-spine-and-how-the-dates-are-made.md` |
| 4 | EG4 | EG | Predynastic Egypt | not written | Opus 5.5 | off | `courses/egypt/EG4-predynastic-egypt.md` |
| 5 | EG5 | EG | Unification and Narmer | not written | Opus 5.5 | off | `courses/egypt/EG5-unification-and-narmer.md` |
| 6 | EG6 | EG | The first two dynasties | not written | Opus 5.5 | off | `courses/egypt/EG6-the-first-two-dynasties.md` |
| 7 | EG7 | EG | Kingship: the idea that held three thousand years | not written | Opus 5.5 | off | `courses/egypt/EG7-kingship-the-idea-that-held-three-thousand-years.md` |
| 8 | EG8 | EG | Djoser and the Third Dynasty | not written | Opus 5.5 | off | `courses/egypt/EG8-djoser-and-the-third-dynasty.md` |
| 9 | EG9 | EG | The Fourth Dynasty: Sneferu to Menkaure | not written | Opus 5.5 | off | `courses/egypt/EG9-the-fourth-dynasty-sneferu-to-menkaure.md` |
| 10 | EG10 | EG | The Fifth and Sixth Dynasties | not written | Opus 5.5 | off | `courses/egypt/EG10-the-fifth-and-sixth-dynasties.md` |
| 11 | EG11 | EG | How the Old Kingdom worked | not written | Opus 5.5 | off | `courses/egypt/EG11-how-the-old-kingdom-worked.md` |
| 12 | EG12 | EG | The end of the Old Kingdom and the First Intermediate Period | not written | Opus 5.5 | off | `courses/egypt/EG12-the-end-of-the-old-kingdom-and-the-first-intermediate-period.md` |
| 13 | EG13 | EG | Reunification and the Twelfth Dynasty | not written | Opus 5.5 | off | `courses/egypt/EG13-reunification-and-the-twelfth-dynasty.md` |
| 14 | EG14 | EG | The Middle Kingdom state: forts, towns and foreigners | not written | Opus 5.5 | off | `courses/egypt/EG14-the-middle-kingdom-state-forts-towns-and-foreigners.md` |
| 15 | EG15 | EG | The classical literature | not written | Opus 5.5 | off | `courses/egypt/EG15-the-classical-literature.md` |
| 16 | EG16 | EG | The Second Intermediate Period | not written | Opus 5.5 | off | `courses/egypt/EG16-the-second-intermediate-period.md` |
| 17 | EG17 | EG | Ahmose and the making of the New Kingdom | not written | Opus 5.5 | off | `courses/egypt/EG17-ahmose-and-the-making-of-the-new-kingdom.md` |
| 18 | EG18 | EG | Hatshepsut | not written | Opus 5.5 | on | `courses/egypt/EG18-hatshepsut.md` |
| 19 | EG19 | EG | Thutmose III and the empire | not written | Opus 5.5 | off | `courses/egypt/EG19-thutmose-iii-and-the-empire.md` |
| 20 | EG20 | EG | Amenhotep III: Egypt at its height | not written | Opus 5.5 | off | `courses/egypt/EG20-amenhotep-iii-egypt-at-its-height.md` |
| 21 | EG21 | EG | Akhenaten to Horemheb: the core account | not written | Opus 5.5 | off | `courses/egypt/EG21-akhenaten-to-horemheb-the-core-account.md` |
| 22 | EG22 | EG | Seti I and Ramesses II | not written | Opus 5.5 | off | `courses/egypt/EG22-seti-i-and-ramesses-ii.md` |
| 23 | EG23 | EG | Merneptah, the Libyans and the Exodus question | not written | Opus 5.5 | off | `courses/egypt/EG23-merneptah-the-libyans-and-the-exodus-question.md` |
| 24 | EG24 | EG | Ramesses III and the Sea Peoples | not written | Opus 5.5 | off | `courses/egypt/EG24-ramesses-iii-and-the-sea-peoples.md` |
| 25 | EG25 | EG | Deir el-Medina | not written | Opus 5.5 | off | `courses/egypt/EG25-deir-el-medina.md` |
| 26 | EG26 | EG | The end of the New Kingdom | not written | Opus 5.5 | off | `courses/egypt/EG26-the-end-of-the-new-kingdom.md` |
| 27 | EG27 | EG | The Third Intermediate Period | not written | Opus 5.5 | off | `courses/egypt/EG27-the-third-intermediate-period.md` |
| 28 | EG28 | EG | Kush and the Twenty-fifth Dynasty | not written | Opus 5.5 | off | `courses/egypt/EG28-kush-and-the-twenty-fifth-dynasty.md` |
| 29 | EG29 | EG | The Saite renaissance | not written | Opus 5.5 | off | `courses/egypt/EG29-the-saite-renaissance.md` |
| 30 | EG30 | EG | Persian Egypt and the last native kings | not written | Opus 5.5 | off | `courses/egypt/EG30-persian-egypt-and-the-last-native-kings.md` |
| 31 | EG31 | EG | Herodotus in Egypt: Book 2 as a source | not written | Opus 5.5 | off | `courses/egypt/EG31-herodotus-in-egypt-book-2-as-a-source.md` |
| 32 | EG32 | EG | The Ptolemies from the Egyptian side | not written | Opus 5.5 | off | `courses/egypt/EG32-the-ptolemies-from-the-egyptian-side.md` |
| 33 | EG33 | EG | Two cultures in one country | not written | Opus 5.5 | off | `courses/egypt/EG33-two-cultures-in-one-country.md` |
| 34 | EG34 | EG | Cleopatra VII and the Roman conquest | not written | Opus 5.5 | off | `courses/egypt/EG34-cleopatra-vii-and-the-roman-conquest.md` |
| 35 | EG35 | EG | Roman Egypt and the end of the old religion | not written | Opus 5.5 | off | `courses/egypt/EG35-roman-egypt-and-the-end-of-the-old-religion.md` |
| 36 | EG36 | EG | What Egyptian religion was | not written | Opus 5.5 | off | `courses/egypt/EG36-what-egyptian-religion-was.md` |
| 37 | EG37 | EG | The cosmogonies | not written | Opus 5.5 | off | `courses/egypt/EG37-the-cosmogonies.md` |
| 38 | EG38 | EG | The gods: a field guide | not written | Opus 5.5 | off | `courses/egypt/EG38-the-gods-a-field-guide.md` |
| 39 | EG39 | EG | Osiris, Isis, Seth and Horus | not written | Opus 5.5 | off | `courses/egypt/EG39-osiris-isis-seth-and-horus.md` |
| 40 | EG40 | EG | The sun's journey and the myths of Re | not written | Opus 5.5 | off | `courses/egypt/EG40-the-suns-journey-and-the-myths-of-re.md` |
| 41 | EG41 | EG | Ma'at | not written | Opus 5.5 | off | `courses/egypt/EG41-maat.md` |
| 42 | EG42 | EG | The person and the dead | not written | Opus 5.5 | off | `courses/egypt/EG42-the-person-and-the-dead.md` |
| 43 | EG43 | EG | Mummification | not written | Opus 5.5 | off | `courses/egypt/EG43-mummification.md` |
| 44 | EG44 | EG | The afterlife: judgement and the Field of Reeds | not written | Opus 5.5 | off | `courses/egypt/EG44-the-afterlife-judgement-and-the-field-of-reeds.md` |
| 45 | EG45 | EG | Tombs | not written | Opus 5.5 | off | `courses/egypt/EG45-tombs.md` |
| 46 | EG46 | EG | Tutankhamun's tomb | not written | Opus 5.5 | on | `courses/egypt/EG46-tutankhamuns-tomb.md` |
| 47 | EG47 | EG | The temple: the house of the god | not written | Opus 5.5 | off | `courses/egypt/EG47-the-temple-the-house-of-the-god.md` |
| 48 | EG48 | EG | Priests and the god's estate | not written | Opus 5.5 | off | `courses/egypt/EG48-priests-and-the-gods-estate.md` |
| 49 | EG49 | EG | Personal religion and magic | not written | Opus 5.5 | off | `courses/egypt/EG49-personal-religion-and-magic.md` |
| 50 | EG50 | EG | Family, women, law and work | not written | Opus 5.5 | off | `courses/egypt/EG50-family-women-law-and-work.md` |
| 51 | EG51 | EG | Grain, beer and the economy | not written | Opus 5.5 | off | `courses/egypt/EG51-grain-beer-and-the-economy.md` |
| 52 | EG52 | EG | Number, sky and body: Egyptian knowledge | not written | Opus 5.5 | off | `courses/egypt/EG52-number-sky-and-body-egyptian-knowledge.md` |
| 53 | EG53 | EG | The scripts and the decipherment | not written | Opus 5.5 | off | `courses/egypt/EG53-the-scripts-and-the-decipherment.md` |
| 54 | EG54 | EG | Reading a cartouche | not written | Opus 5.5 | off | `courses/egypt/EG54-reading-a-cartouche.md` |
| 55 | EG55 | EG | Reading Egyptian art, a site and a museum | not written | Opus 5.5 | on | `courses/egypt/EG55-reading-egyptian-art-a-site-and-a-museum.md` |
| 56 | EG56 | EG | Reception: how Egypt reached you | not written | Opus 5.5 | on | `courses/egypt/EG56-reception-how-egypt-reached-you.md` |
| 57 | EG57 | EG | Capstone: the whole thing in one sitting | not written | Opus 5.5 | off | `courses/egypt/EG57-capstone-the-whole-thing-in-one-sitting.md` |
| 58 | DD-EG1 | EG | From mastaba to true pyramid | not written | Opus 5.5 | off | `courses/egypt/DD-EG1-from-mastaba-to-true-pyramid.md` |
| 59 | DD-EG2 | EG | Quarry, river and harbour | not written | Opus 5.5 | off | `courses/egypt/DD-EG2-quarry-river-and-harbour.md` |
| 60 | DD-EG3 | EG | Raising the stone: ramps and their rivals | not written | Opus 5.5 | off | `courses/egypt/DD-EG3-raising-the-stone-ramps-and-their-rivals.md` |
| 61 | DD-EG4 | EG | Who built them: the workers' town | not written | Opus 5.5 | off | `courses/egypt/DD-EG4-who-built-them-the-workers-town.md` |
| 62 | DD-EG5 | EG | Inside the Great Pyramid | not written | Opus 5.5 | on | `courses/egypt/DD-EG5-inside-the-great-pyramid.md` |
| 63 | DD-EG6 | EG | The complex and its meaning | not written | Opus 5.5 | off | `courses/egypt/DD-EG6-the-complex-and-its-meaning.md` |
| 64 | DD-EG7 | EG | After Giza, and what is still unknown | not written | Opus 5.5 | off | `courses/egypt/DD-EG7-after-giza-and-what-is-still-unknown.md` |
| 65 | DD-EG8 | EG | Before the break: Amenhotep III and the sun | not written | Opus 5.5 | off | `courses/egypt/DD-EG8-before-the-break-amenhotep-iii-and-the-sun.md` |
| 66 | DD-EG9 | EG | The revolution year by year | not written | Opus 5.5 | off | `courses/egypt/DD-EG9-the-revolution-year-by-year.md` |
| 67 | DD-EG10 | EG | The theology of the Aten | not written | Opus 5.5 | off | `courses/egypt/DD-EG10-the-theology-of-the-aten.md` |
| 68 | DD-EG11 | EG | Akhetaten: the city | not written | Opus 5.5 | off | `courses/egypt/DD-EG11-akhetaten-the-city.md` |
| 69 | DD-EG12 | EG | The Amarna letters | not written | Opus 5.5 | off | `courses/egypt/DD-EG12-the-amarna-letters.md` |
| 70 | DD-EG13 | EG | Art, Nefertiti and the succession puzzle | not written | Opus 5.5 | off | `courses/egypt/DD-EG13-art-nefertiti-and-the-succession-puzzle.md` |
| 71 | DD-EG14 | EG | Aftermath and afterlives | not written | Opus 5.5 | off | `courses/egypt/DD-EG14-aftermath-and-afterlives.md` |
| 72 | DD-EG15 | EG | The Pyramid Texts | not written | Opus 5.5 | off | `courses/egypt/DD-EG15-the-pyramid-texts.md` |
| 73 | DD-EG16 | EG | The Coffin Texts | not written | Opus 5.5 | off | `courses/egypt/DD-EG16-the-coffin-texts.md` |
| 74 | DD-EG17 | EG | The Book of the Dead: how it was made | not written | Opus 5.5 | off | `courses/egypt/DD-EG17-the-book-of-the-dead-how-it-was-made.md` |
| 75 | DD-EG18 | EG | The Book of the Dead: reading it | not written | Opus 5.5 | off | `courses/egypt/DD-EG18-the-book-of-the-dead-reading-it.md` |
| 76 | DD-EG19 | EG | The books of the netherworld | not written | Opus 5.5 | off | `courses/egypt/DD-EG19-the-books-of-the-netherworld.md` |
| 77 | DD-EG20 | EG | The last afterlife texts | not written | Opus 5.5 | off | `courses/egypt/DD-EG20-the-last-afterlife-texts.md` |
| 78 | DD-EG21 | EG | What the Egyptians expected of death: the synthesis | not written | Opus 5.5 | off | `courses/egypt/DD-EG21-what-the-egyptians-expected-of-death-the-synthesis.md` |

## Courses to come (Personal Mythology)

Listed in `catalog.toml` (the History track's `planned`; the top-level `next` until P-DEC12) as coming soon, with a scope and reading spine each: Persia, Norse, Celtic, English, Scottish, Chinese, Japanese (Egypt left the list on 23 Nov 2026 for its own section above, row S-EG0). A new course is added with the `new-course` skill.

## Courses to come (Supply Chain)

Listed in `catalog.toml` (`planned` of the Supply Chain track in `tracks`, `THEMES` in `kit/courses.py`) as coming soon, after Supply Chain Execution for Product Teams, Supply Chain Planning for Product Teams and AI in Supply Chain Execution and in this order, each with its title, its scope line and its teaser, word for word from the design chat's list of 19 Nov 2026 (syllabus decision D12): Warehouse Automation and Robotics; Last Mile and Omni-channel Fulfilment. None has a syllabus, a brief, a data folder or a writing row; each needs its own design chat on Fable before anything is queued for it (row P-SCE10). A course on the logistics provider's business is left off: it is promised only if DD-SCE1 proves too thin.
