# `data/ingredients/mapped/Norepinephrine.yaml`

## Verdict

Pass. The CAS-backed `(-)-Norepinephrine` record exact-maps to active
`CHEBI:18357` with matching formula, structure, reviewed synonym, and final
SSSOM payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Norepinephrine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18357` with
  `ontology_mapping.ontology_id: CHEBI:18357`, label `(R)-noradrenaline`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:18357` as active
  `(R)-noradrenaline` with formula `C8H11NO3`, CAS `51-41-2`, and the same
  InChI and SMILES as the record.
- The final SSSOM row maps `MIM:Norepinephrine` exactly to `CHEBI:18357`; its
  `other` values are the reviewed ChEBI synonym plus `CAS:51-41-2`.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, CAS lookup grade,
  and final exact row agree.
- Empty occurrence statistics are expected for this CultureBotHT source record.

## Recommended Edits

- None.
