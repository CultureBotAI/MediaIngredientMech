# `data/ingredients/mapped/Xanthan.yaml`

## Verdict

Pass. The MicrobeDecoder exact `CHEBI:189560` xanthan identity, aggregate row,
and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Xanthan.yaml`.
- Identifier and grounding: `identifier: CHEBI:189560` with matching
  `ontology_mapping.ontology_id`, label `xanthan`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Synonyms: none.
- Occurrences: one MicrobeDecoder metabolite-utilization occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wolfes_Vitamin_Mix` through `Xanthine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the two
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:189560` returns active label `xanthan` and
  defines it as a polysaccharide produced by `Xanthomonas campestris`.
- The final SSSOM row correctly has
  `MIM:Xanthan skos:exactMatch CHEBI:189560` with no `other` labels.

## Issues

None.

## Completeness

- The exact CHEBI mapping, aggregate copy, MicrobeDecoder occurrence, and final
  SSSOM row agree.

## Recommended Edits

None.
