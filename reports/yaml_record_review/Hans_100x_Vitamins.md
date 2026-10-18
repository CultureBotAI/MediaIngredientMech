# `data/ingredients/mapped/Hans_100x_Vitamins.yaml`

## Verdict

Pass. The local fallback identity correctly represents a named vitamin stock
solution with no single-compound parent, and the final SSSOM preserves that
local identity without publishing a broader ontology match.

## Identity

- Reviewed record: `data/ingredients/mapped/Hans_100x_Vitamins.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:hans_100x_vitamins` with the same local
  `ontology_mapping.ontology_id`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: VITAMIN_MIX`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hans_100x_Vitamins.yaml data/ingredients/mapped/Harmaline.yaml data/ingredients/mapped/Harmalol.yaml data/ingredients/mapped/Harmane.yaml data/ingredients/mapped/Harmine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because the primary
  `kgmicrobe.ingredient` CURIE is local to MIM and outside the OBO/CAS scope
  of this check.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- The 2026-05-11 review classified `Hans 100x vitamins` as a concentrated
  vitamin stock or pre-mix pending component-level recipe curation.
- The `promote_resolved_unmapped` event promoted the accepted local registry
  identity to `MAPPED` under the MIM stock-solution convention.
- The current `ontology_mapping` records that no searched ontology term denotes
  this named multi-component preparation and that the record should mint a
  `kgmicrobe.ingredient` identity without a parent because the stock does not
  narrow to any single compound.
- The final SSSOM publishes one exact local registry row from
  `MIM:Hans_100x_Vitamins` to
  `kgmicrobe.ingredient:hans_100x_vitamins`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found this active YAML, matching
  aggregate copies, generated products, and the final SSSOM row.

## Completeness

- The local primary identifier, local ontology mapping, stock-solution
  classification, notes, and final SSSOM row are present and consistent.
- The absence of components is explicit in the current curation state rather
  than masked by a false parent or single-compound identity.

## Recommended Edits

- None.
