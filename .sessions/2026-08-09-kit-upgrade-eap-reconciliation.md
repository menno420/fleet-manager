# 2026-08-09 · hub — the kit upgrade's payload question, settled; and the EAP correspondence committed

> **Status:** in-progress

- **📊 Model:** opus-5 · high · feature build — work OD-13 (kit upgrade first),
  carrying the EAP reconciliation as a live secondary thread

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/kit-upgrade-eap-reconciliation-e9poz5` (restarted from `b10b38c` =
`origin/main` after #830/#831/#832 merged)

💡 Session idea: **the upgrade's premise was never checked, and it is false.**
The plan said "establish which released kit carries `ADVISORY_CENSUS`, then
upgrade to it." The honest answer is **none does** — it landed on substrate-kit
`main` on 2026-08-06, sixteen days after the last release, and sits under
`## [Unreleased]`. So there is no version to upgrade *to*; the payload has to be
*cut* before it can be adopted. That is a different task from the one that was
planned, and the difference was one clone away for two sessions.

Layer-2 handoff: null (fleet-manager itself; substrate-kit cloned read-only for
the version question, not attached for push)

## Previous-session review

⟲ fm #830 recorded the vendored kit as `1.20.1` with **no** `ADVISORY_CENSUS` in
any vendored Python, and was careful to label the *other* half `UNVERIFIED`:
*"Whether any released kit carries `ADVISORY_CENSUS` in executable code was NOT
verified — substrate-kit was never attached."* fm #831 carried that forward
unchanged. This session attached it and answered the question. **The card that
declared the gap is the reason it got closed** — the `UNVERIFIED` label survived
two handoffs intact and pointed the next session straight at the one missing
measurement. That is the certainty legend doing exactly its job.

## What is about to happen

1. **Settle the payload question** against the released artifacts, not the
   changelog prose. *(done — § below)*
2. **Commit the EAP correspondence record**, verified against Gmail rather than
   relayed, and link it from the E1 plan's § 2.
3. **Put the upgrade fork to the owner** with the measurement in hand, because
   the only route to `ADVISORY_CENSUS` is cutting a substrate-kit release, and a
   release is outward-facing and ships to twelve adopters.

## Verification

At close: `python3 bootstrap.py check --strict`, both checkers directly, and
`tools/test_change_guard.py`, real exit codes, each on its own line, never `$?`
after a pipe. Codex review requested while this card is born-red.

## The payload question, settled three ways

`MEASURED` 2026-08-09. Each leg carries its own positive control, per the § 5
rule promoted into `capability-probe` step 3b — the rule exists because this
estate twice read "I found nothing" as "nothing is there", and one of those two
times was about **this exact symbol**.

| leg | result | positive control |
|---|---|---|
| released asset — v1.20.2 `bootstrap.py` (1,345,814 B, sha256 `48ecd478…`) | **0** occurrences of `ADVISORY_CENSUS` | 32 occurrences of `KIT_VERSION` in the same file |
| released asset — v1.20.1 `bootstrap.py` (1,326,908 B, sha256 `d6c4f815…`) | **0** occurrences | 32 occurrences of `KIT_VERSION` |
| tag containment — introduced by `b505d13` (substrate-kit #577, 2026-08-06) | `git tag --contains b505d13` → **empty** | the same command on v1.20.1's commit returns `v1.20.1`, `v1.20.2` |
| changelog section | the entry is at `CHANGELOG.md:75`, under `## [Unreleased]`, above `## [1.20.2] - 2026-07-21` | section boundaries computed, not eyeballed |

**The asset leg is the one that decides it**, and it is the one a changelog read
would have skipped: adopters vendor the published `bootstrap.py`, so what that
file contains *is* the payload. The other three legs agree with it, which is why
they are worth recording — three methods agreeing is what makes this a settled
question rather than one more `UNVERIFIED` row.

**Also measured, and it removes the risk that made this fork look heavy.**
fleet-manager's vendored `bootstrap.py` is **byte-identical** to the released
v1.20.1 asset (same sha256) — clean vendoring, no local drift to reconcile. And
running substrate-kit main's built `dist/bootstrap.py` against this tree:

```
gate-preview — 9 deterministic site(s) in the census; 0 carry findings here
(0 finding(s)). Promoting the pending ones would red this tree: NO.
94 heuristic advisory finding(s) across 6 checker(s) held off the gate channel
```

Exit code 0. So the `[Unreleased]` batch's most consequential item — promoting
six advisory sites to exit-affecting — **would not red fleet-manager**, and the
94 advisory lines that currently bury the verdict at line 92 are exactly what
`ADVISORY_CENSUS` routes off the agent's channel. The probe wrote nothing beyond
the expected guard-fires telemetry append.

## The EAP correspondence — verified, not relayed

The handoff supplied these as facts to commit. They were **derived by a prior
session and relayed through a prompt**, which is a provenance the estate has
been burned by before (fm #830 error #7: agent-quoted fragments called "owner
messages"). Committing them unchecked would have made a chat transcript into a
repo record without adding any verification — so each was re-measured against
Gmail. **Most held exactly. Four did not, and one of those is a fact that
appears not to exist.**

Full record and the four corrections:
[`../docs/findings/2026-08-09-eap-correspondence-record.md`](../docs/findings/2026-08-09-eap-correspondence-record.md).

**The one that matters most: the 07-22 read-only-cutoff report is not
corroborated.** `in:sent after:2026/07/21 before:2026/07/24` returns two threads,
neither of them it — no owner-sent mail exists on 07-22 or 07-23. The positive
control passed (the same query correctly returns the 07-21 sent messages), so
this is a real absence in the sent-mail lane, not a broken query. It is recorded
as **uncorroborated with the query that failed to find it**, never as "did not
happen" — it may live on a surface Gmail does not hold.

## The fork put to the owner

Not re-litigating the decided part: he chose **A, kit upgrade first**, and that
stands. What changed is the route, because the destination turned out not to
exist yet. Stated with the measurement, and work continued on the EAP thread
while it is open rather than stopping on it.

## Close-out

*(to be completed before the Status flips)*
