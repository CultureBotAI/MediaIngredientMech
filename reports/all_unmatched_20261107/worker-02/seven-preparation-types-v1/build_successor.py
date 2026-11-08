"""Seven filed category corrections; private candidates only, no owner writes.

Native writer + FrozenFile/exclusive publisher. Not a universal atomic transaction.
"""
from copy import deepcopy
from datetime import datetime, timezone
import argparse, hashlib, json, subprocess, sys
from pathlib import Path
W=Path(__file__).resolve().parents[4]; R=Path(__file__).resolve().parent; A=R.parent
OLD=A/'filed-followups-v1'; S=OLD/'selected-v3'; O=W/'.temp/w02-seven-preparation-types-v1'
sys.path.insert(0,str(W/'src'))
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import FrozenFile,no_alias
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
from mediaingredientmech.validation.write_validated import write_validated_ingredient
HEAD='f0d2be8b220d9e0c6ae415704d291ed40d3c292e'
MANIFEST_SHA='05522f23d0623bf6f0520c46d246e27f7e41206669a7343a2c4ef7a1815504db'
LEDGER_SHA='ec9cdf6354955276d4fbb98b9cb690743d47449ca5eb70c07a2b9e906fa73b93'
CID='CM_NAME:5d56ea306928dff3c50ac9c4131052b3c20acd05e613f9ada5e372418cc549d0'
CASE_INDEX=58
TARGET_IDS=('a2-proposal-jcm480-preaddition-basal-preparation','a2-proposal-jcm438-preaddition-basal-preparation','a2-proposal-togo-m491-preaddition-basal-preparation','a2-proposal-jcm537-preaddition-basal-preparation','a2-proposal-jcm573-preaddition-basal-preparation','a2-proposal-jcm706-preaddition-basal-preparation','a2-proposal-jcm525-mineral-yeast-basal-preparation')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def encode(v):return (json.dumps(v,indent=2,ensure_ascii=False)+'\n').encode()
def require_pin(content,expected):
 if hashlib.sha256(content).hexdigest()!=expected:raise ValueError('Frozen input bytes changed')
def unique(rows,key):
 result={}
 for row in rows:
  if row[key] in result:raise ValueError('Duplicate target')
  result[row[key]]=row
 return result
def require_output(out,root=R):
 if '..' in out.parts:raise ValueError('Parent traversal')
 out=out.absolute();root=root.absolute();no_alias(root);no_alias(out)
 if out!=out.resolve() or root!=root.resolve() or not out.is_relative_to(root):raise ValueError('Output outside private packet')
 if out.exists():raise FileExistsError(out)
 return out
def history_message(pid):
 if pid not in TARGET_IDS:raise ValueError('Unassigned preparation')
 return ('Under filed #1241 comment6719690144 / W01-W02-PREP-TYPE-001, change solution_type from MINERAL_STOCK to OTHER for '+pid+'. The cited source defines a separately prepared nutrient basal material. Preserve every other field, source-specific preparation partition, literal quantities and added-water scope, unresolved components, prior history and all source/owner/release holds. This category correction does not approve component identity, complete formulation, roles or export.')
def validate_payload_delta(old,new,pid):
 if pid not in TARGET_IDS:raise ValueError('Unassigned preparation')
 if set(old)!=set(new) or any(old[k]!=new[k] for k in old if k not in {'solution_type','curation_history'}):raise ValueError('Unrequested payload field changed')
 if old['solution_type']!='MINERAL_STOCK' or new['solution_type']!='OTHER':raise ValueError('Wrong category delta')
 h=old['curation_history'];n=new['curation_history']
 if len(n)!=len(h)+1 or n[:-1]!=h:raise ValueError('Original history altered or wrong event count')
 e=n[-1]
 if set(e)!={'timestamp','curator','action','changes','llm_assisted'} or e['curator']!='worker02 /root' or e['action']!='CORRECTED' or e['llm_assisted'] is not True or e['changes']!=history_message(pid):raise ValueError('Untruthful or unscoped history')
 if datetime.fromisoformat(e['timestamp']).utcoffset() is None:raise ValueError('Timezone absent')
def correct_payload(old,row):
 pid=row['proposal_id']
 if pid not in TARGET_IDS or old['solution_type']!='MINERAL_STOCK' or old['identifier']!='kgmicrobe.ingredient:'+Path(row['owner_path']).stem:raise ValueError('Wrong preparation preimage')
 if len(old['curation_history'])!=row['history_length'] or digest(old['curation_history'])!=row['history_sha256']:raise ValueError('Wrong historical preimage')
 new=deepcopy(old);new['solution_type']='OTHER'
 record_curation_event(new,curator='worker02 /root',action='CORRECTED',changes=history_message(pid),llm_assisted=True)
 validate_payload_delta(old,new,pid);return new
def pending_case(old):
 if old['case_id']!=CID or len(old['occurrence_ids'])!=24:raise ValueError('Wrong complete case58')
 new=deepcopy(old);new['independent_review']={'status':'pending','evidence_ids':[]};return new
def validate_case_delta(old,new,index):
 if index==CASE_INDEX:
  if new!=pending_case(old):raise ValueError('Unrequested case/source/hold field changed')
 elif new!=old:raise ValueError('Unassigned case changed')
def raw_array_objects(raw,key):
 text=raw.decode();pos=text.index('[',text.index(json.dumps(key)+':'))+1;decoder=json.JSONDecoder();rows=[]
 while True:
  while text[pos].isspace() or text[pos]==',':pos+=1
  if text[pos]==']':break
  end=decoder.raw_decode(text,pos)[1];rows.append(text[pos:end].encode());pos=end
 return rows
def validate_proposal_delta(before,after,new_captures):
 if len(before)!=117 or len(after)!=117:raise ValueError('Wrong proposal denominator')
 if list(unique(before,'proposal_id'))!=list(unique(after,'proposal_id')):raise ValueError('Changed proposal IDs/order')
 if set(new_captures)!=set(TARGET_IDS):raise ValueError('Wrong target set including possible boundary sweep')
 for old,new in zip(before,after,strict=True):
  expected=deepcopy(old)
  if old['proposal_id'] in new_captures:expected['after_capture']=new_captures[old['proposal_id']]
  if new!=expected:raise ValueError('Unrequested proposal metadata changed')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();out=require_output(args.out)
 if subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip()!=HEAD:raise ValueError('Wrong publication parent')
 mf=FrozenFile.capture(OLD/'MANIFEST.json');require_pin(mf.content,MANIFEST_SHA)
 pins={x['path']:x['sha256'] for x in json.loads(mf.content)['members']}
 held=[FrozenFile.capture(S/(n+'.json')) for n in ['decisions','proposals','evidence']]
 for n,f in zip(['decisions','proposals','evidence'],held,strict=True):require_pin(f.content,pins['selected-v3/'+n+'.json'])
 ds,ps,es=[json.loads(f.content) for f in held];before_ds=deepcopy(ds);before_ps=deepcopy(ps);held.append(mf)
 if len(unique(ds['decisions'],'case_id'))!=188 or len(unique(ps['proposals'],'proposal_id'))!=117:raise ValueError('Wrong frozen denominator')
 lf=FrozenFile.capture(R/'context/hash-ledger.json');require_pin(lf.content,LEDGER_SHA);ledger=json.loads(lf.content);held.append(lf)
 rows=unique(ledger['rows'],'proposal_id')
 if tuple(rows)!=TARGET_IDS:raise ValueError('Unexpected confirmed target scope')
 cf=FrozenFile.capture(R/'context/issue1241-comment6719690144.json');comment=json.loads(cf.content);held.append(cf)
 if comment['id']!=6719690144 or comment['html_url']!='https://github.com/CultureBotAI/MediaIngredientMech/issues/1241#issuecomment-6719690144':raise ValueError('Wrong filed comment')
 add=FrozenFile.capture(R/'context/issue1241-addendum.md');held.append(add)
 if comment['body'].rstrip()!=add.content.decode().rstrip():raise ValueError('Filed addendum body differs')
 proposals=unique(ps['proposals'],'proposal_id');payloads={};old_payloads={};caps={};writes=[]
 for p in ps['proposals']:
  cap=p['after_capture'];rel=Path(cap['path'])
  if cap['root']!='artifact' or rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe payload path')
  f=FrozenFile.capture(A/rel);held.append(f);require_pin(f.content,cap['sha256']);payloads[p['proposal_id']]=f
 for pid,row in rows.items():
  p=proposals[pid];f=payloads[pid]
  if p['owner_path']!=row['owner_path'] or p['kind']!=row['kind'] or p['before_sha256']!=row['before_sha256'] or p['case_ids']!=[CID]:raise ValueError('Changed target identity/scope')
  require_pin(f.content,row['payload']['sha256'])
  if str(f.path)!=row['payload']['path']:raise ValueError('Changed selected path')
  if row['case_input_sha256']!=ds['decisions'][CASE_INDEX]['case_input_sha256']:raise ValueError('Changed frozen case binding')
  for entry in [row['source'],*row['frozen_recipe_captures']]:
   frozen=FrozenFile.capture(Path(entry['path']));held.append(frozen);require_pin(frozen.content,entry['sha256'])
  if len(row['selected_occurrences'])!=1 or row['selected_occurrences'][0]['occurrence_id'] not in ds['decisions'][CASE_INDEX]['occurrence_ids']:raise ValueError('Wrong source occurrence')
  old=yaml.safe_load(f.content);new=correct_payload(old,row);old_payloads[pid]=old
  stage=O/'stage'/out.name/(pid+'.yaml');require_output(stage,O);stage.parent.mkdir(parents=True,exist_ok=True)
  write_validated_ingredient(new,stage)
  if yaml.safe_load(stage.read_text())!=new:raise ValueError('Native roundtrip changed payload')
  target=out/'after'/(pid+'.yaml');caps[pid]={'root':'artifact','path':str(target.relative_to(A)),'sha256':sha(stage)}
  p['after_capture']=caps[pid];writes.append((target,stage.read_bytes()))
 ds['decisions'][CASE_INDEX]=pending_case(ds['decisions'][CASE_INDEX])
 for i,(old,new) in enumerate(zip(before_ds['decisions'],ds['decisions'],strict=True)):validate_case_delta(old,new,i)
 validate_proposal_delta(before_ps['proposals'],ps['proposals'],caps)
 raw_d_before=raw_array_objects(held[0].content,'decisions');raw_d_after=raw_array_objects(encode(ds),'decisions')
 raw_p_before=raw_array_objects(held[1].content,'proposals');raw_p_after=raw_array_objects(encode(ps),'proposals')
 assert all(x==y for i,(x,y) in enumerate(zip(raw_d_before,raw_d_after,strict=True)) if i!=CASE_INDEX)
 assert all(x==y for p,x,y in zip(ps['proposals'],raw_p_before,raw_p_after,strict=True) if p['proposal_id'] not in rows)
 receipt={'created_at':datetime.now(timezone.utc).isoformat(),'author':'worker02 /root','parent_head':HEAD,'case_count':188,'occurrence_count':sum(len(d['occurrence_ids']) for d in ds['decisions']),'proposal_count':117,'complete_case58_occurrences':24,'changed_preparations':7,'category_affected_occurrences':7,'unchanged_complete_payloads':110,'unchanged_complete_case_objects':187,'all188case_scientific_fields_unchanged':True,'payload_only_changes':['/solution_type','/curation_history/-'],'case_only_changes':['case58/independent_review'],'dsmz40_included_in_correction':False,'case_rows':[{'case_id':d['case_id'],'old_canonical_sha256':digest(old),'new_canonical_sha256':digest(d),'raw_object_bytes_unchanged':x==y,'source_and_occurrence_ids_unchanged':all(old[k]==d[k] for k in ['case_id','case_input_sha256','source','occurrence_ids'])} for d,old,x,y in zip(ds['decisions'],before_ds['decisions'],raw_d_before,raw_d_after,strict=True)],'proposal_rows':[{'proposal_id':p['proposal_id'],'old_object_sha256':digest(old),'new_object_sha256':digest(p),'old_after_capture':old['after_capture'],'after_capture':p['after_capture'],'raw_object_bytes_unchanged':x==y,'complete_payload_unchanged':old['after_capture']==p['after_capture']} for p,old,x,y in zip(ps['proposals'],before_ps['proposals'],raw_p_before,raw_p_after,strict=True)],'changed_payloads':[{'proposal_id':pid,'before_capture':proposals[pid]['after_capture'] if False else next(p['after_capture'] for p in before_ps['proposals'] if p['proposal_id']==pid),'after_capture':caps[pid],'old_history_length':len(old_payloads[pid]['curation_history']),'old_history_sha256':digest(old_payloads[pid]['curation_history']),'all_other_fields_unchanged':True,'source':rows[pid]['source'],'primary_retrieval_records':rows[pid]['primary_retrieval_records']} for pid in TARGET_IDS],'limits':'Only seven filed category changes; prior source/owner/quantity/preparation/export holds retained. Full scientific review and final native case binding still required. Publisher is bounded exclusive publication, not universal atomicity.'}
 rp=out/'author-preservation-receipt.json';rr=encode(receipt)
 es['evidence'].extend([{'evidence_id':'w02-seven-preparations-filed-comment6719690144','kind':'source_snapshot','capture':{'root':'artifact','path':str(cf.path.relative_to(A)),'sha256':hashlib.sha256(cf.content).hexdigest()},'url':None,'locator':'Filed coordinator addendum '+comment['html_url']+'; actual read times in context/comment-read-receipt.json','supports_or_contradicts':'Administrative exact seven-target authorization; no new primary chemistry or owner approval.'},{'evidence_id':'w02-seven-preparations-author-preservation-v1','kind':'local_validation','capture':{'root':'artifact','path':str(rp.relative_to(A)),'sha256':hashlib.sha256(rr).hexdigest()},'url':None,'locator':'Complete188case/117proposal accounting, exact110payload inheritance and seven bounded deltas','supports_or_contradicts':'Mechanical category/history preservation; independent scientific review remains separate.'}])
 old_e_raw=raw_array_objects(held[2].content,'evidence');new_e_raw=raw_array_objects(encode(es),'evidence');assert new_e_raw[:len(old_e_raw)]==old_e_raw
 out.mkdir();(out/'after').mkdir()
 def verify():
  for f in held:f.verify()
 publish_new_files(writes+[(out/'decisions.json',encode(ds)),(out/'proposals.json',encode(ps)),(out/'evidence.json',encode(es)),(rp,rr)],verify);verify()
 print(json.dumps({'cases':188,'proposals':117,'changed_payloads':7,'untouched_payloads':110,'whole_case58_occurrences':24,'new_hashes':caps},indent=2))
if __name__=='__main__':main()
