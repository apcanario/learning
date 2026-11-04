## Findings

No errors and nothing to mark should-fix. The minor points follow.

1. **minor.** Two names for one course on the home. Course B's tile is titled "Using AI to Build a Brand". The New since row for DD-B2 calls the same course "Building with AI" (`home-markup.html` l.50–55 against l.82). That row name is `sources.courses.brand-b.short` in `data-extract.json`. Nothing else on the home uses "Building with AI", so a reader meets a course name with no tile. This row format is older than P92: P91 set it.

2. **minor.** The UX tile title is "Information **A**rchitecture" (`home-markup.html` l.62). The brief, `sources.newest.course` and every New since row say "Information architecture". The other titles mix their casing as well: "Greek history and mythology" against "Building a Marketable Personal Brand". The capitals read unevenly across the five tiles.

3. **minor.** History's count is a different kind of count from the other three. History says "2 courses · 157 reports · 8 planned"; the others say "1 course · N of M units" (`home-markup.html` l.13, 41, 50, 59; shots 768/1280). Each is true for its track, but the headers are not parallel. The data has no source for the 157 reports, so I could not check it. The 1280 sidebar does show 78 + 79.

4. **minor.** At 430 px the folded "Why history and myth together" summary is cramped. The title wraps to two lines and its sub-label ("the method of / the track") wraps to two lines beside it (`430px-home-{dark,light}-part2`). At ≤400 px the sub-label sits under the title (theme-excerpt l.53–54), and at 768 px it fits on one line. 430 is the one phone width where the block looks squeezed.

5. **minor.** Within a course, a patch's ring count does not always rise with words. In course B, B7 has 7,710 words and 3 rings, while DD-B1 has 7,639 words and 4 rings (`data-rings` in `home-markup.html` l.55). In Rome, U6 has 11,901 words and 1 ring, though 5 × 11,901 / 34,974 is 1.70. This looks like neighbouring rises adding together in the field. The rises themselves are correct by words. Only the ring count, as a reading of size, is uneven.

6. **minor (taste).** On a phone, each track's header rule is followed about 30 px lower by the first tile's coloured top border. That gives two parallel lines in the track's tone under every area name, in all phone shots, part 1–3.

## Confirmed

- **Order** at all six widths, both motion states (`built.*.order`): hero, then four `section.track` (History, Marketing, Technology, User Experience, by id and in the shots), then "How every course works" (folded), then site links, then New since, then the What's new link last.
- **Area headers.** Below 768 px (320, 360, 390 and 430) `heads` is [label false, name true, lede false, count false] for all four, and the shots show the name only. At 768 and 1280 all four flags are true, and the shots show TRACK, the name, the lede and the count.
- **Tiles.** There are five, one per live course, under the right areas, and every tile has the same fields:
  - the chip (area and course) with the status pill under it
  - the title
  - a tile line of at most two lines (clamped; two lines in every shot)
  - three stats
  - the patch, aria-hidden "true"
  - the whole tile as an `<a>` to `#greece`, `#rome`, `#brand-a`, `#brand-b` or `#ux-ia`
- **Patches against the sources.** Rises, codes and words match `sources.courses` exactly, in order, at all 12 snapshots: Greece 13/0, Rome 14/0, A 11/0, B 11/0, IA 7 rises plus 8 planned (IA8–IA12, DD-IA1–3). The markup's `data-label`/`data-words` match too. Stroke and tone per course: Greece red, Rome purple, A teal, B purple, IA blue. Rome and B share purple, as given.
- **Patch sizing.** viewBox 720×180 (4:1) at every width. The patch fills the content width (`pw` = `sw`; `cw` − `pw` = card padding) at height `pw`/4, and the cropping this causes is 0.4% or less. There is no animation on a patch (`anims` lists only the hero).
- **Stats against the sources.** Units written and in-all totals match. Hours match total words at 250 words a minute: Greece 246,589 words gives 16 h; Rome 263,904 gives 18; A 74,284 gives 5.0; B 82,023 gives 5.5; IA 66,866 gives 4.5. Greece plus Rome equals History's 510,493.
- **Columns.** One column on every phone. Two from 768 px, with History's two tiles side by side at equal height. Marketing, Technology and UX tiles are each a lone half-width tile at 768 and 1280.
- **History blocks.** After the tiles come "Why history and myth together" (folded) and "Planned · 8 courses" (folded, with 8 entries: Egypt, Persia, Norse, Celts, England, Scotland, China, Japan).
- **New since.** Its six rows match `sources.new_since_rows` in order. The heading "New since 2 Nov" names the oldest row's day. There is one What's new link, the last block.
- **Site links.** Backlog, Figure kinds and Changelog go one to a row at 320–430 and three across at 768 and 1280. They go to `#backlog`, `#viz-examples` and `#changelog`.
- **No sideways scroll.** `scroll` equals the viewport at every width.
- **Nothing cut.** No text, tile, patch or link is cut at an edge in any shot. The hero copy and the What's new button sit inside the column at every width.
- **Light theme.** The page is warm grey-cream, cards are a shade lighter, ink is near-black, and the track bands are faint tints. I saw no pure-white surface (from the shots; I measured no pixels).
- **verify.py.** Lines agree with the extract (tiles, heads, 6 rows, first area, page width) and end ALL CHECKS PASSED.

## Renderer notes

- The phone and tablet shots are at device scale 2, so the images are twice the CSS size. The 1280 capture shows the sidebar only for its first screen, as the brief warns. Cuts between parts are the shots' own. For example, IA4's row is split between parts 3 and 4 at 320–430, and that is not a page fault.
- Hero items outside this check, seen in passing: the hero contour layer bleeds off the right edge by design; at 1280 the area line breaks after "Marketing ·" at 34 px; and the lede still says "Pick up where you left off." although the home has no Continue.
- I could not verify the colour of the chip text on the filled chips (white or off-white) from the images.

**PASS**
