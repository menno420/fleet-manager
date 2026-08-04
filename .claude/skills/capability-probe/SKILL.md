---
name: capability-probe
description: "The method for testing what a session can do and recording it correctly — run before declaring anything impossible, before assuming a tool or credential is missing, and after discovering something works. Produces a correctly-formed CAPABILITIES.md append entry with venue token and verbatim evidence."
---

# capability-probe

The method skill for the estate's most doctrine-loaded recurring task: turning
"can I do X?" into a ledger fact instead of a guess. The doctrine lives in
`docs/CAPABILITIES.md` (THE DISCOVERY RULE) and the boot file ("record
capabilities, never limitations"); this skill is the executable form.

## When this runs

- You are about to say, think, or type **"I can't"**, "there's no way to",
  "this isn't available", or "the session doesn't have" — STOP, run this.
- A tool, credential, or path you expected is missing.
- Something worked that the ledger doesn't know about — a new capability is
  a deliverable too, and the cheaper one to record.
- An entry you're building on is **older than the 14-day staleness window** —
  it is a claim, not a fact, until re-verified.

## The probe, in order — skipping a step invalidates the conclusion

1. **Check the ledger first** (`docs/CAPABILITIES.md`): the capability or
   wall may already be recorded *for your venue*. Capabilities are
   venue-scoped (`owner-live` · `autonomous-project` · `routine-fired` ·
   `subagent` · `any`); an owner-live fact says nothing about a routine-fired
   seat.
2. **Check the environment before assuming absence**: `printenv` for
   credentials (provisioned tokens are routinely forgotten, not absent),
   `which`/`--version` for binaries, ToolSearch for deferred tools. A missing
   convenience is not a missing capability — `apt-get` and `pip` work here.
3. **Attempt once, for real.** Not a thought experiment — the actual call.
   Capture the **verbatim** error text or the proof it worked. No verbatim
   error = no wall = do it (PL-012 item 4).
4. **One refusal is not a wall.** A denied call can be transient classifier
   state or a path quirk — retry once from a spawned worker, or via the
   documented alternate path (the proxied-vs-direct GitHub split is the
   canonical example: same operation, one path 403s, the other succeeds).
5. **Append the finding SAME SESSION**, below the fence, newest first.

## The entry format — get it right the first time

```
- YYYY-MM-DD · capability|wall · `<venue>` · **<the finding, stated as the
  headline a future session needs>** · evidence: <the exact command/call and
  its verbatim output or error — quoted, not paraphrased> · workaround:
  <the route around, or "none found — <what was tried>">
  — LAST-VERIFIED: YYYY-MM-DD
```

Rules that trip sessions:
- **Re-verifications APPEND, never edit** — a corrected entry sits above its
  predecessor; history is the audit trail.
- **A wall entry without a workaround search is half a probe** — say what was
  tried.
- **Undated walls never age out** (the dateless-wall advisory exists because
  they harden into un-auditable claims) — always stamp LAST-VERIFIED.
- **Weakness is not limitation** (`docs/providers/README.md`): "worse at" is
  a steer and belongs in a provider doc; "cannot" is a wall and needs the
  verbatim error.

## The negative space — what never gets written

**Never write down a limitation in a living doc without the full probe behind
it.** `tools/check_no_false_walls.py --strict` catches present-tense denial
phrasing in living docs — run it yourself; nothing in CI runs it for you. A
false wall stated in *chat* passes the guard clean, which is why this skill
fires at the moment of *thinking* "I can't", not at commit time.

## Traps — each one has cost this estate a real session

- **Generalising from one successful probe**: `gh api user` succeeding was
  read as "auth works" when only that endpoint was served. Probe the actual
  operation you need, not its neighbour.
- **Absence of evidence read as evidence of absence**: "no setup script
  found" was concluded in a session whose environment had one — the probe
  showed only that *this method of looking* found nothing. Say which is
  which.
- **The tool-routing false wall**: a session declared image generation
  unavailable because it searched the wrong catalogue — *"It wasn't a real
  platform limitation. I made a tool-routing error."* Four words of owner
  pushback recovered it; this skill exists so the pushback isn't needed.
- **Trusting a model's account of its own abilities** — including your own.
  Self-report is training data; the probe is telemetry.
