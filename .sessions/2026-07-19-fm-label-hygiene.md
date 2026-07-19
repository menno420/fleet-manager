# 2026-07-19 · fm build slice — `scripts/check_label_hygiene.py` (nothing-stuck label detector)

> **Status:** `in-progress`

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
