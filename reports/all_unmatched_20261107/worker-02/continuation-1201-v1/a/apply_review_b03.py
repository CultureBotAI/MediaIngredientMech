from pathlib import Path
import json,hashlib,datetime,shutil,sys,yaml,copy
sys.path.insert(0,'src')
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
O=Path('reports/all_unmatched_20261107/worker-02');R=O/'continuation-1201-v1/a';V=R/'revisions/draft-v4-source-boundaries';V.mkdir(parents=True,exist_ok=False)
ns=['decisions.json','evidence.json','proposals.json','reassessments.json','proposal-source-scopes.json','solution-scope-assessments.json','component-owner-review.json']
for n in ns:shutil.copy2(R/n,V/n)
L=lambda p:json.loads(p.read_text());S=lambda b:hashlib.sha256(b).hexdigest();C=lambda p:{'root':'artifact','path':str(p.relative_to(O)),'sha256':S(p.read_bytes())}
D,E,P,RA,PS,SS,CO=[L(R/n) for n in ns];oldE={e['evidence_id']:e for e in L(O/'evidence.json')['evidence']};changed=[];touched=set()
failed=['68caf8ce668fba7c','06c82845cf85343d','35d62fba3be2fc9f','4841cce9b82ee564','c1e5e38f919b0014','6dbfe7abf51bc0ab'];emap={};failrows=[]
for suffix in failed:
 old=oldE['a-primary-primary-'+suffix];assert 'Nothing found.' in (O/old['capture']['path']).read_text();new=copy.deepcopy(old);new['evidence_id']='a2-unsuccessful-original-jcm-'+suffix;new['kind']='unsuccessful_search';new['locator']='HTML body: Nothing found.';new['supports_or_contradicts']='The original JCM route returned a page saying Nothing found. This capture provides no recipe or identity evidence. Its original timestamp, URL and bytes are retained; successful TOGO API captures supply the provider recipe evidence where cited. The published old evidence entry is immutable and superseded in applicability by this correction.';E['evidence'].append(new);emap[old['evidence_id']]=new['evidence_id'];failrows.append({'old_evidence_id':old['evidence_id'],'successor_evidence_id':new['evidence_id'],'capture':old['capture'],'url':old['url'],'accessed_at':old['accessed_at']})
def remap(o):
 if isinstance(o,list):return [remap(x) for x in o]
 if isinstance(o,dict):return {k:remap(v) for k,v in o.items()}
 return emap.get(o,o) if isinstance(o,str) else o
D=remap(D);P=remap(P);RA=remap(RA)
failedurls={r['url'] for r in failrows}
for p in P['proposals']:
 path=O/p['after_capture']['path'];rec=yaml.safe_load(path.read_bytes());before=copy.deepcopy(rec);hist=rec.pop('curation_history',[])
 def correct(x):
  if isinstance(x,list):return [correct(v) for v in x if not(isinstance(v,dict) and v.get('source') in failedurls)]
  if isinstance(x,dict):return {k:correct(v) for k,v in x.items()}
  if isinstance(x,str):
   for u in failedurls:x=x.replace(u+'; ','').replace('; '+u,'')
   x=x.replace('JCM382 establishes','TOGO M377, recording JCM382, establishes').replace('JCM382 basal salts','TOGO M377 records JCM382 basal salts').replace('JCM665 explicitly','TOGO M683, recording JCM665, explicitly')
  return x
 rec=correct(rec);rec['curation_history']=hist
 if rec!=before:
  rec['notes']+=' Original JCM endpoint retrieval returned Nothing found; positive formulation evidence is the successful TOGO provider record, not direct inspection of the current original page.'
  record_curation_event(rec,curator='codex_worker02_research_a_continuation1201',action='CORRECTED',changes='Independent reviewer B identified an unsuccessful original JCM endpoint. Remove that route from positive formulation evidence; attribute the formulation to the successfully captured TOGO provider and preserve the historical assertion as audit history.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
  dest=R/'after-v4'/Path(p['owner_path']).name;write_validated_ingredient(rec,dest);changed.append({'proposal_id':p['proposal_id'],'before_capture':p['after_capture'],'after_capture':C(dest),'reason':'Failed original route demoted; successful provider is positive recipe source.'});p['after_capture']=C(dest);p['description']=correct(p['description']);touched.update(p['case_ids'])
# HCl stock whole/part boundary: its part is HCl, not the concentration-qualified whole.
p=next(p for p in P['proposals'] if p['proposal_id']=='a2-proposal-togo-m2746-m2305-hydrochloric-acid-25percent');rec=yaml.safe_load((O/p['after_capture']['path']).read_bytes());owner=Path('data/ingredients/mapped/Hcl.yaml');hcl=yaml.safe_load(owner.read_bytes());assert hcl['identifier']=='CHEBI:17883' and hcl['mapping_status']=='MAPPED';destowner=R/'before/mapped/Hcl.yaml'
if not destowner.exists():shutil.copy2(owner,destowner)
rec['components']=[{'component_name':hcl['preferred_term'],'component_id':hcl['identifier'],'reference_scope':'MIM_CATALOG'}];rec['notes']+=' HCl is the source-known solute part; 25% is a specification of the whole preparation with unstated percent basis. No solvent or solute concentration field is inferred.'
record_curation_event(rec,curator='codex_worker02_research_a_continuation1201',action='CORRECTED',changes='Independent reviewer B corrected the whole/part boundary: reference verified HCl solute CHEBI:17883 as the part, keeping the literal 25% and unknown basis only in the preparation identity and notes.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
dest=R/'after-v4'/Path(p['owner_path']).name;write_validated_ingredient(rec,dest);changed.append({'proposal_id':p['proposal_id'],'before_capture':p['after_capture'],'after_capture':C(dest),'reason':'Known HCl solute part, not whole-stock self-reference.'});p['after_capture']=C(dest);touched.update(p['case_ids']);CO.append({'proposal_id':p['proposal_id'],'component':rec['components'][0],'owner_path':str(owner),'owner_sha256':S(owner.read_bytes()),'owner_capture':C(destowner),'identity_scope':'Known HCl solute only; not whole 25% preparation identity or solvent assertion.'})
# JCM463 explicitly uses JCM462 except late carbon/reducer changes; TOGO M463 is JCM462.
oldids=['a2-proposal-jcm462-preaddition-basal-preparation','a2-proposal-jcm463-preaddition-basal-preparation'];parents=[next(p for p in P['proposals'] if p['proposal_id']==pid) for pid in oldids];p=copy.deepcopy(parents[0]);rec=yaml.safe_load((O/p['after_capture']['path']).read_bytes());slug='jcm462_463_preaddition_basal_preparation';pid='a2-proposal-jcm462-463-preaddition-basal-preparation';label='JCM 462/463 shared pre-addition basal preparation';ident='kgmicrobe.ingredient:'+slug
scope='Original JCM463 explicitly uses JCM462 with changes only to separately added carbon/electron-acceptor and reducer inputs: sodium lactate is replaced by 20 mM sodium acetate and 30 mM ferric citrate, sodium sulfide is omitted, and 0.5 g/L L-cysteine-HCl is added separately. These late inputs are outside this pre-addition basal material. Its source-listed basal components and quantities therefore share the JCM462 formulation. TOGO M464 riboflavin pointer to M463 resolves to JCM462, whose nested riboflavin preparation lists 2.5 mg riboflavin with 100 ml added water. The 1 ml riboflavin input is a named preparation part; no final volume or derived stock concentration is invented. Both original occurrence and source-version scopes remain explicit; this does not equate the complete growth media.'
rec['identifier']=ident;rec['preferred_term']=label;rec['ontology_mapping']['ontology_id']=ident;rec['ontology_mapping']['ontology_label']=label;rec['notes']=scope+' '+rec['notes'].replace('JCM462 instructions','The inherited JCM462 instructions');urls=['https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=462','https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=463','https://togomedium.org/medium/M463','https://togomedium.org/medium/M464'];rec['ontology_mapping']['evidence']=[{'evidence_type':'CURATOR_JUDGMENT','source':'; '.join(urls),'notes':scope+' Bounded whole-preparation local identity; no pure constituent grounding.'}];rec['component_assertion']['evidence']=[{'evidence_type':'RECIPE_SOURCE','source':u,'source_record':label,'notes':scope} for u in urls]
for c in rec['components']:
 if c['component_name']=='Riboflavin (see below)':c['component_name']='JCM 462 riboflavin preparation'
record_curation_event(rec,curator='codex_worker02_research_a_continuation1201',action='CORRECTED',changes='Independent reviewer B resolved the original JCM463 cross-reference and the TOGO M463 riboflavin pointer. Consolidate the two proposed pre-addition basal owners at their demonstrated shared formulation, retaining independent source occurrences and excluding differing late additions.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
dest=R/'after-v4'/(slug+'.yaml');write_validated_ingredient(rec,dest);p.update(proposal_id=pid,owner_path='data/ingredients/mapped/'+slug+'.yaml',after_capture=C(dest),description=scope);p['evidence_ids']=sorted(set(sum([x['evidence_ids'] for x in parents],[])));P['proposals']=[x for x in P['proposals'] if x['proposal_id'] not in oldids]+[p];touched.update(p['case_ids']);changed.append({'proposal_id':pid,'supersedes_proposals':oldids,'before_captures':[x['after_capture'] for x in parents],'after_capture':C(dest),'reason':scope})
def rebind(x):
 if isinstance(x,list):return list(dict.fromkeys(rebind(v) for v in x)) if x and all(isinstance(v,str) for v in x) else [rebind(v) for v in x]
 if isinstance(x,dict):
  y={k:rebind(v) for k,v in x.items()}
  if x.get('proposal_id') in oldids:
   if 'adjudication' in y:y['adjudication']=scope
   if 'scope' in y:y['scope']=scope
   if 'record_identifier' in y:y['record_identifier']=ident
  return y
 if isinstance(x,str):return pid if x in oldids else x.replace('Seventeen source-specific prepared basal or combined mixtures are proposed.','Sixteen bounded basal or combined mixture proposals cover seventeen prepared-material occurrences; JCM462/463 share their demonstrated pre-addition basal formulation.')
 return x
D,RA,PS,SS=[rebind(x) for x in [D,RA,PS,SS]]
PS=[x for x in PS if x['proposal_id']!=pid]+[{'proposal_id':pid,'source_urls':urls,'scope':scope,'indices':[58],'record_identifier':ident}]
# Explain old unsuccessful evidence applicability without modifying the published ledger.
for d in D['decisions']:
 if any(eid in emap.values() for eid in d['evidence_ids']):
  d['reasoning']+=' Original JCM route(s) returning Nothing found are unsuccessful retrievals only; positive recipe interpretation uses the separately captured TOGO provider record. No direct original-page inspection is claimed for those routes.';touched.add(d['case_id'])
for a in RA['assessments']:
 a['primary_evidence_ids']=[e for e in a['primary_evidence_ids'] if e not in emap.values()]
 if a['case_id'] in touched:a['peer_review_revision']='Source-route limitations, JCM462/463 shared basal scope, or exact HCl solute boundary addressed in a2-review-b-source-boundaries; prior draft payload paths retained.'
(R/'component-owner-review.json').write_text(json.dumps(CO,indent=2,ensure_ascii=False)+'\n')
(R/'proposal-source-scopes.json').write_text(json.dumps(PS,indent=2,ensure_ascii=False)+'\n');(R/'solution-scope-assessments.json').write_text(json.dumps(SS,indent=2,ensure_ascii=False)+'\n')
receipt={'reviewer':'/root/research_b','applied_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unsuccessful_original_routes':failrows,'changes':changed,'all_prior_payload_paths_retained':True,'all_original_occurrence_ids_and_holds_preserved':True,'prior_proposals_sha256':S((V/'proposals.json').read_bytes())};(R/'review-b-revision-03.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n');eid='a2-review-b-source-boundaries'
E['evidence'].append({'evidence_id':eid,'kind':'local_validation','capture':C(R/'review-b-revision-03.json'),'locator':'Unsuccessful original JCM retrievals; source-preparation identity consolidation; HCl solute/whole distinction; exact successor captures','supports_or_contradicts':'Independent reviewer findings resolved using original source cross-references and successful provider recipe bytes, preserving source scopes and all old draft payloads.','url':None,'case_ids':sorted(touched)})
for e in E['evidence']:
 path=e['capture']['path']
 if path in [str((R/n).relative_to(O)) for n in ['component-owner-review.json','proposal-source-scopes.json','solution-scope-assessments.json']]:e['capture']=C(O/path)
for d in D['decisions']:
 if d['case_id'] in touched:d['evidence_ids'].append(eid)
for p in P['proposals']:
 if any(p['proposal_id']==x['proposal_id'] for x in changed):p['evidence_ids'].append(eid)
for n,o in [('decisions.json',D),('evidence.json',E),('proposals.json',P),('reassessments.json',RA)]: (R/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
print('active',len(P['proposals']),'changed',len(changed),'evidence',len(E['evidence']))
