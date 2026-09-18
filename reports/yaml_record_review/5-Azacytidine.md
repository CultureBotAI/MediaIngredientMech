# `data/ingredients/mapped/5-Azacytidine.yaml`

## Verdict

Pass, none. The exact `CHEBI:2038` 5-azacytidine identity, CAS, exact
systematic synonym, chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-Azacytidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:2038` with
  `ontology_mapping.ontology_id: CHEBI:2038`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:2038` is active and resolves to
  `5-azacytidine`.
- The current ChEBI page reports CAS `320-67-2`, formula `C8H12N4O5`, the
  stored SMILES, and the stored InChI for `CHEBI:2038`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-vinylphenol.yaml data/ingredients/mapped/4_Carbon_Mix.yaml data/ingredients/mapped/4h-pyran-4-one.yaml data/ingredients/mapped/5-Aminolevulinic_Acid.yaml data/ingredients/mapped/5-Azacytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/5-Azacytidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, InChI, and exact ChEBI synonym
  all support the 5-azacytidine identity.
- The SSSOM row maps `MIM:5-Azacytidine` to `CHEBI:2038` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and the expected exact synonym
  plus `CAS:320-67-2` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy, SSSOM
  row, generated docs, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact systematic synonym, and
  `ingredient_type` are populated.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
