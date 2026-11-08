"""Bind separately reviewed successor fragments without editing predecessor artifacts."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,collections,shutil
R=Path.cwd();P=R/'reports/all_unmatched_20261107/worker-10';S=P/'successor-v1';Q=R.parents[2]/'queue/preliminary-v5'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
load=lambda f:json.loads(f.read_text())
def dump(f,x):f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
cap=lambda f:{'root':'artifact','path':str(f.relative_to(P)),'sha256':sha(f)}
C=load(Q/'shards/shard-10.json')['cases'];old=load(P/'decisions.json');D=copy.deepcopy(old);E=load(P/'evidence.json');PR=load(P/'proposals.json');parts=load(S/'assigned-no-proposal-cohort.json')['partitions'];reviews=load(S/'reviews/final-review-bindings.json');scopes=[]
for part,indices in parts.items():
 f=S/part;ds=load(f/'decisions.json')['decisions'];ps=load(f/'proposals.json')['proposals'];es=load(f/'evidence.json')['evidence'];rev=S/reviews[part]['path'];r=load(rev)
 assert len(ds)==len(indices);assert set(d['case_id'] for d in ds)=={C[i]['case_id'] for i in indices}
 # Reviewer-specific complete status and exact input hashes checked by final binding manifest.
 for name,h in reviews[part]['input_hashes'].items():assert sha(f/name)==h,(part,name)
 eid='sv1-independent-'+part
 E['evidence'].append({'evidence_id':eid,'kind':'independent_review','capture':cap(rev),'url':None,'accessed_at':reviews[part]['reviewed_at'],'locator':'All explicitly listed case and payload assessments plus author input hashes and remediation findings','supports_or_contradicts':'Separate skeptical reviewer assessed every final case/payload in '+part+'; bounded acceptance does not authorize maintained curation or release.'})
 E['evidence']+=es;PR['proposals']+=ps
 by={d['case_id']:d for d in ds}
 for i in indices:
  d=copy.deepcopy(by[C[i]['case_id']]);assert not old['decisions'][i]['proposal_ids'];d['independent_review']={'status':'complete','evidence_ids':[eid]};d.setdefault('no_change_reason',None if d['proposal_ids'] else d['reasoning']);d['disposition']='malformed_or_nonchemical_token' if d['disposition']=='malformed' else d['disposition'];d.setdefault('missing_requirement',None);D['decisions'][i]=d
 scopes.append({'partition':part,'author':reviews[part]['author'],'skeptical_reviewer':reviews[part]['reviewer'],'case_indices':indices,'case_ids':[C[i]['case_id'] for i in indices],'author_fragment_hashes':{n:sha(f/n) for n in ['decisions.json','evidence.json','proposals.json']},'proposals':[{k:p[k] for k in ['proposal_id','owner_path','before_sha256','after_capture']} for p in ps],'independent_review':cap(rev),'actual_scope':'Complete sourcecase assessment and isolated payload review; source-specific limitations/holds retained; no role or export approval.'})
# One independently reviewed cross-partition source-specific shared payload.
for d in D['decisions']:
 for pid in d['proposal_ids']:
  p=next(p for p in PR['proposals'] if p['proposal_id']==pid)
  if d['case_id'] not in p['case_ids']:
   assert d['case_id']==C[53]['case_id'] and pid=='sv1-kg-swine-serum1076b'
   p['case_ids'].append(d['case_id']);p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+d['evidence_ids']+d['independent_review']['evidence_ids']));p['cross_partition_binding']='Bio53 and KG181 refer to the same DSMZ1076b swine heat-inactivated preparation. Independent bio and KG reviews both assess applicability. No payload bytes changed by this backlink.'
assert len(D['decisions'])==188
assert len({e['evidence_id'] for e in E['evidence']})==len(E['evidence'])
assert len({p['owner_path'] for p in PR['proposals']})==len(PR['proposals'])
changed={i for v in parts.values() for i in v};assert len(changed)==144
for i in range(188):
 if i not in changed:assert D['decisions'][i]==old['decisions'][i]
for name,o in [('decisions',D),('evidence',E),('proposals',PR)]:dump(S/(name+'.json'),o)
dump(S/'subagent-scopes.json',{'at':datetime.now(timezone.utc).isoformat(),'predecessor_head':'dbaf4629f3b93d3bd8a78028e243abfe90c7a922','scopes':scopes,'unchanged_cases':44,'unchanged_review_basis':'Exact predecessor decisions,36proposals and review evidence retained. No fresh144case review is attributed to the other44.','external_sessions_started':0})
shutil.copyfile(Q/'shards/shard-10.json',S/'context/shard-10.json')
stats={'cases':188,'fresh_reassessments':144,'unchanged_prior_cases':44,'evidence':len(E['evidence']),'proposals':len(PR['proposals']),'new_successor_proposals':len(PR['proposals'])-36,'proposed_cases':sum(bool(d['proposal_ids']) for d in D['decisions']),'no_proposal_cases':sum(not d['proposal_ids'] for d in D['decisions']),'source_counts':dict(collections.Counter(d['source']['source'] for d in D['decisions'])),'dispositions':dict(collections.Counter(d['disposition'] for d in D['decisions'])),'proposal_kinds':dict(collections.Counter(p['kind'] for p in PR['proposals'])),'owner_preimages':len({o['path'] for d in D['decisions'] for o in d['owner_records']}),'occurrences':sum(len(d['occurrence_ids']) for d in D['decisions'])}
dump(S/'accounting.json',stats);print(json.dumps(stats))
