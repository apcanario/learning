# Corrections check, BW10 corrections 1 (B8, BW1, BW4; notes for BW2, DD-BW3)

Checker: claude-opus-5-5 (Opus 5.5), fresh agent, 16 Nov 2026. Live search: WebSearch first, WebFetch only on URLs returned verbatim. Note on method: WebFetch passes pages through a summarising model; the negative results on the Models overview page (Change 3, Change 4) rest on that reading and on the writer's two independent reads.

## Change 1
File: B8-cost-limits-hygiene.md
Current:
```
*Understanding usage and length limits* still says "Claude's context window size is 200K tokens across all models and paid plans", with 500K on some models for Enterprise; the page shows no date ([article 11647753](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits), read 2 Nov 2026).
```
Replacement:
```
*Understanding usage and length limits* still says "Claude's context window size is 200K tokens across all models and paid plans", with 500K on some models for Enterprise; the page shows no date ([article 11647753](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits), read 2 Nov 2026). On 16 Nov 2026 the same article, now headed *How do usage and length limits work?*, says "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens" ([article 11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work), read 16 Nov 2026).
```
Result: PASS. https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work (read 16 Nov 2026): title "How do usage and length limits work? | Claude Help Center", labelled "Updated over a week ago"; "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens." The writer's replacement would delete the 2 Nov reading; this replacement keeps it and appends the 16 Nov reading, so the paragraph's later "Two pages against two" stays true of 2 Nov and the unit stays a dated record. Same fact, same source as the correction; nothing else added.
Syllabus: no conflict. B8 is private; no brief, filed unit or register entry relies on the 200K reading. Consistent with syllabus flag F9 ("Later units cite BW1 for the mechanism and re-read the figure on the day"). Two other B8 passages describe the 2 Nov state of this article (the claim table row "The window is 200K tokens on every plan … Changed, and disputed" and unsure list item 1, "article 11647753 (undated) … still say 200K"); both are dated to 2 Nov and are left for B8's staleness check (see Not a text change, item 4).

## Change 2
File: B8-cost-limits-hygiene.md
Current:
```
| Usage credits are prepaid and billed at standard API rates |
```
Replacement:
```
| Usage credits are bought ahead and billed at standard API rates; credits bought on or after 7 December 2026 generally expire twelve months after purchase (read 16 Nov 2026) |
```
Result: FAIL. https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans (read 16 Nov 2026, labelled "Updated this week"): "Usage credits are billed at standard API rates"; "You'll then need to purchase credits to cover usage beyond your plan's limits"; "You can also enable auto-reload to automatically make a purchase when your balance falls below a threshold you set"; "Generally, usage credits purchased on or after December 7, 2026 expire 12 months after the purchase date"; "Credits purchased before December 7, 2026 don't expire." Two reasons it fails: (1) the named text is the first column of the table headed "B2 §2 said": it quotes B2's claim, not B8's, so rewriting it would misquote B2; (2) "prepaid" is not wrong: the page describes buying credits (a balance, auto-reload below a threshold) before use, which is what prepaid means; the word's absence from the page is not an error. The expiry fact is real and new; it belongs in B8's own status cell (New 1).
Syllabus: no conflict (no change applied).

## Change 3
File: BW1-mental-model.md
Current:
```
Anthropic's model page gives the current tokenizer's own conversion: 1M tokens is roughly 555k words or 2.5M Unicode characters, about 2.5 characters a token ([*Models overview*](https://platform.claude.com/docs/en/models/overview), read 15 Nov 2026; the per-token division is this unit's arithmetic).
```
Replacement:
```
On 15 November 2026 Anthropic's model page gave the current tokenizer's own conversion: 1M tokens is roughly 555k words or 2.5M Unicode characters, about 2.5 characters a token ([*Models overview*](https://platform.claude.com/docs/en/models/overview), read 15 Nov 2026; the per-token division is this unit's arithmetic); on 16 November 2026 the page no longer carried the figure (read 16 Nov 2026).
```
Result: PASS (the correction's finding is confirmed: the figure is not on the cited page). https://platform.claude.com/docs/en/about-claude/models/overview (read 16 Nov 2026; the page gives https://platform.claude.com/docs/en/models/overview, the URL BW1 cites, as its canonical and og:url): none of "words", "characters", "Unicode", "555", "2.5M" or "tokenizer" appears. Searched for another vendor page carrying it, to move the citation: https://platform.claude.com/docs/en/build-with-claude/context-windows (read 16 Nov 2026): none of those terms; https://platform.claude.com/docs/en/resources/glossary (read 16 Nov 2026): carries BW1's other sentence ("Claude 4.7 and later models … produces approximately 30 percent more tokens … approximately 3.5 English characters") but not 555k or 2.5M. A WebSearch for "1M tokens" "555k words" returned only third-party pages. The citation cannot be moved to a vendor page, so the claim is kept as read on 15 Nov and dated as gone on 16 Nov. No other text changes; BW1 names no private course.
Syllabus: no conflict with a brief or the register (neither quotes the figure). BW4 builds on it (Change 4; its Deliverable's 720-token figure, line "about 720 tokens at 400 words on BW1 §2's conversion", and unsure item 8, which already says the arithmetic divides BW1 §2's figure and is unmeasured). Later units that need a characters-per-token figure should not cite this conversion; the glossary's figure (about 3.5 English characters on pre-4.7 models, about 30 percent more tokens on 4.7 and later) is still on the vendor's page.

## Change 4
File: BW4-context-engineering.md
Current:
```
Anthropic's model page gives 1M tokens as roughly 555,000 words for its current tokenizer (BW1 §2, read there 15 Nov 2026)
```
Replacement:
```
Anthropic's model page gave 1M tokens as roughly 555,000 words for its current tokenizer (BW1 §2, read there 15 Nov 2026; not on the page on 16 Nov 2026)
```
Result: PASS. Same source and reading as Change 3: https://platform.claude.com/docs/en/about-claude/models/overview, read 16 Nov 2026, no "words", "555" or "2.5M". BW4's arithmetic (about 1.8 tokens a word, 720 tokens for 400 words) is already labelled "Illustrative arithmetic, unmeasured" and is left as is.
Syllabus: no conflict. BW4's Deliverable keeps its 400-word instruction-file limit, graded "stated opinion"; the limit does not rest on the token figure. Flag F30 ("BW5 keeps those names or says where it departs") is unaffected.

## Not a text change

1. Source error 2 (B8 §1, Ultra row "Included, up to half the weekly limit", and the Ultra article's "separate weekly limit for Fable"). Confirmed as the writer says: https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan (read 16 Nov 2026, labelled "Updated this week"): "You can use up to 50% of your weekly usage limits on Fable models at no extra cost", Fable models "draw from your plan's regular weekly usage limits and use them faster than other Claude models", and the FAQ "your use of other models draws from the same usage limits"; no separate Fable limit. https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work (read 16 Nov 2026): "Weekly limits apply across all models, and some plans also have a separate weekly limit for Fable." B8's 2 Nov text reports what each page said then, and B8 unsure item 4 already records the disagreement. Needs: a note for B8's six-month staleness check (method §6): "as read 16 Nov 2026 the Fable article describes a share of the regular weekly limit, and the usage-limits article a separate Fable limit on some plans." Unit: B8.
2. Contradiction 2 (BW2 §6 and Appendix, "a separate weekly limit for Fable on some plans"). Both vendor pages say what BW2 reports (quotes in item 1); they disagree with each other, BW2's sentence is a faithful dated report of one of them, and BW2 §6 also cites the Fable article ("it draws from them faster"). No text change. Needs: a note for BW2's staleness check (15 May 2027, flag F17) and for any later unit that states a Fable allowance (DD-BW1, DD-BW3): cite both pages and date them. Units: BW2, BW10, DD-BW1, DD-BW3.
3. Contradiction 3 (BW2 Deliverable rule 1, "on the API an effort change mid-session can invalidate the cache"). Confirmed: https://code.claude.com/docs/en/prompt-caching (read 16 Nov 2026): "On most models, changing the effort level mid-session means the next request reads the entire conversation history with no cache hits"; "On Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1 with an API key or a Claude subscription, changing effort keeps the cache"; Fable 5.2 is not listed; not on Bedrock, Google Cloud's Agent Platform or a Claude apps gateway. BW2 rule 1 cites the API *Effort* page and says "can"; it holds. No text change. Needs: a note for DD-BW3, whose brief asks it to test "the rules of BW10 and DD-BW1 against your own record": an effort change keeps the cache on the four listed models on Anthropic's own API or subscription, breaks it elsewhere. Units: BW2, BW10, DD-BW3.
4. Contradiction 4 (BW4 §4, "The pause is short"). Confirmed: the same Claude Code page gives the main conversation a one-hour TTL "on a Claude subscription, within plan usage" and five minutes on usage credits, API key or cloud provider; BW4's line ("the cache expires after inactivity", saving "unknown") is not contradicted. No change. Also for B8's staleness check: B8's claim table row on the window and unsure list item 1 describe article 11647753 as of 2 Nov (200K, undated); Change 1 records the 16 Nov reading in §1 only. Units: BW4, B8.

## New

## New 1
File: B8-cost-limits-hygiene.md
Current:
```
| Holds; available on Pro, Max and Ultra; a monthly spend limit can be set |
```
Replacement:
```
| Holds; available on Pro, Max and Ultra; a monthly spend limit can be set. On 16 Nov 2026 the page adds that credits bought on or after 7 December 2026 generally expire twelve months after purchase; credits bought before then do not expire |
```
Result: PASS. https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans (read 16 Nov 2026, labelled "Updated this week"): "Generally, usage credits purchased on or after December 7, 2026 expire 12 months after the purchase date." "Credits purchased before December 7, 2026 don't expire." "Expiration dates may vary in certain countries." This is the fact correction 3 cites, placed in B8's own status column instead of the column that quotes B2 (Change 2). The claim column and the row's 2 Nov source label are unchanged.
Syllabus: no conflict. B8 is private; its rule 21 ("credits are billed at API rates and the limit is set under "Adjust limit"") is unaffected. No public brief or the register refers to credit expiry. BW2 §6 ("usage credits keep you working at standard API rates, billed separately and bought in advance") stays accurate; BW10 and any later public unit that advises buying credits should date the 7 Dec 2026 expiry rule.
