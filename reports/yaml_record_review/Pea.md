# `data/ingredients/mapped/Pea.yaml`

## Verdict

Needs curation; major. The `NCIT:C72056` Pea identity passes, but final SSSOM
`other` exports a recipe-order note as though it were a pea synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Pea.yaml`.
- Identifier and grounding: `identifier: NCIT:C72056` with
  `ontology_mapping.ontology_id: NCIT:C72056`, label `Pea`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech occurrences across 2 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this NCIT primary record.
- A fresh OLS4 exact search for `Pea` resolves `NCIT:C72056` `Pea`.
- The final SSSOM row was inspected directly and maps `MIM:Pea` exactly to
  `NCIT:C72056`.

## Evidence

- The exact NCIT label supports the primary Pea grounding, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the NCIT
  row as a missing-prefix validator coverage issue rather than a bad term.
- Major: `Pea(add after dH2O)` is not a real synonym for pea. The parenthetical
  is recipe-order text and should not appear in final SSSOM `other`.

## Completeness

- The exact NCIT row is sufficient for the Pea subject.
- The synonym surface is not complete enough while a conditional recipe note is
  exported as a synonym.

## Recommended Edits

- Major: in `data/ingredients/mapped/Pea.yaml`, retype or suppress the
  `Pea(add after dH2O)` raw synonym so it remains provenance only and no longer
  appears in `mappings/ingredient_mappings.sssom.tsv`. Rebuild the final SSSOM
  and rerun `scripts/validate_sssom_invariants.py`.
