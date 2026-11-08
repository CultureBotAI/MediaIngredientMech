"""Bounded v2-to-v3 metadata rebind and real external-origin byte verification."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,time
import yaml
R=Path.cwd();P=Path(__file__).resolve().parent;A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7';checks=[];inputs={};commands=[];start=datetime.now(timezone.utc).isoformat();clock=time.monotonic()
def sha(b):return hashlib.sha256(b).hexdigest()
def raw(p):
 b=Path(p).read_bytes();inputs[str(p)]=sha(b);return b
def read(p):return json.loads(raw(p))
def ck(n,v):
 checks.append({'name':n,'pass':bool(v)});assert v,n
def cap(r):
 p=A/r['path'];ck('hash '+r['path'],sha(raw(p))==r['sha256']);return p
def canonical(x):return sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
f2=read(S/'author-freeze-v2.json');f3=read(S/'author-freeze-v3.json');v2={n:read(cap(r)) for n,r in f2['core'].items()};v3={n:read(cap(r)) for n,r in f3['core'].items()}
for n in ['proposals.json','evidence.json']:ck(n+' byte-exact v2 to v3',raw(cap(f2['core'][n]))==raw(cap(f3['core'][n])))
newkeys={'old_completion_reassessment_is_historical','historical_completion_reassessment_preserved','active_component_assertion','historical_enum_finding'}
for i,(old,new) in enumerate(zip(v2['decisions.json']['decisions'],v3['decisions.json']['decisions'])):
 if i not in [80,135]:ck('unchanged case '+str(i),old==new);continue
 ck('two exact marker additions '+str(i),set(new['source_successor_v7'])==set(old['source_successor_v7'])|newkeys)
 rolled=json.loads(json.dumps(new))
 for k in newkeys:rolled['source_successor_v7'].pop(k)
 ck('no other case edit '+str(i),rolled==old)
 ck('historical object retained '+str(i),new['completion_reassessment']==old['completion_reassessment'])
 marker=new['source_successor_v7'];ck('historical attribution explicit '+str(i),marker['old_completion_reassessment_is_historical'] is True and 'historical' in marker['historical_completion_reassessment_preserved'] and 'UNKNOWN' in marker['historical_completion_reassessment_preserved'])
 active=marker['active_component_assertion'];payload=yaml.safe_load(raw(cap(active['selected_capture'])));ck('active assertion real selected bytes '+str(i),active['method']==payload['component_assertion']['method']=='LABEL_ENUMERATION' and active['completeness']==payload['component_assertion']['completeness']=='UNKNOWN')
 cap(marker['historical_enum_finding']['captured_finding'])
for row in f3['unchanged_four_payloads']:cap(row['after_capture'])
ck('four payload refs exact',f2['unchanged_four_payloads']==f3['unchanged_four_payloads'])
routing=read(S/'source-routing.json');source_contexts=[]
for row in routing['seven_context_rows']:
 p=cap(row['source_recipe_capture']);doc=yaml.safe_load(raw(p));field,index=row['context_id'].rsplit(':',1)[1].split('/');actual=doc[field][int(index)]
 ck('full context raw component '+row['context_id'],actual==json.loads(row['original_occurrence_row']['ingredient_json']))
 ck('literal context quantity '+row['context_id'],actual['concentration']==row['exact_source_quantity'])
 source_contexts.append({'context_id':row['context_id'],'snapshot':str(p),'sha256':sha(raw(p)),'raw_component':actual,'route_supported':row['route_supported'],'target':row['target_proposal_id']})
dep=read(S/'cross-worker-dependencies.json');w04=R.parents[2]/'workers/w04/worktree';w=dep['W04_origin'];rev=w['selected_head'];prefix='reports/all_unmatched_20261107/worker-04/'
def git(args):
 r=subprocess.run(['git','-C',str(w04),*args],capture_output=True);commands.append({'argv':r.args,'exit_code':r.returncode,'stdout_sha256':sha(r.stdout),'stderr':r.stderr.decode()});ck('W04 readonly Git command',r.returncode==0);return r.stdout
ck('current observed W04 selected head',git(['rev-parse','HEAD']).decode().strip()==rev)
blob=git(['show',rev+':'+prefix+w['original_proposal']['after_capture']['path']]);ck('actual W04 payload Git bytes match dependency',sha(blob)==w['payload_capture']['sha256']==sha(raw(cap(w['payload_capture']))))
proposals=json.loads(git(['show',rev+':'+prefix+'successors/final-review-v1/proposals.json']))['proposals'];actual=next(p for p in proposals if p['proposal_id']==w['proposal_id']);ck('actual W04 proposal complete object preserved',actual==w['original_proposal'])
ck('W04 new-owner null-before retained',actual['kind']=='new_owner' and actual['before_sha256'] is None)
for p in ['inputs/historical-completeness-finding-v1.json','historical-enum-correction.json','author-draft-binding-finding.json','scripts/build_candidates.py']:raw(S/p)
result={'status':'PASS','started_at':start,'finished_at':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.monotonic()-clock,'checks':checks,'input_hashes':inputs,'script_sha256':sha(Path(__file__).read_bytes()),'commands':commands,'author_v3_core':f3['core'],'only_changed_case_indices':[80,135],'unchanged_other_cases':186,'payloads_proposals_evidence_unchanged':True,'source_contexts':source_contexts,'W04_origin':{'head':rev,'proposal_id':w['proposal_id'],'proposal_canonical_sha256':canonical(actual),'actual_git_payload_sha256':sha(blob),'source_authorship_not_taken':True,'not_selected_in_W10_overlay':True},'historical_enum_finding':'Implemented precise clarification verified; scientist owns scientific finding disposition. No issue closure.','scientific_review':False}
with (P/'author-v3-rebind.json').open('x') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'status':'PASS','checks':len(checks),'report_sha256':sha((P/'author-v3-rebind.json').read_bytes())},indent=2))
