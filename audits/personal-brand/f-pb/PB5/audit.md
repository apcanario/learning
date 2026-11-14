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
