"""Seal the independently reviewed report successor without a commit/hash cycle."""
from pathlib import Path
import hashlib,json,datetime,subprocess,sys,collections
R=next(p for p in Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file())
P=R/'reports/all_unmatched_20261107/worker-03';O=P/'successors/issue1226-v1'
sha=lambda b:hashlib.sha256(b).hexdigest()
def cap(p):return {'root':'artifact','path':str(p.relative_to(P)),'sha256':sha(p.read_bytes())}
def put(p,obj):
 with p.open('x') as f:json.dump(obj,f,indent=2,ensure_ascii=False);f.write('\n')

review,technical,assembly=[Path(x).resolve(strict=True) for x in sys.argv[1:4]]
assert all(p.is_relative_to(O) for p in [review,technical,assembly])
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='f6bfbf3c185f705484aa106405f813209146c766'
assert not subprocess.check_output(['git','diff','--name-only'],text=True).strip()
assert not subprocess.check_output(['git','diff','--cached','--name-only'],text=True).strip()
d=json.loads((O/'decisions.json').read_text());p=json.loads((O/'proposals.json').read_text());e=json.loads((O/'evidence.json').read_text())
assert len(d['decisions'])==188 and len(p['proposals'])==74 and len(e['evidence'])==868
with (O/'tools'/Path(__file__).name).open('xb') as f:f.write(Path(__file__).read_bytes())
issue_refs=sorted({u for row in d['decisions'] for u in row['issue_refs']})
h={
 'schema_version':1,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'COMPLETE_REPORT_ONLY_PROVENANCE_SUCCESSOR_INDEPENDENTLY_REVIEWED_FOR_AUTHORIZED_PUBLICATION',
 'worker_slot':3,'branch':'review/all-unmatched-w03-source-review-20261107',
 'predecessor_published_head':'f6bfbf3c185f705484aa106405f813209146c766',
 'original_source_head':'1196d5bc3aaba7563b829d5cbe7e54722fccc35d',
 'frozen_base':'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99',
 'source_root':str(R.parents[2]/'queue/preliminary-v5'),'artifact_root':str(P.relative_to(R)),
 'shard_sha256':d['shard_sha256'],
 'authority':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1226','https://github.com/CultureBotAI/MediaIngredientMech/issues/1246'],
 'active_complete_selection':{n:cap(O/n) for n in ['decisions.json','proposals.json','evidence.json']},
 'selection_rule':'Select these three complete files together instead of predecessor selectors. Do not union old/new proposal sets or consume the retired mixed RCM origin.',
 'counts':{'cases':188,'proposals':74,'evidence':868,'predecessor_evidence_preserved':863,'added_evidence':5,'changed_payloads':49,'unchanged_payloads':25,'evidence_enum_corrections':49,'history_appends':49,**dict(collections.Counter(x['kind'] for x in p['proposals']))},
 'machine_ledger':cap(O/'machine-ledger.json'),'proposal_inventory':cap(O/'proposal-inventory.tsv'),
 'payload_bridge':cap(O/'payload-bridge.json'),'scientific_field_retention':cap(O/'scientific-field-retention.json'),
 'allowlist':cap(O/'context/allowlist/repair-allowlist.json'),
 'accepted_predecessor':cap(O/'context/accepted-predecessor.json'),
 'final_provenance_review':cap(review),'final_technical_review':cap(technical),'independent_skeptical_assembly_review':cap(assembly),
 'final_native_provenance_review':cap(review.parent/'review.yaml'),'final_native_provenance_review_rendered':cap(review.parent/'review.md'),
 'payload_native_review':cap(O/'reviews/provenance/payload-phase-v2/review.yaml'),
 'payload_native_review_rendered':cap(O/'reviews/provenance/payload-phase-v2/review.md'),
 'reviewer_scopes':[
  {'reviewer':'/root/provenance_review','independent_of_author':True,'scope':'All 49 exact complete evidence objects, parent mappings, authentic beforeimages, authorship, appended history and full-field retention; all 74 payloads/exclusions and final 188/74/868 core. Provenance only; scientific_review=false.'},
  {'reviewer':'/root/provenance_controls','independent_of_author':True,'scope':'Private helper repair/code inspection; all original 36 control ASTs retained plus explicit no-write mismatch control; actual 49/74 native payload checks and partonomy negative control; complete core/accounting and maintained preservation.'},
  {'reviewer':'/root/provenance_assembly','independent_of_author':True,'scope':'Separate skeptical complete selection, payload, source-case/capture/hash, issue lineage, prior report, origin and hold preservation review; detached final-seal check follows sealing.'}],
 'checks':{'structural_accounting':cap(O/'validation/structural-audit.json'),'complete_preservation':cap(O/'validation/complete-preservation.json'),'native_payload_schema_partonomy':cap(O/'validation/native-payloads.json'),'archived_native_payload_review':cap(O/'validation/archived-native-payload-review.json')},
 'helper_repair':{'finding':'W03-PROV-GUARD-001','issue':1246,'original_helper':cap(O/'tools/provenance_writer.py'),'repaired_helper':cap(O/'tools/provenance_writer_v2.py'),'disposition':cap(O/'context/helper-repair-disposition.json'),'original_failed_controls_preserved':[23,36],'repaired_controls_passed':37,'original_36_test_methods_ast_unchanged':True,'mismatch_native_writer_not_called':True,'mismatch_no_output':True,'scope':'Private report producer only. Native campaign operator unchanged. No hostile-concurrency guarantee.'},
 'exclusions':{'inherited_manual_objects':[{'proposal_id':'b-proposal-marine-aliases','index':0},{'proposal_id':'c-copper-trihydrate-alias','index':4},{'proposal_id':'m-arabinan_source_alias','index':2}],'oxoid':{'proposal_id':'w03-oxoid-cm0149-product-1224-v1','payload_sha256':'1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae','already_llm_entries':2,'kind':'new_owner','before_sha256':None,'unchanged':True},'retired_mixed_rcm':{'proposal_id':'b-proposal-cm0149-form','active':False,'consumed':False,'retirement':cap(P/'successors/issue1224-v1/retirement.json')}},
 'retention_scope':'188 source decision objects and complete file byte-identical; all 863 earlier evidence objects exact; all 25 excluded payloads and proposal objects exact. For 49 changed payloads all scientific fields, complete evidence source/notes, parent mappings and prior history objects equal; native serializer may reflow scalar text. Prior reviews stay historical, never repinned to new payload bytes.',
 'remaining_holds':{'scientific_decisions':'Every source-specific decision, unresolved requirement and scientific limitation remains unchanged in decisions.json and selected payloads.','source_issue_refs_preserved':issue_refs,'oxoid_unknowns':['Historical CM0149 formula revision','Historical package and lot'],'new_owner_admission':'Existing native admission prerequisites remain; no whole-owner approval is supplied.','roles_and_supported_exports':'All native owner, role, supported/withheld and export holds retained; no release approval.','coordinator_owned_out_of_scope':'Issue1245 Mg/Cr integration dependency; all cross-shard owner reconciliation and candidate application remain root-owned.'},
 'authority_limits':{'maintained_application':False,'whole_owner_approval':False,'scientific_reapproval':False,'role_approval':False,'supported_export_approval':False,'merge':False,'github_mutation':False},
 'validation_limits':'No unchanged full-repository QC, sync, downstream rebuild, provider research, maintained review publication or native operator/gate change. Structural/schema PASS is not scientific evidence. Exact final seal and published commit/remote are checked in detached receipts.',
 'manifest_path':str((O/'MANIFEST.json').relative_to(P)),'transport_path':str((O/'SHA256SUMS').relative_to(P)),
 'publication_receipt':'.temp/w03-provenance-successor-v1/PUBLICATION-RECEIPT.json; records actual commit, parent and non-force remote readback after publication without a self-referential commit hash.'
}
put(O/'HANDOFF.json',h)
files=[]
for f in sorted(O.rglob('*')):
 assert not f.is_symlink(),'No symlink permitted in sealed report'
 if f.is_file():files.append({'path':str(f.relative_to(O)),'sha256':sha(f.read_bytes()),'bytes':f.stat().st_size})
put(O/'MANIFEST.json',{'schema_version':1,'scope':'Exact complete issue1226-v1 report tree; excludes this manifest and SHA256SUMS to avoid self-reference. All earlier reports retained under predecessor commit.','files':files,'file_count':len(files)})
with (O/'SHA256SUMS').open('x') as out:
 for f in sorted(x for x in O.rglob('*') if x.is_file() and x != O/'SHA256SUMS'):
  out.write(sha(f.read_bytes())+'  '+str(f.relative_to(R))+'\n')
print(json.dumps({'HANDOFF':sha((O/'HANDOFF.json').read_bytes()),'MANIFEST':sha((O/'MANIFEST.json').read_bytes()),'manifest_members':len(files),'SHA256SUMS':sha((O/'SHA256SUMS').read_bytes())},indent=2))
