## land S-NAV2 · 2026-11-22T12:02:45+00:00

- start: 445b0c4dd (.git/land/started/S-NAV2.json)
- upstream commits absorbed: 0
- lines preserved: 0 upstream-added lines in 0 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: design/theme.css, kit/build.py, kit/shell.css, kit/verify.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: d1872fd3d8205d09d20fdb60cb2ef530708467c5

## land S-NAV2 · 2026-11-22T12:56:03+00:00

- start: 445b0c4dd (.git/land/started/S-NAV2.json)
- upstream commits absorbed: 2
  - d1872fd land S-NAV2: verify record
  - 7696290 land S-NAV2: baseline re-recorded (A)
- lines preserved: 225 upstream-added lines in 6 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: design/theme.css, kit/shell.css, kit/shell.js, kit/verify.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: fd8ef300e65aea04bcc51d4ffb6b55ea722c1dba

## land S-NAV2 · 2026-11-22T15:15:11+00:00

- start: 445b0c4dd (.git/land/started/S-NAV2.json)
- upstream commits absorbed: 4
  - fd8ef30 land S-NAV2: verify record
  - e13b165 land S-NAV2: baseline re-recorded (B)
  - d1872fd land S-NAV2: verify record
  - 7696290 land S-NAV2: baseline re-recorded (A)
- lines preserved: 541 upstream-added lines in 10 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: design/theme.css, kit/shell.css, kit/verify.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: c3aa941385a2ba0b9f417cbc2e0204f16ae84d03

## land S-NAV2 · 2026-11-22T16:38:36+00:00

- start: 445b0c4dd (.git/land/started/S-NAV2.json)
- upstream commits absorbed: 6
  - c3aa941 land S-NAV2: verify record
  - 7a525a3 land S-NAV2: baseline re-recorded (C)
  - fd8ef30 land S-NAV2: verify record
  - e13b165 land S-NAV2: baseline re-recorded (B)
  - d1872fd land S-NAV2: verify record
  - 7696290 land S-NAV2: baseline re-recorded (A)
- lines preserved: 978 upstream-added lines in 12 files, all present
- accepted drops (--expected): 4
  - kit/verify.py: 390, 768 and 1280 px), the real line (--n on p.harea the number of its words, the tracks) and a probe copy of it with
  - kit/verify.py: const side = desk && innerHeight < 860 ? 240 : 0;   // S-NAV2 step C: the 240 px sidebar of the tablet landscape layout; a desktop home (860 px tall or more) ha
  - kit/verify.py: const want = parseFloat(getComputedStyle(document.body).width) >= 960 ? 3 : 2;   // S-NAV2 step C: three across once the width beside the sidebar reaches 960 px
  - kit/verify.py: want = 3 if pg.evaluate('parseFloat(getComputedStyle(document.body).width)') >= 960 else 2   # S-NAV2 step C: three across once the width beside the sidebar rea
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: kit/verify.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 49eba6d0566a6d04e9686c5626c750af6bcd4c99

## land S-NAV2 · 2026-11-22T18:20:34+00:00

- start: 445b0c4dd (.git/land/started/S-NAV2.json)
- upstream commits absorbed: 8
  - 49eba6d land S-NAV2: verify record
  - 47cde7f land S-NAV2: baseline re-recorded (D)
  - c3aa941 land S-NAV2: verify record
  - 7a525a3 land S-NAV2: baseline re-recorded (C)
  - fd8ef30 land S-NAV2: verify record
  - e13b165 land S-NAV2: baseline re-recorded (B)
  - d1872fd land S-NAV2: verify record
  - 7696290 land S-NAV2: baseline re-recorded (A)
- lines preserved: 1655 upstream-added lines in 18 files, all present
- accepted drops (--expected): 3
  - design/README.md: At 390 or 400 px, 768 px, 1280 px and (since S-NAV2) 1920 px wide, in dark and in light, on every page with every `<details>` open: the document is not wider th
  - design/theme.css: .main-nav{position:fixed;top:0;left:var(--side);right:calc(3 * 44px + 24px);height:var(--bar);display:flex;align-items:center;gap:2px;margin:0;padding:0 8px;bor
  - kit/shell.css: .main-nav{position:fixed;top:0;left:var(--side);right:calc(3 * 44px + 24px);height:var(--bar);display:flex;align-items:center;gap:2px;margin:0;padding:0 8px;bor
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: design/theme.css, kit/build.py, kit/shell.css, kit/verify.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 7a7437f64afef5d379d9a882865f88251b1e75df

