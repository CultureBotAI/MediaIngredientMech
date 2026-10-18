# `data/ingredients/mapped/Menadione_Solution.yaml`

## Verdict

Pass. The local stock-solution identity, narrow parent mapping to menadione,
occurrence count, and final SSSOM registry rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Menadione_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:menadione_solution` with
  `ontology_mapping.ontology_id: CHEBI:28869`, label `menadione`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Occurrences: one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Melibiose` through `Menaquinone`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this
  `kgmicrobe.ingredient`-primary record because it is intentionally outside the
  OBO adapter scope.

## Evidence

- EBI OLS4 resolves the parent `CHEBI:28869` as active `menadione`.
- Fresh exact all-ontology OLS4 and PubChem name searches for `Menadione
  solution` returned no exact public term, supporting the local registry
  treatment.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` also found no exact OLS
  hit for the stock-solution label before the record was promoted through the
  manual #288 stock-solution path.
- The final SSSOM publishes the expected `skos:narrowMatch` parent row to
  `CHEBI:28869` and registry `skos:exactMatch` rows for the local
  stock-solution identity, with empty `other`.

## Completeness

- The record does not assert unsupported roles, component concentrations, or
  non-exact public synonyms for the solution.

## Recommended Edits

- None.
