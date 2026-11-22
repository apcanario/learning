# S-NAV2 step B · Fix 2, a history readout inside the artifact frame (P-NAV7)

Model: Opus 5.5 (`claude-opus-5-5`), a fresh agent. 22 Nov 2026. Nothing committed, pushed or landed. `kit/baseline.json` was not re-recorded and `kit/land.py` was not run. All changes are uncommitted in the working tree, on top of HEAD 8875103 (step A landed).

## What it does

A readout of history in `kit/shell.js`. It appears only when the page's own address carries `?debug` (the regex `/[?&]debug(=|&|$)/` on `location.search`). No fix has been guessed. `go()`'s behaviour is unchanged with or without the readout.

- **Without `?debug`:** `DBG` stays `null`. The page gets no element, no listener and no storage key. Every `dbg()` call returns at once.
  - `go()` takes the same branches as before. Its try/catch only also records a branch name in a local string, and reads `history.length` only when `DBG` is set.
  - The popstate and hashchange handlers, and `saveY`'s catch, each gain an `if(DBG)dbg(...)`. Nothing else in them changes.
- **With `?debug`:** a small panel, `section.dbg`, is fixed at the foot of the screen.
  - First line, the live summary: `history.length N · pushState threw no|yes (k) · last go(): <branch>`.
  - Three buttons, each 44 px tall:
    - **Copy:** puts the summary and log on the clipboard. Where the frame refuses the clipboard, it selects the text instead.
    - **Clear:** empties the log and its storage key.
    - **Hide / Show:** folds the log away.
  - Below them, the log as a plain, selectable `pre`. Each line has the time since load, the event, `history.length` and the hash.
- **What the log records:**
  - **On load:** whether the page is at the top level or in a frame (with `location.ancestorOrigins` when the browser gives it), the address, the referrer, `history.state`, `scrollRestoration` and the user agent.
  - **Each `go(id)`:** which branch it took:
    - `pushState`;
    - `replaceState (a place inside the page shown)`;
    - `pushState threw <name>, replaceState fallback`;
    - `... the fallback threw <name> too: the address is unchanged`;
    - `the same address, no history call`.
    
    Each line also gives the length before the call (the bracket gives it after).
  - **Each event:** each `popstate`, with its state. Each `hashchange`, old hash to new, and whether the handler routes it or it was already routed. A `replaceState` refused in `saveY`. `pagehide`, and `pageshow` from the back-forward cache.
- **Persistence:** the log is kept in `localStorage` under `<the brand's tab key>.debug`, last 300 lines. If a swipe leaves the frame and Pedro comes back, the earlier load's lines are shown above a `--- a new load ---` marker. This only happens with `?debug`, and the key is never written without it.

## Files changed

- **`kit/shell.js`:**
  - the readout block (comment, `DBG`, `dbg`, `dbgH`, `dbgS`, `dbgSum`, and the panel builder that runs only `if(DBG)`), placed before the history section;
  - `go()`: branch names and an `if(DBG)` log;
  - one `if(DBG)dbg(...)` each in the popstate handler, the hashchange handler (it now takes `e`, used only for the log) and `saveY`'s catch.
- **`design/theme.css`, copied to `kit/shell.css`** (`cmp` identical; `rot_check.py` OK):
  - a new section 10, "Debug readout": `.dbg`, `.dbg-sum`, `.dbg-bar`, `.dbg-b`, `.dbg-log`, `.dbg.dbg-min`;
  - a Contents line;
  - a Version 6.21 header entry.
  
  No other rule changed. Without `?debug`, no element carries these classes.
- **`kit/verify.py`:**
  - new `check_debug` (with `DBG_JS`, `DBG_BODY_JS` and `_listeners`, which uses CDP `DOMDebugger.getEventListeners`), called in `main()` right after `check_history`;
  - a docstring paragraph.
- **Rebuilt outputs** (from `baseline.py --check`'s build): `kit/academy/index.html`, and `kit/README.md` (size table: shell 613 KB to 620 KB, whole site 24.74 to 24.75 MB). Also the greece and marketing-ai sites, which are ignored by git.

## What check_debug checks

1. **Without `?debug`, 390 px:**
   - no `.dbg` or `[class*=dbg]` element;
   - the body's children equal the built shell's (parsed from the served `index.html`);
   - no `pagehide` or `pageshow` listener on the window;
   - after the home > area > course > unit walk (`_hist_walk`, the same taps as `check_history`), the window's and the document's listener types are unchanged and there is no `.debug` storage key;
   - no page error.
   
   `check_history` itself runs without `?debug` and is unchanged.
2. **With `?debug`, 390 px:**
   - the panel is shown and fixed, inside the screen, with no sideways scroll;
   - buttons Copy, Clear, Hide, each at least 44 px;
   - the readout adds exactly the `pagehide` and `pageshow` window listeners;
   - the log says `load: top level`;
   - the same walk gives the same `(panel, y)` levels and the same number of history entries as without `?debug`;
   - the log's `go <id>: pushState` lines name the area, course and unit in order, with the length rising by one each;
   - `history.back()` logs `popstate` landing on the course;
   - the summary says `pushState threw no` and gives the right length;
   - Hide folds the log; a reload keeps the earlier load's lines; Clear empties them.
3. **With `?debug` and pushState refused** (the init script throws SecurityError): one `pushState threw SecurityError, replaceState fallback` line per level, and the summary reads `pushState threw yes (k)`.
4. **With `?debug` inside a same-origin sandboxed iframe:** the log says `load: in a frame`.
5. **With `?debug` at 1280 x 800:** the panel is inside the screen, with no sideways scroll.

## Tests

- **`python3 kit/baseline.py --check`:**
  - academy: 460 files, 2 changed (`README.md`, `academy/index.html`);
  - greece: 82 files, 1 changed (`editions/greece/index.html`);
  - 0 added and 0 removed.
  
  These are the expected files.
- **`python3 kit/nav_diff_check.py --build HEAD --now-tree /home/claude/learning`** (start tree: HEAD 8875103; marketing-ai built in the working tree first with `build.py --edition marketing-ai`). NAV DIFF CHECK PASSED:

  | Edition | Classes that differ | Reading pages identical | Drawings |
  |---|---|---|---|
  | academy | shell JS 1, theme CSS 1, size table 1 | 566 | 2417 the same |
  | greece | shell JS 1, theme CSS 1 | 162 | 712 the same |
  | marketing-ai | shell JS 1, theme CSS 1 | 76 | 307 the same |

  The marketing-ai brand strips comments, and its readout still works (probe below).
- **Narrow verify**, without `--full`. verify.py has no single-check flag, so `/tmp/snb/probe.py` imports `verify` and runs `check_history` and `check_debug`. PROBE PASSED:
  - `history`: home (y=1162) > track-history (238) > greece (6500) > m01 (630). The three backs and the forward restore each.
  - pushState refused: no entry added.
  - In the iframe, the back works.
  - debug: the same walk, 3 pushState lines, back > popstate `#greece`. Summary: `history.length 5 · pushState threw no · last go(): pushState`.
  - pushState refused: 3 fallback lines, `pushState threw yes (3)`. 0 faults.
- **`check_debug` alone with `--edition greece`** (`/tmp/snb/probe_ed.py`): one-track walk home > greece > m01, 2 pushState lines. PROBE PASSED.
- **`check_debug` alone with `--edition marketing-ai`:** home > track-marketing > personal-brand-pb > read-pb1. PROBE PASSED.
- **Negative test** (`/tmp/snb/neg.py`): the built shell is served with the `?debug` test replaced by `true`. `check_debug` fails 5 times (readout elements without `?debug`, the body's children, the window's pagehide and pageshow listeners, the storage key, and no listeners added with `?debug`). So the off check catches a readout that leaks.
- **A screenshot at 390 px** after the walk and a back (`/tmp/snb/dbg390.png`): the panel sits at the foot over the page, with the summary, the three buttons and the log legible.
- **`rot_check.py`:** OK.
- **Not run** (left to the landing): `verify.py --full`, `index_check.py`, `private_terms.py`.

## For the main chat

- **Landing:** re-record `baseline.py`, plus `drop:` entries for the lines replaced in `kit/shell.js` (the `saveY` line, `go()`'s first line and try/catch, the popstate and hashchange lines), `kit/README.md` (two size-table rows) and `kit/academy/index.html` (the inlined shell). `design/theme.css`, `kit/shell.css` and `kit/verify.py` only gained lines, except the theme's file end, where a new section was appended after the last rule. Script the entries from `git diff -U0 HEAD`.
- **How to activate it.** `?debug` must reach the frame's own address. On Pages: `https://apcanario.github.io/academy/?debug#home`. In the artifact, claude.ai sets the frame's URL, and I could not test whether `https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH?debug` passes the query into the frame.
  - If the panel does not appear there, the query did not reach the frame. The readout cannot run, and a later row needs another trigger. The log already records `document.referrer` and `ancestorOrigins` for when it does run.
  - I did not add any other trigger, because the spec says `?debug` only and no listener without it.
- **What the readout will decide** (P-NAV7):
  - `pushState threw ...` on each go means the frame refuses pushState. The planned row then makes `go()` also write the location hash.
  - `pushState` with the length rising, and then a swipe that leaves the frame with no `popstate` logged (or a `pagehide` line after a reload), means the frame keeps the entries but the swipe pops claude.ai's.
- **Not done, by design:** no change to `go()`'s behaviour; `design/README.md` and `kit/CHANGELOG.md` do not yet record 6.21 (a line at close, as for 6.20).
