# Executive comparative assessment

> **Status:** `plan` — complete, with its evidence grades on every claim.
>
> **How to read a claim here.** A line tagged **`MEASURED`** was re-derived by
> this session directly, and the derivation is in
> [`run/independent-findings.md`](run/independent-findings.md) under its `I-` id.
> A line tagged **`lane-claimed`** comes from one review lane's own measurement
> and was **not** independently re-run — [`13-verdict.md`](13-verdict.md) § 2
> explains why that distinction is load-bearing here and not a formality: the
> fleet's survival rule passed 98 % of rows, so lane agreement is weak evidence.
> Untagged sentences are argument over those facts, and are mine.

## 1 · What `superbot` gets right

Stated as five things a successor should take, not as praise.

**1 · It answers.** `disbot/bot1.py:540-546` installs an always-answer fallback
for unrecognised input — written for a defect the owner reported as commands
"vanishing." `superbot-next` deleted it: `!helpp` and `!seting` produce total
silence, and so does every unrecognised token (`lane-claimed`, CHALLENGE D). Of
every difference between the two bots this is the one a member would notice
first, and it is four lines of code.

**2 · It enforces the product, not just the invariants.** `superbot` has an
import-direction guard (`scripts/check_architecture.py` over
`architecture_rules/layers.yaml`, `--mode strict`, inside the **required** `Code
Quality` check), command- and settings-reachability checkers, and a back-button
rule — each written against a real reported defect, each with a reasoned
exception file (**`MEASURED`**, I-3 as corrected by I-22; see § 3 for what the
layering half of that actually proves). `superbot-next` has none of these.
Cross-repo, the split is clean: **`superbot` guards what the user can reach;
`superbot-next` guards what the system may not do.** Neither has both.

**3 · Its hub tests drive real callbacks.** `tests/unit/views/test_games_hub_view.py`
instantiates the real view, asserts over `view.children`, and drives each
button's callback against a stubbed `Interaction` — `is_actionable_not_disabled`,
`no_placeholder_or_coming_soon_labels`, `fails_closed_when_subsystem_invisible`.
That is precisely the assertion `superbot-next` lacked. It covers **2 of the 8
declared hubs** (**`MEASURED`**, I-6), which is why § 4.2 turns it into a
construction rule rather than a testing habit.

**4 · Its money primitive is one function, reused.** A single conditional-`UPDATE`
debit primitive, reused seven times, with escrow/settle-once and a
DB-constrained checkpoint table (`lane-claimed`, M3). The successor gets this
shape for free and should not re-derive it — though note M6's live finding that
`transfer()`, the actual `$pay` path, still carries the read-then-write race the
docstrings claim was eliminated (`lane-claimed`).

**5 · Three years in, it is not the tangle its own documentation implies.**
**12 of 883 modules and 1,695 of 243,961 lines (0.69 %) are unreachable from the
composition root, and the tree holds exactly one `TODO` marker** (`lane-claimed`,
CHALLENGE A). The "too much history" framing describes the 863-file doc corpus,
not the runtime. This matters for the rebuild decision itself: it is evidence
that a large Discord bot can be maintained for three years without structural
collapse, which weakens the strongest argument for starting over.

## 2 · What `superbot-next` gets right

**Its real inheritance is not the panel/manifest/parity layer** — the thing it
is famous for. It is that four cross-cutting concerns moved from per-surface
convention into **required fields and registry-derived walks a new feature
cannot forget**: authority, audit, send-egress and member-data erasure.

The measurement that makes this concrete is the `superbot` side of it
(`lane-claimed`, CHALLENGE B): 166 hand-placed authority decorators, 49
hand-written audit calls, **18 of 915 sends setting `allowed_mentions`**, and 31
hand-written teardown helpers against 74 guild-scoped tables (**`MEASURED`**,
[`10-migration.md`](10-migration.md) § 10, which reconciles two conflicting lane
figures — the lanes said 84 and 23/74). Every one of those
is a place a future contributor forgets. In `superbot-next` they are schema.

That is the donation. Around it:

- **A config seam that is machine-enforced** — no `os.getenv` outside
  `sb/kernel/config/**`, one ledgered exception. The pattern generalises to any
  ambient dependency and costs nothing to install on day one.
- **A headless boot-and-wire gate** that M11 fired **with a negative control**
  (`lane-claimed`) — one of the few gates in either repo whose non-vacuity was
  demonstrated rather than asserted.
- **AI kernel seams** — redaction, routing, an audit spine, deterministic
  fallback, a task registry — genuinely well-built and well-tested
  (`lane-claimed`, M10). But the *gateway* itself is `superbot`'s, ported:
  `sb/kernel/ai/gateway.py:1-6` says so in its own header, and **24 of the 30
  files in `sb/kernel/ai/` name a specific `disbot/` source in their first 12
  lines** (**`MEASURED`**, I-4; `lane-claimed` for the 24/30 census, M4).
- **Migration immutability and checksums, namespace/symbol collision checks, an
  egress fence, cost posture, metric cardinality, schema-growth and
  doc-citation gates** — the invariant half of the split named in § 1.2.

**What is *not* on this list, and the reason is § 3:** the manifest, the panel
engine, the golden corpus, the 49-subsystem breadth, and the layer DAG.

## 3 · What each gets wrong

The two failure profiles are not symmetric, and the asymmetry is the finding.

### 3.1 · `superbot`: enforcement narrower than the apparatus implies

- **Of 45 `check_*.py` scripts, 14 run in CI and 5 in the local gate**
  (`lane-claimed`, M5) — but read this next to **`MEASURED`** I-21: **44 of 45
  are driven from `tests/` as libraries behind blocking invariant tests**, which
  is the real enforcement locus and much stronger than the workflow census
  suggests. A reviewer looking only at the workflow file will understate this
  repo badly.
- **The layer-boundary rule is warning-only** for all 36 current violations, plus
  101 lazy cross-layer edges it does not see (`lane-claimed`, M5).
- **The mutation-ownership "hard gate" has a reproduced blind spot** — a new
  raw-write violation in ordinary multi-line SQL formatting passes `--mode
  strict` cleanly (`lane-claimed`, M6; the lane reproduced it).
- **Its two most quotable guards protect a model, not the artifact**:
  help-reachability walks a hand-mirrored, partly-fictional click mechanism;
  cog-size counts file-level LOC excluding the helpers (`lane-claimed`, M7).
  This is the population defect in its home repo.
- **One AI-content vertical, BTD6 strategy Q&A, is 30,923 of 59,744 measured
  lines (51.8 %)** of the games/economy surface (`lane-claimed`, M3) — and has
  nothing to do with the successor's purpose.

### 3.2 · `superbot-next`: completeness measured against the wrong artifact

- **The golden corpus does not test the shipping bot.** Every "actual" wire byte
  comes from `rendered_panel_payload()` in `sb/adapters/parity/transport.py`, a
  serializer used by nothing but the parity adapter and its own tests, while
  production installs a separate `DiscordPanelPresenter` (`sb/app/panel_host.py:66`)
  that **nothing in CI exercises** (`lane-claimed`, R5). 533/533 green compares
  old-bot bytes to a serializer that does not ship.
- **The panel engine's framework-injected navigation reaches 96 of 314 panels**;
  **218 (69 %) declare `renderer_override`**, and the repo's own "NO EXPIRY"
  escape-hatch ratchet counts only tier-3 `view:` refs — of which the snapshot
  holds **zero**, so its committed baseline is literally `"total": 0`
  (`lane-claimed`, M9). Independently, the route-graph walk this session ran
  found **help max depth 0 and 39 of 40 setup panels unreachable**
  (**`MEASURED`**, I-13).
- **Its "degrade instead of refuse to boot" premise is falsified by its own
  composition root.** `sb/spec/config.py:252-255` justifies degrading because
  refusing "darked the WHOLE bot when every slash command still serves" — while
  `sb/app/main.py:616` hardcodes `sync_remote(bot, committed, enabled=False)`, so
  **this composition root publishes no slash-command set at all** (**`MEASURED`**,
  I-19). It does not follow that the audit's *"27 slash commands survive"* is
  refuted — an application keeps commands from an earlier sync, and that is
  unmeasured here (I-19, narrowed after external review). What *is* established
  is that the degrade rationale rests on a surface this root never creates.
- **The clean layer DAG is a measurement artifact.** M8 reported "977 module-level
  cross-layer imports, ZERO reverse-direction." Re-measured including function
  bodies: **296 cross-subsystem `sb.domain` imports, of which 268 (90.5 %) sit
  inside function bodies; 8 mutual subsystem pairs in the union graph, 0 at
  module level** (**`MEASURED`**, I-22, which corrects this session's own earlier
  I-3). The cycles are all in the half nobody counted.
- **It is a prefix-command bot in modern clothing** — 386 of 413 commands
  prefix-only, frozen into a required CI check, while the two gates guarding the
  modern surface run over 18 and 4 commands and are not required
  (`lane-claimed`, CHALLENGE C).
- **The capture-world-literal class is wider than its formal label.** The label
  finds 4 files; the class holds at least 12, and the largest instance is
  unlabelled — `sb/domain/diagnostic/platform_views.py` freezes 28 operator
  diagnostic cards from the old bot's runtime and ships them as 33 registered
  commands inside a live `{ts}/{gid}/{ch}/{tier}` frame, including a
  database-health card that always reports "Schema healthy … 103/103" over a
  57-migration schema (`lane-claimed`, R1).

### 3.3 · The failure both share

**19 of 77 executable guards across both repos are vacuous-capable by
measurement** (`lane-claimed`, R2), and **not one of `superbot-next`'s seven
required checks asserts a floor on how much of the bot works** (`lane-claimed`,
CHALLENGE F). Every gate in the estate asserts *absence* or *self-consistency*.
CHALLENGE F's constructive proof is the sharpest statement of the problem: a bot
whose 863 clickable controls are all wired to resolvable no-op handlers, with one
golden per subsystem and one forged sign-off row per subsystem, **passes 7/7
green**.

That is the population defect, and it is why [`08-verification.md`](08-verification.md)
exists.

## 4 · What the previous reviews got wrong

The 2026-08-21 [`source-review.md`](../2026-08-21-game-community-bot/source-review.md)
is the best prior comparison anyone has, and most of it holds. Its "Reject or
correct" list is still right on every line, and its acceptance correction — *"the
important unit is a **user journey with an observable effect**, not a command,
panel, subsystem, golden string, or manifest row"* — is the correct diagnosis,
reached three weeks before this session and without a fleet.

Four things in it are wrong or missing, each measured rather than argued.

### 4.1 · Two `superbot-next` strengths are actually `superbot`'s

Its "Preserve from `superbot-next` — contracts and guards" list opens with
**"Explicit layers and import-direction guards"** and includes
**"Provider-neutral AI contracts and adapters behind one gateway."** Both
attributions reverse.

- **The import-direction guard is `superbot`'s.** `superbot-next`'s layering is
  real — 0 module-level `sb.kernel` → `sb.domain` imports against 234 the other
  way — and **nothing enforces it**: all 27 `tools/check_*.py` were enumerated and
  read by their own docstrings, none is an import-direction or layer guard, and
  there is no `tests/architecture/` directory. The absence carries its positive
  control: the same query form run against `superbot` finds
  `scripts/check_architecture.py`, which drives `architecture_rules/layers.yaml`
  and runs `--mode strict` inside the **required** `Code Quality` check (I-3).
- **The provider-neutral gateway is `superbot`'s, and its own successor says so.**
  `sb/kernel/ai/gateway.py:1-6`: *"Ported from shipped
  `disbot/core/runtime/ai/gateway.py` @7f7628e1 onto the kernel seams."* Same
  eight pipeline steps in the same order, same three providers, same
  never-raises contract (I-4).

**Why this is not pedantry.** The plan's operative recommendation is *"use
`superbot-next` as an architecture and kernel-pattern donor"* — and a donor list
whose first two entries came from the other repo will send an implementation
session to read the wrong tree for them. The correct reading is sharper and more
useful: **the two repos donate different halves of the same discipline.**
`superbot` donates guards over the **rendered product** — reachability,
actionability, the back-button rule, hub coverage. `superbot-next` donates guards
over the **invariants of the system** — the config seam, migration immutability
and checksums, namespace and symbol collisions, the egress fence, data and
credential lifecycle, cost posture, metric cardinality, the slash budget, schema
growth, doc-citation resolution (I-8). **Neither repo has both**, and the
successor needs both.

### 4.2 · It never credits `superbot`'s reachability enforcement — the one strength most relevant to the failure it is diagnosing

The review's `superbot` column says *"Cogs can be loaded/unloaded, but
responsibilities and config paths are spread"* and its Navigation row says
*"Proven button-first Home/help experience"* — a **product** credit. It nowhere
records that `superbot` already **enforces** navigation reachability in CI:
`scripts/check_command_reachability.py` (written for a defect the owner himself
reported — *"the general cog is completely unfindable from the help menu"*),
`scripts/check_settings_reachability.py`, and the back-button rule inside
`scripts/check_consistency.py`, all with reasoned exception files.

And it misses the transferable form of it. `tests/unit/views/test_games_hub_view.py`
does not inspect panel *shape*: it instantiates the real `GamesHubView`, asserts
over `view.children`, and drives each button's real callback against a stubbed
`Interaction` (`test_every_hub_button_is_actionable_not_disabled`,
`test_no_placeholder_or_coming_soon_labels`,
`test_button_fails_closed_when_subsystem_invisible`). **That is the assertion
`superbot-next` needed and did not have** — and it exists, today, in the repo the
plan treats as the behaviour oracle rather than the engineering donor.

The measurement that turns this from praise into a design instruction: the hub
registry declares **8 hubs**, and hub-view tests of that shape exist for **2** of
them (I-6). The pattern is right; the coverage is by discipline. So the
successor's rule is not "write tests like `superbot`'s" — it is **make this
contract universal by construction**: one hub renderer, one generated contract
over every registered hub, rather than one hand-written test somebody remembers
to add.

### 4.3 · Its modularity answer does not satisfy the constraint OD-19 makes mandatory

The review correctly says *"Do not load every module unconditionally"* and
proposes *"manifest-declared internal modules plus boot-time feature profiles;
no runtime code hot-unload in MVP."* Boot-time profiles are right. But OD-19
makes **cog portability a requirement** — *"I should be able to add exiting cogs
to it on demand, or be able to slightly alter an existing cog so that it works
with this bot"* — and the review does not test whether the donor's extension
mechanism can carry it.

It cannot, for most of the interesting cases. `sb/app/plugin_host.py` fences
plugin manifests to `ALLOWED_FACETS = (commands, panels, settings, events,
capabilities)` and rejects any declaring `HOST_ONLY_FACETS = (stores,
data_invariants, wizard_sections)` — the docstring's reason: *"migrations, S12
money lanes, and the G-19 setup registry have no out-of-tree lane yet."*
Measured against `superbot-next`'s own compiled snapshot: **29 of its 49
subsystems declare `stores`**, so 59 % of its own product could not be an
out-of-tree plugin (I-10). The eligible 20 are the stateless ones.

So the successor carries a requirement neither repo meets: **an out-of-tree
module must be able to own data** — ship migrations into a namespaced schema,
declare its invariants, contribute a setup section — or cog portability fails
for exactly the features worth porting.

### 4.4 · Its acceptance correction is right and still passable by a bot that does not work

This is the most important item, because it is where a good document stops one
step short. The review's eight per-feature requirements — a route from Home, an
authority decision, a typed operation, a visible result, an audit row, a
deterministic AI fallback, an automated journey/effect test, a real test-guild
drive — are the right list. **Not one of them says what population the check
runs over.**

That gap is not hypothetical; it is the exact hole every measured failure in
this family went through. A journey test over a fixture registry satisfies all
eight. `superbot-next`'s navigation-completeness golden would satisfy several of
them today, while being green over a registry its own `autouse` fixture clears
before every test (I-2). `superbot`'s help-reachability invariant satisfies them
too — including a **mutation test written specifically to prove it was not
vacuous** — while checking a hand-built model of the hub registry rather than the
components a panel renders, which is how six moderation subsystems are
click-unreachable behind a green check.

So this plan adds the ninth requirement, and it is the one that makes the other
eight mean anything:

> **Every gate declares the population it runs over, commits the expected set
> beside the gate, and asserts the walked population is EQUAL to it — any
> difference in either direction is a failure — over the real artifact rather
> than a model of it.**

**The rule is given in its corrected form, and the correction is worth more than
the rule.** This document first wrote it as `assert len(population) >= FLOOR`
with a committed floor. External review pointed out that against the 314 measured
panels a floor of 250 lets **64 panels vanish silently**, and a 250-entry
hand-built model passes identically — a lower bound is not an identity check.
**The paragraph prescribing the cure was an instance of the disease**, which is
exactly how this defect survives in careful repositories: a floor feels like
rigour. The floor survives only as a cheap tripwire under the equality check.
Full contract: [`08-verification.md`](08-verification.md) § 1.

Full derivation, and the three source-read instances behind it:
[`04-root-cause.md`](04-root-cause.md) § 2.

## 5 · The most important lessons for attempt three

**1 · Breadth was never the disease, and purity was never the cure.**
`superbot` carries 43 subsystems for three years with 0.69 % dead code and one
`TODO`. `superbot-next` reached 533/533 parity, 3,648 green tests and seven
required checks, and cannot answer a mistyped command. Neither outcome is
explained by module count. Copying `superbot`'s breadth into `superbot-next`'s
architecture — the thing the brief names as the failure mode to avoid — would
reproduce both profiles at once.

**2 · Every gate must declare its population.** This is § 4.4's ninth
requirement, and it is the single most transferable output of this review. Both
repos already built eleven mechanisms that do this correctly and **generalised
none of them** ([`08-verification.md`](08-verification.md) § 3). The successor's
advantage is not inventing a proof system; it is wiring the ones that exist to
the shipping artifact from the first commit, when it is cheap.

**3 · Test the artifact that ships.** `superbot-next`'s single largest
verification failure is not a missing test — it is 533 passing tests against a
serializer production does not install. Any check whose subject is not the object
the user touches is decoration, however green.

**4 · Count the half nobody counts.** M8's "ZERO reverse-direction edges" and
this session's own I-3 were both true of module-level imports and both wrong
about the codebase, because 90.5 % of the edges live in function bodies (I-22).
A census that excludes a construct excludes the defects that hide in it — and
lazy imports are where cycles go to live.

**5 · Reachability is the first slice, and it is a finding rather than a
choice.** Both bots independently lose the first-run journey to the navigation
graph, by unrelated mechanisms: `superbot-next` reaches 39 of 40 setup panels
from nowhere; `superbot` reaches setup only through an ephemeral out-of-graph
launcher with no route back (**`MEASURED`**, I-13). Two independent
implementations failing the same way at the same seam is the strongest available
evidence about where the successor should start.

**6 · Ask the owner one question before locking the design.**
[`12-owner-decisions.md`](12-owner-decisions.md) OD-A — one server or many —
moves the entire 40-panel setup surface in or out of the plan. Everything else
in that file has a default the work can proceed under.
