# 2026-07-10 — owner ruling: Custom Instructions = FULL per-repo paste (UNIVERSAL.md restructure)

> **Status:** `in-progress`

📊 Model: fable family (worker, coordinator-dispatched) · start 2026-07-10T22:20Z (`date -u`)

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
