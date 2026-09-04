# Independent findings — measured by the session itself, not by the fleet

> **Status:** `reference` — measurements, each with the command that produced it.
>
> Every row here was produced by a command run in this session against the pinned
> clones (`superbot` @ `5e3a667b`, `superbot-next` @ `d5f66dc2`), at
> 2026-09-04T11:52Z–13:30Z. They are separate from the fleet's rows so that the
> fleet's verification lane cannot be credited with confirming them.

## I-1 · The prior audit's panel figures reproduce EXACTLY at the current pin — `MEASURED`

Parsing `superbot-next/manifest.snapshot.json` (49 subsystems, 314 panels):

| metric | this session | 2026-08-05 audit |
|---|---|---|
| panels total | 314 | 314 |
| panels with zero `actions` | **153 (49 %)** | 153 (48 %) |
| `help` panels with zero `actions` | **60 / 66** | 60 / 66 |
| buttons / selectors declared | 640 / 130 | 640 / 130 |

A stricter reading — zero `actions` **and** zero `selectors` — gives 115/314 (37 %)
and help 50/66, so the audit's number counts *buttons* and is the right one to quote.
The mechanism is visible in the snapshot: `sb.help.sub_games` carries
`"actions": []` with a body of `{"text": "4 command(s), generated from the games manifest."}`
plus `{"provider": {"$ref": "provider:sb.panels.help_cmds_games_0"}}` — text and a
provider reference where a launcher should be.

## I-2 · superbot-next's navigation-completeness golden is structurally incapable of arming — `MEASURED`

`tests/unit/navigation_golden/test_navigation_completeness.py:` the suite the docstring
calls *"the golden proper"* is:

```python
def test_navigation_completeness_golden(self):
    """THE golden: every registered node reachable, Back+Home injected
    and bound, re-render survives. Green over the empty registry today;
    arms as bands register panels."""
    report = asyncio.run(walk_navigation(_ctx(), subsystem_hubs={
        "economy": "main", "hub": "main"}))
    assert report.ok, report.problems
```

`sim/navigation_walk.py:85-102` builds `inventory = panel_inventory()` and
`roots = set(_HUBS.values())` from the module-level panel registry. The suite's own
`conftest.py` declares an **`autouse=True`** fixture that calls
`clear_panels_for_tests()` before every test, and `sb/kernel/panels/registry.py:177-180`
is `_PANELS.clear(); _STATIC_TABLE.clear(); _HUBS.clear()`.

So `inventory` is `{}`, `roots` is `∅`, `reachable` is `∅`, `problems` is empty and
`report.ok` is `True` — for every possible state of the product. **The docstring's
"arms as bands register panels" cannot happen**: no band can register into a registry
the autouse fixture empties at the start of each test.

This is the single sharpest artifact in the review. superbot-next did **not** fail to
think of reachability. It built the walker, and pointed it at a population that is
empty by construction in the venue where it runs — while the compiled manifest, in the
same repo, holds the 314 panels and 153 dead ends that walker was written to find.

## I-3 · superbot-next's headline layering claim is TRUE but UNENFORCED — `MEASURED`

AST scan of every module-level import under `sb/kernel/`:

- `sb.kernel` → `sb.domain` module-level imports: **0**
- `sb/domain` files importing `sb.kernel`: **234**

The direction is perfect. But **no checker enforces it.** This is an absence claim, so it
carries its positive control (TRAP-003): the same query form, run against `superbot`, finds
`scripts/check_architecture.py` — the query works. And the claim does not rest on the query:
**all 27 `tools/check_*.py` files were enumerated and read by their own docstrings**, and none
is an import-direction or layer guard. There is no `tests/architecture/` directory either.

**superbot, by contrast, enforces layering mechanically**:
`architecture_rules/layers.yaml` declares the allowed directions
(`cogs → services, core, views, governance, utils` · `views → services, core, utils` ·
`services → utils, core/events` · `governance → utils, core` · `core → utils` ·
`utils → stdlib, discord`) and `scripts/check_architecture.py --mode strict` runs
inside the **required** `Code Quality` check.

So the prior plan's line — *"Preserve from `superbot-next`: explicit layers **and
import-direction guards**"* — is a **reversal**. The guard is superbot's.
superbot-next has the property; superbot has the mechanism that keeps it.

## I-4 · The provider-neutral AI gateway is superbot's design, ported — `SOURCE-ENFORCED`

`superbot-next/sb/kernel/ai/gateway.py:1-6` says so itself:

> *"AI gateway (K10) — the single never-raises chokepoint for provider calls.
> **Ported from shipped `disbot/core/runtime/ai/gateway.py` @7f7628e1** onto the
> kernel seams."*

The two pipelines are the same eight steps in the same order (admission/flags →
safety → redaction → routing → provider call under `wait_for` → metrics → parse →
degraded-never-raises), with the same three providers
(`AnthropicProvider`, `OpenAIProvider`, `DeterministicProvider`).

Consequence for the review: "provider-neutral AI gateway" appears on the
`superbot-next` side of the prior comparison table. It is **production-proven
superbot code**. Attribution matters here because it changes which repo the
successor should treat as the donor for this contract.

## I-5 · The capture-world convention is ~30× wider than its formal label — `MEASURED`

The 2026-08-05 audit reported **4** files carrying the literal label
`CAPTURE-WORLD LITERAL` and **34** mentioning "capture world", and named its own
limit: *"an unlabelled instance is invisible to this method."*

Measuring the **convention's own vocabulary** rather than its formal label —
`capture.world | honest successor | successor read | shipped verbatim |
golden.pinned | pinned literal | the oracle carried | goldens pin` — gives, at the
current pin:

| phrase | files in `sb/` | occurrences |
|---|---|---|
| `CAPTURE-WORLD LITERAL` | 4 | 4 |
| `capture world` | 41 | 121 |
| `shipped verbatim` | 44 | 87 |
| `golden-pinned` | 52 | 81 |
| `goldens pin` | 41 | 62 |
| `pinned literal` | 9 | 12 |
| `not armed` / `isn't armed` | 8 / 3 | 11 / 4 |
| **union** | **137 of 634 `sb/` files** | — |
| **union, `sb/domain` only** | **116 of 382 (30 %)** | — |

**This is a candidate set, not a defect count.** "golden-pinned" can legitimately
describe a rendering string that should be constant. What it establishes is that the
convention that produced the four labelled defects was the *house style of 30 % of the
domain layer* — which moves the audit's honest null from unknown to bounded, and makes
"were the four an unlucky sample?" answerable rather than rhetorical.

**A mechanical name-based sweep does NOT work.** An AST scan for module-level literals
whose names describe program state (`_COGS`, `COMMAND_NAMES`, `SUBSYSTEMS`, `*_count`,
`registry`, `roster`, …) returned 12 hits in `sb/domain`, all read by hand: **1 true
positive** (`_COGS`, already labelled) and 11 false (`_SUBSYSTEM = "ai"` identity
strings, `_installed = False` boot flags, `_tables: dict = {}` empty runtime
registries, BTD6 power constants). **Precision 1/12; retired.** The audit's proposed
§ 6 sweep — *"every module-level literal in `sb/domain/` that should be a runtime
read"* — is not mechanizable by name and needs semantic reading.

## I-6 · superbot has the exact test pattern that would have caught superbot-next's failure — applied to 2 of its 8 hubs — `MEASURED`

`tests/unit/views/test_games_hub_view.py` does not check panel *shape*. It instantiates
the real `GamesHubView` and asserts over `view.children`:
`test_view_renders_one_game_hub_button_per_visible_child` ·
`test_every_hub_button_is_actionable_not_disabled` ·
`test_no_placeholder_or_coming_soon_labels` ·
`test_button_fails_closed_when_subsystem_invisible` — and drives each button's real
callback against a stubbed `Interaction`, classifying by which response method was
awaited.

That is precisely *assert over the rendered artifact, not over a model of it*.

The hub registry declares **8 hubs**: `games`, `btd6`, `project_moon`, `economy`,
`moderation`, `community`, `utility`, `admin`. Hub-view test files of this shape exist
for **`games` and `community`** — **2 of 8**. There is no `test_moderation_hub_view`,
no `test_admin_hub_view`, no `test_btd6_hub_view`, no `test_economy_hub_view`, no
`test_project_moon_hub_view`, no `test_utility_hub_view`.

The shared child-discovery seam (`views/hub_children.py`, whose docstring records that
it replaced three hand-rolled copies) has **3 consumers** — games, community, utility.
The other five hubs hand-roll their child lists.

**The successor's conclusion writes itself:** the pattern is right and the coverage is
by discipline. Make it universal *by construction* — one hub renderer and one generated
contract over every registered hub — rather than one hand-written test per hub that
somebody remembers to add.

## I-7 · Both product trees are at the exact pins the 2026-08-21 plan reviewed — `MEASURED`

`superbot` `5e3a667b` and `superbot-next` `d5f66dc2` are unchanged since the GCB plan
was written 14 days ago. All **8** open `superbot` PRs are dependabot; `superbot-next`
and `spider-bot` have **0**. So nothing in either product tree has moved, and the
August evidence is re-usable *as evidence* — the thing that has moved is the owner's
verdict (2026-08-28: `superbot-next` is to be **remade**, the end state is **one** bot).


## I-8 · superbot-next's genuinely new contribution is its CHECKER SET, not its layer tree — `SOURCE-ENFORCED`

Enumerated: **27 `tools/check_*.py`**, each named by a spec clause, several wired into
the required `named-gates` workflow. Read by their own docstrings, the set contains
guards that have **no counterpart in `superbot` at all**:

| checker | what it guards | superbot equivalent |
|---|---|---|
| `check_config_usage` | no `os.getenv` outside `sb/kernel/config/` — one typed accessor | none |
| `check_migrations` | numbering + **immutability + checksum manifest** (57 migrations) | none |
| `check_namespace` + `check_symbol_shadowing` | string-registry collisions, symbol shadowing | none |
| `check_egress` | AST fence on send-egress | none |
| `check_money_race` / `check_settle_once` | the F-001/F-002 money-race class, settle-once | tests only, per-feature |
| `check_data_lifecycle` / `check_credential_lifecycle` / `check_rotation_due` | retention, erasure, credential N-1, rotation cadence | none |
| `check_cost_posture` | declaration-presence for cost | none |
| `check_metric_cardinality` | label-cardinality budget | none |
| `check_slash_cap` | the 100/25/1-nest Discord slash budget | none |
| `check_schema_growth` | schema-growth ledger | none |
| `check_doc_cites` | `file:line` citations in tracked markdown actually resolve | `check_docs.py` (hygiene, not citations) |
| `check_escape_hatches` | `sb/domain/<x>/ui/` modules unreachable from any registered ref | none |

All of these ran clean in this session (`EXIT=0` each for the five sampled).

**This inverts the usual framing.** The prior comparison credits `superbot-next` with
"explicit layers and import-direction guards" — the layer tree it has but does not
enforce (I-3). Its real, transferable, machine-enforced contribution is this checker
set: a habit of turning each named defect class into a stdlib-only AST gate with a
spec clause behind it. **That habit is the thing to preserve, not the folder shape.**

The two repos therefore donate *different halves of the same discipline*: `superbot`
donates the guards over the **rendered product** (reachability, actionability,
back-button, hub coverage); `superbot-next` donates the guards over the **invariants
of the system** (config seam, migration immutability, namespace, egress, lifecycle,
cost, cardinality). A successor needs both, and neither repo has both.

## I-9 · The EAP added almost NO code to `superbot` and 23 % of its documentation — `MEASURED`

Era split by each file's **oldest add commit** (`git log --diff-filter=A`, full clone,
6,391 commits — not the shallow-clone trap), against the EAP fortnight 2026‑07‑07 → 07‑21:

| | pre‑EAP (< 07‑07) | EAP fortnight (14 days) | post‑close | total |
|---|---|---|---|---|
| `disbot/**/*.py` ever added | **909 (100 %)** | **2 (0 %)** | 0 | 911 |
| `docs/**/*.md` ever added | 822 (76 %) | **245 (23 %)** | 8 (1 %) | 1,075 |
| `docs/**/*.md` still present | 624 | **183** | 7 | 814 |

*Method limits, stated:* `--diff-filter=A` attributes a rename as a new add, so both
"ever added" columns are upper bounds on distinct files; 814 present-by-add-path against
863 present-by-`find` is that gap. The era split is unaffected — a rename lands in the
era it happened, and no plausible rename volume moves 100 %/0 % or 76 %/23 %.

**Three things follow, and they reframe the debt narrative:**

1. **`superbot`'s code debt is entirely pre‑EAP, owner‑era, organic growth.** The
   autonomous program added *two* runtime files to it. When the owner says the repo is
   *"filled with too much history, too many trials and errors"*, he is describing
   ~11 months of his own feature accretion — **not** the thing the EAP did.
   So "the EAP damaged superbot" is not available as an explanation, and a successor
   that merely avoids the EAP's working style does **not** thereby avoid superbot's debt.
2. **The EAP's contribution to `superbot` was documentation volume** — 183 surviving
   files in 14 days, ~13/day. That is the half of the sprawl a cleanup can actually cut,
   and it is consistent with the owner's own line that the docs were *"especially true
   in /superbot **before** the EAP was announced."*
3. **`docs/AGENT_ORIENTATION.md` — the router he is describing — was created 2026‑05‑24**,
   six weeks before the EAP, and carries the tier vocabulary (`binding` / reference
   inventory / historical plan / how‑to‑work) that fleet‑manager's own boot file is a
   descendant of. **The quality baseline he names is a real, dated artifact, and it
   predates the program that is usually blamed.** It is a `PRESERVE_PATTERN` candidate
   in its own right, independent of any code.

And the mirror: **`superbot-next` is 100 % EAP-era.** The comparison is therefore not
"old code vs new code" — it is *eleven months of owner-directed organic growth* against
*fourteen days of autonomous construction against a byte-parity oracle*. Every
conclusion about which repo's habits to inherit has to carry that asymmetry.

## I-10 · superbot-next's plugin contract cannot host 29 of its own 49 subsystems — `SOURCE-ENFORCED`

OD-19 makes cog portability a **requirement**: *"I should be able to add exiting
cogs to it on demand, or be able to slightly alter an existing cog so that it
works with this bot."* `superbot-next`'s answer is the out-of-tree plugin host
(`sb/app/plugin_host.py`) — entry-point discovery through the `sb.plugins` group,
hash-pinned in `plugins.lock.json`, compiled in one joint pass with the in-tree
manifests. The pinning and joint-compile discipline is genuinely good.

But the contract has a **facet fence**, in the source, as two constants:

```python
ALLOWED_FACETS: tuple[str, ...] = (
    "commands", "panels", "settings", "events", "capabilities",
)
HOST_ONLY_FACETS: tuple[str, ...] = (
    "stores", "data_invariants", "wizard_sections",
)
```

and the host rejects a plugin declaring any host-only facet:

> `"{dist}: manifest {key!r} declares the host-owned facet {facet!r} — v1 contract allows …"`

The docstring names the reason: *"migrations, S12 money lanes, and the G-19 setup
registry have no out-of-tree lane yet."*

**Measured against its own compiled snapshot** (49 subsystems):

| facet | subsystems declaring it |
|---|---|
| `stores` | **29** |
| `data_invariants` | 4 |
| `wizard_sections` | 1 |
| **union — ineligible to be an out-of-tree plugin** | **29 of 49 (59 %)** |

The 20 that *are* eligible are the stateless ones: `admin`, `automod`, `casino`,
`channel`, `community`, `counters`, `general`, `hermes`, `image_moderation`,
`inventory`, `leaderboard`, `logging`, `projmoon`, `security`, `utility`,
`ux_lab`, `welcome`, `blackjack`, `community_spotlight`, `four_twenty`.
Everything that owns data — `economy`, `moderation`, `roles`, `setup`, `xp`,
`settings`, `ticket`, `starboard`, `btd6`, `mining`, `fishing`, … — cannot be.

**So the rebuild's extension mechanism serves the stateless two-fifths of its own
product**, and precisely not the class the owner wants to port. A superbot cog
that owns tables (14 domains carry an `owner_module` + `db_module` in
`architecture_rules/mutation_owners.yaml`, against 45 `utils/db/*.py` submodules
and 104 migrations) has no lane.

Note the direction of the trade, because it is not one-sided: `superbot`'s
modularity is **coarser but broader** — any cog, data-owning or not, can be
dropped from `INITIAL_EXTENSIONS` or `!cog unload`-ed, because it is in-tree.
`superbot-next`'s is **finer but narrower** — hash-pinned, jointly compiled,
collision-checked, and out-of-tree only, with the data half fenced off.

**The successor's extension contract therefore has one hard requirement neither
repo meets: an out-of-tree module must be able to own data** — ship its own
migrations into a namespaced schema, declare its invariants, and contribute a
setup section — or cog portability fails for 59 % of the feature classes the
owner would want to bring.

## I-11 · The AI surface: a catalogue of 36 with one audited write became a registry of 8 game-trivia reads — `SOURCE-ENFORCED`

**`superbot`** — `disbot/services/ai_tool_catalogue.py` carries a `CATALOGUE`
dict of **36 tools** (AST count of the literal). Its own comment marks the write
boundary:

> *"Support tickets — the one **action** toolset. `open_support_ticket` writes
> (it opens a ticket **through the audited mutation seam**), unlike every other
> catalogued tool, which is read-only."*

So the live production bot's AI is **read-only plus exactly one write**, and that
write goes through the same audited service path a button uses. **That is already
the contract a successor should adopt, and it is production-proven** — not a
design to invent.

**`superbot-next`** — `sb/kernel/ai/tools_catalogue.py` replaced the closed dict
with an open registry, and says so:

> *"ported from shipped `disbot/services/ai_tool_catalogue.py` **with the closed
> domain dict cut**: the shipped `CATALOGUE` hardcoded ~35 BTD6/server tool rows;
> here tools REGISTER (spec + metadata + handler factory) — domains bring their
> toolsets at their port band."*

The abstraction is better: authority is never widened (`min_scope` stays
authoritative), selection is deterministic and inspectable, grounding allowlists
are derived rather than hand-kept. But the **population**: there is exactly
**one** `register_tool(` call site in the whole of `sb/` —
`sb/domain/ai/tools.py:185` — iterating `_ROWS`, which holds **8 rows**:
`btd6_lookup`, `btd6_boss_lookup`, `btd6_power_lookup`,
`btd6_monkey_knowledge_lookup`, `btd6_round_composition`, `btd6_round_cash`,
`btd6_difficulty_cost`, `btd6_paragon_stats_at_degree` — every one a BTD6
factual read at `AIScope.USER`, **zero write-capable**.

**36 → 8, and the one audited write seam did not survive.** The port band that
was supposed to bring the server toolsets never came.

**And golden parity could not see it.** An unregistered tool produces no output,
so no golden covers it — the audit's *"absence is structurally invisible"*,
demonstrated a second time, in the subsystem the owner most wants strengthened
(OD-16: *AI given meaningful freedom from the first slice*).

This is the same shape as I-2 and § 2.4 of the root cause: **the mechanism
improved and the population collapsed, and nothing measured the population.**
The successor's rule follows directly — *a registry ships with a declared floor
and a test that asserts it* — and it is the same one line that fixes the
navigation golden.

## I-12 · The audit's "70 not-armed terminals across 17 subsystems" does not reproduce — and the tree is identical — `MEASURED`

First, the fact that makes this checkable: **`sb/` has not been touched since
2026-07-19** (`git log -1 -- sb/` → `efece51`, 2026-07-19 11:22:54 +0000; zero
commits touching `sb/` since 2026-08-01). The 2026-08-05 live audit therefore
read **the identical source tree** this session is reading at `d5f66dc2`.

The audit's § 3 table reports: *"'not armed' terminals — **70** across **17
subsystems** — grep of shipped copy."*

Measured here, repo-wide (all files, `--exclude-dir=.git`):

| pattern | occurrences | files |
|---|---|---|
| `not armed` | 19 | — |
| `n't armed` | 7 | — |
| union | **26** | **22** |
| — of which under `sb/` | 11 files | |
| distinct `sb/domain` subsystems | **9** (`ai`, `btd6`, `channel`, `cleanup`, `hermes`, `media`, `server_logging`, `settings`, `setup`) + `operator_spine.py` | |

Widening to neighbouring phrasings does not close the gap either: `this build`
= 32 occurrences in 18 files (5 domain subsystems); `honest refusal` = 17 in 10;
`port not armed` = 2 in 2; `not yet ported` and `not available in this build` = 0.
And the **compiled snapshot contains none of these strings at all** — panel body
copy sits behind `provider:` refs rather than inline — so "shipped copy" cannot
mean the snapshot.

**State this as what it is: a failure to reproduce, not a demonstration that the
figure is wrong.** The audit did not record its pattern, so a wider one may exist
that I did not construct. What can be said is that no pattern tried here reaches
70 or 17 against the same bytes, and the audit's own § 9 already files this
number as *"a grep of shipped refusal copy, not a click-through census"*.

**Why it matters, and the direction is the surprising part:** this correction
makes `superbot-next` look **better**, not worse. The refusal surface is a
material input to "how much of it actually works", and a reviewer carrying 70
into the rebuild decision is carrying roughly 2.5× the reproducible figure.

**And it is the right calibration note for the whole review.** The audit's
load-bearing measurements — 314 panels, 153 button-less, help 60/66, 640 buttons,
130 selectors — **reproduce exactly** at this pin (I-1). One softer number,
explicitly self-labelled as a grep, does not. That is a document to trust on its
measurements and to re-run on its greps, which is exactly how it asked to be
read.

## I-13 · The two-tap property, measured at last: from `help.*`, the rebuild's front door reaches NOTHING — `MEASURED`

The 2026-08-05 audit closed with this honest null (§ 9):

> *"The two-tap property was **not measured**, only the zero-button rate. Proving
> or refuting 'every feature is two taps from `!help`' needs the route table
> walked as a graph, which is the acceptance test proposed in § 4b, not a result
> reported here."*

[`reachability_probe.py`](reachability_probe.py) walks it. It is written the way
the successor's gate must be written — it **declares its population, asserts a
committed floor, and walks the shipped artifact** (`manifest.snapshot.json`)
rather than a runtime registry a fixture can empty.

```
POPULATION : every panel in the committed manifest.snapshot.json
             314 panels (floor 250, satisfied)
             200 DOWNWARD edges (button/selector/extra-route to another panel)
             278 edges including framework Back/Home up-links
             a 314-node graph needs >= 313 edges merely to be a tree
```

| entry set | roots | reachable | unreachable | max depth |
|---|---|---|---|---|
| **`help.*` panels** | 66 | **66 / 314** | **248** | **0** |
| `*.hub` / `*.main` | 37 | 107 / 314 | 207 | 2 |
| every panel a **command** routes to | 58 | 117 / 314 | 197 | 2 |
| **all three combined** | 133 | **185 / 314** | **129** | 2 |
| combined, **counting Back/Home up-links too** | 133 | 185 / 314 | 129 | — |

**The first row is the finding.** Walking from the help tree, **max depth is
zero**: the 66 help panels are 66 isolated nodes with no outgoing panel edge
between them. The old bot's product is *"the only command anyone ever needs is
`!help`, from there you can use every feature the bot ships, always 2 taps
away."* In the rebuild, **`!help` reaches nothing at all.** The 60-of-66
zero-button figure said the pages had no buttons; this says the front door is
not a door.

**Second, the structural fact that explains it.** 314 panels are wired by **200**
downward edges. A 314-node graph needs at least 313 edges merely to be a
*connected tree*. The navigation graph was never capable of being connected —
this is not a wiring gap someone forgot to finish, it is an artifact that was
never a graph. Adding Back/Home up-links raises the edge count to 278 and changes
reachability by **zero panels**, exactly as it must: an up-link points at an
ancestor you have already reached, so it can never introduce anyone to anything.

**Third, where the holes are.** From *all* entry points combined — help, every
hub, and every panel any command routes to — 129 of 314 panels are unreachable,
concentrated in the operator surface:

| subsystem | unreachable / total |
|---|---|
| **`setup`** | **39 / 40** |
| `utility` | 10 / 10 |
| `ai` | 10 / 27 |
| `cleanup` | 7 / 12 |
| `settings` | 7 / 13 |
| `general` | 3 / 3 |

`setup` at 39 of 40 is the one that matters most: **first-run onboarding is the
single most important operator journey, and 39 of its 40 panels cannot be reached
from any declared entry point.**

**And `superbot` fails the same journey differently — the difference matters, and
a first cut of this paragraph flattened it.** `superbot` *does* have a first-run
entry: `disbot/views/setup/launcher.py`'s `SetupLauncherView` carries seven
buttons including `_start`, `_repost_launcher` and `_dismiss`, posted on join with
a DM-the-owner fallback when no channel can be made. So setup is reachable — **from
a posted message, not from the navigation graph.** Once that message is dismissed,
cleaned up, or simply old, there is no route back: `"setup"` is not one of the 43
`SUBSYSTEMS` keys (AST-checked, with `moderation` as the positive control), so the
Help dropdown can never list it; `_AdminPanelView` carries 15 `@button` methods and
none is Setup; and `check_command_reachability.py:372` exempts every
operator/owner-tier command from the guard by construction, so nothing would ever
have flagged it. **The `_repost_launcher` button is the tell** — someone met this,
and the fix that shipped was a way to re-post the message rather than a route to
the flow.

So the honest form is not *"both bots lose setup"*. It is: **`superbot` reaches
setup only through an ephemeral out-of-graph message, and `superbot-next` reaches
39 of its 40 setup panels not at all.** Two different failures with one root —
**setup was never a first-class destination in either route graph** — and a
successor that fixes only one of the two mechanisms still ships a bot whose owner
cannot find setup after the first day.

### Honest nulls, and the first is load-bearing

- **"Unreachable" means unreachable IN THE DECLARED GRAPH, not proven unreachable
  at runtime.** Of 640 declared actions, **463 carry a `handler:` ref, 159 a
  `panel:` ref and 18 a `workflow:` ref** — and a `handler:` could render a panel
  programmatically without declaring a panel edge. The true runtime figure is
  somewhere between this and better. **It is nonetheless the right measurement
  for this architecture**, because the manifest's entire premise is that it
  declares the shipped surface: a panel reachable only through an undeclared jump
  is invisible to every generated help page, every reachability check and every
  audit — which is the defect, not an excuse for it.
- The entry sets use `panel_id` prefixes (`help.*`, `*.hub`, `*.main`) plus
  declared command routes. A hand-wired entry matching none of those and routed
  by no command would be missed; the combined row exists to bound that.
- The probe reads `actions`, `selectors[].options[].handler`, `selectors[].handler`
  and `navigation.extra_routes`. The positive control that makes the count
  trustworthy: **every one of the 640 action handlers resolves to a `$ref`** (zero
  non-ref handlers), and `layout.pages` was checked and holds **only** `rows` of
  action-id strings — a layout over actions already counted, contributing no
  edges. So no edge class is silently dropped.

## I-14 · `superbot`'s hub coverage: the shared seam guarantees it, hand-rolling gets it right 8 times in 15 — `MEASURED`

The pilot's two agents contradicted each other on `superbot`'s navigation: P1
found reachability CI-enforced with a mutation-tested guard, 0 orphans, max 2
clicks; P2 found the Moderation hub declaring 6 children and rendering none.
Both were right, because the guard checks a **model** of the hub registry and P2
opened the **rendered view**. This is that contradiction measured across all
eight hubs, by AST, rather than left as one agent's report.

**Declared:** `disbot/utils/hub_registry.py` — **8 hubs, 34 primary children**
(games 10 · community 7 · moderation 6 · admin 6 · economy 3 · utility 2 ·
btd6 0 · project_moon 0).

**Rendered:** three hubs use the shared child-discovery seam
(`discover_hub_children` / `HubChildButton`): **games, community, utility**.
Coverage is guaranteed by construction, and the guarantee is exactly as strong
as the function body — read, not assumed: `disbot/views/hub_children.py`'s
`discover_hub_children` is an **unfiltered** comprehension,
`[(name, dict(meta)) for name, meta in SUBSYSTEMS.items() if meta.get("parent_hub") == hub_key]`,
followed only by a deterministic sort. Every declared child is returned.

**One precision, because the caller adds a filter the seam does not.** The games
hub's own test is named `test_view_renders_one_game_hub_button_per_**visible**_child`:
the caller narrows the discovered set by **per-guild governance visibility**
before rendering. That is correct behaviour — a subsystem an operator disabled
should not offer a button — so the honest form of the guarantee is *every
declared child the viewer is permitted to see*, and the 19/19 below is a
**declared-coverage** figure, like every other row in the table.
**It is also a requirement on the successor's reachability gate**: the gate must
model per-guild visibility, or it will score a correctly-hidden subsystem as an
unreachable one and train its readers to ignore it. The other five hand-roll. Counting `@button`-decorated methods on
each hand-roller's view class:

| hub | declared | mechanism | children with a button | missing |
|---|---|---|---|---|
| `games` | 10 | **shared seam** | 10 (by construction) | — |
| `community` | 7 | **shared seam** | 7 (by construction) | — |
| `utility` | 2 | **shared seam** | 2 (by construction) | — |
| `admin` | 6 | hand-rolled, 15 buttons | **6** | — |
| `economy` | 3 | hand-rolled, 8 buttons | **2** | `leaderboard` |
| `moderation` | 6 | hand-rolled, **7 buttons, all actions** | **0** | all six |
| `btd6` · `project_moon` | 0 | — | — | — |

**27 of 34 declared children have a button on their parent hub; 7 do not** — the
six under `moderation` plus `economy`'s `leaderboard`.

`ModPanelView` is the whole story in one class: its seven buttons are
`warn_btn`, `timeout_btn`, `kick_btn`, `ban_btn`, `unban_btn`, `modlogs_btn`,
`clearwarn_btn` — every one an **action**, none a **route**. And five of its six
declared children (`automod`, `image_moderation`, `logging`, `proof_channel`,
`security`) have **zero** mentions anywhere under `disbot/views/moderation/`. A
server admin who opens *🛡️ Moderation & Safety* to switch on spam protection
gets a panel that can ban people and cannot reach automod.

### The finding is narrower and more useful than "hand-rolling is broken"

`admin` hand-rolls and gets **6 of 6 right**. So hand-rolling is not
automatically wrong — it is *unguaranteed*, and the failure rate is what matters:
**the seam is 19 for 19; hand-rolling is 8 for 15.** That is the argument for the
successor making child rendering a property of the framework rather than of the
hub author, stated as a measurement instead of a preference.

**And a correction to this session's own intermediate pass, kept because it is
the same error class the review is about.** A first cut measured coverage by
grepping each hub's view code for its children's registry names, and scored
`admin` at **2 of 6**. That was wrong: the button methods are `channels_btn`,
`uxlab_btn`, `diagnostics_btn` for children named `channel`, `ux_lab`,
`diagnostic`, so a name-match proxy misses them. It also scored the seam-using
hubs at 0–5 of their children — inverted, since a seam user *should* name none.
**The proxy measured naming and was read as measuring coverage**; only the AST
button count over the actual view classes settled it. Two of the three numbers a
proxy produced here were wrong in opposite directions, which is why the table
above is AST-derived and the proxy is recorded rather than quietly dropped.

## I-15 · The survival rule passed 98 % of the fleet's rows — because it was published to the agents that wrote them — `MEASURED`

**The number first.** Across the 13 lanes returned at 14:45Z: **110 strengths,
127 defects**. Applying the AGGREGATE rule from
[`CONTRACTS.md`](CONTRACTS.md) / [`survival_rule.py`](survival_rule.py):

| | raw | passes the rule |
|---|---|---|
| strengths | 110 | **108 (98 %)** |
| defects | 127 | **125 (98 %)** |

Exactly **two** strengths died — one `TEST-PROVEN` with `effect_asserted=false`,
one `documentation_only`.

**A rule that kills 2 of 237 is doing almost no work, and the cause is mine.**
`fleet-preflight` § 1b requires a fixture that dies and a fixture that survives;
mine passed (4 kill, 2 survive, exit 0). What it does **not** require, and what
this run needed, is a check that the rule still discriminates *on the real
population*. It does not — because the SHARED prompt block published the
predicate to the agents:

> *"THE SURVIVAL RULE your rows are scored against. Write rows that can clear it;
> do not inflate."*

**Publishing a filter to the population being filtered converts it from a filter
into a template.** The field distributions are consistent with that — 108 of 110
rows carry a non-empty `prevents_failure`, and `enforcement_locus` is `ci_check`
or `source_guard` on 95 of 110 — but *consistent with* is not *caused by*, so the
claim rests on a shape test rather than on plausibility.

**The discriminator: `consumers` piles up on the threshold.** The rule passes at
`consumers >= 2`. The distribution across all 110 strengths:

```
 1: ########                                           (8)   ← would die on this field
 2: ################################################## (50)  ← 45 %, the threshold itself
 3: ##########                                         (10)
 4: #####                                              (5)
 5: #######                                            (7)
 6: ########                                           (8)
 7: ######                                             (6)
 8: ###                                                (3)
 9-11: ####                                            (4)
>12:                                                   (9)
```

**45 % of rows sit on the minimum passing value**, with a clean taper on either
side. A genuine count of distinct call sites has no reason to cluster at two —
that is where a writer stops counting once two is known to be enough. And the
eight rows at `consumers: 1` are the other half of the evidence: every one
carries a non-empty `prevents_failure`, which is precisely the rule's alternative
branch. Agents that could not reach two reached for the escape the rule offers.

Both signatures are of a population written against a known predicate.

**This is not evidence the rows are bad.** Spot-checks hold: M9's escape-hatch
claim reproduces exactly (218 of 314 panels carry a non-null `renderer_override`;
`docs/planning/escape-hatch-baseline.json` is verbatim `"per_subsystem": {},
"total": 0`; `check_escape_hatches.py` → `clean`, EXIT=0). It is evidence that
**the survival rule cannot be cited as what filtered them**, which is what the
contract sheet claims it does.

### What is used instead

1. **The adversarial verification lane is the real filter**, not the rule. It was
   designed as a second pass and is now the first one that can actually remove a
   row. Its refutation rate is the number to report, and the survival rule's is
   not.
2. **A stricter cut the agents had no reason to target**, since the rule never
   read these fields together: `evidence_class` in
   {`PRODUCTION-PROVEN`, `LIVE-TESTED`, `SOURCE-ENFORCED`} **and**
   `enforcement_locus` in {`source_guard`, `ci_check`} **and** `consumers >= 2`
   **and** a named `prevents_failure` **and** a non-empty verbatim `quote`
   **and** a real `line_span`. That cuts **110 → 73 (66 %)** — a rate that
   discriminates. Its composition is also the more honest headline of this whole
   review: **`superbot` 40 · `superbot-next` 32 · `spider-bot` 1**, dispositioned
   `PRESERVE_PATTERN` 41 · `PRESERVE_BEHAVIOR` 26 · `PRESERVE_CONTRACT` 5 ·
   `ADAPT` 1.
3. **`guard_population` is the tell worth keeping.** The rule never read it, so
   nobody had a reason to fill it — and **86 of 110** rows did anyway. A field
   nobody was scored on, answered five times out of six, is better evidence the
   lanes engaged with the question than any field the rule touched.

### The generalisation, which is this run's own contribution to the method

The estate's `fleet-preflight` § 1 requires *"at least one fixture must die AND
at least one must survive"* and warns that *"a rule no fixture can kill will not
kill anything at scale."* This run satisfied that and still produced a vacuous
filter — so the skill's check is **necessary and not sufficient**, and the
missing half has a name:

> **Never publish the survival rule to the agents whose rows it scores.** If they
> must know the standard, give them the *evidence* standard (cite file:line,
> quote verbatim, count don't estimate, name the failure) and keep the
> *predicate* out of the prompt. Then measure the pass rate on the real
> population as well as on fixtures: **a rule passing ~98 % is not a strict
> rule, it is a rule the population was written against.**

That is the same defect the whole review is about, one level up: **a correct
instrument pointed at a population that was shaped by knowing the instrument.**
It belongs in `fleet-preflight` § 1 as a fourth check, and this session's
proposal for it is recorded here rather than shipped, since the kit is
owner-paced.

## I-16 · Four of R2's hardest claims, re-run by this session rather than relayed — all reproduce — `MEASURED`

Lane R2 (the vacuous-guard hunt) reported **19 of 77 executable guards
vacuous-capable by measurement**. Because the adversarial verification lane has
not run yet, and because I-15 established that the survival rule is not filtering,
its four most consequential claims were re-executed here directly:

| claim | command | result |
|---|---|---|
| the **required** Postgres concurrency leg passes with zero tests run | `python3 -m pytest tests/integration -q` | `14 skipped in 0.04s`, **EXIT=0** |
| the **required** in-process adapter e2e tier does the same | `python3 -m pytest tests/e2e -q` | `11 skipped in 0.04s`, **EXIT=0** |
| the navigation golden's roots are empty even in a booted process | `grep -rn "[^_]register_hub(" sb/` | **1** (the definition) · `tests/` → **3** |
| the escape-hatch gate scans a glob matching nothing | `ls sb/domain/*/ui/*.py` | **0 files** across **49** domain directories |

**All four reproduce.** Three consequences, and the first is the sharpest thing
either repo yielded:

1. **Two of `superbot-next`'s required CI legs are green over zero executed
   tests** — and they sit in `named-gates.yml`'s single job that provisions
   Postgres and the full runtime lock *precisely so they cannot skip*. The job's
   own comment says so. `pytest` exits 0 on an all-skipped run, and nothing
   asserts a collected-count floor. The 12 money-race regression files that exist
   to prove crash-safety are among the skipped. This is the population contract
   ([`../08-verification.md`](../08-verification.md) § 1) in its purest form: the
   assertion is right, the population is empty, and the exit code is 0.
2. **I-2 was correct and incomplete.** I found the navigation golden vacuous
   because its `autouse` conftest clears the registry. R2 found an *independent
   second* reason: `register_hub()` is never called in production at all, so
   `walk_navigation`'s root set is empty **in a fully-booted process too**. That
   refutes the docstring's *"arms automatically as port bands register real
   panels"* on its own terms — removing the conftest would not arm it. Two
   independent causes for one vacuity, and the deeper one is the one I missed.
3. **The escape-hatch ratchet does not merely under-count** (I-9's reading, that
   it counts tier-3 and misses tier-2's 218 panels). Its `sb/domain/<x>/ui/`
   sweep — the *"also red"* clause in its own docstring — globs **zero files
   across all 49 domain directories.** A required, `NO EXPIRY`, CODEOWNERS-flagged
   gate whose baseline is `{"per_subsystem": {}, "total": 0}` is scanning a
   directory shape the repository does not use.

**Status of the rest.** The other 15 of R2's 19, and every row from the other 14
lanes, remain **lane-claimed and unverified** until the adversarial refutation
pass runs. That distinction is now load-bearing rather than procedural: with the
survival rule not filtering (I-15), verification is the only filter this run has.

## I-17 · A lane count re-derived: 128, not 134 — and the rule this run now follows — `MEASURED`

Lane R3 reported *"134 `from cogs.<x>` import statements inside `cogs/`, all
fully legal under the rule."* Re-derived here by AST over `disbot/cogs/`:
**128 module-level `ImportFrom cogs.*` statements across 51 files.** A six-import
delta, and it is the difference between a textual grep and a parse — R3's figure
most likely counted function-body imports or matched a substring.

**The structural claim it supports is unaffected and confirmed.**
`architecture_rules/layers.yaml` gives
`cogs.may_import: ['utils', 'core', 'services', 'views', 'governance', 'cogs']` —
**`cogs` may import `cogs`**, so superbot's one CI-enforced architecture rule
cannot constrain coupling in the layer the owner specifically wants portable
(OD-19). R3's paired claim also reproduces exactly: `check_architecture.py
--mode strict` emits **1** `views→cogs` warning and exits **0**, against the
55-entry `known_violations` ledger recording 18 — the other 17 having moved into
function bodies, out of the gate's module-level field of view.

### The rule, because the failure was procedural rather than factual

This session drew the line — *"everything else stays lane-claimed and unverified
until the refutation pass"* — and then quoted three lane numbers as fact in the
same reply. **Drawing the line and crossing it in one breath is worse than not
drawing it**, because the qualifier then reads as coverage.

So, for the rest of this run:

> **No lane-produced number reaches a matrix, a headline or the executive
> assessment until this session has re-derived it.** Lane rows are evidence
> *pointers*; the count that gets published is the one re-run here. Where a lane
> number is carried without re-derivation it is marked `lane-claimed` inline, not
> in a footnote.

Cheap, and the evidence says it pays: of the six lane figures re-derived so far,
**five reproduced exactly** (R2's four in I-16, plus R3's `views→cogs` = 1) and
**one was off by 5 %**. That is a good lane hit-rate and precisely the reason the
rule is about *publication* rather than about trust.

## I-18 · The re-derivation ledger — every lane number this plan publishes, re-run here — `MEASURED`

The rule adopted in I-17 needs an artifact, not a promise. This is it: every
lane-produced figure headed for a matrix, a headline or the executive assessment,
re-run by this session against the pinned clones. **Conclusion column is what
matters** — a differing denominator with an intact conclusion is a different
thing from a claim that does not hold.

| lane figure | re-derived here | verdict |
|---|---|---|
| R2: required Postgres leg green over zero tests | `pytest tests/integration -q` → `14 skipped`, EXIT=0 | **exact** |
| R2: e2e tier likewise | `pytest tests/e2e -q` → `11 skipped`, EXIT=0 | **exact** |
| R2: `register_hub()` never called in production | `sb/` → **1** (the def) · `tests/` → **3** | **exact** |
| R2: escape-hatch `ui/` glob matches nothing | `ls sb/domain/*/ui/*.py` → **0** across **49** dirs | **exact** |
| R3: `views→cogs` warnings the strict run emits | `check_architecture.py --mode strict` → **1**, EXIT=0 | **exact** |
| M9: panels declaring `renderer_override` | **218 of 314** | **exact** |
| M9: escape-hatch baseline | `{"per_subsystem": {}, "total": 0}` | **exact** |
| M4: `sb/kernel/ai/` files naming a `disbot/` source in their first 12 lines | **24 of 30** | **exact** |
| R3: `from cogs.<x>` imports inside `cogs/` — claimed 134 | **128** module-level, AST, 51 files | *denominator differs, conclusion intact* |
| M8: cross-layer imports — claimed 977 forward / 0 reverse | **1174 forward / 0 reverse** | *denominator differs (layer-set assumption), **the load-bearing zero is exact*** |
| R2: excuse-row expiry — claimed 1 of 27 checkers | **2 of the 10 that carry exemptions** | *corrected in the plan; conclusion intact and sharper* |
| M9: central audit spine — claimed 1 call site vs superbot's 49 across 28 files | `emit_central_audit(` → **1 site / 1 file**; `emit_audit_action(` → **49 sites / 27 files** | **exact** (27 files vs the lane's 28) — *and this session's first two re-derivations of it were the things that were wrong; see below* |

**Score: 9 exact · 3 with a differing denominator · 0 where the conclusion
flipped.** No lane claim re-derived so far has been wrong about *what it found* —
only about how much of it there was.

### The ledger's own bad row, kept because it is the sharpest lesson here

The audit-spine row took **three** attempts, and the first two were mine.

1. **Guessed API names** (`record_audit|audit_emit|emit_audit|write_audit`) →
   24-vs-10. Matched neither the lane nor reality. Caught, because absurd.
2. **Grepped the MODULE name** (`audit_events`) → *"37 refs / 27 files"*,
   published into this ledger as *"shape reproduces, both numbers differ"* with
   the lane implicitly marked down. **That row was wrong.** Of 44 matching lines
   **31 are `import` statements**, and on the `superbot-next` side it counted the
   defining module's own internals.
3. **Grepped the CALL** (`emit_audit_action(` / `emit_central_audit(`, excluding
   the defining module) → **49 sites / 27 files** versus **1 site / 1 file**. The
   lane said 49 across 28, and 1. **It was right.**

**A re-derivation with an unvalidated instrument is not a re-derivation** — and
this ledger asserted that rule in one paragraph while publishing, in the table
directly above it, a row produced by exactly that. Twice the correction
machinery committed the defect it exists to catch: once caught by absurdity,
once only when a reviewer asked what the number rested on.

So the rule takes the same treatment as every gate in this review: a
re-derivation is done when the **instrument has a positive control** — *find the
symbol before counting the symbol* — not when it produces a number.
`grep <module-name>` and `grep <function>(` answer different questions, and only
one of them is the question.

### And a third instance, in the commit that was correcting the second

The commit meant to land this correction (`70ca1cb`) was authored while the edit
script **raised `AssertionError` before writing anything**. The `git commit` on
the following line was newline-separated rather than `&&`-chained, so it ran
anyway: the commit carries a message describing a fix to this file and contains
**only `.substrate/guard-fires.jsonl`**, 14 lines of telemetry. It was pushed.

**That is a false-done — this review's own subject — produced inside the
correction of the previous false-done.** It is recorded rather than amended away
because the mechanism is worth more than the tidiness: a heredoc that fails
loudly still leaves an unchained `git commit` free to claim the work. The habit
that catches it is the one this review keeps arriving at from every direction —
**verify the artifact, not the exit of the step you think produced it**:
`git show --stat HEAD` after any scripted edit, which is the commit-level twin
of `assert len(population) >= FLOOR`.


## I-19 · The audit's "27 slash commands survive" is wrong, and the weekly restore proof cannot fail — `MEASURED`

Two R4 claims, re-derived here per I-17's rule. Both hold, and the first corrects
the figure this estate has quoted for a month.

### The degraded-boot number

The 2026-08-05 live audit reported that booting without `SB_INTENT_MSGCONTENT_OK`
leaves **"1,300 of 1,327 targets silently unreachable, leaving 27 slash
commands."** The 27 survivors are what made it a *degradation* rather than a
blackout.

They do not survive, because they were never registered. Measured:

```
sb/app/main.py:616      outcome = await sync_remote(bot, committed, enabled=False)
sb/app/tree_sync.py:53      if not enabled:
                    :54          logger.debug("leg C: disabled via AUTO_SYNC_COMMANDS")
                    :55          return SyncOutcome(False, "disabled")
```

The composition root hardcodes `enabled=False`, and `sync_remote` returns
`SyncOutcome(False, "disabled")` before touching Discord. **This root never
publishes a slash command at all** — so a `message_content`-degraded boot is not
1,300-of-1,327 unreachable with 27 left; it is a bot with **no reachable command
surface**, reporting healthy.

**Why this matters more than a corrected number.** `sb/spec/config.py:252-255`
justifies choosing DEGRADE over refuse-to-boot on the grounds that refusing
*"darked the WHOLE bot when every slash command still serves."* The premise is
false in this composition root. **The design decision rests on a survivor set
that does not exist** — which is the population defect again, this time inside an
architectural rationale rather than inside a test.

### The weekly restorability proof

`.github/workflows/restore-verify.yml:124`:

```yaml
run: python3 -m sb.app.verify_boot | tee verify-report.json
```

Measured across all **8** workflow files in the repo: **0 occurrences of
`pipefail`** and **0 `shell:` keys**. The step's exit status is therefore `tee`'s
— 0 whether the boot verified or crashed. **The weekly proof that the bot can be
restored cannot fail.**

**The load-bearing assumption there is that Actions' default `run` shell does not
enable `pipefail`, so it is grounded rather than asserted from memory**, three
ways:

1. **The estate has already measured this class.** `docs/traps.md:512-524`
   carries the exemption semantics in detail — `pipefail` counts only when set on
   a non-comment line *above* the pipe, and not when set after it, inside a
   subshell, or named in a comment — with a six-case test matrix behind it. The
   estate ships a checker for exactly this and treats the swallowed-exit-code
   behaviour as established.
2. **`superbot`'s own maintainers write `set -euo pipefail` by hand inside
   `run:` blocks** — `code-quality.yml:51`, `dashboard-data-refresh.yml:75`,
   `pr-auto-update.yml:67`, across 5 workflow files. Nobody types that if the
   default already provides it. Behavioural evidence from the same authors, in
   the sibling repository.
3. **`verify_boot` does exit non-zero on failure** — `sb/app/verify_boot.py:100`
   is `sys.exit(main())`, so `main()`'s status propagates and the pipe has a real
   non-zero to swallow. Without this the finding would be vacuous in its own
   right.

And this is the estate's own standing rule, from `.claude/CLAUDE.md`: *"verify
before fold; verify with real exit codes (never `$?` after a pipe)."* It is
violated in CI, in the one workflow whose entire purpose is proving
restorability — the exact class the rule was written for, in the place where it
mattered most.

### What the successor takes from this

Two properties, both cheap and both absent here:

- **"Online" must mean a named, counted, reachable command surface**, asserted at
  boot against a committed floor — not a gateway connection and a 200 on
  `/ready`. A bot that reports healthy with zero registered commands is the
  boot-time twin of a green gate over an empty population.
- **Every degraded state goes to a sink that survives the process.** R4 measured
  the current one: the degrade notice appends to a module-level
  `deque(maxlen=256)` with zero sinks attached, is suppressed on later boots by a
  durable latch, and the in-Discord card meant to surface it
  (`!platform findings`) is a frozen capture-world literal that always renders
  *"(none)"*. Three independent mechanisms, each of which alone would have hidden
  it.

## I-20 · The one place `superbot-next`'s parity gate is HONEST — and how this session nearly published its opposite — `MEASURED`

`tools/run_golden_parity.py --gate`, run on a machine with no Postgres:

```
golden-parity gate: 50 ported / 0 pending
gate: RED — 50 subsystem(s) are flipped `ported` but no replay is possible:
  no bot-under-test binding (HarnessBootError: Postgres unavailable:
  asyncpg is not installed — the DB seam cannot serve)
REAL EXIT: 1
```

**It refuses to be vacuous.** It notices that its population cannot be replayed,
names the reason, and **reds** — the opposite of `pytest tests/integration -q`
exiting 0 on `14 skipped` two steps later in the *same job* (I-16). And CI
invokes it correctly: `golden-parity.yml:67` and `named-gates.yml:141` both
`run: python3 tools/run_golden_parity.py --gate` with **no pipe**, and
`continue-on-error` appears **0 times** in either file. The exit propagates.

So this belongs on the credit side of the ledger: **the flagship acceptance gate
detects its own empty population.** Whatever else § 3b says about what it
compares, it does not lie about whether it ran.

### How this session nearly published the reverse, which is the more useful half

The first reading of that command was
`python3 tools/run_golden_parity.py --gate 2>&1 | tail -4; echo "EXIT=$?"` →
**`EXIT=0`**. On that reading the finding was going to be *"the gate announces
its own redness in prose and returns success"* — a spectacular defect, and false.

`$?` after a pipe is `tail`'s status. **This estate's boot file carries exactly
one rule about exit codes** — *"verify with real exit codes (never `$?` after a
pipe)"* — and `docs/traps.md:512-524` carries a six-case matrix for it. **I had
quoted that rule, in this document, about `superbot-next`'s `restore-verify.yml`,
roughly one hour earlier** (I-19), and then committed it in my own shell.

**The mechanism worth extracting is not "remember the rule".** It is why nothing
caught it:

> **The false reading pointed the same way as the thesis.** Every other error in
> this session's re-derivation ledger was caught by absurdity or by a reviewer
> asking — because the number looked wrong. This one looked *right*: a review
> about vacuous gates found a vacuous gate. Confirmation supplied the plausibility
> that would otherwise have triggered a second look.

That is the sharpest statement of this review's whole subject, and it applies to
the successor's gates as directly as to this document: **a defect is hardest to
see when its output agrees with what you expected**, which is precisely the
condition a green CI check creates every day. It is also the argument for why
§ 3's mechanisms must be *structural* rather than *habitual* — habits fail in the
direction of the thing you already believe, and this session demonstrated it
inside the document arguing for it.

## I-21 · `superbot`'s enforcement locus is pytest, not the workflow — 44 of 45, not 14 — `MEASURED`

Three lanes disagreed about whether `superbot`'s 45 `scripts/check_*.py` are
actually enforced. Re-derived here, one loop over all 45:

```
checkers: 45 | referenced from tests/: 44 | referenced from .github/workflows/: 15
```

- **M5 reported** *"of 45 `check_*.py` scripts only 14 run in CI"* — it counted
  workflow references. Measuring the same thing gives 15; either way it is the
  **wrong locus**.
- **R2 caught it mid-lane and said so**: *"my own intermediate reading that '30 of
  45 superbot checkers are unwired' is REFUTED by measurement — 43 of 45 are
  referenced from `tests/`."*
- **R6 made it its headline** and stated the correction loudly in its own
  `contradicts` field: it first counted 15 in CI, found no runner for
  `check_command_reachability` / `check_settings_reachability` in any workflow,
  and then found the real path.

**The checkers are libraries; the gate is `pytest tests/ -v -n auto`** in
`code-quality.yml`. So a workflow-step census of this repo measures its
*documentation*, not its enforcement.

### Why this one matters more than the arithmetic

It **inverts the review's central comparison on the axis that decides everything
else**. The convenient story — *`superbot` is accumulated trial-and-error,
`superbot-next` is the engineered one* — survives only while you believe
`superbot`'s guards are decorative. They are not: 44 of 45 run behind blocking,
zero-tolerance invariant tests, several with the staleness proofs and negative
controls § 3 of the verification design is built from.

And the mirror holds. `superbot-next` inverted the arrangement — checkers driven
from a `set -e` workflow loop rather than from tests — and **three of its
flagship "required, NO EXPIRY" gates are green over an empty or unsigned
population** (`check_escape_hatches`: `"view:` occurrences = 0 in a 2,274,784-byte
snapshot; `check_verified_live`: 0 records, 50 of 50 subsystems `unverified`;
the `ui/` glob at 0 files across 49 directories).

**So on guard architecture, `superbot` is the donor and `superbot-next` is the
cautionary tale** — the exact reverse of how the 2026-08-21 plan assigns the two
roles. That plan's line is *"use `superbot-next` as an architecture and
kernel-pattern donor"*; on this axis the arrow points the other way, and this is
now the third attribution reversal found (I-3 the import-direction guard, I-4 the
AI gateway, this).

### The other reversal in the same lane: this is a PORT, not a convergence

R6 scanned for file-level similarity between the trees and found **54
`disbot`↔`sb` pairs above 0.55, 8 at ≥0.90, and one byte-identical** — verified
here: `disbot/utils/mining/capacity.py` and `sb/domain/mining/capacity.py` share
md5 `64f1665a9fb83a940d95eca5b9492bf2`.

Two consequences:

1. **"Which patterns did the two bots independently converge on?"** — a question
   this review's own R6 brief asked — is **largely void on the domain layer.**
   There was no convergence to discover there; the code was carried across. The
   genuine convergences are in the *kernel* patterns, and the genuine
   *improvement* is navigation (`superbot`'s `attach_standard_nav` is opt-in with
   17 call sites across 9 files; `superbot-next` made engine-injected navigation
   the default — a port that was improved rather than restated).
2. **It is direct evidence for OD-19's cog-portability requirement**, from an
   unexpected direction: a domain module already moved between these two
   architectures **unchanged**. Portability is not hypothetical here; it has
   happened, 54 times, and the fence that blocks it for stateful modules is a
   contract choice (I-10) rather than a structural impossibility.
