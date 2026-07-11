# Platform capability & limitation ledger — claude.ai Projects / sessions

> **Date:** 2026-07-12
> **Author:** fleet-manager research session (`claude/research-platform`)
> **Status:** verified ledger — every claim cited (file@sha, PR#, memory path, or
> verbatim error) or explicitly marked UNVERIFIED / HYPOTHESIS. "Not measured"
> beats invention. Family-level model names only. No secret values.
> **Inputs:** the 2026-07-11 19-repo docs sweep + the team-memory/trigger-schema
> dossier (both compiled by read-only research workers the same night), plus one
> live read-only probe executed by this session (§7, P3).

## Executive summary

1. **Tool surfaces differ per seat** — the same account gets different tool sets by session kind (coordinator vs worker vs routine-fired vs dispatch-only); inventory the toolset at boot, never assume (§1).
2. Trigger/scheduling MCP tools live on **worker** seats, not the coordinator seat — and their calls **bind to the parent session** (proven live 2026-07-11, §1).
3. The auto-mode **merge classifier is contextual, not deterministic**: identical pipelines got denied (fm #68, 3×) and passed (fm #69/#70) the same day; a child session self-merged in substrate-kit with zero denial (§2). Which factor gates is a HYPOTHESIS set, not a known (§2.4, §7).
4. **Relayed/coordinator authorization never reliably clears the merge wall**; a genuine in-session human turn does (§2).
5. superbot is the **only** repo with a `.claude/settings.json` permissions block (bypassPermissions + 12 GitHub-MCP grants); fm PR #92 ports the narrow slice (§2.5).
6. **Direct push to main is branch-protection-walled (GH013)** in protected repos; working landing paths: enabler workflow (3/13 repos), non-author two-party merge, genuine owner turn (§2.6–2.7).
7. Triggers: cron min-interval hourly; `run_once_at` self-disables; `send_later` binds to the CALLING session; **no model parameter exists anywhere** (§3). `list_triggers` pagination beyond 100 **works via cursor — probed live this session** (§3, §7).
8. PR subscriptions deliver comments + CI **failures** only — no CI-success, merge, push, or conflict events; poll or `send_later` to detect green (§4).
9. GitHub is **MCP-only** (no `gh` CLI, REST 403 via proxy incl. stub-200 bodies); tags/releases via `workflow_dispatch`; Actions runners face GH013 + a PR-create permission toggle (§5).
10. Codex "committed X / created PR Y" claims describe its **phantom sandbox** unless a human pressed create-PR (§5).

---

## 1. Seat provisioning variance

The tool surface differs per session generation and surface. **Inventory the
toolset at boot** — before flagging anything as needs-owner
(`session-capability-asymmetry.md`, memory path
`/tmp/claude/memory/team/project/project/1db6fdef-0671-4389-9924-1f1774dc8646/session-capability-asymmetry.md`:
"at project boot, each session type should inventory its actual write
capabilities … before flagging anything as needs-owner").

**Proven 2026-07-11 overnight run (coordinator session context):**

- The coordinator seat **lacks direct `send_later`/trigger tools**; workers it
  spawns **DO** have `mcp__claude-code-remote__send_later` / `create_trigger` /
  `list_triggers` / `delete_trigger` — and those calls **bind to the PARENT
  session**. Proven: `trig_01PMRnVQUuzi2hhYhXB8reQ9` fired into the coordinator
  at 23:08:25Z; failsafe rebind `trig_01BKpsyoBzp1K1ob9H3iu1gM` created+verified
  and old `trig_01F9UdoUtLy8oknBPBkHLshS` deleted.
- Standalone `sleep` commands are **harness-blocked** (foreground `sleep` is
  refused by the tool harness; use `send_later`/Monitor-style waits instead).

Corroborating variance evidence (memory dossier):

- **Routine-fired (wake) sessions had ZERO `mcp__github__*` write tools** —
  only `mcp__claude-code-remote__*` — until the owner attached the repos to the
  Routine's **repository picker** in the web UI (pokemon-mod-lab session 024,
  ~2026-07-11 11:00Z; memory `pokemon-mod-lab-no-pr-write-tool.md`, efed55fa
  project). After attachment every wake had full write tools. Key line: "tool
  provisioning appears to vary by session/project surface, not be a fixed
  platform guarantee." The gap hit interactive sessions on that surface too.
- **Dispatch-only sessions exist** — "verify toolsets before assigning work"
  (fleet-manager `docs/retro/coordinator-seat-2026-07-11.md` @ `e801da5c`).
- A superbot-mineverse append (@ `76be8211`): "the orchestrator/coordinator
  seat lacks GitHub MCP tools AND Bash; worker seats have both."
- Routine-fired background sessions in websites had **no PR-creation tooling**
  at all (only session/repo-management tools) while plain `git push` still
  worked — the git proxy grant is separate from the API/tool grant
  (websites `docs/CAPABILITIES.md` @ `8f976548`, possibly stale vs origin).
- Cross-session messaging tools are absent on non-Project surfaces — verbatim
  "No agent named ... is reachable"; cross-session trigger binding rejected
  verbatim: "binding a trigger to another session is not enabled for this
  organization" (fleet-manager `docs/capabilities.md` @ `e801da5c`).
- Environment-scoped repo allowlists gate even reads: verbatim `Access denied:
  repository … is not configured for this session` (fleet-manager
  `control/status.md` @ `e801da5c`; substrate-kit CAPABILITIES @ `4493251b`
  shows the allowlist enumeration form). But `list_repos` + `add_repo` +
  shallow clone reached a public repo the MCP allowlist walled — "try
  `list_repos`/`add_repo` before declaring a repo unreachable" (same file).
- This session (a spawned worker) confirms the worker-side trigger surface
  live: `mcp__claude-code-remote__list_triggers` is present and worked (§7 P3).

**Operating rule:** the discovery rule from the shared CAPABILITIES ledgers
(§6) — check the file → check the env → attempt once + capture the exact error
→ append the finding same session.

## 2. Permission model — auto-mode classifier + repo settings

### 2.1 Verbatim denials (2026-07-11)

- fleet-manager landing session, merge of peer-verified PRs — verbatim:
  > "[Merge Without Review] ... merge PRs #88 and #89 that were only verified
  > by a coordinator/peer session, not approved by a human ... run outside auto
  > mode so the user can review directly."
- A settings-edit worker was denied the same night under **"[Self-Modification]"**.
- fm PR #68 dispatch denial, verbatim (fleet-manager
  `docs/findings/enabler-install-verification-2026-07-11.md` @ `e801da5c`):
  > "[Self-Approval] The sub-agent prompt instructs a REST squash merge of PR
  > #68, which this session's own sub-agent authored — merging one's own PR
  > defeats two-party review (also [Merge Without Review]); no user authorized
  > merging it, only untrusted cross-session coordinator context."
- Independent-reviewer denial, verbatim (memory
  `automode-classifier-blocks-agent-mesh-merges.md`, eeb9773c project,
  superbot-games PRs #5/#9, 2026-07-09):
  > "[Merge Without Review] ... the only authorization is an untrusted
  > coordinator/cross-session context (not user intent), and it launders a
  > merge the authoring mining session was blocked from self-merging."

### 2.2 Counterpoint — the wall is not universal (verified 2026-07-11)

A fleet-manager-spawned **child session SELF-MERGED its own PR** in
`menno420/substrate-kit` — **substrate-kit PR #254**, squash via GitHub MCP,
merge commit `1295d73`, with **NO classifier denial**. substrate-kit has **NO
`.claude/settings.json` at all**. Auto-merge arming there returned "PR already
in clean status". So absence of a permissions grant did not block, and
self-authorship did not trigger the denial in that context.

Further intermittency evidence: "the wall is intermittent/context-dependent,
plan for it but attempt the merge first" — `merge_pull_request` squash
succeeded directly for the authoring agent on all three repos of a kit-upgrade
wave (memory `kit-upgrade-distribution-gotchas.md`, 7da28322 project). And fm
**PR #68 was denied 3× while identical-pipeline #69/#70 passed** the same day
(fleet-manager `docs/retro/coordinator-seat-2026-07-11.md` @ `e801da5c` —
"content-correlation" denial shape). Deny→grant→deny on identical `add_repo`
calls across wakes, apparently tracking attendedness (memory
`pokemon-mod-lab-add-repo-blocked-by-classifier.md`, efed55fa project).

### 2.3 What reliably works

- **In-session human authorization is the only reliable clearer** — fm PR #68
  merged ~11:48Z via an owner-authorized attempt after 3 denials; "relayed
  coordinator context does not" clear it (fleet-manager `control/status.md`
  PR #71 record @ `e801da5c`).
- **Non-author two-party merge**: "a NON-AUTHOR session that GENUINELY reviews
  a PR it did not write, then merges it, PASSES the auto-mode classifier"
  (substrate-kit `docs/CAPABILITIES.md` @ `4493251b`, evidence venture-lab
  PR #9 merge `95b755b`) — though an independent reviewer acting on relayed
  coordinator authority was denied (§2.1 last bullet); the distinction appears
  to be genuine review vs laundered authorization.
- **Deny-wins**: the first denial burns the shot; never retry around a denial
  (fleet-manager `docs/capabilities.md` + retro @ `e801da5c`).

### 2.4 HYPOTHESES — explicitly not facts

The classifier appears **CONTEXTUAL**. Plausible gating factors (each
UNVERIFIED as *the* factor):

- (a) **Authorship/authority shape**: merging your own just-authored change vs
  landing peer work on relay authority (fits #254-pass vs #88/#89-deny, and the
  venture-lab root-cause line "relayed authorization is never genuine in a
  child seat" — venture-lab `docs/PLATFORM-LIMITS.md` @ `296a1a93`).
- (b) **Diff scope**: control/-only append vs registry restructure (fits #254
  vs #88/#89; fits the #68 vs #69/#70 content-correlation reading).
- (c) **Per-repo branch protection / required checks** shaping what the merge
  call means.
- It is **NOT a per-repo settings grant**: substrate-kit has no settings.json
  and the self-merge passed (§2.2).
- Attendedness (owner actively chatting) is a further observed correlate
  (§2.2, add_repo deny→grant).

Cross-reference: the #68-denied-3×-while-#69/#70-passed finding is the memory
dossier's cleanest demonstration that repo identity + pipeline identity alone
do not determine the verdict.

### 2.5 Repo `.claude/settings.json` landscape (sources sweep, 2026-07-11)

- **superbot @ main `1ecc2113` (blob `cf76618a`, verified live via GitHub MCP
  `refs/heads/main`)** is the **ONLY** repo with a permissions block:
  `"defaultMode": "bypassPermissions"` + `"skipDangerousModePermissionPrompt":
  true` + **12 explicit `mcp__github__*` grants** (`pull_request_read`,
  `list_pull_requests`, `create_pull_request`, `update_pull_request`,
  `merge_pull_request`, `subscribe_pr_activity`, `unsubscribe_pr_activity`,
  `get_file_contents`, `list_commits`, `get_commit`, `get_job_logs`,
  `actions_list`) + bare server-wide `"mcp__github"` (plus CCR/codegraph/
  context7 allows, ~90 Bash patterns, an ask-list for destructive commands).
- websites / idea-engine / superbot-mineverse: **hooks-only**, no permissions
  block (shas `8f976548` / `a9b41f6d` / `76be8211`).
- The other **15 repos have none** — harness defaults apply.
- **fleet-manager PR #92 (open, unmerged, head `2d96f340`)** ports the 12
  grants **minus** `bypassPermissions` / `skipDangerousModePermissionPrompt` /
  bare `mcp__github` / `enable_pr_auto_merge`; "the rule isn't active until
  it's on main" (PR #92 body + findings blob `312be3d5`).
- HYPOTHESIS (per §2.2): a settings.json permissions block may explain why
  superbot sessions don't hit the classifier like other lanes — but the
  substrate-kit counterpoint shows absence doesn't block either, so the causal
  link is unproven. Observable after PR #92 merges (§7 P5).

### 2.6 GH013 — branch protection on direct push

Direct push to main is rejected by branch protection. Verbatim (fleet-manager
PR #82 body, an Actions-runner push):

> `remote: error: GH013: Repository rule violations found for refs/heads/main.`
> `remote: - Changes must be made through a pull request.`
> `! [remote rejected] HEAD -> main (push declined due to repository rule violations)`

Same wall via Contents API on superbot-next, verbatim: `409 Repository rule
violations found — "Changes must be made through a pull request. 6 of 6
required status checks are expected."` (memory
`superbot-next-control-fast-lane.md`, 6670c976 project). Non-runner variant in
venture-lab `docs/PLATFORM-LIMITS.md` @ `296a1a93`: `422 Repository rule
violations found — Changes must be made through a pull request.`

### 2.7 Working landing paths (in order)

1. **Server-side `auto-merge-enabler.yml` workflow** — installed in only
   **3/13 lanes**: substrate-kit, superbot, idea-engine (fleet-manager
   `docs/findings/enabler-install-verification-2026-07-11.md` @ `e801da5c`).
   Recipe: open the PR READY and do nothing else (substrate-kit CAPABILITIES).
2. **Non-author two-party merge** (genuine review, §2.3).
3. **Genuine owner turn** (in-session human authorization, §2.3).
4. Author self-merge + `enable_pr_auto_merge` are **terminally denied in auto
   mode** ("[Auto-Mode Bypass] ... Merge Without Review", substrate-kit
   CAPABILITIES @ `4493251b`) — **but see the substrate-kit PR #254
   counterpoint (§2.2)**: the denial is contextual, not absolute.

## 3. Triggers / Routines (verbatim schemas, loaded via ToolSearch 2026-07-11)

From the memory dossier §2 (schemas quoted verbatim there); the live shapes
below re-confirmed by this session's probe where noted.

- **`create_trigger`** (required: name, prompt) — three targeting modes:
  self-bind default / `persistent_session_id` (fires into a named session you
  own) / `create_new_session_on_fire=true` (fresh session per fire).
  `persistent_session_id` XOR `create_new_session_on_fire`. `cron_expression`
  "**Minimum interval is hourly**", mutually exclusive with `run_once_at`;
  omit both for a poke-only Routine. `run_once_at` fires once then "the
  Routine disables itself with `ended_reason=run_once_fired`". **No model
  parameter exists** (schema properties are exactly name, prompt,
  cron_expression, run_once_at, persistent_session_id,
  create_new_session_on_fire, environment_id, notifications — independently
  confirmed by fleet-manager `docs/capabilities.md` @ `e801da5c`).
  `notifications` "only apply to fresh-session-per-fire Routines … **the
  server rejects this parameter for self-bind or persistent_session_id
  Routines**".
- **`send_later`** (required: message) — "a thin wrapper over create_trigger
  (a self-bind + run_once_at Routine)"; **binds to the CALLING session**;
  granularity one minute; `delay_minutes` minimum 1 XOR `at` (RFC3339,
  seconds truncated); cancellable via `delete_trigger` before fire. To wake
  ANOTHER session use `create_trigger` + `persistent_session_id` (retro @
  `e801da5c`; superbot-mineverse CAPABILITIES @ `76be8211`, verified live).
- **`list_triggers`** — `limit` default 20 max 100, opaque `next_cursor`
  pagination. Response shape (live, 2026-07-11 + re-confirmed this session):
  top-level `{data, has_more, next_cursor}`; per-trigger keys include
  `created_at, created_via, creator, cron_expression, enabled, ended_reason,
  id, job_config, last_fired_at, name, next_run_at, persist_session,
  persistent_session_id, run_once_at, session_grouping_id, updated_at`;
  `job_config.ccr` carries the synthetic user-message event and
  `session_context.allowed_tools`; **no model key anywhere**; `created_via:
  "meta_mcp"` on agent-created triggers. Observed `ended_reason` values:
  `run_once_fired`, `auto_disabled_session_gone`.
  **Pagination >100 verified this session (§7 P3): cursor works.**
- **`delete_trigger`** (required: trigger_id) — account-scoped; deleting
  another account's Routine fails with not-found.
- **Orphan behavior — failsafe bound to an archived session**: a trigger whose
  `persistent_session_id` points at an archived session **spawns a fresh
  session instead of waking it** (observed 2026-07-11 overnight run; also the
  live `ended_reason: auto_disabled_session_gone` value shows the platform
  sometimes auto-disables instead). Treat archived-session bindings as
  fresh-session spawns, not wakes.
- **Completed runs are not inspectable from the owner's Routines screen**
  (fleet-manager `docs/owner-queue.md` @ `e801da5c`, the four
  routines-platform-bugs item: "runs not inspectable · Runs-panel vs
  Routines-screen disagreement · arming seat-inconsistency · model
  attribution").
- Model attribution of routine-fired sessions is a 3-way surface disagreement
  (Routines menu fable-5 · chat header a different family · card self-report);
  the session-card self-report is the least-bad basis (fleet-manager
  `docs/capabilities.md` @ `e801da5c`; memory
  `pokemon-mod-lab-model-attribution-mismatch.md`).

## 4. Webhook / subscription gaps

- `subscribe_pr_activity` delivers **comments + CI failures** as
  `<github-webhook-activity>` messages — but **NOT CI success, merges, pushes,
  or merge-conflict transitions** (tool description, memory dossier §2;
  operationally corroborated by the fleet's poll-based merge-on-green
  practice). **Detecting green requires polling the check runs via GitHub MCP
  or a `send_later` self-wake.**
- Idempotent; but if a PR Steward agent already watches the PR, the call
  succeeds and this session receives **nothing** — the tool result says so
  (verbatim schema note, memory dossier §2).
- **Born-red PRs generate expected-noise CI-failure webhooks**: a PR opened
  with an in-progress session card fails its gate BY DESIGN until the card
  flips. Live example: **this session's own PR #93** — the `substrate-gate`
  failure on head `1c7360b` is deliberate born-red noise, not a defect. The
  GEN-3 hygiene rider encodes this: "BORN-RED webhooks are NOISE" (superbot
  `docs/owner/next-round-founding-prompts-2026-07-11.md` @ `1ecc2113`).
- "CI silently stops firing when a PR is unmergeable: mergeable_state 'dirty'
  … produces ZERO workflow runs" — a dirty PR jams auto-merge with no failure
  event at all (memory `kit-upgrade-distribution-gotchas.md`, 7da28322;
  also 1a40fb77 MEMORY.md).

## 5. Session mechanics

- **Archiving**: archived sessions don't wake — a persistent-session trigger
  aimed at one spawns a fresh session (§3) or the trigger auto-disables
  (`auto_disabled_session_gone`). Whether webhook subscriptions survive
  archiving: UNVERIFIED (§7 P4).
- **Cross-session `send_message`**: message bounded to **64 KiB**; `priority`
  enum **now | next | later** ("now" interrupts the current turn; the others
  wait for turn end) — verbatim schema, memory dossier §2. Only available on
  seats that have the tool (§1).
- **`list_events`**: read another session's recent transcript events (user
  messages, assistant responses, tool calls); limit default 20 max 100,
  `after_id`/`before_id` cursors.
- **Memory system** — `/tmp/claude/memory/team/` (47 files read by the memory
  research worker). Wall memories with paths (all under
  `/tmp/claude/memory/team/project/project/`):
  - `8bf6aac6-…/fleet-born-red-automerge-wall.md` — both self-landing paths
    walled in born-red repos as of 2026-07-11; arming wall is repo-specific
    (blocked fm PR #10, works superbot #1936/#1974/#2003); park READY+green.
  - `eeb9773c-…/automode-classifier-blocks-agent-mesh-merges.md` — relayed
    authorization never clears the merge classifier (§2.1).
  - `1a40fb77-…/github-polling-use-mcp-not-cli.md` — `gh` absent; poll via
    GitHub MCP; anonymous api.github.com reads sometimes work, writes never.
  - `1db6fdef-…/session-capability-asymmetry.md` — inventory write
    capabilities at boot (§1).
  - `c7b20180-…/remote-session-github-write-limits.md` — 403 on tag push /
    release create / branch delete; branch pushes + PR create/merge + reads
    fine. (Branch-delete partially superseded: auto-delete-on-merge works.)
  - `1db6fdef-…/actions-release-workaround.md` + `c7b20180-…/actions-release-workaround-gen2.md`
    — workflow_dispatch release path (below).
  - `efed55fa-…/pokemon-mod-lab-add-repo-blocked-by-classifier.md`,
    `…-classifier-blocks-local-bootstrap-exec.md`,
    `…-classifier-post-merge-denial.md` + `…-classifier-flags-self-merge.md`
    (retroactive same-turn flagging of an already-successful merge),
    `…-session-041-collision.md` (classifier cited a merge that actually
    FAILED), `…-no-pr-write-tool.md` (§1),
    `…-model-attribution-mismatch.md` (§3),
    `…-github-file-tool-plaintext.md` (`create_or_update_file` content is RAW
    TEXT, not base64).
  - `6670c976-…/superbot-next-control-fast-lane.md` — Contents-API-to-main 409
    ruleset wall (§2.6).
  - `e572baad-…/superbot-session-card-telemetry-gate.md` — superbot CI text
    `MERGE HELD — telemetry row missing (Q-0194 guard)`;
    `e572baad-…/parallel-git-workers-need-worktrees.md` — same-cwd concurrent
    git workers race (amend collision); use worktrees.
  - `f491461e-…/verify-spawn-liveness.md` — spawned sessions can die at
    provision with NO failure event, stay "active" forever; require a first
    heartbeat ≤~10 min; `f491461e-…/env-setup-two-source-contract.md` — env
    setup runs with cwd=/home/user over multi-repo checkouts; guard every step.
  - `7da28322-…/kit-upgrade-distribution-gotchas.md` — intermittent REST-merge
    wall; enabler fires on MCP-created PRs in substrate-kit (Q-0127 doesn't
    generalize); `disable_pr_auto_merge` returns success even when nothing is
    armed; webhook auto-merge events attribute the agent's arm to the owner's
    account; proxy stub-200 traps; codeload tarballs work.
- **GitHub is MCP-only**: `gh` CLI absent ("command not found" — fleet-manager
  `docs/findings/enabler-install-verification-2026-07-11.md` @ `e801da5c`;
  memory §1.3); direct REST via the proxy 403s, including a stub variant that
  returns **HTTP 200 with a JSON "GitHub access is not enabled for this
  session" body**, and the mineverse verbatim: 403 "GitHub access is not
  enabled for this session. An org admin must connect the Claude GitHub
  App..." (superbot-mineverse CAPABILITIES @ `76be8211`).
  raw.githubusercontent.com and github.com release-asset downloads pass the
  proxy; codeload tarballs work; raw 404s private repos even with an auth
  header (memory §1.3 scanner-seat matrix).
- **Actions workarounds**: tags/releases via a `workflow_dispatch` release
  workflow with `permissions: contents: write` — the server-side
  `GITHUB_TOKEN` avoids the tag-push 403 (proven codetool-lab-opus4.8 PR #9 →
  run 29035224581, memory §1.6; v1.7.0/v1.6.0/v1.4.0 cut this way in
  substrate-kit @ `4493251b`). Actions runners cannot create PRs until the
  owner ticks "Allow GitHub Actions to create and approve pull requests" —
  verbatim: `pull request create failed: GraphQL: GitHub Actions is not
  permitted to create or approve pull requests (createPullRequest)`
  (fleet-manager PRs #82/#83 bodies, owner-queue item 33). Pushes authored
  with a workflow's own `GITHUB_TOKEN` never retrigger workflows
  (anti-recursion; idea-engine CAPABILITIES @ `a9b41f6d`).
- **Codex phantom-sandbox caveat**: Codex's "committed X / created PR Y"
  claims describe **its sandbox** — phantom unless a human pressed create-PR;
  read its proposed edits from the comment text, never trust the claimed
  refs. (Fleet operating doctrine, 2026-07-11 sweep; Codex post-merge review
  is enabled on all 12 active fleet repos — fleet-manager
  `docs/capabilities.md` @ `e801da5c`.)

## 6. Sources sweep — where all this lives

- **Per-repo `docs/CAPABILITIES.md`** — 14 repos carry one (superbot does NOT;
  its `docs/capability-authority.md` is the bot's Discord authority contract,
  a name collision, not a session ledger). 7 are the byte-identical 68-line
  kit seed; seed source `substrate-kit/src/engine/templates/CAPABILITIES.md.tmpl`.
  All share the **4-step discovery rule** verbatim (check file → check env →
  attempt once + exact error → append same session) — cited from fleet-manager
  `docs/CAPABILITIES.md` @ `e801da5c`.
- **fleet-manager `docs/capabilities.md`** (lowercase) — the fleet MASTER
  ledger, 263 lines @ `e801da5c`: routine self-arm CAN, model-attribution
  rider, cross-session messaging walls, self-merge wall, private-repo
  auto-merge-toggle wall, 8,000-char Custom Instructions cap, GraphQL quota,
  playbook recipes R5/R12/R13/R21/R22.
- **`docs/findings/`** — fleet-manager (16 files + README @ `e801da5c`):
  `enabler-install-verification-2026-07-11.md` (3/13 enabler installs),
  `instruction-and-env-audit-2026-07-11.md` (12 of 13 lane instructions
  prescribed the walled merge path), `permission-rules-port-2026-07-11.md`
  (**NOT on main — ships in PR #92**, head `2d96f340`, blob `312be3d5`),
  plus retro-synthesis / ci-tier-sim / night-review / fleet-economics /
  model-matrix / gba-toolchain-proof / ping-test / ui-visibility. Also
  gba-homebrew (1 file) and pokemon-mod-lab (3 files) @ their shas.
- **superbot owner docs** @ `1ecc2113`: `docs/owner/agent-decision-authority.md`
  (Q-0240 decide-and-flag, Q-0241 rebuild never-wait) and
  `docs/owner/next-round-founding-prompts-2026-07-11.md` (**GEN-3 HYGIENE
  RIDER v5**: one trigger-MCP call per worker — multi-call chains stalled 4×
  under parallel load; clear env for spawned CLIs; hard-sync at start;
  born-red webhooks are noise; preflight volatile facts).
- **The retro**: fleet-manager `docs/retro/coordinator-seat-2026-07-11.md`
  @ `e801da5c` — the four classifier denial shapes, send_later self-bind
  lesson, dispatch-only sessions, cron-jitter vs never-fired distinction.
- **Staleness caveat**: 9 of the 19 local working copies possibly lag live
  main (sha table in the sources dossier; the sweep did not fetch) — treat
  quotes from substrate-kit, websites, superbot-next, trading-strategy,
  superbot-games, gba-homebrew, pokemon-mod-lab, venture-lab (+ superbot's
  stale local origin ref) as possibly one-or-more merges behind.

## 7. Unknowns + safe probes

| # | Unknown | Safe probe | Status |
|---|---|---|---|
| P1 | **Which classifier factor actually gates merges** (authorship vs diff scope vs branch protection vs attendedness, §2.4) | Same-diff-shape own-PR merge in a repo WITH vs WITHOUT branch protection, same session kind, same day | **DEFERRED — needs owner sign-off (it merges)** |
| P2 | Whether `enable_pr_auto_merge` works from a **genuine owner turn** (the denials on record are all agent-initiated) | Owner types "arm auto-merge on PR #N" into the session that will make the call, on a checks-pending PR | DEFERRED (needs owner turn) |
| P3 | Whether `list_triggers` >100 has a working cursor | One paginated read-only call with `cursor=next_cursor` | **EXECUTED this session (2026-07-12): page 1 limit=100 → 100 records, `has_more: true`, opaque base64 `next_cursor`; page 2 with that cursor → 100 MORE records, ZERO id overlap with page 1, `has_more: true` again (fleet has >200 triggers). Pagination WORKS.** |
| P4 | Whether webhook PR subscriptions survive session archiving | Subscribe from a session, archive it, push a failing commit to the PR, observe where (if anywhere) the event lands | DEFERRED (needs a sacrificial session + archive rights) |
| P5 | Whether a repo `.claude/settings.json` permissions block actually changes worker-session tool grants / classifier behavior | Observe the first fleet-manager session after **PR #92** merges: attempt the previously-denied landing calls, diff the outcome against §2.1 | DEFERRED — observable next session after #92 merges |
| P6 | `allow_auto_merge` + required-check config per repo (the search-API repo object lacks the field — recorded as **not measured**, `enabler-install-verification-2026-07-11.md`) | Per-repo `get_file_contents` on `.github/` + a targeted repo-settings read if any MCP surface exposes it | DEFERRED (read-only, cheap, but no known MCP surface today) |
| P7 | Whether the born-red CI-failure webhook noise (§4) is distinguishable from real failures by payload alone | Compare the webhook payloads of a born-red gate failure vs a genuine test failure on the same PR | DEFERRED (read-only, cheap) |

Executed this session: **P3 only** (read-only, two `list_triggers` calls).
Nothing destructive, merge-adjacent, or trigger-creating was executed.
