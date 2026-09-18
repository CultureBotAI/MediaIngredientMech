# `data/ingredients/mapped/Mncl2_X_2_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:131395` manganese chloride dihydrate
identity, structure, hydrate grounding, occurrence count, and final SSSOM row
pass, but the trace-element role is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mncl2_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131395` with
  `ontology_mapping.ontology_id: CHEBI:131395`, label
  `manganese(II) chloride dihydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 40 CultureMech recipe occurrences.
- Chemical identity: formula `Cl2Mn.2H2O`, SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mncl2` through `Mnso4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for all five
  CHEBI-primary records in the same batch.

## Evidence

- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- A fresh EBI OLS4 lookup resolves `CHEBI:131395` as active
  `manganese(II) chloride dihydrate`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mncl2_X_2_H2o` to `CHEBI:131395`.

## Completeness

- The dihydrate target, formula, 40/40 occurrence count, hydrate audit, and
  final exact row agree.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that MnCl2 x 2 H2O is used as a trace
  element source in media, or remove the provisional `TRACE_ELEMENT` role.
