# Session — fm-remove-winddown-current-state

> **Status:** `complete`

**Branch:** `claude/fleet-manager-orientation-oh2tgz`

📊 Model: Opus 4.8 · medium · docs-only

**About to do:** Owner (live chat) asked why the 2-day-old EAP wind-down still reads as current
state, and to remove all mention of it. Scope confirmed with the owner: **live orientation
surfaces only** — strip the wind-down/EAP-cutover framing from the docs a fresh session boots
from, while leaving dated session logs, retrospectives, and findings intact as history. This card
holds the PR red (HOLD) until the edits land, checks stay green, and the enders are filled — then
flips `complete` last.

**Did:**
- **Removed the wind-down/EAP-cutover framing from the live orientation surfaces**, keeping every
  file's structure and its intra-repo links valid (checked live):
  - **`docs/current-state.md`** — rewrote the Stability-baseline callout and the "Current state"
    section to state plainly that the seat is live and the loop runs (dropped the
    "recreated / supersedes the EAP wind-down retirement / read-only 2026-07-21" narration);
    removed "the wind-down had torn down" from the wake-chain bullet; de-framed the apparatus
    bullet and owner-facing-sources line; neutralized the wind-down/EAP wording in the
    "Recently shipped" changelog entries (kept the dated entries + their links); removed the
    pure-narrative "Recreation ruling recorded" changelog line.
  - **`docs/NEXT-TASKS.md`** — dropped the "created by the EAP wind-down / recreation window"
    header, Context, and "do before 2026-07-21" framing; kept the **item numbers stable** (other
    docs reference item 3 / item 5) — item 2 reframed from "EAP project-recreation sweep" to a
    neutral trigger-registry hygiene sweep, item 3 from "wind-down scope" to "sizing scope".
  - **`docs/owner-queue.md`** — removed the wind-down Context section and the "Slimmed … EAP
    wind-down cleanup" header framing; retitled "Superseded by the EAP wind-down" → "Closed /
    no action — ids kept" and de-framed its bullets (all `OQ-` ids preserved); cleaned scattered
    "recreated / post-wind-down / 2026-07-21 / Gmail EAP thread" phrasings in active items. Dated
    "Resolved" log sections left as history.
  - **`docs/RESUME.md`** — dropped the "EAP is extended to 2026-07-21" current-state line and the
    ORDER-046 EAP-extension annotation; retitled §6 "Older reference (EAP finale…)" → "(archived
    program docs)" (links kept).
  - **`docs/AGENT_ORIENTATION.md`** — softened the RESUME.md description (dropped "after the
    2026-07 hiatus" + "EAP finale artifacts").
  - **`README.md`** — neutralized the "EAP program-narrative corpus" framing and removed the block
    of 7 EAP-history rows from the front-door Map (docs stay on disk, now surfaced via a new
    `docs/evidence-index.md` row); root README is not link-checked, so no dead-link risk.
  - **`control/status.md`** — replaced the "RETIRED … EAP wind-down … read-only 2026-07-21 …
    recreation ruling" banner with a neutral "historical scaffolding / under sizing review /
    wake chain armed" banner; retitled the 2026-07-17 session-log heading off "wind-down
    housekeeping". Dated session-log + "Historical — preserved" sections left as history.
- **Left `docs/roster.md` untouched (flagged, not hand-edited):** its wind-down phrases come from
  each sibling repo's `control/status*.md` heartbeat (one-writer rule — not this repo's to edit)
  and it regenerates ~2-hourly from `scripts/gen_roster.py`, so a hand-edit would be overwritten.
  The generator injects no wind-down boilerplate of its own (verified). Durable removal there
  needs the sibling heartbeats to move.
- **Left dated history untouched by design** (owner-confirmed scope): the `.sessions/*` logs,
  `docs/eap-*.md` retrospectives/story/audits, findings, and the owner-queue "Resolved" log record
  a real past event and stay as archived history.
- **Checks green:** `check_docs_links.py` CLEAN (257 files, no dead link introduced) ·
  `check_owner_queue.py` CLEAN (slugs intact; the 2 cross-repo `NOT MEASURED` notes are
  pre-existing 403 probes, not from this diff) · `tools/check_no_false_walls.py` CLEAN ·
  `bootstrap.py check --strict` passed. Guard-fire delta committed with the session, not reverted.

⚑ Self-initiated: None — directed deliverable (owner live-chat request to remove the wind-down
framing from current-state surfaces). No autonomous idea promotion; no trigger created, modified,
fired, or deleted; no sibling repo touched.

💡 Session idea: **A `check_stale_framing.py` advisory checker** that flags when a dated,
time-boxed narrative (a named event + a hard date, e.g. an "X goes read-only YYYY-MM-DD" clause)
still sits in a `living-ledger` boot/current-state doc past that date — so a superseded posture
can't keep reading as current through N sessions the way this one did. Advisory only, stdlib-only,
sibling to the S3/S5/S9 trio; distinct from them (they age register verdicts / wall findings /
cited SHAs — this ages an embedded dated-event clause against wall-clock).

⟲ Previous-session review: **the fm-current-state-refresh card (PR #300)** tried to fix exactly
this two days ago, but only *reframed* the wind-down as "historical context, superseded by the
recreation ruling" — it kept narrating the wind-down in every section, which is precisely what the
owner reacted to today. Lesson: when a posture is genuinely over, **delete the framing, don't
re-explain it** — a "this is now historical" preface still puts the dead narrative on the live
surface. This session removed the framing rather than annotating it.
