"""Independent, isolated controls for successor assembly/native/overlay guards.

Only synthetic fixtures under private .temp are mutated. The copied production
scripts have identical bytes; Git baseline reads are mocked only for the tiny
overlay fixture. No real proposal, source capture or maintained file is changed.
"""
from pathlib import Path
import contextlib, copy, datetime, hashlib, importlib.util, io, json, runpy, shutil
from unittest.mock import patch
import yaml

S=Path(__file__).resolve().parents[1];R=S.parents[4]
PRIVATE=R/'.temp/all-unmatched-worker-04/issue-1201-v1/process-controls'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
can=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+'\n')
def load(p):return json.loads(p.read_text())
results=[]
source_hashes={str(p.relative_to(S)):sha(p) for p in (S/'scripts').glob('*.py')}
real_inputs={p:sha(p) for p in list((S/'fragments').glob('*.json'))+list((S/'proposals').rglob('*.yaml'))+list((S/'scripts').glob('*.py'))}
PRIVATE.mkdir(parents=True,exist_ok=True)
dump(PRIVATE/'real-input-bindings-at-start.json',{'files':[{'path':str(p),'sha256':h} for p,h in real_inputs.items()]})
def fresh(name):
 root=PRIVATE/name
 if root.exists():shutil.rmtree(root)
 work=root/'reports/all_unmatched_20261107/worker-04';s=work/'successors/issue-1201-v1'
 (s/'validation').mkdir(parents=True);(s/'scripts').mkdir()
 for file in ['assemble_successor.py','build_native_review.py','validate_overlay.py']:
  shutil.copyfile(S/'scripts'/file,s/'scripts'/file);assert sha(s/'scripts'/file)==sha(S/'scripts'/file)
 return root,work,s
def module(p):
 spec=importlib.util.spec_from_file_location('fixture_'+hashlib.sha256(str(p).encode()).hexdigest(),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def record(name,expected_fail,fn,contains=None):
 try:
  with contextlib.redirect_stdout(io.StringIO()):fn()
  failed=False;message='accepted synthetic positive control'
 except (AssertionError,SystemExit,KeyError,FileNotFoundError) as ex:
  failed=True;message=str(ex)
  if isinstance(ex,SystemExit) and ex.code in (0,None):failed=False;message='accepted synthetic positive control'
 ok=failed==expected_fail and (not contains or contains in message)
 results.append({'name':name,'expected_rejection':expected_fail,'rejected':failed,'message':message,'status':'PASS' if ok else 'FAIL'})
 assert ok,results[-1]

def assembly_fixture(name):
 root,w,s=fresh(name);prior=[];props=[]
 for i in range(188):
  pid=[] if i<108 else ['old-p-'+str(i)]
  prior.append({'case_id':'c'+str(i),'case_input_sha256':'a'*64,'source':{'source_label':'source'+str(i)},'occurrence_ids':['o'+str(i)],'proposal_ids':pid,'evidence_ids':['EOLD'],'independent_review':{'status':'complete','evidence_ids':['EOLD']},'preserved_holds':['KEEP'],'reasoning':'synthetic original'})
  if pid:props.append({'proposal_id':pid[0],'case_ids':['c'+str(i)],'owner_path':'data/ingredients/mapped/old'+str(i)+'.yaml','before_sha256':None,'after_capture':{'root':'artifact','path':'old-'+str(i)+'.yaml','sha256':'b'*64},'evidence_ids':['EOLD']})
 dump(w/'decisions.json',{'decisions':prior});dump(w/'evidence.json',{'evidence':[{'evidence_id':'EOLD'}]});dump(w/'proposals.json',{'proposals':props})
 selection={}
 for group,indices in [('biological',range(38)),('chemistry',range(38,82)),('media',range(82,108))]:
  ass=[{'case_id':prior[i]['case_id'],'old_decision_sha256':can(prior[i]),'reasoning':'synthetic reassessment'} for i in indices]
  ds=[];ps=[]
  if group=='biological':
   d=copy.deepcopy(prior[0]);d['proposal_ids']=['NEW'];ds=[d]
   payload=w/'successors/issue-1201-v1/proposals/fixture.yaml';payload.parent.mkdir();payload.write_text('identifier: kgmicrobe.ingredient:fixture\npreferred_term: Fixture\nmapping_status: MAPPED\n')
   ps=[{'proposal_id':'NEW','case_ids':['c0'],'owner_path':'data/ingredients/mapped/fixture.yaml','before_sha256':None,'after_capture':{'root':'artifact','path':str(payload.relative_to(w)),'sha256':sha(payload)},'evidence_ids':['EOLD'],'supersedes_proposal_ids':[]}]
  fragments={'reassessments':ass,'decisions':ds,'evidence':[],'proposals':ps}
  for k,v in fragments.items():dump(s/'fragments'/f'{group}-{k}.json',{k:v})
  dump(s/'fragments'/f'{group}-assignment.json',{'cases':[{'published_decision':prior[i]} for i in indices]})
  review={'status':'complete','scientific_disposition':'accepted_narrow_scope','reviewed_fragment_hashes':{f'fragments/{group}-{k}.json':sha(s/'fragments'/f'{group}-{k}.json') for k in fragments},'case_reviews':[{'case_id':prior[i]['case_id']} for i in indices],'payload_reviews':[{'proposal_id':p['proposal_id'],'path':p['after_capture']['path'],'sha256':p['after_capture']['sha256'],'full_payload_read':True} for p in ps]}
  rp=s/'independent-review'/f'{group}.json';dump(rp,review);selection[group]={'path':str(rp.relative_to(s)),'sha256':sha(rp)}
 dump(s/'independent-review/review-selection.json',selection)
 return root,w,s
def refresh_review(s,group,mutate=None):
 p=s/'independent-review'/f'{group}.json';x=load(p)
 x['reviewed_fragment_hashes']={f'fragments/{group}-{k}.json':sha(s/'fragments'/f'{group}-{k}.json') for k in ['reassessments','decisions','evidence','proposals']}
 if mutate:mutate(x)
 dump(p,x);selection=load(s/'independent-review/review-selection.json');selection[group]['sha256']=sha(p);dump(s/'independent-review/review-selection.json',selection)

_,_,s=assembly_fixture('assembly-valid');record('assembly-positive-188-cases',False,lambda:module(s/'scripts/assemble_successor.py').build())
_,_,s=assembly_fixture('assembly-missing-payload-review');refresh_review(s,'biological',lambda x:x.update(payload_reviews=[]));record('missing-payload-review-rejected',True,lambda:module(s/'scripts/assemble_successor.py').build(),'payload review coverage')
_,w,s=assembly_fixture('assembly-payload-tamper');p=w/'successors/issue-1201-v1/proposals/fixture.yaml';p.write_text(p.read_text()+'notes: changed\n');record('changed-reviewed-payload-rejected',True,lambda:module(s/'scripts/assemble_successor.py').build(),'reviewed payload changed')
_,_,s=assembly_fixture('assembly-stale-fragment');p=s/'fragments/biological-reassessments.json';x=load(p);x['reassessments'][0]['reasoning']='changed';dump(p,x);record('stale-primary-fragment-hash-rejected',True,lambda:module(s/'scripts/assemble_successor.py').build(),'biological-reassessments')
_,_,s=assembly_fixture('assembly-forged-predecessor');p=s/'fragments/biological-reassessments.json';x=load(p);x['reassessments'][0]['old_decision_sha256']='0'*64;dump(p,x);refresh_review(s,'biological');record('forged-predecessor-digest-rejected',True,lambda:module(s/'scripts/assemble_successor.py').build(),'reassessment predecessor mismatch')
_,_,s=assembly_fixture('assembly-hold-change');p=s/'fragments/biological-decisions.json';x=load(p);x['decisions'][0]['preserved_holds']=[];dump(p,x);refresh_review(s,'biological');record('inherited-hold-removal-rejected',True,lambda:module(s/'scripts/assemble_successor.py').build(),'changed inherited hold')
_,_,s=assembly_fixture('assembly-unresolved-review');refresh_review(s,'biological',lambda x:x.update(scientific_disposition='findings_open'));record('complete-tag-with-unresolved-review-rejected',True,lambda:module(s/'scripts/assemble_successor.py').build(),'unresolved skeptical review findings')
_,_,s=assembly_fixture('assembly-lost-supersession-case');p=s/'fragments/biological-proposals.json';x=load(p);x['proposals'][0]['supersedes_proposal_ids']=['old-p-108'];x['proposals'][0]['owner_path']='data/ingredients/mapped/old108.yaml';dump(p,x);refresh_review(s,'biological');record('lost-superseded-case-backlink-rejected',True,lambda:module(s/'scripts/assemble_successor.py').build(),'lost case backlink')

def gate_fixture(name):
 root,w,s=fresh(name);data=s/'input.json';dump(data,{'value':'original'})
 audit={'structural_accounting':'PASS','scientific_adequacy_or_approval_established':False,'accounted_case_count':188,'assigned_shard_case_count':188,'independent_review_status_counts':{'complete':188}}
 dump(s/'structural-audit-v1.json',audit);dump(s/'validation/proposal-overlay.json',{'status':'PASS'});dump(s/'validation/guarded-writer-replay.json',{'status':'PASS'})
 bp=s/'validation/input-bindings.json';dump(bp,{'files':[{'path':str(data),'sha256':sha(data)}],'gate_outputs':[{'path':str(p),'sha256':sha(p)} for p in [s/'structural-audit-v1.json',s/'validation/proposal-overlay.json',s/'validation/guarded-writer-replay.json']]})
 receipts={}
 for name in ['predecessor','structural','schema','overlay','guarded_writer','auditor_controls']:
  log=s/'validation'/f'{name}.log';log.write_text('SYNTHETIC FIXTURE; not a real external gate execution.\n')
  receipts[name]={'exit_code':0,'input_binding_sha256':sha(bp),'log':str(log.relative_to(s)),'log_sha256':sha(log)}
 receipts['structural'].update(command=['synthetic-auditor','--output',str(s/'structural-audit-v1.json')],result_path='structural-audit-v1.json',result_sha256=sha(s/'structural-audit-v1.json'))
 dump(s/'validation/command-receipts.json',receipts);return root,w,s
def rebind_gate_fixture(s):
 bp=s/'validation/input-bindings.json';x=load(bp)
 for r in x['gate_outputs']:r['sha256']=sha(Path(r['path']))
 dump(bp,x);rp=s/'validation/command-receipts.json';r=load(rp)
 for v in r.values():v['input_binding_sha256']=sha(bp)
 r['structural']['result_sha256']=sha(s/r['structural']['result_path'])
 dump(rp,r)
_,_,s=gate_fixture('native-valid');record('native-positive-gate-contract',False,lambda:module(s/'scripts/build_native_review.py').verify_gates())
_,_,s=gate_fixture('native-nonzero');p=s/'validation/command-receipts.json';x=load(p);x['schema']['exit_code']=1;dump(p,x);record('native-nonzero-command-rejected',True,lambda:module(s/'scripts/build_native_review.py').verify_gates(),'schema')
_,_,s=gate_fixture('native-input-change');dump(s/'input.json',{'value':'changed'});record('native-bound-input-change-rejected',True,lambda:module(s/'scripts/build_native_review.py').verify_gates(),'changed gate input/output')
_,_,s=gate_fixture('native-output-change');dump(s/'validation/proposal-overlay.json',{'status':'PASS','tampered':True});record('native-gate-output-tamper-rejected',True,lambda:module(s/'scripts/build_native_review.py').verify_gates(),'changed gate input/output')
_,_,s=gate_fixture('native-log-change');(s/'validation/schema.log').write_text('altered');record('native-log-tamper-rejected',True,lambda:module(s/'scripts/build_native_review.py').verify_gates(),'changed gate log')
_,_,s=gate_fixture('native-approval-overclaim');p=s/'structural-audit-v1.json';x=load(p);x['scientific_adequacy_or_approval_established']=True;dump(p,x);rebind_gate_fixture(s);record('native-structural-scientific-overclaim-rejected',True,lambda:module(s/'scripts/build_native_review.py').verify_gates())
_,_,s=gate_fixture('native-incomplete-accounting');p=s/'structural-audit-v1.json';x=load(p);x['accounted_case_count']=187;dump(p,x);rebind_gate_fixture(s);record('native-incomplete-188-accounting-rejected',True,lambda:module(s/'scripts/build_native_review.py').verify_gates())
_,_,s=gate_fixture('native-structural-path-mismatch');p=s/'validation/command-receipts.json';x=load(p);other=s/'structural-audit-v2.json';shutil.copyfile(s/'structural-audit-v1.json',other);x['structural']['result_path']='structural-audit-v2.json';dump(p,x);record('native-structural-command-result-path-mismatch-rejected',True,lambda:module(s/'scripts/build_native_review.py').verify_gates(),'structural command/result path mismatch')

def overlay_fixture(name,mode):
 root,w,s=fresh(name);baseline=root/'data/ingredients/mapped/Anchor.yaml';baseline.parent.mkdir(parents=True)
 base={'identifier':'kgmicrobe.ingredient:anchor','preferred_term':'Anchor','mapping_status':'MAPPED','ingredient_type':'SINGLE_INGREDIENT','ontology_mapping':{'ontology_id':'kgmicrobe.ingredient:anchor','ontology_label':'Anchor','ontology_source':'kgmicrobe.ingredient','mapping_quality':'PLACEHOLDER'}}
 baseline.write_text(yaml.safe_dump(base))
 proposals=[]
 for i in range(2):
  ident=f'kgmicrobe.ingredient:fixture{i}';rec={'identifier':ident,'preferred_term':f'Fixture{i}','mapping_status':'MAPPED','ingredient_type':'UNDEFINED_MIXTURE','ontology_mapping':{'ontology_id':ident,'ontology_label':f'Fixture{i}','ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY'}}
  if mode=='new-placeholder' and i==0:rec['ontology_mapping']['mapping_quality']='PLACEHOLDER'
  if mode in ['inherited-placeholder','changed-placeholder'] and i==0:
   rec=copy.deepcopy(base);rec['ingredient_type']='UNDEFINED_MIXTURE'
   if mode=='changed-placeholder':rec['ontology_mapping']['mapping_quality']='EXACT_MATCH'
  path=w/f'payload{i}.yaml';path.write_text(yaml.safe_dump(rec));p={'proposal_id':f'p{i}','kind':'new_owner','owner_path':f'data/ingredients/mapped/New{i}.yaml','before_sha256':None,'after_capture':{'path':str(path.relative_to(w)),'sha256':sha(path)}}
  if mode=='duplicate':p['destination_owner_path']='data/ingredients/mapped/Same.yaml'
  if mode=='existing' and i==0:p['integration_target_path']='data/ingredients/mapped/Anchor.yaml'
  if mode=='escape' and i==0:p['destination_owner_path']='data/ingredients/mapped/../../escape.yaml'
  if mode in ['inherited-placeholder','changed-placeholder'] and i==0:p.update(kind='edit_existing_owner',owner_path='data/ingredients/mapped/Anchor.yaml',before_sha256=sha(baseline))
  proposals.append(p)
 dump(s/'proposals.json',{'proposals':proposals})
 return root,w,s
def run_overlay(root,s):
 def git_stub(command,**kwargs):
  if command[:2]==['git','show']:return (root/command[2].split(':',1)[1]).read_bytes()
  assert command[:2] in [['git','diff'],['git','ls-files']],command
  return b''
 with patch('subprocess.check_output',side_effect=git_stub):runpy.run_path(str(s/'scripts/validate_overlay.py'),run_name='__main__')
for mode in ['valid','duplicate','existing','escape','new-placeholder','inherited-placeholder','changed-placeholder']:
 root,w,s=overlay_fixture('overlay-'+mode,mode);record('overlay-'+mode+'-control',mode not in ['valid','inherited-placeholder'],lambda:run_overlay(root,s))
 result=load(s/'validation/proposal-overlay.json')
 if mode=='duplicate':assert any('duplicate integration destination' in x for x in result['errors'])
 if mode=='existing':assert any('integration destination already exists' in x for x in result['errors'])
 if mode=='escape':assert any('unsafe integration destination' in x for x in result['errors'])
 if mode in ['new-placeholder','changed-placeholder']:assert any('new registry mapping quality' in x for x in result['errors'])
 if mode=='inherited-placeholder':assert result['ontology_labels'][0]['inherited_mapping_quality_preserved_not_approved'] is True
changed=[{'path':str(p),'before_sha256':h,'after_sha256':sha(p)} for p,h in real_inputs.items() if sha(p)!=h]
if changed:
 dump(S/'independent-review/process-negative-controls-interrupted.json',{'status':'INTERRUPTED_FAIL_CLOSED','controls':results,'changed_real_inputs':changed,'reviewer_mutated_real_inputs':False})
assert not changed,'Real primary input changed during process controls'
assert {str(p.relative_to(S)):sha(p) for p in (S/'scripts').glob('*.py')}==source_hashes,'Production helper changed during controls'
report={'reviewer':'Codex /root/biological','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','scope':'Independent synthetic process guards only; this does not claim actual final worker gates ran.','production_script_hashes':source_hashes,'private_fixture_root':str(PRIVATE),'real_inputs_unchanged':True,'overlay_mock_scope':'Only Git diff and untracked-file baseline reads return empty in tiny synthetic fixture; actual destination, identity, partonomy and registry logic execute unchanged copied script bytes. No external ontology fetch occurs.','controls':results,'limitations':['Source science is reviewed separately. Positive synthetic receipts are fixtures, not substitute final validation evidence.','Overlay semantics retain original owner dictionary keys while separately validating future integration destination uniqueness/safety; no filesystem move is exercised.']}
out=S/'independent-review/process-negative-controls-results.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'controls':len(results),'status':'PASS','result_sha256':sha(out)}))
