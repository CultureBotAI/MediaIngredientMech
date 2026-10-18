# `data/ingredients/mapped/Oxamicetin.yaml`

## Verdict

Pass. The MicrobeDecoder `Oxamicetin` label exact-matches active
`CHEBI:220394`, the stored structure agrees with that term, and the final
SSSOM row exports no unsupported synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxamicetin.yaml`.
- Identifier and grounding: `identifier: CHEBI:220394` with
  `ontology_mapping.ontology_id: CHEBI:220394`, label `Oxamicetin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder `BacDive_Metabolite_production`
  source-column occurrence and zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxamicetin`
  exactly to `CHEBI:220394`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:220394` as active `Oxamicetin` and
  reports the same formula, InChI, SMILES, and mass stored in the YAML.
- The MicrobeDecoder import and review history place the row on the active
  ChEBI term whose canonical label exact-matches the record label.
- The final SSSOM row carries the MicrobeDecoder source and the manual
  `review-ingredients` approval stamp.
- No synonyms, roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, formula, structure, source occurrence count, and final
  SSSOM row agree.

## Recommended Edits

- None.
