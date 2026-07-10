<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# Trigger registry snapshot — 2026-07-10 (the fleet's first committed full trigger snapshot)

> **Extracted:** 2026-07-10 ~22:05Z via `list_triggers` (full pagination: page 1 = 100
> records, page 2 = 14 records, no further cursor → **114 triggers total**). Extractor:
> the registry gap-closure pass (this PR). **Why this file exists:** wake/trigger prompts
> are INVISIBLE unless copied out — `list_triggers` is the only read, and nothing owner-side
> shows a routine's stored prompt after creation. Every *enabled* fleet-seat prompt below is
> **VERBATIM-FROM-REGISTRY, byte-exact, single line as stored** (script-extracted from the
> raw tool output, not retyped). Re-extract on any re-arm and update the seat's
> `failsafe-prompt.md` deployed-state note (ONE-WRITER: the manager edits this registry).

## 1. Enabled cron wakes — the fleet's standing clocks (8)

### `trig_01L5JBefGSCM1fUdwm4SRQnY` — Builder failsafe wake

- **seat:** superbot-next / Builder (coordinator)
- **cron:** `0 */2 * * *` · **enabled:** true · **created:** 2026-07-10T19:48:40.Z
- **session binding:** `session_01HRfuSKiQSnGHXKne3yzadg` (persistent)
- **prompt (verbatim, 257 chars, single line as stored):**

```
FAILSAFE WAKE (Builder, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

### `trig_014odnv5h1tkJAFRhix3tGLq` — fleet-manager failsafe wake

- **seat:** fleet-manager (coordinator)
- **cron:** `30 */2 * * *` · **enabled:** true · **created:** 2026-07-10T20:26:23.Z
- **session binding:** `session_01V66KdPhtbR1AThhK77kDqr` (persistent)
- **prompt (verbatim, 497 chars, single line as stored):**

```
FAILSAFE WAKE (fleet manager, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop — sync menno420/fleet-manager to origin/main HEAD, read control/inbox.md at HEAD, then slice after slice (staleness sweep → route/advance ORDERs → owner-queue + safe-to-delete → doctrine ORDERs), each shipped as its own merged-on-green PR — and re-arm the chain (~15 min) before ending. Heartbeat control/status.md as each batch's last step.
```

### `trig_0178q9Je2xRFJgthwamrg9Br` — idea-engine failsafe wake

- **seat:** idea-engine (coordinator)
- **cron:** `0 */2 * * *` · **enabled:** true · **created:** 2026-07-10T19:47:11.Z
- **session binding:** `session_01TwoaFmWeB8pYbHMyFYgjqJ` (persistent)
- **prompt (verbatim, 261 chars, single line as stored):**

```
FAILSAFE WAKE (idea-engine, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

### `trig_012EvztCrHHg7s4mBsKT3VKs` — product-forge failsafe wake

- **seat:** product-forge (coordinator)
- **cron:** `0 */2 * * *` · **enabled:** true · **created:** 2026-07-10T19:46:57.Z
- **session binding:** `session_01QrRUqynDs8ijKCPqZh1ZGs` (persistent)
- **prompt (verbatim, 263 chars, single line as stored):**

```
FAILSAFE WAKE (product-forge, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

### `trig_01SHfnLv6EqZesr4tC3T9kUU` — sim-lab failsafe wake

- **seat:** sim-lab (coordinator)
- **cron:** `0 1-23/2 * * *` · **enabled:** true · **created:** 2026-07-10T20:54:51.Z
- **session binding:** `session_01JbwY8yeBzLKYcbeR89L88v` (persistent)
- **prompt (verbatim, 724 chars, single line as stored):**

```
FAILSAFE WAKE (simulator, Q-0265 continuous mode): if your send_later continuation chain is alive (a pending continuation exists), verify that in one line and end. If it stalled, RESUME THE WORK LOOP: sync menno420/sim-lab to origin/main HEAD; read control/inbox.md; pull new sim-ready entries from menno420/idea-engine control/outbox.md (raw, at HEAD) into your queue; then work slice after slice — gated verdicts (validity gate + @codex comment + finalized outbox entry), intake triage, harness slices — each merged-on-green. Re-arm the continuation chain (~15 min) before ending the turn; overwrite control/status.md as each turn's last step. If this trigger is one-shot rather than recurring, re-arm it for +120 minutes.
```

### `trig_016EfUawz6KxEYqUM6f1BqDw` — substrate-kit 2-hourly standing wake

- **seat:** substrate-kit (coordinator)
- **cron:** `0 */2 * * *` · **enabled:** true · **created:** 2026-07-10T15:53:36.Z
- **session binding:** `session_01YMJrUDpcarFsqPZ2BeeiVB` (persistent)
- **prompt (verbatim, 655 chars, single line as stored):**

```
2-HOURLY WAKE (substrate-kit): sync menno420/substrate-kit to origin/main HEAD; read control/inbox.md at HEAD; then ONE bounded pass — exactly one of: advance one §6 centralization item | run one distribution wave for a pending kit release | one kit development/bench slice. Lane-repo writes are DISTRIBUTION ONLY (Q-0261.3) — never lane domain work, never their control/ files. Ship merged-on-green per the target repo's conventions; decide-and-flag; no excessive work — one real slice per wake. Overwrite control/status.md as the deliberate last step. If this trigger is one-shot rather than recurring, re-arm it for +120 minutes before ending the turn.
```

### `trig_01YBaVeKAW2fSD83S9F37s2d` — trading-strategy failsafe wake

- **seat:** trading-strategy (coordinator)
- **cron:** `0 */2 * * *` · **enabled:** true · **created:** 2026-07-10T21:03:05.Z
- **session binding:** `session_01NwvvbgUVSdQvY8eYwtuEoo` (persistent)
- **prompt (verbatim, 315 chars, single line as stored):**

```
FAILSAFE WAKE (trading-strategy, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD -> inbox -> slice after slice, each merged-on-green — grade due ledger windows before new research) and re-arm the chain (~15 min) before ending.
```

### `trig_017H9Qb9oxtLgUy6sw2gnSHg` — websites lane wake — 4-hourly inbox ritual (ORDER 008)

- **seat:** websites (fresh-session-per-fire)
- **cron:** `0 */4 * * *` · **enabled:** true · **created:** 2026-07-10T13:49:36.Z
- **session binding:** none — fresh session per fire
- **prompt (verbatim, 576 chars, single line as stored):**

```
websites lane wake (fleet ORDER 008). In /home/user/websites: git fetch origin main and land on origin/main HEAD, then read control/inbox.md at HEAD and run the standing per-session ritual from your instructions (control/README.md: execute any `status: new` order not already in your own control/status.md done= line, claim-first; then overwrite control/status.md as the deliberate last step). Honor the repo's .claude/CLAUDE.md working agreement and docs/CAPABILITIES.md walls; forward-only git; never edit control/inbox.md; never pass ambient RAILWAY_* env vars to anything.
```

## 2. Enabled one-shots at snapshot — the live Q-0265 continuation-chain links (8)

The ~15-min `send_later` pacemaker chains (and watcher check-ins) pending at extraction
time. These are ephemeral by design (each fires once, `ended_reason=run_once_fired`, and
the seat re-arms a fresh one); they are snapshotted here because they are the chain text
patterns the dispatch asked recorded — the per-seat 'continue the work loop' grammar.

### `trig_01AmoT2hN7DxVowpKvgCPA2a` — send_later 2026-07-10T21:52Z #8f110f

- **seat:** trading-strategy (coordinator) · **fires:** 2026-07-10T21:52:00Z · **session:** `session_01NwvvbgUVSdQvY8eYwtuEoo`
- **prompt (verbatim, 198 chars):**

```
continue the work loop (trading-strategy, Q-0265): sync HEAD -> read control/inbox.md -> next slice, each merged-on-green; grade due ledger windows before new research; re-arm ~15 min before ending.
```

### `trig_01MNHBpkdNbfGXmX4ob2Rf6S` — send_later 2026-07-10T21:58Z #2eba13

- **seat:** product-forge (coordinator) · **fires:** 2026-07-10T21:58:00Z · **session:** `session_01QrRUqynDs8ijKCPqZh1ZGs`
- **prompt (verbatim, 101 chars):**

```
CONTINUATION CHAIN (Q-0265): continue the work loop: sync HEAD → inbox → next slice → re-arm ~15 min.
```

### `trig_011yQiYUErpgcybHfcksMKDc` — send_later 2026-07-10T21:58Z #084dab

- **seat:** idea-engine (coordinator) · **fires:** 2026-07-10T21:58:00Z · **session:** `session_01TwoaFmWeB8pYbHMyFYgjqJ`
- **prompt (verbatim, 150 chars):**

```
CONTINUATION CHAIN (idea-engine, Q-0265): continue the work loop — sync HEAD → inbox → next slice → re-arm the chain (~15 min) before ending the turn.
```

### `trig_015ME3CQV9LkXqQHuRVFHnd2` — send_later 2026-07-10T21:59Z #b50135

- **seat:** fleet-manager (coordinator) · **fires:** 2026-07-10T21:59:00Z · **session:** `session_01V66KdPhtbR1AThhK77kDqr`
- **prompt (verbatim, 582 chars):**

```
CONTINUE THE WORK LOOP (Q-0265 chain): verify ORDER 012 (games mapping, PR #41) reached terminal state. If merged and the inbox is still clear, next slice = review-queue drain pass: for the 8 backfilled rows in docs/review-queue.md, post the @codex question on Codex-enabled repos (superbot, superbot-next — one specific question per row on the merged head, R24 template) and manager-verify ONE row on a Codex-less repo; mark rows drained with citations. Plus regenerate docs/roster.md (playbook R25). Re-arm ~15 min before ending. Free window through 2026-07-14: keep the loop hot.
```

### `trig_01Q9WCh7A4BJZdvpo7tzHF6a` — send_later 2026-07-10T21:59Z #d8cb71

- **seat:** sim-lab (coordinator) · **fires:** 2026-07-10T21:59:00Z · **session:** `session_01JbwY8yeBzLKYcbeR89L88v`
- **prompt (verbatim, 466 chars):**

```
PACEMAKER WAKE (sim-lab, Q-0265 continuous mode): continuation chain link. Check project state — pending child replies, control/inbox.md queue; dispatch the next slice if the verdict lane is idle (INTAKE 002 is next after VERDICT 002 finalizes; verdict slices run SERIAL — control files are single-writer), then re-arm this chain ~15 min via a worker before ending the turn. Cron dead-man 'sim-lab failsafe wake' (trig_01SHfnLv6EqZesr4tC3T9kUU) remains the backstop.
```

### `trig_01KUe4AK8vrPvdpPt5aU7QTi` — Builder continuation chain (one-shot)

- **seat:** superbot-next / Builder (coordinator) · **fires:** 2026-07-10T22:00:37Z · **session:** `session_01HRfuSKiQSnGHXKne3yzadg`
- **prompt (verbatim, 134 chars):**

```
CONTINUATION CHAIN (Builder, Q-0265): continue the work loop — sync HEAD → inbox → next slice → re-arm ~15 min before ending the turn.
```

### `trig_01M8BhQZjibwvKjbG47C4Z8m` — send_later 2026-07-10T22:40Z #e95624

- **seat:** other/unmapped · **fires:** 2026-07-10T22:40:00Z · **session:** `session_01Stc1m5xag7i9WBuyuqn71G`
- **prompt (verbatim, 186 chars):**

```
HOURLY WAKE: check list_project_activity, verify child sessions are alive and progressing, settle any blockers, then re-arm the next hourly wake via a worker calling send_later (60 min).
```

### `trig_01SPtXz8EdtUs6Fzt9ciLSDS` — send_later 2026-07-10T22:42Z #d5fe94

- **seat:** other/unmapped · **fires:** 2026-07-10T22:42:00Z · **session:** `session_01UBzu6Zhb38XdK4bvUrHtfh`
- **prompt (verbatim, 518 chars):**

```
Self check-in (part-4d): verify superbot PR #1965 reached a terminal state — it should have auto-merged on green (docs-only, card flipped complete at head 61615e08). If still open, diagnose CI / mergeability and re-kick; if merged, silently unsubscribe from #1965 and do not message the owner unless something is wrong. Also opportunistically re-check: manager ⚑ games-mapping proposal (relay pasted ~21:3xZ, must place the read-only data API), registry location flagged in manager status, sim-lab INTAKE 003 progress.
```
## 3. Superbot hub routines (page 2 of the registry — 3 records)

Superbot has **NO fleet seat by design** (Q-0264); these are the hub's own routines. Their
prompts are multi-kilobyte and have **committed twins in superbot** — they are indexed here,
not re-transcribed (hand-carrying kilobytes invites corruption; the registry read reviewed
them inline this session):

| trigger id | name | cron | enabled | session binding | stored-prompt twin |
|---|---|---|---|---|---|
| `trig_01MWHvQFnRF1dVdZFSP6SM5L` | superbot night executor | none (poke-only; `next_run_at` epoch-zero) | **true** | none (fresh env-session per fire; env `env_01CZRF681i8ef2zqt9GgboYy`) | none committed — the doc section says "MERGED into dispatch (Q-0145)" yet the trigger is still enabled with the full pre-merge NIGHT EXECUTOR prompt stored (incl. retired `needs-hermes-review` / `continue`-issue machinery). **Finding → follow-up below.** |
| `trig_018wP6XTPmf9DLnxrG4RpGVh` | suberbot docs reconciliation *(sic — stored name typo)* | none (poke-only; fired by the `reconcile`-issue Action) | **true** | none (fresh env-session per fire) | superbot `docs/operations/autonomous-routines.md` § "Routine: superbot docs reconciliation" (committed twin 14,206 chars; byte-equality stored-vs-doc UNVERIFIED — trigger `updated_at` 2026-06-23, the doc has been edited since; verify at next superbot routine-maintenance pass) |
| `trig_011XAWqPeksS8LBrS5G9RvVc` | superbot autonomous dispatch | `0 */3 * * *` | **absent/false — paused** (`next_run_at` stale at 2026-07-02T03:07Z; `last_fired_at` 2026-07-02T00:07Z) | none (fresh env-session per fire) | superbot `docs/operations/hermes-dispatch-bridge.md` (line ~77, "You are the SuperBot DISPATCH routine…"; byte-equality stored-vs-doc likewise UNVERIFIED) |

Page 2 also held **11 fired one-shots** (spent send_later check-ins from superbot PR-watch
sessions, 2026-06-30 → 2026-07-06: `trig_01VhS2Z757ASeZhBZwzZjStQ`,
`trig_016j14p6UigFCupDS2vmwMic`, `trig_01RdBx7Lqk9MtwJW17SLBPNL`,
`trig_01XQKtsR9MT9GzSDj3ZYiaBR`, `trig_01SLS7eK69XsWiwfT8HxaNUK`,
`trig_01F8u2vidYoCjJgRRJ3jacZJ`, `trig_01X66nSxikx3YpGemH6C8W6S`,
`trig_01NgtwXN88ywaGwxNBRZWwHc`, `trig_01LzavcNxJVXh4WhxdZU5Cb8`,
`trig_01W4euGdp7ze9HwjfaunU6N6`, `trig_01AR19KhDQ7wxMXjLTH5LxKw` — all
`ended_reason=run_once_fired`).

## 4. Fired one-shot history (page 1 of the registry — 84 spent chain links / check-ins)

Compact index only (spent one-shots; each disabled itself after firing,
`ended_reason=run_once_fired`). Prompt lengths recorded; texts recoverable via
`list_triggers` while the records persist.

| trigger id | name | seat/session | fired at | prompt chars |
|---|---|---|---|---|
| `trig_01BQxk7wDhTDBDqXd6bW2tBn` | Builder continuation chain (one-shot) | superbot-next/Builder | 2026-07-10T21:44:00Z | 134 |
| `trig_01RBCuKChKBmK4gGXkVUJBB2` | send_later 2026-07-10T21:43Z #498e38 | sim-lab | 2026-07-10T21:43:00Z | 466 |
| `trig_01WgK5PCc5vveoi1BhrkLNo7` | send_later 2026-07-10T21:43Z #412df0 | fleet-manager | 2026-07-10T21:43:00Z | 314 |
| `trig_01PV2HYV7VKaztTUugX4jYVx` | send_later 2026-07-10T21:42Z #4d45b1 | product-forge | 2026-07-10T21:42:00Z | 101 |
| `trig_01CeVCcmHQRuCiV8CwxmTQqy` | send_later 2026-07-10T21:42Z #8242ac | idea-engine | 2026-07-10T21:42:00Z | 150 |
| `trig_01NdARN4hgPrj6dZu73t5eXw` | send_later 2026-07-10T21:40Z #66173a | `session_01M7wqFYowEdNDKct3sFu9Et` | 2026-07-10T21:40:00Z | 570 |
| `trig_01SBW5KMbidbAptJNzShDD5v` | send_later 2026-07-10T21:36Z #d1a135 | trading-strategy | 2026-07-10T21:36:00Z | 198 |
| `trig_01LEn5WtBLYtv4LR5JRtTKka` | Builder continuation chain (one-shot) | superbot-next/Builder | 2026-07-10T21:27:00Z | 134 |
| `trig_01CB17YpjvhMBQWgQSsnep6e` | send_later 2026-07-10T21:27Z #b92549 | sim-lab | 2026-07-10T21:27:00Z | 443 |
| `trig_018v2UKHAkM9qUXiFydzqfE9` | send_later 2026-07-10T21:26Z #033181 | product-forge | 2026-07-10T21:26:00Z | 101 |
| `trig_01AJvTMsvfUk46CvS3wSkt3F` | send_later 2026-07-10T21:26Z #64a421 | idea-engine | 2026-07-10T21:26:00Z | 150 |
| `trig_01QWpCYS8wBdX3Pa1sDq6Gk1` | send_later 2026-07-10T21:20Z #b140a0 | trading-strategy | 2026-07-10T21:20:00Z | 198 |
| `trig_01FQmdPjpzNViVpCsjMmW13F` | send_later 2026-07-10T21:13Z #94bace | fleet-manager | 2026-07-10T21:13:00Z | 317 |
| `trig_01T93ZVC5iQHEqw172HKcGRc` | Builder continuation chain (one-shot) | superbot-next/Builder | 2026-07-10T21:11:00Z | 134 |
| `trig_01EPYz7dukY2fN9aVhoDHF5F` | send_later 2026-07-10T21:11Z #abfc12 | sim-lab | 2026-07-10T21:11:00Z | 277 |
| `trig_016NRQ4Phnve6w2XihfsvHib` | send_later 2026-07-10T21:10Z #461c8e | product-forge | 2026-07-10T21:10:00Z | 101 |
| `trig_01KL5aqvEpLQ1xaYV2YegMXd` | send_later 2026-07-10T21:09Z #87d2f6 | idea-engine | 2026-07-10T21:09:00Z | 150 |
| `trig_011TupbSQeEmkjGjsLM77svq` | Builder continuation chain (one-shot) | superbot-next/Builder | 2026-07-10T20:54:00Z | 134 |
| `trig_017LMJAzNHRMhGtNVPgiUhFK` | send_later 2026-07-10T20:53Z #fa298a | idea-engine | 2026-07-10T20:53:00Z | 150 |
| `trig_01QS12GV6hX31U8Had12DAzM` | send_later 2026-07-10T20:53Z #052746 | product-forge | 2026-07-10T20:53:00Z | 101 |
| `trig_016JyeVr57WFPegPgPqUFhW2` | send_later 2026-07-10T21:38Z #2dbe3f | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T21:38:00Z | 186 |
| `trig_01TbqcDzFebPDG6f5pApmqiH` | send_later 2026-07-10T20:43Z #39290f | fleet-manager | 2026-07-10T20:43:00Z | 392 |
| `trig_01ENc3JL3hCocrrkmvpU8L1Q` | send_later 2026-07-10T20:37Z #c969a7 | idea-engine | 2026-07-10T20:37:00Z | 150 |
| `trig_01BMKGV9JEJmrM4XbiTRFqYp` | send_later 2026-07-10T20:37Z #242dbd | product-forge | 2026-07-10T20:37:00Z | 101 |
| `trig_01TLw6n6mwejxAc7BnZXNxJw` | Builder continuation chain (one-shot) | superbot-next/Builder | 2026-07-10T20:37:00Z | 134 |
| `trig_019QdntJiSc6arirJGPGHzMQ` | send_later 2026-07-10T20:21Z #2a3713 | idea-engine | 2026-07-10T20:21:00Z | 150 |
| `trig_01TMYFExUrtTHL5wUceS1Gx7` | Builder continuation chain (one-shot) | superbot-next/Builder | 2026-07-10T20:20:00Z | 134 |
| `trig_018ReTxf36SF1YxuhWQKVHav` | send_later 2026-07-10T20:20Z #82a968 | product-forge | 2026-07-10T20:20:00Z | 101 |
| `trig_01KedTiCKYMbB3oaNZL5rHmf` | Builder continuation chain (one-shot) | superbot-next/Builder | 2026-07-10T20:03:00Z | 134 |
| `trig_01Chw4ZJHgBmTiKKV6iwxdhR` | send_later 2026-07-10T20:04Z #c770d7 | idea-engine | 2026-07-10T20:04:00Z | 150 |
| `trig_01T1C42VdzxRDab7QJL8rKvE` | send_later 2026-07-10T20:03Z #50b7d5 | product-forge | 2026-07-10T20:03:00Z | 101 |
| `trig_01X2UZ1con77MBN2BRhyRM8z` | send_later 2026-07-10T20:36Z #2718d6 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T20:36:00Z | 186 |
| `trig_01Wgan8Wxpp4JqJ5gZXR6VZB` | send_later 2026-07-10T19:30Z #f80a38 | product-forge | 2026-07-10T19:30:00Z | 189 |
| `trig_01Q4d6kUeQdb9uXq5QDcGokb` | send_later 2026-07-10T19:34Z #aff027 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T19:34:00Z | 186 |
| `trig_01PLPGLW1aVVNfjmRYZ7KB99` | send_later 2026-07-10T18:23Z #ef3c02 | `session_013jn6gKuieayKpSyRjYBoBp` | 2026-07-10T18:23:00Z | 712 |
| `trig_016YiG69sRYtZG6n9mQrk87G` | send_later 2026-07-10T18:33Z #ab3c41 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T18:33:00Z | 186 |
| `trig_018qdi4HVuU5JXMY1ifApCdT` | send_later 2026-07-10T17:31Z #38818d | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T17:31:00Z | 186 |
| `trig_014N2ZhTmL7hr8rL4i6dYbAQ` | send_later 2026-07-10T16:37Z #c9537e | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T16:37:00Z | 282 |
| `trig_01DFzCcmYQuugdxLUfuEf9Xo` | send_later 2026-07-10T16:20Z #b73f45 | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T16:20:00Z | 270 |
| `trig_017nBRdCbTDa5bvqxugNP4q3` | send_later 2026-07-10T16:51Z #d85486 | `session_01TTmgk6psnbpDoPhjWeGKFH` | 2026-07-10T16:51:00Z | 687 |
| `trig_01EFoZ9Ro2DKv2Virr6uFLcD` | send_later 2026-07-10T16:30Z #c8a9b9 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T16:30:00Z | 186 |
| `trig_01WP6iQcNi6wFEaXVp1hjoqw` | send_later 2026-07-10T15:50Z #b3e04f | `session_01TTmgk6psnbpDoPhjWeGKFH` | 2026-07-10T15:50:00Z | 514 |
| `trig_01Nbg1LxV2qY8DZWC7Zkc29Q` | send_later 2026-07-10T15:29Z #177503 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T15:29:00Z | 186 |
| `trig_01Vq3hs4d11g1Jyi2J5qs4V2` | send_later 2026-07-10T14:45Z #0d413e | `session_01TTmgk6psnbpDoPhjWeGKFH` | 2026-07-10T14:45:00Z | 369 |
| `trig_01UJmSDKpBxutvhhCAejtzqD` | send_later 2026-07-10T13:53Z #a63e04 | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T13:53:00Z | 270 |
| `trig_01LW2G37sibY7y3pNSAs1obc` | send_later 2026-07-10T14:27Z #89205b | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T14:27:00Z | 186 |
| `trig_01XaVtGnNdzfgFjPVDiHjdWU` | send_later 2026-07-10T13:25Z #5457a9 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T13:25:00Z | 186 |
| `trig_01UqLz87gi7iZe96LgmoXhKg` | send_later 2026-07-10T13:21Z #971ab2 | `session_01Ubm9oFQyDDFguP3jxX3fU4` | 2026-07-10T13:21:00Z | 480 |
| `trig_01LpfrcfGoPA4hG1HCTJMokG` | send_later 2026-07-10T12:26Z #bdbf37 | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T12:26:00Z | 284 |
| `trig_01LsGyRNnbGM7p5DwGHVSDHS` | send_later 2026-07-10T12:14Z #dc5e19 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T12:14:00Z | 186 |
| `trig_01EEKVgzsNFWtqevDw3Khahz` | send_later 2026-07-10T11:12Z #2881ab | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T11:12:00Z | 186 |
| `trig_01UUoo82Lo3Ek11HnToppJxA` | send_later 2026-07-10T10:10Z #cfb683 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T10:10:00Z | 186 |
| `trig_01NDMDw2eXjcszg4saASEc4q` | send_later 2026-07-10T09:08Z #0d0446 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T09:08:00Z | 186 |
| `trig_0124yEJjHMQ47D6gz3js1hv2` | send_later 2026-07-10T08:06Z #fa0700 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T08:06:00Z | 186 |
| `trig_01NF8gZBZ4GxVr2tBiaQ46n2` | send_later 2026-07-10T07:04Z #4583fc | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T07:04:00Z | 186 |
| `trig_01BCNXGtsvNXf4Rdt4FKzWbW` | send_later 2026-07-10T06:01Z #6b7697 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T06:01:00Z | 186 |
| `trig_01NdAd7rc39jKg9sTg7kexht` | send_later 2026-07-10T04:54Z #9da976 | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T04:54:00Z | 268 |
| `trig_0174WRi9mcHCfLh2UR5c9HHv` | send_later 2026-07-10T04:32Z #ee15c8 | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T04:32:00Z | 283 |
| `trig_01Q9fe5SjhQLwvTjBEote2VH` | send_later 2026-07-10T05:00Z #4196fd | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T05:00:00Z | 186 |
| `trig_013T2FBEfRYc9dnEEjk9N7cD` | send_later 2026-07-10T03:58Z #21ab5d | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T03:58:00Z | 293 |
| `trig_01PCtUvkvrgMUrVeqiAuPTBX` | send_later 2026-07-10T03:35Z #02e46d | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T03:35:00Z | 274 |
| `trig_015hEW6svgusqTcAavLWD5T6` | send_later 2026-07-10T03:13Z #7783e1 | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T03:13:00Z | 275 |
| `trig_01DGfox9i7byjJNyiaz4eQiM` | send_later 2026-07-10T03:59Z #24aa5a | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T03:59:00Z | 186 |
| `trig_015NsnAE3akt1barpfjGTYqS` | send_later 2026-07-10T02:49Z #b9235d | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T02:49:00Z | 283 |
| `trig_012uLQogXzJPo9WpDW7FWYUg` | send_later 2026-07-10T02:23Z #b9acc6 | `session_01HfvExBRHuzpPLv5v5sJVUg` | 2026-07-10T02:23:00Z | 238 |
| `trig_01JLgUBvQrKHsoYDBRSJtfFF` | send_later 2026-07-10T02:58Z #b093b7 | round-3 orchestrator (hourly child-watch chain) | 2026-07-10T02:58:00Z | 186 |
| `trig_016sf2NrrGe1UfAcLuQ2xSL3` | send_later 2026-07-10T01:10Z #aaedf4 | `session_019n91gNe1NZ6LPgVK6YPuPr` | 2026-07-10T01:10:00Z | 367 |
| `trig_014DYJJ6tSuPwJKgXQmAHPsX` | send_later 2026-07-10T00:14Z #5c776a | `session_01VfGW2uj7iG9PE7C559m5ua` | 2026-07-10T00:14:00Z | 422 |
| `trig_018NySNnCxeDGpCQB8j8MBj4` | send_later 2026-07-09T05:41Z #0e2d5e | `session_01WTPWnnFMgGF4yT9c3NCacD` | 2026-07-09T05:41:00Z | 654 |
| `trig_01EsNyrorxJwWjA9AC6aSmdw` | send_later 2026-07-09T04:39Z #ea511a | `session_01WTPWnnFMgGF4yT9c3NCacD` | 2026-07-09T04:39:00Z | 490 |
| `trig_01FbPd8kWRVip2tJ2TnRy5tZ` | send_later 2026-07-09T03:37Z #fc997c | `session_01WTPWnnFMgGF4yT9c3NCacD` | 2026-07-09T03:37:00Z | 391 |
| `trig_015W2dNmWbmHDJqnpUcgbhRt` | send_later 2026-07-09T02:37Z #9ea495 | `session_01VHEs2RDpuLUsiMhzPVcYjQ` | 2026-07-09T02:37:00Z | 181 |
| `trig_01PFxuojGx4UisaUdKGdXMiS` | send_later 2026-07-08T15:34Z #8304de | `session_01TUW6Dmh6J3JtfSDenzVVWx` | 2026-07-08T15:34:00Z | 342 |
| `trig_0196YZaZfUSTYgrhXa9zTQHQ` | send_later 2026-07-07T20:12Z #1491c4 | `session_01PLF5wwa5KjQw2gn9gx7aVw` | 2026-07-07T20:12:00Z | 239 |
| `trig_01Dnj8tWyEh8EKuNVpaSWZQ3` | send_later 2026-07-07T19:59Z #145a10 | `session_01PLF5wwa5KjQw2gn9gx7aVw` | 2026-07-07T19:59:00Z | 246 |
| `trig_01BbP1EcnMzETTBSFaLMueJv` | send_later 2026-07-07T19:51Z #ce7d64 | `session_01PLF5wwa5KjQw2gn9gx7aVw` | 2026-07-07T19:51:00Z | 296 |
| `trig_01FCS3NPkbZgDfW5FDbdPa8B` | send_later 2026-07-07T19:45Z #596351 | `session_01XCowiKQiUY1GKCzQ9dvbBV` | 2026-07-07T19:45:00Z | 221 |
| `trig_01YY1JVVjmyRuU9kTmXh2dKA` | send_later 2026-07-07T19:04Z #398b88 | `session_01XCowiKQiUY1GKCzQ9dvbBV` | 2026-07-07T19:04:00Z | 338 |
| `trig_01QEZvcwLbqDef7A7417uLtY` | send_later 2026-07-07T17:02Z #d30ef1 | `session_01XCowiKQiUY1GKCzQ9dvbBV` | 2026-07-07T17:02:00Z | 322 |
| `trig_01BAW2GKnyfd8EJMimzwPkUq` | send_later 2026-07-07T15:07Z #585ab2 | `session_01CBHekm7vi2Sio9fLg2iQeJ` | 2026-07-07T15:07:00Z | 545 |
| `trig_01EKMYPZMg9ticxp6s2JnaRn` | send_later 2026-07-07T13:21Z #2925d8 | `session_01CBHekm7vi2Sio9fLg2iQeJ` | 2026-07-07T13:21:00Z | 345 |
| `trig_01PwLpcas8gEYkysUJtvMdBq` | send_later 2026-07-07T02:41Z #e8cdac | `session_01EMNhdZtGpznHRfLwygVQZ8` | 2026-07-07T02:41:00Z | 386 |
| `trig_01FUaVZZin4N31JYQKKweYCc` | send_later 2026-07-07T02:08Z #8ce219 | `session_01EMNhdZtGpznHRfLwygVQZ8` | 2026-07-07T02:08:00Z | 464 |
| `trig_01EtS2z5fvUhgUpg6xYRrScA` | send_later 2026-07-06T22:23Z #94c374 | `session_01FTc75yfXrBs7uC93Xn8BxE` | 2026-07-06T22:23:00Z | 538 |

## 5. Reconciliation — stored prompts vs this registry's deployed-state claims

Byte-compared 2026-07-10 ~22:05Z (script over the raw `list_triggers` output; wrapped file
blocks compared after unwrap). Verdicts, now folded into each seat's `failsafe-prompt.md`:

| seat | trigger | verdict |
|---|---|---|
| superbot-next/Builder | `trig_01L5JBefGSCM1fUdwm4SRQnY` | **byte-match** (257 chars) — registry claim confirmed |
| idea-engine | `trig_0178q9Je2xRFJgthwamrg9Br` | **byte-match** (261 chars) — registry claim confirmed |
| sim-lab | `trig_01SHfnLv6EqZesr4tC3T9kUU` | **content-match** (724 chars; wrap-only difference) — and the file's "NOT ARMED" status was stale: armed 20:54:51Z, after the package build. Fixed. |
| fleet-manager | `trig_014odnv5h1tkJAFRhix3tGLq` | **MISMATCH** — file quoted the generic §2b template (263 chars); deployed is a richer manager-specific text (497 chars, "fleet manager" with a space). Verbatim now committed. |
| product-forge | `trig_012EvztCrHHg7s4mBsKT3VKs` | **MISMATCH** — file's canonical text is the founding-package long form (790 chars); deployed is the generic §2b template (263 chars). Functional-benign; verbatim committed; canonical re-arm still recommended. |
| trading-strategy | `trig_01YBaVeKAW2fSD83S9F37s2d` | **SUPERSEDED-then-MISMATCH** — old `trig_01Mvn5xRmqGmZJNRHgjqyLpN` is GONE; new 21:03Z failsafe live at `0 */2` with a shortened seat-authored prompt (315 chars) vs the file's 746-char canonical. Verbatim committed. |
| substrate-kit | `trig_016EfUawz6KxEYqUM6f1BqDw` | **[RECONSTRUCTED] resolved** — actual stored text extracted verbatim (655 chars, pre-Q-0265 "2-HOURLY WAKE… ONE bounded pass"); confirms the reconstruction's substance. Q-0265 failsafe cutover still due at next seat contact. |
| websites | `trig_017H9Qb9oxtLgUy6sw2gnSHg` | **UNVERIFIED resolved** — stored prompt IS the v1-era ORDER 008 text (576 chars), now committed verbatim; **v2 is NOT deployed**, owner re-paste (paste-wave item 4) still owed. |

**Cutover-hygiene confirmations:** all four old trigger ids named by the registry as
deleted/superseded (`trig_01Mvn5xRmqGmZJNRHgjqyLpN`, `trig_01QBrp5MjZL3F9mv6KsTXTzN`,
`trig_01KBoHPaquSCDHysip67PQBh`, `trig_01VYZQ7GHxYq3ecSw8UNZek8`) are absent from the full
registry — 0 occurrences across both pages.

**Follow-ups (⚑ for the manager sweep):** (1) superbot `night executor` trigger is still
ENABLED with a pre-Q-0145 prompt whose machinery is retired — disable-or-re-base decision
belongs to the hub/owner; (2) stored-vs-committed byte-equality for the two superbot
routine prompts is unverified; (3) substrate-kit + product-forge + trading canonical
re-arms remain open per their failsafe files.
