"""Attach peer metadata only after checking the exact independently reviewed bytes."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1];WORKER=HERE.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda o:json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def read(p):return json.loads(p.read_text())
def write(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
peerpath=HERE/'independent/review-final.json';peer=read(peerpath)
assert peer['review_status']=='complete' and peer['open_findings']==[] and peer['reviewer']=='/root/materials'
assert sha(HERE/'existing-owner-associations.json')==peer['association_file_sha256']
ds=read(HERE/'decisions.json');evidence=read(HERE/'evidence.json');eid='hx-independent-final'
if not any(e['evidence_id']==eid for e in evidence['evidence']):
    assert sha(HERE/'evidence.json')==peer['evidence_file_sha256_before_peer_attachment']
    evidence['evidence'].append({'evidence_id':eid,'capture':{'root':'artifact','path':str(peerpath.relative_to(WORKER)),'sha256':sha(peerpath)},'kind':'independent_review','url':None,'accessed_at':peer['completed_at'],'locator':'case_reviews[0:2], input/scientific hashes, findings HX-SR-01/02 and re-review; independent/ contains separately captured evidence and lineage reconstruction','supports_or_contradicts':'Separate skeptical reviewer independently verified both exact source forms and source associations. Evidence-applicability and stale-receipt findings corrected and re-reviewed; no open findings. Whole-owner/export holds retained.','case_ids':[d['case_id'] for d in ds['decisions']]})
byid={r['case_id']:r for r in peer['case_reviews']}
for d in ds['decisions']:
    r=byid[d['case_id']]
    assert r['review_status']=='complete'
    assert hashlib.sha256(canon({k:v for k,v in d.items() if k!='independent_review'})).hexdigest()==r['scientific_payload_sha256']
    d['independent_review']={'status':'complete','evidence_ids':[eid]}
write(HERE/'decisions.json',ds);write(HERE/'evidence.json',evidence)
write(HERE/'validation/peer-attachment.json',{'status':'PASS','peer_capture_sha256':sha(peerpath),'reviewed_scientific_payloads_unchanged':True,'source_associations_unchanged':True,'decision_count':2,'attached_evidence_id':eid,'decision_file_sha256':sha(HERE/'decisions.json'),'evidence_file_sha256':sha(HERE/'evidence.json')})
print('PASS: two unchanged scientific payloads bound to completed separate review')
