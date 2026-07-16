# 2026-07-15 — v3.7 duty-form prompt registry + owner execution mandate (ORDER 048)

> **Status:** `complete`

About to (opening declaration, kept): land the owner's standing execution mandate as
**ORDER 048**; rewrite the v3 prompt registry to **duty-form** (9 CIs + 9 startups +
ender + UNIVERSAL grant v2) with the mandate folded in, affirmative practices,
platform-prohibition restatements dropped, and the owner authorization pre-written;
bump v3.6 → v3.7 + registry stamps; land this PR on green via merge-on-green.

## What happened

- **ORDER 048** appended to `control/inbox.md` (owner verbatim mandate from his live
  turn + six duty-form clauses + paste-ready lane fan-out block + manager follow-ups:
  verify, refresh records/meta, fan out adoption ORDERs, drive the merge-on-green
  installs in the workflow-less repos). Expands ORDER 047; supersedes the v3.6
  park-green/owner-click defaults and agent-authored restrictions lacking owner
  provenance.
- **v3.7 registry**: all 9 seats' Custom Instructions + expanded startups rewritten
  duty-form; `session-ender.md` step 1 PARK → LAND; `projects/UNIVERSAL.md` → v5 with
  the owner-landed **grant v2** (LAND EVERY PR · KEEP EVERY PR MOVING TO TERMINAL ·
  wake mechanics · workers · decide-and-flag · DENIAL ROUTING · RULE PROVENANCE).
  Owner authorization **pre-written** in every paste (pasting = signing, zero blanks —
  the owner's "100% paste ready" instruction). Dictionary swap: park green → **land
  on green**, deny-wins → **denial routing**; `CORE` alias retired. Stale merge facts
  corrected at 2026-07-15 verify: fm merge-on-green.yml LIVE (PR #146), superbot +
  superbot-next enablers BOTH live; workflow-less repos (games, gba, pml) now carry
  the standing merge-on-green INSTALL duty (first slice) instead of "owner-click
  only". Safety fences kept full force in duty form (trading research-only, track
  isolation + R22, teaching/safety/privacy rails, Q-0213 brake, Q-0261.3 scope,
  security-before-secrets).
- **Tooling + docs**: `regen_b_files.py` v3.7 (grant/ender/triad anchors, seat stamps
  +1, failsafe template duty-formed); v3/README.md (found-a-seat flow: zero blanks) +
  per-project/README.md (v3.7 changelog + size table) + planned-routes (CORE row
  RESOLVED, merge-on-green row remainder updated) + custom-instructions-core.md
  marked historical.
- **Checks** (all local, this tree): `regen_b_files.py` exit 0 — CI budgets
  7,946–7,966 chars / 7,979–7,998 bytes (all ≤ 8,000 on both bases), drift checks
  9/9 (ender D-10, grant v2 sync, doctrine/card/triad/baton identity, stamps,
  failsafe extraction); `--check-registry` 27/27; `bootstrap.py check --strict`
  exit 0 (the only red = this card's designed born-red HOLD). Duty-form audit grep:
  remaining "never"s are owner quotes ("I don't review PRs and never will"), the
  mandate's "never finished", rule names (R29, ⚠ NEVER-WAIT Q-0241), and the "Never
  idle" ladder title — zero agent-directed prohibitions.
- **Websites impact verified** (via repo read of menno420/websites): the
  control-plane `/prompts`, `/prompts/history/{seat}`, `/projects/{package}` pages
  fetch this repo's `main` LIVE (raw.githubusercontent, 180s TTL, `?refresh=1`
  bypass) — the v3.7 stamp-line format and `registry-header-end` markers are
  preserved and the seat set is unchanged, so the live site serves v3.7 on merge
  with zero websites-repo changes. `review/data/fleet.json` carries no prompt data
  (its "v3.6" strings are heartbeat free-text — refreshed by seats' own heartbeats).
- **Left for the manager (named in ORDER 048)**: roster/current-state/meta.md
  deployed-state refreshes as seats re-paste; lane adoption ORDER fan-out; the
  merge-on-green installs in superbot-games, gba-homebrew, pokemon-mod-lab driven to
  merged. Advisory noted, untouched: projects/fleet-manager/seat-digest.md drift
  (fm coordinator's lane; `seat_digest_sync.py --sync`).

⚑ Self-initiated: none beyond the directed scope — every deliverable traces to the
owner's live turn (mandate, duty-form rewrite, pre-written authorization, website
verification) or the PM-relayed founding checklist it endorsed.

💡 **Session idea:** a **duty-form linter** for the registry — an advisory check in
`regen_b_files.py` that flags prohibition-form patterns (`do not|don't|never
<verb>`) in paste bodies, with an allowlist for owner quotes, rule NAMES (R29,
NEVER-WAIT), and the "Never idle" title. The owner's no-negatives bar (ORDER 048)
was enforced this pass by hand-grep; a checker keeps future edits from regressing
the tone the way budget edits regress counts. Dedup: grepped docs/prompts/v3/ +
docs/ideas-adjacent files — the regen tool checks budgets/drift only; no tone check
exists anywhere in the fleet.

⟲ **Previous-session review** (2026-07-15 owner-no-review-order, PR #246): strong
session — it landed ORDER 047 verbatim with clean provenance, added playbook R29,
and honestly named the #227 workflow-file rail as a technical carve-out rather than
a review hold. Two gaps: its `📊 Model: Fable` line misses the three-field payload
(the telemetry harvest records nothing from that card — the checker still flags it
at every run), and ORDER 047's fan-out block stayed inbox-side with delivery
deferred to "owner/hub paste or next manager wake," which left the policy unfanned
at HEAD a day later. **Workflow improvement (applied in this session's ORDER 048):**
a fan-out ORDER should carry its own delivery plan as named manager follow-ups
inside the ORDER, so the next wake executes distribution instead of rediscovering
it.

- **📊 Model:** Claude Fable (Claude 5 family) · high · docs-only (prompt-registry rewrite)
