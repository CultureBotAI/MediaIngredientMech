# `data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml`

## Verdict

Needs curation. The local stock-solution identity, close parent mapping to
hydrate-specific ChEBI, occurrence count, and final exact
`kgmicrobe.ingredient` row are consistent, but a backfilled unrelated compound
label still publishes as a final SSSOM synonym.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution` with
  `ontology_mapping.ontology_id: CHEBI:91248`, label
  `L-cysteine hydrochloride hydrate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- The MIM subject denotes a prepared L-cysteine hydrochloride hydrate solution;
  its exact identity is therefore local while the ChEBI row remains a close
  parent compound row.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml data/ingredients/mapped/L-Deoxyalliin.yaml data/ingredients/mapped/L-Galactose.yaml data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Glutathione.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:91248` as active `L-cysteine hydrochloride hydrate`
  and lists hydrate-specific synonyms including
  `L-cysteine hydrochloride monohydrate`, supporting the #321 parent repair.
- `reports/hydrate_grounding.tsv` reports `OK_LOCAL_REGISTRY_ID` for
  `kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution`, so the final local
  registry row is expected.
- The final SSSOM publishes the expected `skos:closeMatch` row to
  `CHEBI:91248` and the exact row to
  `kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution`.
- Major: the final SSSOM `other` column still publishes
  `QSY9 succinimidyl ester(1+)`. That labels a succinimidyl ester compound, not
  L-cysteine hydrochloride hydrate solution. The other backfilled raw string,
  `(add to make medium anoxic)`, is correctly filtered out of the final SSSOM.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, exact final SSSOM rows,
  docs projections, hydrate-review rows, hydrate-grounding rows, and subject
  alias regression coverage.

## Completeness

- The local identifier, close ChEBI parent mapping, exact local registry row,
  hydrate-review status, occurrence count, and aggregate copy are present and
  consistent.
- The published synonym surface is incomplete until the unrelated QSY9 synonym
  is removed or retagged so it no longer exports in final SSSOM `other`.

## Recommended Edits

- Major: remove or demote `QSY9 succinimidyl ester(1+)` in
  `data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml`, then
  regenerate the aggregate, browser export, docs data, and final SSSOM so it no
  longer publishes for `MIM:L-Cysteine_X_HCl_X_H2O_Solution`.
- Rerun strict, term, round-trip, hydrate, component, and SSSOM validation after
  the synonym repair.
