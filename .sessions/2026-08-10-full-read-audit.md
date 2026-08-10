# 2026-08-10 · hub — full-read audit of fleet-manager (100% of tracked files)

> **Status:** in-progress

- **📊 Model:** opus-5 family · ultracode workflows · review/verify
- Time: 2026-08-10 · venue: Claude Code remote container, owner-live hub chat ·
  branch `claude/fleet-manager-full-audit-lty31q`

💡 Session idea: coverage is only a claim until the ledger is built from what
the readers returned; an agent that reports "batch covered" has told you about
its intention, not its reading.

Layer-2 handoff: null (fleet-manager itself)

## What is about to happen

Every tracked file in this repository — all 833, 30,006,142 bytes as enumerated
at `4b59e9b` — is read by a fan-out of workflow agents. Each agent returns the
explicit list of paths it opened together with a content-derived fingerprint per
path (line count, head and tail slices), and the coverage ledger is assembled
from those returns and then mechanically diffed against `git ls-files`. Findings
are then refuted by independent agents before any of them are reported.

This session READS and REPORTS. The edit pass is a later session and the owner's
call.

## Previous-session review

⟲ fm #837 (D2 truth pass) rebuilt the cold front door so purpose, live state and
next action are recoverable from three files, and removed volatile counts from
boot prose. It proved the route works for a reader who follows it. The question
it left open — and the reason this session exists — is what is true of the files
that route never visits: five consecutive sessions whose stated job was to read
this repo and put it in order all missed that the owner's current plan was
unreachable from the front door, because each read a curated subset and each
subset was internally coherent.

## Close-out

### Shipped

- `docs/audits/2026-08-10-full-read/enumeration.tsv` — `git ls-files` frozen at
  `4b59e9b` before any file was read: 833 paths, 30,006,142 bytes. The denominator,
  committed first so the set could not be narrowed to whatever got covered.
- `docs/audits/2026-08-10-full-read/coverage-ledger.tsv` — one row per enumerated
  path, assembled from read-agent **returns**. **833 READ · 0 UNVERIFIED · 0
  NO-RETURN**; 814 full, 19 structural. `diff` of the ledger's path set against the
  enumeration returns nothing.
- `docs/audits/2026-08-10-full-read/verification.md` — how a row earned `READ`, and
  the one file (`guard-fires.jsonl`) whose fingerprint provably could not reproduce
  because this audit's own gate runs grew it.
- `docs/audits/2026-08-10-full-read/findings.md` — **345 findings adjudicated, 0
  left unjudged: 322 survived · 23 refuted**, split **108 defect / 212 stale-but-
  harmless**, with a "Start here" section for the seven that cost the most.
- `docs/current-state.md`, `docs/owner-queue.md` — the audit made reachable from a
  live surface, and `OQ-FM-D2-TARGET` filed for the one decision only the owner can
  make.
- `.claude/skills/session-close/SKILL.md` + `docs/SKILLS-local.md` — one broken link
  fixed (`../../` resolved into `.claude/`) and registered in the re-apply table,
  since the kit's copy loop reverts kit-named skills silently.

### Method — why the coverage claim is checkable

Fifty-seven agents each took a contiguous, non-overlapping slice of the frozen
enumeration and returned, per path, a line count plus the first and last non-empty
line. All three were recomputed from the tree and compared; a row needed two of three
to match. An agent that skipped a file could list its path but could not produce that
file's last non-empty line. Then every finding went to an independent refuter told to
default to refuted when uncertain — which killed 23, including a "missing
`fleet_status.py`" that turned out to be superbot's script, correctly referenced
cross-repo here.

### Verify — real exit codes

```
python3 bootstrap.py check --strict   → 1   (sole finding: this card's born-red hold)
```

Four real findings were raised by the gate against this audit's own output and fixed
rather than suppressed: a missing Status badge, an orphaned `verification.md` (the
`reachable` check — the same defect class this audit reports), and quoted markdown
links plus quoted decision ids inside `findings.md`. The last used the estate's own
U+2011 fix from `scripts/gen_roster.py:1029` in preference to adding a
`check-exceptions.yml` suppression, because over-broad suppressions are themselves a
finding here.

### Capability delta

None new. One correction to the record instead: `.claude/CLAUDE.md:262` calls
`trigger_tools_guard.py` "the estate's **only denying hook**". Measured here: it is
the only denying hook **in fleet-manager** (the other five score zero on deny-shaped
code). The estate-wide claim is unverified and other repos were out of scope.

### ⚑ Owner-facing

- `OQ-FM-D2-TARGET` — the NOW pointer names shiftlife; owner said live it is not
  active. Only he can set the target.
- `OQ-FM-AGENTS-BOOT`, `OQ-KIT-V1-21-RELEASE` — untouched.

### Ideas

💡 The audit's own instrument is the reusable part: a fingerprint returned per file
makes "did you actually read it" a mechanical question. `docs/ideas/` already carries
`derive-dont-state-counts`; the larger class this found is **an appended correction
does not retract what it corrects** — worth its own idea file next session.

### ⟲ Previous-session review

fm #837 rebuilt the cold front door and proved the three-file route works for a reader
who follows it. This audit read what that route never visits and found two of the four
defects it reported fixed still live — including `current-state.md:373`, which #837
itself rewrote.
