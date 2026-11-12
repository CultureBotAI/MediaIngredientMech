"""Bounded diagnostic synthesis: no identity approval or source correction."""
from pathlib import Path
import collections, hashlib, json
D=Path(__file__).resolve().parent
W=D.parent/'worktree'
R=W/'reports/kgm_unmapped_chemicals_20261107'
ledger_path=R/'reconciliation-before/ledger.json'
rows=json.loads(ledger_path.read_bytes())
# These are exact source IDs reviewed against their captured raw label/record.
recipe_ids={1143,1379,1387,1402,1507,1530,1732,1784,1812,1863,1941,1999,2026,2052,2431,485,559,748,88,925,992}
biological_ids={1603,1606,1881,1986,2441,2443,575,654,662,725}
priority=[('BLANK_SOURCE_LABEL','EMPTY_SOURCE_LABEL'),('DOWNSTREAM_MATERIAL_HOLD','DOWNSTREAM_MATERIAL_HOLD'),('AMBIGUOUS_MULTIPLE_OWNERS','MULTIPLE_LEXICAL_OWNERS'),('NON_RESOLVING_OR_REJECTED_LABEL_ONLY','REJECTED_OR_NONRESOLVING_HISTORY'),('MATCHED_AMBIGUOUS_OWNER','AMBIGUOUS_CURRENT_RECORD'),('NO_EXACT_CASEFOLD_NAME_MATCH','NO_EXACT_NAME_MATCH'),('MATCHED_UNMAPPED_OWNER','CURRENT_UNMAPPED_RECORD'),('MATCHED_OWNER_HAS_WITHHELD_MAPPINGS','CURRENT_WITHHELD_MAPPING'),('CONSUMED_SUPPORTED_LEXICAL_COVERAGE','CONSUMED_SUPPORTED_NAME_ONLY')]
result=[];nonhits=[]
for row in rows:
 category=next((name for flag,name in priority if flag in row['triage_flags']),'CURRENT_OWNER_NOT_CONSUMED')
 entry={key:row[key] for key in ['candidate_id','source','source_id','category','source_label','raw_source_label','triage_flags']}
 entry.update({'diagnostic_partition':category,'raw_label_differs_from_transformed':bool(row['raw_source_label']) and row['raw_source_label']!=row['source_label'],'scientific_identity_approved':False})
 if 'NO_EXACT_CASEFOLD_NAME_MATCH' in row['triage_flags']:
  number=int(row['source_id'].split(':')[1]) if row['source']=='mediadive' else None
  if number==1944:
   code='EMPTY_LABEL_WITH_MISPLACED_SOURCE_TEXT'; reason='Captured compound field is empty; the attribute contains w/v) Yeast extract (BD-Difco, 10%. Inspect source extraction and formulation; do not turn this into neat yeast-extract identity.'
  elif row['source']=='microbedecoder':
   code='EXISTING_SOURCE_SCOPED_JOINT_CONDITION'; reason='Exact H2+CO2 token carries 98 preserved joint-condition observations and identity-unresolved disposition. Spacing variants are discovery clues only; retain source-scoped hold.'
  elif number==1627:
   code='EXPLICIT_ALTERNATIVE_MATERIALS'; reason='Raw source says Cellobiose or Cellulose MN 300. Resolve the recipe alternatives; do not select one identity or merge them.'
  elif number in recipe_ids:
   code='RECIPE_STOCK_OR_COMMERCIAL_MEDIUM'; reason='Source names a formulation, stock, commercial broth/salt mix, or numbered medium. Follow the cited recipe/catalogue and preserve its material identity; no molecular exact match from this token alone.'
  elif number in biological_ids:
   code='BIOLOGICAL_MATERIAL_OR_PREPARATION'; reason='Source names a biological material/preparation or product. Establish material scope, processing and product context before selecting a record or alias.'
  elif number==1238:
   code='ABBREVIATION_REQUIRES_SOURCE_IDENTITY'; reason='B12 alone is an abbreviation; establish the source chemical form instead of assuming a particular cobalamin identity.'
  elif number==1315:
   code='SOURCE_ALIAS_REVIEWED_SEPARATELY_IN_1149'; reason='Na acetate x 3 H2O is the source spelling addressed by the separate content-bound sodium acetate trihydrate review. This diagnostic does not itself confer approval.'
  else:
   code='FORM_OR_FORMULA_REQUIRES_SOURCE_VERIFICATION'; reason='Preserve every literal formula, salt, stereochemical and hydration token. Check primary source and supplied form; unusual formulas are not automatically classified as typos or mapped to a familiar parent.'
  entry['nonhit_review']={'code':code,'reason':reason,'raw_source_record':row['source_record']}
  nonhits.append(entry)
 result.append(entry)
assert len(result)==len(rows)==len({r['candidate_id'] for r in rows})==549
assert len(nonhits)==61
out=R/'reconciliation-synthesis';out.mkdir(exist_ok=False)
summary={'schema_version':1,'scientific_review':False,'ledger_sha256':hashlib.sha256(ledger_path.read_bytes()).hexdigest(),'input_candidates':len(rows),'diagnostic_partition_counts':dict(sorted(collections.Counter(r['diagnostic_partition'] for r in result).items())),'partition_precedence':priority,'overlapping_native_flags_preserved':True,'nonhit_count':len(nonhits),'nonhit_review_counts':dict(sorted(collections.Counter(r['nonhit_review']['code'] for r in nonhits).items())),'raw_transformed_differences':sum(r['raw_label_differs_from_transformed'] for r in result),'normalization_is_not_identity_approval':True,'source_specific_scientific_decisions_delegated_to_review':True}
for name,payload in [('all-source-diagnostic-partition.json',result),('nonhit-review.json',nonhits),('summary.json',summary)]:
 (out/name).write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
(out/'derivation.py').write_bytes(Path(__file__).read_bytes())
(out/'README.md').write_text('''# Source-bound reconciliation synthesis

All 549 source candidates remain individually addressable. The diagnostic partition is disjoint by the explicit precedence in summary.json; the original native flags overlap and must not be summed. No partition or lexical match approves chemical identity.

Every one of the 61 exact-name nonhits was inspected against its captured source spelling and record. The review separates empty source text, explicit alternatives, joint assay conditions, formulation/stock/product names, biological preparations, abbreviated identity, and chemical forms/formulas needing primary verification. The unusual formula cases are deliberately not called extraction errors or repaired to familiar chemistry without primary evidence.

There are 44 raw/transformed label differences in the input. Parentheses or punctuation removed by a producer are observable source changes, not evidence that the new text is an equivalent chemical name. All raw values remain available in the candidate ledger.

The two opaque sugar source IDs stay distinct and carry exact observation holds even though the generic Sugar record has supported lexical coverage. The other MicrobeDecoder material identities remain unresolved under their native policy. Sodium acetate source alias 1315 is a separate scientific review under issue #1149; its final outcome must be read from that review and the after ledger, not inferred here.

This is a bounded diagnostic synthesis, not a scientific review of all 549 identities. Existing WITHHOLD decisions, downstream material holds, and human scientific questions remain in force.
''')
print(json.dumps(summary,indent=2))
