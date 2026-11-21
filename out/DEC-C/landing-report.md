## land DEC-C · 2026-11-21T05:10:56+00:00

- start: e855c10d4 (.git/land/started/DEC-C.json)
- upstream commits absorbed: 7
  - 791e400 DEC-B: W-DD-SP3 prompt re-saved with carried proposals P-DEC17-19; landing report
  - b882b51 DEC-B: verify --full ALL CHECKS PASSED; verify-hashes.json
  - 4d064da DEC-B close: P-DEC4, P-DEC9, P-DEC6 to CHANGELOG; proposals P-DEC17-19
  - 98800ea DEC-B checker findings applied (README, decoupling §6, pack heading name, biblio path from cpath); manifest rehash for kit/README.md
  - de180ed P-DEC6: biblio text names courses/<course>/bibliography/; 29 expected differences, manifest re-recorded
  - 48b62cf P-DEC9: derive relief tool course lists from course.toml reliefs=true
  - 89c0881 P-DEC4: harden kit/pack.py (changelog by key, insert name/date, briefs and pack.status stops)
- lines preserved: 439 upstream-added lines in 16 files, all present
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: re-recorded (5 differences: 1 declared by a side's baseline.json, 4 by --expected), then clean
- index_check: ok
- verify: ALL CHECKS PASSED (first line: full: kit/build.py, kit/howbuilt.py, kit/verify.py changed)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: 8f932eb2e1db774521426dd8e9ff2d8e8784113b

## land DEC-C · 2026-11-21T06:40:02+00:00

- start: e855c10d4 (.git/land/started/DEC-C.json)
- upstream commits absorbed: 17
  - 8f932eb land DEC-C: verify record
  - f0731bc land DEC-C: baseline re-recorded for expected differences
  - 617d885 DEC-C: kit/baseline.json back to upstream's; land.py re-records it for the declared differences
  - 52f4e5a DEC-C: land --expected file
  - e3778c4 DEC-C: manifest re-recorded on the rebased tree after the diff proved only the five expected files
  - d9f19f5 DEC-C: close P-DEC8, P-DEC11, P-DEC15; proposals P-DEC17, P-DEC18
  - 3596542 DEC-C: apply checker findings (Known limits wording, geo.py saved, docstrings, decoupling marks)
  - 22ad605 P-DEC15: What's new scales per edition, a tenth of the largest day under 110,000 words
  - 2a7679b P-DEC11: a hero of one or two rises held to a 330 px hero's band; a page too short to scroll lands at its foot
  - f174e22 P-DEC8: markdown How it was built drops the S-NOAUDIT AUDIT_LOG clause where the course has no audit_log rows
  - 791e400 DEC-B: W-DD-SP3 prompt re-saved with carried proposals P-DEC17-19; landing report
  - b882b51 DEC-B: verify --full ALL CHECKS PASSED; verify-hashes.json
  - 4d064da DEC-B close: P-DEC4, P-DEC9, P-DEC6 to CHANGELOG; proposals P-DEC17-19
  - 98800ea DEC-B checker findings applied (README, decoupling §6, pack heading name, biblio path from cpath); manifest rehash for kit/README.md
  - de180ed P-DEC6: biblio text names courses/<course>/bibliography/; 29 expected differences, manifest re-recorded
  - 48b62cf P-DEC9: derive relief tool course lists from course.toml reliefs=true
  - 89c0881 P-DEC4: harden kit/pack.py (changelog by key, insert name/date, briefs and pack.status stops)
- lines preserved: 2443 upstream-added lines in 61 files, all present
- accepted drops (--expected): 1
  - docs/CHANGELOG.md: | 21 Nov 2026 | P-DEC8, P-DEC11, P-DEC15 · the build changes that alter output on purpose, one expected-differences proof and one publish (chat DEC-C; session h
- saved row prompts: no merge, not checked
- files auto-merged: none
- baseline: not needed (no build-relevant change of ours)
- index_check: ok
- verify: ALL CHECKS PASSED (first line: scoped: no page changed + home; 4 of 292 pages checked (home, new, changelog, backlog always), and the edition-wide checks)
- lock: released; moved onto 1 of our own lock heartbeats before the push
- push attempts: 1
- pushed: cf5d0de8f878a1eb4f383101b37abdf0ad947c49

