# 2026-07-11 — UNIVERSAL v4: corrected §2.4 merge clause (rebuilt payload for merged #47)

> **Status:** `complete`

📊 Model: fable-5 · lane worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL · start 2026-07-11 (born-red at open)

## Declared at open (born-red)

Rebuild the lost PR #47 payload: apply the owner-provenance corrected §2.4
merge clause (owner-queue item 16 as staged by ORDER 016 / PR #68, now item 13
after the #75 renumber; verbatim source: findings audit §2.4) to BOTH
merge-clause locations in `projects/UNIVERSAL.md`, bump v3→v4, annotate the
queue item, heartbeat, and leave the PR GREEN for the owner to merge
personally — no auto-merge, no self-merge (instruction-authority content).

## What landed (PR #76)

- **`projects/UNIVERSAL.md` v3→v4** — the corrected §2.4 merge clause applied
  VERBATIM at BOTH merge-clause locations (fenced canonical block, was :42-44;
  wake-prompt condensed form, was :74-77). Byte-identity verified twice by
  `cmp`: the two staged sources against each other (findings audit §2.4 block
  == old item-16 block from PR #68 @ `c5e264f`, dedented — identical, 1365
  bytes / 19 lines), and BOTH inserted occurrences against that block after
  edit (identical). v4 provenance block added under the Status line; header
  comment + Status stamp bumped v3→v4. ⚑ Decide-and-flag: the wake block's
  in-paste stamp (`WAKE (universal, v3 …)`) also bumped to v4 — it is the
  drift-check anchor seats quote back; leaving it v3 would defeat the drift
  check forever. Inner "PERMISSIONS & AUTHORITY (v1 …)" stamps deliberately
  NOT bumped ("change nothing else"); flagged for the ORDER 017 re-issue to
  decide.
- **Housekeeping:** legacy card `2026-07-10-universal-permissions-block.md`
  closure note (superseded by #76, grandfathered — merged stuck in-progress
  via #47); owner-queue item 13 (old 16) annotated RESOLVED-PENDING-MERGE of
  #76; `control/status.md` heartbeat + slice record.
- **Deliberately NOT done:** no auto-merge, no agent merge — the owner merges
  #76 personally (instruction-authority content; the guard precedent on #48).

## 💡 Session idea

A **payload-presence gate for re-land vehicles**: the #47 failure class is a
PR whose card declares intent X but whose diff never grows beyond the card —
and it still gets merged as if it carried X. Cheap enforcing guard: the
substrate gate (or a tiny CI step) reds a card-flip-to-complete when the PR's
non-card diff is EMPTY but the card's "Declared at open" names target files —
"declares payload, carries none." That one check would have turned the merged
empty #47 into a red instead of a silent no-op landing.

## ⟲ Previous-session review

The PR #75 verified-refresh slice was exemplary on evidence discipline (every
item re-checked live, per-item citations) and its negative-findings headline
is exactly what surfaced this rebuild lane. Two misses worth naming: (1) it
renumbered the HOT item 16→13 while sibling docs (the succession handoff, the
ORDER 017 gate text, and dispatch prompts) still say "item 16" — a renumber
of a load-bearing item should carry a grep-and-annotate pass for inbound
references, or keep stable item IDs instead of positional numbers; (2) its
15:10:00Z `updated:` stamp was ~4 min ahead of real UTC at write time (this
session read 15:06:06Z from `date -u` after the #75 merge) — the same
future-stamp class the fleet already ordered product-forge to fix (forge
ORDER 003); stamps should come from `date -u`, never rounded up.
