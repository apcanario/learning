Model: claude-fable-5-2

# Stratified-sample audit · PB4 The content system · 14 November 2026 · search on

## Provenance
Fresh, isolated auditor (claude-fable-5-2). Read only `/home/claude/fpb/PB4`; wrote only `out/`. No earlier working files were in `out/`; this is a first run. Web rule followed: WebSearch first, WebFetch only on URLs a search in this agent returned verbatim.

## Sample (recorded before any check)
One claim per `##` section (11 sections).

| # | Section | Sampled claim | Source cited |
|---|---|---|---|
| S1 | §1 | Ruan et al.: speech 2.93× keyboard for English (153 v 52 wpm); pooled English+Mandarin 5.30% v 11.22% corrected, 1.30% v 0.79% left; IMWUT 1(4), Dec 2017 | arXiv 1608.07323 |
| S2 | §2 | AIR Media-Tech, 8 Jun 2026: 18,000 English-language channels (US, UK, CA, AU), primary analysis 100k–1M monthly views; "Channels that went dark for 14+ days three or more times a year got fewer views per video"; "This is correlational data, not causal" | air.io (posting study) |
| S3 | §3 | Buffer, 13 Aug 2025: 2.1M feed posts, 102,000 accounts, fixed effects; +0.12% (1–2 posts), +0.26% (3–5) weekly follower growth v none; reach per post about 12% higher at 3–5 than 1–2 | buffer.com/library/how-often-to-post-on-instagram/ |
| S4 | §4 | Dai, Milkman and Riis, Management Science 60(10), 2014, 2563–2582: "diet" searches, gym visits, commitments rise after temporal landmarks ("the outset of a new week, month, year, or semester; a birthday; a holiday"); "relegate past imperfections to a previous period" | EconPapers record |
| S5 | §5 | Gollwitzer and Sheeran 2006: meta-analysis of 94 independent tests; "the when, where, and how of goal striving in advance"; medium-to-large effect, d = .65; AESP 38, 69–119 | KOPS record |
| S6 | §6 | Masicampo and Baumeister, JPSP 101(4), 2011, 667–683: unfinished goals caused intrusive thoughts in a reading task and hurt an anagram task; "formulate specific plans for their unfulfilled goals" eliminated the effects; "Once a plan is made, the drive to attain a goal is suspended" | BVB library record |
| S7 | §7 | PB3 set the cut order: Instagram three to one (frees 1.0 h); replies to next week; video to about 8 minutes (frees an estimated 1.0 h); upload moved up to 7 days, once; log never cut (PB3, D2) | others/PB3 D2 |
| S8 | Deliverable | D2: every week 1–12 sums to 6.0 (72.0 total); upload 7 public Tuesday 30 March 2027, so Q1 holds seven uploads "as PB1's Q1 review expects (uploads 1–7)"; review Monday 5 April 2027 | arithmetic; others/PB1 D3; case-facts |
| S9 | Template | T2: PB3's 3-hour plan is one anchor every four weeks, one Instagram post a week, one email per anchor, 11.75 h per four weeks; the unit's four weeks sum 3.0, 3.0, 3.0, 2.75 | others/PB3 D2; arithmetic |
| S10 | Sources | Monsell, Sumner and Waters, "Task-set reconfiguration with predictable and unpredictable task switches", Memory & Cognition 31(3), 2003, 327–342, at orca.cardiff.ac.uk/33842 (and the §5 quotation it carries) | ORCA record |
| S11 | Unsure list | "PPC Land dates the FAQ's publication to 2 Sep 2026 in the German Help Centre" (YouTube performance FAQ, answer 141805) | PPC Land |

## Table (sample)

| Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| §1 | S1 Ruan et al. speech v keyboard | https://www.arxiv.org/abs/1608.07323?context=cs and the arXiv PDF | PASS | Abstract: "2.93 times faster (153 vs. 52 WPM)" for English; 5.30% v 11.22% corrected, 1.30% v 0.79% uncorrected. The paper's per-language rates (English 3.93 v 4.72 and 0.55 v 0.35; Mandarin 6.67 v 17.73 and 2.06 v 1.22) average to the abstract's figures, so "across English and Mandarin together" holds. IMWUT 1(4), Dec 2017; v1 25 Aug 2016, v2 17 Jan 2018. The recogniser was Baidu Deep Speech 2, a 2015 publication; "2016 recognisers" is loose, not wrong enough to fix. |
| §2 | S2 AIR Media-Tech, posting study | https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | Dated 8 Jun 2026; 18,000 English-language channels, US, UK, Canada, Australia (India excluded); primary analysis at 100K–1M monthly views; both quotations exact; the schedule finding is views per subscriber at the same number of videos. The page gives no effect size or method for that finding, which the unit's "vendor, correlational" label covers. |
| §3 | S3 Buffer posting frequency | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | Kirsti Lang, 13 Aug 2025; 2.1 million posts, 102K accounts; photos, Reels, carousels, Stories excluded; fixed-effects model; +0.12% and +0.26% against no-post weeks; about 12% more reach per post at 3–5 than at 1–2. The 0.14-point step and 140 × 0.0014 ≈ 0.2 are correct. |
| §4 | S4 Dai, Milkman and Riis | https://econpapers.repec.org/RePEc:inm:ormnsc:v:60:y:2014:i:10:p:2563-2582 | PASS | Management Science 60(10), 2014, 2563–2582; both quotations exact; searches for "diet" (Study 1), gym visits (Study 2), commitments (Study 3); three archival field studies. |
| §5 | S5 Gollwitzer and Sheeran | https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f | PASS | AESP 38, 2006, 69–119; "94 independent tests"; "the when, where, and how of goal striving in advance"; "medium-to-large magnitude (d= .65)". |
| §6 | S6 Masicampo and Baumeister | https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_918752704 | PASS | JPSP 101(4), 2011, 667–683, doi 10.1037/a0024192; intrusive thoughts in a reading task (Studies 1, 5B), anagram task (Study 4); both quotations exact. |
| §7 | S7 PB3's cut order | others/PB3 D2 | PASS | PB3 D2 steps 1–4 and "Never cut: the log" match, with the hours freed (1.0; estimated 1.0). PB3's step 2 frees "up to 0.6 hours", which the unit omits without changing the order. |
| Deliverable | S8 D2 sums, upload 7, Q1 review | script; others/PB1 D3; case-facts.md | PASS | Run-in 4.25, 1.5, 5.25, 5.75; weeks 1–12 each 6.0; total 72.0. Every date and weekday checked by script. PB1 D3: "Q1 review, Monday 5 April 2027 · YouTube uploads 1–7". Upload dates match the register. |
| Template | S9 T2 rules for 3 hours | others/PB3 D2; arithmetic | PASS | PB3's 3-hour column: 2.0, 4.0, 1.0, 2.0, 1.5, 0.25, 1.0 = 11.75. The unit's four weeks sum 3.0, 3.0, 3.0, 2.75 and rebuild every PB3 line exactly. |
| Sources | S10 Monsell, Sumner and Waters | https://orca.cardiff.ac.uk/33842 | PASS | Memory & Cognition 31(3), 2003, 327–342; quotation exact; digit high/low and odd/even tasks. |
| Unsure list | S11 PPC Land and the FAQ's date | https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/ | FAIL | PPC Land (2 Sep 2026) dates a German-language recommendations FAQ posted that day in the German YouTube Help community forum, not the Help Centre. The performance FAQ is one of two accompanying Help Centre pages, for which it gives only a 2026 footer year. The unit's line moves the date onto the wrong document and the wrong place. Erratum PB4-1. |

## Also checked

| Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| §1 | Instagram original content guidelines | https://creators.instagram.com/original-content-guidelines/ | PASS | All three quotations exact; "low-effort edits (e.g. borders, watermarks, speed changes, just crediting the original creator)"; no date but a 2026 footer. |
| §1 | Instagram, 30 Apr 2026, Reels to photos and carousels | https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/ | PASS | "these protections were already in place for reels, and are now being applied to photos and carousels". |
| §1 | Shiffman, Stone and Hufford, abstract | https://citedrive.com/en/discovery/ecological-momentary-assessment | PASS | "Assessment in clinical psychology typically relies on global retrospective self-reports"; "recall bias"; "maximize ecological validity". Year 2008, volume and pages stay unconfirmed (see Not checked). |
| §2 | YouTube Help 13615784, two quotations | https://support.google.com/youtube/answer/13615784?hl=en | PASS | Both exact. |
| §2 | YouTube Help 141805, breaks | https://support.google.com/youtube/answer/141805?hl=en | PASS | Three quotations exact; no sample size, period, method or page date. |
| §2 | vidIQ, 12–51 band | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | Bands 0, 1–11, 12–51, 52+; 8.65% in the 12–51 band; published 11 Sep 2026. The title the unit gives is not the page's (errata PB4-3, PB4-4). |
| §2 | Tasty Edits rule of thumb | https://www.tastyedits.com/how-long-does-it-take-to-edit-a-video/ | PASS | Quotation exact; 19 May 2021, updated 17 Sep 2026; no method or sample; 5 to 10 hours for 10 minutes is correct. |
| §3 | AIR Media-Tech, Shorts study | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels | PASS | 28 May 2026; 18,000 English-language channels; March 2025 to March 2026; quotation exact; "this is correlational data". |
| §3 | Fanpage Karma format reach | https://www.fanpagekarma.com/insights/instagram-format-reach/ | PASS | 7 Aug 2026, modified 28 Aug 2026; more than 3 million posts, January to April 2026; 4.9%, 3.5%, 2.6%; quotation exact; no account count. |
| §3 | Socialinsider: figures "do not match its own 45% headline" | https://www.socialinsider.io/blog/how-long-does-it-take-for-reels-to-get-views/ | FAIL | Two samples: confirmed (40M Reels from 450K accounts; 25,503,389 Reels). The mismatch is not there: the page gives about 14,578 views by day 10 and "just above 8,000" at day 20, a fall of about 45%, which is what "After 10 days ... decreasing by 45%" says. The 17,100 to 14,578 fall (about 15%) is the period before day 10. What the page lacks is a stated end point. Erratum PB4-2. |
| §3 | TechCrunch, 8 Nov 2022 | https://techcrunch.com/2022/11/08/instagram-scheduling-tool-all-professional-accounts | PASS | Title as listed; all professional accounts; "posts, reels and carousels"; "up to 75 days in advance". |
| §3 | Social Media Today, 1 Mar 2026 | https://www.socialmediatoday.com/news/instagram-opens-up-content-scheduling-to-all-users/813448/ | PASS | First sentence: creator tools "available to all public accounts"; scheduling, the insights dashboard and trending audio are listed among them; no quoted Instagram statement; no horizon. |
| §4 | Kivetz, Urminsky and Zheng | https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal | PASS | JMR 43, Feb 2006, 39–58; three quotations exact; the head-start card is the 12-stamp card with two bonus stamps. |
| §4 | YouTube Help series quotations | answers 13615784 and 141805 (URLs above) | PASS | All three exact; the second continues ", or work with the same host". |
| §5 | Rubinstein, Meyer and Evans via APA release | https://www.newswise.com/articles/is-multitasking-more-efficient | PASS | 5 Aug 2001; JEP:HPP 27(4); young adults, four experiments; quotation exact; less familiar tasks cost more; maths problems and classifying geometric objects. |
| §5 | Leroy 2009 | https://econpapers.repec.org/RePEc:eee:jobhdp:v:109:y:2009:i:2:p:168-181 | PASS | OBHDP 109(2), 168–181; two experiments; unfinished task; finishing not sufficient; time pressure. The source has "people" in lower case (erratum PB4-5). |
| §5 | APA, "40 percent" | https://www.apa.org/topics/research/multitasking | PASS | 20 Mar 2006; quotation exact; attributed to Meyer; no study cited. |
| §3 | 0.2 followers a week and PB1 I4's 0.36 | others/PB3 §6; others/PB1 §3, D1 I4 | PASS | Both as the units give them. |
| §1 | PB1 D2 capture quotation; PB3 D2 "24.0 of 24" | others/PB1 D2; others/PB3 D2 | PASS | Exact. |
| §1 | PB2 D4 promise quotation | others/PB2 D4 | PASS | Exact. |
| Template | T2 rules for 10 hours | others/PB3 D2; arithmetic | PASS | 9.75 a week, 39.0 per four weeks, each PB3 line rebuilt; override weeks 10.0 and 8.0; PB3's override and cut order as stated. |
| §7 | PB1 verdict 2 and the 7-hour line | others/PB1 D2, D3 | PASS | "over 7 hours in 3 or more weeks of the quarter"; "A week over 7 hours is logged as over budget". |
| Unsure list | CiteDrive dates Shiffman et al. 2007, no volume | https://citedrive.com/en/discovery/ecological-momentary-assessment | PASS | Year 2007; journal, volume and pages not shown. |
| Deliverable | D2 run-in: PB5 D A 0.75 h; PB2 D5 run 1 | others/PB5 D A; others/PB2 D5 | PASS | PB5: 0.5 to R1 (4.25), 0.25 to R2 (1.5). PB2: run 1 in the week of 7 December 2026. |
| §1 | Cadence rule from PB10 §5 | others/PB10 §5 | PASS | "two or more pieces in a quarter took more than two weekends, in two consecutive quarters". |
| §2 | YouTube Help 1270709 (scheduling; strike penalty period) | https://support.google.com/youtube/answer/1270709?hl=en | unverifiable | Not opened: see Not checked. |
| §3 | Instagram Help scheduling page summary | https://help.instagram.com/iphone-app/439971288310029 | unverifiable | Not opened: see Not checked. |

Other pointers read and found to hold, not counted as claims: PB1 §1 (labels), §7, §8; PB1 D3 (stop rule; verdict 3 from Q2; Q2 review uploads 8–13); PB3 §3, §4, §5, §6; PB5 §1 (one clip per step); PB10 §5 and §8 (two Reels fewer; recovery weeks at 6.5).

## Not checked

- `https://support.google.com/youtube/answer/1270709?hl=en`: WebSearch was refused (the session's search budget, shared by every agent, was used up); retried once, refused again. No search returned the URL, so the web rule barred fetching it.
- `https://help.instagram.com/iphone-app/439971288310029`: same refusal; not fetched.
- `https://pubmed.ncbi.nlm.nih.gov/18509902/` (Shiffman et al.: year, volume, pages): fetched once, the page returned no article content; not retried. The unit's Unsure list already carries this.
- WebSearch: 22 searches ran; three more were refused for the budget reason above. 33 fetches ran.
- Quotations were confirmed through the fetch tool's short verbatim extracts, not by reading whole pages.

## Failure rate

Sample: 1 FAIL in 11 (9.1%). That is not more than one in ten, so the full audit was not triggered. All checks: 38 claims, 34 PASS, 2 FAIL, 0 STALE, 2 unverifiable. 24 of the unit's 26 listed sources were opened.

## Counts

Words (`wc -w`): 10,438. `##` sections: 11. Cited claims in the unit: 111 (48 resting on an outside source, 63 on a named unit of the course). Counted by reading, one per sentence or table row; the 26 entries of the Sources list are references and are not counted.

| Section | Outside source | Other unit | Total |
|---|---|---|---|
| §1 | 4 | 10 | 14 |
| §2 | 8 | 3 | 11 |
| §3 | 8 | 2 | 10 |
| §4 | 4 | 4 | 8 |
| §5 | 6 | 0 | 6 |
| §6 | 1 | 3 | 4 |
| §7 | 1 | 10 | 11 |
| Deliverable | 4 | 19 | 23 |
| Template | 3 | 9 | 12 |
| Sources | 0 | 0 | 0 |
| Unsure list | 9 | 3 | 12 |
| **Total** | **48** | **63** | **111** |

## Figures

1. §2 matrix, "Three pieces in the system at once": PASS. Piece 3 is captured in weeks 1–2 (9 and 16 Jan), edited and cut in weeks 3–4 (24 and 31 Jan) and published in week 5 (2 Feb); pieces 4 and 5 follow a fortnight apart, as D2 has them. "6 posts" is §3's. The caption names §2 and D2.
2. §7 decision, "A lost week: what moves": PASS. Each outcome is in §7's two bullets; the caption's summary of PB3 D2 and PB1 D2's 7-hour line is correct. The 6.5 h in two outcomes is the unit's own figure (see flag PB4-6).
3. §7 stacked bars: PASS. Week A 6.0 and week B 6.0 match D1 E line by line; both recovery rows sum to 6.5 and match §7 (edit 3.0, packaging 1.0, two posts 1.0, scheduling 0.25, capture 1.0, log 0.25). The 0.25 under "Publish, replies" in the recovery rows is scheduling alone (flag PB4-6).

## Deliverable

D1, D2, T1 and T2 are present in full. D1 and D2 follow from the body: every line names its section or unit, the hours table matches PB1 and PB3, and every sum and date is right. T1 and T2 can be filled without the body; each blank says what goes in it, and the 3- and 10-hour rules rebuild PB3's totals exactly. Mara's facts agree with `case-facts.md` (week pattern, run-in, upload dates, seasons, backlog, piece rules, lost-week rules).

One gap, reported as a flag: the 6.5-hour recovery weeks leave out the recovery week's own reply slots. With them the week after a lost week A is 6.75 hours, and the week after a lost week B is 7.0, which is at PB1's line and not under it. The unit never says the slots are dropped.

## Course goal and standard

The unit serves the second outcome directly: it gives a publishing system and a twelve-week calendar inside a 6-hour budget, and hands PB10 the log and the rules its reviews read. Evidence and inference are kept apart: transfers from other settings are marked as the unit's inference, conventions as "her rule", and §4 and §5 say what the evidence does not support. Nothing reads as advice without evidence.

Three observations that need no erratum:
- The header says `search: off`, but the unit dates live platform facts to 12 Nov 2026 and adds sources no earlier unit carries. The six-month staleness check should treat it as a search-on unit.
- Tasty Edits is not one of Part 5's source types. The unit labels it weak and keeps it out of the deliverable as evidence.
- The unit is 10,438 words against the brief's 2,000–6,000 range. About 5,980 words are body (§1–§7, figures included); the rest is deliverable, template, sources and notes.

## Verdict

PB4: **PASS**. Sample failure rate 1 in 11; full audit not run. Two errata on claims (one should-fix, one minor), three minor citation errata, one flag.

## Most consequential errors

1. §7 and D1 F: the recovery weeks after a lost week are given as 6.5 hours, but only if that week's reply slots are skipped, which the unit does not say. Counted, the week after a lost cut window is 7.0 hours, at the over-budget line. This is the one finding that touches the reader's own calendar (flag PB4-6).
2. §3: the unit says Socialinsider's figures contradict its own 45% headline. They do not: day 10 to day 20 on the page is a fall of about 45%. The source is still weak, for other reasons the unit also gives (PB4-2).
3. Unsure list: PPC Land's 2 Sep 2026 date belongs to a German forum FAQ on recommendations, not to the Help Centre performance FAQ the unit quotes (PB4-1).

## Bibliography

No source to mark failed. Retitle vidIQ's 11 Sep 2026 study to "Reaching 1,000 YouTube Subscribers: What 32.9 Million Channels Reveal" (PB1 uses the same wrong label). To add only if the Unsure list is to link what it names: PPC Land, "YouTube finds no link between upload breaks and view counts", 2 Sep 2026, https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/. Two sources not opened in this audit: YouTube Help 1270709 and the Instagram Help scheduling page.

## Changelog

Audit 1 · PB4 · 14 Nov 2026 · claude-fable-5-2 · PASS: sample 1 FAIL in 11, 38 claims checked (34 PASS, 2 FAIL, 2 unverifiable), three figures pass; 5 errata (1 should-fix, 4 minor) and 1 flag (recovery-week reply slots).

## Errata

**PB4-1** · minor · FAIL · Unsure list
- Current: `PPC Land dates the FAQ's publication to 2 Sep 2026 in the German Help Centre, and the English page's own date was not seen`
- Fix: `PPC Land (2 Sep 2026) reports a German-language recommendations FAQ posted that day in the German YouTube Help community forum, with the performance FAQ as an accompanying Help Centre page that it does not date, and the English page's own date was not seen`
- Basis: PPC Land places the dated FAQ ("FAQ: Wie funktionieren die Empfehlungen?") in the German YouTube Help community forum; the performance FAQ is one of two accompanying Help Centre pages with only a 2026 footer year. https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/

**PB4-2** · should-fix · FAIL · §3
- Current: `whose page gives two different samples and day-by-day figures that do not match its own 45% headline`
- Fix: `whose page gives two different samples and does not say what period its 45% fall after day 10 covers`
- Basis: the page gives about 14,578 views by day 10 and "just above 8,000" at the 20-day mark, a fall of about 45% (derived), so its figures do not contradict the headline; it states no end point for the 45%. PB3 §3 calls the same page unclear without claiming a mismatch. https://www.socialinsider.io/blog/how-long-does-it-take-for-reels-to-get-views/

**PB4-3** · minor · other · Sources
- Current: `- vidIQ Research, "Uploads and reaching 1,000 subscribers", 11 Sep 2026. https://vidiq.com/research/youtube-uploads-1000-subscribers/`
- Fix: `- vidIQ Research, "Reaching 1,000 YouTube Subscribers: What 32.9 Million Channels Reveal", 11 Sep 2026. https://vidiq.com/research/youtube-uploads-1000-subscribers/`
- Basis: the page's headline, published September 11, 2026; the quoted phrase appears nowhere on it. PB1 carries the same label; change both together. https://vidiq.com/research/youtube-uploads-1000-subscribers/

**PB4-4** · minor · other · §2
- Current: `[vidIQ, Uploads and reaching 1,000 subscribers, 11 Sep 2026]`
- Fix: `[vidIQ, Reaching 1,000 YouTube Subscribers, 11 Sep 2026]`
- Basis: as PB4-3. https://vidiq.com/research/youtube-uploads-1000-subscribers/

**PB4-5** · minor · other · §5
- Current: `found that "People need to stop thinking about one task`
- Fix: `found that "people need to stop thinking about one task`
- Basis: the abstract has the words mid-sentence in lower case; quotation marks hold the source's exact words. The fresh check noted it and proposed no fix. https://econpapers.repec.org/RePEc:eee:jobhdp:v:109:y:2009:i:2:p:168-181

**PB4-6** · flag · should-fix · other · §7 (also D1 F, both §7 figures, `case-facts.md`, PB10 §8)
- Current: `With capture 1.0 and the log 0.25 that week is 6.5 hours.`
- Fix (a suggestion; needs a decision): `With capture 1.0 and the log 0.25 that week is 6.5 hours, its own reply slot skipped (PB3's step 2); with the slot kept it is 6.75, and the recovery week after a lost week B, which has two reply slots, is 7.0.`
- Basis: D1 E gives week B one reply slot (0.25) and week A two (0.5). §7's 6.5 hours counts neither, and the unit says only that replies "wait for the next slots". With the slots, the weeks are 6.75 and 7.0; 7.0 is at PB1's line, not under it (PB10 §8). The 6.5 figure is also in the register, PB10 §8 and both §7 figures, so it is not applied as an erratum. Internal arithmetic; no URL.
