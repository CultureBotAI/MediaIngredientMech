# `data/ingredients/mapped/Chu_Stock_Solution.yaml`

## Verdict

Needs curation, major. The local stock-solution identity remains appropriate
and current OLS has no exact ontology term for `Chu Stock Solution`, but the
record is asserted to be a multi-component preparation and still lacks both a
component list and a refreshed, recipe-specific CultureMech occurrence row.

## Identity

- Reviewed record: `data/ingredients/mapped/Chu_Stock_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:chu_stock_solution`,
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:chu_stock_solution`,
  `ontology_label: Chu Stock Solution`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `preferred_term: Chu Stock Solution`.
- Live exact OLS lookup for `Chu Stock Solution` found 0 ontology hits,
  matching the `MIM curation (#114)` decision to mint a local stock-solution
  identity rather than map the mixture to a single compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chrysanthemic_Acid_Ethyl_Ester.yaml data/ingredients/mapped/Chrysarobin.yaml data/ingredients/mapped/Chrysin.yaml data/ingredients/mapped/Chrysophanol.yaml data/ingredients/mapped/Chu_Stock_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chrysanthemic_Acid_Ethyl_Ester.yaml data/ingredients/mapped/Chrysarobin.yaml data/ingredients/mapped/Chrysin.yaml data/ingredients/mapped/Chrysophanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all four CHEBI-scoped records in this batch. `Chu_Stock_Solution`
  was intentionally skipped because its `kgmicrobe.ingredient` placeholder
  CURIE is a local registry ID outside Engine A's OBO prefix scope.
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
  `reports` found the active exact local `MIM:Chu_Stock_Solution` SSSOM row and
  matching aggregate/docs rows.
- Hidden/ignored-inclusive search found only stale pre-promotion `UNMAPPED_0112`
  audit rows for the source label; it found no current
  `kgmicrobe.ingredient:chu_stock_solution` row in
  `mappings/culturemech_recipe_membership.tsv`.
- The `MIM curation (#114)` evidence says this is a named, recurring
  multi-component preparation used in 1 medium. The record has no `components`
  list, so a curator cannot recover the actual Chu stock-solution composition
  from the active YAML.
- The record carries no role or environment claims.

## Completeness

- The local stock-solution identifier, fallback SSSOM row, aggregate copy, and
  docs rows agree.
- The active record is incomplete for a named multi-component stock solution:
  it needs component entries or a source-level discussion explaining why the
  component list cannot yet be recovered, plus a refreshed CultureMech
  membership row or other recipe-specific occurrence trail for the retained 1/1
  count.

## Recommended Edits

- In `data/ingredients/mapped/Chu_Stock_Solution.yaml`, add evidence-backed
  `components` for the Chu stock solution if the source recipe gives the
  composition; otherwise add a focused discussion that records the exact source
  checked and the reason the component list remains unresolved.
- Refresh the CultureMech occurrence mapping so the 1/1 `occurrence_statistics`
  value can be traced to a concrete source recipe, then rerun strict
  validation, component partonomy validation, aggregate/roundtrip verification,
  and `scripts/validate_sssom_invariants.py`.
