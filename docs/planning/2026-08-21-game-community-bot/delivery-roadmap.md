# Delivery roadmap

> **Status:** `plan` · dependency ordered. Finish, verify, document, and merge
> one issue-sized slice before starting the next. Phase numbers describe
> dependencies, not dates or simultaneous workstreams.

## Delivery rules

- The new repository becomes the canonical product home in Phase 0. This
  fleet-manager section then becomes a dated pointer.
- Every slice starts with acceptance evidence and ends with one reviewable pull
  request. Avoid horizontal “build all repositories, then all services” work.
- A feature is complete only with navigation, authority, operation/read model,
  visible effect, failure/recovery behavior, automated journey evidence, and
  updated current-state/plan records.
- The live `superbot` service and both existing repositories remain untouched.
- AI scaffolding lands early, but no AI-only feature satisfies a deterministic
  product requirement.
- Phase exit means all named gates are green. It does not mean every imaginable
  capability in that area is complete.

## Phase 0 — canonical home and executable contract

**Outcome:** a new repository that can tell the truth before it has features.

Slices:

1. Confirm GCB-1; create the repository from the estate’s minimal Python bot
   substrate, protections, ownership, and one required `quality` check.
2. Transplant this planning section, add an ADR for clean-repo/server-first/
   single-mutation-path decisions, and create intent/current-state/MAP/README.
3. Add locked dependencies, package/import skeleton, config schema, migration
   runner, test harness, Docker image, and local development command.
4. Start a Discord process with no privileged intent, structured startup log,
   correlation ID, health/readiness, signal-safe shutdown, and a deterministic
   `/home` “not configured” response.
5. Provision a separate test Discord app, Railway test service, test database,
   secret references, and deployment/runbook records after GCB-2.

Exit gates:

- fresh checkout has one documented verify command and one meaningful required
  check;
- process boots without Discord/network for tests and fails closed on invalid
  config/migrations;
- test deployment is isolated from production `superbot` identity/service/DB;
- health proves process, Discord connection state, database, migrations, and
  registry status separately;
- canonical records name the next single phase.

## Phase 1 — kernel, policy, and AI spine

**Outcome:** the complete control path exists before product breadth.

Slices:

1. Implement typed config, Postgres repositories, migration checksums, guild
   scoping, transaction helper, and test database fixtures.
2. Implement actor/context, central admission, feature/channel policy, owner
   bootstrap/recovery, and a table-driven permission matrix.
3. Implement operation/workflow contracts, idempotency, confirmation binding,
   audit, transactional outbox, retries/dead letters, and effect receipts.
4. Add feature/route/setup/operation/event registries plus boot validation and
   import-direction tests.
5. Add provider-neutral AI gateway, deterministic adapter, task/tool registries,
   Observe/Assist/Act policy, budget/kill-switch state, structured trace, and
   invalid/provider-down fallback. Paid adapters remain disabled until GCB-3.
6. Add durable scoped memory records, retrieval permission checks, retention,
   inspect/forget controls, and no raw-transcript default.

Exit gates:

- one test operation is invoked through deterministic UI and AI and produces
  identical authorization/workflow/audit/effect behavior;
- policy profiles can narrow but never widen authority;
- retries and duplicate interactions produce one logical effect;
- provider failure and global AI disable leave Home and deterministic writes
  operational;
- audit links caller, plan, operation, effect verification, and response.

## Phase 2 — Home, discovery, and access

**Outcome:** a truthful, usable front door with no dead or hidden feature.

Slices:

1. Build the route registry and personalized Home renderer for unconfigured,
   member, tester, staff, and owner states.
2. Generate Discord command sync/help metadata from routes; add persistent
   components and signed/re-authorized modal/component state.
3. Implement per-guild feature profiles and central live admission for slash,
   component, modal, scheduled, integration, and AI origins.
4. Add reachability graph, permission/destination explanation, disabled-state
   copy, stale-component recovery, and owner support report.

Exit gates:

- every enabled feature route is reachable from Home within two interactions;
- every rendered target has a registered handler and permitted actor/destination
  test; disabled modules have no orphan command/button;
- owner recovery works under the most restrictive valid guild policy;
- panels render current read-model state, never captured constants.

## Phase 3 — setup and the first AI action slice

**Outcome:** a fresh guild can be safely provisioned and repaired, with AI
freedom demonstrated through the real control path.

Slices:

1. Add read-only guild inspection for roles, channels/categories, permissions,
   AutoMod, events, bot hierarchy, resource bindings, and adoption candidates.
2. Define the Game Testing server profile and deterministic desired-state
   planner for categories/channels/Forums/roles/permissions/log destinations.
3. Implement typed adopt/create/update operations, exact preview, concurrency,
   partial-run receipts, verification, rerun, repair, and manual recovery.
4. Build the guided `/setup` journey, essential/advanced separation, plan hash
   confirmation, progress/result UI, and support export.
5. Register AI setup read tools and the bounded “design/improve this setup”
   task. AI may propose copy/order/approved operations; medium-risk application
   requires owner confirmation.
6. Drive fresh, partially configured, conflicting-name, insufficient-hierarchy,
   interrupted, and rerun cases in the real test guild.

Exit gates:

- setup dry-run makes no mutation; apply creates only the approved diff;
- rerun is a no-op and interrupted work resumes without duplication;
- adopted resources are tracked by ID and ownership/rollback limits are clear;
- AI cannot smuggle a tool or changed argument outside the confirmed plan;
- a test-guild evidence bundle proves setup, verify, repair, and owner recovery.

## Phase 4 — community and safety core

**Outcome:** the server is safe and useful for ordinary members before playtest
automation grows.

Slices:

1. Implement server guide, rules acknowledgement, entry/member/tester roles,
   game-role selection, join/leave behavior, and onboarding completion.
2. Implement logging destinations, structured member/config/resource events,
   privacy/redaction, retention, and staff-visible audit lookup.
3. Implement moderation cases/evidence, warnings/timeouts, member notices,
   appeal/status fields, and deterministic permission/hierarchy validation.
4. Configure native AutoMod where possible; add narrowly justified bot rules,
   rate limits, media/link controls, escalation, and kill switches.
5. Add polls, personal/staff reminders, scheduling leases, delivery retries, and
   user cancellation.
6. Add AI moderation/context summaries and welcome/announcement drafting as
   advisory tasks; keep consequential moderation human-confirmed.

Exit gates:

- join → rules → game/tester role → Home works without staff or AI;
- moderator actions produce one Discord effect, case, notice, and audit link;
- bot hierarchy/permission failures are explained before action where possible;
- native/bot moderation ownership is documented with no duplicate enforcement;
- privacy and retention tests cover public, staff, and AI surfaces.

## Phase 5 — game testing loop

**Outcome:** the first real community can publish builds, run sessions, and
turn Forum discussion into usable feedback.

Slices:

1. Add multi-game records, game roles/destinations, platforms, developer
   assignments, and the first `spider-swing` profile.
2. Add build lifecycle: validate, draft, publish/current, replace/retire,
   announcement preview, cohort routing, and Home projection.
3. Add playtest sessions, Discord Scheduled Event binding, enrollment/capacity/
   waitlist, cohort eligibility, reminders, attendance, and close-out.
4. Add Bug Reports and Feedback Forum bindings, structured intake/tags/status,
   assignment, missing-information prompts, duplicate links, and privacy split.
5. Add run/clip/replay sharing metadata and session/result linkage without
   copying large media into the database.
6. Add AI read/draft/triage/summary tools for builds, sessions, and feedback;
   enable only low-risk tags/assignments/reminders under policy.
7. Drive the full tester and staff journeys for `spider-swing` with real
   participants or designated test actors.

Exit gates:

- a tester can self-serve current build, session, and feedback flows from Home;
- staff can publish and replace a build without stale Home/reminder content;
- Forum remains the human conversation source; structured state survives edits
  and duplicate/status changes;
- AI summaries cite the records/messages used and separate unknowns;
- a second synthetic game profile passes the same tests without code copy.

## Phase 6 — AI community operator

**Outcome:** AI performs meaningful cross-feature work safely and is operable
under failure, spend, and privacy pressure.

Slices:

1. Add grounded server/game search and evidence citations over authorized read
   models, audit, Forum records, and bounded memory.
2. Add multi-step plans for playtest preparation, feedback triage, follow-up
   reminders, build communication, and server-health remediation.
3. Add approval inbox, plan diff/expiry/cancellation, partial-plan handling, and
   explain/replay view for staff.
4. Add per-task provider routing, fallbacks, budgets, circuit breakers, usage
   reports, prompt/profile release records, and evaluation fixtures.
5. Add prompt-injection/tool-result isolation, exfiltration tests, content
   boundary checks, memory poisoning/correction paths, and incident controls.
6. Run a limited Act-mode pilot: low-risk allow-list only, named guild/channel,
   daily budget, enhanced review, and automatic stop conditions.

Exit gates:

- task evaluations measure outcome, grounding, tool choice, policy, cost, and
  safe refusal—not wording parity;
- every side effect maps to a registered operation and verified audit chain;
- kill switches disable Act or all AI immediately without bot restart;
- a provider outage, bad structured response, injected Forum post, stale
  confirmation, and tool failure all stop safely;
- pilot evidence supports any expansion of the low-risk allow-list.

## Phase 7 — optional integrations, one proven need at a time

Candidate slices are GitHub issue export/sync, game-client build webhook,
invite attribution, highlights/participation, LFG, richer analytics, or a web
operator view. Each requires a named user problem, owner confirmation, scoped
credentials, independent kill switch, retry/idempotency contract, and a
deterministic degraded mode. None blocks MVP or production readiness.

## Phase 8 — production pilot and ownership decision

**Outcome:** evidence determines whether the new bot remains an additional
community bot or replaces any live `superbot` responsibility.

Slices:

1. Complete security/privacy/operations review, restore rehearsal, Discord
   intent/permission review, budget rail, capacity drive, and release candidate.
2. Run an isolated pilot guild, then a named canary guild/profile with enhanced
   monitoring and no legacy data import.
3. Compare user journeys, failures, staff workload, AI value/cost, moderation
   outcomes, and rollback evidence against explicit promotion criteria.
4. If replacement is desired, inventory exact live responsibilities/data,
   design and dry-run a separate migration/cutover plan, and get owner approval.
5. Update fleet Layer-2 records. Archive/decommission anything only in a later
   explicit, reversible-where-possible change.

Exit gates:

- release and rollback are rehearsed from immutable artifacts;
- no unresolved severity-1/2 security, data, permission, or journey defect;
- operational owner, alerts, runbooks, backups/restore, and spend response are
  named and tested;
- any production replacement claim is based on real guild effects, not command
  counts or a period with no reported complaints.

## MVP boundary and recommended first implementation slice

The MVP ends after Phase 6 is evidenced in a real test guild. Phases 0–3 create
the truthful control path; Phases 4–5 make the server useful; Phase 6 fulfills
the owner’s AI-freedom goal.

After repository creation, the first implementation PR should be Phase 0 slice
2/3: canonical records plus the smallest bootable package and required check.
Do not begin by copying a cog, subsystem, or generated manifest.
