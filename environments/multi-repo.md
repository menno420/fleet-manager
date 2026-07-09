# Environment spec — `multi-repo` (LIVE)

> **Status:** `living-ledger` — spec of the CURRENT live environment, as built.
> Written 2026-07-09 **from inside the running environment** (facts below
> verified live, not assumed). Names + placeholders only — no values (registry
> hard rule).

## Identity

- **Name:** `multi-repo`
- **Where it exists:** claude.ai/code → Environments (owner-side; agents cannot
  edit it — platform wall, see `README.md`)
- **Verified:** 2026-07-09 (repo list, interpreters, var names checked in-session)

## Repos checked out (workspace children of `/home/user`)

- `substrate-kit`
- `superbot`
- `superbot-games`
- `superbot-next`
- `websites`

## Setup script

The defensive multi-repo shim — canonical copy:
[`templates/setup-universal.sh`](templates/setup-universal.sh). Per-repo
detection (`scripts/env-setup.sh` if present, else `pip install -r
requirements.txt`), every step non-fatal, always exits 0 (playbook R15).
As of 2026-07-09 **no repo in this env ships `scripts/env-setup.sh` yet**, so
every Python repo takes the `requirements.txt` branch under `python3`.

## Environment variables (NAMES only — values live in claude.ai)

`GITHUB_PAT` · `OPENAI_API_KEY` · `DATABASE_URL` · `DISCORD_BOT_TOKEN_PRODUCTION` ·
`RAILWAY_API_KEY` · `RAILWAY_PROJECT_ID` · `RAILWAY_SERVICE_ID` ·
`RAILWAY_ENVIRONMENT_ID` — plus platform-injected `GITHUB_TOKEN` /
`ANTHROPIC_BASE_URL`. Schema + the Railway-trio DANGER note:
[`templates/env-vars.md`](templates/env-vars.md). **This env is
production-pointing** (Railway set, prod DSN, prod bot token) — that is correct
for the superbot/manager lanes and exactly why non-superbot envs must not copy
this var list.

## Which Projects use it

- **fleet-manager** (the manager Project and its workers — this spec was written
  by one, running inside it). *Verified 2026-07-09.*
- Lanes whose repos are mounted here (superbot, superbot-next, superbot-games,
  substrate-kit, websites) can be served by it; **per-Project attachment is
  owner-side UI the manager cannot read** — `<TO-CONFIRM by owner>` which other
  Projects have it selected. Update this list as answers arrive; don't guess.

## Known wrinkles

1. **Default interpreter is 3.11, superbot needs 3.10.** `python3` →
   **3.11.15**; `python3.10` (**3.10.20**) is also present. The shim's bare
   `python3 -m pip install` puts deps in **3.11 site-packages**, while
   superbot's CI parity rule pins everything to `python3.10 -m …` — so
   superbot work must `python3.10 -m pip install -r requirements.txt` (or,
   better: superbot grows a `scripts/env-setup.sh` that pins its interpreter,
   which the shim will then prefer automatically).
2. **Production is ambient.** The Railway trio + prod DSN + prod bot token are
   in every session in this env; workers must treat destructive ops per the
   superbot Q-0213 brake. Non-superbot environments: exclude these vars.
3. **Multi-repo = shared blast radius.** One env serves many lanes; a var added
   "for one repo" is visible to all sessions in the env. Prefer a per-Project
   env (see `SPEC-TEMPLATE.md`) when a lane needs anything sensitive.
