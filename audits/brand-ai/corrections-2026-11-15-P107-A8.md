---
audit: correction check, second round (docs/public-courses.md §3 rule 12; step 1b (f) of row W-BW1)
date: 2026-11-15
units: A8 (found by the P107 check, audits/personal-brand/corrections-2026-11-15-P107.md, section New, item 1)
course: brand-ai · A · Building a Marketable Personal Brand
model: claude-opus-5-5 (stated by the checker)
note: saved verbatim from the checker's returned text; the checker could not write files
---

# Corrections check: A8-private.md, DL 57/2008 citation (W-BW1 step 1b (f)), 15 Nov 2026

**Overall:** the wording A8 attributes to the 2021 amendment is right. The amending act confirms it: 19(3) was amended, 8 m) and z) were relettered, and 9(1) was left unchanged. I could not confirm the proposed new source myself. Five WebSearches never returned either PGDL URL (the consolidated DL 57/2008 page, nid=1067, or the DL 109-G/2021 art. 5 page), so under the web rule I could not open them. The re-pointing therefore rests only on the P107 report's reading of those pages.

## Change 1: line 113 (main text)

1. **Current** (line 113, `grep -cF` = 1):
`([Decreto-Lei 57/2008, consolidated text on the Banco de Portugal site](https://www.bportugal.pt/sites/default/files/anexos/legislacoes/459417805_1.doc.pdf), which carries amendments to Decreto-Lei 9/2021 only; art. 9.º, n.º 1, al. c) is unchanged by the later Decreto-Lei 109-G/2021)`

2. **Replacement:**
`([Decreto-Lei 57/2008, consolidated text to Lei 10/2023, Procuradoria-Geral Distrital de Lisboa legislation database](https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1067&tabela=leis), opened 15 Nov 2026; it does not replace the Diário da República text; art. 19.º as worded by Decreto-Lei 109-G/2021, art. 5.º, and art. 9.º, n.º 1, al. c) unchanged by it)`

3. **Verdict: the wording PASSES; the new source is NOT CHECKED.**
   - **Wording.** Read in the copy of DL 109-G/2021 at https://www.centralgest.com/documentos/blog/DL-109-g2021.pdf (WebSearch result in this run, opened):
     - art. 5 rewrites "Os artigos 3.º, 7.º, 8.º, 9.º, 10.º, 14.º e 19.º";
     - its 19(3) reads "é a Direção-Geral do Consumidor (DGC), que pode solicitar a intervenção da ASAE";
     - art. 9 n.º 1 is given only as "1 - […]", so it is unchanged;
     - 8 m) and z) are "[Anterior alínea n)]" and "[Anterior alínea ab)]";
     - in force "a 28 de maio de 2022".
   - **New source.** The PGDL page itself was not opened in this run. The P107 report quotes only art. 19 from it, so the 9(1)(c) quotation has not been read on PGDL by either run. Before filing, confirm on PGDL that the 9(1)(c) text matches. If it cannot be confirmed, keep the clause "art. 9.º, n.º 1, al. c) unchanged by it" as the basis for that quotation, as written in the replacement.

4. **Syllabus: no contradiction.**
   - R17 (line 232) already says "19.º n.º 3 (as amended by DL 109-G/2021)".
   - Lines 154 and 240 cite art. 9(1)(c), which DL 109-G/2021 did not change.
   - "ASAE is the general enforcer" is still true. Since 2021, 19(1) also names the sector regulator and the market-surveillance body. That is an omission, not an error, so no change is made.

## Change 2: line 307 (Sources)

1. **Current** (line 307, `grep -cF` = 1):
`- Decreto-Lei 57/2008, consolidated text to Decreto-Lei 9/2021, Banco de Portugal site. https://www.bportugal.pt/sites/default/files/anexos/legislacoes/459417805_1.doc.pdf`

2. **Replacement:**
`- Decreto-Lei 57/2008, consolidated text to Lei 10/2023, Procuradoria-Geral Distrital de Lisboa legislation database (it does not replace the Diário da República text), opened 15 Nov 2026. https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1067&tabela=leis`

3. **Verdict: NOT CHECKED in this run.** No WebSearch returned this URL. The P107 report says it was opened and quotes "5ª versão - a mais recente (Lei n.º 10/2023, de 03/03)".

4. **Syllabus:** nothing depends on this line.

**On the amending act's art. 5:** line 306 already cites it through the CentralGest copy: "- Decreto-Lei 109-G/2021, 10 Dec 2021 (art. 5.º amends Decreto-Lei 57/2008), copy on the CentralGest site." I checked that copy in this run and it holds. A second line for the PGDL copy of art. 5 (P107 Source 2) is optional.

## Other citations of the outdated copies

- **Banco de Portugal copy:** cited only at lines 113 and 307, which are the two changes above. Nothing else needed.
- **Madeira copy of DL 57/2008:** not cited anywhere. The madeira.gov.pt links at lines 69 and 328 are for Portaria 480-A/2025/1 (the IAS), not DL 57/2008. No change.
- **Other citations of DL 57/2008 without a named copy:** line 154 and R25 (line 240): art. 9(1)(c), unchanged by DL 109-G/2021; R17 (line 232): 8 m), z), 9(1)(c), 19(3), already marked as amended. None needs a change.
- **Unsure list (lines 350–360):** has no entry on DL 57/2008, so there is no stale note to update.

## Sources opened in this run
- https://www.centralgest.com/documentos/blog/DL-109-g2021.pdf (copy of DL 109-G/2021, DR 1.ª série n.º 238, 10 Dec 2021)
