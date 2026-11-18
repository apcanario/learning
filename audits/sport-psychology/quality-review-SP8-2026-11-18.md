claude-opus-5-5

Verdict: SP8 · fix · 2 errors, 11 should-fix, 13 minor

Quality review of SP8, Competition day (flag F115), run 18 Nov 2026 by a fresh Opus 5.5 agent that had not seen the unit written. It read unit.md, brief.txt, notes.md, unsure.md, sources.md, sourcing-standard.md, case-facts.md, flags.txt, filed SP1 to SP7, audit-units-SKILL.md and viz.py. Web: WebSearch first, then WebFetch only of addresses those searches returned. Every Current below was checked with an exact count and occurs once in unit.md.

## Not verified

These are the only claims or fields the checker could not confirm on a page it opened. Each one is cut or marked.

- [should-fix] [population] Section 2, Smith & Sherwin; Current: "One qualitative study of adults."; Problem: the abstract and the Limerick record give no ages; "elite rugby union" does not establish that every participant was an adult; Fix: "One qualitative study in elite rugby union; the abstract gives no ages."; Basis: https://pure.ul.ie/en/publications/coach-and-athlete-perceptions-of-half-times-inhigh-performancerug/ (8 coaches, 8 players, no ages).
- [should-fix] [population] A2, Half-time row; Current: "one qualitative study of adults in elite rugby]"; Problem: as above; Fix: "one qualitative study in elite rugby union, ages not given]"; Basis: as above.
- [minor] [bibliography] Sources, Smith & Cushion; Current: "Smith M, Cushion CJ"; Problem: no page opened by the checker shows the authors' names or initials (PubMed, SPONET and LIDA show none); title, journal, year, 24(4):355–366 and DOI are confirmed; Fix: no text change; the entry already says the initials come from a later paper's reference list. Leave as marked.
- [minor] [bibliography] Sources, Thelwell et al. (2017); Current: "Thelwell RC, Wagstaff CRD"; Problem: the author list was not shown on any record the checker opened (LIDA shows none); journal, 2017, 35(1):44–55 and DOI are confirmed; Fix: no change needed if the writer's repository copy shows them (the writer's log says it does). Otherwise append "; author list from the repository copy only" to the entry.

Unsure-list items the checker resolved: item 2, Andrade et al. authors (confirmed: Andrade A, Bevilacqua GG, Casagrande PO, Brandt R, Coimbra D, on the Jio Institute library's EBSCO record https://searchworks.jioinstitute.edu.in/articles/edo__149790285). Item 4, Thelwell 2017 print year (2017; 35(1):44–55 on LIDA https://lida.sport-iat.de/twm/Record/4041871?lng=en). Item 6, Zimmerman percentages (Table 1: 70.6% confident, 72.7% genuine; "Is emotional" SD 1.29, the most varied; https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1615784/full). Item 8, Thelwell 2008 issue (22(1); initials RC, NJV, IA, NV on https://eprints.chi.ac.uk/id/eprint/253/). Item 5 (van Kleef sample sizes) remains: the abstract gives none, and the unit says so.

## Findings

Ranked most severe first.

1. [error] [accuracy] Section 7, Tamminen et al.; Current: "and that parents cut in or allowed no reply in about half the cases after a child's praise, statement of confidence or comment on what to improve"; Problem: the praise, the expressions of confidence and the comments on improvement were the parent's, not the child's. The study reports parents interjecting, or not letting the athlete respond, after the parent's own statements (praise 35 of 64, 54.7%; confidence 9 of 18, 50.0%; areas for improvement 48 of 107, 44.9%); Fix: "and that after their own praise, statements of confidence or comments on what to improve, parents cut in or left the athlete no room to reply in about half the cases"; Basis: author's manuscript, Results, Athlete Verbal Responses, https://utoronto.scholaris.ca/server/api/core/bitstreams/e1db026f-0d99-4ca0-9d8b-16528592ab0b/content.
2. [error] [bibliography] Sources, Thelwell et al. (2017); Current: "Rayner A" (
 = a new line), Chapman M" (the Current spans two lines: the text `Rayner A" (`, a line break, then ` = a new line), Chapman M`); Problem: stray text breaks the reference in the middle of the author list, so the entry renders broken; Fix: "Rayner A, Chapman M" (on the one line that starts `- Thelwell RC, Wagstaff CRD,`); Basis: the entry as it should read, confirmed on LIDA, https://lida.sport-iat.de/twm/Record/4041871?lng=en.
3. [should-fix] [bibliography] Sources, Tamminen et al.; Current: ""- Tamminen KA, Bissett JE"; Problem: a stray opening quotation mark stops the line from being a list item; Fix: "- Tamminen KA, Bissett JE"; Basis: Markdown list form used by every other entry.
4. [should-fix] [accuracy] Section 1, Hagan et al.; Current: "Most effects were small"; Problem: the paper says "small effect sizes noted in some areas" and reports time effects of "small to large effect size values (0.16, 0.14, and 0.94)", so "most" overstates it; Fix: "Several effects were small"; Basis: https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00692/full.
5. [should-fix] [bibliography] Sources, Walsh et al.; Current: "read in full on a copy of the published online-first article"; Problem: the source log records the first 100,000 of 135,615 characters, not the full text; Fix: "read on a copy of the published online-first article (its first 100,000 of 135,615 characters, which hold every passage cited here)"; Basis: sources.md row 1; the checker confirmed all eight cited passages in that range on https://researchonline.ljmu.ac.uk/16297/1/Walsh%202020_%20Sleep%20and%20the%20Athlete%202021_%20Consensus%20Review_%20BJSM_%20With%20Supplementary%20Material.pdf.
6. [should-fix] [population] Section 6; Current: "the climate SP3 linked to fear of failure in young athletes [weak, association; SP3's grade]"; Problem: SP3's finding comes from 479 handball players aged 16 and 17, and "young athletes" hides the sample; Fix: "the climate SP3 linked to fear of failure in 479 handball players aged 16 and 17 [weak, association; SP3's grade; for 10 to 15 and 19 to 25 outside the sampled ages]"; Basis: SP3 section 1 and table, Gómez-López et al. (2020).
7. [should-fix] [population] A1, Several athletes row; Current: "[weak, association, for ego-involving attention and fear of failure; SP3]"; Problem: as above; Dani is 14; Fix: "[weak, association, for ego-involving attention and fear of failure; SP3; ages 16 and 17 in the study, so for Dani, 14, outside the sampled ages]"; Basis: SP3 section 1.
8. [should-fix] [flag] Section 1, F84; Current: "- **No new technical instruction about how to move** [practice; SP4 section 5]."; Problem: F84 asks SP8 to use SP6's level-6 rehearsal of the competition's timeline (SP6 section 7: "SP8 builds the competition-day protocol; a rehearsal is where its timings are tried"), and the unit never mentions it; Fix: "- **No new technical instruction about how to move** [practice; SP4 section 5].
- **Try the timings in a rehearsal first, where the athlete's cap allows it.** SP6's top ladder level is a rehearsal of the competition's timeline, run once or twice a season, well before an important competition and never as the last session before one; it is where this protocol's timings are tried. All three case athletes are capped at level 3 while their referrals are under way, so none of them runs it this season [practice; SP6 sections 7 and 8]."; Basis: SP6 sections 7, 8 and 9; flags.txt F84.
9. [should-fix] [scope-safety] Section 6; Current: "another accredited coach, a team manager or a senior athlete who knows the athlete's routine"; Problem: a "second adult" in charge of a minor is given as possibly "a senior athlete", with no check named. A senior athlete may be under 18, or may not have the check the club's safeguarding policy requires; Fix: "another accredited coach, a team manager or an adult senior athlete, with whatever check your club's safeguarding policy requires of adults who look after minors, who knows the athlete's routine"; Basis: brief (safeguarding put as the club's or federation's question); unit section 6, last paragraph.
10. [should-fix] [case] A1, introduction; Current: "Her cue (*added*): "Sleeve first", from the grip-fight process goal she practised calm and under pressure in SP6's block."; Problem: the protocol gives Dani a routine ("her own routine", "her routine again, ending in her cue"), but no routine for Dani exists in the case register or in SP6 (SP6's Deliverable B builds Sara's only), and the notes do not list one; Fix: "Her cue (*added*): "Sleeve first", from the grip-fight process goal she practised calm and under pressure in SP6's block. Her routine between contests (*added*): her usual warm-up, shortened, ending in her cue."; Basis: case-facts.md (SP6 rows for Dani); SP6 Deliverable B. Also add this fact to notes.md under Case facts.
11. [should-fix] [case] A1, Several athletes row; Current: "Dani, the younger, with the referral under way, gets the coach"; Problem: the team-mate's age is not in the register or the notes, so "the younger" is an unlisted invented fact; Fix: "Dani, who stays near her coach before competing and has a referral under way, gets the coach"; Basis: case-facts.md (SP7: stays near her coach); section 6's order.
12. [minor] [case] A1, Between contests; Current: ""Drink, sit, then your warm-up from the band work.""; Problem: "band work" is an invented detail of Dani's warm-up that is not in the notes; Fix: ""Drink, sit, then your usual warm-up.""; Basis: case-facts.md.
13. [minor] [bibliography] Sources, Thelwell et al. (2008); Current: "- Thelwell R, Weston N, Greenlees I, Hutchings N. A qualitative exploration of psychological-skills use in coaches. *The Sport Psychologist* 2008;22:38–53. (abstract read"; Problem: initials, issue and DOI are missing; Fix: "- Thelwell RC, Weston NJV, Greenlees IA, Hutchings NV. A qualitative exploration of psychological-skills use in coaches. *The Sport Psychologist* 2008;22(1):38–53. https://doi.org/10.1123/tsp.22.1.38 (abstract read"; Basis: https://eprints.chi.ac.uk/id/eprint/253/ (initials, 22(1), 38–53); https://www.sciencegate.app/document/10.1123/tsp.22.1.38 (DOI, 22(1), 38–53).
14. [minor] [bibliography] Sources, Thelwell et al. (2008); Current: "issue and DOI not shown: not verified)"; Problem: these are now verified; Fix: "issue and DOI not shown there; initials and issue from the University of Chichester's repository record, https://eprints.chi.ac.uk/id/eprint/253/, and the DOI from the ScienceGate record, both opened by the quality review on 18 Nov 2026)"; Basis: as in 13.
15. [minor] [bibliography] Section 11, Thelwell et al. (2008) link; Current: "(https://researchportal.port.ac.uk/en/publications/a-qualitative-exploration-of-psychological-skills-use-in-coaches/))"; Problem: the brief asks for the DOI address for a paper; Fix: "(https://doi.org/10.1123/tsp.22.1.38))"; Basis: brief, "Links are given as links (the DOI address for a paper)".
16. [minor] [bibliography] Sources, Andrade et al.; Current: "which shows title, journal, year, volume, issue, pages and DOI but not the authors; not the publisher's page)"; Problem: the entry names authors without saying where they were confirmed; Fix: "which shows title, journal, year, volume, issue, pages and DOI but not the authors; authors from the Jio Institute library's EBSCO record, https://searchworks.jioinstitute.edu.in/articles/edo__149790285, opened by the quality review on 18 Nov 2026; not the publisher's page)"; Basis: that record.
17. [minor] [figure] Figure 1, section 1; Current: ""note": "state first, talk later""; Problem: section 7 lets an athlete who wants to talk talk at once, so "talk later" does not match the text; Fix: ""note": "state first; talk when ready""; Basis: unit section 7 ("one who wants to talk talks first").
18. [minor] [figure] Figure 2, section 7; Current: ""outcome": "They talk first; one thing they control; one thing that went well""; Problem: the text says "one thing they controlled"; Fix: ""outcome": "They talk first; one thing they controlled; one thing that went well""; Basis: unit section 7.
19. [minor] [label] Preamble, F48; Current: "the unit says "outside the sampled ages", as SP5 and SP7 do."; Problem: the unit also uses "inference for coaches" (section 11, A1) and "inference for boys" (A2), which the preamble does not define; Fix: "the unit says "outside the sampled ages", as SP5 and SP7 do; where a finding from athletes is applied to coaches, or from girls to boys, it says "inference for coaches" or "inference for boys" (flag F48 leaves the label's scope to syllabus review S-SP1)."; Basis: SP1 section 9; flags.txt F48.
20. [minor] [accuracy] Section 7, Murray et al.; Current: "In 153 athletes from 17 UK university teams (mean age 20.5) asked after a win or a loss to explain the result, how controllable they judged its cause was not associated with their team's confidence before the next match"; Problem: the outcome is collective efficacy, and the mean age is given for the 163 first recruited; Fix: "In 153 athletes from 17 UK university teams (mean age 20.5 among the 163 first recruited) asked after a win or a loss to explain the result, how controllable they judged its cause was not significantly associated with their collective efficacy (their belief in the team's capability) for the next match"; Basis: accepted manuscript, https://dspace.stir.ac.uk/bitstream/1893/30466/1/Murray%20et%20al.%20%28in%20press%29%20PSE%20%20Nov%202019.pdf (163 recruited, M = 20.51; 153 analysed; Table 3).
21. [minor] [label] Section 3; Current: "[practice; Smith & Cushion, 2006, describe what top-level youth coaches did; no outcome was measured]"; Problem: an abstract-only source is cited here without "abstract read"; Fix: "[practice; Smith & Cushion, 2006, abstract read, describe what top-level youth coaches did; no outcome was measured]"; Basis: sourcing standard Part 7 ("a claim that rests on an abstract alone says so").
22. [minor] [accuracy] Section 7, Knight et al. (2011); Current: "positive, honest feedback: positive points, a few pointers, then more positive points"; Problem: the athletes asked for one or two pointers; Fix: "positive, honest feedback: positive points, one or two pointers, then more positive points"; Basis: https://cronfa.swansea.ac.uk/Record/cronfa14907/Download/0014907-10042015110219.pdf, After the Competition.

### Source-log and unsure-list edits (sources.md, unsure.md, notes.md; not unit.md)
- sources.md row 2: "[Authors not verified]." to "Andrade A, Bevilacqua GG, Casagrande PO, Brandt R, Coimbra D (authors from https://searchworks.jioinstitute.edu.in/articles/edo__149790285, opened by the quality review, 18 Nov 2026)."
- sources.md row 5: "Smith, Cushion." to "Smith M, Cushion CJ (DOI from PubMed, https://pubmed.ncbi.nlm.nih.gov/16492600, as the unit's entry says; initials from a later paper's reference list)." The unit cites a PubMed address that the log does not list.
- sources.md row 18: "Fletcher, Scott." to "Fletcher D, Scott M (authors and DOI from https://dspace.lboro.ac.uk/dspace-jspui/handle/2134/22712, opened by the fresh check and again by the quality review, 18 Nov 2026)." The unit's entry names this address; the log does not.
- unsure.md items 2, 4, 6 and 8: add "Resolved by the quality review, 18 Nov 2026", with the sources in "Not verified" above. Item 2's "the Sources entry leaves them out" is no longer true.
- notes.md Case facts: add "(SP8) Dani's routine between contests is her usual warm-up, shortened, ending in her cue. Dani." if finding 10 is applied.

## Passes

**Claims · FIX · 41 claims opened and checked; 37 PASS, 1 FAIL (Tamminen, finding 1), 3 overstated or imprecise (Hagan, Murray, Knight pointers: findings 4, 20, 22), 0 unverifiable in substance (one population word unverified, in "Not verified").** Confirmed:
- Walsh et al. (2021): all eight quoted passages; the 19 authors; Box 2 item 4 uncited; the consensus method not described; Erlacher et al. on German athletes.
- Andrade et al.: 1,010; 511/499; mean age 20; 2.30 (1.47–3.61); 3.45 (2.18–5.48).
- Hagan et al.: 90 players, 15–39, M 26.26; Ghanaian league; the 7 d / 2 d / 1 h pattern; more facilitative at 1 h; self-confidence highest at 1 h; no interaction by gender or skill over time.
- Ren et al.: 36 players (18/18); slower without lower accuracy; less-skilled no significant change; early occlusion; the working-memory quote; attention not measured; laboratory caveat.
- Smith & Cushion: six coaches; interviews; "The use of silence was the largest single behaviour"; silent monitoring with instruction, praise and encouragement.
- Smith & Sherwin: 8 + 8; "succinct" plan devised collaboratively; calm, emotionally controlled coach.
- Rubio et al.: 61 aged 10–16, six teams; the difference gone with age as covariate; 10 boys aged 16–17 over eight matches; the conclusion.
- van Kleef et al.: two field studies, designs and sports; happiness conducive, anger not; no sample sizes.
- Thelwell et al. (2017): 13 athletes; the cues quote; mostly negative; less effective.
- Zimmerman et al.: 264, ages 18–23, 36 teams; 70.6% / 72.7%; "Is emotional" the most varied.
- Knight et al. (2011): 36 girls aged 12–15, team sports; after, during and before items, including reading mood (After the Competition).
- Tamminen et al.: 28 dyads, 11–16, six sports, 98 rides; 12.9% quote; silence 59%; 83.2% of questions closed; ride timing not recorded.
- Knight et al. (2017): all four statements.
- Murray et al.: 153 analysed, 17 UK university teams; controllability not significant.
- Török et al.: 111 athletes aged 13–36; the attribution composite with self-handicapping (β = 0.34).
- Howells & Lucassen: four British women, Rio 2016; highs and lows; celebrity; a normal response.
- Diment et al.: 49 athletes; 27% and 16%; the non-significant tendency.
- Fletcher & Scott: both quotes.
- Thelwell et al. (2008): 13 coaches; the self-talk and imagery quote; purposes.
- Santi et al.: 2,272 Italian coaches; reappraisal lower, suppression higher.

**Bibliography · FIX · 20 entries checked field by field against publisher, repository or index records; all 20 exist; FIX 5 (Tamminen and Thelwell 2017 formatting: findings 2 and 3; Walsh extent read: finding 5; Thelwell 2008 initials, issue, DOI: findings 13 and 14; Andrade author provenance: finding 16).** Confirmed fields:
- Diment GM, Stagis ND, Küttel A, 2023;5:21–30.
- Fletcher D, Scott M, 28(2):127–137.
- Hagan, 8:692.
- Howells & Lucassen, 37:67–78.
- Knight, Berrow & Harwood, 16:93–97.
- Knight, Neely & Holt, 23(1):76–92.
- Murray et al., 47:101620.
- Andrade et al., 49(2):137–142.
- Ren et al., 13:823989.
- Rubio et al., 27(1):59–66, no DOI on the journal archive (https://archives.rpd-online.com/article/view/v27-n1-rubio-hernandez-sanchez-etal.html).
- Santi et al., vol. 11, published 2021.
- Smith & Sherwin, 2025;14(3):315–338.
- Smith & Cushion, 24(4):355–366.
- Tamminen et al., 58:102095.
- Thelwell 2017, 35(1):44–55.
- Török et al., 13:862122.
- van Kleef et al., 41:1–11.
- Walsh et al., 55(7):356–368, 19 authors.
- Zimmerman et al., 7:1615784.

**Source log · FIX · 20 of 20 Sources entries have a row in sources.md; 11 abstract-only sources are each labelled "abstract read" at first citation; FIX 4 (rows 2, 5 and 18 lack the addresses or authors the unit names; one repeat citation lacks "abstract read": finding 21).**

**Grades · FIX · all protocol lines graded (A1 15 rows, A2 18, A3 14 plus 9 timeline rows; B, C and D graded or practice by the deliverable's rule); grades checked against SP1's key and against SP3, SP4, SP5, SP6 and SP7 wording. FIX 2 (population of SP3's grade: findings 6 and 7).** The grades match the source units' own wording:
- SP5's breathing, self-talk, imagery, acceptance, process-goal and external-focus grades.
- SP6's routine (moderate, positive; ages 11 to 40) and debrief (weak, positive, outside sport).
- SP4's challenge association (weak, positive; inference).
- SP3's harsh coaching (weak, against), recognition (weak, positive; 9 to 15), parent education and parental support.
- SP7's package grade (weak, positive; 9 to 15).
- SP2's strong (association) and weak grades.
- SP1's ironic effects (weak, positive; inference).

Consensus-only lines are practice, with SP3's note as the preamble states (F14, F47).

**Population · FIX · 20 findings, each with its sample named; transfers to under-18s labelled inference, or outside the sampled ages. FIX 4 (findings 6, 7 and 19; the "adults" population word in "Not verified").**

**Scope and safety · FIX · no assessment, diagnosis or treatment taught; injury, mental health, eating and abuse each routed (medical service, scope card, urgent route, welfare officer); weigh-in named only as a time, with no comment on weight; no weight-loss method, calorie figure, target weight or self-harm method; rules, supervision and reporting put as questions with bodies to ask; disclaimer present; no real athlete, coach or club named. FIX 1 (second adult for minors: finding 9).**

**Any sport · PASS · examples outside the case: judo 3, football 3, 400 m and athletics 3, swimming 2, gymnastics 2, volleyball 1, tennis 1, archery 1 (16; largest share 3 of 16). The case deliverable gives each case sport a third by the brief's design. Individual, team, weight-class and judged sports are all present. Nothing found that points to the Project's owner, his sport, his club or his athletes.**

## Brief and deliverable, item by item
Section 1:
- The phases and what the coach controls in each: covered (section 1, table and figure).

Section 2:
- The last minute and the case for one cue: covered.

Section 3:
- Sideline behaviour and expressed emotion: covered.

Section 4:
- Resets: covered.

Section 5:
- Rules as a question: covered (six questions; the "not checked" rule).

Section 6:
- Several athletes: covered.

Section 7:
- After a loss and after a win (when to talk, what to talk about, what the athlete controls), at 12 and at 20: covered.

Section 8:
- First and early titles and the days after: covered.

Section 9:
- Parents on the day: covered.

Section 10:
- Competitions over several days: covered.

Section 11:
- The coach's own nerves with SP5's skills: covered.

Popular claims:
- The rousing pre-match speech: named and set against the evidence.
- Harsh coaching: named and set against SP1's and SP3's grade.

Deliverable:
- A1 (bouts, Dani), A2 (team match, Milan) and A3 (timed event, Sara): built in full.
- B (the debrief card, loss and win): built, with a per-athlete version.
- C (the parents' note: Dani's, Milan's variant, and Sara's version to Sara): built.
- D (templates for all three): built, with blanks that say what goes in them.

Complete.

## Flags naming SP8
- F7, F24: dealt with. The unit used publisher pages and repository or index records the session reached, and relies on no PubMed Central page.
- F8: dealt with. SP1's key is used unchanged (preamble).
- F14: dealt with. Consensus-only recommendations are [practice] with "the studies behind it were not opened".
- F21: partly met, and said so. Walsh et al. was opened on a repository copy of the published article because the publisher's page was not returned; notes item 1 passes the sleep-night contradiction to SP9 and SP10.
- F37: dealt with. C adds "At competitions" and "After a competition" to SP3's page; Sara's version goes to Sara.
- F47: dealt with as far as SP8 can. It follows the SP3 convention its preamble states; the syllabus question stays open.
- F48: FIX, minor (finding 19). The unit uses labels beyond the preamble.
- F63: dealt with. Nothing in SP8 rests on the unopened SP5 reviews; only SP5's grades are carried.
- F66: dealt with. Section 1, and every protocol's evening-before and warm-up rows.
- F73: dealt with. Section 11 and A3 make no performance claim for breathing.
- F84: half dealt with. Sara's routine is placed on the timeline from Deliverable B and SP6's pre-competition rules are kept; the level-6 rehearsal is missing (finding 8).
- F96: dealt with. "How nervous" and "how much pressure" sit on separate lines, and the pressure rating is not taken on the day; state-response rows are practice unless graded.
- F97: dealt with. Section 3, "What is not known"; touchline guidance rests on van Kleef et al., abstract read.
- F100: not applicable. SP8 says nothing on medication or anti-doping.

## Consistency with SP1 to SP7
Every pointer checked holds:
- SP5 section 6 (nothing new), SP6 section 8 (one level below; no drill the day before), SP4 section 5 (no new technical instruction).
- SP4 table row 3; SP4's two check-in questions, word for word; SP4 section 7 and SP7 section 6 (no prediction).
- SP7's baseline lines for all three athletes; the tearful, over-aroused and frozen rows; script 1; Milan's Monday (*added*).
- SP6's Deliverable B, elements 1 to 5 and the reset; Sara's cap 3 and level 2 while her sleep is short.
- SP2 section 10.

Where the deliverable uses earlier tools:
- SP6 Deliverable B and SP7's baseline sheet and state-response table are used as flagged.
- SP4 and SP6 ratings are on separate lines.

## Style
- British spelling throughout; "behaviors" and "soccer" appear only in source titles.
- No em dashes; en dashes appear only in page ranges and "parent–athlete".
- No "not X but Y" constructions.
- No private-course reference.

## Figures (7)
- Figure 1 · flow · section 1 · FIX, minor (finding 17). Labels trace to section 1's table, except "talk later". The caption names the section and the source; the kind fits a sequence.
- Figure 2 · decision · section 7 · FIX, minor (finding 18). Every node traces to section 7's ordering paragraph; the caption names the section and the sources; the kind fits a rule with branches.
- Figure 3 · flow · Deliverable A3 · PASS. All eight labels and notes trace to A3's timeline table; the caption names SP6 Deliverable B, SP5 and the unit; the kind fits a sequence.

All three blocks parse as JSON of kinds that viz.py draws. A render was not possible inside the folder because design/theme.css is outside it.

## Read as the coach
The unit is usable on the day. Each protocol row says what to do, what to say and what to avoid. The repeated grades are dense on a phone but consistent. Two points a coach would trip on are findings 9 and 10.

Unit SP8 · fix · 2 errors, 11 should-fix, 13 minor (counts include the 2 should-fix and 2 minor in "Not verified"). No REWRITE is open.
