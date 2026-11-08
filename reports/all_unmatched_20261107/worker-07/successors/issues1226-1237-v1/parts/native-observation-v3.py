"""Preserve failed v1 native wrapper; correct only unsupported issue-key syntax."""
import datetime,hashlib,json,os,shutil,subprocess
from pathlib import Path
import yaml
S=Path('reports/all_unmatched_20261107/worker-07/successors/issues1226-1237-v1');N=Path('.temp/worker07-issues1226-1237-v1/native-repo')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def jp(p,x):
    assert not p.exists(),p
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def run(label,args):
    z=subprocess.run(args,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','GIT_OPTIONAL_LOCKS':'0'})
    jp(S/'validation'/(label+'.json'),{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'args':args,'returncode':z.returncode,'stdout':z.stdout,'stderr':z.stderr})
    print(label,z.returncode,z.stdout[-1200:],z.stderr[-1200:],flush=True);assert z.returncode==0
v1=S/'native-review-input-v2.yaml';review=yaml.safe_load(v1.read_text());before=review['findings'][0]['issue_key'];review['findings'][0]['issue_key']='MediaIngredientMech.W07.JCM900-historical-PARTIAL-draft-pointer'
review['actions']=[{'action_id':'coordinator-issue-first','description':'Coordinator deduplicates/files the inherited JCM900 ledger wording lead before any separately authorized correction. Preserve original source and reviews.','finding_ids':['W07-SKEPTIC-LEDGER-PARTIAL-001'],'target_ids':['W07-COMBINED-JCM900-JCM979-Hutner'],'ownership_note':'Coordinator alone controls issue triage and subsequent correction scope.','acceptance_checks':['Bind both exact case IDs and selected complete immediate-input payload; distinguish list completeness from chemical grounding.','Record issue linkage before a separate immutable ledger correction and obtain independent exact-byte re-review; preserve all historical wording and scientific holds.']} ]
now=datetime.datetime.now(datetime.timezone.utc);review['review_id']=now.strftime('%Y%m%dT%H%M%SZ')+'-w07-issues1226-1237-private-correction-v3';review['finished_at']=now.isoformat().replace('+00:00','Z')
class NoAlias(yaml.SafeDumper):
    def ignore_aliases(self,data):return True
f=S/'native-review-input-v3.yaml';assert not f.exists();f.write_text(yaml.dump(review,Dumper=NoAlias,sort_keys=False,allow_unicode=True));out=N/f;out.parent.mkdir(parents=True,exist_ok=True);assert not out.exists();shutil.copyfile(f,out)
command=[str(Path('.temp/all-unmatched-worker-07/venv/bin/python').resolve()),'scripts/record_review.py','--repo-root',str(N.resolve())]
run('native-validate-v3',command+['validate',str(f.resolve())]);run('native-save-v3',command+['save','--content',str(f.resolve())])
saved=N/'reviews/structured'/review['review_id'];shutil.copytree(saved,S/'native-review'/review['review_id'])
jp(S/'native-review-receipt.json',{'review_id':review['review_id'],'private_repo':str(N.resolve()),'private_saved_path':str(saved),'public_yaml':str(S/'native-review'/review['review_id']/'review.yaml'),'yaml_sha256':sha(saved/'review.yaml'),'markdown_sha256':sha(saved/'review.md'),'wrapper_author':'/root','scientific_review':False,'independent_scopes':'Science5payloads8cases; skeptical79fields74changed26unchanged, attached exact receipts.','failed_v1_retained':{'path':str(v1),'sha256':sha(v1),'validation':str(S/'validation/native-validate.json')},'correction':'V1 invalid issue-key syntax and V2 missing open-finding actions retained. V3 adds coordinator issue-first triage action and exact acceptance checks; actual new finish time/review ID. No scientific content or candidate changes.','old_issue_key':before,'new_issue_key':review['findings'][0]['issue_key']})
run('native-check-v3',command+['check','--base','ddef7355bf7814bd3b1a23b9d61327bea3ac75fe','--require-reviews'])
