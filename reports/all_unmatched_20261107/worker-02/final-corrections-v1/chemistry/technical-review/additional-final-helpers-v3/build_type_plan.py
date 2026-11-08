"""Bind all58 independently audited new-agent entries to composed exact objects."""
from collections import defaultdict
import hashlib,json
from pathlib import Path
import yaml
R=Path(__file__).resolve().parent;A=R.parent
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def main():
 matrix=load(R/'original-58-claim-type-matrix.json');selection=R/'pretype-v2/proposals.json';props={p['proposal_id']:p for p in load(selection)['proposals']}
 cm=load(R/'preparations/mapping-evidence-lineage.json');bm=load(R/'chemistry/mapping-evidence-lineage.json')['entries']
 edits=defaultdict(list);dispositions=[]
 for claim in matrix['entries']:
  flag=claim['exact_original_flag'];pid=flag['proposal_id'];old=flag['entry'];index=claim['original_flag_index'];lineage=None
  matches=[r for r in cm if r['old_proposal_id']==pid and r['old_fullvalue']==old]
  if matches:
   assert len(matches)==1;lineage=matches[0];pid=lineage['successor_proposal_id'];expected=lineage['successor_fullvalue'];pointer=lineage['successor_pointer'];basis='Explicit preparation-author full-value lineage after source/nominal-stock correction.'
  else:
   matches=[r for r in bm if r['proposal_id']==pid and r.get('predecessor_full_value')==old]
   if matches:
    assert len(matches)==1;lineage=matches[0];expected=lineage['successor_full_value'];pointer=lineage['successor_pointer'];basis='Explicit chemistry-author full-value lineage after finite owner correction.'
   else:expected=old;pointer='/'+flag['pointer'];basis='Exact full MappingEvidence object remains unchanged in the composed scientific candidate.'
  p=props[pid];path=A/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];record=yaml.safe_load(path.read_text());idx=int(pointer.rsplit('/',1)[1]);actual=record['ontology_mapping']['evidence'][idx];assert actual==expected and actual['evidence_type']=='MANUAL_CURATION',(pid,index)
  justification=basis+' '+claim['provenance_audit_row']['rationale']
  edits[pid].append({'evidence_index':idx,'expected_complete_entry':actual,'new_type':'LLM_SUGGESTION','classification':'new_agent_record','basis':justification,'original_flag_indices':[index]})
  dispositions.append({'original_flag_indices':[index],'original_proposal_id':flag['proposal_id'],'original_payload':flag['after_capture'],'original_pointer':flag['pointer'],'original_complete_entry':old,'original_entry_sha256':digest(old),'successor_proposal_id':pid,'successor_pretype_capture':p['after_capture'],'successor_pointer':pointer,'successor_complete_entry':actual,'successor_entry_sha256':digest(actual),'authored_lineage':lineage,'proposed_type':'LLM_SUGGESTION','rule':'New agent judgment, not human-supplied evidence; neither source authorship nor ontology URL establishes human MIM review. Preserve all scientific fields and historical human/component objects.','audit_row':claim['provenance_audit_row']['audit_row_id']})
 assert len(dispositions)==58
 for pid,rows in edits.items():assert len({x['evidence_index'] for x in rows})==len(rows)
 result={'author':'worker02 /root','scope':'Claim-specific #1226 type corrections after completed scientific composition; own-authored entries, no self scientific approval.','pretype_proposals_sha256':sha(selection),'original_matrix_sha256':sha(R/'original-58-claim-type-matrix.json'),'original_flag_dispositions':dispositions,'candidate_edits':[{'proposal_id':pid,'pretype_capture':props[pid]['after_capture'],'edits':rows} for pid,rows in edits.items()],'requires_independent_final_byte_review':True}
 with (R/'type-plan-v1.json').open('x') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps({'original_entries':len(dispositions),'composed_candidates':len(edits)}))
if __name__=='__main__':main()
