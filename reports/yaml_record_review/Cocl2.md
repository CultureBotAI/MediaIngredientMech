# `data/ingredients/mapped/Cocl2.yaml`

## Verdict

Needs curation; major. The CultureMech `CoCl2` row is exactly grounded to active
anhydrous `CHEBI:35696`; its CAS RN, formula, InChI, SMILES, 527/527
CultureMech occurrence count, trace-element role evidence, and aggregate copy
agree. The final SSSOM `other` column still exports a tetrahydrate label and a
malformed hydrate token against the anhydrous cobalt dichloride row.

## Identity

- Reviewed record: `data/ingredients/mapped/Cocl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:35696`,
  `ontology_mapping.ontology_id: CHEBI:35696`,
  `ontology_label: cobalt dichloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:35696`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:35696` returns active `CHEBI:35696` labelled
  `cobalt dichloride` with CAS RN `7646-79-9`, formula `2Cl.Co`, and the same
  InChI and SMILES stored in `chemical_properties`.
- The current YAML correctly marks several hidden hexahydrate surface forms as
  `REJECTED_LABEL`, including `CoCl2.6H2O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cobalamine.yaml data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml data/ingredients/mapped/Cocl2.yaml data/ingredients/mapped/Cocl2_X_2_H2o.yaml data/ingredients/mapped/Cocl2_X_4_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cobalamine.yaml data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml data/ingredients/mapped/Cocl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch.
  `Cocl2_X_2_H2o` and `Cocl2_X_4_H2o` were intentionally skipped because their
  `kgmicrobe.compound` identifiers are local registry CURIEs outside Engine A's
  OAK/OLS prefix scope.
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
  `reports` found the active exact `MIM:Cocl2` SSSOM row, the synonym-enrich row
  review, the rejected hydrate-label edits, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `CHEBI:35696` as the active anhydrous record's `identifier` and `ontology_id`
  and as the intended close-match parent for local hydrate registry records.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 527 rows for `CHEBI:35696`
  whose occurrence weights sum to 527, matching the explicit 527/527
  `occurrence_statistics`.
- The active `CoCl .6H O` exact synonym is still emitted to final SSSOM even
  though it is a malformed hydrate-like label, and the final SSSOM row also
  still publishes `CoCl2 x 4 H2O` against anhydrous `CHEBI:35696`.
- The `TRACE_ELEMENT` role is supported by a `DATABASE_ENTRY` that preserves
  CultureMech's imported Mineral source role text.

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence count,
  role evidence, aggregate copy, and docs row are populated and agree.
- The active gap is final SSSOM synonym hygiene for hydrate or malformed formula
  labels on the anhydrous record.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cocl2.yaml`, reject `CoCl .6H O`; also
  remove stale final-SSSOM export of `CoCl2 x 4 H2O` from the anhydrous
  `MIM:Cocl2` row.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
