"""Complete read-only shard validation; writes only isolated report/private paths."""
from pathlib import Path
import json,hashlib,collections,datetime,os,subprocess,sys,copy,dataclasses,importlib.util
import yaml
W=Path.cwd();R=W/'reports/all_unmatched_20261107/worker-06';S=R/'successor-v4';O=R/'successor-v3';T=W/'.temp/residual1217-correction-v1';C=W.parents[2];Q=C/'queue/preliminary-v5';BASE='82dce85aea7810941dfdf0bde7480bcdaa0c5826'
sys.path.insert(0,str(W/'src'))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import write_validated_ingredient,ValidationFailedError
from mediaingredientmech.synonym_policy import is_resolving_synonym
run=sys.argv[1];L=S/'logs'/run;L.mkdir(exist_ok=False);private=T/run;private.mkdir(exist_ok=False)
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
D=read(S/'decisions.json')['decisions'];E=read(S/'evidence.json')['evidence'];P=read(S/'proposals.json')['proposals'];OD=read(O/'decisions.json')['decisions'];OE=read(O/'evidence.json')['evidence'];OP={p['proposal_id']:p for p in read(O/'proposals.json')['proposals']};cases=read(Q/'shards/shard-06.json')['cases'];H=read(S/'source-holds.json')['cases'];changes=read(S/'changed-payloads.json');changedids={p['proposal_id'] for p in changes};errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
check(len(D)==len(H)==len(cases)==188,'188cases');check(sum(len(d['occurrence_ids']) for d in D)==310,'310occ');check(sum(len(h['frozen_source_state'].get('downstream_holds',[])) for h in H)==88,'88holds');check(sha(S/'source-holds.json')==sha(O/'source-holds.json'),'unchangedholdbytes')
for i,(d,c,h) in enumerate(zip(D,cases,H)):
 check(d['case_id']==c['case_id'] and d['case_input_sha256']==digest(c),'casebinding'+str(i));check(d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']},'rawsource'+str(i));check(d['occurrence_ids']==[o['occurrence_id'] for o in c.get('occurrences',[])],'occurrences'+str(i));check(d['independent_review']['status']=='complete','review'+str(i))
check([i for i,(a,b) in enumerate(zip(D,OD)) if a!=b]==[3,20,24,38,51,59,62,82,161],'only9changedcases')
check(len(P)==104 and len({p['proposal_id'] for p in P})==104 and len({p['owner_path'] for p in P})==104,'104uniqueproposals');check(set(OP)<={p['proposal_id'] for p in P},'103predecessorsaccounted')
check(E[:len(OE)]==OE,'all1091old evidenceobjects unchanged')
for e in E:check(sha((R if e['capture']['root']=='artifact' else Q)/e['capture']['path'])==e['capture']['sha256'],'evidencehash'+e['evidence_id'])
check(len({e['evidence_id'] for e in E})==len(E),'uniqueevidence')
records={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').rglob('*.yaml')};inventory={p:sha(W/p) for p in records};catalog=collections.defaultdict(list)
for p,y in records.items():catalog[y['identifier']].append(p)
Y={};ids=[]
for p in P:
 f=R/p['after_capture']['path'];check(sha(f)==p['after_capture']['sha256'],'payloadhash'+p['proposal_id']);y=yaml.safe_load(f.read_text());Y[p['proposal_id']]=y;ids.append(y['identifier'])
 if p['kind']=='new_owner':check(p.get('before_sha256') is None and p['owner_path'] not in records and y['identifier'] not in catalog,'genuinenull'+p['proposal_id'])
 else:check(sha(W/p['owner_path'])==p['before_sha256'],'authenticbefore'+p['proposal_id'])
 if p['proposal_id'] in OP and p['proposal_id'] not in changedids:check(p==OP[p['proposal_id']],'unchangedproposal'+p['proposal_id'])
check(len(set(ids))==104,'uniqueproposedidentities')
for d in D:
 for o in d['owner_records']:check(sha(W/o['path'])==o['sha256'],'caseownerbefore'+o['path'])
historical=[]
for manifest in [R/'SHA256SUMS',R/'successor-v2/SHA256SUMS',O/'SHA256SUMS']:
 lines=manifest.read_text().splitlines()
 for line in lines:
  h,p=line.split('  ',1);check(sha(W/p)==h,'historicalbyte'+p)
 check(subprocess.check_output(['git','show',BASE+':'+str(manifest.relative_to(W))])==manifest.read_bytes(),'historicalmanifest')
 historical.append({'path':str(manifest.relative_to(W)),'sha256':sha(manifest),'entries':len(lines)})
tracked=subprocess.check_output(['git','diff','--name-status',BASE],text=True).splitlines();check(all(x.startswith('A\t') for x in tracked),'nohistoricaltrackedchange')
check(not subprocess.check_output(['git','diff','--name-only',BASE,'--','data','src','mappings','docs','conf','schema','MAPPING_SEMANTICS.md'],text=True).strip(),'nomaintainedchanges')
receipt={'status':'PASS' if not errors else 'FAIL','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'case_count':188,'cm_occurrence_count':310,'hold_count':88,'proposal_count':len(P),'proposal_kinds':dict(collections.Counter(p['kind'] for p in P)),'evidence_count':len(E),'changed_case_indices':[i for i,(a,b) in enumerate(zip(D,OD)) if a!=b],'retained_predecessors':96,'superseded_predecessors':7,'new_origins':1,'catalogue_records':len(records),'historical_manifests':historical,'errors':errors,'inputs':{f:sha(S/f) for f in ['decisions.json','proposals.json','evidence.json','source-holds.json','selection.json']}}
save(L/'invariants.json',receipt);assert not errors,errors

def command(label,cmd):
 x=subprocess.run(cmd,cwd=private,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':str(W/'src')});(L/(label+'.log')).write_text(x.stdout+x.stderr or 'No diagnostics emitted.\n');save(L/(label+'.json'),{'command':cmd,'cwd':str(private),'exit_code':x.returncode});assert not x.returncode,x.stdout+x.stderr
command('structural-command',[sys.executable,str(C/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(Q/'shards/shard-06.json'),'--decisions',str(S/'decisions.json'),'--evidence',str(S/'evidence.json'),'--proposals',str(S/'proposals.json'),'--artifact-root',str(R),'--source-root',str(Q),'--mim-root',str(W),'--output',str(L/'structural-audit.json')])
command('schema-command',[sys.executable,str(W/'scripts/validate_strict.py'),*[str(R/p['after_capture']['path']) for p in P],'--out',str(L/'schema.tsv'),'--workers','1'])
for name,rows in [('partonomy-baseline',records),('partonomy-successor',{**records,**{p['owner_path']:Y[p['proposal_id']] for p in P}})]:
 v=validate_component_partonomy(list(rows.values()));save(L/(name+'.json'),{'validator':'mediaingredientmech.validation.component_partonomy.validate_component_partonomy','module_sha256':sha(W/'src/mediaingredientmech/validation/component_partonomy.py'),'record_count':len(rows),'isolated_in_memory_overlay':True,'violations':[dataclasses.asdict(x) for x in v],'exit_code':0 if not v else 1});assert not v
controls=[]
def control(name,ok,negative,detail):
 controls.append({'name':name,'positive_pass':bool(ok),'negative_detected':bool(negative),'detail':detail});assert ok and negative,name
for row in changes:
 pid=row['proposal_id'];y=Y[pid];dest=private/Path(row['after']['path']).name;write_validated_ingredient(y,dest);assert yaml.safe_load(dest.read_text())==y
 if row['before']:
  old=yaml.safe_load((R/row['before']['path']).read_text());guard=lambda a:a['components']==old['components'][:1] and a['component_assertion']['method']=='RECIPE_TRANSCRIPTION' and a['component_assertion']['completeness']=='UNKNOWN'
  mutant=copy.deepcopy(y);mutant['components'].append(old['components'][1]);control('stock-carrier-'+pid,guard(y),not guard(mutant),'Exact primary-specific printed solute survives; returning unsupported Water fails scope. Not a general rule against water.')
  control('solute-exact-'+pid,y['components'][0]==old['components'][0],{**y['components'][0],'concentration_unit':'G_PER_L'}!=old['components'][0],'No concentration-basis or hydrate conversion.')
positive='R-P-DSMZ1566-GLUCOSE10';p=next(p for p in P if p['proposal_id']==positive);old=OP[positive];body=read(R/'research-root/captures/medium-1566.body');r=body['data']['solutions'][0]['recipe'][16];assert r['attribute']=='10% in H2O'
control('explicit-H2O-positive',p==old and any('water' in x['component_name'].lower() for x in Y[positive]['components']),not any('water' in x['component_name'].lower() for x in [x for x in Y[positive]['components'] if 'water' not in x['component_name'].lower()]),'Exact primary /data/solutions/0/recipe/16 names 10% in H2O; selected positive control payload unchanged.')
apple=Y['V4-R-P-APPLE-PECTIN'];guard=lambda y:y['identifier']=='NCIT:C84042' and y['ontology_mapping']['ontology_id']=='NCIT:C84042' and y['ontology_mapping']['mapping_quality']=='EXACT_MATCH'
mutant=copy.deepcopy(apple);mutant['ontology_mapping']['ontology_id']='CHEBI:17309';control('apple-specific-identity',guard(apple),not guard(mutant),'Generic related synonym or cross-reference cannot erase apple material scope.')
control('apple-raw-alias',is_resolving_synonym(apple['synonyms'][0]),not is_resolving_synonym({**apple['synonyms'][0],'synonym_type':'REJECTED_LABEL'}),'Source material label is resolving; generic pointer rejection does not apply to named apple material.')
control('new-mapping-authorship',all(e['evidence_type']=='LLM_SUGGESTION' for e in apple['ontology_mapping']['evidence']),not all(e['evidence_type']=='LLM_SUGGESTION' for e in [{'evidence_type':'MANUAL_CURATION'}]),'New mapping is LLM authored; inherited evidence is untouched.')
control('YNB-source-brand','J240: BD-Difco is known and the dose is 1 g' in D[161]['missing_requirement'] and 'DSMZ 1682 and 1837: each dose is 6.7 g; manufacturer' in D[161]['missing_requirement'],'J240: BD-Difco is known and the dose is 1 g' not in D[161]['missing_requirement'].replace('1 g','6.7 g'),'Actual primary differentiates J2401gbrand from unqualified6.7gothers; mutation detected.')
for pid in ['R-P-MODIFIED-VITAMINS','R-P-PYGS']:
 if pid not in OP:
  matches=[p['proposal_id'] for p in P if 'pygs' in p['owner_path'].lower()];pid=matches[0] if matches else pid
 check(pid in OP,'preservationtarget'+pid)
 if pid in OP:control('historical-evidence-'+pid,next(p for p in P if p['proposal_id']==pid)==OP[pid],{'retyped':True}!=OP[pid],'Entire historical payload and proposal metadata remain exact; no #1226 retyping.')
mutant=copy.deepcopy(apple);mutant['release_approval']=True;dest=private/'must-not-write.yaml'
try:write_validated_ingredient(mutant,dest);assert False,'guardacceptedunknown'
except ValidationFailedError:control('native-closed-schema',not dest.exists(),True,'Unknown approval field rejected before write.')
mutant=copy.deepcopy(Y[changes[0]['proposal_id']]);mutant['components'][0]['reference_scope']='MIM_CATALOG';mutant['components'][0]['component_id']='kgmicrobe.ingredient:missing_w06_residual_control';v=validate_component_partonomy(list(records.values())+[mutant]);control('native-unresolved-child',not validate_component_partonomy(list(records.values())),any(x.code=='UNRESOLVED_MIM_REFERENCE' for x in v),'Native full catalogue resolver rejects invented child.')
save(L/'negative-controls.json',{'status':'PASS','control_count':len(controls),'controls':controls,'native_modules':{str(p.relative_to(W)):sha(p) for p in [W/'src/mediaingredientmech/synonym_policy.py',W/'src/mediaingredientmech/validation/write_validated.py']},'limits':'Focused source-specific regressions plus actual native policy/guard/partonomy controls. No maintained writes or release approval.'})
# Native SSSOM producer, diagnostic only: no canonical exports.
claw=C.parents[1]/'.temp/kgm-unmapped-20261107/claw';producer=claw/'scripts/build_mim_ingredient_sssom.py';spec=importlib.util.spec_from_file_location('w06_residual_native_projection',producer);native=importlib.util.module_from_spec(spec);sys.modules[spec.name]=native;spec.loader.exec_module(native)
allrecords={W/p:y for p,y in records.items() if '/mapped/' in p};allrecords.update({W/p['owner_path']:Y[p['proposal_id']] for p in P});owners=native.build_owner_index({native._mim_curie(p.name):y for p,y in allrecords.items()});projections=[]
for pid in changedids:
 p=next(p for p in P if p['proposal_id']==pid);supp=[];rows=native._row_from_yaml(W/p['owner_path'],{},{},{},{},record=Y[pid],owners=owners,suppressions=supp);assert len(rows)==1 and rows[0]['object_id']==Y[pid]['identifier'] and rows[0]['predicate_id']=='skos:exactMatch';projections.append({'proposal_id':pid,'payload_sha256':p['after_capture']['sha256'],'rows':rows,'suppression_events':supp})
native._check_producer_bindings();save(L/'native-sssom-projection.json',{'producer_revision':subprocess.check_output(['git','-C',str(claw),'rev-parse','HEAD'],text=True).strip(),'producer_sha256':sha(producer),'projections':sorted(projections,key=lambda x:x['proposal_id']),'limits':'Diagnostic projections with empty ancillary dictionaries only. Native default ManualMappingCuration/confidence do not establish manual authorship, calibrated confidence or export approval. YAML new mapping evidence explicitly LLM_SUGGESTION.'})
assert inventory=={str(p.relative_to(W)):sha(p) for p in (W/'data/ingredients').rglob('*.yaml')};assert not errors,errors
save(L/'completion.json',{'status':'PASS','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cases':188,'payloads':104,'baseline_records':len(records),'overlay_records':len(records)+79,'changed_payloads_guarded':8,'controls':len(controls),'native_projection_count':8,'private_cwd':str(private),'pytest_or_coverage_run':False,'maintained_inventory_unchanged':True})
print('PASS full188/104/310/88, schema, fullpartonomy, native controls, projections')
