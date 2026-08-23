# The trap register — the estate's recurring execution mistakes

> **Status:** `binding` · opened 2026-08-23 · program step **D3**, roadmap
> [§ 5.4](planning/2026-08-08-agent-operating-environment-roadmap.md).
>
> **What this is:** the mistakes sessions in this estate *actually keep making*,
> in the structured form roadmap § 5.4 requires — **TRAP · TRIGGER · WHY ·
> REQUIRED PREVENTION · VERIFY · ORIGIN** — each one wired to the moment it
> happens.
>
> **Why it exists:** [`findings/2026-08-08-why-rules-dont-bind.md`](findings/2026-08-08-why-rules-dont-bind.md)
> measured 116 committed statements across 66 files catching **0 of 16**
> incidents, and fm #915 measured the delivery half: **55 doc-routes, none
> naming an execution mistake.** A trap that is only *stated* has never bound
> anything here. So the register is not the deliverable — the **lifecycle** is:
>
> ```
> mistake → trap entry → route/hook reminder → deterministic checker where possible
> ```
>
> **An entry without a route is unfinished work**, not a record. The `route`
> field on every trap below names the `doc-routes.json` id that delivers it, or
> says plainly that it is undelivered and why.

## How to use this file

- **You will not read this file at the moment you need it.** That is the whole
  premise — the route fires and quotes the trap at you instead. If you *are*
  reading it top to bottom, you are auditing, not working.
- **Adding a trap:** it earns a place when it has happened **at least twice**,
  or once with a real cost, and you can name the instances. A trap nobody has
  fallen into is a style preference; keep those out.
- **The ORIGIN field is load-bearing.** It is what stops a future session
  arguing the trap away in the abstract — the instances are named and dated.

---

## TRAP-001 · A dated document read as current state

- **TRIGGER** — you are about to state what is *true now* — a service exists, a
  cron fires, a repo is deployed, a requirement's value, a count — and your
  basis is a document, a file header, a code comment, or a prior session's
  record.
- **WHY** — every document in this estate was written once and describes the day
  it was written; the live surfaces move underneath it. `MAP.md` already closes
  with the rule (*"When a document here contradicts a live surface, the live
  surface wins"*), and stating it there has not prevented a single instance.
- **REQUIRED PREVENTION** — read the **live surface**, with a credential this
  session already holds: `$GITHUB_PAT` over direct egress for anything on
  GitHub, `$RAILWAY_API_KEY` against `https://backboard.railway.com/graphql/v2`
  for anything deployed. If you genuinely cannot, the sentence must carry its
  own provenance: *"per `<doc>` dated `<date>`, not re-verified."* Never launder
  a citation into a measurement.
- **VERIFY** — the claim names **the call and its output**, not a file path and
  line number. "`GET /user/repos` → 26 repositories, 9 archived" passes;
  "`ESTATE.md:44` says nine are archived" does not.
- **ORIGIN** — `MEASURED` 2026-08-23, three instances in one conversation on one
  question, the superbot `botsite/`+`dashboard/` question:
  1. Called superbot's copies vestigial from a Layer-2 doc.
  2. **Retracted a correct finding** on the strength of a workflow header
     comment written 2026-06-17, two months before the cutover it contradicted.
  3. Wrote *"Measuring the live state instead"* and then cited
     `findings/2026-08-14-railway-websites-audit.md:298` — a document.
  The owner corrected it from memory; the live Railway read then agreed with
  him. **The credential was present in the environment the whole time.**
- **ROUTE** — `stamping-a-measured-claim` (fires on Edit/Write of the `MEASURED`
  tag) and `live-state-assertion` (fires on Bash reads of dated records).

---

## TRAP-002 · An exit code read after a pipe

- **TRIGGER** — a shell command containing a pipe, whose result you then read
  with `$?` or `&&`.
- **WHY** — `$?` after `a | b` is **b's** exit code. The failure is silent and
  inverted: the command failed, the check says it passed, and the session
  reports success. This is the estate's single most-restated trap and, until
  today, its least-delivered one.
- **REQUIRED PREVENTION** — do not pipe the command whose exit code you need.
  Redirect to a file and read the code directly (`cmd > out.txt 2>&1; echo $?`),
  or use `${PIPESTATUS[0]}` when the pipe is unavoidable.
- **VERIFY** — the reported exit code came from a command with **no pipe**, or
  from `PIPESTATUS`.
- **ORIGIN** — `MEASURED`: fm #915 counted **26 of 389 session cards** restating
  this trap and **0 of 55 doc-routes** delivering it. It then happened again on
  2026-08-23 during R5: `pip install … | tail -5; echo "PIP_EXIT=$?"` printed
  `PIP_EXIT=0` — which was **`tail`'s** exit code, while the install's real
  status was still unknown. Caught only because the output looked wrong.
  The kit's own gate discipline (*"read its real exit code, never after a
  pipe"*) is stated in the boot file and did not prevent it.
- **ROUTE** — `exit-code-after-a-pipe` (fires on the Bash command itself, before
  it runs).

---

## TRAP-003 · Absence of evidence recorded as evidence of absence

- **TRIGGER** — you are about to write that something is **not** there — not
  indexed, not referenced, not present, no consumers, no next step — and your
  basis is a search that returned nothing.
- **WHY** — an empty result proves your *query ran*, not that the world is
  empty. The query may be wrong, scoped wrong, or aimed at a surface that never
  contained the thing.
- **REQUIRED PREVENTION** — run the **positive control**: make the same query,
  in the same form, find something you already know is present. If it cannot,
  the query is broken, not the world. For a "not in file F" claim specifically,
  **open F** — a keyword search is not a read.
- **VERIFY** — the record states the positive control and its result alongside
  the null.
- **ORIGIN** — `MEASURED`, three instances:
  1. 2026-08-23 — a 26-repo index sweep using `path:README.md` with no search
     term returned 0 for **every** repo including `fleet-manager`; it measured
     nothing. Caught only because a known-good repo also came back empty.
  2. 2026-08-23 — `spider-swing` was recorded as having *"no next-step line
     anywhere in 662 lines"* on the strength of a heading regex. Reading the
     file found the next step at lines 512–514, in prose. The verdict was wrong
     and the method produced it.
  3. 2026-08-09 (fm #830, pre-existing) — a `prompt_routes` probe returned 0 and
     came one sentence from recording a missing route that exists under a
     different key.
- **ROUTE** — `absence-claim` (fires on Edit/Write of absence phrasing).

---

## TRAP-004 · A claim wider than the sample that produced it

- **TRIGGER** — you are about to write a fraction, a total, or a universal
  (*"only 3 of 26"*, *"none of the other 25"*, *"every repo"*) covering a
  population larger than the set you actually measured.
- **WHY** — the unmeasured members get silently classified with the measured
  ones, and the sentence reads as a census when it is a sample. Downstream
  decisions then rest on a number nobody took.
- **REQUIRED PREVENTION** — state **N measured of M total**, and name what the
  unmeasured remainder is. If the claim needs the full population, measure the
  full population — it is usually cheaper than the argument about whether the
  sample generalises.
- **VERIFY** — every count in the claim maps to an item actually probed.
- **ORIGIN** — `MEASURED` 2026-08-23: *"only 3 of 26 repositories are in the
  `search/code` index"* was written from **11** probes, classifying the untested
  15 with the measured 8. `@codex` caught it on fm #912. Probing the remaining
  15 moved the real figure to **7 of 26** — a wider gap than claimed, so the
  conclusion survived, but the evidence had not supported it. A recorded
  `MEASURED` dependency sweep had rested on the same unstated assumption.
- **ROUTE** — `claim-beyond-the-sample` (fires on Edit/Write of census phrasing).

---

## TRAP-005 · The owner corrected from memory and was right

- **TRIGGER** — the owner states something about this estate that contradicts
  what you have just read or concluded.
- **WHY** — he built it, and his statements are source truth per the boot file.
  The failure mode is not disbelieving him outright; it is the softer one —
  treating his correction as a hypothesis to be adjudicated against the
  documents you already misread.
- **REQUIRED PREVENTION** — take the correction as the new baseline and go
  measure the **live surface** to confirm the mechanism, not to test him. A
  probe that disagrees means you took the wrong path.
- **VERIFY** — the follow-up reads a live surface, not another document.
- **ORIGIN** — `MEASURED` 2026-08-23: he said the superbot web services were
  taken offline and should only be live in `websites`. The records said
  otherwise and had been believed twice. The live Railway read returned
  `reliable-grace` = **`Postgres` + `worker`** — exactly what he said, and it
  additionally falsified the audit's claim that `postgres-botsite` was still
  present. **Across four exchanges on this question his recollection beat the
  written record twice and lost zero times.**
- **ROUTE** — undelivered by a hook, and honestly so: a hook cannot see the
  owner's message contradicting a conclusion. This one binds through
  `CONSTITUTION.md` and the boot file's source-truth rule; the register entry
  exists so the instance count is on the record rather than in a transcript.

---

## Coverage — stated so the gap is visible

| trap | delivered by | deterministic checker |
|---|---|---|
| TRAP-001 | 2 routes | not yet — a checker would need to tell a citation from a measurement |
| TRAP-002 | 1 route, fires pre-execution | **possible and worth building** — a `PreToolUse` deny on `\|` + `$?` is mechanical |
| TRAP-003 | 1 route | not yet |
| TRAP-004 | 1 route | not yet |
| TRAP-005 | **none** — see its entry | no |

**The honest state of this register: it is one session old, five entries, four
delivered.** Roadmap § 5.4's lifecycle ends at *deterministic checker where
possible*, and only TRAP-002 is currently mechanical enough to reach that end.
Building that checker is the obvious next slice; the rest stay at route-level
until an instance shows what a checker would have to catch.
