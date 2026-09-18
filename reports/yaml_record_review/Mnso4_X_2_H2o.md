# `data/ingredients/mapped/Mnso4_X_2_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:86356` manganese sulfate dihydrate identity,
structure, hydrate grounding, occurrence count, and final exact row pass, but
concentration-qualified labels still publish in final SSSOM `other`, and the
trace-element role is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mnso4_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86356` with
  `ontology_mapping.ontology_id: CHEBI:86356`, label
  `manganese(II) sulfate dihydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 42 CultureMech recipe occurrences.
- Chemical identity: formula `2H2O.Mn.O4S`, SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_1_H2o` through `Mnso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the three other active CHEBI-primary records in the same batch.

## Evidence

- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- A fresh EBI OLS4 lookup resolves `CHEBI:86356` as active
  `manganese(II) sulfate dihydrate`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mnso4_X_2_H2o` to `CHEBI:86356`.

## Completeness

- The dihydrate target, formula, 42/42 occurrence count, hydrate audit, and
  final exact row agree.
- The final SSSOM `other` field still exports hydrate labels that include
  source concentrations rather than synonym text.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: mark concentration-qualified MnSO4 x 2 H2O strings as
  `REJECTED_LABEL`, or otherwise filter them from final SSSOM `other`.
- Major: add source-backed evidence that MnSO4 x 2 H2O is used as a trace
  element source in media, or remove the provisional `TRACE_ELEMENT` role.
