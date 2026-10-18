# `data/ingredients/mapped/MES_Buffer.yaml`

## Verdict

Pass. The local stock-solution identity, narrow MES parent mapping, exact local
registry rows, CultureMech occurrence count, aggregate copy, and final SSSOM
rows are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/MES_Buffer.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:mes_buffer` with
  `ontology_mapping.ontology_id: CHEBI:39010`, label `MES`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Chemical properties: none asserted.
- Occurrences: 6 total occurrences in 6 CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `M-inositol` through `MES_sodium_salt`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `M-inositol`, `M-xylene`, and `MES_sodium_salt`;
  `MES_Buffer` and `MES_Hydrat` were skipped because their primary identifiers
  use local and CAS prefixes outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:39010` as active `MES`.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `CHEBI:39010` and exact registry rows to
  `kgmicrobe.ingredient:mes_buffer` and `kgmicrobe.compound:mes_buffer`.
- The raw `MES buffer` synonym is not exported into the final SSSOM `other`
  payload.

## Completeness

- The stock-solution local identity, CHEBI parent, occurrence count, aggregate
  copy, and three final SSSOM rows are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
