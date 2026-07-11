# Env-grant policy — which secrets each project gets, and why

> **Status:** `living-ledger` — the **authorization layer** on top of
> [`archetypes.md`](archetypes.md). archetypes.md answers *"which env-var NAMES
> does each project's environment carry?"*; this doc answers *"which of those
> should actually be granted, at what scope, and how much room to give each
> lane."* Owner-directed 2026-07-11 (in-session): "give the projects some room
> to work with real things — but do it safely."
>
> **Hard rule (unchanged, `README.md` + [`RAILWAY-SAFETY.md`](../docs/../environments/README.md)):**
> values live ONLY in the claude.ai environment panel — never in any repo. This
> doc uses NAMES and placeholder formats only.

## The one principle: trust tiers, widest blast radius held tightest

A secret's danger is its **blast radius** — what a session holding it could break
or spend. Grant by tier; never spread a Tier-3 credential to reach a Tier-2 goal.

### Tier 3 — keys to the kingdom · ONLY `superbot`, `superbot-next`, `coordinator`

| Name | Blast radius if leaked/misused |
|---|---|
| `DISCORD_BOT_TOKEN_PRODUCTION` | Full control of the live Discord bot |
| bot `DATABASE_URL` | The production data |
| account `RAILWAY_API_KEY` | **Entire Railway account — including the live bot's project** |
| `RAILWAY_PROJECT_ID` / `SERVICE_ID` / `ENVIRONMENT_ID` (the `reliable-grace`/`worker` trio) | A direct handle on the production bot service |

**Never** place these in a lab / game / venture env. The ambient production
Railway trio is CI-denylisted outside bot-prod/coordinator
(`scripts/check_no_ambient_railway_ids.py`).

### Tier 2 — real capability, scoped · per lane that needs it

| Name | Scope it correctly | For |
|---|---|---|
| `RAILWAY_TOKEN` | **project-scoped** token (bound to ONE project+env), NOT the account key | websites, product-forge, superbot-mineverse — live deploy/read of *their own* project |
| `GITHUB_PAT` | **fine-grained, repo-scoped** (that lane's repo; read-only where it only reads) | higher GitHub rate limit / Actions on the lane's own repo |
| `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` | budget-capped keys | lanes that genuinely call models |
| `STRIPE_SECRET_KEY` (`sk_test_…`), `STRIPE_WEBHOOK_SECRET` (`whsec_…`) | **TEST mode only** | venture-lab revenue E2E |
| `DISCORD_OAUTH_CLIENT_ID`/`_SECRET`, `OAUTH_REDIRECT_URI`, `WEB_SESSION_SIGNING_KEY` | a *separate* OAuth app, not the bot | superbot-mineverse, websites sign-in |
| `MINING_WRITE_ENDPOINT`, `MINING_WRITE_SHARED_SECRET` | HMAC pair | superbot-mineverse write-back |
| `SITE_PASSWORD`, websites-app `DATABASE_URL` (its OWN db) | not the bot's db | websites gated pages / `/submit` |
| test `DISCORD_BOT_TOKEN` + test guild id | a sacrificial bot, never production | superbot-next live drives ("Galaxy Bot") |

### Tier 1 — baseline · most labs

`substrate-kit, sim-lab, idea-engine, superbot-games, product-forge, codetool ×3`
usually need **no secrets** (stdlib). Optional: a read-only cross-repo PAT, and
an AI key (budget-capped) if the lane calls models.

### Tier 0 — platform-injected, never set by hand

`GITHUB_TOKEN`, `ANTHROPIC_BASE_URL`, proxy plumbing (`HTTPS_PROXY`, CA bundle).

## Why project-scoped Railway tokens (the key recommendation)

The owner's goal — "let projects do real Railway work and see live values" — is
achieved SAFELY by minting a **project token** per infra lane rather than sharing
the account `RAILWAY_API_KEY`. A project token can deploy/read only the project
it's bound to; a lane holding one **cannot reach the production bot's project at
all.** Same live capability, blast radius contained to that lane. The account key
and the production trio stay with the owner + coordinator only.

## Useful vars worth adding (biggest unblock first)

1. **Stripe TEST keys** → venture-lab (unblocks the entire revenue path; zero real-money risk in test mode).
2. **Discord OAuth (separate app)** → superbot-mineverse + websites (sign-in).
3. **Project-scoped `RAILWAY_TOKEN`** → websites / product-forge / mineverse (live infra, contained).
4. **Fine-grained repo `GITHUB_PAT`** → per lane (fixes anonymous rate-limit; far safer than the full-access PAT).
5. **Sandbox `DATABASE_URL`** (a scratch Postgres, not the bot's) → lanes testing DB code.
6. **`YOUTUBE_API_KEY`, `PARAGON_*`, `BTD6_*`** → superbot / superbot-next media features.
7. Releases: prefer **OIDC trusted publishing** (no stored token); `PYPI_API_TOKEN` only as manual fallback.

## Where to manage each (the "direct link" reference)

The console surface for each credential — this is also the source for the
website's per-env management links (see websites
`docs/planning/live-env-visibility-plan-2026-07-11.md`).

| Credential | Where you manage it |
|---|---|
| `RAILWAY_API_KEY` (account) | https://railway.app/account/tokens |
| `RAILWAY_TOKEN` (project-scoped) | railway.app → project → Settings → Tokens |
| Railway service variables | railway.app → project → service → **Variables** |
| `DISCORD_BOT_TOKEN*`, OAuth client id/secret | https://discord.com/developers/applications |
| `STRIPE_SECRET_KEY` (test) | https://dashboard.stripe.com/test/apikeys |
| `STRIPE_WEBHOOK_SECRET` (test) | https://dashboard.stripe.com/test/webhooks |
| `GITHUB_PAT` (fine-grained) | https://github.com/settings/personal-access-tokens |
| `OPENAI_API_KEY` | https://platform.openai.com/api-keys |
| `ANTHROPIC_API_KEY` | https://console.anthropic.com/settings/keys |
| `YOUTUBE_API_KEY` | https://console.cloud.google.com/apis/credentials |
| Supabase URL / service key | Supabase project → Settings → API |
| PyPI trusted publishing | https://pypi.org/manage/account/publishing/ |

## Paste-ready per-lane templates (NAMES only — values in the panel)

```
# superbot-next (Tier 3 bot; use a TEST bot for live drives)
DISCORD_BOT_TOKEN=<sacrificial TEST bot>      # not the production token
DATABASE_URL=<test/scratch postgres>
ANTHROPIC_API_KEY=<budget-capped>   OPENAI_API_KEY=<budget-capped>
SB_APPCMD_SYNC_GUILD_ID=<test guild id>
YOUTUBE_API_KEY=<...>  PARAGON_API_KEY=<...>  PARAGON_API_BASE_URL=<...>
# NO production RAILWAY_* — the live deploy stays owner/coordinator

# venture-lab (Tier 2, revenue)
STRIPE_SECRET_KEY=sk_test_...       STRIPE_WEBHOOK_SECRET=whsec_...
# optional: SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY
# NO Discord/DB/Railway prod vars — hard rail

# superbot-mineverse (Tier 2, browser game)
DISCORD_OAUTH_CLIENT_ID=...   DISCORD_OAUTH_CLIENT_SECRET=...
OAUTH_REDIRECT_URI=...        WEB_SESSION_SIGNING_KEY=<random 32+ bytes>
MINING_WRITE_ENDPOINT=...     MINING_WRITE_SHARED_SECRET=...

# websites (Tier 2, infra)
RAILWAY_TOKEN=<project-scoped to superbot-websites ONLY>
GITHUB_PAT=<fine-grained: menno420 repos>
SITE_PASSWORD=...            DATABASE_URL=<websites-app db, NOT the bot's>
# DENYLISTED (CI-enforced): RAILWAY_PROJECT_ID / SERVICE_ID / ENVIRONMENT_ID

# a typical lab (Tier 1)  — usually nothing; optional:
ANTHROPIC_API_KEY=<budget-capped, only if it calls models>
```

## See also

- [`archetypes.md`](archetypes.md) — the per-project env-var NAME mapping (what each env carries).
- `websites docs/planning/live-env-visibility-plan-2026-07-11.md` — surfacing these live on the control-plane.
- `../docs/RAILWAY-SAFETY.md` (in the websites repo) — the ambient-production-ID rail.
