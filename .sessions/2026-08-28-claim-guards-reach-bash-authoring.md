# 2026-08-28 — the claim guards could not see Bash-authored documents; and the estate-wide skill/rule reuse map

> **Status:** `in-progress` — born red; flips only as the last commit, after a
> review answers at the head that carries the repeat cap and the tests.

- **📊 Model:** opus-5 · high · docs-only
- **📍 Venue:** cloud-container

## Mission

Owner, live, after this session made five claim-quality errors in one sitting
and Codex caught six findings over three rounds: *"Those errors you had, how
could we make sure another session doesn't make the same mistakes? Is this
something we can turn into a hook or skill?"*

The answer turned out not to be a new guard. **The estate had already written
the guards, and they were aimed at a tool this session never used.** This card
lands the coverage fix and its evidence.

## The finding

`MEASURED` 2026-08-28, by A/B against the live hook (not inferred):

**Eight of the 71 routes were registered `Edit`/`Write` only** — and they are
exactly the claim-quality set: `stamping-a-measured-claim`,
`claim-beyond-the-sample`, `absence-claim`, `recording-a-wall`, plus the four
card-discipline routes. Measured by parsing `.claude/hooks/doc-routes.json`
and partitioning every route's `tools` list; the other 63 reach `Bash`,
`Read`, `Grep`, `WebFetch` or the prompt event.

**This session authored every document through Bash heredocs** — the card, the
findings doc, and every edit (`cat > f <<'EOF'`, `python3 - <<'PY'`). Auto
mode's standing system-reminder instructs exactly that: *"make file changes
with sed, heredocs, or short scripts, rather than using the dedicated Read,
Edit, or Write tools."*

**So all eight were disarmed for the entire session, silently.** The A/B, same
offending text both ways, run against `.claude/hooks/route_docs.py`:

| authoring route | result |
|---|---|
| `Write` tool | TRAP-001 **and** TRAP-004 both fire |
| Bash heredoc | no output, exit 0 |

And TRAP-004's own text describes the error this session then made, in advance:
*"THE COUNT-ONLY FORM IS THE ONE THAT KEEPS GETTING THROUGH — 'X cards', 'Y
commits' with no ratio and no qualifier reads as a census and is usually a
sample."* This session published a checker count taken from `grep -l` file
hits (including `__init__.py`), a commit count from memory that was off by
one, and a `MEASURED` label on owner-console state that the certainty legend
reserves for reproducible commands.

**Second defect, same class, already diagnosed in this repo's own code.**
`route_docs.py:505-515` records three measured incidents (fm #922, #923, #937)
of fire-once semantics silencing an *action* guard, and says plainly that the
first two *"were patched by narrowing what CONSUMES the route, which fixes the
instance and leaves the class."* Only `card-flip-before-push` carried
`repeat: true`; the claim-quality routes guard a **recurring** class and were
fire-once, so one early firing spends them for the rest of a multi-hour
session.

## Shipped

- `.claude/hooks/route_docs.py` — new `authored_only()`, the complement of the
  existing `code_only()`, keyed on **write intent** rather than on the presence
  of a heredoc. A Bash command authors when it names a write target
  (`bash_write_targets()`: a redirect, `tee`, or `sed -i`); what it authors is
  its heredoc bodies plus its quoted spans, the latter carrying the payload of
  a `printf '…' > f`. No write target means no text and silence, so a mention
  stays cheap and leaves the route unspent (fm #923's failure, inverted).
  **The first cut keyed on the heredoc alone and was wrong three ways** — see
  the R2 disposition below.
- `.claude/hooks/route_docs.py` — **`target_path` is now derived for Bash** from
  the first write target. `path_when` gates on that field, which a Bash payload
  has no `file_path` for, so both card routes skipped before their content was
  ever examined and stayed silent for the exact authoring path this change
  added them to.
- `.claude/hooks/doc-routes.json` — the 8 write-only routes gain `Bash` +
  `authored_only: true`; the 4 claim-quality ones also gain `repeat: true`.
  Write-only routes remaining: **0**.

## The reuse map — the owner's second ask

*"find out as much as possible about re-using existing rules and skills in the
existing repos … what we already have that is good skill material and … what
previous sessions struggled with."*

Answered by a **79-agent fan-out** (0 errors, 6.9M subagent tokens, 2.6 h) over
all 19 non-archived repositories, cloned to disk: ten seam readers, nine card
miners, then adversarial verification. **1,002 cards opened** of 3,836.
Record: [`docs/findings/2026-08-28-skill-and-rule-reuse-map.md`](../docs/findings/2026-08-28-skill-and-rule-reuse-map.md).

**The spine, re-measured by this session rather than relayed:** sessions write
an idea on **95 % of 3,836 cards**; **357** reach the conveyors. **10 : 1**,
and **28 : 1** excluding `superbot`, whose **3.1 : 1** is the control condition.
`idea-engine` — the ideas repository — has **503 cards, 503 ideas, zero in its
conveyor**. The estate produces reusable knowledge reliably and never reads it
back, which is OD-21's diagnosis with numbers under it.

**Why the container is the whole question:** gate-enforced **95–97 %** ·
card-template **598/969** · best skill invocation **46/969** · `/groom-ideas`
**0/969** against **82** for the same ritual carried by the template.

**Three subagent headlines were corrected before use** — the "41 sessions over
five weeks" span is two days of filename dates; "skills are never invoked" is
false (10 of 14 are); "3 of 12 repos" is 4 of 19. And the verification pattern
is the most reusable result on its own: **17 of 17 refutations kept their source
citation and lost only the verdict**, every one a duplicate of something
fleet-manager already has.

## Verify

```
python3 tools/check_doc_routes.py    # real exit 0 — 71 routes · 36 docs · 0 errors · 0 notes
python3 tools/check_no_false_walls.py # real exit 0 — CLEAN
```

```
python3 tools/test_doc_route_patterns.py  # real exit 0 — 53 cases
```

**53 cases** (10 must-fire, 3 must-be-silent, 4 shallow-clone, 36 plumbing),
up from the 17 that existed before this change. The plumbing half covers each
claim route's tool opt-in, `authored_only` flag and `repeat`; seventeen Bash
authoring spellings split into writes (visible) and non-writes (silent); the
write-target extraction; and **two end-to-end cases run through the hook as a
subprocess**.

**Three negative controls, each confirmed to fail correctly** rather than
merely passing today: reverting to heredoc-only makes the mention cases fail;
breaking the redirect-after-delimiter regex fails those two spellings; deleting
the `target_path` derivation fails the end-to-end card case.

That third one is the reason the end-to-end cases exist. A first version tested
`bash_write_targets()` directly and **passed with the P1 wiring deleted** — the
helper was fine and the call site was the defect, which is this change's own
failure shape repeating one level down.

## Layer-2 handoff

```
Layer-2 handoff: null (fleet-manager itself; the change is hub-local apparatus)
```

## Review disposition

**`@codex` on head `172ccc5` — not a findings review but an independent
reimplementation**, reported as a comment: it built the same `authored_only()`
extraction, enabled the same eight routes, and made the same four claim guards
repeat, then ran its own four-case A/B and got the same result. It could not
open a PR (`make_pr: command not found`, no git remote in its environment), so
its commits are unreachable from here and nothing was taken from them.

**Two things its testing changed here.** Its case list named heredoc spellings
mine had not been tested against — `<<-` tab-stripping, bare and double-quoted
delimiters, multiple heredocs in one command. All ten variants pass, and they
are now pinned in the suite rather than left in a shell transcript, because a
spelling `authored_only()` misses is this same guard silently backing off one
level down. Negative control: removing `<<-` support from the regex makes the
suite exit 1 naming that variant.

Its report also states *"all 17 regression cases passed"* — the suite was 17
cases at `172ccc5` and is **41** now. That is a correct reading of an earlier
head, not a discrepancy, and it is the reason this card did not flip on its
comment: a verdict binds the SHA it ran on (TRAP-007).

**One correction to this card's own earlier claim.** The reply reporting this
work said the two claim routes "never fired" during the session. That was
argued from the A/B rather than read: `route_docs.py` records per-session fire
state at `/tmp/claude-doc-routes/<session_id>.json`, which would have answered
it directly — and this session's regression suite opens with
`rm -rf /tmp/claude-doc-routes`, so the evidence was destroyed by the test for
the bug it would have evidenced. The conclusion still holds (the routes were
structurally incapable of matching heredoc authoring, which the A/B shows), but
it rests on inference where a direct record had existed. **Anyone reusing that
suite should scope the reset to its own synthetic session ids.**

**`@codex` R2 at head `4490046` — 4 findings (1 P1, 3 P2), all `[conceded]`,
and it found a half-working fix that my own green suite had certified.**

| # | finding | disposition |
|---|---|---|
| P1 | Card routes gate on `path_when`, matched against `target_path`, which is empty for a Bash payload — so both card routes skipped before content was examined and stayed silent for the authoring path this change exists to cover. It reproduced with `cat > .sessions/x.md <<'EOF'` | `[conceded]` — `target_path` now derived from the first write target. **My plumbing tests missed it because they covered the four claim routes, which have no `path_when`** |
| P2 | A heredoc feeding a non-writing command (`grep -f -`, a `python3 -` that only prints) still returned prose and fired the guard — and with the repeat cap, three such commands would exhaust a route before the session's first real write | `[conceded]` — the test is now write intent, so a non-write returns nothing |
| P2 | `printf '…' > f`, `echo > f` and `sed -i` reach disk with no heredoc and bypassed every newly-Bash-enabled route. **The suite actively pinned `echo … > a.md` as correctly-silent**, enshrining the gap | `[conceded]` — quoted spans are now extracted for redirect writes, and that case is inverted to must-fire |
| P2 | `cat <<'EOF' > docs/x.md` and `… | tee f` put the redirect after the delimiter; the regex required a newline immediately after it | `[conceded]` — the delimiter now tolerates trailing shell tokens |

**The pattern across R1 and R2 is one mistake, not four.** I keyed the guard on
*"is there a heredoc"* when the question is *"does this command write, where,
and with what text."* Every finding is a consequence of that substitution, and
the suite I wrote inherited it — which is why it went green over a fix that did
not work for two of the eight routes it claimed to cover. A test written from
the same wrong model as the code cannot catch the model being wrong.

**`@codex` R3 at head `3ebdaa7` — 6 findings (1 P1, 5 P2), all `[conceded]`.**

| # | finding | disposition |
|---|---|---|
| P1 | `bash_targets[0]` only, so when a card is not the FIRST write target both card routes fail `path_when` — `echo ok > docs/x.md; cat > .sessions/x.md <<'EOF' … complete …` let a completed card past the merge-safety warning | `[conceded]` — `path_when` now tries **every** target |
| P2 | The write-target test was global to the payload, so any target authorised every quoted span anywhere in it: `grep 'all 26 repositories' f; echo ok > docs/x.md` fired the count guard although the file receives only `ok` | `[conceded]` — the payload is split on `;`/`&&`/`\|\|`/newline and only **writing segments** contribute their quoted spans |
| P2 | Requiring a dot-extension made `cat > README <<'EOF'` invisible | `[conceded]` — extensionless paths count; the special sinks (`/dev/`, `/proc/`, fd numbers) are excluded by name instead |
| P2 | `card-status-write`'s only `when` is the card PATH, and the Bash haystack carried content alone — so it passed `path_when` and then had nothing to match | `[conceded]` — the Bash haystack is now path + content, mirroring `FIELDS["Write"]` |
| P2 | `python3 - <<'PY'` doing `Path(…).write_text(…)` writes with no shell redirect | `[conceded]` — an interpreter heredoc is judged by **write verb**, not by extracting a path: the path can be a variable, an f-string or a join, and the verb is the reliable signal |
| P2 | The end-to-end cases reused `hash(label)` session ids, so with `PYTHONHASHSEED` fixed a second run failed on an already-spent route | `[conceded]` — a fresh `TMPDIR` per case; the suite is now repeatable, verified by running it twice under `PYTHONHASHSEED=0` |

**And R3 exposed a defect in the tests, not just the code.** The end-to-end
cases asserted only that *something* fired. With the P1 fix deleted the card
routes correctly skipped and `session-card-venue` — which has no `path_when` —
fired on the same payload and satisfied the assertion. **That is the third time
in this change a test was too weak in exactly this way**, after the first P1
test that called the helper instead of the call site. Every end-to-end case now
asserts *which* route answered, by a marker string checked to be distinctive
(`card lifecycle` appears in `card-status-write` and not in
`card-flip-to-complete`).

**Convergence, stated plainly:** R2 returned 4 findings, R3 returned 6. That is
not converging, and the reason is structural — statically deciding what a shell
command writes is unbounded, because the shell has no fixed grammar for "this
is a document". Each round has found a real construct the last one missed.
**The five negative controls now pin every behaviour**, so a future round's
finding lands against a suite that fails rather than a claim that it works. If
R4 returns another construct, the right response is a different mechanism —
`PostToolUse` on Bash, reading what actually changed on disk instead of parsing
intent — not a seventh regex.

**Owed fix, found by the Stop hook and not by a reviewer.** The reply
reporting R3 said CI showed "zero test failures". That was an absence claim
from a grep with no positive control, and the control fails: `doc-route
patterns` appears **0 times** in fm #963's CI log, because
`tools/test_doc_route_patterns.py` ran in **no** gate — not
`scripts/preflight.py`, not `substrate-gate.yml`. The suite has existed since
2026-08-26 and has only ever run in a session's own terminal.

That inverted the guarantee this PR had just given `@codex`: a future finding
would "land against a suite that fails" when in fact it would land against a
suite nobody executes. Registered in `preflight.py` beside the checker pair and
`test_owner_comments.py`, which was already there as the precedent. Verified
both ways — preflight now prints `doc-route patterns -> exit 0`, and with the
P1 fix patched out it prints `doc-route patterns -> exit 1 (1 of 61 case(s)
FAILED)` and the gate fails.

## 💡 Session idea

**The disarming is a property of the harness mode, not of this session — so it
is worth checking whether other guards have the same exposure.**
`read_before_write.py` is registered on the same Write/Edit halves
(its docstring: *"read tools record, Write/Edit check"*), which means a session
authoring through Bash heredocs escapes the did-you-open-it check as well —
the exact guard the boot file cites for *"do not write about a file you have
not opened."* Not verified this session and deliberately not fixed here; it is
a separate change with its own blast radius.
**Guard recipe:** the anchors are `read_before_write.py`'s PreToolUse
registration in `.claude/settings.json` and its own tool-name dispatch; the
test target is the same four-case A/B used above, with the write half issued
as a heredoc.

## ⟲ Previous-session review

The previous card is `.sessions/2026-08-28-repo-orientation.md` (fm #962) —
this session's own earlier card. It landed well in one respect: every one of
Codex's six findings across three rounds was conceded and fixed, with the
dispositions recorded in a table rather than summarised.

**What it got wrong is the reason this card exists.** It recorded the six
findings as two defect classes and named the failure as *"skipping the
adversarial self-read before pushing"* — a discipline diagnosis, which is
precisely the kind of fix `intent.md` § 4 says does not work. The mechanical
cause was available and unexamined: the guards that exist for those exact
errors were registered on tools the session was not using. A card that had
checked *why the guard did not fire* instead of resolving to try harder would
have found this five hours earlier.
