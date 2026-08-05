# The foundation, the false-negative gap, and the next order of work

> **Status:** `reference`
>
> Written 2026-08-05 at the close of a long owner-live session, on his direction,
> after an adversarial Gemini review of the conclusions below. It **supersedes
> the three next-actions** left earlier the same day — those were written before
> the foundation problem was understood and before the owner explained that he
> has never reviewed a repository or a pull request, which changes what an
> instrument has to be.
>
> **Every claim carries a certainty label.** Read the legend first; it is the
> point of the document.

## 0 · Certainty legend — what you may trust

| Label | Meaning | What a session should do |
|---|---|---|
| **`MEASURED`** | Run this session with a command and a real exit code. Reproducible. | Trust it. Re-run only if the tree moved. |
| **`MEASURED-PRIOR`** | Measured by an earlier session, cited, **not** re-checked today. | Trust for orientation; re-run before building on it. |
| **`OWNER`** | The owner stated it. He provisioned this estate — see `CAPABILITIES.md` DISCOVERY RULE step 0. | Act on it. Do not probe first. |
| **`REASONED`** | My inference from `MEASURED` facts. The facts are checked; the conclusion is judgement. | Argue with it. It is the most likely thing here to be wrong. |
| **`REVIEWED`** | `REASONED`, then attacked by an independent model, and it survived or was corrected. | Stronger than `REASONED`, still not measured. |
| **`UNVERIFIED`** | Believed, cheap to check, **not checked**. | Check it before it becomes load-bearing. |
| **`NOT-VERIFIABLE`** | Cannot be established from a session — owner-console state, cost data, another party's intent. | Do not try. Route to the owner or leave null. |

## 1 · The revised order of work

The three actions left earlier today were: add a `featured_actions` manifest
facet, port the reachability checker, run the `CAPTURE-WORLD LITERAL` sweep.
They were not wrong. They were **aimed at the bot while the instrument that
would verify the bot did not exist**, and they assumed a reviewer who reads code.

Revised, in order:

| # | Work | Why here | Certainty |
|---|---|---|---|
| **1** | **Port the reachability checker to superbot-next**, adapted to manifests. | It gates everything after it. Deterministic — a command is reachable or it is not — so it is safe as a hard gate for an agent. Building UI *before* the gate lets an agent create new dead ends silently. | `REVIEWED` |
| **2** | **Build the Golden Transcript + the state assertion, as one instrument.** See § 4 — the halves are useless apart, and superbot-next already proved it. | It is the only instrument in this estate that would catch an agent breaking logic *quietly*. Nothing today catches that. | `REVIEWED` |
| **3** | **Kit review — but wire, do not classify.** Bifurcate every checker into deterministic (→ hard gate) and heuristic (→ **off the agent's path entirely**, § 5). | Classifying without wiring changes nothing; the tier taxonomy is already known. | `REVIEWED` |
| **4** | `featured_actions` manifest facet, then cog-by-cog curation. | With (1) in place, an agent that wires a button wrong fails a gate instead of shipping a dead end. | `REASONED` |
| **5** | The `CAPTURE-WORLD LITERAL` sweep. | Still open, still unrun, still the right audit — but it is a cleanup, not a foundation. | `MEASURED` (that it is unrun) |

**The purpose ledger is not on this list, and § 3 explains what happened to it.**

## 2 · The gap this session missed, and it is the important one

`REVIEWED` — raised by the reviewer, not by me.

This session measured the owner's detection **precision**: seven catches, seven
correct, zero false positives (§ 6). It never asked about his **recall**.

His signals are entirely exterior — elapsed time, context consumed, a missing
category of output. **Those catch agents that fail loudly.** An agent that works
fast, uses ordinary context, and writes a convincing summary while quietly
breaking logic passes every check the estate currently has.

In the reviewer's words:

> *"The errors you caught are just the noisy ones… It guarantees you will
> silently merge the mistakes of agents that fail quietly."*

This is Goodhart's law pointed at a verification system: agents optimise toward
whatever is measured, and what is measured here is cost and shape. The fix is
not a better exterior signal. It is an **interior instrument that runs without
him** — which is exactly what the reachability checker is, and why item 1 leads.

**The false-negative rate is `NOT-VERIFIABLE`** by construction: you cannot count
what nothing detected. It can only be shrunk by adding instruments, never
measured directly.

## 3 · The purpose ledger — proposed, attacked, and salvaged in a narrower form

`REVIEWED`. Earlier today I proposed a "purpose ledger": one paragraph per repo
and subsystem — what it is, what it does, **why it is built that way** — so the
owner's comparison instrument has something to compare against.

The reviewer's attack, which I accept:

> *"The ledger does not measure the state of the code, it measures the agent's
> ability to parrot your intent… confirmation bias disguised as an audit."*

Written by the same agents whose output it exists to check, and read by someone
who cannot open the code, a uniformly plausible ledger is indistinguishable from
a correct one.

**What survives is one rule.** The `why it is built that way` clause — my
addition — is exactly the decorative half. Strip it. What remains must pass the

> **Physical Execution Test — can the owner run this sentence and see the result
> with his own eyes, in about thirty seconds?**

| Verdict | Example |
|---|---|
| ❌ Fails — unfalsifiable | *"The help system computes commands from the manifest, avoiding transcription drift."* |
| ✅ Passes — checkable by clicking | *"`!help` returns a panel with exactly 7 buttons. Clicking **Roles** replaces it with the role menu."* |

No manifests, no dispatch tables, no architecture. **Observable triggers and
outputs only.** A line that cannot be executed and seen is prose, and prose is
what got the estate here.

## 4 · The instrument the estate actually needs — and the trap it must avoid

`REVIEWED`, with a correction the reviewer could not have made.

The reviewer's top recommendation was a **Golden Transcript**: a plain-text file
of commands and the exact replies they must produce, replayed against a staging
bot, failing the build on mismatch. Its argument is sound — the agent does not
know which inputs will be tested, so it cannot fake the output without executing
the logic.

**superbot-next already has one, and it certified a broken bot.** `MEASURED-PRIOR`:
533 goldens, 49 of 49 subsystems, zero unmapped — against a help tree where 50 of
66 panels are dead ends. The harness compares **output bytes**, and a polite
refusal replays byte-identically forever. A photograph of a menu scores as a menu.

So the reviewer's instrument #1, built alone, is the instrument that already
failed here. Its own second suggestion is the missing half:

> **A state-invariant sweeper** — a list of things that must never be true after
> a run (*"no user with a negative balance", "no item with no owner"*), asserted
> directly against the database, outside the application code.

**Those two together are the instrument. Neither alone is.** One checks what the
user sees; the other checks that *something actually happened*. That is precisely
what the live-audit doc asked for and nobody built:

> *"Attempt three will converge on the same place unless the harness asserts
> **that something happened** — a state change, a database write, an effect —
> rather than that bytes matched."*

**Build them as one gate, or do not build them.** A byte-comparison harness with
no effect assertion is not a weaker instrument than the pair; it is an actively
misleading one, because it produces a green number that means nothing. That is
the single most expensive lesson in this estate and it cost a month.

## 5 · Do not wire every checker to a gate — bifurcate first

`REVIEWED` — this corrects a recommendation I made earlier today.

I proposed classifying rules into prose / checker-not-run / gated, and implied
the fix was to wire the middle tier up. The reviewer's objection is right and
specific:

> *"'Advisory by design' is a human concept… If an agent sees a warning, its
> default behavior is to try and fix it."*

A noisy heuristic wired to a hard gate does not produce compliance. It produces
an agent hallucinating changes to satisfy a false positive, and a deadlocked PR
that needs a human to bypass — which defeats the point.

The rule:

- **Deterministic checkers** — reachability, tool-pin agreement, schema validity,
  tests. Binary, no judgement. **Wire as hard gates.**
- **Heuristic checkers** — stale-wall agers, doc-link drift, idea-groom nags.
  **Take them off the agent's path entirely.** Not merely un-gated — *unseen*.

`MEASURED` this session: every `bootstrap.py check --strict` run emitted ~33
stale-wall plus ~12 dateless-wall advisories, all explicitly "never
exit-affecting". That is a large, permanent noise field in the exact feedback
channel an agent is trying to satisfy. It should be a scheduled report to the
owner, not a line in an agent's gate output.

## 6 · The measured base rate behind all of this

`MEASURED`. Across this session the owner flagged seven problems in my output:
the skipped fleet-manager reading; the possibility that the handoff prompt itself
was at fault; nine dependabot PRs dismissed on a document's word; an unkept
commitment to read the provider docs; a rule I wrote and then failed to follow
three times; and two wrong claims about his own writing.

**Seven flagged. Seven correct. Zero false positives** — including two where he
corrected me about my analysis of his prose. He also supplied a quantitative
prior about a metric I cannot read from inside a session (context consumed,
~300k against ~400k expected) and it was accurate.

That base rate is why `CAPABILITIES.md` DISCOVERY RULE now opens at **step 0**.

## 7 · Honest nulls

- **The false-negative rate is unmeasurable** (§ 2). It can only be shrunk.
- **The Gemini Interaction API could not be used.** `MEASURED`: it exists only on
  Vertex `v1beta1` (`interactions:create`, chained by `previousInteractionId`
  with `store: true` — schema recorded in `CAPABILITIES.md`), and this project is
  rejected `RESOURCE_PROJECT_INVALID` on both project ID and number across four
  locations. The AI Studio surface has no such method at `v1beta` or `v1alpha`.
  Almost certainly a preview allowlist → **`NOT-VERIFIABLE` without an owner
  console action.** The review below ran multi-turn with client-side history
  instead, which is behaviourally identical and only costs tokens.
- **The review is one model, four turns.** It corrected me twice and was itself
  wrong once (it believed the dependabot deadlock was unfixed; it was fixed hours
  earlier). Treat it as a second opinion, not an oracle.
- **§ 4's instrument has not been built or costed.** "One session each" is the
  reviewer's estimate, `UNVERIFIED`.
- **No superbot-next code was read this session.** The rebuild figures are all
  `MEASURED-PRIOR` from earlier today.
- **Whether stripping advisory output from agent feedback is safe is
  `UNVERIFIED`.** It is reasoned, not tested, and it would remove signal a
  session might legitimately want.
