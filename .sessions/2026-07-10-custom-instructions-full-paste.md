# 2026-07-10 — owner ruling: Custom Instructions = FULL per-repo paste (UNIVERSAL.md restructure)

> **Status:** `complete`

📊 Model: fable family (worker, coordinator-dispatched) · start 2026-07-10T22:20Z · end 2026-07-10T22:30Z (`date -u`)

## Declared at open (born-red)

Owner ruling (owner chat 2026-07-10 ~22:15Z): "custom instructions should remain
complete per project — they always survive archives, so it's better if they are
always fully there." This retracts the thin-pointer design for the Custom
Instructions field (PR #43's Block 1); the universal pointer survives ONLY as
the wake/start-off prompt. About to land, in this PR:

1. **`projects/UNIVERSAL.md`** — restructure to v2: top OWNER RULING note;
   keep the universal WAKE block (version bumped); replace the old Block-1
   universal-instructions text with a short "Custom Instructions flow" section
   (full per-repo `projects/<repo>/instructions.md` paste, version-stamped;
   edit-registry-first → bump vN → re-paste; drift check = ask the seat to
   quote its version header).
2. **`projects/README.md`** — align the "Universal pointer prompts" section +
   paste-wave wording with the ruling (instructions = full paste; wake =
   universal pointer).
3. **`control/status.md`** — heartbeat line recording the ruling (provenance:
   owner chat 2026-07-10).

## Shipped (close-out)

All three items landed as declared. UNIVERSAL.md is now v2: OWNER RULING note
on top (verbatim intent quoted, provenance owner chat 2026-07-10 ~22:15Z), ONE
universal wake block (v2 header), and a "Custom Instructions flow" section
replacing v1's Block 1 (full per-repo paste, version-stamped;
edit-registry-first → bump vN → re-paste; drift check = seat quotes its version
header; rationale: Custom Instructions survive chat archives). projects/README:
section retitled "Universal wake prompt + Custom Instructions flow" + a
paste-shape note atop the paste wave (instructions = full body paste, wake =
universal block). control/status.md universal-pointer line records the ruling +
v2 restructure. Local `bootstrap.py check --strict` green after card flip.

💡 **Session idea:** add a registry lint (kit gate step or tiny script) that
asserts every `projects/<repo>/instructions.md` starts with a machine-readable
`vN · date` version header — the ruling makes that header the ONLY drift
detector for the Custom Instructions field (seats quote it), so a package that
ships without one is silently un-driftcheckable.

⟲ **Previous-session review:** the universal-pointer worker (PR #43) executed
its dispatch cleanly (byte-exact blocks, raw-URL probe, proper born-red card),
but the design it shipped lived ~15 minutes before the owner retracted half of
it — the archive-survival property of Custom Instructions was knowable in
advance. Workflow improvement: when a dispatch changes WHERE owner-pasted text
lives, the proposal should state each surface's persistence property
(survives archives? survives re-boot? fetch-dependent?) as a one-line table —
that's exactly the axis the owner ruled on, and it would have surfaced the
split (durable field = full text; ephemeral wake = pointer) before the build.
