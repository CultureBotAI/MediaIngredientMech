from pathlib import Path
import copy,json,hashlib,datetime,sqlite3,subprocess,sys,yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
R=Path('reports/all_unmatched_20261107/worker-08');S=R/'successors/issue-1227-v1';M=S/'research/vitamins_mixtures';V=M/'final-v1';W=M/'final-v2'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def cap(p):return {'root':'artifact','path':str(Path(p).relative_to(R)),'sha256':h(p)}
def save(n,x):
 p=W/n
 if p.exists():assert read(p)==json.loads(json.dumps(x)),n
 else:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
now=read(W/'primary-form-facts.json')['accessed_at'];frozen={str(p):h(p) for p in V.rglob('*') if p.is_file()};save('v1-preservation-before.json',frozen)
P=read(V/'proposals.json');D=read(V/'decisions.json');AP={p['proposal_id']:copy.deepcopy(p) for p in P};A=read(M/'assignment.json')
primary={'accessed_at':now,'mechanism':'Author independently opened complete official TCI product pages through the web tool; bounded extracted factual paraphrases, not raw HTTP captures.','sources':[{'url':'https://www.tcichemicals.com/US/en/p/L0058','locator':'Product title/CAS lines175–190; general-information lines218–228','facts':['TCI L0058 explicitly names DL-alpha-lipoic acid and DL-thioctic acid; CAS1077-28-7, formulaC8H14O2S2.'],'limit':'Chemical form/registry bridge only; no DSMZ supplier procurement, purity or lot assertion.'},{'url':'https://www.tcichemicals.com/US/en/p/M0181','locator':'Product title/CAS lines175–184; general-information lines216–226','facts':['TCI M0181 explicitly names DL-2-methylbutyric acid and CAS116-53-0; formulaC5H10O2.'],'limit':'Chemical form/registry bridge only; no DSMZ supplier procurement, purity or lot assertion.'}],'failed_retrievals':[{'url':'https://www.ebi.ac.uk/ols4/api/ontologies/ncit/terms?obo_id=NCIT:C61595','result':'Web open inaccessible/internal error; local primary ontology inspected instead.'},{'url':'https://www.ebi.ac.uk/chebi/CHEBI:748116','result':'Web open inaccessible/internal error.'},{'url':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI%3A748116','result':'Web open inaccessible/internal error; no current online response claimed.'}],'recipe_sources':[]}
Ebase={e['evidence_id']:e for e in read(R/'successors/issue-1201-v1/evidence.json')['evidence']}
for eid,idx in [('vm-fetch-d4ba6de7b54bd50f',9),('vm-fetch-ca55b8a6996c682b',5)]:
 e=Ebase[eid];assert h(R/e['capture']['path'])==e['capture']['sha256'];raw=read(R/e['capture']['path']);primary['recipe_sources'].append({'evidence_id':eid,'capture':e['capture'],'original_accessed_at':e['accessed_at'],'url':e['url'],'locator':f'data.recipe[{idx}]','actual_source_row':raw['data']['recipe'][idx],'read_scope':'Complete recipe entries, source amounts/units, preparation steps and volume metadata read; source-batch representation retained.'})
save('primary-form-facts.json',primary)
lookup={'at':now,'databases':[],'terms':{},'searches':[],'decision':'CHEBI:748116 is the specifically racemic lipoic-acid concept: its DL synonyms and direct racemate superclass jointly establish the source-form scope. The generic CHEBI:16494 and NCIT:C61595 targets are not substituted. For explicit DL-2-methylbutyric acid, supplier CAS116-53-0 preserves the form; generic CHEBI:37070 has R/S children and is not exact racemate identity. No exact racemate term was established in these bounded local ChEBI/NCIt searches; this is not universal ontology absence.'}
if (W/'exact-form-ontology-lookup.json').exists():
 lookup=read(W/'exact-form-ontology-lookup.json')
else:
 for db,terms in [('chebi',['CHEBI:748116','CHEBI:60911','CHEBI:16494','CHEBI:37070','CHEBI:38655','CHEBI:45525']),('ncit',['NCIT:C61595'])]:
  path=Path('/Users/marcin/.data/oaklib')/(db+'.db');c=sqlite3.connect('file:'+str(path)+'?mode=ro',uri=True);lookup['databases'].append({'path':str(path),'sha256':h(path)})
  for term in terms:
   rows=c.execute('select predicate,value,object from statements where subject=?',(term,)).fetchall();lookup['terms'][term]=rows
   if term=='CHEBI:748116':
    lookup['lipoic_restrictions']={obj:c.execute('select predicate,value,object from statements where subject=?',(obj,)).fetchall() for pred,val,obj in rows if obj and obj.startswith('_:')}
  q="select subject,predicate,value from statements where (lower(value) like '%lipoic%' or lower(value) like '%thioctic%' or lower(value) like '%methylbut%') and (lower(value) like '%dl%' or lower(value) like '%racem%')"
  lookup['searches'].append({'database':db,'query':q,'rows':c.execute(q).fetchall(),'scope':'Candidates read; unrelated substituted chemicals, amides, hydroxy acids and larger derivatives are not the named free-acid components.'})
  q="select subject,predicate,value from statements where value in ('1077-28-7','cas:1077-28-7','116-53-0','cas:116-53-0')"
  lookup['searches'].append({'database':db,'query':q,'rows':c.execute(q).fetchall()})
  c.close()
 save('exact-form-ontology-lookup.json',lookup)
ids={'CHEBI:748116','cas:1077-28-7','cas:116-53-0'};catalog={str(f):yaml.safe_load(f.read_text()) for f in Path('data/ingredients').rglob('*.yaml')};lookuprows=[]
for f,a in catalog.items():
 if a.get('identifier') in ids:lookuprows.append({'path':f,'sha256':h(f),'identifier':a['identifier'],'mapping_status':a['mapping_status']})
combined=read(R/'successors/issue-1201-v1/proposals.json')['proposals'];overlay={p['proposal_id']:p for p in combined}
for other in ['organic_products','inorganic_forms']:
 other_data=read(S/'research'/other/'proposals.json')
 for p in (other_data['proposals'] if isinstance(other_data,dict) else other_data):overlay[p['proposal_id']]=p
for p in P:overlay[p['proposal_id']]=p
selectedhits=[]
for p in overlay.values():
 a=yaml.safe_load((R/p['after_capture']['path']).read_text())
 if a.get('identifier') in ids:selectedhits.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'identifier':a['identifier'],'mapping_status':a['mapping_status']})
assert not [r for r in lookuprows+selectedhits if r['mapping_status']!='REJECTED']
save('external-scope-owner-lookup.json',{'at':now,'method':'Path.rglob over all individual ingredient YAML files, independent of gitignore; every selected113 proposal payload parsed separately.','maintained_files':len(catalog),'selected_proposals':len(overlay),'identifiers':sorted(ids),'maintained_primary_hits':lookuprows,'selected_primary_hits':selectedhits,'scope':'No active primary-ID owner for these exact references in this bounded catalog/selected overlay. This is not absence of chemically related generic owners or universal absence.'})
changes={
 'vm-prop-new-29':{'index':9,'identifier':'CHEBI:748116','source':'Literal source component: (DL)-alpha-Lipoic acid, 50 mg per source batch, in DSMZ MediaDive solution 5980 (https://mediadive.dsmz.de/rest/solution/5980). Issue 1227 peer correction VM1227-PEER-001: exact racemic identity is CHEBI:748116 (lipoic acid, alpha), whose primary ChEBI release 255 statements include DL synonyms and a direct superclass CHEBI:60911 (racemate, an equimolar enantiomer mixture). It is distinct from the generic parent CHEBI:16494. TCI L0058 (https://www.tcichemicals.com/US/en/p/L0058) independently corroborates the explicit DL name and CAS1077-28-7 but does not establish DSMZ procurement. No active local owner holds CHEBI:748116, so EXTERNAL_TERM is deliberate. Literal amount, source preparation and all holds remain; no generic lipoic-acid components or owner roles are changed.'},
 'vm-prop-new-98':{'index':5,'identifier':'cas:116-53-0','source':'Literal source component: DL-2-Methylbutyric acid, 32.25 ml per source batch, in DSMZ MediaDive solution 608 (https://mediadive.dsmz.de/rest/solution/608). Issue 1227 peer correction VM1227-PEER-001: TCI M0181 (https://www.tcichemicals.com/US/en/p/M0181) explicitly identifies DL-2-methylbutyric acid as CAS116-53-0. This registry-form bridge supports the named DL ingredient, not a DSMZ supplier/product assignment. CHEBI:37070 is a broader concept with individual R/S children; bounded local ChEBI/NCIt lookup did not establish an exact racemate term. No active local owner holds cas:116-53-0, so EXTERNAL_TERM is deliberate. Literal amount, source preparation and all holds remain; no structure, role or owner-wide approval is introduced.'}}
rem=[]
for p in P:
 if p['proposal_id'] not in changes:continue
 x=changes[p['proposal_id']];old=yaml.safe_load((R/p['after_capture']['path']).read_text());a=copy.deepcopy(old);c=a['components'][x['index']];before=copy.deepcopy(c);c['component_id']=x['identifier'];c['reference_scope']='EXTERNAL_TERM';c['source']=x['source'];a['notes']=a['notes'].replace('Component references identify compatible active entities only after source-form review.','Component references identify source-compatible catalog or external entities only after source-form review.')
 record_curation_event(a,curator='all-unmatched-worker08-issue1227-vitamins',action='BOUNDED_COMPONENT_IDENTITY_CORRECTION',changes='Resolve routed VM1227-PEER-001 for '+c['component_name']+': replace the overly broad exact catalog reference with '+x['identifier']+' under EXTERNAL_TERM after primary source/form review. Preserve source amount, unit, all other components, complete stock identity, original history and every source/role/export hold. No new owner or supplier procurement assertion.',previous_status=a['mapping_status'],new_status=a['mapping_status'],llm_assisted=True)
 out=W/'proposed_owners'/Path(p['after_capture']['path']).name;assert not out.exists();write_validated_ingredient(a,out)
 p['after_capture']=cap(out);p['evidence_ids']+=['vm1227-v2-dl-primary','vm1227-v2-dl-ontology','vm1227-v2-external-scope']
 rem.append({'proposal_id':p['proposal_id'],'case_ids':p['case_ids'],'before_capture':AP[p['proposal_id']]['after_capture'],'after_capture':p['after_capture'],'component_index':x['index'],'before_component':before,'after_component':c,'finding_id':'VM1227-PEER-001','history_appended':True,'guarded_writer':'write_validated_ingredient','author':'/root/vitamins','independent_review':'pending'})
 # Exact semantic limits.
 for k in old:
  if k not in ['components','notes','curation_history']:assert a[k]==old[k],k
 assert a['curation_history'][:-1]==old['curation_history'] and a['curation_history'][-1]['llm_assisted'] is True
 for j,(b,n) in enumerate(zip(old['components'],a['components'])):
  if j!=x['index']:assert b==n
  else:
   for k in ['component_name','concentration_value','concentration_unit']:assert b[k]==n[k]
for d in D:
 ps=[p for p in d['proposal_ids'] if p in changes]
 if ps:
  d['reasoning']+=' Issue 1227 peer correction VM1227-PEER-001: the explicit DL component retains its literal name and amount, with exact external reference '+changes[ps[0]]['identifier']+' instead of the broader ChEBI catalog parent. Primary identity evidence and the exact-form lookup are bound; all original occurrence, source, role and export holds remain.'
  d['evidence_ids']+=['vm1227-v2-dl-primary','vm1227-v2-dl-ontology','vm1227-v2-external-scope']
save('proposals.json',P);save('decisions.json',D);save('peer-remediation.json',{'at':now,'finding_id':'VM1227-PEER-001','coordinator_routing':cap(S/'COORDINATOR-NEW-FINDINGS-v3.json'),'rows':rem,'unchanged_other_payloads':[{'proposal_id':p['proposal_id'],'after_capture':p['after_capture']} for p in P if p['proposal_id'] not in changes],'no_maintained_mutation':True})
C=read(V/'component-adjudications.json')
for r in C:
 if r['proposal_id'] in changes and r['component_index']==changes[r['proposal_id']]['index']:
  m=next(x for x in rem if x['proposal_id']==r['proposal_id']);r['superseded_final_v1_after']=copy.deepcopy(r['after']);r['after']=m['after_component'];r['outcome']='grounded_exact_external_entity';r['reason']=changes[r['proposal_id']]['source'];r['catalog_owners']=[];r['source_evidence_ids']+=['vm1227-v2-dl-primary','vm1227-v2-dl-ontology','vm1227-v2-external-scope']
save('component-adjudications.json',C)
B=read(V/'payload-assessments.json')
for r in B:
 if r['proposal_id'] in changes:
  m=next(x for x in rem if x['proposal_id']==r['proposal_id']);r['superseded_final_v1_capture']=r['successor_capture'];r['successor_capture']=m['after_capture'];r['changes'].append(changes[r['proposal_id']]['source']);r['new_catalog_references']-=1;r['exact_external_references']=1;r['primary_source_evidence_ids']+=['vm1227-v2-dl-primary','vm1227-v2-dl-ontology']
save('payload-assessments.json',B)
CA=read(V/'case-assessments.json');DM={d['case_id']:d for d in D}
for r in CA:
 d=DM[r['case_id']];r['appraisal']=d['reasoning'];r['source_evidence_ids']=d['evidence_ids']
save('case-assessments.json',CA)
for n in ['evidence-category-corrections.json','conditional-component-dependencies.json','conditional-deionized-water-dependency.json','completeness-adjudications.json','unsealed-draft-retention-limitation.json']:
 save(n,read(V/n))
DU=read(V/'promotion-selected-proposal-comparison.json');DU['own_successors_index']=cap(W/'proposals.json')
for r in DU['rows']:
 if r['proposal_id'] in changes:r['capture']=next(p['after_capture'] for p in P if p['proposal_id']==r['proposal_id'])
save('promotion-selected-proposal-comparison.json',DU)
ID=read(V/'issue-dispositions.json');ID['peer_followup']={'finding':'VM1227-PEER-001','status':'corrected_pending_independent_review','detail':'Two explicit DL references replaced by exact external identities; explicit racemate ontology CHEBI:748116 takes priority over CAS for lipoic acid; cas:116-53-0 preserves explicit DL-2-methylbutyric acid. All former generic reference claims are preserved only in final-v1 history.'}
for r in ID['issues']:
 if r['finding']=='IR003':r['detail']='236 newly supported references comprise 234 compatible catalog/conditional-overlay entities and two exact external entities after VM1227-PEER-001. All component-specific remaining form/preparation limits are retained; no role/export/withheld release.'
save('issue-dispositions.json',ID)
SL=read(V/'source-read-ledger.json');SL['successor_followup']={'at':now,'sources':cap(W/'primary-form-facts.json'),'ontology':cap(W/'exact-form-ontology-lookup.json'),'owner_scope':cap(W/'external-scope-owner-lookup.json'),'actual_inspection':'Both complete final-v1 payloads and complete MediaDive5980/608 recipe responses reread; both official TCI product pages opened and title/CAS information inspected; actual local ontology statements and racemate superclass inspected. Failed online ontology reads recorded separately.'};save('source-read-ledger.json',SL)
# Full selected overlay, using final other-cohort packets solely for native integrity.
for p in P:overlay[p['proposal_id']]=p
for p in overlay.values():catalog[p['owner_path']]=yaml.safe_load((R/p['after_capture']['path']).read_text())
viol=list(map(str,validate_component_partonomy(catalog.values())));assert not viol,viol
checks={'at':now,'status':'PASS','changed_guarded_payloads':2,'unchanged_payloads_from_v1':45,'full_selected_overlay_proposals':len(overlay),'partonomy_violations':viol,'overlay_input_indices':{str((S/'research'/c/'proposals.json').relative_to(R)):h(S/'research'/c/'proposals.json') for c in ['organic_products','inorganic_forms']},'schema_scope':'Both changed payloads passed guarded native schema; all45 other payload hashes equal final-v1 and retain its strict validation. Additional strict two-file run follows.','before_head':A['before_head'],'no_scientific_approval':True}
for p in P:
 old=AP[p['proposal_id']];assert all(p[k]==old[k] for k in ['proposal_id','kind','owner_path','before_sha256','case_ids'])
 if p['proposal_id'] not in changes:assert p['after_capture']==old['after_capture']
for d in D:
 old=next(x for x in read(V/'decisions.json') if x['case_id']==d['case_id'])
 for k in ['source','case_input_sha256','occurrence_ids','occurrence_context','preserved_native_decisions','preserved_holds','proposal_ids']:assert d.get(k)==old.get(k)
assert all(h(p)==sha for p,sha in frozen.items());checks['final_v1_all_files_unchanged']=True
save('validation.json',checks)
E=read(V/'evidence-additions.json')
for e in E['evidence']:
 name=Path(e['capture']['path']).name
 if (W/name).exists():e['capture']=cap(W/name)
 if e['evidence_id']=='vm1227-component-adjudication':e['locator']=e['supports_or_contradicts']='Every component index with operative final-v2 after snapshot: two explicit DL components use exact external identities; preserved final-v1 incorrect exact-parent claims are explicitly superseded.'
 if e['evidence_id']=='vm1227-payload-assessment':e['locator']=e['supports_or_contradicts']='All47 selected payload assessments with exact final-v2 captures for the two corrected DL references and unchanged45; no whole-owner or export approval.'
E['evidence'] += [{'evidence_id':'vm1227-v2-dl-primary','kind':'primary_source','capture':cap(W/'primary-form-facts.json'),'url':'https://www.tcichemicals.com/US/en/p/M0181','accessed_at':now,'locator':'TCI L0058 and M0181 product title/CAS sections; exact two original MediaDive recipe rows separately bound. Extracted facts, not raw responses.','supports_or_contradicts':'Supports explicit DL form/CAS bridges; does not establish procurement, lot or purity.'},{'evidence_id':'vm1227-v2-dl-ontology','kind':'ontology','capture':cap(W/'exact-form-ontology-lookup.json'),'url':None,'accessed_at':now,'locator':'Local primary ChEBI255 and NCIt26.02d statements; CHEBI748116→racemate60911, generic-parent contrasts, exact bounded name/CAS searches.','supports_or_contradicts':'Supports exact racemic lipoic acid identity under section3 priority, distinguishes generic parents, records candidate and search limits.'},{'evidence_id':'vm1227-v2-external-scope','kind':'local_validation','capture':cap(W/'external-scope-owner-lookup.json'),'url':None,'locator':'Ignored-inclusive2956 individual YAML primary identifiers and all113 selected payload identifiers.','supports_or_contradicts':'No active primary owner for selected exact external identities; no duplicate owner minted.'}]
save('evidence-additions.json',E)
print(json.dumps({'changed_payloads':[{'proposal_id':r['proposal_id'],'after_capture':r['after_capture']} for r in rem],'partonomy':len(viol),'v1_preserved':True}))
