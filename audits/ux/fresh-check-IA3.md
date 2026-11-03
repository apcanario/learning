---
audit: fresh check
unit: IA3 · How people find and understand things
course: ux · IA · Information Architecture
model: Fable 5.1 (claude-fable-5-1, confirmed from the agent's transcript; live search; no Fable 5.1 fresh check is owed for IA3)
date: 2026-11-03
chat: own Fable 5.1 agent context, not shown the writing (P31), launched by the N8 chat (Opus 5.5) in session https://claude.ai/code/session_01KMmgQzRSLQ49HM5ox3pTj2
verdict: keep · 0 errors, 2 should-fix, 6 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). It differs from the report file the checker wrote in its own folder in two places only: the hand-back's Method paragraph adds the sentence naming that file's path, and the file ends with a newline. The maintainer's note follows the report.

# Fresh check · IA3 · How people find and understand things

**Copy check.** `diff unit/IA3-how-people-find-and-understand-things.md unit/IA3-how-people-find-and-understand-things.md.reference` printed nothing (exit 0). `sha256sum` printed `4ab614a7940e22c97f05be613de4c0c9ff14d2e705f302d9725455b16f219436`, the expected hash.

**Model.** This check ran as Fable 5.1 (claude-fable-5-1). No Fable 5.1 fresh check is owed for IA3.

**Method.** Read sourcing-standard.md Parts 1 and 4, brief-IA3.txt, the IA3 and AIMS entries in generator/data/ux/units_data.py, perqo-facts.md, IA1 and IA2 from the vault, and the unit. No audit report read. Every source below was opened by WebSearch and then WebFetch of a URL the search returned verbatim; the unit's own links were fetched only when a search returned them. No memory, Project, connector or publishing tool used. All five figures rendered with render.py (5 figures, 0 failed; SVGs in work/rendered/). Report file: /tmp/claude-0/-home-claude/c2d35acf-33fd-5825-ab1b-cb2e920d03af/scratchpad/n8/checker/report/fresh-check-IA3.md

## Findings

- [should-fix] [figure] Deliverable, as-is sitemap; Current: `"note": "→ see H-2.2.1; fails A1, A2, A3, A5"`; Problem: the caption says tone 6 marks "each element that fails an item of the checklist (item IDs in the notes)", but no note carries F1, which the applied table fails on four elements ("On Home, three of five elements are ambiguous ("Learn more", "Discover", "+"); in Benefits, the fifth item is of another kind"); Fix: `"note": "→ see H-2.2.1; fails A1, A2, A3, A5, F1"`, and likewise `"note": "offers; fails A1, D1, D2"` → `"note": "offers; a second Learn more under it; fails A1, A5, D1, D2, F1"` (the second "Learn more" under the Discover banner, which the text and the A5 row name, is otherwise absent from the figure), `"note": "→ see New claim; fails A4"` → `"note": "→ see New claim; fails A4, F1"`, `"note": "offers again; fails C1, C4, D1, D2"` → `"note": "offers again; fails C1, C4, D1, D2, F1"`; Basis: the unit's own as-is list ("with a second "Learn more" under the banner"), applied table rows A5 and F1, and the figure's caption.
- [should-fix] [deliverable] Deliverable, applied table, row A2; Current: `every other label passes (Home, Benefits, Claims, Card, Account, the four categories, New claim, Check and submit, Purchases, Freeze card, Profile, Notifications, Help)`; Problem: "every other label" is then listed, and the list omits Card details and Help with claims (which "What IA6 keeps" counts as passing), Balance and Recent activity, and says nothing of Discover, Perks and Documents, so a reader cannot tell whether those were judged under A2; Fix: `every other label passes (Home, Benefits, Claims, Card, Account, the four categories, New claim, Check and submit, Help with claims, Card details, Purchases, Freeze card, Profile, Notifications, Help, Balance, Recent activity; Discover, Perks and Documents are one word each and fail A1, not A2)`; Basis: the unit's own as-is list and "What IA6 keeps".
- [minor] [label] 1.2, second bullet; Current: `NN/g guidance, drawn from its usability studies.`; Problem: McCloskey's article ties only the first-words point to NN/g eyetracking research; "describes the page", "assume that it goes to the same place" and the "Click here" advice are stated as guidance without a cited study; Fix: `NN/g guidance; the first-words point rests on its eyetracking research, the rest is stated as guidance.`; Basis: McCloskey, "Writing Hyperlinks", NN/g, 9 March 2014, https://www.nngroup.com/articles/writing-links/
- [minor] [attribution] 2.2; Current: `Young described the diagram in her own words as one that`; Problem: the comment on Baum's interview is posted under "Anonymous" and self-identifies as Indi Young ("I'm Indi, the author of the book"); the page does not verify it; Fix: `A comment on the interview, posted anonymously and signed as the book's author, describes the diagram as one that`; Basis: Baum, "What Is Your Mental Model?", Boxes and Arrows, 14 February 2008, comment 3 of 15 February 2008, https://boxesandarrows.com/what-is-your-mental-model/
- [minor] [accuracy] 3.1; Current: `and the most codable and most used in language`; Problem: the abstract says basic objects are "the categories most codable, most coded, and most necessary in language"; "most used" is not its wording; Fix: `and the most codable, most coded and most necessary in language`; Basis: Rosch and others 1976, abstract, https://www.cns.nyu.edu/~msl/courses/2223/Readings/Rosch-CogPsych1976.pdf
- [minor] [attribution] 5.1 and Sources; Current: `("Search and You May Find", Nielsen Norman Group, 14 July 1997, [nngroup.com/alertbox/9707b.html](https://www.nngroup.com/alertbox/9707b.html))`; Problem: the article's canonical URL is nngroup.com/articles/search-and-you-may-find/; the alertbox URL was not returned by any search and could not be checked (it may redirect); Fix: `("Search and You May Find", Nielsen Norman Group, 14 July 1997, [nngroup.com/articles/search-and-you-may-find](https://www.nngroup.com/articles/search-and-you-may-find/))`, and in Sources `Nielsen Norman Group, 14 July 1997. [nngroup.com/alertbox/9707b.html](https://www.nngroup.com/alertbox/9707b.html)` → `Nielsen Norman Group, 14 July 1997. [nngroup.com/articles/search-and-you-may-find](https://www.nngroup.com/articles/search-and-you-may-find/)`; Basis: https://www.nngroup.com/articles/search-and-you-may-find/ (all three quoted figures confirmed there).
- [minor] [label] 6.2, last sentence; Current: `a backoffice such as Perqo Admin, used daily by the same HR and finance managers`; Problem: "used daily" and "opened a few times a month" are new Perqo facts (frequency of use; the register lists volumes as not yet set) and carry no "(Perqo, fictional)" label or "assumed" marker; Fix: `a backoffice such as Perqo Admin, used daily by the same HR and finance managers (Perqo, fictional; the frequencies are assumed)`; Basis: sourcing-standard.md Part 4, Perqo rule; perqo-facts.md "Not yet set".
- [minor] [coverage] 2.3; Current: `an approved claim stays in the Submitted group until it is paid, and a rejected claim leaves the list`; Problem: IA2, section 5.3, gives Submitted, Approved and Paid tone 5 "because a claim's status is shown on both Admin and the app"; the as-is invented here hides Approved in the Submitted group and does not say it departs from that assumption; Fix: `an approved claim stays in the Submitted group until it is paid (IA2's state diagram assumed the app shows Approved; the as-is here does not, and B2's fix restores it), and a rejected claim leaves the list`; Basis: IA2, section 5.3, state-diagram paragraph.

Note, not a finding: the unit is 8,481 words outside its figures, sources and unsure list (10,843 in all; the deliverable alone 2,207), above the brief's 2,000–6,000 range. It does not read as padded, and IA2 (9,339) was filed at the same length; recorded for the course's own judgement.

## Confirmed

- Pirolli and Card, "Information Foraging", Psychological Review 106(4), 1999, 643–675, DOI 10.1037/0033-295X.106.4.643; abstract: adaptation to gain valuable information at lower cost; patch, scent and diet models; ACT-IF. PASS. https://demo.kerko.whiskyechobravo.com/bibliography/FSB6DCE8
- Card and others, CHI 2001: title, seven authors, Xerox PARC; "Information scent is the (imperfect) perception of the value, cost, or access path of information sources"; "link descriptors, images, contextual clues"; backtracking as scent declines; switch to another site or search engine when scent becomes low; "So long as the potential rewards are above some threshold"; protocol analysis with think-aloud remarks. PASS. https://research.cs.vt.edu/ns/cs5724papers/5.usageenvir.adaptation.card.infoscent.pdf
- Nielsen, "Information Foraging: Why Google Makes People Leave Your Site Faster", 29 June 2003: "a given hunt's likely success from the spoor"; "the scent must keep getting stronger and stronger, or people give up"; "each site is a patch"; better search engines, less time per site; attribution to PARC, "previously Xerox PARC", Card and Pirolli. PASS. https://www.nngroup.com/articles/information-foraging-leave-site/
- Budiu, "Information Scent: How Users Decide Where to Go Next", 2 February 2020: all four quotations exact; scent wasted on a landing page that does not confirm. PASS. https://nngroup.com/articles/information-scent/
- Nielsen, "First 2 Words", 6 April 2009: 80 participants, 20 links from 20 sites, first 11 characters, 35% "hadn't the faintest idea", "Gift Cards" 85%, "Introducing" "had no meaning" and no reasonable prediction, three shared faults, framed around scanning lists. PASS. https://nngroup.com/articles/first-2-words-a-signal-for-scanning
- McCloskey, "Writing Hyperlinks", 9 March 2014: all four quotations exact. PASS (see minor on the label). https://www.nngroup.com/articles/writing-links/
- Laubheimer, "3 Common IA Mistakes", 16 April 2023: vague calls to action ("Explore", "Connect"), forced parallel wording, "I want to…"; "won't click on a category unless it's clear where they will go, before they click"; "Partner" example (Macquarie University) is a label over mixed content. PASS. https://www.nngroup.com/articles/3-ia-mistakes/
- Harley, "Icon Usability", 27 July 2014: both quotations exact. PASS. https://www.nngroup.com/articles/icon-usability/
- WCAG SC 2.4.4, Level A, text exact at the WCAG 2.1 Understanding page the unit links. PASS. https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context
- WCAG SC 3.2.4, Level AA, "Components that have the same functionality within a set of Web pages are identified consistently". PASS. https://www.w3.org/WAI/WCAG20/Understanding/consistent-identification
- Chan, "Mental Models", 26 January 2024 (last reviewed 1 September 2026): all four quotations exact; designers' detailed models; users' models built on other sites. PASS. https://www.nngroup.com/articles/mental-models/
- Norman 2013: jnd.org contents list ch. 1 sections "Conceptual Models" and "The System Image", Basic Books 2013. PASS. https://jnd.org/the-design-of-everyday-things-revised-and-expanded/ The three-model account (designer's model, user's model, system image as the only channel; wrong model when the image is unclear) confirmed from a review of the earlier edition quoting "all communication takes place through the system image" and "the user will end up with the wrong mental model". PASS, as the unsure list states. https://kairos.technorhetoric.net/3.1/reviews/eiler/design.html
- Young, Mental Models, Rosenfeld Media, February 2008: title and author. PASS. https://rosenfeldmedia.com/books/mental-models/ Régeni, Ergomania, 3 April 2018: tasks grouped into towers, towers into mental spaces, existing functions below the horizontal line, gaps as missing and unnecessary functions. PASS (the "towers with nothing below" reading is the review's logic, as the unsure list allows). https://ergomania.eu/indi-young-mental-models-review/
- Baum, "What Is Your Mental Model?", 14 February 2008, interview with Young; comment quotation exact. PASS (see minor). https://boxesandarrows.com/what-is-your-mental-model/
- Rosch and others, "Basic Objects in Natural Categories", Cognitive Psychology 8, 1976, 382–439: "the most inclusive categories for which a concrete image of the category as a whole can be formed" and "the earliest categories sorted and earliest named by children" exact; furniture, chair, kitchen chair in Table 1. PASS. https://www.cns.nyu.edu/~msl/courses/2223/Readings/Rosch-CogPsych1976.pdf
- Rosch and Mervis, "Family Resemblances", Cognitive Psychology 7, 1975, 573–605: all four quotations exact. PASS; the issue number "no. 4" is not on the PDF and is unverifiable. https://courses.grainger.illinois.edu/cs440/fa2023/Quizzes/grad-readings/rosch-and-mervis.pdf
- Lakoff 1987, University of Chicago Press: publisher's description, categories built "around protoypical examples" radiating from central types. PASS. https://press.uchicago.edu/ucp/books/book/chicago/W/bo3632089.html
- Rosenfeld, Morville and Arango 2015, ch. 6: "Challenges of Organizing Information" with Ambiguity, Heterogeneity, Differences in Perspectives, Internal Politics; Exact and Ambiguous Organization Schemes. PASS. https://oreilly.com/library/view/information-architecture-4th/9781491913529/ch06.html Topic as an ambiguous scheme: confirmed by a course summary of the book's schemes. PASS. https://users.monash.edu/~cema/courses/CSE3325/lect7.html
- Rosenfeld, Morville and Arango 2015, ch. 7: opens "Labeling is a form of representation"; the five varieties as section headings; "General Guidelines" under Designing Labels. PASS. https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch07.html
- Rosenfeld, Morville and Arango 2015, chs 3, 4, 9, 11: "Design for Finding", "Design for Understanding", "Does Your Product Need Search?", "Search Log Analysis". PASS. https://oreilly.com/library/view/information-architecture-4th/9781491913529
- Tankala, "Card Sorting: Pushing Users Beyond Terminology Matches", 14 June 2024: quotation exact. PASS. https://www.nngroup.com/articles/card-sorting-terminology-matches/
- Furnas and others 1987, CACM 30(11), 964–971: "surprisingly large"; "In every case two people favored the same term with probability <0.20"; "80-90 percent failure rates in many common situations"; "unlimited aliasing"; "several-fold improvements"; five application domains. PASS. https://cacmb4.acm.org/magazines/1987/11/10035-the-vocabulary-problem-in-human-system-communication and https://honnef.co/notes/references/furnasvocabularyproblemhumansystem1987
- Nielsen, "Use Old Words When Writing for Findability", 27 August 2006: three quotations exact; being found is the first step, the user must still click and the page convert. PASS. https://www.nngroup.com/articles/web-writing-use-search-keywords/
- Farrell, "Search-Log Analysis", 30 July 2017: three quotations exact; heating-pads example; all six recommendations; reformulated queries within a session. PASS. https://www.nngroup.com/articles/search-log-analysis/
- Laubheimer, "Menu-Design Checklist: 17 UX Guidelines", 7 June 2024: guideline 7 title exact; made-up words, jargon, abstract categorisation; front-loading in guideline 8. PASS. https://www.nngroup.com/articles/menu-design/
- Krause, "Maintain Consistency and Adhere to Standards", 10 January 2021: three quotations exact. PASS. https://www.nngroup.com/articles/consistency-and-standards/
- Nielsen, "Search and You May Find", 14 July 1997: "more than half of all users are search-dominant", "about a fifth of the users are link-dominant", "the rest exhibit mixed behavior". PASS (see minor on the URL). https://www.nngroup.com/articles/search-and-you-may-find/
- Spool, "Are There Users Who Always Search?", UIE, 1 May 2001: all five quotations exact; design drives the behaviour; users said they always searched. PASS. https://articles.centercentre.com/?p=15
- Katz and Byrne 2003: abstract confirms search not faster or more accurate, the four influences, breadth and scent on novel sites, "should not be used to compensate for poor menu design". PASS. https://unpaywall.org/10.1145%2F937549.937551 TOCHI 10(3), 198–220 confirmed from a reference list. https://www.humanfactors.com/newsletters/the_answer_you're_searching_for.asp
- Teevan and others, CHI 2004: both quotations exact; modified diary study across email, files and the web; even when they "knew exactly what they were looking for". PASS. https://www.microsoft.com/en-us/research/publication/perfect-search-engine-not-enough-study-orienteering-behavior-directed-search/
- Bates 1989: both quotations exact; Online Review 13(5), 407–424. PASS. https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html and https://demo.kerko.whiskyechobravo.com/bibliography/4CS6GYS2
- Spencer, "Four Modes of Seeking Information", 14 March 2006: the four modes as named. PASS. https://boxesandarrows.com/four-modes-of-seeking-information-and-how-to-design-for-them/
- Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 18 July 2011: "in their own words"; like qualitative studies; analytics tell what, not why; "only hypotheses". PASS. https://uxmatters.com/mt/archives/2011/07/site-search-analytics-a-conversation-with-lou-rosenfeld.php
- Rosenfeld, Search Analytics for Your Site, Rosenfeld Media, 2011: title and author. PASS. https://rosenfeldmedia.com/?p=183965 (the unit's /books/search-analytics/ URL was not returned by search: unverifiable as a link).
- Morville, "User Experience Design", Semantic Studios, 21 June 2004: seven facets; quotation exact. PASS. https://semanticstudios.com/user_experience_design/
- Morville, Ambient Findability, O'Reilly, September 2005, ch. 1 "Lost and Found". PASS. https://oreilly.com/library/view/ambient-findability/0596007655 The three-part definition (locatable or navigable; degree to which a particular object is easy to discover or locate; degree to which a system or environment supports navigation and retrieval) quoted from p. 4 by a review. PASS. https://ariadne.hosting.lboro.ac.uk/issue/49/tonkin-rvw
- Krug, Don't Make Me Think, Revisited, 3rd ed., New Riders: chs 1, 2, 4 titled as the unit says. PASS. https://oreilly.com/library/view/dont-make-me/9780133597271 Peachpit excerpt, 27 January 2014: second-law quotation exact; "scent of information". PASS. https://peachpit.com/articles/article.aspx?p=2170656
- Laubheimer, "The 3-Click Rule for Navigation Is False", 11 August 2019: quotation exact; Porter 2003 cited, abandonment does not rise past three clicks. PASS. https://www.nngroup.com/articles/3-click-rule/
- Larson and Czerwinski, CHI 98, pp. 25–32: both quotations exact. PASS. https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/
- Laubheimer, "Tree Testing", 6 August 2023 (reviewed 19 August 2026): quotation exact; no visual styling. PASS. https://nngroup.com/articles/tree-testing/
- Cooper and others 2014, ch. 1: cited as IA1, section 2.4, cites it (implementation model versus mental model, represented model); consistent with the filed unit. Not re-opened.
- Unverifiable: Rosenfeld, Morville and Arango ch. 6 one-line glosses and ch. 7 "General Guidelines" content (headings only seen, as the unsure list says); the part02.html contents URL; Rosch and Mervis issue number; the alertbox/9707b.html URL.

## Coverage against the brief

- Information foraging and scent, Pirolli and Card 1999 plus NN/g applications: covered (1.1). Strong and weak scent in a label and a link: covered (1.2, with the table and figure).
- Mental models as Young and Norman use the term, and the gap: covered (2.1–2.3).
- Categorisation: basic level, prototypes, the four challenges, meaning for a navigation scheme: covered (3.1–3.3).
- Labelling: forms, vocabulary mismatch, evidence on consistency and specificity, with the two strengths separated: covered (4.1–4.3).
- Search versus browse, and search logs: covered (5.1–5.2).
- Findability (Morville) and Krug, with limits of each: covered (6.1–6.2).
- Figures named by the brief: foraging loop, scent comparison, model gap, categorisation example: all present; five figures, within three to eight.
- Deliverable: checklist with every item sourced, applied item by item to an invented as-is, verdict and fix per failing item, IA6 keeps the passed labels: present in full and usable alone.
- Tool-agnostic: no tool named. "Not X but Y" constructions: none found.

## Figures (numbers, labels, kinds, captions)

Every number in the unit says whose figure it is (Nielsen 2009, Furnas 1987, Spool 2001, Nielsen 1997, Morville 2004). Anecdote, practice and interview sources are labelled (Spool, Spencer, Mausser, Régeni, Baum, Krug); controlled and measured studies are named as such (Katz and Byrne, Teevan, Nielsen 2009, Furnas); NN/g guidance is labelled guidance. Counts re-run by script: 4 moves, 4 NN/g bullets, 6 table tests, 2 model-gap rows, 6 claimable items, 5 log queries, 7 honeycomb facets, 5 label varieties, 3 causes, 4 seeking modes, 19 checklist items (A1–A5, B1–B2, C1–C4, D1–D3, E1–E3, F1–F2), 19 applied rows, 17 Fail and 2 Pass, "three of five" Home elements. All agree with the text.

1. Flow, section 1.1. Labels and notes (Enter a patch / a site, a screen or a list; Read the cues / link labels, headings, the words around them; Judge the scent / likely value against the cost of getting there; Follow or leave with the two bracketed conditions) all appear in the sentence "The loop the theory describes has four moves…". Caption names section 1.1, Pirolli and Card 1999 and Card and others 2001, explains the "→ see" return and the bracketed conditions (IA2's continuation and condition rules), says Perqo is fictional. Tone 3 on every step for the employee, as IA2 sets. Kind fits a sequence. PASS.
2. Matrix, section 1.2. Rows are the six tests of the table; every cell ("no subject", "Your balance", "no"/"yes", "no: two on Home", "none", "Balance") is in the table. Caption names section 1.2, the five sources of the table, the tones and the legend; Perqo fictional. Kind fits items by dimensions. PASS.
3. Matrix, section 2.3. Every cell traced: "four allocations, one per open category and period", "one Balance total on Home", "one pot of money", "a course claim is rejected while Home shows money left", "Submitted, Approved, Rejected, Paid", "Submitted and Paid groups; rejected only in Notifications", "a claim missing from the list is lost", "rejected claims cannot be found where claims are listed". Caption names section 2.3, Norman 2013 ch. 1, the tones (5 the Perqo system, 3 the app and the employee, 6 the fault), marks the employee column assumed, cites IA1 2.4, IA1 5 and IA2 5.3. Kind fits. PASS.
4. Matrix, section 3.3. Six items by four categories; each "covered: <narrower term>" and each "may look here" matches the paragraph's placing (cookery course → Meals, yoga class → Learning, bike helmet → Health). Caption names section 3.3, Rosch and Mervis 1975, Rosch and others 1976, Rosenfeld, Morville and Arango ch. 6, tones and legend, assumed status, IA2 5.3 for categories and terms. Kind fits. PASS.
5. Sitemap, Deliverable. Every box label and note traced to the as-is list and the applied table (Balance/B1; Learn more/A1, A2, A3, A5; Recent activity "Pending"/D2; Discover/A1, D1, D2; "+"/A4; the four category screens/C2, C3; Perks/C1, C4, D1, D2; Claims/B2, F2; New claim → Check and submit; Help with claims → Claim articles; Card details, Purchases, Freeze card; Profile, Notifications; Documents/A1, C4, D1, F2 with Approval rules H-1.2.4; Help/A3). Type tags all from IA2's list; root untagged and explained in the caption; tone 3 everywhere, tone 6 on the faults; "→ see" on every external route. Caption names the Deliverable, F2, the tones, IA1 5 and IA2 5.3. Kind fits a hierarchy. FIX: F1 is missing from the notes of the four elements the F1 row fails (replacement JSON in the first finding).

## Perqo

Every Perqo fact checked against IA1, IA2 and perqo-facts.md: the three surfaces, the five tabs, the four categories and their narrower and variant terms, allocation/Budget/Balance, Claims and Purchases as separate lists, the four claim states, the Claims screen groups Submitted and Paid, New claim → Check and submit (balance after), the contextual route to the claim articles, no search in the app and search in the Help centre only, H-2.1.2 (says "refund", marked update), H-2.2.1, H-1.2.4 (a PDF, marked remove), the Help centre split by audience. All consistent. Labels "(Perqo, fictional)" appear 15 times, on the first use in each section that sets a fact; the one unlabelled new fact is the frequency of use in 6.2 (minor above).

New Perqo facts IA3 sets (for the register):
- The balance a claim is checked against is the balance of the category chosen on the New claim form (2.3, an explicit extension of IA2's rule).
- Home shows one Balance total, the sum of the four category balances (2.3, Deliverable).
- As-is: an approved claim stays in the Submitted group until paid; a rejected claim is not listed and appears only as a message in Notifications (2.3, Deliverable).
- Each client's policy lists what is covered under each category; the app's category screen shows the category's balance and a "What's covered" list of narrower terms with no examples (3.3, Deliverable).
- The example client's policy places: gym membership → Health, Fitness; train pass → Mobility, Public transport; coding course → Learning, Courses; cookery course → Learning, Courses; yoga class → Health, Fitness; bike helmet → Mobility, Bike (3.3).
- The Help centre's For employees search log for one quarter, top five queries in rank order: refund (→ H-2.1.2), allowance (zero results), rejected claim (→ H-2.1.2), gym (zero results), approval (→ H-1.2.4); nobody reads the log (5.2, E2).
- The first merchant fact: merchants that accept the Perqo card can publish offers, listed in the app, reached from Home's "Discover" banner (with a second "Learn more") and from Benefits as a fifth item "Perks"; the partnerships team asked for both placings (Deliverable).
- Home as-is: Balance total with a "Learn more" link to H-2.2.1; Recent activity mixing purchases and claims, a submitted claim shown as "Pending"; a "Discover" banner; a "+" icon with no text opening New claim (Deliverable).
- Claims as-is: a "Help with claims" link to the claim articles; New claim asks category, amount, receipt (Deliverable).
- Card: Card details, Purchases, Freeze card. Account: Profile, Notifications, Documents (holding the Approval rules PDF H-1.2.4), Help (opens the Help centre home, where both audiences start) (Deliverable).
- Perqo Admin is used daily by the same HR and finance managers; the employee app is opened a few times a month (6.2, unlabelled; see minor).

## Pointers

- To IA1: four systems (intro), 2.4 data model and Balance/Budget mapping (2.1, 2.3, 4.2, 4.3), section 5 states and tabs (2.3, Deliverable), Deliverable vocabulary (4.2): all say what IA1 says.
- To IA2: section 5 and the notation sheet (intro, face line), 5.3 inventory, vocabulary, Claims screen, decision tree, navigation table (1.2, 2.3, 3.3, 4.1, 4.2, 5.1, Deliverable), 1.2 (D3): all say what IA2 says, with the one reconciliation noted as minor (Approved shown in the app).
- Forward: IA4 chooses schemes by C1–C4 and IA6 navigation by A1–A5, B1, B2, F1, F2 (Gives: "the criteria IA4's schemes and IA6's navigation are chosen by"); IA6 replaces the as-is and keeps the passed labels (IA6 brief and Takes line); IA11 measures C3, B2, A1–A3 by tree test and first-click test (IA11 Takes "IA3's findability evidence"; IA11 brief names both methods); IA12 takes the log as proxy evidence with each row a hypothesis (IA12 Takes "IA3's search logs as proxies"; IA12 brief lists search logs among proxy evidence with limits labelled). All match units_data.py.

## Public-site rules

No personal fact about the reader beyond the brief's profile; no private person named. The only named people are published authors.

## Verdict

IA3 · keep · 0 error · 2 should-fix · 6 minor. (Zero errors; the two should-fix edits and six minor edits above are a short errata list, each Current occurring exactly once in the filed file, checked with grep -F -c.)

## Maintainer's note (N8, 3 Nov 2026, Opus 5.5)

The report above was saved before any finding was applied. Each finding was verified before it was applied, as an exact replacement by script (each Current occurring once in the unit):

- Figure 5 F1 notes (should-fix): verified against the unit's applied table (rows A5 and F1) and its as-is list ("with a second "Learn more" under the banner"); applied as given, four notes.
- Row A2's list (should-fix): verified against the as-is list and "What IA6 keeps". Holds in part: the proposed parenthesis said Discover, Perks and Documents "fail A1", but the A1 row fails Discover and Documents and not Perks, which fails C1 and D1. Applied as: "Discover, Perks and Documents pass A2 as single words and fail on A1, C1 and D1"; Balance and Recent activity added to the passing list as the finding asked; the row's fix column "keep every other label as it is" became "the other labels need no change under A2", since Discover, Perks and Documents are changed by other rows.
- McCloskey label (minor): verified by WebSearch and a fetch of https://www.nngroup.com/articles/writing-links/ (a URL the search returned): only the first-words point cites NN/g eyetracking research. Applied as given.
- Young's comment (minor): verified by WebSearch and a fetch of https://boxesandarrows.com/what-is-your-mental-model/: comment 3, 15 February 2008, posted as "Anonymous", signed in its text as the book's author. Applied, then widened by one more replacement so the sentence names the interview it comments on: "A comment on Chris Baum's interview with Young, posted anonymously and signed as the book's author, describes the diagram as one that".
- Rosch and others 1976 (minor): verified by WebSearch and a fetch of the cns.nyu.edu PDF: the abstract reads "most codable, most coded, and most necessary in language". Applied as given.
- Nielsen 1997 URL (minor): verified by WebSearch (extended), which returned https://www.nngroup.com/articles/search-and-you-may-find/, and a fetch of it: title, author, date and all three quotations verbatim. Applied in the text and in Sources.
- Frequencies in 6.2 (minor): verified against perqo-facts.md ("volumes" not yet set; no frequency of use set by IA1 or IA2). Applied as given.
- Approved in the app (minor): verified against IA2 §5.3's state-diagram paragraph ("Submitted, Approved and Paid are tone 5, because a claim's status is shown on both Admin and the app"). Applied with one change: "B2's fix" became "the Deliverable's fix for B2", since the reader meets B2 only in the Deliverable.

Figure 5 (FIX) was fixed and re-checked by a new agent given only the unit's text with its figures taken out, the captions and figure 5's frames sheets (`verify.py --shots`, page `read-ux-ia3`); its report follows below when it is in. Figures 1 to 4 passed.

## Figure 5, re-check 1 (fresh Opus 5.5 agent; given only the unit without its figures, the captions and figure 5's frames sheets): report verbatim

# Figure 5 (sitemap) re-check: IA3, Deliverable

I checked all six sheets: phone, tablet and desktop, each in dark and light. On desktop and tablet the figure fits in one frame. On phone it takes 3 frames of sideways scroll.

## (a) Labels, notes, type tags and checklist IDs against the unit's text

### Labels and notes that are correct

- **Root, "Perqo app" / "tab bar: global routes".** Source: "the tab bar, which carries the app's global routes, with its five tabs Home, Benefits, Claims, Card and Account". It has no type tag, as the caption says. Tone 3.
- **The five tabs, Home, Benefits, Claims, Card and Account.** Same line. Tone 3, except Claims (see below).
- **Balance, "one total; fails B1".** Source: "One Balance total, the sum of the four category balances". Row B1: "Home shows one Balance total". Tone 6.
- **Learn more, EXTERNAL, "→ see H-2.2.1; fails A1, A2, A3, A5, F1".** Source: "with a "Learn more" link under it to H-2.2.1 on perqo.com". The rows that name it:
  - A1: "Learn more" (Home, twice)
  - A2: "Learn more" opens with no subject
  - A3: "Learn more" opens a page titled "Your balance explained"
  - A5: Two "Learn more" links
  - F1: "Learn more"

  All five IDs are present.
- **Recent activity, "claim shown as Pending; fails D2".** Source: "A list of recent activity ... shows a submitted claim as "Pending"". Row D2: "A submitted claim is "Pending" on Home".
- **"+", FORM, "→ see New claim; fails A4, F1".** Source: "A "+" icon, with no text, that opens New claim". Rows A4 and F1 both name it.
- **Health, "What's covered: no examples; fails C2, C3".** Source: "Each category screen shows its balance and a "What's covered" list of its narrower terms, with no examples". Row C2 names Health ("(Fitness, Therapy)"). Row C3 names the yoga class, whose second place is Learning, and the bike helmet, whose second place is Health.
- **Perks, "offers again; fails C1, C4, D1, D2, F1".** All five IDs are correct:
  - C1: "Perks ... sits in the list of benefit categories"
  - C4: "Offers appear twice because the partnerships team asked"
  - D1: "Perks"
  - D2: "Perks" in Benefits
  - F1: "in Benefits, the fifth item is of another kind"
- **Claims, "Submitted, Paid; no rejected; fails B2, F2".** Source: "The Submitted and Paid groups; ... rejected claims are not listed". Rows B2 and F2 both name it. Tone 6.
- **New claim and Check and submit, FORM, tone 3.** Source: "New claim asks for a category, an amount and a receipt; Check and submit follows". No row's "what decides it" column names either one.
- **Help with claims, EXTERNAL, "→ see Claim articles", tone 3.** Source: "A link "Help with claims" opens the claim articles in the Help centre". It is kept ("What IA6 keeps").
- **The Card children, Card details, Purchases and Freeze card, tone 3.** Source: "Card details, Purchases, Freeze card". All are kept.
- **Profile and Notifications, tone 3.** Both are kept.
- **Documents, INDEX, "fails A1, C4, D1, F2".** Rows A1, C4, D1 and F2 all name it.
- **Approval rules, FILE, "H-1.2.4, for HR".** Source: "Documents (which holds the "Approval rules" PDF, H-1.2.4 ...)". F2 says "a PDF written for HR".
- **Help, EXTERNAL, "→ see Help centre home; fails A3".** Row A3: "Account's Help opens the Help centre home".

### Errors

1. **Discover is missing C4, and its note mixes two elements.**
   - Row C4 says "Offers appear twice because the partnerships team asked". The text adds "The partnerships team asked for both placings". So both placings fail C4: Discover on Home and Perks in Benefits. Perks carries C4. Discover does not.
   - The note puts the second "Learn more" inside the Discover box. It then lists one set of IDs ("fails A1, A5, D1, D2, F1") after "under it". The reader cannot tell which IDs belong to Discover and which to the second Learn more.
   - A5 belongs only to the Learn more ("Two "Learn more" links on Home open two destinations").
   - A2 is missing for the second Learn more. Row A2 says ""Learn more" opens with no subject", and the A2 row says Discover itself passes A2.
2. **Approval rules is drawn in tone 6 but its note has no IDs.** The caption says tone 6 "marks each element that fails an item of the checklist (item IDs in the notes)". Two rows name this file:
   - C4: "approval rules sit in Documents because Product holds them as a PDF for HR"
   - F2: "reachable only through Account, Documents, a PDF written for HR"
3. **Mobility's note "as Health" gives it C3, which no row supports.**
   - Row C3 says "A cookery course, a yoga class and a bike helmet have no route from the second category an employee is assumed to look in". Section 3.3 names those second categories: Meals for the cookery course ("sits near Meals"), Learning for the yoga class ("pulls it towards Learning") and Health for the bike helmet ("pulls towards Health").
   - Mobility is no item's second category, so it fails C2 only. "as Health" stands for Health's "fails C2, C3", so it is wrong for Mobility.
   - "as Health" is also open to misreading as "classed as Health". Learning and Meals do fail C2 and C3, so their notes are correct in substance. Writing the IDs out removes the ambiguity.

### Elements a row names without failing them (no change)

Four elements appear in a failing row only as the place a fault shows, or as the correct term:
- Notifications, in B2 and F2.
- Account, in F2.
- Home, in A1, A5 and F1.
- Claims' "Submitted", in D2.

The fix column keeps each of them ("What IA6 keeps" lists the five tabs and Notifications, and D2's fix says "Use Submitted everywhere"). Leaving them in tone 3 with no ID is correct.

### Observation on a type tag (no change needed for PASS on its own)

Balance is tagged DETAIL. The text describes Balance only as a figure on Home ("One Balance total ... with a "Learn more" link under it"), and nothing says it opens a page. The tag claims a page the text does not describe. The notation sheet's tag set (IA2) is not in this folder, so I cannot name the right tag. The writer should confirm that DETAIL is IA2's tag for an on-screen element, or change it.

## (b) Caption

The caption says what the figure shows: as-is navigation, F2, page types tagged, root without a type tag, the five tabs as its children. It names the section (Deliverable) and the sources: "from IA1, section 5, and IA2, section 5.3; every other element from this Deliverable". This matches the text: "It keeps everything IA1 and IA2 set ... (IA1, section 5; IA2, section 5.3). It adds, as faults ...".

On tones, the caption is correct for every box except Approval rules: it is tone 6 with no IDs in its note. Error 2's fix brings the drawing into line with the caption. The caption itself needs no change.

## (c) Kind

A sitemap tree is the right kind for a hierarchy of screens. It follows the text: "square-cornered boxes with type tags, every box in the app's tone 3, the faults ... in tone 6, and every route that leaves the app tagged `external` with a "→ see" note". All three exits (Learn more, Help with claims, Help) are EXTERNAL and have "→ see" notes.

## (d) Drawing as read

- **Desktop and tablet, dark and light.** One frame holds the whole figure. No text overlaps or is cut, and all text sits inside its box. The caption is under the figure.
- **Phone, dark and light.** Three frames of sideways scroll, with a "scroll sideways for the whole figure" hint. Every box appears whole in at least one frame:
  - Frame 1: the Home column, Benefits and Card.
  - Frame 2: Benefits, Claims and Account.
  - Frame 3: Claims, its children and Account.

  The faded right edge is the scroll affordance, and no box is clipped in every frame. The caption sits under the figure in each frame. The monospace notes are legible at phone width.
- Tones show clearly in both themes: teal for tone 3 and ochre for tone 6.

No rendering faults.

## FIX: exact replacements (figure notes)

1. **Discover box.**
   - Current: "offers; a second Learn more under it; fails A1, A5, D1, D2, F1"
   - Replacement: "offers; fails A1, C4, D1, D2, F1; a second Learn more under it fails A1, A2, A5, F1"
2. **Approval rules box.**
   - Current: "H-1.2.4, for HR"
   - Replacement: "H-1.2.4, for HR; fails C4, F2"
3. **Mobility box.**
   - Current: "as Health"
   - Replacement: "What's covered: no examples; fails C2"
4. **Learning box.**
   - Current: "as Health"
   - Replacement: "What's covered: no examples; fails C2, C3"
5. **Meals box.**
   - Current: "as Health"
   - Replacement: "What's covered: no examples; fails C2, C3"

Fixes 4 and 5 are for clarity. Their substance is already correct.

The caption needs no change.

## The unit's own text (outside the figure)

1. **Section 2.3 repeats "on Home" in one sentence.**
   - Current: "The app's Home screen (Perqo, fictional) shows one Balance total on Home, the sum of the four category balances."
   - Replacement: "The app's Home screen (Perqo, fictional) shows one Balance total, the sum of the four category balances."
2. **Section 2.3 says the same thing twice.**
   - Current: "An employee with money left in Meals and none in Learning who claims a course is rejected, over balance: a course claim is rejected while Home shows money left."
   - Replacement: "An employee with money left in Meals and none in Learning who claims a course is rejected, over balance, while Home shows money left."
3. **Deliverable, as-is navigation, Home bullet: the parenthesis repeats the clause before it.**
   - Current: "shows a submitted claim as "Pending" (a claim shown as Pending)."
   - Replacement: "shows a submitted claim as "Pending"."
4. **Checklist applied, row A2: the grouped list makes each label seem to fail all three items.** In fact Perks does not fail A1, and Discover and Documents do not fail C1.
   - Current: "Discover, Perks and Documents pass A2 as single words and fail on A1, C1 and D1"
   - Replacement: "Discover, Perks and Documents pass A2 as single words; Discover and Documents fail on A1 and D1, Perks on C1 and D1"
5. **Checklist applied, row F1: the count leaves out the second "Learn more".** Row A1 and the as-is list count two "Learn more" links on Home. The figure folds the second one into Discover, so its five Home children match the "five". The text should still say what it counts.
   - Current: "On Home, three of five elements are ambiguous ("Learn more", "Discover", "+")"
   - Replacement: "On Home, three of five elements are ambiguous ("Learn more", "Discover" with the second "Learn more" under it, "+")"

Figure 5: FIX

### Maintainer's note on re-check 1

FIX. Verified against the unit's applied table, the as-is list and section 3.3 (second places: cookery course Meals, yoga class Learning, bike helmet Health). Applied as given: the Discover note (C4 added; the second Learn more's IDs, A1, A2, A5, F1, split out), Approval rules' IDs (C4, F2), the Learning, Mobility and Meals notes written out (Mobility fails C2 only), and text notes 3, 4 and 5. Held in part: text note 1 (the repeated "on Home") and note 2 (the repeated clause in 2.3) quote the lines figure 3's cells are traced to ("one Balance total on Home"; "a course claim is rejected while Home shows money left"), so the cells' wording was kept and the sentences reworded around it: "The app (Perqo, fictional) shows one Balance total on Home, the sum" and "who claims a course is rejected, over balance. The gap: a course claim is rejected while Home shows money left." Removing "(a claim shown as Pending)" (note 3) took away the line figure 5's Recent activity note was traced to, so that note became "a submitted claim as Pending; fails D2", the text's own words. The observation on Balance's `detail` tag was checked against IA2's fixed tag list (§5.2: `detail`, one item); Balance shows one item, the employee's total, so the tag stands. Re-check 2 follows.
