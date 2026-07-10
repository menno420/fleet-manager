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

## The archetypes

*(The owner's original directive said ≤4; **gba-lab is the 5th by explicit
justification** — the GBA cross-compile toolchain (devkitARM r68 + agbcc +
mGBA headless, all apt/mirror/source-built) is far too heavy to fold into
python-lab, and no other archetype may carry it. Added 2026-07-09 night with
the game-lab founding package; decide-and-flag, vetoable.)*

| Archetype | Script | Shape | Serves |
|---|---|---|---|
| **python-lab** | [`archetype-python-lab.sh`](archetype-python-lab.sh) | stdlib-or-tiny-deps Python lab; zero secrets; no services; single repo (multi-repo safe) | substrate-kit, codetool-lab-fable5, codetool-lab-opus4.8, codetool-lab-sonnet5, superbot-games, fleet-manager, **venture-lab (planned)** |
| **pinned-research** | [`archetype-pinned-research.sh`](archetype-pinned-research.sh) | pinned-`requirements*.txt` research/service lane; zero-to-few secrets; no local DB; may be a **two-source workspace** | trading-strategy, websites |
| **bot-prod** | [`archetype-bot-prod.sh`](archetype-bot-prod.sh) | production Discord bot; Postgres; hash-pinned lockfile; per-repo CI interpreter pins (superbot → `python3.10`, superbot-next → `python3.11`); non-mutating workspace-residue advisory (dead-branch/dirty-tree report + `git checkout main && git pull --ff-only` recovery hint); **the only archetype allowed production-pointing vars** | superbot-next, superbot (legacy) |
| **coordinator** | [`archetype-coordinator.sh`](archetype-coordinator.sh) | N-repo workspace (cwd is NOT a repo); superset manifest handling + dual interpreter | the live `multi-repo` env (fleet-manager coordination sessions) |
| **gba-lab** | [`archetype-gba-lab.sh`](archetype-gba-lab.sh) | GBA cross-compile lab: devkitARM r68 (leseratte10 mirror route) + agbcc + binutils-arm-none-eabi + mGBA headless loop (`mgba-sdl` + pip `mgba==0.10.2`); zero secrets; no services | **gba-homebrew (planned, public)**, **pokemon-mod-lab (planned, PRIVATE)** — the game-lab venture |

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
