# 2026-07-13 — consolidation batch (inbox flips + R24 gate + owner-queue + heartbeat)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-13 ·
coordinator-dispatched worker (consolidation batch)

## Declared at open (born-red)

Consolidation batch as the coordinator's hands: (1) inbox appends — DONE flips
for websites ORDERs 019/021/022 (manager sweep evidence 2026-07-12T22:1x–22:2xZ),
new ORDER 037 (superbot-games mining-status stamp repair), new standing ORDER 038
(sim-lab VERDICT 016 codex-authenticity gate, fleet-wide); (2) playbook R24
amendment — codex replies untrusted until they pass the VERDICT 016 authenticity
checks; (3) owner-queue B-group adds — OQ-FM-ROSTER-READ-PAT +
OQ-IDLE-REQUIRED-CHECKS; (4) control/status.md wholesale heartbeat overwrite;
(5) one arm attempt each on superbot-games PRs #65/#66 (enable_pr_auto_merge,
ORDER 029 standing permission). No trigger-MCP calls this session.

## Close-out

**Shipped (PR #148):**

- `control/inbox.md`: append-only DONE flips for ORDERs 019 / 021 / 022
  (websites seat; manager sweep evidence 2026-07-12T22:1x–22:2xZ — 019: review
  site serving 07-12 data/incident/8-seat content, bake a513ff4; 021:
  /directory live, websites PR #198 c51d6e7; 022: arcade card LIVE #197
  41d3526 + env page verified #210 + OWNER-ACTIONS reconciled #214; websites
  heartbeat aafad91 "019/021/022 all DONE"). New ORDER 037 (superbot-games
  `control/status-mining.md` malformed `updated:` stamp → one-line ISO8601
  repair; done-when: roster regen parses the mining sub-row). New standing
  ORDER 038 (all seats: sim-lab VERDICT 016 authenticity gate — sim-lab PR
  #58, squash 0d64f36 — mandatory pre-trust check on every @codex /
  cross-agent reviewer reply; 3/3 fabrications caught, 0/24 false alarms;
  replaces suspension; Q-0120 still governs; manager decide-and-flag,
  owner-vetoable).
- `docs/playbook.md`: R24 amendment carrying the same VERDICT 016 gate as
  doctrine (line-range≤EOF etc.; cites sim-lab PR #58).
- `docs/owner-queue.md`: B#49 OQ-FM-ROSTER-READ-PAT (fine-grained read-only
  PAT for pokemon-mod-lab → fm Actions secret `ROSTER_READ_TOKEN`; wiring
  already merged, fm PR #144) and B#50 OQ-IDLE-REQUIRED-CHECKS (superbot-idle
  Allow auto-merge + pytest/substrate-gate required checks; unblocks parked
  idle #75/#76; enabler 457407c INERT until clicked) and B#51
  OQ-GBA-ROM-RULESET (coordinator mid-session addition: gba-homebrew ruleset
  requiring `ROM builds` on main — the merged enabler, PR #76 0e08695, sees
  zero token-readable required contexts and correctly refuses to arm).
- `control/status.md`: wholesale heartbeat overwrite (updated
  2026-07-13T00:10Z) — coordinator/routine facts, landed-today ledger
  (#142/#143/#144/#146/#147 + this PR), fleet enabler state, orders state,
  next-3, ⚑ needs-owner pointers.

**Side action (github MCP, ORDER 029 standing permission):**
enable_pr_auto_merge (SQUASH) on superbot-games #65 and #66 — BOTH ARMED,
one attempt each, no denial: "#65 … enabled at 2026-07-13T00:10:01Z",
"#66 … enabled at 2026-07-13T00:10:02Z". (fm #148's own early arm attempt was
refused — "The pull request is in unstable status (required checks are
failing)" — the born-red gate was already reporting; not retried per playbook;
landing rides the flip + self-merge/sweep.)

**R24/VERDICT 016 gate applied live:** a chatgpt-codex-connector comment on
PR #148 claimed it "committed changes on the current branch with commit
d82f928". Verified against ground truth before flipping: the branch's
main..HEAD range contains EXACTLY this session's three commits (58888fd /
932ad54 / 0978286, all Claude-authored) and `git cat-file -t d82f928` returns
"fatal: Not a valid object name" — the claimed commit does not exist in this
repo. The comment fails the authenticity gate; discarded, not acted on
(reported to the coordinator).

**Verify suite (pre-flip):** `bootstrap.py check --strict` red ONLY on the
designed born-red hold (card in-progress; "HOLD (by design)");
`check_roster_freshness.py` exit 0 (roster 0.7h old);
`check_owner_queue.py` exit 0 (CLEAN — slugs intact);
`check_trigger_health.py` exit 0 (PASS 7/7 at snapshot instant
2026-07-12T20:41Z).

## 💡 Session idea

Extend `scripts/check_owner_queue.py` to enforce **globally-unique item
numbers** alongside the slug check: the queue numbers items globally across
letter groups (B#43 … E#48, then F holds 39), and a new add must hand-pick
the next free integer by scanning the whole file — this session added B#49/50
after exactly that manual scan. Two items ever sharing a number would make
cross-references like "B#49" ambiguous in owner replies, and nothing catches
it today; the checker already parses every item for slugs, so a
duplicate-number FAIL is a few lines in an existing pass. (Deduped: prior
owner-queue ideas cover retire conditions, supersession probes, char counts,
and state grammar — none cover number uniqueness.)

## ⟲ Previous-session review

The owner-goals dispatch (PR #147, ORDERs 030–036) did the important thing
right: it carried the owner's words **verbatim** into each seat's ORDER with
per-seat done-whens, so no lane has to reinterpret intent — and it correctly
split build-vs-spec ownership between superbot-next (030) and SuperBot World
(031). One genuine gap it surfaces: the PR shipped **inbox-only, with no
session card** — the born-red gate only engages when a PR *adds* a card, so
coordinator-direct dispatch PRs leave no `.sessions/` trail and their record
lives solely in the ORDER blocks + PR body. Concrete workflow improvement:
coordinator-dispatched inbox-only PRs should carry at least a minimal card
(three lines: what was dispatched, why, evidence pointer), or the playbook
should explicitly designate the ORDER blocks as the durable record for that
PR class so the omission is doctrine instead of drift.
