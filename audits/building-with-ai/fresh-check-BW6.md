---
audit: fresh check
unit: BW6 · Research and verification
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgQxb5xyzkrLHQ6hh6WQ
verdict: fix · 1 errors, 7 should-fix, 3 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW6 · fix · 1 errors, 7 should-fix, 3 minor

Model: claude-opus-5-5
(The harness refused the write to /tmp/bw6/c/out/report.md, so the whole report is here.)

# Fresh check · BW6 · Research and verification

I read sourcing-standard.md Parts 1 and 6, brief.txt, unsure.md, notes.md and case-academy.md. There was no audit report; I skipped it as instructed. I used live search on 16 Nov 2026. Every fetch was of a URL that a WebSearch in this run returned verbatim.

## Findings

[error] [accuracy] Deliverable I; Current: "puts it in six words"; Problem: the quoted sentence "If you can't verify it, don't ship it" has eight words, not six; Fix: "puts it in eight words"; Basis: Anthropic, Best practices for Claude Code, "The trust-then-verify gap … If you can't verify it, don't ship it." https://code.claude.com/docs/en/best-practices.md
[should-fix] [accuracy] §2 heading; Current: "### What the case adds: the commonest failure was a real source, stretched"; Problem: the case file never ranks failure kinds by how often they occur. Its §3 says Audit 1 "named" one pattern (qualifiers the source does not carry). Its §5 lists kinds with no counts, and two of them (a law that had changed, a count that did not add up) are not a stretched source. "Commonest" is therefore a stretch of the case file; Fix: "### What the case adds: the failures it names were in real sources, none invented"; Basis: Academy case file §3, §5
[should-fix] [accuracy] §3, question 4; Current: "The case's commonest failure, a qualifier the source does not carry (§2), fails here."; Problem: the case file gives this as the pattern one audit named, not as the commonest failure; Fix: "The pattern the case's first audit named, a qualifier the source does not carry (§2), fails here."; Basis: Academy case file §3 ("The pattern the audit named: qualifiers the source does not carry.")
[should-fix] [accuracy] §7, "What the numbers support"; Current: "that the commonest failure was a real source stretched, with none invented (§2)"; Problem: the same "commonest" stretch as above; Fix: "that the failures the reports name were in real sources, with none invented (§2)"; Basis: Academy case file §3, §5
[should-fix] [accuracy] Deliverable D; Current: "The case's commonest failure was a qualifier the source does not carry (case file §3)."; Problem: case file §3 gives this as the pattern Audit 1 named, not as the commonest failure; Fix: "The pattern the case's first audit named was a qualifier the source does not carry (case file §3)."; Basis: Academy case file §3
[should-fix] [accuracy] §7, "The fresh check, a census"; Current: "(case file §2; the writer of each draft is not recorded)"; Problem: case file §2 says the opposite: "The model that wrote each unit is recorded." The record exists; it is the per-draft list that the case file does not hold; Fix: "(case file §2, which says the model that wrote each unit is recorded; the case file does not list it per draft)"; Basis: Academy case file §2, "Models" bullet
[should-fix] [accuracy] Deliverable C, "How the case runs it"; Current: "Under C, seven per unit is a tier 1 sample:"; Problem: tier 1's sample is n = 9. Seven is smaller than even tier 1, and the unit's own bound shows it: a clean 7 bounds the rate at 34.8%, above tier 1's 28.3%; Fix: "Under C, seven per unit is smaller than even a tier 1 sample (9):"; Basis: the unit's own §5 tier table (1 − 0.05^(1/7) = 34.8%; ln 0.05 / ln 0.7 = 8.4, rounded up to 9)
[should-fix] [attribution] §8, table row 3, Gemini column; Current: "Gemini CLI subagents work in their own context window (BW5 §11, read 15 Nov 2026)"; Problem: the brief and Part 6 require the other vendor's own documentation, dated. This cell cites another unit instead, and notes item 10 says it was not re-read. The vendor page confirms the claim. Also add to Sources: "Google. *Subagents*. Gemini CLI documentation (vendor). https://geminicli.com/docs/core/subagents/"; Fix: "Gemini CLI subagents each have an \"Independent context window\": [*Subagents*, Gemini CLI documentation](https://geminicli.com/docs/core/subagents/) (vendor, read 16 Nov 2026)"; Basis: https://geminicli.com/docs/core/subagents/ ("Independent context window"; "Each subagent runs in its own isolated context loop.")
[minor] [attribution] §2, "Confident, specific, wrong"; Current: "the tools of LexisNexis (Lexis+ AI) and Thomson Reuters (Westlaw) produced"; Problem: the abstract names three tools. Thomson Reuters' two are Westlaw AI-Assisted Research and Ask Practical Law AI; Fix: "the tools of LexisNexis (Lexis+ AI) and Thomson Reuters (Westlaw AI-Assisted Research and Ask Practical Law AI) produced"; Basis: Magesh et al., arXiv 2405.20362v1 abstract, https://arxiv.org/abs/2405.20362v1
[minor] [attribution] §3, question 2; Current: "Cochrane Database of Systematic Reviews, 16 Feb 2017](https://www.cochrane.org/zh-hans/evidence/MR000033_industry-sponsorship-and-research-outcome)"; Problem: an English Cochrane summary exists with the same figures and the conclusion in English, which removes the paraphrase caveat in unsure item 3. Change the Sources line the same way; Fix: "Cochrane Database of Systematic Reviews, 16 Feb 2017](https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome)"; Basis: https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome ("75 included papers"; "RR: 1.27 (95% CI: 1.17 to 1.37)"; "RR: 1.34 (95% CI: 1.19 to 1.51)"; "an industry bias that cannot be explained by standard 'Risk of bias' assessments"; "16 February 2017")
[minor] [style] front matter; Current: "search: off"; Problem: the unit carries product facts read live on vendor pages on 16 Nov 2026 (Research plans and limits, Gemini's 5–10 minutes, OpenAI's background-mode advice). With the flag off, the six-month staleness check will not be scheduled for them; Fix: "search: on"; Basis: sourcing-standard.md Part 1, per-unit item 2

## Confirmed

- Hadfield et al.: the six authors and the date 13 Jun 2025; "typically use about 4× more tokens than chat interactions"; "use about 15× more tokens than chats"; "token usage by itself explains 80% of the variance", with tool calls and model choice as the other two factors; "consistently chose SEO-optimized content farms over authoritative" (the sentence goes on "but less highly-ranked sources"); "breadth-first queries" and "pursuing multiple independent directions simultaneously"; "are not a good fit for multi-agent systems today"; the citation agent; Opus 4 as lead and Sonnet 4 as subagents; page metadata modified 2026-10-09 (unsure item 8). https://www.anthropic.com/engineering/multi-agent-research-system
- *Use research on Claude*: "runs multiple searches that build on each other"; Pro, Max, Ultra, Team, Enterprise; "You must have web search turned on for research to function"; "research sessions can use up your limits faster due to Claude retrieving multiple sources"; no running time given; "Updated over 2 weeks ago". https://support.claude.com/en/articles/11088861-use-research-on-claude
- *Claude can now connect to your world*: "in anywhere from five to 45 minutes" and "most reports complete in five to 15 minutes"; 1 May 2025. https://claude.com/blog/integrations
- SimpleQA: "models consistently overstate their confidence"; GPT-4o 38.2% and Claude-3.5-sonnet 28.9% correct; Claude models "tend to not attempt questions more often than the GPT-4o models"; the models tested are as listed; confidence was elicited by asking the model to state it (unsure item 6); v1 dated 7 Nov 2024; authors as listed. https://arxiv.org/pdf/2411.04368 and https://arxiv.org/abs/2411.04368v1
- Magesh et al.: "preregistered"; "between 17% and 33% of the time"; the vendor claims "eliminate", "avoid" and "hallucination-free"; hallucinations reduced relative to GPT-4; v1 dated 30 May 2024; six authors. https://arxiv.org/abs/2405.20362v1
- Rao et al.: v1 dated 3 Apr 2026; 10 systems on DRBench; 113.1 and 41.2 URLs per query against 3.0 to 24.3; 10.7% against 4.8% pooled; a hallucinated URL is one that does not resolve and has no Wayback snapshot; "conservative lower bounds"; OpenAI deep research at 10.1% non-resolving and 3.5% hallucinated, so 65% of its non-resolving links are stale; Claude 3.5 and 3.7 Sonnet with search among the systems; neither "Preprint" nor "Under review" appears. https://arxiv.org/html/2604.03173v1
- Walters and Wilder: 84 reviews, 42 topics, 636 citations; 55% and 18% fabricated; 43% and 24% substantive errors among real works; the bibliographic elements checked; "tend to look legitimate at first glance"; support for the text was not checked. https://www.nature.com/articles/s41598-023-41032-5.pdf
- Lundh et al.: 75 papers; both risk ratios with their CIs; the conclusion on risk-of-bias assessments; 16 Feb 2017; five authors. https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome
- Abboud: Carolina J. Abboud, 23 Mar 2017; the nine viewpoints; Hill's two caveats; Hill in vol. 58, p. 295. https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill
- Newman: JAMA 274(13):1013, 4 Oct 1995, a letter; credits Hanley and Lippman-Hand; the upper limit is "approximately 3/N". https://jamanetwork.com/journals/jama/article-abstract/389714
- NIST 6.2.1: destructive testing, high cost, too slow; "not to estimate the quality of the lot". https://itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- SelfCheckGPT: authors; EMNLP 2023, pp. 9004–9017; the quotation; GPT-3 on WikiBio. https://aclanthology.org/2023.emnlp-main.557
- *Best practices for Claude Code*: "won't be biased toward code it just wrote"; "not the reasoning that produced the change"; "so the agent doing the work isn't the one grading it"; "will usually report some, even when the work is sound"; over-engineering; "If you can't verify it, don't ship it"; the `/goal` condition and the Stop hook. https://code.claude.com/docs/en/best-practices.md
- OpenAI: the page at the deep-research address is headed "Web search" and says "Use background mode for reports that can take several minutes" (unsure item 1). https://developers.openai.com/api/docs/guides/deep-research.md
- Gemini: "Edit plan"; "It usually takes about 5-10 minutes to generate the report"; daily request limits; nothing on accuracy or checking. https://support.google.com/gemini/answer/15719111
- Gemini CLI subagents have an independent context window. https://geminicli.com/docs/core/subagents/
- All the arithmetic, recomputed:
  - the table of (1 − p)ⁿ;
  - the bounds 34.8, 28.3, 19.3, 13.9, 9.8 and 10.1%;
  - n = 9, 14 and 29;
  - 3/29 = 10.3% and 3/28 = 10.7%;
  - 0.747⁸ = 9.7%, 23/91 = 25.3% and 28/36 = 77.8%;
  - 45.1%, 25.9% and 12.5%;
  - 0.75²⁹ = 0.02%.
- Case facts checked against the case file:
  - §2, §3, §4 and §6 to §9;
  - §5: the totals, the 8 and 28, the 15 of 20, and the split by checker model. I recounted Fable 5.1 = 19, Opus 5.5 = 12 and Fable 5.2 = 5 from the table.

Unverifiable or not checked:
- Vu et al., FreshLLMs (the quotation, "substantially", the v2 date and the author list): the fetch of arxiv.org/abs/2310.03214v2 was refused. Not checked and not retried.
- "$10 per 1,000 searches" (carried from BW2 §6): the pricing URL redirected. Not checked.
- Whether the 80% variance analysis was run on the Opus 4/Sonnet 4 setup specifically: what I read does not tie the BrowseComp analysis to that setup.
- "2024 and 2025 releases" for Rao's systems: not confirmed.
- Hill's issue 5 and pp. 295–300: the PMC page was not opened.

## (7) Figures

1. **compare · §1 · PASS.**
   - "Chat" = 1: the implied baseline in "more tokens than chat interactions".
   - "Agent with tools" = 4: "typically use about 4× more tokens than chat interactions".
   - "Multi-agent research" = 15: "use about 15× more tokens than chats".
   - The caption names §1 and Hadfield et al. 2025 (vendor). The kind fits.
2. **decision · §1 · PASS.** Every node traces to the routing-rule text and to "Anything after the cutoff, and any specific … you will publish, file or act on". The caption names §1, BW1 §4 and Hadfield. The kind fits.
3. **line · §5 · PASS.** The x values and both series match the §5 table rows ("| 7 | 47.8% | 13.3% |" … "| 29 | 4.7% | 0.0% (0.02%) |"). The caption names §5, the formula and case file §3 (23 of 91, which matches "23/91 = 25.3%"). Line fits a trend.
4. **decision · Deliverable C · PASS.** Every branch traces to C5 ("an invented source … → full check", "any FAIL → full check", "any STALE → sweep", "all PASS → use it … and log it"). The caption names Rule C5 and §5. The kind fits.

## (8) Writer's Source errors list

notes.md lists no source errors, one stale item and three items it could not re-verify.
- **Confirmed.** The help page now shows "Updated over 2 weeks ago" and lists Pro, Max, Ultra, Team and Enterprise ("paid Claude plans (Pro, Max, Ultra, Team, or Enterprise)").
- **Confirmed.** Rao's "under review" label is absent from HTML v1.
- **Neither confirmed nor refuted.** Walters and Wilder's day of publication: the fetch did not show it, and DOAJ's search title reads "Sep 2023". Citing the year only is safe.
- **Confirmed.** Abboud carries the paraphrased Hill points.

## (9) Part 1 and Part 6

Part 1:
- Each claim is sourced where it is made.
- Sources can be opened and are dated by the day they were read.
- "Says what the claim says": this fails in the six places listed in Findings ("commonest" four times, "not recorded", "six words"). It holds everywhere else I checked.
- Reporters are kept separate: Hill is cited "as summarised by" Abboud.
- Each number says whose figure it is.
- Views are not attached to people who did not argue them.
- Every quotation I checked is exact. FreshLLMs was not checked.
- Nothing invented.
- All four figures pass. There are no illustrations.
- Claims that cannot be sourced are said to be unsourced.
- The search flag is "off" despite live reads (minor finding).
- The Sources list is complete except for the Gemini CLI page (should-fix).
- The closing material agrees with the body except for D and C (findings).

Part 6:
- Source classes are labelled. The NIST handbook falls outside the five classes, but it is used only for a statistical definition.
- Evidence grades are applied throughout.
- Each study names its models and task, except FreshQA ("tested 2023 models", models not named; not checked).
- Product facts are dated on the vendor's page, except the $10 figure (carried from BW2) and the Gemini CLI cell (fixed above).
- "On other tools" is present.
- Claims carried over from the source unit hold wherever I could open the source.
- No private-reader detail and no reference to the private course.
- Case facts:
  - every one is in the case file and cited by section;
  - the first use is labelled "(Academy case; one project, an anecdote)";
  - the case is never the only support for a general claim (§2's rule also rests on Walters and Wilder).
- The deliverable is built on the case and then as a template, with gaps marked [UNKNOWN] and not guessed.
- Links are given as links.

## (10) Persona reading

An in-order reader who has done BW1 to BW5 can follow the unit. Four things lean on context the unit does not give:
- "Fable 5.1/5.2" and "large, top rung, Fable 5.2, high (BW2, rows 5 and 9)" (Deliverable E) assume BW2's routing vocabulary.
- Academy is never described in this unit; one clause at first use from case file §1 would let the unit stand alone.
- "the maintainer" is not defined.
- "Audit 1/2" are clear from context.

No term or unit code from the private course appears.

## (6) Pointers

The unit points to these sections of units in the Takes line:
- BW1 §1, §4, §5, §7;
- BW2 §1, §4, §5, §6, routing rows 5, 7, 9, rule 4;
- BW5 §10, §11, Deliverable 2b.

All are plausible. It also points to BW3 (§3; Deliverable templates 3 and 9), which is not in the Takes line. The writer records this in Contradictions 1, citing BW5's build order and BW3's Deliverable. It is plausible, but I cannot check it from the packet; the Takes line should be reconciled as the writer proposes. BW5's 2b blank, quoted in J, could not be checked.

## (11) Attribution pass

- Sources titles match their page headlines. OpenAI is correctly titled *Web search*. Lundh is listed under the Chinese headline it was read under (minor finding). Vu was not checked.
- Every quotation I checked is attributed to the right speaker and matches the exact words. The SEO quotation is a faithful truncation.
- Every figure matches the page that states it for that thing. The 17–33% range covers the three legal tools (minor finding on tool names).

## (1) Coverage

Every item the brief names is covered: the three routes with cost and time where a source states them; failure modes with the studies that measured them; reading a report; writer against checker; the stratified audit with its arithmetic; checking a checker; the case's numbers as anecdote. The deliverable has the checklist, the sampling rule by stakes, the arithmetic, the checker brief and the template. Both things the brief says the unit gives are present: the checker brief (E) and the verifiability test (I). "On other tools" is present. Length: the body is about 6,000 words and the deliverable about 3,500.

## (4) Labels

Anecdote, vendor, preprint and correlational labels are all present: the 80% figure is labelled "an association", and Lundh's finding is labelled an analogy when carried to AI.

## (5) Deliverable

Present in full, follows from §1–§7, and usable alone. It needs the D and C fixes above.

Verdict: BW6 · fix · 1 errors, 7 should-fix, 3 minor
