"""Bind exact author-separated successor reviews; preserve every frozen source case/hold."""
from pathlib import Path
import json,hashlib,datetime,copy
R=Path.cwd();B=R/'reports/all_unmatched_20261107/worker-05';O=B/'correction-1193-v1';Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');S=Q/'shards/shard-05.json';(O/'validation').mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
config=json.loads((O/'review-bindings.json').read_text());cases=json.loads(S.read_text())['cases'];by={c['case_id']:c for c in cases};D=[];E=[];P=[];rows=[]
old={d['case_id']:d for d in json.loads((B/'decisions.json').read_text())['decisions']}
for group,rb in config.items():
 original=json.loads((O/group/'decisions.json').read_text())['decisions'];ev=json.loads((O/group/'evidence.json').read_text())['evidence'];pro=json.loads((O/group/'proposals.json').read_text())['proposals'];rp=B/rb['review_path'];review=json.loads(rp.read_text())
 actual=review.get('reviewed_inputs',review.get('input_hashes'))
 if isinstance(actual,list):actual={Path(i['path']).name:i['sha256'] for i in actual}
 assert actual==rb['reviewed_fragment_hashes'],(group,'Review binding does not match actual manifest')
 assert set(actual)=={'decisions.json','evidence.json','proposals.json'}
 for f,h in actual.items():assert sha(O/group/f)==h,(group,f,'Stale independent review')
 assert review['reviewer']==rb['reviewer']!=rb['primary_author'],(group,'Reviewer is not author-separated')
 unresolved=review.get('open_findings')
 assert unresolved==0 or (isinstance(unresolved,list) and len(unresolved)==0),(group,'Open or uncounted review findings')
 assert review.get('status',review.get('review_status')) in {'complete','PASS'},(group,'Reviewer status incomplete')
 cr=review[rb['case_list_key']];assert len({x['case_id'] for x in cr})==len(cr)
 assert {x['case_id'] for x in cr}=={d['case_id'] for d in original},(group,'Review coverage mismatch')
 assert all(x.get('status') in {'complete','supported_with_stated_limits'} for x in cr),(group,'Case review not complete')
 eid='C1193-INDEPENDENT-'+group.upper();E.append({'evidence_id':eid,'kind':'independent_review','capture':{'root':'artifact','path':rb['review_path'],'sha256':sha(rp)},'url':None,'locator':rb['case_list_key']+' keyed by unchanged case_id; exact final reviewed inputs','supports_or_contradicts':'Separate skeptical review by '+rb['reviewer']+'; all scientific changed/unchanged dispositions and final proposals assessed with explicit limits. No owner/export approval.','case_ids':sorted(x['case_id'] for x in cr)})
 for a in original:
  d=copy.deepcopy(a);c=by[d['case_id']];assert d['case_input_sha256']==digest(c)
  assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}
  rr=d.get('correction_reassessment',d.get('reassessment',{}))
  if 'status' in rr:assert rr['status']=='complete',(group,d['case_id'],'Individual reassessment incomplete')
  else:assert rr.get('classification') and rr.get('actual_searches'),(group,d['case_id'],'No individual scientific reassessment')
  d['correction_reassessment']={**copy.deepcopy(rr),'status':'complete','author_field':'correction_reassessment' if 'correction_reassessment' in a else 'reassessment'}
  assert d['proposal_ids'] or d['no_change_reason'],(group,d['case_id'],'Missing exact action or scientific reason')
  d['independent_review']={'status':'complete','evidence_ids':[eid]};d['authored_fragment_decision_sha256']=digest(a);d['primary_author']=rb['primary_author'];kg=c.get('original_kg_entry',{})
  d['preserved_source_holds']={'policy':'All existing source/material/owner/export holds remain. Source-bound reassessment and isolated proposal only; no release admission.','downstream_holds':copy.deepcopy(kg.get('downstream_holds',[])),'consumed_name_hits':copy.deepcopy(kg.get('consumed_name_hits',[])),'native_review_rows':copy.deepcopy(kg.get('native_review_rows',[])),'owners':copy.deepcopy(kg.get('owners',[]))}
  d['predecessor_decision_sha256']=digest(old[d['case_id']]);d['issue_refs']=list(dict.fromkeys(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1193']));D.append(d)
 E+=ev;P+=pro;rows.append({'primary_author':rb['primary_author'],'independent_reviewer':rb['reviewer'],'primary_count':len(original),'independent_count':len(cr),'case_ids':sorted(x['case_id'] for x in cr),'review_path':rb['review_path'],'review_sha256':sha(rp),'reviewed_fragment_hashes':actual})
assert len(D)==len(by)==188 and {d['case_id'] for d in D}==set(by)
# Exact shared captures can back two primary scopes; conflicting provenance under one ID fails.
em={};dedup=[]
for e in E:
 if e['evidence_id'] in em:
  assert em[e['evidence_id']]==e,('Conflicting duplicate evidence',e['evidence_id']);dedup.append(e['evidence_id'])
 else:em[e['evidence_id']]=e
E=list(em.values());assert len({p['proposal_id'] for p in P})==len(P);assert len({p['owner_path'] for p in P})==len(P),'Multiple final proposals for one owner'
dm={d['case_id']:d for d in D};pm={p['proposal_id']:p for p in P}
for p in P:
 for cid in p['case_ids']:
  assert p['proposal_id'] in dm[cid]['proposal_ids'],('Missing decision backlink',p['proposal_id'],cid)
  if p['kind']=='edit_existing_owner':assert any(o['path']==p['owner_path'] and o['sha256']==p['before_sha256'] for o in dm[cid]['owner_records']),('Unbound actual owner',p['proposal_id'],cid)
for d in D:
 for pid in d['proposal_ids']:assert d['case_id'] in pm[pid]['case_ids'],('Missing proposal backlink',pid)
assert sum(not x['proposal_ids'] for x in old.values())==159
D.sort(key=lambda x:list(by).index(x['case_id']))
for name,data in [('decisions',{'schema_version':1,'worker_slot':5,'shard_sha256':sha(S),'phase':'shard','decisions':D}),('evidence',{'schema_version':1,'evidence':E}),('proposals',{'schema_version':1,'proposals':P})]:(O/(name+'.json')).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
receipt={'assembled_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'case_count':len(D),'prior_no_change_count':159,'reassessed_prior_no_change_count':sum(bool(dm[cid]['correction_reassessment']) for cid,x in old.items() if not x['proposal_ids']),'current_no_change_count':sum(not d['proposal_ids'] for d in D),'current_proposal_case_count':sum(bool(d['proposal_ids']) for d in D),'evidence_count':len(E),'proposal_count':len(P),'exact_shared_evidence_ids_deduplicated':dedup,'review_bindings_sha256':sha(O/'review-bindings.json'),'group_review_receipts':rows,'scientific_changes_at_assembly':'None; metadata-only review/hold/backlink binding; exact authored fragment digest retained.'}
(O/'validation/assembly.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k not in ['group_review_receipts']},indent=2))
