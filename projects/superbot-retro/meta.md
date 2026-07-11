<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# superbot-retro — Project package meta (Retro-Games studio seat — REPO-LESS)

> **v1, registry centralization (registry doctrine, same shape as ORDER 015):
> swept from what verifiably exists and runs (live trigger registry,
> extraction 2026-07-11T13:17:24Z + the founding texts merged in superbot PR
> #1972 @ `10a7486` + an exhaustive GitHub repo search), not authored
> aspirationally.** This seat is the fleet's first **repo-less** package dir:
> `superbot-retro` names an ENVIRONMENT + Project, not a repo — its two
> writable repos are `menno420/gba-homebrew` and `menno420/pokemon-mod-lab`,
> which keep their own package dirs (`projects/gba-homebrew/`,
> `projects/pokemon-mod-lab/`). This dir holds what belongs to the SEAT
> itself: its failsafe, the hourly child-lane wakes it drives, and its
> founding provenance.

## Repo-less — the absence evidence (verbatim, 2026-07-11)

**`menno420/superbot-retro` does NOT exist as a repo.** GitHub MCP
`search_repositories(query="user:menno420 superbot in:name")` returned
`total_count: 6`, `incomplete_results: false` — the complete list: superbot,
superbot-next, superbot-games, superbot-idle, superbot-mineverse,
superbot-plugin-hello. `superbot-retro` is not among them. (A direct
`get_file_contents` probe was session-scope-denied, not a 404, so the
non-truncated exhaustive search is the authoritative proof.) This matches
the founding package by design: its §0/§3 define `superbot-retro` as the
**environment name** attaching both retro repos — no repo was ever supposed
to exist. Everything the seat ships lands in gba-homebrew or pokemon-mod-lab
(one PR = one repo, never across both).

| Field | Value |
|---|---|
| Seat | **Retro-Games studio seat — LIVE, repo-less.** The games program's 3rd dedicated game Project (Q-0259 r.5), owner-directed 2026-07-11: ONE studio seat spanning BOTH retro repos — `gba-homebrew` (original homebrew, public) + `pokemon-mod-lab` (ROM QoL patches, PRIVATE). Booted 2026-07-11 from the superbot founding package `docs/planning/round3-founding-package-games-retro-2026-07-11.md` (merged in superbot PR #1972, squash SHA `10a7486a49c5b44d2db5f414fddb0321e63b4ebb`, 2026-07-11T01:09:06Z) |
| Coordinator session | `session_01BqCRbGYGeo97sFxMJHzu1e` (the failsafe trigger's persistent session binding; persist_session true) |
| Environment | `env_014P62UXP7cuK1bPPWWzg521` — shared by the seat's failsafe AND both hourly child-lane wakes (registry-verified; the hourly wakes' `sources` list both repos: gba-homebrew's wake carries `https://github.com/menno420/pokemon-mod-lab` + `https://github.com/menno420/gba-homebrew`), consistent with founding §0 step 1 (env attaches both repos; retro toolchain, NOT plain python-lab) |
| Cadence | Cron failsafe **`trig_01Y99uDKNtKTz2EtRYPWZkGY`** "superbot-retro failsafe wake" **`50 */2 * * *`**, enabled, armed 2026-07-11T01:16:16Z, bound to the coordinator session — registry-verified, stored prompt VERBATIM in `failsafe-prompt.md`. PLUS two hourly fresh-session child-lane wakes the seat drives (created ~20 min after the failsafe, named "(ORDER 002)"): gba-homebrew `0 * * * *` + pokemon-mod-lab `30 * * * *` — VERBATIM records in `triggers.md`. Unlike the mineverse/idle/games seats, NO "chain link" one-shot triggers for this seat appear in the 549-record registry sweep — the hourly wakes, not a send_later chain, are the observable work drumbeat |
| Orders | No seat-level inbox exists (no repo). Manager orders route via the two repos' own `control/inbox.md` files (e.g. the 2026-07-11 fleet-wide self-review ORDER landed as pokemon#26 `9f3c5fd` + gba#39 `ad895d2`) |
| Grants | Write: `menno420/gba-homebrew` + `menno420/pokemon-mod-lab` (owner-directed TWO-repo deviation from the Q-0260 one-writable-repo norm, flagged in the founding package header; cross-repo writes forbidden — one PR targets exactly one repo). pokemon-mod-lab is PRIVATE (integrity floor: patches-not-ROMs) — raw-read DARK to other seats; env-attach is the only read path |
| Codex | Per-repo, not per-seat: see `projects/gba-homebrew/meta.md` + `projects/pokemon-mod-lab/meta.md` (both pre-dated the ORDER 014 fleet-wide enablement list, which named neither retro repo) |
| Open flags | The gba/pokemon package dirs (built 2026-07-10, BEFORE this seat existed) carry now-stale cadence rows: "`0 */2` spec'd — NOT armed" and "unexecuted hourly ORDER 002s … superseded, never executed" — reality since 2026-07-11T01:36Z is the OPPOSITE (hourly wakes armed and firing, `triggers.md`). Regenerating those two packages against the live seat is the flagged follow-up (regenerate-don't-fork, doctrine 4) — not edited in this bounded slice |

## Founding texts — pointer (registry doctrine: committed once, not forked)

The seat's Custom Instructions (§1) and coordinator brief (§2) exist
committed VERBATIM in **superbot PR #1972, squash SHA
`10a7486a49c5b44d2db5f414fddb0321e63b4ebb`**:
`docs/planning/round3-founding-package-games-retro-2026-07-11.md` — §1
(instructions paste block, ~3,700 chars: two-repo studio mission, the
integrity/legal floor — original-only homebrew · patches-not-ROMs ·
reproducible builds · emulator-verified "it plays" — one-PR-one-repo,
continuous Q-0265 + volume-first Q-0266) and §2 (coordinator brief: boot
order, ORDER 000 toolchain + walking skeleton, the `50 */2` failsafe arm
step whose prompt the deployed trigger matches byte-for-byte, queued arcs).
**No `instructions.md`/`coordinator-prompt.md` copies are created here:**
the running Project's Custom-Instructions field and the live coordinator
prompt have NO committed twin in any readable registry — what was actually
pasted owner-side is invisible; the founding §1/§2 at the SHA above are the
only committed candidates. (The per-repo packages `projects/gba-homebrew/`
and `projects/pokemon-mod-lab/` carry their own pre-seat instruction drafts
— never deployed, see their metas.)

## Deployed-state per part (2026-07-11 sweep)

| Part | Deployed state |
|---|---|
| `instructions.md` | **not created — deliberate.** Deployed field content unknown (no paste receipt); founding §1 committed at superbot `10a7486` (pointer above). Creating a copy here without a paste receipt would imply a deployment record that does not exist |
| `coordinator-prompt.md` | **not created — deliberate.** The running coordinator-session prompt is not stored in any readable registry; founding §2 committed at superbot `10a7486` (pointer above) |
| `setup-script.sh` | **ABSENT — deliberately not created.** Founding §0/§3 call for a retro-toolchain env (gba-homebrew's proven session-7 setup + a ROM-patch tool; explicitly NOT plain python-lab); no paste receipt exists for what the owner actually put in the `superbot-retro` env's Setup-script field. The consolidated lineage (`environments/archetype-gba-lab.sh` + fm PR #73's R3 disposition: xdelta3 in the apt baseline, devkitARM pull gated behind homebrew detection) is the registry's candidate — deployed-state **unknown** |
| `failsafe-prompt.md` | **DEPLOYED + REGISTRY-VERIFIED** — stored prompt captured VERBATIM-FROM-REGISTRY (extraction 2026-07-11T13:17:24Z), byte-checkable, byte-identical to founding §2 step 3 |
| `triggers.md` | **DEPLOYED + REGISTRY-VERIFIED** — both hourly child-lane wake records (gba `0 * * * *` + pokemon `30 * * * *`), stored prompts VERBATIM-FROM-REGISTRY (same extraction) |
| `meta.md` | this file (first version — no prior stub existed for this seat) |

## Sources (all read/verified this build, 2026-07-11)

- Live trigger registry: `list_triggers` full 549-record extraction
  2026-07-11T13:17:24Z — failsafe + both hourly wakes (ids, crons, session/
  env bindings, sources, timestamps, stored prompts verbatim); negative
  finding: zero "superbot-retro chain link" one-shots in the sweep.
- Repo absence: GitHub MCP `search_repositories` exhaustive `superbot*`
  listing under menno420 (6 repos, `incomplete_results: false`) + the
  session-scope denial text of the direct probe (both captured verbatim).
- superbot PR #1972 (MERGED 2026-07-11T01:09:06Z, squash `10a7486a49c…`):
  `docs/planning/round3-founding-package-games-retro-2026-07-11.md` fetched
  verbatim at the merge SHA.
- fleet-manager: `projects/gba-homebrew/meta.md` + all four gba/pokemon
  package parts (2026-07-10 state, for the staleness delta) ·
  `projects/README.md` doctrine · `docs/roster.md` gen #4/#5 (the "retro
  coordinator with NO repo" first sighting).

## Merge-authority supersession note (2026-07-11, ORDER 017)

Merge authority for both child repos is governed by the corrected UNIVERSAL
v4 clause (PR #76, owner-merged, @ `e1848ff`) as carried in
`projects/gba-homebrew/instructions.md` v2 + `projects/pokemon-mod-lab/
instructions.md` v2 (park READY+green; never arm/REST-merge your own PR;
silent-fire self-check rider for the hourly fresh-fire wakes). The seat's
stored wake prompts (failsafe-prompt.md + triggers.md, VERBATIM-FROM-REGISTRY)
predate v4 and are deliberately NOT edited here — editing them without
re-arming would break the byte-match invariant. ⚑ FLAGGED FOLLOW-UP (retro
seat or coordinator): re-arm the triggers with corrected prompt text
(delete_trigger + create_trigger), then regenerate both files from the new
registry records.

**Last verified:** 2026-07-11 (trigger registry 13:17:24Z). Family-level
model names only (Q-0262.4).
