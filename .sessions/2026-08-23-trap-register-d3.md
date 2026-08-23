# 2026-08-23 — D3 first slice: the trap register, and the traps this session proved

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut
> from `origin/main` at `a115e23` (fm #915). Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #915 measured the estate's sharpest structural defect and recommended the
fix: **the trap-delivery gap.** 55 doc-routes installed, **0** of them naming
the estate's own recurring execution mistakes; 26 of 389 session cards restating
the exit-code-after-a-pipe trap; `intent.md` § 2's success criterion — *"the same
class of mistake is never corrected twice"* — failing in the estate's most
recent card. Its recommendation was **D3 as roadmap § 5.4**: harvest the traps,
register them in the structured form, route the top ones through the
`route_docs` hook that is already built and measured working.

This session executes that first slice — and it can do so honestly, because the
session immediately before it **committed the estate's most-restated trap three
times in one conversation, on the same question.** Those instances are the
register's first entries, with verbatim evidence, rather than harvested
second-hand from cards.

The trap to avoid while doing this is the one #915 named: producing **statement
#117**. The value is the lifecycle — mistake → trap entry → route → checker —
not the document. So every entry lands with a route, and the register is
reachable from `MAP.md`.

## previous-session review

fm #915 (`a115e23`) recommended this work and deliberately did not do it —
*"He asked what is most important, not for it to be built."* The owner then said
**"continue, improve anything you can"**, which is the authorisation #915 was
waiting for. Its measurements are reused here rather than re-derived; its
finding that the practice demonstrably works in sibling repos (superbot
802 lines / 689 content vs. fleet-manager 27 / 0) is why this lands as a real
register and not another statement.

## What landed

**[`docs/traps.md`](../docs/traps.md) — the register, five entries**, in roadmap
§ 5.4's required form (TRAP · TRIGGER · WHY · REQUIRED PREVENTION · VERIFY ·
ORIGIN). Three of the five were committed **by the session immediately before
this one**, so their ORIGIN fields carry first-hand verbatim evidence rather
than a second-hand harvest:

- **TRAP-001 · a dated document read as current state** — three instances in one
  conversation on one question. The sharpest: a *correct* finding retracted on
  the strength of a code comment written 2026-06-17, two months before the
  cutover it contradicted; then the sentence *"Measuring the live state
  instead"* followed by a citation to an audit doc. The owner corrected it from
  memory and the live Railway read agreed with him. The credential was in the
  environment throughout.
- **TRAP-002 · an exit code read after a pipe** — the estate's most-restated,
  least-delivered trap (fm #915: 26 of 389 cards, 0 of 55 routes). It recurred
  during R5: `pip install … | tail -5; echo "PIP_EXIT=$?"` printed `PIP_EXIT=0`,
  which was **`tail`'s** exit code.
- **TRAP-003 · absence of evidence recorded as evidence of absence** — the
  26-repo sweep that returned 0 for every repo *including `fleet-manager`*
  because the query carried no search term, and `spider-swing` recorded as
  having no next step from a heading regex when it sits at lines 512–514 in
  prose.
- **TRAP-004 · a claim wider than the sample** — *"only 3 of 26"* written from
  11 probes; `@codex` caught it, and measuring the rest moved it to 7 of 26.
- **TRAP-005 · the owner corrected from memory and was right** — recorded with
  its delivery gap stated plainly, because a hook cannot see a chat message.

**Four `doc-routes` entries, and they are tested, not merely installed.** 55 →
**59 routes**, `check_doc_routes.py` → 0 errors. Each was fired with a synthetic
event and returned its trap text: `exit-code-after-a-pipe` (Bash, pre-execution)
· `stamping-a-measured-claim` · `absence-claim` · `claim-beyond-the-sample`.

**The end-to-end proof was accidental and is the best evidence here.** The
command that *tested* the routes itself piped into `head` and then read `$?` —
and `exit-code-after-a-pipe` fired on it, live, in this session. The route's
first real catch was the session that wrote it.

**[`docs/MAP.md`](../docs/MAP.md)** gains a CORE row so the register is
findable. Deliberately **not** added to the boot file: #915's whole finding is
that statements do not bind, and a sixth restatement in `.claude/CLAUDE.md`
would be exactly the statement #117 it warns about. The routes are the delivery;
MAP is for the auditor.

## What was checked, not assumed

- **Every route fires.** Not inferred from the JSON validating —
  each was fed an event on stdin and its output read.
- **`postgres-botsite` no longer exists.** A full Railway workspace sweep (no
  assumed project id) returned 3 projects / 8 services;
  `reliable-grace` = `Postgres` + `worker`. The 2026-08-14 audit still records it
  as present and hard-rail protected. **Not corrected here** — that is a
  different repo's record and a hard-rail item; it is named in the register's
  TRAP-005 origin and left for a session that scopes it deliberately.
- **fm #915's measurements were reused, not re-derived** — its counts are its
  own and are cited as such.

## The honest gap

Roadmap § 5.4's lifecycle ends at *deterministic checker where possible*, and
this slice stops at route-level for four of five entries. Only **TRAP-002** is
mechanical enough today (`|` plus `$?` is a decidable pattern), and the register
says so in its own coverage table rather than implying full coverage. That
checker is the obvious next slice.

## Verify

- `python3 bootstrap.py check --strict` → **exit 0**, read directly, never after
  a pipe.
- `python3 tools/check_doc_routes.py` → **59 routes · 31 docs routed · 0 errors**.
- `python3 scripts/check_estate_index.py` → 0 findings ·
  `python3 tools/check_no_false_walls.py --strict` → CLEAN.
