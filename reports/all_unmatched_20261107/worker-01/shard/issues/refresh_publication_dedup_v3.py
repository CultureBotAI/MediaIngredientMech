import pathlib,json,datetime,hashlib,subprocess,concurrent.futures
O=pathlib.Path('reports/all_unmatched_20261107/worker-01/shard/issues');C=O/'captures'
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
tasks=[]
for repo,nums in [('CultureBotAI/CultureMech',[408]),('CultureBotAI/MediaIngredientMech',[718,318,1159,1163,1164,1166,1167,1168]),('Knowledge-Graph-Hub/kg-microbe',[1319,1824,788,5,380,572,1668])]:
 for n in nums:tasks.append((repo.split('/')[-1]+'-'+str(n)+'-publication-v3',['gh','issue','view',str(n),'--repo',repo,'--json','number,title,state,url,body,comments,updatedAt,closedAt']))
queries={
 'kg-exact-source-ids':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "mediadive.ingredient:572" OR "mediadive.ingredient:2389"',
 'kg-source-572':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "572" "thiosulfate"',
 'kg-source-2389':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "2389" "water"',
 'kg-dsmz559-thiosulfate':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "559" "thiosulfate"',
 'kg-water-choice':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "distilled or tapwater"',
 'kg-source-fingerprint':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "10543" OR "1667" OR "DSMZ589"',
 'kg-thiosulfate-label':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "thiosulfate"',
 'kg-water-choice-alt':'repo:Knowledge-Graph-Hub/kg-microbe is:issue "distilled or tap"',
 'mim-source-fingerprint':'repo:CultureBotAI/MediaIngredientMech is:issue "mediadive.ingredient:572" OR "mediadive.ingredient:2389"',
}
for name,q in queries.items():tasks.append((name+'-publication-v3',['gh','api','--method','GET','search/issues','-f','q='+q,'-f','per_page=100']))
def run(item):
 name,cmd=item;p=C/(name+'.json');assert not p.exists();start=now();r=subprocess.run(cmd,capture_output=True,text=True,timeout=60);body={'command':cmd,'accessed_at':start,'completed_at':now(),'exit_code':r.returncode,'stderr':r.stderr}
 try:body['response']=json.loads(r.stdout)
 except json.JSONDecodeError:body['stdout']=r.stdout
 p.write_text(json.dumps(body,ensure_ascii=False,indent=2)+'\n');return dict(name=name,path=str(p),sha256=sha(p),exit_code=r.returncode,accessed_at=start,response_summary={k:body.get('response',{}).get(k) for k in ['number','state','total_count','incomplete_results']})
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(run,tasks))
out=O/'publication-dedup-live-v3.json';assert not out.exists();out.write_text(json.dumps(dict(at=now(),captures=results,all_commands_read_only=True,query_scope='Exact source IDs, source names, unusual quantities and known nearest trackers. Per search cap100; inspect total_count/incomplete_results before making absence claims.'),indent=2)+'\n')
print(json.dumps(results,indent=2));assert all(x['exit_code']==0 for x in results)
