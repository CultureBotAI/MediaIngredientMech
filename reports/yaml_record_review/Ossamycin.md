# `data/ingredients/mapped/Ossamycin.yaml`

## Verdict

Pass. The MicrobeDecoder `Ossamycin` label exact-matches active
`CHEBI:77735` ossamycin, the populated structure matches that term, and the
final SSSOM row exports no unsupported synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Ossamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:77735` with
  `ontology_mapping.ontology_id: CHEBI:77735`, label `ossamycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder `BacDive_Metabolite_production`
  source-column occurrence and zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- The final SSSOM row was inspected directly and maps `MIM:Ossamycin`
  exactly to `CHEBI:77735`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:77735` as active `ossamycin`, matching
  the record's exact MicrobeDecoder import.
- The YAML formula `C49H85NO14`, InChI, SMILES, and molecular weight describe
  the same CHEBI compound.
- The MicrobeDecoder review history promoted the exact label match before
  publication, and the final SSSOM row carries that review stamp.
- No synonyms, roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, formula, structure, source occurrence, and final SSSOM
  row agree.
- The empty CultureMech occurrence count is expected for this
  MicrobeDecoder-only metabolite-production import.

## Recommended Edits

- None.
