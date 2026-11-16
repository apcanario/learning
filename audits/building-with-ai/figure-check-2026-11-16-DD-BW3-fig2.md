# DD-BW3 figure 2 (matrix) — figure check

Model: claude-opus-5-5

Verdict: FIX (one legend string; everything else passes)

## (a) Cells against the text
- Badly put / Outcome "redone", Turns "corrections", Two tasks "yes": l.97 "chats with two or more corrections; chats marked "two tasks"; chats whose outcome is "redone"." Supported.
- Badly put / Task type "group": l.101 "if the heavy chats are mostly one task type, the fix is that type's brief". Supported as a read by task type.
- Wrong tool / Routing "yes": l.105 "the routing column". Model "tier": l.105 "among the chats on your heaviest model"; l.107 "another tier". Outcome "redone": l.107 "a light model on a task the routing table puts higher, where the outcome is "redone"". Supported.
- Wrong tool / Task type "group": l.105 "those whose task type your routing table puts lower" uses the task type as a filter (compared with the routing row), not to group the count. The legend "used to group the count by task type" claims more than the text says for this row. FIX.
- By hand / Procedure "yes": l.113. Paid twice / Repeat research "yes": l.121. Supported.
- Column labels match the sheet's labels (l.59-85). Row labels match the four §3 headings.

## Replacement
Change only the legend string for the blue swatch:
  from: "used to group the count by task type"
  to:   "read against the task type"
(Supported for Badly put by l.101 "Then check the type" and for Wrong tool by l.105 "those whose task type your routing table puts lower".) No cell changes. If the JSON keys the legend, e.g. {"legend":[{"swatch":"yes","text":"the column that counts the pattern"},{"swatch":"group","text":"read against the task type"}]}.

## (b) Caption
Says what it shows, names §3 and marks it stated opinion, names where the fixes are taught (BW2, BW3 §6, BW8 §4 and §7, BW10 rule 6; all in §3 text). PASS.

## (c) Kind
Patterns x columns with marked cells: matrix fits. PASS.

## (d) Rendering
Desktop dark/light: whole figure fits, legend and caption readable, no overlap. Phone widths (320-430) and tablet: opening frame readable, "scroll sideways" hint shown, every column reached by the last frame, no clipped cell text. The legend sits inside the scrolled area, so on phone frames 2-4 its text slides partly off the left edge; it is whole in the opening frame. PASS (minor).
