# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #142** · generated-at **2026-07-21T14:36Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready…

- suggested-id: `OQ-SUPERBOT-HUB-SIDE-RESIDUE-ONLY`
- source: superbot/control/status.md @ `882f70f` · heartbeat `updated:` 2026-07-13T18:00:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready when deploy timing suits (CodeQL resolved by code change; merge=deploy Q-0193); the fleet-wide owner queue is consolidated in docs/eap/night-review-2026-07-13.md §7 (canonical: fm docs/owner-queue.md). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### superbot-next — ⚑ needs-owner: broad orphan merged-branch cleanup remains blocked by the GitHub 403 ref-delete wall (owner/ad…

- suggested-id: `OQ-SUPERBOT-NEXT-BROAD-ORPHAN-MERGED-BRANCH`
- source: superbot-next/control/status.md @ `e5e6dfd` · heartbeat `updated:` 2026-07-20T07:30:12Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: broad orphan merged-branch cleanup remains blocked by the GitHub 403 ref-delete wall (owner/admin). The previously-listed owner-blocker items were resolved 2026-07-18 and are dropped here: the two named residual triggers are absent from the account registry (per docs/current-state.md:67-73) and the four named orphan merged branches are absent from origin.
```

### substrate-kit — ⚑ FOR OWNER — venture-lab `upgrade`-verb classifier wall (escalated to fm owner-queue)

- suggested-id: `OQ-SUBSTRATE-KIT-VENTURE-LAB-UPGRADE-VERB`
- source: substrate-kit/control/status.md @ `62621ad` · heartbeat `updated:` 2026-07-21T11:07:21Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER — venture-lab `upgrade`-verb classifier wall (escalated to fm owner-queue)
  WHAT:   The kit `upgrade` verb is classifier-walled venture-lab-specifically, so venture-lab #282 could NOT be re-vendored to v1.20.2 this pass.
  WHERE:  fleet-manager owner-queue (escalated) — venture-lab lane.
  HOW:    run the re-vendor from a non-walled venue, OR add an owner permission rule that clears the verb for venture-lab; then reword-3 + allowlist-4 greens it.
  WHY:    the wall is venue/classifier-specific, not a kit defect — the same verb succeeds in the other adopter lanes.
  UNBLOCKS: venture-lab v1.20.2 re-vendor.
  RISK: ↩️ reversible. RECOMMENDATION: re-run from a non-walled venue.
```

### substrate-kit — ⚑ FOR OWNER — kit-lab daily cron: recreate or retire? (A/B)

- suggested-id: `OQ-SUBSTRATE-KIT-KIT-LAB-DAILY-CRON`
- source: substrate-kit/control/status.md @ `62621ad` · heartbeat `updated:` 2026-07-21T11:07:21Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER — kit-lab daily cron: recreate or retire? (A/B)
  WHAT:   The 06:00Z 'kit-lab daily' owner-business cron is absent from the account trigger registry (coordinator-reported: ~2318 entries paginated to exhaustion 2026-07-17; no kit-named or hour-6 cron; never created or deleted — not re-verified by this stateless seat).
  WHERE:  docs/operations/lab-loop.md asserts it "stays armed across every cutover"; the registry has nothing to keep. The doc documents NO deliberate disarm — the loop is owner-armed-only (👤 P4, console Schedule) and cannot arm itself.
  HOW:    (A) RECREATE — owner arms a daily `0 6 * * *` UTC Schedule in the Claude Code console pointed at the kit-lab loop; (B) RETIRE — remove the "stays armed" line from lab-loop.md and mark the loop dormant-by-design pending reboot.
  WHY:    doctrine and reality contradict; a rebooted seat reads "armed" and trusts a loop that never runs. ORDER 024 also bars the seat from re-arming routines pending the per-seat reboot go, so it will not create the cron unilaterally.
  UNBLOCKS: honest lab-loop doctrine — either daily owner business resumes (A) or the false "armed" claim is removed (B).
  VERIFY: (A) the Schedule shows in the console trigger list and a 06:00Z run lands; (B) `grep -n "stays armed" docs/operations/lab-loop.md` returns nothing.
  RISK: ↩️ reversible either way. RECOMMENDATION: **A — recreate**. Answer: A (recreate) / B (retire).
```

### substrate-kit — ⚑ FOR OWNER — public-flip-or-PAT (pick one)

- suggested-id: `OQ-SUBSTRATE-KIT-PUBLIC-FLIP-PAT-PICK`
- source: substrate-kit/control/status.md @ `62621ad` · heartbeat `updated:` 2026-07-21T11:07:21Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER — public-flip-or-PAT (pick one)
  WHAT: Let the other fleet repos read this one — either make it public or mint a read-only token.
  WHERE: P11: Settings → General → Danger Zone → Change visibility · P13: github.com/settings/tokens → fine-grained read-only PAT scoped to this repo, then add it to the fleet environments.
  HOW: P11 is click-through; P13 is create-token + paste into environment settings.
  WHY: sibling repos cannot read kit data today, so cross-repo sweeps and the merged console run blind.
  UNBLOCKS: B2–B4 cross-repo sweeps + kit data in the merged console.
  VERIFY: a sibling-seat session fetches a kit file read-only without "Access denied: repository … is not configured for this session".
  RISK: ⚠️ P11 effectively irreversible (history exposed once public) · ↩️ P13 reversible — revoke anytime. RECOMMENDATION: **B — mint a read-only PAT** (reversible; no history exposure).
```

### substrate-kit — ⚑ FOR OWNER — t5-headless-guard fix (owner-review: pin-path PR #552 OPEN, awaiting owner merge)

- suggested-id: `OQ-SUBSTRATE-KIT-T5-HEADLESS-GUARD-FIX`
- source: substrate-kit/control/status.md @ `62621ad` · heartbeat `updated:` 2026-07-21T11:07:21Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER — t5-headless-guard fix (owner-review: pin-path PR #552 OPEN, awaiting owner merge)
  STATUS: PR opened, awaiting owner review — https://github.com/menno420/substrate-kit/pull/552 (do-not-automerge; green; the additive shape-2 guard-observability edit to bench/tasks/T5.md). OWNER'S LANE — the agent does NOT touch it.
  WHAT: fix the T5 bench probe so it produces a real in-session guard fire in the ON arm (shape 2 — check-driven guards; no hook-honoring harness rebuild needed).
  WHY: without it, T5 scores all guard items n/a — the ON arm demonstrates nothing over the unguarded baseline.
  VERIFY: a T5 run produces ≥1 real in-session guard fire (or a recorded deliberate violation) in the ON arm.
  RISK: ⚠️ pin-path oracle change → lands via a `do-not-automerge` owner-review PR (never auto-merged). Detail: docs/planning/2026-07-19-needs-planning-recipes.md §4.
```

### substrate-kit — ⚑ FOR OWNER — superbot pin-bump: bump nominal pin, or leave as pin-only? (question)

- suggested-id: `OQ-SUBSTRATE-KIT-SUPERBOT-PIN-BUMP-BUMP`
- source: substrate-kit/control/status.md @ `62621ad` · heartbeat `updated:` 2026-07-21T11:07:21Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER — superbot pin-bump: bump nominal pin, or leave as pin-only? (question)
  WHAT: superbot adopts substrate-kit as a PIN ONLY (substrate.config pin 1.0.0; no vendored dist, no `.substrate/` state) — so the dist-vendoring upgrade is genuinely N/A there; it was correctly skipped in this wave.
  WHERE: superbot/substrate.config.json (or equivalent pin), pin `1.0.0`.
  HOW: (A) bump the nominal pin to `1.20.2` for a truthful version label even though no dist is vendored; (B) leave pin-only and document superbot as intentionally non-vendoring (adoption = pin-nominal only).
  WHY: the pin currently reads 1.0.0 while the fleet is on 1.20.2 — a reader can't tell "deliberately pin-only" from "stale". A one-line decision removes the ambiguity.
  UNBLOCKS: honest fleet version truth for superbot.
  RISK: ↩️ reversible either way. RECOMMENDATION: **B — document pin-only** (superbot genuinely vendors no dist; a bumped pin with no dist would itself mislead). Answer: A (bump pin) / B (document pin-only).
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `62621ad` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### superbot-games · Seat A — ⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded re…

- suggested-id: `OQ-SUPERBOT-GAMES-4-STANDING-DECISIONS-NONE`
- source: superbot-games/control/status.md @ `a9a7dcc` · heartbeat `updated:` 2026-07-14T11:41:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 4 standing decisions, none new this wake — the OWNER ACTIONS checklist (deep links + bolded recommendations + VERIFY steps) is docs/eap-closeout-walkthrough-2026-07-14.md §C, surfaced verbatim in control/outbox.md § EAP CLOSE-OUT: (1) D2 audit-grants ratification · (2) rung-3 packaging/hermeticity · (3) persistence format-governance (3 sub-decisions) · (4) transfer-policy source model. RISK: all four are ↩️ reversible decision replies; no destructive click owed.
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `a9a7dcc` · heartbeat `updated:` 2026-07-09T20:09Z
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
- source: superbot-idle/control/status.md @ `31a4a3a` · heartbeat `updated:` 2026-07-17T10:26:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: OA-003 — WHAT: add `pytest` as a required status check on main. WHERE: https://github.com/menno420/superbot-idle/settings/branches → `main` protection rule → required status checks. HOW: add `pytest` alongside `substrate-gate` + `theme-gate` (click only). RISK: ✅ safe · ↩️ reversible (uncheck to undo). WHY-IT-MATTERS: until then a PR can merge with the test suite red (GREEN ≠ TESTED). UNBLOCKS: merge-on-green becomes trustworthy for every future PR. VERIFIED-NEEDED: branch-protection settings are owner/admin-only — standing since PR #74 (OA-003); agent sessions hold no repo admin scope. Full pending-decision list with recommendations: docs/eap-closeout-walkthrough-2026-07-14.md § C.
```

### superbot-idle (Seat B) — - ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-p…

- suggested-id: `OQ-SUPERBOT-IDLE-MANAGER-NO-LONGER-BLOCKER`
- source: superbot-idle/control/status.md @ `31a4a3a` · heartbeat `updated:` 2026-07-17T10:26:04Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### gba-homebrew — - ⚑ **OWNER/HUB asks (ender):** **merge pml #98 + product-forge #29 in the hub** — both are workflow-file PRs…

- suggested-id: `OQ-GBA-HOMEBREW-HUB-ASKS-ENDER-MERGE`
- source: gba-homebrew/control/status.md @ `3377319` · heartbeat `updated:` 2026-07-18T17:03:04Z (ISO-8601 UTC; coordinator ENDER close…
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
- source: product-forge/control/status.md @ `e3fc844` · heartbeat `updated:` 2026-07-11T19:39:50Z
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

### idea-engine — ⚑ needs-owner: BT-controller plan (ORDER 017, PR #481) awaits owner review (ideas/product-forge/bt-controller…

- suggested-id: `OQ-IDEA-ENGINE-BT-CONTROLLER-PLAN-ORDER`
- source: idea-engine/control/status.md @ `1120a19` · heartbeat `updated:` 2026-07-21T14:08:27Z · round VERDICT 270 landing — P257 -> …
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: BT-controller plan (ORDER 017, PR #481) awaits owner review (ideas/product-forge/bt-controller-plan-2026-07-17.md).
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `2071c7b` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

### fleet-manager (this repo) — 4. **⚑ Guard proposal recorded (awaiting owner/registry):** work-loop cron

- suggested-id: `OQ-FLEET-MANAGER-4-GUARD-PROPOSAL-RECORDED`
- source: fleet-manager/control/status.md @ `2a9ec9d` · heartbeat `updated:` 2026-07-21T08:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
4. **⚑ Guard proposal recorded (awaiting owner/registry):** work-loop cron
   to replace the FM send_later pacemaker chain (second lapse in one day;
   Q-0194 second-occurrence rule). Details in `docs/fleet-triage.md`
   § "11:30Z cycle".
5. **Watches (carried):** superbot-games Seat A idling (4 fires since
   04:54Z) · websites review-bake cron (bake age) · superbot-next
```

---

17 candidate block(s) across 12 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

