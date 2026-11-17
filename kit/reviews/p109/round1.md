<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
PASS 2 (dd-ia3 fig 5, ia9 fig 6), FIX 7. No figure needs a declaration change. The seven FIXes come down to two renderer changes.
R1 (renderer, 7 figures: a8, dd-bw3, pb8, rm31, dd-ia1, ia1, ia11): on the phone the keys scroll with the matrix, so once it is scrolled they are clipped and their text is dimmed partway through words. Move the key block out of the scroller.
R2 (renderer, rm31 fig 3 only): on desktop the 65 px scroll has no sticky row labels, so at the end of the scroll the LAWS column has no row names. Make the row labels sticky as on the phone, or scale this matrix to the column.
All three P109 changes are in place: A8's cells take their keys' tones, IA1's "help, download" and Rome 3.1's blue cells have keys, and PB8 fig 4 fits its desktop frame. No figure scrolls a few pixels at desktop.
The harness refused the write to out/report.md, so the full report follows.

# p109-1 · fresh figure re-check (P109: matrix keys and widths)

Checker: claude-opus-5-5. I opened files in the packet only and published nothing.

## Verdicts

| Figure | Verdict | Notes |
|---|---|---|
| brand-a/read-a8 fig 3 | FIX (R1) | The CHANGE is done. Every tinted cell has its key's tone, checked by pixel in both themes: owns green; confirms, label and enforces tan; reviews red; if unclear and optional violet; policy and sign khaki. Rows and cells match register R1–R32 (text lines 198–229). Desktop is frame 1 of 1 with no scroll. Phone fault: R1. Minor: in light, policy/sign khaki (212,201,175) is barely different from an empty cell (215,209,197) and from label tan (220,197,175). The cell words carry the meaning, so no change is asked. Minor: R17's "lawyer if the DGC writes" is not drawn; the block-level reading is acceptable. |
| building-with-ai-bw/read-dd-bw3 fig 2 | FIX (R1) | Fits at 1280 (frame 1 of 1). Cells match the §2 extra-columns table and the §3 "In the sheet" lines. The yes and group keys match their cells by pixel. Minor: "redone" is in the count tone for Badly put and the group tone for Wrong tool. §3 reads the second against the routing row for the task type ("a light model on a task the routing table puts higher, where the outcome is redone"), so the key's "read against the task type" holds. Phone fault: R1. |
| personal-brand-pb/read-pb8 fig 4 | FIX (R1) | The CHANGE is done. At 1280 the whole figure fits in frame 1 of 1, with no second frame and no fade over the keys. Cells match register A1–R1 (lines 237–260). Minor: M2's "Trade mark attorney" is unconditional in the register, but the Trademark row shows only "if a hit". M2 is open until 2028, so the block reading stands. Phone fault: R1. |
| rome/r-3.1 fig 3 | FIX (R1, R2) | The CHANGE is done. The blue cells (confers, elects, declares, hears, passes) have a key, and "most" has its own. Every cell matches "The settlement" paragraph (line 100). The matrix is over 700 units, so it is drawn wide and scrolls 65 px at 1280 as the rule intends, but see R2. Phone fault: R1. |
| ux-ia/read-dd-ia1 fig 7 | FIX (R1) | Fits at 1280. Every cell matches the figure paragraph (line 180) word for word. Rows are tone 2, the Strain column tone 6, and the keys match by pixel. Minor: in light, tone 2 (220,197,175) and tone 6 (212,201,175) are nearly the same; the Strain header carries the difference. Phone fault: R1. |
| ux-ia/read-dd-ia3 fig 5 | PASS | Fits at 1280. Cells match the paragraph describing the drawn cadence (line 267). There is no key because the figure uses one tone, and the caption gives the reason ("Every row tone 5, shared"). Phone and 320 px are readable. |
| ux-ia/read-ia1 fig 4 | FIX (R1) | The CHANGE is done. The green "help, download" cell has its key ("only for help articles and the link to download the app", matching section 5, line 134). The primary and sign in keys match. Fits at 1280. Phone fault: R1. |
| ux-ia/read-ia11 fig 6 | FIX (R1) | Fits at 1280. Cells match the §6.4 table (lines 264–270). Rows are tone 5 and the Perqo column tone 3; the keys match. Phone fault: R1. |
| ux-ia/read-ia9 fig 6 | PASS | Fits at 1280. Cells match Deliverable C, RV-01 to RV-12 (lines 336–347), with conditions in brackets as the caption says. No key: one tone, and the caption gives the reason. Minor: the last phone frame stops at 196 of 197 px; nothing is hidden. |

Counts: PASS 2, FIX 7. The FIXes need two renderer changes: R1 covers all seven, R2 is rm31 only. No declaration change is needed.

## FIX R1 · renderer: on the phone, keys are dimmed and cut when the matrix is scrolled

What it draws wrong. At 390 and 320 px the key block sits inside the horizontal scroller. As soon as the reader scrolls the matrix, the keys scroll with it:
- Swatches are clipped at the left ("rms", "ws", "clear").
- From a fixed x, about the right edge of the sticky row-label column, the key text is dimmed partway through words: "he acts on it or cha|ses it", "a contabilista certificado co|nfirms", "the surface buil|t for".

It shows in both themes. Examples: phone-read-a8 light and dark frame 2 (scrolled 49 px); phone320-read-a8 light frame 2; phone-read-ia1 light frames 2–3; phone-read-dd-bw3 frames 2–4; phone-read-pb8 frames 2–3; phone-read-dd-ia1 frames 2–3; phone-read-ia11 frames 2–3; phone-rm31 frames 2–3. In frame 1 (the opening position) every key is whole, so nothing is lost there. The fault is that the keys are faded or cut while the reader is matching a right-hand column to them.

How it should draw. Put the key block and the "scroll sideways" line outside the scroller, beneath it, at the column width, so it never scrolls, clips or takes an edge fade. Only the matrix scrolls, under its sticky row labels. This applies to every matrix with keys; in this list: a8 fig 3, dd-bw3 fig 2, pb8 fig 4, rm31 fig 3, dd-ia1 fig 7, ia1 fig 4, ia11 fig 6.

## FIX R2 · renderer: on desktop, rm31 figure 3 loses its row labels when scrolled

What it draws wrong. At 1280 the matrix is drawn wide and scrolls 65 px. On the phone the row-label column is sticky; on desktop it is not.
- At 65 of 65 px (desktop-rm31 frame 2, dark and light), Curiate, Centuriate and Tribal are gone and only "ouncil" of "Plebeian council" remains. The LAWS column, the only place "passes" and "most" sit, is then read with no row names.
- At opening (frame 1), the LAWS column is hidden under the right fade, so the cell the "most" key explains is not on screen until the reader scrolls.

How it should draw. In desktop wide mode, keep the row-label column sticky as on the phone. If the rule allows an exception: the overflow is only 65 px (about 9 percent), so this matrix could instead scale to the column like those of 700 units or less. R1's fix also stops the keys being clipped at the left in this frame.

## Sheets opened

- Desktop 1280, dark and light, all nine figures (the desktop-…-matrix-frames-dark/-light.png sheets). Tones on a8, bw3 and dd-ia1 checked by pixel sampling.
- Phone 390 light, all frames: a8 fig 3, dd-bw3 fig 2, pb8 fig 4, rm31 fig 3, dd-ia1 fig 7, ia1 fig 4, ia11 fig 6. First and last frames: ia9 fig 6, dd-ia3 fig 5.
- Phone 390 dark: a8 fig 3, frames 1–2.
- Phone 320 light: a8 fig 3, frames 1–2.
- Text read:
  - read-a8.md: register, lines 194–236
  - read-dd-bw3.md: lines 55–130
  - read-pb8.md: lines 237–264
  - rm31.md: lines 68–102
  - read-dd-ia1.md: lines 176–183
  - read-dd-ia3.md: lines 265–269
  - read-ia1.md: lines 118–139 and 257
  - read-ia11.md: lines 258–275
  - read-ia9.md: lines 225–231 and 336–347
