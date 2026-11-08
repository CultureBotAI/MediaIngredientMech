"""Fill required explicit no-payload reasons without changing source decisions."""
import datetime,hashlib,json,shutil
from pathlib import Path
W=Path('reports/all_unmatched_20261107/worker-04');S=W/'successors/issue-1201-v1';F=S/'fragments';C=S/'captures/chemistry'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((W/'decisions.json').read_text())['decisions']
reasons={
27:'The original CCAP TAP recipe resolves this occurrence to the existing active Na2edta2h2o owner (CHEBI:64758). Its identity already represents disodium EDTA dihydrate, and the similarly identified Na2-edta_X_2_H2o tombstone is REJECTED. No owner edit or global alias is required; the changed source binding remains source-specific.',
73:'The original CCAP Waris-H recipe resolves this occurrence to the existing active Na2edta2h2o owner (CHEBI:64758). Its identity already represents disodium EDTA dihydrate, and the similarly identified Na2-edta_X_2_H2o tombstone is REJECTED. No owner edit or global alias is required; the changed source binding remains source-specific.',
80:'The original Hoshino/Satoh 1985 S-medium formula prints NaCl 0.2 g and supports the existing sodium-chloride owner (CHEBI:26710). No owner payload is needed to correct this source occurrence binding; the erroneous raw spelling NaCI remains provenance only and is not added as a global alias.',
90:'The primary P5 recipe explicitly names myo-inositol, which is already represented by the existing owner (CHEBI:17268). No owner edit is required for this source-specific chemical binding. The misleading B7 annotation is retained only as source provenance; no B7/B8 alias or vitamin-role assertion is added.'}
byid={old[i]['case_id']:(i,reason) for i,reason in reasons.items()}
p=F/'chemistry-decisions.json';archive=C/'no-payload-reasons-v1';assert not archive.exists();archive.mkdir()
shutil.copyfile(p,archive/p.name);before=sha(p);obj=json.loads(p.read_text());changes=[]
for d in obj['decisions']:
 if d['case_id'] in byid:
  i,reason=byid[d['case_id']];assert not d['proposal_ids'] and d['no_change_reason'] is None
  d['no_change_reason']=reason;changes.append({'case_index':i,'case_id':d['case_id'],'field':'no_change_reason','before':None,'after':reason})
assert len(changes)==4
p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
receipt={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','scope':'Exactly four explicit no-owner-payload reason fields filled from already reviewed source-specific reasoning. No reasoning, identity, proposal, evidence, source, occurrence, or hold field changed.','before_capture':{'path':str((archive/p.name).relative_to(S)),'sha256':before},'changes':changes,'all_four_fragments':{f'fragments/chemistry-{k}.json':sha(F/f'chemistry-{k}.json') for k in ['reassessments','decisions','evidence','proposals']}}
(C/'no-payload-reasons-v1.json').write_text(json.dumps(receipt,indent=2)+'\n')
integrity=json.loads((C/'integrity-final-v2.json').read_text());integrity['checked_at']=receipt['checked_at'];integrity['fragments']=receipt['all_four_fragments'];integrity['no_payload_reason_correction']={'path':str((C/'no-payload-reasons-v1.json').relative_to(S)),'sha256':sha(C/'no-payload-reasons-v1.json')}
(C/'integrity-final-v3.json').write_text(json.dumps(integrity,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
