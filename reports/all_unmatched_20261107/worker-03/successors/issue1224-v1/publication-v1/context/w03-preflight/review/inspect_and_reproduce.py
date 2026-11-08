from pathlib import Path
import json,hashlib,datetime,subprocess,sys,importlib.util,collections
R=Path.cwd();W=R/'reports/all_unmatched_20261107/worker-03';S=W/'successors/issue1224-v1';D=S/'draft-v2';O=R/'.temp/w03-oxoid-successor-v1/review';C=R.parents[2];Q=C/'queue/preliminary-v5'
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,x):
 with (O/n).open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def obj(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
started=datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')
paths=[W/n for n in ['decisions.json','proposals.json','evidence.json','manifest.sha256']]+list(D.glob('*.json'))+[S/'retirement.json',S/'candidate/reinforced_clostridial_medium_oxoid_cm0149.yaml',W/'broths/captures/bbd7246c15ffb57a.html',W/'broths/captures/e931e6ce922a0ffc-targeted.pdf']+list((S/'context').rglob('*'))+list((S/'retired').rglob('*'))
paths=[p for p in paths if p.is_file()]
inputs=sorted(set(str(p.relative_to(R)) for p in paths)|{'MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','scripts/record_review.py','schema/record_review.yaml','docs/record-reviews.md','docs/record-review-profile.md','AGENTS.md','conf/record_review.yaml','src/mediaingredientmech/validation/component_partonomy.py','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/synonym_policy.py'})
spec=importlib.util.spec_from_file_location('rr',R/'scripts/record_review.py');m=importlib.util.module_from_spec(spec);sys.modules['rr']=m;spec.loader.exec_module(m)
tid='kgmicrobe.ingredient:reinforced_clostridial_medium_oxoid_cm0149'
targets=[{'target_id':tid,'path':str((S/'candidate/reinforced_clostridial_medium_oxoid_cm0149.yaml').relative_to(R)),'label':'Reinforced clostridial medium (Oxoid CM0149)','record_class':'IngredientRecord','kind':'record','ownership_note':'Unapplied new-owner candidate; prospective maintained owner data/ingredients/mapped/reinforced_clostridial_medium_oxoid_cm0149.yaml. Root authors successor source binding; /root/next23_context authors exact candidate. User restricts review persistence to private review directory.'}]
dump('native-inspection.json',m.inspect_source(R,targets,inputs))
dump('started.json',{'started_at':started,'reviewer':'/root/oxoid_successor_review','independence':'Separate in-process subagent; did not author payload, source binding, original W03 proposal or preservation helper.'})
old={n:json.loads((W/f'{n}.json').read_text())[n] for n in ['decisions','proposals','evidence']};new={n:json.loads((D/f'{n}.json').read_text())[n] for n in old}
cid='CM_NAME:2be5d4f231ea346e62be345a8e8b35adbc735ccdced2de73963ce5265c48fd66';pid='w03-oxoid-cm0149-product-1224-v1';oldpid='b-proposal-cm0149-form'
ledger={};errors=[]
for n,key in [('decisions','case_id'),('proposals','proposal_id'),('evidence','evidence_id')]:
 a={x[key]:x for x in old[n]};b={x[key]:x for x in new[n]};changed=[k for k in a.keys()&b.keys() if a[k]!=b[k]];removed=list(a.keys()-b.keys());added=list(b.keys()-a.keys());ledger[n]={'original_count':len(old[n]),'successor_count':len(new[n]),'unique_count':len(b),'unchanged_count':sum(a[k]==b[k] for k in a.keys()&b.keys()),'changed_ids':sorted(changed),'removed_ids':sorted(removed),'added_ids':sorted(added),'all_original_object_hashes':{k:obj(v) for k,v in a.items()},'all_successor_object_hashes':{k:obj(v) for k,v in b.items()}}
 assert len(b)==len(new[n])
assert ledger['decisions']['changed_ids']==[cid] and ledger['decisions']['unchanged_count']==187 and not ledger['decisions']['removed_ids'] and not ledger['decisions']['added_ids']
assert ledger['proposals']['removed_ids']==[oldpid] and ledger['proposals']['added_ids']==[pid] and ledger['proposals']['unchanged_count']==73 and not ledger['proposals']['changed_ids']
assert ledger['evidence']['unchanged_count']==852 and not ledger['evidence']['removed_ids'] and not ledger['evidence']['changed_ids']
a=next(x for x in old['decisions'] if x['case_id']==cid);b=next(x for x in new['decisions'] if x['case_id']==cid);p=next(x for x in new['proposals'] if x['proposal_id']==pid);ret=json.loads((S/'retirement.json').read_text())
protected=['case_id','case_input_sha256','source','occurrence_ids','owner_records','frozen_index','preserved_original_kg_entry_downstream_holds','native_owner_review_rows','hold_scope_note']
assert all(a[k]==b[k] for k in protected)
assert ret['retired_decision']==a and ret['retired_proposal']==next(x for x in old['proposals'] if x['proposal_id']==oldpid)
assert b['proposal_ids']==[pid] and p['case_ids']==[cid] and p['kind']=='new_owner' and p['before_sha256'] is None
assert all(oldpid not in x['proposal_ids'] for x in new['decisions'])
assert sum(pid in x['proposal_ids'] for x in new['decisions'])==1
assert p['after_capture']['sha256']=='1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae'
ledger['changed_case']={'protected_fields':protected,'changed_fields':[k for k in a.keys()|b.keys() if a.get(k)!=b.get(k)],'new_proposal':p,'before_case_object_sha256':obj(a),'after_case_object_sha256':obj(b),'retired_case_exact':True,'retired_proposal_exact':True,'one_active_binding':True}
# Independent full frozen case digest and exact capture-byte checks.
shard=json.loads((Q/'shards/shard-03.json').read_text());cs={x['case_id']:x for x in shard['cases']};assert len(cs)==188
for row in new['decisions']:
 raw=cs[row['case_id']];actual=hashlib.sha256(json.dumps(raw,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest();assert actual==row['case_input_sha256'],(row['case_id'],actual)
 assert row['source']=={k:raw[k] for k in ['source','source_case_id','source_label','raw_source_label']}
 assert row['occurrence_ids']==[x['occurrence_id'] for x in raw.get('occurrences',[])]
assert ret['frozen_complete_case']==cs[cid]
bindings=[]
for item in new['evidence']+new['proposals']:
 cap=item.get('capture',item.get('after_capture'));root={'source':Q,'artifact':W}[cap['root']];f=root/cap['path'];assert f.resolve().is_relative_to(root.resolve()) and not f.is_symlink();actual=sh(f);assert actual==cap['sha256'];bindings.append({'id':item.get('evidence_id',item.get('proposal_id')),'path':str(f),'sha256':actual})
for row in new['decisions']:
 for x in row['owner_records']:assert sh(R/x['path'])==x['sha256']
manifest=[]
for line in (W/'manifest.sha256').read_text().splitlines():
 h,n=line.split(None,1);n=n.lstrip('*');assert sh(R/n)==h;manifest.append({'path':n,'sha256':h})
ledger['full_capture_count']=len(bindings);ledger['distinct_capture_count']=len({x['path'] for x in bindings});ledger['original_manifest_members']=len(manifest);ledger['all_188_frozen_case_digests_and_sources_match']=True;ledger['all_owner_context_hashes_match']=True;ledger['status']='PASS_ACCOUNTING_ONLY';ledger['scientific_approval_other187']=False;ledger['publication_condition']='W01 final exact nine-v4 review must be communicated by coordinator before publication; this review does not substitute.'
dump('independent-accounting.json',ledger);dump('exact-capture-bindings.json',bindings);dump('original-manifest-rehash.json',manifest)
print(json.dumps({k:v for k,v in ledger.items() if k not in ['decisions','proposals','evidence','changed_case']},indent=2))
