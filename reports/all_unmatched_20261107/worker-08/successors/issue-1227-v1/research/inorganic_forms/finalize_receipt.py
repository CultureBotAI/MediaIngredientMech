"""Author receipt and claim-level evidence annotation; no corpus writes."""
import copy
import datetime
import hashlib
import json
import pathlib
import subprocess

R = pathlib.Path('reports/all_unmatched_20261107/worker-08')
S = R/'successors/issue-1227-v1'
O = S/'research/inorganic_forms'
A = json.loads((O/'assignment.json').read_text())
D = json.loads((O/'decisions.json').read_text())
P = json.loads((O/'proposals.json').read_text())
E = json.loads((O/'evidence-additions.json').read_text())
OLD_E = {x['evidence_id']:x for x in json.loads((R/'successors/issue-1201-v1/evidence.json').read_text())['evidence']}
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def objsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()

def save(path,data):
    p=O/path
    assert p.resolve().is_relative_to(O.resolve())
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p)}

p5=next(p for p in P if p['proposal_id']=='if-new-sodium-ammonium-phosphate-tetrahydrate')
disposition={
 'historical_evidence_id':'if-web-1cdd59bc636c',
 'historical_capture':OLD_E['if-web-1cdd59bc636c']['capture'],
 'original_accessed_at':OLD_E['if-web-1cdd59bc636c'].get('accessed_at'),
 'status':'historical_incomplete_not_active_property_support',
 'limitation':'The batch6 item is preserved as acquisition history. It does not contain the full Thermo product identity fields and must not substantiate CAS, molecular formula or molecular weight claims.',
 'active_evidence_id':'if1227-thermo-full-batch7',
 'active_capture':next(e for e in E if e['evidence_id']=='if1227-thermo-full-batch7')['capture'],
 'active_original_accessed_at':'2026-11-08T05:08:47.015262+00:00',
 'case_ids':p5['case_ids'],'proposal_ids':[p5['proposal_id']]}
dc=save('evidence-dispositions.json',{'rows':[disposition],'source_times_preserved':True})
de={'evidence_id':'if1227-thermo-evidence-disposition','kind':'local_validation','capture':dc,'url':None,
 'locator':'rows[0]; exact old batch6 and active batch7 bindings',
 'supports_or_contradicts':'Only full batch7 supplies current Thermo property support. Retained batch6 is explicitly historical and incomplete; no retrieval time is invented.',
 'case_ids':p5['case_ids']}
E.append(de)
p5.setdefault('evidence_dispositions',[]).append(disposition)
p5['evidence_ids'].append(de['evidence_id'])
for d in D:
    if d['case_id'] in p5['case_ids']:
        d.setdefault('evidence_dispositions',[]).append(disposition)
        d['evidence_ids'].append(de['evidence_id'])
save('decisions.json',D)
save('proposals.json',P)
save('evidence-additions.json',E)

# Refresh assessment hashes after the explicit evidence-use annotation.
ca=json.loads((O/'case-assessment.json').read_text())
bycase={d['case_id']:d for d in D}
for x in ca['rows']:
    d=bycase[x['case_id']]
    x['after_decision_sha256']=objsha(d)
    x['source_evidence_ids']=d['evidence_ids']
save('case-assessment.json',ca)
fa=json.loads((O/'full-payload-assessment.json').read_text())
byp={p['proposal_id']:p for p in P}
for x in fa['rows']:
    x['source_evidence_ids']=byp[x['proposal_id']]['evidence_ids']
    if x['proposal_id']==p5['proposal_id']:
        x['evidence_dispositions']=[disposition]
save('full-payload-assessment.json',fa)

frozen_findings=json.loads((S/'inputs/external-review/findings.json').read_text())
assigned={'W08-IR-001','W08-IR-003','W08-IR-006','W08-IR-008','W08-IR-010','W08-IR-011'}
conclusions={
 'W08-IR-001':('corrected_pending_peer','47 mapping assertions individually classified. Exactly 23 new LLM-assisted identity judgments changed from MANUAL_CURATION to CURATOR_JUDGMENT. Inherited assertions and ComponentEvidence types are unchanged.'),
 'W08-IR-003':('reassessed_no_compatible_substitution_pending_peer','All 27 component slots inspected: 19 existing active catalog/nested-stock references remain; eight unresolved slots have explicit hydration/form conflicts. Current ignored-inclusive owner candidates are bound. No inorganic replacement is listed by the external feasible-candidate inventory. A separate established Tris salt source fact has an exact W05 coordinator referral, without authorizing that candidate.'),
 'W08-IR-006':('corrected_pending_peer','Applied the exact coordinator refinement: five literal two-input lists COMPLETE, fifteen concentration-defined preparations UNKNOWN, and PCR phosphate buffer retained PARTIAL for an explicit unnamed pH-adjusting input. All five campaign exclusions are retained, including four outside this cohort. No quantity, source form or component membership changed.'),
 'W08-IR-008':('corrected_pending_peer','Four named aliases retyped REJECTED_LABEL on the two phosphate owners, preserving exact text/source and prior 1215 stock-label and 1216 molybdate repairs. No malformed source occurrence is silently normalized.'),
 'W08-IR-010':('corrected_pending_peer','Exact original full Thermo batch7 copied and bound at its original access time. All three cases and the proposal use this claim-specific evidence. The property retrieval timestamp now agrees with batch7; old batch6 remains explicitly historical/incomplete.'),
 'W08-IR-011':('corrected_pending_peer','Case63 missing_requirement now retains only the unresolved seven-water material/source-correction fact. M2231 already establishes 6 g plus 1 L input recipe and 5 ml receiving dose; no repeated dose research is deferred.'),
}
rows=[]
for f in frozen_findings['finding_groups']:
    if f['finding_id'] not in assigned: continue
    status,text=conclusions[f['finding_id']]
    lineage=[]
    for obs in f['observations']:
        original=obs.get('observation',{})
        lineage.append({'path':obs['path'],'sha256':obs['sha256'],'selector':obs['selector'],
          'original_finding_id':original.get('finding_id'),'original_reviewer':original.get('reviewer'),
          'original_severity':original.get('severity'),'original_status':original.get('status')})
    rows.append({'finding_id':f['finding_id'],'title':f['title'],'normalized_severity_preserved':f['severity'],
      'historical_status_preserved':f['status'],'original_observation_lineage':lineage,
      'known_issue_preserved':f['known_issue'],'author_disposition':status,'assessment':text,
      'independent_approval':False,'holds_released':False})
save('issue-dispositions.json',{'findings_capture':{'path':str((S/'inputs/external-review/findings.json').relative_to(R)),'sha256':sha(S/'inputs/external-review/findings.json')},'rows':rows,
  'authority':'Author correction receipt. Historical reviewer identities and severities remain unchanged. Root coordinates current issues; this author did not mutate GitHub.'})

ref=json.loads((S/'inputs/coordinator-triage/completeness-adjudication-refinement.json').read_text())
refrows=[]
for row in ref['rows']:
    p=byp.get(row['proposal_id'])
    target='COMPLETE' if row.get('root_triage_recommendation')=='COMPLETE_FOR_LITERAL_PRINTED_INPUT_LIST' else row['recommended_completeness']
    refrows.append({'proposal_id':row['proposal_id'],'cohort_scope':'assigned' if p else 'other_author',
      'original_adjudication':row['adjudication'],'original_recommended_completeness':row['recommended_completeness'],
      'root_triage_recommendation':row.get('root_triage_recommendation'),'effective_recommendation':target,
      'action':'applied or retained per exact scoped source judgment' if p else 'read and left to assigned author; no mutation',
      'reason':row.get('root_triage_reason',row['reason'])})
save('completeness-refinement-ledger.json',{'counts':ref['counts'],'rows':refrows})

# Record what was actually read this correction, separately from preserved past research.
inspection=[json.loads(x) for x in (O/'inspection-log.jsonl').read_text().splitlines()]
seen=set();reads=[]
for x in inspection:
    key=(x['kind'],x['sha256'])
    if key in seen:continue
    seen.add(key)
    eid=x['kind'].split(':',1)[1] if x['kind'].startswith('primary:') else None
    e=OLD_E.get(eid,{})
    reads.append({**x,'read_status':'scientifically_inspected' if eid else 'entire_selected_owner_inspected',
      'evidence_id':eid,'url':e.get('url'),'original_accessed_at':e.get('accessed_at'),
      'locator':e.get('locator'),'limitation':'A displayed source failure is an inspected failure, not inspected unavailable content. Whole-payload reading does not approve retained roles or release.'})
reads.append({'kind':'primary:if1227-thermo-full-batch7','path':str(R/next(e for e in E if e['evidence_id']=='if1227-thermo-full-batch7')['capture']['path']),
 'sha256':disposition['active_capture']['sha256'],'read_status':'scientifically_inspected','url':'https://www.thermofisher.com/order/catalog/product/040320.22',
 'original_accessed_at':disposition['active_original_accessed_at'],'locator':'Thermo product section lines 103–105,147–154; original full batch7 copy',
 'scope':'Name, CAS, formula, mass, IUPAC, SMILES and hydrate count inspected; no new supplier retrieval.'})
save('source-read-ledger.json',{'author':'/root/inorganics','read_entries':reads,
 'frozen_case_scope':{'capture':{'path':'provenance/shard-08.json','sha256':sha(R/'provenance/shard-08.json')},'case_ids':A['case_ids'],
 'read_scope':'All 80 active decisions and raw occurrence contexts reread. Truncated long-context displays were followed by bounded follow-ups; automatic role/ontology suggestions are not primary chemical authority.'},
 'prior_primary_review_scope':'The earlier primary and independent scientific source review remains preserved in active issue1201 evidence and historical receipts. This bounded correction does not claim to have newly fetched or reread every historical external source; changed claims are tied to actual read captures above.',
 'whole_payload_count':len({x['sha256'] for x in reads if x['kind']=='whole_selected_payload'})})

# Failure-oriented invariant controls run on deep copies, never on scientific files.
def invariant(d,p):
    assert [x['case_id'] for x in d]==A['case_ids']
    assert [x['proposal_id'] for x in p]==A['proposal_ids']
    for x,y in zip(d,A['decisions']):
        for k in ['source','case_input_sha256','occurrence_ids','preserved_native_decisions','preserved_holds']:
            assert x.get(k)==y.get(k)
        assert x['independent_review']['status']=='pending'
    for x,y in zip(p,A['proposals']):
        for k in ['kind','owner_path','before_sha256','case_ids']:
            assert x[k]==y[k]
        assert sha(R/x['after_capture']['path'])==x['after_capture']['sha256']

controls=[]
invariant(D,P);controls.append({'name':'positive exact final fragment','passed':True})
for name,mutate in [
 ('omitted case',lambda d,p:d.pop()),
 ('wrong occurrence',lambda d,p:d[0]['occurrence_ids'].append('CM_OCC:wrong')),
 ('wrong source',lambda d,p:d[0]['source'].update(source_label='wrong')),
 ('wrong frozen digest',lambda d,p:d[0].update(case_input_sha256='0'*64)),
 ('wrong before hash',lambda d,p:p[0].update(before_sha256='0'*64)),
 ('stale payload hash',lambda d,p:p[0]['after_capture'].update(sha256='0'*64)),
 ('duplicate proposal',lambda d,p:p.append(copy.deepcopy(p[0]))),
 ('self scientific approval',lambda d,p:d[0]['independent_review'].update(status='complete')),
]:
    d,p=copy.deepcopy(D),copy.deepcopy(P);mutate(d,p)
    try:invariant(d,p)
    except AssertionError:controls.append({'name':name,'passed':True,'result':'rejected'})
    else:raise AssertionError('Control did not reject: '+name)
diff=subprocess.run(['git','diff','--exit-code','--','data','src','MAPPING_SEMANTICS.md'],capture_output=True,text=True)
assert diff.returncode==0
validation=json.loads((O/'validation.json').read_text())
finalchecks=[]
all_e={**OLD_E,**{e['evidence_id']:e for e in E}}
allowed={'primary_source','source_snapshot','ontology','native_record_review','independent_review','unsuccessful_search','local_validation'}
for e in E:
    assert e['kind'] in allowed
    assert sha(R/e['capture']['path'])==e['capture']['sha256']
for p in P:
    assert all(eid in all_e for eid in p['evidence_ids'])
    assert all(p['proposal_id'] in bycase[c]['proposal_ids'] for c in p['case_ids'])
for d in D:
    assert all(eid in all_e for eid in d['evidence_ids'])
    assert all(d['case_id'] in byp[pid]['case_ids'] for pid in d['proposal_ids'])
save('final-validation.json',{'timestamp':NOW,'mechanical_only':True,'passed':True,'native_validation':{'path':'validation.json','sha256':sha(O/'validation.json'),'passed':validation['passed']},
 'negative_controls':controls,'maintained_surface_diff_exit':diff.returncode,
 'all_new_capture_hashes_and_evidence_kinds':'pass','all_case_proposal_evidence_backlinks':'pass',
 'case_hashes':{d['case_id']:objsha(d) for d in D},'payload_hashes':{p['proposal_id']:p['after_capture']['sha256'] for p in P},
 'final_artifacts':{n:sha(O/n) for n in ['decisions.json','proposals.json','evidence-additions.json','evidence-category-ledger.json','component-reference-ledger.json','case-assessment.json','full-payload-assessment.json','issue-dispositions.json','source-read-ledger.json','evidence-dispositions.json']}})
print(json.dumps({'passed':True,'cases':len(D),'proposals':len(P),'controls':len(controls),'artifacts':{n:sha(O/n) for n in ['decisions.json','proposals.json','evidence-additions.json','final-validation.json']}}))
