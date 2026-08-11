# 2026-08-11 · hub — commit what only the chat holds, then hand the audit over

> **Status:** `in-progress`

- **📊 Model:** identity withheld by session policy · high · docs-only
- Time: 2026-08-11 · venue: owner-live hub chat · branch
  `claude/fleet-manager-full-audit-lty31q`

💡 Session idea: a handoff prompt is the wrong home for anything that will still
be true next week. Everything in this card was about to be typed into a prompt;
committing it first made the prompt four pointers long.

Layer-2 handoff: null (fleet-manager itself)

## What is about to happen

The owner asked for a continuation prompt so the next session can **verify** the
full-read audit and continue from its findings. Running `prompt-preflight` first
turned up three things that exist only in this conversation and would have been
carried inline — which is the failure mode that skill exists to prevent:

1. **The one-PR constraint was never his.** *"The 1 PR instruction wasn't mine,
   that's probably something the previous session invented… It does not matter
   if it happens in 1 PR or 100."* `docs/current-state.md:180` records the grep
   result; nothing records the **directive**, so the next prompt would have had
   to re-carry it and the one after that would have drifted it.
2. **The audit's headline seven have moved since `findings.md` was written** —
   this session's own PRs closed one of them. A session handed that list
   unchanged re-fixes what already landed and concludes the audit was wrong
   about the rest.
3. **The open-PR read gap has no home outside a closed PR's comment thread and
   fm #842's card**, both `RECORD` tier. A planned mechanism recorded only in
   records is a planned mechanism nobody builds.

**And the review changed what two of those three say.** Codex refuted the
diagnosis behind (3) — a `binding` rule already requires the scan
(`control/claims/README.md` step 1); it just lives where every orientation
surface teaches sessions not to look, which makes this a delivery failure rather
than a missing rule. It also refuted the universal in (1): two narrower PR-count
rules are live, and the grep that "proved" otherwise missed one **inside its own
scope**. Both corrections are in the shipped artifacts, and the wrong versions
are recorded beside them rather than quietly replaced — this session's whole
subject is that an appended correction which does not retract is worthless.

## Previous-session review

⟲ fm #842 salvaged fm #838's residue and named the open-PR asymmetry in its
⚑ Owner-facing block. That was the right place to *report* it and the wrong
place to *keep* it: the card is provenance, and provenance is not a backlog.
This card exists partly to correct that.

## Close-out

### Shipped

- `docs/decisions.md` — **`[D-0016]`**, the owner-directive that work is sized by
  what is properly done rather than by pull-request count, with the
  CONSTITUTION's "prompts are guidance, not orders" as what it rules out, and —
  after review — the two narrower PR-count rules that do exist, plus a note
  recording that the grep behind the first version's universal was weaker than it
  read.
- `docs/audits/2026-08-10-full-read/findings.md` — a **status block on the seven**,
  measured against the tree on 2026-08-11 rather than asserted: **1 closed,
  6 open**, each with the command that re-checks it. No `PARTIAL` survived review
  — twice a same-file edit had been credited as progress on the defect that
  produced it. Row 3 was re-judged outright: its "live deployment surface" premise
  fails against the tier map and against the file's own superseded header. Plus
  the **anchor-drift warning**, which names the derivation command rather than a
  file list, because the list written from memory was 6 and the derivation
  returns 24.
- `docs/ideas/consume-the-open-pr-signal-2026-08-11.md` — the delivery failure
  behind fm #838, with the binding rule that already covers it, the route that
  survived two rounds of refutation, and the trust boundary an implementer needs.
- `docs/current-state.md` — the fm #842/#844 recently-shipped entry that was
  missing, so the `CORE` read reflects what landed.

### Verify — real exit codes

```
python3 bootstrap.py check --strict   → 1  (sole finding: this card's designed born-red hold)
added-card lane, run direct           → session-card-hold only, no masked finding
```

**One advisory is worth acting on and is not this card's to fix:**
`[orientation-headroom] boot-read set at 6736/7000 words — 264 of headroom`,
`docs/current-state.md` carrying 6,036 of them. This PR's edits pushed it there.
Every session that appends a Recently-shipped entry moves the `CORE` read closer
to a cliff nobody has budgeted for, and the entries nearest the top are the ones
a fresh session most needs. Trimming it is a real task, not a drive-by — logged
for the edit pass.

### ⚑ Owner-facing

- `OQ-FM-D2-TARGET` — unchanged; still his call, and still the one thing
  blocking D2 from naming a repository.
- The audit's 101 defects remain an **edit pass nobody has started**. This
  session read, reported and recorded; it did not fix. That is the next
  session's work and the handoff prompt says so.

### Ideas

💡 The estate has a `RECORD`/`TASK` tier system and no rule about which tier a
*commitment* may live in. Three of this session's follow-ups were sitting in
`RECORD`-tier session cards, which are read as history and therefore never
actioned. A commitment recorded in a record is a commitment discarded politely.
