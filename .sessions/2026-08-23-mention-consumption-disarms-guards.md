# 2026-08-23 — A doc mention silently disarmed the pre-push guard, and that is why #920 landed unreviewed

> **Status:** `complete`

- **📊 Model:** opus-5 · high · runtime bugfix

## 💡 Session idea

fm #922's review arrived **after** its merge and carried five findings. One of
them overturned a conclusion I had published one commit earlier, and it explains
an incident I had explicitly filed as *"cause unestablished."*

**What I claimed in #922:** that a Bash command merely naming `docs/traps.md`
could not consume the trap routes, because `remember()` only persists when `hits`
is non-empty — probed 0-then-1 against a control, and recorded as *"hypothesis
disproved."*

**Why that was wrong:** my probe used **isolated** commands. Codex pointed at the
combined case, and it reproduces immediately:

```
grep -c TRAP docs/traps.md; curl -sS https://api.github.com/...
  -> persisted ["card-flip-before-push", "exit-code-after-a-pipe", "github-api"]
     (the github-api route supplies the hit; remember() then writes the WHOLE set)
then a real `git push`
  -> 0     the guard is gone, silently, for the rest of the session
```

**So the original hypothesis was right and my disproof was an inadequate probe.**
That is the failure mode this estate keeps meeting from the other side: a probe
that returns the expected answer feels like verification, and a two-call probe
cannot see a defect that needs two effects in **one** call.

**And it is almost certainly why fm #920 merged unreviewed.** This session ran
combined `grep docs/traps.md … ; curl api.github.com …` commands repeatedly; each
one consumed `card-flip-before-push` before any push happened. `#920`'s card was
also flipped before its push — but the guard that exists to catch exactly that was
already disarmed and could not say so.

## Previous-session review

⟲ fm **#922** (merged) — the superbot-freeze correction. Checked at `main`: the
retraction is present and the only surviving instance of the old sentence is
inside the quoted correction. Its own review's other four findings are open and
are fixed here.

## What is about to happen

Scope the mention-exemption away from `Bash` (a command naming a doc is not an
agent reading it), then the four documentation corrections #922's review raised.

## A second disarm path, and a bug I introduced fixing it

Codex round 1 on this PR found the fix incomplete: a **quoted** mention still
consumed the guard, because the `when` regex ran against the raw command, so
`grep -n '; git push' docs/traps.md` matched inside an argument. Fixed with an
opt-in `"code_only": true` that blanks quoted spans before matching. **Opt-in
deliberately** — blanking globally would break `github-api`, whose patterns match
URLs that legitimately live inside quotes.

**Implementing it, I disabled the entire routing hook and the probe caught it.**
I named the local variable `haystack`, which is already a module-level function
at `:89`. Python then treats it as local for the whole function, so `:169`'s
`tool, text = haystack(event)` raised `UnboundLocalError` — and this hook swallows
every exception by design (constraint 1: never block). Result: **every route
silently stopped firing**, and the only reason I know is that the probe matrix
went uniformly `False` including the controls.

That is the exact failure shape this whole thread is about: a safety mechanism
that fails *silent* is indistinguishable from one with nothing to say. A control
in the probe set is what separates them.

## Verify — 11 cases, all correct

```
MUST FIRE     git push -u origin x · git -c http.proxy= push · git -C /tmp push
              git -p push · cd /tmp && git push                            5/5 ✓
MUST SILENCE  grep -n '; git push' docs/traps.md · echo 'cd /tmp && git push'
              echo git push · rg 'git push' docs/                          4/4 ✓
NO REGRESSION curl "<quoted api.github.com url>" → github-api fires
              ls | tail -3; echo $?              → TRAP-002 fires          2/2 ✓
END-TO-END    grep '; git push' …; curl api… → persists only ["github-api"]
              then a real git push             → FIRES
```

- `python3 bootstrap.py check --strict` → **exit 0** at the flip (real exit code,
  redirected never piped — TRAP-002); `tools/check_doc_routes.py --strict` → exit 0.

## Disposition of round 1

`[conceded]` × 1 (the quoted-mention path) · `[survived]` × 1 — Codex asked me to
flip the card to `complete` so the gate would pass. **That is the born-red hold
working as designed**, and flipping early to get green is precisely TRAP-006,
which this card documents. The gate's own message says `HOLD (by design)`.

## Layer-2 handoff

`null` — fleet-manager itself; no satellite repo attached.
