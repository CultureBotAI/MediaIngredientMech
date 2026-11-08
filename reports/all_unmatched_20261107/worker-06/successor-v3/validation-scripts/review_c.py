from pathlib import Path
import json,yaml,hashlib,datetime
R=Path('reports/all_unmatched_20261107/worker-06');S=R/'successor-v3';C=S/'research-c';O=S/'research-root/review-c'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(p):return json.loads(p.read_text())
D=read(C/'decisions-v2.json')['decisions'];P=read(C/'proposals.json')['proposals'];E=read(C/'evidence.json');OLD={p['proposal_id']:p for p in read(R/'successor-v2/final/proposals.json')['proposals']};FD=read(Q/'shards/shard-06.json')['cases'];OD=read(R/'successor-v2/final/decisions.json')['decisions'];bycase={d['case_id']:i for i,d in enumerate(FD)}
analyses={
'A-P-JCM1136-548-GLUCOSE-1M':'JCM548/1136/1406/1412 explicitly name 1M glucose with their own stock addition/autoclaving/anaerobic handling. The four full recipe tables place water in basal media, not in a separately specified glucose stock recipe. Only generic glucose at1M remains as literal input; water omission preserves the source gap, unknown starting form and separate storage instructions. None of the stated gas handling is converted to a dissolved gas component.',
'B-P-JCM977-glucose20':'The exact JCM977 table places790ml distilled water in VNG base and separately adds100ml of20%(w/v)glucose after cooling. That table provides no stock solvent identity. Omission of Water and retention of glucose20%w/v, UNKNOWN closure and unspecified form/volume are supported. The candidate case64 initially retained an aqueous claim; decisions-v2 corrects that exact residual without changing source bytes.',
'C-P-JCM1375-1435-825-GLUCOSE10':'JCM1375/1435/825 each specify10%glucose sterile anaerobic stock, with100/5/50ml receiving additions respectively. None specifies w/v or stock solvent. The PERCENT unit, unspecified form and solvent, and distinct autoclaved preparation are preserved; no equivalence with ETSA filter-sterile stock is inferred.',
'C-P-TOGO2790-GLUCOSE20':'TOGOM2790 narrative names2.5ml of20%glucose per100ml receiving M9medium. Water in basal/salt/trace-metal tables supplies no stock solvent formula. PERCENT rather thanPERCENT_W_V and unspecified sterilization/form/volume remain appropriate; omission of inferred Water does not collapse stock to dry glucose.',
'C-P-JCM1435-YEAST10':'JCM1435 explicitly names10%Yeast extract(Oxoid)solution5ml among sterile anaerobic stock additions. It does not specify stock solvent, percentage basis, catalogue or lot. The one literal Oxoid yeast-extract component and UNKNOWN closure preserve both the product qualifier and these independent unknowns.',
'C-P-TOGO2568-GLUCOSE10':'TOGOM2568 lists10ml10%glucose among freshly prepared filter-sterilized solutions after basal cooling to55C. Its separate hemin/menadione solvents cannot be imported into glucose stock. The proposal keeps PERCENT, unspecified solvent/form/stockvolume and fresh filtration, without conflating autoclaved JCM stock.',
'C-P-JCM1009-GLUCOSE20':'JCM1009 explicitly names0.1ml20%(w/v)glucose per5ml medium from an anaerobic stock stored underN2, with the unstarred autoclaving instruction. Basal water does not identify stock solvent. Unknown solvent/form/volume remain, gas handling is an instruction, and differing JCM977 preparation remains separate.'}
pr=[]
for p in P:
    old=OLD[p['proposal_id']];a=yaml.safe_load((R/old['after_capture']['path']).read_text());b=yaml.safe_load((R/p['after_capture']['path']).read_text())
    assert sha(R/p['after_capture']['path'])==p['after_capture']['sha256']
    assert b['components']==[x for x in a['components'] if x['component_name']!='Water']
    assert b['identifier']==a['identifier'] and b['ontology_mapping']==a['ontology_mapping']
    assert b['curation_history'][:-1]==a['curation_history'] and b['curation_history'][-1]['llm_assisted'] is True
    assert b['component_assertion']['method']=='RECIPE_TRANSCRIPTION' and b['component_assertion']['completeness']=='UNKNOWN'
    pr.append({'proposal_id':p['proposal_id'],'before_capture':old['after_capture'],'after_capture':p['after_capture'],'case_ids':p['case_ids'],'review_verdict':'acceptable_bounded_proposal_with_explicit_unknowns','independent_reasoning':analyses[p['proposal_id']]})
case_assessments=[]
for d in D:
    i=bycase[d['case_id']];f=FD[i]
    assert d['case_input_sha256']==digest(f) and d['occurrence_ids']==[x['occurrence_id'] for x in f.get('occurrences',[])]
    assert d['source']==OD[i]['source']
    desc='Exact source outcome agrees with the explicitly bounded stock/payload assessment above; original raw labels, source IDs and every occurrence remain. No stock solvent or gas composition is inferred.'
    if i==15:desc='The original381body is successful and explicitly links379 without peptone. The captured379D-glucose constituent therefore remains applicable. Correcting metadata toprimary_source and binding the original body, with separate old retrieval index and timestamp, resolves006 without changing D-glucose identity. Other D-glucose source contexts are not reinterpreted.'
    if i==91:desc='The exact frozen concentration is1000ML_PER_L and TOGO2414 supplies1L wholeTSYbroth. Corrected reasoning agrees; no named constituent formula or supplier identity is inferred. The whole-broth formulation remains unknown.'
    if i==111:desc='All40 frozen occurrences preserved. Four raw JCM737/876/887/955bodies sayNothing found. Archived MediaDive J737/4668,J876/4863,J955/4977 independently identify compound1784 at1/10/10ml, with explicitJCMcollection links. These are alternatives, not retroactively successful JCMrequests. J887 root occurrence remains frozen-only; solution4878 is not assignedJ887 without a bridge. PositiveJCM197 formulation and allsource-dose holds persist.'
    if i==152:desc='MediaDive1886response hasdata.media=[]and frozen record has no originating collection. Matching187digits cannot establishJCM187. The revisedunresolved outcome and removedKGbacklink preserve independently supportedCMJCM187contexts; listedowner is only an inspectedcandidate.'
    if i==161:desc='Exact J240compound1507row is1g; capturedDSMZ1682and1837rows are6.7g. Revisedreasoning andno-change explanation retain the correctper-source quantities, withoutchoosing universalYNBgrade/exclusions/SKU.'
    case_assessments.append({'case_index':i,'case_id':d['case_id'],'reviewed_candidate_decision_sha256':digest(d),'verdict':'acceptable_scoped_source_outcome_with_holds','independent_reasoning':desc})
ev=[]
oldE={x['evidence_id']:x for x in read(R/'successor-v2/final/evidence.json')['evidence']}
for e in E['replacements']:
    assert e['accessed_at']==oldE[e['evidence_id']]['accessed_at'];assert sha(R/e['capture']['path'])==e['capture']['sha256']
    body=(R/e['capture']['path']).read_text()
    if e['evidence_id']=='A-E-CAPTURE-121':assert e['kind']=='primary_source' and '379' in body and len(body.encode())==1094
    else:assert e['kind']=='unsuccessful_search' and 'Nothing found' in body
    ev.append({'evidence_id':e['evidence_id'],'kind':e['kind'],'capture':e['capture'],'original_accessed_at':e['accessed_at']})
assert 'aqueous' not in next(d for d in D if bycase[d['case_id']]==64)['reasoning']
captures=['A-E-CAPTURE-100','A-E-CAPTURE-127','B-http-4f360397f0c066dd','C-E-jcm-1375','C-E-jcm-1435','C-E-jcm-825','C-E-jcm-1406','C-E-jcm-1412','C-E-togo-M2790','C-E-togo-M2568','C-E-jcm-1009','A-E-CAPTURE-120','A-E-CAPTURE-121','R-medium-J737','R-medium-J876','R-medium-J955','R-ingredient-1886','R-medium-J240','R-medium-1682','R-medium-1837','B-http-ead203864a2e62b5']
source_refs=[{'evidence_id':eid,'capture':oldE[eid]['capture'],'original_accessed_at':oldE[eid].get('accessed_at')} for eid in captures if eid!='A-E-CAPTURE-121']
source_refs.append({'evidence_id':'A-E-CAPTURE-121','capture':E['replacements'][0]['capture'],'original_accessed_at':E['replacements'][0]['accessed_at']})
out={'reviewer':'/root','current_payload_and_outcome_author':'/root/research_c','independence':'distinct_reviewer_from_successor_author; root originally authored some historical KGcontexts but did not author these corrections','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete','open_findings':0,'initial_finding_disposition':{'finding_id':'V3-ROOT-C-004-RESIDUAL','status':'corrected_in_selected_decisions_v2','prior_receipt':{'path':str(O/'initial-review-v1.json'),'sha256':sha(O/'initial-review-v1.json')},'reinspection':'Read exact corrected reasoning, which now states200g/Lstockwithunspecifiedsolvent; all other13decisions and7payloads remain unchanged.'},'inputs':{str(p.relative_to(R)):sha(p) for p in [C/f for f in ['proposals.json','decisions-v2.json','evidence.json','proposal-metadata-patches.json','source-analysis.json','receiving-occurrence-limits.json','source-boundary-supplement.json','author-receipt-v2.json']]},'proposal_assessments':pr,'case_assessments':case_assessments,'evidence_metadata_assessments':ev,'primary_source_read_bindings':source_refs,'limits':['Review covers finalsevenchangedpayloads,14sourceoutcomes, fiveevidencecorrections andthreeboundedproposalmetadataamendments; no wholeowner/role/exportapproval.','Original source doses, stock forms, percent bases, final volumes and gas-content unknowns remain explicit.','Other D-glucose contexts41/124 retain unchanged exactpayload/sourceassessments and original accessholds;381 evidence is not generalized to those cases.','Final merged ledgers and alias/source overlap atcase111 require separate assembly/binding review.'],'scientific_review':True,'source_owner_export_approval':False}
dest=O/'final-review-v2.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(sha(dest))
