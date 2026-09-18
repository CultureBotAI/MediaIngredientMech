# `data/ingredients/mapped/PBS.yaml`

## Verdict

Needs curation; major. The generic PBS stock-solution record correctly uses a
local `kgmicrobe.ingredient:pbs` identity with a parent `NCIT:C178908` row, but
the final SSSOM also publishes an erroneous `kgmicrobe.compound:pbs` identity
row.

## Identity

- Reviewed record: `data/ingredients/mapped/PBS.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:pbs` with
  `ontology_mapping.ontology_id: NCIT:C178908`, label
  `Dulbecco's Phosphate-Buffered Saline`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: BUFFER_SOLUTION`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO label validation was skipped for this mixed NCIT plus local
  `kgmicrobe.ingredient` record.
- The final SSSOM rows were inspected directly: the record publishes the
  NCIT parent row, the correct `kgmicrobe.ingredient:pbs` registry row, and an
  incorrect `kgmicrobe.compound:pbs` registry row.

## Evidence

- A fresh EBI OLS4 NCIT lookup resolves `NCIT:C178908` as active
  `Dulbecco's Phosphate-Buffered Saline` and lists `PBS` and
  `Phosphate-Buffered Saline` as exact NCIT synonyms.
- The curated YAML primary identifier already uses the non-chemical local
  namespace `kgmicrobe.ingredient:pbs`, which matches the
  `STOCK_SOLUTION`/`BUFFER_SOLUTION` classification.
- The final SSSOM row for `NCIT:C178908` keeps `Phosphate-buffered saline` in
  `other`, which is a legitimate same-buffer synonym for the local PBS record.
- The generated `kgmicrobe.compound:pbs` exact row is not legitimate for this
  subject. PBS is a prepared buffer solution, not a single compound; the needed
  local exact row already exists as `kgmicrobe.ingredient:pbs`.

## Completeness

- The NCIT parent row and local ingredient identity row together preserve the
  generic PBS subject and the available public term.
- The record remains component-unresolved for a generic PBS preparation; that
  is less important than removing the wrong compound-namespace row.

## Recommended Edits

- Major: update the final SSSOM registry-row generation path so broad/narrow
  rows for `ingredient_type: STOCK_SOLUTION` records use
  `kgmicrobe.ingredient:<slug>` and do not emit
  `kgmicrobe.compound:<slug>`. Rebuild `mappings/ingredient_mappings.sssom.tsv`
  and rerun `scripts/validate_sssom_invariants.py` to prove
  `MIM:PBS` keeps only the NCIT parent and the `kgmicrobe.ingredient:pbs`
  exact registry row.
