# `data/ingredients/mapped/N-Acetyl-D-galactosamine.yaml`

## Verdict

Pass. The exact `CHEBI:28037` N-acetyl-D-galactosamine identity, CultureBotHT
CAS provenance, structure, ChEBI synonym, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-Acetyl-D-galactosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28037` with
  `ontology_mapping.ontology_id: CHEBI:28037`, label
  `N-acetyl-D-galactosamine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Myo-inositol` through `N-Acetyl-D-glucosamine_6-phosphate_Sodium_Salt`:
  exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:28037` as active
  `N-acetyl-D-galactosamine` and exposes the stored IUPAC name as an exact
  synonym.
- A fresh PubChem lookup for CAS `1811-31-0` returns formula `C8H15NO6` and the
  same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-Acetyl-D-galactosamine` to `CHEBI:28037` with the ChEBI IUPAC synonym
  and `CAS:1811-31-0` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, synonym, and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
