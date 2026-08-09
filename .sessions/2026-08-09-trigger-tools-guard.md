# 2026-08-09 · hub — stop sessions stalling the owner with trigger deletions

> **Status:** in-progress

- **📊 Model:** opus-5 · high · feature build — owner-stated: `delete_trigger`
  is the one call that raises an approval prompt in automode, so a session that
  makes it stalls until he is back at the keyboard

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/kit-upgrade-eap-reconciliation-e9poz5` (restarted from `54f5283` =
`origin/main` after fm #833 merged)

💡 Session idea: **an autonomy product's worst tool is the one that silently
requires a human.** Every other call this estate makes either succeeds, fails
loudly, or is denied in writing — all three leave the session working.
`delete_trigger` does something worse: it *pauses* and waits, and the session has
no way to see that it is waiting. The owner is away by design during
implementation, so the cost is not a prompt, it is **the rest of the session**.
He named it as the only tool with this property, so the fix is narrow and total.

Layer-2 handoff: null (fleet-manager itself)

## Previous-session review

⟲ fm #833 landed the kit upgrade and the EAP correspondence record. **This
session exists because of a mistake made at the end of it:** with the PR merged,
a pending check-in was cleaned up with `delete_trigger` — tidy by every rule
written down at the time, and exactly the call that costs him a manual approval.
He corrected it live and asked for three things: **do not use them, document it,
and build the hook that warns.**

**The correction also removes a habit this session leaned on.** Five `send_later`
check-ins were armed across fm #833 to poll a PR. He points out they were never
needed — `subscribe_pr_activity` already wakes the session on PR events, which
is push rather than poll, costs nothing while idle, and cannot arm a trigger that
later needs deleting. **The deletions this session had to clean up were created
by the polling it chose.**

## What is about to happen

1. **`trigger_tools_guard.py`** — `PreToolUse`, matching the trigger tools by
   name across any MCP server prefix, plus the direct-API route around them.
2. **`delete_trigger` is DENIED, not warned.** Every other advisory here is
   advisory because it involves judgement; this one does not. A tool name is an
   exact string, the owner has stated there is no legitimate agent use, and the
   cost of a false positive is one env-var override. That is the *"no judgement,
   no config, no way to argue with it"* shape
   [`2026-08-09-error-to-mechanism.md`](../docs/findings/2026-08-09-error-to-mechanism.md)
   § 2 names as ideal — the Edit tool's exact-match, not a checker.
3. **`send_later` is WARNED, not denied** — it has a legitimate use (a genuinely
   external, un-notified wait), it just was not the right tool for polling a PR.
4. **Documented** where a session reads before acting, not only where it reads
   afterwards.

## Verification

Both directions, and against the real call that caused this: the guard must deny
`delete_trigger` under any server prefix, warn on `send_later`, catch the
direct-API route around both, and stay **silent on every other tool** — including
the trigger tools this estate legitimately uses. A test suite, not a walkthrough,
because fm #831 measured that testing a mechanism against its own motivating case
and its absence still missed every defect it met in real traffic.

At close: `python3 bootstrap.py check --strict`, both checkers, and both hook
suites, real exit codes, each on its own line. Codex review requested while
born-red.

## Close-out

*(to be completed before the Status flips)*
