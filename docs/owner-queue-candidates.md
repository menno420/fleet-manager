# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #100** · generated-at **2026-07-19T07:08Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready…

- suggested-id: `OQ-SUPERBOT-HUB-SIDE-RESIDUE-ONLY`
- source: superbot/control/status.md @ `df7bf8d` · heartbeat `updated:` 2026-07-13T18:00:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready when deploy timing suits (CodeQL resolved by code change; merge=deploy Q-0193); the fleet-wide owner queue is consolidated in docs/eap/night-review-2026-07-13.md §7 (canonical: fm docs/owner-queue.md). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### superbot-next — ⚑ needs-owner: (1) disarm the residual failsafe wake triggers via the routines UI — both enabled duplicates o…

- suggested-id: `OQ-SUPERBOT-NEXT-1-DISARM-RESIDUAL-FAILSAFE`
- source: superbot-next/control/status.md @ `266c749` · heartbeat `updated:` 2026-07-18T04:15:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) disarm the residual failsafe wake triggers via the routines UI — both enabled duplicates of "SuperBot 2.0 failsafe wake": trig_01E86nBnXqesQTwm6WA4mSUD + trig_01UC7wiV3n5Vgs3RpSQt4gWz (no standing wake chain in the recreated Project); (2) delete 4 orphan merged branches (blocked agent-side by the GitHub 403 ref-delete wall, recorded 2026-07-17): #385 claude/energy-slice-2, #473 claude/title-equip-write, #476 claude/curation-row72, #424 claude/wp-stack-reconcile.
```

### substrate-kit — ⚑ FOR OWNER — kit-lab daily cron: recreate or retire? (A/B)

- suggested-id: `OQ-SUBSTRATE-KIT-KIT-LAB-DAILY-CRON`
- source: substrate-kit/control/status.md @ `4bb8f7f` · heartbeat `updated:` 2026-07-19T02:42:21Z · phase: rank-2 folded-gate diff-aware…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER — kit-lab daily cron: recreate or retire? (A/B)
  WHAT:   The 06:00Z 'kit-lab daily' owner-business cron is absent from the account trigger registry (coordinator-reported: ~2318 entries paginated to exhaustion 2026-07-17; no kit-named or hour-6 cron; never created or deleted — not re-verified by this stateless seat).
  WHERE:  docs/operations/lab-loop.md asserts it "stays armed across every cutover"; the registry has nothing to keep. The doc documents NO deliberate disarm — the loop is owner-armed-only (👤 P4, console Schedule) and cannot arm itself.
  HOW:    (A) RECREATE — owner arms a daily `0 6 * * *` UTC Schedule in the Claude Code console pointed at the kit-lab loop; (B) RETIRE — remove the "stays armed" line from lab-loop.md and mark the loop dormant-by-design pending reboot.
  WHY:    doctrine and reality contradict; a rebooted seat reads "armed" and trusts a loop that never runs. ORDER 024 also bars the seat from re-arming routines pending the per-seat reboot go, so it will not create the cron unilaterally.
  UNBLOCKS: honest lab-loop doctrine — either daily owner business resumes (A) or the false "armed" claim is removed (B).
  VERIFY: (A) the Schedule shows in the console trigger list and a 06:00Z run lands; (B) `grep -n "stays armed" docs/operations/lab-loop.md` returns nothing.
  RISK ↩️ reversible either way. RECOMMENDATION: **A — recreate** (lab-loop.md frames it as genuine daily owner business; retiring silently drops it over a transient cutover gap; re-arming is one console action gated on the reboot go). Answer: A (recreate) / B (retire).
```

### substrate-kit — ⚑ v1.19.0 adopter-wave authorization

- suggested-id: `OQ-SUBSTRATE-KIT-V1-19-0-ADOPTER`
- source: substrate-kit/control/status.md @ `4bb8f7f` · heartbeat `updated:` 2026-07-19T02:42:21Z · phase: rank-2 folded-gate diff-aware…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ v1.19.0 adopter-wave authorization
WHAT: authorize the v1.19.0 adopter-upgrade wave. (v1.19.0 now supersedes v1.18.0 as the wave target — v1.18.0 was never distributed.)
WHERE: the executing seat session, one live owner turn.
HOW: say 'run the v1.19.0 adopter wave'.
WHY: the seat session's permission classifier denied adopter-repo writes dispatched on coordinator relay alone (denial record verbatim: PR #420 body § "Denial routing"); owner provenance in the executing session is the unblock.
UNBLOCKS: ~15 adopter currency PRs to v1.19.0.
VERIFY: wave report with per-adopter PR list.
RISK: ↩️ reversible, distribution-only diffs.
  NOTE (superbot-games, carried from 2026-07-18 rung-2 re-verify): its DRIFT row is 1 genuine self-report lag + 2 consuming-lane false-positives. The wave clears the genuine half when superbot-games re-renders + re-stamps its own control/status.md v1.15.0→v1.19.0. The two consuming lanes (control/status-mining.md / control/status-exploration.md, v1.7.1 adoption-prose) will NOT clear on a version bump — their `kit:` lines are historical prose, not current claims; either reword them adopter-side, or (kit-side, NOT recommended) prune their tokens from docs/fleet-repos.txt at the cost of lane observability.
```

### substrate-kit — ⚑ CAPABILITIES denial-record entry (parked)

- suggested-id: `OQ-SUBSTRATE-KIT-CAPABILITIES-DENIAL-RECORD-ENTRY`
- source: substrate-kit/control/status.md @ `4bb8f7f` · heartbeat `updated:` 2026-07-19T02:42:21Z · phase: rank-2 folded-gate diff-aware…
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
- source: substrate-kit/control/status.md @ `4bb8f7f` · heartbeat `updated:` 2026-07-19T02:42:21Z · phase: rank-2 folded-gate diff-aware…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ P10 required-check swap
WHAT: Swap which CI check main requires, from the two legacy names to the current one.
WHERE: repo Settings → Rules → the `main` ruleset → required status checks.
HOW: in the ruleset panel, remove the two legacy-alias check names, add `kit-quality`.
WHY: the two legacy-alias jobs are permanently-absent required checks that stall every PR's merge until the enabler/lander path clears them; kit-quality is the real check.
UNBLOCKS: deleting the two legacy-alias jobs; ends the queue-stall class.
VERIFY: next kit PR shows kit-quality as the only required check; agent then removes the alias jobs.
RISK: ↩️ reversible — re-add the old required checks in the same ruleset panel.
```

### substrate-kit — ⚑ public-flip-or-PAT (pick one)

- suggested-id: `OQ-SUBSTRATE-KIT-PUBLIC-FLIP-PAT-PICK`
- source: substrate-kit/control/status.md @ `4bb8f7f` · heartbeat `updated:` 2026-07-19T02:42:21Z · phase: rank-2 folded-gate diff-aware…
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
- source: substrate-kit/control/status-superbot-coordinator.md @ `4bb8f7f` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### venture-lab — OWNER-ACTION handoff that stops at paste-ready (owner-gated publishing — the

- suggested-id: `OQ-VENTURE-LAB-HANDOFF-THAT-STOPS-AT`
- source: venture-lab/control/status.md @ `5d439bf` · heartbeat `updated:` 2026-07-19T00:29:52Z
- possibly-covered-by: none matched (manual dedup needed)

```text
  OWNER-ACTION handoff that stops at paste-ready (owner-gated publishing — the
  doc never auto-publishes). Linked from `docs/launch/README.md` (Cross-product)
  so the docs-gate reaches it; #243/#246 cited as the worked examples. Docs/
  markdown-only, reversible; no OWNER-QUEUE row (a playbook is not a publish
  surface). Posting stays an owner paste-and-post (OWNER-ACTION) — the seat
  performed no publish/spend/account action.
```

### venture-lab — **⚑ Owner-queue (paste-ready, all owner-only):**

- suggested-id: `OQ-VENTURE-LAB-QUEUE-PASTE-READY-ALL`
- source: venture-lab/control/status.md @ `5d439bf` · heartbeat `updated:` 2026-07-19T00:29:52Z
- possibly-covered-by: none matched (manual dedup needed)

```text
**⚑ Owner-queue (paste-ready, all owner-only):**
1. ~8 publish clicks — nothing live yet — per
   [`../docs/publishing/OWNER-QUEUE.md`](../docs/publishing/OWNER-QUEUE.md)
   (authoritative; decisions renumber on insert). The 2 bundles auto-unblock once
   their components publish.
2. Delete leftover remote branch `probe/push-access-check-2026-07-17` (agents are
   403-walled on branch delete).
3. LENGTH-BAND-PREP one-word ratify (unblocks Night Kiln NL omnibus + NL
   narration).
4. Native-speaker NL proofread (unblocks Salt Bell / Wire Garden NL editions).
5. R5 yes/no — authorize/decline the `_api-hardening-core` refactor of the 8
   shipped kits.
```

### superbot-games · Seat A — ⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded re…

- suggested-id: `OQ-SUPERBOT-GAMES-4-STANDING-DECISIONS-NONE`
- source: superbot-games/control/status.md @ `51975b0` · heartbeat `updated:` 2026-07-14T11:41:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded recommendations + VERIFY steps) is docs/eap-closeout-walkthrough-2026-07-14.md §C, surfaced verbatim in control/outbox.md § EAP CLOSE-OUT: (1) D2 audit-grants ratification · (2) rung-3 packaging/hermeticity · (3) persistence format-governance (3 sub-decisions) · (4) transfer-policy source model. RISK: all four are ↩️ reversible decision replies; no destructive click owed.
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `51975b0` · heartbeat `updated:` 2026-07-09T20:09Z
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
- source: superbot-idle/control/status.md @ `38648a5` · heartbeat `updated:` 2026-07-17T10:26:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: OA-003 — WHAT: add `pytest` as a required status check on main. WHERE: https://github.com/menno420/superbot-idle/settings/branches → `main` protection rule → required status checks. HOW: add `pytest` alongside `substrate-gate` + `theme-gate` (click only). RISK: ✅ safe · ↩️ reversible (uncheck to undo). WHY-IT-MATTERS: until then a PR can merge with the test suite red (GREEN ≠ TESTED). UNBLOCKS: merge-on-green becomes trustworthy for every future PR. VERIFIED-NEEDED: branch-protection settings are owner/admin-only — standing since PR #74 (OA-003); agent sessions hold no repo admin scope. Full pending-decision list with recommendations: docs/eap-closeout-walkthrough-2026-07-14.md § C.
```

### superbot-idle (Seat B) — - ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-p…

- suggested-id: `OQ-SUPERBOT-IDLE-MANAGER-NO-LONGER-BLOCKER`
- source: superbot-idle/control/status.md @ `38648a5` · heartbeat `updated:` 2026-07-17T10:26:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### superbot-mineverse — ⚑ needs-owner: unchanged — the pending clicks stay consolidated in docs/eap-closeout-walkthrough-2026-07-14.m…

- suggested-id: `OQ-SUPERBOT-MINEVERSE-UNCHANGED-PENDING-CLICKS-STAY`
- source: superbot-mineverse/control/status.md @ `18a006c` · heartbeat `updated:` 2026-07-16T00:55:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: unchanged — the pending clicks stay consolidated in docs/eap-closeout-walkthrough-2026-07-14.md §C (incl. OA-003), each with a bolded recommendation + VERIFY step.
```

### gba-homebrew — - ⚑ **OWNER/HUB asks (ender):** **merge pml #98 + product-forge #29 in the hub** — both are workflow-file PRs…

- suggested-id: `OQ-GBA-HOMEBREW-HUB-ASKS-ENDER-MERGE`
- source: gba-homebrew/control/status.md @ `97ac85d` · heartbeat `updated:` 2026-07-18T17:03:04Z (ISO-8601 UTC; coordinator ENDER close…
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ **OWNER/HUB asks (ender):** **merge pml #98 + product-forge #29 in the hub** — both are workflow-file PRs the server enabler skips (workflow-file carve-out), both **CI-green + in-scope**; pml #98 is **R22-private verified**. Owner/hub merge is the only landing path for these two.
- (i) **A/B decision on the workflow-PR carve-out rail** — the standing choice on how workflow-touching PRs route around the merge wall; owner call.
- (ii) **Clicks on pml #98 + product-forge #29** (cross-repo; not in this repo's PR list) — owner ready-click / merge. (Same as the ⚑ ask above.)
- (iii) **gba #154 (denial-triage)** — was owner rebase+merge; now **CLOSED unmerged** (10:35:57Z), so it drops off the pending list unless the owner wants it reopened.
- (iv) **Draft ready-flips** — RESOLVED: live set shows Brineward **#177 and #178 now READY** (non-draft) and **#176 MERGED** on green. Nothing left to flip.
- Console required-checks to watch: `substrate-gate` + `rom-builds` + `nds-rom-build`.
```

### product-forge — ⚑ OWNER-ACTION (OA-003, open)

- suggested-id: `OQ-PRODUCT-FORGE-OA-003-OPEN`
- source: product-forge/control/status.md @ `8934ec1` · heartbeat `updated:` 2026-07-11T19:39:50Z
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

### idea-engine — ⚑ needs-owner: ORDER-010(c) sim-lab kit upgrade v1.15.0→v1.18.0 PARKED on owner in-session authorization + AS…

- suggested-id: `OQ-IDEA-ENGINE-ORDER-010-C-SIM`
- source: idea-engine/control/status.md @ `e7c7e10` · heartbeat `updated:` 2026-07-19T07:02:35Z · seat: mirror slice — round-37 GAME-s…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: ORDER-010(c) sim-lab kit upgrade v1.15.0→v1.18.0 PARKED on owner in-session authorization + ASK-005/006 (await the fleet manager) · BT-controller plan (ORDER 017, PR #481) awaits owner review (ideas/product-forge/bt-controller-plan-2026-07-17.md).
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `2071c7b` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

---

19 candidate block(s) across 13 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

