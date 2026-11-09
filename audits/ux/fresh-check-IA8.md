---
audit: fresh check
unit: IA8 · Level 4 · the system map
course: ux · IA · Information Architecture
model: Fable 5.1 (claude-fable-5-1, confirmed from the agent's transcript; live search; no Fable 5.1 fresh check is owed for IA8)
date: 2026-11-09
chat: own Fable 5.1 agent context, not shown the writing (P31), launched by the U-8 chat (Opus 5.5 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgQxpizuvqmnHSUNA1hQ
verdict: fix · 1 error, 3 should-fix, 9 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). The harness refused the checker's write of its own `out/report.md`, so the hand-back is the one copy. The maintainer's note follows the report.

# Fresh check · IA8 · Level 4 · the system map

**Model.** Running as Fable 5.1 (claude-fable-5-1). No Fable 5.1 fresh check is owed for IA8: this is it.

**Integrity.** `diff unit.md unit-readonly.md` printed nothing (identical). `sha256sum unit.md` printed `2290d64950859e587f27b6fcffc672c9e5f5b4345dd99e532abab37d8b17fd45`; unit.sha256 holds the same hash. The unit is 615 lines; read in full. `python3 render.py unit.md` printed `8 figures, 0 with problems` (fig 1 swimlanes, 2 swimlanes, 3 decision, 4 decision, 5 decision, 6 objects, 7 matrix, 8 objects; no undocumented keys). The write of out/report.md was refused by the harness; this reply is the one copy.

**Scripts run.** (a) IDs by regex over the prose: X-01 to X-13 = 13 rows; J-01 to J-14 = 14 rows; CL-1 to CL-6 = 6; EL-1 to EL-6 = 6; G-1 to G-7 = 7; three DT headers; "(Perqo, fictional)" appears 22 times, first at line 12. (b) The 104 count: IA6's `A-` IDs = 23, IA7's `AD-` IDs = 29 (regex over the vault files), IA5 A.4 says 52 rows after the redesign; 52 + 23 + 29 = 104. (c) The three decision tables under the Unique hit policy: enumerated every yes/no combination (DT-1 16, DT-2 16, DT-3 8); each combination matches exactly one row in all three. (d) Word count excluding viz blocks 12,216, of which table words 3,451, prose 8,765 (IA6 14,807 and IA7 14,871 by the same script). (e) Every Current below was checked with Python `str.count` on unit.md and occurs exactly once.

## (1) Coverage against the brief

- Why a system needs a map above the surface maps; shared understanding, gap-finding, scope decisions: covered (§1, with G-1 to G-7).
- Pervasive and cross-channel IA (Resmini and Rosati's heuristics): covered, thin by design (§2.1: chapter names plus one heuristic's definition quoted through Fisher, Norris and Buie; the thinness is stated and on the unsure list).
- Service blueprint (Shostack's origin; Kalbach; NN/g definition): covered (§2.2; Shostack thin, only the article's existence, stated as such).
- Client company's purchase lifecycle (evaluate, trial, contract, onboard, run, renew or churn): covered (§3.2, CL-1 to CL-6, figure 1).
- Employee's benefit lifecycle (enrol, learn, decide, spend, claim, review): covered (§3.3, EL-1 to EL-6, figure 2).
- Published models of the purchase decision journey named and evidence labelled: covered (§3.1: Lavidge and Steiner; Court and others; Gartner; each labelled).
- Decision trees for eligibility, approval routing, spend limits; drawn so engineering can implement and sales can explain: covered (§4.1 to §4.4, figures 3 to 5, tables and the words for sales in D.3).
- Layering, read one layer at a time, what to leave out: covered (§5.1, §5.2).
- How the map stays current: covered (§6).
- Figures asked: lifecycle swimlanes (1, 2), three decision trees (3 to 5), product map across surfaces (6), layered interaction map as layers and as the whole (7, 8): covered; eight figures, within three to eight.
- Deliverable: surface layer (D.1), actor and lifecycle layer (D.2), decision-tree layer (D.3), connections (D.4), reading guide one paragraph per layer (D.5, four paragraphs for four layers): present in full.
- Takes line: IA5 to IA7's IAs and IA2's blueprint and map entries: used throughout.
- Questions handed to IA8 by name (grep of vault/ and the register for "IA8"): IA7's invitation to E-2, claim lifecycle to Claims and the tree, labels across surfaces, leaver, Budget as model name, model boundaries: all answered (D.1, D.3, D.4, §3.4). IA6's external routes, E-2, E-3, claim states, Purchase to the category rule, declined attempt: all answered (X-03 to X-06, J-03, J-06, §4.5). IA5's S-5, S-6 and external routes: answered (X-01 to X-03, X-05). IA4's status attribute and auto-approve limit joins: answered (J-01, J-02). IA2's decision-table rows marked IA8: answered. Register's "Not yet set" purchase lifecycle and enrolment: answered (§3.2, §3.3). No coverage gap.

## Findings

[error] [attribution] §1 · Current: `ch. 2; IA1, section 3)` · Problem: IA1 quotes the Polar Bear book's "digital, physical, and cross-channel ecosystems" definition in its section 1.1 (the four definitions of chapter 2), not in section 3; IA1's section 3 (lines 115 to 136) does not carry it. The pointer sends the reader to the wrong section. · Fix: `ch. 2; IA1, section 1.1)` · Basis: vault/IA1-what-information-architecture-is-and-where-it-sits.md, line 21 (section 1.1), definition 2.

[should-fix] [attribution] §6 · Current: `the map's face carries its version and date for the same reason (IA1, section 4)` · Problem: IA1's section 4 sets that a deliverable states its decision, its readers and what it leaves out; version and date are IA2's (the "Re-stamp the face" rule in section 4 and the "Owner, version, date" row of the notation sheet's face table). · Fix: `the map's face carries its version and date for the same reason (IA2, section 4 and the notation sheet)` · Basis: vault/IA2-…notation.md line 180 ("Re-stamp the face. Update the version, the date, the owner…") and line 413 ("Owner, version, date | who keeps it, and when it was last true"); vault/IA1 lines 137 to 148 contain no "version" or "date".

[should-fix] [style] §5.1 · Current: `as its layers (figures 1 to 6 of this unit)` · Problem: the connections are the fourth layer (table in §5.1) and are drawn as figure 7, the matrix; "figures 1 to 6" leaves the connections layer out of the "layers" drawing and makes the sentence's "drawn twice" false for that layer. · Fix: `as its layers (figures 1 to 7 of this unit)` · Basis: the unit's own §5.1 table (four rows, the fourth "Connections … matrix") and the figure order from render.py (fig 7 matrix, fig 8 objects).

[should-fix] [attribution] Header · Current: `search: off` · Problem: the body states that live search was run ("checked 9 November 2026" on the Camunda source; the unsure list's "from knowledge and search-result titles"), so the flag contradicts the unit; Part 1 ties the dating duty and the six-month staleness check to this flag. · Fix: `search: on` · Basis: unit.md lines 588 and 605; sourcing-part1.md "Per unit", second item.

[minor] [attribution] Sources · Current: `- Fisher, J., S. Norris and E. Buie.` · Problem: the paper's PDF gives the full names, so the unsure-list item is now closable. · Fix: `- Fisher, Jon, Simon Norris and Elizabeth Buie.` · Basis: https://journalofia.org/volume4/issue2/02-fisher/jofia-0402-02-fisher.pdf (title page: Jon Fisher, Simon Norris, Elizabeth Buie).

[minor] [attribution] §2.1 · Current: `J. Fisher, S. Norris and E. Buie quote` · Problem: as above. · Fix: `Jon Fisher, Simon Norris and Elizabeth Buie quote` · Basis: same PDF.

[minor] [attribution] Unsure list · Current: `- Fisher, Norris and Buie 2012: authors' first names not seen (initials only); peer review of the Journal of Information Architecture from knowledge.` · Problem: both points are now checked: the PDF gives the names and the journal's About page says "The Journal of Information Architecture is a peer-reviewed scholarly journal." · Fix: `- Fisher, Norris and Buie 2012: the journal's About page calls it "a peer-reviewed scholarly journal" (checked 9 November 2026).` · Basis: https://journalofia.org/about.

[minor] [attribution] Sources · Current: `*Journal of Marketing*, 1961 (not read; see the unsure list).` · Problem: the volume, issue and month are available from a library record; the unsure list says they were not seen. · Fix: `*Journal of Marketing* 25, no. 6 (October 1961) (the article not read; see the unsure list).` · Basis: https://archives.uah.edu/repositories/2/archival_objects/63052 (The Journal of Marketing, vol. 25, no. 6, 1961-10). Pages 59 to 62 appear in a search-result title only (scirp.org reference list) and were not fetched; not added.

[minor] [attribution] Unsure list · Current: `- Lavidge and Steiner 1961: title, journal and year from knowledge and search-result titles; the article, its volume, pages and its exact steps were not read.` · Problem: volume and issue now seen. · Fix: `- Lavidge and Steiner 1961: title, journal, volume, issue and month from a library record (archives.uah.edu); the article, its pages and its exact steps were not read.` · Basis: as above.

[minor] [style] §2.2 and Sources · Current: `5 November 2017, [nngroup.com, mapping cheat sheet](https://nngroup.com/articles/ux-mapping-cheat-sheet))` · Problem: the only NN/g link in the unit without `www.` and the trailing slash; the article's canonical address is https://www.nngroup.com/articles/ux-mapping-cheat-sheet/ and the bibliography collects links as printed. · Fix: `5 November 2017, [nngroup.com, mapping cheat sheet](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/))` · Basis: WebSearch result URL and the fetched page. Apply the same to the Sources row: Current `5 November 2017. [nngroup.com, mapping cheat sheet](https://nngroup.com/articles/ux-mapping-cheat-sheet)` → Fix `5 November 2017. [nngroup.com, mapping cheat sheet](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/)`.

[minor] [style] §1 and Sources · Current: `insight" ([oreilly.com, Mapping Experiences](https://oreilly.com/library/view/mapping-experiences-2nd/9781492076629))` · Problem: the page's address is https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/ (with www and trailing slash); the printed form was not fetched. · Fix: `insight" ([oreilly.com, Mapping Experiences](https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/))` · Basis: WebSearch result URL and the fetched page. Same in Sources: Current `description). [oreilly.com, Mapping Experiences](https://oreilly.com/library/view/mapping-experiences-2nd/9781492076629)` → Fix `description). [oreilly.com, Mapping Experiences](https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/)`.

[minor] [style] End of file · Current: `
Object: the Perqo interaction map, Deliverable (D.1 to D.5) and section 5` · Problem: a stray line after the unsure list, in no filed unit's format (grep "^Object:" over vault/ finds none); it reads as a packet or build note left in the unit. · Fix: `` (delete the line) · Basis: vault/IA5 to IA7 end on their unsure lists and fresh-check notes.

[minor] [coverage] Whole unit · Current: (no single sentence) · Problem: the brief's length band is 2,000 to 6,000 words; the unit's prose is 8,765 words (12,216 with tables). Not padded: every section does work the brief asks for. Recorded, no fix; IA6 (14,807) and IA7 (14,871) were filed at greater length. · Basis: word count script above.

## (2) Accuracy

PASS · Gibbons, "Service Blueprints: Definition", NN/g, 27 August 2017 (page says published August 27, 2017): "bridges crossdepartment efforts"; "treasure maps that help businesses discover weaknesses"; "A service blueprint is a diagram that visualizes the relationships between different service components"; "directly tied to touchpoints in a specific customer journey"; clusters customer actions, frontstage actions, backstage actions, processes, evidence; lines of interaction, visibility, internal interaction; root causes inside the organisation ("the root cause of a systemic issue", "overlaps and dependencies that departments alone could not see"). All exact. https://www.nngroup.com/articles/service-blueprints-definition/
PASS · Gibbons, "UX Mapping Methods Compared: A Cheat Sheet", NN/g, 5 November 2017: "Think of service blueprints as a part two to customer journey maps."; "Blueprinting is an ideal approach to experiences that are omnichannel, involve multiple touchpoints, or require a crossfunctional effort." https://www.nngroup.com/articles/ux-mapping-cheat-sheet/
PASS · Gibbons, "The 5 Steps to Service Blueprinting", NN/g, 4 February 2018: step 5 "Refine and distribute"; adds timing, metrics; "distributed amongst clients and stakeholders". https://www.nngroup.com/articles/5-steps-service-blueprinting/
PASS · Kalbach, Mapping Experiences, 2nd ed., O'Reilly, 2020: Part 3 "Primary Diagram Types in Detail", ch. 10 Service Blueprints, 11 Customer Journey Maps, 12 Experience Maps, 13 Mental Model Diagrams, 14 Ecosystem Models; publisher's description "use alignment diagrams to turn valuable customer observations into actionable insight". https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/me2_toc.xhtml and https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/
PASS · Resmini and Rosati 2011 contents: Part 2 ch. 3 Heuristics for a Pervasive IA, 4 Place-making, 5 Consistency, 6 Resilience, 7 Reduction, 8 Correlation; Part 3 ch. 9 Designing Cross-channel User Experiences. https://shop.elsevier.com/books/pervasive-information-architecture/resmini/978-0-12-382094-5
PASS · Fisher, Norris and Buie, "Sense-making in Cross-channel Design", JoIA 4(2), Fall 2012, pp. 5 to 32: the four quoted passages are present and presented as Resmini and Rosati's; internal and external correlation distinguished as the unit says. https://journalofia.org/volume4/issue2/02-fisher/jofia-0402-02-fisher.pdf
PASS · Journal of Information Architecture peer-reviewed: "a peer-reviewed scholarly journal". https://journalofia.org/about
PASS · Shostack, "Designing Services That Deliver", HBR, January 1984: listed in the January 1984 issue table of contents at /1984/01/designing-services-that-deliver. https://hbr.org/archive-toc/3841 (the article page itself not fetched; the unit claims nothing from its text).
PASS · Bitner, Ostrom and Morgan, "Service Blueprinting: A Practical Technique for Service Innovation", California Management Review 50(3), 2008, pp. 66 to 94: abstract has "securely grounded in the customer's experience" and "clear visualization of dynamic service processes"; CMR's issue page lists the authors as Ostrom, Bitner, Morgan, as the unit's unsure list says; ASU's record lists Bitner, Ostrom, Morgan. https://asu.elsevierpure.com/en/publications/service-blueprinting-a-practical-technique-for-service-innovation/ and https://cmr.berkeley.edu/browse/issues/50_3/ (sagepub page refused: not checked).
PASS · Court, Elzinga, Mulder and Vetvik, "The consumer decision journey", McKinsey Quarterly 2009 no. 3: "almost 20,000 consumers across five industries and three continents"; automobile, skin care, insurance, consumer electronics, mobile telecom; "initial consideration"; "active evaluation, or the process of researching potential purchases"; "closure, when consumers buy brands"; "postpurchase, when consumers experience them"; "The funnel metaphor does help a good deal". Checked at the search-returned .ashx address of the same path; the unit's printed .pdf form was not fetched (rule), so the printed URL itself is unverified. https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/Marketing%20and%20Sales/Our%20Insights/The%20consumer%20decision%20journey/The%20consumer%20decision%20journey.ashx
PASS · Gartner press release, 9 October 2018: six buying jobs "Problem Identification", "Solution Exploration", "Requirements Building", "Supplier Selection", "Validation", "Consensus Creation"; "resembles more of a maze than a linear path"; no survey figures or method given. Checked through a reproduction (salestechstar.com, dated 10 October 2018 for the repost) and the Business Wire listing dated 2018-10-09; the gartner.com page was not returned by search and not fetched. https://salestechstar.com/sales-marketing/gartner-says-the-marketing-to-sales-handoff-should-no-longer-exist/
PASS · OMG, DMN 1.5, August 2024: "The primary goal of DMN is to provide a common notation that is readily understandable by all business users, from the business analysts needing to create initial decision requirements and then more detailed decision models, to the technical developers responsible for automating the decisions in processes, and finally, to the businesspeople who will manage and monitor those decisions." Exact, including "businesspeople". https://www.omg.org/spec/DMN/1.5/About-DMN
PASS · Camunda, "Hit policy": "A decision table has a hit policy that specifies what the results of the evaluation of a decision table consist of."; Unique: "Only a single rule can be satisfied or no rule at all."; page undated. https://docs.camunda.io/docs/components/modeler/dmn/decision-table-hit-policy/
PASS · Tufte, Envisioning Information, Graphics Press, 1990 (copyright), ch. 3 "Layering and separation" (chapters 1 to 7 as listed). https://search.centrecountylibrary.org/Record/284250/TOC and https://toc.uni.li/FLMF019103.pdf
unverifiable · Lavidge and Steiner 1961: bibliographic record confirms title, journal, vol. 25 no. 6, October 1961 (https://archives.uah.edu/repositories/2/archival_objects/63052); the content claim (ordered steps, conceptual model) could not be checked (semanticscholar and colab.ws pages refused). The unit labels it "on this unit's knowledge" and "not read": correctly labelled.
PASS · Rosenfeld, Morville and Arango 2015 ch. 2 "digital, physical, and cross-channel ecosystems": in IA1, section 1.1 (pointer finding above).
PASS · IA2 quotations and rules: "when the system (not based on user action) must select one path" (IA2 §1.7); "holds the top level of each surface and nothing below; the sitemaps hold the rest" (§1.10); "split rather than cram", "Keep the notation; extend the legend" (§4); "every outcome is named as the screen names it" (§1.7, Fidelity); "capturing your past decisions and guiding your future ones" (§4); Brown "a process, usually centered around a specific task or function" (§2.2); blueprint "as lifecycle swimlanes" (decision table, line 434); tones 1 to 6 as the unit states them (§5.2).
PASS · The 104 count (52 + 23 + 29) by script.
PASS · "IA7's 29 page IDs", "IA6's 23 screen IDs" by script.

## (3) Figures (numbers)

Every number says whose it is: 104 and its parts (IA5, IA6, IA7); "almost 20,000 consumers" (the article's own statement, labelled consultancy, not peer-reviewed); "five industries and three continents" (same); seven gaps, two already named (this unit's drawing); "five working days", "14 days" (IA7); 1,200 employees etc. not repeated. No bare number found.

## (4) Labels

Anecdote: none used. Vendor: Gartner labelled "analyst firm's press release … vendor material"; Camunda "vendor documentation"; OMG "standards documentation"; McKinsey "a consultancy's study … not peer-reviewed"; NN/g "NN/g guidance"; Kalbach "a standard work's practice"; "none of it is a measured comparison" (§2.2); "The rest of the list is this course's practice" (§4.1); "the method below is this course's practice" (§5.1); "Perqo practice" (§6). Correlational data: none claimed. All labelled.

## (5) Deliverable

Present in full (D.1 crossings table 13 rows, shared-objects table 8 rows, two model decisions, figure 6; D.2 actors and five lifecycles; D.3 three tables passing the Unique check and the words for sales; D.4 fourteen J- rows, matrix, whole map; D.5 four paragraphs). It follows from the evidence: every row cites a filed identifier or a section of this unit, and the trees are IA2's and IA7's extended by the unit's own labelled decisions. Usable alone: a reader with D.1 to D.5 can place a change, a label, a rule and an actor without the body. The face carries fidelity, decision, readers, leaves-out, owner, version, date, and "Perqo is fictional".

## (6) Errata applied; pointers

No audit report yet for this course: skipped. Pointers to filed units: every pointer listed under Confirmed below was opened and says what the unit says, except the two pointer findings above (IA1 section 3; IA1 section 4 for version and date). Perqo facts: nothing contradicts or renames a registered fact; new facts (contract end date, churn, onboarding order, invite condition, card Cancelled, allocation closed, "not set yet" state, O-18, R-25, declines, decline notice, CL-, EL-, DT-, J-, X-, G- series, review cadence) are each labelled and fall in the register's free list (purchase lifecycle, enrolment, leaver's allocations and card, IA8's declined-attempt decision, when cards are issued). O-18 and R-25 are the next free identifiers after IA7's O-17 and R-24. Tone 5 for Perqo staff is declared as an extension under IA2 §4. Public-site rules: no personal fact, no private person, no real client; link texts are short (a domain and two or three words).

## (7) Figures

Figure 1 · swimlanes · §3.2. Lanes and steps traced: "Buyer on perqo.com", "Perqo staff: sales and setup", "Client's admin users in Perqo Admin", "Employees in the Perqo app" (line 112); CL-1 to CL-6 and their notes "S-1 to S-3", "S-4; no free trial", "first admin user", "admins, groups, policies, budgets, then invites", "each period: budgets, approvals, reports", "new contract end date", "[after the contract end date] sign-in ends, cards cancelled", "redirect to S-3" (table lines 101 to 106, lines 108, 110); "→ see EL-1" is IA2's continuation note; "[renewed]" and "[not renewed]" are IA2's bracketed conditions for "A renewal sets a new end date. At churn…" (line 108). Not traced: step label "Demo and follow-up" and its note "outside the surfaces": the prose says "the demo itself is outside the surfaces" (line 102) and never "follow-up". Caption names the figure, the section, the sources and the tones (1, 5, 4, 3, 6) and tone 6 is named in the text (line 112). Kind fits (a journey across actors). **FIX** (minor): Current `the demo itself is outside the surfaces` → Fix `the demo itself and sales' follow-up are outside the surfaces (IA4, A.3: demo request -> follow up)`; basis vault/IA4 A.3 line 297 ("demo request | -> follow up *new* | sales | outside Perqo's surfaces").

Figure 2 · swimlanes · §3.3. Traced: all five lanes (line 158 names the Help centre tone 1, the merchant tone 2, the Perqo system tone 5, HR and finance in Admin tone 4, the employee tone 3); "HR invites" / "AD-1.3 [budgets set]" (lines 110, 151); "EL-1 Enrol: Join" / "A-0.1; Active; card ordered" (151, 158); "EL-2 Learn" / "A-1, A-2.1 to A-2.4" (152); "EL-3 Decide" / "card or claim; Card offers A-4.3" (153); "EL-4 Spend: pay" / "Perqo card" (154); "DT-2 approval routing" (214); "HR decides" / "AD-4 [over the limit]" (155, 248); "Purchase, or decline notice" / "A-4.2.1; A-5.2" (158, 289); "EL-6 Review" / "A-3, A-4.2, A-5.2" (156); "Finance sets next period" / "AD-2.2" (156, 350); links "invitation, E-2", "external route", "Submit", "[over the limit]", "notification, E-4" (151, 152, 248, 208). Not traced: (a) step label "What you can claim": the article's title "What you can claim in each category" appears nowhere in the unit, only its ID H-2.1.3 (line 152); (b) step label "DT-3 spend check": the unit calls DT-3 "spend limits" everywhere (214, 263, 449) and "spend check" nowhere; (c) note "A-3.1 to A-3.3" on EL-5 while the EL-5 table row says "A-3.1 to A-3.4" (line 155). Caption names figure, section, sources, tones; no tone 6 drawn. Kind fits. **FIX**: (a) prose, Current `| EL-2 | Learn | the app (A-1, A-2.1 to A-2.4); the Help centre (H-2.1.3, H-2.2.1) |` → Fix `| EL-2 | Learn | the app (A-1, A-2.1 to A-2.4); the Help centre (What you can claim in each category, H-2.1.3; H-2.2.1) |` and figure, Current `{"id": "help", "lane": "help", "col": 3, "label": "What you can claim", "note": "H-2.1.3", "tone": 1}` → Fix `{"id": "help", "lane": "help", "col": 3, "label": "What you can claim in each category", "note": "H-2.1.3", "tone": 1}`; basis vault/IA5 A.3 (H-2.1.3 "What you can claim in each category"). (b) Current `{"id": "dt3", "lane": "sys", "col": 6, "label": "DT-3 spend check", "tone": 5}` → Fix `{"id": "dt3", "lane": "sys", "col": 6, "label": "DT-3 spend limits", "tone": 5}`; basis unit line 214. (c) Current `{"id": "claim", "lane": "app", "col": 8, "label": "EL-5 Claim", "note": "A-3.1 to A-3.3", "tone": 3}` → Fix `{"id": "claim", "lane": "app", "col": 8, "label": "EL-5 Claim", "note": "A-3.1 to A-3.4", "tone": 3}`; basis unit line 155.

Figure 3 · decision · §4.2 (DT-1). Every question and outcome traced to line 231 and the D.3 table rows 1 to 5 (431 to 435): "Client's contract in force?", "Employee Active?", "Category open in the group's policy?", "Allocation set for this period?", "Eligible: card and claims in this category", "Shown: budget for this period not set yet" ("Your budget for this period is not set yet", 231), "Category not shown; card declined there", "Invited: join first. Left: cannot sign in", "Sign-in ended; cards cancelled". Caption names section, sources, tones 5 and 6; tone 6 named in text (231). "yes" on the left. Kind fits (a rule with branches). **PASS**.

Figure 4 · decision · §4.3 (DT-2). Traced to lines 248 and 441 to 445: all five questions and outcomes with T1 to T5 and the app's reasons; tone 4 for HR's question named (248); tone 6 named (248). Extends IA2 §5.3's tree without changing its questions (confirmed against IA2 line 276) and adds IA7's EX-1 and T5 (confirmed, IA7 D.1, D.2). Kind fits. **PASS**.

Figure 5 · decision · §4.4 (DT-3). Traced to lines 265, 282 and 453 to 456; "Declined: card Frozen (notice sent) or Cancelled" matches "every decline triggers the notice … except on a Cancelled card" (265). Tones named (265). Kind fits. **PASS**.

Figure 6 · objects · D.1 (surface layer). Traced: the four surfaces' top levels (line 338; IA5 B, IA7 C, IA6 B); "Sign in (S-5)", "Get the Perqo app (S-6)" (344 to 346); the five shared objects' "Surface: Label" lines (table 362 to 366); link labels "X-01 Sign in", "X-03 download; X-05, X-06 help", "X-04 invites; X-07; X-09 decisions" (344 to 352); "the till", "offers" (338, 353). Not traced to the unit's text: the relationship verbs and counts between the shared objects ("is checked against" 0..* to 1, "spends from" 0..* to 1 twice, "is used for" 1 to 0..*, "takes" 1 to 0..*), the surface-to-object verbs ("sets", "decides [over the limit]", "submits", "shows as Balance", "shows; freezes") and the surfaces' actions ("-> evaluate (CL-1)", "-> find help", "-> configure", "-> decide claims", "-> report", "-> see balance", "-> claim", "-> freeze card", "-> take card payment"): the prose at line 376 names only the surfaces, the five objects and the X- labels. They are IA4's R-09, R-10, R-12, R-13, R-14 and IA2 §5.3's lines, but the P41 rule needs them in this unit's text. Caption names the figure, D.1, sources, tones; no tone 6. Kind fits (things and relationships). **FIX** (should-fix): prose, Current `and the main crossings labelled by their X- identifiers.` → Fix `and the main crossings labelled by their X- identifiers. The lines between the shared objects carry IA4's relationships with their counts: a claim is checked against one policy (R-09) and spends from one allocation (R-10), a card is used for card payments (R-12), a card payment spends from one allocation (R-13) and a merchant takes card payments (R-14) (IA4, A.2); the surface-to-object lines keep IA2's verbs, Admin sets the policy and decides claims over the limit, the app submits claims, shows the allocation as Balance and shows and freezes the card (IA2, section 5.3), and each surface box lists its actions as IA4's calls to action name them: perqo.com -> evaluate (CL-1) and -> find help; Admin -> configure, -> decide claims and -> report; the app -> see balance, -> claim and -> freeze card; the merchant side -> take card payment (IA4, A.3).`; basis vault/IA4 A.2 rows R-09, R-10, R-12, R-13, R-14 (lines 255 to 260) and A.3; vault/IA2 line 327.

Figure 7 · matrix · D.4. Every cell traced to the J- table (lines 464 to 477), shortened but with the same words ("DT-1, Active" for "DT-1, Employee Active"; "HR's question; recheck" for "DT-2, HR's question and the recheck"; "AD-2.2, queue" for "Set budgets (AD-2.2); No budget for next period", "queue" at line 231). Row labels "J-01 status" … "J-14 budgets" are the ID and the short name of the table's second column, two words each; the drawing is 639.7 units (viz-fit), three columns of 156 to 173 units, so cells keep room on a phone; blank cells are the two "none" cells (J-11, J-12). Caption names D.4, the layers' source, tone 5 and why. Kind fits (items by sections). **PASS**.

Figure 8 · objects · D.4 (the whole). Traced: the four surfaces (338); "surface layer", "lifecycle layer", "decision layer" (§5.1 table); "AD-0 to AD-6" (IA7 C.1), "A-0 to A-5" (IA6 B), "the till"; "CL-1 to CL-6", "EL-1 to EL-6", "Submitted, Approved, Rejected, Paid" (199); "DT-1 eligibility", "DT-2 approval routing", "DT-3 spend limits" (214); "→ see figure n" and "→ see IA7, D" continuation notes; link labels J-12, J-10, J-14, J-04, J-03, J-05, J-08, J-06, J-07, J-01, J-02, J-09 (D.4 table). Not traced and not right: the perqo.com box's "S-1 to S-6; H-": IA5's site pages run S-0 to S-12 (plus L- campaign pages), and the unit's own D.1 cites S-4, S-5, S-6 and S-3.x; "S-1 to S-6" understates the surface and names a range the unit never states. Caption names D.4, the layers, the tones; no tone 6. Kind fits. **FIX** (error): Current `{"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["surface layer", "S-1 to S-6; H-", "→ see figure 6"]}` → Fix `{"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["surface layer", "S-0 to S-12; L-; H-", "→ see figure 6"]}`; basis vault/IA5 A.1 (S-0 Home to S-12 Cookie policy, lines 261 to 288), A.2 (L-01, L-02), A.3 (H-).

Figure count: 8 figures; 4 PASS (3, 4, 5, 7); 4 FIX (1 minor, 2 should-fix with one minor part, 6 should-fix, 8 error), each with its exact replacement above. Following the course's filed checks (IA5 to IA7 footers), figure FIXes are counted separately from the unit's severity counts below.

## Confirmed (claims checked and found right)

- IA2 §1.10's question and "holds the top level of each surface and nothing below": vault/IA2 lines 131, 137.
- IA2 §1.7 Garrett "when the system (not based on user action) must select one path"; F3 "every outcome is named as the screen names it"; a person's decision as "one question box in the person's tone": vault/IA2 lines 103 to 107.
- IA2 §1.9 Gibbons's clusters and three lines; Shostack 1984; Kalbach ch. 10: vault/IA2 line 123.
- IA2 §4 rules "Keep identifiers stable", "Mark changes as proposed", "Rename through the vocabulary", "Split rather than cram", "Keep the notation; extend the legend", "capturing your past decisions and guiding your future ones" (RMA ch. 13): lines 173 to 180.
- IA2 §5.2 tones 1 to 6 exactly as the unit's line 14 states them; "yes always on the left"; "Surface: Label"; "→ see"; "[condition]": lines 206, 209, 219.
- IA2 §5.3 decision tree's questions and outcomes (line 276) unchanged in DT-2; blueprint "as lifecycle swimlanes" and cross-surface map rows marked IA8 (lines 432 to 435).
- IA2 §2.2 Brown ch. 6 "Flowcharts visualize a process, usually centered around a specific task or function": line 153.
- IA1 §2.4 one table of transactions with a type field, allocation per category per period; Budget/Balance: line 111. IA1 §1.3 Arango chapters Sustainability, Gardening: line 60. IA1 Deliverable's decision "on which surface, and under which name, a new piece of content or function belongs": line 272. IA1 §4 "every IA deliverable states, on its face, the decision it supports and who is meant to read it"; Tankala on leaving detail out: lines 143, 147.
- IA3 §2.3 the rule reads one category's balance (register line 72); IA3 D2 one thing one label (vault/IA3 line 283).
- IA4 A.1: O-01 client with contract start date; O-04 policy open categories, auto-approve limit; O-06 allocation category, period; O-07 claim status; O-08 card payment; O-09 card Active, Frozen; O-10 notification "the claim it is about"; O-11 merchant one narrower term; O-14 to O-16: lines 224 to 239. A.2 R-07, R-09, R-10, R-12 to R-20: lines 247 to 266. A.3 freeze and unfreeze by the employee; demo request -> follow up by sales outside the surfaces: lines 290, 297. §4.3 "Rules and lifecycles sit outside it … joined to the map in IA8": line 195. "What the map hands on": line 367.
- IA5 §5.5 no self-serve sign-up, no free trial, a client starts after a contract; S-6 Get the Perqo app with download links, employees do not sign in on perqo.com: lines 228 to 230 and register. S-5 external, S-6, S-3.4 removed with redirect to S-3, S-4 Book a demo: A.1 lines 279 to 283. H-2.1 to H-2.3.2 IDs and titles used in X-05 and X-06: A.3 lines 300 to 326. A.4: 42 today, 52 after, 57 rows: line 342. "What the inventory hands on" and "What the catalogue hands on": lines 349, 515. Footer page Get the Perqo app: B.1 line 393.
- IA6 B.3 external routes A-1→H-2.2.1, A-2.x→H-2.1.3, A-3→H-2.1, A-3.1→H-1.2.5, A-3.4→H-2.1.2, A-4→H-2.3.1, H-2.3.2, A-5→H-2; B.5 used-up category→H-2.2.2: lines 390 to 470. B.4 E-1 to E-7 as cited in X-03, X-04, X-06, X-09: lines 448 to 454. C.2 declines over the balance or Frozen, nothing in the app, proposed for IA8: line 525. §4.3 Neusesser and Sunwall 2023: line 183. §4.4 closed category not shown, cross-listings and offers hidden; card not issued state; notifications asked once after the first claim: lines 195 to 202. §6.1 Resmini and Rosati chapters and IA1's label rule: lines 244, 246. A.2 open-question cell "should a declined attempt be shown? (IA8)": line 333. Facts row and assumption row quoted in §4.5: lines 612, 592. "What IA8 and IA11 take": line 576. Reason "over the balance, or by HR"; "More than your Learning balance": register lines 131, 133.
- IA7 §2.3 Perqo card status only, Active, Frozen, Not issued; notification not shown in Admin: lines 85 to 90. §3.2 an action a role holds but cannot take now shown disabled with the reason: line 110. §3.3 at least two HR managers; least privilege: lines 116 to 120. §3.4 account owner set up by Perqo; rest of onboarding free: lines 122 to 128. §4.3 the Approvals wireflow: lines 173 to 176. §5.1 Invited, Active, Left; HR marks left from Invited or Active; leaver's allocations and card left to IA8: line 222. §6.2 Budget question, one bounded context, catalogue and merchant side as candidates at R-07, R-14, R-16, R-17; Evans "a change in the language is a change to the model": lines 268 to 274. C.1 AD-0 to AD-6.4 IDs used (AD-0, AD-1.1, AD-1.1.1, AD-1.3, AD-2.1, AD-2.2, AD-3.1, AD-4, AD-5.3, AD-6.1): lines 476 to 511. C.4 queues Approvals, Not joined, No budget for next period; the invitation: register lines 164, 171. C.5 the sign-in line to S-6: register line 170. D.1 T1 to T6 and D.2 EX-1 to EX-4: lines 582 to 598. "What IA8 and later units take": line 618. O-17 audit entry and R-21 to R-24 (so O-18, R-25 are the next free): register lines 157, 158.
- Register "Not yet set": the purchase lifecycle of a client company; the employee's enrolment beyond IA6's invitation and Join: perqo-facts.md line 176.
- Course units list: IA10 touchpoints built from IA4 to IA8; IA11 validation; IA12 assumption register; DD-IA1 comparison: generator/data/ux/units_data.py lines 67 to 82, 121.

**IA8 · verdict: fix · 1 error, 3 should-fix, 9 minor (unit text); figures: 4 PASS, 4 FIX (figure 8 error, figures 2 and 6 should-fix, figure 1 minor), each with its exact replacement in (7).**

Note for the main session: nothing in this check came from memory, past chats, Projects or connectors; only the packet in /home/claude/u8/c and the web fetches listed above were used. No new fact about the user to remember.

## Maintainer's note (U-8 chat, 9 November 2026)

Every finding was verified before it was applied, as an exact replacement by script (each Current occurring once in the filed unit):
- Finding 1, error (section 1, "IA1, section 3"): held. IA1 quotes the fourth edition's "digital, physical, and cross-channel ecosystems" in section 1.1 (its line 21), and its section 3 does not; applied.
- Finding 2 (section 6, version and date credited to IA1, section 4): held. IA1's section 4 asks for the decision, readers and what is left out; the version and date are IA2's ("Re-stamp the face", section 4; the notation sheet's "Owner, version, date"); applied.
- Finding 3 (section 5.1, "figures 1 to 6"): held; the connections, the fourth row of the section's own table, are figure 7; applied.
- Finding 4 (`search: off` to `search: on`): not applied. The flag is the build order's (`ORDER` and `courses-index.md`: off), and method §4 defines off as writing from knowledge with searches only to verify a specific date, figure or contested point, which is what the writer did (its transcript: 27 searches, each to check a citation). Part 1's dating duty applies to a search-on unit's facts that can change; this unit states none. Recorded.
- Findings 5 to 7 (Fisher, Norris and Buie's names; the journal's peer review): held. The maintainer's own search returned journalofia.org's article page and About page; the article page gives Jon Fisher, Simon Norris and Elizabeth Buie, the About page "a peer-reviewed scholarly journal"; applied. Found in the same check and fixed: the article page gives pp. 5 to 30, and the PDF (search-returned, fetched) prints pages 5 to 30 while its cite-as line says 5 to 32; the unit's two "5 to 32" became "5 to 30" and the unsure line says so.
- Findings 8 and 9 (Lavidge and Steiner's volume and issue): held. The maintainer's search returned a scilit.net record (fetched: Journal of Marketing 25, no. 6, 1 October 1961, starting on page 59); the record the checker cited (archives.uah.edu) was not returned to the maintainer's search and was not fetched; applied, the unsure line naming both records. An econbiz record returned an access-denied page and was not fetched again; a CiNii record returned no body and was not fetched again elsewhere.
- Findings 10 and 11 (the NN/g cheat sheet's and O'Reilly's addresses): held. The checker's transcript shows both canonical forms returned by its searches and fetched with bodies; the maintainer's own searches returned other pages of the same sites, not these, so the canonical forms rest on the checker's fetch, checked by script; applied in text and Sources.
- Finding 12 (the `Object:` line as stray): held in part. The line is required: method §4 and `skills/write-unit` §5 close the unsure list with it, and filing maps the page's relief from it (P96). It sat on its own line after the last item, so Markdown folded it into that item; it is now the list's last item, `- Object: ...`. Not deleted.
- Finding 13 (length over the brief's 2,000 to 6,000 guide): no change asked; none made (method §4, Length rule: the topic decides).

Figures. Figures 3, 4, 5 and 7 passed and their declarations did not change. Applied as verified:
- Figure 1 (minor: "Demo and follow-up" with no "follow-up" in the text): held; IA4, A.3 gives demo request -> follow up by sales outside the surfaces; the table cell now says so; the declaration is unchanged.
- Figure 2 (three labels): held, each; IA5, A.3 gives H-2.1.3 its title "What you can claim in each category"; the EL-2 row and the step label now carry it; "DT-3 spend check" is now "DT-3 spend limits"; the EL-5 note now reads "A-3.1 to A-3.4" as the table does.
- Figure 6 (verbs, counts and actions not in the text): held, and the checker's fix held only in part: its sentence credited the surface boxes' actions to IA4, A.3, which lists actions per object, not per surface. The maintainer kept the checker's relationship sentence (IA4, A.2: R-09, R-10, R-12, R-13, R-14 with their counts, checked line by line) and replaced the actions: each surface box now keeps IA1's actions as IA2 redrew them (perqo.com -> book a demo, -> find help; Admin -> configure, -> approve, -> report; the app -> see balance, -> spend, -> claim; IA1's Deliverable figure and IA2, section 5.3's), the merchant's "-> take card payments" traced to R-14; the prose after the paragraph introducing the figure says each of them.
- Figure 8 (error: "S-1 to S-6"): held; IA5's pages run S-0 to S-12 with campaign pages L- and the Help centre's H-; the box now reads "S-0 to S-12; L-; H-", and D.1's prose now states the ranges, with Admin's AD-0 to AD-6 and the app's A-0 to A-5, which the same figure drew and the text had not stated (found by the maintainer).

Found by the maintainer and fixed: section 6 said IA6 would show the proposal until updated; IA6 was updated in this filing, so the sentence now says so.

Other filed units and the register. IA6: the declined-attempt question it proposed to IA8 is decided (IA8, section 4.5); its C.2 paragraph, its A.2 open-question cell, its facts-table row, its assumption row and its "What IA8 and IA11 take" carry dated notes or the decision; its C.2 wireflow gains the two notification routes (to a Meals screen opened from the notification, and to Card [Frozen]), so that figure's declaration changed and it was checked again (below). IA7: its "What IA8 and later units take" carries a dated note giving IA8's answers to its three open questions and the new condition on Invite employees, and its facts-table row on the leaver says decided by IA8. IA4: a dated note before "What the map hands on" lists IA8's extensions to the object map (Cancelled, closed, contract end date, the notification's two subjects, O-18, R-25). The register's IA6 line "(proposed for IA8)" becomes a fact, and IA8's facts are appended under "Set by IA8"; "Not yet set" is narrowed.

Figure re-checks, each by a fresh Opus 5.5 agent given only the unit's text with its figures taken out (each figure's place marked with its caption), the figure's caption and its shots from `verify.py --shots` (opening frame and frames sheet at 320, 360, 390 and 430 px, 768 px and 1280 px, dark and light); each report below is its hand-back, verbatim, extracted by script from its transcript (none wrote a report file; the hand-back is the one copy):
- Figure 1 (swimlanes, section 3.2): PASS on its second check. Its minors: the CL-5 note "each period: budgets, approvals, reports" (every word traced: Approvals is AD-4) and Churn drawn only in the Admin lane change the declaration and were recorded, not applied; the minor on the text (tone 6 given a second meaning in section 1) was applied: section 1 now says a figure would give each gap row tone 6, a stop.
- Figure 2 (swimlanes, section 3.3): PASS on its second check. The three minors on the declaration (EL-3's claim branch, DT-2's own exit, the caption's "DT-1 to DT-3" while only DT-2 and DT-3 are drawn) were recorded, not applied, every word they touch being traced; the minor on the text was applied (tone 5 is the Perqo system and the rules it applies).
- Figure 6 (objects, D.1): FIX on its second check (an error, the far ends of five relationships' counts not in the text; two should-fix, the "submits" and card payment "spends from" lines reading the wrong way under the figure's rule), fixed against both reports (both ends of each relationship stated in the text from IA4, A.2, checked row by row; a triangle on each of the two lines; the caption and text naming the main crossings, the both-ways perqo.com to app line and the three surfaces whose names the boxes carry), then PASS on its third check. Its last minors on the declaration (the crowded counts at the card payment's corner, a triangle for X-05) were recorded, not applied; those on the text were applied (the counts' notation stated, the crossings drawn and not drawn named, X-03 and X-04 each answering two sources and X-10 to X-13 added here).
- Figure 8 (objects, D.4): PASS on its second check. Its caption minors (the till line, "IA7, D" as a filed deliverable, the box contents' sections) change the declaration and were recorded, not applied; its minor on the text was applied (the middle row names the three lifecycles it draws and where the other two sit).
- IA6, figure 7 (wireflow, C.2), whose declaration changed with the decline notification's two routes: a first build refused a route spanning two rows, so the notification to Meals lands on a screen of its own, Meals [after a decline]; FIX on its first check (a should-fix on IA6's text: B.4 and the A-5 entry still said notifications are about claims only), fixed (B.4 gains E-8, the A-5 entry and the task inventory's notification row a dated note, the caption names the routes, the till says "Merchant's till", the face says C.2 was amended), then PASS on its second check. Its last minors: the caption's tone 6 clause and the "(assumed)" mark on the drawing change the declaration and were recorded, not applied; on the text, Meals [after a decline] is now said to be the ordinary Meals screen reached from the notification, E-8 and the A-5 note name the merchant's category screen in general (Meals in C.2), and IA6's unsure list records the amendment; the arrow-label paraphrases were recorded, not applied. IA6's figures 4 and 5, which label notifications by their claims, were left as filed: the claim labels stay true, and the dated notes beside them say what IA8 added.
- Renderer notes in every report (the opening-frame shot clipped by the sticky bars; sideways scrolling and edge fades on phones; a wrapped "X-01 Sign in") rest on how the renderer lays a figure out, and were recorded, not applied.

The page's relief. The writer's Object line names the Perqo interaction map; the library's map outline is IA2's page's, and the course must show a different outline on each of its eight pages that discuss an object (`p96_uses.py`: eight pages, so eight outlines), so IA8 takes the next object its text discusses at length, the Perqo card (sections 3.4, 4.4 and 4.5: Cancelled, the declines, the notice): the spare outline credit-card, its spare line struck, the deciding sentence "The Perqo card is cancelled at once" (the maintainer added "Perqo" to section 3.4's bold line so the sentence names the outline's keyword; no fact changed). `p95_library.py` was re-run from the three icon sets cloned at their recorded commits (so no outline's file changed; outlines.json's counts now include IA8 and the notes added to IA4, IA6 and IA7) and `relief.py credit-card` re-made its relief.

Transcripts, checked by script after each agent (models, tools, every path with the shell variables a command sets expanded, every fetch against the searches before it): no `mcp__*`, Projects, Artifact, connector or Agent tool in any. The writer (claude-opus-5-5): 27 searches and 20 fetches, each URL returned verbatim by an earlier search, none fetched twice, no redirect followed; every path inside its folder (the script also listed four HTML tag names in a screenshot script's string and the system Chrome binary its screenshot script launched, both inside its own folder's work). The checker (claude-fable-5-1): 23 searches and 26 fetches, each URL search-returned; four fetches refused (sagepub, semanticscholar, colab.ws, marmot) and none retried; three URLs fetched a second time after a first fetch that had returned their text (two NN/g articles and OMG's DMN page), recorded; it checked Gartner's release through a reproduction on salestechstar.com and a Business Wire listing, both search-returned, because no search returned gartner.com's own page, which the writer had fetched: recorded as against the spirit of the copy rule; every path inside its folder. The seven figure re-checkers (claude-opus-5-5): no web tool; every path inside their folders but for figure 6's first re-checker and figure 8's re-checker, which wrote image crops of their own shots to the session's scratchpad (`/tmp/claude-0/.../scratchpad/c/`) and read them back there, reading nothing else outside their folders; recorded, and the later re-checkers' prompts said to crop inside their folders, which they did.

## Figure 1 re-check 1 (Opus 5.5 agent, 9 November 2026; the second check of figure 1, swimlanes: the purchase lifecycle; given the unit without its figures, the caption and the frames sheets, nothing of the earlier reports; verbatim hand-back)

IA8 · figure 1 (swimlanes, section 3.2) · fresh figure check, re-check after fix

(a) Findings

- [minor] [figure] The CL-5 Run box sits only in the Admin lane, and its sub-label reads "each period: budgets, approvals, reports". The stage table (line 105) gives CL-5 as "HR, finance, employees | Admin and the app, each period | budgets, claims, card payments, reports". The figure leaves out the employees' share of Run, so the app lane is empty after "Employees join". It also swaps "claims, card payments" for "approvals". "Approvals" is not a new fact: it is Admin's Approvals area, AD-4, at lines 256 and 345. Fix: change the sub-label to line 105's words ("budgets, claims, card payments, reports"). Optionally, add a tone-3 box in the app lane under CL-5, such as "claims, card payments → see EL-1 to EL-6", so the figure shows both surfaces that line 105 gives for CL-5.
- [minor] [figure] Churn ends sign-in for employees as well as admin users, and it cancels every card (line 108). The figure draws CL-6 Churn only in the Admin lane, with nothing in the app lane. This is acceptable as drawn, because the box text says "sign-in ends, cards cancelled". If the CL-5 fix above adds an app-lane box, a short line from Churn to it would make the employee side visible.
- [minor] [text] The text gives tone 6 two meanings. Line 14: "tone 6 a stop, a path that ends without success". Line 41: "Tone 6, a fault found in a review, is the tone a figure would give each row." This figure uses the line 14 meaning, which matches line 112 and the caption, so the figure is not affected. Fix: in line 41, either say that the gap rows take tone 6 as stops, or say that IA2's notation also gives tone 6 to review faults, if it does.

No label, box text, edge label or arrow overlaps anything at any width or in either theme. All box text sits inside its box. Every box can be seen whole in at least one frame at 320, 360, 390, 430, 768 and 1280 px, in both themes. Tones read clearly on cream (light) and on dark. The kind fits the data: the client's purchase lifecycle is a journey across four actors, so swimlanes is right. The caption says what the figure shows, names section 3.2, and names the sources: Gibbons, NN/g, 2017; IA2, section 1.9; the brief; IA5, section 5.5; IA7, section 3.4. Every tone the figure draws (1, 5, 4, 3, 6) is named in the text at lines 14 and 112 and in the caption.

(b) Confirmed

- Lane "Buyer on perqo.com": line 112, "Lanes are actors on surfaces: the buyer on perqo.com (tone 1)"
- Lane "Perqo staff: sales and setup": line 112, "Perqo's sales and setup staff outside the surfaces (tone 5, the extension declared above)"; line 14, "Perqo's own staff who work outside the three surfaces (sales, and the setup of a new client) take tone 5 in a lane"
- Lane "Client's admin users in Perqo Admin": line 112, "the client's admin users in Admin (tone 4)"
- Lane "Employees in the Perqo app": line 112, "employees in the app (tone 3)"
- "CL-1 Evaluate" / "S-1 to S-3": line 101, "| CL-1 | Evaluate | a buyer at a prospective client | perqo.com: Product, Benefits, Pricing, Customers (S-1 to S-3) | interest; a demo request |"
- "CL-2 Trial: Book a demo" / "S-4; no free trial": line 102, "| CL-2 | Trial | the buyer and Perqo's sales team | perqo.com: Book a demo (S-4); … | Perqo has no free trial; the demo is this stage's form at Perqo |"
- Edge "demo request": line 101, "interest; a demo request"; line 102, "(IA4, A.3: demo request -> follow up)"
- "Demo and follow-up" / "outside the surfaces": line 102, "the demo itself and sales' follow-up are outside the surfaces"
- "CL-3 Contract" / "client and account owner set up": line 103, "| CL-3 | Contract | the client and Perqo's sales team | outside the surfaces | a signed contract; Perqo sets up the client (O-01) with its contract start and end dates and its first admin user as account owner |"
- Edge "first admin user": line 103, "its first admin user as account owner"; line 97, "Perqo sets up the client's first admin user as account owner (IA7, section 3.4)"
- "CL-4 Onboard" / "admins, groups, policies, budgets, then invites": line 104, "| CL-4 | Onboard | the account owner, HR and finance | Perqo Admin | admin users, employee groups, policies, budgets, invitations, in the order below |"; line 110, "(2) the account owner adds admin users … (3) HR creates employee groups and their policies; (4) finance sets budgets for the current period; (5) HR invites"
- Edge "invitations": line 104, "invitations, in the order below"
- "Employees join" / "→ see EL-1": line 110, "(6) employees join"; line 122, "| EL-1 | Enrol | … HR invites; the invitation (E-2) opens Join; the employee becomes Active"
- "CL-5 Run" / "each period: budgets, … reports": line 105, "| CL-5 | Run | HR, finance, employees | Admin and the app, each period | budgets, claims, card payments, reports |". The word "approvals" is not in this row; it comes from Admin's Approvals (AD-4), lines 256 and 345. See (a).
- Edge "[renewed]" and "CL-6 Renew" / "new contract end date": line 106, "| CL-6 | Renew or churn | … | a new contract end date, or the client's end |"; line 108, "A renewal sets a new end date."
- Edge "[not renewed]" and "CL-6 Churn" / "[after the contract end date] sign-in ends, cards cancelled": line 108, "At churn, the day after the contract end date, no admin user and no employee of that client can sign in, and every card of the client is cancelled"
- "Customer story removed" / "redirect to S-3": line 108, "a customer story about a former client is removed with a redirect to Customers"; line 403, "a customer story about a former client is removed with a redirect to S-3"
- Tone 6 on Churn and Customer story removed: line 112, "Churn, and the removal of the client's customer story that follows it, are tone 6, a path that ends without success."

The figure has no dates and no numbers beyond the identifiers listed above.

(c) Renderer notes

- On the phone opening-frame shots (390 px; the 320, 360 and 430 px shots look the same), the sticky section bar covers the top of the drawing. The first lane label shows only "perqo.com", and the CL-1 box shows only "S-1 to S-3". The frame sheets show the full drawing from frame 1, so this is a screenshot effect, not a fault in the declaration.
- The lane-name column is not sticky. Once a reader scrolls sideways on a phone or tablet, the lane names leave the view, and the lanes are told apart only by their background tone. On a phone this holds from about frame 2 onward. Every lane is still readable through its tone and the caption.
- Boxes fade at the left and right edges of the scroll viewport, so in many frames a box appears half-faded. Each box appears whole in a neighbouring frame at every width.
- At 1280 px the drawing is wider than the column and scrolls sideways across 5 frames. It does at 768 px too (5 frames), and on phones it takes 11 to 16 frames.

(d) Verdict

PASS. The check found no error and no should-fix. Three findings are minor: the CL-5 sub-label and its lane, Churn shown only in the Admin lane, and tone 6's second meaning at line 41.

## Figure 2 re-check 1 (Opus 5.5 agent, 9 November 2026; the second check of figure 2, swimlanes: the benefit lifecycle; given the unit without its figures, the caption and the frames sheets, nothing of the earlier reports; verbatim hand-back)

IA8, figure 2 (swimlanes, section 3.3): fresh re-check

The figure passes. Every label in it comes from the unit's text, the caption meets the standard, and it reads at every width in both themes. I have four minor findings, none of which blocks it.

(a) Findings

- [minor] [figure] **The claim branch at EL-3 is not drawn.** EL-3 Decide says "card or claim", but only one arrow leaves it, to EL-4 Spend. The Purchase box then runs straight on to EL-5 Claim, so a reader can take it that a card Purchase is then claimed. Line 124 says "pay with the card at a merchant, or pay another way and claim". **Fix:** give EL-3 two labelled exits: "[card]" to EL-4, and "[pay another way]" to EL-5. Or label the Purchase-to-Claim arrow as stage order only.

- [minor] [figure] **Only HR's route out of DT-2 is drawn.** DT-2 has one exit, "[over the limit]", to HR decides. There is no exit for claims the rule decides by itself (approved automatically, T2, or rejected over the balance, T1). So the figure suggests every claim goes to HR. Line 126 says "a claim, decided by the rule or by HR (section 4.3)", and line 257 has X-09 starting from "AD-4; the Perqo system's rule". **Fix:** add an edge from DT-2 to EL-6 labelled "[at or under the limit] notification, E-4".

- [minor] [figure/caption] **The caption cites a rule the figure does not draw.** The caption credits "the rules from section 4 (DT-1 to DT-3)", but only DT-2 and DT-3 appear. DT-1 (eligibility) is not drawn, and line 129 does not say it is. **Fix:** change the caption to "(DT-2, DT-3)", or add DT-1 at EL-2/EL-3 if the figure is meant to show eligibility.

- [minor] [text] **Line 129 does not say the rule boxes are tone 5.** It names tone 5 as "the Perqo system" lane. The DT-2 and DT-3 boxes in that lane are drawn in tone 5, which agrees with line 14 ("any object, lifecycle or rule that lives on more than one surface"), so there is no gap. Adding "and the rules it applies" to line 129's tone 5 would make it explicit.

Tones drawn: 4 (Admin, blue), 3 (app, green), 1 (Help centre, red), 2 (merchant, brown), 5 (Perqo system and the DT boxes, purple). Each is named in line 14, line 129 and the caption. No tone 6 is drawn, and none is needed.

(b) Confirmed

Lane labels:
- "HR and finance in Perqo Admin": line 129, "HR and finance in Admin (tone 4)".
- "Employee in the Perqo app": line 129, "the employee in the app (tone 3)".
- "Help centre on perqo.com": line 129, "the Help centre (tone 1)"; line 243, "perqo.com (tone 1) with Product, Pricing, Customers, Help centre".
- "Merchant at the till": line 129, "the merchant (tone 2)"; line 125, "the merchant's till".
- "Perqo system": line 129, "the Perqo system (tone 5)".

Boxes and edges:
- "HR invites" / "AD-1.3 [budgets set]": line 122, "Admin (AD-1.3) ... HR invites"; line 252, "Invite employees, AD-1.3 [the group's budgets set]"; line 110, "invite is unavailable for an employee group until its budgets for the current period are set".
- Edge "invitation, E-2": line 122, "the invitation (E-2) opens Join".
- "EL-1 Enrol: Join" / "A-0.1; Active; card ordered": line 122, "EL-1 | Enrol | ... the app (A-0.1) ... the invitation (E-2) opens Join; the employee becomes Active ...; Perqo orders the card".
- "EL-2 Learn" / "A-1, A-2.1 to A-2.4": line 123, "EL-2 | Learn | the app (A-1, A-2.1 to A-2.4)".
- Edge "external route": line 245, "X-03 to X-06 are IA6's external routes"; line 253, X-05, "A-2.1 to A-2.4 ... H-2.1.3".
- "What you can claim in each category" / "H-2.1.3": line 123, "the Help centre (What you can claim in each category, H-2.1.3; H-2.2.1)".
- "EL-3 Decide" / "card or claim; Card offers A-4.3": line 124, "EL-3 | Decide | the app (A-2.x, A-4.3) | pay with the card at a merchant, or pay another way and claim; Card offers".
- "EL-4 Spend: pay" / "Perqo card": line 125, "EL-4 | Spend | the merchant's till; the app (A-4.2.1) | a card payment, or a decline"; line 271, "Perqo card".
- "DT-3 spend limits": line 177, "### 4.4 · Spend limits"; line 181, "Decision tree DT-3, spend limits".
- "Purchase, or decline notice" / "A-4.2.1; A-5.2": line 129, "The figure draws the decline and the Purchase as one step in the app"; line 125, "A-4.2.1"; line 194, "sees the notice in Notifications (A-5.2)".
- "EL-5 Claim" / "A-3.1 to A-3.4": line 126, "EL-5 | Claim | the app (A-3.1 to A-3.4); Admin (AD-4)".
- Edge "Submit": line 256, "Check and submit, A-3.2".
- "DT-2 approval routing": line 171, "### 4.3 · Approval routing"; line 175, "Decision tree DT-2, approval routing".
- Edge "[over the limit]": line 173, "A claim over the limit waits in Approvals"; line 256, "claims over the limit".
- "HR decides" / "AD-4 [over the limit]": line 126, "Admin (AD-4) | a claim, decided by the rule or by HR"; line 256, "Approvals, AD-4".
- Edge "notification, E-4": line 257, "a notification (E-4) to Claim, A-3.4".
- "EL-6 Review" / "A-3, A-4.2, A-5.2": line 127, "EL-6 | Review | the app (A-3, A-4.2, A-5.2) | ... the next period's balances".
- "Finance sets next period" / "AD-2.2": line 127, "the next period's balances"; line 255, "Set budgets, AD-2.2"; line 355, J-14, "Set budgets (AD-2.2); No budget for next period | CL-4, CL-5, EL-6"; line 110, "finance sets budgets".

The figure has no dates and no numbers apart from identifiers. All of those are confirmed above.

(c) Renderer notes

- **Opening frames are clipped by the sticky section bar.** This affects the phone, phone320, phone360 and phone430 opening shots, and the desktop one slightly. The bar ("Section 3 of 9 / The lifecycles that run through Perqo") covers the top of the first lane. On phone 390 it hides the "HR and finance" line of the lane label and the "HR invites" title. The frame sheets show both uncovered at scroll 0.
- **On every width the drawing scrolls sideways**, with a "scroll sideways for the whole figure" hint and faded edges. Boxes and edge labels at a frame's edge are cut by the scroll window (for example "exte / ro" at the right of the desktop opening frame, and "EL-1 En…" at phone320 frame 2). Every box and label appears whole in at least one frame at every width, so nothing is cut in the drawing itself.
- **No overlaps, and no text outside its box**, in either theme. Light frames read cleanly on the cream paper. Dark frames keep their box borders, lane tints and grey edge labels legible.
- **The lanes are drawn in an order the caption does not follow.** Top to bottom they run Admin, app, Help centre, merchant, system; the caption lists the lanes starting from the app. This does not affect reading.

(d) Verdict

PASS. There is no error and no should-fix. The four minor findings in (a) are optional improvements: the EL-3 branch, the auto-decided exit from DT-2, DT-1 cited in the caption but not drawn, and the tone 5 wording in line 129.

## Figure 6 re-check 1 (Opus 5.5 agent, 9 November 2026; the second check of figure 6, objects: the surface layer; given the unit without its figures, the caption and the frames sheets, nothing of the earlier reports; verbatim hand-back)

**Figure 6 (objects), IA8, Deliverable D.1: fresh check, round 3**

**(a) Findings**

- [error] [figure] Half of each multiplicity pair has no source in the unit's text. Line 281 gives only one end of each relationship: "a claim is checked against one policy (R-09) and spends from one allocation (R-10); a card is used for any number of card payments (R-12); a card payment spends from one allocation (R-13); a merchant takes any number of card payments (R-14)". The figure also draws the other ends, and these are facts the text never states:
  - 0..* at the claim end of "is checked against" (a policy is checked by any number of claims).
  - 0..* at the claim end of the claim–allocation "spends from" (an allocation is spent from by any number of claims).
  - 1 at the card end of "is used for" (a card payment uses one card).
  - 0..* at the card-payment end of the payment–allocation "spends from".
  - 1 at the merchant end of "takes" (a card payment is taken by one merchant).
  - Fix: in line 281, state both ends of each relationship, for example: "a claim is checked against one policy and a policy checks any number of claims (R-09); a claim spends from one allocation and an allocation is spent from by any number of claims (R-10); a card is used for any number of card payments and each card payment uses one card (R-12); a card payment spends from one allocation and an allocation is spent from by any number of card payments (R-13); a merchant takes any number of card payments and each is taken by one merchant (R-14)". Alternatively, take the unsourced ends out of the figure.
- [should-fix] [figure] The "submits" line reads the wrong way under the figure's own rule. The rule is in the caption and line 281: "Lines read left to right on a level line, top to bottom otherwise, unless a triangle marks the other way". The line runs on a diagonal from the Perqo app (lower left) up to "transaction, type claim" (upper right). It is not level, so it reads top to bottom: "claim submits Perqo app", the reverse of line 281's "the app submits claims". No triangle is drawn. Fix: add a triangle by "submits" pointing toward the claim box, or route the line level.
- [should-fix] [figure] The "spends from" line between "transaction, type card payment" (lower) and "allocation" (upper) also reads the wrong way. It is a diagonal, so it reads top to bottom: "allocation spends from card payment", the reverse of line 281's "a card payment spends from one allocation (R-13)". No triangle is drawn. Fix: add a triangle by this "spends from" pointing up toward the allocation, as "is checked against" already has.
- [minor] [figure/caption] The caption says "the crossings labelled by ID" and "crossings X-01 to X-13 from D.1's table", but the figure labels only X-01, X-03 to X-07 and X-09. X-02, X-08, X-10, X-11, X-12 and X-13 are not labelled. X-10 and X-11 are the merchant side's crossings to the app. The figure has no box for X-13's "Perqo staff" end, and only the "submits" and "decides" lines stand in for X-08. Line 281 says "the main crossings". Fix: say "the main crossings labelled by ID" in the caption, and either add X-10 and X-11 or name them as left out.
- [minor] [figure] One line carries "X-03 download; X-05, X-06 help" in both directions: X-03 and X-06 run perqo.com to app, X-05 runs app to perqo.com (lines 252–254). Read top to bottom, the line makes X-05 look like a perqo.com-to-app crossing. Fix: add a triangle for X-05, or name the mixed direction in the caption.
- [minor] [figure/caption] The caption says "each surface's name", but the object boxes give only Admin, app and perqo.com lines. The merchant side's names in D.1's table are missing: "accepted at the till" (card), "the sale" (card payment), "not shown" elsewhere (lines 269–271). Fix: add "Merchant: …" lines where the table gives one, or say "the three product surfaces' names".
- [minor] [figure] "X-01 Sign in" wraps to "X-01 Sign / in" at every width, splitting the label. Fix: shorten it to "X-01 sign-in" or widen the label slot.

**(b) Confirmed**

Surface boxes:
- perqo.com: Product, Pricing, Customers, Help centre, Book a demo, Sign in, Get the Perqo app. Line 243: "perqo.com (tone 1) with Product, Pricing, Customers, Help centre, Book a demo and Sign in, and Get the Perqo app in its footer".
- "Sign in (S-5)": line 249, "Sign in, S-5 (`external`)".
- "Get the Perqo app (S-6)": line 250, "Get the Perqo app, S-6".
- "-> book a demo", "-> find help": line 281, "perqo.com -> book a demo and -> find help".
- Perqo Admin: Employees, Budgets, Policies, Approvals, Reports, Settings. Line 243: "Perqo Admin (tone 4) with Employees, Budgets, Policies, Approvals, Reports and Settings".
- "-> configure", "-> approve", "-> report": line 281, "Admin -> configure, -> approve and -> report".
- Perqo app: Home, Benefits, Claims, Card, Account. Line 243: "the Perqo app (tone 3) with Home, Benefits, Claims, Card and Account".
- "-> see balance", "-> spend", "-> claim": line 281, "the app -> see balance, -> spend and -> claim".
- merchant side, "the till", "offers": line 243, "the merchant side (tone 2), the till where the card is taken"; line 258, "the till; the merchant's offers".
- "-> take card payments": line 281, "the merchant side's is -> take card payments".

Object boxes:
- policy: "Admin: Policy / app: not shown / perqo.com: Policies". Line 270: "| policy | Policy | not shown; … | Policies | not shown |".
- transaction, type claim: "Admin: Claim / app: Claim / perqo.com: Claims". Line 268: "| transaction, type claim | Claim; … | Claim; the same states | Claims |".
- allocation: "Admin: Budget / app: Balance / perqo.com: Benefits budget". Line 267: "| allocation (`allocation`) | Budget | Balance | Benefits budget |".
- card: "Admin: Perqo card / app: Card / perqo.com: Perqo card". Line 271: "| card | Perqo card: Active, Frozen, Not issued, Cancelled *new* | Card | Perqo card |".
- transaction, type card payment: "Admin: Card payment / app: Purchase / perqo.com: Card payments". Line 269: "| transaction, type card payment | Card payment, in Reports | Purchase | Card payments |".

Line labels:
- "X-01 Sign in": line 249, "| X-01 | perqo.com | Admin | HR and finance sign in |".
- "X-03 download": line 251, "| X-03 | perqo.com | app | the download links |".
- "X-05": line 253, "| X-05 | app | perqo.com | the external routes, each to its Help centre page |".
- "X-06 help": line 254, "| X-06 | perqo.com | app | links from Help centre articles into the app |".
- "X-04 invites": line 252, "| X-04 | Admin | app | HR's invitation |".
- "X-07": line 255, "| X-07 | Admin | app | budgets as balances; …".
- "X-09 decisions": line 257, "| X-09 | Admin | app | claim decisions |".
- "sets", "decides [over the limit]", "submits", "shows as Balance", "shows; freezes": line 281, "Admin sets the policy and decides the claims over the limit; the app submits claims, shows the allocation as Balance, and shows and freezes the card".
- "is checked against" with 1 at the policy end: line 281, "a claim is checked against one policy (R-09)".
- "spends from" (claim to allocation) with 1 at the allocation end: line 281, "spends from one allocation (R-10)".
- "is used for" with 0..* at the card-payment end: line 281, "a card is used for any number of card payments (R-12)".
- "spends from" (card payment to allocation) with 1 at the allocation end: line 281, "a card payment spends from one allocation (R-13)".
- "takes" with 0..* at the card-payment end: line 281, "a merchant takes any number of card payments (R-14)".

Triangles:
- On "is checked against", pointing up toward the policy: correct, the claim checks against the policy.
- On "takes", pointing left from the merchant: correct, the merchant takes the card payment.

Tones:
- 1 perqo.com, 4 Admin, 3 app, 2 merchant side, 5 objects. Line 14: "Tone 1 is perqo.com …; tone 2 the merchant side …; tone 3 the Perqo app …; tone 4 Perqo Admin …; tone 5 shared: … any object … that lives on more than one surface". Line 281 says the same.
- Tone 6 is not drawn.

Count of shared objects:
- Five object boxes (policy, claim, allocation, card, card payment). Line 281: "five shared objects with each surface's name (tone 5, shared)".

Caption:
- It names what the figure shows, the section (Deliverable, D.1) and the sources (IA4, Deliverable A; IA7, Deliverable A; D.1's table).
- Kind "objects" fits things and relationships.

**(c) Renderer notes**

- Desktop: the figure fits one frame in both themes. The opening-frame shot is clipped at the top by the sticky header and section bar, which cover the lower part of the perqo.com, Perqo Admin and policy boxes. The frames sheet shows the whole figure clear.
- Tablet (768): the figure fits one frame and every label is clear.
- Phones (320, 360, 390, 430): the figure keeps its desktop layout, opens at its left edge with a "scroll sideways for the whole figure" note, and scrolls sideways across 4 to 5 frames at 390 and 320.
  - In the sheets read (390 light, 320 dark) and in the 430 opening frame, every box is whole in at least one frame.
  - Labels cut at the viewport edge in middle frames ("submits", "shows as Balance", "decides [over the limit]") are scroll positions, not overlaps, and each is whole in another frame.
  - Text stays legible at 320 in both themes.
- Light frames on cream show no white patches. Dark frames keep the tone contrast.

**(d) Verdict**

FIX, on three findings:
- The error: the unsourced far-end multiplicities (0..* on the claim, payment and allocation sides, and 1 at the card and merchant ends).
- The should-fix on the "submits" line, which reads claim to app without a triangle.
- The should-fix on the card payment to allocation "spends from" line, which reads allocation to card payment without a triangle.

## Figure 8 re-check 1 (Opus 5.5 agent, 9 November 2026; the second check of figure 8, objects: the whole map; given the unit without its figures, the caption and the frames sheets, nothing of the earlier reports; verbatim hand-back)

IA8 figure 8 (objects, Deliverable D.4) passes: no errors and no should-fix findings. Every label and number in the figure is in the unit's text. Each drawn connection joins the two layers that D.4's table gives it, and the figure reads at every width and in both themes. There are four minor findings.

**(a) Findings**

- [minor] [figure] The line from "merchant side" down to "DT-3 spend limits" is labelled "the till", not a J- ID, while the caption says the main connections are "labelled by their J- IDs". The relation itself is in the text (line 259, line 279, line 327), so no fact is added. Fix: add to the caption "the merchant side's line, labelled the till, is the till reading DT-3 (D.1, X-11; D.3)", or say the same in line 361.
- [minor] [text] Line 361 says "the lifecycles in the middle row", but D.2's table (lines 293–297) lists five lifecycles. The figure draws three: client, claim and employee. Employee status and Card are not boxes; they appear only through J-09's label. The caption's "the actor and lifecycle layer (middle row)" also suggests actors that are not drawn. Fix: line 361 should say "the client, employee and claim lifecycles in the middle row; the employee-status and card lifecycles sit under J-09". Change the caption's "actor and lifecycle layer" to name the lifecycles drawn.
- [minor] [figure] The caption says "Each box points to the figure that draws its layer in full", but the claim lifecycle box points to "IA7, D", a filed unit's deliverable, not a figure in this unit. The pointer is correct (line 295). Fix: in the caption, "points to the figure, or the filed deliverable, that draws its layer in full".
- [minor] [figure] The caption names section 5.1 and D.4's table as sources, but the box contents (S-0 to S-12; L-; H-, AD-0 to AD-6, A-0 to A-5, CL-1 to CL-6, EL-1 to EL-6, DT-1 to DT-3) come from D.1 to D.3. Fix: add "box contents from D.1 to D.3" to the caption's source clause.

No tone the text leaves unnamed: tones 1, 2, 3, 4 and 5 are drawn and all are named in line 361 and in the caption. Tone 6 is not drawn.

The kind fits: things (surfaces, lifecycles, rules) and their relationships drawn as objects.

The caption says what the figure shows, names the section (Deliverable, D.4) and names sources (section 5.1; D.4's table).

Checked at 320, 360, 390, 430, 768 and 1280 px, light and dark:
- No text sits outside its box and nothing overlaps.
- Every label is readable on both the cream and the dark background.
- Every box and label appears whole in at least one frame at every phone width.

**(b) Confirmed**

Surface boxes:
- "perqo.com", "S-0 to S-12; L-; H-". Line 243: "perqo.com (tone 1) … its pages S-0 to S-12 with the campaign pages L- and the Help centre's H-"
- "Perqo Admin", "AD-0 to AD-6". Line 243: "Perqo Admin (tone 4) … its pages AD-0 to AD-6 (IA7, Deliverable C)"
- "Perqo app", "A-0 to A-5". Line 243: "the Perqo app (tone 3) … its screens A-0 to A-5 (IA6, Deliverable B)"
- "merchant side", "the till". Line 243: "the merchant side (tone 2), the till where the card is taken"
- "→ see figure 6" on all four. Line 283: "[Figure 6, objects: … the surface layer of the Perqo interaction map …]". Line 367: "Start from figure 6".

Layer words:
- "surface layer", "lifecycle layer", "decision layer". Lines 206–208: "Surface layer |", "Actor and lifecycle layer |", "Decision-tree layer |". Line 361: "Each box names its layer in its first line and points to the figure that draws it in full".

Lifecycle boxes:
- "client lifecycle", "CL-1 to CL-6", "→ see figure 1". Line 293: "Client company (purchase) | CL-1 Evaluate, … CL-6 Renew or churn | figure 1, section 3.2"
- "claim lifecycle", "Submitted, Approved, Rejected, Paid", "→ see IA7, D". Line 295: "Claim | Submitted, Approved, Rejected, Paid; T1 to T6; EX-1 to EX-4 | IA7, Deliverable D"
- "employee lifecycle", "EL-1 to EL-6", "→ see figure 2". Line 294: "Employee (benefit) | EL-1 Enrol, … EL-6 Review, each period | figure 2, section 3.3"

Decision boxes:
- "DT-1 eligibility", "→ see figure 3". Line 305: "**DT-1 · Eligibility** (figure 3)."
- "DT-2 approval routing", "→ see figure 4". Line 315: "**DT-2 · Approval routing** (figure 4)."
- "DT-3 spend limits", "→ see figure 5". Line 327: "**DT-3 · Spend limits** (figure 5)."

Connection labels (all from the D.4 table, lines 340–355):
- "J-12 demo", perqo.com to client lifecycle. Line 353: "J-12 | demo | Book a demo (S-4); customer stories (S-3.x) | CL-1, CL-2, CL-6 | none"
- "J-10, J-14", Admin to client lifecycle.
  - Line 351: "J-10 | contract | Company (AD-6.1), contract end date | CL-3, CL-6 | DT-1, Contract in force"
  - Line 355: "J-14 | budgets | Set budgets (AD-2.2); No budget for next period | CL-4, CL-5, EL-6 | DT-1, Allocation set"
- "J-04 Approvals", Admin to claim lifecycle. Line 345: "J-04 | Approvals | Approvals (AD-4) | T3, T4, T5; EX-1, EX-3 | DT-2, HR's question and the recheck"
- "J-03 Claims", app to claim lifecycle. Line 344: "J-03 | Claims | Claims groups (A-3) and Claim (A-3.4) | the four claim states; EL-5, EL-6"
- "J-05, J-08", app to employee lifecycle.
  - Line 346: "J-05 | invite | Invite employees (AD-1.3), X-04, Join (A-0.1) | Invited to Active; EL-1; CL-4 | DT-1, Employee Active"
  - Line 349: "J-08 | categories | open categories (O-04) to A-2 | EL-2, EL-3 | DT-1, Category open"
- "J-01, J-02", claim lifecycle to DT-2.
  - Line 342: "J-01 | status | claim status attribute (O-07) | claim states, T1 to T6 (IA7, D) | DT-2 outcomes"
  - Line 343: "J-02 | limit | … | Submitted, waiting in Approvals | DT-2, second question"
- "J-09, J-14", employee lifecycle to DT-1.
  - Line 350: "J-09 | card | card status (O-09; AD-1.1; A-4) | Left; Cancelled | DT-1, Employee Active; DT-3, Card Active"
  - Line 355 as above ("DT-1, Allocation set")
  - Line 299: "The employee's status moves at EL-1 (Invited to Active) and at leaving (Left)"
- "J-06, J-07", employee lifecycle to DT-3.
  - Line 347: "J-06 | Purchase | Purchase (A-4.2.1); card payment (O-08) | EL-4 | DT-3, the category rule"
  - Line 348: "J-07 | decline | decline notice, X-11 (A-5.2) | EL-4 | DT-3, the three declines"
- "the till", merchant side to DT-3.
  - Line 327: "**DT-3 · Spend limits** (figure 5). Read by: the till"
  - Line 259: "X-11 | merchant side | app | declined attempts *new* | the till (DT-3)"

Tones:
- Line 361: "Lifecycles and trees that span surfaces take tone 5, shared; the surfaces keep their own tones: perqo.com 1, Admin 4, the app 3, the merchant side 2."

**(c) Renderer notes**

- The opening-frame shot at phone (390 px) is clipped at the top by the sticky section bar ("Section 7 of 9 · Deliverable · The Perqo interaction map"). The title rows of the perqo.com and Perqo Admin boxes are hidden there. The frame sheet shows them in full, so this comes from the shot, not the drawing.
- At every phone width (320, 360, 390, 430) the drawing is wider than the column. It scrolls sideways under the line "scroll sideways for the whole figure" and opens at 0. The sheets have 5, 4, 4 and 3 frames respectively.
- At the column edges a fade mask partly hides the boxes cut by the edge, for example the left edge of the employee lifecycle box in phone320 frame 4. This is the scroll affordance. Every box is shown unmasked in at least one frame.
- The diagonal J-03 line spans two frames at 320 px. Its label is shown whole in frame 3.
- At tablet (768 px) and desktop (1280 px) the whole figure fits in one frame.

**(d) Verdict**

PASS: no error and no should-fix. The four minor findings in (a) are optional caption and text clarifications.

## IA6 figure 7 re-check 1 (Opus 5.5 agent, 9 November 2026; the first check of IA6's C.2 wireflow after IA8 changed it; given the unit without its figures, the caption and the frames sheets, nothing of the earlier reports; verbatim hand-back)

**(a) Findings**

- [should-fix] [text] The unit now says two different things about notifications. The figure draws a decline notification that opens Meals (A-2.4) or Card (A-4), following C.2's note (line 430). Deliverable B, which the caption names as the source of the screens, still says notifications only concern claims: line 369, "Notifications (each about one claim and opening it: IA4, Deliverable A)"; line 303, the notification row, "opens the claim it is about"; and line 382, where B.4 ("Every way into the app") has only "E-4 | A notification about a claim". So the figure's two notification routes are ways into the app that B.4 does not list, and that line 369 rules out. Fix: add a B.4 row, for example "E-8 | A notification about a declined card payment | the phone's notifications, or Notifications, A-5.2 | Meals (A-2.4) for the balance, Card (A-4) for a Frozen card", with no address unless one is set. Then amend line 369, the line 303 row and B.5's Notifications row so notifications cover claims and declined payments, each with a dated note pointing to IA8, section 4.5. Line 444 already says the decision "would extend the notification beyond claims", which is the gap this closes.
- [minor] [figure] The caption's first clause names the declined path but not the two notification routes, which now take up the figure's bottom row (Card [Frozen], Meals [from the notification]). Fix: "…to the till and the Purchase, with the declined path and the decline notification's two routes back into the app; supports…".
- [minor] [figure] Tone 6 is defined as "a path that ends without success", and line 12 says tone 6 "marks a state where the path ends without success". "Declined at the till" now has two routes leaving it, so the path no longer ends there. Only the payment fails. Fix: in the caption, "tone 6 the declined payment, where the spending ends without success; the notification's two routes lead on in the app".
- [minor] [figure] The title "Meals [from the notification]" puts a way in inside square brackets. Square brackets mark a state (C intro, line 420: "A screen title with a [condition] is a state of that screen"), and section 2 marks ways in with "entry:". The screen is in the low-balance state; the notification is only how the employee gets there. Fix: "Meals [balance too low]" or "Meals [over the Meals balance]". The arrow label already carries "notification:".
- [minor] [figure] "Merchant's card reader" (in At the till) uses words the text never uses. The text says "a merchant's till" (lines 40, 430). It reads as placeholder copy, not a fact. Fix: "Merchant's till", or "The till".
- [minor] [figure] Two arrow labels are inferences, not the text's words. "pay at a Meals merchant": the text says "goes straight to a merchant" (line 430), and "Meals merchant" only follows from the walkthrough being about Meals. "pay at the offer's merchant": the text never says the employee pays at the offer's merchant, though an offer has a merchant (line 368). Both are fair; if exact wording is wanted, use "go straight to a merchant" and "pay at the merchant".
- [minor] [text] Tone 2 is defined only in this figure's caption (line 432). The body text gives tone 3 and tone 6 (line 12) and says only that a step outside the app becomes "a screen of the other surface in its tone" (line 208), with no number. Figure 6 handles tone 1 the same way. Fix, optional: after line 430, add one clause, "the till is drawn in tone 2, the merchant side".
- [minor] [text] Line 430's note repeats "decided by IA8": "IA8 decided it (IA8, section 4.5): a declined attempt sends a notification, decided by IA8, 'Card payment declined'…". Fix: drop the second "decided by IA8,".
- [minor] [text] Deliverable C's face (line 418) still reads "version 1, dated 3 November 2026", although C.2 and figure 7 changed on 9 November 2026. Fix: add "; C.2 amended 9 November 2026 (IA8, section 4.5)", or follow whatever versioning convention the course uses for notes.

No label, date or number in the figure is missing from the text. The figure has no dates or numbers. The kind fits: these are screens, so a wireflow. Every label is fully readable in at least one frame at every width and theme, nothing sits outside its box, and nothing overlaps.

**(b) Confirmed**

- "Home", "Balance", "Health", "Learning", "Mobility", "Meals", "Recent activity": line 365, "**A-1 Home.** Balance: each open category with what remains … Recent activity, the latest purchases and claims mixed"; line 63, "Home … Benefits …"; line 235, "Health, Learning, Mobility, Meals".
- "tap Meals": line 430, "From Home the employee taps Meals".
- "Meals", "Meals balance", "What's covered": line 430, "sees the Meals balance and what's covered".
- "Restaurants: restaurant meal", "Groceries: groceries": line 358, "under Meals, restaurant meal (Restaurants) and groceries (Groceries)".
- "Cookery course: covered under Learning": line 343, "cookery course in Meals … each 'covered under' its home, marked assumed (IA4, R6)"; line 358, "under Learning, coding course and cookery course (Courses)".
- "Card offers in Meals": line 168, "the route 'Card offers in Meals' appears on the Meals screen only when Meals has an offer (R5)".
- "New claim" on Meals: line 366, "New claim with the category already chosen".
- "tap Card offers in Meals": line 430, "either taps Card offers in Meals to see the offers for Meals items".
- "pay at a Meals merchant": line 430, "or goes straight to a merchant" (see (a)).
- "Card offers", "Filter: Meals", "Title and discount", "Merchant, valid until": line 368, "Card offers (A-4.3: … filterable by category, each with title, discount, merchant and valid until)"; line 319, "filtered to that category".
- "pay at the offer's merchant": line 368, offers carry a "merchant"; line 430, "goes straight to a merchant" (see (a)).
- "At the till", "Pay with the Perqo card": line 430, "Spending is done with the Perqo card at a merchant's till"; line 264, "Pay with my card".
- "Merchant's card reader": line 430, "a merchant's till" (wording not in the text; see (a)).
- "[within the Meals balance, card Active] open Card, Purchases": line 430, "a payment over the balance of the merchant's category, or with the card Frozen, is declined at the till. A taken payment appears in Purchases"; line 368, "the status, Active or Frozen"; line 288, "Purchases sits one tap into Card".
- "[over the Meals balance, or card Frozen]": line 430, "a payment over the balance of the merchant's category, or with the card Frozen, is declined at the till".
- "Purchase", "Merchant", "Amount and date", "Category: Meals", "Meals balance after": line 430, "as a Purchase with its merchant, amount, date, category and the category's balance after"; line 368, "A-4.2.1: merchant, amount, date, category and the category's balance after".
- "Declined at the till", "Payment declined", "[over the Meals balance] or [card Frozen]": line 430, "is declined at the till … the employee sees the decline at the till".
- "notification: Card payment declined [card Frozen]" (to Card): line 430, "a declined attempt sends a notification … 'Card payment declined' … opening … Card for a Frozen card".
- "notification: Card payment declined [over the Meals balance]" (to Meals): line 430, "opening the Meals screen for a balance".
- "Card [Frozen]", "Status: Frozen", "Unfreeze card": line 430, "the Card screen shows a Frozen card with Unfreeze card"; line 191, "A Frozen card shows its state and Unfreeze card on the Card screen (IA4, A.3)".
- "Card details", "Purchases" (buttons on Card): line 368, "**A-4 Card.** Card details (A-4.1 …), Purchases (A-4.2, newest first)".
- "Meals [from the notification]", "Meals balance", "What's covered": line 430, "opening the Meals screen for a balance"; line 366, the category screen "shows the category's balance … What's covered".

**(c) Renderer notes**

- Opening-frame shots: at desktop (1280) and phone (390) the figure is taller than the viewport, and the sticky section bar ("Section 9 of 11 · Deliverable · C · Three core flows as wireflows") covers the middle of the drawing (the Card offers and At the till row). This comes from the shot's layout, not the declaration. The frame sheets show every part of the drawing clear of the bar.
- Phone widths (320, 360, 390, 430): the two columns do not fit, so the renderer scrolls the figure sideways ("scroll sideways for the whole figure") and the frames open at x=134. Labels in the gutter between columns, such as "tap Card offers in Meals", "[within the Meals balance, card Active] open Card, Purchases" and "notification: Card payment declined [card Frozen]", are cut at the frame edge in one frame and whole in another, so each can be read at every width in both themes. The fade at the right edge is the renderer's scroll hint.
- In the right-hand gutter the renderer wraps "notification: Card payment declined [over the Meals balance]" and "[over the Meals balance, or card Frozen]" into narrow stacks of four to six lines, at every width. They are readable, just tall. A wider right gutter or shorter labels would fix this, if wanted.
- Desktop and tablet: one frame each, the whole figure fits. On cream (light) and dark, the tones are distinct: tone 3 teal for app screens, tone 2 rust/peach for At the till, and tone 6 olive/khaki for Declined at the till.

**(d) Verdict**

FIX. One should-fix makes it FIX, and it is in the text: Deliverable B still describes notifications as claim-only, and B.4, which claims to list every way into the app, leaves out the decline notification that figure 7 now draws, landing on Meals and on Card. The figure itself has no error and no should-fix. Its findings are all minor: the caption could name the two notification routes and restate what tone 6 means now that the declined state has exits, "[from the notification]" should be a state rather than a way in, and "card reader" should be "till".

## Figure 6 re-check 2 (Opus 5.5 agent, 9 November 2026; the third check of figure 6, objects: the surface layer; given the unit without its figures, the caption and the frames sheets, nothing of the earlier reports; verbatim hand-back)

**Figure 6 (objects), IA8, Deliverable D.1: fresh check**

**(a) Findings**

- [minor] [figure] The four counts labelled "0..\*" on R-09, R-10, R-12 and R-13/R-14 are written in the text only in words ("any number"). The text never writes "0..\*". The fact is in the text; the notation is not. Fix: line 281 adds "(drawn 1 and 0..\*)" after "with their counts", or the caption says "counts in the course notation, 1 and 0..\* for any number".
- [minor] [figure] Two "0..\*" labels sit close together, one above the other, at the top-right corner of "transaction, type card payment". The upper one belongs to the "spends from" line (R-13); the lower one, "0..\*  1", belongs to the "takes" line (R-14). They do not overlap and both can be read, but at a glance you cannot tell which label goes with which line. Fix: start the "spends from" line from the box's top edge, or move its "0..\*" up along that line.
- [minor] [figure] The vertical perqo.com–app line has no triangle. The caption and line 281 say this line carries crossings both ways (X-05 goes app → perqo.com), but the figure's own reading rule ("top to bottom otherwise, unless a triangle marks the other way") would read the whole line downward. The caption covers this, so it is not a should-fix. Fix: put a triangle by "X-05", or give the line triangles at both ends.
- [minor] [text] The caption says "crossings X-01 to X-13 from D.1's table" and line 281 says "the main crossings labelled by their X- identifiers". The figure labels only X-01, X-03 to X-07 and X-09. Not drawn: X-02, X-08 (shown only as the unlabelled "submits" and "decides [over the limit]" lines), X-10, X-11 (the unit's new declined-attempt crossing), X-12 and X-13. Fix: line 281 names the crossings that are drawn and says the rest are in the table. For example, add after "X-05 out of it": "; X-01 Sign in; X-04, X-07 and X-09 from Admin to the app; X-02, X-08 and X-10 to X-13 are in the table only".
- [minor] [text] Line 245 gives X-03 to both IA5's rows ("X-01 to X-03") and IA6's routes ("X-03 to X-06"), and X-04 to both IA6 and IA1 ("X-04, X-07 to X-09"). It does not say where X-10 to X-13 come from. Fix: say that X-03 and X-04 are shared on purpose, and add "X-10 to X-13 are this unit's".

**(b) Confirmed**

Surface boxes:
- "perqo.com", "Product", "Pricing", "Customers", "Help centre", "Book a demo", "Sign in", "Get the Perqo app": l.243 "perqo.com (tone 1) with Product, Pricing, Customers, Help centre, Book a demo and Sign in, and Get the Perqo app in its footer"
- "(S-5)": l.249 "Sign in, S-5 (`external`)"
- "(S-6)": l.250 "Get the Perqo app, S-6"
- "-> book a demo", "-> find help": l.281 "perqo.com -> book a demo and -> find help"
- "Perqo Admin", "Employees", "Budgets", "Policies", "Approvals", "Reports", "Settings": l.243 "Perqo Admin (tone 4) with Employees, Budgets, Policies, Approvals, Reports and Settings"
- "-> configure", "-> approve", "-> report": l.281 "Admin -> configure, -> approve and -> report"
- "Perqo app", "Home", "Benefits", "Claims", "Card", "Account": l.243 "the Perqo app (tone 3) with Home, Benefits, Claims, Card and Account"
- "-> see balance", "-> spend", "-> claim": l.281 "the app -> see balance, -> spend and -> claim"
- "merchant side", "the till": l.243 "the merchant side (tone 2), the till where the card is taken"
- "offers": l.258 "card payments; offers | the till; the merchant's offers"
- "-> take card payments": l.281 "the merchant side's is -> take card payments"

Shared objects:
- "policy" / "Admin: Policy" / "app: not shown" / "perqo.com: Policies": l.270 "| policy | Policy | not shown; open categories … | Policies | not shown |"
- "transaction, type claim" / "Admin: Claim" / "app: Claim" / "perqo.com: Claims": l.268 "| transaction, type claim | Claim; Submitted, Approved, Rejected, Paid | Claim; the same states | Claims | not shown |"
- "allocation" / "Admin: Budget" / "app: Balance" / "perqo.com: Benefits budget": l.267 "| allocation (`allocation`) | Budget | Balance | Benefits budget | not shown |"
- "card" / "Admin: Perqo card" / "app: Card" / "perqo.com: Perqo card": l.271 "| card | Perqo card: Active, Frozen, Not issued, Cancelled *new* | Card | Perqo card | accepted at the till |"
- "transaction, type card payment" / "Admin: Card payment" / "app: Purchase" / "perqo.com: Card payments": l.269 "| transaction, type card payment | Card payment, in Reports | Purchase | Card payments | the sale |"

Crossings:
- "X-01 Sign in": l.249 "| X-01 | perqo.com | Admin | HR and finance sign in | Sign in, S-5"
- "X-03 download": l.251 "| X-03 | perqo.com | app | the download links"
- "X-05" and "X-06 help": l.253 "| X-05 | app | perqo.com | the external routes, each to its Help centre page" and l.254 "| X-06 | perqo.com | app | links from Help centre articles into the app". Both ways: l.281 "(X-03 and X-06 into the app, X-05 out of it)"
- "X-04 invites": l.252 "| X-04 | Admin | app | HR's invitation"
- "X-07": l.255 "| X-07 | Admin | app | budgets as balances"
- "X-09 decisions": l.257 "| X-09 | Admin | app | claim decisions"

Lines from a surface to an object:
- "sets" and "decides [over the limit]": l.281 "Admin sets the policy and decides the claims over the limit"
- "submits" (triangle, upward), "shows as Balance", "shows; freezes": l.281 "the app submits claims, shows the allocation as Balance, and shows and freezes the card"
- "takes" (triangle pointing left), "1" at the merchant, "0..\*" at the card payment: l.281 "a merchant takes any number of card payments, and each is taken by one merchant (R-14)"

Relationships between objects, with their counts:
- "is checked against" (triangle, upward), "1" at the policy, "0..\*" at the claim: l.281 "a claim is checked against one policy, and a policy checks any number of claims (R-09)"
- "spends from", "0..\*" at the claim, "1" at the allocation: l.281 "a claim spends from one allocation, and an allocation is spent from by any number of claims (R-10)"
- "is used for", "1" at the card, "0..\*" at the card payment: l.281 "a card is used for any number of card payments, and each card payment uses one card (R-12)"
- "spends from" (triangle, upward), "0..\*" at the card payment, "1" at the allocation: l.281 "a card payment spends from one allocation, and an allocation is spent from by any number of card payments (R-13)"

Tones:
- Tone 1 red (perqo.com), tone 4 blue (Admin), tone 3 green (app), tone 2 brown/orange (merchant side): l.243 and l.281 "(perqo.com tone 1, Admin tone 4, the app tone 3, the merchant side tone 2)"
- Tone 5 purple (objects): l.281 "five shared objects … (tone 5, shared)"
- No tone 6 is drawn.

Kind and caption:
- Kind "objects" fits things and relationships: l.206 "| Surface layer | … | objects |"
- caption.txt matches l.283 word for word. It names what the figure shows, the section (Deliverable, D.1) and the sources (IA2 §5.3, IA1, IA5 to IA7, IA4 Deliverable A, IA7 Deliverable A, D.1's table).
- The caption's "five shared objects" matches the five boxes drawn.

**(c) Renderer notes**

- Desktop (1280) and tablet (768): the whole figure fits in one frame. The desktop opening-frame shot, in both themes, is clipped at the top by the sticky course and section bars: the bottom of Admin's top level and the "X-01 Sign in" label are hidden behind them. The frames sheet shows the figure whole. This comes from the shot's scroll position, not from the declaration.
- Phones (320, 360, 390, 430): the drawing is wider than the column. It opens at 0 and scrolls sideways (442, 402, 372 and 332 px of travel), with a "scroll sideways for the whole figure" note and a fade at the edge. Every box and label is whole in at least one frame at each width. At 320, Admin and the card payment are whole in frame 2, the merchant side in frame 3, and policy, claim and allocation in frame 5. Boxes cut at the frame edge are expected in a sideways-scrolling figure, not a drawing fault.
- Light theme on cream and dark theme: every label can be read. The multiplicity labels are small and muted but legible at every width.

**(d) Verdict**

PASS. No error and no should-fix. All five findings are minor: the "0..\*" notation is not written in the text, the two "0..\*" labels are crowded at the card payment corner, the both-ways perqo.com–app line has no triangle, the text does not say which X- crossings are drawn, and line 245's X- numbering overlaps.

## IA6 figure 7 re-check 2 (Opus 5.5 agent, 9 November 2026; the second check of IA6's C.2 wireflow after IA8 changed it; given the unit without its figures, the caption and the frames sheets, nothing of the earlier reports; verbatim hand-back)

**Figure check: IA6, figure 7 (wireflow), Deliverable C, C.2**

I checked the figure at desktop (1280), tablet (768), phone (390), phone320, phone360 and phone430, in dark and light. Light frames were judged on cream. I opened the opening shots and the frame sheets. For the tall phone sheets I cut them into pieces in /home/claude/u8/r7/work/ and read those.

The figure has eight screens in two columns:
- Home, then Meals.
- Card offers, then At the till.
- Purchase, then Declined at the till.
- Card [Frozen], then Meals [after a decline].

It has eight labelled arrows. It contains no dates and no numbers.

## (a) Findings

- [minor] [figure] The Meals screen's line "Cookery course: covered under Learning" has no "(assumed)" mark on the drawing. Only the caption says the cross-listing is assumed. Line 473 sets the cross-listing as "(assumed)" and figure 4's notes mark it. Fix: optionally add "(assumed)" to the line, or leave it to the caption as it stands.
- [minor] [figure] The arrow labels "pay at a Meals merchant" and "pay at the offer's merchant" paraphrase line 431 ("goes straight to a merchant"; "a card payment spends from the allocation of the merchant's category"). The text never says outright that the employee goes from Card offers to the offer's merchant; that comes from line 412 ("an offer is a discount for paying with the Perqo card"). No fact is added. Fix: optionally add "or goes from an offer to its merchant" to line 431.
- [minor] [text] Line 421 says "A screen title with a [condition] is a state of that screen". The figure draws two such states that B.5 does not list: Card [Frozen] and Meals [after a decline]. B.5's Card row has only [no card issued], and its category-screen row has only [balance used up]. Line 431 also never says what Meals [after a decline] shows that differs from Meals; in the drawing, only the shorter balance bar differs. Fix: add both states to B.5's table, or say in line 431 that Meals [after a decline] is the ordinary Meals screen reached from the notification.
- [minor] [text] The general entries say the notification opens Meals for a balance: line 386 (E-8, "Meals, A-2.4, for a balance") and line 369 ("opening Meals for a balance"). The decline rule, though, is per merchant category (line 431, "a payment over the balance of the merchant's category"). Within C.2's Meals example the wording is right; as a general rule it is too narrow. Fix: write "the merchant's category screen (A-2.1 to A-2.4; Meals in C.2)" in E-8 and the A-5 note.
- [minor] [text] The Unsure list (line 526) still records the 3 November fresh check as "figures 2, 3, 6 and 7 passed". It does not record the 9 November amendment of figure 7 or its checks since. Fix: add figure 7's amendment and later checks when this check is filed.
- [minor] [figure] The caption's tone-6 clause, "where the spending ends without success, the notification's two routes leading on in the app", runs two ideas into one clause. It reads as if the routes were tone 6, but the arrows are neutral. Fix: "tone 6 the declined payment, where the spending ends without success; from it the notification's two routes lead on in the app."

There are no errors and no should-fix findings:
- **Caption:** it says what the figure shows, names the section (Deliverable C, C.2) and names each source: IA4 Deliverable A, this section, IA8 section 4.5, IA4 rule R6, Laubheimer 2016 and Deliverable B.
- **Kind:** screens, so wireflow fits.
- **Tones:** every tone drawn is named in the text.
  - Tone 3: line 12, "every app box is tone 3".
  - Tone 2: line 431, "the till is drawn in tone 2, the merchant side".
  - Tone 6: line 12, "tone 6, IA2's stop, marks a state where the path ends without success".
- **Legibility:** every label is readable and inside its box in at least one frame at every width and theme. Nothing overlaps.

## (b) Confirmed

Line numbers are from unit-text.md.

- **Screen "Home".** Line 365: "**A-1 Home.** Balance: each open category with what remains, each opening its category screen; … Recent activity, the latest purchases and claims mixed".
- **"Balance", "Recent activity" (on Home).** Line 365, as above. Also line 354: "Balance; Health, Learning, Mobility and Meals and their narrower terms; … and Recent activity, which passed A2".
- **"Health", "Learning", "Mobility", "Meals".** Line 235: "| Health, Learning, Mobility, Meals | F-CAT values CAT-HEA, CAT-LEA, CAT-MOB, CAT-MEA".
- **Arrow "tap Meals".** Line 431: "From Home the employee taps Meals".
- **Screen "Meals", "Meals balance", "What's covered".** Line 431: "sees the Meals balance and what's covered". Line 366: "shows the category's balance (remaining, spent, amount, period), What's covered".
- **"Restaurants: restaurant meal", "Groceries: groceries".** Line 358: "under Meals, restaurant meal (Restaurants) and groceries (Groceries)".
- **"Cookery course: covered under Learning".** Line 358: "under Learning, coding course and cookery course (Courses)". Line 343: "cookery course in Meals, … each "covered under" its home, marked assumed (IA4, R6)". Line 366: "each naming its home ("Yoga class: covered under Health")".
- **Button "Card offers in Meals"** and **arrow "tap Card offers in Meals".** Line 431: "either taps Card offers in Meals to see the offers for Meals items". Line 366: "the route "Card offers in Learning" when the category has offers".
- **Button "New claim".** Line 366: "New claim with the category already chosen".
- **Arrow "pay at a Meals merchant".** Line 431: "or goes straight to a merchant. At the till, a card payment spends from the allocation of the merchant's category".
- **Screen "Card offers", "Filter: Meals".** Line 431: "to see the offers for Meals items". Line 368: "Card offers (A-4.3: offers for items in the open categories, filterable by category". Line 385: "Card offers, filtered".
- **"Title and discount" (twice), "Merchant, valid until".** Line 368: "each with title, discount, merchant and valid until". Line 302: "title, discount, merchant, valid until".
- **Arrow "pay at the offer's merchant".** Line 412: "an offer is a discount for paying with the Perqo card". Line 431: "goes straight to a merchant".
- **Screen "At the till", "Merchant's till", "Pay with the Perqo card".** Line 431: "Spending is done with the Perqo card at a merchant's till". Line 264: "| T-01 | Pay with my card | … the card at a merchant's till".
- **Arrow "[within the Meals balance, card Active] open Card, Purchases".** Line 431: "a payment over the balance of the merchant's category, or with the card Frozen, is declined at the till. A taken payment appears in Purchases". Line 368: "the status, Active or Frozen".
- **Screen "Purchase", "Merchant", "Amount and date", "Category: Meals", "Meals balance after".** Line 431: "as a Purchase with its merchant, amount, date, category and the category's balance after". Line 368: "each Purchase (A-4.2.1: merchant, amount, date, category and the category's balance after)".
- **Arrow "[over the Meals balance, or card Frozen]".** Line 431: "a payment over the balance of the merchant's category, or with the card Frozen, is declined at the till".
- **Screen "Declined at the till", "Payment declined", "[over the Meals balance] or [card Frozen]".** Line 431: "is declined at the till … the employee sees the decline at the till". Line 481: "A card payment over the balance of the merchant's category, or with the card Frozen, is declined at the till".
- **Arrow "notification: Card payment declined [card Frozen]".** Line 431: "a declined attempt sends a notification, "Card payment declined", … opening … Card for a Frozen card".
- **Arrow "notification: Card payment declined [over the Meals balance]".** Line 431: "opening the Meals screen for a balance (Meals [after a decline] in the wireflow below)".
- **Screen "Card [Frozen]", "Status: Frozen", "Unfreeze card".** Line 431: "the Card screen shows a Frozen card with Unfreeze card". Line 191: "A Frozen card shows its state and Unfreeze card on the Card screen".
- **"Card details", "Purchases" (on Card).** Line 368: "**A-4 Card.** Card details (A-4.1: the last four digits and the status, Active or Frozen …), Purchases (A-4.2, newest first)".
- **Screen "Meals [after a decline]", "Meals balance", "What's covered".** Line 431: "(Meals [after a decline] in the wireflow below)". Line 366, as above.
- **Tones.**
  - Tone 3, the six app screens: line 12, "every app box is tone 3".
  - Tone 2, At the till: line 431, "the till is drawn in tone 2, the merchant side".
  - Tone 6, Declined at the till: line 12, "tone 6, IA2's stop, marks a state where the path ends without success".
- **Caption.** The caption in caption.txt is identical to the one at line 433. Its date, "9 November 2026", matches line 431 ("*Note, 9 November 2026: …") and line 419 ("C.2 amended 9 November 2026 (IA8, section 4.5)").

## (c) Renderer notes

- **Opening shots are clipped by the sticky bars.** On desktop, the drawing (1,240 px with its caption) is taller than the viewport, so the sticky course bar and section bar ("SECTION 9 OF 11 · Deliverable · C · Three core flows as wireflows") cover the band between Meals and Purchase. They hide the bottom of the Card offers box, the top of At the till and the arrow label "pay at the offer's merchant". The phone opening shots are clipped the same way across Card offers and At the till. Both frame sheets ("frame 1 of 1") show the whole figure uncovered. This comes from the renderer, not the declaration.
- **On phones the figure scrolls sideways** ("scroll sideways for the whole figure"). Frame 1 opens at the drawing's left edge, and the right column is cut at the frame edge. The 390 px sheet has 3 frames, the 320 px sheet has 4, and the 360 and 430 px sheets have 3 each.
- **Truncated arrow labels on phone.** In some frames these labels are cut at the scroll edge: "tap Card offers in Meals", "[within the Meals balance, card Active] open Card, Purchases" and "notification: Card payment declined [card Frozen]". Each reads whole in a neighbouring frame at every width.
- **Edge fades.** At the scroll edge, header bars fade (for example At the till and Meals [after a decline] at 320 px). Each box title reads whole in another frame.
- **Small jog in the right-hand arrows.** The vertical arrows from Meals, At the till and Declined at the till each have a short elbow just below their label. It is a routing artefact and joins nothing.
- **Theme contrast.** In dark, tone 2 (orange border, brown header) and tone 6 (gold border, olive header) are told apart by their borders. In light on cream, tone 2 is a rust border with a peach header, tone 6 an olive-brown border with a tan header. Both are distinct from each other and from tone 3's teal.

## (d) Verdict

PASS. There are no errors and no should-fix findings. All six findings are minor and optional.
