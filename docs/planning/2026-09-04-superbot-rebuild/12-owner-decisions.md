# Owner decisions

> **Status:** `plan` — the questions the evidence **cannot** settle, and only
> those. Everything the evidence can settle is settled elsewhere in this package
> and is not repeated here as a question.
>
> **The bar for a row being here**, applied strictly: proceeding under either
> answer would either be unsafe, be irreversible, or produce materially different
> work. An implementation choice with a defensible default is **not** owner
> homework — `docs/intent.md` § 6 is explicit that a reversible 50/50 is
> *"decide and flag"*, and § 8b that a session must *"resolve goal ambiguity, not
> every implementation possibility."*
>
> Each row gives: **what is known** · **why the evidence cannot settle it** ·
> **the recommended default** · **what changes if he chooses differently.**
> Every default is chosen so the next session can prepare everything else without
> waiting.

## OD-A · Is the successor one server's tool, or a product for many servers?

**What is known.** His 2026-08-28 statement sets the end state: `spider-bot` and
a remade `superbot-next` *"eventually are rebuild as one real well functioning
bot thats build right from the start … without architectural debt … able to grow
indefinitely."* His 2026-09-04 statement (in flight at
[#1021](https://github.com/menno420/fleet-manager/pull/1021), recorded at
[`run/in-flight-direction.md`](run/in-flight-direction.md)) says `spider-bot`
*"exists to manage the Slingy Spider server and help during testing of the
game"* — and the spider-bot purpose decision recorded in
[`run/in-flight-direction.md`](run/in-flight-direction.md) is careful that this narrows **spider-bot**, not the
successor: *"that one governs the shape this input must be in; this one governs
what it is for."* The 2026-08-21 plan's *"clean, multi-game Discord bot
repository"* headline is narrowed for spider-bot and left standing for nothing
in particular.

**Why the evidence cannot settle it.** Both readings are consistent with every
owner statement on record, and they produce genuinely different architectures.
A one-server tool can hard-code its guild's shape, keep a single settings scope,
skip the setup wizard almost entirely, and treat multi-tenancy as a non-goal.
A many-server product needs per-guild configuration, a first-run journey, a
teardown path and a resource-provisioning model — which is most of what
`superbot`'s 40-panel `setup` subsystem *is*. This is the single largest scope
fork in the package and nothing derivable decides it.

**Recommended default: many servers, one guild at a time.** Build the per-guild
scope and the first-run journey from slice one, and run it in exactly one guild
(Slingy Spider) until it earns a second. Reason: per-guild scoping is cheap to
build in and **expensive to retrofit** — it is the boundary every settings row,
every permission check and every table's primary key depends on — whereas
running in one guild costs nothing. It is the asymmetric-cost default, not a
guess at his ambition.

**If he chooses one server:** drop the setup wizard to a single owner console,
drop guild lifecycle and teardown entirely, and the successor's scope falls by
roughly the whole `setup` surface — the biggest single simplification available
anywhere in this plan.

## OD-B · Does the successor replace the production bot, and when is that even asked?

**What is known.** `superbot` is live, frozen, and behind the estate's hardest
rail. `superbot-next` reached 533/533 golden parity and *"was never possible to
make the switch"* — his words, 2026-08-30. Nothing in the current record commits
the successor to replacing it.

**Why the evidence cannot settle it.** The production bot serves a real server
with real members and a real Postgres. Whether it is eventually replaced,
permanently coexists, or is retired without replacement is a product and
risk preference, and the estate has already been burned once by a rebuild
carrying an implicit replacement promise it could not keep.

**Recommended default: no replacement promise, at all, until a successor has
independently earned it.** The successor is built and judged as its own product;
"replace production" becomes a question a *later* session may raise only after
the cutover ladder's observable criteria are met. Reason: the promise is what
converted `superbot-next`'s honest work into a failure — a bot that is genuinely
useful is a success on its own terms and a failure only against a promise nobody
needed to make.

**If he chooses to commit to replacement now:** the migration map's data column
moves from *"start fresh"* to *"must migrate"* for several subsystems, a
production-data rehearsal becomes a phase rather than a contingency, and the
roadmap grows a parity-of-behaviour obligation this plan otherwise deliberately
refuses.

## OD-C · Does `spider-bot` become the successor, or stay a separate live bot that the successor later absorbs?

**What is known.** OD-19 is a standing constraint: *"these bots remain
seperated"*, and the consolidation he describes is of **repositories**, not of
running bots. `spider-bot` is live in the Slingy Spider server with real users,
27 files and 3,172 lines, and its own record says its next feature is his pick.
His 2026-08-28 statement calls it **one of two inputs** to a bot that does not
exist yet.

**Why the evidence cannot settle it.** "Inputs converge into one bot" and "the
bots remain separated" are both his, and both current. They are reconcilable in
two different ways — the successor is a third repository that eventually replaces
spider-bot's deployment, or spider-bot *is* the successor's seed and grows into
it — and the choice changes what the first slice even is.

**Recommended default: a third repository, and `spider-bot` keeps running
untouched.** Reason: it is the only reading under which *"the bots remain
seperated"* survives literally, and `spider-bot` is the estate's one surface
where a careless push reaches real people in minutes. **A caveat that belongs in
the same breath, not a footnote:** its 3,172 lines run a live, useful bot today.
That is a real datum about how much architecture a first slice needs, and this
plan's blueprint must not out-build it without saying why.

**If he chooses spider-bot as the seed:** the first slice becomes a refactor
inside a live production bot with no PR gate, the deploy trap and the
two-live-instances hazard become first-order risks, and the plan's "isolated test
application, test guild, test database" posture has to be built *around* an
already-running service rather than beside it.

## OD-D · Which of `superbot`'s community features are core, which are optional, and which are gone?

**What is known.** `superbot` ships roughly 59 cog modules across 24 packages.
The 2026-08-05 shortlist proposed ~15 for a server-first core, ~6 deferred, ~19
excluded. The 2026-08-21 plan's exclusion list (casino, blackjack, economy,
inventory, treasury, mining, fishing, farm, creature, BTD6, Project Moon) is
already owner-aligned via OD-16's *"casino/economy/BTD6 and unrelated content do
not transfer"*.

**Why the evidence cannot settle it.** The excluded set is settled. The
**middle** is not: `xp`, `karma`, `leaderboard`, `counting`, `starboard`,
`community_spotlight`, `ticket`, `polls`, `reminders`. Whether each is core,
an optional module, or dropped is a question about *what he wants his server to
feel like*, and no measurement in this package answers it. Feature maturity
certainly does not: several of these are mature and several are unused.

**Recommended default: none of the middle set is core; each is an optional
module the extension contract must be able to carry.** Reason: it makes the
question cheap to answer later and expensive to answer wrong now — a module that
can be added is a smaller commitment than a core feature that must be removed.
It also puts the extension contract under real load in slice one, which is the
only way to find out whether it works.

**If he names some as core:** they move into the first slices and their data
model joins the core schema, which is a one-way door — a core table is far harder
to extract later than an optional module is to promote.

## OD-E · Does anything in the production database carry forward?

**What is known.** `superbot` carries **104 migrations** and **45 `utils/db/`
submodules**; `architecture_rules/mutation_owners.yaml` names 14 domains with an
owned write path. The live Postgres is a protected surface and **was not read by
this session** — nothing here is measured against production data.

**Why the evidence cannot settle it.** What is worth keeping is a judgement about
the *server's* history — whether members' XP, karma, tickets, starboard entries
and economy balances matter to the people who earned them — and only he can make
it. The estate has an open queue entry (`OQ-BOT-DB-BTD6-PRUNE`) showing DB work
is already owner-gated in exactly this way.

**Recommended default: import nothing; start fresh.** Reason: the successor is
not promised as a replacement (OD-B), so there is nothing to be continuous with;
and every migration that does not happen is a class of risk that does not exist.
**If any data does carry forward it is owner-approved, dry-run first, reversible,
measured, and independently verified** — this plan authorises none of it.

**If he wants continuity:** name the *server-visible* surfaces that must survive
(most likely candidates on the evidence: member XP/levels, karma, open tickets)
rather than a table list, and the migration becomes a scoped, rehearsable
exercise rather than a schema port.

## OD-F · How much authority may the AI hold on day one?

**What is known, and it is more than a question usually gets.** That same
decision
already gives the pipeline in his own direction — *AI supplies judgement,
deterministic code supplies authority*; a **typed, schema-validated verdict**;
free-form prose is never parsed into an action; invalid or incomplete model
output means no automatic action; new autonomous moderation starts in **shadow
mode**. And the production bot already proves a compatible shape: of 36
catalogued AI tools, exactly **one** writes, through the audited mutation seam.
OD-16 separately wants AI *"given meaningful freedom from the first slice."*

**Why the evidence cannot settle it.** "Meaningful freedom" and "reliable" pull
in opposite directions at exactly one point: whether a *medium-risk, reversible*
action (a timeout, a role grant, a message delete) may execute without a human
confirming it, once shadow mode has produced a track record. That is a risk
appetite, and it is his.

**Recommended default: auto-act on low-risk reversible operations only;
preview-and-confirm for medium risk; deny high-risk and destructive outright —
and any later confirmation-free expansion is a new, explicit decision rather
than a threshold the system crosses on its own.** Reason: it is the 2026-08-21
plan's GCB-4 default, unchallenged since, and it is compatible with both his
"reliable" bar and his "meaningful freedom" ask because shadow mode supplies the
evidence to revisit it.

**If he wants more from day one:** the effect-verification layer moves from
important to load-bearing — every AI-initiated write needs its state change
asserted and its audit row checked before the action is considered complete, and
that cost lands in slice one rather than later.

## What is deliberately NOT here

Recorded so the absence reads as a decision rather than an oversight:

- **The successor's name, repository and stack.** Owner-only when the time
  comes, and the time is not now — this plan creates nothing.
- **Every architectural choice in [`06-architecture.md`](06-architecture.md).**
  Ownership boundaries, the interaction pipeline, the route registry's shape, the
  config model, the persistence seams: all derivable from the evidence, all
  decided in that document with reasons, none of them his to adjudicate.
- **Whether to keep golden tests.** Settled by evidence, not preference — they
  are kept, demoted to rendering stability, in
  [`08-verification.md`](08-verification.md) § 0.
- **The first slice.** Determined by the measurements: navigation and
  first-run access. `superbot` reaches setup only through an ephemeral
  out-of-graph launcher message with no route back into the help graph;
  `superbot-next` reaches 39 of its 40 setup panels not at all. Two different
  failures, one root — **setup was never a first-class destination in either
  route graph.** It is a finding, not a choice.
