# 2026-08-05 · hub — what Google Play actually requires

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · research + build — grounded store requirements

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **the requirement everyone repeats is rarely the one that sets
the date.** "Play wants an `.aab`, not an `.apk`" is true, verified, and took an
afternoon to satisfy in code. The requirement nobody quotes — a personal
developer account created after 2023-11-13 must run a closed test with **12
testers opted in for 14 continuous days** before it may even *apply* for
production access, then wait ~7 days for review — is a three-week floor that no
amount of finished code shortens. Research that only answers the question asked
would have missed it. The build work is the cheap half; the calendar is the
deliverable.

## previous-session review

`2026-08-05-hud-telemetry-verification.md` (PR #742, merged) established the
"ask for readings, not verdicts" method and seeded `OQ-SWINGY-NAME`. This
session applies the same scepticism to a different surface: grounded citations
were treated as leads, and fetching each one caught a real miscitation.

## What landed

- `docs/findings/2026-08-05-google-play-submission-requirements.md` — every
  requirement with the URL this session fetched itself, and explicit
  **NULL — unverified** for everything it could not confirm.
- `docs/owner-queue.md` — six new `OQ-PLAY-*` entries.
- `menno420/spider-swing` PR #162 — the buildable half (ADR 0005).

## Measured

[[fill: measured]]

## Verification

[[fill: verification]]
