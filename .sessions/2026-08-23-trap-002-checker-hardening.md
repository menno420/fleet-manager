# 2026-08-23 — the TRAP-002 checker looked like it worked

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut
> from `origin/main` at `2af06d6` (fm #917). Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe. Before the flip it returned 1 on the
> designed born-red hold alone — confirmed by reading the finding, not assumed
> from the exit code.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #917 landed `tools/check_pipe_exit_code.py` and its card described the
exemption as *"file-scoped `pipefail`"*. Owner-review asked what the code
actually measures. It measures `re.search(r"PIPESTATUS|pipefail", text)` over
the **whole file** — no scope analysis of any kind. So `pipefail` set *after*
the pipe, inside a subshell, or named only in a **comment** exempted every pipe
in that file, and a single `PIPESTATUS` anywhere exempted every other pipe too.

The second question was what defines a shell script. The answer was `*.sh` — an
extension, so an extensionless executable with a shebang was invisible.

Both are the same failure: **the description was more principled than the
code**, on an instrument shipped one PR earlier to catch exactly that class of
thing.

## previous-session review

fm #917 (`2af06d6`) did the important half right — it built the positive control
before trusting the clean run, which is why the checker was known to catch its
target at all. What it did not do is test the *exemptions* against adversarial
cases: all three exemption fixtures were the well-formed version. A fixture set
that only contains the cases you expect to pass will not find a rule that
exempts too much. That is the lesson worth carrying, and it generalises past
this checker.

## What landed

**The exemptions are positional now.**
`set -o pipefail` exempts only when enabled on a non-comment line **above** the
pipe; `PIPESTATUS` exempts only when read **within the window**, at the use
site. Comments no longer exempt anything.

**Extension is no longer the definition of a shell script.** Extensionless files
whose first 200 bytes match a shell shebang are scanned. `MEASURED` 2026-08-23:
this repo has **zero** such files today — every tracked extensionless file was
checked for a `bash|sh|zsh` shebang and none matched — so this closes a latent
gap, not a live one. Stated that way rather than implying a save.

**The fixture set went 4 → 8**, and the four new ones are the cases the shipped
version silently passed: `pipefail` after the pipe · `pipefail` in a comment ·
`pipefail` in a subshell with the pipe outside · an extensionless shebang
script. Result: **5 flagged, 3 passed, zero false positives.**

**`docs/traps.md`** — the TRAP-002 coverage prose corrected, with the original
defect written into the register rather than quietly fixed, and the residual
limits named: `pipefail` via a sourced file or a function defined above and
called below is still untracked.

## What was checked, not assumed

- **The repo is still clean, and it means more.** 18 files, 0 findings — from a
  checker that now catches four classes it previously missed. The earlier clean
  could not distinguish "no instances" from "exemption swallowed them".
- **The extensionless claim was measured**, not assumed from a glance at the
  tree: every tracked file without a suffix was opened and its first line
  tested.

## The honest gap

Static shell analysis has real limits and the register now says so instead of
implying completeness. The bias remains toward missing a real instance rather
than crying wolf — an instrument nobody trusts gets ignored — but "miss-biased"
is now a stated design choice with named boundaries, not an accident of a
regex.

## Verify

- `python3 bootstrap.py check --strict` → **exit 0**, read directly, never after
  a pipe.
- 8-fixture control → 5 flagged / 3 passed, exit 1 under `--strict`.
- `python3 tools/check_pipe_exit_code.py` → 18 files, 0 findings, CLEAN.
