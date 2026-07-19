# 2026-07-19 · fm build slice — seat-provenance-aware I8 remedy + roster-cron closeout

> **Status:** `complete`

About to happen (declared born-red): build slice #3 from
`docs/planning/2026-07-19-next-slices.md` — rewrite the I8 DUPLICATE-CRON remedy line
in `scripts/check_trigger_health.py` from the generic "keep the OLDEST-created" rule
(which contradicted the correct call on the live SBW pair this very night — the
NEWER trigger belonged to the current seat session; the OLDER was the crash-orphan)
to provenance-aware guidance: verify EACH id's bound session against the owning
seat's live heartbeat; the id bound to the seat's CURRENT session stays, others are
crash-orphans the owning seat (or hub) deletes; keep-oldest is NOT the rule.
Selfcheck assertions updated to pin the new wording. PLUS the roster-cron owner-queue
closeout now fm #344 has merged (odd-hour second cron `40 1-23/2 * * *` verified live
on origin/main): move `OQ-FM-ROSTER-CRON-RELIABILITY` to Resolved with the delivery-
proof condition noted, and refresh the `control/status.md` baton. Claim
`control/claims/claude-fm-i8-provenance.md` (deleted in the flip commit). No
trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — remedy-text edit to a verified checker + records closeout (Q-0105 provenance tier)

## What shipped (PR #353)

- `scripts/check_trigger_health.py` — I8 remedy rewritten seat-provenance-aware
  (provenance comment block on the I8 branch + a header `Amended` entry, both
  citing the 2026-07-19 SBW case): verify EACH live (I1b caveat, unchanged),
  then verify EACH id's bound session against the owning seat's live heartbeat —
  the id bound to the seat's CURRENT session stays, others are crash-orphans the
  owning seat (or hub) deletes; **keep-oldest is NOT the rule** (the SBW keeper
  was the NEWEST). Creation order stays printed as a hint only (newest-created
  usually = the live one) — the heartbeat check decides. The `WHAT IT CHECKS`
  I8 header paragraph updated to match. Selfcheck: the old
  "keeps the oldest-created id" assertion replaced with four pins — no
  keep-oldest text, heartbeat-binding wording present, "keep-oldest is NOT the
  rule" present, newest-created hint names the newest id; `--selfcheck` PASS
  (0 failures). Ground-truth run against the committed 06:15Z snapshot: the I8
  WARN now hints `trig_01DbcKVWxn6RJPhfyRkgTg6m` (newest) as the likely keeper —
  matching the hand-inverted `OQ-SBW-DUP-FAILSAFE` escalation instead of
  contradicting it. Exit contract unchanged (WARN, exit 0).
- `docs/owner-queue.md` — `OQ-FM-ROSTER-CRON-RELIABILITY` → **Resolved**:
  fm #344 merged 2026-07-19T09:22:03Z (merge commit `b6f01d2`, owner resolved
  the conflict); both cron lines (`40 */2` + `40 1-23/2`) verified live in
  `.github/workflows/roster-regen.yml` at origin/main. Status: **fix live,
  delivery proof pending the next odd-hour window** (first post-merge odd
  window 09:40Z; proof = a roster gen stamped within ~1h of an odd :40 window —
  latest regen at read time was gen #100, 07:08Z, even-hour line). Companion
  slug `OQ-FM-ROSTER-CRON-SECOND-LINE` closed in the same entry (its in-diff
  row never landed — the conflict resolution kept main's queue text). Section
  (A) note updated (#344 no longer conflict-dirty).
- `control/status.md` — `updated:` → 09:29Z; ~09:2xZ section (#344 merged fact +
  slice-3 record); baton refreshed: owner-await list drops #344; **planned
  queue drained** (slices 1–3 done: #350/#352/#353) → next = below-the-line
  (fence emitter · capabilities-grammar linter) or a fresh groom; watches =
  odd-hour delivery proof (09:40Z) + websites 036 ack/revival + I6 snapshot
  refresh ~10:15Z.
- `docs/planning/2026-07-19-next-slices.md` — standing queue annotated DONE
  ×3 + drained marker (doc-audit catch: the plan would otherwise claim an
  open queue the baton says is drained).

## Gates

- `python3 scripts/check_trigger_health.py --selfcheck` → PASS (0 failures).
- `python3 scripts/check_trigger_health.py` → PASS (8/9 green, 1 WARN I8 —
  new wording, exit 0).
- `python3 bootstrap.py check --strict` → born-red HOLD pre-flip (by design);
  EXIT 0 expected at this flip.
- Guard-fires telemetry delta committed with the payload (5 records appended,
  allowlist-suppressed reason-carrying findings — no new real fires).

## Enders

- **💡 Session idea (dedup-checked — `routine-claims` grep hits only the plan's
  write-side fence-emitter item; this is the read side, and new):** teach I8 to
  **consult the owning lane's heartbeat `routine-claims` fence directly**. Lane
  heartbeats now carry a machine-readable fence claiming the seat's current
  failsafe id; when I8 finds a duplicate group, it could fetch the owning
  repo's `control/status*.md` fence (same shallow-git path `gen_roster.py`
  already uses) and — when exactly one duplicate id matches the fence's claimed
  failsafe — print "keeper per the seat's own fence: `<id>`" instead of only
  telling the human to run the heartbeat check. Turns the new remedy's manual
  verification step into a computed verdict with the same honesty fallback
  ("fence absent/ambiguous → human decides"). Worth having: the SBW case would
  have been auto-answered the moment that lane adopts the fence.
- **⟲ Previous-session review (PR #352, regen-window skip detector):** strong
  slice — exit-contract regression-checked against main at a pinned `--now`,
  and the synthetic incident-night replay (23:31Z stamp read at 03:30Z → the
  00:40Z drop self-announces) is exactly the right ground-truth style for an
  unverified-tier checker. Missed/improvable: the window report only speaks
  when something *runs the checker* — at fm wakes and in `claude/*` PR gates —
  so a dropped window on a quiet night still waits for the next wake; the
  system improvement is to surface the same window report inside the
  `roster-regen.yml` freshness self-check step (it already runs
  `check_roster_freshness.py` on every fire), so the *adjacent* successful
  window's Actions log names the miss minutes after it happens. Cheap: it is
  the same script, already invoked there — verify the flag defaults do what we
  want in that venue.
- **Doc-audit:** ledger homes checked — Resolved entry carries both slugs +
  merge sha; plan doc annotated (above) so plan/baton agree; no chat-only
  facts left. `bootstrap.py check --strict` green at flip is the automated
  half.
- **Guard-fires:** 5 allowlist-suppressed records appended to
  `.substrate/guard-fires.jsonl` (committed with the payload); no new
  unsuppressed guard fires this session.
- **Claim deleted in this flip commit** (`bootstrap claim fm-i8-provenance
  --delete`).
