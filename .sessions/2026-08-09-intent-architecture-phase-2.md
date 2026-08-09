# 2026-08-09 · hub — review the intent-architecture thread, then Phase 2

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · review/verify — audit what the intent-architecture
  thread landed, fix what the audit finds, then build the Phase 2 slice

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/intent-architecture-phase-2-ntsffd` (started from `d7e7c19`, which is
`origin/main`)

💡 Session idea: **a guard's reach is set by artifact type, not by claim
location — so the estate's most-enforced rule has a hole exactly where its
own toolchain speaks.** `check_no_false_walls.py` is a required status check
built for one rule: never write down a limitation. Its SCAN SET is five file
paths. But the kit itself emits a false wall on **every** `check --strict` run
— `enforcement-required-unverified … (rules API; 403-walled to agents)`, which
`.claude/CLAUDE.md:235-237` records as measured-false since 2026-08-06 — and it
emits it to **stdout**, which no file-scanning checker can reach. The estate
then patched the hole the way it keeps patching holes: a sentence in the boot
file saying *"never quote that NOTE."* That is the injection thesis's own
counter-example sitting inside the injection thesis's home repo. **A claim does
not become safe by being unwritten; it becomes unauditable.**

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ fm #828 landed the Layer-2 ratification and recorded the flip-before-review
trap; fm #829 appended 49 guard-fire telemetry records. Both are sound. The
audit below is not a challenge to their conclusions — it is the re-read that
#828's own two-round cap explicitly left owed, and it found that the ledger
#828 built to be *countable* does not render as a table for six of its eleven
rows.

## What is about to happen

The owner asked for two things beyond the Phase 2 build: **why the repo's 27
skills do not appear in the claude.ai Skills settings list**, and **a review of
the already-landed intent-architecture work before continuing**.

1. **The skills answer**, recorded durably rather than only in chat.
2. **Eight audit findings**, verified against source, and the repo-side fixes
   for those that need no owner decision.
3. **The Phase 2 slice**, tested against real historical owner messages.

## Verification

At close: `python3 bootstrap.py check --strict`, plus both checkers directly,
real exit codes, each on its own line — never `$?` after a pipe. Codex review
requested **while this card is still born-red** (`session-close` 6c).

## What shipped

- **The audit** — eight findings, each verified against source. Five fixed here;
  three left for the owner because they need a decision, not a patch.
- **The error ledger made countable** — six of eleven rows rendered as literal
  pipe text; its class claim corrected from "one defect at four targets" to six
  of eleven instances of one class, `REASONED`, residuals named, arithmetic
  stated.
- **Prompt-route admission bar rule 4 enforced** in `check_doc_routes.py`, and
  `repo-spider-swing` split so the dedup counters are independent.
- **Phase 2's first slice** — the intent map, inside `intake` rather than as a
  new skill, replayed against ten real owner messages:
  [`../docs/findings/2026-08-09-intent-map-replay.md`](../docs/findings/2026-08-09-intent-map-replay.md).
- **The owner's skills question answered durably** in `docs/SKILLS-local.md`,
  with the measured blocker: 15 of 27 descriptions exceed the 200-char cap.

## This session's errors, catcher-attributed

| # | error | caught by |
|---|---|---|
| 1 | probed `doc-routes.json` for a `prompt_routes` key that does not exist, read `0` and was one sentence from recording that Phase 1's prompt route was missing | **self, before cost** — checked the file's actual shape instead of trusting the probe |
| 2 | composed a quotation instead of transcribing it — an `old_string` ending *"as any other"* where the file reads *"as a claim about what he said"* | **the Edit tool's exact-match requirement**, mechanically, at the moment of action |
| 3 | inferred upload-eligibility from **field names** without checking limits on their **values**: *"no frontmatter work is needed"* while 15 of 27 descriptions exceed the 200-char cap | **the owner**, by sending the support article |
| 4 | presented a `REVIEWED` ChatGPT distillation (`intent.md:205`, § 8b) as an owner-verbatim quote, in the SUCCESS cell of a provenance-separation table | **self, by fetching the citation** the ESTABLISHED rule demands |
| 5 | called the Codex review *"overdue at ~8 min"* having counted from PR-open rather than from the request; 223 s had passed against a 335 s baseline | **self**, on computing the actual delta instead of estimating it |

**Errors 1, 3 and 4 are one shape and it is the session's own subject:** a
conclusion drawn one step past what was measured. #1 measured a key's absence and
nearly concluded a feature's absence; #3 measured field *names* and concluded
about field *values*; #4 measured that a line exists in `intent.md` and concluded
whose words it was. **All three were caught by going to the source** — none by
being careful, which is the § 4.8 argument for ESTABLISHED being retrieval rather
than recall, now with the author of that rule as its own data point.

**Error 2 is the mechanical one and worth the most.** No care was involved: an
exact-match requirement rejected a composed quotation the instant it was
submitted. That is the injection thesis in its cheapest possible form — not a
reminder to transcribe, a tool that cannot accept a paraphrase.

## Verification

Real exit codes, each command on its own line — never `$?` after a pipe.

- `python3 bootstrap.py check --strict` → **exit 1** while born-red, sole finding
  the added-card hold; **exit 0** expected on the flip.
- `python3 tools/check_doc_routes.py --strict` → **exit 0**.
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- The new bar-4 check verified **in both directions**: exit 0 on the tree, exit 1
  with the `BAR 4` message on a reintroduced mixed route, exit 0 on restore. A
  green checker nobody has seen fire is not evidence.
- Every push confirmed by comparing `git rev-parse HEAD` to `git ls-remote` —
  never by a pipeline's exit status.
- All relative links in the seven touched files resolve (0 broken).
- Five CI reds on fm #830, each checked against the job log rather than assumed:
  all five the designed born-red hold, checkers `0 errors · 0 notes`.

## Review record

*(pending — Codex review requested at `07:19:11Z` while this card is born-red,
per `session-close` 6c. The card does not flip until the inline comments are read
and each finding verified against source.)*
