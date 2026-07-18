<!-- v3.7 · 2026-07-18 · fleet-manager projects registry -->
# websites — Project package meta

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

## Deployed-state per part (2026-07-18)

| Part | State |
|---|---|
| `instructions.md` (Custom Instructions) | v3.7 · 2026-07-18 · registry-current; deployed console paste predates the registry — owner re-paste to v3.7 is the self-heal item (not repo-verified) |
| `coordinator-prompt.md` (coordinator / wake prompt) | v3.7 · 2026-07-18 · registry-current; owner re-paste to v3.7 pending (self-heal; not repo-verified) |
| `failsafe-prompt.md` | v3.7 · 2026-07-18 · registry-current; failsafe byte-state via the triggers snapshot |

<details><summary>Prior per-part deployment detail (pre-restamp, historical)</summary>

- `instructions.md` — **DEPLOYED, but an OLDER text**: the fm gen-2 fitted version (7,496 chars) was pasted 2026-07-10 (~02:05Z), which predates the registry AND the repo's own `docs/project/` package. No paste record exists for the repo file itself. Re-paste needed. (fm `docs/proposals/instructions/websites.md` §"Deployed fitted version" L324 @ `0eaa668`; websites `docs/project/README.md` @ `fc8354e`.)
- `coordinator-prompt.md` (= wake prompt for this fresh-session lane) — **NOT the deployed text** as of the last record: live trigger carried an older "standing inbox ritual" delegating prompt (paraphrase only). Owner may have re-pasted — **UNVERIFIED**; a fired session's behavior is the test. (websites `docs/owner/OWNER-ACTIONS.md` row E @ `fc8354e`; `docs/project/routine-prompt.md` banner @ `fc8354e`.)
- `setup-script.sh` — owner-paste convention, **no paste record**; which text the console env field holds is unverified. (websites `docs/project/README.md` + inventory-lanes §1; fm `environments/archetypes.md` websites row @ `0eaa668`.)
- `failsafe-prompt.md` (wake cron) — **DEPLOYED trigger verified in registry** (`trig_017H9Qb9oxtLgUy6sw2gnSHg`, `0 */4 * * *`, fresh-session, first fire 16:01:32Z) but its prompt text predates the registry per the last committed record and is **UNVERIFIED since**. (websites `docs/owner/OWNER-ACTIONS.md` row E; `docs/CAPABILITIES.md` append log 2026-07-10.)

</details>

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
