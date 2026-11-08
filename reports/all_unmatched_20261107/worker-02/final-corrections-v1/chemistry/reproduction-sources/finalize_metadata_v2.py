from pathlib import Path
from datetime import datetime, timezone
import json,hashlib,yaml,sys
W=Path(__file__).resolve().parents[3];sys.path.insert(0,str(W/'src'))
from mediaingredientmech.synonym_policy import is_resolving_synonym
R=W/'reports/all_unmatched_20261107/worker-02';S=R/'final-corrections-v1/chemistry'
def read(p):return json.loads(p.read_text())
def h(b):return hashlib.sha256(b).hexdigest()
def save(p,o):assert not p.exists(),p;p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def cap(p):return {'path':str(p.relative_to(R)),'sha256':h(p.read_bytes())}
old=read(R/'continuation-1201-v1/decisions.json');Ds=old['decisions'];P=read(R/'continuation-1201-v1/proposals.json')['proposals'];newP=read(S/'proposals.json')['proposals'];pid={p['proposal_id']:p for p in P};newbyowner={p['owner_path']:p for p in newP}
for kind in ['decisions','proposals','evidence']:
    d=read(S/(kind+'.json'));d['schema_version']=1
    if kind=='decisions':
        for k in ['worker_slot','shard_sha256','phase']:d[k]=old[k]
        d['fragment_scope']='This is an integration fragment, not a standalone complete-shard completion claim; exactly34 affected original cases.'
        for row in d['decisions']:
            n=next(i for i,x in enumerate(Ds) if x['case_id']==row['case_id'])
            if n==69:row['missing_requirement']='The ABEE ester and NBRC1604 concentration-label corrections are concrete isolated proposals. Remaining charge/zwitterion aliases and medium-specific vitamin-role applicability are unapproved; source-case69 remains the frozen unqualified acid contexts M3160/M3161, not the separately recovered M3052 stock.'
            if n==149:row['missing_requirement']='None for the explicitly CAS/form-qualified MediaDive106 source interpretation. The successor separately makes both underqualified global aliases nonresolving while preserving raw labels; source106 metadata cannot license unrestricted hydrate inference. Original complete-owner and release holds remain.'
    if kind=='evidence':
        for e in d['evidence']:
            if e['kind']=='local_context':e['kind']='local_validation'
    d['predecessor_metadata_capture']=cap(S/(kind+'.json'))
    save(S/(kind+'-v2.json'),d)

# Enumerate every originally pointed metadata alias, without turning the whole list of unrelated synonyms into a new claim.
findings=read(W/'.temp/w02-final-corrections-v1/chemistry/assigned-findings.json')
original=next(o['original'] for o in findings[0]['originals'] if o['original']['finding_id']=='W02C-005')
rows=[]
for t in original['targets']:
    owner=t['owner_path'];p=pid.get(t.get('proposal_id'));before=R/p['after_capture']['path'] if p else W/owner
    y=yaml.safe_load(before.read_text());new=newbyowner.get(owner);after=R/new['after_capture']['path'] if new else before;z=yaml.safe_load(after.read_text())
    claims=t.get('reproduced_current_claims',[])
    for c in claims:
        text=c['value']['synonym_text'];a=next(s for s in y['synonyms'] if s['synonym_text']==text);b=next(s for s in z['synonyms'] if s['synonym_text']==text)
        metadata=text.startswith(('Role:','Properties:'))
        status='already_nonresolving_metadata_preserved' if metadata else ('proposed_nonresolving_correction' if b['synonym_type']=='REJECTED_LABEL' and a!=b else 'retained_claim')
        if metadata:assert not is_resolving_synonym(a) and a==b
        rows.append({'owner_path':owner,'old_field_pointer':c['pointer'],'before_full_value':a,'after_full_value':b,'predecessor':cap(before) if before.is_relative_to(R) else {'path':owner,'sha256':h(before.read_bytes())},'after':cap(after) if after.is_relative_to(R) else {'path':owner,'sha256':h(after.read_bytes())},'native_mim_resolving_before':is_resolving_synonym(a),'native_mim_resolving_after':is_resolving_synonym(b),'status':status,'rationale':'Role/Properties prose is already filtered by current native MIM policy; no cleanup or scientific role approval follows.' if metadata else new['description'] if new else 'Retained within exact final qualification; no blanket label inference.'})
# Already-corrected alum labels and actual rejected tombstone are explicit no-op dispositions.
alum=pid['a-proposal-anhydrous-alum'];ap=R/alum['after_capture']['path'];ay=yaml.safe_load(ap.read_text())
for label in ['Na SiO .9H O','ZnSO .7H O']:
    s=next(x for x in ay['synonyms'] if x['synonym_text']==label);assert s['synonym_type']=='REJECTED_LABEL'
    rows.append({'owner_path':alum['owner_path'],'literal':label,'value':s,'selected_capture':cap(ap),'status':'already_rejected_no_change','rationale':'The selected prior proposal already corrected this exact foreign formula; the older baseline review cannot be treated as an unfixed successor defect.'})
for name in ['Mnso4_X_1_H2o.yaml','Cocl2_X_6_H2o.yaml']:
    p=W/'data/ingredients/mapped'/name;y=yaml.safe_load(p.read_text());assert y['mapping_status']=='REJECTED'
    rows.append({'owner_path':str(p.relative_to(W)),'sha256':h(p.read_bytes()),'mapping_status':y['mapping_status'],'status':'rejected_tombstone_preserved','rationale':'Not promoted to an active owner; raw historical aliases remain provenance and do not themselves establish an active resolver winner.'})
roles=[]
for p in P:
    path=R/p['after_capture']['path'];y=yaml.safe_load(path.read_text())
    for field in ['nutritional_roles','biological_roles','physical_roles','functional_roles']:
        for i,role in enumerate(y.get(field,[])):
            evidence=role.get('evidence',[])
            pred=bool(evidence) and all(e.get('reference_type')=='COMPUTATIONAL_PREDICTION' for e in evidence)
            derived=any('Mineral source' in str(e) or 'Defined component' in str(e) for e in evidence)
            if pred or not evidence or derived:
                n=newbyowner.get(p['owner_path']);after=R/n['after_capture']['path'] if n else path
                assert yaml.safe_load(after.read_text()).get(field,[])[i]==role
                roles.append({'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'pointer':f'/{field}/{i}','full_value':role,'selected_capture':cap(path),'successor_capture':cap(after),'category':'prediction_only' if pred else 'empty_evidence' if not evidence else 'metadata_inference','status':'unchanged_unapproved_not_declared_false','missing_fact':'Direct claim-specific evidence that this exact supplied substance has this functional role in the named organism/preparation context; neither chemical ancestry, metadata or occurrence counts alone establishes that applicability.'})
save(S/'finite-claim-dispositions.json',{'review_author':'/root/research_b','created_at':datetime.now(timezone.utc).isoformat(),'alias_claims':rows,'role_claims':roles,'counts':{'pointed_metadata_aliases':sum(r['status']=='already_nonresolving_metadata_preserved' for r in rows),'prediction_only_role_objects':sum(r['category']=='prediction_only' for r in roles),'empty_evidence_role_objects':sum(r['category']=='empty_evidence' for r in roles)},'count_limit':'Role counts are explicit full-object counts over all106 selected YAML; not asserted identical to a native review finding aggregation. Previously quoted seven prediction-only count is retained historically; this explicit enumeration yields eight.','separate_root_scope':'Root handles water PMID36233206 contextual qualification; PABA PMID31986050 corrected in chemistry candidate. Native MIM filter inspected here; prior peer dual-MIM/Claw results are not relabelled as this author running Claw. Agar SINGLE_INGREDIENT explicitly allowed; no change proposed.'})

# Byte-level integrity for actual new proposal inputs/outputs and all affected original source bindings.
checks=[]
for p in newP:
    assert h((W/p['owner_path']).read_bytes())==p['before_sha256']
    assert h((R/p['after_capture']['path']).read_bytes())==p['after_capture']['sha256']
    pre=yaml.safe_load((R/p['selected_predecessor_capture']['path']).read_text());aft=yaml.safe_load((R/p['after_capture']['path']).read_text())
    assert aft['curation_history'][:-1]==pre.get('curation_history',[])
    checks.append({'proposal_id':p['proposal_id'],'before_sha256':p['before_sha256'],'predecessor_capture':p['selected_predecessor_capture'],'after_capture':p['after_capture'],'history_prefix':'exact'})
for d in read(S/'decisions-v2.json')['decisions']:
    oldd=next(x for x in Ds if x['case_id']==d['case_id'])
    assert all(d[k]==oldd[k] for k in ['case_id','case_input_sha256','source','occurrence_ids'])
for e in read(S/'evidence-v2.json')['evidence']:assert h((R/e['capture']['path']).read_bytes())==e['capture']['sha256']
save(S/'integrity-v2.json',{'status':'PASS','author':'/root/research_b','checks':checks,'scientific_verdict':'pending independent review; structural and provenance checks are not source approval','active_fragments':[cap(S/(x+'-v2.json')) for x in ['decisions','proposals','evidence']],'native_writes':15,'failed_attempt_preserved':{'path':'.temp/w02-final-corrections-v1/chemistry/build-candidates-v1.log','reason':'All15 guarded writes completed, then metadata sort expected absent optionalscope_index. Resumed metadata by originalcaseID order; no YAML was rewritten.'},'no_maintained_mutation':True})
print(json.dumps({'status':'PASS','proposals':len(newP),'decisions':len(read(S/'decisions-v2.json')['decisions']),'finite_alias_rows':len(rows),'role_claims':len(roles)}))
