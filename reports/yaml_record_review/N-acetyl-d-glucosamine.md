# `data/ingredients/mapped/N-acetyl-d-glucosamine.yaml`

## Verdict

Pass. The #460 `CHEBI:506227` N-acetyl-D-glucosamine repair, source-backed
carbon-source role, occurrence count, accepted synonyms, and final exact row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetyl-d-glucosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:506227` with
  `ontology_mapping.ontology_id: CHEBI:506227`, label
  `N-acetyl-D-glucosamine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 29 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-_3-oxohexanoyl-dl-homoserine_Lactone` through
  `N-acetyl-glutamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:506227` as active
  `N-acetyl-D-glucosamine` with the expected same-substance aliases.
- The #460 repair correctly moved the record off the peptidoglycan-residue
  target and onto the free monosaccharide.
- CultureMech supplied original role text `Carbon Source`, which directly
  supports the migrated `CARBON_SOURCE` role.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetyl-d-glucosamine` to `CHEBI:506227` with same-substance synonyms,
  the accepted Sigma catalog variant, and `CAS:7512-17-6` in `other`.

## Completeness

- The active ChEBI target, structure, 29/29 occurrence count, source-backed
  role, accepted synonyms, and final row agree.
- The raw `Role: Carbon source; Properties: ...` import strings remain only in
  YAML and are correctly filtered from final SSSOM `other`.

## Recommended Edits

- None.
