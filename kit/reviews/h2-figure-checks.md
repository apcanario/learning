# H-2 figure checks (1 Nov 2026)

Fresh Opus 5.5 agents (P31), one per changed unit figure, each given only the unit's text (figures taken out), the figure as drawn at desktop and in a 390 px frame, and the texts it draws; none saw the renderer being changed. 46 figures: Greek 5.4's timeline (P63), IA2's cross-surface map (P66), IA2's notation legend (ligature fix), and the 43 matrices P53 resized (four more joined after the row-label column rule). Every drawing FIX was fixed in the renderer and re-checked by a new agent; every figure that changed after its PASS (compared by rendering it at its PASS commit) was re-checked. 66 checks in all.

## Drawing: all PASS, or accepted where the width does not exist

- PASS: every figure checked, except the three below.
- Greece 9.1 figure 1 (the orders): the Frieze cell keeps three balanced lines; the table fills the width and every other column sits at its own line count, so no width can move to it without adding a line elsewhere.
- Greece 2.2 figure 4 (Olympian contrasts): one-line Cult and Place cells would need 663 units of a 579-unit share; both stay on two balanced lines.
- Rome 3.1 figure 3 (the assemblies): nine columns at their narrowest unbroken width and the row labels need 763 units; the figure scrolls on desktop with the cue, as it did before H-2 (760).

## Renderer fixes the checks led to

- Greek 5.4: a 700-unit timeline overflowed its 698 px desktop frame by 2 px, under the fade (theme 4i: base-width timelines and flows fit the desktop frame).
- IA2 notation legend: "->" drawn as an arrow ligature (theme 4i: no ligatures in figure text).
- IA2 cross-surface map: two labels side by side near a crossing (objects: each label at least 14 units clear of crossings, other lines and labels already placed).
- Matrices: a cell capped at 220 units leaving a word alone; row labels wrapping beside empty width; headers with one word on a line; a label column wider than its wrapped lines; a header broken mid-word ("COUNTER-PEN / ALTY") by the column rebalance; a caption breaking a number range at its dash; a nine-column matrix far wider than before. Fixed: no cell cap; row labels up to 240 on one line; headers and labels take the width the columns leave; long columns share in proportion; wrapped text balanced; a wrapping label column keeps only its balanced width; every wrapping column may take width that costs no other cell a line; a header keeps its longest word whole and a word breaks after its hyphen first; a wide matrix takes each column's narrowest unbroken width; caption number ranges joined.

## Data findings (not fixed: no unit's text or figure declaration changes in H-2 beyond Greek 5.4's revolt and IA2's map; proposed row P76)

- IA1 figure 2 (Garrett's planes): Strategy and Surface rows place one content in both columns; §1.4 gives no column placing for them.
- IA2 figure 1 (notation legend): the Screen row omits "a button is a control"; the Surface: Label row omits "in lower case"; no row for "nothing is drawn dashed"; the caption omits WCAG 2.2, 1.4.1 and credits the tones to Garrett and Brown, while §5.1 says tones were added.
- IA2 figure 8 (cross-surface map): "perqo.com: Benefits budget" is not in IA2's text; no counts on the object-to-object lines; "approves in Approvals" lacks its [over the limit] condition; "contract, sign in", "download, help" and "invites, decisions" are nouns where §5.2 asks for verbs; the surfaces' actions come from IA1 and are not in IA2; the caption's "F1" and "IA1, section 5" differ from the passage's citations.
- Greece 2.2 figure 4: the caption states "real in ritual but constantly crossed" as fact; the text gives it as the current scholarly view.
- Greece 4.1 figure 2 (Iphigenia): the cause column inherits the row tone, which is the "sacrifice" key; Homer's "neither" cell takes the sacrifice tone.
- Greece 8.4 figure 4: the caption drops "Archaic and Classical" and "with dining" from Ekroth; the row label "Altar" covers the pit or hearth.
- Greece 8.5 figure 3: "Boys from about seven" (Sparta: "from seven"); the caption omits Clouds 961–983.
- Greece 9.1 figure 1: the Corinthian proportion is blank while base, flutes and frieze read "as Ionic"; the caption credits the values to Vitruvius.
- Greece 9.1 figure 4: the caption promises "each Parthenon subject" and draws metopes and pediments only.
- Greece 10.2 figure 3: the Cypria's moral-weight cell is blank though the text gives it.
- Greece 12.2 figure 3: "a journey" omits "to the dead".
- Greece 12.6 figure 3: the caption ties "quoting his On Choices" to 10.136–137 as a whole.
- Rome 2.1 figure 4: Quirinus "fertility, people" drops "wealth".
- Rome 4.1 figure 1: Trogus' motive omits "to save her city".
- Rome 4.1 figure 3: the caption's "cites no ancient source" overstates; "chief gods" where the text calls only Baal Hammon chief.
- Rome 4.2 figure 1: "2,200 talents" omits "Euboean".
- Rome 6.1 figure 2: "refused" for morals omits 19, 18, 11; the row label omits "laws".
- Rome 7.3 figure 1: "Invention" and "Hostile, sound" overstate; the caption's "second-century lives" claims more than the seven graded.
- Optional notes, no conflict: Greece 10.8 figure 4's key "a hero-shrine there" for Podalirius; Rome 13.1 figure 2's Arius wording and bare "Crassus"; Rome 8.5 figure 1's key swatch takes one row's colour; IA1 figure 4's "help, download" tone has no key entry; Rome 6.4 figure 3's "Africa only, from 11 BC".
