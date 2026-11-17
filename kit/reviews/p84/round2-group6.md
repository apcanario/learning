<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
19 PASS, 4 FIX (23 figures).
FIX: m12 fig 3: renderer clips the tops of the second line of the 1952 label ("the BBC (1 July)") at 1280 px.
FIX: rm115 fig 2 and rm127 fig 1: caption section names need quotation marks.
FIX: ia3 fig 4: caption says "tone 3/tone 6", but the keys read "covered"/"may look here".
I could not write out/report.md (the harness refused the write), so the full report follows.

# r2-6 figure re-check

| Figure | Verdict | Notes |
|---|---|---|
| greece r-1.2 fig 1 (m12) | PASS | The LH phases match the Chronology table. LH II and LH IIIA share a lane and stop short where they abut. LH I high chronology is 1700–1500. The takeover (c. 1450) and the destructions (1200–1180) are correct. |
| greece r-1.2 fig 3 (m12) | FIX | The dates match the text (1900, 1940s, 1941, 1952, 1953, 1956). At 1280 px, light and dark, the tops of "th" in "the" are clipped on the second line of the 1952 label. The phone sheets are clean. |
| greece r-1.2 fig 4 (m12) | PASS | Madduwatta is drawn as the fifteenth century (1500–1400), labelled as written. c. 1280, c. 1250 and c. 1220 are correct. |
| greece r-12.7 fig 1 (m127) | PASS | Every span matches the table. Cleanthes and Diogenes abut at 230 with a gap. Embassy at 155. |
| greece r-3.5 fig 3 (m35) | PASS | 467, c. 442, c. 429, c. 409, 405 and 401, and the span c. 442–401, all match. |
| greece r-5.5 fig 3 (m55) | PASS | All 14 events match, and the two spans abut at 527 with a gap. Minor: the span label "546–527 BC" drops the text's "c." on 546. |
| greece r-6.5 fig 1 (m65) | PASS | Every span matches the table. |
| greece r-6.5 fig 3 (m65) | PASS | The spans match the text. The caption explains the Assos span, 347–343. |
| greece r-8.2 fig 1 (m82) | PASS | Positions checked against the gridlines. Minor: the one-year Fourth bar is very thin. Minor: "First Sacred War" is named differently from "Second". |
| greece r-9.2 fig 1 (m92) | PASS | All dates match the text. |
| rome r-1.4 fig 1 (rm14) | PASS | 753, c. 200, the 180s–170s, 27–25 BC, 7 BC and AD 100 are correct across BC/AD. |
| rome r-11.5 fig 2 (rm115) | FIX | The drawing is correct. The caption gives section names without quotation marks, so they cannot be read as names. Minor: the Cilicia label runs across 48–43 BC; the guides are broken correctly where they cross it. |
| rome r-12.7 fig 1 (rm127) | FIX | The drawing is correct (the span 1953–1965 and 12 works). The caption's three section names have no quotation marks, so the sentence does not parse. |
| rome r-2.5 fig 2 (rm25) | PASS | Positions verified by pixel fit. All 8 items match. Minor: the 105 Serapeum has no source, and the caption does not say so. |
| rome r-5.1 fig 2 (rm51) | PASS | All dates match. |
| rome r-7.1 fig 1 (rm71) | PASS | All dates match the table. Minor: the Gaius label sits in lane 0 over AD 41–49. |
| rome r-7.1 fig 4 (rm71) | PASS | All events match. "Boudica, 60 or 61" is drawn as the span 60–61. |
| bw4 fig 1 (matrix) | PASS | The cells match §2. The key sits under the frame, whole at 1280, 390 and 320 px, in the cells' tone. Row labels stay in view. |
| pb8 fig 4 (matrix) | PASS | Every cell matches D3's owner and professional columns. All five keys are whole at every width and match their cells' tones. |
| dd-ia2 fig 3 (matrix) | PASS | All 15 metrics match. The keys are whole and match their tones. Row labels stay in view. Minor: the swatches read "tone 5/1/4", internal names. |
| ia3 fig 2 (matrix) | PASS | Matches section 1.2's table. The keys are whole and match their tones. |
| ia3 fig 4 (matrix) | FIX | The cells match section 3.3. The keys are whole and match their tones. The caption's "tone 3/tone 6" appear nowhere in this figure, whose keys read "covered" and "may look here". |

**FIX 1: greece/r-1.2 fig 3 (renderer).** At 1280 px, the second line of the 1952 label, "the BBC (1 July)", is cut at cap height. The likely cause is the stacked 1953 label's plate, or the first line's plate, painted over that line. Fix: paint all label plates before any label text, or stack staggered event labels with at least one line-gap between one label's last line and the next label's plate.

**FIX 2: rome/r-11.5 fig 2 (caption).**
Replace `From the sections The new man and his consulship to Tullia, philosophy, the Philippics and death, 45–43:`
with `From the sections “The new man and his consulship” to “Tullia, philosophy, the <em>Philippics</em> and death, 45–43”:`

**FIX 3: rome/r-12.7 fig 1 (caption).**
Replace `From the sections The "Harvard school" and the pessimistic reading, The optimistic or Augustan school and Further voices and the end of the binary:`
with `From the sections “The ‘Harvard school’ and the pessimistic reading”, “The optimistic or Augustan school” and “Further voices and the end of the binary”:`

**FIX 4: ux-ia/read-ia3 fig 4 (caption).**
Replace `Tone 3 is the app; tone 6 marks a place this review expects a failed look; every 'may look here' is assumed, to be tested.`
with `'Covered' cells take the app's tone; each 'may look here' marks a place this review expects a failed look, and every one is assumed, to be tested.`

**Sheets opened**
- Desktop (1280) light and dark: all 23 figures.
- Phone (390) light: all 23 figures.
- Zoomed crops: m12 fig 3 desktop (light and dark), m82 fig 1, rm115 fig 2, and a pixel scan of rm25 fig 2.
- Phone 320 light: read-bw4 fig 1.
- Phone dark: not opened; nothing was marginal.
