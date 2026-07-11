# 2026-07-11 — ORDER 016: audit actions (§2.4 owner-queue item, env R1+R5, follow-up tracking)

> **Status:** `in-progress`

📊 Model: Claude (Fable family) · start 2026-07-11T06:48Z (`date -u`) · lane
worker dispatched by coordinator, executing the manager-owned NOW scope of
ORDER 016 (control/inbox.md).

## Declared at open (born-red)

ORDER 016 now-scope: §2.4 owner-queue item, env R1+R5, follow-up tracking,
per-lane enabler verification. About to land, in order:

1. R1 (doc-only): register the 5 unregistered python-lab lanes (sim-lab,
   product-forge, idea-engine, **superbot-idle** [live seat, no archetype
   named — highest priority], mobile-lab) in `environments/archetypes.md`
   + the `Serves:` header of `environments/archetype-python-lab.sh`.
2. R5: point the three codetool-lab-* environments' setup-script field at
   `archetype-python-lab.sh` (has the pyproject `[dev]` branch) instead of
   `setup-universal.sh` lineage (silently skips pyproject).
3. Owner-queue item (fleet-critical): six-field R17 item for the audit §2.4
   corrected UNIVERSAL.md merge-authority clause (owner-provenance — the
   owner lands it, not the manager), verbatim paste block included,
   cross-referenced to item 13's PR-#47 permissions-v2 rider.
4. Tracking doc `docs/planning/order-016-followups-2026-07-11.md`: draft
   ORDER text for (a) the walled-instruction re-issue (gated on the owner
   landing §2.4) and (b) the R2/R3/R4/R6 env-consolidation lane — drafts
   for the coordinator to file into control/inbox.md (one-writer rule).
5. Flip this card `complete` as the deliberate LAST step. NOT in scope:
   control/ writes, merging/arming auto-merge, editing projects/UNIVERSAL.md.
