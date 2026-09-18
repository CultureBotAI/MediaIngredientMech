# `data/ingredients/mapped/Cows_Milk.yaml`

## Verdict

Pass. The mim-queue record is grounded to active `FOODON:02020891` cow milk,
classified as an undefined mixture, has a matching 2/2 CultureMech occurrence
count, exports a clean final SSSOM row, and has no unsupported roles or
component claims.

## Identity

- Reviewed record: `data/ingredients/mapped/Cows_Milk.yaml`.
- Identifier and grounding: `identifier: FOODON:02020891`,
  `ontology_mapping.ontology_id: FOODON:02020891`,
  `ontology_label: cow milk`, `ontology_source: FOODON`,
  `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Live OLS lookup by `FOODON:02020891` returns active `FOODON:02020891`
  labelled `cow milk` and describes milk produced by cow lactation.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cotarnine_Chloride.yaml data/ingredients/mapped/Coumarate.yaml data/ingredients/mapped/Cows_Milk.yaml data/ingredients/mapped/Cr1_Soil.yaml data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Coumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the only CHEBI-identified record in this batch.
  `Cotarnine_Chloride`, `Cows_Milk`, `Cr1_Soil`, and
  `Cr2_So43_X_N_H2o` were intentionally skipped because their CAS, FOODON,
  ENVO, and local `kgmicrobe.compound` identifiers are outside this
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
  `reports` found the active `MIM:Cows_Milk` final SSSOM row, the row-review
  synonym-enrichment note, and matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `FOODON:02020891`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 2 rows for
  `FOODON:02020891` whose occurrence weights sum to 2, matching the explicit
  2/2 `occurrence_statistics`.
- The raw duplicate `Cow's milk` synonym is filtered from the final SSSOM
  `other` column, leaving no exported synonym residue to triage.

## Completeness

- The FoodOn identifier, undefined-mixture classification, final SSSOM row,
  aggregate copy, docs row, and occurrence count are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
