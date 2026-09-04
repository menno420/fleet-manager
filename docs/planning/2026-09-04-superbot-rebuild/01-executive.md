# Executive comparative assessment

> **Status:** `plan` — **PARTIAL, and the banner is the honest part.** § 4 below
> ("what the previous reviews got wrong") is complete and rests only on
> measurements this session made itself
> ([`run/independent-findings.md`](run/independent-findings.md)). §§ 1–3 and § 5
> land from the review fleet and are marked `PENDING FLEET` until they do — an
> empty section that says so is worth more than a plausible one written early,
> which is the failure this whole document is about.

## 1 · What `superbot` gets right

`PENDING FLEET` — lanes M1–M7 and challenge A.

## 2 · What `superbot-next` gets right

`PENDING FLEET` — lanes M8–M11 and challenge B.

## 3 · What each gets wrong

`PENDING FLEET` — lanes R1–R6 and challenges C–F.

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

> **Every gate declares the population it runs over, that declaration is
> committed, and the gate asserts the population is non-empty and is the real
> artifact rather than a model of it** — `assert len(population) >= FLOOR`
> beside every `assert ok`, with `FLOOR` in the repo.

Full derivation, and the three source-read instances behind it:
[`04-root-cause.md`](04-root-cause.md) § 2.

## 5 · The most important lessons for attempt three

`PENDING FLEET` — written from the challenge lanes and the critic.
