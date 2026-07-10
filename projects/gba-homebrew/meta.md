# gba-homebrew — Project package meta

- **Lane:** games program (Q-0259 ruling 5: 3 dedicated game Projects) —
  game-lab Track B, PUBLIC, original Butano homebrew. **LIVE-PARKED,
  scope-complete:** session 7 closed with Lumen Drift SCOPE-COMPLETE and the
  concept doc's polish list EXHAUSTED (`control/status.md` @ `bc73da7`,
  updated 2026-07-10T07:14:30Z; PR #23 merge `f502147`); the lane idles on
  the owner concept pick (⚑: Lumen Drift / Clockwork Courier / Shoal,
  `docs/concepts/session-1-concepts.md`). Inbox ORDER 002 (self-arm hourly
  wake) is `status: new`, UNEXECUTED — landed after the lane's last inbox
  re-read; this package's part 4 supersedes its hourly cadence with
  provenance.
- **Kit:** **v1.7.0 — current as of today's PR #26** (merge `bc73da7` =
  origin/main HEAD, verified via ls-remote this session). Note: the
  committed `control/status.md` kit line still says v1.6.0 — it predates the
  #26 merge (benign lag; the next heartbeat corrects it).
  `.substrate/claude/CLAUDE.md` is RENDERED by the v1.7.0 upgrade (unlike
  Track A's unrendered copy) but staged-only — no `.claude/` dir installed.
- **Cadence:** `0 */2 * * *` (lanes even hours :00; manager `30 */2`; gen-3
  standard §2). Under Q-0265 the cron is the dead-man failsafe; the
  send_later ~15-min chain is the pacemaker. **No routine currently exists
  for this lane** (nothing recorded in status; ORDER 002 unexecuted).
- **Environment archetype:** `fleet-manager environments/archetype-gba-lab.sh`
  (the 5th archetype, explicit-justification carve-out from the ≤4 rule) —
  **⚠ UNTESTED AS-A-WHOLE:** every route was proven in-container by the
  toolchain scout 2026-07-09, but the assembled script "is
  unverified-as-a-whole until the lane's first boot" (fm
  `environments/README.md` @ origin/main `0eaa668`, line 41 — the lane so
  far booted from owner-pasted setups, not this script). The package's
  `setup-script.sh` wraps the repo's own pinned `tools/setup-toolchain.sh`
  (fail-soft call, pins never bypassed) + python basics (mgba==0.10.2 pin) +
  the capability-probe block; first boot verifies the assembled whole —
  treat any [setup:WARN] as a finding.
- **Grants:** `menno420/gba-homebrew` only (Q-0260 single-writable-repo;
  cross-repo reads via public raw). Env variables: **none** (fm
  `environments/archetypes.md` project map: gba-homebrew → gba-lab,
  "*(none)*"; zero secrets by design — public repo).
- **Codex enabled:** **unknown.** Cheap check this session: issue-scoped
  GitHub search for "codex" in menno420/gba-homebrew returned 0 items —
  but that endpoint misses review-comment activity, so absence is not
  evidence. The fleet review-queue ledger lists every non-proven repo's
  Codex availability as "unknown until probed"; the coordinator prompt
  orders a one-time probe (@codex on a merged head, outcome recorded in
  CAPABILITIES).

## Deployed-state per part (2026-07-10)

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — Q-0265/Q-0264/Q-0259-r5 re-base of the game-lab founding §CI | Whatever the live game-lab Project's Custom Instructions hold is **not in git** (founding text was drafted for verbatim paste but its deployment record says NOT YET DEPLOYED; the fitted gen-2 package `fm:docs/proposals/instructions/game-lab.md` is PROPOSED/held, pre-Q-0265). Deployed-state: **unknown** | fm `docs/prompts/game-lab-founding.md` § Deployment record; inventory-hub §A row 4; inventory-games-new §2 |
| 2 coordinator prompt | `coordinator-prompt.md` — continuous rewrite of the founding brief + control/README ritual | **No coordinator/continuous prompt deployed or committed** — the lane ran 7 sessions on the per-wake standing ritual (control/README.md) + the inbox standing-default paragraph; both are discrete-wake shapes | gba `control/README.md` + `control/inbox.md` § Standing default @ `bc73da7`; inventory-games-new §2 |
| 3 setup script | `setup-script.sh` — archetype-gba-lab wrapped fail-soft around `tools/setup-toolchain.sh` + probes | Console field contents **unverified** (owner-paste convention, no paste record). In-repo: `tools/setup-toolchain.sh` @ `bc73da7` is the proven pinned installer (sessions 1–7 + CI cache built on it); the archetype script itself has never run as-a-whole | gba `tools/setup-toolchain.sh` @ `bc73da7`; fm `environments/archetype-gba-lab.sh` + `environments/README.md` L41 |
| 4 failsafe text | `failsafe-prompt.md` — idea-engine Q-0265 reference template adapted; supersedes ORDER 002's hourly text with provenance | **NOT ARMED.** No routine exists; ORDER 002 (hourly self-arm) is `new`/unexecuted and encodes the pre-Q-0265 model. The coordinator arms this file's text at first boot and records the calls verbatim in status | gba `control/inbox.md` ORDER 002 + `control/status.md` orders line @ `bc73da7`; superbot router Q-0265 @ `origin/main` L9573 |

## Sources

- gba-homebrew @ `bc73da7` (= origin/main, ls-remote-verified this session):
  `CONSTITUTION.md` · `README.md` (⚠ HARD RAIL) · `docs/conventions.md`
  (rules 1–16 incl. 13–15 hard rails, 16 CI tier) · `control/README.md`
  (standing ritual) · `control/inbox.md` (ORDERs 001/002 + standing default)
  · `control/status.md` (session-7 close-out, ⚑ concept pick) ·
  `tools/setup-toolchain.sh` (pins + supply-chain posture) ·
  `.github/workflows/rom-builds.yml` (compile-only per-PR) +
  `headless-boot.yml` (workflow_dispatch tier) + `substrate-gate.yml` ·
  `docs/review-queue.md` (11 open rows: #3 #5 #6 #8 #9 #12 #13 #16 #17 #20
  #23) · `docs/PLATFORM-LIMITS.md` (devkitPro 403 · main-push ruleset ·
  self-merge classifier · api.github.com session gate · mGBA load_save
  segfault) · `docs/concepts/session-1-concepts.md` (3 candidates + what
  transfers) · `.substrate/claude/CLAUDE.md` (rendered, staged-only) ·
  `.substrate/upgrade-report.md` (v1.6.0 → v1.7.0).
- fleet-manager @ origin/main `0eaa668`: `docs/prompts/game-lab-founding.md`
  (founding CI + ORDER 001 + deployment record) ·
  `docs/proposals/instructions/game-lab.md` (held gen-2 package, pre-Q-0265)
  · `environments/archetypes.md` (gba-lab row + project map) ·
  `environments/archetype-gba-lab.sh` · `environments/README.md` L41
  (unverified-as-a-whole) · `docs/review-queue.md` (binding N=50 auto-append
  + two-tier drainer) · `docs/playbook.md` R21/R22/R24.
- superbot @ origin/main (fetched this session): router Q-0259 (r5 games
  program, L9347) · Q-0260 (single-repo) · Q-0264 (L9511) · Q-0265 (L9573) ·
  Q-0266 (volume-first).
- Inventories (scratchpad `launch-packages/`): inventory-games-new.md §2 +
  cross-cutting §5/§7; inventory-hub.md §A row 4, §C.
- Codex check: GitHub issue-scoped search `repo:menno420/gba-homebrew codex`
  → 0 items (this session; absence ≠ evidence).

**Last verified:** 2026-07-10 (gba-homebrew read at origin/main HEAD
`bc73da7`; fleet-manager + superbot fetched from origin/main this session).
