# CI consolidation — 2026-07-26

> **Status:** `plan`
>
> Companion to [`2026-07-26-fleet-consolidation-plan.md`](2026-07-26-fleet-consolidation-plan.md)
> (merged as fm #540). Owner asked, 2026-07-26: *"all the CI checks we have,
> would it be possible to consolidate them into less that do the necessary
> things."*
>
> Yes — and it is largely **free**, because most of the surface disappears the
> moment the repo consolidation lands. Measured live 2026-07-26 over the
> direct-PAT path (`.github/workflows/` trees + the Actions runs API).

---

## 1 · The measurement

**97 workflow files across 22 repos. 397 Actions runs in the last 24 hours,
46% of them cron-scheduled.**

| Repo | Workflow files | Runs/24h | of which cron |
|---|---:|---:|---:|
| superbot | 18 | 100 | 24 |
| superbot-next | 8 | 1 | 1 |
| websites | 7 | 39 | 34 |
| superbot-idle | 6 | 1 | 1 |
| product-forge | 6 | 13 | 13 |
| venture-lab / gba-homebrew | 5 each | 4 / 0 | 4 / 0 |
| shiftlife | 4 | 100 | 1 |
| fleet-manager | 4 | 65 | 33 |
| pokemon-mod-lab | 4 | 14 | 14 |
| trading-strategy / superbot-games | 4 each | 4 / 0 | 4 / 0 |
| substrate-kit | 4 | 0 | 0 |
| codetool-lab ×3 | 3 each | 14 each | 14 each |
| superbot-plugin-hello | 1 | 14 | 14 |
| *(7 others)* | 0–3 | 0 | 0 |

Only **two** repos show healthy run profiles: `shiftlife` (100 runs, 1 cron —
all real PR work) and `superbot` (100 runs, 24 cron).

---

## 2 · The diagnosis — the same disease as the repo sprawl

Sort the 97 files by *what they are for*:

| Class | Files | What it is |
|---|---:|---|
| **Agent merge plumbing** | **~43 (44%)** | `auto-merge-enabler` ×14, `substrate-gate` ×14, `merge-on-green` ×7, plus `auto-merge-disarm`, `automerge-card-guard` ×2, `host-automerge-extras`, `ci-rerun-watchdog`, `pr-auto-update`, `pr-conflict-guard`, `heartbeat-guard` |
| **Fleet-oversight automation** | ~8 | `roster-regen`, `roster-freshness`, `main-cron-verify`, `main-verify`, `host-main-advisory`, `quality-main-sweep`, `count-guard`, `heartbeat-guard` |
| **Real product testing** | **~15** | `ci`, `tests`, `pytest`, `quality`, `code-quality`, `codeql`, `golden-parity`, `rom-builds`, `android-ci`, `headless-boot`, `schema-gate`, `theme-gate` |
| Deploy / release / data | ~31 | `release`, `deploy-pages`, `android-release`, `backup-db`, `*-data-refresh`, `smoke-crawl`, `healthcheck`, … |

**Nearly half the CI surface exists to let autonomous agent seats land their own
PRs without a human.** The seats were retired 2026-07-22. The plumbing wasn't.

The part that actually protects the products — real tests — is the **smallest**
class at ~15 files.

### The dead-cron bill

`merge-on-green` fires **14×/day** on `codetool-lab-fable5`, `-opus4.8`,
`-sonnet5`, `superbot-plugin-hello`, `pokemon-mod-lab` and `product-forge` —
repos with **zero open PRs and zero commits since 2026-07-18**. That is ~83
runs/day polling for pull requests that will never arrive.

Add `roster-regen` (20/day, regenerating a roster of seats that no longer
exist), `websites`' 34 cron runs (16 of them `host-automerge-extras`, which the
project closeout itself flagged for removal), and the picture is:

> **Of 185 daily cron runs, roughly 175 serve a program that ended on
> 2026-07-22.**

### What this costs beyond minutes

The `substrate-gate` is not free in reviewer attention either. This plan's own
predecessor PR (#540) was **failed twice by it — on a documentation-only
change**: once because a supersession banner pushed the `> **Status:**` badge
past line 12, once because `superseded` is not in the allowed badge vocabulary.
Neither finding protected anything. That gate was built to hold unattended agent
sessions to a doc discipline; applied to a reviewed human-directed change, it is
pure friction on a doc corpus that is now frozen.

---

## 3 · The fix — and most of it is free

**Archiving a repo stops its scheduled workflows.** So W6 of the repo plan
(archive the 13 emptied repos) removes the dead-cron bill on its own, with no
CI work at all.

That is the key sequencing point: **do not hand-tune 97 workflow files. Land the
repo consolidation, and ~60 of them go away by themselves.** Then standardize
what is left.

### Target: 3 required checks per active repo

| Check | Does what | Where |
|---|---|---|
| **`test`** | The repo's real test suite. Lint/format/typecheck folded in as steps, not separate checks. | Every active repo |
| **`build`** | Proves the shippable artifact still builds. | Only repos with an artifact (bot image, APK, ROM, mobile bundle) |
| **`deploy`** | Release/publish, on tag or main. | Only repos that ship |

Plus a **short** list of genuinely load-bearing specialists, kept because each
catches a class of bug nothing else does:

- `golden-parity` — superbot-next. **The single most valuable check in the
  fleet**: 533 recorded cases proving the rebuild matches the live bot. This is
  what makes the W3 cutover decidable rather than a leap of faith.
- `rom-builds` / `headless-boot` — gba-homebrew.
- `android-ci` / `android-release` — phone-controller.
- `schema-gate` — the mineverse data contract, once folded into the bot repo.
- `codeql` — superbot. Security scanning, keep.

### What gets deleted outright

*(Superseded for fleet-manager itself — 2026-08-11, audit D78. The program's
C2 row carries the corrected rule: keep `merge-on-green`/enabler **wherever
it still lands PRs** — and here it does; it is the workflow that lands this
repo's PRs (§7 records it merging fm #827), and this repo CANNOT use
GitHub-native auto-merge (toggle unavailable on the private-repo plan, per
merge-on-green.yml's own header). Work the C track from the program's C2,
not from this list.)*

The entire **agent merge-plumbing class**: `auto-merge-enabler`,
`merge-on-green`, `auto-merge-disarm`, `automerge-card-guard`,
`host-automerge-extras`, `ci-rerun-watchdog`, `pr-auto-update`,
`pr-conflict-guard`, `heartbeat-guard`. With PRs now reviewed rather than
self-landed, GitHub's native auto-merge toggle covers the remaining need.

### What gets demoted, not deleted

`substrate-gate` — keep it in the **two repos with a living doc corpus**
(`fleet-manager` as records archive, `substrate-kit` as the published kit),
and drop the badge/session-card rules to **advisory** (warn, never fail).
Nowhere else. It should never again fail a product PR over a doc badge token.

`roster-regen` / `roster-freshness` — retire with the roster itself (W7 of the
repo plan). With 9 repos and no autonomous seats, a generated fleet roster has
no consumer.

### Expected end state

| | Now | After |
|---|---:|---:|
| Workflow files | 97 | **~20** |
| Required checks per repo | 2–6, inconsistent | **3, uniform** |
| Runs/24h | 397 | **< 60** |
| Cron runs/24h | 185 | **~5** (backups + scheduled deploys only) |

---

## 4 · Sequencing

This slots into the repo plan rather than competing with it:

- **During W1–W5** — each migration carries the destination repo's checks to
  the 3-check standard as it lands. Do not retrofit repos that are about to be
  archived.
- **At W6 (archive)** — ~60 workflow files and ~175 daily cron runs go quiet as
  a side effect. Measure again here; the remaining list will be much shorter
  than today's.
- **At W7** — retire `roster-regen`/`roster-freshness` and delete the
  merge-plumbing class fleet-wide.

**One-line summary for the owner:** the CI sprawl and the repo sprawl are the
same problem with the same cause, so they have the same fix — and doing the repo
consolidation first makes roughly two-thirds of the CI cleanup happen for free.
