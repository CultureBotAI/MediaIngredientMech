# `data/ingredients/mapped/PIPES_Buffer.yaml`

## Verdict

Needs curation; major. The PIPES buffer stock-solution identity passes, but the
final SSSOM also emits a `kgmicrobe.compound:pipes_buffer` exact row for a
non-compound local subject.

## Identity

- Reviewed record: `data/ingredients/mapped/PIPES_Buffer.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:pipes_buffer`
  with `ontology_mapping.ontology_id: CHEBI:39033`, label `PIPES`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Occurrences: 4 CultureMech occurrences across 4 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 lookup resolves `CHEBI:39033` as active `PIPES`.
- The final SSSOM rows were inspected directly: the record publishes the
  `CHEBI:39033` parent row, the correct
  `kgmicrobe.ingredient:pipes_buffer` exact registry row, and an incorrect
  `kgmicrobe.compound:pipes_buffer` exact registry row.

## Evidence

- The curated mapping note explicitly models `PIPES buffer` as a prepared
  solution of the compound PIPES, not as the compound itself, so the
  `NARROW_MATCH` edge to `CHEBI:39033` preserves the stock-solution boundary.
- The final `CHEBI:39033` parent row keeps only `PIPES buffer (Sigma)` in
  `other`. That CultureMech catalog surface was curated as a same-stock-solution
  `CATALOG_VARIANT`, so it can remain exported.
- The generated `kgmicrobe.compound:pipes_buffer` exact row is wrong for this
  subject. A PIPES buffer is a non-single-compound prepared ingredient, and the
  needed local exact row already exists as
  `kgmicrobe.ingredient:pipes_buffer`.

## Completeness

- The record has the CHEBI parent and local ingredient identity needed for a
  stock solution whose exact public ontology term is absent.
- No role or component evidence is being asserted, so there is no unsupported
  claim beyond the generated compound-namespace SSSOM row.

## Recommended Edits

- Major: update the final SSSOM registry-row generation path so broad/narrow
  rows for `ingredient_type: STOCK_SOLUTION` records use
  `kgmicrobe.ingredient:<slug>` and do not emit
  `kgmicrobe.compound:<slug>`. Rebuild `mappings/ingredient_mappings.sssom.tsv`
  and rerun `scripts/validate_sssom_invariants.py` to prove
  `MIM:PIPES_Buffer` keeps only the CHEBI parent and
  `kgmicrobe.ingredient:pipes_buffer` exact registry row.
