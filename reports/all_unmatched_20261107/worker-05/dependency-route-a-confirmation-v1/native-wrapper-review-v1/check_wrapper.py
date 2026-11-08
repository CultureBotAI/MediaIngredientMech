import datetime,hashlib,importlib.util,json,pathlib,yaml
S=pathlib.Path('.temp/w05-dependency-route-a-confirmation-v1')
R=S/'native-wrapper-review-v1'
B=pathlib.Path('reports/all_unmatched_20261107/worker-05')
Q=B/'dependency-route-a-confirmation-v1'
N=pathlib.Path('reviews/structured/20261108T101857Z-worker05-dependent-origin-confirmation')
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def oh(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
science=j(S/'review/main-review.json');sm=j(S/'review/FINAL-MANIFEST-v1.json')
for row in sm['members']:
 p=S/'review'/row['path'];public=Q/'review'/row['path']
 assert sha(p)==sha(public)==row['sha256'] and p.stat().st_size==public.stat().st_size==row['bytes']
assert sha(S/'review/FINAL-MANIFEST-v1.json')==sha(Q/'review/FINAL-MANIFEST-v1.json')
x=j(Q/'native-review-preparation/review-content.json');saved=yaml.safe_load((N/'review.yaml').read_text());assert x==saved
assert x['source']['git_revision']=='108e213e96f7d423ee345ce265d692e79063127c'
assert x['reviewer']['independence']=='self_review' and '/root/final_skeptical' in x['reviewer']['identity']
assert x['verdict']=='needs_curation' and x['scientific_review'] is True and x['scope']['population_size']==15
rows={r['proposal_id']:r for r in science['payload_reviews']};targets={t['target_id']:t for t in x['targets']}
assert set(rows)==set(targets)==set(x['scope']['reviewed_target_ids'])
inputs={b['path']:b for b in x['source']['inputs']}
for b in inputs.values():assert sha(pathlib.Path(b['path']))==b['sha256']
evidence={e['evidence_id']:e for e in x['evidence']}
for e in evidence.values():assert sha(pathlib.Path(e['reference']))==e['snapshot_sha256']
assert evidence['PEER']['snapshot_sha256']==sha(S/'review/main-review.json')
assessments=[]
for a in x['assessments']:
 assert len(a['target_ids'])==1
 pid=a['target_ids'][0];r=rows[pid];t=targets[pid];details=json.loads(a['details'])
 assert a['summary']==r['assessment']
 assert details['remaining_source_prerequisite']==r['missing_fact_or_application_condition']
 assert details['after_capture']==r['after_capture'] and details['authentic_before']==r['before_sha256']
 assert details['causal_not_observed_recipe'] is True
 p=B/r['after_capture']['path'];assert str(p)==t['path'] and sha(p)==r['after_capture']['sha256']
 assert inputs[str(p)]['role']=='target' and inputs[str(p)]['sha256']==r['after_capture']['sha256']
 assert t['owner_paths'][0]['path']==r['owner_path']
 y=yaml.safe_load(p.read_text());assert t['label']==y['preferred_term']
 assessments.append({'proposal_id':pid,'after_capture':r['after_capture'],'native_assessment_object_sha256':oh(a),'exact_scientific_assessment_reused':True,'exact_current_missing_fact_or_application_condition_reused':True,'actual_scientific_reviewer':'/root/final_skeptical','assessment':'Native wrapper accurately reuses the independently reviewed bounded assessment and its current prerequisite, without converting unresolved source facts or application conditions into owner approval.'})
assert len(assessments)==15 and not x['findings'] and not x['actions']
spec=importlib.util.spec_from_file_location('record_review_readonly',pathlib.Path('scripts/record_review.py'));mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
assert mod.render_markdown(x)==(N/'review.md').read_text()
reference=j(S/'review/reference-wrapper-review-v1.json')
for b in reference['reports']:assert sha(pathlib.Path(b['path']))==b['sha256']
selector=j(Q/'selector.json')
for b in selector['canonical_core']:assert sha(pathlib.Path(b['path']))==b['sha256']
receipt={'reviewer':'/root/final_skeptical','completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','source_science':bind(S/'review/main-review.json'),'source_science_manifest':bind(S/'review/FINAL-MANIFEST-v1.json'),'public_science':bind(Q/'review/main-review.json'),'public_copy_members_exact':len(sm['members']),'source_inputs_hashed':len(inputs),'evidence_snapshots_hashed':len(evidence),'native_content':bind(Q/'native-review-preparation/review-content.json'),'native_pair':[bind(N/n) for n in ['review.yaml','review.md']],'native_renderer':bind(pathlib.Path('scripts/record_review.py')),'native_yaml_equals_content':True,'native_markdown_equals_canonical_renderer':True,'target_reviews':assessments,'reports':[bind(Q/n) for n in ['selector.json','README.md','source-scope-ledger.json']],'source_core':selector['canonical_core'],'new_findings':[],'scope_note':'Exact final reference/native wrapper review only. No new source payload, chemical conclusion, old-review mutation or maintained application. Retained native corpus check is bound separately at final sealing.'}
out=R/'exact-wrapper-checks-v1.json';assert not out.exists();out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(bind(out)))
