---
audit: fresh check
unit: A5 · Production craft
course: brand-ai · A · Building a Marketable Personal Brand
model: Opus 5.5 (search on; a Fable 5.1 fresh check is owed, deferred by Pedro 31 Oct 2026 to the Fable stage)
date: 2026-11-02
chat: own Opus 5.5 agent context, not shown the writing (P31), in session https://claude.ai/code/session_01KMmgR2UTDUnjTFpyKbqrjA (backlog row A-1)
verdict: fix · 1 error, 4 should-fix, 8 minor
---

# Fresh check · A5 · Production craft

The checker's final report, verbatim.

A Fable 5.1 fresh check of A5 is still owed: Pedro deferred Fable 5.1 checks to a later stage on 31 Oct 2026. This check is the interim one, run by Opus 5.5 in its own agent context (P31). The checker did not see A5 being written.

A5 · Production craft. Fresh check, Opus 5.5, 2 Nov 2026, with live search. Read: the unit in full, sourcing-standard.md Parts 1 and 2, the A5 brief in generator/data/brand-ai/units_data.py, audits/brand-ai/audit-1.html and audit-2.md, and the filed units A1, A2, A3, A4, A6, A9, B3 and B5 where A5 points to them. kit/viz.py check_keys and render pass on all four figures.

Web-rule disclosure: I fetched one URL that no search had returned, https://www.sciencedaily.com/releases/2018/04/180413093842.htm. It is printed in the unit, so it counts as typed. That fetch breaks the rule, and I have not used its result. The Newman quotation is confirmed instead on ANU's own release, which a search did return. Every other fetch was of a URL that a search in this agent returned first.

(1) Coverage. Every item the brief names is covered:
- Filming inside a session, with the phone on a tripod, one lav and the six-shot b-roll list.
- "Audio as the thing viewers forgive least": treated as an unsourced comparison, with the study in each direction set out.
- The vidIQ/AIR CTR 4–6% and APV 30–45% figures: both checked at source and the misattribution shown.
- Structure: the brief's 20 s hook is replaced by YouTube's measured 30 s, with the reason given; chapters every 2–3 min are kept as his convention; the ending has no wind-down.
- Thumbnails in the Shōmen styles, and the three clickbait statements with the titles they exclude.
- The workflow for a 12-minute episode in under 4 hours.
- Deliverable: a pre/during/post checklist and an edit template with timings.
Nothing is missing. Nothing is thin.

(2)–(7) Findings

[error | accuracy] §5, Four levers, item 1; Current: `which starts from "reviewing raw footage".`; Problem: The quoted words are not on the Tasty Edits page. Neither "reviewing" nor "review" occurs there. The page says editing time "includes everything from skimming through the raw footage to rendering the final product". Words in quotation marks must be the source's exact words (Part 1). Fix: `which starts from "skimming through the raw footage".`; Basis: Tasty Edits, last updated 17 Sep 2026, https://www.tastyedits.com/how-long-does-it-take-to-edit-a-video/

[should-fix | accuracy] §1, Wind, on runs; Current: `The same Sennheiser manual tells the user to slide the windshield over the microphone head for its outdoor lavaliers, and says its MZC 1-2 cap "attenuares [sic] wind noise by approx. 15 dB" ([Sennheiser, 05/2026](https://docs.cloud.sennheiser.com/en-us/lavalier-mics/lavalier-mics_instruction_manual_05_2026_en.pdf)). That figure is for one product. The general point the manual supports is that an outdoor lav needs a windshield; how much a given shield removes depends on the shield.`; Problem: The manual never uses the words "outdoor", "outside" or "windscreen". "Slide the windshield over the microphone head" appears in the ME 4, MKE Essential, MKE 2 and MKE 40 sections and gives no condition for use. The MZC 1-2 wind figure is in the MKE 1 section. So the manual does not say an outdoor lav needs a windshield; that is a stretch of the source. Fix: `The same Sennheiser manual tells the user of the models it supplies with a windshield (ME 4, MKE Essential, MKE 2, MKE 40) to "Slide the windshield over the microphone head", and says its MZC 1-2 cap for the MKE 1 "attenuares [sic] wind noise by approx. 15 dB" ([Sennheiser, 05/2026](https://docs.cloud.sennheiser.com/en-us/lavalier-mics/lavalier-mics_instruction_manual_05_2026_en.pdf)). That figure is for one product, and the manual does not say when either is needed. That a lav on a run needs a windshield is my inference from that figure; how much a given shield removes depends on the shield.`; Basis: Sennheiser, Lavalier microphones, instruction manual v1.1, 05/2026, https://docs.cloud.sennheiser.com/en-us/lavalier-mics/lavalier-mics_instruction_manual_05_2026_en.pdf

[should-fix | accuracy] §4, Titles the rule excludes, last paragraph; Current: `Both published titles meet that test (A1 §6).`; Problem: The pointer claims more than A1 §6 says. A1 §6 never tests either title against "true of the first 30 seconds" or "says what happened in the fortnight". It reads episode 2 as "a question, not a step in a journey", and it records that episode 1's opening is leaving the house at 7 a.m. Only the length holds: by script count, the titles A1 §6 records are 97 and 96 characters with their suffix. Fix: `Both published titles, with their series suffix, are under 100 characters (97 and 96, counted by script from the titles A1 §6 records); whether each is true of its first 30 seconds, A1 §6 does not say.`; Basis: courses/brand-ai/A1-positioning-the-journey-as-a-format.md §6.

[should-fix | deliverable] Deliverable B4; Current: `- A box overruns: the next box starts on time and loses what it cannot fit; box 8 is the only one that drops work. **(his rule;** basis A3 §6, the hard stop**)**`; Problem: The rule contradicts itself. If each overrun is taken from the next box, any box can lose work, so box 8 cannot be "the only one that drops work". A reader cannot run it as written. Fix: `- A box overruns: the next box still starts and runs its full length; the overrun comes out of box 8, the only box that drops work (the fixes at the bottom of its list), and then out of the 75-minute margin before A3's five-hour stop. **(his rule;** basis A3 §6, the hard stop**)**`; Basis: the unit's own B2 table (box 8: "what does not fit in 15 minutes is dropped") and its B2 arithmetic (75 minutes of margin).

[should-fix | accuracy] §5, How the template meets A3's window; Current: `If edits run over, A2's cut order applies before anything else moves: the episode shortens to about 8 minutes (A2, Deliverable 2; A3, Deliverable 1, G).`; Problem: This misstates the filed units. A2's cut order has four steps, and shortening the episode is the last of them. A3 G says to cut in this order: "Instagram to zero; skip the Short; the off-week email becomes three lines; the episode shortens to about 8 minutes, editing about 4 hours". A3 §6 likewise says the next fortnight "takes A2's cut order before anything else moves". Fix: `If edits run over, A2's cut order applies before anything else moves: Instagram to zero, then the Short, then the off-week email to three lines, and last the episode, shortened to about 8 minutes with about 4 hours of editing (A2, Deliverable 2; A3, Deliverable 1, G).`; Basis: A2 Deliverable 2, cut 4 ("The episode is shortened to about 8 minutes, editing about 4 h"); A3 Deliverable 1, G.

[minor | label] Deliverable B4; Current: `- Three edits in a quarter over five hours: the next episode is planned at about 8 minutes, A2's fourth cut (A2, Deliverable 2).`; Problem: Going straight to the fourth cut skips the order that A2 and A3 set, so it is his rule, not A2's, and needs the label. Fix: `- Three edits in a quarter over five hours: the next episode is planned at about 8 minutes, A2's fourth cut, taken directly because the first three cuts free no editing time (A2, Deliverable 2). **(his rule** for skipping to it**)**`; Basis: A2 Deliverable 2; A3 Deliverable 1, G.

[minor | style] Opening paragraph; Current: `five YouTube Help pages (impressions and clickbait`; Problem: The parenthesis lists seven pages: impressions and clickbait, audience retention, Content tab tips, chapters, thumbnails, upload encoding and automatic captions. Fix: `seven YouTube Help pages (impressions and clickbait`; Basis: the unit's own list and its Sources (7628154, 9314415, 12942217, 9884579, 72431, 1722171, 6373554).

[minor | accuracy] §4, YouTube's three statements on clickbait, row 3; Current: `examples include a title announcing a resignation the video does not address`; Problem: The quoted definition is cut short. The post's sentence goes on to say the problem is especially concerning for breaking news and current events, which is where enforcement starts. The row drops that scope. Fix: `the post singles out breaking news and current events; examples include a title announcing a resignation the video does not address`; Basis: Google India blog (The YouTube Team), 18 Dec 2024, https://blog.google/intl/en-in/products/platforms/strengthening-enforcement-against-egregious-clickbait-on-youtube/

[minor | accuracy] §2, Levels and export, Loudness; Current: `TD1008 is written for internet audio streaming and on-demand audio; using it as the mix target for a YouTube episode is my transfer.`; Problem: Shepherd's report says TD1008 is written "exclusively for online radio stations and streaming services like YouTube, Spotify and TIDAL". The source therefore names YouTube. The real transfer is from a distribution level to a mix target. Fix: `Shepherd's report says TD1008 is written for online radio and streaming services, YouTube among them; it gives distribution levels, and using −18 LUFS as the mix target for an episode is my transfer.`; Basis: Production Advice, 1 Oct 2021, https://productionadvice.co.uk/td1008/

[minor | coverage] §3, Chapters; Current: `because a 12-minute episode with A1 §3's fixed elements falls naturally into five or six parts`; Problem: This disagrees with the unit's own template, B1, which sets seven chapters: two of 30 s, four of 2:30 and one of 1:00. Fix: `because a 12-minute episode with A1 §3's fixed elements falls into seven parts: two 30-second openers, four parts of about 2.5 minutes and a one-minute ending (Deliverable B1)`; Basis: the unit's Deliverable B1 table and its check line.

[minor | label] §3, End on the last line; Current: `No recap, no subscribe request (A6 rule 8; B5 rules for every step).`; Problem: A6 rule 8 and B5's rules forbid subscribe appeals. Neither says anything about a recap, so "no recap" is his rule and needs the label. Fix: `No subscribe request (A6 rule 8; B5 rules for every step); no recap (his rule).`; Basis: A6 Deliverable 1, YouTube rule 8; B5 skill, "Rules for every step".

[minor | label] §1, Frame rate; Current: `Mixing frame rates across a season's clips forces a conversion somewhere.`; Problem: This mechanism claim has no source and no label. YouTube's page says only to upload at the recorded rate. Fix: `Mixing frame rates across a season's clips forces a conversion somewhere (my inference: an edit exports at one rate).`; Basis: YouTube Help 1722171, https://support.google.com/youtube/answer/1722171?hl=en

[minor | label] Deliverable A, Before every session; Current: `- [ ] Lav clipped about 25 cm from the mouth; windshield on outdoors (Sennheiser manual, 05/2026; Audio-Technica, inverse square).`; Problem: The windshield-outdoors rule rests on an inference, as set out in the §1 finding above. Neither source says it. Fix: `- [ ] Lav clipped about 25 cm from the mouth (Sennheiser manual, 05/2026; Audio-Technica, inverse square); windshield on outdoors **(his rule;** basis the Sennheiser MZC 1-2 wind figure, §1**)**.`; Basis: Sennheiser manual v1.1, 05/2026 (as above).

Figures (7)
1. Figure 1 is a compare in §2: PASS. Every label and value (0.93, 0.69, 0.51, 0.33) and the caption's 97 listeners and 0.60 overall are in the Experiment 1 bullet. The caption names §2 and Newman and Schwarz, with a link. Compare fits the shape.
2. Figure 2 is a range in §3: PASS. The four bands (50–70, 40–55, 30–45, 25–35), "his episode" and "the brief's band" are all in §3's text. The caption names §3 and vidIQ, 21 Jul 2026, and says it is vendor guidance with no sample. Range fits, since the data are intervals by category.
3. Figure 3 is a compare in §4: PASS. The values 11.08, 9.19, 5.70, 4.72 and 1.94 are in §4's Contrast paragraph, and I recomputed each with the WCAG formula and got the same figure. The caption names §4, B3 and W3C. Compare fits.
4. Figure 4 is a compare in Deliverable B2: PASS. The nine values (15, 30, 35, 40, 25, 25, 20, 15, 20) match the B2 table and sum to 225. The caption names Deliverable B2, A3 §6 and A9 read 2, and labels the times as his rule. Compare fits.

(6) Errata. Audit 1 sets three things, and A5 applies all three in §3:
- The 4–6% CTR target is unsourced and not used.
- The 30–45% APV band applies only to videos of 15–30 minutes.
- The 2–10% CTR range is cited to YouTube Help 7628154.
Audit 2's errata (B2-1 to B2-25 and A1-1) do not touch A5. The pointers are faithful apart from the two flagged above (A1 §6 titles; A2/A3 cut order).

Confirmed
- AIR Media-Tech (Prokopchuk, updated 5 Nov 2024): "most YouTube creators aim for a CTR between 2% and 10%", the below-2% line, "Aim for that sweet spot of 4% to 10%", no dataset, no retention benchmark, and no 4–6% anywhere. PASS. https://air.io/en/trending/what-is-a-good-ctr-on-youtube
- vidIQ CTR page (updated 27 May 2026): "A good CTR typically falls between 2–10%"; size bands from 8–20% under 1k down to 1.5–4% at 1M+; "patterns we see across vidIQ's user base, generally"; no sample; no 4–6%. PASS. https://vidiq.com/blog/post/6-tips-good-CTR-youtube
- vidIQ AVD page (updated and reviewed 21 Jul 2026): the "vidIQ guidance for target bands" with all four bands; the 3:11, 30.3% and 16.5M views from June 2025 to June 2026; the "Confirm the title and thumbnail promise immediately…" quotation; the "Use an end screen and a clear verbal bridge…" quotation. PASS. https://vidiq.com/blog/post/average-view-duration/
- YouTube Help 7628154: the "Half of all channels…2% and 10%" sentence, the wider range for new videos and those under 100 views, the clickbait sentence verbatim (including "and lower than expected Impressions"), and no target figure. PASS. https://support.google.com/youtube/answer/7628154?hl=en-GB
- Newman and Schwarz, Science Communication 40(2), 246–257, 2018: Exp. 1 had 97 MTurk workers, physics and engineering talks cut to 2–3 min, an echo ("Large Room") filter, an overall difference of .60 [.41, .79], and per-measure differences of .93, .69, .51 and .33; Exp. 2 had 99 workers, Science Friday interviews and a bad phone line, difference .19 [.03, .36]; 64% answered both comprehension checks, with the same pattern; the "Despite identical content…" quotation is exact. PASS. https://www.Gwern.net/doc/design/visualization/2018-newman.pdf; DOI and abstract also on https://openresearch-repository.anu.edu.au/items/67350c38-062b-4837-84c9-81419829d59d
- Newman quotation "it's not just about who you are and what you are saying, it's about how your work is presented": PASS, on ANU's release dated 12 Apr 2018 (https://science.anu.edu.au/news-events/news/what-makes-someone-believe-or-reject-information). ScienceDaily's 13 Apr 2018 date is unverifiable (not checked); see the disclosure above.
- McFarland et al., NTIA TM-10-472, Sep 2010: the seven authors; 78% versus 10% of variance, and 90% versus 3% for speech-only clips; "quite easy to code", "nearly identical", "it is unclear whether this indicates underlying truth, or was merely a consequence of the unbalanced test design", and "will not necessarily be valid for other choices of audiovisual material". PASS. https://its.ntia.gov/publications/download/10-472.pdf
- YouTube Help 1722171: "Content should be encoded and uploaded in the same frame rate it was recorded"; AAC-LC or Opus (Eclipsa Audio also listed); stereo; 48 kHz; 384 kbps stereo. PASS. https://support.google.com/youtube/answer/1722171?hl=en
- Sennheiser manual v1.1, 05/2026: "Attach the microphone to your clothing, keeping a distance of 25 cm (10") from your mouth" (ME 2, ME 4) and the "attenuares … 15 dB" quotation are exact. PASS, with the outdoor reading flagged above. https://docs.cloud.sennheiser.com/en-us/lavalier-mics/lavalier-mics_instruction_manual_05_2026_en.pdf
- Audio-Technica (undated): the 6 dB per doubling quotation, the "inverse square law … in a free field" wording, and "may pick up too much of the room". PASS. The 21.6 dB is right: 20·log10(12) = 21.58. https://www.audio-technica.com/en-us/support/audio-solutions-question-week-tips-placing-microphones-get-best-possible-sound
- YouTube Help 6373554: the background-noise sentence, "You should always review automatic captions", and Portuguese among the supported languages. PASS. https://support.google.com/youtube/answer/6373554?hl=en-GB
- Production Advice, 1 Oct 2021: −18 LUFS for speech-only and "Assorted" content, and no true-peak figure. PASS. The page's byline is blank, but the site is Ian Shepherd's. https://productionadvice.co.uk/td1008/
- YouTube Help 9314415: the Intro definition (30 s), "Modify the first 30 seconds…", "Consider changing your video thumbnail and title…", and "Videos on YouTube generally taper off during the playback period". PASS. https://support.google.com/youtube/answer/9314415
- YouTube Help 12942217: the "If your top moments happen later in your video…" quotation. PASS. https://support.google.com/youtube/answer/12942217?hl=en
- YouTube Help 9884579: first timestamp at 00:00, at least three timestamps in ascending order, a 10 s minimum, and the "add info and context…" line. PASS. https://support.google.com/youtube/answer/9884579?hl=en
- YouTube Help 72431: 16:9; JPG or PNG; 3840 × 2160; a 640 px minimum width; 2 MB on mobile and 50 MB on desktop; a verified account; Community Guidelines, with rejection and a strike. PASS. https://support.google.com/youtube/answer/72431?hl=en-GB
- YouTube Help 2801973: "Using maliciously misleading titles, thumbnails, descriptions or imagery to trick users into clicking on a video", "does not deliver what was promised", the full sports match / only a clip example, warning or strike for some violations, and three strikes in 90 days. PASS. https://support.google.com/youtube/answer/2801973?hl=en-GB
- Google India blog, 18 Dec 2024: the definition, the resignation example, "without issuing a strike", "slowly rolling this out in India over the coming months", and new uploads first. PASS, with the scope noted above. https://blog.google/intl/en-in/products/platforms/strengthening-enforcement-against-egregious-clickbait-on-youtube/
- W3C Understanding SC 1.4.3: 4.5:1, 3:1 for large text, 18 pt or 14 pt bold, and (L1 + 0.05)/(L2 + 0.05). PASS. All five contrast ratios recomputed and matched. https://w3.org/WAI/WCAG20/Understanding/contrast-minimum
- Adobe Help, text-based editing: "edit a transcript and view the corresponding changes in the visuals", undated, with no languages listed. PASS. https://helpx.adobe.com/premiere-pro/using/video/text-based-editing-video.html
- Blackmagic via Silicon UK, 4 Apr 2025: "AI IntelliScript to create timelines based on a text script", "will match the transcribed audio in media clips to the script", a subtitle track from transcription, voice isolation and dialogue leveling, and the public beta. PASS. https://www.silicon.co.uk/press-release/blackmagic-design-announces-davinci-resolve-20
- Tasty Edits, updated 17 Sep 2026: "As a rule of thumb, expect 30 minutes to an hour of editing time per minute of finished video", with no method stated. PASS. https://www.tastyedits.com/how-long-does-it-take-to-edit-a-video/
- Arithmetic, all PASS:
  - 607.5 px crop, about 32% of the frame width, 1.78× enlargement, and 1,215 × 2,160 from 4K.
  - B2 boxes: 225 min, the running clock column, 18.75 min per finished minute, and 75 min of margin.
  - B1 chapters: 12:00 and 10:00 runtimes, and the end screen at 11:40–12:00.
  - Under 4 h for 12 min is under 20 min per finished minute, a third below 30.
  - 4.8–6.6 min average view duration at 12 min.
- Pointers, all PASS:
  - A3 §1: "nothing is filmed twice", the staged-version quotation, centre third, YouTube Help 15424877.
  - A3 §2: 10 min, 12 at most, and the "until A5's editing workflow…" quotation.
  - A3 §6: "Capture is in the session, never a separate job", the five-hour hard stop, and 1.0 h a fortnight for capture.
  - A3 Deliverable 1 B, D, E. A3 §5 (end screens, via 6388789).
  - A4 clauses 2, 3, 5, 7 and record rule 4. A4's publish list (distance, duration, pace, race result, weekly running volume, weight change).
  - A6 §1.2 (Test & Compare on watch time; the 4–6% target not used). A6 playbook YouTube 2, 3, 8. A6 metrics sheet rows Y1–Y4.
  - A9 §2 and row 3. A9 §6's 4.8–6.6 min. A9 Deliverable 2 (CTR below 2% on three or more uploads; Studio read on fixed dates; read 2).
  - A2 §6 (Tasty Edits, 5 h plan).
  - B3 templates 5 and 6 (Tomorrow, #FF2A50 and #54C8FF on near-black, the Swiss-grid and HUD/glitch lines, "<UNKNOWN: word limit; A5 covers thumbnails>", the avoid list) and template 8's worked example (a training partner's consent to appear).
  - B5 steps 1, 4 ("Ending: the last line, from the takes"), 5 (100 characters; "time, weight or result the script does not state") and 6 (crop check), and the rules for every step (no subscribe request).
  - A8's brief covers training partners' image rights.
- Labels: the vendor sources (AIR, vidIQ, Tasty Edits, Blackmagic), the manufacturer sources (Sennheiser, Audio-Technica), the peer-reviewed study, the government lab report, and every "his rule" or "my arithmetic" is labelled. No correlational or anecdotal data is used. The Sources list matches the citations.
- Deliverable: present in full (checklist A pre/during/post; template B1–B4). It follows from §1–§5 and can be used on its own. Apart from the edits above, it adds no unsourced claim without a label.

A5 · verdict: fix. 1 error, 4 should-fix, 8 minor.
