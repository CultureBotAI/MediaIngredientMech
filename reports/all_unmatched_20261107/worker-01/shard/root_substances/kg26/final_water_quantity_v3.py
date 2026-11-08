import pathlib,json,hashlib,datetime,copy,sys,subprocess,yaml
sys.path.insert(0,str(pathlib.Path('src').resolve()))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
R=pathlib.Path('reports/all_unmatched_20261107/worker-01');O=R/'shard/root_substances/kg26';C=O/'captures';P=O/'proposals'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')
save=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
D=json.loads((O/'decisions.fragment.json').read_text());E=json.loads((O/'evidence.fragment.json').read_text());Q=json.loads((O/'proposals.fragment.json').read_text());ds={d['allocation_index']:d for d in D['decisions']}
archive=O/'before-water-quantity-v3';archive.mkdir(exist_ok=False)
for n in ['decisions','evidence','proposals']:(archive/(n+'.fragment.json')).write_bytes((O/(n+'.fragment.json')).read_bytes())
# The source names a water grade. Its unspecified purity is not an unresolved identity.
cmd=['rg','--no-ignore','--hidden','-n','-i','deminerali[sz]ed water|deionized water|kgmicrobe.ingredient:demineralized','data/ingredients','docs/data/label_index.csv'];res=subprocess.run(cmd,capture_output=True,text=True)
records=[(p,yaml.safe_load(p.read_text())) for p in pathlib.Path('data/ingredients').rglob('*.yaml')]
tid='kgmicrobe.ingredient:demineralized_water';dest=pathlib.Path('data/ingredients/mapped/Demineralized_Water.yaml');assert not dest.exists() and not any(a.get('identifier')==tid for p,a in records)
owner=pathlib.Path('data/ingredients/mapped/Distilled_Water.yaml');owner_sha=sha(owner)
save(C/'water161-owner-search-v1.json',dict(at=now(),command=cmd,exit_code=res.returncode,stdout=res.stdout,stderr=res.stderr,ignored_files_included=True,whole_catalog_record_count=len(records),target_identifier=tid,identifier_absent=True,intended_path_absent=True,unchanged_distilled_owner_sha256=owner_sha))
cache=R/'shard/shared_reference_cache/shared-owner-primary-v1';rec=next(x for x in json.loads((cache/'primary-records.json').read_text()) if x['evidence_id']=='OLS:CHEBI:15377');cp=cache/rec['capture_path'];assert sha(cp)==rec['payload_sha256'];term=json.loads(cp.read_text())['_embedded']['terms'][0];assert term['label']=='water'
notes='The source grade demineralized water is explicitly named in all nine admitted ingredient1448 rows across DSMZ1191,1279,1600 and1793, including the source abbreviations H2O demin. and Aqua dem. It is represented as a distinct preparation-qualified solvent, with CHEBI15377 water as a broader molecular parent only. No ion-removal method, conductivity, resistivity, reagent standard, quantitative purity or universal sterility is asserted. The one sterile addition in DSMZ1600 retains that operational qualifier in its recipe; this owner does not globally equate sterile water, distilled water or tap water. The exact-name OLS search found TransformON c_ROHSUO, but TFO is outside the maintained OntologySourceEnum and its conductivity scope is not specified by these sources; the candidate is preserved as context rather than silently adopted or reported absent.'
u='https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1191.pdf'
a=dict(identifier=tid,preferred_term='Demineralized water',mapping_status='MAPPED',ingredient_type='SINGLE_INGREDIENT',synonyms=[dict(synonym_text='Demineralized water',synonym_type='EXACT_SYNONYM',source='mediadive.ingredient:1448; original DSMZ1191/1279/1600/1793')],ontology_mapping=dict(ontology_id='CHEBI:15377',ontology_label='water',ontology_source='CHEBI',mapping_quality='NARROW_MATCH',evidence=[dict(evidence_type='MANUAL_CURATION',source=u,notes=notes)]),supplied_form=[dict(name='Demineralized water',form='preparation-qualified water',notes='Source specifies the demineralized grade but no quantitative specification or treatment route. Sterility is occurrence-specific.')],occurrence_statistics=dict(total_occurrences=0,media_count=0),notes=notes,curation_history=[])
record_curation_event(a,curator='worker01_add_media_identity',action='CREATED',changes='Isolated source-grade identity proposal with NARROW_MATCH broad-parent grounding and mandatory registry sibling; preserve Distilled_Water and all historical rejected-label boundaries. No maintained writes or inherited membership reassignment.',new_status='MAPPED',llm_assisted=True)
pp=P/'Demineralized_Water.yaml';assert not pp.exists();write_validated_ingredient(a,pp);assert sha(owner)==owner_sha
d=ds[161];pid='KG26-PROP-161-IDENTITY';d['proposal_ids']=[pid];d['no_change_reason']=None;d['missing_requirement']=None;d['reasoning']+=' Completeness reassessment: '+notes+' A distinct guarded registry proposal supplies the supported water-grade identity; unspecified numerical purity is not an integration blocker.'
q=dict(proposal_id=pid,case_ids=[d['case_id']],description=notes,evidence_ids=d['evidence_ids'].copy(),owner_path=str(dest),kind='new_owner',before_sha256=None,after_capture=dict(root='artifact',path=str(pp.relative_to(R)),sha256=sha(pp)),identity_predicate_consequence='CHEBI15377 skos:broadMatch via NARROW_MATCH plus mandatory exact kgmicrobe.ingredient:demineralized_water registry sibling; no exact water-molecule or distilled-grade substitution.',applied=False);Q['proposals'].append(q)
proofs=[dict(index=161,after_path=str(pp),after_sha256=sha(pp),intended_owner=str(dest),before_sha256=None,distilled_owner_unchanged=True)]
# Preserve the native-reviewed original, then correct the representation of added water.
q=next(x for x in Q['proposals'] if x['proposal_id']=='KG26-PROP-170-FORMULATION');old=copy.deepcopy(q['after_capture']);bp=R/old['path'];assert sha(bp)==old['sha256'];a=yaml.safe_load(bp.read_text())
for c in a['components']:
 if c.get('concentration_unit') in ['G_PER_L','MG_PER_L']:c['concentration_unit'] += '_PREPARATION_WATER'
for s in a['synonyms']:
 if s['synonym_text']!='JCM976 mineral solution':s['synonym_type']='REJECTED_LABEL';s['source']+='; source-local cross-reference is non-resolving, exact JCM978 occurrence required'
a['notes']+=' Quantity units preserve masses per the listed one litre of preparation water, not a measured final litre after salts and KOH addition. Unqualified Medium No.976 cross-reference aliases are retained as REJECTED_LABEL; only the collection-qualified JCM976 name resolves globally.'
record_curation_event(a,curator='worker01_add_media_identity',action='CORRECTED',changes='Successor artifact corrects prior G_PER_L/MG_PER_L notation to explicit preparation-water units and marks collection-ambiguous cross-reference aliases REJECTED_LABEL. Prior proposal and native author reviews remain immutable; original maintained owner is unchanged.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
pp=P/'Mineral_Solution_See_Medium_No_976-v2.yaml';assert not pp.exists();write_validated_ingredient(a,pp);q['superseded_after_capture']=old;q['after_capture']=dict(root='artifact',path=str(pp.relative_to(R)),sha256=sha(pp));q['description']=a['notes'];ds[170]['reasoning']+=' Successor quantity representation uses explicit preparation-water units and non-resolving cross-reference labels; no final stock volume or globally applicable unqualified medium number is inferred.'
proofs.append(dict(index=170,old_artifact=old,after_path=str(pp),after_sha256=sha(pp),maintained_owner=q['owner_path'],maintained_owner_sha256=sha(pathlib.Path(q['owner_path'])),original_unchanged=sha(pathlib.Path(q['owner_path']))==q['before_sha256']))
save(C/'water-quantity-guards-v3.json',dict(at=now(),checks=proofs))
specs=[(161,'water161-owner-search-v1.json','local_validation','Ignored-inclusive exact grade and registry searches; all ingredient YAML identifiers checked',None),(161,'water161-ols-search-v1.json','ontology','Complete exact-name OLS query; one TFO candidate, not an absence result',None),(161,'water161-tfo-candidate-v1.json','ontology','Complete TransformON candidate annotation and conductivity scope; not adopted',None),(161,'water-quantity-guards-v3.json','local_validation','Guarded water-grade creation and unchanged current DistilledWater owner',None),(170,'water-quantity-guards-v3.json','local_validation','Immutable successor quantity and nonresolving-alias correction',None)]
for n,name,kind,loc,_ in specs:
 p=C/name;eid='KG26-FINAL-'+str(n)+'-'+p.stem;meta=p.with_suffix('.metadata.json');m=json.loads(meta.read_text()) if meta.exists() else {}
 E['evidence'].append(dict(evidence_id=eid,kind=kind,capture=dict(root='artifact',path=str(p.relative_to(R)),sha256=sha(p)),locator=loc,supports_or_contradicts=loc,url=m.get('url'),accessed_at=m.get('retrieved_at',now()),case_ids=[ds[n]['case_id']]))
 ds[n]['evidence_ids'].append(eid)
 for q in Q['proposals']:
  if q['proposal_id'] in ds[n]['proposal_ids']:q['evidence_ids'].append(eid)
eid='KG26-FINAL-WATER-PARENT';E['evidence'].append(dict(evidence_id=eid,kind='ontology',capture=dict(root='artifact',path=str(cp.relative_to(R)),sha256=sha(cp)),locator='Official exact CHEBI15377 term: molecular water only, no preparation grade',supports_or_contradicts='Supports broader molecular parent; does not establish distilled-grade equivalence or source purity.',url=rec['url'],accessed_at=rec['retrieved_at'],case_ids=[ds[161]['case_id']]))
ds[161]['evidence_ids'].append(eid);Q['proposals'][-1]['evidence_ids'].append(eid)
for d in D['decisions']:d['evidence_ids']=[x for x in d['evidence_ids'] if x!='KG26-COMP-NATIVE-IDENTITY-V2']
for q in Q['proposals']:q['evidence_ids']=[x for x in q['evidence_ids'] if x!='KG26-COMP-NATIVE-IDENTITY-V2']
for n,x in [('decisions',D),('evidence',E),('proposals',Q)]:save(O/(n+'.fragment.json'),x)
print(json.dumps(proofs,indent=2))
