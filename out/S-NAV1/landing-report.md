## land S-NAV1 · 2026-11-21T20:15:36+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 0
- lines preserved: 0 upstream-added lines in 0 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: not needed (no build-relevant change of ours)
- index_check: ok
- verify: ALL CHECKS PASSED (first line: scoped: no page changed + home; 4 of 295 pages checked (home, new, changelog, backlog always), and the edition-wide checks)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 0898ff67e298cdcc36cfb63d33094888d77f5018

## land S-NAV1 · 2026-11-21T21:17:43+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 1
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 19 upstream-added lines in 2 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: kit/shell.js, kit/verify.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 2792169a4b41a5affbeddd4d32abdd5eecf790f3

## land S-NAV1 · 2026-11-21T23:50:17+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 5
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 231 upstream-added lines in 7 files, all present
- accepted drops (--expected): 8
  - kit/verify.py: # nothing. At 390 px: a fresh load holds as many entries as a plain page (no push); home -> course -> unit by the links a reader taps (each at a scroll part
  - kit/verify.py: const course = [...document.querySelectorAll('#home a.course[data-target]')].map(a => a.dataset.target).find(t => kind(t) === 'course');
  - kit/verify.py: # ---- EXTENSION POINT, S-NAV1 Step B (area pages): insert the area level here, between the home and the course: the
  - kit/verify.py: # home's link to the course's area page, then the area page's link to the course, so the walk reads
  - kit/verify.py: # home -> area -> course -> unit and the backs below cover three levels. HIST_PATH_JS then returns
  - kit/verify.py: # [[home's link to the area, area id], [area's link to the course, course id]]; nothing else here changes.
  - kit/verify.py: fr.evaluate(f'window.scrollTo(0, {int(at["max"] * .4)})'); fr.wait_for_timeout(350)   # past the save's 200 ms debounce
  - kit/verify.py: if at['y'] < 100: fails.append(f'history {label}: {at["id"]} scrolls only {at["max"]} px, too short to test its restore')
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: design/theme.css, kit/build.py, kit/shell.css, kit/verify.py and 1 more changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 8a7ab424e796d5e909d9e1f8fc7dd7b6036af761

## land S-NAV1 · 2026-11-22T00:57:49+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 10
  - 8a7ab42 land S-NAV1: verify record
  - 119ce57 land S-NAV1: baseline re-recorded (step B fix: 320 px home hero)
  - 830a82c land S-NAV1: baseline re-recorded (step B outputs; kit/baseline.json recorded in the step B commit and verified unchanged)
  - a0eeaab S-NAV1 step B: declare replaced lines
  - cecd554 S-NAV1 step B: an area home per track, one tile per track on the home, crumbs Home > Area > Course > Unit
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 1166 upstream-added lines in 13 files, all present
- accepted drops (--expected): 3
  - kit/build.py: if MULTI:   # S-NAV1 step B: the track's area page heads its group (step C makes the navigation two levels)
  - kit/build.py: out += f'<a class="ditem dcourse darea" href="#track-{t["id"]}" data-target="track-{t["id"]}" style="--c:{t["color"]}"><span class="n">■</span><span class="t">{
  - kit/verify.py: step(f'{aid} area', dict(id=aid, nav='root', u='AREA', t=next(x['name'] for x in THEMES if 'track-' + x['id'] == aid), arrows=False))
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: design/theme.css, kit/build.py, kit/mdcourse.py, kit/shell.css and 3 more changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 731bd686df8e9f5450bf4cf2db36916acc0cd052

## land S-NAV1 · 2026-11-22T02:25:49+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 12
  - 731bd68 land S-NAV1: verify record
  - 9617d2d land S-NAV1: baseline re-recorded (step C: two-level navigation)
  - 8a7ab42 land S-NAV1: verify record
  - 119ce57 land S-NAV1: baseline re-recorded (step B fix: 320 px home hero)
  - 830a82c land S-NAV1: baseline re-recorded (step B outputs; kit/baseline.json recorded in the step B commit and verified unchanged)
  - a0eeaab S-NAV1 step B: declare replaced lines
  - cecd554 S-NAV1 step B: an area home per track, one tile per track on the home, crumbs Home > Area > Course > Unit
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 1628 upstream-added lines in 16 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: design/theme.css, kit/build.py, kit/shell.css, kit/verify.py and 2 more changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: d2cdd04c99e2baa840d6d8176034b254b86b060d

## land S-NAV1 · 2026-11-22T03:31:20+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 14
  - d2cdd04 land S-NAV1: verify record
  - 66de205 land S-NAV1: baseline re-recorded (step D: line illustrations move from their core)
  - 731bd68 land S-NAV1: verify record
  - 9617d2d land S-NAV1: baseline re-recorded (step C: two-level navigation)
  - 8a7ab42 land S-NAV1: verify record
  - 119ce57 land S-NAV1: baseline re-recorded (step B fix: 320 px home hero)
  - 830a82c land S-NAV1: baseline re-recorded (step B outputs; kit/baseline.json recorded in the step B commit and verified unchanged)
  - a0eeaab S-NAV1 step B: declare replaced lines
  - cecd554 S-NAV1 step B: an area home per track, one tile per track on the home, crumbs Home > Area > Course > Unit
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 3198 upstream-added lines in 19 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: kit/nav_diff_check.py, kit/p94_extract.py, kit/p95_shots.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: c6a65d6e64bad63cbe6909c8e0d9868549e57850

## land S-NAV1 · 2026-11-22T05:23:17+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 16
  - c6a65d6 land S-NAV1: verify record
  - e463597 S-NAV1 steps E and F: nav_diff_check.py, p94/p95 pose the swell
  - d2cdd04 land S-NAV1: verify record
  - 66de205 land S-NAV1: baseline re-recorded (step D: line illustrations move from their core)
  - 731bd68 land S-NAV1: verify record
  - 9617d2d land S-NAV1: baseline re-recorded (step C: two-level navigation)
  - 8a7ab42 land S-NAV1: verify record
  - 119ce57 land S-NAV1: baseline re-recorded (step B fix: 320 px home hero)
  - 830a82c land S-NAV1: baseline re-recorded (step B outputs; kit/baseline.json recorded in the step B commit and verified unchanged)
  - a0eeaab S-NAV1 step B: declare replaced lines
  - cecd554 S-NAV1 step B: an area home per track, one tile per track on the home, crumbs Home > Area > Course > Unit
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 3739 upstream-added lines in 24 files, all present
- accepted drops (--expected): 20
  - design/theme.css: the window (a hero) or clear of the frame (a patch) at the top of the swell (verify.py checks both). */
  - kit/nav_diff_check.py: python3 kit/nav_diff_check.py --build COMMIT [--now REV] [--edition E ...] [--keep]
  - kit/nav_diff_check.py: each with that tree's own kit/baseline.py build(), compares them, then removes the worktrees (--keep leaves them)
  - kit/nav_diff_check.py: def check(start, now, edition):
  - kit/nav_diff_check.py: return counts, touched, fails, reading, (len(fa), len(fb), sum(1 for r in set(fa) & set(fb) if fa[r].read_bytes() != fb[r].read_bytes()))
  - kit/nav_diff_check.py: counts, touched, fails, reading, (na, nb, nd) = check(start, now, e)
  - kit/nav_diff_check.py: print('  FAIL ' + f)
  - kit/shell.css: the window (a hero) or clear of the frame (a patch) at the top of the swell (verify.py checks both). */
  - kit/shell.js: try{history.pushState({y:0},'',h);}
  - kit/verify.py: motion no animation runs at all.
  - kit/verify.py: || paths.some(p => !['rl-in', 'rl-out'].includes(p.getAttribute('class')) || [...p.attributes].some(a => !['class', 'd', 'style'].includes(a.name)) || (p.hasAtt
  - kit/verify.py: out.bad.push('the drawing holds more than rl-in and rl-out paths (a class, a d, a --d) in groups of one origin (--o)');
  - kit/verify.py: 12 KB, the page's tone, the halo fainter, its frame, a swell on each line by transform only at a phase of its own, its
  - kit/verify.py: motion no animation runs at all. Prints each page's joins, its widest gap at each pose and its closest clearance."""
  - kit/verify.py: and opens the area (in an edition of one track, the home at the track's band), and a back returns. From 1100 px the
  - kit/viz.py: moving, the outer halo 1, furthest. A halo ring round several pieces takes the blend of their cores and d's,
  - kit/viz.py: def dist(r, lv):
  - kit/viz.py: return 0.0 if deep[id(r)] == lo else max(0.0, (deep[id(r)] - lv) / (deep[id(r)] - lo))
  - kit/viz.py: halo's blend), each level a path, rl-out (the halo) or rl-in (the outline and the levels inside it), carrying its
  - kit/viz.py: ps = ''.join(f'<path class="rl-{k}"{f" style={chr(34)}--d:{_dfmt(dv)}{chr(34)}" if dv else ""} d="{_ct_d(runs)}"/>'
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: catalog.toml, design/theme.css, kit/build.py, kit/nav_diff_check.py and 4 more changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: efea5bdcd5560dd36b9aa3c8b4312765588e7d7e

## land S-NAV1 · 2026-11-22T05:44:07+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 18
  - efea5bd land S-NAV1: verify record
  - e0c2f6a land S-NAV1: baseline re-recorded (checker fixes: pause off-screen drawings, levels kept, drawing digest)
  - c6a65d6 land S-NAV1: verify record
  - e463597 S-NAV1 steps E and F: nav_diff_check.py, p94/p95 pose the swell
  - d2cdd04 land S-NAV1: verify record
  - 66de205 land S-NAV1: baseline re-recorded (step D: line illustrations move from their core)
  - 731bd68 land S-NAV1: verify record
  - 9617d2d land S-NAV1: baseline re-recorded (step C: two-level navigation)
  - 8a7ab42 land S-NAV1: verify record
  - 119ce57 land S-NAV1: baseline re-recorded (step B fix: 320 px home hero)
  - 830a82c land S-NAV1: baseline re-recorded (step B outputs; kit/baseline.json recorded in the step B commit and verified unchanged)
  - a0eeaab S-NAV1 step B: declare replaced lines
  - cecd554 S-NAV1 step B: an area home per track, one tile per track on the home, crumbs Home > Area > Course > Unit
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 4880 upstream-added lines in 31 files, all present
- accepted drops (--expected): 4
  - docs/BACKLOG.md: Next up: **S-NAV1** (section 4e; Pedro, 21 Nov 2026), then **S-NAV2**; then units resume: **W-SCE3** (SCE2 filed by W-SCE2, 21 Nov 2026; Sport Psychology is com
  - docs/BACKLOG.md: Two rows, two chats, in order. S-NAV1 (history, area homes, two-level navigation, line motion) ran first; S-NAV2 (desktop and tablet layouts, CSS only) is writt
  - docs/BACKLOG.md: | S-NAV1 | Back-swipe history, an area home per track, a two-level navigation and the line illustrations moving from their core (replacing the zoom-out), `shell
  - docs/BACKLOG.md: | S-NAV2 | Desktop and tablet layouts, CSS only (`design/theme.css`, copied to `kit/shell.css`), phone untouched; shots shown to Pedro before publishing. ⚠ Ever
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: scoped: no page changed + home; 10 of 301 pages checked (home, new, changelog, backlog, track-history, track-marketing, track-technology, track-ux, track-sports)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 338eec37120557127ab7293b39060c3bd13a2b6a

## land S-NAV1 · 2026-11-22T06:48:42+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 20
  - 338eec3 land S-NAV1: verify record
  - 132989f land S-NAV1: baseline re-recorded (close: changelog, site log, backlog, S-NAV2 prompt)
  - efea5bd land S-NAV1: verify record
  - e0c2f6a land S-NAV1: baseline re-recorded (checker fixes: pause off-screen drawings, levels kept, drawing digest)
  - c6a65d6 land S-NAV1: verify record
  - e463597 S-NAV1 steps E and F: nav_diff_check.py, p94/p95 pose the swell
  - d2cdd04 land S-NAV1: verify record
  - 66de205 land S-NAV1: baseline re-recorded (step D: line illustrations move from their core)
  - 731bd68 land S-NAV1: verify record
  - 9617d2d land S-NAV1: baseline re-recorded (step C: two-level navigation)
  - 8a7ab42 land S-NAV1: verify record
  - 119ce57 land S-NAV1: baseline re-recorded (step B fix: 320 px home hero)
  - 830a82c land S-NAV1: baseline re-recorded (step B outputs; kit/baseline.json recorded in the step B commit and verified unchanged)
  - a0eeaab S-NAV1 step B: declare replaced lines
  - cecd554 S-NAV1 step B: an area home per track, one tile per track on the home, crumbs Home > Area > Course > Unit
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 5005 upstream-added lines in 36 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: not needed (no build-relevant change of ours)
- index_check: ok
- verify: ALL CHECKS PASSED (first line: scoped: no page changed + home; 10 of 301 pages checked (home, new, changelog, backlog, track-history, track-marketing, track-technology, track-ux, track-sports)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: b939d1cd30c9c2c71051d102bb0c1e28f3fe2a4e

## land S-NAV1 · 2026-11-22T07:06:39+00:00

- start: 797b1d479 (.git/land/started/S-NAV1.json)
- upstream commits absorbed: 21
  - b939d1c land S-NAV1: verify record (full run, both editions)
  - 338eec3 land S-NAV1: verify record
  - 132989f land S-NAV1: baseline re-recorded (close: changelog, site log, backlog, S-NAV2 prompt)
  - efea5bd land S-NAV1: verify record
  - e0c2f6a land S-NAV1: baseline re-recorded (checker fixes: pause off-screen drawings, levels kept, drawing digest)
  - c6a65d6 land S-NAV1: verify record
  - e463597 S-NAV1 steps E and F: nav_diff_check.py, p94/p95 pose the swell
  - d2cdd04 land S-NAV1: verify record
  - 66de205 land S-NAV1: baseline re-recorded (step D: line illustrations move from their core)
  - 731bd68 land S-NAV1: verify record
  - 9617d2d land S-NAV1: baseline re-recorded (step C: two-level navigation)
  - 8a7ab42 land S-NAV1: verify record
  - 119ce57 land S-NAV1: baseline re-recorded (step B fix: 320 px home hero)
  - 830a82c land S-NAV1: baseline re-recorded (step B outputs; kit/baseline.json recorded in the step B commit and verified unchanged)
  - a0eeaab S-NAV1 step B: declare replaced lines
  - cecd554 S-NAV1 step B: an area home per track, one tile per track on the home, crumbs Home > Area > Course > Unit
  - 2792169 land S-NAV1: verify record
  - 0948722 S-NAV1 step A: re-record the build manifest
  - 0a8d31a S-NAV1 step A: declare greece edition shell as expected
  - 300300f S-NAV1 step A: real history entries, popstate routing, per-entry scroll
  - 0898ff6 S-NAV1: register S-NAV1 and S-NAV2, close P-DEC16 as superseded
- lines preserved: 5040 upstream-added lines in 36 files, all present
- accepted drops (--expected): 1
  - docs/CHANGELOG.md: | 21–22 Nov 2026 | S-NAV1 · history, area homes, two-level navigation, line motion; P-DEC16 closed as superseded (session https://claude.ai/code/session_01KMmgQ
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: not needed (no build-relevant change of ours)
- index_check: ok
- verify: ALL CHECKS PASSED (first line: scoped: no page changed + home; 10 of 301 pages checked (home, new, changelog, backlog, track-history, track-marketing, track-technology, track-ux, track-sports)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 9ab64078402e9d4b409d0d87f6351dc01ecbbef7

