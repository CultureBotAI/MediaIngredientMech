from pathlib import Path
import copy,datetime,hashlib,importlib.util,json,subprocess,sys
sys.dont_write_bytecode=True
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v4';V=A/'successor-v3';P=R/'.temp/all-unmatched-worker-10/successor-v4/skeptic'
N=R/'reviews/structured/20261108T082153Z-w10-carbonate-completeness-successor'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
load=lambda p:json.loads(p.read_bytes())
bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
checks=[]
def ck(label,value):checks.append({'check':label,'pass':bool(value)})
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
science=load(S/'reviews/skeptic/scientific-review-v1.json')
ck('frozen science report exact',sha(S/'reviews/skeptic/scientific-review-v1.json')=='fcae3c77d942d2aeb29134d50e5c554f0ca452aed49f1908d623af5336feb98a')
F={k:load(S/'final-core'/f'{k}.json')[k] for k in ['decisions','proposals','evidence']}
C={k:load(S/'author-core'/f'{k}.json')[k] for k in F}
B={k:load(V/f'{k}.json')[k] for k in F}
selection=load(S/'selection-v2.json');bridge=load(S/'complete-bridge.json');correction=load(S/'report-metadata-correction-v1.json')
for k,v in selection['authoritative_core'].items():ck('selected final core '+k,sha(A/v['path'])==v['sha256'])
ck('full population',len(F['decisions'])==188 and len(F['proposals'])==127 and len(F['evidence'])==1206)
ck('all304 raw occurrence bindings exact',[d['occurrence_ids'] for d in F['decisions']]==[d['occurrence_ids'] for d in B['decisions']] and len({o for d in F['decisions'] for o in d['occurrence_ids']})==304)
ck('selection and bridge full populations',len(selection['selected_payloads'])==len(bridge['all_proposals'])==127 and len(bridge['all_cases'])==188)
newids=['sv4-independent-completeness','sv4-independent-retention','sv4-native-narrow-validation']
binding_rows=[{'path':'successor-v4/reviews/skeptic/scientific-review-v1.json','sha256':sha(S/'reviews/skeptic/scientific-review-v1.json')},{'path':'successor-v4/reviews/retention/author-core-retention-review-v1.json','sha256':sha(S/'reviews/retention/author-core-retention-review-v1.json')}]
for group in ['decisions','proposals']:
 for i,(a,b) in enumerate(zip(C[group],F[group])):
  changed=i in ([21,187] if group=='decisions' else [80])
  if not changed:ck(f'complete retained author object {group}[{i}]',a==b);continue
  x=copy.deepcopy(b)
  ck(f'exact new review evidence {group}[{i}]',b['evidence_ids']==a['evidence_ids']+newids and b['independent_review']=={'status':'complete','evidence_ids':newids[:2]})
  m=x['completeness_successor'];ck(f'bounded complete review {group}[{i}]',m['review_state']=='complete_for_exact_bounded_completeness_correction' and m['independent_review_bindings']==binding_rows)
  m.pop('independent_review_bindings');m['review_state']=a['completeness_successor']['review_state']
  x['evidence_ids']=a['evidence_ids'];x['independent_review']=a['independent_review']
  if group=='proposals':
   ck('target scoped review explanation','not transferred by this bounded bridge' in x['review_status_explanation'])
   x['review_status_explanation']=a['review_status_explanation']
  ck(f'exact finalization rollback {group}[{i}]',x==a)
for i,(old,new,b) in enumerate(zip(B['decisions'],F['decisions'],bridge['all_cases'])):
 ck(f'full case bridge {i}',b['source_index']==i and b['case_id']==new['case_id'] and b['before_full_object_sha256']==canon(old) and b['after_full_object_sha256']==canon(new) and b['exact_complete_object']==(old==new) and b['occurrence_ids']==new['occurrence_ids'] and b['proposal_ids']==new['proposal_ids'])
for i,(old,new,b,s) in enumerate(zip(B['proposals'],F['proposals'],bridge['all_proposals'],selection['selected_payloads'])):
 ck(f'full proposal bridge {i}',b['proposal_id']==new['proposal_id'] and b['before_proposal_sha256']==canon(old) and b['after_proposal_sha256']==canon(new) and b['old_capture']==old['after_capture'] and b['selected_capture']==new['after_capture'] and b['case_ids']==new['case_ids'] and b['owner_path']==new['owner_path'] and b['before_owner_sha256']==new['before_sha256'] and b['whole_owner_approval'] is False)
 ck(f'complete selected projection {i}',all(s[k]==new.get('destination_path',new['owner_path']) if k=='destination_path' else s[k]==new[k] for k in s))
 ck(f'selected payload exact hash {i}',sha(A/new['after_capture']['path'])==new['after_capture']['sha256'])
 ck(f'retained or bounded selection {i}',i==80 or old==new)
ck('current no retirements; earlier retirement provenance exact',bridge['current_proposals_retired']==[] and sha(A/bridge['earlier_retirement_bridge']['path'])==bridge['earlier_retirement_bridge']['sha256'])
ck('old1200 evidence full objects exact',F['evidence'][:1200]==B['evidence'])
for i,c in enumerate(correction['changes'],1200):
 a,b=C['evidence'][i],F['evidence'][i];x=copy.deepcopy(b);x['kind']=a['kind']
 ck('only disclosed new evidence kind correction '+c['evidence_id'],a['evidence_id']==b['evidence_id']==c['evidence_id'] and a['kind']==c['before_kind'] and b['kind']==c['after_kind'] and x==a)
for e in F['evidence'][1200:]:ck('new exact evidence '+e['evidence_id'],sha(A/e['capture']['path'])==e['capture']['sha256'])
ck('only exact3 review evidence appended',[e['evidence_id'] for e in F['evidence'][1203:]]==newids)
ck('metadata successor decisions/proposals exact root assembled copies',(S/'decisions.json').read_bytes()==(S/'final-core/decisions.json').read_bytes() and (S/'proposals.json').read_bytes()==(S/'final-core/proposals.json').read_bytes())
rootE=load(S/'evidence.json')['evidence'];restored=copy.deepcopy(F['evidence'])
for i in range(1200,1203):restored[i]['kind']=rootE[i]['kind']
ck('metadata successor only3kind changes to root assembled evidence',restored==rootE)
spec=importlib.util.spec_from_file_location('native_review_readonly',R/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
n=mod.load_document((N/'review.yaml').read_text())
try:mod.validate_review(n);mod.assert_current_source(R,n);native_error=None
except Exception as ex:native_error=repr(ex)
ck('independent native validate/current_source',native_error is None)
ck('independent native Markdown parity',mod.render_markdown(n)==(N/'review.md').read_text())
ck('exact native pair freeze',sha(N/'review.yaml')=='f4b47ec24dcef4b231fc31a3f93d8fde22920214058c97de78947bc88434398e' and sha(N/'review.md')=='1096c2361d5c4899caa63dc4a335489b88c52b3ecc6558850322cd0d4ae76ea6')
ck('truthful existing base and workingtree',n['source']['git_revision']==selection['predecessor_head']=='c9a96da71a1977014680e5a92e600dfc7e3874db' and n['source']['state']=='working_tree')
ck('three exact native targets',len(n['targets'])==len(n['assessments'])==n['scope']['population_size']==3 and set(n['scope']['reviewed_target_ids'])=={t['target_id'] for t in n['targets']})
for i,t in enumerate(n['targets']):
 if i==0:ck('native exact proposal target',(R/t['path']).read_bytes()==(A/F['proposals'][80]['after_capture']['path']).read_bytes())
 else:
  j=[21,187][i-1];ck(f'native exact case selector {j}',t['path']==str((S/'final-core/decisions.json').relative_to(R)) and t['selector']==f'$.decisions[{j}]' and t['target_id']==F['decisions'][j]['case_id'])
  details=json.loads(n['assessments'][i]['details']);ck(f'native exact case assessment {j}',details['source_index']==j and details['case_id']==F['decisions'][j]['case_id'] and details['completeness_successor']==F['decisions'][j]['completeness_successor'] and details['fresh_source_association_approval'] is False)
for b in n['source']['inputs']:ck('native current input '+b['path'],sha(R/b['path'])==b['sha256'])
for e in n['evidence']:ck('native evidence exact '+e['evidence_id'],sha(R/e['reference'])==e['snapshot_sha256'])
ck('no terminal original finding closure',n['findings']==n['actions']==[] and 'does not rewrite/close' in ' '.join(n['limitations']))
ck('native scientific scope explicitly bounded',n['scientific_review'] is True and 'only the fresh source-relative completeness' in ' '.join(n['limitations']) and 'not reapproved' in ' '.join(n['limitations']))
ck('truthful actual mixed authorship and missed defect',n['reviewer']['independence']=='self_review' and 'Root authored' in n['reviewer']['independence_basis'] and 'without catching this inherited completeness defect' in n['reviewer']['independence_basis'])
ck('prior science and candidate immutable',sha(S/'reviews/skeptic/scientific-review-v1.json')=='fcae3c77d942d2aeb29134d50e5c554f0ca452aed49f1908d623af5336feb98a' and sha(S/'proposed/carbonate_co2_nominal4percent_togo_m202.yaml')=='135788bfd2a511671a90ff9b912092df789c9209995f88d11b4aa6134eca0625')
ck('source HEAD unchanged',subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()==selection['predecessor_head'])
out={'started_at':start,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if all(x['pass'] for x in checks) else 'FAIL','checks':checks,'check_count':len(checks),'failures':[x for x in checks if not x['pass']],'input_bindings':[bind(S/'selection-v2.json'),bind(S/'complete-bridge.json'),bind(S/'report-metadata-correction-v1.json'),*[bind(S/'final-core'/f'{k}.json') for k in F],bind(N/'review.yaml'),bind(N/'review.md')],'native_error':native_error,'native_inputs_verified':len(n['source']['inputs']),'native_targets_verified':len(n['targets']),'native_evidence_verified':len(n['evidence']),'scope':'Final core/full retention bridge and exact native metadata only; frozen completeness scientific review remains unchanged. Handoff and full native check receipt are assessed separately when ready.'}
with (P/'final-assembly-verification-v2.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'status':out['status'],'checks':out['check_count'],'failures':out['failures'],'receipt':bind(P/'final-assembly-verification-v2.json')}))
