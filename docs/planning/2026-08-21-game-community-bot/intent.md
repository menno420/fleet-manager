# Intent map — Game Community Bot

> **Status:** `plan` · working map promoted because it defines the durable
> pre-repository product intent. Owner words, prior decisions, and inference
> remain separate.

## Main ideas

1. Build a basic Discord bot for a game-testing server that also works as a
   general game-community bot.
2. Preserve the best behavior and architecture from both existing bots without
   preserving their unrelated scope or defects.
3. Make AI substantially more capable and autonomous from the beginning, with
   more freedom than either bot currently exposes.

## EXPLICIT — this request

- Review `fleet-manager` and find the new Discord-bot direction.
- Review both `superbot` and `superbot-next`.
- Create a comprehensive plan in a new, discoverable section of
  `fleet-manager`, using the repository's documented standards.
- The first bot should be basic, keep the best of both predecessors, and focus
  on game testing plus a general game server.
- AI integration is central, and the AI should start with more freedom than the
  existing bot.

## ESTABLISHED — prior owner decisions and measured constraints

- The owner rejected further feature work on the live bot because its
  architectural debt makes it the wrong improvement surface. The replacement
  direction is **server bot first, no game features**. Evidence:
  [`2026-08-05-playtest-discord-and-superbot-value.md` §6](../../findings/2026-08-05-playtest-discord-and-superbot-value.md)
  and the live-audit purpose line.
- `superbot` is the live production bot and is frozen; merges touching bot
  sources can restart production. Its server-management behavior is valuable,
  but it is not a safe foundation.
- `superbot-next` is a real layered rebuild, not a shell, but golden parity
  validated recorded bytes rather than live effects. Its help front door is
  measured at 60/66 panels with no buttons. It is an architecture donor, not
  proof of a ready product.
- The old bot's true product interaction is a Home/help graph: one entry point,
  features reached by buttons in about two taps. Command names are secondary.
- Both bots contain cog/subsystem routing data without a working live admission
  check. The new bot must enforce feature policy at the central dispatcher.
- Discord-native Forum channels are the preferred bug/feedback container;
  private tickets are for private support, not the main QA pipeline.
- `fleet-manager` may hold this cross-repository pre-build plan, but product
  architecture and live state move into the new repository as soon as it
  exists.
- Estate standards favor one finished thing at a time, verify-first behavior,
  a small meaningful CI surface, exact ownership boundaries, and visible
  operator evidence.

## DERIVED — architectural recommendations

- Create a clean repository rather than delete 30+ subsystems from
  `superbot-next`. This is derived from scope and migration risk, not a prior
  owner quote.
- Build a multi-game core with game profiles in data. The first profile is
  `spider-swing`; the core should not hardcode it.
- Prefer slash commands, persistent buttons, selects, and modals as the primary
  UX. Keep an optional prefix alias only if Discord privileged intent approval
  and actual user behavior justify it.
- Give AI more freedom through a risk-scored tool policy, not by allowing model
  output to write tables or call Discord directly.
- Start the first write-capable AI vertical slice early: inspect guild → build
  setup draft → owner confirms → execute typed operations → verify → audit.
- Use Postgres for durable, scoped AI memory. The predecessor's in-process
  conversation cache is not adequate for restarts, multiple workers, retention
  controls, or evidence-backed autonomous work.
- Keep one process and one deployable service for the MVP. Modular code and a
  transactional outbox give clean boundaries without premature microservices.

## OPEN — genuine owner decisions

All are non-blocking during planning; defaults are recorded in the root plan.

- **GCB-1 (HIGH at execution):** the repository's final name and owner. It
  changes the canonical home and must be confirmed before creation.
- **GCB-2 (HIGH at execution):** which Discord application/token is the test
  identity. A production identity is never inferred from an environment name.
- **GCB-3 (HIGH at execution):** provider credentials and spend ceiling. The
  architecture is provider-neutral; enabling paid traffic requires the owner.
- **GCB-4 (HIGH policy):** whether any medium-risk operation may become
  confirmation-free after test-guild evidence. Default remains confirmation.
- **GCB-6 (HIGH migration):** whether a real production guild needs legacy data
  imported. Default is no import.

The server purpose, multi-game posture, server-first scope, AI-first direction,
and use of both repositories as evidence are **not open**; they are stated in
the current request or already recorded.

## GOAL

Create a maintainable, observable, multi-guild Discord bot that makes a game
testing/community server easy to create and run, gives its owner a powerful AI
operator with bounded autonomy, and remains fully useful when AI is disabled or
unavailable.

## NON-GOALS

- Rebuild all 49 old subsystems or achieve command-count parity.
- Port casino, economy, BTD6, mining, fishing, creature, farming, tournaments,
  or unrelated content into the MVP.
- Turn Discord into an issue tracker when native Forums already solve the
  conversation problem.
- Make moderation, setup, or server health depend on an LLM.
- Give an LLM direct database access, arbitrary code execution, raw Discord API
  access, secret access, or a second mutation path.
- Build a web dashboard before the Discord-native owner surface proves
  insufficient.
- Modify or replace the live production bot during development.
- Treat a large golden corpus, command count, or rendered text parity as proof
  that a user journey works.

## SUCCESS

The owner should be able to say “yes, that is what I meant” when all of the
following are true:

1. A new game-testing server can be provisioned safely from one guided flow.
2. Every enabled function is understandable and reachable from Home without
   memorizing commands.
3. Testers can join, choose game/build roles, find the current build, report a
   bug or feedback, join a playtest, and share a run with little friction.
4. Staff can moderate, announce builds, triage feedback, schedule sessions, and
   see what changed.
5. The AI can perform real low-risk work, proposes medium-risk work with a
   preview, and cannot exceed the caller's or guild policy's authority.
6. Every AI decision and tool call is attributable, inspectable, bounded, and
   reversible where the operation allows it.
7. Provider failure degrades to deterministic UX; it never takes the bot down.
8. A second game can be added through a profile/integration module without
   copying the bot.
9. Test-guild evidence, not screenshots or byte parity, proves the main
   journeys.

## Intent status

`INTENT STATUS: RESOLVED` for planning.

The OPEN items are execution gates whose defaults do not alter this plan's
product outcome. No unanswered question prevents the comprehensive plan from
being written or reviewed.

## Decisions flagged

- **MEDIUM:** new repository instead of stripping `superbot-next`. Chosen for
  clean scope, lower deployment risk, and a truthful test surface. Confirmed at
  GCB-1 before creation.
- **MEDIUM:** Discord-native UI first, prefix compatibility optional. This
  avoids making the MVP depend on message-content intent while preserving the
  predecessor's one-entry interaction model.
- **MEDIUM:** one deployable service for MVP. Split workers only after measured
  load, isolation, or deployment cadence justifies it.
- **MEDIUM:** no web dashboard in MVP. Structured logs, metrics, an owner Home
  panel, and exportable reports are the first observability surface.
