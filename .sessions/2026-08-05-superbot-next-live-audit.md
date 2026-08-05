# 2026-08-05 · hub — boot superbot-next and measure what the harness could not see

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: the owner said "boot up the bot yourself" after three of this
session's claims about it turned out to be wrong. Booting it settled every one
of them in minutes, and then surfaced the thing no amount of reading had —
a panel that reports 58 modules healthy from a hardcoded tuple.

## Previous-session review

PR #757 landed the playtest-Discord research and recommended *against*
deploying superbot-next. The owner overrode that with a reason: superbot carries
architectural debt and superbot-next was meant to be a clean functional clone.
Testing that claim is what this session did.

## Planned

- `docs/findings/2026-08-05-superbot-next-live-audit.md` — what was measured by
  running the bot, the `CAPTURE-WORLD LITERAL` finding, the harness diagnosis,
  and the server-first subsystem shortlist for the owner's rebuild plan.

## Verification

To run: `python3 tools/check_no_false_walls.py --strict` and
`python3 bootstrap.py check --strict`, both post-commit, real exit codes.
