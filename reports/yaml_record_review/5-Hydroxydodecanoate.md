# `data/ingredients/mapped/5-Hydroxydodecanoate.yaml`

## Verdict

Pass, none. The exact `CHEBI:195418` 5-hydroxylaurate identity, exact synonym
grounding, ChEBI-derived anion InChI, SSSOM row, kg-microbe node ID, and
aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-Hydroxydodecanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:195418` with
  `ontology_mapping.ontology_id: CHEBI:195418`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:195418` is active and resolves to
  `5-hydroxylaurate`.
- The current ChEBI page reports formula `C12H23O3`, anion SMILES, and the
  stored deprotonated InChI for `CHEBI:195418`.
- `kg_microbe_node_id: CHEBI:195418` and `ingredient_type: SINGLE_INGREDIENT`
  are present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml data/ingredients/mapped/5-Hydroxydodecanoate.yaml data/ingredients/mapped/5-Hydroxymethylfurfural.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/5-Hydroxydodecanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The active ChEBI term and its exact synonym support the mapping from raw
  `5-Hydroxydodecanoate` to `CHEBI:195418` `5-hydroxylaurate`.
- The official ChEBI formula and InChI agree with the record's deprotonated
  anion identity; the record does not mix the neutral acid with the laurate
  anion.
- The two curated exact synonyms, lowercase `5-hydroxydodecanoate` and
  `5-hydroxylaurate`, are exact labels for the same anion.
- The SSSOM row maps `MIM:5-Hydroxydodecanoate` to `CHEBI:195418` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy, SSSOM
  row, old unmapped synonym audit, generated docs, and ignored aggregate
  backups.

## Completeness

- InChI, molecular weight, exact ChEBI synonyms, kg-microbe node ID, and
  `ingredient_type` are populated.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
