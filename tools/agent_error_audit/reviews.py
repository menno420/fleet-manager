import json, os, urllib.request, ssl, re, concurrent.futures, collections
PAT=os.environ['GITHUB_PAT']
ctx=ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
OP=urllib.request.build_opener(urllib.request.ProxyHandler({}), urllib.request.HTTPSHandler(context=ctx))
def get(u):
    r=urllib.request.Request(u, headers={'Authorization':f'Bearer {PAT}','Accept':'application/vnd.github+json'})
    resp=OP.open(r, timeout=90); return json.load(resp), resp.headers.get('Link','')
def pages(base):
    out=[]; p=1
    while True:
        d,link=get(f"{base}{'&' if '?' in base else '?'}per_page=100&page={p}")
        if not d: break
        out+=d
        if 'rel="next"' not in link: break
        p+=1
        if p>40: break
    return out
REPOS=['fleet-manager','superbot','superbot-next','websites','couch-legend','substrate-kit',
       'idea-engine','product-forge','superbot-mineverse','gba-homebrew','sim-lab','venture-lab']
def one(r):
    try:
        c=pages(f"https://api.github.com/repos/menno420/{r}/pulls/comments?sort=created&direction=asc")
        return r,c
    except Exception as e:
        return r,[('ERR',str(e))]
res={}
with concurrent.futures.ThreadPoolExecutor(8) as ex:
    for r,c in ex.map(one, REPOS): res[r]=c
tot=0
rows=[]
for r,cs in res.items():
    n=0
    for c in cs:
        if not isinstance(c,dict): continue
        body=(c.get('body') or '').strip()
        if not body: continue
        rows.append({'repo':r,'pr':int(re.search(r'/pull/(\d+)',c.get('html_url','/pull/0')).group(1)) if '/pull/' in c.get('html_url','') else 0,
                     'user':(c.get('user') or {}).get('login',''),'created':c.get('created_at','')[:10],
                     'path':c.get('path',''),'url':c.get('html_url',''),'body':body[:4000]})
        n+=1
    tot+=n; print(f"{r:22}{n}")
print("TOTAL comments:", tot)
print("by author:", collections.Counter(x['user'] for x in rows).most_common(12))
json.dump(rows, open('review_comments.json','w'))
print("chars:", sum(len(x['body']) for x in rows))
