# Backlog: the rest of Rome (writing)

This is the writing prompt that was `NEXT-SESSION.md` until 27 October 2026. It is now the backlog: the Fable review is under way and `NEXT-SESSION.md` resumes it. Run this file when the review reaches a clean point (after Rome 14.2/14.5 has cleared the written reports, or whenever you decide to write first). Nothing below has been done; two things have changed since it was written:

- The Rome syllabus changed on 27 October (Rome 14.6): the prompts of 1.5, 3.3, 3.5, 7.4, 9.2, 9.3, 10.3, 11.2 and 11.6 gained pointers or wording, and 14.3 gained a core-pairing list. Take every prompt from the current `roman-syllabus.html`, not from memory of this file; 11.6 in particular now asks the writer to weigh 5.4's casualty figures rather than restate them.
- The syllabus, both course copies and the Greek deep dive III prompts are now "Opus 5.5, reviewed with Fable 5.1". Every report keeps its flag; the review queue is `FABLE-REVIEW.md`. A report written on Fable 5.1 is registered as "Fable 5.1" and never enters the queue.

Where the text below says "`FABLE-REVIEW-SESSION.md`", read `NEXT-SESSION.md`. Standing cadence (S3, decided 28 October 2026): after every four content modules written since the last review, Greece and Rome pooled, stop and run the Fable review before writing on; `review_due.py` counts the modules ("n of 4 modules written since the last review", FABLE REVIEW DUE at 4) and `register.py` and `build.py` print its line. The batch plan, cutting across syllabus units: batch 1 = 11.3, 11.4, 11.5, 11.6 → review; batch 2 = 11.7, 11.8, 13.3, 13.4 → review; batch 3 = 13.5, 13.6, 13.7, 13.8 → review; batch 4 = 12.1, 12.2, 12.3, 12.4 → review; batch 5 = 12.5, 12.7, 12.8, 12.6 → review (11.8 last in its unit; 12.6 after 13.2, which is written). Writers run in parallel within a batch only. Each review runs on Fable 5.1 with the `method.md` §6 claim-sample prompt; a module failing more than one claim in ten gets the kit scorecard audit (`audits/AUDIT-BRIEF.md`). Until the Fable stage (Pedro, 31 October 2026) a due review is said and deferred, not run: the count rises, no batch waits.

---

I'm continuing a long self-study project called **Personal Mythology**: a compendium of courses on the history and mythology of different cultures, published as one claude.ai artifact. **Greece (course 1) is complete**: 78 reports, its deep dive III on Greek philosophy written on 25 October 2026. **Rome (course 2)** has units 0 to 10 written, and its three deep dives (units 11 to 13) partly written. Every report written on 25 October went through a writer, a fresh checker that had not seen it written, and a maintainer who verified each finding before applying it.

This session has two jobs, in this order:

1. **Write the rest of Rome**: deep dive I (11.x), deep dive III (13.x), deep dive II (12.x), in the dependency order below.
2. **Re-check the site, publish, and hand over.** When Rome is complete, the next job is the Fable review (`FABLE-REVIEW-SESSION.md`, to be updated for the new reports and audit numbers).

This may be more than one session's work. Publish after every finished unit so nothing registered is ever unpublished, and stop at a clean point when the session runs short.

## Where things stand (end of the session of 25 October 2026)

- **Greece:** complete, 78 reports. Nothing to write.
- **Rome:** 59 of 79 content reports registered (about 180,000 words), every one checked: nothing is unchecked. Units 0 to 10 complete; deep dive I has 11.1 and 11.2; deep dive III has 13.1 and 13.2; deep dive II has none.
- **To write (job 1), 20 modules:** Rome 11.3 to 11.8, 13.3 to 13.8, 12.1 to 12.8. They show a blue "next" pill (`next_up` in `courses.py:ROME`). 11.3 and 11.4 were started on 25 October but nothing reached disk: write them from scratch.
- **Published:** the site with everything registered (the last publish of 25 October, after the checks of 10.5, 13.1 and 13.2, has no unchecked pills and carries the next pills); the Greek syllabus (version 7, unit 13 naming unit 12). The Rome syllabus is unchanged.
- **Open corrections to Fable-written Greek reports** (7.2's Epicurean gods box, 9.3's Ovide moralisé date, 7.3's two, 9.4's exam timings) are in `review_notes` for the Fable review: don't apply them in a writing session. Three small corrections to Opus-written Rome reports (1.4, 3.1, 6.1), found by the 10.5 checker, are in `review_notes` with exact replacements; they were left unapplied in the checks session.

## Where the source is

- Clone the private repo `apcanario/learning`; work in `kit/`; this file is `kit/BACKLOG.md`. Read, in this order: `README.md`, `AGENT-SPEC.md`, `WRITER-BRIEF.md`, `reviews/units-9-13/BRIEF.md` (the checker brief), the end of `reviews/units-9-13/log.md` (the maintainer log: what was fixed, confirmed and left open for every report so far), and the last `review_notes` in `provenance.json`. Run `python3 build.py` and confirm it reproduces `academy/` byte for byte (`git status` clean) before changing anything.
- One kit session at a time: two kits edited in parallel diverge in `provenance.json`, the prompts indexes and the site. End with a commit and push.

Live page: update it, never create a new one.
- The site: https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH
- The standalone syllabus artifacts were retired on 28 October 2026; the site's syllabus panels are the only published copy.

**Publishing, as it worked on 25 October.** Delegate the publish to one small agent so the large page stays out of the main context: the agent reads the site with the Artifact tool (the result says the version "counts as viewed"; the full page need not be read), then publishes `academy/index.html` once with the page's `url`, `root` `academy`, the fetched files `python3 publish_files.py` prints as `files` (since A2 the site is a shell plus one file per report; since P20 the syllabi, briefs and bibliographies are files too) and a short label, and never retries or forces. A refusal right after a successful publish usually means the agent resent its own content; check the local file's time before publishing again.

## Already done, don't redo

- `AGENT-SPEC.md` is course-general: the content rules apply to both courses, with the philosophy citation conventions for each (Diels–Kranz, Stephanus, Bekker, *SVF*, LS, Diogenes Laertius, Sextus, Plotinus; Seneca's *Letters*, Epictetus, Marcus, Musonius, Cicero's philosophical works by English title) and Eusebius' history as *Church History*.
- `WRITER-BRIEF.md` carries the quality-pass lessons and asks every writer for a notes file, `reviews/units-9-13/<course>-<id>-writer.md`, listing its unsure claims.
- `reviews/units-9-13/BRIEF.md` is the checker brief.
- `check.py` has a capstone mode (any module whose prompt asks for a "final examination"); `verify.py` finds each course's last report from the drawer; `build.py` names partial syllabus entries by their `flag_label`.
- The fresh checks of Rome 10.5, 13.1 and 13.2 (findings in `reviews/units-9-13/rome-10.5.md`, `rome-13.1.md`, `rome-13.2.md`; a paragraph each in `log.md`); all three re-registered as `"Opus 5.5"`.

## Order and dependencies for what remains

A writer starts only when every report named in its lane note is registered. Within that rule, keep four or five agents running.

| Step | Modules | Can start when |
|---|---|---|
| 1 | Rome 11.3–11.7 | at once (11.3 shares Clodius' tribunate with 11.5) |
| 2 | Rome 11.8 | last in the unit |
| 3 | Rome 13.3–13.8 | at once: Greek 12.5, 12.6 and 12.8 and Rome 10.2 are registered; 13.4 and 13.6 share the Stoic opposition (see the lane notes) |
| 4 | Rome 12.1–12.5, 12.7, 12.8 | at once (12.8: Rome 10.4 is registered) |
| 5 | Rome 12.6 | after Rome 13.2 is registered (Greek 12.6 and 12.7 already are) |

## How each report is made

1. **Writer** (one per module): give it `WRITER-BRIEF.md`, its module id, its output path (`rome/r-X.Y.html`), its target (in its prompt), its extra files and its lane note below. Writers never use the Artifact tool.
2. **Check:** `python3 check.py rome/r-X.Y.html`.
3. **Checker:** a fresh agent that has not seen the report written. Brief it with `reviews/units-9-13/BRIEF.md`, the report, its prompt, its neighbours, the targets of its pointers, the lane note and the writer's notes file. It writes `reviews/units-9-13/rome-X.Y.md` and never edits the report. On 25 October fresh checkers found errors in nearly every report (about one or two per report, plus should-fix items): run one on every report.
4. **Maintainer:**
   - Verify every finding before applying it; checkers are sometimes wrong, and a finding can be superseded by a fix elsewhere. Apply with exact-match replacements (assert the old text occurs once), keeping whitespace inside `<pre>` untouched. Replace a Self-test item as a whole `<li>`.
   - A finding against a report written with Fable 5.1 (most of the Greek course) is not applied: log it in `review_notes` for the Fable review, as was done for Greek 7.2 and 9.3.
   - Re-run `check.py`; keep the body inside its band (most reports sit near the top of it, so a fix that adds words may need a cut).
   - Append one paragraph to `reviews/units-9-13/log.md`.
5. **Register:** `python3 register.py rome "<model that actually wrote it>" X.Y`.
6. **When a unit is complete:** `python3 crosscheck.py rome <ids>` and check every pointer between the unit's own reports (the early checkers saw their neighbours only as prompts); build, `verify.py`, publish the site, `./deploy.sh` (publishing Academy means the artifact and then GitHub Pages); turn the unit's log into a `review_notes` entry; commit.

## Lane notes

The hand-offs quoted below are what the written reports already say about each module, so the module must deliver them. Check each again before relying on it: a pointer that misdescribes its target is still the commonest fault. Each writer keeps neighbouring material to an outline and hands off by number.

**Rome unit 11: Deep dive I, the fall of the Republic.** 11.1 and 11.2 are written (11.1 has the assemblies, the contio and the Millar debate, pointing to 4.4 and 4.5; 11.2 the army in politics). The prompts point back to units 3 to 5.

| Module | Lane, and extra files |
|---|---|
| 11.3 Politics in the street | 2.4 (the compital associations, dissolved in 64 and revived by Clodius); 5.1 (Gaius Gracchus' grain laws "to Clodius"; the final decree of 121, which 11.3 "treats as legalised violence"); 5.2 (Saturninus' grain law and "the politics of the street"); 5.3 (Clodius tested the final decree in 58); 5.4 (Clodius' adoption; his death in 52 and the Senate house as his pyre). 9.4 has the dole as an institution and hands the grain laws as politics here. Clodius' tribunate is shared with 11.5: here the street, there Cicero. Extra: `rome/r-2.4`, `r-5.1`, `r-5.2`, `r-5.3`, `r-5.4`, `r-9.4`, `r-11.1`. |
| 11.4 Women and the late Republic | 5.1 (Cornelia and her inscribed base: "Deep dive module 11.4 goes further"); 5.3 (Sallust's Sempronia); 5.4 (Servilia); 5.5 (Hortensia, Appian 4.32–34; Fulvia and the Perusine sling bullets, CIL XI 6721); 5.6 (whether Lesbia is the Clodia of *Pro Caelio*); 6.1 (Livia's marriage in 38). The lane with 9.3 (written: the family, the law, the *Laudatio Turiae*, with a line each for Cornelia, Hortensia and Livia): here these women. Extra: `rome/r-5.1`, `r-5.3`, `r-5.4`, `r-5.5`, `r-5.6`, `r-6.1`, `r-9.3`. |
| 11.5 Cicero through his letters | 5.3 and 5.4 (Clodius' tribunate and Cicero's exile, "deep dive modules 11.3 and 11.5"); 5.4 ("Cicero's forced change of course" after Luca); 5.5 (the *Philippics* "as oratory"); 5.6 (the letters to Atticus: "Deep dive module 11.5 reads them"). Rome 13.1 and 13.2 (written) have Cicero as philosopher: point to them. Extra: `rome/r-5.3`, `r-5.4`, `r-5.5`, `r-5.6`. |
| 11.6 Caesar's Commentaries and Gaul | 5.4 (its table of the campaigns uses Caesar's own figures: "The campaigns, the ethnography and the archaeology of Alesia are deep dive module 11.6"; the genocide charge "weighed in deep dive module 11.6"); 5.6 (the plain style as argument: "11.6 takes the Commentaries apart"). Extra: `rome/r-5.4`, `r-5.6`. |
| 11.7 The Ides of March | 5.4 (the conspirators' motives); 5.5 (Antony's funeral speech, Appian 2.143–147 against Suetonius, *Julius* 84: "deep dive module 11.7 compares the versions"). 10.4 (written) places Shakespeare's *Julius Caesar* among the Roman plays and leaves the comparison with the sources here. Extra: `rome/r-5.4`, `r-5.5`, `r-10.4`. |
| 11.8 Why the Republic fell | Write last in the unit. 0.3 (Flower ends the traditional Republic in 88: "Module 11.8 takes it further"); 5.1 (4.5 dates the decline, 5.6 reads Sallust's, "11.8 weighs the explanations"); 5.6 (Sallust's theory); 6.1 (Syme's prosopography: "Deep dive module 11.8 places him among the explanations"). Extra: `rome/r-0.3`, `r-4.5`, `r-5.1`, `r-5.6`, `r-6.1`, and 11.1 to 11.7. |

**Rome unit 12: Deep dive II, the Aeneid.** Hand-offs to honour:
- **12.1:** 6.3 ("Virgil's life belongs to deep dive module 12.1"; the fourth *Eclogue*'s child goes here, and 5.5 places it in 40).
- **12.2 and 12.3:** 6.3 ("take it book by book").
- **12.3:** 5.5 ("Deep dive module 12.3 reads the shield in its book").
- **12.4:** 4.1 ("Book 4 belongs to deep dive module 12.4").
- **12.5:** 2.4 (Virgil's underworld is "Greek in plan"); 3.5 (*Aeneid* 6.836–840, usually taken as Perseus); 6.3 (the precept to spare the conquered, 6.851–853).
- **12.6:** 2.2 (Ennius reconciled Juno in the Hannibalic war, Servius on *Aeneid* 1.281). Write after Rome 13.2 is registered; its prompt points to Rome 13.2 and Greek 12.6 and 12.7 (both written).
- **12.7:** 6.3 ("the debate between Augustan and pessimistic readers that deep dive module 12.7 runs").
- **12.8:** 10.4 (written: reception of Rome in general; leave the *Aeneid*'s own afterlife here); Greek 10.12 for Troy.
- Extra files are the reports each prompt names. 10.1 (Ovid) and 10.2 (imperial literature) are written: point to them where the poem's successors come up.

**Rome unit 13: Deep dive III, Roman philosophy.** 13.1 and 13.2 are written. Greek 12.5 to 12.8 are written and are the Greek side: point back ("Greek module 12.7"), don't retell. Hand-offs to honour:
- **13.3:** Greek 12.6 points forward to it (the Epicureans at Rome); Greek 12.8 leaves Cicero and the Academy at Rome to it.
- **13.4:** 7.1 (Thrasea's walk-out, "the first gesture of a resistance that deep dive module 13.4 follows to his death in 66"); 10.2 (Lucan as a poet; his Cato is 13.4's).
- **13.4 and 13.6:** 7.2 (Helvidius Priscus exiled and killed, *Vespasian* 15, with the expulsion of philosophers, Dio 66.13; under Domitian, Arulenus Rusticus and Herennius Senecio killed and philosophers expelled, *Agricola* 2 and 45: "deep dive modules 13.4 and 13.6"). Split them: give each event one home.
- **13.5:** 7.1 ("Seneca's life is deep dive module 13.5"; his death, Annals 15.60–64); 10.2 (Seneca's tragedies as literature: point back).
- **13.7:** 7.3 ("His life and inner history are deep dive module 13.7"; the rain miracle, Avidius Cassius' revolt of 175 and Commodus' elevation in 177; the martyrs of Lyon in 177).
- **13.8:** 7.3 (the *Meditations*, with the manuscripts' place notes "among the Quadi on the Granua" and "at Carnuntum").

Extra files:
- **13.3:** `rome/r-5.6`, `greece/r-7.2`, `r-7.4`, `r-12.5`, `r-12.6`, `r-12.8`, `rome/r-13.1`.
- **13.4:** `rome/r-5.4`, `r-5.6`, `r-7.1`, `r-7.2`, `r-10.2`.
- **13.5:** `rome/r-7.1`, `r-10.2`, `r-13.2`.
- **13.6:** `rome/r-7.2`, `greece/r-12.7`.
- **13.7 and 13.8:** `rome/r-7.3`, `greece/r-7.4`, `greece/r-12.7`.

## Lessons from 25 October (pass to every writer and checker)

- **Attributions from summaries.** Writers often take a scholar's view from a review or an encyclopedia entry. Every "X argued Y" gets checked; many findings were a view given to the wrong scholar or a box with one side unnamed.
- **The reporter and the claim.** The commonest error class: an ancient author cited for what only another author says (Polybius for a minimum age he does not give, Suetonius for a campaign he does not name, Sextus for a definition Cicero reports).
- **Pointers.** Open the report before writing "module X covers Y". Pointers written while a neighbour was still unwritten were the most often wrong; the maintainer re-checks them at the end of each unit.
- **Duplication.** Self-test questions repeated a neighbour's question; dispute boxes restated a neighbour's box. Each has one home.
- **Self-test answers** must agree with the body after fixes.
- **Philosophy:** quote fragments from the edition cited; keep the doxographer separate from the claim; don't grade a neighbouring report inside a report (log its error instead).
- **Usage limits.** Agents stopped three times on usage limits (session and monthly). Stopped agents keep their work: resume them with `SendMessage` after the reset, never restart them. Record the pipeline state in the log before a likely stop.

## Job 2: re-check and publish

After every unit: build, `python3 verify.py` (it must print ALL CHECKS PASSED), check each new report's panel (Fable flag, prompt matches the syllabus, crumb, prev and next), publish the site, `./deploy.sh`. `register.py` and `build.py` end by printing the Fable review alert (`python3 review_due.py`): **when it reads FABLE REVIEW DUE, finish the unit in hand, do not start another, and tell Pedro in the first line of the reply**; the review (`NEXT-SESSION.md`) runs before writing resumes. At the end: `python3 verify.py --shots <folder>` and look at the Rome course home and one report from each new unit, in dark and light. When Rome is complete, set `status='available'` in `courses.py:ROME` (the value `build.py` treats as complete), check the root card and the Rome home, and update the README.

## Limits and stopping
- **Agents:** at most four or five running at once, writers and checkers together.
- **If the session runs short:** stop at a clean point, ideally a unit boundary. Every registered report is published. Unfinished ones stay out of the prompts index. The log, `review_notes` and the next `NEXT-SESSION.md` say exactly where to resume.

## At the end
- Update `README.md` ("Where things stand", next steps), `review_notes` and the `artefacts` in `provenance.json`; rebuild and publish.
- Add an entry for the session at the top of the sessions in `CHANGELOG.md` (and a row in its "At a glance" table, and update "Where things stand"); `build.py` renders it as the site's Changelog page.
- Commit and push; summarise in a few lines what was written, what changed and what is left. If modules remain, `NEXT-SESSION.md` covers them; if Rome is complete, it says so, and the next job is the Fable review (`FABLE-REVIEW-SESSION.md`, updated for the new reports and audit numbers).

## The Fable review flag
Everything written with a model other than Fable 5.1 is flagged for later review with Fable 5.1: `register.py` records the model, the site marks each flagged report and course home, and `build.py` regenerates `FABLE-REVIEW.md` as the queue. Non-report changes go under `artefacts` in `provenance.json`. No flag is cleared in a writing session. If this session runs on Fable 5.1, record `"Fable 5.1"` for what it writes.

## Design rules (unchanged, don't drift)
- **Theme:** dark-first, with a working light mode and the sun/moon toggle.
- **Colours:** page `#0a0a0c`, cards `#131316`, borders `#1e1e24`. Accents `#ff6b6b` (Greece) and `#9b5de5` (Rome), plus `#f4a261`, `#2a9d8f`, `#457b9d`, `#e9c46a`. No grey as a dominant accent.
- **Fonts:** DM Sans for text, Space Mono for labels, Gentium Book Plus for Greek or Latin display words.
- **Layout:** mobile-first, 700 px column on a phone (760 px from 768 px, with a persistent 300 px sidebar from 1100 px; `design/theme.css` section 6), its own viewport meta tag on every page (`build.py` writes it), 44 px touch targets, fixed frosted top bar, full-height slide-out drawer (a sidebar on a desktop).

## How to work with me
- Be direct and terse.
- One-line progress updates as each unit lands.
- At the end, a short summary of what changed, with the `review_due.py` line as its first line.
- Two rules of 27 October 2026 apply to every new report: the word target is a guide, not a limit (`check.py` no longer fails on length; never pad, never cut substance); and each writer leaves `bibliography/<course>/r-<id>.md` beside the report (`WRITER-BRIEF.md`).
