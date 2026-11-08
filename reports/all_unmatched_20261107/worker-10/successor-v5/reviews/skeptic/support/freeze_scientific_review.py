from pathlib import Path
import datetime,hashlib,json
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';P=R/'.temp/all-unmatched-worker-10/successor-v5/skeptic';O=S/'reviews/skeptic'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_bytes());bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
initial=load(P/'source-scope-review-v1.json');v=load(P/'candidate-verification-v1.json');assert not initial['failures'] and v['status']=='PASS' and not v['failures']
assert sha(S/'proposed/Calf_Blood_TOGO_M2854.yaml')=='7a54c5bb03008949dec5ced0fbb8da9deee348fd4ad2473e66d41655db975b9d'
O.mkdir(parents=True,exist_ok=True);(O/'support').mkdir(exist_ok=True);support=[]
for n in ['inspect_source_scope.py','source-scope-review-v1.json','verify_candidate.py','candidate-verification-v1.json','freeze_scientific_review.py']:
 src=P/n;dst=O/'support'/n
 with dst.open('xb') as f:f.write(src.read_bytes())
 assert sha(src)==sha(dst);support.append({'original':bind(src),'published_copy':bind(dst),'byte_exact':True})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
report={
 'review_id':'w10-successor-v5-calf-wording-independent-scientific-v1',
 'reviewed_at':now,
 'actual_review_start_exact':None,
 'earliest_recorded_assessment_milestone':initial['recorded_at'],
 'timing_note':'The initial receipt is a recorded assessment milestone after source reading began, not a recovered exact reading start. Candidate verifier execution times describe that execution only. This reviewed_at records report completion.',
 'status':'PASS_BOUNDED_CORRECTION',
 'reviewer':'Codex /root/preparation_skeptic (AI), worker10',
 'candidate_author':'Codex worker10 /root (AI)',
 'author_independent':True,
 'prior_involvement':initial['prior_involvement'],
 'scientific_review':True,
 'scientific_review_scope':'Only the current explanatory distinction between blood material and serum, the developmental-origin qualifier calf, and withdrawal of the unsupported source-explicit whole qualifier. Complete payload/case/proposal objects and all retained-byte bindings were checked. Identity, ontology grounding, aliases, source applicability, processing, roles and export acceptance are not newly approved.',
 'predecessor_head':initial['predecessor_head'],
 'reviewed_payload':v['author_freeze']['payload'],
 'predecessor_payload':{'path':'reports/all_unmatched_20261107/worker-10/successor-v3/enum/proposed/sv1-bio-calf_blood_togo_m2854.yaml','sha256':'62f0dc3300c488be2fb9d52f2c65e8e6826715d81177cf8e4ce48af422ed7338','authentication':'Exact committed blob at82fc29d837a223edb9c436445ec7ea13d2840c7b and identical selected working-tree/triage copy.'},
 'input_bindings':[bind(S/n) for n in ['author-freeze.json','proposed/Calf_Blood_TOGO_M2854.yaml','author-core/decisions.json','author-core/proposals.json','author-core/evidence.json','payload-change-proof.json','payload.diff','source-assessment.json','inputs/issue1237-filed-finding.json','inputs/original-finding.json','inputs/source.json','inputs/payload.yaml']],
 'contract_bindings':initial['contract_bindings'],
 'targets':[
  {'kind':'proposed_payload','proposal_id':'sv1-bio-calf_blood_togo_m2854','path':'reports/all_unmatched_20261107/worker-10/successor-v5/proposed/Calf_Blood_TOGO_M2854.yaml','owner_path':'data/ingredients/mapped/Calf_Blood_TOGO_M2854.yaml','ownership_note':'Unapplied proposed new owner; this review approves only the bounded explanation correction, not application or whole-owner acceptance.','field_paths':['notes','ontology_mapping.evidence[0].notes','curation_history appended event']},
  {'kind':'case_snapshot','path':'reports/all_unmatched_20261107/worker-10/successor-v5/author-core/decisions.json','selector':'$.decisions[44]','case_id':v['full_case_after']['case_id'],'occurrence_ids':v['full_case_after']['occurrence_ids'],'scope':'Current reasoning and bounded_scientific_conclusion repeat the same corrected explanation; all identity/routing and existing holds remain exact.'},
  {'kind':'selected_proposal_metadata','path':'reports/all_unmatched_20261107/worker-10/successor-v5/author-core/proposals.json','proposal_id':'sv1-bio-calf_blood_togo_m2854','scope':'Exact selected payload binding, current description, pending review state and preserved historical provenance.'}
 ],
 'source_assessment':{
  'evidence':initial['source_evidence'],
  'source_capture_sha256':'12f6464a1dcc66a32160e85433034cfd067ea5e930f3ae6d12ce2c60d6af2770',
  'source_locator':'Complete capture; specifically components[0].items[1], meta.name and comments[0]',
  'positive_fact':'The captured TOGO M2854 recipe names calf blood at literal10%, as a separate addition to brain-heart infusion agar with antibiotics.',
  'interpretation':'Blood denotes the material rather than serum; calf qualifies developmental origin. The developmental qualifier does not distinguish blood from serum. The source does not literally say whole. No blood processing protocol, supplier/product or percentage basis is established by this capture.',
  'source_context_limits':initial['source_scope_constraints'],
  'new_primary_retrieval':False,
  'full_source_and_case_objects':'Preserved in the byte-exact source-scope support receipt; this review inspected the complete source, original case and frozen receiving recipe.'
 },
 'exact_diff_conclusion':{
  'payload':'The complete successor restores exactly to the authentic predecessor, including raw serialized YAML, after restoring the two original current note values and removing the single appended correction event. No other field or formatting change remains.',
  'current_notes_after':{'notes':v['full_payload_after']['notes'],'ontology_mapping.evidence[0].notes':v['full_payload_after']['ontology_mapping']['evidence'][0]['notes']},
  'appended_history':v['full_payload_after']['curation_history'][-1],
  'original_history':'Both prior events, including the historically erroneous CREATED explanation and subsequent issue1226 provenance correction, are retained verbatim. The new event explicitly corrects the active explanation without rewriting history.',
  'case_and_proposal':'Only case44 and its existing selected proposal change in the author-core. Corrected explanation is identical across the active record, mapping evidence, case reasoning, bounded conclusion and proposal description; old note suffixes and all source/role/export holds remain.',
  'author_review_state':'Correctly pending separate exact review at the author freeze, with actual prior independent-review objects retained in wording_successor. No retroactive transfer of earlier approval.',
  'counts':v['counts'],
  'all127_payload_bindings':v['all127_payload_bindings']
 },
 'finding_dispositions':[{'finding_id':'W10-SV3-SKEPTIC-CALF-BLOOD-WORDING','original_severity':'minor_explanation_error','original_finding':bind(S/'inputs/original-finding.json'),'filed_reference':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6719103915','disposition':'Corrected in the exact isolated candidate and active case/proposal explanation. Original historical field values and finding remain preserved. No GitHub closure or terminal native historical-finding disposition is asserted here.','bounded_effect':'Wording correction only; the local identity and broader blood mapping remain unchanged and are not renewed as whole-owner approval.'}],
 'new_unexpected_findings':[],
 'retained_unknowns_and_holds':['Defibrination, lysis, other processing, supplier/product and literal10% basis remain unknown.','Culture incubation/gas conditions are not treated as blood processing. Imported PERCENT_W_V remains raw receiving-recipe context, not primary-source basis evidence.','No new whole-blood source claim, product, synonym, resolved generic label, role or fraction-processing protocol is introduced.','All source-specific applicability, one CM occurrence, identifiers, broader mapping quality, LLM_SUGGESTION provenance and original source URLs remain exact.','Other187 decisions and126 proposals/payloads, including ISP4, carbonate UNKNOWN successor and pure-carbonate alias rejection, remain exact; other unresolved scientific and integration obligations are not reapproved.'],
 'verification':{'initial_source_checks':initial['check_count'],'candidate_and_retention_checks':v['check_count'],'failures':[],'native_closed_schema':'Independently executed on the complete changed candidate; zero errors.','root_native_validation':'Separate root receipt not yet relied on by this frozen report. Final native wrapper and full assembly are reviewed separately when available.','support_copies':support},
 'finalization_limit':'Root may attach this exact report to current review bindings. Final core, native wrapper and handoff bytes require their own separate metadata check. No future commit or published-head acceptance is inferred.',
 'approval_limits':{'whole_owner':False,'role':False,'export':False,'maintained_application':False,'future_published_head':False,'git_or_github_mutation':False}
}
with (O/'scientific-review-v1.json').open('x') as f:json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
with (O/'scientific-review-v1.md').open('x') as f:
 f.write(f'''Independent calf-blood wording review by Codex /root/preparation_skeptic (AI), completed {now}.\n\n**PASS, bounded correction.** The complete captured TOGO M2854 source names calf blood at a literal 10% receiving dose. Blood identifies the material rather than serum; calf specifies developmental origin. The source does not explicitly say whole or establish processing, supplier/product or percentage basis.\n\nThe exact candidate `7a54c5bb03008949dec5ced0fbb8da9deee348fd4ad2473e66d41655db975b9d` changes only the two current explanatory note fields and appends one truthful AI-assisted history event. All earlier history remains verbatim. Case44 and its proposal repeat the corrected explanation while retaining routing, identity, provenance, unknowns and holds. All 187 other decisions, 126 other selected proposals/payloads and 304 occurrence bindings remain exact.\n\nNineteen source/predecessor checks and 675 candidate/retention checks pass, including fresh native closed-schema validation. Full before/after objects, source context and reproducible scripts are copied unchanged under `support/`.\n\nI authored the original wording finding and previously reviewed this payload, but did not author the original payload or root correction. This review is independent of the candidate author, not historically uninvolved. Fresh science is limited to this explanation. It grants no whole-owner, mapping, role, application, export or future published-head approval. Final assembly/native bindings remain for a separate review.\n''')
print(json.dumps({'status':report['status'],'report':bind(O/'scientific-review-v1.json'),'markdown':bind(O/'scientific-review-v1.md')}))
