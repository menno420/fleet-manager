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
     (pokemon-mod-lab `docs/PLATFORM-LIMITS.md` @ `759dee4` — no such file
     exists in fleet-manager; repo-qualified 2026-07-14, INC-11).
   - Blocking: not-blocking, but a live gate hole.

6. **✅ RESOLVED (owner clicked 2026-07-11; swept 2026-07-14, Slice 0 item 6 /
   INC-06) — superbot-mineverse `pytest` IS a required check.**
   - id: OQ-MINEVERSE-PYTEST-REQUIRED-CHECK
   - Evidence: enabler rules probe verbatim `required contexts (2):
     ["substrate-gate","pytest"]` (Actions run 29260140367); re-confirmed
     live 2026-07-14 (mineverse notes §5.1/§11). The 07-11 gate hole
     (PR #30 merged 40 s before pytest finished) is closed.

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
   gate — ⛔ mooted by the consolidation archive path (see note).**
   - id: OQ-FORGE-SETTINGS-RESIDUE
   - **Reconciliation note (2026-07-12, consolidation plan):** the plan
     verdicts product-forge MIGRATE-THEN-ARCHIVE (Phase 1 rehomes → the B#40
     archive click, OQ-CONSOLIDATION-ARCHIVE-FORGE) — an archived repo needs
     no auto-merge/required-check settings. **Skip these clicks** unless the
     archive path is vetoed at E#44; body kept verbatim below for audit.
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

33. **✅ RESOLVED 2026-07-12 — fleet-manager Actions PR-permission toggle
    CLICKED by the owner and LIVE-VERIFIED.**
   - id: OQ-FM-ACTIONS-PR-PERMISSION
    - Evidence: dispatch run 29202721367 (2026-07-12 17:49Z) SUCCESS
      end-to-end, and the workflow **self-landed roster Generations #17 and
      #18** (PRs #129 + #131, opened AND squash-merged by the workflow
      itself). The stale-roster red-gate class is closed; roster freshness
      no longer depends on any wake.
    - The 2026-07-12 bridge routine (`trig_011LrFY1k5cUHRYH6zwTvPvn`) was
      deleted the same hour by the owner-live session — no self-retirement
      wait needed. (History: the toggle was walled from every agent venue —
      the proxy blocks all `/actions/*` admin paths — which is why the
      bridge existed at all; full trail in this file's git history.)

40. **Consolidation Phase 3.1 — archive product-forge (AFTER the Phase 1
    migrations land)** *(new 2026-07-12, consolidation plan:
    [`planning/2026-07-12-repo-consolidation-plan.md`](planning/2026-07-12-repo-consolidation-plan.md)
    § 3.1).*
   - id: OQ-CONSOLIDATION-ARCHIVE-FORGE
    - WHAT: GitHub archive toggle (read-only, reversible — nothing deleted).
    - WHERE: https://github.com/menno420/product-forge → Settings → Danger
      Zone → "Archive this repository".
    - HOW: one click — **gated on the plan's ORDERs P1-1/P1-2/P1-3** (rehome
      games-web, the data-API proposal, the retro) landing first, and on the
      E#44 gate letter (OQ-CONSOLIDATION-DELETE-VS-ARCHIVE).
    - UNBLOCKS: removes the repo from the kit re-render fan-out (it drew
      re-render PRs for nothing on 2026-07-12); first slice of 19 → 16.
    - VERIFIED-NEEDED: plan § 3.1 — heartbeat frozen 2026-07-11T19:39:50Z; no
      armed trigger references it (832-record trigger-map snapshot). Archive
      toggles are an owner-only settings wall.
    - RISK: ↩️ reversible — unarchive is the same settings toggle.
    - Blocking: not-blocking; sequenced after Phase 1.
    - Dedup: this click moots B#9 (OQ-FORGE-SETTINGS-RESIDUE) and D#26
      (OQ-FORGE-PAGES) — reconciliation notes added on those items.

41. **Consolidation Phase 3.2 — archive codetool-lab-sonnet5 (AFTER the
    Phase 1 migrations land)** *(new 2026-07-12, consolidation plan § 3.2).*
   - id: OQ-CONSOLIDATION-ARCHIVE-SONNET5
    - WHAT: GitHub archive toggle (read-only, reversible).
    - WHERE: https://github.com/menno420/codetool-lab-sonnet5 → Settings →
      Danger Zone.
    - HOW: one click — gated on ORDER P1-4 (port the two writeups to
      substrate-kit) **and your E#45 letter** (release first if A — archiving
      freezes the tag-push path forever).
    - UNBLOCKS: second consolidation slice; no trigger references the repo.
    - VERIFIED-NEEDED: census § sonnet5 — last commit `66c3dfc` 2026-07-09;
      zero tags on origin; owner ruling 2026-07-10 "archive … after harvest".
    - RISK: ↩️ reversible — unarchive toggle; the one thing archiving does
      freeze is tag-push, which is exactly why E#45 sequences first.
    - Blocking: not-blocking.

42. **Consolidation Phase 3.3 — archive codetool-lab-fable5 (AFTER the
    Phase 1 migrations land)** *(new 2026-07-12, consolidation plan § 3.3).*
   - id: OQ-CONSOLIDATION-ARCHIVE-FABLE5
    - WHAT: GitHub archive toggle (read-only, reversible).
    - WHERE: https://github.com/menno420/codetool-lab-fable5 → Settings →
      Danger Zone.
    - HOW: one click — gated on ORDER P1-5 (your named `.pyc`/`.gitignore`
      hygiene precondition) **and your E#46 letter**.
    - UNBLOCKS: third consolidation slice; no trigger references the repo.
    - VERIFIED-NEEDED: census § fable5 — `.pyc`/.gitignore defect verified @
      `a6cf1a9`; owner precondition on record.
    - RISK: ↩️ reversible — unarchive toggle.
    - Blocking: not-blocking.

43. **Consolidation Phase 3.4 — protect pokemon-mod-lab `main` (the fleet's
    only unprotected default branch)** *(new 2026-07-12, consolidation plan
    § 3.4).*
   - id: OQ-POKEMON-PROTECT-MAIN
    - WHAT: branch protection / a ruleset on `main` — `protected:false` today
      via `list_branches`; every other checked repo is protected or has
      documented required-check evidence.
    - WHERE: https://github.com/menno420/pokemon-mod-lab → Settings →
      Branches (or Rules → Rulesets).
    - HOW: add a ruleset matching what you set on websites 2026-07-09.
      **Dedup vs B#5 (OQ-POKEMON-ROM-REQUIRED-CHECK): distinct but paired** —
      B#5 adds the `ROM builds` required-check context INSIDE a main ruleset;
      this item creates the protection itself (the census read the
      classic-protection boolean as false; rule details are agent-unverifiable
      on this private repo, so whether a ruleset already exists can only be
      confirmed on your screen). Do both at the same sitting — creating or
      opening the ruleset here is the natural moment to add B#5's context.
    - UNBLOCKS: closes the fleet's one protection gap.
    - VERIFIED-NEEDED: plan § 3.4 + census § pokemon-mod-lab Methods note
      (boolean flag only). Rulesets are a verified owner-only wall
      (pokemon-mod-lab `docs/PLATFORM-LIMITS.md` @ `759dee4`; repo-qualified
      2026-07-14, INC-11).
    - RISK: ↩️ reversible — delete the ruleset to undo.
    - Blocking: not-blocking, but cheap and worth doing at the B#5 sitting.

49. **fleet-manager — roster read PAT for the one private lane repo**
    *(new 2026-07-13, consolidation batch).*
   - id: OQ-FM-ROSTER-READ-PAT
    - WHAT: create a fine-grained PAT (repository access: **pokemon-mod-lab
      only**, permission: Contents **read-only**) and save it as a
      fleet-manager Actions secret named `ROSTER_READ_TOKEN`.
    - WHERE: https://github.com/settings/personal-access-tokens/new
      (Settings → Developer settings → Fine-grained tokens), then
      https://github.com/menno420/fleet-manager/settings/secrets/actions
      (New repository secret → `ROSTER_READ_TOKEN`).
    - HOW: two clicksets, ~2 min total; the workflow wiring is already
      merged (fm PR #144) — the secret is the only missing piece.
    - WHY: headless roster regen cannot read the one private lane repo, so
      its row printed DEAD while the lane was alive.
    - UNBLOCKS: real pokemon-mod-lab roster rows (honest freshness instead
      of a false DEAD).
    - VERIFIED-NEEDED: next roster generation shows a real `updated:` stamp
      on the pokemon-mod-lab row.
    - RISK: ✅ read-only, single-repo token — minimal scope, revocable.
    - Blocking: not-blocking, but the row lies until clicked.

50. **✅ RESOLVED 2026-07-13 (wake-session live verification) — superbot-idle
    self-landing is WORKING; the two parked PRs landed automatically.**
   - id: OQ-IDLE-REQUIRED-CHECKS
    - Evidence (live GitHub, read 2026-07-13 ~13:20Z): idle **PR #76 MERGED
      2026-07-13T01:23:35Z** and **PR #75 (PLUG-001 adapter) MERGED
      2026-07-13T01:26:30Z**, both `merged_by: github-actions[bot]` — the
      item's UNBLOCKS ("parked idle PRs #75/#76 land automatically") is
      satisfied verbatim, and open idle PRs = 0. Caveat, honest: the merge
      record alone cannot distinguish native auto-merge (the Allow-auto-merge
      tick) from a `GITHUB_TOKEN` merge-on-green workflow — either way the
      self-landing path this item existed for is live. Body history in git.

51. **gba-homebrew — make "ROM builds" a required check via a RULESET on
    main** *(new 2026-07-13, consolidation batch — coordinator addition).*
   - id: OQ-GBA-ROM-RULESET
    - WHAT: make `ROM builds` a required status check via a **ruleset** on
      `main` (rulesets are token-readable; classic branch protection reads
      403 for GITHUB_TOKEN, so the enabler can only see ruleset-defined
      contexts).
    - WHERE: https://github.com/menno420/gba-homebrew → Settings → Rules →
      Rulesets → New branch ruleset → target `main` → Require status checks
      → add context `ROM builds` → Active.
    - HOW: ~1 min, one ruleset form.
    - WHY: the newly installed enabler (PR #76, merged 0e08695) sees ZERO
      token-readable required contexts and correctly refuses to arm until a
      ruleset exists.
    - UNBLOCKS: gba PRs self-land (including the parked slice PRs).
    - VERIFIED-NEEDED: the next `claude/*` PR on gba-homebrew shows
      "Auto-merge enabled" instead of the refuse-to-arm warning.
    - RISK: ✅ reversible — delete or deactivate the ruleset to undo.
    - Blocking: not-blocking, but holds the parked gba slice PRs.

54. **venture-lab — sandbox repo to production-verify merge-on-green.yml**
    *(new 2026-07-13, Q-0264 fan-in batch 2 — routed from venture-lab's
    morning tally; fm ORDER 044 routes the tally's seven sim asks, this is
    its one owner-gated ask.)*
   - id: OQ-VENTURE-SANDBOX-REPO
    - WHAT: create a tiny sandbox repo (or say one word approving venture
      creating one) so the seat can production-verify its
      `merge-on-green.yml` workflow before adopting it on the real lane
      repos.
    - WHERE: https://github.com/new (or a one-word approval in chat — the
      manager relays it).
    - HOW: ~1 min — name it anything (e.g. `venture-sandbox`), private,
      empty; or reply "sandbox: yes".
    - WHY: repo creation is an owner capability wall; venture asked for
      exactly this in its morning tally (venture-lab control/outbox.md
      "night-run MORNING TALLY" SIM-REQUEST line, ~05:00Z).
    - UNBLOCKS: venture's landing-path automation (self-landing PRs on
      green instead of the poll-and-merge workaround).
    - VERIFIED-NEEDED: sandbox repo exists + the venture heartbeat records
      the merge-on-green verification run.
    - RISK: ✅ reversible — a throwaway sandbox repo; delete it after the
      verification.
    - Blocking: not-blocking, but holds the lane's merge automation.

59. **Stale-branch delete batch — gba ×1 + pml ×3 (agent delete is
    403-walled).** *(new 2026-07-13, night-report roll-up — restated asks
    from the gba ORDER 006 + pml ORDER 008 night reports; joins the queued
    pml `claude/fm-r27-wake-repair` delete.)*
    - id: OQ-STALE-BRANCH-DELETES-0713
    - WHAT: delete stale remote branches — gba-homebrew:
      `claude/brineward-wind` (**AFTER #82 merges** — #82 carries its
      slice 6); pokemon-mod-lab: `track-a/session-019`,
      `track-a/session-024`, `claude/eloquent-newton-qaf1ii` (head of
      closed-not-merged PR #47).
    - WHERE: each repo's /branches page (or the PR pages' delete-branch
      buttons after the sweep).
    - HOW: ~1 min total — four delete clicks; sequence the gba one after
      the #82 merge.
    - UNBLOCKS: nothing — pure hygiene; prevents stale-base confusion for
      future agent sessions.
    - VERIFIED-NEEDED: gba PR #89 head `a84933b` outbox §4(c); pml PR #63
      head `db46649` status "Asks pending" item 2; branch deletion is a
      verified agent wall (gba-homebrew + pokemon-mod-lab, each repo's own
      `docs/PLATFORM-LIMITS.md`; repo-qualified 2026-07-14, INC-11).
    - Blocking: not-blocking.

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

17. **✅ RESOLVED 2026-07-12 — mineverse player sign-in LIVE, owner-verified
    end-to-end** (was: six host env vars → two portal steps → done).
    - id: OQ-MINEVERSE-ENV-VARS
    - FINAL: the owner registered the redirect URI (evening) and, after the
      UA-403 token-exchange fix (mineverse #45 — Cloudflare rejects urllib's
      default User-Agent; auto-deployed 18:22Z), **completed a full live
      sign-in** (~20:50 local, screenshot: "Signed in as 3404…6000" on
      web-production-97636). Sign-in requires nothing further from anyone.
    - Still open, AGENT-side only (superbot bot lane, specs verbatim in
      mineverse control/status.md): **FLAG 1** (60s snapshot relay → real
      miners replace the sample snapshot + the STALE banner clears) and
      **FLAG 2** (HMAC write endpoint → the write pair
      `MINING_WRITE_ENDPOINT`/`MINING_WRITE_SHARED_SECRET` gets provisioned
      and the action buttons go live, test-guild allowlisted).
    - History below kept for the record:
    - DONE agent-side 2026-07-12 (owner-live, owner-approved): the web host
      now EXISTS — Railway project `superbot-mineverse`, service `web`,
      domain `https://web-production-97636.up.railway.app`, start command
      `python3 server/app.py`, deployed read-only degraded (by design). THREE
      of the six vars are set: `WEB_SESSION_SIGNING_KEY` (fresh random),
      `OAUTH_REDIRECT_URI`
      (`https://web-production-97636.up.railway.app/auth/callback`),
      `DISCORD_OAUTH_CLIENT_ID` (the production Discord app's id).
    - UPDATE 2026-07-12 (same session, owner-decided): the client-secret half
      is DONE — the owner chose to **reuse the superbot-dashboard's Discord
      app** (id `1403818430758654132`; its id+secret copied from the
      `reliable-grace`/dashboard service, mineverse `web` redeployed,
      `/api/me` now reports `auth_configured: true`). Note: the sign-in
      consent screen shows the dashboard app's name/icon (rename in the
      portal if wanted — cosmetic only).
    - WHAT remains OWNER (Discord Developer Portal, ONE click):
      on app `1403818430758654132` → OAuth2 → Redirects, **add**
      `https://web-production-97636.up.railway.app/auth/callback` as a
      second redirect (the dashboard's existing one stays; must byte-equal
      the env var).
    - WHAT remains AGENT (not owner — do NOT park on the queue): the write
      pair `MINING_WRITE_ENDPOINT` + `MINING_WRITE_SHARED_SECRET` waits on
      superbot bot-lane **FLAG 2** (the HMAC write endpoint,
      mineverse control/status.md spec) — routed to the superbot lane.
    - UNBLOCKS: (owner half) player sign-in on the live host; (agent half)
      test-guild write mode.
    - VERIFIED-NEEDED: portal secrets are genuinely owner-only (no API path).
    - Blocking: blocks player sign-in only; the site is otherwise live.

18. **✅ RESOLVED (delivered 2026-07-12; swept 2026-07-14, Slice 0 item 6 /
    INC-01) — superbot-plugin-hello seed is PUSHED.**
    - id: OQ-PLUGIN-SEED-WORD
    - Evidence: the seed was delivered 2026-07-12T13:29Z (`bbaccec`, ORDER
      002/014 per superbot-next `control/status.md`); **live-re-verified
      2026-07-14** — Contents API returns a full tree at `bbaccec` (README,
      pyproject, `superbot_plugin_hello/`, `tests/`), no 409. The idle
      PLUG-001 HOLD reason is gone (adapter merged, idle #75/#78).
    - History: the ask was written against a genuinely-empty repo and went
      stale after the owner delivered — the exact expiry class
      `check_owner_queue.py` should learn to probe (INC-06 disposition).

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
    - **Manager note — ✅ the YAML half is RESOLVED (swept 2026-07-14, Slice 0
      item 6):** superbot's `codex-final-review` invalid-YAML (broken since
      2026-06-19, 0 successful runs of ~2,808) was fixed by **superbot PR
      #1995, MERGED 2026-07-11T15:18:41Z** (live-verified via the GitHub
      API). Only the flapping-quota half of this item remains.

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
         product-forge Project archives per the consolidation disposition
         (E#37 ⛔ superseded → B#40 + E#44, 2026-07-12).
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

60. **superbot-next — hermes egress credentials
    (`CLAUDE_ROUTINE_FIRE_URL` + token).** *(new 2026-07-13, night-report
    roll-up — from the ORDER 018 report's asks-pending + stall item 8.)*
    - id: OQ-NEXT-HERMES-EGRESS-CREDS
    - WHAT: provide the hermes egress pair — `CLAUDE_ROUTINE_FIRE_URL` +
      its token — to the superbot-next environment so the hermes probe
      stops failing `RuntimeError: missing_config`.
    - WHERE: the superbot-next session environment / env-var surface
      (console → environment settings), same surface as OA-5's
      `ANTHROPIC_API_KEY` (C#16 — bundle the two pastes in one sitting).
    - HOW: two env-var pastes.
    - UNBLOCKS: the hermes routine-fire egress path from that seat
      (currently hard-walled at config).
    - VERIFIED-NEEDED: superbot-next `control/outbox.md` ORDER 018 report
      (on main via #366 = `902791d`), STALLS item 8 verbatim + the
      asks-pending line.
    - Blocking: not-blocking — blocks only the hermes lane.

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
    - **Reconciliation note (2026-07-12, consolidation plan):** hold this
      click — product-forge is MIGRATE-THEN-ARCHIVE (B#40,
      OQ-CONSOLIDATION-ARCHIVE-FORGE), and the games-web build it would
      publish is rehoming under ORDER P1-1 (websites arcade or
      superbot-games); Pages on an archived repo serves nothing. Revisit only
      if the archive path is vetoed at E#44.
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

28. **THE 2026-07-14 BUNDLED SITTING — now FIVE decisions** (idea-engine
    control/status.md@`2e03391` ⚑ line 9; grew from three — decision 4 added
    the 07-11 slice, decision 5 added 2026-07-12 from the consolidation
    plan). Window ends **2026-07-14**.
    **Consolidation-plan note (2026-07-12):** this sitting IS the plan's
    ⏰ TIME-CRITICAL bundle
    ([`planning/2026-07-12-repo-consolidation-plan.md`](planning/2026-07-12-repo-consolidation-plan.md)
    § "⏰ TIME-CRITICAL bundle") — its 5a–5d map to decisions 1–4 below
    (recommendations restated there); 5e is decision 5, new. The plan asks
    for the whole bundle **≤2026-07-13, one sitting** (the EAP window ends
    2026-07-14) — decision 4's hard deadline now covers all five.
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
       RECOMMENDED **Option A** (plan 5d restates: keep the 2-hourly
       failsafes, retire EAP-specific pacemakers — failsafes are cheap; the
       burn is in repo crons, see E#47/E#48).
    5. **websites cutover Options A–D** — retire superbot `dashboard/` +
       `botsite/` in favor of the Railway replacements. RECOMMENDED
       **decide now, execute after CUT-3** — retiring superbot surfaces
       before the cutover decision would strand live services. *(New
       2026-07-12, plan 5e.)*
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

37. **product-forge disposition — ⛔ SUPERSEDED 2026-07-12 (repo
    consolidation plan): do NOT answer this A/B/C as written.** *(Was: not in
    the owner's 8-seat list — retire the seat / fold into Venture Lab / keep
    as a 9th seat; new 2026-07-11, restructure directive — slice 3, fm
    PR #91.)*
   - id: OQ-FORGE-DISPOSITION
    - **Supersession note (2026-07-12, consolidation plan):** the census
      verdict **MIGRATE-THEN-ARCHIVE** + the plan's Phase 1 rehomes (ORDERs
      P1-1/2/3) + the Phase 3.1 archive click replace this item's A/B/C
      choice — option A's "keep the repo parked" framing is out of date; the
      repo now archives (reversibly) after its named assets land elsewhere.
      The seat-registry half (pointer-stub `projects/product-forge/`) rides
      the same disposition. Live successors: **B#40
      (OQ-CONSOLIDATION-ARCHIVE-FORGE)** gated by **E#44
      (OQ-CONSOLIDATION-DELETE-VS-ARCHIVE)**; plan:
      [`planning/2026-07-12-repo-consolidation-plan.md`](planning/2026-07-12-repo-consolidation-plan.md)
      § "Provenance & supersessions". Body kept verbatim below for
      history/audit.
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

38. **✅ STRUCK 2026-07-12 (same session) — item was INVALID: the Railway
    GitHub App has had "All repositories" access all along** (owner
    screenshot of the installation page; unchanged since install).
   - id: OQ-RAILWAY-APP-MINEVERSE
    - The instant build failures that seeded this item were mis-attributed:
      they were the missing Dockerfile (a pre-Dockerfile CLI upload failed
      identically; both paths succeeded once mineverse #44 added it).
      Merge=deploy is LIVE-VERIFIED: Railway auto-built #44's merge commit
      `ac312e8` at 16:50:00Z — one minute after the merge, no click needed.
    - Lesson recorded (capabilities.md rescue-venue section): an instant
      BUILD_IMAGE failure with an empty log means "no buildable app
      detected", NOT "repo unreadable" — check the tree for a build recipe
      before blaming app access.

44. **Consolidation gate — delete vs archive (the plan's FIRST structured
    choice; answer before any Phase 3 click)** *(new 2026-07-12,
    consolidation plan
    [`planning/2026-07-12-repo-consolidation-plan.md`](planning/2026-07-12-repo-consolidation-plan.md)
    § "⚠ First structured choice"; adopted from the game-lab-seat proposal's
    gate #1).*
   - id: OQ-CONSOLIDATION-DELETE-VS-ARCHIVE
    - WHAT — pick one; two of your own instructions contradict (standing
      ruling 2026-07-10 "delete no repos — they are the fleet's memory" vs
      ask 2026-07-12 "delete the test repos"), and this letter resolves it:
      **A (recommended)** — harvest → archive (read-only), delete NOTHING.
      Reversible, honors the standing ruling, still removes the repos from
      the active roster. Every "test-scratch"-labeled repo was found to hold
      shipped releases, finished unreleased tools, or a pinned contract
      exemplar — none is safe to delete on the label.
      **B** — deletion, as an explicit written override of the 2026-07-10
      ruling, per named repo, only after a ≥7-day post-archive cooling-off.
      Not recommended.
    - WHERE: one word wherever the manager reads — `control/inbox.md` ORDER,
      a live session, or a comment on the plan branch.
    - HOW: say "contradiction: A" (or B). Full reasoning: plan § "⚠ First
      structured choice" (the click surface is here; the reasoning is there).
    - UNBLOCKS: the whole Phase 2/3 set below rides this framing — B#40–42
      read their letter from here; the rest of the plan assumes A.
    - VERIFIED-NEEDED: both contradicting instructions are on record (plan
      § cites the 2026-07-10 ruling's home at superbot
      `docs/ideas/adopt-codetool-lab-tools-2026-07-10.md`).
    - RISK: ↩️ A is fully reversible (unarchive toggle) · ⚠️ B is
      destructive — hence the written-override + cooling-off rail.
    - Blocking: blocks B#40–42 (the archive clicks) and sequences E#45/E#46.

45. **Consolidation Phase 2.1 — cfgdiff v0.1.1 (codetool-lab-sonnet5):
    release it before the archive?** *(new 2026-07-12, consolidation plan
    § Phase 2 decision 1.)*
   - id: OQ-CFGDIFF-RELEASE-DECISION
    - WHAT — pick one:
      **A (recommended)** — release-in-place via the proven
      workflow_dispatch recipe (the route opus4.8 used to ship mdverify
      v0.1.0/v0.2.0 on 2026-07-09). One agent slice; zero tags exist on
      origin today, and **archiving freezes the tag-push path forever**, so
      this lands before the B#41 click.
      **B** — explicitly accept cfgdiff staying unreleased; archive as-is.
    - WHERE: one word to the manager (inbox ORDER / live session). The
      owner-click half of A is already staged click-level in Parked
      § "cfgdiff v0.1.1 release — two clicks".
    - HOW: say "cfgdiff: A" (or B). Reasoning: plan § Phase 2 decision 1.
    - UNBLOCKS: sequences B#41 (OQ-CONSOLIDATION-ARCHIVE-SONNET5) — the
      archive click waits on this letter.
    - VERIFIED-NEEDED: census § sonnet5 — zero tags on origin (`ls-remote`);
      owner ruling 2026-07-10 "archive … after harvest".
    - RISK: ↩️ reversible — A's release can be deleted; B forecloses nothing
      until the archive click itself (unarchive reopens the tag path).
    - Blocking: blocks B#41 only.

46. **Consolidation Phase 2.2 — envdrift (codetool-lab-fable5):
    release/adopt before the archive?** *(new 2026-07-12, consolidation plan
    § Phase 2 decision 2.)*
   - id: OQ-ENVDRIFT-RELEASE-DECISION
    - WHAT — pick one:
      **A (recommended)** — same release-in-place route (a release workflow
      must be added first — none exists on that repo), then archive;
      optionally adopt envdrift as a fleet tool afterwards (your named
      environment-tidying interest).
      **B** — accept unreleased; archive after ORDER P1-5 (the
      `.pyc`/`.gitignore` hygiene precondition) lands.
    - WHERE: one word to the manager. The tag/Release click surface already
      exists in Parked § "codetool-lab-fable5 (envdrift) v0.1.0 + v0.2.0
      tags + Releases" (same repo, same wall — that parked item covers the
      historical tags; this decision covers whether a releasable version
      ships at all before the freeze).
    - HOW: say "envdrift: A" (or B). Reasoning: plan § Phase 2 decision 2.
    - UNBLOCKS: sequences B#42 (OQ-CONSOLIDATION-ARCHIVE-FABLE5).
    - VERIFIED-NEEDED: census § fable5 — no release workflow; defects @
      `a6cf1a9`; tag-push is a verified 403 wall for agents on that seat.
    - RISK: ↩️ reversible — same shape as E#45.
    - Blocking: blocks B#42 only.

47. **Consolidation Phase 2.3 — superbot cron trims (the ≈170 runs/day
    burner)** *(new 2026-07-12, consolidation plan § Phase 2 decision 3.)*
   - id: OQ-SUPERBOT-CRON-TRIM
    - WHAT — pick one; today `ci-rerun-watchdog.yml` `*/12 * * * *` ≈120/day
      + `pr-conflict-guard.yml` `*/30 * * * *` ≈48/day:
      **A (recommended)** — watchdog → hourly (24/day) and conflict-guard →
      every 2 h (12/day): ≈168/day → ≈36/day, both functions stay alive.
      **B** — keep as-is until superbot's post-CUT-3 re-verdict.
    - WHERE: one word to the manager — the cron edits themselves are
      agent-side one-liners; the letter is yours because it changes live
      production-repo cadence.
    - HOW: say "superbot crons: A" (or B). Cost table: plan § "Cost table".
    - UNBLOCKS: the largest single cut of the fleet's scheduled Actions burn
      (~235 runs/day fleet-wide today, ≈80% reduction across E#47+E#48).
    - VERIFIED-NEEDED: plan cost table — schedules verified per-repo by
      grepping `schedule:` at origin/main.
    - RISK: ↩️ reversible — one-line cron revert per workflow.
    - Blocking: not-blocking; pure cost.

48. **Consolidation Phase 2.4 — websites enabler cron + fleet-manager
    roster-regen cadence trims (≈65 runs/day combined)** *(new 2026-07-12,
    consolidation plan § Phase 2 decision 4.)*
   - id: OQ-WEBSITES-FM-CRON-TRIM
    - WHAT — pick one; today websites `auto-merge-enabler.yml`
      `13,43 * * * *` = 48/day (+ healthcheck 6-hourly + review-bake daily
      ≈5/day) and fleet-manager `roster-regen.yml` every 2 h ≈12/day, each
      firing able to commit to main:
      **A (recommended)** — enabler → event-driven (`pull_request` trigger —
      it only has work when a PR opens) and roster-regen → regen-on-change
      (push-triggered) or 2×/day.
      **B** — keep as-is.
    - WHERE: one word to the manager — agent-side workflow edits, your
      letter because both crons can commit to main.
    - HOW: say "websites/fm crons: A" (or B). Reasoning + numbers: plan
      § Phase 2 decision 4 + cost table.
    - UNBLOCKS: websites ≈53 → ≈5/day; fleet-manager ~12 → ~2/day or
      on-change; pairs with E#47 for the ≈80% fleet-wide cut.
    - VERIFIED-NEEDED: plan cost table (same `schedule:` grep method).
    - RISK: ↩️ reversible — cron lines restore in one commit.
    - Blocking: not-blocking; pure cost.
    - **Reconciliation note (2026-07-12 merge):** the owner-live session armed a
      CCR roster bridge (`trig_011LrFY1k5cUHRYH6zwTvPvn`, `50 */2 * * *`, see
      B#33 BRIDGED note) that rides the same roster-regen cadence and
      self-retires when OQ-FM-ACTIONS-PR-PERMISSION lands — weigh it in the
      roster-regen half of this letter (it does not decide A/B).

52. **superbot-idle — generator-purchase economy: add the missing core growth
    verb?** *(new 2026-07-13; routed from superbot-idle control/outbox.md
    "OWNER QUESTION: generator-purchase economy", night run 2026-07-13, per
    the Q-0264 fan-in — this E-number is the fleet number the outbox asked
    the manager to assign; morning tally #158 next-3 item 3.)*
    - id: OQ-IDLE-GENERATOR-PURCHASE
    - WHAT — pick one; today there is NO way to buy generators (counts are
      fixed per the repo's current-state.md), so a fresh GameState produces
      nothing, tier2 (in every 2-gen pack) + the owned-milestone track are
      permanently dead content, and boost2 is a trap buy:
      **A (recommended)** — add `purchase_generator` with a geometric
      per-generator cost curve (the idle-genre standard), all numbers
      PROVISIONAL and SIM-pinned (pre-registered target T10 + a fresh
      economy sim) before merge — restores the genre's primary growth verb
      at the lowest design risk.
      **B** — a different curve shape (linear/tiered) if the Simulator's
      run prefers it.
      **C** — do NOT add it: declare tier2 + owned-milestones intentionally
      inert and remove the trap surfaces.
    - WHERE: one word wherever the manager reads — `control/inbox.md` ORDER
      or a live session; the manager relays the letter to superbot-idle's
      inbox.
    - HOW: say "idle generators: A" (or B/C).
    - UNBLOCKS: the core idle growth loop (the seat marks this P1 /
      blocking); un-deadens tier2 + the owned-milestone track; lets the
      pre-registered T10 target run.
    - VERIFIED-NEEDED: superbot-idle `control/outbox.md` @ HEAD (2026-07-13
      OWNER QUESTION entry, "needs fleet Q-number — manager to assign");
      the same night outbox's SIM-001 cluster documents the adjacent
      low-count no-op evidence.
    - RISK: ↩️ reversible — a new purchase path behind SIM-pinned
      PROVISIONAL numbers; C removes surfaces but is a one-commit revert.
    - Blocking: P1 for the idle seat — blocks its core-growth-loop lane;
      blocks nothing fleet-side.
    - Prior art (2026-07-13, batch-2 routing): the T10 cost-curve verdict
      subtree already exists — sim-lab `sims/verdict-017-t10-cost-curve/` —
      so letter A's sim leg starts from a run, not from scratch.

53. **superbot-idle — content-depth / endgame direction after the
    upgrade→prestige spine.** *(new 2026-07-13; routed from superbot-idle
    control/outbox.md "OWNER QUESTION: content-depth / endgame", night run
    2026-07-13, per the Q-0264 fan-in — E-number = the assigned fleet
    number, same as E#52.)*
    - id: OQ-IDLE-CONTENT-DEPTH
    - WHAT — pick one; the engine is complete but shallow as a game: two
      upgrades per pack cap out, prestige pays ~+8–10% for a ~3.5h grind
      (greedy-sim ratio 0.9175), and there is no goal/event/endgame past
      the wall:
      **A (recommended)** — pursue timed-events scoping next, building on
      the seat's existing `docs/design/timed-events-scoping.md` (values
      stay unregistered pending SIM-002/Q-0264) — cheapest depth win
      because the scoping doc already exists and registration gates keep
      it from outrunning the SIM-001 verdicts.
      **B** — prioritize a different depth mechanic (deeper upgrade
      ladders, endgame prestige tiers, achievements-as-goals).
      **C** — hold all depth work until the generator economy (E#52) +
      SIM-001 verdicts land.
    - WHERE: same surface as E#52 — one word to the manager; relayed to
      superbot-idle's inbox.
    - HOW: say "idle depth: A" (or B/C).
    - UNBLOCKS: the seat's next design lane after the engine spine; pairs
      with (does not gate) E#52.
    - VERIFIED-NEEDED: superbot-idle `control/outbox.md` @ HEAD (2026-07-13
      OWNER QUESTION entry, P2); `docs/design/timed-events-scoping.md`
      exists per that entry (values unregistered pending SIM-002/Q-0264).
    - RISK: ↩️ reversible — design/scoping only until SIM registration; no
      live numbers move under any letter.
    - Blocking: not-blocking (P2); sequencing-only interaction with E#52.

55. **curious-research — which slicer do you use?** *(new 2026-07-13,
    night-report roll-up — the seat asked in its PR #4 and restated it in
    REPORT 001's asks-pending.)*
    - id: OQ-CR-SLICER-ANSWER
    - WHAT: name the slicer you actually run (e.g. Cura / PrusaSlicer /
      OrcaSlicer / Bambu Studio) — one word.
    - WHERE: any surface the manager reads (chat / inbox); relayed to
      curious-research's inbox.
    - HOW: say "slicer: <name>".
    - UNBLOCKS: the seat's menu-clicks retraction follow-up guide (exact
      click-paths need the real slicer) — its NEXT-3 item 2.
    - VERIFIED-NEEDED: curious-research `control/outbox.md` REPORT 001 on
      main `a7e9a3f` (asks-pending item 1). NOTE: the trio in asks-pending
      item 2 (gift-polish go/no-go) shipped post-report at 09:55Z (#9 +
      #10) — that half is OVERTAKEN; only the slicer answer remains live.
    - RISK: ✅ none — an answer, not a change.
    - Blocking: blocks only that follow-up guide.

56. **✅ RETIRED to decided-and-flagged (swept 2026-07-14, Slice 0 item 6 /
    INC-05) — trading already ratified AND shipped KILL-SIG.**
    - id: OQ-TRADING-KILLSIG-VERDICT-CLASS
    - Evidence (live-verified via the GitHub API 2026-07-14): trading **PR
      #109 MERGED 2026-07-13T14:03:52Z** — independent review verdict
      **ACCEPT**, ratifying the already-merged R4-A adoption
      (`trading_lab.promotion.classify_verdict`, shipped in trading #100);
      trading **PR #118 MERGED 2026-07-13T23:12:14Z** — Round 6 graded 58
      lanes natively under it (8 KILL-SIG). Decide-and-flag class (Q-0240):
      research-lane grading metadata, reversible; the owner's remaining
      control is veto-on-review, not pre-approval. Flagged here; no owner
      action needed.

57. **superbot-next — curation ratification bundle: DROP-list (60 items) +
    settings-prune + D-0083 anchor.** *(new 2026-07-13, night-report
    roll-up — the ORDER 018 report's asks-pending, decide-and-flag work
    now awaiting the owner's one-pass review.)*
    - id: OQ-NEXT-CURATION-RATIFICATIONS
    - WHAT: one sitting, three ratifications — (1) the curation DROP list:
      60 items proposed for drop (report § DROP, landed via #327 =
      `f47ec6d`); (2) the settings-prune set; (3) the D-0083 anchor
      decision (proposal merged via #346 = `4f469fe`).
    - WHERE: the cited PRs/report on superbot-next main; reply through the
      manager or the seat's inbox.
    - HOW: "curation: ratify all" (or name exceptions per list).
    - UNBLOCKS: the curation rework tail (the open #332/#333/#345/#352/#354
      set builds on these calls); prevents rework if a drop is vetoed late.
    - VERIFIED-NEEDED: superbot-next ORDER 018 report on main (via #366 =
      `902791d`), asks-pending line; curation report #327.
    - RISK: ↩️ reversible pre-cutover — everything is on the rebuild
      substrate, Q-0241 lane.
    - Blocking: not-blocking (Q-0241: decided-and-flagged, veto window).

58. **pokemon-mod-lab — enabler-install decision: auto-merge or keep
    park-and-sweep.** *(new 2026-07-13, night-report roll-up — ORDER 008
    report ask 3.)*
    - id: OQ-PML-ENABLER-INSTALL
    - WHAT: pick one — **A**: install the kit's auto-merge-enabler workflow
      in pokemon-mod-lab (green control-lane PRs then self-land, as in the
      other seats); **B**: keep the current park-and-sweep convention (all
      night work parks green for your morning sweep).
    - WHERE: one word to the manager; relayed to the seat's inbox (install
      itself is agent-doable once decided — only the decision is yours).
    - HOW: say "pml enabler: A" (or B). If A, pair it with B#5 (ROM builds
      required check) so the enabler has contexts to gate on.
    - UNBLOCKS: ends the recurring pml parked-PR pile (5 green PRs parked
      tonight alone: #57/#58/#59/#61/#62 + the report PR #63).
    - VERIFIED-NEEDED: pml ORDER 008 report on PR #63 head `db46649`,
      "Asks pending" item 3 ("Decision only — nothing was installed").
    - RISK: ↩️ reversible — a workflow file; delete to revert.
    - Blocking: not-blocking, but the pile regrows every night run.

61. **superbot-games — DARK seat: re-wake or reassign its build orders.**
    *(new 2026-07-13, EAP final-night DARK sweep —
    docs/eap-final-night-worklists-2026-07-13.md @ `ca1ce28` § DARK
    dispositions.)*
    - id: OQ-GAMES-DARK-REWAKE-OR-REASSIGN
    - WHAT — pick one:
      **A (recommended)** — re-wake the seat: its served balance verdicts
      (ORDER 006 done — mining V042, fishing curve, DnD escort ruling,
      exploration bands) and standing fm ORDERs 030/031/037 are armed with
      no executor; a wake consumes them where they already live.
      **B** — reassign its build orders to an active seat (the SuperBot
      World lane or superbot-next executes the wiring instead; the manager
      relays the orders).
    - WHERE: one word wherever the manager reads — `control/inbox.md`
      ORDER or a live session.
    - HOW: say "games: A" (or B).
    - WHY: the seat has been DARK ~35h14m while served verdicts + three
      standing fm ORDERs sit unconsumed — armed work with no executor.
    - UNBLOCKS: the V042-band wiring + fm ORDERs 030/031/037 get an
      executor under either letter.
    - VERIFIED-NEEDED: docs/eap-final-night-worklists-2026-07-13.md @
      `ca1ce28` § DARK dispositions (roster gen #35; idea-engine
      `control/inbox.md` ORDER 006 @ `2808b16`).
    - RISK: ↩️ reversible — a routing choice; the orders themselves are
      unchanged either way.
    - Blocking: not-blocking fleet-side; blocks that seat's armed work.

62. **gba-homebrew — DARK seat: re-wake.** *(new 2026-07-13, EAP
    final-night DARK sweep — same source doc as E#61.)*
    - id: OQ-GBA-DARK-REWAKE
    - WHAT: re-wake the gba-homebrew seat — approved verdicts V050
      (Gloamline survival ceiling) + V054 (Brineward band-2) are served
      and build-direct plans are armed, with no live executor.
    - WHERE: the Game Lab Project (a wake paste), or one word to the
      manager.
    - HOW: say "gba: wake" (or paste the seat's startup prompt in its
      Project).
    - WHY: DARK ~29h10m with approved verdicts + armed build-direct plans
      sitting idle.
    - UNBLOCKS: the V050/V054 build lanes.
    - VERIFIED-NEEDED: docs/eap-final-night-worklists-2026-07-13.md @
      `ca1ce28` § DARK dispositions (sim-lab `control/outbox.md`
      L879/L959 @ `32ff5c3`).
    - RISK: ✅ a wake, nothing structural.
    - Blocking: not-blocking; holds only that lane's armed work.

63. **product-forge — confirm no-action (stays gated on E#44,
    OQ-CONSOLIDATION-DELETE-VS-ARCHIVE).** *(new 2026-07-13, EAP
    final-night DARK sweep — same source doc as E#61.)*
    - id: OQ-FORGE-DARK-NO-ACTION-CONFIRM
    - WHAT: confirm the sweep's no-action disposition — product-forge
      stays DARK (~2.1d) by design; fm ORDERs 023/024 (games-web →
      websites arcade; retro → fm docs) remain GATED on your consolidation
      approval at E#44 (OQ-CONSOLIDATION-DELETE-VS-ARCHIVE). Nothing runs
      until that letter.
    - WHERE: one word to the manager — or fold into the E#44 answer
      itself.
    - HOW: say "forge: confirmed" (or just answer E#44, which supersedes
      this confirm).
    - WHY: closes the DARK-sweep loop explicitly, so the seat's darkness
      reads as decided rather than missed by future sweeps.
    - UNBLOCKS: nothing directly — records that forge-DARK is
      intentional until E#44.
    - VERIFIED-NEEDED: docs/eap-final-night-worklists-2026-07-13.md @
      `ca1ce28` § DARK dispositions.
    - RISK: ✅ an acknowledgment, not a change.
    - Blocking: not-blocking.

64. **substrate-kit sub-rows gba-trackb + superbot-coordinator — confirm
    wound down so the roster rows retire.** *(new 2026-07-13, EAP
    final-night DARK sweep — same source doc as E#61.)*
    - id: OQ-KIT-SUBROWS-WINDDOWN-CONFIRM
    - WHAT: confirm the two substrate-kit sub-rows are wound down —
      gba-trackb (~3.7d stale) + superbot-coordinator (~3.3d stale), both
      presumed wound down by roster gen #35 — so the roster generator can
      retire the rows instead of printing them stale forever.
    - WHERE: one word to the manager.
    - HOW: say "sub-rows: retire" (or name one to keep).
    - WHY: presumed-dead rows that never retire are permanent roster
      noise and mask real freshness regressions.
    - UNBLOCKS: roster hygiene — gen output stops carrying two
      known-stale rows.
    - VERIFIED-NEEDED: docs/eap-final-night-worklists-2026-07-13.md @
      `ca1ce28` § DARK dispositions (roster gen #35).
    - RISK: ↩️ reversible — a retired row re-adds in one regen if a seat
      revives.
    - Blocking: not-blocking; roster hygiene.

65. **⏰ TIME-BOXED before Friday 2026-07-17 09:00Z — trading-strategy:
    resolve the duplicate grading fire.** *(new 2026-07-14, Slice 0 item 7 /
    plan C9.)*
    - id: OQ-TRADING-0717-DOUBLE-GRADING-FIRE
    - WHAT: TWO enabled triggers both fire the FIRST paper-lane grading on
      Friday 2026-07-17 ~09:00Z — the standing weekly cron
      `trig_01UsNU4JRps4b7jiAMdEfXNi` ("trading-strategy weekly paper-lane
      grading", `0 9 * * 5`, next 2026-07-17T09:05Z) AND a foreign one-shot
      `trig_01YXNmgqYeYQ1LuepsLmbNCG` ("send_later 2026-07-17T09:00Z
      #345500", run_once_at 09:00:00Z). Two grading sessions five minutes
      apart = double-write risk on the paper ledger's first-ever grading
      record.
    - WHERE: https://claude.ai console → Routines (cross-session trigger
      deletion is org-refused agent-side, so the delete click is yours;
      or say the word and the owning session can self-delete if reachable).
    - HOW: one letter — **A: delete the 09:00Z one-shot, keep the weekly
      cron (RECOMMENDED — the cron is the durable pacemaker; the one-shot
      is redundant with it and fires first, taking the "first grading"
      write)** · B: keep both (accept double-fire; second session must
      detect the existing grading record) · C: disable the cron, keep the
      one-shot (leaves NO standing grading pacemaker after 07-17).
    - UNBLOCKS: a clean single-writer first grading of paper-0001 — the
      record the trading KEEP-PARKED verdict waits on.
    - VERIFY: `telemetry/triggers-snapshot.json` (both records verbatim,
      re-checked at this wake); trading triage row "Leave parked until the
      2026-07-17 grading".
    - RISK: ⚠️ time-boxed — after Friday 09:00Z the double-fire has already
      happened; the ask expires into cleanup instead of prevention.
    - Blocking: blocks nothing today; blocks the clean first grading Friday.

66. **Heartbeat doctrine ruling — frozen-archive vs overwrite-per-session
    (one word, fleet-wide).** *(new 2026-07-14, wake 0235Z Slice D —
    INC-16/17/19/80, the fleet-inconsistency ledger's Class B root cause.)*
    - id: OQ-HEARTBEAT-DOCTRINE-RULING
    - WHAT: two binding texts disagree about the same file: every repo's
      `control/README.md` mandates OVERWRITE-per-session heartbeats, while
      superbot `docs/fleet-reading-path.md:55-56` blesses idle/mineverse
      "frozen archive" heartbeats — and seats froze accordingly
      (superbot-games heartbeat frozen at 2026-07-12T10:16Z while ~50 PRs
      shipped; superbot-idle same class). Pick one: **A (recommended):
      overwrite-per-session everywhere — a heartbeat is a LIVE signal;
      archived narrative goes to docs/retro/** · B: frozen-archive allowed
      for wound-down lanes, with a mandatory `frozen:` marker line the
      roster can parse.
    - WHERE: one word wherever the manager reads — `control/inbox.md`
      ORDER or a live session ("heartbeats: A" / "heartbeats: B").
    - HOW: on the word, ONE kit/fm pass re-stamps the divergent seats and
      annotates fleet-reading-path (pending lane writes; superbot +
      affected lanes).
    - WHY: the manager's roster read heartbeat prose as truth and rated a
      shipping seat DARK ~37h (INC-16) — the owner was even asked to
      re-wake a seat that shipped #92–#106 that same night. Mitigation
      already shipped fm-side (this wake): the roster now carries a
      heartbeat-vs-commits divergence marker, so DARK is never declared on
      heartbeat alone — but the doctrine fork itself only closes with this
      ruling.
    - UNBLOCKS: retires INC-16/17/19/80 (half of ledger Class B) in one
      ruling.
    - VERIFIED-NEEDED: fm `docs/fleet-inconsistencies-2026-07-13.md` §3
      (both sides cited per row); roster gen #39 divergence line
      (`docs/roster.md`).
    - RISK: ✅ a doctrine word; the re-stamp pass is reversible text.
    - Blocking: not-blocking (mitigated by the divergence marker); blocks
      only the Class B ledger rows' final retirement.

67. **@codex verdict-review doctrine ruling — gate vs suspend (one word,
    fleet-wide).** *(new 2026-07-14, wake 0633Z Slice C — INC-43, the
    fleet-inconsistency ledger's Class E doctrine fork.)*
    - id: OQ-CODEX-GATE-VS-SUSPEND-RULING
    - WHAT: sim-lab's binding docs fork on the @codex step. Its README
      still MANDATES an @codex review comment on every verdict PR before
      finalization (Q-0264.4) while the step is SUSPENDED @ `dedc12e`
      after 3/3 verified fabricated reviews (incidents #1–#3);
      current-state records the suspension, the binding docs don't.
      Meanwhile fm ordered fleet-wide adoption of the VERDICT 016
      authenticity gate ("gate, don't suspend" — fm inbox L1095). Pick
      one: **A (recommended): GATE — reinstate the @codex step behind the
      VERDICT 016 authenticity checks (an external review only counts
      when it demonstrably engages the real diff), fleet-wide** ·
      B: SUSPEND — retire the mandate everywhere until Codex
      quota/fabrication stabilizes; binding docs annotated accordingly.
    - WHERE: one word wherever the manager reads — `control/inbox.md`
      ORDER or a live session ("codex: A" / "codex: B").
    - HOW: on the word, ONE ORDER-to-lane(sim-lab) annotates
      README/CONVENTIONS/owner-profile once; the same word settles any
      other lane's review-step wording.
    - WHY: two binding texts disagree about a mandatory review step; a
      literal follower of the README performs a ceremony the lane itself
      verified produces fabricated reviews.
    - UNBLOCKS: retires INC-43; unforks sim-lab's binding docs from its
      practiced state.
    - VERIFIED-NEEDED: re-verified live 2026-07-14T07:04Z at sim-lab
      origin/main — README ("Every verdict PR gets an @codex review
      comment … before finalization (Q-0264.4)") vs
      `docs/current-state.md:235` ("SUSPENDED per the outbox codex-line
      escalation @ dedc12e"); fm `docs/fleet-inconsistencies-2026-07-13.md`
      INC-43.
    - RISK: ✅ a doctrine word; the annotation pass is reversible text.
    - Blocking: not-blocking (sim-lab operates on the suspension); blocks
      only the doctrine fork's retirement.

### (F) New intake 2026-07-12 (owner-live session) — decisions, no rush

39. **Railway project duplication — websites services exist in BOTH
    `reliable-grace` (live: review-production-f027, superbot-app) and
    `superbot-websites` (parallel copy, has `control-plane`).**
   - id: OQ-RAILWAY-PROJECT-SPLIT
    - WHAT: decide the canonical home. RECOMMENDATION: **freeze until the
      2026-07-14 EAP window closes** (the Anthropic email links the
      reliable-grace URLs — do not move/rename them this week), then have the
      Websites seat consolidate into `superbot-websites` and retire the
      duplicates. `ANTHROPIC_API_KEY` was set on BOTH review services
      2026-07-12 so either path works.
    - WHERE/HOW: one word to the manager (inbox ORDER) after 07-14.
    - Blocking: nothing; a drift hazard if both sets keep deploying.

## Resolved 2026-07-12 (owner-live session — Railway/API executed directly)

- **websites `ANTHROPIC_API_KEY` ✅** — set on the LIVE review service
  (`reliable-grace`/review, serving review-production-f027; owner-approved,
  service redeployed 2026-07-12 ~16:0xZ) AND on the parallel
  `superbot-websites`/review service. The websites-order (ORDER 019) B-section
  blocker is pre-cleared; the on-site AI assistant has its key.
- **mineverse web host ✅ (the non-portal 4/6 of OQ-MINEVERSE-ENV-VARS)** —
  Railway project `superbot-mineverse` created, `web` service deployed
  read-only degraded at `https://web-production-97636.up.railway.app` (CLI
  one-shot; auto-deploy verified working same day — item 38 struck), 3 vars
  set (signing key · redirect URI · client id). Remainder split: 2 portal
  steps stay owner (item 17), the write pair stays agent-side (FLAG 2).
- **mineverse sign-in: OWNER PORTAL STEPS COMPLETE ✅ (evening, same day)** —
  the owner registered the redirect URI (proven: Discord's consent screen
  renders on /auth/login) after the OAuth-app reuse (item 17 update). The
  first live sign-in then failed at token exchange — root-caused to
  discord.com/Cloudflare 403ing urllib's default User-Agent (valid
  id+secret; curl UA 200 vs python UA 403 on the same endpoint) — fixed in
  mineverse PR #45 (UA header + server-side error logging). Nothing further
  is owner-side for sign-in; #45's merge auto-deploys and the owner retries.
- **roster-freshness BRIDGED ✅** — `fleet roster regen bridge`
  (`trig_011LrFY1k5cUHRYH6zwTvPvn`, `50 */2 * * *`, fleet-manager env,
  fresh-session) lands parked roster PRs + refreshes the triggers snapshot;
  RETIRED same day: the owner clicked the toggle and the bridge trigger was deleted after live verification (runs 29202721367, PRs #129/#131).

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
  Releases are LIVE.) *(2026-07-12: the release-or-not decision is now
  ACTIVE at E#46, OQ-ENVDRIFT-RELEASE-DECISION — this stays as the click
  surface for the historical tags if E#46 = A.)*
- **codetool archive toggles ×3 (paired DECISION)** — all three repos
  `"archived": false` (API-verified 2026-07-10); recommendation: **wait until
  the gen-3 succession question settles, then archive** (archiving makes the
  repos read-only). *(2026-07-12: PROMOTED — superseded by the consolidation
  plan's sequenced clicks: sonnet5 + fable5 archive at B#41/B#42 after
  Phase 1 + E#45/E#46; opus4.8 stays UNARCHIVED (KEEP-QUIET, mdverify
  release host — per the plan it is NOT one of the three archives; the third
  is product-forge, B#40).)*
- **cfgdiff v0.1.1 release — two clicks (codetool-lab-sonnet5):** (1) PyPI
  pending publisher (owner `menno420`, repo `codetool-lab-sonnet5`, workflow
  `release.yml`, environment `pypi`); (2) `git tag -a v0.1.1 0b1eb60 && git
  push origin v0.1.1` — do NOT tag v0.1.0 at `0260aae` (predates release.yml).
  Tag push is a credential-layer 403 on that seat. *(2026-07-12: the
  release-or-not decision is now ACTIVE at E#45,
  OQ-CFGDIFF-RELEASE-DECISION — these two clicks are the HOW if E#45 = A.)*
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
- **fleet-manager stale branch (agent branch-delete is a verified 403):**
  `claude/consolidation-plan-v34` @ 30a48fa — accidental resurrection of PR
  #122's merged head during a parallel merge-back; nothing unique on it (its
  content landed via #122's merge commit fda3182/8f92faa).
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
  - *Reconciliation (2026-07-14, Slice 0 item 6 / INC-04 — the fm↔sim-lab
    state fork):* the two repos conflated **integration-ENABLED** (done —
    the resolution above stands) with **usage-QUOTA-capped** (still real:
    sim-lab `control/status.md` holds ⚑ OA-002 open with 6+ @codex questions
    pending on quota flaps). Split verdict: enabled = RESOLVED here;
    quota-throughput = OPEN, tracked sim-lab-side (its ledger is the write
    surface) + the flapping evidence at `OQ-CODEX-FLAPPING`. Cross-link:
    sim-lab inconsistency 4.
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
