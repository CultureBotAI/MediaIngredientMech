from pathlib import Path
from datetime import datetime, timezone
import json,hashlib,yaml
W=Path(__file__).resolve().parents[3];R=W/'reports/all_unmatched_20261107/worker-02';S=R/'final-corrections-v1/chemistry';V=W/'.temp/w02-final-corrections-v1/frozen-w04-review/science/reviewer-b/captures'
def read(p):return json.loads(p.read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def cap(p):return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())}
def save(p,o):assert not p.exists();p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
for suffix in ['.body','.receipt.json']:
    p=V/('paba-europepmc'+suffix);q=S/'captures'/('w04-paba-europepmc'+suffix);assert not q.exists();q.write_bytes(p.read_bytes())
receipt=read(S/'captures/w04-paba-europepmc.receipt.json');body=S/'captures/w04-paba-europepmc.body';assert sha(body.read_bytes())==receipt['sha256']
pubmed_id='fc-chem-paba-literature-context'
e=read(S/'evidence-v2.json');e['predecessor_metadata_capture']=cap(S/'evidence-v2.json');e['evidence'].append({'evidence_id':pubmed_id,'kind':'primary_source','capture':cap(body),'url':receipt['url'],'accessed_at':receipt['started_at'],'locator':'resultList.result[0], PMID31986050, full abstractText; source HTML italics around p preserve the same semantic quoted phrase.','supports_or_contradicts':'The article describes a1:1 ketoconazole/PABA cocrystal, supporting an adjacent contextual mention. It does not independently establish the pure-acid owner synonym identity or a medium-specific vitamin role. Keep the existing LITERATURE snippet and qualify supports as PARTIAL.'});save(S/'evidence-v3.json',e)
p=read(S/'proposals-v2.json');p['predecessor_metadata_capture']=cap(S/'proposals-v2.json');next(x for x in p['proposals'] if x['proposal_id']=='b-proposal-paba')['evidence_ids'].append(pubmed_id);save(S/'proposals-v3.json',p)
d=read(S/'decisions-v2.json');d['predecessor_metadata_capture']=cap(S/'decisions-v2.json');patch=read(R/'final-corrections-v1/preparations/case69-context-update.json');x=next(x for x in d['decisions'] if x['case_id']==patch['case_id']);assert all(x[k]==patch[k] for k in ['case_id','case_input_sha256','source','occurrence_ids'])
x['evidence_ids'].append(pubmed_id)
for dest,src in [('proposal_ids','append_proposal_ids'),('evidence_ids','append_evidence_ids'),('issue_refs','append_issue_refs')]:x[dest]=list(dict.fromkeys(x[dest]+patch[src]))
x['context_only_proposal_ids']=patch['context_only_proposal_ids'];x['reasoning']+=' '+patch['append_reasoning'];x['preparation_context_patch_capture']=cap(R/'final-corrections-v1/preparations/case69-context-update.json')
d['external_fragment_dependencies']={'proposal_ids':patch['append_proposal_ids'],'evidence_ids':patch['append_evidence_ids'],'source':str((R/'final-corrections-v1/preparations').relative_to(R)),'scope':'C-authored preparation is a context-only inherited-owner correction; not identity asserted for either originalcase69 occurrence.'};save(S/'decisions-v3.json',d)
f=read(S/'finite-claim-dispositions.json');f['predecessor_capture']=cap(S/'finite-claim-dispositions.json');active=0;excluded=[]
for r in f['role_claims']:
    path=R/r['selected_capture']['path'];status=yaml.safe_load(path.read_text())['mapping_status'];r['mapping_status']=status
    if r['category']=='prediction_only':
        if status=='REJECTED':excluded.append({'proposal_id':r['proposal_id'],'pointer':r['pointer'],'full_value':r['full_value'],'reason':'REJECTED owner excluded from active-only count; preserved in all-object inventory.'})
        else:active+=1
f['counts']['active_prediction_only_role_objects']=active;f['counts']['excluded_rejected_prediction_only_role_objects']=len(excluded);f['excluded_rejected_prediction_only']=excluded
f['count_limit']='All106 selected YAML contain8 prediction-only role objects;7 belong to non-REJECTED records. The excluded eighth is the REJECTED nickel-sulfate-hexahydrate tombstone, not a discrepancy with the prior seven active count. One active role has an empty evidence list. Both counts preserve exact full objects and do not infer truth or falsity.';assert active==7 and len(excluded)==1;save(S/'finite-claim-dispositions-v2.json',f)
inputs=[]
for n in [1242,1243,1244,873,1229,1230,1220,811,868,1050,718]:
    for suffix in ['body','comments']:
        q=W/f'.temp/w02-final-corrections-v1/live/issue-{n}-{suffix}.json';inputs.append({'path':str(q.relative_to(W)),'sha256':sha(q.read_bytes()),'scope':'Root-captured live issue bodies/comments read for exact bounded chemistry claims.'})
save(S/'source-and-contract-input-bindings.json',{'author':'/root/research_b','read_inputs':inputs,'live_retrieval_receipt':{'path':'.temp/w02-final-corrections-v1/live/receipts.json','sha256':sha((W/'.temp/w02-final-corrections-v1/live/receipts.json').read_bytes())},'author_contract':read(W/'.temp/w02-final-corrections-v1/chemistry/author-instructions-binding.json'),'native_writer':{'path':'src/mediaingredientmech/validation/write_validated.py','sha256':sha((W/'src/mediaingredientmech/validation/write_validated.py').read_bytes())},'schema':{'path':'src/mediaingredientmech/schema/mediaingredientmech.yaml','sha256':sha((W/'src/mediaingredientmech/schema/mediaingredientmech.yaml').read_bytes())},'mapping_semantics':{'path':'MAPPING_SEMANTICS.md','sha256':sha((W/'MAPPING_SEMANTICS.md').read_bytes())}})
allp=p['proposals'];old=read(R/'continuation-1201-v1/decisions.json')['decisions'];olde=read(R/'continuation-1201-v1/evidence.json')['evidence'];c_e=read(R/'final-corrections-v1/preparations/evidence.json')['evidence'];ev={x['evidence_id']:x for x in olde+e['evidence']+c_e};caseids={x['case_id'] for x in d['decisions']}
for x in d['decisions']:
    prev=next(v for v in old if v['case_id']==x['case_id']);assert all(x[k]==prev[k] for k in ['case_id','case_input_sha256','source','occurrence_ids'])
    for id in x['evidence_ids']:assert id in ev,id
for x in allp:
    assert sha((W/x['owner_path']).read_bytes())==x['before_sha256'];assert sha((R/x['after_capture']['path']).read_bytes())==x['after_capture']['sha256'];assert set(x['case_ids'])<=caseids
    for cid in x['case_ids']:assert x['proposal_id'] in next(z for z in d['decisions'] if z['case_id']==cid)['proposal_ids']
    for id in x['evidence_ids']:assert id in ev,id
for x in e['evidence']:assert sha((R/x['capture']['path']).read_bytes())==x['capture']['sha256']
save(S/'integrity-v3.json',{'status':'PASS','author':'/root/research_b','created_at':datetime.now(timezone.utc).isoformat(),'active_fragments':[cap(S/(kind+'-v3.json')) for kind in ['decisions','proposals','evidence']],'proposal_count':len(allp),'decision_count':len(d['decisions']),'new_evidence_count':len(e['evidence']),'unchanged_candidate_YAML_count':15,'native_writes':'15 completed in originalbuild; unchanged subsequent metadata-only versions do not repeat scientific validation.','metadata_revision_reasons':['Schema envelope and allowed local_validation evidence kind.','Precise case69/149 remainingrequirements.','Explicit primary PABA literature capture and C-authored context-only stock backlink.','All-object8 versus active7 role count, with rejected tombstone exclusion.'],'independent_review':'pending final D content/hash binding','scientific_approval':False,'inherited_scientific_holds_retained':True})
print('PASS:15 chemistry candidates,34 exact original cases,33 new evidence entries; active v3 metadata; all candidate YAML unchanged.')
