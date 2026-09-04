# 2026-09-04 — the SuperBot successor: closing verdict gap 1 by booting `superbot-next` and driving its help tree and setup flow

> **Status:** `in-progress` — branch `claude/superbot-evidence-gap-kyum0x`.
> Born red on purpose. **What is about to happen:** the rebuild package's
> verdict (`docs/planning/2026-09-04-superbot-rebuild/13-verdict.md` gap 1)
> says every dynamic claim in it is read from source because neither bot was
> booted. This session boots `superbot-next` at the pin `d5f66dc2` against a
> throwaway local Postgres, drives the help tree and the setup flow through
> the real dispatch spine and the production panel presenter, and writes the
> observation into the package's `run/` folder — with each layer labelled
> real or synthetic. Slice one is not started: `OQ-SUPERBOT-SUCCESSOR-SCOPE`
> (A) is still open in `docs/owner-queue.md` at this session's start.

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
against current truth and nothing needs re-running before building on it.
One thing that card recorded and this session did not inherit: it read
Codex commenting unprompted on fm #1025 as a possible automatic trigger; the
boot file's record stands (comment is the only reliable trigger) and this
session asks explicitly.

**What this session is about:** one evidence gap, no design work. The plan
package is authoritative and this session changes none of its conclusions
by hand — it adds an observation record and pointers to it. **No repository
is created, no code is written for the successor, and `superbot`, its Railway
worker, its Postgres and every Discord surface stay untouched** (the rail in
`13-verdict.md` § "Must not, under any reading").

## What was done

*(in progress — written as the work lands)*

- **Cold orientation** — the six mandatory reads in `README.md` order, then
  the package's `00-README.md`, `13-verdict.md`, `09-roadmap.md` § 2,
  `08-verification.md` §§ 1, 3c, the two Layer-2 entry points and their
  owner-comment indexes (both empty), the 2026-08-05 live audit's § 7–9, and
  `superbot-next`'s own boot file, orientation router and live-testing
  ledger (`docs/status/testing-report-2026-07-09.md`).
- **Pins re-read** — `superbot` `5e3a667b` · `superbot-next` `d5f66dc2`, both
  unmoved (`git ls-remote refs/heads/main`, direct-PAT path).
- **Environment** — `superbot-next` cloned read-only to `/home/user/superbot-next`
  at the pin; `python3.11` venv with the hash-pinned `requirements.lock`
  (`pip install --require-hashes`, exit 0; discord.py 2.7.1, asyncpg 0.30.0).

## 💡 Session idea

**Apply the population contract to the credential.** The composition root
should refuse to connect the gateway unless `GET /users/@me` on the token it
was handed returns the *committed* expected identity for the declared data
plane — test plane → the test app's id, prod plane → the live worker's id —
derived from a committed file, never from the env var's *name*. The estate
already paid for this twice: on 2026-08-05 a session inferred "production
identity" from the name `DISCORD_BOT_TOKEN_PRODUCTION` and was wrong for an
hour (audit § 7), and today the same name is what stands between a session
and the boot — because nothing but a network call can say what the value is.
A name is prose; an expected id is data. Same shape as `08-verification.md`
§ 1, one level down.

## Verify

```
cd /home/user/fleet-manager && python3 bootstrap.py check --strict --added-card .sessions/2026-09-04-superbot-successor-evidence-gap.md
```
