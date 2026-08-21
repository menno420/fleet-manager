# Product and UX plan

> **Status:** `plan` · product contract for the first build. Exact Discord IDs,
> names, and copy remain configuration; the journeys and safety behavior are
> acceptance requirements.

## Product promise

The bot should make a game-testing community feel organized without making it
feel automated. A new member can understand where to go, a tester can move from
invite to useful feedback quickly, and staff can run the server from one Home
surface. AI reduces operational work; it does not become another system staff
must babysit.

The MVP serves one real `spider-swing` test community while remaining a
multi-game product. “Multi-game” means a guild can register games, builds,
cohorts, and per-game destinations in data. It does not mean shipping dozens of
game-specific commands.

## Actors and authority

| Actor | Main jobs | Default bot authority |
|---|---|---|
| Server owner | Bootstrap, approve structural changes, set AI policy, recover access | All guild operations, including approval of medium-risk plans |
| Administrator | Configure the server, publish builds, run playtests, inspect health | All non-destructive operations permitted by guild policy |
| Moderator/community manager | Welcome members, moderate, schedule sessions, triage feedback | Moderation and community operations; no infrastructure or AI-policy expansion |
| Game developer | Publish assigned game builds, answer feedback, update status | Assigned game/build/feedback operations only |
| Tester | Enroll, choose game/build roles, join sessions, report and follow feedback | Own submissions and public tester workflows |
| Member | Participate in the general community | Public community workflows only |
| AI operator | Read, suggest, and perform approved typed operations for the calling actor | Never more authority than the caller and active guild/channel policy |

Discord permissions remain the hard platform boundary. Bot roles add a narrower
product boundary; they never override Discord.

## Recommended server profile

The setup wizard proposes this profile and shows a diff before creating or
changing anything. Every name can be changed. Existing compatible resources are
adopted by stable Discord ID rather than duplicated.

| Area | Suggested resources | Purpose |
|---|---|---|
| Start | `start-here`, `rules`, `announcements`, `patch-notes` | Orientation and durable official information |
| Testing | `how-to-test`, `builds`, Bug Reports forum, Feedback forum, `playtest-chat`, `share-runs`, playtest voice | The complete tester loop |
| Community | `general`, `media-and-showcase`, `off-topic` | A useful server between test sessions |
| Staff | `staff`, `mod-log`, `bot-ops`, `ai-review` | Private coordination, evidence, and recovery |

Recommended roles are Owner/Admin/Moderator, Developer, Tester, Member,
per-game interest roles, and optional build/cohort roles. A game/build role is
data, not a new code path.

Native Discord features are the default where they are already the better
product:

- Forum channels hold public bug reports and feedback.
- Scheduled Events advertise playtests.
- Discord roles and permissions remain the access-control source.
- AutoMod is used where a native rule is sufficient.
- Threads hold issue discussion; the bot adds structured intake, labels,
  assignment, status, duplicate links, summaries, reminders, and export.

The bot owns cross-feature workflow, validation, discoverability, audit,
automation, and AI assistance. It does not recreate native Discord screens.

## One front door

`/home` opens a persistent, permission-aware Home panel. It is also linked from
the configured start channel and offered after setup. Buttons/selects cover:

- **Start testing** — enroll, choose game/build, find the current build and
  checklist;
- **Playtests** — upcoming sessions, join/leave, reminders, poll, results;
- **Feedback** — report, find, triage, summarize, export;
- **Community** — roles, events, highlights, server guide;
- **Staff tools** — setup, moderation, publishing, AI operator, health;
- **Help** — contextual explanation and safe recovery.

The route registry filters unavailable actions and explains disabled ones.
Every enabled feature must be reachable from Home in at most two interactions.
The same registry generates slash-command discovery, permission metadata, help,
and reachability tests so those surfaces cannot drift. Routes declare explicit
featured-action rank; Home/help curate from that rank instead of dumping the
complete inventory. Boot validation enforces Discord component/select-option
budgets, and paginated/filtered layouts must still meet the two-interaction
contract.

Slash commands are shortcuts, not the only usable interface. The initial
top-level vocabulary is intentionally small:

| Command | Responsibility |
|---|---|
| `/home` | Personalized navigation and current priorities |
| `/setup` | Inspect, plan, preview, apply, verify, repair |
| `/server` | Guide, roles, destinations, feature policy, health |
| `/build` | Register, publish, retire, and find game builds |
| `/playtest` | Schedule, enroll, remind, run, and close sessions |
| `/feedback` | Create/find/triage/summarize/export Forum records |
| `/poll` | Quick community decisions and session availability |
| `/remind` | Personal and staff reminders |
| `/moderation` | Cases, actions, rules, and evidence |
| `/ai` | Ask, plan, act, approve, inspect memory/tools/budget |
| `/config` | Advanced typed configuration and recovery |

Subcommands and components carry detail. An optional prefix alias is a later
compatibility decision, not an MVP dependency.

## Critical journeys

### 1. Bootstrap a fresh server

1. The owner invites the test bot and runs `/setup`.
2. The bot inspects channels, roles, permissions, native AutoMod, and its own
   highest role; it makes no change.
3. The owner chooses the Game Testing profile and registers the first game.
4. The deterministic planner produces typed operations. AI may improve names,
   descriptions, and ordering but cannot add an unauthorized operation.
5. The owner sees resources to adopt/create/change, permission impact, risk,
   and rollback limits.
6. After confirmation, the workflow applies idempotent operations, verifies
   real Discord state, and reports completed/skipped/failed steps.
7. A rerun proposes no duplicate resources. Repair can resume a partial run.
8. Home is pinned or linked; an owner recovery route always remains available.

### 2. Become an active tester and launch the game

1. A member sees rules and the server guide.
2. They accept required rules, select game interests, opt into the external
   test program where one exists, and opt into the Discord Tester role.
3. The bot shows the current build, platform-specific access/redeem/download
   instructions, minimum version/device requirements, test focus, known
   issues, next session, and feedback destinations.
4. The tester records a privacy-minimal access state: requested, granted,
   downloaded, installed, launched, or blocked. The bot never claims success
   from role assignment alone and gives a private support route for a blocked
   access step.
5. Launch confirmation unlocks the active-testing checklist and may enroll the
   tester in a build cohort. Staff can see aggregate funnel drop-off and the
   tester can remove their role/state. No AI call is required.

### 3. Publish a build

1. A permitted developer registers version, platform, access link/reference,
   change summary, test focus, known issues, and expiry/replacement.
2. Validation checks the game, required fields, destinations, and caller.
3. Staff previews an announcement and affected cohorts.
4. Publish creates a pending publication, marks the build current only under
   an expected-version precondition, and attempts the approved Discord post.
   Home/reminders expose pending or partial state until the post receipt is
   verified; retry/reconciliation completes it, while cancellation or a
   compensating operation restores the prior current build when safe.
5. AI can draft and tailor the summary, but the stored build record and final
   approved message are the source of truth.

### 4. Run a playtest

1. Staff chooses game/build, time, capacity, cohort, voice/text destinations,
   objectives, and reminder policy.
2. The bot creates/links a Discord Scheduled Event and enrollment surface.
3. Testers join or leave; capacity/waitlist and role eligibility are enforced.
4. Reminders carry the current build and checklist.
5. Closing the session asks for feedback, records participation, and offers an
   AI summary grounded in linked reports and staff notes.

### 5. Report and triage feedback

1. A tester uses the short feedback modal, which creates/binds a Forum post. An
   already-native Forum post remains valid human conversation and can be
   adopted through an explicit `/feedback adopt`/context action that collects
   the structured fields and exact content the user or staff chooses to submit;
   the bot does not ambiently read guild message bodies.
2. The bot validates game/build, type, reproduction fields, privacy, and
   attachments; it adds structured tags without replacing the human post.
3. AI may suggest a title, missing questions, duplicate candidates, severity,
   and a summary. Suggestions remain attributable.
4. Staff assigns, changes status, links duplicates, requests information, or
   exports to an external tracker.
5. A developer responds and, when fixed, links the corrective build and a
   plain-language resolution. The reporter is notified and can confirm the fix
   on that build or reopen with new evidence.
6. Retest success closes the report; status/build/retest changes update the
   Forum record and audit trail. The reporter can follow progress without
   seeing staff-only notes. External export appears only when that optional
   integration is enabled.

### 6. Ask the AI operator to act

1. An authorized user asks in Home or `/ai`, such as “prepare a playtest for
   Saturday” or “clean up the testing channels.”
2. AI reads only the scoped server/game state and returns its interpretation,
   assumptions, proposed typed operations, risk, and expected result.
3. Low-risk operations allowed by policy may execute automatically. Medium
   risk waits for an explicit confirmation bound to that exact plan. High risk
   is refused or routed to deterministic owner controls.
4. The engine re-authorizes at execution time, applies idempotently, verifies
   effects, records tool/model/prompt-version/caller evidence, and explains the
   result in plain language.

### 7. Moderate safely

1. Deterministic rules detect or receive a report and create a case with
   evidence references.
2. AI may summarize context, translate, classify, or recommend a response. It
   cannot invent missing evidence.
3. A human confirms consequential actions. Timeouts may later become eligible
   for policy-approved automation; bans, mass actions, and destructive cleanup
   are never default autonomous tools.
4. The member-facing notice, private staff record, Discord effect, and private
   appeal link/reference remain consistent.
5. An in-guild member appeals through a private modal; a timed-out, kicked, or
   banned member can use the application DM appeal route tied to guild and case
   reference. Intake reveals only member-visible evidence and status.
6. An uninvolved authorized reviewer accepts, requests information, changes or
   upholds the action, records reasoning, and notifies the appellant privately.
   Tests cover in-guild, DM-only, expired/invalid reference, privacy, and
   outcome effects.

### 8. Remove and reinstall the bot

1. A guild-removal event immediately tombstones the guild and revokes active
   service-principal grants, scheduled jobs, integration deliveries, AI work,
   and outbound retries.
2. Discord resource bindings remain inert evidence; no cleanup assumes the bot
   can still mutate the guild.
3. Configured retention decides which audit/legal records remain and when
   member data, memories, schedules, and integration credentials are purged.
4. Purge is idempotent and visible to the operator. Reinstall starts in a safe
   unconfigured/recovery state and may re-adopt retained resources only after
   fresh owner authorization.

## Scope by release boundary

### MVP

- server profile setup/repair and owner recovery;
- Home/navigation and central admission control;
- typed guild/game/build/tester/cohort configuration;
- welcome, roles, logging, deterministic moderation and baseline AutoMod;
- build publishing, Scheduled Event playtests, enrollment, reminders, polls;
- Forum intake and triage for bugs/feedback;
- AI gateway, durable scoped memory, inspect/plan/act loop, policy, audit,
  diagnostics, and the setup/playtest/feedback tools needed by the journeys;
- health/support report and safe AI/provider kill switches.

### After MVP evidence

- GitHub issue export or sync;
- community highlights, lightweight participation recognition, LFG;
- game-client webhooks/APIs and richer build automation;
- broader language/community automation and analytics;
- a web operator surface only if Discord cannot present the needed evidence.

### Excluded

Economy/casino/content games, BTD6 commands, unrelated game knowledge tools,
full ticketing, arbitrary AI code/shell/SQL/HTTP tools, and bulk legacy data
migration are not dormant MVP flags; they are outside the product boundary.

## Product acceptance rules

- A feature is not “present” until a permitted user can reach it, complete its
  effect, see the result, and recover from failure.
- A tester funnel is not successful until the external opt-in/access/install/
  launch transition is evidenced or a concrete blocked state is routed.
- No panel describes captured or assumed live state; all stateful content is
  rendered from a read model at interaction time.
- Disabled features do not advertise dead commands or buttons.
- Every write has a deterministic non-AI route and the same authorization,
  workflow, audit, and verification path as an AI-originated write.
- User-visible wording names the resource and outcome, not internal subsystem
  vocabulary.
- Destructive or broad changes always state impact and rollback limits before
  confirmation.
