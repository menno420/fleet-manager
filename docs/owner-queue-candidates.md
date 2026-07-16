# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #68** · generated-at **2026-07-16T10:30Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready…

- suggested-id: `OQ-SUPERBOT-HUB-SIDE-RESIDUE-ONLY`
- source: superbot/control/status.md @ `7e41586` · heartbeat `updated:` 2026-07-13T18:00:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready when deploy timing suits (CodeQL resolved by code change; merge=deploy Q-0193); the fleet-wide owner queue is consolidated in docs/eap/night-review-2026-07-13.md §7 (canonical: fm docs/owner-queue.md). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### substrate-kit — - ⚑ FOR OWNER REVIEW (carried forward): ORDER 024 says "do NOT re-arm routines yet; wait for the owner's per-…

- suggested-id: `OQ-SUBSTRATE-KIT-REVIEW-CARRIED-FORWARD-ORDER`
- source: substrate-kit/control/status.md @ `65cf519` · heartbeat `updated:` 2026-07-16T09:51:29Z · phase: SEAT CLOSING (EAP through 202…
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ FOR OWNER REVIEW (carried forward): ORDER 024 says "do NOT re-arm routines yet; wait for the owner's per-seat go". The enabled failsafe above (created 2026-07-16T01:09Z) post-dates that order. Recorded neutrally for owner review/veto; not adjudicated here. Kit-lab daily loop re-arm recipe: docs/operations/lab-loop.md.
```

### substrate-kit — ⚑ v1.18.0 adopter-wave authorization

- suggested-id: `OQ-SUBSTRATE-KIT-V1-18-0-ADOPTER`
- source: substrate-kit/control/status.md @ `65cf519` · heartbeat `updated:` 2026-07-16T09:51:29Z · phase: SEAT CLOSING (EAP through 202…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ v1.18.0 adopter-wave authorization
WHAT: authorize the v1.18.0 adopter-upgrade wave.
WHERE: the executing seat session, one live owner turn.
HOW: say 'run the v1.18.0 adopter wave'.
WHY: the seat session's permission classifier denied adopter-repo writes dispatched on coordinator relay alone (denial record verbatim: PR #420 body § "Denial routing"); owner provenance in the executing session is the unblock.
UNBLOCKS: ~15 adopter currency PRs to v1.18.0.
VERIFY: wave report with per-adopter PR list.
RISK: ↩️ reversible, distribution-only diffs.
```

### substrate-kit — ⚑ CAPABILITIES denial-record entry (parked)

- suggested-id: `OQ-SUBSTRATE-KIT-CAPABILITIES-DENIAL-RECORD-ENTRY`
- source: substrate-kit/control/status.md @ `65cf519` · heartbeat `updated:` 2026-07-16T09:51:29Z · phase: SEAT CLOSING (EAP through 202…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ CAPABILITIES denial-record entry (parked)
WHAT: approve appending the 2026-07-16 adopter-wave denial finding to docs/CAPABILITIES.md in summarized form (finding + date + pointer to the PR #420 body for the verbatim record).
WHERE: the executing seat session, one live owner turn.
HOW: say 'record the adopter-wave denial in CAPABILITIES, summarized'.
WHY: the CAPABILITIES discovery rule wants attempted walls appended same-session; the seat parked the append pending owner direction on form/placement.
UNBLOCKS: the can/cannot ledger stays complete for the successor.
VERIFY: a dated docs/CAPABILITIES.md entry pointing at PR #420.
RISK: ↩️ reversible, docs-only.
```

### substrate-kit — ⚑ P10 required-check swap

- suggested-id: `OQ-SUBSTRATE-KIT-P10-REQUIRED-CHECK-SWAP`
- source: substrate-kit/control/status.md @ `65cf519` · heartbeat `updated:` 2026-07-16T09:51:29Z · phase: SEAT CLOSING (EAP through 202…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ P10 required-check swap
WHAT: Swap which CI check main requires, from the two legacy names to the current one.
WHERE: repo Settings → Rules → the `main` ruleset → required status checks.
HOW: remove "Kit test suite" and "Cold-adoption smoke (adopt + check --strict)"; add `kit-quality` (source: GitHub Actions); set "Require branches to be up to date" OFF.
WHY: the legacy alias jobs exist purely to satisfy the old required names; the up-to-date requirement stalls green PRs `behind`.
UNBLOCKS: deleting the two legacy-alias jobs; ends the queue-stall class.
VERIFY: next kit PR shows kit-quality as the only required check; agent then removes the alias jobs.
RISK: ↩️ reversible — re-add the old required checks in the same ruleset panel.
```

### substrate-kit — ⚑ public-flip-or-PAT (pick one)

- suggested-id: `OQ-SUBSTRATE-KIT-PUBLIC-FLIP-PAT-PICK`
- source: substrate-kit/control/status.md @ `65cf519` · heartbeat `updated:` 2026-07-16T09:51:29Z · phase: SEAT CLOSING (EAP through 202…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ public-flip-or-PAT (pick one)
WHAT: Let the other fleet repos read this one — either make it public or mint a read-only token.
WHERE: P11: Settings → General → Danger Zone → Change visibility · P13: github.com/settings/tokens → fine-grained read-only PAT scoped to this repo, then add it to the fleet environments.
HOW: P11 is click-through; P13 is create-token + paste into environment settings.
WHY: sibling repos cannot read kit data today, so cross-repo sweeps and the merged console run blind.
UNBLOCKS: B2–B4 cross-repo sweeps + kit data in the merged console.
VERIFY: a sibling-seat session fetches a kit file read-only without "Access denied: repository … is not configured for this session".
RISK: ⚠️ P11 effectively irreversible (history exposed once public) · ↩️ P13 reversible — revoke anytime.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `65cf519` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### venture-lab — ⚑ owner (carried forward, still live):

- suggested-id: `OQ-VENTURE-LAB-CARRIED-FORWARD-STILL-LIVE`
- source: venture-lab/control/status.md @ `95e1846` · heartbeat `updated:` 2026-07-16T02:46:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ owner (carried forward, still live):
- Project custom instructions are dictionary v3.4 vs registry v3.6 — re-paste from fm:projects/venture-lab/instructions.md.
- Publish clicks queued and untouched: `docs/publishing/OWNER-QUEUE.md` (19 decisions + 44 click-run sequences; 16 hard-gated). No click performed this wake.
```

### superbot-games · Seat A — ⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded re…

- suggested-id: `OQ-SUPERBOT-GAMES-4-STANDING-DECISIONS-NONE`
- source: superbot-games/control/status.md @ `5db902a` · heartbeat `updated:` 2026-07-14T11:41:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded recommendations + VERIFY steps) is docs/eap-closeout-walkthrough-2026-07-14.md §C, surfaced verbatim in control/outbox.md § EAP CLOSE-OUT: (1) D2 audit-grants ratification · (2) rung-3 packaging/hermeticity · (3) persistence format-governance (3 sub-decisions) · (4) transfer-policy source model. RISK: all four are ↩️ reversible decision replies; no destructive click owed.
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `5db902a` · heartbeat `updated:` 2026-07-09T20:09Z
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
- source: superbot-idle/control/status.md @ `25d34f1` · heartbeat `updated:` 2026-07-14T11:32:05Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: OA-003 — WHAT: add `pytest` as a required status check on main. WHERE: https://github.com/menno420/superbot-idle/settings/branches → `main` protection rule → required status checks. HOW: add `pytest` alongside `substrate-gate` + `theme-gate` (click only). RISK: ✅ safe · ↩️ reversible (uncheck to undo). WHY-IT-MATTERS: until then a PR can merge with the test suite red (GREEN ≠ TESTED). UNBLOCKS: merge-on-green becomes trustworthy for every future PR. VERIFIED-NEEDED: branch-protection settings are owner/admin-only — standing since PR #74 (OA-003); agent sessions hold no repo admin scope. Full pending-decision list with recommendations: docs/eap-closeout-walkthrough-2026-07-14.md § C.
```

### superbot-idle (Seat B) — - ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-p…

- suggested-id: `OQ-SUPERBOT-IDLE-MANAGER-NO-LONGER-BLOCKER`
- source: superbot-idle/control/status.md @ `25d34f1` · heartbeat `updated:` 2026-07-14T11:32:05Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### superbot-mineverse — ⚑ needs-owner: unchanged — the pending clicks stay consolidated in docs/eap-closeout-walkthrough-2026-07-14.m…

- suggested-id: `OQ-SUPERBOT-MINEVERSE-UNCHANGED-PENDING-CLICKS-STAY`
- source: superbot-mineverse/control/status.md @ `ea5c751` · heartbeat `updated:` 2026-07-16T00:55:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: unchanged — the pending clicks stay consolidated in docs/eap-closeout-walkthrough-2026-07-14.md §C (incl. OA-003), each with a bolded recommendation + VERIFY step.
```

### product-forge — ⚑ OWNER-ACTION (OA-003, open)

- suggested-id: `OQ-PRODUCT-FORGE-OA-003-OPEN`
- source: product-forge/control/status.md @ `1efbb3b` · heartbeat `updated:` 2026-07-11T19:39:50Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION (OA-003, open)
WHAT: turn on GitHub Pages for this repo.
WHERE: repo Settings → Pages → Source → select "GitHub Actions".
HOW: click only (no values to paste).
WHY-IT-MATTERS: makes the games-web character-sheet preview publicly viewable.
UNBLOCKS: the prepped deploy-pages workflow publishes games-web to
  https://menno420.github.io/product-forge/ on its next run.
VERIFIED-NEEDED: deploy-pages runs 29126980391 + 29128667052 both fail at
  `actions/configure-pages` ("Get Pages site failed ... Not Found"); the site returns 404
  (last verified ~2026-07-11T19:10Z). Enabling Pages is a repo-settings toggle only the
  owner can perform.
```

### idea-engine — ⚑ needs-owner: docs/eap-closeout-walkthrough-2026-07-14.md §C (unchanged); the wake-rebind decision is review…

- suggested-id: `OQ-IDEA-ENGINE-DOCS-EAP-CLOSEOUT-WALKTHROUGH`
- source: idea-engine/control/status.md @ `96a9f22` · heartbeat `updated:` 2026-07-16T09:56:38Z (real wall-clock via date -u, monotoni…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: docs/eap-closeout-walkthrough-2026-07-14.md §C (unchanged); the wake-rebind decision is reviewed — the live cron stays as-is (see wakes line). ⚑ guard-fires telemetry delta left uncommitted — committing it was classifier-denied this session; owner decision needed (repo doctrine expects it to ride a session PR).
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `61efaa9` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

---

16 candidate block(s) across 11 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

