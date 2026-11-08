"""Isolated, before-guarded successors; never writes a maintained surface."""
from pathlib import Path
import copy, datetime, difflib, hashlib, json, sys, yaml
sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event

O=Path(__file__).parent
R=Path('reports/all_unmatched_20261107/worker-05')
BASE=R/'final-correction-v1/core'
PREFIX='postseal-source-corrections-v1/chemicals/'
AUTHOR='Codex worker05 /root/chemicals_research postseal source review'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def dump(name,x):
 p=O/name; assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n');return p
def cap(p):return {'root':'artifact','path':PREFIX+str(p.relative_to(O)),'sha256':sha(p)}
P=json.loads((BASE/'proposals.json').read_text())['proposals']
D=json.loads((BASE/'decisions.json').read_text())['decisions']
selected=[p for p in P if p['proposal_id'].startswith('R1193-DEP-rumen-')]
assert len(selected)==3
caseids={c for p in selected for c in p['case_ids']};assert len(caseids)==1
caseid=next(iter(caseids))
raw=json.loads((O/'microbedecoder-three-parent-source-records-v1.json').read_text())
refs={'R1193-DEP-rumen-pyglucose':(20394,'Bergey_Substrates_for_end_products'),
      'R1193-DEP-rumen-pyg':(5905,'Bergey_Substrates_for_end_products'),
      'R1193-DEP-rumen-casitone':(5903,'Literature_Substrates_for_end_products')}
common=('The rumen-fluid component is retained at the literal source-label scope as rumen fluid, '
        'UNMAPPED, with no component identifier. The recovered MicrobeDecoder observation does not specify '
        'clarification, animal species, or a preparation protocol. The full cited publication was not '
        'retrieved in this review; the captured access failures cannot establish a protocol. '
        'This is unresolved processing, not evidence that the fluid was untreated. '
        'The former redirect to kgmicrobe.ingredient:clarified_rumen_fluid is withdrawn under '
        'https://github.com/CultureBotAI/MediaIngredientMech/issues/1204#issuecomment-6718503591 '
        'and https://github.com/CultureBotAI/MediaIngredientMech/issues/1237. '
        'Unrelated component identities, concentrations, whole-mixture identity and source holds are unchanged. '
        'Inherited mapping-evidence objects and research evidence remain historical provenance; their '
        'clarification claims and historical all-components-identified counts do not describe this successor. '
        'The prior 2026-11-08 dependency-only redirect event is preserved as superseded history. '
        'No generic UBERON grounding, recipe equivalence, animal-origin claim or downstream approval is added.')
newp=[];lineage=[]
for prior in selected:
 before=R/prior['after_capture']['path'];assert sha(before)==prior['after_capture']['sha256']
 assert sha(prior['owner_path'])==prior['before_sha256']
 old=yaml.safe_load(before.read_text());record=copy.deepcopy(old)
 ix=[i for i,c in enumerate(record['components']) if c.get('component_id')=='kgmicrobe.ingredient:clarified_rumen_fluid'];assert len(ix)==1
 i=ix[0];record['components'][i]['component_name']='rumen fluid';record['components'][i]['reference_scope']='UNMAPPED';del record['components'][i]['component_id']
 number,column=refs[prior['proposal_id']]
 source=next(r for r in raw['records'] if r['record_number']==number);literal=source['complete_record'][column]
 source_note=f'MicrobeDecoder database.csv record {number}, {column} = {literal!r}; full source-row capture and database SHA are retained in {PREFIX}microbedecoder-three-parent-source-records-v1.json.'
 record['notes']=old['notes'].split(' Dependency-only reference maintenance')[0]+' '+common+' '+source_note
 record['component_assertion']['notes']=old['component_assertion']['notes'].split(' Dependency-only reference maintenance')[0]+' '+common
 record['component_assertion']['evidence'].append({'evidence_type':'SOURCE_LABEL','source':'microbedecoder','source_record':f'database.csv record {number}; {column}; {literal}',
  'notes':source_note+' Reviewed by '+AUTHOR+' with LLM assistance. The unqualified label supports the retained rumen-fluid part but does not establish clarification. Earlier CURATED_DATASET assertions are preserved as superseded provenance for this component, not renewed scientific support. Component evidence typing is distinct from MappingEvidence typing.'})
 record_curation_event(record,curator=AUTHOR,action='CORRECTED',changes=common+' '+source_note,previous_status=old['mapping_status'],new_status=old['mapping_status'],llm_assisted=True,llm_model='gpt-6',timestamp=NOW)
 out=O/'proposed'/before.name;out.parent.mkdir(exist_ok=True);assert not out.exists()
 write_validated_ingredient(record,out,target_class='IngredientRecord');assert yaml.safe_load(out.read_text())==record
 # Exact immutable prefixes and all unrelated fields must survive.
 assert record['curation_history'][:-1]==old['curation_history']
 assert record['ontology_mapping']==old['ontology_mapping']
 assert record['component_assertion']['evidence'][:-1]==old['component_assertion']['evidence']
 for j,c in enumerate(old['components']):
  if j!=i:assert record['components'][j]==c
 for k in old:
  if k not in {'components','component_assertion','curation_history','notes'}:assert record[k]==old[k],k
 diff=O/'diffs'/before.with_suffix('.diff').name;diff.parent.mkdir(exist_ok=True)
 diff.write_text(''.join(difflib.unified_diff(before.read_text().splitlines(True),out.read_text().splitlines(True),fromfile=prior['after_capture']['path'],tofile=PREFIX+'proposed/'+out.name)))
 p=copy.deepcopy(prior)
 p['description']=f'Withdraw the unsupported clarification assertion from the rumen-fluid component in {old["preferred_term"]}; preserve the literal named part as UNMAPPED without an identifier.'
 p['identity_consequence']='The whole-mixture identifier, mapping, source labels and occurrence counts remain unchanged. The part retains its source label; its processing and animal origin remain unspecified.'
 p['predicate_consequence']='Remove this one unsupported MIM_CATALOG component link and retain a named UNMAPPED part with no component_id. Whole-record SSSOM predicates are unchanged.'
 p['publication_obligations']=common+' Original W05 source-case and cross-shard ownership boundaries remain unchanged; this does not add the underlying MicrobeDecoder observations to W05 source ownership.'
 p['after_capture']=cap(out)
 p['postseal_correction']={'finding_id':'W05-POSTSEAL-CHEM-001','author':AUTHOR,'timestamp':NOW,'predecessor_after_capture':prior['after_capture'],'predecessor_proposal_object_sha256':objsha(prior),'predecessor_diff':cap(diff),'guarded_write':'PASS','independent_review':'pending','issue_refs':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1204#issuecomment-6718503591','https://github.com/CultureBotAI/MediaIngredientMech/issues/1237'],'historical_metadata_notice':'Earlier final_correction and predecessor_after_capture fields are retained for historical ancestry, not a claim that their reviews bind this successor.'}
 p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+['POSTSEAL-CHEM-RAW-PARENTS','POSTSEAL-CHEM-1204-COMMENT','POSTSEAL-CHEM-1237','POSTSEAL-CHEM-FINDING001','POSTSEAL-CHEM-PRIMARY-ACCESS']))
 newp.append(p)
 lineage.append({'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'original_before_sha256':p['before_sha256'],'predecessor_after_capture':prior['after_capture'],'after_capture':p['after_capture'],'diff':cap(diff),'component_index':i,'before_component':old['components'][i],'after_component':record['components'][i],'raw_record_number':number,'raw_source_field':column,'raw_source_literal':literal,'history_prefix_unchanged':True,'mapping_evidence_unchanged':True,'other_components_unchanged':True,'whole_identity_unchanged':True})
d=copy.deepcopy(next(x for x in D if x['case_id']==caseid));old_d=copy.deepcopy(d)
d['reasoning']='Both JCM1423 and JCM1424 reference clarified rumen fluid from JCM266. JCM266 describes preheated rumen contents followed by centrifugation and supernatant collection. The different receiving doses, 50 versus 20 ml, do not establish a different fluid identity. The three pre-existing dependent MIM mixtures have recovered MicrobeDecoder labels that say only rumen fluid. Their successor proposals withdraw the unsupported clarification claim and retain an UNMAPPED part without an identifier; they do not redirect those parts to the clarified owner or import additional source-case ownership.'
d['applicability']=old_d['applicability'].split(' These three dependent-owner deltas')[0]+' The three dependent-owner corrections are causally linked to this assigned owner correction. Their raw MicrobeDecoder source fields have now been inspected for the limited processing claim; neither their full formulations nor all underlying biological observations are approved. The six publication retrieval paths tried by web and direct HTTP did not yield full source publications, so the exact processing bridge remains unverified. Historical JCM/DSMZ clarification protocols cannot supply that bridge for these three separate labels.'
d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+[e for p in newp for e in p['evidence_ids']]))
d['issue_refs']=list(dict.fromkeys(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1237','https://github.com/CultureBotAI/MediaIngredientMech/issues/1204#issuecomment-6718503591']))
d['postseal_prior_independent_review']=d['independent_review'];d['independent_review']={'status':'pending','evidence_ids':[],'scope':'Successor decision and three complete dependent payloads require independent review; prior reviewed bytes remain historical.'}
d['postseal_correction']={'finding_id':'W05-POSTSEAL-CHEM-001','author':AUTHOR,'timestamp':NOW,'predecessor_decision_object_sha256':objsha(old_d),'changed_proposal_ids':[p['proposal_id'] for p in newp],'source_case_input_occurrence_owner_and_hold_objects_unchanged':True}
for k in ['case_id','case_input_sha256','source','occurrence_ids','owner_records','preserved_source_holds','proposal_ids']:assert d[k]==old_d[k],k
dump('proposals.json',{'fragment':True,'merge_key':'proposal_id','base':{'path':str(BASE/'proposals.json'),'sha256':sha(BASE/'proposals.json')},'proposals':newp})
dump('decisions.json',{'fragment':True,'merge_key':'case_id','base':{'path':str(BASE/'decisions.json'),'sha256':sha(BASE/'decisions.json')},'decisions':[d]})
dump('changed-payload-lineage-v1.json',{'author':AUTHOR,'created_at':NOW,'scope':'Three existing dependency proposals; no new proposal origin or case.','payloads':lineage})
dump('historical-selected-objects-v1.json',{'proposals':selected,'decision':old_d,'object_sha256_algorithm':'SHA256 of UTF-8 json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=False). Historical objects are not successor review.'})
print(json.dumps({'proposals':len(newp),'decisions':1,'lineage':lineage},indent=2))
