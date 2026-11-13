---
audit: correction check (docs/public-courses.md §3 rule 12; step 1b of row W-PB9)
units: PB8 (P105: register lines A3, T1, T2, the deliverable's opening line and D3's status note; flags F61, F64)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk; live search)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB9/W-PB10 chat (which runs on Opus 5.5 and only stages, applies, files and publishes) in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: C1 to C6 PASS, no syllabus conflict; 3 new items (worked in round 2)
---

The checker's final report, verbatim. The harness refused the agent's own write of `out/report.md` ("Subagents should return findings as text, not write report files"), so the report is the text it returned, copied here unchanged by the chat before any change was applied. The exact strings applied are in its `out/edits.json`, checked by script to apply in order with each current found once.

Model: claude-opus-5-5

# Correction check P105: PB8's lines for Portugal (13 Nov 2026)

**Verdict: PASS. 6 edits (C1–C5 plus the note C6), all pass, no syllabus conflict; edits.json applies cleanly in order (each current found once); 3 New items.**

Scope: PB8 lines 231, 266, 272 (A3), 282 (T1) and 283 (T2), as listed in `corrections.md`.

Story fact source: `case-facts.md`, section "Set by syllabus decision P102 (13 Nov 2026)": "Mara lives in Portugal (fictional). Her tax and national legal lines (PB8 register A3, T1, T2) are worked under Portuguese rules as hers, labelled as her case; no Portuguese rate or threshold is stated as the reader's ... and every reader still gets the EU, UK and US questions and sources."

No Portuguese rate, threshold, form or authority name is added, so no Portal das Finanças or Segurança Social page was needed. A script confirmed that these stay unchanged: the EU, UK and US columns, the Question, Owner and Professional columns, and the templates (T1–T3).

## Changes

**C1 (line 231, the deliverable's opening)**
- Current: `her country is not set by any unit, so the register gives the EU, UK and US source on every line.`
- Replacement: `she lives in Portugal (Mara, fictional; set 13 Nov 2026), and the register still gives the EU, UK and US source on every line.`
- Count: 1. **PASS**. No source claim: names the register's story fact (P102).
- Syllabus: no conflict. It agrees with the register (P102). It also keeps the PB8 brief's "give the question to answer and the primary source to open for the EU, the UK and the US".

**C2 (line 266, D3's status note)**
- Current: `Her country is not set by any unit, so lines that depend on it are open until she names it.`
- Replacement: `She lives in Portugal (Mara, fictional; set 13 Nov 2026); lines that depend on Portuguese rules stay open until they are answered for her.`
- Count: 1 after C1. **PASS**. No source claim: names the register's story fact.
- Syllabus: no conflict. The PB8 brief asks for lines "filled where her facts allow and marked open where they do not", and these lines stay open.

**C3 (line 272, A3's status)**
- Current: `| Open: her country not set (13 Nov 2026) | Mara | Neither |`
- Replacement: `| Open: she lives in Portugal; which authority applies the rules there is not yet checked (13 Nov 2026) | Mara | Neither |`
- Count: 1 after C1–C2. **PASS**. No source claim: names the register's story fact.
- The question stays, and the Professional column stays "Neither" as filed.
- Syllabus: no conflict. No authority is named (see New 1).

**C4 (line 282, T1's status)**
- Current: `Open: her country not set; she asks a tax professional before the first income, of any kind (13 Nov 2026)`
- Replacement: `Open: she lives in Portugal; she asks a tax professional before the first income, of any kind (13 Nov 2026)`
- Count: 1 after C1–C3. **PASS**. No source claim: names the register's story fact. The tax professional question stays.
- Syllabus: no conflict.
  - The PB8 brief says "Gives: ... the open tax and contract questions DD-PB2 treats as inputs". T1 stays open, so DD-PB2's "tax as an input the model does not compute, with the instruction for the reader" still holds.
  - F61's "DD-PB2 works her tax inputs under Portuguese rules as hers, labelled" also still holds.
  - Neutral ground ("no country's tax rates or thresholds are stated as the reader's") is respected, because no rate is added.

**C5 (line 283, T2's status)**
- Current: `| Open; until answered, no gifts (clause 7) (13 Nov 2026) | Mara | Tax professional |`
- Replacement: `| Open: she lives in Portugal; until answered, no gifts (clause 7) (13 Nov 2026) | Mara | Tax professional |`
- Count: 1 after C1–C4. **PASS**. No source claim: names the register's story fact.
- Syllabus: no conflict. Clause 7 is unchanged. PB9 ("Takes: ... PB8") gets the same disclosure rules and the same open question on gifts.

**C6 (the dated note, appended after the last Unsure-list item)**
- Current: ``report `audits/personal-brand/fresh-check-PB8.md`\n`` (count 1 after C1–C5)
- Replacement: the same text, followed by:
  `- Correction 2026-11-13, found by P102/P105: this unit said no unit sets Mara's country; P102 (13 Nov 2026) set it as Portugal (Mara, fictional), so the deliverable's opening line, D3's status note and register lines A3, T1 and T2 now name Portugal and stay open, A3 for her to check and T1 and T2 for a tax professional; no Portuguese rate, threshold, form or authority was added, and the EU, UK and US columns and the templates are unchanged.`
- **PASS**. It states only what C1–C5 do. Syllabus: no conflict.

**Script check (`out/build_edits.py`)**
- Each current occurs exactly once at its turn, applied in order to a copy.
- After the edits, "country not set" and "not set by any unit" each occur 0 times.
- 5 lines changed and 1 line was added (the note).
- The template rows A3, T1 and T2 are byte-identical to the original.

## New

1. **A3 could name a sourced authority, but only if the scope is widened.**
   - A WebSearch returned the gov.pt entity page for the Direção-Geral do Consumidor, which I opened: https://www.gov.pt/entidades/direcao-geral-do-consumidor ("Atualizado em 16.06.2026").
   - The page says: "Na área da publicidade é a entidade reguladora, fiscalizando e instruindo processos de contraordenação." The fetch tool relayed this quote.
   - I left it out of C3 for two reasons: the brief asks for the smallest wording, and it would need a new entry in PB8's Sources list, which is outside the text P105 names.
   - I did not open anything showing whether the DGC applies the influencer-disclosure rules specifically.
   - The 2019 portugal.gov.pt guide page I also opened names no authority.
   - The Influencer Legal Hub's Portugal country page was not checked, because no search returned it.
   - Proposed row: A3 names the DGC with this source, and a Sources entry is added.
2. **The register contradicts itself.** `case-facts.md` sets Portugal in its P102 section, but two other entries still treat her country as free:
   - Its final "Left free" section says: "Her country, city, household and income. PB8 works its register for the EU, the UK and the US without fixing her country unless it must."
   - The "Set by PB8" entry says: "Left free: her country of residence and tax (A3, T1, T2 open)".
   - Both need updating. "Left free" should drop "country". The PB8 entry should say that A3, T1 and T2 stay open under Portuguese rules (P102/P105).
3. **E1 (PB8 line 288): a possible audit point, not an error.** The status "meet all three" is still valid. However, the EU column cites GDPR art. 3(2)(a), which covers controllers outside the EU. A controller living in Portugal would fall under art. 3(1). I did not check this against the GDPR text, and the column is reader-facing, so I left it unchanged for the next audit.

Searches run: "Influencer Legal Hub Portugal consumer authority European Commission" and "Direção-Geral do Consumidor influenciadores digitais publicidade guia consumidor.gov.pt". Both fetched URLs came verbatim from those searches: the portugal.gov.pt guide page (29 Mar 2019) and the gov.pt DGC entity page.
