import json,hashlib,importlib.util,sys
from pathlib import Path
from datetime import datetime,timezone
import yaml
R=Path.cwd();S=R/'.temp/w05-buffer-parts-v1';Q=S/'review';B=R/'reports/all_unmatched_20261107/worker-05';P=S/'polypeptone-final'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def j(p):return json.loads(Path(p).read_text())
def oh(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def b(p):return {'path':str(Path(p).relative_to(R)) if Path(p).is_relative_to(R) else str(p),'sha256':h(p)}
old=B/'tellurium-polypeptone-v1/polypeptone/proposed/Polypeptone.yaml';f=P/'proposed-v2/Polypeptone.yaml';a=yaml.safe_load(old.read_text());z=yaml.safe_load(f.read_text())
assert z['identifier']==a['identifier']=='kgmicrobe.ingredient:polypeptone';m=z['ontology_mapping'];assert [m[k] for k in ['ontology_id','ontology_label','ontology_source','mapping_quality']]==['mesh:D010461','Peptones','MESH','NARROW_MATCH']
assert z['curation_history'][:len(a['curation_history'])]==a['curation_history'];assert m['evidence'][:-1]==a['ontology_mapping']['evidence'];assert m['evidence'][-1]['evidence_type']=='LLM_SUGGESTION'
protected={k:a.get(k)==z.get(k) for k in a.keys()|z.keys() if k not in ['ontology_mapping','curation_history','notes','synonyms']};assert all(protected.values())
labels=['Polypeptone peptone (BD-BBL)','Polypeptone Peptone (BD 211910)','Polypeptone (BBL)'];syn=[]
assert len(a['synonyms'])==len(z['synonyms'])
for x,y in zip(a['synonyms'],z['synonyms']):
 assert x['synonym_text']==y['synonym_text']
 if x['synonym_text'] in labels:
  assert y['synonym_type']=='REJECTED_LABEL' and y['source'].startswith(x['source']);syn.append({'before':x,'after':y})
 else:assert x==y
assert len(syn)==3 and sum(x['synonym_type']=='REJECTED_LABEL' for x in z['synonyms'])==8
builder=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py');assert h(builder)==h(B/'final-correction-v1/inputs/pinned-native-row-builder.py');sys.path.insert(0,str(builder.parent));spec=importlib.util.spec_from_file_location('review_poly_builder',builder);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
rows=mod._row_from_yaml(f,{},{},{},{},record=z,owners={});assert {(r['predicate_id'],r['object_id']) for r in rows}=={('skos:broadMatch','mesh:D010461'),('skos:exactMatch','kgmicrobe.ingredient:polypeptone')}
for r in rows:
 for x in labels:assert x not in r.get('other','')
ps=j(P/'proposals-v2.json')['proposals'];assert len(ps)==1;prop=ps[0];assert prop['after_capture']['sha256']==h(f)
baseDs={d['case_id']:d for d in j(B/'tellurium-polypeptone-v1/core/decisions.json')['decisions']};ds=j(P/'decisions-v2.json')['decisions'];case=[]
assess='The ordinary named Polypeptone preparation retains its local identity and is a supported kind of the closer generic MeSH Peptones material category. Full MICRO179 defines the BD casein/animal-tissue blend; it cannot supply exact identity for bare MediaDive442 or Hipolypepton2060. Three BD catalogue labels correctly become nonresolving provenance, retaining exact text/source prefixes, while five earlier Japanese/Hipolypepton exclusions remain exact. This does not prove every product chemically distinct. Current notes explicitly supersede earlier self-only/pending/FoodOn-gate conclusions. Complete history, 135/135 historical counts, provisional role, source/product/quantity holds and supplied-form boundaries are preserved. Mapping is NARROW_MATCH emitting broadMatch plus local identity, with truthful LLM evidence and no BD formula or lot-property assertion.'
for d in ds:
 oldd=baseDs[d['case_id']];changed=[k for k in d.keys()|oldd.keys() if d.get(k)!=oldd.get(k)];assert set(changed)=={'evidence_ids','polypeptone_final_reassessment'}
 assert all(e in d['evidence_ids'] for e in oldd['evidence_ids'])
 case.append({'case_id':d['case_id'],'selected_decision_object_sha256':oh(d),'assessment':assess,'complete_previous_source_decision_preserved':True,'changed_fields':changed,'limitations':'Existing source case raw form, original occurrence scope, generic-product/Japanese version and M122 quantity holds remain unchanged. This does not admit the Hipolypepton source to the Polypeptone owner.'})
ev=j(P/'evidence-v2.json')['evidence'];ec=[]
for e in ev:
 c=e['capture'];q=S/c['path'].split('buffer-parts-v1/',1)[1];assert h(q)==c['sha256'];ec.append({'evidence_id':e['evidence_id'],'capture':c,'assessment':'Source-snapshot of attributed author interpretation/alias decision; actual primary captures and original times retained in linked packets. Not a human MappingEvidence or new primary retrieval.'})
prior=R/'.temp/w05-tellurium-polypeptone-v1/review/main-review.json'
v={'reviewer':'/root/final_skeptical','completed_at':datetime.now(timezone.utc).isoformat(),'primary_author':'/root','verdict':'pass_with_limitations','case_reviews':case,'payload_reviews':[{'proposal_id':prop['proposal_id'],'proposal_object_sha256':oh(prop),'after_capture':prop['after_capture'],'assessment':assess,'complete_payload_read':True,'reviewer':'/root/final_skeptical','protected_fields':protected,'exact_alias_changes':syn,'history_exact_prefix':True,'mapping_evidence_exact_prefix':True,'complete_native_rows':rows}],'inputs':[b(P/n) for n in ['proposals-v2.json','decisions-v2.json','evidence-v2.json','final-assessment.json','alias-assessment-v1.json']],'new_evidence_review':ec,'interpretation_reassessment':b(Q/'ontology-interpretation-reassessment-v1.json'),'fresh_primary_read_bindings':[b(R/'.temp/w05-tellurium-polypeptone-v1/polypeptone/captures/micro-polypeptone.json'),b(S/'parents/captures/mesh-D010461-nlm.json'),b(S/'parents/captures/mesh-M0016245-nlm.json'),b(S/'parents/read/thermo.txt')],'fresh_source_scope':'Full target ontology definitions/annotations; manufacturer printed7 and49; complete final payload and before/after fields. Earlier historical Japanese/JCM/source-context science reused exactly with real attribution, not repeated as new full150-row primary research.','prior_science':b(prior) if prior.exists() else None,'finding_dispositions':[{'finding_id':'POLYPEPTONE-001','disposition':'BOUNDED_SOURCE_ORIGIN_GROUNDING_REPAIRED_NO_COUPLED_OWNER_ACCEPTANCE','assessment':'Current source proposal now has supported closer material broader mapping. The older saved combined-owner review is preserved; this does not close another worker’s review or approve whole-owner/source unions.'},{'finding_id':'W05-PARENTS-NEW01','disposition':'FORMAL_AXIOM_OMISSION_CONFIRMED_STRONGER_ROLE_GATE_QUALIFIED','assessment':'Exact actual restriction retained; source food use/role is not entailed. Selection follows closer material term, with separate explicit qualification.'}],'source_owner_export_approval':False,'limitations':['Full final root decision composition/native batch and publication accounting remain separate.','Unchanged historical135 counts are not new accepted membership. Source association, supplied form and CM150/408 quantity holds remain.']}
p=Q/'polypeptone-scientific-review-v1.json';assert not p.exists();p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(h(p),h(f))
