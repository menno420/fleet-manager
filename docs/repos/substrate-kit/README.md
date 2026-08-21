# substrate-kit — the entry point

> **Status:** `living-ledger` · true as of **2026-08-21**
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
MERGED 2026-08-04**), and its own `docs/current-state.md` body still says
v1.20.2; trust `control/status.md` + the tree.

## Threads

### Thread: the v1.21.0 follow-up worklist — **open, lives in THIS repo, not the kit**

The kit's next worklist is fleet-manager's
[`../../findings/2026-08-13-substrate-kit-v1210-followups.md`](../../findings/2026-08-13-substrate-kit-v1210-followups.md)
— Codex findings on the vendored v1.21.0, grown to **23 rows** (as of
2026-08-14, fm #858 — count from the file, not from here), fix order
restated at its tail ("the false negatives now lead"). `MEASURED` 2026-08-21:
the kit's own tree references it **nowhere** — a session booting on the kit
alone cannot find its own worklist. Start any kit session from that finding.

### Thread: adopter currency — **3 stale rows + 2 invisible adopters** (owner-paced)

Registry at its 2026-08-14 regen: 9 of 12 rows current at v1.21.0; stale:
`superbot-games` v1.20.1 (⚠ DRIFT ×3 self-report rows — the hop is
**owner-paced** — "no adopter yet", owner 2026-08-14), `trading-strategy` v1.20.2 (skipped
pending its archive decision), `pokemon-mod-lab` v1.15.0 (owner-held).
**Adopters are invisible to the registry** where the scan roster
`docs/fleet-repos.txt` omits them: `sim-lab` (kit v1.15.0), `superbot-idle`
(v1.16.0), and `product-forge` (v1.7.0 — the actual oldest, archive-bound
post-R2) — a registry-driven rollout can never find them.
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
- Gate: **`kit-quality` is the ONE required check**; local convergence is
  `python3 scripts/preflight.py`. Legacy alias jobs mirror it without running
  anything (`OQ-KIT-P10-REQUIRED-CHECKS` would retire them).
- **Releases go ONLY via `release.yml` `workflow_dispatch`** (the git proxy
  403s tag pushes — path quirk, not a wall); verify with
  `scripts/verify_release.py` / three-way sha256. The `release` skill here is
  the procedure.
- `docs/adopters.md` is **GENERATED — never hand-edit**; regenerate with
  `python3 dist/bootstrap.py currency` (sole writer: this repo).
- Engine code is stdlib-only, no print/assert/subprocess (CI lint leg).

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to `substrate-kit` in
any record this review read. Add the pointer here when one exists.
