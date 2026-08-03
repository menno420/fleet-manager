# 2026-08-03 · hub — per-provider capability references: Claude, ChatGPT, Gemini

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — three provider references

Time: 2026-08-03 · venue: owner-live hub chat (owner asleep, autonomous stretch)
· branch `claude/provider-capability-docs`

💡 Session idea: **the estate documents what its agents *did* and never what the
surfaces they run on *are*.** Every ledger, card and plan here records outcomes;
until now nothing recorded the platforms themselves, so each session re-derived
the same provider facts from scratch — and, worse, filled the gaps it could not
derive. The `gh` stall, the Drive-link stall and the "1 million tokens on the free
tier" self-report are all the same shape: a session needed a provider fact,
had no place to look it up, and produced a plausible one.

The generalisable version: **a knowledge base that only records work products
leaves its agents to reinvent the environment.** Outcomes are what a session
*produced*; platform facts are what it *worked against*, and the second is more
reusable because it changes far more slowly than the work does. Concretely — the
`providers/` set should be checked at the same moment `CAPABILITIES.md` is: before
declaring any wall. Worth folding into the boot file's read path once it has
proven itself, which is a change to how every session orients and therefore the
owner's call, not an autonomous one.

## previous-session review

`2026-08-03-hub-surfaces-and-prompt-skills.md` (PR #701, merged) found that the
kit's fourteen skills were staged but never installed, and generalised it to *a
handoff between two systems that each believe the other owns a step is invisible
to both*. This card is the same observation about knowledge rather than
machinery: the boot file owns orientation, the ledgers own evidence, and provider
facts fell between them — nobody's step, so nobody ran it.

## Scope

Owner: a dedicated capability document per AI provider, so a future session can
find the information rather than re-derive it. Claude's is largely covered
already; ChatGPT's should go in depth on the different chat types — regular,
plugin/tool modes like Deep Research and Agent, and the Work environment.

## What landed

`docs/providers/` — README plus one file per provider. Each opens with the same
explicit "this is not a routing table" statement, because that is the only real
risk in a document of this kind.

- **`claude.md`** — model table (IDs, context, max output, per-token pricing), the
  five surfaces, what a session here can do, and the three path quirks that have
  each been recorded as a wall at least once, each with the command that refutes
  it. Plus this estate's own recurring failure modes, written down because they
  are ours and recur.
- **`chatgpt.md`** — the six modes and what each *is*, with Deep Research's
  runtime and the specific way its output stays uniform whether or not the
  evidence was readable; Projects and custom GPTs, with the measured Cloudflare
  403 on project URLs and the verified per-chat workaround; and the Work/Codex
  environment's four breaking defaults.
- **`gemini.md`** — plans, the context ceilings that are the only real capability
  difference, the video token arithmetic cross-checked against Google's own
  one-hour statement, Gems, and the measured instance of the model getting its own
  tier wrong.

Plus a pointer from `execution-surfaces.md` (comparison there, depth here) and a
ledger entry for the ChatGPT environment defaults and mode taxonomy.

## The judgement call worth recording

The owner has a standing constraint against documenting which agent does what.
These documents describe **capabilities**, which is what he asked for, and are
carefully not role assignments — but the distinction is thin enough to be worth
stating: each opens by saying it assigns no roles and that a session reading it
should do the work it was asked to do. The failure it guards against is a session
reading a capability table and declining a task it is perfectly able to perform.

## Honest nulls

- **ChatGPT plan and model details are secondary-sourced.** The primary pages
  returned 403 to a fetcher, aggregators disagreed with each other, and the doc
  says so rather than quoting figures as established.
- **The API-vs-app video tokenisation gap is unverified.** The ≈300 tokens/second
  figure is documented for the API; whether the consumer app tokenises uploads
  identically was not tested, and the arithmetic inherits that.
- **Nothing here is wired into the boot read path.** These are reachable from
  `execution-surfaces.md` and the ledger, but a session that never opens either
  will not find them. Making them boot-path reading changes how every session
  orients — the owner's call.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
