# `data/ingredients/mapped/Lomefloxacin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:116278 identity, active ChEBI/PubChem
structure, empty synonym payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lomefloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:116278` with
  `ontology_mapping.ontology_id: CHEBI:116278`, label `lomefloxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C17H19F2N3O3`, InChI, SMILES, and
  molecular weight from ChEBI and PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Locust_Bean_Gum` through `Loratadine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:116278` as active `lomefloxacin`, records formula
  `C17H19F2N3O3`, and records the same InChI and SMILES as the YAML record.
- PubChem resolves the name `lomefloxacin` to CID `3948` with formula
  `C17H19F2N3O3` and the same InChI as the YAML record.
- The MicrobeDecoder occurrence is retained in `source_occurrences` as four
  `BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity` imports,
  while `total_occurrences` and `media_count` correctly remain zero for the
  media-recipe corpus.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:116278` and has
  an empty `other` field.

## Completeness

- The active CHEBI identity, formula, structure block, aggregate copy, and final
  SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
