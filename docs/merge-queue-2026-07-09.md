# Merge queue — 2026-07-09 (verified at live HEAD, 22:41Z)

> **Status:** `owner-guidance`
>
> One row per open PR across the fleet's 10 repos, **re-verified against live
> GitHub at 2026-07-09T22:41:00Z** (state, CI on head, mergeable state — not
> the earlier draft's cached values; playbook R2). Paste this into your merge
> session and work top to bottom. Dispositions are pre-chewed (R16):
> **MERGE** = click it; **SKIP** = leave it, reason given.
>
> Repos with ZERO open PRs at verification: superbot, websites,
> trading-strategy, codetool-lab-fable5, codetool-lab-opus4.8,
> codetool-lab-sonnet5. No stale/abandoned claude/* PRs anywhere.

## The queue

| Repo | PR | Title (short) | State at 22:41Z | Disposition | Pre-merge step |
|---|---|---|---|---|---|
| superbot-next | [#95](https://github.com/menno420/superbot-next/pull/95) | band-5 replay/live seams (D-0062) | ready · 11/12 checks green (`gate`, `tests`, `golden-parity`, `code-quality` all green; only `report` red — pre-existing infra failure, also red on merged #96: missing `parity` DB) · **mergeable_state: DIRTY (conflict with main — NEW since the draft; main moved)** | **MERGE — after a conflict fix** | ⚠️ Can't merge as-is: GitHub reports a merge conflict. Tell the superbot-next session/chat: "PR #95 conflicts with main — merge main into the branch, resolve, re-push." Then merge on green. (Follow-up, separate: fix the `report` job's missing `parity` DB.) |
| substrate-kit | [#49](https://github.com/menno420/substrate-kit/pull/49) | make_seed `yield`-keyword fix + prepare smoke (pin-path) | ready · all 3 checks GREEN · `do-not-automerge` · mergeable_state: behind (base moved; still one-click mergeable — repo doesn't require up-to-date branches) | **MERGE (owner ratification — your click IS the review)** | None. Ruling on the `do-not-automerge` label: it's the kit's pin-path integrity law (the lab never merges its own oracle change) — the label correctly held it FOR YOU; merging it is the intended act. **Highest-value click: unblocks bench B1 run-3.** |
| substrate-kit | [#26](https://github.com/menno420/substrate-kit/pull/26) | PL-011: adoption isn't done until ENGAGED (program law) | ready · all 3 checks GREEN · `do-not-automerge` · mergeable_state: behind (same benign lag) | **MERGE (owner ratification)** | None. Same ruling: program-law PRs ride `do-not-automerge` by kit §8.3; merge = ratify, comment on the thread to veto. |
| superbot-games | [#14](https://github.com/menno420/superbot-games/pull/14) | mining gen-1 wind-down succession package | ready · `substrate-gate` GREEN · mergeable_state: **clean** | **MERGE** | None. Docs-only; parked solely by the agent self-merge wall, not a review hold. |
| superbot-games | [#5](https://github.com/menno420/superbot-games/pull/5) | mining pure-domain port (18 modules, 62 tests) | **draft** · `substrate-gate` GREEN · mergeable_state: clean | **MERGE (owner-gated by design — already owner-queue item 3)** | Click "Ready for review" first, then merge. Its own description reserves ready+merge for you. |
| superbot-games | [#11](https://github.com/menno420/superbot-games/pull/11) | mining grid-encounters first slice (pure domain) | **draft** · `substrate-gate` GREEN · stacked: base = `mining/port-pure-domain` | **SKIP for now** | Only after #5 merges: retarget base to `main` (Edit next to the title → base dropdown), then review/merge at your pace — explicitly owner-gated by its description. Do this AFTER #5 or the diff misleads. |
| fleet-manager | [#10](https://github.com/menno420/fleet-manager/pull/10) | this session (merge-authority policy + env archetypes + this doc) | ready · lands itself (auto-merge/merge-on-green per the new policy) | **no action** | None — listed for completeness; it self-lands on green. |

**Totals: 7 open · 4 MERGE now (#49, #26, games#14, games#5) · 1 MERGE after conflict fix (next#95) · 1 SKIP-until-#5 (games#11) · 1 self-landing (fleet-manager#10).**

## Changes vs the earlier draft sweep

1. **superbot-next #95 went from "conflict unlikely" to a REAL conflict**
   (`mergeable_state: dirty`) — main moved under it. Disposition upgraded
   with the pre-merge step above.
2. **kit #49/#26 mergeable_state resolved** from `unknown` to `behind` —
   benign (merge button works; the repo doesn't require up-to-date branches).
3. **games #14/#5 confirmed `clean`**, all CI greens re-confirmed on current
   heads. Zero-PR repos re-confirmed. fleet-manager #10 (this session) added.

## Note for gen-2 (context, no action)

Under the merge-authority policy shipped this same PR
([`gen2-blueprint.md`](gen2-blueprint.md) §1/§2, owner directive 2026-07-09),
gen-2 lanes never park PRs for review — they land on green and flag
second-eyes items in [`review-queue.md`](review-queue.md). The four
owner-gated rows above are all **gen-1 carve-outs** (kit pin-path/program-law
integrity, mining's explicit owner-gate) and stay valid.
