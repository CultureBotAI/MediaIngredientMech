from pathlib import Path
import json,hashlib,shutil
S=Path('reports/all_unmatched_20261107/worker-06/successor-v3'); A=S/'assembly-attempt-1';A.mkdir(exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for f in ['decisions.json','proposals.json','evidence.json','selection.json','source-holds.json','delta.json','review-coverage.json']:shutil.copyfile(S/f,A/f)
E=json.loads((S/'evidence.json').read_text());e=next(e for e in E['evidence'] if e['evidence_id']=='V3-B-DEDUP');assert e['kind']=='dedup_review';e['kind']='local_validation';dump(S/'evidence.json',E)
d=json.loads((S/'delta.json').read_text());d['new_core_sha256']['evidence.json']=sha(S/'evidence.json');d['integration_notes'].append('Structural gate exposed B dedup_review evidence kind outside the outcome vocabulary; central V3-B-DEDUP is local_validation. Initial central candidate and failed gate remain immutable in assembly-attempt-1 and logs/full-final-v1.');dump(S/'delta.json',d)
x=json.loads((S/'selection.json').read_text());x['core']['evidence.json']['sha256']=sha(S/'evidence.json');x['delta']['sha256']=sha(S/'delta.json');dump(S/'selection.json',x)
dump(S/'evidence-kind-correction.json',{'scope':'Contract vocabulary only; no scientific/source/payload change','evidence_id':'V3-B-DEDUP','before_kind':'dedup_review','after_kind':'local_validation','preserved_candidate':{str(p):sha(p) for p in sorted(A.iterdir())},'failed_gate':'logs/full-final-v1/structural-command.log','final_evidence_sha256':sha(S/'evidence.json'),'final_selection_sha256':sha(S/'selection.json')})
print(sha(S/'selection.json'))
