# `data/ingredients/mapped/Lincomycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:6472 identity, active ChEBI/PubChem
structure, empty synonym payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lincomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:6472` with
  `ontology_mapping.ontology_id: CHEBI:6472`, label `lincomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C18H34N2O6S`, InChI, SMILES, and
  molecular weight from ChEBI and PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lignin_Alkali` through `Lincomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Limonin.yaml`, `Linalool.yaml`, and `Lincomycin.yaml`.

## Evidence

- EBI OLS4 resolves `CHEBI:6472` as active `lincomycin`, records formula
  `C18H34N2O6S`, and records the same InChI and SMILES as the YAML record.
- PubChem resolves the name `lincomycin` to CID `3000540` with formula
  `C18H34N2O6S` and the same InChI as the YAML record.
- The MicrobeDecoder occurrence is retained in `source_occurrences` as 281
  `BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity` imports,
  while `total_occurrences` and `media_count` correctly remain zero for the
  media-recipe corpus.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6472` and has
  an empty `other` field.

## Completeness

- The active CHEBI identity, formula, structure block, aggregate copy, and final
  SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
