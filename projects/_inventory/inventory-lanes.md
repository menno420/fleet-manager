# In-repo inventory — project-package artifacts, active lanes (2026-07-10 ~21:05Z)

Worker inventory for the PROJECT-PACKAGE CENTRALIZATION dispatch. Read-only; all
citations are `path @ <origin/main HEAD sha>` fetched 2026-07-10 ~21:00Z.

HEAD SHAs at inventory time:
- substrate-kit `f0e6c85fbd30f5219263af0dffab0c2287da7aac`
- websites `4056909fcba3840302269700de6c1fe14200e796`
- trading-strategy `0e713b9eebcb1a06e6d2d7be5c337092114b9c7b`
- venture-lab `ce223152719705e22a386b6fdc6d03508a0661c1`
- superbot-next `9757755c61034edad4b5dee5ab715783da18f1a6`
- superbot-games `4493292bc6e7a080d3d73f59f763c0db89b1c0af`

Classification keys:
- TYPE: worker-instructions / seat-prompt / setup-script / failsafe-text / working-agreement / boot-brief / deploy-record
- Q-0265 test: any "one bounded slice per wake" pacing for a production seat = OUTDATED.
- Q-0264 test: idea escalation via Idea Engine / manager heartbeat present?
- DEPLOYED: a trigger's recorded prompt = deployed; a paste-file with no paste record = unknown.

---

## 1. websites @ 4056909 — THE MODEL. Only repo with a dedicated package dir; all four parts present in some form.

| Artifact | TYPE | Q-0265/Q-0264 | DEPLOYED |
|---|---|---|---|
| `docs/project/README.md` | package index ("source of truth is repo; re-paste into console") | — | convention doc |
| `docs/project/project-instructions.md` | worker-instructions (Custom Instructions paste file, <7,000-char console budget) | Q-0264 YES (ladder rung 3: Idea Engine harvests docs/ideas/ by link, sim-worthy → manager heartbeat). Q-0265 **PARTIAL DRIFT**: its § "ROUTINE-FIRED SESSION protocol" still says "execute ONE bounded slice, not a marathon" — v2 prompt superseded the pacing but this section was not updated | UNKNOWN — paste convention; card `.sessions/2026-07-10-q0265-routine-prompt-v2.md` ends with "Owner action…: re-paste both into the console" (no paste record) |
| `docs/project/routine-prompt.md` | seat-prompt, **v2 continuous mode** (work loop up ladder, ~15-min send_later pacemaker, cron as failsafe fallback, backpressure brake, free-window posture, Q-0264 escalation). v1 kept verbatim as history | **CURRENT** (explicitly Q-0265 + Q-0264) | **NOT the deployed text.** Live trigger `trig_017H9Qb9oxtLgUy6sw2gnSHg` (cron `0 */4 * * *`, fresh-session-per-fire) carries "the standing inbox ritual" delegating prompt — `docs/owner/OWNER-ACTIONS.md` row E. Deployed prompt is therefore v1-era → deployed-state OUTDATED vs repo v2 |
| `docs/project/setup-script.sh` | setup-script (fail-soft, `set +e`, capability probe: signing / ls-remote / dry-run push / MCP toolset; PR #47 provisioning-death lesson) | current mechanically | paste convention; unknown if pasted |
| `scripts/setup-env.sh` + `scripts/env-setup.sh` (wrapper) | setup-script, SECOND lineage — the gen-2 wind-down env script + a path-compat wrapper for the "pinned-research environment archetype" hook path | current | unknown |
| `.claude/CLAUDE.md` == `.substrate/claude/CLAUDE.md` (byte-identical) | working-agreement (kit-planted, binding, guided adoption) | pre-dates Q-0264/Q-0265 (generic) | in-repo = active for CC sessions |
| `docs/succession/proposed-custom-instructions-2026-07-09.md`, `docs/succession/next-boot-2026-07-09.md` | worker-instructions proposal + boot-brief, gen-1→2 | OUTDATED — superseded by docs/project/ | historical |
| `docs/owner/OWNER-ACTIONS.md` row E | deploy-record — self-armed trigger confirmed, first fire 2026-07-10T16:01:32Z | — | the de-facto failsafe cron record |

Missing for websites: (a) verbatim committed text of the DEPLOYED trigger prompt
(only paraphrased "standing inbox ritual"); (b) Q-0265 fix to
project-instructions § ROUTINE-FIRED; (c) a distinct failsafe-text file (v2
prompt embeds failsafe semantics but the cron's own prompt is uncommitted);
(d) resolution of the dual setup-script lineage (docs/project/setup-script.sh
vs scripts/setup-env.sh — which field does the console actually hold?).

---

## 2. substrate-kit @ f0e6c85 — richest instruction corpus + the kit templates; no committed seat-prompt text.

| Artifact | TYPE | Q-0265/Q-0264 | DEPLOYED |
|---|---|---|---|
| `docs/gen2/setup.sh` (OA8) | setup-script (fail-soft, exit-0 contract, repo-locate; companion prose `docs/gen2/environment-setup.md`, `docs/environment-setup-script.md`) | current mechanically | owner-paste; no paste record |
| `docs/gen2/custom-instructions-proposal.md` | worker-instructions, full paste-ready kit-lab text (BOOT / RITUAL 1–6 / AUTHORITY / WALLS / WORKERS + K/D/A table vs blueprint) | **OUTDATED vs Q-0265** — session-ritual shaped, no continuous loop, no send_later pacemaker, no Q-0264 line | UNKNOWN — no in-repo record it was ever pasted |
| `docs/gen2/next-boot.md` | boot-brief functioning as seat boot prompt (§0 resume priorities, non-derivable context; ROUTINE-STATE pointer carries superseded-note per PR #128) | pre-Q-0265 | n/a |
| `control/status.md` lines 7–24 | deploy-record: live trigger `trig_016EfUawz6KxEYqUM6f1BqDw` "substrate-kit 2-hourly standing wake", cron `0 */2 * * *`, created 2026-07-10T15:53:36Z via meta_mcp, persist_session, bound coordinator session, first fire ~16:01:56Z. Prior hourly `trig_01FnqnAQjLU2T8d16iHwWQ2h` (ORDER 010) DELETED | **UNKNOWN vs Q-0265** — status says "stored wake prompt matched the coordinator's spec character-for-character" but the spec text is NOT committed anywhere at HEAD | DEPLOYED (verified via list_triggers) |
| `control/inbox.md` ORDER 010 (line 59) | seat-prompt fragment: dispatched delegating prompt 'Read control/inbox.md at HEAD and run the standing ritual from your instructions.' | OUTDATED (superseded by the 2-hourly cutover) | historical |
| `docs/succession/{custom-instructions-proposal,next-boot-2026-07-09,environment-spec}-superbot-coordinator.md` | full seat package for the SUPERBOT coordinator, homed in the KIT repo (cross-repo homing anomaly) | pre-Q-0265 | proposals |
| `src/engine/templates/` | kit-shipped templates: `CLAUDE.md.tmpl` (working agreement), `CONSTITUTION.md.tmpl`, `collaboration-model.md.tmpl`, `control-{README,inbox,status}.md.tmpl`, `CAPABILITIES.md.tmpl`, `question-router.md.tmpl`, `AGENT_ORIENTATION.md.tmpl`, + doctrine docs | overlaps ONLY part 1 (worker-instructions/working-agreement). **No setup-script template, no seat-prompt/routine-prompt template, no failsafe-text template** | template source |

Missing for substrate-kit: committed verbatim wake prompt (the live trigger's
text exists only in a dead chat); Q-0265-mode seat prompt; failsafe-text;
Custom-Instructions deploy record; kit templates for 3 of the 4 package parts.

---

## 3. trading-strategy @ 0e713b9 — deployed clock + fleet-synced setup script; instructions only as proposal.

| Artifact | TYPE | Q-0265/Q-0264 | DEPLOYED |
|---|---|---|---|
| `environments/setup-universal.sh` | setup-script — adopted VERBATIM from fleet canonical `fleet-manager environments/templates/setup-universal.sh` (blob 6b4459b), synced 2026-07-09; header says "Owner pastes this into claude.ai/code → Environments" | current mechanically | paste convention; wind-down review notes "whether the env setup script was ever fixed owner-side is still unverified from inside (⚑ open)" |
| `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md` | worker-instructions proposal (KEEP/DROP/ADD 1–8 + blueprint-aligned ADD-9/10) | **OUTDATED vs Q-0265** (no continuous mode, no Q-0264) | proposal only. **Honest caveat committed in-file: "the exact gen-1 Custom Instructions text is not visible from the repo."** The fleet-manager "Deployed fitted version" claim has NO in-repo evidence here — the deployed text/record must live in fleet-manager |
| `docs/succession/NEXT-BOOT.md` | boot-brief (read order, walking skeleton, verbatim known walls, and the SCHEDULING RECIPE line: create_trigger cron `0 */4 * * *`, send_later liveness) | pre-Q-0265 | n/a |
| `control/status.md` line 6 | deploy-record: "routine state: ARMED AND RECURRING — trigger `trig_01Mvn5xRmqGmZJNRHgjqyLpN`, cron `0 */4 * * *`, confirmed fires through 12:00Z 2026-07-10" | — | DEPLOYED |
| `control/inbox.md` ORDER 006 (line 64–66) | seat-prompt (de-facto deployed): the dispatched prompt 'Read control/inbox.md at HEAD and run the standing ritual from your instructions.' — the .sessions/2026-07-10-order-006-wake-doc.md card confirms the trigger was armed at boot per this order's spec | **OUTDATED vs Q-0265** — 4-hourly delegating wake, ritual bounded per-wake; no continuous loop, no Q-0264 | DEPLOYED (best in-repo evidence of the live prompt) |
| `.substrate/claude/CLAUDE.md` (no root `.claude/`) | working-agreement (kit-planted) | generic | in-repo |

Missing for trading: in-repo Custom-Instructions paste file (proposal only) and
any deploy record for it; Q-0265 continuous seat prompt; failsafe-text;
`.claude/CLAUDE.md` at the harness-read path (only `.substrate/claude/` copy).

---

## 4. venture-lab @ ce22315 — thinnest lane: working agreement only; clockless; orders pending.

| Artifact | TYPE | Q-0265/Q-0264 | DEPLOYED |
|---|---|---|---|
| `.substrate/claude/CLAUDE.md` (no root `.claude/`) | working-agreement (kit-planted) | generic | in-repo |
| `docs/CAPABILITIES.md` **and** `docs/capabilities.md` | DUPLICATE capability ledgers (kit-generated vs fleet-manifest copy carried at seed) — case-collision drift risk | — | — |
| `control/inbox.md` ORDER 002 (status: new) | seat-prompt fragment: self-arm HOURLY wake, prompt 'Read control/inbox.md at HEAD and run the standing ritual from your instructions.' | pre-Q-0265 dispatched text; **UNEXECUTED** — no routine record anywhere in `control/status.md` | NOT DEPLOYED (repo is clockless) |
| `control/inbox.md` ORDER 004 (status: new) | orders the gen-2 archive ender incl. a next-boot brief | UNEXECUTED — the only non-main branch `manager/order-004-gen2-archive-ender` contains just the kit v1.7.0 upgrade, no next-boot | — |
| `candidates/template-packs/pack/CLAUDE.md.template` | product artifact (sellable pack), NOT lane instructions — do not confuse | — | — |

Missing for venture-lab: ALL FOUR package parts effectively — no
custom-instructions file, no seat/routine prompt, no setup script anywhere, no
failsafe text, no boot brief, routine not armed (ORDER 002 pending).

---

## 5. superbot-next @ 9757755 — most CURRENT deployed state (Q-0265 cutover executed + recorded verbatim); weakest on paste files.

| Artifact | TYPE | Q-0265/Q-0264 | DEPLOYED |
|---|---|---|---|
| `control/status.md` lines 11–14 | **failsafe-text + deploy-record, CURRENT**: ORDER 008 record "AMENDED by owner directive Q-0265 (CONTINUOUS-MODE AMENDMENT)". Old builder-wake `trig_01VYZQ7GHxYq3ecSw8UNZek8` DELETED; failsafe `trig_01L5JBefGSCM1fUdwm4SRQnY` "Builder failsafe wake" cron `0 */2 * * *` into persistent session with prompt committed VERBATIM: "FAILSAFE WAKE (Builder, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending." Continuation chain = one-shot create_trigger links (first `trig_01KedTiCKYMbB3oaNZL5rHmf`), re-armed each turn | **CURRENT (Q-0265)**; Q-0264/Q-0265 also referenced in `control/README.md` + `docs/collaboration-model.md` — the only repo besides websites carrying them | DEPLOYED + verified via list_triggers |
| `control/inbox.md` ORDER 008 (line 47) | seat-prompt (old): full 2-hourly Builder wake instruction text ("ship something real every wake… re-arm +120 minutes") | OUTDATED — superseded by the Q-0265 cutover above | historical (was deployed) |
| `.substrate/claude/CLAUDE.md` (no root `.claude/`) | working-agreement (kit-planted) | generic | in-repo |
| `docs/status/README-first.md` | boot-brief fragment ("how to read this repo's red" — golden-parity born-red) | current | n/a |
| `docs/retro/{self,project}-review-2026-07-09.md`, `docs/retro/QUESTIONS.md` | retro inputs to an instructions rewrite | — | — |

Missing for superbot-next: NO custom-instructions paste file at all (no
succession/ proposal either); NO setup script anywhere; the continuous-mode
WORK-LOOP prompt itself (what the chain links say beyond the failsafe) is not
committed as a canonical file — the failsafe text in status.md is the only
verbatim prompt. The most current lane is also the least packaged.

---

## 6. superbot-games @ 4493292 — two-lane artifacts, inconsistent homes; clockless (ORDER 002 pending).

| Artifact | TYPE | Q-0265/Q-0264 | DEPLOYED |
|---|---|---|---|
| `docs/gen2-custom-instructions-exploration.md` (repo root of docs/) | worker-instructions proposal, exploration lane. KEY EVIDENCE LINE: "Sources: the deployed gen-1 text (fleet-manager `docs/prompts/game-exploration.md`, read verbatim this session)" — proof deployed Custom Instructions live in FLEET-MANAGER, not lane repos | pre-Q-0265, no Q-0264 | proposal |
| `docs/retro/proposed-custom-instructions-mining-2026-07-09.md` | worker-instructions proposal, mining lane (KEEP/DROP/ADD; blueprint not readable that session) | pre-Q-0265 | proposal |
| `docs/retro/next-boot-mining-2026-07-09.md` | boot-brief, mining (10-min read order + walking skeleton) | pre-Q-0265 | n/a |
| `environment/setup-exploration.sh` + `environments/setup-mining.sh` | TWO per-lane setup-scripts in INCONSISTENT dirs (`environment/` singular vs `environments/` plural); both fail-soft exit-0, both mirror the fleet template pattern | current mechanically | paste convention; unknown |
| `control/inbox.md` ORDER 002 (line 36, status: new, 2026-07-10T15:52Z) | seat-prompt fragment: self-arm HOURLY Class-A wake, prompt 'Read control/inbox.md at HEAD and run the standing ritual from your instructions.'; explicitly SUPERSEDES the stale "owner creates the routine" asks in the status files | pre-Q-0265 dispatched text; **UNEXECUTED** | NOT DEPLOYED — `control/status.md`: "routine: NOT ARMED"; `control/status-exploration.md`: "routine: not armed"; `control/status-mining.md`: "routine: NOT ARMED — 'No such tool available: mcp__claude-code-remote__send_later'" (verbatim wall). Repo is clockless |
| `control/{inbox,status}-{exploration,mining}.md`, `control/README.md` | per-lane control bus (one-writer-per-file extension) | — | active convention |
| `.substrate/claude/CLAUDE.md` (no root `.claude/`) | working-agreement (kit-planted, merged-lane) | generic | in-repo |

Missing for superbot-games: armed routine (ORDER 002 pending); a unified (or
per-lane current) instructions paste file — both proposals are pre-Q-0265;
failsafe text; single canonical setup-script location; deployed-instructions
record in-repo (it points to fleet-manager instead).

---

## Cross-cutting findings

1. **websites `docs/project/` is the only instance of the package pattern**
   (README + setup-script.sh + project-instructions.md + routine-prompt.md,
   with the "repo file is source of truth, re-paste after edit" convention and
   the v1/v2 prompt-history convention). Everything else is scattered across
   `docs/gen2/`, `docs/succession/`, `docs/retro/`, `environments?/`,
   `control/status.md` records, and inbox ORDER text.
2. **Deployed Custom Instructions are essentially never in lane repos.**
   Direct evidence: superbot-games proposal cites fleet-manager
   `docs/prompts/game-exploration.md` as "the deployed gen-1 text";
   trading's wind-down review states the deployed text "is not visible from
   the repo"; substrate-kit's proposal carries the same honesty note. The
   "Deployed fitted version" records the fleet-manager status mentions are
   NOT in the lane repos — websites is the sole partial exception (paste
   files + OWNER-ACTIONS trigger record, but still no "was pasted on <date>"
   receipt).
3. **De-facto deployed seat prompts live in three places**: (a) trigger
   records in `control/status.md` (kit, trading, superbot-next, websites
   OWNER-ACTIONS), (b) the inbox ORDER text that dispatched the arm (the
   one-line delegating prompt, 4 repos), (c) websites' dedicated
   routine-prompt.md. Only superbot-next's failsafe and websites' v2 are
   committed verbatim AND current.
4. **Q-0265 scorecard**: superbot-next deployed-CURRENT (continuous cutover
   executed); websites repo-CURRENT but deployed-prompt stale (4-hourly
   delegating trigger) + one internal contradiction (project-instructions
   § ROUTINE-FIRED "ONE bounded slice"); substrate-kit deployed-UNKNOWN
   (prompt text uncommitted); trading deployed-OUTDATED (4-hourly bounded
   ritual); venture-lab and superbot-games NOT DEPLOYED (self-arm orders
   pending, clockless).
5. **Q-0264 scorecard**: present only in websites (project-instructions rung 3
   + v2 prompt) and superbot-next (control/README.md, collaboration-model.md).
   Absent from kit, trading, venture-lab, games instruction artifacts.
6. **Setup scripts**: three lineages — fleet canonical setup-universal.sh
   (trading verbatim; games mirrors the pattern), bespoke probe scripts
   (websites docs/project/setup-script.sh, kit docs/gen2/setup.sh), and the
   websites scripts/setup-env.sh + env-setup.sh archetype-path pair. Homes are
   inconsistent: `environments/`, `environment/`, `scripts/`, `docs/project/`,
   `docs/gen2/`. venture-lab and superbot-next have NONE.
7. **The kit ships templates for only 1 of the 4 package parts**
   (working-agreement/instructions family: CLAUDE.md.tmpl + control-bus +
   CAPABILITIES + doctrine). No setup-script, seat-prompt, or failsafe-text
   templates exist in `src/engine/templates/` — a concrete kit gap for the
   centralization job.
8. **Homing anomalies to fix during centralization**: superbot COORDINATOR
   seat package lives inside substrate-kit (`docs/succession/*-superbot-
   coordinator.md`); venture-lab has duplicate `CAPABILITIES.md`/
   `capabilities.md`; trading/venture/next/games plant the working agreement
   only under `.substrate/claude/` with no root `.claude/CLAUDE.md`, while
   websites keeps byte-identical copies at both paths.

## Missing-parts matrix (four-part package: instructions / seat-prompt / setup-script / failsafe-text)

| Repo | worker-instructions | seat-prompt | setup-script | failsafe-text |
|---|---|---|---|---|
| websites | ✅ paste file (Q-0264; one stale § vs Q-0265) | ✅ v2 file CURRENT; deployed trigger still on old delegating prompt | ✅ ×2 lineages (needs one canonical) | ◐ semantics inside v2 prompt; cron's own prompt uncommitted |
| substrate-kit | ◐ proposal only, pre-Q-0265 | ❌ live 2-hourly trigger's prompt uncommitted | ✅ docs/gen2/setup.sh | ❌ |
| trading-strategy | ◐ proposal only, pre-Q-0265; deployed text not in repo | ◐ deployed = ORDER-006 one-liner, OUTDATED vs Q-0265 | ✅ environments/setup-universal.sh (fleet-synced) | ❌ |
| venture-lab | ❌ (working agreement only) | ❌ (ORDER 002 unexecuted, clockless) | ❌ | ❌ |
| superbot-next | ❌ no paste file at all | ◐ old ORDER-008 text superseded; continuous work-loop prompt not canonized | ❌ | ✅ verbatim + deployed (status.md, Q-0265) |
| superbot-games | ◐ two pre-Q-0265 lane proposals; deployed text lives in fleet-manager | ❌ (ORDER 002 unexecuted, clockless) | ✅ ×2 lanes, inconsistent dirs | ❌ |
