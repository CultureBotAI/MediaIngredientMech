# `data/ingredients/mapped/Metall_Salt_Sol_44.yaml`

## Verdict

Needs curation. The local stock-solution identity, fallback registry row, and
occurrence count pass, but the active `STOCK_SOLUTION` record still has no
component list or formulation-specific evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Metall_Salt_Sol_44.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:metall_salt_sol_44` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:metall_salt_sol_44`,
  label `Metall salt sol. 44`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Occurrences: one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meso-Erythritol` through `Methane`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local
  `kgmicrobe.ingredient` record because it is intentionally outside the OBO
  adapter scope.

## Evidence

- A fresh exact all-ontology OLS4 search for `Metall salt sol. 44` returned
  zero results, matching the #288 fallback-registry decision.
- The #288 evidence correctly treats this as a local named multi-component
  preparation with no public ontology term and no single-compound ChEBI parent.
- The final SSSOM publishes one registry `skos:exactMatch` row from
  `MIM:Metall_Salt_Sol_44` to
  `kgmicrobe.ingredient:metall_salt_sol_44` with empty `other`.

## Completeness

- The record was promoted while explicitly pending a component list and
  formulation-specific curation. That gap remains: the YAML has no
  `components` list for the salts in solution 44.

## Recommended Edits

- Curate the solution 44 formulation into `components`, including salts,
  quantities, and source evidence, or add a bounded note identifying the exact
  source table that must be inspected before the components can be filled.
