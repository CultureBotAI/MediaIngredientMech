# `data/ingredients/mapped/Thiamine_monophosphate.yaml`

## Verdict

Pass. The restored CultureMech residual grounding to `CHEBI:9533`, aggregate
row, occurrence count, and final SSSOM row for thiamine monophosphate are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiamine_monophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:9533` with the same
  `ontology_mapping.ontology_id`, label `thiamine(1+) monophosphate`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`,
  `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence in one medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine-hcl_X_2_H2o` through `Thiamine_monophosphate`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset
  from this batch: `Thiamine-hcl_X_2_H2o`, `Thiamine`, `Thiamine_Hcl`, and
  `Thiamine_monophosphate` all passed. The local `Thiamine_Vitamin_Solution`
  row was skipped because its exact `kgmicrobe.ingredient` ID and close `MICRO`
  parent are outside the CHEBI-focused term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:9533` with canonical label
  `thiamine(1+) monophosphate` and related synonym
  `thiamine monophosphate`, supporting the CultureMech residual exact synonym
  grounding.
- The structured `ontology_mapping.evidence` now carries the
  `culturemech:output/ingredient_occurrences.tsv` source used by the SSSOM
  builder; the September 6 curation history explains that this restored
  provenance that had previously existed only in the creation history.
- The final SSSOM has exactly one exact row for `MIM:Thiamine_monophosphate`,
  points at `CHEBI:9533`, keeps the reviewed
  `manual:claude_culturemech_residual_grounding|CREATED|2026-08-30`
  validation token, and leaves `other` empty.

## Completeness

- The CHEBI identity, restored occurrence-table evidence, occurrence count,
  aggregate copy, and final SSSOM row agree.
- No components, roles, synonyms, chemical properties, or environmental
  contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech residual grounding,
  evidence-restoration event, aggregate, and final SSSOM row.

## Recommended Edits

- None.
