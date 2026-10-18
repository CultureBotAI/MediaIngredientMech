# `data/ingredients/mapped/Mnso4_X_6_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:131523` manganese sulfate hexahydrate
identity, structure, hydrate grounding, occurrence count, and final exact row
pass, but the trace-element role is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mnso4_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131523` with
  `ontology_mapping.ontology_id: CHEBI:131523`, label
  `manganese(II) sulfate hexahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: three CultureMech recipe occurrences.
- Chemical identity: formula `6H2O.Mn.O4S`, SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_1_H2o` through `Mnso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the three other active CHEBI-primary records in the same batch.

## Evidence

- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm
  `MIM:Mnso4_X_6_H2o` to `CHEBI:131523`.
- A fresh EBI OLS4 lookup resolves `CHEBI:131523` as active
  `manganese(II) sulfate hexahydrate`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mnso4_X_6_H2o` to `CHEBI:131523`.

## Completeness

- The hexahydrate target, formula, 3/3 occurrence count, hydrate audit, and
  final exact row agree.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that MnSO4 x 6 H2O is used as a trace
  element source in media, or remove the provisional `TRACE_ELEMENT` role.
