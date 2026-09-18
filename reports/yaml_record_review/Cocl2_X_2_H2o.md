# `data/ingredients/mapped/Cocl2_X_2_H2o.yaml`

## Verdict

Needs curation; major. The cobalt dichloride dihydrate row correctly uses the
local `kgmicrobe.compound:cocl2_x_2_h2o` registry identifier and a
`CLOSE_MATCH` to anhydrous `CHEBI:35696` while no exact ChEBI term is available.
Its formula and 5/5 occurrence count are corrected, but anhydrous synonyms and
anhydrous InChI/SMILES values still remain on the active hydrate record.

## Identity

- Reviewed record: `data/ingredients/mapped/Cocl2_X_2_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:cocl2_x_2_h2o`,
  `ontology_mapping.ontology_id: CHEBI:35696`,
  `ontology_label: cobalt dichloride`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:35696`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS exact search for `CoCl2 x 2 H2O` returns no ChEBI class, agreeing
  with the local registry fallback.
- `reports/hydrate_grounding.tsv` classifies the record as
  `OK_LOCAL_REGISTRY_ID`.
- `mappings/hydrate_review.tsv` classifies the named dihydrate as a correct
  local kg-microbe identity and warns against inheriting the anhydrous parent
  CAS identity.

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
  `reports` found the close-match `MIM:Cocl2_X_2_H2o` SSSOM row, its local
  registry identity row, the hydrate audits, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `kgmicrobe.compound:cocl2_x_2_h2o` only as this record's `identifier`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 5 rows for
  `kgmicrobe.compound:cocl2_x_2_h2o` whose occurrence weights sum to 5,
  matching the explicit 5/5 `occurrence_statistics`.
- The record's formula was corrected to `2Cl.Co.2H2O`, but the InChI and SMILES
  fields still encode anhydrous `CHEBI:35696`.
- The active `cobalt(2+) chloride` and `cobalt(II) chloride` exact synonyms are
  anhydrous ChEBI exact synonyms that still reach the close-match SSSOM row for
  this dihydrate.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The local identifier, close-match parent, corrected formula, registry SSSOM
  identity row, aggregate copy, docs row, hydrate review, and occurrence count
  are populated and agree.
- The active gaps are stale anhydrous structure fields, stale anhydrous
  synonyms, and the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cocl2_X_2_H2o.yaml`, remove or correct the
  anhydrous InChI/SMILES fields, remove the anhydrous cobalt chloride exact
  synonyms, and either replace `nutritional_roles.TRACE_ELEMENT` with inspected
  evidence for the dihydrate in this media scope or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
