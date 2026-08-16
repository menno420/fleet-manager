# 2026-08-16 · hub — the owner's three answers executed: orphan DB dumped+deleted, acceptance recorded, PAT-mint probed

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · feature build — owner, live: **A** on
  `OQ-RG-POSTGRES-BOTSITE` (dump to a durable PRIVATE home, verify restore,
  delete the service — the explicit hard-rail amendment for this one service),
  **Accept** on `OQ-SB-BACKUP-ARTIFACT-VISIBILITY` (recorded, no change), and
  on `OQ-WEBSITES-PAT`: *"You can probably get one yourself right? If you use
  my account pat to mint one? Please try that"* — probe the API surface for
  PAT minting and report the measured result. `worker` and the bot's
  `Postgres` remain under the operation-scoped hard rail throughout.

Time: 2026-08-16 · venue: owner-live hub chat · branch
`claude/railway-websites-audit-gp7nc7` restarted from `main` (fm #865 merged)

## Previous-session review

⟲ fm #865 (merged `25c4733`): the records correction this card's asks answer.
Checked at `main`: both queue entries present, option A correctly names a
private durable home. Nothing to repair.

## 💡 Session idea

Execute the three answers with the same verify-every-step discipline as
fm #863; the delete of `postgres-botsite` happens only after the dump's
integrity is verified and the archive is durably stored.

## Close-out

*(flips with the badge)*
