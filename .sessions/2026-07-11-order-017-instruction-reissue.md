# 2026-07-11 — ORDER 017: re-issue lane instructions from corrected UNIVERSAL §2.4 (v4)

> **Status:** `complete`

📊 Model: fable-5 · lane worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL · start 2026-07-11T15:42Z · close 2026-07-11T17:05Z

## Declared at open (born-red)

Execute ORDER 017 (gate CLEARED: PR #76 owner-merged, UNIVERSAL v4 @
`e1848ff`): re-issue all 15 `projects/<repo>/instructions.md` from the
corrected §2.4 merge clause — insert the canonical Permissions & authority
block verbatim (§3.1 resolution = INSERT), kill both §3.2 same-file
contradictions, fold in per-lane enabler status
(enabler-install-verification-2026-07-11) + the seven incident riders,
version-bump every file, update companion coordinator-prompt.md one-liners,
refresh owner-queue items 13/15, projects/README.md paste-wave registry,
superbot-retro meta note, and stage the §3.3 hoist as an owner paste bundle.
No edits to projects/UNIVERSAL.md. PR parked READY for the owner — no arm,
no merge (instruction-authority content).

## What landed (PR #77 — PARKED READY for the owner's click)

- **All 15 instructions.md re-issued** (v1→v2; superbot-games v2→v3): the
  canonical Permissions & authority block inserted BYTE-VERBATIM from
  `projects/UNIVERSAL.md:44-81` @ `e1848ff` (cmp-verified per file); every
  walled arm/REST-merge landing passage replaced with park-READY+green;
  each repo's required-check names + born-red gate kept; all files < 7,500
  bytes (websites trimmed 8,382→7,470 — heaviest).
- **§3.2 contradictions removed** (fleet-manager :76 vs :85;
  trading-strategy :92 vs :93-96). **§3.1 resolved by INSERTION** — the
  "verbatim in every file" claim and the files now agree.
- **Enabler truth per lane** folded from the 2026-07-11 verification; the
  two unprobed lanes closed by raw fetch this session: superbot-idle NO
  enabler (auto-merge-enabler.yml 404), superbot-mineverse HAS it (200).
- **Incident riders**: base set ×15; Q-0120 into the 8 missing files;
  silent-fire into websites/gba-homebrew/pokemon-mod-lab.
- **Companions**: 11 coordinator-prompt.md merge one-liners updated;
  playbook R21 SUPERSEDED-annotated; mineverse :101-104 supersession
  executed; retro meta note + flagged trigger re-arm follow-up (stored
  prompts untouched); owner-queue items 13 (RESOLVED) + 15 (rewritten,
  hold = PR #77 only); projects/README paste registry → v2/v3-bodies-only;
  §3.3 hoist staged as docs/proposals/universal-v5-hoist-bundle-2026-07-11.md
  (NO UNIVERSAL.md edit); inbox ORDER 017 ✅ DONE appended.
- **Deliberately NOT done**: no auto-merge arm, no agent merge on PR #77
  (instruction-authority content — owner clicks); no UNIVERSAL.md edit.

## 💡 Session idea

A **byte-verbatim block checker** for the fleet registry: the §3.1 drift
class ("UNIVERSAL claims the block is verbatim in every file" while 0/15
carried it) is mechanically checkable — a tiny CI step that extracts the
fenced Permissions block from UNIVERSAL.md and `cmp`s it against each
`projects/*/instructions.md` would turn silent doctrine drift into a red
check the moment either side changes. Same pattern extends to a 7,500-byte
paste-size ceiling and the paste-wave `vN` header stamps.

## ⟲ Previous-session review

The PR #76 rebuild slice was exemplary on provenance discipline (double
cmp-verification, both locations, nothing-else-changed) and its
"owner merges personally" park is exactly what let this session execute
cleanly from an owner-provenance source. One miss worth naming: it left the
inner "PERMISSIONS & AUTHORITY (v1 …)" stamps for ORDER 017 to decide but
recorded no recommendation — this session KEPT them at v1 (the block's own
version is the owner-landed grant's version, not the carrier file's); that
rule deserves a line in the v5 hoist bundle era. Workflow improvement: the
per-file 7,500-byte trim work dominated this session's cost — the CI check
in the idea above would let future re-issues fail fast instead of
hand-iterating `wc -c`.
