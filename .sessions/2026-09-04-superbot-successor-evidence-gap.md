# 2026-09-04 — the SuperBot successor: closing verdict gap 1 by booting `superbot-next` and driving its help tree and setup flow

> **Status:** `in-progress` — branch `claude/superbot-evidence-gap-kyum0x`,
> PR fm #1040. Born red on purpose. **What is about to happen:** the rebuild
> package's verdict (`docs/planning/2026-09-04-superbot-rebuild/13-verdict.md`
> gap 1) says every dynamic claim in it is read from source because neither
> bot was booted. This session boots `superbot-next` at the pin `d5f66dc2`
> against a throwaway local Postgres, drives the help tree and the setup flow
> through the real dispatch spine and the production panel presenter, and
> writes the observation into the package's `run/` folder — with each layer
> labelled real or synthetic. Slice one is not started:
> `OQ-SUPERBOT-SUCCESSOR-SCOPE` (A) was still open in `docs/owner-queue.md`
> at this session's start. The flip is the last act.

- **📊 Model:** withheld · max · review/verify
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01CAy4hy5v4AcB9WfXJTMAd2](https://claude.ai/code/session_01CAy4hy5v4AcB9WfXJTMAd2) · "SuperBot successor: evidence gap closure"

**Previous-session review:** the last fleet-manager session on this line
(fm #1025, `.sessions/2026-09-04-superbot-rebuild-comparative-review.md`)
produced the 13-deliverable plan package plus `run/`, answered one Codex round
(13 findings, all addressed), and merged at `e9a9dcb`. Its verdict named four
gaps and said which a session may close alone: gap 1 (no boot). Its
refutation pass landed afterwards in the same package (`run/refutation-pass.md`,
62 of 196 lane strengths refuted). Checked on the way in: both product pins
are **still** the live head of `main` (`superbot` `5e3a667b`, `superbot-next`
`d5f66dc2`, `git ls-remote` 2026-09-04), so the package's measurements are
against current truth and nothing needed re-running before building on it.
One thing that card recorded and this session did not inherit: it read Codex
commenting unprompted on fm #1025 as a possible automatic trigger; the boot
file's record stands (the comment is the only reliable trigger) and this
session asks explicitly.

**What this session is about:** one evidence gap, no design work. The plan
package is authoritative and this session changes none of its conclusions
by hand — it adds an observation record and pointers to it. **No repository
is created, no code is written for the successor, and `superbot`, its Railway
worker, its Postgres and every Discord surface stay untouched** (the rail in
`13-verdict.md` § "Must not, under any reading").

## What was done

- **Cold orientation** — the six mandatory reads in `README.md` order, then
  the package's `00-README.md`, `13-verdict.md`, `09-roadmap.md` § 2,
  `08-verification.md` §§ 1, 3c, the two Layer-2 entry points and their
  owner-comment indexes (both empty), the 2026-08-05 live audit's §§ 4b, 7–9,
  and `superbot-next`'s own boot file, orientation router, live-testing
  ledger (`docs/status/testing-report-2026-07-09.md`) and live-drive runbook.
- **Pins re-read** — `superbot` `5e3a667b` · `superbot-next` `d5f66dc2`, both
  unmoved (`git ls-remote refs/heads/main`, direct-PAT path).
- **Environment** — `superbot-next` cloned read-only to `/home/user/superbot-next`
  at the pin; `python3.11` venv with the hash-pinned `requirements.lock`
  (`pip install --require-hashes`, exit 0; discord.py 2.7.1, asyncpg 0.30.0);
  a throwaway PostgreSQL 16 cluster on `127.0.0.1:54329` run under the
  container's `postgres` account through a 60-line `os.setuid` wrapper
  (the server refuses root; `docker` was not reached for). The repo's own
  `SB_VERIFY_BOOT` profile then answered `{"verified": true}`, exit 0, on the
  fresh database — the offline half of the audit's recipe.
- **The token leg did not run.** The estate's records say the container's
  `DISCORD_BOT_TOKEN_PRODUCTION` is the TEST app (audit § 7; the ledger's
  *"connects as Galaxy Bot#6724 (id=1298426054636994611)"*), and an identity
  check was the designed first step before any connect. Five commands that
  referenced that variable — a `curl` `GET /users/@me`, a Python script
  doing the same, an offline base64 decode of the token's id segment, two
  more forms — were refused by this venue's auto-mode classifier on the day
  (momentary, per call), so no gateway was connected and no token was read.
  Not treated as a wall: the transport was replaced instead (next bullet),
  and the leg is an owner ask (`OQ-SUPERBOT-NEXT-GATEWAY-LEG`).
- **The headless drive** — `run/headless_drive.py`: the composition root
  `run_app()` runs end to end with `connect_gateway` stubbed and Discord's
  HTTP answered by an in-process fake; one synthetic guild in the client
  cache; INTERACTION_CREATE payloads built from the recorded messages drive
  `/help`, the setup flow, the join launcher and all 27 slash commands through
  discord.py's `Interaction` → the tree / component feed → `resolve()` → the
  panel engine → the **production** `DiscordPanelPresenter`. Population
  declared (the committed snapshot's 314 panel ids) and reported both ways.
  Five clean runs on a fresh database plus one restart run; the walker was
  corrected twice on the way (a command-access lock-out it caused itself,
  then a Cog Manager select it re-clicked 6,518 times because session views
  mint a fresh id per render) — both corrections are in the record as
  interventions, not hidden.
- **The observation** — `run/boot-observation.md`, 12 sections: what is real
  and what is synthetic; the boot (57 migrations, 1,327 targets, 314 panels,
  27 commands, `RUNNING` in ~1.3 s, `/ready` 503 `gateway_not_ready`, clean
  `STOPPED`); first contact; the help tree walked to exhaustion (57 of 66
  reached, depth 5, 48 with only a Back button, **0 exits**); the setup flow
  (the join launcher posts; **`/setup` renders its card and never sends it**
  — the production presenter has no branch for a request with no interaction
  origin, the parity twin does, the reply links to message id `0`; the
  advanced wizard behind `/setup-hub` works — 21 of 40 panels, session row,
  depth, skips, 76 audit rows; three of ten setup commands unusable from slash
  because commands register parameterless); **two unhandled
  `AttributeError`s** (`ticket/setup_panel.py:159,191` — `WorkflowResult.ok`;
  `platform/guild_snapshot.py:243` — `ResourceRequirement.name`); the
  **one-click owner lock-out** on the Command Access panel (the override is
  the platform owner's); the global walk (1,821 interactions, 237 of 314
  rendered, 234 sent, 77 never); the population contract applied; a nine-row
  table of package claims confirmed, sharpened or contradicted; the gateway
  leg's recipe; the honest nulls.
- **Pointers into the package** — `13-verdict.md` gap 1 (CLOSED IN PART
  block, what changed, what stays open), `00-README.md`, `run/README.md`;
  the retained raw record `run/raw/headless-drive-2026-09-04.json`.
- **Estate records** — `docs/repos/superbot-next/README.md` (a new thread
  block with the four findings a session working that repo needs),
  `docs/current-state.md` (one sentence on the 2026-09-04 entry),
  `docs/owner-queue.md` (`OQ-SUPERBOT-NEXT-GATEWAY-LEG`),
  `docs/CAPABILITIES.md` (the headless-drive capability and the Postgres
  recipe, with the classifier fact as a route note, never a wall).

## 💡 Session idea

**Apply the population contract to the credential.** The composition root
should refuse to connect the gateway unless `GET /users/@me` on the token it
was handed returns the *committed* expected identity for the declared data
plane — test plane → the test app's id, prod plane → the live worker's id —
derived from a committed file, never from the env var's *name*. The estate
already paid for this twice: on 2026-08-05 a session inferred "production
identity" from the name `DISCORD_BOT_TOKEN_PRODUCTION` and was wrong for an
hour (audit § 7), and today the same name is what stood between a session
and the gateway — because nothing but a network call can say what the value
is. A name is prose; an expected id is data. Same shape as
`08-verification.md` § 1, one level down.

## Landed mid-session, and worth carrying

- **A bot cannot click its own buttons, and it does not have to.** The whole
  interaction pipeline below the socket is drivable in-process with real
  discord.py objects: replace `connect_gateway`, set `async_context` to a
  recording webhook adapter, shadow `HTTPClient.request` with a route table,
  inject a `Guild` into `bot._connection`, and build INTERACTION_CREATE dicts
  from what the presenter last sent. Every click then carries the exact
  `custom_id` the production adapter minted. This is the successor's
  reachability gate in prototype — walked over the **rendered** view — and it
  ran 1,821 interactions in under ten minutes on one CPU.
- **Blocking I/O inside the event loop looks like a dead health server.** The
  first `/ready` probe used `urllib` in the same thread as the bot and timed
  out at 5 s; `asyncio.to_thread` answered in milliseconds with the real 503.
- **A walk over a UI that can change its own admission policy must guard for
  it.** One click on *Selected channels* denied every later click in the
  channel, including the button that would have undone it — for the guild
  owner. The guard resets the policy in the database **and** drops the
  reader's 60 s cache (`forget_guild`), or the reset is invisible.
- **`asyncio.wait_for` returns the result of a task that swallowed its
  cancellation.** The first shutdown "succeeded" at exactly 60 s because the
  stub gateway task never ended and the root's `finally` catches
  `CancelledError`; the stub now ends when `bot.close()` runs, so the exit
  code is the root's own.

## Verify

```
cd /home/user/fleet-manager && python3 bootstrap.py check --strict --added-card .sessions/2026-09-04-superbot-successor-evidence-gap.md
python3 docs/planning/2026-09-04-superbot-rebuild/run/reachability_probe.py /home/user/superbot-next/manifest.snapshot.json   # the static baseline, reproduced at the pin
# the drive itself needs the superbot-next checkout, its venv and a local Postgres — recipe in run/boot-observation.md § 12
```

*(close-out — Shipped, the gate's real exit code, the review round, the
Layer-2 handoff line — is written when the work lands; see below once it is)*
