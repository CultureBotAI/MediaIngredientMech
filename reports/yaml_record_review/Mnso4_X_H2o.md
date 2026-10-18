# `data/ingredients/mapped/Mnso4_X_H2o.yaml`

## Verdict

Pass. The exact `CHEBI:86364` manganese sulfate monohydrate identity, CAS,
structure, source-backed trace-element role, occurrence count, and final SSSOM
row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mnso4_X_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86364` with
  `ontology_mapping.ontology_id: CHEBI:86364`, label
  `manganese(II) sulfate monohydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:86364`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1,183 total occurrences across 1,179 CultureMech recipes.
- Chemical identity: CAS `10034-96-5`, formula `H2O.Mn.O4S`, SMILES, and
  InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_7_H2o` through `Modified_Trace_Vitamins`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm
  `MIM:Mnso4_X_H2o` to `CHEBI:86364`.
- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- A fresh EBI OLS4 lookup resolves `CHEBI:86364` as active
  `manganese(II) sulfate monohydrate`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mnso4_X_H2o` to `CHEBI:86364`.

## Completeness

- The monohydrate target, CAS, formula, 1,183/1,179 occurrence count, supported
  role, and final exact row agree.
- The raw `Role:`/`Properties:` imports are filtered from final SSSOM `other`.

## Recommended Edits

- None.
