from pathlib import Path
import copy, datetime, hashlib, json, os, subprocess, sys
import yaml

W = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w06/worktree')
C = W.parents[2]
R = W / 'reports/all_unmatched_20261107/worker-06'
S = R / 'successor-v5'
O = Path(__file__).parent
T = C / 'preflight/w06-final-metadata-triage-v1'
PY = '/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python'
START = '2026-11-08T08:41:30+00:00'
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ch(x): return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
def j(p): return json.loads(Path(p).read_text())
def save(n,x):
    p=O/n
    assert not p.exists(), f'immutable output exists: {p}'
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ref(p): return {'path':str(p),'sha256':h(p)}
def rows(p,k,idkey): return {x[idkey]:x for x in j(p)[k]}
def diff(a,b,p=''):
    if type(a)!=type(b): return [{'path':p,'before':a,'after':b}]
    if isinstance(a,dict):
        out=[]
        for k in sorted(a.keys()|b.keys()):
            q=p+'/'+k.replace('~','~0').replace('/','~1')
            if k not in a: out.append({'path':q,'before_absent':True,'after':b[k]})
            elif k not in b: out.append({'path':q,'before':a[k],'after_absent':True})
            else: out+=diff(a[k],b[k],q)
        return out
    if isinstance(a,list):
        if len(a)!=len(b): return [] if a==b else [{'path':p,'before':a,'after':b}]
        return sum((diff(x,y,p+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))),[])
    return [] if a==b else [{'path':p,'before':a,'after':b}]

head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip()
triage=[]
for x in j(T/'verified-manifest.json')['files']:
    p=T/x['path']; assert h(p)==x['sha256'];triage.append(ref(p))
prior=[]
for x in j(O.parent/'MANIFEST-science-v1.json')['files']:
    p=O.parent/x['path'];assert h(p)==x['sha256'];prior.append(ref(p))
assert len(prior)==32
save('input-integrity-v1.json',{'verified_triage_members':triage,'prior_a5_sealed_members_unchanged':prior,'triage_manifest':ref(T/'verified-manifest.json'),'prior_a5_manifest':ref(O.parent/'MANIFEST-science-v1.json'),'head':head})

E0=rows(R/'successor-v4/evidence.json','evidence','evidence_id')
E=rows(S/'reviewed-draft/evidence.json','evidence','evidence_id')
D0=rows(R/'successor-v4/decisions.json','decisions','case_id')
D=rows(S/'reviewed-draft/decisions.json','decisions','case_id')
P0=rows(R/'successor-v4/proposals.json','proposals','proposal_id')
P=rows(S/'reviewed-draft/proposals.json','proposals','proposal_id')
F=rows(C/'queue/preliminary-v5/shards/shard-06.json','cases','case_id')
sup=j(S/'claim-supersessions.json')
native=W/'reviews/structured/20261108T080947Z-w06-successor-v4-residuals/review.yaml'
assert h(native)=='b7f505b9eb538ae407b1bfc0a9d6c8bc8fbe1e3d6d1fbba60af5ac1093ee8c17'
assert subprocess.check_output(['git','show',head+':'+str(native.relative_to(W))],cwd=W)==native.read_bytes()
native_obj=yaml.safe_load(native.read_text())
trace=[];bindings=[];cmds=[]
targets=[(20,'CM_NAME:15b5758bf3f61382021511df819630931004403ec89a84bac892db53f1117f34','A-P-TOGO2665-KOH-STOCK','A-E-CAPTURE-078',17),(38,'CM_NAME:3b349c72b9fd9b3e3a66970a7d3a916a563d56a85cee50b5f2de431387c55658','A-P-JCM1344-YEAST-1PCT','A-E-CAPTURE-102',21)]
for ci,cid,pid,eid,ni in targets:
    delta=diff(E0[eid],E[eid]);assert [x['path'] for x in delta]==['/supports_or_contradicts']
    authored=next(x for x in sup['changes'] if x['evidence_id']==eid)
    assert authored['before']==E0[eid] and authored['after']==E[eid]
    capture=R/E[eid]['capture']['path']; assert h(capture)==E[eid]['capture']['sha256']
    if ci==38: assert E0[eid]['supports_or_contradicts'].split('case38:')[0]==E[eid]['supports_or_contradicts'].split('case38:')[0]
    assert P0[pid]==P[pid]
    payload=R/P[pid]['after_capture']['path'];assert h(payload)==P[pid]['after_capture']['sha256']
    assert subprocess.check_output(['git','show',head+':'+str(payload.relative_to(W))],cwd=W)==payload.read_bytes()
    y=yaml.safe_load(payload.read_text()); assert len(y['components'])==1
    assert y['components'][0]['reference_scope']=='UNMAPPED'
    assert y['component_assertion']['method']=='RECIPE_TRANSCRIPTION' and y['component_assertion']['completeness']=='UNKNOWN'
    if ci==20: assert y['components']==[{'component_name':'KOH','reference_scope':'UNMAPPED'}]
    else: assert y['components']==[{'component_name':'Yeast extract','reference_scope':'UNMAPPED','concentration_value':'1','concentration_unit':'PERCENT'}]
    assert D[cid]['case_input_sha256']==ch(F[cid]);assert D[cid]['occurrence_ids']==[x['occurrence_id'] for x in F[cid]['occurrences']]
    dd=diff(D0[cid],D[cid]);allowed={'/evidence_ids','/issue_refs','/independent_review/status','/independent_review/evidence_ids','/prior_v5_independent_review','/source_claim_supersession'}
    assert set(x['path'] for x in dd)<=allowed,dd
    for change in dd:
        if change['path']=='/evidence_ids':assert change['after']==change['before']+['V5-E-STOCK-CLAIM-SUPERSESSION']
        if change['path']=='/issue_refs':assert change['after']==change['before']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1217#issuecomment-6719323521']
        if change['path']=='/prior_v5_independent_review': assert change['after']==D0[cid]['independent_review']
    oldnative=native_obj['evidence'][ni];assert oldnative['evidence_id']==eid
    assert oldnative['summary']==E0[eid]['supports_or_contradicts']+' Exact captured bytes and original retrieval timestamp retained; bounded applicability separately assessed.'
    binding={'case_index':ci,'case_id':cid,'case_input_sha256':ch(F[cid]),'final_decision_canonical_sha256':ch(D[cid]),'proposal_id':pid,'proposal_canonical_sha256':ch(P[pid]),'full_payload':ref(payload),'before_evidence_canonical_sha256':ch(E0[eid]),'after_evidence_canonical_sha256':ch(E[eid]),'capture':ref(capture),'original_accessed_at':E[eid]['accessed_at'],'url':E[eid]['url'],'occurrence_ids':D[cid]['occurrence_ids'],'payload_and_proposal_unchanged':True,'all_case_science_fields_unchanged':True}
    bindings.append(binding)
    trace.append({'binding':binding,'complete_before_decision':D0[cid],'complete_after_decision':D[cid],'complete_proposal_unchanged':P[pid],'complete_payload':y,'complete_frozen_case':F[cid],'complete_before_evidence':E0[eid],'complete_after_evidence':E[eid],'exact_evidence_delta':delta,'exact_decision_delta':dd,'old_native_summary':oldnative,'old_native_locator':f'/evidence/{ni}/summary','explicit_supersession':sup['historical_native_summaries_superseded_claim_only']})
    argv=[PY,str(W/'scripts/validate_strict.py'),str(payload),'--workers','1','--out',str(O/f'case-{ci}-strict.tsv')]
    run=subprocess.run(argv,cwd=O,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
    cmds.append({'argv':argv,'cwd':str(O),'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr,'pytest_used':False,'coverage_used':False})
    assert run.returncode==0

assert E0['A-E-COMPLETION-09']==E['A-E-COMPLETION-09']
togo=R/E['A-E-COMPLETION-09']['capture']['path'];assert h(togo)==E['A-E-COMPLETION-09']['capture']['sha256']
tk=j(togo)['components'][1]['items'][15]
assert tk['component_name']=='KOH solusion' and tk['label']=='Potassium hydroxide solution' and any(x['label']=='Solution' for x in tk['properties'])
sup_e=E['V5-E-STOCK-CLAIM-SUPERSESSION'];assert sup_e['capture']['sha256']==h(S/'claim-supersessions.json')
assert sup_e['case_ids']==[x[1] for x in targets]
retained=[]
for pid,p in P0.items():
    assert pid in P
    assert p['after_capture']==P[pid]['after_capture']
    pp=R/p['after_capture']['path'];assert h(pp)==p['after_capture']['sha256']
    retained.append({'proposal_id':pid,**ref(pp)})
assert len(retained)==104
changed_old=[eid for eid in E0 if E0[eid]!=E[eid]]
assert set(changed_old)=={'A-E-CAPTURE-078','A-E-CAPTURE-102'}
save('fieldtrace-v1.json',{'canonical_hash_method':'SHA256 UTF-8 JSON sorted keys, compact separators, ensure_ascii=False, allow_nan=False, no newline','targets':trace,'explicit_claim_supersession':sup,'supersession_link':sup_e,'unchanged_TOGO_form_evidence':E['A-E-COMPLETION-09'],'retained_previous_payloads_byte_verified_only_not_scientifically_rereviewed':retained,'all_old_evidence_changed_ids':changed_old})
save('native-strict-checks-v1.json',{'checks':cmds,'validator':ref(W/'scripts/validate_strict.py'),'schema':ref(W/'src/mediaingredientmech/schema/mediaingredientmech.yaml')})

report={'schema_version':'1.0.0','review_id':'W06-V5-IR-STOCK-CLAIM-20261108','reviewer':'/root/residual_stock_review','author':'Codex worker06 /root','llm_assisted':True,'independence':'Reviewer did not author or edit either original or final stock payload, corrected evidence, source decisions, or claim-supersession. Reviewer previously independently reviewed seven stock residuals; this additive observation corrects current claim support without rewriting those historical reports.','started_at':START,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'scope':{'case_indices':[20,38],'full_payloads':2,'full_source_outcomes':2,'changed_evidence_objects':2,'complete_primary_bodies_read':['ATCC 1775 entire PDF text extraction','TOGO M2665 entire JSON','JCM 1344 entire HTML'],'excluded':'Case27 is preserved byte-exact, not newly scientifically accepted. No whole-owner, role, exporter, all-source or coordinator acceptance. Technical control limitation is assigned separately to root and skeptical assembly.'},'completion':'complete','verdict':'pass_with_limitations','native_verdict':'Bounded filed current-claim corrections supported; unchanged payloads and source outcomes remain source-scoped proposals.','bindings':bindings,'core_inputs':[ref(S/'reviewed-draft'/f'{x}.json') for x in ['decisions','proposals','evidence']],'claim_supersession':ref(S/'claim-supersessions.json'),'frozen_input':ref(C/'queue/preliminary-v5/shards/shard-06.json'),'historical_native':ref(native),'historical_native_unchanged_against_published_git':True,'positive_assessments':[{'case_index':20,'evidence':['A-E-CAPTURE-078','A-E-COMPLETION-09'],'assessment':'ATCC gives KOH pH adjustment but no supplied form, strength, dose or carrier. TOGO separately and explicitly names KOH solusion, labels potassium hydroxide solution and classifies Solution. The solution-qualified local preparation identity is supported only at that TOGO occurrence scope. Neither the trace-table water nor its approximately 500 ml dissolution / final 1 L volume establishes a KOH-stock carrier, concentration or batch volume. The new summary correctly separates these claims. The unchanged single UNMAPPED KOH component and UNKNOWN completeness retain unquantified input without exact solid/hydrate identity, final neutralization-species or pH-as-stock-property claims.'},{'case_index':38,'evidence':['A-E-CAPTURE-102'],'assessment':'JCM1344 prints 1% Yeast extract solution, 1 ml receiving addition after cooling, under its autoclaved-or-starred-filter-sterilized key. This entry is unstarred, supporting the unchanged separately autoclaved statement. The basal 935 ml water and receiving N2/CO2 atmosphere are not the yeast-stock formulation. New summary preserves strength and dose while correctly leaving stock carrier, product and percent basis unknown. One UNMAPPED Yeast extract component at literal 1 PERCENT, UNKNOWN completeness and no 10 g/L conversion remain supported. No gas, preparation volume, carrier grade, product identity or resolving generic alias is invented.'}],'dispositions':[{'finding_id':'W08-W06V4-001','issue_key':'w06-current-stock-evidence-scope','filed_issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1217#issuecomment-6719323521','status':'resolved_in_exact_reviewed_draft_claims_only','reason':'Both full evidence objects change only supports_or_contradicts; raw bytes, URLs and original access times remain unchanged. Claim-supersessions.json explicitly supersedes two prior native wording claims by exact path/hash/pointers, preserving historical report. Payload and all source-scientific case fields are unchanged; case27 prefix retained byte-for-byte.'},{'finding_id':'W08-W06-LINEAGE-CTRL-001','status':'acknowledged_validation_evidence_limitation_not_retested_by_this_science_reviewer','reason':'Do not infer that historical constructed dictionary/list comparisons exercise full stock/preservation regressions. Root and independent skeptical assembly own stronger controls; no payload defect or source rejection follows from this limitation.'}],'new_confirmed_findings':[],'checks':{'triage_manifest_members_verified':len(triage),'sealed_A5_members_verified_unchanged':len(prior),'strict_native_payload_schema_passes':2,'previous_payloads_byte_verified_unchanged':len(retained),'active_proposal_count_observed':len(P),'old_evidence_objects_changed_only':changed_old,'case27_prefix_exact':True,'focused_source_field_checks':'Whole objects compared with exact allowlisted changed paths; fieldtrace retains full before/after objects and every delta, no broad exclusion of arbitrary keys.'},'limitations':['Review binds reviewed-draft core bytes, not an unobserved future final core; final review metadata requires additive exact binding.','Native report validate/save/check and full-overlay partonomy/controls are root/assembly responsibilities for the final campaign packet; this reviewer reran strict schema only for two unchanged payloads.','No live public refetch was needed for this historical capture-bound review; original timestamps are retained and current local full captures inspected.','Existing KOH and yeast-extract native owners were read as identity context; this review does not approve their inherited aliases, mappings or roles.','No whole-owner/source-case final acceptance, role approval, downstream hold lift, source integration, export or release approval.'],'remaining_scientific_holds':{'20':['KOH stock carrier and carrier grade','strength, density and titrant amount','supplied chemical form and preparation','no equivalence to generic pure KOH or standardized stock'],'38':['stock carrier and carrier grade','percent basis','commercial extract/product and grade','preparation volume and equivalence to any other yeast stock']}}
save('final-science-v1.json',report)
save('HANDOFF-v1.json',{'reviewer':report['reviewer'],'review':ref(O/'final-science-v1.json'),'fieldtrace':ref(O/'fieldtrace-v1.json'),'native_checks':ref(O/'native-strict-checks-v1.json'),'verdict':report['verdict'],'new_confirmed_findings':[],'source_case_final_acceptance':False})
files=[{'path':str(p.relative_to(O)),'bytes':p.stat().st_size,'sha256':h(p)} for p in sorted(O.rglob('*')) if p.is_file()]
save('MANIFEST-v1.json',{'scope':'Immutable additive independent review of two filed evidence-summary corrections; preserves all 32 sealed A5 review files.','files':files})
print(json.dumps({'review':ref(O/'final-science-v1.json'),'fieldtrace':ref(O/'fieldtrace-v1.json'),'manifest':ref(O/'MANIFEST-v1.json'),'bindings':bindings},indent=2))
