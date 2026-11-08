"""Independent exact full-record and author-core audit; no source mutation."""
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[3]
O = Path(__file__).resolve().parent
A = R / 'reports/all_unmatched_20261107/worker-10'
S = A / 'successor-v7'
B = A / 'successor-v6/final-core'
Q = R.parents[2] / 'queue/preliminary-v5'
W = R.parents[1] / 'w07/worktree/.temp/columbia-continuity-independent-v1'
HEAD = 'c66d6d3665368fe1ae8986fb7c16340a103582c1'
NEW = 'sv7-dependent-columbia-unmapped0118-partition'
DIFCO = 'sv3-hm-difco-columbia1270'
TRIS = 'sv1-buffers-tris_hcl_0_2m_ph7_5_dsmz273'
HEPES = 'sv1-buffers-hepes_2m_ph7_jcm556_1200'
OXOID = 'sv1-bio-columbia_blood_agar_oxoid_m2224'
EXPECTED = {NEW: '0bbcb8bd4d35c877569958065243479c868d92b77c741435101add857c2eceaa', DIFCO: 'f4daef57d7e912ee28682bcc989d0c01178b1e14a7bf42014e05adf685ebb0c4', TRIS: '3a2c871e217b65e80ca5c586839bc759b01b6ded50f47e5852e4acbab1951f1a', HEPES: 'daef13c3e059e1fe24aa77a20a29c6c75976ff960a5d63890628cbce78d40217'}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(v): return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
def load(p): return json.loads(p.read_text())
def bind(p): return {'path': str(p), 'sha256': sha(p), 'bytes': p.stat().st_size}
checks=[]
def check(label, condition):
    checks.append({'check': label, 'pass': bool(condition)})
    assert condition, label
def changes(a,b,path=''):
    if type(a) != type(b): return [{'field':path, 'before':a, 'after':b}]
    if isinstance(a,dict):
        out=[]
        for k in sorted(a.keys() | b.keys()):
            if k not in a or k not in b: out.append({'field':path+'/'+k,'before':a.get(k),'after':b.get(k)})
            else: out.extend(changes(a[k],b[k],path+'/'+k))
        return out
    if isinstance(a,list):
        out=[]
        for i in range(max(len(a),len(b))):
            if i>=len(a) or i>=len(b): out.append({'field':path+'/'+str(i),'before':a[i] if i<len(a) else None,'after':b[i] if i<len(b) else None})
            else: out.extend(changes(a[i],b[i],path+'/'+str(i)))
        return out
    return [] if a==b else [{'field':path,'before':a,'after':b}]
def capture(c):
    p=(A if c['root']=='artifact' else Q)/c['path']
    check('capture '+str(p), sha(p)==c['sha256'])
    return p
check('unchanged HEAD',subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()==HEAD)
freeze=load(S/'author-freeze-v3.json')
for c in freeze['core'].values(): capture(c)
old={n:load(B/(n+'.json'))[n] for n in ['decisions','proposals','evidence']}
new={n:load(S/'author-core-v3'/(n+'.json'))[n] for n in old}
op={p['proposal_id']:p for p in old['proposals']}; np={p['proposal_id']:p for p in new['proposals']}
check('127 authentic old proposals plus one dependent',len(op)==127 and len(np)==128 and set(np)-set(op)=={NEW} and not set(op)-set(np))
payload_matrix=[]
for pid,p in np.items():
    after_path=capture(p['after_capture']); after=yaml.safe_load(after_path.read_text())
    if pid in op:
        before_path=capture(op[pid]['after_capture'])
        before_bytes=subprocess.check_output(['git','show',HEAD+':'+str(before_path.relative_to(R))],cwd=R)
        check(pid+' predecessor equals exact Git blob',before_path.read_bytes()==before_bytes)
        before=yaml.safe_load(before_path.read_text())
    else:
        before_path=R/'data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml'
        before=yaml.safe_load(before_path.read_text())
        check('0118 real current Git preimage',subprocess.check_output(['git','show',HEAD+':'+str(before_path.relative_to(R))],cwd=R)==before_path.read_bytes())
        check('0118 copied preimage exact',before_path.read_bytes()==(S/'inputs/Columbia_Blood_Agar_Base.before.yaml').read_bytes())
    delta=changes(before,after)
    if pid not in EXPECTED:
        check(pid+' retained exact payload',before_path.read_bytes()==after_path.read_bytes())
    else:
        check(pid+' exact frozen after hash',sha(after_path)==EXPECTED[pid])
        check(pid+' all original history objects exact and one append',after['curation_history'][:-1]==before['curation_history'] and len(after['curation_history'])==len(before['curation_history'])+1)
        event=after['curation_history'][-1]
        check(pid+' truthful new root AI attribution',event['curator']=='Codex worker10 /root' and event['llm_assisted'] is True)
        rollback=copy.deepcopy(after);rollback['curation_history']=before['curation_history']
        if pid in [TRIS,HEPES]:
            check(pid+' literal UNKNOWN change',before['component_assertion']['completeness']=='PARTIAL' and after['component_assertion']['completeness']=='UNKNOWN')
            rollback['component_assertion']['completeness']='PARTIAL'
        elif pid==DIFCO:
            check('Difco exact preserved vendor source synonym',after['synonyms']==[yaml.safe_load((R/'data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml').read_text())['synonyms'][2]])
            check('Difco prior notes prefix',after['notes'].startswith(before['notes']+' '))
            rollback['notes']=before['notes'];rollback['synonyms']=before['synonyms']
        else:
            check('generic notes prefix',after['notes'].startswith(before['notes']+' '))
            check('generic exact three text/source rows',len(after['synonyms'])==3 and all({k:v for k,v in x.items() if k!='synonym_type'}=={k:v for k,v in y.items() if k!='synonym_type'} for x,y in zip(before['synonyms'],after['synonyms'])))
            check('generic vendor labels rejected only',after['synonyms'][0]==before['synonyms'][0] and [x['synonym_type'] for x in after['synonyms'][1:]]==['REJECTED_LABEL','REJECTED_LABEL'])
            rollback['notes']=before['notes'];rollback['synonyms']=before['synonyms']
        check(pid+' exact allowed changes only',rollback==before)
    payload_matrix.append({'proposal_id':pid,'before':bind(before_path),'after':bind(after_path),'changed':bool(delta),'full_record_science_review':pid in EXPECTED or pid==OXOID,'field_changes':delta if pid in EXPECTED else []})
check('three old changed payloads and124 exact retained',sum(x['changed'] for x in payload_matrix if x['proposal_id']!=NEW)==3 and sum(not x['changed'] for x in payload_matrix)==124)
check('new generic sole authentic preimage use among affected',np[NEW]['before_sha256']==sha(R/'data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml') and all(np[p]['before_sha256'] is None for p in [DIFCO,TRIS,HEPES,OXOID]))
changed_props=[p for p in op if op[p]!=np[p]]
check('exact four old proposal metadata changes',set(changed_props)=={DIFCO,TRIS,HEPES,OXOID})
check('exact four old case changes', [i for i,(a,b) in enumerate(zip(old['decisions'],new['decisions'])) if a!=b]==[80,118,135,178])
check('all188 source identities/order retained',len(new['decisions'])==188 and [d['case_id'] for d in old['decisions']]==[d['case_id'] for d in new['decisions']])
for i,(a,b) in enumerate(zip(old['decisions'],new['decisions'])):
    check('case source membership '+str(i),all(a[k]==b[k] for k in ['case_id','case_input_sha256','source','occurrence_ids']))
check('304 original occurrences unchanged',sum(len(d['occurrence_ids']) for d in new['decisions'])==304)
check('all1218 old evidence exact',len(old['evidence'])==1218 and new['evidence'][:1218]==old['evidence'] and len(new['evidence'])==1224)
check('all new evidence typed without primary promotion',all(e['kind'] in ['source_snapshot','local_validation'] for e in new['evidence'][1218:]))
v2=load(S/'author-core-v2/decisions.json')['decisions']
fix_changes=[]
for i,(a,b) in enumerate(zip(v2,new['decisions'])):
    if i not in [80,135]:check('v3 non-target case exact '+str(i),a==b);continue
    check('historical completion block exact '+str(i),a['completion_reassessment']==b['completion_reassessment'])
    marker=b['source_successor_v7'];check('active UNKNOWN clarification '+str(i),marker['old_completion_reassessment_is_historical'] is True and marker['active_component_assertion']['completeness']=='UNKNOWN')
    rollback=copy.deepcopy(b)
    for k in set(marker)-set(a['source_successor_v7']):del rollback['source_successor_v7'][k]
    check('only added marker fields '+str(i),rollback==a)
    check('active capture exact '+str(i),marker['active_component_assertion']['selected_capture']==np[b['proposal_ids'][0]]['after_capture'])
    fix_changes.append({'case_index':i,'before_object_sha256':objsha(a),'after_object_sha256':objsha(b),'preserved_historical_object_sha256':objsha(a['completion_reassessment']),'diff':changes(a,b)})
for name in ['proposals','evidence']:
    check('v3 exact '+name,(S/'author-core-v2'/(name+'.json')).read_bytes()==(S/'author-core-v3'/(name+'.json')).read_bytes())
check('finding original preserved in source packet',(O/'historical-completeness-finding-v1.json').read_bytes()==(S/'inputs/historical-completeness-finding-v1.json').read_bytes())
routes=load(S/'source-routing.json');matrix=load(W/'review/science/current-source-occurrence-matrix.json')
check('seven contextual rows',len(routes['seven_context_rows'])==7)
for a,b in zip(matrix['rows'],routes['seven_context_rows']):
    check('exact contextual row '+a['recipe_id'],a['occurrence']==b['original_occurrence_row'] and a['source_quantity_preserved']==b['exact_source_quantity'])
    capture(b['source_recipe_capture'])
    check('no new source membership '+a['recipe_id'],not b['assigned_W10_case_added'] and not b['assigned_W10_occurrence_added'] and not b['global_generic_label_or_provider_mapping'])
check('exact three supported dry and four held prepared routes',sum(r['route_supported'] for r in routes['seven_context_rows'])==3 and all(r['target_proposal_id'] is None for r in routes['seven_context_rows'] if not r['route_supported']))
dependency=routes['same_owner_dependency']
check('only genuine original case triggers',dependency['case_ids']==[new['decisions'][i]['case_id'] for i in [118,178]] and np[NEW]['case_ids']==dependency['case_ids'])
cross=load(S/'cross-worker-dependencies.json')
check('coordinator composition explicitly pending',not cross['combined_payload_authored_here'] and not cross['W10_payload_changed'] and not cross['W04_payload_changed'])
capture(cross['W04_origin']['payload_capture']);capture(cross['existing_coordinator_prototype'])
check('literal source300 variable',cross['source_routes'][0]['raw_quantity']=={'unit':'VARIABLE','value':'variable'})
check('literal source92139g',cross['source_routes'][1]['raw_quantity']=={'unit':'G_PER_L','value':'39'})
check('Oxoid unchanged authentic origin',np[OXOID]['after_capture']==op[OXOID]['after_capture'])
frozen=load(Q/'shards/shard-10.json')['cases'];frozen_bindings=[]
for i in [80,118,135,178]:
    f=frozen[i];d=new['decisions'][i]
    check('frozen case exact selected identity '+str(i),f['case_id']==d['case_id'])
    check('frozen case exact occurrence IDs '+str(i),[o['occurrence_id'] for o in f.get('occurrences',[])]==d['occurrence_ids'])
    for o in f.get('occurrences',[]):
        p=Q/o['full_recipe_snapshot'];check('full frozen recipe '+o['occurrence_id'],sha(p)==o['source_file_sha256'])
        frozen_bindings.append({'case_index':i,'occurrence_id':o['occurrence_id'],'recipe':bind(p),'raw_component':o['raw_component'],'source_component_path':o['component_path']})
sys.path.insert(0,str(R/'src'))
from mediaingredientmech.synonym_policy import is_resolving_synonym
generic=yaml.safe_load((S/'proposed'/f'{NEW}.yaml').read_text());difco=yaml.safe_load((S/'proposed'/f'{DIFCO}.yaml').read_text())
check('native generic RAW_TEXT remains resolving',is_resolving_synonym(generic['synonyms'][0]))
check('native both rejected vendorlabels do not resolve',all(not is_resolving_synonym(x) for x in generic['synonyms'][1:]))
check('native exact qualified Difco alias resolves on intended candidate',is_resolving_synonym(difco['synonyms'][0]))
result={'review_id':'W10-SV7-INDEPENDENT-CANDIDATE-BYTE-CHECK-V1','at':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':checks,'check_count':len(checks),'active_freeze':bind(S/'author-freeze-v3.json'),'core_bindings':{n:bind(S/'author-core-v3'/(n+'.json')) for n in old},'payload_matrix':payload_matrix,'four_case_diffs':[{'case_index':i,'case_id':new['decisions'][i]['case_id'],'before_object_sha256':objsha(old['decisions'][i]),'after_object_sha256':objsha(new['decisions'][i]),'diff':changes(old['decisions'][i],new['decisions'][i])} for i in [80,118,135,178]],'historical_enum_fix_verification':fix_changes,'frozen_source_occurrences':frozen_bindings,'new_findings':[],'scope_limit':'Mechanical exact-field, full-record retention and source binding. Scientific conclusions recorded separately; no full-corpus science or application/release approval.'}
p=O/'candidate-verification-v1.json';assert not p.exists();p.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'status':result['status'],'checks':len(checks),'report':bind(p)}))
