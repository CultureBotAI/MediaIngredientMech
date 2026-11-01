"""Independent all-row check of the final native held snapshot; read-only inputs."""
from datetime import datetime,timezone
from pathlib import Path
import contextlib,csv,hashlib,importlib.util,io,json,subprocess
root=Path.cwd(); run=root.parent; notes=run/'step1-independent'; claw=run/'claw-source'
spec=importlib.util.spec_from_file_location('independent_final_builder',claw/'scripts/build_unified_ingredient_mapping.py');builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
raw=(root/'UNIFIED_INGREDIENT_MAPPING.tsv').read_bytes(); final=list(csv.DictReader(raw.decode().splitlines(),delimiter='\t'))
old_path=run/'step1-evidence/unified-candidate.tsv'; old=list(csv.DictReader(old_path.read_text().splitlines(),delimiter='\t'))
old_by_name={r['ingredient_name']:r for r in old}; final_by_name={r['ingredient_name']:r for r in final}; assert len(final_by_name)==len(final)==len(old)==4170
assert old_by_name.keys()==final_by_name.keys()
expected=json.loads((notes/'proposed-source-holds.json').read_text())['rows']; expected_labels={r['ingredient_name'] for r in expected}
changed={name for name in old_by_name if old_by_name[name]!=final_by_name[name]}; assert changed==expected_labels
for name in old_by_name:
 for field in ('ingredient_name','occurrence_count','example_media'):
  assert old_by_name[name][field]==final_by_name[name][field],(name,field)
with contextlib.redirect_stdout(io.StringIO()) as log:
 indexes=builder.load_mim_index(root); labels=builder.load_mim_label_index(root); live=builder.live_records(*indexes)
 rejections=builder.load_mapping_rejections(root,indexes[0],label_index=labels,live=live)
 anchors={row['ingredient_name']:builder._anchor_record(row['ingredient_name'],indexes[0],labels,live) for row in expected}
 assert all(anchor is None for anchor in anchors.values())
 occurrences=json.loads((notes/'claw-source-hold-occurrences.json').read_text())
 generated=builder.build_unified_rows(occurrences,*indexes,rejections,labels)
 assert [{k:str(v) for k,v in row.items()} for row in generated]==final
spec2=importlib.util.spec_from_file_location('independent_freshness',root/'scripts/check_unified_freshness.py'); freshness=importlib.util.module_from_spec(spec2);spec2.loader.exec_module(freshness)
provenance=json.loads((root/'UNIFIED_INGREDIENT_MAPPING.provenance.json').read_text());digest,count=freshness.inputs_digest(root/'data/ingredients');assert digest==provenance['mim_inputs_digest'] and count==provenance['mim_record_count']
assert hashlib.sha256(raw).hexdigest()==provenance['artifact_sha256']
assert provenance['mim_rev']==freshness._git_rev(root)
sssom=root/'mappings/ingredient_mappings.sssom.tsv'; assert sssom.read_bytes()==subprocess.check_output(['git','show','2add44fb:mappings/ingredient_mappings.sssom.tsv'],cwd=root)
receipt_path=run/'step1-source-holds-evidence/unified-generation-receipt.json'; receipt=json.loads(receipt_path.read_text())
assert receipt['after_sha256']==hashlib.sha256(raw).hexdigest()
for path,digest in receipt['input_sha256'].items():
 assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest,path
result={'checked_at':datetime.now(timezone.utc).isoformat(),'mim_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'claw_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=claw,text=True).strip(),'final_tsv_sha256':hashlib.sha256(raw).hexdigest(),'row_count':len(final),'occurrence_count':sum(int(row['occurrence_count']) for row in final),'exact_held_rows_changed':len(changed),'unrelated_rows_unchanged':len(final)-len(changed),'all_rows_preserved_label_count_examples':len(final),'held_anchors_none':len(anchors),'native_builder_output_matches_rows':len(generated),'occurrence_scan_cache_sha256':hashlib.sha256((notes/'claw-source-hold-occurrences.json').read_bytes()).hexdigest(),'generation_receipt_sha256':hashlib.sha256(receipt_path.read_bytes()).hexdigest(),'generation_receipt_input_hashes_verified':len(receipt['input_sha256']),'mim_input_digest_matches_provenance':True,'mim_revision_uses_documented_merge_base':provenance['mim_rev'],'canonical_sssom_same_as_baseline':True,'canonical_sssom_sha256':hashlib.sha256(sssom.read_bytes()).hexdigest(),'canonical_sssom_rows':len(list(csv.DictReader((line for line in sssom.read_text().splitlines() if not line.startswith('#')),delimiter='\t')))}
(notes/'final-snapshot-probe.json').write_text(json.dumps(result,indent=2)+'\n'); (notes/'final-snapshot-probe.log').write_text(log.getvalue()); print(json.dumps(result,indent=2))
