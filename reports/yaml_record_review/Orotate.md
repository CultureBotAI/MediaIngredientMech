# `data/ingredients/mapped/Orotate.yaml`

## Verdict

Pass. The CultureMech residual `Orotate` surface exactly matches active
`CHEBI:30839` orotate, and the final SSSOM row publishes only that exact
identity with no unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Orotate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30839` with
  `ontology_mapping.ontology_id: CHEBI:30839`, label `orotate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and no
  ingredient-type or structure assertion.
- Occurrences: three CultureMech occurrences across three media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- The final SSSOM row was inspected directly and maps `MIM:Orotate` exactly to
  `CHEBI:30839`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:30839` as active `orotate`, matching
  the record's exact ontology mapping.
- The grounding evidence correctly points to the CultureMech ingredient
  occurrence table; the creation history records that the residual importer
  found an exact canonical-label match for `orotate`.
- The final SSSOM row carries the CultureMech occurrence source, the restored
  evidence curator stamp, and the original residual-grounding review stamp.
- No roles, synonyms, supplied forms, components, or chemical structure fields
  are asserted, so there is no unsupported secondary payload.

## Completeness

- The active ChEBI term, YAML identifier, ontology mapping, occurrence counts,
  and final SSSOM object all agree.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`,
  `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and the unified
  snapshot found only the expected `Orotate` mentions for this mapped record.

## Recommended Edits

- None.
