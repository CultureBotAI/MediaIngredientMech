"""Combine reviewed source decisions without changing their scientific content.
Every fragment and independent-review manifest is checked before metadata enrichment.
"""
from pathlib import Path
import json,hashlib,datetime,copy
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-05';Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');S=Q/'shards/shard-05.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
config=json.loads((O/'review-bindings.json').read_text());cases=json.loads(S.read_text())['cases'];by={c['case_id']:c for c in cases};D=[];E=[];P=[];rows=[]
for group,rb in config.items():
 original=json.loads((O/group/'decisions.json').read_text())['decisions'];ev=json.loads((O/group/'evidence.json').read_text())['evidence'];pro=json.loads((O/group/'proposals.json').read_text())['proposals'];rp=O/rb['review_path'];review=json.loads(rp.read_text())
 # Bind exact review inputs explicitly; normalized bindings are curator-authored from actual reviewer manifests.
 actual_inputs=review.get('reviewed_inputs',review.get('input_hashes'))
 if isinstance(actual_inputs,list):actual_inputs={Path(i['path']).name:i['sha256'] for i in actual_inputs}
 assert actual_inputs==rb['reviewed_fragment_hashes'], (group,'binding does not match reviewer manifest')
 for filename,h in actual_inputs.items():assert sha(O/group/filename)==h,(group,filename,'stale independent review')
 assert review['reviewer']==rb['reviewer'] and rb['reviewer']!=rb['primary_author']
 if 'open_findings' in review:assert review['open_findings']==0
 else:assert review.get('review_status',review.get('status'))=='complete', (group,'actual reviewer has open findings')
 case_reviews=review[rb['case_list_key']];reviewids={r['case_id'] for r in case_reviews};assert len(reviewids)==len(case_reviews)
 assert reviewids=={d['case_id'] for d in original},(group,'review scope mismatch')
 authored={d['case_id']:d for d in original}
 for cr in case_reviews:
  assert cr.get('status')=='complete' or cr.get('verdict')=='supported_with_limits', (group,cr['case_id'],'case not reviewed')
  if cr.get('case_input_sha256'):assert cr['case_input_sha256']==digest(by[cr['case_id']])
 assert rb['review_status']=='complete'
 eid='INDEPENDENT-'+group.upper();E.append({'evidence_id':eid,'kind':'independent_review','capture':{'root':'artifact','path':rb['review_path'],'sha256':sha(rp)},'url':None,'locator':rb['case_list_key']+' keyed by case_id; final reviewed inputs and findings resolutions','supports_or_contradicts':'Separate skeptical review by '+rb['reviewer']+' of all '+str(len(original))+' assigned '+group+' cases and exact proposed deltas; no source/owner/export approval.','case_ids':sorted(reviewids)})
 for d0 in original:
  d=copy.deepcopy(d0);c=by[d['case_id']];assert d['case_input_sha256']==digest(c)
  d['independent_review']={'status':'complete','evidence_ids':[eid]};d['authored_fragment_decision_sha256']=digest(d0);d['primary_author']=rb['primary_author']
  kg=c.get('original_kg_entry',{});d['preserved_source_holds']={'policy':'All existing source/material/owner/export holds remain. Scope is source-bound assessment and isolated proposal; no release admission.','downstream_holds':copy.deepcopy(kg.get('downstream_holds',[])),'consumed_name_hits':copy.deepcopy(kg.get('consumed_name_hits',[])),'native_review_rows':copy.deepcopy(kg.get('native_review_rows',[])),'owners':copy.deepcopy(kg.get('owners',[]))}
  # The original case digest also binds every other embedded historical field.
  if any(p in d['proposal_ids'] for p in ['MATERIALS-P-bacto-aliases','MATERIALS-P-proteose-numbered']):d['issue_refs'].append('https://github.com/CultureBotAI/MediaIngredientMech/issues/1176')
  if 'MATERIALS-P-sea-salts-identity' in d['proposal_ids']:d['issue_refs'].append('https://github.com/CultureBotAI/MediaIngredientMech/issues/1177')
  extra=O/'issues/created-fatty.json'
  if 'ROOT-P-fatty-stock' in d['proposal_ids'] and extra.exists():d['issue_refs'].append(json.loads(extra.read_text())['stdout'].strip())
  d['issue_refs']=list(dict.fromkeys(d['issue_refs']));D.append(d)
 E+=ev;P+=pro;rows.append({'agent':rb['primary_author'],'primary_count':len(original),'independent_reviewer':rb['reviewer'],'independent_count':len(case_reviews),'review_capture':rb['review_path'],'review_sha256':sha(rp),'reviewed_fragment_hashes':rb['reviewed_fragment_hashes'],'case_ids':sorted(reviewids)})
assert len(D)==len(by)==188 and {d['case_id'] for d in D}==set(by)
assert len({e['evidence_id'] for e in E})==len(E)
assert len({p['proposal_id'] for p in P})==len(P)
D.sort(key=lambda d:list(by).index(d['case_id']))
for name,data in [('decisions',{'schema_version':1,'worker_slot':5,'shard_sha256':sha(S),'phase':'shard','decisions':D}),('evidence',{'schema_version':1,'evidence':E}),('proposals',{'schema_version':1,'proposals':P})]:(O/(name+'.json')).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
scopes=json.loads((O/'subagent-scopes.json').read_text());scopes['completed_actual_scopes']=rows;scopes['external_sessions_launched_by_this_worker']=0;(O/'subagent-scopes.json').write_text(json.dumps(scopes,indent=2,ensure_ascii=False)+'\n')
progress=json.loads((O/'progress.json').read_text());progress.update(reviewed_case_ids=list(by),remaining_case_ids=[],reviewed_count=len(D),remaining_count=0,phase='final_validation',current_task='All cases independently reviewed; whole-shard structural audit and native formal persistence pending.',updated_at=datetime.datetime.now(datetime.timezone.utc).isoformat());(O/'progress.json').write_text(json.dumps(progress,indent=2)+'\n')
receipt={'assembled_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'case_count':len(D),'evidence_count':len(E),'proposal_count':len(P),'review_binding_sha256':sha(O/'review-bindings.json'),'metadata_only_changes':['independent_review','authored_fragment_decision_sha256','primary_author','preserved_source_holds','deduplicated issue_refs'],'scientific_assessment_changes':'none; exact authored decision digest retained','group_review_receipts':rows};(O/'validation/assembly.json').write_text(json.dumps(receipt,indent=2)+'\n');print(len(D),len(E),len(P))
