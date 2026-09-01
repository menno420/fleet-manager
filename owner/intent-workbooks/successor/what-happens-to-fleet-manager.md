# What happens to this repository

## My current understanding

`VERIFIED`: `[D-0025]` says this repository becomes the **read-only archive**
once the successor exists. Nothing records what that means mechanically —
archived on GitHub, left writable but unused, or something in between.

`VERIFIED`: archiving a repository on GitHub is reversible and blocks writes
only; deletion is the irreversible one. So the archive decision is cheap to
make and cheap to undo.

`DERIVED`: the risk is not losing this repository. It is that both repositories
stay half-alive — an agent boots into the old one out of habit, finds a
plausible boot file, and works from a frozen record. Nothing currently prevents
that, and the boot file here would not tell it anything is wrong.

## What I suggest

`PROPOSED`: whatever you decide, the cutover should include a redirect at the
top of this repository's boot file and README that names the successor and says
this tree is frozen. That single change is what stops a stale session, and it
costs one commit.

## Questions for you

1. Do you want this repository archived on GitHub, or just left alone?
2. How long do you expect to still refer back to it?
3. Is there anything here you would want to keep working on rather than freeze?
4. Would you ever want it deleted, or does it stay indefinitely?

## Your words

`OWNER`:
