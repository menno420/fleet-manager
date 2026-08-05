# A playtest Discord for Slingy Spider — what it needs, and which bot parts serve it

> **Status:** `reference`
>
> Written 2026-08-05 in answer to a direct owner question: what does a good
> Discord game server need — especially one meant for testing — and which parts
> of `superbot` / `superbot-next` are worth getting working properly to build and
> maintain it.
>
> Every requirement below is either quoted from a Discord page fetched in
> session or measured against the cloned repositories and the live Railway API.
> Anything unverified is marked **NULL — unverified**.

## 0. The job this server actually has

The server is not a general community. It exists to serve one metric with a
deadline: **12 Android testers opted in to a Play closed test for 14 continuous
days**, which is what unlocks production access
(`docs/findings/2026-08-05-google-play-submission-requirements.md`).

That sharpens the design, and it corrects an intuition worth stating plainly:

**The 14-day clock does not require anyone to play.** Google's rule is that
testers stay *opted in*, not that they stay active. So the server's retention
job is not "keep them engaged" — it is **"give them no reason to press
leave"**, which is a much cheaper thing to buy. Engagement matters for
*feedback quality*, which is the real prize, but the two goals are separate and
should not be confused into one over-built server.

Three jobs, in priority order:

1. **Recruit** — turn a person who saw a clip into a person who has opted in.
2. **Retain passively** — keep them from opting out for 14 days.
3. **Collect feedback that is actually actionable.**

## 1. What Discord itself says a playtest server needs

Two official sources were fetched in session:
[Discord's game-development docs](https://docs.discord.com/developers/game-development/how-to-create-a-community-for-your-game)
and the
[Game Developer Playbook, Part One](https://discord.com/blog/the-game-developer-playbook-part-one-getting-started-on-discord).
The support-centre articles (Community Onboarding FAQ, Forum Channels FAQ,
Enabling Your Community Server) are **Cloudflare-walled to automated fetching**
— 403 on both the proxied and the direct route — so nothing below is sourced
from them.

### Channel structure — their names, verbatim

| Channel | Their stated purpose |
|---|---|
| `#rules-and-info` | *"A read-only channel with your server's rules and guidelines"* |
| `#announcements` | *"The source for game updates, events, and news"* |
| `#patch-notes` | build-by-build changes |
| `#game-discussion` | *"Where players talk about your game"* |
| `#build-feedback` | *"A spot for members to share feedback, observations, and critiques"* |
| `#bug-reports` / `#report-issue` | *"Also a Forum channel"* |
| `#admin-chat` | *"Private channel for your team to coordinate"* |
| `#admin-log` | *"Logs from your moderators, AutoMod, and bots"* |
| Playtest Room (voice) | screenshare observation during tests |

Their explicit warning: *"more channels does not always mean better"* — keep it
minimal to avoid *"information overload"* for new members.

### The two Forum channels are the load-bearing recommendation

For `#feedback` they say: *"Use Discord's Forum channel type here, not a regular
text channel."* And for both feedback channels: *"Forum Channels give each topic
its own dedicated Thread to hold conversations with the development team…
Discussions are tied to individual posts so they are more organized."*

On bug intake specifically: *"Set up post guidelines to tell players to include
steps to reproduce the issue, platform, and game version. This makes your bug
intake dramatically more actionable than a stream of 'Game crashed' or
'Broken'."*

**This is a native Discord feature, and it is the correct tool.** It costs
nothing, needs no bot, and requires only that Community be enabled on the
server. See § 4 for why this matters more than it looks.

### Roles

- **`@admin`** (renamed to the studio name) — access to every channel.
- **`@playtest`** — everything except admin channels.
- *"Revoke all `@everyone` permissions"* so uninvited users see *"an empty
  server until they have a role."*

### Running the tests

Discord names three mechanics: **Scheduled Events** to reach testers across time
zones, **screenshare** — *"a handy tool to observe user interaction and intent
in real-time"* — and a **reporting template** covering *"a username, what type
of bug it is, and how to reproduce it."*

### Retention and presence

The strongest line in either document, and the cheapest thing on this page:

> *"Even brief, genuine responses matter enormously. One developer reply per day
> shows the devs care more than a monthly wall of text."*

Beyond that they recommend off-topic channels (*"so they don't have to move away
from your server — this helps support member retention"*) and events: *"AMAs,
Trivia, Dev Q&As, and fan art contests."*

### Safety

Enable **verification levels** so *"the newest members will have to reach
certain platform requirements before participating, such as having a verified
email or phone number."* On NDAs they defer to legal counsel; for a free Play
closed test with no confidential content, that is out of scope here.

## 2. The bots — verified deployment state, not documented state

Both repositories were cloned and checked against live APIs.

| | `superbot` | `superbot-next` |
|---|---|---|
| Role | the live production bot | ground-up rebuild |
| Python | 3.10, discord.py, Postgres | 3.11, layered plugin architecture |
| Extensions | **61 loaded** (`disbot/config.py:111`) | 49 subsystems + kernel |
| Surface | 84 cog files | 413 commands / ~200 panels |
| Last push | **2026-08-05** | 2026-07-21 |
| **Deployed?** | **YES — running now** | **never** |

**superbot is live.** Railway project `reliable-grace` was queried directly: the
`worker` service reports deployment status `SUCCESS` at
`2026-08-05T10:53:00Z`, alongside `Postgres`, `dashboard`, `botsite` and
`review`. `Procfile` is `worker: python disbot/bot1.py`. This bot is running
right now.

**superbot-next has never been deployed.** Its own closeout records live-testing
as parked owner-side on a test-bot token. It is feature-complete on paper
(533 golden parity cases) and has never met a real server beyond port bands 1–4.

### A correction to the record

`superbot-next/docs/PROJECT-CLOSEOUT.md` states the repository *"becomes
permanently read-only on 2026-07-22 at 00:00 UTC."* **The GitHub API reports
`archived=false, disabled=false` for both repositories** (checked 2026-08-05).
The freeze was a *program* wind-down, not a repository lock. The repo is
writable. This does not make superbot-next the right tool today — an undeployed
rebuild is still undeployed — but "we can't touch it" is not true, and a future
session should not inherit that belief from the closeout doc.

## 3. Which subsystems actually serve this job

Both bots carry roughly the same surface. Mapped against § 1, most of it is
irrelevant here — which is the honest headline, not a criticism of the bot.
It was built for a games community; this is a QA server.

### Tier 1 — directly serves the three jobs

| Subsystem | State in `superbot` | Why it matters here |
|---|---|---|
| **setup / quicksetup** | live — `!setup`, slash front door, admin-gated, *"the short, jargon-free guided spine"* | Builds the server. Highest leverage single command. |
| **welcome** | live — greeting, farewell, **entry role** on join (`welcome_cog.py`) | The conversion moment: a joiner becomes a tester here or never. |
| **role** (reaction roles) | live — `!reactroles`, `!removereactrole`, `!listreactroles` | Self-serve `@playtest`. Pairs exactly with the self-serve Google Group opt-in. |
| **utility → `!remind`** | live (`utility_cog.py:276`) | The sleeper hit. A day-12 nudge is the cheapest possible defence against an opt-out on day 13. |
| **utility → `!poll`** | live (`utility_cog.py:297`) | Structured feedback beats free text for "which of these felt worst". |
| **starboard** | live | Surfaces the best feedback automatically instead of it scrolling away. |
| **logging** | live | `#admin-log`, exactly as Discord's structure asks. |
| **automod / security / image_moderation** | live (raid window, age gate) | Required the moment the invite is public. |
| **counters** | live | A live opted-in count against the target of 12 is a genuinely motivating server stat. |

### Tier 2 — useful, not on the critical path

`xp` + `xp_role_sync` (roles granted at XP thresholds — light retention),
`karma`, `leaderboard`, `community` / `community_spotlight`, `counting`,
`help`, `channel` ops, `server_management`, `cleanup`.

### Tier 3 — noise for this server

`casino`, `blackjack`, `mining`, `fishing`, `farm`, `creature`,
`creature_battle`, `btd6` (×5 cogs), `paragon`, `projmoon`, `four_twenty`,
`rps_tournament`, `deathmatch`, `economy`, `treasury`, `inventory`, `chain`,
`games`, `proof_channel`.

Roughly **25 of 61 loaded extensions** are content this server does not want.
They are not harmful, but they inflate `!help`, invite off-topic use of a
focused QA server, and make the bot look like it belongs to a different product.

### Tickets: the tool that looks right and is not

`ticket` is live and substantial (12 commands, panel launcher, claim/add/remove,
blacklist, per-guild config). It is the obvious candidate for bug intake.

**Discord's own guidance points the other way.** Bug reports and feedback belong
in **Forum channels**, because a forum post is public, taggable, searchable, and
lets other testers say "same here" — while a ticket is a private one-to-one
thread that dies when it closes. For twelve testers reporting the same crash, a
forum turns twelve reports into one thread; tickets turn it into twelve.

Keep tickets for *private* matters — a tester who wants to raise something
one-to-one. Do not make them the bug pipeline.

## 4. The gap worth knowing about: cog routing is built but not enforced

This is the most consequential finding for the owner's question, and it is
measured, not inferred.

`superbot` has a complete per-scope cog-routing surface:

- storage and a scope chain — `channel → category → guild → default-true`
  (`services/command_routing.py:57`);
- a canonical mutation path with audit emission (`set_policy`, `:88`);
- named batch profiles — *"Games → game channels only"*, *"Economy → …"*,
  *"Moderation → staff channels only"*, *"Recommended (all cogs by channel
  name)"* (`services/cog_routing_profiles.py:182`), each of which disables a cog
  at **guild scope** and re-enables it per detected channel;
- a setup-wizard section and an Access Map projection that display the result.

**Nothing consults it when a command runs.** The admission chain is
`bootstrap_access_cog` → `core.runtime.command_access.resolve_command_access`,
and that resolver imports the *command-access* policy only — it never imports
`command_routing`. Every caller of `is_cog_enabled` is a read: the setup draft
preview (`setup_operations.py:618`), the Access Map projection
(`access_projection.py:368`), and the wizard UI.

So a cog can be marked disabled, the Access Map and help menu will agree it is
disabled, **and the command still runs.**

`superbot-next` reaches the same state and says so in its own words —
*"NO live routing resolver exists in this build — the access_projection axis-3
ledger"* (completeness table, setup row). Two independent codebases, same gap.

**Why this is the highest-value fix.** Everything around it exists: storage,
mutation, audit, profiles, UI, projection. The missing piece is one consultation
inside one resolver. It is the difference between a QA server that shows only
its nine relevant subsystems and one that carries a casino.

### What works today instead

`command_access` **is** enforced, and its modes are `all_channels`,
`selected_channels`, `disabled_except_bootstrap`
(`utils/db/command_access.py:29`). Setting a new server to
**`selected_channels`** confines every bot command to a named channel list — so
a single `#bot-commands` channel absorbs the entire game surface and
`#bug-reports` stays clean. That is a configuration change, available now, no
code.

It is a blunter instrument than routing: it gates *where commands work at all*,
not *which* ones. But for a nine-subsystem QA server it is close enough to be
the right answer until routing is wired.

## 5. Other measured gaps

- **No invite tracking.** `grep` across `disbot/` finds no invite-attribution
  code. For a recruiting server this is the missing number — which invite link
  produced which testers is exactly what tells the owner where to spend effort.
  Genuinely valuable, and a self-contained addition.
- **Scheduled Events are logged, not managed.** `scheduled_event` appears only
  in `services/server_logging.py`. Discord's playtest guidance leans on
  Scheduled Events; the bot can watch them but not create them. Native Discord
  UI covers this, so it is a note rather than a gap.
- **Multi-guild is real.** `guild_lifecycle.teardown` purges per-guild state on
  leave, and `setup_cog` listens on `on_guild_join` to post a setup launcher.
  Inviting the live bot to a brand-new server is a supported path, not a
  migration.

**NULL — unverified:** how many guilds `superbot` currently serves (requires the
running bot's gateway state, not the repository); whether Community must be
enabled before Forum channels appear (strongly implied by Discord's *"if
Community is enabled, use Forum Channels"* phrasing, but the Forum Channels FAQ
could not be fetched); and whether any of the Tier-1 subsystems misbehave in a
guild that has never run the full setup wizard.

## 6. The recommendation

> **SUPERSEDED the same day (2026-08-05) — the owner overrode this section.**
> His reason: superbot carries architectural debt and is not fit to improve
> further, so "use the live bot instead" is not the path. The rebuild target is
> a **server bot first, with no game features**. Steps 1–3 below remain sound as
> *server* advice (they need no bot at all, or only configuration); it is the
> headline verdict that no longer stands. Do not re-propose it. The measured
> follow-ups are
> [`2026-08-05-superbot-next-live-audit.md`](2026-08-05-superbot-next-live-audit.md)
> and [`2026-08-05-three-repo-state-audit.md`](2026-08-05-three-repo-state-audit.md).

**Use the live `superbot`. Do not deploy `superbot-next` for this.** One is
running and multi-guild; the other has never met a real server, and a tester
recruitment drive is the wrong place to find out what breaks.

Order of work, cheapest-first:

1. **Create the server and let Discord do the structural work** — the nine
   channels above, two Forum channels, `@admin` / `@playtest`, `@everyone`
   revoked, verification level on, post guidelines on `#bug-reports`. No bot
   required for any of this.
2. **Invite the live bot, run `!setup`**, then set command access to
   `selected_channels` pointed at one `#bot-commands` channel.
3. **Wire the four that carry the three jobs** — welcome + entry role, reaction
   roles for `@playtest`, `!remind` for the day-12 nudge, `!poll` for structured
   feedback.
4. **Then, if it is worth building:** the routing resolver (§ 4) and invite
   tracking (§ 5). Both are contained, both are real gaps, neither blocks the
   server opening this week.

The thing that most determines whether this works is on none of those lists.
It is Discord's own line: *one developer reply per day.*
