# `data/ingredients/mapped/Nystatin.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-maps to active `CHEBI:7660` nystatin,
and the record does not export unsupported synonyms or roles.

## Identity

- Reviewed record: `data/ingredients/mapped/Nystatin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7660` with
  `ontology_mapping.ontology_id: CHEBI:7660`, label `nystatin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 27 MicrobeDecoder source-column occurrences across
  `BacDive_Antibiotic_resistance` and `BacDive_Antibiotic_sensitivity`, with
  zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7660` as active `nystatin` and
  reports the same generalized formula `C47H75NO17` and mass `926.107` carried
  in `chemical_properties`.
- The MicrobeDecoder review table marks `Nystatin.yaml` approved after an OAK
  canonical-label check, and the live OLS term confirms that the lexical match
  lands on the intended nystatin antibiotic entry.
- The final SSSOM row maps `MIM:Nystatin` exactly to `CHEBI:7660`, has no
  `other` tokens, and carries the manual MicrobeDecoder review stamp.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, canonical label, generalized formula, mass, and final
  SSSOM row agree.
- The hidden and ignored-inclusive search over `mappings`, `reports`,
  `data/ingredients`, and `data/curated` found no open row-review artifact for
  `CHEBI:7660` or `Nystatin` beyond the historical MicrobeDecoder approval.

## Recommended Edits

- None.
