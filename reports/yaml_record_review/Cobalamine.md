# `data/ingredients/mapped/Cobalamine.yaml`

## Verdict

Needs curation; major. The generic cobalamin identity is correctly regrounded to
active `CHEBI:30411`, which leaves oxidation state unspecified and correctly no
longer carries CAS or structure fields. The active synonym set and final SSSOM
row still publish oxidation-state-specific and concentration-qualified labels
against that generic term.

## Identity

- Reviewed record: `data/ingredients/mapped/Cobalamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:30411`,
  `ontology_mapping.ontology_id: CHEBI:30411`,
  `ontology_label: cobalamin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:30411`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS search for `CHEBI:30411` returns active `CHEBI:30411` labelled
  `cobalamin` and describes it as cobalamin with the central cobalt oxidation
  state unspecified.
- The absence of CAS RN, formula, InChI, and SMILES fields is intentional here:
  the August 2026 curation removed values copied from specific +1 or +3
  cobalamin oxidation states.

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
  `reports` found the active exact `MIM:Cobalamine` SSSOM row, the stale
  pre-regrounding row-review artifacts for `CHEBI:28911`, the aggregate/docs
  rows, and the final `other` values exported after regrounding to
  `CHEBI:30411`.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `CHEBI:30411` only as this record's `identifier` and `ontology_id`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 9 rows for `CHEBI:30411`
  whose occurrence weights sum to 9, matching the explicit 9/9
  `occurrence_statistics`.
- The final SSSOM `other` column still contains `Cob(III)alamin`,
  `Cobalamin (III)`, and `cobalamin(III)`, which specify the +3 term that this
  record was intentionally moved away from. It also contains `cobalamin(1+)`,
  which specifies the +1 state, and a concentration-qualified Cobalamin surface
  form rather than a genuine synonym.
- The `VITAMIN_SOURCE` role is supported by a `DATABASE_ENTRY` that preserves
  CultureMech's imported Vitamin Source role text.

## Completeness

- The generic ChEBI identifier, lack of oxidation-state-specific structure
  fields, role evidence, 9/9 occurrence count, SSSOM row, aggregate copy, and
  docs row are populated and agree.
- The active gap is the synonym set: exact and raw synonyms still leak
  oxidation-state-specific or concentration-qualified labels into final SSSOM
  and search outputs.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cobalamine.yaml`, remove or reject
  `Cob(III)alamin`, `Cobalamin (III)`, `cobalamin(III)`, `cobalamin(1+)`, and
  the concentration-qualified Cobalamin surface form.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
