# 2026-08-23 — two asserted claims, tested, settled in opposite directions

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut
> from `origin/main` at `069268a` (fm #929), landed as fm **#930**. Born red on
> purpose and **verified red on open** — `substrate-gate` returned `failure` on
> the first head, naming the born-red hold, per TRAP-006's own check. Flipped
> after `python3 bootstrap.py check --strict` returned a real exit 0 on this
> tree, read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #929 corrected one laundered claim and introduced two more, both asserted
rather than tested. Owner-review caught both. Testing settled them in **opposite
directions**, which is the useful part — the same discipline that upgrades one
claim demotes the other, and a session that only ever "confirms" its own
statements is not running the check.

## previous-session review

⟲ fm #929 (`069268a`) separated a measured absence from a cited deletion — the
right fix. But its *supporting* sentence (*"a dormant service would still be
listed"*) was itself unverified, and its closing caution about
`affiliation=owner` was stated as fact. Correcting a provenance error while
committing two new ones is the pattern worth naming, not the individual slips.

**TRAP-006 fired on this push and was obeyed rather than worked around.** This
change edits an already-complete card, so the diff carried no born-red hold and
the PR would have opened green — auto-merging inside ~37 s, before review. This
card exists to restore the hold.

## What landed

**Upgraded to `MEASURED` — `docs/findings/2026-08-23-active-repo-intent-audit.md` § 3.**
The argument that absence from Railway's service list rules out a *dormant*
service rested on an untested premise. A positive control exists in the same
workspace: **`superbot-websites/dashboard` reports status `SLEEPING` and still
appears in the service list.** So a non-running service IS listed with its
state, and absence from the list is absence of the service. Honest note: this
survived by luck — had every service returned `SUCCESS`, no control would have
existed and the claim would have stayed unverified.

**Downgraded to `REASONED` — this session's predecessor card.** *"If an org is
ever created, `affiliation=owner` silently undercounts"* was inferred from
parameter wording. GitHub's docs define `owner` as *"Repositories that are owned
by the authenticated user"* and `organization_member` as access *"through being a
member of an organization"* — and say **nothing** about a repo owned by an org
the user administers. The empirical check could not settle it either: comparing
both filters against an account with **0 orgs** is vacuous. It is now recorded as
a gap to test *if* an org ever exists, not as a known defect.

## The correction worth carrying

**A comparison run against a population that cannot exhibit the difference
proves nothing, and reads exactly like a passing test.** `affiliation=owner` →
26 and `affiliation=owner,organization_member,collaborator` → 26 looks like
confirmation; with zero orgs it is the only possible result either way. This is
[TRAP-003](../docs/traps.md)'s shape one level up — not a null mistaken for
absence, but a **null control** mistaken for a positive one. The guard is the
same: before trusting a comparison, ask whether the setup could have produced a
different answer.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly, never after a
pipe.
