---
audit: fresh check
unit: PB8 · Voice, disclosure and the rules
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB8 is owed to the Fable stage (P49)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB7/W-PB8 chat (which ran on Opus 5.5 and only staged, applied, filed and published) in session https://claude.ai/code/session_01KMmgQyAmFapUaWMYDKogYn
verdict: fix · 2 errors, 6 should-fix, 8 minor
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/report.md`), copied unchanged. Saved before any finding was applied.

Model: claude-opus-5-5

# PB8 · Voice, disclosure and the rules: fresh check

Checker: a fresh agent that did not see the unit being written. Read: unit.md, unsure.md, brief.txt, sourcing.md (Parts 1 and 5), case-facts.md, notes.md, figure-kinds.txt, units/PB1–PB7. No audit report was read. Live search on 13 Nov 2026; WebFetch was used only on URLs returned by a WebSearch in this run. Every Current below was checked with Python `str.count` and occurs exactly once in unit.md.

Side note, not a finding: notes.md says a "Model:" line was placed under the front matter of unit.md. unit.md has no such line. The front matter's `model: Opus 5.5` field is all there is.

## (1) Coverage

| Brief item | Verdict |
|---|---|
| Honesty as register vs confession as content, with a documented case of each | covered (Tom Scott; Elle Mills; Haushofer as the bridge case) |
| Studies on trust in creators: what they found and did not find | covered, thin: one correlational survey (Frontiers 2026) plus one meta-analysis on sponsorship disclosure. The limits are stated. |
| Audience entanglement and creator burnout, with the guardrails reported | covered (Pillemer et al. via PsyPost; Nguyen and Duffy via Cornell Chronicle) |
| What a disclosure policy decides (self, health, family, employer, others in frame) | covered (§4) |
| A truthful public record, with corrections | covered (§5) |
| Ad disclosure: FTC; ASA and CMA; EU UCPD and the national regulator; the platforms' tools | covered (§6.1). The DFA status is stale (see findings). |
| Other people's image, and children's | covered (§6.2) |
| Music and third-party footage under each platform's rules | covered for YouTube. Thin for Instagram: the licensed-library page did not load, and the unit says so. |
| Employment contract checks | covered (§6.4, seven-item checklist) |
| Registering and declaring income, as a question, for EU, UK and US | covered (§6.5) |
| Data protection for an email list | covered (§6.6) |
| The trademark check PB2 left open | covered (§6.7; register M1, M2) |
| Information, not advice; which lines need a professional | covered (intro; §7) |
| Deliverable: ten-clause policy, pre-mortem two years on, constraints register with all required columns, then templates | covered (D1 has 10 clauses; D2 is set in Jan 2029 with 9 causes; D3 has 23 lines; templates T1–T3) |

## (2)–(6), (9), (10) Findings

[error] [figure] §3 viz 1 (states); Current: {"id": "fun", "label": "Functional entanglement", "note": "balanced dependence", "tone": 3}; Problem: the note "balanced dependence" appears nowhere in the unit's text. It is PsyPost's wording and never reached §3, so the figure adds a fact. Fix: {"id": "fun", "label": "Functional entanglement", "tone": 3}; Basis: unit §3 text; the checker prompt, item 7 (https://www.psypost.org/new-study-sheds-light-on-the-psychological-burden-of-having-a-massive-social-media-audience/).

[error] [figure] §3 viz 1 (states); Current: {"from": "audience", "to": "dys", "label": "usually begins"}; Problem: §3 says only that after a large audience arrives the creators described a dysfunctional entanglement. "Usually" is not in the text, and the unit gives no frequency. Fix: {"from": "audience", "to": "dys", "label": "begins"}; Basis: unit §3 text; PsyPost, 20 Feb 2026 (https://www.psypost.org/new-study-sheds-light-on-the-psychological-burden-of-having-a-massive-social-media-audience/).

[should-fix] [accuracy] §6.1 EU; Current: Its status on 13 November 2026 was not confirmed.; Problem: the status can be confirmed. Reuters reported that the proposal would be presented on Wednesday 11 Nov 2026, and two reports dated 11 and 12 Nov 2026 say the Commission presented it that day. Unsure item 3 is resolved. The two new links also go into Sources. Fix: On 11 November 2026 the Commission presented its Digital Fairness Act proposal, which press reports say includes rules on paid influencer promotion; it still has to pass the European Parliament and the Council before it is law ([ecommercenews.eu, 12 Nov 2026](https://ecommercenews.eu/eu-targets-online-sales-tricks-with-digital-fairness-act/); [CEA Digilaw, 11 Nov 2026](https://ceadigilaw.org/en/blog/digital-fairness-act-addictive-design-pricing/); secondary). Its text was not read for this unit.; Basis: https://ecommercenews.eu/eu-targets-online-sales-tricks-with-digital-fairness-act/ ("presented yesterday", 12 Nov 2026; "Consumers should know when influencers are being paid to promote products"); https://ceadigilaw.org/en/blog/digital-fairness-act-addictive-design-pricing/ ("On 11 November 2026 the European Commission presents its Digital Fairness Act proposal"); https://www.thestar.com.my/tech/tech-news/2026/11/10/companies-risk-fines-of-6-global-turnover-for-unfair-digital-trade-practices-eu-draft-law-shows (Reuters, to be presented 11 Nov).

[should-fix] [accuracy] §6.4 United States; Current: New York, as one example, protects "legal recreational activities"; Problem: the statute defines "recreational activities" as leisure-time activity "for which the employee receives no compensation". An account that earns may therefore fall outside the protection, and the unit, by omitting this, reads as covering a creator's account. Fix: New York, as one example, protects "legal recreational activities" (defined as leisure-time activity "for which the employee receives no compensation", so an account that earns may fall outside it); Basis: N.Y. Labor Law §201-d(1)(b), https://www.nysenate.gov/legislation/laws/LAB/201-D.

[should-fix] [figure] §6.1 viz 2 (decision); Current: "q": "Did a brand give you anything (money, a product, a discount, commission), or is it your own product or your employer's?"; Problem: §6.1 quotes the FTC: a material connection includes "a personal, family, or employment relationship". The figure's "no" branch ends in "No ad label needed" for a brand owned by family or a friend, which contradicts the text the figure draws from. Fix: "q": "Did a brand give you anything (money, a product, a discount, commission), is it your own product or your employer's, or is the brand's owner family or a friend?"; Basis: unit §6.1; FTC, Disclosures 101 (https://ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers/).

[should-fix] [figure] Deliverable D3 viz 4 (matrix); Current: the block from ` "cols": ["Mara", "Tax professional", "Employment lawyer", "Trade mark attorney", "Platform"],` to the ` ],` that closes "legend" (unit.md lines 299–317, unique as one block). Problem: the caption says the figure is D3's owner and professional columns, but (a) it leaves out the lawyer that D3 sets for P1 ("lawyer if anyone objects") and P2 ("Lawyer before any change"); (b) it adds a "Platform" column ("label", "enforces") that is in neither column; (c) "if unclear" and "if a hit" leave out J2 ("if a clause reaches outside work") and M2 (a trade mark attorney before registering). Fix:
```
 "cols": ["Mara", "Tax professional", "Employment lawyer", "Trade mark attorney", "Lawyer"],
 "rows": [
  {"label": "Ad disclosure (A1–A3)", "tone": 4, "cells": ["owns", null, null, null, null]},
  {"label": "People in frame (P1–P3)", "tone": 4, "cells": ["owns", null, null, null, "on objection or change"]},
  {"label": "Music and footage (C1–C3)", "tone": 4, "cells": ["owns", null, null, null, null]},
  {"label": "Employment (J1–J3)", "tone": 4, "cells": ["owns", null, "if unclear", null, null]},
  {"label": "Income (T1–T3)", "tone": 4, "cells": ["owns", "answers", null, null, null]},
  {"label": "Email list (E1–E5)", "tone": 4, "cells": ["owns", null, null, null, null]},
  {"label": "Trademark (M1–M2)", "tone": 4, "cells": ["owns", null, null, "if a hit", null]},
  {"label": "Health and record (H1, R1)", "tone": 4, "cells": ["owns", null, null, null, null]}
 ],
 "legend": [
  {"mark": "owns", "means": "Mara acts on the line or chases it", "tone": 3},
  {"mark": "answers", "means": "a professional where she is taxed answers it before the first income", "tone": 2},
  {"mark": "if unclear", "means": "only if her contract's wording is unclear or a clause reaches work made outside it", "tone": 5},
  {"mark": "if a hit", "means": "if a search returns a close mark, and before she registers", "tone": 5},
  {"mark": "on objection or change", "means": "if anyone in frame objects, or before any child appears", "tone": 5}
 ],
```
Basis: unit D3 rows P1, P2, J2, M1, M2.

[should-fix] [style] D3 lead-in (item 10, persona); Current: no time for these lines is in PB4's run-in hours (see notes); Problem: "notes" are the writer's working notes, which a reader of this public course cannot open. Fix: no time for these lines is in PB4's run-in hours, and where they go in her log is left to PB10's review; Basis: brief ("never refer to the private course or its units, which a reader of this course cannot open"); notes.md, Needs (PB4, PB10).

[should-fix] [style] D3 line M1 (item 10, persona); Current: result not stated here, since no writing chat can run a register search; Problem: "writing chat" is production jargon from the course's own workflow. The reader persona does not know what it is. Fix: result not stated here: she runs the search herself on the date set and writes its date and result into this line; Basis: brief (reader persona; the course is written to be shared with anyone).

[minor] [figure] §6.1 EU; Current: In a coordinated check of 572 influencers' posts; Problem: SCL gives 572, while other reports of the same Commission sweep give 576 (unsure item 1). The unit gives one count as settled. Fix: In a coordinated check of the posts of 572 influencers (SCL's count; other reports of the same sweep give 576); Basis: SCL, 20 Feb 2024 (https://www.scl.org/european-commission-and-consumer-authorities-investigate-online-influencers/: "a sweep of social media posts by 572 influencers"); CDE Universidad de Almería (https://www.cde.ual.es/en/only-1-in-5-influencers-consistently-disclose-their-advertising-content-on-social-media-says-new-commission-study/: "The posts of 576 influencers ... were checked").

[minor] [accuracy] §6.1 United States; Current: and US law applies to posts from abroad that will reasonably affect US consumers; Problem: this paraphrase changes the FTC's test, which is reasonable foreseeability. Fix: and "U.S. law applies if it's reasonably foreseeable that the post will affect U.S. consumers", including posts made from abroad; Basis: https://ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers/.

[minor] [accuracy] §5; Current: YouTube lets a creator trim the beginning, middle or end of a published video without re-uploading; Problem: the page says the trim is done "on a computer". This matters for clause 8, because Mara works only on her phone (PB5 §7), so a trim needs a computer she does not have. Fix: YouTube lets a creator trim the beginning, middle or end of a published video "on a computer", without re-uploading; Basis: YouTube Help 9057455 (https://support.google.com/youtube/answer/9057455: "You can cut out the beginning, middle, or end of your video on a computer").

[minor] [accuracy] §6.6 United Kingdom; Current: which inserted a new paragraph (3A) that was not read for this unit; Problem: what (3A) is can be established (unsure item 6). It is the charitable-purpose soft opt-in, in force from 5 Feb 2026, and does not bear on a creator's list. Fix: which inserted a new paragraph (3A), a soft opt-in for charities' marketing that does not reach a creator's own list ([Withers, "Soft opt-in now in force for UK charities"](https://www.withersworldwide.com/en-gb/insight/read/soft-opt-in-now-in-force-for-uk-charities); secondary); Basis: Withers: provisions "came into force on 5 February 2026"; s. 114 DUAA "inserting a new regulation 22(3A)".

[minor] [style] §6.1 EU; Current: [European Commission, Influencer Legal Hub, undated](https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/influencer-legal-hub_fr); Problem: the link goes to the French-language version for an English-language course, and the page does carry dates (legal briefs of 11 Oct 2023 and 13 Sep 2024). Fix: [European Commission, Influencer Legal Hub, legal briefs dated 11 Oct 2023 and 13 Sep 2024](https://commission.europa.eu/influencer-legal-hub_en); Basis: https://commission.europa.eu/influencer-legal-hub_en (quotes "in the eyes of European law they are categorised as traders" and "applies European and national consumer protection rules in practice" confirmed there).

[minor] [style] Sources; Current: - European Commission, Influencer Legal Hub (undated). https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/influencer-legal-hub_fr; Problem: same as above. Fix: - European Commission, Influencer Legal Hub (legal briefs dated 11 Oct 2023 and 13 Sep 2024). https://commission.europa.eu/influencer-legal-hub_en; Basis: https://commission.europa.eu/influencer-legal-hub_en.

[minor] [attribution] §1 Elle Mills; Current: and she gives as her biggest lesson that "not everyone deserves your vulnerability"; Problem: the quote is accurate and she does call it her biggest lesson, but in her video's narration she credits the line to her friend Tomska. Part 1 asks that a view be attached to the person who argued it. Fix: and she gives as her biggest lesson that "not everyone deserves your vulnerability", a line her video credits to her friend Tomska; Basis: https://creatorhub.patreon.com/articles/digital-spaghetti-elle-mills.

[minor] [deliverable] Template T1 clause 2; Current: Basis: [§4; your contract read under T3 line J1].; Problem: "T3" is both the template's name and the register's tax line T3 (Records), so a reader can follow the wrong pointer. Fix: Basis: [§4; your contract read under your register's line J1].; Basis: unit D3 line codes T1–T3 versus template headings T1–T3.

## Confirmed

- Tom Scott quotations, the author (James Hale), 2 Jan 2024, and "burnout" absent from the article: https://tubefilter.com/2024/01/02/tom-scott-youtube-break/
- Elle Mills: "Burnt out at 19" (2018); "very impulsive with even releasing"; "I took advantage of people's longings to be seen"; "I don't want my life to be the product anymore" is narration from *What Happened To Elle Mills?*; she calls "not everyone deserves your vulnerability" her biggest lesson; the article is undated: https://creatorhub.patreon.com/articles/digital-spaghetti-elle-mills
- Haushofer's reason sentence, "balance the record and provide some perspective", the Meta-Failures line, and the three section types: https://www.liverpool.ac.uk/media/livacuk/researcher/documents/Johannes_Haushofer_CV_of_Failures.pdf
- Frontiers study: authors, vol. 11, 5 Feb 2026, 407 women, 54.8%/45.2%, one focal influencer each, PLS-SEM, every coefficient and p value, R² 0.247/0.355, the limitation sentence, the trustworthiness items: https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2026.1723759/full
- Eisend et al.: 61 papers, 57 data sets, both quoted findings, JA 49(3) 344–366, DOI: https://research.wur.nl/en/publications/a-meta-analysis-of-the-effects-of-disclosing-sponsored-content/
- Audience entanglement: 54 creators, 74 interviews, ">500,000 followers", "nearly 280,000 subscribers", the two states, movement back and forth, the three strategies, the limits ("fitness, beauty, or gaming sectors"): https://www.psypost.org/new-study-sheds-light-on-the-psychological-burden-of-having-a-massive-social-media-audience/ ; ASQ 71(1) 215–260, online 18 Dec 2025, issue March 2026: https://metatoc.com/papers/129690-audience-entanglement-how-independent-creative-workers-experience-the-pressures-of-widespread-appeal-on-digital-platforms
- Nguyen and Duffy: NM&S 7 Jul 2026; 58/62/78; "unspeakable"; the full gratitude sentence; "blowback from audiences"; "One recurrent theme was, 'If I take a break…'"; both gender quotes; Duffy's question; Khanna's bill with no status given: https://news.cornell.edu/stories/2026/07/what-social-media-creators-cant-say-about-their-job
- YouTube trim: URL, view count and comments unchanged; the 100,000-view limit and the YPP exception; nothing on notifying viewers: https://support.google.com/youtube/answer/9057455
- ICMJE: all four quotations: https://icmje.acponline.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
- 16 CFR §255.5 wording: https://www.govinfo.gov/content/pkg/CFR-2025-title16-vol1/pdf/CFR-2025-title16-vol1-sec255-5.pdf ; §255.0(f) "the disclosure should be unavoidable": https://www.law.cornell.edu/cfr/text/16/255.0 ; Federal Register notice of 26 Jul 2023 exists: https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising
- FTC Disclosures 101: "a personal, family, or employment relationship"; "with the endorsement message itself"; in the video, not only the description; ad/advertisement/sponsored acceptable; sp/spon/collab not; "Don't assume that a platform's disclosure tool is good enough"; modified 3 Dec 2024. (The publication date showed as 24 Oct 2019 in the page data against the unit's "Nov 2019"; not treated as a finding.) https://ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers/
- GOV.UK UCP page: in force 6 Apr 2025; DMCC Act; "hidden advertising on social media"; CMA and courts, "up to 10% of their worldwide turnover"; updated 3 Dec 2025: https://www.gov.uk/government/publications/what-businesses-need-to-know-about-unfair-commercial-practices/what-businesses-need-to-know-about-unfair-commercial-practices
- CMA guidance for content creators: updated 3 Sep 2025 and every quoted fragment, including "co-own" and "#Ad in a clear, upfront position"; discount codes and affiliate links are not labels: https://www.gov.uk/government/publications/social-media-endorsements-guide-for-influencers/social-media-endorsements-being-transparent-with-your-followers
- ASA influencers' guide: fourth edition, 23 Oct 2026, developed with the CMA: https://www.asa.org.uk/resource/influencers-guide.html ; Lewis Silkin, 23 Oct 2026: DMCC basis, the five labels, "Sponsored", "Spon" and "Sp" singled out, 12 months: https://www.lewissilkin.com/insights/2026/10/23/new-influencer-guidance-from-the-asa-cap-and-cma-what-has-changed-and-what-to-d-102o6ar (unsure item 2: the unit's secondary label is correct)
- SCL: 20 Feb 2024, 97%, "only one in five systematically indicated…": https://www.scl.org/european-commission-and-consumer-authorities-investigate-online-influencers/
- PinMeTo, 22 Jul 2026: announced as a Q4 2026 initiative; "not law yet": https://www.pinmeto.com/news/eu-digital-fairness-act-scope-split-2026/
- YouTube 154235 (paid promotion button, label at the beginning, legal responsibility): https://support.google.com/youtube/answer/154235?hl=en ; 17596007 (definition, goods that may not be promoted, automatic label, undated): https://support.google.com/youtube/answer/17596007?hl=en ; PPC Land dates the announcement to 3 Sep 2026: https://ppc.land/youtube-will-label-brand-deals-that-creators-fail-to-disclose/
- Instagram, 30 Apr 2026: collab, remix and the paid partnership label; reposts and Stories "ensuring the original creator receives attribution": https://creators.instagram.com/blog/rewarding-original-creators-on-instagram ; the paid partnership page's opening sentence matches the search-result title "When you create organic branded content on Instagram, our…" (the body did not load for this checker either; partial): https://help.instagram.com/android-app/1109894795810258
- *Buivids*, 14 Feb 2019, para. 43: https://collab.dpa.gr/wp-content/uploads/2023/07/CJEU_Decision-In-Case_Buivids_C%E2%80%93345_17-2019_EN.pdf ; DPC Ireland: "you are likely to be considered a data controller" and Art. 6(1) basis: https://dataprotection.ie/en/faqs/topical-data-protection-issues/what-position-regarding-individuals-taking-photographsvideos-public-place ; C-252/21, 4 Jul 2023, the three quoted phrases: https://fra.europa.eu/en/node/44533
- ICO children's guide: updated 15 May 2026; both quotations; the 13+ rule concerns ISS consent: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/using-childrens-information-a-guide/
- Cal. Civ. Code §3344 quotations ("that person's prior consent"; parent or legal guardian): https://california.public.law/codes/civil_code_section_3344 ; Illinois PA 103-0556: in effect 1 Jul 2024, under 16, 30% within a 30-day period, trust: https://www.ilga.gov/Legislation/publicacts/view/103-0556
- YouTube child safety (under 18, features disabled including comments, adult supervision, minors' personal information): https://support.google.com/youtube/answer/2801999?hl=en
- Content ID claims: https://support.google.com/youtube/answer/6013276?hl=en ; strikes ("removed due to a legal copyright removal request"; 3 in 90 days): https://support.google.com/youtube/answer/2814000? ; Audio Library: https://support.google.com/youtube/answer/3376882?hl=en ; fair use (EU categories, fair dealing, credit): https://support.google.com/youtube/answer/9783148?hl=en
- Instagram music guidelines, 20 May 2020, three quotations: https://about.instagram.com/blog/announcements/updates-and-guidelines-for-including-music-in-video ; original content guidelines, "responsible for obtaining any necessary permissions": https://creators.instagram.com/original-content-guidelines/
- Directive 2019/1152 art. 9 (prohibition and incompatibility restrictions): https://lawplayer.com/eu/article/32019L1152/art_9 ; Acas, 24 Jul 2025, "the standards of behaviour expected from employees", no outside-work item: https://www.acas.org.uk/what-must-be-written-in-an-employment-contract/what-the-written-statement-must-include ; Circular 30, rev. 08/2024, quotation (the ellipsis elides "or the party that specially ordered or commissioned that work"): https://www.copyright.gov/circs/circ30.pdf ; NY §201-d 2(c) and 3(a) wording: https://www.nysenate.gov/legislation/laws/LAB/201-D
- HMRC content creators page: modified 22 Sep 2026; £1,000; "even if you just think of it as a hobby"; "adds up"; gifts; "by 5 October": https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/ ; IRS FS-2022-38 (Schedule 1; factors): https://www.irs.gov/newsroom/know-the-difference-between-a-hobby-and-a-business ; Topic 554, $400, reviewed 9 Nov 2026: https://www.irs.gov/taxtopics/tc554 ; Topic 420 quotation, reviewed 8 Oct 2026: https://www.irs.gov/node/68141
- CAN-SPAM guide: Aug 2023, modified 22 Jul 2025; postal address; PO box or private mailbox; 10 business days; $53,088; primary purpose: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business ; ICO email marketing: 19 Nov 2024, both quotations, "under review": https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/
- EU IP Helpdesk (2018): "two main online free-of-charge databases", >50 offices, the "classes" quotation: https://intellectual-property-helpdesk.ec.europa.eu/system/files/2021-03/EU-IPR-Guide-Trade-Mark-Design-Searches-EN.pdf ; UK IPO search page wording and options (the URL with the trailing dot loads): https://gov.uk/search-for-trademark. ; USPTO post of 18 Oct 2023, TESS retired Thursday 30 Nov 2023: https://www.uspto.gov/subscription-center/2023/retiring-tess-what-know-about-new-trademark-search-system
- Not re-opened, checked against the standard texts as known (unsure item 5; the UK copies were not re-fetched): GDPR arts. 2(2)(c), 3(2)(a), 7(1) and 7(3), 9(1) and 9(2)(e), 13; UCPD Annex I points 11 and 22 and art. 7(2); ePrivacy art. 13(1)–(2) as amended in 2009; PECR reg. 22(2); CDPA s. 11(2). The quoted wording matches. Unsure item 4 (UK GDPR art. 2 and art. 9) is unverifiable here, and the unit already hedges it.
- Pointers to filed units, all matching what those units say: PB1 §1 label set; PB1 §8's three tax sources and its question; PB1 D3 checkpoint dates; PB2 §3 (five people, delay and pass mark as conventions); PB2 D2 name, override and same-day claim; PB2 D5, repeat-back test in the week of 7 Dec 2026; PB3 §5 (collection waits for PB8; CAN-SPAM guide); PB3 §6 (YouTube answer 141805 beside AIR Media-Tech); PB4 reply slots (three 15-minute slots a fortnight); PB4 D2 (piece 2 reveal Sat 9 Jan, upload 2 Tue 19 Jan 2027; upload 3 Tue 2 Feb 2027); PB5 §5 Shorts Content ID rule (answer 15424877); PB5 piece 1's sanded-through corner; PB5 Reels in her own sound only; PB6 R3 title rule; PB7 §5 originality; PB7 IR2 and IR9.
- Mara facts agree with case-facts.md (age 38, accountant, one box, account name, 5 Jan 2027 start, six Instagram posts a fortnight, checkpoint dates, override "Mara Venn"). Her first mention is labelled (§1), and the new facts in D1 and D3 are labelled.

## (7) Figures

1. **states, §3**: FIX. "Large audience", "Dysfunctional entanglement", "Functional entanglement", "metrics as validation" (§3: "with metrics as the main source of validation"), "some creators reach" (§3: "which some moved out of into a functional entanglement") and "creators move back" (§3: "creators moved between the two") all trace to the text. "balanced dependence" and "usually begins" do not: errors, fixed above. The caption names §3, the authors, the journal and the source: PASS. The kind (a lifecycle as states) fits.
2. **decision, §6.1**: FIX. Each branch traces to §6.1 (FTC: free products, employment, tools not enough; CMA: affiliate links and codes not labels; YouTube 154235; Instagram paid partnership label). The root question leaves out the family and personal relationships the text quotes, so the "no" outcome contradicts §6.1: fixed above. The caption names the section and sources: PASS. The kind (a rule with branches) fits.
3. **matrix, §6 (sources by area and jurisdiction)**: PASS. Every cell is named in §6.1–§6.7 (UCPD Annex I 11, 22 and art. 7(2); DMCC Act and CMA; 16 CFR 255 and the FTC guide; GDPR and *Buivids*; UK GDPR and ICO; Cal. Civ. Code 3344; Directive 2019/1152 art. 9; CDPA s. 11(2) and Acas; Circular 30; HMRC and £1,000; IRS FS-2022-38 and Topic 554; GDPR arts. 3, 7, 13 and ePrivacy art. 13; PECR reg. 22; CAN-SPAM; TMview and eSearch plus; UK IPO; USPTO). The caption names §6.1–§6.7 and the date. The kind (items by sections) fits.
4. **matrix, Deliverable D3 (who acts)**: FIX. It leaves out D3's lawyer for P1 and P2, adds a "Platform" column that is not in D3's owner or professional columns, and narrows J2 and M2. Replacement JSON is given above. The kind fits. The caption is accurate once the JSON is fixed.

## (8) Writer's Source errors list (notes.md)

The list says "none". Its two citation replacements check out:
- *Buivids* now cited to the judgment, para. 43: confirmed. Para. 43: "since Mr Buivids published the video in question on a video website … without restricting access to that video, thereby permitting access to personal data to an indefinite number of people, the processing … does not come within the context of purely personal or household activities".
- Content ID options cited to answer 6013276: confirmed. "A copyright claim may be automatically generated when an uploaded video matches another video"; block, monetise or track; claims "usually don't impact your channel or account".
This check found no source error that the writer missed in a carried-over claim. The errors above are in the unit's own new text and figures.

## (9) Sourcing standard Part 5, line by line

- Claims with a number, mechanism or recommendation sourced where made: PASS, except the NY §201-d omission and the stale DFA status (findings).
- Source types (peer-reviewed, platform-official, vendor with n and date, documented case): PASS. Law and regulator guidance are labelled as such. The secondary reports (SCL, PinMeTo, Lewis Silkin, PPC Land, Better Internet for Kids, PsyPost, Cornell Chronicle) are labelled.
- Anecdote, correlational and vendor labels: PASS (Scott, Mills, Haushofer as anecdote; the Frontiers survey as correlational; no vendor data used).
- A growth, format or metric claim names its platform: PASS (§3 names Instagram and YouTube; §6 is per platform).
- Carried-over claims re-verified: PASS (notes F2; every carried quotation re-checked here holds).
- No private-course reader detail and no reference to the private course: PASS for both (no names, cities, sports or source-unit codes found). FAIL on the private-workflow jargon "writing chat" and "(see notes)" (findings).
- Mara facts labelled, consistent and never used as evidence; benchmarks sourced: PASS.
- No country's tax rate stated as the reader's; amounts in source currency with dates; legal points as questions with EU, UK and US sources; "information, not legal or tax advice": PASS.
- No uncited figures, no invented names, handles or studies: PASS except figure 1's two unsourced labels (findings).
- Changeable facts dated: PASS (the intro dates everything to 13 Nov 2026, and the pages' own dates are given). The DFA status is stale (finding).
- Deliverable in full for Mara, then as a template with blanks that say what goes in them: PASS (one ambiguous T3 pointer, finding).
- Not advice without evidence: PASS. Each "her rule" names its basis.
- Links given as links: PASS.

## (10) Read as the brief's persona

- "no writing chat can run a register search" (D3 M1) and "(see notes)" (D3 lead-in) assume knowledge of how the course is produced: findings above.
- Codes such as D1, IR2, IR9, R3 and "PB9 (deals, to come)" are pointers to units of this course, so they are allowed. Nothing else assumes a private reader.

PB8, verdict: fix · error 2, should-fix 6, minor 8
