# 2026-07-11 — fleet restructure slice 3: owner queue + roster

> **Status:** `complete`

📊 Model: fable-5 · lane worker dispatched by coordinator (restructure program, slice 3 — final — of the 2026-07-11 owner directive) · start 2026-07-11 (born-red at open)

## Declared at open (born-red)

Close the 2026-07-11 restructure program's records loop: (1) update
`docs/owner-queue.md` to the 8-seat reality — paste-ready owner asks for
the claude.ai Project creates/renames/retires, the six instructions-body
pastes, the trigger cutovers per the slice-2 prompt files, and the
product-forge disposition (structured choice, recommendation first);
dedup/supersede existing entries per the file's own grammar. (2) Re-stamp
this repo's lane roster/manifest tables to the 8-seat reality with dated
attribution (roster.md is GENERATED — annotate in-grammar, never hand-edit
rows). (3) Heartbeat `control/status.md` as the deliberate last content
step. Branch `claude/restructure-roster` STACKED on
`claude/restructure-prompts` (PR #89); PR opens with base =
`claude/restructure-prompts`. Merge order #88 → #89 → this. No merges, no
auto-merge arming, no trigger calls, no superbot-repo edits.

## What landed (PR #91)

- **`docs/owner-queue.md` → the 8-seat reality.** New items, all dated
  (2026-07-11, restructure directive) with R17 six-field grammar + stable
  slugs: **C#34 OQ-RESTRUCTURE-PROJECTS** (rename-strongest-predecessor
  click path — venture-lab→Venture Lab, mineverse→SuperBot World,
  retro→Game Lab, idea-engine→Ideas Lab, substrate-kit→Self Improvement,
  superbot-next→SuperBot 2.0; Websites + Fleet Manager kept; archive list
  named; create-fresh alternative stated) · **C#35
  OQ-RESTRUCTURE-INSTRUCTIONS-PASTE** (8 pastes by registry path + version
  + byte count; bodies never inlined) · **C#36
  OQ-RESTRUCTURE-TRIGGER-CUTOVER** (one coordinator-prompt paste per seat;
  boots run rebind-then-delete; all 9 old trigger ids quoted verbatim from
  the slice-2 prompt files; websites keeps `trig_017H9Qb9…` but is owed the
  v3 prompt re-paste; fleet-manager unchanged — F-1 successor recipe) ·
  **E#37 OQ-FORGE-DISPOSITION** (structured choice: A retire-seat/keep-repo
  RECOMMENDED · B fold into Venture Lab · C keep as 9th seat; explicitly
  does NOT proceed on silence). Dedup: **C#15 OQ-PASTE-WAVE annotated
  SUPERSEDED** with a dated note — body kept verbatim (no paste ever got a
  receipt, nothing owner-side to undo); its websites half is carried by
  C#35/C#36.
- **`docs/fleet-triage.md` re-stamped:** Seat column added to all 19
  register rows (dated header note; verdicts/health untouched — the
  restructure moves the seat layer, not the repos) + a new dated section
  "2026-07-11 owner restructure — 8 standing seats" with the seat table:
  registry dir, constituents, constituent last-seen from roster gen #9
  (2026-07-11T20:25Z), seat state. Seat-level heartbeats written honestly
  as **not measured — no seat Project exists yet**; the retro coordinator
  has no heartbeat home (registry-only).
- **`docs/roster.md`:** appended in-grammar prose annotation ONLY (the file
  is GENERATED — rows untouched; they remain correct pre-cutover live
  truth). The annotation names the cutover dependency and the
  **gen_roster.py LANES follow-up**: the five new `<seat> failsafe wake`
  trigger names match NO existing lane token, so post-cutover generations
  would leave the new failsafes unattributed.
- **`control/status.md` heartbeat** (deliberate last content step,
  overwrite-own grammar): stack state, routed owner asks (slugs cited,
  R17 detail lives in the queue), follow-ups.

**Follow-ups (recorded, deliberately not done):** superbot
`docs/eap/fleet-manifest.md` re-stamp (cross-repo — NOT edited from here)
· `projects/README.md` MATRIX + paste-wave regen against the 8 seats
(forge row blocked on E#37) · gen_roster.py LANES token re-annotation
post-cutover · product-forge disposition execution on the owner's word.

**Pre-existing local state noted:** `.substrate/guard-fires.jsonl` carried
two uncommitted advisory/gate lines from the slice-2 session's check runs;
this session's own check runs append to the same telemetry log — committed
together at flip (append-only telemetry, same practice as #86/#87). The
`owner-action-fields` advisory on `control/status.md` predates this slice
and is advisory-by-design (asks live R17-structured in the owner queue;
the heartbeat cites slugs — the archive-prep precedent).

## 💡 Session idea

An **owner-queue supersession checker rule**: `check_owner_queue.py`
already probes cited-PR state; teach it one more cheap probe — an item
whose WHAT names a `projects/<dir>/` path that is now a pointer STUB (or a
version older than the registry header at HEAD) gets flagged
"stale-target: registry moved under this ask". This session's C#15
supersession was found by hand only because the restructure was
same-session context; a queue ask pointing at a stubbed/re-versioned
registry file is a mechanical drift class the custodian can catch at every
regen, exactly like merged-PR citations.

## ⟲ Previous-session review

Slice 2 (PR #89) was strong where it mattered: the cutover recipes carry
verbatim trigger ids with extraction receipts and honest "last committed
registry state — re-verify live" caveats, which is what let this slice
write a click-level owner cutover item without touching the trigger MCP.
One miss: slice 2 bumped `projects/websites/coordinator-prompt.md` to v3
but left owner-queue C#15 telling the owner to paste "the v2 wake prompt"
— the queue and the registry disagreed on the restructure branch for a few
hours (caught + superseded here). Workflow improvement: a slice that bumps
any registry `vN` should grep `docs/owner-queue.md` for the old version
string in the same session — one grep, and the queue never lags the
registry it points at.
