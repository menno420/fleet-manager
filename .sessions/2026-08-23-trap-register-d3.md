# 2026-08-23 — D3 first slice: the trap register, and the traps this session proved

> **Status:** `in-progress` — branch `claude/r5-archive-execution-4dsvoh`, cut
> from `origin/main` at `a115e23` (fm #915). Born red on purpose; flips only
> after `python3 bootstrap.py check --strict` returns a real exit 0, read
> directly and never after a pipe.

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

_pending — filled before the flip._

## Verify

_pending — `python3 bootstrap.py check --strict`, exit code read directly._
