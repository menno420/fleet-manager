# venture-lab — Project package meta

- **Seat:** revenue lane, POST-CORE (Q-0261.4 pipelined path — not one of the
  core six). Owner mandate: profitability to fund the fleet (Q-0259.4).
- **Lane state: LIVE-BUT-DARK — the riskiest lane state in the fleet.** The
  repo is active (PRs #2–#9 merged; #9 squash `95b755b` 05:11:50Z put the
  sellable buyer zips on main) but the lane has NO CLOCK (`list_triggers`
  shows no venture-lab trigger — fm `docs/launch-readiness-2026-07-10.md`
  §"Gap found live") and its heartbeat is STALE at 2026-07-10T04:57:30Z
  (`control/status.md` @ `a22b403` still says "PR #9 awaiting owner merge" —
  false since 05:11Z). Three ORDERs sit unexecuted at `control/inbox.md` @
  `f999ddf`: 002 (self-arm), 003 (P0 Stripe real-path fix — the ⚑B/⚑D
  unfreeze gate), 004 (archive-ender, names itself the fresh boot's task).
  Launch-readiness verdict: "sharpest state-risk in the fleet: the heartbeat
  the fresh Project reads is stale-by-design until ORDER 004 executes."
- **Cadence:** `0 */2 * * *` (gen-3 standard lane stagger). Under Q-0265 the
  cron is the dead-man failsafe; the send_later ~15-min chain is the
  pacemaker. NOT ARMED — arming rides the fresh boot (parts 2 + 4).
- **Environment archetype:** **python-lab**
  (`fleet-manager environments/archetype-python-lab.sh` verbatim) —
  archetypes.md maps "menno420/venture-lab (planned) → python-lab, env vars
  *(none at launch)*; NO spend/account/publish vars without owner action;
  quality floor = substrate-kit". The package's `setup-script.sh` is the
  probe variant of that archetype for the console field; it probes env var
  NAME presence only (STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET,
  DISCORD_INVITE_URL, SUPABASE_URL, SUPABASE_KEY, STORE_BACKEND,
  MEMBERS_DB_PATH — from `candidates/membership-kit/server/.env.example`)
  and never echoes values. Real key values, when ⚑A lands, live in the
  owner's local `server/.env` / the claude.ai panel — never the repo.
- **Grants:** `menno420/venture-lab` only (Q-0260 single-writable-repo;
  cross-repo reads via raw). Variables: none at launch.
- **Codex: ENABLED (owner, 2026-07-11)** — Codex environments exist for all
  12 active fleet repos, venture-lab included (owner update 2026-07-11
  ~00:2xZ, fm inbox ORDER 014); supersedes the "unknown" cheap-check verdict.
  Review-queue row venture-lab#9 can now drain via @codex directly. Quota
  refusals are RETRY-LATER, never a wall (fm `projects/README.md` § Codex
  fleet-wide enablement).
- **Merge wall (lane-defining):** main requires PRs; `substrate-gate` is NOT
  a required check → PRs go `clean` instantly, auto-merge cannot arm; PR #9
  proved a green PR is agent-unlandable when no genuine-user authorization
  exists (two verbatim classifier denials recorded in `docs/PLATFORM-LIMITS.md`
  @ `4c1b1c2` + status). Package parts 1–2 carry REST merge-on-green as
  primary, first-denial-terminal refusal branch, and the agent-doable
  systemic fix (GITHUB_TOKEN merge-on-green workflow — launch-readiness
  recommendation (b)).
- **Duplicate-file flag (for the lane to fix on boot):** the repo carries
  BOTH `docs/CAPABILITIES.md` (3,472 B, kit-generated) and
  `docs/capabilities.md` (4,634 B, fleet-manifest copy carried at seed) — a
  case-collision drift risk (two capability ledgers can disagree; also breaks
  on case-insensitive filesystems). Queued as work-loop item (c) in part 2:
  merge into ONE ledger at the kit-convention path, update pointers.

## Deployed-state per part (2026-07-10)

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — Q-0265/Q-0264/Q-0259.4 re-base of the held gen-2 package | **NOTHING EVER DEPLOYED AS SUCH.** The gen-2 package was held per Q-0262.6 and never pasted; its predecessor `venture-lab-draft.md` also ❌ NOT deployed (fm prompts README). The lane has run on system-prompt identity + in-repo docs only — no Custom-Instructions paste record exists anywhere | fm `docs/proposals/instructions/venture-lab.md` @ `f28dd12` (badge: PROPOSED, not deployed); fm `docs/prompts/README.md` row; inventory-hub §A row 3 + §B; inventory-lanes §4 |
| 2 coordinator prompt | `coordinator-prompt.md` v2 (slice-2 re-sync, 2026-07-11) — merged-seat brief (venture-lab + trading-strategy research annex): state-repair boot at HEAD, trigger cutover, profitability work loop | **NOT deployed** — no seat prompt has ever existed for this lane (no succession/boot brief on main, verified by the launch-readiness sweep; ORDER 004 orders one written) | fm `docs/launch-readiness-2026-07-10.md` §9; `control/inbox.md` ORDER 004 @ `f999ddf` |
| 3 setup script | `setup-script.sh` — python-lab archetype + probe block + Stripe name-only probes | **NOT deployed** — no setup script exists anywhere in the venture-lab repo (inventory missing-parts matrix: ❌); what the console env field holds is unverifiable from in-repo (no paste record) | inventory-lanes §4 + matrix; fm `environments/archetypes.md` venture row |
| 4 failsafe text | `failsafe-prompt.md` v2 (slice-2 re-sync, 2026-07-11) — merged-seat text, `0 */2 * * *`; cutover retires the old trading-strategy failsafe | **NOT ARMED** — lane is clockless; ORDER 002 unexecuted; no trigger in the registry. Arming rides the fresh boot | fm launch-readiness §"Gap found live" + §9; `control/inbox.md` ORDER 002 @ `f999ddf`; `control/status.md` @ `a22b403` (no routine record) |

## Sources

- venture-lab @ `ce22315` (origin/main): `control/status.md` @ `a22b403`
  (stale 04:57Z heartbeat · PR #9 blocker · ⚑A–D + systemic ⚑) ·
  `control/inbox.md` @ `f999ddf` (ORDERs 001–004) · `docs/PLATFORM-LIMITS.md`
  @ `4c1b1c2` (merge-wall record, two verbatim classifier denials) ·
  `.substrate/claude/CLAUDE.md` (kit-planted working agreement; no root
  `.claude/`) · `docs/CAPABILITIES.md` + `docs/capabilities.md` (the
  duplicate) · `candidates/membership-kit/server/.env.example` (env var
  names).
- fleet-manager @ `0eaa668` (origin/main, newer than the inventory's
  `702ba89` — files re-fetched at this HEAD): `docs/proposals/instructions/
  venture-lab.md` @ `f28dd12` (the held gen-2 package — re-base source) ·
  `docs/launch-readiness-2026-07-10.md` §9 (venture verdict BLOCKED-ON-5,
  frozen clicks, self-landable-path recommendation (b)) ·
  `environments/archetypes.md` (python-lab row) ·
  `environments/templates/env-vars.md` (names-only rule).
- superbot local @ `4fac759`: router Q-0259 ruling 4 (profitability mandate +
  money protocol, L9366–9370) · Q-0262 items 5 (OWNER-ACTION grammar —
  venture-lab conforms at next kit upgrade) + "not appliable" note
  (venture-lab ⚑A–D stay owner-only, frozen behind the P0 Stripe fix).
  Q-0264/Q-0265 text not present at this local HEAD — taken from the
  inventory baseline (sb @ `53fb5ef` L9511–9648) + the part-4 brief §2b.
- Inventories (scratchpad `launch-packages/`): inventory-lanes.md §4 +
  missing-parts matrix (venture-lab: all four parts ❌); inventory-hub.md
  §A row 3, §B, §C, §G.

**Last verified:** 2026-07-10 (venture-lab + fleet-manager files fetched from
origin/main this session; superbot router read locally at `4fac759`).
