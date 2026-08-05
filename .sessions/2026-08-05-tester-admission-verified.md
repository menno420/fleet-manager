# 2026-08-05 · hub — settle how Play testers are actually admitted

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **the honest null was hiding a decision, not a detail.** The
Play findings doc recorded tester mechanics as unverified and moved on. That
looked like a small gap. It was not: inside it sat the answer to "how does a
person actually get this game", and one of the two obvious workarounds is
unavailable by construction while the other is unadvertised.

## previous-session review

PR #752 synced the owner queue to the decided name. Since then the owner
published a signed bundle to the internal testing track, found the opt-in link
Console shows, and asked whether pressing it enrols someone. It does not — and
the question exposed that the queue's recruiting advice was thinner than the
schedule advice sitting next to it.

## Planned

- `docs/findings/2026-08-05-google-play-submission-requirements.md` — a new § 8b
  with the per-track admission rules, quoted from a fetched page.
- `docs/owner-queue.md` — `OQ-PLAY-CLOSED-TEST` gains the recruiting route it was
  missing, and the correction that open testing cannot come first.

## Verification

To run: `python3 tools/check_no_false_walls.py --strict` and
`python3 bootstrap.py check --strict`, both post-commit, real exit codes.
