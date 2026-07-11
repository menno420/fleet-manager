# substrate-kit — Project package meta

- **Seat:** core seat 2 (Q-0261) — the fleet's mechanism repo + distribution
  seat. **LIVE** — booted 2026-07-10 (inventory-hub §E row "substrate-kit …
  Seat LIVE (booted 2026-07-10)"; live coordinator session
  `session_01YMJrUDpcarFsqPZ2BeeiVB` per kit `control/status.md` @ `7e600c6`).
- **Cadence:** `0 */2 * * *` (even hours :00; core-seat stagger — lanes
  `0 */2`, manager `30 */2`; gen-3 standard §2). Under Q-0265 the cron is the
  dead-man failsafe; the send_later ~15-min chain is the pacemaker.
- **Environment archetype:** `fleet-manager environments/archetype-python-lab.sh`
  **verbatim** (founding package §3: "the kit lane already runs on it";
  fm `environments/archetypes.md` @ `702ba89`). The package's
  `setup-script.sh` here is the kit's bespoke probe variant
  (docs/gen2/setup.sh base + capability probes) for the console field —
  assembler/owner picks one lineage; the archetype is the fleet standard.
- **Grants:** `menno420/substrate-kit` + **ALL fleet lane repos** — the second
  Q-0260 exception, Q-0261.3 write-all for distribution, hard-scoped
  (router Q-0261 item 3 @ superbot `53fb5ef`; founding package §3 repo list:
  superbot, superbot-next, fleet-manager, websites, trading-strategy,
  venture-lab, superbot-games, pokemon-mod-lab (private — attach is the only
  path), gba-homebrew, product-forge; codetool arms excluded/archived).
  Variables: none.
- **Codex: ENABLED (owner, 2026-07-11)** — Codex environments exist for all
  12 active fleet repos, the kit included (owner update 2026-07-11 ~00:2xZ,
  fm inbox ORDER 014); supersedes the 2026-07-10 "unknown" verdict. Quota
  refusals are RETRY-LATER, never a wall (fm `projects/README.md` § Codex
  fleet-wide enablement).

## Deployed-state per part (2026-07-10)

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — Q-0265/Q-0264 re-base of founding §1 | Founding §1 text pasted at the 2026-07-10 boot (pre-Q-0265 "ONE bounded slice" session shape); no in-repo paste receipt | superbot `docs/planning/round3-founding-package-substrate-kit-2026-07-10.md` §1 @ `53fb5ef`; inventory-hub §E; inventory-lanes §2 "Custom-Instructions deploy record" missing |
| 2 coordinator prompt | `coordinator-prompt.md` — continuous-mode rewrite of founding §2 | Founding §2 brief pasted at boot; live seat amended to continuous by the §2b chat-paste ONLY (no committed record in the kit repo) — the founding doc is the sole round-3 package with NO Q-0265 banner | founding package §2 @ `53fb5ef`; part-4 brief §2b @ `53fb5ef`; inventory-hub §E kit row |
| 3 setup script | `setup-script.sh` — docs/gen2/setup.sh + probe block | `docs/gen2/setup.sh` was the OA8 paste candidate; owner-paste convention, **no paste record** — what the console field actually holds is unverified | kit `docs/gen2/setup.sh` @ `7e600c6`; inventory-lanes §2 row 1 |
| 4 failsafe text | `failsafe-prompt.md` — §2b template adapted | **NOT deployed.** Live trigger is the OLD standing wake `trig_016EfUawz6KxEYqUM6f1BqDw` "substrate-kit 2-hourly standing wake", cron `0 */2 * * *`, created 2026-07-10T15:53:36Z; its prompt is uncommitted (status: "matched the coordinator's spec character-for-character" → RECONSTRUCTED = founding §2 step-3 text). This file is the next self-re-arm's replacement text | kit `control/status.md` § ROUTINE STATE @ `7e600c6`; inventory-lanes §2 |

## Sources

- superbot @ `53fb5ef` (origin/main): `docs/planning/round3-founding-package-substrate-kit-2026-07-10.md` ·
  `docs/planning/gen3-deployment-standard-2026-07-10.md` ·
  `docs/planning/round3-dispatch-part4-brief-2026-07-10.md` §2b ·
  `docs/owner/maintainer-question-router.md` Q-0261 (L9410) / Q-0262 / Q-0263 / Q-0264 (L9511) / Q-0265-via-gen3-standard.
- substrate-kit @ `7e600c6` (origin/main): `docs/gen2/setup.sh` ·
  `docs/gen2/next-boot.md` §0 · `control/status.md` (ROUTINE STATE + health:
  852 tests passed at PR #133; check --strict exit 0; dist byte-pin clean) ·
  `.github/workflows/ci.yml` (job `kit-quality` + legacy alias jobs "Kit test
  suite" / "Cold-adoption smoke (adopt + check --strict)"; control fast lane) ·
  `.github/workflows/auto-merge-enabler.yml` (required-check `kit-quality`
  target; `do-not-automerge` carve-out) · `docs/CAPABILITIES.md` (THE
  DISCOVERY RULE) · `src/engine/templates/` (20 templates — working-agreement
  family only; no setup-script/seat-prompt/failsafe templates, the known kit
  gap).
- websites @ `4056909`: `docs/project/setup-script.sh` (capability-probe
  pattern; PR #47 fail-soft lesson).
- Inventories (scratchpad `launch-packages/`): inventory-lanes.md §2 +
  missing-parts matrix; inventory-hub.md §A row 7, §E, §F.

**Last verified:** 2026-07-10 (all citations fetched/`git show`n from
origin/main this session).
