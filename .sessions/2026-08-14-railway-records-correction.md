# 2026-08-14 · hub — records correction: durable-dump home + backup-artifact visibility

> **Status:** `complete`

*(Flip note: Codex reviewed `c20560d` — zero findings ("Didn't find any major
issues"). The one commit after the reviewed SHA, `65d8c34`, is the guard-fire
telemetry JSONL append the pre-flip gate run produced — nothing reviewable.
This flip commit changes this badge, this note, the PR line, and any new
telemetry delta. Nothing else.)*

- **📊 Model:** fable-5 · high · docs-only — correct `OQ-RG-POSTGRES-BOTSITE`
  option A (a Release asset on `superbot` is NOT a safe durable home — the repo
  is public, measured `private: false`) and flag the pre-existing visibility
  question on the daily bot-DB backup artifacts, which live on that same
  public repo.

Time: 2026-08-14 · venue: owner-live hub chat · branch
`claude/railway-websites-audit-gp7nc7` restarted from `main` @ `196d582`

## Previous-session review

⟲ fm #863 (merged `196d582`): the execution session. Its OQ-RG-POSTGRES-BOTSITE
entry recommended "a GitHub Release asset on `superbot`" as the durable dump
home — written without checking the repo's visibility. The owner-review hook
asked the visibility question; the check (`GET /repos/menno420/superbot` →
`"private": false`) refutes the recommendation. This card carries the fix.

## 💡 Session idea

One-line truth repair plus one new flag, measured first: worker's 32 variable
values contain zero `postgres-botsite` references and the DB has no public
TCP proxy — the orphan chain is closed by measurement; and public-repo
Actions artifacts are downloadable by any logged-in GitHub user (platform
behavior), which the daily production-DB dumps have relied on unflagged.

## Close-out

**Shipped:** `docs/owner-queue.md` — option A repointed to a genuinely
durable+private home; new ⚑ `OQ-SB-BACKUP-ARTIFACT-VISIBILITY`.
**Verify:** strict gate green pre-flip (real exit code, no pipe).
**Layer-2 handoff:** null (records-only, fleet-manager itself).
**PR:** fm #865 — flipped complete on top of `65d8c34`; landing on green (direct merge after required checks).
