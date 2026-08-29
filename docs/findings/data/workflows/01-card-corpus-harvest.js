export const meta = {
  name: 'estate-agent-error-audit',
  description: 'Harvest, classify and adversarially verify agent errors across 20 repos of session cards, into substrate-kit fixes and skill candidates',
  phases: [
    { title: 'Harvest', detail: '68 lanes over the sharded evidence corpus' },
    { title: 'Synthesize', detail: 'one lane per error class over all its incidents' },
    { title: 'Verify', detail: 'adversarial refute + coverage check + checkability per pattern' },
    { title: 'Prescribe', detail: 'kit changes, skills, hooks, chains' },
  ],
}

const SP = '/tmp/claude-0/-home-user-fleet-manager/5c635c91-40a8-50d4-a884-7c6e9a2b0388/scratchpad'
const CLASSES = [
  'false-state-claim','unverified-verification','null-as-proof','overgeneralized-claim',
  'process-step-skipped','premature-completion','wall-invented','scope-drift','intent-loss',
  'handoff-loss','tool-misuse','stale-record-left','review-mishandling','duplicate-work',
  'fake-precision','other',
]

const INCIDENT = {
  type: 'object',
  properties: {
    incidents: { type: 'array', items: { type: 'object', properties: {
      cite: { type: 'string', description: 'repo · path:line exactly as the shard header gives it' },
      date: { type: 'string' },
      what_happened: { type: 'string', description: 'What the AGENT did wrong, concretely, 1-2 sentences. Not what the code did wrong.' },
      quote: { type: 'string', description: 'verbatim evidence from the shard, <=240 chars' },
      error_class: { type: 'string', enum: CLASSES },
      gap_class: { type: 'string', enum: ['absent','unrouted','unenforced','missing-procedure'] },
      trigger_moment: { type: 'string', description: 'the concrete moment it happens: e.g. "about to write a MEASURED claim", "before git push", "after a piped command"' },
      cost: { type: 'string' },
      deterministic_check: { type: 'string', description: 'a mechanical check that would have caught it, or "none - judgment"' },
      severity: { type: 'string', enum: ['high','medium','low'] },
    }, required: ['cite','what_happened','quote','error_class','gap_class','trigger_moment','severity'] } },
    shard_notes: { type: 'string', description: 'anything notable about this shard: era, repo, striking patterns' },
  },
  required: ['incidents'],
}

const HARVEST_RULES = `
You are auditing an AI-agent estate's own record for AGENT ERRORS — mistakes made by AI coding sessions,
not bugs in product code. The evidence is sections harvested from session cards, findings and retros.
The richest sections are "previous-session review" (each session audits the one before it) and
"friction -> guard". Sections are separated by "---" and headed with [repo] path:line, date and section title.

WHAT COUNTS as an incident: a session claimed something it had not verified; skipped a mandated step;
flipped a card complete too early; recorded a limitation that was not real; misread the owner's intent;
left knowledge only in chat; misused a tool or path; left records inconsistent; ignored or mis-dispositioned
a review; redid existing work; invented a number; drifted from the asked scope; read a stale doc as current truth.

WHAT DOES NOT COUNT: product bugs, test failures with no agent-behaviour story, plain feature work,
"session idea" proposals with no error behind them, generic aspiration.

RULES:
- Every incident MUST carry a verbatim quote from the shard and the exact cite from the section header.
- Never invent an incident to fill quota. A shard with few real incidents should return few.
- Prefer incidents where a session states an error concretely ("the previous session claimed X; X was false").
- error_class must come from the fixed enum. Use 'other' only when nothing fits, and say why in what_happened.
- gap_class per the estate's own taxonomy: absent (no instruction existed) | unrouted (instruction exists but
  was never delivered at the moment of action) | unenforced (delivered but nothing checked it) |
  missing-procedure (no method existed for this at all).
- trigger_moment must be an ACTION MOMENT a hook could fire on, not a vibe.

The estate already has these 7 traps registered — an incident matching one is still worth recording
(frequency evidence matters), but say so in what_happened:
TRAP-001 dated document read as current state; TRAP-002 exit code read after a pipe;
TRAP-003 absence of evidence as evidence of absence; TRAP-004 claim wider than its sample;
TRAP-005 owner corrected from memory and was right; TRAP-006 card flipped complete before branch pushed;
TRAP-007 card flipped complete while a requested review is unanswered.
`

phase('Harvest')
const N = args && args.shards ? args.shards : 68
log(`Harvesting ${N} evidence shards across 20 repos`)

const harvested = await parallel(
  Array.from({ length: N }, (_, i) => () =>
    agent(
      `Read the whole file ${SP}/shards/shard-${String(i).padStart(3,'0')}.md (use Bash: cat, or Read in chunks — read ALL of it, do not sample).
${HARVEST_RULES}
Return every genuine agent-error incident you find in this shard.`,
      { label: `harvest:${i}`, phase: 'Harvest', schema: INCIDENT, effort: 'medium' }
    )
  )
)

const all = harvested.filter(Boolean).flatMap(r => r.incidents || [])
const notes = harvested.filter(Boolean).map(r => r.shard_notes).filter(Boolean)
log(`${all.length} incidents harvested from ${harvested.filter(Boolean).length}/${N} lanes`)

// group by class — a genuine barrier: a class synthesis needs every incident of its class
const byClass = {}
for (const inc of all) {
  const k = CLASSES.includes(inc.error_class) ? inc.error_class : 'other'
  ;(byClass[k] = byClass[k] || []).push(inc)
}
const classes = Object.keys(byClass).sort((a,b) => byClass[b].length - byClass[a].length)
log(`classes present: ${classes.map(c => `${c}(${byClass[c].length})`).join(' · ')}`)

const PATTERN = {
  type: 'object',
  properties: {
    patterns: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string', description: 'short imperative name of the recurring mistake' },
      one_line: { type: 'string' },
      trigger: { type: 'string', description: 'the action moment, hook-firable' },
      why_it_happens: { type: 'string' },
      instances: { type: 'array', items: { type: 'string' }, description: 'cites, most convincing first' },
      repos: { type: 'array', items: { type: 'string' } },
      instance_count: { type: 'number' },
      repo_count: { type: 'number' },
      date_span: { type: 'string' },
      gap_class: { type: 'string', enum: ['absent','unrouted','unenforced','missing-procedure'] },
      fix_family: { type: 'string', enum: ['write','route','hook','checker','skill','chain','none'] },
      proposed_fix: { type: 'string', description: 'concrete: the checker name and predicate, the route regex, the skill step, the hook moment' },
      maps_to_existing_trap: { type: 'string', description: 'TRAP-00N or "new"' },
      severity: { type: 'string', enum: ['high','medium','low'] },
    }, required: ['name','one_line','trigger','instances','repos','instance_count','repo_count','gap_class','fix_family','proposed_fix','maps_to_existing_trap','severity'] } },
  },
  required: ['patterns'],
}

const VERDICT = {
  type: 'object',
  properties: {
    refuted: { type: 'boolean' },
    verdict: { type: 'string', enum: ['CONFIRMED','PARTIAL','REFUTED'] },
    lens: { type: 'string' },
    reasoning: { type: 'string' },
    corrections: { type: 'array', items: { type: 'string' } },
    already_covered_by: { type: 'string', description: 'existing trap id / doc-route id / kit checker filename that already handles this, or "nothing"' },
    checker_feasible: { type: 'boolean' },
  },
  required: ['refuted','verdict','reasoning','already_covered_by'],
}

// pipeline: each class synthesizes then immediately goes to its 3-lens verify
const LENSES = [
  { key: 'refute', ask: `Try hard to REFUTE that this is a real, recurring agent-error pattern. Open the cited files under ${SP}/corpus/<repo>/ and check the quotes are real and mean what the pattern claims. A pattern whose instances turn out to be one incident restated, or product bugs, or the estate's normal discipline working correctly, is REFUTED. Default to refuted=true when uncertain.` },
  { key: 'coverage', ask: `Check whether the estate ALREADY covers this. Read ${SP}/coverage-brief.md in full, plus /home/user/fleet-manager/docs/traps.md and /home/user/fleet-manager/.claude/hooks/doc-routes.json. If an existing trap, doc-route or kit checker already fires at this pattern's trigger moment, say which one and mark refuted=true (it is not a NEW finding). A trap that exists but has NO route delivering it is NOT covered — that is the estate's own definition of unfinished.` },
  { key: 'buildable', ask: `Judge whether the proposed fix is actually buildable and would have caught the cited instances. A checker must have a decidable predicate over files a session touches — if it needs judgment, say so and downgrade fix_family to skill or route. Reject fake precision (invented thresholds). refuted=true only if the pattern itself is not actionable at all.` },
]

phase('Synthesize')
const results = await pipeline(
  classes,
  (cls) => agent(
    `You are the synthesis lane for the agent-error class "${cls}".
Here are ALL ${byClass[cls].length} incidents harvested estate-wide for this class, as JSON:

${JSON.stringify(byClass[cls], null, 1).slice(0, 220000)}

Cluster them into DISTINCT recurring patterns. A pattern earns a row only if it has at least 2 named
instances (the estate's own trap-register bar) — prefer patterns spanning 2+ repos or 2+ months, and say
so in date_span. Merge near-duplicates ruthlessly; a class may yield 1 pattern or 8, never padding.
For each, name the hook-firable trigger moment and a CONCRETE fix: for a checker give the predicate and
what it reads; for a route give the regex and the doc it delivers; for a skill give the step it inserts and
into which existing skill; for a chain give the two links (skill X -> hook Y).
You may open cited files under ${SP}/corpus/<repo>/ to check an instance before asserting it.
Existing trap ids are TRAP-001..TRAP-007 (see ${SP}/coverage-brief.md) — map each pattern to one or say "new".`,
    { label: `synth:${cls}`, phase: 'Synthesize', schema: PATTERN, effort: 'high' }
  ),
  (res, cls) => parallel(
    (res && res.patterns ? res.patterns : []).map(p => () =>
      parallel(LENSES.map(L => () =>
        agent(
          `Adversarially verify this candidate agent-error pattern from the ${cls} class.

PATTERN: ${JSON.stringify(p, null, 1)}

YOUR LENS — ${L.key}: ${L.ask}

Be concrete and cite what you actually read. Return your verdict.`,
          { label: `verify:${L.key}:${(p.name||'').slice(0,28)}`, phase: 'Verify', schema: VERDICT, effort: 'high' }
        )
      )).then(vs => {
        const v = vs.filter(Boolean)
        const refuters = v.filter(x => x.refuted).length
        return {
          ...p,
          class: cls,
          verdicts: v,
          survives: v.length > 0 && refuters < 2,
          refuter_count: refuters,
          covered_by: v.map(x => x.already_covered_by).filter(x => x && x !== 'nothing'),
        }
      })
    )
  )
)

const judged = results.flat().filter(Boolean)
const survivors = judged.filter(p => p.survives)
log(`${judged.length} candidate patterns judged; ${survivors.length} survived the 3-lens panel`)

phase('Prescribe')
const PRESCRIPTION = {
  type: 'object',
  properties: {
    headline: { type: 'string' },
    top_patterns: { type: 'array', items: { type: 'object', properties: {
      rank: { type: 'number' }, name: { type: 'string' }, one_line: { type: 'string' },
      instance_count: { type: 'number' }, repo_count: { type: 'number' },
      trigger: { type: 'string' }, gap_class: { type: 'string' },
      fix: { type: 'string' }, fix_family: { type: 'string' },
      new_or_known: { type: 'string' }, best_cites: { type: 'array', items: { type: 'string' } },
    }, required: ['rank','name','one_line','trigger','fix','fix_family','new_or_known'] } },
    kit_checkers: { type: 'array', items: { type: 'object', properties: {
      filename: { type: 'string' }, predicate: { type: 'string' }, catches: { type: 'string' },
      false_positive_risk: { type: 'string' }, effort: { type: 'string' },
    }, required: ['filename','predicate','catches'] } },
    doc_routes: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, trigger_regex: { type: 'string' }, delivers: { type: 'string' }, catches: { type: 'string' },
    }, required: ['id','trigger_regex','delivers'] } },
    skills: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string' }, new_or_amend: { type: 'string' }, what_it_does: { type: 'string' },
      invoked_when: { type: 'string' }, chains_to: { type: 'string' }, why_a_skill_not_a_checker: { type: 'string' },
    }, required: ['name','new_or_amend','what_it_does','invoked_when'] } },
    chains: { type: 'array', items: { type: 'string' } },
    new_traps: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, title: { type: 'string' }, trigger: { type: 'string' },
      prevention: { type: 'string' }, verify: { type: 'string' }, origin_cites: { type: 'array', items: { type: 'string' } },
    }, required: ['id','title','trigger','prevention','verify','origin_cites'] } },
    already_covered_but_unenforced: { type: 'array', items: { type: 'string' } },
    era_finding: { type: 'string', description: 'did error rate/kind change across the eras (2026-05/06 superbot -> 07 program -> 08 stepped-back)?' },
    what_this_did_not_cover: { type: 'array', items: { type: 'string' } },
  },
  required: ['headline','top_patterns','kit_checkers','doc_routes','skills','new_traps','era_finding'],
}

const payload = JSON.stringify(survivors.map(p => ({
  class: p.class, name: p.name, one_line: p.one_line, trigger: p.trigger, why: p.why_it_happens,
  instances: (p.instances||[]).slice(0,8), repos: p.repos, n: p.instance_count, r: p.repo_count,
  span: p.date_span, gap: p.gap_class, fix_family: p.fix_family, fix: p.proposed_fix,
  trap: p.maps_to_existing_trap, sev: p.severity, covered_by: p.covered_by,
  verdicts: (p.verdicts||[]).map(v => ({ v: v.verdict, why: (v.reasoning||'').slice(0,400), cov: v.already_covered_by, feasible: v.checker_feasible })),
})), null, 1).slice(0, 400000)

const prescription = await agent(
  `You are writing the estate's substrate-kit improvement prescription from a whole-corpus agent-error audit.

CORPUS: 7,214 error-bearing sections from 4,583 session cards + findings + retros across 20 repositories,
spanning 2026-05-29 to 2026-08-28. Harvested by ${N} reader lanes, clustered per error class, and each
candidate pattern put through a 3-lens adversarial panel (refute / already-covered / buildable).

SURVIVING PATTERNS (each already survived >=2 of 3 lenses):
${payload}

Lane notes from the harvest:
${JSON.stringify(notes.slice(0, 40)).slice(0, 30000)}

Read ${SP}/coverage-brief.md and /home/user/fleet-manager/docs/traps.md before writing, so nothing you
propose duplicates what exists. The estate's own doctrine, which you must honour:
- "Records may grow; instructions may not." The fix for an unfollowed rule is a MECHANISM that delivers it
  at the right moment, never another statement of it.
- Deterministic parts in scripts, judgment in skills. A must-happen step never lives only in skill prose.
- The owner does not want new walls: default to enabling, never restrict on agent initiative.
- No fake precision: no invented thresholds or cadences.
- A trap earns a place only with >=2 named, dated instances.

Rank the top patterns by (instances x repos x severity), state plainly which are NEW versus already-known-
but-unenforced, and give the kit work as concrete buildable items. For the era_finding, say whether the
owner's "stepped back and the agents forgot their purpose" hypothesis is visible in the data or not — and
be honest if the corpus cannot answer it.`,
  { label: 'prescription', phase: 'Prescribe', schema: PRESCRIPTION, effort: 'high' }
)

const critic = await agent(
  `Completeness critic. A whole-corpus agent-error audit just produced this prescription:

${JSON.stringify(prescription, null, 1).slice(0, 200000)}

The corpus was ${SP}/shards/ (68 shards, 7,214 sections from 20 repos, 2026-05-29..2026-08-28), extracted by
a regex over section headings and an error lexicon (see ${SP}/extract.py).

Name what is MISSING: error classes the extraction regex would structurally miss; repos under-represented
(check ${SP}/census.json and the per-repo counts); claims in the prescription that rest on no cited instance;
proposed fixes that would not actually have caught their own cited instances; and the single most valuable
next audit. Be specific and short. Return prose.`,
  { label: 'completeness-critic', phase: 'Prescribe', effort: 'high' }
)

return { harvested_incidents: all.length, lanes_ok: harvested.filter(Boolean).length, lanes_total: N,
         classes: classes.map(c => [c, byClass[c].length]), candidates: judged.length,
         survivors: survivors.length, prescription, critic,
         all_judged: judged.map(p => ({ name: p.name, class: p.class, survives: p.survives,
           refuters: p.refuter_count, n: p.instance_count, r: p.repo_count, covered: p.covered_by })) }
