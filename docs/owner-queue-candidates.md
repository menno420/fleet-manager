# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #30** · generated-at **2026-07-13T17:01Z** · by FM failsafe-wake 16:33Z executor session (model: Claude Fable 5), dispatched by Fleet Manager coordinator failsafe wake 2026-07-13T16:33Z
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready…

- suggested-id: `OQ-SUPERBOT-HUB-SIDE-RESIDUE-ONLY`
- source: superbot/control/status.md @ `73aaf43` · heartbeat `updated:` 2026-07-13T09:45:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready when deploy timing suits (CodeQL resolved by code change; merge=deploy Q-0193); the fleet-wide owner queue is consolidated in docs/eap/night-review-2026-07-13.md §7 (canonical: fm docs/owner-queue.md). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### substrate-kit — ⚑ FOR OWNER (paste-ready, carried from the standing set — full field blocks verbatim in git history of this f…

- suggested-id: `OQ-SUBSTRATE-KIT-PASTE-READY-CARRIED-FROM`
- source: substrate-kit/control/status.md @ `736e114` · heartbeat `updated:` 2026-07-13T16:03Z · coordinator session live (v3.6 boot 202…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER (paste-ready, carried from the standing set — full field blocks verbatim in git history of this file @ 86d2a57, ⚑ OWNER-ACTION 2/6 + ⚑ FOR MANAGER):
- **P10 required-check swap (⚑ 2):** Settings → Rules → `main` ruleset → required status checks: remove "Kit test suite" + "Cold-adoption smoke (adopt + check --strict)"; add `kit-quality`; set "Require branches to be up to date" OFF. Reversible; ends the ~35-min queue-stall class. (No agent path to rulesets — verified 403/no-endpoint.)
- **fm #122 v3.4 restamp:** the owner reviews and merges fleet-manager PR #122 PERSONALLY — do NOT agent-merge.
- **UNIVERSAL wake fetch-list vN bump + re-paste:** add `docs/seat-digest.md` (+ `docs/SKILLS.md`) to the manager-authored wake fetch list, bump vN, owner re-pastes via fm's edit-registry-first flow.
```

### substrate-kit — - **⚑ 6 public-flip-or-PAT (pick one):** make this repo public (⚠️ effectively irreversible) OR mint a fine-g…

- suggested-id: `OQ-SUBSTRATE-KIT-6-PUBLIC-FLIP-PAT`
- source: substrate-kit/control/status.md @ `736e114` · heartbeat `updated:` 2026-07-13T16:03Z · coordinator session live (v3.6 boot 202…
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ 6 public-flip-or-PAT (pick one):** make this repo public (⚠️ effectively irreversible) OR mint a fine-grained read-only PAT into the fleet environments (reversible) — unblocks the B2–B4 cross-repo sweeps.
- **Grounded-skills measurement window:** proposal to run the before/after measurement pass ~2026-07-19..26 per docs/reports/2026-07-12-grounded-skills-wrap.md §3d — say nothing to accept the window; a successor fires it when it matures.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `736e114` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### websites — ⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY. EIGHT asks open…

- suggested-id: `OQ-WEBSITES-POINTER-CANONICAL-SIX-FIELD`
- source: websites/control/status.md @ `6013c05` · heartbeat `updated:` 2026-07-13T11:31:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY. EIGHT asks open there, newest = BAKE_PAT (the bake-PR durable fix, filed #274): ORDER 020 contents:write PAT · BAKE_PAT · Q-0004 · Discord OAuth (redirect-URI + client secret) · armed-service control-API token · botsite SITE_PASSWORD · botsite Postgres/DATABASE_URL · PayPal Payouts creds.
```

### superbot-games · Seat A — ⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026…

- suggested-id: `OQ-SUPERBOT-GAMES-ORDER-004-SELF-REVIEW`
- source: superbot-games/control/status.md @ `d6a9526` · heartbeat `updated:` 2026-07-12T10:16:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026-07-11.md (authored 201f8dd/#47, relocated at close-out 3a4eb98/#57); done=004 is backed by real, spec-compliant content, not a bare marker. Remaining owner items: the OWNER-ACTION block below + docs/retro/archive-ready-2026-07-11.md. ⚑ mining WORKFLOW seam (rung 2) — audit-schema decision (D1 which schema / D2 audit item-grants, a divergence from the oracle) needs owner/lab ratification; scoped in docs/design/mining-workflow-seam.md, PR #60.
```

### superbot-games · Seat A — - ⚑ rung-3 packaging decision — docs/design/mining-host-adapter.md (scoped via #66).

- suggested-id: `OQ-SUPERBOT-GAMES-RUNG-3-PACKAGING-DECISION`
- source: superbot-games/control/status.md @ `d6a9526` · heartbeat `updated:` 2026-07-12T10:16:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ rung-3 packaging decision — docs/design/mining-host-adapter.md (scoped via #66).
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `d6a9526` · heartbeat `updated:` 2026-07-09T20:09Z
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

### superbot-idle (Seat B) — - ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-p…

- suggested-id: `OQ-SUPERBOT-IDLE-MANAGER-NO-LONGER-BLOCKER`
- source: superbot-idle/control/status.md @ `96cd635` · heartbeat `updated:` 2026-07-12T10:17Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### superbot-mineverse — ⚑ needs-owner: pytest as a required check on superbot-idle main — full six-field OWNER-ACTION block: control/…

- suggested-id: `OQ-SUPERBOT-MINEVERSE-PYTEST-AS-REQUIRED-CHECK`
- source: superbot-mineverse/control/status.md @ `f79d0ae` · heartbeat `updated:` 2026-07-13T16:15:03Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: pytest as a required check on superbot-idle main — full six-field OWNER-ACTION block: control/outbox.md entry 2026-07-13T14:56Z (VENUE: hub). Carried: MINING_WRITE_ENDPOINT + MINING_WRITE_SHARED_SECRET pair — control/outbox.md 2026-07-12T21:05Z.
```

### pokemon-mod-lab — 1. **⚑ OWNER-ACTION 1 — `ROM builds` required-check click.** GitHub →

- suggested-id: `OQ-POKEMON-MOD-LAB-1-1-ROM-BUILDS`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
1. **⚑ OWNER-ACTION 1 — `ROM builds` required-check click.** GitHub →
   Settings → Rules → `main` ruleset → require status checks → add
   `ROM builds` (keep `substrate-gate`). No agent API surface for
   rulesets (`docs/PLATFORM-LIMITS.md`).
```

### pokemon-mod-lab — 2. **⚑ OWNER-ACTION 2 — next-arc concept pick.** One word: continue

- suggested-id: `OQ-POKEMON-MOD-LAB-2-2-NEXT-ARC`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
2. **⚑ OWNER-ACTION 2 — next-arc concept pick.** One word: continue
   Emerald QoL+ (new-lead spikes) / Emerald Hard / Nuzlocke Mode
   (`docs/mod-concepts.md`). Lane default remains QoL+; reversible.
```

### pokemon-mod-lab — 3. **⚑ OWNER-ACTION 3 — playtest verdict on the 6 game-feel patches**

- suggested-id: `OQ-POKEMON-MOD-LAB-3-3-PLAYTEST-VERDICT`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
3. **⚑ OWNER-ACTION 3 — playtest verdict on the 6 game-feel patches**
   (instant text #4, auto-run #6, HP drain 3× #7, battle msg ×0.5 #7,
   egg hatch 2×/3× #21, fishing dots 2× #23) + the Match Call
   random-nag rider. One-line header flag per revert
   (`docs/build-presets.md`); hatch-128 stacking waits on this.
```

### pokemon-mod-lab — 4. **⚑ stale ref `track-a/session-019` — owner click to delete**

- suggested-id: `OQ-POKEMON-MOD-LAB-4-STALE-REF-TRACK`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
4. **⚑ stale ref `track-a/session-019` — owner click to delete**
   (content squash-merged via PR #24 long ago; sessions must not touch
   it).
```

### pokemon-mod-lab — 5. **⚑ NEW (housekeeping) — stale ref `track-a/session-024` — owner

- suggested-id: `OQ-POKEMON-MOD-LAB-5-NEW-HOUSEKEEPING-STALE`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
5. **⚑ NEW (housekeeping) — stale ref `track-a/session-024` — owner
   click to delete** (content superseded by PR #31; PR #29 closed).
   Session 041 attempted `git push origin :track-a/session-024` at
   archive time and was DENIED by the platform's auto-mode classifier
   ("[Git Destructive] ... not named or authorized by the user") — not
   retried, per playbook. Either owner-click it away alongside
   session-019, or explicitly authorize a future session to delete it.
```

### pokemon-mod-lab — - OWNER-ACTION 4 (wake-env GitHub write tools) and OWNER-ACTION 5

- suggested-id: `OQ-POKEMON-MOD-LAB-4-WAKE-ENV-GITHUB`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- OWNER-ACTION 4 (wake-env GitHub write tools) and OWNER-ACTION 5
  (`add_repo` classifier denials): **RESOLVED** — 20 consecutive clean
  wake cycles (024–043). Reopen only on regression.
```

### product-forge — ⚑ OWNER-ACTION (OA-003, open)

- suggested-id: `OQ-PRODUCT-FORGE-OA-003-OPEN`
- source: product-forge/control/status.md @ `4fdfa8a` · heartbeat `updated:` 2026-07-11T19:39:50Z
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

### idea-engine — ⚑ needs-owner: unchanged since the session-2 close-out — the full three-item bundle (owner sitting ≤2026-07-1…

- suggested-id: `OQ-IDEA-ENGINE-UNCHANGED-SINCE-SESSION-2`
- source: idea-engine/control/status.md @ `a78cd74` · heartbeat `updated:` 2026-07-13T14:19:41Z (real wall-clock via date -u, per the …
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: unchanged since the session-2 close-out — the full three-item bundle (owner sitting ≤2026-07-13, websites cutover, gift repo) stands in history @ ff0b1cb control/status.md ⚑ block.
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `80f6cd1` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

---

19 candidate block(s) across 12 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

