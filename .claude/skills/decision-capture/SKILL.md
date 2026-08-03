---
name: decision-capture
description: "Turn decisions that exist only in a conversation into a committed record, so the next prompt can point at them instead of carrying them. Run it when a planning session is about to end, or when a handoff prompt is getting long."
---

# decision-capture

A decision made in chat and never written down has to be re-carried in every
prompt that depends on it, drifting a little each time, until someone re-opens it.
This lands it once.

## What this does

Converts chat-only decisions into a repo record, so handoffs become pointers.
It is the answer to *"should this go in the prompt or in a doc?"* — **in a doc,
whenever it will matter beyond the next session.**

## When to run it

- A planning session is ending and decisions were made.
- `continuation-prompt` produced a long `CARRY` list — that list is the input here.
- Something is about to be explained for the second time.

**Rule of thumb: explaining it twice means it should have been committed the
first time.** The second explanation costs more than the commit would have.

## Instructions

### 1 · Collect only what was actually decided

From the conversation, not from inference:

- the decision, in one line;
- **why** — the constraint or evidence that produced it;
- what it **rules out**, if anything;
- who decided. Owner-stated decisions are durable and outrank later reasoning;
  a session's own working choice is revisable. **Label which.**

Leave out anything still open. An open question recorded as a decision is worse
than not recording it — it will be read as settled and will not be re-asked.

### 2 · Pick the home — do not create a new one by reflex

In order of preference:

1. **An existing living ledger** — the decision ledger, the capability ledger, a
   plan document's own decision section. Best: already read, already indexed.
2. **The session card** — right for a decision that is genuinely about this
   session's work and will be read as history rather than as standing rule.
3. **A new dated doc** — only when the decision set is large enough to need its
   own structure, and then it gets an index row wherever similar docs are listed.

**Never a new top-level file for a single decision.** That is how a doc tree
becomes unnavigable, and an unfindable record is worth about as much as no record.

### 3 · Write it so it survives being read out of context

Each entry, in one place:

```
<date> · <decided | owner-directive | working-choice> · <the decision, one line>
  why: <the constraint or evidence>
  rules out: <what this closes off, if anything>
```

Two properties matter more than format. **Dated**, so a reader can tell current
from superseded. **Labelled by authority**, so a later session knows whether it
may revisit the decision or must treat it as standing.

### 4 · Land it, then point at it

Commit it. Then, in the handoff prompt, the six-line `CARRY` block becomes:

> "Decisions are recorded in `<path>` — read it, and do not re-open anything
> marked `owner-directive`."

That is the payoff. The prompt gets shorter, the record gets durable, and the
next session reads current truth rather than a snapshot of it.

### 5 · Say what you did not capture

Report back in one line: what landed, where, and **what was left out because it
was still open**. The open items are the owner's next decisions and they should
not disappear silently into a doc that only records settled things.

## Traps

- **Do not upgrade a working choice into a directive.** If a session picked
  something reasonable, record it as a working choice. Recording it as an owner
  directive makes it unrevisable and will eventually block work the owner would
  have allowed.
- **Do not record the conclusion without the reason.** A reasonless decision gets
  re-litigated the first time it is inconvenient, and nobody can tell whether it
  is still valid when its constraint changes.
- **Do not batch a decision into a doc nobody reads.** Check the target is
  actually in a reading path. If it is not, it is a rejected record, not a record.
