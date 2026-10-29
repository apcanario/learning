---
audit: fresh check
unit: A1 · Positioning: the journey as a format (§6 revision and the deliverable lines it changed)
course: brand-ai · A · Building a Marketable Personal Brand
model: Fable 5.1 (search on)
date: 2026-10-29
chat: own Fable 5.1 agent context, not shown the writing, in session https://claude.ai/code/session_01KMmgR2F5YQ4UzcSCsg4nzE
verdict: fix · 1 error, 1 should-fix, 3 minor (all applied the same day)
---

# Fresh check · A1 §6 revision (backlog P28 / B-1a)

Fable 5.1, 29 October 2026, method.md §5 fresh-check prompt scoped to the diff. Checker had not seen the revision written; nothing edited. Episode content checked against `audits/brand-ai/evidence/A1-episodes-2026-10-29.md` (YouTube refuses the fetch tool); other sources opened live.

## Report (verbatim)

Fresh check · A1 §6 revision (29 Oct 2026). Fable 5.1, scoped to the diff `git -C /home/claude/learning diff -- courses/brand-ai/`. Inputs: sourcing-standard.md Parts 1–2; A1 and A4 briefs (units_data.py); A6 playbook rules 1, 5, 6 (courses/brand-ai/A6-how-growth-works-per-platform.md lines 160, 164, 165); hub Frame (hub.py line 98); evidence file audits/brand-ai/evidence/A1-episodes-2026-10-29.md; fresh-check-A1.md. Live: YouTube Help 2657964 and 11585688, Barry Popik. Nothing edited.

Findings

[error] [figure] Deliverable, Override if; Current: `he would rather not put the three 2011–2013 uploads under the new name and will not hide them`; Problem: the evidence file gives the three old uploads only as "11 yr ago", "12 yr ago", "13 yr ago" on 29 Oct 2026, which is roughly 2013–2015, not 2011–2013; the year range is not in the evidence and §6 itself says "11 to 13 years ago"; Fix: `he would rather not put the three uploads from 11 to 13 years ago under the new name and will not hide them`; Basis: audits/brand-ai/evidence/A1-episodes-2026-10-29.md, Channel, Videos tab line (read 29 Oct 2026)

[should-fix] [attribution] Sources; Current: `- YouTube, Mike Boyd About page, read 28 Oct 2026. https://www.youtube.com/@MikeBoyd/about`; Problem: §6 now cites the channel page and the two watch pages by URL, and the Sources list carries none of them (Part 1: every source cited is listed); Fix: `- YouTube, Mike Boyd About page, read 28 Oct 2026. https://www.youtube.com/@MikeBoyd/about
- YouTube, Pedro Canário channel (@apcanario), read in Chrome 29 Oct 2026. https://www.youtube.com/@apcanario
- YouTube, "Sometimes You Win, Sometimes You Learn To Lose | Karate Vlog: Road to WIKF Global Cup 2026, Ep. 1", 11 Oct 2026, read in Chrome 29 Oct 2026 (auto-generated captions). https://www.youtube.com/watch?v=ZzUAtWkMoWo
- YouTube, "Being a Better Athlete Made Me a Worse Person | Karate Vlog: Road to WIKF Global Cup 2026, Ep. 2", 13 Oct 2026, read in Chrome 29 Oct 2026 (auto-generated captions). https://www.youtube.com/watch?v=o5fitxW62Ng`; Basis: sourcing-standard.md Part 1, per unit, third item; unit §6 lines 128, 132, 137

[minor] [accuracy] §6, Episode 1, Expresses bullet; Current: `The constraint the expansion names (a full-time job and the people carrying the cost) is in the description.`; Problem: episode 1's description says "a job, a partner, a family" and "juggle a career"; "full-time job" and "the people carrying you" are episode 2's description; Fix: `The constraint the expansion names (the job and the people it costs) is in the description: "a job, a partner, a family".`; Basis: evidence file, Episode 1 description, paragraph 2; Episode 2 description, paragraph 1

[minor] [label] §6, Episode 2; Current: `He sets himself against the "David Goggins mentality" of pushing through regardless`; Problem: the quoted words are not the caption's exact text, which reads "that David Gogggins mentality" (machine spelling); Fix: `He sets himself against what he calls the David Goggins mentality (the captions spell it "Gogggins") of pushing through regardless`; Basis: evidence file, Episode 2 captions, 2:33–2:41

[minor] [style] §6, Episode 1, Contradicts bullet; Current: `("karate vlog", "WIKF Global Cup")`; Problem: quotation marks carry the title's words in different case; the title reads "Karate Vlog"; Fix: `("Karate Vlog", "WIKF Global Cup")`; Basis: evidence file, Episode 1 title

Confirmed:
- Coverage: brief item 6 (how the two episodes express or contradict the positioning) is now covered: both episodes analysed from content, each with an expresses/contradicts pair, a read-together verdict against §1 and §2, and a metadata action for the two already out — brief in generator/data/brand-ai/units_data.py
- Channel "Pedro Canário", @apcanario, About "Documenting sports and creative endeavours as I go!", 17 subscribers · 11 videos (owner view), five long-form videos (two episodes + three at 11/12/13 yr), two public playlists neither a series — evidence file, Channel (29 Oct 2026); figures labelled YouTube's own, owner view
- Episode 1 title verbatim; brief's title differs; "nobody tells you how much the learning part sucks" verbatim in description — evidence file, Episode 1
- Episode 1: 11 Oct 2026, 4:06 (246 s); "First tournament back after 17 years"; "Last one I was 17. Now I'm 34."; "get the rust out" (0:30); "My mind was there. My body was not responding." (2:14); liked being out there, not what he was doing (2:30–2:38); "practicing like crazy for the last half a year" (3:04); pride in "who I became and the work" not "what I did today" (3:45–3:53); description: job, partner, family, "came back to the sport two years ago", "If you're 30–45 and chasing something late" verbatim; opens at 7:00 a.m. leaving the house (0:02) — evidence file
- Episode 2 title verbatim; 13 Oct 2026, 5:54 (354 s); description "10 days out from the WIKF Global Cup in Athens", "Recorded the day before flying to Poland for the WKF Cadet, Junior & U21 World Championships", "the ending isn't the one I planned", "Not the Goggins version" verbatim; captions: snapped yesterday (0:46), "I've done it many times, more so recently" (1:20), better physically / worse emotionally, "Which one matters most?" "I don't have the answer" (1:43–1:55), rest of the week is resting (4:14), death with no warning of someone he promised to visit (5:03–5:46) — evidence file
- Both titles carry series name, sport, event, episode number; descriptions give Instagram @apcanario — evidence file
- Barry Popik: earliest item a tweet of 10 Sep 2007 (Brandi Jasmine); Maxwell's book 2013 — https://barrypopik.com/blog/sometimes_you_win_sometimes_you_learn
- "You can change your channel name twice within a 14-day period."; "Changing your name will remove your verification badge." — https://support.google.com/youtube/answer/2657964?hl=en
- Handles "are distinct from channel names." verbatim — https://support.google.com/youtube/answer/11585688?hl=en
- YouTube description block: 794 characters, line breaks included, fences and leading/trailing newlines excluded (counted by script); Instagram bio 121 — courses/brand-ai/A1 deliverable
- Decision format: Pick line; three reasons of 9, 9 and 8 words; one Override if line; Before-renaming line follows from the evidence (three old uploads outside the format, rename rules cited) — unit lines 166–173
- Labels: "his rules from this, untested" and "That is his rule from YouTube's series tip, untested" mark the two recommendations; the stranger's sentence is framed as inference ("a stranger would say"); figures carry "YouTube's" / "owner view" — unit §6
- Pointers: §1 one-sentence test (line 22); §2 method-holds-across-topic (lines 27, 46); §3 four fixed elements and stage numbers (syllabus 2, artefact 5; season label in title, playlist, first ten seconds; the miss named is the third element) (lines 54–65); A4 brief = disclosure policy with pre-mortem; A6 rule 1 (search-shaped words a stranger would type), rule 5 (keep every published episode public), rule 6 (one format per season; series from episodes that worked) — A6 lines 160, 164, 165
- Nothing in the new text contradicts unchanged parts: §4's "display name can be changed later" and option 3 analysis stand; the pick keeps the handle, consistent with §4's handle-is-scarce point; unsure items 1–2 updated to match
- Private material: every personal fact in the new text (name, age 34, job, partner, family, snapping, the bereavement) is in the episodes' own public titles, descriptions or captions; nothing beyond them; the public channel description adds only "Road to WIKF Global Cup 2026" and "Athens", both from the descriptions — hub Frame rule not engaged
- No third-party quotation over 15 words in the changed text

A1 (§6 revision), verdict fix: 1 error, 1 should-fix, 3 minor.
