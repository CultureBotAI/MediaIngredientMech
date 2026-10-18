# `data/ingredients/mapped/N-acetyl-beta-D-mannosamine.yaml`

## Verdict

Pass. The exact `CHEBI:63154` N-acetyl-beta-D-mannosamine identity,
MicrobeDecoder provenance, structural properties, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetyl-beta-D-mannosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:63154` with
  `ontology_mapping.ontology_id: CHEBI:63154`, label
  `N-acetyl-beta-D-mannosamine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: two MicrobeDecoder `BacDive_Metabolite_utilization` source
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-_3-oxohexanoyl-dl-homoserine_Lactone` through
  `N-acetyl-glutamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63154` as active
  `N-acetyl-beta-D-mannosamine`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetyl-beta-D-mannosamine` to `CHEBI:63154` with empty `other`.

## Completeness

- The active ChEBI target, beta-anomer label, structural properties,
  MicrobeDecoder provenance, source occurrence count, and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
