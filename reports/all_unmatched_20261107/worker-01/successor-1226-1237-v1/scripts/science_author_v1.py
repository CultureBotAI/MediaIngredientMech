"""Four pinned proposal corrections only: native validation/write then exclusive publication."""
from pathlib import Path
import copy, datetime, hashlib, json, os, re, sys
import yaml
sys.path.insert(0,str(Path.cwd()/'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient, write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.synonym_policy import is_resolving_synonym

D=Path('reports/all_unmatched_20261107/worker-01/successor-1226-1237-v1')
I=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/preflight/final-intake-candidate-v1')
W=Path('reports/all_unmatched_20261107/worker-01')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def out(name,obj):
 p=D/'science'/name
 with p.open('x') as f:json.dump(obj,f,indent=2,ensure_ascii=False);f.write('\n')
def diffs(a,b,p=''):
 if a==b:return []
 if isinstance(a,dict) and isinstance(b,dict):
  return [x for k in sorted(a.keys()|b.keys()) for x in diffs(a.get(k),b.get(k),p+'/'+k)]
 if isinstance(a,list) and isinstance(b,list):
  return [x for k in range(max(len(a),len(b))) for x in diffs(a[k] if k<len(a) else None,b[k] if k<len(b) else None,p+'/'+str(k))]
 return [{'path':p,'before':a,'after':b}]

origins=load(D/'inputs/w01-origin-bindings.json')
allow=load(D/'inputs/w01-full-provenance-allowlist-v2.json')['rows']
input_check=load(D/'science/input-bindings-and-owned-name-check-v1.json')
assert all(not v for v in input_check['owned_name_search']['native_preferred_owner_hits'].values())
assert not input_check['owned_name_search']['selected_proposal_preferred_hits']
assert len(origins)==4
for r in origins:
 assert sha(I/r['payload_path'])==r['payload_sha256']
 assert not (D/'payloads'/(r['proposal_id']+'.yaml')).exists()

hydration=(
 'NBRC1020 prints Na2SeO3 4 mg and Na2WO4 4 mg with 1 L distilled water; '
 'the missing hydrate qualifiers do not establish anhydrous reagents. '
 'JCM317 explicitly prints Na2WO4·2H2O 4 mg with Na2SeO3 4 mg and 1 L distilled water. '
 'The shared nominal amounts and omitted NBRC hydrate do not establish either identical or distinct supplied preparations. '
 'Retain both source-bound partial proposals without merging or co-installing them as proved-distinct owners until supplied-form/applicability evidence or an explicitly reviewed common nominal scope resolves the overlap. '
 'The water amounts are added-water batch quantities, not instructions to make up a final litre.'
)
nb_note='Printed formulas are retained literally; omitted hydration is unresolved, not an anhydrous assignment. '+hydration
jcm_old='Exact source stock distinct from NBRC1020 unhydrated tungstate, JCM852 lower amounts/hydrated selenite, and JCM431 alkaline formula.'
jcm_new=('The JCM317 dihydrate is explicit; a difference from NBRC1020 is not established by its omitted hydrate qualifier. '
         'The previously recorded comparisons with JCM852 lower amounts/hydrated selenite and JCM431 alkaline formula are retained. '+hydration)
fe_text='0.01 M FeSO4·7H2O solution (in 0.02 N HCl)'
fe_rationale=(
 'MAPPING_SEMANTICS section 3 / CHEM-COMP-006 (#1237): the complete raw label '
 +repr(fe_text)+' is an identity-bearing name for this operational stock: it states the ferrous sulfate heptahydrate reagent, 0.01 M strength, and 0.02 N HCl carrier. '
 'JCM1430 and JCM1431 print that name and a 3.0 mL receiving dose after cooling to 50 C. '
 'Its former blanket REJECTED_LABEL disposition is superseded by EXACT_SYNONYM; the exact old rejection text, source and prior history are retained in science/qualifier-negative-audit-lineage-v1.json and the immutable predecessor. '
 'No competing preferred owner was found for the complete token in the explicitly checked current mapped directory and worker01 selected proposals, so owned-name SUPPRESS is not warranted in that scope. '
 'This change does not make shortened ferrous sulfate names equivalent to the stock, infer molecular speciation, or alter component grounding.'
)
bic_rationales=[
 {
 'text':'Bicarbonate solution (1.0 M)***',
 'reason':('NBRC1321 uses this exact string as the receiving-table pointer to its *** footnote. '
 'The text gives a nominal strength but does not name the sodium salt, added-water recipe, or CO2 saturation that defines this proposed preparation. '
 'The *** footnote supplies NaHCO3 8.4 g plus 100 mL distilled water, CO2 saturation, and autoclaving in tightly sealed CO2-filled bottles. '
 'It is a valid source pointer and broader material description, but is not an identity-bearing standalone name for this particular CO2-conditioned stock. '
 'Retain the original sourced REJECTED_LABEL entry and resolve only the explicitly bound source occurrence, rather than claim exact identity for that token outside its footnote.')},
 {
 'text':'Bicarbonate solution***',
 'reason':('NBRC1257 uses this exact string as its receiving-table *** pointer, without even the nominal strength. '
 'Its *** footnote positively specifies the same NaHCO3 8.4 g plus 100 mL distilled water and CO2 saturation/sealed autoclaving as NBRC1321. '
 'The bare token does not identify that sodium/quantity/CO2 preparation independently of the footnote. '
 'Retain its exact sourced REJECTED_LABEL entry as a non-name for this specific owner, while retaining the positive source-occurrence assignment and source-supported NBRC1257/NBRC1321 union.')}
]
bic_note=('MAPPING_SEMANTICS section 3 / CHEM-COMP-006 (#1237), individual label assessments: '
 ' '.join(repr(r['text'])+': '+r['reason'] for r in bic_rationales)+
 ' No competing preferred owner of either exact token was found in the explicitly checked current mapped directory and worker01 proposal set, so no owned-name suppression is proposed. '
 'These dispositions concern name applicability to this specific preparation, not rejection of bicarbonate as a material. '
 'The reported 1.0 M remains nominal: 100 mL is added water, not verified final solution volume; dissolved CO2 amount/speciation is unquantified. '
 'Carbon dioxide remains a source-listed material input because the solution is explicitly saturated, independently of the CO2 headspace condition.')

records=[];audit=[];types=[]
for r in origins:
 old=yaml.safe_load((I/r['payload_path']).read_text());new=copy.deepcopy(old);pid=r['proposal_id']
 rows=[a for a in allow if a['proposal_id']==pid]
 for a in rows:
  match=re.fullmatch(r'ontology_mapping.evidence\[(\d+)\]',a['field']);assert match,a['field']
  i=int(match[1]);ev=new['ontology_mapping']['evidence'][i]
  assert ev==a['full_value'];assert ev['evidence_type']=='MANUAL_CURATION';assert a['suggested_native_type']=='LLM_SUGGESTION'
  ev['evidence_type']='LLM_SUGGESTION'
  assert {k:v for k,v in ev.items() if k!='evidence_type'}=={k:v for k,v in a['full_value'].items() if k!='evidence_type'}
  types.append({'proposal_id':pid,'audit_row_id':a['audit_row_id'],'field':a['field']+'.evidence_type','before':'MANUAL_CURATION','after':'LLM_SUGGESTION','other_complete_object_fields_unchanged':True,'reason':'Agent-authored stock-identity/registry interpretation, not evidence supplied by a human reviewer; #1226 claim-specific allowlist.'})
 if r['index']==6:
  for obj in [new,new['component_assertion']['evidence'][0]]:
   assert obj['notes'].count('Printed unhydrated formulas are retained.')==1
   obj['notes']=obj['notes'].replace('Printed unhydrated formulas are retained.',nb_note)
  new['component_assertion']['notes']+=' '+hydration
  change='Correct CHEM-COMP-002 (#1237): replace inferred unhydrated NBRC wording with literal formulas and unresolved supplied hydration; retain NBRC824 missing-denominator hold, literal batch quantities, and merge/co-installation hold against JCM317. '
 elif r['index']==13:
  for obj in [new,new['component_assertion']['evidence'][0]]:
   assert obj['notes'].count(jcm_old)==1
   obj['notes']=obj['notes'].replace(jcm_old,jcm_new)
  new['component_assertion']['notes']+=' '+hydration
  change='Correct CHEM-COMP-002 (#1237): withdraw unsupported NBRC1020 unhydrated/distinct claim while preserving explicit JCM317 dihydrate, literal batch amounts and other source comparisons; retain unresolved overlap and merge/co-installation hold. '
 elif r['index']==35:
  assert len(new['synonyms'])==1 and new['synonyms'][0]['synonym_text']==fe_text and new['synonyms'][0]['synonym_type']=='REJECTED_LABEL'
  new['synonyms'][0]['synonym_type']='EXACT_SYNONYM'
  new['synonyms'][0]['source']=('JCM1430 https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1430 and JCM1431 https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1431, complete stock label in post-cooling additions. CHEM-COMP-006 (#1237) individual reassessment; original rejected assertion/source preserved in immutable predecessor and science/qualifier-negative-audit-lineage-v1.json.')
  new['notes']+=' '+fe_rationale
  change='Correct CHEM-COMP-006 (#1237): reactivate only the fully qualified 0.01 M FeSO4·7H2O solution (in 0.02 N HCl) name as EXACT_SYNONYM using both primary recipes and the scoped preferred-owner check; preserve the superseded rejected object/source/history in separate immutable audit lineage. '
 else:
  assert r['index']==36 and [s['synonym_text'] for s in new['synonyms']]==[b['text'] for b in bic_rationales]
  new['notes']+=' '+bic_note
  change='Resolve CHEM-COMP-006 (#1237) per string: retain each bicarbonate footnote pointer as REJECTED_LABEL for the specific CO2-conditioned stock, with individual cited applicability reasons; preserve both exact labels/sources and positive NBRC1257/NBRC1321 stock union, literal added-water quantities and explicit CO2 saturation. '
 record_curation_event(new,curator='Codex /root/primary_context (worker01)',action='CORRECTED_PROPOSAL',changes=change+f'Correct {len(rows)} individually allowlisted MappingEvidence type(s) to LLM_SUGGESTION under #1226; all other evidence-object fields remain unchanged. Isolated successor only; no maintained owner, merge, or release approval.',previous_status=old['mapping_status'],new_status=new['mapping_status'],llm_assisted=True)
 assert new['curation_history'][:-1]==old['curation_history'];assert len(new['curation_history'])==len(old['curation_history'])+1
 assert new['components']==old['components'];assert new['identifier']==old['identifier'];assert new['preferred_term']==old['preferred_term']
 if r['index']==35:assert is_resolving_synonym(new['synonyms'][0])
 if r['index']==36:assert new['synonyms']==old['synonyms'];assert not any(is_resolving_synonym(s) for s in new['synonyms'])
 errors=validate_ingredient(new);assert not errors,[str(e) for e in errors]
 records.append((r,old,new))
 audit.append({'proposal_id':pid,'predecessor_path':r['payload_path'],'predecessor_sha256':r['payload_sha256'],'original_synonyms':old['synonyms'],'original_curation_history':old['curation_history'],'successor_synonyms':new['synonyms'],'meaning':'Original negative assertions and all old source/history values preserved as historical assertions; active dispositions are only the successor synonym rows. No duplicate active rejected row shadows the reactivated Fe label.'})
assert len(types)==5

# No writes to a candidate occur until all four pins, per-object changes and native validations pass.
out('qualifier-negative-audit-lineage-v1.json',{'author':'Codex /root/primary_context (worker01)','issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1237','records':audit})
stage=D/'science/native-staged-v1';stage.mkdir(exist_ok=False)
published=[]
for r,old,new in records:
 assert sha(I/r['payload_path'])==r['payload_sha256']
 p=stage/(r['proposal_id']+'.yaml');assert not p.exists()
 write_validated_ingredient(new,p)
 assert yaml.safe_load(p.read_text())==new
 final=D/'payloads'/p.name
 fd=os.open(final,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o644)
 with os.fdopen(fd,'wb') as f:f.write(p.read_bytes());f.flush();os.fsync(f.fileno())
 assert sha(final)==sha(p)
 published.append({'proposal_id':r['proposal_id'],'entry_index':r['index'],'predecessor':{'path':r['payload_path'],'sha256':r['payload_sha256']},'after':{'path':str(final),'sha256':sha(final)},'native_staged_path':str(p),'case_bindings':r['case_bindings'],'native_validation':'pass','native_guarded_write':'pass','exclusive_publication':'O_CREAT|O_EXCL, flushed/fsynced and byte-equal native output','complete_semantic_leaf_deltas':diffs(old,new)})
out('author-payload-receipt-v1.json',{'author':'Codex /root/primary_context (worker01)','created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_version':1,'input_check':{'path':str(D/'science/input-bindings-and-owned-name-check-v1.json'),'sha256':sha(D/'science/input-bindings-and-owned-name-check-v1.json')},'payloads':published,'mapping_evidence_type_changes':types,'four_histories_preserved_as_exact_prefix':True,'components_and_identifiers_unchanged':True,'independent_review_status':'pending; author validation is not independent review','limits':['No whole-owner, role, ontology grounding, merge, co-installation or release approval.','No maintained data or source-capture changes.','The helper does not claim hostile-concurrency atomicity; all candidate outputs are exclusive-create, pinned and read back.']})
print(json.dumps([{'proposal_id':r['proposal_id'],**r['after']} for r in published],indent=2))
