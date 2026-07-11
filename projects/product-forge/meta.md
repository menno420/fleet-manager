# product-forge — package meta (core seat 5)

## Seat state
- **LIVE.** Booted 2026-07-10 ~19:05Z **pre-Q-0265-merge** (dispatch record; part4-brief
  lists Product Forge among the 5 live seats owed the §2b amendment paste).
- **Ground-truth override (repo wins, discovered this build):** `control/status.md` @
  product-forge origin/main **`7f05aa8`** (2026-07-10T20:41Z) shows the seat ALREADY
  operating in Q-0265 continuous mode — chain alive, failsafe armed
  (`trig_012EvztCrHHg7s4mBsKT3VKs`), ORDER 001 (games-web phase-1) **acked=001 done=001**
  (PRs #4+#5 merged green; closeout d300c5c; phase-2 proposal 7f05aa8), inbox DRY with a
  ⚑ manager flag for new ORDERs. The dispatch premise ("expect ORDER 001 @ 3179692,
  failsafe not armed") is stale by ~2h of seat work.
- Whether the **§2b amendment was actually pasted into the chat** is unverifiable from
  the repo; the status record makes it functionally moot (continuous mode is active and
  recorded), but the paste remains the owner's belt-and-braces item (part4-brief §2
  item 0) since chat-held instructions may still carry the pre-Q-0265 §2 text from the
  original ~19:05Z boot paste.

## Cadence
- Failsafe cron `0 */2 * * *` (even hours :00; manager reads at :30 — fleet stagger,
  gen3-deployment-standard §2). Pacemaker = send_later ~15-min continuation chain
  (Q-0265); cron is dead-man only.

## Environment
- Name `product-forge` · repos: `menno420/product-forge` ONLY (Q-0260 single-writable-
  repo) · variables: none.
- **⚑ FLAG — spec needed:** fleet-manager `environments/` has **no product-forge entry**
  (archetypes.md project→archetype map predates round-3; no dedicated env spec file).
  The founding package §3 @ dc19b1e assigns **`archetype-python-lab.sh` verbatim**
  (raw: fleet-manager/main/environments/archetype-python-lab.sh) — matches the earlier
  routing table (hub inventory §C: python-lab "reused verbatim by round-3 for
  idea-engine, product-forge, sim-lab"). Centralization should add product-forge to the
  archetypes.md map. The setup-script.sh in this package is a repo-fitted fail-soft
  probe layer consistent with that archetype; subtree deps stay per-product (root is
  stdlib-only by README doctrine — do not fatten the env script per product).

## Grants
- Writable: product-forge only. Merge authority written in CONVENTIONS.md @ 7f05aa8
  (lands own PRs; verified path = native auto-merge armed in the pending window,
  PLATFORM-LIMITS PR #6: armed 20:27:22Z → merged 20:27:29Z; direct agent merge call is
  harness-walled). Fleet doctrine consumed read-only via public raw.

## Codex
- **ENABLED (owner, 2026-07-11)** — Codex environments exist for all 12 active
  fleet repos (owner update 2026-07-11 ~00:2xZ, fm inbox ORDER 014); supersedes
  the 2026-07-10 "unknown (cheap check done)" verdict. The repo's @codex
  conventions (CONVENTIONS.md, review-queue.md format line) are live paths now.
  Quota refusals are RETRY-LATER, never a wall (fm `projects/README.md`
  § Codex fleet-wide enablement).

## Deployed-state per part
| Part | File here | Deployed? |
|---|---|---|
| 1 instructions | `instructions.md` (5,870-char paste block) | **Never deployed as this text.** The live Project holds the founding package §1 paste from the ~19:05Z boot (already natively continuous, but pre-dating ORDER-001 lessons + claim ritual + PR-#6 landing recipe folded in here). |
| 2 coordinator prompt | `coordinator-prompt.md` | **OLD package pasted** — chat holds founding §2 (boot-shaped: seed-verify steps 1–4 now historical). This version is the standing continuous prompt updated to actual repo state. |
| 3 setup script | `setup-script.sh` | **Never.** No in-repo or recorded env script for this seat anywhere (lanes inventory §6: "no env setup script in-repo"); env presumably pastes archetype-python-lab per §3 — unverified from repo. |
| 4 failsafe | `failsafe-prompt.md` | **ARMED per repo status** (trig_012EvztCrHHg7s4mBsKT3VKs) — dispatch premise "NOT armed" stale; armed prompt's verbatim text uncommitted → text-equality with the canonical block unverified. |

## Notes / divergences (decide-and-flag)
- Build order said "squash on green substrate-gate"; repo-verified recipe is native
  auto-merge **method MERGE** (PLATFORM-LIMITS PR #6). Package follows the repo
  ("merged on green" + the arming recipe) — flag if squash is a deliberate new standard.
- Instructions add the claim-FIRST ritual (control/README.md, twin-execution fix) and
  the discovery rule (PLATFORM-LIMITS append-same-session) — both repo-binding at
  7f05aa8, absent from the founding §1.

## Sources
- superbot origin/main **`dc19b1e`**: docs/planning/round3-founding-package-product-forge-2026-07-10.md
  (primary; natively continuous, exact failsafe text §2 step 5) ·
  gen3-deployment-standard-2026-07-10.md §2 (Q-0265-amended operating model, Q-0266
  volume-first) · round3-dispatch-part4-brief-2026-07-10.md §2b (amendment paste block;
  §2 item 0 live-seat paste list) · maintainer-question-router.md Q-0264 (L9511; forge
  consumes manager-routed ORDERs from finalized evidence; r.5/7 escalation shape) +
  Q-0265 (L9593).
- product-forge origin/main **`7f05aa8`**: README.md (role, build ladder, incubator,
  money protocol) · CONVENTIONS.md · control/README.md (bus, claim ritual, fast lane,
  status format) · control/inbox.md (ORDER 001 games-web, mock-data-first) ·
  control/status.md (live continuous-mode + failsafe record) · PLATFORM-LIMITS.md
  (verified walls incl. the PR-#6 landing recipe) · .github/workflows/substrate-gate.yml
  (control fast lane) · products/games-web/ (run.sh = python3 http.server; stdlib
  tests, jsonschema optional).
- Inventories (same scratchpad dir): inventory-hub.md §E/§C · inventory-lanes.md ·
  inventory-games-new.md §6 (product-forge row — note it read older HEAD c93c0e3,
  pre-boot; superseded by 7f05aa8 findings above).

## Last-verified
2026-07-10 ~21:1xZ — superbot origin/main dc19b1e; product-forge origin/main 7f05aa8
(both freshly fetched this session).
