# The successor's architecture

> **Status:** `plan` — authoritative for the successor bot's composition,
> ownership boundaries, extension contract, interaction pipeline, navigation,
> config, persistence, AI, observability and deployment isolation, until the
> successor's own repository exists and carries them. It is **not** authoritative
> for product scope ([`05-product-definition.md`](05-product-definition.md)), for
> what each feature must supply ([`07-feature-contract.md`](07-feature-contract.md)),
> or for the proof layers ([`08-verification.md`](08-verification.md)).

## 0 · How this file was written, and the rule it applies to itself

**Not derived from `superbot-next`'s layer tree.** The tree is not evidence:
I-22 measured its clean DAG as an artifact of a module-level census — 268 of 296
cross-subsystem `sb.domain` imports (90.5 %) sit inside function bodies, and all
8 mutual subsystem pairs live there, 0 at module level. A shape that survives
only the measurement that cannot see its violations is not a starting point.

So the design below starts from the four constraints that are measured, and
everything else is derived from them:

| constraint | source |
|---|---|
| **C1 · A guard is only as good as its population.** Every registry, graph and surface the successor builds is something a gate will one day have to count. | [`04-root-cause.md`](04-root-cause.md) § 2.4 · [`08-verification.md`](08-verification.md) § 1 |
| **C2 · An out-of-tree module must be able to own data**, or cog portability fails for the feature classes worth porting (`stores` fences out 29 of `superbot-next`'s own 49 subsystems). | I-10 · OD-19 |
| **C3 · AI supplies judgement, deterministic code supplies authority** — through a typed schema-validated verdict, never parsed prose. | [the 2026-09-04 AI-authority decision](run/in-flight-direction.md) |
| **C4 · A feature must cost a local change**, or the exception files grow with the feature set. | [`04-root-cause.md`](04-root-cause.md) § 1.2 |

**The rule this file applies to every abstraction it proposes**, stated once and
then applied inline as `**2nd:** … · **prevents:** …`:

> An abstraction ships only if it has a **named second consumer** and a **named
> measured failure it prevents.** One consumer means the abstraction is the
> feature wearing a costume. No named failure means it is taste.

§ 12 is the consolidated ledger, and § 13 is what the rule **cut** — six
abstractions both repos built that the successor does not.

**Citation marking.** A figure this session re-derived against the pinned clones
is stated bare with its `I-` id, or marked *(read at the pin)* where I opened the
file directly while writing this. A figure carried from a fleet lane is marked
**`lane-claimed`** inline at the number, with its row id.

---

## 1 · The shape: four rings, and one of them is a flat set

```
app/            the composition root — one boot sequence, executed by tests
core/           the framework: ports, registries, the pipeline. No product knowledge.
adapters/       the only place the outside world is named (discord, postgres, llm, http)
modules/<name>/ features. A flat set. Every one has the same shape as an
                out-of-tree distribution, because it loads through the same loader.
```

**Four rules make the shape mean something.** Each is enforced by one whole-AST
guard, and each names the failure it prevents:

1. **`core/` imports nothing from `modules/` or `adapters/`.** It declares ports;
   `app/` binds them. *Prevents:* the transitive-closure trap — `superbot`'s
   `core.runtime → core.resources → governance → …` chain means the most portable
   cog sampled still drags governance and env config out with it (R3-D4,
   `lane-claimed`).
2. **`modules/<a>` never imports `modules/<b>`, at any depth, in any position.**
   Cross-module needs go through declared capability refs the compiler resolves.
   *Prevents:* `superbot`'s 128 module-level `from cogs.<x>` statements across 51
   files inside `cogs/` (I-17), legal under its own layer rule because
   `layers.yaml` lists `cogs` in `cogs.may_import` — the coupling ceiling in
   exactly the layer OD-19 wants portable.
3. **`import discord` appears only under `adapters/discord/`.** The fence counts
   module-level, function-body, `TYPE_CHECKING` **and** `importlib.import_module`
   by name. *Prevents:* the two measured bypasses — `superbot`'s `layers.yaml`
   never sees function-body imports unless CI passes `--report-lazy-imports`,
   which raises findings from 1 to 137 and which CI never passes (R3-D2,
   `lane-claimed`); and `superbot-next`'s `check_no_skip`, which is stricter on
   the three static forms and returns EXIT=0 on the dynamic one (M8-D09,
   `lane-claimed`).
4. **The import guard fails on cycles over the union graph**, function-body edges
   counted as real edges. *Prevents:* I-22 in one line — *"clean architecture"*
   meaning *"we moved the imports."*

**`modules/` is flat on purpose.** There is no `domain/`-vs-`kernel/` gradient to
argue about at review time, and no place for a module to acquire privilege by
sitting higher in a tree. A module is a directory with a fixed interior:

```
modules/starboard/
  manifest.py      THE declaration — commands, routes, settings, stores, ops,
                   events, capabilities, ai_tools, setup_sections, invariants
  ops.py           typed operations (the only mutation entry points)
  store.py         data access; every function takes `conn`
  logic.py         pure functions — no framework imports, no Discord, no DB
  ui.py            panel bodies: data in, RenderedView out
  migrations/      its own ladder + checksums.json, into schema mod_starboard
  tests/
```

**2nd consumer of the fixed interior:** the out-of-tree loader (§ 4) reads exactly
this shape from an installed distribution, and `check_module_portability` walks
it for in-tree modules. **Prevents:** the facet fence — a contract whose in-tree
path has privileges the out-of-tree path lacks ends where `superbot-next`'s did,
with 29 of 49 of its own subsystems ineligible (I-10).

---

## 2 · The composition root

**One file, one function, and the test suite executes it.**

`superbot-next`'s `run_app` is 624 lines that no test executes; the 6 test
references use `inspect.getsource` and assert on source-text substrings, 9 such
call sites across 3 files (M8-D03, `lane-claimed`, and F-D07 counts the same 9).
An assertion over source text is not a population — it is a photograph of one.

**Boot sequence, ordered. Every step has an observable outcome, and steps 5 and 8
are gates that stop the boot.**

| # | step | outcome |
|---|---|---|
| 0 | load typed config | missing required var → abort naming **the variable**, before any connection |
| 1 | select the **profile** (§ 6) | the module set for this process, named |
| 2 | import each module's `manifest.py` | declaration only — a manifest import that touches the DB, the network or a global registry is a compile error |
| 3 | **compile** the declarations | one pass builds the route graph, mints component ids, and derives the op registry, settings grammar, store registry, tool registry, event subscriptions and command tree |
| 4 | apply per-module migrations | each ladder into its own schema; boot-time checksum verify |
| 5 | **compile-time gates** | exactly one root route · no orphan route · no `custom_id` collision · slash budget 100/25/1-nest · no namespace collision · every store declares `data_class`/retention/erasure · every op declares `authority_ref` and `audit_verb` |
| 6 | bind adapters to ports | Discord, Postgres, providers, health, metrics sink |
| 7 | publish the command tree to Discord and **read back what registered** | the count is a measurement, not an intention |
| 8 | **assert the surface floor** (§ 10) | commands published ≥ floor · routes reachable from root ≥ floor · modules loaded == profile. A breach is a failed boot |
| 9 | post the out-of-band startup summary | before READY, so a boot that dies later still produced an artifact — `superbot`'s pattern (R4-S03, `lane-claimed`) |
| 10 | start the scheduler, subscribe events, flip readiness | readiness is a decision table with a named reason per row and is DB-aware (R4-S08, `lane-claimed`); it cannot flip green before step 8 passed |

**2nd consumer of the boot sequence:** the headless composition-root test drives
it end to end with the Discord adapter bound to an in-process fake **at the
transport seam** — not with a substitute renderer (§ 3). **Prevents:** the
measured pair — a required gate whose `install_panel_runtime` returns before
installing the presenter when `discord` is unimportable, so its four presenter
tests skip and the job is `19 passed, 4 skipped`, EXIT=0 (F-D09, `lane-claimed`);
and `verify_boot` executing 3 of `main.py`'s 18 numbered steps while defining the
word "verified" for the weekly restore workflow (M8-D02, `lane-claimed`).

**Step 7 is not a formality.** `sb/app/main.py:616` hardcodes
`sync_remote(bot, committed, enabled=False)`, so that composition root publishes
no slash command at all while `/ready` answers 200 (I-19). Reading back what
registered is the difference between a bot that is online and a bot that says so.

---

## 3 · The Discord adapter — one renderer, no twin

**The single most consequential rule in this file, and it is one sentence:**

> There is exactly one renderer. A second serializer written so that tests can
> run is forbidden; if a test cannot reach the shipping renderer, the seam is
> wrong and the seam is what gets fixed.

The measured failure it prevents is the acceptance oracle's
([`08-verification.md`](08-verification.md) § 3b): every "actual" wire byte in
533 green goldens comes from `rendered_panel_payload()`
(`sb/adapters/parity/transport.py:242`), a hand-written twin imported by nothing
but two parity unit tests, while production installs `DiscordPanelPresenter`
(`sb/app/panel_host.py:66`) — which is on **neither** side of the diff. The
oracle compared real discord.py to a model of discord.py, forever, greenly.

**The seam that makes one renderer testable.** The framework produces a
`RenderedView` — a value object: embed fields, component rows, each component
carrying its minted `custom_id` and its route or op ref. `adapters/discord/`
turns a `RenderedView` into discord.py objects and posts them. Tests drive the
**same** renderer and the **same** adapter, with the HTTP transport faked below
it. That is the shape `superbot-next`'s *expected* side already had, correctly:
`parity/harness/fake_http.py` boots the real bot and fakes discord.py's two
transport seams (`ConnectionState.http` and the webhook `async_context`), so real
serialization runs and only the network is absent. The successor uses that shape
on **both** sides, because there are no longer two sides.

**2nd consumer:** the rendering-stability goldens and the journey layer both drive
it, so a change in either is visible to the other. **Prevents:** 533/533 over a
serializer production does not install.

**The adapter's other three jobs**, each with its own second consumer:

- **Egress containment.** One module constructs `AllowedMentions`; untrusted text
  gets `AllowedMentions.none()` plus markdown escaping. **2nd:** the AI reply path
  uses the same port as the button path. **Prevents:** `superbot`'s live
  mass-ping vector — 915 `.send(` call sites against 18 occurrences of
  `allowed_mentions` in 5 files (B-D06, `lane-claimed`).
- **Component identity.** One static mint table with a **raising** collision
  fence. Read at the pin: `sb/kernel/panels/registry.py:79-87` raises
  `PanelCompileError("custom_id_collision")` when an id is already bound to a
  different binding, and `:88-97` raises `hub_redefined` on reassignment. **2nd:**
  restart-restore of persistent panels resolves against the same table the
  journey tests click. **Prevents:** `superbot`'s router, which logs *"Overwriting
  existing handler for prefix"* and silently replaces the entry, against 280
  hand-written `custom_id=` literals in 86 files (B-D09, `lane-claimed`).
- **Answering.** Every terminal state of the pipeline produces a user-visible
  response — including denial, including an unrecognised token. **Prevents:** the
  regression a member notices first: `!helpp` and `!seting` produce total silence
  in `superbot-next`, while `superbot`'s composition root carries a comment naming
  the suppressed-reply gate as *"the root cause of the 'command vanished' UX"*
  (read at the pin, `disbot/bot1.py:540-547`; CHALLENGE D, `lane-claimed`).

---

## 4 · The extension boundary

This is where OD-19 is won or lost, and the evidence is unusually good: **the
thing being asked for has already happened 54 times.** 54 `disbot`↔`sb` file pairs
score above 0.55 similarity, 8 at ≥ 0.90, and one is byte-identical —
`disbot/utils/mining/capacity.py` and `sb/domain/mining/capacity.py` share md5
`64f1665a9fb83a940d95eca5b9492bf2` (I-21). Portability across these two
architectures is demonstrated. What blocked it as a *contract* is a fence, and
the fence has a stated cause.

### 4.1 · Why the fence exists, and the structural fact under it

`sb/app/plugin_host.py:78-83`, read at the pin:

```python
ALLOWED_FACETS: tuple[str, ...] = (
    "commands", "panels", "settings", "events", "capabilities",
)
HOST_ONLY_FACETS: tuple[str, ...] = (
    "stores", "data_invariants", "wizard_sections",
)
```

The docstring's reason is *"migrations, S12 money lanes, and the G-19 setup
registry have no out-of-tree lane yet."* That is honest, and the structural cause
is one design decision, visible in the checker: `tools/check_migrations.py:4-16`
(read at the pin) requires versions *"unique AND contiguous from 0001"* across
one global directory — **57 `.sql` files plus one `checksums.json`** (counted at
the pin). An out-of-tree module cannot claim a number in a contiguous global
sequence it does not own. The fence follows from the ladder.

And the second structural fact, **measured by this session**: `CREATE SCHEMA`
appears **0 times** across `superbot-next`'s 57 migrations and `superbot`'s 104,
and **0 files** in either set mention `search_path`. Both bots put every table in
`public`. So there is no namespace for a module's data to be its own — not
because it was rejected, but because it was never needed while everything was
in-tree.

### 4.2 · The contract: a module owns its data

> **An out-of-tree module ships migrations, owns a schema, declares its
> invariants, and contributes a setup section. The host owns the pool, the
> transaction, the audit table, the route root and the command budget.**

Concretely, an installed distribution may declare **every facet an in-tree module
may declare** — there is no host-only list — under six host-enforced conditions:

| the module declares | the host enforces |
|---|---|
| `migrations/` — its own ladder, contiguous **within itself**, with its own `checksums.json` | the host creates schema `mod_<name>`, applies the ladder inside it with `search_path` set, and verifies checksums at boot. Cross-schema DDL in a module migration is rejected before it runs |
| `stores` — each with `data_class`, retention, `erasure_ref` | the erasure walk and the guild-teardown walk (§ 8) enumerate the registry, so a new store is covered with no edit anywhere |
| `invariants` — assertions over its own tables | run by the host on a schedule and at boot; a failing invariant marks the module degraded, never the process |
| `setup_sections` — steps in the first-run journey | the host owns the wizard's order, resume and authority; the module owns the step's copy and its typed apply operation |
| `ops` — typed operations, each with `authority_ref` and `audit_verb` | the host's engine runs them; a module cannot open its own transaction |
| the manifest hash, pinned in the lockfile | hash-pin enforcement is `superbot-next`'s and it fires both ways — zeroing a hash and deleting a pin each red (M8-S07, `lane-claimed`) |

**2nd consumer of the whole contract:** the in-tree modules. They load through the
same loader, under the same rules, with the same closure restriction — which is
what makes `check_module_portability` a real gate rather than a promise, and what
makes every in-tree module an out-of-tree candidate by construction.
**Prevents:** I-10 — an extension mechanism that serves the stateless two-fifths
of its own product and precisely not the class the owner wants to port.

### 4.3 · Fault isolation, and the interlock that stops it hiding a missing bot

`superbot` isolates: 59 of 59 extensions load inside their own `try/except`, the
failure is recorded, the loop continues, and the affected subsystems are demoted
(read at the pin, `disbot/bot1.py:721-738`). `superbot-next` aborts: any single
plugin violation collects into `_fail_startup('plugin_gate')` (R3-D6,
`lane-claimed`).

The successor isolates — **and** the surface floor (§ 10) catches what isolation
would otherwise hide. A module that fails to load registers no routes, publishes
no commands, and is therefore missing from step 8's counts; the floor breach
fails the boot. So a broken module degrades to *this module is unavailable and
says so*, and a **profile** of broken modules cannot silently become a bot that
does nothing. **Prevents:** both halves — a whole-boot abort for one bad plugin,
and the do-nothing bot that CHALLENGE F built on paper and scored 7/7 green
(`lane-claimed`).

### 4.4 · Adapting an existing `superbot` cog — the concrete recipe

Worked on `starboard`, chosen because it is the hardest honest case: a live
production cog with three dedicated tables, two migrations and its own config
panel, which is **absent from `SUBSYSTEMS` entirely**, so `!settings` cannot list
it and its only route is the undiscoverable `!starboard` command (R3-D1,
`lane-claimed`).

| # | step | cost |
|---|---|---|
| 1 | copy `logic.py` — the pure functions — unchanged | **zero.** This is the byte-identical case (I-21) |
| 2 | `@commands.command` → a `commands` row in `manifest.py`; the body becomes a handler taking a typed request and returning a typed result | mechanical, per command |
| 3 | `@admin_or_owner` → `authority_ref` on the **operation**, not the surface | mechanical, and it deletes code — `superbot` carries 166 authority decorators in `cogs`, 3 in `views`, 8 in `core`, **0 in `services`**, where the 190 mutation modules live (B-D07, `lane-claimed`) |
| 4 | direct `pool.execute` → store functions taking `conn`, called from a typed op | the real work. This is the *"slightly alter"* OD-19 allows |
| 5 | `NNN_starboard.sql` → `modules/starboard/migrations/0001_*.sql`, renumbered from 0001 within the module, tables unqualified and created inside `mod_starboard` | mechanical; renumbering is safe **because the ladder is now the module's own** |
| 6 | settings rows declared in the manifest → they render in the settings hub with no UI code | this already worked in `superbot` — `SubsystemSchema` has 19 consumers, one per cog (R3-S3, `lane-claimed`) |
| 7 | the config panel becomes a **route with a declared parent** | this is the step that fixes starboard's actual defect, and § 5 makes it unskippable |
| 8 | declare `data_class`, retention and `erasure_ref` per store | one line per store; the erasure and teardown walks then cover it with no edit |

**What is *not* cheap, stated plainly so nobody plans around a fiction:** a cog
that imports another cog at module level (128 statements across 51 files, I-17)
must have that edge resolved first — into `logic.py`, into the host, or into a
declared capability ref. And a cog whose closure pulls governance and env config
(R3-D4's observed traceback, `lane-claimed`) loses that closure at step 4, which
is most of the work. The honest claim is: **steps 1, 2, 3, 5, 6 and 8 are
mechanical; step 4 is the port; step 7 is an improvement the old cog never had.**

### 4.5 · Runtime hot-load: **no.** Runtime disable: **yes, and it is the same lever as visibility.**

The operational need is real and is measured on both sides: `superbot` has
audited runtime load/unload/reload with a `_PROTECTED_COGS` guard reachable from
two surfaces (R3-S2, `lane-claimed`); `superbot-next` ported the Cog Manager as a
dead end whose Load/Unload/Reload buttons are wired to a handler stating the
capability does not exist, with the select and pagination still live so the
surface looks functional (R3-D8, `lane-claimed`).

The successor builds the **incident lever**, not the **code loader**:

- **Disable** flips one governance record. The router already reads it per
  interaction, the renderer already reads it to hide the module's routes, and the
  scheduler reads it before running any of that module's due jobs — so a runaway
  background loop stops too, which is the one thing a governance flag would
  otherwise miss. Audited, per-guild or global, reversible, effective in seconds.
- **Hot-loading new code** buys only *deploy without restart*, and costs a second
  code path that cannot be covered by the boot gates (§ 2 steps 5 and 8), by the
  migration ladder, or by the route graph's construction-time reachability. A
  restart on the host is seconds.

**2nd consumer of the disable lever:** OD-D's optional-module set — the same
switch is how a module is *not shipped to a guild*, so the incident path and the
product path are one mechanism. **Prevents:** two code-loading paths, only one of
which any gate can see.

**Flagged, not asked:** lane R3 dispositioned runtime load/unload `OWNER_DECISION`.
This file decides it, per `docs/intent.md` § 6 (a reversible implementation choice
is *decide and flag*). **The cost of being wrong is one slice**: if the owner
finds himself wanting `!cog unload` for a case disable does not cover, the loader
is additive and nothing above has to be undone.

---

## 5 · Navigation — one route graph, and help is a projection of it

**The finding this section answers is not a wiring gap.** `superbot-next` wires
314 panels with **200** downward edges, where a 314-node graph needs ≥ 313 merely
to be a connected tree; from `help.*` roots max depth is **zero**; `setup` is 39
of 40 panels unreachable; adding Back/Home up-links raises edges to 278 and
reachability by **zero** panels (I-13). And `superbot` reaches setup only through
an ephemeral out-of-graph launcher message with no route back, with
`_repost_launcher` as the tell that someone met this and shipped a way to re-post
the message rather than a route into the flow (I-13). **Setup was never a
first-class destination in either graph.**

### 5.1 · The model

- A **route** is a destination: a panel, a wizard step, a command result page.
- Every route is registered with a **parent** — or with `root=True`, and the
  compiler asserts `count(root) == 1`.
- An **edge** is a declared transition: a button, a select option, a command
  entry, a wizard next-step.
- **Help is generated by walking the graph from the root.** There is no help
  corpus, no help subsystem with its own pages, and no second list of what the
  bot can do. A route's help entry is its label, its authority tier and its
  children — read off the graph at render time.

### 5.2 · Reachability is guaranteed, not tested

The framework makes an orphan **unconstructible**: `add_route()` requires a
parent, so there is no state of the system in which a route exists outside the
graph. What the gate then checks is not *existence* but the two things
construction cannot guarantee:

1. **Budget** — every enabled route is reachable from the root within the
   promised interaction budget, at the guild-visibility settings the route ships
   with. Per-guild visibility must be modelled, or the gate scores a
   correctly-hidden subsystem as unreachable and trains its readers to ignore it
   (I-14).
2. **Population** — the walk declares its population (the graph the composition
   root built), asserts it against a committed floor, and walks the **rendered**
   view rather than a model of the registry
   ([`08-verification.md`](08-verification.md) § 1).

**2nd consumer of the route graph:** the help generator, the reachability gate,
the slash-tree projection (§ 5.3) and the boot surface floor (§ 10) all read the
same object. **Prevents:** the two measured failures at once — a navigation golden
green over a registry its own `autouse` conftest clears, whose `register_hub()`
has 1 definition and 0 production callers so its root set is empty in a booted
process too (I-2, I-16); and a hub-child renderer where the shared discovery seam
is 19 for 19 and hand-rolling is 8 for 15, with `ModPanelView`'s seven buttons
every one an action and none a route (I-14).

That last measurement is the argument for making rendering a framework property
rather than a hub author's job: **`admin` hand-rolls and gets 6 of 6 right.**
Hand-rolling is not wrong, it is *unguaranteed* — and in this family, given time,
unguaranteed and absent have the same failure rate.

### 5.3 · Setup is a route

Not a launcher message. `setup` is a child of the root with the same
reachability guarantee as every other route, its wizard sections contributed by
modules (§ 4.2), resumable, and reachable after the first day. The join-time
launcher message stays — it is good product — but it is now an *additional* entry
edge into a destination that exists in the graph, not the only way in.

### 5.4 · The invocation surface

The route graph projects to **one grouped slash tree**; prefix commands are
declared aliases whose loss degrades nothing. The cap budget (100 top-level /
25 per group / one level of nesting) is a compile-time gate at § 2 step 5 —
`superbot-next` already has these as executable constants rather than prose
(C-S03, `lane-claimed`), and `superbot` already shipped the pattern once, at the
owner's request, collapsing five prefix groups into a single `/btd6` tree
(C-S05, `lane-claimed`). The product argument for it belongs to
[`05-product-definition.md`](05-product-definition.md); the architectural
consequence is only this: **the projection is derived, so there is no second
command list to drift.**

---

## 6 · Boot-time feature profiles

A **profile** is a named module set, declared in the typed config. The process
loads exactly that set. Nothing else selects modules — no env flag per module, no
runtime filter, no partial import.

- `full` — everything the repo ships.
- `test` — the slice under development, for the test guild and test app.
- named profiles as needed (the `spider-bot`-scale case: moderation + utility).

**2nd consumer:** the reachability gate and the surface floor run **per profile**,
so "reachable" and "online" are asserted for each shipped configuration rather
than for the full set only. **Prevents:** R3-D7 (`lane-claimed`) — 49 manifests
loading unconditionally with no flag, env var or config file that will run a
subset, so a second small deployment means deleting manifest modules.

Profiles are boot-time by construction: a profile change is a restart, which is
the same posture as § 4.5.

---

## 7 · Ownership — one owner per kind of state

**The rule:** every registry in the system is **derived** from module manifests at
compile time. A registry with an `add()` reachable outside the compile pass is a
build error. This is C4's mechanism: one declaration, many derived registries,
and therefore nothing to keep in sync and no exception file to grow.

| kind of state | the one owner | second reader | the duplicate this forbids |
|---|---|---|---|
| process / deploy config | `core/config` typed spec | the deployment-readiness verdict (§ 11) | `os.getenv` anywhere else |
| per-guild settings | the module's `settings` declaration → one settings store | the setup wizard renders them with no UI code | a per-module settings table |
| per-guild visibility | one governance record | renderer · reachability gate · scheduler · the disable lever (§ 4.5) | a second enable flag |
| the route graph | the route registry, built at boot | help generator · slash projection · surface floor | a help corpus |
| component identity | one static mint table with a raising collision fence | restart-restore · journey tests | hand-written `custom_id` literals |
| domain rows | the module's store, `conn`-taking | the erasure walk · the teardown walk | raw pool access outside `core/db` |
| mutation authority | the operation's `authority_ref` | every surface inherits it; the audit row records the tier | per-surface decorators |
| audit | one writer, inside the operation's transaction | the case record · the AI decision log | hand-written audit calls |
| schema version | the module's own ladder + checksums | boot verify · CI checksum gate | a global contiguous ladder |
| background work | the scheduler's due queue | module disable · retention and erasure jobs | ad-hoc `asyncio.sleep` |

**The failures each column-4 entry prevents, measured:**

- **The parent link stored twice.** `superbot` keeps it in `subsystem_registry.py`
  and `hub_registry.py`, which is why a bidirectional-drift checker had to exist
  ([`04-root-cause.md`](04-root-cause.md) § 1.2). Derived registries have no
  second copy to drift.
- **The hand-maintained roster.** `SUBSCRIBE_ROSTER` is a 6-entry tuple whose
  completeness is enforced by nothing — correct today, and a 7th subscriber
  omitted from it passes every gate (M8-D05, `lane-claimed`).
- **The registry with no key.** `superbot`'s `SUBSYSTEMS` holds 43 real keys
  against 59 cog modules; 16 have no same-named key, starboard among them, so
  governance has no policy row to resolve for them (R3-D10, `lane-claimed`).
- **Authority on the surface.** 166 decorators in `cogs`, 0 in the 190 `services`
  modules that hold the mutations (B-D07, `lane-claimed`).
- **Audit by hand.** 49 `emit_audit_action(` call sites across 27 files in
  `superbot` (I-18) versus one central writer in `superbot-next` (M9-S03,
  `lane-claimed`; the field is required with no default — read at the pin,
  `sb/kernel/workflow/spec.py:121-131`, `audit_verb: str` inside the
  *"required (no default)"* block).

---

## 8 · Persistence

**One pool. One transaction owner. One write path per kind of state.**

- **Store functions take `conn`.** They cannot be called without a handle the
  engine owns, which makes "every mutation is inside a typed operation" a type
  fact rather than a convention. `superbot-next` already does this in at least
  one domain (B-S12, `lane-claimed`); the successor makes it the only shape, with
  an AST gate whose population is *every function in every `store.py`*.
- **Per-module ladders into `mod_<name>` schemas** (§ 4.2). The host applies them
  in dependency order and verifies checksums at boot — `superbot-next`'s
  immutability gate is the donor and it is enforced twice, in CI and at boot
  (M10-S2, `lane-claimed`; the CI half read at the pin,
  `tools/check_migrations.py:4-16`).
- **Guild teardown and member erasure are the same walk over the store
  registry.** `superbot-next`'s erasure executor already enumerates the registered
  inventory rather than a hand list, and its docstring says why: *"Completeness is
  STRUCTURAL, not audited by inspection"* (read at the pin,
  `sb/kernel/privacy/erasure.py:1-25`). **Prevents:** `superbot`'s 31
  `_teardown_*` helpers against 84 guild-scoped columns, with staged setup drafts
  surviving a guild leaving and being re-read on re-invite (B-D08, M1-D01, both
  `lane-claimed`).
  **And the caveat that comes with the donor:** the declaration is complete and
  the execution is not — 0 of 48 distinct `erasure_ref` names are registered op
  keys, and 6 do not resolve at all (B-D01, `lane-claimed`). So the successor
  takes the *walk* and the *registry*, and the erasure gate asserts that every
  `erasure_ref` resolves to a registered op — population: the store registry,
  floor: its own size.
- **Session identity is a database constraint, not a process dict.** A `UNIQUE`
  on (user, channel, module) with `INSERT … ON CONFLICT … RETURNING` survives the
  restart that destroys an in-memory lock — `superbot`'s pattern (M6-S2,
  `lane-claimed`), and `superbot-next` has no equivalent to port.
- **Money and other conditional writes use one primitive**: a single conditional
  `UPDATE … WHERE balance >= n … RETURNING`. **2nd consumer:** it is reused seven
  times in `superbot` already (M6-S3, `lane-claimed`). **Prevents:** the
  read-then-write race still live in `transfer()`, the actual `$pay` path, which
  the codebase's own docstrings claim was eliminated (M6-D2, `lane-claimed`).

---

## 9 · The deterministic interaction pipeline

[The 2026-09-04 AI-authority decision](run/in-flight-direction.md) in an ordered flow. **One entry point.** Every surface — slash,
component, modal, autocomplete, prefix alias, scheduled job, AI-initiated action —
arrives at step 2 and takes the same path from there. `superbot-next` built this
and its own docstring states the order (read at the pin,
`sb/kernel/interaction/resolve.py:4`: *"admission → authority (K6) → validate →
cooldown → [ACK] → audit"*); the successor adds C3's judgement segment and the
effect assertion at the end.

```
 0  INGRESS            adapters/discord — the only place a discord.py object exists
 1  IDENTIFY           surface + target → a RouteRef or an OpRef in the compiled graph
                       (an unknown token resolves to the not-found route — never silence)
 2  ADMISSION          draining · guild enabled · module enabled · channel policy
                       a denial is an ANSWER, with the resolver's own reason shown
 3  AUTHORITY          resolve_authority(op.authority_ref) — the OPERATION's tier,
                       never the surface's; resolved once, before any work
 4  VALIDATE           typed args parsed into the operation's typed input
 5  COOLDOWN           charged before the ack, refunded on transient failure
 6  ACK                defer mode derived from the SURFACE, not the author
                       (the 3-second rule is the one platform constraint no
                        Discord release will relax — C-S01, lane-claimed)
─── everything above is deterministic and always runs ────────────────────────
 7  PRE-CHECK          the deterministic rules for this route. If they settle it,
                       the AI is never called. This is the default path.
 8  AI ANALYSIS        only if (7) did not settle it AND the route declares an
                       ai_ref. Input is redacted and containment-wrapped
 9  TYPED VERDICT      schema-validated. Invalid, incomplete, timed out or
                       degraded → NO automatic action; (7)'s outcome stands and
                       the degradation is recorded (§ 10)
10  POLICY ENGINE      verdict → proposed operation, through a deterministic
                       table. Free-form prose is never parsed into an action
11  RISK / MODE GATE   (risk tier × authority × mode) → EXECUTE | PREVIEW | DENY
                       modes: shadow (record, act never) · preview (human confirms)
                       · auto (low-risk reversible only, per OD-F's default)
─── from here the AI path and the button path are the same code ──────────────
12  TYPED OPERATION    the one mutation seam; one transaction; the module's
                       store functions called with its conn
13  EFFECT + AUDIT     the state change and the audit row commit together;
                       a case record is opened for anything a human may review
14  RENDER             the route the operation declares as its result node
15  OBSERVE            counters and trace keyed to the route id (§ 10)
```

**Six properties this ordering buys, each answering a measured failure:**

1. **The AI cannot widen authority.** Step 3 ran before step 8 existed. An
   AI-proposed operation is subject to the same `authority_ref` a button is.
   *Prevents:* `superbot-next`'s scope lattice, real and tested, never fed from a
   live user's Discord permissions, with every production call site at the USER
   floor (M10-D3, `lane-claimed`).
2. **Invalid model output is inert.** Step 9 has one failure mode and it is *no
   automatic action*, not a retry that eventually parses.
3. **Shadow mode is a mode of the same pipeline**, not a parallel path — so the
   evidence shadow mode collects is evidence about the code that would have run.
4. **Confirmation is not a separate abstraction.** Preview *is* the risk gate at
   a tier. *Prevents:* `superbot-next`'s `ConfirmationSpec`, carried by 0 of 175
   registered ops, making the `ConfirmRequired` branch dead code (B-D05,
   `lane-claimed`); and `superbot`'s provisioning confirmation gate, bypassed at
   3 of 3 production call sites with `confirmed=True` hardcoded (M1-D02,
   `lane-claimed`).
5. **There is no second write path.** An AI action, a button, a wizard apply and a
   scheduled job all reach step 12. **2nd consumer** of the typed operation is
   therefore structural rather than nominal.
6. **Nothing exits silently.** Steps 2, 9 and 11 all produce a response.

**The AI's write surface starts where production already proved it works:**
`superbot`'s catalogue is 36 tools, 35 read-only and exactly one write —
`open_support_ticket`, which goes through the audited mutation seam (I-11). That
is [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s contract, shipped, in production, today. The successor's registry
is `superbot-next`'s open per-module one (so a module brings its own tools —
`superbot` has **no** per-cog registration hook at all, M4-D6, `lane-claimed`)
carrying `superbot`'s contract, **with a committed floor on the registry**.
*Prevents:* 36 → 8, all read-only, with the one audited write seam not surviving
the port and golden parity structurally unable to see the loss (I-11).

---

## 10 · Observability — "online" is a counted claim

> **Online means: N commands published and read back, M routes reachable from the
> root, K modules loaded — each compared to a committed floor, asserted at boot,
> before readiness flips.**

Not a gateway connection. Not a 200 on `/ready`. The measured failure is exact:
`sb/app/main.py:616` hardcodes `enabled=False`, so that root registers no slash
command, and `/ready` answers 200 anyway — and the *design rationale* for
degrading rather than refusing to boot rests on a survivor set of 27 slash
commands that does not exist (I-19). The population defect inside an
architectural argument.

**The `SURFACE` record**, produced at § 2 step 8 and committed as a floor file:

```
commands_published   112  (floor 100)
routes_reachable     284  (floor 250)
modules_loaded        18  (profile: full, expected 18)
```

**2nd consumer:** the deployment-readiness verdict (§ 11) reads the same record
from the host, and the product-completeness report
([`08-verification.md`](08-verification.md) § 5) reports against the same floors.
**Prevents:** a bot that reports healthy with zero registered commands — the
boot-time twin of a green gate over an empty population.

**Three more properties, each with its measured origin:**

- **Every degraded state reaches a sink that survives the process.** *Prevents:*
  the three independent mechanisms that hid one — a module-level
  `deque(maxlen=256)` with zero sinks attached, a durable latch suppressing the
  notice on later boots, and an in-Discord card that always renders *"(none)"*
  because it is a frozen capture-world literal (R4-D02, R1-D1, both
  `lane-claimed`).
- **Telemetry is wired to the real dispatch path and read back.** `superbot`'s
  per-request correlation ids, structured logging and outcome counters run
  through the actual dispatch path, and its typed failure-mode counters are read
  back by an operator-facing surface (M7-S3, M7-S5, both `lane-claimed`). Take
  that, plus `superbot-next`'s metric-cardinality budget (I-8). **A finding that
  reaches no sink is this review's own defect class wearing an observability
  label.**
- **A diagnostic card computes.** Any operator card that could be a constant is a
  live read or it is not shipped. *Prevents:* a database-health card that always
  reports *"Schema healthy … 103/103"* over a 57-migration ladder (R1-D1,
  `lane-claimed`).

---

## 11 · Deployment isolation

**OD-19: the bots stay separated.** That is an architectural requirement here, not
just an operational one.

- **Separate everything:** its own Discord application and token, its own guild,
  its own Postgres, its own Railway service. It shares no credential, no
  database, no application and no channel with `superbot` or `spider-bot`. The
  estate's standing rail is unchanged: nothing in this plan touches `superbot`'s
  worker, its Postgres or any Discord surface it serves.
- **A deploy watch-path filter from day one.** *Prevents:* ~293 unnecessary
  production restarts caused by a live worker in a 4-service monorepo redeploying
  on any push to `main`, root cause unfixed (M7-D4, `lane-claimed`).
- **Lifecycle from `superbot`, because it is incident-derived.** SIGTERM and a
  restart command both only *record* intent; one watchdog is the sole executor
  with a bounded timeout falling through to a hard exit; the instance lock is
  released *before* the slow drain (M5-S06, M5-S07, both `lane-claimed`, each
  naming the production incident it fixes).
- **Deployment-readiness is a separate verdict from product-completeness**, never
  summed, and it runs **in the host environment with the real dependencies
  installed** — `superbot-next`'s required gate installs only `pytest pyyaml`, so
  the presenter tests skip and every green run was a run in which the renderer did
  not exist (F-D09, `lane-claimed`).
- **The restorability proof runs without a pipe.** `restore-verify.yml:124` pipes
  `python3 -m sb.app.verify_boot` into `tee`, with 0 occurrences of `pipefail`
  and 0 `shell:` keys across all 8 workflow files, so the step's exit status is
  `tee`'s and the weekly proof that the bot can be restored **cannot fail**
  (I-19). The successor's rule is the estate's own: verify with real exit codes.

---

## 12 · The abstraction ledger

Every abstraction this file proposes, its second consumer, and the measured
failure it prevents. **A future session may add to this table only under the same
rule.**

| # | abstraction | 2nd consumer | measured failure prevented |
|---|---|---|---|
| 1 | module manifest (one declaration) | every derived registry: help, settings, tools, commands, migrations, setup | the parent link stored twice + 13 hand-coordinated touch-points (root cause § 1.2; R3-S10 `lane-claimed`) |
| 2 | route graph with required parent | help generator · reachability gate · slash projection · surface floor | help max depth 0; setup 39/40 unreachable (I-13) |
| 3 | single renderer + `RenderedView` | rendering-stability goldens · journey layer · the Discord adapter | 533 green goldens over a serializer production does not install (§ 3b of `08`) |
| 4 | typed operation (one mutation seam) | button path · AI path · scheduler · wizard apply | 190 service modules with 0 authority decorators (B-D07 `lane-claimed`) |
| 5 | `authority_ref` on the operation | every surface inherits it; the audit row records the tier | authority attached to the surface, so a new surface starts unguarded |
| 6 | one audit writer inside the op txn | case record · AI decision log · erasure legs | 49 hand-written audit sites across 27 files (I-18) |
| 7 | store registry with `data_class`/retention/`erasure_ref` | erasure walk · guild teardown walk · schema-growth gate | 31 teardown helpers vs 84 guild-scoped columns (B-D08 `lane-claimed`) |
| 8 | per-module migration ladder + `mod_<name>` schema | out-of-tree modules · restore/verify | the facet fence: 29 of 49 subsystems ineligible (I-10) |
| 9 | typed config spec + `os.getenv` fence | deployment-readiness · the setup wizard's "what is missing" panel | ambient config reads scattered across the tree (M10-S1 `lane-claimed`) |
| 10 | governance/visibility record | renderer · reachability gate · scheduler · disable lever | a second enable flag, and a disable that does not stop background work |
| 11 | one `resolve()` entry point | all six surfaces + the AI path | a fast path added to the adapter directory that skips authority and audit (B-D02 `lane-claimed`) |
| 12 | AI gateway port + provider adapters | NL path · eval harness · deterministic degraded mode | vendor SDK imports spreading with nothing to catch them (M10-D1 `lane-claimed`) |
| 13 | per-module AI tool registry + committed floor | modules register their own tools; the floor gate | 36 → 8, all read-only, invisible to parity (I-11) |
| 14 | risk/mode gate (shadow · preview · auto) | AI actions **and** destructive button confirmation | `ConfirmationSpec` on 0 of 175 ops (B-D05 `lane-claimed`) |
| 15 | scheduler due queue (durable timers) | reminders · retention and erasure jobs · module disable | in-memory `asyncio.sleep` deadlines lost on restart (M2-D2/M2-D4 `lane-claimed`) |
| 16 | egress port | every send · the AI reply path | 915 sends against 18 `allowed_mentions` (B-D06 `lane-claimed`) |
| 17 | `SURFACE` floor record | boot gate · deployment-readiness · product-completeness report | `/ready` 200 with zero commands published (I-19) |
| 18 | boot-time profile | test-guild deployment · per-profile reachability gate | no way to run a subset of the bot (R3-D7 `lane-claimed`) |
| 19 | one loader for in-tree and out-of-tree modules | both paths, by construction | a contract whose in-tree path has privileges the out-of-tree path lacks (I-10) |
| 20 | case record | moderation review surface · AI shadow-mode track record | an AI decision with no artifact a human can review before widening its authority (OD-F) |

---

## 13 · What the rule cut

Six abstractions both repos built, removed here because the second-consumer test
fails on the measurement. **Each names the condition under which it comes back.**

| cut | why | comes back when |
|---|---|---|
| **multi-leg saga compensators** | 185 legs across 175 ops: 176 reversible, 9 compensatable, **0 irreversible** — the compensator/PARTIAL machinery carries no load (B-D11, `lane-claimed`) | a second `EFFECT` leg exists in one operation |
| **the durable outbox** | 763 LOC across five modules for **one** at-least-once event out of 25 known events (M9-D06, `lane-claimed`) | a second at-least-once event exists |
| **`DURABLE_ONCE` idempotency machinery** | 174 of 175 ops are `NATURAL_KEY`, 1 is `NONE_JUSTIFIED`, **0** are `DURABLE_ONCE`, so the dedup branch is unreachable (B-D03, `lane-claimed`). The scheduler's `once()` keeps its key — it has a real consumer | an operation needs cross-request dedup that a natural key cannot give |
| **the fuzzy typo rung** | 174 + 69 LOC, a documented infinite-loop history, a hand-maintained destructive carve-out (C-D09, `lane-claimed`) — and a slash tree with autocomplete removes the need it serves | the prefix surface is ever made primary again |
| **an open renderer escape hatch** | 218 of 314 panels (69 %) took `superbot-next`'s, while the required `NO EXPIRY` ratchet counted a tier-3 marker occurring **0** times (I-16, I-18). The hatch is not banned — it ships with a committed ceiling and a per-entry expiry | never; the ceiling is the mechanism |
| **unused declaration grammar** | 107 of 237 declared field names are never given a non-default value anywhere in the compiled snapshot (M9-D08, `lane-claimed`); three compiler predicates key on fields **0 of 3,552** walked objects carry (M9-D02/D03, `lane-claimed`) | a field ships when it has a live consumer and a predicate with a non-empty population |

---

## 14 · The size check

[`12-owner-decisions.md`](12-owner-decisions.md) OD-C carries an instruction to
this file: `spider-bot`'s **3,172 lines across 27 files** run a live, useful bot
today, and *"this plan's blueprint must not out-build it without saying why."*

**Here is why, and where the line is.** `spider-bot` already contains the smallest
correct version of § 5: `routes.validate()` walks the same literal, non-empty,
module-level `ROUTES` tuple that the real `setup_hook()` calls at boot and the
real Home panel renders from — not a fixture, not a cleared copy (M12-S01,
`lane-claimed`). That is the population contract, built by hand, in a live bot,
by the owner's own recent work. The successor's route graph differs from it by
**requiring a parent and generating help** — not by being larger.

So the honest scoping claim is:

- **Slice one may be `spider-bot`-scale.** The route graph, one renderer, one
  `resolve()`, the typed-config seam, one module, and the surface floor are a few
  hundred lines each. Nothing in §§ 2, 3, 5, 7, 9 or 10 requires 20,000 lines to
  exist — it requires being there **first**, which is the whole finding of
  [`04-root-cause.md`](04-root-cause.md) § 3.
- **What is genuinely bigger is §§ 4 and 8** — the out-of-tree contract and the
  per-module migration ladders — and they are bigger because OD-19 is a
  requirement rather than a nice-to-have, and because I-10 shows what happens when
  the data lane is deferred: it never arrives, and the extension mechanism ends up
  serving the stateless two-fifths.
- **Everything in § 13 is deferred by measurement, not by optimism.** That is
  roughly 2,000 lines of machinery both prior attempts built and neither used.

---

## 15 · What this file does not decide

Routed rather than invented, per the rule in
[`12-owner-decisions.md`](12-owner-decisions.md):

- **OD-A (one server or many)** changes § 5.3 and § 4.2's `setup_sections` lane
  materially. The blueprint above assumes the recommended default — many servers,
  one guild at a time — because per-guild scoping is the boundary every settings
  row, permission check and primary key depends on, and it is expensive to
  retrofit. **If he answers *one server*, the setup surface collapses and § 4.2
  loses one of its six facets.**
- **OD-D (which features are core)** decides how hard § 4 is loaded. If the middle
  set is optional rather than core, the data-owning out-of-tree lane carries the
  whole product rather than an edge case — which is the argument for building it
  in slice one rather than extracting it later.
- **OD-F (how much authority the AI holds)** sets the mode defaults at step 11,
  not the pipeline. The ordering in § 9 is identical under every answer; only the
  tier boundaries move.
- **How long the AI remembers, and what a member may ask it to forget.** No lane
  measured either bot's memory retention or erasure behaviour. The *mechanism* is
  settled — it is a store like any other, under § 8's `data_class`/retention/
  `erasure_ref` declaration — and the *duration* is product intent this file will
  not invent.
