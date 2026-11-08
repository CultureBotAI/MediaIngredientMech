from pathlib import Path
from datetime import datetime,timezone
import copy,json,hashlib,yaml,subprocess,shlex
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v2';N=S/'native-v2';N.mkdir(exist_ok=True);old=yaml.safe_load((S/'native/review-input.yaml').read_text());review=copy.deepcopy(old);targets=review['targets'];props=json.loads((S/'proposals.json').read_text())['proposals'];byid={p['proposal_id']:p for p in props};now=lambda:datetime.now(timezone.utc).isoformat().replace('+00:00','Z');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def run(label,cmd):
 start=now();r=subprocess.run(cmd,capture_output=True,text=True)
 for suffix,txt in [('stdout',r.stdout),('stderr',r.stderr)]:
  with (N/(label+'.'+suffix)).open('x') as f:f.write(txt)
 receipt={'started_at':start,'finished_at':now(),'argv':cmd,'command':shlex.join(cmd),'exit_code':r.returncode};save(N/(label+'-command.json'),receipt);assert r.returncode==0,(label,r.stdout,r.stderr);return r,receipt
changed=[]
for t in targets:
 if not t['target_id'].startswith('PROPOSAL:'):continue
 p=byid[t['target_id'][9:]]
 if p['kind']=='new_owner':
  oldnote=t['ownership_note'];t['ownership_note']='Unapplied isolated new-owner proposal; intended destination '+p.get('destination_path',p['owner_path'])+'. No maintained owner preimage exists for this proposal (before_sha256 is null). No maintained data edit or owner/export acceptance.';changed.append({'target_id':t['target_id'],'old_note':oldnote,'new_note':t['ownership_note']})
assert len(changed)==83;save(N/'targets.json',{'targets':targets})
cmd=['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','inspect','--targets',str((N/'targets.json').relative_to(R))]
inputs={x['path'] for x in old['source']['inputs'] if x['role']=='context'}|{str((S/'native-metadata-finding-v1.json').relative_to(R)),'reviews/structured/'+old['review_id']+'/review.yaml','reviews/structured/'+old['review_id']+'/review.md'}
for p in sorted(inputs):cmd+=['--input',p]
r,ic=run('inspection',cmd);ins=json.loads(r.stdout);save(N/'inspection.json',ins)
review['targets']=ins['targets'];review['source']=ins['source'];review['review_id']=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-w10-completeness-c001-c002-owner-notes';review['started_at']=ic['started_at'];review['finished_at']=now();review['title']='Worker10 C001/C002 review successor: precise new-owner notes with exact unchanged science'
review['summary']+=' Metadata successor corrects83 target notes that previously called proposed new-owner destinations authentic owners despite null preimages. Scientific/core/payload bytes and all316 target identities are unchanged; original review remains preserved.'
review['related_reviews']=[{'repository':review['repository'],'review_id':old['review_id'],'relationship':'Immutable metadata successor corrects83 new-owner target notes only; retains all316 target identities and open nested-trace integration finding. No prior scientific finding is closed.'}]
for finding in review['findings']:finding['previous_occurrences']=[{'repository':review['repository'],'review_id':old['review_id'],'finding_id':finding['finding_id']}]
for check in review['checks']:
 if check['check_id']=='inspect':check['command']=ic['command'];check['summary']='Native reinspection of same316 source/payload targets with corrected83 new-owner notes; exact unchanged core/payload/context hashes retained, original native pair and correction finding bound.'
review['evidence'].append({'evidence_id':'sv2-native-note-correction','kind':'prior_review','reference':str((S/'native-metadata-finding-v1.json').relative_to(R)),'locator':'Full independent metadata observation;83 new_owner ownership notes only','support':'context_only','summary':'Preparation_skeptic observed misleading target-note wording before correction. New-owner destinations have no maintained preimage; only these notes change.','snapshot_sha256':sha(S/'native-metadata-finding-v1.json'),'accessed_at':ic['started_at']})
review['assessments'].append({'assessment_id':'native-new-owner-note-correction','area':'provenance','topic':'Precise proposed destination versus authentic maintained preimage','outcome':'supported','target_ids':[x['target_id'] for x in changed],'evidence_ids':['sv2-native-note-correction','sv2-wrapper-accounting'],'summary':'All83 new_owner targets now explicitly denote proposed destinations without maintained preimages. All45 existing-owner target notes retain genuine original owner hashes. No ingredient field, proposal core, source decision, or review scope changed.'})
class Dumper(yaml.SafeDumper):
 def ignore_aliases(self,data):return True
with (N/'review-input.yaml').open('x') as f:f.write(yaml.dump(review,Dumper=Dumper,sort_keys=False,allow_unicode=True,width=110))
run('validate',['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','validate',str((N/'review-input.yaml').relative_to(R))])
run('save',['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','save','--content',str((N/'review-input.yaml').relative_to(R))])
bundle=R/'reviews/structured'/review['review_id'];save(N/'saved-pair.json',{'review_id':review['review_id'],'files':[{'path':str(f.relative_to(R)),'sha256':sha(f)} for f in [bundle/'review.yaml',bundle/'review.md']],'native_validate_exit':0,'native_save_exit':0,'targets':316,'fresh_source_cases':2,'retained_case_decisions':186,'open_findings':1,'coordinator_published_head_review_pending':True})
for p in props:assert sha(R/'reports/all_unmatched_20261107/worker-10'/p['after_capture']['path'])==p['after_capture']['sha256']
save(N/'metadata-correction-receipt.json',{'at':now(),'finding_id':'SV2-NATIVE-OWNER-NOTE-001','status':'corrected in immutable successor; original retained','old_pair':json.loads((S/'native/saved-pair.json').read_text()),'new_pair':json.loads((N/'saved-pair.json').read_text()),'target_changes':changed,'exact_unchanged_core':{n:sha(S/n) for n in ['decisions.json','evidence.json','proposals.json']},'selected_payloads_unchanged':128,'scope_change':False,'no_scientific_approval':True})
print(json.dumps(json.loads((N/'saved-pair.json').read_text()),indent=2))
