# codetool-lab-opus4.8 — package meta

> **Status: ARCHIVE.** Project CLOSED (fleet-manager `control/status.md` @ `0eaa668`:
> "codetool ×3 — Projects CLOSED; repos retained"; disposition in
> `docs/planning/gen2-launch-record-2026-07-10.md` @ `0eaa668`). Repo retained and
> **NOT platform-archived** — `"archived": false` API-verified 2026-07-10 ~15:12Z; the
> archive toggle is a parked paired DECISION (fleet-manager `docs/owner-queue.md` @
> `0eaa668` § Parked: "wait, then archive" — archiving would make the repo read-only and
> break the NEXT-BOOT write rituals). Repo HEAD at build time: `80f6cd102ef6`
> ("wind-down complete — ready for archive + fresh session", PR #22).
> **Codex env: DELETED (owner, 2026-07-11)** — stale Codex environments for dead
> repos were removed in the fleet-wide Codex enablement pass (owner update
> 2026-07-11 ~00:2xZ, fm inbox ORDER 014); this repo is not among the 12 active
> repos with a Codex environment.

No live package artifacts (nothing deployed; no Project). This meta indexes the
successor-seed material and the repo's terminal state.

## Succession material (would seed any gen-3 successor)

All at `80f6cd1`:

- `docs/succession/NEXT-BOOT.md` — future-seat boot prompt; the richest of the three
  codetool packs (read order with per-line why, walking-skeleton check, §5
  merge-authority probe). Gen-2 discrete-session model.
- `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md` — KEEP/DROP/ADD rewrite. Carries the
  honest caveat that the coordinator **never saw the build lane's actual deployed Custom
  Instructions text** (it critiques *inferred* instructions); the deployed gen-1 CI text
  lived only in the Project surface, never in git (`control/inbox.md` ORDER 001 @
  `80f6cd1` confirms the pattern).
- `docs/succession/ENVIRONMENT.md` + `docs/succession/GEN2-FEEDBACK.md`.
- Setup script: **`environments/setup.sh`** @ `80f6cd1` — defensive, always-exit-0,
  cwd-detecting; written as the fix for the sibling-lane setup-death class (a session
  that died ~10s after spawn, unnoticed ~2.8h).
- Whole-life retro: `docs/retro/project-review-final-2026-07-09.md` (named in
  `control/status.md` notes @ `80f6cd1`).

## Release state — v0.1.0 / v0.2.0 LIVE

Product: **mdverify**. GitHub Releases **v0.1.0 and v0.2.0 are LIVE** — published via
the Actions `workflow_dispatch` release route, authored by `github-actions[bot]`
(v0.1.0 2026-07-09T16:56:21Z, v0.2.0 2026-07-09T17:57:53Z; attested by
`control/status.md` health line @ `80f6cd1` "v0.1.0 + v0.2.0 Releases live" and by the
fable5 correction commit `a6cf1a9` which cites the publish timestamps). Remote tags
verified present at build time (`ls-remote --tags`: v0.1.0, v0.2.0). This lane is the
**proof side of the seat-dependent release-wall lesson** (below). Remaining parked owner
items (`control/status.md` ⚑ @ `80f6cd1`): OPTIONAL PyPI publish of mdverify (name was
free as of 2026-07-09), OPTIONAL Claude GitHub App connect.

⚠ Coordinator note: fleet-manager `docs/owner-queue.md` @ `0eaa668` § Parked still lists
"codetool-lab-opus4.8 v0.1.0 tag + Release — owner click" — stale/mislabeled against the
live releases above (the actually-unreleased tags belong to **fable5**/envdrift).

## The seat-dependent release-wall lesson (recorded at fable5 `a6cf1a9`)

fable5's seat was classifier-denied the exact Actions release route this lane used
successfully. The reconciled doctrine (fable5 `docs/succession/PLATFORM-LIMITS.md` item
4 @ `a6cf1a9`): classifier-denial walls are **SEAT-DEPENDENT** — a successor seat
attempts once from its own seat and records its verbatim outcome; never inherit "route
closed" as doctrine. This repo is the existence proof that the route works on some seats.

## Branches — one stale

- `claude/status-heartbeat-001` — leftover; agent branch-delete is a verified 403, so
  deletion is an owner click (queued in `control/status.md` ⚑(1) @ `80f6cd1` and in
  fleet-manager `docs/owner-queue.md` @ `0eaa668` § housekeeping stale-branch list).

## Gen-3 note

**Any successor seat starts from the gen-3 born-continuous standard, not these gen-2
texts**: superbot `docs/planning/gen3-deployment-standard-2026-07-10.md` @ `dc19b1e8`
(Q-0265-amended: born continuous, send_later pacemaker, `"<seat> failsafe wake"` cron)
+ `round3-dispatch-part4-brief-2026-07-10.md` §2b amendment block. NEXT-BOOT and the CI
proposal here are pre-Q-0265 raw material; re-base per the Q-0262.6 hold before any
deployment.
