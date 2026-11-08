"""Technical invariants only; no independent scientific or application approval."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import csv
import hashlib
import json
import sys
import traceback
import yaml

W=Path.cwd(); P=Path(__file__).absolute().parent/'payload-attempt-v2'; P.mkdir(exist_ok=False); A=W/'reports/all_unmatched_20261107/worker-08'
O=A/'successors/issue-1237-tenvit-v1'
sys.dont_write_bytecode=True;sys.path.insert(0,str(W/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient, ValidationFailedError

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text())
def dump(name,v):
    p=P/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False,default=str);f.write('\n')
    return {'path':str(p.relative_to(W)),'sha256':sha(p)}

PID='vm1237-prop-wolfe-cb-dependent'
CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
TRIGGER='CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'
EXPECTED_SHA='b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f'

def assert_payload(rec,before,w09,rows,prop,decision,olddecision,nominal):
    triples=[(x['component_name'],x['concentration_value'],x['concentration_unit']) for x in rec['components']]
    assert triples==[(x[0],x[1],'MG_PER_L') for x in rows], 'ten exact source names/order/values/units'
    assert len(triples)==10 and all('X'!=x[0] for x in triples), 'metadata is not component'
    assert 'X=100' in rec['notes'] and '100X' in rec['notes'], 'X metadata retained'
    assert rec['curation_history'][:5]==before['curation_history'] and len(before['curation_history'])==5, 'authentic five history events'
    assert rec['curation_history'][:6]==w09['curation_history'], 'W09 event authorship retained'
    assert len(rec['curation_history'])==7 and rec['curation_history'][6]['llm_assisted'] is True, 'honest W08 appended event'
    changed={k for k in set(rec)|set(before) if rec.get(k)!=before.get(k)}
    assert changed=={'components','component_assertion','notes','curation_history'}, 'bounded four field delta'
    assert rec['occurrence_statistics']=={'total_occurrences':61,'media_count':61}, 'historical counts'
    expected=['CHEBI:30961','CHEBI:30753','CHEBI:16494','CHEBI:15940','CHEBI:17015','CHEBI:49105',None,'CHEBI:15956','CHEBI:27470','CHEBI:17439']
    assert [x.get('component_id') for x in rec['components']]==expected, 'planned named entity IDs'
    assert rec['components'][6]['reference_scope']=='UNMAPPED' and 'component_id' not in rec['components'][6], 'pantothenate stereochemistry remains unresolved'
    assert sum(x['reference_scope']=='MIM_CATALOG' for x in rec['components'])==9, 'nine catalog references'
    assert rec['component_assertion']['method']=='RECIPE_TRANSCRIPTION' and rec['component_assertion']['completeness']=='UNKNOWN', 'stock closure unknown'
    assert prop['kind']=='edit_existing_owner' and prop['owner_path']=='data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml' and prop['before_sha256']=='709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738', 'genuine nonnull existing beforeimage'
    assert prop['case_ids']==[CID] and prop['source_occurrence_ids']==[TRIGGER] and prop['cb_campaign_occurrence_count']==0, 'one comparator dependency only'
    assert decision['occurrence_ids']==olddecision['occurrence_ids'] and len(decision['occurrence_ids'])==6, 'six occurrence boundaries retained'
    for src in nominal['nominal_recipe_sources'].values():
        b12=[x for x in src['inputs'] if x['printed_name']=='Vitamin B12']
        assert len(b12)==1 and 'component_id' not in b12[0] and b12[0]['printed_amount']=='0.1', 'generic nominal B12 unselected'
        water=[x for x in src['inputs'] if x['printed_name']=='Distilled water']
        assert len(water)==1 and water[0]['basis']=='listed_water_input' and src['final_stock_volume'] is None, 'water input not final volume'

def main():
    payload=O/'payloads/Wolfes_Vitamin_Mix.yaml'; assert sha(payload)==EXPECTED_SHA
    beforepath=O/'beforeimages/Wolfes_Vitamin_Mix.yaml';before=yaml.safe_load(beforepath.read_text())
    assert sha(beforepath)=='709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738'
    assert sha(W/'data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml')==sha(beforepath)
    w09path=O/'inputs/coordinator-route/captures/candidate-fe607027.yaml';w09=yaml.safe_load(w09path.read_text())
    assert sha(w09path)=='fe6070272f269fde7683696e4c46a331902ab88baac8c5cc93db7bddf9d0ec1b'
    mix=O/'inputs/coordinator-route/captures/w09/history/captures/Mixes.csv'; rows=list(csv.reader(mix.read_text().splitlines()))[41:51]
    assert sha(mix)=='9c58caac081620bbf5700b74fd957e56d3e5e17d17b282767ec26fabec522549'
    prop=read(O/'author/proposal.json');decision=read(O/'author/decision.json'); rec=yaml.safe_load(payload.read_text())
    old=read(A/'successors/issue-1227-plain-flour-v1/decisions.json')['decisions'];olddec=next(x for x in old if x['case_id']==CID)
    nominalpath=O/'research/nominal-recipe-evidence.json';nominal=read(nominalpath)
    assert_payload(rec,before,w09,rows,prop,decision,olddec,nominal)
    replay=P/'guarded-replay/Wolfes_Vitamin_Mix.yaml';write_validated_ingredient(copy.deepcopy(rec),replay)
    assert yaml.safe_load(replay.read_text())==rec
    controls=[]
    for name in ['extra-field','bad-enum']:
        mutant=copy.deepcopy(rec)
        if name=='extra-field':mutant['unknown_tenvit_native_control']=True
        else:mutant['component_assertion']['completeness']='INVALID_NATIVE_ENUM'
        inputref=dump('controls/'+name+'.json',mutant);dest=P/('controls/'+name+'-must-not-exist.yaml')
        try:write_validated_ingredient(mutant,dest)
        except ValidationFailedError as exc:
            assert not dest.exists();controls.append({'name':name,'type':'actual_native_guard','input':inputref,'rejected':True,'diagnostic':str(exc),'target_absent':True})
        else:raise AssertionError(name+' escaped native guard')
    for name in ['scaled-X100','changed-unit','reordered-inputs','invented-water','lost-W09-author','null-beforeimage','lost-occurrence','D-pantothenate','generic-B12-selected','water-as-final-volume']:
        r=copy.deepcopy(rec);p=copy.deepcopy(prop);d=copy.deepcopy(decision);n=copy.deepcopy(nominal)
        if name=='scaled-X100':r['components'][0]['concentration_value']='1000'
        elif name=='changed-unit':r['components'][0]['concentration_unit']='MG_PER_SOURCE_BATCH'
        elif name=='reordered-inputs':r['components'][0],r['components'][1]=r['components'][1],r['components'][0]
        elif name=='invented-water':r['components'].append({'component_name':'Distilled water','concentration_value':'1','concentration_unit':'L_PER_SOURCE_BATCH','reference_scope':'MIM_CATALOG','component_id':'CHEBI:15377'})
        elif name=='lost-W09-author':r['curation_history'][5]['curator']='worker08 replacement'
        elif name=='null-beforeimage':p['before_sha256']=None
        elif name=='lost-occurrence':d['occurrence_ids'].pop()
        elif name=='D-pantothenate':r['components'][6].update(component_id='CHEBI:31345',reference_scope='MIM_CATALOG')
        elif name=='generic-B12-selected':n['nominal_recipe_sources']['JCM197']['inputs'][7]['component_id']='CHEBI:17439'
        elif name=='water-as-final-volume':n['nominal_recipe_sources']['JCM197']['final_stock_volume']='1 L'
        fixture=dump('controls/'+name+'.json',{'payload':r,'proposal':p,'decision':d,'nominal':n})
        try:assert_payload(r,before,w09,rows,p,d,olddec,n)
        except AssertionError as exc:controls.append({'name':name,'type':'same_exact_invariant_path_as_positive','input':fixture,'rejected':True,'diagnostic':str(exc)})
        else:raise AssertionError(name+' escaped invariant')
    inputs=[payload,beforepath,w09path,mix,O/'author/proposal.json',O/'author/decision.json',nominalpath,W/'src/mediaingredientmech/validation/write_validated.py',W/'src/mediaingredientmech/schema/mediaingredientmech.yaml',Path(__file__)]
    dump('payload-checks.json',{'status':'PASS','at':datetime.now(timezone.utc).isoformat(),'executor':'worker08:/root/vitamins','role':'technical executor and prior source author; no independent science approval','payload_sha256':sha(payload),'guarded_replay_sha256':sha(replay),'controls':controls,'input_hashes':{str(p.relative_to(W)):sha(p) for p in inputs},'exact_source_invariants':'Ten ordered literal CB inputs and units; X metadata only; five original events plus W09 event retained; nine planned references with pantothenate hold; genuine preimage; all six case occurrences; nominal generic B12 and water input stay unselected.','scientific_approval':False,'maintained_writes':False,'application_authorized':False})
    print('PASS: guarded payload replay, two actual native negatives, ten same-path invariant controls.')

if __name__=='__main__':
    try:main()
    except BaseException as exc:
        dump('payload-checks-failure.json',{'at':datetime.now(timezone.utc).isoformat(),'error':str(exc),'traceback':traceback.format_exc(),'no_source_edits':True});raise
