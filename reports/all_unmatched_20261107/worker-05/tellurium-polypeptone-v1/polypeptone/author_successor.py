from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, copy, difflib, yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
S=Path('.temp/w05-tellurium-polypeptone-v1/polypeptone')
B=Path('reports/all_unmatched_20261107/worker-05')
PREFIX='tellurium-polypeptone-v1/polypeptone/'
AUTHOR='/root/polypeptone_supplement'
NOW=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
jsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(name,obj):
    p=S/name;p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists(),p;p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');return p
def cap(name):return {'root':'artifact','path':PREFIX+name,'sha256':sha(S/name)}
ps=json.loads((S/'input/selected-proposals.json').read_text())['proposals']
ds=json.loads((S/'input/selected-decisions.json').read_text())['decisions']
p0=next(p for p in ps if p['proposal_id']=='W05-FINAL-MAT-030')
before=B/p0['after_capture']['path'];assert sha(before)==p0['after_capture']['sha256']
old=yaml.safe_load(before.read_text());new=copy.deepcopy(old)
(S/'predecessor').mkdir(exist_ok=True)
(S/'predecessor/Polypeptone.yaml').write_bytes(before.read_bytes())
targets=['Polypepton (Nihon Pharm. Co.)','Polypepton (Nihon Seiyaku)']
for syn in new['synonyms']:
    if syn['synonym_text'] in targets:
        syn['synonym_type']='REJECTED_LABEL'
        syn['source'] += '; provenance-only identity hold under issue1202: retain this historical Nihon-qualified label, but do not resolve it globally to an unsettled Polypeptone owner or the dated BD blend. Wako 2001/2002 and Nihon 2007 sources support a casein-derived digest family; they do not establish the exact historical recipe product/version or equivalence to a particular Hipolypepton SKU. Current JCM181 names Hipolypepton (FUJIFILM Wako), a source-vintage conflict, not a historical equivalence bridge. This disposition does not reject the existence or chemistry of the Japanese product.'
new['notes']=new['notes'].replace('Current BD Polypeptone is an equal-parts pancreatic-casein/peptic-animal-tissue\n  digest blend.','The Thermo Fisher technical guide copyrighted 2019 describes the named BD Polypeptone product as an equal-parts pancreatic-casein/peptic-animal-tissue digest blend.')
new['notes']=new['notes'].replace('Current BD Polypeptone is an equal-parts pancreatic-casein/peptic-animal-tissue digest blend.','The Thermo Fisher technical guide copyrighted 2019 describes the named BD Polypeptone product as an equal-parts pancreatic-casein/peptic-animal-tissue digest blend.')
new['notes']=new['notes'].replace('Wako manufacturer casein-only starting-material description','Wako manufacturer casein-derived starting-material description')
new['notes'] += ('\n\nPolypeptone source-origin supplement under issue1202: the two Nihon-qualified Polypepton labels are retained as provenance-only REJECTED_LABEL entries. This prevents unsupported global resolution; it does not declare every Japanese Polypepton chemically distinct from every Hipolypepton. The 2001/2002 Wako and 2007 Nihon primary sources establish historical casein raw material and enzymatic processing, not a pure final casein composition or an occurrence-specific SKU bridge. Current JCM181 and related recipes naming FUJIFILM Wako Hipolypepton conflict with older Nihon Polypepton labels; preserve both source versions. The current Shioya product catalogues are separate version evidence.\n\nThe selected local identifier and self-only FALLBACK_REGISTRY remain unchanged solely for source-owner continuity in this isolated fragment. They are not accepted final grounding: POLYPEPTONE-001 remains open. FOODON:03315306 protein hydrolyzates supports a broader NARROW_MATCH relation for a settled named protein-hydrolysate preparation. MICRO:0000179 polypeptone has an explicit BD blended-digest definition and is a substantive exact-term candidate for that BD scope under MAPPING_SEMANTICS section3. The coordinator must settle the coupled owner scope and assess this exact-term priority before selecting final grounding; neither ontology label assigns bare MediaDive442 or historical Japanese occurrences to BD. Feasible BD-specific curation need not await resolution of every generic/Japanese occurrence: those routes may remain explicitly held. No competing worker union or arbitrary identifier is selected.\n\nThe 150 context rows are a read-only source-scope ledger, not a new membership count or approval. Historical occurrence_statistics 135/135, every old curation event, the three pre-existing Hipolypepton exclusions, ingredient roles, source quantities and all source/owner/export holds remain unchanged. No owner merge, maintained data change, source-case admission or release approval is conferred.')
event=record_curation_event(new,curator=AUTHOR+'; W05 report-only source-origin supplement',action='CORRECTED',changes='Withdraw unsupported global resolution of the two Nihon-qualified Polypepton aliases while preserving their exact text/source provenance; date the BD blend claim to the 2019 technical guide and qualify historical casein-derived material scope. Preserve local identity/grounding continuity with POLYPEPTONE-001 explicitly open pending coupled scope and MICRO:0000179 exact-term-priority review. Preserve all previous history/statistics, original Hipolypepton exclusions, source forms/quantities and holds. No maintained record or union applied.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True,llm_model='gpt-6',timestamp=NOW)
out=S/'proposed/Polypeptone.yaml';write_validated_ingredient(new,out)
assert new['identifier']==old['identifier'] and new['ontology_mapping']==old['ontology_mapping']
assert new['curation_history'][:-1]==old['curation_history']
assert new['occurrence_statistics']==old['occurrence_statistics']
assert new['nutritional_roles']==old['nutritional_roles']
assert [s for s in new['synonyms'] if s['synonym_text'].startswith('Hipolypepton')]==[s for s in old['synonyms'] if s['synonym_text'].startswith('Hipolypepton')]
assert all(s['synonym_type']=='REJECTED_LABEL' for s in new['synonyms'] if s['synonym_text'] in targets)
changed_fields=[k for k in set(old)|set(new) if old.get(k)!=new.get(k)]
assert set(changed_fields)=={'synonyms','notes','curation_history'}
(S/'field-diff.patch').write_text(''.join(difflib.unified_diff(before.read_text().splitlines(True),out.read_text().splitlines(True),fromfile=str(before),tofile=str(out))))
save('field-diff.json',{'author':AUTHOR,'timestamp':NOW,'predecessor':p0['after_capture'],'after':cap('proposed/Polypeptone.yaml'),'changed_top_level_fields':sorted(changed_fields),'changed_synonym_texts':targets,'all_prior_history_exact':True,'historical_statistics_exact':True,'ontology_mapping_exact':True,'identifier_exact':True,'three_prior_hipolypepton_exclusions_exact':True,'other_fields_exact':True,'curation_event':event})
save('guarded-write-result.json',{'at':NOW,'author':AUTHOR,'writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','schema':'src/mediaingredientmech/schema/mediaingredientmech.yaml','schema_sha256':sha('src/mediaingredientmech/schema/mediaingredientmech.yaml'),'record':cap('proposed/Polypeptone.yaml'),'closed_schema_errors':[str(e) for e in validate_ingredient(new)],'guard_checks':'all asserted preservation checks passed','components':'unchanged absent; conditional BD component obligations documented separately, not added to an unsettled selected owner'})
evidence=[]
for name,kind,claim in [
 ('context-ledger.json','source_snapshot','All150 frozen context rows and exact complete recipes; lexical grouping and source qualifiers preserved without adopting external cases or approving membership.'),
 ('field-diff.json','local_validation','Exact selected source-origin field changes and preservation assertions.'),
 ('guarded-write-result.json','local_validation','Native guarded closed-schema write of the one changed selected payload.'),
]:
 evidence.append({'evidence_id':'SUPPLEMENT-POLY-'+name.split('.')[0].upper(),'kind':kind,'capture':cap(name),'url':None,'locator':name,'supports_or_contradicts':claim,'case_ids':p0['case_ids'],'accessed_at':NOW,'author':AUTHOR})
for receipt_path in sorted((S/'captures').glob('*.receipt.json')):
    receipt=json.loads(receipt_path.read_text());body=S/'captures'/receipt['path']
    if not body.exists():continue
    eid='SUPPLEMENT-POLY-CAP-'+receipt['path'].upper().replace('.','-')
    isontology=any(z in receipt['path'] for z in ['foodon','micro-polypeptone','ontology-all'])
    excluded=receipt['path'] in ['togoM2.json','togoM90.json','togoM2-page.html','togoM90-page.html']
    evidence.append({'evidence_id':eid,'kind':'unsuccessful_search' if excluded else 'ontology' if isontology else 'primary_source','capture':cap('captures/'+receipt['path']),'url':receipt['url'],'locator':'Complete response bytes; claim-level applicability is specified in source-assessment.json and context-ledger.json.','supports_or_contradicts':'Source membership/formulation evidence only within its named product and dated source scope; no wholesale source-case or owner approval.' if not excluded else 'Application page response without extracted recipe data; no identity claim supported.','case_ids':p0['case_ids'],'accessed_at':receipt['accessed_at'],'author':AUTHOR,'receipt':cap('captures/'+receipt_path.name)})
newp=copy.deepcopy(p0);newp['after_capture']=cap('proposed/Polypeptone.yaml');newp['description'] += ' Supplement: withdraw the two unsupported globally resolving Nihon-qualified Polypepton aliases as provenance-only; date BD evidence, preserve all historical origin fields and exact prior exclusions. Final grounding POLYPEPTONE-001 remains OPEN pending the source-supported coupled owner scope and MICRO exact-term-priority assessment; this self-only fragment is not final grounding approval.'
newp['supplement_author']=AUTHOR;newp['supplement_predecessor_capture']=p0['after_capture'];newp['supplement_predecessor_copy']=cap('predecessor/Polypeptone.yaml');newp['supplement_predecessor_proposal_sha256']=jsha(p0)
newp['supplement_scope']='Only W05 cases127/160 source-origin Polypeptone safety correction; no W06 union, owner merge, occurrence adoption or whole-owner/export approval.'
newp['final_grounding_status']='OPEN: POLYPEPTONE-001; source-origin local identity is continuity only, not accepted final self-only grounding.'
newp['evidence_ids'] += [e['evidence_id'] for e in evidence]
newp['independent_review']={'status':'pending_exact_successor_review','evidence_ids':[]}
changes=[]
for d0 in ds:
    if d0['case_index'] not in [127,160]:continue
    d=copy.deepcopy(d0)
    addition=(' Supplement: the Polypeptone owner fragment retains all original Hipolypepton exclusions and now withdraws the two unsupported globally resolving Nihon Polypepton aliases as provenance-only source labels. Historical primary sources support a casein-derived Nihon product family, not pure final casein or an exact recipe-vintage/SKU bridge; current JCM181 names Hipolypepton (FUJIFILM Wako), so older Nihon labels cannot be globally reconciled by a renamed recipe alone. MediaDive442 still provides no supplier. POLYPEPTONE-001 final grounding is OPEN: the supported FOODON broader relation and the MICRO0000179 exact BD-blend candidate require coordinator selection of the coupled owner/product scope. Feasible source-supported BD curation may proceed separately while ambiguous routes remain held. No assigned case, raw label, occurrence, quantity, source hold or owner/release admission is changed by this supplement.')
    d['reasoning'] += addition;d['applicability'] += addition
    d['supplement_reassessment']={'author':AUTHOR,'at':NOW,'predecessor_decision_canonical_sha256':jsha(d0),'selected_proposal_id':p0['proposal_id'],'final_grounding_status':'OPEN POLYPEPTONE-001; coupled scope and exact-term priority pending','quantity_scope':'No quantity edits; read-only M122 context discrepancy reported outside W05 case ownership.','new_case_adopted':False}
    d['evidence_ids'] += [e['evidence_id'] for e in evidence]
    d['independent_review']={'status':'pending_exact_successor_review','evidence_ids':[]}
    for issue in ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1202#issuecomment-6718777428','https://github.com/CultureBotAI/MediaIngredientMech/issues/1226#issuecomment-6718777633']:
        if issue not in d['issue_refs']:d['issue_refs'].append(issue)
    changes.append(d)
save('proposals.json',{'schema_version':1,'proposals':[newp]})
save('decisions.json',{'schema_version':1,'decisions':changes})
save('evidence.json',{'schema_version':1,'evidence':evidence})
save('scope-accounting.json',{'base_head':'76bca688b4f55e8bdf791079df8d4156cded6c4c','author':AUTHOR,'selected_changed_proposals':['W05-FINAL-MAT-030'],'selected_changed_case_indices':[127,160],'selected_changed_case_ids':p0['case_ids'],'read_unchanged_proposal':next(p for p in ps if p['proposal_id']=='W05-FINAL-MAT-029'),'read_unchanged_case':next(d for d in ds if d['case_index']==33),'context_occurrence_rows':150,'context_rows_are_new_case_adoptions':False,'baseline_case_total_not_recounted_here':188,'baseline_original_proposal_total_not_recounted_here':138,'root_obligation':'Rerun full 188-case/138-origin accounting with these same-ID replacements; this lane does not force campaign counts or reauthor unchanged historical support.'})
print(json.dumps({'after_sha256':sha(out),'changed_cases':[d['case_index'] for d in changes],'evidence_entries':len(evidence),'changed_fields':changed_fields},indent=2))
