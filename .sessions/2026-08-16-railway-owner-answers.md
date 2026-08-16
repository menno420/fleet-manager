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

**Shipped (every step verified as it landed):**
- **A executed** — `postgres-botsite`: temp TCP proxy created → this container
  measured unable to reach ANY non-443 TCP (bot-DB proxy + fresh proxy both
  timeout; `github.com:443` connects — new ledger wall) → routed to GitHub
  Actions: private repo `menno420/estate-backups` created (201, doubling as
  the probe's positive POST control), one-shot `dump.yml` with the DSN as a
  sealed secret (named-target PUT passed; the same write in an opaque script
  was classifier-denied — the documented shape), run `31935189177` SUCCESS:
  dump both formats, **full restore into scratch postgres:16, `RESTORE
  VERIFIED: counts identical`**, release `postgres-botsite-final-2026-08-16`
  with sha256 manifest. Then service deleted (`serviceDelete: true`; proxy +
  credential died with it), `PGB_DSN` secret deleted (204), and
  `reliable-grace` re-read = `['Postgres', 'worker']` exactly. **Finding: the
  DB was EMPTY — zero public tables**; provisioned 07-12, never written.
- **Accept recorded** on `OQ-SB-BACKUP-ARTIFACT-VISIBILITY`.
- **PAT-mint probed** per the owner's ask (capability-probe skill, full
  method): three creation endpoints 404 vs `GET /user` 200 + `POST
  /user/repos` 201 positive controls, same token — **no API exists;
  fine-grained PATs are UI-mint-only**. Ledger entries appended (this wall +
  the non-443 egress wall, both with used workarounds); `OQ-WEBSITES-PAT` now
  carries the prepped one-minute UI recipe, wire-up promised on paste.
- Records: OQ ✅ entries · §7 row (fm #867) · current-state follow-up line.

**Verify:** run log greps (`RESTORE VERIFIED`), release asset listing +
manifest download, service listing re-read, strict gate at flip (real exit).

**⚑ decide-and-flag:** none new — all three of the owner's answers executed
or recorded; the only remaining owner motion is pasting the UI-minted PAT
when he feels like it.

**💡 idea:** `estate-backups` (private) now exists as the durable home for
any future pre-deletion archive — the dump.yml pattern (sealed DSN → dump →
in-run restore-verify → release) is reusable as-is.

**⟲ previous-session review:** in the header above.

**Layer-2 handoff:** null (no `docs/repos/` folder for the touched repos;
`estate-backups` is a records vault, not a work repo).

**PR:** fm #867 — <terminal state at flip>.
