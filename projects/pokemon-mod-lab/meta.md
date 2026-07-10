# pokemon-mod-lab — Project package meta

- **Seat:** games program, Emerald seat (Q-0259 r5: 3 dedicated game
  Projects, each with its own repo — this repo is the natural Emerald
  project's repo, carrying the lane's own QoL+ recommendation and its 12
  shipped patches; manager confirms the mapping decide-and-flag). Concept
  RULED: **Emerald QoL+** (Q-0262.7 — "takes effect when the games program
  boots post-core"; until that boot the lane stays parked unless ordered).
- **Lane state:** **LIVE-PARKED** — `control/status.md` @ `a76ada7`
  (2026-07-10T07:49Z, session 008): "LANE PARKED — overnight run complete:
  sessions 001–008, PRs #2–#10 all merged on green"; standing-default queue
  exhausted; 3 ⚑ owner asks carried (required-check click · concept pick —
  now ruled by Q-0262.7 · game-feel playtest, 4 patches to verdict).
- **Visibility:** **private = true — VERIFIED TODAY** (2026-07-10, this
  session, via the claude-code-remote `list_repos` API surface:
  `{"full_name":"menno420/pokemon-mod-lab", "visibility":"private",
  "pushed_at":"2026-07-10T12:56:12Z"}`). History note: the repo was PUBLIC
  through the overnight run (night-review finding Q16); the owner flipped it
  ~12:41Z–12:56Z window per ORDER 003's dispatch note + the pushed_at above.
  ORDER 003 (verify + record in status + R22 standing rule) is still
  UNEXECUTED lane-side — first package boot executes it.
- **Kit:** **v1.6.0** (`control/status.md` kit line @ `a76ada7`) — one
  release behind the fleet's v1.7.0; `.substrate/claude/CLAUDE.md` is still
  the **UNRENDERED** template (`${...}` slots, no root `.claude/` dir) —
  the package's instructions/coordinator prompt order the upgrade + render
  at first natural boundary.
- **Cadence:** failsafe `0 */2 * * *` (gen-3 lane stagger), pacemaker
  send_later ~15 min. Supersedes inbox ORDER 002's hourly ask (unexecuted;
  see failsafe-prompt.md provenance note). **NOT ARMED today** — no trigger
  recorded anywhere in the repo.
- **Environment archetype:** **gba-lab** — fleet-manager
  `environments/archetypes.md` @ `0eaa668` maps pokemon-mod-lab → gba-lab
  (`environments/archetype-gba-lab.sh`, scout-proven routes). The package's
  `setup-script.sh` is that archetype REDUCED to the Track A subset (no
  devkitARM/Butano mirror blocks — those are gba-homebrew's) + the fleet
  capability-probe block + agbcc install from the vendored tree per the
  repo's own `rom-builds.yml`. Variables: none (zero secrets by archetype);
  optional `SKIP_ROM_WARM_BUILD=1`.
- **Grants — PRIVATE-REPO FLAG:** raw-read does NOT work on private repos,
  so every access path needs an explicit repo grant: (a) the Project's
  session/environment needs menno420/pokemon-mod-lab attached (the only
  read/write path); (b) **the manager's own env lacks it** — router Q-0260
  carve-out: "the manager's staleness sweep needs pokemon-mod-lab attached
  to the manager's environment (or accepts a DARK-by-privacy verdict relayed
  via the owner)"; (c) substrate-kit's distribution seat likewise
  ("attach is the only path", kit founding package §3 repo list). Owner
  click: attach the repo to this Project's env + (optionally) the manager's.
- **Codex:** **likely N/A on a private repo** — the @codex connector has
  reviewed only public fleet repos; no codex-connector comment exists on any
  of PRs #2–#10 (lane history shows post-merge review via review-queue.md
  only). Check cheaply at first boot: one @codex mention on a merged PR; if
  no response within a session, record `codex: unavailable (private)` in
  docs/capabilities.md and rely on review-queue.md + manager sweep instead.
  Do NOT paste private-repo diffs to any external review surface (PRIVATE
  hard rail).

## Deployed-state per part (2026-07-10)

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — Q-0265/Q-0264/Q-0262.7 re-base with the PRIVATE + R22 rails | The gen-2 game-lab founding text was the pasted CI at the 2026-07-10 lane boot (shared game-lab Project, two repos — pre-Q-0265, pre-visibility-flip, no R22); no paste receipt in-repo | fm `docs/prompts/game-lab-founding.md` @ `0eaa668` (its deployment record still says "NOT YET DEPLOYED" — stale vs the lane's live history); inventory-games-new §1 |
| 2 coordinator prompt | `coordinator-prompt.md` — continuous seat brief; executes ORDERs 002/003 at boot | **No coordinator prompt ever deployed** — the lane ran on manager/owner-driven sessions + the committed standing ritual (`control/README.md`); ORDER 002's hourly self-arm text is the closest committed ancestor, unexecuted | pokemon-mod-lab `control/README.md` + `control/inbox.md` @ `a76ada7`; `control/status.md` orders line ("no order consumed" after 001) |
| 3 setup script | `setup-script.sh` — gba-lab archetype Track-A subset + probes | Unknown console state; the gba-lab archetype is the fleet-side candidate ("assembled-whole unverified until first lane boot" caveat, inventory-hub §C); no repo-level session-setup script existed in-repo | fm `environments/archetype-gba-lab.sh` + `archetypes.md` @ `0eaa668`; pokemon-mod-lab `.github/workflows/rom-builds.yml` + `docs/capabilities.md` @ `a76ada7` |
| 4 failsafe text | `failsafe-prompt.md` — Q-0265 template + R22, `0 */2` superseding ORDER 002's hourly | **NOT ARMED** — no trigger recorded in-repo; ORDER 002 status `new`, unexecuted | pokemon-mod-lab `control/inbox.md` ORDER 002 + `control/status.md` @ `a76ada7`; idea-engine deployed-failsafe exemplar (inventory-games-new §8) |

## Sources

- pokemon-mod-lab @ `a76ada7` (origin/main, local clone synced this
  session): `README.md` (PRIVATE hard-rail text) · `CONSTITUTION.md` ·
  `control/{README,inbox,status}.md` (standing ritual; ORDERs 001–003;
  parked state + 3 ⚑s) · `docs/conventions.md` (landing path R21/R5/R12) ·
  `docs/capabilities.md` (toolchain + headless recipes) ·
  `docs/PLATFORM-LIMITS.md` (ruleset/classifier/403 walls) ·
  `docs/mod-concepts.md` §1 (QoL+ systems map) · `docs/backlog.md` (parked
  queue + owner-gated leftovers) · `docs/qol-patches.md` (12 patches) ·
  `.github/workflows/{rom-builds,substrate-gate}.yml` ·
  `.substrate/claude/CLAUDE.md` (unrendered).
- fleet-manager @ `0eaa668` (origin/main): `docs/prompts/game-lab-founding.md`
  (the deployed gen-2 founding text this package re-bases) ·
  `docs/proposals/instructions/game-lab.md` (HELD gen-2 package — superseded
  by this package; its `game-lab-emerald` repo naming never happened) ·
  `environments/archetypes.md` + `environments/archetype-gba-lab.sh`.
- superbot @ `dc19b1e` (origin/main): `docs/owner/maintainer-question-router.md`
  Q-0259 r5 (L9347) · Q-0260 carve-out item 3 (private-repo raw-read) ·
  Q-0262.7 (L9442 block) · Q-0263.2 · Q-0264 (L9511) · Q-0265 (L9573).
- Live API: claude-code-remote `list_repos` (visibility verification, this
  session).
- Inventories (scratchpad `launch-packages/`): inventory-games-new.md §1 +
  cross-cutting §5/§7; inventory-hub.md §B/§C/§F.

**Last verified:** 2026-07-10 (repos fetched to origin/main + visibility
API call made this session).
