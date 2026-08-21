# Source review — what to keep from each bot

> **Status:** `reference` within this plan · reviewed against `main` on
> 2026-08-21. This is a planning comparison, not a replacement for either
> repository's own truth.

## Bottom line

The two bots are complementary evidence:

- `superbot` proves which behaviors and interaction patterns are useful in a
  real Discord server. It also exposes the cost of accumulated coupling,
  duplicate state/config paths, oversized feature scope, and production-bound
  development.
- `superbot-next` proves that a typed layered kernel, registries, workflow
  seams, provider-neutral AI, and extensive automated tests are achievable. It
  also proves that architecture and byte parity can be green while the product
  journey is wrong.

The new bot therefore ports **contracts and observed behavior**, never entire
directories by default.

## Evidence pins and important measurements

| Evidence | Result that affects this plan |
|---|---|
| `superbot` `5e3a667b` | Live production source; 59 `INITIAL_EXTENSIONS` entries; mature setup, role, welcome, moderation, logging, ticket, utility, AI, and help surfaces |
| `superbot-next` `d5f66dc2` | 49 subsystems + kernel, 3,660 tests, 533 goldens; layered manifests/workflow/audit architecture; never deployed in production |
| live audit 2026-08-05 | 1,327 targets, 314 panels, 640 buttons; 153/314 panels button-less; help 60/66 button-less; capture-world literals presented old state as live state |
| playtest finding 2026-08-05 | setup/welcome/roles/reminders/polls/logging/moderation are high-value; native Forums beat tickets for public QA; both bots fail to enforce their feature-routing policy |
| current Layer-2 entries | production bot frozen and protected; rebuild direction unresolved until this owner request; both repos have auto-merge/CI traps |

## Comparative disposition

| Area | `superbot` | `superbot-next` | New bot decision |
|---|---|---|---|
| Runtime shape | Large discord.py process with cogs, services, views, runtime helpers, and years of incremental seams | Clear `spec → kernel → domain → adapters → app` layering | **KEEP the layered direction**, simplify it, and pin boundaries with import/ownership tests |
| Modularity | Cogs can be loaded/unloaded, but responsibilities and config paths are spread | Manifest-declared subsystems and central registries | **MERGE:** manifest-declared internal modules plus boot-time feature profiles; no runtime code hot-unload in MVP |
| Navigation | Proven button-first Home/help experience; real users rarely type commands | Help text ported without the live route graph | **KEEP behavior, REBUILD implementation:** one route registry generates Home, help, command metadata, and reachability tests |
| Setup | Deep guided wizard, resource provisioning, previews, role/channel templates, diagnostics | Well-separated setup domain and typed operation/workflow patterns | **MERGE:** preserve the user journey, implement every change as a typed idempotent setup operation with preview/apply/verify |
| Access control | Bootstrap escape hatch and command-access resolver work; feature-routing policy is stored but not enforced | Authority/workflow seams are stronger; subsystem routing still not live | **REBUILD centrally:** caller authority × guild feature policy × channel/role access evaluated once before dispatch |
| Roles/channels | Mature features and many edge cases | Resource lifecycle concepts and audited workflows | **KEEP behaviors that serve setup/moderation; REBUILD on one lifecycle service per resource** |
| Welcome/onboarding | Entry role, join/leave/DM configuration | Ported domain patterns | **KEEP and simplify**, add game/build-role onboarding and completion state |
| Moderation/safety | Mature automod, security, image moderation, logs | Typed ops, authority and audit seams; AI moderation is advisory | **MERGE:** deterministic enforcement + audited cases; AI triage/assist under policy, never an unlogged direct action |
| Feedback/tickets | Full private ticket system | Instance-lifecycle design patterns | **DEFER tickets to private support.** Build Forum enhancement, structured intake, duplicate linking, status/tags, and export first |
| Utility | Polls and reminders already useful | Deferred action and workflow patterns | **KEEP** polls/reminders/playtest events behind one scheduling service |
| AI provider layer | Active provider-neutral gateway, per-task routing, safety/redaction, policy, diagnostics | Cleaner kernel port of OpenAI/Anthropic/deterministic adapters | **KEEP the contract, REBUILD clean:** provider plugin registry, per-task route, fallback/circuit-breaker, budget, trace |
| AI tools | Old bot has many read-only game/server tools and an orchestration policy; writes remain deliberately separate | Only eight real BTD6 tools registered; strong scope-narrowing catalogue | **KEEP registry and scope rules; DROP BTD6 tools; ADD server/playtest read and typed write tools** |
| AI memory | In-process, per-channel cache with a small floor | Same kernel concept | **REPLACE** with Postgres-backed scoped summaries/facts, explicit retention and forget controls |
| AI autonomy | Mainly explain/recommend; state changes require existing UI/services | Tool orchestration can plan/execute/verify, but actual server write tools are absent | **IMPROVE:** risk-classed Act mode from day one, using the single deterministic workflow engine |
| Configuration | Multiple legacy scalars plus typed policy/projection and drift diagnostics | Typed config accessor and manifest settings | **KEEP typed config only.** No legacy projection layer in a new repo |
| Persistence | Postgres, mature but many subsystem tables and direct historical paths | Per-domain stores plus central workflow audit | **KEEP Postgres and owned repositories**, add transactional outbox and idempotency keys |
| Observability | Metrics, health server, audit/logging surfaces; some duplicate reporting | Structured kernel bands and planned D4 surfaces | **MERGE:** structured logs, metrics, health/readiness, correlation IDs, audit explorer, no dashboard requirement initially |
| Testing | Large unit surface and real production behavior, but older coupling | Extensive unit/integration/e2e/golden gates; parity measured the wrong property | **KEEP test depth, REPLACE headline metric** with journey/effect/reachability/access/idempotency assertions |
| Deployment | Railway worker is live; source merge can restart it | Railway/Docker shape exists but never production-deployed | **KEEP Railway as first venue**, separate test app/service/DB; immutable build and explicit promote/rollback |
| Games/economy | Large mature content surface | Almost all of it ported | **DROP from MVP** and from default dependency graph. Future community mini-features require a real demand and plugin contract |

## Preserve from `superbot` — behavior and lessons

### Preserve behavior

- One obvious Home/help entry and persistent button navigation.
- Guided setup with jargon-free essentials before advanced settings.
- Safe bootstrap access so a bad policy cannot lock the server owner out.
- Welcome, entry roles, reaction/self roles, moderation, automod, logging,
  server/channel/role management, reminders, polls, starboard-like showcasing.
- Per-guild configuration and genuine multi-guild teardown/cleanup.
- AI provider gateway, task routing, safety/redaction, diagnostics, decision
  audit, instruction profiles, behavior presets, and explicit unavailable
  fallbacks.
- Central service-layer mutations and preview-before-apply where already
  proven.

### Preserve lessons, not code

- A stored routing policy is not a feature until the dispatcher consults it.
- Multiple config representations require drift machinery forever; a new repo
  should start with one typed source.
- Process-local AI memory disappears on restart and cannot support durable
  autonomous work.
- A giant command surface pollutes discovery even if disabled commands are
  harmless.
- Production-bound development makes every ordinary change operationally
  expensive.

## Preserve from `superbot-next` — contracts and guards

### Preserve patterns

- Explicit layers and import-direction guards.
- Manifest/registry ownership of commands, panels, settings, events, stores,
  setup sections, AI tasks, and AI tools.
- One workflow engine for state changes with typed authority, idempotency,
  before/after evidence, audit rows, and post-commit events.
- Provider-neutral AI contracts and adapters behind one gateway.
- Tool selection that can only narrow authority; a profile can never grant a
  tool above the caller's scope.
- Central config accessor, schema migrations with checksums, testable namespace
  registry, and deterministic composition root.
- In-process adapter tests covering slash commands, components, modals, and
  writes.

### Reject or correct

- Do not make the old bot's output corpus the product acceptance target.
- Do not ship constants that describe live system state.
- Do not count a rendered refusal as a ported capability.
- Do not register an enabled feature without a real handler and a reachable
  route.
- Do not load every module unconditionally.
- Do not make message-content intent the silent difference between an online
  and unusable bot.
- Do not leave lifecycle/failure-mode docs as empty generated skeletons.

## Feature disposition for the first release

### Build now

- Home/help/navigation
- setup and server profiles
- roles, channels, permissions, welcome/onboarding
- logging, moderation, automod, security baseline
- build registry and announcements
- tester enrollment/cohorts
- Forum-based bug/feedback enhancement
- playtest events, reminders, polls
- run/clip/replay sharing metadata
- AI gateway, policy, memory, tools, audit, diagnostics
- operator status/support report

### Build after MVP evidence

- invite attribution
- GitHub issue export/sync
- community highlights/starboard
- XP/karma/light participation rewards
- LFG/event discovery
- web dashboard
- game-client webhook/API integration
- richer analytics and cross-game benchmarking

### Explicitly excluded unless later re-approved

- casino, blackjack, economy, inventory, treasury
- mining, fishing, farm, creature, BTD6, Project Moon
- runtime code loading/unloading from Discord
- arbitrary code/shell/database tools for AI
- general-purpose ticketing as the public bug pipeline
- mass migration of legacy production tables

## Acceptance correction carried into the new plan

The important unit is a **user journey with an observable effect**, not a
command, panel, subsystem, golden string, or manifest row. Every planned
feature therefore needs:

1. a route from Home;
2. an authority decision;
3. a typed operation or read model;
4. a visible result;
5. an audit/metric where appropriate;
6. a deterministic fallback when AI is involved;
7. an automated journey/effect test;
8. a real test-guild drive before production claims.
