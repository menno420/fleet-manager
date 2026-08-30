# 2026-08-30 — the owner's structure sketch captured, with the consults he invited

> **Status:** `complete` — the owner went to sleep leaving his
> target-structure ideas in chat with an explicit invitation: *"you can think
> about this and discuss with gemini and codex if you want."* Chat does not
> survive a container reclaim; this PR does. Both invited consults ran and
> both changed the design: Gemini's six adversarial findings are in the
> addendum, and the Codex round (review object on `9ebe693`) added two more
> — the no-stub candidate now carries an inbound-link-rewrite precondition,
> and the archive search exclusion moves from prose into the tools' real
> ignore configuration. Fixes Gemini-verified before this flip.

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** harness policy forbids a model identifier in a
  pushed artifact; effort and task class are exact.
- **📍 Venue:** cloud-container (owner asleep — autonomous close of an
  owner-live sitting)
- **🔗 Session:** [session_01D2EKd9GfuiWbyuNmCDisLk](https://claude.ai/code/session_01D2EKd9GfuiWbyuNmCDisLk) · "2026-08-28/29 audits and fleet-preflight review"

## Mission

Shipped:

- `docs/planning/2026-08-30-fresh-start-redirect.md` § Addendum — his sketch
  verbatim (root-minimal · `AGENTS.md` routing · a map pointing at
  well-structured folders · per-folder READMEs · the scope-and-time archive
  mirror), his own urgency revision, the session analysis (the `codex.md`
  indirection question; the archive as the new hub's immune system;
  flag-never-auto-move), and the **Gemini consult** — six findings worth
  designing against (search pollution · stub accumulation · mirror drift ·
  reference-lock deadlock · README context cost · routing split-brain), two
  down-weighted with reasons. The **Codex half of his invitation is this
  PR's own review round.**
- `docs/owner-queue.md` — **`OQ-FM-FRESH-START-CONFIRMS`**: the three
  confirms the redirect waits on, now in the one queue the owner reads,
  instead of only inside a planning doc's § Open.

## This PR's exception reason (one-PR guideline)

The sitting's PRs are all merged, so growing one is impossible; the sleep
gap plus an ephemeral container makes this the urgency class (records that
exist only in chat and working tree), and the consult work was his explicit
invitation. Seventh and last split of the sitting.

## Verify

- `python3 bootstrap.py check --strict` → real exit code, no pipe; born-red
  on this card until the flip.
- Gemini call: free-key route, 200/STOP, findings quoted in the addendum
  from the response, not from memory.
- One flip-readiness Codex round (the invited second consult); fixes, if
  any, verified on the free-key route per the cadence.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-session-card-pr-test.md`](2026-08-29-session-card-pr-test.md)
(fm #974, a genuinely different conversation — read whole). **Held up** —
the card-only PR was treated as an instrument and read as one: four landing
mechanisms observed in isolation, an honest TRAP-003 refusal to read 90
quiet seconds as a null, and the trailing telemetry decision put to the
owner instead of decided silently. **Its 💡 idea aged into tonight's
evidence:** it proposed a stale-base warning before `added_cards()` runs —
and this session was bitten by exactly that class twice (the detached-HEAD
chain behind the empty fm #983 merge, and a merged card re-graded as ADDED
before a fetch). Still unbuilt, still queued, now with two more instances
of its justification. **What it could not close and tonight's cadence did:**
its flip-exemption worry (merged heads carrying commits no reviewer saw) is
narrower under the flip-on-answered-verdict practice — every capture PR
tonight flipped only after its round answered, fixes Gemini-verified.

## 💡 Session idea

**Any same-structure mirror doubles the agent search surface.** Gemini's
sharpest finding generalizes past `archive/`: every mirror namespace
(archive, backup, staging) makes each glob and grep return two generations
of truth, and stale hits poison context silently. The new hub's tree design
should reserve exactly one non-active namespace and put its exclusion in
the search tools' real ignore files (`.rgignore`/`.ignore` — not
`.gitignore`, archived files stay tracked), with `AGENTS.md` documenting
the opt-in for deliberate archive searches. (First written as "taught in
`AGENTS.md`" — the Codex round corrected it: prose changes no tool's
default.)
