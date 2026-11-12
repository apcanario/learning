---
audit: fresh check
unit: PB5 · Production craft with a phone
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB5 is owed to the Fable stage (P49)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB5 chat (which ran on Opus 5.5 and only staged, applied, filed and published; the same chat runs W-PB6) in session https://claude.ai/code/session_01KMmgQyyVNoMqGMdFywhNmh
verdict: fix · 0 errors, 3 should-fix, 11 minor
---

The checker's final report, verbatim, from its hand-back in the chat (the checker was told to return its report rather than write a file; the harness's indentation of the hand-back is removed). Saved before any finding was applied.

Model: claude-opus-5-5

# PB5 fresh check: Production craft with a phone

**Verdict: fix. 0 errors, 3 should-fix, 11 minor.** Nothing was edited and nothing was published.

**Method**
- I read only files in /tmp/pb5/check/: the unit, the brief, sourcing-standard Parts 1 and 5, case-facts, notes, filed units PB1–PB4, and A5 with its fresh check.
- I fetched only URLs that a search in this run had returned.
- The Gwern.net copy of Newman and Schwarz was never returned by a search, so I did not fetch it.
- All four viz blocks pass `check_keys` and render without error.

## (1) Coverage
- **Covered:**
  - Filming alone: frame, light, one clip per step, a five-shot list.
  - Audio: the common claim shown to have no source, and the evidence in each direction.
  - The opening seconds: each platform's window, every figure labelled.
  - Long-form structure.
  - Shorts and Reels: length, hook, captions and cover.
  - Carousels: the limit as Instagram states it (dated), the first slide, the order.
  - Titles and thumbnails inside YouTube's three statements.
  - Captions and contrast.
  - A time-boxed edit workflow.
  - What not to buy.
  - The deliverable: checklist (pre, during, post), timed 10-minute edit, Reel template, carousel template, each worked for Mara, then blank templates.
- **Thin:** the Shorts cover. Only the Reel cover is treated (finding 9).

## Findings

1. [should-fix | accuracy] §6, The shape
   - Current: `Vendor guides give 4:5 at 1080 × 1350 pixels as the tallest feed size, with the grid showing a 3:4 preview: "Stick with the 4:5 format (1080 x 1350 px) for feed posts" ([Metricool, Best Instagram post sizes, 21 Jan 2026](https://metricool.com/instagram-image-size/); vendor guide; no Instagram page stating the size was found).`
   - Problem: This is stale. On 28 May 2025 Instagram (via its Creators channel) announced that 3:4 images appear as shot, in single posts and in carousels. That is taller than 4:5 and matches the grid. The Metricool quotation itself is accurate.
   - Fix: `Instagram announced on 28 May 2025 that "when you upload a 3:4 image it'll now appear exactly as you shot it", and that "This works with both single-photo posts and carousels" ([Social Media Today, 28 May 2025](https://www.socialmediatoday.com/news/instagram-adds-support-phone-camera-aspect-ratio-images), quoting Instagram's Creators channel; platform statement via the press; no Instagram help page stating feed sizes was found). A vendor guide still advises "Stick with the 4:5 format (1080 x 1350 px) for feed posts" and says the grid shows a 3:4 preview ([Metricool, Best Instagram post sizes, 21 Jan 2026](https://metricool.com/instagram-image-size/); vendor guide).`
   - Basis: https://www.socialmediatoday.com/news/instagram-adds-support-phone-camera-aspect-ratio-images ; https://metricool.com/instagram-image-size/

2. [should-fix | accuracy] §5, Length
   - Current: `no Instagram statement of a limit above three minutes was found, so the length selector in the app is the check.`
   - Problem: Instagram did announce 20-minute recording in the Reels camera (Social Media Today, 23 Nov 2025, quoting Instagram; PetaPixel, 25 Nov 2025, citing Instagram's @design account). Social Media Today also reports Instagram has said it recommends only Reels under 3 minutes, which bears on Mara's length rule.
   - Fix: `Instagram itself announced 20-minute recording in the Reels camera in November 2025, saying it "allows for more creative freedom and longer storytelling"; Social Media Today reports that Instagram has repeatedly said it "will only recommend Reels that are under 3 minutes in length" ([Social Media Today, 23 Nov 2025](https://socialmediatoday.com/news/instagram-update-reels-camera-with-improved-functions/806247); platform statement via the press). No Instagram page stating which accounts have it was found, so the length selector in the app is the check.`
   - Basis: https://socialmediatoday.com/news/instagram-update-reels-camera-with-improved-functions/806247 ; https://petapixel.com/2025/11/25/instagram-updates-camera-so-you-can-film-20-minute-reels

3. [should-fix | accuracy] §5, The cover
   - Current: `a vendor guide states the grid now shows posts at 3:4, so a 1080 × 1920 Reel cover appears on the grid cropped to its middle (the guide's figure)`
   - Problem: Planoly gives the sizes but does not say which part of the cover the grid keeps. "Cropped to its middle" stretches the source.
   - Fix: `a vendor guide states that the grid "now displays images in a 3:4 ratio (specifically 1013x1350 pixels)" and that "your Reels cover photos are still 1080x1920, but they'll appear as 1013x1350 on your grid"; it does not say which part of the cover is kept`
   - Basis: https://www.planoly.com/blog/guide-to-instagrams-new-vertical-grid.md

4. [minor | label] §5, The cover (follows from 3)
   - Current: `so both the full cover and the grid crop carry it (her rule).`
   - Fix: `so both the full cover and the grid preview should carry it, which she checks on her profile after the first post (her rule; the guide does not say where the crop falls).`
   - Basis: as 3.

5. [minor | accuracy] §5, Length
   - Current: `and is itself inconsistent about whether that applies to recording or upload`
   - Problem: Inro describes the 20-minute option as a recording option throughout. Its summary line just says "20-minute option".
   - Fix: `and describes it as a recording option`
   - Basis: https://www.inro.social/blog/instagram-reels-length

6. [minor | accuracy] §7, thumbnails
   - Current: `"Your account must be verified to use this feature";`
   - Problem: On answer 72431 that sentence sits in the note about custom thumbnails for Shorts. The general requirement is in the page's introduction.
   - Fix: `a creator can "upload your own if your account is verified";`
   - Basis: https://support.google.com/youtube/answer/72431?hl=en

7. [minor | accuracy] §3, Socialinsider
   - Current: `labelled "under 5,000" in the method`
   - Problem: The method's words are "less than 5000". The bracket-sum point is right: 974,294 + 693,768 + 2,648,482 + 1,320,562 + 4,134,721 = 9,771,827, which is 5 more than the stated total.
   - Fix: `labelled "less than 5000" in the method`
   - Basis: https://socialinsider.io/blog/instagram-reels-statistics/

8. [minor | label] §3, What the figures support
   - Current: `and on Reels most views of brand accounts' Reels are skipped within 3 seconds (vendor, brand accounts)`
   - Problem: The source gives average skip rates by follower band (60.50%–65.50%), not a share of all views.
   - Fix: `and on Reels brand accounts' average skip rate in the first 3 seconds runs from 60.5% to 65.5% across Socialinsider's follower bands (vendor, brand accounts, averages)`
   - Basis: as 7.

9. [minor | coverage] §5, Shorts for Mara
   - Current: `which is why Mara's Reels use only her own sound (her rule).`
   - Problem: The brief asks for "the cover" under Shorts and Reels; the Shorts cover is not treated. YouTube restricts it to computers, which matters for a phone-only reader.
   - Fix: `which is why Mara's Reels use only her own sound (her rule). YouTube says "Custom thumbnails for Shorts are currently only available to add in YouTube Studio on a computer" ([YouTube Help 72431](https://support.google.com/youtube/answer/72431?hl=en), checked 12 Nov 2026; platform-official), so a reader who works only on a phone, as Mara does, cannot set one.`
   - Basis: https://support.google.com/youtube/answer/72431?hl=en

10. [minor | attribution] §9, Where the edit stops
    - Current: `The 4 hours run from copying the clips to the exported file uploaded as private (PB4, D1 C).`
    - Problem: PB4 D1 C says "hard stop at 4.0 hours; export and upload as private before the stop". It does not say the clock starts at copying the clips.
    - Fix: `The 4 hours run from copying the clips to the exported file uploaded as private (her rule for the start; PB4, D1 C sets the export and private upload before the stop).`
    - Basis: filed-units/PB4 D1 C.

11. [minor | deliverable] Deliverable A
    - Current: `**Pre: once, in the run-in (week R1, 7–13 December 2026)**`
    - Problem: The block includes the 19 December audio re-test and the 0.25 h added to R2.
    - Fix: `**Pre: once, in the run-in (weeks R1 and R2, 7–20 December 2026)**`
    - Basis: the unit's own D A lines; PB4 D2.

12. [minor | deliverable] Deliverable A, cut window
    - Current: `- [ ] Six Instagram posts, 30 minutes each, by templates C and D (PB4 §3).`
    - Problem: Templates C and D build only post 1 (reveal Reel) and post 5 (before-and-after carousel). PB4 §3's posts 2–4 and 6 are other kinds.
    - Fix: `- [ ] Six Instagram posts, 30 minutes each: the four Reels on template C's boxes and the two carousels on template D's, each with its own beats or slides (PB4 §3; her rule).`
    - Basis: filed-units/PB4 §3 table.

13. [minor | style] T-D
    - Current: `**Slides** ([number], at most 20; 4:5; text colours [from T-A]):`
    - Fix: `**Slides** ([number], at most 20; 4:5 or 3:4, every slide the same; text colours [from T-A]):`
    - Basis: as 1.

14. [minor | style] §1, opening paragraph
    - Current: `Search was off for this unit. It was used on 12 November 2026 only to re-open at its source every claim carried over from earlier material and to check specific platform limits, policies and figures; each platform rule below carries that date unless another is given.`
    - Problem: This is process language a public reader cannot interpret ("search off", then search used). The front matter also says `search: off`.
    - Fix: `Every claim carried over from earlier material was re-opened at its source on 12 November 2026, and the platform limits, policies and figures below were checked the same day; each platform rule carries that date unless another is given.`
    - Basis: the persona in the brief.

**Two edits that go with the fixes**
- **Sources (needed by fixes 1 and 2).** Current: `- Social Media Today, "Instagram adds retention insights for Reels", 24 Aug 2025. https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/`. Fix: that line, then two new lines:
  - `- Social Media Today, report on Instagram's 3:4 image support, 28 May 2025. https://www.socialmediatoday.com/news/instagram-adds-support-phone-camera-aspect-ratio-images`
  - `- Social Media Today, report on the Reels camera update, 23 Nov 2025. https://socialmediatoday.com/news/instagram-update-reels-camera-with-improved-functions/806247`

  I did not record the exact titles of these two articles, so they are described rather than quoted.
- **Unsure list (minor, style).** unit.md has no `## Unsure list` section or `Object:` line; the filed units carry both. Current: `- YouTube Help, "Video chapters" (answer 9884579), checked 12 Nov 2026. https://support.google.com/youtube/answer/9884579?hl=en`. Fix: that line, then a blank line, `## Unsure list`, the ten items of unsure.md as written (items 2 and 3 amended per findings 1–2), and `- Object: the phone on its clamp at the edge of the work table, §1`.

## Confirmed (all PASS unless stated)
- **Social Media Today, 24 Aug 2025:** the skip-rate definition quoted from Instagram, word for word; it replaces view rate "in the coming weeks". The rollout date is not given.
- **Socialinsider (24 Jun 2026, updated 6 Nov 2026):**
  - 9,771,822 Reels "from brands", 1K–1M followers, January–June 2026, organic only.
  - Skip rates 65.50% (1–5K) and 60.50% (100K–1M).
  - Reach rates 5.20 / 5.60 / 5.30 / 4.30 / 3.50% by length.
  - No per-figure sample sizes.
- **Meta Creators (17 Jun 2022):** all seven quotations (9:16, blurry video, beginning–middle–end, hook or payoff, cover photo, visibly recycled / 3rd-party fonts).
- **YouTube Help:**
  - 1722171: 16:9; the player adapts; same frame rate; AAC-LC/Opus/Eclipsa, 48 kHz, 384 kbps stereo; no loudness target.
  - 15424877: three minutes; after 15 Oct 2024 on standard channels; square or vertical; the Content ID block.
  - 9314415: Intro at 30 s, both pieces of advice, the taper sentence.
  - 12942217: typical intro about 30 s; 50% "above typical intros"; top moments earlier.
  - 12220281: Stayed to watch; engaged views; no number of seconds given.
  - 9884579: chapter rules, all four quotations.
  - 6388789: 5–20 s; at least 25 s; mobile web (iPad excepted). The page does not say whether end screens can be added from the phone.
  - 72431: 16:9; 3840 × 2160; 640 px minimum; JPG/PNG; 2 MB phone / 50 MB computer; the rejection-and-strike sentence; 30-day removal.
  - 7628154: the 2%–10% range, the wider range for new videos, the clickbait sentence.
  - 2801973: malicious-clickbait wording, the sports-match example, three strikes in 90 days.
  - 16391400: up to 3 titles and thumbnails; highest watch time; computers only; advanced features; no Shorts; insufficient impressions.
  - 6373554: the background-noise sentence, "always review", "may not be ready", long-form and Shorts.
- **Google India blog (18 Dec 2024):** the definition with breaking news and current events, "without issuing a strike", the India rollout. No search showed enforcement outside India.
- **Instagram Help Centre:** "up to 20 photos and videos", word for word.
- **Metricool (9 Aug 2024):** global rollout reported, no Instagram statement quoted.
- **Metricool sizes guide (21 Jan 2026):** quotation exact.
- **Planoly:** dated 28 Jan 2025, updated 31 Oct 2025.
- **Net Influencer (20 Jan 2025):** three minutes, up from 90 seconds; the tall grid.
- **Inro (updated 23 Jul 2026):** quotation exact; no Instagram source.
- **Instagram, Introducing Edits (22 Apr 2025):** "free for download" and "watermark-free" exact; no timeline or 4K specifications.
- **Levoy and Pritch (14 Nov 2018):** shot-noise and read-noise sentences.
- **Newman and Schwarz:** ANU records give DOI 10.1177/1075547018759345, 40(2), 246–257, 2018, and the "Despite identical content…" sentence. The experiment numbers (97 and 99 workers, 0.60 [0.41, 0.79], 0.93/0.69/0.51/0.33, 0.19, 64%) are **unverifiable in this run**: the Gwern copy was not returned by any search. The A5 fresh check (2 Nov 2026) recorded them as PASS.
- **NTIA TM-10-472 (Sep 2010):** seven authors; 78/10% and 90/3%; both caveats exact.
- **Audio-Technica:** 6 dB per doubling, "too much of the room", free field. Arithmetic: 20·log10 4 = 12.04 dB.
- **Sennheiser manual 05/2026:** the 25 cm sentence in the ME 2 and ME 4 sections.
- **RNID (16 Jun 2026):** "Transcribing audio"; "tap on the words to edit or change them"; "not available on computers, only on mobile apps".
- **W3C:** SC 1.2.2 text, intent and "meaningful sound effects"; SC 1.4.3 4.5:1, 3:1, 18 pt / 14 pt bold, the formula. I recomputed all seven contrast ratios by script (17.04, 14.12, 5.62, 4.65, 3.03, 2.25, 7.58); all match.
- **vidIQ AVD (21 Jul 2026):** the APV formula, the 40–55% band at 5–15 minutes labelled "vidIQ guidance for target bands" with no sample, both quotations.
- **Tasty Edits (Lefkowitz, 19 May 2021, updated 17 Sep 2026):** the rule of thumb and "skimming through the raw footage"; no method.
- **Arithmetic:**
  - 607.5 px, 1.78×, 1,215 × 2,160.
  - Runtime map sums to 10:00, with correct start times.
  - Edit boxes sum to 220 minutes, the clock column is right, 22 minutes per finished minute.
  - Reel 30 minutes, carousel 30, packaging 60.
  - Audio check: 7 errors in 38 words fails the 1-in-20 mark.
  - R1 4.25 h, R2 1.5 h.
  - The 8-minute version takes 0:40 from each of chapters 3, 4 and 6.
- **Filed-unit pointers:**
  - PB1: §1 labels; D2 microphone line, 150 USD cap, clamp line; D3; Y2; Y3.
  - PB2: D1 "tools that fit in one box"; D4 promise sentence.
  - PB3: D2 24.0 of 24, 8-minute cut, no Shorts hours.
  - PB4: §1 capture table, §3 posts and 30 minutes, §5, §6 piece 1, §7 fallback, D1 G, D2 dates (post 5 on Thu 14 Jan 2027).
  - Only finding 10 overstates a pointer.

## (3) Figures say whose figure they are
PASS. Every number carries its source or "her rule", "derived" or "convention" (finding 8 is a wording fix).

## (4) Labels
PASS. Vendor, correlational, manufacturer, charity guide, government lab and peer-reviewed sources are all labelled, and every her-rule is marked. No anecdote is used.

## (5) Deliverable
PASS, with fixes 11 and 12. It is present in full: checklist A, edit template B1–B3, Reel C, carousel D, blank templates T-A to T-D. It follows from §1–§10 and can be used on its own.

## (6) Errata
There is no PB5 audit report yet. The A5 fresh-check errata that touch carried-over material are all applied:
- "skimming through the raw footage" (§9).
- The frame-rate inference is labelled (§1).
- The India post's breaking-news scope is kept (§7 table).
- The box-overrun rule is coherent (B3).
- The Sennheiser windshield claim is not carried over.

Pointers to filed units are faithful, apart from finding 10.

## (7) Figures
1. **Compare, §2: PASS.** Values 0.93, 0.69, 0.51 and 0.33, plus 97 listeners and 0.60 overall, are all in the Experiment 1 bullet. The caption names §2 and the source. The kind fits.
2. **Matrix, §3: PASS.** Every cell is in the §3 text ("50%+ listed as above typical", 40–55% at 5–15 min, 65.5% for 1–5K, "initial seconds", 30 s, 3 s). The caption names §3 and all sources. A matrix fits items by attributes.
3. **Flow, §4: PASS.** The eight labels, starts and lengths match the runtime-map table. The caption names §4, PB2 D4 and answer 9884579. A sequence fits flow.
4. **Compare, Deliverable B2: PASS.** The nine values match B2. The caption names B2, her rule and Tasty Edits' 300–600 minutes (in §9). The kind fits.

## (8) The writer's notes
**Source errors list ("none"): confirmed.** Every re-opened source holds, apart from what findings 1–3 and 5–7 cover; those are new findings, not source errors.

**The four A5 omissions:**
- **12942217 (typical intro, 50% list):** real omission in A5; PB5 uses it correctly.
- **6388789 (mobile web):** real omission; used correctly.
- **15424877 (Content ID block over one minute):** real omission; used correctly.
- **16391400:** partly real. A5 already said Test & Compare picks a "title or thumbnail", so "now tests titles as well" is not an omission. Computers-only and advanced features are real omissions, and PB5 uses them correctly.

**Contradictions:**
- **1 (PB4 recording before the first tool): real.** PB4 §1 has "recording before the first tool comes out of the box" and D1 B "Phone recording before the first tool comes out". PB5's one clip per step changes that.
- **2 (PB4 D2 run-in hours): real.** PB4 D2 R1 "**3.75**" and R2 "**1.25**" do not include PB5's 0.75 h of tests.
- **3 (editing time): not a disagreement.** PB4 §2 already says the figure gives "5 to 10 hours (derived), above Mara's 4.0" and asks PB5 "to show 10 minutes in 4 hours or say what changes". PB5 does that.
- **4 (PB6 testing): a constraint on PB6's brief, not a filed-unit contradiction.** PB6 is unwritten. The constraint is real (YouTube Help 16391400).

## (9) Sourcing standard Part 5, line by line
1. Sourced where made: PASS.
2. Source types: PASS with a note. Several sources are not datasets: vendor guides (Metricool, Planoly, Inro, Tasty Edits, vidIQ bands), manufacturer pages, the RNID guide, the Google engineering blog and W3C. Each is labelled, and each is used for a product fact or as the only figure with its weakness stated.
3. Labels: PASS (finding 8).
4. Platform named: PASS.
5. Carried-over claims re-verified: PASS.
6. Private reader and course: PASS. No private name, term, unit or course appears. `kit/private_terms.py` was not available to run.
7. Mara: PASS. Every new fact is labelled and agrees with case-facts. The new facts are listed in the notes under Needs, to append.
8. Tax and law: PASS. No legal point is made; music licensing and on-camera consent are deferred to PB8 in the notes.
9. No uncited figures: PASS. The 1-in-20 mark is labelled a convention.
10. Dated changeable facts: **FAIL at two places**, §5 Length and §6 Shape (findings 1–2).
11. Deliverable built for Mara, then as a template: PASS.
12. Not advice without evidence: PASS.
13. Links given as links: PASS.

## (10) Read as the brief's reader
- §1 opening: "Search was off for this unit…" is internal process language (finding 14).
- **Unexplained terms:**
  - "lower third" (§4, B1, B2). Suggest: `It goes on screen as a lower third (a line of text across the bottom of the frame)…`.
  - "Content ID claim" (§5): no gloss; no change proposed without a sourced definition.
  - "advanced features" (§7): YouTube's term, unexplained.
  - "unlisted" and "Studio" (§2): probably known.
- A phone-only reader is told Test & Compare needs a computer, but not that a Shorts thumbnail does too (finding 9).
- No reference to the private course, its units or its reader. Every pointer is to PB1–PB4 or forward to PB6–PB8.

## The writer's unsure list
1. **Skip rate:** the Social Media Today quote is confirmed; the rollout date is "in the coming weeks"; no Instagram page was read.
2. **Reels length:** three minutes confirmed. Instagram's 20-minute recording statement was found (finding 2).
3. **4:5 and 3:4:** the vendor quotes are confirmed. An Instagram 3:4 statement was found (finding 1).
4. **Socialinsider:** confirmed as written (brand-only, the +5 sum, no per-figure samples).
5. **Caption track timing:** "may not be ready" is confirmed. Whether the phone Studio app shows the caption track was not checked.
6. **End screens from the phone:** unverifiable; answer 6388789 is silent.
7. **Clickbait enforcement outside India:** no statement found, which agrees with the unit.
8. **Newman and Schwarz:** the DOI, issue, pages and abstract are confirmed; the experiment numbers are unverifiable in this run.
9. **Phone editor for a 10-minute 4K timeline:** unverifiable; the Edits page gives no specifications.
10. **Second-slide carousel claim:** not checked; no rule in the unit depends on it.
11. **The Object line:** design/outlines/ was not in the check folder, so the illustration's licence is unverifiable.

PB5 · verdict fix · 0 error, 3 should-fix, 11 minor

**Memory:** I used nothing from memory, and nothing in this work needs saving.
