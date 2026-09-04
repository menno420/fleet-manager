# Independent findings — measured by the session itself, not by the fleet

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
