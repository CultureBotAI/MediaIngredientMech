"""Independent bounded native conversion and staged delivery audit; no data edits."""
import collections,datetime,hashlib,importlib.util,json,pathlib,subprocess
R=pathlib.Path('reports/all_unmatched_20261107/worker-02'); B=R/'b'; N=pathlib.Path('reviews/structured/20261108T054002Z-w02-all-unmatched-source-review')
sha=lambda b:hashlib.sha256(b).hexdigest()
def load(p):return json.loads((R/p).read_text())
def canon(x):return sha(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
def git(*args):return subprocess.check_output(['git',*args])
def utc(v):return datetime.datetime.fromisoformat(v.replace('Z','+00:00')).astimezone(datetime.timezone.utc)
def fileinfo(p):return {'path':str(p),'sha256':sha(p.read_bytes())}
spec=importlib.util.spec_from_file_location('native_review', 'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
n=mod.yaml.load((N/'review.yaml').read_text(),Loader=mod._ReviewLoader)
assert mod.render_markdown(n)==(N/'review.md').read_text(), 'native markdown is not exact renderer output'
D=load('decisions.json')['decisions']; E=load('evidence.json')['evidence']; P=load('proposals.json')['proposals']; C=load('integration/independent-review-coverage.json')['cases'];old=load('b/review-final-integration.json'); dm={d['case_id']:d for d in D}; cm={c['case_id']:c for c in C};ne={e['evidence_id']:e for e in n['evidence']}
assert len(D)==len(dm)==len(C)==len(cm)==len(n['targets'])==len(n['assessments'])==188
assert n['scope']['population_size']==188 and n['scope']['coverage']=='full' and n['scope']['reviewed_target_ids']==[d['case_id'] for d in D]
assert n['reviewer']['independence']=='self_review' and n['verdict']=='needs_curation' and n['completion']=='completed'
assert n['source']['git_revision']=='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
input_paths={i['path'] for i in n['source']['inputs']}; assert len(input_paths)==len(n['source']['inputs'])==1094
for i in n['source']['inputs']:assert sha(pathlib.Path(i['path']).read_bytes())==i['sha256'],i['path']
kindmap={'primary_source':'primary_source','source_snapshot':'record_content','ontology':'authority','native_record_review':'prior_review','independent_review':'prior_review','unsuccessful_search':'search','local_validation':'validation'}
assert len(ne)==len(n['evidence'])==1434 and len(E)==1430
for e in E:
 x=ne[e['evidence_id']];c=e['capture'];ref=str(R/c['path']) if c['root']=='artifact' else 'Frozen queue preliminary-v5/'+c['path']
 assert x['snapshot_sha256']==c['sha256'] and x['summary']==e['supports_or_contradicts'] and x['kind']==kindmap[e['kind']]
 assert x['reference']==(e.get('url') or ref) and x['locator']==ref+'; '+e['locator']
 assert x['support']==('context_only' if e['kind']=='unsuccessful_search' else 'partial')
 if e.get('accessed_at'):assert utc(x['accessed_at'])==utc(e['accessed_at'])
 else:assert x['accessed_at']==n['finished_at']
for x in n['evidence'][-4:]:assert sha(pathlib.Path(x['reference']).read_bytes())==x['snapshot_sha256']
findings={f['finding_id']:f for f in n['findings']};bindings=[]
for i,(d,t,a) in enumerate(zip(D,n['targets'],n['assessments'])):
 cid=d['case_id'];assert t['target_id']==cid and t['label']==d['source']['source_label'] and t['path']==str(R/'context/frozen-shard-02.json') and t['selector']==f'cases[case_id={cid}]'
 assert {o['path'] for o in t.get('owner_paths',[])}=={o['path'] for o in d['owner_records']}
 refs=list(dict.fromkeys(d['evidence_ids']+d['independent_review']['evidence_ids']))
 assert a['target_ids']==[cid] and a['summary']==d['reasoning'] and a['topic']==d['source']['source_label'] and a['evidence_ids']==refs
 assert a['details'].startswith(d['applicability']+' Next requirement: ') and a['dimensions'][0]['value']==d['disposition']
 expected='unknown' if d['disposition']=='unresolved' else ('concern' if d['disposition'] in ('supplied_form_correction','malformed_or_nonchemical_token') else 'supported');assert a['outcome']==expected
 assert a['dimensions'][0]['definition']=='Bounded frozen-source assessment; not a mapping/export approval.'
 f=findings.get(f'source-requirement-{i:03d}')
 if d['missing_requirement']:assert f and f['description']==d['missing_requirement'] and f['external_issues']==d['issue_refs'] and f['target_ids']==[cid] and f['status']=='deferred'
 else:assert f is None
 assert canon(d)==cm[cid]['final_decision_sha256'] and d['independent_review']['status']=='complete'
 assert canon(d)==next(z['final_decision_sha256'] for z in old['case_bindings'] if z['case_id']==cid)
 bindings.append({'case_id':cid,'final_decision_sha256':canon(d),'reviewer':cm[cid]['independent_reviewer']})
assert len(P)==len(n['actions'])==25 and len(n['findings'])==171
for i,(p,a) in enumerate(zip(P,n['actions'])):
 f=findings[f'proposal-{i:02d}']; assert f['title']==p['proposal_id'] and f['target_ids']==p['case_ids'] and f['evidence_ids']==p['evidence_ids']
 assert p['after_capture']['sha256'] in f['description'] and p['after_capture']['path'] in f['description'] and a['target_ids']==p['case_ids'] and p['proposal_id'] in a['description'] and p['owner_path'] in a['ownership_note']
 assert len(a['acceptance_checks'])==3 and 'independently review the full resulting owner payload' in a['acceptance_checks'][1]
 assert sha((R/p['after_capture']['path']).read_bytes())==p['after_capture']['sha256']
for label in ['GDP','Zinc','ATP']:
 d=next(d for d in D if d['source']['raw_source_label']==label);assert not d['proposal_ids'] and d['disposition']=='unresolved'
checks={x['check_id']:x for x in n['checks']};assert checks['proposal-labels']['status']=='failed' and checks['proposal-labels']['exit_code']==1 and not checks['proposal-labels']['required'];assert checks['maintained-export-gates']['status']=='not_applicable'
for p in ['native-validate-final.json','native-save-final.json','native-check-final.json']:assert load('validation/'+p)['exit_code']==0
log=(R/'validation/native-check-final.log').read_text();assert '"valid_reviews": 1020' in log and '"coverage": "declared_scopes_only"' in log
native_report={'schema_version':1,'reviewer':'/root/research_b','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'approve_bounded_native_source_review','inputs':[fileinfo(N/'review.yaml'),fileinfo(N/'review.md')]+[fileinfo(R/f) for f in ['decisions.json','evidence.json','proposals.json','integration/independent-review-coverage.json','prepare_native_review.py','validation/native-check-final.json','validation/native-check-final.log']],'checks':{'native_render_exact':True,'native_input_paths_and_sha256_valid':1094,'targets_assessments_final_bindings':188,'source_requirement_findings':146,'proposal_findings_and_actions':25,'root_evidence_preserved':1430,'additional_validator_evidence':4,'original_external_timestamps_preserved':True,'unsuccessful_search_context_only':True,'native_self_review_declared_honestly':True,'unavailable_MICRO_label_check_failure_retained':True,'full_retained_review_check_bundles':1020,'full_check_scope':'declared_scopes_only'},'claim_review':'Native outcomes summarize the exact bounded source decisions, including all unknown/concern dispositions, requirements and holds. Supported means the stated source disposition is supported, not an exact ingredient mapping or whole-owner approval. Actions bind only the25 active proposals; withdrawn GDP/Zn/ATP drafts have no action. Root compilation is correctly self-review; case peer-review evidence remains independently bound.','findings':[],'limits':'B authored67 primary cases and does not replace C/A scientific review of them. This conversion/delivery review grants no owner, role, export, quantity correction or production integration approval.'}
(B/'review-native-bundle.json').write_text(json.dumps(native_report,ensure_ascii=False,indent=2)+'\n')
# Read exact staged blobs in one batch, without using working-tree bytes as a substitute.
paths=git('diff','--cached','--name-only','-z').decode().rstrip('\0').split('\0'); assert len(paths)>1400 and len(paths)==len(set(paths))
allowed=(str(R)+'/',str(N)+'/');assert all(p.startswith(allowed) for p in paths)
entries={}
for row in git('ls-files','--stage','-z').decode().rstrip('\0').split('\0'):
 meta,p=row.split('\t',1);mode,oid,stage=meta.split()
 if p in paths:assert stage=='0' and mode=='100644';entries[p]=(oid,mode)
assert set(entries)==set(paths)
proc=subprocess.run(['git','cat-file','--batch'],input=('\n'.join(entries[p][0] for p in paths)+'\n').encode(),capture_output=True,check=True); raw=proc.stdout;pos=0;inventory=[];working_delta=[]
for p in paths:
 end=raw.index(b'\n',pos);oid,typ,size=raw[pos:end].decode().split();assert typ=='blob' and oid==entries[p][0];size=int(size);data=raw[end+1:end+1+size];assert raw[end+1+size:end+2+size]==b'\n';pos=end+2+size
 h=sha(data);inventory.append({'path':p,'git_blob':oid,'mode':entries[p][1],'bytes':size,'sha256':h})
 if not pathlib.Path(p).exists() or sha(pathlib.Path(p).read_bytes())!=h:working_delta.append(p)
assert pos==len(raw)
# Metadata refinements in flight require a separate final delta review.
assert not set(working_delta)-{str(R/'HANDOFF.md'),str(R/'progress.json'),str(R/'SHA256SUMS')},working_delta
critical=[str(R/f) for f in ['decisions.json','evidence.json','proposals.json','integration/independent-review-coverage.json']]+[str(N/'review.yaml'),str(N/'review.md')]
for p in critical:assert next(x['sha256'] for x in inventory if x['path']==p)==sha(pathlib.Path(p).read_bytes())
surfaces=['data/ingredients','data/curated','mappings','docs/data','UNIFIED_INGREDIENT_MAPPING.tsv'];baseline=n['source']['git_revision'];assert subprocess.run(['git','diff','--exit-code',baseline,'--',*surfaces],capture_output=True).returncode==0
tracked=set(git('ls-tree','-r','--name-only','-z',baseline,'--',*surfaces).decode().rstrip('\0').split('\0'));actual={str(p) for root in surfaces[:-1] for p in pathlib.Path(root).rglob('*') if p.is_file()};actual.add(surfaces[-1]);assert tracked==actual
assert git('diff','--cached','--name-only','--diff-filter=MDRCTU').decode()==''
assert git('rev-parse','HEAD').decode().strip()==baseline
handoff=(R/'HANDOFF.md').read_text();assert '1,094 hashed inputs' in handoff
assert '18 edits, 7 new owners' in handoff and collections.Counter(p['kind'] for p in P)=={'edit_existing_owner':18,'new_owner':7}
assert dict(collections.Counter(d['source']['source'] for d in D))=={'culturemech':130,'mediadive':53,'metatraits':4,'metatraits_gtdb':1}
assert sum(len(d['occurrence_ids']) for d in D)==322 and len({o['path'] for d in D for o in d['owner_records']})==84 and sum(not d['owner_records'] for d in D)==59
receipt={'schema_version':1,'reviewer':'/root/research_b','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'approve_bounded_staged_delivery','scope':'Actual Git index artifacts under the worker02 report and exact new native review directories. Exact index blob hashes below; future receipt/manifest additions and handoff metadata refinements require a separate delta check.','independence_limit':native_report['limits'],'head_base':baseline,'staged_file_count':len(inventory),'staged_total_bytes':sum(x['bytes'] for x in inventory),'staged_inventory_canonical_sha256':canon(inventory),'staged_files':inventory,'working_tree_metadata_delta_at_review':working_delta,'checks':{'all_staged_paths_within_two_assigned_delivery_roots':True,'only_added_regular_100644_files':True,'maintained_inventory_ignored_included':True,'maintained_file_count':len(tracked),'maintained_added_removed_or_changed':False,'final_root_case_bindings_verified':188,'active_proposals':25,'root_scientific_payloads_unchanged_since_bounded_prefinal_review':True,'native_source_review_matches_root':True,'no_active_GDP_Zn_ATP_proposals':True,'handoff_accounting_verified':True,'handoff_input_count_typo_corrected_in_working_file':True},'case_bindings':bindings,'native_review_receipt':fileinfo(B/'review-native-bundle.json'),'handoff_reviewed_bytes':fileinfo(R/'HANDOFF.md'),'quantity_comment_review':fileinfo(B/'review-quantity-comment.json'),'findings':[{'finding_id':'b-handoff-native-input-count','status':'resolved','summary':'Saved native bundle contains1094 unique hashed inputs; handoff1093 typo corrected to1094 before final receipt. If earlier handoff is staged, finalmetadata delta must stage and confirm corrected bytes.'}],'remaining_delivery_boundary':['This new receipt and native-review receipt were written after the staged snapshot and must be explicitly staged, with regenerated SHA256SUMS.','Any later issue-post receipt/progress/handoff/manifest changes need the separately promised final metadata delta check.','No commit or push was performed by this reviewer; root must verify final branch/remote delivery.','MICRO0000520 adapter remains unavailable; no whole-owner or downstream release approved.'],'self_reference_policy':'Exact staged inventory is the snapshot observed before this receipt exists in the index. It intentionally does not recursively claim its own future SHA or a future manifest hash.'}
(B/'review-final-staged.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'files':len(inventory),'bytes':receipt['staged_total_bytes'],'metadata_delta':working_delta,'native_receipt_sha256':sha((B/'review-native-bundle.json').read_bytes()),'staged_receipt_sha256':sha((B/'review-final-staged.json').read_bytes())}))
