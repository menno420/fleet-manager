# Environment archetypes — the fleet's consolidated environments (4 + gba-lab)

> **Status:** `living-ledger`
>
> Owner directive 2026-07-09: consolidate every current + planned project's
> environment into **at most 4 archetypes**, each with ONE tested defensive
> setup script and the union of env var **NAMES** it serves (names only —
> NEVER values; `README.md` hard rule). Derived from the per-lane env specs
> gathered at HEAD 2026-07-09 (substrate-kit `docs/gen2/environment-setup.md`,
> websites `docs/succession/environment-spec-2026-07-09.md`, trading-strategy
> `docs/succession/ENVIRONMENT.md`, the three codetool
> `docs/succession/ENVIRONMENT.md`s, superbot-games
> `docs/succession-exploration.md`, superbot-next packaging/CI, and this
> repo's `multi-repo.md`).
>
> All four scripts follow the fleet canonical shim contract
> ([`templates/setup-universal.sh`](templates/setup-universal.sh), playbook
> R15): `set +e`, `.git`-based multi/single-repo detection, per-repo manifest
> guards, `scripts/env-setup.sh` escape hatch, **unconditional `exit 0`** —
> and each ran clean in-container on a representative layout, **including the
> bare two-source checkout that killed 2 trading-strategy sessions at
> provision** (test transcripts in PR #10's body).

> **Authorization layer:** this doc maps env-var **NAMES** per project; which of
> them to actually **grant**, at what scope, and how much room to give each lane
> lives in [`env-grant-policy.md`](env-grant-policy.md) (trust tiers + templates +
> where-to-manage links).

## The archetypes

*(The owner's original directive said ≤4; **gba-lab is the 5th by explicit
justification** — the GBA cross-compile toolchain (devkitARM r68 + agbcc +
mGBA headless, all apt/mirror/source-built) is far too heavy to fold into
python-lab, and no other archetype may carry it. Added 2026-07-09 night with
the game-lab founding package; decide-and-flag, vetoable.)*

| Archetype | Script | Shape | Serves |
|---|---|---|---|
| **python-lab** | [`archetype-python-lab.sh`](archetype-python-lab.sh) | stdlib-or-tiny-deps Python lab; zero secrets; no services; single repo (multi-repo safe) | substrate-kit, codetool-lab-fable5, codetool-lab-opus4.8, codetool-lab-sonnet5, superbot-games, fleet-manager, venture-lab, sim-lab, product-forge, idea-engine, superbot-idle, mobile-lab |
| **pinned-research** | [`archetype-pinned-research.sh`](archetype-pinned-research.sh) | pinned-`requirements*.txt` research/service lane; zero-to-few secrets; no local DB; may be a **two-source workspace** | trading-strategy, websites |
| **bot-prod** | [`archetype-bot-prod.sh`](archetype-bot-prod.sh) | production Discord bot; Postgres; hash-pinned lockfile; per-repo CI interpreter pins (superbot → `python3.10`, superbot-next → `python3.11`); non-mutating workspace-residue advisory (dead-branch/dirty-tree report + `git checkout main && git pull --ff-only` recovery hint); **the only archetype allowed production-pointing vars** | superbot-next, superbot (legacy) |
| **coordinator** | [`archetype-coordinator.sh`](archetype-coordinator.sh) | N-repo workspace (cwd is NOT a repo); superset manifest handling + dual interpreter | the live `multi-repo` env (fleet-manager coordination sessions) |
| **gba-lab** | [`archetype-gba-lab.sh`](archetype-gba-lab.sh) | GBA cross-compile lab: devkitARM r68 (leseratte10 mirror route) + agbcc + binutils-arm-none-eabi + mGBA headless loop (`mgba-sdl` + pip `mgba==0.10.2`) + xdelta3 patch tooling; zero secrets; no services | **gba-homebrew (planned, public)**, **pokemon-mod-lab (planned, PRIVATE)** — the game-lab venture |

## The base shim + knob table (R2, ORDER 018 — 2026-07-11)

The four Python-family archetype scripts above are now **thin configs over ONE
base shim**, [`setup-base.sh`](setup-base.sh) — the audit (§4.2, 2026-07-11)
found the multi/single-repo detection block byte-identical in all 5 scripts
and coordinator's manifest ladder a strict superset of the other three, so
all shared logic lives in the base and each archetype is a ~25-line knob
diff. **gba-lab stays a genuinely separate full script** (heavy
apt/mirror/source toolchain — the audit's own carve-out).

Each thin config resolves the base in order: `$FLEET_SETUP_BASE` override →
`environments/setup-base.sh` (cwd IS fleet-manager) →
`fleet-manager/environments/setup-base.sh` (workspace child) → alongside the
script file → raw fetch from `fleet-manager/main` (Q-0260 path). If all fail
it warns and still exits 0 (R15) — the session lives, installs run in-session.

| Knob | python-lab | coordinator | bot-prod | pinned-research |
|---|---|---|---|---|
| `BASELINE_PIP` | `pytest ruff build` | `pytest ruff` | *(none)* | `pytest python-multipart` |
| `PICK_PYTHON_TABLE` | *(none — python3)* | `superbot=python3.10 superbot-next=python3.11` | `superbot=python3.10 superbot-next=python3.11` | *(none — python3)* |
| `ENV_REPORT` | *(none)* | *(none)* | `DISCORD_BOT_TOKEN_PRODUCTION DATABASE_URL SB_DATA_PLANE YOUTUBE_API_KEY` | `GITHUB_TOKEN GITHUB_PAT RAILWAY_API_KEY SITE_PASSWORD DATABASE_URL` |
| `GIT_TRIAGE` (branch/dirty report, never mutates) | 0 | 0 | 1 | 1 |

Notes:

- **Audit §4.2 latent-bug fix:** coordinator's `pick_python` previously had
  NO `superbot-next→python3.11` case (superbot-next, a child of the live
  multi-repo env, installed under bare `python3` — correct only by luck). The
  pin table is now data shared with bot-prod, so both carry both cases.
- The base's manifest ladder is the coordinator superset for every archetype:
  `scripts/env-setup.sh`|`scripts/setup-env.sh` → `requirements.lock`
  (hash-pinned) → `requirements*.txt` (depth 2, each individually) →
  `pyproject.toml` (`[dev]` then `-e .`) → skip. python-lab therefore now
  also picks up `requirements-dev.txt` / lockfiles if a lab ever grows one —
  intended superset behavior.
- A second consolidation fix: `pick_python`'s missing-interpreter WARNING now
  goes to stderr — it is called via command substitution, so the old stdout
  warning would have been captured into the interpreter variable and
  corrupted it (latent in every pre-consolidation copy).
- The thin configs are **re-derived and unverified-as-thin-configs** until
  the next owner paste / lane boot runs one end-to-end (Q-0105 posture); the
  pre-consolidation scripts they replace were in-container tested (PR #10).

### R3 disposition — gba-lab's two lane gaps (ORDER 018, 2026-07-11)

- **(a) Patch/distribution tooling — FIXED IN-SCRIPT:** `xdelta3` added to the
  apt baseline. The ROM itself is un-distributable, so a shipping pokemon mod
  necessarily emits base→modded patches; xdelta3 is the in-apt-archive patch
  tool and covers that the moment the lane ships. Confirming pokemon-mod-lab's
  exact shipping model from fleet side is walled (PRIVATE repo — raw reads
  need a grant this session doesn't hold), but the add is tiny, harmless for
  Track B, and required under every patch-shipping model. **`flips` (Floating
  IPS) NOT added — why-not:** it is not in the Ubuntu apt archive; installing
  it would mean another unsigned source build, the exact supply-chain surface
  R3(b) exists to shrink. If the lane specifically needs BPS/IPS output, it
  adds a pinned build via its own `scripts/env-setup.sh` escape hatch.
- **(b) devkitARM Track-B gating — FIXED IN-SCRIPT:** the Block-3 unsigned
  leseratte10-mirror pull is now gated behind homebrew detection — it runs
  only when a checked-out repo is NOT pokeemerald-shaped (the Block-4
  `include/global.h` + `Makefile` signature), or when no repos are visible
  (bare/unknown layout keeps the proven pre-gate behavior), or on
  `GBA_TRACK_B=force`; `GBA_TRACK_B=skip` disables it outright. A
  pokeemerald-only env no longer pulls a toolchain it never uses.

### R6 decision — mobile-lab's shape (⚑ decide-and-flag, ORDER 018, 2026-07-11)

**Decision: the repo escape-hatch STAYS; no node-lab knob is built today.**
mobile-lab remains registered **python-lab** with its Node/Expo toolchain
riding the repo's own `scripts/env-setup.sh` (which every archetype prefers
automatically). Rationale: mobile-lab is the fleet's ONLY JS lane — a
`node-lab` knob on the base shim would be speculative surface serving one
held, unlaunched lane. **Named promotion path (binding when triggered):** the
moment a SECOND JS lane appears, promote a thin `node-lab` knob (e.g.
`BASELINE_NPM`) on `setup-base.sh` rather than repeating the escape-hatch or
minting a 6th archetype — per the audit's own R6 reasoning. ⚑ Vetoable;
flagged on the ORDER 018 run report.

## Project → archetype mapping (EVERY current + planned project)

| Project (repo) | Archetype | Env var NAMES the env must carry (owner-set) | Notes |
|---|---|---|---|
| menno420/substrate-kit | **python-lab** | *(none)* | stdlib-only, no requirements.txt; script installs pytest+ruff+build baseline. Future/owner-gated only: `RAILWAY_TOKEN` (kit-lab-scoped), a read-only cross-repo PAT (only if P13 is picked) |
| menno420/codetool-lab-fable5 (envdrift) | **python-lab** | *(none)* | zero-dependency; repo ships `scripts/env-setup.sh` — the shim prefers it automatically |
| menno420/codetool-lab-opus4.8 (mdverify) | **python-lab** | *(none)* | pyproject `[dev]` editable path; node/ruby deliberately not required |
| menno420/codetool-lab-sonnet5 (cfgdiff) | **python-lab** | *(none required)* — optional `PYPI_API_TOKEN` (manual twine fallback ONLY; prefer OIDC trusted publishing, no stored secret) | PyYAML/tomli/tomli-w via pyproject editable path |
| menno420/superbot-games | **python-lab** | *(none)* | pure-stdlib domains; Block-4-class ban stands: never add Railway IDs / Discord tokens / DSNs / API keys here |
| menno420/fleet-manager | **python-lab** | *(none)* | docs/control repo; stdlib `bootstrap.py` |
| menno420/venture-lab (planned) | **python-lab** | *(none at launch)* | gen-2 born-right pilot; quality floor = substrate-kit; NO spend/account/publish vars without owner action |
| menno420/superbot-idle | **python-lab** | *(none)* | ⚠ was a LIVE seat naming NO archetype until 2026-07-11 (audit R1's highest-priority drift — registered here doc-only); Seat B games lane, no setup-script.sh deployed (`projects/superbot-idle/meta.md`) |
| menno420/sim-lab | **python-lab** | *(none)* | registered 2026-07-11 (audit R1 — was self-flagged unregistered); round-3 lane, archetype script already reused verbatim (`projects/_inventory/inventory-hub.md`) |
| menno420/product-forge | **python-lab** | *(none)* | registered 2026-07-11 (audit R1 — was self-flagged unregistered); round-3 lane, archetype script already reused verbatim |
| menno420/idea-engine | **python-lab** | *(none)* | registered 2026-07-11 (audit R1); markdown-first repo, stdlib `bootstrap.py`; round-3 lane, archetype script already reused verbatim |
| menno420/mobile-lab (held) | **python-lab** | *(none)* | registered 2026-07-11 (audit R1); Node/Expo toolchain rides the repo `scripts/env-setup.sh` escape hatch — R6 DECIDED 2026-07-11 (ORDER 018): escape-hatch stays; a `node-lab` knob on `setup-base.sh` is the named promotion path if a second JS lane appears (§ "R6 decision" above) |
| menno420/gba-homebrew (planned, public) | **gba-lab** | *(none)* | Track B (Butano original homebrew); devkitARM via the leseratte10 r68 mirror route (⚠ unsigned community infra — supply-chain caveat in [`../docs/findings/gba-toolchain-proof-2026-07-09.md`](../docs/findings/gba-toolchain-proof-2026-07-09.md)); publish-safe code only |
| menno420/pokemon-mod-lab (planned, PRIVATE) | **gba-lab** | *(none)* | Track A (pokeemerald mod); agents mirror pret/pokeemerald in; **Nintendo-copyrighted material — PRIVATE only, never publish/commit ROMs or extracted assets publicly** |
| menno420/trading-strategy | **pinned-research** | *(none)* — proxy vars (`HTTPS_PROXY`, `REQUESTS_CA_BUNDLE`) and git auth are platform-provided | Python **3.11** floor (container 3.11.15 OK). **Its env is a TWO-SOURCE workspace** (trading-strategy + substrate-kit as cwd children) — the layout that killed 2 sessions; this archetype's script is tested against exactly that shape |
| menno420/websites | **pinned-research** | `GITHUB_PAT`, `RAILWAY_API_KEY`, `SITE_PASSWORD`, `DATABASE_URL` (websites app DB); service-side/optional: `AUTOREFRESH_SECONDS`, `PORT` | THREE requirements files (root/botsite/dashboard) — script installs each individually; extras pytest+python-multipart baked in. Container is 3.11.x, production Dockerfiles 3.12 — do not assume 3.12 locally. **DENYLISTED here:** `RAILWAY_PROJECT_ID`/`RAILWAY_ENVIRONMENT_ID`/`RAILWAY_SERVICE_ID` (production-pointing; CI-enforced by `scripts/check_no_ambient_railway_ids.py`) |
| menno420/superbot-next | **bot-prod** | Required fail-fast: `DISCORD_BOT_TOKEN_PRODUCTION`, `DATABASE_URL`. Ops: `BOT_PREFIX`, `BOT_OWNER_USER_ID`, `EXTRA_OWNER_USER_IDS`, `DISCORD_WEBHOOK_URL`, `LOG_LEVEL`, `HEALTH_PORT`, `HEALTH_HOST`, `AUTO_SYNC_COMMANDS`, `STRICT_DISABLED`, `IDENTITY_CONTRACT_STRICT`, `HEALTH_GROUPED_FINDINGS`, `AUTOMATION_SCHEDULER_ENABLED`. AI (dormant unkeyed): `AI_ENABLED`, `AI_DEFAULT_PROVIDER`, `AI_FALLBACK_PROVIDER`, `AI_TOOLS_ENABLED`, `AI_SERVER_MEMBER_LOOKUP_ENABLED`, `AI_TASKS_DISABLED`, `AI_TASK_ROUTING`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `SETUP_ADVISOR_PROVIDER`, `SETUP_ADVISOR_OPENAI_MODEL`. BTD6/media: `PARAGON_API_KEY`, `PARAGON_API_BASE_URL`, `BTD6_*` family, `YOUTUBE_API_KEY`. Plane/platform: `SB_DATA_PLANE`, `SB_TEST_DB_HOSTS`, `SB_PROD_ATTEST`, `SB_VERIFY_BOOT`, `SB_APPCMD_SYNC_GUILD_ID`, `SB_INTENT_MEMBERS_OK`, `SB_INTENT_MSGCONTENT_OK`, `RAILWAY_SERVICE_NAME`. Routines: `CLAUDE_ROUTINE_FIRE_URL`, `CLAUDE_ROUTINE_TOKEN`, `CLAUDE_ROUTINE_BETA`, `CLAUDE_ROUTINE_VERSION`, `CONTROL_API_TOKEN`. DB tuning: `DB_COMMAND_TIMEOUT_S`, `DB_IDLE_LIFETIME_S` | Python **3.11** (all CI jobs pinned); hash-pinned `requirements.lock` (`--require-hashes` — the script's dedicated branch); **needs Postgres** (CI uses postgres:18). Smallest-set rule still applies: a test-plane env sets only what the session needs |
| menno420/superbot (legacy) | **bot-prod** | `DATABASE_URL`, `DISCORD_BOT_TOKEN_PRODUCTION`, `RAILWAY_API_KEY`, `RAILWAY_PROJECT_ID`, `RAILWAY_SERVICE_ID`, `RAILWAY_ENVIRONMENT_ID`, `OPENAI_API_KEY`, `GITHUB_PAT` (the observed live set) | **Python 3.10 CI parity** — the script pins `python3.10 -m pip` for this repo by name (see wrinkle below) |
| live `multi-repo` coordinator env | **coordinator** | Union as observed live 2026-07-09 (`templates/env-vars.md`): `GITHUB_PAT`, `OPENAI_API_KEY`, `DATABASE_URL`, `DISCORD_BOT_TOKEN_PRODUCTION`, `RAILWAY_API_KEY`, `RAILWAY_PROJECT_ID`, `RAILWAY_SERVICE_ID`, `RAILWAY_ENVIRONMENT_ID` | cwd = workspace with repo children (substrate-kit, superbot, superbot-games, superbot-next, websites, …) |

**Platform-injected everywhere (never set manually):** `GITHUB_TOKEN`,
`ANTHROPIC_BASE_URL`, proxy plumbing (`HTTPS_PROXY`, CA bundle).

## ⚠️ The 3.10-vs-3.11 wrinkle (and its cousins)

1. **Container default `python3` is 3.11.x; legacy superbot's CI parity is
   3.10** (`multi-repo.md` wrinkle #1). A bare `python3 -m pip` installs into
   the wrong site-packages for superbot work. Both `bot-prod` and
   `coordinator` scripts pin `python3.10 -m pip` for the repo named
   `superbot` (with a logged fallback if 3.10 is absent). The durable fix
   remains a `scripts/env-setup.sh` in superbot itself — every archetype
   script prefers it automatically.
2. **websites:** container 3.11.x vs production Dockerfiles 3.12 — pinned
   deps install cleanly on both; "the gen-2 lane should not assume 3.12
   locally" (its spec's explicit warning).
3. **trading-strategy / superbot-next need >=3.11; the labs floor at
   3.9–3.10** — the container's 3.11.15 satisfies every lane except legacy
   superbot's parity case (#1). No archetype needs a third interpreter.

## Non-negotiables (paid for in blood, 4+ lanes)

Every archetype script: always exits 0 · never assumes cwd is a repo ·
no bare `pip install -r` without an existence guard · `.git`-based
multi/single-repo detection · per-repo `scripts/env-setup.sh` escape hatch ·
one broken repo never blocks the others · env var NAMES only, smallest set,
**production trio excluded outside bot-prod/coordinator**.

## Owner paste-steps (click path, per environment)

1. **claude.ai/code → Environments → New environment** (or edit existing).
2. Name it after the archetype (+ lane if split, e.g. `pinned-research-trading`).
3. Add the repo(s) from the mapping row.
4. **Setup script:** paste the full contents of the archetype's
   `environments/archetype-<name>.sh`.
5. **Environment variables:** add each NAME from the mapping row with its
   real value (values live only in the claude.ai panel — never in the repo).
6. Save; in the target Project → settings → Environment, select it.
7. The next session in that env verifies boot and flips the lane spec's
   `Verified` line.
