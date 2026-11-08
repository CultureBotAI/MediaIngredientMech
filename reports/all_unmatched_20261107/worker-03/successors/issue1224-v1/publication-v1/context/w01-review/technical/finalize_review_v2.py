import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

P=Path(__file__).resolve().parent
def read(n):return json.loads((P/n).read_text())
def bind(p):return {'path':str(Path(p).resolve()),'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest()}
def save(n,v):
    with (P/n).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
all_d=read('whole-candidate-dossiers-v1.json');d=next(x for x in all_d if x['candidate_id']=='TARGET-024')
o=next(x for x in d['origins'] if x['origin']['entry_id']=='w05::MATERIALS-C1193-soy-peptone-boundary')
entry=d['candidate']['ontology_mapping']['evidence'][0]
assert entry==o['full_record']['ontology_mapping']['evidence'][0]
assert entry not in d['authentic_before']['ontology_mapping']['evidence']
assert entry['source']=='https://mediadive.dsmz.de/rest/ingredient/75' and entry['evidence_type']=='MANUAL_CURATION'
event=next(x for x in o['full_record']['curation_history'] if x['curator']=='worker05/materials_research correction1193 (isolated proposal)')
assert event['llm_assisted'] is True and event['llm_model']=='gpt-6'
lineage=next(x for x in read('nine-candidate-lineage-schema-alias-v1.json') if x['candidate_id']=='TARGET-024')
now=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
finding={'finding_id':'W01-NINE-TECH-001','issue_key':'CultureBotAI/MediaIngredientMech/1226/soy-source75-worker-evidence','category':'provenance','severity':'major','status':'open','certainty':'confirmed','title':'Retained W05 source75 mapping evidence is labeled human-supplied','description':'TARGET-024 ontology_mapping.evidence[0] is MANUAL_CURATION for the MediaDive ingredient75 interpretation. That exact object is absent from the authentic beforeimage and first appears in the W05 isolated proposal whose actual event identifies worker05/materials_research, llm_assisted=true and gpt-6. The final coordinator candidate retains it unchanged. The current MappingEvidence enum defines MANUAL_CURATION as human-supplied evidence; this exact source lineage does not support that attribution. This is a concrete inherited-worker counterexample under existing1226, separate from the13new coordinator entries already corrected. No global reclassification or new affected-count claim follows.','target_ids':['TARGET-024'],'field_paths':['ontology_mapping.evidence[0]'],'evidence_ids':['retained-worker-provenance','lineage','metadata'],'rule_id':'EvidenceTypeEnum.MANUAL_CURATION','native_severity':'P2 retained evidence provenance','normalization_reason':'Material provenance misattribution in a retained current claim; schema-valid and scientifically unassessed. Prevents unqualified whole-candidate acceptance but does not invalidate the correctly bounded13-entry coordinator correction.','ownership_note':'W05 original source proposal and coordinator TARGET-024 successor; coordinator/W02 inherited-evidence audit owns any future guarded correction. No record changed by this reviewer.','external_issues':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1226']}
proof={'at':now,'reviewer':'OpenAI Codex /root/issue_context independent technical reviewer','discovery_attribution':'Skeptical reviewer isolated the exact counterexample; technical reviewer independently compared complete authentic before, W05 origin and final objects and the actual author event.','finding':finding,'authentic_before':lineage['authentic_before'],'authentic_before_mapping_evidence':d['authentic_before']['ontology_mapping']['evidence'],'origin_payload':next(x['payload'] for x in lineage['origins'] if x['entry_id']==o['origin']['entry_id']),'origin_entry_id':o['origin']['entry_id'],'actual_W05_event':event,'final_candidate':lineage['candidate'],'retained_exact_evidence_object':entry,'three_way_object_comparison':{'absent_from_authentic_before':True,'introduced_in_W05':True,'identical_in_final_candidate':True},'schema':next(x for x in read('native-full-projection-v1.json')['native_sources'] if x['path'].endswith('/schema/mediaingredientmech.yaml')),'preservation':'No candidate or source mutation. Older MIM#260 manual evidence is a different entry; ComponentEvidenceType is a separate enum. Only this exact retained worker object is dispositioned here.'}
save('finding-retained-worker-evidence-1226-v1.json',proof)
review=yaml.safe_load((P/'review-v1.yaml').read_text())
review['review_id']=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-w01-nine-candidate-technical-v2'
review['finished_at']=now
review['verdict']='needs_curation'
review['native_verdict']='NATIVE_GUARD_CHECKS_PASS_RETAINED_WORKER_PROVENANCE_DEFECT_HELD'
review['summary']='All nine native schema checks, full37-candidate partonomy projection, guards, origin/case hashes,13new coordinator evidence corrections and33exact byte reuses pass. One confirmed retained W05 evidence-provenance defect in TARGET024 remains under existing1226. Unqualified whole-candidate acceptance is withheld; no payload changes or global inherited-evidence reinterpretation.'
review['evidence'].append({'evidence_id':'retained-worker-provenance','kind':'record_content','reference':str(P/'finding-retained-worker-evidence-1226-v1.json'),'locator':'Exact authentic-before / W05 origin / final evidence object and actual W05 authorship event','accessed_at':now,'support':'supports','summary':'Confirms the bounded retained source75 provenance defect under1226, separate from the13coordinator corrections.','snapshot_sha256':bind(P/'finding-retained-worker-evidence-1226-v1.json')['sha256']})
review['findings']=[finding]
review['assessments'].append({'assessment_id':'retained-source75-evidence','area':'provenance','topic':'Inherited worker evidence source attribution','outcome':'concern','summary':finding['description'],'target_ids':['TARGET-024'],'evidence_ids':['retained-worker-provenance','lineage']})
review['actions']=[{'action_id':'retain-1226-source75-hold','description':'Carry this exact source75 object into the coordinator/W02 inherited-evidence audit under1226. Before whole-candidate acceptance, prepare any separately authorized guarded successor with truthful attribution and appended history, then re-review the exact bytes. Do not globally replace inherited enums or alter ComponentEvidenceType.','finding_ids':[finding['finding_id']],'target_ids':['TARGET-024'],'ownership_note':finding['ownership_note'],'acceptance_checks':['Bind the unchanged authentic before and W05 original; preserve all prior histories and source URLs.','Independently verify the exact replacement evidence attribution and native schema; keep the13already corrected coordinator entries and33byte-reuse claims intact.','Repeat focused native alias and full projected reference checks only if the authorized successor affects those surfaces.']}]
review['limitations'].append('The source75 retained W05 counterexample is confirmed, not merely a generic future-audit lead. It is not counted among the13new coordinator entries. All broader inherited evidence remains outside this narrow disposition and no blanket rewrite is authorized.')
review['notes'].append('Supersedes the unsealed review-v1 draft for its no-findings conclusion. Native validation rejected that first YAML solely for serialization aliases; both draft and failure receipt are preserved. This successor uses a no-alias serializer and adds the independently confirmed retained-worker finding.')
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self,data):return True
with (P/'review-v2.yaml').open('x') as out:yaml.dump(review,out,Dumper=NoAliasDumper,sort_keys=False,allow_unicode=True,width=100)
final=read('REVIEW-v1.json');final.update(at=now,verdict=review['native_verdict'],new_findings=[finding],review_yaml=bind(P/'review-v2.yaml'),prior_unsealed_draft=bind(P/'REVIEW-v1.json'),retained_worker_finding=bind(P/'finding-retained-worker-evidence-1226-v1.json'))
final['limits']=review['limitations'];final['programs'].append(bind(Path(__file__)))
final['assessments']['TARGET-024']+=' Exact source75 MANUAL_CURATION retained from the LLM-authored W05 proposal is a confirmed provenance defect under1226; unqualified whole-candidate acceptance is withheld.'
save('REVIEW-v2.json',final)
print(json.dumps({'report':bind(P/'REVIEW-v2.json'),'yaml':bind(P/'review-v2.yaml'),'finding':bind(P/'finding-retained-worker-evidence-1226-v1.json')}))
