"""Exact #1226 report-only writer. No production or maintained paths are writable.

Refuses stale inputs and existing/aliased destinations before native serialization.
This is a single-author task wrapper, not a hostile-concurrency/atomicity API.
"""
from pathlib import Path
import copy,hashlib,json,os,subprocess,sys
import yaml
R=next(p for p in Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file())
sys.path.insert(0,str(R/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient,validate_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
HEAD='f6bfbf3c185f705484aa106405f813209146c766'
ALLOWLIST_SHA='9b8283520ab7f9911f4997d62a85aea798f634bd8e8ed69c60dd77a26cdeec9d'
PACKET=R.parents[2]/'preflight/w03-current-provenance-allowlist-v1'
ARTIFACT=R/'reports/all_unmatched_20261107/worker-03'
CURRENT=ARTIFACT/'successors/issue1224-v1/publication-v1'
PUBLICATION=ARTIFACT/'successors/issue1226-v1'
PRIVATE=R/'.temp/w03-provenance-successor-v1'
ACTION='CORRECTED_EVIDENCE_PROVENANCE'
def require(v,msg):
 if not v:raise ValueError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def read_regular(p):
 require(p.is_file() and not p.is_symlink(),'not a regular non-symlink input: '+str(p));return p.read_bytes()
def verify_binding(row,proposal,payload,before):
 require(row['proposal_id']==proposal['proposal_id'],'proposal mismatch')
 require(row['field']=='ontology_mapping.evidence[0].evidence_type','unlisted field')
 require(row['change']=={'from':'MANUAL_CURATION','to':'LLM_SUGGESTION'},'unlisted substitution')
 require(row['proposal_kind']==proposal['kind'] and row['owner_path']==proposal['owner_path'] and row['case_ids']==proposal['case_ids'],'origin mismatch')
 require(row['payload']['sha256']==proposal['after_capture']['sha256']==sha(payload),'old payload bytes differ')
 require(row['current_published_head']==HEAD,'wrong current head')
 record=yaml.safe_load(payload)
 require(record['identifier']==row['current_identifier'] and record['mapping_status']==row['current_mapping_status'],'identity/status drift')
 obj=record['ontology_mapping']['evidence'][0];parent={k:v for k,v in record['ontology_mapping'].items() if k!='evidence'}
 require(obj==row['complete_mapping_evidence_object'] and sha(canon(obj))==row['complete_object_canonical_sha256'],'complete object drift')
 require(parent==row['parent_context'] and sha(canon(parent))==row['parent_context_sha256'],'parent mapping drift')
 require(sha(canon(record.get('curation_history',[])))==row['history_prefix_sha256'],'history prefix drift')
 require(obj['evidence_type']=='MANUAL_CURATION','already corrected or wrong evidence type')
 require(row['classification']=='new_agent_record','not an allowed newly agent-authored object')
 if row['authentic_before'] is None:
  require(before is None and proposal['before_sha256'] is None and proposal['kind']=='new_owner','fabricated new-owner beforeimage')
 else:
  require(before is not None and sha(before)==row['authentic_before']['sha256']==proposal['before_sha256'],'authentic beforeimage drift')
  old=yaml.safe_load(before)
  require(obj not in old.get('ontology_mapping',{}).get('evidence',[]),'inherited evidence excluded')
  require({k:v for k,v in old.get('ontology_mapping',{}).items() if k!='evidence'}==row['before_parent_context'],'before parent drift')
 history=record.get('curation_history',[])
 require(all(x in history for x in row['author_evidence']['added_curation_history']),'author history missing')
 return record

def retained_projection(record):
 r=copy.deepcopy(record);r['ontology_mapping']['evidence'][0]['evidence_type']='PROJECTION_ENUM';r.pop('curation_history',None);return r

def corrected_record(row,record):
 result=copy.deepcopy(record);result['ontology_mapping']['evidence'][0]['evidence_type']='LLM_SUGGESTION'
 event=record_curation_event(result,curator='codex-worker03 /root provenance successor',action=ACTION,changes='Correct only ontology_mapping.evidence[0].evidence_type from MANUAL_CURATION to LLM_SUGGESTION under https://github.com/CultureBotAI/MediaIngredientMech/issues/1226; exact allowlist '+row['audit_row_id']+'. The original assertion was agent-authored interpretation, not human-supplied evidence. Preserve its source, notes, complete prior history and all scientific fields/holds. Report-only proposal; no identity, role or export reapproval.',previous_status=record['mapping_status'],new_status=record['mapping_status'],llm_assisted=True)
 require(retained_projection(record)==retained_projection(result),'scientific fields changed')
 require(result['curation_history'][:-1]==record.get('curation_history',[]),'history prefix changed')
 require(not validate_ingredient(result),'native schema rejected corrected record')
 return result,event

def check_destination(root,dest):
 root=Path(root);dest=Path(dest)
 require(root.is_absolute() and dest.is_absolute(),'absolute private paths required')
 require('..' not in root.parts and '..' not in dest.parts,'lexical traversal refused')
 permitted=any(root.is_relative_to(p) for p in [PUBLICATION,PRIVATE/'technical'])
 require(permitted,'outside declared private/report output boundary')
 require(dest.is_relative_to(root) and dest!=root,'destination escapes output root')
 for p in [root,*root.parents,dest,*dest.parents]:
  require(not p.is_symlink(),'symlink/aliased output path refused')
 require(root.resolve()==root and dest.resolve()==dest,'resolved output alias refused')
 require(not os.path.lexists(dest),'existing destination refused')
 if dest.parent.exists():require(not any(p.name.casefold()==dest.name.casefold() for p in dest.parent.iterdir()),'case-aliased destination refused')

class Repair:
 def __init__(self):
  data=read_regular(PACKET/'repair-allowlist.json');require(sha(data)==ALLOWLIST_SHA,'allowlist bytes changed')
  self.rows={x['proposal_id']:x for x in json.loads(data)['rows']};require(len(self.rows)==49,'allowlist cardinality')
  self.row_hashes={k:sha(canon(v)) for k,v in self.rows.items()};self.prepared_hashes={}
  require(subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD'],text=True).strip()==HEAD,'source head changed')
  for n in ['decisions.json','proposals.json','evidence.json']:
   require(read_regular(CURRENT/n)==read_regular(PACKET/('current-'+n)),'current complete core drift: '+n)
  self.proposals={x['proposal_id']:x for x in json.loads((CURRENT/'proposals.json').read_text())['proposals']}
  self.cases={x['case_id']:x for x in json.loads((CURRENT/'decisions.json').read_text())['decisions']}
 def prepare(self,pid):
  require(pid in self.rows,'unlisted proposal');row=self.rows[pid];require(sha(canon(row))==self.row_hashes[pid],'allowlisted row mutated')
  p=self.proposals[pid];payload=read_regular(R/row['published_payload_path']);require(payload==read_regular(PACKET/row['payload']['path']),'packet/source payload mismatch')
  before=read_regular(R/row['authentic_before_path']) if row['authentic_before_path'] else None
  if before is not None:require(before==read_regular(PACKET/row['authentic_before']['path']),'packet/native before mismatch')
  else:require(not os.path.lexists(R/p['owner_path']),'new-owner path unexpectedly exists')
  require(all(self.cases[k]['case_input_sha256']==v for k,v in row['case_input_sha256'].items()),'case binding drift')
  record=verify_binding(row,p,payload,before);result,event=corrected_record(row,record)
  self.prepared_hashes[pid]=sha(canon(result))
  return {'row':copy.deepcopy(row),'proposal':copy.deepcopy(p),'before_record':record,'after_record':result,'event':event,'old_bytes':payload}
 def write(self,prepared,root,dest):
  row=prepared['row'];pid=row['proposal_id'];require(pid in self.rows and sha(canon(row))==self.row_hashes[pid],'unlisted/mutated write row')
  # Rebind current bytes immediately before the one authorized native write.
  p=self.proposals[pid];before=read_regular(R/row['authentic_before_path']) if row['authentic_before_path'] else None
  current=verify_binding(row,p,read_regular(R/row['published_payload_path']),before)
  require(current==prepared['before_record'],'prepared source drift')
  after=prepared['after_record'];require(sha(canon(after))==self.prepared_hashes.get(pid),'prepared output/history mutated');expected=copy.deepcopy(current);expected['ontology_mapping']['evidence'][0]['evidence_type']='LLM_SUGGESTION';expected['curation_history'].append(prepared['event'])
  require(after==expected,'unlisted output field/object drift')
  event=prepared['event'];require(event['action']==ACTION and event['llm_assisted'] is True and event['previous_status']==event['new_status']==current['mapping_status'] and 'issues/1226' in event['changes'],'invalid history event')
  check_destination(root,dest);write_validated_ingredient(after,dest)
  require(yaml.safe_load(read_regular(dest))==after,'serializer semantic drift')
  return {'proposal_id':pid,'audit_row_id':row['audit_row_id'],'before_payload_sha256':sha(prepared['old_bytes']),'after_payload_sha256':sha(dest.read_bytes()),'new_payload_path':str(dest.relative_to(R)),'old_object':row['complete_mapping_evidence_object'],'new_object':after['ontology_mapping']['evidence'][0],'parent_context':row['parent_context'],'before_history_sha256':row['history_prefix_sha256'],'appended_history':event,'scientific_projection_sha256':sha(canon(retained_projection(after))),'full_record_unchanged_except_exact_enum_and_history':True,'original_proposal':p,'original_authorship_and_reviews':row['author_evidence'],'authentic_before':row['authentic_before']}
