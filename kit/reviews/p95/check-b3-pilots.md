Verdict: PASS

Scope: I read every text file in p95-checkB3: README, previous-report, changes, uses.json, theme-relief-rules.css, the three object files, line 5 of each page's HTML in full and the caption and placement spans of the text files. I viewed shots at every width for at least one theme per page, both themes for each page, and 13 of the 15 pose shots (m43 and read-a5 at all five poses, rm14 at 0, .25, .5, .75 and 1). Nothing from outside the folder was used as a source.

## Earlier findings (second check)

1. **read-a5, phone drawn upright (minor): settled, and the reason is sound.**
   - The text never describes the phone's look. Its talk of a "horizontal frame" and "3840 × 2160" is about framing, not the object.
   - The caption claims only "A phone".
   - changes.md has a garbled sentence ("turning it would be a change to the drawing that;"), and its claim that the row "forbids editing an outline" is not in the README's verbatim rule. A rotation done by the renderer from data would still meet the design rule. But the main reason, that nothing in the text is contradicted, holds on its own.
2. **"phone" keyword false hits (minor): resolved for the cases named.**
   - The phone entry in read-a5-object.md now has `"excludes": ["phone (?:fields?|numbers?|line|volume)"]`.
   - A5's count fell from 15 to 13 (`courses/brand-ai/A5-production-craft.md`, 13).
   - "uploaded from a phone" / "2 MB from a phone" (the thumbnail-limit sentences) are still counted. This does not affect the pilot (see new finding 2).
3. **CC BY attribution for an adaptation (minor): resolved.**
   - All three captions now say the relief is "drawn as a relief from an icon", followed by the entry's credit.
   - Each licence word links to `licence_url`: CC BY 3.0 to https://creativecommons.org/licenses/by/3.0/, and MIT to the Phosphor LICENSE at commit 2b75f3a…. Both have `target="_blank" rel="noopener"`.

The two minors settled in the first round (rm14 wolf's expression, rm14 density at 1x) are still settled. rm14-768-dark and rm14-1280-light still look dense around the ruff, but the lines stay separate.

## Current pages, checked with no defect

1. **Placement.**
   - In m43-page.html, rm14-page.html and read-a5-page.html, line 5 is `<p class="scope">…</p><figure class="relief-fig">…</figure>`, line 6 is `</header>`, and line 7 opens `div.stepbar`.
   - In each *-text.txt, the scope sentence runs straight into the caption and then "Section 1 of N", with nothing else inserted.
   - The shots show scope, then relief, then caption, then section bar at every width.
2. **Caption.**
   - "The wooden horse, a stylised outline drawn as a relief from an icon. Icon: Delapouite, game-icons.net, CC BY 3.0."
   - "A wolf's head, a stylised outline drawn as a relief from an icon. Icon: Lorc, game-icons.net, CC BY 3.0."
   - "A phone, a stylised outline drawn as a relief from an icon. Icon: Phosphor Icons, phosphoricons.com, MIT."
   - Each credit equals the entry's `credit` plus a full stop. Grammar and capitals are correct.
   - The caption uses the figure caption's style, through the shared selector `.viz figcaption,.relief-fig figcaption` (css line 27).
3. **Fidelity.**
   - m43 has a whole section, "06 The Wooden Horse: Laocoön, Sinon, Cassandra", which opens: "The Iliou Persis opens with the Trojans debating the horse: throw it from the cliff, burn it, or dedicate it to Athena." Other sentences: "Epeius, by Athena's design, builds the Wooden Horse." and "the Mykonos relief pithos (c. 670 BC) already shows the Wooden Horse with warriors visible through portholes".
   - rm14: the she-wolf runs through §2, §6 and §7 ("A she-wolf coming down to drink heard the crying, suckled them and licked them"; "Objects take the wolf and twins a century further back."; the Capitoline wolf, "The wolf alone; the twins were added after 1471"). The scope line itself names "the wolf".
   - read-a5: §1 is headed "One phone, one tripod, one lav", followed by "The phone on a tripod."; "record at 3840 × 2160 when the phone allows it"; "Lav off for sparring; the phone records the room."
   - None of the three drawings contradicts its text. "A stylised outline … from an icon" makes clear that none is evidence.
4. **Rendering.**
   - Every frame is at its outline's aspect (`--ar` .9729, 1.0718, .7204).
   - On a phone each frame fits the column and is at most 280 px tall. At 320 px the wolf is limited by the column's width and stays inside the gutter (rm14-320-dark). The phone is about 242 css px tall (read-a5-320-dark).
   - From 768 px each frame is at most 340 px tall (read-a5-768-light, m43-768-dark).
   - Nothing is cut, and there is no sideways scroll at 320, 360, 390, 430, 768 or 1280 in either theme.
   - The halo is fainter in both themes. The colours are ct-t1 red, ct-t5 purple and ct-t3 teal, matching each page's eyebrow.
   - The lines stay separate. The phone's dark-theme halo is very faint, which is acceptable for a decorative drawing.
5. **Poses.** In every pose shot viewed, every line, halo included, stays inside the frame with a margin, including m43 pose0 and pose1 (the head and rear wheel) and rm14 pose1 (the ear tip and the left tuft).
6. **Markup.**
   - Each figure is `figure.relief-fig` > `div.topo.relief[aria-hidden="true"]`, with a style that sets only `--ph` and `--ar`.
   - Inside the div is one `svg.topo-l ct-tN` holding exactly one `path.rl-out` and one `path.rl-in`, each with only `class` and `d`. There is no text in the drawing.
   - Size: each SVG is under 7,000 characters (a bounded grep matched all three), so well under 12 KB.
   - The `figcaption` comes after the div.
   - Motion runs only under `prefers-reduced-motion: no-preference` (css line 21), so the drawing is still under reduced motion.

## New findings

1. **minor · all three captions · wording.**
   - "…drawn as a relief from an icon. Icon: Lorc…" repeats "icon. Icon:".
   - It is correct and meets the licence purpose, but it reads a little clumsily on a phone (three lines at 320 px).
   - Optional fix: "…drawn as a relief from an icon by Lorc, game-icons.net, CC BY 3.0." That would need the credit field reworded in the renderer, not by hand.
   - The row's verbatim example ("An amphora, a stylised outline. Icon: …") and any verifier rule built on it should be updated to the new pattern before P96, so the rollout and verify.py agree. I cannot check verify.py from this folder.
2. **minor · library (P96) · "from a phone" still counted.**
   - read-a5-object.md still lists "up to 2 MB when uploaded from a phone" and "2 MB from a phone or 50 MB from a computer". Neither is about the object being filmed with.
   - The A5 pilot clears the bar without them.
   - Before P96 thresholds pick pages, check the per-page counts by hand, or add "from a phone" to the excludes.
3. **minor · uses.json · stale example in "about".**
   - It says "a history report m61, rm14", but the mapping uses m43.
   - Fix: change "m61" to "m43".

## Not verifiable from this folder

- Whether the theme/row text and verify.py now expect the new caption wording.
- Whether anything outside the header moved: there is no before-build page. The text files and shots show nothing out of place.

## For memory

Nothing new about the user came up in this check.
