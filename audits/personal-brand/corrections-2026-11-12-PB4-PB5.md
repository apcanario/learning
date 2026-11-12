---
audit: correction check (docs/public-courses.md §3 rule 12; step 7b of row W-PB7)
units: PB5 (C1, flag F41), PB4 (C3, flag F32)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; no agent transcript on disk; live search)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB7/W-PB8 chat in session https://claude.ai/code/session_01KMmgQyAmFapUaWMYDKogYn
verdict: C1 PASS, C3 PASS, no syllabus conflict; nothing new to correct
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/report.md`), copied unchanged. Saved before any change was applied. The exact strings it applied are in its `edits.json`, each checked by script to appear verbatim in this report.

Model: claude-opus-5-5

# Correction check, W-PB7 corrections C1 (PB5) and C3 (PB4), 12 Nov 2026

Every Current string was checked with Python `str.count` against the filed unit: each occurs exactly once, also after the earlier edits in this report are applied in order (script `out/check.py`, strings in `out/edits.json`). All three sources were found by WebSearch and fetched from the URL the search returned; none refused.

## C1 · PB5 §6, the carousel second-slide claim (flag F41)

Location: PB5 §6 "Carousels", paragraph **The first slide.** (line 201). PB5 currently says only that no Instagram statement was found; it does not mention the two press reports, so a change is needed.

### 1–2. Change C1a (§6)

Current (count 1 in the filed file):

```
no Instagram statement of it was found on 12 November 2026, so no rule here depends on it.
```

Replacement:

```
no Instagram statement of it was found on 12 November 2026. Two press reports say it does, neither quoting Instagram: Lia Haberman summarises a 2024 Mosseri post as saying the algorithm gives a carousel "a second chance after it's posted, resurfacing it to followers who previously swiped by" ([ICYMI, 14 Oct 2025](https://liahaberman.substack.com/p/the-best-instagram-content-formats); her summary, not his words), and Uppbeat paraphrases an undated Mosseri interview with Colin and Samir as saying a carousel scrolled past "may come back around with the second slide showing" ([Uppbeat, 3 Nov 2026](https://uppbeat.io/blog/creator-news/whats-working-on-instagram-right-now-carousels-and-sends-says-adam-mosseri); a paraphrase, not a quotation). No rule here depends on it.
```

### 3. Against the sources: PASS

- Haberman, ICYMI, 14 Oct 2025 (https://liahaberman.substack.com/p/the-best-instagram-content-formats): introduced with "Last year, Adam Mosseri attributed Carousel's success to:", then "the algorithm gives your Carousel a second chance after it's posted, resurfacing it to followers who previously swiped by". No quotation marks and no original Mosseri wording on the page, so a summary, not a quotation. Post dated 14 Oct 2025, so "last year" is 2024.
- Uppbeat, 3 Nov 2026 (https://uppbeat.io/blog/creator-news/whats-working-on-instagram-right-now-carousels-and-sends-says-adam-mosseri): reported speech, "He told Colin and Samir that" a scrolled-past carousel "may come back around with the second slide showing". The interview is not dated (it is called his "latest conversation" with them). The only direct Mosseri quotes in the paragraph are about the format's depth, not about the resurfacing.
- Neither source quotes Instagram on the resurfacing. The Replacement labels both as reports and states that neither quotes Instagram.

### 1–2. Change C1b (PB5 Unsure list, same claim)

The Unsure line says the claim's "origin was not traced". After C1a that is out of date. The correction covers "PB5's sentence(s) on this claim", so this line is in its scope. It adds no source beyond C1's two.

Current (count 1 in the filed file):

```
- The claim that Instagram re-shows an unengaged carousel from its second slide was searched once; no Instagram statement was found and its origin was not traced (§6).
```

Replacement:

```
- The claim that Instagram re-shows an unengaged carousel from its second slide: no Instagram statement was found; it rests on Haberman's summary of a 2024 Mosseri post (ICYMI, 14 Oct 2025) and Uppbeat's paraphrase of an undated Mosseri interview (3 Nov 2026), and neither underlying statement was read (§6).
```

### 4. Syllabus: no conflict

The PB5 brief ("carousels (the slide limit as Instagram states it, dated; the first slide; the order)") is still met. No PB5 rule, template or Mara fact depends on the claim: D's first-slide test and the eight-slide shape stay as they are. The register says nothing on it. F41's carry ("Later units do not state them, or label them unsourced") still holds, because the claim stays labelled as unconfirmed by Instagram. The text matches PB7 §10 item 7 and PB7's Unsure line. No later brief (PB8–PB10, DD-PB1, DD-PB2) relies on it.

### 5. Dated note (after PB5's last note, the F36 note by the P99 correction check, before `## Sources`)

Current (count 1 in the filed file):

```
since PB4 now carries this unit's one clip per step (flag F36).

```

Replacement:

```
since PB4 now carries this unit's one clip per step (flag F36).

Correction 12 Nov 2026, found by PB7's writer: §6 now says that two press reports, Haberman's summary of a 2024 Mosseri post (ICYMI, 14 Oct 2025) and Uppbeat's paraphrase of an undated Mosseri interview (3 Nov 2026), say Instagram re-shows an unengaged carousel from its second slide, neither quoting Instagram, where it said only that no Instagram statement was found; the Unsure list line follows; no rule changes (flag F41).

```

If C1b is not applied, drop "; the Unsure list line follows" from the note.

### 6. Sources entries (both sources are new to PB5)

The list is alphabetical, publication first, with the author in brackets (as in "Tasty Edits (Alex Lefkowitz)"). "ICYMI" sorts after "Google India blog" and before "Inro".

Current (count 1 in the filed file):

```
- Inro, "How long can Instagram Reels be?"
```

Replacement:

```
- ICYMI (Lia Haberman), "The best Instagram content formats", 14 Oct 2025. https://liahaberman.substack.com/p/the-best-instagram-content-formats
- Inro, "How long can Instagram Reels be?"
```

"Uppbeat" sorts after "Tasty Edits" and before "vidIQ":

Current (count 1 in the filed file):

```
updated 17 Sep 2026. https://www.tastyedits.com/how-long-does-it-take-to-edit-a-video/
- vidIQ,
```

Replacement:

```
updated 17 Sep 2026. https://www.tastyedits.com/how-long-does-it-take-to-edit-a-video/
- Uppbeat, "What's working on Instagram right now? Carousels and sends, says Adam Mosseri", 3 Nov 2026. https://uppbeat.io/blog/creator-news/whats-working-on-instagram-right-now-carousels-and-sends-says-adam-mosseri
- vidIQ,
```


## C3 · PB4 §3, who may schedule on Instagram (flag F32)

Location: PB4 §3, paragraph **Scheduling.** (line 101). It cites only TechCrunch 2022 ("all professional accounts", 75 days) and the unreadable Help Centre page, so a change is needed.

### 1–2. Change

Current (count 1 in the filed file):

```
([TechCrunch, 8 Nov 2022](https://techcrunch.com/2022/11/08/instagram-scheduling-tool-all-professional-accounts)). Instagram's help page
```

Replacement:

```
([TechCrunch, 8 Nov 2022](https://techcrunch.com/2022/11/08/instagram-scheduling-tool-all-professional-accounts)). Social Media Today reported on 1 March 2026 that Instagram had made content scheduling, with the insights dashboard and trending audio, "available to all public accounts" ([Social Media Today, 1 Mar 2026](https://www.socialmediatoday.com/news/instagram-opens-up-content-scheduling-to-all-users/813448/); press report, quoting no Instagram statement); it gives no scheduling horizon. Instagram's help page
```

The rest of the paragraph is unchanged: "so the current limit is unconfirmed" and "Mara schedules at most 13 days ahead…" stay.

### 3. Against the source: PASS

Social Media Today, 1 Mar 2026 (https://www.socialmediatoday.com/news/instagram-opens-up-content-scheduling-to-all-users/813448/): creator tools are "available to all public accounts in the app", naming the insights dashboard, content scheduling and trending audio. It contains no direct quotation from Instagram and does not say how many days ahead posts can be scheduled. So the Replacement's "quoting no Instagram statement" and "no scheduling horizon" are right. The article adds that some options stay tied to Professional Mode or to follower thresholds; the Replacement does not use that.

### 4. Syllabus: no conflict

The PB4 brief does not name scheduling. The register's facts (the six posts scheduled in the 0.5-hour slot of the cut window, posts out Tue/Thu/Sat, the provisional mix) are unchanged, and the 13-day rule stands. PB4's Unsure line on the 75-day limit (line 419) is still accurate and needs no change. The text matches PB7 §4 and PB7's Unsure line ("does not quote Instagram; the scheduling horizon … remains unconfirmed"). No later brief relies on who may schedule. PB9's "professional dashboard" concerns revenue eligibility, not scheduling.

### 5. Dated note (after PB4's last note, the F37 note by PB5's writer, before `## Sources`)

Current (count 1 in the filed file):

```
R2 from 1.25 to 1.5 hours, both under 6; no other total changes (flag F37).

```

Replacement:

```
R2 from 1.25 to 1.5 hours, both under 6; no other total changes (flag F37).

Correction 12 Nov 2026, found by PB7's writer: §3 now cites Social Media Today's report (1 Mar 2026) that scheduling is open to all public accounts, a press report quoting no Instagram statement, beside TechCrunch's 2022 report of all professional accounts; the 75-day horizon stays unconfirmed and Mara's 13-day rule is unchanged (flag F32).

```

### 6. Sources entry (new to PB4)

The list is alphabetical. "Social Media Today" sorts before "Socialinsider", as in PB5's list.

Current (count 1 in the filed file):

```
doi 10.1146/annurev.clinpsy.3.022806.091415. https://doi.org/10.1146/annurev.clinpsy.3.022806.091415
- Socialinsider,
```

Replacement:

```
doi 10.1146/annurev.clinpsy.3.022806.091415. https://doi.org/10.1146/annurev.clinpsy.3.022806.091415
- Social Media Today, "Instagram opens up content scheduling to all users", 1 Mar 2026. https://www.socialmediatoday.com/news/instagram-opens-up-content-scheduling-to-all-users/813448/
- Socialinsider,
```


## New findings

1. **The wording of C3 and F32 does not match PB4's text (no change; for the record).** C3 says PB4 "left open whether any public account may schedule", and F32 cites "a Meta help summary [suggesting] any public account may now schedule". PB4 says neither. It states TechCrunch's 2022 "all professional accounts" and that the Help Centre body was unreadable. The Replacement above leaves the 2022 report in place beside the 2026 one, so it does not need either wording.
2. **The PB4 checklist (line 246) cites "TechCrunch 2022" for scheduling the six posts.** No change: that citation still supports the act of scheduling, and the correction names only §3.
3. **Uppbeat's wording.** The source says "carousel" ("may come back around with the second slide showing"), where C1 says "post". The Replacement follows the source.

Nothing else found.
