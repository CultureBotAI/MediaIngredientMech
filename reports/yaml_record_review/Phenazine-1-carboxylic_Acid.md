# `data/ingredients/mapped/Phenazine-1-carboxylic_Acid.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:62412`
phenazine-1-carboxylic acid, and the final SSSOM synonyms are scoped to this
same compound.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenazine-1-carboxylic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:62412` with
  `ontology_mapping.ontology_id: CHEBI:62412`, label
  `phenazine-1-carboxylic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:62412` resolves `CHEBI:62412`
  `phenazine-1-carboxylic acid`.
- A local CAS checksum calculation confirmed that `2538-68-3` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Phenazine-1-carboxylic_Acid` exactly to `CHEBI:62412`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe phenazine-1-carboxylic acid.
- `PCA` is an abbreviation for the same compound and is already represented in
  `mappings/ingredient_mappings_synonym_enrich_review.tsv`.
- The final SSSOM row exports only `PCA` and `CAS:2538-68-3`.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
