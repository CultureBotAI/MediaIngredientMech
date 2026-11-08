"""W08-PF-PROCESS-001: deterministic native-helper replay, not a new curation.

Rebuild the original scientific transition from aa8390… using the exact published
mutator literals, then construct its historical sixth event through the native
helper. The published script/payload and active selector are read-only inputs.
No live ontology search or fresh scientific review is claimed by this replay.
"""
import argparse,ast,copy,datetime,hashlib,json,sys
from pathlib import Path
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient

ROOT=Path.cwd();PUBLIC=ROOT/'reports/all_unmatched_20261107/worker-08/process-replays/plain-flour-v1';PRIVATE=ROOT/'.temp/all-unmatched-worker-08/plain-flour-process-replay-v1'
PREDECESSOR_SHA='aa8390f17f1ed9f9c083fd6b487ee1c40228e754072b7e390b97dfb2fd6eae83'
SELECTED_SHA='884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873'
SCRIPT_SHA='1790bb6525e047fde7158a4f84ab9a623de43ba8b4a85aa96fc09b5244d8b0c0'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(path,value):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
def differences(a,b,path=''):
 if type(a)!=type(b):return [{'path':path,'expected':a,'actual':b}]
 if isinstance(a,dict):
  rows=[]
  for k in a.keys()|b.keys():
   if k not in a or k not in b:rows.append({'path':path+'/'+k,'expected':a.get(k),'actual':b.get(k),'missing_key':True})
   else:rows+=differences(a[k],b[k],path+'/'+k)
  return rows
 if isinstance(a,list):
  if len(a)!=len(b):return [{'path':path,'expected_length':len(a),'actual_length':len(b)}]
  return [d for i,(x,y) in enumerate(zip(a,b)) for d in differences(x,y,path+'/'+str(i))]
 return [] if a==b else [{'path':path,'expected':a,'actual':b}]

def inputs(predecessor_path=None):
 oldpath=Path(predecessor_path) if predecessor_path else PUBLIC/'inputs/predecessor.yaml'
 assert sha(oldpath)==PREDECESSOR_SHA,'wrong predecessor: replay must start from exact five-event aa8390 payload'
 script=PUBLIC/'inputs/original-author.py';selected=PUBLIC/'inputs/selected-payload.yaml'
 assert sha(script)==SCRIPT_SHA and sha(selected)==SELECTED_SHA
 before=yaml.safe_load(oldpath.read_text());expected=yaml.safe_load(selected.read_text())
 assert before['identifier']=='FOODON:00004510' and len(before['curation_history'])==5
 assert len(expected['curation_history'])==6 and expected['curation_history'][:-1]==before['curation_history']
 tree=ast.parse(script.read_text());literals={}
 for node in tree.body:
  if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ['scope','lexical']:
   literals[node.targets[0].id]=ast.literal_eval(node.value)
 matches=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='append' and isinstance(n.func.value,ast.Subscript) and isinstance(n.func.value.slice,ast.Constant) and n.func.value.slice.value=='curation_history']
 assert len(matches)==1 and len(matches[0].args)==1 and isinstance(matches[0].args[0],ast.Dict)
 event={}
 for k,v in zip(matches[0].args[0].keys,matches[0].args[0].values):
  key=ast.literal_eval(k)
  if isinstance(v,ast.Name):assert v.id=='NOW' and key=='timestamp';event[key]=expected['curation_history'][-1]['timestamp']
  else:event[key]=ast.literal_eval(v)
 assert event==expected['curation_history'][-1] and event['llm_assisted'] is True
 return before,expected,literals,event

def reconstruct(before,literals,event):
 """Replay the four scientific mutations; native helper appends the sole event."""
 rec=copy.deepcopy(before);scope=literals['scope'];lexical=literals['lexical']
 rec['preferred_term']='flour'
 rec['notes']+='\n\nW08-FINAL-001 correction: '+scope+' '+lexical+' The original Plain flour RAW_TEXT synonym and stable owner filename remain unchanged.'
 rec['ontology_mapping']['evidence'][0]['notes']=lexical
 rec['ontology_mapping']['evidence'].append({'evidence_type':'LLM_SUGGESTION','source':'https://bacmedia.dsmz.de/ingredients/1465','notes':scope+' Source facts use the original capture from2026-11-08T05:16:12.135246+00:00; no new remote source retrieval is claimed.'})
 record_curation_event(rec,curator=event['curator'],action=event['action'],changes=event['changes'],previous_status=event['previous_status'],new_status=event['new_status'],llm_assisted=True,llm_model=event['llm_model'],timestamp=event['timestamp'])
 return rec

def require_equivalent(rec,expected,before):
 delta=differences(expected,rec)
 assert not delta,json.dumps({'complete_payload_differences':delta},ensure_ascii=False)
 assert rec['curation_history'][:-1]==before['curation_history'] and len(rec['curation_history'])==len(before['curation_history'])+1
 assert rec['curation_history'][-1]==expected['curation_history'][-1]

def replay(output_dir,executor='worker08:/root',predecessor_path=None):
 output_dir=Path(output_dir).absolute()
 assert output_dir.is_relative_to(PRIVATE) or output_dir==PUBLIC/'replay','output restricted to new task-private fixtures or designated report replay'
 assert not output_dir.exists(),'immutable replay output already exists'
 before,expected,literals,event=inputs(predecessor_path)
 output_dir.mkdir(parents=True,exist_ok=False)
 calls=[];helpercode=record_curation_event.__code__;writercode=write_validated_ingredient.__code__
 assert Path(helpercode.co_filename).resolve()==ROOT/'src/mediaingredientmech/curate/curation_event.py'
 assert Path(writercode.co_filename).resolve()==ROOT/'src/mediaingredientmech/validation/write_validated.py'
 def trace(frame,what,arg):
  if what=='call' and frame.f_code in [helpercode,writercode]:
   local=frame.f_locals
   row={'function':frame.f_code.co_name,'source_file':frame.f_code.co_filename,'line':frame.f_code.co_firstlineno,'caller_file':frame.f_back.f_code.co_filename,'caller_line':frame.f_back.f_lineno,'history_length_before_call':len(local['record']['curation_history'])}
   if frame.f_code==helpercode:row['kwargs']={k:copy.deepcopy(local[k]) for k in ['curator','action','changes','previous_status','new_status','llm_assisted','llm_model','timestamp','skip_if_recent']}
   else:row['output_path']=str(local['path'])
   calls.append(row)
 oldprof=sys.getprofile();sys.setprofile(trace)
 try:
  rec=reconstruct(before,literals,event);require_equivalent(rec,expected,before)
  dest=output_dir/'Plain_Flour.yaml';assert not dest.exists();write_validated_ingredient(rec,dest)
 finally:sys.setprofile(oldprof)
 assert yaml.safe_load(dest.read_text())==expected
 assert sha(dest)==SELECTED_SHA,'complete parsed payload equal but serialized bytes differ; do not select changed bytes'
 assert [c['function'] for c in calls]==['record_curation_event','write_validated_ingredient']
 assert calls[0]['history_length_before_call']==5 and calls[1]['history_length_before_call']==6
 receipt={'status':'PASS','replayed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'executor':executor,'finding_id':'W08-PF-PROCESS-001','meaning':'New execution of a historical transition, not a new scientific judgment or a second event appended to the selected record.','predecessor_sha256':PREDECESSOR_SHA,'original_author_sha256':SCRIPT_SHA,'selected_payload_sha256':SELECTED_SHA,'replay_payload_sha256':sha(dest),'complete_payload_object_equal':rec==expected,'complete_payload_bytes_equal':dest.read_bytes()==(PUBLIC/'inputs/selected-payload.yaml').read_bytes(),'complete_final_event_equal':rec['curation_history'][-1]==event,'full_history_equal':rec['curation_history']==expected['curation_history'],'original_history_events':len(before['curation_history']),'replay_history_events':len(rec['curation_history']),'selected_record_events_added':0,'historical_event':event,'actual_calls':calls,'payload_differences':differences(expected,rec),'native_helper_sha256':sha(ROOT/'src/mediaingredientmech/curate/curation_event.py'),'native_writer_sha256':sha(ROOT/'src/mediaingredientmech/validation/write_validated.py'),'replay_script_sha256':sha(Path(__file__)),'scientific_review':False,'source_case_additions':0,'selector_changed':False,'maintained_writes':False,'role_export_approval':False}
 save(output_dir/'receipt.json',receipt)
 return receipt

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=PUBLIC/'replay');parser.add_argument('--executor',default='worker08:/root');args=parser.parse_args()
 result=replay(args.output_dir,args.executor);print(json.dumps({k:result[k] for k in ['status','predecessor_sha256','replay_payload_sha256','complete_final_event_equal','complete_payload_bytes_equal','selected_record_events_added']},indent=2))
