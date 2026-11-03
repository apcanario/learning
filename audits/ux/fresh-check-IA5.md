---
audit: fresh check
unit: IA5 · Level 1 · the sales and product website
course: ux · IA · Information Architecture
model: Fable 5.1 (claude-fable-5-1, confirmed from the agent's transcript; live search; no Fable 5.1 fresh check is owed for IA5)
date: 2026-11-03
chat: own Fable 5.1 agent context, not shown the writing (P31), launched by the U-5 chat (Fable 5.1 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgR2PbWYa8nEE8H2FMZw
verdict: fix · 2 errors, 3 should-fix, 5 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). It differs from the report file the checker wrote in its own folder in one place only: the hand-back's Integrity paragraph adds a sentence naming that file. The maintainer's note follows the report.

# IA5 · fresh check (skills/audit-units §3b)

Model: Fable 5.1 (claude-fable-5-1).

**Integrity.** `diff K/unit.md K/unit-readonly.md` printed nothing (exit 0). `sha256sum K/unit.md` = `1322257470e01ebef6f7e66e41494945e909ea70387316359cd627ead9174da6`, identical to K/unit.sha256. Every `Current:` below was counted with `grep -F -c` logic on the exact copy; each occurs once (count given). This report is saved verbatim at /tmp/claude-0/-home-claude/b87888dd-2662-5ba9-857f-629ed606bf9c/scratchpad/u5/checker/out/report.md.

**Brief.** IA5's brief (units_data.py, `IA` entry "IA5", fifth field) read in full, with `PRE` and `AIMS["IA5"]`. No audit report exists for the course; errata step skipped.

## (1) Coverage

| Brief item | Status | Where |
|---|---|---|
| How to run a content inventory and audit (Halvorson and Rach; Spencer) and what to record per item | covered | sections 1.1, 1.2; figure 1 |
| Audience-, task- and topic-based structures and the case for each on a B2B software site | covered | sections 2.1 to 2.5; figure 2 |
| Page types versus pages; templates as the unit of IA on a site | covered | sections 3.1 to 3.3 |
| Depth, breadth, the home-page and landing-page problem | covered | sections 4.1 to 4.3 |
| Constraints: search-engine structure, campaign landing pages, localisation, pricing page, sign-up and log-in boundary, and how the sitemap records them | covered | sections 5.1 to 5.5; figure 3 |
| How a sitemap is read by marketing, engineering, a content writer; the fidelity each needs | covered | section 6; figure 4 |
| Figures: inventory structure; three candidates compared; chosen sitemap; template catalogue | covered | figures 1, 2, 6, 7 (plus a decision tree, an audit summary and a readers matrix: 7 figures, within the three-to-eight rule) |
| Deliverable: inventory (every page, type, audience, owner, status; Perqo facts labelled); sitemap in the notation; template catalogue (purpose, required and optional modules) | covered | Deliverables A, B, C |

Nothing thin or missing.

## Findings

1. [error] [attribution] section 2.1; Current: `a label such as "For employees" does not say whether the content is about the group or for it` (count 1); Problem: Sherwin's second problem is that a bare group label such as "Faculty" does not say whether the section is about the group or for it, and she says the opposite of the unit's example: "The simple addition of the preposition "for" clarifies the purpose and the contents of that category" and "Users are much more successful with audience navigation that includes the additional word(s) "for" or "Information for"". Attributing the ambiguity to a "For …" label reverses her point; Fix: `a bare group label such as "Faculty" does not say whether the content is about the group or for it (she notes that adding "for" clarifies it)`; Basis: Sherwin, "Audience-Based Navigation: 5 Reasons to Avoid It", NN/g, 7 September 2015, https://www.nngroup.com/articles/audience-based-navigation/ (fetched 3 November 2026).

2. [error] [deliverable] section 5.5; Current: `Three routes cross the boundary, and the sitemap draws each as IA2's `external` tag with a "→ see" note (IA2, section 5.2):` (count 1); Problem: the sitemap in Deliverable B draws only Sign in (S-5) as `external`; Book a demo is `form` (S-4) and Get the Perqo app is `detail` (S-6), and the inventory A.1 gives the same types. The text contradicts its own deliverable; Fix: `Three routes cross the boundary. The one that leaves the site, Sign in, is drawn with IA2's `external` tag and a "→ see" note (IA2, section 5.2); the other two stay on perqo.com and are drawn as its pages:`; Basis: K/unit.md, Deliverable A.1 rows S-4, S-5, S-6 and the sitemap JSON (types `form`, `external`, `detail`); IA2, section 5.2 (`external` = leaves this surface).

3. [should-fix] [deliverable] Deliverable A, "What the inventory hands on"; Current: `IA8 takes the external rows (S-5, S-6) as perqo.com's crossings in its surface layer` (count 1); Problem: S-6 is typed `detail` in A.1, not `external`; only S-5 is an external row; Fix: `IA8 takes the crossing rows (S-5, the one `external` row, and S-6, whose download links leave for the app stores) as perqo.com's crossings in its surface layer`; Basis: K/unit.md A.1 rows S-5 (`external`) and S-6 (`detail`).

4. [should-fix] [figure] figure 6 (sitemap), Deliverable B; Current: `"note": "S-6 · T-06 · footer · → see app stores"` (count 1); Problem: in IA2's notation "→ see" means "continues in another figure or node" (IA2, notation sheet, Labels); the app stores are neither a figure nor a node of any course artefact, and S-6 is a perqo.com `detail` page whose outward links are module M-24, not a sitemap continuation; Fix: `"note": "S-6 · T-06 · footer"`; Basis: IA2, section 5.1 ("Continuation point: a note "→ see" and the name of the figure or node it continues in") and the notation sheet.

5. [should-fix] [figure] figure 4 (readers matrix), section 6; Current: `"cells": ["top level, labels, Pricing, Customers, Book a demo, campaigns", "F1 or F2", "the label checks (B.2)"]` (count 1); Problem: the cell "the label checks (B.2)" adds a fact the section's text does not state: the Marketing paragraph says what marketing reads for and the fidelity, and never says it also needs B.2; Fix (to the text, keeping the cell): replace `F1 or F2 is enough; marketing argues about the top two levels, and the page-by-page detail would hide the argument.` (count 1) with `F1 or F2 is enough; marketing argues about the top two levels, and the page-by-page detail would hide the argument. What it also needs is the label table (B.2), because the labels are what it argues about.`; Basis: sourcing-standard Part 1, "A figure adds no fact".

6. [minor] [style] Unsure list; Current: `- Spencer 2014: chapter titles and order from the edition's front matter in an excerpt; the content of chs 11 to 16 was not seen, so no claim is made about what they recommend beyond their order.` (count 1); Problem: the body cites chapters 11 to 15 (part 3) and the Sources entry says "chs 11 to 15"; chapter 16, "IA Patterns", opens part 4 and is not cited; Fix: `- Spencer 2014: chapter titles and order from the edition's front matter in an excerpt; the content of chs 11 to 15 was not seen, so no claim is made about what they recommend beyond their order.`; Basis: the edition's excerpt at uxmastery.com (PracticalIA.pdf, returned by search; contents list part 3 "Understanding content" as Content You Have, Content You Need, Communicating About Content, Content Planning, Classification Schemes, then IA Patterns in part 4).

7. [minor] [style] Sources and section 5.1; Current: `[developers.google.com/search/docs/advanced/crawling/block-indexing](https://developers.google.com/search/docs/advanced/crawling/block-indexing)` (count 1); Problem: the page's canonical address (its canonical and og:url tags, as the fetch reported) is `/search/docs/crawling-indexing/block-indexing`; the `/advanced/crawling/` path is the old one; Fix: `[developers.google.com/search/docs/crawling-indexing/block-indexing](https://developers.google.com/search/docs/crawling-indexing/block-indexing)` (and the same path in the section 5.1 link); Basis: Google Search Central, "Block Search indexing with noindex", last updated 2025-12-10, fetched 3 November 2026 from the search-returned URL.

8. [minor] [figure] figure 1 (inventory structure), section 1.2; Current: `{"label": "Format", "tone": 1, "cells": ["inventory", "record", "record"]},` (count 1); Problem: the F3 column gives "record" for Format and for Audience, and the paragraph after the figure says what F3 does with ID, title, URL, owner, outcome, the structure fields, traffic and last-modified, but not with Format or Audience; the cells are status words, not labels or numbers, so this is not counted as an added fact; Fix (to the text): replace `traffic and last-modified dates are dropped, because the migration needs neither.` (count 1) with `format and audience are carried over as recorded; traffic and last-modified dates are dropped, because the migration needs neither.`; Basis: sourcing-standard Part 1, figure rule.

9. [minor] [figure] figure 6, Deliverable B.1; Current: `Footer pages are marked "footer": the footer is a route, outside the levels.` (count 1); Problem: "footer" is a new note word outside IA2's label rules; IA2's rule is "Keep the notation; extend the legend" (IA2, section 4), which the unit invokes for the status *new* in section 1.1 but not here; Fix: `Footer pages are marked "footer" in their notes: the footer is a route, outside the levels; the word is added to the figure's legend under IA2's rule "Keep the notation; extend the legend" (IA2, section 4).`; Basis: IA2, section 4.

10. [minor] [figure] figure 5 (audit summary), Deliverable A.4; Current: `{"kind": "matrix", "numeric": true, "tone": 1, "min": 0, "max": 15, "scale_label": "pages", "caption": "Audit summary:` (count 1); Problem: the fields `numeric`, `min`, `max` and `scale_label` appear in no filed unit's figure and kit/viz.py is not in K, so whether the matrix kind draws a shaded numeric matrix could not be verified; if it does not, the figure fails at build; Fix: none if viz.py accepts the fields; otherwise drop the four fields and keep the cells as plain numbers; Basis: filed units IA1 to IA4 (no numeric matrix); unverifiable here.

## Confirmed

- Kaley, "Content Inventory and Auditing 101", NN/g, 27 September 2020: quotes "fits your organization's needs and your team's capacity", "manageable yet impactful subset", "spreadsheets tend to work best for content inventories and audits"; fields title, URL, owner, topic, format, last-modified date, metadata, source files; keep/update/remove with an owner per update. PASS. https://www.nngroup.com/articles/content-audits/
- Halvorson and Rach, *Content Strategy for the Web*, 2nd ed., 2012, publisher's sample: ch. 5 "AUDIT. Take a close-up look at your current content", ch. 6 "ANALYSIS. Your content lives in a complicated world"; index entries quantitative inventories, qualitative audits (best practices assessment, strategic assessment), content sampling with the six factors, rolling audits; the nine audit-data items (index has "title/topics") and the ten qualitative factors. PASS (the unit says it cites the structure and field names only). https://ptgmedia.pearsoncmg.com/images/9780321808301/samplepages/0321808304.pdf
- Spencer, *A Practical Guide to Information Architecture*, 2nd ed., UX Mastery, 2014: part 3 "Understanding content"; Content You Have, Content You Need, Communicating About Content, Content Planning, Classification Schemes in that order (edition excerpt at uxmastery.com, search-returned). PASS. The unit's announcement link (uxmastery.com, 20 June 2014) confirms publisher and year. The store page redirects (302) and was not followed.
- Sherwin, NN/g, 7 September 2015: five problems; exact quotes "people don't always fall neatly into a single category, nor are they able to quickly self-identify", "the information they see might be incomplete or incorrect", "Only use audience-based navigation when the content truly justifies it"; secondary navigation; "mutually exclusive and jargon free". PASS except finding 1. https://www.nngroup.com/articles/audience-based-navigation/
- Richardson, Inside GOV.UK, 18 July 2014: users did not fit the three groups; "professionals" read as training; people feared content labelled for others was missing; recommendation "labels that describe the information contained in a topic, not labels based on audience type". PASS. https://insidegovuk.blog.gov.uk/2014/07/18/hey-you-there-the-trouble-with-audience-based-navigation/
- McGovern, "What Really Matters: Focusing on Top Tasks", Center Centre, 20 January 2016 (A List Apart, April 2015): exact quotes "the small set of tasks (usually less than 10, often less than five) that matter most to your customers", "three tasks got as much of the vote as the bottom 44", "over 400 times"; method long list, stakeholder shortlist, customer vote. PASS. https://articles.centercentre.com/?p=877
- European Commission, Europa Web Guide, task-based IA: adopted 2014; "it avoids making users think and potentially, hesitate"; "avoids content duplication and unnecessary maintenance costs"; undated. PASS. https://commission.europa.eu/resources-partners/europa-web-guide/planning-your-web-presence/architecture-and-navigation/task-based-information-architecture_en
- Loranger, NN/g, 1 December 2013: "Business customers report pricing as the top most needed piece of information online"; "In our studies, we watch participants go to competitors' sites when websites do not show prices"; typical scenarios, ranges; no sample sizes. PASS. https://www.nngroup.com/articles/show-price/
- Fessenden, NN/g, 1 September 2019: "Show the price; and if the price is variable, offer common pricing scenarios"; "the first site to show a price can anchor users' expectations"; "provide a reason why you are making the request" (form fields). PASS. https://www.nngroup.com/articles/b2b-trust-from-b2c/
- Google, "URL structure best practices", last updated 2026-10-21: readable words rather than long ID numbers; words in the audience's language; hyphens; trim unnecessary parameters; example.com/de/ for multi-regional sites. PASS. https://developers.google.com/search/docs/crawling-indexing/url-structure
- Google, "Redirects and Google Search", last updated 2026-04-14: "permanent server-side redirect whenever possible"; "a signal that the redirect target should be canonical". PASS. https://developers.google.com/search/docs/crawling-indexing/301-redirects
- Google, "Block Search indexing with noindex", last updated 2025-12-10: "regardless of whether other sites link to it", page dropped from results. PASS (path: finding 7). Fetched at the search-returned URL https://developers.google.com/search/docs/advanced/crawling/block-indexing
- Google, "Localized versions of your pages", last updated 2026-09-21: "Each language version must list itself as well as all other language versions"; "If two pages don't both point to each other, the tags will be ignored"; x-default as the fallback. PASS. https://developers.google.com/search/docs/specialty/international/localized-versions?authuser=4
- Frost, *Atomic Design*, 2016, outline: ch. 2 "Atomic Design Methodology"; "page-level documents"; "specific instances of a template"; "Replaces content structure with real representative content". PASS. https://atomicdesign.bradfrost.com/outline
- Krug, *Don't Make Me Think, Revisited*, 3rd ed., New Riders: ch. 7 "The Big Bang Theory of Web Design" (O'Reilly contents; release listed December 2013, the brief and IA3 give 2014). PASS on the chapter title; the chapter's argument is from memory, as the unsure list says. https://oreilly.com/library/view/dont-make-me/9780133597271
- Baker, *Every Page Is Page One*, XML Press, 2013: publisher and year confirmed by the XML Press announcement of 17 October 2013 (https://xmlpress.net/?p=2693). The quoted line "People don't arrive at your site, they arrive at your pages" could not be opened (the book's site was not returned by search): unverifiable.
- Cited through the filed units and checked against them (not reopened): Brown 2011 ch. 5 ("increasingly represent page types or templates in addition to (or instead of) specific pages", "one view") in IA2 §1.3 and IA1 §4; Cardello 2014 "Related Link" in IA2 §1.3; Tankala 2023 in IA1 §4; Rosenfeld, Morville and Arango ch. 13 content models in IA2 §1.5 and ch. 6 internal politics in IA3 §3.2; Nielsen 2003 patches in IA3 §1.1; Budiu 2020 scent on arrival in IA3 §1.2; Laubheimer 2023 and Nielsen 2009 in IA3 §1.2; Nielsen 2006 and Farrell 2017 in IA3 §4.2 and §5.2; Furnas 1987 in IA3 §4.2; Hearst 2006 in IA4 §3.2; Whitenton 2013 quote, Zaphiris 2000 (5 structures, 64 pages) and Larson and Czerwinski 1998 (512 documents, medium beat broadest shallow) in IA4 §2.1; Berners-Lee 1998 in IA4 §5; Sitemaps protocol in IA2 §1.3. All as the unit states them.

**Pointers to filed units, each confirmed:** IA1 §5 (shallow hierarchy; buyer "typically someone in HR or finance"; employees meet perqo.com for help and the download link); IA1 §2.3 (Help centre split by audience then task); IA1 §4 (deliverables name readers and decision; Tankala; Brown "one view"); IA1 Deliverable (top-level areas; perqo.com column Benefits budget, Card payments, Claims, Policies, Teams and groups; what crosses: contract and sign-in to Admin, download link and help to the app, invitations Admin to app); IA2 §1.0 (F1 to F3), §1.1 (inventory versus audit; URL-sorted inventory read as a sitemap; F2 before redesign, F3 as migration list), §1.3 (Brown; page types; Cardello; Sitemaps protocol; sitemap fidelities), §1.5 (content models), §4 (identifiers; "Keep the notation; extend the legend"), §5.1 (conditional area; "→ see"), §5.2 (tags; tones; tone 1 perqo.com), §5.3 (F2 sitemap; Book a demo added to global routes; inventory slice H-2.1.1, H-2.1.2 "refund", H-2.2.1 at /help/employees/balance, H-1.1.1, H-1.2.4 PDF owned by Product; search inside the Help centre), Deliverable (decision table rows for inventory and sitemap naming IA5); IA3 §1.1, §1.2, §3.2, §4.2, §5.2 (search log: "gym" zero results), §6.2, Deliverable (checklist A1 to A3, C2, D1 to D3; partnerships team's placings; merchants accept the card and publish offers); IA4 §1.1 (hybrid fails C1, layered passes), §1.2 (articles both audiences need listed under both), §2.1, §3.2, §4.3 (category stays a taxonomy term), §5 (addressing by identifier; Help centre redirects), Deliverable A (O-01, O-14 attributes audience and last modified, O-15, O-16 attributes and "not in Admin", R-19), Deliverable B (CAT identifiers; R5, R7, R9; "What IA5 and DD-IA3 take"). IA8, IA10 and DD-IA3 hand-ons match those units' briefs in units_data.py.

**Perqo labels and register.** First invented fact is labelled "(Perqo, fictional)" in section 1.3 (15 labels in the unit); the intro's mention of Perqo states nothing beyond IA1, the same pattern as IA3 and IA4. Every fact checked against perqo-facts.md and IA1 to IA4: surfaces and top-level areas, Book a demo among global routes, Help centre split and IA2's five inventory rows (kept, with H-2.2.1's move and H-1.2.4's replacement declared as extensions), perqo.com's vocabulary column, variant terms "allowance" and "refund", the search log's "gym", IA4's objects and attributes on perqo.com, F-CAT identifiers and rules R5, R7, R9, the merchant facts, the partnerships team's request. No contradiction. Nothing in "Not yet set" is breached: no named person or real client; customer stories are by sector only.

**Public-site rules.** No personal fact about the reader; no private person named (Pedro, Porto, ADHD, employer: 0 occurrences each).

**Labels (Part 4).** McGovern labelled practice and a consultant's own data; EC institutional guidance; Google vendor documentation with dates; Krug, Baker and Richardson practice; Loranger and Fessenden NN/g guidance from observation without figures; Sherwin NN/g guidance. Every number says whose it is (McGovern's 400-plus and Cisco; Zaphiris and Larson and Czerwinski through IA4; the unit's own 52, 17, 27, 57, 42). No vendor guidance cited as a study. No anecdote presented as evidence.

**Deliverable (5).** Present in full: A (57 rows in three tables, with type, template, audience, owner, F-CAT, status; A.4 totals), B (sitemap JSON in the notation; B.2 label table; B.3 trace), C (27 modules, 17 templates with purpose, required and optional modules, builds, localisation). Each follows from the sections (scheme from 2.4, templates from 3.2 and 3.3, campaign and localisation rules from 5.2 and 5.3, pricing from 5.4, boundary from 5.5) and is usable alone with its face. Closing material adds no unsourced claim.

## (7) Figures

1. matrix, section 1.2 (inventory structure). Row labels: the 14 fields of the 1.2 table, each present there ("| ID |" … "| Indexed |"). Columns and F2/F3 cells: "At F2 … the inventory and audit fields are recorded and the audience is judged; the structure fields stay empty"; "At F3 … the ID is stable, the title and URL are the final ones, the owner is named, the outcome may also be new, and the structure fields carry a page-type tag, a template ID, CAT identifiers, a redirect target's ID and yes or no for indexing; traffic and last-modified dates are dropped". Caption names what it shows, section 1.2 and the sources. Kind: items by sections, matrix fits. Tone 1 throughout, one surface. PASS (finding 8 minor).
2. matrix, section 2 (three structures). Top-level cells from 2.1 ("For HR teams, For finance teams, For employees, For merchants"), 2.2 ("See how it works, Check the price, Read customer stories, Get help, Book a demo"), 2.3 ("Product, Pricing, Customers, Help centre, with Book a demo and Sign in"); "pick a role", "read a phrase", "pick a subject" from 2.1 to 2.3; "repeated under HR and finance" from 2.1 ("an audience top level would carry them twice"); "names a role", "verbs first" from 2.1 and 2.2; "Used on perqo.com for" row from 2.4. Tone 6 marks faults, as IA2 sets. Caption names section 2 and the sources. Kind fits. PASS.
3. decision, section 5.2. Four questions and outcomes quoted from the paragraph "First: will the page outlive one campaign? … New page under its topic, with an ID and a template"; "yes" on the left; tone 1. Caption names section 5.2 and sources. A rule with branches: decision fits. PASS.
4. matrix, section 6 (readers). Rows Marketing, Engineering, Content writer and their "reads for" and fidelity cells from the three paragraphs; "inventory: URL, redirect, indexed" from "the inventory carries the URL, redirect and index columns"; "inventory row and template entry" from "the writer's real document is the inventory row plus the template entry". Cell "the label checks (B.2)" is not in the text: FIX, finding 5 (text addition given there). Caption names section 6 and sources; kind fits.
5. matrix (numeric), Deliverable A.4. Cells 15, 6, 3, 5 / 1, 0, 1, 0 / 12, 3, 1, 10 equal the A.4 table and my recount of A.1 to A.3. Caption names A.4, Kaley and the tables. Kind: counts by area and outcome, a two-way table: matrix fits (compare would lose one dimension). PASS; finding 10 minor on the unverified fields.
6. sitemap, Deliverable B. Every label, type, ID and template traced to A.1 to A.3 (S-0 to S-12 except removed S-1.6, S-1.7, S-3.4; L-01; H-0 to H-2.3.2 except removed H-1.2.4), stacks named in B.1 ("The three legal pages are drawn as one stack, Legal pages"; article stacks by topic), "[campaign live]" from 5.2, "→ see Perqo Admin" from 5.5, "stack_from": 2 as IA2. Tone 1 everywhere, tags from IA2's closed list. Caption names Deliverable B, IA1 §2.3, IA2 §5.3 and Deliverable A. FIX: finding 4 (the "→ see app stores" note); finding 9 minor.
7. matrix, Deliverable C (template catalogue). All 17 rows and 7 columns cross-checked by script against C.2's required and optional columns (M-01, M-04, M-03, M-05, M-13, M-18, M-02): 0 mismatches. Legend declares req and opt. Caption names Deliverable C and sources. Kind fits. PASS.

## Counts re-run by script

- Inventory rows: A.1 29 (keep 15, update 6, remove 3, new 5); A.2 2 (1, 0, 1, 0); A.3 26 (12, 3, 1, 10); total 57 (28, 9, 5, 15): all equal the A.4 table and figure 5.
- Rows on the site today (not new): 42; after the redesign (not removed): 52: both as stated in A.4, section 3.2 and the facts table.
- Templates in C.2: 17; modules in C.1: 27; every module is used by at least one template and every module used is defined; every template ID in A.1 to A.3 exists in C.2 and the "Builds" column matches the inventory for all 17 (T-08 builds S-3.1 to S-3.3 after S-3.4's removal; T-12 builds L-01 after L-02's removal).
- Figures: 7 viz blocks, all valid JSON (kinds matrix, matrix, decision, matrix, matrix, sitemap, matrix).
- Fields table in 1.2: 14 rows, equal to figure 1's 14 rows. B.2 label table: 11 rows. B.3 trace: 5 rows. Facts table: 18 rows. "(Perqo, fictional" labels: 15.
- Depth: deepest path Home → Help centre → For employees → Claims → article = four levels below Home; every buyer page within three (S-1.4.x at three); Product's list five items (Perqo Admin, Perqo app, Perqo card, Benefits, Security): all as stated in 4.1.
- Word count: the unit states none. Measured: 13,608 words in all; 7,463 excluding viz blocks and tables; 6,496 excluding also Sources, the facts table and the unsure list. PRE's 2,000–6,000 guide is exceeded by the prose alone by about 500 words and by the deliverables' tables, which the brief asks for in full; not raised as a finding.

## Verdict

IA5 · **fix** · errors 2, should-fix 3, minor 5. Checked by Fable 5.1 (claude-fable-5-1), so no separate Fable 5.1 fresh check is owed.

---

## Maintainer's note (U-5 chat, 3 November 2026)

Every finding was verified before it was applied, then applied by script as an exact replacement (each `Current:` counted once in the vault file, finding 7's twice as the finding says: Sources and section 5.1).

- Finding 1 (error): verified against the source under the web rule (a search returned https://www.nngroup.com/articles/audience-based-navigation/, fetched as returned): problem 2 is the bare label "Faculty" and the "for" advice sits under the article's mitigation tips. Applied as given.
- Finding 2 (error): verified against Deliverable A.1 (S-4 `form`, S-5 `external`, S-6 `detail`) and the sitemap JSON. Applied as given.
- Finding 3 (should-fix): verified the same way. Applied as given.
- Finding 4 (should-fix, figure 6): verified against IA2's continuation-point rule (section 5.1 and the notation sheet). Applied as given; figure 6 re-checked by a new agent (report below).
- Finding 5 (should-fix, figure 4): verified that section 6's Marketing paragraph did not state the B.2 cell; the text addition applied as given, the cell kept; figure 4 re-checked by a new agent (report below).
- Finding 6 (minor): verified against the Sources entry ("chs 11 to 15"). Applied as given.
- Finding 7 (minor): verified under the web rule (a search returned https://developers.google.com/search/docs/advanced/crawling/block-indexing; the fetch reported og:url `/search/docs/crawling-indexing/block-indexing`, last updated 2025-12-10). Applied in both places.
- Finding 8 (minor): verified against section 1.2's paragraph. Applied as given.
- Finding 9 (minor): holds in part. The sitemap kind in `kit/viz.py` carries no legend field, so the proposed sentence ("added to the figure's legend") could not be made true. Applied as far as it holds: the B.1 sentence says the word extends IA2's note vocabulary under its rule (IA2, section 4) and that the caption declares it; figure 6's caption now says what "footer" marks.
- Finding 10 (minor): does not call for a change. `kit/viz.py`'s docstring documents the matrix kind with `"numeric": true`, `min`, `max` and `scale_label` (P44, 29 Oct 2026); the figure rendered at build. Nothing changed.

---

## Figure 4 re-check 1 (Opus 5.5 agent, 3 November 2026; given the unit without its figures, the captions and the frames sheets; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

Note: writing F/out/report.md was refused by the harness ("Subagents should return findings as text, not write report files"), so the report exists only here, not on disk.

# Figure 4 re-check (IA5, matrix: readers of the perqo.com sitemap)

## Findings

- [minor] [figure]; Current: Marketing row, ALSO NEEDS cell "the label checks (B.2)"; Problem: the text never says "label checks". Its word is "the label table (B.2)". B.2's heading is "The labels, judged by IA3's checklist"; Fix: change the cell to "the label table (B.2)"; Basis: line 205, "What it also needs is the label table (B.2), because the labels are what it argues about."
- [minor] [figure]; Current: Engineering row, READS FOR cell "IDs, page types, templates, external routes"; Problem: the text calls what engineering reads "every `external` box", not "external routes". In section 5.5, "routes" means all three boundary crossings, and two of them stay on the site. The cell leaves out the "URLs, redirects, indexed" that line 207 lists. That part stands, because the figure puts them under ALSO NEEDS and line 207 supports that ("the inventory carries the URL, redirect and index columns the drawing has no room for"); Fix: change "external routes" to "external boxes"; Basis: line 207, "every box's ID, page type and template, the URLs, the redirects, which pages are indexed, and every `external` box"; line 193, "Three routes cross the boundary. The one that leaves the site, Sign in, is drawn with IA2's `external` tag".
- [minor] [figure]; Current: Content writer row, READS FOR cell "parent, template, owner, audience, F-CAT tags"; Problem: the cell leaves out the last item the text lists, "the word the site uses for each thing (IA1, Deliverable, the perqo.com column)"; Fix: make the cell "parent, template, owner, audience, F-CAT tags, site's words"; Basis: line 209.
- [minor] [caption]; Current: "'one view' from Brown, Communicating Design, 2nd ed., 2011, ch. 5"; Problem: the caption credits Brown for content the figure does not carry. Nothing in the figure draws on Brown's "one view"; the idea appears only in the paragraph after the figure (line 213); Fix: the caption becomes "Readers of the perqo.com sitemap: what each reads for, the fidelity each needs, and the artefact that carries what the drawing cannot; supports the decision on which version of the sitemap goes to whom (section 6). Fidelities from IA2, sections 1.0 and 1.3; detail left out on purpose from Tankala, NN/g, 2023. Every row tone 1, perqo.com. Perqo is fictional."; Basis: line 213; captions.md, Figure 4.
- [minor] [text]; Current: line 205 says for marketing "F1 or F2 is enough", and line 213 says "the F1 version for marketing is the same drawing cut to two levels"; Problem: the figure follows line 205 ("F1 or F2"), but line 213 narrows marketing to F1 alone, so the two lines disagree; Fix: in line 213, change "the F1 version for marketing" to "the F1 or F2 version for marketing"; Basis: lines 205 and 213.

## Confirmed

- Row "Marketing": READS FOR "top level, labels, Pricing, Customers, Book a demo, campaigns". Line 205: "the top level and its labels, the place of Pricing, Customers and Book a demo, and where campaigns go".
- Marketing FIDELITY "F1 or F2". Line 205: "F1 or F2 is enough".
- Engineering FIDELITY "F3". Line 207: "Only F3 serves".
- Engineering ALSO NEEDS "inventory: URL, redirect, indexed". Line 207: "the inventory carries the URL, redirect and index columns the drawing has no room for". The field name "Indexed" is from line 61.
- Content writer FIDELITY "F2". Line 209: "F2 is the drawing's level".
- Content writer ALSO NEEDS "inventory row and template entry". Line 209: "the writer's real document is the inventory row plus the template entry".
- Three readers, in the text's order. Line 203: "the three readers who use the sitemap most are marketing, engineering and the content writer".
- F1, F2 and F3 as IA2's fidelities. Line 203: "IA2 set three fidelities, F1 sketch, F2 working and F3 specification ... (IA1, section 4; IA2, sections 1.0 and 1.3)".
- The caption names the section "(section 6)". The figure sits in section 6 (line 211).
- The caption says what the figure shows and names the decision it supports; each part matches the three columns.
- Caption source "Fidelities from IA2, sections 1.0 and 1.3". Line 203.
- Caption source "detail left out on purpose from Tankala, NN/g, 2023". Line 205: "Tankala's point that a sitemap leaves detail out on purpose ... (Tankala, NN/g, 2023 ...)". Sources list, line 447: Tankala, NN/g, 3 September 2023.
- Kind: matrix is right. Readers are rows against three attributes (items by sections), with no dates, sequence, hierarchy or numbers.
- Notation: every cell uses one tone in each theme, which fits "Every row tone 1, perqo.com". Line 12: "on a figure of one surface every box takes that surface's tone, so every perqo.com box is tone 1". The figure has no tags or notes for any other rule to apply to.
- Drawing, desktop (desktop-read-ux-ia5-fig-04-matrix-dark.png, -light.png, -frames-dark.png, -frames-light.png): frame 1 of 1. Text sits inside its cells, nothing overlaps or is cut, and the caption is under the figure in both themes.
- Drawing, tablet (tablet-read-ux-ia5-fig-04-matrix-dark.png, -light.png, -frames-dark.png, -frames-light.png): frame 1 of 1. The same holds, and the longest cell, "inventory: URL, redirect, indexed", fits inside its box.
- Drawing, phone (phone-read-ux-ia5-fig-04-matrix-dark.png, -light.png, -frames-dark.png, -frames-light.png): the figure scrolls in its frame (frames 1 to 4, 0 to 372 px) with the hint "scroll sideways for the whole figure". The label column (Marketing, Engineering, Content writer) stays in view in every frame. The scroll edge fades rather than cuts. Every cell can be read across frames 1 to 4, and the caption is under the figure in both themes.

Figure 4: PASS (error 0, should-fix 0, minor 5)

---

## Figure 6 re-check 1 (Opus 5.5 agent, 3 November 2026; same packet; verbatim hand-back; the harness refused its `out/` write)

Note: I could not save F/out/report.md. The harness blocked the write ("Subagents should return findings as text, not write report files"). The report below is the full text meant for that file.

# Figure 6 (sitemap) re-check · IA5

## Findings

1. [error] [figure]; Current: Customer stories note "S-3.1 to S-3.3 · T-08 · one per client"; Problem: "one per client" sets a rule the text does not state: at most one story per client. The text says only that each story is about a client ("a customer story is about a client (IA4, Deliverable A, R-19)"; T-08 "one client's story"). Fix: change the note to "S-3.1 to S-3.3 · T-08 · one client's story each", or end it at "T-08"; Basis: unit line 75; C.2 row T-08 (line 401); M-09 "R-19: a story is about a client" (line 370).

2. [should-fix] [figure]; Current: "Get the Perqo app" (DETAIL, "S-6 · T-06 · footer") sits in the second row from Home's trunk, beside Help centre, Book a demo and Sign in. The other footer pages (For merchants, About Perqo, Contact, Legal pages) are in a separate row below the Help centre; Problem: the text puts the footer "outside the levels", and Get the Perqo app is one of the footer routes. Drawn in the row of global routes, it reads as a seventh level-1 route, against "Home, its six global routes" in the caption and M-01's six items. It also splits the footer pages into two groups; Fix: move the Get the Perqo app box out of the Help centre / Book a demo / Sign in row and into the footer row as its first box, so the footer row reads Get the Perqo app, For merchants, About Perqo, Contact, Legal pages (M-02's order); Basis: line 316 "the footer is a route, outside the levels"; M-02 "Get the Perqo app, For merchants, About Perqo, Contact, the three legal pages" (line 363); M-01 (line 362); B.2 "'Get' is the only verb in the footer" (line 334); images desktop-…-frames-light.png, tablet-…-frames-light.png.

3. [minor] [caption]; Current: "an ID and a template in every note"; Problem: the Sign in note is "S-5 · → see Perqo Admin" and has no template, because S-5's template is "none". The caption overstates it; Fix: "an ID in every note and a template in every note but the external box's"; or the full caption opening: "Sitemap: perqo.com as redesigned, F3, page types tagged, an ID in every note and a template in every note but Sign in's, many pages of one type drawn as one stack; …"; Basis: A.1 row S-5 "external | none" (line 246).

4. [minor] [text]; Current: B face "with an ID and a template on every box" (line 312), and B.1 "Each box's note gives its ID and template" (line 316); Problem: the same overstatement as finding 3. Sign in has no template; Fix: "with an ID on every box and a template on every box but the external one"; Basis: line 246.

5. [minor] [notation]; Current: "STACK · Approval articles · H-1.3.1 · T-16"; Problem: the stack is IA2's mark for "many pages of one type drawn as one stack", but this stack holds a single page (H-1.3 has one article). Every other article stack holds two or more; Fix: either redraw it as "DETAIL · Approving and rejecting claims · H-1.3.1 · T-16", or keep the stack and accept it as a stack that will grow (no text change needed). The first keeps the notation strict; Basis: line 120; A.3 row H-1.3.1 (line 279).

6. [minor] [drawing]; Current: in desktop-read-ux-ia5-fig-06-sitemap-light.png and desktop-read-ux-ia5-fig-06-sitemap-dark.png, the opening frame starts with the Home box hidden under the page's sticky "Section 8 of 10" bar; Problem: on desktop a reader landing on the figure does not see its root. The frames sheets show Home intact, so the figure itself is not cut. This is the page's scroll offset under the sticky header; Fix: give the figure a scroll-margin-top at least the sticky bar's height (in theme.css), or check whether this is only an artefact of the capture; Basis: the two desktop opening-frame images; compare desktop-…-frames-*.png.

7. [minor] [notation]; Current: the Campaign pages stack "[campaign live] L-01 · T-12 · no navigation" hangs from Home's trunk by a connector, like the other children; Problem: the text says campaign pages "appear in no navigation" and are "off the hierarchy" (T-12). A solid parent line from Home can read as a navigation route. The bracketed condition and "no navigation" do state the exception, so this is not wrong under IA2's conditional-area rule as the unit quotes it; Fix: optional. Draw the connector dashed, or leave the box unconnected below the footer row; Basis: line 173; line 175; C.2 row T-12 (line 405).

## Confirmed

- Kind: a hierarchy drawn as a sitemap, the right kind. Line 120: "a structural sitemap's box is a page type or a group, with many pages of one type drawn as one stack".
- HOME · Home · S-0 · T-01: line 225 "S-0 | Home | / | home | T-01".
- Six global routes under Home (Product, Pricing, Customers, Help centre, Book a demo, Sign in): line 316 "Home over Product, Pricing, Customers, Help centre, Book a demo and Sign in"; M-01, line 362.
- SECTION · Product · S-1 · T-02: line 226.
- DETAIL · Perqo Admin S-1.1, Perqo app S-1.2 and Perqo card S-1.3, each T-03: lines 227 to 229.
- SECTION · Benefits · S-1.4 · T-02: line 230.
- DETAIL · Health S-1.4.1 · T-04 · CAT-HEA; Learning S-1.4.2 · T-04 · CAT-LEA; Mobility S-1.4.3 · T-04 · CAT-MOB; Meals S-1.4.4 · T-04 · CAT-MEA: lines 231 to 234.
- DETAIL · Security · S-1.5 · T-06: line 235.
- Product holds five items (Admin, app, card, Benefits, Security): line 145 "keeps Product's own list at five short items".
- DETAIL · Pricing · S-2 · T-05, at level 1: line 238; line 189 "Pricing stays a level-1 page in the global header".
- INDEX · Customers · S-3 · T-07: line 239.
- STACK · Customer stories · S-3.1 to S-3.3 · T-08: lines 240 to 242. S-3.4 is removed and not drawn (line 243).
- FORM · Book a demo · S-4 · T-09: line 244.
- DETAIL · Demo request received · S-4.1 · T-10: line 245.
- EXTERNAL · Sign in · S-5 · "→ see Perqo Admin": line 246 "leaves for Perqo Admin | external"; line 193 "drawn with IA2's `external` tag and a '→ see' note".
- DETAIL · Get the Perqo app · S-6 · T-06 · footer: line 247; M-02, line 363.
- DETAIL · For merchants · S-7 · T-06 · footer: line 248; line 114 "reached from the footer".
- DETAIL · About Perqo · S-8 · T-06 · footer: line 249; M-02.
- FORM · Contact · S-9 · T-09 · footer: line 250; M-02.
- STACK · Legal pages · S-10 to S-12 · T-11 · footer: lines 251 to 253; line 316 "The three legal pages are drawn as one stack, Legal pages".
- STACK · Campaign pages · "[campaign live]" · L-01 · T-12 · "no navigation": line 175 "one box tagged `stack` whose note opens with the condition in square brackets, '[campaign live]'"; line 173 "appears in no navigation, uses the campaign template (T-12)"; line 259 L-01. L-02 is removed and not drawn (line 260).
- INDEX · Help centre · H-0 · T-13: line 266.
- INDEX · Search results · H-0.1 · T-14: line 267.
- SECTION · For HR and finance teams · H-1 · T-15: line 268.
- SECTION · Budgets · H-1.1 · T-15; STACK · Budget articles · H-1.1.1, H-1.1.2 · T-16: lines 269 to 271.
- SECTION · Policies · H-1.2 · T-15; STACK · Policy articles · H-1.2.1 to H-1.2.3, H-1.2.5 · T-16; H-1.2.5 also listed under Claims: lines 272 to 277 (H-1.2.4 is removed and not drawn); line 277 "also listed under H-2.1"; line 293 "the Claims section lists it".
- SECTION · Approvals · H-1.3 · T-15; H-1.3.1 · T-16: lines 278 and 279.
- SECTION · For employees · H-2 · T-15: line 280.
- SECTION · Claims · H-2.1 · T-15; STACK · Claim articles · H-2.1.1 to H-2.1.4 · T-16; also lists H-1.2.5: lines 281 to 285; line 293.
- SECTION · Balance · H-2.2 · T-15; STACK · Balance articles · H-2.2.1, H-2.2.2 · T-16: lines 286 to 288.
- SECTION · Card · H-2.3 · T-15; STACK · Card articles · H-2.3.1, H-2.3.2 · T-16: lines 289 to 291.
- Deepest path, four levels below Home (Help centre, For employees, Claims, article): line 145.
- Help centre drawn by audience, then by task: line 108; line 145 "keeps IA1's two levels, audience then task".
- Every page type tag is from IA2's closed list (home, section, index, detail, stack, form, external): line 120.
- Every box is one tone (tone 1, perqo.com) in both themes: line 12 "every perqo.com box is tone 1"; caption.
- Removed pages are not drawn (S-1.6, S-1.7, S-3.4, L-02, H-1.2.4): B face, line 312 "leaves out: removed pages".
- Every additional box that B.1 lists is drawn: Benefits with four category pages, Security, the demo confirmation, the footer pages, Approvals, Card, search results and the campaign stack (line 316).
- Caption: it says what the figure shows (F3, tags, IDs, templates, stacks), names the section (Deliverable B) and the sources (IA1, section 2.3; IA2, section 5.3; Deliverable A), declares the word "footer" under IA2's rule, section 4 (line 316), and gives the bracketed-note and "→ see" conventions (lines 175 and 193).
- Drawing, desktop and tablet, light and dark (desktop-…-frames-light/dark.png, tablet-…-frames-light/dark.png and tablet-…-sitemap-light/dark.png): the whole figure fits in one frame; text sits inside every box; no overlaps; nothing cut; the caption is under the figure.
- Drawing, phone, light and dark (phone-…-sitemap-light/dark.png, phone-…-frames-light/dark.png): the figure is wider than its frame and scrolls sideways inside it, with the hint "scroll sideways for the whole figure"; across the four frames every box is shown whole at least once (Home, Pricing, Customers and Customer stories, Sign in, Get the Perqo app, Contact, Legal pages, Campaign pages); text sits inside its boxes; no overlaps; the caption is under the figure in every frame. No label column applies, since this is not a matrix.

Figure 6: FIX (error 1, should-fix 1, minor 5)

### Maintainer's note on the re-checks

Figure 4: PASS with five minor findings, all verified against the text and applied: the Marketing cell reads "the label table (B.2)", the Engineering cell "external boxes", the Content writer cell adds "site's words", the caption no longer credits Brown for content the figure does not draw, and section 6's "F1 version for marketing" reads "F1 or F2 version".

Figure 6: FIX. Finding 1 (error, "one per client"): the count is IA2's registered fact (IA2, section 5.3: "one page per client"; the register's perqo.com section), cited in IA5 only through IA4's R-19; applied by stating it in B.1 with its pointer ("Customers over a stack of customer stories, one page per client (IA2, section 5.3)"), so the note is traced to the text and IA2's fact is kept. Finding 2 (should-fix, Get the Perqo app in the row of global routes): holds in part. The sitemap kind in `kit/viz.py` draws the root's children in rows that wrap by width and has no row control, so the row a box lands in is not a level and cannot be set from the declaration; the footer pages are told apart by their notes, as B.1 says. Applied as far as it holds: the caption now says the five footer pages are Home's children like the six global routes and that only their notes tell them apart. Findings 3 and 4 (minor, "a template in every note"): applied to the caption, the face and B.1. Finding 5 (minor, a one-page stack): applied, the Approvals topic's one article drawn as the page "Approving and rejecting claims" (detail, H-1.3.1 · T-16). Finding 6 (minor, the desktop opening frame): not a fault of the page: the opening-frame shot scrolls the figure's top to the viewport's top, where the sticky section bar sits, which is how a figure taller than the viewport is captured; the frames sheets show Home whole, and a reader scrolling meets the root before the bar covers it. Finding 7 (optional, the campaign stack's connector): not applied; IA2's conditional-area rule is met by the bracketed note, as the finding itself says. Figure 6 was then checked a third time by a new agent (report below).

---

## Figure 6 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of the figure; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write)

# IA5 · Figure 6 (sitemap) · fresh figure check

Read: unit-text-without-figures.md (all 488 lines), captions.md, all 12 PNGs. I split the two phone frame sheets (1074×32976) into nine strips each to read them. The harness refused the write to F/out/report.md ("Subagents should return findings as text, not write report files"), so this reply is the only copy of the report.

## Findings

- [should-fix] [caption]; Current: "the five footer pages are Home's children like the six global routes"; Problem: the footer holds seven pages, not five. M-02 lists "Get the Perqo app, For merchants, About Perqo, Contact, the three legal pages", and B.1 says "The three legal pages are drawn as one stack, Legal pages". The figure draws five footer *boxes*: Get the Perqo app, For merchants, About Perqo, Contact and Legal pages (S-10 to S-12). So the caption's count clashes with the text; Fix: replace with "the five footer boxes (seven pages, the three legal pages drawn as one stack) are Home's children like the six global routes"; Basis: unit text, C.1 M-02 row; B.1 "The three legal pages are drawn as one stack, Legal pages."; every image, bottom row plus Get the Perqo app.
- [minor] [caption | notation]; Current: the Campaign pages stack ("[campaign live] · L-01 · T-12 · no navigation") hangs from Home's trunk, the same way as the routes; the caption explains this only for the footer pages; Problem: section 5.2 says a campaign page "appears in no navigation", and T-12 is "off the hierarchy". Drawn as a child of Home, it looks like a level-1 page. Its note says "no navigation", but the caption does not say why the box hangs from Home; Fix: after "...and only their notes tell them apart." add "The Campaign pages stack hangs from Home for the same reason; its note, 'no navigation', marks it as off the hierarchy."; Basis: unit text 5.2 "appears in no navigation"; C.2 T-12 "off the hierarchy, noindex"; desktop-read-ux-ia5-fig-06-sitemap-frames-light.png, bottom box.
- [minor] [figure]; Current: stack box labels "Budget articles", "Policy articles", "Claim articles", "Balance articles", "Card articles"; Problem: the text never uses these group names. It names the topics (Budgets, Policies, Claims, Balance, Card) and the articles one by one in A.3. The labels are descriptive and correct for the IDs they hold, so no error stands, but strictly they are words the figure adds; Fix: none required. Optionally, add to B.1's list "each topic's articles drawn as one stack, '<topic> articles'"; Basis: unit text B.1; A.3.
- [minor] [drawing]; Current: desktop-read-ux-ia5-fig-06-sitemap-light.png and -dark.png, the opening frame, show the figure from the Product/Pricing/Customers row down. The page's sticky header ("Section 8 of 10 · Deliverable · B · The perqo.com sitemap") covers the Home box; Problem: in that frame the root is hidden under the header. The frames sheets show Home in full, so this is the capture's scroll position, not the figure; Fix: none to the figure. If it is the build's default anchor, offset the figure's scroll target by the sticky header's height; Basis: desktop-read-ux-ia5-fig-06-sitemap-light.png, desktop-read-ux-ia5-fig-06-sitemap-dark.png against desktop-read-ux-ia5-fig-06-sitemap-frames-light.png and -frames-dark.png.
- [minor] [text]; Current: B's face reads "readers: marketing (cut to two levels, F1), engineering (F3), content (F2)"; Problem: section 6 says marketing needs "F1 or F2". The face fixes F1. This is not a fault in the figure, but the figure's caption names Deliverable B, and the two lines differ; Fix: in B's face, "marketing (cut to two levels, F1 or F2)"; Basis: unit text section 6, "F1 or F2 is enough"; Deliverable B face.

## Confirmed

- Kind: sitemap for a page hierarchy. Right for "structural sitemap of perqo.com... at fidelity F3" (Deliverable B face).
- Caption names the section and the source: "(Deliverable B)", "from IA1, section 2.3, and IA2, section 5.3; the rest from Deliverable A". Matches B.1, "It extends IA2's F2 sitemap and keeps everything in it (IA2, section 5.3)".
- Caption "six global routes": M-01, "Product, Pricing, Customers, Help centre, Book a demo, Sign in".
- Caption "an ID in every note and a template in every note but Sign in's": B.1, "Each box's note gives its ID and template (Sign in, the external box, has no template)"; every box checked.
- Caption "'footer' in a note... a word added under IA2's rule, section 4": B.1, "the word extends IA2's note vocabulary under its rule 'Keep the notation; extend the legend' (IA2, section 4)".
- Caption "Removed pages are not drawn": B face, "leaves out: removed pages". S-1.6, S-1.7, S-3.4, H-1.2.4 and L-02 are absent.
- Caption "Every box is tone 1": section intro, "every perqo.com box is tone 1". Every box uses the one tone in both themes.
- HOME Home · S-0 · T-01: A.1 row S-0 "home | T-01".
- SECTION Product · S-1 · T-02: A.1 "S-1 | Product | /product | section | T-02".
- DETAIL Perqo Admin S-1.1, Perqo app S-1.2, Perqo card S-1.3, all T-03: A.1 rows S-1.1 to S-1.3, "detail | T-03".
- SECTION Benefits · S-1.4 · T-02: A.1 "S-1.4 | Benefits | ... | section | T-02".
- DETAIL Health S-1.4.1 · T-04 · CAT-HEA; Learning S-1.4.2 · CAT-LEA; Mobility S-1.4.3 · CAT-MOB; Meals S-1.4.4 · CAT-MEA: A.1 rows S-1.4.1 to S-1.4.4, "detail | T-04 | ... | CAT-HEA/LEA/MOB/MEA".
- DETAIL Security · S-1.5 · T-06: A.1 "S-1.5 | Security | ... | detail | T-06".
- DETAIL Pricing · S-2 · T-05: A.1 "S-2 | Pricing | /pricing | detail | T-05"; section 5.4, "Pricing stays a level-1 page".
- INDEX Customers · S-3 · T-07: A.1 "S-3 | Customers | /customers | index | T-07".
- STACK Customer stories · S-3.1 to S-3.3 · T-08 · one per client: A.1 rows S-3.1 to S-3.3, "T-08" (S-3.4 removed); B.1, "a stack of customer stories, one page per client".
- INDEX Help centre · H-0 · T-13: A.3 "H-0 | Help centre | / | index | T-13".
- INDEX Search results · H-0.1 · T-14: A.3 "H-0.1 | Search results | /search | index | T-14".
- SECTION For HR and finance teams · H-1 · T-15: A.3 row H-1.
- SECTION Budgets · H-1.1 · T-15, and STACK H-1.1.1, H-1.1.2 · T-16: A.3 rows H-1.1, H-1.1.1, H-1.1.2.
- SECTION Policies · H-1.2 · T-15, and STACK "H-1.2.1 to H-1.2.3, H-1.2.5 · T-16; H-1.2.5 also listed under Claims": A.3 rows H-1.2.1 to H-1.2.3, H-1.2.5 "new; also listed under H-2.1"; H-1.2.4 removed.
- SECTION Approvals · H-1.3 · T-15, and DETAIL Approving and rejecting claims · H-1.3.1 · T-16: A.3 rows H-1.3, H-1.3.1. One page, so it is drawn as a detail box, not a stack, which is right.
- SECTION For employees · H-2 · T-15: A.3 row H-2.
- SECTION Claims · H-2.1 · T-15, and STACK "H-2.1.1 to H-2.1.4 · T-16; also lists H-1.2.5": A.3 rows H-2.1 to H-2.1.4; A.3 note, "the Claims section lists it, so one page has one URL and two routes".
- SECTION Balance · H-2.2 · T-15, and STACK H-2.2.1, H-2.2.2 · T-16: A.3 rows H-2.2, H-2.2.1, H-2.2.2.
- SECTION Card · H-2.3 · T-15, and STACK H-2.3.1, H-2.3.2 · T-16: A.3 rows H-2.3 to H-2.3.2.
- FORM Book a demo · S-4 · T-09, and DETAIL Demo request received · S-4.1 · T-10: A.1 rows S-4, S-4.1; section 5.5, "a form (S-4) and a confirmation page (S-4.1)".
- EXTERNAL Sign in · S-5 · → see Perqo Admin: A.1 "S-5 | Sign in | leaves for Perqo Admin | external | none"; section 5.5, "drawn with IA2's `external` tag and a '→ see' note".
- DETAIL Get the Perqo app · S-6 · T-06 · footer: A.1 row S-6 "detail | T-06"; M-02 footer.
- DETAIL For merchants · S-7 · T-06 · footer: A.1 row S-7; section 2.5, "reached from the footer".
- DETAIL About Perqo · S-8 · T-06 · footer: A.1 row S-8; M-02.
- FORM Contact · S-9 · T-09 · footer: A.1 "S-9 | Contact | /contact | form | T-09"; M-02.
- STACK Legal pages · S-10 to S-12 · T-11 · footer: A.1 rows S-10 to S-12 "T-11"; B.1, "The three legal pages are drawn as one stack, Legal pages".
- STACK Campaign pages · [campaign live] · L-01 · T-12 · no navigation: section 5.2, "one box tagged `stack` whose note opens with the condition in square brackets, '[campaign live]'", and "appears in no navigation"; A.2, L-01 "T-12", L-02 removed.
- Depth: the deepest path is Home, Help centre, For employees, Claims, articles, matching 4.1, "its deepest path is four levels below Home (Home, Help centre, For employees, Claims, an article)".
- Count: the drawn IDs come to 26 S- pages, 1 L- page and 25 H- pages, 52 in all. This matches A.4, "the redesigned site has 52" (A.1: 29−3; A.2: 2−1; A.3: 26−1).
- Notation: every type tag is from IA2's closed list (home, section, index, detail, stack, form, external) per 3.1. Many pages of one type are drawn as one stack (3.1, IA2 section 1.3). One external box (5.5). A bracketed condition marks the conditional area (5.2). One tone throughout.
- Drawing, desktop (desktop-read-ux-ia5-fig-06-sitemap-frames-light.png and -frames-dark.png, "frame 1 of 1 (the whole figure fits)"): text sits inside every box; nothing overlaps or is cut; the caption is under the figure.
- Drawing, tablet (tablet-read-ux-ia5-fig-06-sitemap-light/dark.png and -frames-light/dark.png, "the whole figure fits"): same; no fault.
- Drawing, phone (phone-read-ux-ia5-fig-06-sitemap-light/dark.png and -frames-light/dark.png, frames 1 to 4 of 4, scrolled 5 to 372 px): the figure scrolls sideways inside its frame, with the hint "scroll sideways for the whole figure". Boxes are cut only at the frame edge, with a fade, and appear whole in another frame:
  - frame 1: Product and its children, the Help centre tree, For merchants, About Perqo
  - frame 2: Home, Pricing, Book a demo, Demo request received, Contact, Campaign pages
  - frame 3: Customers, Customer stories, Sign in, Legal pages
  - frame 4: Customers, Customer stories, Sign in, Get the Perqo app, Legal pages

  Text stays inside boxes and the caption is under the figure in every frame, in both themes. There is no matrix, so the label-column rule does not apply.

Figure 6: FIX (error 0, should-fix 1, minor 4)

---

## Figure 6 re-check 3 (Opus 5.5 agent, 3 November 2026; the fourth check of the figure; same packet; verbatim hand-back; the harness refused its `out/` write)

Figure 6 passes. It has no errors and no should-fix findings; there are three minor findings. I could not save this report to F/out/report.md because the tool blocked the file write, so this reply is the report.

# IA5 · Figure 6 (sitemap) · fresh figure check

## Findings

- [minor] [notation]; Current: Home's second row of children reads "Help centre · Book a demo · Sign in · Get the Perqo app", and the other four footer boxes ("For merchants · About Perqo · Contact · Legal pages") sit on the next row. Get the Perqo app is a footer page ("S-6 · T-06 · footer") but it is drawn beside the global routes. Problem: the caption says "only their notes tell them apart", and that is true. But the placement puts one footer box among the six global routes and splits the five footer boxes, so a reader scanning by position can take Get the Perqo app for a seventh header route. Fix: order Home's children as the six global routes first (Product, Pricing, Customers, Help centre, Book a demo, Sign in), then the five footer boxes together in M-02's order (Get the Perqo app, For merchants, About Perqo, Contact, Legal pages), then Campaign pages. Basis: C.1, M-02 "Get the Perqo app, For merchants, About Perqo, Contact, the three legal pages | the footer routes (Deliverable B)"; M-01 "Product, Pricing, Customers, Help centre, Book a demo, Sign in"; desktop/tablet-...-frames-light/dark.png, row 2 against row 3.
- [minor] [caption]; Current: "'footer' in a note marks a page reached from the footer, outside the levels (a word added under IA2's rule, section 4)". Problem: "section 4" can be read as this unit's section 4 (Depth, breadth…), which has nothing to do with the rule. B.1 cites it as "(IA2, section 4)". Fix: "(a word added under IA2's rule 'Keep the notation; extend the legend', IA2, section 4)". Basis: B.1 "the word extends IA2's note vocabulary under its rule 'Keep the notation; extend the legend' (IA2, section 4)".
- [minor] [drawing]; Current: on the phone, the figure opens scrolled to 5 of 372 px. The root box shows only "HOME Home S-0 ·", cut at the frame's right edge, and Pricing shows only "DET Pri S-2". Problem: the figure does scroll in its frame, and the note "scroll sideways for the whole figure" sits under it. Nothing is lost; frames 2 to 4 show Home, Pricing, Customers, Sign in and Get the Perqo app whole. But the reader's first view of a tree cuts its root. Fix: open the phone frame scrolled so the Home box is fully in view (about 169 px, as in frame 2), or draw the root left-aligned over its first child. Basis: phone-read-ux-ia5-fig-06-sitemap-light.png, phone-read-ux-ia5-fig-06-sitemap-dark.png, phone-...-frames-light/dark.png frame 1 against frame 2.

## Confirmed

(a) Every box traced to the unit's text:
- HOME, Home, S-0 · T-01. Basis: A.1 "S-0 | Home | / | home | T-01".
- SECTION, Product, S-1 · T-02. Basis: A.1 "S-1 | Product | /product | section | T-02".
- DETAIL, Perqo Admin / Perqo app / Perqo card, S-1.1 / S-1.2 / S-1.3 · T-03. Basis: A.1 rows S-1.1 to S-1.3, "detail | T-03".
- SECTION, Benefits, S-1.4 · T-02. Basis: A.1 "S-1.4 | Benefits | /product/benefits | section | T-02".
- DETAIL, Health / Learning / Mobility / Meals, S-1.4.1 to S-1.4.4 · T-04 · CAT-HEA / CAT-LEA / CAT-MOB / CAT-MEA. Basis: A.1 rows S-1.4.1 to S-1.4.4; section 3.3 "pages built from one template, T-04, each bound to its F-CAT identifier".
- DETAIL, Security, S-1.5 · T-06. Basis: A.1 "S-1.5 | Security | /product/security | detail | T-06".
- DETAIL, Pricing, S-2 · T-05. Basis: A.1 "S-2 | Pricing | /pricing | detail | T-05"; section 5.4 "Pricing stays a level-1 page".
- INDEX, Customers, S-3 · T-07. Basis: A.1 "S-3 | Customers | /customers | index | T-07".
- STACK, Customer stories, S-3.1 to S-3.3 · T-08 · one per client. Basis: A.1 rows S-3.1 to S-3.3 "T-08"; B.1 "Customers over a stack of customer stories, one page per client"; S-3.4 removed and not drawn.
- INDEX, Help centre, H-0 · T-13. Basis: A.3 "H-0 | Help centre | / | index | T-13".
- INDEX, Search results, H-0.1 · T-14. Basis: A.3 "H-0.1 | Search results | /search | index | T-14".
- SECTION, For HR and finance teams, H-1 · T-15; For employees, H-2 · T-15. Basis: A.3 rows H-1 and H-2, "section | T-15".
- SECTION, Budgets H-1.1, Policies H-1.2, Approvals H-1.3, Claims H-2.1, Balance H-2.2, Card H-2.3, each · T-15. Basis: A.3 rows; C.2 T-15 "Builds H-1, H-1.1 to H-1.3, H-2, H-2.1 to H-2.3".
- STACK, Budget articles, H-1.1.1, H-1.1.2 · T-16. Basis: A.3 rows H-1.1.1 and H-1.1.2; B.1 "(Budget articles, Policy articles, Claim articles, Balance articles, Card articles)".
- STACK, Policy articles, "H-1.2.1 to H-1.2.3, H-1.2.5 · T-16; H-1.2.5 also listed under Claims". Basis: A.3 rows H-1.2.1 to H-1.2.3 and H-1.2.5 "new; also listed under H-2.1"; H-1.2.4 removed and not drawn.
- DETAIL, Approving and rejecting claims, H-1.3.1 · T-16. Basis: A.3 "H-1.3.1 | Approving and rejecting claims | … | detail | T-16" (one page, so not a stack).
- STACK, Claim articles, "H-2.1.1 to H-2.1.4 · T-16; also lists H-1.2.5". Basis: A.3 rows H-2.1.1 to H-2.1.4; text after A.3 "the Claims section lists it, so one page has one URL and two routes".
- STACK, Balance articles, H-2.2.1, H-2.2.2 · T-16. Basis: A.3 rows H-2.2.1 and H-2.2.2.
- STACK, Card articles, H-2.3.1, H-2.3.2 · T-16. Basis: A.3 rows H-2.3.1 and H-2.3.2.
- FORM, Book a demo, S-4 · T-09; DETAIL, Demo request received, S-4.1 · T-10, under it. Basis: A.1 rows S-4 and S-4.1; section 5.5 "a form (S-4) and a confirmation page (S-4.1)".
- EXTERNAL, Sign in, "S-5 · → see Perqo Admin", no template. Basis: A.1 "S-5 | Sign in | leaves for Perqo Admin | external | none"; section 5.5 "drawn with IA2's `external` tag and a '→ see' note".
- DETAIL, Get the Perqo app, S-6 · T-06 · footer. Basis: A.1 "S-6 | Get the Perqo app | /app | detail | T-06"; C.1 M-02.
- DETAIL, For merchants, S-7 · T-06 · footer. Basis: A.1 row S-7; section 2.5 "reached from the footer".
- DETAIL, About Perqo, S-8 · T-06 · footer; FORM, Contact, S-9 · T-09 · footer. Basis: A.1 rows S-8 and S-9; C.1 M-02.
- STACK, Legal pages, S-10 to S-12 · T-11 · footer. Basis: A.1 rows S-10 to S-12 "detail | T-11"; B.1 "The three legal pages are drawn as one stack, Legal pages".
- STACK, Campaign pages, "[campaign live] L-01 · T-12 · no navigation". Basis: section 5.2 "one box tagged `stack` whose note opens with the condition in square brackets, '[campaign live]'" and "appears in no navigation, uses the campaign template (T-12)"; A.2 L-01 keep, L-02 removed and not drawn.
- The drawn pages total 26 site pages + 1 campaign page + 25 Help centre pages = 52. Basis: text after A.4 "15 are added, so the redesigned site has 52"; A.4 rows 29 − 3, 2 − 1, 26 − 1.
- Depth: Home > Help centre > For employees > Claims > Claim articles is four levels below Home, and Home > Product > Benefits > Health is three. Basis: section 4.1 "its deepest path is four levels below Home … and every buyer page is within three".
- The figure shows nothing the text does not state.

(b) Caption:
- It says what the figure shows ("perqo.com as redesigned, F3, page types tagged, an ID in every note and a template in every note but Sign in's, many pages of one type drawn as one stack").
- It names the decision and the section ("Deliverable B").
- It names the sources ("IA1, section 2.3, and IA2, section 5.3; the rest from Deliverable A") and states "Perqo is fictional".
- It sits under the figure at every width and theme.
- Its counts match the figure: "five footer boxes (seven pages …)" (S-6, S-7, S-8, S-9 and S-10 to S-12) and "six global routes" (Product, Pricing, Customers, Help centre, Book a demo, Sign in; M-01).

(c) Kind: the data is a hierarchy of pages under a root, so sitemap fits. Basis: B.1; section 3.1.

(d) Drawing:
- At desktop and tablet, light and dark, the whole figure fits in one frame ("frame 1 of 1 (the whole figure fits)"). All text sits inside its boxes, nothing overlaps, nothing is cut, and the connectors run cleanly. Basis: desktop- and tablet-...-frames-light/dark.png.
- On the phone the figure scrolls sideways in its own frame across four frames, with the hint "scroll sideways for the whole figure". Across the frames every box is shown whole at least once. Basis: phone-...-frames-light/dark.png.
- The desktop opening-frame images show the page's sticky reader header ("Section 8 of 10 · Deliverable · B · The perqo.com sitemap") over the middle of the figure. That is page chrome caught by the full-page capture, not part of the figure; the frames sheets show the same area clean. Basis: desktop-read-ux-ia5-fig-06-sitemap-light.png and -dark.png against desktop-...-frames-light/dark.png.
- Both themes read clearly.

(e) Notation:
- Every tag is from IA2's closed list (`home`, `section`, `index`, `detail`, `stack`, `form`, `external`). Basis: section 3.1.
- Every box is tone 1. Basis: introduction "every perqo.com box is tone 1".
- Pages of one type are drawn as stacks. Basis: section 3.1, IA2's rule.
- The conditional area is in square brackets. Basis: section 5.2.
- The external box carries "→ see". Basis: section 5.5.
- "footer" is declared in the caption as an added note word. Basis: B.1.
- Removed pages are not drawn. Basis: face of Deliverable B "leaves out: removed pages".
- Sign in has no template. Basis: B.1 "(Sign in, the external box, has no template)".

[text]: none. The unit's counts (A.4, the 52 rows, the depths in section 4.1) agree with the figure.

Figure 6: PASS (error 0, should-fix 0, minor 3)

### Maintainer's note on figure 6's third and fourth checks

Third check (re-check 2): FIX, one should-fix (the caption counted "five footer pages" where the footer holds seven pages in five boxes, the three legal pages as one stack), verified against M-02 and B.1 and applied as given; the minors applied: the caption says why the Campaign pages stack hangs from Home, B.1 names the article stacks ("<topic> articles"), and Deliverable B's face reads "F1 or F2" as section 6 does. The desktop opening-frame minor is the same capture artefact as before, not applied. Fourth check (re-check 3): PASS, three minors. The caption's "section 4" now names IA2's rule in full (applied). The ordering minor does not call for a change: Home's children are already declared in that order (the six global routes, then M-02's five footer boxes, then Campaign pages); the row a box lands in is the sitemap kind's wrap by width, not a level. The phone opening-scroll minor is the shell's centring of a drawing wider than its frame (P44: a figure opens at the drawing's start), a renderer behaviour shared by every wide figure, not applied in the unit. Figure 6 took four checks in all.
