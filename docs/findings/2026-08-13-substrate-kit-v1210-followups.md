# substrate-kit v1.21.0 follow-ups — the next kit session's worklist

> **Status:** `reference` · 2026-08-13 · sources: Codex inline review of fm
> #853 (the v1.21.0 adoption diff, head `daf5b7c`) + one residue this session
> found itself. Line numbers are against **vendored v1.21.0**.
>
> **Why this file exists:** the same mechanism that produced
> [the seven-defect worklist](2026-08-09-substrate-kit-defects.md) — Codex
> reading the vendored dist inside an adoption diff — ran again on the release
> that closed it, and returned five findings. Per that worklist's own
> doctrine, **none was patched in fleet-manager**: `cmd_upgrade` overwrites
> the dist and no gate hashes it, so a local patch silently forks one adopter
> and then evaporates. The fixes belong upstream, in the next cut.

## The findings (all Codex, fm #853, P2)

| # | site (vendored v1.21.0) | defect | provenance | why the adoption stands |
|---|---|---|---|---|
| 1 | `bootstrap.py:20183` (workflow generator, verify-step sentinel) | the direct-invocation anchor does not recognise interpreter options — `python3 -u bootstrap.py check --strict` gets NO absent-card sentinel, leaving the mtime-fallback hazard for that shape | **new in v1.21.0** (the sentinel itself is new) | a missed sentinel = the pre-v1.21.0 behaviour, never worse; fm's own confirmed command is the plain form, which IS rewritten |
| 2 | `bootstrap.py:27733` (strict-loop advisory promotion) | a promoted `ADVISORY_GATE_READY` finding prints under the "never exit-affecting" header and records `posture="advisory"` in guard-fires, then fails the command — contradictory output and telemetry | **pre-existing on kit main since #579 (2026-08-06)** — shipped in this release but not authored by it | dormant in practice: the fresh 12-adopter sweep measured 0 promoted-site findings on 12/12 trees |
| 3 | `bootstrap.py:2966` (`check_claim_provenance`, #565) | scans hard-coded `target/docs` instead of `config.docs_root` — silently no findings for non-default layouts | **pre-existing since #565 (2026-08-04)** | advisory checker; every registry adopter runs the default `docs/` |
| 4 | `bootstrap.py:4533` (`check_boot_path`, #579) | infers the agreement via `agreement_home()` file-existence instead of parsing the router's committed pointer — a stale pointer at a missing `.claude/CLAUDE.md` passes when `CONSTITUTION.md` happens to have a boot section, the exact original failure class | **pre-existing since #579** | advisory and deliberately un-gated (its own changelog entry: 11/11 adopters red, hand-edit fix) |
| 5 | `bootstrap.py:5485` (`_CLAUSE_SEP` subordinators + mention region) | a subordinated repudiation ABOUT a quoted mention is severed from it: `The "agents cannot merge" rule is not a wall because it was superseded` stays clear (cue precedes the subordinator), but a predicate carried INSIDE the subordinate clause (`…rule because it is superseded`) now reds where v1.20.2 cleared | **new in v1.21.0** (the defect-7 fix's price) | a false POSITIVE — self-announcing, the cheap direction by the checker's own doctrine; corpus A/B measured 0 newly-flagged lines across both repos' live docs |

## Residue this session found itself (not Codex)

- **The kit's `tests/test_skills_index_install_contract.py` guard regex is
  vacuous against the very text it guards**: `install\s+with[^.]{0,80}skills`
  cannot cross the period in "bootstrap.py", so it would MISS the old
  defect-5 claim if it ever returned. fm's `tools/ab_kit_scan.py` had the
  same `[^.]` gap and fixed it in fm #853 (`[\s\S]{0,100}?`); the kit test
  needs the same one-line fix. Found by running the harness's positive
  control against the dist that HAS the claim (claim=0 where 1 was true).

## How to use this

The next kit session takes this file the way this session took the
seven-defect worklist: fix upstream in this order (2 and 5 first — 2 is a
telemetry/exit contradiction on the required gate's own output, 5 is the only
adopter-facing behaviour regression class), with reproductions before
dispositions, and verify against the published asset, not the changelog.
Rows 1 and 5 carry the fm #853 Codex thread verbatim; rows 2–4 predate the
release and simply had their first non-author read here.
