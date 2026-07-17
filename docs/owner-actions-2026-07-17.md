# Owner actions — fleet-wide, 2026-07-17

> **Status:** `audit`
>
> Single verified, paste-ready list of everything the owner personally needs to
> do across the whole superbot fleet, as of 2026-07-17. Every item was checked
> against **live GitHub** (per-PR `get_pull_request` + live check-runs), not
> agent reports, the morning of 2026-07-17. Built by fleet-manager session
> `claude/owner-actions-0717` (PR #279). Hand this to an owner-live hub session
> to execute in one sitting. Where a queued item was already resolved or
> superseded, it is in §5 and dropped from the action sections.

## ✅ EXECUTED 2026-07-17 (09:17–10:19Z)

**§1–§3 all executed by the owner** the morning of 2026-07-17 (09:17–10:19Z).
**11 PRs reached terminal state: 8 merged / 3 closed.** Every state below was
re-verified live per-PR via `get_pull_request` on 2026-07-17 before this note
was written (fleet-manager close-out PR #281).

- **Merged (8):** websites #380 (10:19:30Z) · superbot-games #151 (09:20:49Z) ·
  gba-homebrew #153 (09:17:04Z, the DO-FIRST — repaired main's substrate-gate) ·
  superbot-idle #145 (09:19:07Z) · pokemon-mod-lab #94 (09:19:06Z) ·
  superbot-next #503 (09:19:10Z), #499 (09:28:14Z), #500 (09:28:27Z).
- **Closed-unmerged (3):** websites #359 (09:23:17Z — superseded by #380, §5) ·
  pokemon-mod-lab #87 (10:17:04Z — §3 D1 outcome = CLOSE) · superbot-games #149
  (10:17:01Z — **§3 D3 outcome was CLOSE, not rebase+merge**; the draft mirror of
  idle #142 was discarded, the reconcile-race guard rides the idle-side fix).

**Still OPEN for the owner (NOT executed):** **§4** veto passes (6 menus,
~266 proposals — non-vetoed items get built either way) and **§6** settings /
provisioning (9 owner-only console items). The **websites 8 green drafts** in §2
also remain GATED behind the auto-merge draft-gap patch (§6 item 2) — not landed
this sitting.

## Totals

- **§1 Merges (owner click to land):** 2 — both need an admin-override click (branch protection blocks the normal path).
- **§2 Ready-flips (green drafts → "Ready for review"):** 12 PRs — 4 land cleanly on flip; 8 (websites) are gated on the draft-gap patch (see notes).
- **§3 Decisions (one-letter answerable):** 5.
- **§4 Veto passes (optional menu filtering):** 6 menus, ~266 proposals. Non-vetoed items get built either way.
- **§5 Already done / superseded:** stale queue items to skip.
- **§6 Settings / provisioning (owner-only console):** 9 items.

**Estimated effort:** §1–§3 (merges + flips + decisions) is one ~30–45 min sitting. §4 veto passes and §6 settings are additional and can be batched separately.

**DO-FIRST:** flip **gba-homebrew #153** (§2) — it repairs main's substrate-gate and unblocks 27 downstream PRs.

---

## §1 — Merges (green, non-draft; need an owner click to land) — ✅ EXECUTED 2026-07-17

*✅ EXECUTED: #380 merged 10:19:30Z (admin-override) + #359 closed 09:23:17Z; superbot-games #151 merged 09:20:49Z.*

Both are green but `mergeable_state: blocked/unstable` — the normal auto-merge path is not available, so they need an **admin-override** squash-merge ("Merge without waiting for requirements").

**websites #380** — today's fleet-data bake.
- https://github.com/menno420/websites/pull/380
- What: daily fleet-data JSON refresh (data-only, 4 files). `quality` check green; non-draft. `blocked` because auto-merge could not arm (no `BAKE_PAT` secret — see §6/D4).
- Do: admin squash-merge #380, then **close #359** (yesterday's identical bake, superseded).
- RISK: ↩️ · Verify after: #380 merged, #359 closed.

**superbot-games #151** — docs truth-refresh of `current-state.md`.
- https://github.com/menno420/superbot-games/pull/151
- What: docs-only current-state refresh. Non-draft. `tests` + `substrate-gate` green; the `enable-auto-merge` + `reconcile` jobs are red (advisory, not required).
- Do: admin squash-merge (if those jobs are non-required); else re-run them.
- RISK: ↩️ · Verify after: merged; current-state.md updated on main.

---

## §2 — Ready-flips (green drafts → "Ready for review") — ✅ PARTIALLY EXECUTED 2026-07-17

*✅ EXECUTED: ① gba-homebrew #153 MERGED 09:17:04Z · ② superbot-idle #145 MERGED 09:19:07Z · ③ pokemon-mod-lab #94 MERGED 09:19:06Z · ④ superbot-next #503 MERGED 09:19:10Z. **⑤ websites 8 green drafts stay GATED** behind the §6 auto-merge draft-gap patch — NOT flipped this sitting.*

**① DO FIRST — gba-homebrew #153** — repairs main's substrate-gate + unblocks 27 arc PRs.
- https://github.com/menno420/gba-homebrew/pull/153
- What: restores read-path reachability for 5 docs orphaned by #151. Green + `clean`. Flip to Ready → merges on green.
- RISK: ✅ · Verify after: merged; main substrate-gate green.
- NOTE: the other 27 gba drafts (#154–#180) do NOT auto-clear when you flip #153 — they inherit the gate-red and need an agent rebase onto #153's fix first. **Do not bulk-flip them today.**

**② superbot-idle #145** — control stale-claims sweep. Green + clean draft.
- https://github.com/menno420/superbot-idle/pull/145
- RISK: ✅ · Verify after: merged.

**③ pokemon-mod-lab #94** — overnight veto menu (33 proposals). Green draft; held by the seat landing wall. Flip → merges (menu lands on main; read it in §4).
- https://github.com/menno420/pokemon-mod-lab/pull/94
- RISK: ✅ · Verify after: merged.

**④ superbot-next #503** — coordinator close-out heartbeat card. Draft "owner lands" by design. Undraft → merges.
- https://github.com/menno420/superbot-next/pull/503
- RISK: ✅ · Verify after: merged.

**⑤ websites — 8 green drafts (GATED).** #372, #373, #375, #376, #377, #378, #379 (+ #371 optional).
- All `quality`-green drafts. They will NOT self-merge until the staged **auto-merge draft-gap patch** lands (workflow write, owner-gated — §6). Recommended: land that patch first, then flip all 8 in one pass; or manually flip + admin-merge each.
- Links: /pull/372 /373 /375 /376 /377 /378 /379 /371 (repo menno420/websites)
- RISK: mixed ✅/↩️ (test/guard + console/dashboard UI; #375 + #373 are the websites veto-menu docs — §4).
- Verify after: each merged.

---

## §3 — Decisions (one-letter answerable) — ✅ EXECUTED 2026-07-17

*✅ EXECUTED: D1 pokemon-mod-lab #87 → CLOSE (closed 10:17:04Z) · D2 superbot-next #499+#500 → LAND both (merged 09:28:14Z / 09:28:27Z) · D3 superbot-games #149 → outcome was CLOSE, not rebase+merge (closed 10:17:01Z). D4 (websites bakes) / D5 (trading-strategy per-seat-go) ride their §6 settings items.*

**D1 — pokemon-mod-lab #87: rebase vs close.**
- https://github.com/menno420/pokemon-mod-lab/pull/87 — green CI but `mergeable_state: dirty` (real control/status.md conflict; the file it rewrites is already replaced on main by merged #92/#95).
- **A** rebase/resolve then merge · **B (recommended)** close as superseded (rebase would resurrect a stale wholesale overwrite; seat status.md already says close-as-superseded).
- Answer: A or B.

**D2 — superbot-next #499 + #500: land vs hold.**
- Both draft + born-red card (substrate-gate red = the deliberate card hold, not a defect; all substantive CI green). The overnight seat froze its whole loop on this consent question.
- #499 (https://github.com/menno420/superbot-next/pull/499): control-plane hygiene only — retire 6 terminal claims + file 1. No code/workflow/schema. Fully reversible.
- #500 (https://github.com/menno420/superbot-next/pull/500): re-mints 31 non-kernel parity goldens raw→stripped; loosens parity-depth floors (narrated in-file). Strip-only, gate-green, test-covered. No workflow/runtime/schema.
- **Recommended: LAND both** (undraft + flip each card to `complete` → auto-merge on green). Both contained/reversible.
- Answer: "land both" / "land 499 only, hold 500" / "hold both".

**D3 — superbot-games #149: rebase+merge vs close.**
- https://github.com/menno420/superbot-games/pull/149 — reconcile-race fix (games mirror of idle #142, already merged). `mergeable_state: dirty` (conflict) + draft + `do-not-automerge` label + touches `.github/workflows/`. Cannot auto-merge.
- **A (recommended)** dispatch an agent to rebase/resolve, then clear the `do-not-automerge` label and squash-merge (workflow-touch needs the manual click) · **B** close if the guard is covered elsewhere.
- Answer: A or B.

**D4 — websites bakes: provision vs manual.**
- #359/#380 can't self-merge (no `BAKE_PAT`).
- **A (recommended)** provision `BAKE_PAT` (§6) so nightly bakes self-land — never recurs · **B** just admin-merge #380 today (§1) and revisit the secret later.
- Answer: A or B.

**D5 — trading-strategy double-grading: per-seat-go vs defer.**
- A foreign trigger fires 2026-07-17 09:00Z near the lane's own (archived, won't-fire) 09:08Z grading window; the host-owned replacement `weekly-grading.yml` is parked on an owner "per-seat go."
- Impact this week ≈ **zero**: `grade_paper.py` is a no-op until ~August (no evaluable ledger entry yet). Deadline today 09:00Z is imminent/passed but nothing grades regardless.
- **Recommended: give the one-line "per-seat go"** to land `weekly-grading.yml` at your convenience (secures the executor before August); no rush this week.
- Answer: "per-seat go" / "defer".

---

## §4 — Veto passes (OPTIONAL menu filtering)

Veto is optional: strike the ids you DON'T want; everything un-vetoed gets built. Suggested skim order = smallest / already-on-main first.

1. **fleet-manager — 25 proposals** · on main · `docs/planning/overnight-menu-2026-07-17.md` · rec first-build **S3/S5/S9**.
2. **trading-strategy — 25** · on main · `planning/2026-07-17-overnight-menu.md`.
3. **venture-lab — 38** · on main · `docs/ideas/2026-07-17-overnight-menu.md`.
4. **pokemon-mod-lab — 33** · in draft PR #94 (flip to land on main — §2).
5. **websites — 61** · split across draft PRs #375 (37) + #373 (24); flip to land (§2).
6. **gba-homebrew — 84** · in draft PR #171 only (`docs/planning/OVERNIGHT-MENU-2026-07-16.md`); blocked behind #153 — read in the PR.

Total ≈ **266 proposals across 6 menus.** (superbot-games has no overnight menu, only `dnd-story-game-plan.md`.)

---

## §5 — Already done / superseded (skip these)

- **websites #359 "merge by hand" (owner-queue #69) — STALE.** Do NOT merge #359; superseded by today's #380 (identical bake, newer base). Close #359; handle #380 in §1.
- **owner-queue #71 "ready-flip trio" — partially stale.** games #149 is NOT a clean flip (conflict → D3). gba #153 + idle #145 remain valid (§2).
- **venture-lab / trading-strategy overnight PRs — already merged.** Menus are on main (§4); no PR action.
- **superbot-next ORDERs 001–023 — all acked/done.** No open agent-side orders.

---

## §6 — Settings / provisioning (owner-only console; batch separately)

Console/settings clicks agents cannot do:
1. **websites `BAKE_PAT` secret** (ASK-0008): add a PAT with PR-write as an Actions secret → nightly bakes self-land (D4-A).
2. **websites auto-merge draft-gap patch**: land the staged workflow patch (needs owner provenance) → sweeps the 8 green drafts (§2 gate).
3. **superbot-idle — make `pytest` a required check** (OA-003): Settings→Branches→main→add `pytest`. Until then green ≠ tested.
4. **gba-homebrew — arcade go-live**: Settings→Pages source "GitHub Actions", then run "Deploy web arcade to Pages" on main; verify https://menno420.github.io/gba-homebrew/ loads.
5. **gba-homebrew — add `nds-rom-build` + `substrate-gate` to main branch protection** required checks (currently not required — the red gate did not block merges).
6. **trading-strategy — "per-seat go"** to land `weekly-grading.yml` (D5).
7. **superbot-next — delete predecessor failsafe trigger** `trig_01UC7wiV3n5Vgs3RpSQt4gWz` (still ENABLED; agents platform-denied).
8. **venture-lab — enable repo write for the failsafe session** (git push → 403) OR accept observe-only.
9. **fleet-manager owner-queue residue**: settings items 5 (pokemon ROM required-check), 7 (next merge-queue), 9 (forge settings residue) + fleet decisions 44–67 — see `docs/owner-queue.md`.

---

*Verified live against GitHub 2026-07-17 by fleet-manager session `claude/owner-actions-0717` (PR #279). Source of truth is live GitHub state; re-verify any item if acting more than a few hours after this timestamp.*
