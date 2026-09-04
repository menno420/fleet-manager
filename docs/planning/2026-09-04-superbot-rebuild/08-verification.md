# Verification architecture — the proof layers that replace parity

> **Status:** `plan` — **PARTIAL.** § 1 (the population contract) and § 2 (the
> worked failures it is derived from) are complete and rest on this session's own
> measurements. §§ 3–5 — the full layer table, the real-guild ladder and the
> production-readiness split — land from fleet lanes R2 (the vacuous-guard
> census), R5 (the parity harness anatomy) and challenge F (the gate-breaking
> pass), and are marked `PENDING FLEET` until they do.

## 0 · What this replaces, and what it keeps

`superbot-next`'s acceptance oracle was **533 golden files asserting byte
equality against the old bot's captured output**. It was honest, disciplined,
green, and it certified a bot whose front door reaches nothing
([`04-root-cause.md`](04-root-cause.md) § 2).

Golden tests are not the mistake. **The mistake is a proof layer whose population
is not the product.** Byte-comparison legitimately proves *rendering stability* —
that a refactor did not change copy nobody asked to change — and that property is
worth keeping, under a contract that says so. What it cannot prove is that
anything happened, that anyone can get there, or that anything was built at all.
So the successor keeps goldens, demotes them to the one property they hold, and
adds the layers that carry the rest.

## 1 · The population contract — the one rule the other layers hang on

> **Every gate declares the population it runs over. The declaration is
> committed beside the gate. The gate asserts the population is non-empty
> against a committed floor, and that it is the shipped artifact rather than a
> model of it.**

Concretely, every check in the successor carries three lines it cannot omit:

```python
POPULATION = "every panel in the committed manifest snapshot"   # prose, for a human
FLOOR      = 250                                                 # committed, versioned
assert len(population) >= FLOOR, f"POPULATION FLOOR BREACH: {len(population)} < {FLOOR}"
assert ok, problems
```

Four properties follow, and each answers a measured failure rather than a
hypothetical one:

1. **A floor breach is a RED, not a pass.** It is the single line that would have
   failed `superbot-next`'s navigation golden on the day it was written, instead
   of leaving it green over an empty registry for the project's whole life.
2. **The floor is committed and versioned**, so shrinking the population is a
   reviewable diff. A gate whose coverage silently halved is the
   `superbot-games` failure — `pytest tests/ -q` collecting 73 of 121 while a
   card's own arithmetic said 73 was the total.
3. **"The shipped artifact rather than a model of it"** is the clause that
   separates a guard with teeth from a guard with teeth pointed at a mannequin.
   `superbot`'s help-reachability invariant is mutation-tested — and both the
   guard and its mutation test operate on `scheme_live()`, a hand-built model of
   the hub registry, which is how six moderation subsystems sit click-unreachable
   behind a green check.
4. **Declaring the population is cheap at authoring time and unrecoverable
   later.** All three measured failures had a correct assertion; none had a
   declared population. Nobody had to be careless for any of them to happen.

**The rule is enforced by the framework, not by discipline.** A check registers
through a helper that takes `population` and `floor` as required arguments; a
check that does not register cannot run in the gate. This is the same move the
successor makes for hub children (§ 2.3) and for the same measured reason: in
this family, *unguaranteed* and *absent* have the same failure rate given enough
time.

## 2 · The three failures this is derived from — all source-read

Not illustrations. These are the population defects measured in this family's own
repositories, and § 1's four properties are one-to-one with them.

### 2.1 · A population emptied by the test's own fixture

`superbot-next`, `tests/unit/navigation_golden/test_navigation_completeness.py`.
The suite its docstring calls *"the golden proper"* walks the panel registry via
`panel_inventory()` and `_HUBS`. Its own `conftest.py` declares an
**`autouse=True`** fixture calling `clear_panels_for_tests()` — which is
`_PANELS.clear(); _STATIC_TABLE.clear(); _HUBS.clear()` — before every test in
the directory.

Inventory `{}`, roots `∅`, reachable `∅`, `problems` empty, `report.ok` True, for
every possible state of the product. The docstring's *"arms automatically as port
bands register real panels"* cannot happen: no band can register into a registry
the fixture empties at the start of each test.

**What § 1 would have done:** `FLOOR = 250` fails on line one, permanently, until
the walker is pointed at the compiled manifest — where the real population sits,
in the same repo, in a committed file.

### 2.2 · A population that is a model of the artifact

`superbot`, `tests/unit/invariants/test_help_reachability.py`. The guard checks
`tools/sim/help_menu_grouping_sim.py::scheme_live()`, which builds each hub's
children by filtering `SUBSYSTEMS` on `parent_hub`. The rendered panel is never
constructed.

And it is **mutation-tested**, which is what makes it the sharpest case in the
review. `test_guard_has_teeth_detects_an_unhomed_subsystem` opens with the right
instinct verbatim — *"a vacuous check is worse than none"* — then removes
`blackjack` from `scheme_live()` and asserts `orphans_of` flags it. **The
mutation is applied to the model and checked against the model.** The guard is
demonstrably not vacuous over its model, and completely vacuous over the product.

Measured consequence: the `moderation` hub declares 6 `primary_children` and
`ModPanelView` renders 7 buttons, every one an action (warn, timeout, kick, ban,
unban, modlogs, clearwarn) and none a route. Across all 8 hubs, 27 of 34 declared
children have a button on their parent hub; the shared discovery seam is 19 for
19, hand-rolling is 8 for 15.

**What § 1 would have done:** *"the shipped artifact rather than a model of it"*
forbids `scheme_live()` as the population. The replacement already exists in the
same repository — `tests/unit/views/test_games_hub_view.py` instantiates the real
`GamesHubView`, asserts over `view.children`, and drives each button's real
callback against a stubbed `Interaction`, classifying by which response method
was awaited. It is applied to 2 of 8 hubs.

### 2.3 · A population that shrank without anyone deciding to shrink it

Two instances, one shape.

`superbot-games`: the `substrate-gate` CI step ran `pytest tests/ -q`, which
collected **73 of 121** tests — `games/exploration/tests/`'s 48 invisible — while
the session card's own arithmetic, *"mining 62 + encounters 11 + exploration =
73"*, papered over it. **62+11 is already 73**: the equation's third term
contributes nothing, and it shipped.

`superbot-next`'s AI tools: `sb/kernel/ai/tools_catalogue.py` replaced
`superbot`'s closed 36-entry `CATALOGUE` with an open registry — a genuinely
better abstraction, with authority that can only narrow and derived grounding
allowlists. There is exactly **one** `register_tool(` call site in all of `sb/`,
registering **8** rows, all BTD6 factual reads at `AIScope.USER`, **zero**
write-capable. The production bot's one audited write tool
(`open_support_ticket`, through the audited mutation seam) did not survive. Under
byte parity this is invisible: an unregistered tool emits no output, so no golden
covers it.

**What § 1 would have done:** a committed floor on the registry — the successor
ships `FLOOR` for its tool catalogue, its panel graph, its command surface and
its migration set, so *the mechanism improved and the population collapsed* is a
red diff rather than a discovery two months later.

## 3 · The proof layers

`PENDING FLEET` — the layer table (structural · unit/domain · contract/integration
· journey · reachability · effect · real-guild · production-readiness), each with
its declared population and its named blind spot, lands from lanes R2 and R5 and
challenge F.

Two layers are already fixed by measurement and will not move:

- **Reachability** runs over the **committed route graph**, walked from the
  canonical entry point, and asserts every enabled feature is reachable within
  the promised interaction budget. Prototype and first result:
  [`run/reachability_probe.py`](run/reachability_probe.py) — which found
  `superbot-next`'s help tree at **max depth 0** and `setup` at **39 of 40
  panels unreachable**. It must model per-guild visibility, or it will score a
  correctly-hidden subsystem as an unreachable one and train its readers to
  ignore it.
- **Effect** requires that a write feature produce the state change and a
  dynamic-status feature change its output when the state changes — proven by
  mutating the state and re-reading, never by comparing to a recorded string. A
  refusal counts as success only where refusal is the specified behaviour. This
  is the layer that makes a transcribed constant unable to pass.

## 4 · The real-guild ladder

`PENDING FLEET`.

## 5 · Product-completeness versus deployment-readiness

`PENDING FLEET` — they are separate verdicts and must not be compressed into one
green score.
