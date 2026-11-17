# P84 and P109 · timeline spans on the axis, matrix keys (row H-4, 16–17 Nov 2026)

The chat ran as Opus 5.5 (claude-opus-5-5) and wrote the kit code itself; every re-check was a fresh Opus 5.5 agent on a packet staged by `stage.py` (the page's text with its figures removed, each figure's caption, and the frames sheets `shots.py` saved with verify.py's `frames()` at 320, 390 and 1280 px, dark and light; the declaration for a course-home or examples figure). Each agent stated claude-opus-5-5. Most agents' harnesses refused their write to `out/`; their reports here are their final replies, saved verbatim by the chat (marked so at the top).

Changed figures were listed by script each round (`changed.py`, every figure of every built page compared with the build before): `changed-figures.txt` (round 1: 138 timelines and 4 examples), `../p109/changed-figures.txt` (9 matrices), `round2-changed-figures.txt` (183), `round3-changed-figures.txt` (73, with the wide matrices whose look changed only by the theme), `round4-changed-figures.txt` (25), `round5-changed-figures.txt` (2). Declaration fixes were applied by `apply_round1.py` to `apply_round4.py`, exact replacements inside viz blocks only (prose never touched), plus the Rome course home in `kit/courses.py` and the A8 and DD-PB2 notes.

| Round | Figures | PASS | FIX | What the FIXes changed |
|---|---|---|---|---|
| 1 (P84) | 142 | 101 | 40 | 36 declarations; renderer round 2 below |
| 1 (P109) | 9 | 2 | 7 | renderer: keys out of the scroller; matrices up to 15 % over 700 scale |
| 2 | 183 | 159 | 24 | 21 declarations and captions; renderer round 3 |
| 3 | 73 | 66 | 7 | 10 declarations; renderer round 4 |
| 4 | 25 | 23 | 2 | 4 declarations |
| 5 | 2 | 2 | 0 | — |

No figure was dropped. Renderer and theme changes, in `viz.py`'s docstring (P84, P84 round 2, P109 and its round 2) and `design/theme.css` 6.13 to 6.15: spans on lanes tied to the axis with end guides and gridlines; every span label carries its years (`span_text`, `span_names`: years, runs, decades, centuries, split years; a partial date stops the build); side labels wrap at 220 units with the date whole on the last line; in-bar labels wrap inside a taller bar; abutting spans stop short of their shared year; guides and gridlines break at bars and plates; edge tick labels keep their distance; no year 0; a timeline up to 15 % over 700 scales on a desktop (viz-snug); span labels keep their case; figure text drawn with geometric precision (Chromium cut a wrapped label's ascenders at 1280 px); matrix keys in their own svg under the frame; a matrix up to 15 % over 700 scales, a wider one pins its row labels on a desktop too. `verify.py` checks every span label names its years and every bar end has its guide to the axis.

The m12 figure 3 clipping (round 2 and 3) was found by the chat to be Chromium's text painting in a timeline scaled from 700 to 698 units: nothing in the drawing covered it; `text-rendering: geometricPrecision` on figure text cleared it (round 4 PASS).
