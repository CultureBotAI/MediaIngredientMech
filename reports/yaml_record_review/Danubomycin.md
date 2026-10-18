# `data/ingredients/mapped/Danubomycin.yaml`

## Verdict

Needs curation. The reviewed local `kgmicrobe.compound:danubomycin` placeholder
still has no exact live OLS replacement and can remain as a local identity, but
the `SELECTIVE_AGENT` role is supported only by a provisional name-pattern
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Danubomycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:danubomycin` with
  the same `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- Live OLS exact search for `Danubomycin` returned zero hits, agreeing with the
  May 2026 placeholder review that found no exact external ontology candidate
  or normalized local duplicate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through the two ChEBI records and then failed on
  `kgmicrobe.compound:danomycin` because local registry targets hit the known
  OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping `Danomycin` and this local
  placeholder.
- `curl -L ... q=Danubomycin&exact=true`: live OLS returned zero exact hits.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `kgmicrobe.compound:danubomycin`, matching `occurrence_statistics.media_count:
  0` and `total_occurrences: 0`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  kg-microbe object as `expected_registry_identifier` pending promotion to an
  external ontology term.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Danubomycin` to `kgmicrobe.compound:danubomycin` with
  `skos:exactMatch`, object source `kgm:compound`, and an empty `other`
  column.
- The `SELECTIVE_AGENT` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the
  name-pattern role is provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `kgmicrobe.compound:danubomycin`.
- Chemical properties are correctly empty while the exact external identity is
  unresolved.
- The record has no source occurrences, component decomposition, or
  environmental contexts to resolve.

## Recommended Edits

- In `data/ingredients/mapped/Danubomycin.yaml`, remove the provisional
  `SELECTIVE_AGENT` role or replace its `COMPUTATIONAL_PREDICTION` evidence
  with inspected claim-level evidence for this compound.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
