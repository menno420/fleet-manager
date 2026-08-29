import json, re, os, collections
rows=[json.loads(l) for l in open('evidence.jsonl')]
DATE=re.compile(r'(20\d\d-\d\d-\d\d)')
for r in rows:
    m=DATE.search(r['file']) or DATE.search(r['text'][:300])
    r['date']=m.group(1) if m else ''
    r['tier']=1 if r['section_match'] else 2
    r['weight']=len(r['text'])
rows.sort(key=lambda r:(r['tier'], r['repo'], r['file'], r['line']))
os.makedirs('shards', exist_ok=True)
# pack into shards of ~140k chars each
shards=[]; cur=[]; w=0
for r in rows:
    if w + r['weight'] > 140000 and cur:
        shards.append(cur); cur=[]; w=0
    cur.append(r); w+=r['weight']
if cur: shards.append(cur)
for i,s in enumerate(shards):
    with open(f'shards/shard-{i:03d}.md','w') as f:
        f.write(f"# Evidence shard {i:03d} — {len(s)} sections from session cards / findings\n\n")
        for r in s:
            f.write(f"\n---\n## [{r['repo']}] {r['file']}:{r['line']} · date={r['date'] or 'unknown'} · section: {r['section']}\n\n{r['text']}\n")
print('shards:', len(shards))
print('tier1 sections:', sum(1 for r in rows if r['tier']==1), '| tier2:', sum(1 for r in rows if r['tier']==2))
print('date range:', min((r['date'] for r in rows if r['date']), default='?'), '→', max((r['date'] for r in rows if r['date']), default='?'))
c=collections.Counter(r['date'][:7] for r in rows if r['date'])
print('by month:', dict(sorted(c.items())))
json.dump([len(s) for s in shards], open('shard_sizes.json','w'))
