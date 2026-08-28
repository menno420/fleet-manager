# 2026-08-28 — the estate-wide agent-error harvest (OD-24 §6 step 1, extended)

> **Status:** `in-progress` — born-red by design. The audit is paused at the
> owner's request for a usage-limit reset and resumes on a bound one-shot
> trigger at 23:48Z. This card flips only when the finding lands.

- **📍 Venue:** cloud-container

## Mission

Owner ask, live: find what has already been audited today and what still needs
attention, then fan out across repositories to gather what would improve
`substrate-kit` and its skills — focused on **common agent errors across
sessions and repos**.

That resolves to **OD-24 §6 step 1, extended**. The genesis dig (fm #956)
executed step 1 **fleet-manager-side only**, over the August stepped-back
window, and its §9 names the remainder as skipped: the eighteen satellite
repositories, the June/July bulk, and superbot's PR review threads. This
session sweeps that declared remainder.

## Corpus (measured, not sampled)

- **4,583 session cards** across 20 repositories, 2026-05-29 → 2026-08-28,
  fetched as API tarballs → **7,214 error-bearing sections** → 68 shards.
- **1,592 pull-request review comments** across 12 repositories — **1,431**
  external reviewer findings and **155 written by the owner himself**, the
  highest-signal source in the estate.
- Two independent corpora deliberately: session cards are **self-reported**,
  review comments are **externally caught after the agent declared done**.
  Patterns present in both are the strongest available signal.

## State at pause

226 subagent results cached, zero empty: 2,188 card-corpus incidents · 687
review-corpus incidents · 284 candidate patterns · 20 per-repo
instruction-versus-enforcement censuses. Both harvest phases completed; the
synthesis and adversarial-verification phases were in flight when stopped.

Preserved at `.audit-recovery/` because the harvest lives only on this
container — `find` confirmed **no scratchpad file predates the 18:28:55 boot**,
and the box holds exactly one session directory, so a reclaimed container would
destroy it. The directory is deleted before this PR merges.

## Verify

- Corpus counts are re-derivable: the five scripts in the recovery tarball
  rebuild everything from the GitHub API.
- One in-flight self-correction worth inheriting: the first extraction returned
  **564** sections rather than 7,214, because Python's `glob` does not match
  dot-directories and `.sessions/` was never scanned — TRAP-003's own class
  (a null produced by the query, not the world), hit while auditing for it.

## Not done here

No finding is written yet, no trap is registered, and nothing is proposed to
the kit. Those land when the audit completes.
