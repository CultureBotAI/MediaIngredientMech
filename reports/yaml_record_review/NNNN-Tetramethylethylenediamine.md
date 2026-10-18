# `data/ingredients/mapped/NNNN-Tetramethylethylenediamine.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:32850` tetramethylethylenediamine identity,
CultureBotHT CAS provenance, ChEBI synonym, structure, and final exact row
pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/NNNN-Tetramethylethylenediamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:32850` with
  `ontology_mapping.ontology_id: CHEBI:32850`, ASCII ChEBI label
  `N,N,N',N'-tetramethylethylenediamine`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-lauroylsarcosine_Sodium_Salt` through
  `NNNN-Tetramethylethylenediamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32850` as active
  `N,N,N',N'-tetramethylethylenediamine`, with `cas:110-18-9`, formula
  `C6H16N2`, the stored InChI/SMILES, and the accepted IUPAC synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:NNNN-Tetramethylethylenediamine` to `CHEBI:32850`, preserving the
  ASCII ChEBI object label and exporting only same-substance `other` values:
  the IUPAC synonym and `CAS:110-18-9`.

## Completeness

- The active ChEBI target, CAS RN, structure, accepted synonym, and final row
  agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
