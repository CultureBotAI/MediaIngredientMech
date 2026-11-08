"""Bounded report-only corrections for the two filed #1241 followups.

Uses native validated writes and exclusive publication. No maintained owner write.
The multi-file publisher is bounded/exclusive, not a fully atomic transaction.
"""
from copy import deepcopy
from datetime import datetime,timezone
import argparse,hashlib,json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[4];R=Path(__file__).resolve().parent;A=R.parent
OLD=A/'final-corrections-v1';S=OLD/'review-bound-v1';O=W/'.temp/w02-filed-followups-v1'
sys.path.insert(0,str(W/'src'))
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import FrozenFile,no_alias
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
from mediaingredientmech.validation.write_validated import write_validated_ingredient
PID='b2-proposal-sodium_resazurin_01_percent_wv_jcm363_1023'
ACID='b2-proposal-sulfuric_acid_10n_named_sources'
MANIFEST_SHA='5fbab1d12661a09e4f91ca063983e140326219ad52c14f514969a578787f8daa'
OLD_SHA='8c43d59c4d4adcd07300804b29b219c2197328630bb6077adcc4fd95f8b3062d'
ACID_SHA='95aca3c8092ca7430df24c8cbdaa65151b36d5cb15346abb86f7d7cb7d934ee1'
AFFECTED=(88,93,114,118)
IDS={88:'CM_NAME:9e73eaf786d4833fb53a84a62e9594e4244b95f5a6a8af642f771969ce564ba0',93:'CM_NAME:a9bdbb9f988695e32b7abedbd6a479e802564b2d0b045935af5f9ff166cf004b',114:'CM_NAME:d951d3a06dbf1687dcd7ad4b09cf6eaff094051a7ec99faad346cb175a61b703',118:'CM_NAME:e487376ddf68008986b13e55fced4761f2f5003a4f0d5b0d12c05e3549a18cdb'}
TAIL='Normality is source-stated and does not require a guessed solvent or conversion to molarity. A source-supported isolated stock proposal now replaces the previous unperformed-curation deferral.'
NARRATIVES={114:'The six occurrences in case 114 explicitly prescribe 10 N H2SO4 for source-specific pH adjustment or preparation. This case covers M2680, M2734, M377, M84 and M2668 plus the JCM382-derived occurrence. Together with the one occurrence in case 118 (Kim/M3239), the unchanged shared proposal covers seven occurrences. '+TAIL,118:'The one occurrence in case 118 (Kim/M3239) explicitly prescribes 10 N H2SO4 for source-specific pH adjustment or preparation. Together with the six occurrences in case 114, the unchanged shared proposal covers seven occurrences. '+TAIL}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def encode(v):return (json.dumps(v,indent=2,ensure_ascii=False)+'\n').encode()
def require_output(out,root=R):
 if '..' in out.parts:raise ValueError('Parent traversal')
 out=out.absolute();root=root.absolute();no_alias(root);no_alias(out)
 if out!=out.resolve() or root!=root.resolve() or not out.is_relative_to(root):raise ValueError('Output outside private report packet')
 if out.exists():raise FileExistsError(out)
 return out
def correct_case(old,index):
 if index not in AFFECTED or old['case_id']!=IDS[index]:raise ValueError('Wrong source case')
 new=deepcopy(old)
 if index in NARRATIVES:
  if len(old['occurrence_ids'])!={114:6,118:1}[index] or old['reasoning'] not in old['applicability'] or not old['reasoning'].startswith('All seven occurrences explicitly prescribe10NH2SO4'):raise ValueError('Unexpected scope preimage')
  new['reasoning']=NARRATIVES[index];new['applicability']=old['applicability'].replace(old['reasoning'],new['reasoning'])
 new['independent_review']={'status':'pending','evidence_ids':[]}
 return new
def validate_case_delta(old,new,index):
 allowed={'independent_review'}|({'reasoning','applicability'} if index in NARRATIVES else set())
 if set(old)!=set(new) or any(old[k]!=new[k] for k in old if k not in allowed):raise ValueError('Unauthorised source/case field delta')
 if index in AFFECTED:
  expected=correct_case(old,index)
  if new!=expected:raise ValueError('Unexpected case narrative or review delta')
 elif old!=new:raise ValueError('Unassigned case changed')
def correct_payload(old):
 if old['identifier']!='kgmicrobe.ingredient:sodium_resazurin_01_percent_wv_jcm363_1023' or old['solution_type']!='MINERAL_STOCK':raise ValueError('Wrong stock preimage')
 if old['components']!=[{'component_name':'Resazurin sodium salt','reference_scope':'UNMAPPED','concentration_value':'0.1','concentration_unit':'PERCENT_W_V'}] or old['component_assertion']['completeness']!='UNKNOWN':raise ValueError('Unexpected chemistry or closure preimage')
 new=deepcopy(old);new['solution_type']='OTHER'
 record_curation_event(new,curator='worker02 /root',action='CORRECTED',changes='Under filed #1241 comment6719443273 / W02-FC-D-SODIUM-RESAZURIN-TYPE, change solution_type from MINERAL_STOCK to OTHER for the named 0.1% w/v sodium-resazurin indicator preparation. Preserve the complete solute/component description, UNMAPPED reference, 0.1 PERCENT_W_V, UNKNOWN closure, all source evidence, prior history and owner/release holds. No chemistry, quantity, identity, role or release approval is implied.',llm_assisted=True)
 validate_payload_delta(old,new);return new
def validate_payload_delta(old,new):
 if set(old)!=set(new) or any(old[k]!=new[k] for k in old if k not in {'solution_type','curation_history'}):raise ValueError('Chemistry or other payload field changed')
 if old['solution_type']!='MINERAL_STOCK' or new['solution_type']!='OTHER':raise ValueError('Wrong category delta')
 history=old['curation_history'];updated=new['curation_history']
 if updated[:-1]!=history or len(updated)!=len(history)+1:raise ValueError('Old history changed or extra history')
 event=updated[-1]
 if set(event)!={'timestamp','curator','action','changes','llm_assisted'} or event['curator']!='worker02 /root' or event['action']!='CORRECTED' or event['llm_assisted'] is not True or 'W02-FC-D-SODIUM-RESAZURIN-TYPE' not in event['changes']:raise ValueError('Untruthful or unrelated history')
 if datetime.fromisoformat(event['timestamp']).utcoffset() is None:raise ValueError('History timestamp has no zone')
def raw_array_objects(raw,key):
 text=raw.decode();start=text.index('[',text.index(json.dumps(key)+':'));pos=start+1;decoder=json.JSONDecoder();rows=[]
 while True:
  while text[pos].isspace() or text[pos]==',':pos+=1
  if text[pos]==']':break
  end=decoder.raw_decode(text,pos)[1];rows.append(text[pos:end].encode());pos=end
 return rows
def require_pin(content,expected):
 if hashlib.sha256(content).hexdigest()!=expected:raise ValueError('Frozen predecessor bytes changed')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();out=require_output(args.out)
 held=[FrozenFile.capture(S/(n+'.json')) for n in ['decisions','proposals','evidence']]
 manifest=FrozenFile.capture(OLD/'MANIFEST.json');require_pin(manifest.content,MANIFEST_SHA)
 expected={x['path']:x['sha256'] for x in json.loads(manifest.content)['members']}
 for name,frozen in zip(['decisions','proposals','evidence'],held,strict=True):require_pin(frozen.content,expected['review-bound-v1/'+name+'.json'])
 ds,ps,es=[json.loads(x.content) for x in held];held.append(manifest);old_ds=deepcopy(ds);old_ps=deepcopy(ps)
 if len(ds['decisions'])!=188 or len(ps['proposals'])!=117:raise ValueError('Wrong frozen denominator')
 if len({d['case_id'] for d in ds['decisions']})!=188 or len({p['proposal_id'] for p in ps['proposals']})!=117:raise ValueError('Duplicate source target')
 comment_path=R/'context/issue1241-comment6719443273.json';cf=FrozenFile.capture(comment_path);held.append(cf);comment=json.loads(cf.content)
 if comment['id']!=6719443273 or comment['html_url']!='https://github.com/CultureBotAI/MediaIngredientMech/issues/1241#issuecomment-6719443273' or OLD_SHA not in comment['body']:raise ValueError('Wrong filed prerequisite')
 payloads={};sources={}
 for p in ps['proposals']:
  f=FrozenFile.capture(A/p['after_capture']['path']);held.append(f)
  if hashlib.sha256(f.content).hexdigest()!=p['after_capture']['sha256']:raise ValueError('Stale selected payload')
  payloads[p['proposal_id']]=p;sources[p['proposal_id']]=f
 if payloads[PID]['after_capture']['sha256']!=OLD_SHA or payloads[ACID]['after_capture']['sha256']!=ACID_SHA:raise ValueError('Wrong selected stock preimage')
 if set(payloads[ACID]['case_ids'])!={IDS[114],IDS[118]}:raise ValueError('Wrong shared stock scope')
 for i in AFFECTED:ds['decisions'][i]=correct_case(ds['decisions'][i],i)
 for i,(old,new) in enumerate(zip(old_ds['decisions'],ds['decisions'],strict=True)):validate_case_delta(old,new,i)
 old_payload=yaml.safe_load(sources[PID].content);new_payload=correct_payload(old_payload)
 stage=O/'stage'/out.name/(PID+'.yaml');stage.parent.mkdir(parents=True,exist_ok=True)
 if stage.exists():raise FileExistsError(stage)
 write_validated_ingredient(new_payload,stage);assert yaml.safe_load(stage.read_text())==new_payload
 target=out/'after'/(PID+'.yaml');cap={'root':'artifact','path':str(target.relative_to(A)),'sha256':sha(stage)};payloads[PID]['after_capture']=cap
 for before,after in zip(old_ps['proposals'],ps['proposals'],strict=True):
  permitted=deepcopy(before)
  if before['proposal_id']==PID:permitted['after_capture']=cap
  if after!=permitted:raise ValueError('Unrelated proposal metadata changed')
 raw_before=raw_array_objects(held[0].content,'decisions');raw_after=raw_array_objects(encode(ds),'decisions')
 assert all(raw_before[i]==raw_after[i] for i in range(188) if i not in AFFECTED)
 raw_p_before=raw_array_objects(held[1].content,'proposals');raw_p_after=raw_array_objects(encode(ps),'proposals')
 assert all(a==b for a,b,p in zip(raw_p_before,raw_p_after,ps['proposals'],strict=True) if p['proposal_id']!=PID)
 receipt={'created_at':datetime.now(timezone.utc).isoformat(),'author':'worker02 /root','parent_head':'5a32a86e124b657df4cf340592a6bdc8b2a61374','filed_comment':{'path':str(comment_path.relative_to(W)),'sha256':sha(comment_path),'url':comment['html_url']},'old_candidate':old_ps['proposals'][list(payloads).index(PID)]['after_capture'],'new_candidate':cap,'payload_only_changes':['/solution_type','/curation_history/-'],'old_history_preserved':True,'unchanged_complete_payloads':116,'shared_acid_payload_sha256':ACID_SHA,'case_rows':[{'case_index':i,'case_id':d['case_id'],'old_sha256':digest(old_ds['decisions'][i]),'new_sha256':digest(d),'changed_fields':[k for k in d if d[k]!=old_ds['decisions'][i][k]],'frozen_source_fields_unchanged':all(d[k]==old_ds['decisions'][i][k] for k in ['case_id','case_input_sha256','source','occurrence_ids']),'raw_object_bytes_unchanged':raw_before[i]==raw_after[i]} for i,d in enumerate(ds['decisions'])],'proposal_rows':[{'proposal_id':p['proposal_id'],'old_object_sha256':digest(before),'new_object_sha256':digest(p),'after_capture':p['after_capture'],'raw_object_bytes_unchanged':x==y} for p,before,x,y in zip(ps['proposals'],old_ps['proposals'],raw_p_before,raw_p_after,strict=True)],'case_count':188,'occurrence_count':sum(len(x['occurrence_ids']) for x in ds['decisions']),'proposal_count':117,'unchanged_full_case_objects':184,'unchanged_case_science_except_two_narratives':186,'independent_review_status':'pending_exact_bytes','limits':'No chemistry/quantity/identity/source/owner/role/release change. Prior reviews/holds remain immutable. Multi-file publication is exclusive but not fully transactional; only a completed validated/reviewed selection is usable.'}
 receipt_raw=encode(receipt);receipt_path=out/'author-preservation-receipt.json'
 extra=[{'evidence_id':'w02-followups-filed-comment6719443273','kind':'source_snapshot','capture':{'root':'artifact','path':str(comment_path.relative_to(A)),'sha256':sha(comment_path)},'url':None,'locator':'Complete coordinator issue comment '+comment['html_url']+'; captured by actual gh api read in this turn, with no HTTP access timestamp inferred from filesystem metadata','supports_or_contradicts':'Administrative scope/filing receipt; no primary chemistry or owner approval.'},{'evidence_id':'w02-followups-author-preservation-v1','kind':'local_validation','capture':{'root':'artifact','path':str(receipt_path.relative_to(A)),'sha256':hashlib.sha256(receipt_raw).hexdigest()},'url':None,'locator':'Exact field deltas,188case/117proposal preservation and shared acid bytes','supports_or_contradicts':'Mechanical scope proof only; actual independent review is required.'}]
 es['evidence'].extend(extra)
 out.mkdir();(out/'after').mkdir()
 def verify():
  for f in held:f.verify()
 publish_new_files([(target,stage.read_bytes()),(out/'decisions.json',encode(ds)),(out/'proposals.json',encode(ps)),(out/'evidence.json',encode(es)),(receipt_path,receipt_raw)],verify);verify()
 print(json.dumps({'cases':188,'proposals':117,'changed_payloads':1,'changed_narratives':2,'review_pending_cases':4,'new_payload_sha256':cap['sha256']}))
if __name__=='__main__':main()
