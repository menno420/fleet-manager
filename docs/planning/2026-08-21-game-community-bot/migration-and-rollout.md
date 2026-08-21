# Migration and rollout plan

> **Status:** `plan` · protects the live bot while the new product proves
> itself. “Migration” initially means controlled knowledge/code harvesting, not
> production traffic or data movement.

## Non-negotiable safety boundary

- Do not commit to, merge into, or deploy from `superbot` or `superbot-next` as
  part of the new build.
- Do not reuse the production Discord application/token, Railway service,
  database, queues, volumes, domains, or alert destinations for development.
- Do not place new-bot code in `fleet-manager`; this repository holds the plan
  only until the product repository exists.
- Do not add the new bot to a production guild until the test-guild gates for
  the relevant phase are complete.
- Do not call the new bot a replacement until each exact live responsibility
  and any data continuity requirement has a verified cutover/rollback path.

The current `superbot` remains the safe rollback because this plan never edits
it. `superbot-next` remains a reference repository, not a staging branch.

## How source material is harvested

Every reuse candidate gets a short extraction ledger in the new repository:

| Field | Required evidence |
|---|---|
| Source | repository, exact commit, file/symbol, applicable license/ownership |
| User behavior | journey/effect being preserved and how it was observed |
| Decision | copy, adapt, rewrite from contract, or reject |
| Coupling | imports, configuration, tables, Discord assumptions, side effects |
| New owner | target package/domain and operation/route registry entry |
| Proof | focused tests, journey test, and test-guild observation |
| Differences | deliberate behavior/security/config changes |

Default choices:

- **From `superbot`:** rewrite from observed behavior and focused service
  contracts. Copy only small, independently tested helpers with no live/runtime
  coupling.
- **From `superbot-next`:** adapt typed kernel contracts and tests where they
  match the new ownership model. Do not import the 49-subsystem manifest,
  generated capture corpus, BTD6 tools, or entire domain tree.
- **From both:** use names as search clues, then re-verify the live code path.
  A document or golden output alone is not behavior evidence.

A copied module is not “faster” if it brings a legacy config projection,
database schema, direct Discord mutation, unused feature dependency, or parity
fixture. Those are rewrite signals.

## Environment ladder

| Environment | Identity and data | Purpose | Promotion evidence |
|---|---|---|---|
| Local/CI | mock Discord, ephemeral Postgres, deterministic AI | fast contract and journey tests | required `quality` check |
| Test | separate Discord app, dedicated test guild, test Railway service/DB, tiny AI budget | real Discord permissions/UI/effects and failure drives | signed evidence bundle per phase |
| Canary | same new app, named non-critical guild/profile, isolated config and budget | realistic use with narrow feature/AI allow-list | release scorecard and rollback rehearsal |
| Production | owner-approved guilds and explicit feature profiles | supported service | operations review and promotion decision |

Configuration identifies environment explicitly. An environment name never
selects a token by convention; deployment wiring binds exact secret/resource
references. Startup logs safe identity evidence: application ID, guild allow-
list mode, database identity fingerprint, build SHA, migration set, feature
profile, and AI mode—never secret values.

## Test-guild drive protocol

Each main journey is driven from a known starting snapshot with designated
owner/admin/mod/developer/tester/member accounts or test identities. The evidence
bundle records:

- release/build SHA and migration set;
- Discord application/guild ID and feature profile;
- actor and starting permissions/resource snapshot;
- operations requested, confirmations, receipts, audit/correlation IDs;
- resulting Discord IDs/state and database read-model state;
- screenshots only as supporting UI evidence, never the sole proof;
- cleanup/rollback result and unresolved defects.

Drive denied and failure paths as deliberately as happy paths: insufficient bot
hierarchy, removed caller role, deleted/adopted resource, duplicate interaction,
provider timeout, database interruption, stale component, partial setup, budget
exhaustion, missing Community or privileged-intent prerequisite, guild removal,
reinstall, and kill switch.

## Data migration posture

MVP creates no broad legacy migrator and imports no production data. New game,
build, server-profile, and policy records are seeded intentionally in the test
guild. Discord resources can be **adopted** by ID after inspection without
claiming ownership or deleting them on rollback.

If a production guild later needs continuity, create a separate, reviewed
migration plan with:

1. exact source/target tables and field semantics at pinned commits;
2. privacy/retention decision and data minimization;
3. read-only extractor and deterministic transform;
4. dry-run report with counts, invalid rows, conflicts, checksums, and examples;
5. repeatable import with idempotency and source-to-target mapping;
6. dual-read/shadow comparison only where it materially reduces risk;
7. backup/restore rehearsal and a point after which rollback needs a forward
   reconciliation;
8. owner approval for the exact dataset and cutover window.

Discord messages, tickets, economy/game content, process-local AI memory, and
uncertain legacy config are excluded by default. “Import everything” is not an
acceptable requirement.

Guild removal is not a data-migration event. It immediately tombstones the
guild and revokes scheduled/integration/AI authority; configured retention and
legal/audit holds then decide an idempotent purge. Reinstall never silently
reactivates old jobs, delegations, credentials, or member memory.

## Release and promotion ladder

1. **Pull request:** immutable candidate passes `quality`, review, migration
   checks, package/image build, and plan/current-state update.
2. **Test deploy:** deploy exact artifact; run smoke, readiness, command sync,
   support report, main affected journey, and rollback.
3. **Phase evidence:** complete the test-guild protocol and close defects.
4. **Canary enablement:** allow-list exact guild/features/AI tools/budget;
   monitor operator-visible metrics and audit, with automatic stop conditions.
5. **Promotion decision:** compare the release scorecard to documented gates;
   promote the same artifact/config revision or reject it. Never rebuild from a
   moving branch for production.
6. **Broader enablement:** add guilds/features independently. A game profile or
   AI Act expansion is a policy rollout, not an implicit deploy side effect.

There is no time-served gate such as “seven quiet days” by itself. Promotion
requires completed journeys and sufficient real traffic/operations to exercise
the changed surface.

## Rollback design

Rollback is defined at four levels:

| Level | Mechanism |
|---|---|
| AI | disable Act, a task/tool, a provider, or all AI; deterministic UX remains |
| Feature/guild | disable the manifest profile or integration for exact guilds without deleting state |
| Application | redeploy the previous immutable image/config and run compatible schema checks |
| Discord/data change | execute the operation’s compensation when safe, otherwise use the recorded manual recovery plan |

Database migrations follow expand/contract discipline. A release cannot depend
on a destructive contract migration until the prior application is no longer a
rollback candidate and backup/restore has been proven. Discord setup distinguishes
bot-created resources from adopted resources; rollback never deletes adopted
resources and never promises recreation of deleted message history.

If a future cutover replaces `superbot` in a guild, the rollback plan must name
the old app’s permissions/config/data compatibility and the exact re-enable
steps. The old bot is not decommissioned in the same change that first promotes
the new one.

## Cutover decision record

Before any responsibility transfers, record a table with one row per live
behavior: owner, current bot/path, new journey/effect evidence, data dependency,
Discord permissions/intents, downtime/dual-running behavior, rollback, and
final decision. “Command exists in both” is not sufficient.

Dual running is allowed only with partitioned ownership. Event listeners,
welcome/role assignment, AutoMod, logging, reminders, and moderation actions
must never both act on the same event accidentally. The guild profile names one
owner for each responsibility.

## Completion and archival

After the new repository exists, replace this section’s authority banner with a
pointer to its copied/reconciled plan and update both Layer-2 entries. Archive
or rename either existing bot only after a separate owner decision verifies:

- no live deployment or scheduled workflow depends on it;
- repository/default-branch protections and historical evidence are retained;
- secrets/services/data have explicit keep/delete ownership;
- the fleet registry and external links are updated;
- recovery no longer requires its code or artifact.
