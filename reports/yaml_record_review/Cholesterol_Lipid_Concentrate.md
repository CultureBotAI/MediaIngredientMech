# `data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml`

## Verdict

Pass. The record intentionally preserves `cholesterol lipid concentrate` as a
local stock-solution identity with a `skos:narrowMatch` parent row to
`CHEBI:16113` cholesterol, registry identity rows, a 2/2 CultureMech
occurrence count, and agreeing aggregate and SSSOM exports.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:cholesterol_lipid_concentrate`,
  `ontology_mapping.ontology_id: CHEBI:16113`,
  `ontology_label: cholesterol`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Direct ChEBI inspection of `CHEBI:16113` confirms active `cholesterol`.
  Keeping the stock solution under a distinct `kgmicrobe.ingredient` identity
  and only linking it narrowly to cholesterol is therefore more specific than
  collapsing the solution record to the single compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chocolate_agar.yaml data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Cholin_Acetate.yaml data/ingredients/mapped/Choline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Choline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this narrowed run.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active narrow parent SSSOM row to `CHEBI:16113`, the
  companion exact `kgmicrobe.ingredient` and Rule B1 `kgmicrobe.compound`
  registry rows, and matching aggregate/docs rows.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found exactly two recipe
  membership rows for
  `kgmicrobe.ingredient:cholesterol_lipid_concentrate`, matching the record's
  2/2 occurrence statistics.
- The batch review warning that the ontology label differs from the preferred
  term is stale for this record: the label differs because the maintained
  mapping is intentionally `NARROW_MATCH` to a parent compound while exact
  identity is held by the `kgmicrobe.ingredient` registry row.
- The record carries no formula, role, component, or environment assertions
  that would overstate the exact composition of the stock solution.

## Completeness

- The local stock-solution identifier, CHEBI parent, raw input synonym,
  occurrence count, registry SSSOM rows, aggregate copy, and docs rows are
  populated and agree.

## Recommended Edits

- None for this record.
