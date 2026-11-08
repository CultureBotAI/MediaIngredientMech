"""Author a bounded successor observation; never modify published parent evidence."""
import copy, datetime, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
WORKER = HERE.parents[1]
REPO = next(p for p in HERE.parents if (p/'MAPPING_SEMANTICS.md').is_file())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
canon = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
def write(name, obj):
    (HERE/name).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n')
def cap(path):
    return {'root':'artifact','path':str(path.relative_to(WORKER)), 'sha256':sha(path)}

cases=json.loads((HERE/'cases.json').read_text())['cases']
old=json.loads((WORKER/'decisions.json').read_text())
previous={d['case_id']:d for d in old['decisions']}
lineage=json.loads((HERE/'provenance/source-associations.json').read_text())
evidence=[]
def local(eid,path,kind,summary,locator):
    evidence.append({'evidence_id':eid,'capture':cap(HERE/path),'kind':kind,'url':None,'locator':locator,'supports_or_contradicts':summary,'case_ids':[c['case_id'] for c in cases]})
def primary(eid,name,summary,locator):
    meta=json.loads((HERE/'captures'/f'{name}.metadata.json').read_text())
    assert meta['status_code']==200
    evidence.append({'evidence_id':eid,'capture':cap(HERE/'captures'/f'{name}.capture'),'kind':'primary_source','url':meta['url'],'accessed_at':meta['accessed_at'],'locator':locator,'supports_or_contradicts':summary,'case_ids':[c['case_id'] for c in cases]})

local('hx-frozen-cases','cases.json','source_snapshot','Exact unchanged two source-case objects, including raw labels, all owner candidates, consumed-name hits and inherited holds.','cases[0:2]; not an occurrence census')
local('hx-lineage','provenance/source-associations.json','source_snapshot','The frozen source-record values select medium14/solution20 by verified first-wins producer order. Equal-row matching alone is nonunique.','associations; exact JSON pointers and original observed_at; all owner hashes')
local('hx-lineage-validation','provenance/replay-validation.json','local_validation','All3344 retained medium response bodies checked against admitted manifest and ordered medium values;1214 compounds and5442 solutions replayed in exact insertion order using frozen producer functions. Pure extraction check, no cache or downstream rebuild.','status PASS; script and input hashes')
original=lineage['associations'][0]
evidence.append({'evidence_id':'hx-original-body','capture':cap(HERE/'provenance/captures/original-medium-14.body'),'kind':'primary_source','url':original['url'],'accessed_at':original['observed_at'],'locator':'/data/solutions/1/recipe/5 and /7; /data/medium/link','supports_or_contradicts':'Original retained 2026-11-05 response explicitly names both six-water reagents and links DSMZ_Medium14.pdf. Original timestamp and response bytes preserved.','case_ids':[c['case_id'] for c in cases]})
primary('hx-dsmz-recipe','original-dsmz-medium-14','Original DSMZ recipe specifies CoCl2 x6H2O0.20g and NiCl2 x6H2O0.02g in SL-4. This supplies the reagent-form witness missing from the earlier review.','Page1, Trace element solution SL-4 table; Co and Ni rows. Amounts locate context, not independent identity proof.')
primary('hx-current-rest','rest-medium-14','Current REST medium14 bytes equal the retained original response. Confirms current recipe lineage; not independent evidence from its source PDF.','/data/medium/link and /data/solutions/1/recipe')
primary('hx-current-solution','download-solution-20','Current official SL-4 download explicitly associates ingredient38/40 with recipe rows6/8 and six-water names. Same provider lineage as the original recipe.','recipe entries with compound_id38 and40')
for num,symbol,parentcas,parentchebi,mass in [(38,'Co','7646-79-9','35696','129.839'),(40,'Ni','7718-54-9','34887','129.599')]:
    primary(f'hx-ingredient-{num}',f'ingredient-{num}-download',f'Ingredient{num} retains explicit hexahydrate name but parent CAS{parentcas}, CHEBI{parentchebi}, formula Cl2{symbol}, mass{mass}. Secondary annotation conflict remains captured; these fields do not override the traced original recipe.','JSON name, group, cas_rn, chebi, formula, mass')
    primary(f'hx-page-{num}',f'ingredient-{num}',"Provider disclaimer says most identifiers and chemical parameters are automatically matched, not manually curated. This does not expose the provenance of each individual field.",'Disclaimer beneath identifiers and chemical parameters')
    primary(f'hx-group-{symbol}',f'group-{symbol}Cl2',('CoCl2 group shares parent CAS/formula/ChEBI/mass across4 forms.' if symbol=='Co' else 'NiCl2 group shares parent CAS/formula/ChEBI across5 forms; masses129.599 at80% and129.6 at20% are rounded parent-scale values, not hydration-specific.')+' Consistent with broad/group-level automatic annotation; inheritance mechanism is inference, not proven backend lineage.','Group distribution and ingredient table')
    for entry in evidence[-3:]:
        entry['case_ids']=[cases[0 if num==38 else 1]['case_id']]
local('hx-issue344','common/issue-344.json','native_record_review','Entire current CLOSED issue and both comments read. First comment explicitly notes genuine NiCl2 hexahydrate and Na2HPO4 dodecahydrate can carry parent mass. Atypical labels remain separate unresolved source investigations.','body; comments[0] and[1]; no issue reopening or blanket resolution')
local('hx-current-owners','common/current-owner-hashes.json','source_snapshot','Actual9 candidate owner files remain byte-identical to frozen baseline. Active hexahydrate owners and rejected tombstones were distinguished; owner match was not used as source-form evidence.','9 hashes and preserved owner copies')
local('hx-remote-owners','common/remote-main-owners.json','source_snapshot','Both active owners at captured remote main revision match assigned baseline bytes. No adoption of concurrent proposed payloads.','pinned current remote revision and two owner hashes')
old_e={e['evidence_id']:e for e in json.loads((WORKER/'evidence.json').read_text())['evidence']}
for eid in ('sa-chebi-53503','sa-chebi-53542'):
    e=copy.deepcopy(old_e[eid]);e['evidence_id']='hx-'+eid;e['case_ids']=[cases[0 if '53503' in eid else 1]['case_id']]
    e['supports_or_contradicts']='Reused unchanged primary ChEBI capture with original timestamp. Exact six-water chloride term and CAS support the ontology target after the source form is independently established by its original recipe; no source applicability inferred from an available owner.'
    assert sha(WORKER/e['capture']['path'])==e['capture']['sha256'];evidence.append(e)

decisions=[];associations=[]
for i,c in enumerate(cases):
    num=38 if i==0 else 40
    term='CHEBI:53503' if i==0 else 'CHEBI:53542'
    cas='7791-13-1' if i==0 else '7791-20-0'
    owner='data/ingredients/mapped/'+('Cobalt_chloride_hexahydrate.yaml' if i==0 else 'Nickel_II_chloride_hexahydrate.yaml')
    d=copy.deepcopy(previous[c['case_id']]); assert d['case_input_sha256']==hashlib.sha256(canon(c)).hexdigest()
    d.update(disposition='existing_identity_or_alias',reasoning=f'The exact frozen MediaDive{num} source_record is the first producer-selected compound occurrence in medium14, solution20 (SL-4), recipe row{6 if i==0 else 8}. Full admitted-generation replay and the retained original response establish that locator. The linked original DSMZ recipe explicitly supplies the hexahydrate; ChEBI independently supplies the exact hydrate term {term}/CAS{cas}. The parent CAS/formula/mass on the ingredient download are secondary annotation attached to a clearly specified reagent in this traced context, rather than unresolved source-form ambiguity. The automatic-matching disclaimer and group distributions are consistent with broad/group-level annotation; the exact backend assignment mechanism is not proven. No derived mmol/L, matching owner, supplier guess or equal-row choice establishes this identity.',applicability=f'Only {c["case_id"]}, source_id mediadive.ingredient:{num}, exact frozen row and reconstructed /data/solutions/1/recipe/{5 if i==0 else 7} in retained medium14 response. Original source response observed2026-11-05T06:23:28.282363+00:00; fresh PDF supplies primary recipe witness. Related provider views/PDF share source lineage and are not counted as independent chemical witnesses. Other MediaDive occurrences and atypical hydrate families are outside this reassessment.',evidence_ids=['hx-frozen-cases','hx-lineage','hx-lineage-validation','hx-original-body','hx-dsmz-recipe','hx-current-rest','hx-current-solution',f'hx-ingredient-{num}',f'hx-page-{num}',f'hx-group-{"Co" if i==0 else "Ni"}','hx-issue344','hx-current-owners','hx-remote-owners','hx-sa-chebi-'+term.split(':')[1]],proposal_ids=[],no_change_reason='Existing active exact hydrate owner already preserves the raw source label. The bounded source association is supplied separately; no owner bytes, global alias activation, canonical mapping or release selector change is proposed.',missing_requirement=None,independent_review={'status':'pending','evidence_ids':[]})
    d['supersedes_source_assessment_only']={'published_head':'d74ab6d48f6345260087cf973cadbe7b6269109f','path':str((WORKER/'decisions.json').relative_to(REPO)),'case_id':c['case_id'],'prior_disposition':'unresolved','reason':'New exact recipe provenance and original recipe witness resolve only this source-form question. Historical review bytes and all other assessments remain unchanged.'}
    d['retained_holds']={'whole_owner_export_disposition':'WITHHOLD','exact_frozen_review_key':'799' if i==0 else '2097','source_hold_recommendation':'Source-form ambiguity resolved for this exact case after separate review; coordinator must reconcile existing content-bound gates before any routing change. No runtime hold or selector is edited.','excluded_scopes':['Every other source case','Atypical/unattested hydrate forms in issue344','All unrelated owner aliases and provisional roles','Rejected legacy records and source-specific rejected labels','Any solution/stock or dissolved-species identity','Whole-row publication approval']}
    d['source_association_id']=f'hx-association-{num}'
    decisions.append(d)
    associations.append({'association_id':f'hx-association-{num}','case_id':c['case_id'],'case_input_sha256':d['case_input_sha256'],'source_id':c['source_case_id'],'raw_source_label':c['raw_source_label'],'source_record':c['original_kg_entry']['source_record'],'source_locator':lineage['associations'][i]['locator'],'source_response_sha256':original['body_sha256'],'owner_path':owner,'before_sha256':sha(REPO/owner),'identifier':term,'cas_rn':cas,'relation':'exact substance identity for the supplied reagent in this source case','association_kind':'existing_owner_source_association','after_capture':None,'maintained_mutation':False,'global_alias_activation':False,'export_approval':False,'evidence_ids':d['evidence_ids'],'retained_holds':d['retained_holds']})
write('decisions.json',{'schema_version':1,'worker_slot':9,'phase':'bounded_followup','scope':'Only these2 source assessments supersede corresponding historical decisions; other185 are not re-reviewed.','decisions':decisions})
write('existing-owner-associations.json',{'schema_version':1,'status':'proposed source associations pending separate skeptical review','associations':associations})
write('proposals.json',{'schema_version':1,'proposals':[],'reason':'No proposed YAML bytes; exact existing-owner/source associations are in existing-owner-associations.json.'})
write('evidence.json',{'schema_version':1,'evidence':evidence})
write('scientific-payload-hashes.json',{'algorithm':'SHA256 canonical JSON excluding only independent_review from each decision; associations file raw bytes','case_hashes':{d['case_id']:hashlib.sha256(canon({k:v for k,v in d.items() if k!='independent_review'})).hexdigest() for d in decisions},'association_file_sha256':sha(HERE/'existing-owner-associations.json'),'evidence_file_sha256_before_peer_attachment':sha(HERE/'evidence.json')})
print(json.dumps({'decisions':len(decisions),'associations':len(associations),'evidence':len(evidence),'owner_payload_proposals':0}))
