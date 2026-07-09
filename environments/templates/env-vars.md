# Environment variables — standard fleet schema

> **Status:** `living-ledger` — variable **NAMES + purpose + placeholder** only.
> **NEVER a real value** (registry hard rule, `environments/README.md`). Real
> values are set solely in claude.ai/code → Environments → environment variables.
>
> Placeholder convention: every value in a spec is written **`<SET-IN-CLAUDE-AI>`**.
> Names observed live in the `multi-repo` environment on 2026-07-09.

## Owner-set fleet variables

| Name | Purpose (one line) | Value in specs |
|---|---|---|
| `GITHUB_PAT` | Owner's GitHub PAT for operations the app-scoped `GITHUB_TOKEN` is walled from | `<SET-IN-CLAUDE-AI>` |
| `OPENAI_API_KEY` | OpenAI access for the bot's AI features / cross-model checks | `<SET-IN-CLAUDE-AI>` |
| `DATABASE_URL` | SuperBot production Postgres DSN (Railway) — **production-pointing** | `<SET-IN-CLAUDE-AI>` |
| `DISCORD_BOT_TOKEN_PRODUCTION` | Live production Discord bot token — **production-pointing** | `<SET-IN-CLAUDE-AI>` |
| `RAILWAY_API_KEY` | Railway account token (fleet's historical name; Railway convention is `RAILWAY_API_TOKEN` — superbot tooling accepts the fleet name) | `<SET-IN-CLAUDE-AI>` |
| `RAILWAY_PROJECT_ID` | Railway project id the tooling targets | `<SET-IN-CLAUDE-AI>` |
| `RAILWAY_SERVICE_ID` | Railway service id the tooling targets | `<SET-IN-CLAUDE-AI>` |
| `RAILWAY_ENVIRONMENT_ID` | Railway environment id (optional fourth of the set) | `<SET-IN-CLAUDE-AI>` |

### ⚠️ DANGER — the Railway trio (`RAILWAY_API_KEY` / `RAILWAY_PROJECT_ID` / `RAILWAY_SERVICE_ID`)

The **ambient IDs point at production** — the live SuperBot Railway project/service
(worker + Postgres). Any environment that carries them hands its agents the
production control plane. **Exclude the trio (and `RAILWAY_ENVIRONMENT_ID`) from
every non-superbot environment** — a codetool-lab or games lane has no business
holding a handle to the production bot. The same production-pointing caution
applies to `DATABASE_URL` and `DISCORD_BOT_TOKEN_PRODUCTION`: superbot-lane only.

## Platform-injected (do NOT set manually)

Observed in the live environment but believed injected by the Claude Code
platform / GitHub integration, not by the owner — a new-env spec should **not**
list them as asks (unverified: confirm across environments before trusting):

| Name | Purpose |
|---|---|
| `GITHUB_TOKEN` | App-scoped GitHub token the harness provides |
| `ANTHROPIC_BASE_URL` | Model API routing for the harness itself |

## Rules for specs

- A spec lists **only the names its lane actually needs** — smallest set wins;
  every extra production-pointing var is unpriced blast radius.
- New fleet-standard names get a row here (append; note the date); lane-specific
  one-offs stay in the lane's own spec.
