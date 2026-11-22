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

