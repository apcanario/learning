---
audit: correction check, round 2 (docs/public-courses.md §3 rule 12 (f); step 7b of row W-PB9)
units: PB7 (R2-1, its Q2 post count), PB9 (R2-2, CTT's tariff date and label)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk; live search)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB9/W-PB10 chat in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: R2-1 PASS; R2-2 date PASS, label FAIL (not applied, flag F72); no syllabus conflict
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/correction-check.md`), copied unchanged by script before any change was applied. The exact strings applied are its `out/edits.json`.

Model: claude-opus-5-5

# W-PB9 correction check, round 2 (R2-1, R2-2), 13 Nov 2026

Sources read: only the files in /home/claude/stage/corr4/. Web: one WebSearch; one WebFetch of the CTT PDF URL that the search returned verbatim. The fetch succeeded.

## R2-1 · PB7: Q2 post count gets the guide-build condition

**Which strings are Q1 and which Q2.** Only one PB7 string gives a Q2 count:
- D2 closing paragraph (line 258): "when 39 more posts (25 Reels, 14 carousels; derived from the same post order) give each format a second quarter". This is **Q2**: it changes.
- IG1 "39 planned (27 Reels, 12 carousels)" sits in the column headed "Mara, Q1 review, Mon 5 Apr 2027", and D2's opening (line 240) gives "39 in all (27 Reels, 12 carousels ...)" for the "first quarter". Both are **Q1**: unchanged. The correction calls IG1 a Q2 figure. It is not.
- IR1's "27 Reels and 12 carousels in Q1" is Q1: unchanged.

### R2-1a
- File: `PB7-how-instagram-growth-works.md`
- Current (count 1): `39 more posts (25 Reels, 14 carousels; derived from the same post order)`
- Replacement: `39 more posts (25 Reels, 14 carousels; derived from the same post order; 31, with 17 Reels, if PB9's guide build is decided at the Q1 review)`
- **PASS.** Register line 94: "25 and 14 in Q2 (17 and 14 if PB9's guide build is decided at the Q1 review: two Reels fewer in each of the four fortnights cut on 25 Apr, 9 May, 23 May and 6 Jun 2027)". PB1 line 306: "39 posts, 31 in Q2 if PB9's guide build is decided at the Q1 review". PB9 D1 line 185: "in each of those fortnights two Reels are not made (six posts become four)". Arithmetic: 4 × 2 = 8 Reels; 25 − 8 = 17; 39 − 8 = 31; carousels stay at 14.
- **Syllabus: no conflict.** It now matches the register and PB1. IR11 ("her carousels' median non-follower views across Q1 and Q2") still works: both formats still get a second quarter. brief-PB7 "Gives: the Instagram rows of PB10's metrics sheet" and brief-PB10 ("that procedure run on Mara's first two quarters with her invented numbers labelled") need both Q2 cases available, and they are.

### R2-1-note
- File: PB7. Anchor: the last line of the unsure list (count 1): `- Fresh check 2026-11-12 (Opus 5.5; a Fable 5.1 fresh check is owed, P49): fix · 3 errors, 9 should-fix, 7 minor; all applied as the report gives them; report `audits/personal-brand/fresh-check-PB7.md``
- Replacement: that line, then a newline, then
  `- Correction 2026-11-13, found by the W-PB9 correction check: the Q2 count at the end of D2 now gives 31 posts (17 Reels) if PB9's guide build is decided at the Q1 review, as PB1 D3 read 1 and the register do; the Q1 figures (D2's opening, IG1) are unchanged.`
- PASS. Syllabus: no conflict.

## R2-2 · PB9: CTT tariff date and label

**Source check.** WebSearch returned https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf verbatim, and it was fetched. The PDF's dates are "Preços 2020" (section header and title) and "novembro/2020" (issue date under the title). The only other date is "podendo ser utilizados até dia 31 de dezembro de 2020 os envelopes ...". No "1 de novembro" appears. Apartado: "Singulares: Concessão Anual 58,00 €" and "Coletivos: Concessão Anual 80,00 €", footnote (a) "Preços sujeitos a aplicação de IVA à taxa legal em vigor". The 58.00 € + VAT figure holds.

### R2-2a (D2 V17)
- File: `PB9-monetisation-what-pays-at-each-audience-size.md`
- Current (count 1): `[CTT, Tarifário de serviços postais, 1 Nov 2020](`
- Replacement: `[CTT, Tarifário de serviços postais, Nov 2020](`
- **PASS.** "novembro/2020"; no day is given. Syllabus: no conflict. PB1's note already says "CTT's tariff dated November 2020", and the register leaves "the price of the postal address" free.

### R2-2b (Sources)
- Current (count 1, after R2-2a): `- CTT, "Tarifário de serviços postais", 1 Nov 2020.`
- Replacement: `- CTT, "Tarifário de serviços postais", Nov 2020.`
- PASS (same source). Syllabus: no conflict.

### R2-2c (Unsure list)
- Current (count 1, after R2-2a/b): `CTT's tariff of 1 Nov 2020`
- Replacement: `CTT's tariff of Nov 2020`
- PASS (same source). Syllabus: no conflict.
- Line 261 ("on CTT's 2020 tariff") has no "1 Nov" and is not touched.

### R2-2d (label): not applied
- Current: `Platform-official, 2020 tariff; stale` (V17 grade cell, count 1)
- Proposed: `operator's own tariff, 2020 tariff; stale`
- **FAIL against the unit's label set.** PB9 §1 area, line 12: "The evidence labels are the ones PB1 §1 defines (platform-official, vendor, correlational, survivor sample, peer-reviewed, anecdote or documented creator case, derived) and the two PB8 added (primary law, regulator guidance)." "Operator's own tariff" is not in that set, so using it would add a label. None of the set's labels fits a postal operator's price list:
  - PB1 §1 defines Platform-official as "YouTube's or Instagram's own help pages, or a statement the company made to the press".
  - Vendor is "a dataset published by a company that sells tools or services to creators or brands".
  
  The correction's condition ("pick the label that fits that set") cannot be met, so no label edit is proposed and the label stays unchanged in edits.json. See New 1.

### R2-2-note
- Anchor: the last line of the PB9 unsure list (count 1): `- Fresh check 2026-11-13 (Opus 5.5; a Fable 5.1 fresh check is owed, P49): fix · 3 errors, 5 should-fix, 10 minor; all applied as the report gives them; figures 1 and 4 corrected and re-checked, figures 2 and 3 passed; report `audits/personal-brand/fresh-check-PB9.md`.`
- Replacement: that line, then a newline, then
  `- Correction 2026-11-13, found by the W-PB9 correction check: CTT's tariff is dated Nov 2020, not 1 Nov 2020 (D2 V17, Sources, this list); the PDF shows "Preços 2020" and "novembro/2020", and "1nov" is only its file name.`
- PASS. Syllabus: no conflict. The note covers only the date change that was applied.

## edits.json
`out/edits.json` holds, in order:
- PB7: R2-1a, R2-1-note
- PB9: R2-2a, R2-2b, R2-2c, R2-2-note

A script applied each file's list in order to a copy. Every `current` had count 1 at the point it was applied. Afterwards PB9 contains "1 Nov 2020" only inside its own note.

## New
1. **PB9 V17 label (for Pedro to decide).** The unit's declared label set has no label for a non-platform provider's own price list. "Platform-official" on V17 is wrong by PB1 §1's definition. Strictly read, so is its use on Gumroad, Etsy, beehiiv and Amazon pages, which are not "YouTube's or Instagram's own" pages. Two ways to fix it:
   - Define a label (e.g. "provider's own price list") in PB9 §1 / PB1 §1 and apply it.
   - Widen PB1 §1's definition of Platform-official.
   
   Either change goes beyond this correction.
2. **PB9 V17 title.** The fetched PDF gives its title as "Preços 2020"; PB9 cites "Tarifário de serviços postais". This rests on a summarised fetch and was not changed.
3. **PB9 V17 tier.** The 58.00 € concession is the "Singulares" (individual) rate; "Coletivos" pay 80,00 €. PB1's note already says "Singulares", PB9 does not. Mara as an individual fits 58.00 €, so nothing changes. Noted only.
