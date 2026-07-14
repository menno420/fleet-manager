# Branch-recreation census — four-repo read-only sweep (2026-07-14)

> **Status:** `reference`
>
> Four-repo read-only census, 2026-07-14 ~13:4x–14:0xZ (coordinator-run;
> fm-seat Q-0120 spot-checked at 13:49–13:52Z): **460/491 surviving
> `claude/*` agent branches (93.7%) sit at EXACTLY their merged PR's head
> SHA.** Companion to the email draft's ask 4
> ([eap-final-email-draft-2026-07-14.md](../eap-final-email-draft-2026-07-14.md))
> and owner-checklist row 11
> ([eap-owner-checklist-2026-07-14.md](../eap-owner-checklist-2026-07-14.md)).

## Headline

Across four repos, 460 of 491 surviving `claude/*` agent branches (93.7%)
sit at exactly their merged PR's head SHA — i.e. the overwhelming majority
of the branch pile-up is *merged work whose head branch was never (or not
durably) deleted*, not abandoned work.

## Per-repo table

| Repo | Exact-match survivors / surviving `claude/*` branches |
|---|---|
| websites | 154/167 |
| venture-lab | 135/137 |
| fleet-manager | 39/41 |
| superbot-next | 132/146 |
| **Total** | **460/491 (93.7%)** |

## Mechanism (two-tier)

Per curious-research PROPOSAL 003 + the same-day ADDENDUM (menno420/curious-research
`control/outbox.md`):

- **PRIMARY** — GitHub's "Automatically delete head branches" appears NOT to
  fire for PRs completed by auto-merge (merged by `github-actions[bot]`).
  Controlled counter-datapoint: curious-research PR #46's branch survived its
  13:37:07Z auto-merge with zero post-merge push.
- **SECONDARY** (proven by the 6 diverged survivors) — when the ref IS deleted
  at merge, the still-live session container's post-merge push (stop-hook
  flip/close-out) silently re-creates it.

Note that ~59% of merged-PR heads WERE properly deleted, so auto-delete does
fire on some path (owner/hand merges).

## Six diverged survivors

- **websites #19** — merged 2026-07-09T11:37:39Z → post-merge commit
  11:44:26Z, +1 commit — SPOT-VERIFIED live: PR head f53e953…, tip 722a8af…
- **fleet-manager #122** — merged 2026-07-12T19:49:25Z by owner → push 21s
  later at 19:49:46Z — SPOT-VERIFIED live: tip 30a48fa… is a REWRITTEN
  SIBLING of merge-time head fda3182…, not a descendant.
- **venture-lab #150, #173** — census-reported, not individually re-verified.
- **superbot-next #469, #349** — census-reported, not individually re-verified.

## Exact-match spot-samples (fm-seat, live)

- websites `claude/bound-error-reasons` == PR #240 head 8b67fb3…
- websites `claude/fix-landing-grammar` == PR #212 head 2fe6b85…

Both merged by `github-actions[bot]`, corroborating the ADDENDUM.

## Corollary

The ~460 exact-match survivors are **safe to bulk-delete ONCE and that
deletion is permanent for THOSE branches** (their sessions are terminated;
nothing can re-push them) — the hub sweep does it. But accumulation
CONTINUES for future bot-auto-merged PRs until the GitHub-side cause is
resolved and the kit stop-hook guard ships (relayed as substrate-kit inbox
ORDER — a sibling worker is landing it as a kit PR; see the kit inbox ORDER,
control-only PR of 2026-07-14).

## Provenance

Relayed by the Fleet Manager seat per owner discussion, coordinator dispatch
2026-07-14; census coordinator-run, spot-checks per Q-0120.
