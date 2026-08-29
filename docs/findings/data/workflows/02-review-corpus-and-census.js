export const meta = {
  name: 'external-review-error-audit',
  description: 'Mine 1,592 PR review comments (Codex + the owner) and the 20 repos instruction surfaces for agent-error patterns and enforcement gaps',
  phases: [
    { title: 'Owner', detail: '3 lanes over the 155 comments the owner wrote himself' },
    { title: 'Codex', detail: '9 lanes over 1,437 external review findings' },
    { title: 'Census', detail: 'per-repo instruction-vs-enforcement surface census' },
    { title: 'Cluster', detail: 'patterns per error class, adversarially verified' },
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
      cite: { type: 'string', description: 'repo PR #N and the comment URL' },
      date: { type: 'string' },
      what_the_agent_did_wrong: { type: 'string' },
      quote: { type: 'string', description: 'verbatim from the review comment, <=240 chars' },
      error_class: { type: 'string', enum: CLASSES },
      gap_class: { type: 'string', enum: ['absent','unrouted','unenforced','missing-procedure'] },
      trigger_moment: { type: 'string' },
      would_a_checker_catch_it: { type: 'string' },
      severity: { type: 'string', enum: ['high','medium','low'] },
      owner_voice: { type: 'boolean', description: 'true if the comment is the OWNER correcting the agent, not a bot' },
    }, required: ['cite','what_the_agent_did_wrong','quote','error_class','gap_class','trigger_moment','severity','owner_voice'] } },
    lane_notes: { type: 'string' },
  },
  required: ['incidents'],
}

const RULES = `
Each entry is a REVIEW COMMENT on a pull request written by an AI coding session. This is an
INDEPENDENT record of agent error: something a reviewer caught in work the agent had already
declared finished. Sections are separated by "---" with repo, PR number, date, author, file and URL.

For each comment that identifies a real agent mistake, record one incident.
- Classify what the AGENT did wrong, not what the reviewer said in the abstract.
- The 'quote' must be verbatim from the comment.
- Skip pure style nits with no behavioural story, and skip comments that are the agent's own replies.
- gap_class: absent (no rule existed) | unrouted (a rule exists somewhere but was not delivered at the
  moment of action) | unenforced (delivered but nothing mechanically checked it) | missing-procedure.
- trigger_moment must be an action moment a hook could fire on.
- would_a_checker_catch_it: name the decidable predicate, or say "judgment only".

The estate already registers 7 traps: TRAP-001 dated doc read as current state · TRAP-002 exit code after
a pipe · TRAP-003 absence of evidence as evidence of absence · TRAP-004 claim wider than its sample ·
TRAP-005 the owner corrected from memory and was right · TRAP-006 card flipped complete before push ·
TRAP-007 card flipped complete while a requested review is unanswered. Recording a match is still useful.
`

phase('Owner')
log('3 lanes over the 155 review comments the OWNER wrote himself — the highest-signal source')
const ownerLanes = await parallel([1,2,3].map(i => () =>
  agent(
    `Read ALL of ${SP}/rshards/owner-0${i}.md (cat it; read every comment).
${RULES}

THIS SHARD IS SPECIAL: every comment is written by the OWNER (menno420) reviewing his agents' work.
Set owner_voice=true. Pay attention to what he repeatedly corrects, what he asks for that he did not get,
where he expresses frustration, and where he states a preference agents keep missing. Also record, in
lane_notes, his recurring VOCABULARY and the things he asks for that no rule in the estate captures.`,
    { label: `owner:${i}`, phase: 'Owner', schema: INCIDENT, effort: 'high' }
  )
))

phase('Codex')
const codexLanes = await parallel(Array.from({length: 9}, (_, i) => () =>
  agent(
    `Read ALL of ${SP}/rshards/codex-0${i}.md (cat it; read every comment).
${RULES}

These are external reviewer findings on agent PRs. Set owner_voice=false unless the comment is clearly
the owner's. Be selective: a shard of 150 findings might yield 20-40 genuine agent-error incidents.`,
    { label: `codex:${i}`, phase: 'Codex', schema: INCIDENT, effort: 'medium' }
  )
))

const CENSUS = {
  type: 'object',
  properties: {
    repo: { type: 'string' },
    instructs: { type: 'array', items: { type: 'string' }, description: 'what this repo tells agents to do that is specific to it' },
    enforcement: { type: 'array', items: { type: 'object', properties: {
      mechanism: { type: 'string' }, kind: { type: 'string', enum: ['hook','checker','ci','prose-only','none'] },
      what_it_catches: { type: 'string' } }, required: ['mechanism','kind','what_it_catches'] } },
    prose_only_rules: { type: 'array', items: { type: 'string' }, description: 'rules stated but with NO mechanism delivering or checking them' },
    kit_version: { type: 'string' },
    divergences_from_kit: { type: 'array', items: { type: 'string' }, description: 'local edits to kit-shipped skills/checkers that would be lost on upgrade' },
    biggest_gap: { type: 'string' },
    portable_lesson: { type: 'string', description: 'something this repo does that the KIT should ship to everyone' },
  },
  required: ['repo','instructs','enforcement','prose_only_rules','biggest_gap','portable_lesson'],
}

phase('Census')
const REPOS = ['fleet-manager','superbot','substrate-kit','superbot-next','websites','sim-lab',
  'idea-engine','venture-lab','gba-homebrew','spider-swing','superbot-games','trading-strategy',
  'superbot-idle','superbot-mineverse','pokemon-mod-lab','shiftlife','product-forge','couch-legend',
  'spider-bot','creator-kit']
const census = await parallel(REPOS.map(r => () =>
  agent(
    `Census the agent-instruction surface of the repo "${r}".
Its files are on disk at ${SP}/corpus/${r}/ — read CLAUDE.md, everything under .claude/ (hooks, settings,
skills, doc-routes), docs/current-state.md, docs/PROJECT-CLOSEOUT.md, docs/traps* if present, and enough
of .sessions/ (list it, read the 3 most recent cards) to see what discipline actually runs there.
For fleet-manager also read /home/user/fleet-manager/.claude/ directly — it is the live checkout.

Answer: what does this repo INSTRUCT agents to do, and what MECHANISM actually enforces each instruction?
The distinction that matters is prose-only (a rule stated in a doc, delivered by nothing, checked by
nothing) versus routed (a hook injects it at the moment of action) versus checked (a script fails on it).
List the rules that are prose-only — those are the estate's unenforced surface.
Also note any LOCAL edits to substrate-kit-shipped skills or checkers that an upgrade would revert.
If the repo has no such surface at all, say so plainly rather than inventing one.`,
    { label: `census:${r}`, phase: 'Census', schema: CENSUS, effort: 'medium' }
  )
))

const all = [...ownerLanes, ...codexLanes].filter(Boolean).flatMap(r => r.incidents || [])
const ownerIncidents = all.filter(i => i.owner_voice)
log(`${all.length} incidents from review comments (${ownerIncidents.length} in the owner's own voice)`)

const byClass = {}
for (const inc of all) {
  const k = CLASSES.includes(inc.error_class) ? inc.error_class : 'other'
  ;(byClass[k] = byClass[k] || []).push(inc)
}
const classes = Object.keys(byClass).sort((a,b) => byClass[b].length - byClass[a].length)
log(`classes: ${classes.map(c => `${c}(${byClass[c].length})`).join(' · ')}`)

const PATTERN = {
  type: 'object',
  properties: {
    patterns: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string' }, one_line: { type: 'string' }, trigger: { type: 'string' },
      why_it_happens: { type: 'string' },
      instances: { type: 'array', items: { type: 'string' } },
      repos: { type: 'array', items: { type: 'string' } },
      instance_count: { type: 'number' }, repo_count: { type: 'number' },
      owner_flagged: { type: 'boolean', description: 'did the OWNER himself flag this, not just a bot' },
      date_span: { type: 'string' },
      gap_class: { type: 'string', enum: ['absent','unrouted','unenforced','missing-procedure'] },
      fix_family: { type: 'string', enum: ['write','route','hook','checker','skill','chain','none'] },
      proposed_fix: { type: 'string' },
      maps_to_existing_trap: { type: 'string' },
      severity: { type: 'string', enum: ['high','medium','low'] },
    }, required: ['name','one_line','trigger','instances','repos','instance_count','repo_count','owner_flagged','gap_class','fix_family','proposed_fix','maps_to_existing_trap','severity'] } },
  },
  required: ['patterns'],
}

const VERDICT = {
  type: 'object',
  properties: {
    refuted: { type: 'boolean' },
    verdict: { type: 'string', enum: ['CONFIRMED','PARTIAL','REFUTED'] },
    reasoning: { type: 'string' },
    already_covered_by: { type: 'string' },
    checker_feasible: { type: 'boolean' },
    corrections: { type: 'array', items: { type: 'string' } },
  },
  required: ['refuted','verdict','reasoning','already_covered_by'],
}

const LENSES = [
  `Try to REFUTE that this is a real recurring agent-error pattern. Fetch one or two of the cited comment URLs with curl (direct egress: curl -sS --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" <api url>) or find them in ${SP}/rshards/ and check the quote is real and means what is claimed. Reviewer findings are sometimes wrong, and an agent's [survived] disposition may have been correct. Default refuted=true if uncertain.`,
  `Check whether the estate ALREADY covers this: read ${SP}/coverage-brief.md, /home/user/fleet-manager/docs/traps.md and /home/user/fleet-manager/.claude/hooks/doc-routes.json. If an existing trap, route or kit checker fires at this trigger moment, name it and set refuted=true. A trap with no delivering route is NOT covered.`,
  `Judge buildability: would the proposed fix have caught the cited instances, and is its predicate decidable over files a session touches? Reject invented thresholds. Downgrade to skill/route if it needs judgment. refuted=true only if not actionable at all.`,
]

phase('Cluster')
const results = await pipeline(
  classes,
  (cls) => agent(
    `Synthesis lane for agent-error class "${cls}", from EXTERNAL REVIEW evidence (PR review comments).
All ${byClass[cls].length} incidents in this class:

${JSON.stringify(byClass[cls], null, 1).slice(0, 220000)}

Cluster into distinct recurring patterns, minimum 2 named instances each. Weight patterns the OWNER
flagged above bot-only ones and set owner_flagged accordingly. Give each a hook-firable trigger and a
concrete fix (checker predicate / route regex / skill step / chain links). Map to TRAP-001..007 or "new".`,
    { label: `synth:${cls}`, phase: 'Cluster', schema: PATTERN, effort: 'high' }
  ),
  (res, cls) => parallel(
    (res && res.patterns ? res.patterns : []).map(p => () =>
      parallel(LENSES.map((ask, li) => () =>
        agent(
          `Adversarially verify this pattern from the ${cls} class.\n\nPATTERN: ${JSON.stringify(p, null, 1)}\n\nYOUR LENS: ${ask}`,
          { label: `verify:${li}:${(p.name||'').slice(0,26)}`, phase: 'Cluster', schema: VERDICT, effort: 'high' }
        )
      )).then(vs => {
        const v = vs.filter(Boolean)
        const refuters = v.filter(x => x.refuted).length
        return { ...p, class: cls, verdicts: v, survives: v.length > 0 && refuters < 2,
                 refuter_count: refuters, covered_by: v.map(x => x.already_covered_by).filter(x => x && x !== 'nothing') }
      })
    )
  )
)

const judged = results.flat().filter(Boolean)
const survivors = judged.filter(p => p.survives)
log(`${judged.length} patterns judged; ${survivors.length} survived`)

return {
  source: 'external-review + instruction census',
  incidents: all.length, owner_incidents: ownerIncidents.length,
  owner_notes: ownerLanes.filter(Boolean).map(r => r.lane_notes).filter(Boolean),
  codex_notes: codexLanes.filter(Boolean).map(r => r.lane_notes).filter(Boolean),
  classes: classes.map(c => [c, byClass[c].length]),
  survivors, all_judged: judged.map(p => ({ name: p.name, class: p.class, survives: p.survives,
    refuters: p.refuter_count, n: p.instance_count, r: p.repo_count, owner: p.owner_flagged, covered: p.covered_by })),
  census: census.filter(Boolean),
}
