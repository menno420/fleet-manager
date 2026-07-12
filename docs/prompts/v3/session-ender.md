<!-- v3.0-draft · 2026-07-12 · provenance: research PRs #93/#95 + owner baseline 2026-07-11 · owner spec delta 2026-07-11T23:47Z (the ender NEVER re-arms) -->
<!-- char-count: 1,896 chars = the paste body below this comment block (headers excluded) · budget ~2,000 (spec §6) -->
<!-- Artifact D — universal session ender. ONE version for every seat; no slots. Net-new artifact (spec §3a). -->

v3.0 · 2026-07-12 · universal session ender

SHUT DOWN NOW, in order. This ends your session's chain — start no new work.

1. PARK — every session PR reaches READY+green or closed-with-reason; nothing left draft or red. If anything merged this session, diff the merge commit and confirm the payload actually landed (an empty-vehicle merge is a known failure class).
2. ROUTINE DISPOSITION — you NEVER re-arm here, and you never hand a routine to the owner. Close your session's OWN routines: the pending send_later pacemaker and every session-bound trigger this session created — delete_trigger each, then VERIFY absent via list_triggers paginated to exhaustion (limit 100, next_cursor until has_more is false). The failsafe cron follows the same rule: close it if this seat can. If arming/disarming is walled from this toolset, relay the SAME delete through a spawned worker (ONE trigger-MCP call per worker), then verify. Anything genuinely uncloseable: document it in the heartbeat — trigger id + why it could not be closed — for the successor to close.
3. RELEASE — delete your claim files; flip the born-red session card to complete as the deliberate last commit.
4. HEARTBEAT (deliberate last write) — overwrite control/status.md: routine disposition (ids closed / ids left-for-successor + why), parked-PR list, ⚑ owner asks paste-ready, next-2-tasks baton. NEUTRAL facts + pointers ONLY — no steering lines, no verbatim denial quotes (walls are quoted in the PR body / owner-queue instead); durable links live in docs/current-state.md, never sole-homed in status.
5. REPORT — shipped / parked / walls / flags, every claim citing a commit/PR/CI run. Then END: arm nothing, wake nothing — the chain terminates with you.

Confirm before ending: recite the trigger ids you closed, the ids you documented for the successor (+ why), and that no new routine was armed.
