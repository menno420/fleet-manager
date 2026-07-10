# 2026-07-10 — universal pointer prompts (projects/UNIVERSAL.md)

> **Status:** `complete`

📊 Model: fable family (worker, coordinator-dispatched) · start 2026-07-10T21:58Z · end 2026-07-10T22:06Z (`date -u`)

## Declared at open (born-red)

Worker for the coordinator's universal-pointer-prompts dispatch. About to land,
in this PR:

1. **`projects/UNIVERSAL.md`** — the owner's universal pointer prompts (v1 ·
   2026-07-10): one Custom-Instructions block + one wake block pasted the SAME
   into every Project; the Project's repo attachment tells the session which
   `projects/<repo>/` registry dir is its own, and the session self-locates its
   real package via raw fetches. Edit-registry-first; blocks carry quotable
   version headers.
2. **`projects/README.md`** — a "Universal pointer prompts" section pointing at
   UNIVERSAL.md (why: one paste everywhere; per-repo packages stay canonical;
   public-repo caveat noted).
3. **`control/status.md`** — heartbeat line: UNIVERSAL pointer prompts live at
   `projects/UNIVERSAL.md`.

Sequenced after PR #42 (registry gap closure) per the dispatch; raw-URL sanity
check done pre-branch (websites instructions.md → HTTP 200).

## Shipped (close-out)

All three items above landed as declared. Both fenced blocks verified
byte-for-byte against the dispatch spec (scripted diff — EXACT MATCH ×2).
Raw-URL sanity check: `https://raw.githubusercontent.com/menno420/fleet-manager/
main/projects/websites/instructions.md` → **HTTP 200**. PR #42 was still open
at branch time (per coordinator directive: don't wait), so this PR is based on
origin/main @ 7660be5; update-branch before merge if main moves under it.

💡 **Session idea:** add a tiny CI/link check that fetches each
`projects/<repo>/instructions.md` raw URL referenced by UNIVERSAL.md's pointer
pattern (one HEAD request per registry dir with an `instructions.md`) so a
renamed/removed package or a repo-visibility flip to private is caught in the
gate instead of by a seat's failed boot fetch — the universal blocks make every
seat depend on these URLs resolving.

⟲ **Previous-session review:** the package-registry assembly session
(`2026-07-10-package-registry.md`) shipped a clean, well-provenanced registry,
but it left the "owner must match prompt to Project" friction unaddressed —
exactly the gap this session closes; the workflow improvement it suggests is
that any registry-shaped deliverable should ship its *access pattern* (how
consumers find their entry) in the same pass, not just the content.
