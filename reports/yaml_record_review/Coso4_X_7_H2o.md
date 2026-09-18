# `data/ingredients/mapped/Coso4_X_7_H2o.yaml`

## Verdict

Needs curation; major. The record was correctly promoted to active `CHEBI:91244`
cobalt(2+) sulfate heptahydrate, and its CAS RN, formula, 828/828 CultureMech
occurrence count, SSSOM row, and hydrate-specific synonyms agree. The remaining
gap is that the active InChI and SMILES still describe anhydrous cobalt sulfate
from the old `CHEBI:53470` parent.

## Identity

- Reviewed record: `data/ingredients/mapped/Coso4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91244`,
  `ontology_mapping.ontology_id: CHEBI:91244`,
  `ontology_label: cobalt(2+) sulfate heptahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id: CHEBI:91244`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:91244` returns active `CHEBI:91244` labelled
  `cobalt(2+) sulfate heptahydrate` with heptahydrate-specific synonyms.
- The CAS RN was corrected to the hydrate-specific `10026-24-1`, and the
  formula was corrected to `Co.O4S.7H2O`.
- `chemical_properties.inchi` and `chemical_properties.smiles` remain identical
  to anhydrous cobalt sulfate even though the active record now represents the
  heptahydrate.

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
  `reports` found the active `MIM:Coso4_X_7_H2o` final SSSOM row, stale
  pre-promotion row-review artifacts under old `CHEBI:53470`, and matching
  generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:91244`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 828 rows for
  `CHEBI:91244` whose occurrence weights sum to 828, matching the explicit
  828/828 `occurrence_statistics`.
- The final SSSOM `other` column contains CoSO4 heptahydrate surface forms,
  `Cobalt sulfate heptahydrate`, and `CAS:10026-24-1`, all specific to the
  active heptahydrate grounding.
- `TRACE_ELEMENT` is backed by original CultureMech `Role: Mineral source`
  database text.

## Completeness

- The ChEBI hydrate identifier, CAS RN, formula, occurrence count,
  trace-element role evidence, SSSOM row, aggregate copy, and docs row are
  populated and synchronized.
- The consequential gap is the stale anhydrous structure string pair left after
  the hydrate promotion.

## Recommended Edits

- Major: in `data/ingredients/mapped/Coso4_X_7_H2o.yaml`, replace or remove the
  stale anhydrous InChI and SMILES so every active `chemical_properties` value
  reflects `CHEBI:91244` cobalt(2+) sulfate heptahydrate.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
