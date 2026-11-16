# Site log

The one source of Academy's Backlog and Changelog pages (S-PAGES, 15 Nov 2026): `kit/build.py` renders both from the two tables below and from nothing else. `docs/BACKLOG.md`, `docs/CHANGELOG.md` and `kit/CHANGELOG.md` stay the full records in the repo; they are not on the site.

Rules for an entry (`docs/method.md` §8):
- **Next**: one row per item still to do, in the overall order (#, from 1, no gaps); **Done**: one row per item done, any order (the pages sort newest first), the date as `YYYY-MM-DD` (the first day, where the work ran over several).
- **Code**: the item's short name: a unit's code (PB1, IA3), a history course's syllabus unit (G12 for Greece unit 12, R0–3 for Rome units 0 to 3), the backlog row's code for anything else (P96, S-PAGES), and K plus the session number for a site change of the kit's early sessions (K1 to K11), which had no row code. Keep it short: the column is narrow on a phone.
- **Area**: one of Mythology (Greece, Rome), Marketing (courses A and PB), AI (courses B and BW), UX, Coaching (course SP), Academy (the site and its method).
- **Sentence**: one plain sentence for an ordinary reader: what it is (Next) or what happened (Done). No model names, token counts, script or file names, row mechanics (rows, chats, prompts, corrections, mirrors), agent or audit vocabulary, and no private term (`kit/private-terms.txt`; `python3 kit/private_terms.py` scans this file). No `|` in a sentence.
- **One entry per item**: a unit, a course milestone or a visible site change. Housekeeping, corrections and re-checks are folded into the item they served, never listed on their own. A proposed item enters Next only when it is confirmed; a withdrawn one leaves it.
- The chat that closes a backlog row moves its entry from Next to Done (or adds it to Done), renumbers Next, and adds an entry to Next for each item it confirms into the queue.

## Next

| # | Code | Area | What it is |
|---|---|---|---|
| 1 | G-R | Academy | Give the pages of the two public courses, PB and BW, their object pictures. |
| 2 | SP1 | Coaching | Write SP1, What a coach can do, and how to tell evidence from noise, for Sport Psychology for Coaches. |
| 3 | SP2 | Coaching | Write SP2, The developing athlete, 10 to 25, for Sport Psychology for Coaches. |
| 4 | SP3 | Coaching | Write SP3, Motivation and the climate you create, for Sport Psychology for Coaches. |
| 5 | SP4 | Coaching | Write SP4, Anxiety, arousal and performing under pressure, for Sport Psychology for Coaches. |
| 6 | SP5 | Coaching | Write SP5, The cognitive-behavioural toolkit, for Sport Psychology for Coaches. |
| 7 | SP6 | Coaching | Write SP6, Training under pressure, for Sport Psychology for Coaches. |
| 8 | SP7 | Coaching | Write SP7, Reading and responding to an athlete, for Sport Psychology for Coaches. |
| 9 | SP8 | Coaching | Write SP8, Competition day, for Sport Psychology for Coaches. |
| 10 | SP9 | Coaching | Write SP9, Wellbeing, red flags and referral, for Sport Psychology for Coaches. |
| 11 | SP10 | Coaching | Write SP10, The season plan, for Sport Psychology for Coaches. |
| 12 | DD-SP1 | Coaching | Write DD-SP1, Deep dive: the coach's line with minors, for Sport Psychology for Coaches. |
| 13 | DD-SP2 | Coaching | Write DD-SP2, Deep dive: weight, body and who decides, for Sport Psychology for Coaches. |
| 14 | DD-SP3 | Coaching | Write DD-SP3, Deep dive: tuning out the noise, for Sport Psychology for Coaches. |

## Done

| Date | Code | Area | What happened |
|---|---|---|---|
| 2026-11-16 | S-SP0 | Coaching | Sport Psychology for Coaches, a new course, added: 13 units to write. |
| 2026-11-16 | DD-BW3 | AI | DD-BW3, the deep dive in which the reader reviews their own usage, written; course BW complete. |
| 2026-11-16 | DD-BW2 | AI | DD-BW2, Deep dive: one project, with its numbers, written. |
| 2026-11-16 | DD-BW1 | AI | DD-BW1, Deep dive: how the best practitioners work, written. |
| 2026-11-16 | BW10 | AI | BW10, Cost, limits, privacy, written. |
| 2026-11-15 | BW1 | AI | BW1, Mental model, written. |
| 2026-11-15 | BW2 | AI | BW2, Choosing the model and the effort, written. |
| 2026-11-15 | BW3 | AI | BW3, Briefing: prompts that hold up, written. |
| 2026-11-15 | BW4 | AI | BW4, Context engineering, written. |
| 2026-11-15 | BW5 | AI | BW5, Specifying a project, written. |
| 2026-11-16 | BW6 | AI | BW6, Research and verification, written. |
| 2026-11-16 | BW7 | AI | BW7, Pipelines: raw material to finished output, written. |
| 2026-11-16 | BW8 | AI | BW8, Skills and automation, written. |
| 2026-11-16 | BW9 | AI | BW9, Agents, written. |
| 2026-10-22 | G0–9 | Mythology | The Greece syllabus set out, then its core written: fifty reports from the sources and the geography, through myth, history, religion and art, to a final exam. |
| 2026-10-22 | G10 | Mythology | Greece gains its first deep dive, the Trojan War, in twelve reports. |
| 2026-10-24 | G11 | Mythology | Greece gains a second deep dive, Alexander, in eight reports. |
| 2026-10-24 | PM | Mythology | The project becomes Personal Mythology, a journey through the myths and histories of many cultures, with Greece as course 1 and nine more planned. |
| 2026-10-24 | R0–3 | Mythology | Rome begins: its syllabus, its own course home, and units 0 to 3 (the sources, Italy before Rome, the gods, the early Republic), nineteen reports. |
| 2026-10-24 | R4 | Mythology | Rome unit 4 written: Carthage and the Mediterranean, five reports. |
| 2026-10-24 | R5–6 | Mythology | Rome units 5 and 6 written, the fall of the Republic and Augustus, and every cross-reference between the Rome reports checked. |
| 2026-10-25 | R7 | Mythology | Philosophy deep dives added to both syllabi; Rome unit 7, the Principate, written; every Rome report so far read again and corrected. |
| 2026-10-25 | G12 | Mythology | Greece complete: its third deep dive, Greek philosophy, in eight reports, brings it to 78. |
| 2026-10-25 | R8–10 | Mythology | Rome units 8 to 10 written: crisis and the late empire, law, army and daily life, literature and art, and the final exam. |
| 2026-10-25 | R11, R13 | Mythology | Rome's first deep dive, the fall of the Republic, begins with its first two reports, and its philosophy deep dive with two more. |
| 2026-10-27 | K10 | Mythology | Every Greek and Rome report gains its own list of sources, ancient passages and modern works in full; the Greek deep-dive reports read again against the course's standard and their slips corrected. |
| 2026-10-30 | N4 | Mythology | Figures added to the Rome reports: timelines, comparisons, family trees and steps drawn from each report's own text. |
| 2026-10-30 | N5 | Mythology | Figures added to the Greek reports in the same way, and the facts found wrong while drawing them corrected in both courses. |
| 2026-11-01 | R11 | Mythology | Rome's deep dive on the fall of the Republic continues: politics in the street, women, Cicero's letters, and Caesar in Gaul. |
| 2026-11-01 | R11–13 | Mythology | Rome complete, 79 reports: the Ides of March, why the Republic fell, the deep dive on the Aeneid, and the Stoics through Marcus Aurelius. |
| 2026-10-28 | A9 | Marketing | A9, What to expect: benchmarks, written again from its brief, with a figure drawn from its own data. |
| 2026-10-28 | A2 | Marketing | A2, Audience and platform economics, written again from its brief, with a figure drawn from its own data. |
| 2026-10-28 | A6 | Marketing | A6, How growth works, per platform, written again from its brief. |
| 2026-10-29 | A1 | Marketing | A1, Positioning: the journey as a format, written; its section on two vlog episodes rebuilt from the episodes themselves. |
| 2026-10-29 | A3 | Marketing | A3, The journey system, written. |
| 2026-10-29 | A4 | Marketing | A4, Voice, disclosure and the record, written. |
| 2026-10-30 | N3 | Marketing | Figures added to every course A unit written so far. |
| 2026-11-01 | A5 | Marketing | A5, Production craft, written. |
| 2026-11-02 | A7 | Marketing | A7, Monetisation, written: an integration plan and a revenue model in three scenarios. |
| 2026-11-02 | A8 | Marketing | A8, Legal, tax, time, written, with a register of every constraint and who confirms it. |
| 2026-11-02 | DD-A1 | Marketing | Deep dive: five creators who did this, written. |
| 2026-11-02 | DD-A2 | Marketing | Deep dive: the exit math, written; course A complete. |
| 2026-11-11 | G-0 | Marketing | Course PB, Building a Personal Brand on Instagram and YouTube, created for any reader from course A: twelve units, each with its brief. |
| 2026-11-12 | PB1 | Marketing | PB1, What to expect: odds, timeline, cost, written. |
| 2026-11-12 | PB2 | Marketing | PB2, Positioning: the sentence a stranger can repeat, written. |
| 2026-11-12 | PB3 | Marketing | PB3, Audience and the two platforms, written. |
| 2026-11-12 | PB4 | Marketing | PB4, The content system, written. |
| 2026-11-12 | S-PB1 | Marketing | Course PB's plan reviewed after four units: three later briefs changed and the case study's facts corrected. |
| 2026-11-12 | PB5 | Marketing | PB5, Production craft with a phone, written. |
| 2026-11-12 | PB6 | Marketing | PB6, How YouTube growth works, written. |
| 2026-11-12 | PB7 | Marketing | PB7, How Instagram growth works, written. |
| 2026-11-13 | PB8 | Marketing | PB8, Voice, disclosure and the rules, written, with the rules of the case study's home country. |
| 2026-11-13 | PB9 | Marketing | PB9, Monetisation: what pays at each audience size, written. |
| 2026-11-13 | PB10 | Marketing | PB10, Read your numbers: the quarterly review, written. |
| 2026-11-13 | DD-PB1 | Marketing | Deep dive: creators who did this, written: six creators read against the course's rules. |
| 2026-11-14 | DD-PB2 | Marketing | Deep dive: the quit-your-job math, written; course PB complete, and its twelve units then corrected in 103 places against their sources. |
| 2026-10-28 | B1 | AI | B1, Mental model, written. |
| 2026-10-28 | B2 | AI | B2, Choosing the model, written, with a figure drawn from its own data. |
| 2026-10-28 | DD-B3 | AI | Course B gains a third deep dive, on how the best practitioners use the tool, and is renamed Using AI to Build a Brand. |
| 2026-10-29 | B3 | AI | B3, Prompting that holds up, written, with a library of ten templates. |
| 2026-10-29 | B4 | AI | B4, Context engineering, written. |
| 2026-10-29 | DD-B3 | AI | Deep dive: how the best practitioners use the tool, written. |
| 2026-10-29 | B5 | AI | B5, Skills and automation, written. |
| 2026-10-30 | N3 | AI | Figures added to every course B unit written so far. |
| 2026-11-01 | B7 | AI | B7, Content pipeline, written. |
| 2026-11-02 | B6 | AI | B6, Research and verification, written. |
| 2026-11-02 | B8 | AI | B8, Cost, limits, hygiene, written. |
| 2026-11-02 | DD-B1 | AI | Deep dive: agents, written. |
| 2026-11-02 | DD-B2 | AI | Deep dive: his unknown unknowns, written; course B complete. |
| 2026-11-11 | G-0 | AI | Course BW, Building with AI, created for any reader from course B: thirteen units, each with its brief. |
| 2026-10-29 | U-0 | UX | The User Experience area opens with course IA, Information Architecture, written for designers around one fictional benefits platform. |
| 2026-10-29 | V1 | UX | Seven new kinds of figure for course IA: site maps, object maps, decision trees, matrices, state diagrams, swimlanes and wireflows. |
| 2026-10-30 | IA1 | UX | IA1, What information architecture is, and where it sits, written. |
| 2026-10-30 | IA2 | UX | IA2, The shapes IA takes: the artefact catalogue and the course notation, written. |
| 2026-11-03 | S-1 | UX | Course IA's plan reviewed: every unit now states its aim, what it takes from earlier units and what it gives to later ones. |
| 2026-11-03 | IA3 | UX | IA3, How people find and understand things, written. |
| 2026-11-03 | IA4 | UX | IA4, Organisation systems: schemes, structures, objects, taxonomies, written. |
| 2026-11-03 | IA5 | UX | IA5, Level 1: the sales and product website, written. |
| 2026-11-03 | IA6 | UX | IA6, Level 2: the client app, written. |
| 2026-11-03 | IA7 | UX | IA7, Level 3: the backoffice, written. |
| 2026-11-09 | IA8 | UX | IA8, Level 4: the system map, written. |
| 2026-11-09 | IA9 | UX | IA9, IA in the product development lifecycle, written. |
| 2026-11-09 | IA10 | UX | IA10, Touchpoints: what each part of the business needs from the IA, written. |
| 2026-11-10 | IA11 | UX | IA11, Validating an IA: evidence, methods, numbers, written. |
| 2026-11-10 | IA12 | UX | IA12, When the inputs are missing: building the backbone anyway, written. |
| 2026-11-10 | DD-IA1 | UX | Deep dive: five information architectures read closely, written. |
| 2026-11-10 | DD-IA2 | UX | Deep dive: what IA costs and returns, written. |
| 2026-11-10 | DD-IA3 | UX | Deep dive: taxonomy and governance at scale, written; course IA complete. |
| 2026-10-23 | K1 | Academy | The first site: a phone layout with arrows and a slide-out contents drawer, a light theme, and a home that opens on Continue. |
| 2026-10-24 | K2 | Academy | The site holds more than one course, and its pages fit a phone at normal scale. |
| 2026-10-25 | K7 | Academy | A Changelog page added, one card per work session. |
| 2026-10-27 | K11 | Academy | The site moves onto the project's shared visual theme. |
| 2026-10-28 | A1 | Academy | The site becomes Academy, one site for every course, also published on GitHub Pages. |
| 2026-10-28 | P11 | Academy | Layouts for tablet and desktop: a wider column, and from desktop width a sidebar that stays open. |
| 2026-10-28 | A0 | Academy | Academy's home becomes a catalogue of the courses, grouped by area. |
| 2026-10-28 | A0 (2) | Academy | Academy can be read by anyone it is shared with: a breadcrumb trail on every page and a Start button on every course. |
| 2026-10-28 | A3 | Academy | Courses A and B move into Academy, each with its own home, reading pages, briefs and sources, and a Backlog page joins the site. |
| 2026-10-28 | A2 | Academy | Academy splits into a main page plus one file per report, loaded as it is read, so the site stays light. |
| 2026-10-28 | A4 | Academy | A page on how each course was built: who wrote each unit, how it was checked, and the method in force. |
| 2026-10-28 | A6 | Academy | The home opens on where the reader left off, with the newest units and the courses by area. |
| 2026-10-28 | A8 | Academy | A sharper visual theme, and figures drawn from data (timelines, comparisons, trees, steps), first on the Greece and Rome homes. |
| 2026-10-29 | P44 | Academy | New data figures (lines, bars, scatter plots, ranges) and figures that scroll in their own frame on a phone. |
| 2026-10-29 | P40 | Academy | Figures drawn in the site's own fonts and colours. |
| 2026-10-29 | P31 | Academy | Several units may be written in one working session, each by a fresh writer that sees only its brief and the units already filed. |
| 2026-10-30 | P41 | Academy | Figures become part of how every unit is written, wherever structure is the content. |
| 2026-10-30 | P55 | Academy | Figure labels that do not fit move aside or widen the drawing instead of being cut off, with eight hard cases on the Figure kinds page. |
| 2026-10-30 | P58 | Academy | Six drawing faults in the figures fixed, each with a hard case on the Figure kinds page. |
| 2026-11-01 | H-1 | Academy | A new reading layout: every unit and report opens on its scope and reads one section at a time, with a progress bar and a section menu. |
| 2026-11-01 | H-2 | Academy | Figures open on the drawing on a phone, timelines may name a century, and matrix columns fit their contents. |
| 2026-11-01 | P70 | Academy | A Greece-only edition of Academy, published on its own, and the Greek course as an e-book with every figure. |
| 2026-11-03 | P83 | Academy | Wide figures keep their labels in view while they scroll on a phone. |
| 2026-11-04 | P90 | Academy | A new home with a map of Academy, and a paper-like light theme in which every colour reads clearly. |
| 2026-11-04 | P91 | Academy | The home as a bookshelf of every unit, and a What's new page listing every unit and report by the day it was filed. |
| 2026-11-04 | P92 | Academy | The home opens on a contour map drawn from the words written in each area. |
| 2026-11-04 | P93 | Academy | Every contour drawing moves slowly, and contour maps join the course homes and What's new. |
| 2026-11-08 | P94 | Academy | Every section of every reading page ends on a small contour line drawn from its paragraphs. |
| 2026-11-08 | P95 | Academy | Object pictures: a library of outlines and three trial pages. |
| 2026-11-08 | P96 | Academy | Object pictures on 95 of the 187 reading pages, wherever the text discusses an object at length. |
| 2026-11-12 | P97 | Academy | Every comparison figure opens whole on a 320 or 390 px phone. |
| 2026-11-12 | P98 | Academy | Bar figures drawn at their own size on a 320 px phone, each value clear of the end of its bar. |
| 2026-11-15 | S-NOAUDIT | Academy | Periodic reviews of written units stopped, and their pages removed from the site. |
| 2026-11-15 | P112 | Academy | The project's working copies of the queue and this record brought up to date. |
| 2026-11-15 | S-PAGES | Academy | The Backlog and Changelog pages redrawn as this plain overview by area. |
| 2026-11-15 | S-BW1 | AI | The writing rules of the public AI course tightened before its first unit (honest source titles, quotations credited to the speaker, figures cited to the page that states them), the lesson carried back into course A, and the course's writing sessions made leaner. |
