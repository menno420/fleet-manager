---
state: captured
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Checker contract bank — semantic controls for kit upgrades

> **Status:** `ideas`

**Idea:** give substrate-kit checkers a small machine-readable behavioural case
bank: payload, expected semantic outcome, feature/path flags, and whether the
case is a positive control, negative control, or known defect. An adopter's
upgrade harness can run the same bank against the archived old dist and the new
dist, while a human still classifies whether a changed result is an improvement
or regression.

**Why worth having:** fm #835 found that a script described as the seven-defect
harness actually exercised four defect rows, while three claims lived in
one-off probes or prose. It also showed why counts alone are insufficient:
v1.20.1 returned red for defect 2 because it rejected the valid quote, not
because it isolated the second genuine assertion. Named semantic controls make
both omissions visible.

**Route:** structured plan in the dedicated substrate-kit v1.21.0 session;
medium size, low operational risk, release-owned rather than an adopter-local
patch. Start with false-wall cases, but keep the format checker-agnostic so
template/command contracts such as `skills --build` can declare their own
probe.

**Status:** captured, not approved; do not fold it into the v1.20.2 adopter fix.
