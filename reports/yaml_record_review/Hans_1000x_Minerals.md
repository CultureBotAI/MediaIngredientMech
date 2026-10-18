# `data/ingredients/mapped/Hans_1000x_Minerals.yaml`

## Verdict

Pass. The local fallback identity correctly represents a named mineral stock
solution with no single-compound parent, and the final SSSOM preserves that
local identity without publishing a broader ontology match.

## Identity

- Reviewed record: `data/ingredients/mapped/Hans_1000x_Minerals.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:hans_1000x_minerals` with the same local
  `ontology_mapping.ontology_id`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H3bo3.yaml data/ingredients/mapped/HOMOPIPES.yaml data/ingredients/mapped/Haemin.yaml data/ingredients/mapped/Halomicin.yaml data/ingredients/mapped/Hans_1000x_Minerals.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because the primary
  `kgmicrobe.ingredient` CURIE is local to MIM and outside the OBO/CAS scope
  of this check.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- The 2026-05-11 review classified `Hans 1000x minerals` as a concentrated
  mineral stock or pre-mix pending component-level recipe curation.
- The `promote_resolved_unmapped` event promoted the accepted local registry
  identity to `MAPPED` under the MIM stock-solution convention.
- The current `ontology_mapping` records that no searched ontology term denotes
  this named multi-component preparation and that the record should mint a
  `kgmicrobe.ingredient` identity without a parent because the stock does not
  narrow to any single compound.
- The final SSSOM publishes one exact local registry row from
  `MIM:Hans_1000x_Minerals` to
  `kgmicrobe.ingredient:hans_1000x_minerals`.

## Completeness

- The local primary identifier, local ontology mapping, stock-solution
  classification, notes, and final SSSOM row are present and consistent.
- The absence of components is explicit in the current curation state rather
  than masked by a false parent or single-compound identity.

## Recommended Edits

- None.
