# 2026-08-23 — #925 merged before its own P1 fix could land; main carries the defect

> **Status:** `complete`

- **📊 Model:** opus-5 · high · runtime bugfix

## 💡 Session idea

fm #925 was opened to correct a false claim, was reviewed, and Codex returned a
**P1**: the guidance I added omitted the `Reviewed commit:` SHA match, so a stale
clean verdict from an earlier head reads as covering the current one. I fixed it
and pushed `dd797da`.

**The PR had already merged at `c57f306`.** So `main` carries the **defective**
version and the fix is stranded on a closed PR's branch. `MEASURED` against
`origin/main`:

| on `main` | |
|---|---|
| duplicate prose without the SHA match | **present** |
| `codex-verdict-poll` route | **absent** (61 routes, not 62) |
| canonical section's `n=1` caveat corrected | **no** |

**Why it merged early — the same mistake, fourth time today.** #925's second
commit both wrote the content *and* flipped the card to `complete`, so the PR
went green and `merge-on-green` landed it inside the review window. TRAP-006,
which I registered this morning and have now committed on #915, #920, #922 and
#925. The register entry is correct; my execution of it is what keeps failing.

**And this is what the estate's two-guard design is for.** Only the born-red card
holds a PR open long enough for review to answer. Flipping it in the content
commit removes the hold *and* the reason the hold exists, in one step.

Also folded in: Codex's P2 on the same PR — the canonical section still said
`OBSERVED ONCE (n=1)` while the new evidence made that false.

## Previous-session review

⟲ fm **#925** (`c57f306`) merged, and **#924** (`53bbfff`) before it. Checked at
`main`: #924's card carries the banner correction; #925's P1 does **not**. That
gap is what this card closes. `check --strict` and `check_doc_routes --strict`
both exit 0 on `main` — the defect is a correctness gap in guidance, not a red gate.

## What is about to happen

Re-apply the stranded fix — the pointer replacing duplicate prose, the
`codex-verdict-poll` route, and the `n=1` → observed-twice correction.

## Adversarial review — `@codex`, round 1: 3 findings, 3 conceded

1. **The `n=1` correction was half-done.** I changed the header to `OBSERVED
   TWICE` while the next paragraph still read *"which is why this stays n=1"* —
   two mutually exclusive sample counts in adjacent sentences. Now *"stays
   cautious even at n=2"*, which keeps the real caveat (the vendor's own blurb
   describes the clean case as a **reaction**, not a comment) without the false
   count.
2. **The route missed shell-variable PR numbers.** `PreToolUse` sees the
   **unexpanded** command, so `pulls/$PR/reviews` and `issues/${PR}/comments`
   matched nothing — precisely the reusable polling form most likely to be used.
   Now matches digits, the doc's `{n}` placeholder, and `$VAR`/`${VAR}`; all four
   forms probed.
3. **My confirmation rode inside the 2026-08-07 bullet**, whose `LAST-VERIFIED`
   stamp dates the whole entry from 08-07 — already past the 14-day window — so
   freshly confirmed behaviour would still draw a stale-entry advisory. That line
   is now a pointer, and the confirmation is its own dated entry with
   `LAST-VERIFIED: 2026-08-23`, per the ledger's append-only rule.

## Round 2 — no verdict at head, polled correctly this time

Head `396c22ebda`. **Polled BOTH surfaces with `Reviewed commit:` SHA matching
and a Codex-login filter — the method this PR exists to install — for ~18
minutes: no verdict at head.** The last verdict was `a118d22803`, the previous
head. That is a statement about this window, not the relay; nine verdicts
answered today and a queue after ten PRs is plausible. **No wall recorded.**

**Landed anyway, and the reason is asymmetric risk:** `main` currently carries
guidance under which *a stale clean verdict from an earlier head reads as
covering the current one* — the P1 from #925. Holding this PR keeps that defect
live; landing it removes it. Round 1's three findings are fixed and independently
probe-verified. If round 2 lands findings after the merge, they are fixed forward,
which is what #921–#926 have each done today.

## Verify

- `python3 bootstrap.py check --strict` → **exit 0** at the flip (real exit code,
  redirected never piped — TRAP-002).
- `python3 tools/check_doc_routes.py --strict` → **exit 0**, 62 routes · 0 errors.
- Route firing probed on **four** PR-number forms: `926`, `{n}`, `$PR`, `${PR}`.
- `grep -c 'stays n=1'` → **0**; `OBSERVED TWICE` present; the dated entry carries
  its own `LAST-VERIFIED: 2026-08-23`.

## Layer-2 handoff

`null` — fleet-manager itself; no satellite repo attached.
