# EAP final-day recon + closeout fan-out record (2026-07-14)

> **Status:** `audit`
>
> The fleet-manager record of the EAP final-day closeout (owner directive
> 2026-07-14, coordinator-relayed; fm PR #193). Part 1 — the read-only lane
> recon (window 2026-07-14T09:20–09:27Z, per-lane scratch reports; every
> heartbeat/ORDER/PR state cited from the lane's live origin/main or the
> GitHub MCP with the ~25-min staleness caveat noted). Part 2 — the 13-lane
> ORDER fan-out and its terminal states, **re-verified at live GitHub
> ground truth 2026-07-14T09:51–09:53Z** (`git fetch` + merge-commit
> committer times; MCP `pull_request_read` for the two open PRs). Findings
> at the end. Companion tracker: [EAP audit collection](eap-audit-collection.md);
> dispatch rows also in [`docs/dispatch-log.md`](dispatch-log.md).

## Part 1+2 — one row per lane

Heartbeat age is at recon time (~09:20–09:27Z). "Completable today" is the
recon's cited unfinished-work list — it became each lane's closeout ORDER
item (a). Final state re-verified live 09:51–09:53Z.

| Lane | Heartbeat age at recon | Unfinished — completable today (recon-cited) | Parked / blocked (why) | ORDER | Dispatch PR | Final state |
|---|---|---|---|---|---|---|
| superbot (hub) | ~15.3 h (`updated: 2026-07-13T18:00Z`; predates ORDERs 003–005) | 9 items: ORDER 003 doc lane (stale live-Schedule refs) · ORDER 005 supersession stubs · ORDER 004 ack/heartbeat · reconciliation-consistency guard · casino trio V022/V025/V029 · BTD6 slice · S4 trim ratchet · S2 counter lists · walkthrough (+email-3 owner assist) | #2058/#2061 owner deploy-hold (Q-0193) · email-3 SEND is owner-only · ORDER 003 console click owner-confirming · recon-at-#2100 routine-only (Q-0124) | 006 | #2096 | **MERGED** 2026-07-14T09:43:33Z (`e7d4d68`) |
| superbot-next | ~1 h 47 m (07:33:51Z) | ORDER 021 (a)+(b) docs truing · casino section BUILD (spec self-published, needed the ORDER) · mining title-equip write slice · curation row 72 · ⚑7 banner strings · #466 shepherd | WP stack #312→#371 owner-click sweep · #392 base-parked · ORDER 020 terminal (plugin-hello #2 merge) · ORDER 001 owner token · DROP-list + anchor-call decisions owner (stamped in the fm owner-queue) | 022 | #469 | **MERGED** 2026-07-14T09:40:52Z (`b0b6763`) — pre-fix, see finding (c) |
| substrate-kit | effective ~25 min (08:58Z entry; header 04:02Z) | nothing agent-buildable ("backlog DRY", 11/11 consumed); conditional: owner clicks #317 → release wave + verify | #317 + #345 `do-not-automerge` owner-ratification parks · grounded-skills window ~07-19 · standing ⚑ owner set | 021 | #367 | **MERGED** 2026-07-14T09:42:31Z |
| websites | ~6.0 h (03:21:07Z; orders line omitted 028/029) | finish ORDER 028 (PR #334 dirty — rebase) · unstick bake PR #330 · heartbeat truing · smoke-crawl re-verify window open · ORDER 025 standing invitation | ORDER 020/021 owner-gated (PAT / Discord-auth Q-0004) · #324 parked-by-design · 7 draft lifeboats owner disposal · 9 ⚑ owner asks | 030 | #335 | **MERGED** 2026-07-14T09:42:25Z |
| venture-lab | ~25 min (08:58:01Z) | ORDER 013 conventions rules 2–3 rewrite (only open ORDER) · telemetry `d1b0208` cherry-pick · orders-line truing | 262 owner publish clicks (16 hard-gated) · photo-pack originals · Ship-It ⚑B/⚑D · Kiln ruling · makerbench forbidden · branch-delete 403 · Friday grading time-gate | 014 | #194 | **MERGED** 2026-07-14T09:42:26Z |
| trading-strategy | ~7.3 h (02:03Z commit) | EAP repo-local audit (never fanned here) · heartbeat re-stamp · round-7 pre-registered plan (ORDER 012 item 4 standing) · walkthrough | R5-C OOS ~2026-09-09 gate · MTF-Bollinger FROZEN · wake-resilience owner click · Friday grading 07-17 time-gate | 015 | #122 | **MERGED** 2026-07-14T09:42:26Z (`0ea6950`) |
| idea-engine | ~4.8 h (04:31:48Z; lagged 16 merges) | heartbeat + orders-line flip (010/011) · claim prune (done lane-side pre-dispatch, #415) · PROPOSAL 063 (pipeline DRY — standing ORDER 003 unmet) · ORDER 011 ack · walkthrough | ⚑ needs-owner 3-item bundle · makerbench owner-verbatim forbidden · ASK 005 awaits fm · ASKs 001–003 on kit lane | 012 | #417 | **MERGED** 2026-07-14T09:42:34Z (`24195f8`) |
| sim-lab | ~30 min (08:55:04Z; ledger lagged V069–V073) | orders done= flip + ledger refresh through V073 · VERDICT 074 on P063 arrival · walkthrough | OA-002 Codex quota owner click · OA-003 review-site deploy · OA-004 tag-push 403 · Codex question step suspended | 008 | #138 | **MERGED** 2026-07-14T09:42:37Z (`d4ff3c8`) |
| superbot-idle | ~15.7 h (17:43Z 07-13; INC-17 class — its ORDER 008 re-stamp unstarted at recon) | ORDER 008 heartbeat re-stamp (only ordered work left) | feltness-floor SIM-REQUEST awaiting fm routing (now routed, see games row) · PRESTIGE 10→25 sim-pinned · timed-events + generator-economy await fleet Q-numbers · OA-003 required-check owner click | 009 | #130 | **MERGED** 2026-07-14T09:42:17Z (`efccd69`) |
| superbot-games | ~15.4 h untouched (top stamp ~47 h; ~35 PRs merged since) | heartbeat re-stamp + `acked=008` · production-grade improvement waves (ORDER 008 (b) standing) | fishing SIM-REQUESTs awaited routing — **routed this dispatch, finding (d)** · exploration band honest-NULL on superbot harness · rung-3 packaging ⚑ · owner-queue trio | 009 | #136 | **MERGED** 2026-07-14T09:42:38Z (`ed2fabb`) |
| superbot-mineverse | ~24 min (09:03:48Z — freshest lane) | nothing ordered remains (0 open PRs, 7/7 ORDERs done); ORDER = confirm-clean + walkthrough | sender-side HMAC (superbot #2058 flip + env vars) owner/bot-lane · six host env vars owner-only · conformance e2e blocked on them · OA-003 carried | 008 | #108 | **MERGED** 2026-07-14T09:44:33Z (`c01c013`) |
| pokemon-mod-lab | ~2 d 12 h (2026-07-11T21:03:45Z; all newer state on parked branches) | mostly honest parking: 27 open PRs, main frozen since 07-12T16:13Z, NO merge automation; ORDER 006 gitignore green-unmerged #57; parked control wave #58–#66/#82 needs merge + triple-007 renumber; walkthrough; audit #84 in flight | whole parked wave owner-sweep ("OPEN PRs STAY OPEN"); self-merge classifier-blocked; owner ⚑: ROM-builds required-check click, concept pick, playtest verdict, stale refs | 009 (collision-safe; 007×3 + 008 ride parked PRs) | #85 | **PARKED GREEN** @ `bbb2361` — substrate-gate + ROM builds both success (09:42:34Z / 09:44:42Z), `mergeable_state: clean`; NOT merged by design (no merge automation; joins the owner-sweep wave) |
| gba-homebrew | effective <1 h (main commit 08:52Z; header stamp stale by design of append-only status) | Tiltstone stack #92←#93←#95←#97 landing/retarget · #85 close-as-superseded disposition · juice.js packaging follow-up · answer the outbox night-ORDER ask (this ORDER answers it) · audit #131 (landed 09:27Z) | Tiltstone stack + #85 are other lanes' claims · owner ⚑: melonDS go/no-go, canonical merge clause, NDS required checks · Gloamline scope-complete owner-gated | 006 (supersedes the never-delivered night ORDER; answers the 22:29Z outbox ask) | #132 | **MERGED** 2026-07-14T09:38:53Z (`f485622`) — pre-fix, see finding (c) |

**Fan-out terminal tally: 13/13 terminal — 12 MERGED + 1 PARKED GREEN
(pokemon-mod-lab #85, by design: the repo has no merge automation).**
All merges landed via each lane's own automation (or the hub's own merge
path for #2096); this seat armed nothing and merged nothing, per rails.

### gba-homebrew ALIVE note

The roster carried gba-homebrew as DARK-but-commits-FRESH; recon verdict is
**ALIVE**: last merge to main ~29 min before recon (`d0290d6`, 08:52:05Z);
audit PR #131 opened 09:21:37Z by a live seat session; failsafe wake
routine `trig_01JD1t7rD5jUCqkJQJaNCi3E` cron `50 */2 * * *` firing on
schedule (12:50Z + 14:50Z fires delivered, control/status.md@d0290d6), with
the auto-merge-enabler live at HEAD (proven server-side on #98–#130).

### DARK-seat dispositions (no ORDER — DARK, clean; recon 09:25–09:27Z)

All four received the external fleet-cleanup-audit merge ~07:07Z today —
the auditor landing, not a lane wake; all four self-report dark/wound-down.

| Seat | Last main commit | Open PRs | Disposition |
|---|---|---|---|
| product-forge | `f7f2dd2` 2026-07-14T07:06:57Z (audit #24) | 0 | DARK, clean — close-out self-reported 2026-07-11; archive-vs-migrate decision parked in fm owner-queue (OQ-CONSOLIDATION-ARCHIVE-FORGE) |
| codetool-lab-opus4.8 | `0e0ec02` 07:07:06Z (audit #23) | 0 | DARK, clean — wind-down complete, dark ≈since 2026-07-10; CI green, v0.2.0 consistent; "a clean archival candidate" (one leftover branch, ref-delete 403 wall) |
| codetool-lab-sonnet5 | `0331176` 07:07:03Z (audit #17) | 0 | DARK, clean — dark since 2026-07-09; 26/26 CI runs green; tags/releases owner-gated, none exist |
| codetool-lab-fable5 | `5b0835b` 07:06:59Z (audit #15) | 0 | DARK, clean — succession/retro pack in place; remaining items owner-only (tag/release/PyPI) + `__pycache__`/.gitignore nit |

## Findings

**(a) ORDER-grammar dash-prefix defect + the one-commit fleet fix.** The
fan-out's ORDER blocks initially failed the kit's `inbox-order-grammar`
enforcer on every gated lane. Root cause, verbatim from the gate-fix
report: "The appended ORDER block wrote its fields as markdown list items
(`- priority:`, `- do:`, `- why:`, `- done-when:`), but the kit's grammar
enforcer matches `ln.lstrip().startswith(field)` with
`ORDER_REQUIRED_FIELDS = (\"priority:\", \"do:\", \"why:\", \"done-when:\")`
(bootstrap.py `_validate_block`) — the `- ` prefix defeats all four
matches. One shared template defect; identical in all 13 lane branches."
Fix: one fixup commit per red branch stripping the leading `- ` in the
appended region only (pure-append preserved; ORDER substance unchanged),
validated locally with each repo's own gate before push — all lanes green,
including substrate-kit's two alias jobs (`legacy-alias-test` /
`legacy-alias-smoke`), which hard-fail whenever `kit-quality` is not
success and were not pre-existing main failures. Residue: three mains now
carry a dash-format ORDER that pre-fix merges let through (superbot-next
ORDER 022, gba-homebrew ORDER 006, plus superbot hub ORDER 006 which has
no gate) — future gates won't re-flag them (grammar runs on newly appended
regions only), but mechanical field parsers should tolerate the `- `
prefix in exactly those three blocks. Lesson for every future control
write: match each file's existing field-line format precedent exactly.

**(b) Dangling fixup commits on merged branches — owner sweep.**
superbot-next `claude/eap-final-closeout` @ `f1f84e7` and gba-homebrew
same-name branch @ `76971ef` were pushed seconds after those PRs
auto-merged pre-fix. Cleanup (branch reset/delete) was DENIED by the
auto-mode classifier ("force-push rewrites remote history"). Harmless — no
open PR references them — but branch deletion or reset to the merged head
needs owner/approved hands.

**(c) Gate-coverage gaps (follow-up candidates, not fixed here).**
superbot-next CI has the grammar code in its bootstrap.py but **no
`--inbox-base` wiring in any workflow** — its inbox gate never ran on
#469, which is why it merged pre-fix. gba-homebrew has the gate step but
it **self-skipped** on #132 (likely merge-base/fetch-depth in its
checkout — its local bootstrap correctly reds the same bytes). Both are
one-workflow-edit fixes for those lanes.

**(d) superbot-games SIM-REQUESTs routed.** The two stranded games
SIM-REQUESTs (`fishing-full-roster-economy`, filed via games PR #92
`21937f3`, + the folded-in `fishing-cook-economy`) — recon-verified
unrouted in both fm and sim-lab — were routed to sim-lab inside its
closeout ORDER 008 this dispatch; the games seat tracks the verdict via
its own ORDER 009 note.

**Owner-actions aggregation.** Each lane's closeout ORDER (b) requires a
per-seat walkthrough (`docs/eap-closeout-walkthrough-2026-07-14.md` —
recon-verified absent in all 13 repos) whose OWNER ACTIONS checklist
surfaces every pending click with a bolded recommendation and VERIFY step.
Owner-actions therefore now aggregate lane-side; the fm owner-queue stays
the cross-fleet dedup surface.
