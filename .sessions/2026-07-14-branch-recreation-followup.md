# 2026-07-14 — Branch-recreation census follow-up (findings doc + email ask-4 clause + checklist truing)

> **Status:** `complete`

📊 Model: Fable 5 (family-level)

about to do: land the fleet branch-recreation census + EAP email ask-4 clause per coordinator dispatch 2026-07-14 — a new `docs/findings/branch-recreation-census-2026-07-14.md` (four-repo census: 460/491 surviving claude/* branches at exactly their merged PR head SHA, two-tier mechanism, spot-check verdicts), a surgical mechanism clause in the email draft's ask 4 (+ appendix row evidence), and a truing amendment to owner-checklist row 11 (hub sweep safe-permanent; auto-delete unreliable for bot-merged PRs).

Provenance: coordinator dispatch 2026-07-14; census coordinator-run ~13:4x–14:0xZ, fm-seat spot-checks per Q-0120 at 13:49–13:52Z; mechanism per curious-research PROPOSAL 003 + same-day ADDENDUM.

Work record: all three record edits landed on PR #200 @ cf08c3e (findings doc + README index; email ask-4 clause + appendix row; checklist row 11 truing); heartbeat overwrite + this flip close it. Verification: bootstrap check --strict green apart from this card's designed hold; roster OK (2.0h); owner-queue CLEAN; trigger-health PASS 9/9. CI at cf08c3e: freshness + merge-on-green green; substrate-gate red on the [session-card-hold] finding only (job-log verified).

💡 Session idea: the born-red close-out flip is a fixed 2-commit choreography (heartbeat wholesale overwrite → badge flip + claim delete) that every dispatch worker re-derives from prose — a `scripts/close_out.py --card <path> --claim <path>` helper (or kit skill) that stages exactly those two commits would remove the "nothing else in the commit" foot-gun and make the dispatcher's instructions one line.

⟲ Previous-session review: the checklist-refresh-2 session (PR #199) merged three walkthroughs' §C rows cleanly and left an accurate straggler line that this session leaned on directly — strong. Its miss: row 11's Verify cell ("next merged PR's head branch auto-deletes") was already contradicted by evidence available at its sweep time; a truth-check of Verify cells against known walls when merging §C rows would have caught it a session earlier. Concrete improvement: when folding walkthrough rows into the checklist, spot-check each Verify signal against the findings ledger before recording it as the verification path.
