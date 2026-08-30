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
   a one-line "what is about to happen", and the required header lines:
   `📊 Model:`, `📍 Venue:`, and `🔗 Session:` — your own id and title read
   via `get_session` (claude-code-remote MCP, no argument), or the exact
   honest-null `unavailable — <why>` where the venue cannot read it
   (D-0023; grammar and forms: `.sessions/README.md` § 🔗 Session).
   **One main PR per session (guideline, D-0024):** the session's further
   work grows THIS PR with more commits — richer card, one flip-readiness
   review round instead of one per split. Open an extra PR (or merge early)
   only for a stated reason, named in the card: urgency · independent
   revertability · reviewability · a records-only PR that must land first ·
   the owner asked. Not a gate — but countable: the card's session line
   groups a session's PRs, so a split with no stated reason is visible. Push, then open the PR READY (not
   draft) immediately: the open PR + the claim are the in-flight signal
   parallel sessions collide without.
3. Land your own green PR — merging is normal agent work. Once the required
   checks are green, merge it directly (MCP/REST), or let the server-side
   auto-merge-enabler land it; either is fine. A `do-not-automerge` label
   holds the lander off while a flagged fork is put to the owner — **within
   the session only**: under `[D-0017]` nothing waits in an open PR across
   sessions. If the fork is still unanswered when the session must end,
   **step 7b is the exit — close nothing from here**; the close-out and the
   ask have not been written yet at this step. Read a red on a born-red head as the
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
5c. **Venue + the activity log — the cross-session half (local amendment,
   2026-08-26, fm #947).** Two small things, both about a session that is not
   this one:

   - The card carries a `- **📍 Venue:** <token>` line under its
     `📊 Model:` line — `local-desktop` · `local-cli` · `cloud-container` ·
     `codex-cloud` · `chatgpt-work` · `other`. **Omit it rather than guess**;
     the generator reports an absent line as `unstated` and prints the
     coverage count, so an honest null stays visible.
   - If the session did anything that produced **no commit anywhere** — a
     laptop change, a ChatGPT or Gemini sitting, a Drive reorganisation, an
     install — that is the one thing nothing can derive, so log it:
     `python3 tools/estate_activity.py log --venue <token> --title "..."`.
     Repository work needs nothing: `refresh` picks the card up on its own.

   Refresh the derived index when you want the current picture across the
   estate: `python3 tools/estate_activity.py refresh`. Not required at every
   close — it is a generated file, and a stale one is corrected by one command.
   Why this exists: [`docs/activity/README.md`](../../../docs/activity/README.md).

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
6c. **Anything you still owe this PR happens BEFORE the flip — Codex review
   above all.** The born-red hold is not only a completeness gate; it is the
   only thing keeping `merge-on-green` off the PR. **The flip is the
   merge-eligibility event**, so a review requested after it is a race you will
   lose. Request the review while the card still reads `in-progress`, wait for
   it (**≥6 minutes**; ~335 s measured), read the **inline** comments rather
   than the summary body, then flip.

   `MEASURED` 2026-08-08 on fm #827: review requested `19:06:39Z`, the enabler
   merged the PR at **`19:07:01Z` — 22 seconds later**, and a commit pushed 55 s
   after that never reached `main` at all. No session merged anything early;
   the close sequence itself was wrong, and this skill's step 7 described the
   flip as bookkeeping when it is the irreversible act.

   **A review binds the SHA it was run on, so acting on findings invalidates
   it.** Applying the fixes and flipping straight away merges correction commits
   that no reviewer has seen — and this repo's own policy rates a stale review
   `REVIEW`, never `PASS` (`docs/workflow-pr-merge-policy.md`). So the step is a
   **loop, not a line**:

   ```
   request review on the current head
     → wait, read the inline comments
     → verify each finding against source before acting on it
     → if you changed anything a reviewer would have an opinion about:
         push, re-request on the NEW head, and wait again
     → flip only when the outstanding review covers the head you are flipping
   ```

   **The loop advances on changes you MAKE, not findings you receive** — that is
   the termination condition, and it is the reason this cannot spin. A finding
   you verify and decline does not start a round; it gets its disposition in the
   PR thread (`[survived]` / `[conceded]` / `[partial]`) and the loop ends.
   Concretely:

   | severity | what it costs |
   |---|---|
   | **P1 · P2** | must be dispositioned — fixed, or refuted in the thread with the evidence. A fix means another round. |
   | **P3 · advisory · nits** | acknowledge and land. **These do not earn a round of their own**; batch them into the next session's work. |

   **Cap it at two re-review rounds, then land with the open findings named** in
   the card and the PR body. This is not impatience — it is `MEASURED`:
   `substrate-kit#580` ran **five rounds and 34 findings without converging**,
   and the convergence predicted from its own curve (9 → 9 → 8 → 2) was falsified
   when round 5 returned 6
   ([`docs/conventions/adversarial-review.md`](../../../docs/conventions/adversarial-review.md)
   § *Round 5 falsified the convergence reading*). A reviewer that always finds
   something is not a reason to never land; **an unbounded loop hands the merge
   decision to the reviewer**, which is the same defect as a gate the owner never
   operates.

   The one exemption is the flip commit itself — a badge flip plus the card's own
   close-out text changes nothing reviewable — and taking that exemption means
   **saying so in the card**, naming the reviewed SHA and what came after it.

   **The failure this prevents was committed four times while writing it:**
   this session requested a review, then pushed again before it landed, four
   consecutive times, each push silently superseding the request it was waiting
   on. Requesting a review and then continuing to push is not waiting.
7. Flip as the deliberate LAST step — flip the card badge to `complete`,
   delete your own claim file, push. Green then merges server-side; a
   flipped-early card merges a partial PR (the failure the gate exists
   for), and an unpushed flip leaves the PR red forever. **After the flip,
   treat the PR as gone:** the lander can take it within seconds, so a
   follow-up correction is a new branch off the new `main`, never another
   push to this one.
7b. **Unanswered fork at close — the `[D-0017]` exit.** If a
   `do-not-automerge` work PR still waits on the owner when the session must
   end: (1) branch a **records-only PR off `main`** carrying the outcome —
   a card **born in its terminal state** recording the fork and the measured
   verdict (the fm #856 / kit #584 precedent), the owner ask in
   `docs/owner-queue.md`, and any §7/ledger rows — and (2) land it green
   through the normal steps above; (3) only then close the work PR with a
   comment linking the landed record — the branch survives for whoever picks
   the fork up. `main` now carries the handoff; the closed PR carries only
   the work. Closing before the records PR lands strands the ask on a
   non-default branch no session reads.

## Report format (card close-out)

- Shipped: one line per artifact, with paths + commit SHAs.
- Verify: each command + its tail, verbatim.
- ⚑ decide-and-flag lines · 💡 session idea · ⟲ previous-session review.
- PR: #<n> + terminal state, probed against the tree/checks — not a stale
  PR read.

Declared capabilities: edit (the log + docs), run (the checks + git).
