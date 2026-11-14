Model: claude-fable-5-2

# PB8 · Voice, disclosure and the rules: stratified-sample audit (course PB, Audit 2)

Date: 14 November 2026. Search: on. Unit audited: `unit.md` (PB8, written 2026-11-13 by Opus 5.5, search on). The unit was not edited.

Verdict: **PASS.** One of 17 sampled claims fails (5.9%, under the one-in-ten line), so no full audit was run. Eleven errata follow (6 should-fix, 5 minor) and no flags.

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2. Read only inside `/home/claude/fpb/PB8`; wrote only inside `out/`. `out/` was empty at the start, so there was no lost run to resume.
- Read: PROMPT.md, unit.md, brief.txt, sourcing-parts-1-and-5.md, case-facts.md, fresh-check-PB8.md (to avoid re-reporting; none of its verdicts reused), and `others/` for pointers only.
- Web rule followed: WebSearch first; WebFetch only on a URL that a search in this agent returned verbatim; a refusal or failure is "not checked" and was not retried.
- Web use: 25 searches run, 32 fetches. After the 25th search the tool refused two more: the turn's search budget (200 calls, shared by every agent) was used up. Every sampled claim had been opened at its source by then. The checks beyond the sample stopped there, apart from fetches of URLs already returned.
- Reading of "one claim per `##` section": the unit has 11 `##` sections. §6 holds seven `###` subsections, each a separate rule with its own sources, so one claim was drawn from each of §6.1 to §6.7 in place of a single claim for §6. Sample size: 17. The sample was written to this file before any check.

## Sample and verdicts

| # | Section | Claim | Source opened | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | Tom Scott's four quotations; Tubefilter, James Hale, 2 Jan 2024; "burnout" absent from the report | https://tubefilter.com/2024/01/02/tom-scott-youtube-break/ | PASS | All four quotations, author and date on the page; "for the past 10 years"; no "burnout". |
| S2 | §2 | Muhmin, Syah and Anggraeni: 407 Indonesian women 18–35; paths 0.225 / 0.128 / 0.075 (p = 0.135); bond to purchase intention 0.432; R² 24.7% and 35.5%; *Frontiers in Communication* 11, 5 Feb 2026 | https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2026.1723759/full | PASS | Every figure matches, with 54.8%/45.2%, PLS-SEM, the direct paths 0.127/0.129/0.124 and the limitation sentence. |
| S3 | §3 | Nguyen and Duffy, *New Media & Society* (7 Jul 2026): 58 examples, 62 news accounts, 78 interviews; Cornell Chronicle, Tom Fleischman, 8 Jul 2026 | https://news.cornell.edu/stories/2026/07/what-social-media-creators-cant-say-about-their-job | PASS | The counts sentence is verbatim. The other seven quotations in the paragraph are on the page. The Khanna bill's status is not given, as the unit says. |
| S4 | §4 | GDPR art. 9(2)(e), "manifestly made public by the data subject"; C-252/21 (4 Jul 2023): "explicitly made the choice beforehand", "with full knowledge of the facts", "publicly accessible to an unlimited number of persons" | https://www.legislation.gov.uk/eur/2016/679/article/9/adopted ; https://fra.europa.eu/en/node/44533 | PASS | Art. 9(1) lists "data concerning health" and ends "shall be prohibited". All three phrases are in point 3 of the ruling. "Full knowledge of the facts" there qualifies the user's individual settings. |
| S5 | §5 | YouTube trim: "on a computer"; URL, view count and comments stay the same; the 100,000-view limit; the Partner Program exception | https://support.google.com/youtube/answer/9057455 | PASS | All four fragments verbatim. |
| S6 | §6.1 | UK: unfair commercial practices rules in the DMCC Act 2024 since 6 April 2025; "hidden advertising on social media" banned; fines "up to 10% of their worldwide turnover"; page updated 3 Dec 2025 | https://www.gov.uk/government/publications/what-businesses-need-to-know-about-unfair-commercial-practices/what-businesses-need-to-know-about-unfair-commercial-practices | PASS | "The changes came into force on 6 April 2025"; the phrase sits under "What is always banned?"; "The CMA and the courts can now fine traders…"; "Updated 3 December 2025". |
| S7 | §6.2 | Illinois Public Act 103-0556: from 1 July 2024 a minor under 16 is "considered engaged in the work of vlogging" at 30% of compensated content in 30 days; trust | https://www.ilga.gov/Legislation/publicacts/view/103-0556 | PASS | Date, age, 30%, 30 days and the trust all hold. The Act requires a second condition the unit leaves out (the pay threshold or USD 0.10 a view): erratum PB8-8, minor. |
| S8 | §6.3 | A strike "means your content was removed due to a legal copyright removal request"; "Channels that get 3 copyright strikes in 90 days are subject to termination" | https://support.google.com/youtube/answer/2814000?hl=en | PASS | Both sentences verbatim. Fetched with `?hl=en`, as the search returned it. |
| S9 | §6.4 | Directive (EU) 2019/1152 art. 9: no ban on other employment outside the work schedule, no adverse treatment; "incompatibility restrictions" on four named grounds | https://lawplayer.com/eu/article/32019L1152/art_9 | PASS | Paragraph 1 verbatim; paragraph 2 has "incompatibility restrictions" and the four grounds. The EUR-Lex copy returned no body text, so the official text was not compared. |
| S10 | §6.5 | HMRC content creators page: over £1,000; "even if you just think of it as a hobby"; the allowance "adds up"; gifts' value included; "by 5 October"; modified 22 Sep 2026 | https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/ | PASS | Figure, quotations and date hold (the date is in the page's metadata). "Adds up" is on the page, but said of earnings, not of the allowance: erratum PB8-7, minor. |
| S11 | §6.6 | CAN-SPAM guide: postal address (PO box or registered private mailbox); opt-outs "within 10 business days"; "of up to $53,088" per email; Aug 2023, modified 22 Jul 2025 | https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business | PASS | All verbatim. Not stale: 16 CFR 1.98 on eCFR still lists USD 53,088, last amended 90 FR 5581, 17 Jan 2025 (https://www.ecfr.gov/current/title-16/chapter-I/subchapter-A/part-1/subpart-L/section-1.98). |
| S12 | §6.7 | USPTO replaced TESS on 30 November 2023 with a "new trademark search system"; post of 18 Oct 2023 | https://www.uspto.gov/subscription-center/2023/retiring-tess-what-know-about-new-trademark-search-system | PASS | Post dated 10/18/2023; "Thursday, November 30"; the new system is at tmsearch.uspto.gov. |
| S13 | §7 | "the US and UK pages above treat gifted goods as income in some cases" | https://www.irs.gov/node/68141 ; HMRC page as S10 | PASS | IRS Topic 420's bartering sentence is verbatim, reviewed 08-Oct-2026. HMRC: "must include the value of any gifts or services you received from promoting products online". |
| S14 | Deliverable, D3 line A3 | Portugal's advertising regulator is the Direção-Geral do Consumidor (gov.pt, updated 16 Jun 2026); Decreto-Lei 57/2008 art. 19(3) and 19(1) | https://www.gov.pt/entidades/direcao-geral-do-consumidor ; https://www.bportugal.pt/sites/default/files/anexos/legislacoes/459417805_1.doc.pdf | PASS | "Na área da publicidade é a entidade reguladora, fiscalizando e instruindo processos de contraordenação"; "Atualizado em 16.06.2026". Art. 19(1) and 19(3) verbatim; the copy notes amendments to DL 9/2021 and says "Não dispensa a consulta do documento original". |
| S15 | Template, T3 line E1 | The EU source for "which data law reaches your list" is GDPR art. 3(2)(a) | https://www.legislation.gov.uk/eur/2016/679/article/3/adopted/data.htm | **FAIL** | Art. 3(2) applies only to "a controller or processor not established in the Union". A reader established in the EU comes under art. 3(1). The unit says this for Mara in D3 line E1, and left the template, D3's EU source cell and §6.6 naming only art. 3(2)(a). Errata PB8-1 to PB8-3. |
| S16 | Sources | Pillemer, Harrison, Murphy and Park, *Administrative Science Quarterly* 71(1), 215–260, online 18 Dec 2025 (metatoc record) | https://metatoc.com/papers/129690-audience-entanglement-how-independent-creative-workers-experience-the-pressures-of-widespread-appeal-on-digital-platforms | PASS | Volume, issue, pages, online date and issue (March 2026) match. The record's visible text does not list the authors; PsyPost names all four. |
| S17 | Unsure list | SCL (20 Feb 2024): 572 influencers, 97%, one in five; other reports give a different count | https://www.scl.org/european-commission-and-consumer-authorities-investigate-online-influencers/ | PASS | SCL says exactly this. The Commission's own count is 576: see "Also checked" 9 and errata PB8-4 to PB8-6. |

On S15: the paragraph the template cites says what the unit quotes from it, and for a reader outside the EU it is the right one. It is marked FAIL because the template is for a reader in any country, and for a reader established in the EU it names the wrong paragraph. Marked PASS instead, the failure rate would be 0 of 17; the verdict is the same either way.

## Also checked (beyond the sample; counted in the totals)

| # | Section | Claim | Source opened | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §3 | Audience entanglement: 54 creators, 74 interviews, "over 500,000 followers", "nearly 280,000 subscribers", the two states, movement between them, three strategies, the limits | https://www.psypost.org/new-study-sheds-light-on-the-psychological-burden-of-having-a-massive-social-media-audience/ | PASS | Eric W. Dolan, 20 Feb 2026. PsyPost says "24 hours" where the unit says "a full day". |
| 2 | §2 | Eisend et al.: 61 papers, 57 data sets; the two quoted findings; *Journal of Advertising* 49(3), 344–366, 2020 | https://research.wur.nl/en/publications/a-meta-analysis-of-the-effects-of-disclosing-sponsored-content/ | PASS | Verbatim; the DOI matches. |
| 3 | §2 | Each respondent rated one influencer; the trustworthiness items concern genuineness and honesty in recommending products | Frontiers article as S2 | PASS | This settles the Unsure list's Frontiers line: both points are on the article (items TRU1 to TRU4). |
| 4 | §5 | Nothing on the trim page says the viewer is shown that a video changed | YouTube answer 9057455 as S5 | PASS | The page covers the creator's steps only. |
| 5 | §6.1 | CMA guidance for content creators: payment definition, unsolicited gifts, own brands and employers, clear and unclear labels, platform tools; updated 3 Sep 2025 | https://www.gov.uk/government/publications/social-media-endorsements-guide-for-influencers/social-media-endorsements-being-transparent-with-your-followers | PASS | Every quoted fragment is on the page. |
| 6 | §6.1 | Influencers' guide, 2026 edition: rests on the 2024 Act; five labels; "Sponsored", "Spon" and "Sp" insufficient; 12 months (the unit rests this on Lewis Silkin) | https://www.asa.org.uk/static/17cf70a4-f904-4684-a68c8310ba7700e1/Influencers-guide-to-making-clear-that-ads-are-ads.pdf | PASS | The guide's PDF opened here (edition dated October 2026) and holds all four points. The ASA resource page and Lewis Silkin's summary were not opened, so "fourth edition" and "23 October" were not re-checked. |
| 7 | §6.1 | Digital Fairness Act proposal presented 11 Nov 2026; covers paid influencer promotion; still to pass Parliament and Council | https://www.lewissilkin.com/insights/2026/11/11/european-commission-publishes-long-awaited-digital-fairness-act-102o9b5 | PASS | Still current on 14 Nov 2026: published 11 Nov; influencers must "clearly disclose when they are being paid to promote a product"; negotiation ahead. The unit's own two press sources were not opened. |
| 8 | §6.6 | Whether an email is "commercial" under CAN-SPAM depends on its primary purpose | FTC guide as S11 | PASS | "What matters is the 'primary purpose' of the message." |
| 9 | §6.1 | EU sweep in the body: "572 influencers (SCL's count; other reports of the same sweep give 576)", 97%, one in five | SCL as S17; https://germany.representation.ec.europa.eu/news/screening-von-kommissionverbraucherschutzbehorden-influencer-kennzeichnen-selten-werbung-2024-02-14_de | PASS | Correctly attributed and hedged, so it passes. The Commission's Representation in Germany (14 Feb 2024) settles the count: 576 influencers checked, of whom 572 posted on Instagram. SCL's total is a misreading. Errata PB8-4 to PB8-6, should-fix. |
| 10 | §6.6 | GDPR art. 3(2)(a) wording | https://www.legislation.gov.uk/eur/2016/679/article/3/adopted/data.htm | PASS | Verbatim. |
| 11 | §6.6 | UK GDPR art. 3(2)(a): "data subjects in the United Kingdom" | https://www.legislation.gov.uk/eur/2016/679/article/3/data.html | PASS | Verbatim. |
| 12 | Deliverable, D3 line E1 | GDPR art. 3(1) wording; art. 3(2) is for a controller "not established in the Union" | GDPR art. 3 as adopted, as 10 | PASS | Both verbatim. Recital 22 was not opened. |

## Not checked

- **WebSearch: search budget used up** (limit of 200 calls per turn, shared by every agent). Two searches were refused, for the FTC's Disclosures 101 and the ASA resource page. The tool's message said not to search again, so neither was retried. No sampled claim was affected.
- **Unit sources never opened as a result** (none was in the sample): Patreon Creator Hub; Haushofer's CV and CNBC; ICMJE; 16 CFR 255 and the Federal Register notice; FTC Disclosures 101; ASA resource page; Lewis Silkin (23 Oct 2026); UCPD Annex I and art. 7; Influencer Legal Hub; PinMeTo; ecommercenews.eu; CEA Digilaw; YouTube answers 154235, 17596007, 2801999, 6013276, 3376882 and 9783148; PPC Land; the four Instagram pages; *Buivids*; the Irish DPC page; GDPR arts. 7 and 13; ICO children's guide; ICO email marketing; California §3344; Better Internet for Kids; CDPA s. 11; Acas; Circular 30; N.Y. Labor Law §201-d; Your Europe; GOV.UK trading allowance; IRS FS-2022-38 and Topic 554; ePrivacy art. 13; PECR reg. 22; Withers; European IP Helpdesk; GOV.UK trade mark search; EUR-Lex (GDPR recital 22).
- https://eur-lex.europa.eu/eli/dir/2019/1152/oj/eng : the page returned its header and navigation only, with no article text.
- https://journals.sagepub.com/doi/10.1177/00018392251399652 : failed at the site (client error). The *Administrative Science Quarterly* paper stays unopened, as the unit says of itself.

## Failure rate

- Sample: 17 claims, 16 PASS, 1 FAIL, 0 STALE, 0 unverifiable. **1 in 17 = 5.9%.**
- All claims checked: 29, of which 28 PASS and 1 FAIL.
- The one-in-ten line is not crossed, so no full audit was run.

## Counts

- Words: 14,410 (`wc -w unit.md`). `##` sections: 11. `viz` figures: 4. Entries in Sources: 72, carrying 71 links.
- **Cited claims in the unit: 169**, tallied by reading, section by section. A sentence or table row counts once when it rests a number, date, quotation, attribution or mechanism on a cited source; a sentence citing two separate sources for two separate facts counts twice. Pointers to another unit's sourced content count. Mara's invented facts and the unit's own unsourced rules do not.

| Section | Cited claims |
|---|---|
| §1 | 7 |
| §2 | 10 |
| §3 | 11 |
| §4 | 3 |
| §5 | 3 |
| §6 (6.1: 17; 6.2: 10; 6.3: 8; 6.4: 5; 6.5: 8; 6.6: 12; 6.7: 3) | 63 |
| §7 | 1 |
| Deliverable (D1: 10 clauses; D2: 9 causes; D3: 23 lines) | 42 |
| Template (T1 clause 3; 20 lines of T3 that name a source) | 21 |
| Sources (a reference list; no claims counted) | 0 |
| Unsure list (4 items, and 4 in the two correction notes) | 8 |
| **Total** | **169** |

## Figures

1. **states, §3: PASS.** Every label is in §3's text: "Large audience", "Dysfunctional entanglement", "metrics as validation", "Functional entanglement", "begins", "some creators reach", "creators move back". The caption's journal, issue, online date, PsyPost date and link match the text. The two labels the fresh check removed are gone.
2. **decision, §6.1: PASS.** The root question now carries the personal and family relationship that §6.1 quotes from the FTC. Each outcome traces to §6.1 (the FTC on video and on tools; the CMA on commissions, discounts and "#aff"; YouTube answer 154235; Instagram's label). The caption's dates (Nov 2019, modified 3 Dec 2024; updated 3 Sep 2025) match the text.
3. **matrix, §6: FIX (PB8-9, minor).** Every cell traces to §6.1 to §6.7 except one. The UK cell of the music row reads "Fair dealing", and §6.3 says only that "other countries have 'fair dealing'"; it never names the UK. The figure adds the link. YouTube answer 9783148 could not be opened to see whether the page names the UK. The caption is accurate.
4. **matrix, D3 (who acts): PASS.** All eight rows and five legend entries match D3's Owner and Professional columns (P1, P2, J1, J2, T1, T2, M1, M2), and the "Lawyer" column the fresh check asked for is there.

## Deliverable

- **Exists in full.** D1 has ten clauses, each with its basis. D2 is set in January 2029, two years after the first upload on 5 January 2027, with nine causes and five checkpoint questions. D3 has 23 lines with every column the brief names, each status dated and marked settled, to do or open. Templates T1 to T3 follow, and their blanks say what goes in them.
- **Follows from the evidence.** Each clause and each pre-mortem cause names the section and source it rests on, and all of them are in the body. Nothing in the deliverable carries a claim the body lacks, except the Portuguese sources in A3 and the art. 3(1) and recital 22 text in E1, which are cited in the row itself.
- **Usable without the unit, with two limits.** Line J1 points to "§6.4's checklist" and line E3 to "the art. 13 items"; both lists are in the body only. The register names its sources without links; the links are in the Sources list.
- **One defect.** D3 line E1's EU source cell names art. 3(2)(a) while its own status text says her test is art. 3(1) (PB8-2). The template repeats it for every reader (PB8-3).
- **Mara's facts agree with `case-facts.md`:** age, job, the one box, the account name and provisional handle, the cadence and the 5 January 2027 start, the four checkpoint dates, Portugal, upload 3 on 2 February 2027, upload 14 on 6 July 2027, beehiiv, and every register date. Her first mention is labelled "(Mara, fictional)". Weekdays were checked by arithmetic: 29 Nov 2026, 6 Dec 2026 and 31 Jan 2027 are Sundays; 5 Jul 2027 is a Monday.
- **Pointers to other units all hold:** PB1 §1 (the seven labels), §8 (the tax and equipment question), D3; PB2 §2, §3 (five people, the delay and the pass mark as conventions), D1, D2; PB3 §5 (collection waits for PB8), §6 (YouTube answer 141805 on breaks beside AIR Media-Tech); PB4 D2 (piece 2's reveal on Sat 9 Jan and upload 2 on Tue 19 Jan 2027; three 15-minute reply slots; voice notes); PB5 §5 (the Shorts Content ID rule) and piece 1's sanded corner; PB6 R3; PB7 §5, IR2, IR9 and its note that Help Centre bodies did not load; PB9 D1 (deals from upload 14); PB10 (the review re-reads the policy). No contradiction was found, so there are no flags.

## Course goal and sourcing standard

- **Course goal.** The unit serves the first two outcomes indirectly and does what its Aim says: a written disclosure policy and a register of every rule with the source that settles it. It gives PB9 its disclosure rules and DD-PB2 its open tax and contract lines, as the brief's Gives line asks.
- **Advice without evidence: none found.** Each rule that no source sets is marked "(her rule)" or "this course's" with its basis. Transfers from large-creator studies to an account under 1,000 followers are said to be inferences.
- **Neutral ground holds.** No rate or threshold is stated as the reader's. £1,000, $400 and $53,088 are each in their source's currency with the page's date. Each legal point is a question with EU, UK and US sources. The unit says three times that it is information and not legal or tax advice.
- **Dates.** Changeable facts carry their check date (13 Nov 2026) or the page's own date.
- **Sources list.** Every link in the body is in Sources. Three sources are listed that the body cites by name without a link (the gov.pt page, the Banco de Portugal copy, EUR-Lex for recital 22), all in D3 lines A3 and E1. Part 5 asks for links as links. This is a note; no erratum is given.
- **The one gap.** §6.6 answers "which law applies" only for a controller outside the EU or the UK. A reader who lives in either is told the question turns on targeting, when art. 3(1) applies to them directly (PB8-1).

## Verdict

**PB8: PASS.** Sample failure rate 5.9% (1 of 17). No full audit run. No section needs rewriting. Eleven errata: 6 should-fix (PB8-1 to PB8-3 on GDPR art. 3; PB8-4 to PB8-6 on the sweep count) and 5 minor. No flags.

## The most consequential errors

1. **A reader in the EU or the UK is pointed to the wrong paragraph of the GDPR.** §6.6, the register and the template name only art. 3(2)(a), the rule for someone outside the Union. Someone established inside it is covered by art. 3(1), with no question of "targeting" to settle. The unit corrected this for Mara and left it for the reader (PB8-1 to PB8-3).
2. **The EU sweep's headline count is the secondary source's mistake.** The unit leads with 572 influencers and hedges with 576. The Commission's figure is 576; 572 is how many of them posted on Instagram (PB8-4 to PB8-6).
3. **The HMRC allowance sentence can be read backwards.** "The £1,000 allowance 'adds up' across all of them" suggests one allowance per activity. The page says there is a single allowance and that earnings from all side activities count towards it (PB8-7).

## Bibliography line

Add: European Commission Representation in Germany, news release of 14 Feb 2024 on the influencer screening (576 influencers); the ASA/CAP/CMA Influencers' guide PDF, October 2026 edition (https://www.asa.org.uk/static/17cf70a4-f904-4684-a68c8310ba7700e1/Influencers-guide-to-making-clear-that-ads-are-ads.pdf), which confirms what the unit takes from Lewis Silkin; 16 CFR 1.98 on eCFR for the current CAN-SPAM penalty. Mark failed: none; note against SCL (20 Feb 2024) that its total of 572 is the Instagram count.

## Changelog line

2026-11-14 · PB8 · Audit 2 stratified sample (claude-fable-5-2, search on): PASS; 17 sampled, 1 FAIL (5.9%), 29 checked in all, no full audit; 11 errata (6 should-fix, 5 minor), 0 flags; figures 3 PASS, 1 FIX; search budget ran out after the sample was complete.

## Errata

Each Current was counted with `grep -c -F` and occurs exactly once in `unit.md`, on one line. The exact strings are in `errata.json`. PB8-6 is needed only if PB8-4 is applied, and its Fix holds a line break (it adds one line to Sources). PB8-9 and PB8-10 were not checked at source.

### PB8-1 · should-fix · erratum

- Section: §6.6 Which law applies
- Verdict: FAIL
- Current: `The GDPR reaches a controller outside the EU where processing relates to`
- Fix: `The GDPR applies to processing "in the context of the activities of an establishment of a controller or a processor in the Union" (art. 3(1)), so a reader established in the EU is covered with no targeting test; it also reaches a controller outside the EU where processing relates to`
- Basis: GDPR art. 3(1) and 3(2) as adopted: art. 3(2) applies only to "a controller or processor not established in the Union". The unit says so for Mara in D3 line E1 but not for the reader. https://www.legislation.gov.uk/eur/2016/679/article/3/adopted/data.htm

### PB8-2 · should-fix · erratum

- Section: Deliverable D3, line E1 (EU source cell)
- Verdict: FAIL
- Current: `| E1 | Which law | Which data law applies to her list? | GDPR art. 3(2)(a) |`
- Fix: `| E1 | Which law | Which data law applies to her list? | GDPR art. 3(1) if established in the Union; art. 3(2)(a) if not |`
- Basis: Same as PB8-1; the cell contradicts the status text of the same row, which gives art. 3(1) as her test. https://www.legislation.gov.uk/eur/2016/679/article/3/adopted/data.htm

### PB8-3 · should-fix · erratum

- Section: Template T3, line E1
- Verdict: FAIL
- Current: `| E1 | Which law | [which data law reaches your list] | [GDPR art. 3(2)(a)] | [UK GDPR art. 3(2)(a)] |`
- Fix: `| E1 | Which law | [which data law reaches your list] | [GDPR art. 3(1) if you are established in the EU; art. 3(2)(a) if you are not] | [UK GDPR art. 3(1) if you are established in the UK; art. 3(2)(a) if you are not] |`
- Basis: GDPR art. 3(1)-(2) as adopted, https://www.legislation.gov.uk/eur/2016/679/article/3/adopted/data.htm ; UK GDPR art. 3(1): "in the context of the activities of an establishment of a controller or a processor in the United Kingdom", https://www.legislation.gov.uk/eur/2016/679/article/3/data.html

### PB8-4 · should-fix · erratum

- Section: §6.1 European Union
- Verdict: other
- Current: `In a coordinated check of the posts of 572 influencers (SCL's count; other reports of the same sweep give 576), 97% posted commercial content and "only one in five systematically indicated that their content was advertising" ([SCL, 20 Feb 2024](https://www.scl.org/european-commission-and-consumer-authorities-investigate-online-influencers/); secondary report of the Commission's sweep).`
- Fix: `In a coordinated check of the posts of 576 influencers (the Commission's count; 572 of them posted on Instagram, the figure SCL gives as the total), 97% posted commercial content and "only one in five systematically indicated that their content was advertising" ([SCL, 20 Feb 2024](https://www.scl.org/european-commission-and-consumer-authorities-investigate-online-influencers/); secondary report of the Commission's sweep; the count is from the [Commission's Representation in Germany, 14 Feb 2024, in German](https://germany.representation.ec.europa.eu/news/screening-von-kommissionverbraucherschutzbehorden-influencer-kennzeichnen-selten-werbung-2024-02-14_de)).`
- Basis: Commission Representation in Germany, 14 Feb 2024: "Bei dem Screening wurden die Beiträge von 576 Influencerinnen und Influencern auf großen Social-Media-Plattformen überprüft"; "572 posteten auf Instagram"; 97 Prozent; 20 Prozent. https://germany.representation.ec.europa.eu/news/screening-von-kommissionverbraucherschutzbehorden-influencer-kennzeichnen-selten-werbung-2024-02-14_de

### PB8-5 · should-fix · erratum

- Section: Unsure list
- Verdict: other
- Current: `- EU influencer sweep (§6.1): SCL's report (20 Feb 2024) gives 572 influencers' posts, 97% with commercial content and one in five disclosing systematically; other press reports give a different count, and the Commission's own press release was not opened.`
- Fix: `- EU influencer sweep (§6.1): the Commission's count is 576 influencers, of whom 572 posted on Instagram (Commission Representation in Germany, 14 Feb 2024, in German; opened by the audit of 14 Nov 2026); SCL's report (20 Feb 2024) gives 572 as the total, with 97% posting commercial content and one in five disclosing systematically; the Commission's English press release was not opened.`
- Basis: Same as PB8-4. https://germany.representation.ec.europa.eu/news/screening-von-kommissionverbraucherschutzbehorden-influencer-kennzeichnen-selten-werbung-2024-02-14_de

### PB8-6 · should-fix · erratum

- Section: Sources
- Verdict: other
- Current: `- European Commission, Influencer Legal Hub (legal briefs dated 11 Oct 2023 and 13 Sep 2024). https://commission.europa.eu/influencer-legal-hub_en`
- Fix: `- European Commission, Influencer Legal Hub (legal briefs dated 11 Oct 2023 and 13 Sep 2024). https://commission.europa.eu/influencer-legal-hub_en` then, on a new line, `- European Commission, Representation in Germany, news release of 14 Feb 2024 on the screening of influencers by the Commission and consumer authorities (in German). https://germany.representation.ec.europa.eu/news/screening-von-kommissionverbraucherschutzbehorden-influencer-kennzeichnen-selten-werbung-2024-02-14_de`
- Basis: Needed only if PB8-4 is applied: a source cited in the text must be listed (sourcing standard Part 1, per unit). The fix adds one line after the current one (the fix holds a line break). https://germany.representation.ec.europa.eu/news/screening-von-kommissionverbraucherschutzbehorden-influencer-kennzeichnen-selten-werbung-2024-02-14_de

### PB8-7 · minor · erratum

- Section: §6.5 United Kingdom
- Verdict: other
- Current: `that the £1,000 allowance "adds up" across all of them`
- Fix: `that there is "a single £1,000 tax-free allowance (for each tax year)" towards which earnings from every side activity count`
- Basis: On the HMRC page "adds up" is said of earnings ("that adds up to £1,300"), not of the allowance; as written the phrase can be read as one allowance per activity, the opposite of the page: "a single £1,000 tax-free allowance (for each tax year)"; "anything you earn from different types of side hustles all counts towards this". https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/

### PB8-8 · minor · erratum

- Section: §6.2 United States
- Verdict: other
- Current: `includes the minor, and the vlogger must set aside earnings in a trust`
- Fix: `includes the minor and the views met "the online platform's threshold for the generation of compensation" or paid at least $0.10 a view, and the vlogger must set aside earnings in a trust`
- Basis: Public Act 103-0556, Sec. 2.6(a): both criteria must be met; criterion (2) is the pay threshold or compensation "equal to or greater than $0.10 per view". The unit gives criterion (1) alone as sufficient. https://www.ilga.gov/Legislation/publicacts/view/103-0556

### PB8-9 · minor · erratum · figure

- Section: §6 figure 3 (matrix, sources by area and jurisdiction)
- Verdict: other
- Current: `"cells": ["Permitted categories", "Fair dealing", "Fair use", "Content ID; Instagram music rules"]`
- Fix: `"cells": ["Permitted categories", "YouTube answer 9783148", "Fair use", "Content ID; Instagram music rules"]`
- Basis: A figure adds no fact: §6.3 says only that "other countries have 'fair dealing'" and never names the UK. Not checked at source (answer 9783148 could not be opened: search budget used up). If that page names the UK among fair-dealing countries, the better fix is to say so in §6.3 and keep this cell. Unit §6.3; https://support.google.com/youtube/answer/9783148?hl=en

### PB8-10 · minor · erratum

- Section: Deliverable D3, line C1 (UK source cell)
- Verdict: other
- Current: `| Fair dealing (same page) |`
- Fix: `| Same page (it names "fair dealing" for other countries) |`
- Basis: Same as PB8-9: the unit's text does not tie fair dealing to the UK. Not checked at source. Unit §6.3; https://support.google.com/youtube/answer/9783148?hl=en

### PB8-11 · minor · erratum

- Section: Sources (units of this course)
- Verdict: other
- Current: `PB9 (deals, to come).`
- Fix: `PB9 (deals; D1); PB10 (the review).`
- Basis: PB9 and PB10 are filed (others/PB9, others/PB10); the unit cites "PB9 D1" in register line A3 and "PB10's review" in the D3 lead-in, and the list omits both. No URL: the course's own units.
