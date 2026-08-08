---
name: session-close
description: "Land the session — claim, born-red card first, READY PR, batched work, close-out docs, flip complete last; land on green."
---

# session-close

> **Venue note (fleet-manager, 2026-08-04; steps rewritten in place 2026-08-08):**
> the boot file rules `control/` **seat-era historical** here, so the steps
> below now name their live venues directly — the session card, the PR
> description, and `docs/owner-queue.md` — instead of leaving a translation the
> reader had to perform at the most momentum-exposed moment of a session.
> `control/README.md` remains valid as the OWNER-ACTION *format* reference.
> Decided per the precedence rule (the owner-set boot file outranks older skill
> text); **owner-ratified 2026-08-05, veto declined**.
>
> **This file is kit-named**, so a kit upgrade's skill install overwrites it —
> re-apply these local amendments after any upgrade (`docs/SKILLS-local.md`
> § Why the local half exists).


Land fleet-manager's session correctly — the full landing path, claim to
merged-on-green. Playbook-grade: a session reading this executes without
improvising (grounded-skills plan §7.2).

## What this does

Drives the session's work to a terminal, verified state on two rails:
the born-red gate (card first, flip last) and landing your own green PR
(merge it directly once required checks pass, or let the server-side
auto-merge-enabler land it — either is fine). Everything else is ordered
steps.

## Instructions

1. Claim first (session start — verify it happened). In fleet-manager the
   claim is **the born-red session card plus the open PR**, not a
   `control/claims/` file: `control/` is seat-era historical here (boot file,
   owner-ratified 2026-08-05), and the card+PR pair is the in-flight signal a
   parallel session actually sees. In a repo where the control bus is live,
   file the claim there as well.
2. Born-red card as the FIRST commit — `.sessions/<date>-<slug>.md` whose
   Status badge line declares `in-progress` (the born-red hold token), plus
   a one-line "what is about to happen". Push, then open the PR READY (not
   draft) immediately: the open PR + the claim are the in-flight signal
   parallel sessions collide without.
3. Land your own green PR — merging is normal agent work. Once the required
   checks are green, merge it directly (MCP/REST), or let the server-side
   auto-merge-enabler land it; either is fine. Only a `do-not-automerge`-
   labelled PR waits for the owner. Read a red on a born-red head as the
   designed hold, not a CI failure: verify any red against the job log
   before diagnosing — alias/mirror jobs echo the required check without
   running anything (kit repo example: the two legacy jobs mirroring
   `kit-quality`), and "HOLD (by design)" means nothing to investigate.
4. Batch the work — push when a batch is meaningfully complete, never every
   commit (superseded CI runs are the dominant Actions cost).
5. Close-out docs, into the SAME card: what shipped (paths + commits);
   Capability delta — new capability or wall discovered? Append it to
   `docs/CAPABILITIES.md` (dated, with its venue token, exact error or
   proof, workaround — below the seed fence, never inside it); every
   ⚑ needs-owner ask goes to `docs/owner-queue.md` with the OWNER-ACTION
   fields (WHAT / WHERE / HOW / WHY-IT-MATTERS / UNBLOCKS / VERIFIED-NEEDED —
   attempted, or the exact wall; the field grammar in `control/README.md` is
   still the format reference) — withdraw stale asks; groom one idea
   forward; add one new 💡 idea you genuinely believe in; write the ⟲
   previous-session review.
5b. **The Layer 2 handoff — one line on the card, never skipped.** If the
   session worked a repo, update its `docs/repos/<name>/` folder: replace
   **your own** thread block only, close a thread you finished, leave paused
   and parallel threads alone. Then record what you did, verbatim shape:

   ```
   Layer-2 handoff: docs/repos/<name>/README.md — <thread> updated
   Layer-2 handoff: null (<why — e.g. no repo attached; fleet-manager itself>)
   ```

   The null is a **normal, expected outcome** and it is what stops this
   becoming ritual — but it must be written, because a missing line and a
   deliberate null are indistinguishable otherwise. Decided in
   `docs/planning/2026-08-08-fleet-manager-as-index.md` § Maintenance and
   deliberately **not** a gate: *"did the session attach a repo"* is a fact,
   *"did the handoff state change"* is a judgement, and this estate has
   withdrawn two gates for mechanising meaning.
6. Verify — **one command: `python3 bootstrap.py check --strict`.** It fans out
   through `scripts/preflight.py` to the added-card lane and both checkers, so
   this is the same predicate CI evaluates; do not maintain a list of gates
   here, because every written enumeration of it has gone stale (this step
   named two of three until 2026-08-08). Read real exit codes, never `$?`
   after a pipe. The only acceptable pre-flip red is the designed born-red
   hold naming this session's own card — verify that against the job log, and
   note that a failing run's LAST line is telemetry, so read up to the
   `finding(s):` header rather than the tail.
6b. **Leave the truth accurate** — if you completed a program step, append the
   §7 progress-ledger row in `docs/planning/2026-07-26-consolidation-program.md`
   and move the NOW pointer; if you changed an owner ask, update
   `docs/owner-queue.md`; if you verified a new capability, append it to the
   ledger (never a wall).
7. Flip as the deliberate LAST step — flip the card badge to `complete`,
   delete your own claim file, push. Green then merges server-side; a
   flipped-early card merges a partial PR (the failure the gate exists
   for), and an unpushed flip leaves the PR red forever.

## Report format (card close-out)

- Shipped: one line per artifact, with paths + commit SHAs.
- Verify: each command + its tail, verbatim.
- ⚑ decide-and-flag lines · 💡 session idea · ⟲ previous-session review.
- PR: #<n> + terminal state, probed against the tree/checks — not a stale
  PR read.

Declared capabilities: edit (the log + docs), run (the checks + git).
