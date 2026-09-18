# `data/ingredients/mapped/Coso4.yaml`

## Verdict

Needs curation; major. The anhydrous cobalt sulfate identity, CAS RN, formula,
InChI, SMILES, 64/64 CultureMech occurrence count, and trace-element role pass,
but the active final SSSOM row still exports `cobalt(2+) sulfate--water (1/7)`,
an exact synonym of the sibling heptahydrate `CHEBI:91244`, as an `other` token
for anhydrous `CHEBI:53470`.

## Identity

- Reviewed record: `data/ingredients/mapped/Coso4.yaml`.
- Identifier and grounding: `identifier: CHEBI:53470`,
  `ontology_mapping.ontology_id: CHEBI:53470`,
  `ontology_label: cobalt(2+) sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:53470`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:53470` returns active `CHEBI:53470` labelled
  `cobalt(2+) sulfate` with anhydrous cobalt sulfate synonyms.
- The record stores CAS RN `10124-43-3`, formula `Co.O4S`, and populated InChI
  and SMILES values for anhydrous cobalt sulfate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Corn_Meal.yaml data/ingredients/mapped/Corn_Oil.yaml data/ingredients/mapped/Corn_Steep_Liquor_Glucose_Fumarate.yaml data/ingredients/mapped/Coso4.yaml data/ingredients/mapped/Coso4_X_7_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Corn_Oil.yaml data/ingredients/mapped/Coso4.yaml data/ingredients/mapped/Coso4_X_7_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch. `Corn_Meal` and
  `Corn_Steep_Liquor_Glucose_Fumarate` were intentionally skipped because their
  FOODON and local `kgmicrobe.ingredient` identifiers are outside this
  CHEBI-focused LinkML term-validation pass.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active `MIM:Coso4` final SSSOM row, the OAK/OLS
  row-review confirmation, the sibling heptahydrate row, and matching generated
  docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:53470`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 64 rows for
  `CHEBI:53470` whose occurrence weights sum to 64, matching the explicit
  64/64 `occurrence_statistics`.
- Live OLS lookup by `CHEBI:91244` confirms
  `cobalt(2+) sulfate--water (1/7)` is an exact synonym of cobalt(2+) sulfate
  heptahydrate, but `mappings/ingredient_mappings.sssom.tsv` still exports that
  token on the anhydrous `MIM:Coso4` row.
- `TRACE_ELEMENT` is backed by original CultureMech `Role: Mineral source`
  database text.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence count,
  trace-element role evidence, SSSOM row, aggregate copy, and docs row are
  populated and synchronized.
- The consequential gap is the hydrate-specific `other` token on the final
  anhydrous SSSOM row.

## Recommended Edits

- Major: in `data/ingredients/mapped/Coso4.yaml`, mark
  `cobalt(2+) sulfate--water (1/7)` as a rejected hydrate synonym, move it to
  `Coso4_X_7_H2o.yaml`, or otherwise filter it so the anhydrous cobalt sulfate
  SSSOM row no longer exports it.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
