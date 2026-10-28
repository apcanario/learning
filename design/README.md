# design/

`theme.css` is the only place style is defined in the Learning Project. It is the Personal Mythology visual system (the history site's `shell.css` of 27 October 2026), with three fixes and the few components the hubs need that the history pages lack. Every page in the Project is built from it; no page carries its own stylesheet.

## Why it is inlined

A published claude.ai artifact cannot load an external stylesheet. So the generators read `theme.css` at build time and write it into each page's `<style>`. The consequence: **a change to `theme.css` reaches a page only when that page is rebuilt and republished.** There is no other way to propagate it.

## How to change it and propagate the change

1. Edit `design/theme.css`. Change a token in section 1 before touching a component; most changes are a token.
2. Copy it over the kit: `cp design/theme.css kit/shell.css`. The theme keeps every class name `shell.css` had, so `build.py` and `shell.js` need no change (verified 28 October 2026: no class undefined, `build.py` builds, `verify.py` passes).
3. Rebuild every hub: `cd kit && python3 build.py && python3 verify.py`; from `generator/`, `python3 build_hub.py data/brand-ai` → `hubs/brand-and-ai-courses.html`; any other hub: `python3 build_hub.py data/<slug>`.
4. Check each rebuilt page at 400 px wide in dark and light: no horizontal scroll, every control at least 44 px tall, light mode legible (the checks are listed below).
5. Republish each page to its existing artifact (never a new one). The links are in `docs/courses-index.md`.

## What is in the file

| Section | Holds |
|---|---|
| 0 Fonts | DM Sans (text), Space Mono (labels, codes), Gentium Book Plus (Greek and Latin display words), from Google Fonts |
| 1 Tokens | Dark (default) and the light palette, which is defined twice (system setting and toggle) and must stay identical in both places |
| 2 Base and type | Body, links, inline `code` |
| 3 Layout | Fixed frosted top bar (`.top`, `.ib`, `.cur`), slide-out drawer (`.drawer`, `.dlist`, `.ditem`, `.dunit`, `.dsec`), 700 px reading column, panel rhythm (`.panel.root/.home/.syl/.log/.stack`) |
| 4 Components (history) | Report (`.report`, `.toc`, `.dispute`, `.quiz`, `.carry`, `.prompt`, `.pager`, `.tbl`), home (`.hero`, `.lede`, `.stats`, `.howto`, `.ucard`, `.hrow`, `.pill`), syllabus (`.smod`, `.pbox`, `.copy`, `.rlink`, `.hbtn`), era ribbon, rule blocks and parts, root home (`.course`, `.ml`), changelog (`.clog`) |
| 5 Components (hubs) | `.dsec.hub` (Learn / Build group labels), `.ditem.sub`, `.howto.edge` (callout with a coloured edge: the pick, the review rule, a goal), `.stats[data-n="4"]`, `.course ul`, `.meter`, `.smod.deep` and `.smod .ships`, `table.order`, `.logrows`/`.logrow`, `.rlink.dim`, `small.url` |

## Tokens

| Token | Dark | Light | Role |
|---|---|---|---|
| `--bg` | `#0a0a0c` | `#f5f5f7` | page |
| `--card` | `#131316` | `#ffffff` | cards, drawer |
| `--line` / `--line-2` | `#1e1e24` / `#2a2a32` | `#e3e3ea` / `#cfcfd9` | borders |
| `--fg` / `--muted` / `--dim` | `#ececf1` / `#9a9aa6` / `#6b6b78` | `#17171c` / `#50505b` / `#6c6c78` | text, secondary, tertiary |
| `--red` | `#ff6b6b` | `#c23b3b` | Greece, Learn, disputes |
| `--purple` | `#9b5de5` | `#7a3fcf` | Rome, course B |
| `--orange` | `#f4a261` | `#a3580f` | Build, "unchecked" |
| `--teal` | `#2a9d8f` | `#1b7569` | links, course A, "written" |
| `--blue` | `#457b9d` | `#3a6a8a` | goals, "next" |
| `--gold` | `#e9c46a` | `#7f6308` | deep dives, labels, audits |
| `--on-accent` | `#0a0a0c` | `#ffffff` | text on a filled accent button |

Dark accents are the house palette and do not change. No grey is a dominant accent.

## Rules for pages

- A page's only `<style>` is `theme.css`, inlined by a generator. No `style` attribute except to set a custom property (`--c` item colour, `--cc` course colour, `--hc` callout colour) or a progress width.
- Every page carries `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`. Without it phones lay the page out 980 px wide (the v5.1 Brand + AI hub had no viewport tag, which is why its 44 px targets measured 32 to 40 px on a phone).
- New component: first check section 4 for one that already does the job (most hub needs were met by `.howto`, `.smod`, `.hrow`, `.course`, `.pill`). If none does, add it to section 5 with a one-line comment, using tokens only.

## Fixes made in the theme

The hub template satisfied three rules the history CSS broke; each was fixed here, not in a page.

| Rule | Was | Now |
|---|---|---|
| 44 px targets | Report section links (`.toc a`) and every `<summary>` (Answer, Model answer, The prompt this answers) were 32 px tall, on all 137 report pages | 44 px |
| Light mode designed, not inverted | Light accents and tertiary text below 4.5:1 on the page: red 4.2, orange 3.8, gold 3.7, teal 4.4, dim 3.1 | Every accent and `--dim` at 4.7 to 5.3:1 on the page and higher on cards; muted text darkened to keep the hierarchy; white text on filled buttons at 5.2:1 or more |
| No horizontal overflow at 400 px | A long URL in a link could widen the page | `overflow-wrap:break-word` on the body (tables still size as before), `anywhere` on report links and URL lines; tables and code scroll only inside their own container |

Checked on 27 October 2026 with Chromium at 400 px, dark and light, every panel of both hubs with every disclosure open: no page wider than the viewport, no control under 44 px, no console error.

## Checks before republishing

At 400 px wide, in dark and in light, on every page with every `<details>` open: the document is not wider than the viewport; no button, summary or block link is under 44 px tall; text tokens keep at least 4.5:1 against `--bg` and `--card`. `python3 generator/check_page.py generator/hubs/<page>.html` measures the first two for every panel in both themes and prints what fails (needs Playwright with Chromium). The history kit's `verify.py` runs its own checks on the site as well.
