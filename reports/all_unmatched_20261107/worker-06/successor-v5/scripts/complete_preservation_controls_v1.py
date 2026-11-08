from pathlib import Path
import json,copy,hashlib,datetime,subprocess,sys,os,importlib.util,yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient
W=Path.cwd();C=W.parents[2];R=W/'reports/all_unmatched_20261107/worker-06';S=R/'successor-v5';T=W/'.temp/info004-successor-v1';L=S/'logs/complete-preservation-controls-v1';L.mkdir(exist_ok=False);cwd=T/'complete-controls-private-cwd';cwd.mkdir(exist_ok=False);Q=C/'queue/preliminary-v5'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
module=S/'scripts/preservation_path_v1.py';spec=importlib.util.spec_from_file_location('preservation_path_v1',module);validator=importlib.util.module_from_spec(spec);spec.loader.exec_module(validator)
P=read(S/'reviewed-draft/proposals.json')['proposals'];OP=read(R/'successor-v4/proposals.json')['proposals'];changes=read(R/'successor-v4/changed-payloads.json');stocks=[x['proposal_id'] for x in changes if x['before']];assert len(stocks)==7
historical=[p['proposal_id'] for p in P if p['owner_path'].endswith('/Modified_Trace_Vitamins.yaml') or p['owner_path'].endswith('/PYGS.yaml')];assert len(historical)==2
rows=[]
def audit(name,selection):
 f=L/(name+'-proposals.json');save(f,{'schema_version':1,'proposals':selection});cmd=[sys.executable,str(C/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(Q/'shards/shard-06.json'),'--decisions',str(S/'reviewed-draft/decisions.json'),'--evidence',str(S/'reviewed-draft/evidence.json'),'--proposals',str(f),'--artifact-root',str(R),'--source-root',str(Q),'--mim-root',str(W),'--output',str(L/(name+'-audit.json'))];x=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONPATH':str(W/'src'),'PYTHONDONTWRITEBYTECODE':'1'});(L/(name+'-audit.log')).write_text(x.stdout+x.stderr);save(L/(name+'-command.json'),{'command':cmd,'cwd':str(cwd),'exit_code':x.returncode});assert x.returncode==0,x.stderr
 failures=validator.validate_retained_payloads(selection,OP,R);return {'fixture':name,'complete_case_count':188,'complete_proposal_count':len(selection),'native_campaign_audit_exit_code':x.returncode,'retention_failures':failures}
positive=audit('positive-exact105',P);assert not positive['retention_failures'];rows.append(positive)
for n,pid in enumerate(stocks+historical+['R-P-DSMZ1566-GLUCOSE10']):
 selected=copy.deepcopy(P);p=next(p for p in selected if p['proposal_id']==pid);old=R/p['after_capture']['path'];before=yaml.safe_load(old.read_text());y=copy.deepcopy(before)
 if pid in stocks:
  c=y['components'][0]
  if 'concentration_value' in c:c['concentration_value']='999'
  else:c.update(concentration_value='999',concentration_unit='G_PER_L')
  mutation='Unsupported change to the complete stock payload first solute amount; other semantic fields preserved.';assert y['components'][0]!=before['components'][0] and {k:v for k,v in y.items() if k!='components'}=={k:v for k,v in before.items() if k!='components'}
 elif pid in historical:
  entries=y['ontology_mapping']['evidence'];e=next(e for e in entries if e['evidence_type']=='MANUAL_CURATION');e['evidence_type']='LLM_SUGGESTION';mutation='Retype one genuine inherited MANUAL_CURATION mapping-evidence object in a complete otherwise unchanged historical payload.'
 else:
  oldcount=len(y['components']);y['components']=[c for c in y['components'] if 'water' not in c['component_name'].lower()];assert len(y['components'])==oldcount-1;mutation='Remove explicitly source-supported Water from the complete10%inH2O stock payload.'
 out=L/(f'negative-{n:02d}-payload.yaml');write_validated_ingredient(y,out);assert yaml.safe_load(out.read_text())==y;p['after_capture']={'root':'artifact','path':str(out.relative_to(R)),'sha256':sha(out)}
 row=audit(f'negative-{n:02d}',selected);assert any(f['proposal_id']==pid and f['code']=='RETAINED_PAYLOAD_BYTES_CHANGED' for f in row['retention_failures']);row.update(proposal_id=pid,mutation=mutation,complete_guarded_payload={'path':str(out.relative_to(W)),'sha256':sha(out)},declared_capture_hash_rebound=True,negative_detected_by='Actual report-local predecessor preservation function used by the final complete-shard validator, after native complete188case/105proposal structural audit accepts internal hashes.');rows.append(row)
result={'status':'PASS','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'filed_finding':'W08-W06-LINEAGE-CTRL-001','filed_issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1217#issuecomment-6719323521','actual_validation_path':{'path':str(module.relative_to(W)),'sha256':sha(module)},'positive_full_fixture_count':1,'negative_complete_payload_fixture_count':10,'native_complete_campaign_audit_runs':11,'cases_per_audit':188,'proposals_per_audit':105,'private_cwd':str(cwd),'pytest_or_coverage_run':False,'rows':rows,'scope':'These tests demonstrate exact preservation-path rejection of actual complete mutated payloads with correctly rebound internal hashes. They do not scientifically validate arbitrary changed formulations, establish general chemistry correctness, or alter maintained/native gates. Original weak comparisons remain historical and are not counted as full-path controls.'};save(L/'receipt.json',result);print('PASS1positive+10completepayloadnegativefixtures;11nativefullaudits')
