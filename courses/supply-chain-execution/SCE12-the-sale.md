---
code: SCE12
title: The sale
course: supply-chain-execution · SCE · Supply Chain Execution for Product Teams
model: Opus 5.5
written: 2026-11-28
search: on
intro: How a selection runs from trigger to contract, what decides each of eight stages and what each cannot show, from buying research, analyst and review-site pages and US public tenders; deliverable: the stage sheet, built for Corvane (fictional).
---

# SCE12 · The sale

SCE11 described the people on a buying committee. This unit follows them through the selection itself, stage by stage: what happens at each stage, what decides it, and what it cannot show the people deciding. Grades follow SCE1's key (section 10 there): **independent**, **analyst**, **vendor-reported**, **practice**. As in SCE5 and SCE11, a line that rests on no opened source is a **working description**: the course's own account, graded nothing and never used as evidence. Case facts are marked [register]; facts this unit adds to the case are listed in the notes. Every web page cited was read on 28 November 2026 unless another date is given.

Three limits hold through the unit.

- **No study of a warehouse, transport or order system selection was found.** The research opened is on enterprise resource planning (ERP) and other packaged software, or on business-to-business buying in general, and most of it was read in abstract only. Applying it to execution software is this unit's inference.
- **The published requirement lists opened are public bodies' tenders**, all from the United States; the UK and New Zealand pages read are guidance on evaluation, not tenders. A public body buys under procurement rules that a private retailer such as Corvane (fictional) does not follow; what transfers is the shape of the documents; the rules stay with the public body (this unit's inference). Which rules bind a given company is a question for its legal counsel.
- **The free selection templates found were published by software vendors, by integrators or by trade magazines**, which this course does not use as sources (SCE11 §6). The analyst firms' templates are paid, so only their public pages were read; no Gartner buying guide, toolkit or market guide was read here (flag F130). Robinson, Faris and Wind (1967) and Webster and Wind (1972) were not opened either (flag F129); section 1 gives them as Grewal et al. (2015) describe them.

## 1. The stages, and where the stage model comes from

A **selection** is the work a company does from deciding it may need new software to signing a contract for one product. This course names eight stages, in the order a buyer usually meets them: the trigger, the long list, the request for information, the request for proposal, the scripted demonstration, reference calls and site visits, a proof of concept where there is one, and negotiation and contract. The list and the order are the course's, taken from the brief; the sources below say how far the order holds.

**The classic model is a sequence.** A review of business-to-business buying by twelve authors describes the "BuyGrid" of Robinson, Faris and Wind (1967) as a sequential series of decision-making stages, and the classic view, which it credits to Robinson et al. and to Webster and Wind (1972), as covering information gathering, product evaluation and negotiation, and purchase and usage; it links that process to "creeping commitment", where each choice removes some alternatives (pp. 195, 200–201) ([Grewal et al., 2015](https://doi.org/10.1007/s40547-015-0040-5), read in full) [practice: a review with no measurement of its own]. The same review argues that modern buying is not like that: "These processes are contemporaneous rather than sequential" (p. 195) [practice].

**The analysts' model is a set of jobs done in any order.** Gartner's page on the business-to-business buying journey names six buying jobs (problem identification, solution exploration, requirements building, supplier selection, validation and consensus creation) and says the journey "doesn't play out in any kind of predictable, linear order" ([Gartner, "The B2B Buying Journey", undated](https://www.gartner.com/en/sales/insights/b2b-buying-journey)) [analyst: the page states no sample or date]. Info-Tech Research Group's page on running a request for proposal gives seven steps: identify need, define business requirements, gain business authorisation, perform the request for information or proposal, negotiate agreement, purchase, and assess and measure performance ([Info-Tech, "Drive Successful Sourcing Outcomes With a Robust RFP Process", published 11 Aug 2020, last modified 24 Jul 2023](https://www.infotech.com/research/ss/drive-successful-sourcing-outcomes-with-a-robust-rfp-process)) [analyst].

**One ERP case shows the stages looping.** Verville and Halingten followed one ERP acquisition at a holding company for a gas and electric utility and a non-utility energy business; it took about six months, and they found six iterative, recursive and interrelated processes, an approach the abstract calls "non-typical of their normal procurement practices" ([Verville & Halingten, 2002, *Management Decision*](https://doi.org/10.1108/00251740210420156), abstract) [independent: one case]. Their article proposing a six-stage model of the buying process for ERP software (*Industrial Marketing Management* 32(7), 2003; DOI 10.1016/S0019-8501(03)00007-5, as a library record gives it) was not opened at its publisher's page and carries nothing here. An empirical study comparing ERP selection in small or medium-sized and large organisations addressed the packages considered, the weights given to selection criteria, the size and structure of the decision team, and the methods and effort used ([Bernroider & Koch, 2001](https://doi.org/10.1108/14637150110392746), abstract) [independent]; the abstract gives none of the results, so none is reported here.

What this unit takes from the three, as its inference: the eight stages are a checklist of the work a selection contains, and a useful order for a sheet, but a real selection runs several at once and goes back. A buyer can reopen requirements after a demonstration, or drop a vendor after a reference call.

```viz
{"kind": "flow", "title": "The eight stages of a selection (course order)", "steps": [{"label": "Trigger", "note": "a need and a sponsor"}, {"label": "Long list", "note": "analyst lists, reviews, peers"}, {"label": "Request for information", "note": "non-binding"}, {"label": "Request for proposal", "note": "requirements, prices, plan"}, {"label": "Scripted demonstration", "note": "the buyer's scenarios"}, {"label": "References and site visits", "note": "customers the vendor names"}, {"label": "Proof of concept", "note": "where there is one"}, {"label": "Negotiation and contract", "note": "price, plan, partner, terms"}], "caption": "Section 1 of this unit: the course's eight stages, from the brief. The order is a convention: Grewal et al. (2015, p. 195) argue that buying processes run at the same time, Gartner's B2B buying journey page says the jobs follow no linear order, and Verville and Halingten (2002) found one ERP acquisition's processes iterative."}
```

## 2. The trigger

**What it is.** The **trigger** is the event that makes a company start a selection: a system reaching the end of its vendor's support, a new building, a merger, a failure the business can no longer absorb. It ends when someone senior agrees to sponsor the work and fund it. Info-Tech's steps put "Gain Business Authorization" before any request goes out (Info-Tech, RFP process page) [analyst]; Gartner's first buying job is problem identification (Gartner, B2B buying journey) [analyst].

**What decides it.** Whether a sponsor can get the money approved. Gartner's survey of 1,120 respondents in late 2021 found technology purchases funded at least partly outside IT in 74% of cases and shared funding delaying the budget for 75% of those sharing it (SCE11 §2, Gartner press release of 13 April 2022) [analyst]. No source opened measures what triggers warehouse-system replacements or how often each cause occurs: no independent source found.

**What it hides.** The trigger sets the question, and the question sets what every later stage compares. A company that starts from "our system's support ends" is choosing a replacement; one that starts from "web orders are promised from stock we cannot find" is choosing a fix to a seam between systems (SCE10), which a warehouse system alone may not hold (this unit's inference).

**The case.** At Corvane (fictional), a fashion retailer, the warehouse system is about twelve years old, runs on Corvane's own servers and is near the end of its vendor's support; web orders are promised from stock the distribution centre cannot find; and Corvane is deciding whether to replace the warehouse system and whether to buy order and transport systems from the same vendor [register]. Edda, vice-president supply chain, sponsors the replacement [register]. The second question widens the trigger: it brings the order system's owners into a warehouse decision (SCE11 §4).

## 3. The long list: analyst reports and peer reviews, as their publishers describe them

**What it is.** The **long list** is every product the buyer considers before asking any vendor for anything; the **shortlist** is the few it invites to propose or to demonstrate. The long list is built from what the buyer already knows, from colleagues at other companies, from analyst evaluations and from peer-review sites.

**How the analyst firms describe their use.** Gartner's page on using a Magic Quadrant (its graphic evaluation of a market's vendors, SCE1 §8) calls it "a first step to understanding the technology providers you might consider", and says "focussing on the leaders' quadrant is not always the best course of action", since it depends on how a provider aligns with your business goals ([Gartner, "How do I use a Gartner Magic Quadrant?", undated](https://gartner.co.uk/en/methodologies/magic-quadrants-research)) [analyst]. Its 2024 methodology note, read in abstract by SCE1, advises using an evaluation to narrow a list of providers and "don't base your decision on this evaluation only" (SCE1 §8) [analyst]. Forrester calls its Wave "a guide for buyers considering their purchasing options in a technology marketplace" ([Forrester, "The Forrester Wave Methodology", last modified 28 Apr 2026](https://www.forrester.com/marketing/policies/forrester-wave-methodology.html)) [analyst]. A vendor must buy reprint rights to post a Forrester Wave on its site, and the course's working assumption is the same for Gartner; a copy found on a vendor's site is one that vendor chose to post (SCE1 §8) [analyst].

**Who is absent by rule.** An evaluation covers only vendors that meet its inclusion criteria. Gartner's 2022 warehouse evaluation, the latest edition SCE6 could read, required sales and implementation resources in three or more regions and excluded vendors concentrated in one geography (SCE6 §2) [analyst]. A buyer whose long list was the 2022 Magic Quadrant's vendor list had left out every single-region vendor before looking at a product (this unit's inference from SCE6; the 2026 edition's criteria were not read). Common claim C10, that the vendor in the Leaders quadrant is the best choice, is not made by the analysts (SCE1 §11) and is tested in SCE17.

**How the review sites describe their use.** Gartner's Peer Insights invites buyers to "Choose solutions with confidence based on verified peer reviews and ratings" and says users go through a verification process ([Gartner Peer Insights, "About us", undated](https://www.gartner.com/peer-insights/about-us)) [analyst]. G2's scoring page says its Grid "helps buyers understand the competitive landscape for a category"; a product needs at least 10 reviews in a category to appear on a Grid report; vendors may ask their customers for reviews, but "vendors should not segment customers to solicit only positive reviews", and reviews gathered without an incentive weigh more in its scores ([G2, "Research Scoring Methodologies", updated 26 Oct 2026](https://documentation.g2.com/docs/research-scoring-methodologies)) [vendor-reported: a review site where vendors can invite reviewers, SCE1 §7]. Gartner's own review rules let vendors invite reviewers through a custom link (SCE1 §7) [analyst].

**What buyers report using.** Three surveys, each from a firm with an interest in the answer:

- Gartner Digital Markets, a business unit of Gartner that serves software providers as well as buyers ([Gartner Digital Markets, "About", undated](https://gcom.pdo.aws.gartner.com/en/digital-markets/about)), surveyed 3,500 "global software buyers" (roles, dates and company sizes not given on the page; Gartner owned the Capterra, Software Advice and GetApp review sites, and on 29 January 2026 G2 announced that it had agreed to acquire them ([G2, 29 Jan 2026](https://company.g2.com/news/g2-acquires-capterra-software-advice-getapp)) [vendor-reported]). In that survey, reviews were voted the most influential information source during shortlist research, 83% of buyers changed their initial list after research, and buyers actively engage with "only 2.5 vendors on average" ([Gartner Digital Markets, "2025 Software Buying Trends Report", undated](https://gcom.pdo.aws.gartner.com/en/digital-markets/insights/2025-software-buying-trends)) [analyst].
- Salminen, R. T. & Möller, K. (2006). Role of References in Business Marketing – Towards a Normative Theory of Referencing. *Journal of Business-to-Business Marketing* 13(1), 1–51, as the copy on the IMP Group's site gives it (its landing page lists Moller first) (abstract, on that page; the journal publisher's record was not opened). https://impgroup.org/2006/01/01/role-of-references-in-business-marketing-towards-a-normative-theory-of-referencing/
- TrustRadius, a review site, surveyed 1,862 technology buyers and 444 vendors worldwide in January 2026: 74% of buyers use reviews to inform purchase decisions, and 13% used analyst reports to make purchase decisions, which it gives as a 63% fall since 2022 ([TrustRadius, release of 15 Jul 2026](https://hginsights.com/news/trustradius-2026-b2b-buying-disconnect-report-reveals-ai-has-changed-how-buyers-research-but-not-what-they-trust/)) [vendor-reported: a review site's survey of its own subject]. Its headline finding concerns AI research tools, which this course does not treat.
- Gartner surveyed 646 business-to-business buyers in August and September 2025: 67% said they prefer a buying experience without a sales representative ([Gartner press release, 9 Mar 2026](https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience)) [analyst]. The release's other main figures are on AI use, which this course does not treat, and on decision confidence: confident buyers were twice as likely to report a high-quality deal.

None of the three is about execution software, and none separates large enterprise purchases from small ones. What they show, read together and as this unit's inference: a long list is formed largely before a vendor's salesperson is involved, from sources the buyer reads alone.

**What decides it.** What the committee already believes, and which sources it reads. **What it hides.** Every product the sources do not cover, and the difference between a product the analyst assessed and one that would suit this operation (SCE6 §2: most operations, in Gartner's 2022 model, do not need the most advanced functionality) [analyst].

## 4. The request for information and the request for proposal

**The two documents.** A **request for information (RFI)** asks vendors to describe themselves and their products, so the buyer can learn the market; it commits the buyer to nothing. A **request for proposal (RFP)** sets out the buyer's requirements and asks each vendor for a priced, written offer the buyer can compare and can hold the vendor to. Info-Tech advises an RFI when you lack in-depth knowledge of the market, the solutions or the viable vendors, and an RFP when you have defined requirements, approved funding and enough time (Info-Tech, RFP process page) [analyst].

**One RFI, read in full.** Washington State's Department of Enterprise Services published an RFI for an asset management software product on 7 February 2024. It states that "Release of this RFI in no way obligates the State of Washington", lists draft requirements for reference, asks how the product is hosted and how it authenticates users, asks for the product's roadmap "for enhancements, upgrades, and end of life/support", and invites selected responders to a 50-minute virtual demonstration ([Washington DES, "Request for Information (RFI) Survey: Asset Management Software Solution", 7 Feb 2024](https://des.wa.gov/sites/default/files/2024-02/FPS-asset-management-software-RFI.pdf)) [practice: one public buyer's document]. It asks for no prices.

**Three RFPs, read in full or nearly.** Each was published by a US public body and read in the copy its issuer posts:

- The Alabama Alcoholic Beverage Control Board's RFP for warehouse automation with software integration (17 July 2024) covers warehouse system requirements (cross-docking, perpetual cycle counting), automation, integration with the board's ERP, a cloud-based solution, training, support, a completion window of 14 months, itemised fixed prices, five reference projects, and a six-year purchase-to-own agreement; it scores proposals in five criteria of 20% each: design fit, meeting the specification, cost per year, ability to meet the timeline, and experience with similar projects ([Alabama ABC Board, "Request for Proposal: Warehouse Automation with Software Integration", 17 Jul 2024, §§3.2, 4, 5, 6.0, 7](https://alabcboard.gov/sites/default/files/2024-07/ABC%20RFP%20final%20July%2017%202024.pdf)) [practice: one public buyer].
- The Pinellas County Sheriff's Office's RFP 24-01 for an inventory management system (12 January 2024) asks for software, implementation, training, hosting and support; it weights functional requirements 40%, technology requirements 20%, implementation services 20%, vendor information 10%, and pricing with the total five-year cost 10% (§2.4.B); it may hold interviews (§2.4.A) and request a best and final offer (§1.14) ([Pinellas County Sheriff's Office, "Request for Proposal 24-01, Inventory Management System", 12 Jan 2024](https://pinellassheriff.gov/WebFormsEntry/UploadedFiles/567/RFP%2024-01.pdf)) [practice: one public buyer; the copy read was truncated after its response instructions, so the requirement rows were not read].
- The Mississippi Department of Education's technical requirements for food distribution software (Attachment A to RFP 4459, undated) run from functional requirements through data migration, implementation work, acceptance, security, and maintenance and support with an availability target of 99.98%; vendors answer each point "WILL COMPLY" or "EXCEPTION" ([Mississippi Department of Education, "Attachment A to RFP No. 4459: MDE Food Distribution Software Technical Requirements"](https://rfps.its.ms.gov/Procurement/rfps/4459/4459attachmenta.pdf)) [practice: one public buyer].

Pinellas's weights, drawn:

```viz
{"kind": "compare", "title": "One buyer's evaluation weights (Pinellas County Sheriff's Office, RFP 24-01, 2024)", "unit": "%", "max": 100, "rows": [{"label": "Functional requirements", "value": 40}, {"label": "Technology requirements", "value": 20}, {"label": "Implementation services", "value": 20}, {"label": "Vendor information", "value": 10}, {"label": "Pricing and total five-year cost", "value": 10}], "caption": "Section 4 of this unit: the weights in section 2.4.B of the Pinellas County Sheriff's Office's RFP 24-01 for an inventory management system, 12 January 2024. One US public buyer's weights, evidence of nothing about other buyers."}
```

**What decides the RFP stage.** The written answers, scored against weights the buyer set before reading them. The UK government's bid evaluation guidance says "Bids should be independently scored by at least two evaluators", that finance models should be evaluated independently of the technical specification, that a moderator who did not score should lead the panel to one agreed score, which "should not simply be an average", and that "Clarification is not an opportunity for bidders to improve their bids"; on price against quality, "It is not about the lowest upfront price", and an 80/20 quality-to-price split signals that quality matters most (§§3.3.2, 3.3.4, 5.1, 9.2.1, 9.3.2) ([UK government, "Bid Evaluation guidance note", May 2021](https://assets.publishing.service.gov.uk/media/60a387e48fa8f56a3e32fa9a/Bid_evaluation_guidance_note_May_2021.pdf); the page does not name its issuing department) [practice: public-sector guidance, UK]. In the two RFPs with weights, price carries 10% (Pinellas) and 20% (Alabama) of the score (above) [practice].

**Who sits on the panel.** Two public bodies describe it. The Virginia Information Technologies Agency (VITA) names the business owner, the procurement lead and contract risk management as the key roles of an IT procurement's project and evaluation teams, and recommends that "these four corners of expertise" (business, technical, legal and financial) be represented on the evaluation team; outside experts "may provide information to the ET but cannot score"; the procurement lead "Leads the negotiation process", and the business owner "Identifies negotiation objectives and participates in negotiations" ([VITA, "24.3.1 Putting together the procurement project team (PPT) and evaluation team (ET)", undated](https://www.vita.virginia.gov/procurement/buy-it-manual/chapter-24---requests-for-proposals-and-competitive-negotiations/2431-putting-together-the-procurement-project-team-ppt-and-evaluation-team-et.html)) [practice: US state guidance]. New Zealand Government Procurement says "The panel should be 3–5 people", may include technical, cultural, financial or legal expertise, and that each member declares conflicts of interest; experts can advise without being panel members ([New Zealand Government Procurement, "Setting up the evaluation panel", published 5 Oct 2017, modified 9 Feb 2021](https://procurement.govt.nz/procurement/guide-to-procurement/plan-your-procurement/setting-up-the-evaluation-panel)) [practice: NZ government guidance]. Neither page mentions end users. Set against SCE11's seven roles, VITA names business, technical, financial and procurement members, as SCE11 §3 does, and New Zealand names technical and financial expertise; both add **legal**, which SCE11 has no card for; neither names a site manager or an outside integrator (this unit's comparison; how far public-sector practice describes a retailer's committee is this unit's inference).

**What the RFP stage hides.** How the product behaves. A written answer is the vendor's claim, graded vendor-reported however it is scored (SCE1 §10). A weight table rewards what it weights: in Pinellas's, 90% of the score goes to written answers and plans (functional 40, technology 20, implementation 20, vendor 10) and 10% to price, and none of the five lines is the demonstration (this unit's reading of §2.4.B).

## 5. What a requirements list contains, and what kind of product it rewards

A **requirements list** (requirements matrix, capability matrix) is the table at the centre of an RFP: one row per thing the buyer needs, one column for the vendor's answer. The lists opened share a form.

**What the rows contain.** The Alabama RFP's warehouse rows are capabilities named by operation, such as cross-docking and perpetual cycle counting, beside rows for integration, hosting, training and support (§3.2) [practice]. The Mississippi list runs from functional rows to data migration, an implementation plan, a user acceptance testing plan, security, support levels and service credits (Sections II to IX) [practice]. A city's ERP requirements matrix published by Birmingham, Alabama groups its rows by function (finance, grants, procurement and supply chain with an inventory subsection of 11 rows, human resources, payroll, projects, e-government services, reporting, general system) ([City of Birmingham, "RFP Section 4: Requirements Matrix", 2024](https://birminghamal.gov/wp-content/uploads/2024/08/RFP-Section-4.pdf)) [practice: one public buyer; the page shows no title, date or issuer beyond the address, and the copy read was truncated]. ARC Advisory Group's warehouse selection guide lists criteria under business goals, product functions and features, and service requirements for the project and the lifecycle, and names total cost of ownership, integration, usability, implementation support and training and the supplier's long-term viability among the issues ([ARC Advisory Group, "Warehouse Management System Selection", undated](https://www.arcweb.com/technology-evaluation-and-selection/warehouse-management-systems)) [analyst]; its second page of the same title adds sections of supplier analysis and supplier profiles, names no supplier in the text read, and invites readers to engage ARC ([ARC, second address](https://www.arcweb.com/technology-evaluation-and-selection/warehouse-management-system-selection)) [analyst].

**How the answers are coded.** The Birmingham matrix asks each vendor to mark every row "S = Standard", "F = Available with Configuration", "C = Available with Customization", "P = Available through a 3rd-party" or "N = Not Available" [practice]. Pinellas asks for one of four options per row, a blank or a double mark read as "No" (Attachment B) [practice]. Mississippi asks only "WILL COMPLY" or "EXCEPTION" [practice].

**What kind of product it rewards**, as this unit's inference from those forms:

- **Breadth claimed in the vendor's own words.** A list scored row by row rewards the product that can answer yes to the most rows. A yes costs the vendor a mark on a form; whether the capability works at the buyer's volume is not on the form (SCE6 §9: a vendor's page cannot show it either).
- **The product built for the buyer's vocabulary.** Rows are written in the buyer's words, and SCE6 §1 shows that a textbook and an analyst draw different boundaries round "warehouse management system". Forrester's abstract on warehouse-system functions says vendors' marketing messages and a lack of standardisation amplify the difficulty of telling which product solves a business problem (SCE11 §6) [analyst].
- **Configuration over customisation, where the codes separate them.** A list that asks for S, F, C, P or N lets the buyer see which rows need code changes, which SCE6 §4 shows carry cost into every later upgrade [independent, for the ERP studies there]. A list that asks only "will comply" does not.
- **The integrated product, where integration has its own row.** In one survey of Turkish manufacturing companies (sample size not given in the abstract), fit with the parent or allied organisation's systems was "the most important selection criterion", followed by cross-module integration, compatibility with other systems and vendor references ([Baki & Çakar, 2005](https://doi.org/10.1108/14637150510578746), abstract) [independent; ERP, one country].

**What it cannot show.** How the operation's peak, exceptions and people would use it (SCE5, SCE15). A list counts capabilities; it does not weigh how often each is used or by whom (this unit's inference).

## 6. The scripted demonstration: what it shows and what it cannot

**What it is.** In a **scripted demonstration** the buyer writes the scenarios and the vendor shows its product working through them, in place of the vendor's own standard presentation. Info-Tech's ERP demonstration template says it gives vendors "scenarios that prompt them to display how the tool will support" the buyer's particular needs ([Info-Tech, "ERP Vendor Demonstration Script Template", published 10 Apr 2023, modified 15 Oct 2026](https://www.infotech.com/research/erp-vendor-demonstration-script-template), public page; the template itself is paid) [analyst]. An older Info-Tech note warns that many businesses neglect the planning demonstrations need, which "can be a very valuable input to the final selection process" when done properly, and lists the steps: choose which vendors to invite, set the length and the requirements to cover (use cases, scripts, bake-offs, that is, vendors run through the same scenarios one after another), prepare a "well-defined, time-boxed demo agenda", prepare the stakeholders, and build a scoring strategy and debriefs ([Info-Tech, "Master the Enterprise Application Vendor Demo", A. Hay, published 18 Dec 2007, modified 3 Apr 2012](https://www.infotech.com/research/master-the-enterprise-application-vendor-demo)) [analyst; the page is nearly twenty years old].

**How the public documents place it.** Washington's RFI invited selected responders to a 50-minute virtual demonstration (section 4) [practice]. Pinellas's shortlisted vendors may give a "virtual evaluation committee presentation" and "should be prepared to demonstrate all aspects of their service" (§1.13) [practice]. The UK guidance asks departments to "carefully consider the use of bidder presentations, interviews, scenario tests or site visits" and to set out in the procurement documents how each will be evaluated (§6.3.7) [practice]. In neither RFP with weights is the demonstration a weighted line of its own (section 4).

**What a scripted demonstration shows**, as this unit's inference from those sources: that the product can do the scenario, on screen, with the vendor's people at the keyboard; how many steps and screens the scenario takes; how the vendor answers questions it did not prepare for, if the script leaves room for them.

**What it cannot show**, as this unit's inference from the units named:

- **Volume and peak.** A demonstration runs a handful of orders on a prepared system. Corvane's (fictional) web volume in peak is about four times a normal week [register]; nothing on the screen shows the system at that load.
- **The configuration behind the screen.** The vendor configured the demonstration system. How much configuration or customisation the buyer's own operation would need is the question SCE6 §4 raises, and the demonstration does not answer it.
- **The seams.** A scenario that stays inside the product cannot show a cancellation reaching released work in another system, or which system holds the stock figure (SCE10 §§2, 7).
- **The shift.** The people who will use the system every shift may not be in the room; nothing opened says how often they are (SCE11 §5). A scenario watched on a projector is not a picker's shift on a handheld (SCE5 §3). In Howcroft and Light's case of one small consultancy choosing a customer relationship management package, salesmanship directed by the vendor or consultant at senior management's interests "marginalises user needs and ultimately secures the procurement of the software package" ([Howcroft & Light, 2008](https://doi.org/10.1108/17410390810911203), abstract) [independent: one case, not in a warehouse].

**Common claim C13: "Buyers decide on the demonstration."** In this unit's reading (no source opened states it in this form), the claim is that the demonstration, more than the written proposal or the references, is where the deal is won. What the sources opened show:

- TrustRadius's 2026 survey (above) names product demonstrations and free trials, with user reviews and prior experience, among the most influential resources, and gives no percentage for demonstrations [vendor-reported].
- Gartner Digital Markets reports that 62% of the 3,500 software buyers it surveyed say a product trial is their top factor in the final decision (section 3) [analyst]. A trial is the buyer using the product, which is not the vendor demonstrating it, and the sample's company sizes are not given.
- Gartner's buying-journey page says buyers spend only 17% of their buying time meeting potential suppliers, and only 5% or 6% with any one supplier's representative when comparing several (Gartner, B2B buying journey) [analyst: no sample stated]. Every demonstration sits inside that share.
- In the one conjoint study of IT managers' criteria seen (Keil and Tiwana, 2006, as Olson et al. report it), reliability and functionality had the largest effects and ease of use a smaller one (SCE11 §2) [practice, origin not traced]. In Baki and Çakar's survey, the top criteria were fit with existing systems, integration and vendor references (section 5) [independent]. Neither study measured demonstrations.
- In the two public RFPs with weights, the demonstration carries no weight of its own (section 4) [practice].

**What the evidence shows.** No source opened measures how much a demonstration decides a selection of execution software, or of enterprise software in general. The surveys that name demonstrations or trials rank them among several influences, give no number for demonstrations, and come from a review site and from a Gartner business that served software providers and whose parent then owned review sites (section 3). **No independent source found** for the claim.

## 7. Reference calls and site visits, and why references weigh

**What they are.** A **reference customer** is a customer a vendor names to speak to a buyer (SCE11 glossary). A **reference call** is the buyer's conversation with one; a **site visit** (reference visit) is the buyer's committee going to see the product running at a reference customer's operation.

**What the public documents ask for.** Alabama asks for five reference projects of similar services, each with a contact and a summary of the software and system configuration (§4) [practice]. Pinellas asks for at least five clients equal or greater in size and complexity, each with the project's scope, dates, contract length and unanticipated delays (Section C.5) [practice]. The UK guidance lists site visits among the activities a department must set out in advance if it evaluates them (§6.3.7) [practice].

**Why references weigh.** In Baki and Çakar's survey, vendor references ranked fourth among the ERP selection criteria (section 5) [independent; one country; sample not given in the abstract]. A study of suppliers, based on 38 interviews with managers at four process and information technology companies, found that suppliers use references to gain status from reputable customers, to signal they passed a customer's selection, to "concretize and demonstrate complex solutions" and to "provide indirect evidence of their experience" ([Jalkala & Salminen, "The Practices and Functions of Customer Reference Marketing – Leveraging Customer References as Marketing Assets", IMP Group conference, Marseille, 2009](https://impgroup.org/?p=4961), abstract) [practice: a conference paper whose peer review the page does not state; supplier-side interviews, not buyers]. An earlier paper by Salminen and Möller (the IMP Group's page lists Moller first; the copy it hosts gives Salminen first) notes that "there is very little reported academic research on references" ([Salminen & Möller, "Role of References in Business Marketing – Towards a Normative Theory of Referencing", *Journal of Business-to-Business Marketing* 13(1), 2006](https://impgroup.org/2006/01/01/role-of-references-in-business-marketing-towards-a-normative-theory-of-referencing/), abstract on the IMP Group's page) [practice: abstract only, on the IMP Group's page; the journal's record was not opened, so the paper's peer-reviewed form is not confirmed].

**What they hide.** The vendor chooses the references. Forrester's own method shows the pattern at the analyst level: "Forrester interviews or surveys the reference customers provided by the vendor" (Forrester, Wave methodology) [analyst]. A reference is therefore evidence of a customer the vendor was willing to put forward (SCE1 §9; this unit's inference). It does not show the customers the vendor left out, and a reference running a different flow (pallets, not single items; one country, not four) says little about the buyer's own (SCE1 §9: what would transfer). A site visit shows a running operation, at the reference's volume and with the reference's configuration, which is more than a demonstration shows and still not the buyer's operation (this unit's inference).

## 8. A proof of concept, where there is one

**What it is.** A **proof of concept** (pilot) is a test of the product on the buyer's own data or processes before the contract, run by the vendor, the buyer or both. VITA's page on the procurement and evaluation teams mentions "evaluation-phase tests/pilot programs", in which subject matter experts may assist the business owner (VITA 24.3.1) [practice]. None of the three RFPs read asks for one; Alabama makes the delivered system subject to any test the board may determine, which this unit reads as acceptance of what is delivered after award; the clause does not state its timing (§7.1) [practice].

**What it shows and hides**, as this unit's inference: it shows the product on the buyer's items, locations or orders, which no earlier stage does. It is usually narrow (one process, one flow, a sample of data), it costs both sides time, and who pays for it is a commercial question with no public figure. Gartner Digital Markets' 62% figure on trials (section 3) [analyst] suggests buyers value using the product themselves; it is not a measurement of proofs of concept in execution software.

## 9. Negotiation and contract: the plan and the partner are part of what is bought

**What is negotiated.** Price, and much else. The public documents show what else is put in writing before signature (each [practice: one public buyer]):

- **Price form.** Alabama asks for itemised fixed prices and a firm fixed cost (§4.5, §5.12); Pinellas asks for a fixed price broken out by component, each marked one-time or annual, will not consider time-and-materials pricing, ties payments to milestones from kick-off to final acceptance, asks that software maintenance not increase during the first five years of live operation, and sets an initial term of five years (§1.15; Section B, 2.2.O to 2.2.R).
- **A best and final offer.** Pinellas may request one from the shortlisted vendors (§1.14).
- **The implementation plan.** Mississippi asks for a preliminary project management plan, a system design document, a data migration plan and a user acceptance testing plan with the proposal, and a train-the-trainer programme for three to five administrators (Sections IV, V, IX). Alabama sets a 14-month completion window (§5) and asks for profiles of the supplier's key personnel (§4). Pinellas weights implementation services at 20% of the score, as much as the technology (§2.4.B).
- **Who negotiates.** In VITA's account, the procurement lead leads and the business owner sets the objectives and takes part (section 4) [practice].

**Why the plan and the partner are bought too.** A warehouse system arrives configured, integrated and loaded with the operation's data, or it does not run. Who does that work is part of the offer: Halvern Systems (fictional) implements through its own services team and through partners [register], and SCE11 §3.6 describes the **integrator**, the outside firm that implements alongside or instead of the vendor. ARC's guide puts implementation support and training, and service requirements for the project and the lifecycle, among the criteria (section 5) [analyst]. As this unit's inference: when the buyer signs, it buys a product, a plan, a team named in that plan and a price for the plan's work. SCE14 takes the plan into implementation.

**What negotiation hides.** The terms of other customers' contracts, and any price a private vendor has not published: no public figure. Which contract terms protect the buyer, and whether they are enforceable where the buyer operates, are questions for its legal counsel.

**The case.** At Corvane (fictional), Helene, chief financial officer, can veto on cost, and a procurement function, unnamed, runs the request and the contract (SCE11 cards 3 and 5, working). The register gives Corvane's peak as mid-November to early January [register]; when a go-live could fall is a question for the plan, not settled here.

## 10. Why deals are won or lost: what the public evidence is

The evidence is thin, and most of it is told by vendors or by firms that sell to them.

- **Win rates and loss reasons of real vendors** are not public. No source opened gives a win rate for any vendor of execution software, and the course states none for a private company (course rule). The "win/loss" reports this unit's searches returned were published by firms that sell win/loss interviews or sales software (working description of the search results); none was opened, and under the course's key they would be vendor-reported.
- **Regret.** Gartner's survey of 1,120 respondents at manager level or above, involved in evaluating or selecting technology, in North America, Western Europe and Asia/Pacific, fielded in November and December 2021, found 56% reporting a high degree of regret over their largest technology purchase of the past two years, regret highest among those who had not yet started implementation, and high-regret purchases taking 7 to 10 months longer on average to complete; 67% of the people involved in technology buying were outside IT ([Gartner press release, 12 Jul 2022](https://www.gartner.com/en/newsroom/press-releases/2022-07-12-gartner-finds-that-majority-of-technology-purchases-come-with-high-degree-of-regret)) [analyst]. Gartner Digital Markets reports 59% of its 3,500 software buyers regretting at least one purchase in the past 18 months (section 3) [analyst].
- **Conflict in the committee.** Gartner's survey of 632 business-to-business buyers, fielded in August and September 2024, found 74% of buyer teams showing "unhealthy conflict" during the decision, and buying groups that reached consensus 2.5 times more likely to report a high-quality deal ([Gartner press release, 7 May 2025](https://www.gartner.com/en/newsroom/press-releases/2025-05-07-gartner-sales-survey-finds-74-percent-of-b2b-buyer-teams-demonstrate-unhealthy-conflict-during-the-decision-process)) [analyst]. That is a correlation in buyers' own reports, not a cause.
- **Selection as a social process.** Howcroft and Light's longitudinal study of one small organisation argues against reading selection as a rational search for the "best technology solution" and shows how various actors shape it ([Howcroft & Light, 2010](https://doi.org/10.17705/1jais.00224), abstract) [independent: one case].

**What follows, as this unit's inference.** A deal can be lost to another vendor, to no decision at all, or to a committee that cannot agree; the public sources measure the last two only in buyers' general reports, not in execution software. Anyone who tells you why a particular deal was lost is giving an account, and the account is the seller's unless it came from the buyer.

## 11. What a product team can change at each stage, and what it cannot

A **product team** here is the people who decide what the product does: product managers, designers and engineers. Every line below is this unit's inference from the sections named; no source opened tests it.

| Stage | What the product team can change | What it cannot |
|---|---|---|
| Trigger | Whether the product addresses the problem the trigger names (section 2) | The trigger itself, or the sponsor's budget |
| Long list | What the public pages and documentation say the product does, which analysts and reviewers read (SCE6 §9) | Analysts' inclusion rules (section 3); which reviewers a vendor invites |
| RFI and RFP | How many requirement rows the product meets as standard or by configuration, not customisation (section 5; SCE6 §4) | The rows the buyer writes, their weights, and how the vendor's team answers them |
| Scripted demonstration | How many steps a scenario takes; whether exceptions and seams can be shown working (section 6) | The script, who is in the room, and the vendor's demonstration configuration |
| References and site visits | Whether existing customers run the product well enough to speak for it, which depends on what was built for them | Which customers the vendor names (section 7) |
| Proof of concept | How quickly the product takes the buyer's data and configuration (section 8) | Whether one is run, and its scope |
| Negotiation and contract | What the implementation plan has to contain: the configuration, integrations and data the product needs (section 9; SCE6 §11) | Price, terms, the partner chosen and the contract's legal form |

## On a site visit

This unit is not about an operation. Its questions are for your own colleagues in sales and in services, about selections they took part in, because the answers are not public (sections 7 and 10).

- **Which stage did we lose most deals at last year, and how do we know?** Ask whether the reason came from the buyer or from our own team (section 10).
- **Where did our recent long lists come from?** An analyst report (which, in what form), a review site, a consultant, a former customer (section 3).
- **Who wrote the requirements lists we answered, and what share of rows did we answer as standard, configuration, customisation or partner?** (Section 5.)
- **Who wrote the script for our last scripted demonstration, who was in the room, and was anyone from the floor there?** (Section 6; SCE11 §5.)
- **Which scenarios do we decline or steer away from in a demonstration, and why?** (Section 6.)
- **Who chooses our reference customers, how often is each asked, and which customers do we not offer?** (Section 7.)
- **How often is a proof of concept asked for, who pays, and what was its scope?** (Section 8.)
- **Who writes the implementation plan in a proposal, who is named in it, and how often does the plan change after signature?** Ask services, then SCE14 (section 9).
- **When we lose to no decision, what does the buyer say happened?** (Section 10.)

## Self-check

1. **Name the eight stages this course uses, and say why their order is a convention.**
   Trigger, long list, RFI, RFP, scripted demonstration, references and site visits, proof of concept, negotiation and contract. Grewal et al. (2015) argue buying processes run at the same time, Gartner says the buying jobs follow no linear order, and Verville and Halingten found one ERP acquisition's processes iterative (section 1).
2. **How do Gartner and Forrester describe the use of their evaluations?**
   Gartner: a Magic Quadrant is a first step to understanding the providers you might consider, the Leaders quadrant is not always the best course, and the 2024 note says not to decide on the evaluation alone. Forrester: a guide for buyers considering their options. A Forrester Wave on a vendor's site is one the vendor bought reprint rights to post; for Gartner that is the course's working assumption (section 3).
3. **What is the difference between an RFI and an RFP?**
   An RFI asks vendors to describe themselves and binds the buyer to nothing (Washington's RFI says so); an RFP sets out requirements and asks for priced offers the buyer can compare. Info-Tech advises an RFP once requirements, funding and time are in place (section 4).
4. **What do the response codes of a requirements matrix tell you, and what kind of product does a row-by-row list reward?**
   Codes such as Birmingham's (standard, configuration, customisation, third party, not available) show which rows need code changes; a list scored row by row rewards the product that can answer yes to most rows, which is not evidence of how it runs (section 5, inference).
5. **What can a scripted demonstration not show?**
   Volume and peak, the configuration behind the screen, the seams with other systems, and a user's whole shift; in one case, salesmanship marginalised user needs (section 6).
6. **What does the evidence say about C13, "buyers decide on the demonstration"?**
   A review site's and an analyst's surveys rank demonstrations or trials among several influences, with no number for demonstrations; Gartner says buyers spend 17% of their buying time with suppliers; no source measures the demonstration's weight. No independent source found (section 6).
7. **Why do references weigh, and what do they hide?**
   Buyers ranked vendor references among the top ERP criteria in one Turkish survey; suppliers use them as indirect evidence of experience. The vendor chooses them, as Forrester's own reference customers are provided by the vendor (section 7).
8. **What, besides the product, does a buyer sign for?**
   A plan, a named team and a price for the plan's work: the public RFPs ask for implementation plans, data migration and testing plans, key personnel, milestones and a completion window, and one weights implementation as heavily as technology (section 9).

## Deliverable

### A. The stage sheet form

One block per stage, in the order of section 1. Every line ends with its source in brackets: a section of this unit or another with its grade, "register" for a case fact, or "working" for a working description. The field names are the brief's.

| # | Field | What goes in it |
|---|---|---|
| 1 | Stage | The stage's name and its number (S1 to S8) |
| 2 | Who is in it | The committee roles (SCE11 §3) and others who take part, by name where the case gives one |
| 3 | What decides it | What moves a product to the next stage or out |
| 4 | What it hides | What the people deciding cannot see at this stage |
| 5 | What a product team can affect | From section 11 |
| 6 | What to ask internally | The question for your own sales, services or product colleagues |

### B. Corvane (fictional) replacing its warehouse system

Corvane (fictional) is a fashion retailer with 60 stores in four European countries and one website, one distribution centre of 28,000 m², about 140 staff in a normal week and about 260 in peak, and a warehouse system about twelve years old on its own servers, near the end of its vendor's support; it is deciding whether to replace the warehouse system and whether to buy order and transport systems from the same vendor [register]. The committee is SCE11's: Edda (operations executive and sponsor), Ravi (IT director), Helene (chief financial officer), Marek (site manager), an unnamed procurement function and an unnamed integrator (SCE11 deliverable B, working). The vendors named are the case register's, all fictional; which ones reach each stage is this sheet's assumption (notes).

```viz
{"kind": "matrix", "title": "Who takes part in each stage at Corvane (fictional; working)", "cols": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"], "rows": [{"label": "Edda (sponsor)", "tone": 1, "cells": ["sponsors", "in", "in", "scores", "in", "visits", null, "sets aims"]}, {"label": "Ravi (IT)", "tone": 2, "cells": ["in", "in", "in", "scores", "in", "calls", "if run", null]}, {"label": "Helene (finance)", "tone": 3, "cells": [null, null, null, "scores", null, null, null, "veto"]}, {"label": "Marek (site)", "tone": 5, "cells": [null, null, null, "scores", "in", "visits", null, null]}, {"label": "Procurement", "tone": 4, "cells": [null, null, "sends", "runs", null, null, null, "leads"]}, {"label": "Legal counsel", "tone": 6, "cells": [null, null, null, "consulted", null, null, null, "terms"]}, {"label": "Integrator", "tone": 6, "cells": [null, null, null, null, null, null, null, "named in plan"]}], "caption": "Deliverable B of this unit: the 'Who is in it' line of each stage block, S1 trigger to S8 negotiation and contract, as a grid. Every cell is a working description from those blocks, built on SCE11's cards (deliverable B there) and on VITA's account of evaluation teams (section 4). The figure adds no fact."}
```

**S1 · Trigger**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S1, trigger |
| 2 | Who is in it | Edda, who sponsors the replacement [register]; Ravi, whose servers run the old system [register; SCE11 card 2, working] |
| 3 | What decides it | Whether Edda gets the replacement funded; whether the order and transport question is in scope from the start [register for the question; section 2, working] |
| 4 | What it hides | Whether the known trouble (web orders promised from stock the centre cannot find) sits in the warehouse system or in the seam to the order system [register; SCE10, working] |
| 5 | What a product team can affect | Whether the product addresses the trouble the trigger names (section 11, working) |
| 6 | What to ask internally | Which triggers bring us into selections, and at what stage we usually hear of them (section 2, working) |

**S2 · Long list**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S2, long list |
| 2 | Who is in it | Edda and Ravi; possibly an outside selection consultant, none named (SCE11 §3.6, working) |
| 3 | What decides it | What the committee already knows, what peers say, analyst evaluations used as a first step (section 3) [analyst], and review sites (section 3) [vendor-reported for review content] |
| 4 | What it hides | Vendors outside an evaluation's inclusion rules, such as single-region vendors (SCE6 §2) [analyst]; whether a product fits a single-site retailer's flows (section 3, inference) |
| 5 | What a product team can affect | What public pages and documentation claim, which is what analysts and buyers read (SCE6 §9; section 11, working) |
| 6 | What to ask internally | Where our long lists come from, and in what form the buyer read any analyst report (section 3) |

On the list, as this sheet's assumption: Halvern Systems (fictional), which sells order, warehouse and transport software and says of itself "One vendor for execution", because Corvane asks whether to buy all three from one vendor; Kestrow (fictional), which sells one warehouse system to single-site customers and says "Live in weeks" [register for the vendors and their statements, which are vendor-reported claims of fictional companies and evidence of nothing].

**S3 · Request for information**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S3, request for information |
| 2 | Who is in it | Corvane's procurement function sends it (SCE11 card 5, working); Ravi and Edda write the questions (working) |
| 3 | What decides it | Written answers on hosting, roadmap, support end-of-life and fit, as in Washington's RFI (section 4) [practice]; who answers at all |
| 4 | What it hides | Prices (the one RFI read asked none) [practice]; how the product runs |
| 5 | What a product team can affect | Whether the roadmap and the support life of each version can be stated plainly; Ravi's move from own servers to a cloud service (SCE6 §3) is the question it raises (working) |
| 6 | What to ask internally | Who answers RFIs here, and from what source of truth about the product (working) |

**S4 · Request for proposal**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S4, request for proposal and the requirements list |
| 2 | Who is in it | Procurement runs it; Edda, Ravi, Helene and Marek score their parts; legal is consulted on terms, a role the register does not name and SCE11 mentions (card 5) without a card (section 4: VITA's four corners [practice]; working) |
| 3 | What decides it | Scores against weights set before reading, with price one weighted line (section 4) [practice]; in the codes asked, the share of rows met as standard or by configuration (section 5) [practice] |
| 4 | What it hides | Whether the product behaves as answered; how often each row matters on Corvane's floor; the peak of about four times a normal week's web volume [register; section 5, inference] |
| 5 | What a product team can affect | How many rows the product meets without customisation, so the answer can be S or F, not C (section 5; SCE6 §4) |
| 6 | What to ask internally | What share of the last few requirement lists we answered S, F, C, P or N, and which rows we lose on (section 5) |

**S5 · Scripted demonstration**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S5, scripted demonstration |
| 2 | Who is in it | Edda, Ravi, Marek; whether Mina (picker), Tobias (outbound supervisor) or Carla (inventory controller) attend is not in the register (SCE11 §5; working) |
| 3 | What decides it | How the product runs the committee's scenarios: from SCE11's cards, a web order promised from stock the centre cannot find, a store shipping a web order, a short pick on the handheld, a cancellation reaching released work (SCE11 cards 1, 2, 4, working) |
| 4 | What it hides | Volume and peak; the vendor's configuration of the demonstration system; the seams with the order system and carriers' portals; a picker's whole shift (section 6, inference) |
| 5 | What a product team can affect | How many steps each scenario takes; whether exceptions and seams can be shown working (section 11, working) |
| 6 | What to ask internally | Who writes the script, who attends from the buyer, and which scenarios we steer away from (section 6) |

**S6 · Reference calls and site visits**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S6, references and site visits |
| 2 | Who is in it | Marek and Edda visit; Ravi calls on interfaces and support (SCE11 cards 1, 2 and 4, working) |
| 3 | What decides it | Whether a customer like Corvane (a retailer serving stores and a website from one centre, with a peak) runs the product well (section 7, inference) |
| 4 | What it hides | The customers the vendor did not name; how far the reference's flows, countries and volume match Corvane's (section 7) [analyst for Forrester's vendor-provided references; inference] |
| 5 | What a product team can affect | Whether existing customers run the product well enough to speak for it (section 11, working) |
| 6 | What to ask internally | Who chooses our references, and which retail customers with store and web flows we could offer (section 7) |

**S7 · Proof of concept, if Corvane runs one**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S7, proof of concept; whether Corvane runs one is not in the register (working) |
| 2 | Who is in it | Ravi's team and Carla's stock records, if run (working) |
| 3 | What decides it | Whether the product takes Corvane's item and location data and runs one flow on it (section 8, inference) |
| 4 | What it hides | Everything outside the flow tested; who pays for it, with no public figure (section 8) |
| 5 | What a product team can affect | How quickly the product takes a buyer's data and configuration (section 11, working) |
| 6 | What to ask internally | How often a proof of concept is asked for, who pays, and what its scope was (section 8) |

**S8 · Negotiation and contract**

| # | Field | Content |
|---|---|---|
| 1 | Stage | S8, negotiation and contract, with the implementation plan and the partner |
| 2 | Who is in it | Procurement leads; Edda sets the objectives; Helene can veto on cost; the integrator, if one, is named in the plan; Corvane's legal counsel on terms (section 9; SCE11 cards 3, 5, 6; working) |
| 3 | What decides it | The price form (fixed or not, one-time and annual), milestones, the plan's team and window, any maintenance price cap, a best and final offer, as in the public RFPs (section 9) [practice]; whether order and transport are in the same contract [register for the question] |
| 4 | What it hides | Other customers' terms; any private vendor's prices (no public figure); whether the plan will hold through Corvane's peak of mid-November to early January [register; section 9] |
| 5 | What a product team can affect | What the plan must contain because the product needs it: the configuration, the ERP and order-system integrations, the item and location data (section 11; SCE6 §11, working) |
| 6 | What to ask internally | Who writes the plan in our proposals, who is named in it, how often it changes after signature, and when a legal question goes to counsel (section 9) |

Who has no stage in this sheet where they score or decide (working): Mina, Tobias and Carla, who will use the system every shift, and whose attendance at the demonstration is open (S5; SCE11 §5: in the studies opened, the users' place varies); Freya, who ships web orders from a store, and Jonas, who answers customers [register for the roles; working].

### C. Template: the stage sheet

Copy one block per stage, S1 to S8. Every line ends with its source in brackets.

| # | Field | Fill in |
|---|---|---|
| 1 | Stage | ______ (S1 trigger, S2 long list, S3 request for information, S4 request for proposal, S5 scripted demonstration, S6 references and site visits, S7 proof of concept, S8 negotiation and contract; say "not run" where a stage was skipped) |
| 2 | Who is in it | ______ (each person by first name or role label and committee role from SCE11 §3; who leads; who is consulted and does not score; the users who are absent) |
| 3 | What decides it | ______ (the documents, scores, weights or events that move a product on or out; the source of each: the buyer's document, a colleague who was there, or working) |
| 4 | What it hides | ______ (what the people deciding cannot see at this stage: volume, configuration, seams, the shift, the customers not named, prices not published) |
| 5 | What a product team can affect | ______ (the product decisions that change how this stage goes; mark working unless a selection record shows it) |
| 6 | What to ask internally | ______ (one or two questions for your sales, services or product colleagues; record who answered and when) |

Below the sheet: the trigger in one sentence (______), the vendors on the long list as the buyer named them (______, or "not known"), and where the money comes from (______: one budget or several, SCE11 §2).

### D. Glossary lines

| Term | Definition | Source |
|---|---|---|
| Selection | The work from deciding new software may be needed to signing for one product | Working |
| Trigger | The event that starts a selection | Working; Gartner's "problem identification" [analyst] |
| Long list; shortlist | Every product considered; the few invited to propose or demonstrate | Working |
| Request for information (RFI) | A non-binding request for vendors to describe themselves and their products | Washington DES RFI, 2024 [practice]; Info-Tech [analyst] |
| Request for proposal (RFP) | A request for written, priced offers against stated requirements | Info-Tech [analyst]; definition working |
| Requirements list (requirements matrix, capability matrix) | The table of the buyer's needs, one row each, with a column for the vendor's answer | Birmingham, Pinellas [practice]; definition working |
| Response code | The mark a vendor gives each row: standard, configuration, customisation, third party, not available | Birmingham, 2024 [practice] |
| Evaluation panel (evaluation team) | The people who score the proposals | VITA; NZ Government Procurement [practice] |
| Moderation | Agreeing one score per question across evaluators, led by someone who did not score | UK Bid Evaluation guidance note, 2021 [practice] |
| Best and final offer | A last revised offer requested from shortlisted vendors | Pinellas RFP 24-01 [practice]; definition working |
| Scripted demonstration | A demonstration in which the buyer writes the scenarios | Info-Tech [analyst]; definition working |
| Bake-off | Vendors running the same scenarios one after another | Info-Tech, 2007 [analyst]; definition working |
| Reference call; site visit | A buyer's conversation with a reference customer; a visit to see the product running there | Working; Forrester (reference customers) [analyst] |
| Proof of concept (pilot) | A test of the product on the buyer's data or processes before the contract | VITA (pilot programmes) [practice]; definition working |
| Milestone payment | A payment due when a stated stage of the project is reached | Pinellas RFP 24-01 [practice]; definition working |
| User acceptance testing | Testing by the buyer's users that the delivered system works, before it is accepted | Mississippi RFP 4459 Attachment A [practice]; definition working |
| Product team | The people who decide what the product does | Working |

## Sources

All addresses opened on 28 November 2026; the source log gives what was read at each. Sources cited only through earlier units (Gartner's press release of 13 April 2022; Gartner's 2024 Magic Quadrant methodology note; Forrester RES181465; Olson, Johansson and de Carvalho 2012, for Keil and Tiwana) are listed in SCE1 and SCE11.

- Alabama Alcoholic Beverage Control Board. "Request for Proposal: Warehouse Automation with Software Integration". 17 July 2024. https://alabcboard.gov/sites/default/files/2024-07/ABC%20RFP%20final%20July%2017%202024.pdf
- ARC Advisory Group. "Warehouse Management System Selection". Undated. https://www.arcweb.com/technology-evaluation-and-selection/warehouse-management-systems
- ARC Advisory Group. "Warehouse Management System Selection" (second page of the same title). Undated. https://www.arcweb.com/technology-evaluation-and-selection/warehouse-management-system-selection
- Baki, B. & Çakar, K. (2005). Determining the ERP package-selecting criteria: The case of Turkish manufacturing companies. *Business Process Management Journal* 11(1), 75–86. https://doi.org/10.1108/14637150510578746 (abstract, read at https://www.emerald.com/insight/content/doi/10.1108/14637150510578746/full/html)
- Bernroider, E. & Koch, S. (2001). ERP selection process in midsize and large organizations. *Business Process Management Journal* 7(3), 251–257. https://doi.org/10.1108/14637150110392746 (abstract, read at https://emerald.com/insight/content/doi/10.1108/14637150110392746/full/html)
- City of Birmingham, Alabama. "RFP Section 4: Requirements Matrix". 2024 (the page shows no title or date; year from the address). https://birminghamal.gov/wp-content/uploads/2024/08/RFP-Section-4.pdf
- Forrester. "The Forrester Wave Methodology". Last modified 28 April 2026. https://www.forrester.com/marketing/policies/forrester-wave-methodology.html
- G2. "G2 to Acquire Capterra, Software Advice, and GetApp from Gartner". 29 January 2026. https://company.g2.com/news/g2-acquires-capterra-software-advice-getapp
- G2. "Research Scoring Methodologies". Published 21 November 2023, updated 26 October 2026. https://documentation.g2.com/docs/research-scoring-methodologies
- Gartner. "The B2B Buying Journey". Undated. https://www.gartner.com/en/sales/insights/b2b-buying-journey
- Gartner. "How do I use a Gartner Magic Quadrant?". Undated. https://gartner.co.uk/en/methodologies/magic-quadrants-research
- Gartner. "Gartner Survey Finds That Majority of Technology Purchases Come with High Degree of Regret". Press release, 12 July 2022. https://www.gartner.com/en/newsroom/press-releases/2022-07-12-gartner-finds-that-majority-of-technology-purchases-come-with-high-degree-of-regret
- Gartner. "Gartner Sales Survey Finds 74% of B2B Buyer Teams Demonstrate "Unhealthy Conflict" During The Decision Process". Press release, 7 May 2025. https://www.gartner.com/en/newsroom/press-releases/2025-05-07-gartner-sales-survey-finds-74-percent-of-b2b-buyer-teams-demonstrate-unhealthy-conflict-during-the-decision-process
- Gartner. "Gartner Sales Survey Finds 67% of B2B Buyers Prefer a Rep-Free Experience". Press release, 9 March 2026. https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience
- Gartner Digital Markets. "2025 Software Buying Trends Report". Undated. https://gcom.pdo.aws.gartner.com/en/digital-markets/insights/2025-software-buying-trends
- Gartner Digital Markets. "About" ("A growth accelerator for every business"). Undated. https://gcom.pdo.aws.gartner.com/en/digital-markets/about
- Gartner Peer Insights. "About us" (page headline at reading: "Gartner acquires Pulse to enhance your leadership community"). Undated. https://www.gartner.com/peer-insights/about-us
- Grewal, R., Lilien, G. L., Bharadwaj, S., Jindal, P., Kayande, U., Lusch, R. F., Mantrala, M., Palmatier, R. W., Rindfleisch, A., Scheer, L. K., Spekman, R. & Sridhar, S. (2015). Business-to-Business Buying: Challenges and Opportunities. *Customer Needs and Solutions* 2(3), 193–208. https://doi.org/10.1007/s40547-015-0040-5 (read in full at https://link.springer.com/content/pdf/10.1007/s40547-015-0040-5.pdf)
- Howcroft, D. & Light, B. (2008). IT consultants, salesmanship and the challenges of packaged software selection in SMEs. *Journal of Enterprise Information Management* 21(6), 597–615. https://doi.org/10.1108/17410390810911203 (abstract, read at https://emeraldinsight.com/insight/content/doi/10.1108/17410390810911203/full/html)
- Howcroft, D. & Light, B. (2010). The Social Shaping of Packaged Software Selection. *Journal of the Association for Information Systems* 11(3). https://doi.org/10.17705/1jais.00224 (abstract, read at https://aisel.aisnet.org/jais/vol11/iss3/2)
- Info-Tech Research Group. "Drive Successful Sourcing Outcomes With a Robust RFP Process". Published 11 August 2020, last modified 24 July 2023. https://www.infotech.com/research/ss/drive-successful-sourcing-outcomes-with-a-robust-rfp-process
- Info-Tech Research Group. "ERP Vendor Demonstration Script Template". H. Kwok. Published 10 April 2023, last modified 15 October 2026. https://www.infotech.com/research/erp-vendor-demonstration-script-template
- Info-Tech Research Group. "Master the Enterprise Application Vendor Demo". A. Hay. Published 18 December 2007, last modified 3 April 2012. https://www.infotech.com/research/master-the-enterprise-application-vendor-demo
- Jalkala, A. & Salminen, R. T. (2009). The Practices and Functions of Customer Reference Marketing – Leveraging Customer References as Marketing Assets. IMP Group conference, Marseille (abstract). https://impgroup.org/?p=4961
- Mississippi Department of Education. "Attachment A to RFP No. 4459: MDE Food Distribution Software Technical Requirements". Undated. https://rfps.its.ms.gov/Procurement/rfps/4459/4459attachmenta.pdf
- New Zealand Government Procurement. "Setting up the evaluation panel". Published 5 October 2017, last modified 9 February 2021. https://procurement.govt.nz/procurement/guide-to-procurement/plan-your-procurement/setting-up-the-evaluation-panel
- Pinellas County Sheriff's Office. "Request for Proposal (R.F.P.) 24-01, Inventory Management System (IMS)". 12 January 2024. https://pinellassheriff.gov/WebFormsEntry/UploadedFiles/567/RFP%2024-01.pdf
- TrustRadius (an HG Insights company). "TrustRadius 2026 B2B Buying Disconnect Report Reveals AI Has Changed How Buyers Research, But Not What They Trust". Release, 15 July 2026. https://hginsights.com/news/trustradius-2026-b2b-buying-disconnect-report-reveals-ai-has-changed-how-buyers-research-but-not-what-they-trust/
- UK government. "Bid Evaluation guidance note". May 2021 (issuing department not named on the page; Crown copyright). https://assets.publishing.service.gov.uk/media/60a387e48fa8f56a3e32fa9a/Bid_evaluation_guidance_note_May_2021.pdf
- Verville, J. & Halingten, A. (2002). An investigation of the decision process for selecting an ERP software: the case of ESC. *Management Decision* 40(3), 206–216. https://doi.org/10.1108/00251740210420156 (abstract, read at https://emerald.com/insight/content/doi/10.1108/00251740210420156/full/html)
- Virginia Information Technologies Agency (VITA). "24.3.1 Putting together the procurement project team (PPT) and evaluation team (ET)", in chapter 24, "Requests for Proposals and Competitive Negotiations". Undated. https://www.vita.virginia.gov/procurement/buy-it-manual/chapter-24---requests-for-proposals-and-competitive-negotiations/2431-putting-together-the-procurement-project-team-ppt-and-evaluation-team-et.html
- Washington State Department of Enterprise Services. "Request for Information (RFI) Survey: Asset Management Software Solution". 7 February 2024. https://des.wa.gov/sites/default/files/2024-02/FPS-asset-management-software-RFI.pdf

Filed units cited: SCE1 (§§7, 8, 9, 10, 11), SCE5 (§2), SCE6 (§§1, 2, 3, 4, 9, 11), SCE10 (§§2, 7), SCE11 (§§2, 3, 3.6, 4, 5, 6; deliverable B cards 1 to 6; glossary).

## Unsure list

# Unsure: SCE12

1. Quotations from the public PDFs and pages (VITA "these four corners of expertise", the UK guidance phrases, Pinellas "should be prepared to demonstrate all aspects of their service") are as a fetch tool extracted them; not checked against the rendered documents.
2. Pinellas RFP 24-01: resolved at the fresh check. The checker read the price items as Section B, 2.2.O to 2.2.R (section 9) and the interviews as §2.4.A (section 4); §1.13, §1.14, §1.15 and §2.4.B were confirmed; C.5 is as the extraction gave it.
3. The Birmingham requirements matrix shows no title, date or issuer; "City of Birmingham, Alabama" and 2024 are inferred from the address.
4. The UK "Bid Evaluation guidance note" (May 2021) does not name its issuing department on the page; Sources gives "UK government".
5. Jalkala & Salminen (2009) is graded practice because the IMP page does not state peer review; a checker may grade the 38-interview study independent. Salminen & Möller's journal details (volume 13, pp. 1–51) come from the IMP page only.
6. TrustRadius is described as a review site from search listings, not from the release; its survey is graded vendor-reported, and G2's method page vendor-reported while Gartner Peer Insights' page is graded analyst: a reading of SCE1's key a checker may question.
7. The Gartner Peer Insights "About us" page carried an unrelated announcement as its headline when read; Sources lists it by page name.
8. Baki & Çakar: "vendor references ranked fourth" is a reading of the abstract's order ("followed"); the sample size is not in the abstract.
9. Grewal et al. (2015): resolved at the fresh check. RePEc's record gives volume 2, issue 3, pp. 193–208 (opened 28 Nov 2026); Sources corrected.
10. Figures were rendered with viz.py copied into out/kit and a stub out/design/theme.css (only --topo-grow), both deleted after rendering; the real theme was not used, so final drawing at filing may differ in styling.

Fresh check 2026-11-28 (Opus 5.5 (claude-opus-5-5)): fix · 1 errors, 5 should-fix, 13 minor; report `audits/supply-chain-execution/fresh-check-SCE12.md`
