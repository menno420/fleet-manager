# Game Community Bot — authoritative pre-repository plan

> **Status:** `plan` · 2026-08-21 · owner-directed
>
> **Authoritative for:** the intended outcome, scope, architecture, delivery
> order, migration route, and evidence gates for the new Discord bot **until
> its own repository exists**.
>
> **Not authoritative for:** the internal state of `superbot` or
> `superbot-next`, live Discord/Railway state, provider prices, or the future
> bot's post-creation implementation truth. The source repositories and live
> services always win. When the new repository is created, this plan is copied
> into that repo, reconciled against its first commit, and this folder becomes
> a dated pointer rather than a second product source of truth.

## NARROWED 2026-09-04 — the owner said what the bot is FOR, and it is one server

`OWNER`, live, and it is newer than everything below including the OD-19
amendment:

> *"Spider Bot exists to manage the Slingy Spider server and help during testing
> of the game. It should become a reliable automoderator with heavy AI
> integration. People should be able to talk naturally to it for guidance,
> complaints, bugs, feedback and improvement ideas. Those reports should become
> durable, easy for the developer to find and act on — preferably through GitHub
> or an equally clear developer-facing system."*

**What this does to this plan.** The decision headline below opens *"Build a
clean, **multi-game** Discord bot repository"* and § "Product success in one
screen" describes a fresh game-server owner inviting the bot and running a setup
wizard. **That is no longer what `spider-bot` is being built to be.** This plan
stays authoritative as the **architecture and source research** — the donor
disposition in [`source-review.md`](source-review.md), the AI-autonomy model and
typed-operation discipline in [`architecture.md`](architecture.md), the evidence
gates in [`verification-and-operations.md`](verification-and-operations.md) are
all still the best record anyone has and are being built on. It is **no longer**
the description of the product. A session must not re-broaden `spider-bot` into
the multi-game platform on this document's authority.

**Two open items below are closed by the same sentence:**

- **`OQ-GCB-REVIEW-SCOPE`** — *"what must the review bot actually do?"*, open
  since 2026-08-23, the gate this README's "Next executable action" put ahead of
  everything: **the testing-and-feedback loop, plus moderation of the server
  that runs it.** The four candidate scopes in the owner queue are answered by
  his own words rather than picked from.
- **The sequencing conflict this file records** (roadmap Phases 1–4 breadth
  versus OD-19's small review bot first) **resolves toward OD-19 and stays
  there.** The AI spine is built — but as the moderation-and-intake spine of one
  server, not as the platform kernel [`delivery-roadmap.md`](delivery-roadmap.md)
  Phase 1 describes. That roadmap is **not** the executable order for
  `spider-bot` any more; the repo's own plan is.

Canonical intent: [`../../repos/spider-bot/intent.md`](../../repos/spider-bot/intent.md).
The four rules his statement generates are stamped at spider-bot's entry
point: [`docs/repos/spider-bot/README.md`](../../repos/spider-bot/README.md).

## AMENDED 2026-08-23 — OD-19 narrows the first slice and adds one hard constraint

`OWNER`, live, refining OD-16. Read this before the headline below: it does not
replace the plan, it **orders** it.

> *"both superbot repos should eventually be consolidated into one new one, but
> first there should be a smaller review oriented bot for the game server, tho we
> should probably keep in mind that it should still be expandable, meaning that I
> should be able to add exiting cogs to it on demand, or be able to slightly alter
> an existing cog so that it works with this bot, tho I think that it's important
> that these bots remain seperated."*

Three consequences for this plan:

1. **The first build is smaller than the headline.** A **review-oriented bot for
   the game server** is slice one. The multi-game community bot below is the
   destination, not the opening scope — so Phase 0 should size for the review
   bot and leave room, rather than standing up the full scope first.
2. **Cog portability is a stated requirement, not an emergent nicety.** He must be
   able to add an existing cog **on demand**, or make one work with **slight**
   alteration. That is a constraint on the extension interface at design time: it
   has to stay close enough to the existing bots' cog shape that adaptation stays
   small. Treat "how far does an existing cog have to bend?" as a Phase 0
   acceptance question, not a later discovery.
3. **The bots remain separated — standing constraint.** The eventual
   consolidation he describes is of the two `superbot` **repositories** into one
   new repository. It is **not** a merge of running bots. Nothing in this plan
   should converge the deployments.

### The executable roadmap now contradicts this, and that is not resolved here

`MEASURED` 2026-08-23 (`@codex`, fm #937). Telling Phase 0 to "size for" the
review bot is **not** enough, because
[`delivery-roadmap.md`](delivery-roadmap.md) still orders the work the other way:

| roadmap phase | what it requires |
|---|---|
| **Phase 1** | the full kernel, policy and **AI spine** |
| **Phase 2–4** | Home/discovery/access, setup, then **community and safety core** |
| **Phase 5** | the **game testing loop** |

**This is a POSSIBLE sequencing conflict, not a measured one** (`@codex`, fm
#938). Calling Phase 5 *"OD-19's first slice"* assumes the review bot **is** the
game-testing loop — and his words say only *"review oriented bot for the game
server"*. Whether that means playtest capture, bug intake, build handoff or
feedback triage is **unknown and is `OQ-GCB-REVIEW-SCOPE`**. Asserting the
identity would be the product-intent inference this section exists to refuse.

What *is* certain: OD-19 puts a **small** review bot first, while the roadmap
requires the AI spine and the community core across four phases before any
testing-loop work. So a GCB session following the dependency order would very
likely reach the review bot last. **Confirm the scope first, then re-sequence.**

**Not re-sequenced here, deliberately.** Inserting a review-bot slice with its
own exit gate is product-design work on an owner-gated plan, and OD-19 is one
sentence — what "review oriented" covers (playtest capture? bug intake? build
handoff? feedback triage?) is **not** specified, and inventing that scope would
be manufacturing product intent, which
[`../../intent.md`](../../intent.md) § 8b forbids.

**So this is the first work a GCB session does, before Phase 0:** get
`OQ-GCB-REVIEW-SCOPE` answered — what the review bot must actually do — and only
then put its slice and exit gate ahead of the destination breadth. The queue entry
carries four candidate scopes for him to pick from. Until then the roadmap and
OD-19 disagree, and **OD-19 wins** — it is the later owner statement.

**GCB-1 is unchanged and still owner-gated** — none of the above authorises
creating the repository.

## Decision headline

Build a **clean, multi-game Discord bot repository** whose first real job is
running a game-testing community and whose second job is remaining useful as a
general game server.

- Use `superbot-next` as an **architecture and kernel-pattern donor**, not as a
  codebase to trim and not as a parity target.
- Use live `superbot` as the **behavior, operator-UX, and feature oracle**, not
  as the new foundation.
- Keep both existing repositories and the live production bot untouched during
  the build.
- Make AI a first-class operating layer from the first vertical slice. The AI
  may act with meaningful freedom, but every side effect passes through the
  same typed, permissioned, auditable service operations used by buttons and
  commands.
- Ship a small server-management and playtest core first. Do not carry over the
  casino/economy/game-content surface merely because it exists.
- Make the bot multi-game by data model and configuration. `spider-swing` is
  the intended first playtest consumer; adding another game must not require a
  new bot fork.

This resolves the direction fork recorded in
[`docs/repos/superbot-next/README.md`](../../repos/superbot-next/README.md):
the old cutover ladder is not the build plan, and the 2026-08-05 server-first
direction is retained and upgraded into an implementation-ready plan.

## Why a new repository is the default

`superbot` is live, frozen, tightly coupled, and a merge can restart production.
`superbot-next` has a cleaner layered kernel, but it also carries 49 subsystems,
a 2.3 MB generated manifest, a parity corpus that certified captured text as
working behavior, and no production deployment history. Starting clean is the
lowest-risk way to preserve the good boundaries without inheriting either
repository's accidental product scope.

This is a **reversible planning decision**. The owner confirms the repository
name and creation immediately before Phase 0; nothing in this planning PR
creates a repository, bot application, secret, server, or deployment.

## Read this section in order

1. [`intent.md`](intent.md) — what the owner said, what was already decided,
   what is inferred, and the remaining owner calls.
2. [`source-review.md`](source-review.md) — the evidence-backed comparison and
   the keep/rebuild/drop disposition.
3. [`product-and-ux.md`](product-and-ux.md) — actors, server shape, workflows,
   commands, and feature boundaries.
4. [`architecture.md`](architecture.md) — modules, ownership boundaries,
   deterministic event flow, AI autonomy model, persistence, and deployment.
5. [`delivery-roadmap.md`](delivery-roadmap.md) — dependency-ordered phases,
   issue-sized slices, and done-before-next gates.
6. [`migration-and-rollout.md`](migration-and-rollout.md) — how the two existing
   bots are used safely, live-guild validation, cutover, and rollback.
7. [`verification-and-operations.md`](verification-and-operations.md) — CI,
   tests, observability, security, runbooks, and release evidence.

## Source baseline

The plan was derived from current `main` plus the measured 2026-08-05 live
audit. Pins make the evidence reproducible; they are not claims that the repos
can never move.

| Source | Pin reviewed | What it contributes |
|---|---|---|
| `menno420/fleet-manager` | `9f8eb079` | Current intent, Layer-2 handoffs, server-first findings, operating standards |
| `menno420/superbot` | `5e3a667b` | Live behavior, setup/navigation UX, server operations, AI platform, production traps |
| `menno420/superbot-next` | `d5f66dc2` | Layered kernel, manifests, workflow/audit seams, tests, and the measured parity/reachability failure |

Primary fleet evidence:

- [Playtest Discord and bot value finding](../../findings/2026-08-05-playtest-discord-and-superbot-value.md)
- [`superbot-next` live audit](../../findings/2026-08-05-superbot-next-live-audit.md)
- [Three-repo state audit](../../findings/2026-08-05-three-repo-state-audit.md)
- [`superbot` Layer-2 entry](../../repos/superbot/README.md)
- [`superbot-next` Layer-2 entry](../../repos/superbot-next/README.md)

## Product success in one screen

The MVP is successful when a fresh game-server owner can invite the test bot,
run one setup flow, preview and approve a plan, and receive a usable server with:

- a clear Home panel from which every enabled feature is reachable in at most
  two interactions;
- safe roles, channels, permissions, welcome, logs, moderation, and recovery;
- native Discord Forum channels for bugs and feedback, enhanced rather than
  replaced by the bot;
- build announcements, tester onboarding, playtest sessions, reminders, polls,
  and feedback triage;
- an AI operator that can inspect the guild, propose a typed plan, execute the
  owner-approved operations, verify their effects, and explain exactly what it
  did;
- no casino, economy, BTD6, or unrelated content loaded;
- a provider outage, AI disable switch, or failed AI request that never makes
  the deterministic server-management features unavailable.

## Owner calls before implementation

These do not block this plan. Defaults are chosen so the next session can
prepare everything else; the owner confirms them before the named irreversible
step.

| ID | Call | Recommended default | Needed before |
|---|---|---|---|
| GCB-1 | Repository name | `superbot-community` | creating the repository |
| GCB-2 | Discord application | use a separate test application/token | first live guild drive |
| GCB-3 | Initial providers, Discord-data policy, and monthly spend rail | approve allowed source classes and private/staff exclusions, provider retention/training terms, guild/user disclosure and consent, deletion/export propagation, then enable the already-supported OpenAI + Anthropic adapters with a hard budget and per-task routing | sending any Discord-derived content to a non-deterministic provider in the test guild |
| GCB-4 | Initial AI autonomy policy | auto-act only on low-risk reversible tools; preview + owner confirmation for medium-risk; deny high-risk/destructive tools; any later confirmation-free medium-risk expansion is a new explicit decision | enabling AI Act in the test guild |
| GCB-5 | First game profile | `spider-swing`; keep the core multi-game | seeding the first real server |
| GCB-6 | Legacy production data | import nothing for MVP; add a dry-run migrator only if a real guild needs continuity | any production cutover |

## Explicit non-actions

This plan does **not** invite a bot, create a Discord application, create or
rename a GitHub repository, touch Railway, move production data, alter either
existing bot, or promise a production cutover. Those are later, separately
verified phases.

## Next executable action

**Two gates now, not one** (amended 2026-08-24, `@codex` fm #938 — this section
still sent a session straight into the unresequenced roadmap the OD-19 amendment
says not to execute).

1. **`OQ-GCB-REVIEW-SCOPE` — what must the review bot actually do?** Owner-only.
   Four candidate scopes are in [`../../owner-queue.md`](../../owner-queue.md).
   Until it is answered, the first slice has no definition and the roadmap cannot
   be re-sequenced against OD-19.
2. **GCB-1** — confirm the clean repository and its name. Owner-only.

**Then, and in this order:** re-sequence [`delivery-roadmap.md`](delivery-roadmap.md)
so the review-bot slice and its exit gate come *before* the destination breadth
currently spread across Phases 1–4 — **do not skip this and start Phase 0 as
written**. Only then create the repository from a minimal substrate-kit seed and
execute Phase 0: transplant this plan, add the architecture decision record,
establish one required CI check, and land an empty but observable Discord process
before any feature module is ported.
