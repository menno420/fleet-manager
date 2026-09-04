# The SuperBot rebuild — comparative review and successor plan

> **Status:** `plan` · 2026-09-04 · produced by an Ultracode fan-out session on
> `menno420/fleet-manager`.
>
> **Authoritative for:** the evidence-backed comparison of `superbot` and
> `superbot-next`, the disposition of every meaningful capability and
> engineering pattern, the successor's product definition, architecture,
> verification system and phased roadmap — **until the successor's own
> repository exists and carries them.**
>
> **Authoritative for nothing else.** The source repositories and the live
> services always win. This plan modifies no repository, deploys nothing,
> touches no Discord application, guild, token or production data, and creates
> no repository. `superbot` backs a live production bot and was read-only
> throughout.
>
> **Supersedes** the comparative and architectural halves of
> [`2026-08-21-game-community-bot/`](../2026-08-21-game-community-bot/README.md)
> — see § "What the previous reviews got wrong" in
> [`01-executive.md`](01-executive.md). That plan's owner-directive record
> (OD-16/OD-19 amendments) remains the history of how the direction moved and is
> not superseded.

## Read in this order

| # | File | What it answers |
|---|---|---|
| 1 | [`01-executive.md`](01-executive.md) | What each bot gets right, what each gets wrong, what previous reviews got wrong, the lessons for attempt three |
| 2 | [`02-product-matrix.md`](02-product-matrix.md) | Capability-by-capability comparison with evidence and disposition |
| 3 | [`03-architecture-matrix.md`](03-architecture-matrix.md) | Engineering-pattern comparison with evidence and disposition |
| 4 | [`04-root-cause.md`](04-root-cause.md) | Why `superbot` accumulated debt · why `superbot-next` reached architectural and test completeness without product completeness · how the successor prevents both |
| 5 | [`05-product-definition.md`](05-product-definition.md) | Who the successor is for, what it does, how features are enabled, what the AI is for, the non-goals |
| 6 | [`06-architecture.md`](06-architecture.md) | The successor's composition, ownership, interaction flow, navigation, config, persistence, AI, observability, deployment |
| 7 | [`07-feature-contract.md`](07-feature-contract.md) | What every new capability must provide, and what it must NOT have to modify |
| 8 | [`08-verification.md`](08-verification.md) | The proof layers that replace parity, each with its population and its blind spot |
| 9 | [`09-roadmap.md`](09-roadmap.md) | Dependency-ordered vertical slices with gates, and the first slice named |
| 10 | [`10-migration.md`](10-migration.md) | Old source → contract → new owner → approach → verification → phase; and the data disposition |
| 11 | [`11-risks.md`](11-risks.md) | Architectural, product, verification, migration, operational, AI and scope risks |
| 12 | [`12-owner-decisions.md`](12-owner-decisions.md) | Only the calls that genuinely need his intent, each with a recommended default |
| 13 | [`13-verdict.md`](13-verdict.md) | The readiness verdict and exactly why |

Run material — the preflight contract sheet, the instruments, this session's own
measurements, and the fleet's raw output — is in [`run/`](run/README.md).

## The measurement snapshot

Everything here was measured against these pins at **2026-09-04T11:52:55Z**:

| repo | pin | state |
|---|---|---|
| `menno420/superbot` | `5e3a667b2a55bae98a7863dd66492f477dd19546` | 6,391 commits · 8 open PRs, **all dependabot** |
| `menno420/superbot-next` | `d5f66dc27768d49b2755f368c6a2d0ecca66a1af` | 653 commits · 0 open PRs |
| `menno420/spider-bot` | `bf4d75278a74147aaf9c7f19e2da2c7abb1939cb` | 20 commits · 0 open PRs |
| `menno420/fleet-manager` | `caa6cd2ab6591794258b68b3c385a8378a55c8d3` | shallow clone — no history claim is made from it |

**`superbot` and `superbot-next` are at the exact pins the 2026-08-21 plan
reviewed.** Neither product tree has moved in fourteen days. What has moved is
the owner's verdict.

## The owner's direction this plan is built on

From [`findings/2026-08-28-owner-intent-elicitation.md`](../../findings/2026-08-28-owner-intent-elicitation.md)
§ 1.15, his words verbatim and the newest statement on the bots:

> *"Superbot itself is a repo that's filled with too much history, too many
> trials and errors. What I want from spiderbot and superbot-next (this one will
> have to be remade aswell since the current build is nothing like the desired
> product) is that they eventually are rebuild as one real well functioning bot
> thats build right from the start, which is already documented but apparently
> not well enough.*
>
> *The goal is to create a bot without architectural debt for as far as that's
> possible. Everything should be planned and connected from the start so it
> remains manageable and able to grow indefinitely."*

Four standing constraints from the directive table, all still live:

- **OD-19 (2026-08-23):** the successor must be **cog-portable** — *"I should be
  able to add exiting cogs to it on demand, or be able to slightly alter an
  existing cog so that it works with this bot"* — and **the bots remain
  separated**; the consolidation is of **repositories**, not of running bots.
- **OD-16 (2026-08-21):** server-first, retaining the best of both, AI given
  meaningful freedom from the first slice.
- **OD-13 (2026-08-08):** methods and enforcement come before high-value product
  work. **This plan is method work about a product**, not an execution order —
  nothing here authorises implementation.
- **[D-0025] (2026-08-30):** the estate's plan executes in a **fresh hub
  repository**; this repo becomes the read-only archive. This document is placed
  forward-only under `docs/planning/` and carries no relative links outside
  its own folder that a carry step would have to rewrite, except the four named
  in this section.

And from 2026-09-01, the quality baseline he named himself: documentation that
lets *"any agent work on any repo with little to no input from my side"*, which
*"was especially true in /superbot before the EAP was announced."*
[§ I-9](run/independent-findings.md) measures that claim and finds it dated and
correct.
