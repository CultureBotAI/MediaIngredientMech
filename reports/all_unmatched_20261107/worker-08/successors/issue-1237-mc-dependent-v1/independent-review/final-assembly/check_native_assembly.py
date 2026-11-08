"""Independent final assembly readback of the saved native pair and selected core."""
from datetime import datetime, timezone
import hashlib, importlib.util, json, subprocess, traceback
from pathlib import Path
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-08';O=A/'successors/issue-1237-mc-dependent-v1'
P=R/'.temp/mc-dependent-successor-v1/final-review'
PAIR=Path('reviews/structured/20261108T102223Z-w08-mc-dependent-successor/review.yaml')
PID='mc1237-prop-mc-vitamins-dependent';CID='CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
CHECKS=[];INPUTS={}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):INPUTS[str(p)]=sha(p);return json.loads(Path(p).read_text())
def canonical(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def check(ok,description):
 if not ok:raise AssertionError(description)
 CHECKS.append(description)
def main():
 start=datetime.now(timezone.utc).isoformat()
 receipt=read(O/'native/receipt.json');selection=read(O/'selection.json')
 check(sha(R/PAIR)=='f379d8775e739dc728f5646ebdbe76dcc0eef9f479b5d439bae1392fd393f64d','exact final native YAML')
 check(sha((R/PAIR).with_name('review.md'))=='da7656dee99cfe349550dfe6330044f0f9562bd7bfa9d0ef45ae8f7bc7b2ef54','exact final native Markdown')
 spec=importlib.util.spec_from_file_location('mc_native_readback',R/'scripts/record_review.py');native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
 review=native.read_review(R,str(PAIR));native.validate_review(review)
 check(native.render_markdown(review)==(R/PAIR).with_name('review.md').read_text(),'actual native read validate render exact')
 native.assert_current_source(R,review)
 check(review['source']['git_revision']=='a0190fed72b8f5119432003d1f9c84b8c1de7a48' and review['source']['state']=='working_tree','actual source base/state')
 check(len(review['source']['inputs'])==len({x['path'] for x in review['source']['inputs']})==receipt['input_count']==131,'131 unique native inputs')
 for row in review['source']['inputs']:
  path=R/row['path'];check(path.is_file() and not path.is_symlink() and sha(path)==row['sha256'],'native input '+row['path']);INPUTS[str(path)]=row['sha256']
 check(review['scope']['population_size']==1 and review['scope']['reviewed_target_ids']==[PID],'single target coverage does not claim115 fresh science')
 check(len(review['targets'])==1 and review['targets'][0]['target_id']==PID,'exact native target')
 check(review['targets'][0]['path']==str((O/'payloads/Mc_vitamins.yaml').relative_to(R)),'actual selected payload target')
 check(review['targets'][0]['owner_paths'][0]['path']=='data/ingredients/mapped/Mc_vitamins.yaml','actual existing maintained owner')
 check(review['verdict']=='pass_with_limitations' and review['completion']=='completed','bounded completed verdict')
 check(review['scientific_review'] is True,'aggregate scientific flag corresponds to separate actual science receipt')
 check('Root is actual candidate/native-envelope author' in review['reviewer']['independence_basis'],'root author is not independent approver')
 check(review['findings']==[] and 'empty findings does not close' in ' '.join(review['notes']),'no fabricated native closure')
 check(len(review['assessments'])==6 and all(x['target_ids']==[PID] for x in review['assessments']),'six bounded target assessments')
 limits=' '.join(review['limitations'])
 for text in ['maintained owner application','W04/coordinator','No exclusive Mc/CB','UNMAPPED','Other114payloads','TSB/Bacto admission failure','18planningpayloadholds']:
  check(text in limits,'retained native limitation '+text)
 for e in review['evidence']:
  check(e['reference']==e['locator'],'exact local native evidence locator '+e['evidence_id'])
  check(sha(R/e['locator'])==e['snapshot_sha256'],'native evidence digest '+e['evidence_id'])
 check(len(review['evidence'])==18,'18 exact native evidence references')
 selected_core=read(P/'selection-bindings.json')
 check(selected_core['selection_sha256']==sha(O/'selection.json')=='33f0f1f5166e75283a3e0488f6172844002919cc2461a04f2089f8c4f8fedab8','earlier exact full-core receipt remains current')
 for path,digest in selected_core['input_hashes'].items():check(sha(path)==digest,'selected core receipt still exact '+path)
 proposals=read(O/'proposals.json')['proposals'];decisions=read(O/'decisions.json')['decisions']
 proposal=next(p for p in proposals if p['proposal_id']==PID);case=next(d for d in decisions if d['case_id']==CID)
 peer_bindings={}
 for role in ['science','lineage']:
  f=O/f'independent-review/{role}/final-bindings.json';peer=read(f);peer_bindings[role]={'path':str(f.relative_to(A)),'sha256':sha(f)}
  check(peer['selection']['sha256']==sha(O/'selection.json'),'peer final selector '+role)
  check(not peer['open_blocking_findings'],'peer no final blocker '+role)
  if role=='science':
   check(peer['changed_case']['canonical_final_sha256']==canonical(case),'science final case binding')
   check(peer['new_proposal']['canonical_final_sha256']==canonical(proposal),'science final proposal binding')
   check(peer['new_proposal']['payload_sha256']==proposal['after_capture']['sha256'],'science final payload binding')
   check(peer['no_scope_expansion'].startswith('This receipt does not freshly approve other 114 owners'),'science prior-scope restraint')
  else:
   check(peer['final_case_canonical_sha256']==canonical(case),'lineage final case binding')
   check(peer['final_proposal_canonical_sha256']==canonical(proposal),'lineage final proposal binding')
   check(peer['new_payload_sha256']==proposal['after_capture']['sha256'],'lineage final payload binding')
   check(peer['source_route_approval'] is False and peer['owner_merge_approval'] is False and peer['role_export_approval'] is False,'lineage approval limits')
 technical=read(P/'projection-attempt-v3/receipt.json')
 check(sha(O/'validation/projection-attempt-v3/receipt.json')==sha(P/'projection-attempt-v3/receipt.json'),'exact public technical receipt copy')
 copies=read(O/'validation/capture-bindings.json')
 for row in copies:check(sha(row['original_path'])==sha(R/row['published_path'])==row['sha256'],'exact copied technical artifact '+row['published_path'])
 check(sum(technical['negative_controls'].values())==27,'27 actual technical controls')
 audit=read(O/'structural-audit.json');controls=read(O/'accounting-controls.json')
 check(audit['structural_accounting']=='PASS' and audit['accounted_case_count']==188 and audit['proposal_count']==115 and audit['evidence_count']==1114,'root actual structural auditor counts')
 check(audit['scientific_adequacy_or_approval_established'] is False,'root auditor is not scientific approval')
 check(len(controls['actual_checks'])==6 and all(x['native_rejected'] for x in controls['actual_checks']),'six actual root accounting negatives')
 native.assert_current_source(R,review)
 check(sha(O/'payloads/Mc_vitamins.yaml')=='996fc2bfc69284abcbbe75fba6b069bc41fabb3e35c73d5a493de30ab153bcf3','candidate unchanged at seal')
 check(sha(R/'data/ingredients/mapped/Mc_vitamins.yaml')=='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123','maintained owner unchanged')
 INPUTS[str(R/PAIR)]=sha(R/PAIR);INPUTS[str((R/PAIR).with_name('review.md'))]=sha((R/PAIR).with_name('review.md'));INPUTS[str(Path(__file__))]=sha(__file__)
 result={'status':'PASS','review_type':'independent_final_assembly_and_skeptical_technical_review','reviewer':'worker08:/root/inorganics','author':'worker08:/root','started_at':start,'completed_at':datetime.now(timezone.utc).isoformat(),'independence':'Reviewer did not author this Mc payload, core or native envelope. Earlier W08 inorganic authorship and other peer work are disclosed; no independent scientific approval of those earlier authored proposals is made. Mc scientific source assessment is the separate organics receipt; vitamins supplies separate lineage review.','scientific_review':False,'native_pair':receipt,'final_selection_sha256':sha(O/'selection.json'),'counts':selection['counts'],'case_ids':[CID],'proposal_ids':[PID],'full_actual_Mc_payload_read':True,'case_hashes':{CID:canonical(case)},'payload_hashes':{PID:proposal['after_capture']['sha256']},'peer_final_bindings':peer_bindings,'technical_receipt':{'path':str((P/'projection-attempt-v3/receipt.json').relative_to(R)),'sha256':sha(P/'projection-attempt-v3/receipt.json')},'full_core_readback':{'path':str((P/'selection-bindings.json').relative_to(R)),'sha256':sha(P/'selection-bindings.json')},'native_methods_actually_run':['read_review','validate_review','render_markdown','assert_current_source (entry and exit)'],'native_input_count':131,'checks':CHECKS,'input_hashes':INPUTS,'findings':[],'open_blocking_findings':[],'assessments':[{'area':'whole_candidate_and_history','outcome':'supported_technical_implementation','details':'Actual helper/writer replay reproduces the complete candidate bytes. Literal ten names and quantities, nine other references, four original event objects, identity/aliases/roles and source statistics are preserved. UNMAPPED with no ID and the appended truthful event match the bounded reviewed change.'},{'area':'full_selected_core','outcome':'exact_preservation_with_one_dependency','details':'All114 original proposal objects/payloads and1101 evidence objects remain exact;187 other decisions and all320 occurrence IDs remain exact. One genuine nonnull-before Mc edit is tied only to the existing NBRC903 trigger. CB and null-before NBRC903 origins remain unchanged.'},{'area':'scientific_authority_and_routing','outcome':'separate_reviews_bound_no_scope_expansion','details':'Actual independent science and lineage final receipts bind the exact candidate/case/proposal. The external8-case/71CM/84KG-hold/6-exclusion envelope is preserved. Mc-only component assertions are not transferred to JCM/NBRC. W04/coordinator association, duplicate reconciliation, role/export and whole-owner approval remain pending.'},{'area':'native_and_negative_controls','outcome':'supported_with_explicit_limits','details':'Actual native guarded schema, full2956catalog/prior114/new115 overlay partonomy, and27technical controls passed. Six root accounting controls are inspected separately. Known D/DL mismatch passes structural gates; science remains a separate requirement. Actual SSSOM identity/predicate/alias obligations are unchanged, while event-derived source/date provenance changes are explicitly recorded.'},{'area':'final_native_pair','outcome':'bound_and_current','details':'Saved YAML validates and matches derived Markdown using the actual native helper. All131 input hashes and18 native evidence snapshots are current; only one full Mc candidate is the native target. Empty findings does not close existing SCI-TENVIT-003 or other source holds.'}],'limitations':['No maintained application, owner merge, W04 source routing, downstream rebuild, release, CI or fresh acceptance approval.','Other114 proposals receive exact technical preservation only; no fresh scientific review, especially of own prior inorganic proposals.','Prior TSB/Bacto FAILED/HELD and18 planning limits remain.','Two reviewer harness failures are preserved: KG holds were initially counted in the wrong field; whole-row SSSOM equality initially omitted legitimate history-derived source/date changes. Neither is an author source/payload finding.','No full-catalog scientific or complete maintained SSSOM-product pass is claimed.','Native source is a working-tree observation at a0190fed; later committed-head acceptance is coordinator work.'],'author_or_maintained_mutation':False,'Git_GitHub_mutation':False}
 with (P/'final-assembly.json').open('x') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps({'status':'PASS','checks':len(CHECKS),'final_assembly_sha256':sha(P/'final-assembly.json'),'native_input_count':131}))
if __name__=='__main__':
 try:main()
 except BaseException as e:
  with (P/'final-assembly-failure.json').open('x') as f:json.dump({'type':type(e).__name__,'message':str(e),'traceback':traceback.format_exc(),'checks':CHECKS},f,indent=2);f.write('\n')
  raise
