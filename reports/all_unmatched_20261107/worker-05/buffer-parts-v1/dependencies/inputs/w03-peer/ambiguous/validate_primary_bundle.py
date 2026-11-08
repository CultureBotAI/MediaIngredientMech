from pathlib import Path
import csv, datetime, hashlib, io, json, subprocess, zipfile
A=Path(__file__).resolve().parent
R=A.parents[2]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[]
def check(name, condition, detail):
    assert condition, (name,detail)
    checks.append({'name':name,'result':'PASS','detail':detail})
claims=json.loads((A/'selected-claims.json').read_text())
ledger=json.loads((A/'per-claim-scientific-ledger.json').read_text())
check('exact_claim_coverage',set(c['claim_key'] for c in claims)==set(c['claim_key'] for c in ledger['claims']) and len(ledger['claims'])==10,'10 selected claims, 10 unique assessed claims')
for x in json.loads((A/'owner-beforeimage-pins.json').read_text()):
    check('owner_beforeimage:'+Path(x['path']).name,sha(x['path'])==x['sha256']==sha(A/x['copy']),x['sha256'])
obs=json.loads((A/'original-source-observations.json').read_text())
check('source_archive',sha(obs['archive'])==obs['archive_sha256'],obs['archive_sha256'])
with zipfile.ZipFile(obs['archive']) as z: raw=z.read(obs['member'])
check('source_archive_member',hashlib.sha256(raw).hexdigest()==obs['member_sha256'],obs['member_sha256'])
original=list(csv.DictReader(io.StringIO(raw.decode('latin1'))))
for o in obs['rows']:
    r=original[o['record_index_zero_based']]
    assert o['csv_row_including_header']==o['record_index_zero_based']+2
    assert r[o['field']]==o['literal']
    assert r['Genus']==o['genus'] and r['Species']==o['species']
    for key,value in o['source_links'].items():assert r[key]==value
check('all_original_observations',len(obs['rows'])==124,'124 original row/field/value/taxon/source-link checks; includes114 PYG')
check('observation_ledger_coverage',sum(c['original_source_observation_count'] for c in ledger['claims'])==124,'Complete selected population; no exhaustive114-paper claim')
for e in json.loads((A/'source-evidence-catalog.json').read_text()):
    for f in e['files']: assert sha(A/f['path'])==f['sha256']
check('source_catalog_capture_hashes',True,'Every catalogued file rehashed')
for p in json.loads((A/'candidate-context-pins.json').read_text()):
    path=p.get('path',p.get('source_path'));assert sha(path)==p['independently_rehashed_sha256']
check('candidate_contexts',True,'3 frozen W05 proposal bytes plus2 exact coordinator context candidates; no acceptance implied')
for p in json.loads((A/'input-pins.json').read_text()):assert sha(p['path'])==p['sha256']
check('contract_and_intake_inputs',True,'All recorded contract/plan input bytes unchanged')
for p in json.loads((A/'research-lead-pins.json').read_text()):assert sha(p['path'])==p['sha256']==sha(A/p['copy'])
check('research_leads_preserved',True,'10 exact citation lead copies; no primary evidence conversion')
html=A/'captures/moore1976-primary-mirror.pdf'
check('denied_raw_pdf_not_promoted',not html.read_bytes().startswith(b'%PDF'),'403 HTML retained; primary-paper read is web-tool extracted text only')
for c in ledger['claims']:
    assert not any(c[k] for k in ['source_case_accepted_for_integration','whole_owner_approved','role_approved','supported_export_approved','worker03_own_proposals_approved'])
    assert c['minimal_withdrawal_recommendation']['reference_scope']=='UNMAPPED'
check('holds_and_scope',True,'No whole-owner, role, export or own-proposal approval; quantities and original observation/interpretation distinction retained')
head=subprocess.run(['git','rev-parse','HEAD'],cwd=R,text=True,capture_output=True,check=True).stdout.strip()
status=subprocess.run(['git','status','--short'],cwd=R,text=True,capture_output=True,check=True).stdout
check('published_head_preserved',head=='fe31a02850932a7bdf2fe65c93cb636a86f82a2c',head)
check('tracked_worktree_clean',status=='',status)
out={'validated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':'PYTHONDONTWRITEBYTECODE=1 .temp/all-unmatched-worker-03/env/bin/python .temp/peptone-consumer-independent-v1/ambiguous/validate_primary_bundle.py','exit_code':0,'kind':'artifact_binding_and_coverage','scientific_approval':False,'native_owner_validation':'Parent performs all20 focused native/schema review; not rerun here.','checks':checks}
with (A/'validation-receipt.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'checks_passed':len(checks),'head':head,'validation_receipt_sha256':sha(A/'validation-receipt.json')},indent=2))
