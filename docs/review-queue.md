# Review queue — needs-second-review ledger (post-merge)

> **Status:** `living-ledger`
>
> Created by owner directive 2026-07-09, as part of the gen-2
> merge-authority policy ([`gen2-blueprint.md`](gen2-blueprint.md) §1/§2):
> **no PR ever waits for review before landing.** A PR that deserves second
> eyes is merged anyway and flagged HERE (and/or gets an @Codex mention on
> its thread). Review is **post-merge**; veto = revert (forward-only git).

## How to use

- **Any lane, any session** appends one line per merged PR that deserves a
  second look: `repo#N · what to re-check · why it deserves second eyes`.
- **Reviewer** (Codex, another lane, the owner, a later session) checks the
  item, then either strikes the line (`~~…~~ — reviewed <date>, ok`) or
  ships/queues the revert with a one-line verdict.
- Append-only per line; never rewrite others' open entries (playbook R9).
- This ledger is for *quality* second-eyes. Safety brakes (irreversible /
  external / production actions) are unchanged and pre-merge as ever.

## Open items

*(none yet)*

| PR | What to re-check | Why |
|---|---|---|

## Reviewed / closed items

*(move rows here with the verdict + date)*
