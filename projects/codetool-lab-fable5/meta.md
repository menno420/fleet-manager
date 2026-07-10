# codetool-lab-fable5 — package meta

> **Status: ARCHIVE.** Project CLOSED (fleet-manager `control/status.md` @ `0eaa668` lane
> line: "codetool ×3 — Projects CLOSED; repos retained"; disposition recorded in
> `docs/planning/gen2-launch-record-2026-07-10.md` @ `0eaa668`: "codetool arms ×3 —
> Projects → CLOSE; repos stay"). Repo retained and **NOT platform-archived** — GitHub API
> reports `"archived": false` (verified 2026-07-10 ~15:12Z); the archive toggle is a
> **parked paired DECISION** in fleet-manager `docs/owner-queue.md` @ `0eaa668` (§ Parked):
> recommendation "wait, then archive" — archiving makes the repo read-only and would break
> the NEXT-BOOT write rituals the succession pack expects. Repo HEAD at build time:
> `a6cf1a9d5e8b` (= the succession-doc fix commit itself, PR #14).

No live package artifacts exist for this seat (nothing deployed; no Project). This meta
is the archive index: where a gen-3 successor's seed material lives, and what state the
repo was left in.

## Succession material (would seed any gen-3 successor)

All at `a6cf1a9`:

- `docs/succession/NEXT-BOOT.md` — the future-seat boot prompt (gen-2 discrete-session
  model: heartbeat-before-work → read order → walking skeleton → work).
- `docs/succession/custom-instructions-proposal.md` — KEEP/DROP/ADD rewrite of the
  founding Custom Instructions (proposal only; the actually-deployed gen-1 CI text was
  never committed to git).
- `docs/succession/PLATFORM-LIMITS.md` — walls with exact error text, including the
  seat-dependence correction (below).
- `docs/succession/ENVIRONMENT.md` + `docs/succession/gen2-feedback.md`.
- Setup scripts: **`environments/setup-universal.sh`** (fleet-canonical defensive shim,
  R15 always-exit-0) routing to **`scripts/env-setup.sh`** (repo-specific editable
  install, non-fatal). The most complete env-setup pair of the three codetool arms;
  `control/status.md` ⚑(3) @ `a6cf1a9` names it as the paste-ready env script for any
  gen-2/3 boot.
- Wider context: `docs/ROADMAP.md`, `docs/retro/wind-down-review-2026-07-09.md`
  (whole-life retro), `docs/retro/project-review-2026-07-09.md` §(e) (owner-manual
  release steps).

## Release state — envdrift tags PARKED

Product tip: **envdrift 0.2.0 on main** (PR #9, `13a84e5`). Tags **v0.1.0 (`73ef38d`)
and v0.2.0 (`13a84e5`) + GitHub Releases were never pushed** — zero tags on the remote
(verified `ls-remote --tags` at build time). Owner-manual steps are in
`docs/retro/project-review-2026-07-09.md` §(e); parked as `control/status.md` ⚑(1)–(2)
@ `a6cf1a9` (this lane's seat got credential-layer 403 on tag push AND classifier
denials on the Actions release route — but see the seat-dependence lesson).

⚠ Suspected hub drift worth a coordinator look: fleet-manager `docs/owner-queue.md` @
`0eaa668` (§ Parked) carries "codetool-lab-**opus4.8** v0.1.0 tag + Release — owner
click", but opus4.8's v0.1.0/v0.2.0 Releases are LIVE (its own status + the a6cf1a9
correction both attest). The un-released tags are **this repo's** (fable5/envdrift) —
the queue line looks mislabeled.

## The seat-dependent release-wall lesson (commit `a6cf1a9`, PR #14)

`docs/succession/PLATFORM-LIMITS.md` item 4 correction — the single most reusable
lesson in this archive:

- This lane's seat was denied the Actions `workflow_dispatch` release route twice by
  the permission classifier ("[Auto Mode Bypass]"; retry with explicit owner
  authorization: "No reason provided") and originally recorded "Route closed. Releases
  are owner-manual."
- That verdict was an **over-generalization from one seat's classifier outcome**:
  sibling lane codetool-lab-opus4.8 published two live GitHub Releases via exactly that
  route (v0.1.0 2026-07-09T16:56:21Z, v0.2.0 2026-07-09T17:57:53Z, both authored by
  `github-actions[bot]`).
- Corrected doctrine: classifier-denial walls (vs credential-layer 403s) are
  **SEAT-DEPENDENT** — "probing a documented wall twice is a bug" applies **per seat**;
  a successor on a different seat attempts once and records its own verbatim outcome.
  Same rider added to item 8 (scheduler tools: `send_later`/`create_trigger` absent on
  this coordinator seat but present on Project-session seats).

Any gen-3 founding package (codetool successor or otherwise) should inherit this as a
probe-once-per-seat rule, not as a wall list to obey blindly.

## Branches

No stale branches — remote has `main` only (verified `ls-remote --heads` at build time).

## Gen-3 note

**Any successor seat starts from the gen-3 born-continuous standard, not these gen-2
texts**: superbot `docs/planning/gen3-deployment-standard-2026-07-10.md` (@ superbot
`dc19b1e8`, operating model amended per Q-0265: born continuous, send_later pacemaker,
cron demoted to `"<seat> failsafe wake"`) + the Q-0265 amendment paste block in
`docs/planning/round3-dispatch-part4-brief-2026-07-10.md` §2b. The succession pack above
is **raw material** (walls, env scripts, KEEP/DROP/ADD rationale) — its NEXT-BOOT
discrete-wake shape and CI proposal are pre-Q-0265 by design and must be re-based, per
the Q-0262.6 hold, before anything is deployed.
