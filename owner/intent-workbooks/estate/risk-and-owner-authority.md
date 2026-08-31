# How I think risk and owner authority should work

## My current understanding

`VERIFIED`: agents may handle safe, reversible technical details within the
requested scope. They should ask before spending, publishing, sending messages,
changing access or privacy, handling credentials, deleting material, or taking
another consequential external action.

`DERIVED`: the important boundary is consequence, not whether a task is
technically difficult. You want agents to act decisively inside the boundary
and to make the exact consequential step visible when your authority is needed.

`DERIVED`: repositories with real users, production services, private data, or
payments need stronger repository-specific rails than experiments.

## What I suggest

`PROPOSED`: each repository declares its consequence profile: users, production,
money, private data, external communication, destructive operations, and
recovery path. Shared rules remain short; repository-specific risks live beside
the code they govern.

## Questions for you

1. What level of spending is always meaningful enough to ask about?
2. Which services may agents restart or redeploy without asking?
3. Which repositories must remain private, and why?
4. What kinds of temporary downtime are acceptable without your approval?
5. When is a reversible deletion, such as archiving or trashing, still important
   enough to ask first?
6. Are there external messages agents may draft but never send without you?

## Your words

`OWNER`:

