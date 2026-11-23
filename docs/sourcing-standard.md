# Sourcing standard

One checklist for the writer (before handing a unit in) and the auditor (when sampling it). Part 1 applies to every course. Parts 2 to 12 are each course family's own rules, taken from its brief preamble and its spec (Parts 8 to 10 and 12 from their courses' syllabuses, section 6; Part 11 from its course's shared preamble); a unit must also pass its own course's part. Every item is phrased so it can be answered yes or no about one claim or one unit.

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
- [ ] A figure adds no fact: every label, date and number in it appears in the unit's own sourced text, and its caption says what it shows and where its data comes from (section, author, line).
- [ ] An illustration adds no claim (P95): an object relief shows an object the text discusses at length, from a file in design/outlines/ whose licence allows reuse with credit (outlines.json: its source repository, path and commit, author and licence); its caption says what it shows, that it is a stylised outline, and gives the credit exactly as the licence asks; it is never offered as evidence of what the object looked like.

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
- [ ] Citation conventions for the course are followed (Greek: Diels–Kranz, Stephanus, Bekker, *SVF*, LS, Diogenes Laertius by book and section; Rome: Cicero's treatises by English title, speeches by Latin title, invectives in English; Dio by Loeb book with the Loeb's margin (traditional) number in brackets where they differ; Seneca's *Letters* by number and section; the full list is `AGENT-SPEC.md`).
- [ ] "Module X covers Y" is written only after opening module X and checking that it does.
- [ ] Every Self-test answer agrees with the body.
- [ ] The writer leaves `courses/<course>/bibliography/r-<id>.md`: every ancient author and work with passages and the edition or translation relied on where known; every modern work with author, full title, place or journal and year of the edition named.
- [ ] Web search is used to verify a specific date or contested point the writer is unsure of, not to write from (search flag off).

## Part 4 · User Experience (from the shared preamble of `courses/ux/briefs.md`)

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

## Part 5 · Building a Personal Brand on Instagram and YouTube (from the shared preamble of `courses/personal-brand/briefs.md`)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed work; platform-official documentation or statements; a large-sample vendor dataset, named, with sample size and date; a documented creator case with verifiable numbers.
- [ ] Creator anecdotes are labelled as anecdote; correlational and vendor data are labelled as such.
- [ ] A claim about growth, formats or metrics says which platform it holds for.
- [ ] Every claim carried over from a source unit of the private course was re-verified at its source by the writer; nothing rests on the source unit alone.
- [ ] Nothing about the private course's reader appears, and the unit never refers to the private course or its units (`python3 kit/private_terms.py` prints OK).
- [ ] Every fact about Mara Venn, the fictional running example, is labelled "(Mara, fictional)" on its first use in the unit, agrees with `courses/personal-brand/notes/case-facts.md`, and is never used as evidence for a claim about the world; every benchmark she is set against is sourced.
- [ ] No country's tax rate or threshold is stated as the reader's; an amount is in its source's currency with its date; a legal point is a question with the primary source to open for the EU, the UK and the US, and the unit says it is information, not legal or tax advice.
- [ ] No uncited figures; no invented handles, names, studies or numbers (Mara's labelled facts apart); a claim that cannot be sourced is said to be unsourced and is left out of the deliverable.
- [ ] Where the unit's search flag is on, every fact that can change (platform rules and thresholds, features, prices, published benchmarks) carries the date it was checked.
- [ ] The deliverable is built in full for Mara and then given as a template whose blanks say what goes in them.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, so the course bibliography can collect them.

## Part 6 · Building with AI (from the shared preamble of `courses/building-with-ai/briefs.md`)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed work; a preprint, labelled as one; vendor documentation or statements, labelled as vendor and dated; a named practitioner's own post, talk or repository, labelled as practice; an independent benchmark with its version and date.
- [ ] Each method or practice carries an evidence grade: measured, documented practice, or stated opinion.
- [ ] A study's finding names the models and the task it tested; a transfer to a current model or to the reader's work is said to be the unit's inference.
- [ ] Every product fact (a limit, a price, a feature, a model name) carries the date it was read on the vendor's own page.
- [ ] The body ends with a section "On other tools" that says which claims are specific to Claude and cites the other vendors' own documentation for each equivalent, or says none was found.
- [ ] Every claim carried over from a source unit of the private course was re-verified at its source by the writer; nothing rests on the source unit alone.
- [ ] Nothing about the private course's reader appears, and the unit never refers to the private course or its units (`python3 kit/private_terms.py` prints OK).
- [ ] Every fact about the Academy case is in `courses/building-with-ai/notes/case-academy.md`, is cited to its section, is labelled "(Academy case)" on first use and as an anecdote, and is never the only support for a general claim.
- [ ] No uncited figures; no invented names, studies, quotations or numbers; a claim that cannot be sourced is said to be unsourced and is left out of the deliverable.
- [ ] The deliverable is built in full on the case (or on a neutral example whose invented content is labelled) and then given as a template whose blanks say what goes in them.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, so the course bibliography can collect them.

## Part 7 · Sport Psychology for Coaches (from the shared preamble of `courses/sport-psychology/briefs.md`)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: a consensus or position statement of the IOC, ISSP, FEPSAC, AASP, AAP, ACSM or a national body of the same kind, labelled as consensus; a systematic review or meta-analysis; a peer-reviewed primary study; a standard textbook or handbook cited by edition and chapter; for safeguarding and rules, the issuing body's own page, dated.
- [ ] No video, podcast, social-media post, blog, coaching influencer, popular book or press report of a study is cited as a source; one may be named only as the claim under examination.
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read (abstract or full text) and the date; a claim that rests on an abstract alone says so.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
- [ ] Every technique and recommendation carries one of the five grades (strong, moderate, weak, contested, practice), and the grade follows SP1's key.
- [ ] A study's finding states its sample (children, adolescents, students, adult athletes, non-athletes) and its design; a correlation is called a correlation.
- [ ] A finding from adults, students or non-athletes applied to younger athletes is labelled as the unit's inference.
- [ ] An effect size is given in the source's own terms, with the sample it comes from, or not given.
- [ ] A popular claim on the course's list is named as a claim and set against its evidence, or against "no peer-reviewed source found".
- [ ] The unit stays inside the coach's part: nothing teaches assessment, diagnosis or treatment, and each topic of mental health, eating, injury or abuse says where the coach's part ends and who takes over.
- [ ] No weight-loss method, calorie figure or target weight appears; nothing describes a method of self-harm.
- [ ] No law is stated as the reader's; a legal or reporting duty is a question with the body to consult; the unit says it is information, not legal, medical or psychological advice.
- [ ] No real athlete, coach or club is named as an example of abuse, illness or failure unless a cited court, public inquiry or peer-reviewed source names them.
- [ ] Examples come from at least three kinds of sport, and no single sport supplies more than a third of them.
- [ ] Every fact about Dani, Milan and Sara is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his sport, his club or his athletes appears (`python3 kit/private_terms.py` prints OK).
- [ ] Where the search flag is on (SP9, DD-SP1, DD-SP2), every code, rule, tool, service or reporting route carries the date it was read on the issuing body's own page.
- [ ] The deliverable is built in full on the case athletes the brief names and then given as a template whose blanks say what goes in them.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper, so the course bibliography can collect them.

## Part 8 · Supply Chain Execution for Product Teams (from section 6 of `docs/supply-chain-execution-syllabus.md`)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed research; a standard textbook cited by edition and chapter; an industry association's report or survey with its sample and year; an analyst report by firm, title and date; an audited company filing; a standards body's own page; a vendor's own page, release or documentation, dated.
- [ ] No video, podcast, social-media post, unsigned blog, comparison or lead-generation site, or press rewrite of a release is cited as a source; one may be named only as the claim under examination.
- [ ] Every claim carries one of the four grades (independent, analyst, vendor-reported, practice), and the grade follows SCE1's key.
- [ ] An analyst report says how it was read: in full, in a public reprint, or in abstract. A claim that rests on an abstract alone says so.
- [ ] No real vendor is assessed, ranked, compared or recommended, and no real vendor's product line is mapped.
- [ ] A real vendor is named only to attribute a dated public statement to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every vendor on the list given alike.
- [ ] Worked product examples use only the fictional vendors of `case-facts.md`, labelled "(fictional)"; no fictional vendor is said or hinted to stand for a real one.
- [ ] A peer-review site is cited by market for what its reviewers say, with the number of reviews, never to assess a named vendor.
- [ ] A number says whose figure it is, the sample and the year. No price, revenue or win rate of a private company appears unless that company published it.
- [ ] A study's finding states its sample, setting and design; a finding from one site or industry applied to another is labelled as the unit's inference.
- [ ] A common claim on the course's list is named as a claim and set against its evidence, or against "no independent source found".
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read and the date.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
- [ ] Every fact about Corvane, Ostrel Foods, Tandric Logistics, Halvern Systems, Varnby Software and Kestrow is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his employer, his role or his work appears (`python3 kit/private_terms.py` prints OK).
- [ ] Nothing treats AI features; no unit is framed as interview preparation; no craft method is taught.
- [ ] Where the search flag is on, every analyst list, market figure and filing figure carries the date it was read.
- [ ] The deliverable is built in full on the case the brief names and then given as a template whose blanks say what goes in them.
- [ ] "On a site visit" and "Self-check" are present, and every Self-check answer agrees with the body.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper.

## Part 9 · Supply Chain Planning for Product Teams (from section 6 of `docs/supply-chain-planning-syllabus.md`)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed research; the published results of a forecasting competition; a standard textbook cited by edition and chapter; an industry association's report or survey with its sample and year; an analyst report by firm, title and date; an audited company filing; a standards body's own page; a vendor's own page, release or documentation, dated.
- [ ] No video, podcast, social-media post, unsigned blog, comparison or lead-generation site, or press rewrite of a release is cited as a source; one may be named only as the claim under examination.
- [ ] Every claim carries one of the four grades (independent, analyst, vendor-reported, practice), and the grade follows SCP1's key.
- [ ] A finding states what kind of evidence it is (forecasting competition, field experiment, laboratory experiment, simulation, single-company case study, survey), with its data, setting and year; a simulation is not presented as a field result; a correlation is called a correlation.
- [ ] A finding from one industry, company or dataset applied to another is labelled as the unit's inference.
- [ ] No formula and no worked calculation appears; a method is described by what goes in, what comes out, what it assumes and when it fails. A number is a sourced finding in its source's own terms, or a case fact marked fictional.
- [ ] Statistical, machine-learning and optimisation methods are treated on published evidence. Nothing treats generative AI, language-model assistants or agents; a vendor's word "AI" is reported as the vendor's word.
- [ ] An analyst report says how it was read: in full, in a public reprint, or in abstract. A claim that rests on an abstract alone says so.
- [ ] No real vendor is assessed, ranked, compared or recommended, and no real vendor's product line is mapped.
- [ ] A real vendor is named only to attribute a dated public statement to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every vendor on the list given alike.
- [ ] Worked product examples use only the fictional vendors of `case-facts.md`, labelled "(fictional)"; no fictional vendor is said or hinted to stand for a real one.
- [ ] A real company's planning practice is described only from a peer-reviewed paper, a published case with named authors or its own audited filing; an account co-written by the company's staff or its software supplier is labelled an interested party's account.
- [ ] A book or article by someone who sells the method it describes is labelled an interested party's account.
- [ ] A peer-review site is cited by market for what its reviewers say, with where any count was read, never to assess a named vendor.
- [ ] A number says whose figure it is, the sample and the year. No price, revenue or win rate of a private company appears unless that company published it. No return, saving or payback is promised to the reader.
- [ ] A common claim on the course's list is named as a claim and set against its evidence, or against "no independent source found".
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read (abstract, reprint or full text) and the date; the edition or release cited is the one opened.
- [ ] The source log gives every reference's kind of venue (peer-reviewed journal, academic or professional publisher's book, forecasting competition, association, analyst firm, audited filing, standards body, vendor) and any commercial interest its authors have in what they describe.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal or publisher, year, volume, pages, DOI.
- [ ] Every fact about Corvane, Ostrel Foods, Pellward, Lathmoor, Ebbfield and Varnby Software is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his employer, his role or his work appears (`python3 kit/private_terms.py` prints OK).
- [ ] No unit is framed as interview preparation; no craft method is taught.
- [ ] Where the search flag is on, every analyst list, market figure, filing figure and vendor page carries the date it was read.
- [ ] The deliverable is built in full on the case the brief names and then given as a template whose blanks say what goes in them.
- [ ] "In the planning meeting" and "Self-check" are present, and every Self-check answer agrees with the body.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper.

## Part 10 · AI in Supply Chain Execution (from section 6 of `docs/ai-in-supply-chain-execution-syllabus.md`)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed research, including peer-reviewed proceedings named as such; a preprint, labelled; a standard textbook cited by edition and chapter; a standards body's own page; the text of a law or regulation at its issuing body's page, or a regulator's own release or order; an industry association's report or survey with its sample and year; a research report of a university centre or an independent research organisation, labelled as a report, with its method; an analyst report or release by firm, title and date; an audited company filing; a vendor's, a model provider's or a consultancy's own page, documentation or survey, dated.
- [ ] No video, podcast, social-media post, unsigned blog, comparison or lead-generation site, law-firm or consultancy summary of a law, or press report of a study or a release is cited as a source; one may be named only as the claim under examination.
- [ ] Every claim carries one of the four grades (independent, analyst, vendor-reported, practice), and the grade follows AIE1's key. A consultancy's survey is vendor-reported. An analyst's prediction is called a prediction.
- [ ] Every claim about performance carries one setting tag (field trial, field observation, simulation, benchmark, demonstration, none), and the tag follows AIE1's key. No simulated or benchmarked result is written as if it had been measured in an operation.
- [ ] A preprint is called a preprint and is never the only support for a recommendation.
- [ ] A study's finding states its setting, sample, design, what was compared with what, the period and who measured; the effect is in the source's own terms; a correlation is called a correlation.
- [ ] A finding from another kind of work (a call centre, a consultancy, a hospital, a cockpit) applied to execution work is labelled as the unit's inference.
- [ ] A result obtained with a named model or version says which; its transfer to a current model is labelled as the unit's inference.
- [ ] Every feature discussed is placed in one family and on one rung by AIE1's keys, or the unit says why it sits across two.
- [ ] An analyst report says how it was read: in full, in a public reprint, or in abstract. A claim that rests on an abstract alone says so.
- [ ] No real vendor or model provider is assessed, ranked, compared or recommended, and no real vendor's product line or AI feature is mapped.
- [ ] A real vendor or model provider is named only to attribute a dated public statement or its own documentation to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every entry given alike. A company named by a peer-reviewed study as its setting is named as that setting only.
- [ ] Worked examples use only the fictional vendors, features and claims of `case-facts.md`, labelled "(fictional)"; none is said or hinted to stand for a real one; no fictional claim is repeated as a finding.
- [ ] A number says whose figure it is, the sample and the year. No price, revenue or win rate of a private company appears unless that company published it.
- [ ] A common claim on the course's list is named as a claim and set against its evidence, or against "no independent source found"; a circulating statistic is traced to the work that first reported it.
- [ ] A legal point names its jurisdiction, cites the text or the authority's own page with the date it was read, and is put as a question with the body to consult; the unit says it is information, not legal advice.
- [ ] A claim about jobs, pace, injury or surveillance rests on peer-reviewed work, a regulator or a named report with its method. Nothing teaches covert monitoring of an identified worker or the avoidance of a duty to inform or consult.
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read and the date.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
- [ ] Every fact about Corvane, Ostrel Foods, Tandric Logistics, Halvern Systems, Varnby Software and Kestrow is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his employer, its products, his role or his work appears (`python3 kit/private_terms.py` prints OK).
- [ ] No unit points to a unit of another course by code; no unit is framed as interview preparation; no model-building, prompt-writing, design or sales method is taught; no mathematics beyond arithmetic and no code.
- [ ] Where the search flag is on, every law, date, standard, analyst list, survey figure and product fact carries the date it was read.
- [ ] The deliverable is built in full on the case the brief names and then given as a template whose blanks say what goes in them.
- [ ] "In a demo or a pilot review" and "Self-check" are present, and every Self-check answer agrees with the body.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper.

## Part 11 · Managing an Athlete's Career (from the shared preamble of `courses/athlete-career/briefs.md`)

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: peer-reviewed research or a systematic review; a position or consensus statement of the ISSP, the IOC or a body of the same kind, labelled as consensus; a standard textbook cited by edition and chapter; a rule-maker's own text on its own page, dated; legislation or official guidance at its issuing body's page, dated; a court's judgment or press release at the court's own page; a public authority's own statement of what a law it administers requires, for that statement, dated; a funding body's or event organiser's own published figures; a survey with its sample and year; an agency's, sponsor's, platform's, vendor's or advocacy group's own page or report, labelled interested party and dated, as evidence of what that party says, offers or requires and never of how things are; an athlete's own published statement about their own case, labelled anecdote.
- [ ] No law firm's note or press report is the source for what a law, a rule or a judgment says; the text itself is read and cited.
- [ ] No video, podcast, social-media post, unsigned blog, recruiting-service or lead-generation site, or press rewrite of a release is cited as a source; one may be named only as the claim under examination.
- [ ] Every claim carries one of the five grades (research, rule, data, interested party, practice), and the grade follows AC1's key.
- [ ] A study's finding states its sample, setting and design; a correlation is called a correlation; a finding from famous athletes, large sponsorships or consumers applied to an unknown athlete is labelled as the unit's inference.
- [ ] No rule or law is stated as the reader's: each is given as its issuing body's text, with the sport and country it belongs to and the date read, followed by the question for the reader's own federation, event or authority.
- [ ] The unit says once that it is information and not legal, tax, financial or medical advice; nothing advises on investing money.
- [ ] No fee, rate, commission or "typical deal" is stated unless a named source published it, with whose figure it is, the sample, the year and the currency; where none exists the unit says so.
- [ ] Where the brief asks for it, the section "In Portugal" is present, every text in it was read at its issuing body's page and dated, it is labelled one country's worked example, and a Portuguese text is cited in Portuguese with its article number and rendered in English as the unit's translation.
- [ ] Nothing proposes for a minor a sponsor in alcohol, gambling, supplements or weight management, a sexualised presentation, or the publication of where the child lives, studies or trains; from AC5 on, "If the athlete is under 18" is present and agrees with AC4.
- [ ] No supplement is recommended; a supplement sponsor is treated as an anti-doping risk.
- [ ] No real athlete, coach or family is named as an example of hardship, exploitation, bankruptcy or failure unless they said it themselves in a cited source or a court or public inquiry names them, and then only as that source states it.
- [ ] No real agent, agency or sponsor is assessed, ranked or recommended; a real company is named only to attribute a dated public statement or rule to it.
- [ ] Nothing teaches how to get around an eligibility or advertising rule.
- [ ] The conflict between the reader's roles (coach, sponsor, representative) is named wherever the coach or the coach's business has a stake in the decision the unit describes.
- [ ] Examples come from at least three kinds of sport, and no single sport supplies more than a third of them.
- [ ] Every fact about Sara, Dani, Milan, their coaches and families, and the fictional sponsors, clubs and agents is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his sport, his club or his athletes appears (`python3 kit/private_terms.py` prints OK).
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read (abstract, summary or full text) and the date; a claim that rests on an abstract alone says so.
- [ ] Every Sources entry matches its publisher's, Crossref's or its issuing body's record: authors, title, journal or publisher, year, volume, pages, DOI; for a law, its number, date and official-journal reference.
- [ ] Where the search flag is on, every rule, law, programme, amount, schedule and ruling carries the date it was read on the issuing body's own page.
- [ ] The deliverable is built in full on the case the brief names and then given as a template whose blanks say what goes in them.
- [ ] "Check before you act" and "Self-check" are present, and every Self-check answer agrees with the body.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper.

## Part 12 · Egyptian history and mythology (from section 6 of `docs/egypt-syllabus.md`)

- [ ] Every claim that carries a date, a number, a name, an attribution or an interpretation is sourced where it is made.
- [ ] Each source is one of: an Egyptian text in a named, opened edition or translation; an object or monument by museum and accession number, excavation number or standard designation; a classical author by book and chapter; a peer-reviewed journal article; a monograph or edited volume from an academic press; the UCLA Encyclopedia of Egyptology; an excavation report or the page of the mission or institute that dug; a museum's own collection record; a peer-reviewed scientific study.
- [ ] No video, documentary, podcast, social-media post, unsigned web page, general encyclopaedia or wiki, travel or tour site, press report, popular book by a non-specialist, or translation by E. A. Wallis Budge is cited as a source; one may be named only as the claim under examination.
- [ ] Every reference in Sources is in the module's source log with the address opened, what was read (full text, chapter, abstract or catalogue record) and the date; a claim that rests on an abstract or a record alone says so.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors or editors, title, journal or press, year, volume, pages, DOI or ISBN.
- [ ] Every claim carries one of the seven grades (attested, later tradition, consensus, contested, scientific, announced, conjecture), and the grade follows EG1's key.
- [ ] An Egyptian text is cited by its standard designation and by the translation opened; the translator is named; a quotation is under 15 words and was read in that translation.
- [ ] A later source is never cited as if contemporary: the module states the gap in centuries between the source and what it describes (Manetho, Herodotus, Diodorus, Plutarch, a Ptolemaic temple text, a Ramesside king list).
- [ ] Every date before 664 BC is approximate and names the chronology it follows (EG3's convention); a disputed date gives the range.
- [ ] Every number (years of reign, troops, blocks, workers, dimensions, counts of texts or objects) names whose figure it is.
- [ ] A modern scholar is named for a view only from that scholar's own opened text, or from an opened peer-reviewed review or encyclopaedia article that reports it, named as the reporter.
- [ ] Every disagreement between sources or between scholars is in a dispute box with a named source or scholar on each side.
- [ ] A scientific result states its sample, its method and its published criticism, if any; a result on one body or one site is not generalised.
- [ ] A discovery known only from an announcement is graded announced, dated, and never built upon.
- [ ] A popular claim is named as a claim, stated as it circulates, set against its evidence or against "no peer-reviewed source found", and not mocked.
- [ ] Topics that touch living faiths or identities (EG23, EG28, EG56, DD-EG10, DD-EG21) report evidence and named positions and argue for no confession or camp.
- [ ] A hieroglyphic sign is given by Gardiner number and described in words; a Unicode sign is added only if the build renders it (flag F1).
- [ ] "Module X covers Y", "Greek module X" and "Rome module X" are written only after opening that module.
- [ ] Where the search flag is on, every current fact carries the date it was read.
- [ ] Every Self-test answer agrees with the body; the deliverable adds no unsourced claim.
- [ ] Links are given as links, the DOI address for a paper.
