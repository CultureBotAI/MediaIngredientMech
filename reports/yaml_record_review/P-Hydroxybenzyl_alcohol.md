# `data/ingredients/mapped/P-Hydroxybenzyl_alcohol.yaml`

## Verdict

Pass. The CultureMech residual `p-Hydroxybenzyl alcohol` surface exact-matches
active `CHEBI:67410`, and the final SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record:
  `data/ingredients/mapped/P-Hydroxybenzyl_alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:67410` with
  `ontology_mapping.ontology_id: CHEBI:67410`, label
  `p-hydroxybenzyl alcohol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`,
  `mapping_status: MAPPED`, and no ingredient-type or structure assertion.
- Occurrences: two CultureMech occurrences across two media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps
  `MIM:P-Hydroxybenzyl_alcohol` exactly to `CHEBI:67410`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:67410` as active
  `p-hydroxybenzyl alcohol`.
- The grounding evidence correctly points to the CultureMech ingredient
  occurrence table; the creation history records that the residual importer
  found an exact canonical-label match for `p-hydroxybenzyl alcohol`.
- The final SSSOM row carries the CultureMech occurrence source, the restored
  evidence curator stamp, and the original residual-grounding review stamp.
- No roles, synonyms, supplied forms, components, or chemical structure fields
  are asserted.

## Completeness

- The active ChEBI term, YAML identifier, ontology mapping, occurrence counts,
  and final SSSOM object all agree.

## Recommended Edits

- None.
