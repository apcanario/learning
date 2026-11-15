# Corrections from BW2's writer's notes

Corrections checker: Opus 5.5 (claude-opus-5-5), fresh agent, 15 Nov 2026, live search on. Read only the packet; edited no unit.

Scope worked: notes.md, Source errors (2) and Contradictions (2). Result: 2 changes, both to `courses/brand-ai/B2-choosing-the-model.md`; 2 PASS, 0 FAIL, 2 to apply. No change to BW1 or any other filed unit. Neither contradiction is a correction to a filed unit's text (see "Contradictions" below and `brief_changes.md`).

---

## c1 · B2 §1, Opus 5.5 bullet: the 40% figure's qualifier

**File:** `courses/brand-ai/B2-choosing-the-model.md` (packet: `sources/B2-choosing-the-model.md`, line 29)

**Current** (occurs exactly once in the file; 0 times in BW1):

> and that lower per-token prices plus fewer tokens per task cut costs by 40% against Opus 5

**Replacement:**

> and that it costs 40% less to run than Opus 5 on typical workloads at default settings, from lower per-token prices and fewer tokens per task

Note on the replacement: the writer's notes give it as "Anthropic says Opus 5.5 costs 40% less ... per task". Dropped verbatim into the sentence it would read "Anthropic says it performs ... and that Anthropic says Opus 5.5 costs ...", which is broken. The Current is therefore taken from "and that" and the replacement keeps the sentence's own frame ("Anthropic says it performs ... and that it costs ..."). Content is the writer's replacement word for word otherwise. Citation unchanged.

Resulting sentence: "Anthropic says it performs at about the level of Fable 5.1 on most work, and that it costs 40% less to run than Opus 5 on typical workloads at default settings, from lower per-token prices and fewer tokens per task ([Anthropic, *Introducing Claude Opus 5.5*, 22 Sep 2026](...))."

**Verdict: PASS.** Searched anew; fetched https://anthropic.com/news/claude-opus-5-5 (returned by the search "anthropic.com news claude-opus-5-5"), published 22 Sep 2026. The page says:
- "Our tests show that at default settings it will cost 40% less than Opus 5 on typical workloads."
- "It costs less per token than Opus 5 and uses fewer tokens per task, which nets out to a 40% drop in costs."
- "It performs at the level of Claude Fable 5.1 on most work and costs 40% less to run than Opus 5."

Every element of the replacement is on the page: 40% less to run, against Opus 5, typical workloads, default settings, lower per-token price, fewer tokens per task.

Calibration: the current text is not false. It is a close paraphrase of the page's own "nets out to a 40% drop in costs" sentence, which also carries no qualifier. The error is the one the writer names: the qualifier the page attaches to the measured figure in its cost section is dropped. The fix makes the claim as narrow as the page's measured statement; it is a precision correction, not a reversal.

Observation, outside scope, not a change: B2 links the launch post as `https://www.anthropic.com/claude-opus-5-5`; the search returned it at `https://anthropic.com/news/claude-opus-5-5`. The B2 link itself was not fetched (not returned by a search), so whether it resolves is not checked.

**Syllabus:** none. No BW brief, filed unit or the register uses the 40% figure (searched briefs-all-BW-units.txt, units_data.py, hub.py, syllabus-flags.md, case-academy.md, filed/BW1-mental-model.md: no match for "40%", "typical workload", "default settings"). BW2's brief takes B2 only "as source material; its lineup and prices are re-read, not carried over"; the writer states BW2 does not use the figure. No later brief relies on it.

**Apply:** yes.

**Erratum note:** The 40% saving against Opus 5 was given without the launch page's qualifier (typical workloads, default settings).

---

## c2 · B2 §7, "What a step of effort costs, measured": what the post labels illustrative

**File:** `courses/brand-ai/B2-choosing-the-model.md` (packet: line 225)

**Current** (occurs exactly once in the file; 0 times in BW1):

> the only visuals it labels illustrative are its two cost-curve charts

**Replacement** (the writer's, verbatim; fits the sentence as is):

> the visuals it labels illustrative are its two cost-curve charts and the token IDs in its tokenization example

Resulting clause: "the post gives no measurement behind it, and the visuals it labels illustrative are its two cost-curve charts and the token IDs in its tokenization example ([Claude blog](...)), so that figure is one unmeasured example, not evidence."

**Verdict: PASS.** Searched anew ("Choosing a Claude model and effort level in Claude Code Lydia Hallie"); fetched https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code (returned verbatim by that search). Lydia Hallie, 7 Jul 2026. The post labels exactly three things illustrative:
- Tokenization figure caption: "Each chunk in the top row becomes its token ID (bottom row); IDs shown are illustrative."
- Effort chart, simple task: "Curves are for illustration purposes only, shown for a single task simple enough to be accomplished quickly by both models. They do not represent real benchmark data."
- Effort chart, hard task: "Curves are for illustration purposes only, shown for a single task hard enough to stretch both models. They do not represent real benchmark data."

The 7x caption ("Same prompt, two effort levels. The high effort path generates roughly 7x more tokens to reach a higher confidence answer.") is not labelled illustrative, so the clause's conclusion ("one unmeasured example, not evidence") still stands after the change, and the writer's related remark about B2's fresh-check report is confirmed: the caption is not labelled "for illustration purposes only". That report is not a unit and is not corrected here.

**Syllabus:** none. No BW brief, filed unit or the register refers to the post's illustrative labels or the 7x caption (searched for "illustrat", "7x", "token ID", "tokeniz": the only hits are BW1's own illustrative arithmetic and token definition, unrelated, and BW2's own text, unfiled). No later brief relies on it.

**Apply:** yes.

**Erratum note:** Said the post labels only its two cost-curve charts illustrative; it also labels the token IDs in its tokenization example illustrative.

---

## Contradictions (notes.md): neither is a correction to a filed unit

### Contradiction 1 · BW2's brief against Anthropic's lineup (three tiers vs two large rungs)

Not a correction. The text that would change is a brief (and BW2, which is not filed); BW7 and BW10 are unwritten. No filed unit's text is involved: BW1 was checked and does not use the tier words "small and fast, mid, large". Listed in `brief_changes.md` as a possible brief change, with the brief quoted. The writer proposes none; BW2 handles it inside the brief's wording.

### Contradiction 2 · Academy case file §2 against §5

Not a correction to a unit and not a brief change. Verified in case-academy.md: §2 reads "**Models.** One model (Opus 5.5) writes; a different model (Fable 5.1) audits."; the §5 checker column counts 19 Fable 5.1, 12 Opus 5.5, 5 Fable 5.2 (36 fresh checks). §2 speaks of the sample audit, §5 of fresh checks, so the two do not conflict in fact. The remedy, if any, is a clarifying line in the register itself, which only the filing chat may add ("the fact is added here from the records, by the chat that files the unit, never by a writer"). No filed unit (BW1) states either fact in a way that conflicts. Listed in `brief_changes.md` as "no brief change; register note optional".

### Other items in notes.md not worked

- The stale Artificial Analysis rows, Fable 5.2 pricing, the Ultra plan name and B2 §2's chat window are listed by the writer as stale, not mistakes, for B2's next staleness check. Not corrections under this task; not checked.
- Needs 1 to 7 and "Facts about Academy that case-academy.md lacks" are syllabus and register needs, not corrections.
