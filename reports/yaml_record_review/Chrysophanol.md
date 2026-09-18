# `data/ingredients/mapped/Chrysophanol.yaml`

## Verdict

Pass. The CultureBotHT record is exactly grounded to active `CHEBI:3687`
`chrysophanol`; its CAS, formula, InChI, SMILES, exact synonym, SSSOM row, zero
occurrence count, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chrysophanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:3687`,
  `ontology_mapping.ontology_id: CHEBI:3687`,
  `ontology_label: chrysophanol`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup for `Chrysophanol` returns active `CHEBI:3687` labelled
  `chrysophanol` with `1,8-dihydroxy-3-methyl-9,10-anthraquinone` as an exact
  synonym.
- PubChem lookup of CAS `481-74-3` resolves to CID `10208` with formula
  `C15H10O4` and the same standard InChI stored in the record.

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
  `reports` found the active exact `MIM:Chrysophanol` SSSOM row, OAK/OLS
  row-review confirmation, matching aggregate/docs rows, and no QC report entry
  that flags this record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` plus active per-record YAML and
  review reports found no `CHEBI:3687` membership rows, matching the explicit
  0/0 media-recipe occurrence statistics.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, exact synonym, zero
  occurrence count, SSSOM row, aggregate copy, and docs row are populated and
  agree.

## Recommended Edits

- None for this record.
