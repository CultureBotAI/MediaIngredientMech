"""Bounded report-only Mc component correction. No maintained writes."""
import copy,datetime,hashlib,json,subprocess,shutil
from pathlib import Path
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
R=Path.cwd();P=R/'.temp/mc-dependent-successor-v1';A=R/'reports/all_unmatched_20261107/worker-08';OLD=A/'successors/issue-1237-tenvit-v1';O=A/'successors/issue-1237-mc-dependent-v1'
HEAD='a0190fed72b8f5119432003d1f9c84b8c1de7a48';OWNER='data/ingredients/mapped/Mc_vitamins.yaml';BEFORE='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123';CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506';TRIGGER='CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531';PID='mc1237-prop-mc-vitamins-dependent'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def ref(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
SCOPE='This component assertion transcribes only the CultureBotHT Mc_vitamins Mixes block, rows1112–1125: ten literal solutes in g/L with source metadata X100. COMPLETE is closure of that printed immediate solute list, not a claim about carrier, final volume, purchased lot or analytical composition. The JCM197/NBRC837/NBRC903 batch tables retain their own literal unspecified calcium-pantothenate and Vitamin B12 labels, masses, added-water inputs and individual preparation profiles; they do not inherit Mc D,L or per-litre assertions. No water, phosphate, gas, titrant or X100 rescaling is added here.'
DEP='SCI-TENVIT-003 dependent comparator correction, triggered by the existing NBRC903 occurrence '+TRIGGER+' in W08 case '+CID+'. The separately reviewed ten-vitamin sources and McCas protocol support a common nominal laboratory recipe; generic CultureBot Wolfe also overlaps nominally. Final occurrence association and cross-owner routing remain pending the bounded W04/coordinator decision. Neither Mc nor CB is declared the exclusive owner, and no duplicate nominal owner, merge, source-number identity or inherited owner/role/export approval is introduced. This dependency claims zero Mc campaign occurrences; the authentic Mc source statistics remain22. The other five occurrences in the mixed W08 case and the external eight-case/71CM/84KG/six-exclusion envelope remain unchanged.'
def make_candidate(before,timestamp):
 assert before['identifier']=='kgmicrobe.ingredient:mc_vitamins'
 assert len(before['curation_history'])==4
 c=before['components'][6]
 assert c=={'component_name':'calcium D,L-pantothenate','component_id':'CHEBI:31345','reference_scope':'MIM_CATALOG','concentration_value':'0.005','concentration_unit':'G_PER_L'}
 rec=copy.deepcopy(before);c=rec['components'][6];del c['component_id'];c['reference_scope']='UNMAPPED'
 c['source']='CultureBotHT Mixes row1122 literally names calcium D,L-pantothenate at0.005g/L. The compounds-to-CAS row92 combines D/L aliases with CAS137-08-6 and Sigma C8731; CHEBI:31345 carries a D-specific structure. That conflicted crosswalk does not establish the literal D,L form. No same-form child is verified in this bounded correction; the name and amount are retained without a resolving ID.'
 oldnote=rec['component_assertion']['evidence'][1]['notes']
 rec['component_assertion']['evidence'][1]['notes']='The CultureBotHT compounds-to-CAS crosswalk supplies historical reference context for the Mc inputs. Row92 combines calcium D,L-pantothenate with D-calcium aliases, CAS137-08-6 and Sigma C8731; it cannot ground the explicit D,L input to D-specific CHEBI:31345. That component remains UNMAPPED. The B12 crosswalk is source-specific dictionary context, not proof of an actual purchased Mc vitamer or of JCM/NBRC Vitamin B12 identity. Other inherited references remain unchanged within their prior scope. The original blanket grounding note is retained verbatim in the appended curation event.'
 rec['component_assertion']['notes']=SCOPE
 rec['component_assertion']['evidence'].append({'evidence_type':'CURATED_DATASET','source':'https://www.ebi.ac.uk/chebi/CHEBI:31345','source_record':'CHEBI:31345; archived OLS4 response and CultureBotHT Mixes row1122/compounds-to-CAS row92','notes':'The primary ontology record supplies a stereospecific SMILES/InChI, D-calcium pantothenate synonyms and CAS137-08-6. It does not establish the printed D,L ingredient. The component-reference withdrawal is an LLM-assisted assessment, not a new recipe input, owner identity or role assertion. Original acquisition receipts and exact capture bytes are retained in the proposal evidence bundle.'})
 rec['notes']+='\n\n'+SCOPE+'\n\n'+DEP
 event=record_curation_event(rec,curator='worker08:/root SCI-TENVIT-003 dependent source proposal',action='CORRECTED',changes='Withdraw unsupported D-specific CHEBI:31345 from the literal calcium D,L-pantothenate0.005G_PER_L component and set native reference_scope UNMAPPED. Qualify the historical CAS-crosswalk grounding note and explicitly limit decomposition to the Mc source table. Preserve all ten names/amounts/units, other nine resolving references, four original history events, identity, aliases,22-source statistics, original role objects and X100 metadata. Link a genuine existing-owner dependency to the reviewed NBRC903 comparator; candidate association and cross-owner routing remain pending W04/coordinator, with no owner merge or release approval. Original crosswalk note: '+oldnote,previous_status='MAPPED',new_status='MAPPED',llm_assisted=True,llm_model='GPT-6',timestamp=timestamp)
 assert rec['curation_history'][:-1]==before['curation_history'] and event['llm_assisted'] is True
 for k in set(before)|set(rec):
  if k not in ['components','component_assertion','notes','curation_history']:assert rec.get(k)==before.get(k),k
 for i in range(10):
  for k in ['component_name','concentration_value','concentration_unit']:assert rec['components'][i][k]==before['components'][i][k]
  if i!=6:assert rec['components'][i]==before['components'][i]
 return rec

def main():
 assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD
 assert sha(R/OWNER)==sha(O/'beforeimages/Mc_vitamins.yaml')==BEFORE
 assert sha(OLD/'selection.json')=='fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699'
 now=datetime.datetime.now(datetime.timezone.utc).isoformat();before=yaml.safe_load((R/OWNER).read_text());rec=make_candidate(before,now)
 out=O/'payloads/Mc_vitamins.yaml';assert not out.exists();out.parent.mkdir();write_validated_ingredient(rec,out);assert yaml.safe_load(out.read_text())==rec
 oldd=next(x for x in read(OLD/'decisions.json')['decisions'] if x['case_id']==CID);case=copy.deepcopy(oldd);assert TRIGGER in case['occurrence_ids'] and len(case['occurrence_ids'])==6
 eids=['mc1237-author-assessment','mc1237-source-readback','mc1237-filed-003','mc1237-filed-continuity','mc1237-original-route-envelope','mc1237-dependency']
 proposal={'proposal_id':PID,'kind':'edit_existing_owner','owner_path':OWNER,'before_sha256':BEFORE,'after_capture':ref(out),'case_ids':[CID],'source_occurrence_ids':[TRIGGER],'description':DEP,'source_scope':'Existing-owner correction triggered by NBRC903 comparator; no Mc campaign occurrence or accepted exact stock association is asserted.','mc_campaign_occurrence_count':0,'evidence_ids':eids,'publication_review_obligations':['Authorship-separated full final payload/source-case and lineage review.','W04/coordinator cross-owner nominal source routing remains pending; no exclusive Mc/CB winner or duplicate installation.','Original role, source/form, owner and export holds remain; ATCC MD-VS positive phosphate/product boundary unchanged.']}
 case['reasoning']+='\n\nCurrent SCI-TENVIT-003 dependency: '+DEP;case['applicability']+='\n\nOnly NBRC903 triggers the Mc comparator correction. The supported nominal recipe comparison is distinct from pending W04 cross-owner association. No actual occurrence is newly mapped to Mc; original source labels, doses, six-occurrence partition and exclusions remain.'
 case['owner_records'].append({'path':OWNER,'sha256':BEFORE});case['proposal_ids'].append(PID);case['evidence_ids']+=eids
 for url in ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720042215','https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720201812']:case['issue_refs'].append(url)
 case.setdefault('prior_independent_reviews',[]).append(case['independent_review']);case['independent_review']={'status':'pending','evidence_ids':[]}
 save(O/'author/proposal.json',proposal);save(O/'author/decision.json',case)
 save(O/'author/assessment.json',{'at':now,'author':'worker08:/root','beforeimage':ref(O/'beforeimages/Mc_vitamins.yaml'),'payload':ref(out),'history_count_before':4,'history_count_after':5,'history_prefix_preserved':True,'native_event_helper':'mediaingredientmech.curate.curation_event.record_curation_event','native_guarded_writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','changed_top_level_fields':[k for k in rec if before.get(k)!=rec[k]],'unchanged_top_level_fields':[k for k in before if before[k]==rec[k]],'complete_ten_literal_component_profiles_preserved':True,'same_form_decision':'No same-form child verified; UNMAPPED with component_id omitted.','routing':'Pending W04/coordinator; common nominal recipe supported without exclusive owner association.','scientific_acceptance':'Pending independent final-payload review','whole_owner_role_export_approval':False})
 save(O/'author/dependency.json',{'new_proposal':proposal,'changed_case_id':CID,'all_six_occurrence_ids':case['occurrence_ids'],'trigger_occurrence':TRIGGER,'zero_new_case_or_mc_campaign_occurrence':True,'prior_proposal_ids':oldd['proposal_ids'],'prior_proposal_objects_payloads_evidence_immutable':True,'existing_CB_proposal_unchanged':'vm1237-prop-wolfe-cb-dependent','existing_NBRC903_new_owner_null_before_unchanged':'vm1201-prop-nbrc903-vitamin','source_envelope':ref(O/'inputs/w09-continuity/source-routing-and-origin-bindings.json'),'source_envelope_counts':read(O/'inputs/w09-continuity/source-routing-and-origin-bindings.json')['counts'],'routing_status':'PENDING_W04_CROSS_OWNER_DECISION','source_recipe_profiles':'Retain original Mc g/L X100; JCM/NBRC literal masses/water-input and individual procedures; no stereochemistry/vitamer/carrier/gas/final-volume transfer.','no_role_export_or_owner_approval':True})
 shutil.copy2(Path(__file__),O/'provenance/author.py');print(json.dumps({'payload':ref(out),'proposal':ref(O/'author/proposal.json'),'case':ref(O/'author/decision.json')},indent=2))
if __name__=='__main__':main()
