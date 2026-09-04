# The successor product definition

> **Status:** `plan` — authoritative for **what the successor is, who it is for,
> how a person reaches it, what its AI may decide, and what it will not be.**
> It does not decide how any of it is built ([`06-architecture.md`](06-architecture.md)),
> what a feature must ship with ([`07-feature-contract.md`](07-feature-contract.md)),
> or how any of it is proven ([`08-verification.md`](08-verification.md)). It
> authorises no implementation — OD-13 stands, and this plan creates no
> repository.

**Evidence marking, same rule as the rest of the package.** A number re-derived
against the pinned clones is stated bare and carries its `I-` id from
[`run/independent-findings.md`](run/independent-findings.md), or says
*"re-derived here"* with the file and line when it was measured while writing
this file. A number carried from a review lane without re-derivation is marked
**`lane-claimed`** inline, at the number, with its row id from
[`run/evidence-digest.md`](run/evidence-digest.md). Where the evidence cannot
settle a question of product intent, it is routed to
[`12-owner-decisions.md`](12-owner-decisions.md) by row id rather than answered.

---

## 1 · Who uses it

Three audiences, and the ranking between them is a finding rather than a
preference: **both predecessors are strongest for the audience that appears
last in this list and weakest for the one that appears first.**

**The server owner — one person, usually alone, usually at the worst possible
moment.** He installs the bot, decides what it is allowed to do in his server,
and is the only person who ever sees most of its configuration. He is the
audience both bots lose: `superbot-next` reaches **39 of its 40 `setup` panels
from no declared entry point at all**, and `superbot` reaches setup only through
an ephemeral on-join launcher message with no route back into the help graph —
`"setup"` is not one of the 43 `SUBSYSTEMS` keys, so the help dropdown can never
list it, and `_AdminPanelView`'s 15 buttons include no Setup (I-13). Two
independent implementations losing the same journey at the same seam is the
strongest single statement in this package about who the successor is built for
first.

**The moderator or staff member — the person who has to act, and later has to
explain what happened.** They need the action itself (warn, timeout, remove,
lock) to be two interactions away, the *reason* recorded, and the record
readable **from Discord**. `superbot` mirrors Discord's own audit-log gateway
event into a log channel with the actor named, including actions taken by humans
in the web client (`lane-claimed`, D-S09). `superbot-next` writes an `audit_log`
row inside the mutation transaction for **every one of its 175 registered
compound ops** — its central architectural claim — and ships **no way to read
them from Discord**: the only `SELECT` against `audit_log` in the tree is the
workflow engine's dedup lookup by idempotency key (`lane-claimed`, D-D09). A
write-only audit spine serves compliance and does not serve the person at 02:00.

**The member — everyone else, who did not read a manual and will not.** They
type something, click something, or ask a question in words. Their entire
experience of the bot is: does it answer, can they find the thing, and does the
thing do what it said. This is the audience `superbot` serves best and its
successor serves worst — see § 3.

**A fourth party is a consumer of the product without being a user of it: the
developer who receives what the bot collects.** [The 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s pipeline exists so
that reports, complaints and feedback *"become durable, easy for the developer
to find and act on — preferably through GitHub or an equally clear
developer-facing system"* (owner, live, 2026-09-04, in flight at
[#1021](https://github.com/menno420/fleet-manager/pull/1021); recorded at
[`run/in-flight-direction.md`](run/in-flight-direction.md)). That statement was
made about `spider-bot`; what the successor inherits is the **shape** — durable
first, projected second — and whether the successor itself hosts a
testing-feedback loop depends on
[`12-owner-decisions.md`](12-owner-decisions.md) **OD-A** and **OD-C**.

---

## 2 · What servers it serves

**Many servers, one guild at a time — and the first guild is a test guild.**
This is [`12-owner-decisions.md`](12-owner-decisions.md) **OD-A**'s recommended
default, adopted here so the rest of this file can be written; it is not settled
by evidence and the row explains why. The operative consequence for the product:
**every setting, permission decision and row of data is scoped to a guild from
the first slice**, because that boundary is cheap to build in and expensive to
retrofit, while running in exactly one guild costs nothing.

If he answers *one server*, roughly the whole first-run configuration surface
leaves this document — the largest simplification available anywhere in the
package — and § 4 shrinks to a single owner console. Nothing else in this file
changes.

**Which real guild is first is his to name** (**OD-C**: the recommended default
keeps `spider-bot` running untouched and makes the successor a third
repository). Until he does, the successor's home is an isolated test application
against a test guild and a test database — the posture
[`13-verdict.md`](13-verdict.md) already fixes.

**The standing ranking rule comes with the same statement and is adopted
verbatim:** *a capability that does not serve server operations, the testing
assistant, the AI community assistant, AI-assisted moderation, or the 12
testers × 14 continuous days number, is later — not wrong.*

---

## 3 · The primary interaction model

### 3.1 · One grouped slash tree is the invocation surface; prefix is a declared alias

This is the single highest-leverage product decision in the package, and it is
decided here rather than routed to him, because it is reversible, evidence-backed
and has owner precedent in his own repository.

**What the evidence says.** Re-derived here from
`superbot-next/manifest.snapshot.json` (parsed as JSON, not read as text): of
**413** commands across **49** subsystems, **386 are `kind=prefix`, 18 `slash`,
9 `both`** — **27 of 413 (6.5 %) reachable without the `message_content`
privileged intent.** The ground-up rebuild is a prefix bot. Worse, its
**required** CI check freezes that vocabulary: `compat/compat-frozen.json` pins
413 prefix command names and 135 aliases and `check_compat_frozen` is one of the
seven required contexts, while the two gates that would notice a modern surface
— the slash-cap budget and intent survivability — are **not required** and run
over populations of **18** and **4** commands (`lane-claimed`, C-D03/C-D04/C-S04).
The repo froze the historical surface into law and left the modern one
ungoverned.

**And the owner already asked for the fix, in the other repository, and it
shipped.** `disbot/cogs/btd6/_unified.py:1-16` (read verbatim here) records the
request dated **2026-06-24** — collapse five prefix groups (`btd6`, `btd6ref`,
`btd6ops`, `btd6strat`, `btd6events`) into a single `/btd6` tree, *"so users no
longer have to remember which prefix owns which action"* — with everyday lookups
flat and the bigger buckets nested one level, explicitly budgeted against
Discord's *"max 25 per level, one level of nesting"*. That is the successor's
invocation model, already designed, already accepted, two weeks before
`superbot-next`'s first commit.

**One decision resolves four separately measured defects and one platform risk.**
It is worth spelling out because each was found by a different lane:

- **Invoker-only panels rendered publicly.** 238 of 314 panels declare
  `audience=invoker` and the presenter computes `ephemeral` from exactly that —
  then drops it on the prefix branch, so five members typing the same command
  leave five permanent public embeds each of which only one of them may click
  (`lane-claimed`, D-D02). On a slash surface ephemerality is native.
- **A declared-ephemeral surface nobody can reach.** 13 of the 14 commands
  declaring `reply_visibility=ephemeral` are slash-only, and slash sync is
  hardcoded off (`sb/app/main.py:616`, I-19) — so the private surface is
  unreachable and `!setup` posts the wizard into whatever channel the owner was
  reading (`lane-claimed`, D-D03).
- **No channel hygiene.** One `delete_after` send exists in the whole of
  `superbot-next`'s runtime, against 113 counted in `superbot`'s cogs alone
  (`lane-claimed`, D-D10/D-S02). `superbot` needs 113 of them *because* prefix
  replies are public and permanent; ephemeral replies make most of that
  machinery unnecessary rather than better.
- **Discovery.** Typing `/` is Discord's only built-in discovery affordance. In
  `superbot` it shows 30 of 243 features; in `superbot-next`, 27 of 413
  (`lane-claimed`, D-D08; the 27 re-derived here).
- **The platform risk.** `message_content` is privileged. A bot that loses or
  never obtains it loses **93.5 %** of `superbot-next`'s command surface in one
  step, and its own written justification for degrading rather than refusing to
  boot rests on a survivor set that does not exist (I-19).

**So the product promise is:** every capability is invocable from the slash tree;
prefix aliases may exist for muscle memory and carry **no unique capability**, so
losing the intent degrades convenience and nothing else. The top-level tree is
budgeted against Discord's caps as executable constants — `superbot-next`'s
`sb/spec/governance.py` is the only place in either repo where
`SLASH_CAP_TOP_LEVEL = 100`, `SLASH_CAP_PER_GROUP = 25` and a one-level nesting
rule exist as code rather than prose (`lane-claimed`, C-S03), and the successor
keeps that file's idea and fixes its population (C-D03: the cap gate discards
every command whose surface is not exactly `slash`, so its real population is 18
of 413).

### 3.2 · Conversation is a route, not a fallback

From the same owner statement: *"People should be able to talk naturally to it
for guidance, complaints, bugs, feedback and improvement ideas."* The design rule
recorded with it and adopted here: **one intake implementation, many entry
points.** A slash command, a button, a form and a sentence typed at the bot all
reach the *same* handler, the same validation and the same durable record;
nobody has to know a command name or a form name, and no entry point is a
second-class path with its own bugs.

This is also the load-bearing reason the AI cannot be a stage on the message
pipeline. In **both** predecessors the conversational surface is exactly that —
`superbot` registers the natural-language stage into `message_pipeline` at cog
setup alongside eight other stages, and `superbot-next` lists `nl_message` and
`passive_onmessage` in its intent contract — so the estate's largest engineering
investment dies with the `message_content` intent and has no slash entry point
to fall back to (`lane-claimed`, C-D12). In the successor, conversation is one
entry point into an intake that has others.

### 3.3 · The bot never says nothing

**This is a product invariant, not a nicety.** Every input addressed to the bot
produces one of exactly three outcomes, always within one interaction: the
result, a **typed refusal that names the reason**, or a did-you-mean.

`superbot` already holds this property and its own source says why. Re-derived
here: `disbot/bot1.py:501` is one global `on_command_error`, and the comment at
`540-546` names the defect it was written for — *"the legacy
`in_allowed = ctx.channel.id in ALLOWED_CHANNELS` gate that suppressed replies
outside hardcoded channel IDs was the root cause of the 'command vanished' UX —
operators in fresh guilds saw nothing when a command failed."* Seven branches
follow, ending in a catch-all at `617-620`; the not-found branch replies at
`602` (`lane-claimed`, D-S01, for the 243-command denominator).

`superbot-next` deleted it. Re-derived here:
`sb/kernel/interaction/adapters/fuzzy.py`'s `prefix_typo_reply` returns `None` on
**both** miss branches — no close match, and a close match classified AUTO on a
read target — and `sb/adapters/discord/message_feed.py:115-127` is the *only*
not-found path in the message feed, so an unrecognised token produces silence.
The rebuild's front door is mute on the surface that is the only one it actually
runs.

**What the successor takes and what it drops.** It takes the always-answer
handler and the did-you-mean *suggestion*. It drops the auto-run rung: no command
is ever executed from a token the user did not type. `superbot`'s fuzzy resolver
is 174 + 69 lines with a documented infinite-loop history (BUG-0014), a
three-outcome model and a hand-maintained `DESTRUCTIVE_COMMANDS` carve-out
(`lane-claimed`, C-D09) — an entire subsystem that exists only because invocation
is free text. On a slash-primary surface, Discord's own command picker replaces
most of it, and what remains is one suggestion string.

### 3.4 · The interaction budget is a committed number

`superbot` states the promise in its own source —
`disbot/cogs/help/panels.py:11`, read verbatim here: *"Every feature is
reachable through its hub in ≤2 clicks"*, recorded with the owner decision of
2026-06-22 that deleted the flat "All Commands" browser once every subsystem was
homed.

**The successor keeps the promise and makes it a gate rather than a docstring.**
The reason is I-13: `superbot-next` wires 314 panels with **200** downward edges
where a connected tree needs at least 313, walking from the 66 `help.*` roots
gives **max depth zero**, and adding framework Back/Home up-links raises the edge
count to 278 and reachability by **zero** panels. That artifact was never a graph,
and no amount of navigation polish on a disconnected graph produces a reachable
product.

So, at product level: **every panel has exactly one declared parent, and every
enabled feature is reachable from the canonical entry point within the committed
budget, at the visibility settings it ships with.** The budget is a number in the
repository that the reachability gate asserts (
[`08-verification.md`](08-verification.md) § 3c, layer 5), and it must model
per-guild visibility or it will score a correctly-hidden subsystem as unreachable
and train its readers to ignore it (I-14).

### 3.5 · Two affordances neither bot has, chosen because the measurement is a zero

- **Autocomplete over any set the user must pick from.** Re-derived here: the
  token `autocomplete` appears **once** in `superbot/disbot` and **twice** in
  `superbot-next/sb`, every occurrence saying it is not implemented. Meanwhile
  the estate carries paginated-select machinery so a user can click *Next* four
  times to find one of ~180 towers or one of 60 roles (`lane-claimed`, C-D07).
  Autocomplete is a platform feature that has been free since 2021.
- **Context menus for per-message actions.** Re-derived here:
  `context_menu` / `ContextMenu` return **zero** hits across both trees. Both
  bots' per-object affordance is a reaction listener with an undiscoverable emoji
  vocabulary (`lane-claimed`, C-D08). "Report this message", "warn this author",
  "star this" are right-click actions on the object they act on.

Neither is a large build. Both are named here because a zero measured in two
independent codebases is evidence about a blind spot, not about difficulty.

---

## 4 · What the operator experience should feel like

**One front door, and it is in the graph.** `superbot` presents **four** setup
entry points — `!setup`, `!setupadvanced`, the on-join launcher, and the Server
Management hub — and the copy behind them fails its own repository's
plain-language rule at 133 counted operator-facing strings, with *"stage"* 55
times, *"final review"* 37 and *"operation"* 36 (`lane-claimed`, D-D12). The
successor has one console, reachable from the canonical entry point like every
other feature, plus an on-join message that **links to it** rather than being the
only way in. The on-join path is worth keeping on its own evidence — `superbot`
creates a private channel, posts with an owner ping, and degrades through two
named fallbacks before DMing the owner (`lane-claimed`, D-S06) — but it is a
convenience, never the route.

**It speaks the operator's language.** Two of the ten top-level labels a
first-time owner reads in `superbot-next`'s wizard are named after internal
mechanisms — *"Cleanup inheritance"* (a resolver precedence chain) and *"Cog
routing"* (a discord.py extension term), both carried over deliberately
(`lane-claimed`, D-D06). A label naming an implementation is a defect with the
same standing as a broken button, and `superbot` already ships the checker shape
for it (`scripts/check_setup_copy.py`, a ratchet with a ceiling — which, as
[`08-verification.md`](08-verification.md) § 3.3 records, is the one ratchet in
that repo *without* a staleness proof; the successor's carries one).

**Nothing it says is frozen state.** `superbot-next`'s help description of a
diagnostic command **is** a captured card title from another guild's runtime, so
an operator reading the listing is told *"setup-readiness — 🛰 Setup Readiness —
0 %"* as if it were a command description (`lane-claimed`, D-D05), and 28
operator diagnostic cards are frozen literals of the *old* bot's runtime
(`lane-claimed`, R1-D1). Every number an operator reads is computed at read time
or is not shown.

**"Online" means a counted, named, reachable command surface.** `superbot-next`'s
readiness endpoint answers 200 while its composition root publishes no slash
command at all (I-19). The successor asserts its command surface against a
committed floor at boot, and a boot that registers fewer routes than declared is
a failed boot, not a healthy one.

**Every degraded state reaches a sink that survives the process.** The measured
counter-example is three independent mechanisms hiding one fact: the degrade
notice appends to a module-level `deque(maxlen=256)` with no sink attached, a
durable latch suppresses it on later boots, and the in-Discord card meant to
surface it is a frozen literal that always renders *"(none)"* (`lane-claimed`,
R4-D02, via I-19). A finding that reaches no sink is this review's own defect
class wearing an observability label.

**The audit spine has a read surface from day one.** See § 1: a write-only audit
log is a compliance artifact, not an operator tool.

---

## 5 · How features are enabled

**Enabling is declared, per guild, in one vocabulary — and `enabled` must mean
`can actually run`.**

The donor is `superbot-next`'s activation model, read verbatim here at
`sb/spec/settings.py:63-69`: every boolean setting declares one of
`ON_BY_DEFAULT`, `ON_WHEN_BOUND`, `ON_WHEN_KEYED`, `OFF_UNTIL_OPT_IN`, and the
compiler enforces the grammar at `:306-321` — a bool-typed setting **must**
declare an activation, a non-bool **must not**, `ON_WHEN_KEYED` must name its
secret, `ON_WHEN_BOUND` must name its binding, and anything with
`external_side_effects` is **forced** to `OFF_UNTIL_OPT_IN`. That last clause is
a privacy decision expressed as grammar, and it is exactly the shape the
successor wants: a policy that cannot be forgotten because a feature that
violates it will not compile.

The second half is `superbot`'s per-guild governance resolver — visibility
resolved per guild with role-scoped overrides, a cache, and an events channel
(`disbot/governance/resolver.py`, `__init__.py:59,152-197`, inspected here) —
which is what makes a feature genuinely absent for a server that did not want it,
rather than merely unlisted. `superbot-next` has no equivalent: `sb/app/main.py`
`pkgutil`-imports **all 49** manifests unconditionally (read here at `:95-108`),
which is why a BTD6 tower-defense wiki is a permanent, non-removable top-level
category in every server, at 74 of 413 commands (`lane-claimed`, D-D11).

**And the rule both bots break, stated as a product requirement:** a feature
reported as ON must be able to run. `superbot-next`'s welcome greeting is
`on_by_default`, renders *"👋 Greet on join — ✅"* straight from the setting, and
**cannot ever fire**: re-derived here, there is no `on_member_join` listener
anywhere in `sb/` — the only registered gateway feeds are `on_interaction`,
`on_guild_join`, `on_message` and the two raw-reaction feeds. An owner can read
the toggle, edit the template, and watch three members join in silence. So:
**every activation state is asserted against the wiring it depends on**, and a
feature that is enabled and unwired is a red gate, not a support ticket.

Two levels, and they are different things that must not be conflated: **boot-time
composition** decides which modules exist in this deployment; **per-guild
activation** decides what a given server sees and may use. The successor needs
both; `superbot` has the second without the first, `superbot-next` has neither.

---

## 6 · How optional modules fit

**OD-19 is the binding constraint** — *"I should be able to add exiting cogs to it
on demand, or be able to slightly alter an existing cog so that it works with
this bot"* — and the evidence says two things about it that pull in opposite
directions.

**It is achievable, and it has already happened.** 54 `disbot`↔`sb` file pairs
score above 0.55 similarity, 8 at ≥ 0.90, and one is **byte-identical** —
`disbot/utils/mining/capacity.py` and `sb/domain/mining/capacity.py` share md5
`64f1665a9fb83a940d95eca5b9492bf2` (I-21, verified). A domain module already
moved between these two architectures unchanged. Portability is not a hope.

**And the rebuild's own extension mechanism cannot carry the interesting half.**
`sb/app/plugin_host.py` fences plugin manifests to
`ALLOWED_FACETS = (commands, panels, settings, events, capabilities)` and rejects
any declaring `HOST_ONLY_FACETS = (stores, data_invariants, wizard_sections)`,
because *"migrations, S12 money lanes, and the G-19 setup registry have no
out-of-tree lane yet."* Measured against its own compiled snapshot: **29 of 49
subsystems declare `stores`**, so **59 % of its own product is ineligible to be
an out-of-tree plugin** (I-10). The mechanism serves the stateless two-fifths and
precisely not the class worth porting.

**So the successor's extension contract carries one requirement neither repo
meets: an out-of-tree module must be able to own data** — ship its own migrations
into a namespaced schema, declare its invariants, and contribute a setup section
— or cog portability fails for exactly the features the owner would want to
bring. The pinning and joint-compile discipline around it is right and is kept
(hash-pinned lock file, one compile pass over in-tree and out-of-tree manifests,
collision checks); the facet fence goes. The mechanical design is
[`06-architecture.md`](06-architecture.md)'s and the per-feature obligations are
[`07-feature-contract.md`](07-feature-contract.md)'s; what this file fixes is the
product promise: **an optional module is a full citizen, including its data.**

**Which of the middle-set community features are core, optional or gone is
routed, not decided** — [`12-owner-decisions.md`](12-owner-decisions.md)
**OD-D**, whose recommended default is that none of `xp`, `karma`,
`leaderboard`, `counting`, `starboard`, `community_spotlight`, `ticket`, `polls`
or `reminders` is core and each is an optional module the extension contract must
be able to carry. That default exists partly to put the contract under real load
in slice one, which is the only way to find out whether it works.

---

## 7 · What the AI is for, and how much it may decide

### 7.1 · The pipeline, verbatim

[The 2026-09-04 AI-authority decision](run/in-flight-direction.md) (owner, live, 2026-09-04; in flight at #1021 at the time of writing,
quoted here under the estate's precedence rule that a live owner statement stands
on its own):

```
Discord event → deterministic pre-check → optional AI analysis
  → TYPED, SCHEMA-VALIDATED VERDICT → deterministic policy engine
  → permission/risk gate → typed operation → Discord API → audit + case record
```

with two rules attached: **free-form prose is never parsed into a moderation
action**, and **invalid or incomplete model output means no automatic action.**
The one-line form is his: **the AI supplies judgement; deterministic code
supplies authority.**

### 7.2 · Why this is not a proposal but a confirmation

The production bot already ships a compatible shape and has for months.
`superbot`'s `disbot/services/ai_tool_catalogue.py` carries **36** catalogued
tools of which **exactly one writes** — `open_support_ticket`, and it writes
*through the audited mutation seam a button uses*, with the comment marking it as
the one action toolset (I-11). The owner's pipeline and the production bot's
proven contract are the same design, reached independently, which is the
strongest warrant in this package for any AI decision in it.

The cautionary half is the successor's. `superbot-next` replaced the closed
36-entry dict with an open registry — a genuinely better abstraction, with
`min_scope` authority that can only narrow and derived grounding allowlists — and
then registered **8** rows from **one** call site, every one a BTD6 factual read
at `AIScope.USER`, **zero write-capable**; the one audited write seam did not
survive the port (I-11). *The mechanism improved and the population collapsed,
and nothing measured the population.* The successor takes the open registry
**with a committed floor on it**, so that collapse is a red diff rather than a
discovery two months later.

### 7.3 · What the AI is for

Three jobs, and no others in the first horizon:

1. **Understanding what a person meant** — turning a sentence into a typed intent
   that the same handlers a button reaches will execute (§ 3.2). The AI is a
   *router and a form-filler* here, and its output is validated before anything
   runs.
2. **Judgement on content and situations** — is this spam, is this a bug report
   or a complaint, is this escalating — emitted as a typed, schema-validated
   verdict with a confidence and a reason, never as prose the code then parses.
3. **Answering questions and guiding people** — read-only, grounded in an
   allowlist derived from the tool catalogue rather than hand-kept, with the
   provider boundary redacting on the way out and on every tool result
   re-entering context (`lane-claimed`, M4-S7).

**Reports are durable first and projected second** — a confirmed report enters
durable private storage with a stable id **before** any GitHub call; GitHub is a
projection and a sink, never the primary store, and never a place private or
interpersonal material is published ([the 2026-09-04 AI-authority decision](run/in-flight-direction.md), adopted verbatim).

**New autonomous moderation starts in shadow mode** with a staff review surface,
because *"reliable"* is his word and an unfalsifiable classifier cannot earn it.

### 7.4 · How much authority, on day one

**Routed, with a default the work can proceed under:**
[`12-owner-decisions.md`](12-owner-decisions.md) **OD-F** — auto-act on low-risk
reversible operations only, preview-and-confirm for medium risk, deny high-risk
and destructive outright, and any later confirmation-free expansion is a new
explicit decision rather than a threshold the system crosses on its own. What is
**not** in question and is fixed here: every AI-initiated write goes through the
same typed operation, the same permission and risk gate, and the same audit row
as the equivalent button — there is no AI-only write path, ever.

---

## 8 · What must work with the AI switched off

**Everything except judgement.** Stated as a testable product property rather
than a reassurance:

- **Every capability has a non-AI route.** If a feature can only be reached by
  talking to it, it is not finished. This is the direct product consequence of
  § 3.2 — one intake, many entry points — and of the measured failure it comes
  from: in both bots the conversational surface is a message-pipeline stage, so
  losing one privileged intent removes the estate's largest investment in one
  step with no fallback (`lane-claimed`, C-D12).
- **Moderation degrades to deterministic rules only.** The pre-check in
  [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s pipeline runs first and is deterministic by construction; with AI
  off, the pipeline is pre-check → policy engine → gate → operation, and the
  optional analysis step is simply absent. Nothing in the authority path was ever
  the model's.
- **A provider outage is a degradation, not an error.** The gateway is
  never-raises with a deterministic provider in the same provider set — that is
  `superbot`'s design, ported (I-4), and it is kept.
- **The bot says so.** An unavailable AI surface renders a stated refusal, not a
  spinner and not silence. `superbot-next` already built the primitive —
  `pending_handler`, a registered handler returning a `BLOCKED` reply, *"declared
  surface, honest refusal, never silent"* (`lane-claimed`, F-S07) — and it is the
  right shape for every unavailable capability, AI or otherwise.
- **The kill switch is per guild and immediate**, and it is one of the settings
  in § 5's vocabulary rather than a deploy-time flag.

**The gate that keeps this true** (and it belongs to
[`08-verification.md`](08-verification.md), named here because it is a product
promise): the journey suite runs a declared population **with AI disabled**, and
every non-AI journey must pass while every AI journey produces its declared
refusal. A journey suite that only runs in the AI-enabled configuration is
measuring one of the two products the bot has to be.

---

## 9 · What makes it one bot rather than fifty cogs

**Breadth is not the disease, and purity was not the cure.** `superbot` carries
43 subsystems for three years with **12 of 883 modules and 1,695 of 243,961 lines
(0.69 %) unreachable from the composition root, and exactly one `TODO` marker**
(`lane-claimed`, CHALLENGE A). `superbot-next` reached 533/533 parity, 3,648
green tests and seven required checks and cannot answer a mistyped command.
Neither outcome is explained by module count, so the coherence answer cannot be
*"fewer features."*

Coherence is six things being singular:

1. **One declaration per feature, and every registry derived from it.** This is
   [`04-root-cause.md`](04-root-cause.md) § 1.2's answer: `superbot`'s debt is
   precisely that one ordinary feature touches ten places, five of them exception
   lists. The parent link is stored once, not twice — the reason a bidirectional
   drift checker had to exist there is that it was stored twice.
2. **One route graph, and the help surface is generated from it.** Not written
   beside it. `superbot`'s hub coverage is 27 of 34 declared children, and the
   split is the whole argument: the shared discovery seam is **19 for 19**;
   hand-rolling is **8 for 15** (I-14). Rendering children is a property of the
   framework, not of the hub author.
3. **One authority model and one audit vocabulary.** `superbot` places authority
   by hand — 166 decorators in cogs, **zero** in the 190 service modules that
   hold the mutations (`lane-claimed`, B-D07) — which is a place every future
   contributor can forget. In the successor, authority and audit are required
   fields of the operation, which is `superbot-next`'s genuine donation
   (`lane-claimed`, CHALLENGE B).
4. **One settings and activation vocabulary** (§ 5), so *"how do I turn this
   off"* has the same answer for every feature.
5. **One error and refusal surface.** `superbot-next`'s user-facing copy is a
   single 28-line table in the kernel with `from_exception` as the only
   constructor (`lane-claimed`, D-S03) — the right structure, and better than
   `superbot`'s split between the command handler and the webhook reporter. Keep
   the structure; keep `superbot`'s seven-branch coverage inside it.
6. **One intake** (§ 3.2), so a bug report filed by voice, by button and by form
   is the same record.

**And one structural test of coherence, which is free once § 3.1 is adopted:**
the top-level slash tree must fit Discord's 100-command budget with room, as
executable constants rather than prose. A product whose top-level tree cannot be
curated to fit has stopped being one bot, and the budget says so in CI before a
human has to.

---

## 10 · How a new feature joins the journey

This is the product-level shape; the normative checklist is
[`07-feature-contract.md`](07-feature-contract.md) and the rungs are
[`08-verification.md`](08-verification.md) § 4.

**It starts by naming an audience and a journey.** Which of § 1's audiences, and
what they are trying to finish. A capability that cannot name one is an optional
module (§ 6) or it is not built (**OD-D**).

**It arrives as one declaration** carrying: its name and owner; its position in
the route graph (exactly one declared parent); its authority tier; its settings,
each with an activation value from § 5's four; its operations, each with an audit
verb; any AI tools it exposes, with their scope and whether they write; and any
data it owns, as migrations in its own namespace.

**Every registry is derived from that record** — the help entry, the parent's
button, the settings page, the permission table, the AI tool exposure, the audit
vocabulary. There is no second place to edit, which is the only durable answer to
§ 9.1.

**Then it climbs the ladder, and it cannot skip a rung** (R0 declared · R1 wired
· R2 journeyed with its effect asserted · R3 reachable within the budget at its
shipped visibility · R4 driven by a human in a real guild with every field of the
record resolvable · R5 operated across a restart and a degraded dependency). Two
of those rungs are product promises rather than engineering hygiene, and they are
the two this package exists for: **R3 — if it is not reachable it is not
shipped**, and **R2's effect assertion — if the state did not change, it did not
happen.**

**And its copy is part of the feature.** Operator-facing labels name what the
person is doing, not what the code is doing (§ 4); every number shown is computed
at read time; and a string that would have to change for the feature to improve
is never pinned by an acceptance oracle (`lane-claimed`, D-D07: 128 of 2,102
distinct user-facing strings in `superbot-next` are pinned in goldens *with*
internal jargon, so improving that copy reds a required check).

---

## 11 · Non-goals

Each with the one reason it is out, and none of them a judgement about whether
the thing is good.

- **Not a games platform.** Casino, blackjack, economy, inventory, treasury,
  mining, fishing, farm, creature, BTD6 and Project Moon do not transfer —
  OD-16, and the scale is why it matters: BTD6 alone is 74 of 413 commands
  (`lane-claimed`, D-D11) and one AI-content vertical is 30,923 of 59,744
  measured lines of `superbot`'s games/economy surface (`lane-claimed`, M3).
- **Not byte-parity with either predecessor.** The oracle never ran the shipping
  renderer ([`08-verification.md`](08-verification.md) § 3b), and the owner has
  rejected the build those bytes pin.
- **Not a replacement for the production bot**, and no promise of one — **OD-B**;
  the promise is what converted `superbot-next`'s honest work into a failure.
- **No production data import** — **OD-E**; every migration that does not happen
  is a class of risk that does not exist.
- **Not a prefix-parity product.** 413 frozen prefix names and 135 aliases are a
  2020-era invocation vocabulary, and freezing it in a required check is what
  blocks the migration that matters (`lane-claimed`, C-S06/C-D04).
- **No free-form prose parsed into an action, ever** — [the 2026-09-04 AI-authority decision](run/in-flight-direction.md); an invalid or
  incomplete model output means no automatic action, which is a hard stop rather
  than a threshold.
- **No AI-only write path and no autonomous destructive action** — **OD-F**'s
  default; the AI reaches the world through the same typed operation, gate and
  audit row a button does.
- **No command auto-executed from a typo.** The suggestion survives; the auto-run
  rung does not, and its own repository records the infinite-loop history
  (`lane-claimed`, C-D09).
- **No runtime code hot-swap.** Modules load at boot; the in-Discord lever is the
  per-guild *disable* of § 5, which is a different and safer thing than unloading
  code from a live process.
- **Not a documentation program.** The EAP added 183 surviving documentation
  files to `superbot` in fourteen days and two runtime files (I-9); the
  successor's documentation is its declaration and its record, and prose is not a
  deliverable.
- **Not a publicly listed bot in this plan's horizon.** Crossing ~100 guilds
  triggers Discord verification and changes the intent model this whole document
  is built on; if that becomes the goal it is a new decision, not a growth
  milestone.

---

**Where this file could not decide, it routed rather than invented:** OD-A (one
server or many, which moves the whole of § 4), OD-B (whether replacement is ever
promised), OD-C (whether the successor is a third repository or `spider-bot`
grown into one), OD-D (which community features are core, optional or gone), OD-E
(whether any production data carries forward) and OD-F (how much authority the AI
holds on day one). Every one has a recommended default in
[`12-owner-decisions.md`](12-owner-decisions.md), and this document is written
under those defaults so that the next session can proceed on all of it while any
of them is still open.
