# `data/ingredients/mapped/N-methylhydantoin.yaml`

## Verdict

Pass. The exact `CHEBI:16354` N-methylhydantoin identity, PubChem CAS
provenance, occurrence count, ChEBI synonyms, structure, and final exact row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-methylhydantoin.yaml`.
- Identifier and grounding: `identifier: CHEBI:16354` with
  `ontology_mapping.ontology_id: CHEBI:16354`, label `N-methylhydantoin`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: four CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-lauroylsarcosine_Sodium_Salt` through
  `NNNN-Tetramethylethylenediamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:16354` as active
  `N-methylhydantoin`, with `cas:616-04-6`, formula `C4H6N2O2`, the stored
  InChI/SMILES, and the curated ChEBI synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-methylhydantoin` to `CHEBI:16354` with same-substance synonyms and
  `CAS:616-04-6` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, 4/4 occurrence count, accepted
  synonyms, and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
