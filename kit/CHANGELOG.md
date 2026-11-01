# Changelog

Everything that has happened to Personal Mythology and, from session 13, to Academy, from the first request on 22 October 2026 to now, newest first. Each entry is one working session. It is assembled from the kit's own records (`provenance.json`, the review folders and the maintainer log) and from the session transcripts. Where a session recorded the site's version number, it is given. The exact day of each step in the first, three-day session was not recorded; its entries are in order.

## Where things stand

- **Editions and the ebook (session 38, P70, P71):** `build.py --edition greece` builds a Greece-only Academy in `editions/greece/`, `verify.py --edition greece` checks it, and `build.py --epub greece` writes an EPUB of it; neither is published. Every new course is a markdown course.
- **Reading layout (session 36, P68):** every unit and report opens on its one-line scope and reads one section at a time under a sticky bar ("Section n of N", the section menu, a progress bar, "Whole unit"); each h2 is a numbered band; Sources, the writer's opening note (a markdown unit's text before its first heading, session 37) and "How this unit was made" are closed accordions after the last section. The section last read is kept, so Continue resumes there. Theme version 6.1.
- **Figures (sessions 25 and 27):** fifteen kinds in `viz.py`: the seven for Information Architecture added by V1, four data kinds (line, bars, scatter, range) and a numeric matrix added by P44; the Figure kinds page shows one of each, sixteen figures. On a phone every figure keeps its natural size and scrolls sideways in its own frame, with a fade and a cue line. Figures added after writing (sessions 29, 30 and 32): 38 in the Brand + AI units, 180 in the Rome reports (177, then 3 written back by P57), 260 in the Greek reports, each checked by a separate Opus 5.5 agent; a Fable 5.1 check is owed (P48). Since session 31 (P55) the renderer moves or widens a label that cannot fit instead of clipping it, stops the build on what it cannot draw honestly (a year 0, a list given as a string, years BC without `years`), and `verify.py` checks the geometry of every figure on every page. Since session 37 (H-2) it draws a copy of each block and checks every block's keys, a timeline date may name a century, matrices size their columns to their contents, centred drawings open on the drawing on a phone, and object-map labels keep clear of crossings.
- **User Experience (sessions 24, 34 and 35):** a fourth track and a second markdown family, `generator/data/ux/`; its first course, IA · Information Architecture, has its frame, syllabus and briefs, IA1 (session 34, six figures) and IA2 (session 35, eight figures, the course notation every later figure uses) filed in `courses/ux/`; the course reads "in progress", 2 of 15. Its fresh checks run on Opus 5.5 until Pedro has Fable again (Fable 5.1 checks owed, row P49).
- **Greece, course 1:** complete. 78 reports, about 244,000 words: 55 written with Fable 5.1, 23 with Opus 5.5.
- **Rome, course 2:** complete, 79 of 79 reports, about 264,000 words, all written with Opus 5.5 and all checked by a fresh agent. The last 20 (11.3 to 11.6 in session 39; 11.7, 11.8, 12.1 to 12.8 and 13.3 to 13.8 in session 40) are flagged for the Fable review, due and deferred to stage 5.
- **Fable review:** every Rome report is reviewed (session 9). Of the 23 Greek Opus reports, 17 are reviewed (eleven audited in full, six cleared on the sample) and six are still flagged: 11.1, 11.2, 11.4, 11.5, 11.6, 11.8 (session 10). Rome 14.3 and the Greek 13.3 high-signal pairs are done; every pair passed.
- **Bibliography:** every report has a machine-extracted unit list and a curated `r-<id>.md` (session 10; the curated files are flagged until Fable spot-checks three units).
- **Corrections (session 33):** the figure checkers' Prose and Self-test leads were worked on 30 October: 25 Rome and 78 Greek reports corrected (`reviews/corrections-2026-10-30.md`). Faults found outside the leads wait as proposed row P61.
- **Theme and home (sessions 11 and 12):** `shell.css` is a copy of the Learning Project's `design/theme.css`. The kit lives in the private repo `apcanario/learning` as `kit/`; the zip is retired. The only published page is the site; the standalone syllabus artifacts and the stray draft pages are deleted.
- **A5 (session 23):** the Brand + AI units are read from the vault; `docs/courses-index.md` is checked by `index_check.py` on every verify; a new course of either family is a folder plus a `courses.py` entry.
- **A4 (session 22):** every course has a generated "How it was built" page: the model behind each report or unit, every check and audit with its verdict, the flags still open, the method and the sources policy. Site version 63.
- **P22 (session 21):** the two history course homes are fetched files too (`academy/<course>/home.html`); the shell is 293 KB, down from 366 KB. Site version 60.
- **P20 (session 20):** the two syllabi and the Brand + AI briefs and bibliography pages are fetched files like the reports (`academy/<course>/syllabus.html`, `briefs.html`, `bibliography.html`); the shell is 366 KB, down from 747 KB. Site version 58.
- **A2 (session 19):** the site is a shell (747 KB) plus one file per report (143), fetched when a report is opened; `personal-mythology.html` is retired and the build is `academy/`. Site version 55.
- **A3 (session 18):** the Brand + AI courses are read inside Academy (`mdcourse.py`), each with its units, briefs, build order, audits, bibliography and changelog; the standalone hub is retired. Backlog page, collapsible drawer groups, theme v3 hover states. Site version 50.
- **DD-B3 (session 17):** course B is 8 core units and 3 deep dives; Academy shows B 2 of 11. Site version 49.
- **Navigable (session 16):** breadcrumbs on every page, Start or Continue on every course page; course B is Using AI to Build a Brand. Site version 47.
- **Catalogue (session 15):** the home lists every course under its track (History, Marketing, Technology); Brand + AI is two Academy courses, A and B. Site version 46.
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
| 28 Oct | 15. The home becomes a catalogue by track (A0) | 78 | 59 |
| 28 Oct | 16. Navigable by others: breadcrumbs, start buttons, course B renamed | 78 | 59 |
| 28 Oct | 17. Course B gains DD-B3; Academy counts rebuilt | 78 | 59 |
| 28 Oct | 18. Brand + AI inside Academy (A3), the Backlog page, collapsible drawer, hover states | 78 | 59 |
| 28 Oct | 19. The split: a shell plus one file per report (A2) | 78 | 59 |
| 28 Oct | 20. The syllabi, briefs and bibliographies leave the shell too (P20); SETUP.md off the zips (P21) | 78 | 59 |
| 28 Oct | 21. The history course homes leave the shell (P22) | 78 | 59 |
| 28 Oct | 22. "How it was built" for every course (A4) | 78 | 59 |
| 28 Oct | 23. The vault is the source; a new course is a folder (A5) | 78 | 59 |
| 1 Nov | 39. Rome batch 1: 11.3 to 11.6 (R-1) | 78 | 63 |
| 1 Nov | 40. Rome complete: 11.7, 11.8, 12.1 to 12.8, 13.3 to 13.8 (R-2) | 78 | 79 |

## 1 November 2026 · Session 40 · Rome complete: 11.7, 11.8, 12.1 to 12.8, 13.3 to 13.8 (R-2)

Backlog row R-2 of `docs/BACKLOG.md`, Part A, one chat, Opus 5.5 throughout (P31): each module written by its own fresh agent that saw only its writer's material; each fresh check by a separate agent briefed with `reviews/units-9-13/BRIEF.md` that had not seen the writing or the writer's reply; each module's figures checked by another agent given only the text with its figures taken out, the captions and the figures as drawn at desktop and in 390 px phone frames, dark and light, with a new agent for each re-check; at most eight agents at a time; this chat only filed. Every finding was verified before it was applied as an exact replacement; the maintainer log (`reviews/units-9-13/log.md`) has a paragraph per module. The four figure lessons of R-1 went into `BACKLOG.md` first. `review_due.py` printed FABLE REVIEW DUE throughout; the review is deferred to the Fable stage (Pedro, 31 October 2026), and the count stands at 20.

**The modules** (words after fixes; fresh check: errors, should-fix, minor; figures kept).
- 11.7 The Ides of March: 4,390; fix (4, 2, 5); the source matrix (the flow of the Ides dropped after three failed checks).
- 11.8 Why the Republic fell: 3,523; fix (1, 5, 4); the ancient matrix and the modern timeline (Flower's timeline dropped). Written last in its unit.
- 12.1 Virgil and the making of the poem: 3,741; fix (1, 4, 5); the life timeline and the making flow (the pairing matrix dropped).
- 12.2 Books 1 to 6, the Odyssean Aeneid: 4,842; fix (2, 2, 4); the book matrix and the games matrix (the route of book 3 dropped).
- 12.3 Books 7 to 12, the Iliadic Aeneid: 5,596; keep (0, 0, 8); none (both matrices dropped).
- 12.4 Dido: 4,725; fix (2, 4, 5); the flow and two matrices (the reception timeline dropped).
- 12.5 Book 6, the underworld and the parade of heroes: 5,287; fix (2, 2, 10); the parade flow and the route flow (the matrix against *Odyssey* 11 dropped).
- 12.6 The gods of the Aeneid: 3,749; fix (1, 5, 6); the flow and the tree. Written after 13.2.
- 12.7 Augustan or anti-Augustan?: 3,162; keep (0, 3, 3); the critics' timeline (the test-case matrix dropped).
- 12.8 The Aeneid after Rome: 3,872; fix (3, 3, 5); the English flow and the twentieth-century timeline (the reception matrix dropped).
- 13.3 The rival schools at Rome: 3,863; fix (3, 5, 6); none (the schools matrix and the timeline dropped).
- 13.4 Cato and the Stoic opposition: 3,589; fix (3, 4, 10); the tree and the timeline.
- 13.5 Seneca: 4,246; fix (2, 2, 4); the flow of his death (the timeline dropped).
- 13.6 Musonius Rufus and Epictetus: 3,503; keep (0, 1, 4); the timeline, the tree and the flow.
- 13.7 Marcus Aurelius, a life: 4,122; fix (2, 4, 6); the tree and the timeline (the revolt flow dropped).
- 13.8 The Meditations and the afterlife of Roman Stoicism: 3,312; fix (1, 2, 8); the flow and the tree (the timeline dropped).

**Units closed.** Units 11, 12 and 13 each closed with `crosscheck.py` over the unit and every pointer opened against its target: 11.7's Sedley box became a pointer to 13.3, and 12.4's paragraph retelling 4.1's Dido became a one-sentence pointer. Logged for others and not applied here: Rome 7.2 cites Dio 66.13, which exists only in Boissevain's numbering; 13.5's Dio 61(62).12.1; Greek 10.12 dates Otis's *Virgil* to 1964 where the Clarendon title page has 1963 (both circulate); the renderer notes the figure checkers raised (bars and captions past a phone frame, tick overlaps, the year-0 scale, faint connectors, light-mode contrast of span labels, wide desktop timelines) go to P83 and P84.

**Rome is complete:** 79 of 79 content reports, about 264,000 words, all Opus 5.5. `ROME['next_up']` is empty and Rome's status is available. Academy rebuilt, verified (ALL CHECKS PASSED, both builds) and published; GitHub Pages deployed once at the end. Part B of R-2, P71-3 (Greece and Rome to Markdown), stays in the queue.

## 1 November 2026 · Session 39 · Rome batch 1: 11.3 to 11.6, with P78, P79 and P80 (R-1)

Backlog row R-1 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout (P31): each module written by its own fresh agent that saw only its writer's material; each fresh check by a separate agent that had not seen the writing or the writer's reply; each module's figures checked by another agent given only the text with its figures taken out and the figures as drawn at 390 px and desktop; this chat only filed. Every finding verified before it was applied as an exact replacement. The maintainer log is `reviews/units-9-13/log.md`.

**The modules.** 11.3 Politics in the street (4,331 words; fresh check: 2 errors, 3 should-fix, 2 minor; four figures, three fixed once). 11.4 Women and the late Republic (3,964; 2 errors, 6 should-fix, 6 minor; three figures, the timeline dropped after two failed checks and restored with the fixes on Pedro's word, then passed). 11.5 Cicero through his letters (4,745; 2 errors, 8 should-fix, 5 minor; three figures, two dropped after two failed checks and restored with the fixes on Pedro's word, then passed). 11.6 Caesar's Commentaries and Gaul (5,100; 1 error, 5 should-fix, 4 minor; three figures, two fixed once). All four registered "Opus 5.5" and filed in the vault (`courses/rome/`); `crosscheck.py` over the four checked every pointer among them and back to 11.1 and 11.2, and replaced one retold anecdote (Posidonius' reply, 13.1's) with a pointer. `review_due.py`: FABLE REVIEW DUE at 4 of 4, deferred to the Fable stage (Pedro, 31 October 2026). Rome 63 of 79.

**P78.** The objects reading-direction mark is a narrow isosceles triangle, 14 units from base to tip and 6 across. On a level line it sits at the label plate's right end; on a slanted or vertical line it sits on the line itself, 12 units past the plate on its object's side (4 on a short line), so the line runs on both sides of it. A hard case on the Figure kinds page draws two marks on slanted lines. Three fresh figure-checks of IA2's cross-surface map: the first found the vertical mark off its line at the drawing's edge; the second found the slanted mark where the plate cut its line, reading as an arrowhead pointing back; the third passed both.

**P79.** A tree's svg carries `data-xr`, its root box's right edge plus 8, and `shell.js` opens a phone frame no further left than puts the root in view, so the Greece home's Hesiod tree opens on Chaos and the Olympians, not on empty upper rows. `verify.py` checks that every tree wider than its 358-unit phone frame opens with its root whole and a lower box in view.

**P80.** `EDITIONS` entries may carry `rules`, their own text for a "How every course works" line that names a course they do not hold: the Greece edition's "One unit per chat" line says nothing of Brand + AI. The full Academy's home is byte for byte unchanged. The Greece edition is published as its own private artifact, "Academy · Greece" (its URL in `docs/academy.md` and `EDITIONS['greece']`); it has no Pages repo.

## 1 November 2026 · Session 38 · Method, skills, errata and builds (H-3: P51, P37, P46, S3, P74 to P77, P70, P71)

Backlog row H-3 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout. Every erratum was drafted by a fresh agent and checked by a second fresh agent before it was applied (exact replacements, the current text occurring once); every changed figure was then checked by a fresh figure-checker given only its unit's text with the figures taken out and the figure as drawn at 390 px and desktop, and each FIX re-checked by a new agent (P31).

**P51.** `AGENT-SPEC.md`'s element list names the figure declaration, `<figure class="viz" data-viz="…"><script type="application/json">…</script><figcaption>…</figcaption></figure>`, the only script allowed.

**P37, P46.** `skills/write-unit`, `audit-units` and `file-unit` take a markdown course's folders from its `kit/courses.py` entry (`vault`, `data`, audits in `audits/<id>/`) and its sourcing part from `sourcing_part` (Part 2 when absent); §3b's fresh-check prompt is now for any markdown course. A fresh agent read the three against `courses.py`: two placeholders unresolved (the audit errata, the commit message's course), both fixed; `method.md` §4, §5 and §7 and `audits/README.md` aligned. Every skill description is 200 characters or fewer (185 to 198), PyYAML clean.

**S3.** `review_due.py` counts content modules written since the last review, Greece and Rome pooled, four to a review; the six Greek reports the 27 October review left to S4 are carried by `review_mark` in `provenance.json`. It prints "Fable review: 0 of 4 modules written since the last review." The batch plan is in `BACKLOG.md`; the index keeps one Personal Mythology counter.

**P74, P75 · IA2.** The notation gains the reading-direction mark: §5.2 (Lines, Labels), the legend and the notation sheet say a label that cannot read left to right or top to bottom carries a small triangle pointing at the object it reads towards. The legend's Screen row says a button is a control, its Surface: Label row says lower case, a row says nothing is drawn dashed, and its caption names WCAG 2.2, 1.4.1 and says the tones were added. The cross-surface map: a search of every grid up to 4 by 4 found one-crossing layouts but none with every label 14 units clear, so it is drawn on a two-crossing grid with every label clear, two links marked; its surface-to-surface labels are verbs from IA1's "what crosses" table (the paragraph before it changed with them), the object lines carry 0..* and 1, the approval reads [over the limit], and its caption names F1 (section 1.10), the tones and where each part comes from. The figure-checker misread the slanted mark's direction; the data is right and the mark's shape is proposed as P78.

**P76.** All sixteen figures H-2's checkers questioned were brought to their units' text: IA1 figure 2; Greece 2.2, 4.1, 8.4, 8.5, 9.1 (two), 10.2, 12.2, 12.6; Rome 2.1, 4.1 (two), 4.2, 6.1, 7.3. 27 replacements, then 7 more from the figure checks (a caption saying what a tone or a blank means, "Throat", "Payment", Euripides' titles in full); every figure PASS. No finding needed a prose change.

**P77 · DD-B3.** The "Evidence grades" paragraph moved, words unchanged, to the top of §1.0; a fresh agent found one sentence that counted it among the opening's limits, now "Two limits shape this unit, and they are stated once here."

**P70 · editions.** `courses.py` gains `EDITIONS`; `python3 build.py --edition greece` writes `editions/greece/` (Greece only; no Changelog, Backlog, "How it was built", build pages, Figure kinds or planned courses; a link into a missing page is plain text, a button or row to it is dropped) and `verify.py --edition greece` runs the same checks on it: ALL CHECKS PASSED. The full Academy builds byte for byte as before (compared before and after). A fresh agent on the edition's screenshots found an empty planned row in the drawer (fixed) and the Hesiod tree opening blank at 390 px (in the full Academy too; P79).

**P71 (1) and (2).** Every new course is a markdown course (`method.md` §2 and §7, `skills/new-course`). `python3 build.py --epub greece` writes `editions/greece.epub` (`epub.py`): 78 reports in syllabus order, each with its Sources, no process notes, 260 figures drawn by `viz.py` with the theme's light styles written into each SVG, the stylesheet cut from `design/theme.css`, the theme's fonts embedded. EPUBCheck 5.3.0: no errors or warnings.

## 1 November 2026 · Session 37 · The figure renderer (P52, P63, P50, P53, P66), and two reading-page rows (P72, P73)

Backlog row H-2 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout. Renderer only: the two figure declarations the rows name are the only unit files edited (Greek 5.4's revolt event; IA2's cross-surface map, whose grid stands, see P66). Every changed unit figure was checked by a fresh Opus 5.5 agent (P31) given only the unit's text and the rendered figure: 66 checks over 46 figures, record in `reviews/h2-figure-checks.md`.

**P52 · render on a copy.** `viz.render` draws a deep copy, so its working keys (`_t`, `_h` …) never reach a unit. `viz.VIZ_KEYS` documents every kind's keys at every level, and `verify.py` reads every ```viz block in the vault, every history figure declaration, every course home figure and every examples block against it (531 blocks, none undocumented); the examples page's timeline fields now list `date`.

**P63 · a date by century.** A timeline event's `date` may name a century or a span without its year ("mid-seventh century", "late eighth century BC", "c. 670–640"), printed as written and drawn at `at`, which must lie inside it (`viz.date_names`), or the build stops. A hard case and a block that stops the build on the Figure kinds page; `verify.py` checks every built date line against the year its dot stands at. Greek 5.4's revolt now reads "mid-seventh century" over "Revolt", with no year the text does not give.

**P50 · centred drawings open on the drawing.** Sitemap, objects, decision, states and wireflow carry `data-x0` where their drawing starts, so a phone frame opens on it; the left fade shows only past that point. `verify.py` checks every such figure.

**P53 · matrix columns sized to their contents.** Each column is as wide as its widest cell or header, not a share of the 700-unit width; a narrower matrix draws at its own width (theme 4i `.viz-fit`). From the checks: row labels to 240 on one line; headers and labels take what the columns leave; long columns share in proportion; wrapped text balanced, so no word sits alone; a wrapping label column keeps only its balanced width; width moves to a wrapping column when it costs no other cell a line; a header keeps its longest word whole (a word breaks after its hyphen first); a matrix with too many columns takes each column's narrowest unbroken width. A3 §6 draws at 373 units, B3 §5 at 498, A1 §6 at 523.

**P66 · object maps.** Every line is drawn before any label; each label sits on its own line, at least 14 units clear of every crossing, other line and placed label, or the build stops. A link may carry `"dir": "to"` or `"from"`, a small solid triangle at the end of its label pointing at the object it reads towards (a hard case on the Figure kinds page). IA2's cross-surface map: an exhaustive search of grids up to 6 by 3 and 4 by 4 found none with fewer than three crossings that keeps the reading rule IA2's text and caption state, so the map keeps its grid and its labels now sit clear of the crossings; fewer crossings needs the direction mark in IA2's notation (proposed P74).

**P72 · reading-page polish.** A history report's eyebrow wraps by whole segments ("GREECE · UNIT 5 ·" / "THE ARCHAIC AGE, 800 TO 480 BC ·" / "5.4 · 2,796 WORDS"); its course and unit labels reach 6.5:1 or more in the light theme; a URL written out in a Sources list wraps after its slashes and before its dots (`mdcourse.url_breaks`, theme 9).

**P73 · the writer's opening note.** A markdown unit's text before its first heading leaves section 1 and is read at the end, in a third closed accordion, "The writer's opening note" (`#<pid>-note`), between Sources and "How this unit was made", linked from the section menu; a deep link lands and opens it. A rule in `mdcourse.reading`; `verify.py` checks it (12 units with an opening, each with its closed note; IA1 and IA2 without, none shown). A fresh agent read the twelve openings: eleven are method; DD-B3's is mixed (its three grades frame the unit), listed for Pedro, not moved.

**Theme 6.1.** 4i: `.viz-fit`, no ligatures in figure text, base-width timelines and flows fit the desktop frame; 4a: eyebrow segments and the light-theme label colour; 9: Sources wrap at break points. `shell.css` copied from `design/theme.css`.

**Checks.** `verify.py`: figure keys, opening notes, centred drawings and date lines added; ALL CHECKS PASSED. Screenshots of m54, read-ia2, read-a3, read-b3 and read-b4 and the Figure kinds sheets looked at, phone and desktop, dark and light. Academy published to its artifact and to GitHub Pages, carrying H-1's backlog and changelog pages too.

## 1 November 2026 · Session 36 · The reading layout (P68), and screenshots of long units (P35)

Backlog row H-1 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout. Formatting only: no file in `courses/` and no history report in `kit/greece/` or `kit/rome/` changed. One fresh Opus 5.5 agent (P31), which had not seen the layout built, checked the screenshots against P68's spec.

**P35 · screenshots of long units.** `verify.py --shots` no longer renders the whole page before clipping it: the viewport is made 2,600 px tall, captured as it is and put back. DD-B3's phone shot took 80 s (and longer pages failed past the timeout); it now takes about 1 s.

**P68 · the reading layout, every unit and report of every course.** One rule in the renderer (`mdcourse.reading`, called by `mdcourse.py` for the markdown courses and by `build.py` for the history reports; stepping in `shell.js`; theme section 9), no page-level edit:
- *Content first.* The page opens on the title and the one-line scope (the unit's `units_data.py` scope; a history report's syllabus line), then section 1. The provenance paragraph that used to open a markdown unit, the old section chips and the history reports' "Written with" line and prompt are gone from the top.
- *One section at a time.* A sticky bar under the top bar: "Section n of N" over the section's title, a progress bar, and the section menu (every section, then Sources, How this unit was made and the "Whole unit" toggle). Each section ends on Previous and Next; the last ends on "End of the unit". The section last read is kept per page, so Continue, a drawer item or a reload reopens it there; a deep link to a section (`#m54-3`, `#read-ia2-2`) or to an accordion (`#m54-sources`, also on a fresh load) shows it first. "Whole unit" shows every section for search, and print always shows every section. Still one fetched file per unit.
- *Section bands.* Each h2 is a full-width band on a tint of the course colour with its place as a numeral (01, 02 …); a heading "Deliverable · X" shows "Deliverable" as a kicker over X; a bare section number equal to the place is shown once, as the numeral. h3 lighter (600).
- *Process last.* After the last section: Sources (a markdown unit's Sources list; a history report's curated bibliography, `bibliography/<course>/r-<id>.md`), then "How this unit was made" (the provenance paragraph or "Written with" line, the writer's unsure list, the fresh-check line, taken out of the unsure list where the writer put it there, a history report's checks and audits with their verdicts, and the brief or prompt with its copy button), both closed. The next-unit cards come after them and now say "Previous unit" and "Next unit".
- Text that stands before a unit's first heading (DD-B3's and B4's openings, for example) is the unit's own text and opens section 1, before its band.
- Wide tables get the figures' fade and a "scroll sideways for the whole table" cue. The top bar is more opaque (0.94), so text no longer shows through it.

**Found on the way.** A bracketed placeholder in running text (B4's `| <code> ·`, A3's `<journey>`) reached the page as an HTML element: hidden, and B4's unclosed `<code>` set the rest of its deliverable in monospace. `mdcourse.render_md` now escapes a bracketed word that is not inline HTML, or an element opened or closed without its pair in the paragraph, outside code; the two placeholders now show as written, and no other unit's text changed (rendered text compared before and after).

**Checks.** `verify.py` gains the reading checks: on all 152 units and reports (1,581 sections) the order header, bar, text, accordions; no process text before the text; each section reached by next, by previous and by the menu, with "Section n of N" and the progress bar right at each; the accordions and next-unit cards hidden before the last section and closed at it; "Whole unit" on and off; Sources opened by the menu's link and by the end-of-unit link; on one page per course a deep link to a section and to Sources on a fresh load, and Continue and a reload resuming at the section last read. The panel checks measure a reading page whole, so every section is still measured (529 figure frames, as before). `--shots` of a `--page` reading page adds the states its top does not show (the menu, the end of section 1, section 2, the end of the last section, both accordions open, "Whole unit"). The fresh checker's gaps were fixed in the renderer: process and next-unit cards at the end of every section (now after the last only), the bar's title cut to a few characters on a phone (the toggle moved into the menu; the title has the bar's width), a doubled coloured rule over each band, low contrast on the bar's count and the accordion counts, next-button labels breaking, unlabelled unit cards, tables with no scroll cue, and the light-theme shots opening on the section last read. `verify.py` ALL CHECKS PASSED. Academy published to its artifact and to GitHub Pages.

## 30 October 2026 · Session 35 · IA2 written and filed (N7)

Backlog row N7 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout. The writer and the checker were each a fresh Opus 5.5 agent (P31), the checker never seeing the writing or the writer's report; this chat only applied, built and filed.

**N7 · IA2.** *The shapes IA takes: the artefact catalogue and the course notation*, written by an isolated agent that saw only its brief (the User Experience Briefs page: PRE with the course goal, then IA2's brief), `skills/write-unit`, `sourcing-standard.md` Parts 1 and 4, the figure kinds in `viz.py` and the filed IA1; search off, used only to verify editions, chapters, dates and URLs. About 9,200 words before Sources, the two deliverables and the example tables included (the brief's range is 2,000 to 6,000; row P67); eight figures (the notation legend as a matrix, a sitemap, two object maps, a wireflow, a decision tree, a state diagram, a service blueprint in swimlanes); deliverables: the course notation sheet and the artefact decision table. Fresh check (`skills/audit-units` §3b verbatim, with the figures paragraph; Part 4 for Part 2, the UX brief and the course's unit list from `units_data.py`, no errata, pointers checked against IA1) by a second isolated agent: fix, 3 errors (three figures that read backwards or carried labels the text lacked), 10 should-fix, 17 minor; report saved verbatim at `audits/ux/fresh-check-IA2.md` before anything was applied, then all 30 applied as exact replacements, each `Current:` found once. The decision table's "unit that builds it" column, left as placeholders by the writer (the course's unit list was not among its inputs), was filled by the checker's fix from `units_data.py`. Filed at `courses/ux/IA2-the-shapes-ia-takes-the-artefact-catalogue-and-the-course-notation.md`; `hub.py` v3 (reading page `read-ia2`, IA2 written, IA3 next, Audit 1 counter 2 of 4, deferred); `courses-index.md` row.

**Figures fixed by eye.** The checker's two replacement object maps failed the build's figure geometry at phone width (counts drawn over boxes, labels over labels). Both fixed by moving boxes in their declarations, labels and captions unchanged and every relationship still reading left to right or top to bottom: the Admin object-relationship map to a three-row grid with no crossing lines; the cross-surface map to a four-row grid (three crossings is the least any grid allows with its reading rule) with the links whose labels sit on a crossing drawn last, so their plates mask the line beneath. One drawing fix in `viz.py` (`objects`): a count on a slanted line that would fall on its own box moves to the other side of the line. One fault left: on the cross-surface map, Admin's "sets" to policy sits where that line crosses "submits" (row P66).

**Build.** `verify.py` ALL CHECKS PASSED. `--shots` with `--page read-ia2`; IA2's page and its eight figures looked at at 390 px and desktop, dark and light: every figure scrolls in its frame with the cue on a phone. Academy published to its artifact and to GitHub Pages.

## 30 October 2026 · Session 34 · IA1 written and filed (N6), and the body faults outside the corrections pass (P61)

Backlog rows N6 and P61 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout (P61 confirmed by Pedro 30 Oct 2026, 16:51, to run with N6). Every writer, fixer, checker and figure checker a fresh Opus 5.5 agent (P31), at most eight at a time, a checker never seeing the work it checked being done or the report of the agent that did it; this chat only applied, built and filed.

**N6 · IA1.** *What information architecture is, and where it sits*, the first unit of course IA, written by an isolated agent that saw only its brief (the User Experience Briefs page: PRE with the course goal, then IA1's brief), `skills/write-unit`, `sourcing-standard.md` Parts 1 and 4 and the figure kinds in `viz.py`; search off, used only to verify editions, chapters, dates and URLs. About 5,500 words before Sources; six figures (tree, two matrices, timeline, swimlanes, objects); deliverables: a one-page definition sheet for a product team and the Perqo surfaces map. Fresh check (`skills/audit-units` §3b, verbatim, with the figures paragraph) by a second isolated agent that had not seen the writing: keep, 0 errors, 4 should-fix, 7 minor, all applied as exact replacements; report `audits/ux/fresh-check-IA1.md` (a Fable 5.1 fresh check is owed, row P49). Filed at `courses/ux/IA1-what-information-architecture-is-and-where-it-sits.md`; `generator/data/ux/hub.py` v2 (reading page `read-ia1`, IA1 written, IA2 next, Audit 1 counter 1 of 4, deferred); the course's status in `courses.py` from coming soon to in progress; `docs/courses-index.md` updated.

**P61.** The body faults `reviews/corrections-2026-10-30.md` listed outside its leads, 24 reports: one fresh fixer per report (its report, its items, `AGENT-SPEC.md`, `WRITER-BRIEF.md`, and the reports it cross-references), a fresh checker per report on each replacement (PASS or FAIL; a figure edit had to draw), only PASSes applied with `check.py` and `register.py`, models unchanged; changed figures through P58's figure check. 16 reports corrected with 33 replacements (Greek 1.1, 2.2, 2.4, 4.2, 4.5, 6.6, 7.3, 9.3, 10.3, 10.10, 11.4, 11.8, 12.2; Rome 2.5, 5.4, 7.4); four figures changed (Greek 1.1, 2.4, 6.6 passed the figure check; 9.3 passed after one FIX); 9 items not real (the three "nine-question" Self-tests already had ten; the cross-references held); one proposal failed its check: Greek 5.4's revolt "in the mid-seventh century" still prints 650 BC, since a date line must carry the event's year (proposed row P63). Record: `reviews/corrections-2026-10-30-p61.md`; `provenance.json` artefact and review note.

**Build.** `verify.py` ALL CHECKS PASSED. `--shots` with `--page` for `read-ia1` and the 16 changed reports; IA1's page and its six figures and the four changed report figures looked at whole at 390 px and at desktop: every figure scrolls in its frame with the cue on a phone and fits the column on desktop; nothing to fix. Academy published to its artifact and to GitHub Pages.

## 30 October 2026 · Session 33 · The six drawing faults (P58), corrections from the figure checkers' leads (P54, P59), and hidden answers in the write-unit skill (P60)

Backlog rows P60, P58, P54 and P59 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout; every fixer, checker and re-checker a fresh Opus 5.5 agent (P31), at most eight at a time, a checker never seeing the work's reasons; this chat only applied, built and filed. Specs rendered from copies (P52).

**P60.** `skills/write-unit` §4b gains one line, **Hidden answers**: no figure draws what a Self-test or exam hides in `<details>`, since a figure sits at the top level and would show the answer under its question; an exam's figures draw only what its visible questions give. Nothing else in the skill changed; the skill zip was rebuilt for re-upload.

**P58.** The six faults the Greek checkers met (`reviews/p43-greece-notes.md`, Drawing), fixed under P55's rule that a label moves or the drawing widens and is never clipped or cut. Each has its contract in `viz.py`'s docstring, a hard case on the Figure kinds page (now 14 hard cases) and a `verify.py` check, run on every built figure (`figure rules (P58)`), that fails the build on the old drawing:
- *Range, a row whose low equals its high:* drawn as a point (a diamond), its value printed once with its sources joined in one tag; end labels are tried inward, centred on their ends, meeting in the middle, then the high one a line lower, and each sits under the value it names. Check: no value printed twice in a row; each end plate spans its end.
- *Timeline, wrapping:* "c.", "ca.", "by", "after", "before", "from" and "until" are glued to the number after them, so a wrap never parts them. Check: no wrapped line ends in one of them with its number on the next.
- *Timeline and range, dates:* an event may carry `"date"`, the text its date line prints ("c. 600", "476/5", "from 7 BC on"); it must contain the event's year and keep to the figure's notation, or the build stops. A figure may set `"era": "BCE"` to print BCE/CE. Checks: a date line that drops a "c." or split year its label keeps, a label that marks its date "(c.)" because the date line cannot, and BC/AD in a figure on a page whose prose writes BCE.
- *Objects, a link label in a narrow gap:* the gap widens to the label's longest word (and a box narrower than 110 widens the drawing, which scrolls); a diagonal link never wraps narrower than its longest word. Check: every link label drawn whole.
- *Range, word units:* a value of 1 takes the singular ("1 head"; `"unit_one"` where the singular is not the unit less its s, else the build stops). Check: no "1 <word>s".
- *Tree, a one-child chain:* a tree narrower than its frame is centred. Check: narrow trees centred.

Redrawn: of the 483 report figures, 67 drew differently with the new renderer before any data changed (26 trees centred, 23 ranges, 17 timelines, 1 objects figure). Figure data changed only where a checker's note named the figure or a label repeated its date only to keep the "c.": 66 figures in 54 reports, each event's approximate or split year moved from its label into `"date"` (Greek 3.1 also to BCE). Greece (48 figures): 0.1 1 and 2; 0.3 2 and 3; 1.2 1 and 4; 3.1 2; 3.3 2; 3.5 3; 3.7 1; 4.3 4; 4.5 4; 5.1 1, 3 and 4; 5.2 3; 5.3 1 and 4; 5.4 1; 5.5 3; 5.6 1 and 3; 6.1 1 and 3; 6.2 1 and 3; 6.3 1; 6.6 1; 6.7 1; 7.1 4; 7.2 2; 8.4 2; 9.1 2 and 3; 9.2 1 and 3; 10.2 4; 10.3 2; 10.4 3; 10.5 3; 11.1 1; 11.3 2; 11.7 3; 11.8 2; 12.3 1; 12.4 1; 12.6 1; 12.8 2. Rome (18): 0.1 2; 0.2 2; 1.1 3; 1.5 1; 1.6 1 and 3; 2.4 4; 3.3 2; 4.4 3; 4.5 1; 5.2 2; 6.4 2; 7.3 3; 7.4 3; 8.1 2; 9.2 2; 9.3 4; 10.4 1. Each changed figure was checked against its report's text by a fresh agent: 62 passed, 4 got a FIX (Greek 6.2 and 11.7, Rome 1.5 and 4.4), all four passed the re-check; none dropped, none failed twice. After each report `check.py` printed no HARD line, its word count did not move and its prose with the figures removed was byte-identical. Two captions that described the old labels were brought into line by eye (Rome 1.5 "(c.) marks a date…" removed; Greek 12.8 "kept in the labels" now "kept"). 10.9's regridded objects figure left as it was.

**P54 and P59.** The corrections pass on the Prose and Self-test leads of `reviews/p43-rome-notes.md` and `reviews/p43-greece-notes.md`: one fresh fixer per report with leads (it saw only its report, its leads, `AGENT-SPEC.md` and `WRITER-BRIEF.md`; a Self-test answer that said more than the body was fixed in the answer; a lead needing a source was searched, and left if unsettled), then a fresh checker per report on each replacement, PASS or FAIL; only PASSes applied, with `check.py` and `register.py` (report models unchanged). Rome: 28 reports with leads, 25 corrected, 32 replacements applied, 2 failed the check, 8 leads not real or out of scope. Greece: 78 reports, all corrected, 394 replacements applied, 27 failed the check, 91 leads not real or out of scope, 6 unsettled (cross-references the fixer could not open). No figure changed in this pass. Report by report, with the faults found outside the leads (Greek 7.3's OGIS 338 box, 11.4's Aornos, 11.8's Sarapis date, 9.3's figure step, 10.10's Troy II answer, three Self-tests with nine questions, and others): `reviews/corrections-2026-10-30.md`, recorded in `provenance.json` (an artefact entry and a review note), so in `FABLE-REVIEW.md`.

**By eye.** `--shots` with `--page` for the Figure kinds page and the 84 report pages whose figures drew differently (119 figures), every changed figure looked at whole at 390 px and at desktop. Two faults found and fixed in the renderer, each with its contract, a hard case and a `verify.py` check: (1) a centred tree (fault 6) opened on a phone on the empty margin of its 700-unit drawing, so a tree's svg now carries `data-x0`, where its drawing starts, and `shell.js` opens a scrolling frame there (P50 can give the other kinds the same); (2) a timeline stem ran through a neighbouring event's date or label where two events sit a few years apart beside a wide label: 6 report figures before P58, 8 after its date texts (Greek 0.3, 5.2, 5.5, 5.6, 6.6, 8.3, 10.2, 11.8; Rome 0.3) and the Figure kinds page's "Labels at the edges". Now every direction of the events caught is tried, then the drawing widens until no stem crosses a label (Greek 0.3 figure 2, 5.2 figure 3 and 11.8 figure 2 and Rome 0.3 figure 1 widened and scroll); `verify.py` fails any stem through another event's text, and finds none. Left as the checkers passed it: Greek 11.7's Syriac Alexander Legend dated "c. 630" under AD ticks (the report's wording). Built; `verify.py` ALL CHECKS PASSED, the figure rules reading 515 built figures with no fault, and again after the shots. Academy published to its artifact and to Pages; proposed rows P61 (the faults the corrections pass found outside its leads) and P62 (the stale branch `n5-p57-wip`, whose delete this session refused).

## 30 October 2026 · Session 32 · Figures in the Greek reports (P43), and the Rome figures put back (P57)

Backlog rows N5 (P43, Greece) and P57 of `docs/BACKLOG.md`, one chat, Opus 5.5 throughout; every adder, checker and re-checker a fresh Opus 5.5 agent (P31) seeing only its report, `viz.py`'s docstring with the P55 contract and `skills/write-unit` §4b, a checker never the adder's report; this chat only applied, built and filed. Specs rendered from copies (P52). After each report `check.py` printed no HARD line, the word count did not move and the prose with the figures removed was byte-identical to the original.

**N5, Greece.** The figure pass run over the 78 Greek reports, rolling, at most eight agents at a time: 78 adders, 78 checkers, 62 re-checkers. 266 figures proposed, 166 passed the first check, 95 got a FIX, 94 of those passed the re-check; 6 dropped. Kept, 260. By kind: timeline 98, flow 66, tree 33, matrix 22, range 19, compare 12, decision 5, objects 3, bars 2. By unit: 0 8, 1 11, 2 19, 3 19, 4 19, 5 21, 6 25, 7 15, 8 15, 9 14, 10 45, 11 22, 12 27; every report has at least one (8.1 one, most four; the per-report counts are in `provenance.json`). Dropped: 7.2's timeline of the schools, after failing twice (its caption called the Cynics a school, which the text above it denies); on the checker's verdict, 2.6's Typhon tree (it repeats the report's own genealogy), 8.1's chain of the four nested levels (no tree shape, and it draws the strict model the text qualifies), 9.4's range and timeline (9.4 is a closed-book exam: each drew a model answer hidden in its Self-test, and a figure cannot sit inside the hidden block), 12.7's scale of tension (a sentence redrawn as a succession the text does not state). The Greek course home's figure unchanged. One figure changed by eye after `verify.py` failed it: 10.9's objects figure of the theomachy, whose link label "concedes without a blow" was cut mid-word in the narrow gap between two columns and ran out of the drawing; its grid now puts each pairing in a column so the links run vertically (no label, box or link changed). `provenance.json`: report models unchanged; new `artefacts` entry `greece figures (P43)`, "Opus 5.5, checked with Opus 5.5", review P48. The checkers' prose leads and drawing faults in `reviews/p43-greece-notes.md`, none fixed here.

**P57, Rome.** The 14 Rome reports whose figures N4 had reshaped or dropped around the drawing faults P55 fixed (content drops left alone): a fresh adder per report (14) decided from the text whether the original shape was better and redrew it, a fresh checker (12, one per report with a change) checked each change, the two FIXes (7.4, 10.2) were re-checked and passed; none failed twice. 15 figures changed: 12 restored in their original shape (1.5, 1.6, 3.5, 4.5, 5.6, 7.1, 7.4, 8.6 figures 1, 2 and 4, 10.2, 11.1) and 3 dropped figures written back (3.4's compare of the 225 infantry, 9.1's tree of Gaius' scheme, 10.2's tree of Seneca's plays); kept: 1.2 (text lengths stay dropped: approximate counts with no cited source), 6.4, 7.1 figure 4, 8.6 figure 3. Rome now has 180 P43 figures (timeline 74, flow 54, matrix 14, tree 14, compare 9, decision 5, bars 5, range 4, objects 1). `rome figures (P43)` entry updated; what was restored and kept added to `reviews/p43-rome-notes.md`.

**Drawing faults met, not fixed here** (proposed row P58): a range row whose low equals its high prints its value two or three times; a wrapped timeline event label parts "c." from its year; a timeline event's date line prints a bare first year, dropping "c." and split years, and writes BC/AD where a report uses BCE/CE; an objects link label in a narrow gap is cut mid-word; a range word unit takes no singular; a one-child tree chain sits against the left edge.

Built; `verify.py` failed once, on 10.9's cut objects label (fixed by eye, above), then ALL CHECKS PASSED, the phone pass checking the geometry of all 509 figures on 152 panels (dark and light), and again after the last build. `--shots` with `--page` for the Greek course home, Greek 5.1, 6.1, 9.1 and 10.9 (four figures each, the most any Greek report has, chosen for their range, timeline, matrix and objects kinds) and the twelve Rome reports P57 changed; every figure on those pages looked at whole at 390 px and at desktop; the faults above are visible there and left for P58. The machine-extracted unit bibliographies (`bibliography/<course>/unit-*.md`) now also pick up the works the captions cite. Academy artifact version 93 and Pages (`773a1e7`) published. Proposed rows P58 (the drawing faults), P59 (corrections from the Greek notes), P60 (no figure draws a hidden Self-test answer).

## 30 October 2026 · Session 31 · The figure renderer's drawing faults, and a flaky check (P55, P56)

Backlog rows P55 and P56 of `docs/BACKLOG.md`, Opus 5.5. `viz.py` now draws the cases the N4 checkers met and worked around (`reviews/p43-rome-notes.md`), under one rule: a label that cannot fit moves, or the drawing widens and scrolls; it is never clipped, shrunk or cut, and a block the renderer cannot draw honestly stops the build saying what to change. Timeline: a span's label sits inside its bar only when it fits with 6 units either side, else beside the bar in the muted column-head mono; spans sit in lanes, so spans that overlap in time never share one (abutting spans do); the drawing widens until span, event and tick labels fit, and stops the build past 2,400 units naming the ticks too close to label both; ticks, events and spans outside start..end stop it. A year 0 anywhere (tick, event, value) stops the build: there is no year 0. Compare and bars: labels wrap in a measured column up to 240 wide (compare's was a fixed 170 that clipped; bars' wrapped at 160); compare's values take thousands separators; a unit of three letters or more prints after a space ("1,200 men"), in every kind. Tree: boxes keep 112 units (wider when one word needs it), labels wrap whole and a level grows to its longest label; a tree more than 15 % over 700 scrolls instead of shrinking. Objects: the letter-by-letter wrap was attrs given as a bare string; any list field given a string now stops the build, in every kind. Range: `"years": true` prints years; negative whole numbers without it stop the build. Contracts recorded in `viz.py`'s docstring. `verify.py`: the figure checks (nothing outside the drawing, text inside its box or bar, no two boxes or labels overlapping, no free label over a box) now cover every kind, the A8 and data kinds included, and run on every figure of every panel in the phone pass (246 figures on 74 panels) as well as the examples page, which gains eight hard cases (one per fault) and lists the four blocks that must stop the build, each checked. P56: a fresh-load anchor is measured once its top has held still in the landing band (up to 3 s), with one retry; the same for every anchor in that loop and for `#rm12-2`. Figure data unchanged but one: `rome/r-2.4.html`'s tick at 0, which drew "AD 0" and now stops the build, moved to 1 (AD 1), as the new message says; no prose, word count or provenance changed. 77 existing figures draw differently (26 compare, 35 timeline, 14 tree, 1 range, plus 2.4's tick), all looked at whole at natural size, the named pages at 390 px and desktop. The theme did not move.

## 30 October 2026 · Session 30 · Figures in the Rome reports (P43)

Backlog row N4 (P43, Rome) of `docs/BACKLOG.md`, Opus 5.5. The figure pass of `skills/write-unit` §4b run over the 59 written Rome reports, in waves of eight: a fresh Opus 5.5 agent per report added figure declarations in the fragment syntax of `WRITER-BRIEF.md` and nothing else (seeing only its report, `viz.py`'s docstring and §4b), a separate fresh Opus 5.5 agent per report checked each new figure against the text without the adder's report, every FIX was applied and re-checked by another fresh agent, and a figure that failed twice was dropped. Specs were rendered from copies (`viz.render(copy.deepcopy(spec))`, P52); no `_` key reached a report. After each report `check.py` printed no HARD failure, its word count did not move and its prose, with the figures removed, was byte-identical to the original. 177 figures kept (timeline 75, flow 54, matrix 14, tree 12, compare 8, decision 5, bars 5, range 3, objects 1): unit 0 8, unit 1 16, unit 2 16, unit 3 15, unit 4 17, unit 5 18, unit 6 11, unit 7 17, unit 8 20, unit 9 16, unit 10 13, unit 11 5, unit 13 5; 0.3's earlier anchor-dates timeline and the course home's figure unchanged. 18 dropped: 8 after failing twice (0.3 foundation dates, 1.2 text lengths and decline, 1.5 Tarquin archaeology, 3.4 manpower of 225, 4.1 Carthage's coasts, 9.1 Gaius' scheme, 13.2 Cicero's late works), 10 on the checker's verdict as decorative, repetitive or unreadable. The reports' models in `provenance.json` are unchanged; a new `artefacts` entry, `rome figures (P43)`, "Opus 5.5, checked with Opus 5.5", review P48, puts them in the Fable review queue. The checkers also noted prose slips outside the figures (Self-test answers that state what the body does not, one double full stop, one repeated phrase); none was changed here. They are listed in `reviews/p43-rome-notes.md` with the drawing faults the checkers worked around (proposed rows P54 and P55).

## 30 October 2026 · Session 29 · Figures in the Brand + AI units (P42)

Backlog row N3 (P42) of `docs/BACKLOG.md`, Opus 5.5. The figure pass of `skills/write-unit` §4b run over the twelve filed Brand + AI units: a fresh Opus 5.5 agent per unit added ```viz blocks only (seeing only its unit, `viz.py`'s docstring and the figure pass), a separate fresh Opus 5.5 agent per unit checked each new figure against the text without the adder's report, every FIX was applied and re-checked by another fresh agent, and a figure that failed twice was dropped. 38 figures kept (A1 3, A2 2, A3 3, A4 4, A6 3, A9 4, B1 3, B2 4, B3 3, B4 4, B5 3, DD-B3 2), 4 dropped; no prose, citation, front matter, written date or word count changed. A Fable 5.1 check of them is owed (P48).

`viz.py`: the flow kind measures and wraps each step's label and note to the box, as the IA kinds do, and a row's boxes grow to its tallest step; a long note no longer runs out of its box and over the next arrow on a phone. Each box and its text are one `<g data-box>`, so `verify.py`'s text-in-box check now covers flows. `verify.py`: the page and figure screenshots wait up to 120 s (a long reading page took more than 30 s at phone width). Brand + AI hub v8.3. Verified (ALL CHECKS PASSED), every reading page shot at three widths and each new figure read at 390 px; published to the artifact and Pages.

## 30 October 2026 · Session 28 · Figures in the writing method (P41)

Backlog row N2 (P41) of `docs/BACKLOG.md`, Opus 5.5, run unattended overnight. The figure rule is now part of how a unit is written, checked and filed; no brief or syllabus prompt changed. `skills/write-unit` gains a figure pass after the draft (§4b: each section asked whether its content has a shape; a table of shape to kind for all fifteen kinds; one to four figures a unit as a guide, the UX briefs' three to eight standing; captions say what and where from; every figure rendered before handing in). `WRITER-BRIEF.md`'s figure paragraph says the same in the fragment syntax. `docs/method.md` §4 (Figure pass) and §7 (Figures: the check, the screenshots, and Pedro's 29 October decision that a figure retrofit does not count toward the four-unit audit and is checked by a separate agent); `docs/sourcing-standard.md` Part 1 gains a figure line; `skills/audit-units` §3b gains a figures section for the fresh check; `skills/file-unit` screenshots each new figure.

Tooling for the history retrofit: `check.py` accepts a figure declaration in the form of `WRITER-BRIEF.md` (the JSON must parse, its kind match `data-viz`, the caption be non-empty, and `viz.render` draw it) and still fails any other figure, script or style; `rome/r-0.3.html` now passes (it failed on its own figure before). `build.py`'s `wc` and `check.py`'s count leave figure blocks out: Greece stays at 246,357 words; Rome goes from 180,245 to 180,103, the 142 words of the drawn labels of 0.3's timeline, which the count had included, and from now on a figure never moves a count. `verify.py --shots <dir> --page <id>` also saves each figure of that panel on its own (`<width>-<panel>-fig-<nn>-<kind>-<theme>.png`). Verified (ALL CHECKS PASSED), published to the artifact and Pages.

## 29 October 2026 · Session 27 · Data figures, and figures on a phone (P44)

Backlog row N1 (P44) of `docs/BACKLOG.md`, Opus 5.5, run unattended overnight. `viz.py` draws four more kinds for data, each with its contract in the docstring: `line` (named series over an ordered x, numbers to scale or labels evenly, years with `yr`; every point labelled with its value or only the ends; dashed annotations with a note; a legend), `bars` (grouped or stacked horizontal bars, values at the bar ends, a stacked segment's value inside it when it fits, a legend), `scatter` (labelled points on two numeric axes with gridlines, optional quadrant lines and names; each label takes the nearest free spot and a label with none stops the build) and `range` (per row a low-to-high bar, an optional point estimate, each end's value with its source tag), and `matrix` gains a numeric mode (numbers shaded in five steps of one tone, a scale legend). Point labels, legend entries, quadrant names and range tags sit on plates, so the box checks also prove they do not overlap. Theme 5.4: the data classes in §4i, and the phone rule: below 768 px a figure draws at its natural size, one SVG unit to one CSS pixel, and scrolls sideways inside its frame, never the page; `shell.js` fades the edge that has more drawing and shows "scroll sideways for the whole figure" under a figure only when it is wider than its frame (on load, on resize, when a fetched panel lands and when a `<details>` opens). The cue is added by the script, so no report's word count moves. The line chart's figure class is `viz-linechart`, because `viz-line` already styles structural lines.

The Figure kinds page has sixteen figures (five new, on Perqo, fictional). `verify.py` checks, at 390 px on every panel, that each figure draws at its natural size and its frame scrolls to the whole drawing, that the cue shows exactly on the frames that overflow, and at desktop width that it shows only on a figure wider than its column. Verified (ALL CHECKS PASSED), published to the artifact and Pages.

## 29 October 2026 · Session 26 · Figures in the reader's fonts and colours (P39, P40)

Backlog rows P39 and P40, Opus 5.5. `verify.py` now loads the theme's own fonts from a vendored copy in `kit/fonts/` instead of stubbing Google Fonts, so every check measures what a reader's phone draws; the measure check is 68ch of the report font inside the column. Theme 5.3: dates, ticks, values and notes in figures draw muted and span labels on their accent, as the theme always meant (the rules had lost to `.viz text`). Timelines place each label so no stem runs through another label, facing right, left or centred: the Rome home's timeline is five rows without a crossing; labels are no longer cut at two lines. Verified, published to the artifact and Pages.

## 29 October 2026 · Session 25 · The IA figure kinds (V1)

Backlog row V1 of `docs/BACKLOG.md`, Opus 5.5. `viz.py` draws seven more kinds for the Information Architecture course: `sitemap` (top-down, page-type tags, the first level wrapping into rows, deeper levels stacked), `objects` (an object map in a grid, relationships with cardinalities), `decision` (questions, labelled branches, filled outcomes, packed level by level), `matrix` (rows by columns, a mark and a tone per cell, a legend), `states` (rounded states in order, gap arrows, routed transitions, start marker, end rings, loops), `swimlanes` (lanes, steps by column, links through the gaps; widens and scrolls) and `wireflow` (screens with placeholder content, labelled arrows). Text is measured in the theme's fonts and wrapped inside its box; a kind that cannot draw its data stops the build. Theme 5.2: nineteen classes in §4i. The four A8 kinds are unchanged, and so is every page that uses them.

A new page, Figure kinds (`#viz-examples`, linked from the home): one figure of every kind on the fictional Perqo, each with the block that draws it, written by `viz_examples.py` through the same Markdown path a unit takes. `verify.py` checks it has eleven figures and that every label lies inside its box, no two boxes overlap and nothing leaves its drawing; `--shots` photographs each figure at three widths in both themes. Verified, published to the artifact and Pages. IA1 waits for Pedro's look at the page.

## 29 October 2026 · Session 24 · User Experience track and course IA (U-0)

A second markdown family, `generator/data/ux/` (`hub.py`, `units_data.py`), and the `UX` entry in `courses.py` with a new track, User Experience (`var(--blue)`). The first course, IA · Information Architecture, is twelve core units in four parts and three deep dives, one brief each, nothing written; the home, the drawer, the course home, briefs, build order, audits, bibliography, changelog and "How it was built" pages all come from the existing markdown build.

Kit changes for a family that is not Brand + AI: `build.py` gives a markdown course with no unit filed the status coming soon, counts it as planned in the home's totals and the track headers, and labels its card button Open the syllabus; `mdcourse.py` names the course's family and its status in the eyebrow (no longer "Brand + AI · IN PROGRESS" for every markdown course) and shows the frame on a data file's first course; `howbuilt.py` reads a course's `sourcing_part` (`Part 4` for UX) and parses any unit-code prefix in its audit log; `verify.py` derives the root drawer-group check from `THEMES`. Theme: `.ditem .n`, `.dsoon .n` and `.hrow .n` widen to 3.6em so a six-character code (`DD-IA1`) stays on one line; copied to `shell.css`.

`docs/sourcing-standard.md` Part 4 (User Experience). `docs/courses-index.md`: the User Experience section (0 of 15), an audit counter, the hub row. Verified at three widths; published to the artifact and Pages. Before IA1: the IA figure kinds (backlog V1).

## 28 October 2026 · Session 23 · The vault is the source; a new course is a folder (A5)

Backlog row A5 of `docs/BACKLOG.md`, Opus 5.5. No report or unit changed; the built site is byte for byte what it was.

- **Vault as source.** `build.py:load_markdown` reads a markdown course's units from its vault folder (`courses.py` `vault='courses/brand-ai'`): a unit is written when its file is there with front matter, `WRITTEN` is derived, and a `READINGS` entry for a unit carries only its page's name and intro (no file path). A filed unit with no entry still gets a page, its intro made from the front matter. The duplicate copies in `generator/data/brand-ai/units/` are deleted; `mdcourse.py` and `howbuilt.py` read the paths `load_markdown` resolved. The build fails, naming the file, on a vault unit whose code is not in the data file, on two files for one code, or on a reading whose unit is not filed.
- **The index checked.** `index_check.py` checks `docs/courses-index.md` against the sources: one row per unit and module, title, written or not, model, status (reviewed, sampled, flagged), search and path, the count line above each table and the staleness table. `verify.py` runs it, so ALL CHECKS PASSED covers the index. Fixes it forced: A2, A6 and A9 have their own rows (they shared one), and the dead `gen/data/brand-ai/units/` paths are gone.
- **A new course is a folder.** A history course is `kit/<id>/` (syllabus, prompts index, fragments) plus its entry, and builds with no report written (the Start button opens the syllabus). A markdown course is `generator/data/<slug>/` plus its entry; its pages are `<id>-<key>`, `<id>-<key>-briefs` and so on, while Brand + AI keeps its A3 anchors (`prefix`, `legacy_ids`). `verify.py` takes the home's expected tracks from `courses.py`. Tested in a copy of the repo with a throwaway Egypt course and the template markdown course: both on the home after one build, verify clean but for their missing index sections, then clean with them.
- **Method.** `method.md` §7, `SETUP.md`, the `file-unit`, `new-course` and `audit-units` skills, the READMEs and `project-instructions.md` follow the new layout.

## 28 October 2026 · Session 22 · "How it was built" for every course (A4)

Backlog row A4 of `docs/BACKLOG.md`, Opus 5.5. No report changed and no flag was cleared.

- **A4.** `howbuilt.py` builds one page per course and `build.py` places it after the course home (history) or after the build pages (Brand + AI), fetched as `academy/<course>/built.html`, linked from the course home and the drawer. History pages: one table per syllabus unit, each written report with its `provenance.json` entry, the quality pass or fresh check verdict (dated and attributed from each review folder's `BRIEF.md`), the Fable audit scorecards (verdict, mean, factual errors, from the file), the overlap checks that name it, and its writer's unsure list and curated bibliography; then the audits run, the course and kit material from `artefacts`, and the `review_notes` naming the course. Brand + AI pages: one row per written unit from its vault front matter (model, date, search), its STATUS, its fresh check (front matter, with the chat link) and the AUDIT_LOG verdicts, and the staleness date from the six-month rule. Both: flags still open, `docs/method.md` §1 (the family's column, the common rule, the five decisions with their overrides) and `docs/sourcing-standard.md` (Part 1 and the course's part). `verify.py` requires each page to be a fetched file with anchors and to carry one row per written report or unit. Shell 298 KB, 155 fetched files, ALL CHECKS PASSED.

## 28 October 2026 · Session 21 · The history course homes leave the shell (P22)

Backlog row P22 of `docs/BACKLOG.md`, Fable 5.1. No report changed and no flag was cleared.

- **P22.** After P20 the two course homes (`#greece`, `#rome`, about 38 KB each) were the shell's largest growing part. Each now carries `data-split="home"` from `course_home()`, so `build.py`'s one split rule writes it to `academy/<course>/home.html` and keeps the stub with `data-src` and `data-anchors` (its unit cards: `#greece-u3`). `shell.js` runs `updateContinue()` again once a course panel's file has landed, because the home's continue and start buttons and its unit cards only exist after the fetch; the failed-fetch message now says "page" rather than "report". `verify.py` requires every numbered (history) course home to be a stub with a file and anchors, lands on `#greece-u3` and `#rome-u1` from a fresh load, checks that a fresh load of `#greece` shows the start button and opens one unit card, that reading 2.3 and returning shows "Continue 2.3 …" without a second fetch, and that a failed home fetch shows the retry button and the retry loads the cards; the tablet pass waits for the Rome home before measuring its card grid. Result: shell 293 KB, 151 fetched files (4.75 MB in all), ALL CHECKS PASSED at the three widths in both themes; a new history course now adds about 1 KB to the shell (its stubs and drawer). The Brand + AI course homes (about 10 KB each) stay in the shell. `README.md`, `publish_files.py`, `deploy.sh`'s comment and `docs/academy.md` A2 note the change.

Shell 293 KB; Greece 80 files, 2.28 MB; Rome 61, 1.76 MB; course A 6, 281 KB; course B 4, 147 KB; site 4.75 MB.

## 28 October 2026 · Session 20 · The syllabi, briefs and bibliographies leave the shell (P20); SETUP.md off the zips (P21)

Backlog rows P20 and P21 of `docs/BACKLOG.md`, Fable 5.1. No report changed and no flag was cleared.

- **P20.** The shell was 747 KB after A2, of which the two syllabi were 276 KB and the Brand + AI briefs and bibliography pages 110 KB; each new history course would have added about 180 KB, so the 1 MB limit was about four courses away. Now every panel that leaves the shell carries `data-split="<stem>"` from its builder (a history report `r-<id>`, a reading page its id, a syllabus `syllabus`, the briefs `briefs`, the bibliography `bibliography`), and `build.py`'s split is one rule: the panel's inner HTML becomes `academy/<ctx>/<stem>.html` and the shell keeps the empty stub with `data-src`. A stub that is not a report also carries `data-anchors`, the ids inside its file, and `shell.js` routes a hash to one of them (`#rs-u3`, `#s-m23`, `#b-a2`) by loading that panel first, as it already did for report sections by their numbering. `verify.py` requires every report, syllabus, briefs and bibliography panel to be a stub with a file and anchors, opens the Rome syllabus (its prompts and copy buttons present, fetched once), and lands on `#rs-u3`, `#s-m23`, `#b-a2` and `#b-b3` from a fresh load. Result: shell 366 KB, 149 fetched files (4.74 MB in all), ALL CHECKS PASSED at the three widths in both themes; a new history course now adds about 40 KB (its course home) to the shell. `README.md`, `publish_files.py`, `deploy.sh`'s comment, `docs/academy.md` A2 and the publish steps in the skills say "fetched files" rather than "report files".
- **P21.** `SETUP.md` §6 (Personal Mythology), §7, §8 and §9 step 1 no longer attach `personal-mythology-kit.zip` or `learning-project.zip`: the chat clones `apcanario/learning`.

Site version 58 published, Pages pushed.

## 28 October 2026 · Session 19 · The split: a shell plus one file per report (A2)

Backlog row A2 of `docs/academy.md`, Opus 5.5. The single page was 4.9 MB against a 16 MB cap with eight history courses still to come. No report changed and no flag was cleared.

### The build
`build.py` writes `academy/`: `index.html`, the shell (home, drawer, course homes, syllabi, build pages, changelog, backlog), and one file per report, `academy/<course>/r-<id>.html` for Greece and Rome and `academy/brand-<k>/read-<code>.html` for a Brand + AI reading page. A report panel stays in the shell as an empty stub carrying its attributes and `data-src`; the file is the panel's inner HTML. The shell now declares UTF-8 itself. `personal-mythology.html` is deleted. Two builds in a row give the same files.

### The shell
`shell.js` fetches a report the first time it is opened, keeps it in the panel for the rest of the visit, builds its pager once it has landed, and fetches the next report in the course in the background. Clicks on `data-target` links and copy buttons are delegated, so fetched content behaves like content that was in the page. A section link into an unopened report (`#m23-2`) loads the report, then scrolls to the section. A failed fetch shows the report's title, the reason and a Try again button. Hash routing, prev/next, Continue and stored progress are unchanged.

### Checks
`verify.py` serves `academy/` over local HTTP, as the artifact and Pages do, and every pass waits for the fetch before measuring a report (P13): phone, light, tablet (which now also measures a Rome report) and desktop. New: the files on disk (every stub has its file, no file is orphaned, no report file carries a style or script, the shell is under 1 MB, `README.md`'s size table matches) and the split in the browser (empty stub until opened, fetched once and kept, the next one prefetched, the pager, a section link on a fresh load, a 503 then the retry). ALL CHECKS PASSED. The published site was also opened in the real artifact viewer and a report fetched and rendered there.

### Sizes
Shell 747 KB; Greece 78 files, 2.12 MB; Rome 59, 1.58 MB; course A 4, 218 KB; course B 2, 97 KB; site 4.74 MB. The two syllabi are 284 KB of the shell; each new history course adds about 180 KB to it, so the 1 MB line is about four courses away (P20 proposed).

### Publishing
`publish_files.py` prints the report files as the list the Artifact tool's `files` takes. Publish = the shell as the page, `root` `academy`, that list; then `deploy.sh`, now site-only. The procedure is in `README.md` (Site layout and sizes), `skills/file-unit`, `skills/new-course`, `SETUP.md`, the root README, `generator/README.md`, `docs/project-instructions.md`, `NEXT-SESSION.md` and `BACKLOG.md`. Published as version 55 (144 files), then the shell alone once more after the backlog row was closed (the report files stay on the artifact); Pages pushed after each.

## 28 October 2026 · Session 18 · Brand + AI inside Academy (A3), the Backlog page, collapsible drawer, hover states

Pedro's five points after session 17, worked at once: Brand + AI units opened the hub artifact instead of a page of the site; the public site should show the backlog beside the changelog; the drawer should be collapsible; side-by-side cards should share a height with their buttons on one line; the theme had no hover states. No report changed and no flag was cleared.

### A3
`mdcourse.py` is the markdown course family: `build.py` reads `generator/data/brand-ai/hub.py` (unchanged, AD5) and builds one Academy course per course in it (AD6): the course home (goal, outcomes, progress, units in writing order, audits run, course A's Frame), a reading page per written unit (`#read-<code>`, `data-kind="report"`, so prev/next, Continue and stored progress work), and the "How it is built" pages (`#brand-<k>-build`, `-order`, `#briefs-<k>`, `-audits`, `-bibliography`, `-changelog`). The drawer of each course has two groups: Units (open) and How it is built (closed). No navigation leaves the site. `verify.py` walks both courses, their reading and build pages, the Continue buttons, the drawer groups and the Backlog page, and runs the panel checks in the light theme as well; it absorbs the retired `check_page.py`. Retired: `generator/build_hub.py`, `hub.js`, `check_page.py`, `build_history.py`, `hubs/`. The skills, `SETUP.md`, `method.md` §7 and the READMEs point at Academy.

### Backlog page
`#backlog` (root) renders `docs/BACKLOG.md` and `docs/CHANGELOG.md` as they are; the Academy home links it beside the Changelog, and so does the root drawer.

### Drawer
Groups are generic (`.dunit`): a course's units are an accordion (opening one closes the others; the current report's unit opens on arrival), the root tracks are collapsible and open by default, and the reader's choice is remembered per group (`hellas-units-open` now stores 1 or 0).

### Theme version 3
`design/theme.css` section 7: hover states on cards, rows, drawer items, buttons, chips, summaries and links where a pointer can hover; pressed states everywhere; transitions that respect reduced motion; catalogue cards are flex columns so side-by-side cards share a height with the button on one line (`.cgrid` stretches). `shell.css` is the copy.

### Published
Version 50 of the site to the Academy artifact and, with it, versions 49 and 50 to GitHub Pages (`deploy.sh` went through on the third try). The Brand + AI hub and Audience Growth artifacts were deleted on Pedro's word.

## 28 October 2026 · Session 17 · Course B gains DD-B3; Academy counts rebuilt

Pedro's request: a deep dive on Karpathy's documented practice and the other verifiable methods of using AI as a tool. Added to course B as DD-B3 in `generator/data/brand-ai/units_data.py` (hub v6.8), placed after A1 in the build order. Academy rebuilt from the same data file: course B is 2 of 11 units written; nothing else on the site changed, no report touched. `build_hub.py` now numbers the hub's build-order rows as `docs/courses-index.md` does and drops the duplicate sample-audit row beside the final audit.

### Published
Version 49 of the site to the Academy artifact; the hub as v6.8. The Pages push (`deploy.sh`) was refused by the session's deploy guard and is left to run by hand.

## 28 October 2026 · Session 16 · Navigable by others: breadcrumbs, start buttons, course B renamed

Pedro's request after session 15 (`docs/academy.md` AD7): the site must be navigable by anyone it is shared with, using only what it shows; the content stays written for him. No report changed and no flag was cleared.

### Navigation
A breadcrumb trail (`.crumbs`, new in `theme.css` section 5, every link 44 px) opens every course page (Academy › track › course), syllabus page (Academy › course › Syllabus), report (Academy › course › Unit n › id, the unit crumb landing on the course home's unit card, now anchored `<course>-u<n>`) and the changelog. Every course page has Start the course (its first report) beside Continue; `shell.js` shows one or the other, and `data-one` is set only when a single button is left. Brand + AI course pages start at their first written unit on the hub. Syllabus pages are titled "<Course>: syllabus and prompts".

### Course B
Renamed Using AI to Build a Brand, in `hub.py`, both filed B units' front matter, `method.md` §7, `docs/project-instructions.md` and `courses.py`. Unit texts and the course copy are untouched.

### Published
Versions 47 and 48 of the site (48 after the rebase onto the P8 commit), to the Academy artifact and GitHub Pages; the hub as v6.7.

## 28 October 2026 · Session 15 · The home becomes a catalogue by track (A0)

Pedro's request after session 14, worked in the same chat on Fable 5.1 (`docs/academy.md` AD6). No report changed and no flag was cleared.

### Tracks
`courses.py` gains `THEMES` (History, Marketing, Technology, each with a colour and a lede) and every course names its track. The Academy home is now a catalogue: an Academy hero with four stat tiles (courses live, reports and units written, words, hours of reading) and a jump button per track; then one banner per track (`.track`, `.thead`, new in `theme.css` section 5) over its course cards, every card the same shape (track chip, title, blurb, meta row, progress meter, status pill, Continue or Open). The History track keeps the coming-soon list and folds the mythos/logos essay into a collapsed "Why history and myth together" block; the rules block sits collapsed at the end. The root drawer is grouped the same way.

### Brand + AI as two courses
The data file is unchanged (AD5), but Academy now builds one course per entry in its `COURSES`: `brand-a` (Personal brand) under Marketing and `brand-b` (Building with AI) under Technology, each with its own panel (goal and outcomes, four tiles, the units in writing order linking to the hub, the audit log) and its own drawer context. `tracks` in `courses.py:BRAND_AI` maps a course key to its track and short name.

### Titles
Course and home titles are the course names: "Academy", "Greek history and mythology", "Roman history and mythology", the two Brand + AI course names; the hub home is "Brand + AI: two courses" (v6.6). `verify.py` checks the track order on the home and that no course title is a slogan.

### Published
Version 46 of the site, to the Academy artifact and GitHub Pages; the hub as v6.6.

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
