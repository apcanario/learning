# P98 · figure renderer finishes (12 Nov 2026, row W-PB5 step 1b)

Opus 5.5 (the chat), with fresh Opus 5.5 re-check agents. No agent transcript was kept on disk in this session, so the scripted transcript checks could not be run; each agent's model is the one it stated (claude-opus-5-5). The agents' harness refused their own report writes; each report here is the agent's final reply, saved verbatim by the chat.

## What changed

1. **Bars on a 320 px phone.** `_bars_phone` draws at `PHONE_NARROW` (258 units) in place of `PHONE_FRAME` (328); `design/theme.css` 6.10 shows a bars figure's svg.viz-alt at its own size, as a compare's. Correction to the row's premise, found by `probe-bars.py`: before P98 the 328-unit drawing did not scroll on a 320 px phone; the theme shrank it to the 258 px frame, so its text was drawn at about 79% of its size. It is now drawn at its own size.
2. **A value at the end of its track.** `viz._val_x`: a compare's value sits 8 units past its bar when it fits wholly on the track there (4 units clear of the end), else wholly beyond the track's end (6 units past it), in both drawings. Bars draw no track, so the rule does not apply to them.
3. **Caption and label notes** (S-PB1's re-checks): applied in the figures' declarations, prose untouched: A9 fig 5 `decimals: 2`; DD-A1 fig 3 caption (M and K); A3 fig 4 caption (weeks 1 and 2, the tones); A5 fig 3 caption (the tones are the theme's); B4 fig 4 and DD-B2 fig 1 captions (tones); B2 fig 1 caption "(prompt up to 100K)"; B6 fig 1 "about 4×", "about 15×"; IA6 fig 3 decimals dropped (8, 3, 2, 1); PB1 fig 2 caption (tones).

`verify.py`: `check_compare_phone` is now `check_phone_figures`: every compare and bars figure at 320 and 390 px opens unscrolled with every bar and every value whole in the frame, in its phone drawing; and at 320, 390 and 1280 px no value sits across the end of its track. `negative-test.py` runs it on the build before P98: 121 values across a track's end, none after.

## Re-checks

- `changed-figures.txt`: 67 figures on 50 pages changed against the build before P98 (43 compare, 24 bars), listed by script. Sheets by `shots.py` (verify's `frames()`), 320, 390 and 1280 px, dark and light.
- Round 1: `brand-a.md` 14/14 PASS, `brand-b.md` 13/13 PASS, `greece.md` 12/12 PASS, `rome.md` 13/13 PASS, `ux-pb-examples.md` 12/15 PASS: PB3 fig 3 and PB4 fig 3 FAIL (Capture and Log share a tone: the seventh series repeats tone 1), viz-examples fig 21 FAIL (the chat had staged figure 13's declaration as figure 21's).
- Fixes: the two captions say which segment is which (the checker's text); figure 21 re-checked against its own declaration. Minor notes with a fix were applied in the declarations: Greece 3.7 fig 2 (totals after the bars), A5 fig 4 and A9 fig 2 (tones), A9 fig 5 (bands with no percentage), PB1 fig 1 and PB3 fig 2 (tones), PB3 fig 1 (the All adults row).
- Round 2 (`recheck-2.md`): the 10 figures changed or re-staged, 10/10 PASS. Its two minors with a fix (A5 fig 4's fourth tone; PB1 fig 1 counts livestreams too) were applied as its exact text; the drawings are unchanged.
- Recorded, not applied (the figure's own text cannot meet them, or the note says no change): segment values left out of narrow stacked segments (renderer rule, Rome 4.3, A2, A7, DD-B2, examples 13); two decimals forced by 11.75 and 0.25 (PB3 fig 3, PB4 fig 3, B1 fig 2); "k tokens" form (B4 fig 2, B8 fig 2); work titles in roman in bar labels (Greece 3.7, 4.1); close light-theme hues (Greece 3.5; PB3 and PB4 Email and Edit); figures with no title line (A4, A6, DD-A1, UX); the 35,000 "about" (Greece 6.6, label already says unsourced).
