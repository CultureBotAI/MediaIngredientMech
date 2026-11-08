"""Private native review; publishes nothing and never invokes the native saver."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,datetime,importlib.util
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
R=ROOT/'reports/all_unmatched_20261107/worker-09/followups/provenance1226-v1'
PUB=R/'independent-review'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
data=read(OUT/'successor-assessments.json');baseline=read(OUT/'baseline-inspection.json')
for name in ['successor-assessments.json','baseline-inspection.json','preservation.json','claim-context-notes.json','issue-and-provenance-context.json']:
    assert (PUB/name).read_bytes()==(OUT/name).read_bytes(), 'Published copy differs: '+name
spec=importlib.util.spec_from_file_location('w09_review_contract',ROOT/'scripts/record_review.py')
native=importlib.util.module_from_spec(spec);sys.modules[spec.name]=native;spec.loader.exec_module(native)
now=datetime.datetime.now(datetime.timezone.utc);finished=now.isoformat().replace('+00:00','Z')
rid=now.strftime('%Y%m%dT%H%M%SZ')+'-w09-provenance1226-independent'
targets=[]
for p in data['payloads']:
    targets.append({'target_id':p['proposal_id'],'path':p['selected_path'],'label':p['proposal_id'],'kind':'source',
                    'ownership_note':'Complete selected proposal payload. Maintained application and whole-owner/source/role/export approval remain outside this review.'})
for c in data['cases']:
    targets.append({'target_id':c['case_id'],'path':str((R/'effective-decisions.json').relative_to(ROOT)),
                    'selector':'/decisions/'+str(c['index']),'label':c['source'].get('source_label') or c['case_id'],
                    'kind':'snapshot_row','ownership_note':'Exact effective source-case outcome retained from77d6beae; no scientific reassessment or routing/hold release.'})
receipts=[('E-SCHEMA',ROOT/'src/mediaingredientmech/schema/mediaingredientmech.yaml','authority','Current MappingEvidence, EvidenceTypeEnum, ComponentEvidenceTypeEnum and CurationEvent contracts.'),
 ('E-SEMANTICS',ROOT/'MAPPING_SEMANTICS.md','authority','Identity, mapping quality, supplied form and component boundaries remain unchanged by provenance correction.'),
 ('E-ALLOWLIST',R/'inputs/w09-eight-entry-allowlist.json','authority','Eight dispatched complete evidence objects and exact payload/mapping-context attribution bindings.'),
 ('E-HISTORICAL',R/'inputs/w09-preserved-historical-exception.json','record_content','Preserved historical Casamino wrapper and its inherited#263 assertion with unresolved authorship.'),
 ('E-AUDIT',R/'inputs/w02-nine-row-audit-extract.json','prior_review','Exact W02 provenance audit rows; not scientific mapping approval.'),
 ('E-ISSUE',R/'inputs/probes/audit-comment-live.json','primary_source','Actual official issue1226 final-comment API capture read for attribution and correction boundaries.'),
 ('E-BASE',PUB/'baseline-inspection.json','record_content','Independent complete predecessor mapping/history/object rebinding,32payload hashes and187effective case hashes.'),
 ('E-ASSESS',PUB/'successor-assessments.json','record_content','Independent full successor assessments and reconstructed-predecessor proof;8changed24retained187cases.'),
 ('E-PRESERVATION',PUB/'preservation.json','validation','Independent rehash of original reports, planning packet, three sealed private packets and all effective outcomes.'),
 ('E-CONTEXT',PUB/'claim-context-notes.json','record_content','Claim-specific independent attribution and full-owner context limits for each of eight corrected payloads.'),
 ('E-SELECTION',R/'selection.json','record_content','Exact32proposal selection bridge; original IDs and24raw payloads retained.'),
 ('E-PROPOSALS',R/'proposals.json','record_content','Original32proposal objects with only eight selected after_capture bindings changed.'),
 ('E-EFFECTIVE',R/'effective-decisions.json','record_content','Exact byte-identical187case effective hexahydrate-successor ledger.'),
 ('E-OUTCOMES',R/'outcome-retention.json','validation','Case input, raw source, occurrence and outcome-retention bindings.'),
 ('E-FIELDS',R/'allowlist-proof.json','validation','Author complete-field allowlist proof, independently recomputed in E-ASSESS.'),
 ('E-CONTROLS',R/'validation/controls-v2.json','validation','28focused positive/negative controls, with all requested refusal classes and unchanged-unmapped projection control.'),
 ('E-FINAL-CHECKS',R/'validation/complete-successor.json','validation','Final author32payload schema/projection and complete outcome check; scientific renewal explicitly excluded.'),
 ('E-WRITER',R/'tools/correct_provenance.py','record_content','Inspected exact guarded author helper; native schema writer plus exclusive fd wrapper and complete-object allowlist.'),
 ('E-TEST-CODE',R/'tools/test_controls.py','record_content','Actual meaningful test assertions independently read, including stale/fullobject/field/history/science/output boundary cases.')]
extra=[str(p.relative_to(ROOT)) for _,p,_,_ in receipts]
extra += [str((R/'predecessors'/f"{p['proposal_id']}.yaml").relative_to(ROOT)) for p in data['payloads']]
extra += [str(p.relative_to(ROOT)) for p in [R/'preflight.json',R/'predecessor-cores/proposals.json',R/'predecessor-cores/decisions.json',R/'predecessor-cores/evidence.json',R/'inputs/frozen-shard-09.json',ROOT/'scripts/record_review.py',ROOT/'schema/record_review.yaml',ROOT/'src/mediaingredientmech/validation/write_validated.py',ROOT/'src/mediaingredientmech/curate/curation_event.py',ROOT/'src/mediaingredientmech/synonym_policy.py',ROOT/'src/mediaingredientmech/sssom_grading.py']]
inspection=native.inspect_source(ROOT,targets,extra)
inspection['source']['snapshot_id']='W09 exact77d6beaea5793a0a763957b99e8141ff12b216d2 report-only provenance1226 successor;32selected payloads,8type+history changes,187effective outcomes unchanged.'
evidence=[]
for eid,p,kind,summary in receipts:
    evidence.append({'evidence_id':eid,'kind':kind,'reference':str(p.relative_to(ROOT)),
                     'accessed_at':finished,'support':'supports' if kind in ['record_content','authority'] else 'context_only',
                     'summary':summary+' This record supports only the provenance/preservation scope; no renewed chemical/role/export approval.',
                     'snapshot_sha256':sha(p)})
assessments=[]
for i,p in enumerate(data['payloads']):
    n=p['details']['assessment'];summary=n['typing_reason']+' '+n['full_record_context']+' '+n['approval_limit']
    assessments.append({'assessment_id':f'PAYLOAD-{i:03}','area':'provenance','topic':'Complete selected payload provenance and retention',
                        'outcome':'supported','summary':summary,'target_ids':[p['proposal_id']],
                        'evidence_ids':['E-ASSESS','E-BASE','E-SELECTION','E-ALLOWLIST','E-SCHEMA','E-CONTEXT']+(['E-HISTORICAL'] if p['proposal_id']=='ma-casamino-distinct' else []),
                        'details':json.dumps(p,ensure_ascii=False),
                        'dimensions':[{'name':'approval-boundary','value':'Provenance-only; scientific_review=false; no whole-owner release.',
                                       'definition':'Complete payload read and exact preservation do not renew underlying claim approval.','evidence_ids':['E-ASSESS']}]})
for i,c in enumerate(data['cases']):
    assessments.append({'assessment_id':f'CASE-{i:03}','area':'consistency','topic':'Complete effective source-case retention',
                        'outcome':'supported','summary':c['reason'],'target_ids':[c['case_id']],
                        'evidence_ids':['E-ASSESS','E-BASE','E-EFFECTIVE','E-OUTCOMES'],
                        'details':json.dumps(c,ensure_ascii=False)})
ids=[t['target_id'] for t in targets]
checks=[{'check_id':'INDEPENDENT-COMPLETE-INPUTS','name':'Eight changed full payloads,24retained payloads and187effective source outcomes',
         'status':'passed','required':True,'summary':'Independent exact predecessor reconstruction and source accounting pass, including every current target; no source/role/export approval.',
         'target_ids':ids,'evidence_ids':['E-ASSESS','E-BASE'],'command':'.temp/all-unmatched-worker-09/venv/bin/python .temp/w09-provenance1226-successor-v1/independent-review/check_successor.py','exit_code':0},
        {'check_id':'PRESERVED-PACKETS','name':'Original source and prior sealed packets preserved','status':'passed','required':True,
         'summary':'Independent exact member hashes/membership pass for original1233report files,135planning members and437/1730/11215prior private packet members.',
         'target_ids':ids,'evidence_ids':['E-PRESERVATION'],'command':'.temp/all-unmatched-worker-09/venv/bin/python .temp/w09-provenance1226-successor-v1/independent-review/check_preservation.py','exit_code':0},
        {'check_id':'FOCUSED-CONTROLS','name':'Native guarded writer and focused controls inspected','status':'passed','required':True,
         'summary':'Author final28controls pass. Reviewer independently read full helper and test assertions, exact output diffs and final receipt; did not rerun author tests into occupied fixtures.',
         'target_ids':ids,'evidence_ids':['E-WRITER','E-TEST-CODE','E-CONTROLS','E-FINAL-CHECKS']},
        {'check_id':'SCIENTIFIC-RENEWAL','name':'Underlying scientific approval not renewed','status':'not_applicable','required':False,
         'summary':'Authorized task changes provenance only. Source scientific truth, inherited roles, aliases and export gates are preserved, not re-approved.',
         'target_ids':ids,'evidence_ids':['E-ALLOWLIST','E-HISTORICAL','E-CONTEXT']}]
review={'schema_version':'1.0.0','review_id':rid,'kind':'batch','repository':'CultureBotAI/MediaIngredientMech',
        'title':'Independent W09 issue1226 eight-entry provenance successor review',
        'started_at':baseline['checked_at'].replace('+00:00','Z'),'finished_at':finished,
        'reviewer':{'identity':'Codex /root/provenance1226_reviewer','kind':'agent','independence':'independent',
                    'independence_basis':'New in-process reviewer did not author W09 original proposals, this successor, author guard or controls. Full inputs and attribution were independently read; author scientific approvals were not inherited.'},
        'skill':'.claude/skills/review-yaml-record/SKILL.md','completion':'completed','verdict':'pass_with_limitations','scientific_review':False,
        'summary':'All eight authorized MappingEvidence entries now use LLM_SUGGESTION with truthful appended agent-assisted history. Full objects/parent context and remaining scientific fields are unchanged. Historical Casamino ambiguity and all187effective outcomes/32proposal selection are retained; no scientific or export renewal.',
        'source':inspection['source'],'scope':{'description':'All32selected payloads and187effective source outcomes; full8changed payload attribution plus24byte-identical retention.',
             'selection':'Exactly the dispatched eight-entry allowlist and complete accepted77d6beae effective ledger; no target dropped.',
             'coverage':'full','population_size':219,'reviewed_target_ids':ids},
        'targets':inspection['targets'],'checks':checks,'evidence':evidence,'assessments':assessments,'findings':[],'actions':[],
        'limitations':data['limits']+['The three direct-term DATABASE_MATCH alternatives were not selected; no assertion was rewritten or narrowed.',
        'The author and reviewer each initially assumed an optional ontology_mapping on an unchanged unresolved owner. Failed helper probes are retained; explicit no-mapping projection fixed the review helper only. No candidate content or gate was changed for this recovery.',
        'Native writer reservation protects against tested pre-existing/aliased outputs; no atomic eight-file transaction or hostile-concurrency guarantee is asserted.',
        'This review is a working-tree observation at the unchanged77d6beae source base with exact successor hashes. Later commit identity and non-force push are separately verified by the author/coordinator; no Git mutation was performed by this reviewer.',
        'This private native bundle uses the native serializer, strict loader, semantic/source checks and Markdown renderer. The native saver into maintained reviews was not run.'],
        'tags':['w09','issue1226','provenance-only','independent','no-scientific-renewal']}
native.validate_review(review);native.assert_current_source(ROOT,review)
raw=native._dump_document(review);parsed=native.load_document(raw);assert parsed==review
native.validate_review(parsed);native.assert_current_source(ROOT,parsed)
with (OUT/'review.yaml').open('x') as f:f.write(raw)
with (OUT/'review.md').open('x') as f:f.write(native.render_markdown(parsed))
assert (OUT/'review.md').read_text()==native.render_markdown(native.load_document((OUT/'review.yaml').read_bytes()))
result={'reviewer':'Codex /root/provenance1226_reviewer','status':'PASS','review_id':rid,'source_head':inspection['source']['git_revision'],
        'targets':len(targets),'assessments':len(assessments),'inputs':len(inspection['source']['inputs']),'evidence_entries':len(evidence),
        'strict_load':True,'native_semantic_validation':True,'exact_current_source':True,'render_parity':True,'scientific_review':False,
        'native_saver_run':False,'review_yaml_sha256':sha(OUT/'review.yaml'),'review_md_sha256':sha(OUT/'review.md')}
with (OUT/'native-validation.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result))
