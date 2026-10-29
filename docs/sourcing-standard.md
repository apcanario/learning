# Sourcing standard

One checklist for the writer (before handing a unit in) and the auditor (when sampling it). Part 1 applies to every course. Parts 2 to 4 are each course family's own rules, taken from its brief preamble and its spec; a unit must also pass its own course's part. Every item is phrased so it can be answered yes or no about one claim or one unit.

A **checkable claim** is any sentence that carries a number, a date, a named source, an attribution ("X argued Y", "the source says"), a mechanism or a recommendation. The auditor's sample is drawn from these (method.md §6).

## Part 1 · Every course

**Per claim**
- [ ] The claim is sourced where it is made, not only in a list at the end.
- [ ] The source can be opened by the reader: author or organisation, work or page title, the locator (book, chapter and line; page; or URL) and the date of the edition or the data.
- [ ] The source says what the claim says, not a stretch of it.
- [ ] The source is cited for what it says itself, not for what a later source reports about it (keep the reporter separate from the claim).
- [ ] A number says whose figure it is.
- [ ] A view is attached to a named person only when that person is known to have argued it; otherwise it is stated without a name.
- [ ] Words in quotation marks are the source's exact words.
- [ ] Nothing is invented: no citation, name, handle, number or quotation that the writer cannot point to.

**Per unit**
- [ ] A claim that cannot be sourced is said to be unsourced or uncertain, or is left out.
- [ ] If the unit's search flag is on, every fact that can change (rules, prices, limits, lineups, benchmarks, regulatory status) carries the date it was checked.
- [ ] The unit leaves its sources: every source it cites is listed with a full reference, and nothing is listed that it does not cite.
- [ ] The closing material (deliverable, self-test, carry-forward) agrees with the body and adds no unsourced claim.

**Auditor's verdict per sampled claim:** PASS (the source holds it), FAIL (wrong, unsupported, miscited or invented), STALE (true when written, superseded now; give the newer figure and its source). A citation the auditor cannot open is "unverifiable", not FAIL, and is reported as such.

## Part 2 · Brand + AI (from the shared preamble)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced.
- [ ] Each source is one of: peer-reviewed work; platform-official documentation or statements; a large-sample vendor dataset, named, with sample size and date; a documented creator case with verifiable numbers.
- [ ] Creator anecdotes are labelled as anecdote.
- [ ] Correlational and vendor data are labelled as such.
- [ ] No uncited figures; no invented handles, names or numbers.
- [ ] A claim that cannot be sourced is said to be unsourced and is left out of the deliverable.
- [ ] Where the unit depends on current facts (prices, platform rules, model lineups), the writer searched before writing and dated the facts.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, so the hub's bibliography can collect them.

## Part 3 · Personal Mythology (from `AGENT-SPEC.md` and `WRITER-BRIEF.md`)

- [ ] Primary sources are named by author and work, with book, chapter and line where the writer is confident, author and work only where not (Hesiod, *Theogony* 453–506; Livy 1.7.3; Plutarch, *Romulus* 9).
- [ ] Every number of dead, troops, money, people or distance names an ancient author with a citation or a named modern estimate.
- [ ] A modern book carries the title and date of the edition named (the original's title with its date, or the translation's with its own); no modern work is cited by surname and year alone.
- [ ] "X argued Y" about a modern scholar is something X argued; otherwise the view is stated without a name, or checked by search.
- [ ] An ancient author is cited only for what that author says ("Aristotle says Thales held …", not "Thales held …, *Metaphysics* 983b"); fragments are quoted only from the edition cited, and the doxographer is kept separate from the philosopher.
- [ ] Every disagreement between ancient sources or between modern scholars is in a dispute box that names a source or scholar on each side; "uncertain" is said when it is.
- [ ] Rome: the date of the event and the date of the source are kept apart; for anything before about 300 BC the unit says who tells the story and how many centuries later.
- [ ] Citation conventions for the course are followed (Greek: Diels–Kranz, Stephanus, Bekker, *SVF*, LS, Diogenes Laertius by book and section; Rome: Cicero's treatises by English title, speeches by Latin title, invectives in English; Dio by Loeb book with Boissevain's in brackets where they differ; Seneca's *Letters* by number and section; the full list is `AGENT-SPEC.md`).
- [ ] "Module X covers Y" is written only after opening module X and checking that it does.
- [ ] Every Self-test answer agrees with the body.
- [ ] The writer leaves `bibliography/<course>/r-<id>.md`: every ancient author and work with passages and the edition or translation relied on where known; every modern work with author, full title, place or journal and year of the edition named.
- [ ] Web search is used to verify a specific date or contested point the writer is unsure of, not to write from (search flag off).

## Part 4 · User Experience (from the shared preamble of `generator/data/ux/units_data.py`)

- [ ] Every claim that carries a number, a named source, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: a standard work of the field cited by author, title, edition and year with the page or chapter the claim is drawn from; a Nielsen Norman Group article or report with author, title, date and URL; peer-reviewed HCI or information-science research with venue and year; platform, standards or vendor documentation labelled as such; a practitioner's article or talk with a named author and date, labelled as practice.
- [ ] Vendor guidance (a research tool's advice on sample sizes, a platform's own claims) is labelled as vendor guidance, never cited as a study.
- [ ] Practice is labelled as practice; measured findings are kept separate from craft advice.
- [ ] A diagram redrawn or adapted from a source credits that source in its caption.
- [ ] Nothing is asserted about a real company's information architecture beyond what is visible on its public screens (dated) or documented by the company itself (cited).
- [ ] Every fact about Perqo, the fictional running example, is labelled "(Perqo, fictional)" on its first use in the unit, agrees with the Perqo facts in the filed units, and is never used as evidence for a claim about the world.
- [ ] Every figure is a fenced `viz` block of a kind `kit/viz.py` draws; its labels and numbers appear in the unit's own sourced text; no screenshot, embedded image or hand-written SVG.
- [ ] No uncited figures; no invented articles, authors, studies, URLs, names or numbers; a claim that cannot be sourced is said to be unsourced and is left out of the deliverable.
- [ ] Where the unit's search flag is on (DD-IA1, DD-IA2), every observation of a live product and every published figure carries the date it was checked.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, so the course bibliography can collect them.
