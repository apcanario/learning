---
audit: fresh check
unit: BW7 · Pipelines: raw material to finished output
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgQxb5xyzkrLHQ6hh6WQ
verdict: fix · 2 errors, 7 should-fix, 11 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW7 · fix · 2 errors, 7 should-fix, 11 minor

Model: claude-opus-5-5

# Fresh check · BW7 · Pipelines: raw material to finished output

The write to /tmp/bw7/c/out/report.md was refused ("Subagents should return findings as text"), so the full report is here.

- Checked 16 Nov 2026, with live search.
- Read the packet only. No audit report, so that step was skipped.
- BW1 to BW6 were not available, so pointers to them are checked for plausibility only.

## Findings

[error] [accuracy] §4 table intro; Current: "Eight studies bear on where that line falls."; Problem: the table that follows lists nine studies (Noy and Zhang; Dell'Acqua et al.; Doshi and Hauser; Padmakumar and He; Chakrabarty, Laban and Wu; Agarwal, Naaman and Vashistha; Jentzsch and Kersting; Gorenz and Schwarz; Jakesch et al.); Fix: "Nine studies bear on where that line falls."; Basis: the unit's own §4 table.
[error] [accuracy] §4 Options; Current: "Fiction, rated by strangers, with 2024's GPT-4."; Problem: the study cannot have used a 2024 GPT-4: the paper was "Submitted 14 December 2023" and says "At the time of the study, we used the API from OpenAI's latest model, GPT-4"; the model predates 2024; Fix: "Fiction, rated by strangers, with GPT-4 as it was before the paper's submission on 14 December 2023."; Basis: Doshi and Hauser, Science Advances 10, eadn5290, Exeter repository copy, https://ore.exeter.ac.uk/rest/bitstreams/199326/retrieve
[should-fix] [accuracy] §5 item 4; Current: "was on a task where the AI's answer was persuasive."; Problem: stretch: the paper never calls the AI's answer persuasive or convincing. It says the task "was designed so that GPT-4 would make an error", and that AI users "consistently outperformed those not using AI in terms of recommendation quality, regardless of the correctness of their answer"; Fix: "was on a task designed so that GPT-4 would make an error, and the AI users' recommendations were still rated higher in quality whether or not they were correct."; Basis: Dell'Acqua et al., HBS WP 24-013, https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
[should-fix] [accuracy] §4 Structure; Current: "What it supports for a pipeline (inference): the model takes the rough-draft and arrangement work, and your time moves to choosing and editing, which is where the gates are."; Problem: Noy and Zhang measured how participants split their time (brainstorm, rough draft, edit), not a model arranging a text, so "arrangement" is not in the source. The structure claim also has no evidence grade (Part 6); Fix: "What it supports for a pipeline (inference): the model takes the rough-draft work, and your time moves to choosing and editing, which is where the gates are. The study measured time and graded quality, not the model's arranging of a text; grade for structure: stated opinion, built on this finding and Anthropic's outline example (§1)."; Basis: Noy and Zhang working paper, 10 Mar 2023, https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf
[should-fix] [label] §2; Current: "Four reasons, each sourced."; Problem: reason 4 ("Files survive the loss of a session") rests only on the Academy case, which Part 6 forbids as the only support for a general claim; Fix: "Four reasons; the first three are sourced, and the fourth is an anecdote that illustrates the first."; Basis: sourcing-standard Part 6; Academy case file §7.
[should-fix] [accuracy] Deliverable Part 1, Step 4; Current: "- **Gate (human):** each finding is verified at its source before it is applied"; Problem: the case file names only "a maintainer" (§2) and does not say it is a person. The unit's own Model line and its §8 table ("Human or maintainer gate") say this is not recorded, so "human" infers a case fact the file does not hold; Fix: "- **Gate (maintainer; whether a person or a model is `[NOT IN CASE FILE]`):** each finding is verified at its source before it is applied"; Basis: Academy case file §2.
[should-fix] [attribution] Deliverable Part 3, final pass; Current: "(BW6, Part 2, steps F and G)"; Problem: §5 and Part 1 point to "BW6, Deliverable Part 1, steps F and G", and Sources lists only BW6's Deliverable Part 1, so this pointer is inconsistent; Fix: "(BW6, Deliverable Part 1, steps F and G)"; Basis: the unit's §5 and Sources list.
[should-fix] [deliverable] Deliverable Part 2, step 5; Current: "`report-v1.md`, the clean notes → `checks/report-check.md`"; Problem: step 6 reads `report-v2.md`, but no step produces it, so the procedure cannot be run as written; Fix: "`report-v1.md`, the clean notes → `checks/report-check.md`, then the verified findings applied → `report-v2.md`"; Basis: the unit's own Part 2 table (step 6 input).
[should-fix] [style] §4, before the matrix; Current: "The division of the work that follows, used by every pipeline in the Deliverable:"; Problem: repeats the opening of the paragraph just above it, a leftover duplicate; Fix: ""; Basis: unit text.
[minor] [accuracy] §4 First-person prose; Current: "Four studies point the same way"; Problem: the four bullets cite five studies (Padmakumar and He; Doshi and Hauser; Dell'Acqua et al.; Chakrabarty et al.; Agarwal et al.); Fix: "Five studies point the same way"; Basis: unit text.
[minor] [accuracy] Deliverable Part 1, Step 0; Current: "The unit's brief exists, approved, with"; Problem: the case file records no approval of briefs (§2: "One brief per unit, never reworded"); Fix: "The unit's brief exists, with"; Basis: Academy case file §2.
[minor] [deliverable] Deliverable Part 2, step 4; Current: "Safe; writes `report-v2.md`; steps 5 to 8 re-run on it"; Problem: a re-run of step 4 and the checked draft would both be called `report-v2.md`, which breaks §6's rule of one named version per output; Fix: "Safe; writes a new draft version (`report-v1b.md`); steps 5 to 8 re-run on it"; Basis: unit §6, point 2.
[minor] [style] Deliverable Part 1, Step 3; Current: "override, Opus 5.5, high, in a fresh context, recorded as the writer's model."; Problem: unclear what is recorded or why; Fix: "override: Opus 5.5, high, in a fresh context; the log records that the checker ran on the writer's model."; Basis: unit text.
[minor] [label] §7; Current: "**What a line holds** (this unit's form; each field traces to the source named):"; Problem: the log form is a practice with no evidence grade (Part 6); Fix: "**What a line holds** (this unit's form, stated opinion; each field traces to the source named):"; Basis: sourcing-standard Part 6.
[minor] [attribution] Sources, units line; Current: "BW4 (§4, §5, Deliverable Part 4, step 6)"; Problem: the Deliverable's conventions cite "BW4's Part 3 folders", but the Sources list does not include Part 3; Fix: "BW4 (§4, §5, Deliverable Part 3, Deliverable Part 4, step 6)"; Basis: unit Deliverable conventions.
[minor] [attribution] Sources, Dolan entry; Current: "PsyPost, 4 July 2024 (reporting Gorenz and Schwarz, *PLOS ONE*, 2024)."; Problem: the reported paper is named without its title. Its title is "How funny is ChatGPT? A comparison of human- and A.I.-produced jokes" (PubMed Central listing; the page was reached only by a redirect and was not opened); Fix: "PsyPost, 4 July 2024 (reporting Gorenz and Schwarz, *How funny is ChatGPT? A comparison of human- and A.I.-produced jokes*, *PLOS ONE*, 2024, not opened)."; Basis: search result title for https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11221738/
[minor] [style] §8 table, Publishing row; Current: "| A structure audit of the project found private terms reaching a public build (§7) |"; Problem: a public-course reader is not told what "private terms" means; Fix: "| A structure audit of the project found private terms (words meant to stay out of the public site) reaching a public build (§7) |"; Basis: Academy case file §7 and header.
[minor] [accuracy] Deliverable Part 1, Pipeline card; Current: "and every four units, at the sample audit (case file §2)."; Problem: the card presents the sample-audit boundary as running, but the case file records that audits 3 onward had not run at 11 Nov 2026; Fix: "and every four units, at the sample audit (case file §2; audits 3 onward had not run at 11 Nov 2026, case file §9)."; Basis: Academy case file §9.
[minor] [attribution] §9 table, fresh-context row; Current: "| BW6 §4 (*Best practices for Claude Code*) |"; Problem: names a vendor page that the Sources list does not include (Part 1); Fix: "| BW6 §4 |"; Basis: sourcing-standard Part 1.
[minor] [attribution] §2 reason 2; Current: "That is Laban and colleagues' measurement, summarised in BW3 §5."; Problem: a measured claim is made with no source, models or task (Part 6). The study is Laban, Hayashi, Zhou and Neville, arXiv 2505.06120: 15 LLMs, "an average drop of 39% across six generation tasks"; Fix: "That is Laban and colleagues' measurement across 15 models and six generation tasks, summarised in BW3 §5 ([Laban, Hayashi, Zhou and Neville, *LLMs Get Lost In Multi-Turn Conversation*, arXiv 2505.06120](https://arxiv.org/pdf/2505.06120); preprint)."; Basis: https://arxiv.org/pdf/2505.06120

## Confirmed

- **Building effective agents** (PASS). https://anthropic.com/engineering/building-effective-agents
  - Dated "Dec 19, 2024"; "Written by Erik S. and Barry Zhang".
  - Tooling note: "has changed since December 2024".
  - "decomposes a task into a sequence of steps"; "can add programmatic checks", labelled "gate"; "can be easily and cleanly decomposed into fixed subtasks".
  - The latency-for-accuracy trade and both examples.
  - Workflows "orchestrated through predefined code paths"; agents "dynamically direct their own processes and tool usage".
- **Prompting best practices, "Chain complex prompts"** (PASS). https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts
  - "handles most multistep reasoning internally".
  - "still useful when you need to inspect intermediate outputs or enforce a specific pipeline structure".
  - "log, evaluate, or branch at any point".
  - The self-correction chain.
- **Dell'Acqua et al.** (PASS). https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
  - WP 24-013, September 22, 2023; 758 consultants.
  - 12.2% more tasks and 25.1% faster; more than 40% higher quality.
  - "19 percentage points less likely to produce correct solutions".
  - The §3.1 "marked reduction in the variability" quotation.
- **Noy and Zhang, Science, July 2023** (PASS). https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence
  - 453 professionals; "The average time taken decreased by 40% and output quality rose by 18%".
- **Noy and Zhang working paper, 10 Mar 2023** (PASS). https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf
  - The restructuring quotation.
  - Time split 25/50/25; rough-draft share down by more than half.
  - 20- to 30-minute tasks, of the four task types named; no ChatGPT version given.
- **Doshi and Hauser** (PASS). https://ore.exeter.ac.uk/rest/bitstreams/199326/retrieve
  - 500 recruited, 293 analysed; 600 evaluators; GPT-4.
  - 8.1% and 9.0% gains; 10.7% and 11.5% for less creative writers.
  - "10.7% and 8.9% of the total range"; "resembles a social dilemma".
  - Published 12 July 2024.
- **Padmakumar and He** (PASS). https://arxiv.org/html/2309.05196v3 ; https://proceedings.iclr.cc/paper_files/paper/2024/hash/02dec8877fb7c6aa9a79f81661baca7c-Abstract-Conference.html
  - 38 writers; essays of about 300 words; davinci and text-davinci-003.
  - All three quotations.
  - ICLR 2024, pp. 642–669 (metadata).
- **Chakrabarty, Laban and Wu, v5 of 2025-03-04** (PASS). https://arxiv.org/html/2409.14509v5
  - No venue on the arXiv page.
  - 18 writers from MFA mailing lists, all with MFAs per Table 4.
  - 1,057 paragraphs; "about 8 edits per paragraph, totaling 8,035"; 28/20/18/17% (§5.1); seven categories; three models.
  - 65% and 60% (§6.3); the §7.4 quotation.
- **Agarwal et al.** (PASS). https://arxiv.org/html/2409.11360v3
  - 118 participants from India and the US; four short essays in English.
  - GPT-4o inline autocomplete; both quotations; CHI '25, Yokohama.
- **Jentzsch and Kersting** (PASS). https://aclanthology.org/2023.wassa-1.29
  - WASSA 2023, pp. 325–340; the "same 25 Jokes" quotation; "GPT3-based model".
- **Gorenz and Schwarz via PsyPost** (PASS as the report's account). https://www.psypost.org/ai-outshines-humans-in-humor-study-finds-chatgpt-is-as-funny-as-the-onion/
  - Dolan, 4 Jul 2024; ChatGPT 3.5; 73/63/87%; "no significant difference" from The Onion.
  - The paper itself is unverifiable: it was reached only by a redirect.
- **Jakesch et al.** (PASS). https://arxiv.org/pdf/2302.00560
  - 1,506 participants; text-davinci-002.
  - 2.04 and 2.0 times; the "often unaware" quotation; the survey shift; the authors; CHI '23.
- **Airflow 2.3.3** (PASS). https://airflow.apache.org/docs/apache-airflow/2.3.3/best-practices.html
  - All five quotations hold verbatim.
- **OpenAI "Agent orchestration"** (PASS). https://openai.github.io/openai-agents-python/multi_agent/
  - The chaining quotation and the blog-post example; the evaluator-loop quotation.
  - No sentence on logging, so "No equivalent sentence found" holds.
- **Vertex AI "Break down complex tasks into simpler prompts"** (PASS). https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/break-down-prompts
  - All three quotations; "Last updated 2026-11-12 UTC".
- **Academy case** (PASS). Academy case file.
  - Checkers 19 Fable 5.1, 12 Opus 5.5, 5 Fable 5.2 (recounted from the §5 table); 58 errors; 28 of 36 drafts with an error.
  - Restarts, the "fable" session, missing transcripts (§7).
  - The figure rules and the eighth-check sitemap (§6).
  - Audit 1's missing deliverables (§3).
  - BW1's report saved from the reply, 15 Nov 2026 (§7 note).
  - No hours measure and no control (§9); Opus 5.5 writes, Fable 5.1 audits (§2).

## (1) Coverage

- Covered: what a pipeline is (§1), file hand-offs (§2), human gates (§3), the final pass (§5), re-running (§6), logging (§7), the case pipeline with its failures (§8), On other tools (§9), and the Deliverable's three parts.
- The studies (§4) are covered, each with its models and task.
- Cuts and endings rest on inference, which the unit says. Structure is thin: its support is a time-allocation finding.

## (2) Accuracy, from unsure.md

1. Gorenz and Schwarz: the figures are confirmed as the report's account; the paper is unverifiable (redirect).
2. Doshi and Hauser: volume, article, 293 of 500 and GPT-4 confirmed. The issue number was not checked. The study predates December 2023 (error).
3. Chakrabarty: all confirmed; all 18 writers hold an MFA (Table 4).
4. Noy and Zhang: confirmed in the working paper.
5. Dell'Acqua §3.1: confirmed.
6. Jentzsch: confirmed.
7. Cuts and endings: graded as inference, as stated.
8. Building effective agents: author line and tooling note confirmed.
9. Airflow: confirmed; the current version was not checked.
10. Gemini prompt-design page: not checked by me either.

## (3) Whose figure

Every number is attributed: study figures to their study, case counts to the case file, Part 2's numbers labelled invented. PASS.

## (4) Labels

- Vendor pages are labelled and dated.
- Preprints and working papers are labelled.
- The case is labelled "(Academy case)" on first use (§2) and as an anecdote.
- Exception: in §2, reason 4 makes the case the only support for a general claim.

## (5) Deliverable

- Present in full: Part 1 (eight steps plus Step 0 and the boundary), Part 2 (eight steps, sample outputs, run log) and Part 3 (template with self-describing blanks and pre-run checks).
- It follows from §3 to §7.
- It is usable alone except for the `report-v2.md` gap and the BW6 pointer.

## (6) Pointers

- The pointers to BW2, BW3, BW5 and BW6 (all in the Takes line) are plausible.
- BW1 and BW4 are cited but are not in the Takes line. They are earlier units the reader has read, so this is plausible.
- Two inconsistencies, both in the findings: "BW6, Part 2", and BW4 Part 3 missing from Sources.
- None of these units could be opened.

## (7) Figures

1. compare, §4: **PASS**.
   - Labels and values trace to "awkward word choice and phrasing (28% of edits), poor sentence structure (20%), unnecessary or redundant exposition (18%) and clichés (17%) (§5.1)".
   - The caption's numbers trace to "had 18 writers with MFA backgrounds edit 1,057 paragraphs ... gathering 8,035 edits ... the four largest of seven categories".
   - The caption names the section and the source; the kind fits.
2. matrix, §4: **PASS**.
   - The marks trace to "the model's stage drafts ... you approve the structure, check the cuts and choose among the options ... may write a marked bridge only ... never writes humour ... points to candidates in your material; you write the prose and the humour and decide the ending".
   - The caption names §4 and its sources; the kind fits.
   - Legend tones 2, 1 and 4 match their cells.
3. flow, §8: **PASS**.
   - Every note traces to the §8 table: "never reworded"; "Writers lost to container restarts"; "28 of 36 drafts had at least one error"; "verified, then applied as an exact replacement"; "the backlog row moved to the changelog; the writing model recorded"; "built by script"; "one sitemap passed on its eighth check"; "private terms reaching a public build".
   - The caption names §8 and case file sections; the kind fits (a sequence).

## (8) Writer's Source errors list

The B7 text these items quote is outside the packet, so only the corrections are checked.
1. **Confirmed**: "we recruited 500 participants"; "a total number of writers and stories of 293" (Exeter copy).
2. **Confirmed**: "we used the API from OpenAI's latest model, GPT-4".
3. **Confirmed**: "fetched an inline autocomplete suggestion from GPT-4o" (arXiv v3).

## (9) Sourcing standard, Parts 1 and 6

Part 1:
- Holds, except where the claim must be what the source says: §4 "arrangement" and §5 "persuasive" fail it.
- Sources complete: no. "Best practices for Claude Code" is named but not listed, BW4 Part 3 is missing, and Laban is not listed.
- Closing material agrees: no, the BW6 pointer.
- Every other line holds, including the exact quotations and that nothing was invented. The wrong "2024" date is an error, not an invention.

Part 6:
- Holds, except for the evidence grades (structure and the §7 log form are not graded).
- Models and task named: the Laban claim cites BW3 instead of the study.
- Case facts: Step 4's "human" gate and Step 0's "approved" are not in the case file.
- No private-course or private-reader terms found.
- On other tools: the OpenAI fresh-context cell says "not checked" instead of "none found"; the unit discloses this.

## (10) Persona read

Nothing needs knowledge of the private course. Terms an outside reader meets without explanation:
- "private terms"
- "deep dive"
- "a sitemap figure"
- "Fable 5.1/5.2" and "large top rung" (these assume BW2)
- "BW5's BUILD-ORDER.md"

The body runs to about 6,700 words, above the 2,000–6,000 guide. The brief allows what the topic needs, but the six- and seven-column tables will be hard to read on a phone.

## (11) Attribution pass

- Every Sources title matches its page headline.
- Every quotation matches its speaker and the source's exact words.
- Every figure matches its page, except the Doshi model date and the Dell'Acqua "persuasive" characterisation (both in the findings).
