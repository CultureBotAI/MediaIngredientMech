"""Independent technical proof of one GYPS origin; never native apply.
The local fixture Git commits are explicit test publication identities, not the
real worker remote head. Real final-head intake must be independently rebound.
"""
import argparse,copy,datetime,hashlib,importlib.util,json,pathlib,subprocess,sys
R=pathlib.Path.cwd();C=R.parents[2];T=R/'.temp/gyps-native-origin-v1/technical-review';I=C/'integration/worktree'
sys.path.insert(0,str(I/'src'))
from mediaingredientmech.curate import campaign_owner_apply as native
from mediaingredientmech.validation import mapping_change_receipts as chain
spec=importlib.util.spec_from_file_location('reviewed_crosswalk_v3',C/'integration/final-application-accounting-v3/crosswalk.py');crosswalk=importlib.util.module_from_spec(spec);spec.loader.exec_module(crosswalk)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def put(root,name,value):
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(value if isinstance(value,bytes) else json.dumps(value,indent=2).encode()+b'\n');return p

def ref(root,name):return {'path':name,'sha256':sha((root/name).read_bytes())}
def git(root,*args):return native.git(root,*args).decode().strip()
def run(ledger_path):
 fixture=T/'fixture-v2';assert not fixture.exists();fixture.mkdir(parents=True);(fixture/'data/ingredients/unmapped').mkdir(parents=True)
 raw=ledger_path.read_bytes();ledger=json.loads(raw);assert len(ledger['proposals'])==1;proposal=ledger['proposals'][0]
 assert proposal['kind']=='edit_existing_owner' and proposal['owner_path']=='data/ingredients/mapped/GYPS.yaml'
 assert proposal['before_sha256']=='36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e'
 assert proposal['after_capture']['sha256']=='fa98f361a39dcaf0bea1f4046829287581bc45e2813044696e5070de58708aa1'
 caseid='KG_CASE:ba039f9e4a33baf69eb111ceb979cf6c9ad8fe788c13488f256336508ce94151';assert proposal['case_ids']==[caseid]
 payload=R/'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1/payloads-v2/GYPS.yaml';assert sha(payload.read_bytes())==proposal['after_capture']['sha256']
 before=R/proposal['owner_path'];assert sha(before.read_bytes())==proposal['before_sha256']
 for path in native.PRODUCERS:put(fixture,path,(I/path).read_bytes())
 put(fixture,proposal['owner_path'],before.read_bytes())
 # Fixture-only canonical row: no maintained native mapping receipt/chain is impersonated.
 sssom=b'# mapping_set_id: https://example.invalid/gyps-native-fixture\n# predicate_semantics: skos\nsubject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tother\nMIM:GYPS\tGYPS\tskos:exactMatch\tkgmicrobe.ingredient:gyps\tGYPS\t\n'
 put(fixture,'mappings/ingredient_mappings.sssom.tsv',sssom)
 put(fixture,'intake/proposals.json',raw)
 payload_path='intake/'+proposal['after_capture']['path'];put(fixture,payload_path,payload.read_bytes())
 put(fixture,'intake/global-cases.json',(C/'queue/preliminary-v5/union-ledger.json').read_bytes())
 cases=json.loads((fixture/'intake/global-cases.json').read_bytes());assert len(cases)==1879;case=next(c for c in cases if c['case_id']==caseid);casehash=sha(canon(case));assert casehash=='d42806e437d2e4c72f3e148314c5ef72e8c21f08c78b7b70eebe3d32c83b67d6'
 put(fixture,'intake/shard-03.json',(C/'queue/preliminary-v5/shards/shard-03.json').read_bytes())
 put(fixture,'intake/shard-05.json',(C/'queue/preliminary-v5/shards/shard-05.json').read_bytes())
 put(fixture,'intake/decision.json',{'scope':'fixture evidence of unchanged original188W03decisions; causal W05case not an assigned W03decision','source':str(R/'reports/all_unmatched_20261107/worker-03/successors/issue1226-v1/decisions.json'),'sha256':sha((R/'reports/all_unmatched_20261107/worker-03/successors/issue1226-v1/decisions.json').read_bytes())})
 put(fixture,'intake/route.json',(R/'.temp/gyps-native-origin-v1/inputs/issue1176-route-comment.json').read_bytes())
 put(fixture,'intake/independent-review.json',(C/'preflight/w03-peptone-final-head-independent-v1/HANDOFF.json').read_bytes())
 put(fixture,'intake/fixture-scope.json',{'fixture_only':True,'apply_called':False,'source_owner_count':1,'full_global_case_ledger_count':1879,'approval':'NONE: structural one-owner fixture, not scientific/application authorization','real_new_published_head':'NOT_YET_ASSIGNED_IN_THIS_FIXTURE','note':'FixtureGithead binds exact prospective native ledger bytes; does not claim remote publication or realfullcampaignprepared.'})
 beforemap=native.hashes(native.inventory(fixture));put(fixture,'before.json',{'schema_version':1,'owners':beforemap});aftermap=dict(beforemap);aftermap[proposal['owner_path']]=proposal['after_capture']['sha256'];put(fixture,'after.json',{'schema_version':1,'owners':aftermap})
 put(fixture,'protected.json',{'schema_version':1,'files':chain.verify_mapping_chain(fixture)['input_hashes']})
 git(fixture,'init','-q');git(fixture,'add','.');git(fixture,'-c','user.name=Native fixture','-c','user.email=fixture@example.invalid','commit','-qm','Private GYPS native-intake fixture; no actual publication')
 head=git(fixture,'rev-parse','HEAD');bindings=[]
 def bind(name,role,path,published=False):
  b=dict(binding_id=name,role=role,**ref(fixture,path),published_head=head if published else None,published_path=path if published else None);bindings.append(b)
 bind('full-cases','case_ledger','intake/global-cases.json');bind('W03-shard','shard','intake/shard-03.json');bind('W05-causal-shard','shard','intake/shard-05.json');bind('original-decisions-context','decision','intake/decision.json');bind('new-proposal','proposal','intake/proposals.json',True);bind('original-payload','evidence',payload_path,True);bind('independent-review','review','intake/independent-review.json');bind('filed-route','reconciliation','intake/route.json');bind('fixture-scope','reconciliation','intake/fixture-scope.json')
 for index,path in enumerate(native.PRODUCERS):bind('native-producer-'+str(index),'producer',path)
 origin={'worker_slot':'worker-03','head_sha':head,'proposal_id':proposal['proposal_id'],'proposal_binding':'new-proposal','payload_binding':'original-payload','case_hashes':{caseid:casehash}}
 operation={'operation_id':'FIXTURE-GYPS-NATIVE','kind':'edit','before_source_record':proposal['owner_path'],'source_record':proposal['owner_path'],'before_yaml_sha256':proposal['before_sha256'],'after_capture':ref(fixture,payload_path),'origins':[origin],'change':'Exact previously reviewed GYPS dependency payload only; no change of scientific bytes.','verification':'Fixture-only structural evidence. Case is real global W05 causal parent context, not GYPS observation or W03 assigned case. Conditional Bacto requirement remains.'}
 plan={'schema_version':1,'operation':'apply_reviewed_campaign_owners','repository':'CultureBotAI/MediaIngredientMech','baseline_commit':head,'intake_heads':{'worker-03':head},'before_inventory':ref(fixture,'before.json'),'after_inventory':ref(fixture,'after.json'),'protected_inputs':ref(fixture,'protected.json'),'bindings':bindings,'records':[operation]}
 def save(name,p):
  pp=put(fixture,name+'/plan.json',p);a={'schema_version':1,'scope':'source_application_only','plan_sha256':sha(pp.read_bytes()),'baseline_commit':p['baseline_commit'],'intake_heads':p['intake_heads'],'binding_sha256':{b['binding_id']:b['sha256'] for b in p['bindings']},'accepted_operations':{x['operation_id']:x['after_capture']['sha256'] for x in p['records']},'review_bindings':['independent-review']};ap=put(fixture,name+'/acceptance.json',a);return pp,ap
 pp,ap=save('positive',plan);prepared=native.prepare(fixture,pp,ap)
 oid='w03::'+proposal['proposal_id'];crow={'origin_id':oid,'worker_slot':3,'published_head':head,'proposal':proposal,'proposal_object_sha256':sha(canon(proposal)),'payload_sha256':proposal['after_capture']['sha256'],'case_hashes':{caseid:casehash}}
 crossbinding={'origin_id':oid,'proposal_ledger':{**ref(fixture,'intake/proposals.json'),'published_path':'intake/proposals.json'},'payload':{**ref(fixture,payload_path),'published_path':payload_path}}
 reviewref=ref(fixture,'intake/independent-review.json');resolution={'origin_id':oid,'status':'apply','evidence_refs':[ref(fixture,'intake/route.json')],'operation_id':'FIXTURE-GYPS-NATIVE','payload_sha256':proposal['after_capture']['sha256'],'independent_review_refs':[reviewref]}
 crossargs=dict(root=fixture,origin_bindings=[crossbinding],native_plan={'plan':ref(fixture,str(pp.relative_to(fixture))),'acceptance':ref(fixture,str(ap.relative_to(fixture)))})
 proof=crosswalk.validate_resolution_crosswalk([crow],[resolution],**crossargs)
 results=[]
 for name,mut in [('wrong-causal-hash',lambda p:p['records'][0]['origins'][0]['case_hashes'].update({caseid:'0'*64})),('wrong-preimage',lambda p:p['records'][0].update(before_yaml_sha256='0'*64)),('wrong-original-payload-hash',lambda p:next(b for b in p['bindings'] if b['binding_id']=='original-payload').update(sha256='0'*64)),('missing-causal-case',lambda p:p['records'][0]['origins'][0].update(case_hashes={}))]:
  bad=copy.deepcopy(plan);mut(bad);p,a=save('negative/'+name,bad)
  try:native.prepare(fixture,p,a)
  except ValueError as e:results.append({'control':name,'result':'REFUSED','message':str(e)})
  else:raise AssertionError('negative accepted:'+name)
 mutated=copy.deepcopy(crow);mutated['proposal']['technical_counterfactual_claim']='foreign W05 case claimed as assigned W03';mutated['proposal_object_sha256']=sha(canon(mutated['proposal']))
 try:crosswalk.validate_resolution_crosswalk([mutated],[resolution],**crossargs)
 except ValueError as e:results.append({'control':'crosswalk-full-original-object-mismatch','result':'REFUSED','message':str(e)})
 else:raise AssertionError('crosswalk accepted differentcompleteproposal')
 # Do not call apply: both actual data and fixture owner stay exact beforeimages.
 assert sha((fixture/proposal['owner_path']).read_bytes())==proposal['before_sha256'];assert git(fixture,'rev-parse','HEAD')==head;assert not git(fixture,'diff','--name-only','HEAD','--')
 summary={'reviewer':'/root/gyps_native_technical','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_BOUNDED_ONE_OWNER_NATIVE_PREPARE_AND_EXACT_ORIGINAL_CROSSWALK','actual_ledger_path':str(ledger_path),'actual_ledger_sha256':sha(raw),'proposal_id':proposal['proposal_id'],'proposal_object_sha256':sha(canon(proposal)),'original_payload_sha256':proposal['after_capture']['sha256'],'before_sha256':proposal['before_sha256'],'fixture_root':str(fixture.relative_to(R)),'fixture_git_head':head,'fixture_head_is_real_worker_publication':False,'native_prepare_called':True,'native_apply_called':False,'full_campaign_prepared':False,'fixture_owner_count':len(beforemap),'global_ledger_count':len(cases),'native_input_count':len(prepared.inputs),'native_producer_count':len(native.PRODUCERS),'owner_before_after_unchanged':True,'crosswalk_result':proof,'negative_controls':results,'source_operator_sha256':sha((I/'src/mediaingredientmech/curate/campaign_owner_apply.py').read_bytes()),'crosswalk_sha256':sha((C/'integration/final-application-accounting-v3/crosswalk.py').read_bytes()),'limitations':['This proves exact prospective ledger bytes in a privateGitfixture, notnewrealpublishedhead nor fullcampaign acceptance.','FixtureSSSOM is explicitly synthetic and no realnativechain equivalence is claimed.','Falseassignedforeigncase semantic control is separate: nativeoperator hashes globalcase but doesnotvalidate assignedshardmeaning.','Only exact published successor and coordinator actualintakecrosswalk can satisfy realintegration; no operator/gatechanges.']}
 put(T,'native-prepare-crosswalk-v2.json',summary);print(json.dumps({k:summary[k] for k in ['status','actual_ledger_sha256','fixture_git_head','fixture_owner_count','global_ledger_count','native_input_count','native_producer_count','negative_controls']},indent=2))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--ledger',type=pathlib.Path,required=True);ns=a.parse_args();run(ns.ledger.absolute())
