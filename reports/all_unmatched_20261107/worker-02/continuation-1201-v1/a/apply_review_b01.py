from pathlib import Path
import copy,json,hashlib,datetime,shutil,sys,yaml
sys.path.insert(0,'src')
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
O=Path('reports/all_unmatched_20261107/worker-02');R=O/'continuation-1201-v1/a';V=R/'revisions/draft-v2-source-only-duplication';V.mkdir(parents=True,exist_ok=False)
for n in ['decisions.json','evidence.json','proposals.json','reassessments.json','component-owner-review.json','proposal-source-scopes.json']:shutil.copy2(R/n,V/n)
shutil.copytree(R/'after',V/'after')
L=lambda p:json.loads(p.read_text());S=lambda b:hashlib.sha256(b).hexdigest();C=lambda p:{'root':'artifact','path':str(p.relative_to(O)),'sha256':S(p.read_bytes())}
D=L(R/'decisions.json');E=L(R/'evidence.json');P=L(R/'proposals.json');RA=L(R/'reassessments.json');SS=L(R/'proposal-source-scopes.json')
indices={x['index']:x['decision']['case_id'] for x in L(R/'assigned.json')['cases']};bycase={d['case_id']:d for d in D['decisions']}
retire={p['proposal_id'] for p in P['proposals'] if p['proposal_id'].endswith('sulfuric-acid-2m') or p['proposal_id']=='a2-proposal-jcm1483-concentrated-sulfuric-acid'}
old=[p for p in P['proposals'] if p['proposal_id'] in retire];assert len(old)==6
source_scopes=[s for s in SS if s['proposal_id'] in retire]
base=next(p for p in old if p['proposal_id'].endswith('2609-sulfuric-acid-2m'));record=yaml.safe_load((O/base['after_capture']['path']).read_bytes())
slug='sulfuric_acid_2m_preparation';name='2 M sulfuric acid preparation (solvent unspecified)';pid='a2-proposal-sulfuric-acid-2m-preparation';scope='The five frozen occurrences in TOGO M2609, M3032, M3119, M3141 and M3252 explicitly name2M H2SO4 preparations. Source IDs alone do not establish distinct substances, so one record represents their common stated analytical-concentration scope. Solvent, assay tolerance and unlisted constituents remain unknown; complete-formulation equivalence or interchangeability is not asserted. Every original occurrence and receiving-medium context is retained separately. No receiving dose is reinterpreted as stock concentration.'
record['identifier']='kgmicrobe.ingredient:'+slug;record['preferred_term']=name;record['ontology_mapping'].update(ontology_id=record['identifier'],ontology_label=name)
urls=[f'https://togomedium.org/medium/M{x}' for x in [2609,3032,3119,3141,3252]]
record['ontology_mapping']['evidence']=[{'evidence_type':'CURATOR_JUDGMENT','source':u,'notes':scope+' No verified eligible exact whole-preparation ontology term or held whole-preparation owner was established; the pure acid CURIE is only a component reference.'} for u in urls]
record['notes']=scope+' Raw source labels remain in source evidence and are not activated as global aliases. All inherited release holds remain.'
record['component_assertion']['evidence']=[{'evidence_type':'RECIPE_SOURCE','source':u,'source_record':name,'notes':scope} for u in urls]
record['curation_history']=[];record_curation_event(record,curator='codex_worker02_research_a_continuation1201',action='PROPOSED_NEW_INGREDIENT',changes='Independent reviewer B identified unsupported source-ID-only splitting; consolidated bounded known2M preparation. '+scope,new_status='MAPPED',llm_assisted=True)
p=R/'after'/f'{slug}.yaml';write_validated_ingredient(record,p)
new=copy.deepcopy(base);new.update(proposal_id=pid,description=scope,owner_path=f'data/ingredients/mapped/{slug}.yaml',after_capture=C(p),evidence_ids=sorted({eid for q in old if q['case_ids']==[indices[17]] for eid in q['evidence_ids']}))
new['review_revision']='B finding: consolidate known identical concentration scope; distinct source IDs do not by themselves create distinct material identities.'
P['proposals']=[q for q in P['proposals'] if q['proposal_id'] not in retire]+[new]
for q in old:(O/q['after_capture']['path']).unlink() # bytes retained in V/after; only withdrawn active artifact paths removed
x=bycase[indices[17]];x['proposal_ids']=[pid];x['reasoning']=scope
x=bycase[indices[46]];shared='b2-proposal-concentrated_sulfuric_acid_assay_unspecified';x['proposal_ids']=[shared];x['reasoning']='JCM1483 SolutionC explicitly uses concentrated H2SO4 without numerical assay. Its bounded stated preparation scope matches the shared concentrated-sulfuric-acid record authored by B; no distinct substance is justified solely by its source ID. Preserve the separate original JCM source and occurrence. This link asserts neither equal commercial assay nor complete-formulation equivalence, and does not assign100% acid, a solvent or a molarity.'
for a in RA['assessments']:
 if a['index']==17:
  a['reason']=bycase[indices[17]]['reasoning'];a['proposal_ids']=[pid]
  for s in a['scoped_outcomes']:s['proposal_id']=pid
 if a['index']==46:a['reason']=bycase[indices[46]]['reasoning'];a['proposal_ids']=[shared];a['independent_review_route']='C must review this cross-author B target; B cannot approve its own target through A46.'
SS=[x for x in SS if x['proposal_id'] not in retire]+[{'proposal_id':pid,'source_urls':urls,'scope':scope,'indices':[17],'record_identifier':record['identifier']},{'proposal_id':shared,'source_urls':['https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1483'],'scope':bycase[indices[46]]['reasoning'],'indices':[46],'shared_external_author':'B; root adds reciprocal case/evidence backlinks and C reviews'}]
co=L(R/'component-owner-review.json');template=next(x for x in co if x['proposal_id']==base['proposal_id']);co=[x for x in co if x['proposal_id'] not in retire];template=copy.deepcopy(template);template['proposal_id']=pid;co.append(template)
(R/'component-owner-review.json').write_text(json.dumps(co,indent=2,ensure_ascii=False)+'\n')
for e in E['evidence']:
 if e['capture']['path']=='continuation-1201-v1/a/component-owner-review.json':e['capture']=C(R/'component-owner-review.json')
receipt={'reviewer':'/root/research_b','applied_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'findings':[{'finding':'source-ID-only2Mstock splitting','disposition':'five retired proposals replaced with one bounded known2M preparation','retired':[x['proposal_id'] for x in old if x['case_ids']==[indices[17]]],'replacement':pid},{'finding':'concentratedacid overlap withB','disposition':'A duplicate withdrawn; A46 explicitly links B shared target; root adds reciprocal backlinks and C independently reviews','retired':'a2-proposal-jcm1483-concentrated-sulfuric-acid','replacement':shared}],'prior_proposals_sha256':S((V/'proposals.json').read_bytes()),'unchanged_source_field_assertion':'case IDs, digests, raw labels and occurrence lists unchanged; inherited holds retained'}
(R/'review-b-revision-01.json').write_text(json.dumps(receipt,indent=2)+'\n')
eid='a2-review-b-source-scope-consolidation';E['evidence'].append({'evidence_id':eid,'kind':'local_validation','capture':C(R/'review-b-revision-01.json'),'locator':'Both findings and explicit successor targets','supports_or_contradicts':'Author response to independent reviewer B; not independent approval. Preserved draft bytes precede consolidation; no scientific formula/assay guessed.','url':None,'case_ids':[indices[17],indices[46]]})
for i in [17,46]:bycase[indices[i]]['evidence_ids'].append(eid)
new['evidence_ids'].append(eid)
for n,o in [('decisions.json',D),('evidence.json',E),('proposals.json',P),('reassessments.json',RA),('proposal-source-scopes.json',SS)]: (R/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
print('active proposals',len(P['proposals']),'active after',len(list((R/'after').glob('*.yaml'))),'new',new['after_capture'])
