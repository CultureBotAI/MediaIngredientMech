# `data/ingredients/mapped/Leupeptin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:6426 identity, active ChEBI structure,
PubChem structure, empty synonym payload, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Leupeptin.yaml`.
- Identifier and grounding: `identifier: CHEBI:6426` with
  `ontology_mapping.ontology_id: CHEBI:6426`, label `leupeptin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C20H38N6O4`, InChI, SMILES, and
  molecular weight from ChEBI and PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Leupeptin` through `Levomenthol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:6426` as active `leupeptin`, records formula
  `C20H38N6O4`, and records the same InChI and SMILES as the YAML record.
- PubChem resolves the name `leupeptin` to CID `72429` with formula
  `C20H38N6O4` and the same InChI as the YAML record.
- The MicrobeDecoder occurrence is retained in `source_occurrences` as one
  `BacDive_Metabolite_production` import, while `total_occurrences` and
  `media_count` correctly remain zero for the media-recipe corpus.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6426` and has
  an empty `other` field.

## Completeness

- The active CHEBI identity, formula, structure block, aggregate copy, and final
  SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
