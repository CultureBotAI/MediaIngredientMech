from pathlib import Path
import json,hashlib,datetime,shutil,sys,yaml,copy
sys.path.insert(0,'src')
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
O=Path('reports/all_unmatched_20261107/worker-02');R=O/'continuation-1201-v1/a';V=R/'revisions/draft-v3-component-references';V.mkdir(parents=True,exist_ok=False)
for n in ['decisions.json','evidence.json','proposals.json','reassessments.json','component-owner-review.json']:shutil.copy2(R/n,V/n)
L=lambda p:json.loads(p.read_text());S=lambda b:hashlib.sha256(b).hexdigest();C=lambda p:{'root':'artifact','path':str(p.relative_to(O)),'sha256':S(p.read_bytes())}
D=L(R/'decisions.json');E=L(R/'evidence.json');P=L(R/'proposals.json');RA=L(R/'reassessments.json');CO=L(R/'component-owner-review.json')
# Manual exact source-form adjudications; no fuzzy inference of hydrate, stock, brand or stereochemistry.
M={
'FeSO4・7H2O':('Feso4_X_7_H2o.yaml','CHEBI:75836'),
'Fe(NH4)2(SO4)2 x 7 H2O':('Fe_Nh42_So42_X_7_H2o.yaml','CHEBI:131378'),
'Na2MoO4・2H2O':('Na2moo4_X_2_H2o.yaml','CHEBI:75213'),
'MnCl2・4H2O':('Mncl2_X_4_H2o.yaml','CHEBI:86368'),
'ZnSO4・7H2O':('Znso4_X_7_H2o.yaml','CHEBI:32312'),
'CuCl2・2H2O':('Cucl2_X_2_H2o.yaml','CHEBI:86318'),
'FeCl3・6H2O':('Fecl3_X_6_H2o.yaml','CHEBI:86254'),
'CoSO4・7H2O':('Coso4_X_7_H2o.yaml','CHEBI:91244'),
'Na2S2O3・5H2O':('Na2s2o3_X_5_H2o.yaml','CHEBI:32150'),
'KBr':('Kbr.yaml','CHEBI:32030'),
'NaH2PO4・H2O':('Sodium_phosphate_monobasic_monohydrate.yaml','CHEBI:114249'),
'NaNO3':('Nano3.yaml','CHEBI:63005'),
'MgSO4 · 7H2O':('Mgso4_X_7_H2o.yaml','CHEBI:31795'),
'CoCl2 · 6H2O':('Cobalt_chloride_hexahydrate.yaml','CHEBI:53503'),
'MnSO4 · 4 H2O':('Mnso4_X_4_H2o.yaml','CHEBI:86358'),
'CaSO4・2H2O':('Caso4_X_2_H2o.yaml','CHEBI:32583'),
'CAPSO':('Capso.yaml','CHEBI:183882'),
'Tween 80':('Tween_80.yaml','CHEBI:53426'),
'Yeast extract':('Yeast_Extract.yaml','FOODON:03315426'),
'yeast extract':('Yeast_Extract.yaml','FOODON:03315426'),
'peptone':('Peptone.yaml','MICRO:0000178')}
owners={};changes=[];touched=set()
for raw,(fn,ident) in M.items():
 p=Path('data/ingredients/mapped')/fn;obj=yaml.safe_load(p.read_bytes());assert obj['identifier']==ident and obj['mapping_status']=='MAPPED'
 dest=R/'before/mapped'/fn
 if not dest.exists():shutil.copy2(p,dest)
 owners[raw]={'path':str(p),'sha256':S(p.read_bytes()),'capture':C(dest),'record':obj,'identity_reason':'Source names the same exact fixed hydrate/form, common named buffer/material or unqualified biological ingredient. No hydration, assay, source brand or stereochemical specificity is added.'}
for p in P['proposals']:
 record=yaml.safe_load((O/p['after_capture']['path']).read_bytes());changed=[]
 for c in record.get('components',[]):
  raw=c['component_name']
  if c['reference_scope']=='UNMAPPED' and raw in M:
   owner=owners[raw];old=copy.deepcopy(c);c['component_name']=owner['record']['preferred_term'];c['component_id']=owner['record']['identifier'];c['reference_scope']='MIM_CATALOG';changed.append({'source_component':raw,'before':old,'after':copy.deepcopy(c),'owner_path':owner['path'],'owner_sha256':owner['sha256'],'owner_capture':owner['capture']})
 if not changed:continue
 previous=p['after_capture'];record_curation_event(record,curator='codex_worker02_research_a_continuation1201',action='CORRECTED',changes='Independent reviewer B requested complete assessment of known components. Resolve verified source-form parts to actual active MIM owners without changing source amounts or inferring any new formulation. '+', '.join(x['source_component'] for x in changed),previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
 dest=R/'after-v3'/Path(p['owner_path']).name;write_validated_ingredient(record,dest);p['after_capture']=C(dest)
 changes.append({'proposal_id':p['proposal_id'],'before_capture':previous,'after_capture':p['after_capture'],'component_changes':changed});touched.update(p['case_ids'])
 for x in changed:CO.append({'proposal_id':p['proposal_id'],'component':x['after'],'owner_path':x['owner_path'],'owner_sha256':x['owner_sha256'],'owner_capture':x['owner_capture'],'identity_scope':'Explicit fixed source form or common named ingredient; no whole-stock identity is inferred.'})
(R/'component-owner-review.json').write_text(json.dumps(CO,indent=2,ensure_ascii=False)+'\n')
for e in E['evidence']:
 if e['capture']['path']=='continuation-1201-v1/a/component-owner-review.json':e['capture']=C(R/'component-owner-review.json')
left={}
for p in P['proposals']:
 rec=yaml.safe_load((O/p['after_capture']['path']).read_bytes())
 for c in rec.get('components',[]):
  if c['reference_scope']=='UNMAPPED':left.setdefault(c['component_name'],[]).append(p['proposal_id'])
limitations={
'Na2B4O7・10H2O':'Current CHEBI131366 owner label matches decahydrate but inherited formula 10H2O.H4B4O9.2Na does not transparently match source Na2B4O7·10H2O; defer this exact component reference pending ontology/structure reconciliation, while source part remains recorded.',
'Resazurin':'The source name does not select free resazurin versus commonly supplied sodium salt; do not infer counterion from the generic input name.',
'casamino acids':'Actual Casamino_Acids and Casein_Peptone share FOODON03315719 at nonexact/nearby scope. Do not use their broad common identity to assert exact acid-hydrolysate versus enzymatic-peptone part equivalence.',
'Peptone from casein':'Actual Casein_Peptone shares FOODON03315719 with distinct Casamino_Acids at broad/nearby scope; preserve the specified source ingredient until a precise local component identity is curated.',
'Glucose':'Source does not establish anomeric/specific supplied form; leave its literal named component without adding stereochemical specificity.',
'Sodium glutamate':'Source does not explicitly select stereochemistry or hydration; existing L-specific/hydrate owners must not fill those gaps.',
'sodium acetate':'Source does not select anhydrous versus trihydrate material; preserve salt label without choosing a fixed supplied form.',
'Ca(NO3)2':'Source does not select hydration; existing anhydrous/tetrahydrate forms remain distinct.',
'CaCl2':'Source does not select hydration; existing anhydrous/dihydrate/hexahydrate candidates remain distinct.',
'VOSO4・xH2O':'Variable-hydrate candidate exists but this bounded component review does not assume a specific vanadyl-sulfate hydration/registry interpretation; source x is retained.'}
receipt={'reviewer':'/root/research_b','applied_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changes':changes,'unmapped_components_remaining':[{'name':n,'proposal_ids':ps,'reason':limitations.get(n,'Source-local preparation, product/brand or literal chemical uncertainty is retained; no exact whole-preparation/grade component identity is established by a name match to a generic ingredient.')} for n,ps in left.items()],'prior_proposals_sha256':S((V/'proposals.json').read_bytes()),'full_owner_approval':False}
(R/'review-b-revision-02.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
eid='a2-review-b-exact-component-references';E['evidence'].append({'evidence_id':eid,'kind':'local_validation','capture':C(R/'review-b-revision-02.json'),'locator':'Exact source-form component changes, current owner byte bindings, and remaining unresolved scope explanations','supports_or_contradicts':'Author response to independent reviewer B; mechanically preserved all prior after paths, guard-wrote versioned successors, and resolved explicitly verified components without inventing hydrate/stock/brand equivalence.','url':None,'case_ids':sorted(touched)})
for d in D['decisions']:
 if d['case_id'] in touched:d['evidence_ids'].append(eid)
for p in P['proposals']:
 if any(p['proposal_id']==x['proposal_id'] for x in changes):p['evidence_ids'].append(eid)
for a in RA['assessments']:
 if a['case_id'] in touched:a['component_reference_revision']='See a2-review-b-exact-component-references; explicit exact hydrate/common ingredient refs added, unresolved scope left stated.'
for n,o in [('decisions.json',D),('evidence.json',E),('proposals.json',P),('reassessments.json',RA)]: (R/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
print('changed_payloads',len(changes),'resolved_parts',sum(len(x['component_changes']) for x in changes),'cases',len(touched))
