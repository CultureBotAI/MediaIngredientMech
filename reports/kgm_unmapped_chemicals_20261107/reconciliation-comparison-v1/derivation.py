"""Compare immutable before/after reconciliations without modifying either."""
from pathlib import Path
import collections, hashlib, json
D=Path(__file__).resolve().parent
R=D.parent/'worktree/reports/kgm_unmapped_chemicals_20261107'
A=R/'reconciliation-before';B=R/'reconciliation-after-v1'
a={r['candidate_id']:r for r in json.loads((A/'ledger.json').read_bytes())}
b={r['candidate_id']:r for r in json.loads((B/'ledger.json').read_bytes())}
assert set(a)==set(b)
changed=[]
for key in a:
 fields={name:{'before':a[key][name],'after':b[key][name]} for name in sorted(a[key]) if a[key][name]!=b[key][name]}
 if fields:changed.append({'candidate_id':key,'source':a[key]['source'],'source_id':a[key]['source_id'],'source_label':a[key]['source_label'],'changes':fields})
assert {r['source_id'] for r in changed}=={'mediadive.ingredient:1315','kgmicrobe.compound:3_methylacetate'}
assert all(a[key]['downstream_holds']==b[key]['downstream_holds'] for key in a)
assert all(a[key]['consumed_name_hits']==b[key]['consumed_name_hits'] for key in a)
three=next(r for r in changed if r['source_id']=='kgmicrobe.compound:3_methylacetate')
assert set(three['changes'])=={'owners'}
old,new=three['changes']['owners']['before'],three['changes']['owners']['after']
assert len(old)==len(new)==1
assert old[0]['mapping_status']==new[0]['mapping_status']=='REJECTED'
assert {k:v for k,v in old[0].items() if k!='sha256'}=={k:v for k,v in new[0].items() if k!='sha256'}
sodium=next(r for r in changed if r['source_id']=='mediadive.ingredient:1315')
assert sodium['changes']['resolving_owner_paths']['before']==[]
assert sodium['changes']['resolving_owner_paths']['after']==['data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml']
sa=json.loads((A/'summary.json').read_bytes());sb=json.loads((B/'summary.json').read_bytes())
assert sa['native_current_dispositions']==sb['native_current_dispositions']=={'SUPPORTED':1739,'WITHHOLD':1275}
assert sa['consumed_partition_counts']==sb['consumed_partition_counts']=={'source':3014,'supported':1739,'withhold':1275}
summary={'schema_version':1,'scientific_approval_added_by_comparison':False,'candidate_count':len(a),'candidate_id_sets_equal':True,'unchanged_candidates':len(a)-len(changed),'changed_candidates':len(changed),'changed_source_ids':[r['source_id'] for r in changed],'all_downstream_holds_byte_equal_as_json':True,'all_consumed_name_hits_byte_equal_as_json':True,'native_dispositions_unchanged':sb['native_current_dispositions'],'consumed_partition_unchanged':sb['consumed_partition_counts'],'current_source_matches_consumed_before':sa['current_source_equals_consumed_source'],'current_source_matches_consumed_after':sb['current_source_equals_consumed_source'],'flag_deltas':{k:sb['flag_counts'].get(k,0)-sa['flag_counts'].get(k,0) for k in sorted(set(sa['flag_counts'])|set(sb['flag_counts'])) if sb['flag_counts'].get(k,0)!=sa['flag_counts'].get(k,0)},'inputs':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for folder in [A,B] for p in folder.iterdir()}}
out=R/'reconciliation-comparison-v1';out.mkdir(exist_ok=False)
(out/'changed-candidates.json').write_text(json.dumps(changed,indent=2,ensure_ascii=False)+'\n')
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'derivation.py').write_bytes(Path(__file__).read_bytes())
(out/'README.md').write_text('''# Before/after reconciliation

The 549 exact candidate IDs/categories are unchanged; 547 candidate entries are identical. MediaDive 1315 (Na acetate x 3 H2O) now has a lexical synonym hit on Sodium_Acetate_Trihydrate. Its new spelling is absent from the exact KG-consumed supported generation, so the report says MIM_NAME_NOT_IN_CONSUMED_SUPPORTED_EXPORT rather than claiming downstream adoption. This alias has its own scientific review; the lexical report adds none.

The 3-methylacetate candidate changes only its current owner-record hash. Mapping status remains REJECTED, no resolving hit appears, and its exact source-owned material hold is unchanged. The note correction is not identity approval.

Every consumed name-hit entry and every downstream-hold entry is unchanged. Native current dispositions remain 1,739 SUPPORTED / 1,275 WITHHOLD, as does the captured consumed partition. Current canonical source bytes now differ from the consumed generation; downstream must deliberately adopt a coherent, reviewed new generation later. No KG input was replaced by this reconciliation.
''')
print(json.dumps(summary,indent=2))
