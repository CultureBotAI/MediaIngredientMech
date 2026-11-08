"""Freeze author-stage technical report; final native assembly is separate."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
P=Path(__file__).resolve().parent;R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7'
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ref(p):return {'path':str(p),'sha256':sha(p)}
def save(n,x):
 with (P/n).open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
x=read(P/'author-v2-checks/checks.json');v3=read(P/'author-v3-rebind.json');command=read(P/'author-v2-command.json');base=read(P/'baseline-v1.json');freeze=read(S/'author-freeze-v3.json')
assert x['status']==v3['status']=='PASS' and command['exit_code']==0 and all(c['pass'] for c in x['checks']+v3['checks'])
report={
 'review_id':'worker10-sv7-author-technical-v1','status':'complete','verdict':'pass_with_limitations','scientific_review':False,
 'reviewer':'worker10:/root/buffers_research','author':'worker10:/root','reviewed_source_head':'c66d6d3665368fe1ae8986fb7c16340a103582c1','active_author_freeze':ref(S/'author-freeze-v3.json'),'core':v3['author_v3_core'],
 'independence':{'current_author_independent':True,'prior_authorship':'I authored the original W10 Tris/HCl0.2M DSM273 and HEPES2M JCM556/1200 proposals, other buffer/HCl proposals and later serum corrections. This is a technical/metadata preservation and native process review; it does not independently approve my original source science. Separate preparation_skeptic owns the primary scientific review.','columbia_authorship':'I did not author the original W10 Difco/Oxoid proposals, current root Columbia dependency or W04 origin; earlier W10 retention/native reviews remain disclosed context.','W04_origin':'Actual Git proposal and payload verified read-only. Its source authorship and proposal origin are preserved, not transferred to W10 or counted as independent approval of this correction.'},
 'timing':{'baseline_recorded_at':base['at'],'native_run_started_at':x['started_at'],'native_run_finished_at':x['finished_at'],'native_runtime_seconds':x['runtime_seconds'],'metadata_rebind_started_at':v3['started_at'],'metadata_rebind_finished_at':v3['finished_at'],'metadata_runtime_seconds':v3['runtime_seconds'],'review_finished_at':datetime.now(timezone.utc).isoformat(),'qualification':'Contract and complete payload reads occurred before and between these executions. Baseline is the earliest retained technical milestone, not a claimed exact first mental-review time.'},
 'counts':x['counts'],'checks_passed':len(x['checks'])+len(v3['checks']),'findings':[],
 'full_payload_review':[
  {'proposal_id':r['proposal_id'],'payload_sha256':r['after_capture']['sha256'],'technical_scope':'All fields parsed under native closed schema; complete original/current object delta enumerated, all history retained, exact new event reconstructed through actual native helper, full guarded serialization byte-equal. Source prose read in full but scientific judgment assigned separately.'}
  for r in freeze['unchanged_four_payloads']
 ],
 'field_assessment':{
  'generic_0118':'Same owner path, identifier UNMAPPED_0118, generic preferred label, UNMAPPED status, NAMED_MEDIUM type, occurrence statistics and original five events retained. Exact two vendor strings and source values retained; only their types become REJECTED_LABEL plus explicit appended notes/history. No ontology/formula/component/supplied-form/role added.',
  'Difco':'Only one exact original sourced BD-Difco vendor alias, appended notes and truthful history change. Identifier, source-qualified term, supplier, all seven complete component objects, CURATED_INTERPRETATION/COMPLETE nominal-name-list assertion/evidence, quantities and historical constraints retained. New-owner kind and null beforeimage retained.',
  'two_buffers':'Only component_assertion.completeness PARTIAL→UNKNOWN and one native history event each. Every other field, including component name/scope, evidence, method, quantities, source, identity, pH/strength, chemistry and source uncertainty is exact. No blanket change to other stocks.',
  'Oxoid':'Entire37e8 payload exact. Proposal gains genuine dependency/routing metadata only; W04 current4a3d authored origin and5846 prototype are read-only external inputs, not W10 installation candidates.',
  'held_origins':'No whole-owner/role/export approval. Generic providercompound2046 has no global identity; four1L prepared-base contexts remain held. W04 source300 retains VARIABLE and CM0331; W10 source921 retains39g without an inferred historical catalogue. Central single-family composition remains required.'},
 'native_results':{
  'schema':{'fresh_selected_records':128,'violations':0,'scope':'Closed schema for complete selected payloads, no unrelated full suite.'},
  'guarded_history_roundtrips':x['history_calls'],
  'partonomy':{'predecessor_records':3037,'successor_records':3037,'violations':x['partonomy'],'active_identifier_membership_unchanged':True,'no_external_W04_or_prototype_owner_inserted':True,'owner_admission_is_separate':True},
  'aliases':{'actual_label_index_emitted_private':True,'generic_vendor_labels_nonresolving':True,'exact_Difco_alias_resolving':True,'relevant_rows':x['label_index_relevant_rows'],'reverted_rejected_label_control_detected':True},
  'projection':{'real_Claw_producer':True,'full_overlay_owner_index':True,'actual_differences':x['projection_differences'],'generic_unmapped_owner_rows':0,'mapped_own_identity_rows':3,'rule_D_positive_violations':0,'rule_D_degraded_identity_rejections':len(x['RuleD_negative_rejections']),'no_maintained_export_or_publisher':True},
  'controls':x['negative_controls'],'controls_limit':'Native writer and partonomy reject invalid shape/references; exact full-field guards and native resolution behavior detect schema-valid provenance or scope drift. These are not scientific proof.'},
 'lineage':{
  'all_old_membership':'188case IDs and all304occurrence memberships preserved.124oldpayloads and123oldproposalobjects exact;184othercaseobjects exact;1218old evidence entries exact prefix.',
  'new_dependency':'Only added ID sv7-dependent-columbia-unmapped0118-partition is edit_existing_owner with authentic29ed preimage. It is attached to existing cases118/178, no new source case.',
  'v2_to_v3':'Only two explicit historical/current completeness marker additions. Both original completion_reassessment objects remain exact; active selected payload completeness UNKNOWN is bound.186othercaseobjects plus all proposal/evidence/payload bytes exact between v2/v3.',
  'real_external_origin':v3['W04_origin'],
  'seven_contexts':v3['source_contexts'],
  'draft_corrections':'The initial overly broad new-evidence associations and later historical-enum ambiguity were recorded before their append-only author metadata corrections. Their preserved findings are not erased; no payload changes were required.',
  'pending_native_review':'Current author-core independent_review pending is appropriate at this stage. Final reviewed pointers, native review and handoff require a separate final assembly check.'},
 'retained_limits':['Scientific review is not performed or replaced by this technical report, particularly for my original buffer proposals.','All inherited source/form/physical/quantitative/owner/role/export holds remain. Passing partonomy or schema does not waive any known owner-admission or source-routing hold.','No external W04 author case, origin or prototype is installed in the W10 overlay; joint Oxoid reconciliation remains coordinator-owned.','No maintained, shared-source, Git or GitHub mutation, paid research, external session or downstream rebuild was performed.','No future head, final publication, whole-owner or role/export approval. Final assembly review remains outstanding.'],
 'support':[ref(P/n) for n in ['baseline-v1.json','plan-v1.json','author-v2-checks/checks.json','author-v2-command.json','author-v3-rebind.json','check_author_v2.py','bind_author_v3.py']],
 'writes_only':str(P),'frozen_author_review':True}
save('author-technical-review-v1.json',report)
with (P/'author-technical-review-v1.md').open('x') as f:f.write('''# S7 author technical review

**Pass with limitations; no new technical findings.** The exact active author-v3 core is bound in the JSON report.

All128 selected complete payloads pass native closed schema. The four changed payloads reproduce their exact new events through the real history helper and round-trip byte-for-byte through the guarded writer. Both3037-record overlays pass partonomy, with unchanged active identifier membership. Native label projection excludes both vendor labels from generic UNMAPPED_0118 and includes the exact sourced BD-Difco alias on the Difco proposal. Real mapping projection changes only that alias and truthful buffer curator provenance. Eight focused controls and three actual Rule D negatives pass.

The generic owner has its authentic29ed preimage; all vendor new-owner origins retain null beforeimages. The entire W10 Oxoid37e8 payload stays exact. W04's actual7cc3 Git proposal and4a3d payload are verified read-only and are not added to the W10 overlay. All188case/304occurrence memberships and1218old evidence entries remain;124oldpayloads are exact. The v3 clarification changes only two historical/current enum markers and preserves original history.

I authored the original two buffer preparations. This report verifies native behavior, metadata, exact field boundaries and preservation; the separate scientist owns source conclusions. All existing source, prepared-base, nominal-family, owner, role and export holds remain. Final native assembly and publication metadata are not approved by this author-stage report.
''')
files=[ref(p) for p in sorted(P.rglob('*')) if p.is_file() and p.name!='AUTHOR_REVIEW_MANIFEST.json']
save('AUTHOR_REVIEW_MANIFEST.json',{'at':datetime.now(timezone.utc).isoformat(),'files':files,'count':len(files),'scope':'Author-stage technical artifacts only as frozen now; later final-assembly review will be a separate append-only artifact.'})
print(json.dumps({'report':ref(P/'author-technical-review-v1.json'),'markdown':ref(P/'author-technical-review-v1.md'),'manifest':ref(P/'AUTHOR_REVIEW_MANIFEST.json'),'checks':report['checks_passed']},indent=2))
