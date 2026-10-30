---
audit: fresh check
unit: IA1 · What information architecture is, and where it sits
course: ux · IA · Information Architecture
model: Opus 5.5 (search on; a Fable 5.1 fresh check is owed, row P49)
date: 2026-10-30
chat: own Opus 5.5 agent context, not shown the writing (P31), in session https://claude.ai/code/session_01KMmgR2Zan8kwEeeM9BGKBs
verdict: keep · 0 errors, 4 should-fix, 7 minor (all applied the same day)
---

# Fresh check · IA1 · What information architecture is, and where it sits

The checker's final report, verbatim. Checked with Opus 5.5, not Fable 5.1: Pedro deferred Fable checks on 29 Oct 2026, and the Fable 5.1 fresh check that replaces this one is owed (backlog row P49).

# Fresh check · IA1 · What information architecture is, and where it sits

Checker: Opus 5.5, isolated context (P31). Read: prompt.md, unit.md, brief.md, sourcing-standard-parts-1-and-4.md. Live search and fetch on 30 Oct 2026.

## (1) Coverage

- Rosenfeld, Morville and Arango's four systems, what the definition includes and leaves out: covered (1.1).
- Covert's sense-making, and information vs content vs data: covered (1.2).
- Arango's architecture of information environments: covered (1.3).
- Garrett's structure plane between scope and skeleton: covered (1.4).
- IA vs navigation design, with worked example: covered (2.1).
- IA vs the user interface, with worked example: covered (2.2).
- IA vs content strategy, with worked example: covered (2.3).
- IA vs the engineering data model, with worked example: covered (2.4).
- Why IA exists (library science and the first web, the Polar Bear book's history, Wurman's coinage), told briefly: covered (3).
- What an IA deliverable is for, which decision it supports, who reads it: covered (4).
- First look at IA across three surfaces, Perqo: covered (5).
- Figures the brief names (the four systems; Garrett's planes with IA located; the Perqo surfaces and who uses each): covered (figures 1, 2 and 4). Six figures in all, inside the range of three to eight.
- Deliverable, definition sheet (what IA is, what it is not, the four systems in a sentence each, the five questions): covered.
- Deliverable, Perqo surfaces map: covered.
- Length: about 5,400 words of prose, inside 2,000 to 6,000.

## (2) to (5) Findings

[should-fix] [accuracy] 4; Current: `Garrett published a notation for drawing such diagrams, *A visual vocabulary for describing information architecture and interaction design* (2002, [jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/)); IA2 sets this course's own notation.`; Problem: the vocabulary was first released in October 2000 and revised afterwards, so "(2002)" dates the first release two years late. The jjg.net page cannot be fetched (robots), so no 2002 version date could be confirmed either; Fix: `Garrett published a notation for drawing such diagrams, *A visual vocabulary for describing information architecture and interaction design* ([jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/)), first released in October 2000 and revised since ("The Visual Vocabulary Three Years Later: An Interview with Jesse James Garrett", Boxes and Arrows, 11 December 2003, [boxesandarrows.com](https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/)); IA2 sets this course's own notation.`; Basis: Boxes and Arrows, 11 Dec 2003, "In October 2000, Jesse James Garrett introduced a site architecture documentation standard called the Visual Vocabulary", https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/ ; also Rosenfeld and Morville, 2nd ed. 2002, appendix "Examples, Deliverables, and Tools" ("originally released in October 2000"), https://www.oreilly.com/library/view/information-architecture-for/0596000359/apas07.html

[minor] [accuracy] Sources; Current: `- Garrett, Jesse James. "A visual vocabulary for describing information architecture and interaction design". 2002. [jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/)`; Problem: same date as the finding above, and the new Boxes and Arrows source must also be listed; Fix (two lines, replacing the one): `- Garrett, Jesse James. "A visual vocabulary for describing information architecture and interaction design". First released October 2000, revised since. [jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/)` NEWLINE `- "The Visual Vocabulary Three Years Later: An Interview with Jesse James Garrett". Boxes and Arrows, 11 December 2003. [boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett](https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/) (interview; practice).`; Basis: as above.

[should-fix] [attribution] Deliverable, What IA is not; Current: `- **Navigation.** Navigation is the set of interface components that let people move through the IA. Changing a menu is not an IA change; changing what is grouped or what it is called is (Cardello 2014).`; Problem: Cardello does not say that changing a menu is not an IA change. She says IA informs navigation, and warns that choosing navigation components on looks "can force you to change an ideal IA". The rule is the unit's own (section 2.1) but is attributed to her, and it is also a not-X-but-Y construction the brief bans; Fix: `- **Navigation.** Navigation is the set of interface components that let people move through the IA; the IA is the organisation, structure and naming beneath them (Cardello 2014). Swapping one menu component for another leaves the IA as it was; changing what is grouped or what it is called changes it (this unit's rule, section 2.1).`; Basis: Cardello, NN/g, 22 Jun 2014 (IA is "the underlying organization, structure and nomenclature"; "IA informs UI"), https://www.nngroup.com/articles/ia-vs-navigation/

[should-fix] [attribution] Deliverable, What IA is not; Current: `- **The user interface.** The interface decides which controls present the structure on a screen. A table redesign leaves the IA as it was; removing a route to an item changes it (Garrett 2000).`; Problem: Garrett's diagram defines interface design and IA. The table-redesign and removed-route rule is the unit's own Perqo example (section 2.2), not Garrett's; Fix: `- **The user interface.** The interface decides which controls present the structure on a screen; the IA is the structure beneath it (Garrett 2000). A table redesign leaves the IA as it was; removing a route to an item changes it (this unit's rule, section 2.2).`; Basis: Garrett, diagram of 30 Mar 2000, https://www.jjg.net/elements/pdf/elements.pdf

[should-fix] [figure] 1.4; Current: `and interface design is "design of interface elements to facilitate user interaction with functionality" (Garrett 2000).`; Problem: figure 2 puts functional specifications in the software column, content requirements in the hypertext column and information design in both skeleton cells. The unit's text never states these placings, so the figure adds facts (Part 1, "A figure adds no fact"). The placings themselves match the 2000 diagram; Fix: `and interface design is "design of interface elements to facilitate user interaction with functionality" (Garrett 2000). The same diagram puts functional specifications on the software side of the scope plane and content requirements on the hypertext side, and sets information design on the skeleton plane in both columns, beside interface design and beside navigation design (Garrett 2000).`; Basis: Garrett, diagram of 30 Mar 2000 (its text carries the information-design definition twice, once per column; functional specifications and content requirements are the two scope elements), https://www.jjg.net/elements/pdf/elements.pdf

[minor] [accuracy] 2.1; Current: `that help people find information and take action.`; Problem: Cardello's wording is that navigation components "help users find information and functionality, and encourage them to take desirable actions". The paraphrase drops functionality, which matters for a task-heavy product; Fix: `that help people find information and functionality and encourage them to take desirable actions.`; Basis: https://www.nngroup.com/articles/ia-vs-navigation/

[minor] [accuracy] 2.1; Current: `which she says supports about four levels of depth.`; Problem: the source gives a ceiling, not an approximation: "An inverted-L can accommodate sites that are no more than 4 tiers deep"; Fix: `which she says can hold a site no more than four tiers deep.`; Basis: https://www.nngroup.com/articles/ia-vs-navigation/

[minor] [attribution] Deliverable, What IA is not; Current: `They need not match, and the mapping between them is written down (Cooper and others 2014, ch. 1).`; Problem: Cooper and his co-authors argue that the represented model should sit close to the user's mental model. Writing the mapping down is the unit's own rule (section 2.4), attributed to them; Fix: `The closer what people meet sits to their mental model, the easier the product is to use (Cooper and others 2014, ch. 1). The two need not match, and the mapping between them is written down (this unit's rule, section 2.4).`; Basis: About Face 4th ed. contents, ch. 1, "Implementation Models and Mental Models", p. 16, https://content.e-bookshelf.de/media/reading/L-2753659-0f3cbca15c.pdf

[minor] [attribution] Sources; Current: `2nd ed. New Riders, 2011. Chs 2 to 7.`; Problem: the body cites Brown chs 3 to 7 and ch. 5, never ch. 2 (Diagram Basics). The 2nd ed. was published in September 2010 with a 2011 copyright, and the entry should say so because the unsure list raises it; Fix: `2nd ed. New Riders, 2011 (published September 2010, copyright 2011). Chs 3 to 7.`; Basis: InformIT catalogue, 2nd ed., published 15 Sep 2010, copyright 2011, contents, https://www.informit.com/store/communicating-design-developing-web-site-documentation-9780321712462

[minor] [style] 2.1; Current: `IA does not appear in the visible interface: it shapes the interface, and it is documented in spreadsheets and diagrams.`; Problem: a "not X: Y" construction of the kind the brief bans; Fix: `IA shapes the interface without appearing in it, and it is documented in spreadsheets and diagrams.`; Basis: brief, Tone ("no 'not X but Y' constructions").

[minor] [style] 5; Current: `It is also why this course does not stop at the sitemap:`; Problem: same construction; Fix: `It is also why this course goes past the sitemap:`; Basis: brief, Tone.

Figures (3): every number in the unit says whose it is. The only numbers are dates, editions, pages and Cardello's four tiers, and each carries its source. Pass, apart from the items above.

Labels (4): the unit has no anecdote, vendor or correlational data. Practice sources are labelled: Steenson as "a historian's blog, labelled as such" and the Knemeyer interview as "(interview; practice)". Cardello's sequencing is labelled "NN/g guidance". Pass.

Perqo: labelled "(Perqo, fictional)" on first use ("A Perqo claim (Perqo, fictional)"), at each worked example and in the deliverable. Names stay the same throughout:
- Budget in Admin, Balance in the app; Claims
- Admin areas: Employees, Budgets, Policies, Approvals, Reports, Settings
- App areas: Home, Benefits, Claims, Card, Account
- Benefit categories: Health, Learning, Mobility, Meals

No Perqo fact is used as evidence about the world. Pass.

Deliverable (5): both parts are present in full, follow from sections 1 to 5, and can be used on their own. The definition sheet carries every item the brief names. The attribution fixes above apply.

## Confirmed

- Rosenfeld, Morville and Arango, 4th ed., O'Reilly, October 2015. The four definitions in ch. 2 are verbatim: https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch02.html
- Ch. 2 asks "But isn't information architecture about making sitemaps, wireframes, and website navigation menus?" and says "But there is much more to this story!". Its sections include Context, Content and Users: same URL.
- The Part II introduction says "four systems that are shared by most interactive information environments". Chs 6 to 9 are Organization, Labeling, Navigation and Search Systems; ch. 10 is Thesauri, Controlled Vocabularies, and Metadata: https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/part02.html
- Ch. 5 says "a well-designed information architecture is invisible to users", and its sections include Browsing Aids, Search Aids and "Invisible" Components: https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch05.html
- Ch. 13, Design and Documentation, covers high-level and detailed sitemaps, wireframes, content mapping and inventory, content models, controlled vocabularies and IA style guides: https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/
- Covert's definition, "Information architecture (IA) is the way we arrange the parts of something to make it understandable as a whole", and the seven chapter titles in order: https://abbycovert.com/make-sense/
- Covert, How to Make Sense of Any Mess, CreateSpace (self-published), 2014: https://www.abebooks.com/9781500615994/Sense-Mess-Information-Architecture-Covert-1500615994/plp
- Covert, "What's Information?", UX Magazine, 22 Jan 2015, an excerpt of the book. All five quotations are verbatim, italics aside: https://uxmag.com/articles/whats-information
- Arango, UX Magazine excerpt of ch. 6, "Architecture", 14 Aug 2019. The definition, the Slack and Android passage and "by arranging semantic elements such as icons, labels, buttons, and links" are verbatim: https://uxmag.com/articles/living-in-information-responsible-design-for-digital-places-a-book-excerpt
- Living in Information: the ten chapter titles in order: https://rosenfeldmedia.com/books/living-in-information/
- Living in Information, 2018, is listed under Two Waves Books (unsure list item): https://www.perlego.com/publisher/10196/two-waves-books
- Garrett, Elements, 2nd ed., New Riders, published 16 Dec 2010, copyright 2011. The titles of chs 3 to 7 are as the unit gives them (unsure list item): https://www.informit.com/store/elements-of-user-experience-user-centered-design-for-9780321683687
- Garrett's diagram is dated 30 March 2000 and its column labels are "Web as software interface" and "Web as hypertext system". The definitions of information architecture, interaction design, navigation design and interface design are verbatim. The information-design definition appears twice, once per column (unsure list item): https://www.jjg.net/elements/pdf/elements.pdf
- Cardello, "The Difference Between Information Architecture (IA) and Navigation", NN/g, 22 Jun 2014, confirms that IA is "not part of the on-screen user interface", that it is "documented in spreadsheets and diagrams", the list of navigation components, and "a first pass is necessary": https://www.nngroup.com/articles/ia-vs-navigation/
- Halvorson and Rach, 2nd ed., New Riders, February 2012. Ch. 8 is "Content" and ch. 9 is "People"; the substance and structure questions are verbatim: https://www.oreilly.com/library/view/content-strategy-for/9780132883269/ch08.html
- The workflow question is verbatim and the governance paraphrase is faithful ("How are key decisions about content ...") (unsure list item): https://www.oreilly.com/library/view/content-strategy-for/9780132883269/ch09.html ; the full wording of both is in Brain Traffic's quad: https://www.braintraffic.com/blog/brain-traffic-lands-the-quad
- About Face, 4th ed.: the contents put "Implementation Models and Mental Models" in ch. 1 on p. 16, so the locator is confirmed. The body text could not be opened online, so the claim about what the section argues is unverifiable here; it matches the section's known argument (unsure list item): https://content.e-bookshelf.de/media/reading/L-2753659-0f3cbca15c.pdf
- Resmini and Rosati, Journal of Information Architecture vol. 3 no. 2, 2011, pp. 33 to 46. Confirmed from the article:
  - the 1964 Amdahl, Blaauw and Brooks paper on the IBM System/360, defining architecture as "the conceptual structure and functional behavior"
  - the 1970 Xerox PARC group and the "architecture of information"
  - Wurman's 1976 conference address
  - Morville's report of the 1975 coinage (unsure list item)
  - the 1994 courses
  - the 1998 book that "hit the shelves, and information architecture went mainstream"
  - the "Polar Bear book" nickname, from its cover image
  - Morville's "this is not information architecture, this is information design"
  https://journalofia.org/volume3/issue2/03-resmini
- Steenson, girlwonder.com, 1 Oct 2010: Wurman chaired the 1976 AIA convention in Philadelphia, and the brochure line is "A place where public information is not public" (unsure list item): https://www.girlwonder.com/2010/10/you-really-wish-you-could-attend-these-conferences.html
- Knemeyer, "Richard Saul Wurman: The InfoDesign interview", InfoDesign, January 2004. Wurman says architecture "was a clearer word that had to do with systems that worked and performed"; the unit's paraphrase is faithful (unsure list item): https://www.bogieland.com/specials/wurman_interview.html
- Wurman, Information Architects, Graphis Inc., New York, 1997. Resmini and Rosati's text also gives 1997; their reference list gives 1996: https://vufind.katalog.k.utb.cz/Record/6144/Details
- Polar Bear book, 2nd ed., August 2002 (unsure list item): https://www.oreilly.com/library/view/information-architecture-for/0596000359 ; 3rd ed., November 2006: https://www.oreilly.com/library/view/information-architecture-for/0596527349
- Brown, Communicating Design, 2nd ed.: chs 3 to 7 are Personas, Concept Models, Site Maps, Flowcharts and Wireframes. The ch. 5 site-map definition and "one view of how the site will be constructed" are verbatim: https://oreilly.com/library/view/communicating-design-developing/9780131385399/ch05.html
- Tankala, "Information Architecture vs. Sitemaps", NN/g, 3 Sep 2023: "The IA comes first, the sitemap follows", and sitemaps are "intentionally designed to include only the details that stakeholders need to know": https://www.nngroup.com/articles/information-architecture-sitemaps/
- Resmini and Rosati, Pervasive Information Architecture: Designing Cross-Channel User Experiences, Morgan Kaufmann, 2011: https://shop.elsevier.com/books/pervasive-information-architecture/resmini/978-0-12-382094-5

## (6) Errata applied

Nothing to check: the course has had no audit, so there are no errata, and no other unit of the course is filed, so there are no pointers to check.

## (7) Figures

1. Tree, section 1.1. **PASS.**
   - Labels traced to lines 29 to 32: "Organisation system: how content is grouped", "Labelling system: what each group and item is called", "Navigation system: how people browse and move", "Search system: how people query and read results".
   - The caption says what the figure shows and names section 1.1 and the source (Rosenfeld, Morville and Arango 2015, Part II, chs 6 to 9).
   - The kind fits: a hierarchy.
2. Matrix, section 1.4. **FIX, in the text only; the JSON and caption stay unchanged.**
   - Labels traced: the column heads "Web as software interface" and "Web as hypertext system" (line 66); "Sensory design", "Interface Design, Navigation Design, and Information Design", "Interaction Design and Information Architecture", "Functional Specifications and Content Requirements" and "Product Objectives and User Needs" (line 64).
   - The caption names the section and both sources, and the kind fits: items by sections.
   - The column placings of functional specifications, content requirements and information design are not in the text. The fix is the section 1.4 addition in the findings.
3. Timeline, section 3. **PASS.**
   - Dates and labels traced to lines 119 and 121: "a 1964 IBM paper on the System/360", "in 1970 a group at Xerox PARC", "Wurman's address at the American Institute of Architects conference of 1976", "teaching early courses on the internet by 1994", "(O'Reilly, 1998)", "Pervasive Information Architecture ... (Morgan Kaufmann, 2011)", "the fourth (2015) ... For the Web and Beyond".
   - The caption names the section and the sources.
   - The kind fits: dated events.
4. Matrix, section 5. **PASS.**
   - Labels traced to lines 153 to 156: "A buyer at a prospective client ... uses perqo.com", "They reach Admin through Sign in on perqo.com", "through the same sign-in", "They meet perqo.com only for help articles and the link to download the app".
   - The caption says what the figure shows, names section 5 and says Perqo is fictional.
   - The kind fits: items by sections.
5. Swimlanes, section 5. **PASS.**
   - Labels traced to line 196: "A buyer books a demo on perqo.com; once the client has signed, its finance manager sets budgets and its HR manager sets policies in Admin; HR invites employees; an employee opens the app and sees a balance; the employee submits a claim; the claim queues in Admin's Approvals for HR; finance reads the resulting spend in Reports". Also "approve claims" (line 154) and "A signed contract" (line 258).
   - The caption names section 5 and says Perqo is fictional.
   - The kind fits: a journey across surfaces.
6. Objects, Deliverable. **PASS.**
   - Labels traced:
     - "Product, Pricing, Customers, Help centre" (line 173)
     - "Sign in on perqo.com" (line 154)
     - "Employees, Budgets, Policies, Approvals, Reports and Settings" (line 175)
     - "Home (the balance), Benefits, Claims, Card and Account" (line 177)
     - actions from lines 153 to 156 and the surfaces table (lines 248 to 250)
     - links from the crossings table, lines 258 to 260: "A signed contract; HR and finance sign in", "Download link; help articles for employees", "Budgets (as balances), policies ..., invitations, approval decisions"
   - The caption says what the figure shows, names the deliverable and section 5, and says Perqo is fictional.
   - The kind fits: things and relationships.

IA1 · verdict keep · 0 error, 4 should-fix, 7 minor
