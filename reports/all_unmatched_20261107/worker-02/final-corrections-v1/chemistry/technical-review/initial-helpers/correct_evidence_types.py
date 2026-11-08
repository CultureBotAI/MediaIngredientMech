"""Apply a reviewed, claim-specific type plan to isolated full candidates only.

No enumeration scanning or global replacement. Each edit binds a full exact
MappingEvidence value and authentic baseline exclusion, after scientific edits.
"""
from copy import deepcopy
from datetime import datetime,timezone
import argparse,hashlib,json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[4];R=Path(__file__).resolve().parent;A=R.parent
sys.path.insert(0,str(W/'src'))
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import FrozenFile,no_alias
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
from mediaingredientmech.validation.write_validated import write_validated_ingredient
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def load(p):return json.loads(p.read_text())
def require_complete_flags(dispositions):
 flags=[i for row in dispositions for i in row['original_flag_indices']]
 if sorted(flags)!=list(range(58)) or len(flags)!=58:raise ValueError('Missing or duplicate original flagged entry')
 return flags
def apply_exact_edits(record,baseline,edits):
 result=deepcopy(record);seen=set();proof=[]
 for edit in edits:
  idx=edit['evidence_index']
  if not isinstance(idx,int) or isinstance(idx,bool) or idx<0 or idx in seen:raise ValueError('Duplicate or invalid mapping-evidence index')
  seen.add(idx)
  actual=result['ontology_mapping']['evidence'][idx]
  if actual!=edit['expected_complete_entry']:raise ValueError('Complete evidence object changed')
  if actual in (baseline or {}).get('ontology_mapping',{}).get('evidence',[]):raise ValueError('Historical unchanged evidence cannot be retyped')
  if actual['evidence_type']!='MANUAL_CURATION':raise ValueError('Expected newly agent-authored manual enum')
  if edit['new_type']!='LLM_SUGGESTION' or edit['classification']!='new_agent_record':raise ValueError('Unjustified provenance type/classification')
  if not edit.get('basis') or not edit.get('original_flag_indices'):raise ValueError('Missing claim-specific audit provenance')
  before=deepcopy(actual);actual['evidence_type']=edit['new_type'];proof.append({'evidence_index':idx,'before':before,'after':deepcopy(actual),'basis':edit['basis'],'original_flag_indices':edit['original_flag_indices']})
 return result,proof
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--selection',type=Path,required=True);ap.add_argument('--plan',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
 output=args.out.absolute();no_alias(output)
 if not output.is_relative_to(R):raise ValueError('Output outside new report packet')
 output.mkdir(parents=True,exist_ok=False)
 path=args.selection/'proposals.json';held=[FrozenFile.capture(path),FrozenFile.capture(args.plan)]
 document=load(path);proposals={p['proposal_id']:deepcopy(p) for p in document['proposals']};plan=load(args.plan)
 flags=require_complete_flags(plan['original_flag_dispositions'])
 changes=[];outputs=[]
 for row in plan['candidate_edits']:
  p=proposals[row['proposal_id']];source=A/p['after_capture']['path'];frozen=FrozenFile.capture(source);held.append(frozen)
  if sha(source)!=p['after_capture']['sha256']:raise ValueError('Stale full candidate')
  baseline=None
  if p['kind']=='edit_existing_owner':
   before=FrozenFile.capture(W/p['owner_path']);held.append(before)
   if hashlib.sha256(before.content).hexdigest()!=p['before_sha256']:raise ValueError('Stale authentic preimage')
   baseline=yaml.safe_load(before.content)
  record=yaml.safe_load(frozen.content);revised,proof=apply_exact_edits(record,baseline,row['edits'])
  if revised==record:raise ValueError('Empty type correction')
  record_curation_event(revised,curator='worker02 /root',action='CORRECTED',changes='Under #1226, retype only the explicitly bound newly agent-authored ontology mapping evidence entries '+','.join(str(x['evidence_index']) for x in proof)+' from human-supplied MANUAL_CURATION to LLM_SUGGESTION. Exact citations, scientific notes, prior history, component evidence and all source/owner/role/export holds remain unchanged. This records authorship, not scientific approval.',llm_assisted=True)
  stage=W/'.temp/w02-final-corrections-v1/provenance-stage'/output.name/(p['proposal_id']+'.yaml');stage.parent.mkdir(parents=True,exist_ok=True);assert not stage.exists();write_validated_ingredient(revised,stage)
  target=output/'after'/(p['proposal_id']+'.yaml');target.parent.mkdir(parents=True,exist_ok=True);outputs.append((target,stage.read_bytes()))
  oldcap=deepcopy(p['after_capture']);p['after_capture']={'root':'artifact','path':str(target.relative_to(A)),'sha256':sha(stage)}
  changes.append({'proposal_id':p['proposal_id'],'before_scientific_capture':oldcap,'after_capture':p['after_capture'],'entries':proof,'other_fields_unchanged_except_appended_history':True})
 def verify():
  for snapshot in held:snapshot.verify()
 publish_new_files(outputs,verify);verify()
 result={'schema_version':1,'proposals':[proposals[p['proposal_id']] for p in document['proposals']]}
 receipt={'author':'worker02 /root','created_at':datetime.now(timezone.utc).isoformat(),'plan_sha256':sha(args.plan),'pretype_proposals_sha256':sha(path),'changed_candidates':changes,'original_flag_dispositions':plan['original_flag_dispositions'],'independent_scientific_or_provenance_approval':False,'limits':'Guarded native writes plus exclusive bounded publication. Native publisher is not a multi-file atomic transaction; private complete selection is published only after successful validation/review. No maintained data is written.'}
 for name,value in [('proposals.json',result),('type-correction-receipt.json',receipt)]:
  with (output/name).open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps({'corrected_candidates':len(changes),'corrected_entries':sum(len(c['entries']) for c in changes),'original_entries_accounted':len(flags)}))
if __name__=='__main__':main()
