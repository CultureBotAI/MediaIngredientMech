# `data/ingredients/mapped/Mnso4_X_5_H2o.yaml`

## Verdict

Pass. The exact `CHEBI:131524` manganese sulfate pentahydrate identity, CAS,
source-backed trace-element role, hydrate grounding, occurrence count, and
final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mnso4_X_5_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131524` with
  `ontology_mapping.ontology_id: CHEBI:131524`, label
  `manganese(II) sulfate pentahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 41 CultureMech recipe occurrences.
- Chemical identity: CAS `13465-27-5`, formula `5H2O.Mn.O4S`, SMILES, and
  InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_1_H2o` through `Mnso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the three other active CHEBI-primary records in the same batch.

## Evidence

- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm
  `MIM:Mnso4_X_5_H2o` to `CHEBI:131524`.
- A fresh EBI OLS4 lookup resolves `CHEBI:131524` as active
  `manganese(II) sulfate pentahydrate`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mnso4_X_5_H2o` to `CHEBI:131524`.

## Completeness

- The pentahydrate target, CAS, formula, 41/41 occurrence count, hydrate audit,
  supported role, and final exact row agree.
- The raw `Role:`/`Properties:` imports are filtered from final SSSOM `other`.

## Recommended Edits

- None.
