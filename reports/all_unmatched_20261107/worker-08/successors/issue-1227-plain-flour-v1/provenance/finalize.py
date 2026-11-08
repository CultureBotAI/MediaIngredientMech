import datetime,hashlib,json,shutil,subprocess
from pathlib import Path
ROOT=Path.cwd();P=ROOT/'.temp/all-unmatched-worker-08/plain-flour-method-v1';A=ROOT/'reports/all_unmatched_20261107/worker-08';O=A/'successors/issue-1227-plain-flour-v1'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
def save(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
assembly=read(P/'independent/final-native-assembly.json')
assert assembly['status']=='PASS',assembly
shutil.copy2(P/'independent/final-native-assembly.json',O/'independent-review/final-native-assembly.json')
shutil.copy2(P/'native-build.log',O/'provenance/native-build.log')
shutil.copy2(P/'finalize.py',O/'provenance/finalize.py')
native=read(O/'native/receipt.json');technical=read(O/'validation/receipt.json')
assert native['status']==technical['status']=='PASS'
for key in ['review_yaml','review_markdown']:
    r=native[key];assert sha(ROOT/r['path'])==r['sha256']
sel=read(O/'selection.json');assert sel['counts']=={'cases':188,'proposals':113,'occurrence_ids':320,'evidence':1082,'changed_payloads':1,'unchanged_payloads':112,'changed_cases':1,'unchanged_cases':187}
assert sha(O/'selection.json')=='335806d22ce278eaf628930b521d7164f0dee2493a19fbc790ae3c273d179f92'
assert sha(ROOT/'.temp/w06-residual-successor-independent-v1/SEAL.json')=='b9eaf3bc9ef39dc36c440fb1330677fa267b1945ba1c65c2b24c4e8d4278226f'
subprocess.run(['git','diff','--exit-code','HEAD','--'],check=True,capture_output=True)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
handoff={
 'created_at':now,'status':'single_filed_correction_reviewed_for_ordinary_publication; coordinator_final_head_acceptance_pending',
 'branch':'review/all-unmatched-w08-source-review-20261107','parent_head':'1701ccf2049022866adfcebcc9bba9b6492407c6',
 'finding_id':'W08-FINAL-001','filed_before_fix':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1227#issuecomment-6719268318',
 'selector':ref(O/'selection.json'),'payload':ref(O/'payloads/Plain_Flour.yaml'),
 'predecessor_payload_sha256':'aa8390f17f1ed9f9c083fd6b487ee1c40228e754072b7e390b97dfb2fd6eae83',
 'original_owner_before_sha256':'becb2e4860868161607a709d6c4b5cbef56c2b4a3e06c9a4fc9214e35e4e9a8e',
 'owner_path':'data/ingredients/unmapped/Plain_Flour.yaml','counts':sel['counts'],
 'change':'Adopt the independently reviewed generic flour preferred label and record a new actual primary-label resolution of that label. Retain EXACT_MATCH for this current method, without claiming the old Plain flour lookup was exact, synonymous or CAS-based. Separate direct ontology DATABASE_MATCH facts from explicitly LLM-assisted material-scope interpretation. Preserve the RAW_TEXT source alias, identity, filename and five prior history events; append one truthful event.',
 'unchanged_other_payload_proof':ref(O/'lineage.json'),
 'scientific_review':ref(O/'independent-review/science/review.json'),'skeptical_review':ref(O/'independent-review/skeptical/review.json'),
 'final_scientific_bindings':ref(O/'independent-review/science/final-bindings.json'),'final_skeptical_bindings':ref(O/'independent-review/skeptical/final-bindings.json'),
 'final_native_assembly_review':ref(O/'independent-review/final-native-assembly.json'),
 'native_review_yaml':native['review_yaml'],'native_review_markdown':native['review_markdown'],'native_receipt':ref(O/'native/receipt.json'),
 'native_scope':'One complete changed owner, with its full case180 source assessment and113/188/320 accounting as bound context. Other112 owners gain no fresh whole-owner approval.',
 'native_finding_disposition':'Exact correction supported in isolated payload. Formal coordinator final-head acceptance and legacy finding closure remain deferred; no prior native review identity was invented and no issue was closed.',
 'technical_validation':ref(O/'validation/receipt.json'),'structural_accounting':ref(O/'structural-audit.json'),'preservation':ref(O/'preservation.json'),
 'checks':{'guarded_changed_payloads':1,'strict_payloads':113,'baseline_records':2956,'overlay_records':3037,'partonomy_violations':0,'identity_obligation_rows':120,'actual_RuleD_negative_rejections':111,'nonmapped_selected_records_emitting_no_identity_row':2,'actual_Claw_projected_before_after_payloads':2,'independent_science_final_checks':1906,'independent_skeptical_final_checks':864},
 'independence':{'author':'worker08:/root','scientific_reviewer':'worker08:/root/vitamins','skeptical_reviewer':'worker08:/root/inorganics','technical_executor':'worker08:/root/organics; prior OP author, no independent scientific approval','native_assembly_author':'worker08:/root','native_assembly_reviewer':'worker08:/root/vitamins'},
 'new_referral':{'id':'PF-LINEAGE-001','artifact':ref(O/'independent-review/skeptical/coordinator-referral.json'),'scope':'Unsupported supermarket quotation in old reviewer prose only; current/final source correctly says Plain flour. Original review untouched. Referred for coordinator deduplication/routing before any later correction; no extra payload fix.'},
 'preserved_reviews':'Complete W05 and W06 packets, prior W08 source artifacts and Soy/R2A confirmation seals and manifest members were rehashed unchanged. Root full1701 review remains separately owned and unmodified.',
 'holds':['Unknown grain/supplier/product/catalogue/treatment/composition and automatic CAS not inferred.','No owner merge, role or supported-export approval.','Every original source/occurrence/identity/form/role/export hold remains.','Trypticase/Bacto owner admission remains FAILED/HELD; no gate exception expansion.','The18 original unaffected planning payloads retain their original limits.'],
 'failure_preservation':'Reviewer harness schema/key assumptions and the pre-native validation author/final evidence-suffix mismatch are retained with corrected successors. No gate weakened and no author source defect concealed.',
 'publication_manifest':str((O/'MANIFEST.sha256').relative_to(ROOT)),
 'post_publication_receipt':'.temp/all-unmatched-worker-08/plain-flour-method-v1/publication-receipt.json',
 'maintained_corpus_edits':False,'shared_inputs_or_gate_changes':False,'GitHub_mutation':False,'paid_research':False,'external_sessions_added':False,'release_approval':False,
}
save(O/'HANDOFF.json',handoff)
md='''# W08 Plain Flour mapping-method successor

This immutable successor corrects only filed **W08-FINAL-001** relative to `1701ccf2049022866adfcebcc9bba9b6492407c6`. The complete selection remains188 cases,113 proposals and320 occurrence IDs. Exactly one payload and one source-case assessment changed;112 other payloads and187 decisions remain exact. All1075 original evidence entries remain an exact prefix of1082 entries.

The proposed existing owner now uses preferred label **flour**, the verified primary label of FOODON:00004510. A new native primary-label resolution supports current EXACT_MATCH. This does not recast the old raw **Plain flour** lookup as an exact label, ontology synonym or CAS method. Direct ontology facts and the explicitly agent-assisted generic material-scope decision are separated. Raw source synonym, identifier, filename, original beforeimage and all five prior history events remain; one truthful event is appended. No grain, supplier, treatment, product, CAS, role or merge specificity is introduced.

Worker08 root authored the correction. `/root/vitamins` independently reviewed the whole payload/source case; `/root/inorganics` independently challenged science and lineage and disclosed the prior method miss. Both then read the final113/188 indices:1906 and864 checks passed. `/root/organics`, the earlier OP author, performed technical validation only. A separate peer checked the final native assembly.

Native guarded replay, strict113-payload validation, full2956-baseline/3037-overlay partonomy,120 identity obligations and111 actual RuleD negative controls passed. Two non-MAPPED selected records emit no identity row. Actual before/after Claw projections preserve MIM:Plain_Flour → FOODON:00004510 with exactMatch; the current subject label is flour and Plain flour survives as an alias. No canonical SSSOM was written. Trypticase/Bacto admission remains FAILED/HELD.

`selection.json` is authoritative for the new complete proposal selection. `lineage.json` supplies exact changed/unchanged payload and case hashes. `HANDOFF.json` binds all final reviews, source proof, native YAML/Markdown, commands, controls and preservation receipts. The native record covers the one changed full owner with its complete source case as context; it does not grant fresh whole-owner approval to112 unchanged candidates. Formal external finding closure/final-head acceptance remains with the coordinator; the isolated correction itself is independently supported.

**Separate coordinator referral PF-LINEAGE-001:** an old skeptical appraisal inserted “supermarket” into the frozen source label. The actual record says “Plain flour”. The old review remains immutable; this discrepancy is recorded with its exact locator/hash and is not inherited as material evidence. No unrelated payload correction or GitHub mutation was made.

Every original source, scientific, role, owner and export hold remains, including the18 unaffected planning-payload limits. W05/W06 sealed reviews, prior W08 source work and Soy/R2A confirmation manifest members verified unchanged. The coordinator's full1701 review remains separate. No maintained data, shared inputs, gates, pins, workflow, releases or merges changed.

Publication is an ordinary commit/non-force push on the existing W08 branch. The exact new head and remote readback are recorded in the task-private `publication-receipt.json`. Coordinator independent final-head review is the next step.
'''
with (O/'HANDOFF.md').open('x') as f:f.write(md)
active=A/'ACTIVE-SUCCESSOR-plain-flour-v1.json'
save(active,{'created_at':now,'status':handoff['status'],'predecessor_head':handoff['parent_head'],'selector':ref(O/'selection.json'),'handoff':ref(O/'HANDOFF.json'),'native_review':native['review_yaml'],'scope':'New immutable W08 selection pointer; every older pointer/selection remains preserved. No coordinator integration pin is changed.'})
paths=[f for f in O.rglob('*') if f.is_file()]+[active,ROOT/native['review_yaml']['path'],ROOT/native['review_markdown']['path']]
assert len(paths)==len(set(paths));assert not any(f.is_symlink() for f in paths)
manifest=O/'MANIFEST.sha256'
with manifest.open('x') as f:
    for path in sorted(paths,key=lambda f:str(f.relative_to(ROOT))):f.write(sha(path)+'  '+str(path.relative_to(ROOT))+'\n')
for line in manifest.read_text().splitlines():
    digest,path=line.split('  ',1);assert sha(ROOT/path)==digest
save(P/'precommit-seal.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','new_paths_without_manifest':len(paths),'manifest':ref(manifest),'selector':ref(O/'selection.json'),'handoff':ref(O/'HANDOFF.json'),'active':ref(active),'native':native,'payload':ref(O/'payloads/Plain_Flour.yaml'),'new_referral':handoff['new_referral'],'original_tracked_diff':'empty at seal','publication_pending':True})
print(json.dumps(read(P/'precommit-seal.json'),indent=2))
