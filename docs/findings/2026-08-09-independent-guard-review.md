# Independent review of fm #833 and #834

> **Status:** `reference` · 2026-08-09 · fm #835 · evidence below is `MEASURED`
>
> **Scope:** attack the seven substrate-kit defect claims, the local scanner's
> fixed-distance negation exemption, and the trigger guard plus its 52-case
> baseline suite. This is a claim → command → verdict record, not a prose read.

## Verified starting state

| claim | what ran | verdict |
|---|---|---|
| `main` is `0ab4d07` | local `git rev-parse HEAD main origin/main` plus the connected GitHub repository head | **survived** — all resolved to `0ab4d07edd7ad989ed2614b34584d2f933777c28` before the branch was cut |
| zero open PRs | connected GitHub pull-request query, state `open` | **survived** — zero before fm #835 opened |
| all five gates are green | each requested command was run independently on untouched `main`; exits were 0 / 0 / 0 / 0 / 0 | **survived** — `bootstrap.py check --strict`, doc routes, local false-wall checker, change-guard suite, trigger-guard suite |

The first gate appended 49 records to `.substrate/guard-fires.jsonl`; that is
expected checker telemetry and is retained in the session delta.

## A. Seven substrate-kit defect claims

### What ran

`python3 tools/ab_kit_scan.py` was run against banked v1.20.1 and live v1.20.2.
The inherited script exited 0 but printed only six rows: two controls plus
defects 2, 3, 6, and 7. It did **not** run defects 1, 4, or 5, so the claim that
this command reran all seven did not survive.

Independent probes then exercised defect 1 with `is_render_path=True`, defect 4
across a fenced block, and defect 5 by running both dists' `init` followed by the
documented `skills --build` command in separate fresh temporary adopter roots.
The harness was extended so one invocation now repeats all of those probes.

### Verdicts

`want=flag` means a correct scanner must report at least one hit;
`want=clear` means it must report none.

| claim | measured old → new | semantic expectation | verdict |
|---|---:|---|---|
| 1 · render-file early return hides authored prose | 1 → 0 | flag | **survived; regression** in v1.20.2 |
| 2 · a repudiated quote clears a second genuine assertion | 1 → 0 | flag | **partial; line-level regression**, but old is red for the wrong reason: its quote-only control is also 1 → 0, so old did not prove occurrence-level attachment |
| 3 · `deploy` family regex never matches plain `deploy` | 0 → 0 | flag | **survived; long-standing**, not a regression |
| 4 · lookforward crosses a Markdown fence | 1 → 0 | flag | **survived; regression** in v1.20.2 |
| 5 · `skills --build` is described as install but only stages | claim=1, init=0, build=0, staged=14, live=0 in both | successful install requires live > 0 | **survived; long-standing**, not a regression |
| 6 · conjunction splitter rejects valid repudiation | 0 → 1 | clear | **survived; regression** in v1.20.2 |
| 7 · negation before `because` clears another subject's wall | 1 → 0 | flag | **survived; regression** in v1.20.2 |

The corrected classification is therefore **five new behaviours** (1, 2, 4,
6, 7) and **two long-standing defects** (3, 5). Six scanner behaviours differ
because the quote-only control is a legitimate v1.20.2 improvement in addition
to the five defect changes. The `want=` values are correct; treating every
`DIFFERS` row as a defect would not be.

## B. Fleet-manager's 48-character negation cliff

### What ran before the fix

Three real `--root` fixtures established the direction before source changes:

| fixture | `python3 tools/check_no_false_walls.py --strict --root <fixture>` | verdict |
|---|---:|---|
| bare wall | exit 1 | positive control caught |
| `does not reproduce because` followed by the same wall | exit 0 | **hole confirmed** |
| valid direct negation of the wall | exit 0 | negative control clear |

The old `main` source was also loaded directly from `git show` and swept around
the boundary. Measuring from the end of the `not` token to the wall signal gave:

| distance | 43 | 44 | 45 | 46 | 47 | 48 |
|---:|---:|---:|---:|---:|---:|---:|
| flagged | no | no | no | yes | yes | yes |

That reproduces the requested coarse cliff — 44 clears and 48 flags — and pins
the exact transition between 45 and 46 token-end characters. The cause was the
literal slice `window[max(0, sig_start - 48):sig_start]`, not grammatical
attachment.

### Fix and post-fix verdict

`tools/check_no_false_walls.py` now starts the bounded lookback after the last
same-window clause boundary (punctuation, conjunction, or subordinator). The
48-character cap remains so a direct correction can still hard-wrap across one
physical Markdown line.

The permanent self-test covers the reported phrase and both hard-wrap
directions. Separate post-fix CLI fixtures returned:

| fixture | exit | verdict |
|---|---:|---|
| bare wall | 1 | **survived** — still red |
| `does not reproduce because` + wall | 1 | **fixed** — now red |
| direct wall negation | 0 | **survived** — valid correction remains clear |

This is a deliberately narrow attachment heuristic, not a parser. An arbitrary
unrelated negation inside one unsplit grammatical clause can still be ambiguous;
the accepted failure class and the observed boundary forms are now pinned.

## C. Trigger deletion guard and baseline 52-case suite

### What ran

- `python3 tools/test_trigger_tools_guard.py` on untouched `main`: exit 0,
  **52/52 passed**.
- Full source-to-assertion audit of `.claude/hooks/trigger_tools_guard.py` and
  `tools/test_trigger_tools_guard.py`.
- `python3 tools/install_root_hooks.py`: exit 0; the installed matcher includes
  `Bash|mcp__.*__delete_trigger|mcp__.*__send_later` and needed no repair.
- Independent subprocess traffic probes for exact tool names, literal Python /
  JavaScript API forms, executing and inert heredocs, and a data-flow command.
- Expanded suite after the independent audit: exit 0, **58/58 passed**.

### Verdicts

| claim | what the probe showed | verdict |
|---|---|---|
| deletion is denied on the tool name | exact `mcp__x__delete_trigger` returned process exit 0 with `permissionDecision: deny` | **survived**; docstring corrected because the process itself never exits nonzero |
| command-text deletion is advisory only | literal curl/Python/JavaScript forms returned warning context, never deny | **survived** — command intent remains undecidable by regex |
| common direct-API forms are covered | `requests.request('DELETE', …)` and JS `{method: 'DELETE'}` were silent in the baseline | **conceded and fixed**; `.request` plus `method:` are now covered and tested |
| quoted heredocs are safely stripped only when inert | file-writing heredoc stayed silent, but `eval` and `source` consumers were silent in the baseline | **partial and fixed**; both executors now warn, inert quoted writes remain silent |
| command-text coverage is complete | `METHOD=DELETE; curl -X "$METHOD" …` remains silent | **refuted as a possible guarantee**; recorded boundary is intentional, and the exact tool-name leg remains the enforcement point |
| `send_later` warning follows the owner's no-PR-self-wake rule | baseline warning recommended `send_later` as a PR-CI fallback | **conceded and fixed**; warning now reserves it for external un-notified waits and says to report pending PR CI after bounded polling |
| the suite pins warning meaning | baseline asserted only that some warning existed | **conceded and fixed**; it now asserts that subscriptions miss CI success and that the warning does not recommend a PR self-wake |
| `subscribe_pr_activity` wakes on all CI results / merges | measured capability record says comments, reviews, and CI failures; not CI success or new push | **refuted**; boot file, decision, and hook docs now use the measured scope |
| disabling stops a firing immediately | `enabled: false` is verified for future firings; cancellation of an in-flight run is unverified | **refuted at that bound**; docs now state only what was measured |
| API warning dedups once per session | implementation keys on the distinct command fingerprint | **refuted**; README corrected to once per distinct command |
| README's numeric suite count is current | it said 31 while the baseline executable ran 52 | **refuted**; the duplicate count was removed and the suite prints its own count |

No one of the baseline 52 cases was found to require the opposite expected
outcome. The remaining defects were **coverage and contract-assertion gaps**:
the suite passed while literal API forms, two executing heredocs, and the
warning's prohibited recommendation went untested. The first six added
assertions made those gaps executable without pretending the regex can
understand dynamic shell data flow.

### Codex landing review on fm #835

Codex reviewed `6388db4c1fec89e7ae84be80ad6e883ee38b225d` and returned two
inline findings. Both survived direct reproduction and were conceded:

| finding | reproduction | disposition |
|---|---|---|
| P2 · causal `since` was not a negation boundary | `does not reproduce since agents cannot merge` returned clear; `given that` did too | added `since` and `given [the fact] that`; pinned both plus the valid `not as if …` control so bare `as` does not overcorrect |
| P3 · `eval|source` matched filenames anywhere before `<<` | inert writes to `source.md` and `eval.md` warned, while `note.md` stayed silent | anchored those executors to shell command positions; pinned both filenames and a `&& source … <<` execution control |

The post-review trigger suite is **61/61**: nine assertions beyond the 52-case
baseline. Because both findings changed reviewable code, the corrected head is
sent through one re-review round before the born-red flip.

## Result and residual work

- The local defect-7 analogue is fixed and acceptance-tested.
- The seven-defect A/B instrument now matches its own coverage claim.
- Trigger enforcement remains exact on the tool name and advisory on command
  text, with nine more regression assertions and corrected operational guidance.
- The local occurrence-attachment analogue of kit defect 2 still exists. It is
  recorded here and in the canonical kit finding; it was not folded into the
  owner's line-284 acceptance scope.
- Cutting substrate-kit v1.21.0 remains a separate owner-gated session.
