# The `estate` structure proposal — what is behind each door

> **Status:** `plan` · plan input under OD-26 § 13. Three short files, one
> question each; the owner answered the six letters they raised on 2026-09-01
> (all defaults). Companion measurements:
> [`../../findings/2026-09-01-fleet-manager-measured.md`](../../findings/2026-09-01-fleet-manager-measured.md).
> His words that evening:
> [`../../findings/2026-09-01-owner-direction.md`](../../findings/2026-09-01-owner-direction.md).

| File | The question it answers |
|---|---|
| [`structure.md`](structure.md) | The tree for `estate`, two levels deep, the six-read boot path with a token budget, the nine file rules a check can enforce, the door-test walks. |
| [`failure-to-mechanism-map.md`](failure-to-mechanism-map.md) | Which recorded mistake happens at which moment, and which hook or check belongs there — fifteen moments, seven covered today. |
| [`kit-prerequisites-and-migration.md`](kit-prerequisites-and-migration.md) | What substrate-kit must change before the seed (K1–K7), the carry · distill · archive table for fleet-manager's living core, the acceptance test, the build order. |

**Built from it, 2026-09-04 — the build order's step 2 is done.** K1–K5 landed on
substrate-kit `main` as
[kit #590](https://github.com/menno420/substrate-kit/pull/590), squash-merged
`8a83c73`, **unreleased**. What is proven, deferred and still owner-gated is in
[`../../repos/substrate-kit/README.md`](../../repos/substrate-kit/README.md)
§ *Thread: K1–K5*. The step that follows is step 3 — the seed-set folder
READMEs and the migration manifest — **not** the seed itself. (The build
order is question E, answered 2026-09-01; its decision id is stamped at its
one home, `findings/2026-09-01-owner-direction.md`.)

Decided from it, in `docs/decisions.md` dated 2026-09-01: the archive shape, the file-length caps, the build order, and hooks in the hub repo only by design (their one citing home is `findings/2026-09-01-owner-direction.md`). Open: G, the automerger.
