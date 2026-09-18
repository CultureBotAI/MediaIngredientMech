# `data/ingredients/mapped/Beef_Extract.yaml`

## Verdict

Pass. The exact `FOODON:03302088` beef extract mapping, curated catalog
synonyms, removed false-positive CAS, refreshed occurrence count, SSSOM row,
and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Beef_Extract.yaml`.
- Identifier and grounding: `identifier: FOODON:03302088` with
  `ontology_mapping.ontology_id: FOODON:03302088`,
  `ontology_label: beef extract`, `ontology_source: FOODON`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `foodon` resolves `FOODON:03302088` to `beef extract`.
- The record denotes commercial beef extract as a multi-component food extract,
  not a single CHEBI chemical or a CAS-identifiable compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Bedaquiline.yaml data/ingredients/mapped/Beef.yaml data/ingredients/mapped/Beef_Brain_Powder.yaml data/ingredients/mapped/Beef_Extract.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Beef_Extract.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 546 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The 2026-04-18 FOODON promotion records that the commercial beef-extract
  forms were promoted to `FOODON:03302088`; the 2026-07-05 curation event
  explicitly removed PubChem CAS `103-47-9` as a CHES false positive.
- `mappings/complex_ingredients.tsv` records the same FOODON identity and the
  same Bacto, BD-Difco, BBL, Sigma, and Lab-Lemco commercial variants that are
  stored as synonyms.
- `rg -c` over `mappings/culturemech_recipe_membership.tsv` found 330 distinct
  recipe rows for `FOODON:03302088`, matching
  `occurrence_statistics.media_count`.

## Completeness

- The exact FOODON identifier, raw and catalog synonyms, provisional
  protein-source role, occurrence count, SSSOM row, and aggregate copy are
  populated.
- No CAS, formula, InChI, SMILES, supplied form, or component list is required
  for this un-decomposed commercial extract.

## Recommended Edits

- None.
