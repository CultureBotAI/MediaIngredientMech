from pathlib import Path
import json,hashlib,datetime,shutil,sys,yaml,copy
sys.path.insert(0,'src')
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
O=Path('reports/all_unmatched_20261107/worker-02');R=O/'continuation-1201-v1/a';V=R/'revisions/draft-v5-quality-treatment-boundaries';V.mkdir(parents=True,exist_ok=True)
ns=['decisions.json','evidence.json','proposals.json','reassessments.json','proposal-source-scopes.json']
for n in ns:
 if not (V/n).exists():shutil.copy2(R/n,V/n)
L=lambda p:json.loads(p.read_text());S=lambda b:hashlib.sha256(b).hexdigest();C=lambda p:{'root':'artifact','path':str(p.relative_to(O)),'sha256':S(p.read_bytes())}
D,E,P,RA,PS=[L(R/n) for n in ns];replacements={};changes=[];touched=[]
settings=[(9,'a2-proposal-togo-m3249-ultrapure-water','a2-proposal-water-source-quality-provenance','Distilled_Water.yaml','CHEBI:15377','TOGO M3249 explicitly specifies Ultrapure water. This is source-qualified molecular-water provenance only: no purity standard, resistivity, purification process or formulation difference is established. Quality alone does not justify a separate mixture identity under MAPPING_SEMANTICS sections3/6. This annotation does not identify ultrapure water with the named distilled preparation, activate a resolving alias, reverse rejected water labels, or establish grade interchangeability.','https://togomedium.org/medium/M3249'),(15,'a2-proposal-atcc2883-filter-sterilized-methanol','a2-proposal-methanol-source-filtration-provenance','Methanol.yaml','CHEBI:17790','Original ATCC2883 broth and agar recipes specify Methanol (filter sterilized), 3 ml added after autoclaving. This establishes a source-qualified treatment of the methanol input, not a new mixture identity. No assay, solvent, dilution, filter pore size or universal grade equivalence is inferred. The raw source wording remains in this provenance note rather than an automatically resolving alias. The existing Methanol (10%) label denotes a concentration-qualified stock; it is retained as REJECTED_LABEL on the pure molecular methanol owner.','https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/2/8/8/3/atcc-medium-2883.pdf')]
for idx,oldpid,pid,fn,ident,scope,url in settings:
 p=next(x for x in P['proposals'] if x['proposal_id']==oldpid);old=copy.deepcopy(p);owner=Path('data/ingredients/mapped')/fn;rec=yaml.safe_load(owner.read_bytes());assert rec['identifier']==ident;before=copy.deepcopy(rec);dst=R/'before/mapped'/fn
 if not dst.exists():shutil.copy2(owner,dst)
 rec['notes']=(rec.get('notes','')+'\n\n'+scope+' All inherited source, ingredient, full-owner and downstream publication holds remain.').strip()
 if idx==15:
  rec.setdefault('supplied_form',[]).append({'name':'Methanol (filter sterilized)','form':'filter sterilized','notes':'ATCC2883 source-qualified input. Assay and solvent are unstated; this is a preparation treatment, not a separate identity.'})
  for sy in rec['synonyms']:
   if sy['synonym_text']=='Methanol (10%)':sy['synonym_type']='REJECTED_LABEL'
 record_curation_event(rec,curator='codex_worker02_research_a_continuation1201',action='CORRECTED',changes=scope+' This bounded provenance amendment does not approve the whole inherited owner or its remaining aliases.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
 dest=R/'after-v5'/fn;write_validated_ingredient(rec,dest)
 eid=f'a2-case-{idx:02d}-quality-treatment-owner';E['evidence'].append({'evidence_id':eid,'kind':'owner_snapshot','capture':C(dst),'locator':'Complete existing owner, identity, aliases and curation history; changes limited to source-qualified notes/treatment and explicitly rejected concentration stock label.','supports_or_contradicts':'Actual current owner inspected in full. Molecular identity remains unchanged; source quality/treatment does not independently demonstrate a distinct mixture. Existing full-owner release limitations retained.','url':None,'case_ids':p['case_ids']})
 p.update(proposal_id=pid,owner_path=str(owner),kind='edit_existing_owner',before_sha256=S(owner.read_bytes()),after_capture=C(dest),description=scope,mapping_consequence='No identity, grounding or preferred-label change. Bounded source provenance/supplied-form amendment; methanol concentration-stock alias rejection affects future exported label eligibility. Full native integration and publication holds remain.',inherited_owner_findings=['Bounded source amendment only; inherited owner synonym/evidence history is not globally approved. Water preparation rejection policy remains intact.' if idx==9 else 'Other inherited methanol aliases and provenance remain outside this bounded correction and require full-owner approval before publication.']);p['evidence_ids'].append(eid);replacements[oldpid]=pid;touched.extend(p['case_ids']);changes.append({'old_proposal':old,'successor_proposal_id':pid,'before_capture':C(dst),'after_capture':C(dest),'scope':scope})
 for d in D['decisions']:
  if d['case_id'] in p['case_ids']:
   d['reasoning']=scope;d['applicability']+=' Successor proposal is a bounded existing-owner provenance amendment at molecular identity scope; it does not automatically resolve the raw quality/treatment label.';d['evidence_ids'].append(eid)
 for a in RA['assessments']:
  if a['index']==idx:a['reason']=scope;a['identity_boundary_revision']='Separate local mixture draft superseded by bounded existing-owner provenance; original draft remains immutable.'
# Add valid source spelling for independently assessed C151 to the variable identity.
p=next(x for x in P['proposals'] if x['proposal_id']=='a2-proposal-manganese-sulfate-variable-hydrate');rec=yaml.safe_load((O/p['after_capture']['path']).read_bytes());raw='MnSO4 x n H2O';assert not any(s['synonym_text']==raw for s in rec['synonyms']);rec['synonyms'].append({'synonym_text':raw,'synonym_type':'HYDRATE_FORM','source':'MediaDive ingredient 1000; frozen case KG_CASE:55268b66b04a59d2f2c6487270ae15e4a4686148d8fff29fd66b248269821cd8'})
record_curation_event(rec,curator='codex_worker02_research_a_continuation1201',action='ADDED_SYNONYMS',changes='Independent reviewer B verified C151 MediaDive1000 literal MnSO4 x n H2O is the same variable-hydration identity; preserve its exact raw spelling and source. No fixed hydrate, molecular weight or structure is inferred.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True)
dest=R/'after-v5'/Path(p['owner_path']).name;write_validated_ingredient(rec,dest);changes.append({'proposal_id':p['proposal_id'],'before_capture':p['after_capture'],'after_capture':C(dest),'scope':'Source C151 exact variable-hydrate spelling, no fixed hydration.'});p['after_capture']=C(dest);touched.extend(p['case_ids'])
def rebind(x):
 if isinstance(x,list):return [rebind(v) for v in x]
 if isinstance(x,dict):return {k:rebind(v) for k,v in x.items()}
 return replacements.get(x,x) if isinstance(x,str) else x
D,RA,PS=[rebind(x) for x in [D,RA,PS]]
for x in PS:
 if x['proposal_id'] in replacements.values():
  p=next(p for p in P['proposals'] if p['proposal_id']==x['proposal_id']);x['scope']=p['description'];x['record_identifier']=yaml.safe_load((O/p['after_capture']['path']).read_bytes())['identifier']
(R/'proposal-source-scopes.json').write_text(json.dumps(PS,indent=2,ensure_ascii=False)+'\n')
receipt={'reviewer':'/root/research_b','applied_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changes':changes,'all_prior_payload_paths_retained':True,'all_original_occurrence_ids_and_holds_preserved':True};(R/'review-b-revision-04.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n');eid='a2-review-b-quality-treatment-boundaries';E['evidence'].append({'evidence_id':eid,'kind':'local_validation','capture':C(R/'review-b-revision-04.json'),'locator':'Exact source-quality/treatment owner amendments; variable-hydrate source spelling','supports_or_contradicts':'Peer findings resolved at identity versus supplied-form boundary with exact current owner hashes and versioned guarded successor payloads.','url':None,'case_ids':sorted(set(touched))})
for e in E['evidence']:
 if e['capture']['path']==str((R/'proposal-source-scopes.json').relative_to(O)):e['capture']=C(R/'proposal-source-scopes.json')
for d in D['decisions']:
 if d['case_id'] in touched:d['evidence_ids'].append(eid)
for p in P['proposals']:
 if p['proposal_id'] in replacements.values() or p['proposal_id']=='a2-proposal-manganese-sulfate-variable-hydrate':p['evidence_ids'].append(eid)
for n,o in [('decisions.json',D),('evidence.json',E),('proposals.json',P),('reassessments.json',RA)]: (R/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
print('active',len(P['proposals']),'evidence',len(E['evidence']))
