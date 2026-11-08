"""Private native validation and controls; never a replacement production gate."""
import copy, dataclasses, datetime, hashlib, importlib.util, json, shutil, sys
from collections import defaultdict
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient,write_validated_ingredient,ValidationFailedError
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym

R=Path('reports/all_unmatched_20261107/worker-07');S=R/'successors/issues1226-1237-v1';P=Path('.temp/worker07-issues1226-1237-v1')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def jp(p,x):
    assert not p.exists(),p
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def loadmod(name,path):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
build=loadmod('correction_build',S/'parts/build-correction.py')
fn=loadmod('native_filename',Path('scripts/check_record_filename_case.py'))
def index(records,aliases=False):
    d=defaultdict(list)
    for path,r in records.items():
        keys=[r['identifier']]
        if aliases:keys=[r['preferred_term']]+[s['synonym_text'] for s in r.get('synonyms',[]) if is_resolving_synonym(s)]
        for key in set(keys):d[key].append(path)
    return {k:sorted(v) for k,v in d.items()}
def semantic_guard(pid,old,new,rows):
    expected=copy.deepcopy(old)
    for row in rows:expected['ontology_mapping']['evidence'][row['index']]['evidence_type']=row['suggested_value']
    if pid==build.TRIS:
        expected['components']=expected['components'][:1];expected['component_assertion']['notes']+=' '+build.SCI[pid]
    if pid in build.SCI:expected['notes']+=' '+build.SCI[pid]
    assert new.get('curation_history',[])[:len(old.get('curation_history',[]))]==old.get('curation_history',[])
    if old==new:assert not rows and pid not in build.SCI
    else:
        assert len(new['curation_history'])==len(old.get('curation_history',[]))+1
        expected['curation_history']=copy.deepcopy(new['curation_history'])
    assert expected==new,'non-allowlisted field change'
    if pid==build.TRIS:
        assert len(new['components'])==1 and new['component_assertion']['completeness']=='UNKNOWN'
        assert new['components'][0]==old['components'][0]

ps=json.loads((S/'draft-v1/proposals.json').read_text())['proposals']
olds={p['proposal_id']:p for p in json.loads((R/'successors/issue1203-v1/proposals.json').read_text())['proposals']}
allow=json.loads((S/'provenance/allowlist-v1.json').read_text());by=defaultdict(list)
for row in allow['rows']:by[row['proposal_id']].append(row)
cat={str(p):yaml.safe_load(p.read_text()) for state in ['mapped','unmapped'] for p in Path('data/ingredients',state).glob('*.yaml')}
base=copy.deepcopy(cat);oldproject=copy.deepcopy(cat);results=[];pairs={}
for p in ps:
    pid=p['proposal_id'];f=R/p['after_capture']['path'];of=R/olds[pid]['after_capture']['path']
    assert sha(f)==p['after_capture']['sha256'] and sha(of)==olds[pid]['after_capture']['sha256']
    old=yaml.safe_load(of.read_text());new=yaml.safe_load(f.read_text());pairs[pid]=(old,new)
    for row in by[pid]:build.rebind(old,sha(of),row)
    semantic_guard(pid,old,new,by[pid]);errors=[str(v) for v in validate_ingredient(new)];assert not errors
    if p['kind']=='edit_existing_owner':assert sha(Path(p['owner_path']))==p['before_sha256']
    else:assert p['owner_path'] not in base
    oldproject[p['owner_path']]=old;cat[p['owner_path']]=new
    results.append({'proposal_id':pid,'owner_path':p['owner_path'],'sha256':sha(f),'schema_errors':errors,'semantic_allowlist':'PASS','prior_bytes_retained':True,'changed':old!=new})
parts=[dataclasses.asdict(v) for v in validate_component_partonomy(cat.values())]
baselineparts=[dataclasses.asdict(v) for v in validate_component_partonomy(base.values())]
assert not parts
ids=index(cat);oldids=index(oldproject);baseids=index(base)
assert ids==oldids,'new identifier change'
newidcoll={k:v for k,v in ids.items() if len(v)>1 and v!=baseids.get(k,[])}
assert not newidcoll
aliases=index(cat,True);oldaliases=index(oldproject,True);basealiases=index(base,True)
assert aliases==oldaliases,'resolving alias drift through provenance correction'
collisions={k:v for k,v in aliases.items() if len({cat[p]['identifier'] for p in v})>1}
proposalowners={p['owner_path'] for p in ps}
affectedcoll={k:v for k,v in collisions.items() if proposalowners.intersection(v)}
project=P/'projected-catalog'
assert not project.exists()
for path,record in cat.items():
    target=project/path;target.parent.mkdir(parents=True,exist_ok=True)
    source=next((R/p['after_capture']['path'] for p in ps if p['owner_path']==path),Path(path))
    shutil.copyfile(source,target)
expected=set(cat);disk=fn.disk_paths(project)
assert expected==disk and not fn.find_drift(expected,disk) and not fn.find_collisions(expected)
controls=[]
def rejected(name,operation,types=(AssertionError,)):
    try:operation()
    except types as exc:controls.append({'control':name,'result':'rejected','reason':str(exc)})
    else:raise AssertionError('control escaped: '+name)
row=copy.deepcopy(allow['rows'][0]);old,new=pairs[row['proposal_id']]
rejected('stale_owner',lambda:build.rebind(old,'0'*64,row))
bad=copy.deepcopy(old);bad['ontology_mapping']['evidence'][row['index']]['notes']+=' altered'
rejected('stale_complete_object',lambda:build.rebind(bad,row['payload']['sha256'],row))
badrow=copy.deepcopy(row);badrow['enum']='ComponentEvidenceTypeEnum'
rejected('wrong_enum_namespace',lambda:build.rebind(old,row['payload']['sha256'],badrow))
badrow=copy.deepcopy(row);badrow['baseline_match_index']=0
rejected('historical_object_exclusion',lambda:build.rebind(old,row['payload']['sha256'],badrow))
badrow=copy.deepcopy(row);badrow['duplicate_ordinal_1based']=2
rejected('wrong_duplicate_ordinal',lambda:build.rebind(old,row['payload']['sha256'],badrow))
old,new=pairs[build.TRIS]
bad=copy.deepcopy(new);bad['components'].append(copy.deepcopy(old['components'][1]))
rejected('restored_unsupported_HCl',lambda:semantic_guard(build.TRIS,old,bad,by[build.TRIS]))
bad=copy.deepcopy(new);bad['components'].append({'component_name':'water','reference_scope':'UNMAPPED'})
rejected('invented_solvent',lambda:semantic_guard(build.TRIS,old,bad,by[build.TRIS]))
bad=copy.deepcopy(new);bad['identifier']='CHEBI:9754'
rejected('whole_stock_to_solute',lambda:semantic_guard(build.TRIS,old,bad,by[build.TRIS]))
for kind in ['unknown_field','bad_mapping_enum']:
    bad=copy.deepcopy(new)
    if kind=='unknown_field':bad['invented_field']='not native'
    else:bad['ontology_mapping']['evidence'][0]['evidence_type']='HUMAN_OR_LLM'
    dest=P/'controls'/(kind+'.yaml');dest.parent.mkdir(exist_ok=True)
    rejected('native_writer_'+kind,lambda:write_validated_ingredient(bad,dest),types=(ValidationFailedError,))
    assert not dest.exists()
proof=json.loads((S/'validation/preexisting-tracked-byte-bindings.json').read_text())
drift=[p for p,h in proof['files'].items() if not Path(p).is_file() or sha(Path(p))!=h];assert not drift
jp(S/'validation/projected-native-v1.json',{'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','selected_payloads':len(results),'changed_payloads':sum(r['changed'] for r in results),'projected_catalog_records':len(cat),'baseline_records':len(base),'baseline_partonomy':baselineparts,'projected_partonomy':parts,'identifier_collisions_introduced':newidcoll,'filename_case_drift':[],'filename_case_collisions':[],'filename_full_disk_set_matches':True,'resolving_alias_projection_identical_to_predecessor':True,'inherited_multi_identity_alias_collisions':collisions,'inherited_alias_collisions_touching_selected_owners':affectedcoll,'alias_limit':'Native resolving synonym policy used across whole projected catalog. Inherited collisions listed, no merger/suppression/role/export approval or repair. This correction adds no alias and changes no resolver result.','results':results,'controls':controls,'tracked_input_files':len(proof['files']),'tracked_input_drift':drift,'scientific_approval':False})
print(json.dumps({'status':'PASS','selected':len(results),'projected':len(cat),'partonomy_errors':len(parts),'controls':len(controls),'inherited_alias_collisions':len(collisions),'selected_owner_alias_collisions':len(affectedcoll),'tracked_inputs_unchanged':len(proof['files'])}))
