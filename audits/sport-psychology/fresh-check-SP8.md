---
audit: fresh check
unit: SP8 · Competition day
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-18
chat: https://claude.ai/code/session_01KMmgR34XZwxjLvEDzEhodB
verdict: fix · 0 errors, 10 should-fix, 12 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SP8 · fix · 0 errors, 10 should-fix, 12 minor

# Fresh check: SP8 · Competition day (Sport Psychology for Coaches)

Model: claude-opus-5-5. Isolated agent context; I did not see the unit being written. Checked on 18 Nov 2026 with live search (WebSearch first; I fetched only URLs a search in this context returned). Errata: no audit report, so I skipped it. SP1's key is taken as the brief quotes it: strong / moderate / weak / contested / practice.

## (1) Coverage
- The day in eight phases, and what the coach controls in each: covered (section 1, table, figure 1).
- The last minute, how much instruction an athlete can use, the case for one cue: covered (section 2).
- The coach's behaviour and expressed emotion on the sideline: covered (section 3).
- Resets between rounds, periods and attempts: covered (section 4).
- The sport's rules on coaching, put as a question: covered (section 5).
- Several athletes on one day: covered (section 6).
- After a loss and after a win (when, what, controllable versus not, at 12 and at 20): covered (section 7).
- A first title and an early title, and the days after: covered (section 8).
- Parents on the day: covered (section 9).
- Competitions over several days: covered (section 10).
- The coach's own nerves, using SP5's skills: covered (section 11).
- Deliverable: three protocols (A1 bouts/Dani, A2 team match/Milan, A3 timed event/Sara), debrief card after a loss and after a win (B), parents' note (C, with Sara's version), and templates for all three tools (D). All present in full.
- "Gives" items: the coach's own noise for DD-SP3 (section 11) is present.

## Findings

[should-fix] [accuracy] section 2, Ren et al.; Current: "high cognitive anxiety slowed responses without lowering accuracy, in both groups; the skilled players slowed more."; Problem: the full text says response time rose significantly only in the skilled group (about 638 to 872 ms); the less-skilled group's response time did not change significantly. "In both groups" overstates the finding; Fix: "high cognitive anxiety slowed the skilled players' responses without lowering accuracy, while the less-skilled players' response times did not change significantly; processing efficiency fell under high anxiety, mainly when the clip was cut off early."; Basis: Ren et al. 2022, full text, https://www.frontiersin.org/articles/10.3389/fpsyg.2022.823989

[should-fix] [accuracy] section 1, Walsh Box 2; Current: "One of its boxed points says that a poor night's sleep the night before competition should not affect performance, a point given without a citation and at odds with its own statement that the evidence is unclear"; Problem: the point sits under Box 2's "Bank sleep" tool and reads "athletes can be confident that a poor night's sleep the night before competition should not affect their performance". It is tied to banking sleep beforehand. Quoting it without that context stretches it; Fix: "One of its boxed points, under its tool for banking sleep, says athletes can be confident that \"a poor night's sleep the night before competition should not affect their performance\", a point given without a citation and hard to square with its own statement that the evidence is unclear"; Basis: Walsh et al. 2021, repository copy, https://researchonline.ljmu.ac.uk/16297/1/Walsh%202020_%20Sleep%20and%20the%20Athlete%202021_%20Consensus%20Review_%20BJSM_%20With%20Supplementary%20Material.pdf

[should-fix] [attribution] Sources, Tamminen et al. missing; Current: "- Thelwell RC, Wagstaff CRD, Rayner A"; Problem: Tamminen et al. (2022) is cited in sections 7 and 9 and is in the source log (row 12), but it has no Sources entry. This fails Part 1 ("every source it cites is listed with a full reference"); Fix: "- Tamminen KA, Bissett JE, Azimi S, Kim J. Parent and child car-ride interactions before and after sport competitions and practices: Video analysis of verbal and non-verbal communication. *Psychology of Sport and Exercise* 2022;58:102095. https://doi.org/10.1016/j.psychsport.2021.102095 (full text of the author's manuscript read on the University of Toronto's repository, https://utoronto.scholaris.ca/server/api/core/bitstreams/e1db026f-0d99-4ca0-9d8b-16528592ab0b/content; not the publisher's page)\n- Thelwell RC, Wagstaff CRD, Rayner A" (\n = a new line); Basis: authors and full title from the PSE vol. 58 contents list, https://idrottsforum.org/psychology-of-sport-and-exercise-vol-58-january-2022/, and the University of Toronto record, https://utoronto.scholaris.ca/items/72363cef-efc9-49aa-be8c-71243f61128b. I did not verify article number 102095 (it is from the source log).

[should-fix] [attribution] Sources, pre-competition sleep survey; Current: "- [Authors not verified]. Prevalence of poor sleep quality"; Problem: the authors can be verified: Andrade A, Bevilacqua GG, Casagrande PO, Brandt R, Coimbra D; the journal, 49(2):137–142 and the DOI also match. Also update source log row 2; Fix: "- Andrade A, Bevilacqua GG, Casagrande PO, Brandt R, Coimbra D. Prevalence of poor sleep quality"; Basis: Jio Institute library index record, https://searchworks.jioinstitute.edu.in/articles/edo__149790285

[should-fix] [attribution] Sources, Thelwell et al. (coach stress); Current: "*Journal of Sports Sciences* 35(1):44–55 (year given as 2016 on the copy read; print year not verified)"; Problem: the issue record gives 2017;35(1):44–55, DOI 10.1080/02640414.2016.1154979. The 2016 date is the repository or online date; Fix: "*Journal of Sports Sciences* 2017;35(1):44–55 (published online 2016)"; Basis: LIDA record, https://lida.sport-iat.de/twm/Record/4041871?lng=en; authors confirmed on https://eprints.staffs.ac.uk/2259

[should-fix] [attribution] Sources, Fletcher & Scott; Current: "(abstract read on the SPONET index record, https://sponet.de/sponet/Record/4018057?lng=en, which shows title, journal, year, volume, issue and pages but not the authors or the DOI; the authors' names are those of the search that found the record and were not shown on any page opened: not verified; DOI not verified)"; Problem: the authors (Fletcher, David; Scott, Michael) and the DOI 10.1080/02640410903406208 are confirmed. Part 7 requires the DOI address; Fix: "https://doi.org/10.1080/02640410903406208 (abstract read on the SPONET index record, https://sponet.de/sponet/Record/4018057?lng=en; authors and DOI as on Loughborough University's repository record, https://dspace.lboro.ac.uk/dspace-jspui/handle/2134/22712, opened by the fresh check on 18 Nov 2026)"; Basis: https://dspace.lboro.ac.uk/dspace-jspui/handle/2134/22712

[should-fix] [attribution] Sources, Smith & Cushion; Current: "- Smith, Cushion (initials not shown on any page opened). An investigation of the in-game behaviours of professional, top-level youth soccer coaches. *Journal of Sports Sciences* 2006;24(4):355–366. (abstract read on the SPONET index record, https://www.sponet.de/sponet/Record/4010744?lng=en, which shows title, journal, year, volume, issue and pages but not the authors or DOI; the authors' names are those of the search that found the record and were not shown on any page opened: not verified; DOI not verified)"; Problem: PubMed gives the DOI 10.1080/02640410500131944 and confirms 24(4):355–366. The initials (Smith M, Cushion CJ) appear in a later paper's reference list, though no primary record shown to me gave them. Part 7 requires the DOI address; Fix: "- Smith M, Cushion CJ. An investigation of the in-game behaviours of professional, top-level youth soccer coaches. *Journal of Sports Sciences* 2006;24(4):355–366. https://doi.org/10.1080/02640410500131944 (abstract read on the SPONET index record, https://www.sponet.de/sponet/Record/4010744?lng=en; DOI as on PubMed, https://pubmed.ncbi.nlm.nih.gov/16492600; initials from a later paper's reference list, not shown on PubMed's page as opened)"; Basis: https://pubmed.ncbi.nlm.nih.gov/16492600 ; https://core.ac.uk/download/288351928.pdf

[should-fix] [label] A2, Evening before; Current: "[weak, positive, for keeping added demands out of the last hour; SP4's grade; inference]"; Problem: section 4 names SP4's grade as "weak, positive, for the association of a challenge state with performance". The row moves that grade onto the recommendation itself, which is untested. That breaks the key's rule that a line with no source testing it is practice; Fix: "[weak, positive, for the association of a challenge state with performance; SP4's grade; inference]; [practice, for keeping added demands out of the last hour]"; Basis: the unit's own section 4 and SP1's key as quoted in the brief

[should-fix] [label] A3 timeline, Call room, early; Current: "[weak, positive, for heart-rate variability; weak, mixed, for performance in the laboratory; no performance claim; SP5, SP6; flag F73]"; Problem: section 11 grades the same SP5 evidence "weak, no performance benefit shown" and says no study opened showed that it improves performance. The two grades for one technique disagree. The maintainer should check SP5 and use one wording in both places. If section 11 is right: Fix: "[weak, positive, for heart-rate variability; weak, no performance benefit shown; SP5, SP6; flag F73]"; Basis: internal consistency with section 11 of the unit

[should-fix] [label] C, Dani's parents' note; Current: "In a study of young athletes, this is what they said they wanted from their parents at games"; Problem: the study sampled 36 girls aged 12 to 15 in team sports (mean 13.5). "Young athletes" generalises the sample, in a note given to the parents of a judoka; Fix: "In one study of girls aged 12 to 15 in team sports, this is what they said they wanted from their parents at games"; Basis: Knight, Neely & Holt 2011 abstract, https://informahealthcare.com/doi/abs/10.1080/10413200.2010.525589

[minor] [attribution] section 1, sleep survey in-text citation; Current: "[Prevalence of poor sleep quality in athletes before competition, 2021, abstract read on a sport-literature index record; authors not verified]"; Problem: the authors are now verified (see the Sources finding); Fix: "[Andrade et al., 2021, abstract read on a sport-literature index record]"; Basis: https://searchworks.jioinstitute.edu.in/articles/edo__149790285

[minor] [attribution] section 3, Thelwell year; Current: "[Thelwell et al., 2016, abstract read on Loughborough University's repository]"; Problem: the print year is 2017; Fix: "[Thelwell et al., 2017, abstract read on Loughborough University's repository]"; Basis: https://lida.sport-iat.de/twm/Record/4041871?lng=en

[minor] [attribution] section 11, Thelwell year; Current: "[Thelwell et al., 2016, abstract read]("; Problem: the print year is 2017; Fix: "[Thelwell et al., 2017, abstract read]("; Basis: https://lida.sport-iat.de/twm/Record/4041871?lng=en

[minor] [style] section 2, Smith & Cushion link; Current: "(https://www.sponet.de/sponet/Record/4010744?lng=en)). The abstract"; Problem: Part 7 asks for the DOI address for a paper, and the DOI is now known; Fix: "(https://doi.org/10.1080/02640410500131944)). The abstract"; Basis: https://pubmed.ncbi.nlm.nih.gov/16492600

[minor] [style] section 11, Fletcher & Scott link; Current: "(https://sponet.de/sponet/Record/4018057?lng=en)). Athletes said"; Problem: the same: the link should be the DOI address; Fix: "(https://doi.org/10.1080/02640410903406208)). Athletes said"; Basis: https://dspace.lboro.ac.uk/dspace-jspui/handle/2134/22712

[minor] [figure] section 7, Murray et al. sample; Current: "In 153 athletes from 17 UK university teams"; Problem: the abstract gives N = 163 from 17 teams. My fetch of the full text was refused (not checked), so 153 (92 + 61) may be the analysed sample, and the controllability result, which the abstract does not mention, is unverified; Fix: "In 153 athletes (the abstract gives 163) from 17 UK university teams"; Basis: https://researchportal.hw.ac.uk/en/publications/adaptive-thinking-can-adaptive-dispositional-attributions-protect/

[minor] [label] section 11, last bullet; Current: "the second adult named in section 6 takes over the athlete's cue and routine."; Problem: this recommendation has no grade. The section's opening grade covers SP5's skills only; Fix: "the second adult named in section 6 takes over the athlete's cue and routine [practice]."; Basis: SP1's key as quoted in the brief ("every technique and every recommendation carries one grade")

[minor] [label] section 7, After a win; Current: "as part of a coach programme; ages 9 to 15; SP3's grade]"; Problem: the advice is applied to athletes up to 20 (the table, A3) without saying that this falls outside the sampled ages. Section 7's "After a loss" line ("ages 9 to 15") has the same gap; Fix: "as part of a coach programme; ages 9 to 15, so for 16 to 25 outside the sampled ages; SP3's grade]"; Basis: the unit's preamble convention ("outside the sampled ages")

[minor] [style] section 9, internal flags; Current: "athlete, who decides what to share (SP3; flag F37)"; Problem: syllabus flag numbers mean nothing to the public reader. The same applies at lines 201, 223, 245, 261, 269, 286, 330, 356 and 446. Keep them only if SP2 to SP7 print them as a course convention; Fix: "athlete, who decides what to share (SP3)"; Basis: brief (written to be shared with anyone)

[minor] [coverage] A1, Dani's coach; Current: "raises his voice in training, working on normal volume (SP3)"; Problem: "working on normal volume" is not in case-facts.md (no SP3 row) and not in the unit's notes. If SP3's deliverable set it, add it to the register; otherwise mark it as added; Fix: "raises his voice in training, working on normal volume (*added*)"; Basis: case-facts.md; notes.md

[minor] [coverage] A1 and A3, SP6 caps; Current: "Her SP6 cap is 3; her last session before the event ran one level below her current level."; Problem: neither Dani's cap of 3 nor Sara's cap of 3 and "level 2 at most" (A3) is in case-facts.md or the notes. Add them to the register, or mark them; Fix: "Her SP6 cap is 3 (*added*); her last session before the event ran one level below her current level."; Basis: case-facts.md; notes.md

[minor] [coverage] A3, Sara's coach's gender; Current: "Checks the timetable with her; tells her where he will be."; Problem: case-facts.md does not give the gender of Sara's coach. "He" also appears in the A3 "Several athletes" row. Unless an earlier unit fixed it, it is an unlisted fact; Fix: "Checks the timetable with her; tells her where the coach will be."; Basis: case-facts.md

(I checked every Current with grep -F: each occurs exactly once in unit.md.)

## (2) Accuracy
My verdicts on each cited claim. "Not opened" means I could not open the source in this context.
- Walsh et al. 2021: the quotations "Sleep disturbance is a common occurrence prior to competition...", "were more evident in individual compared with team sports" (citing Erlacher et al., German athletes), "Athletic performance is reduced by a night or more without sleep", partial restriction over 1 to 3 nights "remains unclear", the evening matches 18:00 to 21:00 "commonly associated with later sleep onset time", jet lag about 1 day per time zone, "sparse" direct evidence, 19 authors, and no consensus method described: PASS. Box 2 point: FAIL (stretch). Bibliography 55(7):356–368, DOI: PASS (experts.arizona.edu).
- Andrade et al. 2021 (pre-competition sleep): 1,010 athletes, 656 men and 354 women, 511 young and 499 adults, mean age 20 ± 7, OR 2.30 (1.47–3.61), OR 3.45 (2.18–5.48): PASS.
- Hagan et al. 2017: 90 table tennis players, Ghana league, aged 15 to 39 (M 26.26), measures at 7 days, 2 days and 1 hour, intensity fell at 2 days after rising at 7, sharp rise at 1 hour, cognitive anxiety more facilitative at 1 hour, rising self-confidence, the same pattern across gender and skill: PASS. The self-confidence effect was large, so "most effects were small" is fair only as "most".
- Ren et al. 2022: 36 players (18 skilled college, 18 PE students), accuracy unchanged, the quotation, attention not measured, laboratory versus match: PASS. "In both groups": FAIL.
- Smith & Cushion 2006: six coaches, modified ASUOI plus interviews, silence the most frequent behaviour, silent monitoring interspersed with instruction, praise and encouragement: PASS on substance. I confirmed the exact quotation only in paraphrase (PubMed).
- Smith & Sherwin 2025: 8 coaches and 8 players, elite rugby union, interviews, a calm environment and an emotionally controlled coach, recovery, a "succinct" plan devised collaboratively: PASS. Bibliography 14(3):315–338: PASS.
- Rubio et al. 2018: 61 players aged 10 to 16 from 6 teams, F(1,60) = 27.32, the difference gone with age as covariate, 10 male players aged 16 to 17 over 8 matches, variation attributed to the match, the conclusion: PASS. No DOI listed at the journal: PASS.
- van Kleef et al. 2019: two multilevel field studies (cross-sectional baseball/softball; cross-lagged soccer before, during and after), happiness and anger predicted players' emotions, their inferences and team performance, happiness better and anger not, no sample sizes in the abstract: PASS.
- Thelwell et al. 2017 (coach stress): 13 professional and national-level athletes, verbal and behavioural cues, most effects negative, coaches less effective when stressed: PASS. Year: see finding.
- Zimmerman et al. 2025: 264 NCAA athletes aged 18 to 23, 36 teams, interactive sports, 70.6% "always" for confident and 72.7% for genuine (the unit's "about 71%" and "about 73%"), "is emotional" the most varied: PASS.
- Knight, Neely & Holt 2011: 36 female athletes, mean 13.5, team sports, interviews, wants that differ by phase: PASS from the abstract. The detailed lists for during and after games are not opened.
- Tamminen et al. 2022: 28 dyads, 98 videos, sport talk 12.9%, mostly silence, mostly closed questions, parents sometimes interrupting: PASS from the abstract. "About half the cases": not opened (full-text fetch refused). The abstract gives 12.9% "of the time"; the unit's "of the interactions" is close enough.
- Knight, Berrow & Harwood 2017: "not necessarily clear-cut", the timing of behaviours, watching an upset or losing child is hard, few strategies evaluated: PASS.
- Murray et al. 2020: unverifiable (full text not opened; the abstract gives N = 163 and does not mention controllability).
- Török et al. 2022: 111 elite athletes aged 13 to 36, cross-sectional, internal, stable, global, controllable and intentional negative attributions associated with self-handicapping: PASS.
- Howells & Lucassen 2018: four female British athletes, Rio 2016, IPA, highs and lows, celebrity, read as a normal response: PASS.
- Diment et al. 2023: 49 Danish Olympians one month after Tokyo, 27% and 16%, a non-significant tendency: PASS.
- Fletcher & Scott 2010: "potential health and performance costs... are significant", "needs to be monitored and addressed": PASS.
- Thelwell et al. 2008: 13 elite coaches, structured interviews, deductive content analysis, self-talk and imagery cited more often than relaxation and goal setting: PASS.
- Santi et al. 2021: 2,272 Italian coaches, lockdown survey, reappraisal with lower stress and suppression with higher, author order: PASS.

## (3) Figures (numbers)
Every number names whose figure it is: PASS, except Murray's N (minor finding).

## (4) Labels
Correlational, qualitative and observational designs are labelled throughout: PASS. I found no vendor data. Grade findings are listed above.

## (5) Deliverable
Present in full. A1, A2 and A3 have every phase row, with words, what not to do, and a grade; B has the loss and win columns and the case table; C has Dani's, Milan's and Sara's versions; D has three templates whose blanks say what goes in them. The deliverable follows from the body and can be used alone: PASS, subject to the grade findings.

## (6) Errata applied
There is no audit report for this course, so I skipped this item. The pointers to SP1 to SP7 I could not check against those units, because the units were not in the packet. They are consistent with case-facts.md, except for the three minor case findings.

## (7) Figures
1. Section 1, a flow of eight phases. Every label and note traces to the section 1 text and table. The caption names the section and the source. A sequence fits a flow. PASS.
2. Section 7, a decision tree. Every question and outcome traces to section 7 ("an injury, illness or red flag goes to medical help or the urgent route now"; "gets you near or the space they asked for, and no review"; "agrees a time, usually the next session"; "talks first, about one thing they controlled and one thing that went well"). The caption names the section and the source. A rule with branches fits a decision. PASS.
3. Deliverable A3, a flow of eight steps. Every label traces to the A3 timeline table. The caption names the deliverable and the source. A sequence fits a flow. PASS.

## Seven passes
- **Claims: FIX.** 19 sources checked. PASS on 17, FAIL/stretch on 2 claims (Ren "both groups"; Walsh Box 2). Not opened: 3 sub-claims (Murray full text and N, Tamminen "about half", Knight 2011 detailed lists).
- **Bibliography: FIX.** 19 entries in Sources. All exist (none invented). 14 match the record field by field. 4 need correcting (Andrade et al. authors, Thelwell 2017, Fletcher & Scott DOI and authors, Smith & Cushion DOI and initials). 1 cited reference is missing (Tamminen et al.). Not verified: Tamminen's article number, and the issue and DOI of Thelwell 2008.
- **Source log: PASS.** 19 of 19 Sources entries have a row in sources.md; every abstract-only claim carries "abstract read" where it is cited (13 sources, every occurrence checked).
- **Grades: FIX.** 2 should-fix and 1 minor. Every protocol row in A1, A2 and A3 carries a grade, and lines without a source are [practice].
- **Population: FIX.** 1 should-fix and 1 minor. Every other transfer to under-18s is labelled inference, and every finding names its sample.
- **Scope and safety: PASS.** Nothing teaches assessment, diagnosis or treatment. Mental health, eating, injury and the coach's own stress are routed to the named services. No weight method, calorie figure or target weight; the weigh-in appears as a time only. No method of self-harm. Rules and safeguarding are put as questions with a body to consult, and the disclaimer is present. No real person, coach or club is named.
- **Any sport: PASS.** Illustrative examples by sport, counted once each: football 3, judo 2, athletics 2, gymnastics 2, and swimming, volleyball, tennis and archery 1 each. That makes 13, with football at 23%. Study samples add table tennis 2, football 3, rugby 1, baseball/softball 1, and football is still under a third. There is nothing that identifies the Project's owner, his sport, club or athletes.

## Other checks
- **Part 7, line by line.** Every line passes except the bibliography, grades and population items above; links as links fail in 2 places (minor). I could not run private_terms.py from this folder; I searched the text by hand and found nothing.
- **British spelling: PASS.** The only American spelling is "behaviors", inside the Knight et al. article title, which is correct.
- **Em dashes: PASS (none).**
- **"Not X but Y" constructions: PASS (none).**
- **Private terms and references to other courses: PASS.** Only SP and DD-SP units of this course are named. The flag numbers are a minor finding.
- **Read as the coach in the preamble would: usable.** The protocols are concrete, phase by phase, with scripted words. The flag numbers are the only text a coach cannot resolve.

## Confirmed
The URLs listed in (2) and in the findings' Basis fields: frontiersin.org (Hagan, Ren, Zimmerman, Török, Santi), pubmed 16492600, pure.ul.ie and informahealthcare (Smith & Sherwin), archives.rpd-online.com (Rubio), cris.haifa.ac.il (van Kleef), eprints.staffs.ac.uk/2259 and the LIDA record 4041871 (Thelwell 2017), cronfa.swansea.ac.uk (Knight 2011 and 2017), utoronto.scholaris.ca/items (Tamminen), researchportal.hw.ac.uk (Murray abstract), pure.cardiffmet.ac.uk (Howells), tidsskrift.dk (Diment), dspace.lboro.ac.uk handle 2134/22712 (Fletcher), researchportal.port.ac.uk (Thelwell 2008), experts.arizona.edu and the LJMU copy (Walsh), searchworks.jioinstitute (Andrade).

## Not checked
- Murray et al. 2020 accepted manuscript and Tamminen et al. 2022 author manuscript: fetches refused by the permission check; not retried.
- scilit.net and the ncbi PMC12463970 URL: redirected; not followed.
- peeref.com/works/20780924: a login page. pmc.ncbi PMC7874101: a browser check.

SP8 · fix · 0 errors, 10 should-fix, 12 minor. No REWRITE is open.
