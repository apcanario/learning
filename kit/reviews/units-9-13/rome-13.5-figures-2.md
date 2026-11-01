# Rome 13.5 Seneca: figure check 2

Checked against `text.txt`, `captions.md` and all twelve renders (desktop and phone frames, dark and light). House rules applied: sideways scroll in phone frames, spans as short bars above the axis, range-dated events on the range's first year.

## Figure 1 (timeline): FIX

**Trace, drawing to text**

| Item in figure | Text | Passage in text | Result |
|---|---|---|---|
| c. 4–1 BC, Born at Corduba (modern estimate) | "some time between about 4 and 1 BC; no ancient source gives the year, and modern estimates are inferences" (§ Corduba) | none: the text says no ancient source gives the year | OK. Dot sits at 4 BC (house rule) |
| about 31, Return from Egypt (modern dating) | "Modern biographers … date his return to that voyage, about 31; Seneca says neither outright" (§ Illness, Egypt) | Consolation to Helvia 19.4–7 for the voyage | OK. "about" is kept |
| AD 39, Nearly killed by Gaius (Dio) | "Dio 59.19.7–8, under 39" | Dio 59.19.7–8 | OK |
| Span CORSICA, 41–49 | heading "Corsica, 41–49"; exile "within months of Claudius' accession in 41" | Dio 60.8.5; recall in 49, Annals 12.8 | OK. The label carries its years |
| Span TUTOR AND MINISTER, 49–62 | recall and tutorship in 49 (Annals 12.8.2); Burrus died in 62 and "Seneca's power broke" (14.52) | 12.8; 14.52 | OK |
| Span WITHDRAWAL, 62–65 | heading "Withdrawal, 62–65" | 14.52–56, 15.45 | OK |
| October 54, Nero emperor | "When Nero succeeded in October 54" | none: Annals 13.2 is cited for what follows, not for the date | OK. The month is kept |
| AD 56, Suffect consul | "Seneca was suffect consul in 56." | none | OK |
| AD 58, Suillius' attack | "In 58 the old prosecutor Publius Suillius … attacked Seneca openly" | Annals 13.42 | OK |
| March 59, Agrippina killed | "In March 59, when the collapsing boat had failed, Nero summoned the two men"; "urged the murder" (Dio 61.12.1); "After killing his mother" (15.62) | Annals 14.7, 14.11.3 | OK. The month is kept |
| AD 64, Second request to retire | "After the fire of 64 he asked again to retire"; self-test: "after a second refusal in 64" | 15.45.3 | OK |
| AD 65, Ordered to die | "The death in 65"; "In April 65 Piso's conspiracy was betrayed"; the tribune "found him at a villa" | 15.60–64 | **Fault (b)** |

The events run in the text's order. Dot spacing is proportional: about 9 px a year between the AD 41 and AD 65 ticks, and the 56, 58, March 59, 64 and 65 dots fall where they should. Nothing is clipped or overlapping in either theme. The three span colours and the leader lines read clearly in dark and light. Phone frames 1 and 2 overlap around AD 31 and together show the whole axis.

**Faults**

(a) The caption says the figure draws on "this report's first five sections and its account of the death". The withdrawal span (62–65) and the AD 64 second request come from the sixth section, "Withdrawal, 62–65". The sections run Corduba; Illness, Egypt; Corsica; Tutor and minister; The fortune; Withdrawal.

(b) "Ordered to die" claims something the text never says. The text gives Nero's wish for a pretext, the tribune finding Seneca, the refused tablets and the death, but it never states that Seneca was ordered to die. The caption itself calls this item "the death".

(c) Minor, for exactness: the caption says "the accession of 54", but the figure gives "October 54", which is also the text's date.

**Fix**

- Event label: change "Ordered to die" to **"Death at his villa"** (or simply "Death"), date AD 65 unchanged. If the writer would rather keep "Ordered to die", the text needs a sentence such as: "Silvanus brought Nero's order that he die (15.61)." That passage can be added only if the writer checks it against Tacitus. The checker has not sourced it.
- Caption, replacing the first sentence and the last: "Seneca's life in dated events and periods, from this report's first six sections and its account of the death. … The accession in October 54 and the consulship of 56 are given in the text without a passage."

Renderer note (does not decide the verdict): the "AD 65" axis tick label sits about two years left of its year, apparently pulled in from the column edge, so it stands nearer the AD 64 dot than the AD 65 dot. Each event carries its own date below the axis, so nothing is misread. Fixing it would mean centring edge tick labels on their tick in the renderer, not changing this figure's data.

## Figure 2 (flow): PASS

**Trace, drawing to text** (section "The death in 65: a Socratic performance")

| # | Box | Text | Passage |
|---|---|---|---|
| 1 | The tribune arrives: villa four miles from Rome | "The tribune Gavius Silvanus … found him at a villa four miles from Rome" | 15.60–61 |
| 2 | The image of his life: left to his friends | "he left them … the image of his life (imago vitae suae, 15.62)" | 15.62 |
| 3 | Arms cut: with Paulina | "Paulina chose to die with him, and both cut their arms" | 15.63 |
| 4 | Legs and knees cut: Paulina taken away | "he cut the veins of his legs and knees; … he had her taken to another room" | 15.63 |
| 5 | Dictation: words published | "called secretaries and dictated at length; Tacitus declines to paraphrase the words, since they had been published (15.63)" | 15.63 |
| 6 | The Athenian poison: fails | "the poison … used to kill those condemned by the public court of the Athenians; it failed" | 15.64 |
| 7 | Warm pool: libation to Jupiter the Liberator | "He entered a pool of warm water, sprinkled the slaves … offered the liquid to Jupiter the Liberator" | 15.64 |
| 8 | Steam bath: suffocates | "Carried into a steam bath, he suffocated." | 15.64 |
| 9 | Cremation: without ceremony, by codicil | "cremated without ceremony, as he had directed in a codicil" | 15.64 |

The nine stages follow the text's order exactly. The flow kind fits a single linear sequence, and the wrap connectors (box 4 to box 5, box 8 to box 9) read correctly. The caption names a passage for every item: arrival 15.60–61, image 15.62, "the veins and dictation" 15.63 (covering boxes 3–5), poison, pool, steam bath and cremation 15.64. It claims nothing the figure does not show. The figure has no dates or numbers to qualify. All box text fits, with no clipping or overlap, in dark and light. Phone frames 1 and 2 overlap at column 3 and together show every box.
