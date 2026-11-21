# S-NAV1 · Step A · history

Model: Opus 5.5 (claude-opus-5-5), a fresh agent. 21 Nov 2026.

## Verdict

Done. Back and forward walk the site; each entry's scroll is restored; the first load pushes nothing; a refused
pushState falls back to the old replaceState behaviour. History test passes. No commit, no push, no land.py (the main
chat commits). No unit, brief, vault, design or CSS file touched.

## What changed

**kit/shell.js** (inlined by kit/build.py as before; build.py not changed)
- `go(id)`: saves the scroll of the entry it leaves (`history.replaceState({y}, '')`), then `history.pushState({y:0}, '', '#'+id)`.
  No push when the address already holds `#id` (a "Try again" on the current page, a second tap), so no duplicate entries.
- Fallback (artifact case): if `pushState` throws, `replaceState(null, '', '#'+id)`, the behaviour before S-NAV1; if
  that throws too, the panel is still shown without touching the address (before, a throw there stopped navigation).
- `history.scrollRestoration = 'manual'` (in try), so the browser does not jump before a fetched panel lands.
- The scroll is also saved to the current entry 200 ms after scrolling stops (debounced, so replaceState is not flooded),
  which covers plain `<a href="#...">` links the browser itself pushes.
- `route()` now returns the promise of `show()` (settles once the panel holds its content and any target is revealed).
- `routeTo(state)`: route, then `scrollTo(0, state.y)` if the entry kept one (and the address has not moved meanwhile).
  Listeners: `popstate` routes and restores; `hashchange` routes only if popstate has not already routed that hash
  (Chromium fires both for a hash navigation; the `routed` marker stops a double route). The first load calls
  `routeTo(history.state)`: it never pushes; on a reload it restores the y the entry kept.

**kit/verify.py** (history test only): `check_history(br, fails)`, called in `main()` after `check_site_log`, with helpers
`HIST_PATH_JS`, `HIST_UNIT_JS`, `HIST_AT_JS`, `_hist_ready`, `_hist_walk`, `_hist_ctx`. Three parts, all at 390 px:
1. Top level: a fresh load holds as many entries as a plain script-free page (no push). Walk home -> course -> unit by the
   links a reader taps (the home's first course tile, the course home's first unit link), each page scrolled to 40% of
   its height first (the y read back, over 100 px or the test fails as meaningless), the tap done by `el.click()` so
   Playwright does not scroll; each new page must open at the top. Entries added = levels walked - 1. Then
   `history.back()` once per level: each lands on its page with its y (2 px tolerance); then `history.forward()` to the
   end lands on the unit with its y.
2. pushState refused (an init script makes it throw): the same walk without scrolls; every page still opens, the
   address ends on the unit, no entry is added, no page error.
3. Inside an `<iframe sandbox="allow-scripts allow-same-origin">` (as an artifact viewer may hold the page): the walk,
   then one back to the course with its y.

**Extension point for Step B** (area pages): marked `# ---- EXTENSION POINT, S-NAV1 Step B (area pages)` in `_hist_walk`.
`HIST_PATH_JS` returns the list of [link selector, panel] levels between the home and the course; today it has one
(home tile -> course). Step B makes it two (home -> area, area -> course); the backs, forward and entry counts follow
the list, so nothing else changes and the test then covers home -> area -> course -> unit with three backs.

## Test results

`check_history` run alone against the rebuilt site (a script importing verify.py, so verify-hashes.json was not written):

```
history: home (y=1947) -> greece (y=6500) -> m01 (y=630); back -> greece y=6500 (kept 6500); back -> home y=1947 (kept 1947); forward to the end -> m01 y=630 (kept 630)
history, pushState refused: replaceState fallback, home -> greece -> m01 shown, no entry added (2), address #m01
history, sandboxed iframe: home -> greece -> m01, back -> greece y=6500 (kept 6500)
HISTORY CHECKS PASSED
```

Regression spot check, same way: `check_reading` (235 pages; deep links, Continue and reload resuming at the section)
and `check_split` (fetch, prefetch, deep links into unopened panels, failed fetch and retry): 0 fails each.

Build: `python3 kit/baseline.py --check` was clean before the change; after it, 3 differ, all expected (baseline.json
not re-recorded): `README.md` (size table), `academy/index.html`, `editions/greece/index.html`. Listed in
`out/S-NAV1/expected-A.txt`.

Not run: the full `kit/verify.py` (shell.js changed, so it is a full run, and a pass writes kit/verify-hashes.json, a
file outside this step's list). land.py runs it at landing; the main chat may run it first.

## Open choices (taken, recorded)

- Hash, not a path: `pushState` with `'#'+id`, keeping the existing hash routing, Pages and the artifact unchanged.
- State is `{y}` only; the panel comes from the address. The section a reading page shows is not in history (it stays
  in localStorage per page, as before); a back to a unit restores its y within the section it shows.
- Scroll is restored after the panel's fetch lands, not before; a late font or figure layout shift after that is not
  corrected.
- Reload now restores the entry's y (with `scrollRestoration = 'manual'` the browser no longer does).
- In-page section links on a reading page (menu, next/previous section) still do not push entries (unchanged: they
  preventDefault and reveal). The bar's prev/next unit arrows and the Home button go through go(), so they now push.
- Edge left: if both pushState and replaceState throw and the target is an id inside a panel (not a panel id), route()
  reads the unchanged address and shows the old page. Not reachable in any frame tested; before S-NAV1 the same case
  threw and did nothing.
- The iframe test uses `allow-same-origin`; a fully opaque sandbox (no same-origin) cannot fetch the split panels from
  the local server at all, so it was not tested; the pushState-refused case stands in for a frame that refuses history.

## Blockers

None. No permission check refused a script.
