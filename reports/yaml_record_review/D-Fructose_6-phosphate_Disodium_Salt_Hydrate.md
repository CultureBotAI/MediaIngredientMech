# `data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml`

## Verdict

Needs curation, with major role and SSSOM synonym issues. The CAS primary
identifier and `skos:closeMatch` to anhydrous `CHEBI:190546` correctly avoid
collapsing the hydrate into the parent, but the final SSSOM row still exports
an anhydrous parent synonym as `other`, and `CARBON_SOURCE` is asserted only
from a provisional name-pattern computation.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml`.
- Current identifier and grounding: `identifier: cas:26177-86-6`,
  `ontology_mapping.ontology_id: CHEBI:190546`,
  `ontology_label: D-Fructose 6-Phosphate-Disodium Salt`,
  `ontology_source: CHEBI`, `mapping_quality: CLOSE_MATCH`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:190546` returns active `CHEBI:190546` labelled
  `D-Fructose 6-Phosphate-Disodium Salt`, the anhydrous close-match parent.
- A live exact CHEBI label/synonym search for the full hydrate label returned
  no exact candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:26177-86-6` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-2-Aminobutyric_Acid.yaml data/ingredients/mapped/D-Alanine.yaml data/ingredients/mapped/D-Aspartic_Acid.yaml data/ingredients/mapped/D-Cycloserine.yaml data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-2-Aminobutyric_Acid.yaml data/ingredients/mapped/D-Alanine.yaml data/ingredients/mapped/D-Aspartic_Acid.yaml data/ingredients/mapped/D-Cycloserine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-primary exact records in this batch.
  This record was intentionally skipped because its primary identifier is
  `cas:26177-86-6`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The `CLOSE_MATCH` regrade is appropriate: live `CHEBI:190546` resolves to
  the anhydrous disodium salt, and the record already explains that a hydrate
  is similar to but not subsumed by its anhydrous form.
- The `cas:26177-86-6` registry row in final SSSOM matches the YAML primary
  identifier and `chemical_properties.cas_rn`.
- `mappings/culturemech_recipe_membership.tsv` contains no rows for this CAS
  primary or its `CHEBI:190546` parent, matching the record's 0/0
  `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the old CAS
  and kg-microbe `UNKNOWN_TERM` rows are expected registry identifiers rather
  than OAK/OLS ontology terms.
- The active exact synonym
  `disodium;[(2R,3R,4S)-2,3,4,6-tetrahydroxy-5-oxohexyl] phosphate` is a
  synonym of anhydrous `CHEBI:190546`; exporting it as `other` for the hydrate
  MIM subject erases the hydrate boundary that issue #342 intentionally
  preserved.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from a curated name-pattern rule and its own `curator_note` calls it
  provisional.

## Completeness

- No exact CHEBI replacement for the hydrated salt was found in live OLS, so
  the bounded fix is not a remapping.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected parent, CAS-registry, and
  row-review surfaces and no curated exact CHEBI successor for the hydrate.

## Recommended Edits

- In
  `data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml`,
  remove or demote the anhydrous `disodium;[...] phosphate` exact synonym so
  the final SSSOM no longer publishes it in `other`, then regenerate the final
  SSSOM.
- In the same record, either replace the computational `CARBON_SOURCE`
  evidence with direct source-backed media-role evidence for this hydrated
  salt, or remove the role facet; then rerun strict validation and the final
  SSSOM build.
