---
audit: correction check, round 2 (docs/public-courses.md §3 rule 12 (f); step 1b of row W-PB9)
units: PB8 (R2-1: register line A3 and Sources; R2-2: register line E1's status)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk; live search)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB9/W-PB10 chat in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: R2-1 PASS, R2-2 PASS (with a limit), no syllabus conflict; 4 new items (register follow-up applied; three left in the Corrections section)
---

The checker's final report, verbatim, returned as text (agents in this session may not write report files) and copied here unchanged before any change was applied. The exact strings applied are its `out/edits.json`.

Model: claude-opus-5-5

Both changes pass, and neither conflicts with a brief. `out/edits.json` holds four edits: R2-1a, R2-1b, R2-2 and the note. A script applied them in order to a copy of PB8. Each Current occurred exactly once at its step, each replacement once after, and the note lands as the new last line. The copy went from 445 to 447 lines. No pipe characters were added to table cells. Only files inside the folder were read, and only `out/edits.json` was written; the script and the applied copy are in /tmp/corr2scripts/.

## R2-1 — A3: Portugal's consumer authority (two edits)

**Source (opened, found by my own WebSearch):** https://www.gov.pt/entidades/direcao-geral-do-consumidor, "Atualizado em 16.06.2026". It says: "Na área da publicidade é a entidade reguladora, fiscalizando e instruindo processos de contraordenação." Its mission includes "promover a política de salvaguarda de direitos dos consumidores". **PASS**: the page supports naming the Direção-Geral do Consumidor (DGC) as the body that regulates advertising in Portugal, which covers ad disclosure.

**Another body?** The opening section of Decreto-Lei 57/2008, Portugal's law implementing the EU unfair-commercial-practices directive, does name one. It was read in a vLex copy behind a paywall, so only that opening part was readable, not the enforcement articles. It says ASAE "ou a entidade reguladora do sector são consideradas autoridades administrativas competentes" in general. In advertising, though, "a autoridade administrativa competente é a Direcção-Geral do Consumidor." So no primary source found puts another body over advertising disclosure. ASAE is the general authority for unfair practices outside advertising.

Not checked:
- the Diário da República page for DL 57/2008 (it returned only "JavaScript is required")
- the Advertising Code's (Código da Publicidade) enforcement article
- any DGC guidance for influencers (found only in secondary reports)

**R2-1a**
- Current: `Open: she lives in Portugal; which authority applies the rules there is not yet checked (13 Nov 2026)`
- Replacement: `To do: she lives in Portugal; the advertising regulator there is the Direção-Geral do Consumidor, which "na área da publicidade é a entidade reguladora" (in advertising, it is the regulator) (gov.pt, updated 16 Jun 2026, checked 13 Nov 2026); she reads what it publishes on advertising before the first deal (13 Nov 2026)`

I used "reads what it publishes on advertising", not round 1's "reads its guidance", because no DGC guidance document was opened.

**R2-1b** (Sources). Alphabetically, "Direção" comes before "Directive", so the entry goes after "Data Protection Commission".
- Current: `- Directive (EU) 2019/1152, art. 9 (LawPlayer copy). https://lawplayer.com/eu/article/32019L1152/art_9`
- Replacement: `- Direção-Geral do Consumidor, entity page (gov.pt, Portuguese government portal), updated 16 Jun 2026. https://www.gov.pt/entidades/direcao-geral-do-consumidor` + newline + the Current line unchanged.

**Syllabus:** No conflict with the PB8, PB9, PB10 or DD-PB2 briefs.
- PB9's brief relies on PB8 for "the disclosure rules PB9's brand deals follow". A3 now gives it a named authority and changes no rule.
- DD-PB2's brief relies on "the open tax and contract questions". T1 and T2 are untouched.
- D3's opening note ("lines that depend on Portuguese rules stay open until they are answered for her") stays true.
- **Register text to update in the same filing chat:** case-facts.md line 114 ("Left free: her tax answers (A3, T1, T2 stay open under Portuguese rules, P102/P105…)") and line 124 ("…with her own lines open under Portuguese rules (P105)") still describe A3 as open. A3 is listed as left free, not set, and P105 itself allows naming it once sourced, so I read this as a needed follow-up edit, not a contradiction. The earlier correction note (PB8 line 445: "no … authority was added") is a dated record and stays as it is.

## R2-2 — E1: Mara's GDPR route

**Source (opened, found by my own WebSearch):** https://www.legislation.gov.uk/eur/2016/679/chapter/I/adopted/data.htm (the GDPR as adopted, Chapter I).
- Art. 3(1): "This Regulation applies to the processing of personal data in the context of the activities of an establishment of a controller or a processor in the Union, regardless of whether the processing takes place in the Union or not."
- Art. 3(2): "…by a controller or processor not established in the Union, where the processing activities are related to:"
- Art. 2(2)(c): "by a natural person in the course of a purely personal or household activity;"
- Art. 4(7): "'controller' means the natural or legal person … which, alone or jointly with others, determines the purposes and means of the processing of personal data".

**PASS, with a limit:** the text supports art. 3(1) as the EU route for a natural person who controls a list run from inside the Union. Art. 3(2)(a) by its terms covers only controllers "not established in the Union". The household exception in art. 2(2)(c) is the only way out. However, Article 4 defines only "main establishment", not "establishment". Recital 22, which explains the term, was not reached on EUR-Lex or legislation.gov.uk; search returned only third-party copies, which I did not use. So the replacement gives the test and does not claim the text alone settles whether her home counts as an establishment.

- Current: `Settled as a working rule: meet all three (§6.6) (13 Nov 2026)`
- Replacement: `Settled as a working rule: meet all three (§6.6). She lives in Portugal (Mara, fictional), so the EU test for her own list is art. 3(1), processing "in the context of the activities of an establishment of a controller or a processor in the Union", not art. 3(2)(a), which is for a controller "not established in the Union"; the GDPR does not apply to "a purely personal or household activity" (art. 2(2)(c)), and she does not treat her list as one (her rule) (13 Nov 2026)`

Only Mara's status cell changes. E1's EU, UK and US columns, §6.6 and the template line E1 (line 345) are unchanged. Art. 3 is already in Sources, and art. 2(2)(c) is already cited in §6.2, so no new Sources entry is needed.

**Syllabus:** No conflict. No brief relies on E1. Register line 112 sets E2–E5, not E1, and nothing in the register sets which GDPR article applies.

## Note (fourth edit)

- Current: `and the EU, UK and US columns and the templates are unchanged.`
- Replacement: the same text, then a newline, then:

`- Correction 2026-11-13 (round 2), found by the P105 check: register line A3 now names Portugal's advertising regulator, the Direção-Geral do Consumidor, from its gov.pt entity page (updated 16 Jun 2026, opened 13 Nov 2026), and moves from open to to do; Sources gains that page; register line E1's status now gives GDPR art. 3(1) (an establishment in the Union) as the EU test for her own list in place of art. 3(2)(a), and names the art. 2(2)(c) household exception, both read in the Regulation as adopted (legislation.gov.uk, Chapter I); the EU, UK and US columns, §6.6 and the templates are unchanged.`

## New

1. **ASAE:** DL 57/2008's opening section (vLex copy, text as published in 2008; later amendments not checked) makes ASAE, or the sector's regulator, the general authority for unfair commercial practices, and the DGC the authority for advertising. If A3 is meant to cover more than ad disclosure, ASAE belongs in it; that would be a separate proposed change.
2. **A3's "to do" has no calendar date.** D3 defines "to do" as "an action with a date", and the new A3 status is tied to "the first deal". E4 already uses "to do" without a date, but a filing chat may want a date set for A3.
3. **Register follow-up:** case-facts.md lines 114 and 124 need A3 moved out of "stay open" when these edits are filed.
4. **Recital 22 not read:** recital 22 (what "establishment" means) was not reached on an allowed primary-source site. If E1 should go further than the test, a later check should open it on EUR-Lex.

Search and page links used: [gov.pt DGC entity page](https://www.gov.pt/entidades/direcao-geral-do-consumidor), [portugal.gov.pt digital advertising guide news, 29 Mar 2019](https://portugal.gov.pt/gc21/comunicacao/noticias/guia-de-boas-praticas-sobre-publicidade-no-meio-digital) (names no regulator), [vLex DL 57/2008](https://vlex.pt/vid/decreto-lei-36610827), [Diário da República DL 57/2008](https://diariodarepublica.pt/dr/detalhe/decreto-lei/57-2008-246504) (not checked: JavaScript only), [GDPR Chapter I as adopted, legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/chapter/I/adopted/data.htm).
