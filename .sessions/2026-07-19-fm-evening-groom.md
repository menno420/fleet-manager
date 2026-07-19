# 2026-07-19 · fm evening groom — harvest post-14Z 💡 set + build top slice

> **Status:** `complete`

Declared born-red: planning+tooling slice — (a) GROOM: harvest all un-landed 💡
ideas from today's post-14Z session cards into a dated ranked section appended
to `docs/planning/2026-07-19-next-slices.md` (build-worthy vs park vs drop,
honest one-liners); (b) decide-and-flag the top S-sized pick and BUILD it this
session (stdlib, Q-0105 header, selfcheck, verbatim ground-truth demo run);
(c) `control/status.md` heartbeat + baton (owner items unchanged; next slice =
groom's #2 pick; ~22:00Z snapshot cycle). RAW-DATA; no trigger-MCP calls from
this venue.

## What happened

- **Groom (a):** "Evening re-groom (2026-07-19T20:15Z)" section appended to
  `docs/planning/2026-07-19-next-slices.md`. Ranked build-worthy: (1)
  `gen_idea_backlog.py` **S** · (2) wake-without-work detector in
  `check_lane_liveness.py` **S/M** · (3) I8-reads-lane-fence **M** · (4)
  `r30_merge_check --post` **M**. Parked/dropped/routed with one-liners:
  classifier-safe naming (batch with next emitter touch), park-label
  vocabulary (blind spot currently empty per the 16:15Z run),
  `--probe-runs` (cron observably delivering, gen #111), `covers:`
  (owner-ask pending), registry-growth trendline (delta note covers),
  kit-graduation (routed to substrate-kit lane), `gen_hub_queue_baton.py`
  (inputs not fleet-wide), emitter `--from-export` (let V1 catch one live
  lag first).
- **Decision (decide-and-flag):** top pick = `gen_idea_backlog.py` — the only
  S-sized candidate with zero network/classifier surface in this venue, and
  meta-leverage: every future groom starts from a machine-built list instead
  of a ~19-card hand-grep.
- **Build (b):** `scripts/gen_idea_backlog.py` (stdlib-only, Q-0105
  unverified header with provenance/neighbors/kill-switch, advisory — NOT
  wired into `bootstrap.py check`). Harvests top-level `💡` bullets (both
  `- 💡 **…` and `- **💡 …` forms; inline mid-prose 💡 ignored), extracts a
  title (first non-header bold span, boilerplate-stripped fallback),
  cross-references `docs/planning/*.md` by >=60% title-token overlap
  (best-hit doc, min 2 tokens), flags ungroomed ideas older than
  `--max-age-days` (default 2). Modes: write / `--stdout` / `--check`
  (drift, exit 1) / `--selfcheck`. Generates
  `docs/planning/idea-backlog.md` (`audit` badge, GENERATED + NOT SOURCE OF
  TRUTH marker, linked from `docs/planning/README.md`). Two heuristic
  weaknesses seen in the first real run were fixed in-session (fallback
  title kept the dedup header; groom pointer picked a generic large doc on
  single-token hits).
- **Ground-truth runs (verbatim):**
  - `python3 scripts/gen_idea_backlog.py --selfcheck` →
    `selfcheck: OK — 6 harvest/format assertions + determinism`
  - `python3 scripts/gen_idea_backlog.py` → `wrote docs/planning/idea-backlog.md`
  - `python3 scripts/gen_idea_backlog.py --check` → `CHECK: backlog current`
  - Generated summary line: `45 idea block(s) across 244 card(s) · 3
    ungroomed · 3 ungroomed older than 2d.` — the 3 ungroomed are all
    pre-2026-07-16 card ideas (e.g. `2026-07-15-wake-1126z-queue-sweep.md`
    "I9 heartbeat-vs-registry coherence invariant" — `**ungroomed** ⚠ >2d`),
    exactly the silent-rot class the harvester exists to surface. (The
    committed backlog says 46/244: the flip regen harvested this card's own
    💡 ender — the tool caught its own session's idea, dogfood working.)
- **Heartbeat (c):** `control/status.md` — `updated: 2026-07-19T20:20Z`, 20:2xZ
  section + Baton (owner 2 items unchanged; next slice = wake-without-work
  detector; ~22:00Z snapshot watch). Routine claims re-verified at 20:18Z
  (`verify_routine_state.py` → `VERDICT: OK — heartbeat routine claims match
  the export (3 claim(s) verified).`); fence `updated` bumped via
  `emit_routine_claims.py` (dogfood; volatile fields untouched — export
  truth; round-trip verified by the emitter itself).
- **Checks:** `bootstrap.py check --strict` → designed born-red HOLD only
  pre-flip; `check_docs_links.py` → `CLEAN — every intra-repo link in 260
  file(s) resolves`.

## Enders

- 📊 Model: fable-5 (worker, remote container venue; coordinator-dispatched).
- 💡 **Session idea (dedup-checked — `docs/planning/idea-backlog.md` (the new
  machine-built list — first dogfood use), `docs/planning/*.md`, `docs/ideas/`;
  no shipped-state concept anywhere):** **teach `gen_idea_backlog.py` a
  `shipped → scripts/<file>` status.** The backlog currently conflates
  "groomed into a plan" with "actually built": e.g. the volatile-drift and
  label-hygiene rows read `groomed → 2026-07-19-next-slices.md` though both
  SHIPPED today (#365/#370). Cheap disambiguation: when an idea title carries
  a backticked script/flag name (`scripts/x.py`, `check_y.py`, `--flag`),
  test it against files on disk / the named script's argparse surface and
  print `shipped → scripts/x.py` above `groomed`. Turns the backlog into a
  true lifecycle index (ungroomed → groomed → shipped) and makes the ⚠ rot
  flag precise (a shipped idea can never rot).
- ⟲ **Previous-session review (PR #374, 18Z cycle records slice):** strong
  cycle — third-escalation SBW honesty (annotated, not re-litigated), and the
  `OQ-LABEL-DEFS-DELETE` → Resolved-verified re-scope correctly used the
  checker's own run as the item's VERIFY instead of a hand-claim. Improvement
  it surfaces: its baton queued "fresh planning groom when new ideas
  accumulate" with no way to measure *accumulate* — this session had to be
  told by the coordinator that the threshold was crossed. The backlog
  generator built here makes that measurable (`N ungroomed` in the generated
  summary line); the follow-on is for wake batons to cite that count instead
  of prose.
- **Doc audit:** everything durable is homed — groom judgment →
  `docs/planning/2026-07-19-next-slices.md` evening section; machine index →
  `docs/planning/idea-backlog.md` (linked from `docs/planning/README.md`);
  live posture + baton → `control/status.md`; decision rationale → this card
  + the plan section + the status section (same one line, three homes by
  design). `check_docs_links.py` CLEAN (260 files); `bootstrap.py check
  --strict` green at flip. Nothing chat-only left behind.
- **Guard fires:** 4 records appended by the strict gate this session
  (allowlist suppressions with verdicts), committed with the work commit
  (`.substrate/guard-fires.jsonl` — do not revert).
- **Claim:** `control/claims/claude-fm-evening-groom.md` deleted in this flip
  commit.
