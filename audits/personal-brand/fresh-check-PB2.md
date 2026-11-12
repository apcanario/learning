---
audit: fresh check
unit: PB2 · Positioning: the sentence a stranger can repeat
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB2 is owed to the Fable stage (P49)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB2 chat (which ran on Opus 5.5 and only staged, applied, filed and published; the same chat ran W-PB1) in session https://claude.ai/code/session_01KMmgQxN77fE9zvQ2PYwtZy
verdict: fix · 1 error, 3 should-fix, 6 minor
---

The checker's final report, verbatim, from its hand-back in the chat (the checker was told to return its report rather than write a file; the harness's indentation of the hand-back is removed). Saved before any finding was applied.

Model: claude-opus-5-5

# Fresh check: PB2, Positioning: the sentence a stranger can repeat

I read only what is in /home/claude/packets/PB2-check/. I edited nothing and published nothing. Every live page I opened came from a URL that a WebSearch in this agent returned. One fetch was redirected (typeset.io) and I did not follow it. I could not run kit/private_terms.py because it is not in the packet, so I grepped the unit for private terms instead (finding 3 below covers the one hit). All three viz blocks render with tools/viz.py.

## 1 · Coverage
- What a positioning is, set against a description of the person: covered (§1).
- The three patterns, how each survives a change of subject, graded, with the thinness of the evidence stated: covered (§2 and its matrix).
- The repeat-back test with strangers: covered (§3, D5).
- Naming:
  - Account name against handle: covered.
  - Limits and change rules, dated: covered.
  - Availability on both platforms: the procedure is covered, but the check itself is thin. No handle was checked in either app, and the unit says so plainly.
  - Trademark left to PB8: covered.
- Instagram bio and YouTube description, with their limits: covered (§5).
- Deliverable:
  - One sentence plus a 60-word expansion: present.
  - Three name options with their checks and one pick: present.
  - Bio and description written in full: present.
  - Repeat-back script: present.
  - Template: present.

## 2 · Findings
[error] [accuracy] §4, Instagram Name row of the limits table; Current: "No limit found stated by Instagram or by the third-party page checked"; Problem: the row cites SocialBee, and SocialBee does state a limit: "Instagram allows up to 30 characters for both your username and your display name." Writer-unsure item 4 has the same mistake; Fix: "30 characters, reported by a third party (SocialBee: up to 30 characters for both your username and your display name); no Instagram page found states it"; Basis: SocialBee, 27 Apr 2026, modified 5 Nov 2026, https://socialbee.com/blog/how-to-change-your-name-on-instagram/

[minor] [accuracy] D3, Name field; Current: "(26 characters, counted by script; under 30, since no Instagram limit was found)"; Problem: follows from the finding above; a third-party figure of 30 exists. The count of 26 is correct; Fix: "(26 characters, counted by script; under the 30 a third party reports, since no Instagram page found states a limit)"; Basis: as above

[should-fix] [deliverable] D2, third reason for the pick; Current: "The box is the one detail a stranger repeats; "furniture" in the name field and bio fixes the trade reading."; Problem: D3's name field is "Mara · One Box Restoration" and does not contain "furniture". The word is in bio line 1 and in the first line of the D4 description; Fix: "The box is the one detail a stranger repeats; "Mid-century furniture" in the first line of the bio and of the description fixes the trade reading."; Basis: unit D3 and D4

[should-fix] [style] §1, opening paragraph; Current: "It was used on 12 November 2026 only to re-check the claims this unit carries from its source material, the platforms' name, handle and text-field rules, two academic citations, and whether the handles chosen for Mara could be found in use."; Problem: (a) "its source material" points at the private course, which a public reader cannot open and should not be told about (brief preamble; Part 5). (b) The sentence is also wrong: the unit cites four academic works, and several sources were found by new searching (Camerer et al., Thomson, Mosseri 2021, Instagram Help, SocialBee, Net Influencer, Khare's site). None of these is in the source unit; Fix: "It was used on 12 November 2026 to check every source this unit cites, including the platforms' name, handle and text-field rules, and to look for the handles chosen for Mara."; Basis: source-units/A1 Sources list (none of the sources named is in it); brief.txt preamble ("never refer to the private course or its units")

[should-fix] [figure] §2 matrix, legend; Current: "{"mark": "YouTube tip", "means": "named as a route to returning viewers, no effect size", "tone": 4}, {"mark": "Boyd; D'Avella", "means": "anecdote, survivors", "tone": 2}"; Problem: tone 4 also colours "Instagram search" (about discovery, not returning viewers), "winners vary subjects" (vendor), "fit, products only" and "attachment, celebrities" (peer-reviewed). The legend therefore tells the reader all of these are YouTube tips about returning viewers. The tone-2 label names only one of the two creator cells; Fix: "{"mark": "source found", "means": "a source bears on the pattern; none gives an effect size or tests a change of subject", "tone": 4}, {"mark": "creator cases", "means": "anecdote, survivors", "tone": 2}"; Basis: unit §2 text; the corrected JSON renders with tools/viz.py

[minor] [attribution] §2, The method, Mike Boyd case; Current: "[Net Influencer, Learning in public, undated, about 2026]"; Problem: the article is dated and has a named author: published 4 March 2026 by Dragomir Stojkov; Fix: "[Net Influencer, Learning in public, 4 Mar 2026]"; Basis: https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/

[minor] [attribution] §2, The person; Current: "according to the same undated profile"; Problem: same as above; Fix: "according to the same profile (4 Mar 2026)"; Basis: as above

[minor] [attribution] Sources; Current: "Net Influencer (Dragomir), "Learning in public: how Mike Boyd built a sustainable YouTube business on curiosity", undated (about 2026)."; Problem: date and full author name; Fix: "Net Influencer (Dragomir Stojkov), "Learning in public: how Mike Boyd built a sustainable YouTube business on curiosity", 4 Mar 2026."; Basis: as above

[minor] [coverage] §4, Checking availability; Current: "**Whether the three handles are in use on either platform was not checked.**"; Problem: D2 names five handles (three options plus the fallbacks @onebox.restoration and @oneboxrestore), and none was checked. Separately, for the filer: case-facts.md says PB2 picks the handle "after checking that the handle is not in use on either platform on the day". The unit could not do that check, so the notes' "Contradictions: none" is not quite right. Text cannot close that gap. Someone has to check in the two apps, or the register line has to be amended; Fix: "**Whether any of the five handles in D2 (the three options and the two fallbacks) is in use on either platform was not checked.**"; Basis: unit D2; case-facts.md, Left free

[minor] [deliverable] D5, If it fails; Current: "Record each run's sheet with the date; PB10 reads it with the quarter's other numbers."; Problem: PB10's brief does not include the repeat-back sheet (notes, Needs 6), so this states as fact something a later unit is not yet asked to do; Fix: "Record each run's sheet with the date and keep it with that quarter's review (PB10)."; Basis: all-briefs.md, PB10

## 3 · Accuracy: the writer's unsure list
1. Handles in use: unverifiable. My search for the handles also found no profile under any of them, and that does not show they are free (same as the unit).
2. Bitly gives 150 and 30, cites no Instagram source, and is dated 19 Dec 2023, updated 29 Sep 2026: PASS.
3. SocialBee's sentences "twice every 14 days" and "may become available for others to claim", with its dates and author: PASS as SocialBee's. No Instagram page states them.
4. No name-field limit found: FAIL (finding 1).
5. Data API limits: PASS. 30 characters is stated for brandingSettings.channel.title (snippet.title states none), 1000 for the description, and 500 in total for keywords. The Help page states no limits: PASS. That Studio enforces the same limits is unverifiable.
6. Graham Mann quotes are verbatim: PASS. McGraw-Hill, New York, 1981 is confirmed by the TAMU library record (https://libcat.library.tamu.edu/Record/in00000640581/Versions).
7. Aaker and Keller: the CiteDrive abstract is PASS, and its 2018 year is confirmed as wrong. Pages 54(1), 27–41 are confirmed by the sciencegate record (https://next.sciencegate.app/document/10.2307/1252171): PASS.
8. Net Influencer: the content is PASS and gives no numbers for the second channel. "Undated" is FAIL; the article is dated 4 Mar 2026 (findings above).
9. Khare: "award-winning docuseries Challenge Accepted", "tackled the world's toughest professions and stunts" and 5.43M are on her About page, and the page is undated: PASS.
10. Rosetta: nine 2019 titles contain "30 days"; sugar is dated 12 Feb 2019, breathwork 10 Dec 2019, and zone 2 30 Mar 2026: PASS. These were not checked against YouTube.

One more claim is unverifiable: the D2 collision results from the writer's own web searches. My search for "One Box Restoration" returned software-restore pages and a storage-box restoration project, not building or cleaning businesses. Search results vary, so neither result can be checked against the other.

## 4 · Figures and labels
- Every number names its source: vidIQ, the Data API, Bitly, SocialBee and so on.
- Everything derived is marked as derived: the 20 points from five people, and the word and character counts.
- Conventions are marked as unsourced: five people, a ten-minute delay, four of five to pass.
- Vendor data is labelled (OverseerOS: vendor, survivor sample, correlational).
- Anecdote is labelled for Boyd, D'Avella and Khare.
- Third-party pages are labelled as third-party.
- Labels conform to PB1 §1. "Third-party" and "Platform statement" are additions, used consistently.

## 5 · Deliverable
Every part is present in full and follows from §1–§5. It can be used on its own. The template's blanks each say what goes in them. I recounted everything with Python:

| Field | Count | Limit |
|---|---|---|
| Sentence | 29 words | — |
| Expansion | 60 words | 60 words |
| Bio | 111 characters | 150 |
| Description | 841 characters | 1,000 |
| Name field | 26 characters | 30 |
| Username / handle | 17 characters | 30 |
| Channel name | 19 characters | 30 |
| No Workshop Restoration | 23 characters | 30 |
| @noworkshoprestoration | 21 characters | 30 |
| @mara.venn | 9 characters | 30 |
| Keywords | 152 characters | 500 |

My fixes change none of these fields.

## 6 · Errata from the A1 fresh-check reports that touch PB2
- OverseerOS is called "a vendor of YouTube analytics tools": applied.
- "Equal to" is replaced by "ranks none of the three": applied.
- Aaker and Keller pages 27–41: applied.
- The "unique identifier" misquote: not carried over.
- The rest are about the private reader and do not apply.

PB1 pointers all match PB1:
- The §1 labels.
- The cadence of 26 videos a year and three Instagram posts a week from the same footage.
- Day one, 4 January 2027.
- The Q1 review on Monday 5 April 2027.

## 7 · Figures
1. **Matrix, §2: FIX** (legend, finding above). Every cell traces to the §2 text:
   - "YouTube tip; Instagram search"
   - "winners vary subjects" (quoted in §2's grade)
   - "fit, products only"
   - "attachment, celebrities"
   - "Boyd; D'Avella"
   - "Khare; D'Avella"
   - "none" ("No dataset found compares…")
   
   The caption names the section and its sources. The kind fits (items by sections).
2. **Flow, §3: PASS.** All seven steps match §3 steps 1–7. The caption names §3 and Camerer et al. and marks the conventions. The kind fits (a sequence).
3. **Decision, D2: PASS.** The labels match the D2 Override and Conditions text (the override condition, the handles, the fallbacks, PB8). The caption names D2 and the YouTube Help sources. The kind fits (a rule with branches).

## 8 · The writer's Source errors list
All six are confirmed, and each quoted A1 line exists in source-units/A1.
1. The 2657964 page is now titled "Manage your YouTube channel's profile" and carries "You can change your handle twice within a 14-day period": confirmed.
2. The 30-character limit is on brandingSettings.channel.title, and snippet.title has no maximum: confirmed.
3. Handles: middle dots allowed, Han/Hangul 1–10, Ethiopic/Hiragana/Katakana 2–20, "aren't case-sensitive", page titled "Learn about YouTube handles": confirmed.
4. Answer 15920820: twice in 14 days, the previous handle held for 14 days, both URLs work, then "Afterward, the handle will become available for other users to select as their handle": confirmed.
5. vidIQ Mike Boyd: 2.93M · 197 · 477,008,214, last updated 11 Nov 2026: confirmed.
6. vidIQ Matt D'Avella: 4,060,000 · 472 · 337,764,525, as of 5 Nov 2026: confirmed.

## 9 · Part 5, rule by rule
- **Sourced where made:** met.
- **Acceptable source types:** met in part.
  - Bitly and SocialBee are vendor blog pages, not datasets, and their 150 and 30 enter D3 as ceilings. The unit labels them third-party and names the app as the authority.
  - Net Influencer, Laughing Squid and Rosetta are press or index sources for creator cases whose numbers come from vidIQ.
- **Anecdote, vendor and correlational data labelled:** met.
- **Platform named for growth, format and metric claims:** met (§2 Instagram/YouTube split; "YouTube only").
- **Carried-over claims re-verified:** met (notes; six source errors confirmed above).
- **Nothing private, no reference to the private course:** not met at one point, §1 "its source material" (finding 3). No names, places, sports or handles from the private course appear.
- **Mara labelled and kept consistent:** met. The one tension is the register's handle-check condition (the handles finding).
- **Tax and legal:** met.
  - No country's figures appear.
  - The trademark question is deferred to PB8, as the brief says.
  - "Information, not legal advice" is stated in §4.
  - The rules on asking strangers are deferred to PB8.
- **No uncited figures, conventions marked:** met.
- **Changeable facts dated:** met (12 Nov 2026 throughout).
- **Deliverable plus template:** met.
- **Not advice without evidence:** met. The working rule is stated as built from weak evidence.
- **Links as links:** met. The Data API link is to developers.google.cn; notes Needs 8 already raises this.

The frontmatter says "search: off", but the unit did new searching. Whether that header should change is the filer's call.

## 10 · Read as the public persona
The unit assumes nothing only a private-course reader would know, with one exception: §1's "the claims this unit carries from its source material" (finding 3). It names no private person, employer, city, sport, business or handle. Course pointers are only to PB1–PB10.

## Confirmed
- Ries and Trout definition and "The mind rejects complexity, so a strong position is usually a single word or idea you can own": https://grahammann.net/book-notes/positioning-al-ries-jack-trout
- Camerer, Loewenstein and Weber, JPE 97(5), 1232–1254, 1989: "market forces reduce the curse by approximately 50 percent, but do not eliminate it" — https://ideas.repec.org/a/ucp/jpolec/v97y1989i5p1232-54.html
- YouTube Help 13615784, both tip quotes verbatim, no effect sizes or ranking: https://support.google.com/youtube/answer/13615784?hl=en
- Mosseri, 25 Aug 2021, "We try to match what you type with relevant usernames, bios, captions, hashtags and places", plus the handle, name and bio tips: https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works/
- OverseerOS, Zaid Alkuheli, 21 Aug 2026:
  - 1,620 videos, 163 channels, 97.5%, 20%
  - "Successful channels repeated a recognizable world…"
  - "we cannot calculate the probability that a broad channel succeeds"
  - topics machine-extracted, correlational
  - https://www.overseeros.com/blog/stick-to-one-niche-youtube
- Beaupré quotes via SEJ, Matt G. Southern, 4 Mar 2024: https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/
- Aaker and Keller "fit" abstract, CiteDrive year 2018: https://www.citedrive.com/en/discovery/consumer-evaluations-of-brand-extensions/
- Bottomley and Holden, JMR 38(4), 494–500, 2001; original study plus seven replications; "varies by brand and culture"; "premature…" verbatim: https://researchers.mq.edu.au/en/publications/do-we-really-know-how-consumers-evaluate-brand-extensions-empiric/
- Thomson, JM 70(3), 104–119, 2006; three studies; both quotes verbatim: https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_227781169
- Laughing Squid, Lori Dorn, 30 Dec 2016; round-up title; the six skills: https://laughingsquid.com/a-recap-of-everything-mike-boyd-taught-himself-to-quickly-learn-in-2016/
- vidIQ Mike Boyd, joined 23 Oct 2008: https://vidiq.com/youtube-stats/channel/@mikeboyd/
- vidIQ Matt D'Avella, joined 25 Jul 2011: https://vidiq.com/youtube-stats/channel/@mattdavella/
- Rosetta 2019 titles: https://rosetta.to/u/mattdavella/2019
- Rosetta zone 2: https://rosetta.to/u/mattdavella/i-tried-zone-2-training-for-30-days-what-i-learned
- Michelle Khare About: https://michellekhare.com/about
- YouTube Help 2657964:
  - name twice within 14 days
  - badge removed
  - "Your description is accessible in the channel header"
  - Community Guidelines
  - no character limits
  - https://support.google.com/youtube/answer/2657964?hl=en
- YouTube Help 11585688:
  - all handle rules
  - "distinct from channel names"
  - "Each channel can only have one handle"
  - "already being used"
  - https://support.google.com/youtube/answer/11585688?hl=en
- YouTube Help 15920820, handle change and release rules: https://support.google.com/youtube/answer/15920820
- YouTube Data API, Channels: title 30 (brandingSettings), description 1000, keywords 500 in total — https://developers.google.cn/youtube/v3/docs/channels?hl=en
- Bitly, Daniel Wiersema, 19 Dec 2023, updated 29 Sep 2026: 150 and 30, no Instagram source — https://bitly.com/blog/instagram-character-limit/
- Instagram Help: "You can add periods, numbers, underscores or abbreviations…" — https://help.instagram.com/513717858639392
- SocialBee, Roxana, 27 Apr 2026, modified 5 Nov 2026, both quoted lines: https://socialbee.com/blog/how-to-change-your-name-on-instagram/
- Every Mara fact agrees with case-facts.md and PB1 (age, job, followers, phone, hours, cadence, day one, Q1 date), apart from the handle-check tension noted above. Mara is labelled "(Mara, fictional)" on first use in §1, and the new facts are labelled in D1–D5.

PB2, verdict fix: 1 error, 3 should-fix, 6 minor. Without the error, the keep rule would have been met, but the should-fix edits are still needed.

## Maintainer's notes (W-PB2 chat, 12 Nov 2026)

- All ten findings applied by script as exact replacements, each Current found once in the unit as checked (the checked copy equal to the filed draft, commit 136192c). Items 4 and 8 of the writer's unsure list were brought into line with findings 1 and 6 to 8.
- The front matter keeps `search: off`: the searches were the re-checks and the platform rules the brief asks to date, which method §4 allows with search off.
- The checker's tension between the register's handle-check line and what the unit could do is raised as flag F13; Contradictions in the writer's notes otherwise none.
- F2 stays open: it names every unit from PB2 to DD-PB2, so it must reach the later writers.
- Figure 1 (matrix), fixed by finding 5, was re-checked by a new Opus 5.5 agent (claude-opus-5-5, as it states) from the text without figures, the captions and the frames: PASS.
- Figure 3 (decision), which the checker passed, broke the handles mid-word on a phone in the maintainer's look at the frames (`@oneboxrestoratio n`); its labels were shortened to name the picked and fallback handles by role, with the handles in the caption, and re-checked by a new agent (result in the unit's fresh-check line).
- No agent transcript is kept on disk in this session, so none could be checked by script; each agent's model is the one it states.
