"""Independent final accounting replay; never executes root author mutations.

Supply explicit assembly directory, selection config and saved native YAML paths.
This successor preserves the unexecuted initial checker and failed assembly.
All outputs/fixtures are confined to this independent review directory.
"""
import copy, datetime, hashlib, importlib.util, json, pathlib, shutil, sys, yaml
ROOT=pathlib.Path.cwd();R=ROOT/'reports/all_unmatched_20261107/worker-08';S=R/'successors/issue-1227-v1';O=S/'independent-review/final_assembly'
sys.path.insert(0,str(S/'scripts'))
import assemble as a
import check_identity_obligations as identity
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
checks=[]
def check(name,value,detail=None):
 checks.append({'check':name,'passed':bool(value),'detail':detail});assert value,(name,detail)
B=pathlib.Path(sys.argv[1]).resolve();config_path=pathlib.Path(sys.argv[2]).resolve();native_path=pathlib.Path(sys.argv[3]).resolve();md_path=native_path.with_suffix('.md')
check('explicit final selection paths',B==S/'final-v2' and config_path==S/'provenance/final-selection-v2.json' and a.SELECTION==B and a.SELECTION_CONFIG==config_path)
config=read(config_path);parent={k:read(a.checked_capture(v,R)) for k,v in config['parent_inputs'].items()};groups=[]
for g in config['groups']:
 x=copy.deepcopy(g)
 for k in ['decisions','proposals','evidence']:
  value=read(a.checked_capture(g['inputs'][k],R));x[k]=value[k] if isinstance(value,dict) else value
 x['peer']=read(a.checked_capture(g['peer_capture'],R));groups.append(x)
 check('distinct author/reviewer '+g['name'],g['author']!=g['reviewer'])
 check('full independent coverage '+g['name'],x['peer']['full_payload_review'] is True and not x['peer']['open_blocking_findings'])
 for k in ['decisions','proposals','evidence']:
  ref=g['inputs'][k];check('peer index hash '+g['name']+' '+k,x['peer']['input_hashes'][ref['path']]==ref['sha256'])
 for path,h in x['peer']['input_hashes'].items():check('peer exact reviewed input '+g['name']+' '+path,sha(R/path)==h)
root_e=read(a.checked_capture(config['root_evidence'],R))['evidence'] if config.get('root_evidence') else []
replayed=a.assemble(parent,groups,R,root_e)
for name,obj in replayed.items():check('exact in-memory assembly replay '+name,read(B/name)==obj)
D=read(B/'decisions.json')['decisions'];P=read(B/'proposals.json')['proposals'];E=read(B/'evidence.json')['evidence'];prov=read(B/'assembly-provenance.json')
check('exact188/113 scope',len(D)==188 and len(P)==113)
check('own inorganic science has separate peer',next(g for g in groups if g['name']=='inorganic_forms')['reviewer']=='/root/vitamins')
check('organic final uses corrected reviewer receipt',next(g for g in groups if g['name']=='organic_products')['peer_capture']['path'].endswith('/review-v2.json'))
vm=next(g for g in groups if g['name']=='vitamins_mixtures')
check('vitamin metadata successor peer selected',vm['peer_capture']['path'].endswith('/review-v3.json') and vm['peer']['metadata_review']['status']=='resolved')
prior_vm=read(S/'independent-review/vitamins_mixtures/review.json')
for field in ['case_ids','proposal_ids','case_hashes','payload_hashes','case_reviews','proposal_reviews','unapproved_fields']:check('vitamin complete prior review preserved '+field,vm['peer'][field]==prior_vm[field])
original_e={e['evidence_id']:e for e in parent['evidence']['evidence']};final_e={e['evidence_id']:e for e in E}
referral=read(S/'COORDINATOR-ASSEMBLY-FINDING-v1.json')
for path,h in referral['failed_assembly_inputs'].items():check('failed first assembly preserved '+path,sha(S/path)==h)
failed_e={e['evidence_id']:e for e in read(S/'evidence.json')['evidence']}
check('metadata successor keeps evidence set',set(failed_e)==set(final_e))
for eid,entry in failed_e.items():check('only routed local-query category changed '+eid,final_e[eid]==(dict(entry,kind='local_validation') if eid=='vm1227-v2-dl-ontology' else entry))
check('metadata successor keeps exact proposal rows',read(S/'proposals.json')==read(B/'proposals.json'))
check('historical evidence immutable',all(final_e[k]==v for k,v in original_e.items()))
Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
for e in E:
 c=e['capture'];path=(R if c['root']=='artifact' else Q)/c['path'];check('evidence bytes '+e['evidence_id'],sha(path)==c['sha256'])
validation=read(S/'validation/combined-validation.json')
check('guarded/strict/partonomy success',validation['guarded_replays']==113 and validation['strict_exit_code']==0 and all(not validation[k] for k in ['baseline_partonomy_violations','overlay_partonomy_violations','label_errors']) and not validation['preservation']['mismatches'])
check('bounded validation distinct from failed admission',validation['bounded_correction_validation_status']=='PASS' and validation['owner_admission_status']=='HELD' and len(validation['owner_admission_failures'])==1)
admission=validation['owner_admission_failures'][0]
check('exact Trypticase collision remains failed',admission['proposal_id']=='op1201-trypticase-soy-broth' and admission['gate_status']=='failed' and admission['maintained_admission']=='HELD' and admission['failure']==['changed identity collides','MICRO:0000113',['data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml']])
check('admission binds unchanged selected candidate',admission['selected_sha256']==next(p['after_capture']['sha256'] for p in P if p['proposal_id']==admission['proposal_id']))
for path,h in admission['owner_hashes'].items():check('admission exact owner '+path,sha(ROOT/path)==h)
preservation_ref=validation['preservation']['independent_complete_preservation_receipt']
preservation_path=R/preservation_ref['path'];preservation=read(preservation_path)
check('complete preservation exact receipt',sha(preservation_path)==preservation_ref['sha256'])
check('complete preservation status',preservation['status']=='PASS' and preservation['failure_count']==0 and not preservation['failures'] and not preservation['inventory_failures'])
before=read(S/'provenance/predecessor-working-bytes.json')
check('preservation original inventory binding',preservation['predecessor_input']['sha256']==sha(S/'provenance/predecessor-working-bytes.json'))
for group,value in preservation['groups'].items():
 if 'checks' in value:check('preservation complete subgroup '+group,value['checks']==value['passed'] and value['failed']==0)
check('preservation distinguishes original capture and supplement',len(before['files'])==validation['preservation']['prior_captured_working_files']==preservation['groups']['initial_hashed_working_files']['checks']==15633 and before['tracked_count']==validation['preservation']['declared_tracked_entries']==15643 and preservation['groups']['supplemental_ten_baseline_entries']['checks']==validation['preservation']['supplemental_git_tree_entries']==10)
check('W05 complete manifest coverage',preservation['groups']['w05_all_manifest_members']['checks']==6968)
for name,ref in preservation['receipt_files'].items():check('preservation subsidiary receipt '+name,sha(R/ref['path'])==ref['sha256'])
for path,h in validation['input_hashes'].items():check('native-validation current input '+path,sha(ROOT/path)==h)
idreport=read(S/'validation/identity-obligations.json');check('identity receipt exact input',idreport['input_sha256']==sha(B/'proposals.json') and idreport['selected_payload_count']==113 and not any(idreport['native_failures'].values()))
fixture=O/'.temp/final-v2-identity-fixture';fixture.mkdir(parents=True,exist_ok=False);native=identity.load_rules();native.INGREDIENTS_DIR=fixture;rows=[]
for p in P:
 path=a.checked_capture(p['after_capture'],R);dest=fixture/pathlib.Path(p['owner_path']).name;check('unique identity fixture '+p['proposal_id'],not dest.exists());shutil.copyfile(path,dest)
 rec=yaml.safe_load(dest.read_text());subject=identity.mim_curie_for_stem(dest.stem);native._subject_to_path.cache_clear();check('native own-ID fixture '+p['proposal_id'],native.record_identifier(subject)==rec['identifier']);rows.extend(identity.projected_obligations(subject,rec))
native._subject_to_path.cache_clear()
for rule in ['b1','b2','b3','b5','d']:check('independent native proposed obligations '+rule,not list(getattr(native,'evaluate_rule_'+rule)(rows)))
bad=[dict(row,predicate_id='skos:closeMatch') for row in rows if native.record_identifier(row['subject_id'])==row['object_id']]
check('RuleD exercised every degraded own-ID',len(bad)>0 and len(list(native.evaluate_rule_d(bad)))==len(bad))
check('native identity receipt row count',len(rows)==idreport['projected_obligation_rows'])
doc=yaml.safe_load(native_path.read_text());check('saved native Markdown exists',md_path.is_file())
check('native301 exact targets',{t['target_id'] for t in doc['targets']}=={d['case_id'] for d in D}|{p['proposal_id'] for p in P} and len(doc['targets'])==301)
check('native root honest self-review',doc['reviewer']['independence']=='self_review' and doc['verdict']=='pass_with_limitations')
check('native target assessment coverage',{t for x in doc['assessments'] for t in x['target_ids']}=={t['target_id'] for t in doc['targets']})
check('inherited concern assessments remain',{'retained-valerate-owner-hold','retained-thauer-stereo-owner-hold','retained-soy-family-hold','retained-tpp-referenced-owner-hold','retained-jcm403-class-relation-limit','retained-menadione-owner-scope','retained-thauer-evidence-limit'} <= {x['assessment_id'] for x in doc['assessments'] if x['outcome']=='concern'})
check('native named Trypticase concern remains',any(x['assessment_id']=='tsb-existing-owner-admission-hold' and x['outcome']=='concern' and x['target_ids']==['op1201-trypticase-soy-broth'] for x in doc['assessments']))
admission_check=next(x for x in doc['checks'] if x['check_id']=='tsb-owner-admission')
check('native failed admission is not a pass',admission_check['status']=='failed' and admission_check['required'] is False and admission_check['exit_code']==1 and admission_check['target_ids']==['op1201-trypticase-soy-broth'])
for x in doc['source']['inputs']:check('native exact source input '+x['path'],sha(ROOT/x['path'])==x['sha256'])
for ev in doc['evidence']:
 path=ROOT/ev['reference'];check('native evidence exact '+ev['evidence_id'],sha(path)==ev['snapshot_sha256'])
old=yaml.safe_load((S/'inputs/external-review/review.yaml').read_text());ofs={f['finding_id']:f for f in old['findings']};nfs={f['finding_id']:f for f in doc['findings']}
check('12 distinct native findings with actual predecessor lineage',len(nfs)==12 and set(nfs)==set(ofs) and all(x['status']=='resolved' for x in nfs.values()))
for fid,f in ofs.items():
 check('original finding severity '+fid,nfs[fid]['severity']==f['severity'])
 check('actual native predecessor '+fid,nfs[fid]['previous_occurrences']==[{'repository':old['repository'],'review_id':old['review_id'],'finding_id':fid}])
new=read(S/'new-finding-dispositions.json')['findings'];check('6 distinct routed new findings',len(new)==6 and len({x['finding_id'] for x in new})==6)
corrections={x['assessment_id']:x for x in doc['assessments'] if x['assessment_id'].startswith('correction-')}
check('all six JSON findings have distinct native correction assessments',set(corrections)=={'correction-'+f['finding_id'].lower() for f in new})
for f in new:
 c=corrections['correction-'+f['finding_id'].lower()]
 check('new correction lineage binding '+f['finding_id'],c['summary']==f['bounded_disposition'] and c['target_ids']==f['proposal_ids'] and c['outcome']=='supported' and 'new-findings' in c['evidence_ids'] and f['finding_id'] in c['details'] and 'original severity '+f['original_severity'] in c['details'] and 'normalized '+f['normalized_severity'] in c['details'])
 for p in f['final_payload_bindings']:check('new finding exact payload '+f['finding_id']+' '+p['proposal_id'],next(v for v in P if v['proposal_id']==p['proposal_id'])==p)
# Native schema validation is read-only. Render equality checks the actual saved pair.
spec=importlib.util.spec_from_file_location('independent_record_review',ROOT/'scripts/record_review.py');rr=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rr;spec.loader.exec_module(rr)
rr.validate_review(doc)
check('native structured validation',True)
render=rr.render_markdown(doc)
check('native YAML Markdown exact pair',md_path.read_text()==render)
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/inorganics','author':'/root','status':'PASS','scope':'Independent exact assembly mechanics, separately authored peer bindings, native review and identity-obligation checks. This reviewer authored inorganic scientific proposals; those are excluded from this scientific approval and rely on the separate vitamins review. Organic science has its own sealed51/31 receipt; no science is reapproved by these checks.','counts':{'cases':len(D),'payloads':len(P),'evidence':len(E),'native_targets':len(doc['targets']),'native_findings':len(doc['findings']),'degraded_own_id_controls':len(bad)},'input_hashes':{str(p.relative_to(ROOT)):sha(p) for p in [config_path,B/'decisions.json',B/'proposals.json',B/'evidence.json',B/'assembly-provenance.json',S/'validation/combined-validation.json',S/'validation/identity-obligations.json',S/'issue-dispositions.json',S/'new-finding-dispositions.json',native_path,md_path]},'script_hashes':{str(p.relative_to(ROOT)):sha(p) for p in sorted((S/'scripts').glob('*.py'))},'checks':checks,'findings':[],'limitations':['No maintained corpus or downstream SSSOM/export built or validated.','Complete owner, source-specific, role and cross-shard holds remain. Root is honestly recorded as integration author/self-review.','This receipt does not replace coordinator final-head acceptance.']}
report['open_blocking_findings']=[]
report['full_selection_accounting_review']=True
report['independent_scientific_approval_of_inorganic_authored_payloads']=False
report['maintained_admission']='HELD: exact preexisting Trypticase/Bacto MICRO:0000113 collision. Bounded correction validation is not whole-owner admission.'
report['counts']['routed_new_correction_assessments']=len(corrections)
path=O/'final-review.json';assert not path.exists();path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'status':report['status'],'counts':report['counts'],'checks':len(checks),'sha256':sha(path)}))
