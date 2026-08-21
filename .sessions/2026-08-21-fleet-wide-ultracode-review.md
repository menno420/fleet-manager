# 2026-08-21 — Fleet-wide estate review → Fleet Manager improvement

> **Status:** `in-progress` — branch `claude/fleet-wide-ultracode-review-q2sj7n`,
> fm #878. Owner-directed fleet-wide review: every accessible repository read
> from source, the estate map adversarially verified, and the justified
> fleet-manager routing improvements implemented in this PR. Satellite repos
> were evidence only — none received changes.

- **📊 Model:** fable-5 · high · review/verify

## What happened

1. **Phase 0–1:** the six-read cold-start walked; live account enumerated
   (26 repos via `list_repos`); all 25 satellites shallow-cloned; per-repo
   GitHub state harvested over the direct-PAT path; fm main verified at
   `a12e44f` with 0 open PRs (no conflicting live work).
2. **Phase 2:** 8 parallel family investigators reviewed all 25 satellites
   from source vs fleet-manager's coverage (~1.2 M tokens, 379 tool calls).
3. **Phase 3:** claims driving edits re-verified by this session against the
   tree/live API; then 4 independent refuters attacked the drafted surfaces —
   **116 claims: 106 CONFIRMED · 9 PARTIAL · 1 REFUTED, all corrected before
   landing** — and 10 fresh-agent cold-start routing tests ran against the
   changed front door: **10/10 correct** (owning repos, blockers, contracts,
   ambiguity declared). Evidence:
   [`docs/findings/2026-08-21-fleet-estate-review.md`](../docs/findings/2026-08-21-fleet-estate-review.md).

## Shipped (paths + commits `672e372`, `f86d3db`)

- `docs/ESTATE.md` — the estate index: one routing row per repository
  (all 26), grouped by state, aliases, canonical entries, cross-repo edges,
  owner-vocabulary disambiguation. Linked from `README.md` (live map),
  `docs/MAP.md`, and the boot file's Layer-2 paragraph.
- `docs/repos/{superbot-next,substrate-kit,venture-lab}/README.md` — the
  owner-cleared Tier-1 entry points (settled shape; depth files on demand).
- Refreshed: `docs/repos/spider-swing/README.md` (build vc66; Play thread
  trued — app id + upload key were DONE 2026-08-05; trademark
  settled-for-launch; run-evidence schema-2), `couch-legend` (test-count
  un-frozen; not-a-kit-adopter contract), `superbot` (no-root-README fact,
  dependabot disposition, working contract + stale-walls caveat),
  `websites` (satellite-ledger staleness warning), `estate-backups`
  (archive Release tag named).
- `.claude/hooks/doc-routes.json` — 10 route pairs (20 route records):
  folder routes for product-forge, superbot-next, substrate-kit, venture-lab;
  ESTATE.md routes for the SuperBot-World satellites, codetools, shiftlife,
  gba/pokemon, research family, Substrate-kit-app. `check_doc_routes` 0 errors.
- `docs/owner-queue.md` — OQ-PLAY-APP-ID · OQ-PLAY-UPLOAD-KEY ·
  OQ-GBA-ROM-RULESET · OQ-GBA-LUMEN-RELEASE resolved as overtaken (each
  verified live first); OQ-GBA-NEXT-PICKS + OQ-PML-EMERALD-LETTER added
  (owner-only asks that lived only in satellite closeouts); OQ-POKEMON-*
  annotated with the measured plan-gate conflict (not resolved);
  OQ-VENTURE-PUBLISH-CLICKS corrected (SWTK live since 07-12; OD-11 hold).
- `scripts/check_estate_index.py` — advisory index↔folders↔routes
  consistency checker, house pattern (provenance header, kill-switch,
  `--selftest` 7/7, `--advisory`).
- `docs/planning/2026-07-26-consolidation-program.md` — R3 row enriched with
  the per-lab release mechanics (cfgdiff v0.1.1@`0b1eb60` only; envdrift has
  no release.yml — API Releases at `73ef38d`/`13a84e5`).
- `docs/findings/README.md` — three missing rows added (the two unindexed
  2026-08-14 findings + this review's).
- `docs/current-state.md` — one Recently-shipped entry, **net-zero words**
  (paid for by merging the two same-day couch-legend pointer entries;
  the boot-read set sits exactly at the 7,000-word budget).

## Verify

- `python3 bootstrap.py check --strict` → exit 1 with exactly **1 finding**:
  the designed born-red hold on this card (`[preflight-script]` added-card
  lane). CI substrate-gate red confirmed as the same hold from the job log
  (`session-card-hold`, "designed hold, not a defect"). Stamp findings and
  the orientation-budget red raised mid-session were fixed before landing.
- `python3 tools/check_doc_routes.py` → 52 routes · 0 errors · exit 0.
- `python3 scripts/check_estate_index.py` → 0 findings; `--selftest` 7/7.
- `python3 scripts/check_docs_links.py` → CLEAN, 401 files, exit 0.

## Deliberate boundaries (recorded, not silent)

- Layer-2 folders NOT built for superbot-games / superbot-mineverse /
  gba-homebrew / shiftlife despite investigator layer2-readme
  recommendations — the owner's no-pre-stub doctrine stands; their
  load-bearing warnings ride ESTATE.md rows + routes; build on demand.
- The `current-state.md` "Tier 1 filled" stale line stays — the audit record
  reserves that edit pass for the owner; a drafted fix was reverted (also:
  zero word-budget headroom).
- The raw audit copy of that sentence in `adjudication.jsonl` was left
  verbatim when `change_guard` flagged it — frozen RECORD evidence
  `[survived]`.
- No satellite repo modified; no `register_repo_root` for attached private
  satellites (hub session loads hub apparatus only — boot-triad doctrine).
- Harness note: one acceptance agent's *simulated* answer proposed release
  actions and drew a security flag; verified it performed none (0 tags,
  0 releases live on codetool-lab-fable5).

## ⚑ decide-and-flag

- ⚑ `OQ-POKEMON-ROM-REQUIRED-CHECK`/`-PROTECT-MAIN`: repo records vs the
  measured plan-gate 403 conflict — one owner Settings-UI look settles both
  (annotated in the queue; not resolved on inference).
- ⚑ `check_estate_index.py` ships advisory, not gate-wired — promotion is a
  new red condition and therefore the owner's call.

## 💡 session idea

The kit's `docs/fleet-repos.txt` scan roster omits sim-lab, superbot-idle
and product-forge, so `bootstrap currency` can never report the estate's
oldest kits — a one-line roster fix in the next substrate-kit session
(alongside the 23-row worklist) makes the registry complete; decide
deliberately whether product-forge stays off (archive-bound post-R2).

## ⟲ previous-session review

The previous card (2026-08-20 keep-bot-only execute, fm #871, plus its #874/
#875 correction rounds) held up under independent re-verification: the
mineverse service/project deletion, the review→Pages cutover, the crawler
gate, and the BTD6 sizing all re-confirmed live by this review's
investigators/refuters (websites + estate-backups Layer-2 entries verified
accurate against source). Its post-merge lesson (disarm the enabler before
requesting review) was applied here as doctrine: this PR is born-red-held
until the exact-head review answers.

## Layer-2 handoff

```
Layer-2 handoff: docs/repos/superbot-next/README.md — created (direction fork + traps)
Layer-2 handoff: docs/repos/substrate-kit/README.md — created (worklist + adopter threads)
Layer-2 handoff: docs/repos/venture-lab/README.md — created (OD-11 supersession carried)
Layer-2 handoff: docs/repos/spider-swing/README.md — threads refreshed (build/Play/trademark/run-evidence)
Layer-2 handoff: docs/repos/{couch-legend,superbot,websites,estate-backups}/README.md — corrections applied
Layer-2 handoff: docs/ESTATE.md — baseline 2026-08-21 for all repos without folders
```

## PR

fm #878 — born-red held until this card flips; exact-head Codex review before
the flip per the session-close loop.
