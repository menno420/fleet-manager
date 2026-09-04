# Root cause — two different failures, and the one mechanism that produces both

> Evidence for every claim: [`run/independent-findings.md`](run/independent-findings.md)
> (this session's own measurements) and the fleet lanes recorded in
> [`run/`](run/README.md). Where a claim comes from the 2026-08-05 live audit
> rather than from this session, it says so.

## 0 · The one-sentence version

`superbot` accumulated debt because **eleven months of owner-directed feature
growth had no mechanism that made the cost of a new feature local**, and
`superbot-next` reached architectural and test completeness without product
completeness because **every instrument it built to check the product was
pointed at a model of the product rather than at the product**. Those are not
the same failure, and a successor that only avoids one of them fails the other.

## 1 · Why `superbot` accumulated debt

### 1.1 The debt is pre-EAP and it is feature growth, not agent damage

`MEASURED` (I-9). Of 911 runtime Python files ever added under `disbot/`,
**909 (100 %) predate the EAP fortnight** and **2** were added during it. Of
1,075 documentation files ever added under `docs/`, **822 (76 %) predate it and
245 (23 %) were added inside those fourteen days** (183 of the 245 survive).

So the accumulation the owner names — *"too much history, too many trials and
errors"* — is **his own eleven months of building**, and the autonomous program
contributed **two runtime files** and a large tranche of prose. Two consequences
that a rebuild plan must not get backwards:

- **"Avoid the EAP's working style" does not avoid `superbot`'s debt.** The debt
  predates the style. A successor built entirely in owner-live sessions, with
  no autonomous program anywhere near it, reaches the same place on the same
  timescale unless something structural changes.
- **The documentation sprawl is the part with an EAP component** — and it is the
  part a cleanup can actually cut, which is what OD-17 and the fresh-start
  redirect are already about.

### 1.2 The structural cause: every feature costs a non-local change

`superbot`'s own rule files are the confession. A feature is not finished when
its cog exists; it must also appear in `utils/subsystem_registry.py`
(`SUBSYSTEMS`), in `utils/hub_registry.py` (`HUBS.primary_children`) — **the same
parent link stored twice, which is why a bidirectional-drift checker had to be
written** — in `architecture_rules/mutation_owners.yaml`, potentially in
`consistency_exceptions.yml`, `command_reachability_exceptions.yml`,
`settings_reachability_exceptions.yml`, `audit_seam_exceptions.yml`,
`deferred_recovery_exceptions.yml`, `duplicate_allowlist.yaml` and
`extension_roles.yaml`, plus a settings key, a migration, an events entry and a
help route.

**That is the debt, precisely located.** Not the 243,961 lines and not the 59
cogs — the fact that adding one ordinary feature touches ten places, five of
which are exception lists whose entries are the measure of how much each rule is
already not true. `superbot` responded the right way — it turned each recurring
defect into a machine check — but the checks are downstream of a shape that
makes the defect easy, so the exception files grow with the feature set.

### 1.3 And the response was genuinely good — which is the useful half

Do not read § 1.2 as a verdict on the repo. The same eleven months produced:

- `scripts/check_architecture.py --mode strict` inside the **required**
  `Code Quality` check, driving `architecture_rules/layers.yaml` — a real,
  enforced import-direction contract (`cogs → services, core, views, governance,
  utils` · `views → services, core, utils` · `services → utils, core/events` ·
  `governance → utils, core` · `core → utils` · `utils → stdlib, discord`);
- `mutation_owners.yaml` — one canonical mutation service per domain, with raw
  `pool.execute()` allowed only inside `utils/db/`;
- `scripts/check_command_reachability.py`, written for a defect the **owner
  himself reported** (*"the general cog is completely unfindable from the help
  menu"*), and `scripts/check_settings_reachability.py` beside it;
- `docs/AGENT_ORIENTATION.md`, created **2026-05-24** — six weeks before the EAP
  — with the tier vocabulary (`binding` / reference inventory / historical plan /
  how-to-work) that this estate's own boot file descends from.

**A repository that converts its own recurring defects into enforced checks is
not a repository to discard.** § 3 says which of these transfer.

## 2 · Why `superbot-next` reached completeness without product completeness

### 2.1 It is not that they forgot to check the product

The story that gets told is that a parity-obsessed rebuild never thought about
whether the bot worked. **The source refutes that.** `superbot-next` contains
`tests/unit/navigation_golden/test_navigation_completeness.py`, whose docstring
calls it *"the CI proof"* that every declared node is reachable with
framework-injected Back/Home. Somebody understood the exact property that later
failed, and built a walker for it.

### 2.2 What actually happened: the instrument was pointed at an empty set

`MEASURED` (I-2). The suite the file itself calls *"the golden proper"* is:

```python
report = asyncio.run(walk_navigation(_ctx(), subsystem_hubs={
    "economy": "main", "hub": "main"}))
assert report.ok, report.problems
```

`sim/navigation_walk.py` builds its graph from `panel_inventory()` and `_HUBS`
— the module-level panel registry. The suite's own `conftest.py` declares an
**`autouse=True`** fixture calling `clear_panels_for_tests()`, which is
`_PANELS.clear(); _STATIC_TABLE.clear(); _HUBS.clear()`, before every test in the
directory.

So the inventory is empty, the root set is empty, the reachable set is empty,
`problems` is empty, and the assertion passes — **for every possible state of the
product, permanently.** The docstring's promise that it *"arms automatically as
port bands register real panels"* cannot come true: no band can register into a
registry the fixture empties at the start of each test.

Meanwhile the same repository's committed `manifest.snapshot.json` holds the real
population — **314 panels, 153 with zero actions, `help` 60 of 66** (I-1,
re-measured this session at the current pin, reproducing the 2026-08-05 audit
exactly). The data the walker needed was in the repo, in a file, the whole time.

### 2.3 The same shape, one layer up: golden parity

The 533/533 corpus has the identical defect at a different scale. It asserts that
the rebuild's **bytes** match the oracle's bytes. Under that rule a polite refusal
replays forever, a transcribed roster reproduces the capture exactly because it
*is* the capture, and a command that was never ported emits nothing so no golden
covers it. The number was honest. It measured a property the product does not
have.

And it did more than fail to catch the defect — **it created the incentive for
it.** The `CAPTURE-WORLD LITERAL` convention is stated in the code's own words as
*"the shipped description interpolated `len(bot.cogs)` — the capture world's 58
loaded cogs. Both goldens pin the one value, so the line ships as the pinned
literal."* Computing the value would have made the golden red. Transcribing it
made the golden green. **The gate selected for the photograph.**

`MEASURED` (I-5): the convention's own vocabulary — `capture world`,
`shipped verbatim`, `golden-pinned`, `goldens pin`, `pinned literal`,
`honest successor`, `successor read`, `the oracle carried` — appears in **137 of
634 `sb/` files and 116 of 382 `sb/domain` files (30 %)**, against the four files
carrying the formal label. That is a candidate set, not a defect count; what it
establishes is that the habit which produced the four labelled defects was the
house style of roughly a third of the domain layer.

### 2.4 The generalisation, which is the transferable finding

Both artifacts above, and `superbot`'s own reachability guard, are the same bug
in three places:

> **A guard is only as good as the population it runs over.** Every one of these
> checks was correctly written. Each was pointed at something other than the
> artifact a user touches — an emptied registry, a byte transcript, a hand-built
> model of the hub table.

`superbot`'s instance: `tests/unit/invariants/test_help_reachability.py` checks
`tools/sim/help_menu_grouping_sim.py::scheme_live()`, which builds each hub's
children by filtering `SUBSYSTEMS` on `parent_hub` — **a model of the registry,
never the components the panel renders.** So the Moderation hub can declare six
`primary_children` while `ModPanelView` renders seven action buttons and no child
navigation, and the guard stays green. And the guard is **mutation-tested**, which is what makes this the sharpest
example in the whole review. `test_guard_has_teeth_detects_an_unhomed_subsystem`
opens with the right instinct, verbatim:

> *"The guard must actually catch an orphan — **a vacuous check is worse than
> none**. Simulate a regression by dropping a known child from its section and
> confirm the orphan detector flags exactly it."*

It then does this:

```python
live = sim.scheme_live()
target = "blackjack"
for section in live.sections:
    if target in section.children:
        section.children.remove(target)
        break
assert target in sim.orphans_of(live)
```

The mutation is applied to `scheme_live()` — **the model** — and checked with
`orphans_of` — **also the model**. The rendered view never enters either the
guard or its teeth test.

So: a team that wrote down *"a vacuous check is worse than none"*, and then built
a mutation test to prove their check was not vacuous, produced a check that is
demonstrably not vacuous **over its model** and completely vacuous **over the
product**. Six moderation subsystems are click-unreachable behind it.

The lesson is not "test harder". It is that **teeth are a property of the
population, not of the assertion** — and the only way to know which population a
guard bites is to write it down, which is why § 3's first mechanism is a declared
population rather than a better test.

### 2.5 · It is not this family's mistake — it is this estate's dominant defect class

Four instances, four repositories, all in the estate's own committed record:

| where | the guard | the population it actually ran over | the population it was reported as |
|---|---|---|---|
| `superbot-next` | the navigation-completeness golden | the panel registry, emptied by the suite's own autouse fixture (I-2) | "every declared node reachable" |
| `superbot-next` | 533/533 golden parity | the captured **bytes** of the old bot's output | "49/49 subsystems ported, zero unmapped" |
| `superbot` | `test_help_reachability` + its mutation test | `scheme_live()`, a hand-built model of the hub registry | "every Help subsystem is reachable from the menu" |
| `superbot-games` | the `substrate-gate` CI step | **73 of 121 tests** — 48 exploration tests invisible to collection | "the gate now runs the test suite" |
| `venture-lab` | the Stripe checkout suite, 13/13 green | synthetic events from a hand-rolled helper that always set `customer_email` | "Stripe Checkout + webhook, pre-wired, ready to sell" — the live path had `customer_email: null` |

The last two are not this session's findings; they are the estate's own
[false-done ledger](../../findings/2026-09-02-eap-mail-evidence-report.md) § 3
(rows L03/FD-01 and L02), verified there under adversarial review.

**So the mechanism in § 3 is not a fix for one rebuild's mistake.** It is the
answer to the failure this estate keeps paying for: *a green instrument whose
population is smaller than, or a model of, the population it is reported as
covering.* Every proposed gate in
[`08-verification.md`](08-verification.md) therefore has to declare its
population, and that declaration is the deliverable — not the assertion.

## 3 · How the successor prevents both

Each mechanism below answers a specific failure above; none is general advice.

| the failure | the mechanism | why it holds |
|---|---|---|
| § 1.2 · a feature costs a non-local change | **one declaration per feature, and every registry derived from it** — the parent link stored once, help generated from the route graph, settings/permissions/AI-tool exposure read off the same record | there is no second place to update, so there is no drift to check and no exception file to grow |
| § 1.2 · exception lists absorb the rules | **an allowlist entry expires.** Every exception carries a reason and a date, and the checker fails on an expired one | an allowlist that can only grow is a rule being retired in slow motion |
| § 2.2 · a guard over an empty population | **every gate declares its population and asserts it is non-empty**, with a floor checked in the same run: `assert len(population) >= FLOOR` beside every `assert ok` | the exact line that would have failed superbot-next's navigation golden on day one |
| § 2.2/2.4 · a guard over a model | **reachability and actionability are asserted over the rendered artifact** — instantiate the view, read `view.children`, drive the callback, classify by which response was awaited | this is not invented here: it is `superbot`'s own `test_games_hub_view.py`, applied to 2 of its 8 hubs. The successor makes it universal by construction, not by discipline |
| § 2.3 · the gate selects for the photograph | **an effect assertion is required beside every output assertion.** A write feature must produce the state change; a status feature must change its output when the state changes — proven by mutating the state and re-reading | a transcribed constant cannot pass a test that changes the world and demands the output move |
| § 2.3 · absence is invisible | **the shipped surface is enumerated from the declaration and every entry must be exercised**, so a capability that was never built is a missing test, not a silent zero | golden corpora are keyed on what exists; declarations are keyed on what was promised |
| § 1.1 · the debt is organic, not stylistic | **the extension contract is the deliverable of slice one**, not a later extraction | the shape that makes ordinary growth local has to exist before there is growth |

**And the honest caveat that belongs in this section rather than in a footnote:**
`superbot-next` is the estate's *existing* precedent for exactly this plan — a
clean-start rebuild, disciplined, well-instrumented, that reached 533/533 and was
parked as a donor. The successor would be the **third** start-fresh attempt in
this family. Nothing above is worth anything unless the population rule and the
effect rule are in the first commits, before the first feature; they are cheap
then and unaddable later, which is precisely what happened last time.
