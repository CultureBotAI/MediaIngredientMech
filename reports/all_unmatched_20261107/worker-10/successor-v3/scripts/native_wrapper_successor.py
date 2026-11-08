from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,subprocess,yaml
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v3';old=S/'native';N=S/'native-v2';N.mkdir(exist_ok=True);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
review=yaml.safe_load((old/'review-input.yaml').read_text());baseline=copy.deepcopy(review);text='These are unapplied source-qualified proposed HCl preparations with no maintained owner preimage. Coordinator owns cross-source reconciliation and final owner selection; existing pure HCl owner is not the stock and is not to be repurposed.'
finding=next(f for f in review['findings'] if f['finding_id']=='hcl-conditional-reconciliation');finding['ownership_note']=text
action=next(a for a in review['actions'] if a['action_id']=='resolve-hcl-conditional-reconciliation');action['ownership_note']=text
rid=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-w10-family-provenance-successor';review['review_id']=rid;review['finished_at']=now();rollback=copy.deepcopy(review);rollback['review_id']=baseline['review_id'];rollback['finished_at']=baseline['finished_at']
next(f for f in rollback['findings'] if f['finding_id']=='hcl-conditional-reconciliation').pop('ownership_note');next(a for a in rollback['actions'] if a['action_id']=='resolve-hcl-conditional-reconciliation').pop('ownership_note');assert rollback==baseline
class Dumper(yaml.SafeDumper):
 def ignore_aliases(self,data):return True
with (N/'review-input.yaml').open('x') as f:f.write(yaml.dump(review,Dumper=Dumper,sort_keys=False,allow_unicode=True,width=110))
save(N/'wrapper-correction.json',{'at':now(),'old_review_input':{'path':str((old/'review-input.yaml').relative_to(R)),'sha256':sha(old/'review-input.yaml')},'old_failed_validation':{'path':str((old/'validate-command.json').relative_to(R)),'sha256':sha(old/'validate-command.json')},'new_review_input':{'path':str((N/'review-input.yaml').relative_to(R)),'sha256':sha(N/'review-input.yaml')},'changed_fields':['review_id','finished_at','findings[hcl-conditional-reconciliation].ownership_note','actions[resolve-hcl-conditional-reconciliation].ownership_note'],'all_other_content_equal':True,'scientific_payload_changes':False,'reason':'Native validation requires explicit ownership limit for a cross-proposal finding/action without maintained owner paths. Recorded before fixing; failed wrapper and original error remain immutable.'})
for label,cmd in [('validate',['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','validate',str((N/'review-input.yaml').relative_to(R))]),('save',['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','save','--content',str((N/'review-input.yaml').relative_to(R))])]:
 start=now();r=subprocess.run(cmd,text=True,capture_output=True)
 for ext,txt in [('stdout',r.stdout),('stderr',r.stderr)]:
  with (N/(label+'.'+ext)).open('x') as f:f.write(txt)
 save(N/(label+'-command.json'),{'started_at':start,'finished_at':now(),'argv':cmd,'exit_code':r.returncode});assert r.returncode==0,(label,r.stdout,r.stderr)
bundle=R/'reviews/structured'/rid;save(N/'saved-pair.json',{'review_id':rid,'files':[{'path':str(f.relative_to(R)),'sha256':sha(f)} for f in [bundle/'review.yaml',bundle/'review.md']],'targets':len(review['targets']),'native_validate_exit':0,'native_save_exit':0,'fresh_source_cases':18,'selected_proposals':127,'open_findings':len(review['findings']),'selected_wrapper':'native-v2','prior_failed_wrapper_preserved':True,'approval':False});print(json.dumps(json.loads((N/'saved-pair.json').read_text()),indent=2))
