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

## 3 · The five mechanisms the estate already built — and never generalised

**This section replaces what was going to be an invented rule.** The population
contract in § 1 is not this session's idea. Both repositories already contain
working anti-vacuity mechanisms — five of them, each written after a real
incident, each solving one face of the problem — and **not one was generalised to
the guards beside it.** The successor's job is not to invent the rule; it is to
make these five the *default shape of a check* instead of five isolated good
days.

All five verified in source by this session, not carried on a lane's word.

### 3.1 · The denominator assertion — `superbot-next`, inside the parity harness

`tools/run_golden_parity.py:162-170`. The most surprising artifact in either
repo: the byte-parity harness — the instrument this whole review indicts —
**contains the fix for its own failure class.**

> *"F-003 fix: the denominator check. `results` only ever holds cases that
> SUCCESSFULLY reconstructed … a golden that failed to reconstruct into a case
> never gets an entry there, so the loop above has no way to see it and **the
> gate could false-green with fewer cases replayed than goldens on disk.**
> Assert the two counts match per ported subsystem so a silently-dropped golden
> reds the gate instead of just shrinking what got checked."*

Somebody noticed the population question exactly, named the false-green, and
fixed it **in code rather than in prose** — comparing a filesystem walk against
the loader's output, two independently derived counts. Then it stayed in that one
file. The nine other mechanisms M11 measured as empty, near-empty or a model
would each have been caught by the same three lines.

### 3.2 · The live-population negative control — `superbot`

`tests/unit/invariants/test_help_reachability.py:61-80`, and its docstring is the
rule in one sentence: *"a vacuous check is worse than none."* It mutates the
**live** scheme rather than a fixture and `pytest.fail()`s when the target is not
present, so **the control itself fails if the population is empty.**

Its limit is the one § 2.2 records — the live population it mutates is
`scheme_live()`, a model of the registry rather than the rendered panel. **The
mechanism is right and its target is wrong**, which is precisely why the
successor takes the mechanism and repoints it.

### 3.3 · The shrink-only ratchet with a staleness proof — `superbot`

`tests/unit/invariants/test_command_reachability.py:96-104`: a paired test that
**fails when a baseline entry is no longer a gap**, so recorded debt can only
shrink and can never go stale. Its baseline is currently `frozenset()` — the
ratchet drained itself and finished its job, which is what a working ratchet
looks like. Its sibling ratchet in the same repo (setup-copy jargon, ceiling 133,
24-entry tolerance list) **has no such test**.

### 3.4 · Excuse-row expiry — `superbot-next`

`tools/check_settle_once.py:629-637`: an `ALLOWLIST` or `KNOWN_RISKS` row
matching no warn-classified root is **itself a finding** —
`"STALE-ROW … never let an excuse outlive its reason"`. It is the checker-level
twin of § 3.3.

**Corrected count, and the correction is instructive.** Lane R2 reported this as
*"the only checker of the 27 that expires its own exemptions"*, and a first cut of
this section published that. It is **two**: `tools/check_money_race.py:610-616`
carries the same pattern verbatim — `(set(ALLOWLIST) | set(KNOWN_RISKS)) -
matched` emitting `"STALE-ROW … never let an excuse outlive the code it
excused"`. Positive control: `grep -rln "STALE" tools/*.py` returns exactly those
two files.

**And 27 was the wrong denominator anyway**, because it counts checkers with no
exemptions to expire. Measured: **10 of the 27 carry an exemption / allowlist /
baseline structure at all**, and **2 of those 10 expire it** —
`check_settle_once` and `check_money_race`. The eight that do not include
`check_escape_hatches` (21 exemption-ish references) and `check_sim_gate` (26),
which are §§ 3.1/3.6's two worst population cases.

2-of-10 is a weaker headline than 1-of-27 and it is the true one; it supports the
same conclusion, which is the point of re-deriving rather than relaying.

This is the direct answer to `superbot`'s exception files
(`consistency_exceptions.yml`, `command_reachability_exceptions.yml`,
`known_violations` at 55 entries): an allowlist that can only grow is a rule
being retired in slow motion, and a set-difference in the same run is the whole
fix.

### 3.5 · The guard that guards the guards — `superbot`

`tests/unit/scripts/test_workflow_script_flags.py`, and its provenance header
names the incident verbatim: PR #1770 invoked `check_session_slug_unique.py
--strict` on a script defining no `--strict`; **argparse exited 2 and the checker
silently never ran.** The test asserts every long option in the workflow is one
the script's `--help` advertises. Population: **11** `scripts/*.py` invocations
in `code-quality.yml`.

It is the only guard in either repo aimed at the *silently-dead-checker* class —
and it is scoped to one workflow file, and marked *"disposable … delete this test
if it proves unreliable."*

### 3.6 · What the successor does with them

| mechanism | today | in the successor |
|---|---|---|
| denominator assertion (§ 3.1) | one file | **every** gate asserts its own count against an independently derived one |
| live-population negative control (§ 3.2) | one guard, pointed at a model | **every** population-walking guard ships one, pointed at the rendered artifact, and it must fail on empty |
| shrink-only ratchet + staleness proof (§ 3.3) | 1 of 2 ratchets | **every** baseline/allowlist/exception list carries a paired staleness assertion; a list without one is a build error |
| excuse-row expiry (§ 3.4) | 2 of the 10 checkers that carry exemptions | in the checker **template**, so it is present by construction |
| workflow↔script flag parity (§ 3.5) | one workflow, "disposable" | checkers self-register their argparse surface and CI derives invocations from that registry, so the guard's population cannot drift |

**And the finding that makes this section worth more than the rule in § 1:**
these five were written by the same people, in the same two repositories, against
the same defect class — and each stayed in the file where it was born. The
successor's real requirement is therefore not a better idea. It is **a checker
framework in which these five are the default and opting out is the thing that
takes effort**, because this estate has now demonstrated twice that a good
pattern applied by discipline reaches 1-of-2, 1-of-27, and 2-of-8.

## 3b · What the parity system actually proves — and the six primitives worth keeping

Lane R5 dissected the acceptance oracle. Its sharpest finding is **verified here**
and is the deepest instance of this review's defect class:

### The oracle never runs the shipping renderer

Every wire byte on the **actual** side of a golden diff comes from
`rendered_panel_payload()` — defined at `sb/adapters/parity/transport.py:242`,
called at `:531`, and otherwise imported by exactly two parity unit tests.
Production installs a different renderer entirely:
`sb/app/panel_host.py:66` → `panel_engine.install_panel_presenter(DiscordPanelPresenter())`
(3 references in `tests/`, none on the golden path).

**So 533 goldens compare the old bot's real discord.py output against a
hand-maintained model of discord.py.** It is `superbot`'s help-reachability sim
(§ 2.2) one level deeper: the same guard-over-a-model shape, sitting at the heart
of the acceptance oracle rather than beside it. A byte-perfect pass says the
*parity serializer* agrees with the capture; it says nothing about what a user
sees.

### The corpus figures — `lane-claimed`, and marked as such

These are R5's and are **not** re-derived here, because reproducing them needs
the disposition transforms applied first: **38 of 533** goldens assert nothing
after dispositions (38 of the 66 slash goldens, 58 %) · **165 of 183** rendered
component custom_ids are never clicked by any case (90 %), with only **42 of
533** actuating anything · **36 of 533** pin a refusal as the expected behaviour ·
`check_parity_depth`'s "100 % declared-surface touch coverage" runs over a
denominator of **83** surfaces, with **22 of 49** ported subsystems declaring
zero. One adjacent figure *was* re-derived and matches: **62 of 533** goldens
carry an empty `db_delta`.

### The six primitives the successor keeps — every one already built

R5's most useful output is not the indictment; it is that the harness contains
**six** transferable mechanisms, on top of § 3's five:

| primitive | where | what it gives the successor |
|---|---|---|
| **`db_delta` effect capture** | per-case `TRUNCATE … RESTART IDENTITY`, fixture SQL, full snapshot of every row of every `pg_tables` table before and after, row-level diff, volatile columns scrubbed **by name** | *"the only assertion in either repo that proves a write happened."* This is the **effect layer**, already implemented |
| **the F-003 denominator assert** | `run_golden_parity.py:162-170` | § 3.1 — every gate asserts its checked count equals the count that exists |
| **composition-root reachability boot** | `check_runtime_smoke` boots the real root headlessly and resolves every manifest ref, PanelRef and armed subscriber | the **reachability layer**, cheap: no DB, no token, no network. Missing one assertion — that every registered `custom_id` resolves to a handler, which is the 165-never-clicked hole |
| **the single-entry-seam fence** | `check_no_skip`: AST proof that no Discord surface reaches a handler except through `resolve()`, and `import discord` appears only under `sb/adapters/` | **the cog-portability enabler.** Widen its root to wherever ported cogs live, and pair it with the positive direction — every registered command *is* reachable from `resolve()` |
| **the frozen compat pin** | `compat/compat-frozen.json`: 413 command rows, 265 legacy custom_ids, 49 subsystem keys, 23 event-payload field sets, 17 AI task ids, CODEOWNERS-routed | R5 calls it *"the highest-value artifact in either repo for the owner's stated goal"* — the executable form of the cog-portability contract |
| **GAP-on-unmodeled-effect** | an outbound effect the transport does not model raises during **both** capture and replay | *"an unmodeled effect is a RED, never a skip — the single discipline that separates this harness from a screenshot differ"* |

Plus two hygiene patterns: **symmetric disposition transforms** (an accepted
difference is applied to both sides, so it cannot become a one-sided blind spot)
and a **closed reason-class vocabulary** for exemptions (12 declared classes,
*"never a bare flaky"*, 49 exempt rows across 21 subsystems) — which makes
coverage debt countable, and needs only an expiry per class so *time-driven*
cannot mean *forever*.

**The conclusion this forces.** `superbot-next` did not lack the ingredients of a
real proof system — it had a genuine effect assertion, a denominator guard, a
real-boot reachability check and a containment fence, and it **pointed its
headline oracle at a model anyway**. The successor's advantage is not better
ideas; it is wiring these six to the shipping artifact from the first commit.

## 3c · The proof layers

`PENDING FLEET` — the full layer table (structural · unit/domain ·
contract/integration · journey · reachability · effect · real-guild ·
production-readiness) lands with challenge F's gate-breaking pass.

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
