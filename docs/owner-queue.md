# Owner queue

> **Status:** `living-ledger` — the ONE deduplicated queue of things waiting on the owner.
> The manager adds/removes items; asks stay valid until acted on (playbook R11).
> Every item below must carry WHAT/WHERE/HOW/WHY/UNBLOCKS + proof it's owner-only (R17).

Rewritten **2026-07-11 (verified fleet-wide sweep — every item re-checked against
live state; PR #75)**. Every finding below was verified TODAY (2026-07-11,
~13:30–15:00Z) by read-only workers — citations are given per item. Lineage:
previous full rewrite 2026-07-10 (morning) + four same-day amendments + the
2026-07-11 ORDER 010 relay stamp; launch context:
[`planning/gen2-launch-record-2026-07-10.md`](planning/gen2-launch-record-2026-07-10.md);
the Q-0261 launch-readiness checklist that seeded items 9–12 of the previous
rewrite: [`launch-readiness-2026-07-10.md`](launch-readiness-2026-07-10.md).

**Old-item mapping (superseded/absorbed by this rewrite):** item 3 (4-patch
playtest → now SIX patches, folded into E#28(2)) · item 4 Track B (→ E#28(3)) ·
item 11 (→ C#15 paste wave) · item 12(b) (→ B#7) · item 15 (→ D#26) · item 14
(split: §5 veto → E#29, plugin seed push → C#18). Resolved-today findings are in
"Resolved 2026-07-11 (verified)" below.

Item fields (R17, kit grammar): **WHAT · WHERE (click-surface URL) · HOW
(click-level) · UNBLOCKS · VERIFIED-NEEDED (evidence citation) · blocking?**

**Stable ids (P2, 2026-07-11, fm PR #85):** every active item carries an
`id: OQ-<slug>` line — content-derived, NEVER positional (this file's own
PR #75 renumbering broke a cross-reference; numbers reshuffle on every
rewrite, slugs survive it). Cross-references cite the slug, not "item N".
An item keeps its slug for life — through rewrites, regrouping, and its
move to Resolved. `scripts/check_owner_queue.py` enforces presence +
uniqueness and probes cited-PR state at each wake/regen;
`docs/owner-queue-candidates.md` (GENERATED) is the intake feed the
manager curates from.

## Active queue — grouped by click surface

### (A) GitHub merges — one click each

*(Empty — the whole 2026-07-11 merge group was clicked by the owner ~14:56Z;
see "Resolved 2026-07-11 (P3 curation sweep)" below.)*

### (B) GitHub settings / repo admin

5. **pokemon-mod-lab OA-1 — add required check `ROM builds` (keep
   substrate-gate).**
   - id: OQ-POKEMON-ROM-REQUIRED-CHECK
   - WHERE: https://github.com/menno420/pokemon-mod-lab/settings/rules → main
     ruleset → Require status checks.
   - HOW: add context `ROM builds`; leave substrate-gate in place.
   - UNBLOCKS: true merge-on-green — today a red ROM build could merge.
   - VERIFIED-NEEDED: control/status.md@`f69ab95` (⚑ OWNER-ACTION 1, re-stated
     14:10Z today); rulesets are a verified owner-only wall
     (docs/PLATFORM-LIMITS.md).
   - Blocking: not-blocking, but a live gate hole.

6. **superbot-mineverse — add required check `pytest`.**
   - id: OQ-MINEVERSE-PYTEST-REQUIRED-CHECK
   - WHERE: https://github.com/menno420/superbot-mineverse/settings/rules →
     main ruleset → Require status checks.
   - HOW: add context `pytest`.
   - UNBLOCKS: test-gated merges without coordinator babysitting.
   - VERIFIED-NEEDED: LIVE-PROVEN today — PR #30 merged 10:25:33Z while its
     pytest check completed 10:26:13Z: the PR merged **40 s before pytest
     finished**; only substrate-gate gated. Rulesets = owner-only wall.
   - Blocking: not-blocking, but a live, demonstrated gate hole.

7. **superbot-next OA-3 — enable merge queue OR drop require-up-to-date for
   `docs/**` + `control/**`.**
   - id: OQ-NEXT-MERGE-QUEUE
   - WHERE: https://github.com/menno420/superbot-next/settings/rules
   - HOW: either enable the merge queue on main, or relax "require branches to
     be up to date" for docs/control paths.
   - UNBLOCKS: kills the update-branch dance on the 6-check ruleset (every
     unattended Builder session loses time to it).
   - VERIFIED-NEEDED: control/status.md@`168ef80` line 20(b) (today,
     15:46+0200). Rulesets = owner-only wall. *(Absorbs old item 12(b).)*
   - Blocking: not-blocking; chronic time sink.

8. **trading-strategy — tick "Allow auto-merge".**
   - id: OQ-TRADING-ALLOW-AUTOMERGE
   - WHERE: https://github.com/menno420/trading-strategy/settings → General →
     Pull Requests.
   - HOW: tick the "Allow auto-merge" checkbox.
   - UNBLOCKS: native auto-merge — ends the lane's poll-and-merge workaround.
   - VERIFIED-NEEDED: control/status.md@`3172b43` ⚑(c), reconfirmed on PR #36
     (the "unstable status" arming failure); a direct API read of the setting
     field was unavailable to agents this session (exact-wall evidence).
   - Blocking: not-blocking (REST-squash workaround in use, PRs #40–#43).

9. **product-forge — post-seed settings residue: Allow auto-merge + required
   gate.**
   - id: OQ-FORGE-SETTINGS-RESIDUE
   - WHERE: https://github.com/menno420/product-forge/settings
   - HOW: tick "Allow auto-merge"; make the substrate gate / smoke check a
     required check on main.
   - UNBLOCKS: self-landing forge PRs.
   - VERIFIED-NEEDED: old queue item 9's residue, unchanged today;
     required-check settings are agent-unreadable/unwritable.
   - Blocking: not-blocking.

10. **substrate-kit P10 — swap required checks to `kit-quality`,
    up-to-date OFF.**
   - id: OQ-KIT-P10-REQUIRED-CHECKS
    - WHERE: substrate-kit → Settings → Rules → main ruleset (rulesets 403 for
      agents).
    - HOW: REMOVE "Kit test suite" + "Cold-adoption smoke", ADD `kit-quality`;
      set "Require branches to be up to date" OFF.
    - UNBLOCKS: retires the legacy alias jobs / the W-9 false-alarm class.
    - VERIFIED-NEEDED: carried from kit ⚑ OWNER-ACTION 2 @ `2aa7a51` (the P4
      daily-loop half of the old combined item is self-armed agent-side — see
      Resolved below).
    - Blocking: not-blocking.

11. **websites — delete 4 stale branches.**
   - id: OQ-WEBSITES-STALE-BRANCHES
    - WHAT: delete `claude/harden-verify`, `claude/rework-dashboard`,
      `claude/wire-github-token-docs`, `manager/control-plant`. **NOT**
      `claude/anthropic-review-site` (belongs to open PR #132).
    - WHERE: https://github.com/menno420/websites/branches (or Settings →
      enable "Automatically delete head branches").
    - HOW: trash-icon per branch.
    - UNBLOCKS: branch-list hygiene only.
    - VERIFIED-NEEDED: all 4 still on remote today (ls-remote); agents 403 on
      every deletion path (docs/CAPABILITIES.md@`52381a9`).
    - Blocking: cosmetic.

12. **gba-homebrew — create the Lumen Drift GitHub Release.**
   - id: OQ-GBA-LUMEN-RELEASE
    - WHERE: https://github.com/menno420/gba-homebrew/releases/new
    - HOW: tag `lumen-drift-v1.3` (create on publish, target main) → title
      `Lumen Drift v1.3` → attach `dist/lumen-drift.gba` (167,996 B; put sha256
      `195a86795e57e2fa0059a96782f1ac7a147cbcebc0cb28a96f353e5d9babae94` in the
      notes) → point notes at `docs/PLAYING.md`.
    - UNBLOCKS: a downloadable player artifact for the 07-14 sitting + the
      venture itch.io path (D#27).
    - VERIFIED-NEEDED: today — ZERO releases AND zero tags on the repo
      (`ls-remote --tags` empty; `list_releases` = `[]`); tag-push 403 wall
      stands (docs/CAPABILITIES.md@`e00612c`). (Also carried: gba merged-branch
      cleanup — agent 403.)
    - Blocking: blocks the 07-14 play sitting artifact.

33. **fleet-manager — tick "Allow GitHub Actions to create and approve pull
    requests"** *(new 2026-07-11, P1 FRESHNESS; the last click that makes
    roster freshness fully autonomous).*
   - id: OQ-FM-ACTIONS-PR-PERMISSION
    - WHERE: https://github.com/menno420/fleet-manager/settings/actions →
      "Workflow permissions".
    - HOW: check the box "Allow GitHub Actions to create and approve pull
      requests" → Save. (If greyed out, flip the same toggle in the
      account-level Actions settings first.)
    - UNBLOCKS: the roster-regen cron (`40 */2 * * *`,
      `.github/workflows/roster-regen.yml`) landing `docs/roster.md`
      regenerations on its own — it already regenerates + pushes
      `bot/roster-regen` fine but cannot open the PR.
    - VERIFIED-NEEDED: attempted twice live 2026-07-11 (~19:17Z + ~19:23Z),
      walls verbatim — direct push: `GH013 … Changes must be made through a
      pull request.` (run 29164975251); PR path: `pull request create failed:
      GraphQL: GitHub Actions is not permitted to create or approve pull
      requests (createPullRequest)` (run 29165152964; the regen commit
      `a310a12` DID reach `bot/roster-regen`, so ONLY the PR-create
      permission is missing). Owner-only: repo/account settings surface, no
      API path for GITHUB_TOKEN.
    - Blocking: not-blocking (manager wakes still regen the roster; the
      freshness checker alarms at >4h), but this click removes the last
      manager-wake dependence — the whole point of P1.

### (C) Claude platform (console / environments / sessions / Codex)

14. **Re-paste the consolidated env setup scripts — COORDINATOR ENV FIRST.**
    *(Old item 17.)*
    - id: OQ-ENV-SETUP-REPASTE
    - WHERE: claude.ai/code → Environments → (each env) → Setup script field;
      environment-to-script map:
      [`../environments/archetypes.md`](../environments/archetypes.md).
    - HOW: coordinator (multi-repo) env FIRST —
      `environments/archetype-coordinator.sh` raw from main — then python-lab /
      pinned-research / bot-prod / gba-lab archetypes per the map. Script-text
      swap only; variables untouched.
    - UNBLOCKS: activates the superbot-next→python3.11 fix (PR #73) — inert
      until pasted; converges every env on the one maintained lineage.
    - VERIFIED-NEEDED: STILL NEEDED — platform-side, not agent-verifiable
      (console fields have no agent read/write surface); no resolution evidence
      anywhere in today's sweeps; the PR #73 fix is INERT until pasted.
    - Blocking: blocks CI-parity installs in the coordinator env.

15. **Paste wave — ⛔ SUPERSEDED 2026-07-11 (owner restructure directive,
    slice 3, fm PR #91): do NOT run this wave as written.** *(Was: HOLD
    LIFTED / click-ready after PR #77, merge `39b888a`.)*
    - id: OQ-PASTE-WAVE
    - **Supersession note (2026-07-11, restructure directive):** the same-day
      8-seat restructure (fm PRs #88/#89/#91, stacked) replaced the per-repo
      Project layout this wave targets — the per-repo v2/v3 bodies below are
      superseded by the 8 seat bodies, and the websites sub-step's "v2 wake
      prompt" is stale (`projects/websites/coordinator-prompt.md` is **v3**
      since slice 2). Live successors: **C#34 (OQ-RESTRUCTURE-PROJECTS)** +
      **C#35 (OQ-RESTRUCTURE-INSTRUCTIONS-PASTE)** + **C#36
      (OQ-RESTRUCTURE-TRIGGER-CUTOVER)**. Body below kept verbatim for
      history/audit (the wave was click-ready when written; zero of its
      pastes have a receipt, so nothing owner-side needs undoing).
    - WHAT (in this order, one sitting, each paste = the FULL
      `projects/<repo>/instructions.md` body from main after #77 lands —
      **v2 everywhere, v3 for superbot-games; never v1**):
      1. **websites** — re-paste the v2 wake prompt
         (`projects/websites/coordinator-prompt.md`) into trigger
         `trig_017H9Qb9oxtLgUy6sw2gnSHg` AND paste
         `projects/websites/instructions.md` v2 into the Project's Custom
         Instructions (deployed text is pre-Q-0265 v1 — most drifted).
      2. **trading-strategy** — paste `instructions.md` v2 into its Project.
      3. **substrate-kit** — paste `instructions.md` v2 + OA8 setup-script
         field (`projects/substrate-kit/setup-script.sh`).
      4. **product-forge** — paste `instructions.md` v2.
      5. **sim-lab / idea-engine / fleet-manager / superbot-next** — paste
         each `instructions.md` v2 into its Project field (live seats operate
         equivalently; the paste closes the committed-vs-deployed gap).
      6. **superbot-games (v3) · superbot-idle (v2) · superbot-mineverse
         (v2)** — paste if/where those Projects carry Custom Instructions
         (idle/games have no paste receipt yet — first paste creates it).
      7. **superbot (optional)** — only if the owner hosts superbot sessions
         in a Project with an empty field (`.claude/CLAUDE.md` auto-loads
         in-repo).
      Registry: [`projects/README.md`](../projects/README.md) § Paste wave.
    - WHERE: console Custom-Instructions fields + the one websites trigger
      prompt (no agent write surface — verified walls).
    - HOW: paste top to bottom in one sitting from main (the re-issued bodies
      landed with #77); each body carries its own `vN` header — drift check =
      ask the seat to quote it.
    - UNBLOCKS: every live seat running on the corrected merge clause +
      permissions block; ends the walled-instruction class fleet-wide.
    - VERIFIED 2026-07-11 (P3 curation sweep, live PR state): **PR #77 is
      MERGED** (menno420, 2026-07-11T18:40:12Z, merge `39b888a`) — the hold is
      lifted and the re-issued v2/v3 bodies are on main. (Trail: the old
      HELD-on-#47 rider was already obsolete — the §2.4 payload landed via
      PR #76, owner-merged `e1848ff`; #47 merged 14:55Z, `5625e3b`,
      intent-signal-only.)
    - Blocking: nothing holds it — click-ready.

16. **superbot-next OA-5 — export real `ANTHROPIC_API_KEY` +
    `AI_ENABLED=true` into the builder session environment.**
    - id: OQ-NEXT-API-KEY
    - WHERE: the same env-var surface where `DISCORD_BOT_TOKEN_PRODUCTION`
      lives (the builder session environment — NOT GitHub secrets/CI); config
      seam `sb/spec/config.py:166` + `:148`.
    - HOW: add the two variables to the builder env.
    - UNBLOCKS: band-7 live-NL evidence (deterministic surfaces already
      shipped, #151).
    - VERIFIED-NEEDED: status@`168ef80` line 20(c) + band-7 wrap-up 12:45Z
      today ("live-NL leg owner-key-gated"). API keys are owner-only.
    - Blocking: blocks band-7's live-NL leg only.

17. **superbot-mineverse — provision six host env vars.**
    - id: OQ-MINEVERSE-ENV-VARS
    - WHAT: `DISCORD_OAUTH_CLIENT_ID`, `DISCORD_OAUTH_CLIENT_SECRET`,
      `OAUTH_REDIRECT_URI`, `WEB_SESSION_SIGNING_KEY`, `MINING_WRITE_ENDPOINT`,
      `MINING_WRITE_SHARED_SECRET`.
    - WHERE: host runtime env + Discord Developer Portal (not CI).
    - HOW: create the Discord OAuth app values in the Developer Portal; set all
      six in the host runtime. The site runs degraded read-only meanwhile (130
      tests pass with zero vars).
    - UNBLOCKS: player sign-in; with the write pair + bot-lane FLAG 2,
      test-guild write mode.
    - VERIFIED-NEEDED: control/status.md@`4be012e` ⚑ OWNER-ACTION 1.
      Credentials are owner-only.
    - Blocking: blocks player sign-in only; site otherwise functional.

18. **superbot-plugin-hello — say the seed-push word (LIVE OWNER WORD, not a
    click).**
    - id: OQ-PLUGIN-SEED-WORD
    - WHAT: the repo exists but is EMPTY; the ask is to say **"push the plugin
      seed"** in a session — the classifier requires a live owner word for
      cross-repo publication.
    - WHERE: any live session; seed staged at superbot-next
      `examples/superbot-plugin-hello/` @`168ef80`; contract: superbot
      `docs/owner/product-catalog.md` §10 @`9f46cb7`.
    - HOW: one line in a session you're present in.
    - UNBLOCKS: superbot-idle PLUG-001 (lane HOLD) + the plugin-contract
      end-to-end proof.
    - VERIFIED-NEEDED: re-verified today — Contents API returns verbatim
      `409 Git Repository is empty`. *(Split out of old item 14.)*
    - Blocking: blocks idle PLUG-001.

19. **trading-strategy — archive the dead gen-1 "ORDER 001 successor"
    session.**
    - id: OQ-TRADING-ARCHIVE-SESSION
    - WHERE: claude.ai → project session list.
    - HOW: archive the session (died at provision, still lists as active).
    - UNBLOCKS: nothing — hygiene; consumes nothing.
    - VERIFIED-NEEDED: status@`3172b43` ⚑(d).
    - Blocking: cosmetic.

20. **Codex — CHANGED: pool is FLAPPING, not hard-capped; usage raise now
    OPTIONAL.**
    - id: OQ-CODEX-FLAPPING
    - WHAT: the "Codex hard usage-cap" claim is retired — usage-limit replies
      at 05:08Z today, then FULL substantive reviews on superbot-next #154
      (05:54Z) and #157 (06:31Z).
    - WHERE (optional): chatgpt.com/codex → usage/limits.
    - HOW: raise limits only if you want fewer flaps — it is a mitigation, not
      an outage fix.
    - UNBLOCKS: steadier @codex review throughput.
    - VERIFIED-NEEDED: status@`168ef80` FLAP UPDATE (today).
    - Blocking: not-blocking.
    - **Manager note (agent-fixable, routed to the superbot lane — NOT an owner
      click):** superbot's `codex-final-review` workflow has had invalid YAML
      since 2026-06-19 — 0 successful runs of 2,811; latest run 29156086075
      instant-fails at parse.

34. **Fleet restructure — create/rename the claude.ai Projects to the 8
    standing seats** *(new 2026-07-11, owner restructure directive — slice 3,
    fm PR #91; Projects are the restructure's one hard owner-only wall).*
   - id: OQ-RESTRUCTURE-PROJECTS
    - **Note (2026-07-12, prompts v3.2 — owner correction): the startup
      prompts these Projects get are now STATELESS** — no PR numbers, CI
      colors, trigger ids, or "do X now" items are baked into any paste;
      current work always comes from each repo's `control/inbox.md` + state
      docs (the WORK SOURCES ladder). Whenever this restructure runs, paste
      the **v3.2** bodies from `docs/prompts/v3/per-project/` — being
      stateless, they need no re-cut before the sitting the way dated
      v3.0/v3.1 drafts did.
    - WHAT: end state = exactly 8 standing Projects — **Venture Lab ·
      SuperBot World · Game Lab · Ideas Lab · Self Improvement ·
      SuperBot 2.0 · Websites · Fleet Manager**. Recommended click path
      (rename the strongest predecessor so its Project knowledge survives;
      archive the rest):
      1. RENAME the venture-lab Project → **Venture Lab** (absorbs
         trading-strategy, research-only) · archive the trading-strategy
         Project.
      2. RENAME the superbot-mineverse Project → **SuperBot World**
         (flagship = mineverse) · archive the superbot-games +
         superbot-idle Projects.
      3. RENAME the retro-games coordinator Project → **Game Lab** (it
         already drives gba-homebrew + pokemon-mod-lab) · archive any
         separate gba/pokemon Projects.
      4. RENAME the idea-engine Project → **Ideas Lab** · archive the
         sim-lab Project.
      5. RENAME the substrate-kit Project → **Self Improvement**.
      6. RENAME the superbot-next Project → **SuperBot 2.0** (the superbot
         hub Project keeps its Q-0264 owner-session character inside the
         merged seat — archive it only if you never start superbot sessions
         from it).
      7. KEEP **Websites** and the fleet-manager Project (→ **Fleet
         Manager**) as-is.
      8. Archive any leftover shells: codetool-lab ×3 (already closed) ·
         mobile-lab / games-program if shells exist (pre-birth) ·
         product-forge awaits E#37.
      (Equivalent alternative: create the 6 new-name Projects fresh and
      archive all predecessors — same end state, more clicks.)
    - WHERE: claude.ai → Projects screen. Owner-side surface with NO agent
      read — this list is derived from committed paste receipts/metas;
      adjust to what the screen actually shows.
    - HOW: per Project: ⋯ menu → Rename (or New Project); archive the
      retired ones.
    - UNBLOCKS: C#35 + C#36 (pastes and cutovers land in these Projects) —
      the restructure's platform half.
    - VERIFIED-NEEDED: registry restructured on the stacked PRs #88 (seats)
      / #89 (prompts) / #91 (this queue) — merge order #88→#89→#91;
      Projects = standing owner-only wall (no agent surface, playbook
      platform-walls section).
    - Blocking: blocks the restructure's platform half; the repo/registry
      half is already parked on the stack.
    - **Prompts v3.1 note (re-stamped 2026-07-12 after prompts v3.1 (#103)):**
      when booting sessions in these Projects, the startup prompt to use per
      seat is `docs/prompts/v3/per-project/<seat>-startup.md` (generated from
      `docs/prompts/v3/universal-startup.md`, the fleet-wide startup
      artifact) and the shared ender is `docs/prompts/v3/session-ender.md`.

35. **Fleet restructure — paste each seat's instructions body into its
    Project's Custom Instructions** *(new 2026-07-11, restructure directive —
    slice 3, fm PR #91; supersedes C#15's per-repo wave).*
   - id: OQ-RESTRUCTURE-INSTRUCTIONS-PASTE
    - WHAT: after C#34, paste the FULL body of each registry file below
      (source = the restructure stack, branch `claude/restructure-roster`
      until it merges, then the same paths on main; every body fits the
      verified 8,000-char console cap):
      1. Venture Lab ← `projects/venture-lab/instructions.md` (v3 · 7,498)
      2. SuperBot World ← `projects/superbot-world/instructions.md` (v1 · 7,489)
      3. Game Lab ← `projects/game-lab/instructions.md` (v1 · 7,481)
      4. Ideas Lab ← `projects/ideas-lab/instructions.md` (v1 · 7,494)
      5. Self Improvement ← `projects/self-improvement/instructions.md` (v1 · 7,486)
      6. SuperBot 2.0 ← `projects/superbot-2.0/instructions.md` (v1 · 7,499)
      7. Websites ← `projects/websites/instructions.md` (v2 · 7,470 — carried
         over from #77; still no paste receipt, so the paste is still owed)
      8. Fleet Manager ← `projects/fleet-manager/instructions.md` (v3 ·
         7,763 — needed on seat re-boot; the successor boot flow covers it)
    - WHERE: each Project → Custom Instructions field (owner-only console
      surface, verified wall).
    - HOW: open the raw file → select all → paste. Drift check afterwards:
      ask the seat to quote its in-paste first line
      (`vN · 2026-07-11 · <seat> instructions`).
    - UNBLOCKS: every standing seat running on the 8-seat doctrine text that
      survives chat archives.
    - VERIFIED-NEEDED: version headers + byte counts verified on the stack
      2026-07-11 (slice 3); Custom-Instructions fields are a verified
      owner-only wall (registry doctrine, projects/README.md §3).
    - Blocking: do it in the same sitting as C#34 — a renamed Project still
      carrying old per-repo instructions is live drift.
    - **Re-stamp note (re-stamped 2026-07-12 after prompts v3.1 (#103)):** the
      `projects/<seat>/instructions.md` bodies + counts above are SUPERSEDED
      as paste sources — the canonical Custom-Instructions paste per seat is
      now the v3.1 ASSEMBLED CI: the filled universal core
      (`docs/prompts/v3/custom-instructions-core.md`, paste order per that
      file) + the seat block from
      `docs/prompts/v3/per-project/<seat>-custom-instructions.md`. Counts
      re-verified on disk 2026-07-12 (seat-block paste bodies re-measured,
      match every in-file claim exactly; assembled-filled = filled core +
      block per each file's assembly-accounting header, arithmetic verified;
      all ≤ 7,998 < the 8,000 hard cap — budget table:
      `docs/prompts/v3/per-project/README.md`):
      1. Venture Lab ← `venture-lab-custom-instructions.md` (block 990 ·
         assembled filled 7,998; file 2,165 bytes by `wc -c`)
      2. SuperBot World ← `superbot-world-custom-instructions.md` (block 966 ·
         assembled filled 7,997; file 2,133 bytes by `wc -c`)
      3. Game Lab ← `game-lab-custom-instructions.md` (block 971 · assembled
         filled 7,984; file 2,122 bytes by `wc -c`)
      4. Ideas Lab ← `ideas-lab-custom-instructions.md` (block 980 ·
         assembled filled 7,992; file 2,115 bytes by `wc -c`)
      5. Self Improvement ← `self-improvement-custom-instructions.md`
         (block 992 · assembled filled 7,992; file 2,158 bytes by `wc -c`)
      6. SuperBot 2.0 ← `superbot-custom-instructions.md` (block 984 ·
         assembled filled 7,994; file 2,146 bytes by `wc -c`)
      7. Websites ← `websites-custom-instructions.md` (block 951 · assembled
         filled 7,943; file 2,106 bytes by `wc -c`)
      8. Fleet Manager ← `fleet-manager-custom-instructions.md` (block 975 ·
         assembled filled 7,972; file 2,093 bytes by `wc -c`)
      (All 8 under `docs/prompts/v3/per-project/`.) Drift-check first line is
      now `v3.1 · 2026-07-12 · <seat> instructions` (v3.1 core), not the
      2026-07-11 stamp above.

36. **Fleet restructure — boot each new seat (one coordinator-prompt paste
    per Project); the boot retires the old triggers and arms the new
    failsafe** *(new 2026-07-11, restructure directive — slice 3, fm PR #91).*
   - id: OQ-RESTRUCTURE-TRIGGER-CUTOVER
    - WHAT: cutovers are agent-side by design (rebind-then-delete, BOOT
      step 2 of each `projects/<seat>/coordinator-prompt.md`; the verbatim
      create_trigger block + old-trigger list lives in each seat's
      `projects/<seat>/failsafe-prompt.md`). Your click = paste each seat's
      `coordinator-prompt.md` as the FIRST message of a new chat in that
      Project. The boot then creates the new failsafe, verifies via
      list_triggers, deletes the old triggers, verifies them absent, and
      records every call verbatim in the seat heartbeat. Old triggers that
      go (last committed registry state — each boot re-verifies live first):
      - **SuperBot World** (arms `superbot-world failsafe wake` ·
        `20 */2 * * *`): retires games `trig_019ZgWyL78Rx1sr6LhvL8NE3`
        (`15 */2`) · idle `trig_01TWKGFW8RUsMvxUMt2ndzqA` (`45 */2`) ·
        mineverse `trig_01K8xmAKYS5S2HLy1HPANM7j` (`20 */2`).
      - **Game Lab** (arms `game-lab failsafe wake` · `50 */2 * * *`):
        retires the retro failsafe `trig_01Y99uDKNtKTz2EtRYPWZkGY`
        (`50 */2`) + BOTH hourly child wakes — gba
        `trig_0137SkvhXEJvwepX8aVNkcSn` (`0 * * * *`) · pokemon
        `trig_01BTJjkMVMKtWPjuYe7643Hi` (`30 * * * *`).
      - **Ideas Lab** (arms `ideas-lab failsafe wake` · `0 */2 * * *`):
        retires idea-engine `trig_0178q9Je2xRFJgthwamrg9Br` (`0 */2`) +
        sim-lab `trig_01SHfnLv6EqZesr4tC3T9kUU` (`0 1-23/2`).
      - **Self Improvement** (arms `self-improvement failsafe wake` ·
        `0 */2 * * *`): retires the old pre-Q-0265 standing wake
        `trig_016EfUawz6KxEYqUM6f1BqDw`.
      - **SuperBot 2.0** (arms `superbot-2.0 failsafe wake` ·
        `0 */2 * * *`): retires the Builder failsafe
        `trig_01L5JBefGSCM1fUdwm4SRQnY`; superbot hub triggers are
        explicitly left alone.
      - **Venture Lab** (arms `venture-lab failsafe wake` · `0 */2 * * *`):
        retires the trading-strategy failsafe
        `trig_01YBaVeKAW2fSD83S9F37s2d` (`0 */2`).
      - **Websites** — NO cutover (keeps `trig_017H9Qb9oxtLgUy6sw2gnSHg`,
        `0 */4 * * *`); owed instead: re-paste
        `projects/websites/coordinator-prompt.md` (now **v3**) into that
        trigger's prompt on the Routines screen.
      - **Fleet Manager** — unchanged by the restructure: the successor
        coordinator rebinds-then-deletes `trig_01F9UdoUtLy8oknBPBkHLshS`
        per `projects/fleet-manager/reboot-prompt.md` v2 (F-1).
    - WHERE: each new Project (chat paste, first message); plus the one
      websites trigger prompt on the Routines screen.
    - HOW: one paste per seat, same sitting as C#34+C#35. If a seat's
      surface walls the trigger calls, its boot records the verbatim denial
      and hands you the create_trigger block (name + cron + prompt) from its
      failsafe-prompt.md.
    - UNBLOCKS: the 8-seat wake fabric; retires 9 armed triggers that
      otherwise keep waking archived/retired seats every wake slot.
    - VERIFIED-NEEDED: trigger ids/crons quoted from the slice-2 prompt
      files at the stack head (committed registry state with extraction
      receipts in each failsafe-prompt.md provenance block); every boot
      re-verifies live via list_triggers before deleting anything.
    - Blocking: until cutover, the old failsafes fire into archived seats
      on every slot (silent-fire class).
    - **Prompts v3.1 note (re-stamped 2026-07-12 after prompts v3.1 (#103)):**
      for the boot pastes, the startup prompt to use per seat is
      `docs/prompts/v3/per-project/<seat>-startup.md` (generated from
      `docs/prompts/v3/universal-startup.md`, the fleet-wide startup
      artifact) and the shared ender is `docs/prompts/v3/session-ender.md`.

### (D) External services

21. **venture-lab ⚑A — Stripe TEST keys.**
    - id: OQ-VENTURE-STRIPE-KEYS
    - WHERE: Stripe Dashboard (test mode) → Developers → API keys / Webhooks.
    - HOW: paste `sk_test_…` as `STRIPE_SECRET_KEY` + `whsec_…` as
      `STRIPE_WEBHOOK_SECRET` into `candidates/membership-kit/server/.env`
      (never committed; no CI job reads these — local owner action).
      Verified-when: `python3 app.py` prints `mode=stripe`; `stripe trigger
      checkout.session.completed` grants membership → `/members` 200.
    - UNBLOCKS: the only unverified leg of the payment path for all 3 products.
    - VERIFIED-NEEDED: status@`a447f1a` ⚑A ("live E2E NEVER executed").
      Payment accounts/keys are owner-only (hard rail).
    - Blocking: blocks payment-path E2E verification.

22. **venture-lab — the publish clicks (⚑B/⚑D/⚑E, all gates met).**
    - id: OQ-VENTURE-PUBLISH-CLICKS
    - WHAT: publish **membership-kit $49** (`dist/membership-kit-v0.2.zip`,
      script `docs/launch/membership-kit/owner-actions.md`) ·
      **template-packs $19 PWYW** (`dist/template-packs-v0.1.zip`) ·
      **stripe-webhook-test-kit $29** (`dist/stripe-webhook-test-kit-v0.1.zip`,
      sha256 `d3ac5f88…eeb0d8`, script
      `docs/launch/stripe-webhook-test-kit/publish-owner-action.md`).
    - WHERE: gumroad.com → New product (or Lemon Squeezy).
    - HOW: per-product listing paste + zip upload + Publish (scripts above are
      click-level).
    - UNBLOCKS: the first-revenue path.
    - VERIFIED-NEEDED: status@`a447f1a` line 12 "launch-ready ×3 … owner-gated";
      revenue $0. Marketplace accounts are owner-only (hard rail).
    - Blocking: blocks all revenue.

23. **venture-lab — publish the gotcha article.**
    - id: OQ-VENTURE-GOTCHA-ARTICLE
    - WHAT: publish `docs/launch/stripe-webhook-test-kit/gotcha-article.md`
      ("Your Stripe webhook says customer_email is null — here's why").
    - WHERE: Dev.to / Hashnode (funnel: `docs/launch/distribution-channels.md`).
    - HOW: paste + publish.
    - UNBLOCKS: starts the test-kit 14-day validation clock, on which
      candidates #4/#5 wait.
    - VERIFIED-NEEDED: external publish is owner-only (hard rail).
    - Blocking: blocks the validation clock.

24. **websites — Railway Postgres.**
    - id: OQ-WEBSITES-RAILWAY-POSTGRES
    - WHERE: railway.app → project superbot-websites → New → Database →
      PostgreSQL.
    - HOW: copy `DATABASE_URL` into service **botsite** → Variables.
    - UNBLOCKS: public `/submit` intake.
    - VERIFIED-NEEDED: status@`52381a9` ⚑ + `self-review-2026-07-11.md:95-101`;
      agent-side is policy-walled (websites decision ledger, the
      no-agent-provisioning rule).
    - Blocking: blocks /submit.

25. **websites — fine-grained PAT.**
    - id: OQ-WEBSITES-PAT
    - WHERE: create at https://github.com/settings/personal-access-tokens
      (menno420 repos; contents+actions read; actions:write) → paste as
      `GITHUB_TOKEN` on railway.app → superbot-websites → **control-plane** →
      Variables (`docs/deployment.md` § owner TODO).
    - HOW: two clicks (create, paste).
    - UNBLOCKS: 5000 req/h for all fleet surfaces (now anonymous 60/h), board
      cells, /owner CI re-run.
    - VERIFIED-NEEDED: STILL unset — current-state.md@`52381a9`:109-110
      corrected an earlier false "set" claim. Tokens are owner-only.
    - Blocking: not-blocking, but rate-limits every fleet surface.

26. **product-forge OA-003 — enable GitHub Pages.** *(Old item 15.)*
    - id: OQ-FORGE-PAGES
    - WHERE: https://github.com/menno420/product-forge/settings/pages
    - HOW: Source: **GitHub Actions**; then re-run the deploy-pages workflow.
    - UNBLOCKS: the games-web RPG at `menno420.github.io/product-forge/`.
    - VERIFIED-NEEDED: today — latest run 29128667052 (2026-07-10T22:46Z)
      FAILED with "Get Pages site failed … Not Found" — Pages was never
      enabled; only 2 runs exist. Repo Settings are owner-only.
    - Blocking: blocks the public games-web build.

27. **itch.io — Lumen Drift publish clicks (conditional).**
    - id: OQ-ITCH-LUMEN-PUBLISH
    - WHERE: itch.io → new project.
    - HOW: conditional on decision E#28(1); ride the 07-14 sitting together
      with B#12's Release.
    - UNBLOCKS: public playable distribution + the venture itch.io path.
    - VERIFIED-NEEDED: external publish is owner-only (hard rail).
    - Blocking: waits on E#28(1).

### (E) Decisions & veto windows (silence-deadlines explicit)

28. **THE 2026-07-14 BUNDLED SITTING — now FOUR decisions** (idea-engine
    control/status.md@`2e03391` ⚑ line 9; grew from three — decision 4 added
    this slice). Window ends **2026-07-14**.
    1. **Lumen Drift itch.io go/no-go** + the publish clicks (D#27, B#12).
    2. **pokemon playtest verdicts — NOTE: now SIX patches, not 4** (instant
       text PR#4 · auto-run invert-B PR#6 · HP-bar drain 3× PR#7 ·
       battle-message waits ×0.5 PR#7 · egg hatch 2×/3× patch#14/PR#21 ·
       fishing dot 2× patch#16/PR#23; patch#15 excluded; rider: the Match Call
       nag one-worder). 0/6 verdicted — docs/qol-patches.md@`f69ab95`:437
       "Feel verdict pending". *(Supersedes old item 3.)*
    3. **gba Track B concept pick** (Lumen-deepening / Clockwork Courier /
       Shoal — the gba heartbeat carries it). *(Supersedes old item 4 Track B.)*
    4. **post-EAP routine posture** — HARD deadline: decide **≤2026-07-13**;
       RECOMMENDED **Option A**.
    - id: OQ-SITTING-0714-DECISIONS

29. **games §5 late-veto — OPEN, objection-only, silence=proceed ALREADY
    OPERATING.** No calendar date; ORDER 015 inbox:420. The §5.3 name resolved
    by react-by-action (owner created superbot-idle 2026-07-11T00:15:40Z);
    points 1/2/4/5 stand accepted-by-boot, late veto open — re-verified today,
    no objection on record. **No click unless vetoing.** *(Split out of old
    item 14.)*
    - id: OQ-GAMES-S5-LATE-VETO

30. **ORDER 018 R6 mobile-lab — decided 2026-07-11** (PR #73;
    `environments/archetypes.md:104-115`): escape-hatch stays, no node-lab
    knob. Standard Q-0240 vetoable, **NO dated window — open indefinitely**;
    veto = strike the decision. No click unless vetoing.
    - id: OQ-R6-MOBILE-LAB-VETO

31. **trading OOS protocol — REFRAMED (was mislabeled a veto window): OPT-IN,
    flag-only, NEVER self-executes, NO silence=proceed.** If wanted: file an
    inbox ORDER authorizing a pre-registered post-2026 protocol draft; if not
    wanted, no click — dev-candidates stay dev-only indefinitely
    (status@`3172b43` ⚑(f)).
    - id: OQ-TRADING-OOS-OPTIN

32. **Standing objection-only notes (no click unless veto):** kit P4 daily
    loop self-armed (`trig_01MHwmBrA1bziEp49g6xqGt5`, cron `0 6 * * *`;
    veto = delete the Routine) · kit five releases cut agent-side ·
    superbot-next D-0064–D-0069 decide-and-flag.
    - id: OQ-STANDING-OBJECTION-NOTES

37. **product-forge disposition — not in the owner's 8-seat list: retire the
    seat / fold into Venture Lab / keep as a 9th seat** *(new 2026-07-11,
    restructure directive — slice 3, fm PR #91; structured choice — the seat
    stays as-is until you pick; this one does NOT proceed on silence).*
   - id: OQ-FORGE-DISPOSITION
    - WHAT — pick one:
      **A (recommended)** — retire the SEAT, keep the REPO parked: archive
      the product-forge Project; registry dir `projects/product-forge/` →
      pointer stub (manager executes). No trigger to disarm — roster gen #9
      records its wake state as NONE. The repo keeps its KEEP verdict
      (fleet-triage: real games-web, 22 PRs, "home to homeless projects");
      future forge work routes via owner-started sessions or a Venture Lab
      order. Fully reversible — the v2/v3 seat package stays in git history.
      **B** — fold into **Venture Lab** (same shape as trading-strategy's
      fold): forge becomes a Venture Lab work surface; registry dir merges;
      one more repo on that seat's plate.
      **C** — keep product-forge as an unlisted 9th standing seat (status
      quo; contradicts the 8-seat directive — say so explicitly if intended).
      Recommendation: **A** — matches the directive, loses nothing, cheapest
      to reverse.
    - WHERE: one word wherever the manager reads — `control/inbox.md` ORDER,
      a live session, or a comment on the restructure stack (fm #88/#89/#91);
      plus the Projects screen for the archive click if A.
    - HOW: say "product-forge: A" (or B/C); the manager executes the
      registry/roster half.
    - UNBLOCKS: closes the restructure's only open seat question; lets the
      projects/README.md MATRIX/paste-wave regen (named follow-up) render
      exactly 8 seats.
    - VERIFIED-NEEDED: slice-1 finding (fm PR #88): product-forge is a live
      seat with a current package but absent from the owner's 8-seat list;
      roster gen #9 row 2026-07-11: FRESH, wake NONE, phase "close-out /
      archived-ready".
    - Blocking: not-blocking (seat is dormant — no failsafe armed); blocks
      only the final MATRIX regen follow-up.

## Resolved 2026-07-11 (P3 curation sweep, ~20:1xZ — every state below re-verified LIVE per PR, Q-0120)

The whole (A) merge group plus the UNIVERSAL-clause trail item, all clicked by
the owner (merged_by menno420 in every case; states read live via the GitHub
API this sweep, not from reports):

- **OQ-GAMES-PR27-MERGE ✅** — superbot-games #27 MERGED 2026-07-11T14:56:05Z,
  merge `50f6774` (Q-0267 theme-readiness delta on main).
- **OQ-GAMES-PR32-MERGE ✅** — superbot-games #32 MERGED 2026-07-11T14:56:17Z,
  merge `f9c2f7a` (survival sim harness + Q-0087 bands in CI).
- **OQ-GAMES-PR38-MERGE ✅** — superbot-games #38 MERGED 2026-07-11T14:56:26Z,
  merge `2f1e7cd` (D&D story design; the story-game code lane is unblocked —
  the walking skeleton in fact already landed as games #48 → `b835f59`).
- **OQ-KIT-PR181-RATIFY ✅** — substrate-kit #181 MERGED (= ratified)
  2026-07-11T14:56:40Z, merge `f7aa633` (T5 re-scope v2; kit's own ledger
  recorded the ratification at `5d4978e`).
- **OQ-UNIVERSAL-MERGE-CLAUSE ✅** *(old items 16 → 13 — the HOT
  owner-provenance item)* — the corrected §2.4 merge-authority clause is LIVE:
  PR #76 MERGED by the owner 2026-07-11T15:26:47Z (merge `e1848ff`,
  UNIVERSAL.md v4 at both locations, cmp-verified during ORDER 017); ORDER 017
  executed fleet-wide via PR #77, MERGED by the owner 2026-07-11T18:40:12Z
  (merge `39b888a`). Trail: #47 merged 14:55:53Z (`5625e3b`,
  intent-signal-only); the §2.4 block was staged by #68 (merged 11:48:30Z,
  `c5e264f`). Successor ask: the paste wave (OQ-PASTE-WAVE) is now
  click-ready.

## Resolved 2026-07-11 (verified)

- **superbot-games #34 MERGED** 13:40:40Z (merge `5147a23`) and **#36 MERGED**
  13:40:50Z (merge `325c567`); **games ORDER-004 self-review LANDED** (games
  PR #47 → main `201f8dd`, 13:41:25Z). The "5 parked PRs" item is now the 3
  merge clicks at A#1–3.
- **pokemon-mod-lab PRIVATE confirmed stuck** (API `private: true` + lane R22
  re-verify 14:07:05Z @`f69ab95`).
- **kit P4 daily-loop half of old item 5 — self-armed agent-side** (kit
  self-review @`2aa7a51`); the P10 half is carried as B#10.
- **Codex hard-cap claim RETIRED → flapping** (evidence at C#20).
- **trading OOS "veto window" framing RETIRED → opt-in** (reframed at E#31).

## Parked (valid, no rush)

- **Account-wide visibility review** — all 13 repos public at the 2026-07-10
  night review; pokemon-mod-lab now private, the rest — including
  fleet-manager (this owner queue is on the open internet) — remain public.
  Decide per-repo public/private; pairs with the §4.9 repo-settings sweep.
- **superbot-next grants** — intents toggles · sacrificial Discord account ·
  capped API key (band 7); folds into the band flow (superbot-next
  `control/status.md` ⚑). *(The API-key half is now the active C#16.)*
- **websites product questions** — domains · /submit Postgres (now active
  D#24) · /admin OAuth+home · restyle · cutover (websites
  `docs/owner/OWNER-ACTIONS.md`, each with a recommended default).
- **Anthropic email pack** — review + send before the 2026-07-14 window close;
  include the four routines platform bugs (runs not inspectable · Runs-panel
  vs Routines-screen disagreement · arming seat-inconsistency · model
  attribution inconsistent across surfaces; evidence: `capabilities.md`
  § routine self-arm rider).
- **PyPI trusted-publishing registration** (~2 min) — token-less kit releases.
- **codetool-lab-fable5 (envdrift) v0.1.0 + v0.2.0 tags + Releases** —
  tag-push 403; owner click at Releases → Draft: v0.1.0 @ `73ef38d`, v0.2.0 @
  `13a84e5`. (Provenance of the earlier opus4.8 mislabel correction:
  `projects/codetool-lab-{fable5,opus4.8}/meta.md`; opus4.8's mdverify
  Releases are LIVE.)
- **codetool archive toggles ×3 (paired DECISION)** — all three repos
  `"archived": false` (API-verified 2026-07-10); recommendation: **wait until
  the gen-3 succession question settles, then archive** (archiving makes the
  repos read-only).
- **cfgdiff v0.1.1 release — two clicks (codetool-lab-sonnet5):** (1) PyPI
  pending publisher (owner `menno420`, repo `codetool-lab-sonnet5`, workflow
  `release.yml`, environment `pypi`); (2) `git tag -a v0.1.1 0b1eb60 && git
  push origin v0.1.1` — do NOT tag v0.1.0 at `0260aae` (predates release.yml).
  Tag push is a credential-layer 403 on that seat.
- **Paper-doll PNG pack for mining** — art asset, whenever.

### Safe to delete / archive (housekeeping, consolidated 2026-07-10 · 18:31Z wake)

Everything here is verified spent — deleting/archiving loses nothing (all
state is committed in the repos). Do in one sitting whenever convenient.

- **Spent chats (archive in claude.ai):** OLD kit-lab coordinator chat
  (cutover VERIFIED — old trigger deleted, fresh seat live) · dead trading
  gen-1 "ORDER 001 successor" session (= C#19) · wound-down gen-1 lane chats
  generally (succession packages on main; chat context spent by design).
- **Stale branches (agent branch-delete is a verified 403):** codetool ×2 —
  `claude/status-heartbeat-001` (opus4.8), `test/push-check` (sonnet5) ·
  superbot-games ×2 — `mining/adopt-substrate-kit` (closed-unmerged-deliberate)
  and `mining/grid-encounters` (**verify tip is merged before deleting**) ·
  websites ×4 (= B#11).
- **NOT yet safe:** codetool repo archive toggles ×3 (paired decision above);
  anything holding an open READY PR.

## Resolved 2026-07-11 (earlier — ORDER 010 relay slice)

- **Item 0 (Idea Engine Project):** seat heartbeat/repo trace landed —
  idea-engine `control/status.md` @ `835b260`, phase STEADY; roster gen #4 row
  (fm PR #59, merge `b0639a9`): failsafe `0 */2` armed, chain HOT. Retired per
  the item's own retire condition.
- **Item 9 (product-forge repo + Project), halves 1+2 — overtaken by events:**
  repo exists with the deploy workflow on main (forge PR #13, HEAD `6f5cfad`);
  seat booted and heartbeating (`control/status.md` @ `77f5231`, continuous
  mode + failsafe `0 */2`). Residue: the settings sub-click (now B#9) and
  Pages (now D#26).
- **sim-lab OA-002 (Codex integration):** Codex environments exist for ALL 12
  active fleet repos (owner update 2026-07-11 ~00:2xZ, inbox ORDER 014). Quota
  refusals are RETRY-LATER, never a wall.
- **fleet-manager Codex env ask (PR #26):** resolved by the same fleet-wide
  enablement; @codex now PRIMARY on this repo's review-queue rows.
- **Games mapping item 14, Seat B repo-creation click — DONE:**
  `menno420/superbot-idle` exists (public, seeded, pushed
  2026-07-11T00:15:40Z) — the react-by-action on the §5.3 name; remaining veto
  window is E#29.

## Resolved 2026-07-10 (later additions)

- **trading-strategy PR #37 (final P5 holdout report) — MERGED by the owner
  2026-07-10T20:56:34Z** (merged_by menno420, API-verified). Program terminal
  state is ON MAIN: holdout SPENT, report FINAL, 0/13 clears significance.

## Resolved 2026-07-10 (Q-0262 owner-rulings batch, reconciled by the 18:31Z wake)

The owner answered the round-3 decision sheet wholesale (superbot router
Q-0262; routed as inbox ORDER 008 + lane orders):

- **kit F-5 ruling = Reading A** (Q-0262.1) — kit ORDER 011, executed (kit
  #127/#128; headline 1 PASS / 3 FAIL; B1 run-5 unblocked).
- **trading P5 holdout unlock = GRANTED** (Q-0262.2) — trading ORDER 008
  @ `fd5e9fe`; executed; terminal report merged (see above).
- **superbot-next flag-13 disposition = ACCEPTED** (Q-0262.3) — next ORDER
  009, applied in next #105.
- **Core seat 6 = the superbot hub Project** (policy 4) — owner may veto.
- **pokemon concept = QoL+** (Q-0262.7) — effective when the games program
  boots post-core (it since booted; QoL+ is the live concept).
- **The 8 undeployed instruction packages stay undeployed** until the gen-3
  blueprint delta lands, then re-base + deploy in one sitting (policy 3 —
  doctrine at blueprint §4; the deploy sitting is now C#15, held on B#13).
- Fleet policies folded into doctrine same day (fm PR #33): family-level model
  names ONLY (blueprint §1); kit OWNER-ACTION grammar wins by definition
  (playbook R17 rider).

## Resolved since the last rewrite (2026-07-09 → 2026-07-10 morning)

- **🚨→✅ pokemon-mod-lab flipped to PRIVATE** (URGENT item, night-review Q16)
  — done by the owner, re-verified via API; the account-wide visibility review
  moved to Parked.
- Fleet environments created — gen-2 lanes booted in them overnight.
- venture-lab + game-lab launch click-lists executed; gen-1 wind-down pasted
  and completed fleet-wide.
- Merge session done: kit #26 + #49 MERGED ~00:10Z, games #5 MERGED 00:00:58Z.
- Gen-1 wind-down prompt, external ChatGPT campaign, and Anthropic-email items
  consolidated (campaign closed with gen-1; email pack parked above).
