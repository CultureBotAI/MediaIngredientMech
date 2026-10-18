# `data/ingredients/mapped/D-Galacturonic_Acid_Monohydrate.yaml`

## Verdict

Needs curation, with a major SSSOM synonym issue. The CAS primary identifier,
monohydrate formula correction, and `skos:closeMatch` to anhydrous
`CHEBI:18024` correctly avoid collapsing the hydrate into D-galacturonic acid,
but the final SSSOM still exports `D-galacturonate`, an anhydrous-parent
synonym, as `other` for the hydrate subject.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Galacturonic_Acid_Monohydrate.yaml`.
- Current identifier and grounding: `identifier: cas:91510-62-2`,
  `ontology_mapping.ontology_id: CHEBI:18024`,
  `ontology_label: D-galacturonic acid`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:18024` returns active `CHEBI:18024` labelled
  `D-galacturonic acid`, the anhydrous close-match parent, with an anhydrous
  formula `C6H10O7`.
- A live exact CHEBI label/synonym search for the full monohydrate label
  returned no exact candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:91510-62-2` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Galacturonic_Acid_Monohydrate.yaml data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml data/ingredients/mapped/D-Glucosamine_Hydrochloride.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  This record and `D-Glucosamine_Hydrochloride` were intentionally skipped
  because their primary identifiers are CAS registry CURIEs.
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

- The `CLOSE_MATCH` regrade and `C6H10O7.H2O` formula repair are appropriate:
  live `CHEBI:18024` resolves to anhydrous `D-galacturonic acid`, and this
  record already explains that the monohydrate is similar to but not subsumed
  by the anhydrous form.
- The `cas:91510-62-2` registry row in final SSSOM matches the YAML primary
  identifier and `chemical_properties.cas_rn`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the old CAS
  and kg-microbe `UNKNOWN_TERM` rows are expected registry identifiers rather
  than OAK/OLS ontology terms.
- The active exact synonym `D-galacturonate` is a synonym of the anhydrous
  `CHEBI:18024` parent, not of this monohydrate; exporting it as final SSSOM
  `other` erases the hydrate boundary that issues #321 and #342 intentionally
  preserved.

## Completeness

- No exact CHEBI replacement for the monohydrate was found in live OLS, so the
  bounded fix is not a remapping.
- No roles, supplied-form substructure beyond the CAS identity, or mixture
  components are asserted, so there are no unsupported secondary claims beyond
  the active anhydrous synonym.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected parent, CAS-registry, and
  row-review surfaces and no curated exact CHEBI successor for the monohydrate.

## Recommended Edits

- In `data/ingredients/mapped/D-Galacturonic_Acid_Monohydrate.yaml`, remove or
  demote `D-galacturonate` from active `EXACT_SYNONYM` status so the final
  SSSOM no longer publishes it in `other`, then regenerate and validate the
  final SSSOM.
