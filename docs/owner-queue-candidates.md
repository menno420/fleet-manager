# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #41** · generated-at **2026-07-14T04:41Z** · by failsafe-wake 0434z worker (model: fable-5), PR #185, dispatched by fleet-manager failsafe-wake executor (2026-07-14 ~04:34Z)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready…

- suggested-id: `OQ-SUPERBOT-HUB-SIDE-RESIDUE-ONLY`
- source: superbot/control/status.md @ `50481b7` · heartbeat `updated:` 2026-07-13T18:00:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: hub-side residue only — flip the two deliberately-held mineverse FLAG drafts #2058/#2061 ready when deploy timing suits (CodeQL resolved by code change; merge=deploy Q-0193); the fleet-wide owner queue is consolidated in docs/eap/night-review-2026-07-13.md §7 (canonical: fm docs/owner-queue.md). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### substrate-kit — ⚑ FOR OWNER (unchanged standing set — full paste-ready field blocks verbatim in git history of this file @ 86…

- suggested-id: `OQ-SUBSTRATE-KIT-UNCHANGED-STANDING-SET-FULL`
- source: substrate-kit/control/status.md @ `c0297d8` · heartbeat `updated:` 2026-07-14T04:02Z · coordinator session live (v3.6) · phase…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER (unchanged standing set — full paste-ready field blocks verbatim in git history of this file @ 86d2a57):
- P10 required-check swap (ruleset: require `kit-quality`, drop the two legacy contexts).
- fm #122 v3.4 restamp — owner reviews/merges PERSONALLY.
- UNIVERSAL wake fetch-list vN bump (+ docs/seat-digest.md, docs/SKILLS.md).
```

### substrate-kit — - ⚑ 6 public-flip-or-PAT (unblocks B2–B4 cross-repo sweeps).

- suggested-id: `OQ-SUBSTRATE-KIT-6-PUBLIC-FLIP-PAT`
- source: substrate-kit/control/status.md @ `c0297d8` · heartbeat `updated:` 2026-07-14T04:02Z · coordinator session live (v3.6) · phase…
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ 6 public-flip-or-PAT (unblocks B2–B4 cross-repo sweeps).
- Grounded-skills measurement window ~2026-07-19..26 — silence accepts.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `c0297d8` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### venture-lab — ⚑ Owner asks queued: (1) OWNER-QUEUE click-runs (docs/publishing/OWNER-QUEUE.md, defaults **bolded**, "go wit…

- suggested-id: `OQ-VENTURE-LAB-ASKS-QUEUED-1-QUEUE`
- source: venture-lab/control/status.md @ `991dd96` · heartbeat `updated:` 2026-07-14T04:01:48Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ Owner asks queued: (1) OWNER-QUEUE click-runs (docs/publishing/OWNER-QUEUE.md, defaults **bolded**, "go with defaults" works); (2) R5-C A/B/C letter (trading `docs/proposals/r5c-btc-bollinger-breakout-oos-proposal.md`); (3) Night Kiln 2 length band (16k parity vs the packet's 20–30k plan); (4) branch-delete credential (403 wall, docs/PLATFORM-LIMITS.md).
Next 2 (baton): (1) Friday 2026-07-17 grading pass — executor live on the coordinator seat, dry-run CLEAN; (2) owner click-runs / round-7 + follow-on probes on owner direction.
2026-07-14T02:10Z night-progress (BOOKS generative rung, ORDER 008 item 1 / ORDER 011 item 2): new adult title **The Sweetwater Sea** complete on PR #182 (`claude/night-new-title`) — 12 chapters, honest `wc -w` 15,243 (band 15,000–16,000), `candidates/adult-novels/the-sweetwater-sea/{en/the-sweetwater-sea.md,DECISIONS.md}` (verified-vs-invented ledger in DECISIONS); shortlist of 4 ranked unwritten concepts (The Wire Garden 26/30 · The Salt Bell 24 · The Lamp Room 24 · The Eleven Cities 23) recorded at `docs/ideas/2026-07-14-adult-title-concepts.md`; `docs/publishing/**` untouched — Sweetwater vetting packet queued as the follow-up slice; enabler's armed squash auto-merge left in place.
2026-07-14T02:40Z night-progress (BOOKS lane, ORDER 011 item 2 continuation, owner night directive): NL catalog line COMPLETE — three complete NL editions landed tonight: *Liefde in de kantlijn* 15,633w (PR #183, merged), *De Morgendeur* 16,730w (PR #185, merged), *De geborgen boomgaard* 15,750w (anchor PR #184, enabler auto-merge armed, lands on the card flip); adult NL editions now 11, every ORDER-011 EN adult manuscript covered (EN-only remainders: *The Harvest Rows* Book 3 + tonight's *The Sweetwater Sea*, PR #182). Follow-through in the same batch per the #166 remedy class (PR #184): 4 vetting packets — `de-geborgen-boomgaard`, `liefde-in-de-kantlijn`, `de-morgendeur` (Book-2 length-band ⚑ carried untouched), `the-sweetwater-sea` (coordinator scope-add for PR #182; collision recorded honestly: Low exact-title, Moderate Great-Lakes-epithet search drift, subtitle mandatory) — keyword-map rows (6 new browse-node claims + 28 keyword rows incl. three C4 first-claims, the map's first SERIES node-share for De Morgendeur, and C3's fourth Netherlands era-register for Sweetwater; full-map V057 first-claim scan clean, no existing claim touched), ONE `derive_owner_queue.py` regen — counts now **19 decisions / 41 sequences / 241 clicks (14 hard-gated), 43/43 inputs clean** (from 19/37/213, 11 hard-gated) — and counts-sync to current-state + NEXT-SESSION (stale "4 adult NL editions" → 11 by grep; packets 38 → 42; adult EN manuscripts 12 → 13).
2026-07-14T03:40Z night-progress (BOOKS lane, ORDER 011 NL-completion remainder, night-final slice): NL catalog 13/13 COMPLETE — the two EN-only remainders landed as NL editions on PR #186 (`claude/night-nl-final`, born-red anchor card): *De zoete zee* 15,467w (12 chapters, +1.5% over the 15,243w EN source; pre-named title per DECISIONS.md, subtitle *Een novelle van de Zuiderzee*) and *De Oogstslag* 24,655w (12 chapters, +5.7% over the 23,334w EN source; title derived decide-and-flag — no pre-naming existed — Books One–Two series glossary inherited unchanged, translated AS WRITTEN with the Book-2 length-band ⚑ untouched). Same-batch follow-through per the #166 remedy class: 2 vetting packets (`de-zoete-zee`, `de-oogstslag`) + 14 keyword-map rows (7+7 NL C4 first-claims; full-map V057 first-claim scan run clean twice — at proposal and re-run at apply — zero collisions, no spares used; De zoete zee shares The Sweetwater Sea's two browse nodes per C4, De Oogstslag rides De Nachtoven's two per the §3 series rule, the map's second series node-share), ONE `derive_owner_queue.py` regen — counts now **19 decisions / 43 sequences / 256 clicks (16 hard-gated), 45/45 inputs clean** (from 19/41/241, 14 hard-gated) — and counts-sync to current-state + NEXT-SESSION (adult NL editions 11 → 13, packets 42 → 44; night-kiln versions/README "two EN novellas" intro drift fixed to three EN + three NL). Title-ratification ⚑s queued owner-side (De Oogstslag bundled with the series' titles, De zoete zee with its §2 collision findings); nothing published, no clicks performed.
2026-07-14T03:43:50Z night-progress (BOOKS generative rung, ORDER 008 item 1 / ORDER 011 item 2): second adult title **The Wire Garden** complete on PR #187 (`claude/night-wire-garden`) — 12 chapters, honest `wc -w` 15,900 (band 15,000–16,000), `candidates/adult-novels/the-wire-garden/{en/the-wire-garden.md,DECISIONS.md}` (verified-vs-invented Dodendraad ledger; exact-title collision recorded, subtitle mandatory; NL title pre-named De draadtuin); shortlist doc marked 2 WRITTEN · 3 unwritten (next: The Salt Bell 24/30); docs/publishing/** untouched — vetting packet queued as follow-up slice.
2026-07-14T04:01:48Z night-summary (continuation wave complete — final close-out slice, `claude/night-wire-garden-packet`): the Wire Garden owed follow-up landed — vetting packet `docs/publishing/vetting/the-wire-garden.md` (manuscript-backed, 15,900w re-measured; §2 collision re-scan confirms the 2025 genre-disjoint Marcum thriller, retitle declined, subtitle *A novella of the Dodendraad* MANDATORY; NL pre-name *De draadtuin* carried), keyword-map rows (2 browse-node claims + 7 EN rows; C3's fifth Netherlands era-register, WWI neutral-border/Dodendraad; full-map V057 first-claim scan run at proposal and re-run at apply, zero collisions), ONE `derive_owner_queue.py` regen — counts now **19 decisions / 44 sequences / 262 clicks (16 hard-gated), 46/46 inputs clean** (from 19/43/256, 16) — counts-sync to current-state + NEXT-SESSION. NIGHT TALLY, all lists done, no remainder: venture shipped product #10 (AI Novella Production Kit $29 publish-READY) + 2 new EN novellas (The Sweetwater Sea 15,243w PR #182, The Wire Garden 15,900w PR #187) + 7 NL editions (PRs #183–#186 wave — NL catalog 13/13 complete) + 8 large-print EDITION-SPECs (PR #172) + sim verdicts applied (V037/V039/V040/V041 + V053/V057/V049, PRs #163/#173) + V020 probe pre-registered (PR #179); trading shipped round 6 + retrospective + 2 infra improvements (trading repo); pointers: docs/publishing/OWNER-QUEUE.md (owner clicks), docs/current-state.md + docs/NEXT-SESSION.md (synced counts).
```

### superbot-games · Seat A — ⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026…

- suggested-id: `OQ-SUPERBOT-GAMES-ORDER-004-SELF-REVIEW`
- source: superbot-games/control/status.md @ `b7b1062` · heartbeat `updated:` 2026-07-12T10:16:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026-07-11.md (authored 201f8dd/#47, relocated at close-out 3a4eb98/#57); done=004 is backed by real, spec-compliant content, not a bare marker. Remaining owner items: the OWNER-ACTION block below + docs/retro/archive-ready-2026-07-11.md. ⚑ mining WORKFLOW seam (rung 2) — audit-schema decision (D1 which schema / D2 audit item-grants, a divergence from the oracle) needs owner/lab ratification; scoped in docs/design/mining-workflow-seam.md, PR #60.
```

### superbot-games · Seat A — - ⚑ rung-3 packaging decision — docs/design/mining-host-adapter.md (scoped via #66).

- suggested-id: `OQ-SUPERBOT-GAMES-RUNG-3-PACKAGING-DECISION`
- source: superbot-games/control/status.md @ `b7b1062` · heartbeat `updated:` 2026-07-12T10:16:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ rung-3 packaging decision — docs/design/mining-host-adapter.md (scoped via #66).
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `b7b1062` · heartbeat `updated:` 2026-07-09T20:09Z
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
- source: superbot-idle/control/status.md @ `5ddd5a2` · heartbeat `updated:` 2026-07-13T17:43Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### superbot-mineverse — ⚑ needs-owner: (1) sender-side HMAC adoption — owner/bot-lane work via the superbot #2058 draft flip; full OW…

- suggested-id: `OQ-SUPERBOT-MINEVERSE-1-SENDER-SIDE-HMAC`
- source: superbot-mineverse/control/status.md @ `0b388f1` · heartbeat `updated:` 2026-07-14T03:46:08Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) sender-side HMAC adoption — owner/bot-lane work via the superbot #2058 draft flip; full OWNER-ACTION block below (§ OWNER-ACTION). (2) The six OAuth/write host env vars remain owner-only — six-field block: control/outbox.md entry 2026-07-12T21:05Z (outstanding pair: MINING_WRITE_ENDPOINT + MINING_WRITE_SHARED_SECRET; the ingest side additionally needs MINING_SNAPSHOT_RELAY_SHARED_SECRET + MINING_SNAPSHOT_PATH web-host-side, see §2058 block). (3) Carried: pytest as required check on superbot-idle main (OA-003) — six-field block: control/outbox.md entry 2026-07-13T14:56Z (VENUE: hub).
```

### superbot-mineverse — ⚑ OWNER-ACTION

- suggested-id: `OQ-SUPERBOT-MINEVERSE-FLAG`
- source: superbot-mineverse/control/status.md @ `0b388f1` · heartbeat `updated:` 2026-07-14T03:46:08Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION
WHAT: flip superbot PR #2058 (the bot-side snapshot pusher) out of draft and have the bot lane adopt sender-side HMAC signing so its POSTs authenticate against this repo's live `/api/snapshot/ingest` endpoint.
WHERE: github.com/menno420/superbot → PR #2058 ("Ready for review" button + bot-lane follow-through); host env vars land in the bot host's environment plus the web host per the seam doc `docs/mining-data-contract.md` § Sender (superbot PR #2058).
HOW: sender signs with the repo's ONE canonical scheme (`X-Mineverse-Signature`/`X-Mineverse-Timestamp`, HMAC-SHA256 over `"POST\n/api/snapshot/ingest\n<TIMESTAMP>\n<sha256_hex(BODY)>"`), keyed with `MINING_SNAPSHOT_RELAY_SHARED_SECRET`; env names: `MINING_SNAPSHOT_RELAY_URL` + `MINING_SNAPSHOT_RELAY_GUILD_ID` (bot side), `MINING_SNAPSHOT_RELAY_SHARED_SECRET` + `MINING_SNAPSHOT_PATH` (web host). Values stay owner-side, never in any repo.
RISK: ↩️ reversible — unset the env vars / re-draft the PR to undo; the receive side stays fail-closed (503) whenever the secret or path is unset.
WHY-IT-MATTERS: the FLAG-1 READ relay's receive half is live and tested; live miner data cannot flow until the sender signs and pushes.
UNBLOCKS: live bot→web snapshot flow (FLAG 1), replacing the committed fixture; the staleness badge (VERDICT 056) starts measuring a real feed.
VERIFIED-NEEDED: #2058 is another repo's owner/bot-lane draft and its body names no transport auth (recorded in `docs/mining-data-contract.md` @48e158e); agent sessions hold no write seat on menno420/superbot and no host-env access (docs/CAPABILITIES.md) — receive-side work is complete in this repo (PRs #88/#93), only the sender half remains.
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

### gba-homebrew — - **⚑ Self-initiated** (rung 4, coordinator-directed): web-arcade

- suggested-id: `OQ-GBA-HOMEBREW-SELF-INITIATED-RUNG-4`
- source: gba-homebrew/control/status.md @ `b778d39` · heartbeat `updated:` 2026-07-12T16:20:12Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ Self-initiated** (rung 4, coordinator-directed): web-arcade
  packaging refreshed from main @ `982b23a` — **supersedes the
  stale PR #85 pending owner disposition** (#85 is conflicted and
  packaged the pre-#84 Drift Garden foundation; it was not touched,
  closed, or commented on).
- `tools/package-web-arcade.sh` now stages main's ACTUAL shipped
  set: Undertow v1.0, Tiltstone v1.0 (pre-juice — the #92←#93←#95←#97
  stack is still open; juice.js staging + version bump noted as the
  pending follow-up), Drift Garden **v1.0 as the playable seeded
  round game** (#84, merge `7ffcf1c`), arcade bundle v1.1.
  Determinism: fixed epoch + LC_ALL=C-sorted `zip -X`, two runs
  byte-identical; `docs/RELEASES.md` pins every zip AND staged file
  sha256, machine-asserted by the new `--verify` mode.
- With this slice: **Shoal v1.0 and Clockwork Courier v1.0 are both
  CONCEPT-COMPLETE** (PRs #98-#103, #96+#105-#108), the web arcade
  package is current, and no inbox ORDER is unserved (001-005 all
  served; the EAP night ORDER never arrived — the #104 outbox ask to
  the manager stands). Open non-lane PRs: Tiltstone stack
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

### idea-engine — ⚑ needs-owner: unchanged — the full three-item bundle (owner sitting ≤2026-07-13, websites cutover, gift repo…

- suggested-id: `OQ-IDEA-ENGINE-UNCHANGED-FULL-THREE-ITEM`
- source: idea-engine/control/status.md @ `e4852e0` · heartbeat `updated:` 2026-07-14T04:30:17Z (real wall-clock via date -u, monotoni…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: unchanged — the full three-item bundle (owner sitting ≤2026-07-13, websites cutover, gift repo) stands in history @ ff0b1cb control/status.md ⚑ block.
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `80f6cd1` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

---

21 candidate block(s) across 13 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

