# `data/ingredients/mapped/5-Hydroxymethylfurfural.yaml`

## Verdict

Pass, none. The exact `CHEBI:412516` identity, CAS, exact ChEBI synonym,
chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-Hydroxymethylfurfural.yaml`.
- Identifier and grounding: `identifier: CHEBI:412516` with
  `ontology_mapping.ontology_id: CHEBI:412516`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:412516` is active and resolves to
  `5-hydroxymethylfurfural`.
- The current ChEBI page reports CAS `67-47-0`, formula `C6H6O3`, the stored
  SMILES, and the stored InChI for `CHEBI:412516`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml data/ingredients/mapped/5-Hydroxydodecanoate.yaml data/ingredients/mapped/5-Hydroxymethylfurfural.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/5-Hydroxymethylfurfural.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, InChI, and exact ChEBI synonym
  all support the 5-hydroxymethylfurfural identity.
- The SSSOM row maps `MIM:5-Hydroxymethylfurfural` to `CHEBI:412516` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and the expected exact synonym
  plus `CAS:67-47-0` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy, SSSOM
  row, generated docs, source review outputs, stale advisory rows, and ignored
  aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
