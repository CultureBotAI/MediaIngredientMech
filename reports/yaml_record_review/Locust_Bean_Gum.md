# `data/ingredients/mapped/Locust_Bean_Gum.yaml`

## Verdict

Pass. The CAS-primary locust bean gum identity, FOODON parent mapping, exact CAS
and kgmicrobe registry rows, and empty final synonym payload are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Locust_Bean_Gum.yaml`.
- Identifier and grounding: `identifier: cas:9000-40-2` with
  `ontology_mapping.ontology_id: FOODON:03413132`, label `locust bean gum`,
  source `FOODON`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `9000-40-2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Locust_Bean_Gum` through `Loratadine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `FOODON:03413132` as active `locust bean gum`.
- PubChem lookup by CAS RN `9000-40-2` found no CID, so the record correctly
  leaves structure fields empty.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `FOODON:03413132`, an exact CAS registry row to `cas:9000-40-2`, and an exact
  registry sibling row to `kgmicrobe.ingredient:locust_bean_gum`.
- The registry-row `other` fields contain only `CAS:9000-40-2`; the FOODON
  parent row has an empty `other` field.

## Completeness

- The active FOODON parent identity, CAS RN, aggregate copy, and final SSSOM
  registry rows are present and consistent.

## Recommended Edits

- None.
