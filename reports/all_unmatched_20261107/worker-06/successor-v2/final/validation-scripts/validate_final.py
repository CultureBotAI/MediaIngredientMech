from pathlib import Path
import json,hashlib,subprocess,datetime,collections,sys,yaml,shutil
R=Path('reports/all_unmatched_20261107/worker-06');S=R/'successor-v2/final';T=Path('.temp/all-unmatched-worker-06/successor-v2/final-validation');T.mkdir(exist_ok=True);Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');PY='/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python';BASE='d5a7613c931d45d057eaca7b5ec15280aca76c9e';FROZEN='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,j):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
def digest(j):return hashlib.sha256(json.dumps(j,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
D=json.loads((S/'decisions.json').read_text())['decisions'];E=json.loads((S/'evidence.json').read_text())['evidence'];P=json.loads((S/'proposals.json').read_text())['proposals'];OD=json.loads((R/'decisions.json').read_text())['decisions'];OE=json.loads((R/'evidence.json').read_text())['evidence'];OP=json.loads((R/'proposals.json').read_text())['proposals'];C=json.loads((Q/'shards/shard-06.json').read_text())['cases'];H=json.loads((S/'source-holds.json').read_text())['cases'];errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
check(len(D)==len(C)==188,'case count');check(len(P)==99,'proposal count');check([x['case_id'] for x in D]==[x['case_id'] for x in C],'frozen case order');check(sha(S/'source-holds.json')==sha(R/'source-holds.json'),'source holds unchanged')
for i,(d,old,c,h) in enumerate(zip(D,OD,C,H)):
 check(d['case_input_sha256']==digest(c),'frozen source digest '+str(i));check(d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']},'raw source '+str(i));check(d['occurrence_ids']==[x['occurrence_id'] for x in c.get('occurrences',[])],'exact occurrences '+str(i));check(d['independent_review']['status']=='complete','review incomplete '+str(i))
 if i not in [19,133,35,183]:check(d==old,'unaffected decision changed '+str(i))
 check(h['frozen_case_sha256']==digest(c),'hold digest '+str(i))
 for k,v in h['frozen_source_state'].items():check(v==(c[k] if k in c else c.get('original_kg_entry',{}).get(k)),'hold flag '+str(i)+' '+k)
check(sum(len(h['frozen_source_state'].get('downstream_holds',[])) for h in H)==88,'88 holds')
oldby={p['proposal_id']:p for p in OP};oldids={'A-P-NBRC1308-TRACE','C-P-NBRC1356-TRACE'};newid='V2-P-NBRC1308-1356-TRACE';new=next(p for p in P if p['proposal_id']==newid)
firstD=json.loads((R/'successor-v2/decisions.json').read_text())['decisions'];firstP=json.loads((R/'successor-v2/proposals.json').read_text())['proposals']
for i in [19,133]:check(D[i]==firstD[i],'unchanged reconciled stock decision '+str(i))
check(new==next(p for p in firstP if p['proposal_id']==newid),'unchanged reconciled stock payload metadata')
merck=next(p for p in P if p['proposal_id']=='A-P-MERCK108339');oldmerck=oldby['A-P-MERCK108339'];a=yaml.safe_load((R/oldmerck['after_capture']['path']).read_text());b=yaml.safe_load((R/merck['after_capture']['path']).read_text())
check(b['components'][2]['component_name']=='D-glucose','canonical Merck component name');check('D(+)Glucose' in b['component_assertion']['evidence'][0]['notes'],'raw supplier spelling preserved')
b['components'][2]['component_name']=a['components'][2]['component_name'];b['component_assertion']['evidence'][0]['notes']=a['component_assertion']['evidence'][0]['notes'];b['curation_history'].pop();check(b==a,'Merck changes beyond bounded label/provenance/history')
check(not (oldids&{p['proposal_id'] for p in P}),'superseded selections retained')
for p in P:
 if p['proposal_id'] not in [newid,'A-P-MERCK108339']:check(p==oldby[p['proposal_id']],'unchanged proposal object '+p['proposal_id'])
 check(sha(R/p['after_capture']['path'])==p['after_capture']['sha256'],'after hash '+p['proposal_id'])
check(len(set(p['owner_path'] for p in P))==99,'unique owner paths')
check({x['case_id'] for x in new['source_contexts']}==set(new['case_ids']),'new source context cases')
check(set(new['applicable_occurrence_ids'])=={OD[19]['occurrence_ids'][1],OD[133]['occurrence_ids'][0]},'two stock occurrences')
check(set(new['excluded_occurrence_ids'])=={OD[19]['occurrence_ids'][0],OD[19]['occurrence_ids'][2]},'exclude1020/824')
check(new['occurrence_scopes_by_case'][OD[19]['case_id']]['included_occurrence_ids']==[OD[19]['occurrence_ids'][1]],'case19 partial scope')
other=next(p for p in P if p['proposal_id']=='A-P-NBRC1020-824-TRACE');check(set(other['applicable_occurrence_ids']).isdisjoint(new['applicable_occurrence_ids']),'stock partition disjoint');check(set(other['applicable_occurrence_ids'])|set(new['occurrence_scopes_by_case'][OD[19]['case_id']]['included_occurrence_ids'])==set(OD[19]['occurrence_ids']),'stock partition complete')
check(E[:len(OE)]==OE,'all original evidence entries unchanged')
for e in E:
 root=R if e['capture']['root']=='artifact' else Q;check(sha(root/e['capture']['path'])==e['capture']['sha256'],'capture hash '+e['evidence_id'])
# Original manifest remains authoritative for historical evidence. New successor files
# supplement it; this check never regenerates or edits old captures/reviews/ledgers.
oldmanifest=R/'SHA256SUMS';old_count=0
for line in oldmanifest.read_text().splitlines():
 h,path=line.split('  ',1);check(sha(Path(path))==h,'changed published evidence '+path);old_count+=1
check(hashlib.sha256(subprocess.check_output(['git','show',BASE+':'+str(oldmanifest)])).hexdigest()==sha(oldmanifest),'original manifest changed')
for f in ['decisions.json','evidence.json','proposals.json','source-holds.json']:
 check(hashlib.sha256(subprocess.check_output(['git','show',BASE+':'+str(R/f)])).hexdigest()==sha(R/f),'original ledger changed '+f)
paths=subprocess.check_output(['rg','--files','--no-ignore','--hidden','data/ingredients'],text=True).splitlines();records={p:yaml.safe_load(Path(p).read_text()) for p in paths if p.endswith('.yaml')};catalog=collections.defaultdict(list)
for path,y in records.items():catalog[y['identifier']].append(path)
ownerhashes={o['path']:o['sha256'] for d in D for o in d['owner_records']};proposed_ids=[]
for p in P:
 y=yaml.safe_load((R/p['after_capture']['path']).read_text());proposed_ids.append(y['identifier'])
 if p['kind']=='new_owner':check(not Path(p['owner_path']).exists() and y['identifier'] not in catalog,'new owner collision '+p['proposal_id'])
 else:ownerhashes[p['owner_path']]=p['before_sha256']
for path,h in ownerhashes.items():
 check(sha(Path(path))==h,'actual owner hash '+path);check(hashlib.sha256(subprocess.check_output(['git','show',FROZEN+':'+path])).hexdigest()==h,'not original before hash '+path)
check(len(set(proposed_ids))==len(P),'unique proposed identifiers')
changed=subprocess.check_output(['git','diff','--name-only',BASE,'--','data','mappings','src','conf','docs','UNIFIED_INGREDIENT_MAPPING.tsv','MAPPING_SEMANTICS.md'],text=True).splitlines();check(not changed,'maintained changes')
receipt={'status':'PASS' if not errors else 'FAIL','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':PY+' '+str(Path(__file__)),'case_count':len(D),'unchanged_case_count':184,'reassessed_cases':[D[i]['case_id'] for i in [19,133,35,183]],'proposal_count':len(P),'unchanged_selected_payload_count':97,'proposal_kinds':dict(collections.Counter(p['kind'] for p in P)),'evidence_count':len(E),'original_evidence_entries_preserved':len(OE),'original_manifest_files_preserved':old_count,'original_manifest_sha256':sha(oldmanifest),'cm_occurrence_count':sum(len(d['occurrence_ids']) for d in D),'downstream_hold_row_count':88,'actual_baseline_owner_count':len(ownerhashes),'maintained_records_enumerated_including_ignored':len(records),'maintained_changed_paths':changed,'inputs':{str(S/f):sha(S/f) for f in ['decisions.json','evidence.json','proposals.json','source-holds.json']},'errors':errors}
dump(S/'logs/invariants.json',receipt);assert not errors,errors
# Full shard structural binding, exact explicit artifact/source roots, no subset scope.
cmd=[PY,str(Q.parent.parent/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(Q/'shards/shard-06.json'),'--decisions',str((S/'decisions.json').resolve()),'--evidence',str((S/'evidence.json').resolve()),'--proposals',str((S/'proposals.json').resolve()),'--artifact-root',str(R.resolve()),'--source-root',str(Q),'--mim-root',str(Path.cwd()),'--output',str((S/'logs/structural-audit.json').resolve())]
x=subprocess.run(cmd,capture_output=True,text=True);(S/'logs/structural-audit.log').write_text(x.stdout+x.stderr);dump(S/'logs/structural-command.json',{'command':cmd,'exit_code':x.returncode});assert x.returncode==0,x.stdout+x.stderr
cmd=[PY,'scripts/validate_strict.py',*[str(R/p['after_capture']['path']) for p in P],'--out',str(S/'logs/schema.tsv'),'--workers','1'];x=subprocess.run(cmd,capture_output=True,text=True);(S/'logs/schema.log').write_text('Exact command/exit and payload hashes in schema-command.json. Empty producer output means no diagnostics.\n'+x.stdout+x.stderr);dump(S/'logs/schema-command.json',{'command':cmd,'exit_code':x.returncode,'proposal_count':len(P),'payload_hashes':{p['proposal_id']:p['after_capture']['sha256'] for p in P}});assert x.returncode==0,x.stdout+x.stderr
# Read-only simulation in a private isolated directory. Replace each existing owner
# by its exact selected payload once; add new payloads once. No maintained writes.
base_dir=T/'partonomy-baseline';overlay_dir=T/'partonomy-overlay'
for folder,rows in [(base_dir,records),(overlay_dir,{**records,**{p['owner_path']:yaml.safe_load((R/p['after_capture']['path']).read_text()) for p in P}})]:
 folder.mkdir(exist_ok=True)
 for mapped,name in [(True,'mapped_ingredients.yaml'),(False,'unmapped_ingredients.yaml')]:
  (folder/name).write_text(yaml.safe_dump({'ingredients':[y for y in rows.values() if (y.get('mapping_status')=='MAPPED')==mapped]},sort_keys=False,allow_unicode=True))
 cmd=[PY,'scripts/validate_component_partonomy.py','--curated-dir',str(folder)];x=subprocess.run(cmd,capture_output=True,text=True);label='partonomy-baseline' if folder==base_dir else 'partonomy-successor';(S/'logs'/f'{label}.log').write_text(x.stdout+x.stderr);dump(S/'logs'/f'{label}.json',{'command':cmd,'exit_code':x.returncode,'record_count':len(rows),'input_files':{str(folder/f):sha(folder/f) for f in ['mapped_ingredients.yaml','unmapped_ingredients.yaml']},'isolated_overlay_only':True,'maintained_write':False});assert x.returncode==0,x.stdout+x.stderr
shutil.copyfile(Path(__file__),S/'validation-scripts/validate_final.py');print('PASS full188 structural/invariants;99 schema; baseline and full successor-overlay partonomy; original1758 manifest files unchanged')
