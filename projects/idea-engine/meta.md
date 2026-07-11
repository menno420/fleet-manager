# idea-engine — package meta

| Field | Value |
|---|---|
| Seat | **Idea Engine** — core seat 4, **LIVE** (the Q-0264 origin + the Q-0265 reference implementation) |
| Repo | `menno420/idea-engine` (public) — verified at origin/main **c8651f7** (2026-07-10, PR #16 merged; 13 slices shipped, outbox depth 3, backpressure held) |
| Cadence | Failsafe cron `0 */2 * * *` — **even hours :00, 2-hourly**. Pipeline stagger (inter-Project contract, centralize as a pair): engine even → sim-lab odd (`0 1-23/2 * * *`) → manager `30 */2 * * *` |
| Operating model | Continuous per Q-0265 — `send_later` continuation chain (~15 min) is the pacemaker; the cron is a dead-man failsafe only. Backpressure brake (Q-0265.4, this seat's named brake): proposal-generating probes pause while several outbox proposals sit unpulled; harvest/groom/repo-internal work continues |
| Env archetype | **python-lab, reused verbatim** — founding package §0.3 names `fleet-manager/environments/archetype-python-lab.sh` verbatim as this env's setup script. **⚠ SPEC MISSING:** fleet-manager `environments/archetypes.md` @ **0eaa668** has NO idea-engine row in either table (Serves list or Project→archetype mapping) — assembler should note it so the manager adds the row (same gap for sim-lab and product-forge). Repo is stdlib-only at HEAD (no requirements.txt / pyproject.toml — verified by import scan); part-3 script keeps the manifest branches for future growth |
| Grants | Writable: `idea-engine` ONLY (single-writable-repo rule Q-0260). Reads: **public raw of all fleet lanes** (`raw.githubusercontent.com/menno420/<repo>`) — the harvest path. Carve-out: pokemon-mod-lab is PRIVATE ⇒ DARK to this seat (raw 404 + MCP scope denial + git auth wall, verified live per status @ c8651f7 notes); harvest skipped + flagged, never guessed. Env vars: none. No secrets ever |
| Codex | **ENABLED (owner, 2026-07-11)** — Codex environments exist for all 12 active fleet repos (owner update 2026-07-11 ~00:2xZ, fm inbox ORDER 014); supersedes the 2026-07-10 "unknown" cheap-check verdict. The repo's @codex post-merge conventions (README § Landing conventions, Q-0258) are live paths now. Quota refusals are RETRY-LATER, never a wall (fm `projects/README.md` § Codex fleet-wide enablement) |

## Deployed-state per part

| Part | State |
|---|---|
| 1 · instructions.md | **DEPLOYED (equivalent live)** — the Project runs the founding package v2 §1 Custom Instructions (pasted at boot) as amended by the owner-pasted §2b Q-0265 block. This file is the centralized post-amendment consolidation (adds Q-0265 continuous/backpressure, the live landing conventions incl. `scripts/preflight.py` [PR #16], card markers, the cadence-pair contract); the deployed paste itself is not committed anywhere — founding §1 + §2b are the closest committed twins |
| 2 · coordinator-prompt.md | **DEPLOYED (equivalent live, chat-only)** — the live coordinator chat holds founding §2 boot brief + the §2b amendment; the loop it runs is observable in `control/status.md` (mode: continuous, backpressure line, chain alive). This file is the reconstructed, paste-ready standing prompt for re-boot/succession — as such **not previously committed** |
| 3 · setup-script.sh | **DEPLOYED (by reference)** — the env was created with `archetype-python-lab.sh` verbatim per founding §0.3; this copy = same shim + a websites-pattern capability probe (additive, fail-soft, still exit-0). Not in the idea-engine repo (no `environments/` there) |
| 4 · failsafe-prompt.md | **DEPLOYED + VERIFIED, committed verbatim** — `trig_0178q9Je2xRFJgthwamrg9Br`, enabled, self-bound to `session_01TwoaFmWeB8pYbHMyFYgjqJ`, verified via `list_triggers`; full delete+create JSON committed in `control/status.md` routine line (the only committed-verbatim deployed failsafe in the fleet besides superbot-next's) |

## Sources (all verified this build, 2026-07-10)

- idea-engine @ **c8651f7** (origin/main, fetched fresh): `README.md` (pipeline contract, § Landing conventions incl. preflight line, probe battery, outbox grammar, cadence ruling), `control/status.md` (routine cutover verbatim, mode/backpressure/notes), `control/README.md` (bus protocol, claim ritual, OWNER-ACTION format), `control/outbox.md` (PROPOSALs 001–003), `control/inbox.md` (empty — no manager ORDERs yet), `CONSTITUTION.md`, `docs/CAPABILITIES.md`, `.sessions/README.md` (born-red card + four markers), `.github/workflows/substrate-gate.yml` (control fast lane), `scripts/` import scan (stdlib-only)
- superbot @ **dc19b1e8** (origin/main, fetched fresh): `docs/planning/round3-founding-package-idea-engine-2026-07-10.md` (v2, Q-0265-amended banner; §§0–4), router **Q-0264** (pipeline directives 1–8) + **Q-0265** (continuous mode 1–7), `docs/planning/gen3-deployment-standard-2026-07-10.md` (§2 standards incl. Q-0266 volume-first), `docs/planning/round3-dispatch-part4-brief-2026-07-10.md` §2b (amendment block verbatim)
- fleet-manager @ **0eaa668** (origin/main, fetched fresh): `environments/archetype-python-lab.sh` (the R15 shim), `environments/archetypes.md` (mapping table — idea-engine row absent)
- Inventory: `launch-packages/inventory-games-new.md` §8 (idea-engine row — cutover-verbatim finding) + `inventory-hub.md` (founding-package classification, archetype reuse note)

**Last verified:** 2026-07-10 ~21:1xZ (all three repos fetched to origin/main this build; GitHub search for Codex evidence same time).
