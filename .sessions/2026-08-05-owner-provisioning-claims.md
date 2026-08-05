# 2026-08-05 · hub — the owner's provisioning claims are primary evidence

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the estate's verify-first doctrine was built to stop agents
trusting **records** and **their own inferences**. It got applied to the person
who provisioned the environment, and the result is sessions spending turns
verifying a credential against the man who created it. That is not caution —
it is checking a source against its own output.

## Previous-session review

Every correction landed on me today came from the owner, and every one was
right. That is the evidence this entry rests on: the doctrine is not "believe
him because he is the owner", it is "his provisioning claims have a measured
track record and re-deriving them costs the scarcest resource in the estate."

## Scope

Owner-directed live. Write it so a **skeptical** agent acts on it — which means
it must not read as "do not verify", or a reader will correctly resolve it
against the surrounding doctrine and ignore it. It resolves instead as the
DISCOVERY RULE already stated, applied in the right order.

## What landed

- `docs/CAPABILITIES.md` — **step 0** of the DISCOVERY RULE, plus a
  *"why this is not an exception to verify-first"* section carrying the measured
  base rate, the cost in the owner's own words, and the boundary as a table.
- `.claude/CLAUDE.md` — the operative rule in the capabilities section, where a
  session reads it *before* the doubt rather than after.
- substrate-kit `CAPABILITIES.md.tmpl` (PR #574) — the same step 0, so it
  reaches every adopter instead of this repo alone.

## Why it is written this way

The failure mode is not ignorance — it is a session correctly applying
verify-first to the wrong object. So an entry saying *"trust the owner"* would
lose: a skeptical reader resolves it against the surrounding evidence doctrine
and moves on. It only holds if it resolves **with** that doctrine.

It does. The DISCOVERY RULE already says *attempt once, capture the exact
error.* Sessions have been running verify-**then**-attempt, which is the
inversion. And the rules it would seem to conflict with — probe-not-record, the
tree beats a self-report, a green check that fights the evidence is a bug in the
check — were built against **stale records** and **agent inference**. The owner
is neither. He is the source the record would be describing, so probing his
statement before acting checks a source against its own output.

Three things make it persuasive rather than assertive: the **base rate**
(measured, below), the **cost** in his own words, and the **boundary** stated
explicitly so the entry cannot be over-read into "stop checking responses."

## Measured

**Seven owner corrections this session. Seven correct. Zero false positives.**
A skipped reading pass · nine open PRs dismissed on a doc's word · an unkept
commitment to read the provider docs · a rule this session wrote and then failed
to follow three times · and two wrong claims about his own writing, where the
agent supposedly held the expertise.

He also supplied a quantitative prior the session cannot read about itself —
context consumed, ~300k against ~400k expected — and it was accurate.

**The cost of the current behaviour, his words:** *"multiple turns across
multiple sessions, where an agent first spends multiple minutes trying to verify
certain claims or pushes back with questions about what the certain tokens can
or can't do."*

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Kit side: build, ruff, `2116 passed`, `dist/bootstrap.py check --strict`
  → all **exit 0**.

**Honest nulls.** This entry has **no mechanism** — nothing can gate "a session
doubted its owner", so it binds only by being read, which is the weakness this
whole day kept finding. Placement is the only lever available, hence both the
boot file and step 0 of the file a session opens at the moment of doubt. The
base rate is n=7 from one session with one owner; it is strong evidence about
*this* owner and none at all about adopters', which is why it stayed out of the
kit template.

## ⟲ Previous-session review

The wall-refutation session recorded that the ledger *"knew how to find out"*
and had no way to make it happen. This is the same file, one layer up: it knew
to attempt-then-record, and had no entry for the case where the answer was
already supplied. Both are the discovery rule being incomplete rather than
wrong — and in both cases the missing piece cost real turns before anyone
noticed it was missing.

## 💡 Session idea

**Render the owner's settled facts into the boot file, per environment.** Step 0
tells a session to trust a provisioning statement it *hears*. It does nothing
for a session that never hears one, because the owner is not in the room — which
is most sessions.

The kit already fills templates from an interview. The same mechanism could
render a short **"already settled in this environment"** block: which credentials
exist and their scope, which provider path is chosen, which surfaces are
reachable. Then a fresh session does not need to remember a principle about
authority, and does not need the owner present to benefit from it — it opens
already knowing the answers he would otherwise have to give again. That converts
this entry from doctrine into data, which is the only move that has reliably
worked all day.
