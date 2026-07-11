# meta — fleet-manager package

- **Project:** fleet-manager — the MANAGER core seat (seat 1 of the core six,
  Q-0261). **LIVE** since 2026-07-10 ~13:45Z (runbook §3.1: env + §2a/§2b pasted,
  calibration GOOD, boot PR fleet-manager#26 squash-merged `117caeb`); running
  **CONTINUOUS mode** since 2026-07-10 ~20:26Z (ORDER 011 cutover, PR #37).
- **Repo:** `menno420/fleet-manager` (public). Baseline for this package:
  origin/main @ `702ba890` (2026-07-10); the ORDER 011 DONE / failsafe re-arm
  records cited are on branch `claude/order-003-007-review-queue` (PR #37,
  in flight at build time — commits `de5c1ca`/`e0d8016`).
- **Cadence:** pacemaker = ~15-min `send_later` continuation chain (first chain
  fire 20:43Z); cron failsafe `30 */2 * * *` — the manager's :30 offset per the
  gen-3 standard (lanes even hours :00, manager :30 to read fresh heartbeats).
- **Environment archetype:** `coordinator` — the live env is `multi-repo`
  (spec: fm `environments/multi-repo.md` @702ba89, written from inside it),
  setup script `environments/archetype-coordinator.sh` **verbatim** (canonical,
  R15 always-exit-0; runbook §2c names it + its raw URL). Env vars (NAMES only):
  GITHUB_PAT · OPENAI_API_KEY · DATABASE_URL · DISCORD_BOT_TOKEN_PRODUCTION ·
  RAILWAY_* trio+env — production-pointing, unique to this env; never copy the
  list to lane envs. This package's `setup-script.sh` is the repo-fitted probe
  variant (gen-3 shape), NOT a replacement for the deployed archetype.
- **Repo grants:** read-everywhere / multi-repo — the manager is the **sole
  Q-0260 exception** ("every Project except the manager attaches exactly ONE
  repo… the manager stays multi-repo — oversight is its job", runbook §1), and
  it needs **pokemon-mod-lab attached** (private → raw reads 404, sweep would
  misread the lane as DARK; same runbook §1 carve-out). Attached at spec time:
  substrate-kit, superbot, superbot-games, superbot-next, websites
  (environments/multi-repo.md; the round-3 repos — idea-engine, sim-lab,
  product-forge — are public, raw-readable without attachment).
- **Codex: ENABLED (owner, 2026-07-11)** — Codex environments now exist for
  ALL 12 active fleet repos, this one included (owner update 2026-07-11
  ~00:2xZ, inbox ORDER 014). Supersedes the earlier "NO — env-creation ask on
  PR #26" verdict (that ask is RESOLVED). Consequence: @codex is now the
  PRIMARY review-queue drain path here too; the manager failsafe-wake batch
  drops to the fallback tier (quota windows + archives/non-enabled repos
  only). Quota refusals are RETRY-LATER, never a wall —
  `projects/README.md` § Codex fleet-wide enablement.

## Deployed-state per package part

| Part | State |
|---|---|
| `coordinator-prompt.md` | **DEPLOYED** — the seat prompt was owner-pasted as the chat's first message at boot (runbook §2b v3 FINAL, ~13:45Z) and lives in the persistent coordinator chat, subsequently amended live by the owner-pasted Q-0265 §2b block + ORDER 011. This file is the first committed home of that text (previously superbot-only), re-based to continuous per Q-0265 — the live chat already operates on the amended model, so a re-paste is only needed on a seat re-boot. |
| `failsafe-prompt.md` | **DEPLOYED + VERIFIED** — `trig_014odnv5h1tkJAFRhix3tGLq` "fleet-manager failsafe wake", cron `30 */2 * * *`, created 20:26:23Z, verified in the 88-record `list_triggers` at ~20:47Z; old trigger deleted-and-verified-gone (status.md re-arm record, PR #37). |
| `instructions.md` | **NEVER DEPLOYED as such** — the Project's Custom Instructions field carries the runbook §2a v3 text pasted at boot (pre-Q-0265, "ONE bounded slice"); sessions have since run from the pasted founding package + the live chat amendments. This file is the gen-3 re-base (Q-0265 + Q-0264 + landing pattern folded, 2026-07-10 provenance stamps inline) — needs an owner re-paste to become the deployed text. |
| `setup-script.sh` | **UNKNOWN** — what the live `multi-repo` env's setup field actually holds is owner-side UI the manager cannot read (environments/README wall); the canonical intended content is `archetype-coordinator.sh` verbatim. This repo-fitted variant has no paste record (new file). |

## Provenance / sources (all read 2026-07-10)

- superbot @ `dc19b1e8` (origin/main; the runbook/brief/standard texts quoted
  match the 53fb5ef9 inventory baseline — no drift in the quoted sections):
  `docs/planning/round3-dispatch-runbook-2026-07-10.md` §1 (locked architecture
  decisions, Q-0260) + §2 (manager founding package v3 + Q-0265 AMENDED banner);
  `docs/planning/round3-dispatch-part4-brief-2026-07-10.md` §2b (continuous-mode
  amendment + failsafe template + MANAGER-ONLY rider);
  `docs/planning/gen3-deployment-standard-2026-07-10.md` §2 (born-continuous
  standard, Q-0265/Q-0266 folds); router Q-0264 (idea pipeline) + Q-0265.
- fleet-manager @ `702ba890` + PR #37 branch: MISSION.md; control/README.md
  (one-writer bus, manager variant); control/status.md + control/inbox.md
  ORDER 011 (re-arm record); docs/gen2-blueprint.md (Q-0265 changelog fold,
  2026-07-10 night); docs/playbook.md R17/R19/R21/R24; docs/capabilities.md
  (walls: auto-merge arming, GraphQL quota, private-repo toggle, 8,000-char CI
  cap, model attribution); environments/{archetypes.md, archetype-coordinator.sh,
  multi-repo.md, README.md}; .sessions/README.md (born-red card contract).
- websites @ `71c634bf`: `docs/project/setup-script.sh` (probe-block pattern) +
  the `docs/project/` package-dir convention this package generalizes.
- Hub/lane/games inventories: `launch-packages/inventory-{hub,lanes,games-new}.md`
  (2026-07-10) — incl. the finding that the manager's own package had no home in
  its own repo (inventory-hub §G.2), which this package resolves.

**Q-0265 folds applied in this package (dated provenance):** instructions.md
session-shape re-based from "ONE bounded slice" to dispatched-slice-of-a-
continuous-seat (2026-07-10, Q-0265); coordinator-prompt.md step 4 "ARM YOUR
ROUTINE (2-hourly standing wake)" replaced by pacemaker-chain + failsafe model
(2026-07-10, Q-0265/ORDER 011); stale §2b "superbot docs/planning/…launch-pack §1
is your durable twin" pointer widened to include this committed file
(2026-07-10, centralization dispatch).

**Family-level model names only** throughout (Q-0262 policy 1).

- **Last verified:** 2026-07-10 (~21:2xZ, this build; read-only — nothing
  committed or pushed by the builder).
