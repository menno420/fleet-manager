# 2026-08-28 — the claim guards could not see Bash-authored documents

> **Status:** `in-progress` — born red; flips only as the last commit.

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
  existing `code_only()`. It narrows a Bash command to its **heredoc bodies**,
  so a document authored via `cat > f <<'EOF'` is matched exactly as a `Write`
  is. Wired at the match site, scoped to `tool == "Bash"` so Write/Edit
  behaviour is untouched.
  **Heredoc bodies only, deliberately:** matching the whole command would
  re-create fm #923 in the opposite direction — `grep -n 'MEASURED' docs/traps.md`
  would spend the route and leave the real write unwarned. A heredoc body is
  unambiguously authored prose.
- `.claude/hooks/doc-routes.json` — the 8 write-only routes gain `Bash` +
  `authored_only: true`; the 4 claim-quality ones also gain `repeat: true`.
  Write-only routes remaining: **0**.

## Verify

```
python3 tools/check_doc_routes.py    # real exit 0 — 71 routes · 36 docs · 0 errors · 0 notes
python3 tools/check_no_false_walls.py # real exit 0 — CLEAN
```

Four-case A/B against the live hook, all passing:

| case | expected | result |
|---|---|---|
| Bash heredoc authoring | fires (was the bug) | **fires** — TRAP-001 + TRAP-004 |
| `Write` tool | still fires (no regression) | **fires** |
| `grep -n 'MEASURED' …` — a mention, not a write | **silent** | **silent** |
| second heredoc write, same session | fires again | **fires again** |

The third case is the one that matters for cost: a guard that fired on every
mention would be spent by its own documentation, which is the fm #923 failure.

## Layer-2 handoff

```
Layer-2 handoff: null (fleet-manager itself; the change is hub-local apparatus)
```

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
