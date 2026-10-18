# `data/ingredients/mapped/Ornithine.yaml`

## Verdict

Pass. The MicrobeDecoder generic `Ornithine` label exact-maps to active
generic `CHEBI:18257` ornithine, and the record does not export the bad
D/L-ornithine synonym that was already flagged on the distinct
`D-ornithine` record.

## Identity

- Reviewed record: `data/ingredients/mapped/Ornithine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18257` with
  `ontology_mapping.ontology_id: CHEBI:18257`, label `ornithine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 295 MicrobeDecoder `BacDive_Metabolite_utilization`
  source-column occurrences and zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:18257` as active `ornithine` and
  reports the same generic formula, InChI, SMILES, and mass stored in the
  YAML.
- The MicrobeDecoder review table marks `Ornithine.yaml` approved after an OAK
  canonical-label check, and the live OLS term confirms the same generic
  target.
- The final SSSOM row maps `MIM:Ornithine` exactly to `CHEBI:18257`, has no
  `other` tokens, and carries the manual MicrobeDecoder review stamp.
- No unsupported synonyms, roles, components, supplied forms, or environmental
  contexts are asserted.

## Completeness

- The active ChEBI term, canonical label, formula, structure, source occurrence
  count, and final SSSOM row agree.
- L-ornithine, D-ornithine, and L-ornithine monohydrochloride remain distinct
  records, so this record preserves the generic label's specificity.

## Recommended Edits

- None.
