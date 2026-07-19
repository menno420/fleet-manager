# 2026-07-19 · fm build slice — `emit_routine_claims.py` write-side fence emitter

> **Status:** `complete`

About to happen (declared born-red): the below-the-line "write-side fence emitter"
slice from `docs/planning/2026-07-19-next-slices.md` (baton item 2 of the 10:38Z
heartbeat) — a small stdlib script `scripts/emit_routine_claims.py` that updates the
```json routine-claims``` fence in `control/status.md` from CLI args
(`--failsafe-id/--cron/--next-run/--last-fired/--state`, repeatable `--deleted`,
`--pacemaker-cadence/--pacemaker-note`, `--updated` defaulting to now), so heartbeat
writers stop hand-editing JSON — the drift source the PR #341 review flagged (the
fence's `next_run`/`last_fired` go stale by hand). It validates the result
round-trips through `verify_routine_state.py`'s fence parser before writing,
`--dry-run` prints the new fence, and it refuses (exit 2) on zero or two fences.
Also: one doc index line where `verify_routine_state.py` is indexed
(`docs/playbook.md` R26), a status.md `updated` bump via the emitter itself
(dogfood), claim `control/claims/claude-fm-fence-emitter.md` (deleted in the flip
commit). No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — new write-side tool over a verified parser contract (Q-0105 provenance tier)

## What shipped (PR #357)

- `scripts/emit_routine_claims.py` (Q-0105 provenance header): `locate_fence`
  mirrors the read-side detection rules but keeps line positions, refusing
  (exit 2) on zero fences, multiple fences, or an unclosed fence; `apply_args`
  carries every unspecified field forward in original key order (`--deleted`
  is wholesale-overwrite like the heartbeat itself; a list-shaped `failsafe`
  is refused — CLI edits the single-object shape only); `render` re-emits the
  body as `json.dumps(..., indent=2)` and **round-trips the whole new file
  through `verify_routine_state.parse_fence_claims` before a byte is
  written** — the consumer's parser is the write gate, so the emitter can
  never produce a fence the verifier would exit-2 on. `--dry-run` prints;
  `--updated` defaults to now; `--selfcheck` pins carry-forward, overwrite,
  round-trip refusal (bad state), zero/two/unclosed-fence refusals, and
  list-failsafe refusal. Design note: landed as a standalone script, not an
  `--emit-fence` flag on the verifier — the read tool stays read-only.
- `docs/playbook.md` R26 — one write-side index line next to the
  `verify_routine_state.py` companion-proof line.
- `control/status.md` — fence `updated` → 11:02Z **written by the emitter
  itself (dogfood)**; slice subsection; baton advanced (fence emitter DONE,
  next = `check_capabilities_grammar.py` or a fresh groom); Gates refresh line.

## Demo — dry-run vs the real fence, current values (2026-07-19T11:02Z, verbatim)

Abridged (backtick fence markers elided so this card doesn't itself carry a
second tagged fence):

    fence in control/status.md — changed: updated
    [fence] json routine-claims
    { "seat": "fleet-manager (coordinator)", "updated": "2026-07-19T11:02Z",
      "failsafe": { "id": "trig_01GK4mjoKBP3yCabn9ux1MB2",
        "cron": "30 */2 * * *", "next_run_at": "2026-07-19T10:31:48Z",
        "last_fired": "2026-07-19T08:32:09Z", "state": "armed" },
      "deleted": [ "trig_01Bo7dZxM9xz2hwR36L424Z8" ],
      "pacemaker": { "mode": "send_later", "cadence_minutes": 30, "note": "…" } }
    [/fence]
    DRY-RUN — nothing written.

(passing the exact current values changes ONLY `updated` — carry-forward
proven on the live file; full verbatim output in the PR report.)

**Real run (the dogfood write):** same values, no `--dry-run` → `changed:
updated` → `WROTE control/status.md (round-trip verified against
verify_routine_state.parse_fence_claims).` The 10:31:48Z-window failsafe fire
was **not** bumped into `last_fired`: it is unverifiable from this venue (no
trigger-MCP calls; the committed 10:28:57Z snapshot is pre-fire), so the
volatile fields honestly keep the export truth — exactly the no-invented-fire
rule.

**Post-write verifier (verbatim tail):**
```
claims source: routine-claims fence
export capture instant 2026-07-19T10:28Z (0.6h before now=2026-07-19T11:02Z)
[OK   ] C1 claimed failsafe `trig_01GK4mjoKBP3yCabn9ux1MB2` present + enabled, cron `30 */2 * * *` matches
[OK   ] C3 claimed-DELETED `trig_01Bo7dZxM9xz2hwR36L424Z8` — absent from export
VERDICT: OK — heartbeat routine claims match the export (2 claim(s) verified).
```
`--selfcheck` → `selfcheck: PASS (0 failure(s))`.

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/`, the PR #349 plan doc,
  2026-07-18/19 cards):** **volatile-field drift check in
  `verify_routine_state.py`.** The fence's `next_run_at`/`last_fired` are
  informational to the parser today ("reads id/state/cron and ignores the
  rest"), so the exact staleness the emitter prevents on the write side is
  still invisible on the read side. A small INFO/WARN diff of those fields
  against the export's record for the claimed failsafe id — with capture-lag
  honesty (a NEWER export value is expected progress; only a fence value
  newer than the export, or frozen across multiple captures, warns) — would
  close the loop: write side prevents, read side detects. Distinct from C1
  (id/enabled/cron) and from the dropped `post_capture_deltas` idea (that was
  about capture_notes, not field diffing).
- ⟲ **Previous-session review (PR #355, 10Z records slice):** exemplary
  export-value honesty — it recorded `next 10:31:48Z` with an explicit
  "written at 10:38Z, pre-fire; fence carries the export truth" caveat
  instead of inventing the fire, which is precisely the discipline this
  slice's no-invented-fire rule reused. Miss/improvement it surfaces: #355
  hand-edited those volatile fence fields (the drift source itself — benign
  there, but the class the #341 review flagged); now that the emitter
  exists, heartbeat writers should quote their emitter command line in the
  session card so the write is replayable — adopted in this card.
- **Doc-audit:** durable homes checked — tool rationale + contract in its own
  Q-0105 header/docstring, write-side index line in `docs/playbook.md` R26
  (same home as the read side), facts + baton in `control/status.md`,
  verbatim demo outputs in this card. The plan doc's below-the-line list
  stays dated as written (DONE marks live in the baton, the #352-card rule).
  No chat-only conclusions left unhomed.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed
  (do-not-revert); born-red HOLD was the only red in `bootstrap.py check
  --strict` pre-flip.
- **Claim:** `control/claims/claude-fm-fence-emitter.md` deleted in this flip
  commit.
