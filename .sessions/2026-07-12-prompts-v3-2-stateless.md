# 2026-07-12 — prompts v3.2: strip volatile state from startup artifacts

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
lane worker (owner correction 2026-07-12, dispatched)

## Declared at open (born-red)

Owner correction: startup prompts must never carry volatile state (PR numbers,
CI colors, trigger ids asserted as facts, "do X now" items) — they direct
agents to the repo documents where current state lives. This session: strip
the 9 startup artifacts (8 B files + A template; audit the ender), replace
FIRST WORK ORDERS with durable WORK SOURCES ladders, relocate still-valid
now-actions as ORDERs to the owning repos' inboxes (verified at HEAD first),
regen B files, bump to v3.2, update owner-queue C#34, heartbeat.

## Close-out

Shipped on fm PR #108:

- `docs/prompts/v3/universal-startup.md` → **v3.2**: STATELESS role-brief
  sentence; `{{OLD_TRIGGER_IDS}}` → `{{OLD_TRIGGER_SOURCES}}` (fills name
  records, never literal ids); LANDING PR citation + GEN-3 SHA pins replaced
  with durable pointers; drift class **D-9** minted.
- `tools/regen_b_files.py`: every seat's FIRST WORK ORDERS → a durable
  **WORK SOURCES ladder** — (a) control/inbox.md at HEAD, (b) the seat's
  named state docs (every named file existence-verified at that repo's HEAD
  2026-07-12; zero gaps), (c) the standing mission. All volatile slot facts
  stripped; durable rails kept (track isolation, security-before-secrets
  ordering, research-only). 8 B files regenerated: 7,770–7,999 chars, all
  under the 8,000 hard cap (budget table recounted, filled basis).
- `session-ender.md` audited — paste body already stateless; stamp → v3.2.
- `per-project/README.md`: v3.2 changelog with the full relocation table +
  dead-action evidence; stagger-table transients re-verified against
  `telemetry/triggers-snapshot.json`.
- `docs/owner-queue.md` C#34: note — startup prompts are stateless; current
  work always comes from each repo's inbox/state docs.
- **Task 2 (relocate, don't delete): 12 ORDERs filed + MERGED across 10
  owning repos**, each verified at the owning repo's HEAD first:
  mineverse #43 `f8b6dbf` (ORDER 003: land CSRF PR #42 before secrets) ·
  idle #73 `45ff2bf` (003: pytest CI) · games #61 `9efe599` (005: heartbeat
  truth-stamp) · pml #53 `2efe16d` (006: .gitignore ROM guard) ·
  superbot-next #244 `dab14ad` (014: plugin-hello seed; 015: boot-doc
  render) · websites #157 `10214ea` (012: records reconcile; 013: owner-POST
  CSRF) · venture-lab #62 `f92a2ef` (007: ⚑ re-verification) · trading #67
  `6d7f6bc` (011: parked-PR landing + grading executor) · substrate-kit #259
  `745ee17` (015: dead boot-pointer template fix) · sim-lab #49 `27bdfb3`
  (003: merge-on-green landing path). Zero merge denials this session.
- Dead v3.1 actions (no ORDER; evidence in the README v3.2 changelog):
  superbot F2 (#196/#206 closed, #213/#217 merged), venture #58
  closed-unmerged, ideas handoff closed (verdict-012 at sim-lab HEAD),
  game-lab card convention shipped in both repos, v3.1's baked cutover
  trigger ids all absent from the telemetry snapshot.
- Known non-blockers observed: fm `freshness` red = repo-wide roster-age
  wall (not this diff); superbot-next `report` red-by-design (non-required;
  the required `gate` job passed before #244 merged).

## 💡 Session idea

Make D-9 (the stateless rule) *enforcing*, not just reviewed: add a
volatile-token linter to `regen_b_files.py` (or the fleet CI) that reds the
regen when A or any seat fill matches `trig_\w{10,}`, a `#\d+` PR ref, a
7–40-hex SHA, or an "expected as of <date>" clause. v3.1 baked all four
classes within one day of writing them despite three QA passes — review
discipline demonstrably doesn't hold this line under deadline; a 20-line
grep gate would.

## ⟲ Previous-session review

The staleness sweep (2026-07-12-staleness-sweep-8seat.md, PR #105) paid for
itself twice here: its committed 783-trigger telemetry snapshot and per-seat
verdicts were directly reusable citations for this session's Task-2
verification (games-heartbeat contradiction, dead trigger ids) — evidence
committed as data beats evidence narrated in prose. Miss: the sweep found
the superbot-games heartbeat contradiction but left it as a report row —
this session had to file the ORDER (games #61). Improvement: apply the
sweep's own DEAD-verdict rule ("a DEAD verdict becomes a routed ORDER,
never just a report") to STALE verdicts too — sweeps should end by filing
the correction ORDER in the owning repo's inbox, not just recording the
verdict.
