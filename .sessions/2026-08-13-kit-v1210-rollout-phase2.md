# Session — substrate-kit v1.21.0 rollout, phase 2 (both superbot repos)

> **Status:** `in-progress`
>
> Born-red: this card is the sole FIRST commit on the branch; the program §7 row
> and the ledger entry land in the following commits; the `in-progress` →
> `complete` flip is the deliberate LAST commit.

- **📊 Model:** opus-5 · high · mechanical refactor

## previous-session review

The previous session (fm #853) adopted v1.21.0 here and wrote
`docs/findings/2026-08-13-substrate-kit-v1210-followups.md` — five P2s Codex found
in the vendored dist, none patched, all routed upstream. That doctrine held for this
whole wave: **nothing was patched in any vendored dist**, in either superbot repo.

It also left the adopters registry alone, and that is what bit at the start of this
session: the registry claimed **superbot-next was at v1.17.0** when its tree had been
at **v1.20.2** since #602. The handoff prompt inherited that number, flagged it as
stale, and told this session to verify state before trusting it. That instruction
paid for itself immediately — and the registry turned out to be lying for a
*mechanical* reason, not merely an old one (below).

## Order

The owner, live 2026-08-13: the wave's first batch is **both superbot repos**,
`superbot-next` then `superbot`. One `upgrade-distribution` run each, never batched.
This session records that call in the program's §7 ledger, which is the one place it
existed nowhere before.

## Result

Both repos adopted and **tree-verified at their own `main`**, plus the registry
aftermath. This card's own repo change is records-only: the §7 row and the ledger
entry.

| repo | from → to | PR | merged at | tree-verified |
|---|---|---|---|---|
| superbot-next | v1.20.2 → v1.21.0 | sbn #606 | `d5f66dc` | ✔ dist sha256 + pin |
| superbot | (pin v1.0.0, no dist) → v1.21.0 | sb #2436 | `6067b2d2` | ✔ dist sha256 + pin + 10 allowlist entries + card complete |
| substrate-kit | registry regen | kit #583 | open | — |

`sha256 8807a00e…9cc7356` agreed **five ways** on both adoptions (released asset ·
`release.json` field · sidecar · kit's committed `dist/bootstrap.py` at the release
commit `0021adc`, resolved through the annotated tag `3f1d514` · fleet-manager's
already-adopted copy). superbot-next banked a rollback verified **byte-identical to
the pre-upgrade tree**; superbot banked none and none applies — there was no prior
vendored dist, so its rollback is `git revert`.

### Three inherited claims that measurement overturned

The prompt was explicit that a stale number had already burned this session once. Three
more did not survive contact with the trees:

1. **The allowlist advisory was attributed to the wrong repo.** Briefed as
   superbot-next's enabler arming `{claude/*}` while config would regenerate
   `{claim/*, claude/*}`. Measured: superbot-next's enabler armed **six** prefixes and
   the regen **narrowed** them to one — wrong direction, wrong contents. The
   `{claim/*, claude/*}` advisory is **superbot's**, where config has no `automerge`
   key at all so the comparison runs against kit defaults.
2. **The registry's own identity.** The prompt described "the adopter registry" as
   generated 2026-07-21 with a v1.17.0 row. fleet-manager's `registry/kit-versions.md`
   is a *different* file — generated 2026-07-14, saying v1.15.0, and already
   self-bannered `historical`. The v1.17.0 row lives in the **kit's**
   `docs/adopters.md`. Both are stale; only one was the one meant.
3. **superbot's shape.** "Expect adopt-shaped work" was right that it is not an
   upgrade, but neither documented path fits: `upgrade` refuses outright (no state,
   exit 1, tree untouched) and `adopt` over-corrects into **21 paths**, planting a
   `docs/decisions.md` beside superbot's existing `docs/decisions/` directory and
   regenerating its enabler. The working path is undocumented: **vendor the dist,
   bump the pin**, which runs `check --strict` in full.

### The one I got wrong, and what it costs the rest of the wave

On superbot I corrected two false walls using **fleet-manager's** verified capability
matrix — asserting GitHub repo secrets are agent-settable, and that release creation
works over the direct-credential path. Codex refuted both: neither is verified *in
that tree*, and superbot's own canonical records say the settings layer is
owner-console-only. The "correction" swapped an over-broad wall for an over-broad
capability claim and left two documents disagreeing — the exact condition that strands
a future provisioning session.

**A correction that is not verifiable in this tree must narrow the overclaim, not
replace it with a different unverified claim.** That binds the remaining ~9 adopters,
most of which carry their own wall findings.

### Adversarial review — `[conceded]` 11/11 across two repos

Codex reviewed both PRs. **superbot-next: 7 findings (5 P1, 2 P2), conceded 7/7** — on
a host workflow I wrote to preserve a guard the kit regen dropped. The disqualifying
one: on the close-out push the `synchronize` payload still carries the hold label, so
the enabler's job-level `!contains(…)` skips its **entire job**; the release step then
removes the label, finds nothing armed, and exits — and `unlabeled` is not an event the
enabler subscribes to. **The guard written to protect born-red PRs would have stranded
every one of them.** Withdrawn, not patched: the enabler regen was reverted so that
file is byte-identical to `main`, and the PR ends with **zero** arming-behaviour
change. **superbot: 4 findings, conceded 4/4** (above, plus a miscounted allowlist —
ten entries, not nine).

The general lesson is the one worth keeping: **a guard that is not itself a required
context cannot fail closed.** My "fail loud" `sys.exit(1)` on an unreadable diff felt
safe and was fail-*open*, because a red non-required job blocks nothing.

## Flagged for the owner — decisions I did not take

- **Make `substrate-gate` a required check on superbot-next's `main`?** Today its
  seven required contexts are `code-quality`, `manifest-validate`, `architecture`,
  `sim-gate`, `golden-parity`, `check_compat_frozen`, `pip-audit` — **none reads a
  session card**, so a born-red card holds nothing closed and the in-enabler card
  guard is the only protection. Making the gate required deletes that whole problem
  class by the kit's designed path. It changes merge policy for every PR, so it is
  flagged, not taken.
- **A pre-existing break reds superbot-next's `substrate-gate`.**
  `sb/domain/counting/parsing.py:307` tests `isinstance(node, ast.Num)`, removed in
  Python 3.12, while `substrate-gate.yml` floats `python-version: "3.x"` (now 3.14+)
  and `ci.yml` pins `3.11`. Product source on that branch was **byte-identical to
  `main`**; reproduced under 3.11 by deleting `ast.Num`, which yields the CI error
  string verbatim. Not mine and not fixed — the real question is whether to delete the
  dead branch or pin the gate to the interpreter the product ships on.
- **superbot's gate is honestly red at 2**, not green: `enforcement-unwired` (wiring a
  gate changes how a frozen repo lands PRs, and it would be red from day one) and
  `orientation-budget` (17,664 words against a 7,000 budget — a records restructure,
  the same call reserved for fleet-manager's identical finding). **Flagged, not
  allowlisted** — suppressing either would buy green by hiding a true finding.

## 💡 Session idea

**The registry lies for a mechanical reason, and the mechanism is still live.**
`currency`'s fetcher is `raw → authenticated API → tarball` with the raw step
**unauthenticated** for public repos. Unauthenticated raw served superbot's *pre-merge*
pin persistently — across three regens over ~15 minutes and against a
`Cache-Control: no-cache` request — while git, the authenticated API, the tarball and
*authenticated* raw all returned the correct value. A stale copy is a valid **HTTP
200**, so the fallback chain never engages; there is nothing to fall through from.

That is almost certainly why the registry said v1.17.0 in the first place: not merely
old, but structurally unable to tell "current" from "cached". Every session that
verifies against that registry inherits the lie, and the release cut itself consumed it
(`2026-08-13-kit-release-v1.21.0.md` ran its A/B sweep against "every tree in
`docs/adopters.md`"). **A sweep is only as current as the roster it sweeps.** Fix filed
upstream on kit #583: authenticate the raw step, or reorder to
`API → tarball → raw`.
