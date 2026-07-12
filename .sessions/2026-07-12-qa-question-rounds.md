# 2026-07-12 — QA question rounds against the v3 prompt set

> **Status:** `complete`

📊 Model: fable-5 · QA coordinator + parallel question-round workers · start 2026-07-12 (born-red at open)

## Declared at open (born-red)

QA question rounds against the v3 prompt set (R1–R6 perspectives); deliverable docs/research/2026-07-12-qa-question-rounds.md.

## Results

Six parallel question rounds interrogated the v3 prompt set (docs/prompts/v3/
at main 8056b7e, PR #98) — 89 hard questions, answered strictly from the v3
texts (quote-or-fail; fleet-lore-only answers scored UNANSWERED).

Scores (answered/ambiguous/unanswered):

- R1 cold-boot: 3/8/4 of 15
- R2 mid-session wall: 5/5/5 of 15
- R3 session end + succession: 6/6/3 of 15
- R4 owner steering: 5/6/4 of 15
- R5 cross-seat: 3/5/6 of 14
- R6 security/safety: 5/9/1 of 15
- **Overall: 27 A / 39 AMB / 23 UN of 89**

Deliverable: `docs/research/2026-07-12-qa-question-rounds.md` — full per-round
gap inventory (all 62 AMBIGUOUS/UNANSWERED questions with readings, fixes,
target artifacts), 11 cross-round themes, and a P0/P1/P2 fix-priority table
for v3.1 (12 P0 rows, led by the unscoped account-wide trigger deletion that
three rounds independently flagged as a sibling-lane kill risk). Index:
`docs/research/README.md` (new directory, living-ledger root).

💡 Session idea: run these question rounds as a standing regression — re-ask
the 62 gap questions against every future prompt revision and track the
answered-rate as the prompt set's test suite; a fix that doesn't move a
question from AMBIGUOUS/UNANSWERED to ANSWERED didn't fix it.

⟲ Previous-session review: the v3 draft session (PR #98) shipped a strong
per-project paste set, but left 5 of 8 seat pastes carrying the known
pacemaker-vs-ender contradiction its own README flags as defect #6 — the next
revision should patch all seats, not exemplars: a defect acknowledged in the
registry but live in the pastes is still a live defect.
