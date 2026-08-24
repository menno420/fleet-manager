# 2026-08-24 — E1 follow-up: the aphorism that survived its own qualification

> **Status:** `in-progress` — branch `claude/final-eap-mail-x2s9kx` restarted from
> `origin/main` at `07591dd` (fm #943, merged). Born red on purpose.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

Owner-review, immediately after fm #943 merged, asked whether *"Agents append;
they do not retract"* was proven or a tendency in one sample. **It was a
tendency, stated as a universal, and it had reached `main`.**

The paragraph around it is the sharp part. It reads, in order:

1. the mechanism behind the audit's **highest-cost** findings,
2. *"(We did not classify all 101 by mechanism, so read this as the shape of the
   worst ones, not a majority.)"* — a correct, explicit scope limit,
3. **"Agents append; they do not retract."** — the universal anyway.

**The qualification was appended and the unqualified claim was not retracted.**
That is the exact defect the sentence describes, committed in the sentence
describing it — the fourth instance in two sessions of a lesson failing to bind
the line being written. Six adversarial rounds passed over it; two of them
narrowed the *neighbouring* sentences (round 3 scoped "the dominant class",
round 6 scoped "every review a human actually performs") and left the bolded
aphorism between them untouched, because it reads as a summary rather than a
claim.

## previous-session review

fm #943 landed the sweep, the draft and `check_claim_propagation.py`. This
session's fix is a defect in what that PR merged, found one turn after it landed.

## What landed

- The claim scoped to its sample in the outbound mail.
- `agents-append-universal` added to `tools/check_claim_propagation.py` (13
  patterns now), so the wording cannot return silently.
- A pre-send flag on the 97.5 % figure — see below.

## Flagged, not changed: the 97.5 % has two readings in its own source

`MEASURED` 2026-08-24 by arithmetic on the audit's own table, not by a fresh
database query. [`2026-08-14-railway-websites-audit.md`](../docs/findings/2026-08-14-railway-websites-audit.md)
§ 5 prose says **97.5 %** of the 939 MB `public` schema; its table rows sum to
668 + 135 + 122 = **925 MB**, which is **98.5 %** of 939. The gap is plausibly
exact-bytes-versus-rounded-MB, but **it was not resolved here and must not be
resolved by picking one.** The mail carries the audit's own 97.5 % with its
2026-08-20 date. Owner call 2 already says re-measure before sending; this is
the concrete reason to.
