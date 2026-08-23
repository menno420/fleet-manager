# 2026-08-23 — The E1 evidence pack: what the projects actually created, measured

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research *(measurement of the estate from source, written up as the E1 evidence base)*

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

## Adversarial review — `@codex`, 4 rounds, 23 findings

**`[conceded]` × 23 · `[survived]` × 0.** Rounds: 5 · 5 · 8 · 5.

Three would have reached the owner's mail as false, which is the whole reason the
pack got a review at all:

1. **The 8,000 figure.** My first sweep used `search/issues` and returned
   **2,783** — false, because the index is blind to most of this account
   (`superbot` → 0 against a newest PR of #2450). Unchecked, the mail carries a
   figure **5,217 too low**. Re-measured off the `pulls?state=all` Link header
   with positive controls that reproduce.
2. **"He archived them because he could not review them."** Codex refused it: the
   disposition table's nine executed rows give per-repo reasons — releases
   completed, research concluded, scope rejected or unused, experiments parked.
   **None says "could not review."** As drafted it turned a verified count into an
   unsupported causal claim about the owner's motives, addressed to a third party.
3. **The opening sentence** fused an all-time estate total with fortnight output.
   No during-the-fortnight PR count was ever derived.

**And the command-per-figure rule falsified my own arithmetic.** Codex asked for
the recipe behind the `19 / 17 / 1 / 6` partition; writing it and *running* it
showed all 19 EAP-window repositories were created by 07-13 — the 17 is the first
**four** days. I had summed four days and labelled it five. So I stopped trusting
the recipes and extracted each published block from the committed document and ran
it verbatim: `26 / 19 / 17 / 1 / 6`, every figure reproduced.

**The route I added was twice defective before it worked.** Routes fire once per
session per ID, so one route matching both the card write and the push was
consumed by the write, leaving the push silent (`1-then-0`; split gives
`1-then-1`). Then the regex missed `git -c … push` — the estate's own documented
proxy-bypass form — and `git -p/-P push`. Then it fired on a bare *mention*
(`echo git push`), consuming the ID before any real push. Ten forms probed; six
fire, four stay silent. `MultiEdit` was also inert until the hook matcher itself
was updated in `.claude/settings.json` (×3) and `tools/install_root_hooks.py`.

## Accepted open — named, not silently dropped

Four P2s from the final round, left with reasons: two further regex refinements
(quoted shell separators, `env X=1 git push`-style wrappers), fallback-branch
response validation in a recipe, and summing the card census inside the recipe
rather than printing per-repo lines. Rounds went 5 → 5 → 8 → 5 with severity
falling to all-P2; that is where the estate's convention says to stop cycling and
say what remains.

## Verify

- `python3 bootstrap.py check --strict` → **exit 0** at the flip (real exit code,
  redirected never piped — TRAP-002). Born-red hold was the only red before it.
- **CI's own added-card invocations run locally**, after CI caught what my plain
  local run did not: an off-taxonomy `📊 Model:` task class. Both exit 0, zero
  grammar findings.
- `python3 tools/check_doc_routes.py --strict` → **exit 0**, 61 routes · 31 docs
  routed · 0 errors.
- Every published figure re-derived from the tree and cross-checked across four
  surfaces: cards 4,551/4,551 · routes 61/61 · traps 6/6.

## Layer-2 handoff

`docs/repos/websites/README.md` — the review-site era pass landed as websites
#512; this hub session's own deliverable is `docs/findings/`, not a Layer-2 repo.
