---
audit: stratified-sample audit (Audit 2)
units: PB5, PB6, PB7, PB8
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Fable 5.2 (claude-fable-5-2; accepted by Pedro for row F-PB, 14 Nov 2026), search on
date: 2026-11-14
chat: one fresh Fable agent per unit, isolated on its packet, in session https://claude.ai/code/session_01KMmgQyKuvCKpHpSB9xzQYA (row F-PB part 1)
verdicts: PB5 PASS · PB6 PASS · PB7 PASS · PB8 PASS
---

# Audit 2 · PB · PB5, PB6, PB7, PB8

Built by script (`f-pb/tools/build_audits.py`) from each agent's `out/audit.md`, saved verbatim under `audits/personal-brand/f-pb/<code>/` before any erratum was applied. Errata applied by `f-pb/tools/apply.py`; what was applied, held and flagged is in `f-pb/applied.json`.

---

<!-- PB5: f-pb/PB5/audit.md, verbatim -->

Model: claude-fable-5-2

# Stratified-sample audit · PB5 · Production craft with a phone · 14 November 2026 · search on

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2, 14 Nov 2026. Read only `/home/claude/fpb/PB5`; wrote only `out/`. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool used.
- Unit: `unit.md` (PB5, written 2026-11-12 by Opus 5.5, search flag off), 12,497 words (`wc -w`), 14 `##` sections.
- Web rule: WebSearch first; WebFetch only on a URL a search in this agent returned verbatim.
- `out/` was empty at the start: this is not a resumed run.
- Web use: 18 searches, 20 fetches. The search budget, shared by every agent in the turn, ran out after the 18th search; the sample was complete by then, and the sources left unopened are listed under Not checked.
- The earlier fresh check (`fresh-check-PB5.md`) was read to avoid re-reporting applied fixes; none of its verdicts is reused.

## Sample (recorded before any check)

One claim per `##` section, 14 in all.

| # | Section | Claim sampled | Source the unit cites |
|---|---|---|---|
| 1 | §1 Filming | Levoy and Pritch quotation: "For smartphone cameras, which have small lenses and sensors, a major source of noise is the natural variation of the number of photons entering the lens, called shot noise"; Google Research blog, 14 Nov 2018 | research.google/blog/night-sight-seeing-in-the-dark-on-pixel-phones/ |
| 2 | §2 Audio | Newman and Schwarz experiment 1: 97 Mechanical Turk workers; good audio rated higher by 0.60 (95% CI 0.41 to 0.79); 0.93 / 0.69 / 0.51 / 0.33 on the four measures | Science Communication 40(2), 2018, 246–257 |
| 3 | §3 Opening | Socialinsider: 9,771,822 organic Reels of brand accounts with 1,000 to 1 million followers, Jan–Jun 2026; average skip rate 65.50% at 1–5K, 60.50% at 100K–1M | socialinsider.io/blog/instagram-reels-statistics/ |
| 4 | §4 Structure | End screens "can be added to the last 5–20 seconds of a video", the video "has to be at least 25 seconds long", not shown on mobile web, iPad excepted | YouTube Help answer 6388789 |
| 5 | §5 Shorts and Reels | "You can now create YouTube Shorts up to three minutes in length", for uploads after 15 October 2024; a Short over one minute with an active Content ID claim "will be blocked globally on YouTube" | YouTube Help answer 15424877 |
| 6 | §6 Carousels | Instagram: "You can upload up to 20 photos and videos and share them as a single post in Instagram Feed" | Instagram Help Centre 269314186824048 |
| 7 | §7 Titles and thumbnails | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%" | YouTube Help answer 7628154 |
| 8 | §8 Captions and contrast | WCAG: contrast ratio "at least 4.5:1", large text 3:1, "18 point text or 14 point bold text", formula "(L1 + 0.05) / (L2 + 0.05)" | W3C Understanding SC 1.4.3 |
| 9 | §9 Editing | Tasty Edits: "As a rule of thumb, expect 30 minutes to an hour of editing time per minute of finished video"; published 19 May 2021, updated 17 Sep 2026 | tastyedits.com/how-long-does-it-take-to-edit-a-video/ |
| 10 | §10 What not to buy | Edits is free and exports without a watermark (Instagram, 22 Apr 2025) | creators.instagram.com/blog/edits-video-creation-app |
| 11 | Deliverable | Thumbnail: 16:9, 3840 × 2160 or at least 640 wide, JPG or PNG, under 2 MB from the phone | YouTube Help answer 72431 |
| 12 | Templates | YouTube's chapter rules: first chapter at 00:00, at least three, each at least 10 seconds | YouTube Help answer 9884579 |
| 13 | Sources | McFarland, Pinson, Ford, Webster, Ingram, Hanes and Anderson, *Relating Audio and Video Quality Using CIF Video*, NTIA TM-10-472, ITS, Sep 2010 | its.ntia.gov/publications/download/10-472.pdf |
| 14 | Unsure list | "the ANU record confirms the DOI and the abstract but shows no volume or pages" (Newman and Schwarz 2018) | ANU Open Research record |

## Table (the sample, 14 claims)

| # | Section | Claim | Source opened | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §1 Filming | Levoy and Pritch: shot-noise sentence; Google Research blog, 14 Nov 2018 | https://research.google/blog/night-sight-seeing-in-the-dark-on-pixel-phones/ | PASS | Page dated November 14, 2018, by Marc Levoy and Yael Pritch; the shot-noise and read-noise sentences read as quoted. |
| 2 | §2 Audio | Newman and Schwarz exp. 1: 97 Mechanical Turk workers; 0.60 (0.41–0.79); 0.93 / 0.69 / 0.51 / 0.33 | https://www.Gwern.net/doc/design/visualization/2018-newman.pdf | PASS | Full text opened (the URL was returned by a search in this run): 97 workers, "2- to 3-minute segments", the "Large Room" filter, 0.60 [.41, .79], 0.93, 0.69, 0.51, 0.33. This closes the gap the fresh check left open. |
| 3 | §3 Opening | Socialinsider: 9,771,822 organic Reels, brands 1K–1M, Jan–Jun 2026; skip rate 65.50% (1–5K) to 60.50% (100K–1M) | https://socialinsider.io/blog/instagram-reels-statistics/ | PASS | Published Jun 24, 2026, updated Nov 6, 2026; every figure as stated; organic posts only. |
| 4 | §4 Structure | End screens: last 5–20 seconds; video at least 25 seconds; not seen on mobile web, iPad excepted | https://support.google.com/youtube/answer/6388789 | PASS | All three statements on the page, word for word where quoted. |
| 5 | §5 Shorts and Reels | Shorts up to three minutes, uploads after 15 October 2024; Content ID block over one minute | https://support.google.com/youtube/answer/15424877?hl=en-GB | PASS | Sentences as quoted; "standard" channels after 15 October 2024 (Official Artist Channels have a later date, which the unit does not need). |
| 6 | §6 Carousels | Instagram: "You can upload up to 20 photos and videos and share them as a single post in Instagram Feed" | https://help.instagram.com/iphone-app/269314186824048 | PASS | Word for word; page title as the unit gives it. |
| 7 | §7 Titles and thumbnails | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%" | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | Word for word. |
| 8 | §8 Captions and contrast | WCAG SC 1.4.3: 4.5:1; large text 3:1; "18 point text or 14 point bold text"; "(L1 + 0.05) / (L2 + 0.05)" | https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum | PASS | All four elements on the page; it covers images of text. |
| 9 | §9 Editing | Tasty Edits rule of thumb, 30 minutes to an hour per finished minute; published 19 May 2021, updated 17 Sep 2026 | https://www.tastyedits.com/how-long-does-it-take-to-edit-a-video/ | PASS | Both quoted sentences word for word; author Alex Lefkowitz; both dates; no method or data, as the unit says. |
| 10 | §10 What not to buy | Edits is free and exports without a watermark (Instagram, 22 Apr 2025) | https://creators.instagram.com/blog/edits-video-creation-app | unverifiable | The cited URL answered 302 to edits.instagram.com/blog/edits-video-creation-app/; a redirect is not followed under the web rule. Not a FAIL. |
| 11 | Deliverable | Thumbnail: 16:9, 3840 × 2160 or at least 640 wide, JPG or PNG, under 2 MB from the phone | https://support.google.com/youtube/answer/72431?hl=en | PASS | 16:9 for videos, 3840 x 2160, minimum width 640, JPG or PNG, 2 MB for video thumbnails on mobile. |
| 12 | Templates | YouTube chapter rules: first at 00:00, at least three, each at least 10 seconds | https://support.google.com/youtube/answer/9884579?hl=en | PASS | The three rules word for word, and §4's "add info and context" sentence. |
| 13 | Sources | McFarland, Pinson, Ford, Webster, Ingram, Hanes and Anderson, NTIA TM-10-472, Sep 2010 | https://its.ntia.gov/publications/download/10-472.pdf | PASS | Title page as cited. The report's own data sheet and the ITS publication page spell the sixth author "Haines"; the unit follows the title page. |
| 14 | Unsure list | The ANU record confirms the DOI and the abstract but shows no volume or pages | https://openresearch-repository.anu.edu.au/items/67350c38-062b-4837-84c9-81419829d59d | PASS | Record opened: DOI and the "Despite identical content" sentence; no volume, issue or pages; the file is restricted. |

## Also checked (beyond the sample, while a source was open; counted in the totals)

| # | Section | Claim | Source opened | Verdict | Note |
|---|---|---|---|---|---|
| 15 | §2 Audio | Newman and Schwarz exp. 2: 99 workers, Science Friday, "bad phone line", 0.19 (0.03–0.36) | https://www.Gwern.net/doc/design/visualization/2018-newman.pdf | PASS |  |
| 16 | §2 Audio | Comprehension: 64% of exp. 1 answered correctly about both talks; pattern held | https://www.Gwern.net/doc/design/visualization/2018-newman.pdf | PASS |  |
| 17 | §2 Audio | "Despite identical content, people evaluated the research and researcher less favorably when the audio quality was low." | https://www.Gwern.net/doc/design/visualization/2018-newman.pdf | PASS | Also on the ANU record. |
| 18 | §2 Audio / Sources | Reference: Science Communication 40(2), 2018, 246–257, doi 10.1177/1075547018759345 | https://www.Gwern.net/doc/design/visualization/2018-newman.pdf | PASS |  |
| 19 | §2 Audio | NTIA TM-10-472: video 78% and audio 10% of variance; speech-only 90% and 3%; both caveats quoted | https://its.ntia.gov/publications/download/10-472.pdf | PASS | CIF video, coding impairments, as the unit describes. |
| 20 | §2 Audio | Audio-Technica: 6 dB per doubling of distance in a free field; "too much of the room"; page undated | https://www.audio-technica.com/en-us/support/audio-solutions-question-week-tips-placing-microphones-get-best-possible-sound | PASS |  |
| 21 | §1 Filming | Levoy and Pritch is about still photographs (the unit says applying it to video is its own inference) | https://research.google/blog/night-sight-seeing-in-the-dark-on-pixel-phones/ | PASS |  |
| 22 | §1 Filming | A video "with a square or vertical aspect ratio up to three minutes in length" is categorised as a Short | https://support.google.com/youtube/answer/15424877?hl=en-GB | PASS |  |
| 23 | §3 Opening | Instagram skip-rate definition, first 3 seconds, replacing view rate; Social Media Today, 24 Aug 2025 | https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/ | PASS | Quotation exact; article by Andrew Hutchinson, August 24, 2025; the change comes "in the coming weeks". |
| 24 | §3 Opening | vidIQ: "Confirm the title and thumbnail promise immediately…"; 40–55% at 5–15 minutes; "vidIQ guidance for target bands"; updated 21 Jul 2026 | https://vidiq.com/blog/post/average-view-duration/ | PASS | No sample given, as the unit says. |
| 25 | §3 Opening | Socialinsider bracket counts sum to 5 more than the stated total; "less than 5000" in the method, "1–5K" in the table | https://socialinsider.io/blog/instagram-reels-statistics/ | PASS | 974,294 + 693,768 + 2,648,482 + 1,320,562 + 4,134,721 = 9,771,827. |
| 26 | §5 Shorts and Reels | Socialinsider reach rate by length: 5.20 / 5.60 / 5.30 / 4.30 / 3.50% | https://socialinsider.io/blog/instagram-reels-statistics/ | PASS |  |
| 27 | §1, §3, §5 | Meta Creators, 17 Jun 2022: 9:16; blurry video; beginning, middle and end / hook or payoff; cover photo; visibly recycled | https://creators.facebook.com/reels-best-practices-tips-tricks | PASS | Dated June 17, 2022; covers Reels on Facebook and Instagram. The tail of the hook sentence ("like a big reveal, punchline or plot twist") was returned truncated and is not confirmed word for word. |
| 28 | §4 Structure | vidIQ: "APV (%) = (AVD / total video length) x 100"; "Use an end screen and a clear verbal bridge to another relevant video." | https://vidiq.com/blog/post/average-view-duration/ | PASS |  |
| 29 | §7 and §5 | Answer 72431: "upload your own if your account is verified"; rejection and strike; 30 days or termination; 50 MB from a computer; Shorts thumbnails on a computer only | https://support.google.com/youtube/answer/72431?hl=en | PASS |  |
| 30 | §7 Titles and thumbnails | Answer 7628154: the clickbait sentence with lower than expected impressions; the wider range under a week or under 100 views | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS |  |
| 31 | §8 Captions and contrast | The seven contrast ratios (17.04, 14.12, 5.62, 4.65, 3.03, 2.25, 7.58) | recomputed by script with the W3C formula, https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum | PASS | All seven match to two decimals. |
| 32 | Sources | Sources line: Social Media Today, "Instagram adds retention insights for Reels", 24 Aug 2025 | https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/ | FAIL | The article's headline is "Instagram Adds Retention Metrics for Reels" (H1 and title tag); the words in quotation marks are the URL slug, not the title. Minor: erratum PB5-1. |
| 33 | Unsure list | End screens: "YouTube's steps start at studio.youtube.com"; the page is silent on the phone app | https://support.google.com/youtube/answer/6388789 | PASS |  |
| 34 | §3, Sources | Socialinsider dated 24 Jun 2026, updated 6 Nov 2026 | https://socialinsider.io/blog/instagram-reels-statistics/ | PASS |  |

## Not checked

The WebSearch budget ran out after 18 searches (the limit is shared by every agent in the turn). The refusal was retried once and refused again, so it is recorded as "not checked: permission". Every source below is cited by the unit and was not opened in this run, because no search could return its URL; none of them carries a sampled claim except the first.

- https://creators.instagram.com/blog/edits-video-creation-app: redirect (302 to edits.instagram.com), not followed
- WebSearch: budget used up after 18 searches (limit shared by every agent in the turn); refused, retried once, refused again; not checked: permission
- https://support.google.com/youtube/answer/1722171?hl=en: no search could return it (WebSearch refused)
- https://support.google.com/youtube/answer/6373554?hl=en-GB: no search could return it (WebSearch refused)
- https://support.google.com/youtube/answer/9314415: no search could return it (WebSearch refused)
- https://support.google.com/youtube/answer/12942217?hl=en: no search could return it (WebSearch refused)
- https://support.google.com/youtube/answer/12220281: no search could return it (WebSearch refused)
- https://support.google.com/youtube/answer/2801973?hl=en-GB: no search could return it (WebSearch refused)
- https://support.google.com/youtube/answer/16391400?hl=en: no search could return it (WebSearch refused)
- https://blog.google/intl/en-in/products/platforms/strengthening-enforcement-against-egregious-clickbait-on-youtube/: no search could return it (WebSearch refused)
- https://docs.cloud.sennheiser.com/en-us/lavalier-mics/lavalier-mics_instruction_manual_05_2026_en.pdf: WebSearch refused
- https://rnid.org.uk/information-and-support/technology-and-products/how-to-use-video-captions-subtitles-social-media-accessibility/instagram/: WebSearch refused twice
- https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html: no search could return it (WebSearch refused)
- https://www.netinfluencer.com/instagram-announces-3-minute-reels-and-vertical-grids/: no search could return it (WebSearch refused)
- https://www.inro.social/blog/instagram-reels-length: no search could return it (WebSearch refused)
- https://www.socialmediatoday.com/news/instagram-adds-support-phone-camera-aspect-ratio-images: no search could return it (WebSearch refused)
- https://socialmediatoday.com/news/instagram-update-reels-camera-with-improved-functions/806247: no search could return it (WebSearch refused)
- https://www.planoly.com/blog/guide-to-instagrams-new-vertical-grid.md: no search could return it (WebSearch refused)
- https://metricool.com/instagram-increases-carousel-content-limit/: no search could return it (WebSearch refused)
- https://metricool.com/instagram-image-size/: no search could return it (WebSearch refused)
- https://liahaberman.substack.com/p/the-best-instagram-content-formats: no search could return it (WebSearch refused)
- https://uppbeat.io/blog/creator-news/whats-working-on-instagram-right-now-carousels-and-sends-says-adam-mosseri: no search could return it (WebSearch refused)

## Failure rate

- Sample: 14 claims; 13 PASS, 0 FAIL, 0 STALE, 1 unverifiable (the Edits page, a redirect). Failure rate 0 in 14 (0%). The rule (more than one in ten) is not met, so no full audit was run.
- All claims checked: 34 (14 sampled, 20 also checked); 32 PASS, 1 FAIL (a title in the Sources list, minor), 0 STALE, 1 unverifiable.

## Counts

- Words: 12,497 (`wc -w unit.md`). `##` sections: 14.
- Cited claims in the whole unit: 139. Counting rule: one for each sentence, list item, table row or figure that rests a number, date, quotation, attribution or mechanism on an outside cited source, including a derivation or a rule that names the source it rests on; pointers to other units, "her rule" and "derived" lines with no outside source, and the reference lines of the Sources list are not counted. A script (`out/count.py`) listed 151 candidate lines; the tally below is that list read line by line, with fragments of one sentence merged, unmarked sentences that carry a source's figures added, and the 38 reference lines removed.
- Per section: §1 7; §2 26; §3 16; §4 7; §5 15; §6 6; §7 8; §8 12; §9 3; §10 3; Deliverable 21; Templates 5; Sources 0; Unsure list 10. Total 139.

## Figures

| Figure | Verdict | Note |
|---|---|---|
| §2 compare, good audio minus echoing audio | PASS | 0.93, 0.69, 0.51, 0.33, 97 listeners, 0.60, 2–3 minute talks and the reference are all in §2's Experiment 1 bullet, and all match the paper. |
| §3 matrix, how each platform measures the opening | PASS | Every cell (Intro, 30 s, 50%+ above typical; 40–55% at 5–15 min, vidIQ, no sample; Stayed to watch, initial seconds, none; skip rate, 3 s, 65.5% at 1–5K, Socialinsider) and every date in the caption is in §3's text. |
| §4 flow, the eight chapters | PASS | Labels, start times and lengths match the runtime map row for row; the caption's three YouTube rules are in §4. |
| Deliverable B2 compare, minutes per box | PASS | The nine values match table B2 and sum to 220; 240, 300 to 600 and 17 Sep 2026 are in §9. |

No figure needs a fix.

## Arithmetic and Mara's facts

- Recomputed and correct: 607.5 px, 32%, 1.78 times, 1,215 × 2,160; 12.0 dB and 6 dB; 7 errors in 38 words against 1 in 20; the runtime map (10:00, start times); the nine boxes (220 minutes, the clock column, 22 minutes per finished minute); 300 to 600 minutes; the Reel's 45 seconds and both 30-minute box sets; packaging 60 minutes; R1 4.25 h and R2 1.5 h; 0:40 from each of chapters 3, 4 and 6; the seven contrast ratios.
- Weekdays: 12, 19 and 26 December 2026 are Saturdays; 27 December and 3 January 2027 Sundays; 5 January a Tuesday; 14 January a Thursday.
- `case-facts.md`: every PB5 fact in the unit agrees with the register (phone 3840 × 2160 at 30 fps, the set, the audio check's counts and dates, the storage test, 0.75 h of tests, the colours, four words, no Test & Compare, the eight chapters, the sanded corner, the 27 December edit, Reel 1 at 45 seconds, post 5 on Thu 14 Jan 2027, the season line, the three-overrun rule, the clamp only). Mara is labelled "(Mara, fictional)" on first use and is never used as evidence.
- Pointers to other units, all found in `others/`: PB1 §1 labels, D2 (150 USD cap, the conditional microphone, the tripod-or-clamp line), D3, row Y3 (vidIQ 40–55%); PB2 D1 ("tools that fit in one box"), D3 (the profile link), D4 (the promise sentence, word for word); PB3 D2 (24.0 of 24, about 8 minutes, no Shorts hours, PB6 may revisit); PB4 §1 (capture table, nothing filmed twice, two or three repositionings, three prompts, originality), §2 (the 10-minutes-in-4-hours question), §3 (30 minutes a post, post 5 a carousel), §4 (the season line, left to PB5), §5, §6 (piece 1), §7 (six posts to two), D1 C, D, G, D2 (R1–R4 dates and hours). The later units' pointers back to PB5 (PB6 §7 and R2; PB7 IR3, IR12; PB8 C1; PB9 D2; PB10's use of PB5 §9) agree with it, with one exception, flag PB5-5.

## Deliverable

- It exists in full inside the unit: checklist A (pre, during, post), the timed edit B1–B3 for a ten-minute video, the Reel template C, the carousel template D, each worked on piece 1, then the blank templates T-A to T-D with each blank saying what goes in it.
- It follows from the unit's evidence: every line names a section, a source or "her rule"; nothing in it rests on an unsourced claim, and the unsourced items (the caption-error pass mark, every minute) are labelled conventions or estimates.
- Usable without the unit: yes, with three small repairs. B1 points to §4 for the eight chapters that B2 then works through (PB5-4); box 9 says "B's settings" where the settings sit in A (PB5-2); D's slide order differs from the order §6 states (PB5-3).

## Course goal and sourcing standard

- Course goal: the unit serves the second outcome (a publishing system run inside an hours budget) by fitting a 10-minute edit, a Reel and a carousel into PB4's windows, and it hands PB6 the packaging rules and PB7 the format templates, as the brief's Gives line asks.
- Advice without evidence: none found. Each recommendation is either tied to a platform page or vendor figure where it is made, or labelled "her rule", "convention", "inference" or "derived", and the unit says where no source exists (the bad-audio comparison, hook formulas, slide order, editing time per stage).
- Labels and platforms: vendor, correlational, manufacturer, charity and press-report sources are labelled; each growth or metric claim names its platform. No legal point is made, so the information-not-advice line is not needed here.
- Sources list: 38 lines, each cited in the body, and every linked URL in the body is listed. One title is wrong (PB5-1). The Edits link now redirects to edits.instagram.com.

## Verdict

**PASS.** 0 of 14 sampled claims failed; no full audit was run. Outside the sample: one minor miscited title, three minor repairs to the deliverable and §6, and one cross-unit flag. 21 of the 38 pages in the unit's Sources list were not opened in this run (20 because the search budget ran out, 1 a redirect); none of the 17 that were opened contradicts the unit.

## Most consequential errors

1. PB10's Q2 verdict changes Mara's thumbnail to the layout PB5 already gives her from piece 1 (fault and finished piece side by side), and cites PB5 §7 for it. PB5 is not wrong; the two units cannot both stand (flag PB5-5).
2. The deliverable's edit template points back to §4 for its chapters and to "B's settings" for export settings that are in A, so a reader holding only the deliverable is missing both (PB5-4, PB5-2).
3. The Sources list quotes a Social Media Today headline the article does not carry (PB5-1). No figure, date or rule in the unit is affected.

## Bibliography line

New sources to add: none. Sources to mark failed: none. To correct: the Social Media Today 24 Aug 2025 entry's title ("Instagram Adds Retention Metrics for Reels", Andrew Hutchinson); to note: the Edits post at creators.instagram.com now redirects to edits.instagram.com/blog/edits-video-creation-app/ (target not opened), and NTIA TM-10-472's sixth author is "Hanes" on the title page and "Haines" on the report's data sheet and the ITS publication page.

## Changelog line

2026-11-14 · PB5 · Audit 2 stratified sample (claude-fable-5-2, search on) · PASS: 14 sampled, 0 FAIL, 1 unverifiable (redirect); 34 claims checked in all, 1 minor FAIL (a Sources title); 4 minor errata (PB5-1 to PB5-4) and 1 flag against PB10 (PB5-5); four figures PASS; 21 source pages not opened (search budget used up).

## Errata

**PB5-1** · erratum · minor · Sources
- Current: `- Social Media Today, "Instagram adds retention insights for Reels", 24 Aug 2025.`
- Fix: `- Social Media Today (Andrew Hutchinson), "Instagram Adds Retention Metrics for Reels", 24 Aug 2025.`
- Basis: The article's headline (H1 and title tag) is "Instagram Adds Retention Metrics for Reels"; the unit put the URL slug in quotation marks. Opened 14 Nov 2026: https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/

**PB5-2** · erratum · minor · Deliverable B2, box 9
- Current: `Export at B's settings; upload as private;`
- Fix: `Export at checklist A's edit-window settings (the recorded frame rate, AAC-LC stereo, 48 kHz, 384 kbps); upload as private;`
- Basis: Template B states no export settings; they are in checklist A, 'Post: edit window' (unit.md, Deliverable A), from YouTube Help answer 1722171, https://support.google.com/youtube/answer/1722171?hl=en (that page was not re-opened in this run; the settings are copied from the unit's own line).

**PB5-3** · erratum · minor · §6 Carousels, The order
- Current: `then one slide per step; then what went wrong; then the finished piece;`
- Fix: `then one slide per step, with what went wrong placed where it happened; then the finished piece;`
- Basis: Deliverable D puts 'What went wrong' on slide 5, between step 2 (slide 4) and step 3 (slide 6), as the runtime map does in §4 (chapter 5 before chapter 6); §6 says it comes after every step. Internal consistency; no outside source.

**PB5-4** · erratum · minor · Deliverable B1
- Current: `**B1 · The runtime map.** As in §4: eight chapters, 00:00 to 10:00, with the season line as a lower third inside chapter 1 and the end screen over 09:40–10:00.`
- Fix: `**B1 · The runtime map.** Eight chapters, 00:00 to 10:00, as in §4: The table 00:00 (0:30) · What was wrong 00:30 (1:00) · Lifting the rings 01:30 (2:00) · The edges 03:30 (2:00) · What went wrong 05:30 (1:30) · The finish 07:00 (2:00) · What it cost 09:00 (0:40) · Last line 09:40 (0:20); the season line is a lower third inside chapter 1 and the end screen runs over 09:40–10:00.`
- Basis: Method §6 step 4: the deliverable must be usable without reading the unit; B2 refers to 'the eight chapters' and '§4's times', which the deliverable does not hold. The times are copied from §4's runtime map (unit.md); no outside source.

**PB5-5** · flag · should-fix · §7 Mara's packaging rules, rule 1 (against PB10 D4 and the register)
- Current: `1. *The thumbnail image is a frame from the footage*, usually the as-found and finished views from the taped mark side by side.`
- Fix: No change in PB5. PB10's Q2 verdict ('from upload 15 … the thumbnail shows the fault and the finished piece side by side, at most four words, in her colours (PB5 §7), in place of the finished piece alone') and the register line that repeats it describe as a change the layout PB5 §7 rule 1 and Deliverable A already set from piece 1. Either PB10 names a different packaging change, or PB10 says Mara's thumbnails had drifted to the finished piece alone.
- Basis: others/PB10-read-your-numbers-the-quarterly-review.md line 475; case-facts.md, 'Set by PB10', Verdicts line; unit.md §7 rule 1 and Deliverable A (piece 1 thumbnail 'the as-found and finished views from the taped mark side by side'). No URL: a cross-unit contradiction.

Each Current was counted with `grep -c -F` against `unit.md` and occurs exactly once.

---

<!-- PB6: f-pb/PB6/audit.md, verbatim -->

Model: claude-fable-5-2

# Stratified-sample audit · PB6 · How YouTube growth works · 14 November 2026 · search on

**Verdict: PASS.** 13 claims sampled, one per `##` section plus the two parts of the deliverable; 0 FAIL, so no full audit was run. 54 claims checked in all: 50 PASS, 2 FAIL (both minor, both outside the sample), 0 STALE, 2 unverifiable (one YouTube Help page could not be opened). Two minor errata and two flags follow.

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2, 14 Nov 2026. Read only `/home/claude/fpb/PB6`; wrote only `out/`. `out/` was empty at the start, so nothing was resumed.
- Unit: `unit.md` (PB6, written 2026-11-12 by Opus 5.5, search on). Not edited.
- The sample below was written to this file before any source was opened.
- Web rule followed: WebSearch first; WebFetch only on a URL a search in this agent returned verbatim. 34 searches, 43 fetches. Pages were read through the fetch tool, which returns extracts; where it cut a long sentence short, the note says so.
- The earlier fresh check (`fresh-check-PB6.md`) was read to avoid re-reporting; none of its verdicts was reused. Erratum PB6-1 reverses its item 19, on the page's own bucket labels.

## Sample (recorded before checking; one claim per `##` section)

| # | Section | Sampled claim | Source cited |
|---|---|---|---|
| S1 | §1 | Recommendations page: "over 80 billion pieces of information"; surveys help understand "satisfaction, not just watch time" | https://support.google.com/youtube/answer/16089387?hl=en |
| S2 | §2 | Metricool: 799,718 videos, 71,177 accounts, 2025 against 2026; Shorts feed more than 61%, subscribers 11%, search 9%, related 5.77%, playlists 5.05%, channel pages about 3%; browse not reported | https://metricool.com/youtube-trends/ |
| S3 | §3 | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." | https://support.google.com/youtube/answer/7628154?hl=en-GB |
| S4 | §4 | vidIQ first-week views: 38,229,639 long-form videos, 15 Aug to 5 Sep 2026; median 234; 37.7% under 100; 70.1% under 1,000; top 1% took 54.1%, next 9% 34.6%, next 40% 10.8%, bottom 50% 0.5%; published 16 Sep 2026 | https://vidiq.com/research/youtube-first-week-views/ |
| S5 | §5 | AIR: 18,000 English-language channels, 40+ videos and 10+ long-form, Mar 2025 to Mar 2026; Home and DIY "near-identical", 95,100 v 94,600 and 251,500 v 256,000 | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels |
| S6 | §6 | vidIQ: 32,926,088 channels under 1,000 subscribers, 360 days; 0.20% / 1.86% / 8.65% / 30.77% crossed 1,000 by videos added; "observational association"; formats not separated | https://vidiq.com/research/youtube-uploads-1000-subscribers/ |
| S7 | §7 | Search: relevance ("how well the title, tags, description, and video content match your search query"), engagement (watch time per query), quality (expertise, authoritativeness, trustworthiness); importance "may vary by search type"; no payment for placement; no channel size or upload date on the page | https://support.google.com/youtube/answer/16090438?hl=en |
| S8 | §8 | 10 Aug 2026 blog post: from 1 Feb 2027 new applicants need 8,000 qualified watch hours in 365 days or 20M qualified Shorts views in 90 days; Shorts revenue sharing only at 10M qualified Shorts views in 90 days; (with 1,000 subscribers; terms accepted by 31 Jan 2027) | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ |
| S9 | §9 | "Publish time is not known to impact a video's long-term performance"; publishing when the audience is active "can be beneficial for early viewership" | https://support.google.com/youtube/answer/141805?hl=en |
| S10 | Deliverable D1 R4 | "consistent and similar in topic or format"; "a series of videos from topics that have already proven popular" | https://support.google.com/youtube/answer/13615784?hl=en |
| S11 | Deliverable D2 YT9 | +0.5 a month at 1–99 subscribers, +1.4 at 100–499, +3.7 at 500–999; 3,332,098 channels; 90 days to 20 Jul 2026 | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ |
| S12 | Sources | TechCrunch (Amanda Silberling), "YouTube adds new creator tools like video A/B testing, dynamic thumbnails, and live dubbing", 23 Sep 2026; and the §8 row it supports | https://techcrunch.com/2026/09/23/youtube-adds-new-creator-tools-like-video-a-b-testing-dynamic-thumbnails-and-live-dubbing/ |
| S13 | Unsure list | vidIQ first-week study states no channel count; livestreams not filtered out | https://vidiq.com/research/youtube-first-week-views/ |

The twelve `##` sections are §1 to §9, Deliverable, Sources and Unsure list. The deliverable gave two sampled claims (D1 and D2). The templates carry no checkable claim of their own beyond the D1 and D2 rows; they are covered under "Deliverable".

## Table: sampled claims

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | Recommendations page: "over 80 billion pieces of information"; surveys help understand "satisfaction, not just watch time" | https://support.google.com/youtube/answer/16089387?hl=en | PASS | Both strings are on the page as quoted. The page names no clicks, upload time or new-channel treatment, as the unit says. |
| S2 | §2 | Metricool: 799,718 videos, 71,177 accounts, 2025 against 2026; Shorts feed more than 61%, subscribers 11%, search 9%, related 5.77%, playlists 5.05%, channel pages about 3%; browse not reported | https://metricool.com/youtube-trends/ | PASS | Every figure, the sample, the author (Gretchen Oestreicher) and both dates (29 Jul, modified 4 Aug 2026) confirmed. |
| S3 | §3 | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | Verbatim. |
| S4 | §4 | vidIQ first-week views: 38,229,639 long-form videos, 15 Aug to 5 Sep 2026; median 234; 37.7% under 100; 70.1% under 1,000; top 1% took 54.1%, next 9% 34.6%, next 40% 10.8%, bottom 50% 0.5%; published 16 Sep 2026 | https://vidiq.com/research/youtube-first-week-views/ | PASS | All figures and the three caveat phrases confirmed. |
| S5 | §5 | AIR: 18,000 English-language channels, 40+ videos and 10+ long-form, Mar 2025 to Mar 2026; Home and DIY "near-identical", 95,100 v 94,600 and 251,500 v 256,000 | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels | PASS | Confirmed, with both caveat sentences. The page meta description says "the full 2025 calendar year"; the body says March 2025 through March 2026, which the unit follows. |
| S6 | §6 | vidIQ: 32,926,088 channels under 1,000 subscribers, 360 days; 0.20% / 1.86% / 8.65% / 30.77% crossed 1,000 by videos added; "observational association"; formats not separated | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | All confirmed; published 11 Sep 2026. |
| S7 | §7 | Search: relevance ("how well the title, tags, description, and video content match your search query"), engagement (watch time per query), quality (expertise, authoritativeness, trustworthiness); importance "may vary by search type"; no payment for placement; no channel size or upload date on the page | https://support.google.com/youtube/answer/16090438?hl=en | PASS | Confirmed; two of the quoted sentences were returned truncated but matched as far as shown. |
| S8 | §8 | 10 Aug 2026 blog post: from 1 Feb 2027 new applicants need 8,000 qualified watch hours in 365 days or 20M qualified Shorts views in 90 days; Shorts revenue sharing only at 10M qualified Shorts views in 90 days; (with 1,000 subscribers; terms accepted by 31 Jan 2027) | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | PASS | Blog confirms title, byline (The YouTube Team), date, 8,000/365, 20M/90, 10M/90 and 1 Feb 2027. The 1,000-subscriber condition and the 31 Jan 2027 deadline were not found in the blog as read; they rest on answer 12843009, which was not opened (see Not checked). Answer 72851 (en-GB) carries both "1,000 subscribers" and "review and accept the updated terms in YouTube Studio by 31 January 2027", so the row holds. |
| S9 | §9 | "Publish time is not known to impact a video's long-term performance"; publishing when the audience is active "can be beneficial for early viewership" | https://support.google.com/youtube/answer/141805?hl=en | PASS | Both verbatim. |
| S10 | Deliverable D1 R4 | "consistent and similar in topic or format"; "a series of videos from topics that have already proven popular" | https://support.google.com/youtube/answer/13615784?hl=en | PASS | Both strings are on the page. |
| S11 | Deliverable D2 YT9 | +0.5 a month at 1–99 subscribers, +1.4 at 100–499, +3.7 at 500–999; 3,332,098 channels; 90 days to 20 Jul 2026 | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | Medians confirmed. 3,332,098 is the sum of the three bands (1,047,481 + 1,430,714 + 853,903), not a figure the page prints; PB1 row Y6 uses the same sum. |
| S12 | Sources | TechCrunch (Amanda Silberling), "YouTube adds new creator tools like video A/B testing, dynamic thumbnails, and live dubbing", 23 Sep 2026; and the §8 row it supports | https://techcrunch.com/2026/09/23/youtube-adds-new-creator-tools-like-video-a-b-testing-dynamic-thumbnails-and-live-dubbing/ | PASS | Author, title, date, Ask Studio, Dynamic Thumbnails, "three different cuts for Shorts" from 2027 and the absence of dates or eligibility all confirmed. |
| S13 | Unsure list | vidIQ first-week study states no channel count; livestreams not filtered out | https://vidiq.com/research/youtube-first-week-views/ | PASS | Page: "Livestreams were not separately filtered out"; no channel count. |

## Also checked (beyond the sample, counted in the totals)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 14 | §1 | Help page: where recommendations appear, the signal list, Up Next main signal, Home relies primarily on watch history | https://support.google.com/youtube/answer/16089387?hl=en | PASS |  |
| 15 | §1 | Goodrow, VP of engineering, 15 Sep 2021: six quoted strings | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | PASS | All six verbatim. |
| 16 | §1 | Creator page: "What matters is how viewers respond…", "does not penalize a channel overall", "consistently stops watching", monetised videos not prioritised, unlisted-first quote | https://support.google.com/youtube/answer/16559651?hl=en | PASS |  |
| 17 | §1 | Beaupré, SEJ 4 Mar 2024: four quotations | https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/ | PASS | First fetch refused by permission; retried once and read. All four verbatim. |
| 18 | §1 | Beaupré via PPC Land, 2 Sep 2026: interview published 1 Sep 2026; "Each viewer gets a different ranking"; "videos are reaching people who've never watched the channel before"; topic-match and impressions-stop are paraphrases | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS | Quotes are inside quotation marks attributed to him; the paraphrases are labelled as PPC Land's in the unit. |
| 19 | §2 | Traffic source definitions (six table rows) | https://support.google.com/youtube/answer/1714921?hl=en-GB | PASS | All quoted definitions verbatim; the page labels the last two "External sources" and "Direct or unknown sources". |
| 20 | §2 | FAQ: "You released a new video in a series…"; "Viewers, on average, are subscribed to dozens of channels…" | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 21 | §2 | Beaupré on subscribers: "10% or less click-through rate", "even your best videos, 90% of the time…", "The number one place…"; subscriptions feed small in paraphrase | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS | The "even your best videos" sentence stands in quotation marks in the article without its own speaker tag, directly after the attributed 10% quote. |
| 22 | §2 | Android Studio app path (Content, video, Analytics card, Reach); "Thumbnail impressions" naming; search terms report | https://support.google.com/youtube/answer/9314355?hl=en | PASS |  |
| 23 | §3 | CTR definition; external sites and end screens not counted; the other six FAQ bullets | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | Two sentences were returned truncated and matched as far as shown. |
| 24 | §3 | Focus Digital: "4–6%", January to June 2026, sources named, no sample size; 11 Sep 2026 | https://focus-digital.co/average-youtube-ctr-organic-paid-benchmarks-2026/ | PASS | Page metadata shows it was modified on 5 Nov 2026; the byline date is 11 Sep 2026. |
| 25 | §3 | Retention report: Intro, spikes, dips, 60 seconds and 100 views, "all YouTube videos of similar length" | https://support.google.com/youtube/answer/9314415?hl=en | PASS |  |
| 26 | §3 | Typical retention ("the last 10 of your videos of a similar length"); "A typical intro is about 30 seconds long"; 50% and the "above typical intros" list | https://support.google.com/youtube/answer/12942217?hl=en | PASS |  |
| 27 | §3 | vidIQ: "5 to 15 minutes: aim for 40 to 55% viewed"; "vidIQ guidance for target bands"; own channel 30.3% across 16.5M views, 26 Jun 2025 to 25 Jun 2026; updated 21 Jul 2026 | https://vidiq.com/blog/post/average-view-duration/ | PASS |  |
| 28 | §3 | Test & Compare: up to 3, computers only, advanced features, no Shorts, "Not enough impressions", "Inconclusive", default-title sentence, watch time over CTR | https://support.google.com/youtube/answer/16391400?hl=en | PASS |  |
| 29 | §3 | Packaging changes: "can lead to a shift in its performance…", "recommended when a video has a lower click-through rate (CTR)…", "not to change what is already working well" | https://support.google.com/youtube/answer/16559651?hl=en | PASS | The second sentence was returned truncated after "(CTR)"; the "fewer impressions than usual" half was not re-read in this run. |
| 30 | §4 | Four FAQ quotes on old videos and "regardless of when that video was uploaded" | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 31 | §4 | "Qualified watch hours gained from long-form videos that you've set to public"; private, unlisted, deleted and Shorts do not count | https://support.google.com/youtube/answer/72851?hl=en-GB | PASS | The page also excludes ad campaigns. |
| 32 | §4 | Answer 12843009: "8,000 qualified watch hours in the last 365 days, or 20M qualified Shorts views in the last 90 days", with 1,000 subscribers | https://support.google.com/youtube/answer/12843009 | unverifiable | Page not opened: no search in this run returned its URL. The figures themselves are confirmed by the 10 Aug 2026 blog post. |
| 33 | §4 | Metricool: peak in first three days; about 83% of interactions within ten days; "keeps earning views for months" | https://metricool.com/youtube-trends/ | PASS |  |
| 34 | §5 | Formats "will not inherently confuse the algorithm"; long-form viewers may see Shorts; "Any perceived effect…" | https://support.google.com/youtube/answer/16559651?hl=en | PASS |  |
| 35 | §5 | Related video on a Short; "only available with advanced feature access"; blog guide 14 Jul 2026, "billions of daily views", no conversion figure | https://support.google.com/youtube/answer/14075157?hl=en; https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/ | PASS |  |
| 36 | §5 | Metricool: 8,789 at about five Shorts a month, 5,985 global, 4,364 with none; 35+ falls back; "Correlation isn't causation here…" | https://metricool.com/youtube-trends/ | PASS |  |
| 37 | §5 | vidIQ first ten: Shorts 1,362 and 1,344; long-form 180 and 272; three caveat quotes; "no incremental growth, in fact a slight decline over time" | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | Best-of-ten 1,948 (D2 YT2) also confirmed. |
| 38 | §5 | OverseerOS: 370 videos, 37 channels, 1.021, 19 of 37, subset of 16 at 0.754, "found no consistent evidence…", 1 Sep 2026, no subscriber finding | https://www.overseeros.com/blog/do-youtube-shorts-hurt-long-form-views | PASS |  |
| 39 | §5 | OverseerOS: 9,982 Shorts at least 30 days old, about eight days; "Among 1,546 Shorts starting below 1,000 views, none gained another 1,000 views during that interval"; "selected, not random"; 8 Nov 2026 | https://www.overseeros.com/blog/do-youtube-shorts-get-views-after-30-days | PASS | The quoted sentence is in the page's opening summary; median interval 7.9 days. |
| 40 | §5 | AIR states "0.04% to 0.5% Shorts-to-long-form conversion" with no definition, method, source or sample | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels | PASS |  |
| 41 | §6 | Break and cadence quotes; PPC Land reports a German-language FAQ in the YouTube Help community on 2 Sep 2026 with two Help Center pages | https://support.google.com/youtube/answer/141805?hl=en; https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/ | PASS | The English page shows no date, as the unit says. |
| 42 | §6 | "To grow regular viewers, publish content regularly and maintain a strong connection with your audience" | https://support.google.com/youtube/answer/13615784?hl=en | PASS |  |
| 43 | §6 | AIR cadence: 18,000 channels, US/UK/Canada/Australia, 100K–1M tier; Home and DIY 83,050 (116), 114,000 (178), 105,000 (130), 90,700 (87); 14+ day gaps; predictable schedule; "correlational data, not causal"; no effect size for the gap finding | https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | Author Mariia Loboda, 8 Jun 2026. |
| 44 | §6 | Metricool: 2 to 4 long-form posts a week best per post, about 10,552 views; under once a week weakest monthly result | https://metricool.com/youtube-trends/ | PASS |  |
| 45 | §7 | Tags "play a minimal role in your video's discovery"; useful where "commonly misspelled"; title, thumbnail, description matter more | https://support.google.com/youtube/answer/146402?hl=en | PASS |  |
| 46 | §7 | AIR titles: 18,080 channels, 100K–100M monthly views, 11 niches; engagement definition; "the universal sweet spot" at 30 to 50; keyword in first 40%; Home and DIY finished-project finding; caveats; period not stated; titles not separated from thumbnails | https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches | PASS | Page H1 matches the Sources entry; author Nataliia Prokopchuk, 12 Jun 2026. |
| 47 | §8 | 4 Dec 2025: title testing in Test & Compare, global, up to three titles, thumbnails or pairs, long-form, desktop, watch time | https://www.searchenginejournal.com/youtube-title-a-b-testing-rolls-out-globally-to-creators/562571/ | PASS |  |
| 48 | §8 | Shift in Shorts ranking from mid-Sep 2025; YouTube "hasn't confirmed any algorithm change"; SEJ 5 Dec 2025 | https://www.searchenginejournal.com/youtube-shorts-algorithm-may-now-favor-fresh-over-evergreen/562661/ | PASS |  |
| 49 | §8 | "Videos that are made with AI can be recommended as broadly as videos made without AI" | https://support.google.com/youtube/answer/16089387?hl=en | PASS |  |
| 50 | §9 | Item 6: Mario Joos, on X, 30 Nov 2025, "satisfied watch time per click", reported by PPC Land 2 Dec 2025; YouTube gave no explanation | https://ppc.land/youtube-creators-report-drops-in-shorts-viewership-after-september-algorithm-change/ | PASS | PPC Land dates his disclosure 30 Nov 2025; the X post it embeds is stamped 29 Nov 2025. The unit follows PPC Land's date. His full phrase is "expected satisfied watch time per click from impressions". |
| 51 | §9 / D2 YT11 | "Audience segments do not affect reach or monetization"; regular = at least once a month for more than 6 months in the past year | https://support.google.com/youtube/answer/10246996?hl=en | PASS | Answer 13615784 words the same definition as "at least six months"; the unit cites 10246996, which says "more than 6 months". |
| 52 | D2 YT10 | "3,000 for fan funding (answers 12843009, 72851)" | https://support.google.com/youtube/answer/12843009; https://support.google.com/youtube/answer/72851?hl=en-GB | unverifiable | 12843009 was not opened. The en-GB page 72851, as read, gave no fan-funding threshold (it links to a video on earlier access). The 10 Aug 2026 blog says fan-funding thresholds are unchanged but prints no number. The 3,000 could not be confirmed at either cited page. |
| 53 | D2 YT11 / T2 YT11 | Metric named "Returning, casual and regular viewers" | https://support.google.com/youtube/answer/10246996?hl=en | FAIL | The cited page names three segments: "New viewers", "Casual viewers", "Regular viewers". "Returning" is not one of them (casual and regular viewers together are the returning ones). PB10 repeats the label, so it is reported as a flag. |
| 54 | §7 | AIR: "titles of over 90 characters underperforming on views" | https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches | FAIL | The page's bucket is "90+" ("90+ character titles consistently underperform on views"); it does not say "over 90". A one-character boundary; minor. |

## Not checked

- https://support.google.com/youtube/answer/12843009: not checked, no WebSearch in this run returned this URL, so it could not be fetched under the web rule
- WebSearch: the turn's search budget ran out after 34 searches; one further search (fan-funding threshold) was refused and not retried by other means
- https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/: first fetch refused by permission; retried once and read (checked)
- Not opened, and nothing rests on them here: the iPhone version of the reach page (the unit says it was not read); YouTube's Creator Insider videos behind the press reports; the German-language community FAQ.
- A second YouTube blog URL for the Partner Programme post appeared in search results (`blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/`); it was not opened. The URL the unit cites opened and carries the post.

## Failure rate

- Sample: 0 FAIL of 13 (0%). The rule (more than one in ten) is not met; no full audit.
- All claims checked: 2 FAIL of 54 (3.7%), both minor; 0 STALE; 2 unverifiable.
- Nothing checked had been superseded between 12 and 14 Nov 2026. Answer 72851 still shows the 4,000-hour line as current, with the 1 Feb 2027 change announced, which agrees with the unit.

## Counts

- Words: 10,515 (`wc -w unit.md`). `##` sections: 12.
- Cited claims in the whole unit: 144, counted by `out/count.py`. Rule: outside `viz` blocks, Sources and the Unsure list, each prose sentence, bullet or table row counts once if it names an outside source (a link, a Help answer number, or a named vendor, publication or speaker) or carries a number or quotation inside a paragraph or list that does; rows and sentences resting only on other units of the course or on Mara's invented facts are not counted; blank template rows are not counted.
- Per section: §1 9 · §2 13 · §3 26 · §4 10 · §5 17 · §6 10 · §7 12 · §8 9 · §9 12 · Deliverable 26 · Sources 0 · Unsure list 0.

## Figures

| Figure | Checked against | Result |
|---|---|---|
| §2 compare, share of organic views by source | §2 text: 61, 11, 9, 5.77, 5.05, 3; 799,718 videos; 71,177 accounts; 29 Jul and 4 Aug 2026 | PASS |
| §3 decision, reading one upload's click-through rate | §3 FAQ bullets (a week old, 100 views, clickbait signature, lower CTR at high impressions, compare over the long term); caption's exception for rule R2 | PASS |
| §4 compare, share of first-week views by band | §4 text: 54.1, 34.6, 10.8, 0.5; 38,229,639 videos; 15 Aug to 5 Sep 2026; median 234; 16 Sep 2026 | PASS |
| §5 matrix, Shorts and a long-form channel | §5 text for all seven rows; caption dates 29 Jul, 28 Jul, 28 May and 1 Sep 2026 | PASS |

No figure adds a fact, and each caption says what it shows and where its data comes from. No FIX.

## Deliverable

- **Exists in full.** D1 has eleven rules, each with evidence, a grade and a label, and the grades are defined. D2 has twelve rows with all six asked-for columns, worked for the Q1 review on Monday 5 April 2027. T1 and T2 follow, and every blank says what goes in it.
- **Follows from the evidence.** Each rule's evidence cell repeats a claim checked above. Conventions are marked as conventions (R6's selection rule, R7's date, R8's hours decision). R4 quotes answer 13615784 for two strings the body does not use; both are on the page (S10).
- **Dates and arithmetic hold.** 5 Jan 2027 is a Tuesday; 5 Apr and 5 Jul 2027 are Mondays. On 5 Apr, uploads 1 to 5 are 34 days old or more, upload 6 is 20 days old and upload 7 is 6 days old, as YT2 and YT3 say. Mara's first title is 82 characters and "teak" starts at character 13.
- **Usable without the unit, with two limits.** Evidence cells cite Help pages by answer number and vendors by short name, so a reader needs the Sources list to open them. R10 gives only the half of YouTube's sentence that supports it (erratum PB6-2).
- **Two cells could not be confirmed.** YT10's "3,000 for fan funding" was not found at 72851 as read, and 12843009 was not opened. YT11's metric name does not match the cited page (flags PB6-3 and PB6-4).

## Mara's facts and pointers to other units

- **Register:** every Mara fact in the unit agrees with `case-facts.md` (channel name, cadence, upload dates 5 Jan to 30 Mar 2027, review dates, phone only, no Shorts in year one, title and search rule, packaging check, rows YT1 to YT12, 24.0 hours per four weeks). "(Mara, fictional)" is on her first use. None of her numbers is used as evidence.
- **Pointers, all found:** PB1 rows Y1, Y2, Y3, Y4, Y6, Y10, Y11, §2, §4 and D3 (stop rule, verdict 3 as corrected, the Q1 note); PB3 §4 and D2; PB4 §2, §7 and D1 ("Never publish two videos in one week to catch up"); PB5 §3 and §7 (the title, the promise test, Test & Compare on computers only); PB10 (60-minute review, rows YT1 to YT12, R6, the Shorts test at the twelve-month review); DD-PB1 reads rules R3, R4, R7, R8, R10 and R11.
- **One cross-unit point:** PB10 carries the same "Returning, casual and regular viewers" label for YT11 (see flags).

## Course goal and sourcing standard

- **Goal.** The unit serves the third outcome directly: it gives the YouTube rows the quarterly review reads, each set against a sourced benchmark or marked as own-baseline only. The brief's ten topics are all covered.
- **Sourced where made.** Every number, mechanism and recommendation sampled had its source beside it. Vendor data is labelled vendor and correlational, survivor samples are named, executive statements via the press are labelled, and paraphrases are attributed to PPC Land. Sources lists exactly the 38 URLs linked in the body, no more and no fewer.
- **Advice without evidence.** None found. Rules with no source are marked "convention" and inferences are marked as inferences.
- **Platform and dates.** Every claim is about YouTube; facts that can change carry 12 Nov 2026 or their own date.
- **Private course.** No reference to it or to its reader was seen.
- **Process language (observation, no erratum).** The correction line after the templates and the last Unsure-list item carry internal codes ("P100", "flag F42", "P49"). PB1's correction lines do the same, so this looks like the course's convention for those lines.

## Verdict

**PB6: PASS.** No full audit was run (0 of 13 sampled claims failed). No section needs rewriting.

## Most consequential errors

None is consequential. In order of weight:

1. D2 row YT10 cites two pages for "3,000 for fan funding" and neither could be confirmed: one was not opened, and the other, as read, does not print the figure. This is unverifiable, not shown wrong; the next check should open answer 12843009.
2. The YT11 metric is called "Returning, casual and regular viewers"; YouTube's page calls the segments new, casual and regular. PB10 repeats the label.
3. §7 says AIR found titles of "over 90" characters underperform; AIR's bucket is "90+".

## Bibliography line

No new source to add and none to mark failed; note against YouTube Help answer 12843009 that it was not opened in this audit, and that vidIQ's 3,332,098 is a sum of three band counts.

## Changelog line

2026-11-14 · Audit 2, PB6 · claude-fable-5-2 · stratified sample 13 claims, 0 FAIL; 54 checked, 2 minor FAIL, 0 STALE, 2 unverifiable (answer 12843009 not opened); four figures PASS; verdict PASS; 2 minor errata, 2 flags (YT11 label, shared with PB10).

## Errata

**PB6-1** · erratum · severity minor · verdict FAIL · §7 · Titles and search for a small channel (What the title data says)
- Current: `titles of over 90 characters underperforming on views`
- Fix: `titles of 90 or more characters underperforming on views`
- Basis: AIR Media-Tech's length buckets are "under 30, 30–50, 50–70, 70–90, 90+ characters", and the finding reads "90+ character titles consistently underperform on views"; the page does not say "over 90". https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches

**PB6-2** · erratum · severity minor · verdict other · Deliverable · D1, rule R10
- Current: `| "Publish time is not known to impact a video's long-term performance" (answer 141805) | Strong |`
- Fix: `| "Publish time is not known to impact a video's long-term performance", although publishing when the audience is most active "can be beneficial for early viewership" (answer 141805) | Strong |`
- Basis: The same FAQ answer carries both halves, and §9 item 8 of the unit gives both; the deliverable row, which must stand without the unit, gives only the half that supports the rule. https://support.google.com/youtube/answer/141805?hl=en

**PB6-3** · flag · severity minor · verdict FAIL · Deliverable · D2, row YT11
- Current: `| YT11 | Returning, casual and regular viewers |`
- Fix: `| YT11 | New, casual and regular viewers |`
- Basis: The cited page names the three segments "New viewers", "Casual viewers" and "Regular viewers"; "returning" is not a segment name. Flag, not erratum: PB10 (D1, row YT11) uses the same label "Returning, casual and regular viewers", so the two units would have to change together. https://support.google.com/youtube/answer/10246996?hl=en

**PB6-4** · flag · severity minor · verdict FAIL · Deliverable · Templates, T2, row YT11
- Current: `| YT11 | Returning, casual, regular viewers |`
- Fix: `| YT11 | New, casual, regular viewers |`
- Basis: Same finding as PB6-3, second occurrence (the template row). https://support.google.com/youtube/answer/10246996?hl=en

Each Current was counted once in `unit.md` with `grep -c -F`.

---

<!-- PB7: f-pb/PB7/audit.md, verbatim -->

Model: claude-fable-5-2

# PB7 · How Instagram growth works · stratified-sample audit (course PB, Audit 2)

Date: 14 November 2026. Search: on. Auditor: one fresh, isolated agent; unit not edited.

## Provenance

- Read: `unit.md`, `brief.txt`, `sourcing-parts-1-and-5.md`, `case-facts.md`, `fresh-check-PB7.md` (to avoid re-reporting; none of its verdicts reused), `others/` (pointers only).
- Web rule followed: WebSearch first; WebFetch only on a URL a search in this agent returned verbatim.
- `out/` was empty at the start: no resumed run.

## Sample (recorded before any check)

One claim per `##` section (13 sections), with D1, D2 and Templates sampled separately inside Deliverable: 15 claims.

| n | Section | Sampled claim | Source cited |
|---|---|---|---|
| 1 | §1 | 30 Apr 2024: each eligible piece of content "is shown to a small audience that we think will enjoy it"; "the top performing set of reels are shown to a slightly wider audience"; "A new input to ranking that will give smaller creators more distribution" | Instagram Creators, Helping Creators Find New Audiences, 30 Apr 2024 |
| 2 | §2 | Fanpage Karma: more than 3 million posts, Jan–Apr 2026; under 10,000 followers median reach per post 4.9% (Reels), 3.5% (images), 2.6% (carousels) of followers; "Reels reach nearly three times as many non-followers as carousels" | Fanpage Karma, 7 Aug 2026 |
| 3 | §3 | Socialinsider: 67,541,436 organic posts, brand accounts 1,000 to 1 million followers; 1,000–5,000: carousels 993, Reels 580, images 417 views per post; engagement 0.55% / 0.52% / 0.37% | Socialinsider, 2026 Instagram Organic Benchmarks |
| 4 | §4 | Socialinsider skip rate: average 65.50% at 1,000–5,000 followers, 60.50% at 100,000–1 million, from 9,771,822 organic Reels, Jan–Jun 2026 | Socialinsider, Instagram Reels statistics, 24 Jun 2026 |
| 5 | §5 | 30 Apr 2026: protections extended from Reels to photos and carousels; "will no longer be shown in places where we recommend content"; 75% of recommendations in the US come from original posts | Instagram Creators, Rewarding original creators on Instagram, 30 Apr 2026 |
| 6 | §6 | Reposts: go to the reposter's friends' and followers' feeds, "credited to the original poster", and a reposts tab on the profile; 6 Aug 2025 | Meta, New Instagram features to help you connect, 6 Aug 2025 |
| 7 | §7 | 18 Dec 2025: Instagram "will gradually update the number of hashtags that you can include in a caption for a reel or post to five"; Mosseri: hashtags "don't improve visibility on Instagram" | Social Media Today, 18 Dec 2025 |
| 8 | §8 | Buffer: about 2.1 million feed posts, 102,000 accounts; weekly follower growth +0.12% / 0.26% / 0.44% / 0.66%; reach per post +12% / 18% / 24%; "likely the sweet spot" | Buffer, 13 Aug 2025 |
| 9 | §9 | YouTube: "External" is "Traffic from websites and apps that have your YouTube video embedded or that link to it"; "Direct or unknown sources" covers "direct URL entry, bookmarks, signed-out viewers and unidentified apps" | YouTube Help, answer 1714921 |
| 10 | §10 | Mosseri: "You're more than welcome to say 'link in bio,' it will not affect your reach one way or another" | Social Media Today, 23 Jul 2025 |
| 11 | Deliverable · D1 (IR8) | Trial reels shown to non-followers first; automatic sharing on views in 72 hours (10 Dec 2024); 1,000 followers and a public account (Mosseri via SMT, 13 Jul 2025) | Instagram Creators, 10 Dec 2024; Social Media Today, 13 Jul 2025 |
| 12 | Deliverable · D2 (IG3) | Median reach 261 accounts a post, all sizes pooled, from over 27 million posts of 273,000 accounts; page also gives 30 million posts from 250,000 accounts; updated 8 Nov 2026 | Buffer, Instagram benchmarks |
| 13 | Deliverable · Templates (T2 IG12) | Follower demographics read "from 100 followers" on "Meta's threshold" (body: "Not returned if the IG User has less than 100 followers") | Meta for Developers, Instagram account insights |
| 14 | Sources | Reference entry: Engadget, "Meta is testing clickable links in Instagram captions for verified subscribers", 12 Mar 2026 (title, date, and the claim it carries in §9) | Engadget, 12 Mar 2026 |
| 15 | Unsure list | Trial reels eligibility "rests on Social Media Today's paraphrase of a Mosseri Threads post, 13 Jul 2025" | Social Media Today, 13 Jul 2025 |

## Table (sampled claims)

| n | Section | Claim | Source opened | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §1 | 30 Apr 2024: small test audience; top performing set shown wider; new ranking input for smaller creators; no size, window or effect size | https://creators.instagram.com/recommendations-and-originality | PASS | All four quotations verbatim; dated 30 Apr 2024; page gives no audience size, window or effect size. |
| 2 | §2 | Fanpage Karma: >3 million posts, Jan–Apr 2026; under 10,000: 4.9% / 3.5% / 2.6% median reach; Reels nearly three times the non-follower reach of carousels | https://www.fanpagekarma.com/insights/instagram-format-reach/ | PASS | Published 7 Aug 2026, modified 28 Aug 2026; accounts not counted, as the unit says. |
| 3 | §3 | Socialinsider: 67,541,436 posts, brands 1K–1M; 1K–5K views 993 / 580 / 417; engagement 0.55% / 0.52% / 0.37% | https://socialinsider.io/social-media-benchmarks/instagram | PASS | Read at the address the search returned, not the unit's link (see Not checked). Published 20 Feb 2026, modified 4 Nov 2026; averages; quotation on carousels verbatim. |
| 4 | §4 | Socialinsider skip rate: 65.50% at 1–5K, 60.50% at 100K–1M; 9,771,822 Reels, Jan–Jun 2026 | https://socialinsider.io/blog/instagram-reels-statistics/ | PASS | Published 24 Jun 2026, updated 6 Nov 2026; averages; brands; no watch-time figure. The page's method note says accounts over 100K were excluded while its results report a 100K–1M band; the unit reports the figure as the page gives it. |
| 5 | §5 | 30 Apr 2026: protections extended to photos and carousels; 'will no longer be shown in places where we recommend content'; 75% of US recommendations from original posts | https://creators.instagram.com/blog/rewarding-original-creators-on-instagram | PASS | All verbatim; dated 30 Apr 2026. |
| 6 | §6 | Reposts go to friends' and followers' feeds, 'credited to the original poster', with a profile tab; 6 Aug 2025 | https://about.fb.com/news/2025/08/new-instagram-features-help-you-connect/ | PASS | Verbatim; 'it may be recommended to that person's followers, even if those people don't follow you'. |
| 7 | §7 | 18 Dec 2025: hashtag limit of five (Instagram, quoted); Mosseri: hashtags "don't improve visibility on Instagram" (in quotation marks) | https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/ | FAIL | The limit and both Instagram quotations hold (Threads post of @creators, quoted by SMT). The words "don't improve visibility on Instagram" are the reporter's paraphrase (link text, no quotation marks in the article, dated 'May this year'); the unit puts them in quotation marks as what Mosseri said. Errata PB7-1. |
| 8 | §8 | Buffer: 2.1 million feed posts, 102,000 accounts, fixed effects; +0.12/0.26/0.44/0.66% weekly growth; reach per post +12/18/24%; 'likely the sweet spot' | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | All figures and both phrases hold; baseline for reach per post is 1–2 posts a week, as the unit says; no split by size or format. |
| 9 | §9 | YouTube: definitions of External and of Direct or unknown sources | https://support.google.com/youtube/answer/1714921?hl=en-GB | PASS | Both verbatim; the External sites or apps card exists. |
| 10 | §10 | Mosseri: 'You're more than welcome to say 'link in bio,' it will not affect your reach one way or another' | https://www.socialmediatoday.com/news/instagram-doesnt-penalize-posts-that-include-link-in-bio/753899/ | PASS | Verbatim in SMT, 23 Jul 2025; title as the unit gives it. |
| 11 | Deliverable · D1 (IR8) | Trial reels: non-followers first; automatic sharing on 72-hour views; 1,000 followers and a public account | https://creators.instagram.com/blog/instagram-trial-reels ; https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/ | PASS | Instagram Creators, 10 Dec 2024, holds the mechanism ('all eligible creators', eligibility left to the Help Centre). SMT, 13 Jul 2025, paraphrases Mosseri: 'to all creators with at least 1,000 followers and an account set to "Public"'. Graded as the unit grades it. |
| 12 | Deliverable · D2 (IG3) | Buffer benchmarks: median reach 261 (All); 27 million posts / 273,000 accounts and 30 million / 250,000 both on the page; updated 8 Nov 2026 | https://buffer.com/social-media-benchmarks/instagram | PASS | All hold; tier filters are offered, tier figures not readable; the page recommends filtering by size. |
| 13 | Deliverable · Templates (T2 IG12) | Meta's threshold: follower demographics not returned under 100 followers | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | 'Not returned if the IG User has less than 100 followers.' on both rows (follows_and_unfollows, follower_demographics). |
| 14 | Sources | Engadget reference: title, 12 Mar 2026; Meta confirmed the caption-link test for Meta Verified; no word on wider availability | https://www.engadget.com/social-media/meta-is-testing-clickable-links-in-instagram-captions-for-verified-subscribers-184555406.html | PASS | Title and date exact. A search on 14 Nov 2026 returned no report of a wider rollout. |
| 15 | Unsure list | Trial reels eligibility rests on SMT's paraphrase of a Mosseri Threads post, 13 Jul 2025 | https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/ | PASS | Paraphrase and date hold. The Threads post SMT links sits on another account (oncescuradu) and was not opened, so 'a Mosseri Threads post' is not confirmed; minor wording erratum PB7-7. |

## Also checked (beyond the sample, while a source was open; counted in the totals)

| n | Section | Claim | Source opened | Verdict | Note |
|---|---|---|---|---|---|
| 16 | §5 | 30 Apr 2024: originals replace copies in recommendations, label to the original creator, repeat aggregators excluded | https://creators.instagram.com/recommendations-and-originality | PASS |  |
| 17 | §2 | Fanpage Karma: reach within the existing community 2.1% images, 2.0% Reels (under 10,000) | https://www.fanpagekarma.com/insights/instagram-format-reach/ | PASS |  |
| 18 | §3 | Fanpage Karma: interaction rate images 0.51%, Reels 0.34%; not stated as medians | https://www.fanpagekarma.com/insights/instagram-format-reach/ | PASS |  |
| 19 | D2 IG8 | Socialinsider: 22% yearly follower growth, brand accounts 1,000–5,000 | https://socialinsider.io/social-media-benchmarks/instagram | PASS | 22.00% in 2025, 38.00% in 2024. |
| 20 | §5 | 30 Apr 2026: 'does not impact how we show people content from accounts they follow'; collabs, remix, paid-partnership label, Stories, reposts | https://creators.instagram.com/blog/rewarding-original-creators-on-instagram | PASS |  |
| 21 | §6 | Reposts row, Who can use it: 'All accounts', cited to Meta, 6 Aug 2025 | https://about.fb.com/news/2025/08/new-instagram-features-help-you-connect/ | FAIL | The page states no eligibility; it says only that 'you can repost public reels and feed posts'. Unsupported cell; the unit's own text below the table says it more carefully. Erratum PB7-3. |
| 22 | §7 | Instagram: fewer, more targeted hashtags 'can improve both your content's performance and people's experience on Instagram' | https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/ | PASS | In the Threads post SMT embeds. |
| 23 | §10 item 1 | Mosseri said in 2025 that hashtags "don't improve visibility" | https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/ | FAIL | Same fault as claim 7: the reporter's paraphrase set in quotation marks as Mosseri's words. Erratum PB7-2. |
| 24 | §3 | Buffer left Stories out: 'Since stories are not typically shown to non-followers' | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS |  |
| 25 | §4 | Meta developer reference: definitions of views and reach; FOLLOWER and NON_FOLLOWER as a breakdown | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | Views definition continues 'Content includes reels, posts, stories.'; reach continues ', including in ads'. FOLLOWER / NON_FOLLOWER are values of the follow_type breakdown (reach; follows_and_unfollows). |
| 26 | §9 | profile_links_taps counts taps on contact buttons only | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | 'The number of taps on your business address, call button, email button and text button.' |
| 27 | §1, §4, D1 IR4 | Mosseri, Jan 2025: top three signals; likes for connected, sends for unconnected; average watch time, likes per reach, sends per reach; 'connected' undefined, SMT's reading | https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/ | PASS | Three quotations verbatim; dated 22 Jan 2025. |
| 28 | §3 | Metricool Trends 2026: 24,364,803 posts, 375,118 accounts; carousels' views about 1.69% above Reels'; Reels engagement +24.76%, shares +67.19% | https://metricool.com/instagram-trends/ | PASS | Published 16 Jun 2026, modified 9 Jul 2026. |
| 29 | §3 | Metricool 2026: Stories reach −1.77%, replies +88%; 65% / 76% of views in days 1–3; 44% of a single image's views on day 1 | https://metricool.com/instagram-trends/ | PASS |  |
| 30 | §8 | Metricool 2026: 2,000–10,000 best at 7–14 posts a week; 10,000–100,000 at 14–30; 100,000–1M better per post when posting less; no band under 2,000 | https://metricool.com/instagram-trends/ | PASS |  |
| 31 | §4 | Meta media insights: reels_skip_rate; ig_reels_avg_watch_time 'The average amount of time spent playing the reel'; no insights for media within an album; shares, saves, likes, comments, follows, profile visits defined there | https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights/ | PASS | reels_skip_rate: 'The percentage of views from people who skipped during the first 3 seconds of the reel.' |
| 32 | Sources | Reference title: Social Media Today, 'Instagram shares algorithm insights for 2025', 22 Jan 2025 | https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/ | FAIL | The article's headline is 'Instagram Shares Algorithm Insights To Inform Strategy'; the unit's title follows the URL slug. Date and URL right. Erratum PB7-5. |
| 33 | Sources | Reference title: Social Media Today, 'Instagram expands access to trial reels', 13 Jul 2025 | https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/ | FAIL | The article's headline is 'Instagram Trial Reels Are Now Available to More Creators'. Date and URL right. Erratum PB7-6. |
| 34 | Sources | Reference title: Social Media Today, 'Instagram implements new limits on hashtag use', 18 Dec 2025 | https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/ | PASS |  |
| 35 | Sources | Reference title: Buffer, 'How often should you post on Instagram', 13 Aug 2025 | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | Shortened from 'How Often Should You Post on Instagram in 2026? What Data From 2 Million Posts Tells Us'; date right. |
| 36 | D2 IG11 | Recommendation eligibility 'regained after 30 days of mostly original posts' | https://creators.instagram.com/blog/rewarding-original-creators-on-instagram | FAIL | A stretch: Instagram says eligibility returns when recent posts are 'considered original in a 30-day period', on a rolling basis, and the guidelines' words (quoted in the unit's §5) are 'a significant percentage', which §5 itself says is not defined. 'Mostly' and 'after 30 days' are the unit's. Erratum PB7-4. |
| 37 | §8 | Buffer: Stories excluded; each account compared with itself; reach-per-post gain measured against 1–2 posts a week | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS |  |

Staleness, two changeable facts searched on 14 Nov 2026 (results read as lists, no page opened): trial reels eligibility (no report of a change from 1,000 followers and a public account) and caption links (no report of a rollout beyond the Meta Verified test). Nothing STALE found.

## Not checked

- `https://www.socialinsider.io/instagram-benchmarks` (the unit's link for Socialinsider's benchmarks): no search returned this address verbatim, so it was not fetched. The same report (same title, dates and figures) was read at `https://socialinsider.io/social-media-benchmarks/instagram`, which a search did return. Whether the unit's link resolves was not checked.
- Threads posts that Social Media Today links (Mosseri's statements; the @creators post on hashtags): not returned by a search, not opened. Every Mosseri statement was checked against the press report the unit cites, which is how the unit says it cites them.
- Instagram Help Centre: not attempted; the unit cites no Help Centre page.
- 24 of the 42 listed sources were outside the sample and not opened. 18 were opened.
- No site refused, redirected or timed out, and no tool permission was refused.

## Failure rate

- Sample: 15 claims, 14 PASS, 1 FAIL (claim 7, a paraphrase set in quotation marks), 0 STALE, 0 unverifiable. Sample failure rate 1 in 15 (6.7%), not more than one in ten: no full audit.
- All claims checked: 37, of which 31 PASS and 6 FAIL (two on the one misattributed quotation, one unsupported table cell, one stretched paraphrase, two reference titles), 0 STALE, 0 unverifiable. No figure, date, sample size or benchmark was found wrong.

## Counts

- Words (`wc -w unit.md`): 10,591. `##` sections: 13 (§1–§10, Deliverable, Sources, Unsure list). Sources listed: 42.
- Cited claims in the unit, counted by reading each sentence and table row (a script split the text into sentences and rows and marked candidates; each was then kept or dropped by hand): **126**. Per section: §1 15 · §2 14 · §3 14 · §4 14 · §5 8 · §6 10 · §7 7 · §8 6 · §9 8 · §10 7 · D1 11 (IR1–IR10, IR12) · D2 12 (every IG row but IG9) · Templates 0 · Sources 0 · Unsure list 0. Counted once each: a sentence or row that rests a number, date, quotation, attribution or mechanism on a cited source, including a back-reference to a cited statement (§n). Not counted: statements of absence ("no source found"), pointers to other units, Mara's facts, the unit's labelled inferences, reference entries.

## Figures

1. §1, matrix "Instagram's surfaces: whom each serves". Every cell traces to §1's table and text (Feed "followed, plus recommended" / "your activity"; Stories "followed only" / "viewing history"; Explore "not followed" / "information about the post"; Reels "mostly not followed" / "your activity"; Search "the text typed"). Caption dates (31 May 2023; 25 Aug 2021) match the text, and it says the last column is the unit's reading. **PASS.**
2. §3, matrix "Which Instagram format each dataset puts first". Every mark traces to §3's table and "Where they disagree" (Reels first in three, carousels in Socialinsider, "carousels, by 1.69%" in Metricool 2026; engagement marks; populations). Caption dates (14 Oct 2025; 7 Aug 2026; 23 Oct 2024 and 19 Mar 2026; modified 4 Nov 2026) match the text. **PASS.**
3. §9, flow "From a Reel to the YouTube video". The five steps trace to §9 ("tap the name, tap a link", "up to five", no caption links, External / Direct or unknown). Caption dates (18 Apr 2023; 25 Nov 2024; answer 1714921) match the text, and it says the path is the unit's reading. **PASS.**

No figure erratum.

## Mara's facts and pointers

- Register (`case-facts.md`, "Set by PB7" and earlier entries): 140 followers; Tuesday, Thursday, Saturday; four Reels and two carousels a fortnight at 30 minutes; 27 + 12 in Q1; 36 qualifying posts (24 + 12) on Mon 5 Apr 2027 with the Reels of 30 Mar, 1 Apr and 3 Apr recorded only; 37 (23 + 14) in Q2, 29 (15 Reels) with PB9's guide build; profile links, the "Full video: link in profile" line, the fortnightly Story (5 of 15 minutes); the post-1 caption line and five hashtags; public creator account with the search-engine setting on; IR8, IR11, IR12; IG1–IG13. All agree. The calendar holds (4 Jan 2027 is a Monday, 13 weeks × 3 = 39 posts, 27 Mar is a Saturday). "(Mara, fictional)" is given at her first naming in §2 and again in D1 and D2. She is nowhere used as evidence about the world.
- Pointers: PB1 I1, I3, I4, I5, I7, D3 read 1 (39 / 37 / 29) and verdict 3; PB2 D3 (name field); PB3 §3 (the 7-accounts and 4-accounts calculation), §4 (no Instagram-to-YouTube rate), D1 trait 8, the shop-window role; PB4 D2, §3 mix, lost-week rules, the season's second video; PB5 §3 (65.5% skip rate; rule 4), §5 (export from her own edit; 30–60 seconds); PB6 YT6 and grade definitions; PB10 §5 (two Reels for the review's hour) and its 60-minute review. All exist and say what PB7 says they say. No flag.
- The unit's own Unsure list carries two filing notes that record a superseded Q2 count (31 posts, then 37 / 29); the body and the register agree on the later one. Not an erratum.

## Deliverable

Exists in full inside the unit: D1 (twelve rules, each with evidence, grade and label, plus hours and the worked caption), D2 (thirteen rows with metric, place in Insights, frequency, PB1 row, reference and Mara's Q1 entry), T1 and T2 (templates whose blanks say what goes in them). It follows from the body: every rule's evidence cell names a source the body cites; rules and thresholds with no source are graded convention (IR11, the 4:2 split, the 7-day wait, IR10's trigger, IR12's thresholds). Usable without the unit: yes for the rules and rows; the pointers to PB4, PB5 and PB1 need those units' deliverables, which is the course's design. Corrections: IG11's reference cell (PB7-4). IR5 states the hashtag point without quotation marks and needs no change.

## Course goal and sourcing standard

- Goal: the unit gives the third outcome its Instagram half (rows to read each quarter against sourced benchmarks, with the format test and flag that feed the continue / change / stop decision) and keeps the twelve-week system inside the hours budget. It moves the reader toward the stated outcomes.
- Advice without evidence: none found. Each recommendation is tied to a cited statement or labelled convention, inference or "her rule"; vendor data is labelled vendor and correlational; each claim names its platform; changeable facts carry 12 Nov 2026 or their own date.
- Standard, Part 1: one breach of "words in quotation marks are the source's exact words" in the sense the reader takes them (PB7-1, PB7-2); two reference titles that are not the pages' titles (PB7-5, PB7-6). Part 5: no breach found; no private-course reference found; one internal flag label left in the Unsure list (PB7-8).
- Known and disclosed, not re-reported: Mosseri's statements are cited through the press, not to the statements themselves, which the brief asks for; the unit says so in its opening paragraph.

## Verdict

**PASS.** Sample failure rate 1 in 15; no full audit run. Eight errata (2 should-fix, 6 minor), no flag.

## Most consequential errors (this unit)

1. A reporter's paraphrase is printed as Mosseri's own words: "don't improve visibility" (§7, §10 item 1). The substance is as Social Media Today reports it; the quotation marks are not earned. A reader who checks the citation will not find Mosseri saying those words.
2. D2 IG11 tells Mara that eligibility is "regained after 30 days of mostly original posts". Instagram says "a significant percentage" over a rolling 30 days and does not define it; the cell states a rule firmer than the source.
3. The Reposts row says "All accounts" can use the feature; Meta's page states no eligibility.

None changes a rule, a number or a row of the deliverable.

## Bibliography line

New sources to add: none. Sources to mark failed: none. Two titles to correct (Social Media Today, 22 Jan 2025 and 13 Jul 2025; PB7-5, PB7-6); Socialinsider's benchmarks were read at https://socialinsider.io/social-media-benchmarks/instagram, the unit's link not checked.

## Changelog line

2026-11-14 · PB7 · Audit 2, stratified sample (claude-fable-5-2, search on): 15 sampled, 1 FAIL (6.7%); 37 checked in all, 6 FAIL, 0 STALE, 0 unverifiable; figures 3 of 3 PASS; verdict PASS, no full audit; 8 errata (2 should-fix, 6 minor), 0 flags.

## Errata

**PB7-1** · should-fix · §7 · Hashtags · verdict FAIL
- Current: `The same article reports Mosseri saying in 2025 that hashtags "don't improve visibility on Instagram", though they are "a great way to let people know what a post is about and connect posts" (same source).`
- Fix: `The same article reports Mosseri saying in May 2025 that hashtags don't improve visibility on Instagram (the article's paraphrase, not his words), though they are "a great way to let people know what a post is about and connect posts" (same source).`
- Basis: Social Media Today, 18 Dec 2025: 'In May this year, Mosseri once again said that hashtags don't improve visibility on Instagram, but they are "a great way to let people know what a post is about and connect posts."' Only the second phrase is in quotation marks in the article. https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/

**PB7-2** · should-fix · §10 · item 1 · verdict FAIL
- Current: `Mosseri said in 2025 that hashtags "don't improve visibility"; Instagram limits them to five (§7).`
- Fix: `Mosseri, as Social Media Today paraphrases him, said in May 2025 that hashtags don't improve visibility; Instagram limits them to five (§7).`
- Basis: As PB7-1: the phrase is the reporter's paraphrase, not a quotation. https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/

**PB7-3** · minor · §6 · table, Reposts row · verdict FAIL
- Current: `| All accounts | [Meta, New Instagram features to help you connect, 6 Aug 2025]`
- Fix: `| No eligibility limit stated on the page | [Meta, New Instagram features to help you connect, 6 Aug 2025]`
- Basis: Meta, 6 Aug 2025, says 'you can repost public reels and feed posts' and states no eligibility. https://about.fb.com/news/2025/08/new-instagram-features-help-you-connect/

**PB7-4** · minor · D2 · IG11 · verdict FAIL
- Current: `Eligible is the expected state; regained after 30 days of mostly original posts (Original content guidelines; Instagram, 30 Apr 2026)`
- Fix: `Eligible is the expected state; regained when a significant percentage of the posts of a rolling 30 days are original (Original content guidelines; Instagram, 30 Apr 2026)`
- Basis: Instagram Creators, 30 Apr 2026: eligibility returns when recent posts are 'considered original in a 30-day period', on a rolling basis; the unit's §5 quotes the guidelines' 'a significant percentage' and notes it is not defined. https://creators.instagram.com/blog/rewarding-original-creators-on-instagram

**PB7-5** · minor · Sources · verdict FAIL
- Current: `- Social Media Today, Instagram shares algorithm insights for 2025, 22 Jan 2025.`
- Fix: `- Social Media Today, Instagram Shares Algorithm Insights To Inform Strategy, 22 Jan 2025.`
- Basis: The article's headline and page title. https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/

**PB7-6** · minor · Sources · verdict FAIL
- Current: `- Social Media Today, Instagram expands access to trial reels, 13 Jul 2025.`
- Fix: `- Social Media Today, Instagram Trial Reels Are Now Available to More Creators, 13 Jul 2025.`
- Basis: The article's headline and page title. https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/

**PB7-7** · minor · Unsure list · item 1 · verdict other
- Current: `rests on Social Media Today's paraphrase of a Mosseri Threads post, 13 Jul 2025;`
- Fix: `rests on Social Media Today's paraphrase of Mosseri, 13 Jul 2025, which links a Threads post on another account (not opened);`
- Basis: SMT credits Mosseri and links a Threads post on the account oncescuradu; whether the words are in a post of Mosseri's own was not confirmed. https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/

**PB7-8** · minor · Unsure list · item 8 · verdict other
- Current: `(§4; flag F32)`
- Fix: `(§4)`
- Basis: brief.txt: the course is shared with anyone; 'flag F32' is an internal label a reader cannot open (the fresh check removed 'flag F6' from §4 for the same reason). No URL: internal consistency.

---

<!-- PB8: f-pb/PB8/audit.md, verbatim -->

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
