from pathlib import Path
import json,hashlib,datetime,subprocess,shutil
R=Path('reports/all_unmatched_20261107/worker-06');S=R/'successor-v2';F=S/'final'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,j):p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
review=S/'research-a/final-successor-diff-review.json';r=json.loads(review.read_text());print('Independent final diff verdict',r.get('verdict',r.get('status')))
checks=json.loads((F/'validation-status.json').read_text())['current_required_checks'];assert all(x['status']=='PASS' and x['exit_code']==0 for x in checks)
sel=json.loads((F/'selection.json').read_text());native=[]
for kind in ['stock','merck']:
 j=json.loads((F/f'logs/native-{kind}-save.json').read_text());native.extend(Path(p).relative_to(Path.cwd()) for p in j.values())
dump(F/'completion.json',{'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'worker_slot':6,'branch':subprocess.check_output(['git','branch','--show-current'],text=True).strip(),'parent_published_commit':'d5a7613c931d45d057eaca7b5ec15280aca76c9e','current_authoritative_selection':{'path':str(F/'selection.json'),'sha256':sha(F/'selection.json')},'old_proposal_ledger':{'path':str(R/'proposals.json'),'sha256':sha(R/'proposals.json'),'count':100},'new_proposal_ledger':{'path':str(F/'proposals.json'),'sha256':sha(F/'proposals.json'),'count':99},'case_count':188,'newly_reassessed_case_indices':[19,35,133,183],'unchanged_case_count':184,'unchanged_selected_payload_count':97,'evidence_count':1066,'original_evidence_entries_preserved':1056,'all_100_original_payloads_preserved':True,'all_1758_prior_manifest_files_preserved':True,'downstream_holds_preserved':88,'independent_receipts':{str(p):sha(p) for p in [S/'research-b/scientific-review.json',S/'research-b/merck-label-delta-review.json',S/'research-b/final-binding-v2.json',review]},'native_reviews':[{'path':str(p),'sha256':sha(p)} for p in native],'required_validation_status':'PASS','maintained_changes':False,'source_owner_export_approval':False,'merge_pr_or_downstream_rebuild_performed':False,'extra_external_sessions_started':0,'publication':'Ordinary commit/push of the enclosing commit; exact head and remote readback reported in session completion.'})
shutil.copyfile(Path(__file__),F/'validation-scripts/manifest.py')
files=sorted([p for p in S.rglob('*') if p.is_file() and p.name!='SHA256SUMS']+native);assert not any(p.is_symlink() for p in files)
m=S/'SHA256SUMS';m.write_text(''.join(sha(p)+'  '+str(p)+'\n' for p in files))
for line in m.read_text().splitlines():
 h,p=line.split('  ',1);assert sha(Path(p))==h,p
for line in (R/'SHA256SUMS').read_text().splitlines():
 h,p=line.split('  ',1);assert sha(Path(p))==h,p
print('Verified successor manifest',len(files),'files SHA256',sha(m));print('Original evidence manifest remains exact',sha(R/'SHA256SUMS'))
