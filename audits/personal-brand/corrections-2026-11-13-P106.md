---
audit: correction check (docs/public-courses.md §3 rule 12; step 1b of row W-PB10)
units: PB8 (P106 a, b, c), PB9 (d), PB1 (e); register
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk; live search)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB9/W-PB10 chat in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: a to e PASS, no syllabus conflict; 3 new items (one left as P107; two need no change)
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/correction-check.md`), copied unchanged by script before any change was applied. The exact strings applied are its `out/edits.json`.

Model: claude-opus-5-5

# P106 correction check, 2026-11-13

Verdict: all five items (a–e) PASS, with no conflict with any syllabus document. Thirteen changes across PB8, PB9, PB1 and case-facts.md are in `out/edits.json`. A script confirmed that each file's list applies in order to a copy, with every Current occurring exactly once at its turn. PB5 is cited but not changed.

Sources opened (each a URL that a WebSearch in this run returned verbatim):
- Decreto-Lei 57/2008, consolidated text, Banco de Portugal: https://www.bportugal.pt/sites/default/files/anexos/legislacoes/459417805_1.doc.pdf (also the original 2008 text, …/471885900_1.doc.pdf)
- GDPR, EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
- CTT tariff PDF: https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf
- Not checked: diariodarepublica.pt pages for DL 57/2008 and DL 109-G/2021, both returning only "JavaScript is required" (not retried).

## a1 · PB8-voice-disclosure-and-the-rules.md

Current:
```
(in advertising, it is the regulator) (gov.pt, updated 16 Jun 2026, checked 13 Nov 2026);
```
Replacement:
```
(in advertising, it is the regulator) (gov.pt, updated 16 Jun 2026, checked 13 Nov 2026); under Decreto-Lei 57/2008, art. 19(3), for an unfair practice "em matéria de publicidade" (in advertising) the authority competent "para aplicar as medidas previstas no artigo seguinte" (to apply the measures of art. 20) is the DGC, "que pode solicitar a intervenção da ASAE" (which may ask ASAE to intervene); otherwise it is ASAE or the sector regulator (art. 19(1)) (consolidated text to DL 9/2021, Banco de Portugal copy, opened 13 Nov 2026);
```

PASS. Source: Decreto-Lei 57/2008, consolidated text (marked "Diploma consolidado"; amendment notes to DL 205/2015 and DL 9/2021), Banco de Portugal copy, reached from a WebSearch result. Art. 19(3): "Tratando-se de uma prática comercial desleal em matéria de publicidade, a autoridade administrativa competente para aplicar as medidas previstas no artigo seguinte é a Direcção-Geral do Consumidor (DGC), que pode solicitar a intervenção da ASAE para a efetiva execução da sua ação." Art. 19(1): "A autoridade administrativa competente para ordenar as medidas previstas no artigo seguinte é a Autoridade de Segurança Alimentar e Económica (ASAE) ou a entidade reguladora do sector". The answer to (a): ASAE does not sit beside the DGC as advertising authority. It is the general authority, and in advertising matters the DGC may ask it to intervene. The Diário da República page (diariodarepublica.pt/dr/detalhe/decreto-lei/57-2008-246504) returned only "JavaScript is required": not checked, not retried. Amendments after DL 9/2021 (e.g. DL 109-G/2021, whose DR page also needs JavaScript) were not checked. Both gaps are stated in the note.
Syllabus: no conflict. Brief PB8: "the EU's unfair-commercial-practices rules and the national regulator that applies them". The register's line that "A3 names the Direção-Geral do Consumidor as Portugal's advertising regulator" still holds, and r-b adds ASAE's role. PB9 D1 "A3 read first" is unaffected.

## a2 · PB8-voice-disclosure-and-the-rules.md

Current:
```
- Direção-Geral do Consumidor, entity page (gov.pt, Portuguese government portal), updated 16 Jun 2026. https://www.gov.pt/entidades/direcao-geral-do-consumidor
```
Replacement:
```
- Decreto-Lei n.º 57/2008, de 26 de março (unfair commercial practices), art. 19, consolidated text to Decreto-Lei n.º 9/2021 (Banco de Portugal copy; it does not replace the Diário da República text). https://www.bportugal.pt/sites/default/files/anexos/legislacoes/459417805_1.doc.pdf
- Direção-Geral do Consumidor, entity page (gov.pt, Portuguese government portal), updated 16 Jun 2026. https://www.gov.pt/entidades/direcao-geral-do-consumidor
```

PASS (the source line for a1, the law the correction names). Syllabus: no conflict.

## b1 · PB8-voice-disclosure-and-the-rules.md

Current:
```
she reads what it publishes on advertising before the first deal (13 Nov 2026)
```
Replacement:
```
she reads what it publishes on advertising by Mon 5 Jul 2027, before brand deals can open with upload 14 on Tue 6 Jul 2027 (PB9 D1; Mara, fictional) (13 Nov 2026)
```

Rests on the units and register. PB8 D3: "**to do** (an action with a date)". PB9 D1: "Brand deals from Season 3 (upload 14, Tuesday 6 July 2027)". PB8 D1 clause 7 and register: "No brand deal ... in Seasons 1 and 2". Register PB1: checkpoint "5 July 2027". 5 Jul 2027 is a Monday (26 weeks after Mon 4 Jan 2027), the last day before deals can open. PASS.
Syllabus: no conflict. The date is a deadline ("by") and not an item handed to the Q2 review, so the PB10 brief's list ("the items earlier units hand the review besides PB1's seven reads: PB2's ..., PB3's ..., and PB4's three items") is unchanged. PB8 D3 still holds: "no time for these lines is in PB4's run-in hours, and where they go in her log is left to PB10's review". The register line must follow (r-b).

## c1 · PB8-voice-disclosure-and-the-rules.md

Current:
```
not art. 3(2)(a), which is for a controller "not established in the Union";
```
Replacement:
```
not art. 3(2)(a), which is for a controller "not established in the Union"; recital 22: "Establishment implies the effective and real exercise of activity through stable arrangements", and their legal form "is not the determining factor" (EUR-Lex, OJ L 119, 4 May 2016);
```

PASS. EUR-Lex, CELEX 32016R0679 (OJ L 119/1, 4.5.2016), reached from a WebSearch result. Recital (22): "Any processing of personal data in the context of the activities of an establishment of a controller or a processor in the Union should be carried out in accordance with this Regulation, regardless of whether the processing itself takes place within the Union. Establishment implies the effective and real exercise of activity through stable arrangements. The legal form of such arrangements, whether through a branch or a subsidiary with a legal personality, is not the determining factor in that respect." E1 gains only the definition. It draws no conclusion on whether Mara's list is an establishment, and the note says that this is not decided.
Syllabus: no conflict. Brief PB8: "data protection for an email list". The register says "E1 gives GDPR art. 3(1) as her EU test", which is unchanged.

## c2 · PB8-voice-disclosure-and-the-rules.md

Current:
```
- GDPR, art. 13, as adopted (legislation.gov.uk). https://www.legislation.gov.uk/eur/2016/679/article/13/adopted/data.htm
```
Replacement:
```
- GDPR, art. 13, as adopted (legislation.gov.uk). https://www.legislation.gov.uk/eur/2016/679/article/13/adopted/data.htm
- GDPR, recital 22, as published in OJ L 119, 4 May 2016 (EUR-Lex). https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
```

PASS (the source line for c1). Syllabus: no conflict.

## n-PB8 · PB8-voice-disclosure-and-the-rules.md

Current:
```
- Correction 2026-11-13 (round 2), found by the P105 check: register line A3 now names Portugal's advertising regulator, the Direção-Geral do Consumidor, from its gov.pt entity page (updated 16 Jun 2026, opened 13 Nov 2026), and moves from open to to do; Sources gains that page; register line E1's status now gives GDPR art. 3(1) (an establishment in the Union) as the EU test for her own list in place of art. 3(2)(a), and names the art. 2(2)(c) household exception, both read in the Regulation as adopted (legislation.gov.uk, Chapter I); the EU, UK and US columns, §6.6 and the templates are unchanged.
```
Replacement:
```
- Correction 2026-11-13 (round 2), found by the P105 check: register line A3 now names Portugal's advertising regulator, the Direção-Geral do Consumidor, from its gov.pt entity page (updated 16 Jun 2026, opened 13 Nov 2026), and moves from open to to do; Sources gains that page; register line E1's status now gives GDPR art. 3(1) (an establishment in the Union) as the EU test for her own list in place of art. 3(2)(a), and names the art. 2(2)(c) household exception, both read in the Regulation as adopted (legislation.gov.uk, Chapter I); the EU, UK and US columns, §6.6 and the templates are unchanged.
- Correction 2026-11-13, found by the W-PB9 correction check (P106): register line A3 now gives Decreto-Lei 57/2008, art. 19(3): in advertising the Direção-Geral do Consumidor is the competent authority and may ask ASAE to intervene, ASAE being the authority otherwise (art. 19(1)); read in the Banco de Portugal consolidated copy, which notes amendments to DL 9/2021; the Diário da República page needs JavaScript and was not read, and later amendments, including DL 109-G/2021, were not checked; Sources gains that copy. A3's to-do now has a date, Mon 5 Jul 2027, the day before brand deals can open (PB9 D1). E1 now gives recital 22's definition of an establishment, read on EUR-Lex, which Sources gains; whether her own list is such an establishment is not decided here. The EU, UK and US columns, §6 and the templates are unchanged.
```

Note line for PB8 (P106), anchored on its last unsure-list line. Syllabus: no conflict.

## d1 · PB9-monetisation-what-pays-at-each-audience-size.md

Current:
```
[CTT, Tarifário de serviços postais, Nov 2020](https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf): Apartado, concessão anual, 58.00 € before VAT;
```
Replacement:
```
[CTT, Preços 2020, novembro/2020](https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf): Apartados, Singulares (individuals), concessão anual, 58.00 € before VAT;
```

PASS. The CTT PDF, reached from a WebSearch result, is headed "Preços 2020" and dated "novembro/2020". The phrase "Tarifário de serviços postais" does not appear in it. Under "APARTADOS (a)", the "Singulares" block gives "Concessão Anual 58,00 €" ("Coletivos": 80,00 €). Note (a): "Preços sujeitos a aplicação de IVA à taxa legal em vigor."
Syllabus: no conflict. The register (PB9) says "CTT PO box for an individual, 58.00 € + VAT a year on the Nov 2020 tariff", which agrees. The amount and date are unchanged, and PB1 D2 and DD-PB2's inputs are untouched. F72 (the platform-official label) is left alone.

## d2 · PB9-monetisation-what-pays-at-each-audience-size.md

Current:
```
- CTT, "Tarifário de serviços postais", Nov 2020.
```
Replacement:
```
- CTT, "Preços 2020", novembro/2020.
```

PASS (same source: its heading). Syllabus: no conflict.

## n-PB9 · PB9-monetisation-what-pays-at-each-audience-size.md

Current:
```
- Correction 2026-11-13, found by the W-PB9 correction check: CTT's tariff is dated Nov 2020, not 1 Nov 2020 (D2 V17, Sources, this list); the PDF shows "Preços 2020" and "novembro/2020", and "1nov" is only its file name.
```
Replacement:
```
- Correction 2026-11-13, found by the W-PB9 correction check: CTT's tariff is dated Nov 2020, not 1 Nov 2020 (D2 V17, Sources, this list); the PDF shows "Preços 2020" and "novembro/2020", and "1nov" is only its file name.
- Correction 2026-11-13, found by the W-PB9 correction check (P106): D2 V17 and Sources cited CTT's tariff as "Tarifário de serviços postais", a phrase the PDF does not contain; its heading is "Preços 2020" (novembro/2020), and V17 now says the 58.00 € is the annual rate under "Singulares" (individuals); the amount is unchanged.
```

Note line for PB9 (P106). Syllabus: no conflict.

## e1 · PB1-what-to-expect-odds-timeline-cost.md

Current:
```
the cap stands unless the converted price exceeds what remains under it (PB9 D2 V17) |
```
Replacement:
```
the cap stands unless the converted price exceeds what remains under it (PB9 D2 V17); if a later audio check fails and the microphone is bought (PB5 §2, §10), that line is spent, the address is paid from what then remains under the cap (the contingency and any unspent part of the tripod-or-clamp line), and if that does not cover both, this D2 is corrected (PB9 D3) |
```

Rests on the units and register. PB5 §2: "the check is re-run if a piece needs a noisier tool". PB5 §10: "PB1's microphone line stays unspent unless the check fails on a later piece", and the table: "The audio check fails twice, after the free fixes". PB1 D2: "Contingency | 11 USD | The remainder of the cap"; "Tripod or clamp | up to 40 USD". PB9 D3: "if it exceeds what remains under the cap, PB1's D2 is corrected". Register PB1: "a clip-on microphone (99.00 USD ...) only if PB5's audio check fails". PASS. The change adds no price, rate or exchange rate.
Syllabus: no conflict. The PB9 and DD-PB2 briefs rely on PB9's income lines and costs, and the default (the unspent microphone line) stands. The register line must follow (r-e).

## n-PB1 · PB1-what-to-expect-odds-timeline-cost.md

Current:
```
Correction 13 Nov 2026, found by the W-PB7 figure re-check: D3's decision figure caption now places the 1.86% base rate in §2 and D1 row Y4, within 360 days and for channels whose video count grew by 1 to 11 (it said §2 and §5, a year), ties rows Y2 and Y3 to the format verdict, and names the above-median rule as hers, resting on the two YouTube Help statements.
```
Replacement:
```
Correction 13 Nov 2026, found by the W-PB7 figure re-check: D3's decision figure caption now places the 1.86% base rate in §2 and D1 row Y4, within 360 days and for channels whose video count grew by 1 to 11 (it said §2 and §5, a year), ties rows Y2 and Y3 to the format verdict, and names the above-median rule as hers, resting on the two YouTube Help statements.
- Correction 2026-11-13, found by the W-PB9 correction check (P106): D2's postal-address line now says what pays it if a later audio check fails and the microphone is bought (PB5 §2, §10): what then remains under the 150 USD cap, the contingency and any unspent part of the tripod-or-clamp line, with D2 corrected if that does not cover both (PB9 D3); no price, rate or source is added, and the cap is unchanged.
```

Note line for PB1 (P106), anchored on its last line, the unsure list's closing correction paragraph. Syllabus: no conflict.

## r-b · case-facts.md

Current:
```
A3 names the Direção-Geral do Consumidor as Portugal's advertising regulator and is to do before the first deal, P105 round 2)
```
Replacement:
```
A3 names the Direção-Geral do Consumidor as Portugal's advertising regulator, which may ask ASAE to intervene (Decreto-Lei 57/2008, art. 19(3)), and is to do by Mon 5 Jul 2027, before brand deals can open, P105 round 2, P106)
```

Register line that follows a1 and b1 (PB8 section, "Left free" bullet). Syllabus: no conflict.

## r-e · case-facts.md

Current:
```
paid from PB1's unspent microphone line (D2 V17; PB1 D2).
```
Replacement:
```
paid from PB1's unspent microphone line (D2 V17; PB1 D2); if a later audio check buys the microphone, from what then remains under PB1's cap, with PB1's D2 corrected if that does not cover both (PB1 D2, corrected 13 Nov 2026, P106).
```

Register line that follows e1 (PB9 section, postal-address bullet). Syllabus: no conflict.

## New

- (a) residue: the current wording of DL 57/2008 art. 19 after DL 109-G/2021 and any later act was not checked, because the Diário da República needs JavaScript. A later check that can open the consolidated DR text should confirm art. 19(1) and 19(3). This could be a proposed backlog row.
- The CTT PDF also lists "Renovação / Realuguer 38,00 €" (Singulares). Year one needs only the annual concession, so nothing is changed. If the address runs into year two, the renewal rate is the line to check, together with the current price.
- PB9 still writes "CTT's 2020 tariff" / "CTT's tariff of Nov 2020" in D3, the costs row and the unsure list. These are accurate and are not changed.
