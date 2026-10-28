# Changelog

Everything that has happened to Personal Mythology and, from session 13, to Academy, from the first request on 22 October 2026 to now, newest first. Each entry is one working session. It is assembled from the kit's own records (`provenance.json`, the review folders and the maintainer log) and from the session transcripts. Where a session recorded the site's version number, it is given. The exact day of each step in the first, three-day session was not recorded; its entries are in order.

## Where things stand

- **Greece, course 1:** complete. 78 reports, about 244,000 words: 55 written with Fable 5.1, 23 with Opus 5.5.
- **Rome, course 2:** 59 of 79 reports, about 180,000 words, all written with Opus 5.5 and all checked. 20 modules are queued: deep dive I (11.3 to 11.8), deep dive II, the Aeneid (12.1 to 12.8), and deep dive III (13.3 to 13.8).
- **Fable review:** every Rome report is reviewed (session 9). Of the 23 Greek Opus reports, 17 are reviewed (eleven audited in full, six cleared on the sample) and six are still flagged: 11.1, 11.2, 11.4, 11.5, 11.6, 11.8 (session 10). Rome 14.3 and the Greek 13.3 high-signal pairs are done; every pair passed.
- **Bibliography:** every report has a machine-extracted unit list and a curated `r-<id>.md` (session 10; the curated files are flagged until Fable spot-checks three units).
- **Corrections:** all nine that were waiting (Greek 6.3, 7.2, 7.3, 8.1, 9.3, 9.4; Rome 1.4, 3.1, 6.1) were applied on 27 October. None is waiting.
- **Theme and home (sessions 11 and 12):** `shell.css` is a copy of the Learning Project's `design/theme.css`. The kit lives in the private repo `apcanario/learning` as `kit/`; the zip is retired. The only published page is the site; the standalone syllabus artifacts and the stray draft pages are deleted.
- **Responsive (session 14):** `design/theme.css` version 2 adds section 6: tablet from 768 px (760 px column, cards in two columns), desktop from 1100 px (the drawer is a persistent 300 px sidebar). The phone layout is unchanged. `verify.py` runs a phone, tablet and desktop pass. Publishing Academy means the artifact, then `./deploy.sh`.
- **Academy (session 13):** the site is Academy: its home lists every course of both hubs, Brand + AI as a placeholder panel until A3. `deploy.sh` publishes the built page to GitHub Pages through the public repo `apcanario/academy` (https://apcanario.github.io/academy/).

## At a glance

| Date | Session | Greece | Rome |
|---|---|---|---|
| 22 to 24 Oct | 1. The Greek course, then Personal Mythology | 0 to 70 | |
| 24 Oct | 2. Rome begins: syllabus, site, units 0 to 3 | 70 | 19 |
| 24 Oct | 3. Rome unit 4 | 70 | 24 |
| 24 to 25 Oct | 4. Rome units 5 and 6, the cohesion review | 70 | 34 |
| 25 Oct | 5. Philosophy in both syllabi, Rome unit 7, the quality pass | 70 | 39 |
| 25 Oct | 6. Rome units 8 to 10, Greek deep dive III | 78 | 59 |
| 25 Oct | 7. The three checks and this changelog | 78 | 59 |
| 27 Oct | 8. The Fable review begins: the rubric and the syllabus | 78 | 59 |
| 27 Oct | 9. Every Rome report reviewed: the sample, the capstone, the decision | 78 | 59 |
| 27 Oct | 10. Bibliographies for every report; the Greek Opus cohort; the overlap checks | 78 | 59 |
| 27 Oct | 11. The site moves onto the Learning Project theme | 78 | 59 |
| 28 Oct | 12. The repo, five artifacts deleted, the kit docs | 78 | 59 |
| 28 Oct | 13. The site becomes Academy (A1), with GitHub Pages | 78 | 59 |
| 28 Oct | 14. Tablet and desktop layouts (P11), Pages in every publish (P8), the deploy script ready for the split (P10) | 78 | 59 |

## 28 October 2026 · Session 14 · Tablet and desktop layouts (P11), Pages in every publish (P8), the deploy script ready for the split (P10)

Backlog rows P8 to P11 of `docs/BACKLOG.md`, on Fable 5.1. No report changed and no flag was cleared.

### Responsive theme (P11)
`design/theme.css` is version 2: a section 6 with two breakpoints and no new token or component. Tablet (768 px and up): the reading column and the top bar widen to 760 px; course cards (a new `.cgrid` wrapper written by `build.py` and `build_hub.py` around the cards that already existed), unit cards, hub unit cards and the coming-soon list go to two columns; a lone card spans both; stat tiles stay three or four across. Desktop (1100 px and up): the drawer is a persistent 300 px sidebar (always open, no backdrop, menu and close buttons hidden, its list scrolls on its own, the current item highlighted as before), the body is padded by the sidebar width so the top bar and the column sit beside it, and report text keeps its 68ch measure. Dark and light alike. `shell.js` and `hub.js` sync the sidebar's `aria-hidden` and the scroll lock with the breakpoint. The phone layout at 390 px is the one version 1 described: `verify.py` before and after reports 144 panels and a tightest gap of 6 px (home) both times. `shell.css` is a copy of the new theme.

### Checks at three widths
`verify.py` runs its panel checks at phone 390×844, tablet 768×1024 and desktop 1280×800: no horizontal scroll, no boxes closer than 6 px, and now no interactive target under 44 px (inline links exempt), no console error; the tablet pass confirms the drawer is still a drawer (off screen, 360 px with a backdrop when open) and the desktop pass the sidebar (300 px at the left, content from 410 px, top bar from 300 px, current item, 68ch measure, home cards and mythos/logos side by side). `--shots DIR` saves dark and light screenshots at the three widths. `generator/check_page.py` runs the same three widths and both themes with the gap and target checks, the drawer or sidebar check and the console, and ends with ALL CHECKS PASSED or FAIL. Both exclude inline elements (inline `code`) from the gap measure.

### GitHub Pages in every publish (P8)
`./deploy.sh` is the last step of every publish procedure: `skills/file-unit` (§3.8 and §5.3), `NEXT-SESSION.md`, `BACKLOG.md` (the pipeline line and job 2), `SETUP.md` §7 and §9, and the A2 and A3 specs in `docs/academy.md`, where "publish Academy" is defined as the artifact, then `deploy.sh`. The Pages site returned 404 at the start of the session (`has_pages` true, no Pages build run); rechecked after this session's deploy, see the session reply.

### The deploy script after the split (P10)
`deploy.sh` copies `kit/academy/` whole when it exists (the A2 shell plus one file per report, fetched by relative path), otherwise the single page as before; the published tree is replaced each time so files that leave the build leave the repo. Tested against a local bare remote in both shapes; run once against the live repo (nothing to deploy: the page was current). Recorded in the A2 spec.

### Data source for A3 (P9)
Decision AD5 in `docs/academy.md`: `generator/data/brand-ai/hub.py` stays the Brand + AI data file and `courses.py` only points at it; `build_hub.py` is retired at A3, `hub.py` is not. One source already read by both `load_markdown` and the hub builders A3 imports; `file-unit` §4 unchanged.

### Published
Version 45 of the site (theme v2, this changelog), to the Academy artifact and GitHub Pages; the Brand + AI hub as v6.5.

## 28 October 2026 · Session 13 · The site becomes Academy (A1), with GitHub Pages

The root home is now Academy (`docs/academy.md`, A1): it lists every course of both hubs, the two history courses and the eight to come under Personal Mythology, and Brand + AI as a placeholder course panel. No report changed and no flag was cleared. Work on Fable 5.1.

### Academy
`courses.py` gives every course a `family` (`history`, `markdown`) and adds `BRAND_AI`, a markdown course whose content is read from `generator/data/brand-ai/hub.py` at build time (courses, goals, outcomes, units, written set, audit log, next unit), so nothing on its panel is typed by hand. `build.py` builds the Academy root home (title, hero, the common rules, the Personal Mythology section with its mythos/logos text and course cards, the Brand + AI card), one drawer context per course as before, and the placeholder `#brand-ai` panel: each written unit links to its reading page on the Brand + AI hub until A3 moves the units in. `shell.js` lets a drawer item without `data-target` follow its link. `biblio.py`, `review_due.py`, `register.py` and `crosscheck.py` iterate the history courses only. `verify.py` checks the Brand + AI drawer, panel, links and the page title. Published as versions 43 and 44 with the title Academy.

### Deterministic bibliography (P5)
`biblio.py` sorts modern works by surname, year, title and name, and every locator set by a total natural key, so two builds of the same reports write identical `bibliography/` files (`git status` clean between builds; the thirteen files that drifted in session 12 no longer do).

### GitHub Pages (P7)
`deploy.sh` clones or pulls the public repo `apcanario/academy`, copies the built page in as `index.html` with a `.nojekyll`, commits and pushes to `main`. The page is served at https://apcanario.github.io/academy/ once Pages is enabled on that repo (the Pages API is refused through this session's GitHub proxy; Pedro enables it in the repo settings). `learning` stays private; the public repo holds the build output only.

## 28 October 2026 · Session 12 · The repo, five artifacts deleted, the kit docs

Housekeeping, no writing and no review (the kit work on Fable 5.1; the decisions are Pedro's, recorded in `docs/pm-status-2026-10-28.md` in the repo). No report changed and no flag was cleared. The session-11 kit never travelled: the zip handed over was session 10's (version 40, the old `shell.css`), so this session re-applied the theme to it (`cp ../design/theme.css shell.css`; `build.py` and `verify.py` pass; the three pages looked at in both themes) and restored the session 11 entry below from the live page, where it had been published.

### The repo
The kit was reviewed against the Project docs on 28 October and found to be the latest (`build.py` reproduces the site byte for byte). It now lives as `kit/` in the private GitHub repo `apcanario/learning`, beside `design/`, `docs/`, `generator/` and the vault `courses/`. A session clones the repo, works in `kit/` and ends with a commit; the zip is retired as transport. `README.md`, `BACKLOG.md` and `NEXT-SESSION.md` say so instead of "what I've attached".

### Five artifacts deleted
Pedro deleted the two standalone syllabus artifacts (Hellas Syllabus, Roma Syllabus) and the three stray draft pages (Rome 3.2, 3.3; Greek 11.6). The site's `#syllabus` and `#rome-syllabus` panels are the only published copy of the syllabi; `greek-syllabus.html` and `roman-syllabus.html` stay as build inputs. Their links were removed from `README.md`, `BACKLOG.md`, `NEXT-SESSION.md` and `SYLLABUS-CHANGES.md`.

### Doc fixes
`README.md`: the file table's `NEXT-SESSION.md` line (the review resumes at Greek 13.2 and 13.5 on the six flagged reports, not Rome 14.1) and `audits/` line (38 files, listed by audit) corrected; the design rules say the theme is changed in `design/theme.css` and copied. `provenance.json` `artefacts`: the code entry records the theme copy, the docs entry the fixes. Found in passing: `biblio.py` orders modern works that share a surname and year by set iteration, so `bibliography/<course>/unit-<n>.md` can reorder lines between builds with no change of content.

### Published
Version 42 of the site (this changelog; the page is otherwise version 41).

## 27 October 2026 · Session 11 · The site moves onto the Learning Project theme

No report written, reviewed or changed. The site's stylesheet is now `design/theme.css` of the Learning Project (the claude.ai Project that holds this course and Brand + AI), copied over `shell.css`; `build.py` and `shell.js` are unchanged, since the theme keeps every class name. Three things changed on the page: section links and every Answer, Model answer and prompt toggle are 44 px tall (they were 32); the light palette is retuned so every accent and the tertiary text reach 4.5:1 on page and card; long URLs wrap instead of widening the page. `verify.py` passes. From now on a style change is made in the Learning Project's `theme.css`, copied over `shell.css`, rebuilt and republished; see the Project's `design/README.md`.

### Published
Version 41 of the site (the theme only). The kit of this session was not handed on; session 12 rebuilt it from the session 10 kit and this entry from the live page.

## 27 October 2026 · Session 10 · Bibliographies for every report; the Greek Opus cohort; the overlap checks

Three parts, two models. The curated bibliographies ran on Sonnet 5.5 (agents, Pedro's choice for cost); the review ran on Fable 5.1. No report was written.

### Curated bibliographies, all 137 reports
One Sonnet 5.5 agent per unit group (26 groups, about 4.5 million tokens) wrote `bibliography/<course>/r-<id>.md` for every existing report to `bibliography/BIBLIO-BRIEF.md`: ancient sources with the passages the report cites, modern works completed to full references, corpora, and a Not resolved list. Web verification was thin (search returned links without text; Crossref blocked), so most modern references completed from memory are marked "(not verified)", "(partly verified)" or "(identified from context)". The files are an `artefacts` entry in `provenance.json`, flagged until Fable 5.1 spot-checks about three units. The agents also reported five apparent slips in the reports; three were real and are fixed (Rome 1.5 credited *The Genesis of Roman Architecture* to three authors, it is Hopkins alone; Greek 1.1 gave Hoeck's *Kreta* the wrong title and year; Greek 10.2 credited *Schliemann of Troy* to Calder and Traill, it is Traill), two were not (Rome 6.3's Dobbin 1995 and 10.3's Paul Davies are right; those bibliography files were corrected). Rome 4.2's unverified "(2014)" after William Murray, added in session 9, was removed.

### Greek 13.2, 13.5 and 13.4: the Opus cohort
Six-report sample (10.4, 10.9, 11.3, 11.7, 12.1, 12.6), one fresh Fable agent each on the Greek scorecard (`audits/AUDIT-BRIEF-GREECE.md`): 4.0, 4.5, 4.5, 4.1, 4.8, 4.8. The stratum mean of 4.44 clears the rule, but the two provenances inside the sample differ by half a point (unit 12 with checkers 4.8; units 10 and 11 without, 4.28), the gap sits in one dimension (dispute boxes with unnamed sides, 10.4 and 11.7 at 2 and 3), and a mechanical scan found the same pattern across the unsampled units-10-to-11 reports and almost none in unit 12. The stratum was split (`audits/greece-13.4-cohorts.md`): unit 12's six unsampled reports cleared "(sampled)"; the eleven of units 10 and 11 audited in full. Done: 10.7 (4.0), 10.8 (4.1), 10.10 (4.25), 10.11 (4.6), 10.12 (3.75, two slips, the lowest score of the review). Every erratum and revise item was applied as exact replacements under 13.5 (named sides for about thirty dispute boxes; titles for about forty modern works; six small factual slips; one new box on Rome's adoption of Aeneas in 10.12), `check.py` OK on each, and the eleven became "Opus 5.5, reviewed with Fable 5.1". The audits of 11.1, 11.2, 11.4 were cut off by an API spend limit and 11.5, 11.6, 11.8 not started; those six remain flagged.

### Rome 14.3 and Greek 13.3: the overlap checks
Mechanical first (`audits/overlap.py`, seven-word shingles and a name-Jaccard over every written pair the syllabi list: 42 Rome, 38 Greek): verbatim overlap is nil everywhere, so the question was semantic. Readers (one agent per group, `audits/OVERLAP-BRIEF.md`) then classified the later report section by section for the Rome deep-dive pairs (11.1; 13.1 and 13.2 with their Greek cross-course pairs), the seven unmeasured Rome core pairings and the six Greek pairs with the highest signal: every one of the 22 pairs passed (Rome 90 to 100 percent new; Greek 70 to 95 percent new or deeper), with 4.4 → 10.7 at the threshold. Six contradictions between Greek 6.7 and its deep dives were resolved against 6.7 and fixed (Hephaestion's pyre, Harpalus's talents, P.Oxy. 4808's year, Diodorus's distance, Callisthenes's death, the dismissal of the League allies). The six repeated Greek disputes from the 25 October crosscheck were given one home each with pointers elsewhere (`audits/greece-13.3-disputes.md`). Three pointers were added (Rome 4.5 → 11.1, Rome 1.5 → 0.3, Greek 6.7 → 11.5 and 11.7). The 32 lower-signal Greek pairs were not read.

### Published
Version 40 of the site (the three slips, the review's edits, the pointers).

## 27 October 2026 · Session 9 · Every Rome report reviewed: the sample, the capstone, the decision

The second session on Fable 5.1. Rome 14.2, 14.5 and 14.4 were run; all 59 Rome reports are off the review queue. No report was written.

### The review alert
- `review_due.py` was added at Pedro's request: it counts the complete units (both courses pooled) that still hold a flagged report and prints "FABLE REVIEW DUE" at four. `register.py` and `build.py` print its line after every registration and build, `FABLE-REVIEW.md` opens with it, and `BACKLOG.md` tells a writing session to stop at the unit boundary and say so in its first line when it fires. Tested on simulated states (three units: status line; four: due).

### Rome 14.2, twelve reports by stratified sample
- The 58 unaudited reports were split by how they had been checked: quality-pass "keep" (13), quality-pass "fix" (26) and the fresh-checker pipeline (17), the capstone kept apart. Sample: 0.1, 1.4, 1.6, 4.2, 7.3; 2.3, 3.5, 5.2, 6.4; 8.3, 9.2, 11.2. Each was audited by a fresh agent on the Rome scorecard with the brief in `audits/AUDIT-BRIEF.md`: whole report read, at least fifteen claims checked (29 to 35 in practice), every pointer opened, every self-test answered, each writer's unsure list and each earlier review's open items taken as the starting point. Scorecards in `audits/rome-14.2-r-<id>.md`.
- Scores: 0.1 4.9, 1.4 4.9, 1.6 4.8, 4.2 4.4, 7.3 4.8, 2.3 4.6, 3.5 4.6, 5.2 4.8, 6.4 4.6, 8.3 4.9, 9.2 4.6, 11.2 4.7; mean 4.72. Verdicts 8 pass, 4 revise, 0 rewrite. Four factual slips in 36,459 words: 1.4's "the literature begins about 200 BC"; 2.3's Pliny "thought Cornelia innocent" (he withholds judgement); 4.2's "more than 20,000" mercenaries (Polybius: about 20,000); 11.2's Sulla letter dated 83 (written from the East in 85 or 84). Thirty-seven errata rows in all, the rest citation sharpenings (a title and date for a modern work, a chapter for a book), two dispute boxes given their unnamed side (0.1 Timpe, 4.2 Thiel and Goldsworthy), a loose pointer (3.5 to 4.3), one place-name form (Acragas for Agrigentum) and three self-test answers brought into line with their bodies.
- 14.5: every erratum and revise item applied as an exact replacement, `check.py` OK on each (all twelve inside the band), and each entry in `provenance.json` set to "Opus 5.5, reviewed with Fable 5.1".
- The 3.5 auditor found the sides reversed in `audits/rome-14.6-syllabus.md`'s coinage row (Burnett and HN Italy hold the early date, Crawford's RRC the late one); corrected there.

### Rome 14.4, the decision
- `audits/rome-14.4-cohorts.md`. Against the Greek Fable baseline (mean 4.8, spread 4.6 to 4.9) the Rome sample's mean of the eight shared dimensions is 4.68 against 4.78, inside the baseline's own spread: noise. One systematic habit: modern works cited by surname and year with no title (nine of twelve scored 4 on citation for it). Rome's length discipline is better (+12 percent on average, all in band; the Greek core +19 with two out of band). Not found: Livy over-trusted, Greek modules retold, weaker self-tests or argument. Rome reads as if the same author wrote it.
- Strata: 4.76, 4.65 and 4.73, no report with more than one factual error, so all three met the rule fixed on 27 October (mean at least 4.4, at most one factual error per report). The 44 unsampled reports became "Opus 5.5, reviewed with Fable 5.1 (sampled)".
- Applied with the clearance: the review_notes corrections to 3.1 (Livy's sources "besides Fabius Pictor") and 6.1 (Judge's reading and the aureus of 28), and 4.1's treaty box now names Beaumont, as 1.6 does, not Walbank.

### Rome 10.5, the capstone
- Audited on its own: all 40 model answers read against their home reports (including the twelve corrected today), 35 claims checked directly, every pointer opened. 4.7, pass, no factual error; two gap-note pointers tidied (gap 7 now names Ardashir and module 7.4; gap 1 says 11.3 fills its part "once written"). The auditor's one structural note, that six Part A questions reuse core self-tests, is left for the maintainer. Off the queue: no Rome report is flagged.

### Greek corrections applied (Fable-written, no flag involved)
- 7.2's Epicurean gods box (Konstan realist; Long and Sedley idealist); 7.3's Veii statuettes "of disputed date" and the 88 BC massacre figures (80,000 in Valerius Maximus and Memnon, 150,000 in Plutarch); 9.3's Ovide moralisé early fourteenth-century; 9.4's exam allowance "about four and a quarter hours"; 6.3's 3,000 prisoners credited to Plutarch; 8.1's Q8 answer. 7.2 and 8.1 still fail `check.py` on length, as before.

### Two rules from Pedro, afternoon of 27 October
- **Length is a guide, not a law.** A topic takes the words it needs, 2,000 or 6,000. `check.py` now reports the count against the target as a note and never fails on it; `AGENT-SPEC.md`, `WRITER-BRIEF.md` and the rubric (dimension 8 no longer scores length; padding is the fault) say so. On the new rule Greek 2.1 is a 5 on style and the baseline mean 4.9; no verdict in this session changes.
- **Every unit keeps its sources and bibliography for future checks.** New `biblio.py`, run by `build.py`, extracts from every report's inline citations a per-unit list (`bibliography/<course>/unit-<n>.md`, 26 files covering all 137 reports): ancient works with locators, authors cited by bare locator, modern works with title and year, corpora and inscriptions, per report. Machine-made, so a check aid. Every new report's writer now also leaves a curated `bibliography/<course>/r-<id>.md` (`WRITER-BRIEF.md`); the unit file links to it. Curated files for the 137 existing reports were then written the same day by Sonnet 5.5 agents, one per unit group, to `bibliography/BIBLIO-BRIEF.md`; they are flagged in `provenance.json` `artefacts` until Fable 5.1 spot-checks about three units.

### Kit
- New: `review_due.py`, `biblio.py` and `bibliography/`, `audits/AUDIT-BRIEF.md`, thirteen scorecards, `audits/rome-14.4-cohorts.md`. `README.md`, `BACKLOG.md`, `AGENT-SPEC.md` updated for the alert; `NEXT-SESSION.md` rewritten to resume at Greek 13.2.

## 27 October 2026 · Session 8 · The Fable review begins: the rubric and the syllabus

The first session run on Fable 5.1. Three of the audit modules were run; no report was audited under 14.2, and no report's flag was cleared.

### Greek 13.1, the rubric
- The four baseline reports (2.1, 4.2, 6.3, 8.1) were read in full against their prompts and every checkable claim was checked. The eight-dimension rubric with 1, 3 and 5 anchors, quoted from the baselines, is in `audits/greece-13.1-rubric.md`, with the scoring rules every later audit uses and a blank scorecard.
- Baseline scores: 2.1 4.6, 4.2 4.9, 6.3 4.9, 8.1 4.8 (mean 4.8). The only low mark is 2.1's length, 45 percent over its 2,000-word target.
- Two small errata in the Fable-written baselines are logged for a later pass: 6.3 gives Plutarch's 3,000 prisoners at Aegospotami under Xenophon's citation; 8.1's Self-test answer on death pollution adds "sweeping the house", which the body does not say.

### Rome 14.6, the syllabus
- All 85 Rome prompts, why lines and unit rationales were read, every date, citation, title and count checked, and every Greek module a prompt points to opened. No factual error. The Greek unit 12 prompts and the Greek audit were read by the same method: no change. The 25 October syllabi review's changes were all confirmed in place.
- Eleven corrections applied, all pointers or wording: 1.5 points back to 0.3 for the 244 years; 3.5 marks the first silver coinage's date as disputed and points back to 1.3 for Pyrrhus as Achilles; 3.3 points to 2.5 for evocatio; 7.4 leaves the jurists' work to 9.1; 9.2 extends 3.4 on the manipular legion and points back to 6.4 for the Augustan army; 9.3 points back to 5.3 for Spartacus; 10.3 to 6.2 for the Ara Pacis; 11.2 reads "83 to 82" for Sulla's second march; 11.6 weighs 5.4's casualty figures instead of restating them; 14.3 gained a list of nine core pairings. `prompts-rome.json` was kept in step for the written modules. Findings in `audits/rome-14.6-syllabus.md`.
- The Rome syllabus, `courses.py:ROME`, `courses.py:GREECE` and the Greek deep dive III prompts are now "Opus 5.5, reviewed with Fable 5.1" and off the queue. The Rome syllabus page was republished.

### Rome 14.1, the Rome rubric
- The three Rome dimensions (source criticism, cross-reference integrity, names and forms) got their 1, 3 and 5 anchors, quoted from Rome 0.1 and 1.4, which were read in full and scored as calibration samples: 0.1 5.0, 1.4 4.9 (its one slip is the "literature begins about 200 BC" sentence already logged). Both sit at or above the Greek baseline. `audits/rome-14.1-rubric.md` has the scales, the rules and the Rome scorecard.
- `AGENT-SPEC.md` and `WRITER-BRIEF.md` were read with it: rules confirmed, two stale status lines fixed, the writers' quality-bar files set to Greek 4.2, 6.3 and 8.1. Both are off the queue.

### Kit
- The writing prompt for the 20 unwritten Rome modules became `BACKLOG.md`; `NEXT-SESSION.md` is now the review's resume prompt (resuming at Rome 14.2) and replaces `FABLE-REVIEW-SESSION.md`. New folder `audits/` holds the review's outputs.

## 25 October 2026 · Session 7 · The three checks and this changelog

The checks that session 6 could not finish, then this page.

### The checks
- Rome 10.5 (the capstone exam), 13.1 and 13.2 each had a fresh checker that had not seen it written. 10.5's checker used an exam version of the brief: coverage of units 0 to 10 and of the Greek course, every model answer tested against the reports it draws on, every pointer opened, and each of the ten gaps tested for whether it is real.
- All three came back "fix": 9 errors, 10 should-fix and 21 minor findings. Each was verified before it was applied, and all were applied.
- **13.1:** Laelius, not Scipio, recalls the talks with Panaetius (*On the Republic* 1.34). The Posidonius box gave a false reason for the *Brutus*' silence. Carneades' two speeches are cited to Lactantius, not Plutarch. Eight minor fixes.
- **13.2:** in *On Fate* 10–11 Socrates does not answer Zopyrus; his reply is in the *Tusculan Disputations* (4.80). Four minor fixes.
- **10.5, errors:**
  - The opening box described positions no answer takes.
  - One answer said every writer counted the consular colleges.
  - Another had all of Livy's sources writing after 133, but he names Fabius Pictor.
  - The twins were dated to the first written records of about 200 BC, but Callias named them about 300.
  - One follow-up prompt duplicated units 12 and 13.
- **10.5, other changes:**
  - The timings add up to four and a quarter hours, not three.
  - Slavery, named in the prompt, now has a question.
  - Two follow-up prompts were replaced.
  - Generals other than Ricimer no longer make emperors.
- All three were re-registered as "Opus 5.5". The site has no "unchecked" pills (there were 12), and the 20 queued modules keep their "next" pills.
- The checker also found slips in reports outside this session's job. They are logged, not edited: Greek 9.4's exam timings (Fable 5.1, for the Fable review), and Rome 1.4, 3.1 and 6.1.
- `NEXT-SESSION.md` now covers only the 20 modules still to write. The site was published as version 32.

### The changelog
- `CHANGELOG.md` was added to the kit, and the site gained a Changelog page built from it. It is linked from the home page and from the drawer on the home page. Each session is a card, and the newest is open.
- `shell.js` now keeps the prev and next arrows hidden on the root pages, and `verify.py` checks the changelog page.
- From now on each session sends only the kit zip; `NEXT-SESSION.md` and `CHANGELOG.md` travel inside it.

## 25 October 2026 · Session 6 · Rome units 8 to 10, Greek deep dive III, the first Rome deep dives

The biggest writing session so far: 28 reports. It stopped twice on usage limits, resumed both times, and was stopped a third time by an interruption.

### Site and tooling
- Two bugs found by the re-check at the end of session 5 were fixed. The Fable flag matched provenance keys badly in `build.py`, and `verify.py` assumed Greek 11.8 was always the last report.
- `AGENT-SPEC.md` was made course-general, with the philosophy citation conventions for both courses: Diels–Kranz, Stephanus, Bekker, *SVF*, Long and Sedley, Diogenes Laertius, Sextus, Plotinus, and Seneca, Epictetus and Marcus.
- `WRITER-BRIEF.md` asks every writer for a notes file listing its unsure claims, and a checker brief was written (`reviews/units-9-13/BRIEF.md`).
- `check.py` gained a capstone mode, `build.py` names partial syllabus entries by their flag label, and unit cards read "in progress" while partly written.
- New pipeline: every report has a writer, then a fresh checker that has not seen it written, then a maintainer who verifies each finding before applying it.

### Rome
- **Unit 8, crisis and the late empire (8.1 to 8.6):** 8.2 keep, the rest fix. 7 errors, 4 should-fix, 30 minor.
- **Unit 9, law, army and daily life (9.1 to 9.5):** all fix. 8 errors, 12 should-fix, 26 minor.
- **10.1 to 10.4, Ovid, imperial literature, Roman art and reception:** all fix. 4 errors, 9 should-fix, 10 minor.
- **Deep dive I, 11.1 and 11.2 (the assemblies, the army in politics):** 11.1 keep, 11.2 fix. 1 error, 4 should-fix and 9 minor between them.
- **10.5 (the capstone exam), 13.1 and 13.2:** written, but their checks were stopped by the interruption. They were registered as "unchecked", with an orange pill on the site. The 20 modules still to write got a blue "next" pill.

### Greece
- **Deep dive III, Greek philosophy (12.1 to 12.8):** the first Greek unit with numbered cross-references. 12.3 keep, the rest fix. 7 errors, 22 should-fix, 43 minor.
- The Greek course was complete at 78 reports. Its syllabus was republished as version 7, with unit 13's line naming unit 12.
- Two corrections to Fable-written Greek reports were found and logged for the Fable review, not applied: 7.2's Epicurean gods box has the scholars' names reversed, and 9.3 dates the *Ovide moralisé* a century too early.

### Published
- The site after each unit; version 29 carried Rome units 8 and 9, 10.1 to 10.4 and Greek 12.1 to 12.5. The last publish of the session carried the unchecked and next pills.

## 25 October 2026 · Session 5 · Philosophy in both syllabi, Rome unit 7, the quality pass

### Syllabi
- The changes planned in `SYLLABUS-CHANGES.md` were applied:
  - Rome gained deep dive III, Roman philosophy, the Stoics and Marcus Aurelius (unit 13).
  - Greece gained deep dive III, Greek philosophy (unit 12).
  - The Aeneid prompts were tightened.
  - The audits were renumbered: Rome unit 14, Greek unit 13.
- Rome now has 15 units and 85 modules (79 content, 6 audit); Greece has 14 units and 83 modules (78 content, 5 audit).
- Two facts in the plan were corrected first: Cato's Athenodorus and Augustus' Athenodorus were two men (Strabo 14.5.14), and "at Carnuntum" stands between books 2 and 3 of the *Meditations*.
- A review of the reshaped syllabi found 4 errors, 29 should-fix and 15 minor problems; all were applied.

### Rome unit 7, the Principate, AD 14 to 235
- 7.1 to 7.5, about 15,500 words. Rome stood at 39 of 79 reports, about 115,000 words.

### The quality pass
- All 39 Rome reports were read by ten fresh reviewer agents, three to five reports each, grouped by unit. None had written or seen the reports.
- Verdicts: 13 keep, 26 fix, none to rewrite. Findings: 41 errors, 62 should-fix and 106 minor. Each was checked before it was applied (`reviews/2026-quality-pass/`).
- The recurring slips became rules in `AGENT-SPEC.md`:
  - a modern book's year or title not matching the edition named;
  - an ancient author cited for what only a later one says;
  - a Self-test answer contradicting a corrected body;
  - a dispute box with one side unnamed;
  - a figure without a source.
- `crosscheck.py greece` found seven pairs of Greek reports with shared passages and six disputes told in several reports. They were logged for the Fable review.

### Published, then planned
- The site and both syllabi were published.
- A re-check of the site found two bugs (fixed in session 6). `NEXT-SESSION.md` was rewritten for Rome units 8 to 13 and Greek unit 12, with a lane note for each module listing what the written reports already hand to it.

## 24 to 25 October 2026 · Session 4 · Rome units 5 and 6, the cohesion review

### Reports
- **Unit 5, the fall of the Republic (5.1 to 5.6):** the Gracchi; Marius and Sulla; Pompey, Crassus, Cicero and Catiline; Caesar; Antony, Octavian and Cleopatra; writing in a falling Republic.
- **Unit 6, Augustus (6.1 to 6.4):** from Octavian to Augustus; the city of marble and the restored religion; the Augustan writers and their myth; empire without end.
- Fixed as they landed:
  - 5.2 was cut from 5,233 to 3,184 words.
  - Marius' equestrian family was sourced to Velleius.
  - The Clodius hand-offs were repointed to deep dives 11.3 and 11.5.
  - A false pointer to 0.1 was removed.
  - Wiseman's attribution on Valerius Cato was softened.

### Cohesion review
- `crosscheck.py` was added: it lists every cross-reference with its context, finds shared passages and flags overlapping dispute boxes.
- It was run over all Rome reports, 0.1 to 6.4:
  - Three pointers that misdescribed their targets were fixed.
  - Two duplications were given one home each (Ennius' augury; Tarquin's poppies).
  - The citation style was normalised across 13 reports.
  - "Augustus" for 29 BC was corrected.

### Planned
- `SYLLABUS-CHANGES.md` set out the philosophy deep dives for both syllabi, and `NEXT-SESSION.md` set out Rome unit 7 and a full quality pass.

## 24 October 2026 · Session 3 · Rome unit 4: Carthage and the Mediterranean

- **4.1 to 4.5:** Carthage and Dido; the First Punic War; Hannibal and the Second; Macedon, Spain and the year 146; Polybius, Cato and the Greek invasion of Rome. Each was read in full and spot-checked as it landed.
- Fixes:
  - 4.1: the Chapelle Cintas date loosened.
  - 4.2: an unverified attribution to Goldsworthy removed.
  - 4.3: Hannibal's years in Italy made consistent.
  - 4.4: a duplicated dispute box replaced by a pointer.
  - 4.5: a pointer to Greek 7.3 added.
- Confirmed with sources: Lancel's Col du Clapier, Hoyos (1985) on Philinus, and Gellius 7.4 on Regulus' sons.
- The site was published as version 24. A third stray draft page from an earlier session was found ("r-11.6") and listed for deletion.

## 24 October 2026 · Session 2 · Rome begins: syllabus, site, units 0 to 3

### Syllabus
- The Rome syllabus: 14 units and 77 modules (71 content, 6 audit), in the Greek syllabus's format, published as its own page. Its review of the syllabus itself (then 13.6, now 14.6) was added after units 0 and 1.

### The site becomes multi-course
- `build.py`, `shell.js` and `shell.css` were generalised and the courses moved into `courses.py`; the Greek output stayed the same.
- Rome got its own course home with parts, an era ribbon and a reading spine, a syllabus page and a drawer context. Its colour is `#9b5de5`.

### Reports
- **Units 0 to 3:**
  - the sources, the geography and the timeline;
  - the Iron Age peoples, the Etruscans and the founding legends;
  - the gods of Rome;
  - the early Republic and the conquest of Italy.
- 19 reports, about 55,000 words. Fixes: the Liber Linteus date (1.2) and an unverifiable Beard quotation (1.4).

### Tooling and the Fable flag
- `check.py` (structure, length band, spelling, em dashes), `register.py` (prompts index and provenance) and `verify.py` (browser checks on an emulated phone). `WRITER-BRIEF.md` for parallel writers.
- The Fable review flag: everything not written with Fable 5.1 is marked on the site and listed in `FABLE-REVIEW.md`, rebuilt on every build. Non-report material is recorded under `artefacts`.
- One consolidated kit zip with `README.md`, `NEXT-SESSION.md` (for unit 4) and `FABLE-REVIEW-SESSION.md`.

### Fixes
- The pages looked zoomed out on phones because the artifact viewer drops its own viewport tag. All three pages now carry their own, and `verify.py` checks the layout at 390 px and scale 1.
- Two writers published stray draft pages (Rome 3.2 and 3.3). `WRITER-BRIEF.md` now forbids any publishing tool.
- Greek 7.3's Veii date was flagged for the Fable review.

## 22 to 24 October 2026 · Session 1 · The Greek course, then Personal Mythology

It began on 22 October with a request for a syllabus to learn Greek history and mythology in depth, with a prompt for each topic.

### Hellas: the syllabus and the core
- **The syllabus, 22 October:** ten units and 50 modules, each with a one-line reason and a drop-in prompt, published as its own page.
- **Units 0 to 2:** twelve reports written in parallel and assembled into one tabbed page.
- **Units 3 to 6:** 37 reports, 114,729 words.
- **Unit 7:** 41 reports, 126,137 words.
- **Units 8 and 9:** ending with the capstone exam, 9.4. This finished the core's 50 reports.

### The site takes shape
- **Mobile redesign:** a fixed top bar with prev and next, and a full-height slide-out drawer grouped by unit, its units closed by default.
- **Light mode** with a sun and moon toggle.
- **23 October:** the site opens on Home, with a Continue button. A Syllabus page shows every prompt with a copy button and a link to its report.
- **The home page restructured:**
  - a to-scale timeline from 3000 BC to AD 529;
  - four parts (ground rules, myths, history, practice and legacy) plus the deep dives;
  - collapsible unit cards with progress bars;
  - "soon" rows in the drawer.
  - A drawer bug that filed 10.1 to 10.6 under unit 1 was fixed.
- **A "Next steps" page** listing the nine cultures planned after Greece.

### The deep dives
- **Deep dive I, the Trojan War (unit 10, 12 modules)** and **deep dive II, Alexander (unit 11, 8 modules)** were added to the syllabus, bringing it to 70 modules.
- Troy was written in two halves: 62 of 70 reports, about 197,000 words.
- **24 October:** Alexander, 11.1 to 11.8. The course was complete at 70 reports, about 219,500 words. A writer published 11.6 as a stray page.

### Personal Mythology
- The project was renamed and reframed as **Personal Mythology**, a personal journey towards understanding mythos and logos.
- The "Next steps" page became the root home page: a mythos and logos introduction, "How every course works", Greece as course 1 and nine cultures coming soon.
- A home icon was added to the top bar. The drawer became context-aware: courses on the home page, one course's units inside it.
- **Unit 12, a quality audit (12.1 to 12.5),** was added to the syllabus, bringing it to 75 modules.
- `provenance.json` records which model wrote each report: Fable 5.1 wrote 55, and Opus 5.5 wrote 15 (10.4, 10.7 to 10.12, all of unit 11). Each report shows its model at the foot.
- The spacing rule: at least 6 px between stacked boxes, checked by a script on all 73 pages.
- The source was packaged as a kit that rebuilds the site byte for byte, with the first handoff prompt, for Rome units 0 and 1.
