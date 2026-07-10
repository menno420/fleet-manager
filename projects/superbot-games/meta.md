# superbot-games — Project package meta

- **Seat:** games-plugins merged lane (mining + exploration, one repo, one
  clock — inbox ORDER 002's "merged-lane identity"). **PARKED + CLOCKLESS:**
  both gen-1 per-lane Projects wound down (exploration PR #13, mining PR #14,
  close-out heartbeats PRs #19/#20); no routine has EVER been armed for this
  repo; inbox ORDERs 001 (P0) and 002 (P1) are both `status: new`, unexecuted
  (`control/inbox.md` @ `4493292`).
- **Horizon (design constraint, not current state):** superbot router Q-0259
  ruling 5 — the games program becomes THREE dedicated game projects, each its
  own repo, booting post-core; the manager maps current lanes onto that shape
  decide-and-flag; Q-0262.7 already rules pokemon = QoL+. The 3 repos are
  owner-created ("not appliable by delegation"), none exist. This lane's
  modules must stay portable for that mapping — baked into the package's
  instructions + coordinator prompt.
- **Kit: v1.7.0, CURRENT — the dispatch's "v1.2.0 (5 behind)" is heartbeat
  drift, not tree state.** PR #22 (kit v1.2.0 → v1.7.0, sha256-verified
  release asset) merged 2026-07-10T20:22:34Z and IS the current HEAD
  `4493292`; `substrate.config.json` `kit_version: "1.7.0"`. The per-lane
  heartbeats still SAY `kit: substrate-kit v1.2.0` — PR #22's lane-owed
  follow-up 1 (update on next status overwrite); follow-up 2: per-lane status
  files are not in `heartbeat_files` (only `control/status.md` is — feeds the
  one-writer resolution below).
- **Cadence:** failsafe `0 */2 * * *` ("superbot-games failsafe wake", lane
  stagger; gen-3 standard §2), send_later/one-shot chain as pacemaker —
  **NOT ARMED** (ORDER 002 pending; this package's part 4 is the arming text).
  Wall on record, verbatim (mining close-out, `control/status-mining.md` @
  `4493292`): "No such tool available: mcp__claude-code-remote__send_later" —
  scheduler tools are SEAT-DEPENDENT (four sibling seats armed successfully
  the same day); re-probe each session.
- **Environment archetype:** `fleet-manager environments/archetype-python-lab.sh`
  (its header lists superbot-games as a consumer; both held gen-2 packages §3
  assign it). Package `setup-script.sh` = canonicalized merge of the repo's
  two per-lane scripts + capability probes. **Dir-inconsistency flag:** the
  repo keeps setup scripts in BOTH `environment/` (singular —
  setup-exploration.sh) and `environments/` (plural — setup-mining.sh).
  **Canonical = `environments/`** (plural; fleet + trading-strategy
  convention) — first session commits the canonical script there and retires
  the two per-lane copies.
- **Grants:** `menno420/superbot-games` only (Q-0260 single-writable-repo).
  Cross-repo READ (public raw): `menno420/superbot` (porting oracle),
  `menno420/superbot-next` (SubsystemManifest plugin contract) — declared in
  the held games-mining package §3. Variables: **none** (pure stdlib; Block-4
  ban on Railway IDs / tokens / DSNs stands).
- **Codex enabled: unknown.** Cheap check this session: GitHub issue-scoped
  search (`codex repo:menno420/superbot-games`) → 0 results; the endpoint
  cannot see PR review comments, so absence is not evidence. No Codex click
  recorded in any games package.

## Two-writer anomaly (the package's structural fix)

`control/status.md` — the kit's sole registered heartbeat file — was written
by BOTH gen-1 lanes: exploration's pointer text + mining's additively appended
heartbeat (PR #20), violating one-writer-per-file, while the real heartbeats
live in `control/status-{mining,exploration}.md` (the kit hardcodes a single
status file vs the repo's per-lane files — the standing ⚑ owner item in
`control/status-mining.md`). **Package resolution (decide-and-flag):** under
the merged-lane identity there is ONE writer again — adopt `control/status.md`
as the single coordinator-written status file with per-track sections; freeze
the per-lane files as historical pointers. Coordinator prompt step 5.

## Deployed-state per part (2026-07-10)

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — merged-lane, Q-0265/Q-0264 re-base | **Nothing current.** Gen-1 per-lane texts were deployed 2026-07-09 and live verbatim in fleet-manager `docs/prompts/game-{mining,exploration}.md` (living-ledger); those Projects are wound down. Gen-2 per-lane packages exist but are HELD (fm `docs/proposals/instructions/games-{mining,exploration}.md`, Q-0262.6) and are pre-Q-0265 + pre-merge-lane | fm @ `0eaa668`; superbot router Q-0262.6 @ `53fb5ef` |
| 2 coordinator prompt | `coordinator-prompt.md` — continuous, merged-lane | **Not deployed** — no live seat; gen-1 startup prompts (same fm prompt files) historical | fm `docs/prompts/` ledger |
| 3 setup script | `setup-script.sh` — canonicalized merge + probes | Two per-lane scripts committed in inconsistent dirs; whether either was ever pasted into a console field is **unrecorded** (paste convention, no receipt) | superbot-games `environment/setup-exploration.sh` + `environments/setup-mining.sh` @ `4493292` |
| 4 failsafe text | `failsafe-prompt.md` — §2b-adapted, `0 */2 * * *` | **NOT ARMED** — repo clockless; ORDER 002 (self-arm) status:new; mining seat's scheduler-tool denial on record verbatim | `control/inbox.md` ORDER 002 + `control/status-mining.md` @ `4493292` |

## P0 flag carried through the whole package

CI collects **73/121 tests** (pytest step runs `pytest tests/ -q`;
`games/exploration/tests/` — 48 tests — invisible). ORDER 001 (P0, status:new)
orders collect-ALL-suites + a collected-count floor assertion + evidence in
the PR body. **Post-#22 nuance the order text doesn't know:** the pytest step
now lives in `.github/workflows/tests.yml` (host carve-out — substrate-gate.yml
is kit-owned and regenerated on upgrades; hand edits there die), and `tests`
is a **non-required check** (PR #22 body flags it) — so the fix targets
tests.yml and the required-check flip is an owner click. Until merged, no
session may trust a green gate (instructions P0 rail; setup script prints the
real collected count at boot).

## Sources

- superbot-games @ `4493292` (origin/main, = PR #22 merge, 2026-07-10T20:22:34Z):
  `control/inbox.md` (ORDERs 001/002) · `control/status.md` +
  `control/status-{mining,exploration}.md` (two-writer anomaly, kit-line
  drift, walls verbatim) · `control/README.md` (multi-Project extension) ·
  `docs/lanes.md` (binding track map) · `docs/gen2-custom-instructions-exploration.md` +
  `docs/retro/proposed-custom-instructions-mining-2026-07-09.md` (the two
  pre-Q-0265 lane CI proposals) · `environment/setup-exploration.sh` +
  `environments/setup-mining.sh` · `.github/workflows/{substrate-gate,tests}.yml` ·
  `substrate.config.json` · PRs #16 #17 #18 #20 #21 #22 (PR #21 = landing-path
  verification, control fast lane, opened 15:53:33Z → merged 15:57:17Z).
- fleet-manager @ `0eaa668` (origin/main): `docs/prompts/game-{mining,exploration}.md`
  (deployed gen-1 texts, verbatim ledger) ·
  `docs/proposals/instructions/games-{mining,exploration}.md` (held gen-2
  packages; R21 landing evidence, archetype §3, ORDER 001 drafts) ·
  `environments/archetype-python-lab.sh`.
- superbot: router Q-0259 (r5 games program) + Q-0260/Q-0261 + Q-0262 (.6 hold,
  .7 pokemon QoL+) read from the local clone @ `4fac759`; Q-0263/Q-0264/Q-0265
  cited via the verified inventory (superbot @ `53fb5ef` L9511–9648 — the
  local clone predates them) + the part-4 brief §2b template as encoded in the
  sibling build packages (substrate-kit, superbot-next).
- Inventories (scratchpad `launch-packages/`): inventory-lanes.md §6 +
  missing-parts matrix; inventory-hub.md §A/§B/§C/§F.

**Last verified:** 2026-07-10 (~22:00Z) — all superbot-games and fleet-manager
citations fetched from origin/main via GitHub MCP this session.
