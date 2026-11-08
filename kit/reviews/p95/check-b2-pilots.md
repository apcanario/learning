Verdict: PASS

Scope: I read every file in p95-checkB2. That covers the three page HTML files, the text and object files, theme-relief-rules.css, uses.json, previous-report.md and changes.md. I also looked at the shots at all six widths for A5 in both themes, a spread of widths and both themes for m43 and rm14, and every pose shot that bears on clipping. I used nothing from outside the folder as a source.

## Earlier findings

1. **read-a5, microphone vs lavalier (should-fix): resolved on the page.**
   - uses.json now maps read-a5 to "phone".
   - The figure on read-a5-page.html line 5 draws the Phosphor device-mobile-fill outline. Its caption reads "A phone, a stylised outline. Icon: Phosphor Icons, phosphoricons.com, MIT."
   - The phone is the unit's camera and recorder, so the drawing fits the text:
     - The §1 heading is "One phone, one tripod, one lav".
     - "The phone on a tripod. One static camera set up before the warm-up and left alone. It does three jobs at once…"
     - "His rule: record at 3840 × 2160 when the phone allows it."
     - "Lav off for sparring; the phone records the room."
     - "Kit: phone, tripod, one lavalier…"
   - changes.md also says the microphone library entry now depicts "a stand microphone" and no longer has the keywords "lav" and "lavalier". That entry is not in this folder, so I cannot confirm it. The page-level fix is confirmed.
2. **rm14, the wolf's expression (minor): settled, and the reason is sound.**
   - The text never describes the wolf's look.
   - The caption claims only "a wolf's head".
   - The two alternatives named (lorc/wolf-howl, lorc/direwolf) were checked and rejected for stated reasons.
   - The search covered only game-icons. That is acceptable for a minor where no change was required.
3. **rm14, density at 1x (minor): settled, and the reason is sound.**
   - rm14-768-dark and rm14-1280-light still read as dense hatching around the cheek and ruff.
   - The lines stay separate, and at 320–430 px (rm14-320-dark, rm14-390-light, rm14-430-dark) the drawing is clear.
   - A level rule that is the same for every outline is a fair reason not to tune this one.

## Current pages, checked with no finding

1. **Placement.**
   - In all three files, line 5 is `<p class="scope">…</p><figure class="relief-fig">…</figure>`, line 6 is `</header>` and line 7 opens `div.stepbar`.
   - The shots show the same order on every page: scope, then relief, then caption, then section bar.
   - In read-a5-text.txt the scope sentence runs straight into the caption and then "Section 1 of 6"; nothing else was inserted.
2. **Caption.** Each caption is the entry's `credit` plus a full stop, prefixed by what it shows, and reads correctly:
   - "The wooden horse, a stylised outline. Icon: Delapouite, game-icons.net, CC BY 3.0."
   - "A wolf's head, a stylised outline. Icon: Lorc, game-icons.net, CC BY 3.0."
   - "A phone, a stylised outline. Icon: Phosphor Icons, phosphoricons.com, MIT."

   The licence words are now links:
   - CC BY 3.0 links to https://creativecommons.org/licenses/by/3.0/.
   - MIT links to the LICENSE file at commit 2b75f3a….
   - Both equal `licence_url` in their entries and carry `target="_blank" rel="noopener"`.

   The caption shares `.viz figcaption,.relief-fig figcaption` (css line 27).
3. **Fidelity.**
   - m43: the horse is discussed in a whole section, "06 The Wooden Horse: Laocoön, Sinon, Cassandra":
     - "The Iliou Persis opens with the Trojans debating the horse…"
     - "Epeius, by Athena's design, builds the Wooden Horse."
     - "…the Trojans breach their own wall to bring the horse in."
     - "the Mykonos relief pithos … shows the Wooden Horse with warriors visible through portholes."
   - rm14: 23 matching lines in the vault text, including the whole "07 The earliest evidence" section on wolf-and-twins objects.
   - None of the three drawings contradicts its text, and the caption "a stylised outline" keeps each one from passing as evidence.
4. **Rendering.**
   - Aspect: the frames match their outlines (`--ar` .9729, 1.0718, .7204). The pose crops measure 546×562, 602×562 and 404×562, which give ratios of .971, 1.071 and .719.
   - Size on a phone: within the column and 280 px. At 320 the wolf is limited by the column's width, and it stays inside the gutter.
   - Size from 768 px: at most 340 px.
   - Nothing is cut, and there is no sideways scroll at any width.
   - The halo is visibly fainter in both themes (`.rl-out` uses `stroke-opacity: var(--topo-rh)`).
   - Each drawing takes its page's tone: ct-t1 red, ct-t5 purple, ct-t3 teal.
   - The phone's few, widely spaced levels are the most legible of the three.
5. **Poses.** In every pose shot I viewed (read-a5 at all five poses; m43 and rm14 at 0, .5 and 1), every line, halo included, stays inside the frame with a margin.
6. **Markup.**
   - Each figure is `figure.relief-fig` > `div.topo.relief[aria-hidden="true"]` with a style that sets only `--ph` and `--ar`.
   - Inside that is one `svg.topo-l ct-tN` holding exactly one `path.rl-out` and one `path.rl-in`, each with only `class` and `d`.
   - There is no text in the drawing, and the `figcaption` comes after the div.
   - Size: the phone SVG is under 3,000 characters, and all three are under 9,500, so under 12 KB.
   - Motion runs only under `prefers-reduced-motion: no-preference` (css line 21), so the drawing is still under reduced motion.
   - `data-outline` is still on both the figure and the div, which is harmless.

## New findings

1. **minor · read-a5 · fidelity: the phone is drawn upright, but the unit films landscape.**
   - The text says "A3 §1 keeps the subject in the centre third of a horizontal frame so a vertical crop holds" and "record at 3840 × 2160".
   - The outline is an upright phone (read-a5-390-dark.png). The text never describes the phone's look, and the caption says only "A phone", so this does not contradict the text. A reader could still take it as a hint to film vertically.
   - No change is required. If wanted, a renderer-side rotation option in the outline's data would fix it without drawing by hand.
2. **minor · library (P96 rollout) · the keyword count for "phone" includes false hits.**
   - read-a5-object.md lists 17 lines. They include the caption itself, "made to sound like a bad phone line" and "Every line intelligible at phone volume", none of which is about the object.
   - outlines.json counts 15 for A5.
   - A5's real discussion of the phone clears the bar, so the pilot is unaffected. When the threshold picks pages in P96, "phone line" and "from a phone" style hits could push a page over it on passing mentions. Check the per-page counts by hand, or exclude "phone line" and "phone volume".
3. **minor · captions on m43 and rm14 · the attribution wording for derived icons.**
   - Both reliefs are adaptations of the icons (background removed, levels added), and the credit reads "Icon: Delapouite…".
   - From my own knowledge, not from any file in this folder, CC BY 3.0 asks that the credit on an adaptation say the work was adapted, for example "Relief after an icon by Delapouite, game-icons.net, CC BY 3.0".
   - The current wording follows the row's verbatim rule, so this is not a defect against the spec. Confirm it against the licence text before P96 repeats the wording on many pages.

## Not verifiable from this folder

- The microphone library entry's new `depicts` value and the removed keywords (changes.md item 1).
- Whether anything else on the pages moved: there is no before-build page to compare, so this rests on the shots looking normal.

## For memory

Nothing new about the user came up in this check.
