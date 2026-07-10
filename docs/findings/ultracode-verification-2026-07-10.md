# Ultracode verification — tonight's three ultracode-class outputs vs. the repos at HEAD

> **Status:** `reference`
>
> Adversarial-verification worker record, **2026-07-10 (~00:45–01:15Z)**.
> Playbook R2 applied to the verifiers themselves: every claim below was
> re-derived from the repos / GitHub / Gmail at HEAD, never taken from the
> reports under review. The three verdict tables are reproduced **verbatim**
> from the verification workers' output files. *(Naming note: the dispatching
> template's date slot rendered as `undefined`; this file substitutes the
> actual date, 2026-07-10.)*

## Executive summary (for the owner — plain language)

Three big "ultracode"-style outputs landed tonight. Independent verification
workers re-checked each one against the actual repositories at HEAD — not
against what the reports say about themselves. Headline: **all three are
genuinely high quality.** Almost every claim reproduced exactly, down to
merge timestamps and line counts. Each one contains exactly one or two small,
concrete errors, all listed below.

1. **Fable's gen-1 grand review (superbot PR #1911)** — verified 18 of 20
   major claims exactly. One claim is wrong: it says parity rows exist for
   all 8 unported subsystems, but **starboard and paragon have no rows** in
   superbot-next's parity dashboard. **Already merged by you** at 00:33:40Z —
   the merge is sound (new files only, no binding docs); the parity-row
   sentence is worth a small follow-up correction.
2. **The harness × model experiment package (fleet-manager PR #15)** —
   verified 13 claims; two minor letter-level inaccuracies ("new files only"
   is strictly false — it also adds 2 navigation lines to
   AGENT_ORIENTATION.md; and the "pre-registered rubric" requirement is
   misattributed to the GPT-5.6 doc). **Already merged.** Two assumptions to
   confirm **before launching the experiment**: that "ultracode" is a real,
   invokable feature (the whole U-arm treatment rests on that one prompt
   line), and that experiment sessions can actually self-merge PRs (the
   classifier wall; direct-to-main sidesteps it).
3. **The fleet wind-down audit (superbot PR #1913, still OPEN)** — verified
   17 of its claims exactly, including all five of its headline
   inaccuracy-findings about other lanes (and yes: fleet-manager's own
   ping-test report wrongly lists websites as "NO ACK" — websites did ack,
   1h39m late, via its PR #44). One error found in the audit itself: sonnet5
   was NOT the "only lane to ship an actual shell script" — five other lanes
   shipped real setup scripts too. **Held: it needs a conflict rebase**
   (current-state.md/telemetry collide with #1911/#1914 which merged after it
   opened) and deserves a one-line correction of that sentence, then merge.

**Environment templates:** both updated archetype scripts land in this PR —
`archetype-pinned-research.sh` (recognizes websites' committed
`scripts/setup-env.sh` hook, git-state triage, GITHUB_TOKEN presence line)
and `archetype-bot-prod.sh` (per-repo CI interpreter pins — superbot →
python3.10, superbot-next → python3.11 — plus a report-only workspace-residue
advisory). Both keep the R15 defensive contract (always exit 0) and tested
clean.

**Merging was permission-blocked in this session** (session wall — no merge
tool may be called), so every merge below is queued for you (or a permitted
session): this PR itself, and superbot #1913 after its rebase.

---

## Verdict 1 — Fable gen-1 grand review (superbot PR #1911) — verbatim

# Verdict — Fable fleet-review ultracode output (superbot PR #1911, gen-1 grand review)

**Target:** menno420/superbot PR #1911 — `docs/eap/gen1-grand-review-2026-07-09.md`,
`docs/eap/gen1-wrapup-email-final-candidate.md`, `docs/eap/README.md`,
`.sessions/2026-07-09-gen1-grand-review.md`, `telemetry/model-usage.jsonl` (1 appended row).
Read at PR head `a26ee413`. **Note:** the task labeled this PR OPEN, but it is **already
MERGED** (2026-07-10T00:33:40Z, merged by menno420). Diff is 804 insertions / 0 deletions —
new files only, no binding-doc edits.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Manifest snapshot at next#97: 41 manifests, 276 commands / 121 settings / 14 events / 45 stores / 96 panels, `stable_hash sha256:40ea3b28…` | VERIFIED | Recomputed from `superbot-next manifest.snapshot.json` at commit `6d95258` (#97 merge): every number reproduces exactly, incl. family counts (mining 37, fishing 20, counting 10, channel 17, blackjack 4, moderation 10, xp 6). Hash on current main differs (`21721a74…`) only because #95 landed after — the report pins it to the #97 point, correctly |
| 2 | 8 whole subsystems missing (utility, ticket, starboard, general, four_twenty, paragon, ux_lab, hermes); "parity rows exist for each in parity/parity.yml" | REFUTED (partially) | All 8 cogs exist in old `superbot/disbot/cogs/` and none in `superbot-next/sb/domain/` — that half is true. But `parity/parity.yml` (49 rows) has **no `starboard` and no `paragon` rows**, and no matching goldens dirs; "parity rows exist for each" is wrong for 2 of 8 |
| 3 | Depth gaps: mining 10,276 lines old vs 732 new; fishing 6,113 vs 566 | VERIFIED | Recounted from both trees at HEAD: old mining .py = 10,276 exactly; old fishing = 6,113; new `sb/domain/mining` = 732; `sb/domain/fishing` = 566. Exact reproduction |
| 4 | Pillow image cards have no named successor — diff overview marks them outstanding | VERIFIED | `superbot-next docs/status/old-vs-new-diff-overview-2026-07-09.md` line 169: "No explicit successor named — outstanding" |
| 5 | Rebuild infra: 465 goldens pinned to superbot @`7f7628e1`; 24 checksum-pinned migrations vs 104; 1,015 `--hash` lines; 62-entry decision ledger; ~1,132 tests | VERIFIED | `parity/parity.yml` pins `sha: 7f7628e12f…`, `goldens: 465` (466 files incl. `_sweep_skips.json`); migrations 0001–0024 + `checksums.json` vs 104 files in `disbot/migrations/`; `requirements.lock` has exactly 1,015 `--hash` lines; `docs/decisions.md` has exactly 62 `## [D-` blocks; #95 PR body: "pytest 1130/2-skipped" ≈ 1,132 collected |
| 6 | `golden-parity` report job red-by-design ("never to be marked required"), gate leg green; fix was orientation — #97 shipped `docs/status/README-first.md` | VERIFIED | `docs/decisions.md` says verbatim "BORN RED BY DESIGN, never to be marked required"; `docs/status/README-first.md` exists on main, shipped by merged #97 |
| 7 | Worldcard Reply-shape bug (AttributeError 'dict' has no attribute 'outcome') found and fixed in next#97 | VERIFIED | next#97 merged 23:45:49Z, commit `6d95258` matches the described bug and fix exactly. Minor nit: report says suite "1,125→1,126 green"; #97's own body says post-fix "1,125 passed / 1 skipped" — off by one, non-material |
| 8 | PR sweep table: #1910 merged 23:18:36Z; next#95 23:52:01Z; next#97 ~23:47Z; games #5=`1eea13a`, #11=`b285df6`, #14=`4c9f889`; kit#49 + #26 merged with `do-not-automerge` label kept; fm#12 23:40:31Z; fm#13 23:37:03Z | VERIFIED | Every timestamp and merge SHA reproduced exactly from GitHub API + git logs (#97 actual: 23:45:49Z, within the "~" tolerance). Kit #49 (merged 00:07:46Z) and #26 (00:12:35Z) both still carry the `do-not-automerge` label |
| 9 | End state: zero open PRs across all six repos except #1911 and superbot #1913 (parallel session, opened 00:07Z) | VERIFIED | Live API check 2026-07-10: superbot-next / superbot-games / substrate-kit / fleet-manager / websites all 0 open; superbot has only #1913 (opened 00:07:13Z; its quoted headline matches its body verbatim). #1911 itself has since merged |
| 10 | superbot merged-PR count: 1,815 at audit time, 1,816 after #1912 (correcting draft v2's "~1,900") | VERIFIED | `search_pull_requests repo:menno420/superbot is:merged` now returns 1,818 with `incomplete_results:false` = 1,816 + #1911 + #1914 (both merged after the audit). Arithmetic reproduces exactly |
| 11 | Gmail ground truth: sent thread `19f41cd2e5380bb3` one message 2026-07-08T15:06:39Z, no reply; Diana Liu broadcast 2026-07-09T22:29:19Z extending EAP "through next Tuesday, 7/14" | VERIFIED | Gmail API: thread has exactly 1 SENT message at 15:06:39Z to claude-code-early-access@anthropic.com; dliu@anthropic.com mail at 22:29:19Z, snippet "will extend the program through next Tuesday, 7/14" — verbatim |
| 12 | Railway: 2 build-failure notify mails 03:46:11Z / 03:47:05Z for the websites dashboard | VERIFIED | Gmail: exactly two `hello@notify.railway.app` "Build failed for superbot-websites" mails at those exact timestamps, Service: dashboard |
| 13 | Email correction 2: 63/100/66 are three *labs* (trading / opus4.8 / fable5), reconciled exactly; sonnet5 arm had nothing to audit | VERIFIED | `docs/eap/fleet-quality-review-2026-07-09.md`: "all three labs' claimed test counts (63/100/66) reconciled *exactly*", with per-lab breakdowns (59+parametrize=63; 21+18+14+17+13+15+2=100) |
| 14 | Email correction 3: kit #74/#75 merged (20:22:31Z / 20:17:11Z), #77 wind-down complete; kit v1.5.0+v1.6.0 released same day; tests 705→722 | VERIFIED | Kit git log: #74 merged 22:22:31+02:00 (=20:22:31Z), #75 22:17:11+02:00 (=20:17:11Z), #77 "WIND-DOWN COMPLETE" on main; CHANGELOG has [1.5.0] and [1.6.0] both 2026-07-09. Test count: 726 `def test_` at HEAD (post-#26/#49) — 722 plausible at the audit point |
| 15 | games#8 merged 2026-07-09T17:06:06Z; ping datapoint 17:54Z dispatch → 19:54:00Z discovery (games#12) | VERIFIED | games git log: #8 merge commit 19:06:06+02:00 = 17:06:06Z exactly; #12 commit text: "Discovered 2026-07-09T19:54:00Z … no session was live between the 17:54Z dispatch and now" |
| 16 | Hub-file staleness: fleet-manifest kit row still "v1.0.0, 637 tests"; next row "no wind-down reaction" is wrong (#87–#94 exist) | VERIFIED | `docs/eap/fleet-manifest.md` line 13: "v1.0.0 released, 637 tests"; line 27: "superbot-next — no wind-down reaction"; superbot-next main has #87 (retro), #92 (project review), #90/#93/#94 — the manifest cell is indeed stale/wrong as claimed |
| 17 | Gen-2 synthesis: blueprint contains §2a measured wake cadences, §2b CI-tier standard (added by fm#12), merge-authority directive; venture-lab = owner-queue item 14 | VERIFIED | `fleet-manager/docs/gen2-blueprint.md` headings "2a. Wake cadence — measured, not asserted", "2b. CI-TIER STANDARD", merge-authority note in header; `docs/owner-queue.md` item 14 = "Launch venture-lab" click-list |
| 18 | Efficiency verdict quote: trading-strategy's "the model-work was efficient; the orchestration layer lost the day" | VERIFIED | Verbatim in `trading-strategy/docs/retro/project-review-2026-07-09.md` §(d) |
| 19 | games CI gap: `substrate-gate` runs no pytest (owner action 8); starboard blocked on a reaction adapter that doesn't exist in the new tree | VERIFIED | `superbot-games/.github/workflows/substrate-gate.yml` runs only `bootstrap.py check --strict` — no pytest step; `superbot-next/sb/adapters/discord/` has message/component/gateway feeds but no reaction feed |
| 20 | Session-process claims: 17 discovery agents, 5 adversarial refuters, ~1.9M subagent tokens; kit #26/#49 merges covered by an owner in-chat review-and-merge authorization | UNVERIFIABLE | Session-side facts (chat transcripts, token counts, an in-chat owner directive) leave no repo evidence to check. The *outcomes* (merges, label retention) are real; the authorization itself can't be independently confirmed |

## Summary (plain language)

I checked the grand-review report the way it claims to have checked everyone else — against the actual repositories, GitHub, and Gmail, not against what it says about itself. It holds up remarkably well: of 20 major claims, 18 verified exactly, down to merge SHAs, second-level timestamps, line counts (mining 10,276 vs 732 reproduced to the digit), the Gmail thread, and even Anthropic's extension email quote. One claim is partly wrong: the report says all 8 unported subsystems have rows in the rebuild's parity dashboard, but two of them (starboard and paragon) have no rows at all — a small error, and ironically the same "stale/overreach" class the report itself hunts for. The session-internal numbers (17 agents, ~1.9M tokens, the owner's in-chat merge authorization) can't be checked from the repos and are marked unverifiable, not wrong. The PR was already merged by the owner before this verification ran, adds only new files, and touches no binding docs, so no action is needed — the one correction worth carrying forward is the starboard/paragon parity-row error, plus a one-off test-count nit (report says #97's suite went to 1,126; the PR's own body says 1,125).

## Disposition

**none** — PR #1911 is already merged (2026-07-10T00:33:40Z, by the owner). Were it still open, the content quality would support merging (new-files-only, no binding-doc edits), with the starboard/paragon parity-row claim flagged as a known small error.

---

## Verdict 2 — harness × model experiment package (fleet-manager PR #15) — verbatim

# Verdict — fleet-manager PR #15 (harness × model experiment package), verified at HEAD ce8e984

Target: `docs/experiments/` package (protocol `harness-x-model-2026-07-09.md`, three pair prompts, `tools/wcag-contrast-check.py`, `README.md`) added by PR #15 (merged 2026-07-10T00:11:47Z).

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | PR body: "New files only (owner-queue/blueprint/playbook untouched)" | REFUTED (minor) | `git diff 7479a65..ce8e984` shows 7 files: 6 new + a **modification of existing `docs/AGENT_ORIENTATION.md`** (+2 nav lines pointing at experiments/README). owner-queue.md, gen2-blueprint.md, playbook.md are indeed untouched, and the edit is a benign navigation pointer — but "new files only" is strictly false. |
| 2 | Package exists at HEAD with all cited files | VERIFIED | `docs/experiments/{README.md, harness-x-model-2026-07-09.md, prompts/pair-{fable,opus,sonnet}.md, tools/wcag-contrast-check.py}` all present at ce8e984; contents match the PR body's description. |
| 3 | Fairness doctrine cited from `docs/findings/gpt-5-6-report-2026-07-09.md`: native harness per arm, fixed budget, artifact-based judging | VERIFIED | Report §(b) "Codex comparison arm": "each vendor's *native* harness … a fixed budget axis (dollars AND wall-clock…) … **artifact-based judging** … rather than self-reported success" (lines 91–99). |
| 4 | Same citation also attributes "rubric pre-registered BEFORE launch" to that doctrine doc | REFUTED (minor misattribution) | Grep of `gpt-5-6-report-2026-07-09.md` for "regist/rubric/before launch" returns nothing; the pre-registration requirement is the experiment package's own (sound) addition, not in the cited report. |
| 5 | Idea provenance: PAIR-OPUS ← `docs/ideas/design-system-lane-2026-07-09.md` (owner-originated, captured); PAIR-SONNET ← `docs/ideas/devlog-building-in-public-2026-07-09.md` | VERIFIED | Both files exist at HEAD with front-matter `state: captured`, `origin: owner`; content matches the brandkit/devlog task specs. |
| 6 | PAIR-FABLE adjacency: game-lab founding package (PR #14) + `docs/findings/gba-toolchain-proof-2026-07-09.md`; PR #14 "confirmed terminal (merged 2026-07-09T23:51:26Z)" | VERIFIED | GitHub API: PR #14 merged=true, merged_at exactly `2026-07-09T23:51:26Z`, before #15's creation (00:02:48Z). Proof doc exists at HEAD. |
| 7 | Toolchain facts: `mgba==0.10.2` pip pin; apt `mgba-sdl` + `binutils-arm-none-eabi` known-good; leseratte10 devkitARM r68 mirror; headless mGBA loop proven | VERIFIED | PyPI: `mgba` 0.10.2 is available (in fact the only published version). `gba-toolchain-proof-2026-07-09.md` records the in-container proof: ~290 fps headless loop, `apt install binutils-arm-none-eabi`, `mgba-sdl` + pip pin ABI note, leseratte10 mirror route (Butano build 17.5s). |
| 8 | `environments/archetype-gba-lab.sh` "landed in PR #14" | VERIFIED | File exists at HEAD; `git log --follow` shows it introduced in commit d54fd9d ("game-lab founding package…"), PR #14's branch. `archetype-python-lab.sh` (the base archetype for all six) also exists. |
| 9 | WCAG judge script: sanity check "black/white → 21.0"; described as the "15-line reference script" | VERIFIED | Ran `python3 docs/experiments/tools/wcag-contrast-check.py '#000000' '#ffffff'` → `21.0000`. Implements the standard WCAG relative-luminance formula (0.2126/0.7152/0.0722, +0.05 offsets). Non-blank/non-comment code lines = exactly 15. |
| 10 | Standards facts: WCAG AA ≥ 4.5:1 normal text; native GBA frame 240×160 | VERIFIED | Both are correct per WCAG 2.x AA and GBA hardware specs. |
| 11 | "Cross-pair protocol (identical text in all three packages)" + ultracode opt-in sentence identical in all three U arms | VERIFIED (with caveat) | Diffed the three blocks: identical except each names its own pair's task shape (explicitly intended) and trivial line-wrapping. The exact sentence "Use ultracode: orchestrate this however you judge best." appears verbatim 2× in each package (protocol + wrapper). |
| 12 | Judge ruff pin: "pre-registered judge version ruff 0.14.0" installable | VERIFIED | PyPI lists ruff 0.14.0 (current latest 0.15.21) — the pin is reproducible. |
| 13 | "Block-4-class ban" (no secrets/env vars in the six repos) is a real fleet concept | VERIFIED | `environments/archetypes.md` line 48 uses the exact phrase ("Block-4-class ban stands: never add Railway IDs / Discord tokens / DSNs / API keys"); Block 4 is the per-repo secrets/setup block in every `environments/archetype-*.sh`. |
| 14 | Landing claim: "card-less routine PR; lands via REST merge-on-green (R21)" | VERIFIED | `docs/playbook.md` line 104: "R21 (2026-07-09) — REST merge-on-green is the PRIMARY landing path on born-red…". PR #15 landed merged-by-owner-account via that path. |
| 15 | Launch checklist division of labor matches documented platform walls (owner creates repos, Projects, environments) | VERIFIED | `docs/capabilities.md` WALLED section: "Creating/editing claude.ai environments, routines, or Projects — no API surface for the agent → owner clicks"; the protocol §4 assigns exactly these to the owner. devkitPro-Cloudflare-403 wall also honored (mirror route used). |
| 16 | Design assumption: "ultracode" is an invokable multi-agent orchestration capability of a Claude Code web session | UNVERIFIABLE | The term appears nowhere in the fleet before this PR (grep across fleet-manager docs) and no platform/capabilities doc attests it. The whole U-arm treatment rests on this opt-in line actually doing something; if it is a no-op, the experiment measures prompt-line placebo. Owner should confirm the feature name before launch. |
| 17 | Wrapper rule "a PR you open AND merge yourself is fine" is achievable by the sessions | UNVERIFIABLE (tension noted) | `docs/capabilities.md` documents a classifier wall: "Direct self-merge of own PRs in established repos — blocked… arming auto-merge while checks are pending is the sanctioned path." Whether the wall fires in fresh empty experiment repos is untested; also GitHub only offers auto-merge when required checks/protections exist, which truly-empty repos won't have. Direct-to-main (also allowed by the wrappers) is the safe path, so the risk is contained. |

## Summary (plain language)

The experiment package is real, complete, and internally consistent at HEAD: every cited file exists, the judge's contrast script really prints 21.0 for black-on-white, the mgba/devkitARM toolchain claims match the earlier in-container proof and PyPI, and the cross-pair "identical text" and landing-rule (R21) claims check out. Two minor letter-level inaccuracies: the PR body says "new files only" but the PR also adds two navigation lines to `docs/AGENT_ORIENTATION.md`, and the "rubric pre-registered before launch" requirement is attributed to the GPT-5.6 doctrine doc, which doesn't actually contain it (it's the package's own, sensible, addition). Two things could not be verified from the repos and matter for the run: whether "ultracode" is a real, invokable orchestration feature (the entire experimental treatment hinges on that one line), and whether experiment sessions can actually self-merge PRs given the documented self-merge classifier wall — direct-to-main commits, which the wrappers permit, sidestep the second issue. The design itself is sound and unusually careful (pre-registration, fake-branch ladder, judge recomputation, no cross-pair aggregation). PR #15 is already merged, so no action is needed; nothing found rises to the level of a correction PR.

---

## Verdict 3 — fleet wind-down audit (superbot PR #1913, OPEN) — verbatim

# Verdict — menno420/superbot PR #1913 (OPEN): "docs(eap): independent fleet wind-down audit (2026-07-09)"

**Identity:** This is tonight's owner-dispatched audit session (branch `claude/code-projects-winddown-audit-6w0r6r`, created 2026-07-10T00:07Z, session card says "Run type: manual (owner-requested audit task)", 32-subagent Workflow-tool pipeline — consistent with an orchestrated/ultracode-style Code Projects session). It is **not** an exploration-project output: its prompt was clearly the fleet wind-down audit, and it delivered exactly that. Telemetry self-reports model Sonnet 5 (unverifiable from repo data). CI on the final head (ad55d458) is fully green (code-quality, CodeQL, flag-conflicts, conflict-guard); mergeable_state is "blocked" only because the required merge hasn't happened.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Fleet-manager's ping-test report lists websites as "NO ACK" with no stated sweep cutoff | VERIFIED | `fleet-manager/docs/findings/ping-test-2026-07-09.md` line 96: `❌ NO ACK … ∞ (>1h at sweep)`; no "as of HH:MM" stamp anywhere in the ack table |
| 2 | websites did ack — PR #44, +1h39m after the order landed | VERIFIED | websites commit `a447514` "control: PING-ACK ORDER 006 + ack ORDER 005 as seen (#44)" at 19:35:58Z; order landed 17:57:05Z → 1h38m53s ≈ 1h39m |
| 3 | substrate-kit ack row re-derivation (order 18:01:34Z #64 after #62 superseded; ack 18:12:39Z #65; 11m05s) | VERIFIED | substrate-kit commits `6951254` (#64, 18:01:34Z) and `208aeb4` (#65, 18:12:39Z) — exact match |
| 4 | opus4.8 heartbeat 18:09:15Z, 15m31s after the ping, acks only 001–003 | VERIFIED | opus4.8 commit `c96318c` (#19) at 18:09:15Z, message "done=001,002,003"; ping landed 17:53:44Z |
| 5 | opus4.8 retro falsely calls `c96318c` "the main tip at wind-down"; 3 more PRs merged after, incl. PR #22 `80f6cd1` ~2h later | VERIFIED | `docs/retro/project-review-final-2026-07-09.md:40` contains the quote; commits #20 (20:06Z), #21 (20:08Z), #22 `80f6cd1` (20:13:54Z) all after 18:09:15Z (+2h05m) |
| 6 | opus4.8 has no "wind-down-review" file; retro lives at `project-review-final-2026-07-09.md` | VERIFIED | Directory listing of `docs/retro/` at HEAD — no wind-down-review file; the named file exists and is a full retro |
| 7 | opus4.8 citation misattribution: exact classifier-denial quotes attributed to the self-review, which only paraphrases them; literal quotes live elsewhere | VERIFIED | Final review header (line 9) attributes build-seat quotes to `self-review-2026-07-09.md`; §3.2's "Exact texts" (e.g. `Permission for this action was denied by the Claude Code auto mode classifier.`) grep-hit only in project-review-final, `GEN2-FEEDBACK.md`, `NEXT-BOOT.md` — NOT in the self-review, which paraphrases |
| 8 | superbot-games "~1.5 hour" wait repeated across four documents; own timestamps compute ~1h55m | VERIFIED | Found in self-review (l.58/141), project-review (l.49/73), project-review-wind-down (l.26/75), gen2-custom-instructions (l.35); PR #3 open 14:47Z → merged 16:42Z = 1h55m |
| 9 | superbot-games status file stamped ~1h after its PR merged; retro flags the drift itself | VERIFIED | Retro §(f): PR #8 merged 17:06:06Z (git), status stamped `updated: 2026-07-09T18:05Z` |
| 10 | substrate-kit "contained same-hour" imprecision — second follow-up PR landed 2h21m later | VERIFIED | Incident PR #22 08:10:21Z; #23 08:27:30Z (same hour); #24 10:31:52Z = +2h21m |
| 11 | sonnet5 misattributes the agent-audit/probe retro item to PR #8; it shipped in PR #7 | VERIFIED | PR #7 `dec6f84` = "retro: full project review — state, agent audit, probe results"; PR #8 `c6128a9` touched only `control/status.md`; winddown-review l.33 credits #8 |
| 12 | sonnet5 differential-testing incident: 3 real parser bugs fixed, exact before/after test count | VERIFIED | PR #11 `0b1eb60` "fix: env parser escape/unicode/hash-value bugs found by differential corpus; 0.1.1" — three bugs enumerated; suite "165+4" matches |
| 13 | sonnet5 is the "only lane to ship an actual shell script (not prose) as its environment deliverable" | **REFUTED** | At least five other lanes shipped real bash scripts in their wind-down packs before this audit ran: opus4.8 `environments/setup.sh` (PR #21, "tested setup script", 20:08Z), websites `scripts/setup-env.sh` (PR #47, 20:21Z), trading-strategy `environments/setup-universal.sh` (PR #9, 20:01Z), fable5 `environments/setup-universal.sh` (PR #12, 20:06Z), superbot-games `environment/setup-exploration.sh` (PR #13, 20:10Z) — all `#!/usr/bin/env bash`, defensive, exit-0 scripts |
| 14 | venture-lab seed: exactly 11 files; status honestly shows ORDER 001 unexecuted; cites a real timestamped source video | VERIFIED | `git ls-files` = 11; `control/status.md`: "orders acked/done: none — ORDER 001 unexecuted"; shortlist cites the YouTube interview with transcript timestamps ([21:02] etc.) |
| 15 | fable5: no baseline instructions file at all; CI has a five-Python-version matrix | VERIFIED | No CLAUDE.md/instructions file at HEAD; `ci.yml` matrix `["3.9","3.10","3.11","3.12","3.13"]` |
| 16 | trading-strategy self-reports failure: PR #12 admits the env fix "never took effect"; 2.8h draft-parked PR; DOA sessions | VERIFIED | PR #12 `79ac6f8` "wind-down amendment: video-lane DOA truth"; "the fix never took effect" verbatim in `control/status.md` + `docs/succession/QUEUE.md`; project-review documents the 2.8h draft gap and the 10s-after-spawn DOA |
| 17 | All 7 lanes shipped complete succession packages; websites incidents (empty PR #19 etc.) real | VERIFIED | Succession/retro packs present at HEAD in all 7 repos; websites `docs/retro/QUESTIONS.md` G2 references the #19 empty-merge incident; full succession set + setup-env.sh + queue-state present |
| 18 | Superbot-internal: previous session card (#1910, eap-email-draft-v2) skips the 💡 and ⟲ sections | VERIFIED | `.sessions/2026-07-09-eap-email-draft-v2.md` exists on main; zero matches for either section |
| 19 | New AGENT_ORIENTATION route facts: superbot = Python 3.10, superbot-next = 3.11 | VERIFIED | superbot CLAUDE.md/CI pin 3.10; superbot-next `ci.yml` pins 3.11 throughout |
| 20 | Method claims: 32 sub-agents, 350 tool calls, artifact link, model "Sonnet 5" | UNVERIFIABLE | Session-side facts; not reproducible from repo data (the report itself marks the artifact as convenience-only) |

**Summary for the owner:** This PR really is tonight's owner-dispatched wind-down-audit session, and the audit it delivered is genuinely excellent — I re-derived its evidence independently and nearly everything checks out to the second. Its headline findings all reproduce exactly: websites truly did acknowledge the ping test 1h39m late (PR #44), so fleet-manager's "NO ACK" row is wrong just as the audit says; the opus4.8 "main tip" error, the superbot-games 1.5h-vs-1h55m drift, the substrate-kit "same-hour" imprecision, the sonnet5 PR #7/#8 mix-up, and the quote misattribution are all real and precisely stated. I found exactly one error in the audit itself: it credits sonnet5 as the "only lane to ship an actual shell script" as its environment deliverable, but five other lanes also shipped real setup scripts in their wind-down packs. The PR only inserts content (new files plus pure additions to living docs — the ledger, the orientation router, an idea marked implemented, one telemetry row); it touches no binding doc, and CI is green on the final head. Recommendation: merge-worthy after (or with) a one-line correction of that single sentence — flagged as leave-open-comment only because of that one refuted detail.

---

## PR-disposition record

| Repo | PR | Link | State | Notes |
|---|---|---|---|---|
| menno420/superbot | #1911 | <https://github.com/menno420/superbot/pull/1911> | **merged** (no action) | Merged by the owner 2026-07-10T00:33:40Z, before verification completed. Content 18/20 verified; follow-up worth queueing: correct the "parity rows exist for each" sentence (starboard/paragon have none). |
| menno420/fleet-manager | #15 | <https://github.com/menno420/fleet-manager/pull/15> | **merged** (no action) | Merged 2026-07-10T00:11:47Z. 13/17 verified, 2 minor letter-level inaccuracies; two pre-launch assumptions for the owner to confirm (see flags). |
| menno420/superbot | #1913 | <https://github.com/menno420/superbot/pull/1913> | **commented / blocked on conflicts** | Verification comment posted. `mergeable_state: dirty` — current-state.md/telemetry conflict with #1911/#1914 which merged after it opened; card already flipped complete. Needs a rebase/conflict resolution + a one-line correction (sonnet5 "only shell script" sentence), then owner merge. |
| menno420/fleet-manager | #16 (this PR) | <https://github.com/menno420/fleet-manager/pull/16> | **ready-to-merge on green — owner merges** | This session is permission-blocked from merging (session wall). Gate goes green after the card flip; land via REST merge-on-green (R21). |

## ⚑ Flags (owner's morning)

- ⚑ **Merges queued for you (merging was permission-blocked in this session):**
  (1) **fleet-manager #16** (this PR) — merge on green; (2) **superbot #1913**
  — first needs a conflict rebase (dirty against main after #1911/#1914) and
  deserves the one-line sonnet5-sentence correction; a permitted session can
  do the rebase+fix, then you merge.
- ⚑ **Before launching the harness × model experiment (fm #15):** confirm
  "ultracode" is a real, invokable feature name (the entire U-arm treatment
  hinges on that one prompt line), and note the self-merge classifier-wall
  tension — direct-to-main commits (which the wrappers allow) sidestep it.
- ⚑ **Follow-up correction in superbot** (small, any session): the merged
  #1911 grand review says parity rows exist for all 8 missing subsystems;
  **starboard and paragon have no rows** in superbot-next `parity/parity.yml`.
- ⚑ **fleet-manager's own `docs/findings/ping-test-2026-07-09.md` is wrong
  about websites** ("NO ACK") — websites acked 1h39m late via its PR #44,
  independently re-verified tonight. Not corrected in this PR (kept to the
  declared scope; #1913 recommends the same fix) — cheap follow-up for the
  next fleet-manager session.
- ⚑ **venture-lab access wall (resolved, worth knowing):** the GitHub MCP
  initially denied `menno420/venture-lab` ("not configured for this
  session"); `claude-code-remote add_repo` succeeded and the sweep covered it
  (0 open PRs; seed #1 merged 22:49:51Z). New verification sessions should
  expect to need the add_repo step.
- ⚑ **Template rendering bug in the dispatch chain:** the task template's
  cutoff timestamp, dump path, and this file's date slot all rendered as the
  literal string `undefined` — the dispatching workflow should fix its
  variable substitution before the next verification wave.
