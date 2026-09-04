# The feature contract — what every capability ships, and what it may never touch

> **Status:** `plan` — authoritative for **the obligations a new capability must
> satisfy in the successor, the single declaration that carries them, the list of
> files a feature is forbidden to modify, and the gate that enforces that list.**
> It does not decide what the successor is for
> ([`05-product-definition.md`](05-product-definition.md)), how the runtime is
> composed ([`06-architecture.md`](06-architecture.md)), or how anything is proven
> ([`08-verification.md`](08-verification.md)) — it names the facets those files
> consume. It authorises no implementation; OD-13 stands and this plan creates no
> repository.

**How to read a number here.** A figure re-derived by this session against the
pinned clones (`superbot` @ `5e3a667b`, `superbot-next` @ `d5f66dc2`) is stated
bare with the command or the `I-` id behind it; where it was measured while
writing *this* file, the file and line are given so it can be re-run. A figure
carried from a review lane without re-derivation is marked **`lane-claimed`**
inline, at the number, with its row id from
[`run/evidence-digest.md`](run/evidence-digest.md). Where the evidence cannot
settle a question of product intent it is routed to
[`12-owner-decisions.md`](12-owner-decisions.md) by row id rather than answered.

---

## 1 · The rule this file exists to make executable

[`04-root-cause.md`](04-root-cause.md) § 3 states it in one line: **one
declaration per feature, and every registry derived from it — there is no second
place to update, so there is no drift to check and no exception file to grow.**

That is a sentence until someone writes down (a) exactly what the declaration
contains, (b) exactly what is derived from it, and (c) exactly which files a
feature's diff may not contain. This file is those three lists.

The measured target it is aimed at is not a slogan either. `superbot`'s own
executable integration standard, `scripts/new_subsystem.py`, enumerates **14
named touch-points** for adding one subsystem — re-derived here by reading
`build_checks` (`scripts/new_subsystem.py:164-359`): `key-identity` ·
`registry-entry` · `hub-linkage` · `hub-primary-children` · `panel-command` ·
`cog-file` · `cog-setup` · `help-hook` · `surface-map-row` ·
`command-map-section` · `navigation-map-row` · `extension-loaded` ·
`extension-role` · `sector-folio`. Eleven to fourteen of them fire on any given
key, depending on whether it has a parent hub and a docs folio; the tool's own
docstring calls the job *"~a dozen coordinated edits with no automation"*
(`scripts/new_subsystem.py:11-12`).

**The contract's success criterion is therefore countable, not rhetorical:** a
new feature's pull request touches its own directory and nothing else. § 4 makes
that a gate.

---

## 2 · The declaration — one record, seven identity fields and sixteen facets

The successor's unit of extension is a **feature**: one directory, one manifest
module, one key. The manifest is the only place a feature is registered, and
every other surface is derived from it.

`superbot-next` already built four fifths of this and it is the strongest
transferable artifact in either repository. `sb/spec/manifest.py:24-35` declares
`SubsystemManifest` with **ten fields, eight of them facets** — `key` and
`version`, then `commands`, `panels`,
`settings`, `stores`, `events`, `capabilities`, `data_invariants`,
`wizard_sections` — and `sb/app/main.py:91-104` discovers every module under
`sb/manifest/` by `pkgutil`, so **adding a subsystem requires no registry edit at
all** (R3-S6). That is the shape. The successor keeps it and adds the facets the
evidence says are missing, each one tied to a specific measured failure rather
than to taste:

```python
@dataclass(frozen=True)
class FeatureManifest:
    # --- identity -----------------------------------------------------
    key: str                      # namespace-reserved, frozen, one per feature
    version: int
    owner: str                    # a person or team; R0 of the ladder needs it
    summary: str                  # one line; the help renderer's only copy source
    tier: FeatureTier             # core | optional | experimental  → OD-D
    # --- placement in the route graph ---------------------------------
    parent: FeatureKey | Root     # the ONE parent link; nothing stores the reverse
    entry: RouteRef               # the canonical entry point, budgeted
    # --- surfaces ------------------------------------------------------
    commands:      tuple[CommandSpec, ...]
    panels:        tuple[PanelSpec, ...]
    journeys:      tuple[JourneySpec, ...]        # + vs superbot-next
    # --- authority -----------------------------------------------------
    capabilities:  tuple[CapabilitySpec, ...]     # {feature}.{resource}.{action}
    operations:    tuple[OperationSpec, ...]      # + typed, risk-classed, audited
    # --- state ---------------------------------------------------------
    stores:        tuple[StoreSpec, ...]
    migrations:    tuple[MigrationSpec, ...]      # + namespaced to the feature
    data_invariants: tuple[InvariantSpec, ...]
    settings:      tuple[SettingSpec, ...]
    # --- time and reaction ---------------------------------------------
    events:        tuple[EventSpec, ...]          # what it emits
    subscriptions: tuple[SubscriptionSpec, ...]   # + what it listens to
    jobs:          tuple[JobSpec, ...]            # + durable scheduled work
    # --- judgement ------------------------------------------------------
    ai_tools:      tuple[AIToolSpec, ...]         # + per-feature, [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)-typed
    # --- proof and operation --------------------------------------------
    metrics:       tuple[MetricSpec, ...]         # + declared, cardinality-budgeted
    audit_actions: tuple[AuditActionSpec, ...]    # + the verbs it may write
    wizard_sections: tuple[WizardSectionSpec, ...]
```

**Why each addition exists — the measurement, not the preference:**

| added facet | the measured failure it answers |
|---|---|
| `owner`, `tier` | R0 of the verification ladder ([`08-verification.md`](08-verification.md) § 4) needs a named owner; `tier` is the field [`12-owner-decisions.md`](12-owner-decisions.md) **OD-D** writes into when he rules on the middle set |
| `parent`, `entry` | the parent link is stored **twice** in `superbot` — `SUBSYSTEMS[key]["parent_hub"]` and `HUBS[hub].primary_children` — and `disbot/utils/hub_registry.py:44-57` documents the bidirectional roster rule and the drift checker that had to be written for it. Re-derived: 8 hubs, **34** primary children, **34** subsystems carrying `parent_hub`, matching. Storing it once removes the checker, not just the drift |
| `journeys` | layer 4 of [`08-verification.md`](08-verification.md) § 3c is the **first layer a do-nothing bot fails** and the first one neither repo has. A journey cannot be asserted if it was never declared |
| `operations` | [the 2026-09-04 AI-authority decision](run/in-flight-direction.md): *AI supplies judgement, deterministic code supplies authority.* The typed operation is the authority half. It is also what a permission gate and an audit row hang off |
| `migrations` (namespaced) | I-10: `superbot-next`'s plugin fence lists `stores` as host-only, so **29 of its own 49 subsystems cannot be out-of-tree plugins**. A feature that cannot ship its schema cannot be portable |
| `subscriptions` | `superbot`'s listeners are `@commands.Cog.listener()` methods — invisible to every registry, so nothing can enumerate what reacts to what |
| `jobs` | re-derived: **7** `@tasks.loop` decorators across `disbot/` in 7 cog files, declared nowhere. `superbot-next` has a real kernel scheduler (`sb/kernel/scheduler/`) and **no manifest facet for it**, so a feature still cannot declare durable work |
| `ai_tools` | M4-D6, re-derived here: `register_tool|add_tool|ToolProvider|register_ai_tool|tool_provider` across `disbot/` returns **0** matches; every tool is hardcoded in `disbot/services/ai_tools.py` (**2,719** lines) plus a closed `CATALOGUE` of **36** rows (AST-counted at `disbot/services/ai_tool_catalogue.py`). **Positive control:** the same query against `superbot-next` returns **2** — the definition at `sb/kernel/ai/tools_catalogue.py:86` and the single call site at `sb/domain/ai/tools.py:185` — so the query works and the absence is real |
| `metrics` | `superbot-next` ships `check_metric_cardinality` (I-8) guarding a label budget that no feature declares against |
| `audit_actions` | I-18: `emit_audit_action(` appears at **49 call sites across 27 files** in `superbot` against **1 site / 1 file** for `emit_central_audit(` in `superbot-next`. A verb list per feature is what lets a gate assert the write happened |

**And one deletion, stated so it is not read as an oversight.** There is no
`help` facet and no `navigation` facet. Help pages and Back/Home links are
**generated** from `parent`, `entry`, `commands`, `panels` and `summary`. This is
`superbot-next`'s one unambiguous product improvement and I-21 records it:
`superbot`'s `attach_standard_nav` is opt-in with **17 call sites across 9
files**, while `superbot-next` made engine-injected navigation the default — *"a
port that was improved rather than restated."* The successor keeps the
improvement and fixes what it did not fix: I-13 measured `superbot-next`'s help
tree at **max depth 0** over **314** panels wired by **200** downward edges,
where a 314-node graph needs 313 merely to be a tree. Injected Back/Home links
cannot repair that, and the probe proved it — adding the up-links raises the edge
count to 278 and changes reachability by **zero panels**, because an up-link
points at an ancestor you have already reached.

---

## 3 · The fourteen obligations

Each obligation states four things: what the feature **declares**, what is
**derived** from that declaration (and therefore what the feature does *not*
write), which **gate** reads it, and the **evidence** that the obligation exists.
An obligation with no gate is a wish; every row below names one.

Every gate here inherits [`08-verification.md`](08-verification.md) § 1 without
restating it: it declares its population, asserts a committed floor, and runs
over the shipped artifact. A gate registered without a population and a floor
cannot run.

### 3.1 · Identity and manifest

**Declares** `key`, `version`, `owner`, `summary`, `tier`.
**Derived** the feature's namespace for settings keys, capability strings, event
names, metric names, table names and migration ids; its row in the estate index;
its entry in the release's product-completeness fraction.
**Gate** namespace collision + reservation, modelled on `superbot-next`'s
`check_namespace` / `check_symbol_shadowing` (I-8 — guards with *no counterpart
in `superbot` at all*). Population: every manifest in the shipped package; floor:
the committed feature count.
**Evidence** `superbot`'s identity is spread over `disbot/utils/subsystem_registry.py`
(re-derived: **43** keys), `disbot/config.py`'s `INITIAL_EXTENSIONS`
(re-derived: **59** entries) and `architecture_rules/extension_roles.yaml`
(**67** classified names). Three lists of the same population, three chances to
disagree — and they do: R3-D10 counts **16** cog modules with no matching
registry key, `starboard` among them.

### 3.2 · Route — the invocation surface

**Declares** `commands` (name, group, kind, arguments, audience tier, capability,
summary, usage) and `entry`.
**Derived** the slash tree and its 100/25/1-nest budget; the prefix aliases; the
help page; the command→panel edges the reachability walk uses.
**Gate** slash-budget cap (`superbot-next`'s `check_slash_cap`, I-8) **and** the
reachability walk of § 3.9. Population: every declared command; floor: committed.
**Evidence** [`05-product-definition.md`](05-product-definition.md) § 3.1 settles
the invocation model — one grouped slash tree, prefix as a declared alias — on
`superbot-next`'s measured **386 prefix / 18 slash / 9 both** split and the
owner's own 2026-06-24 request in `disbot/cogs/btd6/_unified.py:1-16`. This file
adds only the contract consequence: **the route is declared, so the alias table
is generated and `compat`-style freezing of a hand-maintained command list is
never needed.** `superbot`'s `KNOWN_PANEL_COMMANDS` is the counter-example —
**22** hand-maintained `(subsystem, command)` pairs at
`disbot/services/customization_catalogue.py:85-108`, from which `ai` is absent
even though `SUBSYSTEMS["ai"]` declares `entry_points: ["ai", "aimenu"]`
(re-derived; § 5.5).

### 3.3 · Handler

**Declares** for every command, panel action, selector option and subscription, a
`HandlerRef` resolving to exactly one callable.
**Derived** the dispatch table; the "every declared surface resolves" contract
check.
**Gate** the single-entry-seam fence — `superbot-next`'s `check_no_skip`, an AST
proof that no Discord surface reaches a handler except through `resolve()`, and
that `import discord` appears only under the adapter root
([`08-verification.md`](08-verification.md) § 3b). The successor widens its root
to wherever ported features live **and pairs it with the positive direction**:
every registered handler must be reachable *from* `resolve()`, not merely
callable.
**Evidence** layer 3 of [`08-verification.md`](08-verification.md) § 3c scores a
do-nothing bot at **100 %** — *"callable" is the whole assertion, so 1,947 no-op
coroutines are indistinguishable from a working bot* (`lane-claimed`, F-S08).
Resolvability is therefore necessary and never sufficient, which is why § 3.13
requires a journey and an effect beside it.

### 3.4 · Domain / service behaviour

**Declares** `operations` — one typed record per state change: input type, output
type, capability, risk class, idempotency key, audit verb.
**Derived** the permission gate's input; the audit row's shape; the AI pipeline's
action vocabulary ([the 2026-09-04 AI-authority decision](run/in-flight-direction.md)); the effect layer's list of things that must be
proven to change the database.
**Gate** no write outside a declared operation. `superbot` already has the
coarser version and it is genuinely good: `architecture_rules/mutation_owners.yaml`
names one canonical mutation service per domain with raw `pool.execute()` allowed
only inside `utils/db/` (re-derived: **14** domains, 6 list entries, 122 lines).
The successor's version is per-operation rather than per-domain, so the
declaration is also the audit contract.
**Evidence** the shape is production-proven in the one place it matters most.
`superbot`'s single write-capable AI tool does not write: it validates
eligibility and emits `ticket.open_requested` so a human clicks a button, and the
row is written by the audited ticket mutation service (M4-S3, `lane-claimed`;
the catalogue's own comment at `disbot/services/ai_tool_catalogue.py:50-52` calls
it *"the one **action** toolset … unlike every other catalogued tool, which is
read-only"*). That is [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s pipeline, shipped, before the decision was
written.

### 3.5 · Persistence

**Declares** `stores`, `migrations`, `data_invariants`.
**Derived** the schema; the per-feature namespace; the `db_delta` effect
assertion's table list; the retention and erasure obligations.
**Gate** migration numbering, **immutability and checksum manifest**
(`superbot-next`'s `check_migrations`, I-8 — over 57 migrations, with no
counterpart in `superbot`), plus a schema-growth ledger, plus the data-lifecycle
checkers. Population: every declared store; floor: committed.
**Evidence, and this is the contract's hardest requirement.** I-10: `superbot-next`'s
plugin host fences three facets out of the out-of-tree contract —
`sb/app/plugin_host.py:78-83`, `ALLOWED_FACETS = (commands, panels, settings,
events, capabilities)` against `HOST_ONLY_FACETS = (stores, data_invariants,
wizard_sections)` — and **29 of its own 49 subsystems declare `stores`**, so 59 %
of its product is structurally ineligible to be the thing its extension mechanism
extends. The host's own docstring gives the reason: *"migrations, S12 money
lanes, and the G-19 setup registry have no out-of-tree lane yet."*

> **Requirement, stated as a requirement because OD-19 makes it one:** an
> out-of-tree feature must be able to own data — ship its own migrations into a
> namespaced schema, declare its invariants, and contribute a setup section — or
> cog portability fails for exactly the classes the owner named. Neither
> predecessor meets this. It is the single largest new build in the contract and
> § 5 shows why: three of the five sampled cogs are on the wrong side of that
> fence.

### 3.6 · Settings

**Declares** `settings` — key, scope (guild / channel / role / user), type,
default, validator, capability required to change it, and the copy shown.
**Derived** the settings panel section (no UI code); the key constant; the
per-guild resolution chain; the settings-reachability assertion.
**Gate** every declared setting is reachable from the settings entry point and
every setting a store reads is declared.
**Evidence, and this is a `PRESERVE_PATTERN` from `superbot`.** `SubsystemSchema`
is a real per-feature config extension point with **19** consumers — re-derived:
19 files matching `disbot/cogs/*/schemas.py` declare `SubsystemSchema(...)` —
and declaring one makes the feature's settings render in the central `!settings`
hub *with no UI code* (R3-S3). `check_settings_reachability` reports **19
reachable · 3 exempt · 0 GAP**, EXIT=0 (`lane-claimed`, R3-S3; not re-run here).
**The pattern is right and its population is the registry**, which is how a live
production feature with three dedicated tables sits outside it: `starboard` has
no `schemas.py`, no `settings_keys` module and no `SUBSYSTEMS` entry (all three
re-derived), so `0 GAP` is true and uninformative — the guard's population and
the product's population are different sets. Under this contract the settings
facet *is* the registry, so a feature cannot be absent from it and present in the
product.
**And one central file the successor must not reproduce:** adding a settings key
to `superbot` means editing three places — the per-subsystem module (good, that
part is local), the re-export block in `disbot/utils/settings_keys/__init__.py`,
and that file's `__all__` (re-derived: **124** exported names).

### 3.7 · Permissions and risk

**Declares** `capabilities` (`{feature}.{resource}.{action}`) and, on every
operation, a risk class: `low-reversible` · `medium-reversible` ·
`high-or-destructive`.
**Derived** the permission check applied at the seam; the per-guild visibility
resolution; the AI pipeline's gate; the confirmation requirement.
**Gate** no handler enforces permission in its own body; the seam applies the
declared capability, and a handler whose declared capability is never checked is
a build error.
**Evidence** `superbot` enforces with decorators — `admin_or_owner`,
`app_admin_or_owner`, `perms_or_owner(manage_guild=True)` — at the handler, while
`SUBSYSTEMS[key]["capabilities"]` carries capability strings as *metadata*
(`disbot/utils/subsystem_registry.py:1002-1007` for `utility`). Two
representations of one fact, only one of them enforcing. `superbot-next`'s
per-guild visibility chain (thread > channel > category > guild) **survived its
rebuild** and is a `PRESERVE_CONTRACT` (R3-S9, `lane-claimed`).
**Risk classes are the owner's call and the default is recorded:**
[`12-owner-decisions.md`](12-owner-decisions.md) **OD-F** — auto-act on low-risk
reversible only, preview-and-confirm for medium, deny high and destructive. This
file consumes that answer; it does not make it.

### 3.8 · UI

**Declares** `panels` — id, audience (`invoker` / `channel`), layout, actions,
selectors, and for each action a `HandlerRef` or a `PanelRef`.
**Derived** the rendered components; the ephemerality flag; the Back/Home links;
the custom_id namespace.
**Gate** the rendered-artifact assertion, universal by construction. Instantiate
the real view, assert over `view.children`, drive each callback against a stubbed
interaction, classify by which response method was awaited.
**Evidence** this is not invented here — it is `superbot`'s own
`tests/unit/views/test_games_hub_view.py`, whose four assertions are exactly the
right ones (`renders_one_hub_button_per_visible_child` ·
`every_hub_button_is_actionable_not_disabled` · `no_placeholder_or_coming_soon_labels`
· `button_fails_closed_when_subsystem_invisible`), applied to **2 of 8** hubs
(I-6). The measured argument for making it a property of the framework instead of
a habit is I-14: **the shared child-discovery seam is 19 for 19; hand-rolling is
8 for 15.** `admin` hand-rolls and gets 6 of 6 right, so hand-rolling is not
wrong — it is *unguaranteed*, and in this family unguaranteed and absent have the
same failure rate given enough time.
**One precision the gate must carry:** the seam's caller narrows by per-guild
governance visibility before rendering, so the assertion is *every declared child
the viewer is permitted to see*. A gate that does not model visibility will score
a correctly-hidden feature as unreachable and train its readers to ignore it
(I-14).
**And the trap that sits directly under this obligation.** The acceptance oracle
in `superbot-next` never runs the shipping renderer: production installs
`DiscordPanelPresenter` (`sb/app/panel_host.py:66`) while every golden's actual
side comes from `rendered_panel_payload()` (`sb/adapters/parity/transport.py:242`,
called at `:531`), a hand-written twin imported by nothing but parity. The
successor's UI gate therefore asserts over **the presenter production installs**,
and a test that constructs any other renderer is not a UI test.

### 3.9 · Help and navigation

**Declares** nothing beyond § 3.1's `summary` and § 2's `parent` / `entry`.
**Derived** the help page, the parent's child button, the Back/Home links, the
breadcrumb, and the entry in the route graph.
**Gate** the reachability walk over the **committed route graph**, from the
canonical entry point, inside the promised interaction budget, with per-guild
visibility modelled. The prototype exists and has already produced results:
[`run/reachability_probe.py`](run/reachability_probe.py) declares its population,
asserts a floor and walks the shipped manifest.
**Evidence** I-13. From the `help.*` roots, `superbot-next` reaches **66 of 314**
panels at **max depth 0** — the front door is not a door. From all entry points
combined, **129 of 314** are unreachable, concentrated in `setup` at **39 of 40**.
`superbot` fails the same journey differently: setup is reachable only from an
ephemeral on-join launcher message with no route back, because `"setup"` is not
one of the 43 `SUBSYSTEMS` keys and `_AdminPanelView`'s 15 buttons include no
Setup. **Two implementations, one root: setup was never a first-class
destination in either route graph.** Under this contract it cannot fail that way,
because `parent` and `entry` are required fields and the walk asserts them.

### 3.10 · Events

**Declares** `events` (what it emits, with the payload's field set) and
`subscriptions` (what it listens to, with the handler).
**Derived** the platform's known-event catalogue; the emitter↔listener
cross-check; the event-payload compatibility pin.
**Gate** every emitted name is declared by exactly one feature; every
subscription names a declared event; a declared event with no emitter and no
subscriber is a stale row and expires (§ 4.4).
**Evidence** `superbot` keeps a central catalogue: `disbot/core/events_catalogue.py`'s
`KNOWN_EVENTS` holds **47** members — 42 string literals plus 5 imported
constants (AST-counted here) — and the module's own docstring instructs *"Add the
literal string to `KNOWN_EVENTS` below."* That is one more central file per
feature. `superbot-next` got this exactly right and it is the pattern to keep:
`sb/spec/manifest.py:31` declares `events` as a manifest facet with the comment
*"K4 derives KNOWN_EVENTS"* — **the catalogue is generated, not edited.**
Subscriptions are the half neither declares: `superbot`'s listeners are
`@commands.Cog.listener()` methods, invisible to every registry, which is why
nothing can enumerate what reacts to what.

### 3.11 · Background tasks

**Declares** `jobs` — id, schedule or trigger, idempotency key, misfire policy,
the store it reconciles against, and the operation it invokes.
**Derived** the scheduler's registration; the boot-time reconcile; the
restart-survival assertion (rung R5 of the ladder).
**Gate** every job survives a restart, proven by a test that kills and re-boots
the process; a durable promise implemented with an in-process sleep is a build
error.
**Evidence, and it is a small measurement with a large consequence.** `superbot`
has **7** `@tasks.loop` decorators across 7 cog files (re-derived), declared
nowhere. And `disbot/cogs/utility_cog.py:55-64` is the shape the rule exists to
forbid: `_remind_later` is `await asyncio.sleep(delay)` followed by a channel
send, wrapped in a bare `except: pass`. Re-derived here: **zero** reminder tables
among the 92 `CREATE TABLE` names in `disbot/migrations/*.sql`. A member who sets
a reminder and a deploy that happens ten minutes later produce a promise the bot
cannot keep and never records breaking (M2-D4 reproduces). `superbot-next` built
a real kernel scheduler (`sb/kernel/scheduler/` — `due_queue`, `misfire`,
`user_automation`) and gave features **no facet to declare into it**.

### 3.12 · AI tools

**Declares** `ai_tools` — for each: spec, minimum scope, whether it reads or
proposes, the typed verdict schema it returns, and the declared `operation` a
proposal maps onto.
**Derived** the model-facing tool list per scope; the grounding allowlist; the
eval-coverage floor; the AI pipeline's action vocabulary.
**Gate** three, and all three answer a measured failure:
1. **A registry floor.** `assert len(registered_tools) >= FLOOR` in the same run
   as the correctness assertions. I-11: `superbot-next` replaced `superbot`'s
   closed 36-row catalogue with a genuinely better open registry — authority can
   only narrow, grounding allowlists are derived — and shipped **8** rows from
   **one** call site (`sb/domain/ai/tools.py:185`), every one a BTD6 factual read
   at `AIScope.USER`, **zero write-capable**. *The mechanism improved and the
   population collapsed, and nothing measured the population.*
2. **Eval coverage equals the catalogue, with no acknowledged holes.** M4-D1: the
   one write-capable tool of 36 is the one tool excluded from eval coverage —
   `_ACK_UNCOVERED_TOOLS = frozenset({"open_support_ticket"})` with
   `_TOOL_COVERAGE_FLOOR` at 35 (`lane-claimed`, M4-D1). An excuse row that
   exempts precisely the riskiest member of the population is the § 4.4 case in
   its purest form.
3. **No free-form prose becomes an action.** [The 2026-09-04 AI-authority decision](run/in-flight-direction.md), quoted as the pipeline it
   is: event → deterministic pre-check → optional AI analysis → **typed
   schema-validated verdict** → policy engine → permission/risk gate → typed
   operation → Discord API → audit + case. Invalid model output means **no
   automatic action** — which is a gate on the verdict type, not a code review
   habit.

**Evidence for the facet existing at all** is § 2's table row: `0` per-cog tool
hooks in `superbot` (re-derived, with the `superbot-next` positive control), a
2,719-line central `ai_tools.py`, and M4-D6's scenario — *"the owner drops an
existing cog into the successor and asks the bot in natural language to use it.
The AI has no tool for it, because tools live in a central registry that cog
cannot reach."* That is OD-19 and OD-16 failing together, and one manifest facet
is the whole fix.

### 3.13 · Tests

**Declares** nothing new — the tests are derived obligations, one per facet, and
the manifest is what makes them enumerable.
**Required, per feature, before it may claim any rung above R1:**

| # | test | over what population | what it forbids |
|---|---|---|---|
| 1 | **journey** | every declared `journey` | the canonical path completing only in pieces |
| 2 | **effect** | every declared `operation` | a write that is asserted by its return value instead of by the row it wrote — proven as a `db_delta`, mutating the state and re-reading |
| 3 | **reachability** | every declared `panel` | a surface reachable only by a jump nothing declares |
| 4 | **rendered UI** | the real presenter production installs | a test against a hand-written twin (§ 3.8) |
| 5 | **negative control** | the same population, mutated | a green test over an empty or modelled set |
| 6 | **degraded** | every declared dependency | a feature that reports healthy with its dependency gone |

**The negative control is a hard requirement, not a nicety, and the evidence is
unusually direct.** `superbot`'s help-reachability guard *has* one — it mutates
the live scheme and `pytest.fail()`s when the target is absent, so the control
itself fails on an empty population
([`08-verification.md`](08-verification.md) § 3.2) — and both the guard and its
mutation test operate on `scheme_live()`, a model of the registry. The mechanism
is right and the target is wrong. The contract inherits the mechanism and points
it at the rendered artifact.
**And the population line is not optional prose.** Two of `superbot-next`'s
**required** CI legs are green over zero executed tests: `pytest tests/integration
-q` → `14 skipped`, EXIT=0, and `pytest tests/e2e -q` → `11 skipped`, EXIT=0
(I-16, re-derived from R2). Both sit in the one job that provisions Postgres
*precisely so they cannot skip*. A skipped test in a required gate is a red gate
([`08-verification.md`](08-verification.md) § 5).

### 3.14 · Observability and audit

**Declares** `metrics` (name, labels, cardinality budget) and `audit_actions`
(the verbs this feature may write).
**Derived** the metric registration; the audit vocabulary; the operator's view of
what this feature did.
**Gate** every declared operation writes its declared audit verb inside the same
transaction as its state change, asserted as an effect; every emitted metric is
declared and within budget (`superbot-next`'s `check_metric_cardinality`, I-8);
**and the audit is readable from Discord**.
**Evidence** the last clause is a product requirement, not an engineering one,
and [`05-product-definition.md`](05-product-definition.md) § 1 already states why:
`superbot-next` writes an `audit_log` row inside the mutation transaction for
every one of its **175** registered compound ops (`lane-claimed`, D-D09) and
ships no way to read them from Discord — the only `SELECT` against `audit_log` in
the tree is the workflow engine's dedup lookup. *A write-only audit spine serves
compliance and does not serve the person at 02:00.* `superbot` is the other way
round: **49** `emit_audit_action(` call sites across **27** files (I-18,
re-derived on the third instrument), and it mirrors Discord's own audit-log
gateway event into a log channel with the actor named (`lane-claimed`, D-S09).
The successor needs both halves, and only the declaration makes the pair
checkable.

---

## 4 · What a feature must NOT have to modify

### 4.1 · The counter-example, measured

This is the debt [`04-root-cause.md`](04-root-cause.md) § 1.2 locates, stated as
files and counts so the successor's no-touch list has a shape to be the negative
of. Every figure below was re-derived in this session against `superbot` @
`5e3a667b`.

| central file a new feature must edit today | population it holds | how it was counted |
|---|---|---|
| `disbot/utils/subsystem_registry.py` | **43** subsystem keys, ~20 fields each | live import of `SUBSYSTEMS` |
| `disbot/utils/hub_registry.py` | **8** hubs, **34** primary children — **the second copy of the parent link** | live import of `HUBS` |
| `disbot/config.py` `INITIAL_EXTENSIONS` | **59** entries | AST |
| `disbot/services/customization_catalogue.py` `KNOWN_PANEL_COMMANDS` | **22** `(subsystem, command)` pairs | source read, `:85-108` |
| `disbot/core/events_catalogue.py` `KNOWN_EVENTS` | **47** members (42 literals + 5 constants) | AST |
| `disbot/utils/settings_keys/__init__.py` | re-export block + `__all__` at **124** names | AST |
| `architecture_rules/extension_roles.yaml` | **67** classified names | YAML key count |
| `architecture_rules/mutation_owners.yaml` | **14** domains | YAML parse |
| `docs/help-command-surface-map.md` | **50** table rows, one per subsystem key | `grep -c '^\| \`'` |
| `docs/setup-platform/settings-customization-command-map.md` | **48** `###` sections | `grep -c '^### '` |
| `docs/repo-navigation-map.md` | a path-level orientation document the check requires the key to be *mentioned* in | `new_subsystem.py:280-300` + reading the doc's header |
| `docs/repo-sector-map.md` | **not** a per-feature list: 5 sectors, plus a machine-readable `sector-folio-map` block (`:243-248`) homing each `docs/subsystems/<key>.md` folio to exactly one sector. It fires only for the **8** features that have a folio (`ls docs/subsystems/` → 9 files, one of them `README.md`) | read at source |

**And five exception files, which are the measure of how much each rule is
already not true.** Re-derived entry counts:
`consistency_exceptions.yml` **102** · `command_reachability_exceptions.yml`
**10** · `duplicate_allowlist.yaml` **9** · `audit_seam_exceptions.yml` **6** ·
`settings_reachability_exceptions.yml` **3** · `deferred_recovery_exceptions.yml`
**1** — **131 entries across six files** — plus `layers.yaml`'s **55**
`known_violations` and **3** `known_lazy_violations` (YAML-parsed).

Two things follow that a rebuild must not get backwards. First, **the response
was right**: `superbot` turned each recurring defect into a machine check, and
I-21 measured that those checks are real — **44 of 45** `scripts/check_*.py` are
driven by asserting tests, on three independent instruments, behind a blocking
`pytest tests/ -v -n auto` step. Second, **the checks are downstream of a shape
that makes the defect easy**, so the exception files grow with the feature set.
The contract attacks the shape.

### 4.2 · The no-touch list

**A feature's pull request contains its own directory and nothing else.**
Concretely, the successor has no file that plays any of these roles, and if one
appears, its appearance is the defect:

1. **No central subsystem registry.** Identity is the manifest.
2. **No hub child list.** The parent link is stored once, on the child; the
   parent's children are a query.
3. **No extension load list.** Manifests are discovered — `superbot-next` already
   proved this works: `pkgutil` over `sb/manifest/`, 49 of 49, with three
   independent tools reusing the same loader (R3-S6).
4. **No central command / panel-command table.** Routes are declared.
5. **No central event catalogue.** It is derived (`sb/spec/manifest.py:31`).
6. **No central settings-key module and no `__all__` to extend.** Keys are
   namespaced by feature key.
7. **No central AI tool file.** Tools are a facet.
8. **No documentation file with one row per feature.** The estate index, the help
   surface map, the navigation map and the sector map are **generated** from the
   manifests. This is the half of the sprawl a cleanup can actually cut, and I-9
   measured its size: the EAP added **183 surviving documentation files in 14
   days** to `superbot` while adding **2** runtime files.
9. **No exception file that only grows.** See § 4.4.

**The one legitimate central artifact** is the committed compiled snapshot — the
manifest corpus recompiled and hash-compared at boot, which `superbot-next`
already does (`sb/app/boot_gate.py`, leg A; divergence is `FAILED_STARTUP`,
R3-D12). It is regenerated by a tool, not edited, and R3-D12 is right that this
partly repays the "one file, no registry edit" gain: adding a feature is one new
file **plus a regenerated snapshot in the same commit**. That is a fair trade and
it should be stated rather than hidden — the snapshot is a build product under
review, not a registry someone maintains.

### 4.3 · `check_feature_locality` — the gate that makes the list real

A rule with no instrument is prose, and this package's whole subject is what
happens to those. The gate:

```
POPULATION : every file changed by this pull request
FLOOR      : 1                      # a PR that changes nothing is not a feature PR
RULE       : for a PR labelled `feature:<key>`, every changed path is under
             features/<key>/ , or is the regenerated snapshot, or is listed in
             this PR's `cross_cutting` block with a reason and an expiry.
```

Three properties it needs, each taken from a mechanism this estate already built
and never generalised ([`08-verification.md`](08-verification.md) § 3):

- **a denominator assertion** — the count of changed files it classified equals
  the count `git diff --name-only` reports, so a path it fails to parse reds the
  gate instead of silently passing (§ 3.1's F-003 pattern, which exists in
  exactly one file today);
- **a negative control** — a fixture PR that touches a forbidden path must fail
  the gate in the same run, so the gate cannot go quiet;
- **an expiry on every `cross_cutting` entry** — § 4.4.

**Why a diff-shaped gate rather than a code-shaped one:** the property being
enforced is *locality of change*, which is a property of a change and not of a
tree. A tree-shaped checker can tell you `features/x/` imports something it
should not; only a diff-shaped one can tell you that adding a feature required
editing nine other files. `superbot`'s `new_subsystem.py` is the closest existing
instrument and R3-D11 names its limit exactly: it checks **one** key, passed by
hand, with no `--all` mode and no test that iterates the 59 cog modules — *the
executable integration standard is never swept.*

### 4.4 · The expiry rule, applied to every list

**Every allowlist, exemption, baseline and `cross_cutting` entry carries a reason
and a date, and the checker fails on an expired one and on a row that no longer
matches anything.**

This is not a new idea either; it is `superbot-next`'s, applied to **2 of the 10
checkers that carry exemptions** — `check_settle_once.py:629-637` and
`check_money_race.py:610-616`, both emitting `"STALE-ROW … never let an excuse
outlive its reason"`, with `grep -rln "STALE" tools/*.py` returning exactly those
two files as the positive control
([`08-verification.md`](08-verification.md) § 3.4). It goes in the checker
**template**, so it is present by construction and opting out is what takes
effort.

Its target is measured: **131 exception entries across six files plus 55
`known_violations`** in `superbot` (§ 4.1), and the sharpest single instance is
M4-D1's `_ACK_UNCOVERED_TOOLS` — a one-element allowlist whose one element is the
only write-capable tool in the catalogue.

---

## 5 · The portability exercise

### 5.0 · Why a claim is not enough

OD-19 is a requirement, not an aspiration: *"I should be able to add exiting cogs
to it on demand, or be able to slightly alter an existing cog so that it works
with this bot."* Both predecessors claim portability. `superbot`'s is coarse and
broad — any cog, data-owning or not, can be dropped from `INITIAL_EXTENSIONS` or
`!cog unload`-ed, because it is in-tree. `superbot-next`'s is fine and narrow —
hash-pinned, jointly compiled, collision-checked, out-of-tree only, **and fenced
against the data half** (I-10). Neither claim survives contact with a specific
cog, which is why this section takes five.

**One fact should be held throughout, because it changes the question.**
Portability between these two architectures is not hypothetical: R6 found **54**
`disbot`↔`sb` file pairs above 0.55 similarity and **8** at ≥ 0.90
(`lane-claimed`, R6), and one pair is **byte-identical** — re-verified here,
`disbot/utils/mining/capacity.py` and `sb/domain/mining/capacity.py` share md5
`64f1665a9fb83a940d95eca5b9492bf2`. Domain logic already moved unchanged. What
does not move is everything a cog touches *around* its logic, and that is exactly
what the contract governs.

**Method, so the numbers can be re-run.** For each cog: an AST scan of its module
for imports rooted in `{services, core, utils, views, governance, cogs}`, split by
whether the `import` node sits at module level or inside a function body; a
transitive closure over the same roots, computed twice — once following only
module-level imports, once following every import node; migrations matched by
filename; tables by `CREATE TABLE` over `disbot/migrations/*.sql`;
touch-points by running `scripts/new_subsystem.py check` with a stub `discord`
package on `PYTHONPATH` and reading the **real** exit code, never `$?` after a
pipe.

**The closure figures are an upper bound on what a port must carry and a lower
bound on nothing.** Importing a package `__init__` pulls whatever that package
re-exports, so a closure counts *reachable* modules, not *required* ones. They
are comparable to each other, which is the use they are put to here.

### 5.1 · `utility_cog` — the simple-utility class

| | measured |
|---|---|
| size | **725** lines · **15** commands · 0 listeners · 0 task loops |
| direct internal imports | **9** distinct (**8** module-level, **1** function-body: `views.profile`) |
| transitive closure | **124** files module-level · **159** whole-AST |
| data | 0 migrations by filename · 0 tables named `utility*` · no `SubsystemSchema` |
| registration | key `utility` present; **11 of 11** touch-points OK, `new_subsystem.py check --key utility --cog UtilityCog --panel-command utilitymenu` → **REAL EXIT=0** |

R3-D4 calls this *"the most portable cog sampled"*, and it is. **It still drags
124 modules behind it at module level.** The single line
`from core.runtime.permission_checks import …` is the one R3 traced through a
real traceback into `core.runtime → core.resources → role_service →
governance/__init__ → governance/cleanup → governance/resolver` and out to env
config (`lane-claimed`, R3-D4).

**What must change under the contract:**

1. **The cog class disappears.** 15 commands become 15 `CommandSpec` rows with
   `HandlerRef`s; the handlers become plain functions over a typed request
   context rather than methods over `commands.Context`. Mechanical, per command.
2. **Permission decorators become declarations.** It already declares three
   capability strings in `SUBSYSTEMS` (`utility.info.server`, `utility.info.user`,
   `utility.tool.ping`) as *metadata* while the decorator does the enforcing;
   under § 3.7 the declaration is the enforcement and the transitive pull into
   `governance` goes with it.
3. **`views.base` / `views.navigation` / `views.hub_children` go away.**
   Navigation is engine-injected (§ 2), and child rendering is a framework
   property (§ 3.8).
4. **`views.profile` is the one real coupling.** A function-body import into
   another feature's view — a cross-feature call that under the contract is
   either a declared dependency on that feature's published operation or a route
   to its panel. It is a design decision, not a rename.
5. **`!remind` is a rewrite, not a port.** § 3.11: `asyncio.sleep` plus a bare
   `except: pass`, zero reminder tables. Under the contract a durable promise is
   a `jobs` row plus a store plus a boot reconcile, and the current
   implementation is a build error.

**Verdict: ADAPT.** Four fifths mechanical; one genuine coupling; one behaviour
the contract refuses. This is the class OD-19's *"slightly alter"* actually
describes.

### 5.2 · `starboard_cog` — the stateful-community class

| | measured |
|---|---|
| size | **329** lines · 1 command group + 5 subcommands · **2** listeners (`on_raw_reaction_add/remove`) · 0 task loops |
| direct internal imports | **5** distinct (**3** module-level, **2** function-body: `views.base`, `views.starboard`) |
| transitive closure | **86** files module-level · **152** whole-AST |
| data | **3** tables (`starboard_settings`, `starboard_entries`, `starboard_ignore_channels`) · **2** migrations (`083_starboard.sql`, `084_starboard_pr2.sql`) |
| supporting code | `services/starboard_service.py` **297** lines · `views/starboard/` 2 files, **282** lines |
| registration | **absent from `SUBSYSTEMS`**, from `KNOWN_PANEL_COMMANDS`, from `mutation_owners.yaml`, from `settings_keys/`, and it has no `schemas.py` — all re-derived. `new_subsystem.py check --key starboard --cog StarboardCog --panel-command starboard` → **REAL EXIT=1**, *"6 touch-point(s) missing"*: `registry-entry`, `panel-command`, `help-hook`, `surface-map-row`, `command-map-section`, `navigation-map-row` (R3-D1 reproduces exactly) |

**This is the row that proves the contract's hardest requirement.** A live
production feature with three tables, two migrations and its own config panel is
invisible to the registry that governance resolves policy against, invisible to
the settings hub, and invisible to the help menu — and the repo's guard for
exactly this reports `0 GAP`, because the guard's population is the registry
(§ 3.6). On the other side, `superbot-next` *does* model starboard properly —
`sb/manifest/starboard.py` declares 6 commands, panels, and **two stores** — and
that manifest is therefore one of the **29 of 49** that its own plugin contract
refuses (I-10).

**What must change under the contract:**

1. **It ships its schema.** `stores` + 2 namespaced `migrations` +
   `data_invariants`. Under § 3.5 this is what an out-of-tree feature is allowed
   to do; under `superbot-next`'s v1 fence it is precisely what it may not.
2. **Its two listeners become `subscriptions`** on typed gateway events, so the
   reachability and journey layers can enumerate and drive them. Today they are
   `@commands.Cog.listener()` methods no registry can see.
3. **Its settings become a `settings` facet** — channel, threshold, self-star,
   ignore list — and the settings hub renders them with no UI code, which is
   `superbot`'s own 19-consumer `SubsystemSchema` pattern applied to the feature
   that most obviously needed it and never got it.
4. **Its identity gap closes by construction.** There is no separate registry to
   be absent from, so the six missing touch-points cannot exist.
5. **The reaction → entry path gets an effect test.** Layer 6: mutate the state,
   re-read, assert the row and the audit verb.

**Verdict: PORTS WITH ITS DATA — under this contract, and under neither
predecessor's.** It is also the cheapest possible demonstration that the
requirement in § 3.5 is not theoretical.

### 5.3 · `server_management_cog` — the server-management class

| | measured |
|---|---|
| size | **101** lines · **2** commands (prefix + slash) · 0 listeners · 0 task loops |
| direct internal imports | **3** distinct, all module-level |
| transitive closure | **94** files module-level · **268** whole-AST |
| supporting code | `views/server_management/` 3 files, **822** lines |
| data | 0 migrations by filename — **and see the null below** |
| registration | **11 of 11** touch-points OK, `new_subsystem.py check --key server_management --cog ServerManagementCog --panel-command servermanagement` → **REAL EXIT=0**; a declared child of the `admin` hub, which hand-rolls its buttons and gets **6 of 6** right (I-14) |

Its own docstring is the finding: *"A thin command host … The cog holds **no
domain logic** — every action routes into an existing manager inside the hub
view"* (`disbot/cogs/server_management_cog.py:1-16`). The cog is already the
right shape. **The weight is 822 lines of view code that mixes routing, rendering
and privileged mutation**, and the module-level closure of 94 against a whole-AST
closure of 268 says most of what it reaches, it reaches lazily.

**What must change under the contract:**

1. **The cog file disappears entirely** — two `CommandSpec` rows and a
   `PanelSpec`. This one really is trivial.
2. **Each "manager inside the hub view" becomes a declared `operation`** with a
   capability, a risk class, an idempotency key and an audit verb (§ 3.4, § 3.7).
   This is the work, and it is not mechanical: today an operator action's
   authority is a decorator on a callback and its audit is whatever the manager
   happened to call.
3. **Risk classes make it AI-addressable.** It is the feature class [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s
   pipeline is aimed at — a moderator-facing operator surface where a typed
   verdict may propose and only a typed operation may act. Which risk classes may
   auto-act is **OD-F**, not this file.
4. **Reachability from the canonical entry point.** This is the class nearest the
   journey both bots lose (I-13). It must be a first-class destination in the
   route graph, not a panel behind a posted message.

**Verdict: the shell ports in an afternoon; the 822-line view is a rewrite
against § 3.4.** Stated plainly because a portability claim that counts only the
cog file would score this feature as trivially portable and be wrong by an order
of magnitude.

**Honest null, carried from R3's own list and not resolved here:** *"I could not
count DB tables for `utility_cog` and `server_management_cog`. Both matched 0
migration files by filename, but they may read or write shared tables through
`utils/db`, which I did not trace."* The 0-migration figure for both is a
filename match, not a data-coupling measurement, and § 5.6's scoreboard carries
that caveat rather than hiding it.

### 5.4 · `fishing_cog` — the game/content class

| | measured |
|---|---|
| size | **446** lines · **20** commands · 0 listeners · 0 task loops |
| direct internal imports | **6** distinct, all module-level |
| transitive closure | **127** files module-level · **189** whole-AST |
| data | **5** tables (`fishing_bait`, `fishing_catch_log`, `fishing_energy`, `fishing_rod`, `fishing_venue`) · **7** migrations by filename |
| supporting code | `views/fishing/` 11 files, **2,324** lines · `services/fishing_workflow.py` **1,151** lines · a `utils/fishing/` package |
| registration | key present, child of the `games` hub; **13 of 13** touch-points OK → **REAL EXIT=0**. No `SubsystemSchema` — so, like starboard, its settings are not in the settings hub |
| cross-feature | imports `game_xp_service` — the shared cross-game progression track |

**Two structural facts decide this one.** First, `superbot-next`'s `fishing`
manifest declares `stores`, so it is another of the 29 that its plugin contract
refuses (I-10). Second, `fishing` appears in **two** of the 8 mutual subsystem
pairs I-22 found in `superbot-next`'s domain graph — `('fishing','games')` and
`('fishing','mining')` — and **all 8 are invisible at module level**: 296
cross-subsystem `sb.domain` imports split **28 module-level (9.5 %) / 268
function-body (90.5 %)**, with 0 mutual pairs at module level and 8 in the union
graph. The clean DAG is a property of the census, not of the design.

**What must change under the contract:**

1. **Schema ownership**, as § 5.2 — 5 stores, 7 migrations, namespaced.
2. **The `game_xp_service` edge is inverted or declared.** Under the contract it
   is either a declared dependency on the progression feature's published
   operation, or — better, and the evidence points this way — an event the
   fishing feature emits and progression subscribes to. `superbot` already has
   the vocabulary: `game_xp.awarded` and `game_xp.level_up` are two of the 47
   `KNOWN_EVENTS` members.
3. **The cycles must break or be declared.** I-22's rule is a contract obligation
   here: **the successor's import guard walks the whole AST, counts function-body
   imports as real edges, and fails on cycles** — otherwise *"clean architecture"
   means "we moved the imports."* `superbot`'s own checker knows this and has a
   `--report-lazy-imports` mode that raises its findings from 1 to **137**, and
   **CI never passes the flag** (R3-D2; the 1-warning strict run and the 137-warning
   lazy run are both `lane-claimed`, R3 method note, and I-17 re-derived the
   `views→cogs` = 1 half).
4. **20 commands become one grouped tree** with the prefix surface as a declared
   alias ([`05-product-definition.md`](05-product-definition.md) § 3.1).
5. **Settings join the hub** by declaring the facet.

**Verdict: the contract carries it; the cycles are the work.** This is the row
that tests *"able to grow indefinitely"*, because a content feature is exactly
the thing that accretes cross-references to other content features.

**And a scope note that is not this file's to settle.** Fishing is on the
2026-08-21 exclusion list and OD-16 already rules that casino/economy/BTD6 and
unrelated content do not transfer. Whether fishing ships is
[`12-owner-decisions.md`](12-owner-decisions.md) **OD-D**. **Whether the contract
could carry it is this file's question, and the answer is the exercise above** —
which is the useful reading either way, since the class is what matters, not the
fish.

### 5.5 · `ai_cog` — the AI-integrated class

| | measured |
|---|---|
| size | **796** lines · 2 commands + 1 group · 0 listeners · 0 task loops |
| direct internal imports | **12** distinct — **4** module-level, **8** function-body |
| transitive closure | **10** files module-level · **302** files whole-AST |
| data | **8** `ai_*` tables · **10** migrations by filename |
| supporting code | `core/runtime/ai/` **12** top-level files, **3,494** lines, of which `natural_language_stage.py` is **1,662** (**48 %**) · **24** `ai_*.py` services · `views/ai/` 21 files, **3,542** lines |
| registration | key present, child of the `admin` hub, has one of the 19 `SubsystemSchema`s; **1 of 12** touch-points missing → **REAL EXIT=1**: `ai` is absent from `KNOWN_PANEL_COMMANDS`'s 22 rows while `SUBSYSTEMS["ai"]` declares `entry_points: ["ai", "aimenu"]` |
| load-time side effects | **4** registries at `cog_load`; **1** undone at `cog_unload` |

**The 10-versus-302 closure is the sharpest single measurement in this exercise.**
It is I-22's finding at the cog scale: a module-level census of `ai_cog` sees ten
files, and the code actually reaches three hundred and two. Any layer rule, any
portability estimate and any "this cog is self-contained" claim built on the
first number is measuring the placement of `import` statements.

**The registration asymmetry is the second.** `cog_load` registers into the
schema registry, `message_pipeline`, `interaction_router` and
`response_renderer_registry`; `cog_unload` can undo one of them. The source says
why, verbatim: *"`interaction_router` has no `unregister()` API; registrations
are process-lifetime"* (`disbot/cogs/ai_cog.py:308-311`), and again at `:353-356`
— *"We cannot remove the 'ai' prefix here."* R3 dropped this as a row for want of
a user-visible failure, and for a *feature contract* it is central: **a host that
cannot unload a feature cannot load a second version of it**, and a hot reload
leaves a live handler behind.

**What must change under the contract:**

1. **`ai_tools` is the whole point of the row.** § 3.12: `superbot` has **0**
   per-cog tool hooks (re-derived, with the `superbot-next` positive control) and
   a 2,719-line central `ai_tools.py`; `superbot-next` built the registry and
   shipped **8** rows from one call site, all read-only. The successor's feature
   declares its tools in its manifest, with a floor asserted in the same run.
2. **The write path is already designed and it is `superbot`'s.**
   `open_support_ticket` — one action tool of 36, which does not write: it emits
   `ticket.open_requested` so a human clicks, and the audited mutation service
   writes the row (M4-S3, `lane-claimed`). The contract adopts it as the general
   shape: **an AI tool returns a typed verdict; a declared operation acts.**
3. **Registration becomes declarative.** Four imperative registries collapse into
   facets the host reads. Unload becomes trivial because there is nothing to
   undo — which is the property `superbot-next` lost on purpose and recorded as
   final (R3-D8: the Cog Manager's Load/Unload/Reload buttons wired to a
   pending_handler stating the capability does not exist).
4. **`natural_language_stage.py` does not come.** At 1,662 lines it is 48 % of
   the package and it owns `AIScope` derivation, so M4-D10's scenario is exact:
   *"a rebuild session tries to take the AI platform without the Discord
   conversational stage"* and finds scope derivation inside it. Under the
   contract, scope derivation is a kernel authority seam
   ([`06-architecture.md`](06-architecture.md)) and the conversational stage is a
   feature like any other.
5. **The two-registry disagreement disappears** with the second registry
   (§ 4.2 rule 4).

**Verdict: the platform ports; the cog does not.** And the platform's provenance
is worth restating because the 2026-08-21 plan had it backwards: the
provider-neutral gateway is **`superbot`'s** design — `superbot-next`'s own
`sb/kernel/ai/gateway.py:1-6` says *"Ported from shipped
`disbot/core/runtime/ai/gateway.py`"*, and **24 of 30** files in `sb/kernel/ai/`
name a `disbot/` source in their first twelve lines (I-4, I-18). The successor is
porting it a second time, and the `ai_tools` facet is what makes the third time
unnecessary.

### 5.6 · The scoreboard

| cog | class | lines | direct imports (mod / fn) | closure mod / full | owns data | touch-points | verdict | the part that is **not** mechanical |
|---|---|---|---|---|---|---|---|---|
| `utility_cog` | simple utility | 725 | 8 / 1 | **124 / 159** | no¹ | 11 of 11 ✓ | **ADAPT** | the `views.profile` cross-call; `!remind` is a rewrite |
| `starboard_cog` | stateful community | 329 | 3 / 2 | 86 / 152 | **3 tables, 2 migrations** | **6 of 11 missing** | **PORTS WITH ITS DATA** | nothing, once § 3.5 exists — and impossible without it |
| `server_management_cog` | server management | 101 | 3 / 0 | 94 / **268** | no¹ | 11 of 11 ✓ | **SHELL PORTS, VIEW REWRITES** | 822 lines of view mixing routing, rendering and privileged mutation |
| `fishing_cog` | game / content | 446 | 6 / 0 | 127 / 189 | **5 tables, 7 migrations** | 13 of 13 ✓ | **CARRIED, CYCLES ARE THE WORK** | 2 mutual subsystem pairs visible only in function bodies; the `game_xp` edge |
| `ai_cog` | AI-integrated | 796 | 4 / **8** | **10 / 302** | 8 tables, 10 migrations | 1 of 12 missing | **PLATFORM PORTS, COG DOES NOT** | 4 load-time registries with 1 unregister; `AIScope` inside a 1,662-line stage |

¹ *0 migrations by filename; DB coupling through shared `utils/db` modules was
not traced (§ 5.3's null).*

### 5.7 · What the exercise forces into the contract

Four requirements, each one a cog above rather than a principle:

1. **An out-of-tree feature must own data.** `starboard` and `fishing` are on the
   wrong side of `superbot-next`'s `HOST_ONLY_FACETS` fence, together with 27
   others (I-10). Without § 3.5, OD-19 fails for **59 %** of the successor's own
   feature classes before a single cog is ported.
2. **Registration must be declarative, never imperative.** `ai_cog`'s four
   registries and one unregister are what makes unload impossible; declarative
   facets make it free.
3. **The import guard walks the whole AST and fails on cycles.** `ai_cog` at
   10 module-level versus 302 whole-AST, and `fishing` in two mutual pairs that
   are invisible at module level, are the same defect at two scales (I-22). A
   layer rule with a documented bypass is a layer rule both repositories took.
4. **A feature declares its AI tools.** Zero per-cog hooks in `superbot`, one
   call site with eight read-only rows in `superbot-next`, and the production
   bot's only audited write tool lost in transit (I-11, M4-D6). OD-16's *"AI
   given meaningful freedom from the first slice"* is a manifest facet or it is
   nothing.

**And the counterweight, because the exercise is not a case against porting.**
The most portable cog sampled needed one design decision and one rewrite; the
least portable was still 796 lines sitting on a platform that has already been
ported once, successfully, by hand. Portability here is real and it is bounded by
*what a cog touches around its logic*, which is the entire subject of §§ 3–4. One
domain module has already crossed these two architectures **byte-identically**
(§ 5.0).

### 5.8 · Honest nulls

- **Neither bot was observed running.** Both clones are read-only, `discord.py`
  and `asyncpg` are absent (stubbed to run the checkers), and there is no token
  or Postgres here. Every claim above is source-read at the pins.
- **The closures bound reachability, not necessity** (§ 5.0 method). They are
  comparable to one another, which is what they are used for.
- **DB coupling for `utility_cog` and `server_management_cog` is unestablished**
  (§ 5.3). Their portability scores understate data coupling by an unknown
  amount.
- **"What must change" is a design judgement against a contract with no
  implementation.** The measurements underneath each row are checkable; the
  transformation is falsifiable only by building it, which is
  [`09-roadmap.md`](09-roadmap.md)'s job and not this file's.
- **No effort estimate is given, in hours or in lines.** Nothing in this evidence
  base supports one, and this package has already recorded what happens when a
  number is published on an instrument that could only return the answer it
  returned (I-18, I-20, I-22).
- **`check_settings_reachability`'s `19 reachable · 3 exempt · 0 GAP` was not
  re-run here** (`lane-claimed`, R3-S3). The three facts it is used against —
  19 `schemas.py` files, starboard's absence from the registry, starboard's
  absence from `settings_keys/` — were each re-derived independently.

---

## 6 · What this file routes to the owner

Nothing here is an implementation choice with a defensible default; those are
decided above with reasons, per `docs/intent.md` § 6. Three questions genuinely
change the contract's shape and belong to him:

| routed to | what this file needs from it | what it changes here |
|---|---|---|
| **OD-D** — which community features are core, optional, or gone | the value of `tier` for the middle set (`xp`, `karma`, `leaderboard`, `counting`, `starboard`, `community_spotlight`, `ticket`, polls, reminders) | a `core` feature's schema joins the core migration set — a one-way door; an `optional` one exercises § 3.5 under real load, which is the only way to find out whether the extension contract works |
| **OD-F** — how much authority the AI may hold on day one | which risk classes in § 3.7 may auto-act after shadow mode | if it is more than low-risk-reversible, § 3.14's effect assertion moves from important to load-bearing in slice one |
| **OD-A** — one server or many | whether `settings` scope is guild-first and whether `wizard_sections` is a required facet at all | one server drops the first-run configuration surface and most of what the `wizard_sections` facet exists for |

The recommended defaults in those rows are already written and are sufficient to
proceed: none of the three blocks specifying the contract, and each has been
adopted provisionally where this file needed an answer to be concrete.

---

## 7 · The one-page version

A capability in the successor is **one directory, one manifest, one key**. The
manifest declares identity, placement, routes, panels, journeys, capabilities,
operations, stores, migrations, invariants, settings, events, subscriptions,
jobs, AI tools, metrics and audit verbs. **Everything else is derived**: the help
page, the parent's button, the Back/Home links, the settings section, the event
catalogue, the schema, the tool list, the docs rows, the estate index.

A feature's pull request touches its own directory and the regenerated snapshot.
`check_feature_locality` reds on anything else, and every cross-cutting exception
carries a reason and an expiry.

Every obligation has a gate; every gate declares its population and asserts a
floor over the shipped artifact; every population-walking gate ships a negative
control that fails when the population is empty. The measured reason for all
three clauses is in [`08-verification.md`](08-verification.md) § 1, and the
measured reason for the derivation rule is that adding one ordinary feature to
`superbot` today means fourteen coordinated touch-points, eight central code and
configuration files, four documents, and
a growing share of 131 exception entries — while its successor's answer to the
same problem fences the data-owning majority of its own product out of the
extension mechanism it built.
