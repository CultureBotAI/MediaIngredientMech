# `data/ingredients/mapped/Beef_Heart.yaml`

## Verdict

Needs curation, minor. The exact `FOODON:00004410` beef-heart mapping,
refreshed 164/164 occurrence count, provisional protein-source role, SSSOM row,
and aggregate copy pass, but the top-level `notes` still describe the obsolete
imported-unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/Beef_Heart.yaml`.
- Identifier and grounding: `identifier: FOODON:00004410` with
  `ontology_mapping.ontology_id: FOODON:00004410`,
  `ontology_label: beef heart`, `ontology_source: FOODON`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `foodon` resolves `FOODON:00004410` to `beef heart`.
- The record denotes beef heart material and is correctly typed as
  `UNDEFINED_MIXTURE`, not as a single chemical.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beef_Heart.yaml data/ingredients/mapped/Beef_Heart_Infusion.yaml data/ingredients/mapped/Beijerincks_Solution.yaml data/ingredients/mapped/Benzaldehyde.yaml data/ingredients/mapped/Benzalkonium_Chloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Beef_Heart.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 547 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 378 marked the
  `FOODON:00004410` mapping `CONFIRMED`; the fresh Engine A and OLS checks
  still agree with that verdict.
- `rg -c` over `mappings/culturemech_recipe_membership.tsv` found 164 rows for
  `FOODON:00004410`, matching `occurrence_statistics: 164/164`.
- The only stale claim is the top-level `notes` field: it still says this
  CultureBotHT import had no ontology match and needed curator review, even
  though the record was later exact-mapped to FOODON and occurrence-refreshed.

## Completeness

- The exact FOODON identifier, raw source synonym, provisional role, occurrence
  count, SSSOM row, and aggregate copy are populated.
- No CAS, formula, InChI, SMILES, supplied form, or component list is required
  for this un-decomposed beef-heart material.

## Recommended Edits

- Minor: update `notes` in `data/ingredients/mapped/Beef_Heart.yaml` to
  describe the current exact FOODON mapping and refreshed CultureMech occurrence
  count, then run `just sync-curated`.
