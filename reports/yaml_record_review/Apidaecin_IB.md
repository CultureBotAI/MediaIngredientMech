# `data/ingredients/mapped/Apidaecin_IB.yaml`

## Verdict

Pass. The record is intentionally grounded to the MeSH `apidaecin` SCR through
its exact `apidaecin Ib` synonym, and the MeSH identity, exact raw source label,
SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Apidaecin_IB.yaml`.
- Identifier and grounding: `identifier: mesh:C061361` with
  `ontology_mapping.ontology_id: mesh:C061361`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` records the exact OLS
  synonym hit from `Apidaecin IB` to `MESH:C061361` `apidaecin` through
  synonym `apidaecin Ib`.
- `kg_microbe_node_id: mesh:C061361` is synchronized with the primary
  identifier.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apidaecin_IB.yaml data/ingredients/mapped/Apigenin.yaml data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml data/ingredients/mapped/Apiole.yaml data/ingredients/mapped/Apple_Juice.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Apidaecin_IB.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` row 38 records
  `UNMAPPED_0173` / `Apidaecin IB` as a `SYNONYM_EXACT` hit to
  `mesh:C061361` with matched synonym `apidaecin Ib`.
- `mappings/ingredient_mappings.sssom.tsv` row 442 maps
  `MIM:Apidaecin_IB` to `mesh:C061361` with `skos:exactMatch`.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, OLS exact-audit row, SSSOM row, and a schema unit-test fixture
  for `mesh:C061361`.

## Completeness

- MeSH identity, raw source label, curation history, `kg_microbe_node_id`,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  no-CAS fallback rather than a media recipe ingredient.
- No chemical structure, component, role, environmental context, discussion, or
  dataset entry is needed.

## Recommended Edits

- None.
