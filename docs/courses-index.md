# Courses index

Every course and every unit in the Learning Project, in build order, with status, the model that wrote it, the search flag and where the unit lives. State as of 30 October 2026 (User Experience family and course IA added 29 October, IA1 and IA2 written 30 October; Personal Mythology: end of the third Fable review session, plus the decisions of 28 October in `pm-status-2026-10-28.md` and `academy.md`, and A1 to A5 done: the site is Academy; Brand + AI v7.3, B2 filed, DD-B3 added, P27 figures in A2, A9, B2; Brand + AI v7.8 on 29 Oct 2026, Audit 2 run; v8.0, A3 filed; v8.1, B5 filed; v8.2, A4 filed). Update a row whenever a unit is filed or audited (method.md §7). `kit/index_check.py` checks every unit row, count line and staleness date against the syllabi, `kit/provenance.json`, the vault and the data files; `kit/verify.py` runs it. The notes, review rows and audit counters are not checked (the counters wait for S3).

Paths, all in the repo https://github.com/apcanario/learning: `kit/` is the Personal Mythology kit; `vault/` is `courses/`; `gen/` is `generator/`. Units not yet written show the vault path they will be filed at.

## Hubs

| Hub | Page | Link | Built from |
|---|---|---|---|
| Academy | The one site: the Academy home listing every course by track, with the Changelog and the Backlog; Greece and Rome in full (syllabi, every report); Brand + AI as two courses (A, B), each with its units, briefs, build order, audits, bibliography and changelog; User Experience with its first course IA (coming soon, 29 Oct 2026); the eight history courses to come | https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH (version 55 onward, 28 Oct) · GitHub Pages: https://apcanario.github.io/academy/ (`kit/deploy.sh` through the public repo `apcanario/academy`) | kit `build.py` from `kit/courses.py` (`family` history or markdown; markdown through `kit/mdcourse.py`), `shell.css` = `design/theme.css`; A1, A3 and A2 of `academy.md` done 28 Oct: the build is `kit/academy/`, a shell plus one file per report fetched on navigation (sizes in `kit/README.md`); publish with `kit/publish_files.py` |

A5 done 28 Oct 2026: the Brand + AI units are read from the vault, `courses/brand-ai/` (no copy under `gen/`); a new course of either family is a folder plus a `kit/courses.py` entry.

A4 done 28 Oct 2026: every course has a generated "How it was built" page (`#greece-built`, `#rome-built`, `#brand-a-built`, `#brand-b-built`; `kit/howbuilt.py`).

A3 done 28 Oct 2026: the Brand + AI courses are read in Academy (`#brand-a`, `#brand-b`; each unit at `#read-<code>`, the superseded research at `#read-audience-growth`), built by `kit/build.py` through `kit/mdcourse.py` from `gen/data/brand-ai/hub.py`. The Brand + AI hub artifact and the Audience Growth artifact are retired.

Retired 28 October 2026 (deleted): the standalone Hellas Syllabus and Roma Syllabus artifacts, and the three stray draft pages (r-3.2, r-3.3, r-11.6). The site's `#syllabus` and `#rome-syllabus` panels are the only published syllabi; `kit/greek-syllabus.html` and `kit/roman-syllabus.html` remain as build inputs.

## Audit counters

| Hub | Units since last audit | Next audit | Note |
|---|---|---|---|
| Brand + AI | 4 of 4 (Audit 2 ran 29 Oct 2026; DD-B3, A3, B5, A4 since) | Audit 3 now (DD-B3, A3, B5, A4), before A5 | Audit 1: B1 PASS; A2·A6·A9 REWRITE, rewritten 28 Oct 2026. Audit 2 (29 Oct 2026): B2, B3, B4, A1 all PASS; B2 errata for Intelligence Index v5.0 and one miscite, A1 erratum (P33), applied. DD-B3, A3, B5 and A4 filed 29 Oct 2026; Audit 3 next, before A5. Fresh checker required for every Brand + AI unit (method §1 override). |
| User Experience | 2 of 4 (IA1, IA2 since) | Audit 1 after IA4 (deferred by Pedro 29 Oct 2026, row P49) | Course IA created 29 Oct 2026; IA1 and IA2 filed 30 Oct 2026. Fresh checker required for every unit, as for Brand + AI (Opus 5.5 for IA1 to IA3; Fable 5.1 checks owed, P49). |
| Personal Mythology | 4 of 4 modules (Rome 11.3, 11.4, 11.5, 11.6; Greece and Rome pooled; `kit/review_due.py`) | due now (FABLE REVIEW DUE), deferred to the Fable stage at the end of the queue (Pedro, 31 Oct 2026); batch 2 goes on (batch plan in `kit/BACKLOG.md`) | Decision of 28 October 2026: strict four-module cadence per method.md §6; `kit/review_due.py` counts modules since S3 (1 Nov 2026), from the `review_mark` in `kit/provenance.json`. Six Greek reports still flagged from the 27 October review and carried by that mark, so not counted: 11.1, 11.2, 11.4, 11.5, 11.6, 11.8 (`NEXT-SESSION.md`, S4) |

## Staleness checks due (search-on units)

| Unit | Written | Check due |
|---|---|---|
| A2 | 28 Oct 2026 (rewrite) | 28 Apr 2027 |
| A6 | 28 Oct 2026 (rewrite) | 28 Apr 2027 |
| A9 | 28 Oct 2026 (rewrite) | 28 Apr 2027 |
| B1 | 28 Oct 2026 (search on: Anthropic product facts) | 28 Apr 2027 |
| B2 | 28 Oct 2026 (search on: lineups, prices, plan rules, benchmarks) | 28 Apr 2027 |
| DD-B3 | 29 Oct 2026 (search on: practitioners' posts, repositories, papers) | 29 Apr 2027 |

## Brand + AI

Two courses for one reader. **A · Building a Marketable Personal Brand** (9 core units, 2 deep dives) and **B · Using AI to Build a Brand** (8 core, 3 deep dives; DD-B3 added 28 Oct 2026). 12 of 22 written. A unit is written when its file is in `courses/brand-ai/` (A5: Academy reads it from there). Briefs: each course's Briefs page in Academy (`gen/data/brand-ai/units_data.py`). Build order: the Build order page.

| # | Unit | Course | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| — | Research | A | Audience growth across platforms (research, superseded) | written 27 Oct 2026 across five tracks; Audit 1 (28 Oct) found 23 of 91 claims failing and the deliverables missing, REWRITE for A2, A6 and A9; kept as the record (`#read-audience-growth`) | Fable 5.1 research agents | on | `gen/data/brand-ai/audience-growth-across-platforms.md` |
| 1 | A9 | A | What to expect: benchmarks | rewritten 28 Oct 2026 from its brief after Audit 1's REWRITE (own chat); fresh check Fable 5.1 fix, 2 errors, 15 should-fix, 8 minor, applied; report `audits/brand-ai/fresh-check-A9.md`; figure added 28 Oct (P27: crossing 1,000 by videos added, §3) | Opus 5.5 | on | `courses/brand-ai/A9-what-to-expect-benchmarks.md` |
| 2 | A2 | A | Audience and platform economics | rewritten 28 Oct 2026 from its brief after Audit 1's REWRITE (own chat); fresh check Fable 5.1 fix, 3 errors, 13 should-fix, 11 minor, applied; report `audits/brand-ai/fresh-check-A2.md`; figure added 28 Oct (P27: Pew ever-use by platform, §2) | Opus 5.5 | on | `courses/brand-ai/A2-audience-and-platform-economics.md` |
| 3 | A6 | A | How growth works, per platform | rewritten 28 Oct 2026 from its brief after Audit 1's REWRITE (own chat); fresh check Fable 5.1 fix, 1 error, 9 should-fix, 7 minor, applied; report `audits/brand-ai/fresh-check-A6.md` | Opus 5.5 | on | `courses/brand-ai/A6-how-growth-works-per-platform.md` |
| 4 | B1 | B | Mental model | written 28 Oct 2026 | Opus 5.5 | on (writer's call: dated product facts) | `courses/brand-ai/B1-mental-model.md` |
| ✓ | Audit 1 | A+B | Stratified-sample audit of the last four units | run 28 Oct 2026: B1 PASS, A2·A6·A9 REWRITE | Fable 5.1 | on | `audits/brand-ai/audit-1.html` (saved from the artifact) |
| 5 | B2 | B | Choosing the model | written 28 Oct 2026 (own chat; fresh check Fable 5.1 fix, 3 errors, 10 should-fix, 14 minor, applied; report `audits/brand-ai/fresh-check-B2.md`; figure added 28 Oct, P27: output price per model, §3; Audit 2 29 Oct: PASS, errata B2-1 to B2-25 applied) | Opus 5.5 | on | `courses/brand-ai/B2-choosing-the-model.md` |
| 6 | B3 | B | Prompting that holds up | written 29 Oct 2026 (own context; fresh check Fable 5.1 fix, 1 error, 4 should-fix, 9 minor, applied; report `audits/brand-ai/fresh-check-B3.md`) | Opus 5.5 | off | `courses/brand-ai/B3-prompting-that-holds-up.md` |
| 7 | B4 | B | Context engineering | written 29 Oct 2026 (own context; fresh check Fable 5.1 fix, 0 errors, 7 should-fix, 9 minor, applied; report `audits/brand-ai/fresh-check-B4.md`) | Opus 5.5 | off | `courses/brand-ai/B4-context-engineering.md` |
| 8 | A1 | A | Positioning: the journey as a format | written 29 Oct 2026 (own context, written out of order beside B3; fresh check Fable 5.1 fix, 1 error, 4 should-fix, 6 minor, applied; report `audits/brand-ai/fresh-check-A1.md`; §6 rewritten 29 Oct 2026 from the two episodes (P28), fresh check Fable 5.1 fix, 1 error, 1 should-fix, 3 minor, applied; report `audits/brand-ai/fresh-check-A1-s6.md`; Audit 2 29 Oct: PASS, erratum A1-1 (P33) applied) | Opus 5.5 | off | `courses/brand-ai/A1-positioning-the-journey-as-a-format.md` |
| ✓ | Audit 2 | A+B | Stratified-sample audit of the last four units | run 29 Oct 2026: B2, B3, B4, A1 PASS (96 claims checked; 1 FAIL, 10 STALE, all B2; errata B2-1 to B2-25 and A1-1 applied) | Fable 5.1 | on | `audits/brand-ai/audit-2.md` |
| 9 | DD-B3 | B | Deep dive: how the best practitioners use the tool | written 29 Oct 2026 (own context; fresh check Fable 5.1 fix, 1 error, 3 should-fix, 9 minor, applied; report `audits/brand-ai/fresh-check-DD-B3.md`; erratum 1 Nov 2026, H-3 P77: the "Evidence grades" paragraph moved, words unchanged, from the opening to the top of §1.0, and the opening's "Three limits shape what follows" made "Two limits shape this unit") | Opus 5.5 | on | `courses/brand-ai/DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md` |
| 10 | A3 | A | The journey system | written 29 Oct 2026 (own context; fresh check Fable 5.1 keep, 0 errors, 1 should-fix, 9 minor, applied; report `audits/brand-ai/fresh-check-A3.md`) | Opus 5.5 | off | `courses/brand-ai/A3-the-journey-system.md` |
| 11 | B5 | B | Skills and automation | written 29 Oct 2026 (own context; fresh check Fable 5.1 fix, 1 error, 4 should-fix, 5 minor, applied; report `audits/brand-ai/fresh-check-B5.md`) | Opus 5.5 | off | `courses/brand-ai/B5-skills-and-automation.md` |
| 12 | A4 | A | Voice, disclosure and the record | written 29 Oct 2026 (own context; fresh check Fable 5.1 fix, 2 errors, 3 should-fix, 8 minor, applied; report `audits/brand-ai/fresh-check-A4.md`) | Opus 5.5 | off | `courses/brand-ai/A4-voice-disclosure-and-the-record.md` |
| ✓ | Audit 3 | A+B | Stratified-sample audit of the last four units | due now (DD-B3, A3, B5, A4), before #13 | Fable 5.1 | on | hub Audits page |
| 13 | A5 | A | Production craft | not written | Opus 5.5 | off | `courses/brand-ai/A5-production-craft.md` |
| 14 | B7 | B | Content pipeline | not written | Opus 5.5 | off | `courses/brand-ai/B7-content-pipeline.md` |
| 15 | A7 | A | Monetisation through Shōmen | not written | Opus 5.5 | off | `courses/brand-ai/A7-monetisation-through-shomen.md` |
| 16 | A8 | A | Legal, tax, time | not written | Opus 5.5 | on | `courses/brand-ai/A8-legal-tax-time.md` |
| ✓ | Audit 4 | A+B | Stratified-sample audit of the last four units | due after #16 | Fable 5.1 | on | hub Audits page |
| 17 | B6 | B | Research and verification | not written | Opus 5.5 | off | `courses/brand-ai/B6-research-and-verification.md` |
| 18 | B8 | B | Cost, limits, hygiene | not written | Opus 5.5 | on | `courses/brand-ai/B8-cost-limits-hygiene.md` |
| 19 | DD-A1 | A | Deep dive: five creators who did this | not written | Opus 5.5 | on | `courses/brand-ai/DD-A1-deep-dive-five-creators-who-did-this.md` |
| 20 | DD-B1 | B | Deep dive: agents | not written | Opus 5.5 | off | `courses/brand-ai/DD-B1-deep-dive-agents.md` |
| ✓ | Audit 5 | A+B | Stratified-sample audit of the last four units | due after #20 | Fable 5.1 | on | hub Audits page |
| 21 | DD-A2 | A | Deep dive: the exit math | not written | Opus 5.5 | off | `courses/brand-ai/DD-A2-deep-dive-the-exit-math.md` |
| 22 | DD-B2 | B | Deep dive: his unknown unknowns | not written | Fable 5.1 | off | `courses/brand-ai/DD-B2-deep-dive-his-unknown-unknowns.md` |
| ✓ | Audit 6 | A+B | Final audit of DD-B2 plus a full read of both courses against their goals | after #22 | Fable 5.1 | on | hub Audits page |

## User Experience

The family for courses written to be handed to other designers: the Project's one exception to its single-reader rule (decided 29 Oct 2026); the reader is the persona in each brief's preamble, and `reader.md` is unchanged. First course: **IA · Information Architecture**, twelve core units in four parts (foundations and notation; the four levels of complexity on the fictional Perqo; IA in the lifecycle and across the business; working without the inputs) and three deep dives. 2 of 15 written (IA1, IA2, 30 Oct 2026). Status: in progress. A unit is written when its file is in `courses/ux/` (the folder appears with the first one). Briefs: the course's Briefs page in Academy (`gen/data/ux/units_data.py`). Build order: the Build order page. Before IA1: the IA figure kinds for `kit/viz.py` (backlog row V1).

| # | Unit | Course | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | IA1 | IA | What information architecture is, and where it sits | written 30 Oct 2026 (isolated agent context, P31; fresh check Opus 5.5 keep, 0 errors, 4 should-fix, 7 minor, applied; report `audits/ux/fresh-check-IA1.md`; Fable 5.1 fresh check owed, P49; figure erratum 1 Nov 2026, H-3 P76: figure 2's caption) | Opus 5.5 | off | `courses/ux/IA1-what-information-architecture-is-and-where-it-sits.md` |
| 2 | IA2 | IA | The shapes IA takes: the artefact catalogue and the course notation | written 30 Oct 2026 (isolated agent context, P31; fresh check Opus 5.5 fix, 3 errors, 10 should-fix, 17 minor, applied; report `audits/ux/fresh-check-IA2.md`; Fable 5.1 fresh check owed, P49; erratum 1 Nov 2026, H-3 P74 and P75: the reading-direction triangle added to §5.2, the legend and the notation sheet; the legend's Screen, Surface: Label and dashed-line rows and its WCAG 2.2 caption; the cross-surface map redrawn on a grid with two crossings and every label clear, verb labels from IA1's table (text changed with them), counts, [over the limit], caption citations; the owed Fable 5.1 check covers it) | Opus 5.5 | off | `courses/ux/IA2-the-shapes-ia-takes-the-artefact-catalogue-and-the-course-notation.md` |
| 3 | IA3 | IA | How people find and understand things | not written | Opus 5.5 | off | `courses/ux/IA3-how-people-find-and-understand-things.md` |
| 4 | IA4 | IA | Organisation systems: schemes, structures, objects, taxonomies | not written | Opus 5.5 | off | `courses/ux/IA4-organisation-systems-schemes-structures-objects-taxonomies.md` |
| ✓ | Audit 1 | IA | Stratified-sample audit of the last four units | due after #4 | Fable 5.1 | on | course Audits page |
| 5 | IA5 | IA | Level 1 · the sales and product website | not written | Opus 5.5 | off | `courses/ux/IA5-level-1-the-sales-and-product-website.md` |
| 6 | IA6 | IA | Level 2 · the client app | not written | Opus 5.5 | off | `courses/ux/IA6-level-2-the-client-app.md` |
| 7 | IA7 | IA | Level 3 · the backoffice | not written | Opus 5.5 | off | `courses/ux/IA7-level-3-the-backoffice.md` |
| 8 | IA8 | IA | Level 4 · the system map | not written | Opus 5.5 | off | `courses/ux/IA8-level-4-the-system-map.md` |
| ✓ | Audit 2 | IA | Stratified-sample audit of the last four units | due after #8 | Fable 5.1 | on | course Audits page |
| 9 | IA9 | IA | IA in the product development lifecycle | not written | Opus 5.5 | off | `courses/ux/IA9-ia-in-the-product-development-lifecycle.md` |
| 10 | IA10 | IA | Touchpoints: what each part of the business needs from the IA | not written | Opus 5.5 | off | `courses/ux/IA10-touchpoints-what-each-part-of-the-business-needs-from-the-ia.md` |
| 11 | IA11 | IA | Validating an IA: evidence, methods, numbers | not written | Opus 5.5 | off | `courses/ux/IA11-validating-an-ia-evidence-methods-numbers.md` |
| 12 | IA12 | IA | When the inputs are missing: building the backbone anyway | not written | Opus 5.5 | off | `courses/ux/IA12-when-the-inputs-are-missing-building-the-backbone-anyway.md` |
| ✓ | Audit 3 | IA | Stratified-sample audit of the last four units | due after #12 | Fable 5.1 | on | course Audits page |
| 13 | DD-IA1 | IA | Deep dive: five information architectures read closely | not written | Opus 5.5 | on | `courses/ux/DD-IA1-deep-dive-five-information-architectures-read-closely.md` |
| 14 | DD-IA2 | IA | Deep dive: what IA costs and returns | not written | Opus 5.5 | on | `courses/ux/DD-IA2-deep-dive-what-ia-costs-and-returns.md` |
| 15 | DD-IA3 | IA | Deep dive: taxonomy and governance at scale | not written | Opus 5.5 | off | `courses/ux/DD-IA3-deep-dive-taxonomy-and-governance-at-scale.md` |
| ✓ | Audit 4 | IA | Final audit of the three deep dives plus a full read of the course against its goal, and a read-through as the persona | after #15 | Fable 5.1 | on | course Audits page |

## Personal Mythology

One reader, one civilisation at a time; each module a long-form report with named sources, dispute boxes, a ten-question self-test and three carry-forward ideas. Model column: the model that wrote the report (`kit/provenance.json`). "Flagged" means not yet reviewed with Fable 5.1. All modules: search off.

### Greece (course 1)

Complete: 78 of 78 content reports; 83 modules with the audit unit. Written in syllabus order.

| # | Module | Syllabus unit | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | 0.1 | 0 · Foundations | How we know anything: the sources | written | Fable 5.1 | off | `kit/greece/r-0.1.html` |
| 2 | 0.2 | 0 · Foundations | Geography, dialects and the shape of Greece | written | Fable 5.1 | off | `kit/greece/r-0.2.html` |
| 3 | 0.3 | 0 · Foundations | The timeline spine, 3000 BC to AD 529 | written | Fable 5.1 | off | `kit/greece/r-0.3.html` |
| 4 | 1.1 | 1 · The Bronze Age and the long dark | Minoan Crete | written | Fable 5.1 | off | `kit/greece/r-1.1.html` |
| 5 | 1.2 | 1 · The Bronze Age and the long dark | Mycenaean Greece | written | Fable 5.1 | off | `kit/greece/r-1.2.html` |
| 6 | 1.3 | 1 · The Bronze Age and the long dark | The collapse of 1200 and the Dark Age | written | Fable 5.1 | off | `kit/greece/r-1.3.html` |
| 7 | 2.1 | 2 · Mythology I: the cosmos and the gods | Cosmogony: Chaos to Zeus | written | Fable 5.1 | off | `kit/greece/r-2.1.html` |
| 8 | 2.2 | 2 · Mythology I: the cosmos and the gods | The Twelve Olympians | written | Fable 5.1 | off | `kit/greece/r-2.2.html` |
| 9 | 2.3 | 2 · Mythology I: the cosmos and the gods | The underworld and the chthonic gods | written | Fable 5.1 | off | `kit/greece/r-2.3.html` |
| 10 | 2.4 | 2 · Mythology I: the cosmos and the gods | Prometheus, Pandora, the Five Ages and the Flood | written | Fable 5.1 | off | `kit/greece/r-2.4.html` |
| 11 | 2.5 | 2 · Mythology I: the cosmos and the gods | The lesser divinities and personifications | written | Fable 5.1 | off | `kit/greece/r-2.5.html` |
| 12 | 2.6 | 2 · Mythology I: the cosmos and the gods | The monsters and their genealogy | written | Fable 5.1 | off | `kit/greece/r-2.6.html` |
| 13 | 3.1 | 3 · Mythology II: the heroes | What a hero is, and Perseus | written | Fable 5.1 | off | `kit/greece/r-3.1.html` |
| 14 | 3.2 | 3 · Mythology II: the heroes | Heracles | written | Fable 5.1 | off | `kit/greece/r-3.2.html` |
| 15 | 3.3 | 3 · Mythology II: the heroes | Theseus and Athens | written | Fable 5.1 | off | `kit/greece/r-3.3.html` |
| 16 | 3.4 | 3 · Mythology II: the heroes | Jason, the Argonauts and Medea | written | Fable 5.1 | off | `kit/greece/r-3.4.html` |
| 17 | 3.5 | 3 · Mythology II: the heroes | The Theban cycle: Cadmus to Antigone | written | Fable 5.1 | off | `kit/greece/r-3.5.html` |
| 18 | 3.6 | 3 · Mythology II: the heroes | The other heroes: Bellerophon, Meleager, Atalanta, Pelops, Tantalus | written | Fable 5.1 | off | `kit/greece/r-3.6.html` |
| 19 | 3.7 | 3 · Mythology II: the heroes | Love, hubris and metamorphosis | written | Fable 5.1 | off | `kit/greece/r-3.7.html` |
| 20 | 4.1 | 4 · Mythology III: the Trojan cycle | Causes of the war and the gathering at Aulis | written | Fable 5.1 | off | `kit/greece/r-4.1.html` |
| 21 | 4.2 | 4 · Mythology III: the Trojan cycle | The Iliad | written | Fable 5.1 | off | `kit/greece/r-4.2.html` |
| 22 | 4.3 | 4 · Mythology III: the Trojan cycle | The fall of Troy: the lost Epic Cycle | written | Fable 5.1 | off | `kit/greece/r-4.3.html` |
| 23 | 4.4 | 4 · Mythology III: the Trojan cycle | The Returns and the Odyssey | written | Fable 5.1 | off | `kit/greece/r-4.4.html` |
| 24 | 4.5 | 4 · Mythology III: the Trojan cycle | The house of Atreus after Troy | written | Fable 5.1 | off | `kit/greece/r-4.5.html` |
| 25 | 5.1 | 5 · The Archaic age, 800 to 480 BC | The eighth-century renaissance | written | Fable 5.1 | off | `kit/greece/r-5.1.html` |
| 26 | 5.2 | 5 · The Archaic age, 800 to 480 BC | The polis and colonisation | written | Fable 5.1 | off | `kit/greece/r-5.2.html` |
| 27 | 5.3 | 5 · The Archaic age, 800 to 480 BC | Hoplites, lawgivers and tyrants | written | Fable 5.1 | off | `kit/greece/r-5.3.html` |
| 28 | 5.4 | 5 · The Archaic age, 800 to 480 BC | Sparta | written | Fable 5.1 | off | `kit/greece/r-5.4.html` |
| 29 | 5.5 | 5 · The Archaic age, 800 to 480 BC | Athens from Solon to Cleisthenes | written | Fable 5.1 | off | `kit/greece/r-5.5.html` |
| 30 | 5.6 | 5 · The Archaic age, 800 to 480 BC | Lyric poets and the first philosophers | written | Fable 5.1 | off | `kit/greece/r-5.6.html` |
| 31 | 6.1 | 6 · The Classical age, 480 to 323 BC | The Persian Wars | written | Fable 5.1 | off | `kit/greece/r-6.1.html` |
| 32 | 6.2 | 6 · The Classical age, 480 to 323 BC | The Athenian empire and the radical democracy | written | Fable 5.1 | off | `kit/greece/r-6.2.html` |
| 33 | 6.3 | 6 · The Classical age, 480 to 323 BC | The Peloponnesian War | written | Fable 5.1 | off | `kit/greece/r-6.3.html` |
| 34 | 6.4 | 6 · The Classical age, 480 to 323 BC | Tragedy and comedy | written | Fable 5.1 | off | `kit/greece/r-6.4.html` |
| 35 | 6.5 | 6 · The Classical age, 480 to 323 BC | The Sophists, Socrates, Plato and Aristotle | written | Fable 5.1 | off | `kit/greece/r-6.5.html` |
| 36 | 6.6 | 6 · The Classical age, 480 to 323 BC | The fourth century: Sparta, Thebes, Philip | written | Fable 5.1 | off | `kit/greece/r-6.6.html` |
| 37 | 6.7 | 6 · The Classical age, 480 to 323 BC | Alexander | written | Fable 5.1 | off | `kit/greece/r-6.7.html` |
| 38 | 7.1 | 7 · Hellenistic and Roman Greece, 323 BC to AD 529 | The Successors and the kingdoms | written | Fable 5.1 | off | `kit/greece/r-7.1.html` |
| 39 | 7.2 | 7 · Hellenistic and Roman Greece, 323 BC to AD 529 | Alexandria: science, scholarship and the new philosophies | written | Fable 5.1 | off | `kit/greece/r-7.2.html` |
| 40 | 7.3 | 7 · Hellenistic and Roman Greece, 323 BC to AD 529 | Rome conquers Greece | written | Fable 5.1 | off | `kit/greece/r-7.3.html` |
| 41 | 7.4 | 7 · Hellenistic and Roman Greece, 323 BC to AD 529 | Greece under the Empire and the end of antiquity | written | Fable 5.1 | off | `kit/greece/r-7.4.html` |
| 42 | 8.1 | 8 · Religion and daily life | Ritual practice: sacrifice, temples, priests, pollution | written | Fable 5.1 | off | `kit/greece/r-8.1.html` |
| 43 | 8.2 | 8 · Religion and daily life | Oracles and mystery cults | written | Fable 5.1 | off | `kit/greece/r-8.2.html` |
| 44 | 8.3 | 8 · Religion and daily life | Festivals and the games | written | Fable 5.1 | off | `kit/greece/r-8.3.html` |
| 45 | 8.4 | 8 · Religion and daily life | Death, the afterlife and hero cult | written | Fable 5.1 | off | `kit/greece/r-8.4.html` |
| 46 | 8.5 | 8 · Religion and daily life | Households, women, slaves, the symposium and sexuality | written | Fable 5.1 | off | `kit/greece/r-8.5.html` |
| 47 | 9.1 | 9 · Art, the ground, and the afterlife of it all | Reading Greek art: temples, sculpture, vases | written | Fable 5.1 | off | `kit/greece/r-9.1.html` |
| 48 | 9.2 | 9 · Art, the ground, and the afterlife of it all | Reading a site: Athens on foot | written | Fable 5.1 | off | `kit/greece/r-9.2.html` |
| 49 | 9.3 | 9 · Art, the ground, and the afterlife of it all | Reception: how it all reached you | written | Fable 5.1 | off | `kit/greece/r-9.3.html` |
| 50 | 9.4 | 9 · Art, the ground, and the afterlife of it all | Capstone: the whole thing in one sitting | written | Fable 5.1 | off | `kit/greece/r-9.4.html` |
| 51 | 10.1 | 10 · Deep dive I: the Trojan War | Achilles | written | Fable 5.1 | off | `kit/greece/r-10.1.html` |
| 52 | 10.2 | 10 · Deep dive I: the Trojan War | Agamemnon and the kingship of the Atreids | written | Fable 5.1 | off | `kit/greece/r-10.2.html` |
| 53 | 10.3 | 10 · Deep dive I: the Trojan War | Hector, Priam and the Trojan side | written | Fable 5.1 | off | `kit/greece/r-10.3.html` |
| 54 | 10.4 | 10 · Deep dive I: the Trojan War | Odysseus | written · reviewed | Opus 5.5 | off | `kit/greece/r-10.4.html` |
| 55 | 10.5 | 10 · Deep dive I: the Trojan War | Helen, Menelaus and Sparta | written | Fable 5.1 | off | `kit/greece/r-10.5.html` |
| 56 | 10.6 | 10 · Deep dive I: the Trojan War | Reading the Iliad closely: Books 1, 6, 9, 16, 18, 22, 24 | written | Fable 5.1 | off | `kit/greece/r-10.6.html` |
| 57 | 10.7 | 10 · Deep dive I: the Trojan War | Reading the Odyssey closely: the Telemachy, the Apologoi, the Nekyia, the recognitions | written · reviewed | Opus 5.5 | off | `kit/greece/r-10.7.html` |
| 58 | 10.8 | 10 · Deep dive I: the Trojan War | The other Greeks at Troy | written · reviewed | Opus 5.5 | off | `kit/greece/r-10.8.html` |
| 59 | 10.9 | 10 · Deep dive I: the Trojan War | The gods at Troy | written · reviewed | Opus 5.5 | off | `kit/greece/r-10.9.html` |
| 60 | 10.10 | 10 · Deep dive I: the Trojan War | Troy the place: Hisarlik and the historicity question | written · reviewed | Opus 5.5 | off | `kit/greece/r-10.10.html` |
| 61 | 10.11 | 10 · Deep dive I: the Trojan War | Homeric society and Homeric warfare | written · reviewed | Opus 5.5 | off | `kit/greece/r-10.11.html` |
| 62 | 10.12 | 10 · Deep dive I: the Trojan War | Troy after antiquity | written · reviewed | Opus 5.5 | off | `kit/greece/r-10.12.html` |
| 63 | 11.1 | 11 · Deep dive II: Alexander | Macedon before Alexander | written · flagged for Fable review | Opus 5.5 | off | `kit/greece/r-11.1.html` |
| 64 | 11.2 | 11 · Deep dive II: Alexander | Alexander's generalship: the battles and sieges | written · flagged for Fable review | Opus 5.5 | off | `kit/greece/r-11.2.html` |
| 65 | 11.3 | 11 · Deep dive II: Alexander | The Achaemenid side | written · reviewed | Opus 5.5 | off | `kit/greece/r-11.3.html` |
| 66 | 11.4 | 11 · Deep dive II: Alexander | Alexander and the gods | written · flagged for Fable review | Opus 5.5 | off | `kit/greece/r-11.4.html` |
| 67 | 11.5 | 11 · Deep dive II: Alexander | The court: Companions, conspiracies and the orientalising policy | written · flagged for Fable review | Opus 5.5 | off | `kit/greece/r-11.5.html` |
| 68 | 11.6 | 11 · Deep dive II: Alexander | The eastern campaign: Bactria, Sogdiana, India and the return | written · flagged for Fable review | Opus 5.5 | off | `kit/greece/r-11.6.html` |
| 69 | 11.7 | 11 · Deep dive II: Alexander | The sources for Alexander | written · reviewed | Opus 5.5 | off | `kit/greece/r-11.7.html` |
| 70 | 11.8 | 11 · Deep dive II: Alexander | Death, body and afterlives | written · flagged for Fable review | Opus 5.5 | off | `kit/greece/r-11.8.html` |
| 71 | 12.1 | 12 · Deep dive III: Greek philosophy | The Presocratics | written · reviewed | Opus 5.5 | off | `kit/greece/r-12.1.html` |
| 72 | 12.2 | 12 · Deep dive III: Greek philosophy | The Sophists and Socrates | written · reviewed (sampled) | Opus 5.5 | off | `kit/greece/r-12.2.html` |
| 73 | 12.3 | 12 · Deep dive III: Greek philosophy | Plato | written · reviewed (sampled) | Opus 5.5 | off | `kit/greece/r-12.3.html` |
| 74 | 12.4 | 12 · Deep dive III: Greek philosophy | Aristotle | written · reviewed (sampled) | Opus 5.5 | off | `kit/greece/r-12.4.html` |
| 75 | 12.5 | 12 · Deep dive III: Greek philosophy | Cynics, Cyrenaics and the other Socratic schools | written · reviewed (sampled) | Opus 5.5 | off | `kit/greece/r-12.5.html` |
| 76 | 12.6 | 12 · Deep dive III: Greek philosophy | Epicurus and the Garden | written · reviewed | Opus 5.5 | off | `kit/greece/r-12.6.html` |
| 77 | 12.7 | 12 · Deep dive III: Greek philosophy | The Stoa from Zeno to Posidonius | written · reviewed (sampled) | Opus 5.5 | off | `kit/greece/r-12.7.html` |
| 78 | 12.8 | 12 · Deep dive III: Greek philosophy | Sceptics and Neoplatonists: the late schools to 529 | written · reviewed (sampled) | Opus 5.5 | off | `kit/greece/r-12.8.html` |
| ✓ | 13.1 | 13 · Quality audit | Calibrate the rubric | run 27 Oct 2026 (`kit/audits/greece-13.1-rubric.md`) | Fable 5.1 | off | `kit/audits/` |
| ✓ | 13.2 | 13 · Quality audit | Audit one report | in progress: 17 of 23 Opus reports cleared (11 audited, 6 on the sample); 11.1, 11.2, 11.4, 11.5, 11.6, 11.8 remain (S4) | Fable 5.1 | off | `kit/audits/` |
| ✓ | 13.3 | 13 · Quality audit | Deep-dive overlap check | partly run: six repeated disputes homed, six pairs read; 32 pairs measured mechanically only | Fable 5.1 | off | `kit/audits/` |
| ✓ | 13.4 | 13 · Quality audit | Compare the cohorts | interim decision recorded (`kit/audits/greece-13.4-cohorts.md`); final after 13.2 | Fable 5.1 | off | `kit/audits/` |
| ✓ | 13.5 | 13 · Quality audit | Fix a report | in progress with 13.2 | Fable 5.1 | off | `kit/audits/` |

### Rome (course 2)

In progress: 71 of 79 content reports; 85 modules with the audit unit. Written in syllabus order to 10.5, with 11.1 to 11.7, 12.1, 13.1 to 13.8 (batch 1, 11.3 to 11.6, written 1 Nov 2026, R-1; the rest written 1 Nov 2026, R-2). The 16 still to write go in batches of four, a Fable review after each (decision of 28 October 2026; `pm-status-2026-10-28.md` S3): batch 1 = 11.3, 11.4, 11.5, 11.6; batch 2 = 11.7, 11.8, 13.3, 13.4; batch 3 = 13.5, 13.6, 13.7, 13.8; batch 4 = 12.1, 12.2, 12.3, 12.4; batch 5 = 12.5, 12.7, 12.8, 12.6. The dependency rules of `kit/BACKLOG.md` hold inside the batches (11.8 last in its unit; 12.6 after 13.2).

| # | Module | Syllabus unit | Title | Status | Model | Search | Path |
|---|---|---|---|---|---|---|---|
| 1 | 0.1 | 0 · Foundations | How we know anything: the sources | written · reviewed | Opus 5.5 | off | `kit/rome/r-0.1.html` |
| 2 | 0.2 | 0 · Foundations | Italy and the Mediterranean: the shape of Rome's world | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-0.2.html` |
| 3 | 0.3 | 0 · Foundations | The timeline spine, 1000 BC to AD 476 | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-0.3.html` |
| 4 | 1.1 | 1 · Italy before Rome and the founding legends | The peoples of Iron Age Italy | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-1.1.html` |
| 5 | 1.2 | 1 · Italy before Rome and the founding legends | The Etruscans | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-1.2.html` |
| 6 | 1.3 | 1 · Italy before Rome and the founding legends | Before Romulus: Evander, Hercules and Aeneas | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-1.3.html` |
| 7 | 1.4 | 1 · Italy before Rome and the founding legends | Romulus and Remus | written · reviewed | Opus 5.5 | off | `kit/rome/r-1.4.html` |
| 8 | 1.5 | 1 · Italy before Rome and the founding legends | The seven kings | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-1.5.html` |
| 9 | 1.6 | 1 · Italy before Rome and the founding legends | The fall of the monarchy: Lucretia, Brutus and Porsenna | written · reviewed | Opus 5.5 | off | `kit/rome/r-1.6.html` |
| 10 | 2.1 | 2 · The gods of Rome | What Roman religion was | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-2.1.html` |
| 11 | 2.2 | 2 · The gods of Rome | The gods of Rome and their Greek doubles | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-2.2.html` |
| 12 | 2.3 | 2 · The gods of Rome | Priests, augury and the calendar | written · reviewed | Opus 5.5 | off | `kit/rome/r-2.3.html` |
| 13 | 2.4 | 2 · The gods of Rome | House, family and the dead | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-2.4.html` |
| 14 | 2.5 | 2 · The gods of Rome | New gods: Cybele, Bacchus, Isis, Mithras and the Christians | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-2.5.html` |
| 15 | 3.1 | 3 · The early Republic and the conquest of Italy, 509 to 264 BC | The Struggle of the Orders | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-3.1.html` |
| 16 | 3.2 | 3 · The early Republic and the conquest of Italy, 509 to 264 BC | The legends of the early Republic | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-3.2.html` |
| 17 | 3.3 | 3 · The early Republic and the conquest of Italy, 509 to 264 BC | Veii, the Gauls and Camillus | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-3.3.html` |
| 18 | 3.4 | 3 · The early Republic and the conquest of Italy, 509 to 264 BC | The Samnite Wars and the Roman system in Italy | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-3.4.html` |
| 19 | 3.5 | 3 · The early Republic and the conquest of Italy, 509 to 264 BC | Pyrrhus and the Greek south | written · reviewed | Opus 5.5 | off | `kit/rome/r-3.5.html` |
| 20 | 4.1 | 4 · Carthage and the Mediterranean, 264 to 133 BC | Carthage and Dido | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-4.1.html` |
| 21 | 4.2 | 4 · Carthage and the Mediterranean, 264 to 133 BC | The First Punic War | written · reviewed | Opus 5.5 | off | `kit/rome/r-4.2.html` |
| 22 | 4.3 | 4 · Carthage and the Mediterranean, 264 to 133 BC | Hannibal and the Second Punic War | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-4.3.html` |
| 23 | 4.4 | 4 · Carthage and the Mediterranean, 264 to 133 BC | East and West: Macedon, Spain and the year 146 | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-4.4.html` |
| 24 | 4.5 | 4 · Carthage and the Mediterranean, 264 to 133 BC | Polybius, Cato and the Greek invasion of Rome | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-4.5.html` |
| 25 | 5.1 | 5 · The fall of the Republic, 133 to 30 BC | The Gracchi | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-5.1.html` |
| 26 | 5.2 | 5 · The fall of the Republic, 133 to 30 BC | Marius and Sulla | written · reviewed | Opus 5.5 | off | `kit/rome/r-5.2.html` |
| 27 | 5.3 | 5 · The fall of the Republic, 133 to 30 BC | Pompey, Crassus, Cicero and Catiline | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-5.3.html` |
| 28 | 5.4 | 5 · The fall of the Republic, 133 to 30 BC | Caesar | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-5.4.html` |
| 29 | 5.5 | 5 · The fall of the Republic, 133 to 30 BC | Antony, Octavian and Cleopatra | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-5.5.html` |
| 30 | 5.6 | 5 · The fall of the Republic, 133 to 30 BC | Writing in a falling Republic | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-5.6.html` |
| 31 | 6.1 | 6 · Augustus, 31 BC to AD 14 | From Octavian to Augustus | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-6.1.html` |
| 32 | 6.2 | 6 · Augustus, 31 BC to AD 14 | The city of marble and the restored religion | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-6.2.html` |
| 33 | 6.3 | 6 · Augustus, 31 BC to AD 14 | Virgil, Horace, Livy and Ovid: the Augustan myth | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-6.3.html` |
| 34 | 6.4 | 6 · Augustus, 31 BC to AD 14 | Empire without end | written · reviewed | Opus 5.5 | off | `kit/rome/r-6.4.html` |
| 35 | 7.1 | 7 · The Principate, AD 14 to 235 | The Julio-Claudians | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-7.1.html` |
| 36 | 7.2 | 7 · The Principate, AD 14 to 235 | The year of four emperors and the Flavians | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-7.2.html` |
| 37 | 7.3 | 7 · The Principate, AD 14 to 235 | The adoptive emperors | written · reviewed | Opus 5.5 | off | `kit/rome/r-7.3.html` |
| 38 | 7.4 | 7 · The Principate, AD 14 to 235 | The Severans and the citizenship of 212 | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-7.4.html` |
| 39 | 7.5 | 7 · The Principate, AD 14 to 235 | How the empire worked | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-7.5.html` |
| 40 | 8.1 | 8 · Crisis and the late empire, AD 235 to 476 | The third-century crisis | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-8.1.html` |
| 41 | 8.2 | 8 · Crisis and the late empire, AD 235 to 476 | Diocletian and the Tetrarchy | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-8.2.html` |
| 42 | 8.3 | 8 · Crisis and the late empire, AD 235 to 476 | Constantine | written · reviewed | Opus 5.5 | off | `kit/rome/r-8.3.html` |
| 43 | 8.4 | 8 · Crisis and the late empire, AD 235 to 476 | Julian, Theodosius and the end of the old gods | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-8.4.html` |
| 44 | 8.5 | 8 · Crisis and the late empire, AD 235 to 476 | The fall of the West, 395 to 476 | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-8.5.html` |
| 45 | 8.6 | 8 · Crisis and the late empire, AD 235 to 476 | The Rome that did not fall | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-8.6.html` |
| 46 | 9.1 | 9 · Law, army and daily life | Roman law | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-9.1.html` |
| 47 | 9.2 | 9 · Law, army and daily life | The army | written · reviewed | Opus 5.5 | off | `kit/rome/r-9.2.html` |
| 48 | 9.3 | 9 · Law, army and daily life | Family, women and slaves | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-9.3.html` |
| 49 | 9.4 | 9 · Law, army and daily life | Bread, baths and games | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-9.4.html` |
| 50 | 9.5 | 9 · Law, army and daily life | Reading a site: Rome on foot | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-9.5.html` |
| 51 | 10.1 | 10 · Literature, myth-making and reception | Ovid and the Roman remaking of Greek myth | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-10.1.html` |
| 52 | 10.2 | 10 · Literature, myth-making and reception | Imperial literature, Seneca to Apuleius | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-10.2.html` |
| 53 | 10.3 | 10 · Literature, myth-making and reception | Reading Roman art and architecture | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-10.3.html` |
| 54 | 10.4 | 10 · Literature, myth-making and reception | Reception: how Rome reached you | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-10.4.html` |
| 55 | 10.5 | 10 · Literature, myth-making and reception | Capstone: the whole thing in one sitting | written · reviewed | Opus 5.5 | off | `kit/rome/r-10.5.html` |
| 56 | 11.1 | 11 · Deep dive I: the fall of the Republic | How the Republic worked at its height | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-11.1.html` |
| 57 | 11.2 | 11 · Deep dive I: the fall of the Republic | Generals and their armies | written · reviewed | Opus 5.5 | off | `kit/rome/r-11.2.html` |
| 58 | 13.1 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | Philosophy comes to Rome | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-13.1.html` |
| 59 | 13.2 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | Stoicism made Roman | written · reviewed (sampled) | Opus 5.5 | off | `kit/rome/r-13.2.html` |
| 60 | 11.3 | 11 · Deep dive I: the fall of the Republic | Politics in the street | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-11.3.html` (+ `courses/rome/11.3-politics-in-the-street.md`) |
| 61 | 11.4 | 11 · Deep dive I: the fall of the Republic | Women and the late Republic | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-11.4.html` (+ `courses/rome/11.4-women-and-the-late-republic.md`) |
| 62 | 11.5 | 11 · Deep dive I: the fall of the Republic | Cicero through his letters | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-11.5.html` (+ `courses/rome/11.5-cicero-through-his-letters.md`) |
| 63 | 11.6 | 11 · Deep dive I: the fall of the Republic | Caesar's Commentaries and Gaul | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-11.6.html` (+ `courses/rome/11.6-caesars-commentaries-and-gaul.md`) |
| ✓ | Review | Rome | Fable review of batch 1 (method.md §6) | after #63 | Fable 5.1 | off | `kit/audits/` |
| 64 | 11.7 | 11 · Deep dive I: the fall of the Republic | The Ides of March | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-11.7.html` (+ `courses/rome/11.7-the-ides-of-march.md`) |
| 65 | 11.8 | 11 · Deep dive I: the fall of the Republic | Why the Republic fell | not written · batch 2, last in unit 11 | Opus 5.5 | off | `courses/rome/11.8-why-the-republic-fell.md` (+ `kit/rome/r-11.8.html`) |
| 66 | 13.3 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | The rival schools at Rome | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-13.3.html` (+ `courses/rome/13.3-the-rival-schools-at-rome.md`) |
| 67 | 13.4 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | Cato and the Stoic opposition | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-13.4.html` (+ `courses/rome/13.4-cato-and-the-stoic-opposition.md`) |
| ✓ | Review | Rome | Fable review of batch 2 | after #67 | Fable 5.1 | off | `kit/audits/` |
| 68 | 13.5 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | Seneca | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-13.5.html` (+ `courses/rome/13.5-seneca.md`) |
| 69 | 13.6 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | Musonius Rufus and Epictetus | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-13.6.html` (+ `courses/rome/13.6-musonius-rufus-and-epictetus.md`) |
| 70 | 13.7 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | Marcus Aurelius: a life | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-13.7.html` (+ `courses/rome/13.7-marcus-aurelius-a-life.md`) |
| 71 | 13.8 | 13 · Deep dive III: Roman philosophy, the Stoics and Marcus Aurelius | The Meditations and the afterlife of Roman Stoicism | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-13.8.html` (+ `courses/rome/13.8-the-meditations-and-the-afterlife-of-roman-stoicism.md`) |
| ✓ | Review | Rome | Fable review of batch 3 | after #71 | Fable 5.1 | off | `kit/audits/` |
| 72 | 12.1 | 12 · Deep dive II: the Aeneid | Virgil and the making of the poem | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-12.1.html` (+ `courses/rome/12.1-virgil-and-the-making-of-the-poem.md`) |
| 73 | 12.2 | 12 · Deep dive II: the Aeneid | Books 1 to 6: the Odyssean Aeneid | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-12.2.html` (+ `courses/rome/12.2-books-1-to-6-the-odyssean-aeneid.md`) |
| 74 | 12.3 | 12 · Deep dive II: the Aeneid | Books 7 to 12: the Iliadic Aeneid | not written · batch 4 | Opus 5.5 | off | `courses/rome/12.3-books-7-to-12-the-iliadic-aeneid.md` (+ `kit/rome/r-12.3.html`) |
| 75 | 12.4 | 12 · Deep dive II: the Aeneid | Dido | not written · batch 4 | Opus 5.5 | off | `courses/rome/12.4-dido.md` (+ `kit/rome/r-12.4.html`) |
| ✓ | Review | Rome | Fable review of batch 4 | after #75 | Fable 5.1 | off | `kit/audits/` |
| 76 | 12.5 | 12 · Deep dive II: the Aeneid | Book 6: the underworld and the parade of heroes | not written · batch 5 | Opus 5.5 | off | `courses/rome/12.5-book-6-the-underworld-and-the-parade-of-heroes.md` (+ `kit/rome/r-12.5.html`) |
| 77 | 12.7 | 12 · Deep dive II: the Aeneid | Augustan or anti-Augustan? | not written · batch 5 | Opus 5.5 | off | `courses/rome/12.7-augustan-or-anti-augustan.md` (+ `kit/rome/r-12.7.html`) |
| 78 | 12.8 | 12 · Deep dive II: the Aeneid | The Aeneid after Rome | not written · batch 5 | Opus 5.5 | off | `courses/rome/12.8-the-aeneid-after-rome.md` (+ `kit/rome/r-12.8.html`) |
| 79 | 12.6 | 12 · Deep dive II: the Aeneid | The gods of the Aeneid | written 1 Nov 2026 · flagged for Fable review | Opus 5.5 | off | `kit/rome/r-12.6.html` (+ `courses/rome/12.6-the-gods-of-the-aeneid.md`) |
| ✓ | Review | Rome | Fable review of batch 5; then 14.2 to 14.5 rerun over the 20 new reports as the course audit | after #79 | Fable 5.1 | off | `kit/audits/` |
| ✓ | 14.1 | 14 · Quality audit | Calibrate the rubric for Rome | run 27 Oct 2026 (calibrated on 0.1 and 1.4) | Fable 5.1 | off | `kit/audits/` |
| ✓ | 14.2 | 14 · Quality audit | Audit one report | run on a sample of 12 and the capstone; reruns on the 20 new reports when Rome is complete | Fable 5.1 | off | `kit/audits/` |
| ✓ | 14.3 | 14 · Quality audit | Overlap check: deep dives and Greek cross-references | 16 pairs read, all pass; reruns on the 20 new reports when Rome is complete | Fable 5.1 | off | `kit/audits/` |
| ✓ | 14.4 | 14 · Quality audit | Compare against the Greek baseline | run; all strata cleared; reruns on the 20 new reports when Rome is complete | Fable 5.1 | off | `kit/audits/` |
| ✓ | 14.5 | 14 · Quality audit | Fix a report | run; every erratum applied; reruns on the 20 new reports when Rome is complete | Fable 5.1 | off | `kit/audits/` |
| ✓ | 14.6 | 14 · Quality audit | Review the syllabus itself | run 27 Oct 2026 | Fable 5.1 | off | `kit/audits/` |

## Courses to come (Personal Mythology)

Listed in `kit/courses.py` (`NEXT`) as coming soon, with a scope and reading spine each: Egypt, Persia, Norse, Celtic, English, Scottish, Chinese, Japanese. A new course is added with the `new-course` skill.

