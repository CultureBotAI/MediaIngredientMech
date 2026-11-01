"""Read-only replay of the already generated candidate; no transaction or writes to MIM."""
from pathlib import Path
import hashlib,importlib.util,json
HERE=Path(__file__).resolve().parent
RUN=HERE.parents[1];ROOT=RUN/'step3-mim'
spec=importlib.util.spec_from_file_location('carnitine_1038_probe',ROOT/'scripts/merge_carnitine_hydrochloride.py');w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
current={p:(ROOT/p).read_bytes() for p in w.SOURCE_PATHS}
w.complete_sources(current)
source=RUN/'step3-application/source-apply.json'
w.validate_completed_receipt(ROOT,ROOT/w.EVIDENCE,source,current)
candidate=ROOT/'output/step3-native-candidate/candidate.sssom.tsv';raw=candidate.read_bytes()
assert w.digest(raw)=='02b40e540b0663944500071e5725004ec0610e46bf3dd0b83cd4987820af7736'
before=w.frozen_bytes(w.SSSOM);live_before=(ROOT/w.SSSOM).read_bytes();assert live_before==before
result=w.promoted_sssom(before,raw,{p:current[p] for p in w.OWNERS})
old=w.table(before)[1];new=w.table(result)[1]
assert [r for r in old if r['subject_id'] not in w.SUBJECTS]==[r for r in new if r['subject_id'] not in w.SUBJECTS]
assert (ROOT/w.SSSOM).read_bytes()==live_before
assert w.digest(source.read_bytes())=='8e031dc9d823b904dbbd3cab07d5dffa8411d7a4c59661d96ad8da6217743533'
report={'kind':'read-only author replay; not production promotion or independent review','writer_sha256':hashlib.sha256((ROOT/'scripts/merge_carnitine_hydrochloride.py').read_bytes()).hexdigest(),'candidate_path':str(candidate),'candidate_sha256':w.digest(raw),'source_receipt_sha256':w.digest(source.read_bytes()),'before_sha256':w.digest(before),'proposed_sha256':w.digest(result),'canonical_unchanged':True,'before_rows':len(old),'after_rows':len(new),'selected_rows':[r for r in new if r['subject_id'] in w.SUBJECTS],'source_proposal_and_receipt_still_exact':True}
with (HERE/'actual-candidate-replay.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in report.items() if k!='selected_rows'},indent=2))
