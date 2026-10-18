# `data/ingredients/mapped/Sodium_Thiosulfate_Pentahydrate.yaml`

## Verdict

Pass. This is a rejected duplicate of the formula-named
`Na2S2O3 x 5 H2O` pentahydrate survivor; it points at the same active
`CHEBI:32150` identity and emits no final SSSOM row.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_Thiosulfate_Pentahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:32150` with
  `ontology_mapping.ontology_id: CHEBI:32150`, label
  `sodium thiosulfate pentahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: this tombstone has `0` occurrences after the #414 merge into the
  live `Na2S2O3 x 5 H2O` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Thiosulfate_Pentahydrate` through `Soil`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:32150` with label
  `sodium thiosulfate pentahydrate` and CAS `10102-17-7`.
- Fresh PubChem lookup for CAS `10102-17-7` resolves to sodium thiosulfate
  pentahydrate with the same hydrate InChI and SMILES as the record.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active survivor at
  `data/ingredients/mapped/Na2s2o3_X_5_H2o.yaml` and no final SSSOM row for
  `MIM:Sodium_Thiosulfate_Pentahydrate`.

## Completeness

- The rejected duplicate keeps its provenance and no longer carries any
  occurrences that would be lost from the live record.
- The catalog-specific surface form and provisional `ELECTRON_DONOR` role
  inherited by the live survivor are already tracked in the
  `Na2s2o3_X_5_H2o` review report.

## Recommended Edits

- None for this record.
