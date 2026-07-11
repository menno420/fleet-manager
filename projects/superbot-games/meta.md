<!-- v2 · 2026-07-11 · fleet-manager projects registry -->
# superbot-games — Project package meta (Seat A)

> **v2, registry centralization (ORDER 015 as RE-SCOPED —
> `docs/succession/coordinator-handoff-2026-07-11.md` §5): the seat
> SELF-BOOTED, so this package was regenerated IN PLACE from what the booted
> seat ACTUALLY runs (live trigger registry + repo state), not authored as a
> founding package.** v1 (2026-07-10) described a PARKED+CLOCKLESS merged
> lane; that state is history.

| Field | Value |
|---|---|
| Seat | **Seat A — LIVE** (conformed games mapping, fm `docs/proposals/games-program-mapping-conformed-2026-07-10.md`): ONE seat owns SuperBot's entire game world, `games/**` — mining, exploration, fishing, D&D story game, shared world systems (root `README.md` single-seat contract @ `773fab0`; gen-1 two-lane split = GEN-1 HISTORY, `docs/lanes.md`). Self-booted 2026-07-10 from its succession packs; failsafe armed 2026-07-10T23:47:02Z |
| Cadence | Continuation chain (~15-min one-shot/send_later links) as pacemaker + cron failsafe **`trig_019ZgWyL78Rx1sr6LhvL8NE3`** "superbot-games failsafe wake" **`15 */2 * * *`**, enabled, bound to persistent session `session_01TZcMwFdE7zvViW9HgH7fqZ` — registry-verified (`list_triggers` extraction 2026-07-11T01:26:43Z; stored prompt 266 chars, VERBATIM in `failsafe-prompt.md`) |
| Orders | **001 DONE + 002 DONE** (heartbeat `control/status.md` @ `773fab0`, updated 2026-07-11T01:17:42Z: `orders: acked=001,002 done=001,002`). ORDER 001 (P0 CI collection) = **MERGED PR #24** (branch `order-001-collection-scope`, head `241fb21`, merged 2026-07-11T00:20:47Z, merge SHA `7d4c3473bb489e58c047c369521a66e7d6e1fbc0`; CI green on head — `tests` run 29131622448 + `substrate-gate` run 29131622510). Fix lives in **`.github/workflows/tests.yml`** (the order's `substrate-gate.yml` pointer was stale — kit-owned, regenerated); collected-count floor since raised **121 → 147 (`8b9f153`, fishing) → 230** at main HEAD `773fab0` (shared-inventory PR #29 + fishing-adapter PR #33). ORDER 002 (self-arm) = executed in the Q-0265 shape (failsafe + chain, above); heartbeat records it "superseded by Q-0265" |
| Position | At `773fab0`: inventory/resource contract migration — PR-1 shared inventory seam (#29) + PR-2 fishing adapter (#33) SHIPPED; 230 pure-domain tests green; queue: PR-3 mining catalog adapter → PR-4 quest adapter → PR-5 encounter typed grant → PR-6 fish→mining bridge fix; theme-audit roadmap R2–R4 behind it |
| Kit | **v1.8.0** at HEAD `773fab0` (`substrate.config.json` `kit_version: "1.8.0"`; upgrade PR #30, 2026-07-11) |
| Grants | Write: `menno420/superbot-games` only (Q-0260). Read: `menno420/superbot` (oracle, raw) + `menno420/superbot-next` (plugin contract, raw). Env vars: **none** needed (pure-stdlib lane) |
| Codex | **ENABLED (owner, 2026-07-11** — fm inbox ORDER 014, all 12 active repos). Quota refusals = RETRY-LATER, never a wall (`projects/README.md` § Codex fleet-wide enablement) |

## Deployed-state per part (2026-07-11, ORDER 015 sweep)

| Part | Deployed state |
|---|---|
| `instructions.md` | **REGENERATED v2 — no paste receipt exists** (seat self-booted from succession packs, not from this registry; v1 was never pasted). v2 canonizes the single-seat reality at `773fab0` for re-boot/succession; owner paste rides the paste wave |
| `coordinator-prompt.md` | **REGENERATED v2 — never deployed** (the live coordinator session runs on its self-boot context, not a registry paste). v2 is the canonical continuous operating prompt for re-boot/succession; v1's boot steps (ORDER 001/002, one-writer resolution) all EXECUTED by the live seat and removed |
| `setup-script.sh` | **NEVER-DEPLOYED as-written (registry draft, kept + marked).** No paste receipt; the repo itself carries `scripts/env-setup.sh` (kit-standard) + the two gen-1 per-lane scripts (`environment/setup-exploration.sh`, `environments/setup-mining.sh`) at `773fab0` — v1's canonical-home consolidation never executed. Header states this; probe text refreshed to post-ORDER-001 reality (floor 230) |
| `failsafe-prompt.md` | **DEPLOYED + REGISTRY-VERIFIED** — stored trigger prompt captured VERBATIM-FROM-REGISTRY (extracted 2026-07-11T01:26:43Z), byte-checkable (no in-band stamp per registry doctrine). Supersedes v1's never-armed draft |
| `meta.md` | this file |

## Sources (all read/verified this build, 2026-07-11)

- Live trigger registry: `list_triggers` extraction 2026-07-11T01:26:43Z
  (trigger id, cron, session, armed timestamp, stored prompt verbatim).
- superbot-games @ origin/main `773fab06289cc9133ac41c6de2408383329cea54`:
  root `README.md` (single-seat contract) · `control/README.md` (bus protocol)
  · `control/status.md` (heartbeat 2026-07-11T01:17:42Z, orders done=001,002)
  · `control/inbox.md` (ORDERs 001/002 text) ·
  `.github/workflows/tests.yml` (collect-ALL + 230 floor, verified in-tree) ·
  `substrate.config.json` (kit 1.8.0) · PR #24 (merge `7d4c347`, CI runs
  29131622448/29131622510) · PRs #29/#30/#31/#33.
- fleet-manager: `docs/succession/coordinator-handoff-2026-07-11.md` §5
  (re-scope provenance) · `docs/review-queue.md` superbot-games#16 row
  (closed this PR).

**Last verified:** 2026-07-11 (superbot-games HEAD `773fab0`; ls-remote-matched
before capture). Family-level model names only (Q-0262.4).
