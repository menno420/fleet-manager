# spider-bot — the entry point

> **Status:** `living-ledger` · true as of **2026-08-24** (built by the
> registration session, the same day the repo went live)
>
> **What this is:** fleet-manager's entry point for `menno420/spider-bot` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The repo's own `README.md` wins on its state, its
> `CLAUDE.md` wins on the working rules, and the live tree and Railway service
> win over both. This file summarises and points; when it disagrees with the
> repo, the repo is right and this file is stale.
>
> **README-only build, on purpose** (the on-demand shape): the depth files
> (`capabilities.md` / `records.md` / `working-here.md`) are not yet written —
> the repo is one day and five commits old, so there is nothing scattered to
> consolidate yet. Add them when the record actually spreads.

## The one-paragraph answer

**Spider Bot** is the AI community bot of the **Slingy Spider** Discord server
(guild `1541447750628147351`) — the GCB plan's clean game-community repo,
created 2026-08-24 under owner direction. Python 3.12 + discord.py 2.7, one
Railway worker (project `spider-bot`, service `worker`, europe-west4), deployed
live the same day. v0.1 ships the tester funnel (`/jointest`, `/feedback`,
opted-in watcher), the human-only tester roster (`/tester add|remove|count` —
the role mirrors the real Play closed-test cohort, granted only after the
owner verifies the opt-in), owner/mod utilities (`/announce`, `/status`), and
AI chat: replies on @mention anywhere public, initiative ONLY in
`AI_INITIATIVE_CHANNELS` (currently `general`), every AI decision audited
(stdout JSON + #mod-log embeds). `MEASURED` 2026-08-24: latest deployment
SUCCESS building `e0d8909` = HEAD; deploy log reads
`ready as Spider Bot#7153 in Slingy Spider; AI=True`.

`superbot` (live, frozen) is its behavior/UX oracle and `superbot-next`
(parked) its architecture donor — every reuse gets a row in the repo's
`docs/extraction-ledger.md` (6 rows at registration). Neither source repo is
ever modified. GCB-1 is resolved by this repo's existence; the owner chose
the name `spider-bot` over the plan's `superbot-community` default.

## The deploy trap — read before pushing anything

**Push to main deploys straight to production.** No PR gate; CI (`quality`:
ruff + 78 tests + compileall) is informational. Railway's deploy status
SUCCESS alone proves nothing about which code runs: verify the new
deployment's `meta.commitHash` equals HEAD (the repo README documents the
`serviceConnect` trap that makes this necessary). And never leave a local
instance running while the Railway worker is up — that is two live bots
answering in the real server.

**Owner intent (DRAFT, awaiting his words):** [`intent.md`](intent.md) — from
the 2026-08-28 elicitation sitting; it proposes no feature direction, per this
file's own rule.

## Threads

### Thread: Phase-0 hardening — **closed 2026-08-24** (the registration session)

Shipped at menno420/spider-bot@e0d8909: a pytest harness (78 tests — safety
wrapping + marker-forgery disarm, gateway degrade paths, the chat decision
pipeline, config redaction, audit sinks, the opted-in watcher, intents), ruff
(tools-only `pyproject.toml` — NIXPACKS checks `requirements.txt` first,
verified in its source, so the Railway build path cannot change), and CI
workflow `quality` on every push (informational). Deploy re-verified live
after landing. Still deferred until the bot needs durable state:
Postgres/migrations, Docker, config schema.

### Thread: next feature — **active, owner's pick**, updated 2026-08-24

The owner chooses what the bot grows next; a session must not infer it.
Candidates on the table (from the GCB plan + the build sessions): a `/home`
panel · richer tester-funnel tracking · more knowledge depth · making CI a
required check (that one changes the landing workflow to a PR flow, so it is
owner-gated twice over). The larger arc — what the review/testing loop
covers — is `OQ-GCB-REVIEW-SCOPE` in [`../../owner-queue.md`](../../owner-queue.md),
still open.

### Thread: plan transplant — **open, unstarted**

The GCB plan's own README says that on repo creation the plan is copied into
the repo, reconciled against the first commit, and the fleet-manager folder
becomes a dated pointer. None of that has happened: spider-bot points AT
[`../../planning/2026-08-21-game-community-bot/`](../../planning/2026-08-21-game-community-bot/README.md)
instead. Workable for now — but whoever re-sequences the roadmap after the
review-scope letters land should do the transplant in the same pass.

## Before you attach it

The repo is **public** — read-only questions need a raw fetch, not a clone:
`https://raw.githubusercontent.com/menno420/spider-bot/main/<path>`.
For writes, the repo's own venue rule (`CLAUDE.md` § Venue rules): clone
fresh, work, push, **delete the clone** — a stale resident clone reading as
authoritative is the failure the owner's laptop hub already measured.
Secrets: names in the repo, values only in Railway / the Developer Portal /
the owner's laptop env (`DISCORD_BOT_TOKEN_SPIDERBOT`); never print a value
anywhere.

## Once attached — the per-repo boot path

| file (in spider-bot) | what it is |
|---|---|
| `README.md` | identity, stack ruling, secret NAMES, deployment + the deploy trap. **Start here** |
| `CLAUDE.md` | the 12 invariants (defect lines, not style preferences) + verify commands + venue rules |
| `docs/extraction-ledger.md` | every reuse from superbot / superbot-next, with the decision per row |
| `tests/` | the 78-test harness — the executable form of the invariants |

## External workspaces (§ 5.7)

Drive / ChatGPT / Gemini: null — none mapped. The bot's operational venues
are the Railway project (`spider-bot`) and the Discord Developer Portal (app
`1541449715932205187`), both owner-held; the owner's laptop hub
(`Hub/journal.md` on his OneDrive) carries the build-session narrative.

## How much of the repo this was built from — `MEASURED` 2026-08-24

Unusually for this directory: **the whole runtime tree, read this session** —
all twelve `spiderbot/*.py` files, `README.md`, `CLAUDE.md`, the extraction
ledger and requirements, plus live GitHub state (commits, branches, CI runs)
and live Railway state (deployments, `meta.commitHash`, deploy logs). The
repo is five commits old and small, so this entry starts from full knowledge
— and will drift from here; the dated header is the honesty mechanism.
