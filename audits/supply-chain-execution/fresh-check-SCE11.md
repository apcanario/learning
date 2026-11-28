---
audit: fresh check
unit: SCE11 · The buying committee
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: Opus 5.5 (claude-opus-5-5)
date: 2026-11-28
chat: https://claude.ai/code/session_01KMmgQzMe8qwXyeLryD2JaE
verdict: keep · 0 errors, 5 should-fix, 18 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Model: claude-opus-5-5

The Write tool refused /home/claude/work/c11/out/report.md ("Subagents should return findings as text"). Nothing was written, so the full report follows.

# Fresh check · SCE11 · The buying committee

**Procedure:**
- audit-units-SKILL.md §3 fresh-check prompt, with the figures paragraph (7).
- Read against: sourcing-standard.md Part 1 and Part 8, brief.txt, case-facts.md, and filed SCE1–SCE10. Started from unsure.md.
- Web: WebSearch first. WebFetch only on addresses a WebSearch in this agent returned verbatim.
- Checked 28 Nov 2026.

## Findings

[should-fix] [accuracy] front matter, intro; Current: "Every study of software buying opened here was read in abstract only, except the Gartner and ARC pages, read in full."; Problem: Olson, Johansson and de Carvalho (2012) was read in full (Sources entry and source log S7). Its p. 67 and Table 4 carry the Keil and Tiwana report the unit uses, so the sentence is wrong; Fix: "Every study of software buying opened here was read in abstract only, except Olson, Johansson and de Carvalho (2012), read in full, and the Gartner and ARC pages, read in full."; Basis: https://rd.springer.com/content/pdf/10.1007/978-3-642-28827-2_5.pdf
[should-fix] [accuracy] preamble, second paragraph; Current: "And every study of software buying opened here was read in abstract only; what a study found beyond its abstract is not stated."; Problem: same error: Olson et al. (2012) was read in full; Fix: "And every study of software buying opened here was read in abstract only, except Olson et al. (2012), read in full for its report of an earlier study; what a study found beyond its abstract is not stated."; Basis: https://rd.springer.com/content/pdf/10.1007/978-3-642-28827-2_5.pdf
[should-fix] [accuracy] §3.5 Trusts; Current: "a site manager is the user-side voice most often present (this unit's inference)"; Problem: "most often present" is a frequency claim with no source. §5 says "nothing opened says how often warehouse users are among them", so the inference has no basis; Fix: "a site manager is the user-side voice a committee is likely to include (this unit's inference; no source opened counts who sits on a committee, section 5)"; Basis: unit §5; https://www.emerald.com/insight/content/doi/10.1108/13522750210432995/full/html
[should-fix] [label] Deliverable C, Card 1 (Karin), field 3; Current: "Losing a client over a slipped go-live or disputed invoices; both have happened [register: known trouble]"; Problem: "both have happened" reads as if Tandric lost a client. The register has a slipped go-live and disputed invoices, and no lost client; Fix: "Losing a client over a slipped go-live or disputed invoices [working]; a slipped go-live and disputed invoices have both happened, and a lost client is not in the register [register: known trouble]"; Basis: case-facts.md, Tandric "Known trouble"
[should-fix] [label] §6, Forrester abstracts; Current: "Read with SCE1 §8, where vendors supply the reference customers Forrester interviews, the satisfaction is that of customers the vendors put forward (this unit's inference)."; Problem: SCE1's key (§10, analyst) and the brief require an analyst grade to carry the note that vendors license reprints. Neither Forrester citation carries it; Fix: "Read with SCE1 §8, where vendors supply the reference customers Forrester interviews, the satisfaction is that of customers the vendors put forward (this unit's inference). Both reports were read in abstract on Forrester's site; a copy of a Forrester report on a vendor's site is one that vendor bought reprint rights to post (SCE1 §8) [analyst]."; Basis: filed SCE1 §8, §10; https://www.forrester.com/report/lessons-learned-from-the-forrester-wave-tm-order-management-systems-q1-2025/RES182379
[minor] [accuracy] §6, Forrester RES181465; Current: "(Swerdlow, Kalra and Nagel, 12 September 2024) opens:"; Problem: the abstract opens with "Digital business leaders struggle to identify which technology solutions will solve their business problems." The quoted sentence is the second; Fix: "(Swerdlow, Kalra and Nagel, 12 September 2024) says, in its abstract's second sentence:"; Basis: https://www.forrester.com/report/demystifying-the-technical-functions-of-warehouse-management-systems/RES181465
[minor] [accuracy] §2, Gartner B2B page; Current: "buyers spend 17% of a considered purchase meeting potential suppliers"; Problem: the page says that buyers considering a purchase "spend only 17% of that time meeting with potential suppliers". The 17% is a share of their time; Fix: "buyers considering a purchase spend 17% of the time they give it meeting potential suppliers"; Basis: https://www.gartner.com/en/sales/insights/b2b-buying-journey
[minor] [accuracy] §6, ARC criteria; Current: "product functions and features (architecture, functionality, customer support)"; Problem: the page's criteria in this group also include leadership and organisation, so the list reads as complete when it is not; Fix: "product or solution functions and features (architecture, functionality, customer support, leadership, organisation)"; Basis: https://www.arcweb.com/technology-evaluation-and-selection/warehouse-management-systems
[minor] [label] §5; Current: "Use of a warehouse system is mandated: the operator scans because the job requires it."; Problem: a mechanism the section relies on, with no source and no label; Fix: "Use of a warehouse system is mandated: the operator scans because the job requires it (working description)."; Basis: Part 8, line 1; unit preamble on working descriptions
[minor] [attribution] §1 "The age."; Current: "is the usual source of the five roles;"; Problem: unsourced. Webster and Wind was not opened, and the editorial is not quoted saying this; Fix: "is, in this unit's working description, the usual source of the five roles;"; Basis: source log "Not opened"; Part 1 per-unit line 1
[minor] [label] §2; Current: "Gartner's 2026 Tech Buying Behavior Study, published 27 July 2026, reports on AI purchases, which this course does not treat ([Gartner, 27 Jul 2026](https://www.gartner.com/en/articles/tech-buying-behavior-in-the-age-of-ai))."; Problem: the only Gartner citation in the section with no grade; Fix: "Gartner's 2026 Tech Buying Behavior Study, published 27 July 2026, reports on AI purchases, which this course does not treat ([Gartner, 27 Jul 2026](https://www.gartner.com/en/articles/tech-buying-behavior-in-the-age-of-ai)) [analyst]."; Basis: https://www.gartner.com/en/articles/tech-buying-behavior-in-the-age-of-ai
[minor] [style] §3.2 Trusts; Current: "Gartner's 2022 survey found IT paying at least part of 70% of technology purchases"; Problem: the same survey is called "2022" in §3.2 and §3.3, and "2021" in card 2 and in On a site visit. It was fielded Nov–Dec 2021 and published 13 Apr 2022; Fix: "Gartner's survey of late 2021 (published April 2022) found IT paying at least part of 70% of technology purchases"; Basis: https://www.gartner.com/en/newsroom/press-releases/2022-03-13-gartner-survey-finds-rise-in-business-technologists-is-driving-funding-for-tech-purchases-outside-of-it
[minor] [attribution] Deliverable C, Card 1 (Karin), field 2; Current: "settles disputed client invoices [SCE10 register note, working]"; Problem: no register row says this. The source is SCE10 deliverable B row 11 ("Karin settles the dispute (working…)"); Fix: "settles disputed client invoices [SCE10 deliverable B row 11, working]"; Basis: filed SCE10 deliverable B row 11; case-facts.md SCE10 rows
[minor] [accuracy] §3.5 What a failed project costs; Current: "a failed one is their peak (SCE5 card 5, working)"; Problem: unclear, and SCE5 card 5 says nothing about a failed go-live; Fix: "a failed one falls on their shifts and their staff (working)"; Basis: filed SCE5 card 5
[minor] [accuracy] §7, first bullet; Current: "Vendor case studies name a customer and quote one person; they are vendor-reported (SCE1 §9)."; Problem: SCE1 §9 grades case studies vendor-reported. It does not say they name a customer and quote one person, so that generalisation is unsourced; Fix: "Vendor case studies are vendor-reported (SCE1 §9): what they show of a selection is what the vendor and its customer agreed to publish."; Basis: filed SCE1 §9
[minor] [style] §2, "What IT managers weigh"; Current: "Keil and Tiwana's (2006) conjoint study, in which"; Problem: "conjoint" is used without a definition and has no glossary line; Fix: "Keil and Tiwana's (2006) conjoint study (respondents rate whole product profiles, and the weight of each attribute is inferred from their ratings; working definition), in which"; Basis: brief, Frame; https://rd.springer.com/content/pdf/10.1007/978-3-642-28827-2_5.pdf (p. 67)
[minor] [accuracy] §4 A manufacturer; Current: "A manufacturer's warehouse usually serves its own plants and customers from an ERP that already runs production and finance (working description)."; Problem: "usually" is a frequency claim with no source; Fix: "A manufacturer's warehouse may serve its own plants and customers from an ERP that already runs production and finance (working description; no source opened gives how often)."; Basis: Part 1 per-unit line 1
[minor] [label] Deliverable E, glossary; Current: "| Business unit | A part of a company outside IT that runs its own budget | Gartner press release, 13 Apr 2022 [analyst] |"; Problem: the release uses the term but does not define it, so the definition is the course's; Fix: "| Business unit | A part of a company outside IT that runs its own budget | Term in Gartner press release, 13 Apr 2022 [analyst]; definition working |"; Basis: Gartner press release URL above
[minor] [figure] §1 timeline, event label; Current: "Howcroft & Light: one small firm"; Problem: the text and the abstract say "small organisation"; Fix: "Howcroft & Light: one small organisation"; Basis: https://aisel.aisnet.org/jais/vol11/iss3/2
[minor] [figure] §1 timeline caption; Current: "with its sample where the abstract gives one"; Problem: the Gartner sample (1,120) comes from a press release, and Olson et al. was read in full; Fix: "with its sample where the source read gives one"; Basis: unit §2; source log S11
[minor] [attribution] Sources, Verville & Halingten (QMR); Current: "*Qualitative Market Research* 5(3), 188–198."; Problem: the publisher gives the full title as *Qualitative Market Research: An International Journal*; Fix: "*Qualitative Market Research: An International Journal* 5(3), 188–198."; Basis: https://www.emerald.com/insight/content/doi/10.1108/13522750210432995/full/html
[minor] [attribution] Sources, He & King; Current: "https://jmis-web.org/articles/493 (abstract, on the journal's site)"; Problem: the brief asks for a DOI address for a paper. None is given, and none was confirmed by this check; Fix: "https://jmis-web.org/articles/493 (abstract, on the journal's editorial site; no DOI shown there or found in this unit's searches)"; Basis: https://jmis-web.org/articles/493
[minor] [attribution] Sources, closing line; Current: "Filed units cited: SCE1 (§§1, 3, 7, 8, 9, 10), SCE5 (§§1.5, 2; cards 1, 4, 5), SCE6 (§§3, 12), SCE8 (§4; cards 4, 5), SCE9, SCE10 (§§7, 11; deliverable B)."; Problem: the body never cites SCE1 §3 or SCE10 §11, and it does cite SCE5 deliverable A, which the line leaves out; Fix: "Filed units cited: SCE1 (§§1, 7, 8, 9, 10), SCE5 (§§1.5, 2; cards 1, 4, 5; deliverable A), SCE6 (§§3, 12), SCE8 (§4; cards 4, 5), SCE9, SCE10 (§7; deliverable B)."; Basis: the unit's own pointers; filed SCE1, SCE5, SCE10

A Python script confirmed that each of the 23 Current strings occurs exactly once in unit.md.

## Confirmed

- **Johnston & Bonoma (1981), *JM* 45(3), 143–156, DOI 10.1177/002224298104500312.**
  - What checked: 31 firms; capital equipment and industrial services; communications network; "Equipment and service purchase measures differed reliably"; structure and situation correlated with the group's dimensions; no country stated.
  - Result: PASS. Closes unsure items 1 and 7.
  - Sources: catalogue record of the SAGE DOI (https://katalog.adlr.link/Record/ai-49-aHR0cDovL2R4LmRvaS5vcmcvMTAuMTE3Ny8wMDIyMjQyOTgxMDQ1MDAzMTI?lng=en) and a university-hosted copy of the article (https://vc.uni-bamberg.de/pluginfile.php/2929163/mod_folder/content/0/The%20Buying%20Center%20Structure%20and%20Interaction%20Patterns.pdf).
- **Ehret, Johnston & Ritter (2024), *IMM* 117, A10–A16, DOI 10.1016/j.indmarman.2023.12.020.**
  - What checked: bibliographic record only; the record calls it "Editorial Material".
  - Result: PASS. The practice grade fits SCE1's key (unsure item 3).
  - Source: https://clarivate.forskningsportal.dk/display/pub-wos-001195999100001
- **Bonoma, HBR R0607P.**
  - What checked: dated 1 July 2006, "first published in 1982"; both quoted phrases appear in the publisher's description.
  - Result: PASS (unsure item 5: the unit attributes the words to the description).
  - Source: https://store.hbr.org/product/major-sales-who-really-does-the-buying-hbr-classic/R0607P
- **Verville & Halingten, *MD* 40(3), 206–216.**
  - What checked: holding company for a gas and electric utility and a non-utility energy business; about six months; six iterative, recursive, interrelated processes.
  - Result: PASS.
- **Verville & Halingten, *QMR* 5(3), 188–198.**
  - What checked: four organisations; Webster and Wind's framework; the quoted phrase on users.
  - Result: PASS.
- **Das Neves, Fenn & Sulcas, *SAJBM* 35(1), 45–52.**
  - What checked: eleven cases; University of Cape Town; process and checklist; the roles discussed.
  - Result: PASS.
- **Olson et al., LNBIP 105, 64–74.**
  - What checked: p. 67 has 126 responses on 7 profiles from MIS managers of large organisations. Effects in order: reliability 0.464, functionality 0.457, cost −0.253, ease of customisation 0.129, ease of use 0.073. Vendor reputation and ease of implementation were not significant.
  - Result: PASS. Unsure item 4 is confirmed as far as Olson et al. go. The practice grade for an origin that was not traced is correct.
- **Howcroft & Light 2010, *JAIS* 11(3), DOI 10.17705/1jais.00224.**
  - What checked: longitudinal; a small organisation; "best technology solution"; "various actors shape the process".
  - Result: PASS.
- **Howcroft & Light 2008, *JEIM* 21(6), 597–615.**
  - What checked: SME consultancy, CRM; both quotations; marginalises user needs; external parties' vested interest.
  - Result: PASS.
- **Brown et al. 2002, *EJIS* 11(4), 283–295.**
  - What checked: the quotation is exact; "primary drivers"; a banking field study; no sample size; the relationships that differed are not named.
  - Result: PASS (unsure item 6). Checked at RePEc and the Springer PDF address.
- **Venkatesh & Davis 2000, *MS* 46(2), 186–204.**
  - What checked: four systems at four organisations, N = 156, two voluntary and two mandatory; three measurement points; both processes significant.
  - Result: PASS (unsure item 2). Checked at RePEc.
- **He & King 2008, *JMIS* 25(1), 301–331.**
  - What checked: 82 studies; "minimally-to-moderately beneficial"; effects stronger on attitudes and behaviour than on productivity.
  - Result: PASS.
- **Gartner B2B page.**
  - What checked: H1 "The B2B Buying Journey"; undated; no sample; "six to 10 decision makers"; 17%; the six jobs; uses "buying group".
  - Result: PASS.
- **Gartner press release, dated 13 Apr 2022 on the page.**
  - What checked: 74%, 26%, 70% and 75% (delays reaching agreement on budget allocation, among respondents using shared funding); 1,120 respondents at manager level or above; revenue of $1 million or more; the three regions; Nov–Dec 2021.
  - Result: PASS. Figure 2 PASS.
- **Gartner 2026 study, 27 Jul 2026.**
  - What checked: it is about AI investment in buying groups.
  - Result: PASS.
- **ARC page.**
  - What checked: the quoted sentence; cross-functional evaluation; cost-benefit analysis; the items to check; no demonstrations, reference checks or roles; no vendor named; undated; offers ARC's engagement.
  - Result: PASS. A second ARC address was not opened (unsure item 10).
- **Forrester RES181465.**
  - What checked: title, subtitle, authors, 12 Sept 2024, and the quotation.
  - Result: PASS.
- **Forrester RES182379.**
  - What checked: title and 28 Apr 2025; the quotation is present; genAI mentioned; no authors shown.
  - Result: PASS.
- **Webster & Wind 1972, *JM* 36(2).**
  - What checked: the record matches what the unit says; nothing in the unit rests on it.
  - Result: PASS.
- **Pointers to filed units.** Each one checked says what the unit claims, apart from the two findings (Karin's "register note"; the closing list). Checked:
  - SCE1 §§1, 7, 8, 9, 10 and 11 (C14 → SCE13).
  - SCE5 §1.5, §2; cards 1, 4 and 5; deliverable A.
  - SCE6 §3 and §12.
  - SCE8 §4 (Gartner 2026 TMS written around shippers; the four ways a provider differs) and cards 4 and 5.
  - SCE9 (Lena).
  - SCE10 §7, and deliverable B rows 2, 10, 11, 12 and 14.
- **The unit's own section pointers** all resolve.
- **Case facts.** Every Corvane, Ostrel, Tandric, Halvern and Varnby fact matches case-facts.md (including "Added by units") or is listed in notes.md. Each is labelled "(fictional)" on first use, and none is used as evidence.

## Could not verify

- **Ehret et al. (2024), content.** No search returned the ScienceDirect page, so these points are unverifiable:
  - "Buyers play a diverse set of specific roles" and the five roles.
  - External actors complementing or substituting for them.
  - The 1967 and 1972 seminal works, "published more than 45 years ago".
  - Cyert, Simon & Trow (1956) and the mainframe purchase.
  - IT as agent, servitization, and purchasing being outsourced.
- **Brown et al.:** the Crossref API record was refused by the permission system (not checked); the metadata was confirmed at RePEc.
- **He & King:** DOI not confirmed (dblp blocked by a bot check).
- **Howcroft & Light 2010:** page range not shown on the AIS page.
- **Johnston & Bonoma:** the SAGE page itself was not opened.
- **Keil & Tiwana (2006):** the original was not opened.
- **Gartner B2B page:** the date of its figures (unsure item 8).
- **Venkatesh & Davis:** the factor lists in brackets were not matched word for word against the abstract.
- **kit/private_terms.py** is not in the packet. A grep for the owner's name, his employer and its former name, and the major real vendors found nothing.

## Passes

1. **References exist and match.** 18 entries. 17 match their publisher's or a bibliographic record. Two minor findings: the full *QMR* title, and He & King's DOI. Howcroft & Light 2010 pages not checked.
2. **Claims against sources.** Every claim on the 17 sources that opened was read against its source. All pass except three minor wording findings (Forrester "opens", Gartner 17%, ARC list). Ehret's content is unverifiable.
3. **Grades against SCE1's key.** The grades are correct:
   - practice for an untraced origin and for the editorial;
   - analyst for the Gartner, ARC and Forrester pages;
   - abstract readings stated throughout;
   - no vendor statement used as evidence.

   Gaps: should-fix for the missing reprint note, and for the misstatement that every study was read in abstract only. Minor: one ungraded Gartner line.
4. **Vendors.** No real vendor is named, assessed or mapped; the vendor named in the Verville abstract is withheld. The unit has no vendor lists and no figures from private companies. Halvern and Varnby (fictional) are used only as the register gives them and are not tied to real companies. PASS.
5. **The case.** All facts trace to the register or to notes.md items 1–9. Labelled fictional, never used as evidence. PASS, with one should-fix (Karin field 3) and one minor (Karin field 2).
6. **Scope and tone.**
   - AI is touched three times, each time in one clause, then left.
   - No interview framing, no method teaching, nothing about the owner or his employer.
   - Tone is direct.
   - The age and setting of the buying-centre research are stated (§1, front matter, figure 1). The transfer to execution software is labelled as the unit's inference (§1 "What the transfer is", §3, §4).
   - Terms are defined on first use, except "conjoint" (minor).
   - Coverage: every brief item is covered. Two are thin:
     - The per-role lines are "working descriptions" where the brief asks for "sourced or labelled as practice". The notes raise this (Contradictions 2, Needs 1), and no edit can fix it.
     - Analyst guides: the Gartner pages failed, and the unit says so.
7. **Deliverable and figures.**
   - Deliverable A has the brief's six fields plus SCE5's "Who", in SCE5's form.
   - B: six Corvane cards for seven roles, because Edda holds 3.1 and 3.7.
   - C: six Tandric cards; Anke holds 3.5 and 3.1, and Dario stands in for 3.2.
   - Both are built in full, covering the named executives.
   - D is a template whose blanks say what goes in them.
   - "On a site visit" (8 asks) and "Self-check" (8 questions) are present, and every answer agrees with the body.
   - Figure 1 (timeline, §1): the kind fits and every label traces to the text. FIX, for two minor findings.
   - Figure 2 (compare, §2): PASS.
   - Figure 3 (matrix, §3): every cell traces to the §3 "Answers for" lines and to §3.2; the caption names its sources. PASS.

**Part 8, line by line.** Each item passes except as noted:
- Sourced where made: three lines carry claims with no source; one should-fix (§3.5) and two minor (§4, §5).
- Allowed source types only.
- Grades follow the key: passes, apart from the reprint note.
- How each analyst report was read is stated.
- Vendor rules met.
- Every number says whose figure it is, with sample and year.
- No private company figures.
- Every study gives its sample, setting and design, and transfers are labelled.
- C14 is named; C13 is left to SCE12.
- 18 of 18 references are in the source log.
- Records match, apart from two minor findings.
- Case facts match.
- Owner and AI exclusions hold.
- Search-on dates are present.
- The deliverable is built in full and then as a template.
- Site visit and Self-check agree with the body.
- The unit does not read as advice without evidence.
- Papers are linked by DOI, except He & King (minor).

**Read as the preamble's reader:** the limits of the evidence are stated plainly, and the cards can be used on their own. The repeated "[working]" tags are dense but correct.

**References opened (17):** Johnston & Bonoma (catalogue record and article copy), Ehret (WoS record only), Bonoma HBR, Verville & Halingten ×2, Das Neves, Olson, Howcroft & Light ×2, Brown, Venkatesh & Davis, He & King, Gartner ×3, ARC, Forrester ×2.

**Not opened:** Ehret's ScienceDirect page (no search returned it), the SAGE page for Johnston & Bonoma, the Crossref API record for Brown (refused), dblp for He & King (bot block), Keil & Tiwana, and Webster & Wind's publisher page (only its record was opened).

Verdict: SCE11 · keep · 0 error, 5 should-fix, 18 minor
