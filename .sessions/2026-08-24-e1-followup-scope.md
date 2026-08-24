# 2026-08-24 — E1 follow-up: the aphorism that survived its own qualification

> **Status:** `complete` — branch `claude/final-eap-mail-x2s9kx` restarted from
> `origin/main` at `07591dd` (fm #943, merged), landed as fm **#944**. Born red
> on purpose and **verified red at open**: `substrate-gate` returned `failure` on
> `cdf787f` naming the born-red hold (job `97597173590`), per TRAP-006. One
> review round requested and answered at `cdf787f`; **3 findings, all conceded.**
> Flipped after `python3 bootstrap.py check --strict` returned a real exit 0 on
> this tree, read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

Owner-review, immediately after fm #943 merged, asked whether a claim in the
outbound mail was proven or a tendency in one sample. **It was a tendency
stated as a universal, it had reached `main`, and it is now WITHDRAWN** — the
retired wording was *"Agents append; they do not retract."*

*(The retraction marker deliberately precedes the quotation here.
[`check_claim_propagation.py`](../tools/check_claim_propagation.py) only accepts
a marker on the claim's own line or earlier in its block, and that asymmetry is
correct: a record should introduce a dead claim as dead, not quote it and
qualify afterwards. The first draft of this card did the latter, and the sweep
flagged it — the guard working on the document announcing the guard.)*

The paragraph around it is the sharp part. It reads, in order:

1. the mechanism behind the audit's **highest-cost** findings,
2. *"(We did not classify all 101 by mechanism, so read this as the shape of the
   worst ones, not a majority.)"* — a correct, explicit scope limit,
3. the universal anyway — now **WITHDRAWN**: *"Agents append; they do not
   retract."*

**The qualification was appended and the unqualified claim was not retracted.**
That is the exact defect the sentence describes, committed in the sentence
describing it — the fourth instance in two sessions of a lesson failing to bind
the line being written. Six adversarial rounds passed over it; two of them
narrowed the *neighbouring* sentences (round 3 scoped "the dominant class",
round 6 scoped "every review a human actually performs") and left the bolded
aphorism between them untouched.

**Why they missed it is `REASONED`, not measured** (`@codex`, fm #944). The
review history establishes only that the sentence survived while both its
neighbours changed. **The explanation** — that a bolded one-line distillation
reads as a *summary* rather than a claim, and a summary is not where a reviewer
looks for an unsupported assertion — **is an inference of mine.** It matters
because it is the sole basis for treating the mail's other bolded distillations
as a high-risk class; that follow-on inherits the softness and is a hypothesis
worth testing, not a finding.

## previous-session review

fm #943 landed the sweep, the draft and `check_claim_propagation.py`. This
session's fix is a defect in what that PR merged, found one turn after it landed.

## What landed

- The claim scoped to its sample in the outbound mail.
- `agents-append-universal` added to `tools/check_claim_propagation.py` (13
  patterns now), so the wording cannot return silently.
- A pre-send flag on the 97.5 % figure — see below.

## The guard was silenced by one generic word — found by testing it, not reading it

`MEASURED` 2026-08-24. After broadening `agents-append-universal` to catch
paraphrases, a deliberate regression test — reintroduce the **WITHDRAWN** wording
as a paraphrase, *"Agents append; they never retract"*, and re-sweep — reported
**CLEAN**. The cause: **`corrected`**, a bare English word this session had added
to `ALLOW_IN_RETRACTION` a few hours earlier. The mail's own Finding 2 paragraph
uses it to *describe* the defect, it precedes the claim in the block, and the
filter therefore silenced the guard on the one paragraph it most needed to watch.

**`corrected` and `conceded` are removed, and the file now says why:** every
remaining marker names a RETRACTION; neither of those is — they are words
ordinary prose reaches for when merely discussing a correction. **This is the
vocabulary whack-a-mole the file's own comment warns about, committed by the
session that wrote the warning.**

Three further defects in the same tool, each caught by a different check:

- **No match site passed `re.I`**, so a lower-case pattern could not match a
  capitalised sentence. Caught by the selftest reporting `DEAD PATTERN` — a loud
  failure, which is why it cost minutes.
- **An edit anchored on `NEAR_BEFORE, NEAR_AFTER` silently no-opped** because a
  prior commit had already replaced that mechanism, and the `replace()` carried
  no assert. Caught by a `hasattr` failure while debugging something else.
- **A malformed marker list broke the file's syntax.** Caught immediately, because
  a `SyntaxError` cannot be mistaken for a pass.

**The pattern across all four: the checks that failed loudly cost minutes; the
one that failed silently (`corrected`) needed a deliberate regression test to
find.** That is the session's thesis reproduced in its own instrument.

**Both directions now demonstrated:** reintroducing the paraphrase reports
`RESIDUAL -> docs/planning/2026-08-24-final-eap-email-draft.md:106`; restoring
the scoped wording reports `CLEAN`.

## Flagged and moved into the send gate: the 97.5 % has two readings in its own source

`MEASURED` 2026-08-24 by arithmetic on the audit's own table, not by a fresh
database query. [`2026-08-14-railway-websites-audit.md`](../docs/findings/2026-08-14-railway-websites-audit.md)
§ 5 prose says **97.5 %** of the 939 MB `public` schema; its table rows sum to
668 + 135 + 122 = **925 MB**, which is **98.5 %** of 939. The gap is plausibly
exact-bytes-versus-rounded-MB, but **it was not resolved here and must not be
resolved by picking one.** **Recording it only here was the defect** (`@codex`, fm #944): a session card is
not where the sender looks. It is now in the draft's § 2 call 2, with a third
option the earlier framing lacked — **cut the ratio and keep the shape**, since
the argument (cost accumulates unseen) survives with no percentage at all.
