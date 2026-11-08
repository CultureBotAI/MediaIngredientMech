"""Attach real peer review receipts only after exact scientific payload checks."""
import collections,datetime,hashlib,json
from pathlib import Path
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file())
OUT=ROOT/'reports/all_unmatched_20261107/worker-09'
SOURCE=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def science(d):return hashlib.sha256(json.dumps({k:v for k,v in d.items() if k!='independent_review'},sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
reviews={'antibiotics':'salts/review-of-antibiotics/review-final.json','salts':'materials/review-of-salts/review-final.json','materials':'antibiotics/review-of-materials/review-final.json'}
decisions=json.loads((OUT/'decisions.json').read_text()); evidence=json.loads((OUT/'evidence.json').read_text()); byid={d['case_id']:d for d in decisions['decisions']};receipt=[]
for group,rel in reviews.items():
 review=json.loads((OUT/rel).read_text())
 assert review['review_status']=='complete', (group,'incomplete reviewer receipt')
 for filename in ('decisions.json','evidence.json','proposals.json'):
  expected=sha(OUT/group/filename)
  keys=(filename,str((OUT/group/filename).relative_to(ROOT)))
  hashes=[review['input_hashes'][k] for k in keys if k in review['input_hashes']]
  assert hashes and all(h==expected for h in hashes), (group,filename,'reviewed file changed or missing binding')
 proposals=json.loads((OUT/group/'proposals.json').read_text())['proposals']
 assert {p['proposal_id'] for p in proposals}=={p['proposal_id'] for p in review['proposal_reviews']}, (group,'proposal review coverage mismatch')
 assert len(proposals)==len(review['proposal_reviews']), (group,'duplicate proposal review')
 for p in proposals:
  assert sha(OUT/p['after_capture']['path'])==p['after_capture']['sha256'], (group,p['proposal_id'],'reviewed after payload changed')
 for item in json.loads((OUT/group/'evidence.json').read_text())['evidence']:
  capture=item['capture'];base={'artifact':OUT,'source':SOURCE}[capture['root']]
  assert sha(base/capture['path'])==capture['sha256'], (group,item['evidence_id'],'reviewed capture changed')
 primary=json.loads((OUT/group/'decisions.json').read_text())['decisions']; peer={d['case_id']:d for d in review['case_reviews']}
 assert set(peer)=={d['case_id'] for d in primary} and len(peer)==len(review['case_reviews']), (group,'review coverage mismatch')
 for d in primary:
  statuses=[peer[d['case_id']][k] for k in ('review_status','status') if k in peer[d['case_id']]]
  assert statuses and all(s=='complete' for s in statuses), (group,d['case_id'],'individual review incomplete')
  assert science(d)==peer[d['case_id']]['scientific_payload_sha256'], (group,d['case_id'],'reviewed science changed')
  assert science(byid[d['case_id']])==science(d), (group,d['case_id'],'assembled science changed')
 eid='w09-independent-'+group
 assert eid not in {e['evidence_id'] for e in evidence['evidence']}, 'run once on freshly assembled files'
 evidence['evidence'].append({'evidence_id':eid,'kind':'independent_review','capture':{'root':'artifact','path':rel,'sha256':sha(OUT/rel)},'url':None,'locator':'Complete case_reviews and proposal_reviews, exact input hashes, initial challenges and final re-review','supports_or_contradicts':'Separate in-process agent reviewed every assigned scientific decision and exact proposal; accepts bounded dispositions with source gaps and publication holds preserved. This is not export approval.','case_ids':[d['case_id'] for d in primary]})
 for d in primary:byid[d['case_id']]['independent_review']={'status':'complete','evidence_ids':[eid]}
 receipt.append({'primary_group':group,'review_capture':rel,'review_sha256':sha(OUT/rel),'case_count':len(primary),'case_scientific_payloads_verified':True,'case_ids':[d['case_id'] for d in primary]})
assert len(byid)==187 and all(d['independent_review']['status']=='complete' for d in byid.values())
write(OUT/'decisions.json',decisions);write(OUT/'evidence.json',evidence)
progress=json.loads((OUT/'progress.json').read_text());progress.update(reviewed_count=187,remaining_count=0,reviewed_case_ids=list(byid),remaining_case_ids=[],current_task='Final native review, validation, commit and push',updated_at=datetime.datetime.now(datetime.timezone.utc).isoformat());write(OUT/'progress.json',progress)
write(OUT/'validation/independent-review-bindings.json',{'status':'PASS','reviewed_count':187,'method':'Canonical decision JSON hash excluding only independent_review; all other fields, including issue refs and primary author, must match the actual separate reviewer receipt.','reviews':receipt,'only_aggregate_field_changed':'independent_review','export_approval':False})
scopes=json.loads((OUT/'agent-scopes.json').read_text());scopes['completed_independent_review_scopes']=receipt;scopes['review_rotation']='salts independently reviewed antibiotics58; antibiotics independently reviewed materials60; materials independently reviewed salts69';write(OUT/'agent-scopes.json',scopes)
print(json.dumps({'status':'PASS','reviewed':187,'independent_receipts':3,'evidence_entries':len(evidence['evidence'])}))
