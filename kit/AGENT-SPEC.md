# Report writing spec

You are writing one module of a self-study course in the Personal Mythology compendium: long-form reports on the history and mythology of one culture at a time, for an educated adult reader who wants genuine depth. Courses so far: Greece (course 1, complete: core and three deep dives) and Rome (course 2, in progress). Read the prompt you are given and answer it fully. Write from your own knowledge; use web search only to verify a specific date or a contested scholarly point if you are unsure. Do not pad.

## Output

Write ONE file: the path you are given, a Markdown file in the vault, `courses/<course>/<id>-<slug>.md` (P71-3, 1 November 2026: Greece and Rome are Markdown courses; `docs/p71-3.md`). It holds the report's text, its trees and its figure declarations, nothing else: no HTML (but `<sup>` and `<sub>`, which Markdown has no form for), no class, no style, no emoji, nothing about layout. The build adds the page (the section bands, the boxes, the answers' accordions, the Sources and the prompt) and the ebook. It opens with its front matter and title:

```
---
code: 4.2
title: <the module's title, as in the syllabus>
course: rome · Personal Mythology · Rome
model: <the model that wrote it>
written: <YYYY-MM-DD>
search: off
---

# <the module's title>
```

Then use only these forms (`kit/mdcourse.py`, `history_html`, reads each one):

- `## ` for the report's main sections (6–10 of them). No other `# ` line after the title.
- `### ` for sub-sections where needed.
- Paragraphs, `- ` and `1. ` lists, `**bold**`, `*italic*` (`_italic_` inside bold), and `> ` for short quoted ancient text (under 15 words), one quotation per `> ` paragraph.
- A pipe table (header row, `|---|` row, then the rows) for genuinely tabular material (chronologies, lists of names with attributes). A `|` inside a cell is written `\|`.
- A ```` ```tree ```` fenced block for a text family tree or mental map if the prompt asks for one; it is drawn exactly as typed.
- A ```` ```viz ```` fenced block for a figure where the content has a shape: the figure's JSON, `"kind"` first and `"caption"` last (kinds and fields in `kit/viz.py`, when to declare one in `WRITER-BRIEF.md`).
- The dispute box: a paragraph that opens with `**Where sources disagree.**` — a short block, used wherever ancient sources or modern scholars disagree. Use it several times across the report; it is required.
- Final two sections, in this order, with these exact headings:
  - `## Self-test`, then a numbered list of 10 items; each item is the question, then a blank line and the answer as an indented paragraph (four spaces) that opens with `Answer:`. The build puts the answer in its closed box.
  - `## Carry forward`, then a numbered list of exactly 3 items, the three ideas the reader must keep for later modules.

## Sources and bibliography (Pedro's rule, 27 October 2026)
Every report keeps its sources for future checks. The report itself cites inline, as below. Beside it the writer leaves `bibliography/<course>/r-<id>.md`: every ancient author and work cited, with the passages used and the edition or translation relied on where known; every modern work cited, with author, full title, place or journal and year of the edition named. `biblio.py` (run by `build.py`) also extracts a machine-made list per unit from the inline citations, `bibliography/<course>/unit-<n>.md`, as a check aid; where the curated file exists the unit file links to it. Reports written before this rule have the machine list only until a curated file is made for them.

## Content rules

- Length: the word count the prompt asks for is a guide, not a law (Pedro's rule, 27 October 2026). Give the topic the words it needs: some need 2,000, some 6,000. Plan the section budget before writing and write in one pass; do not pad to reach the target and do not cut substance to meet it. `check.py` reports the count against the target as a note only.
- Name specific primary sources by author and work (e.g. Hesiod, Theogony 453–506; Apollodorus, Library 1.1.5; Herodotus 7.204; Livy 1.7.3; Dionysius of Halicarnassus, Roman Antiquities 1.79; Plutarch, Romulus 9). Book, chapter and line numbers where you are confident; otherwise author and work only. Never invent a citation.
- Flag disagreements between ancient sources and between modern scholars honestly, with names on each side. Say "uncertain" when it is.
- Plain, direct prose. No preamble ("In this report I will…"), no summary of what you are about to say, no closing pleasantries. Begin directly with the first `## ` section after the title.
- British spelling.
- Every number (dead, troops, money, people, distances) says whose figure it is: an ancient author with a citation, or a named modern estimate.
- Every "X argued Y" about a modern scholar must be something you are sure X argued; otherwise state the view without a name, or search. Give a modern book the date and title of the edition you name (the original's title with its date, or the translation's with its own).
- Keep the reporter separate from the claim: cite an ancient author only for what that author says, not for what a later author says about him ("Aristotle says Thales held …", not "Thales held …, Metaphysics 983b").
- Dispute boxes name a source or scholar on each side. A Self-test answer must agree with the body.
- Before writing "module X covers Y", open that report and check that it does.

### Greek course
- Use Greek names in their standard English forms (Zeus, Heracles, Odysseus; not Roman names) unless the point is about Roman transmission.
- Refer to other Greek modules as "module 6.5" (deep dives too: "module 11.7") and to Rome modules as "Rome module 13.2". Where the prompt points back to a module, open that report, point back in those words and do not retell what it covers.
- Philosophy citation conventions (deep dive III):
  - Presocratics by Diels–Kranz number (DK 22 B 30); Plato by Stephanus page (*Republic* 514a); Aristotle by Bekker page (*Nicomachean Ethics* 1097b22).
  - Stoic fragments by *SVF* volume and number (*SVF* 3.178), and Long and Sedley by section and letter (LS 59D), only where used.
  - Diogenes Laertius by book and section (7.87); Sextus Empiricus, *Outlines of Pyrrhonism* by book and section (1.36); Plotinus by Ennead, treatise and chapter (*Enneads* 5.1.6).
  - Quote a fragment only from the edition you cite, and keep the doxographer separate from the philosopher: "Simplicius reports that Anaximander …" (DK 12 B 1), not a bare attribution.

### Rome course
- Use Latin names for Roman gods (Jupiter, Juno, Hercules, Castor) and give the Greek equivalent only where the identification is the point. Use the standard English forms of people and places (Livy, Pompey, Mark Antony, Octavian until 27 BC and Augustus after, Tarquinius Priscus, Veii).
- Keep the date of the event and the date of the source apart. For anything before about 300 BC, say who tells the story and how many centuries after the event they wrote.
- Where the prompt points back to a Greek module ("point back to Greek module 7.3"), refer to it in those words and do not retell what it covers. Refer to other Rome modules as "module 1.4" and to deep dives as "deep dive module 11.7".
- Citation conventions: Cicero's treatises by English title (*On the Republic*, *On the Laws*, *On Divination*, *On Duties*), his speeches by Latin title (*Pro Caelio*, *Pro Sestio*, *De lege agraria*, *De domo sua*, *De haruspicum responso*), his invectives in English (*Against Catiline*, *Against Piso*, *Verrines*, *Philippics*); Plutarch's lives of the Catos as *Cato Maior* and *Cato Minor*; Varro's and Cato's treatises as *On the Latin Language* and *On Agriculture*; Censorinus as *De die natali*; Eusebius' history as *Church History* (and his *Life of Constantine*). Dio by the Loeb book number (Boissevain's division, which the Loeb follows), with the traditional number the Loeb gives in its margin in brackets where they differ (73(72).14.3); check which numbering a book number belongs to before writing it.
- Philosophy citation conventions (deep dive III, and wherever these authors are cited):
  - Seneca's *Letters* by number and section (*Letters* 65.2), the dialogues by English title (*On Anger* 2.3, *On the Shortness of Life*, *On Providence*).
  - Epictetus, *Discourses* by book, chapter and section (1.1.7), and the *Handbook* by chapter; Marcus Aurelius, *Meditations* by book and section (2.1); Musonius Rufus by lecture number.
  - Cicero's philosophical works by English title (*On Ends*, *Tusculan Disputations*, *On the Nature of the Gods*, *On Fate*, *Academica*).
  - Greek philosophers by the Greek course's conventions (Diels–Kranz, Stephanus, Bekker, *SVF*, Diogenes Laertius by book and section).

## Provenance and the Fable review flag (for the maintainer, not the writer)
Every new report must be added to `provenance.json`, under its course, with the model that actually wrote it (`register.py` does this). Anything whose entry does not mention Fable 5.1 is flagged for review with Fable 5.1 (after review, record it as "Opus 5.5, reviewed with Fable 5.1"): the site marks it on the report and on the course home, and `build.py` lists it in `FABLE-REVIEW.md`. Greek reports are reviewed through Greek unit 13, Rome reports through Rome unit 14. Non-report material written with another model (a syllabus, course-home text, specs, code) goes under `artefacts` in `provenance.json` so it appears in the queue too. `review_due.py` (called by `register.py` and `build.py`) prints FABLE REVIEW DUE once four written units hold flagged reports; a writing session then stops at the unit boundary and tells Pedro.
