# `data/ingredients/mapped/Mncl2_X_4_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:86368` manganese chloride tetrahydrate
identity, CAS, structure, hydrate grounding, occurrence count, and final exact
row pass, but malformed `MnCl4` labels still publish in final SSSOM `other`,
and the trace-element role is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mncl2_X_4_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86368` with
  `ontology_mapping.ontology_id: CHEBI:86368`, label
  `manganese(II) chloride tetrahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2,990 CultureMech recipe occurrences.
- Chemical identity: CAS `13446-34-9`, formula `Cl2Mn.4H2O`, SMILES, and
  InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mncl2` through `Mnso4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for all five
  CHEBI-primary records in the same batch.

## Evidence

- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- A fresh EBI OLS4 lookup resolves `CHEBI:86368` as active
  `manganese(II) chloride tetrahydrate`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mncl2_X_4_H2o` to `CHEBI:86368`.

## Completeness

- The tetrahydrate target, CAS, structure, 2,990/2,990 occurrence count,
  hydrate audit, and final exact row agree.
- The final SSSOM `other` field still exports malformed `MnCl4` 4-water
  aliases that were retained only as raw absorbed spellings of MnCl2 x 4 H2O.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: mark the `MnCl4` 4-water strings as `REJECTED_LABEL`, or otherwise
  filter them from final SSSOM `other`.
- Major: add source-backed evidence that MnCl2 x 4 H2O is used as a trace
  element source in media, or remove the provisional `TRACE_ELEMENT` role.
