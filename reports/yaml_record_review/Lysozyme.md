# `data/ingredients/mapped/Lysozyme.yaml`

## Verdict

Pass. The CAS-primary lysozyme record, narrow FOODON parent mapping, exact CAS
and local registry rows, and final SSSOM output are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lysozyme.yaml`.
- Identifier and grounding: `identifier: cas:2650-88-3` with
  `ontology_mapping.ontology_id: FOODON:03413135`, label `lysozyme`, source
  `FOODON`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `2650-88-3`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lydimycin` through `Lysozyme`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `FOODON:03413135` as active `lysozyme`.
- PubChem does not resolve CAS RN `2650-88-3` to a CID, and the record does not
  assert a structure.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `FOODON:03413135` and exact rows to `cas:2650-88-3` and
  `kgmicrobe.ingredient:lysozyme`.

## Completeness

- The CAS primary identifier, FOODON parent mapping, CAS sibling row, local
  registry sibling row, aggregate copy, and final SSSOM rows are present and
  consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
