# `data/ingredients/mapped/Beef_Heart_Infusion.yaml`

## Verdict

Needs curation, minor. The kg-microbe registry identity, broader FOODON parent
mapping, 2/2 occurrence count, provisional protein-source role, SSSOM rows, and
aggregate copy pass, but top-level `notes` still describe the obsolete
imported-unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/Beef_Heart_Infusion.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:beef_heart_infusion` with
  `ontology_mapping.ontology_id: FOODON:00004410`,
  `ontology_label: beef heart`, `ontology_source: FOODON`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `foodon` resolves `FOODON:00004410` to `beef heart`.
- The record denotes a beef-heart infusion, a more specific prepared material
  than the broader FOODON beef-heart parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beef_Heart.yaml data/ingredients/mapped/Beef_Heart_Infusion.yaml data/ingredients/mapped/Beijerincks_Solution.yaml data/ingredients/mapped/Benzaldehyde.yaml data/ingredients/mapped/Benzalkonium_Chloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Beef_Heart_Infusion.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The authoritative SSSOM rows are the `skos:narrowMatch` to
  `FOODON:00004410` and the `skos:exactMatch` registry row to
  `kgmicrobe.ingredient:beef_heart_infusion`.
- `data/custom/kgmicrobe_ingredients.tsv` preserves the same local
  kg-microbe ingredient mint against parent `FOODON:00004410`.
- `rg -c` over `mappings/culturemech_recipe_membership.tsv` found two rows for
  `kgmicrobe.ingredient:beef_heart_infusion`, matching
  `occurrence_statistics: 2/2`.
- The only stale claim is the top-level `notes` field: it still says this
  CultureBotHT import had no ontology match and needed curator review, even
  though the record was later grounded to a FOODON parent and minted as a
  kg-microbe ingredient to preserve infusion-level specificity.

## Completeness

- The kg-microbe primary identifier, FOODON parent, raw source synonym,
  provisional role, occurrence count, SSSOM rows, and aggregate copy are
  populated.
- No CAS, formula, InChI, SMILES, supplied form, or component list is required
  for this un-decomposed beef-heart infusion.

## Recommended Edits

- Minor: update `notes` in `data/ingredients/mapped/Beef_Heart_Infusion.yaml`
  to describe the current kg-microbe identity and FOODON parent mapping, then
  run `just sync-curated`.
