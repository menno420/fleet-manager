# 2026-08-05 · hub — what a playtest Discord needs, and which bot parts serve it

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: the owner owns a 61-extension Discord bot and needs a server
that does about nine things. The interesting question is not "what can the bot
do" but "what does this specific job need, and what of that is already live" —
and those two sets overlap far less than the bot's size suggests.

## Previous-session review

PR #171 recorded the trademark register search. The Play track needs 12 Android
testers opted in for 14 continuous days; a Discord server is the recruiting and
feedback vehicle for that, which is why this question arrived now.

## What landed

- `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md` — Discord's
  own playtest-server guidance (fetched), the verified deployment state of both
  bots, a three-tier map of which subsystems serve this job, and the gap that
  matters.
- `docs/findings/README.md` — index row, so the finding is not an orphan.

## Measured

**Deployment state, from live APIs rather than from either repo's own docs:**

- `superbot` is **running**. Railway project `reliable-grace`, service `worker`,
  deployment status `SUCCESS` at `2026-08-05T10:53:00Z`, beside `Postgres`,
  `dashboard`, `botsite`, `review`.
- `superbot-next` has **never** been deployed.
- **Both repositories report `archived=false, disabled=false`** from the GitHub
  API — which contradicts `superbot-next/docs/PROJECT-CLOSEOUT.md`, whose own
  words are that the repo *"becomes permanently read-only on 2026-07-22"*. The
  freeze was a program wind-down, not a repository lock.

**The gap worth the owner's attention:** cog routing in `superbot` has storage,
a scope chain, a canonical mutation path with audit, four named batch profiles,
a wizard section and an Access Map projection — and **nothing consults it at
command admission**. `core.runtime.command_access.resolve_command_access` never
imports `command_routing`; every caller of `is_cog_enabled` is a preview, a
projection or a UI. A cog can be marked disabled, every surface will agree it is
disabled, and the command still runs. `superbot-next` reaches the same state and
records it in its own completeness table: *"NO live routing resolver exists in
this build."*

Two independently-built codebases with the same hole is worth noticing on its
own — it suggests the surface was specified as configuration and never as
enforcement, in both attempts.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Both bot repositories cloned and read; Railway and GitHub queried live over
  direct egress. No claim in the finding rests on either repo's status docs —
  the one place they were trusted, the closeout's read-only claim, turned out to
  be wrong and is corrected in the finding.

**NULL — unverified:** `superbot`'s current guild count (needs the running
bot's gateway state); whether Community must be enabled before Forum channels
appear; and Discord's support-centre articles generally — Community Onboarding
FAQ, Forum Channels FAQ and Enabling Your Community Server are **Cloudflare-403
to automated fetching** on both the proxied and direct routes, so nothing in the
finding is sourced from them.

## 💡 Session idea

**The size of the tool said nothing about its fit for the job.** The owner has a
61-extension bot; this server needs about nine of them, and the single most
useful thing in the whole analysis — put bug reports in Discord's native Forum
channels rather than the bot's ticket system — is a recommendation to use *less*
bot. The ticket subsystem is live, substantial and the obvious candidate, and it
is the wrong shape: a ticket is private and dies on close, so twelve testers
hitting one crash produce twelve dead threads instead of one living forum post.

The other half is a pattern worth naming: **a configuration surface complete in
every respect except enforcement.** Routing has storage, mutation, audit,
profiles, UI and a projection that reports the setting back accurately. Every
one of those is evidence that it works. The only missing piece is the one that
makes it true, and it is invisible from every surface that displays it — the
Access Map will cheerfully report a cog disabled while the cog runs. Built twice,
same gap both times.
