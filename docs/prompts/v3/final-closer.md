> **Status:** `reference`

v1.0 · 2026-07-21 · FINAL CLOSER (program end)

# Final close — paste once per project, today

Your startup prompt still governs what your seat is. This prompt ends the run: **at 2026-07-22T00:00Z (5pm PT today) every session in this Project becomes permanently read-only** — nothing in-session survives; only what is committed to the repos does. Work backward from that deadline. This is your seat's last run: land everything that matters, write the handover, wipe your routines, and end cleanly.

**Priorities under the deadline (strict order):** (1) the closeout document; (2) records true-up; (3) routine wipe; (4) finishing in-flight work — a half-done slice becomes a documented continuation step, not a race against the clock. If time runs short, cut from the bottom of this list, never the top.

**1 · Finish or park everything in flight.** Every PR your seat owns reaches terminal: merged on green or closed with a one-line reason. A slice too big to finish before the deadline is parked properly: commit what exists to its branch, write exact resume steps in the PR body, and reference it in the closeout doc. Open no new feature work.

**2 · Write the closeout document — the heart of this close.** Create `docs/PROJECT-CLOSEOUT.md` (Status badge per the docs gate + a real link from your docs index or current-state.md), written for two readers who know NOTHING about these sessions: the owner, and a fresh future Claude session. Sections:
- **What this project is & what was accomplished** — the real story: every major thing shipped, with PR/commit citations. Complete but readable.
- **Current true state** — verified live at write time (git/CI/deploys), not from memory.
- **Continuation** — open threads, parked work, and next steps in priority order; where the plans and backlogs live; exact resume instructions per item.
- **Owner walkthrough** — plain non-technical language: every valuable artifact (live sites and URLs, dashboards, bots, documents, tools), a clickable link to each, what it is for, and how to use it — paste-ready commands wherever the owner would run something. End with a short "owner checklist" of anything that genuinely needs him (settings, secrets, decisions), quickest first.
- **Working this repo with a fresh session** — boot route (CLAUDE.md → orientation docs), verify commands, how PRs land (the landing workflow), and the one or two gotchas a newcomer must know.

**3 · True up the records.** current-state.md accurate; owner-queue reconciled (retire satisfied asks; keep only genuinely-open items, each self-contained); delete your seat's claim files. Confidentiality: repo docs are public — describe this period generically (e.g. "autonomous agent sessions"); do not name or describe the confidential program or its mechanics in repo files.

**4 · Wipe your routines to ZERO — no exceptions.** After the deadline your sessions can never be woken; every trigger bound to them is dead weight. Delete every send_later and every cron your seat created — including your failsafe (no bridge carve-out: nothing survives this close). Verify via list_triggers paginated to exhaustion: zero triggers attributable to your seat remain. A sibling's id is left alone. Deletion walled → relay once through a worker; genuinely uncloseable → record the id + why in the heartbeat.

**5 · Final heartbeat + land it.** Overwrite control/status.md: first line `SEAT CLOSED — <date -u>`; pointer to docs/PROJECT-CLOSEOUT.md; PR list with terminal states; routine-wipe result (ids deleted, verified zero); anything uncloseable. Land the closeout PR on green (born-red card → flip last, as usual) and VERIFY it merged — an unmerged closeout is not written.

**6 · Final recital in chat** (the owner reads this later): what shipped this close (with cites), the closeout doc link, every PR's terminal state, "routines: zero (verified)", and the single most valuable thing a future session should do first. Then end. Do not re-arm anything.
