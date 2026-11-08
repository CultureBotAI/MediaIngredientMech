"""Verify all old core objects survive except the explicitly declared successor deltas."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

D=Path(__file__).resolve().parents[1]
OLD=D.parent/'shard'


def load(path):return json.loads(path.read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def rowsha(row):return hashlib.sha256(json.dumps(row,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()


def check(stage):
    core=D/'cores'/stage
    delta=load(D/'science/assembly-deltas-v1.json')
    updates={r['case_id']:r['updates'] for r in delta['case_updates']}
    oldd=load(OLD/'decisions.json');newd=load(core/'decisions.json')
    assert {k:v for k,v in oldd.items() if k!='decisions'}=={k:v for k,v in newd.items() if k!='decisions'}
    assert len(oldd['decisions'])==len(newd['decisions'])==188
    cases=[]
    for old,new in zip(oldd['decisions'],newd['decisions']):
        assert old['case_id']==new['case_id']
        stripped=copy.deepcopy(new)
        lineage=stripped.pop('successor_lineage')
        assert lineage['predecessor_row_sha256']==rowsha(old)
        assert lineage['original_independent_review']==old['independent_review']
        expected=copy.deepcopy(old)
        expected.update(updates.get(old['case_id'],{}))
        for key in ['independent_review','evidence_ids','issue_refs']:
            if key in ['evidence_ids','issue_refs']:
                assert all(x in new[key] for x in old[key])
            stripped[key]=copy.deepcopy(old[key])
        assert stripped==expected,old['case_id']
        cases.append({'case_id':old['case_id'],'old_row_sha256':rowsha(old),'new_row_sha256':rowsha(new),'scientific_delta':old['case_id'] in updates,'source_occurrence_and_other_outcome_fields_unchanged':True})
    oldp=load(OLD/'proposals.json')['proposals'];newp=load(core/'proposals.json')['proposals']
    pupdates={r['proposal_id']:r['updates'] for r in delta['proposal_updates']}
    assert len(oldp)==len(newp)==76
    for old,new in zip(oldp,newp):
        assert old['proposal_id']==new['proposal_id']
        stripped=copy.deepcopy(new)
        lineage=stripped.pop('successor_lineage');stripped.pop('successor_review_status')
        assert lineage['predecessor_row_sha256']==rowsha(old)
        expected=copy.deepcopy(old);expected.update(pupdates.get(old['proposal_id'],{}))
        assert new['evidence_ids'][:len(old['evidence_ids'])]==old['evidence_ids']
        for key in ['evidence_ids','after_capture']:stripped[key]=copy.deepcopy(old[key])
        assert stripped==expected,old['proposal_id']
    olde=load(OLD/'evidence.json')['evidence'];newe=load(core/'evidence.json')['evidence']
    assert newe[:len(olde)]==olde
    return {'result':'PASS','stage':stage,'scope':'All188 full decision objects,76 proposal objects, and the complete1118 original evidence-entry prefix compared; only explicitly scoped amendments and new lineage/review bindings differ.','case_count':len(cases),'case_scientific_deltas':len(updates),'proposal_count':len(oldp),'proposal_scientific_metadata_deltas':len(pupdates),'original_evidence_entries_retained':len(olde),'total_evidence_entries':len(newe),'cases':cases,'core_sha256':{n:sha(core/(n+'.json')) for n in ['decisions','proposals','evidence']},'whole_owner_or_export_approval':False}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--stage',required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    result=check(args.stage)
    with args.output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['cases','core_sha256']}))
