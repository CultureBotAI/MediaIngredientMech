from pathlib import Path
import json,hashlib,subprocess,datetime,copy
W=Path.cwd();C=W.parents[2];O=W/'.temp/ebios-no-install-v1/lineage';R=W/'reports/all_unmatched_20261107/worker-02/successors/ebios-no-install-v1';A=C/'workers/w08/worktree/.temp/ebios-candidate-independent-v1';H='0c659aa4c121a5b1832bff699c28e30da577ca08';sha=lambda b:hashlib.sha256(b).hexdigest();canon=lambda x:sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode());load=lambda p:json.loads(Path(p).read_text());checks=[]
def check(n,x):
 checks.append({'check':n,'passed':bool(x)})
 if not x:raise AssertionError(n)
def dump(n,x):
 p=O/n
 if p.exists():raise RuntimeError('already exists')
 p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
binding=load(O/'original-ebios-binding-v1.json');cohort=load(O/'cohort-continuity-v1.json');author=load(O.parent/'author-write-receipt.json');st=load(R/'source-origin-retirement.json');sel=load(R/'selector.json');rec=load(R/'source-case-reconciliation.json');files=[]
for p in sorted(R.rglob('*')):
 if p.is_file():check('regular_'+str(p.relative_to(R)),not p.is_symlink());files.append({'path':str(p),'sha256':sha(p.read_bytes()),'size':p.stat().st_size})
check('exact_twelve_files',len(files)==12);check('exact_author_inventory',{r['path']:r['sha256'] for r in files}=={str(W/r['path']):r['sha256'] for r in author['outputs']})
check('original_proposal_complete',load(R/'original/proposal.json')==binding['proposal']);check('original_decision_complete',load(R/'original/case-decision.json')==binding['decision']);check('original_payload_complete',sha((R/'original/payload.yaml').read_bytes())==binding['proposal']['after_capture']['sha256'])
selected=load(W/'reports/all_unmatched_20261107/worker-02/seven-preparation-types-v1/selected-v3/evidence.json')['evidence'];expected_e=[x for x in selected if x['evidence_id'] in binding['decision']['evidence_ids']];actual_e=load(R/'original/evidence.json')['evidence'];check('all_eight_complete_original_evidence',actual_e==expected_e and len(actual_e)==8);check('all_evidence_canonical_hashes',rec['unchanged_original_evidence_object_sha256']=={e['evidence_id']:canon(e) for e in actual_e})
for e in actual_e:
 cap=e['capture'];base=(W/'reports/all_unmatched_20261107/worker-02') if cap['root']=='artifact' else C/'queue/preliminary-v5';check('case_evidence_capture_'+e['evidence_id'],sha((base/cap['path']).read_bytes())==cap['sha256'])
check('retirement_exact_contract_fields',set(st)=={'schema_version','kind','origin_id','origin_proposal_sha256','successors','reason'});check('schema_version_actual_integer',type(st['schema_version']) is int and st['schema_version']==1);check('retirement_identity',st['kind']=='source_origin_retirement' and st['origin_id']=='w02::'+binding['proposal']['proposal_id'] and st['origin_proposal_sha256']==canon(binding['proposal']));check('no_successor',st['successors']=={} and type(st['successors']) is dict);check('selector_retirement_hash',sel['retirements'][0]['sha256']==sha((R/'source-origin-retirement.json').read_bytes()));check('selector_reconciliation_hash',sel['source_case_reconciliation']['sha256']==sha((R/'source-case-reconciliation.json').read_bytes()));check('rec_current_original_identity',rec['original_kind']=='new_owner' and rec['original_before_sha256'] is None and rec['unchanged_original_decision_object_sha256']==canon(binding['decision']));check('rec_exact_case_occurrence',rec['original_case_id']==binding['decision']['case_id'] and rec['case_input_sha256']==binding['decision']['case_input_sha256'] and rec['original_occurrence_ids']==binding['decision']['occurrence_ids']);check('metadata_counts',sel['original_counts_retained']=={'cases':188,'CM_occurrence_ids':322,'proposals':117,'evidence_objects':1830})
for name,b in sel['original_full_core_selection'].items():
 raw=(W/b['path']).read_bytes();old=subprocess.check_output(['git','show',H+':'+b['path']]);check('selected_original_core_'+name,raw==old and sha(raw)==b['sha256'])
for p in cohort['proposals']:
 check('final_all_payloads_'+p['proposal_id'],sha((W/p['payload_path']).read_bytes())==p['payload_sha256'])
check('base_exact',sel['publication_base_head']==H);check('no_publication_claim',sel['final_published_head_review']=='Separate coordinator responsibility; this author selector is not that review.');check('source_holds_exact_family',sel['source_family_lot_role_export_holds']==load(A/'HANDOFF.json')['limitations'] if 'limitations' in load(A/'HANDOFF.json') else sel['source_family_lot_role_export_holds']==load(A/'HANDOFF.json')['held_limits'])
# Exact original-context Git bindings, not W01/W06 acceptance or writes.
gitproof=[]
for b in load(A/'lineage-verification.json')['git_bindings']:
 slot=b['captured_path'].split('/')[1];repo=C/f'workers/{slot}/worktree';raw=subprocess.check_output(['git','-C',str(repo),'show',b['head']+':'+b['path']]);check('original_context_git_'+b['path'],sha(raw)==b['sha256']);gitproof.append({**b,'independently_rehashed':True})
# Supplemental wrong-lineage controls operate only on in-memory objects.
def boundary(s,r):
 assert type(s['schema_version']) is int and s['schema_version']==1
 assert s['origin_proposal_sha256']==binding['proposal_sha256']
 assert s['successors']=={}
 assert r['original_kind']=='new_owner' and r['original_before_sha256'] is None
 assert r['original_occurrence_ids']==binding['decision']['occurrence_ids']
 assert r['case_input_sha256']==binding['decision']['case_input_sha256']
controls=[]
for name,change in [('invented_successor',lambda s,r:s.update(successors={'w02::fake':'0'*64})),('fabricated_beforeimage',lambda s,r:r.update(original_before_sha256='1'*64)),('retyped_original_edit',lambda s,r:r.update(original_kind='edit_existing_owner')),('dropped_occurrence',lambda s,r:r.update(original_occurrence_ids=[])),('wrong_proposal_hash',lambda s,r:s.update(origin_proposal_sha256='2'*64)),('boolean_schema_version',lambda s,r:s.update(schema_version=True))]:
 s=copy.deepcopy(st);r=copy.deepcopy(rec);change(s,r)
 try:boundary(s,r)
 except AssertionError:controls.append({'control':name,'refused':True,'layer':'supplemental lineage assertions; not native validator'})
 else:raise AssertionError('accepted '+name)
boundary(st,rec)
dump('metadata-verification-v1.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'checks':checks,'counts':{'checks':len(checks),'passed':sum(x['passed'] for x in checks),'context_git_bindings':len(gitproof)},'git_bindings':gitproof,'negative_controls':controls,'publication_proof_executed':False,'native_prepare_executed':False,'source_or_candidate_changed':False})
print(json.dumps({'checks':len(checks),'passed':sum(x['passed'] for x in checks),'controls':len(controls)}))
