# `data/ingredients/mapped/Micronutrients.yaml`

## Verdict

Pass. The residual CultureMech `Micronutrients` surface is grounded to the
active `CHEBI:27027` micronutrient class, restored SSSOM evidence is present,
and the final row publishes cleanly.

## Identity

- Reviewed record: `data/ingredients/mapped/Micronutrients.yaml`.
- Identifier and grounding: `identifier: CHEBI:27027` with
  `ontology_mapping.ontology_id: CHEBI:27027`, label `micronutrient`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgso4_X_7_H2o` through `Middlebrook_7H10_Agar`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the two other CHEBI-primary records in the same batch.

## Evidence

- EBI OLS4 resolves `CHEBI:27027` as active `micronutrient` with
  `micronutrients` as a synonym.
- `mappings/culturemech_residual_groundings.tsv` maps the missing CultureMech
  ingredient `Micronutrients` to `CHEBI:27027`, and the record's restored
  `ontology_mapping.evidence` now carries
  `culturemech:output/ingredient_occurrences.tsv` so the final SSSOM row
  publishes that provenance.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Micronutrients` to `CHEBI:27027` with empty `other`.

## Completeness

- The record does not publish unsupported roles, raw synonyms, or stale CAS
  values.

## Recommended Edits

- None.
