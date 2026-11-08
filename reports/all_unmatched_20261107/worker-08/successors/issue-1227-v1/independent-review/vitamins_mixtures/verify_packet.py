import hashlib,json,sys,subprocess,datetime,re
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
B=Path('reports/all_unmatched_20261107/worker-08');S=B/'successors/issue-1227-v1';M=S/'research/vitamins_mixtures';R=S/'independent-review/vitamins_mixtures';version=sys.argv[1]
def read(p):return json.loads(p.read_text())
def rows(p,k):
 x=read(p);return x[k] if isinstance(x,dict)else x
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lp(name):return M/version/name if (M/version/name).exists() else M/name
def canon(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
A=read(M/'assignment.json');P=rows(M/version/'proposals.json','proposals');D=rows(M/version/'decisions.json','decisions');old={p['proposal_id']:p for p in A['proposals']};oldD={d['case_id']:d for d in A['decisions']};checks=[];payloads=[]
def ck(n,v,detail=None):
 checks.append(dict(check=n,pass_=bool(v),detail=detail))
ck('exact assignment cases and proposals',set(A['case_ids'])=={d['case_id']for d in D}and set(A['proposal_ids'])=={p['proposal_id']for p in P}and len(P)==47 and len(D)==57)
for p in P:
 f=B/p['after_capture']['path'];d=yaml.safe_load(f.read_text());z=yaml.safe_load((B/old[p['proposal_id']]['after_capture']['path']).read_text());errors=list(map(str,validate_ingredient(d)))
 ck(p['proposal_id']+' hash/schema/preimage contract',sha(f)==p['after_capture']['sha256']and not errors and all(p[k]==old[p['proposal_id']][k]for k in ['proposal_id','kind','owner_path','before_sha256','case_ids']),errors)
 ck(p['proposal_id']+' history prefix and holds-bearing unchanged fields',d.get('curation_history',[])[:len(z.get('curation_history',[]))]==z.get('curation_history',[])and all(d.get(k)==z.get(k)for k in ['roles','community_organism_roles','nutritional_roles','physicochemical_roles','cellular_metabolic_roles','causal_graphs','occurrence_statistics','chemical_properties']))
 if p['before_sha256']:
  actual=Path(p['owner_path']);ck(p['proposal_id']+' maintained preimage hash',sha(actual)==p['before_sha256'])
 payloads.append({'proposal_id':p['proposal_id'],'capture':p['after_capture'],'before_sha256':p['before_sha256'],'component_count':len(d.get('components',[])),'identity':d['identifier'],'full_fields':sorted(d),'schema_errors':errors})
for d in D:
 z=oldD[d['case_id']];ck(d['case_id']+' frozen source occurrence and native holds',all(d.get(k)==z.get(k)for k in ['case_input_sha256','source','occurrence_ids','preserved_native_decisions','owner_records','proposal_ids','disposition','missing_requirement','no_change_reason']))
# Including ignored files: pathlib does not consult gitignore.
base={str(f):yaml.safe_load(f.read_text())for f in Path('data/ingredients').rglob('*.yaml')};overlay=dict(base);selected={p['proposal_id']:p for p in rows(B/'successors/issue-1201-v1/proposals.json','proposals')}
for cohort,fn in [('inorganic_forms','proposals.json'),('organic_products','proposals-v3.json')]:
 selected.update({p['proposal_id']:p for p in rows(S/'research'/cohort/fn,'proposals')})
selected.update({p['proposal_id']:p for p in P})
inv=[]
for p in selected.values():
 f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];d=yaml.safe_load(f.read_text());overlay[p['owner_path']]=d
 inv.append(dict(proposal_id=p['proposal_id'],owner_path=p['owner_path'],capture=p['after_capture'],identifier=d['identifier'],preferred_term=d['preferred_term'],component_signature=[{k:c.get(k)for k in ['component_name','component_id','reference_scope','concentration_value','concentration_unit']}for c in d.get('components',[])]))
part=list(map(str,validate_component_partonomy(overlay.values())));ck('all113 combined selected overlay native partonomy',len(selected)==113 and not part,part)
for pid in ['vm-prop-jcm403-b12','vm-prop-linsmaier-skoog']:
 p=next(x for x in P if x['proposal_id']==pid);rec=overlay[p['owner_path']];collision=[f for f,d in overlay.items()if f!=p['owner_path']and d.get('mapping_status')!='REJECTED'and d.get('identifier')==rec['identifier']];ck(pid+' promotion primary identifier collision',not collision,collision)
# Duplicate inventory by source, label and formula candidates. No universal absence claim.
candidates=[]
for f,d in base.items():
 if re.search(r'linsmaier|l0230|vitamin.?b.?12.*solution|vitamin.*403|cyanocobalamin',json.dumps(d,ensure_ascii=False),re.I):candidates.append(dict(path=f,sha256=sha(Path(f)),identifier=d.get('identifier'),preferred_term=d.get('preferred_term'),status=d.get('mapping_status'),components=d.get('components',[])))
for dep in read(lp('conditional-component-dependencies.json'))+[read(lp('conditional-deionized-water-dependency.json'))]:
 target=selected[dep['target_proposal_id']];ck('conditional dependency '+dep['source_proposal_id'],dep['target_after_capture']['sha256']==target['after_capture']['sha256'] and sha(B/dep['target_after_capture']['path'])==dep['target_after_capture']['sha256'])
# Verify evidence files independently; successful hashes are integrity, not proof of reading.
evidence={e['evidence_id']:e for e in rows(B/'successors/issue-1201-v1/evidence.json','evidence')};evidence.update({e['evidence_id']:e for e in rows(M/version/'evidence-additions.json','evidence')});ids={i for d in D for i in d['evidence_ids']}|{i for p in P for i in p['evidence_ids']};caps=[];src=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
for i in sorted(ids):
 e=evidence[i];c=e['capture'];f=(B if c['root']=='artifact'else src)/c['path'];ok=f.exists()and sha(f)==c['sha256'];caps.append(dict(evidence_id=i,capture=c,hash_valid=ok,kind=e.get('kind'),locator=e.get('locator'),url=e.get('url')));ck('capture '+i,ok)
result=dict(version=version,reviewer='/root/organics',author='/root/vitamins',at=datetime.datetime.now(datetime.timezone.utc).isoformat(),checks=checks,failures=[c for c in checks if not c['pass_']],payloads=payloads,case_hashes={d['case_id']:canon(d)for d in D},payload_hashes={p['proposal_id']:p['after_capture']['sha256']for p in P},input_hashes={str((M/version/f).relative_to(B)):sha(M/version/f)for f in ['decisions.json','proposals.json','evidence-additions.json']},catalog_count=len(base),overlay_records=len(overlay),partonomy_violations=part,scientific_approval=False)
(R/(version+'-independent-validation.json')).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');(R/(version+'-selected-duplicate-inventory.json')).write_text(json.dumps({'ignored_files_included':True,'selected':inv,'maintained_candidates':candidates},indent=2,ensure_ascii=False)+'\n');(R/(version+'-capture-integrity.json')).write_text(json.dumps(caps,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'version':version,'cases':len(D),'proposals':len(P),'checks':len(checks),'failures':result['failures'],'catalog_records':len(base),'overlay_records':len(overlay),'captures':len(caps)}))
