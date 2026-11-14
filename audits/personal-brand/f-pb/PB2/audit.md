Model: claude-fable-5-2

# Stratified-sample audit · PB2 · Positioning: the sentence a stranger can repeat · 14 November 2026 · search on

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2. Read only `/home/claude/fpb/PB2`; wrote only `out/`. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool used.
- Unit: `unit.md` (PB2, written 2026-11-12 by Opus 5.5, front matter `search: off`). Not edited.
- Web rule followed: WebSearch first; WebFetch only on a URL a search in this agent returned verbatim.
- `out/` was empty at the start: no earlier run to resume.

## Sample (recorded before any check)

One claim per `##` section (9 sections).

| # | Section | Sampled claim | Source the unit cites |
|---|---|---|---|
| S1 | §1 | Camerer, Loewenstein and Weber named the "curse of knowledge"; markets reduced it by "approximately 50 percent" without removing it; JPE 97(5), 1989, 1232–1254 | IDEAS/RePEc record |
| S2 | §2 | OverseerOS: 1,620 long-form videos with 1M+ views from 163 channels with five or more such videos; 97.5% of channels had a different topic query for every video; median most-repeated entity in 20.0% of winners; quote "Successful channels repeated a recognizable world…"; 21 Aug 2026 | OverseerOS article |
| S3 | §3 | With five people, one answer moves the result by 20 percentage points (derived: 1 of 5); the reason for strangers is sourced, the five / ten minutes / four of five are conventions | derived; Camerer et al. |
| S4 | §4 | YouTube handle: changeable twice within a 14-day period; previous handle held 14 days, both URLs work, then "Afterward, the handle will become available for other users to select" | YouTube Help 15920820 (and 11585688) |
| S5 | §5 | YouTube channel description: 1,000 characters in the Data API; "accessible in the channel header" | YouTube Data API Channels; YouTube Help 2657964 |
| S6 | Deliverable | D3 bio is 111 characters including line breaks, against a third-party limit of 150 (Bitly) | script count; Bitly |
| S7 | Template | T4 "Handle: … 3–30" characters | YouTube Help 11585688 |
| S8 | Sources | Thomson, "Human brands: investigating antecedents to consumers' strong attachments to celebrities", *Journal of Marketing* 70(3), 2006, 104–119 | library record |
| S9 | Unsure list | Instagram name-change rule "twice every 14 days" and old username "may become available for others to claim" rest on SocialBee, 27 Apr 2026, modified 5 Nov 2026 | SocialBee |

## Table (sample)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | "Curse of knowledge"; markets reduced it by "approximately 50 percent" without removing it; JPE 97(5), 1989, 1232–1254 | https://ideas.repec.org/a/ucp/jpolec/v97y1989i5p1232-54.html ; wording confirmed in the paper itself, https://www.cmu.edu/dietrich/sds/docs/loewenstein/CurseknowledgeEconSet.pdf | PASS | Authors, journal, volume, issue, year, pages hold. The abstract reads "reduce the curse by approximately 50 percent but do not eliminate it". The unit's limit ("economic judgments, not profiles") is right. |
| S2 | §2 | OverseerOS: 1,620 videos, 163 channels, 1M+ views, five or more per channel, English, long-form; 97.5%; 20.0%; the "recognizable world" quote; limits; 21 Aug 2026 | https://www.overseeros.com/blog/stick-to-one-niche-youtube | PASS | Every figure, the date, the author and both quotations hold. The limits are the article's own (no failed channels, machine-extracted labels, "Correlation Is Not Causation"). "Vendor of YouTube analytics tools" fits how the site describes itself. |
| S3 | §3 | Five people: one answer moves the result by 20 percentage points (derived: 1 of 5); the number, delay and pass mark are conventions | derived; Camerer et al. (S1) | PASS | 1/5 = 20 points. The unit says in the text and in the figure caption that the five, the ten minutes and four of five are unsourced conventions. |
| S4 | §4 | YouTube handle: twice within a 14-day period; previous handle held 14 days; both URLs work; "Afterward, the handle will become available for other users to select" | https://support.google.com/youtube/answer/15920820 | PASS | All four points verbatim on the page (the sentence continues "as their handle"). |
| S5 | §5 | Channel description: 1,000 characters in the Data API; "Your description is accessible in the channel header" | https://developers.google.cn/youtube/v3/docs/channels?hl=en ; https://support.google.com/youtube/answer/2657964 | PASS | "The property's value has a maximum length of 1000 characters" (snippet.description and brandingSettings.channel.description). Help sentence verbatim; the Help page states no limit, as the unit says. Opened as the search returned it, without `?hl=en`. |
| S6 | Deliverable | D3 bio is 111 characters including line breaks; third-party limit 150 | script count; https://bitly.com/blog/instagram-character-limit/ | PASS | Recounted: 111. Bitly: "The Instagram bio character limit is 150 characters." It cites no Instagram page, as the unit says. |
| S7 | Template | T4 handle "3–30" characters | https://support.google.com/youtube/answer/11585688?hl=en | PASS | "between 3-30 characters"; the Han/Hangul 1–10 and Ethiopic/Hiragana/Katakana 2–20 exceptions in §4 hold too. |
| S8 | Sources | Thomson, "Human brands…", *Journal of Marketing* 70(3), 2006, 104–119 | https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_227781169 | PASS | Author, title, journal, volume, issue, year (July 2006), pages hold. |
| S9 | Unsure list | Instagram display-name rule "twice every 14 days" and old username "may become available for others to claim" rest on SocialBee, 27 Apr 2026, modified 5 Nov 2026 | https://socialbee.com/blog/how-to-change-your-name-on-instagram/ | PASS | Both wordings, the author (Roxana) and both dates hold; they are SocialBee's statements, labelled third-party in the unit. |

## Also checked (beyond the sample; counted in the totals)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| A1 | §1 | Both Ries and Trout wordings, as quoted from Graham Mann's notes | https://grahammann.net/book-notes/positioning-al-ries-jack-trout | PASS | Verbatim. The page gives 1981 and no publisher; "McGraw-Hill" was not checked here. The unit says the book was not opened. |
| A2 | §2 | YouTube tips: both quotations; no effect sizes, no ranking | https://support.google.com/youtube/answer/13615784?hl=en | PASS | Verbatim, under the returning-viewer tips. |
| A3 | §2, §5 | Mosseri, 25 Aug 2021: search matches "usernames, bios, captions, hashtags and places"; handle, profile name and bio advice | https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works/ | PASS | Quote verbatim; the advice is paraphrased fairly (the bio tip also mentions locations). |
| A4 | §2 | Beaupré's two quotations, via Search Engine Journal, 4 Mar 2024 | https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/ | PASS | Both verbatim; author and date hold. The unit marks its own inference from them as untested. |
| A5 | §2 | Aaker and Keller: "a perception of 'fit' between the two product classes", high quality of the original brand; CiteDrive year 2018 in error | https://www.citedrive.com/en/discovery/consumer-evaluations-of-brand-extensions/ | PASS | Abstract wording and the 2018 error hold. Volume and pages (54(1), 27–41) are not on this record and were not re-checked. |
| A6 | §2 | Bottomley and Holden, JMR 38(4), 2001, 494–500; original plus seven replications; both quotations | https://researchers.mq.edu.au/en/publications/do-we-really-know-how-consumers-evaluate-brand-extensions-empiric/ | PASS | All hold. |
| A7 | §2 | Net Influencer, 4 Mar 2026: "himself learning a new skill as quickly as possible"; the second channel Mike Boyd Climbs, no numbers | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS | Quote verbatim; author Dragomir Stojkov; the reason for the second channel and the absence of numbers hold. |
| A8 | §2 | Laughing Squid, 30 Dec 2016 (Lori Dorn): the six skills of the 2016 round-up | https://laughingsquid.com/a-recap-of-everything-mike-boyd-taught-himself-to-quickly-learn-in-2016/ | PASS | Violin, lock, Rubik's Cube under two minutes, reverse-steering bicycle, juggling, unicycle ("among other things"). |
| A9 | §2 | The round-up is "titled" "A round up of 2016's 'Learn Quick'" | same page | FAIL (minor) | The page quotes "A round up of 2016's "Learn Quick". What will you learn in 2017?" as a line under the embedded video. It does not say this is the video's title, and its own headline is different. "Titled" is not supported. Erratum PB2-1. |
| A10 | §2 | vidIQ, Mike Boyd: created 23 Oct 2008; 2.93 million subscribers; 197 videos; 477,008,214 views on 11 Nov 2026 | https://vidiq.com/youtube-stats/channel/@mikeboyd/ | PASS | Join date, subscribers and video count hold. The page now reads 477,016,889 views, updated 13 Nov 2026; the unit's figure is dated 11 Nov and is a snapshot, so no change. |
| A11 | §2 | Rosetta: nine 2019 titles with "30 days"; sugar 12 Feb 2019; breathwork 10 Dec 2019; zone 2 on 30 Mar 2026 | https://rosetta.to/u/mattdavella/2019 ; https://rosetta.to/u/mattdavella/i-quit-sugar-for-30-days ; https://rosetta.to/u/mattdavella/i-tried-zone-2-training-for-30-days-what-i-learned | PASS | Nine counted; titles and all three dates hold. |
| A12 | §2 | vidIQ, Matt D'Avella: created 25 Jul 2011; 4.06 million subscribers; 472 videos on 5 Nov 2026 | https://vidiq.com/youtube-stats/channel/@mattdavella/ | PASS | All hold; the page is still dated 5 Nov 2026. |
| A13 | §2 | Michelle Khare: "award-winning docuseries Challenge Accepted"; "tackled the world's toughest professions and stunts"; 5.43 million, undated | https://michellekhare.com/about | PASS | Both phrases and 5.43M on the page; no date beyond a © 2026 footer. |
| A14 | §2 | Thomson: three studies; both quotations | library record (S8) | PASS | Verbatim in the abstract; three studies. |
| A15 | §4 | YouTube handle rules: allowed characters, none at start or end, not case-sensitive, one per channel, "already being used", "are distinct from channel names" | https://support.google.com/youtube/answer/11585688?hl=en | PASS | All hold. |
| A16 | §4 | Channel name: "You can change your channel name twice within a 14-day period"; "Changing your name will remove your verification badge" | https://support.google.com/youtube/answer/2657964 | PASS | Both verbatim. |
| A17 | §4, §5 | Data API: channel title 30 characters (brandingSettings.channel.title); keywords 500 in total | https://developers.google.cn/youtube/v3/docs/channels?hl=en | PASS | Both hold; snippet.title states no maximum. The page calls keywords "a space-separated list of strings"; D4 writes them with commas, which the unit does not source. Observation, no erratum. |
| A18 | §4 | Instagram Help: "periods, numbers, underscores or abbreviations"; no limit or release rule stated | https://help.instagram.com/513717858639392 | PASS | Sentence verbatim; the page gives no limit and no rule on old usernames. |
| A19 | §4 | SocialBee: up to 30 characters for username and display name | https://socialbee.com/blog/how-to-change-your-name-on-instagram/ | PASS | "Instagram allows up to 30 characters for both your username and your display name." |
| A20 | §4, Sources | Bitly: username 30; Daniel Wiersema; 19 Dec 2023, updated 29 Sep 2026; no Instagram source | https://bitly.com/blog/instagram-character-limit/ | PASS | All hold. |
| A21 | Deliverable | Counts: sentence 29 words; expansion 60 words; name field 26; description 841; handles 17, 21, 9; names 19, 23, 9; keywords 152 of 500 | script in this audit | PASS | All recounted and equal. 4 Jan 2027, 5 Apr 2027 and 7 Dec 2026 are Mondays. |
| A22 | §1, Deliverable | Mara's facts against `case-facts.md` | register | PASS | Base facts, PB1's cadence and dates, and every "Set by PB2" line agree; the handle is provisional in both. |
| A23 | whole unit | Pointers to PB1 §1 (labels), PB3 (audience), PB4 (series), PB6, PB7 (formats; sending a viewer to YouTube, §9), PB8 (trademark §6.7 for EU, UK, US; disclosure; other people's image §6.2), PB10 (run 2 at the review) | `others/` | PASS | Each pointed-to unit does what PB2 says it does. |

## Not checked

- No URL was refused, redirected or timed out, and no tool call was refused for permission.
- Not attempted: Aaker and Keller's pages 27–41 at the DOI (the unit reads the abstract on CiteDrive; the fresh check confirmed the pages elsewhere); "McGraw-Hill" as the 1981 publisher; whether any of the five handles is in use (no tool here can open the two apps; the unit and the register both say so).
- https://help.instagram.com/182492381886913 (returned by a search, opened to look for an Instagram-stated username limit): the page served no article text. The unit's statement that no Instagram page found states the limit stands unchanged.

## Failure rate

- Sample: 9 claims, 0 FAIL, 0 STALE, 0 unverifiable. Failure rate 0 in 9 (0%). The one-in-ten rule is not triggered; no full audit run.
- All claims checked: 32 (9 sampled, 23 also checked): 31 PASS, 1 FAIL (minor), 0 STALE, 0 unverifiable.

## Counts

- Words: 8,183 (`wc -w unit.md`). `##` sections: 9.
- Cited claims in the unit: 65, tallied by section (a sentence or table row resting a number, date, quotation, attribution or mechanism on a cited source counts once; a sentence citing two sources for two facts counts twice; summary restatements in the grades and in "What no source shows" are not counted again):
  - §1: 3 (Ries and Trout attribution; Mann's two quotations; Camerer et al.)
  - §2: 23 (topic 8; method 10; person 5)
  - §3: 1 (the reason for strangers, by back-reference)
  - §4: 13 (handles "distinct"; 7 table rows; 3 in "Three things follow"; 2 in the availability steps)
  - §5: 5
  - Deliverable: 4 (the limits cited in D3 and D4)
  - Template: 7 (the limits in T2, T3, T4)
  - Sources: 0 (24 reference entries; each matches a link in the body and none is uncited)
  - Unsure list: 9

## Figures

1. Matrix, §2: PASS. Every cell traces to §2's text; the caption names its sources; the legend's three marks cover every tone used.
2. Flow, §3: PASS. Seven steps equal §3's steps 1 to 7; the caption marks the conventions as unsourced.
3. Decision, D2: PASS. The override question, both outcomes, the handles in the caption and the order of fallbacks equal D2's text.

## Deliverable

Present in full: D1 (sentence and 60-word expansion), D2 (three options, the checks, the pick, the override, the conditions), D3 (username, name field, bio), D4 (name, handle, description, keywords), D5 (the script, scoring, pass mark, what to do on a fail), then the template T1 to T5 with every blank saying what goes in it. It follows from §1 to §5, adds no unsourced claim about the world, states what was not checked (the handles, the trademark), and can be used without the body. Every count in it is right.

## Course goal and standard

- Goal: the unit delivers the first outcome (one sentence saying who the account is for and what it gives) and puts it into both profiles.
- Standard: claims are sourced where made; vendor, third-party, anecdote and survivor labels are applied; platforms are named; conventions are marked as unsourced; the trademark question is left to PB8 with "information, not legal advice".
- Advice without evidence: none that decides anything. Two small unsourced lines remain, neither in the deliverable as a claim: §4 step 3, "viewers will confuse the two" (a reason given without a source), and D4's comma-separated keywords (the Data API describes a space-separated list). Reported as observations, no errata.
- Front matter says `search: off` while the unit states search was used on 12 Nov 2026 to check its sources; the unit explains this in its first paragraph. No change proposed.

## Verdict

**PB2: PASS.** Sample 0 FAIL in 9; no full audit run. One minor erratum from the wider check.

## Most consequential errors

1. §2 calls a line that Laughing Squid quotes under Mike Boyd's video the video's title. The page does not say it is the title. Nothing in the unit's argument depends on it.

No other error found.

## Bibliography line

No source to mark failed. Optional addition: the paper itself for Camerer, Loewenstein and Weber (https://www.cmu.edu/dietrich/sds/docs/loewenstein/CurseknowledgeEconSet.pdf), which carries the exact "approximately 50 percent" wording.

## Changelog line

2026-11-14 · PB2 stratified-sample audit (Audit 1, PB) · claude-fable-5-2 · PASS: 9 sampled, 0 FAIL; 32 checked in all, 1 minor FAIL (Laughing Squid "titled"), 0 STALE, 0 unverifiable; 3 figures PASS; 1 erratum (PB2-1), no flags.

## Errata

**PB2-1** · minor · FAIL · §2, The method or repeatable format (creator cases)

- Current: `and his 2016 round-up, titled "A round up of 2016's 'Learn Quick'", covered`
- Fix: `and his 2016 round-up video, which the page quotes as "A round up of 2016's 'Learn Quick'", covered`
- Basis: the Laughing Squid page prints "A round up of 2016's "Learn Quick". What will you learn in 2017?" as a quoted line under the embedded video and does not call it the title; its own headline is "A Recap of Everything Mike Boyd Taught Himself to Quickly Learn in 2016". https://laughingsquid.com/a-recap-of-everything-mike-boyd-taught-himself-to-quickly-learn-in-2016/
- `grep -c -F` on Current: 1.
