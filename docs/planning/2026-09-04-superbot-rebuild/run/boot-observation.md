# `superbot-next`, booted and driven — the observation behind verdict gap 1

> **Status:** `reference` — an observation record, not a conclusion. Written
> 2026-09-04 (fm #1040) at the pin **`d5f66dc27768d49b2755f368c6a2d0ecca66a1af`**,
> which was the live head of `main` at the time (`git ls-remote`, same day).
> Certainty tags per
> [`../../../findings/2026-08-05-foundation-continuation.md`](../../../findings/2026-08-05-foundation-continuation.md):
> everything below is `MEASURED` unless it says otherwise, **and "measured"
> here means measured HEADLESS** — read § 1 before quoting any number.
>
> **What produced it:** [`headless_drive.py`](headless_drive.py), run eight
> times to a clean end on a fresh database while the walker itself was being
> corrected (§ 6, § 7) and then hardened after review, plus one *restart* run
> over the same database. The retained result of the final run is
> [`raw/headless-drive-2026-09-04.json`](raw/headless-drive-2026-09-04.json)
> (every interaction, render and `resolve()` outcome, and the process log;
> message payloads and component lists dropped, texts clipped — the
> `--retain` mode of the instrument, § 12, is the whole transform). The panel counts in §§ 2–6 were
> identical across the runs; § 7's figures are the final run's.

## 0 · The finding in one paragraph

The composition root boots, cleanly, in about a second, and the rebuild's
front door is worse at runtime than the static read said and better in one
place. **Better:** the help tree is not depth 0 — its selectors are
provider-fed, so `/help` reaches 57 of 66 help panels, up to five taps deep.
**Worse:** 48 of those 57 carry nothing but a Back button and **not one click
leads out of the help tree**; the primary setup entry (`/setup`, and the join
launcher's *Start Setup*) creates the private workspace channel, renders the
first card and **never sends it** — the production presenter has no send
branch for a request without an interaction origin, the parity twin does, so
the reply links to message id `0` and the 13-panel essential flow is
unreachable through the shipped adapter; a guild owner **locks themself out of
every control in a channel with one click** on the Command Access panel,
because the owner override belongs to the platform owner; and two unhandled
`AttributeError`s sit behind ordinary buttons. The advanced wizard behind
`/setup-hub` works — 24 of its 40 panels rendered and 21 sent, its session
row, depth, skips and audit rows written and read back after a restart. Nothing here
touched Discord: the transport and the guild are synthetic (§ 1), and the
gateway leg is the owner's (§ 10).

## 1 · What is real, what is synthetic, what is not observed

The instrument stubs exactly one function and one transport, and everything
else that runs is `superbot-next` at the pin.

| layer | real or synthetic | how |
|---|---|---|
| composition root `sb.app.main.run_app()` | **real, end to end** | preflight → K0 installs → boot-gate leg A → `db.init` + 57 migrations → metrics → health server → `build_runtime` + live manifests → dispatch index → panels → leg B → plugin host → the discord.py `commands.Bot` → error handlers → egress ports → the test-guild effect ports → app-command tree → component feed → *(gateway stub)* → RUNNING → leg C → guild sync → intent markers → feeds → poll supervisor → rosters → escrow recovery → boot hooks → canary → serve → SIGTERM → drain → STOPPED |
| PostgreSQL | **real** (PostgreSQL 16, throwaway local cluster, fresh database per run) | `initdb`/`pg_ctl` under the container's `postgres` account; DSN on `127.0.0.1:54329` |
| the dispatch spine | **real** | discord.py `Interaction` → `bot.tree._call` / `component_feed.handle_*` → `resolve()` → the panel engine → **`DiscordPanelPresenter`** (the production presenter, `sb/adapters/discord/panel_view.py`) → discord.py `InteractionResponse` / `Webhook` → the wire payload |
| the gateway | **stubbed** | `gateway.connect_gateway` replaced by a stub that fills what READY would have filled (client user, application id, one guild) and returns a task that ends when the root closes the bot. **No token is read** — the token variable is overwritten with a placeholder before import, as the repo's own `restore-verify.yml` does |
| Discord's REST API | **faked in-process** | `HTTPClient.request` and the webhook adapter answer from a recorder that mints message ids and stores payloads; 17 routes answered (one of them, the remote command list, deliberately refused); 4 met and not modelled (moderation kick/ban, `GET /users/{id}`) |
| the guild | **synthetic** | one guild, five text channels, three roles, four members (owner · admin · member · the bot); permission overwrites are stored, not enforced |
| the actor | **synthetic** | the guild owner unless a step says *member*; member tier comes from the real `member_tier_from_member` over the synthetic payload |
| the clicks | **synthetic payloads, real ids** | INTERACTION_CREATE dicts built from the recorded messages — a click carries the exact `custom_id` the presenter put on the wire; selects carry a real option value; native pickers carry a synthetic channel / role / user id; modals are submitted with `3` for numeric-looking fields and a fixed string otherwise |
| **not observed at all** | — | rate limits, permission errors, the remote command set, the real READY, rendering in a client, a human. This is below rung R4 of [`../08-verification.md`](../08-verification.md) § 4 and does not claim it |

**Population contract** ([`../08-verification.md`](../08-verification.md) § 1):
`EXPECTED` is the 314 panel ids of the committed `manifest.snapshot.json`,
read independently of the engine; `ACTUAL` is the set of panel ids the
presenter was asked to present. § 8 reports both directions of the difference.

## 2 · The boot

Log lines from the final run, in boot order (the whole process log, boot to
shutdown with the dispatch-trace lines dropped, is the raw record's
`process_log`):

| step | observed |
|---|---|
| `db.init` | 57 migrations applied, `0001 idempotency keys … 0057 command access channel roles`, on the empty database (`pool.init` — pool + migration chain + the checksum verify the root documents; only the *Applied* lines are in the log) |
| health server | `listening on 127.0.0.1:18080` |
| `build_runtime` | `live dispatch index installed: 1327 target(s)` |
| panels | `panel registry armed: 314 manifest-declared panel(s)` |
| plugin host | both pinned plugins **skipped — not installed** (`superbot-idle-plugin`, `superbot-plugin-hello`) |
| effect ports | moderation, role, channel and utility/diagnostic ports **ARMED for the synthetic guild only** (`SB_DATA_PLANE=test` + `SB_APPCMD_SYNC_GUILD_ID`) |
| app-command tree | `27 slash command(s) from the live manifests` |
| component feed | armed (buttons, selects, modal submits) |
| leg C | `compare-only fetch failed (non-fatal)` — the fake refuses `GET /applications/{id}/commands` so that nothing here pretends to know the remote set |
| guild sync | `27 command(s) → guild 900000000000000000` — the LOCAL tree, accepted by the fake `PUT`; says nothing about Discord |
| intents | both privileged intents **DEGRADE** (no approval env set): the message feed is **not armed**, so the prefix surface (`!help`, `!setup`) was never driven |
| feeds | reaction feed 3 consumers; guild-join feed 1 consumer (`setup.launcher`) |
| rosters | 6 `subscribe(bus)` modules armed |
| boot hooks | `setup.resume_sweep: ok` |
| readiness | `boot complete: RUNNING` at **1.25–1.96 s** after `run_app()` started (the eight runs); `/ready` → **503** `{"status": "not_ready", "reason": "gateway_not_ready", "phase": "RUNNING", "accepting_commands": true}` — correct for a process with no gateway |
| shutdown | SIGTERM (the root's own handler) → drain → `lifecycle STOPPED — clean exit`, **`run_app()` returned 0** |

`REASONED`: the boot is the part of the package's dynamic picture that was
never in doubt, and the run confirms it — the root is a real boot script, its
rails compose, and the readiness decision table answers truthfully.

## 3 · First contact on a fresh guild, empty tables

| who | what | answer |
|---|---|---|
| guild owner | `/help` | `help.home` rendered, ephemeral |
| plain member (no roles) | `/help` | `help.home` rendered — the help tree admits everyone |
| plain member | `/setup-hub` | **stated refusal:** *"You need the **administrator** role (or higher) to use this."* — `authority`, not silence |

**Not reproduced:** the 2026-08-05 audit's note that *"commands answer nothing
on a fresh database"* unless `guild_command_access_policy.mode` is set. At
this pin, with no policy row, `resolve_channel_access` receives `mode=None`
and allows (`sb/kernel/authority/channel_access.py`, `_policy_verdict`), and
every slash command answered on the empty database. The prefix surface was
not driven (§ 2, intents), so the note may still hold there — `UNVERIFIED`.

## 4 · The help tree, walked to exhaustion

`/help` as the owner, then every control on every rendered panel, once — 116
interactions, queue empty, budget not exhausted.

| measure | static read (the package, `reachability_probe.py`) | runtime (this run) |
|---|---|---|
| help panels reachable from `/help` | **0 edges** — max depth 0, because the selectors' options are provider-fed and the snapshot carries none | **57 of 66**, depth histogram `{0: 1, 1: 8, 2: 43, 3: 3, 4: 1, 5: 1}` |
| the 9 never reached | — | `help.cat_other`, `help.sub_hermes`, `help.sub_starboard` (the *Other* category is not among the 8 options `help.home` offers) and the 6 `help.editor_*` panels (the overlay editor; all 6 are reached from the admin hub — § 7) |
| dead ends | audit 2026-08-05: 60 of 66 with zero buttons, *"counted generously"* | **48 of the 57 reached carry nothing but `nav:back:*`**; the 9 with a control are `help.home` (one select, 8 options) and the 8 category panels (one select each) |
| exits | — | **0 panels outside `help.*` reachable from `/help`.** A sub-panel is a text list of command names and a Back button |

So the package's claim survives with its number corrected: the help tree is
internally navigable — a category select, then a feature select, then paging
(`More (2/4) ▶`) — and it introduces the user to **nothing**. The audit's
*"picture of a menu"* is what the production presenter actually sends.

## 5 · The setup flow

### 5.1 · The join launcher

`dispatch_guild_join` (the seam the live `guild_feed` adapter fires) with the
synthetic guild: **1 consumer.** The ladder ran as the source says it does —
`fetch_member` for the bot (a REST fallback, answered by the fake), **one
`POST /guilds/{id}/channels`** creating `#superbot-setup` with the overwrite
map, then **one channel send** into it:

> `<@owner> SuperBot just joined! I'll use this private channel as the setup
> workspace. Click **Start Setup** below (or run `!setup` / `/setup`) to begin.`

The launcher card's seven buttons, clicked as the owner:

| button | outcome |
|---|---|
| Start Setup | → the `/setup` path below: card rendered, **never sent** |
| Run Readiness Scan | text scorecard: *"Nothing essential is set up yet — run setup to get started"* + six ➖ essentials |
| Smart Suggestions | `setup.suggestions_card` rendered and sent |
| Choose Preset | `setup.preset_card` rendered and sent |
| View Summary | refusal: *"Setup is not complete yet. Run **Start Setup** to finish the wizard before viewing the summary."* |
| Repost launcher | the launcher card again |
| Dismiss | *"Setup dismissed. Use the setup launcher later to resume."* — `setup_status = dismissed` written |

### 5.2 · `/setup` — the primary entry — renders its card and never sends it

`/setup` (`setup.essential_open`, `sb/domain/setup/handlers.py:61`) does what
its docstring says: ensures the workspace (found this time — the join created
it), then `service.post_panel_to_channel(ESSENTIAL_PANEL_ID, …)`, then replies
with a pointer. What the run saw:

- the panel engine rendered `setup.essential_card` — title *"✨ What kind of
  server is this?"*, one select and two buttons (*Save & continue*, *Skip —
  set things up myself*);
- the production presenter **returned `None` and sent nothing** — no channel
  send, no followup, no edit — because `post_panel_to_channel`
  (`sb/domain/setup/service.py:178-200`) re-scopes the request with
  `origin=None` and a `_ChannelSendOrigin` responder, and
  `DiscordPanelPresenter.__call__` (`sb/adapters/discord/panel_view.py:321-379`)
  has four send branches — channel-anchor *with an origin channel*, an
  un-acked interaction response, a followup, a message `reply` — and none of
  them matches a request with no origin. The parity `ParityPresenter`
  (`sb/adapters/parity/transport.py:522-560`) has exactly that branch:
  `if channel_id is None: gap(...)` else `record_send(channel_id, payload)`.
  `_ChannelSendOrigin`'s own docstring names the gap: *"the live presenter's
  channel-anchor lane is the D-0049-family successor"*;
- the reply: **`✅ Setup is ready in <#…> — [open it](https://discord.com/channels/900000000000000000/910000000000000269/0)`**
  — message id `0`, because the post returned nothing to link to.

The same shape drops three panels in this run: `setup.essential_card`
(`/setup`, *Start Setup*), `setup.status_card` (`/setup-status` — *"📋 Setup
status posted in <#…>"*, nothing posted) and `setup.workspace_notice`
(`push_setup_notice`). `/setup-advanced` renders `setup.hub` the same way and
replies with a `/0` link too. **The 13 `setup.essential_*` panels behind the
card were never rendered by anything in this run.** `REASONED`: the goldens
that pin these surfaces (`goldens/setup/sweep_setup`,
`sweep_slash_setup-advanced`) replay through the parity presenter, which is
the mechanism [`../04-root-cause.md`](../04-root-cause.md) describes — here is
its most consequential instance: the first thing a new server owner is told
to click links to a message that does not exist.

### 5.3 · `/setup-hub` — the advanced wizard works

`/setup-hub` answers with the ephemeral depth chooser (`setup.hub`: ⚡ Quick ·
🛠 Standard · 🔬 Advanced); a depth click mints the session row
(`setup.start_session`) and opens `setup.sections_hub`; each section card
opens its detail; presets preview; the final review renders. **The setup walk
(183 interactions, queue empty) rendered 23 of the 40 setup panels and sent 20
of them** — the three of § 5.2 were dropped — and the launcher phase adds
`suggestions_card`, so across the two phases **24 are rendered and 21 sent**:

`setup.hub` · `sections_hub` · `section_channels` · `channels_detail` ·
`section_logging_presets` · `logging_picker` · `section_roles` ·
`roles_detail` · `section_role_templates` · `role_templates_detail` ·
`section_cleanup` · `cleanup_detail` · `section_moderation` ·
`moderation_detail` · `section_cog_routing` · `cog_routing_detail` ·
`preset_card` · `preset_preview` · `final_review` · `wizard_step` ·
`suggestions_card` (from the launcher).

The effect layer is real here. The setup phase alone — the join, the setup
walk and the launcher clicks, against a baseline taken just before it — wrote:
`setup_session` 1 row (`depth = advanced`, `skipped_sections` for every
section the walker skipped, `setup_status` and `current_step` rewritten by
the clicks — `in_progress` / `cog_routing` at the end of the run, `dismissed`
in the run whose launcher walk ended on *Dismiss*), `audit_log` +62
(`setup.session.depth_set`, `setup.session.section_skip`,
`setup.session.dismissed`, …), `sb_drafts` 1 + `sb_draft_operations` 34 (the
staged operations `/setup-reset` later reports clearing: *"✅ Cleared **34**
staged operations"*), `ticket_config` +1, `event_outbox` +62 with the relay
delivering as it ticked. What the boot, the first contact and the help walk
had written before that baseline: the 57 migrations, 7 `ai_instruction_profile`
rows, 4 idempotency keys, 4 invariant-sweep rows, 1 `settings` row (the
platform latch), 1 audit row (the boot canary) and 2 outbox rows — the help
tree writes nothing.

Three modals were issued and submitted (roles time tier, roles XP tier, the
ticket launcher's *Open a support ticket*); the numeric ones took the value.

### 5.4 · Three of the ten setup commands cannot work from slash

`register_app_commands` registers every command **parameterless**
(`sb/adapters/discord/command_tree.py:9-12`: *"CommandSpec declares no option
facet, so commands register parameterless"*). Observed: `/setup-describe`
always answers the empty-description hint; `/setup-skip` and `/setup-unskip`
always answer *"Unknown section ``. Available: …"*. They are prefix-only
commands wearing slash names.

### 5.5 · Two unhandled exceptions behind ordinary buttons

| where | what | user sees |
|---|---|---|
| `sb/domain/ticket/setup_panel.py:159` and `:191` | `result.ok` on a `WorkflowResult` (`sb/kernel/workflow/result.py:82` — no such field) | *Enable tickets* and *Auto-create log channel* on the Support Tickets section → **"Something went wrong on our end — it's been logged."** (a `BUG` envelope) |
| `sb/domain/platform/guild_snapshot.py:243` | `spec.name` on a `ResourceRequirement` while walking manifest `settings` facets | logged as an exception on **every** setup recommender read (110 records in the retained run's process log); the channels section degrades to the advisor fallback, silently |

Both are in code the goldens replay past. `REASONED`: neither could have been
caught by a parity oracle, because both are in the live seams (the workflow
result read on the live path, the gateway-cache snapshot) that the parity
harness replaces.

### 5.6 · Restart — "come back the next day"

A second boot over the same database: `boot hook setup.resume_sweep: ok`
(nothing to resume — the session row carries no launcher message id,
`setup_message_id` is `NULL`), `/setup-hub` shows the depth chooser again (static copy — it does
not reflect the saved `depth = advanced`), `/setup-status` and `/setup` drop
their cards exactly as before, `/help` renders. The session row survived the
restart with its depth and skips intact. `UNVERIFIED` whether the sections hub
re-reads the row (the restart run did not click a depth); `REASONED` from
§ 5.3 that it does, since the walk's own skips were read back into the row.

## 6 · The lock-outs

In the global walk (§ 7) the owner opened `settings.command_access` and
clicked, in order, *All channels* (fine), *Selected channels*, and then the
next button on the same panel:

> **"Commands aren't enabled in this channel. Use one of the configured
> command channels or ask an admin to update Command Access in `!settings`."**

Every control in `#general` — the panel's own buttons included — was denied
from that click on. The same happened after the panel's role picker set a
per-channel role-set (*"Commands in this channel are limited to specific
roles…"*) and after *Disabled except bootstrap*. Three shapes, one cause:
`owner_override_holds` (`sb/kernel/authority/owner.py:80`) is **platform
owner AND member** — the guild owner gets no override, and component targets
are not bootstrap commands (`sb/namespace/bootstrap.py` is a fixed name list:
`help`, `settings`, `setup`, …). The reply's advice is `!settings`, a prefix
command, dead without the message-content intent (§ 2). Whether `/settings`
(bootstrap) re-opens the hub is `REASONED` yes; whether its buttons then work
is `MEASURED` **no** — that is what the denials above were.

**Intervention, recorded:** the instrument detects a `channel` denial,
records the lock-out with the click that caused it, resets the policy in the
database (`mode = all_channels`, the channel and role-set rows deleted,
`forget_guild` to drop the 60-second reader cache) and replays the denied
click once. Three lock-outs were met and reset in the final run; the walk
then continued with **no further channel denials**. Without the reset, the
first run lost 1,646 of its 2,770 interactions to the lock-out.

## 7 · Every slash command, every control

The 27 commands in the tree, as the owner, then every rendered control once —
a control keyed by its declared identity, because session-lifecycle panels
(the Cog Manager) mint a fresh id per render and an id-keyed walk re-clicked
one select 6,518 times before that was fixed.

- **All 27 commands answered.** 23 render a panel — three of them the
  dropped workspace cards of § 5.2, two of them `hermes.bridge_unconfigured`
  (`/bugreport`, `/dispatch`: honest, no bridge configured); four answer in
  text — `/setup-reset` usefully, `/setup-describe`, `/setup-skip` and
  `/setup-unskip` as § 5.4 says.
- **Interactions:** 1,493 in the global walk — 1,490 clicks plus the three
  replays after the lock-out resets of § 6 — and 1,802 in the whole run
  (3 first-contact + 116 help + 183 setup + 7 launcher + 1,493); budget not
  exhausted (8,000 allowed), queue empty; 42 modals submitted.
- **Panels rendered from any command:** 236 (depth histogram
  from the command roots `{0: 21, 1: 66, 2: 114, 3: 28, 4: 4, 5: 3}`).
- **`BUG` envelopes met:** 4 — the two ticket buttons of § 5.5, each met in
  the setup walk and again here; nothing else carried the `bug` error class.
  One more reply carried the same *"Something went wrong on our end — it's
  been logged."* copy as a handler-level `blocked` result:
  `blackjack.hub.bj_solo_bet`, the solo-bet modal, whose bet field the walker
  filled with text (§ 11) — a validation gap that answers with the crash copy
  rather than a *"bets are numbers"* line.
- **Not modelled, met:** `PUT /guilds/{id}/bans/{uid}`, `DELETE …/bans/{uid}`,
  `DELETE /guilds/{id}/members/{uid}`, `GET /users/{uid}` — the live moderation
  effects, which the fake refuses (each rendered as the adapter's honest
  *"Could not …"* copy); a real test guild would take them.

**Never rendered by anything in this run — 77 of 314, by subsystem:**

| subsystem | never rendered / expected | panels |
|---|---|---|
| `setup` | 16 / 40 | `setup.apply_recovery`, `setup.complete_card`, `setup.essential_commands`, `setup.essential_extras`, `setup.essential_greet`, `setup.essential_helpdesk`, `setup.essential_log`, `setup.essential_mods`, `setup.essential_resume`, `setup.essential_reward`, `setup.essential_reward_role`, `setup.essential_spam`, `setup.essential_summary`, `setup.launcher`, `setup.review_item`, `setup.section_recovery` |
| `btd6` | 8 / 8 | `btd6.card`, `btd6.ctteam`, `btd6.ctteam_confirm`, `btd6.hub`, `btd6.paragon`, `btd6.paragon_requirements`, `btd6.paragon_stats`, `btd6.strategy_submit` |
| `inventory` | 7 / 8 | `inventory.cat_collectibles`, `inventory.cat_crafted_items`, `inventory.cat_economy_items`, `inventory.cat_fishing`, `inventory.cat_mining_materials`, `inventory.cat_other`, `inventory.cat_tools` |
| `rps_tournament` | 5 / 6 | `rps_tournament.botmatch`, `rps_tournament.match`, `rps_tournament.pvp`, `rps_tournament.quickplay`, `rps_tournament.registration` |
| `mining` | 5 / 10 | `mining.forge`, `mining.home`, `mining.skills`, `mining.titles`, `mining.vault` |
| `utility` | 5 / 10 | `utility.bot_info`, `utility.error_card`, `utility.member_census`, `utility.pong`, `utility.user_card` |
| `blackjack` | 4 / 6 | `blackjack.pvp`, `blackjack.registration`, `blackjack.tournament_results`, `blackjack.tournament_table` |
| `help` | 3 / 66 | `help.cat_other`, `help.sub_hermes`, `help.sub_starboard` |
| `creature` | 3 / 9 | `creature.collectors_card`, `creature.dex_card`, `creature.record_card` |
| `general` | 2 / 3 | `general.card`, `general.trivia_card` |
| `channel` | 2 / 9 | `channel.info_card`, `channel.list_card` |
| one each | 17 / — | `fishing.card`, `proof_channel.hub`, `casino.poker_game`, `security.status`, `image_moderation.status`, `counting.rules_card`, `cleanup.policies_remove`, `automod.status`, `starboard.config`, `economy.daily_card`, `settings.access`, `deathmatch.challenge_card`, `ai.card`, `karma.error_card`, `counters.presets`, `role.info_card`, `xp.import_scan` |

`REASONED`, per class: the 13 `setup.essential_*` + `complete_card` +
`apply_recovery` + `review_item` + `section_recovery` sit behind the dropped
card (§ 5.2) or a recovery state the walk never entered; the game interiors
(`rps_tournament.*`, `blackjack.*`, `deathmatch.challenge_card`,
`casino.poker_game`, `creature.*`, `fishing.*`, `mining.*`) need a second
player, a running match or a modal the walk answered with a wrong value; the
`*_card` and `*.status` panels are effect renders behind live reads the
synthetic guild cannot serve (`utility.member_census`, `channel.info_card`,
`security.status`) or behind prefix-only commands. The static probe's
*"185 of 314 reachable from all entry points combined"* is therefore
**237 of 314 rendered (234 sent) — 52 more than the static combined-roots figure, from the same 314** at runtime — a fuller walk with a second actor and
game state would move it further; the walk's own budget did not bind.

## 8 · The population contract, applied

| set | count |
|---|---|
| `EXPECTED` — panel ids in the committed snapshot | **314** |
| presented — the presenter was asked to present it | **237** |
| sent — the presenter put it on the wire | **234** |
| rendered but never sent | **3** — `setup.essential_card`, `setup.status_card`, `setup.workspace_notice` (§ 5.2) |
| presented but not in `EXPECTED` | **0** |
| expected but never presented | **77** (§ 7) |

The identity check both ways is the contract; the interesting number is the
third row, which no floor would have caught.

## 9 · What this changes in the package

| claim, where | static / prior | runtime | disposition |
|---|---|---|---|
| I-13, `09-roadmap.md` § 2: *"From `help.*` roots max depth is 0"* | declared graph: 0 downward edges from help | **57 of 66 help panels reached, depth up to 5** — the edges are provider-fed at runtime | **number superseded; conclusion sharpened** — the tree is navigable and leads out to nothing (§ 4) |
| I-13: *"`setup` is 39 of 40 panels unreachable from every declared entry point"* | declared graph | **23 of 40 rendered and 20 sent** from `/setup-hub` (the advanced wizard; 24 and 21 with the launcher's suggestions card); **the essential flow's 13 are unreachable through the production presenter** (§ 5.2) | **split** — the wizard IS in the graph behind a slash root; the primary entry is broken by a missing send branch, not by the graph |
| 2026-08-05 audit § 4b: *"the front door is 91 % dead ends"* | 60 of 66 button-less, generously counted | **48 of the 57 reached** have no non-nav control (84 %) and **0 exits** | **confirmed, tighter** |
| audit § 8: *"commands answer nothing on a fresh database"* | recipe note | slash commands answer with no policy row (§ 3) | **not reproduced on the slash surface**; prefix `UNVERIFIED` |
| I-19, `13-verdict.md` gap 1: *"this composition root publishes no command set"* | `sync_remote(..., enabled=False)` | the root **builds a 27-command local tree and guild-syncs it** when the test-guild opt-in is set; the global set is never written; the remote set stays unobserved | **holds for the global set; the guild leg is real code that ran** |
| `04-root-cause.md`, the parity presenter is a twin no production path uses | source read | the twin has a channel-send branch the production presenter lacks, and the primary setup entry falls through it (§ 5.2) | **confirmed with the worst instance** |
| `13-verdict.md` gap 4: *"533/533 goldens, 3,648 green tests"* as evidence of completeness | — | two unhandled `AttributeError`s behind buttons (§ 5.5), one dropped first card (§ 5.2), one one-click lock-out (§ 6) | **the package's thesis, instantiated** |
| `09-roadmap.md` § 2 acceptance drive step 7 (*a non-admin gets a stated refusal*) | design intent | the member's `/setup-hub` refusal names the reason (§ 3) | **already true in the donor** — `superbot-next`'s authority copy is a donor field, as `10-migration.md` says |
| `09-roadmap.md` § 2 acceptance drive step 5 (*restart, state read live*) | design intent | the session row survives; the depth chooser does not show it (§ 5.6) | **partly** — a runtime observation the R4 drive should repeat |

## 10 · The gateway leg — what is still owed, and the recipe

Nothing above observed Discord. The remaining leg is one owner-live step,
queued as `OQ-SUPERBOT-NEXT-GATEWAY-LEG` in
[`../../../owner-queue.md`](../../../owner-queue.md). What it adds:

1. **the identity check first** — `GET /users/@me` with the container's bot
   token must answer the test app (`1298426054636994611`, *Galaxy Bot*, per
   `superbot-next`'s `docs/status/testing-report-2026-07-09.md` and the
   2026-08-05 audit § 7 — **not re-verified here**); anything else stops
   before any connect;
2. **the remote command set** — `GET /applications/{app}/commands` and
   `GET /applications/{app}/guilds/{guild}/commands`: whether the audit's
   *"27 slash commands survive"* / *"78 stale commands from the old bot's
   tree"* is a fact today (the one-call measurement gap 1 names);
3. **a real boot** — `python3 -m sb` on the test plane with
   `SB_APPCMD_SYNC_GUILD_ID` set to a **fresh test guild**, `HEALTH_HOST`
   set, and both `SB_INTENT_*_OK` reflecting the portal (the ledger says
   both were approved on 2026-07-09): READY, the join launcher landing in a
   real channel, `/ready` flipping 200;
4. **a human's drive** — `/help` and `/setup` in that guild, which is the R4
   rung the successor's own gates will need anyway.

No token value belongs in any record; the recipe reads it from the
environment.

## 11 · Honest nulls

- **Synthetic guild.** Overwrites are stored, not enforced; `fetch_member`
  is answered from a dict; the bot is a member with an admin role. A real
  guild can refuse where this one allowed.
- **No client rendered anything.** Embed budgets, component limits and
  Discord's own rejections were not exercised — only the payloads.
- **My inputs.** Modals took `3` for a field whose label reads as a number
  and a fixed string otherwise; native pickers took one synthetic id each. The
  `invalid literal for int()` errors in the log are the walker feeding that
  string to numeric fields, not defects of the bot — most render as the
  handlers' own *"could not parse"* copy; the blackjack bet form (§ 7)
  answered with the generic failure copy instead, which is the one
  validation gap worth a line. `moderation.hub.logs`, which an earlier run's
  log showed failing on the same input, parsed the `3` and rendered
  `moderation.modlogs_card` in the retained run.
- **The prefix surface was not driven** (no message intent declared), so
  `!help` / `!setup` and the audit's fresh-database note are unmeasured here.
- **Timing is not representative** — no network, one process, one actor.
- **The walk intervened three times** (§ 6), by design and recorded.
- **The walk's coverage is a lower bound**, not the set of reachable panels
  (§ 7): one actor, no second player, no prior game state.

## 12 · Reproduction

```bash
# 1. the repo at the pin, and its hash-pinned venv
git clone https://github.com/menno420/superbot-next && cd superbot-next && git checkout d5f66dc2
python3.11 -m venv ../sbnext-venv && ../sbnext-venv/bin/pip install --require-hashes -r requirements.lock

# 2. a throwaway PostgreSQL 16 (any port; trust auth; a fresh database)
#    in the CCR container: initdb/pg_ctl under the `postgres` account, DSN
#    postgresql://superbot@127.0.0.1:54329/superbot

# 3. the drive — fresh database, then the restart check over the same one.
#    --pin is the revision you EXPECT; the drive refuses a checkout at any other
#    HEAD, or one with modified or untracked files (its own --out excepted), and
#    records the HEAD it actually ran on. Keep the outputs OUTSIDE the checkout.
DRIVE=<fleet-manager>/docs/planning/2026-09-04-superbot-rebuild/run/headless_drive.py
../sbnext-venv/bin/python $DRIVE --repo . --pin d5f66dc27768d49b2755f368c6a2d0ecca66a1af \
    --dsn postgresql://superbot@127.0.0.1:54329/superbot --out /tmp/drive.json
../sbnext-venv/bin/python $DRIVE --repo . --pin d5f66dc27768d49b2755f368c6a2d0ecca66a1af \
    --dsn postgresql://superbot@127.0.0.1:54329/superbot --restart-check --out /tmp/restart.json

# 4. the retained record (run/raw/headless-drive-<date>.json) is exactly this
#    transform of the two dumps — no hand step in between
python3 $DRIVE --retain /tmp/drive.json --retain-restart /tmp/restart.json \
    --out run/raw/headless-drive-2026-09-04.json
```

Read the real exit code, not one after a pipe — the drive returns 0 only when
the composition root itself exited 0 after a clean boot and shutdown. The
final run took about eight minutes; `--skip-global` gives the help and setup
walks alone in under a minute.
