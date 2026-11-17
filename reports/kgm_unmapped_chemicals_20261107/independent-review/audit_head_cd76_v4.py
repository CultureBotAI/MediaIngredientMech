from pathlib import Path
import json,csv,io,subprocess,hashlib,ast,collections,datetime
T=Path(__file__).resolve().parents[1];W=T/'worktree';R=T/'reviewer';head='cd76b3e5d3475545f68b65cd765a876ca61e0a2b';base='0dac278466699129a083343a921c2e0ca18a9ab4';REPORT='reports/kgm_unmapped_chemicals_20261107/'
def git(*args):return subprocess.check_output(['git',*args],cwd=W)
def blob(rev,p):return git('show',rev+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def table(b):return list(csv.DictReader((s for s in b.decode().splitlines() if not s.startswith('#')),delimiter='\t'))
assert git('rev-parse','HEAD').decode().strip()==head
changes=git('diff','--name-status','-z',base,head).decode().split('\0');changes=[tuple(changes[i:i+2]) for i in range(0,len(changes)-1,2)]
olddec=table(blob(base,'reports/semantic_review_20260921/resolution/assertion-dispositions.tsv'));newdec=table(blob(head,'reports/semantic_review_20260921/resolution/assertion-dispositions.tsv'))
assert len(olddec)==len(newdec)
nonmap=[];mapping=[]
for a,b in zip(olddec,newdec,strict=True):
 assert all(a[k]==b[k] for k in ('source_record','assertion_type','source_position'))
 if a==b:continue
 (mapping if a['assertion_type']=='mapping' else nonmap).append({'before':a,'after':b})
assert len(nonmap)==1
role=nonmap[0]; assert role['before']['source_record']=='data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml' and role['before']['resolution_status']=='APPROVED' and role['after']['resolution_status']=='OPEN'
assert role['before']['assertion_sha256']==role['after']['assertion_sha256']
mapstatus=[x for x in mapping if x['before']['resolution_status']!=x['after']['resolution_status']];assert not mapstatus
oldreview=json.loads(blob(base,'reports/sssom_completion_20260921/review.json'));review=json.loads(blob(head,'reports/sssom_completion_20260921/review.json'))
assert [x['disposition'] for x in oldreview['decisions']]==[x['disposition'] for x in review['decisions']]
mdiff=[i+1 for i,(a,b) in enumerate(zip(oldreview['decisions'],review['decisions'],strict=True)) if a!=b]; assert mdiff==[2556]
assert len(review['decisions'])==3014
manifest=json.loads(blob(head,REPORT+'candidate-reviewed-sssom/manifest.json'))
assert manifest['review_sha256']==sha(blob(head,'reports/sssom_completion_20260921/review.json')) and manifest['source_sha256']==sha(blob(head,'mappings/ingredient_mappings.sssom.tsv'))
for p,d in manifest['files'].items():assert sha(blob(head,REPORT+'candidate-reviewed-sssom/'+p))==d
assert manifest['files']['withheld_mappings.sssom.tsv']==sha((R/'baseline-reviewed-export-v1/withheld_mappings.sssom.tsv').read_bytes())
oldcomp=json.loads(blob(base,'reports/owned_name_deferred_669_20261103/companion-review.json')); comp=json.loads(blob(head,REPORT+'companion-review.json'))
assert comp['decisions']==oldcomp['decisions'] and comp['record_inputs']==oldcomp['record_inputs'] and comp['claims_sha256']==oldcomp['claims_sha256']
assert blob(head,REPORT+'companion-review.json')==blob(head,REPORT+'companion-review-v2.json')
audit=json.loads(blob(head,REPORT+'companion-refresh-v2.json'));assert not audit['scientific_approval_added']
for p,d in audit['source_alias_addition']['input_sha256'].items():assert sha(blob(head,p))==d
assert [x for x in changes if x[1].startswith('.github/')]==[('M','.github/workflows/qc-reviewed-sssom.yaml')]
oldpath='reports/owned_name_deferred_669_20261103/companion-review.json';newpath=REPORT+'companion-review.json'
for p in ('tests/test_ingredient_bundle.py','.github/workflows/qc-reviewed-sssom.yaml'):assert blob(head,p)==blob(base,p).replace(oldpath.encode(),newpath.encode())
assert all(s=='A' or p=='tests/test_ingredient_bundle.py' for s,p in changes if p.startswith('tests/'))
for p in ('.github/workflows/qc-evidence.yaml','scripts/.vendored_canon_ref','mappings/suppressed_aliases.tsv','mappings/other_cross_record_baseline.tsv'): assert blob(head,p)==blob(base,p)
for p,d in json.loads((R/'implementation-rereview-v1.json').read_bytes())['current_sha256'].items(): assert sha(blob(head,p))==d
receiptpath='reports/sssom_completion_20260921/mapping_changes/issue1149-1151-kgm-source-corrections.json';receipt=json.loads(blob(head,receiptpath));assert receipt['sequence']==27 and receipt['changed_rows']==1 and receipt['added_rows']==receipt['removed_rows']==0 and len(receipt['records'])==2
oldreceipts=git('ls-tree','-r','--name-only','-z',base,'--','reports/sssom_completion_20260921/mapping_changes').decode().split('\0');oldreceipts=[p for p in oldreceipts if p.endswith('.json')];assert len(oldreceipts)==26
for p in oldreceipts:assert blob(base,p)==blob(head,p)
qc=json.loads(blob(head,REPORT+'validation-v1/status.json'))
for p,d in qc['logs'].items(): assert sha(blob(head,REPORT+'validation-v1/'+p))==d
proof={'reviewer':'/root/step7d_independent_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'base':base,'committed_scope_readback':'PASS','all_frozen_repaired_implementations_match':True,'changed_file_count':len(changes),'canonical_rows':3014,'changed_mapping_decisions':mdiff,'mapping_disposition_counts':dict(collections.Counter(x['disposition'] for x in review['decisions'])),'prior26_receipts_byte_preserved':True,'new_receipt_sequence':27,'new_receipt_two_owners_one_changed_row':True,'withheld_export_byte_preserved':True,'reviewed_export_file_hashes':manifest['files'],'companion_owners':len(comp['record_inputs']),'companion_decisions':len(comp['decisions']),'companion_claims_unchanged':True,'paired_selector_only_existing_test_workflow_change':True,'protected_files_unchanged':True,'nonmapping_disposition_changes':nonmap,'other_nonmapping_assertions_unchanged':True,'mapping_semantic_disposition_changes':0,'completed_checks_logs_hash_match':True,'required_checks_pending':qc['pending'],'final_release_approval':False}
p=R/'committed-head-cd76-audit-v1.json';p.write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2))
