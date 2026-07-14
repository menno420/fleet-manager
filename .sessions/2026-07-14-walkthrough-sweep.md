# 2026-07-14 — EAP walkthrough straggler sweep

> **Status:** `in-progress`

📊 Model: Claude Fable (family-level)

about to do: sweep newly-landed EAP closeout walkthroughs (`docs/eap-closeout-walkthrough-2026-07-14.md`) across the 13 target repos at live HEAD and merge their §C owner-action rows into `docs/eap-owner-checklist-2026-07-14.md`, refreshing the UPDATABLE docs (audit-collection walkthrough state, email-draft straggler appendix) to live truth.

Provenance: coordinator baton (control/status.md next-session item 1: "Straggler sweep: as pending walkthroughs land, merge their §C rows into docs/eap-owner-checklist-2026-07-14.md and refresh the UPDATABLE docs"); EAP final-day closeout context per inbox ORDER 045 + docs/eap-final-recon-2026-07-14.md.

## Work record (PR #198; card flip owed to the coordinator, not this session)

- Sweep (~12:02Z, raw@main for the 12 public targets; MCP `get_file_contents` for private pokemon-mod-lab): **8/13 walkthroughs landed** — six NEW beyond the 10:30Z pair (substrate-kit, trading-strategy): superbot-next, venture-lab, superbot-idle, superbot-games, superbot-mineverse, gba-homebrew. Still missing: superbot (hub — ordered via #2096/ORDER 006(b), which MERGED 09:43:33Z; doc not yet on main), websites, idea-engine, sim-lab, pokemon-mod-lab.
- Checklist merge: `docs/eap-owner-checklist-2026-07-14.md` **29 → 41 rows** — 12 new rows (superbot-next 29–32 · venture-lab 33–34 · idle/mineverse 35–36+38 · games 37 · gba 39–40; old row 29 renumbered to 41 and marked merged per live truth ddff49c); dedupe annotations added in place on rows 13, 17, 18, 25 (nds-rom-build · WP stack/plugin-hello/DROP list · #2058/#2061 sequencing detail · R5-C cross-seat flag); header + footer counts refreshed.
- `docs/eap-audit-collection.md`: added the per-repo **walkthrough column** (12:02Z states, all 14 rows); superbot row updated (#2096 MERGED 09:43:33Z); pml row re-verified (PR #84 STILL OPEN, `mergeable_state: clean`, head 6349c6c unchanged at 12:02Z).
- `docs/eap-final-email-draft-2026-07-14.md`: straggler appendix refreshed to 8/13 + live pml/#2096 truth; **no new ANTHROPIC-tagged asks** found in the six new walkthroughs (grep-verified: next's sole hit is the `ANTHROPIC_API_KEY` env-var name; venture's references its audit asks A–E already in the appendix) — appendix table untouched, email body above the COPY marker untouched.
- Claim bullet reformatted to the parseable `check_claims` grammar mid-session (advisory fired on first commit).
- Verification: `python3 bootstrap.py check --strict` — green apart from the DESIGNED born-red hold on this card; `check_roster_freshness.py` OK (0.2h); `check_owner_queue.py` CLEAN; `check_trigger_health.py` PASS 9/9.

💡 Session idea: the walkthrough/audit collection sweeps re-derive the 13-target repo list and per-repo probe method (raw vs MCP-private) from prose each time — a tiny committed manifest (`docs/eap-sweep-targets.yml`: repo · visibility · doc paths) plus a ~30-line prober emitting the landed/missing table would make every future collection sweep one command and kill the risk of a sweep silently dropping a target repo (same regenerate-don't-restate instinct as the roster).

⟲ Previous-session review: the email-rebalance session (PR #196) executed the owner's self-containedness directive cleanly and verified every cited number survived — strong. Its miss (inherited by the 10:30Z sweep): straggler state was recorded in three places (checklist header, email appendix, audit-collection notes) with no single walkthrough-state surface, which this session had to reconcile by adding the audit-collection column. Concrete improvement: keep per-repo landed-state in exactly one table (audit-collection) and let the other two docs point at it — the checklist header and appendix should carry counts only, not repo lists, so the next straggler sweep edits one row instead of three prose blocks.
