# `data/ingredients/mapped/Sorbose.yaml`

## Verdict

Pass. The MicrobeDecoder-imported exact `CHEBI:27922` sorbose identity and final
SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sorbose.yaml`.
- Identifier and grounding: `identifier: CHEBI:27922` with
  `ontology_mapping.ontology_id: CHEBI:27922`, label `sorbose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: 4 source occurrences from the MicrobeDecoder
  `BacDive_Metabolite_utilization` column.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soil_Extract` through `Sorbose`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:27922` with label `sorbose`.
- The record was auto-grounded by OLS label-exact matching and then promoted by
  the MicrobeDecoder review pass.
- Final SSSOM publishes one exact ChEBI row with no unsafe `other` payload.

## Completeness

- The ChEBI ID, label, MicrobeDecoder source occurrence count, review history,
  and final exact row agree.
- Optional synonym, role, component, and chemical-property fields are correctly
  empty.

## Recommended Edits

- None.
