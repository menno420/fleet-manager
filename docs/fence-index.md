# Fleet fence-exposure index — which repos expose which seat-digest fences

> **Status:** `reference`
>
> Central-docs-plan **C13** ("CONFIRM fm as registered consumer — document
> the consumer half centrally; index which repos expose which fences"),
> landed 2026-07-14 (wake 0434z, PR #185). The extraction contract itself is
> documented producer-side in every adopter's generated `docs/seat-digest.md`
> and consumer-side in **`docs/prompts/v3/tools/seat_digest_sync.py`** — the
> registered consumer (tree scan + fence-prefix match + byte compare, never
> executing kit code). This file is the per-repo exposure snapshot the
> contract docs don't carry.
>
> **Dated snapshot** — probed 2026-07-14T04:58Z over
> `raw.githubusercontent.com` (HEAD of each repo's main). Re-probe before
> acting on a row (one curl per repo; recipe at the bottom). Decide-and-flag:
> kept as a dated hand-probe for now — mechanizing it into `gen_roster.py`
> is a natural follow-up once the row set stabilizes.

## The three fences (contract: kit `src/engine/grammar.py`, vendored in the consumer)

| fence | lives in | feeds |
|---|---|---|
| `substrate-kit:skills-digest` | `docs/seat-digest.md` | seat-prompt skill blocks |
| `substrate-kit:walls-digest` | `docs/seat-digest.md` | seat-prompt wall blocks (venue-filtered) |
| `substrate-kit:capability-seed` | `docs/CAPABILITIES.md` | kit-refreshed seed section (upgrade-managed) |

## Exposure by repo (probed 2026-07-14)

| Repo | `docs/seat-digest.md` (skills+walls fences) | `capability-seed` fence in `docs/CAPABILITIES.md` | Note |
|---|---|---|---|
| fleet-manager | ✅ exposed | ✅ present | fm's own source; consumer selftest target |
| superbot-next | ✅ exposed | ✅ present | |
| websites | ✅ exposed | ❌ absent | walls live un-fenced → digest under-reports (INC-48 class) |
| trading-strategy | ✅ exposed | ✅ present | |
| venture-lab | ✅ exposed | ❌ absent | INC-48 class (walls in PLATFORM-LIMITS, digest empty) |
| superbot-games | ✅ exposed | ✅ present | |
| superbot-idle | ✅ exposed | ✅ present | |
| superbot-mineverse | ✅ exposed | ✅ present | |
| gba-homebrew | ✅ exposed | ✅ present | |
| idea-engine | ✅ exposed | ✅ present | |
| sim-lab | ✅ exposed | ❌ absent | INC-48 named case — real walls in `PLATFORM-LIMITS.md` (mirrored to the fm master 2026-07-14, B3); digest renders "(no walls recorded)" |
| superbot | ❌ no digest file | ❌ absent | kit deliberately pinned v1.0.0 (INC-41) — pre-digest generation |
| substrate-kit | ❌ no digest file | ❌ absent | the kit's self-hosting repo; generates the contract, doesn't consume it |
| product-forge | ❌ no digest file | ❌ absent | kit v1.7.0 lag; archive-bound (E#44) |
| pokemon-mod-lab | NOT MEASURED | NOT MEASURED | private repo — unauthenticated raw returns 404 (a wall, never absence; ROSTER_READ_TOKEN pending) |

Reading: an "❌ absent" capability-seed with an exposed digest is the B4 /
INC-48 lane-side fold class — the digest's walls block extracts from the
fenced `CAPABILITIES.md` section, so an un-fenced ledger renders an empty
walls digest while real walls sit elsewhere. Those folds are lane writes,
routed via inbox ORDERs (plan Phase 1 B4), never fixed from here.

## Re-probe recipe

```bash
for r in <repos>; do
  curl -s https://raw.githubusercontent.com/menno420/$r/main/docs/seat-digest.md \
    | grep -c "substrate-kit:.*-digest BEGIN"
  curl -s https://raw.githubusercontent.com/menno420/$r/main/docs/CAPABILITIES.md \
    | grep -c "substrate-kit:capability-seed BEGIN"
done
```

Consumer drift guard (structure + byte-match, run any time):
`python3 docs/prompts/v3/tools/seat_digest_sync.py --check`
