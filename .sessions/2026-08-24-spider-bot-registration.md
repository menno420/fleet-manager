# 2026-08-24 — spider-bot joins the estate: ESTATE row, Layer-2 folder, routes, GCB-1 resolution

> **Status:** `complete` — branch `claude/spider-bot-registration`, off
> `origin/main` at `a9d36ae`. Born red on purpose: the card was the merge hold
> (TRAP-006/007). Flipped after `python bootstrap.py check --strict` returned
> the designed born-red hold naming this card and nothing else (CI
> substrate-gate red verified against the job log as the same hold), **and**
> after `@codex` answered clean on `156d77c` — the head being flipped. This
> flip commit is the exempt close-out (badge + card text only); reviewed SHA
> `156d77c`, nothing else came after it.

- **📊 Model:** fable-5 · docs-only (registration of an externally-built repo)

## previous-session review

⟲ The 2026-08-24 clean-verdict card (fm #941's chain): TRAP-007 and the
two-shapes correction are present at `main` (`docs/traps.md:259`, the
review-object-vs-issue-comment split). One live data point from this session:
**today's clean pass on fm #942 DID carry a `Reviewed commit:` line in the
issue comment** (`156d77c242`, matching the head), where fm #938's clean pass
measurably carried none — so the line is *variably* present. Their operative
conclusion (never RELY on parsing it) holds and is strengthened; the stronger
claim ("that line does not exist in a clean-pass comment") is falsified by
today's artifact. Recorded here rather than editing their card.

## 💡 Session idea

`scripts/check_estate_index.py` compares the header's declared count against
the table rows — which caught this session's 26→27 drift exactly as designed —
but nothing compares the table against the **live account** (`GET
/user/repos`). A repo created and never registered is invisible to every
checker: spider-bot existed for most of a day with no ESTATE row and nothing
flagged it. A once-per-run advisory that diffs the row names against the live
list (over the direct-PAT path CI already can't use — so local-only, like the
rest of that script) would make "unregistered repo" a finding instead of a
discovery.

## Shipped (all at `156d77c`)

- `docs/ESTATE.md` — spider-bot row (Active), baseline restated **26 → 27**
  with split verification dates, "the bot" disambiguation now names three
  candidates, `superbot` + `superbot-next` rows and the cross-repo edge
  updated, plugin-hello gate note.
- `docs/repos/spider-bot/README.md` — Layer-2 entry point, README-only
  on-demand shape, reasons in header; threads: Phase-0 hardening (closed) ·
  next feature (owner's pick) · plan transplant (open).
- `docs/repos/README.md` — coverage row.
- `.claude/hooks/doc-routes.json` — `repo-spider-bot` + `repo-spider-bot-prompt`
  (the folder ships with its routes in the same PR).
- `docs/owner-queue.md` — `OQ-GCB-REVIEW-SCOPE` dated update: the GCB-1
  clause is resolved by creation; the A–D letters stay owner-only.
- `docs/current-state.md` — the OD-19 bullet's "GCB-1 is unchanged and still
  owner-gated" corrected in place.
- `.substrate/guard-fires.jsonl` — telemetry delta, committed per its rule.

Context, for the record: the repo being registered was built and hardened the
same day **outside this venue** (owner-directed laptop-hub sessions) —
menno420/spider-bot@e0d8909: 78-test pytest harness + ruff + informational CI
`quality`, deploy verified live (`meta.commitHash` = HEAD; deploy log
`ready as Spider Bot#7153 in Slingy Spider; AI=True`). This PR is the
estate-side record of that fact, not the work itself.

## Verify

- `python tools/check_doc_routes.py` → `67 routes · 33 docs routed · 0 errors · 4 notes`
- `python scripts/check_estate_index.py` → `0 finding(s)` (after the baseline
  restate; its row-count checker caught the 26/27 drift first — working as
  designed)
- `python bootstrap.py check --strict` → pre-flip: the designed born-red HOLD
  naming this card, and nothing else.
- `@codex` on `156d77c`: *"Didn't find any major issues."* — 0 inline
  comments (the `/pulls/942/comments` endpoint read directly, per TRAP-007's
  lesson, not inferred from the summary).

## ⚑ decide-and-flag

- ⚑ GCB-1's resolution half-lifts the `superbot-next` + `superbot-plugin-hello`
  archive gate; the "no longer being harvested" clause is a judgment call
  (spider-bot's extraction ledger is still growing), so the archive stays
  queued R5 work for a session that takes it deliberately — not done in
  passing here.
- ⚑ spider-bot's CI `quality` is informational; making it a required check
  (= a PR flow on a repo whose pushes deploy straight to the live bot) is an
  owner call, recorded in the repo README and the Layer-2 entry.

## Layer-2 handoff

Layer-2 handoff: docs/repos/spider-bot/README.md — created (entry point
built; threads: Phase-0 hardening closed 2026-08-24 · next feature = owner's
pick · plan transplant open).
