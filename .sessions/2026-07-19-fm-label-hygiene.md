# 2026-07-19 · fm build slice — `scripts/check_label_hygiene.py` (nothing-stuck label detector)

> **Status:** `complete`

About to happen (declared born-red): build slice #3 from
`docs/planning/2026-07-19-next-slices.md` — a new stdlib-only advisory checker
`scripts/check_label_hygiene.py` that mechanizes the owner's 2026-07-19
nothing-stuck directive ("I want them gone, nothing should ever be stuck"):
for every fleet repo, detect (a) any hold-class label DEFINITION
(`do-not-automerge` / `owner-held` / variants — the merge-on-green
`PARK_LABELS` vocabulary plus known variants) and (b) any OPEN PR/issue
CARRYING one. Per-repo table + headline; WARN lines carry the paste-ready
remedy (strip via MCP / hub REST one-liner, citing `OQ-LABEL-DEFS-DELETE`).
Advisory exit 0; `--strict` exits 1 only on an application to an OPEN item
(a mere definition is WARN-only). Reads: unauthenticated-capable GitHub REST
over direct egress with honest per-repo "NOT MEASURED" on any HTTP wall
(403/429 rate-limit aware — never a guess). Also: index line beside the other
advisory checkers (`docs/current-state.md`), `control/status.md` baton
advance, claim `control/claims/claude-fm-label-hygiene.md` (deleted in the
flip commit). No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — new advisory checker, tooling+docs (Q-0105 provenance tier)

## What shipped (PR #370)

- `scripts/check_label_hygiene.py` (new, stdlib + gen_roster LANES import) —
  per-repo hold-class label definitions + open applications over 19 fleet
  repos (LANES repos incl. archived + `EXTRA_REPOS = ["curious-research"]`,
  the Curious Research seat's repo, registry-only in LANES). Hold vocabulary
  anchored on merge-on-green's `PARK_LABELS` + variants (`do-not-automerge`,
  `do-not-merge`, `owner-held/-hold`, `on-hold`, `hold`, `held`, `park(ed)`,
  `blocked`, `stuck`, `needs-hermes-review`); **deliberately excluded:**
  `needs-human-review` + `codex-cleared/-flagged` (codex-triage ROUTING
  labels — merge-on-green ignores them, they hold nothing; decided-and-flagged
  here rather than asked). Transport: two-rung urllib (direct egress first —
  the CAPABILITIES direct-PAT path; then proxied once, the Actions rung);
  Bearer from `$GITHUB_PAT`/`$GITHUB_TOKEN` when set, anonymous-capable;
  403/429 → per-repo `NOT MEASURED (wall: <verbatim>)`, sweep continues.
  Completeness: an applied label always has a repo definition on GitHub, so
  application-scan under found definitions misses nothing (documented in
  header). Exit: advisory 0; `--strict` → 1 only on an application to an
  OPEN item; `--selfcheck` offline pins (classification incl. anchored-match
  safety — `holdings-parser`/`unblocked` never fire — exit contract, remedy
  text cites `OQ-LABEL-DEFS-DELETE` + paste-ready strip path).
- `docs/current-state.md` — advisory-tier bullet extended (fm #370 index
  line beside S3/S5/S9 + lane-liveness + capabilities-grammar).
- `control/status.md` — `updated:` → 16:20Z; wake-paragraph sentence
  (incl. catching up sibling #365/#368 landings the paragraph lacked);
  16:1xZ slice section + baton (next = I8-reads-lane-fence or fresh groom —
  the 2026-07-19 next-slices queue is drained).

## Ground-truth run 1 (2026-07-19T16:15:38Z, full fleet, verbatim)

```
# Label hygiene — nothing-stuck hold-label detector

| Repo | Hold-class definitions | Open items carrying one | Verdict |
|---|---|---|---|
| superbot | none | none | clean |
| superbot-next | none | none | clean |
| substrate-kit | none | none | clean |
| websites | none | none | clean |
| trading-strategy | none | none | clean |
| venture-lab | none | none | clean |
| superbot-games | none | none | clean |
| superbot-idle | none | none | clean |
| superbot-mineverse | none | none | clean |
| pokemon-mod-lab | none | none | clean |
| gba-homebrew | none | none | clean |
| product-forge | none | none | clean |
| idea-engine | none | none | clean |
| sim-lab | none | none | clean |
| codetool-lab-fable5 | none | none | clean |
| codetool-lab-opus4.8 | none | none | clean |
| codetool-lab-sonnet5 | none | none | clean |
| fleet-manager | none | none | clean |
| curious-research | none | none | clean |

HEADLINE: 0 hold-class definition(s) · 0 application(s) to OPEN items · 0 repo(s) not measured (of 19)
```
`--strict` on the same state: exit 0. `--selfcheck`: OK (pins over 19-repo
universe).

**Honest deviation from the dispatch's expected demo:** the task expected
~9 definitions (the `OQ-LABEL-DEFS-DELETE` list of 08:38Z). Live truth at
16:15Z is **0** — the deletions were executed between the queue write and
this run (hub venue or owner; not by this worker). This run therefore IS the
item's "re-run after deletions → 0 definitions" verification, ahead of
schedule. **Caveat verified still live:** websites
`host-automerge-extras.yml` on main still creates + applies
`do-not-automerge` on workflow-touching `claude/*` PRs (raw read 16:16Z,
`gh api … -f name='do-not-automerge'` at ~line 79) — the checker is the
standing tripwire for that re-appearance. Queue-item re-scope flagged to the
coordinator's next records slice, not edited here. Anonymous-path note: the
shared egress IP's unauthenticated api.github.com quota was exhausted at
probe time (verbatim `API rate limit exceeded for 35.253.94.253`), so run 1
rode the PAT rung; the wall rung is exercised by that live 403 + selfcheck
pins, and stays honest (`NOT MEASURED`, never a guess).

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/` 16 files, planning docs,
  2026-07-18/19 cards; no label-vocabulary idea exists):**
  **workflow-sourced park-label vocabulary.** This checker hardcodes
  `HOLD_PATTERNS`, but the fleet's real park vocabulary lives in workflow
  files (`merge-on-green.yml` `PARK_LABELS = {...}`, websites'
  `-f name='do-not-automerge'` create call). A lane inventing a NEW park
  label (e.g. `ratification-park`) parks PRs invisibly to any pattern list.
  Small follow-up: scan fleet repos' `.github/workflows/*.yml` for
  label-literal patterns (skip-if-labeled conditions, label-create/apply
  calls) and diff that harvested set against `HOLD_PATTERNS` — WARN on any
  workflow-referenced hold-shaped label the vocabulary doesn't cover. Turns
  the checker's one blind spot (novel names) into a measured surface.
- ⟲ **Previous-session review (PR #368, R30-adoption records slice):** solid
  records discipline — it caught a sibling's #367 policy landing within ~50
  minutes and annotated three queue threads ANSWERED rather than leaving the
  stale "awaiting confirmation" state to rot; the parallel-writer note
  (zero collisions via per-file claims) is exactly the evidence the claims
  convention wants. Miss, small: its baton still carried
  "`OQ-LABEL-DEFS-DELETE` (9 label definitions)" as an on-owner fact without
  a re-verify flag, and by 16:15Z that count was 0 — same volatile-claim
  lesson the #349→#350 review already named. Improvement: volatile counts in
  baton lines should carry their as-of stamp ("9 defs *as of 08:38Z*"), so a
  later reader knows the number is a snapshot, not a standing truth; this
  card's baton edit does that.
- **Doc-audit:** everything durable is homed — checker motivation + run-1
  evidence in its own Q-0105 header, index in `docs/current-state.md`,
  facts + baton + queue-re-scope flag in `control/status.md`, verbatim table
  here. Nothing chat-only. `docs/owner-queue.md` deliberately NOT edited
  (records surface is the coordinator seat's; flagged in the baton).
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed with the
  payload commit (do-not-revert); born-red HOLD was the only red in
  `bootstrap.py check --strict` pre-flip.
- **Claim:** `control/claims/claude-fm-label-hygiene.md` deleted in this
  flip commit.
