# The roadmap — vertical slices, in dependency order

> **Status:** `plan` — authoritative for **the order the successor is built in,
> what each slice must leave working end to end in a real guild, and the ladder a
> cutover would have to climb.** It is not authoritative for what is built
> ([`05-product-definition.md`](05-product-definition.md)), how it is composed
> ([`06-architecture.md`](06-architecture.md)), what a feature owes
> ([`07-feature-contract.md`](07-feature-contract.md)) or how it is proven
> ([`08-verification.md`](08-verification.md)). **It authorises no
> implementation and it performs no cutover** — OD-13 stands, this package
> creates no repository, and [`13-verdict.md`](13-verdict.md) fixes what a future
> session may and may not do on it.

**Evidence marking, same rule as the rest of the package.** A figure re-derived
by this session against the pinned clones is stated bare with its `I-` id from
[`run/independent-findings.md`](run/independent-findings.md). A figure carried
from a review lane without re-derivation is marked **`lane-claimed`** inline, at
the number, with its row id from [`run/evidence-digest.md`](run/evidence-digest.md).

**Slice ids are stable** (`S1` … `S6`). Other files in this package key their
phase columns to them.

---

## 0 · The four rules this file follows

Each is a rule because a measurement forced it, not because it reads well.

### 0.1 · A slice is a journey. It is never a port band.

`superbot-next` was built in **port bands** — subsystem after subsystem, against
a byte oracle. The result is the measurement this whole package turns on: 49
subsystems compiled, 314 panels registered, 533/533 goldens green, and from the
66 `help.*` roots **max depth zero** — the front door reaches nothing (I-13).
The band that would have delivered the AI write surface simply never came: the
tool catalogue went from 36 tools with one audited write to **8 rows from one
call site** (`sb/domain/ai/tools.py:185`), all read-only (I-11).

A band can complete while the product does not exist, and nothing in a band's
definition notices. **A slice is defined by a person finishing something**, so it
cannot complete while the product does not exist.

### 0.2 · Every slice ends at rung R4 in a real guild, or it has not ended

[`08-verification.md`](08-verification.md) § 4's ladder — R0 declared · R1 wired
· R2 journeyed with its effect asserted · R3 reachable within budget at shipped
visibility · R4 driven by a human in a real guild with every record field
resolvable · R5 operated across a restart and a degraded dependency — is the
per-feature ladder. **At slice level the exit bar is R4 for every feature the
slice ships**, and R5 for every feature once S5 exists.

The reason is F-D09 (`lane-claimed`): `superbot-next`'s required gate installs
only `pytest pyyaml`, `install_panel_runtime` returns before installing the
presenter when `discord` is unimportable, and the four presenter tests skip —
`19 passed, 4 skipped`, EXIT=0. **Every green run of that required gate was a run
in which the renderer did not exist.** A slice that ends on CI alone is making
the same claim.

### 0.3 · A slice earns its place by putting an existing seam under a new *kind* of load

This is [`06-architecture.md`](06-architecture.md) § 12's second-consumer rule,
lifted to the slice. S1 builds the typed operation; S3 makes a *human moderator*
its caller; S4 makes a *model* its caller; S5 makes a *timer* its caller. Each
later slice is chosen because it is the first caller of a different kind — not
because it adds features.

The failure this prevents is measured on both sides. `superbot-next` declared
erasure over **52 stores** and executed nothing — of 48 distinct `erasure_ref`
names, **zero** are registered op keys and 6 do not resolve at all (B-D01,
`lane-claimed`). `ConfirmationSpec` is carried by **0 of 175** registered ops, so
the `ConfirmRequired` branch is dead code (B-D05, `lane-claimed`). Both are
seams with one nominal consumer and no real one. A slice that only adds features
to an existing seam is a port band wearing a journey's name.

### 0.4 · The population contract is not a slice — it is in the first commits or the plan has already failed

[`08-verification.md`](08-verification.md) § 1's three lines
(`POPULATION` / `FLOOR` / `assert len(population) >= FLOOR`) and the checker
framework that makes them **required arguments of registration** are not
scheduled anywhere below, because they are not schedulable. They are the shape
of the first check written, in S1, before the first feature.

[`04-root-cause.md`](04-root-cause.md) § 3 closes with exactly this and it is
repeated here only as a sequencing constraint: these mechanisms are cheap in the
first commits and **unaddable later**, which is precisely what was true last
time. `superbot-next` is the estate's existing precedent for a disciplined
clean start that reached 3,648 green tests without them.

---

## 1 · The map

| id | slice | the journey it finishes | the seam it is the first *new kind* of caller for | exit rung |
|---|---|---|---|---|
| **S1** | **Front door and first run** | an owner installs the bot, finds setup from the root, configures it, comes back the next day and finds it again | — (it builds the seams) | R4 on setup + help |
| **S2** | The ported module that owns its data | a member uses a feature that arrived **from outside the repository**, with its own tables | the module loader, from out of tree; the erasure/teardown walk | R4 |
| **S3** | The mutation spine and the record a human can read | a moderator acts, and at 02:00 someone reads back what happened, in Discord | the typed operation, called by a *human under authority*, with preview at the risk gate | R4 |
| **S4** | Judgement without authority | a member says something in words; the bot understands, proposes, and a human confirms | the typed operation, called by a *model*; the case record | R4, AI-off suite green |
| **S5** | Operations: time, degradation, restart | the bot survives a restart, a dead provider and a dead database, and says so | every registry, walked by a *timer* with no interaction context | R5 on everything shipped |
| **S6** | The second configuration | the same build serves a second guild and a second profile | the per-guild scope and the per-profile floor | R4 per profile |

**Dependency shape.** Not a chain everywhere: S3 and S2 are independent after S1,
and S4 depends on S3 rather than on S2.

```
S1 ── front door, route graph, one renderer, surface floor, population contract
 │
 ├── S2  out-of-tree module owning data ─────────────┐
 │                                                    │
 └── S3  mutation spine + audit read surface ── S4  AI judgement (shadow → preview)
                                                      │
                                     S5  time, degradation, restart  ← needs S2+S3+S4
                                                      │
                                     S6  second profile / second guild
```

**S5 is deliberately last of the build slices and is not optional.** It is the
slice that turns every earlier declaration into something a timer executes, and
it is where R5 becomes reachable at all. `superbot-next` shipped a weekly
restorability proof that **cannot fail** — `restore-verify.yml:124` pipes
`python3 -m sb.app.verify_boot` into `tee`, with **0 occurrences of `pipefail`
and 0 `shell:` keys across all 8 workflow files**, so the step's exit status is
`tee`'s (I-19).

### 1.1 · The venue is an owner step, and it is not a slice

S1 cannot start until an isolated **Discord application + bot token**, a **test
guild**, and a **test Postgres** exist, none shared with `superbot` or
`spider-bot` ([`06-architecture.md`](06-architecture.md) § 11). That is owner
work, it is four items, and it should be handed over as finished steps rather
than as directions. It is listed here so its absence is visible as a blocker
rather than discovered on the first day.

The estate's standing rail is unchanged by every line below: **nothing in this
roadmap modifies `superbot`, its Railway worker, its Postgres, or any Discord
surface it serves.**

---

## 2 · S1 · Front door and first run

> **The unambiguous name:** *one route graph with a single root, from which the
> first-run setup console is a destination like any other — reachable on day one,
> reachable on day thirty, and reachable after the join message is gone.*

### Why this is first, and why it is a finding rather than a preference

Both bots lose the same journey at the same seam, by unrelated mechanisms
(I-13):

- `superbot-next` wires **314 panels with 200 downward edges**, where a 314-node
  graph needs **≥ 313** merely to be a connected tree. From `help.*` roots max
  depth is **0**. `setup` is **39 of 40 panels unreachable** from every declared
  entry point combined. Adding framework Back/Home up-links raises edges to 278
  and reachability by **zero** panels — as it must, since an up-link points at an
  ancestor you already reached.
- `superbot` reaches setup **only** through an ephemeral on-join launcher
  message with no route back: `"setup"` is not one of the 43 `SUBSYSTEMS` keys so
  the help dropdown can never list it, `_AdminPanelView`'s 15 buttons include no
  Setup, and `check_command_reachability.py:372` exempts every operator-tier
  command from the guard by construction. The `_repost_launcher` button is the
  tell — someone met this and shipped a way to re-post the message rather than a
  route into the flow.

**And the ordering argument is stronger than the defect argument.** Every later
slice registers routes into this graph. If the graph arrives second, everything
built before it is a population the reachability gate never saw — which is the
population defect, scheduled deliberately.

### Objective

Build the smallest system in which a route cannot exist without a parent, a
person can reach every enabled route from one root inside a committed budget, and
the first-run console is one of those routes.

### User-visible outcome

An owner invites the bot to a fresh guild and, **without being told any command**,
configures it: which channels it may use, which modules are on, who may
administer it. Then he dismisses the join message, restarts the bot, comes back
the next day, types the root command, and finds the same console — showing the
state he actually applied, read live.

A member types a wrong token and gets an answer.

### Architectural capability introduced

The whole spine, at minimum size ([`06-architecture.md`](06-architecture.md)
§§ 1–3, 5, 7, 9, 10):

- composition root as **one function the test suite executes** — against
  `superbot-next`'s 624-line `run_app` that no test executes, referenced 6 times
  through `inspect.getsource` (M8-D03, `lane-claimed`);
- typed config spec with the `os.getenv` fence (M10-S1, `lane-claimed`);
- **one renderer** and the `RenderedView` value object — no twin, ever
  ([`08-verification.md`](08-verification.md) § 3b);
- the route graph: `add_route()` requires a parent, compiler asserts
  `count(root) == 1`, **help is generated by walking it**;
- one `resolve()` entry point with pipeline steps 0–6 and 12–15 (the AI segment
  7–11 is absent, not stubbed);
- one settings store, per guild, with the four activation values
  (`sb/spec/settings.py:63-69`, grammar enforced at `:306-321` — the donor);
- the typed operation with `authority_ref` and `audit_verb`, first caller: the
  wizard's apply;
- the `SURFACE` floor record and boot step 8;
- **the checker framework**: `population` and `floor` are required arguments of
  check registration, and a check that does not register cannot run in the gate.

### Depends on

§ 1.1's venue. Owner decision **OD-A** sets the size of the setup surface — the
slice is written under its recommended default (*many servers, one guild at a
time*); if he answers *one server*, the wizard collapses to a single owner
console and S1 gets smaller without changing shape.

### Implementation boundaries

**In:** root route, help projection, setup console + wizard sections, the
join-time message **as an additional entry edge**, per-guild settings, one
authority tier boundary, the not-found answer, boot floors.

**Out, explicitly:** moderation, AI (no gateway, no provider adapter, no tool
registry), the scheduler, the out-of-tree loader, any second module, any
community feature from OD-D's middle set, prefix aliases beyond the root.

**The one thing that must be in even though it looks like S2's:** the *shape* of
a module directory ([`06-architecture.md`](06-architecture.md) § 1) and the
loader that reads it. S1 ships **one** in-tree module through that loader, so
that S2's out-of-tree path is the same loader with a different source rather than
a second mechanism.

### Tests, by proof layer

| layer | population it declares | floor | negative control it ships with |
|---|---|---|---|
| structural | every module in the shipped package | modules == profile | add a `modules/a → modules/b` import in a scratch commit; the AST guard must red, **counting function-body imports** (I-22: 268 of 296 cross-subsystem edges, 90.5 %, sit in function bodies, and all 8 mutual pairs live there) |
| contract | every registered route, command and component id | route count ≥ floor | mint a duplicate `custom_id`; the collision fence must raise, as `sb/kernel/panels/registry.py:79-87` already does |
| journey | the setup wizard's canonical path, end to end | 1 (it is the only journey) | delete the wizard's apply op; the journey must fail, not skip |
| reachability | **the route graph the composition root built**, walked from the root over the **rendered** view | routes ≥ floor | remove one route's parent edge; the walk must name that route |
| effect | the wizard's apply operation | 1 | assert the settings row changed **and** the audit row exists; then re-run with the write suppressed and require a red |
| rendering stability | the root and console panels | — | demoted to its one property; it may never be the acceptance oracle |

**Two anti-vacuity requirements that are conditions of merge, not aspirations:**

1. **Every gate above ships its negative control in the same PR**, and the
   control is *run in CI* — the mechanism `superbot` already built and left in one
   file (`tests/unit/invariants/test_help_reachability.py:61-80`, whose docstring
   is *"a vacuous check is worse than none"*), plus the denominator assert
   `superbot-next` built and left in one file
   (`tools/run_golden_parity.py:162-170`).
2. **A skipped test in a required gate is a red gate.** No `-q` run may exit 0
   over an empty collection. The measured original: `pytest tests/integration -q`
   → `14 skipped in 0.04s`, **EXIT=0**, and `pytest tests/e2e -q` →
   `11 skipped`, **EXIT=0**, both inside `superbot-next`'s required
   `named-gates` job that provisions Postgres *precisely so they cannot skip*
   (I-16).

### Test-guild scenario — the acceptance drive, in order

Run by a human in the test guild, against the built SHA. This is the R4 record.

1. Invite the bot to a **fresh** guild. It creates or picks a channel and posts
   the first-run message with an owner ping, degrading through named fallbacks to
   a DM — `superbot`'s shape, kept because it is production-proven (D-S06,
   `lane-claimed`).
2. **Delete that message.** Then type the root command. Reach setup from the
   root in ≤ the committed budget.
3. Complete the wizard. Abandon it halfway once and resume — the resume path is
   `superbot`'s `views/setup/recovery.py` shape, with the mutating buttons
   re-checking authority against a fresh snapshot (M1-S07, `lane-claimed`).
4. Set one module's visibility off. Confirm its button disappears from the
   parent, **and** that the reachability gate scores it *hidden*, not *orphan*
   (I-14 — the gate must model per-guild visibility or it trains its readers to
   ignore it).
5. Restart the process. Re-open the console: state is read live and matches.
6. Type `/hlep`, `!seting`, and a bare mention. Three answers, no silence.
7. As a non-admin, open the console: a **stated refusal**, naming the reason —
   `superbot`'s two-tier line is the donor (`services/setup_access.py`:
   `is_setup_admin` may view, `can_apply_setup` may write, M1-S03,
   `lane-claimed`), together with the bootstrap escape hatch that admits an
   operator's bootstrap command *before* reading the per-guild policy row
   (`disbot/core/runtime/command_access.py:351-358`, M1-S01, `lane-claimed`).

### Observability

Boot emits the `SURFACE` record — `commands_published` (read back from Discord,
not intended), `routes_reachable`, `modules_loaded` — before readiness flips, and
posts the startup summary out of band **before** the gateway connects, so a boot
that dies later still produced an artifact (R4-S03, `lane-claimed`). Readiness is
a decision table with a named reason per row and is DB-aware (R4-S08,
`lane-claimed`).

The measured counter-example this replaces: `sb/app/main.py:616` hardcodes
`sync_remote(bot, committed, enabled=False)` — that root publishes **no slash
command at all** — while `/ready` answers 200, and the *design rationale* for
degrading rather than refusing to boot rests on 27 surviving slash commands that
were never registered (I-19).

### Failure and rollback

- **Rollback:** the slice is one merge into a repository with no users. Revert
  is the whole rollback path, and it stays that cheap only while OD-B's *no
  replacement promise* holds.
- **The stop rule — this is the important half.** If the reachability gate can
  only be made green by adding exemptions, **stop and re-cut the graph**; do not
  start an exception file. `superbot` carries five of them
  (`consistency_exceptions.yml`, `command_reachability_exceptions.yml`,
  `settings_reachability_exceptions.yml`, `audit_seam_exceptions.yml`,
  `deferred_recovery_exceptions.yml`) plus a 55-entry `known_violations` ledger,
  and [`04-root-cause.md`](04-root-cause.md) § 1.2 locates the debt precisely
  there. If an exemption is genuinely unavoidable it carries a reason **and an
  expiry**, and the checker fails on an expired one — the mechanism
  `superbot-next` already built in 2 of the 10 checkers that carry exemptions
  (`tools/check_settle_once.py:629-637`).
- **The false-done signature to watch for:** the gate goes green on the first
  run. On a real graph it should be red until the graph is wired, and a
  first-run green means the population is empty. Check `len(population)` in the
  log before believing the tick — the exact reading that would have caught
  `superbot-next`'s navigation golden on the day it was written (I-2).

### Exit criteria — "done" for S1, stated so it cannot be argued

All seven, each observable:

1. **Root → every enabled route within the committed budget**, asserted by a gate
   whose population is the composition root's route graph, walked over the
   rendered view, with a committed floor and a negative control that reds.
2. **`count(root) == 1`** and **zero orphans by construction** — `add_route()`
   cannot be called without a parent.
3. **Setup is in the graph**, reachable after the join message is deleted, after
   a restart, and on a later day. The join message is an *additional* edge.
4. **The wizard's apply changed the database and wrote its audit row**, proven by
   effect assertion, not by a recorded string.
5. **Boot asserts the `SURFACE` floor and reads back the published command
   count**; a deliberately removed command fails the boot in a scratch branch.
6. **Nothing is silent** — result, typed refusal, or did-you-mean, always within
   one interaction.
7. **R4 for the setup journey and the help journey**: a human drove them, the
   record's `build_sha` equals the PR head, `signed_at` parses inside the build's
   lifetime, every evidence link resolves to a message in the recorded guild, and
   `surface_id` resolves in the committed manifest. The signer is a human, not
   the session that wrote the feature ([`08-verification.md`](08-verification.md)
   § 4 — challenge F forged a record with `surface_id='/NO_SUCH_COMMAND_AT_ALL'`,
   `signer='me'`, `build_sha='zzzz'` and it validated with **zero problems,
   EXIT=0**, `lane-claimed` F-D04).

---

## 3 · S2 · The ported module that owns its data

### Objective

Prove the extension contract by installing a feature **from outside the
repository** that owns tables, contributes a setup section, and is covered by the
erasure and teardown walks without anyone editing them.

### Why this is second

OD-19 is a requirement, not a preference, and it is the requirement **neither
predecessor meets**: `sb/app/plugin_host.py:78-83` fences plugins to
`ALLOWED_FACETS = (commands, panels, settings, events, capabilities)` and rejects
`HOST_ONLY_FACETS = (stores, data_invariants, wizard_sections)`, so **29 of
`superbot-next`'s own 49 subsystems (59 %) are ineligible as out-of-tree
plugins** (I-10) — everything that owns data.

And the encouraging half is equally measured: portability across these two
architectures **has already happened 54 times**, 8 pairs at ≥ 0.90 similarity and
one byte-identical — `disbot/utils/mining/capacity.py` and
`sb/domain/mining/capacity.py`, md5 `64f1665a9fb83a940d95eca5b9492bf2` (I-21).
The fence is a contract choice, not a structural limit.

**Second rather than later because the contract must carry the product, not an
edge case.** OD-D's recommended default is that none of the middle set (`xp`,
`karma`, `leaderboard`, `counting`, `starboard`, `community_spotlight`, `ticket`,
`polls`, `reminders`) is core — which puts the extension contract under real load
immediately, and that is the only way to find out whether it works.

### The module to port, and the criteria if it is changed

**Reference: `starboard`**, which [`06-architecture.md`](06-architecture.md) § 4.4
already works step by step. It is the hardest honest case: a live production cog
with three dedicated tables, two migrations and its own config panel, which is
**absent from `SUBSYSTEMS` entirely** — `new_subsystem.py check --key starboard`
exits 1 with 6 of 11 touch-points missing, so `!settings` cannot list it and its
only route is the undiscoverable `!starboard` command (R3-D1, `lane-claimed`).

The actual pick is **OD-D**'s. Any substitute must satisfy four conditions, or
the slice does not test what it exists to test: it **owns at least one table**,
**contributes at least one setup section**, **exposes at least one typed
operation**, and **already exists in `superbot`** so the port is a port rather
than a new build.

### User-visible outcome

A member uses the feature, and an operator turns it on from the same settings
surface as everything else. Neither can tell it lives outside the repository.

### Architectural capability introduced

- the **out-of-tree loader** — the same loader S1 used in-tree, reading an
  installed distribution, hash-pinned in a lockfile
  (`superbot-next`'s pinning is proven both ways: zeroing a `manifest_hash` and
  deleting a pin each EXIT=1, M8-S07, `lane-claimed`);
- **per-module migrations into `mod_<name>`**, contiguous *within the module*,
  with its own `checksums.json`, verified at boot. This is the decision that
  dissolves the fence: `tools/check_migrations.py:4-16` requires versions unique
  and contiguous from `0001` across **one global directory**, and an out-of-tree
  module cannot claim a number in a sequence it does not own;
- the **store registry** with `data_class` / retention / `erasure_ref`, and the
  erasure + guild-teardown walks that enumerate it;
- **module-contributed setup sections** — the host owns order, resume and
  authority; the module owns copy and its typed apply.

### Depends on

S1 (loader, route graph, settings, typed operation, floors). Nothing else.

### Implementation boundaries

**In:** one module, out of tree, with data. The `CREATE SCHEMA` path (measured
absent from both predecessors: `CREATE SCHEMA` appears **0 times** across
`superbot-next`'s 57 and `superbot`'s 104 migrations, and **0 files** in either
mention `search_path` — every table is in `public`).

**Out:** a second module, a plugin marketplace, dependency resolution between
modules, hot-loading (decided against in
[`06-architecture.md`](06-architecture.md) § 4.5 — the lever is *disable*, and it
arrives in S5).

### Tests

- **Portability gate** — `check_module_portability` walks the fixed interior for
  **every** in-tree module, so every in-tree module is an out-of-tree candidate
  by construction. Population: all modules. Floor: all modules.
- **Migration gate** — checksums verified at boot and in CI; a cross-schema DDL
  statement in a module migration is rejected **before it runs**; negative
  control: a migration touching another module's schema must red.
- **Erasure gate** — every `erasure_ref` resolves to a **registered operation**.
  Population: the store registry. Floor: its own size. This is the gate whose
  absence B-D01 measured (`lane-claimed`): 52 stores declared, **0 of 48**
  `erasure_ref` names registered as op keys, 6 not resolving at all.
- **Effect layer** — the module's op changes its own tables and **no others**,
  asserted as a row-level diff over a before/after snapshot. `superbot-next`'s
  `db_delta` capture is the donor and R5 called it *"the only assertion in either
  repo that proves a write happened"* (`lane-claimed`).
- **Teardown** — the guild-leave walk empties every one of the module's tables
  with no edit to the walk. Negative control: add a fourth table without
  declaring it; the walk's completeness assert must red. The measured original is
  `superbot`'s **31 hand-written teardown helpers against 84 guild-scoped
  columns**, with staged setup drafts surviving a guild leaving and being
  re-read on re-invite (B-D08, M1-D01, both `lane-claimed`).

### Test-guild scenario

Install the module from a built artifact — not from the source tree. Turn it on
from settings; use it; confirm the data lands in `mod_<name>`. Kick the bot from
a second scratch guild and confirm that guild's rows are gone and the module's
own audit trail behaves as declared. Uninstall the module, restart, and confirm
the bot boots with the module absent, its routes gone from the graph, and the
`SURFACE` floor recomputed **for that profile** — not breached.

### Observability

`modules_loaded` names the source of each module (in-tree / distribution +
version + hash). A module that fails to load is **isolated** — the boot
continues, the module is marked unavailable and *says so* when reached
(`superbot`'s pattern: 59 of 59 extensions load in their own `try/except`) —
**and** the surface floor is what stops isolation from hiding a bot that does
nothing ([`06-architecture.md`](06-architecture.md) § 4.3).

### Failure and rollback

Uninstall is a lockfile entry and a restart; the module's schema is dropped or
retained by an explicit, audited operation, never implicitly. **Stop rule:** if
the module needs a host-side edit to work — any edit outside its own directory —
the contract has failed and the fix belongs in the contract, not in a host
special case. That is the fence re-forming, and it is how 29 of 49 became
ineligible.

### Exit criteria

1. The module was installed **from outside the repository** and the same loader
   loaded it.
2. It owns a schema, applies its own ladder, and its checksums verify at boot.
3. Erasure and teardown cover it **with no edit to either walk**, proven by the
   negative control.
4. Its setup section appears in the wizard, in the host's order.
5. `check_module_portability` is green over **all** modules, in-tree included.
6. R4 for the module's canonical journey.

---

## 4 · S3 · The mutation spine and the record a human can read

### Objective

Make a human moderator the first caller of the typed operation under real
authority, and ship the read surface without which the audit spine serves
compliance rather than a person.

### User-visible outcome

A moderator acts on a member — two interactions, reason captured. At 02:00 a
different staff member opens a case in Discord and reads what happened, who did
it and why. A destructive action asks first, and the confirmation is the risk
gate at a tier rather than a bespoke dialog.

### Architectural capability introduced

- `authority_ref` **on the operation**, not the surface — which deletes code:
  `superbot` carries 166 authority decorators in `cogs`, 3 in `views`, 8 in
  `core` and **0 in `services`**, where the 190 mutation modules live (B-D07,
  `lane-claimed`);
- **one audit writer inside the operation's transaction** — `superbot-next`'s
  central spine, measured at **1 call site / 1 file** against `superbot`'s **49
  sites / 27 files** (I-18);
- **the case record** and its Discord read surface. `superbot-next` writes an
  audit row for every one of its 175 registered ops — its central architectural
  claim — and the only `SELECT` against `audit_log` in the whole tree is the
  workflow engine's dedup lookup (D-D09, `lane-claimed`);
- the **risk/mode gate** at `PREVIEW`, with a real consumer. B-D05
  (`lane-claimed`) is the warning: 0 of 175 ops carried a `ConfirmationSpec`, and
  `superbot`'s own provisioning confirmation gate is bypassed at **3 of 3**
  production call sites with `confirmed=True` hardcoded (M1-D02, `lane-claimed`).

### Depends on

S1. Independent of S2 — but if S2 landed first, the moderation module ships
through the same contract, which is the cheapest available second test of it.

### Implementation boundaries

**In:** one deterministic moderation capability (the pre-check half of
`[D-0042]`'s pipeline), the case record, the audit read surface, preview/confirm.

**Out:** anything a model decides. S3 contains **no AI**. `[D-0042]`'s step 8 does
not exist yet, and that is the point: the pipeline's authority half must be
complete and exercised before the judgement half is written, or the judgement half
is the thing being tested by the authority half's first test.

### Tests

- **Effect layer at full strength**: state change + audit row commit together,
  asserted as a `db_delta`; a suppressed audit write must red.
- **Authority**: the operation refuses for every tier below its `authority_ref`,
  driven through **every** surface it is reachable from, with the population
  declared as *every surface that routes to this op*.
- **Preview**: a destructive op cannot execute without the confirm step; negative
  control removes the gate and the test must red.
- **Read-back**: the case a test creates is retrievable through the Discord read
  surface, rendered by the **shipping renderer**.
- **Journey with AI off** — trivially true here, and the assertion is installed
  now so it is not retrofitted in S4.

### Test-guild scenario

A moderator warns a member; a second staff member finds the case from the root
route and reads the reason; the actor is named. Repeat for a destructive action
and cancel at the confirm step — confirm nothing changed, by reading the
database, not the reply. Then attempt the action as a member: a stated refusal
naming the reason, logged as a structured deny line (M1-S08, `lane-claimed`).

### Observability

Per-request correlation ids and outcome counters wired to the **real dispatch
path** — `superbot`'s pattern, with typed failure-mode counters read back by an
operator surface (M7-S3, M7-S5, both `lane-claimed`) — plus a metric-cardinality
budget (I-8). Every audit row carries the resolved authority tier.

### Failure and rollback

Per-guild disable of the moderation module (S5 makes this a general lever; S3
ships the settings half). **Stop rule:** if the audit read surface slips to
"later", the slice is not done. A write-only audit spine is the measured failure
this slice exists to not repeat, and it is the one that reads as harmless right
up until 02:00.

### Exit criteria

1. Every mutating surface reaches the world through **one** typed operation —
   an AST gate whose population is *every function in every `store.py`* and which
   proves store functions cannot be called without a `conn` the engine owns.
2. Authority is resolved from the operation, before any work, on every surface.
3. Effect + audit commit together, proven by mutation, not by declaration.
4. A human can read a case from Discord.
5. Preview/confirm has a real consumer and a negative control.
6. R4 for the moderator journey and the case-read journey.

---

## 5 · S4 · Judgement without authority

### Objective

Add `[D-0042]`'s steps 7–11 — deterministic pre-check, optional AI analysis,
typed schema-validated verdict, policy engine, risk/mode gate — with a model as
the first non-human caller of S3's typed operation, and **no new write path**.

### User-visible outcome

A member describes a problem in words. The bot understands it, files a durable
report with a stable id, and answers. A staff member reviews what the classifier
would have done, in shadow mode, before anything is allowed to act.

### Architectural capability introduced

- the **AI gateway port** and provider adapters, never-raises, with a
  deterministic provider in the same set — `superbot`'s design, and its
  successor's own header says so: *"Ported from shipped
  `disbot/core/runtime/ai/gateway.py`"* (I-4);
- the **per-module tool registry with a committed floor**. This is I-11's direct
  answer: `superbot`'s closed catalogue of 36 tools with exactly one audited
  write became `superbot-next`'s open registry with **8 read-only rows from one
  call site**, and byte parity could not see the loss because an unregistered
  tool emits nothing. The registry is the better abstraction and it ships **with
  `FLOOR`**. `superbot` has **no per-cog registration hook at all** — `grep` for
  `register_tool` / `add_tool` / `tool_provider` across `disbot/` returns
  **zero** (M4-D6, `lane-claimed`) — so this is genuinely new on both sides;
- **shadow mode as a mode of the same pipeline**, so the evidence it collects is
  evidence about the code that would have run;
- **durable-first report intake**: the record exists with a stable id before any
  external projection (`[D-0042]`, adopted verbatim).

### Depends on

S3 — the typed operation, authority, audit, case record. Not S2.

### Implementation boundaries

**In:** intent understanding for capabilities that already exist, one classifier
in shadow mode, the report intake, the tool registry with read-only tools plus
**exactly one** audited write, which is the shape production already proved
(`open_support_ticket`, through the audited mutation seam, I-11).

**Out:** autonomous action above OD-F's default (auto only for low-risk
reversible; preview for medium; deny high-risk and destructive). Any widening is
a new explicit decision, never a threshold the system crosses on its own. **Out:**
memory retention duration — the mechanism is a store like any other; the duration
is product intent this package does not invent
([`06-architecture.md`](06-architecture.md) § 15).

### Tests

- **The AI-off suite is a required gate.** The journey population runs **with AI
  disabled**: every non-AI journey passes, every AI journey produces its declared
  refusal. A suite that only runs AI-enabled measures one of the two products the
  bot has to be.
- **Verdict schema**: invalid, incomplete, timed-out and degraded model output
  each produce **no automatic action** and a recorded degradation — four cases,
  each asserted.
- **No second write path**: an AST gate proving every AI-initiated effect enters
  at the same typed operation, with the same `authority_ref`, as the button.
- **Registry floor**: tool count ≥ `FLOOR`, write-capable tool count == declared.
  Negative control: unregister one and the gate reds.
- **Authority is never widened**: the model's proposal is subject to the tier
  resolved at step 3. `superbot-next`'s scope lattice is real and tested and was
  **never fed from a live user's Discord permissions** — every production call
  site sits at the USER floor (M10-D3, `lane-claimed`).
- **Provider containment**: vendor SDK imports only under the provider adapter
  directory, whole-AST, including function bodies and `importlib` by name
  (M10-D1 measured the absence of any such checker, `lane-claimed`).

### Test-guild scenario

A member reports a bug in plain language; the report appears in durable storage
with an id, and the member is told the id. A staff member opens the shadow-mode
review surface and sees N classifier decisions with their reasons, none of which
acted. Then a provider outage is injected: the bot **says** the capability is
unavailable — the `pending_handler` shape, *"declared surface, honest refusal,
never silent"* (F-S07, `lane-claimed`) — and every deterministic route still
works.

### Observability

Every model call records provider, latency, token cost, verdict validity and
whether the pre-check had already settled it. Every degraded state reaches a sink
that survives the process — the measured counter-example being three independent
mechanisms hiding one fact: a module-level `deque(maxlen=256)` with **zero
sinks**, a durable latch suppressing the notice on later boots, and an
in-Discord card that always renders *"(none)"* because it is a frozen
capture-world literal (R4-D02, R1-D1, both `lane-claimed`).

### Failure and rollback

The per-guild AI kill switch is one of S1's settings, immediate, and it is not a
deploy-time flag. Rolling back S4 leaves S1–S3 fully working — which is the
structural claim § 8 of [`05-product-definition.md`](05-product-definition.md)
makes and this slice proves.

**Stop rule:** if any capability becomes reachable *only* by talking to the bot,
the slice has broken the product invariant and the non-AI route is added before
anything else proceeds.

### Exit criteria

1. `[D-0042]`'s pipeline is implemented in order, and steps 7–11 are skippable
   without affecting steps 0–6 and 12–15.
2. Invalid model output is inert, in four asserted failure modes.
3. Shadow mode has produced a reviewable track record a human has read.
4. The tool registry has a committed floor and exactly one audited write, through
   S3's operation.
5. The AI-off journey suite is required and green.
6. R4 for the report-intake journey and the shadow-review journey.

---

## 6 · S5 · Operations — time, degradation, restart

### Objective

Make a timer the first caller with no interaction context, and make "online",
"degraded" and "restored" all mean something a machine asserted.

### User-visible outcome

A reminder fires after a restart. A retention job deletes what it said it would.
An operator flips one switch and a misbehaving module stops — including its
background work. The bot survives a dead database and says which capability is
unavailable and why.

### Architectural capability introduced

- the **scheduler due queue** with durable timers — against in-memory
  `asyncio.sleep` deadlines lost on restart (M2-D2/M2-D4, `lane-claimed`);
- **retention and erasure as scheduled jobs** over the store registry;
- the **disable lever**: one governance record read by the router, the renderer
  **and the scheduler**, so a runaway background loop stops too;
- **session identity as a database constraint** — `UNIQUE (user, channel,
  module)` with `INSERT … ON CONFLICT … RETURNING`, which survives the restart
  that destroys an in-memory lock (M6-S2, `lane-claimed`; `superbot-next` has no
  equivalent to port);
- **deployment-readiness as a separate verdict**, run **in the host environment
  with real dependencies installed**, never summed with product-completeness;
- **lifecycle from `superbot`, because it is incident-derived**: SIGTERM and the
  restart command only *record* intent, one watchdog is the sole executor with a
  bounded timeout falling through to a hard exit, and the instance lock is
  released *before* the slow drain (M5-S06, M5-S07, both `lane-claimed`).

### Depends on

S2, S3 and S4 — because the point is to walk *their* registries from a caller
that has no interaction, no user and no guild context handed to it.

### Implementation boundaries

**In:** scheduler, retention, erasure jobs, disable lever, restart-restore of
persistent components, the deploy watch-path filter, the restore proof.

**Out:** autoscaling, multi-process sharding, a second host.

### Tests

- **Restart-restore**: every persistent component's `custom_id` resolves after a
  restart, against the same mint table the journey tests click.
- **Scheduler**: a job due during downtime runs after boot; the population is
  *every declared job*, the floor is its size.
- **Disable**: flipping the record stops the module's routes, its rendering
  **and** its due jobs — three assertions, one flag.
- **Degraded**: with the database down, readiness returns a named reason rather
  than 200, and every degraded notice reaches a durable sink. Negative control:
  remove the sink and the test must red.
- **The restore proof runs with real exit codes.** No pipe, no `tee`, `pipefail`
  where a pipe is unavoidable. The measured original is I-19:
  `restore-verify.yml:124`, 0 `pipefail` and 0 `shell:` keys across 8 workflow
  files, so the weekly proof that the bot can be restored **cannot fail** — and
  `sb/app/verify_boot.py:100` does exit non-zero, so there was a real status
  being swallowed.
- **Deployment-readiness**: the built image boots on the host, renders a real
  Discord message, and survives a restart — three floors, asserted in the host
  environment, because a gate that installs only `pytest pyyaml` is measuring a
  different program (F-D09, `lane-claimed`).

### Test-guild scenario

Schedule something for five minutes out; restart the process twice inside that
window; it fires once. Disable a module mid-run and watch its scheduled work stop
within one cycle. Kill the database; the bot answers with a named degradation on
every route that needs it, and the routes that do not, still work. Restore the
database; the bot recovers without a restart, or says it needs one.

### Observability

The `SURFACE` record is re-emitted at every boot and compared to the committed
floor; the deployment-readiness verdict is reported **adjacent to, never summed
with**, the product-completeness fraction:

```
PRODUCT      R4 on 12 of 14 shipped features   (floor: 100 % of shipped)
DEPLOYMENT   boots on the host image, renders a real message,
             survives a restart                (floor: all three)
```

### Failure and rollback

A failed deploy rolls back to the previous image; the module disable lever is the
in-incident tool and needs no deploy at all. **A deploy watch-path filter ships in
this slice** — `superbot`'s live worker has none in a 4-service monorepo and it
already caused ~293 unnecessary production restarts, root cause unfixed (M7-D4,
`lane-claimed`).

### Exit criteria

1. R5 for every feature shipped so far — a restart and one injected dependency
   failure, in the guild, recorded.
2. A scheduled job survives a restart, exactly once.
3. The disable lever stops routes, rendering and background work.
4. The restore proof fails when the boot fails — demonstrated by making it fail.
5. Deployment-readiness reported separately, from the host, with real
   dependencies.

---

## 7 · S6 · The second configuration

### Objective

Prove the claims that a single-guild deployment cannot test: per-guild scope and
per-profile floors.

### User-visible outcome

The same build serves a second guild with different settings, different visible
modules and no leakage between them — and serves a *smaller* named profile whose
own reachability and surface floors are asserted independently.

### Architectural capability introduced

Nothing new. **That is the point** — S6 is the slice that fails if per-guild
scoping was ever nominal. `superbot-next` `pkgutil`-imports **all 49** manifests
unconditionally, with no flag, env var or config file that will run a subset, so
a second small deployment means deleting manifest modules (R3-D7,
`lane-claimed`); a BTD6 wiki is a permanent, non-removable top-level category in
every server at **74 of 413 commands** (D-D11, `lane-claimed`).

### Depends on

S5, and on **OD-A**. If the owner answers *one server*, **S6 reduces to the
profile half** — a second named module set, its own floors, its own reachability
run — and the guild half disappears with the rest of the multi-tenant surface.

### Tests

- The reachability gate and the surface floor run **per profile**, so "reachable"
  and "online" are asserted for each shipped configuration rather than for the
  full set only.
- A cross-guild read is a test failure: the population is *every store*, and the
  assertion is that no query returns another guild's rows.
- Teardown on guild-leave, run for real in the second guild, verified by reading
  the database.

### Test-guild scenario

Invite the build to a second guild. Configure it differently. Confirm from guild
A that nothing from guild B is visible, and vice versa. Boot the smaller profile
and confirm its floors are its own — not the full set's, and not zero.

### Failure and rollback

Leave the second guild; teardown runs and is verified. **Stop rule:** if
per-guild scope needs a schema change at this point, S1's boundary was wrong and
the correct response is to fix the boundary rather than to add a filter at each
call site — the retrofit OD-A's default exists to avoid.

### Exit criteria

1. Two guilds, two configurations, zero leakage, proven by query.
2. Two profiles, two independent floors, both asserted at boot.
3. R4 per profile for the root journey.

---

## 8 · What is deliberately not a slice

Recorded so each absence reads as a decision.

| not scheduled | why | when it returns |
|---|---|---|
| a "framework slice" before S1 | a framework with no journey is a port band with better manners; the framework arrives as exactly what S1's journey needs | never as a slice |
| a documentation programme | the EAP added **183 surviving doc files to `superbot` in fourteen days and 2 runtime files** (I-9); the successor's documentation is its declaration and its record | never |
| byte-parity with either predecessor | the oracle never ran the shipping renderer ([`08-verification.md`](08-verification.md) § 3b), and the owner has rejected the build those bytes pin | never |
| the games/economy vertical | OD-16; and one AI-content vertical is **30,923 of 59,744 measured lines** of `superbot`'s games surface (M3, `lane-claimed`) | never in this horizon |
| production data import | OD-E's default is *import nothing*; every migration that does not happen is a class of risk that does not exist | only on his answer, dry-run first, reversible, independently verified |
| runtime code hot-load | [`06-architecture.md`](06-architecture.md) § 4.5 — the incident lever is *disable*, which S5 ships | if a case appears that disable does not cover; the loader is additive |
| the six abstractions § 13 of `06` cut | saga compensators (0 irreversible legs of 185), the durable outbox (763 LOC for 1 at-least-once event of 25), `DURABLE_ONCE` (0 of 175 ops), the fuzzy typo rung, an open renderer escape hatch, unused declaration grammar (107 of 237 declared field names never given a non-default value) — all `lane-claimed`, all measured as unused | each names its own trigger condition in that table |

---

## 9 · The cutover ladder

> **This plan performs no cutover, and authorises none.** `superbot` stays live,
> frozen and untouched; `spider-bot` keeps running (OD-C's default); OD-B's
> default is **no replacement promise at all** until a successor has
> independently earned one. The ladder below exists so that a *later* session
> asking "may we hand a journey over?" has a written answer with observable
> criteria, instead of inventing one under pressure. Climbing it is a separate
> decision, made by the owner, after this package's verdict has been superseded
> by a working bot.

The promise is what converted `superbot-next`'s honest work into a failure. The
ladder is therefore written so that **no rung is reached by a green board**.

| rung | what it asserts | how it is decided |
|---|---|---|
| **C0 · Standing alone** | the successor runs in its own guild, on its own application, database and service, with no relationship to any incumbent | S1–S5 exit criteria met; **this is where the plan stops** |
| **C1 · Journey-complete for a named list** | every journey on a **named, owner-approved list** — not "parity", not a subsystem count — is at R4, and R5 after S5 | the PRODUCT verdict reads `R4 on N of N shipped features`, denominator visible |
| **C2 · Operated** | R5 on every listed journey: a restart and an injected dependency failure survived in the target-shaped guild | the DEPLOYMENT verdict, run from the host with real dependencies, adjacent and unsummed |
| **C3 · Coexistence** | the successor runs **beside** the incumbent in the same guild, on non-overlapping surfaces, through an observation window | observable behaviour only — see below |
| **C4 · One journey handed over** | for exactly one journey, the incumbent's route is disabled per guild and the successor's is enabled; reversible by one setting flip; its own observation window | the same criteria as C3, scoped to that journey, plus a clean reversal rehearsed at least once |
| **C5 · The verdict** | the incumbent's surface for that guild is empty and the observation criteria held throughout | **the owner's decision, informed by C3/C4's record. Not a gate, and not a score.** |

### The observation window, and why the final verdict is behavioural

C3 and C4 are decided by **what the bot did in the guild**, over a stated window
of **14 consecutive days** — chosen as a window length, not inherited from
anything. (The estate's one hard external clock, *12 testers opted in for 14
continuous days*, is Google's Play closed-testing requirement for Slingy Spider.
It **ranks** work; it does not define bot readiness, and it is not this
criterion.)

Five criteria, each observable and each with its own instrument, all of which
must hold for the whole window:

1. **Zero unanswered inputs.** Every input addressed to the bot produced a
   result, a typed refusal or a did-you-mean. Instrument: the counter on the
   not-found route, compared to the gateway's received count. This is the
   regression a member notices first, and `superbot-next` shipped it —
   `!helpp` and `!seting` produce total silence (CHALLENGE D, `lane-claimed`).
2. **Zero surface-floor breaches across every boot in the window**, with
   `commands_published` **read back from Discord** at each one. A single boot
   that reported healthy with fewer commands than its floor ends the window.
3. **Every case opened was closed by a human**, with the audit row and the case
   record agreeing. Instrument: the read surface S3 shipped, queried.
4. **Zero AI-initiated writes outside their declared mode.** Shadow means zero
   writes; preview means zero unconfirmed writes. Instrument: the audit rows,
   joined on the actor kind — not the classifier's own log.
5. **Every degraded state that occurred reached a durable sink and was read by a
   human.** A window with zero recorded degradations is not evidence of health;
   it is a reason to check the sink, and the check is part of the criterion.

**And the disqualifier, stated as plainly as the criteria.** A green CI board is
**not** an input to C3, C4 or C5. The whole basis of this package is that 533/533
green certified a bot whose front door reached nothing; a board that could
certify that cannot certify a cutover.

### What the ladder does not decide

- **Whether a cutover is ever wanted** — OD-B, whose default is *no*.
- **Whether `spider-bot` is in scope at all** — OD-C, whose default keeps it
  running untouched and makes the successor a third repository. Nothing in this
  ladder applies to it.
- **Whether any data moves** — OD-E, whose default is *import nothing*. If he
  wants continuity, he names the **server-visible surfaces** that must survive,
  not a table list, and the migration becomes a scoped, rehearsable exercise
  rather than a schema port.

---

## 10 · What this roadmap could not settle

Routed rather than invented, per [`12-owner-decisions.md`](12-owner-decisions.md):

| row | what it moves in this file |
|---|---|
| **OD-A** — one server or many | the size of S1's setup surface, and whether **S6** exists at all (it reduces to profiles under *one server*) |
| **OD-B** — is replacement ever promised | whether § 9's ladder is ever climbed; it is written but not scheduled |
| **OD-C** — third repository or `spider-bot` grown | if `spider-bot` is the seed, **S1 becomes a refactor inside a live bot** with no PR gate, and the test-guild posture every slice above assumes has to be rebuilt around a running service |
| **OD-D** — which community features are core | which module S2 ports, and how many optional modules exist to load the contract |
| **OD-E** — does production data carry forward | nothing in S1–S6; it would add a rehearsal phase before C4 |
| **OD-F** — how much authority the AI holds | S4's mode defaults at the risk gate. **The pipeline order is identical under every answer**; only the tier boundaries move |

Two gaps from [`13-verdict.md`](13-verdict.md) also bear on sequencing and are
not this file's to close: **neither bot was booted**, so every reachability figure
above is a declared-graph figure (closed by an hour in a test guild with
`superbot-next`); and **the fan-out's adversarial refutation pass had not run**,
which is why every lane number in this file carries its `lane-claimed` mark
inline.

**One last sequencing note, and it is the only thing in this file that is not
negotiable.** [`04-root-cause.md`](04-root-cause.md) § 3's closing caveat applies
to the roadmap as a whole: the population contract and the effect rule are cheap
in the first commits and unaddable later. If S1 ships without them, the rest of
this document describes a fourth attempt rather than a third.
