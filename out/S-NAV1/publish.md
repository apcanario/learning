# S-NAV1 · publish record (22 Nov 2026)

Publisher: a fresh agent, model claude-opus-5-5 (Opus 5.5).

## Verdict: NOT PUBLISHED

The Academy publish was refused by the session's permission classifier ("Destructive or Unwanted Actions") and nothing was published. The refusal was not worked around. Because the Greece edition publish is the same kind of action, it was not attempted. deploy.sh was not run (as instructed; `apcanario/academy` attach was already denied). Nothing in the repo was committed, pushed or edited apart from this file.

## Repo state
- Clone /home/claude/learning at HEAD b352a76 ("land S-NAV1: unlock"), one commit past the b939d1c named in the brief. That commit came from land.py's unlock. Tree clean apart from out/S-NAV1/landing-report.md (modified) and this file.
- The kit/academy build on disk equals kit/baseline.json at HEAD for all 273 academy files. kit/editions/greece also matches HEAD's baseline for all 82 files. No rebuild was needed.
- Start build: kit/baseline.json at 797b1d479. Between start and HEAD, 272 of the 273 built academy files differ (all but viz-examples.html), and 81 of 82 Greece files differ (all but greece/syllabus.html). The 460 baseline keys also include sources, and none of the 3 non-site build keys differ.

## Academy artifact, read first
- get_artifact: slug f27e8dc3-7579-4b08-91d2-516bfe862526 (https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH), version 1795290172-9fea, read mode `owner` (so no shared_live), title Academy.
- list_files: 273 files. Every file except index.html matches the start build's sha256, comparing the first 12 hex digits of the transcribed list_files sha256 against baseline@797b1d479.
- read_file (paths) saved the live shell: sha256 107ad4ae38d65425f53018c1cbaee2955e8a74dbb20a4d53c95597cd0e847d1f, 566,776 B. A line diff against the start shell (git show 797b1d479:kit/academy/index.html, sha256 a10e62d4584376b6...) shows only the hosting wrapper: one added first line (doctype, head, style, `<body>`, 531 B) and a closing `</body></html>`. Wrapping the start shell reproduces the live file byte for byte. The live artifact is therefore the start build, with no unexplained difference.

## Prepared, not sent
- Shell in the live wrapper: /home/claude/snav1-publish/academy-index-wrapped.html, sha256 e6e8981ed7ab406d85b41a35329a99a0619e59c2e97efcad86bdf58b3918546a, 626,365 B. The bare HEAD shell's sha256 is 2962210b78631a5ef6ae929ba116824695dc0fbd1b7dc7a727512ce11b8876e2. The copy is outside the repo because publish_files refuses files under /tmp.
- Batch 1 (255 files): the wrapped shell plus 254 changed files, from brand-a/bibliography.html through ux-ia/briefs.html.
- Batch 2 (17 files): ux-ia/built.html, home.html, read-dd-ia1 to 3, read-ia1 to 12. It was to go in a second patch on the new base_version.
- Attempts: (1) refused before sending because the shell was under /tmp; (2) refused before sending because the short id was given as slug, and the tool needs the UUID; (3) with slug f27e8dc3-..., base_version 1795290172-9fea, mode patch: denied by the permission classifier. After the denial, get_artifact still shows version 1795290172-9fea.

## Greece edition
- Artifact https://claude.ai/artifact/M9g881qokC98jC5VEo1Tk3 (editions/greece.toml). `python3 kit/publish_files.py --edition greece` prints one list of 81 fetched files. Not read, not published.

## Read-back
None, because nothing was sent.

## Browser history test
Not tested. The S-NAV1 build is not on the artifact, so the live page cannot show its navigation. A left-edge swipe cannot be tested with a desktop browser in any case.

## To finish
The user needs to allow artifact publishing for this session, or publish themselves. Then: get_artifact (it must still be 1795290172-9fea, otherwise re-check), send the two batches above in mode patch to slug f27e8dc3-7579-4b08-91d2-516bfe862526, read every sent file back by sha256, then do the same for Greece (read the live page, wrap its shell, send the 81 files), then deploy.sh once the attach is allowed.
