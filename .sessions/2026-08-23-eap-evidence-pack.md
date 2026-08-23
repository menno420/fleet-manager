# 2026-08-23 — The E1 evidence pack: what the projects actually created, measured

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs + measurement

## 💡 Session idea

Owner directive, live 2026-08-23: *"the goal will be today to send the mail but
only after we have properly looked at everything the projects created and have a
good batch of information to send them with an updated review website if
possible. ... but first make sure everything is in order etc"*

**E1 stays owner-reserved** (`OQ-E1-FINAL-EAP-EMAIL`) — no session drafts or
sends it. What a session *can* do, and what he asked for, is the half that has
never existed: **the measured evidence base**, so the mail cites numbers derived
today instead of numbers recalled from July.

Two things made this worth a session rather than a lookup:

1. **The consolidation number is finally closed.** The owner's own guidance
   (`docs/owner-reflection-2026-07-21.md` § "The vendor final-review email")
   names *"the consolidation number"* as one of six net-new sections. Until
   2026-08-23 it was an intention — R5 had never archived anything. It has now
   run: **26 repositories, 9 archived, 0 deleted.**
2. **The obvious way to measure the estate is wrong**, and this session hit it.
   See § Correction below.

## Previous-session review

⟲ fm **#918** (`aa9bb86`) — the TRAP-002 checker hardening, on top of #916/#917
(the trap register and its first deterministic checker). Checked at `main`:
`docs/traps.md` carries 5 traps, `tools/check_pipe_exit_code.py` is present and
wired into `scripts/preflight.py`. Nothing to repair. Two sessions ran in
parallel with this one; `main` moved twice during it (`2af06d6` → `aa9bb86`)
and this branch was reset onto each, never merged around.

**The register earned itself inside this session.** `route_docs` fired TRAP-002
at me live while I was cloning `websites` — I had piped `git clone` into `tail`
and read `$?`, which is `tail`'s exit code. The clone happened to succeed, so the
check was invalid rather than wrong. That is the § 5.4 lifecycle working at the
moment of action, on its first day, against the session that recommended it.

## Correction — the first measurement was wrong, and the failure mode is TRAP-003

My first estate sweep used `search/issues` per repo and returned **2,783 PRs
opened all-time**. That number is **false**. `superbot` came back **0** while its
newest PR is **#2450**; `websites` came back 0 while I had an open PR on it.

**The search index does not cover most of this account** — the same defect R5
measured for `search/code` (7 of 26 repositories indexed), now observed for
`search/issues` too. A zero from an unindexed repository is indistinguishable
from a genuine absence, which is exactly **TRAP-003** (absence of evidence
recorded as evidence of absence).

Re-measured with `GET /repos/{o}/{r}/pulls?state=all&per_page=1`, counting the
`Link` header's `rel="last"` page number — a method with a **built-in positive
control**: superbot returns 2,378 against a max PR number of 2,450 (the gap is
issues sharing the numbering), and `websites` returns 512, which is the PR this
session opened. Both controls pass, so the method sees what the search index
could not.

**Had this reached the mail unchecked, the owner would have sent Anthropic a
figure 5,217 PRs too low.**

## What is about to happen

`docs/findings/2026-08-23-eap-evidence-pack.md` — every figure with the command
that produced it, organised against the six net-new sections his own reflection
names, plus the honest nulls. Then the queue and program pointers.

## Verify

(filled before the flip — real exit codes, never after a pipe: TRAP-002)
