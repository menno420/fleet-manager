export const meta = {
  name: 'eap-false-done-ledger',
  description: 'Read the EAP fortnight corpus (superbot docs/eap + fleet-manager EAP docs) and build the false-done ledger: every claim of done/complete/shipped, matched against what was later found true',
  phases: [
    { title: 'Read', detail: 'one reader per file (48: 32 superbot docs/eap, 16 fleet-manager EAP docs), split any file over 400 lines by line range' },
    { title: 'Merge', detail: 'correlate claims against corrections across all readers into ledger rows' },
    { title: 'Verify', detail: 'two refuting lenses per row (holds? real false-done, not just plan evolution or already-known?); same survival rule as Fleet A' },
    { title: 'Critic', detail: 'completeness critic — what was not read, what looks thin' },
  ],
}

// ---- aggregation contract (fleet-preflight § 1) — asserted before any agent spawns, same rule as Fleet A (04-eap-mail-evidence-pass.js)
const dies = (a, b) => (a.refuted || b.refuted) || (Boolean(a.already_covered_by) && Boolean(b.already_covered_by))
const FIX = [
  [{ refuted: true,  already_covered_by: '' }, { refuted: false, already_covered_by: '' }, true ],
  [{ refuted: false, already_covered_by: 'traps.md TRAP-006' }, { refuted: false, already_covered_by: 'redirect doc' }, true ],
  [{ refuted: false, already_covered_by: '' }, { refuted: false, already_covered_by: '' }, false ],
]
for (const [a, b, exp] of FIX) { if (dies(a, b) !== exp) throw new Error('aggregation fixture failed') }
log('aggregation fixtures: 2 kill, 1 survive — pass; fields read: refuted, already_covered_by')

const FM = (typeof args === 'object' && args && args.fm) || '/home/user/fleet-manager'
const SB = (typeof args === 'object' && args && args.sb) || '/tmp/eap-night/superbot-eap'
const JUDGE_MODEL = (typeof args === 'object' && args && args.judgeModel) || undefined
log(`paths: fm=${FM} sb=${SB} · verify/critic model=${JUDGE_MODEL || 'session default'}`)

const TASK = `You are one reader in a multi-agent pass building a FALSE-DONE LEDGER for Menno's estate: a table of every claim of "done" / "complete" / "shipped" / "working" / "finished" / "landed" made during the EAP fortnight (July 2026, the Anthropic Early Access Program on the /superbot production Discord bot), matched against what was later found to actually be true. This is not the mail-evidence pass (a sibling fleet handles that) — this fleet's ONLY product is the ledger. The owner's own words about this: "I noticed that much of the work that was claimed to be complete was in fact not complete at all." Turn that sentence into countable rows.`

const READ_RULES = `READING RULES (non-negotiable):
- Read the WHOLE file (or your assigned line range) in slices: sed -n '1,220p' FILE, then '221,440p', and so on until past the last line (or the end of your assigned range). Never rely on head, grep -l, or a listing to characterise content.
- Copy every claim and every correction VERBATIM or near-verbatim with its exact citation. Never paraphrase away the specific words ("done", "complete", "shipped", "working", "fixed", "resolved", "landed", "ready") that make it a done-claim.
- Copy every number verbatim with its stated method, date and unit. Never round, never recompute.
- Certainty: report the tag the source itself uses (MEASURED / MEASURED-PRIOR / OWNER / REASONED / REVIEWED / UNVERIFIED / DERIVED) or "unstated".
- Citations are FILE:LINE-RANGE of what you actually read. Do not cite anything you did not open.
- Do not write, create or modify any file. Read only. Your final message must be the structured output only.`

const READER_B = { type: 'object', required: ['source', 'date', 'method', 'claims', 'corrections', 'self_stated_limits'], properties: {
  source: { type: 'string' }, date: { type: 'string' }, method: { type: 'string' },
  claims: { type: 'array', items: { type: 'object', required: ['statement', 'citation', 'date_stated', 'certainty'], properties: {
    statement: { type: 'string' }, citation: { type: 'string' }, date_stated: { type: 'string' }, certainty: { type: 'string' },
    topic: { type: 'string' } } } },
  corrections: { type: 'array', items: { type: 'object', required: ['statement', 'citation', 'date_stated', 'certainty', 'refers_to'], properties: {
    statement: { type: 'string' }, citation: { type: 'string' }, date_stated: { type: 'string' }, certainty: { type: 'string' },
    refers_to: { type: 'string' }, topic: { type: 'string' } } } },
  self_stated_limits: { type: 'array', items: { type: 'string' } } } }

const ROW = { type: 'object', required: ['id', 'claim', 'claimed_where', 'claimed_when', 'actually', 'found_when', 'found_by', 'citation_claim', 'citation_found'], properties: {
  id: { type: 'string' }, claim: { type: 'string' }, claimed_where: { type: 'string' }, claimed_when: { type: 'string' },
  actually: { type: 'string' }, found_when: { type: 'string' }, found_by: { type: 'string' },
  citation_claim: { type: 'string' }, citation_found: { type: 'string' }, certainty: { type: 'string' } } }

const ROWS = { type: 'object', required: ['rows', 'orphaned_corrections'], properties: {
  rows: { type: 'array', items: ROW },
  orphaned_corrections: { type: 'array', items: { type: 'object', required: ['statement', 'citation', 'reason'], properties: {
    statement: { type: 'string' }, citation: { type: 'string' }, reason: { type: 'string' } } } } } }

const VERDICT = { type: 'object', required: ['refuted', 'already_covered_by', 'what_i_opened', 'discrepancies', 'corrected_claim'], properties: {
  refuted: { type: 'boolean' }, already_covered_by: { type: 'string' }, what_i_opened: { type: 'array', items: { type: 'string' } },
  discrepancies: { type: 'array', items: { type: 'string' } }, corrected_claim: { type: 'string' } } }

const CRITIC = { type: 'object', required: ['missing_sources', 'unverified_claims', 'overlap_unchecked', 'other_gaps'], properties: {
  missing_sources: { type: 'array', items: { type: 'string' } }, unverified_claims: { type: 'array', items: { type: 'string' } },
  overlap_unchecked: { type: 'array', items: { type: 'string' } }, other_gaps: { type: 'array', items: { type: 'string' } } } }

function readerPrompt(path, range, note) {
  const rangeNote = range ? ` Read ONLY lines ${range[0]}-${range[1]} (this file is split across two readers; a sibling reads the rest) — read that slice in full with sed -n.` : ' Read the whole file.'
  return `${TASK}
Your source: ${path}.${rangeNote} ${note || ''}
Extract two things, separately:
1. CLAIMS — every place the source asserts something is done / complete / shipped / working / finished / landed / resolved / ready, with the exact statement, its citation, the date it was made (from the file's own date or header if the line has none), and topic (one or two words, e.g. "automerger", "watch-filter", "classifier").
2. CORRECTIONS — every place the source says something was actually still broken/incomplete/wrong, retracts or corrects an earlier claim, or reports something "found later" / "turned out" / "still not" / "actually" — with the exact statement, citation, date, topic, and refers_to (in your own words, what earlier claim this corrects, if the source says or implies it — otherwise "unstated").
A single file may contain BOTH a claim and its own later correction (a retrospective often does). Extract every instance of each, do not summarise them together.
${READ_RULES}`
}

// ---------------- Phase 1: readers — one per file, split files over 400 lines ----------------
phase('Read')
const SB_FILES = [
  { path: `${SB}/fleet-manifest.md` }, { path: `${SB}/gen1-wrapup-email-part1-questions-2026-07-09.md` },
  { path: `${SB}/NEXT-SESSION-finalize-email.md` }, { path: `${SB}/codex-review-round-verification-2026-07-10.md` },
  { path: `${SB}/2026-07-18-dewall-capabilities-evidence.md` }, { path: `${SB}/anthropic-email-4-classifier-regression-sent-2026-07-16.md` },
  { path: `${SB}/2026-07-18-followup-email-draft.md` }, { path: `${SB}/fleet-overnight-review-2026-07-10.md` },
  { path: `${SB}/session-handoff-2026-07-11-fleet-management.md` }, { path: `${SB}/gen1-wrapup-email-draft-v2-2026-07-09.md` },
  { path: `${SB}/superbot-next-runtime-review-2026-07-10.md` }, { path: `${SB}/README.md` },
  { path: `${SB}/anthropic-email-3-draft-2026-07-13.md` }, { path: `${SB}/night-review-2026-07-12.md` },
  { path: `${SB}/eap-program-review-2026-07-10.md` }, { path: `${SB}/campaign-self-audit-2026-07-08.md` },
  { path: `${SB}/fleet-winddown-audit-2026-07-09.md` }, { path: `${SB}/night-review-2026-07-11.md` },
  { path: `${SB}/fleet-review-2026-07-09.md` }, { path: `${SB}/email-attachment-set-2026-07-12.md` },
  { path: `${SB}/fleet-cleanup-audit-2026-07-13.md` }, { path: `${SB}/hostile-audit-checking-the-checkers-2026-07-10.md` },
  { path: `${SB}/fleet-quality-review-2026-07-09.md` }, { path: `${SB}/night-review-2026-07-13.md` },
  { path: `${SB}/permission-classifier-findings-consolidated-2026-07-16.md` }, { path: `${SB}/gen1-gen2-doctrine-review-2026-07-10.md` },
  { path: `${SB}/gen1-grand-review-2026-07-09.md` }, { path: `${SB}/external-review-pack-2026-07-09.md` },
  { path: `${SB}/gen1-wrapup-email-final-candidate.md`, split: [[1, 220], [221, 425]] },
  { path: `${SB}/anthropic-email-2-draft-2026-07-11.md`, split: [[1, 310], [311, 608]] },
]
const FM_FILES = [
  { path: `${FM}/docs/eap-audit-collection.md` }, { path: `${FM}/docs/eap-final-recon-2026-07-14.md` },
  { path: `${FM}/docs/fleet-inconsistencies-2026-07-13.md` }, { path: `${FM}/docs/pr-landing-audit-2026-07-16.md` },
  { path: `${FM}/docs/audits/eap-project-audit-2026-07-14.md` }, { path: `${FM}/docs/fleet-account-2026-07-26.md` },
  { path: `${FM}/docs/eap-story.md`, split: [[1, 300], [301, 580]] },
  { path: `${FM}/docs/eap-retrospective.md`, split: [[1, 220], [221, 427]] },
  { path: `${FM}/docs/launch-readiness-2026-07-10.md`, split: [[1, 360], [361, 710]] },
  { path: `${FM}/docs/dispatch-log.md`, split: [[1, 340], [341, 671]] },
  { path: `${FM}/docs/PROJECT-CLOSEOUT.md`, split: [[1, 210], [211, 414]] },
]

function expand(files, tag) {
  const out = []
  for (const f of files) {
    if (f.split) f.split.forEach((r, i) => out.push({ path: f.path, range: r, label: `${tag}:${f.path.split('/').pop()}[${r[0]}-${r[1]}]` }))
    else out.push({ path: f.path, range: null, label: `${tag}:${f.path.split('/').pop()}` })
  }
  return out
}
const SB_UNITS = expand(SB_FILES, 'sb')
const FM_UNITS = expand(FM_FILES, 'fm')
log(`reader units: superbot ${SB_UNITS.length} (from ${SB_FILES.length} files) · fleet-manager ${FM_UNITS.length} (from ${FM_FILES.length} files)`)

const fmReads = parallel(FM_UNITS.map(u => () => agent(readerPrompt(u.path, u.range, 'This is a fleet-manager estate record about the EAP fortnight.'), { label: u.label, phase: 'Read', schema: READER_B })))
const sbReads = parallel(SB_UNITS.map(u => () => agent(readerPrompt(u.path, u.range, 'This is a superbot docs/eap record, written live during the EAP fortnight.'), { label: u.label, phase: 'Read', schema: READER_B })))
const [fmOutRaw, sbOutRaw] = await Promise.all([fmReads, sbReads])
const fmOut = fmOutRaw.filter(Boolean), sbOut = sbOutRaw.filter(Boolean)
log(`readers: fleet-manager ${fmOut.length}/${FM_UNITS.length} · superbot ${sbOut.length}/${SB_UNITS.length}`)
if (fmOut.length < FM_UNITS.length) log(`DROPPED fm units: ${FM_UNITS.filter((u, i) => !fmOutRaw[i]).map(u => u.label).join(', ')}`)
if (sbOut.length < SB_UNITS.length) log(`DROPPED sb units: ${SB_UNITS.filter((u, i) => !sbOutRaw[i]).map(u => u.label).join(', ')}`)
const allReaders = [...fmOut, ...sbOut]
const totalClaims = allReaders.reduce((n, r) => n + r.claims.length, 0)
const totalCorrections = allReaders.reduce((n, r) => n + r.corrections.length, 0)
log(`extracted: ${totalClaims} claims, ${totalCorrections} corrections across ${allReaders.length} reader units`)

// ---------------- Phase 2: merge (barrier is correct: correlate claims × corrections across ALL readers) ----------------
phase('Merge')
const mergeRules = `Rules: a ledger ROW requires BOTH a claim (something asserted done/complete/shipped) AND a correction that reverses or qualifies it (found still broken, incomplete, wrong, or retracted) — from the same topic, even if from different files or different dates. Match by topic and by what the statements are actually about, not just by shared keywords. claimed_where/claimed_when/citation_claim come from the claim; actually/found_when/found_by/citation_found come from the correction (found_by = who/what found it — a named audit, a named session, the owner, a specific review round — copy from the correction's context, or "unstated" if the source does not say). Copy statements close to verbatim; do not soften "done" into "attempted" or invent a false-done where the source only shows normal iteration (a plan that was always described as in-progress, then finished, is NOT a false-done). A claim with no correction anywhere in the pool is NOT a row — do not manufacture one. A correction with no matching claim anywhere in the pool goes into orphaned_corrections with a reason (e.g. "no earlier done-claim found in this corpus for this topic"). Do not open files; work only from the extractions. Final message: the structured output only.`
const claimPool = allReaders.flatMap(r => r.claims.map(c => ({ ...c, source: r.source })))
const correctionPool = allReaders.flatMap(r => r.corrections.map(c => ({ ...c, source: r.source })))
log(`pool: ${claimPool.length} claims, ${correctionPool.length} corrections`)

// split correction pool into groups; each merge group gets the FULL claim pool (it must search across all claims) plus its own slice of corrections
const CHUNK = 25
const corrGroups = []
for (let i = 0; i < correctionPool.length; i += CHUNK) corrGroups.push(correctionPool.slice(i, i + CHUNK))
if (corrGroups.length === 0) corrGroups.push([])
log(`merge groups: ${corrGroups.length} × up to ${CHUNK} corrections, each searched against all ${claimPool.length} claims`)

const mergeParts = (await parallel(corrGroups.map((g, gi) => () =>
  agent(`${TASK}
You build ledger ROWS for group ${gi + 1} of ${corrGroups.length} of the corrections pool below, by finding each one's matching earlier claim in the FULL claims pool. Produce at most 25 rows (ids R${gi + 1}-1..R${gi + 1}-25).
${mergeRules}
CORRECTIONS (this group): ${JSON.stringify(g)}
FULL CLAIMS POOL (search this for matches): ${JSON.stringify(claimPool)}`,
    { label: `merge R${gi + 1}: corrections → rows`, phase: 'Merge', schema: ROWS, model: JUDGE_MODEL })))).filter(Boolean)

const mergedRows = mergeParts.flatMap(m => m.rows || [])
const orphaned = mergeParts.flatMap(m => m.orphaned_corrections || [])
log(`merged: ${mergedRows.length} candidate rows, ${orphaned.length} orphaned corrections`)

const dedup = await agent(`${TASK}
Deduplicate and rank the candidate ledger rows below (produced by ${corrGroups.length} parallel merge groups, so the same false-done may appear more than once from different angles). Return one ranked list of at most 30 rows: merge any two describing the same underlying false-done (keep both citations), rank by how clearly it shows a "claimed done, actually not" pattern with a solid citation on both sides. Drop nothing silently — a row you drop must still appear, marked with certainty "dropped" and the reason in the actually field.
ROWS: ${JSON.stringify(mergedRows)}
Do not open files. Final message: the structured output only.`, { label: 'dedupe + rank rows', phase: 'Merge', schema: ROWS, model: JUDGE_MODEL })
const ranked = (dedup && dedup.rows ? dedup.rows : []).filter(Boolean)
const toVerify = ranked.filter(r => r.certainty !== 'dropped').slice(0, 30)
log(`ranked ${ranked.length}; verifying ${toVerify.length}`)

// ---------------- Phase 3: verify (pipelined; two refuting lenses per row, same rule as Fleet A) ----------------
phase('Verify')
function verifyHolds(r) {
  return `You are an adversarial verifier for a false-done ledger row. Your job is to REFUTE this row if it does not hold. Default to refuted=true when you cannot confirm it from the cited lines.
ROW: ${JSON.stringify(r)}
Open BOTH citations (citation_claim and citation_found) under ${FM} or ${SB} with sed -n. Check: does citation_claim actually assert the thing was done/complete/shipped, in those words or unmistakably that meaning? Does citation_found actually show it was NOT true, contradicting or correcting the claim? Read to the end of the paragraph or section for a qualifier that reverses the read. Are the dates right (claimed_when before found_when)? If the row is essentially right but a date, a citation line, or a word is off, set refuted=false and put the exact fix in corrected_claim. Leave already_covered_by empty unless you personally find this exact false-done already named in docs/traps.md (TRAP-006, TRAP-007) or docs/planning/2026-08-30-fresh-start-redirect.md's "what killed the last rebuild" section — then name it. Read only; never write. Final message: the structured output only.`
}
function verifyFit(r) {
  return `You are an adversarial verifier for a false-done ledger row, with the FIT lens: refute (refuted=true) if this is NOT actually a false-done — e.g. it is normal iterative design (a plan always described as in-progress that later finished on schedule), the "claim" was already hedged/scoped honestly at the time, the "correction" is a routine follow-on rather than a retraction, or the dates don't support claimed-before-found. Also check: is this the SAME pattern already named in docs/traps.md or the fresh-start-redirect doc's account of the failed rebuild? If so put that file in already_covered_by (it still belongs in the ledger, but marked as already-known plumbing, not a fresh finding). List every file you opened in what_i_opened.
ROW: ${JSON.stringify(r)}
Read only; never write. Final message: the structured output only.`
}
const verified = await pipeline(toVerify,
  r => parallel([() => agent(verifyHolds(r), { label: `holds? ${r.id}`, phase: 'Verify', schema: VERDICT, effort: 'high', model: JUDGE_MODEL }),
                 () => agent(verifyFit(r), { label: `fit? ${r.id}`, phase: 'Verify', schema: VERDICT, effort: 'high', model: JUDGE_MODEL })]),
  (vs, r) => {
    const [a, b] = vs
    if (!a || !b) return { row: r, a, b, survives: false, reason: 'a verifier returned null' }
    const d = dies(a, b)
    return { row: r, a, b, survives: !d, reason: d ? (a.refuted || b.refuted ? 'refuted' : 'already covered per both lenses') : 'survives' }
  })
const results = verified.filter(Boolean)
const survivors = results.filter(r => r.survives)
log(`verify: ${survivors.length}/${results.length} survive · refuted ${results.filter(r => r.reason === 'refuted').length} · covered ${results.filter(r => r.reason.startsWith('already')).length}`)

// ---------------- Phase 4: completeness critic ----------------
phase('Critic')
const critic = await agent(`You are the completeness critic for a multi-agent pass building the EAP false-done ledger. Below is what was read, what survived verification, and what was dropped. Say what is MISSING: sources under ${FM}/docs (EAP-related) or ${SB} that should have been read and were not; surviving rows whose verification looks thin (a verifier that opened nothing, or a corrected_claim that changes the row's meaning); orphaned corrections that plausibly DO have a matching claim somewhere the merge missed; and any other gap. Be concrete and short.
READ: fleet-manager ${JSON.stringify(FM_FILES.map(f => f.path))} · superbot ${JSON.stringify(SB_FILES.map(f => f.path))}
SURVIVORS: ${JSON.stringify(survivors.map(r => ({ id: r.row.id, claim: r.row.claim, actually: r.row.actually })))}
NON-SURVIVORS: ${JSON.stringify(results.filter(r => !r.survives).map(r => ({ id: r.row.id, claim: r.row.claim, reason: r.reason })))}
ORPHANED CORRECTIONS: ${JSON.stringify(orphaned)}
Read only; never write. Final message: the structured output only.`, { label: 'completeness critic', phase: 'Critic', schema: CRITIC, effort: 'high', model: JUDGE_MODEL })

return {
  contract: 'see 05-CONTRACTS-night.md beside this script',
  counts: { fm_units: FM_UNITS.length, sb_units: SB_UNITS.length, fm_ok: fmOut.length, sb_ok: sbOut.length,
    claims: claimPool.length, corrections: correctionPool.length, merged: mergedRows.length, orphaned: orphaned.length,
    ranked: ranked.length, verified: results.length, survivors: survivors.length },
  readers: allReaders,
  ranked,
  verified: results,
  orphaned_corrections: orphaned,
  critic,
}
