from pathlib import Path
import json,hashlib,datetime,collections
R=Path('reports/all_unmatched_20261107/worker-06')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,j):p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
D=json.loads((R/'decisions.json').read_text())['decisions'];E={e['evidence_id']:e for e in json.loads((R/'evidence.json').read_text())['evidence']};P=json.loads((R/'proposals.json').read_text())['proposals']
limits=[]
for i,d in enumerate(D):
 if not any(E[e]['kind']=='primary_source' for e in d['evidence_ids']):
  limits.append({'case_index_zero_based':i,'case_id':d['case_id'],'raw_source_label':d['source']['raw_source_label'],'disposition':d['disposition'],'missing_requirement':d.get('missing_requirement') or 'The narrow chemical lexical identity is supported by the frozen source spelling and official ontology authority; a version-matched primary recipe has not been independently recovered. No source-release approval.','evidence_ids':d['evidence_ids'],'evidence_kinds':sorted({E[e]['kind'] for e in d['evidence_ids']}),'independent_review':d['independent_review']})
dump(R/'primary-access-limitations.json',{'at':now(),'selection':'All final decisions without a linked capture classified primary_source. Official ontology authority is itself primary authority for its term, but is not a primary recipe. Other decisions can also contain partial access gaps, version or product-lot limits documented individually.','count':len(limits),'cases':limits,'scientific_release_approval':False})
a=json.loads((R/'agent-scopes.json').read_text());reviews=['independent/root-review-a/final-review-v2.json','research-a/review-b/review-b-v6.json','research-b/review-c/review-final.json','research-c/review-root/completion-addendum.json']
for s,review in zip(a['scopes'],reviews):
 folder=(R/s['authored_fragment']).parent
 d=json.loads((folder/'decisions.json').read_text())['decisions'];p=json.loads((folder/'proposals.json').read_text())['proposals'];e=json.loads((folder/'evidence.json').read_text())['evidence']
 s.update({'status':'complete; separate skeptical review complete with explicit scientific limitations','authored_case_count':len(d),'frozen_cm_occurrence_id_count':sum(len(x['occurrence_ids']) for x in d),'authored_proposal_count_before_cross_group_dedup':len(p),'evidence_count':len(e),'independent_review_path':review,'independent_review_sha256':sha(R/review),'input_hashes':{str((folder/f).relative_to(R)):sha(folder/f) for f in ['decisions.json','evidence.json','proposals.json']}})
a.update({'at':now(),'all_reviewed_count':len(D),'authored_fragment_proposal_count':sum(s['authored_proposal_count_before_cross_group_dedup'] for s in a['scopes']),'unique_selected_proposal_count':len(P),'deduplication':'One frozen Yeast_Extract owner: C-P-YEAST-EXTRACT replaced by independently reviewed combined B-P-Yeast_Extract; historical C payload retained but not selected.','integration_reviewer':'/root/research_b (A separately reviewed B-authored scientific decisions)','integration_review_path':'research-b/integration-review/review-final.json','cross_shard_and_ontology_auditor':'/root/research_c','release_approval':False})
dump(R/'agent-scopes.json',a)
p=json.loads((R/'progress.json').read_text());p.update({'updated_at':now(),'reviewed_case_ids':[d['case_id'] for d in D],'remaining_case_ids':[],'reviewed_count':len(D),'remaining_count':0,'authored_case_count':len(D),'independently_completed_case_count':sum(d['independent_review']['status']=='complete' for d in D),'phase':'final validation and handoff','current_task':'Finalize native formal review, independent final diff review, manifest, ordinary commit and push.','blockers':[],'remaining':'Scientific shard review complete; final publication of this evidence branch remains.','case_dispositions':dict(collections.Counter(d['disposition'] for d in D)),'proposal_count':len(P),'evidence_count':len(E)})
dump(R/'progress.json',p)
print('Metadata',len(D),'cases',len(P),'selected proposals;',len(limits),'without primary recipe capture')
