"""Assemble a new immutable review core. Never overwrites a predecessor or stage."""
import argparse
import copy
import datetime
import hashlib
import json
from pathlib import Path

D = Path(__file__).resolve().parents[1]
W = Path(__file__).resolve().parents[5]
ARTIFACT = D.parent
OLD = ARTIFACT/'shard'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rowsha(row):
    return hashlib.sha256(json.dumps(row,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()


def read(p):
    return json.loads(p.read_text())


def put(p, obj):
    with p.open('x') as f:
        json.dump(obj,f,indent=2,ensure_ascii=False,allow_nan=False)
        f.write('\n')


def capture(p):
    return {'root':'artifact','path':str(p.relative_to(ARTIFACT)),'sha256':sha(p)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--stage',choices=['pre-review','final'],required=True)
    parser.add_argument('--review',type=Path)
    args=parser.parse_args()
    out=D/'cores'/args.stage
    assert not out.exists(),out
    if args.stage=='final':
        assert args.review and args.review.is_file()
    pins=next(x for x in read(D/'inputs/current-worker-bindings.json')['workers'] if x['worker']==1)
    for value in list(pins['core'].values())+pins['all_selected_payloads']:
        assert sha(Path(value['path']))==value['sha256'],value['path']
    a=read(D/'inputs/w01-full-provenance-allowlist-v2.json')
    bypid={}
    for row in a['rows']:
        bypid.setdefault(row['proposal_id'],[]).append(row)
    science=read(D/'science/assembly-deltas-v1.json')
    cupdate={x['case_id']:x for x in science['case_updates']}
    pupdate={x['proposal_id']:x for x in science['proposal_updates']}
    assert len(cupdate)==5 and len(pupdate)==4
    decisions=read(OLD/'decisions.json')
    proposals=read(OLD/'proposals.json')
    evidence=read(OLD/'evidence.json')
    additions=[
        ('W01-SUCCESSOR-ALLOWLIST',D/'inputs/w01-full-provenance-allowlist-v2.json','source_snapshot','Closed 76-entry, 66-payload agent provenance allowlist; not scientific approval.'),
        ('W01-SUCCESSOR-SCIENCE-DELTAS',D/'science/assembly-deltas-v1.json','source_snapshot','Four authorized #1237 scientific corrections and five exact source-case rationale deltas; author analysis with source bindings.'),
        ('W01-SUCCESSOR-EXACT-DELTAS',D/'checks/exact-deltas-v1.json','local_validation','Independent complete-object comparison, exact history prefix, 62 typing-only scientific content equality, ten byte-identical payloads and negative controls.'),
        ('W01-SUCCESSOR-NATIVE-CHECKS',D/'checks/native-checks-v1.json','local_validation','Native schema, baseline/predecessor/successor partonomy, generated predicates and nonresolving alias checks; no release approval.'),
    ]
    if args.review:
        additions.append(('W01-SUCCESSOR-INDEPENDENT-REVIEW',args.review,'independent_review','Author-independent review of exact full changed payloads, primary scope and 188/76 accounting. Limited to successor corrections and preservation; no whole-owner, role or export approval.'))
    for eid,path,kind,claim in additions:
        evidence['evidence'].append({'evidence_id':eid,'kind':kind,'capture':capture(path),'locator':'Complete exact file; scope and target identifiers stated within','supports_or_contradicts':claim,'url':None})
    bridge=[]
    science_ids=set(pupdate)
    for proposal in proposals['proposals']:
        prior=copy.deepcopy(proposal)
        pid=proposal['proposal_id']
        candidate=D/'payloads'/(pid+'.yaml')
        old_capture=copy.deepcopy(proposal['after_capture'])
        changed=pid in bypid
        if pid in pupdate:
            updates=pupdate[pid]['updates']
            assert set(updates)<= {'description','scope','integration_obligations','scientific_limitations','resolver_treatment','identity_predicate_consequence','integration_requirements'}
            proposal.update(copy.deepcopy(updates))
        proposal['after_capture']=capture(candidate)
        proposal['successor_lineage']={'source_head':pins['head'],'predecessor_core':capture(OLD/'proposals.json'),'proposal_id':pid,'predecessor_row_sha256':rowsha(prior),'predecessor_payload':old_capture,'relation':'supersedes_selected_payload' if changed else 'retains_exact_selected_payload','apply_rule':'Select this one row for this proposal ID; never apply predecessor and successor together.','inherited_whole_owner_support':False,'historical_review_scope':'Prior evidence retains only its actually unchanged claims; new bytes require the current independent review.','changed':changed,'issue_refs':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1226'] if changed else []}
        if pid in science_ids:proposal['successor_lineage']['issue_refs'].append('https://github.com/CultureBotAI/MediaIngredientMech/issues/1237')
        proposal['evidence_ids']+= [x[0] for x in additions]
        proposal['successor_review_status']='complete' if args.review else 'pending'
        bridge.append({'proposal_id':pid,'kind':proposal['kind'],'owner_path':proposal['owner_path'],'before_sha256':proposal['before_sha256'],'old_capture':old_capture,'selected_capture':proposal['after_capture'],'relation':proposal['successor_lineage']['relation'],'change_scope':'science_plus_typing' if pid in science_ids else 'typing_only' if changed else 'byte_identical','allowlist_entry_ids':[x['audit_row_id'] for x in bypid.get(pid,[])],'case_ids':proposal['case_ids'],'applicable_occurrence_ids':proposal.get('applicable_occurrence_ids',[]),'depends_on_proposals':proposal.get('depends_on_proposals',[]),'integration_obligations':proposal.get('integration_obligations',[]),'inherited_whole_owner_support':False})
    for decision in decisions['decisions']:
        prior=copy.deepcopy(decision)
        cid=decision['case_id']
        if cid in cupdate:
            updates=cupdate[cid]['updates']
            assert set(updates)<= {'reasoning','missing_requirement','candidate_assessment','applicability','completeness_revision'}
            decision.update(copy.deepcopy(updates))
        # Complete source objects, raw context and occurrence lists remain unchanged.
        for key in ['case_id','case_input_sha256','source','occurrence_ids','occurrence_bindings','proposal_ids','disposition','owner_records']:
            assert decision.get(key)==prior.get(key), (cid,key)
        decision['successor_lineage']={'source_head':pins['head'],'predecessor_core':capture(OLD/'decisions.json'),'case_id':cid,'predecessor_row_sha256':rowsha(prior),'scientific_rationale_changed':cid in cupdate,'finding_id':cupdate[cid]['finding_id'] if cid in cupdate else None,'original_independent_review':prior['independent_review'],'new_review_scope':'Exact successor corrections and preservation; prior unchanged scientific outcomes retained, no new approval.'}
        decision['evidence_ids'] += [x[0] for x in additions]
        decision['independent_review']={'status':'complete' if args.review else 'pending','evidence_ids':['W01-SUCCESSOR-INDEPENDENT-REVIEW'] if args.review else []}
        if any(pid in bypid for pid in decision['proposal_ids']):
            decision['issue_refs']=list(dict.fromkeys(decision['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1226']))
        if cid in cupdate:
            decision['issue_refs']=list(dict.fromkeys(decision['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1237']))
    assert len(decisions['decisions'])==188 and len(proposals['proposals'])==76
    assert len(set(p['proposal_id'] for p in proposals['proposals']))==76
    out.mkdir(parents=True)
    for name,data in [('decisions',decisions),('proposals',proposals),('evidence',evidence)]:put(out/(name+'.json'),data)
    selection={'schema_version':1,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author':'Codex /root (worker01 assembly only)','source_head':pins['head'],'stage':args.stage,'core_paths':{n:capture(out/(n+'.json')) for n in ['decisions','proposals','evidence']},'proposal_count':76,'case_count':188,'changed_payloads':66,'typing_only_payloads':62,'science_payloads':4,'unchanged_payloads':10,'selected_entries':bridge,'case_bindings':[{'case_id':x['case_id'],'case_input_sha256':x['case_input_sha256'],'source':x['source'],'occurrence_ids':x['occurrence_ids'],'proposal_ids':x['proposal_ids'],'missing_requirement':x['missing_requirement'],'disposition':x['disposition']} for x in decisions['decisions']],'selection_rule':'Exactly one selected payload per original proposal ID; no predecessor/successor double application. All source cases retained. Source-bound Se/W candidates remain partial and cannot be co-installed as proven distinct on omitted hydration.','scientific_owner_role_export_approval':False,'coordinator_37_composed_candidates_changed':False}
    put(out/'SELECTION.json',selection)
    print(json.dumps({'stage':args.stage,'case_count':188,'proposal_count':76,'selection_sha256':sha(out/'SELECTION.json'),'core_sha256':{n:sha(out/(n+'.json')) for n in ['decisions','proposals','evidence']}}))


if __name__=='__main__':main()
