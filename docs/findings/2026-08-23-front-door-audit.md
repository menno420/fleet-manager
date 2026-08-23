# Back-link audit — 9 of 15 satellite front doors never name the hub

> **Status:** `audit` · 2026-08-23 · `MEASURED` unless tagged otherwise.
> Certainty legend:
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
>
> **Read [`2026-08-23-active-repo-intent-audit.md`](2026-08-23-active-repo-intent-audit.md)
> first — it is the primary document for this question and it is better
> grounded than this one.** It ran D2's actual acceptance test by reading each
> repo's declared entry point, and produced the D2 order this repo should work.
> **This file is a narrow supplement**: it adds one measurement that audit did
> not take — whether a satellite README names the hub — and nothing else.
>
> **Two corrections to how an earlier draft of this header described it**
> (`@codex`, fm #937). Its verdict classes **name 16 repositories, not 17**:
> 6 pass · 5 unrated · 1 stale · 3 fail · 1 hub — while its own headline says
> *7 pass*. **`spider-swing` carries no verdict**; it appears only in that
> audit's activity table. So it is not a complete 17-repo sweep, and
> `spider-swing` — the repo with the live external clock — is the unclassified
> one. And **one of its three failures was fixed the same day**, not two:
> `idea-engine` (#900) is a fail and `sim-lab` (#360) is the *stale* row.
> **`product-forge` and `estate-backups` remain open failures.**
>
> **Scope discipline, stated because the first draft failed it (`@codex`, fm
> #937, 5 of 6 findings):** presence of a file is not truth of its contents, and
> **this audit cannot size the documentation work.** The intent audit's verdicts
> decide that. Everything below is about one property: whether a satellite
> repo's root README names the hub.

## 1 · What was measured

**Population: the 15 satellite root READMEs.** Of 17 unarchived repos, `superbot`
has no root README at all (§ 3) and `fleet-manager`'s own README is excluded —
checking whether the hub names itself is not a meaningful test. **17 − 1 − 1 =
15**, which is the denominator throughout. *(The first draft published "6 of 15"
against a stated population of 17 and never named the exclusion — `@codex`
caught that the count could not be reproduced from the method.)*

Method, via the direct-PAT path (`curl --noproxy '*'`, proxy bypassed):

- `GET /repos/menno420/{repo}/git/trees/HEAD?recursive=1` — presence of
  `README.md`, `docs/current-state.md`
- `GET /repos/menno420/{repo}/contents/README.md` → base64-decoded →
  `grep -ci "fleet-manager"`

## 2 · The result

| names the hub (6) | does not (9) |
|---|---|
| `gba-homebrew` 3 · `pokemon-mod-lab` 3 · `idea-engine` 2 · `shiftlife` 2 · `venture-lab` 1 · `estate-backups` 1 | `spider-swing` · `couch-legend` · `websites` · `superbot-next` · `substrate-kit` · `product-forge` · `sim-lab` · `curious-research` · `superbot-plugin-hello` |

**Stated exactly, and no wider** (`@codex`): **9 of 15 satellite root READMEs do
not contain the literal string `fleet-manager`.** That is the whole result.

It is **not** established that those nine have no return path —
[`ESTATE.md`](../ESTATE.md) points outward to all 26 repositories, but whether
each satellite reaches back by some other route is **unmeasured** (§ 4, § 6).
An earlier draft wrote *"the estate's linking is one-directional"* and *"point
nowhere back"*, which its own nulls already contradicted.

Two of the nine carry real recent work — `websites` (19 merged PRs in 14 days)
and `couch-legend` (18), per the intent audit § 5. *(A first draft called four of
the nine "the four most-worked repos in the estate". That was **wrong** and
contradicted by a measurement already in this tree: the real 14-day order is
`fleet-manager` 99 · `superbot` 64 · `websites` 19 · `couch-legend` 18 ·
`spider-swing` **2**, and `substrate-kit` merged nothing in the 7-day window this
session measured. Last-commit dates cannot rank activity; the claim is
withdrawn.)*

## 3 · Presence, as context only — not as a sizing

| measure | result |
|---|---|
| carry a root `README.md` | 16 of 17 |
| carry `docs/current-state.md` | 15 of 17 |

**The one structural absence worth naming: `superbot` has no root README** — the
repo behind the LIVE production Discord bot, entered via
`docs/AGENT_ORIENTATION.md`. Anything arriving at the repository page gets
nothing.

`estate-backups` (130-byte README, no state file) and `product-forge` (24-line
generated template) are **already the intent audit's two open failures** — it
found them by reading contents, which is the method that can actually support
the finding. They are listed here only so this file does not read as if it
discovered them.

## 4 · Why the direction matters — `REASONED`, and narrower than the first draft

The boot triad in [`.claude/CLAUDE.md`](../../.claude/CLAUDE.md) records
(`MEASURED` 2026-08-07, `curious-research`) that a session booting in a satellite
loads **that repo's** `.claude/` and **none of the hub's** — no estate read path,
no doc-routing, no hub skills. PL-013: a routing table cannot bind a session that
never loaded it.

**What that supports:** the hub's apparatus does not auto-load in a satellite, so
discoverability there depends on something written *in that repo*.

**What it does NOT support, and the first draft claimed anyway:** that the README
back-link is *the only* channel. `@codex` was right — the satellite's own
`.claude/` **does** load, so a pointer in its boot file, its `current-state.md`,
or its orientation docs is an equally live boot-time mechanism. **This audit
searched root READMEs only and therefore has not ruled those out.** Whether any
of the nine reach the hub by another route is **unmeasured**; the correct
statement is that their *README* does not, not that they are unreachable.

## 5 · What this does and does not license

**Does:** adding a hub back-link to a satellite front door is cheap and
defensible, and the nine are a concrete list.

**Does not:** treating D2 as a mechanical link sweep, or treating a missing
literal string as a proven missing route. The intent audit's order —
**`product-forge` → `estate-backups` → the `websites` date stamp** — is the
grounded one, because it came from reading contents against D2's actual
acceptance test. Both of those are still-open **failures**, not tidy-ups. Its
five *unrated* repos are one read each and still owed, and **`spider-swing` has
no verdict at all** — classify it before anyone calls that sweep complete.

**No README was edited here.**

## 6 · Honest nulls

- **Truth was not assessed anywhere in this file.** Only presence and one grep.
- **`grep -ci` counts mentions, not working links.** The six positives were not
  checked for whether the path resolves; a mention could be a broken link, and a
  zero could conceivably link by bare URL. Verify before relying on the six.
- **Other discovery channels in the nine were not searched** (§ 4).
- **Staleness signal, corrected:** **three** repos have gone over three weeks
  without a commit — `shiftlife` 07-27, `pokemon-mod-lab` 07-21,
  `superbot-plugin-hello` 07-15. *(A first draft said four and included
  `curious-research` at 08-07, which is 16 days. Arithmetic error, `@codex`.)*
  And staleness of commits is not staleness of docs: all three are paused repos,
  and the intent audit **passed** all three on its acceptance test.
- **The nine archived repos were not audited.** Several are kept as references —
  `superbot-mineverse` carries the SuperBot-World MASTER closeout, the three
  code-tool labs are install documentation for three released CLIs.
  (`superbot-next` is **not** archived: it is active, gated on GCB-1, and is
  inside the 17 counted here. An earlier draft listed it as archived.)
