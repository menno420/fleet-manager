# superbot — Project package meta

- **Seat:** **NONE — by design.** Q-0264 (owner directive, 2026-07-10)
  superseded the hub-seat idea: the Q-0262.8 pick of superbot as hub-executor
  seat 6 was vetoed (Q-0264 items 2/5 — sim-lab took seat 6; hub
  games-finishing routes to the games program (Q-0259 r.5) / owner-started
  superbot sessions; router @ superbot origin/main `dc19b1e8`). This package
  therefore serves **owner-started sessions**, not a standing coordinator:
  part 2 is a manual kickoff prompt, part 4 documents the deliberate absence
  of a wake.
- **What runs here anyway:** (a) owner-started sessions (any focus; default
  lane = the games completion wave per Q-0259/Q-0264.8); (b) the **LIVE
  production bot** — Railway auto-redeploys `worker` on every merge to main
  (merge=deploy, Q-0193; the live bot keeps its Q-0213 `*Delete`/`*Restore`
  brake); (c) the **self-firing Q-0107 recon loop** — ROUTINE_PAT +
  `reconciliation-trigger.yml` + `check_reconciliation_due.py` open a
  `reconcile` issue every 30-PR band (42nd pass ran off issue #1951,
  band-#1950; `docs/current-state.md` "Last updated" @ `dc19b1e8`); (d) the
  **Idea Engine harvests `docs/ideas/` by link** (referenced, never migrated
  — Q-0264.8), so hub sessions route ideas simply by filing them.
- **Cadence:** none (no seat, no cron, no pacemaker — part 4). The recon loop
  above is issue-triggered, not cron-shaped, and needs no Project.
- **Environment archetype:** `fleet-manager environments/archetype-bot-prod.sh`
  (serves "superbot (legacy)"; fm origin/main `0eaa668`) — the ONLY archetype
  allowed production-pointing vars. **python3.10 pinned by repo name** (CI
  parity with `code-quality.yml`; bare python3 is 3.11.x in-container —
  archetypes.md wrinkle #1). Part 3 here is the single-repo specialization;
  the repo's own SessionStart hook (`scripts/claude_session_start.sh`:
  `setup_dev_env.sh` + CodeGraph `@optave/codegraph@3.11.2`) does the heavy
  lifting once the session opens.
- **Env var NAMES (owner-set; observed live set, fm `environments/archetypes.md`
  row "menno420/superbot (legacy)"):** `DATABASE_URL`,
  `DISCORD_BOT_TOKEN_PRODUCTION`, `OPENAI_API_KEY`, `GITHUB_PAT`,
  `RAILWAY_API_KEY`, `RAILWAY_PROJECT_ID`, `RAILWAY_SERVICE_ID`,
  `RAILWAY_ENVIRONMENT_ID`; plus `YOUTUBE_API_KEY` (deploy-required,
  degrades soft). Values never in any repo.
- **Grants:** `menno420/superbot` only, per session (Q-0260 single-writable-repo
  applies to whatever Project hosts the session). Historical note: the
  2026-07-07 "SuperBot" Projects-EAP coordinator had both superbot +
  superbot-next in scope — that gen-1 arrangement ended with the EAP fleet
  close-out; superbot-next has its own Builder seat now.
- **Kit pin:** `substrate.config.json` pins `kit_version: "1.0.0"` —
  **vestigial, never adopted.** EAP program-review finding §5.9: "The hub
  never adopted its own kit. superbot pins a fictional v1.0.0, hand-authors
  telemetry, and maintains a parallel (better) session-gate implementation —
  the origin repo is the only active repo not on the substrate it exports"
  (`docs/eap/eap-program-review-2026-07-10.md` @ `dc19b1e8`). Real kit
  adoption is a substrate-kit-seat distribution job, not this package's.
- **Codex:** **LIVE.** Evidence: merged codex-authored PR **#1917**
  (`Merge pull request #1917 from menno420/codex/add-return-docstring-to-function-in-utils`,
  merge commit `f0737dee` on origin/main) + the standing @codex reviewer
  ruling Q-0258 with connector activity through the Sol/Codex evaluation
  thread #1938–#1943 (current-state ledger @ `dc19b1e8`; review-queue
  backfill notes carried the same evidence hub-side).

## Deployed-state per part (2026-07-10)

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — distillation for owner-started sessions | **`.claude/CLAUDE.md` IS the deployed instructions — in-repo, auto-loaded every session; no console paste exists or is required.** This file is the paste candidate only if the owner hosts superbot sessions in a Project whose console field is empty | superbot `.claude/CLAUDE.md` @ `dc19b1e8`; no deploy record anywhere (none needed) |
| 2 kickoff prompt | `coordinator-prompt.md` — manual session kickoff | NOT deployed (nothing to deploy — used per-session at will). NOTE the homing anomaly it supersedes: a pre-Q-0265 "superbot coordinator" seat package sits in substrate-kit `docs/succession/{custom-instructions-proposal,next-boot-2026-07-09,environment-spec}-superbot-coordinator.md` — **superseded by the Q-0264 no-seat ruling**, flagged for retirement during centralization | inventory-lanes.md §2 + §8 anomaly 1; router Q-0264 @ `dc19b1e8` |
| 3 setup script | `setup-script.sh` — bot-prod archetype, single-repo | The fleet standard for this repo is fm `environments/archetype-bot-prod.sh` (owner-paste convention; **no paste record** — what any console field actually holds is unverified) | fm `environments/archetype-bot-prod.sh` + `archetypes.md` @ `0eaa668` |
| 4 failsafe | `failsafe-prompt.md` — documents the deliberate absence | N/A by design — no trigger exists or should exist for a hub seat; the recon loop is issue-based (ROUTINE_PAT), verified firing (issue #1951) | Q-0264; `.github/workflows/reconciliation-trigger.yml` + current-state "Last updated" @ `dc19b1e8` |

## Sources

- superbot @ `dc19b1e8` (origin/main, fetched this session): `.claude/CLAUDE.md` ·
  `docs/AGENT_ORIENTATION.md` · `docs/current-state.md` header ·
  `docs/owner/maintainer-question-router.md` Q-0259/Q-0264/Q-0265 ·
  `docs/planning/gen3-deployment-standard-2026-07-10.md` ·
  `docs/eap/eap-program-review-2026-07-10.md` §5.9 · `substrate.config.json` ·
  `scripts/claude_session_start.sh` · `.github/workflows/reconciliation-trigger.yml` ·
  merge commit `f0737dee` (PR #1917, codex branch).
- fleet-manager @ `0eaa668` (origin/main, fetched this session):
  `environments/archetype-bot-prod.sh` · `environments/archetypes.md`
  (bot-prod row + superbot-legacy var-NAME row + the 3.10/3.11 wrinkle).
- Inventories (scratchpad `launch-packages/`): inventory-hub.md §E/§G item 1
  (no hub package by design) · inventory-lanes.md §2 kit succession rows +
  §8 homing anomaly.

**Last verified:** 2026-07-10 (all citations `git show`n from freshly-fetched
origin/main of both repos this session; note both heads are NEWER than the
inventory baselines `53fb5ef`/`702ba89` — no contradictions found on the
cited items).
