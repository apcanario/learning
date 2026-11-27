claude-opus-5-5

# SCE8 applier notes

Findings: 16. Apply 14, hold 2 (f5, f11), both repaired as extra fixes. Every `current` occurs once in unit.md, and every extra fix's `current` occurs once after the applied findings, checked by script (out/make.py) applying all of them in memory in order. No fix contains an em dash.

Sources re-read in this run, each address returned by a WebSearch here: the Gartner MQ TMS 2026 reprint (lp.shipsy.ai), Staudt et al. 2026 at SciELO, the Evangelista et al. 2013 Aston manuscript, Routledge's page for Rodrigue 6th ed., x12.org "About X12", Oracle's and C.H. Robinson's (en-sg) report landing pages.

## Holds

- **f5 (D2 rule).** The problem is real, but the fix says "in the fourth column". In D2 the columns are #, Need, Shipper, Provider, Where the needs pull apart, Basis, so the fourth column is Provider. Repaired as X1, which names the column by its header.
- **f11 (Deliverable E, control tower).** Restoring the aim is right. But "the same study found it unmet in its cases" goes beyond the paper. The paper says end-to-end supply chain management was not identified in the cases and two of the three companies had no real-time tracking or visibility layers. It does not say end-to-end visibility was found unmet. Repaired as X2 using the paper's own finding, worded as section 10 already words it.

## Could not verify list

1. **FreightLab 302 redirect.** Not checked. A redirect counts as not checked under the web rule, and no search returned the address. It bears on SCE1's citation, not on any SCE8 claim; SCE8 cites only ctl.mit.edu/research/freightlab, which the report confirmed. No change to SCE8. It stays with the SCE1 correction (writer's contradiction 1).
2. **Bartholdi & Hackman §1.2.** Not cited in SCE8 (no occurrence in unit.md). It bears only on the writer's note about SCE1's 3PL row. No change; not checked.
3. **Rodrigue ISBN 9781032380407.** Verified: Routledge's page gives The Geography of Transport Systems, 6th edition, Jean-Paul Rodrigue, 2024, ISBN 9781032380407. No entry.
4. **Tail of the MQ planning quotation.** Verified in the reprint: "including order and shipment consolidation, mode selection, route determination and carrier selection." This matches §1. No entry.
5. **§9, two vendors' landing pages.** Verified: Oracle's and C.H. Robinson's pages hold no report text, and both say "The Gartner document is available upon request from" the vendor. No entry.
6. **§3.3 "X12, the US-based standards body".** Only partly verified. x12.org says X12 is "an ANSI-accredited, consensus-based, non-profit organization" chartered by the American National Standards Institute that develops EDI standards, but it does not state a US base. Replaced by what the page says (X3).
7. **kit/private_terms.py.** Not run: it is outside the packet. It must be run at filing.

Totals: 3 verified (items 3, 4, 5), 1 corrected to its source (item 6, X3), 3 not checked with no SCE8 claim resting on them (items 1, 2, 7). Nothing cut, nothing marked unverified.

## For syllabus flags

- **F64 and F6 (SCE1 §3, SCE7 §5, SCE10).** The 2026 MQ names "bid and rate management and optimization" under freight sourcing. Its carrier-network common feature exchanges rates, booking requests and confirmations over API or EDI. "Payment" appears in two vendor profiles (Manhattan Associates, Pando). Units that rely on "the report names no rating or tendering" should take this wording.
- **Common features, analytics (SCE8 and any unit citing the 2026 MQ's common features).** The common analytics feature is itself embedded analysis. Do not describe it as "beyond the embedded kind".
- **C11 (SCE1 C10/C11, SCE8 §10, later control-tower units).** Staudt et al.'s definition builds end-to-end visibility in as an aim. Their findings (no end-to-end supply chain management identified; two of three without real-time visibility layers) should not be restated as "found end-to-end visibility unmet".
- **SCE1 FreightLab citation (writer's contradiction 1).** Still open: the redirect was not checked, and SCE1 §2's figure caption must change with its text.
- No held error is left open in SCE8: both holds are repaired by X1 and X2.
