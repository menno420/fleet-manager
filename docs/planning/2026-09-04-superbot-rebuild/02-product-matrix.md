# Product capability matrix — every meaningful capability, both bots, one disposition each

> **Status:** `plan` — authoritative for **what the successor's product contains**:
> capability by capability, what each existing bot actually has (with evidence),
> what a user needs, the disposition, which successor seam owns it, and how it is
> proved. It is authoritative for nothing about *how* the code is arranged —
> [`03-architecture-matrix.md`](03-architecture-matrix.md) owns that — and it
> settles no question of owner intent: rows the evidence cannot decide are routed
> to [`12-owner-decisions.md`](12-owner-decisions.md) by name rather than guessed.

## 0 · How to read this

**Dispositions.** One per row, chosen against the evidence, not against taste.

| token | means |
|---|---|
| `PRESERVE_BEHAVIOR` | the user-visible behaviour is carried across as it is today |
| `PRESERVE_CONTRACT` | the interface, permission tier or typed seam is carried; implementation is free |
| `PRESERVE_PATTERN` | the engineering shape is carried, not the code |
| `ADAPT` | carried with a named change, stated in the row |
| `REBUILD` | the capability is kept, the existing implementation is not |
| `SIMPLIFY` | carried with scope deliberately cut, stated in the row |
| `OPTIONAL_PLUGIN` | not in the core product; must be carriable by the extension contract |
| `DEFER` | not in the first phases; revisited at a named point |
| `DROP` | deliberately not carried — every instance is listed in § 3 with its reason |
| `OWNER_DECISION` | the evidence cannot decide; the row names its entry in `12-owner-decisions.md` |

**Successor owner** names the seam that owns the capability, not a file.
[`06-architecture.md`](06-architecture.md) is authoritative for the final names;
these are the roles this matrix commits to, and a row whose owner is `—` is a
row that does not ship.

**Verification method** names the proof layer from
[`08-verification.md`](08-verification.md) **and its population**, because a
layer without a population is the defect this whole plan is about
([`04-root-cause.md`](04-root-cause.md) § 2.4). `POP` = what the gate runs over;
`FLOOR` = the committed non-empty minimum asserted in the same run.

**Evidence ids.** `M*`/`R*`/`D-*` are fleet lane rows in
[`run/evidence-digest.md`](run/evidence-digest.md); `I-*` are this session's own
measurements in [`run/independent-findings.md`](run/independent-findings.md) and
**outrank a lane row where they disagree**. A number this session did not
re-derive is marked **`lane-claimed`** inline. Measurements first made while
writing *this* file are marked **`§2 measured`** and carry their command or
`file:line` in § 5.

## 1 · The three facts that decide most rows

Not a restatement of the root cause — three product-level consequences of it
that a reader needs before the tables make sense.

**1 · `superbot-next` ported the configuration surface and not the behaviour,
because that is exactly what the goldens covered.** Its `starboard` package says
so in its own first ten lines: *"the reaction-listener pipeline … is deliberately
NOT ported — no golden pins a reaction step"*
(`sb/domain/starboard/__init__.py:1-12`, **§2 measured**). `welcome` says *"the
member-join feed arms when the member band ports"*; `ticket` says every surface
it ports *"answers from the config-absent state those goldens captured"*. Counted
across the tree, **35 of 49 `sb/domain/` directories carry an under-port /
not-armed / "arms when" phrase in their own source** (**§2 measured** — a
candidate set, not a defect count, on the same footing as I-5). The mechanism is
[`08-verification.md`](08-verification.md) § 2.3: an unported capability emits
nothing, so no golden covers it, so absence is invisible.

**2 · The gateway census is the shortest proof of it.** `superbot` listens to
**16 distinct Discord gateway events** — audit-log entries, member join / leave /
update, messages (one platform-level `on_message` installed by
`message_pipeline.setup(bot)` at `disbot/bot1.py:977`, fanned out to 9 registered
stages), message edit / delete / raw-delete, reactions raw and cached, voice
state, guild join / remove, interactions, ready. `superbot-next` arms **5**
(`bot.add_listener` × 5: `on_interaction`, `on_message`,
`on_raw_reaction_add`, `on_raw_reaction_remove`, `on_guild_join`), and its
message feed's own docstring enumerates what rides it — prefix dispatch, the XP
chat award, the four-twenty egg — then says *"Everything else on the message band
stays DORMANT here, exactly as ledgered"*, naming counting, chain, fuzzy typo
re-dispatch and the AI shell (`sb/adapters/discord/message_feed.py:1-40`,
**§2 measured**). Its 3 reaction consumers are `ai.review_thumbs_down`,
`rps.tournament_signup`, `blackjack.tournament_signup` — starboard is not among
them. **Every "passive" feature in the right-hand column below is a settings page
with no trigger behind it**, and that is a census result, not a sample.

**3 · Reachability is the product problem, not a polish item.** From the
`help.*` roots `superbot-next`'s route graph has **max depth 0** — 314 panels
wired by 200 downward edges where a tree needs 313 — and `setup` is **39 of 40
panels unreachable** (I-13). `superbot` reaches setup only through an ephemeral
on-join launcher message with no route back, and 27 of 34 declared hub children
have a button on their parent hub — the shared discovery seam is 19 for 19,
hand-rolling is 8 for 15 (I-14). So *"does this feature exist"* and *"can anyone
get to it"* are separate columns in every table below, and the second one is
where both bots lose.

## 2 · The matrix

### A · Access, orientation and operation

| area | `superbot` has | `superbot-next` has | what users actually need | disposition | successor owner | verification |
|---|---|---|---|---|---|---|
| **Navigation & help** | 8 help categories behind one dropdown that swaps the message in place + a Back button; the flat "All Commands" browser deliberately deleted (D-S07, `disbot/cogs/help/panels.py:1-18,96-104`). 8 hubs / 34 declared children; **27 of 34** have a button; shared seam 19/19, hand-rolled 8/15 (I-14) | 314 panels, 66 of them `help.*`; framework-injected Back/Home/Help in one render block (M9-S01, `sb/kernel/panels/render.py:606-613`) — but **max depth 0 from `help.*`**, 129 of 314 unreachable from all entry points combined (I-13) | one front door that reaches **every enabled** feature inside the promised budget, and a route back from everywhere | `REBUILD` — keep `superbot`'s IA and `superbot-next`'s injected-nav mechanism; the route graph itself is generated from feature declarations, never hand-wired | `core/route-graph` | reachability walk over the **committed** route graph · `POP` = every panel reachable from the canonical entry · `FLOOR` = 100 % of enabled features ≤ 2 hops, asserted with the visibility model applied (I-14) |
| **Hub child rendering** | shared `discover_hub_children` seam used by 3 of 8 hubs, unfiltered comprehension + per-guild visibility filter at the caller; `ModPanelView` renders 7 action buttons and **0 routes** (I-14) | one panel engine renders all 314; **150 of 314 render zero injected nav components, 51 render zero components at all** (M9-D05, `lane-claimed`) | a hub always lists its children; a child never appears that the viewer may not use | `PRESERVE_PATTERN` + make universal by construction — one renderer, one generated contract over every registered hub (01-executive § 4.2) | `core/route-graph` | rendered-artifact contract · `POP` = every registered hub × its declared children · `FLOOR` = the declared child count; instantiate the view, read `children`, drive each callback (`tests/unit/views/test_games_hub_view.py` is the model, applied to 2 of 8 there) |
| **Setup & first-run** | a real first-run journey: `on_guild_join` creates a private setup channel, posts the launcher with an owner ping, degrades to safest-channel then DM (D-S06, `disbot/cogs/setup_cog.py:613-641`); recovery surface with Continue/Retry/Skip re-checking authority against a fresh snapshot (M1-S07). But **four front doors** (M1-D09, D-D12) and `setup` is not one of the 43 `SUBSYSTEMS` keys (I-13, **§2 measured**) | **40 setup panels — the largest single surface after help** — of which **39 are unreachable** (I-13); 10 setup commands; 2 of the 10 top-level section labels name internal mechanisms ("Cleanup inheritance", "Cog routing" — D-D06) | to be walked through it once, find it again on day 30, and never read a word of implementation vocabulary | `REBUILD` — **one** journey, one front door, setup a first-class node in the route graph. It is the first slice (12-owner-decisions § "What is deliberately NOT here") | `core/first-run` | journey + reachability · `POP` = every setup step in the declared journey · `FLOOR` = every step reachable from Home **and** resumable after the launcher message is deleted — the exact hole in both bots |
| **Settings** | `SubsystemSchema` per cog, 19 consumers, renders in the central hub with no UI code (R3-S3); reachability guard certifies from a **source literal**, so a schema module never registered still counts reachable (M1-D04) | **127 settings entries in the compiled snapshot** (**§2 measured**; M9-S08 counts 102 `SettingSpec` declarations in source — a source-vs-compiled delta, conclusion unchanged); a construction-time fence forces `external_side_effects=True` → `activation=off_until_opt_in` (M9-S08, `sb/spec/settings.py:314-318`); logging alone declares 23, automod 15, moderation 13 (**§2 measured**) | to change a thing and see it take effect; to find the setting from the feature, not from a settings tree | `PRESERVE_CONTRACT` (declare-once, render-free) + `REBUILD` the reachability proof over the **live** registry | `core/settings` | effect · `POP` = every registered setting · `FLOOR` = the declared count; each setting is written, re-read, and its feature's output must move (08-verification § 3c) |
| **Command access & lockout** | the best-shaped thing in either bot's operator layer: `resolve_command_access` admits a bootstrap command run by an operator **before** reading the per-guild policy row, so no policy can lock the owner out (M1-S01, `disbot/core/runtime/command_access.py:351-358`); both admission gates surface the user-facing reason + a structured deny line (M1-S08). Gap: the Server Management hub is in **neither** bypass list (M1-D05) | `settings access` command exists; no equivalent bootstrap escape hatch found in the lane rows | never to be locked out of the thing that unlocks the bot | `PRESERVE_BEHAVIOR` — port the escape hatch nearly verbatim, and derive the bypass list from the route graph instead of hand-keeping it (M1-D05 is a hand-list drift) | `core/access` | contract + negative control · `POP` = every registered operator entry point · `FLOOR` = all of them; assert each is admissible under every access mode |
| **Diagnostics / server status** | `!platform lifecycle` reads a **live** provider snapshot and degrades honestly to *"Provider not registered."* (R4-S05, `disbot/services/diagnostic_embeds.py:1270-1283`); real liveness/readiness endpoints + Prometheus (M7-S4). Gap: the settings hub's Missing-Bindings / Needs-Setup panels are read-only dead ends that say the fix is *"planned"* (M1-D10) | **42 diagnostic commands** — the second-largest command surface in the bot (**§2 measured**) — and the platform cards are **frozen capture literals**: `sb/domain/diagnostic/platform_views.py:180` ships *"ladder contiguous 001 → 103; all applied … count=103"* against **57** committed migration `.sql` files (**§2 measured**; R1 reports 28 such cards, `lane-claimed`) | a status card that is a fact about *this* process, and a fix button beside every problem it names | `REBUILD` — every diagnostic reads live state or refuses; every problem card carries the action that fixes it | `core/diagnostics` | effect + negative control · `POP` = every diagnostic card · `FLOOR` = all of them; mutate the underlying state and assert the card's output moves — the one test a frozen literal cannot pass |
| **Admin & runtime module control** | live load / unload / reload of any of the 59 extensions, audited, with a protected-core guard and two independent surfaces (R3-S2, `disbot/cogs/admin/cog_manager.py:191-200`); per-extension boot fault isolation, 59 of 59 (R3-S1) | the Cog Manager panel was ported **as a dead end** — Load/Unload/Reload wired to a handler that states the capability does not exist, recorded as final (R3-D8); `cogmgr.py:87-105` ships a hardcoded 58-entry roster of the **old** bot's cog modules so a golden replays green (M11-D05) | to silence a misbehaving feature in seconds without a deploy | `ADAPT` — keep the operator lever, drop code hot-unload: **per-guild and global runtime disable through governance**, audited, no `importlib` in the loop. Matches the 2026-08-21 plan's "no runtime code hot-unload in MVP" | `core/extension-host` + `core/governance` | effect · `POP` = every registered feature · `FLOOR` = all of them; disable each, assert its commands and panels stop resolving and an audit row exists |
| **Boot-time feature selection** | `INITIAL_EXTENSIONS` — **59 entries**, per-entry try/except, a failed extension demotes its subsystem to INTERNAL rather than crashing (R3-S1, **§2 measured**) | none: `load_live_manifests()` imports every module in `sb/manifest/`; **all 49 load unconditionally**, no flag, env var or config file (R3-D7) | to run a small deployment (the spider-bot shape) from the same codebase | `PRESERVE_CONTRACT` — boot-time feature profiles, declared, with per-feature fault isolation | `core/extension-host` | boot · `POP` = the declared profile's feature set · `FLOOR` = the profile's own count; boot each committed profile headlessly and assert exactly its features resolve |
| **Server management hub** | `ServerManagementHubView` re-evaluates the administrator floor **live on every interaction** rather than locking the panel to its invoker, which is what lets one builder back both a persistent anchored panel and an ephemeral one (M1-S04, `disbot/views/server_management/hub.py:126-134`) | 2 commands, 3 panels (**§2 measured**) | one operator console, and authority checked at the moment of the click | `PRESERVE_BEHAVIOR` — the live re-check is the rule for **every** persistent panel, not one view's habit | `core/route-graph` + `core/access` | contract · `POP` = every persistent/anchored panel · `FLOOR` = all of them; assert authority is re-resolved per interaction, with a demotion case |

### B · Membership and community

| area | `superbot` has | `superbot-next` has | what users actually need | disposition | successor owner | verification |
|---|---|---|---|---|---|---|
| **Roles / self-roles** | 17-command surface; role-menu view names and enforces Discord's 25-option select cap and the 25-component view cap rather than truncating at render (M2-S5, `disbot/views/roles/role_menu_view.py:36-38,270-272`); reaction roles, temp roles, autorole on join. Gap: the registry's operator-facing hint points at `!rolemenu`, which is itself `hidden=True` + `legacy_duplicate` (M2-D6) | 17 commands, 2 panels, 8 stores (**§2 measured**) — the second-largest store count in the bot after `mining`'s 9; the join-time autorole path has no listener (§ 1 fact 2) | to click a button and get a role; the operator to build that menu without hitting an API cap by surprise | `PRESERVE_BEHAVIOR` + `ADAPT` — carry the cap-awareness as a framework property of every selector, not a per-view constant | `feature/roles` | contract + effect · `POP` = every declared selector · `FLOOR` = all of them; assert the option/component budget is enforced before render, and that a grant writes the role and an audit row |
| **Welcome / onboarding** | `on_member_join` in 4 cogs (welcome, role, security, logging) — greeting, autorole, raid screening and join logging all ride the real event (**§2 measured**) | the setting is **ON by default** and can never fire: `welcome_join_enabled` defaults True, `!welcome` renders *"Greet on join — ✅"*, and **no `on_member_join` listener exists anywhere in `sb/`** (D-D04; **§2 measured** — 5 armed listeners, none of them member-join) | a greeting that actually greets, or a switch that admits it is off | `REBUILD` — and the rule the row exists to produce: **a setting may not be `on` unless its trigger is armed**, enforced at declaration | `feature/welcome` + `core/settings` | effect · `POP` = every setting whose activation implies a trigger · `FLOOR` = all of them; a declaration-time check that the named trigger is registered, plus a journey that joins a member and asserts the message |
| **XP / levels** | full: passive chat award through the message pipeline, config modals, rank cards, leaderboard provider (M3-S4, `disbot/services/rank_providers.py:14-17`) | genuinely armed — one of the **three** consumers of the live message feed (`sb/adapters/discord/message_feed.py:1-40`, **§2 measured**); 6 commands, 4 panels, 5 settings | levels that move when you talk, and a rank anyone can check | `OPTIONAL_PLUGIN` — OD-D's default: not core, must be carriable by the extension contract, and it **owns a table**, so it is the contract's first real load-bearing test (I-10) | `plugin:xp` | effect · `POP` = the award path · `FLOOR` = 1 armed trigger; post a message, assert the row moved and the level-up event fired |
| **Karma** | `karma_service.give` with self-give guard, per-recipient cooldown, daily cap and disabled check, tested against the real function with only the DB/bus mocked (M2-S4) | 4 commands, 2 panels, 4 settings, 2 stores (**§2 measured**) | to thank someone and see it counted | `OPTIONAL_PLUGIN` (OD-D) — carry `karma_service`'s **anti-abuse orchestration** as the pattern for every rate-limited user action | `plugin:karma` | effect · `POP` = the give path · `FLOOR` = 1; assert the cooldown and cap actually block, not just that the happy path writes |
| **Leaderboard** | a genuinely working plugin seam: `RankProvider` ABC + registry read by exactly 2 host surfaces, with **7 independently registered providers** (M3-S4) | 1 command, 1 panel (**§2 measured**); `leaderboard` is one of `economy`'s declared children in `superbot` and **the one economy child with no button on its parent hub** (I-14) | one board that any feature can appear on without editing the board | `PRESERVE_PATTERN` — this is the extension seam the successor wants, proven in production, and it is the shape to generalise beyond leaderboards | `core/extension-host` | contract · `POP` = every registered provider · `FLOOR` = the registered count; assert each provider's rows render and that registering one requires **no** edit to the host |
| **Counters** | counters cog under `community` (**§2 measured**) | 2 commands, 3 panels, **7 settings**, 0 stores (**§2 measured**); `counters.status` renders an embed and **zero components** — a member who clicks Counters on the Community hub has no route back (M9-D05, `lane-claimed`) | a live number in a channel name that stays correct | `OPTIONAL_PLUGIN` (OD-D) | `plugin:counters` | reachability + effect · `POP` = the counter's declared triggers · `FLOOR` = 1; change the underlying count and assert the rendered value moves |
| **Counting** | full game with persistence: `_save_guild`'s DB write rides the managed-task seam so a persistence failure is logged + metered instead of silently swallowed (M2-S2) | 10 commands, 1 store — and the counting listener is **named dormant in the message feed's own docstring** (**§2 measured**), so the count never advances | a channel game that survives a restart | `OPTIONAL_PLUGIN` (OD-D) — carry the fire-and-forget-with-a-supervisor pattern (M2-S2 / M6-S5) as a core rule, the game as a plugin | `plugin:counting` | effect · `POP` = the message trigger · `FLOOR` = 1; count, restart the process, assert the state survived |
| **Community spotlight** | present as a registered subsystem under `community` (**§2 measured**) | 1 command, 2 panels; subscribes an event bus name that the declared event graph does not model (M9-D07, `lane-claimed`) | occasional, ignorable, harmless | `DEFER` — no measured usage signal either way, and it is not on any journey the first slices need | `—` (deferred) | n/a until scheduled |
| **Starboard** | fully built — cog + service + 3 tables + 2 migrations + a config panel — and **absent from `SUBSYSTEMS` entirely** (M2-D1; **§2 measured**: 43 keys, `starboard` in none), so it is invisible to Help, the settings browser and per-guild governance; every one of its 5 config mutations emits an audit row from inside the function body (M2-S1) | config command group + 1 panel; the **reaction pipeline is explicitly not ported** — *"no golden pins a reaction step"* (`sb/domain/starboard/__init__.py:1-12`, **§2 measured**) | a starred message to actually appear on the board | `OPTIONAL_PLUGIN` (OD-D) + `PRESERVE_PATTERN` — `starboard_service`'s audit-inside-the-body shape is the template for every mutating service | `plugin:starboard` | effect · `POP` = the reaction trigger · `FLOOR` = 1; react past threshold, assert the board entry and the audit row |
| **Tickets** | open/claim orchestration tested against the real `tm.open_ticket`, asserting the emitted bus payload and that the audit call fired (M2-S7). Gap: no DB-layer test at all, unlike moderation and roles (M2-D7) | 12 commands, 2 stores — and its own package docstring says every surface *"answers from the config-absent state those goldens captured"*; the store, the channel-provisioning open flow and `!ticketsetup` are unported (`sb/domain/ticket/__init__.py:6-12`, **§2 measured**) | to open a ticket and have somebody find it | `OPTIONAL_PLUGIN` (OD-D) — but note it is the **one** capability the production AI is allowed to initiate (I-11), so its typed operation is on the core AI path even when the feature is a plugin | `plugin:tickets` + `core/ai-tools` | effect + journey · `POP` = the open→claim→close path · `FLOOR` = the full path; assert rows at each step, including through the AI-initiated entry |

### C · Safety and moderation

| area | `superbot` has | `superbot-next` has | what users actually need | disposition | successor owner | verification |
|---|---|---|---|---|---|---|
| **Moderation (manual)** | warn / timeout / kick / ban / unban / modlogs / clearwarnings, all routed through the audited mutation service; the moderated member gets a DM naming action, server and reason, templated with plain token replacement and **explicitly never `str.format`**, so an operator's brace cannot become an attribute expression (D-S08, `disbot/services/moderation_config.py:419-437`). Gap: `ModPanelView` is 7 actions and **0 routes to its 6 declared children** (I-14) | 9 commands, 13 settings, 2 stores (**§2 measured**); one audit row written inside the mutation transaction for every compound op — **175 of 175 registered ops carry an audit verb** (M9-S03, `lane-claimed` at 175; the single-call-site spine is I-18-confirmed at 1 site vs `superbot`'s 49 across 27 files) | the action to happen, the person to be told why, and the operator to find the record afterwards | `PRESERVE_BEHAVIOR` (the actions and the DM) + `PRESERVE_PATTERN` (`superbot-next`'s audit-inside-the-transaction spine, which is strictly better than 49 hand-written call sites) | `core/moderation-authority` + `core/audit` | effect · `POP` = every typed moderation operation · `FLOOR` = the registered count; each one mutates Discord state **and** writes exactly one audit row, asserted by reading both back |
| **Automod** | a registered message-pipeline stage at order 5, ahead of every AI stage — one of **9 stages** registered through the single `message_pipeline.register(...)` API (M4-S5; **§2 measured**: 9 call sites) | a **pure decision engine with zero production callers**: `sb/domain/automod/engine.py`'s `evaluate` is referenced only from `tests/` (**§2 measured**), behind 15 declared settings and 1 command. The engine is good; nothing feeds it | spam and invite filtering that runs on messages | `REBUILD` — take `superbot-next`'s pure-function decision engine and `superbot`'s ordered pipeline, and make "declared + enabled ⇒ armed" a checked property | `feature/automod` + `core/message-pipeline` | effect · `POP` = every declared rule × its trigger · `FLOOR` = the declared rule count; post a violating message, assert the deletion and the audit row; assert the engine has ≥ 1 production caller |
| **Security / raid** | raid lockdown with slowmode raise; the restart gap is **triaged, allowlisted with a named reason, and the allowlist entry states the residual user-visible caveat in plain language** (M2-S6, `architecture_rules/deferred_recovery_exceptions.yml:16-28`) — the estate's best-shaped honest limitation. The gap itself: `_hold_then_lift` is an in-memory `asyncio.sleep` with no persisted deadline, so a restart leaves slowmode raised indefinitely (M2-D2) | 1 command, 11 settings, no armed trigger (§ 1 fact 2) | protection that survives a deploy | `REBUILD` — every timed state change is a persisted deadline with a boot reconcile, never a sleeping task. `PRESERVE_PATTERN` for the exception-with-a-caveat convention, **plus an expiry** (08-verification § 3.4) | `feature/security` + `core/scheduler` | effect across a restart · `POP` = every timed state change · `FLOOR` = all of them; trigger, restart the process, assert the state was restored |
| **Image moderation** | the cleanest instance of [the 2026-09-04 AI-authority decision](run/in-flight-direction.md) already in production: images are classified by an external provider and any action is routed through `services/moderation_service` **so escalation and audit stay one authority**, only the image URL leaves the server, exempt channels short-circuit before the API call, and any fault fails **open** (`disbot/cogs/image_moderation/listener.py:1-20`, **§2 measured**). Gap: provider-unavailable is a silent per-message no-op with no in-Discord surface (M2-D3) | 1 command, 8 settings; *"the scan listener arms with the message band + provider keys"* (`sb/domain/image_moderation/__init__.py:1-3`, **§2 measured**) — not armed | protection that works, and a visible admission when it cannot | `PRESERVE_CONTRACT` — this is the reference implementation of AI-judgement / deterministic-authority; carry it verbatim in shape and add the degraded-state surface | `core/ai-gateway` → `core/moderation-authority` | effect + degraded-state · `POP` = the scan path · `FLOOR` = 1; assert the action goes through the same typed operation a button uses, and that provider-down raises a visible finding |
| **Logging / audit visibility** | subscribes `on_audit_log_entry_create` and mirrors **every** administrative action by **any** actor — humans in the web client and other bots included — into the log channel with the actor named, and surfaces the missing View Audit Log permission in `!logging status` rather than failing silently (D-S09, `disbot/cogs/logging_cog.py:249-266`, **§2 measured**). Severity-route fallback chain tested end-to-end against the real function (M2-S3) | 6 commands and **23 settings** — the largest settings surface in the bot (**§2 measured**) — and no audit-log listener; separately, **no read surface for its own audit spine**: the only `SELECT` against `audit_log` in the tree is the workflow engine's dedup lookup (D-D09) | at 2am, *"who changed this"*, answerable from inside Discord | `PRESERVE_BEHAVIOR` — the audit-log mirror is the single most operator-valuable thing either bot does and only one of them has it — **plus** the read surface neither has | `feature/logging` + `core/audit` | effect + journey · `POP` = the mirrored event classes · `FLOOR` = the declared class count; perform an action **outside** the bot, assert it appears in the log channel and is queryable in-Discord |
| **Cleanup / purge** | a registered pipeline stage (`CleanupStage`), channel cleanup levels, word filter, history sweep (**§2 measured**) | 7 commands, **12 panels** and 2 stores, of which **7 of 12 panels are unreachable** from every entry point combined (I-13); `!clear` answers *"🧹 Purging needs the live message view (arms with the live adapter)"* (`sb/domain/utility/handlers.py:40-41`, **§2 measured**) | to delete messages, with a preview of what will go | `ADAPT` — carry the levels model, make every destructive bulk action preview-then-confirm by declaration rather than by the author remembering (`superbot-next`'s confirmation predicate covers **2 of 640** actions — M9-D04, `lane-claimed`) | `feature/cleanup` + `core/policy-engine` | effect + confirmation fence · `POP` = every action the declaration marks destructive · `FLOOR` = the marked count, cross-checked against what the operation actually writes |

### D · Utility and member-facing extras

| area | `superbot` has | `superbot-next` has | what users actually need | disposition | successor owner | verification |
|---|---|---|---|---|---|---|
| **Utility (ping/avatar/serverinfo/userinfo/membercount/invite)** | present across `utility_cog` (**§2 measured**) | 14 utility commands, 10 panels, 0 stores (**§2 measured**) | small facts, instantly, with no ceremony | `PRESERVE_BEHAVIOR`, `SIMPLIFY` — carry the read-only ones; they are cheap and they are what a member types first | `feature/utility` | journey · `POP` = every utility command · `FLOOR` = all of them; each returns a non-error reply in a real guild |
| **Polls** | works, and is a toy: a reaction poll on a plain embed, hardcoded ≤ 10 options, **no persistence, no tally command, no expiry, no audit row** (`disbot/cogs/utility_cog.py:297-311`, **§2 measured**; M2-D5) | validates the option count and then refuses: `_POLL_DOWN` = *"📊 Poll creation needs the reaction egress port (arms with the live adapter)"* (`sb/domain/utility/handlers.py:38-39`, **§2 measured**) | a poll whose result can still be read tomorrow | `REBUILD` **or** `DROP` — it ships with persistence, a tally and an expiry, or it does not ship. Carrying the current shape forward is what the owner's *"trials and errors"* names | `plugin:polls` (OD-D) | effect · `POP` = the poll lifecycle · `FLOOR` = create→vote→close; assert the tally survives a restart |
| **Reminders** | `!remind` is `tasks.spawn(asyncio.sleep(delay))` then a channel send — **no DB row, no boot reconcile, nothing anywhere else in the tree named `remind`** (`disbot/cogs/utility_cog.py:55-64`, **§2 measured**; M2-D4). A deploy 90 seconds in destroys it silently | worse in the exact way § 1 predicts: `utility.remind_view` returns *"⏳ Reminder set for **N** minute(s)"* and **nothing delivers anything** — the handler's own docstring says the golden's capture window closed before any delivery, *"only the ack is pinned"* (`sb/domain/utility/handlers.py:371-394`, **§2 measured**) | the reminder to arrive | `REBUILD` — persisted deadline + boot reconcile, on the same scheduler as the raid-lockdown lift. This row and the security row are one mechanism | `plugin:reminders` (OD-D) + `core/scheduler` | effect across a restart · `POP` = every scheduled deadline · `FLOOR` = 1; set, restart, assert delivery |
| **General / fun content** (`fact`, `joke`, `quote`, `trivia`, `motivate`, `8ball`, `greet`) | present under `utility` (**§2 measured**) | 8 commands, 3 panels; **all 3 `general` panels unreachable** from every entry point combined (I-13) | harmless; nobody is blocked by their absence | `OPTIONAL_PLUGIN` — the cheapest possible first exercise of the extension contract: no data, no permissions, no triggers | `plugin:fun` | journey · `POP` = the command set · `FLOOR` = all of them |

### E · AI

| area | `superbot` has | `superbot-next` has | what users actually need | disposition | successor owner | verification |
|---|---|---|---|---|---|---|
| **AI gateway & providers** | **the origin of the design** — `superbot-next`'s own `sb/kernel/ai/gateway.py:1-6` says *"Ported from shipped `disbot/core/runtime/ai/gateway.py` @7f7628e1"*, and 24 of 30 files in `sb/kernel/ai/` name a `disbot/` source in their first 12 lines (I-4, I-18). Provider-independent by an AST guard with an empty allowlist over the real 883-file population (M4-S1); redaction at the single provider boundary and on every tool result re-entering context (M4-S7); 4 feature flags layering strictly, each defaulting safe (M4-S9) | the same eight pipeline steps plus two real additions: `socket_guard.deny_sockets()` makes the deterministic eval suite structurally incapable of a live network call — absent from `superbot` entirely (M10-S4) — and every metrics emission is fault-isolated in a guarded `_observe()` (M10-S5) | the bot to keep working when the model does not | `PRESERVE_CONTRACT` — carry the pipeline and the never-raises contract; take the two additions; **and add the enforcement neither has**: `superbot`'s guard is real but its successor's boundary *"is enforced by nothing"* (M10-D1) | `core/ai-gateway` | contract + negative control · `POP` = every module outside the provider package · `FLOOR` = the file count; AST-assert zero vendor SDK imports, with a planted violation as the negative control |
| **AI tools / actions** | a closed catalogue of **36** tools, of which **35 are read-only and exactly 1 writes** — `open_support_ticket`, and it writes *"through the audited mutation seam"*, the same path a button uses (I-11, M4-S3, `disbot/services/ai_tools.py:2416-2427`). Authority is derived from **verified Discord state, never from message text**, and checked twice — at registry build and at dispatch (M4-S4). Gaps: the one write tool is the one tool excluded from eval coverage (M4-D1) and there is **no per-cog tool registration hook anywhere** — 0 grep matches (M4-D6) | a better abstraction with a collapsed population: an open registry where authority can only narrow and grounding allowlists are derived — and **one `register_tool(` call site in all of `sb/`, registering 8 rows, every one a BTD6 factual read at `USER` scope, zero write-capable** (I-11). The audited write seam did not survive the port | the AI to be able to *do* a small number of useful things, through exactly the machinery a button uses | `PRESERVE_CONTRACT` (`superbot`'s read-mostly-plus-one-audited-write shape, production-proven) + `PRESERVE_PATTERN` (`superbot-next`'s open registry) + `REBUILD` the registration hook, because **neither bot has a working per-feature one** | `core/ai-tools` | population floor + effect · `POP` = the registered tool set · `FLOOR` = committed in the repo — the single line that turns "36 → 8" into a red diff instead of a discovery (08-verification § 2.3) · every write tool asserts its state change **and** its audit row |
| **AI chat (conversational)** | the last tier of a single ordered message pipeline — automod (5–25) and rewards (30–40) run and may delete or award **before** the AI stage (70) can short-circuit (M4-S5). Untrusted text wrapped in containment delimiters with forged delimiters disarmed by bracket-doubling (M4-S11). Gaps: `natural_language_stage.py` is 1,662 lines = 48 % of the AI package and the sole consumer of 3 services (M4-D10); containment covers 1 of 3 `AIRequest` construction sites (M4-D8) | the NL shell exists and is **not armed** — the message feed's docstring names *"the NL shell (AI arming is flag 7/52 owner work)"* among the dormant consumers (**§2 measured**) | to be answered, and never to be answered *instead of* the deterministic thing that should have happened | `REBUILD` on [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s pipeline — deterministic pre-check → optional AI analysis → **typed schema-validated verdict** → policy engine → permission/risk gate → typed operation → audit + case. `PRESERVE_BEHAVIOR` for stage ordering and containment; containment applies to **every** request construction site by construction | `core/ai-gateway` + `core/policy-engine` | contract + effect · `POP` = every AI entry point · `FLOOR` = all of them; assert (a) no free-form prose path reaches an action, (b) an invalid verdict produces **no** automatic action, (c) the deterministic tier ran first |
| **AI moderation & review** | `ai_review_cog` records a 👎 or a correction-reply against the bot's own AI answers, recovering the original Q&A from the answer registry so a correction can only be logged against a message the bot actually answered (`disbot/cogs/ai_review_cog.py:1-19`, **§2 measured**); `ai_decision_audit_service` is a real chokepoint with 8 production consumers that stores **no raw message content** (M4-S10) | `ai.review_thumbs_down` is one of only **3** armed reaction consumers (**§2 measured**) — so this is the one AI product surface that is live in both bots | a correction loop, and no autonomous moderation until it has a track record | `PRESERVE_BEHAVIOR` + `ADAPT` — new autonomous moderation starts in **shadow mode** per [the 2026-09-04 AI-authority decision](run/in-flight-direction.md); the review log is where its track record accumulates | `core/policy-engine` + `core/audit` | effect · `POP` = shadow verdicts · `FLOOR` = the shadow window's count; assert every shadow verdict is recorded with the action it *would* have taken, and that nothing executed |
| **AI configuration & instruction profiles** | per-guild/per-channel instruction profiles exist as a documented feature with **zero production consumers** — nothing under `disbot/` imports `ai_instruction_mutation`, so no command, cog or view reaches the write seam (M4-D4). AI config mutations are **outside** the audit log: 1 of 24 `ai_*` services calls `emit_audit_action` (M4-D5) | 12 AI settings, 24 AI commands, 27 panels — the largest panel surface after help and setup (**§2 measured**); 10 of its 27 panels unreachable (I-13) | to set the bot's voice for their server, and to see who changed the AI config | `REBUILD` — the write seam gets a route or it does not ship; AI config mutations go through the same audited path as everything else | `core/settings` + `core/audit` | reachability + effect · `POP` = every AI setting · `FLOOR` = all of them; each is reachable from Home and each mutation writes an audit row |

### F · Games, economy and content

| area | `superbot` has | `superbot-next` has | what users actually need | disposition | successor owner | verification |
|---|---|---|---|---|---|---|
| **Economy / casino / blackjack / inventory / treasury** (grouped) | the money-safety pattern is genuinely worth keeping: one conditional `UPDATE … WHERE coins >= $amount RETURNING coins` primitive reused by 7 service files (M3-S1), escrow-at-accept + idempotent settle under `FOR UPDATE` (M3-S2), and a single restart-safe checkpoint table whose invariant is a **DB constraint**, not application logic (M3-S3). Not universal: the daily/work reward gates still run the read-then-write race the debit path eliminated (M3-D1), and two documented "public API" functions are dead in production (M3-D3, M3-D4) | 9 economy commands, 5 stores; `casino` 2, `blackjack` 4, `inventory` 1 command / 8 panels, `treasury` 3 (**§2 measured**); `check_money_race` / `check_settle_once` are real AST gates with **excuse-row expiry** — 2 of the 10 checkers that carry exemptions do this (08-verification § 3.4) | nothing — OD-16 is explicit that casino/economy do not transfer | `DROP` from the product; `PRESERVE_PATTERN` for the debit primitive, the escrow shape and the checkpoint-as-constraint, which belong to **any** feature that moves a countable resource | `—` (pattern only) | n/a as product; the pattern is verified wherever it is next used |
| **World / idle games — mining, fishing, farm, creature** (grouped) | four cogs under the `games` hub, plus the `world_registry` seam — whose selling point *"a new world docks into the spine by registering one entry — no edit to the hub"* is **false for the two worlds it names as examples**: 2 of its 3 call sites are hardcoded (M3-D5) | mining is the third-largest command surface at **37 commands / 9 stores** — the most data-owning subsystem in the bot; fishing 20 / 5; creature 7 / 2; farm 1 / 1 (**§2 measured**) | nothing — OD-16 | `DROP` from the product — **and they are the acceptance load for the extension contract**: `disbot/utils/mining/capacity.py` and `sb/domain/mining/capacity.py` are **byte-identical**, md5 `64f1665a9fb83a940d95eca5b9492bf2` (I-20). Portability here is not hypothetical; it has already happened | `—` / test fixture for `core/extension-host` | the extension contract's own gate · `POP` = a stateful module ported end-to-end · `FLOOR` = 1 — an out-of-tree module that **owns data** must load, migrate and run, which is the requirement neither repo meets (I-10) |
| **BTD6 assistant** | the single largest thing in either repo: **30,923 lines**, more than the other 18 features in its lane combined (M3-D7, `lane-claimed`) | **74 of 413 commands — 17.9 %, the largest capability in the bot** (**§2 measured**), a permanent top-level help category a server owner cannot remove (D-D11) | nothing, in a server-first bot — but it is real content the owner built | `DROP` from the successor's core; `OWNER_DECISION` on whether it survives anywhere → [`12-owner-decisions.md`](12-owner-decisions.md) **OD-D**. Sizing note a roadmap must carry: scoping "port the games mass" without separating BTD6 under-estimates it by more than 2× (M3-D7) | `—` | n/a |
| **Project Moon** | a registered subsystem with its own cog (**§2 measured**) | 11 commands, 2 panels (**§2 measured**) | nothing — OD-16 | `DROP` | `—` | n/a |
| **Party games — deathmatch, rps_tournament, chain, four_twenty** | pipeline stages for chain and rps; deathmatch views (**§2 measured**) | `rps_tournament` and `blackjack` own **2 of the 3** armed reaction consumers in the whole bot — the tournament sign-up paths (**§2 measured**); `chain`'s listener is named dormant | nothing — OD-16 | `DROP` | `—` | n/a |
| **UX Lab** | an admin-only gallery of fake Discord UI patterns whose own cog docstring says it performs **zero writes**, at **4,937 lines across 13 files** (M3-D6, `lane-claimed`) | 2 commands, 1 panel (**§2 measured**) | nothing | `DROP` — see § 3 | `—` | n/a |
| **Proof channel / hermes / media maintenance / automation** | `proof_channel` is a staff-tier subsystem under moderation; `hermes` and `media_maintenance` are cogs with no registry key (R3-D10 lists 16 such unkeyed cog modules, `lane-claimed`; **§2 measured**: 59 extensions against 43 registry keys) | `proof_channel` 5 commands; `hermes` 2; `automation` **0 commands, 0 panels, 1 store** (**§2 measured**) — a subsystem with no surface at all | unclear; no journey in this review touches them | `DEFER` — and the general rule they illustrate: **a module with no registry key is invisible to help, settings and per-guild governance**, which is `starboard`'s defect (M2-D1) with 15 more instances | `—` (deferred) | n/a until scheduled |

## 3 · What deliberately disappears

Every `DROP` above, plus the product-level things that do not survive the
rebuild, each with the one reason that decides it. Recorded here so the absence
reads as a decision.

1. **Byte-parity goldens as the acceptance oracle.** They certify rendering
   stability and are kept for exactly that ([`08-verification.md`](08-verification.md)
   § 0); as an acceptance oracle they made a transcribed constant cheaper than a
   live read, and the shipping renderer is on **neither** side of the diff
   (08-verification § 3b).
2. **Four setup front doors.** `!setup`, `!setupadvanced`, the on-join launcher
   and the Server Management hub are one journey wearing four faces, and the repo
   names one of them a duplicate in its own command metadata (M1-D09, D-D12).
3. **The provisioning preview → Apply → confirm UI.** 450 lines across three
   modules with **zero production callers**, while all 3 call sites of
   `provision()` hardcode `confirmed=True` (M1-D03, M1-D02). The *confirmation
   requirement* survives as a declaration-level property (Band C, cleanup row);
   the orphaned UI does not.
4. **Read-only diagnostic dead ends.** `MissingBindingsView` and `NeedsSetupView`
   list the exact problems setup exists to fix and tell the operator the fix is
   *"planned"* (M1-D10). A problem card without an action is a screenshot.
5. **The frozen capture-world diagnostics.** A database-health card reporting
   *"103/103 migrations applied"* over a 57-file migration ladder
   (`sb/domain/diagnostic/platform_views.py:180`, **§2 measured**) and a
   58-entry roster of the **old** bot's cog modules shown as *"✅ Loaded"*
   (M11-D05) are not diagnostics; they are photographs of another bot.
6. **The Cog Manager dead-end panel.** Live select and pagination in front of
   buttons wired to a handler that states the capability does not exist (R3-D8) —
   a surface that looks functional is worse than an absent one.
7. **`bet_and_settle` and `fishing_workflow.fish()`.** Presented in their own
   module docstrings as canonical public API, with zero production callers
   (M3-D3, M3-D4). Documented dead code is a trap for the next porter, which is
   precisely the audience this plan has.
8. **UX Lab.** 4,937 lines of admin-only mock UI performing zero writes
   (M3-D6, `lane-claimed`), sitting in the same namespace family as real content
   so that every triage pass pays for it.
9. **`!rolemenu` as an advertised entry point.** The registry hint points at a
   command that is `hidden=True` with `classification: legacy_duplicate` and
   whose own docstring says to use `!roles` (M2-D6).
10. **Prefix-first as the primary invocation surface.** `superbot`: 249
    prefix-command/group decorators against 32 `@app_commands.command` and
    **zero** hybrids (**§2 measured**; D-D08 reports 243/30, `lane-claimed`).
    `superbot-next`: **386 prefix / 18 slash / 9 both** — 27 of 413 slash-reachable
    — with global sync hardcoded off at `sb/app/main.py:616`, so the entire
    declared-ephemeral surface (14 commands) is unreachable (**§2 measured**).
    A member's only built-in discovery affordance is `/`. The successor's
    invocation surface is a grouped slash tree; prefix is a declared alias
    (CHALLENGE C).
11. **Casino, blackjack, economy, inventory, treasury, mining, fishing, farm,
    creature, BTD6, Project Moon, deathmatch, rps_tournament, chain,
    four_twenty.** OD-16: *"casino/economy/BTD6 and unrelated content do not
    transfer."* They leave the product and become the **load test for the
    extension contract** — the thing that proves OD-19 rather than asserting it.
12. **In-memory-only reminders and polls.** Not dropped as features — dropped as
    *shapes*. Both bots ship a reminder that a deploy destroys and a poll nobody
    can read tomorrow; the successor ships them persisted or not at all.

**And one thing that pointedly does not disappear**, because a first cut of this
matrix nearly cut it: `superbot`'s always-answer error handler. One global
handler covers every prefix command across 7 branches including a three-outcome
typo ladder (D-S01, `disbot/bot1.py:501,548-621`), and 131 `delete_after=` sends
across `disbot/` keep the channel clean (**§2 measured**; D-S02 reports 113 in
`cogs/`, `lane-claimed` — my count there is 106). `superbot-next` deleted it:
`!helpp` produces **total silence** (D-D01), and it has **one** `delete_after`
send in the entire runtime (D-D10). The three-years-later bot is better here, and
it is the most basic member-facing property either bot has.

## 4 · What this matrix cannot settle

Four rows above are `OWNER_DECISION` or carry a default that is his to overturn.
Each is already stated in [`12-owner-decisions.md`](12-owner-decisions.md) with a
recommended default; nothing here re-opens them.

| the fork | rows it governs | where it lives |
|---|---|---|
| one server's tool vs a product for many servers | **Setup & first-run** (the whole 40-panel surface), per-guild scope in every settings and permission row | **OD-A** |
| which community features are core, optional, or gone | every `OPTIONAL_PLUGIN` row in Band B and D — xp, karma, leaderboard, counters, counting, community spotlight, starboard, tickets, polls, reminders | **OD-D** |
| whether BTD6 content survives anywhere | Band F, BTD6 row (30,923 lines, `lane-claimed`) | **OD-D** |
| how much authority the AI holds on day one | **AI tools**, **AI chat**, **AI moderation** — specifically whether a medium-risk reversible action executes without a human confirming | **OD-F** |

Everything else in this document was decided against the evidence. Where a
default was chosen because the cost is asymmetric rather than because the
evidence is conclusive, the row says so in its disposition cell.

## 5 · Method, and what this file measured itself

Per I-17's rule — *no lane-produced number reaches a matrix until this session
has re-derived it* — every figure above is one of three things: re-derived in
[`run/independent-findings.md`](run/independent-findings.md) (cited `I-*`),
re-derived while writing this file (marked **`§2 measured`**), or carried with
the tag **`lane-claimed`** inline.

New measurements made for this file, against `superbot` `5e3a667b` and
`superbot-next` `d5f66dc2`:

| measurement | how | result |
|---|---|---|
| `superbot-next` subsystem/command/panel census | `python3 -c` over `manifest.snapshot.json` | 49 subsystems · 413 commands · 314 panels; per-subsystem counts as quoted |
| command kinds | same | 386 prefix · 18 slash · 9 both; 14 declare `reply_visibility: ephemeral` |
| `superbot` subsystem registry | AST parse of the `SUBSYSTEMS` `AnnAssign` in `disbot/utils/subsystem_registry.py:58` | **43** keys; `starboard` and `setup` in **neither** — reproducing M2-D1/R3-D1 and I-13 |
| `superbot` extension list | AST parse of `INITIAL_EXTENSIONS` in `disbot/config.py` | **59** entries |
| `superbot-next` armed gateway listeners | `grep -rn "add_listener(" sb/` | **5**: interaction, message, raw reaction add/remove, guild join. **No** `on_member_join` anywhere in `sb/` |
| `superbot` gateway listeners | `grep -rhno "async def on_[a-z_]*" disbot/`, plus the platform `on_message` installed at `message_pipeline.setup()` (`disbot/core/runtime/message_pipeline.py:355`, called from `disbot/bot1.py:977`) | **16** distinct gateway events incl. `on_audit_log_entry_create`, member join/remove/update, voice state, message edit/delete. *Corrected from a first count of 15* — the `on_message` listener is registered inside `setup()`, so a `def on_*` grep alone misses it, which is the same instrument-without-a-control error I-18 records |
| `superbot` message-pipeline stages | `grep -rn "message_pipeline.register(" disbot/` | **9** call sites (counting, cleanup, ai, chain, rps, automod, image_moderation, xp, ai_review) |
| `superbot-next` reaction consumers | `grep -rn "register_reaction_consumer" sb/` | **3**: `ai.review_thumbs_down`, `rps.tournament_signup`, `blackjack.tournament_signup` |
| `superbot-next` automod engine consumers | callers of `evaluate(` outside its own module | production **0**; only `tests/unit/band2/` |
| under-port phrasing census | regex over all `sb/domain/*/**.py` for *arms with / arms when / not ported / under-port / named successor / lands with* | **35 of 49** domain directories. **A candidate set, not a defect count** — the same limit I-5 states for the capture-world vocabulary |
| frozen migration card | `grep -n "103" sb/domain/diagnostic/platform_views.py` vs `find . -name '*.sql' -path '*migration*'` | card claims `count=103`, repository holds **57** |
| `superbot` command-surface shape | `grep -c` for `@commands.command` / `@commands.group`, `@app_commands.command`, `hybrid_*` | **249 / 32 / 0** (D-D08 reports 243/30, `lane-claimed` — a grep-vs-AST delta, conclusion unchanged) |
| `superbot` transient-reply hygiene | `grep -c "delete_after="` | **131** in `disbot/`, **106** in `disbot/cogs/` (D-S02 reports 113 in `cogs/`, `lane-claimed`) |
| `spider-bot` product size | `spiderbot/ui/routes.py:49-156`; `ls spiderbot/cogs/`; `find spiderbot -name '*.py' -not -path '*__pycache__*'` + `cat … \| wc -l` | **8 routes** (5 member: join, optedin, feedback, bug, ask · 3 moderator: clock, post, health) across **6** cogs, **27 files / 3,172 lines** — the whole live product, reproducing 12-owner-decisions OD-C exactly |

**The honest null this file carries.** *"What users actually need"* is the one
column no measurement produces. Where the evidence supplies it, it does so
through a **measured failure** — a member types `!helpp` and gets silence, an
owner reads *"Greet on join ✅"* and watches three members join in silence, a
member clicks Counters and cannot get back — and those rows are grounded. Where
it does not, the row is `OWNER_DECISION` or `DEFER` and says which. No row in
this matrix asserts product intent the owner has not stated.

**And the bound worth keeping in view.** `spider-bot` runs a live, useful bot for
real users on **8 routes and 3,172 lines** (M12-S01, **§2 measured**;
12-owner-decisions OD-C carries the same caveat). Every `PRESERVE` and `REBUILD`
row above is a commitment against that number, and a successor whose first slice
out-builds it needs a reason it can state.
