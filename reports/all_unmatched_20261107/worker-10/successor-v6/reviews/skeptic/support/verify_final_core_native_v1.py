from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,os,re,subprocess,yaml
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v6';P=R/'.temp/all-unmatched-worker-10/successor-v6/skeptic'
HEAD='3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b';C9='c9a96da71a1977014680e5a92e600dfc7e3874db';started=datetime.now(timezone.utc).isoformat();checks=[]
def check(name,v):checks.append({'check':name,'pass':bool(v)})
def sha(b):return hashlib.sha256(b).hexdigest()
def osh(x):return sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def js(p):return json.loads(p.read_text())
def cap(p):return {'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())}
def gitbytes(head,p):return subprocess.check_output(['git','show',head+':'+str(p.relative_to(R))])
def checkbinding(x,label,base=A):check(label+' '+x['path'],sha((base/x['path']).read_bytes())==x['sha256'])
def refs(x,label,base=A):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x and isinstance(x['path'],str):
   path=Path(x['path']);bp=R if x['path'].startswith(('reports/','reviews/','.claude/','docs/','src/')) else base
   if path.is_absolute():bp=Path('/')
   check(label+' '+x['path'],sha((bp/path).read_bytes())==x['sha256'])
  for v in x.values():refs(v,label,base)
 elif isinstance(x,list):
  for v in x:refs(v,label,base)
def loadcore(base):return {k:js(base/f'{k}.json')[k] for k in ['decisions','proposals','evidence']}
final=loadcore(S/'final-core');author=loadcore(S/'author-core');s5=loadcore(A/'successor-v5/final-core')
c9={k:json.loads(gitbytes(C9,A/'successor-v3'/f'{k}.json'))[k] for k in final}
science=js(S/'reviews/skeptic/scientific-review-v1.json');selected=js(S/'selection.json');fr=js(S/'finalization-binding.json');pair=js(S/'native/saved-pair.json')
check('science frozen hash',sha((S/'reviews/skeptic/scientific-review-v1.json').read_bytes())=='9f1c8ed7af03810e51441f423f5054fe02bf3daac4f19cfba5b5488bce2ee582')
check('HEAD predecessor',subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD)
refs(selected,'selection');refs(fr,'finalization');refs(pair,'native saved pair')
for k in s5:check('authentic S5 '+k,(A/'successor-v5/final-core'/f'{k}.json').read_bytes()==gitbytes(HEAD,A/'successor-v5/final-core'/f'{k}.json'))
target_ids={x['proposal_id'] for x in science['payload_assessments']};target_cases=set(science['case_indices']);new_eids=['sv6-independent-assertions','sv6-independent-retention','sv6-native-narrow-validation']
for x in science['payload_assessments']:check('exact scientifically reviewed final payload '+x['proposal_id'],sha((R/x['after']['path']).read_bytes())==x['after']['sha256'])
for key,idkey,allowed in [('decisions','source_index',target_cases),('proposals','proposal_id',target_ids)]:
 check(key+' stable ordered IDs',[x[idkey] for x in final[key]]==[x[idkey] for x in author[key]])
 for b,a in zip(author[key],final[key]):
  ident=a[idkey]
  if ident not in allowed:check(key+' exact untouched '+str(ident),a==b);continue
  expected=copy.deepcopy(b);expected['evidence_ids']+=new_eids
  expected['independent_review']={'status':'complete','evidence_ids':new_eids[:2]}
  expected['component_assertion_successor']['review_state']='complete_for_exact_qualified_source_assertion_correction'
  expected['component_assertion_successor']['independent_review_bindings']=a['component_assertion_successor']['independent_review_bindings']
  refs(a['component_assertion_successor']['independent_review_bindings'],'exact review pointer')
  check(key+' original current source scope preserved '+str(ident),a['component_assertion_successor']['active_assertion_scope']==b['component_assertion_successor']['active_assertion_scope'])
  check(key+' no inherited owner approval '+str(ident),a['component_assertion_successor']['whole_owner_or_export_approval'] is False)
  if key=='proposals':
   expected['review_status_explanation']=a['review_status_explanation']
   check('final limited status '+str(ident),'not blanket-transferred' in a['review_status_explanation'] and 'only for nominal 2009 seven immediate ingredient names' in a['review_status_explanation'])
  check(key+' exact metadata finalization '+str(ident),a==expected)
check('all author evidence retained',final['evidence'][:-3]==author['evidence'])
check('1218 evidence rows and exact three additions',len(final['evidence'])==1218 and [x['evidence_id'] for x in final['evidence'][-3:]]==new_eids)
for x in final['evidence'][-3:]:refs(x['capture'],'new final evidence')
selected_by={x['proposal_id']:x for x in selected['selected_payloads']}
for p in final['proposals']:
 row=selected_by[p['proposal_id']]
 check('selected exact proposal payload '+p['proposal_id'],row['after_capture']==p['after_capture'] and row['case_ids']==p['case_ids'] and row['before_sha256']==p['before_sha256'] and row['owner_path']==p['owner_path'] and row['destination_path']==p.get('destination_path',p['owner_path']))
 checkbinding(p['after_capture'],'all final payload bytes')
bridges=[]
for name,baseline in [('complete-bridge.json',s5),('combined-c9-bridge.json',c9)]:
 bridge=js(S/name);refs({k:v for k,v in bridge.items() if k not in ['all_cases','all_proposals']},name+' references')
 check(name+'315 complete ordered entries',len(bridge['all_cases'])==188 and len(bridge['all_proposals'])==127 and [x['case_id'] for x in bridge['all_cases']]==[x['case_id'] for x in final['decisions']] and [x['proposal_id'] for x in bridge['all_proposals']]==[x['proposal_id'] for x in final['proposals']])
 for row,b,a in zip(bridge['all_cases'],baseline['decisions'],final['decisions']):
  label=name+' case '+str(row['source_index'])
  check(label+' before after exact hashes',row['before_object_sha256']==osh(b) and row['after_object_sha256']==osh(a))
  check(label+' equality and reasoning flags',row['complete_object_exact']==(b==a) and row['reasoning_exact']==(b['reasoning']==a['reasoning']))
  check(label+' source occurrences routing retained',row['source_identity_occurrence_owner_hashes_exact'] and all(b[k]==a[k] for k in ['case_id','case_input_sha256','source','source_index','occurrence_ids','owner_records','disposition','applicability','proposal_ids']) and row['occurrence_ids']==a['occurrence_ids'] and row['proposal_ids']==a['proposal_ids'])
 for row,b,a in zip(bridge['all_proposals'],baseline['proposals'],final['proposals']):
  label=name+' proposal '+row['proposal_id']
  check(label+' before after exact hashes',row['before_proposal_sha256']==osh(b) and row['after_proposal_sha256']==osh(a))
  check(label+' equality flags',row['proposal_object_exact']==(b==a) and row['payload_byte_exact']==(b['after_capture']['sha256']==a['after_capture']['sha256']))
  check(label+' exact source payload owner and no approval',row['old_capture']==b['after_capture'] and row['selected_capture']==a['after_capture'] and row['owner_path']==a['owner_path'] and row['before_owner_sha256']==a['before_sha256'] and row['case_ids']==a['case_ids'] and row['whole_owner_approval'] is False)
 bridges.append({'path':str((S/name).relative_to(R)),'sha256':sha((S/name).read_bytes()),'case_entries':len(bridge['all_cases']),'proposal_entries':len(bridge['all_proposals'])})
account=js(S/'accounting.json')
check('accounting exact counts',account=={'cases':188,'unique_occurrences':304,'proposal_ids':127,'changed_payloads_since_s5':5,'byte_identical_other_payloads_since_s5':122,'affected_case_indices':[65,87,94,102,125,178],'unchanged_complete_case_objects_since_s5':182,'affected_cm_occurrences':12,'source_outcomes_changed':0,'changed_payloads_since_c9':7,'unchanged_complete_case_objects_since_c9':179,'prior_evidence_objects_exact':1212,'evidence_objects':1218,'current_retirements':0})
for name,baseline in [('s5',s5),('c9',c9)]:
 check(name+' changed payload count',sum(a['after_capture']['sha256']!=b['after_capture']['sha256'] for a,b in zip(final['proposals'],baseline['proposals']))==(5 if name=='s5' else 7))
 check(name+' retained complete cases',sum(a==b for a,b in zip(final['decisions'],baseline['decisions']))==(182 if name=='s5' else 179))
prior_file_count=0
for directory in ['successor-v4','successor-v5']:
 paths=subprocess.check_output(['git','ls-tree','-r','--name-only','-z',HEAD,'--',str((A/directory).relative_to(R))]).decode().split('\0')
 for path in filter(None,paths):
  p=R/path;check('prior sealed tracked bytes '+path,p.read_bytes()==gitbytes(HEAD,p));prior_file_count+=1
nativepath=R/pair['files'][0]['path'];native=yaml.safe_load(nativepath.read_text());native_md=R/pair['files'][1]['path']
check('native author self-review honestly typed',native['reviewer']['independence']=='self_review' and 'Root authored' in native['reviewer']['independence_basis'] and 'authored the original four S1 HCl' in native['reviewer']['independence_basis'])
check('native exact base and working tree',native['source']['git_revision']==HEAD and native['source']['state']=='working_tree')
check('native complete bounded verdict',native['completion']=='completed' and native['verdict']=='pass_with_limitations' and native['scientific_review'] is True)
check('native exact11 targets',len(native['targets'])==11 and len(native['assessments'])==11 and native['scope']['population_size']==11)
expected_targets={'PROPOSAL:'+pid for pid in target_ids}|{x['case_id'] for x in final['decisions'] if x['source_index'] in target_cases}
check('native exact assessed IDs',set(native['scope']['reviewed_target_ids'])==expected_targets=={x['target_id'] for x in native['targets']}=={i for x in native['assessments'] for i in x['target_ids']})
for t in native['targets']:
 if t['kind']=='snapshot_row':
  i=int(re.fullmatch(r'\$\.decisions\[(\d+)\]',t['selector']).group(1));check('native exact case selector '+t['target_id'],final['decisions'][i]['case_id']==t['target_id'] and i in target_cases)
 else:check('native exact payload path '+t['target_id'],t['path']==str((A/next(x['after_capture']['path'] for x in final['proposals'] if 'PROPOSAL:'+x['proposal_id']==t['target_id'])).relative_to(R)))
for x in native['source']['inputs']:check('native input '+x['path'],sha((R/x['path']).read_bytes())==x['sha256'])
for x in native['evidence']:check('native exact evidence '+x['evidence_id'],sha((R/x['reference']).read_bytes())==x['snapshot_sha256'])
for a in native['assessments']:
 check('positive bounded assessment '+a['assessment_id'],a['outcome']=='supported')
 details=json.loads(a['details'])
 if a['assessment_id'].startswith('ASSERTION'):
  refs(details['after_capture'],'native assessed after');refs(details['before_capture'],'native assessed before');check('native no owner approval '+a['assessment_id'],details['whole_owner_or_release_approval'] is False)
 else:check('native no source acceptance '+a['assessment_id'],details['fresh_whole_owner_or_source_acceptance'] is False)
check('native finding closure not fabricated',native['findings']==[] and native['actions']==[] and any('No historical native finding or GitHub issue is closed' in x for x in native['limitations']))
preflight=js(S/'preflight.json');start=datetime.fromisoformat(native['started_at'].replace('Z','+00:00'));finish=datetime.fromisoformat(native['finished_at'].replace('Z','+00:00'))
check('native timing exact milestone',start==datetime.fromisoformat(preflight['at']) and finish>start and any('Exact earlier reading start is unknown' in x for x in native['limitations']))
commands=[];env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
for label,args in [('validate',['validate',str(nativepath)]),('render',['render','--content',str(nativepath)])]:
 cmd=[str(R/'.temp/all-unmatched-worker-10/venv/bin/python'),'scripts/record_review.py',*args]
 run=subprocess.run(cmd,capture_output=True,env=env);check('independent native '+label+' exit0',run.returncode==0)
 if label=='render':check('canonical rendered Markdown byte parity',run.stdout==native_md.read_bytes())
 record={'command':cmd,'exit_code':run.returncode,'stdout_sha256':sha(run.stdout),'stderr':run.stderr.decode()}
 for suffix,data in [('stdout',run.stdout),('stderr',run.stderr)]:
  with (P/f'final-native-{label}-v1.{suffix}').open('xb') as f:f.write(data)
 commands.append(record)
check('final HEAD unchanged',subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD)
out={'started_at':started,'finished_at':datetime.now(timezone.utc).isoformat(),'reviewer':'OpenAI Codex /root/preparation_skeptic','scope':'Final core/bridges/native bindings and retained byte accounting; no renewed science or future publication-head acceptance. Handoff/completed full native check are separate pending inputs.','checks':checks,'check_count':len(checks),'failures':[x for x in checks if not x['pass']],'bridges':bridges,'prior_s4_s5_files_compared_to_head':prior_file_count,'native_inputs':len(native['source']['inputs']),'native_targets':len(native['targets']),'native_evidence':len(native['evidence']),'commands':commands,'bindings':[cap(S/x) for x in ['final-core/decisions.json','final-core/proposals.json','final-core/evidence.json','selection.json','complete-bridge.json','combined-c9-bridge.json','accounting.json','finalization-binding.json','native/saved-pair.json','issue-linked-correction.json']]+[cap(nativepath),cap(native_md)]}
dest=P/'final-core-native-verification-v1.json'
with dest.open('x') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'path':str(dest),'sha256':sha(dest.read_bytes()),'checks':len(checks),'failures':out['failures'],'prior_files':prior_file_count,'native_inputs':out['native_inputs']},indent=2))
