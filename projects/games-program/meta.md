# games-program — package meta

> **Status: PRE-BIRTH ×3 repos.** Q-0259 ruling 5 (owner, 2026-07-10; superbot
> `docs/owner/maintainer-question-router.md` @ `dc19b1e8`): standing instruction —
> **"3 dedicated game projects, each with their own repo"**, that continuously improve
> existing games, invent new games, or mod other games — presenting **a few options
> wherever that feels wise** rather than asking. A capability test by design; the
> **owner plays the builds AFTER the EAP, not now** (EAP free window through 2026-07-14
> per fleet-manager status), and improvement rounds follow. No games-program Projects
> exist; none of the 3 repos-as-projects are mapped or created yet.

## The mapping — DECIDE-AND-FLAG, pending the manager's proposal

Q-0259's routing line assigns it: "the manager maps the current game lanes
(superbot-games shared repo · pokemon-mod-lab · gba-homebrew) onto the
3-projects/3-repos shape **decide-and-flag**." No mapping proposal exists in
fleet-manager at `0eaa668` (grep: no Q-0259-r5 reference in either game repo's control
files, and both lanes' last substantive status writes predate the ruling). The likely
shape this package set plans for (flag, not decided):

1. **Project 1 — Emerald/QoL+ mod project → reuses `pokemon-mod-lab`** (exists, HEAD
   `a76ada70cb0b`, PRIVATE, live-parked). Q-0262.7 already ruled its concept:
   **Pokemon concept pick = QoL+** (the lane's own recommendation; its 12 shipped
   game-feel patches form the foundation) — "takes effect when the games program boots
   post-core." Privacy carve-out: private repo ⇒ no raw-read by other Projects; must be
   attached to the manager's env (Q-0260 consequence 3). Inherits ORDER 003's
   visibility=private hard rail (in its inbox, unexecuted).
2. **Project 2 → reuses `gba-homebrew`** (exists, HEAD `bc73da7`, public, kit v1.7.0,
   live-parked; Lumen Drift SCOPE-COMPLETE). Track-B concept pick still OPEN
   (fleet-manager owner-queue item); the ruling's "present a few options" instruction
   fits this fork point exactly.
3. **Project 3 — TBN** (invent-new-games or mod-other-games mandate; no repo). Repo
   creation is owner-only (Q-0262 "not appliable by delegation" list names "repo
   creations … 3 game repos"). Whether superbot-games (the merged games-plugins lane)
   folds in here or stays a superbot-hub concern is part of the manager's mapping call.

Everything above the ruling itself is **DECIDE-AND-FLAG pending the manager's mapping
proposal** — recommendation recorded, owner/manager veto window open, nothing executes
from this dir.

## What exists today (raw material, all pre-Q-0265)

- One shared **game-lab lane across two repos** with per-repo inboxes
  (`control/README.md` in both repos — the manager↔lane protocol + standing ritual).
- Both repos carry an **unexecuted ORDER 002** (self-arm HOURLY wake) — the old
  discrete-wake model; superseded by Q-0265 continuous mode and must be reconciled at
  first boot, not executed.
- Held gen-2 packages in fleet-manager `docs/proposals/instructions/` @ `0eaa668`:
  `game-lab.md`, `games-exploration.md`, `games-mining.md` — all under the **Q-0262.6
  hold** (stay undeployed until re-based on the gen-3 blueprint delta). The gen-2
  founding CI base: `docs/prompts/game-lab-founding.md` (never deployed as such; both
  lanes' ORDER 001 cited it).
- Env archetype: `fleet-manager environments/archetype-gba-lab.sh` @ `0eaa668`
  (devkitARM r68 + agbcc + mGBA) — plus gba-homebrew's own pinned
  `tools/setup-toolchain.sh` @ `bc73da7` (leseratte10 mirror workaround for the
  devkitPro Cloudflare-403 wall).

**These are 3 NEW per-project packages to be built from the gen-3 template — not a port
of the single game-lab-founding.md prompt** (the shared-lane shape is what Q-0259 r5
retires).

## Companion file

`expected-seed.md` (this dir) — the pre-birth checklist per repo, modeled on how
product-forge's seed worked.
