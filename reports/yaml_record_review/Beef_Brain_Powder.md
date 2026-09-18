# `data/ingredients/mapped/Beef_Brain_Powder.yaml`

## Verdict

Needs curation, minor. The kg-microbe registry identity, broader FOODON parent
mapping, refreshed 3/3 occurrence count, provisional protein-source role, SSSOM
rows, and aggregate copy pass, but top-level `notes` still describe the
obsolete imported-unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/Beef_Brain_Powder.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:beef_brain_powder` with
  `ontology_mapping.ontology_id: FOODON:02020911`,
  `ontology_label: beef brain`, `ontology_source: FOODON`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `foodon` resolves `FOODON:02020911` to `beef brain`;
  exact OLS search for `Beef brain powder` itself returned no FOODON term.
- The record denotes beef brain powder, a more specific prepared material than
  the broader FOODON beef brain parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Bedaquiline.yaml data/ingredients/mapped/Beef.yaml data/ingredients/mapped/Beef_Brain_Powder.yaml data/ingredients/mapped/Beef_Extract.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Beef_Brain_Powder.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `FOODON:02020911` and the `skos:exactMatch` registry row to
  `kgmicrobe.ingredient:beef_brain_powder`.
- `data/custom/kgmicrobe_ingredients.tsv` preserves the same local
  kg-microbe ingredient mint against parent `FOODON:02020911`.
- `rg -c` over `mappings/culturemech_recipe_membership.tsv` found three rows
  for `kgmicrobe.ingredient:beef_brain_powder`, matching
  `occurrence_statistics: 3/3`.
- The only stale claim is the top-level `notes` field: it still says this
  mim-queue import had no ontology match and needed curator review, even though
  the record was later grounded to a FOODON parent and minted as a kg-microbe
  ingredient to preserve powder-level specificity.

## Completeness

- The kg-microbe primary identifier, FOODON parent, raw source synonym,
  provisional role, occurrence count, SSSOM rows, and aggregate copy are
  populated.
- No CAS, formula, InChI, SMILES, supplied form, or component list is required
  for this un-decomposed tissue powder.

## Recommended Edits

- Minor: update `notes` in `data/ingredients/mapped/Beef_Brain_Powder.yaml` to
  describe the current kg-microbe identity and FOODON parent mapping, then run
  `just sync-curated`.
