# `data/ingredients/mapped/Nordihydroguaretic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed `Nordihydroguaretic Acid` record exact-maps
to active `CHEBI:73468` masoprocol with matching formula, structure, ChEBI
synonym, and final SSSOM payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Nordihydroguaretic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:73468` with
  `ontology_mapping.ontology_id: CHEBI:73468`, label `masoprocol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:73468` as active `masoprocol` with
  formula `C18H22O4`, CAS values including `500-38-9`, and the same InChI and
  SMILES as the record.
- The final SSSOM row maps `MIM:Nordihydroguaretic_Acid` exactly to
  `CHEBI:73468`; its `other` values are the reviewed ChEBI synonym plus
  `CAS:500-38-9`.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, and final SSSOM
  row agree.
- Empty occurrence statistics are expected for this CultureBotHT source record.

## Recommended Edits

- None.
