---
code: DD-IA2
title: "Deep dive: what IA costs and returns"
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-10
search: on
intro: Deep dive DD-IA2, written 10 Nov 2026 by Opus 5.5 in an isolated agent context that saw only its brief (with the Aim, Takes and Gives lines), the writing skill, sourcing Parts 1 and 4, the figure kinds, the Perqo register, IA1 to IA12 and DD-IA1 (P31), search on: every published figure carries its source, sample, date and label (peer-reviewed, consultancy report, maker's report, vendor, anecdote, official statistics) where it is made, read at its source that day unless marked as cited through a filed unit; fresh check the same day by a separate Fable 5.2 agent that had not seen the writing: fix, 2 errors, 11 should-fix, 7 minor, all applied as verified, three minors needing no change. Six figures in the course notation: figures 3 to 6 passed the fresh check; figures 1 and 2, changed by its findings, passed their fourth check, each by a separate re-checker. The published evidence on findability failure and its cost (task-success and tree-test rates, first clicks, search against browsing, self-service and support contacts, redesigns with before-and-after numbers) as register rows RD-16 to RD-31, every row at C0 for Perqo; what cannot be measured and six claims the field repeats without evidence, named as such; the measurement model, leading indicators read on a structure before it ships and lagging indicators read in use; the business case, from the cost of change by layer, the cost of not changing and the decision the case supports; and the limits of the exercise. Deliverable: the IA measurement model, fifteen metrics (IA11's M-01 to M-05, M-07 and M-11 and eight new, M-12 to M-19) each with its source of data, baseline method, target, cadence and rung; the business-case template with reference ranges and the rule for labelling a number; the case filled once for Perqo Admin, every number sourced, assumed or arithmetic, with its break-even and sensitivity; and two proposed decision log entries, DL-021 and DL-022. Known gaps: no published figure enters the Perqo arithmetic, and every magnitude of the case is the unit's assumption at C0; Boehm and Basili's ratios, the Forrester report behind the $1 to $100 claim and Prioritizing Web Usability were not seen; Katz and Byrne's participant numbers were not on the record read; UNC's year comes from the post's address.
---

# DD-IA2 · Deep dive: what IA costs and returns

IA1 to IA12 built the IA of Perqo (Perqo, fictional), tested part of it on paper, and recorded the rest as assumptions, and DD-IA1 read five real products from outside. This unit asks what any of that work is worth in numbers, and how far numbers can answer. It covers the published evidence on findability failure and its cost: usability studies with task-success rates, search-versus-browse figures, the cost of support contacts and of failed self-service, and redesigns with before-and-after numbers, each with its source, sample, date and label; what cannot be measured, and the claims the field repeats without evidence, named as such; the measurement model for an IA, with leading indicators measured on a structure before it ships and lagging indicators measured in use; how to build a business case for IA work in a product company, from the cost of change by layer, the cost of not changing and the decision the case supports; and the limits of the exercise. The deliverable is the IA measurement model and a business-case template with sourced ranges and labels, filled once for Perqo Admin, with every figure traced to its source or marked as this unit's own assumption.

Every published figure in this unit was read at its source on 10 November 2026, the day the unit was written, and each carries that date, its sample and its label where it is made; the exceptions are the figures cited through IA3, IA11 and DD-IA1 (Nielsen 1997, Bailey and others 2009, Dub 2021), which are marked as cited there. A figure that could not be opened at its source is said to be unverified. Every figure uses IA2's notation (IA2, section 5.2 and the notation sheet). This unit draws five of the notation's six tones. Tone 2, "the merchant side and anything outside Perqo", carries every published figure about real products and studies, since all of them lie outside Perqo. Tone 6, a stop, "a path that ends without success, or a fault found in a review", marks, in figure 1, the published shares of task attempts that failed because of the IA; figure 2, a numeric grid drawn in one tone, gives the same two shares in tone 2. Tone 1, perqo.com, carries the metrics read from the Help centre's search, which sits on perqo.com. Tone 4, Perqo Admin and the HR and finance managers who use it, carries the metrics read from Admin's own records and every figure of the Admin business case. Tone 5, shared, carries the leading metrics, because a test method serves any surface, and the rule for labelling a number, which serves any case.

What the filed units hand on, and where this unit uses it:

| From | What it hands on | Used in |
|---|---|---|
| IA7, section 2.2, Deliverable C and "What IA8 and later units take" | Perqo Admin's IA, AD-0 to AD-6, as the scope of the case; the sizing client's volumes and queue numbers as the assumed load, each to be replaced by measured figures | section 4; Deliverable C |
| IA11, sections 1.2, 3.4, 4.4 and 6.4; Deliverable A, A.1 cost column and A.2 row 1 | the metrics M-01 to M-11, each with one definition and one interval method; the marks; the rungs C0 to C5 as the strength of each claimed benefit; the plan's costs as the unit costs of evidence; the sizing client's volumes routed to this unit | sections 3 and 4; Deliverables A and C |
| IA12, sections 3.4 and 5; Deliverable B | the Admin register AR-01 to AR-49 as the assumptions the case rests on, each at its rung; AR-02 and AR-37 as rows records can lift to C5; the 25 backbone rows as the cost of being wrong; the absent inputs as the cost of evidence not yet bought | sections 4.2 to 4.4; Deliverable C |
| IA10, section 2.9, Deliverables A and B | the leadership page (FO-09) and the sales brief (BR-3) as two audiences; the touchpoint matrix, TP-01 to TP-12, as the functions a case must speak to | section 4.1; Deliverables C and D |
| IA9, sections 2.4, 4.1 to 4.4 and 6; Deliverable C | IA debt; the change-control flow and the version rule, as the work a late change sets off; the reviews RV-04 to RV-06 and RV-10 as the cadence of the lagging reads | sections 3.3 and 4.2; Deliverable A |
| DD-IA1, section 2, Deliverable A and "What later units take" | GOV.UK's search figures with no intervals, as practice; whether GOV.UK's three search measures join the model; the register of published claims, RD-01 to RD-15, as the form in which a case records outside evidence, continued here from RD-16 | sections 1 and 3.2; Deliverable B |

## 1 · The published evidence on findability failure and its cost

### 1.1 · Five labels, and what each licenses

A published number carries the weight of the work behind it, and the course's sourcing rule asks that its kind be named where it is used. This unit uses five labels. **Peer-reviewed**: research published after review in an HCI or information-science venue, with its method open to inspection. **Consultancy report**: a research firm's own data and analysis, published by the firm, whose sample and method are given in part or not at all (NN/g, MeasuringU, Gartner, IDC, McKinsey Global Institute). **Maker's report**: an organisation's account of a test on its own product, as DD-IA1 labelled GOV.UK's posts ("a maker's report of its own test"; DD-IA1, section 2); it is the vendor label applied to a product's own makers, whose interest is in the result. **Vendor**: a company that sells the tool or service whose value it reports. **Anecdote**: a single case without a stated method or sample. A sixth kind, **official statistics**, enters only in section 4, for wages.

DD-IA1 set the ceiling for every one of them when carried to Perqo: a test GOV.UK ran on GOV.UK's users is evidence about GOV.UK, and for Perqo it is a reasoned default at C0 on IA11's ladder until Perqo's own test raises it (DD-IA1, section 1; IA11, section 6.4). The figures below are therefore read for two different uses. As evidence about the world, each is worth what its label says. As an input to a Perqo case, each is at most a reference range, labelled, and never a forecast of what Perqo will see.

### 1.2 · Task success, and the failures the IA causes

**How often tasks succeed.** Jeff Sauro's analysis of MeasuringU's practice data found that "the average task-completion rate is 78%", from 1,189 tasks in 115 usability tests with 3,472 users across more than a dozen organisations; a rate above 92% is in the top quartile and one below 49% in the bottom ("What Is A Good Task-Completion Rate?", MeasuringU, 21 March 2011, [measuringu.com, task completion](https://measuringu.com/task-completion/), read 10 November 2026; consultancy report). The tasks were on full interfaces, the products are not named, and nothing says how the tests were chosen, so the 78% describes MeasuringU's clients' tests and no wider population. IA11 used the same figure for scale (IA11, section 4.4).

**How often tree tests succeed.** Sauro reported an average tree-test completion rate of 66% across 77 tasks from 200 users in three studies, and called it "tentative". In an experiment on two retailers' structures, 17 of 20 tasks had a higher completion rate on the tree test than on the live site ("Using Tree-Testing To Test Information Architecture", MeasuringU, 26 March 2013, [measuringu.com, tree testing](https://measuringu.com/tree-testing-ia/), read 10 November 2026; consultancy report). The second finding matters more for this unit than the first: a tree test and the live product measure different things, and the one study that set them side by side found the tree test higher, by margins it does not generalise.

**How often the IA is the cause.** Jakob Nielsen's comparison of two NN/g studies is the one published figure found for this unit that attributes task failures to the IA itself: "14% of task attempts failed due to IA problems in 2004" and "10% of task attempts failed due to IA problems in 2009", from user testing of 25 websites and of 24 websites; over the same years the average success rate rose from 66% to 81%, and "Bad IA is now the greatest cause of task failures" ("IA Task Failures Remain Costly", Nielsen Norman Group, 15 April 2009, [nngroup.com, IA task failures](https://www.nngroup.com/alertbox/ia-failures.html), read 10 November 2026; consultancy report). The attribution rests on a classification scheme NN/g developed in 2004 and describes in a book; the article does not say how many people coded each failure or how agreement was checked. The two samples are different sites, so the change from 14% to 10% is a change across the web NN/g tested, and no redesign of any one site.

**What a first click predicts.** Robert Bailey and his colleagues report that "if the user's first click was correct, the chances of getting the overall scenario correct was .87", against ".46" after a wrong first click, from tests across several websites; the paper does not give the number of participants or studies (Bailey and others, *HCII 2009*, LNCS 5619, pp. 3 to 12; peer-reviewed proceedings; as read and cited by IA11, section 2.3). This is the one published link found between a leading indicator and the task's outcome, and section 3.1 builds on it.

### 1.3 · Search and browse

Three findings, all filed in IA3 (section 5.1), describe how people choose between a menu and a search box. Nielsen reported in 1997 that "more than half of all users are search-dominant" ("Search and You May Find", NN/g, 14 July 1997; as cited in IA3, section 5.1; consultancy report, no sample given in the article as IA3 cites it). Jared Spool's team tested that claim with 30 users performing 121 shopping tasks on three to six e-commerce sites each: "there wasn't a single user out of 30 who always used the search engine first"; on 21% of the sites every user searched, on 32% every user followed links, and 47% were "not dominant to search or links" ("Are There Users Who Always Search?", UIE, 1 May 2001, [articles.centercentre.com, always search](https://articles.centercentre.com/?p=15), read 10 November 2026; consultancy report, practice). Michael Katz and Michael Byrne ran two studies on e-commerce sites and found that "use of the site search functions did not yield faster or more accurate performance", and that the breadth and scent of the menus influenced browsing; their conclusion is that "providing site search should not be used to compensate for poor menu design" ("Effects of Scent and Breadth on Use of Site-Specific Search on E-Commerce Web Sites", *ACM Transactions on Computer-Human Interaction* 10, no. 3, September 2003, abstract at [unpaywall.org, Katz and Byrne](https://unpaywall.org/10.1145%2F937549.937551), read 10 November 2026; peer-reviewed; the participant numbers are not on the record read).

Two maker's figures add scale. GDS wrote in 2021 that "while most users start from a search engine, around 15% use topic pages to navigate" on GOV.UK, without the method behind the 15% (Dub 2021, as read by DD-IA1, section 2, RD-03; maker's report). And GOV.UK's A/B test of a new site search reported "a 14% increase in overall clickthrough from the search results page", "an 11% decrease in users having to refine their search" and "an 8% reduction in users leaving site from the search page"; the test was ramped to 50% of users who consented to analytics, and the post gives no sample size, no test length and no intervals, and does not say whether the three changes are relative or in percentage points (Catriona Fraser, Christian Sutter and Tara Stockford, "A new search engine for GOV.UK", Inside GOV.UK, 23 October 2024, [insidegovuk.blog.gov.uk, new search engine](https://insidegovuk.blog.gov.uk/2024/10/23/a-new-search-engine-for-gov-uk/), read 10 November 2026; maker's report; DD-IA1's RD-05).

Read together: the peer-reviewed result says search does not rescue a weak menu, the practice result says the site shapes the choice more than the person does, and the 1997 claim of a search-dominant majority did not survive a test. None of them gives a rate a Perqo case can use; they decide what to measure. A product whose search is a supplement, as the Help centre's is, should be measured on both routes, and a product with no search, as Admin has none (IA7, section 4.5), on its lists and their find fields.

### 1.4 · Support contacts and failed self-service

A failed search for help often ends in a contact. Gartner reported in 2019 that "Only 9% of customers report resolving their issues completely via self-service"; from its 2019 poll of customer service and support leaders, that "live channels such as phone, live chat and email cost an average of $8.01 per contact", and "self-service channels such as company-run websites and mobile apps cost about $0.10 per contact"; and from "a survey of 8,398 customers", the channels customers preferred for resolving an issue, phone first at 44% (Gartner, "Gartner Says Only 9% of Customers Report Solving Their Issues Completely via Self-Service", press release, 25 September 2019, [gartner.com, self-service](https://www.gartner.com/en/newsroom/press-releases/2019-09-25-gartner-says-only-9--of-customers-report-solving-thei), read 10 November 2026; consultancy report). Three limits follow from the release itself. The 9% is not tied in the text to a named sample. The cost figures are averages reported by service leaders, across industries and mostly consumer service, and say nothing about a business tool's support. And a self-service contact at $0.10 is a cost to the company; the customer's time is not in it.

For work tools, the older figures are about intranets. Susan Feldman of IDC wrote in 2004 that knowledge workers "spend from 15% to 35% of their time searching for information", citing studies by IDC and others with no sample or year for the range; that a 1999 European IDC study put the cost at $5,000 per worker a year, without its method; and that an IDC study, which the article dates 2001 and cites as "Quantifying Enterprise Search", IDC, May 2002, found that only 21% of respondents found what they needed 85% to 100% of the time ("The high cost of not finding information", KMWorld, 1 March 2004, [kmworld.com, not finding information](https://www.kmworld.com/Articles/Editorial/Feature/The-high-cost-of-not-finding-information-9534.aspx), read 10 November 2026; consultancy report). Nielsen's intranet study of 2002 is the one with a stated sample: employees at 14 companies doing 16 common tasks, from which he computed the annual cost of the time those tasks take per employee at $3,042 on a low-usability intranet, $2,069 on an average one and $1,563 on one in the best quarter ("Intranet Usability: The Trillion-Dollar Question", NN/g, 10 November 2002, [nngroup.com, intranet usability](https://www.nngroup.com/articles/intranet-usability-the-trillion-dollar-question/), read 10 November 2026; consultancy report). The per-employee figures are measured times priced at assumed salaries and overheads; section 2.2 returns to what he did with them.

### 1.5 · Redesigns with before-and-after numbers

**Averages across many redesigns.** Nielsen reported in 2008 that in NN/g's new survey of design projects "the average improvement was 83%" in key performance indicators, against 135% in its survey six years earlier; the full report holds 72 case studies, and the article does not say how many projects the 83% averages; projects with improvements of "a factor of 10 or more", about 12% of them, were removed as outliers, and the difference between the two surveys was "marginally significant", at p = 8% ("Usability ROI Declining, But Still Strong", NN/g, 21 January 2008, [nngroup.com, usability ROI](https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/), read 10 November 2026; consultancy report). Kate Moran's update gives 99 case studies collected for NN/g's report since 2006, each with at least one before-and-after metric: an average improvement of 247% for 2006 to 2008 and 75% for 2020, the difference "statistically significant (p = 0.01)", and for 2020 a 95% confidence interval from 8% to 104%; half the values fell between 13% and 157% ("UX Gains Shrinking", NN/g, 1 November 2020, [nngroup.com, UX gains shrinking](https://www.nngroup.com/articles/ux-gains-shrinking/), read 10 November 2026; consultancy report). Both are averages of case studies NN/g collected for its reports, by a selection neither article describes, across every kind of UX change, of which IA is one.

**Single redesigns of a structure.** Four reports, each a maker's account or weaker:

- **GOV.UK's topic pages, 2022.** An A/B test in which "50% of GOV.UK users got this new design": clickthrough to content, the pages' key indicator, "increased from 61.6% to 65.1%"; no sample size, test length or interval is given (Sam Dub, "Rolling out a new design for browsing GOV.UK by topic", Inside GOV.UK, 8 August 2022, [insidegovuk.blog.gov.uk, browsing by topic](https://insidegovuk.blog.gov.uk/2022/08/08/rolling-out-a-new-design-for-browsing-gov-uk-by-topic/), read 10 November 2026; maker's report).
- **The ONS taxonomy, 2013.** A card sort with around 200 users and tree tests with over 130; "The average success rate across all test 2 versions was 86%"; "It took users half the time to complete the tasks", and success rates "were almost 30% better than that of the existing taxonomy", with no absolute figure for the old one; themes cut "from 11 to 4" in a taxonomy of "over 1400" items, "5 levels deep". The post also cites Sauro's 78% as "a satisfaction benchmark", where Sauro's figure is a completion rate (Jonathan Porton, "No longer taxing – we hope", ONS Digital blog, 5 December 2013, [digitalblog.ons.gov.uk, taxonomy](https://digitalblog.ons.gov.uk/2013/12/05/no-longer-taxing-we-hope), read 10 November 2026; maker's report).
- **UNC Libraries' navigation.** A tree test of the new navigation with 170 participants on four tasks, against "a similar test conducted before the navigation changes" whose sample is not given: overall success from 63% to 70% and directness from 69% to 74%, while one task, borrowing a book the library does not hold, fell from 79% to 61%; no statistical test is reported (Daniel Pshock and Chad Haefele, "Assessing nav changes", UNC Libraries UX blog, dated 19 May 2016 in its address, [libux.web.unc.edu, nav changes](https://libux.web.unc.edu/2016/05/19/assessing-nav-changes/), read 10 November 2026; maker's report).
- **An intranet, unnamed.** A vendor's case study quotes an anonymous New Zealand financial organisation's intranet manager: "53% faster to find the information through the new content", from "controlled testing with frontline staff" with no sample, tasks or times given (SWOOP Analytics, "How one organisation made intranet information 53% faster to find", case study, 27 July, year not stated, [swoopanalytics.com, case study](https://www.swoopanalytics.com/case-studies/intranet-information-faster-to-find), read 10 November 2026; vendor, anecdote).

The UNC result is the most useful of the four for a business case, and for its worst row: an overall gain hid a task that got markedly worse. A case that reports one number per redesign loses that.

### 1.6 · The evidence, tabulated

Figure 1 sets the published success and failure rates side by side, each in percent, in tone 2 for figures about products and studies outside Perqo and tone 6 for the two shares of task attempts that failed because of the IA. Its rows: MeasuringU, tasks, 2011, 78 (usability tasks completed); MeasuringU, tree tests, 2013, 66 (tree-test tasks completed); NN/g sites, success, 2004, 66; NN/g sites, success, 2009, 81; ONS tree tests, 2013, 86 (the new taxonomy); Bailey, right first click, 2009, 87, and Bailey, wrong first click, 2009, 46 (scenario right after each); Gartner, fully self-served, 2019, 9 (customers who report resolving their issue completely by self-service); NN/g sites, failed by IA, 2004, 14; NN/g sites, failed by IA, 2009, 10.

```viz
{"kind": "compare", "caption": "Published success and failure rates: ten figures on task success, tree-test success, first clicks, self-service and IA-caused failure, each in percent; supports the reading of what a findability failure rate looks like in the published evidence, and how little of it transfers (section 1.6, from sections 1.2, 1.4 and 1.5). Sauro, MeasuringU, 2011 and 2013 (consultancy reports); Nielsen, NN/g, 2009 (consultancy report); Porton, ONS Digital blog, 2013 (maker's report); Bailey and others, HCII 2009 (peer-reviewed, as cited in IA11); Gartner press release, 2019 (consultancy report). All but Bailey and others read 10 November 2026. Samples differ from source to source; section 1.6's table gives each, or says it is not given. Tone 2: outside Perqo; tone 6: a stop, here the share of attempts on sites outside Perqo that failed because of the IA.", "unit": "%", "max": 100, "rows": [
 {"label": "MeasuringU, tasks, 2011", "value": 78, "tone": 2},
 {"label": "MeasuringU, tree tests, 2013", "value": 66, "tone": 2},
 {"label": "NN/g sites, success, 2004", "value": 66, "tone": 2},
 {"label": "NN/g sites, success, 2009", "value": 81, "tone": 2},
 {"label": "ONS tree tests, 2013", "value": 86, "tone": 2},
 {"label": "Bailey, right first click, 2009", "value": 87, "tone": 2},
 {"label": "Bailey, wrong first click, 2009", "value": 46, "tone": 2},
 {"label": "Gartner, fully self-served, 2019", "value": 9, "tone": 2},
 {"label": "NN/g sites, failed by IA, 2004", "value": 14, "tone": 6},
 {"label": "NN/g sites, failed by IA, 2009", "value": 10, "tone": 6}]}
```

The figure flattens what the table below keeps: no two sources share a population, a task set or a method, and NN/g's 2004 and 2009 rows are different sites, so no row can be read against another as better or worse. The 86% is one organisation's new tree on its own tasks; the 66% for MeasuringU's tree tests is an average across three studies; the 87% is a conditional probability.

Figure 2 draws the before-and-after pairs from sections 1.2 and 1.5 that give both numbers, as a grid in tone 2, each cell a percent, its scale labelled "percent, as published": GOV.UK, clicks (clickthrough), 61.6 and 65.1; UNC, all (all tasks), 63 and 70; UNC, direct (directness), 69 and 74; UNC, borrow (the borrow task), 79 and 61; NN/g, success, 66 and 81; NN/g, IA fail (attempts failed by IA), 14 and 10. GOV.UK's row is its topic pages, UNC's are UNC Libraries' tree tests, and NN/g's are the sites it tested; the last two rows are different sites in 2004 and 2009, under Before and After, a trend and no redesign; in that last row a lower share is the better result. No pair here carries an interval.

```viz
{"kind": "matrix", "numeric": true, "tone": 2, "unit": "%", "min": 0, "max": 100, "scale_label": "percent, as published", "caption": "Before and after: the published pairs of sections 1.2 and 1.5 that give both numbers, each cell a percent as its source gives it; supports the reading that an overall gain can hide a task that got worse (UNC's borrow task) and that no pair here carries an interval (section 1.6). Dub, Inside GOV.UK, 2022; Pshock and Haefele, UNC Libraries UX blog, dated 2016 in its address; Nielsen, NN/g, 2009 (different sites in 2004 and 2009, a trend and no redesign; in its last row lower is better). Maker's reports and a consultancy report, read 10 November 2026. Tone 2: outside Perqo.", "cols": ["Before", "After"], "rows": [
 {"label": "GOV.UK, clicks", "cells": [61.6, 65.1]},
 {"label": "UNC, all", "cells": [63, 70]},
 {"label": "UNC, direct", "cells": [69, 74]},
 {"label": "UNC, borrow", "cells": [79, 61]},
 {"label": "NN/g, success", "cells": [66, 81]},
 {"label": "NN/g, IA fail", "cells": [14, 10]}]}
```

The register below records each published figure in a form adapted from DD-IA1's (the columns are this unit's), continuing its identifiers from RD-16 (DD-IA1, Deliverable A); RD-03 and RD-05, GOV.UK's, are DD-IA1's and are not repeated. "Rung for Perqo" is C0 for every row: published evidence about other products is a reasoned default for Perqo (DD-IA1, section 1).

| ID | Source and date | Published figure | Sample | Label | Left out | Rung for Perqo |
|---|---|---|---|---|---|---|
| RD-16 | Sauro, MeasuringU, 21 Mar 2011 | average task completion 78%; quartiles above 92% and below 49% | 1,189 tasks, 115 tests, 3,472 users | consultancy report | which products; how tests were chosen | C0 |
| RD-17 | Sauro, MeasuringU, 26 Mar 2013 | tree-test completion 66%, "tentative"; 17 of 20 tasks higher on the tree than live | 77 tasks, 200 users, 3 studies | consultancy report | the range; the live rates | C0 |
| RD-18 | Nielsen, NN/g, 15 Apr 2009 | 14% (2004) and 10% (2009) of task attempts failed because of the IA; success 66% and 81% | 25 sites; 24 sites | consultancy report | coders, agreement, intervals | C0 |
| RD-19 | Bailey and others, HCII 2009 (as cited in IA11) | scenario right .87 after a right first click, .46 after a wrong one | not given | peer-reviewed | participants, studies | C0 |
| RD-20 | Nielsen, NN/g, 14 Jul 1997 (as cited in IA3) | "more than half of all users are search-dominant" | not given | consultancy report | the method; contradicted by RD-21; RD-22 found the choice shaped by the site's menus | C0 |
| RD-21 | Spool, UIE, 1 May 2001 | no user of 30 always searched first; sites: 21% search, 32% links, 47% neither | 30 users, 121 tasks | consultancy report, practice | the number of sites | C0 |
| RD-22 | Katz and Byrne, ACM TOCHI, Sep 2003 | search not faster or more accurate; menu breadth and scent shape browsing | two studies; n not on the record read | peer-reviewed | the participant numbers, as read | C0 |
| RD-23 | Gartner, press release, 25 Sep 2019 | 9% resolve fully by self-service; $8.01 live and $0.10 self-service per contact | 8,398 customers (channels); a poll of service leaders (costs) | consultancy report | the 9%'s sample; business support | C0 |
| RD-24 | Feldman, KMWorld, 1 Mar 2004 | 15% to 35% of time searching; $5,000 per worker a year (IDC, 1999) | not given | consultancy report | every sample and method | C0 |
| RD-25 | Nielsen, NN/g, 10 Nov 2002 | cost of 16 tasks a year per employee: $3,042, $2,069, $1,563 by intranet quality | 14 companies, 16 tasks | consultancy report | salaries assumed; the worldwide figures extrapolated (section 2.2) | C0 |
| RD-26 | Nielsen, NN/g, 21 Jan 2008 | average KPI gain 83% (135% six years earlier) | not given for the 83%; the report holds 72 case studies; outliers removed | consultancy report | how cases were chosen | C0 |
| RD-27 | Moran, NN/g, 1 Nov 2020 | average gain 247% (2006 to 2008), 75% (2020), 95% interval 8% to 104% | 99 case studies | consultancy report | IA's share among UX changes | C0 |
| RD-28 | Dub, Inside GOV.UK, 8 Aug 2022 | topic pages' clickthrough 61.6% to 65.1% | A/B, 50% of users; n not given | maker's report | n, length, interval | C0 |
| RD-29 | Porton, ONS Digital blog, 5 Dec 2013 | new taxonomy 86% success; "almost 30% better"; half the time | about 200 (sort), over 130 (tree tests) | maker's report | the old taxonomy's absolute rate | C0 |
| RD-30 | Pshock and Haefele, UNC Libraries, 2016 | success 63% to 70%; borrow task 79% to 61% | 170 (after); before not given | maker's report | the before sample; any test | C0 |
| RD-31 | SWOOP Analytics, case study, year not stated | "53% faster to find" | not given | vendor, anecdote | everything but the quotation | C0 |

## 2 · What cannot be measured, and the claims made without evidence

### 2.1 · What no measure of an IA reaches

Five things lie outside every measure in section 1, and a case that claims them claims without evidence.

- **The counterfactual.** A before-and-after comparison measures a release, and a release carries more than a structure: GOV.UK's 2024 change was a new search engine, its 2022 change a new page design, and ONS reworked a whole taxonomy at once (RD-05, RD-28, RD-29). Only a split test isolates one change, and GOV.UK's two A/B tests are the only split tests in the evidence above; neither gives an interval.
- **The people who never arrived.** A search log holds no one who gave up before searching, and an analytics path no one who never opened the product (IA11, section 7). A structure that sends people to support, or to a competitor, shows in a log only as their absence.
- **Who would have left.** Nielsen's 2009 article argues that most of the business gain from a better IA comes from "antagonizing customers less, so that they're more likely to stay" (RD-18), which is an argument; no study read for this unit measures it for an IA.
- **What a rework did not cost.** A structure that was right the first time leaves no record of the change it made unnecessary. IA9 said the same of IA debt: "No study known to this unit measures what IA debt costs" (IA9, section 2.4).
- **The share that belongs to the IA.** Moran's 99 cases are UX changes of every kind (RD-27), and Nielsen's survey is of design projects (RD-26). The one figure that separates the IA's share of failures is RD-18's, and its coding method is not open.

### 2.2 · Six claims the field repeats

Each claim below circulates in business cases for UX and IA work. Each is named here with what its source shows.

1. **"Every $1 spent on UX returns $100."** A 2021 post by a director at an SAP consultancy gives "$1 spent on UX returns $100" from "a 2019 Forrester report", hedged in its own introduction with "if Roger Pressman and a secondary Forrester Report are to be believed"; it quotes nothing from the report and names no page (Adam Anderson, "User Experience (UX) turns your $1 investment into a $100 return…really?", Mindset Consulting, 20 October 2021, [mindsetconsulting.com, UX return](https://www.mindsetconsulting.com/user-experience-ux-turns-your-1-investment-into-a-100-return-really/), read 10 November 2026; practice). The report was not seen for this unit. As it circulates, the claim is unsourced.
2. **"A defect costs 100 times more to fix after release."** The chart most often given for it is attributed to an "IBM Systems Sciences Institute". Hillel Wayne reports that Laurent Bossavit traced the institute to an internal training programme and found no study behind the chart, which as far as anyone knows is "completely made up"; Wayne's own reading of the primary research is that it "tentatively points in that direction", depending on how late-stage, bugs and more expensive are read, with "no smoking gun" ("I ****ing hate Science", *Computer Things*, 19 July 2021, [buttondown.com, Hillel Wayne](https://buttondown.com/hillelwayne/archive/i-ing-hate-science/), read 10 November 2026; practice). Bossavit's book gives the curve a chapter and a bibliographical appendix (*The Leprechauns of Software Engineering*, Leanpub, page dated 20 December 2025, ch. 10 and appendix B, contents, [leanpub.com, Leprechauns](https://leanpub.com/leprechauns); only the contents were read). The primary candidate, Barry Boehm and Victor Basili's "Software Defect Reduction Top 10 List" (*Computer* 34, no. 1, January 2001, pp. 135 to 137), was seen only as a catalogue record with its abstract ([umiacs.umd.edu, record](https://umiacs.umd.edu/node/12156), read 10 November 2026); its ratios are unverified here. The counter-claim is no better supported: Mike Cohn writes that the curve "hasn't disappeared, but it's far flatter than most people assume", and cites no data ("The Cost of Change Curve Is Outdated", Mountain Goat Software, last updated 3 March 2026, [mountaingoatsoftware.com, cost of change](https://www.mountaingoatsoftware.com/blog/the-cost-of-change-curve-is-outdated), read 10 November 2026; practice). Section 4.2 uses no multiplier from either side.
3. **"Knowledge workers spend a fifth of their time searching."** The figure usually given, 19% or 1.8 hours a day, is McKinsey Global Institute's own estimate, in its 2012 report on social technologies: interaction workers spend "19 percent of working hours trying to track down information needed to complete tasks", which its appendix gives as 8.8 hours of a 46.5-hour week in an exhibit titled "We adjust IDC data to estimate time spent on different activities by a typical interaction worker" (Exhibit A7; 8.8 hours over five days is 1.76 hours a day, this unit's arithmetic). The same report says social tools could reduce "information searching time by as much as 35 percent", which would "return approximately 6 percent of the workweek to other tasks", and that knowledge workers spend 28 hours a week "writing e-mails, searching for information, and collaborating internally" (Michael Chui and others, *The social economy*, McKinsey Global Institute, July 2012, [mckinsey.com, social economy](https://mckinsey.com/~/media/McKinsey/Industries/Technology%20Media%20and%20Telecommunications/High%20Tech/Our%20Insights/The%20social%20economy/MGI_The_social_economy_Full_report.ashx), read 10 November 2026; consultancy report). The 19% is therefore a consultancy's estimate adjusted from IDC survey data, with no sample given in the passages read; it estimates time spent looking for information and measures nothing about time lost to a poor structure. Feldman's 15% to 35% names no sample (RD-24).
4. **"Most users are search-dominant."** Nielsen's 1997 claim (RD-20), contradicted by Spool's observation (RD-21); Katz and Byrne's experiments found the choice between searching and browsing shaped by the site's menus (RD-22; IA3, section 5.1).
5. **"Poor intranets cost the world $100 billion a year", or $1.3 trillion.** In June 2002 Nielsen wrote: "I estimate that low intranet usability costs the world economy $100 billion per year in lost employee productivity", with no method given ("Foreword to Information Architecture (2nd edition)", NN/g, 1 June 2002, [nngroup.com, foreword](https://www.nngroup.com/articles/foreword-ia-2nd/), read 10 November 2026). Five months later his study of 14 intranets extrapolated savings of $311,294,070,513 a year for the 16 tasks if every intranet reached the best quarter, about $600 billion with assumed company-specific tasks, and $1.3 trillion if every task reached the best level found (RD-25). Two estimates by one author in one year differ thirteenfold; both rest on priced time from 14 companies multiplied across the world's workers.
6. **"UX improves key metrics by 83%", or 247%, or 75%.** These are real averages (RD-26, RD-27), and Moran's own interval, 8% to 104% for 2020, shows how little one average says about the next project. Used as a forecast for one product, each is a claim without evidence.

What the six have in common is a number detached from its sample. Each one, put back beside its sample, shrinks to what it can support, and section 4.6 makes that the rule for every number in a case.

## 3 · The measurement model

### 3.1 · Leading and lagging

A leading indicator, in this unit's use, is measured on a structure before it ships, with people doing tasks on a tree, a sort or a screen: it predicts. A lagging indicator is measured in use, from the product's own records, after release: it confirms. The terms are this unit's, set to match IA11's ladder, where leading tests reach C2 or C3 and records of the behaviour itself reach C5 (IA11, section 6.4).

The published link between the two is thin. Bailey's first click is a leading measure with a stated relation to the outcome, .87 against .46 (RD-19), and IA11 adopted it as M-03 for that reason (IA11, section 2.3). Sauro's comparison runs the other way: 17 of 20 tasks did better on a tree test than on the live site (RD-17), so a tree test's success is an estimate of findability in the structure and an overestimate of success in the product, by an amount no source fixes. IA11 gave the mechanism: a tree test has no visual design, no content on the page and no search, and a label may fail or pass on a screen where its neighbours explain it (IA11, section 2.2). The model therefore keeps the two kinds apart: a lagging number is never read as the verdict on a leading test, or the reverse. Where a test and a record agree on one question, they converge, which IA11's ladder holds at C4 (IA11, section 6.4); where they disagree, the question stays open (IA11, section 6.3).

### 3.2 · Which metrics, and why these

The brief names four lagging indicators: task success, search exits, support tickets by category, and time to find. IA11's eleven metrics were defined for tests and for the app's records; eight lagging metrics are new here, three from GOV.UK's search work and five that Admin's records need.

- **Leading: IA11's metrics, kept.** M-01 success rate, M-02 directness, M-03 first-click correctness, M-04 time on task, M-05 placement share and M-11 problem frequency, each as IA11 defines it, with IA11's 95% adjusted-Wald interval for every proportion (IA11, sections 1.2 and 3.4).
- **Lagging, search: M-07 kept, and GOV.UK's three measures joined.** DD-IA1 left this unit to decide whether GOV.UK's clickthrough from results, refinement and exit from the search page join the model ("What later units take"). They join, as new metrics M-12 to M-14, for the Help centre's search on perqo.com, which is where Perqo has a search box (IA3, section 5.1); they do not apply to Admin, which has none (IA7, section 4.5). Each is defined below so that it can carry an interval, which GOV.UK's report did not give (RD-05).
- **Lagging, Admin: five new metrics.** M-15 tickets per page answers "support tickets by category", on IA9's tag practice (IA9, section 6.2). M-16 find-to-open time answers "time to find" for Admin, whose finding is done in each list's find field (IA7, section 4.5). M-17 landing match is the read IA12 named for AR-37 (IA12, Deliverable B). M-18 overdue share is the read named for AR-41. M-19 flow completion answers "task success" in use, for the forms where Admin's work is saved.

The new definitions (this unit's, Perqo, fictional):

| ID | Metric | Definition | Read with |
|---|---|---|---|
| M-12 | Results clickthrough | searches followed by a click on a result before any further search, divided by all searches, in one period; after GOV.UK's "clickthrough from the search results page" (RD-05) | the interval of a difference of two proportions, period with period (IA11, section 1.2, M-10's reading, and section 6.2; section 3.4 gives the interval of one proportion) |
| M-13 | Refinement rate | searches followed in the same session by another search with no result clicked between them, divided by all searches; IA3's reformulated query (IA3, section 5.2) | as M-12 |
| M-14 | Search exit rate | sessions that end on a results page, divided by sessions with a search; after GOV.UK's "users leaving site from the search page" (RD-05) | as M-12 |
| M-15 | Tickets per page | tickets tagged with one AD- page or DT- tree in a month, per 100 active admin users; per tag | compared with the range of the four quarters before (this unit's rule) |
| M-16 | Find-to-open time | the median seconds from the first character typed in a list's find field to opening a record from that list, per list; with find abandonment, finds that open no record divided by all finds | median beside the abandonment share and its interval |
| M-17 | Landing match | sessions of a role whose first action after sign-in is on that role's landing page (AD-4 for an HR manager, AD-2 for a finance manager), divided by that role's sessions | the interval of a proportion (IA11, section 3.4) |
| M-18 | Overdue share | claims that waited in Approvals more than five working days, divided by claims that entered Approvals in the period | as M-17 |
| M-19 | Flow completion | starts of Invite employees (AD-1.3), Set budgets (AD-2.2) or Edit policy (AD-3.1.1) that end in a save in the same session, divided by starts; per form | as M-17 |

M-16 and M-19 need two records Perqo does not keep today: a find-field event and a save event on Admin's forms (Perqo, fictional; set here). Admin's page views by AD- identifier and its failed sign-ins are already recorded (IA9, section 6.3). M-12 to M-14 need a click event on the Help centre's results page (Perqo, fictional; set here).

### 3.3 · Baselines, targets and cadence

**Baselines.** A leading indicator's baseline is the same tasks on the current structure, the form IA11 gave TT-0 for the app (IA11, Deliverable B, B.6, and V-17). A lagging indicator's baseline is at least one full quarter of records before the change, because a single month can hold a campaign or an onboarding; Farrell's advice to read several months of a search log is the source of the rule (Farrell, NN/g, 2017, as cited in IA3, section 5.2). For a proportion the baseline carries its interval; for a count or a median, its range over the four quarters before (this unit's rule, since IA11 set no interval method for counts or medians).

**Targets.** Every target is set before the measure is read, which is IA11's rule (IA11, section 4.4) and the one GOV.UK's reports did not show (DD-IA1, "What later units take"). For Admin's leading tests IA11 left the marks free ("Perqo facts set by this unit", marks for Admin's tests); this unit sets them by IA11's pattern: 80% for the two tasks that are each role's most frequent work, deciding a claim and setting budgets (IA7, Deliverable C, C.2, assumed), and 70% for every other Admin task (Perqo, fictional). For a lagging indicator the target is a direction and a rule: after a change, the interval of the difference lies wholly on the improving side, or for a count, the next two months fall outside the baseline's range on the improving side (this unit's rule).

**Cadence.** Lagging reads follow IA9's reviews: search logs quarterly at RV-04, ticket tags monthly at RV-05, analytics quarterly at RV-06, each with its triggers (IA9, Deliverable C). Leading tests run in a cycle that touches Admin's labels or roles, at FO-07 (IA10, A.2), and before and after a change to a top level, at RV-11 (IA9, Deliverable C).

### 3.4 · The model, drawn

Figure 3 draws the model's fifteen metrics with four columns: kind, data, cadence and the rung a read reaches (IA11, section 6.4). Rows for the leading metrics are tone 5, shared, because a method serves any surface; rows read from the Help centre on perqo.com are tone 1; rows read from Admin's records are tone 4. Its legend reads "shared: a method serves any surface", "perqo.com: the Help centre's search" and "Admin: Perqo Admin's records". The rows and their cells, as drawn:

- M-01 Success rate: leading; tree test; each FO-07 cycle; RV-11; C2 at 12, C3 at 50.
- M-02 Directness: leading; tree test; with M-01; C2 or C3.
- M-03 First click: leading; first-click test; each FO-07 cycle; C2 or C3.
- M-04 Time on task: leading; any test; with M-01; read beside M-01.
- M-05 Placement share: leading; hybrid sort; when a label is in question; C2 or C3.
- M-11 Problem frequency: leading; usability round; each round; C2.
- M-07 Zero-result rate: lagging; Help centre log; quarterly, RV-04; C1.
- M-12 Results clickthrough: lagging; Help centre log; quarterly, RV-04; C1.
- M-13 Refinement rate: lagging; Help centre log; quarterly, RV-04; C1.
- M-14 Search exit rate: lagging; Help centre log; quarterly, RV-04; C1.
- M-15 Tickets per page: lagging; ticket tags; monthly, RV-05; C1.
- M-16 Find-to-open time: lagging; Admin events; quarterly, RV-06; C5.
- M-17 Landing match: lagging; first actions; quarterly, RV-06; C5.
- M-18 Overdue share: lagging; claim records; quarterly, RV-06; C5.
- M-19 Flow completion: lagging; Admin events; quarterly, RV-06; C5.

```viz
{"kind": "matrix", "caption": "Measurement model: the fifteen metrics for an IA, leading (measured on a structure before release) and lagging (measured in use), with the data each is read from, its cadence and the rung a read reaches; supports the decision on what to measure, when, and how much each read can decide (section 3.4; Deliverable A). Metrics M-01 to M-11 as IA11, section 1.2 defines them; M-12 to M-14 after GOV.UK's search measures (Fraser, Sutter and Stockford, Inside GOV.UK, 2024; maker's report); M-15 to M-19 defined in section 3.2; cadence from IA9, Deliverable C, and IA10, A.2; rungs from IA11, section 6.4. Tone 5, keyed 'shared': a method serves any surface; tone 1, keyed 'perqo.com': the Help centre's search; tone 4, keyed 'Admin': Perqo Admin's records. Perqo is fictional.", "cols": ["Kind", "Data", "Cadence", "Rung"], "rows": [
 {"label": "M-01 Success rate", "tone": 5, "cells": ["leading", "tree test", "each FO-07 cycle; RV-11", "C2 at 12, C3 at 50"]},
 {"label": "M-02 Directness", "tone": 5, "cells": ["leading", "tree test", "with M-01", "C2 or C3"]},
 {"label": "M-03 First click", "tone": 5, "cells": ["leading", "first-click test", "each FO-07 cycle", "C2 or C3"]},
 {"label": "M-04 Time on task", "tone": 5, "cells": ["leading", "any test", "with M-01", "read beside M-01"]},
 {"label": "M-05 Placement share", "tone": 5, "cells": ["leading", "hybrid sort", "when a label is in question", "C2 or C3"]},
 {"label": "M-11 Problem frequency", "tone": 5, "cells": ["leading", "usability round", "each round", "C2"]},
 {"label": "M-07 Zero-result rate", "tone": 1, "cells": ["lagging", "Help centre log", "quarterly, RV-04", "C1"]},
 {"label": "M-12 Results clickthrough", "tone": 1, "cells": ["lagging", "Help centre log", "quarterly, RV-04", "C1"]},
 {"label": "M-13 Refinement rate", "tone": 1, "cells": ["lagging", "Help centre log", "quarterly, RV-04", "C1"]},
 {"label": "M-14 Search exit rate", "tone": 1, "cells": ["lagging", "Help centre log", "quarterly, RV-04", "C1"]},
 {"label": "M-15 Tickets per page", "tone": 4, "cells": ["lagging", "ticket tags", "monthly, RV-05", "C1"]},
 {"label": "M-16 Find-to-open time", "tone": 4, "cells": ["lagging", "Admin events", "quarterly, RV-06", "C5"]},
 {"label": "M-17 Landing match", "tone": 4, "cells": ["lagging", "first actions", "quarterly, RV-06", "C5"]},
 {"label": "M-18 Overdue share", "tone": 4, "cells": ["lagging", "claim records", "quarterly, RV-06", "C5"]},
 {"label": "M-19 Flow completion", "tone": 4, "cells": ["lagging", "Admin events", "quarterly, RV-06", "C5"]}],
 "legend": [{"mark": "shared", "means": "a method serves any surface", "tone": 5}, {"mark": "perqo.com", "means": "the Help centre's search", "tone": 1}, {"mark": "Admin", "means": "Perqo Admin's records", "tone": 4}]}
```

*Note, 17 November 2026: this figure's key no longer prints the drawing's tone names; each swatch now names what its cells mean, and the caption and the sentence before the metric list say so (carried proposal CP-3, row S-BW; re-checked by a fresh Opus 5.5 agent from its frames). No cell changed.*

### 3.5 · What the model means for a backoffice with few users

The sizing client has three admin users (IA7, section 2.2). A quantitative tree test wants about 50 participants per tree, a convention of guidance and practice (IA11, section 3.2), so Admin's tree test at 50 would need the admin users of at least 17 clients the size of the sizing client, all willing to take part at FO-07. Until Perqo has that many, Admin's leading tests run at the small sizes IA11 reported for qualitative work, ten to fifteen moderated sessions (IA11, section 3.2, after Barker, Boxes and Arrows, 2007, practice), and reach C2: they show that a problem exists and why, and they cannot pass a mark. IA11 put the arithmetic plainly: at 12 participants "nothing short of 12 of 12 clears a 70% mark ... and nothing clears 80%" (IA11, section 4.4). For Admin, then, the lagging indicators carry most of the measurement. Four of them (M-16 to M-19) read the behaviour itself and reach C5 without recruiting anyone, which is IA12's point that a team with no access to users can still reach C5 for questions about frequency or use (IA12, section 3.3).

## 4 · The business case for IA work

### 4.1 · The decision the case supports, and who reads it

A business case is an argument for one decision, made by one decider, at one meeting, and it is worth writing only if a number in it could change that decision. At Perqo the decision on IA work is a ranking: IA debt and open faults are "ranked by value and effort on the backlog" at RV-10, the quarterly debt triage, which product management owns (IA9, Deliverable C). The case supplies the value and the effort. IA10 named two audiences for it, and its touchpoint matrix the functions it must speak to (IA10, "What later units take").

- **Leadership, at FO-09.** One page, F1, with identifiers so a question can be followed down (IA10, section 2.9). The case reaches leadership as its decision, its cost and its break-even, with the register's counts that DL-019 proposes for the same page (IA12, Deliverable D, D.4).
- **Sales, through BR-3.** The case is where sales learns what it may say about Admin's ease of use. Nothing in Admin's register is above C0 (IA12, section 3.4), so the answer today is no figure at all; Deliverable D proposes that BR-3 says so (DL-021).
- **The other functions.** Product management decides and signs off (TP-01); engineering gives the engineering days of a change (TP-02); the content team and support give the articles and tags a change touches (TP-03, TP-08); customer success gives the per-client hours and recruits for FO-07 (TP-07); clients give their admin users' time (TP-09); legal and security are consulted where a role or a field changes (TP-10, TP-11) (IA10, A.1). Each number the case takes from a function is labelled with that function as its source.

### 4.2 · The cost of change by layer

IA12 gave the criterion: a part that would break many citations if changed is backbone and is fixed early; a part that changes by adding is open (IA12, section 5). IA9's version rule says what a break is: an identifier retired or moved, a label renamed, a relationship or transition removed, a rule's outcome changed (IA9, section 4.4). The cost of a change to a layer is the work IA9's change-control flow sets off for it: the decision log entry, the impact check, the artefacts and their faces, the vocabulary first, the structure test where a top level moves, the build, and everyone told (IA9, section 4.2). Those steps give the cost's parts; their size at Perqo is not on record anywhere, and this unit assumes it.

The figures for Perqo Admin are in Deliverable C, C.4, each the unit's own assumption (Perqo, fictional): a late change to Admin's objects costs about 22 staff days, to its roles 15, its top level 10.5, its vocabulary 8, its addresses 7; an open part costs 1.5 to 3 (reports 3, lower labels 2, queues 2, lists 1.5, landing 1.5). One part of one figure is sourced in Perqo's own record: the structure test's 1.5 days of the IA designer's time is IA11's cost for V-17, the before-and-after test (IA11, Deliverable A). The ordering follows the dependents IA12 named for each layer; the magnitudes are assumptions, and no multiplier from section 2.2's second claim is applied.

Figure 4 draws those totals in staff days, every row tone 4, Perqo Admin, because every figure in it belongs to the Admin case: Objects 22; Roles 15; Top level 10.5; Vocabulary 8; Addresses 7; Reports 3; Lower labels 2; Queues 2; Lists 1.5; Landing 1.5.

```viz
{"kind": "compare", "caption": "Cost of change by layer: the staff days of a late change to each layer of Perqo Admin's IA, from the backbone (objects, roles, top level, vocabulary, addresses) to the open parts; supports the decision on which layers to test before more is built on them (section 4.2; Deliverable C, C.4). Layers and their dependents from IA12, section 5; the steps a change sets off from IA9, sections 4.2 and 4.4; the structure test's 1.5 days from IA11, Deliverable A, V-17. Every magnitude is this unit's assumption, C0; no published multiplier is applied (section 2.2). Every row tone 4, Perqo Admin. Perqo is fictional.", "unit": "days", "max": 25, "rows": [
 {"label": "Objects", "value": 22, "tone": 4},
 {"label": "Roles", "value": 15, "tone": 4},
 {"label": "Top level", "value": 10.5, "tone": 4},
 {"label": "Vocabulary", "value": 8, "tone": 4},
 {"label": "Addresses", "value": 7, "tone": 4},
 {"label": "Reports", "value": 3, "tone": 4},
 {"label": "Lower labels", "value": 2, "tone": 4},
 {"label": "Queues", "value": 2, "tone": 4},
 {"label": "Lists", "value": 1.5, "tone": 4},
 {"label": "Landing", "value": 1.5, "tone": 4}]}
```

Two costs lie outside the figure. A change that admin users see costs every client time: customer success explains it and each client's admin users relearn it, which this unit assumes at 4 hours a client for a change to objects, roles or the top level and 1 hour for a rename (Perqo, fictional). And a change already built into clients' own habits, links and documents costs them more than Perqo can count; the case leaves it out and says so.

### 4.3 · The cost of not changing

Not changing has two costs, and a case states both. The first recurs: while a part of the IA is wrong, the people who use it pay time on every visit, and support pays for the tickets. The second is the late change itself, which grows with every client trained on the wrong structure. Neither is measured at Perqo, because nothing about Admin has been read: every row of the register is at C0 and "not run" (IA12, section 3.4).

What the published evidence gives is a set of reference ranges for pricing hours and contacts, each labelled. For client staff time, the US Bureau of Labor Statistics gives a median annual wage of $149,280 for human resources managers and $166,570 for financial managers in May 2025 (BLS, *Occupational Outlook Handbook*, "Human Resources Managers", last modified 29 October 2026, [bls.gov, HR managers](https://www.bls.gov/ooh/Management/human-resources-managers.htm), and "Financial Managers", last modified 27 August 2026, [bls.gov, financial managers](https://www.bls.gov/OOH/management/financial-managers.htm), both read 10 November 2026; official statistics), and wages were 70.0% of employer costs for private industry workers in June 2026 (BLS, *The Economics Daily*, 17 September 2026, [bls.gov, compensation costs](https://www.bls.gov/opub/ted/2026/compensation-costs-for-private-industry-workers-averaged-46-89-per-hour-worked-in-june-2026.htm), read 10 November 2026; official statistics). At an assumed 2,080 working hours a year, that is about $71.77 an hour for an HR manager in wages, or about $102.53 with employer costs, if a manager's wage share equals all private workers' (this unit's arithmetic and assumption). These are US figures; Perqo's clients' countries are not set, so the case keeps its arithmetic in hours and shows money only as a conversion. For support contacts, Gartner's $8.01 per live contact (RD-23) is the only published figure found, and it is a consumer-service average; Perqo's own cost per ticket is not set.

### 4.4 · The cost of evidence

The cost of evidence is what it takes to raise a register row's rung. IA11's plan priced each test of the app in staff days and participants' minutes (IA11, Deliverable A): a usability round costs the IA designer 3 days and five participants 45 minutes each (V-03); a before-and-after tree test, 1.5 days and 50 participants at 6 minutes (V-17); a quarterly analytics read, product management 1 day and engineering 0.5 day (V-01). Those are Perqo's own unit costs, and Deliverable C, C.5 prices Admin's evidence from them.

IA12 gave the size of what is missing. Of the 49 register rows, 28 have a test or a first read in Admin's own records or support's tickets (IA12, section 3.4): those cost a read, with no recruiting. The rest wait on forums that have not met. Counted from the register's Input column, 30 rows are wholly absent and two partly (AR-40 and AR-43): FO-07, the client validation session, is named for 21 of them; FO-05, onboarding, for 6; FO-08, privacy and security, for 4; FO-09, leadership, for 1 (IA12, Deliverable B; this unit's count). The cost of evidence for those rows is a forum's first meeting, and for most of them, recruiting admin users from several clients.

### 4.5 · Benefits, each at its rung

A case claims benefits, and each benefit stands on evidence at some rung of IA11's ladder. The rule for the case is that a benefit is stated at its rung and no higher, and that a published figure never stands in for a measure (this unit's rule, from section 1.1 and IA11, section 6.4). For Admin today, every benefit is at C0: the HR time a better Approvals list would save, the tickets a clearer top level would prevent, the finance time a better landing page would save. Each has a metric that would raise it (Deliverable A) and a test in the register (IA12, Deliverable B). Deliverable C, C.7 lists them with the rung each would reach.

### 4.6 · Every number labelled

Every number in a case is sourced, measured or assumed, or a published figure kept as context, and the case says which beside it: **sourced**, with its source, sample, date and label; **measured**, from Perqo's own records or tests, with its rung; **assumed**, the case's own, at C0, with the test or read that would replace it. A published figure enters the arithmetic only if it measures the same quantity for a similar product and population; otherwise it is context, shown beside the arithmetic and never inside it. Figure 5 draws the rule as a tree; Deliverable B, B.3 carries it into the template.

## 5 · The limits of the exercise

**The numbers that decide are the ones nobody has.** Deliverable C's break-even turns on three assumptions: how much time a wrong backbone part costs each client a year, how many clients Perqo has, and how long a fault would go unfound without the evidence. Figure 6 there shows the break-even moving from about 12% to about 87% across ranges of those three that no reader could rule out. A case honest about that range supports a decision about evidence, and a weaker one about the structure.

**Averages do not forecast one project.** Moran's 2020 interval, 8% to 104% (RD-27), is the field's own measure of how far one project can sit from the average, and it comes from case studies whose selection the article does not describe.

**Attribution stays open.** A lagging indicator moves for many reasons at once: a release carries more than a structure, a client's onboarding changes the mix of users, a campaign fills the search log (section 2.1; IA11, section 2.5). The model reads a lagging change as a hypothesis about the IA at C1 unless the change was split-tested or the record is of the behaviour itself (IA11, section 6.4).

**Hours of different people are summed.** The case adds Perqo's staff days to clients' admin users' hours. Perqo pays the first; clients pay the second, and Perqo's interest in them runs through renewal (CL-6), which no figure here measures. A decider who counts only Perqo's own hours gets a different break-even, and the case shows both (Deliverable C, C.6).

**A case can be gamed by its targets.** A target set after the read, or a metric chosen because it moved, turns a measure into an argument. IA11's rule that the mark is set before the test (IA11, section 4.4) is the only guard the model has, and section 3.3 extends it to every lagging target.

**Some value has no measure.** A structure that spares support a category of tickets, or lets sales answer a tender truthfully (IA10, BR-3), has value the case can name and cannot price. It is listed in the case as unpriced, and never given a number to make the total look complete.

## Deliverable · A · The IA measurement model

*Face of this artefact (IA2, the notation sheet): measurement model for an IA, one row per metric, leading and lagging, filled for Perqo Admin and the Help centre's search on perqo.com; fidelity F3 (ready to use). Decision: what is measured about the IA, from which data, against which baseline and target, how often, and how much each read can decide. Readers: the IA designer (runs the tests, reads the results), product management (owns RV-06 and RV-10), support (owns RV-04 and RV-05), engineering (the events M-12 to M-14, M-16 and M-19 need), leadership through FO-09 (DL-022, proposed). Leaves out: the app's metrics already in IA11's plan (M-08 to M-10, with V-01 to V-17), M-06, read inside a sort's analysis (IA11, Deliverable D, CS-A), every result (none has been read), money. Owner: the IA designer; version 1, dated 10 November 2026; Perqo is fictional.*

### A.1 · Leading indicators

Every leading metric is IA11's, with IA11's definition and its 95% adjusted-Wald interval (IA11, sections 1.2 and 3.4). Verdicts are IA11's: pass when the interval's lower end is at or above the mark, fail when its upper end is below it, undecided otherwise (IA11, section 4.4).

| ID | Metric | Definition | Source of data | Baseline method | Target | Cadence | Rung |
|---|---|---|---|---|---|---|---|
| M-01 | Success rate | IA11, section 1.2 | tree test of Admin's six areas with admin users from at least four clients, moderated (Deliverable C, E2); perqo.com's trees at RV-11 | the current tree, same tasks, before any change (IA11's TT-0 form) | lower end at or above 80% for deciding a claim and setting budgets, 70% for other Admin tasks | each FO-07 cycle touching Admin's labels or top level; before and after a top-level change (RV-11) | C2 at 12 participants; C3 at 50 |
| M-02 | Directness | IA11, section 1.2 | as M-01 | as M-01 | no mark: read beside M-01 | with M-01 | C2 or C3 |
| M-03 | First-click correctness | IA11, section 1.2 | first-click test on Admin's screens with admin users (AR-45) | the current screens, same tasks | as M-01's marks | each FO-07 cycle | C2 or C3 |
| M-04 | Time on task | IA11, section 1.2 (median) | every test | the same tasks on the current structure | none alone: read beside M-01 | with M-01 | as M-01 |
| M-05 | Placement share | IA11, section 1.2, which defines it for a closed sort; applied here to the given categories of a hybrid sort (this unit's extension) | hybrid card sort with admin users (Deliverable C, E3) | none: the first sort is the baseline | home placement confirmed at a lower end of 50% (IA11, section 4.4) | when an object or label is in question (AR-01, AR-13, AR-14) | C2 at 15; C3 at about 50 |
| M-11 | Problem frequency | IA11, section 1.2 | usability round with five admin users (Deliverable C, E4) | round 1 | no problem in 2 or more of 5 (IA11, section 6.1) | each round | C2 |

### A.2 · Lagging indicators

M-07 is IA11's; M-12 to M-19 are new, defined in section 3.2 and set here (Perqo, fictional). "Range" means the lowest and highest of the four quarters before (or twelve months, for a monthly read).

| ID | Metric | Definition | Source of data | Baseline method | Target | Cadence | Rung |
|---|---|---|---|---|---|---|---|
| M-07 | Zero-result rate | IA11, section 1.2 | the Help centre's search log, For HR and finance teams and For employees | one quarter before, per query, with its interval | no query among the 20 most frequent returns zero results; overall rate's interval of difference not above zero after a change | quarterly, RV-04; the month after a rename | C1 |
| M-12 | Results clickthrough | section 3.2 (new) | the Help centre's log with click events (new) | one quarter before, with its interval | after a search or label change, interval of the difference above zero | quarterly, RV-04 | C1 |
| M-13 | Refinement rate | section 3.2 (new) | as M-12 | as M-12 | interval of the difference below zero | quarterly, RV-04 | C1 |
| M-14 | Search exit rate | section 3.2 (new) | as M-12 | as M-12 | interval of the difference below zero | quarterly, RV-04 | C1 |
| M-15 | Tickets per page | section 3.2 (new) | support's ticket tags by AD- page and DT- tree (IA9, section 6.2) | the range over twelve months, per tag | after a change to a page, two months below its range | monthly, RV-05; a tag that rises after a release | C1 |
| M-16 | Find-to-open time | section 3.2 (new) | Admin's find-field and record-open events (new) | one quarter, median per list and abandonment with its interval | abandonment's interval wholly below 20% on Employees (AD-1) and Approvals (AD-4); above it, AR-34's global search goes to FO-01 as a proposed DL entry | quarterly, RV-06 | C5 |
| M-17 | Landing match | section 3.2 (new) | first actions after sign-in, by role (IA9, RV-06) | the first quarter read is the baseline and AR-37's test | holds while the lower end is above 50%; fails when the upper end is below 50% and the landing pages go to FO-01 | quarterly, RV-06 | C5 |
| M-18 | Overdue share | section 3.2 (new) | claim records and their audit entries (IA7, O-17) | one quarter, with its interval | set at FO-01 from the first read, before any change to Approvals ships | quarterly, RV-06 | C5 |
| M-19 | Flow completion | section 3.2 (new) | Admin's form-start and save events (new) | one quarter per form, with its interval | after a change to a form, interval of the difference not below zero | quarterly, RV-06 | C5 |

### A.3 · Rules for reading the model

1. **Set the target first.** Every target is written in the row before the read it applies to; a target changed after a read is a new row, with the old one kept (IA11, section 4.4).
2. **Read a proportion with its interval.** IA11's 95% adjusted-Wald interval for one proportion; for a change, the interval of the difference of two proportions (IA11, sections 3.4 and 6.2, after Laubheimer 2024 on comparing trees).
3. **Read a count or a median against its range.** No interval method is set for them in the course; the range of the period before is the comparison (this unit's rule).
4. **Keep the kinds apart.** A lagging number is never the verdict on a leading test, nor the reverse (section 3.1); each goes to the register row it tests, at its own rung (IA12, section 3.2), and agreement between a test and a record on one question is convergence, C4 (IA11, section 6.4).
5. **A lagging change is a hypothesis.** Unless the change was split-tested, or the metric records the behaviour itself (M-16 to M-19), a lagging change raises a hypothesis at C1 for a test (IA11, section 6.4; IA9, section 6.4).
6. **Report what moved the other way.** Every read lists the rows, tasks or pages that worsened, as UNC's borrow task did (RD-30), beside the overall figure.

## Deliverable · B · The business-case template

*Face of this artefact (IA2, the notation sheet): one-page business case for IA work in a product company, with its fields, a table of sourced reference ranges with their labels, and the rule for labelling every number; fidelity F3 for the template (ready to fill). Decision: whether to fund a piece of IA work, or the evidence for it, now. Readers: product management (decides at RV-10), leadership (FO-09, one page), the IA designer (writes it), every function whose number it takes. Leaves out: the work's design, the tests' scripts (IA11), a forecast of results. Owner: the IA designer; version 1, dated 10 November 2026; Perqo is fictional.*

### B.1 · The fields

| Field | What to write | Rule |
|---|---|---|
| Decision | the decision, in one line; who decides (IA9, D.1, or the RV-10 ranking); the forum and date | one decision per case (section 4.1) |
| Options | at least: do nothing; the cheapest evidence; the change or the full evidence | each option costed the same way |
| Scope | the artefacts and identifiers, and the register rows (AR-) the case rests on, each with its rung | IA12, section 3.2 |
| Load | volumes the arithmetic uses, each sourced, measured or assumed | section 4.6 |
| Cost of change by layer | per layer touched: staff days by function, and per-client hours | section 4.2; IA9, section 4.2 |
| Cost of not changing | recurring hours while a fault stands; the late change; who pays each | section 4.3 |
| Cost of evidence | per test or read: staff days, participants' hours, the forum it needs, the rung it reaches | section 4.4; IA11, Deliverable A |
| Benefits | each with its metric (Deliverable A), its rung now and the rung the evidence would reach; unpriced value listed as unpriced | section 4.5 |
| Arithmetic | the formula, in words and symbols, and its result | every term labelled |
| Break-even and sensitivity | the value of the unknown at which the options cost the same; the result across a stated low and high for each assumption | section 5 |
| What would change it | the read or test result that would reverse the recommendation | IA11, section 6.1 |
| Audiences | the one-page summary for FO-09; the line for BR-3; what each function gave | IA10, sections 2.9 and 2.4 |
| Number register | every number in the case, with its kind, source and label | B.3 |

### B.2 · Sourced reference ranges

Published figures a case may cite, each with its label and its use. "Reference" means it may appear beside the arithmetic as context; "do not use" means it may appear only as a claim examined. No row enters a Perqo case's arithmetic, because none measures a Perqo quantity (DD-IA1, section 1).

| Quantity | Published range | Source (register) | Label | Use in a case |
|---|---|---|---|---|
| Task completion in usability tests | 78% average; 49% to 92% between the quartiles | RD-16 | consultancy report | reference, for scale |
| Tree-test completion | 66% average, "tentative" | RD-17 | consultancy report | reference; a tree test overestimates live success |
| Share of attempts failing because of the IA | 10% to 14% | RD-18 | consultancy report | reference, for websites |
| Scenario success after a right or wrong first click | .87 against .46 | RD-19 | peer-reviewed | reference, for why M-03 leads |
| Average gain from a UX redesign | 75% (2020; interval 8% to 104%) to 247% (2006 to 2008) | RD-26, RD-27 | consultancy report | reference only, with its interval; never a forecast |
| Before-and-after change from one redesign | 61.6% to 65.1%; 63% to 70%, with one task 79% to 61% | RD-28, RD-30 | maker's report | reference, as examples of what is reported and left out |
| Cost per support contact | $8.01 live; $0.10 self-service | RD-23 | consultancy report (consumer service) | reference; replace with the product's own cost |
| Full resolution by self-service | 9% | RD-23 | consultancy report | reference |
| Annual cost of common tasks per employee | $1,563 to $3,042 by intranet quality (2002) | RD-25 | consultancy report | reference, for intranets only |
| Wages of the people who use a backoffice | $149,280 (HR managers), $166,570 (financial managers), May 2025; wages 70.0% of employer costs (June 2026) | section 4.3 | official statistics (US) | conversion of hours to money, where clients are in the US |
| Time spent searching at work | 15% to 35%; 19% (McKinsey Global Institute, 2012, adjusted from IDC data) | RD-24; section 2.2, claim 3 | consultancy report, no sample | do not use |
| Worldwide cost of poor intranets | $100 billion to $1.3 trillion a year | section 2.2, claim 5 | consultancy estimate | do not use |
| Return on UX spending | "$1 ... returns $100" | section 2.2, claim 1 | practice, unsourced as circulated | do not use |
| Multiplier for a late fix | "100 times" | section 2.2, claim 2 | unverified | do not use |

### B.3 · The rule for each number

Figure 5 draws the rule of section 4.6 as a decision tree, read top-down, every box tone 5, shared, because the rule serves any case. Its questions: "Has the product's own record or test measured it?"; "Is there a published figure for this quantity?"; "Same quantity, similar product and population?". Its answers are yes and no, yes on the left. Its outcomes: "Measured: give the rung and the date"; "Sourced: in the arithmetic, with source, sample, date and label"; "Context only: beside the arithmetic, labelled"; "Assumed (C0): name the read or test that replaces it".

```viz
{"kind": "decision", "caption": "Decision tree: how each number in a business case for IA work is labelled and where it may stand; supports the decision on whether a number enters the case's arithmetic (section 4.6; Deliverable B, B.3). Labels from section 1.1; rungs from IA11, section 6.4; the rule that published evidence about other products is a reasoned default for Perqo from DD-IA1, section 1; assumptions at C0 named with their test as IA12, section 3.2 records them. Every box tone 5, shared: the rule serves any case. Perqo is fictional.", "root": {"q": "Has the product's own record or test measured it?", "tone": 5, "branches": [
 {"label": "yes", "to": {"outcome": "Measured: give the rung and the date", "tone": 5}},
 {"label": "no", "to": {"q": "Is there a published figure for this quantity?", "tone": 5, "branches": [
  {"label": "yes", "to": {"q": "Same quantity, similar product and population?", "tone": 5, "branches": [
   {"label": "yes", "to": {"outcome": "Sourced: in the arithmetic, with source, sample, date and label", "tone": 5}},
   {"label": "no", "to": {"outcome": "Context only: beside the arithmetic, labelled", "tone": 5}}]}},
  {"label": "no", "to": {"outcome": "Assumed (C0): name the read or test that replaces it", "tone": 5}}]}}]}}
```

The number register in each case has these columns: the number; what it measures; its kind (measured, sourced, context, assumed; a number computed from others is marked arithmetic, and a cost taken from a filed Perqo plan is marked as that plan's); its source, sample, date and label, or its rung, or the read that would replace it; where in the case it is used.

## Deliverable · C · The case filled for Perqo Admin

*Face of this artefact (IA2, the notation sheet): business case for the first evidence package on Perqo Admin's IA, filled in the template of Deliverable B; fidelity F2 (complete for its scope; every number labelled). Decision: whether product management ranks the first FO-07 evidence package for Admin's backbone into the next cycle, at RV-10, or holds the backbone at C0 and reads the records only. Readers: product management, leadership (C.9, at FO-09), the IA designer, customer success, support, engineering. Leaves out: any change to Admin's IA (none is proposed), money for Perqo's staff (its rate is not set), clients' own costs beyond their admin users' hours. Owner: the IA designer; version 1, dated 10 November 2026; every number in it is a Perqo fact or this unit's assumption; Perqo is fictional.*

### C.1 · Decision and options

**Decision.** Whether the first FO-07 evidence package for Admin's backbone (E2 to E4 below) is ranked into the next cycle at RV-10, decided by product management, which owns RV-10 (IA9, Deliverable C), and shown to leadership at FO-09 (Perqo, fictional).

| Option | What it is | Cost (C.5) |
|---|---|---|
| O-1 Hold | keep every row at C0; read nothing | none now |
| O-2 Records only | E1: the first quarterly read of Admin's records at RV-06, lifting AR-02 and AR-37, and the other rows records can reach, to C1 or C5 | 1.5 staff days a quarter |
| O-3 Records and package | E1 with E2 to E4: a moderated tree test, a hybrid card sort and a usability round with admin users at FO-07 | 1.5 staff days a quarter, and 9 staff days and 14.75 hours of admin users once |

### C.2 · Scope

Perqo Admin's IA as IA7 drew it, pages AD-0 to AD-6 (IA7, Deliverable C, C.1), and its register, AR-01 to AR-49, every row at C0 and not run on 10 November 2026 (IA12, Deliverable B). The package touches seven of the 25 backbone rows: AR-01, AR-13 and AR-14 (objects and their names), AR-24 and AR-27 (the six areas, and a list and a detail per object), AR-03 and AR-06 (the employee's lifecycle, the rejection note), and three open rows, AR-25, AR-29 and AR-34 (IA12, Deliverable B, B.1 and B.3).

### C.3 · Load

| Number | What | Kind | Source | Replaced by |
|---|---|---|---|---|
| 1,200 | employees at the sizing client | assumed, C0 | IA7, section 2.2; AR-02 | E1, analytics on live clients |
| 3 | admin users at the sizing client (two HR, one finance) | assumed, C0 | IA7, section 2.2 | E1 |
| 180 | claims a month in Approvals (15% of about 1,200) | assumed, C0 | IA7, section 2.2 | E1; M-18's read |
| 9 | claims a working day in Approvals | assumed, C0 | IA7, section 2.2, over 20 working days | E1 |
| 20 | clients like the sizing client, now | assumed, C0, for this case only | this unit (Perqo, fictional) | the client count, from customer success |
| 1 | new client a month | assumed, C0, for this case only | this unit (Perqo, fictional) | customer success's pipeline |

### C.4 · Cost of change by layer

Staff days of a late change to each layer, by function, and per-client hours; every figure this unit's assumption (Perqo, fictional) except the structure test's 1.5 days, which is IA11's cost for V-17 (IA11, Deliverable A). Totals are drawn in figure 4 (section 4.2).

| Layer | Fix (IA12) | IA designer | Structure test (RV-11) | Engineering | Content, support, sales | Total staff days | Per client, hours |
|---|---|---|---|---|---|---|---|
| Objects | backbone | 3 | 0 | 15 | 4 | 22 | 4 |
| Roles | backbone | 2 | 0 | 10 | 3 | 15 | 4 |
| Top level | backbone | 2 | 1.5 | 4 | 3 | 10.5 | 4 |
| Vocabulary | backbone | 1 | 0 | 3 | 4 | 8 | 1 |
| Addresses | backbone | 1 | 0 | 4 | 2 | 7 | 0 |
| Reports | open | 0.5 | 0 | 2 | 0.5 | 3 | 0 |
| Lower labels | open | 0.5 | 0 | 0.5 | 1 | 2 | 0 |
| Queues | open | 0.5 | 0 | 1 | 0.5 | 2 | 0 |
| Lists | open | 0.5 | 0 | 1 | 0 | 1.5 | 0 |
| Landing | open | 0.5 | 0 | 0.5 | 0.5 | 1.5 | 0 |

What each figure counts: the IA designer's days are IA9's steps 2, 3, 6 and 7 (log, impact check, vocabulary, artefacts and faces); engineering's are the build, migration and redirects; content, support and sales are Help centre articles for HR and finance teams, ticket tags, and BR-3 re-issued (IA9, section 4.2; IA10, BR-3). Per client: customer success's hour and each admin user's hour relearning (Perqo, fictional).

### C.5 · Cost of evidence

| ID | Evidence | Register rows | Participants | Staff days | Participants' hours | Rung it reaches | Unit cost from |
|---|---|---|---|---|---|---|---|
| E1 | quarterly read of Admin's records at RV-06: first actions after sign-in, page views, claim records | AR-02, AR-37 and the rows read at RV-06 | none | product management 1, engineering 0.5 | 0 | C5 for AR-02 and AR-37; C1 or C5 for others | IA11, V-01 |
| E2 | moderated tree test of Admin's six areas, 30 minutes each | AR-24, AR-27 | 12 admin users from at least four clients | IA designer 3 | 6 | C2 | IA11, V-03 (assumed to carry); 10 to 15 sessions after IA11, section 3.2 |
| E3 | hybrid card sort of Admin's objects and their names, 20 minutes each, in E2's twelve sessions and three more | AR-01, AR-13, AR-14 | 15 admin users from at least five clients | IA designer 2 | 5 | C2 | 15 participants after IA11, section 3.1; days assumed |
| E4 | usability round: a run of ten decisions, find this employee and this claim, invite and mark as left | AR-03, AR-06, AR-25, AR-29, AR-34 | 5 admin users | IA designer 3 | 3.75 | C2 | IA11, V-03 |
| Recruiting | arranging E2 to E4 through clients, at FO-07 | | | customer success 1 | | | assumed |

E2 to E4 with recruiting: 9 staff days, and 14.75 hours of admin users' time; at an assumed 8 hours a staff day, 86.75 hours in all (this unit's arithmetic). E1: 1.5 staff days a quarter. E3's 15 participants, at three admin users a client, need at least five clients at FO-07, which is the package's precondition.

### C.6 · Cost of not changing, and the break-even

O-3 differs from O-2 in one thing: a fault in one of the seven backbone rows the package touches is found now, at C2, instead of later, when it surfaces in tickets at C1 and waits for a test (IA11, section 6.4). The change costs the same staff days either way (C.4); what finding it earlier saves is the time the fault costs clients while it stands, and the re-training of clients onboarded on the wrong structure in the meantime.

The arithmetic (this unit's; every term assumed, Perqo, fictional):

- f, hours a fault in a backbone part costs one client a year: **10** (three admin users losing about 4 minutes a week each over 48 working weeks is 9.6 hours, rounded); low 2, high 20.
- N, clients now: **20**; low 10, high 40.
- g, new clients a year: **12**.
- d, years before the fault is found without the package: **1**; low 0.5, high 2.
- r, hours of re-training a client per fault: **4** (C.4).
- E, the package's cost: **86.75 hours** (C.5).

Hours saved per fault found early, A = f × (N × d + g × d² ÷ 2) + r × g × d = 10 × (20 + 6) + 48 = **308 hours**. The package pays for itself when the chance p that at least one of the seven rows is wrong satisfies p × A ≥ E, so the break-even is p = E ÷ A = 86.75 ÷ 308, about **28%**. The sum mixes payers (section 5). Counted on Perqo's hours alone, the package costs 72 staff hours and saves 12, customer success's hour for each of the 12 clients not re-trained, so it never pays for itself on Perqo's own time: its case for Perqo rests on clients' time, which reaches Perqo through renewal (CL-6) and is not measured. Counted on clients' hours alone, it costs 14.75 and saves 296 (260 of time lost and 36 of admin users' re-training), a break-even of about 5%. As a conversion only, at the US HR manager's $102.53 an hour with employer costs (section 4.3), clients' 14.75 hours are about $1,512 and their 296 hours about $30,349 (this unit's arithmetic; Perqo's clients' countries are not set).

Figure 6 draws the break-even across each assumption's range with the others held, every row tone 4: Fault cost a client a year, 2 to 20 hours, from 15.3% to 86.8%; Clients now, 10 to 40, from 17.1% to 41.7%; Years to find without it, 0.5 to 2, from 11.8% to 62.4%; each with the base case's 28.2% as its point, and each end tagged "assumed".

```viz
{"kind": "range", "unit": "%", "min": 0, "max": 100, "ticks": [0, 25, 50, 75, 100], "caption": "Break-even sensitivity: the chance of a fault in the seven backbone rows at which the FO-07 evidence package costs what it saves, across each assumption's range with the others held at the base case; supports the decision on whether to rank the package into the next cycle (Deliverable C, C.6; section 5). Arithmetic and every assumption this unit's, Perqo, fictional, C0; the package's unit costs from IA11, Deliverable A (V-01, V-03); load from IA7, section 2.2. Low and high ends are the assumption's high and low values. Every row tone 4, Perqo Admin.", "rows": [
 {"label": "Fault cost a client a year, 2 to 20 hours", "low": 15.3, "high": 86.8, "point": 28.2, "low_src": "assumed", "high_src": "assumed", "tone": 4},
 {"label": "Clients now, 10 to 40", "low": 17.1, "high": 41.7, "point": 28.2, "low_src": "assumed", "high_src": "assumed", "tone": 4},
 {"label": "Years to find without it, 0.5 to 2", "low": 11.8, "high": 62.4, "point": 28.2, "low_src": "assumed", "high_src": "assumed", "tone": 4}]}
```

**What the case concludes.** No published or Perqo figure gives p. The nearest Perqo evidence is the app pilot, where one of ten tasks failed its mark at 12 participants and eight were undecided (IA11, Deliverable D, TT-A): a C2 result about a different surface. The nearest published figure, 10% of task attempts failing because of the IA on 24 websites (RD-18), counts failed attempts on sites unlike Admin, a different quantity from wrong structural decisions. The case therefore supports one decision firmly and one conditionally. **O-2 now**: E1 costs 1.5 staff days, needs no recruiting, and replaces the load the whole case argues from (AR-02) with measured figures; nothing in the arithmetic argues against it. **O-3 when five clients agree to FO-07**, if product management judges p above the break-even for the measured N and the measured d; at the base case that is a better than one-in-four chance that at least one of seven untested backbone answers is wrong.

What would change it: the client count from customer success (N) and the reads bearing on f (M-15 at RV-05; M-16 once its find-field event is recorded, section 3.2) move the break-even directly; a C2 failure in E2 or E3 turns the package's cost into a found fault, and the change goes to the decision log by IA9's flow (IA9, section 4.2).

### C.7 · Benefits, each at its rung

| Benefit claimed | Metric (Deliverable A) | Register rows | Rung now | Rung after O-2 | Rung after O-3 |
|---|---|---|---|---|---|
| HR finds and decides claims without losing its place | M-11; M-16; M-18 | AR-29, AR-34, AR-41 | C0 | C5 for M-18; C5 for M-16 once its find-field event is recorded (section 3.2) | C2 for the list and detail |
| Admin users find each area where they look | M-01; M-02; M-15 | AR-24, AR-27 | C0 | C1 from tickets | C2 |
| Admin users recognise their objects and names | M-05 | AR-01, AR-13, AR-14 | C0 | C0 | C2 |
| Each role lands where its work is | M-17 | AR-37 | C0 | C5 | C5 |
| Fewer tickets about where things are in Admin | M-15 | AR-45 | C0 | C1 | C1; C4 with a first-click test (AR-45) |
| Sales can answer a tender truthfully about roles and rules | none | AR-16, AR-17 | C0 | C0 | C0: unpriced |

### C.8 · Number register

| Number | Measures | Kind | Source, or the read that replaces it |
|---|---|---|---|
| 1,200; 3; 180; 9 | load | assumed, C0 | IA7, section 2.2; replaced by E1 |
| 20; 12 a year | clients now; new clients a year | assumed, C0 | this unit; customer success |
| 22, 15, 10.5, 8, 7, 3, 2, 2, 1.5, 1.5 | staff days of a late change by layer | assumed, C0 | this unit; engineering and content give their days at FO-01 |
| 1.5 | structure test, IA designer's days | Perqo's plan | IA11, Deliverable A, V-17 |
| 3; 5 × 45 minutes | a usability round | Perqo's plan | IA11, Deliverable A, V-03 |
| 1 and 0.5 | a quarterly records read | Perqo's plan | IA11, Deliverable A, V-01 |
| 12; 15; 5 | participants in E2, E3, E4 | assumed, within published guidance | IA11, sections 3.1 and 3.2; Nielsen 2000 through IA11, section 2.6 |
| 4; 1 | per-client hours of a change | assumed, C0 | this unit; customer success |
| 10 (2 to 20) | hours a fault costs a client a year | assumed, C0 | this unit; M-15 and M-16 after E1 |
| 1 (0.5 to 2) | years to find a fault without the package | assumed, C0 | this unit |
| 8 | hours in a staff day | assumed | this unit |
| 10 to 40 | range of clients now | assumed, C0 | this unit; customer success |
| 4 minutes a week; 48 working weeks | the working behind the 10 hours | assumed, C0 | this unit; M-16 once its event is recorded |
| 30; 20 minutes | session length of E2; of E3 | assumed | this unit |
| 3; 2; 1 | staff days of E2, E3 and recruiting | assumed | this unit; E2's carried from IA11, V-03 |
| 9; 14.75; 72; 12; 296; 5% | staff days and participants' hours of E2 to E4; Perqo's hours spent and saved; clients' hours saved and their break-even | arithmetic | C.5 and C.6 |
| 15.3% to 86.8%; 17.1% to 41.7%; 11.8% to 62.4% | the break-even across each assumption's range | arithmetic | C.6, figure 6 |
| 86.75; 308; 28% | the package's hours; hours saved per fault; break-even | arithmetic | C.5 and C.6 |
| $149,280; $166,570; 70.0%; 2,080; $102.53; $1,512; $30,349 | wages, employer costs and the conversion of C.6, for conversion only | sourced, official statistics (US); 2,080 hours assumed | BLS, section 4.3 |
| $8.01 | cost per live contact, context only | sourced, consultancy report | RD-23 |
| 10% | attempts failing because of the IA, context only | sourced, consultancy report | RD-18 |

### C.9 · For leadership and for sales

**The page at FO-09** (F1, one page; IA10, section 2.9):

> **Admin's IA: what we know and what it would cost to know more.** All 49 rows of Admin's assumption register, its structural decisions with four assumptions from other units and three open questions, stand on reasoning, none on a test or a read (AR-01 to AR-49; 25 of them backbone, expensive to change once built). Reading our own records once costs 1.5 staff days a quarter and replaces our assumed volumes with measured ones: ranked now (O-2). Testing seven backbone decisions with admin users costs 9 staff days and about 15 hours of five or more clients' admin users' time (O-3). It saves more than it costs if the chance that at least one of the seven is wrong is above about 28%, a figure that moves between 12% and 87% with assumptions we can replace with the first records read. Most of what it saves is clients' admin users' time; on our own staff hours alone it does not pay, and its value to us runs through renewal, which we do not measure. Decision at RV-10 by product management; next review after the first read.

**The line for BR-3**, proposed in DL-021: "No figure for time saved or ease of use in Admin is given to a buyer until a measure at C3 or above is on record; until then, say what Admin does and what it does not do."

## Deliverable · D · Decision log entries proposed

Both entries use IA12's template (IA12, Deliverable D, D.1), with its proposed fields, positions (DL-011) and register rows (DL-017), filled as they would be if accepted. Neither changes a filed artefact until it is decided; the filing chat applies nothing.

### D.1 · DL-021: what sales may claim about Admin's ease of use

| Field | DL-021 |
|---|---|
| Change | BR-3, "What Perqo does not do", gains the line: "No figure for time saved or ease of use in Admin is given to a buyer until a measure at C3 or above is on record; until then, say what Admin does and what it does not do." |
| Raised by, from | DD-IA2, sections 2.2 and 4.1: every Admin row at C0 (IA12, section 3.4); published averages that cannot forecast one product (RD-26, RD-27) |
| Touches | IA10, Deliverable B, BR-3; FO-04's inputs (IA10, A.2); no J- row |
| Register rows (proposed) | AR-01 to AR-49, as the evidence the line waits on |
| Alternatives considered | quote NN/g's average gains as "industry figures" (a forecast without evidence, section 2.2, claim 6); say nothing (leaves sales to choose its own figures) |
| Positions (proposed) | none recorded; sales to be asked at the next FO-04 |
| Decided by | IA designer, consulting product management: inside one artefact, renaming nothing (IA9, D.1), as DL-019 is |
| Decide at | FO-01, the IA review's next meeting; sales told at the next FO-04 |
| Decision, date, reason | not decided |
| Version effect | a dated amendment to IA10, Deliverable B: it adds a line and breaks no citation (IA9, section 4.4) |
| Places to apply | IA10, BR-3, "What Perqo does not do": the line added; BR-3 re-issued at FO-04; not done |
| Told (DL-012, proposed) | sales at FO-04; product management at FO-01 |
| Supersedes, superseded by | none |
| Status | proposed |

### D.2 · DL-022: the measurement model's read on the leadership page

| Field | DL-022 |
|---|---|
| Change | The one-page map for leadership (TP-12) adds, each quarter, the latest read of M-15 to M-19 for Admin with each one's interval or range, and any business case decided that quarter with its break-even |
| Raised by, from | DD-IA2, section 4.1 and Deliverable C, C.9 |
| Touches | IA10, section 2.9 and A.1, TP-12's artefact; FO-09's inputs (IA10, A.2) |
| Register rows (proposed) | AR-02, AR-37, AR-41, as the rows the reads move |
| Alternatives considered | send leadership Deliverable A itself (the wrong format for the keep-satisfied quadrant, IA10, section 1.4); report reads only at RV-10 (leadership does not attend) |
| Positions (proposed) | none recorded |
| Decided by | IA designer, consulting product management, which prepares TP-12: inside one artefact, renaming nothing (IA9, D.1) |
| Decide at | FO-01, the IA review's next meeting, with DL-019 |
| Decision, date, reason | not decided |
| Version effect | a dated amendment to IA10, Deliverable A |
| Places to apply | IA10, section 2.9 and A.1, TP-12's artefact cell: add "M-15 to M-19 for Admin, latest read; cases decided this quarter"; A.2, FO-09's inputs: add "the measurement model's Admin reads"; each not done |
| Told (DL-012, proposed) | product management at FO-01; leadership at FO-09 |
| Supersedes, superseded by | none |
| Status | proposed |

## What later units take

**DD-IA3** takes taxonomy and governance to scale, in several languages and markets. From this unit it takes the measurement model (Deliverable A) as the set of reads its governance forums receive, with M-07 and M-12 to M-14 to be read per language once the Help centre has more than one (TP-05, dormant); the business-case template (Deliverable B) as the form in which a case for taxonomy work at scale is made, with its rule that every number is measured, sourced, context or assumed; and DL-021 and DL-022 as the log's state at this unit's date, beside DL-011 to DL-020.

**The final audit** takes the evidence register RD-16 to RD-31 as the claims to sample, each with its source, sample, date and label; section 2.2's six claims as the list of figures the course has examined and refused; the new metrics M-12 to M-19 and the marks for Admin's tests as Perqo facts to check against IA11; and Deliverable C's number register (C.8) as the test of whether every number in the case is traced or labelled. Both the model and the template are built to be used without the rest of the course: each row cites the unit that defines it.

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA12 or DD-IA1 label, object, attribute or relationship. DL-021 and DL-022 are proposed, so no filed artefact changes at this unit's filing.

| Fact | Set in | Left free |
|---|---|---|
| Metrics M-12 results clickthrough, M-13 refinement rate, M-14 search exit rate (the Help centre's search), M-15 tickets per page, M-16 find-to-open time with find abandonment, M-17 landing match, M-18 overdue share, M-19 flow completion (Admin), each with one definition | section 3.2 | none |
| The measurement model: fifteen metrics, M-01 to M-05, M-07, M-11 to M-19, with source of data, baseline method, target, cadence and rung | Deliverable A | every result |
| Marks for Admin's leading tests: 80% for deciding a claim and setting budgets, 70% for every other Admin task | section 3.3; Deliverable A, A.1 | marks for perqo.com's tests |
| Lagging targets as A.2 gives them, among them M-16's find abandonment under 20% on AD-1 and AD-4, above which AR-34's global search goes to FO-01 | Deliverable A, A.2 | M-18's target, set at FO-01 after the first read |
| New records: a click event on the Help centre's results page; find-field, record-open, form-start and save events in Admin | section 3.2 | how long events are kept |
| Lagging baselines: one full quarter before; counts and medians read against the range of the period before | section 3.3; Deliverable A, A.3 | none |
| The business-case template's fields, the reference-range table and the number rule | Deliverable B | none |
| Staff days of a late change by layer, by function, and per-client hours, as C.4 gives them, all assumed | Deliverable C, C.4 | measured days |
| The evidence package E1 to E4, with its participants, staff days and rungs; at least five clients at FO-07 as its precondition | Deliverable C, C.5 | when it runs |
| For this case only, assumed: 20 clients like the sizing client and 1 new client a month; f 10 hours, d 1 year, r 4 hours, 8 hours a staff day | Deliverable C, C.3 and C.6 | the real client count |
| The case's conclusion: O-2 ranked now; O-3 when five clients agree to FO-07 and p is judged above the break-even | Deliverable C, C.6 | product management's decision at RV-10 |
| DL-021, proposed: BR-3 gains a line on figures for ease of use | Deliverable D, D.1 | its decision |
| DL-022, proposed: the leadership page adds Admin's lagging reads and the quarter's decided cases | Deliverable D, D.2 | its decision |
| The evidence register continues DD-IA1's identifiers, RD-16 to RD-31; later readings take RD-32 onward | section 1.6 | none |

## Sources

- Anderson, Adam. "User Experience (UX) turns your $1 investment into a $100 return…really?" Mindset Consulting, 20 October 2021 (practice). Read 10 November 2026. [mindsetconsulting.com, UX return](https://www.mindsetconsulting.com/user-experience-ux-turns-your-1-investment-into-a-100-return-really/)
- Boehm, Barry, and Victor R. Basili. "Software Defect Reduction Top 10 List". *Computer* 34, no. 1 (January 2001): 135 to 137. Catalogue record with abstract, read 10 November 2026; the article was not seen. [umiacs.umd.edu, record](https://umiacs.umd.edu/node/12156)
- Bossavit, Laurent. *The Leprechauns of Software Engineering*. Leanpub, page dated 20 December 2025. Ch. 10, "The cost of defects: an illustrated history"; appendix B. Contents only. [leanpub.com, Leprechauns](https://leanpub.com/leprechauns)
- Bureau of Labor Statistics. *Occupational Outlook Handbook*, "Human Resources Managers", last modified 29 October 2026 (official statistics). Read 10 November 2026. [bls.gov, HR managers](https://www.bls.gov/ooh/Management/human-resources-managers.htm)
- Bureau of Labor Statistics. *Occupational Outlook Handbook*, "Financial Managers", last modified 27 August 2026 (official statistics). Read 10 November 2026. [bls.gov, financial managers](https://www.bls.gov/OOH/management/financial-managers.htm)
- Bureau of Labor Statistics. "Compensation costs for private industry workers averaged $46.89 per hour worked in June 2026". *The Economics Daily*, 17 September 2026 (official statistics). Read 10 November 2026. [bls.gov, compensation costs](https://www.bls.gov/opub/ted/2026/compensation-costs-for-private-industry-workers-averaged-46-89-per-hour-worked-in-june-2026.htm)
- Chui, Michael, James Manyika, Jacques Bughin, Richard Dobbs, Charles Roxburgh, Hugo Sarrazin, Geoffrey Sands and Magdalena Westergren. *The social economy: Unlocking value and productivity through social technologies*. McKinsey Global Institute, July 2012 (consultancy report). Read 10 November 2026. [mckinsey.com, social economy](https://mckinsey.com/~/media/McKinsey/Industries/Technology%20Media%20and%20Telecommunications/High%20Tech/Our%20Insights/The%20social%20economy/MGI_The_social_economy_Full_report.ashx)
- Cohn, Mike. "The Cost of Change Curve Is Outdated". Mountain Goat Software, last updated 3 March 2026 (practice). Read 10 November 2026. [mountaingoatsoftware.com, cost of change](https://www.mountaingoatsoftware.com/blog/the-cost-of-change-curve-is-outdated)
- Dub, Sam. "Rolling out a new design for browsing GOV.UK by topic". Inside GOV.UK, 8 August 2022 (maker's report). Read 10 November 2026. [insidegovuk.blog.gov.uk, browsing by topic](https://insidegovuk.blog.gov.uk/2022/08/08/rolling-out-a-new-design-for-browsing-gov-uk-by-topic/)
- Feldman, Susan. "The high cost of not finding information". KMWorld, 1 March 2004 (consultancy report, IDC). Read 10 November 2026. [kmworld.com, not finding information](https://www.kmworld.com/Articles/Editorial/Feature/The-high-cost-of-not-finding-information-9534.aspx)
- Fraser, Catriona, Christian Sutter and Tara Stockford. "A new search engine for GOV.UK". Inside GOV.UK, 23 October 2024 (maker's report). Read 10 November 2026. [insidegovuk.blog.gov.uk, new search engine](https://insidegovuk.blog.gov.uk/2024/10/23/a-new-search-engine-for-gov-uk/)
- Gartner. "Gartner Says Only 9% of Customers Report Solving Their Issues Completely via Self-Service". Press release, 25 September 2019 (consultancy report). Read 10 November 2026. [gartner.com, self-service](https://www.gartner.com/en/newsroom/press-releases/2019-09-25-gartner-says-only-9--of-customers-report-solving-thei)
- Katz, Michael A., and Michael D. Byrne. "Effects of Scent and Breadth on Use of Site-Specific Search on E-Commerce Web Sites". *ACM Transactions on Computer-Human Interaction* 10, no. 3 (September 2003): 198 to 220. Abstract read 10 November 2026. [unpaywall.org, Katz and Byrne](https://unpaywall.org/10.1145%2F937549.937551)
- Moran, Kate. "UX Gains Shrinking". Nielsen Norman Group, 1 November 2020. Read 10 November 2026. [nngroup.com, UX gains shrinking](https://www.nngroup.com/articles/ux-gains-shrinking/)
- Nielsen, Jakob. "Foreword to Information Architecture (2nd edition)". Nielsen Norman Group, 1 June 2002. Read 10 November 2026. [nngroup.com, foreword](https://www.nngroup.com/articles/foreword-ia-2nd/)
- Nielsen, Jakob. "Intranet Usability: The Trillion-Dollar Question". Nielsen Norman Group, 10 November 2002. Read 10 November 2026. [nngroup.com, intranet usability](https://www.nngroup.com/articles/intranet-usability-the-trillion-dollar-question/)
- Nielsen, Jakob. "Usability ROI Declining, But Still Strong". Nielsen Norman Group, 21 January 2008. Read 10 November 2026. [nngroup.com, usability ROI](https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/)
- Nielsen, Jakob. "IA Task Failures Remain Costly". Nielsen Norman Group, 15 April 2009. Read 10 November 2026. [nngroup.com, IA task failures](https://www.nngroup.com/alertbox/ia-failures.html)
- Porton, Jonathan. "No longer taxing – we hope". ONS Digital blog, 5 December 2013 (maker's report). Read 10 November 2026. [digitalblog.ons.gov.uk, taxonomy](https://digitalblog.ons.gov.uk/2013/12/05/no-longer-taxing-we-hope)
- Pshock, Daniel, and Chad Haefele. "Assessing nav changes". UNC Libraries UX blog, dated 19 May 2016 in its address (maker's report). Read 10 November 2026. [libux.web.unc.edu, nav changes](https://libux.web.unc.edu/2016/05/19/assessing-nav-changes/)
- Sauro, Jeff. "What Is A Good Task-Completion Rate?" MeasuringU, 21 March 2011 (consultancy report). Read 10 November 2026. [measuringu.com, task completion](https://measuringu.com/task-completion/)
- Sauro, Jeff. "Using Tree-Testing To Test Information Architecture". MeasuringU, 26 March 2013 (consultancy report). Read 10 November 2026. [measuringu.com, tree testing](https://measuringu.com/tree-testing-ia/)
- Spool, Jared M. "Are There Users Who Always Search?" UIE, 1 May 2001 (consultancy report, practice). Read 10 November 2026. [articles.centercentre.com, always search](https://articles.centercentre.com/?p=15)
- SWOOP Analytics. "How one organisation made intranet information 53% faster to find". Case study by Sharon Dawson, 27 July, year not stated (vendor, anecdote). Read 10 November 2026. [swoopanalytics.com, case study](https://www.swoopanalytics.com/case-studies/intranet-information-faster-to-find)
- Wayne, Hillel. "I ****ing hate Science". *Computer Things*, 19 July 2021 (practice). Read 10 November 2026. [buttondown.com, Hillel Wayne](https://buttondown.com/hillelwayne/archive/i-ing-hate-science/)
- Cited through the filed units, for claims made there: Bailey, Wolfson, Nall and Koyani, "Performance-Based Usability Testing", *HCII 2009*, LNCS 5619 (IA11); Barker, "Measuring the Success of a Classification System", Boxes and Arrows, 2007 (IA11; practice); Dub, "Our plans to improve navigation on GOV.UK", GDS blog, 2021 (DD-IA1); Farrell, "Search-Log Analysis", NN/g, 2017 (IA3); Laubheimer, "Tree Testing Part 2: Interpreting the Results", NN/g, 2024 (IA11); Nielsen, "Search and You May Find", NN/g, 1997 (IA3); Nielsen, "Why You Only Need to Test with 5 Users", NN/g, 2000 (IA11). Full references in IA3, IA11 and DD-IA1, Sources.

## Unsure list

- Boehm and Basili 2001: only the catalogue record and the abstract's first sentence were read; the article's ratios are unverified here and are not used.
- McKinsey Global Institute 2012: the "19%" is in the report (the main text beside Exhibit 20, and Exhibit A7, 8.8 hours of 46.5); "1.8 hours a day" does not appear there and is 8.8 hours over five days, rounded; the sample behind the IDC data the report adjusts was not found in the passages read.
- Gartner 2019: the release ties the 8,398 customers to the channel preferences; whether the 9% comes from the same survey is not stated.
- Moran 2020: read through a summary of the page; the figures and the interval are as the summary gave them, and the page's exact wording was not checked line by line.
- Katz and Byrne 2003: the number of participants in each study was not on the record read; the authors' first names, issue and pages are from knowledge and IA3's citation.
- Pshock and Haefele: the year comes from the post's address; the page gives only April 15 to 25 for the test, with no year, and the "before" test's sample and date are not given.
- Spool 2001 appears on articles.centercentre.com, the site of Spool's company; the original UIE publication was not seen.
- Anderson 2021: the post's link suggests the Forrester report is titled "The ROI of Design Thinking, Part 1: Overview"; the report was not seen, and its contents are unknown.
- Nielsen 2009: how failures were attributed to the IA is given only as a scheme described in *Prioritizing Web Usability*, which was not read.
- Object: the business case for Perqo Admin's IA, with its cost of change by layer and its break-even, Deliverable C
- Fresh check 2026-11-10 (Fable 5.2): fix · 2 error, 11 should-fix, 7 minor; all applied as verified (three minors needing no change); figures 3 to 6 passed the fresh check; figures 1 and 2, changed by its findings, passed their fourth check; report `audits/ux/fresh-check-DD-IA2.md`
