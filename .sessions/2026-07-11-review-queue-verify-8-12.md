# 2026-07-11 — Review-queue manager-verify: pokemon-mod-lab#8 + gba-homebrew#12

> **Status:** `complete`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~02:2xZ · lane
worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: manager-verify of the two remaining fallback-tier review-queue rows —
**pokemon-mod-lab#8** (sha1-chain / byte-identity claims of the #4–#8
engine-patch train, checkable from committed `docs/proof/session-006/`
fixtures; feel half stays owner-playtest) and **gba-homebrew#12** (whether the
dispatch-tier HUD asserts of #13 reached per-PR CI, or gameplay regressions
still merge on a green compile). Ground truth via GitHub MCP against the lane
repos (both LIVE-PARKED — read-only, zero lane-repo writes; all edits land in
fleet-manager `docs/review-queue.md`). Heartbeat `control/status.md` as the
deliberate last content step; flip this card `complete` as the final commit;
REST squash-merge on green (R21).

## Shipped (close-out)

- **pokemon-mod-lab#8 — sha1-chain half VERIFIED** (row annotated, stays open only
  on the owner-playtest feel half): five proof bundles chain link-by-link
  `eec6d6af` → `94ee8845` → `3c68b982` → `17e20a0a` → `a2023c19` → `dfa279f2` →
  `715a8ad2` → `15ef187d` → `805aeaee`; two independent CI-log anchors (job
  86304782740 printed `805aeaee…` on the PR #8 merge head; job 86297858710 printed
  `715a8ad2…` on PR #7's). Cosmetic commit-label drift noted (`609dae9` vs `2b06a89`).
- **gba-homebrew#12 — CLOSED: VERIFIED-ANSWERED-BY-DESIGN**: the #13 HUD asserts
  are deliberately dispatch-tier-only (workflow's own comment, HEAD `39b33d7`);
  dispatch tier exercised 4× 2026-07-10 (run 1 failed, latest green on `f502147`);
  per-PR no longer compile-only since gba#31 (`tools/check-cave.py` per-PR).
- Heartbeat slice record in `control/status.md`; lane repos untouched.

💡 **Session idea:** the pokemon lane's `rom-builds.yml` already *prints* the ROM
sha1 on every push but asserts nothing — one committed `docs/rom-sha1-chain.txt`
(expected sha1 of the shipped ROM at HEAD) plus a one-line `sha1sum -c` in the
workflow would convert the whole byte-identity chain from lane-attested to
CI-gated for ~zero cost (the build already runs). Route to the pokemon lane /
retro coordinator when un-parked work resumes; this verify would then be a
standing red/green signal instead of a manager archaeology pass.

⟲ **Previous-session review:** the roster-gen-4 slice (PR #59) set the transport
doctrine this slice leaned on — ls-remote-pinned HEADs and verbatim wall
recording — and its slice record made attribution/citation style easy to match.
One improvement it surfaced for the workflow: its `updated:` header had already
been the *third* consecutive slice to hand-compose the long `phase:` chain; the
prepend-and-demote pattern works but the phase line is now ~4k chars of nested
"Prior phase:" — a `control/status-archive.md` rotation rule (phase chain deeper
than N=3 rotates to archive) would keep the heartbeat readable. Genuine, small,
and checkable; nothing else to fault.
