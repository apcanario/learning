# P64 timing check: OGIS 338 (= I.Pergamon I 249) relative to Attalus III's death

Checker model: claude-opus-5-5 (fresh corrections checker). Only file opened on disk: /home/claude/packets/p64/places.md.

## Source relied on

https://change.csad.ox.ac.uk/inscriptions/item/item-4.1268 (CHANGE database, University of Oxford CSAD), entry for I.Pergamon 249 (PHI ID 301891, Trismegistos 868412). Words relied on:
- Title: "Decree granting citizenship and resident foreigner status to various groups after death of Attalos III"
- Date fields: "Date From -133", "Date To -133"; Date "133 BCE".

This supports: passed in 133 BC, after Attalus' death. No source found says "within weeks" or "just after". The interval within 133 is not established by any source checked. (The Roman-ratification clause was outside this task and is not confirmed by this page, which does not mention it.)

## Place 1 (line 79)

Current:
```
**Where sources disagree.** The letter of Mithridates in Sallust, *Histories* 4.69 M, alleges the will was forged by Rome. The Pergamene decree *OGIS* 338, passed within weeks of Attalus' death, cites the will and says that Rome had still to ratify it, which most historians take as decisive; the motive, probably to pre-empt a succession war, remains conjecture.
```

Verdict: REPLACE ("within weeks" unsupported; the source supports only "in 133, after his death").

Replacement:
```
**Where sources disagree.** The letter of Mithridates in Sallust, *Histories* 4.69 M, alleges the will was forged by Rome. The Pergamene decree *OGIS* 338, passed in 133, after Attalus' death, cites the will and says that Rome had still to ratify it, which most historians take as decisive; the motive, probably to pre-empt a succession war, remains conjecture.
```

Check against the source: PASS. https://change.csad.ox.ac.uk/inscriptions/item/item-4.1268: "after death of Attalos III"; "Date From -133 ... Date To -133".

## Place 2 (line 181)

Current:
```
    Answer: The Pergamene decree OGIS 338, passed just after his death in 133, cites the will and says that Rome had still to ratify it; the forgery allegation appears only in Mithridates' letter in Sallust's Histories.
```

Verdict: REPLACE ("just after" is stronger than any source checked; year 133 and "after his death" are supported).

Replacement:
```
    Answer: The Pergamene decree OGIS 338, passed in 133, after his death, cites the will and says that Rome had still to ratify it; the forgery allegation appears only in Mithridates' letter in Sallust's Histories.
```

Check against the source: PASS. Same source and words as Place 1.

## Searches and fetches

1. WebSearch: `OGIS 338 Pergamon decree Attalus III will "ratified by the Romans" date 133`: returned results incl. attalus.org/docs/ogis/s332.html, change.csad.ox.ac.uk item-4.1268 and item-12.1269.
2. WebSearch: `attalus.org OGIS 338 Pergamon decree citizenship after death of Attalus Philometor will`: returned results incl. attalus.org/docs/other/inscr_120.html.
3. WebFetch https://www.attalus.org/docs/ogis/s332.html: fetched; page is OGIS 332 only (divine honours for Attalos III, 138-133 BC), not OGIS 338. Not used.
4. WebFetch https://www.attalus.org/docs/other/inscr_120.html: refused by permission classifier. Not checked; not retried.
5. WebSearch: `"OGIS 338" Pergamon decree "shortly after" death Attalus III 133`: no result stating the interval.
6. WebFetch https://change.csad.ox.ac.uk/inscriptions/item/item-4.1268: fetched; I.Pergamon 249, "after death of Attalos III", dated -133 to -133. Used.
7. WebSearch: `Pergamene decree after Attalus III death "until the will is ratified" Romans citizenship paroikoi 133 BC immediately after`: returned www.Wikipedia.com/wiki/War_of_Aristonicus among others.
8. WebFetch https://www.Wikipedia.com/wiki/War_of_Aristonicus: refused by permission classifier. Not checked; not retried.


---
Applied 17 Nov 2026 by the H-4 chat (Opus 5.5): both replacements, each passed against the source above, as exact replacements in `courses/greece/7.3-rome-conquers-greece.md` (each current text occurred once). The ratification clause itself was confirmed by `corrections-2026-11-17-p64.md` and is unchanged.
