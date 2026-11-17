# cp3-1 figure re-check (key renames)

Checker: claude-opus-5-5, fresh agent. Read figures.md, text/ (three units) and all 18 sheets (1280 px dark/light whole; 390 and 320 px frames split per frame, first and last frames read, key band of every width x theme combination read).

| Figure | Verdict | Notes |
|---|---|---|
| read-ia6 fig 5 (screen states) | PASS | (1) Keys print "app / the Perqo app" and "stop / the path ends without success here"; no tone name. (2) app swatch = teal cells, stop swatch = brown cells in both themes; the brown cells are exactly the caption's stops (Home empty and error; Category empty; Claims, Purchases error; New claim error; Check and submit error; Card empty). (3) Caption: "tone 3, the app, keyed 'app'; tone 6 ... keyed 'stop', a state in which the path ends without success" agrees with the keys; page note says only the caption changed, and no legend sentence exists in the text. (4) Every row label and cell matches B.5's table (row labels drop the A- identifiers; blank cells = "none", as the caption says). (5) Keys whole and readable at 320, 390, 1280, dark and light; the stop label wraps to two lines at 320/390 without clipping. |
| read-dd-ia2 fig 3 (measurement model) | PASS | (1) Keys "shared / a method serves any surface", "perqo.com / the Help centre's search", "Admin / Perqo Admin's records". (2) Purple = M-01 to M-05, M-11 (leading); red = M-07, M-12 to M-14 (Help centre log); blue = M-15 to M-19; matches. (3) Caption and section 3.4's sentence quote the three keys verbatim. (4) All 15 rows and every cell match the section 3.4 list. (5) Keys whole at every width and theme. Minor, no fix: M-15's data is support's ticket tags, which the key groups under "Perqo Admin's records"; the text itself puts M-15 in "Lagging, Admin" and in the tone-4 rows, so figure and text agree. |
| read-dd-ia3 fig 1 (taxonomy vs navigation) | FIX | (1) Keys "taxonomy / shared, under every surface", "navigation / the Perqo app's examples". (2) Purple = taxonomy column, teal = navigation column; matches. (4) All eight row labels and sixteen cells match section 1.2. (5) Keys whole at every width and theme. (3) Caption opens its colour sentence with "Rows tone 5;", which nothing in the drawing shows (the row labels are uncoloured and the navigation column is tone 3), and it glosses navigation as "the Perqo app" where the key and the page text say "the Perqo app's examples". |

## FIX

**read-dd-ia3 figure 1, caption**

Current: `Rows tone 5; the taxonomy column tone 5, shared, keyed 'taxonomy'; the navigation column tone 3, the Perqo app, keyed 'navigation'.`

New: `The taxonomy column tone 5, shared, keyed 'taxonomy'; the navigation column tone 3, the Perqo app's examples, keyed 'navigation'.`

## Outside the figures (page text, not a figure verdict)

- text/read-dd-ia2.md, note after figure 3: "the caption and the sentence before the metric list say says so" → "the caption and the sentence before the metric list say so".
- text/read-dd-ia3.md, note after figure 1: "the caption and the sentence before it say says so" → "the caption and the sentence before it say so".
