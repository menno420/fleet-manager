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

## Close-out (what actually landed — card left `in-progress` deliberately)

All four declared items landed, one commit each (PR #68); the card flip is
the COORDINATOR's call, not this worker's (dispatch rail: "do not flip"):

1. R1 — `environments/archetypes.md` (Serves cell + 5 new mapping rows,
   superbot-idle flagged as the live-seat drift) +
   `environments/archetype-python-lab.sh` Serves: header.
2. R5 — `projects/codetool-lab-{fable5,opus4.8,sonnet5}/meta.md` setup-script
   fields repointed at `environments/archetype-python-lab.sh` (doc registry
   only; live-console paste rider = one line in the follow-ups doc, per the
   audit's low-urgency call).
3. Owner-queue item 16 (🔥 HOT) — §2.4 corrected merge clause, six-field R17
   form, verbatim paste block, cross-referenced to item 13's PR #47 rider.
4. `docs/planning/order-016-followups-2026-07-11.md` — draft ORDERs 017
   (walled-instruction re-issue, GATED on item 16) + 018 (R2/R3/R4/R6 env
   consolidation), for the coordinator to file (one-writer rule).

Gate: `python3 bootstrap.py check --strict` — one real finding (badge token
`draft` → fixed to `plan`); the remaining card-completeness finding is this
deliberate born-red hold; the control/status.md advisory is pre-existing and
control/ is out of scope.

💡 Session idea: `bootstrap.py check` could cross-check
`environments/archetypes.md`'s mapping table against `projects/*/` dirs — a
lane with a package dir but no archetype row (the superbot-idle drift class
this session closed by hand) would become a mechanical finding instead of an
audit discovery.

⟲ Previous-session review: the ORDER 015 registry-centralization session
(#58) landed all seven declared items one-commit-each with verifiable
citations — a clean pattern this card copies. One improvement it surfaces:
its meta.md setup-script lines recorded repo-local script *lineage* without
naming which script the live console field should carry; this session had to
infer that distinction for R5. Package metas should always name the
console-field value explicitly (now done for the three codetool metas).
