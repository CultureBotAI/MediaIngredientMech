# `data/ingredients/mapped/Pectin.yaml`

## Verdict

Pass. The CultureMech import maps exactly to active `CHEBI:17309` pectin, and
the final SSSOM `other` values are real pectin synonyms or the structured CAS.

## Identity

- Reviewed record: `data/ingredients/mapped/Pectin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17309` with
  `ontology_mapping.ontology_id: CHEBI:17309`, label `pectin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 13 CultureMech occurrences across 13 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:17309` resolves `CHEBI:17309` `pectin`
  and returns the kg-microbe synonym set carried by this record.
- The final SSSOM row was inspected directly and maps `MIM:Pectin` exactly to
  `CHEBI:17309`.

## Evidence

- The CHEBI primary identifier and mapping target denote pectin.
- The `CARBON_SOURCE` role is backed by imported CultureMech database evidence
  whose original role text was `Carbon Source`.
- The kg-microbe synonyms all appear on the OLS4 `CHEBI:17309` response.
- The final SSSOM exports only the exact pectin synonyms and `CAS:9000-69-5`.
  The raw `Role:`/`Properties:` strings remain provenance-only and are not
  leaked into `other`.

## Completeness

- The exact CHEBI mapping, structured CAS value, CultureMech role, and final
  synonym surface are complete enough for this record.

## Recommended Edits

- None.
