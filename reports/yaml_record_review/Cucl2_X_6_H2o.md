# `data/ingredients/mapped/Cucl2_X_6_H2o.yaml`

## Verdict

Needs curation; major. The malformed MediaDive 6-water copper chloride label is
correctly retained as a local `kgmicrobe.compound` identity with
`CHEBI:49553` only as the anhydrous close parent, but its `TRACE_ELEMENT` role
is still backed only by a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Cucl2_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:cucl2_x_6_h2o`,
  `ontology_mapping.ontology_id: CHEBI:49553`,
  `ontology_label: copper(II) chloride`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookups for `CuCl2 x 6 H2O` and `copper(II) chloride
  hexahydrate` found no exact CHEBI class, so the local registry identity is
  still warranted.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using
  `kgmicrobe.compound:cucl2_x_6_h2o` as a primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cucl2_X_2_H2o.yaml data/ingredients/mapped/Cucl2_X_5_H2o.yaml data/ingredients/mapped/Cucl2_X_6_H2o.yaml data/ingredients/mapped/Cumene_Hydroperoxide.yaml data/ingredients/mapped/Curamycin_A.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cucl2_X_2_H2o.yaml data/ingredients/mapped/Cucl2_X_5_H2o.yaml data/ingredients/mapped/Cumene_Hydroperoxide.yaml data/ingredients/mapped/Curamycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `Cucl2_X_6_H2o` was intentionally skipped because its local
  `kgmicrobe.compound` primary identifier and close ChEBI parent are outside
  this CHEBI-focused exact-label validation pass.
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

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the paired final SSSOM rows:
  `MIM:Cucl2_X_6_H2o skos:closeMatch CHEBI:49553` and the sibling
  `skos:exactMatch kgmicrobe.compound:cucl2_x_6_h2o` registry row.
- `mappings/culturemech_recipe_membership.tsv` contains eight
  `kgmicrobe.compound:cucl2_x_6_h2o` rows and a total occurrence sum of 8,
  matching `occurrence_statistics` `8/8`.
- `mappings/hydrate_review.tsv` agrees with the local-identity decision:
  the source label is unresolved and should stay local with no exact formula,
  CAS, InChI, or SMILES until the malformed MediaDive hydration count is
  corrected upstream.
- Anhydrous and wrong-hydrate labels are stored as `REJECTED_LABEL` and no
  longer appear in final SSSOM `other`; the retained compact 6-water label is a
  same-subject surface for the local unresolved source identity.
- Major: `nutritional_roles.TRACE_ELEMENT` uses
  `reference_type: COMPUTATIONAL_PREDICTION` with `reference_text: Inferred
  from curated media-role name pattern`. No inspected source is attached to the
  role-level claim.

## Completeness

- The local registry identifier, parent CHEBI close match, empty
  `chemical_properties`, paired SSSOM rows, aggregate copy, and occurrence
  count are populated and agree.
- The remaining cleanup gap is role evidence, not identity.

## Recommended Edits

- Major: either replace the provisional `TRACE_ELEMENT` evidence in
  `data/ingredients/mapped/Cucl2_X_6_H2o.yaml` with a source-backed
  `DATABASE_ENTRY`, or drop the role if the CultureMech rows do not actually
  support this unresolved label as the mineral or trace element source.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
