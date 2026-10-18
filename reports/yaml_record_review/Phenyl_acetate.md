# `data/ingredients/mapped/Phenyl_acetate.yaml`

## Verdict

Pass. The CultureMech residual grounding maps exactly to active `CHEBI:8082`
phenyl acetate, and the final SSSOM row has no unsafe `other` values.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenyl_acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:8082` with
  `ontology_mapping.ontology_id: CHEBI:8082`, label `phenyl acetate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `match_level: EXACT`,
  `mapping_status: MAPPED`, and no `ingredient_type`.
- Occurrences: 1 CultureMech occurrence in 1 recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8082` resolves `CHEBI:8082`
  `phenyl acetate`.
- The final SSSOM row was inspected directly and maps `MIM:Phenyl_acetate`
  exactly to `CHEBI:8082`.

## Evidence

- The record was created from the CultureMech residual table on an exact label
  match to phenyl acetate, the neutral ester.
- The structured `ontology_mapping.evidence` correctly preserves
  `culturemech:output/ingredient_occurrences.tsv` as the source table consumed
  by the SSSOM builder.
- The final SSSOM row exports no `other` tokens.

## Completeness

- No consequential gap was found for this exact CHEBI mapping; the empty
  synonym and chemical-property slots are not required for this imported
  residual record.

## Recommended Edits

- None.
