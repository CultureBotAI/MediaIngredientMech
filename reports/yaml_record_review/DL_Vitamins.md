# `data/ingredients/mapped/DL_Vitamins.yaml`

## Verdict

Pass. `DL vitamins` is modeled as a local kg-microbe stock solution rather than
as one vitamin compound, the CultureBotHT Mixes tab supports the ten listed
vitamin components and the vitamin-source role, and the final SSSOM row
publishes only a true same-stock source label in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/DL_Vitamins.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:dl_vitamins` with the same
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The local identity is appropriate because `DL vitamins` is a named
  multi-component CultureBotHT vitamin stock and the record's curation evidence
  documents searches of CHEBI, NCIT, MeSH, FOODON, and ENVO that found no term
  for the full preparation.
- The record is typed as `ingredient_type: STOCK_SOLUTION` and
  `solution_type: VITAMIN_MIX`, so it does not collapse the mix onto any single
  component vitamin.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed when non-OBO fallback targets were included.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping this
  `kgmicrobe.ingredient:` fallback and `DNA_From_Salmon`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed in
  the unchanged full-corpus validation run.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT Mixes CSV defines a 100X DL vitamins recipe with the ten
  component rows recorded in YAML: d-Biotin `0.02 mg/L`, Folic Acid
  `0.02 mg/L`, Pyridoxine HCl `0.1 mg/L`, Riboflavin `0.05 mg/L`,
  Thiamine `0.05 mg/L`, Nicotinic Acid `0.05 mg/L`, Pantothenic Acid
  `0.05 mg/L`, Vitamin B12 `0.001 mg/L`, p-Amino Benzoic Acid `0.05 mg/L`,
  and DL-6,8-thioctic acid `0.05 mg/L`.
- The `VITAMIN_SOURCE` role has `DATABASE_ENTRY` evidence scoped to the same
  Mixes tab, and the cited recipe is a vitamin premix.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:DL_Vitamins` to `kgmicrobe.ingredient:dl_vitamins` with
  `skos:exactMatch`.
- The final SSSOM `other` token `DL vitamins (see below)` is a CultureMech
  occurrence surface for this same stock solution and is not an instruction or
  non-identity note.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `kgmicrobe.ingredient:dl_vitamins`.
- The component assertion is marked `COMPLETE`, and all ten component IDs are
  catalog references rather than external component-only identities.
- No CAS, formula, or ChEBI parent is required for the full stock mixture.

## Recommended Edits

- None.
