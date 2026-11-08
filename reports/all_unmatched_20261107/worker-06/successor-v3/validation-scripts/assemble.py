"""Assemble reviewed fragments without changing any historical or author bytes."""
from pathlib import Path
import copy, datetime, hashlib, json, shutil
R=Path('reports/all_unmatched_20261107/worker-06'); S=R/'successor-v3'; O=R/'successor-v2/final'
def read(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def dump(p,o):
 assert not Path(p).exists(),p
 Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def unique(a): return list(dict.fromkeys(a))
DD=read(O/'decisions.json'); D=DD['decisions']; OD=copy.deepcopy(D)
PP=read(O/'proposals.json'); P={p['proposal_id']:p for p in PP['proposals']}; OP=copy.deepcopy(P)
EE=read(O/'evidence.json'); E={e['evidence_id']:e for e in EE['evidence']}
index={d['case_id']:i for i,d in enumerate(D)}
A=read(S/'research-a/proposals.json')['proposals']; B=read(S/'research-b/revision-2/proposals.json')['proposals']; C=read(S/'research-c/proposals.json')['proposals']; T=read(S/'research-root/stock-proposal.json')
for p in A+C+B+[T]:P[p['proposal_id']]=p
for patch in read(S/'research-c/proposal-metadata-patches.json')['patches']:
 p=P[patch['proposal_id']]
 for k,v in patch['replace_fields'].items():p[k]=unique(p.get(k,[])+v) if k=='evidence_ids' else v
P['C-P-NZAMINE-A']['pending_coordinator_case_backlinks']=[]
for x in read(S/'research-c/decisions-v2.json')['decisions']+read(S/'research-b/revision-2/decisions.json')['decisions']:D[index[x['case_id']]]=x
for x in read(S/'research-root/stock-case-replacements.json')['replacements']:D[x['case_index']]=x['decision']
amend=read(S/'research-a/case-amendments.json')['amendments']
for a in amend:
 d=D[a['case_index']]
 for k,v in a['field_replacements'].items():
  if a['case_index']==111 and k=='applicability':d[k]+=' W06-IR-002 correction:'+v.split('W06-IR-002 correction:',1)[1]
  else:d[k]=v
 d['evidence_ids']=unique(d['evidence_ids']+a['append_evidence_ids'])
for f in ['research-a/evidence.json','research-b/revision-2/evidence.json']:
 for e in read(S/f)['evidence']:
  if e['kind']=='author_review':e['kind']='local_validation'
  assert e['evidence_id'] not in E
  E[e['evidence_id']]=e
ec=read(S/'research-c/evidence.json')
for e in ec['replacements']+ec['additions']+[read(S/'research-root/stock-evidence.json')]:E[e['evidence_id']]=e
reviewsets=[
 ('V3-IR-ALIAS','research-b/review-a/final-scientific-review.json',[a['case_index'] for a in amend],[p['proposal_id'] for p in A],'research_a','research_b','Exact eleven payload alias deltas and twenty-four case alias claims; overlap111 retains the separate receiving-source review.'),
 ('V3-IR-PRODUCT','research-a/review-b/final-scientific-review.json',[92,118,121,125,173,71,102],[p['proposal_id'] for p in B],'research_b','research_a','Four exact bounded product payloads, unchanged TypeA payload, all seven affected source outcomes and eleven qualified/unqualified KG contexts.'),
 ('V3-IR-SOURCE','research-root/review-c/final-review-v2.json',[index[d['case_id']] for d in read(S/'research-c/decisions-v2.json')['decisions']],[p['proposal_id'] for p in C],'research_c','root','Seven exact literal-membership payload corrections and fourteen complete source outcomes, plus five evidence corrections and three proposal metadata patches.'),
 ('V3-IR-STOCK-MERCK','research-a/review-v2/final-scientific-review.json',[19,133,35,183],['V2-P-NBRC1308-1356-TRACE','A-P-MERCK108339'],'root','research_a','Reconciled NBRC1308/1356 complete nominal input membership, all affected occurrence partitions, and unchanged independently reviewed Merck label correction.')]
coverage=[]
for eid,path,indices,pids,author,reviewer,scope in reviewsets:
 E[eid]={'evidence_id':eid,'kind':'independent_review','capture':{'root':'artifact','path':'successor-v3/'+path,'sha256':sha(S/path)},'url':None,'locator':'Full exact-payload and source-case scientific review receipt','supports_or_contradicts':scope+' Author and reviewer differ; previous lineage is disclosed. No whole-owner, source-release or export approval.','case_ids':[D[i]['case_id'] for i in indices]}
 coverage.append({'evidence_id':eid,'author':author,'reviewer':reviewer,'scope':scope,'case_indices':indices,'proposal_ids':pids,'review_capture':E[eid]['capture']})
 for i in indices:
  d=D[i]
  d.setdefault('prior_independent_review',copy.deepcopy(OD[i]['independent_review']))
  r=d.setdefault('successor_review_evidence_ids',[]);r.append(eid)
  d['independent_review']={'status':'complete','evidence_ids':unique(OD[i]['independent_review']['evidence_ids']+r)}
  d['successor_review_scope']='; '.join(c['scope'] for c in coverage if i in c['case_indices'])
  d['issue_refs']=unique(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/'+('1207' if i in [19,133] else '1217')])
 for pid in pids:
  p=P[pid];p['independent_review']={'status':'complete','evidence_ids':[eid]};p['successor_review_scope']=scope
changed=[i for i,(a,b) in enumerate(zip(D,OD)) if a!=b]
for c in coverage:
 c['final_case_object_sha256']={str(i):digest(D[i]) for i in c['case_indices']}
 c['final_payload_sha256']={pid:P[pid]['after_capture']['sha256'] for pid in c['proposal_ids']}
dump(S/'review-coverage.json',{'scope':'Fresh independent scientific review of changed payloads and affected source outcomes; unchanged cases retain original review. Final integration binding is separately reviewed.','review_sets':coverage,'changed_case_indices':changed,'coordinator_source_case_acceptance':'pending','whole_owner_role_export_approval':False})
DD['decisions']=D;PP['proposals']=list(P.values());EE['evidence']=list(E.values())
dump(S/'decisions.json',DD);dump(S/'proposals.json',PP);dump(S/'evidence.json',EE)
shutil.copyfile(O/'source-holds.json',S/'source-holds.json')
delta={'from_published_head':'1b3641853c7105b9091f81b5a9b19c99e8ed351e','historical_original_head':'d5a7613c931d45d057eaca7b5ec15280aca76c9e','old_core_sha256':{f:sha(O/f) for f in ['decisions.json','proposals.json','evidence.json','source-holds.json','selection.json']},'new_core_sha256':{f:sha(S/f) for f in ['decisions.json','proposals.json','evidence.json','source-holds.json']},'case_deltas':[{'case_index':i,'case_id':D[i]['case_id'],'before_object_sha256':digest(OD[i]),'after_object_sha256':digest(D[i]),'changed_fields':[k for k in set(OD[i])|set(D[i]) if OD[i].get(k)!=D[i].get(k)]} for i in changed],'proposal_deltas':[{'proposal_id':pid,'before_object_sha256':digest(OP[pid]) if pid in OP else None,'after_object_sha256':digest(p),'before_after_capture':OP[pid]['after_capture'] if pid in OP else None,'after_capture':p['after_capture'],'payload_changed':pid not in OP or OP[pid]['after_capture']['sha256']!=p['after_capture']['sha256'],'changed_metadata_fields':[k for k in set(OP.get(pid,{}))|set(p) if OP.get(pid,{}).get(k)!=p.get(k)]} for pid,p in P.items() if pid not in OP or p!=OP[pid]],'evidence_corrections':ec['replacements'],'integration_notes':['Case111 uses C corrected receiving applicability plus only A alias correction sentence.','C187 receives A alias payload while unsupported KG152 backlink is removed by C.','TypeA completed case71 backlink no longer remains pending.','B author_review evidence metadata normalized to contract local_validation; original fragment bytes retained.','EBIOS owner path denotes frozen before owner; integration_target_path denotes proposed mapped relocation. No maintained writes.']}
dump(S/'delta.json',delta)
dump(S/'selection.json',{'selection_id':'w06-successor-v3','authoritative_for':'Complete worker06 proposed intake superseding the v2 selection; all earlier evidence and selections remain historical.','based_on_published_head':delta['from_published_head'],'frozen_shard_sha256':DD['shard_sha256'],'core':{f:{'path':str(S/f),'sha256':sha(S/f)} for f in ['decisions.json','proposals.json','evidence.json','source-holds.json']},'case_count':len(D),'proposal_count':len(P),'evidence_count':len(E),'frozen_cm_occurrence_count':sum(len(d['occurrence_ids']) for d in D),'frozen_downstream_hold_count':88,'changed_payloads':[x for x in delta['proposal_deltas'] if x['payload_changed']],'review_coverage':{'path':str(S/'review-coverage.json'),'sha256':sha(S/'review-coverage.json')},'delta':{'path':str(S/'delta.json'),'sha256':sha(S/'delta.json')},'coordinator_source_case_acceptance':'pending independent re-review','whole_owner_role_export_approval':False,'maintained_application':False})
print('Assembled',len(D),'cases',len(P),'proposals',len(E),'evidence;',len(changed),'changed case metadata;',sum(x['payload_changed'] for x in delta['proposal_deltas']),'new/changed payloads')
