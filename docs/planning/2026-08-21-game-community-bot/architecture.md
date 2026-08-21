# Architecture plan

> **Status:** `plan` · target architecture, not an implementation inventory.
> Concrete library versions and hosting settings are chosen and locked in the
> new repository after its seed is verified.

## Architecture goals

1. One understandable mutation path for commands, buttons, scheduled work,
   integrations, and AI.
2. Deterministic server operation even when every AI provider is off.
3. More useful AI autonomy without giving a model ambient authority.
4. A small deployable unit with strong internal ownership boundaries.
5. Multi-guild and multi-game behavior by construction.
6. Evidence at each boundary: authorization, operation, Discord/database
   effect, post-commit event, and user-visible outcome.

## Runtime shape

Start with one Python 3.12 deployable service and one Postgres database. The
service contains the Discord gateway, application services, scheduler/outbox
consumer, AI orchestration, and a small health/readiness endpoint. Concurrency
is explicit inside that service; it is not split into microservices until
measured isolation or scaling needs justify the operational cost.

Use a locked dependency set, immutable container image, schema migrations with
checksums, and separate development/test/production configuration. Railway is
the first deployment venue because the fleet already operates it, but the
container and health contract must remain provider-neutral.

## Package and ownership model

```text
src/game_community_bot/
  app/          composition root, lifecycle, scheduler, health
  kernel/       config, auth, database, workflow, events, UI, AI, observability
  domain/
    guilds/     guild profile, resources, feature/channel policy
    setup/      inspection, plans, resource lifecycle, repair
    community/  onboarding, roles, reminders, polls, highlights
    moderation/ rules, cases, evidence, deterministic actions
    games/      games, builds, cohorts, tester enrollment
    playtests/  sessions, capacity, attendance, close-out
    feedback/   Forum records, tags, status, duplicates, export
  adapters/
    discord/    commands, components, modals, events, Discord API
    ai/         provider clients and model response parsing
    github/     optional issue export/sync
    http/       health and future game webhooks
  manifests/    feature profiles and central registry declarations
migrations/
tests/
```

Import direction is `app → adapters/domain/kernel`, `adapters → domain/kernel`,
and `domain → kernel contracts`. Kernel never imports a domain or adapter;
domains never import Discord/provider SDKs or each other’s stores. Cross-domain
work uses application services, typed queries/operations, or post-commit
events. Automated architecture tests enforce this.

There is one composition root. It validates config, migrations, manifests,
routes, tools, task policies, and event handlers before marking the process
ready. A partially registered feature is a startup failure, not a dead button.

## Registries — one declaration, several derived surfaces

| Registry | Owns | Derived evidence |
|---|---|---|
| Feature manifest | feature ID, dependencies, config schema, routes, operations, events, stores | boot profile, config docs, dependency graph |
| Route registry | command/component/modal route, renderer, authority, feature, destination rules, featured rank, component cost | Curated Home/help, Discord command sync, reachability and pagination graph |
| Setup registry | inspect/plan/apply/verify/repair sections and resource ownership | setup diff, rerun/repair tests |
| Operation registry | input/result schema, risk, permission, idempotency, preview/verify/compensation | deterministic UI actions and AI tools |
| Event registry | event schema, producer, consumer, retry/dead-letter policy | outbox dispatch and compatibility tests |
| AI task/tool registry | task profile, provider route, allowed tools/scopes, budgets, output schema | diagnostics, policy tests, operator disclosure |

Registration describes capability; it does not prove behavior. CI additionally
proves every enabled route has a handler, every button target exists, every
operation has tests, and every main journey reaches an observable effect.

## Deterministic request and mutation flow

Every entry point follows one route:

1. The adapter converts the Discord event, scheduled job, integration event,
   or AI proposal into a typed request with actor or service principal, guild,
   channel, correlation ID, and idempotency key. Non-interactive work uses a
   purpose-limited delegation record containing its initiating actor, allowed
   operation/destination, guild/game scope, expiry, and revocation state; it
   never borrows ambient owner or bot authority.
2. Central admission intersects Discord authority, bot role, guild feature
   profile, game assignment, channel policy, rate limit, and operation risk.
3. A read request uses an application query/read model. A write request enters
   the workflow engine with an exact operation version and validated input.
4. The owning domain service changes only its own state through its repository
   and, where needed, its Discord resource adapter.
5. The transaction records before/after evidence, audit, and transactional
   outbox events together. External Discord calls use operation receipts and
   reconciliation because Discord and Postgres cannot share one transaction.
6. The engine verifies the database and/or real Discord effect. Retries reuse
   the same idempotency key and never create a second logical resource.
7. Post-commit consumers update projections/send follow-ups. Failures retry
   with bounded backoff and become visible dead letters.
8. The renderer returns an outcome, partial-failure/recovery path, and audit
   reference appropriate to the caller.

No cog, component callback, AI tool, or event consumer writes a domain table or
calls a mutating Discord method outside this path.

## Typed operation contract

Every side-effecting operation declares:

- stable name and version;
- validated input and typed result;
- owning domain and feature;
- required caller scope and permitted destinations;
- risk class and confirmation rule;
- preview/diff support and irreversible effects;
- resource IDs plus expected database versions/Discord-state fingerprints as
  execution preconditions; drift invalidates the plan and requires re-preview;
- idempotency identity and concurrency key;
- execute and effect-verification behavior;
- compensation or explicit “manual recovery only” instructions;
- audit fields, event outputs, timeout, retry, and rate-limit policy.

This makes one operation usable from a button, slash command, setup plan,
scheduled workflow, integration, or AI tool without creating a second policy
or mutation path.

## AI as an operating layer

### Modes

| Mode | Capability | Default availability |
|---|---|---|
| Observe | Read scoped server/game state, search approved records, explain health/history | Permitted staff and contextual member tasks |
| Assist | Draft, classify, summarize, compare, propose a typed plan | Enabled by task policy; output is advisory |
| Act | Invoke registered typed operations after admission and risk handling | Low-risk auto; medium-risk exact-plan confirmation; high-risk denied by default |

“More freedom” means the model can choose and sequence a useful set of approved
operations instead of only returning prose. It does not mean broader ambient
credentials.

### Effective authority

For each tool call, effective authority is the intersection of:

`registered tool scope × caller/delegation authority × guild feature policy ×
game and channel scope × task profile × risk/confirmation policy × rate/spend
limits`.

Every profile may narrow that result and none may widen it. Authorization and
delegation validity are checked when planning and again immediately before
execution. Confirmation is bound to the canonical plan hash, caller, guild,
expiry, resource IDs, and expected versions/fingerprints; changed arguments or
resource drift invalidates it and produces a fresh preview.

### Risk classes

| Class | Examples | Default AI behavior |
|---|---|---|
| Read | inspect resources/config/builds/feedback/health/audit summaries | Execute if the caller may read the source; redact private fields |
| Low/reversible | create personal reminder, tag/assign permitted feedback, enroll caller, prepare draft, publish owner-approved template/content, or post free-form content only to a private review destination | May execute and explain; rate limited and audited |
| Medium/structural or public | create/adopt channels or roles, change permissions, publish any model-authored free-form public content/build announcement, create scheduled event, change cohort roles/config | Preview exact diff/content and require an authorized confirmation |
| High/destructive | delete resources, mass role changes, bans/kicks, rotate secrets, deploy, migrate/erase data, weaken AI policy | No general AI tool in MVP; use explicit deterministic owner workflow or refuse |

Moderation recommendations may use AI, but consequential enforcement remains a
human-confirmed deterministic operation in the MVP.

### Agent loop

The bounded loop is **observe → plan → authorize → execute → verify → audit →
explain**. The planner emits a schema-constrained plan over registered tools,
with assumptions and expected effects. A deterministic controller enforces
maximum steps, tool/result size, deadlines, budgets, recursion prohibition, and
stop conditions. Tool results are untrusted data and cannot modify system
policy or reveal hidden instructions.

If the model response is invalid, authorization changes, verification fails,
or the budget/provider is unavailable, the controller stops safely and offers
the deterministic workflow. It never guesses success.

### Provider gateway and budgets

Preserve the predecessor’s provider-neutral shape: task ID → policy → model
route → adapter, with OpenAI, Anthropic, and deterministic adapters initially.
Add per-task timeouts, retry classification, circuit breakers, concurrency,
token/cost budgets, daily/monthly guild rails, and an owner kill switch.
Provider/model changes are configuration with audit, not domain code changes.
No Discord-derived content reaches a non-deterministic provider until GCB-3
records the provider data-flow decision: allowed source/data classes,
staff/private exclusions, retention/training terms, guild/user disclosure and
consent, regional/contract constraints where relevant, and deletion/export
propagation tests. A task policy identifies each allowed source class; redaction
cannot silently expand it.

Structured outputs are schema validated. Prompts are versioned. Stored traces
contain provider/model, task/tool versions, usage/cost, latency, result class,
policy decision, and correlation ID; secrets, raw credentials, and unnecessary
private content are redacted.

### Durable, scoped memory

Memory is a Postgres service, not an unbounded transcript. Supported records:

- scoped facts/preferences with subject, provenance, confidence, expiry, and
  visibility;
- task/workflow state with owner, status, next action, and source references;
- bounded conversation summaries linked to the original Discord messages when
  policy permits;
- approved server/game terminology and instruction profiles.

Guild, channel/thread, game, actor, and privacy scopes are explicit. Retrieval
must pass the caller’s current read permission. Users/staff can inspect and
forget eligible memory. Retention jobs expire data; deletion events clear
derived indexes. Raw Discord history is not copied wholesale, and model output
does not become a durable fact without provenance or confirmation.

## Data ownership

The conceptual model begins small:

| Owner | Primary records |
|---|---|
| Guilds/setup | guild profiles, resource bindings, feature/channel policies, setup plans/runs/receipts |
| Community | member onboarding, role selections, reminders, polls |
| Moderation | cases, evidence references, rules, actions, appeals/status |
| Games | games, builds, platforms, cohorts, tester enrollments |
| Playtests | sessions, objectives, enrollment/waitlist, attendance, outcomes |
| Feedback | Forum record bindings, structured fields, tags, assignment, status, duplicate/export links |
| Kernel workflow | operations, confirmations, effects, audit, outbox/dead letters |
| AI | task decisions, tool invocations, usage/budget, memories, prompt/profile versions |

Rows carry guild ownership and timestamps; mutable records use optimistic
versioning. Discord resources are bound by stable guild/resource IDs, never by
name alone. Domain repositories expose intentional methods rather than generic
table access. Guild lifecycle state includes active, removed/tombstoned,
retention-hold, and purged; removal revokes service-principal grants, jobs,
integrations, and AI work before any later retention/purge job can run.

## Configuration hierarchy

Precedence is explicit: code defaults → environment deployment settings →
typed guild profile → scoped game/channel overrides → request-only parameters.
Each setting has one canonical typed representation, owner, visibility,
validation, and restart/dynamic behavior. Secrets remain environment/secret
store references and are never persisted in guild configuration or exposed to
AI.

Feature profiles are allow-lists. MVP production loads only server, community,
moderation, games, playtests, feedback, and AI support modules. Unknown config,
dependency cycles, duplicate registry keys, and enabled features without their
requirements fail startup.

## Security and privacy boundaries

- Least-privilege Discord intents and OAuth scopes; message-content intent is
  off for the MVP. Native Forum events are metadata/resource signals only;
  structured intake and AI content enter through explicit interactions (modal
  or adopt/context action) with re-authorization and disclosure. Any later
  ambient-content feature requires a separate privileged-intent, privacy,
  deployment, degraded-mode, and test-guild decision.
- Owner bootstrap uses Discord ownership and an auditable recovery path; a bad
  guild rule cannot lock the owner out.
- Component/modal IDs are signed or server-resolved, short-lived where needed,
  and re-authorized on interaction.
- Home/help renderers enforce Discord component/select-option limits at boot
  and runtime; featured actions are curated and pagination/filter tests retain
  the promised two-interaction reachability.
- External content, attachments, Forum text, and tool results are untrusted;
  apply size/type limits, escaping, malware/media controls where relevant, and
  prompt-injection isolation.
- Sensitive fields are classified, redacted from logs/model context, encrypted
  in transit and at rest through the platform, and subject to retention/delete
  workflows.
- Outbound HTTP is allow-listed per integration; there is no general URL-fetch
  or SSRF-capable AI tool.
- Staff-private evidence never appears in public summaries or member memory.
- Dependency, secret, static, and migration checks gate release; incident kill
  switches can disable AI Act, all AI, an integration, a feature, or the bot
  process independently.

## Availability and scaling seams

Discord interactions are acknowledged within the platform deadline; longer AI
or workflow work is deferred and correlated. Database connection loss makes
write routes unavailable with a truthful message; read-only cached surfaces
must not present stale state as live. Provider loss disables only AI work.

The scheduler and outbox use database leases so multiple instances can run
without duplicate logical work. Guild/resource concurrency keys serialize
conflicting setup and configuration changes. Stateless adapters plus Postgres
state allow horizontal workers later without redesigning memory or jobs.

## Architecture proof, not architecture theater

The new repo is not allowed to claim this architecture from folders alone.
Each boundary gets an executable check: forbidden-import tests, registry
validation, operation contract tests, permission matrix tests, outbox recovery,
Discord-effect reconciliation, AI tool-policy tests, and main journey drives.
