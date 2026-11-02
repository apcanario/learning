---
code: DD-A2
title: Deep dive: the exit math
course: brand-ai · A · Building a Marketable Personal Brand
model: Opus 5.5
written: 2026-11-02
search: off
---

# DD-A2 · Deep dive: the exit math

This unit is the last of course A, written with A1 to A9 and DD-A1 filed, and it takes their numbers as its inputs. Search was off. On 2 November 2026 it verified three points: the euro–dollar reference rate, the Social Security Institute's rule on unemployment benefit after a resignation, and one bank's guidance on emergency savings; each carries that date. Searches for Portuguese long-term unemployment figures opened nothing readable, and nothing from them is used. Every household figure is the brief's. Every other number is a filed unit's, named by section, or my arithmetic on them, run by script and shown. Nothing here assumes that the job should end or will: the model answers one question, the earliest date on which the evidence would let an exit be considered, and it leaves the decision with him.

## 1 · The household floor

**What the brief gives.** Take-home €4,800 a month; a current margin of about €0; a car credit of €430 a month until August 2027. A margin of zero means the household spends what it takes home, so this unit reads monthly outgoings as €4,800. The brief does not say whether the second earner's income sits inside the €4,800 or on top of it; the model handles both readings through one input (§2), and the unsure list records the question.

**What changes in September 2027.** When the car credit ends, outgoings fall to €4,800 − €430 = €4,370, provided the €430 is not spent on something else (my arithmetic; the provision is an assumption he confirms). That €430 is also the first money the household can save: with a margin of zero, nothing is saved before September 2027 unless spending is cut.

**The floor in one line.** €4,800 a month until August 2027, €4,370 from September 2027. Across calendar 2027 that is 8 × €4,800 + 4 × €4,370 = €55,880 (my arithmetic).

**Why the floor is larger than it looks.** Salary arrives after tax and social security. Income from a channel, a brand or clients arrives gross, and A8 sets what comes off it. An independent worker contributes "21,4 %" on relevant income, which for services is 70% of the amount invoiced and for goods 20% ([Decreto-Lei 2/2018, arts. 162.º and 168.º of the Código dos Regimes Contributivos](https://seg-social.pt/documents/10152/15523435/DL_2_2018/9a9cffcd-29c6-44a4-b1fc-72c5aceedcd6), as A8 §3 gives it). That is 21.4% × 70% = 14.98% of service income and 21.4% × 20% = 4.28% of sales of goods (my arithmetic). While he is employed, service income below four times the IAS (€2,148.52 of relevant income a month in 2026) can be exempt, but only if the job continues: one of the three conditions is mandatory cover from the employment ([gov.pt, updated 3 Sep 2026](https://www.gov.pt/servicos/requerer-a-isencao-do-pagamento-de-contribuicoes-para-a-seguranca-social), A8 §3). After an exit the exemption cannot apply. IRS comes on top. A8 §1 found that category B income is aggregated with salary while he is employed and did not open the 2026 brackets, so this unit models no income-tax rate; the accountant's figure is an unfilled input.

So the side income that replaces €4,370 of take-home has to be €4,370 ÷ (1 − 0.1498) = **€5,139.97 a month** of service income, €61,679.60 a year, before IRS (my arithmetic). Before September 2027 the same sum on €4,800 is €5,645.73.

## 2 · A survivable floor with a variable second income

The brief asks what a survivable floor is, given that the second earner's income varies. No filed unit gives its amount or its range, and this unit invents none. What the model can fix is how the variable income enters.

**The rule (his rule; no source sets it).** The survivable floor is

F_s = outgoings − C − V_min

where **C** is spending the household has agreed in writing to cut if his salary stops, and **V_min** is the second earner's lowest single month of income over the last twelve, counting only the part that pays household costs. The minimum month is used because a variable income averaged over a year hides the month that breaks the budget; a runway sized on the average runs out in the bad month.

- If the €4,800 already includes the second earner's income, V_min is the lowest month of that share.
- If the €4,800 is his take-home alone and the household also spends the second income, outgoings are €4,800 plus that income, and the lowest month cancels the part of it that is reliable. In both readings, F_s is what his salary covers in the second earner's worst month.

**The default is the sole-earner case.** The brief asks how much runway a sole earner needs, so every number in this unit sets V_min = 0 and C = 0 until he enters his own. At those defaults F_s = €4,370 from September 2027. Every €100 of V_min or C lowers F_s by €100 and the side-income target by €100 ÷ 0.8502 = €117.62 a month (my arithmetic).

**What the state does not cover.** The unemployment benefit is no part of any exit path. The Social Security Institute's practical guide requires unemployment "por razões alheias à sua vontade", lists a worker's own termination of the contract ("denúncia do contrato de trabalho/demissão por iniciativa do trabalhador") as voluntary, and accepts a termination by mutual agreement only in cases of restructuring or economic difficulty at the employer ([ISS, *Guia prático: subsídio de desemprego*, 6001 v4.72, 20 Feb 2025](https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b); official guidance, read 2 Nov 2026). Leaving to build an independent income is a resignation. The same guide caps the benefit at two and a half times the IAS, which it states as €1,306.25 a month, which would be 27.2% of €4,800 in any case (my arithmetic). Every month of an exit is paid from savings or from side income.

## 3 · How many months of runway a sole earner needs

**What the sources say.** No study among the filed units, and none found on 2 November 2026, measures how long an employee who leaves to build creator or freelance income takes to replace a salary, which is the quantity a runway has to cover. The one source opened is a bank's consumer guidance, without a dataset: Caixa Geral de Depósitos says an emergency fund should equal "pelo menos, seis meses de despesas", and that under current uncertainty the margin should be "pelo menos, um ano de despesas" ([CGD, Saldo Positivo, *Constituir um fundo de emergência*, 9 Apr 2026](https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx); bank guidance, read 2 Nov 2026). It does not distinguish one-income households or variable incomes.

**Why this unit uses twelve months (his rule).** Three facts from the sources push to the top of the bank's range. There is no state bridge after a resignation (§2). Three of the four lines the brief names (brand deals, consulting, courses) have no sourced time to first income at all (§4). And A9's checkpoints read the channel once a quarter, so a test that needs two readings to pass needs about six months just to be read twice; a six-month runway would be spent by the time the second reading arrives. The model carries six months as the sensitivity.

**What twelve months costs.** 12 × €4,370 = **€52,440**; six months is €26,220 (my arithmetic).

**How long it takes to save.** No filed unit gives the household's savings, and the brief's margin of zero says none are being added now. The model calls existing savings **S0**, an unfilled input set to 0 by default. From September 2027 the household can save the €430 the car credit frees, plus any agreed cut C. Then

months to runway = (12 × F_s − S0) ÷ (€430 + C)

At the defaults: €52,440 ÷ €430 = 121.95, so 122 months, counted from September 2027 to October 2037. The first quarterly checkpoint after that is Tuesday 3 November 2037. The six-month runway takes €26,220 ÷ €430 = 60.98, so 61 months, to September 2032, first read at the checkpoint of Tuesday 9 November 2032 (my arithmetic; checkpoints every 91 days from A3's dates, A3 §5). Each €1,000 already saved brings the date forward by €1,000 ÷ €430 = 2.33 months; each month of floor already saved (€4,370) brings it forward by 10.16 months.

The consequence is the main finding of this unit. **At the brief's numbers and zero savings, the runway alone takes until 2037 to save from salary; only a side income large enough to pass the income test on its own can pay for it sooner.** S0 is the most valuable number he has not entered.

## 4 · The income mix, line by line, and the timeline for each

The brief names four lines: brand deals, Shōmen margin, consulting or fractional product work, and courses. The filed units also measure two that are not on the list, a paid tier on the email list and YouTube ads, and those two are where the sourced numbers are. Each line below gives what the research documents, the earliest date the research supports, and how it enters the model.

### 4.1 · The paid tier: the only line with a dated route

**What is documented.** Two cases put the paid share of a list at about 0.9% and 1.6% ([Artificial Ignorance, 11 Feb 2025](https://www.ignorance.ai/p/two-years-of-artificial-ignorance); Generalist World via [beehiiv, 6 Jan 2026](https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md); A9 §7, documented cases). Patreon's company-sponsored survey gives $52 a year per fan and $110 per paying member ([Net Influencer, 21 Feb 2025](https://www.netinfluencer.com/patreon-2025-state-of-create-report-how-creators-are-breaking-free-from-platform-control/)), which A7 uses as prices (A7 a11). Substack and card fees are 13.6% plus $0.30 per monthly payment (A7 a12, from [Substack Support, updated 29 Sep 2026](https://support.substack.com/hc/en-us/articles/360037607131-How-much-does-Substack-cost)). Substack's own claim of 5–10% is a platform statement without a dataset (A9 §7).

**What the floor needs.** At $110 a year, a member nets $110 − $14.96 − $3.60 = $91.44 a year, which is €81.85 at the ECB reference rate of $1.1172 per euro on 30 October 2026 ([ECB, euro reference rates, US dollar](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.it.html), read 2 Nov 2026), or €6.82 a month. The target of €61,679.60 a year is $68,908.45, so 754 members, and at 1.6% a list of **47,125** (my arithmetic). At 0.9% the list is 83,778; at Substack's 5% it is 15,080.

**How fast a list grows, on the filed anchors.** A9 §6 and A7 §1 hold four: two newsletters written alongside other work, at about 833 and 2,000 subscribers a year ([The Introverted Networker, charts as of 28 May 2025](https://theintrovertednetworker.substack.com/p/how-i-grew-my-newsletter-to-2500); [The Creator's Playbook, 30 Jul 2025](https://thecreatorplaybook.substack.com/p/celebrating-1-year-on-substack); anecdotes); beehiiv's 2025 launches, at a median of 8,314 by the end of year one (platform-published, self-selected); and Amy Suto, 42,000 in three years, about 14,000 a year (my division; [Amy Suto, 4 Jul 2026](https://www.amysuto.com/desk-of-amy-suto/how-to-grow-a-substack); anecdote). At the two part-time paces, 47,125 takes about 57 and 24 years (47,125 ÷ 833 and ÷ 2,000; my arithmetic). At beehiiv's median it takes 5.67 years; at Suto's, 3.37 years.

**Timeline.** The earliest the tier can open is 1 September 2027, if the list is at least 1,000 at the review of 17 August 2027 (A7 a8). A9 §6 reports beehiiv's median time to first dollar for 2025 launches as 66 days (platform-published). The earliest date the tier could carry the floor is worked out in the deliverable: Tuesday 11 February 2031, at Suto's pace.

### 4.2 · YouTube ads: zero in 2027 and no route to the floor

New Partner Program applicants need 1,000 subscribers and 8,000 qualified watch hours from 1 February 2027 ([YouTube Help, answer 12843009](https://support.google.com/youtube/answer/12843009?hl=en); A9 row 11). A9 expects fewer than 1,000 subscribers at month twelve ([vidIQ, 11 Sep 2026](https://vidiq.com/research/youtube-uploads-1000-subscribers/)), and of the channels that crossed 1,000, 68% had 40 or more videos, which at his cadence is about month 18 ([vidIQ, 9 Jun 2025](https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers/); A9 rows 5 and 6; vendor data). Once inside, the Health & Sport median RPM is $1.23 ([AIR Media-Tech, 1 Jul 2026](https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm); A9 row 12; vendor, managed channels). At that rate the floor's $68,908.45 a year needs about 56.0 million views a year, or 2,154,736 an episode across 26 episodes, which is about 7,922 times the tenth-upload median of 272 (my arithmetic on A9 rows 1 and 12). Ads enter the model at zero.

### 4.3 · Brand deals: unsourced rate, unsourced timeline

**What is documented.** No filed unit gives a fee per deal, per follower or per view. What exists describes creators who already have deals, and it is thin. Of 783 European creators with 5,000 or more followers and at least one brand deal, 28% work full-time and 23% of the men earn under €500 a month; Portugal is not in the sample ([Kolsquare, 7 Jul 2025](https://www.kolsquare.com/en-gb/free-resources/voices-of-the-creator-economy-by-kolsquare-newtonx), A9 §8; vendor survey). €500 is 11.4% of the €4,370 floor (my arithmetic). More than half of 3,000-plus creators surveyed by Influencer Marketing Hub earn under $15,000 a year ([Influencer Marketing Hub, Aug 2025](https://influencermarketinghub.com/creator-earnings-report-2025/); A9 §8; vendor survey), which is €13,426.42 a year or €1,118.87 a month at the ECB rate above (my arithmetic). In Kajabi's survey of 1,717 creators, brand-deal revenue was reported down 52% ([Net Influencer, 17 Apr 2025](https://www.netinfluencer.com/creator-commerce-rises-as-platform-dependency-declines-kajabi-report-shows/); A2 §3; self-report on a course platform). Of the five comparables, Boyd has long-term partnerships through an agent and Sidibe the title of Gymshark Athlete; neither source gives a fee or a term (DD-A1 §3, §4).

**What applies before any deal.** The activity is opened before the first recurring payment (A8 R1); a gifted product is refused until its tax treatment is confirmed (A8 R9); every deal carries the platforms' labels and a spoken line (A8 R18).

**Timeline.** None sourced. The only follower threshold in the filed data on brand deals is Kolsquare's sampling floor of 5,000 followers, and no filed unit gives his follower counts (A7 a1). Brand deals enter the model as **B**, the monthly amount of signed deals, filled only from contracts.

### 4.4 · Shōmen margin: sourced revenue, no sourced margin

**What A7 found.** A7's model gives 2027 merch revenue of $388.00, $2,328.00 and $11,640.00 in its three scenarios, gross sales before any cost, and says that no filed unit gives Shōmen's costs, so none of it is profit yet (A7, Deliverable B, B2, a16 and B4). That holds here. Converted at $1.1172, the three are €347.30, €2,083.78 and €10,418.90 for the year, €28.94, €173.65 and €868.24 a month (my arithmetic). The rate under them, 0.40–1.20% of followers per drop and a $48.50 order, is VoxBooster's ([VoxBooster, 22 Aug 2026](https://voxbooster.com/blog/merch-sales-creator-statistics-2026)), which A9 called the weakest-sourced figure in its unit (A9 §7; A7 §1).

**What else comes off.** On sales of goods, social security takes 4.28% of the sale value (§1). Above €15,000 of turnover a year the IVA exemption ends (A8 R6), so part of every order is IVA. Whether Shōmen's sales are his turnover at all depends on its legal form, which is open (A8 R10).

**Timeline.** Drops on 4 March and 16 September 2027; his own conversion replaces VoxBooster's from the read of 18 May 2027 (A7, Deliverable A, part 4; B4). The margin can be known only once A8 R10 is settled and the first drop's costs are counted. Until then the margin enters as **m**, unfilled, and the deliverable tests the extreme m = 100% to show the earliest date the revenue alone could support.

### 4.5 · Consulting or fractional product work: no figure in any source

**What is documented.** No filed unit gives a day rate, a retainer, a time to a first client or a share of people who find one, and no source meeting the standard was opened for them. The line enters as **K**, monthly contracted income net of its costs, filled only from signed contracts.

**What the filed units do set.** Service income is category B, under a coefficient of 0.75 if his activity code is on the art. 151.º list and 0.35 otherwise, aggregated with salary while he is employed (A8 §1, R3, R5); social security is 14.98% of it after an exit (§1). The employment contract is read against A8 §4's checklist before any paid work, and three of its items bear directly on paid work in his own field: exclusivity or outside work (item 1), conflicts of interest (item 2) and any post-employment non-compete (item 6). The Código do Trabalho's duty of loyalty bars negotiating "em concorrência" with the employer (art. 128.º, n.º 1, al. f), A8 §4). A8 found the channel itself clear of that limb on the plain words; whether consulting would be depends on the contract and on the employer's business, which no filed unit states and this unit does not.

**Hours.** None are free for it. Publishing takes 6.25–6.75 hours a week and the half-marathon block about 2.5–4.5 more, 8.75–11.25 hours before karate, coaching, SC Braga, Shōmen and the history course (A8 §11). Consulting while employed would come out of those or out of rest.

**Timeline.** None sourced.

### 4.6 · Courses: a figure exists and fails the standard

Teachery's guidance is to expect "about 2-3% of your email audience to purchase your mini-course", per offer, with no dataset ([Teachery](https://make500.teachery.co/lessons/part-2-managing-expectations)); A9 §7 kept it out of its deliverable as below the standard, and so does this one. For scale only: on A7's highest list, 8,314, that would be 166 to 249 buyers per offer (my arithmetic), and no filed unit gives a price. Kajabi's creators reported digital-download sales up 20% and educational content up 14% (Net Influencer, 17 Apr 2025, above; A2 §3; self-report). The one documented course is Abdaal's: the first cohort of his Part-Time YouTuber Academy ran in November 2020, about 41 months after his first medical video, when he had passed one million subscribers, and a third-party summary of his own video gives it £220,000 ([Summify, video of 28 Dec 2020](https://summify.io/discover/how-much-money-i-earn-as-a-doctor-youtuber-VTTp5A/); DD-A1 §2; survivor, third-party summary). Courses enter as **Q**, unfilled, with no sourced timeline.

### 4.7 · What the mix can reach on sourced numbers

Set the sourced lines against the floor. A7's three scenarios for 2027, all lines together and the merch line gross, are 0.6%, 4.0% and 21.9% of the year's €55,880 floor (€347.30, €2,237.92 and €12,233.19 a year, or €28.94, €186.49 and €1,019.43 a month; my arithmetic). Entering 2028, A7's High case has a paid-tier run rate of $14,630 a year gross (A7, table B2), which after fees is $14,630 − $1,989.68 − $478.80 = $12,161.52, or €907.14 a month: 17.6% of the €5,139.97 target. Its merch line runs at €868.24 a month gross, 19.9% of the €4,370 floor at a margin of 100%.

```viz
{"kind": "compare", "title": "Side income against the floor, euros a month",
 "max": 5500, "decimals": 2,
 "rows": [
  {"label": "Target before IRS (T), sole earner", "value": 5139.97, "display": "€5,139.97", "tone": 1},
  {"label": "Survivable floor from Sep 2027", "value": 4370, "display": "€4,370", "tone": 4},
  {"label": "A7 High, 2027", "value": 1019.43, "display": "€1,019.43", "tone": 3},
  {"label": "A7 Base, 2027", "value": 186.49, "display": "€186.49", "tone": 3},
  {"label": "A7 Low, 2027", "value": 28.94, "display": "€28.94", "tone": 3}
 ],
 "caption": "§1 and §4.7: the sole-earner floor from September 2027 and the side income that replaces it before IRS, against A7's three 2027 scenarios a month (A7, Deliverable B, B2: $13,666.92, $2,500.20, $388.00 a year, merch gross before costs), converted at the <a href=\"https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.it.html\">ECB reference rate of $1.1172 per euro, 30 Oct 2026</a>. Floor from the brief; the target and conversions are this unit's arithmetic."}
```

The gap between the sourced lines and the target is what B, K and Q would have to fill, and those are the three lines with no sourced rate. Any mix that reaches the floor early does so on numbers no source gives.

## 5 · Against A7, A9, A2 and DD-A1

**A7, Deliverable B.** The three totals ($388.00, $2,500.20, $13,666.92) recompute exactly, and so do the paid-tier lines (Base: 50 member-months × $52 ÷ 12 = $216.67, fees $29.47 and $15.00; High: 266 × $110 ÷ 12 = $2,438.33, fees $331.61 and $79.80). Merch is 93.1% of Base and 85.2% of High, as A7 B4 says. A7's treatment of the margin stands and is carried into this model: merch enters as revenue times an unfilled m, and nothing in the model treats it as profit. One addition: A8 §2 left open whether A7's totals cross €15,000. At the ECB rate of 30 October 2026, the High total is €12,233.19, and across the range the ECB page shows from July to October 2026 ($1.1130 to $1.1699) it is €11,682.13 to €12,279.35, under €15,000 throughout (my arithmetic). Whose turnover it is stays open (A8 R10).

**A9 §8, the expectation sheet and the checkpoints.** This unit agrees with all three and depends on them. The model reads only on A9's checkpoint dates as A3 shifts them (A3 §5), which continue every 91 days: 16 February, 18 May, 17 August and 16 November 2027, 15 February 2028, and A9's two-year review of 31 October 2028 falls on Tuesday 14 November 2028 (my arithmetic). A9 §8's plateau bears on Path A by analogy: on YouTube, median monthly subscriber growth falls with size at every band (vidIQ, vendor data), and A9 says the median rates describe no actual path to a large audience. No filed unit measures how list growth changes with size. Path A's list grows linearly at an anecdote's pace for four years, so it is the optimistic case, and A9's plateau is the reason to read its date as the earliest possible.

**A2 §3.** No source measures the share of viewers or followers who join a list; the platform's network is the only measured source of subscribers (Substack's claim of 50% of new subscriptions, [On Substack, 22 Feb 2024](https://on.substack.com/p/substacks-recommendations-network); platform claim). So the list growth that Path A needs cannot be derived from channel numbers; it is read directly, as list size, at every checkpoint (A9 read 7).

**DD-A1.** The five histories document monetisation only for Abdaal in amounts (third-party summaries), and none dates the month at which creator income first covered the creator's household costs. Two show another income carrying the early years: Abdaal's work as a junior doctor from 2018 to 2020, and Boyd's partner working full-time elsewhere until the channel could pay them both (DD-A1, pattern 3). DD-A1's line "Keep the job; the comparables that document income kept another source of it through the early years" is consistent with this model, which makes continued employment the state every path starts from and returns to.

## Deliverable · Threshold model: three paths and the earliest honest date on each

Version 1, 2 November 2026. Euros unless marked; dollars converted at $1.1172 per euro (ECB, 30 Oct 2026). Every row names its source or its label; **(his rule)** marks a convention set in this unit; **unfilled** marks an input he enters and no source gives. The arithmetic was run by script on 2 November 2026. The model is read at A9's checkpoints and at no other time.

### D1 · Inputs

| # | Input | Value used | Source, or label |
|---|---|---|---|
| i1 | Household take-home | €4,800 a month | Brief |
| i2 | Current margin | ≈ €0, read as outgoings of €4,800 | Brief |
| i3 | Car credit | €430 a month to August 2027 | Brief |
| i4 | Outgoings from September 2027 | €4,370 | i1 − i3, my arithmetic; assumes the €430 is not re-spent (his assumption, to confirm) |
| i5 | V_min: second earner's lowest month in the last twelve, household share | 0 | Unfilled; no figure in the brief or any filed unit. 0 is the sole-earner case the brief asks about |
| i6 | C: cuts agreed in writing if the salary stops | 0 | Unfilled |
| i7 | S0: savings available for the runway today | 0 | Unfilled; no filed unit gives savings; the brief's margin of zero |
| i8 | Runway | 12 months of F_s (6 as sensitivity) | **His rule**; basis: CGD, 9 Apr 2026 (bank guidance, no dataset: at least six months, at least a year); ISS guide 6001 v4.72 (no benefit after a resignation) |
| i9 | Social security on service income after an exit | 21.4% × 70% = 14.98% | DL 2/2018, CRC arts. 162.º, 168.º (A8 §3); employee exemption lapses with the job (gov.pt, A8 §3) |
| i10 | Social security on sales of goods | 21.4% × 20% = 4.28% | Same |
| i11 | IRS on side income | Not modelled | Unfilled; brackets not opened in A8 §1; the accountant's figure |
| i12 | Exchange rate | $1.1172 per euro | ECB reference rate, 30 Oct 2026, read 2 Nov 2026 |
| i13 | Paid share of the list | 1.6% (0.9% and 5% as sensitivities) | Generalist World via beehiiv; Artificial Ignorance (documented cases); Substack's claim, no dataset (A9 §7; A7 a9) |
| i14 | Price per member | $110 a year ($52 as sensitivity) | Patreon State of Create via Net Influencer, company-sponsored; used as prices (A7 a11) |
| i15 | Paid-tier fees | 13.6% + $0.30 per monthly payment | Substack Support, updated 29 Sep 2026 (A7 a12) |
| i16 | List growth | 14,000 a year (8,314; 2,000; 833 as sensitivities) | Amy Suto, 42,000 in three years (anecdote); beehiiv year-one median (platform-published, self-selected); The Creator's Playbook and The Introverted Networker (anecdotes) (A9 §6, row 13) |
| i17 | List shape | Linear from 0 on 5 Nov 2026; members = paid share × list each month; no churn | **His assumption**, following A7 a7; no filed unit gives a churn rate, so no churn favours an early date |
| i18 | Tier opening | 1 Sep 2027 if the list is ≥ 1,000 on 17 Aug 2027 | A7 a8 |
| i19 | Average order | $48.50 = €43.41 | VoxBooster, weakly sourced (A7 a4) |
| i20 | Orders per drop ÷ followers | 1.20% (0.40% as sensitivity) | VoxBooster, weakly sourced (A7 a2) |
| i21 | Followers on drop day | 10,000 in 2027, A7's High | **His assumption** (A7 a1) |
| i22 | Follower growth from 2028 | 22.0% a year | [Socialinsider, Instagram benchmarks, updated 22 Oct 2026](https://www.socialinsider.io/instagram-benchmarks), brand accounts at 1,000–5,000, 2025 (vendor; A7 §1) |
| i23 | Drops | 4 March and 16 September each year | A7, Deliverable A, part 4 (2027); repeated yearly, **his assumption** |
| i24 | m: Shōmen margin after costs and IVA | Unfilled; 100% used only as the upper bound | A7 a16; A8 R6, R10 |
| i25 | B: signed brand deals, a month | Unfilled | No sourced rate (§4.3) |
| i26 | K: contracted consulting or fractional work, a month | Unfilled | No sourced rate (§4.5) |
| i27 | Q: course income, a month | Unfilled | Only figure below the standard (§4.6) |
| i28 | YouTube ads | 0 | A9 rows 11–12 (§4.2) |
| i29 | Checkpoints | Every 91 days from Tue 16 Feb 2027 | A9, Deliverable 2, on A3 §5's dates; later dates my arithmetic |
| i30 | Pass rule | Side income over the trailing twelve full months ≥ 12 × T, at two checkpoints running | **His rule**; basis: A9's fixed-date reads; A7 Deliverable A, part 7 (a trigger must hold twice) |

### D2 · The thresholds, line by line

1. Floor from September 2027: F = €4,800 − €430 = **€4,370**.
2. Survivable floor: F_s = F − C − V_min = €4,370 − 0 − 0 = **€4,370**.
3. Social security share on services: 0.214 × 0.70 = 0.1498.
4. **Income threshold** T = F_s ÷ (1 − 0.1498) = €4,370 ÷ 0.8502 = **€5,139.97 a month**, **€61,679.60 a year**, before IRS. For goods: €4,370 ÷ (1 − 0.0428) = €4,565.40 a month, €54,784.79 a year of margin.
5. **Runway threshold** = 12 × F_s = 12 × €4,370 = **€52,440** (six months: €26,220).
6. Months to runway = (€52,440 − S0) ÷ (€430 + C) = €52,440 ÷ €430 = 121.95, so 122 months from September 2027: complete in October 2037, first read **Tue 3 Nov 2037**. Six months: €26,220 ÷ €430 = 60.98, so 61 months: September 2032, first read Tue 9 Nov 2032.
7. Each €1,000 of S0: 2.33 months earlier. Each €100 of C: F_s down €100, saving up €100 a month, T down €117.62.
8. **The rule.** An exit may be considered at the first checkpoint at which (a) side income has met T over the trailing twelve months at that checkpoint and the one before, (b) the runway is saved, and (c) A8 R1 (activity opened) and R13 (contract read, notice given where needed) are done. Until all three hold, the state is the present one: employed, building, read next quarter.

```viz
{"kind": "decision",
 "caption": "Deliverable, D2 line 8, drawn: the exit rule at each checkpoint. T is €5,139.97 a month and the runway €52,440 at the defaults (sole earner, no cuts, no savings; D2 lines 4–5). The thresholds are this unit's arithmetic on the brief's figures and DL 2/2018 (A8 §3); the runway length is his rule on CGD's guidance (9 Apr 2026); R1 and R13 are A8's register.",
 "root": {"q": "Side income ≥ T over the trailing 12 months, at this checkpoint and the last?", "tone": 4, "branches": [
  {"label": "no", "to": {"outcome": "Stay employed; keep building; read again next quarter", "tone": 2}},
  {"label": "yes", "to": {"q": "Runway of 12 × the survivable floor saved?", "tone": 4, "branches": [
   {"label": "no", "to": {"outcome": "Stay employed; bank side income until it is", "tone": 2}},
   {"label": "yes", "to": {"q": "Activity opened (A8 R1) and contract read (A8 R13)?", "tone": 4, "branches": [
    {"label": "no", "to": {"outcome": "Do those first", "tone": 3}},
    {"label": "yes", "to": {"outcome": "An exit can be considered; the model does not decide it", "tone": 1}}
   ]}}
  ]}}
 ]}}
```

### D3 · Path A · The audience pays: the paid tier carries the floor

**Arithmetic.**

1. Net per member: $110 − 13.6% ($14.96) − 12 × $0.30 ($3.60) = $91.44 a year = €81.85 = €6.82 a month.
2. T in dollars: €61,679.60 × 1.1172 = $68,908.45.
3. Members: $68,908.45 ÷ $91.44 = 753.6, so **754**.
4. List: 754 ÷ 1.6% = **47,125**.
5. At 14,000 a year from 5 Nov 2026 the list is 10,924 on 17 Aug 2027, so the tier opens on 1 Sep 2027 (i18), and reaches 47,125 after 47,125 ÷ 14,000 = 3.37 years, in March 2030.
6. Members follow the list (i17), so the trailing twelve months' net receipts are €60,075.41 at the checkpoint of 13 Aug 2030 (short), €64,655.73 at 12 Nov 2030 and €69,236.06 at 11 Feb 2031 (both ≥ €61,679.60).
7. Runway: salary saving from September 2027 to January 2031 is 41 months × €430 = €17,630. Tier receipts over the same months are €160,909.41 before IRS; keeping 21.6% of them closes the gap to €52,440.

**Earliest honest date: Tuesday 11 February 2031**, at Suto's pace.

| Test | Earliest date |
|---|---|
| As modelled: 1.6%, $110, 14,000 a year | Tue 11 Feb 2031 |
| beehiiv's year-one median, 8,314 a year | Tue 10 May 2033 |
| 0.9% (Artificial Ignorance), 14,000 a year | Tue 9 Aug 2033 |
| 0.9%, 8,314 a year | Tue 3 Nov 2037 |
| $52 a member (Patreon's per-fan figure), 14,000 a year | Tue 6 Feb 2035 |
| 5% (Substack's claim, no dataset), 14,000 a year | Tue 13 Feb 2029 |
| 1.6% at the part-time paces, 2,000 or 833 a year | List takes about 24 or 57 years; no date inside any horizon |

Each €100 a month of B, K or Q he can show from contracts lowers the members needed by 14.66 and the list by 916.

**What has to be true.**

1. The list grows at about 14,000 a year for four years, 1.7 times beehiiv's median and seven times the faster part-time case (A9 row 13; my division), with no slowdown, against A9 §8's evidence that growth slows with size.
2. 1.6% of the list pays, the higher of the two documented cases, at $110 a year, with no churn.
3. The list is grown by a channel run inside 5–7 hours a week, a pace no case in DD-A1 documents (DD-A1, deliverable: none grew on 5–7 hours of one person's work).
4. The checkpoints of 12 Nov 2030 and 11 Feb 2031 both read trailing receipts at or above T, and the runway and R1 and R13 are done by the second.

### D4 · Path B · The brand pays: Shōmen's margin carries the floor

**Arithmetic.**

1. Average order: $48.50 ÷ 1.1172 = €43.41.
2. Sales needed a year: €52,440 ÷ (m − 0.0428). At the upper bound m = 100%: €52,440 ÷ 0.9572 = **€54,784.79**.
3. Orders: €54,784.79 ÷ €43.41 = 1,262 a year, **631 per drop**.
4. Followers on drop day at 1.20%: 631 ÷ 0.012 = **52,584** (at 0.40%: 157,750).
5. From 10,000 in 2027 at 22.0% a year: ln(52,584 ÷ 10,000) ÷ ln(1.22) = 8.35 years, about May 2036.
6. The drops of March and September 2036 bring €55,927.04 of sales, €55,927.04 × 0.9572 = €53,533.36 after social security on goods, at or above €52,440. The trailing twelve months first contain both at the checkpoint of 4 Nov 2036, and again at 3 Feb 2037; at 5 Aug 2036 they hold the September 2035 and March 2036 drops, €48,439.87 after social security (short).
7. Runway: salary saving to January 2037 is 113 months × €430 = €48,590; banking 7.2% of the last twelve months' margin closes the gap.

**Earliest honest date: Tuesday 3 February 2037, and only at a margin of 100%**, which no business has: the date is a bound that the real margin can only push later.

| Test | Earliest date |
|---|---|
| m = 100%, 1.20% per drop | Tue 3 Feb 2037 |
| m = 50% (110,167 followers on drop day) | Tue 29 Jan 2041 |
| m = 100%, 0.40% per drop | Tue 29 Jul 2042 |

**What has to be true.**

1. Shōmen's own conversion reaches VoxBooster's top rate, a weakly sourced figure, at every drop for nine years; A7's override needs it to do so only twice (A7, Deliverable A, part 7).
2. The accounts that announce a drop hold 10,000 followers in 2027 and grow at a brand-account rate measured for accounts of 1,000–5,000, past 50,000.
3. A margin exists and is known: A8 R10 settled, costs counted, IVA paid from the price above €15,000 of turnover (A8 R6).
4. Two drops a year, each about 631 orders, are run in Shōmen's time, which sits outside the 5–7 hours (A7 §2).

### D5 · Path C · The skill pays: contracted work carries the floor

**Arithmetic.**

1. Income test: K + B + Q + tier + m × merch ≥ €5,139.97 a month over the trailing twelve months at two checkpoints running, with K billed as services (14.98% social security after an exit, i9).
2. While employed, service income stays exempt from social security below €2,148.52 of relevant income a month, about €3,069 of gross service income, if A8 R11's conditions hold (A8 §3); the exemption ends with the job.
3. Runway: (€52,440 − S0) ÷ (€430 + C + k), where k is consulting income banked after tax while employed. At k = 0: 122 months, complete October 2037, read **Tue 3 Nov 2037**.

**Earliest honest date: none from the research.** No source in the filed units or opened here gives a rate, a time to a first contract or the share of people who find one, so the income test cannot be dated. The only dated bound is the runway at k = 0: Tuesday 3 November 2037, or Tuesday 9 November 2032 on a six-month runway. Once K is a signed monthly figure, lines 1 and 3 give the date by the same arithmetic.

**What has to be true.**

1. The contract permits paid work in his field, or he gives the notice it requires and keeps the reply (A8 §4, items 1, 2 and 6; R13).
2. Signed, recurring contracts, read as at least two quarters of receipts, cover T on their own or with the sourced lines.
3. The hours exist: A8 §11 already has 8.75–11.25 hours a week of publishing and running before karate, coaching, SC Braga, Shōmen and the history course.
4. The activity is opened before the first invoice (A8 R1), with the coefficient set by the accountant (A8 R3).

### D6 · The three dates together

```viz
{"kind": "timeline", "start": 2027, "end": 2038, "ticks": [2027, 2029, 2031, 2033, 2035, 2037],
 "events": [
  {"at": 2027, "date": "Aug 2027", "label": "Car credit ends; saving can start", "tone": 4},
  {"at": 2028, "date": "14 Nov 2028", "label": "A9 two-year review", "tone": 6},
  {"at": 2031, "date": "11 Feb 2031", "label": "Path A: tier carries the floor", "tone": 1},
  {"at": 2032, "date": "9 Nov 2032", "label": "Six-month runway, zero savings", "tone": 2},
  {"at": 2037, "date": "3 Feb 2037", "label": "Path B, at 100% margin", "tone": 3},
  {"at": 2037, "date": "3 Nov 2037", "label": "Path C bound: twelve-month runway", "tone": 5}
 ],
 "caption": "Deliverable, D3 to D5: the earliest honest date on each path, with the end of the car credit (brief), A9's two-year review on A3's dates, and the runway dates at zero savings. Path A at Amy Suto's list growth (anecdote) and the 1.6% paid share (documented case); Path B at VoxBooster's weakly sourced top rate and an impossible 100% margin; Path C has no sourced income date, so its date is the runway's. Dates are this unit's arithmetic on the filed figures."}
```

**Read together.**

- On the sourced numbers, Path A is the only route with a date inside a decade, and that date rests on an anecdote's growth rate held for four years. At the strongest-sourced growth figure, beehiiv's median, it moves to May 2033.
- Path B cannot be dated until Shōmen has a margin; the revenue alone, at a margin no business has, gives February 2037.
- Path C, and brand deals and courses inside any mix, depend on figures no source gives. Every €100 a month of them that he can show from contracts lowers the list Path A needs by 916.
- At zero savings, the runway is the binding date on Path C; on Paths A and B the income test binds, and banked receipts pay for the runway. Entering S0, C and V_min is the first act of the model; each one moves every date.

**When it is read.** At every A9 checkpoint, in the same sitting as the seven reads, with S0, C, V_min and the paid-tier, merch and contract figures updated, and the result written into the record. The first reading is Tuesday 16 February 2027, when the inputs he enters replace the defaults. Under the pass rule (i30), no path can pass before twelve months of side income stand behind two checkpoints running.

## Sources

- AIR Media-Tech, "Which YouTube niche makes the most money in 2026, ranked by real RPM and CPM", 1 Jul 2026, as cited in A9 §6. https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm
- Amy Suto, "How to grow a Substack", 4 Jul 2026, as cited in A9 §6. https://www.amysuto.com/desk-of-amy-suto/how-to-grow-a-substack
- Artificial Ignorance, "Two years of Artificial Ignorance", 11 Feb 2025, as cited in A9 §7. https://www.ignorance.ai/p/two-years-of-artificial-ignorance
- beehiiv, "The State of Newsletters 2026", 6 Jan 2026, as cited in A9 §6–7. https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md
- Caixa Geral de Depósitos, Saldo Positivo, "Constituir um fundo de emergência: poupe para uma urgência", 9 Apr 2026, read 2 Nov 2026. https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx
- Decreto-Lei 2/2018 (Código dos Regimes Contributivos, arts. 162.º and 168.º), Segurança Social site, as cited in A8 §3. https://seg-social.pt/documents/10152/15523435/DL_2_2018/9a9cffcd-29c6-44a4-b1fc-72c5aceedcd6
- European Central Bank, euro foreign exchange reference rates, US dollar, rate of 30 Oct 2026, read 2 Nov 2026. https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.it.html
- gov.pt, "Pedir a isenção do pagamento de contribuições para a Segurança Social", updated 3 Sep 2026, as cited in A8 §3. https://www.gov.pt/servicos/requerer-a-isencao-do-pagamento-de-contribuicoes-para-a-seguranca-social
- Influencer Marketing Hub, "Creator Earnings Report 2025", Aug 2025, as cited in A9 §8. https://influencermarketinghub.com/creator-earnings-report-2025/
- Instituto da Segurança Social, *Guia prático: subsídio de desemprego* (6001 v4.72), 20 Feb 2025, read 2 Nov 2026. https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b
- Kolsquare × NewtonX, "Voices of the Creator Economy", 7 Jul 2025, as cited in A9 §8. https://www.kolsquare.com/en-gb/free-resources/voices-of-the-creator-economy-by-kolsquare-newtonx
- Net Influencer, Kajabi creator commerce report summary, 17 Apr 2025, as cited in A2 §3. https://www.netinfluencer.com/creator-commerce-rises-as-platform-dependency-declines-kajabi-report-shows/
- Net Influencer, Patreon State of Create 2025 summary, 21 Feb 2025, as cited in A7 §1 and A9 §7. https://www.netinfluencer.com/patreon-2025-state-of-create-report-how-creators-are-breaking-free-from-platform-control/
- On Substack, "Substack's recommendations network", 22 Feb 2024, as cited in A2 §3. https://on.substack.com/p/substacks-recommendations-network
- Socialinsider, Instagram benchmarks, updated 22 Oct 2026, as cited in A7 §1. https://www.socialinsider.io/instagram-benchmarks
- Substack Support, "How much does Substack cost?", updated 29 Sep 2026, as cited in A7 a12. https://support.substack.com/hc/en-us/articles/360037607131-How-much-does-Substack-cost
- Summify, summary of Ali Abdaal, "How much money I earn as a doctor & YouTuber" (video of 28 Dec 2020; third-party summary), as cited in DD-A1 §2. https://summify.io/discover/how-much-money-i-earn-as-a-doctor-youtuber-VTTp5A/
- Teachery, "Make $500, Part 2: Managing expectations", as cited in A9 §7. https://make500.teachery.co/lessons/part-2-managing-expectations
- The Creator's Playbook (Mark Wils), "Celebrating 1 year on Substack", 30 Jul 2025, as cited in A9 §6. https://thecreatorplaybook.substack.com/p/celebrating-1-year-on-substack
- The Introverted Networker, "How I grew my newsletter to 2,500", charts as of 28 May 2025, as cited in A9 §6. https://theintrovertednetworker.substack.com/p/how-i-grew-my-newsletter-to-2500
- vidIQ Research, "Uploads and reaching 1,000 subscribers", 11 Sep 2026, as cited in A9 §3. https://vidiq.com/research/youtube-uploads-1000-subscribers/
- vidIQ, "How many videos to get 1,000 subscribers", 9 Jun 2025, as cited in A9 §3. https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers/
- VoxBooster, "Merch sales creator statistics 2026", 22 Aug 2026, as cited in A7 §1 (weakly sourced). https://voxbooster.com/blog/merch-sales-creator-statistics-2026
- YouTube Help, "Changes to the YouTube Partner Program" (answer 12843009), as cited in A9 §6. https://support.google.com/youtube/answer/12843009?hl=en
- Filed units cited by section: A2 (§3); A3 (§5); A7 (§1, §2, Deliverable A part 4 and part 7, Deliverable B: B1 a1–a12, a16, B2, B4); A8 (§1, §2, §3, §4, §11; register R1, R3, R5, R6, R9, R10, R11, R13, R18); A9 (§6, §7, §8; Deliverable 1 rows 1, 5, 6, 11, 12, 13; Deliverable 2); DD-A1 (§2, §3, §4; deliverable, pattern 3).

## Writer's unsure list

1. Whether the brief's €4,800 take-home is the household's or his alone, and so whether the second earner's income is inside it; the model's F_s = outgoings − C − V_min covers both readings, but the reader has to say which holds.
2. The ECB rate of $1.1172 on 30 October 2026 and the July–October range ($1.1130 to $1.1699) come from the fetch tool's reading of the ECB's Italian-language US dollar page; the table's date was read as "30" in the October 2026 table.
3. The ISS guide (v4.72, 20 February 2025) was read through the fetch tool; whether a later version changes the voluntary-unemployment rule or the cap was not checked. The gov.pt service page for the benefit failed at its site and was not opened.
4. CGD's six-months-to-a-year guidance is a bank's consumer advice without a dataset; no source meeting the standard was found for the runway length, so twelve months is his rule.
5. Social security on side income after an exit uses the 2018 regime's 21.4% on 70% (services) and 20% (goods) as A8 §3 gives it; whether a first-year exemption or another regime applies to a newly independent worker was not checked here (A8 R12 is open on enrolment timing).
6. IRS is not modelled; every threshold is before income tax, so every date in the deliverable is earlier than the true one by an amount the accountant sets.
7. Path A treats members as an instant 1.6% of the list with no churn, and the list as linear at Amy Suto's pace for four years; both favour an early date, and Suto's figure is an anecdote.
8. Path B repeats A7's two drop dates every year and applies Socialinsider's 22.0% growth (brand accounts at 1,000–5,000 in 2025) to accounts far above that tier for nine years.
9. The €430 freed in September 2027 is assumed to be saved in full; nothing in the brief says it will be.
10. Whether consulting in his field would touch the competition limb of the duty of loyalty depends on the contract and the employer's business, neither of which is in any filed unit; the unit states no view on it.
