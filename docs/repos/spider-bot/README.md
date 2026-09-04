# spider-bot — the entry point

> **Status:** `living-ledger` · live state re-derived **2026-09-04** against the
> GitHub API and a fresh clone; the construction record at the bottom is still
> the 2026-08-24 registration session's.
>
> **What this is:** fleet-manager's entry point for `menno420/spider-bot` —
> where the last session left off and where the next one should look.
> **Canonical for nothing except purpose.** [`intent.md`](intent.md) beside this
> file is the canonical intent surface (owner-answered 2026-09-04). The repo's
> own `README.md` wins on its state, its `CLAUDE.md` wins on the working rules,
> its `docs/product-shape.md` wins on the product model, and the live tree and
> Railway service win over all of them.
>
> **What this file got wrong, and how** — kept because the correction is the
> useful part. Written 2026-08-24 when the repo was one day and five commits
> old, it froze that day's numbers into prose and was never re-derived. By
> 2026-09-04 it was wrong about the commit count (5 → **20**), the test count
> (78 → **246**), and, worst, it still listed *"a `/home` panel"* as a
> **candidate** for the next feature when the panel, the route registry, the
> closed-test clock and membership memory had all shipped on 2026-08-24/25. A
> dated header is not a honesty mechanism if nothing re-reads it.

## The one-paragraph answer

**Spider Bot** is the **AI operations bot of the Slingy Spider Discord server**
(guild `1541447750628147351`) — the owner said so live on 2026-09-04, and that
statement is newer than the plan this repo was created under. Its job is to
**manage the server and help during testing of the game**: be a reliable
automoderator, let people talk to it naturally for guidance, complaints, bugs,
feedback and ideas, and turn what they say into **durable reports the developer
can find and act on**. Read [`intent.md`](intent.md) before inferring anything
about direction — and read [`[D-0042]`](../../decisions.md) for the four rules
that statement generates, the sharpest being that *heavy AI integration* means
the AI supplies **judgement** while deterministic code supplies **authority**.

Python 3.12 + discord.py 2.7, one Railway worker (project `spider-bot`, service
`worker`, europe-west4), live since 2026-08-24. `MEASURED` 2026-09-04 from the
API: `main` = `bf4d75278a74` (2026-08-25T22:42:55Z), **20 commits**, **0 open
PRs**, **no rulesets and no branch protection**, CI workflow `quality` green on
the last 10 runs. A fresh clone measures **57 tracked files** — 27 runtime
modules (3,172 lines), 16 test files (2,999 lines, **246 collected tests**), 4
repo docs. `ruff check .`, `python -m pytest` and `python -m compileall
spiderbot` all exit **0** at that SHA.

What has actually shipped: the tester funnel (`/jointest`, `/feedback`, the
opted-in watcher), the human-only tester roster (`/tester add|remove|count`),
owner/mod utilities (`/announce`, `/status`), AI chat (mention anywhere public,
initiative only in `AI_INITIATIVE_CHANNELS`), the **app-like UI layer** —
`/home` + a pinnable `/panel`, one typed route registry, preview-then-confirm
presets, a locked visual system — the **closed-test clock** read out of the
guild audit log, **membership memory** (roles restored on rejoin, the tester
role deliberately never), and Railway IaC with build watch patterns.

`superbot` (live, frozen) is its behavior/UX oracle and `superbot-next`
(parked) its architecture donor — every reuse gets a row in the repo's
`docs/extraction-ledger.md` (12 rows at 2026-09-04). Neither source repo is
ever modified.

## The deploy trap — read before pushing anything

**Push to main deploys straight to production.** No PR gate and no ruleset;
CI (`quality`: ruff + 246 tests + compileall) is informational. Railway's deploy status
SUCCESS alone proves nothing about which code runs: verify the new
deployment's `meta.commitHash` equals HEAD (the repo README documents the
`serviceConnect` trap that makes this necessary). And never leave a local
instance running while the Railway worker is up — that is two live bots
answering in the real server.

One more Railway fact, and it is not a failure when you see it:
**`.railway/railway.ts`** sets build **watch patterns** (`spiderbot/**`,
`requirements.txt`, `.python-version`), so a docs- or tests-only commit
deliberately does **not** deploy and the live `commitHash` will lag HEAD.
Preserve them — without watch patterns a scheduled commit once restarted a
donor's production worker ~293 times in one billing cycle.

**CORRECTED 2026-09-04.** This paragraph said `railway.json`, and listed
`railway.json` itself among the patterns. The repo has held only
`.railway/railway.ts` since spider-bot#1/#2 landed the Railpack/IaC migration
on 2026-08-25 — three weeks before this entry repeated the older shape, as did
spider-bot's own `CLAUDE.md` and `docs/rollout.md` until the review pass on
spider-bot#3 read the docs against the tree. **It mattered rather than being
cosmetic:** the lag it predicts had already happened and nobody had looked —
the live worker ran `bc4f9985` while `main` was `bf4d7527`, because that commit
touched only `.railway/railway.ts`, which is not among the patterns. A
post-merge `meta.commitHash == HEAD` check would have compared against a hash
that was never live.

**Owner intent — ANSWERED 2026-09-04:** [`intent.md`](intent.md). The
2026-08-28 draft's four ❓ slots are closed there, and the rules the answer
generates are [`[D-0042]`](../../decisions.md).

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

### Thread: purpose — **answered 2026-09-04, live** (supersedes "next feature — owner's pick")

The thread this file carried since 2026-08-24 — *"the owner chooses what the bot
grows next; a session must not infer it"* — is **closed by him choosing.**
Spider Bot is the **AI operations bot of this one server**: a reliable
automoderator, a natural-language front door for guidance, complaints, bugs,
feedback and ideas, and a machine that turns those into durable
developer-findable reports (preferably GitHub issues on `spider-swing`).
Canonical: [`intent.md`](intent.md) · rules: [`[D-0042]`](../../decisions.md).

`OQ-GCB-REVIEW-SCOPE` — open since 2026-08-23, asking *what must the
review-oriented bot actually do* — is **answered by the same statement**: the
testing-and-feedback loop, plus moderation of the server that runs it. See
[`../../owner-queue.md`](../../owner-queue.md).

### Thread: AI operations build — **active**, opened 2026-09-04

The first tranche against the new purpose. Shape, in dependency order: shared
foundations (stable ids, a storage seam, a GitHub client, typed AI verdict
contracts, a policy layer, correlation) → the developer feedback loop (one
intake service behind every entry point, conversational filing, privacy
classification, store-first, idempotent GitHub projection) → the AI moderation
foundation (event logging, classifier, deterministic policy evaluator, **shadow
mode**, one case model, a staff review surface) → the game-knowledge seam (a
versioned support feed produced by `spider-swing`, consumed with a
last-known-good fallback) → run-evidence import.

**Nothing new enforces on arrival.** New moderation ships `off`/`shadow`; the
GitHub path is fail-closed until a credential exists. What turns each
enforcement class on is evidence, defined in the plan, not the fact that the
code compiles.

### Thread: plan transplant — **open, and now partly moot**

The GCB plan's own README says that on repo creation the plan is copied into the
repo, reconciled against the first commit, and the fleet-manager folder becomes
a dated pointer. That never happened. It matters less now: [`[D-0042]`](../../decisions.md)
narrows the plan's multi-game breadth out of spider-bot's scope, so what is left
to transplant is the architecture research, not the product definition. The
repo's own `docs/product-shape.md` and `docs/architecture.md` are the live
product surfaces.

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
| `CLAUDE.md` | the **21** invariants (defect lines, not style preferences) + verify commands + venue rules. It said twelve here until 2026-09-04; the file has carried twenty-one since 2026-08-25 |
| `docs/extraction-ledger.md` | every reuse from superbot / superbot-next, with the decision per row |
| `docs/product-shape.md` | `binding` — what the bot is for and how it should feel. Read it after `CLAUDE.md` |
| `docs/architecture.md` | `binding` — the layered design the AI-operations work is built on |
| `tests/` | the **246**-test harness — the executable form of the invariants |

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
