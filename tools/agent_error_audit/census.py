import json, os, urllib.request, ssl, concurrent.futures
PAT=os.environ['GITHUB_PAT']
ctx=ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
OPENER=urllib.request.build_opener(urllib.request.ProxyHandler({}), urllib.request.HTTPSHandler(context=ctx))
def api(url):
    req=urllib.request.Request(url, headers={'Authorization':f'Bearer {PAT}','Accept':'application/vnd.github+json'})
    return json.load(OPENER.open(req, timeout=60))
repos=[r for r in json.load(open('repos.json'))]
def one(r):
    name=r['full_name']; br=r['default_branch']
    try:
        t=api(f"https://api.github.com/repos/{name}/git/trees/{br}?recursive=1")
    except Exception as e:
        return (name, br, 'ERR '+str(e)[:60], 0,0,0,0)
    paths=[x['path'] for x in t.get('tree',[]) if x['type']=='blob']
    cards=[p for p in paths if p.startswith('.sessions/') and p.endswith('.md') and 'README' not in p]
    findings=[p for p in paths if p.startswith('docs/findings/') and p.endswith('.md')]
    retro=[p for p in paths if '/retro' in p or p.startswith('docs/retro')]
    return (name, br, 'ok' if not t.get('truncated') else 'TRUNCATED', len(paths), len(cards), len(findings), len(retro))
with concurrent.futures.ThreadPoolExecutor(16) as ex:
    rows=list(ex.map(one, repos))
rows.sort(key=lambda x:-x[4])
print(f"{'repo':32}{'branch':10}{'state':12}{'files':>7}{'cards':>7}{'findings':>10}{'retro':>7}")
tot=0
for n,b,s,f,c,fi,re_ in rows:
    print(f"{n.split('/')[1]:32}{b:10}{s:12}{f:7}{c:7}{fi:10}{re_:7}")
    tot+=c
print("TOTAL CARDS:", tot)
json.dump([{'repo':n,'branch':b,'state':s,'files':f,'cards':c,'findings':fi} for n,b,s,f,c,fi,_ in rows], open('census.json','w'), indent=1)
