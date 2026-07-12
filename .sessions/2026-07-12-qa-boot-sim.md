# 2026-07-12 — QA boot simulation of the v3 startup prompt set

> **Status:** `complete`

📊 Model: fable-5 · QA worker dispatched by coordinator · start 2026-07-12 (born-red at open)

## Declared at open (born-red)

QA boot simulation of the v3 startup prompt set (docs/prompts/v3/) — deliverable docs/research/2026-07-12-qa-boot-simulation.md. Per-prompt verdicts + defect list; PR parks READY+green for coordinator review, not merged by this session.

## Shipped (close-out)

- **Deliverable:** `docs/research/2026-07-12-qa-boot-simulation.md` (790 lines) —
  Wave 3 cold-boot simulation of all 9 v3 prompts (8 per-project startups +
  universal run unslotted) at fleet-manager@8056b7e, consolidating three QA
  worker slice reports; plus minimal `docs/research/README.md` (new dir index —
  kept to a single link on purpose; sibling research PRs #93–#96 also create it,
  resolve by union of link lists).
- **Verdict:** 9/9 **BOOTS-WITH-WARNINGS** (0 STALLS, 0 BOOTS-CLEAN) —
  **0 BLOCKER / 15 MAJOR / 29 MINOR.** Biggest defect class: the landing-path /
  self-arm contradiction between the assembled core's never-self-arm rule and
  per-seat doctrine (superbot Q-0127, idle arm-at-creation, venture-lab
  owner-merge-only disproven by enabler-landed #59/#60). Second: hours-scale
  census decay — facts baked 07-11/12 already overtaken at ship. Positives: the
  unslotted universal genuinely doesn't stall (line-9 derivation rule), all char
  budgets byte-exact, all named tools/args schema-real, mineverse PR #42 merge
  order verified safe. Fix-priority table for v3.1 included (P1 = landing
  doctrine + fm regen from post-#99 A + verify-at-boot census rails).
- **PR:** #102 — parks READY+green for coordinator review per the open
  declaration; this session does not merge or arm it.

## Walls hit

- None. (Gate red during the session was only the designed born-red hold.)

💡 Session idea: **prompt-freshness gate** — any startup prompt that bakes a
live fact (PR state, trigger id, CI/gate state, run conclusion) must phrase it
as "verify at boot; expected X as of <date>", never as a bare assertion. A
checker could lint the prompt files for bare volatile assertions (PR-number +
action-verb patterns, trigger ids outside a verify clause, "green/red at HEAD"
without an as-of date) — this simulation measured census decay as the dominant
defect class (8 of 15 MAJORs), and a lint would catch it at draft time instead
of at a QA wave.

⟲ Previous-session review: the prompts-v3-draft session (PR #98) shipped 20
consistent files with byte-exact self-measured char budgets — every one of the
15 recounted bodies/blocks matched its claim, which is unusually disciplined —
but it baked volatile census facts as assertions hours before they decayed
(venture #58 closed 48 min before the prompts merged; fm's own gen-#10 fact was
stale at its own merge commit), which this simulation quantified as the dominant
defect class. Improvement: census facts belong behind verify-at-boot rails
("expected X as of <date>, recheck"), and the seat files should be regenerated
from the final core at send time (fm B froze against pre-#99 A and lost its
landing path) — regen-at-send, not copy-at-draft.
