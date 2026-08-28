# substrate-kit — the entry point

> **Status:** `living-ledger` · true as of **2026-08-28**
>
> **What this is:** fleet-manager's entry point for `menno420/substrate-kit` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The kit's own `control/status.md` (freshest
> single surface) and `docs/PROJECT-CLOSEOUT.md` win on its state; the PL
> register (`docs/program/rulings.md`) is program law for every adopter; the
> live tree wins over everything. Depth files are **not yet written** —
> created by the 2026-08-21 fleet review (Tier-1, "cleared to build" since
> 2026-08-08) and carries only the entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`substrate-kit` is the estate's **method kit**: a portable agent
workflow/memory substrate shipped as a single stdlib-only `dist/bootstrap.py`,
adopted across the estate (12 registry rows), plus the **PL register** —
program law that binds every adopter — and the generated adopter registry
`docs/adopters.md`. **v1.21.0** since 2026-08-13 (cut, published, distributed;
kit #581–#586). The Self-Improvement seat closed 2026-07-21; releases are cut
by owner-directed sessions using this repo's `release` →
`upgrade-distribution` skills. `MEASURED` 2026-08-21: 0 open PRs — records
still carrying "#552 parked for owner ratification" describe July (**#552
MERGED 2026-08-04**). ~~Its own `docs/current-state.md` body still says
v1.20.2~~ — **reconciled 2026-08-28 (kit #588)**: a dated reconcile block
now heads that file; `control/status.md`'s stale #552 line fixed in the
same PR.

## Threads

### Thread: the owner-directed review round — **session 3 DONE (the kit-tree truth pass + the two owed checks; current-state reconciled); the letters still wait**

The owner ordered a kit review round in the second overnight 2026-08-27→28
hub sitting (*"review it again and improve it"* — verbatim record + the
four-step method:
[`../../findings/2026-08-28-owner-direction-agent-autonomy.md`](../../findings/2026-08-28-owner-direction-agent-autonomy.md),
**OD-24**). **Session 1** (overnight 2026-08-28, steps 1–2):
[the genesis dig](../../findings/2026-08-28-substrate-kit-genesis-dig.md) —
three-era history, twelve classified gaps (dominant
**unenforced/unrouted**), the rival-hypothesis verdict, the §10
dispositions table (recommendations only, execution owner-gated).
**Session 2** (2026-08-28, daytime) executed §11 items 1–2 and 4:

- **kit #587 (MERGED on green after three Codex rounds):** the kit-tree
  worklist pointer (gap #5 — `kit:docs/NEXT-TASKS.md` superseded into the
  route) and the false-negative family fixed (worklist rows 13/17/18, each
  reproduced against the published asset first; pre-push adversarial
  verification + Codex R1 5/5 and R2 6/6 conceded-and-fixed; R3's 4
  verified and deferred as worklist **row 35** under the two-re-review cap
  — tally 5→6→4, measured non-convergent). Fixes ride kit `main`
  unreleased; the cut stays owner-paced.
- **The item-4 audit:**
  [the router band re-read](../../findings/2026-08-28-router-band-reread.md)
  — all 208 body sections superbot:Q-0063–Q-0272, 59/59 quotes
  machine-verified (ledger committed in its appendix); seven genesis-dig
  claims narrowed, each routed in place at the claim site; a carrier
  census of standing owner rules (five absent from every fm document, the
  rest in seat-era/reference surfaces or carrying a different facet);
  genesis precedents mapped onto the gap table; its two new owner asks
  queued (`OQ-KIT-PROMPT-DOCTRINE` · `OQ-EAP-SPEND-WINDOW-MOOT`).
- **The morning letters (Move-1 GO · journal · §10 confirmations) were
  checked first and remain UNANSWERED** — everything owner-gated stayed
  gated. The re-read adds superbot:Q-0101 as evidence for the journal
  letter.

**Session 3** (2026-08-28, daytime — the round's next audit):
[the kit-tree truth pass](../../findings/2026-08-28-kit-tree-truth-pass.md)
— the kit's whole committed doc surface (187 files at `a9acc41`, the dig's
skipped subdirectories + `docs/succession/` included) judged per-doc with
adversarial verification (31/36 upheld, 5 minor corrections applied), and
**both owed checks answered**: PL-002's canonicalization **preserves**
Q-0241's rebuild-only scope (the one drop is a Q-0241-vs-Q-0271 provenance
mislabel in three derived copies of one owner-profile sentence), and
Q-0214's delete-with-tombstones retention **substantially shipped** as the
v1.0.0 economy engine — never run on the kit's own 343-card corpus. The
headline: 103 of 187 files are honest self-bannered history; the failure
class is ~20 current-truth-voiced files, catalogued as recommendations in
the finding's §5 (a future doc-surface truth sweep; nothing owner-gated).
**Executed in the kit's venue: kit #588** — `docs/current-state.md`
reconciled (the supersede table's open item 4) + `control/status.md`'s
false #552 line, through the kit's full discipline; Codex R1's two P2s
conceded-and-fixed (the release-path wording is now precise: tag push
owner-side canonical, workflow_dispatch the only agent-runnable trigger).
`OQ-KIT-P10-REQUIRED-CHECKS` retired by a live rules read (kit-quality is
the one required check — the ci.yml legacy-alias deletion is now unblocked
agent work).

**Next session:** the letters' answers when they come; otherwise the
worklist's restated order — the work-destroyers 26, 29, 33 (+34/35) — or
the truth pass §5's doc-surface sweep (records-only, sized one session), or
the round's routing work (gap #3's shipped-but-unrouted reflection miner).
Nothing GOs the held packets; AGENTS.md stays parked for the round.

### Thread: the v1.21.0 follow-up worklist — **open, lives in THIS repo, not the kit**

The kit's next worklist is fleet-manager's
[`../../findings/2026-08-13-substrate-kit-v1210-followups.md`](../../findings/2026-08-13-substrate-kit-v1210-followups.md)
— Codex findings on the vendored v1.21.0 (count the rows from the file;
rows 13/17/18 consumed by kit #587, row 35 added from its R3), fix order
restated at its tail (the work-destroyers 26/29/33 now lead — the false
negatives are consumed). ~~`MEASURED` 2026-08-21: the kit's own tree
references it **nowhere**~~ — **closed 2026-08-28 (kit #587):**
`kit:docs/NEXT-TASKS.md` is superseded into a routed pointer to this
worklist and the round thread, reachable from the kit's boot path via its
`current-state.md` links. Start any kit session from that finding.

### Thread: adopter currency — **3 stale rows + 5 invisible adopters** (owner-paced)

Registry at its 2026-08-14 regen: 9 of 12 rows current at v1.21.0; stale:
`superbot-games` v1.20.1 (⚠ DRIFT ×3 self-report rows — the hop is
**owner-paced** — "no adopter yet", owner 2026-08-14), `trading-strategy` v1.20.2 (skipped
pending its archive decision), `pokemon-mod-lab` v1.15.0 (owner-held).
**Adopters are invisible to the registry** where the scan roster
`docs/fleet-repos.txt` omits them: `sim-lab` (kit v1.15.0), `superbot-idle`
(v1.16.0), `product-forge` (v1.7.0 — the actual oldest, archive-bound
post-R2), and — `MEASURED` 2026-08-21, the couch-legend seed session —
**`spider-swing` (v1.20.2) and `couch-legend` (v1.21.0, seeded that day)**
too: neither is in the roster nor in the registry's 12 rows — a
registry-driven rollout can never find any of the five. The roster fix is
kit-side (this thread already carries it); until then the registry
undercounts the estate's adopters.
Rollout ask: `OQ-KIT-V1-21-RELEASE` in [`../../owner-queue.md`](../../owner-queue.md).

### Thread: the provenance mandate — **kit-side open plan** (paused)

`docs/planning/2026-08-06-provenance-review-mandate.md` (owner-specified; its
§ 8 build order is authoritative — the kit's current-state explicitly refuses
to duplicate it). The blast-radius exporter has no engine code yet. Read
fleet-manager's
[`../../findings/2026-08-06-provenance-mechanism-measured.md`](../../findings/2026-08-06-provenance-mechanism-measured.md)
before touching kit #580's territory. Also deferred by design: the `intake`
skill graduation (roadmap § 7) — its own session.

## Before you attach / modify — the traps, measured

- **`src/engine/` is source of truth; `dist/bootstrap.py` is GENERATED and
  byte-pinned** — after any engine edit run `python3 src/build_bootstrap.py`;
  CI reds on divergence.
- Gate: **`kit-quality` is the ONE required check** (live rules re-verified
  2026-08-28); local convergence is `python3 scripts/preflight.py`. Legacy
  alias jobs mirror it without running anything (`OQ-KIT-P10-REQUIRED-CHECKS`
  resolved 2026-08-28 — deleting the aliases from `ci.yml` is now unblocked
  agent work for a build session).
- **Releases: `workflow_dispatch` on `release.yml` is the only AGENT-runnable
  path** (the git proxy 403s tag pushes — path quirk, not a wall); the
  workflow's other supported trigger, a hand-pushed `v*` tag, is owner-side
  canonical (its own header; precision from Codex R1 on kit #588). Verify
  with `scripts/verify_release.py` / three-way sha256. The `release` skill
  here is the procedure.
- `docs/adopters.md` is **GENERATED — never hand-edit**; regenerate with
  `python3 dist/bootstrap.py currency` (sole writer: this repo).
- Engine code is stdlib-only, no print/assert/subprocess (CI lint leg).

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to `substrate-kit` in
any record this review read. Add the pointer here when one exists.
