Verdict: FIX

I used only the files in the p95-checkB folder: the three page HTML files, the text and object files, theme-relief-rules.css, uses.json, and every screenshot at all six widths in both themes plus all 15 pose shots.

## Findings

1. **should-fix · read-a5 · fidelity: the microphone drawing is a different kind of microphone from the one the text uses.**
   - The drawing is the generic stand or podcast microphone: a capsule held in a U-shaped yoke on a stem (see `shots/read-a5-390-dark.png` and `read-a5-pose*.png`).
   - The text's microphone is a clip-on lavalier ("lav"), and its kit leaves out any other kind. From `read-a5-object.md`:
     - "One phone, one tripod, one lav"
     - "One lavalier microphone."
     - "[ ] Kit: phone, tripod, one lavalier with a windshield for outdoor sessions"
     - "Lav clipped about 25 cm from the mouth"
     - "the phone's own microphone records the room"
   - The page discusses microphones at length (31 sentences), but every one is a lav or the phone's built-in microphone. The drawing shows a type of microphone the unit never prescribes, so a reader could take it as part of the kit.
   - The root cause is in the library entry, not the page. In `read-a5-object.md`, `outlines.json` maps the keywords "lav" and "lavalier" to `microphone-fill.svg`. When the reliefs roll out (P96), every page that mentions a lav would get this stand microphone.
   - Fix, either of:
     - Use a lavalier or clip-on microphone outline from an open icon set, as a separate library entry, and remove "lav" and "lavalier" from this entry's keywords.
     - Keep this outline, remove those two keywords, and change the caption so it does not suggest the unit's microphone, for example "A microphone, the common symbol; a stylised outline. Icon: …".

2. **minor · rm14 · fidelity: the wolf's expression doesn't match the text's wolf.**
   - The Lorc wolf-head is a snarling head with bared teeth (`shots/rm14-pose0.png`).
   - The text's wolf is the nursing she-wolf: "A she-wolf coming down to drink heard the crying, suckled them and licked them"; also "Romans displayed the wolf with evident pride."
   - Nothing in the text says how the wolf looked, so this contradicts nothing. The caption, "A wolf's head, a stylised outline", is accurate and does not suggest evidence.
   - The tone is off, though. A calmer wolf outline would fit better if one exists in the sets. No change is required.

3. **minor · rm14 · rendering: the wolf is the least legible of the three.**
   - The jagged inner levels interlock, so at 1x (768 and 1280, especially light: `shots/rm14-768-light.png`, `rm14-1280-light.png`) the cheek and ruff area reads as dense hatching. The lines are still separate and the eye and teeth are readable, so this is not merging into bands.
   - At 320–430 px (2x shots) it is clear.
   - If it is worth changing, use fewer inner levels or a wider level step for this outline.

## Checked with no finding

1. **Placement (all three):** in each HTML file, line 5 is `<p class="scope">…</p><figure class="relief-fig">…</figure>`. Line 6 closes the header, and line 7 opens the `div.stepbar`, the section bar. Every shot shows the order scope → relief → caption → section bar, and nothing else in the header looks displaced.
   - I had no before-build page to compare against, so "nothing else moved" rests on the shots looking normal.
2. **Caption:** each matches its library entry exactly and reads correctly:
   - "The wooden horse, a stylised outline. Icon: Delapouite, game-icons.net, CC BY 3.0."
   - "A wolf's head, a stylised outline. Icon: Lorc, game-icons.net, CC BY 3.0."
   - "A microphone, a stylised outline. Icon: Phosphor Icons, phosphoricons.com, MIT."

   Style: `.viz figcaption,.relief-fig figcaption` share one rule (`theme-relief-rules.css` line 22). The caption is outside the `div.topo`. On phones "game-icons.net" wraps at its own hyphen, which is acceptable.
3. **Fidelity, m43:** the page discusses the horse at length:
   - A section is titled "The Wooden Horse: Laocoön, Sinon, Cassandra".
   - "Epeius, by Athena's design, builds the Wooden Horse."
   - "the Trojans breach their own wall to bring the horse in"
   - "the Iliou Persis opens with the Trojans debating the horse"
   - "Laocoön … hurls a spear into the horse's flank"
   - "the Mykonos relief pithos (c. 670 BC) already shows the Wooden Horse with warriors visible through portholes"

   The drawing, a horse on wheels with a hatch, contradicts nothing in the text, and the caption marks it as stylised rather than evidence.

   rm14 also discusses its object at length: there is a whole "earliest evidence" section on wolf and twins objects.
4. **Rendering, all 36 page shots:**
   - Each frame matches its outline's aspect: `--ar` .9729 for the horse, 1.0718 for the wolf, .7457 for the microphone, and the pose crops measure 546×562, 602×562 and 418×562.
   - On phones the frames stay within the column and 280 px; from 768 px they stay within 340 px.
   - Nothing is cut, and there is no sideways scroll.
   - The halo is visibly fainter (`.rl-out` uses `stroke-opacity: var(--topo-rh)`).
   - Each drawing takes its page's tone: red `ct-t1` for Greece, purple `ct-t5` for Rome, teal `ct-t3` for Personal brand.
   - Contrast is reasonable for decoration in both themes.
5. **Poses, all 15 shots:** at every pose all lines, including the halo, stay inside the frame with a margin, and nothing is clipped. Motion runs only under `prefers-reduced-motion: no-preference` (css line 16), so the drawing is still under reduced motion.
6. **Markup, all three:** each figure matches, in full, a strict pattern:
   - `figure.relief-fig` > `div.topo.relief` with `aria-hidden="true"` and a style that sets only `--ph` and `--ar`.
   - Inside it, one `svg.topo-l ct-tN` with `viewBox`, `preserveAspectRatio`, `xmlns` and `focusable`.
   - Exactly one `path.rl-out` and one `path.rl-in`, each with only `class` and `d`.
   - No text inside the drawing, then the `figcaption`.

   Each SVG is under 11,000 characters, so all are under 12 KB. The microphone's is under 5,000.
   - The figure and div also carry `data-outline`, which seems harmless.
