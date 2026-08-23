# 2026-08-23 — "superbot is frozen so it won't grow" is not enforced by anything

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

The owner's stand-in review challenged a sentence I had shipped in the E1 evidence
pack: *"`superbot` is also frozen, so that headroom is not closing."* The question
was exact — **what enforces the freeze, or is this inferred from inactivity?**

**It is inferred, and it is wrong.** `MEASURED` 2026-08-23 against
`GET /repos/menno420/superbot`:

- `archived: false` · `disabled: false` — the repository is **writable**.
- `open_issues_count: 9` — eight dependabot PRs plus one issue, all mergeable.
- `pushed_at: 2026-08-20T23:17:54Z` — three days before this claim was written.
- Its newest session card is **`2026-08-13-substrate-kit-v1-21-0.md`**, so
  `.sessions/` grew **ten days ago**, not never.
- Measured earlier the same session: **64 PRs merged into `superbot` in 14 days.**

"Frozen" in this estate is an **editorial status** (OD-16: the behavioural oracle
for the game-community bot) — a directive about intent, not a technical lock.
Nothing prevents a session from adding cards there, and sessions demonstrably do.

**Why it matters beyond the wording:** the sentence was load-bearing for a
*ceiling* claim. `superbot`'s `.sessions/` holds 969 cards against the Contents
API's 1,000-entry listing cap — **31 of headroom** — and I dismissed the risk by
asserting the directory was static. It is not. The honest version keeps the
measurement (not hit today) and drops the false reassurance about why.

## Previous-session review

⟲ fm **#921** (`a9390a7`), **#920** (`6376999`), **#919** (`e2fe0bb`), websites
**#512** (`478cb13`) — all merged. Checked at `main`: the pack's census recipe run
verbatim emits `26 / 19 / 4535` matching its table, and the live review site
states the programme concluded on 7 of 7 pages. This card corrects one sentence
those PRs shipped.

**Carried lesson:** fm #915 and #920 merged in under a minute with zero reviews
because the card was flipped before the push (TRAP-006). This card is pushed
**red, as its own commit, before any content work** — the discipline that worked
on #921.

## What is about to happen

Correct the sentence in the pack; keep the measurement, drop the inference.

## Verify

(filled before the flip — real exit codes, never after a pipe: TRAP-002)
