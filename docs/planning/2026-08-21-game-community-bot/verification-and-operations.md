# Verification and operations plan

> **Status:** `plan` · defines the evidence needed to call a capability real
> and the minimum operating surface before production use.

## One required check with meaningful internals

Use one branch-protection check named `quality`. Its jobs may run in parallel,
but the required surface stays stable and tells one story:

| Job | Proves |
|---|---|
| format/lint/type | source is formatted, statically coherent, and free of banned imports/patterns |
| unit/contracts | domain, registry, operation, policy, rendering, and failure contracts |
| integration | real Postgres migrations/repositories/outbox and adapter boundaries |
| journeys | Home reachability and main user/effect flows through Discord test adapters |
| security/supply chain | dependency/secret/static checks, permission/tool-policy tests, locked artifacts |
| package | wheel/container build, boot smoke, migration/registry validation, artifact identity |

Deployment and real-guild drives are promotion evidence, not a way to make an
unrelated source check permanently red. The repository documents one local
command that reproduces the required source gate as closely as practical.

## Test portfolio

### Fast deterministic tests

- domain rules for games, builds, cohorts, playtests, feedback, moderation;
- typed config parsing, precedence, secret redaction, invalid/unknown settings;
- registries: duplicate IDs, missing targets, dependency cycles, incomplete
  features, event/tool/schema compatibility, featured-action/component budgets;
- route reachability, pagination/selection limits, and rendered target graph
  for each actor/profile/state;
- table-driven Discord × bot-role × guild-feature × channel/game access;
- operation preview, confirmation hashing, re-authorization, idempotency,
  expected-state fingerprint drift, optimistic concurrency, compensation
  metadata;
- AI structured plan parsing, scope intersection, risk handling, maximum steps,
  budgets, redaction, memory visibility/expiry/forget, deterministic fallback;
- no live-state/capture literals in stateful panels.

### Integration and failure tests

- Postgres migrations from empty and each supported prior schema; checksums,
  rollback-compatible expand/contract, repository guild isolation;
- transaction + outbox atomicity, lease contention, duplicate delivery,
  retry/dead-letter/replay, scheduler restart;
- Discord adapter commands/components/modals/events, stale interaction,
  rate-limit/retry classification, partial external effect and reconciliation;
- native Forum events with Message Content off: no ambient body/attachment
  claim, explicit modal/adopt intake, disclosure, authorization, edits, and
  deterministic metadata-only degraded behavior;
- setup inspect/plan/apply/verify/rerun/repair with adoption, conflicts,
  hierarchy failure, permission loss, and interruption;
- provider adapters with recorded contract fixtures, timeouts, invalid schemas,
  refusals, circuit breaker, failover, budget exhaustion, and kill switch;
- prompt injection in messages/Forum/tool results, oversized/malicious content,
  cross-guild/private-source exfiltration attempts, memory poisoning/correction;
- provider data-class allow/deny, disclosure/consent, retention, and deletion/
  export propagation under the approved GCB-3 policy;
- member-intent absent/present readiness, guild removal authority revocation,
  retention/purge, and safe reinstall;
- backup and restore of a representative database into an isolated target.

Network/provider tests use controlled fakes in the required gate. A small
scheduled/non-blocking contract suite may detect provider API drift without
making ordinary merges depend on paid or unstable external traffic.

### Main journey/effect tests

Automated adapters cover at least:

1. owner bootstraps and reruns/repairs a fresh server;
2. member accepts rules, completes external test opt-in/access, obtains and
   installs the build, and confirms launch—or reaches a tested blocked/support
   state;
3. developer publishes/replaces a build and all projections/reminders update;
4. staff schedules/runs/closes a playtest and a tester joins/leaves/waitlists;
5. tester reports feedback; staff/developer triage, link the corrective build,
   notify, retest/reopen, and close it; export is asserted only when the
   optional external integration is enabled;
6. moderator handles a case with evidence, notice, Discord effect, and audit,
   then both an in-guild and guild-removed appellant complete private review;
7. AI reads, proposes, obtains exact state-bound confirmation, acts, verifies,
   and explains; free-form public model content always requires confirmation;
8. provider/AI disabled follows the equivalent deterministic route;
9. unauthorized/stale/cross-guild actions fail without side effects;
10. guild removal revokes jobs/integrations/AI, retention/purge is idempotent,
    and reinstall starts without stale authority;
11. a second synthetic game profile completes the generic flow.

Each test asserts the visible response, stored read model, external effect or
adapter receipt, audit, post-commit event, and retry behavior—not only a string.

### Real test-guild evidence

Automation cannot fully prove Discord permission hierarchy, native Forum/Event
behavior, mobile component usability, command propagation, role/channel UX, or
provider latency. Each phase’s affected journeys therefore get a test-guild
drive using the protocol in [`migration-and-rollout.md`](migration-and-rollout.md).

No screenshot, panel count, command count, manifest row, golden byte file, or
absence of complaints substitutes for this evidence.

## AI evaluation and release gate

Maintain versioned task cases for setup design, server health, playtest prep,
build announcement, feedback triage/summary, moderation assist, and recovery.
Cases contain authorized source records, adversarial/untrusted content,
available tools, expected constraints/outcomes, and cost/latency ceilings.

Score separately:

- intent/assumption handling and appropriate clarification;
- grounding/citations and unsupported-claim rate;
- tool selection/arguments/ordering and minimality;
- authorization, risk classification, confirmation, refusal, and privacy;
- operation/result verification and partial-failure explanation;
- usefulness of the resulting server/user effect;
- token/cost/latency and deterministic/provider-down behavior.

A wording change is not a regression if these outcomes remain correct. A
well-written answer is a failure if it chose an unauthorized tool, claimed an
unverified effect, leaked data, or left the user without a usable next action.
Any expansion of Act-mode tools needs task-specific evaluation, test-guild
evidence, a kill switch, and an explicit policy change.

## Operational signals

### Structured logs and trace

Every request carries correlation, interaction/event, guild, actor (privacy-
appropriate), route/task, build SHA, operation/workflow, and outcome fields.
AI spans add task/profile/prompt/provider/model/tool/usage/cost/policy fields;
secrets, raw tokens, unnecessary message content, and private evidence are
redacted.

### Metrics

At minimum measure:

- process/Discord/database readiness, reconnects, event-loop lag;
- interactions by route/outcome, acknowledgement and completion latency;
- workflow success/partial/failure, retries, idempotency hits, reconciliation,
  outbox age/dead letters;
- scheduler due/delivered/failed and reminder lateness;
- setup operation/result/repair counts and orphan/drift findings;
- onboarding completion, build/playtest/feedback funnel outcomes;
- moderation actions/errors/appeals without exposing member content;
- AI requests by task/outcome/provider/model, latency, tokens/cost, fallback,
  invalid output, denial/confirmation/tool verification, budget/circuit state;
- rate-limit pressure and external integration health.

Metrics are tagged with bounded identifiers/profile names, not unbounded user,
channel, prompt, or error text.

### Health and owner support report

Liveness proves the process can make progress. Readiness separately reports
config, migrations, database, Discord gateway/application identity, registry,
outbox/scheduler, and required feature dependencies. AI/provider health is a
degraded component unless the queried route specifically needs AI.

An owner-visible support report exposes safe application/build identity,
guild/profile, enabled features, bot role/permission/hierarchy gaps, resource
bindings/drift, recent failed workflows/dead letters, scheduler, AI mode/budget/
provider circuit, and correlation/audit references. It never exposes secrets or
staff-private content.

## Initial service objectives and release thresholds

These are engineering gates to validate in the test/canary environments, not a
business SLA promise:

- acknowledge ordinary Discord interactions inside 2.5 seconds at p95; defer
  before doing AI or long external work;
- 100% of successful state-changing operations have caller, authorization,
  operation version, input digest, outcome, and effect-verification audit;
- zero duplicate logical effects in idempotency/retry test suites;
- 100% of enabled routes are handler-complete and Home-reachable for at least
  one permitted actor; no rendered target is missing;
- no cross-guild or unauthorized read/write in the permission and adversarial
  suites;
- provider-down/all-AI-off passes every deterministic core journey;
- setup rerun produces no unapproved change, and interrupted setup has a proven
  resume/repair route;
- restore rehearsal meets a recovery target chosen from measured database size
  before production promotion; do not publish an invented RPO/RTO now.

Canary promotion additionally requires all critical journeys to pass with real
Discord effects, no unresolved severity-1/2 security/data/permission/journey
defect, and sufficient completed operations to exercise the changed surface.

## Alerts and automatic stop conditions

Page/notify the named operator for process/readiness loss, sustained interaction
failure, migration mismatch, outbox/dead-letter growth, scheduler backlog,
Discord auth/permission break, backup failure, security signal, unexpected AI
spend, provider circuit storm, repeated tool verification failure, or cross-
guild/policy invariant failure.

Automatic controls should:

- open the provider circuit on classified provider failures;
- stop AI Act on budget breach, policy/audit unavailability, repeated invalid
  plans, or operation verification anomalies;
- disable an integration on credential/auth or poison-message loops;
- stop promotion on migration/restore/security/journey failure;
- preserve deterministic Home/support/recovery whenever safe.

## Required runbooks

Before canary, the repository owns concise, rehearsed runbooks for:

1. deploy/promote/rollback an immutable artifact;
2. migration failure and rollback-compatible recovery;
3. Discord token compromise/rotation and app/permission/hierarchy failure;
4. database outage, backup verification, restore, and reconciliation;
5. outbox/scheduler dead letter inspection and safe replay;
6. provider outage, cost spike, AI Act/all-AI kill switch, and bad prompt/model
   release rollback;
7. incorrect Discord resource/setup operation and adopted-resource recovery;
8. moderation/privacy incident, evidence access, retention/delete request;
9. external integration credential/failure and webhook replay;
10. support report collection without exposing secrets.

Each runbook names trigger, authority, commands/UI route, evidence to capture,
stop conditions, recovery verification, communication owner, and follow-up.

## Definition of done for a release

A release is promotable only when:

- scope and changed journeys are named;
- code, config schema, migrations, registries, docs/current state, and runbooks
  agree;
- `quality` is green on the exact SHA and review findings are resolved;
- package/image identity and provenance are recorded;
- applicable test-guild journey/failure evidence is attached;
- permissions/intents, data/privacy, AI tools/budget, and rollback impact are
  reviewed;
- deploy smoke, health/support report, and rollback rehearsal pass;
- the operator can see success/failure and knows the next safe action;
- Layer-2 fleet records are updated after the canonical product record.
