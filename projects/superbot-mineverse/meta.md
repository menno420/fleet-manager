<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# superbot-mineverse — Project package meta (mining-browsergame seat)

> **v1, registry centralization (registry doctrine, same shape as ORDER 015):
> the seat SELF-BOOTED 2026-07-11, so this package is SWEPT from what
> verifiably exists and runs (live trigger registry, extraction
> 2026-07-11T13:17:24Z + repo state at `4be012e` + the founding texts merged
> in superbot PR #1972 @ `10a7486`), not authored aspirationally.** Where a
> part was never deployed or has no committed twin, its row SAYS so
> explicitly. This closes the "LIVE seat with no `projects/` package" gap
> (the seat was born after the 2026-07-10 package-centralization pass).

| Field | Value |
|---|---|
| Seat | **Mining-browsergame seat — LIVE, fully active.** Repo `menno420/superbot-mineverse` (public, created 2026-07-11T01:14:30Z, description "webbrowsergame linked to bots game"); seeded born-right kit v1.8.0 (root commit `d1d8c9f`, "seed: substrate-kit v1.8.0 born-right adopt --wire-enforcement"); booted from the superbot founding package `docs/planning/round3-founding-package-mining-web-2026-07-11.md` (merged in superbot PR #1972, squash SHA `10a7486a49c5b44d2db5f414fddb0321e63b4ebb`, 2026-07-11T01:09:06Z). At origin/main `4be012e65a0b8da292143bb1a07ffe22db2ceb26`: **~30 PRs merged in ~9h** — walking skeleton → read contract v1 → Discord OAuth → write contract v1 (test-guild shim) → live-prod cutover prep → full v1-contract view coverage → ORDERs 001+002 done; 191 pytest tests + 1 conditional skip per the seat's status; heartbeat 2026-07-11T10:24:00Z |
| Coordinator session | `session_017yrng4qx2LcLNqKb5AGoe8` (boot session cse_017yrng4qx2LcLNqKb5AGoe8 per the seat's own heartbeat notes; the failsafe trigger is bound to this persistent session) |
| Cadence | Continuation chain (send_later links re-armed each wake; ~15 min normal, ~60 min while externally blocked — the seat's ROUTINE RECORD) as pacemaker + cron failsafe **`trig_01K8xmAKYS5S2HLy1HPANM7j`** "superbot-mineverse failsafe wake" **`20 */2 * * *`**, enabled, seat-armed 2026-07-11T01:30:43Z, registry-verified (`list_triggers` extraction 2026-07-11T13:17:24Z; stored prompt VERBATIM in `failsafe-prompt.md`). The registry also shows the seat's spent one-shot "superbot-mineverse chain link" triggers (20 between 01:32Z and 12:23Z) — the chain is demonstrably live |
| Orders | `control/inbox.md` @ `4be012e`: ORDER 001 (model-attribution relay, P3) + ORDER 002 (self-review, P1) — **both DONE** (heartbeat `orders: acked=001,002 done=001,002`; ORDER 001 via mineverse PR #27, ORDER 002 via the Self-review 2026-07-11 status section) |
| CI / ruleset | `substrate-gate` required on `main` (seat-verified: PR #5's enabler job read the ruleset server-side; heartbeats ride the control-only fast lane). **pytest is NOT a required check** — evidenced live (PR #16 merged 28s before pytest finished); standing OWNER-ACTION 2 on the seat's status. Auto-merge WORKS in this repo (`auto-merge-enabler.yml` installed by the kit seed; e.g. PR #24 auto-merged on green) |
| Kit | **v1.8.0** at `4be012e` (heartbeat kit line: `kit: v1.8.0 · check: green · engaged: yes`) |
| Grants | Write: `menno420/superbot-mineverse` only (Q-0260). Read (oracle, public raw): superbot `disbot/services/mining_workflow.py` + `disbot/utils/mining/**` + mining views; superbot-next as it ports. Env vars: **none committed, six named** — DISCORD_OAUTH_CLIENT_ID, DISCORD_OAUTH_CLIENT_SECRET, OAUTH_REDIRECT_URI, WEB_SESSION_SIGNING_KEY, MINING_WRITE_ENDPOINT, MINING_WRITE_SHARED_SECRET are host-env-only, owner-provisioned (seat OWNER-ACTION 1); degraded mode until set, full test suite passes with zero env vars. Access path note: the GitHub MCP initially denied this repo ("not configured for this session"); `add_repo` → clone succeeded wall-free |
| Codex | Not in the 2026-07-11 ORDER 014 fleet-wide enablement list (that pass covered the 12 repos active at the time; this repo was hours old). **Deployed state: unknown — no probe on record.** Probe-once-per-seat applies (doctrine 6) |
| Open flags | Seat-side (carried verbatim on its heartbeat @ `4be012e`): **FLAG 1** (bot lane: READ relay projection per `schemas/mining_snapshot.v1.schema.json`) + **FLAG 2** (bot lane: HMAC-signed audited WRITE endpoint) — both await the superbot/Builder lane via the manager; **OWNER-ACTION 1** (six host env vars) + **OWNER-ACTION 2** (make pytest a required check). Ladder state: 0 ✓ · a ✓ · b ✓ · c ✓ web-side · d PREPARED — live-prod stays OWNER-FLAG-GATED, never agent-decided |

## Deployed-state per part (2026-07-11 sweep)

| Part | Deployed state |
|---|---|
| `instructions.md` | **CENTRALIZED COPY of the founding §1 paste block (superbot PR #1972 @ `10a7486`) — the running Custom-Instructions field has NO committed twin.** No paste receipt exists in any registry we can read; whatever the owner actually pasted owner-side is invisible to the fleet. The founding §1 text is the only committed candidate for what was pasted; the copy here states that explicitly rather than inventing a canonization |
| `coordinator-prompt.md` | **CENTRALIZED COPY of the founding §2 coordinator brief (superbot PR #1972 @ `10a7486`) — the running coordinator-session prompt is not stored in any readable registry.** The live session (`session_017yrng4qx2LcLNqKb5AGoe8`) booted from a paste of this brief (its behavior — ORDER 000, trigger name/cron, staged ladder — matches it exactly), but the actual pasted text has no committed record |
| `setup-script.sh` | **ABSENT — deliberately not created.** The founding §3 specifies `archetype-python-lab.sh` verbatim by reference; no paste receipt exists and the console field is owner-side-invisible. Per R4 (fm PR #73) the per-project setup-script probe variants are retired to the one `environments/` lineage anyway — a new per-seat script here would recreate the retired class. Deployed-state: **unknown (by-reference presumed, unverified)** |
| `failsafe-prompt.md` | **DEPLOYED + REGISTRY-VERIFIED** — stored trigger prompt captured VERBATIM-FROM-REGISTRY (extraction 2026-07-11T13:17:24Z), byte-checkable (no in-band stamp per registry doctrine 3). Seat-armed at boot; the seat's own status carries the arming record |
| `meta.md` | this file (first version — no prior stub existed for this seat) |

## Sources (all read/verified this build, 2026-07-11)

- Live trigger registry: `list_triggers` full 549-record extraction
  2026-07-11T13:17:24Z (trigger id, cron, session binding, timestamps, stored
  prompt verbatim; plus the 20 "superbot-mineverse chain link" one-shots).
- superbot-mineverse @ origin/main `4be012e65a0b8da292143bb1a07ffe22db2ceb26`
  (full history via add_repo → clone → fetch --unshallow): root `README.md`
  (lane contract, staged-ladder table) · `control/status.md` (heartbeat
  10:24:00Z, ROUTINE RECORD verbatim, OWNER-ACTIONs 1–2, FLAGs 1–2,
  Self-review 2026-07-11) · `control/inbox.md` (ORDERs 001+002) ·
  `control/README.md` + `control/claims/README.md` (kit-standard protocol) ·
  commit log (root seed `d1d8c9f` → `4be012e`, ~30 merged PRs).
- superbot PR #1972 (MERGED 2026-07-11T01:09:06Z, squash `10a7486a49c…`):
  `docs/planning/round3-founding-package-mining-web-2026-07-11.md` fetched
  verbatim at the merge SHA.
- fleet-manager: `projects/README.md` doctrine · fm PR #73 (`cf2c4ee`, R4
  setup-script retirement) · `docs/roster.md` gen #5.

**Last verified:** 2026-07-11 (superbot-mineverse HEAD `4be012e`; trigger
registry 13:17:24Z). Family-level model names only (Q-0262.4).
