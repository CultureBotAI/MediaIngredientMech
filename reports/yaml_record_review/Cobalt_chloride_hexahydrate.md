# `data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml`

## Verdict

Needs curation; major. The CAS-derived cobalt chloride hexahydrate record is
grounded to active `CHEBI:53503`; its CAS RN, hydrate-specific formula, InChI,
SMILES, 2638-count CultureMech occurrence total, SSSOM row, and aggregate copy
agree. The material gap is that `TRACE_ELEMENT` is supported solely by a
provisional in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:53503`,
  `ontology_mapping.ontology_id: CHEBI:53503`,
  `ontology_label: cobalt chloride hexahydrate`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:53503` returns active `CHEBI:53503` labelled
  `cobalt chloride hexahydrate` with CAS RN `7791-13-1`, formula
  `2Cl.Co.6H2O`, and the same InChI and SMILES stored in
  `chemical_properties`.
- `reports/hydrate_grounding.tsv` classifies the record as an
  `OK_HYDRATE_TERM`, and `mappings/hydrate_review.tsv` classifies the named
  hexahydrate as a correct `CHEBI:53503` grounding.

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
  `reports` found the active exact `MIM:Cobalt_chloride_hexahydrate` SSSOM row,
  the OAK/OLS row-review confirmation, the hydrate audits, and matching
  aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `CHEBI:53503` on this active record and the rejected
  `Cocl2_X_6_H2o` duplicate, plus expected stock-solution `component_id`
  references.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 2636 rows for
  `CHEBI:53503` whose occurrence weights sum to 2638, matching the explicit
  2636/2638 `occurrence_statistics`.
- The final SSSOM `other` column contains hydrate-specific cobalt chloride
  labels, the merged `CoCl2 x 6 H2O` label, and the matching `CAS:7791-13-1`
  value.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `claude_in_session_curation` and is explicitly marked "Provisional
  in-session LLM role assignment; review recommended."

## Completeness

- The CAS-derived ChEBI identifier, CAS RN, formula, InChI, SMILES, hydrate
  review, SSSOM row, aggregate copy, docs row, and occurrence count are
  populated and agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml`, either
  replace `nutritional_roles.TRACE_ELEMENT` with inspected evidence for cobalt
  chloride hexahydrate as a trace element in this media scope, or remove the
  role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
