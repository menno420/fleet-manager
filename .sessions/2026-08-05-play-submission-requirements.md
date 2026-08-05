# 2026-08-05 · hub — what Google Play actually requires

> **Status:** `complete`

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

**The paid Gemini key reaches Pro with grounding, first call.** `gemini-3.1-pro-preview`
+ `tools: [{"google_search": {}}]` over direct egress returned HTTP 200 with
`groundingChunks` populated. The free key refuses both. One trap for the next
session: `trust_env` is a `requests.Session` **attribute**, not a `post()`
kwarg — passing it as a kwarg raises `TypeError`.

**Grounding is not evidence, measured twice in seven queries:**

| Query | Grounding chunks | Outcome |
|---|---|---|
| AAB, signing, listing, policy, account | 4–9 each | all confirmed on fetch |
| **target SDK** | **0** | model memory; claims happened to be right, confirmed on fetch |
| **games-specific** | **0** | model memory; **not** confirmed, recorded as null |

A zero-chunk response is formatted identically to a grounded one. Nothing in the
text distinguishes them — only `groundingMetadata` does. Read it every time.

**The miscitation.** `answer/9859751` was cited as the content-rating source. It
is the *publishing status* page and never mentions IARC. The requirement was
real; the citation was laundered. Correct page (`answer/9859655`) found and
fetched. This is the second measured instance in this estate of a grounded
citation pointing somewhere plausible and wrong.

**Where source beat documentation.** Godot's class reference describes
`gradle_build/export_format` as *"Application export format (\*.apk or \*.aab)"*
and never gives the numbers — useless for editing a text preset. `export_plugin.cpp`
carries the hint `"Export APK,Export AAB"`, default `EXPORT_FORMAT_APK`, and a
bounds check proving **APK=0 < AAB=1**. Same read also yielded
`DEFAULT_TARGET_SDK_VERSION = 36`, which happens to equal what Play requires from
2026-08-31 — so the engine default was already compliant, and pinning it
explicitly protects against a future engine bump moving it.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**, CLEAN across 5
  living/binding docs. Real exit code, not `$?` after a pipe.
- `python3 bootstrap.py check --strict` → **exit 1**, sole finding the designed
  born-red `[session-card-hold]`; everything else advisory (a status heartbeat
  restamped in spider-swing, stale-wall re-verification notices in that repo's
  own ledger).
- Every requirement acted on was fetched from its official URL in this session.
  Eleven pages fetched; each source link in the findings doc is one of them.
- spider-swing PR #162: `game-quality` **success**, `android-debug` **success**,
  `substrate-gate` red only on its own born-red hold.

**Honest nulls, carried deliberately rather than smoothed:** the pre-2026-08-31
target API requirement (no fetched page stated it); the `-validity 10000` keytool
convention (not on Google's signing page); the `com.example` Play restriction
(support-community thread, not documentation); D-U-N-S for organisations (not
applicable, not fetched); the government/financial/advertising-ID declarations
(Gemini cited a bare site root — nothing to fetch); and everything
games-specific. Also: `android-release.yml` has never run end to end and cannot
from a session, since it needs the owner's repository variables.
