# superbot-next — what booting it measured, and why the harness could not see it

> **Status:** `reference`
>
> Written 2026-08-05 from a live boot of `menno420/superbot-next` in a fresh
> container: real PostgreSQL 16, hash-pinned install, the owner's test bot token,
> connected to Discord, driven by the owner in his own guilds.
>
> **Purpose.** The owner is disbanding or rebuilding the project and plans
> multiple independent reviews — several sessions, several AI models, both
> repositories — feeding one plan executed cog by cog, with a **server bot
> carrying no game features** as the first milestone. This document exists so
> those reviewers start from measurements instead of re-deriving them, and so
> they do not inherit the three wrong claims this session made before booting it.
>
> Every number below was produced by running something. Where a claim rests on a
> grep or an estimate, it says so.

> **Correction, same day.** The first version of this document reported the
> menu-versus-text ratio as *"inherited, not introduced."* That was wrong and it
> dismissed the owner's central complaint. **§ 4b replaces it** with the
> measurement that matters — reachability — and § 7 records the error.

## 0. The finding in one paragraph

superbot-next boots, connects, and serves real interactions — 1,327 dispatch
targets, 314 panels, 640 buttons, real handlers, real database writes. It is not
a shell. But four of its files carry a **named, documented convention** in which
a value the old bot *computed* ships as a *literal* transcribed from the capture
corpus. The Cog Manager is the worst case: 58 hardcoded module names, status
glyphs baked into an f-string, and a legend advising a command that does not
exist in the build. It passes golden parity perfectly — **because it is the
captured bytes.** The construction was largely real; the verification method
could not distinguish working from photographed.

**The same transcription hit the bot's front door.** In superbot the navigation
graph *is* the product — one `!help`, then everything reachable by button in
about two taps. In the rebuild, **60 of 66 `help` panels have no buttons at
all**, and 153 of 314 panels overall. The help pages render the captured *text*
of the old bot's help output instead of a live route table. Byte-identical, and
one is a menu while the other is a picture of one. That is § 4b, and it is the
largest single thing the harness let through.

## 1. `CAPTURE-WORLD LITERAL` — the convention, in the codebase's own words

The phrase is a formal term in that repository, carrying trap numbers and
precedents. From `sb/domain/admin/panels.py`:

> **CAPTURE-WORLD LITERAL (trap 10a):** the shipped description interpolated
> `len(bot.cogs)` — the capture world's 58 loaded cogs. Both goldens pin the one
> value, **so the line ships as the pinned literal**; the live manifest-registry
> count (via `admin.subsystems_view`) is **the honest successor read** if a
> future golden pins a second value.

That is the mechanism stated plainly by its authors: **a value the capture
observed only once became a constant.** The real computation is acknowledged and
deferred.

### The Cog Manager, in full

`sb/domain/admin/cogmgr.py` is the surface the owner opened first, and it is the
convention at its most complete:

```python
#: the capture world's 58 loaded cogs, alphabetical — the golden-pinned…
_COGS: tuple[str, ...] = ("admin_cog", "ai_cog", … "xp_cog")
```

Those are **`superbot`'s module filenames**. superbot-next has no cogs at all —
its subsystems are compiled manifests. The list describes a different program.

The status indicators are not computed either. Line 169:

```python
lines.append(f"✅ 🟢  `{name}`{suffix}{marker}")
```

The glyphs are inside the f-string. Every entry renders *Loaded · OK*
unconditionally, and the module docstring says why: *"every cog was loaded +
syntax-OK in the capture world, so only the ✅/🟢 glyphs appear."*

The legend then instructs the operator:

> `🛡 Protected (panel unload denied — use !cog unload <name>)`

`!cog` is one of exactly three commands that were never ported (§ 3). The panel
directs the user to a command that does not exist.

Observed live, 2026-08-05: `admin:cogmgr:unload` → `outcome: blocked`. The
button is offered and refuses.

### Scope — measured, with its limit stated

| Marker | Count |
|---|---|
| Files carrying the literal `CAPTURE-WORLD LITERAL` | **4** |
| — | `admin/cogmgr.py`, `admin/panels.py`, `diagnostic/flag_catalog.py`, `diagnostic/command_catalog.py` |
| `honest successor` / `successor read` deferrals | 6 |
| Files mentioning "capture world" at all | 34 |

The 34 is **not** the defect count. Most are legitimately static — BTD6 datasets,
fishing weather tables, game constants — where transcription is correct because
the data really is constant.

The dangerous class is narrower and has a clean definition:

> **static data presented as live system state.**

All four labelled instances are admin or diagnostic surfaces, which is exactly
where output *describes* state rather than *being* the function. That is also why
the owner hit it within minutes: the cog manager and settings manager are the
first things anyone opens to evaluate a bot.

**The limit:** these were found by grepping a label. Nothing guarantees every
instance was labelled. **An unlabelled instance is invisible to this method** —
finding those needs the audit in § 6.

## 2. Why 533/533 golden parity certified it

The harness records the old bot's real outputs and requires the rebuild to
reproduce them byte-for-byte. Against that metric:

- A handler that replies *"this isn't armed in this build"* replays identically
  forever. **A polite refusal scores as full parity.**
- A panel printing a hardcoded roster reproduces the capture exactly. **A
  photograph scores as full parity** — necessarily, since it *is* the capture.
- A command that was never ported emits no output, so no golden covers it.
  **Absence is structurally invisible.**

So `533/533 goldens · 49/49 subsystems ported · zero unmapped` is *true* and
simultaneously compatible with panels that do nothing. The number was honest; it
measured the wrong property.

**This is the single most important thing to carry into any rebuild.** A month of
disciplined work against a metric that cannot see this defect class produces
exactly this artifact. Attempt three will converge on the same place unless the
harness asserts *that something happened* — a state change, a database write, an
effect — rather than that bytes matched.

## 3. Everything else measured

Produced by running the bot or compiling its manifests, not by reading docs.

| Measurement | Result | Method |
|---|---|---|
| Boots to verified | `verified: true`, **exit 0** | `SB_VERIFY_BOOT=true`, real Postgres |
| Goes online | gateway READY, **3 guilds**, RUNNING | live gateway connect |
| Dispatch targets | **1,327** | live boot log |
| Panels registered | **314** | live boot log |
| Buttons / selectors declared | **640 / 130** across 161 panels | compiled snapshot |
| Manifests loaded | **49 of 49**, unconditionally | `load_live_manifests()` returns |
| Subsystem selection | **none** — signature is `() -> list[object]`, no filter | live introspection |
| Runtime load/unload | **none** — zero hits for `unload`/`reload`/`remove_cog` in `sb/` | grep |
| Commands absent vs superbot | **17 of 368** | compiled-inventory diff |
| — real capability gap | **3**: `cog`, `loadall`, `unloadall` | — |
| — superseded | 2: `syncslash`, `syncs` | — |
| — aliases only | 12 (`diag`, `sysinfo`, `quicksetup`, `hilfe`, …) | verified each parent exists |
| Slash commands | **27** of 413 — the rest are prefix-only | live boot log |
| Panels with **no buttons at all** | **153 of 314 — 48%** | compiled snapshot (exact) |
| — of those, the `help` tree | **60 of 66 panels** | compiled snapshot (exact) |
| "not armed" terminals | **70** across 17 subsystems | grep of shipped copy |

### Two configurability gaps confirmed by execution

**No boot-time subsystem selection.** `load_live_manifests()` scans the package
directory and imports everything. All 14 game/economy subsystems load, always.
There is no config field for it — the entire surface is nine env fields.

**No runtime load/unload**, and it is deliberate. From `docs/decisions.md`:

> NOT ported (deliberate): cog / loadall / unloadall (extension management — no
> analog in the compiled architecture: subsystems are manifests, not
> runtime-loadable cogs)

Against a charter of *"the same functions with less noise"*, that is a scope
decision presented as an architectural necessity. superbot's configurability —
trim `INITIAL_EXTENSIONS`, `!cog load/unload/reload` live — is the property the
owner states he built the bot around.

**Cog routing is also unported.** The Access Map records its own routing axis as
`skipped` — *"cog routing not ported — setup-wizard section slug only."* Note
that superbot's routing is stored but **also never enforced**: its admission
resolver never imports `command_routing` either. Both codebases have the hole.

### The bootstrap gap — the owner's diagnosis, confirmed

Booting without `SB_INTENT_MSGCONTENT_OK` produced:

```
intent DEGRADE: message_content → prefix, fuzzy, triggers, nl_message, passive_onmessage not registered
message feed NOT armed: prefix class degraded (message_content unapproved)
```

**1,300 of 1,327 targets silently unreachable**, leaving 27 slash commands. The
only trace was one log line; in Discord the bot appears online and mostly inert
with no way to ask why.

superbot prevents exactly this. `bootstrap_access_cog` loads **first** by
explicit `INITIAL_EXTENSIONS` ordering, and its docstring states the guarantee:

> *"The admin escape hatches (`!force`, bootstrap commands for guild operators)
> are preserved — the prefix-only `!force` short-circuit is handled inline here,
> the bootstrap bypass is inside the resolver."*

Gates installed before anything registers, **plus a bypass so an operator is
never locked out by their own configuration.** superbot-next has neither. This is
a genuine port gap with no architectural excuse attached.

## 4. What holds up — do not throw this away

The rebuild's premise was not fantasy, and a post-mortem that concludes
"worthless" would discard real work:

- It **boots, connects, and serves**. Prefix, slash, component and modal
  surfaces all dispatched successfully with the owner driving.
- **640 real buttons** across 161 panels; the panel engine, component feed and
  modal band are live.
- Migrations, the outbox relay, the poll supervisor, workflow/audit seams, and
  the draft pipeline all ran clean, including a durable boot canary delivered on
  the first RUNNING tick.
- The **layered architecture** (spec/namespace → kernel → domain → adapters →
  app, with import-direction guards) is genuinely better-founded than superbot's
  accumulated patches. That was the point of the rebuild and it survived.

The defensible summary: **the code is better than one bad session suggested; the
verification method is what failed** — and § 4b is the largest thing that method
let through.

## 4b. The navigation graph — the product, and it was not ported

**This section replaces a wrong claim in the first version of this document**
(see § 7). That version reported the menu-versus-text ratio as *"inherited, not
introduced"* on a 17%-vs-21% comparison of how many **commands** build a view.

That measurement is exact and answers a question nobody has. **Nobody types
superbot's commands.** The owner's description of how the bot is actually used:

> *"every command is reachable and activated by a button, the only command
> anyone ever needs is `!help`, from there you can use every feature the bot
> ships, in seconds, always 2 taps away from any command"*

Confirmed from a screen recording of the live old bot (2026-08-05). Its
`!help` leads into panels that are **launchers**, not listings:

- **Blackjack** — eight buttons: Solo Free Play · Solo Bet · Challenge Player ·
  Tournament · Status · Rules · Help · Games.
- **Casino** — New Poker Table (primary), Roulette (disabled, honestly
  labelled), Help, overflow.
- **Server Stats** — **live computed values** (3 members, 16 text channels, 1
  voice, 5 roles) above an eleven-button grid: Settings · Server Management ·
  Channels · AI · Platform · Diagnostics · UX Lab · Logging · Reload All · Log
  Level · Server Stats.

The command surface is incidental. **The navigation graph is the product**, and
the correct measurement is reachability: can a user reach every feature by
clicking, from one entry point, in about two taps?

### Measured on the rebuild

| | Panels | With **zero** buttons |
|---|---|---|
| **All subsystems** | 314 | **153 — 48%** |
| **`help`** | 66 | **60 — 91%** |

Buttons that exist are counted generously here: a panel scores as "has buttons"
even if all of them are Back/Home navigation.

Where the button-less panels concentrate:

| Subsystem | Button-less / total |
|---|---|
| `help` | **60 / 66** |
| `ai` | 17 / 27 |
| `utility` | 9 / 10 |
| `creature` | 7 / 9 |
| `inventory` | 7 / 8 |
| `cleanup` | 5 / 12 |
| `economy` | 5 / 6 |
| `counters` | 3 / 3 |
| `fishing` | 3 / 14 |
| `setup` | 3 / 40 |

**The front door is 91% dead ends.** Navigating into a help category yields a
text list of command names with nothing to press — observed live, and visible in
the compiled snapshot as help sub-panels carrying `"actions": []` with a body of
text plus a provider reference.

### It is the same defect as the Cog Manager

`diagnostic/command_catalog.py` is one of the four `CAPTURE-WORLD LITERAL` files
(§ 1). The help pages render a **transcribed list of command names** — the
captured *text* of the old bot's help output — rather than a live route table
with launch buttons behind it.

The old panel's text and the new panel's text match byte-for-byte. One is a
menu; the other is a picture of a menu. **Golden parity cannot distinguish them,
and scored it 100%.**

So the Cog Manager was not an unlucky outlier the owner happened to open first.
The same transcription was applied to the bot's entire front door, which is why
the impression of pervasiveness formed immediately — the front door genuinely is
pervasive.

### Consequence for the rebuild

Milestone one is not "~15 working subsystems." It is **one working navigation
tree with ~15 subsystems hanging off it.** Build the graph first and the
cog-by-cog batches have somewhere to attach; build the subsystems first and
every one of them is unreachable until the graph exists.

A concrete acceptance test, and the one the golden harness could never express:
**from `!help`, every shipped feature is reachable by clicking, in two taps, with
no typed command.** That is a property of the route table, checkable
mechanically, and it fails today at 91% on the help tree alone.

## 5. The server-first shortlist — the owner's first milestone

The stated first goal is a bot that runs a server with **no game features**.
That maps onto roughly a fifth of the surface. Grouped by whether it serves
running a server:

**Keep — the operator spine (≈15)**

`admin` · `settings` · `setup` · `help` · `role` · `welcome` · `logging` ·
`moderation` · `automod` · `security` · `image_moderation` · `channel` ·
`server_management` · `counters` · `ticket` · `starboard` · `utility`
(`poll`/`remind`) · `platform` · `governance` · `kernel`

**Defer — light community, optional (≈6)**

`xp` · `karma` · `leaderboard` · `community` · `community_spotlight` ·
`counting`

**Exclude from milestone one (≈19)**

`casino` · `blackjack` · `mining` · `fishing` · `farm` · `creature` ·
`creature_battle` · `btd6` (×5 incl. `paragon`) · `projmoon` · `four_twenty` ·
`rps_tournament` · `deathmatch` · `economy` · `treasury` · `inventory` ·
`chain` · `games` · `proof_channel` · `hermes` · `ux_lab`

Three consequences worth planning around:

1. **Milestone one is ~15 subsystems, not 49.** That is a materially smaller
   target than either existing repo suggests.
2. **The excluded set is the argument for boot-time selection.** If subsystem
   selection exists from day one, "no game features" is a config value rather
   than a fork — and the game subsystems can land later without a migration.
3. **The navigation tree is milestone zero** (§ 4b). Subsystems built before the
   graph exists are unreachable by the only route real users take. Build the
   launcher first, hang the fifteen off it, and every later batch has an
   attachment point.

## 6. What to give the independent reviewers

The owner's plan is several sessions and several models reviewing both repos
independently. Three things make those reviews worth more than this one:

**Give each reviewer the boot recipe, not just the repo.** Reading produced three
wrong claims in this session (§ 7); booting settled all of them in minutes. The
recipe is in § 8 and takes about five minutes in a fresh container.

**Set the audit target explicitly.** The mechanical sweep worth running is:
*every module-level literal in `sb/domain/` that should be a runtime read.* The
four labelled cases are the seed, not the answer. The signature to hunt is a
constant describing **the program's own state** — inventories, rosters, counts,
status — as opposed to game data, which is legitimately constant. This cannot be
delegated to a grep alone, because the labelling is not guaranteed complete.

**Ask each reviewer the harness question separately.** Not "is the code good" but
*"what would this test suite fail to notice?"* The answer here — refusals,
photographs, and absences — was available from the harness design alone, without
reading a line of product code.

## 7. Where this session was wrong — so reviewers do not inherit it

Recorded because three of these were asserted to the owner before being checked,
and each was caught by him rather than by this session.

| Claim | Reality | Cause |
|---|---|---|
| "superbot cannot cleanly disable cogs" | It can — trim `INITIAL_EXTENSIONS`, plus `!cog load/unload/reload` live | Read the routing policy, missed the extension mechanism |
| "superbot-next's boot gate would reject a subset" | Leg A recompiles the package independently of what loaded; **leg B** is the constraint, and for a different reason | Reasoned from a docstring instead of running `gate_recompile` |
| "The token in the environment is the production identity" | **False.** Live worker = bot `1403818430758654132`; the environment holds `1298426054636994611` (the test app) | Inferred from the variable *name*; the repo's own testing ledger said otherwise |
| "314 panels, zero components" | **640 buttons across 161 panels** | Counted a `components` key that does not exist; the fields are `actions`/`selectors` |
| "It's a faithful clone, 365 of 368" | True of command *names*, and it missed that whole classes can be silently unreachable | Counted the wrong thing |
| **"The menu-vs-text ratio is inherited, not introduced" (17% vs ~21%)** | **Wrong, and it dismissed the owner's central complaint.** The ratio measured how many *commands* build a view, in a bot whose commands nobody types. The real measure is reachability: the `help` tree is **60 of 66 panels with zero buttons**. See § 4b | Measured a precise, exact, reproducible answer to a question nobody had — then reported it as reassurance |

The root cause is uniform and worth stating once: **this session read the code
and skipped both repositories' required boot files.** `superbot-next`'s
orientation names `docs/status/testing-report-2026-07-09.md` as *"the
live-testing ledger — what has actually been driven in a real guild, band by
band"* — the exact question being inferred around for an hour. It also
identifies the environment token as the test app, which would have prevented the
worst claim above.

Additionally, the owner's first review session ran against a bot booted **without
privileged intents** and against a **40-minute-old empty database**. Both were
this session's setup errors, and both made the bot look considerably worse than
it is. Any impression formed in that window should be discounted, not carried
into the rebuild decision.

## 8. Reproduction recipe

Roughly five minutes in a clean container, no Discord token needed for the
offline half:

```bash
python3.11 -m venv .venv
.venv/bin/pip install --require-hashes -r requirements.lock
# local Postgres 16, trust auth, any port
SB_VERIFY_BOOT=true SB_DATA_PLANE=test DATABASE_URL=postgresql://… \
  .venv/bin/python -m sb.app.verify_boot     # → {"verified": true}, exit 0
```

To go online, add a **test** bot token plus:

```
SB_INTENT_MSGCONTENT_OK=true   # without this, prefix commands are silently dead
SB_INTENT_MEMBERS_OK=true      # without this, join/leave events never fire
HEALTH_HOST=0.0.0.0            # the default '::' fails where IPv6 is absent
SB_DATA_PLANE=test
```

Set `guild_command_access_policy.mode = 'all_channels'` per guild, or commands
answer nothing on a fresh database.

## 9. Honest nulls

- **Completeness of the literal audit.** Four labelled instances found; the
  labelling is not guaranteed exhaustive. § 6 names the sweep that would settle
  it. It was not run here.
- **The reachability figures count declared buttons, not working ones.** A panel
  with buttons that all route to "not armed" terminals still scores as having
  buttons, so **48% / 91% are floors** — the true dead-end rate is higher. A
  click-through census would settle it and was not run.
- **The two-tap property was not measured**, only the zero-button rate. Proving
  or refuting "every feature is two taps from `!help`" needs the route table
  walked as a graph, which is the acceptance test proposed in § 4b, not a
  result reported here.
- **The 70 "not armed" terminals** is a grep of shipped refusal copy, not a
  click-through census. The true count of dead-ended surfaces may differ.
- **Nothing below band 1 was exercised live in this session.** The owner drove
  help, settings and the cog manager; 46 subsystems were never opened.
- **Whether any Tier-1 subsystem behaves correctly on a guild that has never run
  the setup wizard** is untested — the one live session ran against an empty
  database.
