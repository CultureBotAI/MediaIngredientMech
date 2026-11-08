"""Run the actual campaign auditor and reject stale complete-case bindings."""
import argparse
import copy
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

D=Path(__file__).resolve().parents[1]
W=Path(__file__).resolve().parents[5]
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
AUDITOR=C/'scripts/audit_worker_outcomes_v1.py'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def save(p,obj):
    with p.open('x') as f:json.dump(obj,f,indent=2,ensure_ascii=False);f.write('\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--stage',required=True,choices=['pre-review','final'])
    parser.add_argument('--output-directory',type=Path,required=True)
    args=parser.parse_args()
    assert not args.output_directory.exists()
    spec=importlib.util.spec_from_file_location('campaign_outcome_auditor',AUDITOR)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    cores=D/'cores'/args.stage
    kwargs={'shard_path':C/'queue/preliminary-v5/shards/shard-01.json','decisions_path':cores/'decisions.json','evidence_path':cores/'evidence.json','proposals_path':cores/'proposals.json','artifact_root':D.parent,'source_root':C/'queue/preliminary-v5','mim_root':W}
    positive=module.audit(**kwargs)
    args.output_directory.mkdir()
    save(args.output_directory/'positive-native-audit.json',positive)
    original=json.loads((cores/'decisions.json').read_text())
    controls=[]
    variants=[]
    bad=copy.deepcopy(original);bad['decisions'][0]['case_input_sha256']='0'*64
    variants.append(('stale-full-case-object',bad))
    bad=copy.deepcopy(original);row=next(r for r in bad['decisions'] if r['occurrence_ids']);row['occurrence_ids']=row['occurrence_ids'][1:]
    variants.append(('missing-original-occurrence',bad))
    bad=copy.deepcopy(original);bad['decisions'][0]['source']['raw_source_label']+=' invented qualifier'
    variants.append(('raw-source-label-changed',bad))
    for label, data in variants:
        path=args.output_directory/(label+'.json');save(path,data)
        control_kwargs=dict(kwargs,decisions_path=path)
        try:
            module.audit(**control_kwargs)
        except module.InvalidOutcome as exc:
            controls.append({'control':label,'rejected':True,'exception':type(exc).__name__,'message':str(exc),'counterexample_path':str(path.relative_to(D)),'sha256':sha(path)})
        else:
            controls.append({'control':label,'rejected':False})
    assert all(c['rejected'] for c in controls)
    result={'reviewer':'Codex /root (worker01 technical accounting)','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS','stage':args.stage,'auditor':{'path':str(AUDITOR),'sha256':sha(AUDITOR)},'positive_receipt_sha256':sha(args.output_directory/'positive-native-audit.json'),'controls':controls,'scientific_adequacy_or_approval_established':False}
    save(args.output_directory/'controls.json',result)
    print(json.dumps({'result':'PASS','stage':args.stage,'accounted_cases':positive['accounted_case_count'],'assigned_cases':positive['assigned_shard_case_count'],'negative_controls':len(controls)}))


if __name__=='__main__':main()
