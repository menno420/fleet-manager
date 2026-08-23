# 2026-08-23 — A doc mention silently disarmed the pre-push guard, and that is why #920 landed unreviewed

> **Status:** `in-progress`

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

## Verify

(filled before the flip — real exit codes, never after a pipe: TRAP-002)
