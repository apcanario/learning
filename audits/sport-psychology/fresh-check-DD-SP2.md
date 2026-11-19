---
audit: fresh check
unit: DD-SP2 · Deep dive: weight, body and who decides
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgQzDra5WhwrnjTVBqy8
verdict: fix · 2 errors, 7 should-fix, 10 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: DD-SP2 · fix · 2 error, 7 should-fix, 10 minor
Model: claude-opus-5-5

(The harness refused the write to out/report.md, so the whole report is here.)

Fresh check of DD-SP2 (audit-units section 3, with the figures paragraph), 19 Nov 2026. I did not edit the unit. No audit errata apply ("no audit report: skip it"). The filed units (SP1 to SP10, DD-SP1) are not in the packet, so every pointer to them is "not checked" (listed under UNVERIFIED). Web rule kept: I fetched only URLs that a search in this agent returned. I did not follow redirects, retry anything, or fetch a copy in place of a page that failed.

## Pass 1. Claims: FIX
Opened and checked: UWW rules, British Taekwondo SOP031, the IJA policy, World Rowing Rules of Racing (March 2025 and a later version), Lakicevic 2022 (repository full text), Veale & Matsunaga 2014, Mountjoy 2023 (PubMed abstract), Joy 2016 (full text and info page), Boudreault 2022 (SPONET abstract record), Lakicevic 2021 (DOAJ abstract), De Souza 2026 (Penn State and SPONET records), Li 2024 (index record with abstract), Kenđel Jovanović 2024 (abstract), Sullivan 2023 (RePEc abstract), Castor-Praga 2021 (full text), Willson 2025 (abstract), Dvořáková 2024 (PDF), Teixidor-Batlle 2021 (abstract and record), Kovács 2022 (full text), Stoyel 2021 (full text to 100,000 characters), Baceviciene 2023 (full text), Kontele 2022, Albaladejo-Saura 2021, Malina 2013 (PDF), Werner 2013 (repository PDF), Lavender 2017 (abstract).
- Two attribution errors. Section 13 cites Dvořáková for a warning that the review attributes to the IOC consensus. Section 15 credits Stoyel's participants with a statement that is the authors' introduction, drawn from earlier literature.
- Section 8 gives an adult-height prediction error of −0.45 to −2.1 cm. That does not match Sullivan's abstract, which says three methods came within 1 cm (unsure item 6).
- Section 6 names France among the countries of the review's studies. The review names Belgium, not France.
- Not opened (redirect or reCAPTCHA): the full texts of Boudreault (PMC), Lakicevic 2021, Ganson 2025 (PMC), Li 2024 (PMC), and the full texts of Kenđel Jovanović, Willson and Teixidor-Batlle (the pages served only abstracts). Their full-text-only figures are under UNVERIFIED.

## Pass 2. Bibliography: FIX (minor)
- Mountjoy 2023: 57(17):1073–1097 confirmed on PubMed. The seed list's 1098 is wrong, so unsure item 3 is resolved in the unit's favour. I did not see the authors at the publisher.
- De Souza 2026: Sports Med 56(2):327–373 confirmed. The Penn State record lists 15 authors, Plessow last, and gives the online date as 4 Feb 2026. The unit gives 31 Dec 2025 (UNVERIFIED).
- Boudreault 2022: SPONET gives pages 431–439 for 57(3). The unit says "pages not seen".
- Malina 2013: the PDF lists 9 authors, ending Rogol AD, Russell K. The unit's "et al." is harmless.
- Teixidor-Batlle: vol. 11, article 559832, published 26 Jan 2021. Matches.
- Willson: vol. 6 (2024), year listed as 2025. Matches the unit's note.
- Dvořáková: the PDF is labelled "TYPE Systematic Review". Matches.
- Joy 2016: I could confirm only the 50/3/154 path. The end page (162) and the authors other than Joy are not confirmed.
- Lakicevic 2021: vol. 13, issue 1. Article number not seen, as the unit says.
- All other entries match their record on title, journal, year, volume and DOI.

## Pass 3. Source log: PASS
Every Sources entry is in sources.md with its address, what was read and the date. Each abstract-only claim says "abstract read": Mountjoy, Kontele, Albaladejo-Saura, Lavender. The five "named, not opened" entries carry no claim.

## Pass 4. Grades: PASS (SP1 not checked)
I could not check SP1 section 9 itself (filed unit not in the packet). Against the brief's key:
- Section 5 [weak] is right: cross-sectional and qualitative studies only.
- Section 8 [weak] is right: one review, no pooling, with inference for girls.
- Every [practice] line says that no study tests it.
- Consensus claims whose studies were not opened are graded [practice] with the required note.
- Narrative reviews: none carries a grade. The source-type caveat is applied to Lakicevic 2021 but not to Malina 2013 (minor finding).

## Pass 5. Population: FIX
Adult samples applied to coaching young athletes without the inference label:
- Stoyel (aged 19 to 44) in sections 5 and 15.
- Kovács (retired gymnasts, mean age 20.25) in section 5. Section 13 does label it.

Every other finding names its sample and design. Willson and Ganson carry the label.

## Pass 6. Scope and safety: PASS
- No weight-loss method, calorie figure or target weight appears anywhere, examples and scripts included. "Eating less, drinking less or training extra" names restriction only so it can be referred. Dehydration is named only as the harm British Taekwondo's rule prevents.
- No self-harm method.
- No law is stated as the reader's: legal duties are put as questions (section 11, D9), with the disclaimer in the preamble.
- No real athlete, coach or club is named.
- Body dysmorphic disorder is defined once, from a clinical source (Veale & Matsunaga, an account of the ICD-11 proposals, with that status stated). It is kept apart from body dissatisfaction in sections 4 and 16.
- Each federation rule was read by me on the federation's own page and is dated. One version is superseded (World Rowing, should-fix).
- Internal inconsistency: section 11 says decisions wait for medical input whenever an eating concern is open, but Deliverable A records Dani's decision while her concern is open (should-fix).

## Pass 7. Any sport: PASS (on estimate)
- Body examples by my count: judo and gymnastics are each roughly a quarter. The rest come from wrestling, taekwondo, boxing, rowing, endurance sports, football, basketball and rugby.
- The deliverable is judo throughout, as the brief requires ("built in full for Dani"), and its templates are sport-neutral.
- The check for anything a reader of the Project's owner would recognise could not be run: private_terms.py is not in the packet.

## Part 7, line by line
Every line PASS except these:
- Bibliography match: minor fixes.
- Adult-to-youth inference: Pass 5.
- Date of each rule read on the issuing body's page: World Rowing should cite the later version.
- Case facts: two invented details not listed in the notes (minor).

Read as the coach in the preamble: usable and specific. The main confusion is the section 11 / Deliverable A conflict over whether an open eating concern holds up the class decision.

## Figures (7)
1. Section 6, range: FIX (minor). Every number traces to the text. The caption names the section and the source. Range fits competing estimates. The judo row is one study of three, so label it.
2. Section 11, matrix: PASS. Rows trace to section 11 and steps 1 to 6. Caption complete. Matrix fits items by roles.
3. Section 12, flow: FIX (should-fix). Flow fits a sequence. But the first note, "not said", contradicts the text for adults ("For an adult, a view given once when asked is the most you offer").

FINDINGS
[error] [attribution] section 13; Current: "A review of the markers used to diagnose REDs warns that too much attention to body measurements and composition can increase the pressure on athletes, especially those under 18"; Problem: the review attributes this warning to the IOC consensus statement ("The authors of the IOC Consensus statement also pointed out that too much focus on anthropometric parameters and body composition can intensify the pressure placed on athletes, especially on adolescents under the age of 18 years"). Part 1 requires the reporter to be kept separate from the claim; Fix: "A systematic review of the markers used to diagnose REDs reports that the authors of the IOC consensus statement pointed out that too much focus on body measurements and composition can intensify the pressure on athletes, especially adolescents under 18 (the IOC statement itself was read here only in its abstract, which does not say this)"; Basis: Dvořáková et al. 2024, https://frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1375740/pdf
[error] [attribution] section 15; Current: "and athletes described pressure to be thin for performance and for how they looked to judges and others (Stoyel et al., 2021)"; Problem: "pressure to be thin to maximize both performance and appearance for judges and others" is the authors' introduction about lean sports in general, drawn from earlier literature. It is not a finding from the nine endurance athletes, none of whom competed in a judged sport. The sample is also adult; Fix: "and the authors' introduction, drawing on earlier studies, describes a pressure in lean sports to be thin for performance and for appearance to judges and others (Stoyel et al., 2021; the interviews were with nine adults aged 19 to 44, so for under-18s this is the unit's inference)"; Basis: Stoyel et al. 2021, https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.633490/full
[should-fix] [deliverable] section 11; Current: "Where any restriction would be needed (eating less, drinking less or training extra to make or hold a weight), or where any concern about eating, weight or body is already open, it waits for medical input."; Problem: Deliverable A records Dani's decision ("Medical input: not needed for this choice") while her eating concern is open, which this sentence forbids. A coach following both cannot tell which rule holds; Fix: "Where any restriction would be needed (eating less, drinking less or training extra to make or hold a weight), it waits for medical input. Where a concern about eating, weight or body is already open, a choice that needs no restriction may be recorded and the medical contact is told of it; any choice that could need restriction waits for them."; Basis: internal consistency (unit section 11 against Deliverable A, "Medical input" and "The decision, as recorded")
[should-fix] [deliverable] Deliverable A template; Current: "Whether it is needed (any restriction, or any open concern), who gives it, and the date it was given."; Problem: the same conflict in the template; Fix: "Whether it is needed (any restriction), who gives it, and the date it was given; where a concern is already open, the date the medical contact was told of the decision."; Basis: as above
[should-fix] [accuracy] section 18; Current: "**Rowing: World Rowing, *Rules of Racing* (version March 2025).**"; Problem: World Rowing's site carries a later version of the Rules of Racing (Overall & Classic Rowing, "Last updated: July 1, 2025", posted April 2026). Rule 19, Rule 26 and the Bye-Law to Rule 23 are unchanged in it; Fix: "**Rowing: World Rowing, *Rules of Racing* (version March 2025; the later version on World Rowing's site, last updated 1 July 2025, has the same Rules 19 and 26 and Bye-Law to Rule 23, checked 19 Nov 2026).**"; Basis: https://d2cx26qpfwuhvu.cloudfront.net/worldrowing/wp-content/uploads/2026/04/13160233/overall-classic-rowing-v1-2026-04-13-1.pdf
[should-fix] [accuracy] section 18; Current: "junior rowers do not race in weight categories at all"; Problem: overstates the source. World Rowing's rules cover its own events only, and a national federation may run junior lightweight events; Fix: "junior rowers do not race in weight categories at World Rowing's events (ask your national federation about its own junior events)"; Basis: World Rowing Rules of Racing, Rules 19 and 26, https://worldrowing.com/wp-content/uploads/2025/04/2025-World-Rowing-Rules-of-Racing-Overall-Classic-rowing-Related-byelaws_March2025.pdf
[should-fix] [figure] section 8; Current: "The review does report predicted adult *height* falling within about half a centimetre to two centimetres of observed adult height (discrepancies of −0.45 to −2.1 cm)"; Problem: the review's abstract says three methods estimated adult height "within 1cm of actual adult height", and that "Discrepancies were evident between actual and predicted adult height and age at PHV". The unit's range and its sign were not found and are on the writer's unsure list (item 6); Fix: "The review's abstract does report three methods estimating adult *height* to within 1 cm of actual adult height, while noting discrepancies between predicted and actual adult height and age at peak height velocity"; Basis: Sullivan et al. 2023, abstract, https://ideas.repec.org/a/plo/pone00/0286768.html
[should-fix] [figure] section 12, figure 3; Current: "{"label": "A view, said once", "note": "outside DD-SP1's card: not said"}"; Problem: contradicts the text for adults ("For an adult, a view given once when asked is the most you offer"); Fix: "{"label": "A view, said once", "note": "under 18: not said; an adult who asks: once, about the competition"}"; Basis: unit section 12, final paragraph, and section 11, step 3
[should-fix] [label] section 5; Current: "Endurance athletes in the UK interviews described coaches' comments as one of the pressures that added up (Stoyel et al., 2021)."; Problem: the sample is adults aged 19 to 44, with no inference label. What I could read supports coaches' expectations feeding the link between appearance and performance, not a list of comments. Kovács's gymnasts in the same bullet are retired adults, also unlabelled here; Fix: "Adult endurance athletes (aged 19 to 44) in the UK interviews described coaches' expectations as feeding the link between how they looked and how they performed (Stoyel et al., 2021). For athletes under 18, both studies in this bullet are the unit's inference."; Basis: Stoyel et al. 2021, https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.633490/full; Kovács et al. 2022, https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.955232/full
[minor] [accuracy] section 18; Current: "between one and two hours before their first race of each event (Bye-Law to Rule 23)"; Problem: the bye-law applies on each day of competition; Fix: "between one and two hours before their first race of each lightweight event on each day of racing (Bye-Law to Rule 23)"; Basis: World Rowing Rules of Racing, Bye-Law to Rule 23, URL above
[minor] [accuracy] section 6; Current: "studies from the United States, Israel, Croatia, Brazil and France among others"; Problem: the review lists the USA, Israel, Belgium, Croatia, Brazil (two studies) and a boxing study across twelve European countries. France is not named; Fix: "studies from the United States, Israel, Belgium, Croatia and Brazil, and a boxing study across twelve European countries"; Basis: Lakicevic et al. 2022, https://core.ac.uk/download/519724025.pdf
[minor] [figure] section 6, figure 1; Current: "{"label": "Judo", "low": 80"; Problem: 80% is one study (Berkovich et al.) of the review's three judo studies, while the boxing row is labelled "(1 study)"; Fix: "{"label": "Judo (1 of 3 studies)", "low": 80"; Basis: Lakicevic et al. 2022, URL above
[minor] [label] section 13; Current: "a "blinded weight" (taken without showing the athlete the number)"; Problem: Joy et al. list "Vital signs—blinded weight" without defining it, so the gloss is the unit's; Fix: "a "blinded weight" (the review does not define it; read here as a weight taken without showing the athlete the number)"; Basis: Joy et al. 2016, https://bjsm.bmj.com/content/50/3/154.long
[minor] [attribution] Sources, Boudreault; Current: "2022;57(3) (first published online 26 May 2021; pages not seen)"; Problem: the pages can be filled in; Fix: "2022;57(3):431–439 (first published online 26 May 2021; pages from the SPONET record)"; Basis: https://www.sponet.de/sponet/Record/4079527?lng=en (to be confirmed against Crossref at filing)
[minor] [style] section 14; Current: "## 14. Competition-day weigh-ins: what you say before and after (F120)"; Problem: an internal flag code in a reader-facing heading. The same applies to "(F16)" (sections 4 and 8), "F124" (section 14), "(F139)" (section 17), "F168" and "(F171)" (section 19), and "F120" (C5); Fix: "## 14. Competition-day weigh-ins: what you say before and after"; Basis: brief (reader is a coach; tone)
[minor] [style] section 12; Current: "**The decision on F182.**"; Problem: an internal flag code the reader cannot decode; Fix: "**Why weight stays outside the comment test card.**"; Basis: brief
[minor] [label] section 7; Current: "([Malina et al., 2013, review, full text read to the section on diet](https://doi.org/10.1007/s40279-013-0058-5))"; Problem: a narrative review is outside Part 7's source types. The unit flags this for Lakicevic 2021 but not here; Fix: "([Malina et al., 2013, narrative review, full text read to the section on diet](https://doi.org/10.1007/s40279-013-0058-5); a narrative review is outside the course's source types, and no grade rests on it)"; Basis: sourcing-standard Part 7; Malina et al. 2013, https://link.springer.com/content/pdf/10.1007/s40279-013-0058-5.pdf
[minor] [accuracy] Deliverable B, card 1; Current: ""Weigh-in is at 8:30. Bring your ID card and both judogi.""; Problem: an invented case time that is not listed in the notes for the register. "Warm-up is at 9:40, mat 2" (sections 14, B2, C5) needs the same listing; Fix: ""Weigh-in is at [time]. Bring your ID card and both judogi."" (or list 8:30 and 9:40 in the notes as *added*); Basis: brief (invented case facts listed in the notes); case-facts.md
[minor] [accuracy] Deliverable B, card 10; Current: ""Strength sessions are Tuesday and Thursday, the same plan for your age group.""; Problem: invents a schedule for Dani's squad that is not in case-facts.md or the notes (Tuesday and Thursday are Milan's slots); Fix: ""Strength sessions are [days], the same plan for your age group.""; Basis: case-facts.md

(Every Current string above was checked by grep: each occurs exactly once in unit.md.)

UNVERIFIED
- Section 2 (De Souza): the 16-person panel, >85% agreement, the quotes on delayed menarche and growth restriction, and sections 3.1 and 3.2.1. The publisher's full text was not returned by my search. The Penn State record lists 15 authors, which does not settle the panel size.
- Section 2 (Mountjoy): author list (repository record not opened by me).
- Sections 3, 5, 6, 12, 16 (Boudreault): 4.1%, 3.9%, OR 8.04, 18.35, 11.95, and three in four. The full text was a PMC redirect, not followed. The abstract confirms 999, 14 to 17, 16.9%, 9.7%, 44% and 7.4%. It gives girls as 19.75%; the unit says 19.7%.
- Section 3 (Kenđel Jovanović): 59.7% under 18, school and local clubs, and in section 5 30.7%, 36.9%, 24.0% and 27.7%. Only the abstract was served. It confirms 462, 12 to 25, six countries, 14.9%, 19.9%, 44.6% and 46.1%, and says younger athletes reported more coach pressure (unsure item 8).
- Sections 3, 4, 16 (Li): 11,184 participants; the age pattern (adult men more concerns than adolescent boys); the male wrestlers. Only the abstract was served, which confirms 31 studies and "complex and inconclusive".
- Section 5 (Willson): r = .311; "current and recently retired"; over 16; mean age 27.85; indicators higher in aesthetic or weight-class athletes. The abstract reports only a positive correlation and a marginal interaction for aesthetic or weight-based athletes.
- Sections 5 and 13 (Teixidor-Batlle): the introduction listing public weigh-ins. Abstract only. The abstract confirms 646, 33 sports, mean age 16.7, Catalonia, and coach and sport-specific pressure higher in symptomatic female athletes.
- Section 16 (Ganson): all figures and the definition (PMC redirect, not followed).
- Sections 6 and 7 (Lakicevic 2021): 60–90%, "as early as 12", the growth quote. The DOAJ abstract lacks them; the publisher PDF redirected. The weigh-in recommendation is confirmed.
- Section 8 (Sullivan): the verbatim quote "none of the estimated ages at PHV were equivalent to actual ages at PHV" (abstract only; consistent in sense).
- Section 18 (UWW): "each wrestler enters one category, the one corresponding to their weight at the official weigh-in" (not reported in my read).
- Section 4: the final ICD-11 text for body dysmorphic disorder (no WHO page returned by search).
- Filed units, not in packet: SP1 section 9 grade key; SP2 bands, three clocks and section 10; SP3; SP6 (referral, pressure cap 3); SP7; SP8 (the "Meet at 7:30 at the club. Bring two judogi and lunch" message, "Sleeve first", normal volume); SP9's red-flag rows, the scoping-review figures (0–14%, 11–41%) and the IOC mental health quote; SP10 rows and the "Not mine" line; DD-SP1 sections 1, 2, 5, 9 and 17, comment 11 ("You'd fly if you lost a bit"), card questions 3, 6 and 7, and E2/E3.

Confirmed
- UWW, January 2026: U15 14–15 (from 13 with medical and parental authorisation), U17, U20; weigh-in each morning of the category after a medical examination, singlet only; "The weigh-in and the medical control lasts 30 minutes."; no rule specific to minors' weight in the part read. https://cdn.uww.org/2025-12/wrestling_rules_1.pdf
- British Taekwondo SOP031 v5a, June 2024, sections 6.1, 6.2, 6.4 (smaller margins for younger categories; the dehydration sentence; "never BT's recommendation ... particularly very young athletes"), 6.6–6.7 (random weigh-ins, list published in advance). https://www.britishtaekwondo.org.uk/wp-content/uploads/2024/08/Weigh-In-Policy.pdf
- IJA policy, version 1, 01.02.2022, review due 01.02.2025: Pre-Cadet and Cadet "must compete in the weight category above"; referral to coach or nutrition professional and to the Nutrition Lead; "may be deselected". https://irishjudoassociation.ie/wp-content/uploads/2024/05/IJA-Weight-Management-Policy-2022.pdf
- World Rowing, March 2025: Rule 19 lightweight "for Seniors and Under 23"; no U19 lightweight event; weighed in racing uniform, 1–2 h before, as a crew. URL above.
- Lakicevic 2022: 7 studies, 3,135, ≤19; wrestling 42–77% (3 studies), judo 80%, boxing 25%; abstract 25–94%, with 94% attributed to older athletes; ages 4 and 9; coaches the main encouragers; the "stringently regulated and ideally banned" quote; less focus on categories for 13 and under; similar to adults. https://core.ac.uk/download/519724025.pdf
- Lakicevic 2021: weigh-ins closer to the start of competition. https://doaj.org/article/5f21520e4da541e98dd47275ba901c17
- Veale & Matsunaga 2014: "either unnoticeable to others or only slightly noticeable"; repetitive or avoidance behaviours; "either significantly distressing or interfering with one's life"; the "too fat" sentence; the adolescent continuum; no muscle dysmorphia specifier; bibliographic details. https://www.scielo.br/j/rbp/a/SWBw7Ys3CPWGgFRkV3hZKjS/?lang=en
- Mountjoy 2023: three abstract quotes; data on low energy availability in males; 57(17):1073–1097. https://pubmed.ncbi.nlm.nih.gov/37752011/
- Joy 2016: "even in the absence of a formal eating disorder diagnosis"; leanness sports in the abstract; "blinded weight" in follow-up vital signs. https://bjsm.bmj.com/content/50/3/154.long
- Castor-Praga 2021: 160, aged 7–24, mean 13.34, Mexico; Table 13 26% + 40% = 66%; discussion 86% (inconsistent in the source, as the unit says); coaches most influential; "sporting identity" cited, not measured; 6:637671. https://www.frontiersin.org/articles/10.3389/fsoc.2021.637671/full
- Kovács 2022: 4 retired gymnasts (mean age 20.25), 5 coaches, 3 mothers, Hungary; lean body linked to success by all groups; weighing in front of teammates; home weighing after retiring; the "Nothing is more humiliating..." quote; coach-judges not free to give the deserved score. https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.955232/full
- Stoyel 2021: 9 athletes aged 19–44, UK, mostly endurance; "If you're light and you're thin, you're expected to be fast."; costumes intensify comparison. https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.633490/full
- Baceviciene 2023: 1,003, aged 15–44, Lithuania, 2022, cross-sectional; aesthetic females more coach body pressure and more self-weighing; adolescent females more disordered-eating behaviours; adult males more restraint; drive for muscularity measured; 15(12):2724. https://www.mdpi.com/2072-6643/15/12/2724/htm
- Kontele 2022: 147 and 122 aged 11–17; 16.3% and 7.4%; 30.3% of variance; competitive gymnasts higher on appearance pressure; 9(2):254. https://mdpi.com/2227-9067/9/2/254/htm
- Albaladejo-Saura 2021: girls, only height and body mass (SMD 0.96–1.19); "more research is needed"; 18(1):328. https://mdpi.com/1660-4601/18/1/328
- Malina 2013: cause–effect quote; adult height not compromised; pubertal growth not attenuated; select, shorter sample; energy intake suggested as inhibitory; endocrine data inadequate; 43:783–802. https://link.springer.com/content/pdf/10.1007/s40279-013-0058-5.pdf
- Werner 2013: 15 studies, aged 12–25; "no certainty that the prevalence is higher than in control groups" except leanness sports; competitive pressure a risk factor for both genders; "data are inconsistent"; 1:18. https://publications.goettingen-research-online.de/bitstream/2/97184/1/document.pdf
- Sullivan 2023: 15 studies, 4,707 players U9–U18, no meta-analysis, poor concordance between methods; 18(9):e0286768; authors. https://ideas.repec.org/a/plo/pone00/0286768.html and https://econpapers.repec.org/RePEc:plo:pone00:0286768
- Lavender 2017: the "increasingly focusing on muscularity-oriented manifestations" quote; 19(6). https://www.springermedizin.de/men-muscles-and-eating-disorders-an-overview-of-traditional-and-/12262088
- Dvořáková 2024: labelled "TYPE Systematic Review"; authors; vol. 6. https://frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1375740/pdf
- De Souza 2026: title, Sports Med 56(2):327–373, DOI, author order. https://pure.psu.edu/en/publications/2025-update-to-the-female-athlete-triad-coalition-consensus-state/
- Teixidor-Batlle 2021: vol. 11, article 559832, 26 Jan 2021. https://diposit.ub.edu/items/c84c4abf-f189-4391-8b5f-099fe7cc2ea8/full
