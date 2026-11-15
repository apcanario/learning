---
audit: correction check (docs/public-courses.md §3 rule 12; step 1b of row W-BW1)
date: 2026-11-15
units: PB8 (P107)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: claude-opus-5-5 (stated by the checker)
note: saved verbatim from the checker's returned text; its Write tool refused a report file, so the chat saved it
---

# Correction check: P107 (PB8, register line A3), row W-BW1 step 1b, 15 Nov 2026

## Result

Decreto-Lei 109-G/2021 (art. 5) amended art. 19 of Decreto-Lei 57/2008, in force since 28 May 2022. A3 cites the Banco de Portugal copy, which runs only to DL 9/2021.
- A3's three Portuguese quotations still occur in the current 19(3).
- Its paraphrase of 19(1) leaves out the third authority.
- It also leaves out 19(3)'s new proviso, "sem prejuízo das competências especificas atribuídas a outras entidades".

PB8 needs three changes. The DGC is still the advertising authority and may still ask ASAE to intervene, so the register and the later briefs are unaffected.

## Art. 19(1) and 19(3) now, and where read

**Source 1:** Procuradoria-Geral Distrital de Lisboa legislation database, "DL n.º 57/2008, de 26 de Março", https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1067&tabela=leis (WebSearch result in this run, opened 15 Nov 2026).
- Amending acts listed: DL 205/2015, DL 9/2021, DL 109-G/2021, Lei 10/2023.
- Version shown: "5ª versão - a mais recente (Lei n.º 10/2023, de 03/03)".
- No last-update date on the page, only "© Copyright 2026".
- History under art. 19: only "DL n.º 109-G/2021, de 10/12"; the only earlier version listed is the 1ª versão (DL 57/2008).

Current text (given in full because the task asks for it):
- 19(1): "A autoridade administrativa competente para ordenar as medidas previstas no artigo seguinte é a Autoridade de Segurança Alimentar e Económica (ASAE), a entidade reguladora do setor no qual ocorra a prática comercial desleal ou a entidade fiscalizadora de mercado setorialmente competente."
- 19(3): "Tratando-se de uma prática comercial desleal em matéria de publicidade, a autoridade administrativa competente para aplicar as medidas previstas no artigo seguinte é a Direção-Geral do Consumidor (DGC), que pode solicitar a intervenção da ASAE para a efetiva execução da sua ação, sem prejuízo das competências especificas atribuídas a outras entidades." ("especificas" is as in the source.)

**Source 2, the amending act itself:**
- PGDL, DL 109-G/2021 art. 5.º, https://pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=3539A0010&ficha=1&nid=3539&nversao=&pagina=1&so_miolo=&tabela=leis (WebSearch result, opened 15 Nov 2026). It reads: "Os artigos 3.º, 7.º, 8.º, 9.º, 10.º, 14.º e 19.º do Decreto-Lei n.º 57/2008 ... passam a ter a seguinte redação". Its 19(1) and 19(3) are identical to Source 1.
- CentralGest copy of the act, https://www.centralgest.com/documentos/blog/DL-109-g2021.pdf (WebSearch result, opened 15 Nov 2026). Header: "Diário da República, 1.ª série, N.º 238, 10 de dezembro de 2021". Same art. 5 and the same 19(1) and 19(3). Entry into force: "entra em vigor a 28 de maio de 2022". It does not republish DL 57/2008.

**Not checked:**
- The official DR PDF https://files.dre.pt/1s/2021/12/23801/0000200052.pdf: the fetch was refused by the permission check and was not retried.
- The DR pages diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2008-34454075 and …/dr/detalhe/decreto-lei/57-2008-246504: both returned only "JavaScript is required".

PGDL is a public body, but its consolidated text does not replace the Diário da República. Two independent sources agree word for word.

**Later acts:**
- DL 109-G/2021 changed art. 19(1) and 19(3) as above. It also rewrote 19(2), which now names the Banco de Portugal, the CMVM and the ASF.
- Lei 10/2023 (3 Mar 2023) amended DL 57/2008 but not art. 19. PGDL's art. 19 history lists only DL 109-G/2021. The MLGTS alert of 29 Mar 2023 cites only art. 21(2)-(3).
- After Lei 10/2023, no amending act was found. PGDL marks Lei 10/2023 "a mais recente", but the page is undated. No Portuguese transposition of Directive (EU) 2024/825 (deadline 27 Mar 2026) was found. The one 2026 DR PDF the searches returned, DL 171/2026 of 26 Aug 2026, does not touch DL 57/2008. This is a negative search result, not confirmed on the DR.

## Change 1 (PB8.md line 272, register A3)

1. **Current** (PB8.md, `grep -cF` = 1):
`"que pode solicitar a intervenção da ASAE" (which may ask ASAE to intervene); otherwise it is ASAE or the sector regulator (art. 19(1)) (consolidated text to DL 9/2021, Banco de Portugal copy, opened 13 Nov 2026)`

2. **Replacement:**
`"que pode solicitar a intervenção da ASAE" (which may ask ASAE to intervene), "sem prejuízo das competências especificas atribuídas a outras entidades" (without prejudice to powers given to other bodies); otherwise it is ASAE, the sector regulator or the market-surveillance body competent for the sector (art. 19(1)) (wording given by Decreto-Lei 109-G/2021, art. 5, in force since 28 May 2022; consolidated text to Lei 10/2023, Procuradoria-Geral Distrital de Lisboa legislation database, opened 15 Nov 2026)`

3. **Verdict: current text FAIL; replacement PASS.** Source: PGDL consolidated DL 57/2008, art. 19, opened 15 Nov 2026 (page undated, © 2026).
   - 19(1) now ends "ou a entidade fiscalizadora de mercado setorialmente competente". A3 leaves out this third authority.
   - 19(3) now adds "sem prejuízo das competências especificas atribuídas a outras entidades".
   - A3's cited copy predates the amendment.
   - A3's other quotations still occur unchanged.

4. **Syllabus: no contradiction.**
   - register-case-facts.md line 114 says: "A3 names the Direção-Geral do Consumidor as Portugal's advertising regulator, which may ask ASAE to intervene (Decreto-Lei 57/2008, art. 19(3)), and is to do by Mon 5 Jul 2027". It is still true and needs no change.
   - The brief asks for "the EU's unfair-commercial-practices rules and the national regulator that applies them". The DGC is still that regulator.
   - F59: "PB9 builds its deal rules on clause 7 and A1–A3". The authority, the to-do and the date Mon 5 Jul 2027 are unchanged.
   - F61 and DD-PB2 use tax inputs only.
   - The replacement contains no em dash.

## Change 2 (PB8.md line 372, Sources)

1. **Current** (`grep -cF` = 1):
`- Decreto-Lei n.º 57/2008, de 26 de março (unfair commercial practices), art. 19, consolidated text to Decreto-Lei n.º 9/2021 (Banco de Portugal copy; it does not replace the Diário da República text). https://www.bportugal.pt/sites/default/files/anexos/legislacoes/459417805_1.doc.pdf`

2. **Replacement** (two lines):
`- Decreto-Lei n.º 57/2008, de 26 de março (unfair commercial practices), art. 19, consolidated text to Lei n.º 10/2023 (Procuradoria-Geral Distrital de Lisboa legislation database; it does not replace the Diário da República text), opened 15 Nov 2026. https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1067&tabela=leis`
`- Decreto-Lei n.º 109-G/2021, de 10 de dezembro, art. 5 (amends arts. 3, 7, 8, 9, 10, 14 and 19 of Decreto-Lei n.º 57/2008; in force 28 May 2022) (Procuradoria-Geral Distrital de Lisboa legislation database), opened 15 Nov 2026. https://pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=3539A0010&ficha=1&nid=3539&nversao=&pagina=1&so_miolo=&tabela=leis`

3. **Verdict: PASS.**
   - PGDL: "5ª versão - a mais recente (Lei n.º 10/2023, de 03/03)".
   - Art. 5 lists "19.º" among the articles it rewrites.
   - The CentralGest copy gives the date in force: "entra em vigor a 28 de maio de 2022".
   - The Banco de Portugal copy is dropped because A3 no longer cites it.

4. **Syllabus:** nothing relies on this line.

## Change 3 (PB8.md, Unsure list, new note after line 451)

1. **Anchor** (end of line 451, `grep -cF` = 1):
`whether her own list is such an establishment is not decided here. The EU, UK and US columns, §6 and the templates are unchanged.`

2. **Replacement:** the anchor unchanged, then a new line below it, before the blank line that precedes the Erratum paragraphs:
`- Correction 2026-11-15, found by the W-BW1 correction check (P107): Decreto-Lei 109-G/2021, art. 5, in force since 28 May 2022, rewrote art. 19 of Decreto-Lei 57/2008. Register line A3 now gives 19(1) as ASAE, the sector regulator or the market-surveillance body competent for the sector, and adds 19(3)'s proviso "sem prejuízo das competências especificas atribuídas a outras entidades". The DGC is still the authority in advertising and may still ask ASAE to intervene. Read in the consolidated text to Lei 10/2023 on the Procuradoria-Geral Distrital de Lisboa legislation database (15 Nov 2026), which Sources now gives in place of the Banco de Portugal copy. Lei 10/2023 did not change art. 19. No later amending act was found, and the Diário da República's own consolidated text needs JavaScript and was not read. A3's to-do, its date, the EU, UK and US columns, §6 and the templates are unchanged.`

3. **Verdict: PASS.** Same sources as Change 1. The note settles line 451's "later amendments, including DL 109-G/2021, were not checked".
   - Confirm the attribution "W-BW1 correction check (P107)" against the backlog. corrections.md is headed "step 1b of row W-BW1".
   - If it is wrong, use the neutral form `- Correction 2026-11-15 (P107): ...`.

4. **Syllabus:** nothing relies on the Unsure list.

## New

1. **A8-private.md (private unit, outside this row).** Line 113 and R17 (line 232) say that art. 19(3) is "as amended by Decreto-Lei 109-G/2021". That is correct, and A8's quoted fragment "é a Direção-Geral do Consumidor (DGC)" matches the current text. But line 113 cites, for that wording, the Banco de Portugal copy "which carries amendments to Decreto-Lei 9/2021 only". Proposal: re-point line 113 and Sources line 307 to the PGDL consolidated text. This is a citation fix, not an error of substance.
2. **Out-of-date copies.** The Banco de Portugal and Madeira copies that the two earlier checks treated as "unamended" both predate DL 109-G/2021. Any unit that cites them for arts. 3, 7, 8, 9, 10, 14, 19 or 21 of DL 57/2008 should be re-read against PGDL.
3. **Directive (EU) 2024/825.** No Portuguese transposition act was found. If one has been published, it would likely amend DL 57/2008. PB8's six-month staleness check should look for it.

Sources opened in this run:
- https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1067&tabela=leis
- https://pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=3539A0010&ficha=1&nid=3539&nversao=&pagina=1&so_miolo=&tabela=leis
- https://www.centralgest.com/documentos/blog/DL-109-g2021.pdf
- https://www.mlgts.pt/xms/files/site_2018/Newsletters/2023/Lei_n.o_10-2023_de_3_de_marco_relativa_a_defesa_dos_consumidores_-_Legal_Alert_ML_-PT-.pdf
- https://files.diariodarepublica.pt/1s/2026/08/16500/0001000051.pdf (DL 171/2026; not relevant)
