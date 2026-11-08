from pathlib import Path
import json, yaml,hashlib,re,copy,datetime,subprocess,collections
R=Path.cwd(); A=R/'reports/all_unmatched_20261107/worker-10'; S=A/'successor-v3';P=R/'.temp/all-unmatched-worker-10/successor-v3/skeptic'
def rd(p):return json.loads(Path(p).read_text())
def sh(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ca(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
checks=[]
def ck(n,v):checks.append({'check':n,'pass':bool(v)})
def df(a,b,p=''):
 if type(a)!=type(b):return [p]
 if isinstance(a,dict):return sum([df(a.get(k),b.get(k),p+'/'+k) for k in set(a)|set(b)],[])
 if isinstance(a,list):return [p+'/length'] if len(a)!=len(b) else sum([df(x,y,p+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))],[])
 return [] if a==b else [p]
dec=rd(S/'decisions.json')['decisions'];props=rd(S/'proposals.json')['proposals'];pm={p['proposal_id']:p for p in props};dm={d['case_id']:d for d in dec}
snap=rd(S/'reviews/skeptic/support/final-full-payload-snapshots-v2.json')['records'];sm={r['proposal_id']:r for r in snap}
oldps=rd(A/'successor-v2/proposals.json')['proposals'];opm={p['proposal_id']:p for p in oldps}
for fname,key,idkey,allowed,expected in [('decisions.json','decisions','case_id',{'independent_review','final_successor_review'},18),('proposals.json','proposals','proposal_id',{'independent_review','review_status_explanation'},101)]:
 before={x[idkey]:x for x in rd(S/'assembly-v1'/fname)[key]};after={x[idkey]:x for x in rd(S/fname)[key]};changes=0
 ck('same object universe '+fname,set(before)==set(after))
 for ident,x in after.items():
  fields={k for k in set(before[ident])|set(x) if before[ident].get(k)!=x.get(k)}
  ck('only reviewed metadata finalization '+ident,fields<=allowed)
  if fields:changes+=1;ck('complete bounded review status '+ident,x['independent_review']['status']=='complete')
 ck('expected finalization count '+fname,changes==expected)
before=rd(S/'assembly-v1/evidence.json')['evidence'];after=rd(S/'evidence.json')['evidence'];bm={x['evidence_id']:x for x in before};am={x['evidence_id']:x for x in after}
ck('one review evidence appended',len(after)==len(before)+1 and set(am)-set(bm)=={'sv3-independent-source-provenance'})
for i,x in bm.items():ck('original evidence exact '+i,x==am[i])
for p in props:
 c=p['after_capture'];ck('bound final capture '+p['proposal_id'],c==sm[p['proposal_id']]['capture'] and sh(A/c['path'])==c['sha256'])
 for cid in p['case_ids']:ck('final backlink '+p['proposal_id']+cid,p['proposal_id'] in dm[cid]['proposal_ids'])
sel=rd(S/'selection.json');ck('selection count',len(sel['selected_payloads'])==127)
for x in sel['selected_payloads']:
 p=pm[x['proposal_id']]
 ck('complete exact selected row '+x['proposal_id'],x['owner_path']==p['owner_path'] and x['destination_path']==p.get('destination_path',p['owner_path']) and x['before_sha256']==p.get('before_sha256') and x['after_capture']==p['after_capture'] and x['case_ids']==p['case_ids'])
for f,h in sel['authoritative_core'].items():ck('selection core hash '+f,sh(S/f)==h)
bridge=rd(S/'retirement-bridge.json')['rows'];ck('all128 retired/retained history rows',len(bridge)==128 and {r['old_proposal_id'] for r in bridge}==set(opm))
for x in bridge:
 old=opm[x['old_proposal_id']];ck('full original proposal retained '+x['old_proposal_id'],old==x['historical_proposal'] and ca(old)==x['old_proposal_sha256'])
 pid=x['selected_proposal_id']
 if pid:ck('bridge actual final proposal '+pid,ca(pm[pid])==x['selected_proposal_object_sha256'] and pm[pid]['after_capture']==x['selected_payload'] and pm[pid]['case_ids']==x['selected_case_ids'])
 else:ck('only calf retired without replacement',x['old_proposal_id']=='sv1-kg-calf-serum1303')
native_path=R/'reviews/structured/20261108T075320Z-w10-family-provenance-successor/review.yaml';n=yaml.safe_load(native_path.read_text());v2=yaml.safe_load((S/'native-v2/review-input.yaml').read_text());v1=yaml.safe_load((S/'native/review-input.yaml').read_text())
ck('saved native exact input',n==v2)
ck('native correction only declared four fields',set(df(v1,v2))=={'/review_id','/finished_at','/findings/2/ownership_note','/actions/2/ownership_note'})
for x in n['source']['inputs']:ck('native source hash '+x['path'],sh(R/x['path'])==x['sha256'])
expected=set(dm)|{'PROPOSAL:'+pid for pid in pm};nt={x['target_id']:x for x in n['targets']};na={x['target_ids'][0]:x for x in n['assessments']}
ck('315 targets/assessments/exact scope',len(n['targets'])==len(n['assessments'])==315 and set(nt)==set(na)==set(n['scope']['reviewed_target_ids'])==expected)
for i,t in nt.items():
 a=na[i]
 if i.startswith('PROPOSAL:'):
  pid=i[9:];p=pm[pid];ck('native proposal payload target '+pid,R/t['path']==A/p['after_capture']['path'])
  sr=sm[pid]
  ck('native proposal area '+pid,a['area']==('representation' if sr['scientific_correction'] else 'provenance'))
  expectprefix='Complete corrected payload scientifically read' if sr['scientific_correction'] else 'Complete final payload read for claim-specific provenance/context' if sr['metadata_correction'] else 'Exact unchanged selected payload'
  ck('native proposal actual scope '+pid,a['summary'].startswith(expectprefix) and p['description'] in a['summary'])
  ck('native ownership scope '+pid,'no maintained preimage' in t['ownership_note'] if p['kind']=='new_owner' else 'preimage' in t['ownership_note'])
 else:
  d=dm[i];ix=int(re.fullmatch(r'\$\.cases\[(\d+)\]',t['selector']).group(1));obj=rd(R/t['path'])['cases'][ix]
  ck('native exact original case selector '+str(ix),obj['case_id']==i and ca(obj)==d['case_input_sha256'] and ix==d['source_index'])
  science=ix in rd(S/'accounting.json')['fresh_scientific_case_indices'];ck('case assessment scope '+str(ix),a['area']==('identity' if science else 'provenance') and d['reasoning'] in a['summary'])
ck('five open findings and actions',len(n['findings'])==len(n['actions'])==5 and all(x['status']=='open' for x in n['findings']))
for f in n['findings']:ck('finding target scope '+f['finding_id'],set(f['target_ids'])<=expected)
for f in n['actions']:ck('action target scope '+f['action_id'],set(f['target_ids'])<=expected)
for p in ['native-v2/validate-command.json','native-v2/save-command.json','structural-command.json']:ck('actual validation exit '+p,rd(S/p)['exit_code']==0)
ck('failed native predecessor preserved',rd(S/'native/validate-command.json')['exit_code']!=0 and 'requires maintained owner paths or an explicit ownership limit' in (S/'native/validate.stderr').read_text())
for x in rd(S/'native-v2/saved-pair.json')['files']:ck('saved pair hash '+x['path'],sh(R/x['path'])==x['sha256'])
head=subprocess.run(['git','rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip();ck('published source head unchanged',head=='808ff934f9cdec7ad8fdc8cdcaa583f1ae068d5e')
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':sh(__file__),'source_head':head,'checks':checks,'check_count':len(checks),'failures':[x for x in checks if not x['pass']],'native_hash':sh(native_path),'final_core_hashes':{p:sh(S/p) for p in ['decisions.json','evidence.json','proposals.json','selection.json','retirement-bridge.json','accounting.json']},'metadata_correction_paths':df(v1,v2),'note':'Independent exact final core/native metadata check. Handoff and preservation receipts reviewed separately when available. Does not renew source-scientific scope or approve any future published head.'}
(P/'assembly-checks-v1.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
