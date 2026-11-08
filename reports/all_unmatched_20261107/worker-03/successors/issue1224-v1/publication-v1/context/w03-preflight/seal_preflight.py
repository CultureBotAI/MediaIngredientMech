"""Seal this unpublished preflight after actual independent review completes."""
from pathlib import Path
import json,hashlib,datetime,subprocess
R=Path.cwd();A=R/'.temp/w03-oxoid-successor-v1';O=R/'reports/all_unmatched_20261107/worker-03/successors/issue1224-v1';P=O.parents[1];D=O/'draft-v2'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,obj):
 with p.open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
def binding(p):return {'path':str(p),'sha256':sha(p)}
review=A/'review/HANDOFF.json';assert review.is_file(),'Do not seal before actual skeptical review receipt exists'
review_data=json.loads(review.read_text())
tracked=json.loads((A/'context/tracked-before.json').read_text());assert all((R/n).is_file() and sha(R/n)==h for n,h in tracked.items())
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='1196d5bc3aaba7563b829d5cbe7e54722fccc35d'
case=json.loads((D/'decisions.json').read_text())['decisions'];props=json.loads((D/'proposals.json').read_text())['proposals'];evid=json.loads((D/'evidence.json').read_text())['evidence']
counts={'cases':len(case),'active_proposals':len(props),'evidence_entries':len(evid),'other_case_objects_unchanged':187,'other_proposal_objects_unchanged':73,'original_evidence_objects_unchanged':852}
ledger={'schema_version':1,'status':'SEALED_UNPUBLISHED_PREFLIGHT_PENDING_REQUIRED_W01_COORDINATOR_COMMUNICATION','scope':'One source-case successor; no independent science reapproval of other187 cases or final owner/export approval.','counts':counts,'draft_complete_selector':binding(D/'HANDOFF.json'),'core_ledgers':{n:binding(D/n) for n in ['decisions.json','proposals.json','evidence.json']},'new_proposal_id':'w03-oxoid-cm0149-product-1224-v1','retired_proposal_id':'b-proposal-cm0149-form','retirement':binding(O/'retirement.json'),'new_payload':binding(O/'candidate/reinforced_clostridial_medium_oxoid_cm0149.yaml'),'candidate_author':'/root/next23_context','source_binding_author':'/root','actual_reviewers':[{'identity':'/root/oxoid_contract','scope':'Original and successor technical accounting, ignored-inclusive duplicate boundary and controls','handoff':binding(A/'technical/HANDOFF.json')},{'identity':'/root/oxoid_primary','scope':'Independent primary-source scientific preflight only; no final acceptance','handoff':binding(A/'science/HANDOFF.json')},{'identity':'/root/oxoid_successor_review','scope':'Separate whole-candidate/source-case/retirement/complete unchanged-proof review of exact draft-v2','handoff':binding(review)}],'complete_object_and_capture_coverage':binding(A/'review/independent-accounting.json'),'preservation':binding(A/'successor-preservation-draft-v2.json'),'native_new_candidate_check':binding(A/'native-candidate-validation.json'),'native_controls':binding(A/'native-negative-controls.json'),'full_shard_auditor':binding(D/'structural-audit.json'),'prior_sealed_reviews':binding(A/'prior-sealed-review-preservation.json'),'tracked_preservation':binding(A/'tracked-preservation-after.json'),'publication_condition':{'received':False,'requirement':'Coordinator communication of completed W01 independent review of nine exact v4 successors, including findings and dispositions.','authority':binding(O/'context/author-task.md')},'published':False,'maintained_application':False,'whole_owner_approval':False,'role_approval':False,'supported_export_approval':False}
dump(A/'machine-ledger.json',ledger)
report_files=[{'path':str(p.relative_to(O)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(O.rglob('*')) if p.is_file() and p.name!='PREFLIGHT-MANIFEST.json']
dump(O/'PREFLIGHT-MANIFEST.json',{'status':'Unpublished immutable draft materials, not an active application selector','files':report_files})
exclude={'HANDOFF.json','MANIFEST.json','SHA256SUMS'};private_files=[]
for p in sorted(A.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(A)
 if len(rel.parts)==1 and p.name in exclude:continue
 if '__pycache__' in rel.parts or rel.as_posix()=='science/primary-fetch-results.json':continue
 private_files.append({'path':str(rel),'sha256':sha(p),'bytes':p.stat().st_size})
dump(A/'MANIFEST.json',{'files':private_files,'excluded':['science/primary-fetch-results.json: private transient public response cookie header; exact source body and sanitized public transport separately retained','runtime __pycache__'],'report_draft_manifest':binding(O/'PREFLIGHT-MANIFEST.json')})
handoff={'schema_version':1,'status':ledger['status'],'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'local_head':'1196d5bc3aaba7563b829d5cbe7e54722fccc35d','remote_head_observed':'1196d5bc3aaba7563b829d5cbe7e54722fccc35d','remote_observation':'Fresh successful read-only git ls-remote after final preflight checks','counts':counts,'machine_ledger':binding(A/'machine-ledger.json'),'assessment':binding(A/'ASSESSMENT.md'),'manifest':binding(A/'MANIFEST.json'),'report_draft_manifest':binding(O/'PREFLIGHT-MANIFEST.json'),'review_receipt':binding(review),'independent_review_yaml':binding(A/'review/review.yaml'),'independent_review_markdown':binding(A/'review/review.md'),'complete_draft_selector':binding(D/'HANDOFF.json'),'active_published_selector':'Original published worker03/HANDOFF.json at1196d5bc; no replacement published','next_action':'Await required coordinator W01 exact-review/findings disposition. Bind actual receipt, prepare separately immutable final complete selector with exact review metadata and final independent currentness check, then authorized ordinary commit/non-force push; no new permission needed.','no_commit_or_push':True,'no_maintained_edits':True,'no_github_mutation':True,'no_external_session_or_paid_provider':True}
dump(A/'HANDOFF.json',handoff)
# Transport over every declared private member plus root manifest and handoff.
with (A/'SHA256SUMS').open('x') as f:
 for x in private_files:f.write(x['sha256']+'  '+x['path']+'\n')
 for p in [A/'MANIFEST.json',A/'HANDOFF.json']:f.write(sha(p)+'  '+p.name+'\n')
assert all(sha(A/x['path'])==x['sha256'] for x in private_files)
assert all(sha(O/x['path'])==x['sha256'] for x in report_files)
print(json.dumps({'HANDOFF':sha(A/'HANDOFF.json'),'machine_ledger':sha(A/'machine-ledger.json'),'MANIFEST':sha(A/'MANIFEST.json'),'SHA256SUMS':sha(A/'SHA256SUMS'),'private_members':len(private_files),'report_members':len(report_files),'publication':'not performed; explicit W01 communication pending'},indent=2))
