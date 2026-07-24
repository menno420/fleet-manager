# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #197** · generated-at **2026-07-24T11:20Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready…

- suggested-id: `OQ-SUPERBOT-HUB-SIDE-RESIDUE-ONLY`
- source: superbot/control/status.md @ `b20cf04` · heartbeat `updated:` 2026-07-13T18:00:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready when deploy timing suits (CodeQL resolved by code change; merge=deploy Q-0193); the fleet-wide owner queue is consolidated in docs/eap/night-review-2026-07-13.md §7 (canonical: fm docs/owner-queue.md). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `617f34b` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### websites — ⚑ needs-owner: the ⚑ rows in docs/owner/OWNER-ACTIONS.md (canonical list there; unchanged at close).

- suggested-id: `OQ-WEBSITES-ROWS-DOCS-ACTIONS-MD`
- source: websites/control/status.md @ `6960299` · heartbeat `updated:` 2026-07-21T21:11:34Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: the ⚑ rows in docs/owner/OWNER-ACTIONS.md (canonical list there; unchanged at close).
```

### superbot-games · Seat A — ⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded re…

- suggested-id: `OQ-SUPERBOT-GAMES-4-STANDING-DECISIONS-NONE`
- source: superbot-games/control/status.md @ `9332400` · heartbeat `updated:` 2026-07-14T11:41:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded recommendations + VERIFY steps) is docs/eap-closeout-walkthrough-2026-07-14.md §C, surfaced verbatim in control/outbox.md § EAP CLOSE-OUT: (1) D2 audit-grants ratification · (2) rung-3 packaging/hermeticity · (3) persistence format-governance (3 sub-decisions) · (4) transfer-policy source model. RISK: all four are ↩️ reversible decision replies; no destructive click owed.
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `9332400` · heartbeat `updated:` 2026-07-09T20:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: |
  NOTHING BLOCKING. Gen-2 relaunch clicks (optional, in order):
  (1) paste the proposed gen-2 Custom Instructions from
  docs/gen2-custom-instructions-exploration.md §B into the relaunched Project (agents
  cannot edit Project settings); (2) create the wake routine — relaunch starts Class A
  hourly per the lane's gen-2 feedback §3 (the measured ORDER-005 pickup without a
  routine was ~2h); (3) branch-deletion housekeeping (agents 403 on branch delete):
  claude/exploration-ping-ack-005, claude/exploration-wind-down-2026-07-09 (after #13
  merges), claude/exploration-wakeup-2026-07-09, plus the older merged branches listed
  in docs/retro/project-review-2026-07-09-exploration.md §e — do NOT delete
  mining/port-pure-domain or mining/grid-encounters (live mining drafts #5/#11);
  (4) the #13 merge click ONLY IF this session's own merge-on-green failed (the PR
  records the exact error if so). Standing veto windows unchanged: D‑0007 (Q-0040
  posture, open until the P3→P4 gate), D‑0009 (CI gate; revert = veto).
```

### superbot-idle (Seat B) — ⚑ needs-owner: OA-003 — WHAT: add `pytest` as a required status check on main. WHERE: https://github.com/menn…

- suggested-id: `OQ-SUPERBOT-IDLE-OA-003-WHAT-ADD`
- source: superbot-idle/control/status.md @ `8cea5bf` · heartbeat `updated:` 2026-07-17T10:26:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: OA-003 — WHAT: add `pytest` as a required status check on main. WHERE: https://github.com/menno420/superbot-idle/settings/branches → `main` protection rule → required status checks. HOW: add `pytest` alongside `substrate-gate` + `theme-gate` (click only). RISK: ✅ safe · ↩️ reversible (uncheck to undo). WHY-IT-MATTERS: until then a PR can merge with the test suite red (GREEN ≠ TESTED). UNBLOCKS: merge-on-green becomes trustworthy for every future PR. VERIFIED-NEEDED: branch-protection settings are owner/admin-only — standing since PR #74 (OA-003); agent sessions hold no repo admin scope. Full pending-decision list with recommendations: docs/eap-closeout-walkthrough-2026-07-14.md § C.
```

### superbot-idle (Seat B) — - ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-p…

- suggested-id: `OQ-SUPERBOT-IDLE-MANAGER-NO-LONGER-BLOCKER`
- source: superbot-idle/control/status.md @ `8cea5bf` · heartbeat `updated:` 2026-07-17T10:26:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### product-forge — ⚑ OWNER-ACTION (OA-004, open) — **playtest the controller on real hardware** (the one

- suggested-id: `OQ-PRODUCT-FORGE-OA-004-OPEN-PLAYTEST`
- source: product-forge/control/status.md @ `b9a0593` · heartbeat `updated:` 2026-07-24T10:55:37Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION (OA-004, open) — **playtest the controller on real hardware** (the one
step CI cannot prove; ~5 min, two Android devices):
1. Install the APK (Releases page, or the CI-run artifact) on the controller phone.
2. Open it → grant Nearby devices → status shows the capability verdict.
3. Tap Discoverable → pair from the target device → "Connected — controller is live".
4. Open an emulator on the target; Gamepad pad should show up as a controller
   (Keys pad = keyboard fallback). Hold a D-pad direction: movement must HOLD.
VERIFIED-WHEN: one full session driving an emulator; report the phone model + verdict
code (an `OEM_DISABLED` phone is the engine working as designed — try another phone).
```

### product-forge — ⚑ RESOLVED 2026-07-24 (OA-005, was owner-optional; executed agent-side under the

- suggested-id: `OQ-PRODUCT-FORGE-RESOLVED-2026-07-24`
- source: product-forge/control/status.md @ `b9a0593` · heartbeat `updated:` 2026-07-24T10:55:37Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ RESOLVED 2026-07-24 (OA-005, was owner-optional; executed agent-side under the
live "please continue" directive) — **stable release signing is configured**: repo
secrets `PC_RELEASE_KEYSTORE_B64` + `PC_RELEASE_KEYSTORE_PASSWORD` set via
direct-egress REST (sealed-box encrypt; the Slice-4 PKCS12 keystore, alias
`phone-controller`); v0.9.0 re-signed with it via workflow_dispatch. Updates now
install in place from v0.9.0 onward (one final uninstall when coming from
ephemeral-signed ≤v0.8.0). Keystore lives ONLY in the repo secret.
```

### product-forge — ⚑ OWNER-ACTION (OA-003, open, unchanged) — GitHub Pages toggle for games-web preview

- suggested-id: `OQ-PRODUCT-FORGE-OA-003-OPEN-UNCHANGED`
- source: product-forge/control/status.md @ `b9a0593` · heartbeat `updated:` 2026-07-24T10:55:37Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION (OA-003, open, unchanged) — GitHub Pages toggle for games-web preview
(Settings → Pages → Source → "GitHub Actions"); deploy-pages runs 29126980391 /
29128667052 failed at configure-pages until enabled.
```

### idea-engine — ⚑ needs-owner: none — run closing; the prior EAP-era ask is withdrawn at closeout (see docs/PROJECT-CLOSEOUT.…

- suggested-id: `OQ-IDEA-ENGINE-NONE-RUN-CLOSING-PRIOR`
- source: idea-engine/control/status.md @ `c69d85a` · heartbeat `updated:` 2026-07-21T17:17:40Z · project closeout in progress — loop …
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: none — run closing; the prior EAP-era ask is withdrawn at closeout (see docs/PROJECT-CLOSEOUT.md for the final state and continuation).
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `2071c7b` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

---

12 candidate block(s) across 9 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

