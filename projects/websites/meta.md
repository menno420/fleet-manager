# websites — Project package meta

> **Restamp 2026-07-12:** the sibling package files (`instructions.md` /
> `coordinator-prompt.md` / `failsafe-prompt.md`) are GENERATED COPIES
> serving **prompts v3.3** (generated from `docs/prompts/v3` @ `48650f8`;
> v3.3 generation on main @ `98d0f68`) — under the v3 generation the lane
> moves off the fresh-session-per-fire model to the uniform self-bind
> pattern. Lane state as of 2026-07-12 — verify at HEAD: the Q-0265
> continuous-mode chain is **PARKED** (owner archive-prep order; lane
> heartbeat `control/status.md` updated 2026-07-11T19:49:00Z, phase CLOSING,
> health green) while the repo still lands work (HEAD `869cb76`,
> 2026-07-12T13:50:06Z). That heartbeat records the 4-hourly wake trigger as
> staying armed, but `trig_017H9Qb9oxtLgUy6sw2gnSHg` is ABSENT from the later
> committed registry snapshot (fm `telemetry/triggers-snapshot.json`,
> exported 2026-07-12) — no websites trigger appears there; re-arm rides the
> v3.3 deployment sitting (owner-queue C#34–C#36).

- **Seat:** post-core lane (not one of the Q-0261 core six) — **LIVE**, and
  websites is the fleet's only lane running **fresh-session-per-fire** with no
  persistent coordinator seat. Gen-2 Project relaunched 2026-07-10 (fitted
  Custom Instructions pasted; fm `docs/proposals/instructions/websites.md`
  §Deployed); wake routine self-armed same day under ORDER 008 (websites
  `docs/owner/OWNER-ACTIONS.md` row E @ `fc8354e`; first fire confirmed
  2026-07-10T16:01:32Z). Uniquely, the lane ALREADY kept its own package
  in-repo at `docs/project/` — the fleet's model (inventory-lanes §1 "THE
  MODEL") — so this registry package is a canonicalization of that dir, not a
  new draft.
- **Cadence:** deployed `0 */4 * * *` (trigger `trig_017H9Qb9oxtLgUy6sw2gnSHg`,
  fresh-session-per-fire) · **recommended `0 */2 * * *`** per the gen-3 lane
  stagger (superbot `docs/planning/gen3-deployment-standard-2026-07-10.md` §2
  @ `53fb5ef`) — recommendation only; 4-hourly is legitimate maintenance-lane
  pacing (fm `docs/gen2-blueprint.md` §2a doctrine survives Q-0265 for bounded
  lanes). No separate failsafe trigger: with no persistent seat, the cron is
  the pacemaker (see failsafe-prompt.md).
- **Environment archetype:** `fleet-manager environments/archetype-pinned-research.sh`
  (fm `environments/archetypes.md` @ `0eaa668`: archetype table row
  "pinned-research … trading-strategy, websites"; per-repo row L54:
  menno420/websites → pinned-research, THREE requirements files
  (root/botsite/dashboard) installed individually, container 3.11.x vs
  production Dockerfiles 3.12 — never assume 3.12 locally; env-var NAMES
  `GITHUB_PAT`, `RAILWAY_API_KEY`, `SITE_PASSWORD`, `DATABASE_URL`, optional
  `AUTOREFRESH_SECONDS`/`PORT`; **DENYLISTED:** the Railway trio
  `RAILWAY_PROJECT_ID`/`RAILWAY_ENVIRONMENT_ID`/`RAILWAY_SERVICE_ID`,
  CI-enforced by `scripts/check_no_ambient_railway_ids.py`). The package's
  `setup-script.sh` is the lane's bespoke console text (capability probes);
  the archetype is the fleet standard — assembler/owner picks one lineage for
  the console field.
- **Grants:** `menno420/websites` only (Q-0260 single-writable-repo). Cross-repo
  reads are UNAUTHENTICATED raw fetches, not grants: sessions read
  fleet-manager and superbot over raw.githubusercontent.com — fleet-manager
  is verified anonymously readable (websites `docs/CAPABILITIES.md` append log
  2026-07-10 @ `fc8354e`, corrected finding), and the websites architecture
  itself mandates "cross-repo data arrives only as committed JSON read over
  raw.githubusercontent.com (read-only, forward-only)" (websites
  `.claude/CLAUDE.md`). Session-side `api.github.com` stays 403-gated to
  ungrained repos (the add_repo wall — same append log). Variables: names
  above; no secret values anywhere in the package.
- **Codex: ENABLED (owner, 2026-07-11)** — Codex environments exist for all
  12 active fleet repos, websites included (owner update 2026-07-11 ~00:2xZ,
  fm inbox ORDER 014); supersedes the 2026-07-10 "unknown" verdict. Quota
  refusals are RETRY-LATER, never a wall (fm `projects/README.md` § Codex
  fleet-wide enablement).

## Deployed-state per part (2026-07-10 snapshot — historical)

> **Restamp 2026-07-12:** dated build-time snapshot, kept as provenance.
> Superseded since: package files serve prompts v3.3 (banner above); row 4's
> deployed trigger `trig_017H9Qb9oxtLgUy6sw2gnSHg` is absent from the
> 2026-07-12 committed registry snapshot; the lane chain is PARKED per the
> owner archive-prep order. Verify at HEAD.

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — repo `docs/project/project-instructions.md` body @ `fc8354e` + the one Q-0265 fix (§ROUTINE-FIRED "ONE bounded slice" → work loop); body 6,989 chars | **DEPLOYED, but an OLDER text:** the fm gen-2 fitted version (7,496 chars) was pasted 2026-07-10 (~02:05Z) — that is pre-Q-0265 AND pre-dates the repo's own `docs/project/` package (written after the 16:01Z incident). No paste record exists for the repo file itself. **Re-paste needed** with this package's text | fm `docs/proposals/instructions/websites.md` §"Deployed fitted version" L324 @ `0eaa668` (in-file L3 "PROPOSED" badge is stale vs its own §Deployed — inventory-hub §A row 1); websites `docs/project/README.md` @ `fc8354e` (paste convention, no receipt) |
| 2 wake prompt (= coordinator prompt for this fresh-session lane) | `coordinator-prompt.md` v3 (slice-2 re-sync, 2026-07-11 — Ideas Lab naming; lineage: repo `routine-prompt.md` v2 → ORDER 017 re-issue) + fresh-session send_later caveat | **NOT the deployed text** as of the last record: live trigger carries the v1-era "standing inbox ritual" delegating prompt (paraphrase only — verbatim uncommitted). Owner may have re-pasted v2 — **UNVERIFIED**; a fired session's behavior is the test (v2 = works the loop, cites Q-0265) | websites `docs/owner/OWNER-ACTIONS.md` row E @ `fc8354e`; `docs/project/routine-prompt.md` v2 banner @ `fc8354e`; inventory-lanes §1 routine-prompt row |
| 3 setup script | `setup-script.sh` — `docs/project/setup-script.sh` @ `fc8354e` verbatim + registry note picking it canonical over the `scripts/setup-env.sh`+`env-setup.sh` lineage (retirement candidate for the lane) | Owner-paste convention, **no paste record** — which text (if either) the console env field holds is unverified; the archetype script is a third possible occupant | websites `docs/project/README.md` + inventory-lanes §1 "Missing (d)" (dual lineage); fm `environments/archetypes.md` websites row @ `0eaa668` |
| 4 wake cron text | `failsafe-prompt.md` v2 — prescribes the v3 prompt + `0 */2` recommended (4-hourly kept legitimate) | **DEPLOYED trigger verified in registry** (`trig_017H9Qb9oxtLgUy6sw2gnSHg`, `0 */4 * * *`, fresh-session, first fire 16:01:32Z) but its **prompt text is v1-era per the last committed record and UNVERIFIED since** (possible owner re-paste of v2 — unrecorded) | websites `docs/owner/OWNER-ACTIONS.md` row E; `docs/CAPABILITIES.md` append log 2026-07-10 (trigger creation record 13:49:36Z); inventory-lanes §1 "Missing (a)/(c)" |

## Known drift this package fixes / flags

1. **Fixed in part 1:** `project-instructions.md` §ROUTINE-FIRED still carried
   v1 "ONE bounded slice" pacing after the same repo's routine-prompt went v2
   (inventory-lanes §1 flagged; Q-0265 provenance stamped inline). Lane should
   port the fix back to `docs/project/project-instructions.md`.
2. **Flagged for the lane:** dual setup-script lineage — retire/fold
   `scripts/setup-env.sh` + `scripts/env-setup.sh` per part 3's registry note.
3. **Flagged for the lane/owner:** commit the DEPLOYED trigger prompt verbatim
   (the only lane artifact that exists nowhere in git), then re-paste v2 and
   record it; optionally retune to `0 */2`.
4. **Flagged upstream (fleet-manager):** `docs/proposals/instructions/websites.md`
   L3 badge still says "PROPOSED, not deployed" — stale vs its own §Deployed.

## Sources

- websites @ `fc8354e` (origin/main; inventory was cut at `4056909` —
  `docs/project/` is byte-identical between the two, diff-verified this
  session): `docs/project/{README,project-instructions,routine-prompt}.md` ·
  `docs/project/setup-script.sh` · `docs/owner/OWNER-ACTIONS.md` row E ·
  `docs/CAPABILITIES.md` (2026-07-10 append log: 16:01Z stranded session,
  403 verbatim, trigger creation, no-PR-tooling wall, fleet-manager
  anonymous-read correction) · `scripts/setup-env.sh` + `scripts/env-setup.sh`
  (second lineage) · `.claude/CLAUDE.md` (architecture / raw-read rule).
- fleet-manager @ `0eaa668` (origin/main): `docs/proposals/instructions/websites.md`
  (§Deployed fitted L324, 7,496 chars, pasted 2026-07-10; 8,000-char cap
  discovery) · `environments/archetypes.md` (pinned-research row, websites
  env-var names, Railway-trio denylist) · `environments/archetype-pinned-research.sh` ·
  `docs/gen2-blueprint.md` (Q-0265 amendment banner; §2a maintenance doctrine).
- superbot @ `53fb5ef`: `docs/planning/gen3-deployment-standard-2026-07-10.md`
  §2 (lane stagger `0 */2`, born-continuous operating model) ·
  `docs/planning/round3-dispatch-part4-brief-2026-07-10.md` §2b (Q-0265
  amendment template) · router Q-0264 / Q-0265.
- Inventories (scratchpad `launch-packages/`): inventory-lanes.md §1 (THE
  MODEL + Missing (a)–(d)) + missing-parts matrix; inventory-hub.md §A row 1,
  §C (env registry), §F (gen-3 standard).

**Last verified:** 2026-07-10 (all repo citations `git show`n from freshly
fetched origin/main this session; trigger facts are the repo's committed
records — the live registry was NOT re-queried this session).
**Restamped 2026-07-12** (lane state re-verified: websites HEAD `869cb76`
2026-07-12T13:50:06Z + `control/status.md` updated 2026-07-11T19:49:00Z;
trigger facts from fm `telemetry/triggers-snapshot.json` exported 2026-07-12).
